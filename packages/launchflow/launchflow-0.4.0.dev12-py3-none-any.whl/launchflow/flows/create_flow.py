import asyncio
import dataclasses
import datetime
import io
import logging
import os
import time
from functools import cached_property
from typing import Any, Dict, List, Literal, Optional, Tuple, Union

import beaupy
import deepdiff
import rich
import yaml
from rich.console import Console
from rich.live import Live
from rich.table import Table

from launchflow import exceptions
from launchflow.cli.resource_utils import deduplicate_resources, is_local_resource
from launchflow.clients.docker_client import docker_service_available
from launchflow.config import config
from launchflow.docker.resource import DockerResource
from launchflow.flows.flow_logger_v2 import OperationsLiveView
from launchflow.locks import Lock, LockInfo, LockOperation, OperationType, ReleaseReason
from launchflow.managers.environment_manager import EnvironmentManager
from launchflow.managers.resource_manager import ResourceManager
from launchflow.managers.service_manager import ServiceManager
from launchflow.models.enums import CloudProvider, ResourceStatus, ServiceStatus
from launchflow.models.flow_state import EnvironmentState, ResourceState, ServiceState
from launchflow.models.launchflow_uri import LaunchFlowURI
from launchflow.node import Node
from launchflow.resource import Resource
from launchflow.service import Service
from launchflow.validation import validate_resource_name, validate_service_name
from launchflow.workflows.apply_resource_tofu.create_tofu_resource import (
    create_tofu_resource,
)
from launchflow.workflows.apply_resource_tofu.schemas import ApplyResourceTofuInputs
from launchflow.workflows.manage_docker.manage_docker_resources import (
    create_docker_resource,
    replace_docker_resource,
)
from launchflow.workflows.manage_docker.schemas import CreateResourceDockerInputs

_RESOURCE_COLOR = "light_goldenrod3"
_SERVICE_COLOR = "blue"
_ENVIRONMENT_COLOR = "bold purple"
_OP_COLOR = "bold pale_green3"
_DEPENDS_ON_COLOR = "yellow"


class _ResourceRef:
    def __init__(self, resource: Resource):
        self.resource = resource

    def __str__(self):
        return f"[{_RESOURCE_COLOR}]{self.resource}[/{_RESOURCE_COLOR}]"


class _ServiceRef:
    def __init__(self, service: Service):
        self.service = service

    def __str__(self):
        return f"[{_SERVICE_COLOR}]{self.service}[/{_SERVICE_COLOR}]"


class _EnvironmentRef:
    def __init__(self, environment_manager: EnvironmentManager):
        self.environment_manager = environment_manager

    def __str__(self):
        return f"[{_ENVIRONMENT_COLOR}]{self.environment_manager.project_name}/{self.environment_manager.environment_name}[/{_ENVIRONMENT_COLOR}]"


def _dump_verbose_logs(logs_file: str, title: str):
    rich.print(f"───── {title} ─────")
    with open(logs_file, "r") as f:
        print(f.read())
    rich.print(f"───── End of {title} ─────\n")


def _compare_dicts(d1, d2):
    diff = deepdiff.DeepDiff(d1, d2, ignore_order=True)
    diff_keys = diff.affected_root_keys
    diff_strs = []
    for key in diff_keys:
        old_value = d1.get(key)
        new_value = d2.get(key)
        diff_strs.append(f"[cyan]{key}[/cyan]: {old_value} -> {new_value}")
    return "\n    ".join(diff_strs)


def _dump_resource_inputs(resource_inputs: Dict[str, Any]):
    return yaml.safe_dump(resource_inputs).replace("'", "")


# This plan type is used to represent something that failed to plan, usually due to a
# validation error
@dataclasses.dataclass
class FailedPlan:
    resource_or_service: Union[Resource, Service]
    error_message: str


# TODO: create a base class for these plan types. Might need to call FailedPlan
# something else since not every func supports them.
@dataclasses.dataclass
class CreateResourcePlan:
    resource: Resource
    resource_manager: ResourceManager
    existing_resource_state: Optional[ResourceState]
    environment_state: EnvironmentState
    _lock: Optional[Lock] = None

    @cached_property
    def operation_type(self) -> Literal["noop", "create", "update", "replace"]:
        operation_type = "noop"
        if (
            self.existing_resource_state is None
            or self.existing_resource_state.status == ResourceStatus.CREATE_FAILED
        ):
            return "create"
        existing_resource_inputs = {}
        if self.existing_resource_state is not None:
            existing_resource_inputs = self.existing_resource_state.inputs or {}
        new_resource_inputs = self.resource.inputs(
            self.environment_state.environment_type
        ).to_dict()
        resource_diff = deepdiff.DeepDiff(
            existing_resource_inputs,
            new_resource_inputs,
            ignore_order=True,
        )
        if resource_diff.affected_root_keys:
            operation_type = "update"
            for key in resource_diff.affected_root_keys:
                if key in self.resource.replacement_arguments:
                    operation_type = "replace"
                    break
        return operation_type

    def print_plan(
        self,
        console: rich.console.Console = rich.console.Console(),
        left_padding: int = 0,
    ):
        left_padding_str = " " * left_padding
        if self.existing_resource_state is None or (
            self.existing_resource_state.inputs is None
            and self.existing_resource_state.status == ResourceStatus.CREATE_FAILED
        ):
            resource_inputs = self.resource.inputs(
                self.environment_state.environment_type
            ).to_dict()
            if resource_inputs:
                resource_inputs_str = _dump_resource_inputs(resource_inputs)
                console.print(
                    f"{left_padding_str}{_ResourceRef(self.resource)} will be [{_OP_COLOR}]created[/{_OP_COLOR}] with the following configuration:"
                )
                console.print(
                    left_padding_str
                    + "    "
                    + f"\n{left_padding_str}    ".join(resource_inputs_str.split("\n"))
                )
            else:
                # TODO: Print the default configuration instead of this message
                console.print(
                    f"{left_padding_str}{_ResourceRef(self.resource)} will be [{_OP_COLOR}]created[/{_OP_COLOR}] with the default configuration."
                )
                console.print()
        else:
            args_diff = _compare_dicts(
                self.existing_resource_state.inputs,
                self.resource.inputs(self.environment_state.environment_type).to_dict(),
            )
            if args_diff:
                op_msg = "updated"
                if self.operation_type == "replace":
                    op_msg = "replaced"
                console.print(
                    f"{left_padding_str}{_ResourceRef(self.resource)} will be [{_OP_COLOR}]{op_msg}[/{_OP_COLOR}] with the following updates:\n    {args_diff}"
                )
            console.print()

        if self.resource.depends_on:
            console.print(
                f"{left_padding_str}    [{_DEPENDS_ON_COLOR}]Depends on:[/{_DEPENDS_ON_COLOR}]"
            )
            for dep in self.resource.depends_on:
                console.print(
                    f"{left_padding_str}        [{_RESOURCE_COLOR}]{dep}[/{_RESOURCE_COLOR}]"
                )
            console.print()

    def task_description(self):
        if self.operation_type == "create":
            return f"Creating {_ResourceRef(self.resource)}..."
        if self.operation_type == "update":
            return f"Updating {_ResourceRef(self.resource)}..."
        if self.operation_type == "replace":
            return f"Replacing {_ResourceRef(self.resource)}..."
        return f"Running unknown operation for {_ResourceRef(self.resource)}..."

    def pending_message(self):
        return f"{_ResourceRef(self.resource)} waiting for dependencies..."

    def success_message(self):
        if self.operation_type == "create":
            return f"Successfully created {_ResourceRef(self.resource)}"
        if self.operation_type == "update":
            return f"Successfully updated {_ResourceRef(self.resource)}"
        if self.operation_type == "replace":
            return f"Successfully replaced {_ResourceRef(self.resource)}"
        return f"Successfully ran unknown operation for {_ResourceRef(self.resource)}"

    def failure_message(self):
        return f"Failed to {self.operation_type} {_ResourceRef(self.resource)}"

    # TODO: Make this a context manager
    async def lock_plan(self) -> bool:
        if self._lock is not None:
            # TODO: Create a custom exception for this
            raise RuntimeError("This plan is already locked.")

        op_type = OperationType.CREATE_RESOURCE
        if self.operation_type == "update":
            op_type = OperationType.UPDATE_RESOURCE
        elif self.operation_type == "replace":
            op_type = OperationType.REPLACE_RESOURCE
        plan_output = io.StringIO()
        console = Console(no_color=True, file=plan_output)
        self.print_plan(console)
        plan_output.seek(0)
        try:
            lock = await self.resource_manager.lock_resource(
                operation=LockOperation(
                    operation_type=op_type, metadata={"plan": plan_output.read()}
                ),
            )
        except Exception as e:
            # TODO: Improve this error handling
            logging.error("Exception occurred: %s", e, exc_info=True)
            return False
        try:
            refreshed_resource_state = await self.resource_manager.load_resource()
        except exceptions.ResourceNotFound:
            refreshed_resource_state = None
        if self.existing_resource_state != refreshed_resource_state:
            # If the resource has changed since planning we release the lock
            # and will not attempt to execute the plan
            await lock.release(lock.lock_info.lock_id, reason=ReleaseReason.ABANDONED)
            return False

        self._lock = lock
        return True

    async def unlock_plan(self, reason: ReleaseReason):
        if self._lock is None:
            return
        await self._lock.release(self._lock.lock_info.lock_id, reason=reason)
        self._lock = None

    def get_lock(self) -> Lock:
        if self._lock is None:
            raise RuntimeError("This plan is not locked.")
        return self._lock


@dataclasses.dataclass
class CreateResourceResult:
    plan: CreateResourcePlan
    resource_state: ResourceState
    logs_file: Optional[str] = None

    def successful(self) -> bool:
        return self.resource_state.status == ResourceStatus.READY


@dataclasses.dataclass
class CreateServicePlan:
    service: Service
    service_manager: ServiceManager
    existing_service_state: Optional[ServiceState]
    environment_state: EnvironmentState
    resource_plans: List[CreateResourcePlan]
    _lock: Optional[Lock] = None

    @cached_property
    def operation_type(self) -> Literal["noop", "create", "update"]:
        operation_type = "noop"
        if (
            self.existing_service_state is None
            or self.existing_service_state.status == ServiceStatus.CREATE_FAILED
        ):
            return "create"
        for resource_plan in self.resource_plans:
            if resource_plan.operation_type == "create":
                operation_type = "create"
            elif (
                resource_plan.operation_type == "replace"
                or resource_plan.operation_type == "update"
            ):
                operation_type = "update"
                break
        # We only need to run these checks if the operation type is "noop" or "create"
        if operation_type != "update":
            existing_service_inputs = {}
            if self.existing_service_state is not None:
                existing_service_inputs = self.existing_service_state.inputs or {}
            new_service_inputs = self.service.inputs().to_dict()
            service_diff = deepdiff.DeepDiff(
                existing_service_inputs,
                new_service_inputs,
                ignore_order=True,
            )
            if service_diff.affected_root_keys:
                operation_type = "update"
        return operation_type

    def print_plan(
        self,
        console: rich.console.Console = rich.console.Console(),
        left_padding: int = 0,
    ):
        left_padding_str = " " * left_padding
        if self.existing_service_state is None or (
            self.existing_service_state.status == ServiceStatus.CREATE_FAILED
        ):
            console.print(
                f"{left_padding_str}{_ServiceRef(self.service)} will be [{_OP_COLOR}]created[/{_OP_COLOR}] with the following Resources:"
            )
            for resource_plan in self.resource_plans:
                resource_plan.print_plan(console, left_padding=left_padding + 4)

        else:
            op_msg = "created"
            if self.operation_type == "update":
                op_msg = "updated"
            console.print(
                f"{_ServiceRef(self.service)} will be [{_OP_COLOR}]{op_msg}[/{_OP_COLOR}] with the following Resource updates:\n"
            )
            for resource_plan in self.resource_plans:
                resource_plan.print_plan(console, left_padding=left_padding + 4)
            console.print()

    def task_description(self):
        if self.operation_type == "create":
            return f"Creating {_ServiceRef(self.service)}..."
        if self.operation_type == "update":
            return f"Updating {_ServiceRef(self.service)}..."
        if self.operation_type == "replace":
            return f"Replacing {_ServiceRef(self.service)}..."

    def success_message(self):
        if self.operation_type == "create":
            return f"Successfully created {_ServiceRef(self.service)}"
        if self.operation_type == "update":
            return f"Successfully updated {_ServiceRef(self.service)}"
        if self.operation_type == "replace":
            return f"Successfully replaced {_ServiceRef(self.service)}"

    def failure_message(self):
        return f"Failed to {self.operation_type} {_ServiceRef(self.service)}"

    # TODO: Make this a context manager
    async def lock_plan(self) -> bool:
        if self._lock is not None:
            # TODO: Create a custom exception for this
            raise RuntimeError("This plan is already locked.")

        op_type = OperationType.CREATE_SERVICE
        if self.operation_type == "update":
            op_type = OperationType.UPDATE_SERVICE
        plan_output = io.StringIO()
        console = Console(no_color=True, file=plan_output)
        self.print_plan(console)
        plan_output.seek(0)
        try:
            lock = await self.service_manager.lock_service(
                operation=LockOperation(
                    operation_type=op_type, metadata={"plan": plan_output.read()}
                ),
            )
        except Exception as e:
            # TODO: Improve this error handling
            logging.error("Exception occurred: %s", e, exc_info=True)
            return False
        try:
            refreshed_service_state = await self.service_manager.load_service()
        except exceptions.ServiceNotFound:
            refreshed_service_state = None
        if self.existing_service_state != refreshed_service_state:
            # If the service has changed since planning we release the lock
            # and will not attempt to execute the plan
            await lock.release(lock.lock_info.lock_id, reason=ReleaseReason.ABANDONED)
            return False

        lock_resource_tasks = []
        for resource_plan in self.resource_plans:
            lock_resource_tasks.append(resource_plan.lock_plan())
        lock_resource_results = await asyncio.gather(*lock_resource_tasks)
        if not all(lock_resource_results):
            # If any of the resource plans fail to lock, we release the resource locks
            # and then release the service lock
            unlock_resource_tasks = []
            for resource_plan in self.resource_plans:
                unlock_resource_tasks.append(
                    resource_plan.unlock_plan(ReleaseReason.ABANDONED)
                )
            await asyncio.gather(*unlock_resource_tasks)
            await lock.release(lock.lock_info.lock_id, reason=ReleaseReason.ABANDONED)
            return False

        self._lock = lock
        return True

    async def unlock_plan(self, reason: ReleaseReason):
        if self._lock is None:
            return
        unlock_resource_tasks = []
        for resource_plan in self.resource_plans:
            unlock_resource_tasks.append(resource_plan.unlock_plan(reason))
        await asyncio.gather(*unlock_resource_tasks)
        await self._lock.release(self._lock.lock_info.lock_id, reason=reason)
        self._lock = None

    def get_lock(self) -> Lock:
        if self._lock is None:
            raise RuntimeError("This plan is not locked.")
        return self._lock


@dataclasses.dataclass
class CreateServiceResult:
    plan: CreateServicePlan
    service_state: ServiceState
    resource_results: List[CreateResourceResult]

    def successful(self) -> bool:
        return self.service_state.status == ServiceStatus.READY


async def _create_or_update_tofu_resource(
    new_resource_state: ResourceState,
    plan: CreateResourcePlan,
    environment: EnvironmentState,
    launchflow_uri: LaunchFlowURI,
    lock_info: LockInfo,
    logs_file: str,
) -> ResourceState:
    inputs = ApplyResourceTofuInputs(
        launchflow_uri=launchflow_uri,
        backend=plan.resource_manager.backend,
        gcp_env_config=environment.gcp_config,
        aws_env_config=environment.aws_config,
        resource=new_resource_state,
        lock_id=lock_info.lock_id,
        logs_file=logs_file,
    )

    to_save = new_resource_state.model_copy()
    try:
        outputs = await create_tofu_resource(inputs)
        to_save.aws_arn = outputs.aws_arn
        to_save.gcp_id = outputs.gcp_id
        to_save.status = ResourceStatus.READY
    except Exception as e:
        # TODO: Log this to the logs_file
        with open(logs_file, "a") as f:
            f.write(str(e))
        # logging.error("Exception occurred: %s", e, exc_info=True)
        # Reset the create args to their original state
        if to_save.status == ResourceStatus.CREATING:
            to_save.inputs = None
            to_save.status = ResourceStatus.CREATE_FAILED
        elif to_save.status == ResourceStatus.REPLACING:
            to_save.inputs = plan.existing_resource_state.inputs
            to_save.status = ResourceStatus.REPLACE_FAILED
        else:
            to_save.inputs = plan.existing_resource_state.inputs
            to_save.status = ResourceStatus.UPDATE_FAILED

    return to_save


async def _create_or_update_docker_resource(
    plan: CreateResourcePlan,
    new_resource_state: ResourceState,
    operation_type: str,
    logs_file: str,
) -> ResourceState:
    resource: DockerResource = plan.resource

    inputs = CreateResourceDockerInputs(
        resource=new_resource_state,
        image=resource.docker_image,
        env_vars=resource.env_vars,
        command=resource.command,
        ports=resource.ports,
        logs_file=logs_file,
        environment_name=plan.resource_manager.environment_name,
        resource_inputs=resource.inputs().to_dict(),
    )

    to_save = new_resource_state.model_copy()
    if operation_type == "create":
        fn = create_docker_resource
    elif operation_type == "update":
        fn = replace_docker_resource
    else:
        raise NotImplementedError(f"Got an unexpected operator type {operation_type}.")
    try:
        outputs = await fn(inputs)

        resource.ports.update(outputs.ports)
        resource.running_container_id = outputs.container.id

        to_save.status = ResourceStatus.READY
    except Exception as e:
        logging.error("Exception occurred: %s", e, exc_info=True)
        # Reset the create args to their original state
        if to_save.status == ResourceStatus.CREATING:
            to_save.inputs = None
            to_save.status = ResourceStatus.CREATE_FAILED
        else:
            to_save.inputs = plan.existing_resource_state.inputs
            to_save.status = ResourceStatus.UPDATE_FAILED

    return to_save


async def plan_create_resource(
    resource: Resource,
    environment_state: EnvironmentState,
    environment_manager: EnvironmentManager,
) -> Union[CreateResourcePlan, FailedPlan]:
    try:
        validate_resource_name(resource.name)
    except exceptions.InvalidResourceName as e:
        return FailedPlan(
            resource_or_service=resource,
            error_message=str(e),
        )

    if resource.product.cloud_provider() == CloudProvider.GCP:
        if environment_state.gcp_config is None:
            return FailedPlan(
                resource_or_service=resource,
                error_message="CloudProviderMismatch: Cannot use a GCP Resource in an AWS Environment.",
            )
    elif resource.product.cloud_provider() == CloudProvider.AWS:
        if environment_state.aws_config is None:
            return FailedPlan(
                resource_or_service=resource,
                error_message="CloudProviderMismatch: Cannot use an AWS Resource in a GCP Environment.",
            )

    if is_local_resource(resource):
        resource_manager = environment_manager.create_docker_resource_manager(
            resource.name
        )
    else:
        resource_manager = environment_manager.create_resource_manager(resource.name)
    try:
        existing_resource_state = await resource_manager.load_resource()
    except exceptions.ResourceNotFound:
        existing_resource_state = None

    if (
        existing_resource_state is not None
        and existing_resource_state.product != resource.product
    ):
        exception = exceptions.ResourceProductMismatch(
            existing_product=existing_resource_state.product.name,
            new_product=resource.product,
        )
        return FailedPlan(
            resource_or_service=resource,
            error_message=str(exception),
        )

    # Determine the operation type using the existing resource state

    # Return the plan
    return CreateResourcePlan(
        resource=resource,
        resource_manager=resource_manager,
        existing_resource_state=existing_resource_state,
        environment_state=environment_state,
    )


async def plan_create_service(
    service: Service,
    environment: EnvironmentState,
    environment_manager: EnvironmentManager,
) -> Union[CreateServicePlan, FailedPlan]:
    try:
        validate_service_name(service.name)
    except ValueError as e:
        return FailedPlan(
            resource_or_service=service,
            error_message=str(e),
        )

    if service.product.cloud_provider() == CloudProvider.GCP:
        if environment.gcp_config is None:
            return FailedPlan(
                resource_or_service=service,
                error_message="CloudProviderMismatch: Cannot use a GCP Service in an AWS Environment.",
            )
    elif service.product.cloud_provider() == CloudProvider.AWS:
        if environment.aws_config is None:
            return FailedPlan(
                resource_or_service=service,
                error_message="CloudProviderMismatch: Cannot use an AWS Service in a GCP Environment.",
            )

    service_manager = environment_manager.create_service_manager(service.name)
    try:
        existing_service = await service_manager.load_service()
    except exceptions.ServiceNotFound:
        existing_service = None

    if existing_service is not None and existing_service.product != service.product:
        exception = exceptions.ServiceProductMismatch(
            existing_product=existing_service.product.name,
            new_product=service.product,
        )
        return FailedPlan(
            resource_or_service=service,
            error_message=str(exception),
        )

    # Plan the resources for the service
    resource_plan_tasks = []
    for resource in service.resources():
        resource_plan_tasks.append(
            plan_create_resource(
                resource=resource,
                environment_state=environment,
                environment_manager=environment_manager,
            )
        )
    resource_plans: List[Union[CreateResourcePlan, FailedPlan]] = await asyncio.gather(
        *resource_plan_tasks
    )
    if any(isinstance(plan, FailedPlan) for plan in resource_plans):
        return FailedPlan(
            resource_or_service=service,
            error_message="One or more child Resources failed to plan.",
        )

    return CreateServicePlan(
        service=service,
        service_manager=service_manager,
        existing_service_state=existing_service,
        environment_state=environment,
        resource_plans=resource_plans,
    )


async def plan_create(
    *nodes: Node,
    environment: EnvironmentState,
    environment_manager: EnvironmentManager,
) -> List[Union[CreateResourcePlan, CreateServicePlan, FailedPlan]]:
    plan_tasks = []
    for node in nodes:
        if isinstance(node, Resource):
            plan_tasks.append(
                plan_create_resource(
                    resource=node,
                    environment_state=environment,
                    environment_manager=environment_manager,
                )
            )
        elif isinstance(node, Service):
            plan_tasks.append(
                plan_create_service(
                    service=node,
                    environment=environment,
                    environment_manager=environment_manager,
                )
            )
        else:
            raise ValueError(f"Unknown node type {node}")
    return await asyncio.gather(*plan_tasks)


def print_plans(
    *plans: Union[CreateResourcePlan, CreateServicePlan, FailedPlan],
    environment_manager: EnvironmentManager,
    console: rich.console.Console = rich.console.Console(),
):
    failed_plans: List[FailedPlan] = []
    noop_plans: List[Union[CreateResourcePlan, CreateServicePlan]] = []
    valid_plans: List[Union[CreateResourcePlan, CreateServicePlan]] = []
    for plan in plans:
        if isinstance(plan, FailedPlan):
            failed_plans.append(plan)
        elif plan.operation_type == "noop":
            noop_plans.append(plan)
        else:
            valid_plans.append(plan)

    # First we print the failed plans above the plan section
    for plan in failed_plans:
        if isinstance(plan.resource_or_service, Resource):
            console.print(
                f"[red]✗[/red] {_ResourceRef(plan.resource_or_service)} failed to plan:\n    {plan.error_message}"
            )
        elif isinstance(plan.resource_or_service, Service):
            console.print(
                f"[red]✗[/red] {_ServiceRef(plan.resource_or_service)} failed to plan:\n    {plan.error_message}"
            )

    # Then we print the noop plans
    for plan in noop_plans:
        if isinstance(plan, CreateResourcePlan):
            if plan.operation_type == "noop":
                console.print(
                    f"[green]✓[/green] {_ResourceRef(plan.resource)} is up to date."
                )
        elif isinstance(plan, CreateServicePlan):
            if plan.operation_type == "noop":
                console.print(
                    f"[green]✓[/green] {_ServiceRef(plan.service)} is up to date."
                )

    if valid_plans:
        # Finally we print the plan section with plans that have work to do
        console.rule("[bold purple]plan")
        console.print()
        console.print(
            f"The following infrastructure changes will happen in {_EnvironmentRef(environment_manager)}:\n"
        )
        for plan in valid_plans:
            plan.print_plan(console)


async def select_plans(
    *plans: Union[CreateResourcePlan, CreateServicePlan, FailedPlan],
    environment_manager: EnvironmentManager,
    console: rich.console.Console = rich.console.Console(),
    confirm: bool = True,
) -> Union[None, List[Union[CreateResourcePlan, CreateServicePlan]]]:
    failed_plans: List[FailedPlan] = []
    noop_plans: List[Union[CreateResourcePlan, CreateServicePlan]] = []
    valid_plans: List[Union[CreateResourcePlan, CreateServicePlan]] = []
    for plan in plans:
        if isinstance(plan, FailedPlan):
            failed_plans.append(plan)
        elif plan.operation_type == "noop":
            noop_plans.append(plan)
        else:
            valid_plans.append(plan)

    print_plans(*plans, environment_manager=environment_manager, console=console)

    if not valid_plans:
        return None  # The None is used to indicate that no valid plans were found

    if len(valid_plans) == 1:
        selected_plan = valid_plans[0]
        if isinstance(selected_plan, CreateResourcePlan):
            entity_ref = f"resource {_ResourceRef(selected_plan.resource)}"
        elif isinstance(selected_plan, CreateServicePlan):
            entity_ref = f"service {_ServiceRef(selected_plan.service)}"
        else:
            raise NotImplementedError(
                f"Got an unexpected plan type {type(selected_plan)}."
            )

        if not confirm:
            return [selected_plan]

        selected_plan.print_plan(left_padding=2)
        answer = beaupy.confirm(
            f"[bold]{selected_plan.operation_type.capitalize()}[/bold] {entity_ref} in {_EnvironmentRef(environment_manager)}?"
        )
        if not answer:
            return []
        return [selected_plan]

    if not confirm:
        return valid_plans

    console.print(
        f"Select the plans you want to execute in {_EnvironmentRef(environment_manager)}:"
    )

    def preprocessor(plan: Union[CreateResourcePlan, CreateServicePlan]):
        if isinstance(plan, CreateResourcePlan):
            return f"[bold]{plan.operation_type.capitalize()}[/bold] resource {_ResourceRef(plan.resource)}"
        elif isinstance(plan, CreateServicePlan):
            return f"[bold]{plan.operation_type.capitalize()}[/bold] service {_ServiceRef(plan.service)}"
        else:
            raise NotImplementedError(f"Got an unexpected plan type {type(plan)}.")

    selected_plans: List[
        Union[CreateResourcePlan, CreateServicePlan]
    ] = beaupy.select_multiple(
        options=valid_plans,
        preprocessor=preprocessor,
    )
    for plan in selected_plans:
        if isinstance(plan, CreateResourcePlan):
            console.print(f"[[pink1]✓[/pink1]] [pink1]{plan.resource}[/pink1]")
        elif isinstance(plan, CreateServicePlan):
            console.print(f"[[pink1]✓[/pink1]] [pink1]{plan.service}[/pink1]")
        else:
            raise NotImplementedError(f"Got an unexpected plan type {type(plan)}.")
        print()
    return selected_plans


# TODO: make this a context manager so that we can ensure that all plans are unlocked,
# even if an error occurs
async def lock_plans(
    *plans: Union[CreateResourcePlan, CreateServicePlan],
    environment_manager: EnvironmentManager,
) -> bool:
    local_plans = []
    remote_plans = []
    for plan in plans:
        if isinstance(plan, CreateResourcePlan) and is_local_resource(plan.resource):
            local_plans.append(plan)
        else:
            remote_plans.append(plan)

    async def _unlock_plans(plans: List[Union[CreateResourcePlan, CreateServicePlan]]):
        unlock_plan_tasks = []
        for plan in plans:
            unlock_plan_tasks.append(plan.unlock_plan(ReleaseReason.ABANDONED))
        await asyncio.gather(*unlock_plan_tasks)

    async def _lock_plans(plans: List[Union[CreateResourcePlan, CreateServicePlan]]):
        lock_plan_tasks = []
        for plan in plans:
            lock_plan_tasks.append(plan.lock_plan())
        results = await asyncio.gather(*lock_plan_tasks)
        if not all(results):
            await _unlock_plans(plans)
            return False
        return True

    local_lock_result = await _lock_plans(local_plans)
    remote_lock_result = True
    if remote_plans:
        async with await environment_manager.lock_environment(
            operation=LockOperation(operation_type=OperationType.LOCK_ENVIRONMENT)
        ):
            remote_lock_result = await _lock_plans(remote_plans)

    return local_lock_result and remote_lock_result


async def _execute_resource_plan(
    plan: CreateResourcePlan,
    verbose: bool,
) -> CreateResourceResult:
    lock = plan.get_lock()
    env_type = plan.environment_state.environment_type
    async with lock as lock_info:
        base_logging_dir = "/tmp/launchflow"
        os.makedirs(base_logging_dir, exist_ok=True)
        logs_file = f"{base_logging_dir}/{plan.resource.name}-{int(time.time())}.log"

        launchflow_uri = LaunchFlowURI(
            project_name=plan.resource_manager.project_name,
            environment_name=plan.resource_manager.environment_name,
            resource_name=plan.resource_manager.resource_name,
        )

        updated_time = datetime.datetime.now(datetime.timezone.utc)
        created_time = (
            plan.existing_resource_state.created_at
            if plan.existing_resource_state
            else updated_time
        )
        if plan.operation_type == "update":
            status = ResourceStatus.UPDATING
        elif plan.operation_type == "replace":
            status = ResourceStatus.REPLACING
        else:
            status = ResourceStatus.CREATING

        new_resource_state = ResourceState(
            name=plan.resource.name,
            product=plan.resource.product,
            cloud_provider=plan.resource.product.cloud_provider(),
            created_at=created_time,
            updated_at=updated_time,
            status=status,
            inputs=plan.resource.inputs(env_type).to_dict(),
            depends_on=[r.name for r in plan.resource.depends_on],
        )
        # Save resource to push status to the backend
        await plan.resource_manager.save_resource(new_resource_state, lock_info.lock_id)

        if is_local_resource(plan.resource):
            to_save = await _create_or_update_docker_resource(
                plan, new_resource_state, plan.operation_type, logs_file
            )
        else:
            to_save = await _create_or_update_tofu_resource(
                new_resource_state,
                plan,
                plan.environment_state,
                launchflow_uri,
                lock_info,
                logs_file,
            )

        await plan.resource_manager.save_resource(to_save, lock_info.lock_id)
        if verbose:
            _dump_verbose_logs(
                logs_file,
                f"Create {plan.resource.__class__.__name__}({plan.resource.name}) logs",
            )
        if to_save.status == ResourceStatus.READY:
            return CreateResourceResult(
                plan=plan,
                resource_state=to_save,
                logs_file=logs_file,
            )

        return CreateResourceResult(
            plan=plan,
            resource_state=to_save,
            logs_file=logs_file,
        )


async def _execute_resource_plans(
    plans: List[CreateResourcePlan],
    environment_manager: EnvironmentManager,
    live_view: OperationsLiveView,
    verbose: bool,
    left_padding: int = 0,
) -> List[CreateResourceResult]:
    resource_name_to_plan: Dict[str, CreateResourcePlan] = {
        plan.resource.name: plan for plan in plans
    }

    tasks: Dict[str, asyncio.Task] = {}

    async def create_with_dependencies(
        dependency: Resource,
    ) -> Union[CreateResourceResult, ResourceState]:
        # Handles the case where a resource depends on a resource that is not in the
        # current plan. This happens when the parent resource was already created.
        dependency_plan = resource_name_to_plan.get(dependency.name)
        if dependency_plan is None:
            resource_manager = environment_manager.create_resource_manager(
                dependency.name
            )
            try:
                return await resource_manager.load_resource()
            except exceptions.ResourceNotFound:
                return None

        if dependency.name in tasks:
            return await tasks[dependency.name]

        async def task():
            with live_view.start(
                dependency_plan.pending_message(), left_padding
            ) as task_id:
                for dep in dependency.depends_on:
                    result = await create_with_dependencies(dep)
                    if isinstance(result, ResourceState):
                        # This happens when a resource depends on remote resources that
                        # are outside of the current plan, but do exists
                        continue
                    # The None case happens when remote resources do NOT exist
                    if result is None or not result.successful():
                        if result is None:
                            live_view.error(
                                f"Dependency for {dependency} not found: {dep}"
                            )
                        live_view.done(
                            task_id,
                            dependency_plan.failure_message(),
                            failed=True,
                        )
                        # TODO: move this to a helper function so its easier to follow
                        updated_at = datetime.datetime.now(datetime.timezone.utc)
                        if dependency_plan.existing_resource_state is not None:
                            to_save = (
                                dependency_plan.existing_resource_state.model_copy()
                            )
                            to_save.updated_at = updated_at
                            if dependency_plan.operation_type == "create":
                                to_save.status = ResourceStatus.CREATE_FAILED
                            elif dependency_plan.operation_type == "replace":
                                to_save.status = ResourceStatus.REPLACE_FAILED
                            else:
                                to_save.status = ResourceStatus.UPDATE_FAILED
                        else:
                            to_save = ResourceState(
                                name=dependency_plan.resource.name,
                                product=dependency_plan.resource.product,
                                cloud_provider=dependency_plan.resource.product.cloud_provider(),
                                status=ResourceStatus.CREATE_FAILED,
                                created_at=updated_at,
                                updated_at=updated_at,
                            )
                        # TODO: move this locking step into the helper function as well
                        lock = dependency_plan.get_lock()
                        async with lock as lock_info:
                            await dependency_plan.resource_manager.save_resource(
                                to_save, lock_info.lock_id
                            )
                        return CreateResourceResult(
                            plan=dependency_plan,
                            resource_state=to_save,
                        )

                live_view.update(task_id, dependency_plan.task_description())
                result = await _execute_resource_plan(dependency_plan, verbose=verbose)
                if result.successful():
                    live_view.done(
                        task_id,
                        dependency_plan.success_message(),
                        failed=False,
                    )
                else:
                    live_view.done(
                        task_id,
                        dependency_plan.failure_message(),
                        failed=True,
                    )
                return result

        tasks[dependency.name] = asyncio.create_task(task())
        return await tasks[dependency.name]

    results = await asyncio.gather(
        *[create_with_dependencies(plan.resource) for plan in plans]
    )
    # filter out the types used for remote resource dependencies
    filtered_results = [r for r in results if isinstance(r, CreateResourceResult)]

    return filtered_results


async def _execute_service_plan(
    plan: CreateServicePlan,
    environment_manager: EnvironmentManager,
    live_view: OperationsLiveView,
    verbose: bool,
) -> CreateServiceResult:
    lock = plan.get_lock()
    with live_view.start(plan.task_description()) as task_id:
        async with lock as lock_info:
            updated_time = datetime.datetime.now(datetime.timezone.utc)
            created_time = (
                plan.existing_service_state.created_at
                if plan.existing_service_state
                else updated_time
            )
            if plan.operation_type == "update":
                status = ServiceStatus.UPDATING
            else:
                status = ServiceStatus.CREATING

            new_service_state = ServiceState(
                name=plan.service.name,
                product=plan.service.product,
                cloud_provider=plan.service.product.cloud_provider(),
                created_at=created_time,
                updated_at=updated_time,
                status=status,
                inputs=plan.service.inputs().to_dict(),
            )
            # Save service to push status to the backend
            await plan.service_manager.save_service(
                new_service_state, lock_info.lock_id
            )

            resource_results = await _execute_resource_plans(
                plan.resource_plans,
                environment_manager,
                live_view,
                verbose,
                left_padding=2,
            )

            # NOTE: We use the primary resource to populate things like gcp_id and aws_arn
            primary_resource = plan.service.primary_resource()
            primary_resource_result = None
            if primary_resource is not None:
                primary_resource_result = next(
                    (
                        r
                        for r in resource_results
                        if r.plan.resource == primary_resource
                    ),
                    None,
                )

            if all(result.successful() for result in resource_results):
                new_service_state.status = ServiceStatus.READY
                # TODO: Determine if we should fail the service if the primary resource is None in this case
                if primary_resource_result is not None:
                    new_service_state.aws_arn = (
                        primary_resource_result.resource_state.aws_arn
                    )
                    new_service_state.gcp_id = (
                        primary_resource_result.resource_state.gcp_id
                    )

                new_service_state.service_url = "TODO"

                live_view.done(task_id, plan.success_message(), failed=False)
            else:
                if new_service_state.status == ServiceStatus.CREATING:
                    new_service_state.status = ServiceStatus.CREATE_FAILED
                else:
                    new_service_state.status = ServiceStatus.UPDATE_FAILED
                live_view.done(task_id, plan.failure_message(), failed=True)

            await plan.service_manager.save_service(
                new_service_state, lock_info.lock_id
            )

            return CreateServiceResult(
                plan=plan,
                service_state=new_service_state,
                resource_results=resource_results,
            )


async def execute_plans(
    *plans: Union[CreateResourcePlan, CreateServicePlan],
    environment_manager: EnvironmentManager,
    verbose: bool = False,
    console: Console = Console(),
) -> List[Union[CreateResourceResult, CreateServiceResult]]:
    resource_plans = []
    service_plans = []
    for plan in plans:
        if isinstance(plan, CreateResourcePlan):
            resource_plans.append(plan)
        elif isinstance(plan, CreateServicePlan):
            service_plans.append(plan)
        else:
            raise ValueError(f"Got an unexpected plan type {type(plan)}.")

    with Live(console=console, refresh_per_second=10) as live:
        create_resource_group_tasks = []

        if resource_plans:
            live_view = OperationsLiveView(live)
            create_resource_group_tasks.append(
                _execute_resource_plans(
                    resource_plans, environment_manager, live_view, verbose
                )
            )

        for service_plan in service_plans:
            live_view = OperationsLiveView(live)
            create_resource_group_tasks.append(
                _execute_service_plan(
                    service_plan, environment_manager, live_view, verbose
                )
            )

        task_results = await asyncio.gather(*create_resource_group_tasks)

        # flatten the results
        results: List[Union[CreateResourceResult, CreateServiceResult]] = []
        for task_result in task_results:
            if isinstance(task_result, list):
                results.extend(task_result)
            else:
                results.append(task_result)

    return results


async def create(
    *nodes: Tuple[Node],
    environment_name: Optional[str] = None,
    prompt: bool = True,
    verbose: bool = False,
    console: Console = Console(),
):
    """
    Create resources in an environment.

    Args:
    - `nodes`: A tuple of Resources and Services to create.
    - `environment_name`: The name of the environment to create resources in. Defaults
        to the env configured in the launchflow.yaml.
    - `prompt`: Whether to prompt the user before creating resources.
    - `verbose`: If true all logs will be written to stdout.
    """
    if not nodes:
        console.print("No resources or services to create. Exiting.")
        return True

    docker_resources: List[DockerResource] = []
    cloud_resources: List[Resource] = []
    cloud_services: List[Service] = []
    for node in nodes:
        if isinstance(node, DockerResource):
            docker_resources.append(node)
        elif isinstance(node, Resource):
            cloud_resources.append(node)
        elif isinstance(node, Service):
            cloud_services.append(node)
        else:
            raise ValueError(f"Got an unexpected node type {type(node)}.")

    docker_resources = deduplicate_resources(docker_resources)
    cloud_resources = deduplicate_resources(cloud_resources)

    if docker_resources and not docker_service_available():
        raise exceptions.MissingDockerDependency(
            "Docker is required to create local resources."
        )

    environment_manager = EnvironmentManager(
        project_name=config.launchflow_yaml.project,
        environment_name=environment_name,
        backend=config.launchflow_yaml.backend,
    )

    environment = await environment_manager.load_environment()

    if (cloud_resources or cloud_services) and (
        environment.gcp_config is None and environment.aws_config is None
    ):
        raise exceptions.EnvironmentNotConnected(environment_manager.environment_name)

    # Step 1: Build the plans
    create_plans = await plan_create(
        *nodes, environment=environment, environment_manager=environment_manager
    )

    # Step 2: Select the plan
    selected_plans = await select_plans(
        *create_plans,
        environment_manager=environment_manager,
        console=console,
        confirm=prompt,
    )
    if selected_plans is None:  # The None is a special case for no valid plans
        console.print("Nothing to create. Exiting.")
        return False

    if (
        not selected_plans
    ):  # The empty list case means the user did not confirm any plans
        console.print("No plans selected. Exiting.")
        return True

    # Step 3: Lock the plans
    # TODO: Determine if we should check if the Environment state has changed since planning
    result = await lock_plans(*selected_plans, environment_manager=environment_manager)
    if not result:
        console.print("Failed to lock all plans. Exiting.")
        return False

    # Step 4: Execute the plans
    console.rule("[bold purple]operations")

    all_results = await execute_plans(
        *selected_plans,
        environment_manager=environment_manager,
        verbose=verbose,
        console=console,
    )
    resource_results = [r for r in all_results if isinstance(r, CreateResourceResult)]
    service_results = [r for r in all_results if isinstance(r, CreateServiceResult)]

    # Step 5: Print the results

    # Step 5.1: Print the logs
    should_print_logs = False
    table = Table(show_header=True, show_edge=False, show_lines=False, box=None)
    table.add_column("Resource", justify="left", no_wrap=True)
    table.add_column("Logs", style="blue")
    if resource_results:
        for result in resource_results:
            if result.logs_file is None:
                continue
            should_print_logs = True

            if result.successful():
                table.add_row(
                    f"[green]✓[/green] {result.plan.operation_type} {_ResourceRef(result.plan.resource)}",
                    result.logs_file,
                )
            else:
                table.add_row(
                    f"[red]✗[/red] {result.plan.operation_type} {_ResourceRef(result.plan.resource)}",
                    result.logs_file,
                )
    if service_results:
        for result in service_results:
            for result in result.resource_results:
                if result.logs_file is None:
                    continue
                should_print_logs = True

                if result.successful():
                    table.add_row(
                        f"[green]✓[/green] {result.plan.operation_type} {_ResourceRef(result.plan.resource)}",
                        result.logs_file,
                    )
                else:
                    table.add_row(
                        f"[red]✗[/red] {result.plan.operation_type} {_ResourceRef(result.plan.resource)}",
                        result.logs_file,
                    )
    if should_print_logs:
        console.rule("[bold purple]resource logs")
        console.print()
        console.print(table)
        console.print()

    # Step 5.2: Print the service urls
    should_print_urls = False
    table = Table(show_header=True, show_edge=False, show_lines=False, box=None)
    table.add_column("Service", justify="left", no_wrap=True)
    table.add_column("URL", style="blue")
    for result in service_results:
        should_print_urls = True
        if result.service_state.service_url:
            table.add_row(
                _ServiceRef(result.plan.service), result.service_state.service_url
            )
    if should_print_urls:
        console.rule("[bold purple]service urls")
        console.print()
        console.print(table)
        console.print()

    # Step 5.3: Print the dns settings
    # TODO: add dns settings section

    # Step 5.4: Print the secrets
    # TODO: add secrets section

    # Step 5.5: Print the results summary
    console.rule("[bold purple]summary")
    console.print()

    successful_resource_create_count = 0
    failed_resource_create_count = 0
    successful_resource_update_count = 0
    failed_resource_update_count = 0
    successful_resource_replace_count = 0
    failed_resource_replace_count = 0
    successful_service_create_count = 0
    failed_service_create_count = 0
    successful_service_update_count = 0
    failed_service_update_count = 0

    for result in all_results:
        if isinstance(result, CreateResourceResult):
            if result.successful():
                if result.plan.operation_type == "create":
                    successful_resource_create_count += 1
                elif result.plan.operation_type == "update":
                    successful_resource_update_count += 1
                elif result.plan.operation_type == "replace":
                    successful_resource_replace_count += 1
            else:
                if result.plan.operation_type == "create":
                    failed_resource_create_count += 1
                elif result.plan.operation_type == "update":
                    failed_resource_update_count += 1
                elif result.plan.operation_type == "replace":
                    failed_resource_replace_count += 1
        elif isinstance(result, CreateServiceResult):
            if result.successful():
                if result.plan.operation_type == "create":
                    successful_service_create_count += 1
                elif result.plan.operation_type == "update":
                    successful_service_update_count += 1
            else:
                if result.plan.operation_type == "create":
                    failed_service_create_count += 1
                elif result.plan.operation_type == "update":
                    failed_service_update_count += 1
            for resource_result in result.resource_results:
                if resource_result.successful():
                    if resource_result.plan.operation_type == "create":
                        successful_resource_create_count += 1
                    elif resource_result.plan.operation_type == "update":
                        successful_resource_update_count += 1
                    elif resource_result.plan.operation_type == "replace":
                        successful_resource_replace_count += 1
                else:
                    if resource_result.plan.operation_type == "create":
                        failed_resource_create_count += 1
                    elif resource_result.plan.operation_type == "update":
                        failed_resource_update_count += 1
                    elif resource_result.plan.operation_type == "replace":
                        failed_resource_replace_count += 1

    if successful_resource_create_count or successful_service_create_count:
        if successful_service_create_count == 0:
            console.print(
                f"[green]Successfully created {successful_resource_create_count} {'resource' if successful_resource_create_count == 1 else 'resources'}[/green]"
            )
        elif successful_resource_create_count == 0:
            console.print(
                f"[green]Successfully created {successful_service_create_count} {'service' if successful_service_create_count == 1 else 'services'}[/green]"
            )
        else:
            console.print(
                f"[green]Successfully created {successful_resource_create_count} {'resource' if successful_resource_create_count == 1 else 'resources'} and {successful_service_create_count} {'service' if successful_service_create_count == 1 else 'services'}[/green]"
            )
    if failed_resource_create_count or failed_service_create_count:
        if failed_service_create_count == 0:
            console.print(
                f"[red]Failed to create {failed_resource_create_count} {'resource' if failed_resource_create_count == 1 else 'resources'}[/red]"
            )
        elif failed_resource_create_count == 0:
            console.print(
                f"[red]Failed to create {failed_service_create_count} {'service' if failed_service_create_count == 1 else 'services'}[/red]"
            )
        else:
            console.print(
                f"[red]Failed to create {failed_resource_create_count} {'resource' if failed_resource_create_count == 1 else 'resources'} and {failed_service_create_count} {'service' if failed_service_create_count == 1 else 'services'}[/red]"
            )
    if successful_resource_update_count or successful_service_update_count:
        if successful_service_update_count == 0:
            console.print(
                f"[green]Successfully updated {successful_resource_update_count} {'resource' if successful_resource_update_count == 1 else 'resources'}[/green]"
            )
        elif successful_resource_update_count == 0:
            console.print(
                f"[green]Successfully updated {successful_service_update_count} {'service' if successful_service_update_count == 1 else 'services'}[/green]"
            )
        else:
            console.print(
                f"[green]Successfully updated {successful_resource_update_count} {'resource' if successful_resource_update_count == 1 else 'resources'} and {successful_service_update_count} {'service' if successful_service_update_count == 1 else 'services'}[/green]"
            )
    if failed_resource_update_count or failed_service_update_count:
        if failed_service_update_count == 0:
            console.print(
                f"[red]Failed to update {failed_resource_update_count} {'resource' if failed_resource_update_count == 1 else 'resources'}[/red]"
            )
        elif failed_resource_update_count == 0:
            console.print(
                f"[red]Failed to update {failed_service_update_count} {'service' if failed_service_update_count == 1 else 'services'}[/red]"
            )
        else:
            console.print(
                f"[red]Failed to update {failed_resource_update_count} {'resource' if failed_resource_update_count == 1 else 'resources'} and {failed_service_update_count} {'service' if failed_service_update_count == 1 else 'services'}[/red]"
            )
    if successful_resource_replace_count:
        console.print(
            f"[green]Successfully replaced {successful_resource_replace_count} {'resource' if successful_resource_replace_count == 1 else 'resources'}[/green]"
        )
    if failed_resource_replace_count:
        console.print(
            f"[red]Failed to replace {failed_resource_replace_count} {'resource' if failed_resource_replace_count == 1 else 'resources'}[/red]"
        )
    # Returns true if the command succeeded
    return (
        not failed_resource_create_count
        and not failed_resource_update_count
        and not failed_resource_replace_count
        and not failed_service_create_count
        and not failed_service_update_count
    )

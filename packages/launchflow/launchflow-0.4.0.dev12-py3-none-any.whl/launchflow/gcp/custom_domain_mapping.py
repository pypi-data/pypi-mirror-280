import dataclasses

import rich
from rich import box
from rich.padding import Padding
from rich.table import Table

from launchflow.gcp.cloud_run_container import CloudRunServiceContainer
from launchflow.gcp.resource import GCPResource
from launchflow.models.enums import EnvironmentType, ResourceProduct
from launchflow.node import Inputs, Outputs


@dataclasses.dataclass
class CustomDomainMappingOutputs(Outputs):
    ip_address: str
    ssl_certificate_id: str


@dataclasses.dataclass
class CustomDomainMappingInputs(Inputs):
    domain: str
    cloud_run_service: str
    region: str


class CustomDomainMapping(GCPResource[CustomDomainMappingOutputs]):
    def __init__(
        self, name: str, *, domain: str, cloud_run: CloudRunServiceContainer
    ) -> None:
        super().__init__(
            name=name,
            product=ResourceProduct.GCP_CUSTOM_DOMAIN_MAPPING,
            depends_on=[cloud_run],
        )
        self.domain = domain
        self.cloud_run = cloud_run

    def inputs(self, environment_type: EnvironmentType) -> CustomDomainMappingInputs:
        return CustomDomainMappingInputs(
            domain=self.domain,
            cloud_run_service=self.cloud_run.name,
            region=self.cloud_run.region,
        )

    async def _print_success_message(self) -> str:
        rich.print("  > Add the following DNS records to point to the load balancer:")
        outputs = await self.outputs_async()
        table = Table(
            box=box.SIMPLE,
            caption="It make take several minutes or hours for GCP to verify your DNS records once you have updated them.",
        )
        table.add_column("Host Name", style="cyan")
        table.add_column("Type", style="yellow")
        table.add_column("IP Address", style="magenta")
        table.add_row(self.domain, "A", outputs.ip_address)
        p = Padding(table, (0, 0, 0, 4))
        rich.print(p)

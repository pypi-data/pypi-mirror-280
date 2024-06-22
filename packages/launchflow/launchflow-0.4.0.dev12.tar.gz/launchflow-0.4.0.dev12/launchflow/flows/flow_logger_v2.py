from contextlib import contextmanager

from rich.console import Group
from rich.live import Live
from rich.progress import Progress, SpinnerColumn, TextColumn, TimeElapsedColumn


class OperationsLiveView:
    def __init__(self, live: Live, indent: int = 0):
        self.live = live
        indent = " " * indent
        self.progress = Progress(
            TextColumn(indent),
            SpinnerColumn(finished_text=""),
            TextColumn("{task.description}"),
            TimeElapsedColumn(),
        )
        current_renderable = self.live.renderable
        if current_renderable is None:
            current_renderable = Group(self.progress, "")
        elif isinstance(current_renderable, Group):
            # adds a new line before the new progress bar
            current_renderable = Group(
                *current_renderable.renderables, "", self.progress, ""
            )
        else:
            current_renderable = Group(current_renderable, self.progress)
        self.live.update(current_renderable)

    def error(self, message: str):
        self.progress.console.print(f"[red]{message}[/red]")

    def update(self, task_id, description: str, left_padding: int = 0):
        left_padding_str = " " * left_padding
        self.progress.update(task_id, description=f"{left_padding_str}{description}")

    @contextmanager
    def start(self, description: str, left_padding: int = 0):
        left_padding_str = " " * left_padding
        task_id = self.progress.add_task(f"{left_padding_str}{description}", total=1)
        yield task_id

    def done(
        self, task_id, description: str, failed: bool = False, left_padding: int = 0
    ):
        left_padding_str = " " * left_padding
        if failed:
            self.progress.update(
                task_id,
                description=f"{left_padding_str}[red]✗[/red] {description}",
                completed=1,
            )
        else:
            self.progress.update(
                task_id,
                description=f"{left_padding_str}[green]✓[/green] {description}",
                completed=1,
            )

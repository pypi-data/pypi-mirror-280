from create_api_app.setup.base import ControllerBase
from create_api_app.conf.constants import PASS

from rich.console import Console
from rich.progress import Progress, SpinnerColumn, TextColumn


def run_tasks(tasks: list[tuple[ControllerBase, str]], console: Console) -> None:
    """The task handler for performing each operation in the CLI."""
    with Progress(
        SpinnerColumn(),
        TextColumn("[progress.description]{task.description}"),
        console=console,
    ) as progress:
        for idx, (task, desc) in enumerate(tasks, 1):
            new_desc = f"{idx}. {desc}"
            task_id = progress.add_task(description=new_desc, total=None)
            task().run(progress)
            progress.update(task_id, completed=1, description=f"{new_desc} {PASS}")


def run_frontend_tasks(
    container_controller: ControllerBase,
    other_tasks: list[tuple[ControllerBase]],
    console: Console,
) -> None:
    """The task handler for performing frontend tasks."""
    for task, desc in container_controller.tasks:
        console.print(desc)
        task()

    console.clear()

    console.print("Continuing stage [green]2[/green]/[cyan]3[/cyan]...")
    run_tasks(other_tasks, console)

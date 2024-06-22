import os
import shutil
import subprocess
from dataclasses import dataclass

import typer
from typing_extensions import Annotated

from rich.progress import track
from rich.console import Console


app = typer.Typer(rich_markup_mode="rich")

console = Console()


@dataclass
class Task:
    command: list[str]
    msg: str
    code: int = 0


def handle_existing(name: str) -> None:
    name = typer.style(f"'{name}'", fg=typer.colors.MAGENTA)
    exists = typer.style("exists", fg=typer.colors.RED)
    overwrite = typer.style("overwrite", fg=typer.colors.YELLOW)

    delete = typer.confirm(
        f"A project with the name {name} already {exists}! Do you want to {overwrite} it?"
    )

    if not delete:
        console.print("\n[dark_goldenrod]No changes made.[/dark_goldenrod]")
        raise typer.Abort()


def perform_tasks(tasks: list[Task]) -> list[Task]:
    for task in track(tasks, description="Progress...", console=console):
        result = subprocess.run(task.command, capture_output=True, text=True)

        if result.returncode == 0:
            task.msg = f"Success: {task.msg}\n"
            task.code = 0
        else:
            task.msg = f"Fail: {task.msg}\n  [red]{result.stderr}[/red]"
            task.code = 1
            break

    return tasks


def output_task_msgs(tasks: list[Task]) -> None:
    console.print()
    for idx, task in enumerate(tasks, start=1):
        console.print(f"  {idx}: {task.msg}")

    if any([task.code == 1 for task in tasks]):
        console.print(
            "\n[red]Failed[/red] to create project. Please [green]resolve[/green] [red]errors[/red] then [dark_goldenrod]try again[/dark_goldenrod]."
        )
        raise typer.Abort()


@app.command()
def create(
    name: Annotated[
        str, typer.Argument(help="The name of the project", show_default=False)
    ],
):
    dirpath = os.path.join(os.getcwd(), name)

    if os.path.exists(dirpath):
        handle_existing(name)

        shutil.rmtree(dirpath)
        os.mkdir(dirpath)

    console.clear()

    image_name = "achronus/nextjs_app"
    container_name = "nextjs_app_container"

    transfer_tasks = [
        Task(
            command=["docker", "pull", image_name],
            msg=f"Image [cyan]{image_name}[/cyan] retrieved",
        ),
        Task(
            command=["docker", "run", "-d", "--name", container_name, image_name],
            msg=f"Started [cyan]{container_name}[/cyan]",
        ),
        Task(
            command=["docker", "cp", f"{container_name}:frontend", dirpath],
            msg=f"Copied files from [cyan]{container_name}:frontend[/cyan] to [magenta]./{name}[/magenta]",
        ),
    ]

    cleanup_tasks = [
        Task(
            command=["docker", "stop", container_name],
            msg=f"Stopped container [cyan]{container_name}[/cyan]",
        ),
        Task(
            command=["docker", "rm", container_name],
            msg=f"Removed container [cyan]{container_name}[/cyan]",
        ),
        Task(
            command=["docker", "rmi", image_name],
            msg=f"Removed image [cyan]{image_name}[/cyan]",
        ),
    ]

    console.print("\nBuilding [green]Next.js[/green] app...")
    console.print("  Steps to complete:")
    console.print("    1. [yellow]File creation[/yellow]")
    console.print("    2. [cyan]Docker cleanup[/cyan]\n")

    console.print("Performing step: [yellow]1[/yellow]/[cyan]2[/cyan]\n")
    transfer_tasks = perform_tasks(transfer_tasks)
    output_task_msgs(transfer_tasks)

    console.print("\n")
    console.print("Performing step: [cyan]2[/cyan]/[cyan]2[/cyan]")
    cleanup_tasks = perform_tasks(cleanup_tasks)
    output_task_msgs(cleanup_tasks)

    console.print(
        f"\nApplication created successfully. Access it at: [dark_goldenrod][link={dirpath}]./{name}[/link][/dark_goldenrod]"
    )


if __name__ == "__main__":
    app()

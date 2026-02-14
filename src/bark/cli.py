"""Bark CLI — a static site generator."""

from pathlib import Path

import typer
from rich.console import Console

app = typer.Typer(
    name="bark",
    help="A static site generator.",
    no_args_is_help=True,
)
console = Console()


@app.command()
def build(
    project_dir: Path = typer.Argument(Path("."), help="Project directory"),
) -> None:
    """Build the static site."""
    from bark.builder import build_site
    from bark.config import load_config

    project_dir = project_dir.resolve()
    config = load_config(project_dir)
    console.print(f"[bold]Building [cyan]{config.site.name}[/cyan]...[/bold]")
    build_site(config, project_dir)
    console.print(f"[bold green]Site built to {config.build.output_dir}/[/bold green]")


@app.command()
def serve(
    project_dir: Path = typer.Argument(Path("."), help="Project directory"),
    port: int = typer.Option(8000, help="Port to serve on"),
) -> None:
    """Serve the site locally with live reload."""
    from bark.server import serve_site

    project_dir = project_dir.resolve()
    serve_site(project_dir, port)


@app.command()
def new(
    name: str = typer.Argument(..., help="Name of the new project"),
) -> None:
    """Scaffold a new project."""
    from bark.scaffold import create_project

    create_project(name)
    console.print(f"[bold green]Created new project: {name}/[/bold green]")
    console.print(f"\n  cd {name}")
    console.print("  bark build")
    console.print("  bark serve\n")


if __name__ == "__main__":
    app()

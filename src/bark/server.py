"""Development server with live reload."""

import http.server
import threading
import time
from functools import partial
from pathlib import Path

from rich.console import Console
from watchdog.events import FileSystemEventHandler
from watchdog.observers import Observer

console = Console()


class RebuildHandler(FileSystemEventHandler):
    """Watch for file changes and trigger rebuild."""

    def __init__(self, project_dir: Path, rebuild_fn: callable) -> None:
        self.project_dir = project_dir
        self.rebuild_fn = rebuild_fn
        self._last_rebuild = 0.0
        self._debounce_seconds = 0.5

    def on_any_event(self, event) -> None:
        if event.is_directory:
            return
        # Skip hidden files and output directory
        src_path = event.src_path
        if "/.git/" in src_path or "/dist/" in src_path:
            return

        now = time.time()
        if now - self._last_rebuild < self._debounce_seconds:
            return

        self._last_rebuild = now
        console.print(f"[yellow]Change detected: {Path(src_path).name}[/yellow]")
        try:
            self.rebuild_fn()
            console.print("[green]Rebuilt successfully.[/green]")
        except Exception as e:
            console.print(f"[red]Build error: {e}[/red]")


def serve_site(project_dir: Path, port: int = 8000) -> None:
    """Build, serve, and watch for changes."""
    from bark.builder import build_site
    from bark.config import load_config

    config = load_config(project_dir)

    def rebuild() -> None:
        cfg = load_config(project_dir)
        build_site(cfg, project_dir)

    # Initial build
    console.print(f"[bold]Building [cyan]{config.site.name}[/cyan]...[/bold]")
    build_site(config, project_dir)
    console.print("[bold green]Build complete.[/bold green]")

    output_dir = project_dir / config.build.output_dir

    # Start threaded HTTP server (handles concurrent requests, suppresses BrokenPipeError)
    class QuietHandler(http.server.SimpleHTTPRequestHandler):
        def __init__(self, *args, **kwargs):
            super().__init__(*args, directory=str(output_dir), **kwargs)

        def log_message(self, fmt, *args):
            """Only log errors, not every request."""
            pass

        def handle_one_request(self):
            try:
                super().handle_one_request()
            except BrokenPipeError:
                pass

        def handle(self):
            try:
                super().handle()
            except BrokenPipeError:
                pass

    class ThreadedServer(http.server.ThreadingHTTPServer):
        allow_reuse_address = True
        allow_reuse_port = True

    server = ThreadedServer(("", port), QuietHandler)

    server_thread = threading.Thread(target=server.serve_forever, daemon=True)
    server_thread.start()
    console.print(f"\n[bold]Serving at [cyan]http://localhost:{port}[/cyan][/bold]")
    console.print("[dim]Press Ctrl+C to stop.[/dim]\n")

    # Start file watcher
    observer = Observer()
    content_dir = project_dir / config.content.dir
    observer.schedule(RebuildHandler(project_dir, rebuild), str(content_dir), recursive=True)

    # Also watch bark.yml
    observer.schedule(RebuildHandler(project_dir, rebuild), str(project_dir), recursive=False)
    observer.start()

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        console.print("\n[bold]Stopping server...[/bold]")
        observer.stop()
        server.shutdown()
    observer.join()

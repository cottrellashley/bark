"""Tests for bark.cli."""

from pathlib import Path

import pytest
from typer.testing import CliRunner

from bark.cli import app

runner = CliRunner()


def test_cli_help() -> None:
    """Test that CLI shows help."""
    result = runner.invoke(app, ["--help"])
    assert result.exit_code == 0
    assert "blog-focused" in result.stdout.lower() or "static site" in result.stdout.lower()


def test_cli_build(tmp_project: Path) -> None:
    """Test bark build command."""
    from bark.builder import build_site
    from bark.config import load_config

    config = load_config(tmp_project)
    build_site(config, tmp_project)
    assert (tmp_project / "dist" / "index.html").exists()


def test_cli_build_missing_config(tmp_path: Path) -> None:
    """Test bark build with no bark.yml."""
    result = runner.invoke(app, ["build", str(tmp_path)])
    assert result.exit_code != 0


def test_cli_new(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> None:
    """Test bark new command."""
    monkeypatch.chdir(tmp_path)
    project_name = "my-test-blog"
    result = runner.invoke(app, ["new", project_name], catch_exceptions=False)
    assert result.exit_code == 0
    assert project_name in result.stdout
    assert (tmp_path / project_name / "bark.yml").exists()

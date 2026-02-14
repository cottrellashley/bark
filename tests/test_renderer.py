"""Tests for bark.renderer."""

import pytest

from bark.renderer import create_markdown_renderer, get_pygments_css, load_theme, render_markdown


def test_create_markdown_renderer() -> None:
    """Test creating a markdown renderer."""
    md = create_markdown_renderer()
    assert md is not None


def test_render_markdown_basic() -> None:
    """Test basic markdown rendering."""
    md = create_markdown_renderer()
    result = render_markdown(md, "# Hello\n\nA paragraph.")
    assert "<h1" in result
    assert "Hello" in result
    assert "<p>" in result


def test_render_markdown_code_block() -> None:
    """Test fenced code block rendering."""
    md = create_markdown_renderer()
    result = render_markdown(md, '```python\nprint("hi")\n```')
    assert "highlight" in result or "codehilite" in result


def test_render_markdown_table() -> None:
    """Test table rendering."""
    md = create_markdown_renderer()
    result = render_markdown(md, "| A | B |\n|---|---|\n| 1 | 2 |")
    assert "<table>" in result


def test_render_markdown_reset() -> None:
    """Test that renderer resets between calls."""
    md = create_markdown_renderer()
    render_markdown(md, "# First")
    result = render_markdown(md, "# Second")
    assert "Second" in result
    assert "First" not in result


def test_load_theme_default() -> None:
    """Test loading the built-in default theme."""
    env = load_theme("default")
    assert env is not None
    template = env.get_template("base.html")
    assert template is not None


def test_load_theme_not_found() -> None:
    """Test loading a non-existent theme."""
    with pytest.raises(FileNotFoundError, match="not found"):
        load_theme("nonexistent")


def test_get_pygments_css() -> None:
    """Test Pygments CSS generation."""
    css = get_pygments_css()
    assert ".highlight" in css
    assert len(css) > 100

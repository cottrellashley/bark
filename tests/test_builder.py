"""Tests for bark.builder."""

from pathlib import Path

from bark.builder import build_site, collect_tags
from bark.config import load_config
from bark.content import Post

from datetime import date


def test_build_site(tmp_project: Path) -> None:
    """Test full site build."""
    config = load_config(tmp_project)
    build_site(config, tmp_project)

    dist = tmp_project / "dist"
    assert dist.exists()
    assert (dist / "index.html").exists()
    assert (dist / "about" / "index.html").exists()
    assert (dist / "posts" / "index.html").exists()
    assert (dist / "posts" / "test-post" / "index.html").exists()
    assert (dist / "posts" / "second-post" / "index.html").exists()
    assert (dist / "archive" / "index.html").exists()
    assert (dist / "tags" / "index.html").exists()
    assert (dist / "tags" / "python" / "index.html").exists()
    assert (dist / "static" / "css" / "style.css").exists()
    assert (dist / "static" / "css" / "pygments.css").exists()


def test_build_filters_drafts(tmp_project: Path) -> None:
    """Test that draft posts are not built."""
    config = load_config(tmp_project)
    build_site(config, tmp_project)

    dist = tmp_project / "dist"
    assert not (dist / "posts" / "draft-post" / "index.html").exists()


def test_build_post_content(tmp_project: Path) -> None:
    """Test that post HTML contains expected content."""
    config = load_config(tmp_project)
    build_site(config, tmp_project)

    post_html = (tmp_project / "dist" / "posts" / "test-post" / "index.html").read_text()
    assert "Test Post" in post_html
    assert "python" in post_html.lower()
    assert "highlight" in post_html or "codehilite" in post_html


def test_build_index_content(tmp_project: Path) -> None:
    """Test that the home page contains expected content."""
    config = load_config(tmp_project)
    build_site(config, tmp_project)

    index_html = (tmp_project / "dist" / "index.html").read_text()
    assert "Welcome" in index_html


def test_build_cleans_output(tmp_project: Path) -> None:
    """Test that output directory is cleaned before build."""
    config = load_config(tmp_project)
    dist = tmp_project / "dist"
    dist.mkdir()
    (dist / "stale.html").write_text("old")

    build_site(config, tmp_project)
    assert not (dist / "stale.html").exists()


def test_collect_tags() -> None:
    """Test tag collection from posts."""
    posts = [
        Post(title="A", slug="a", source_path=Path("a.md"), content_markdown="",
             date=date(2026, 1, 1), tags=["python", "testing"]),
        Post(title="B", slug="b", source_path=Path("b.md"), content_markdown="",
             date=date(2026, 1, 2), tags=["python"]),
    ]
    tags = collect_tags(posts)
    assert len(tags["python"]) == 2
    assert len(tags["testing"]) == 1


def test_build_nav_links(tmp_project: Path) -> None:
    """Test that navigation links appear in output."""
    config = load_config(tmp_project)
    build_site(config, tmp_project)

    index_html = (tmp_project / "dist" / "index.html").read_text()
    assert "Home" in index_html
    assert "About" in index_html
    assert "Blog" in index_html

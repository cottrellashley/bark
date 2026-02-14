"""Tests for bark.content."""

from datetime import date
from pathlib import Path

from bark.content import discover_pages, discover_posts, parse_frontmatter


def test_parse_frontmatter_with_meta() -> None:
    """Test parsing frontmatter from markdown."""
    text = "---\ntitle: Hello\ndate: 2026-01-01\n---\n\n# Content"
    meta, body = parse_frontmatter(text)
    assert meta["title"] == "Hello"
    assert body == "# Content"


def test_parse_frontmatter_no_meta() -> None:
    """Test parsing markdown without frontmatter."""
    text = "# Just Content\n\nNo frontmatter here."
    meta, body = parse_frontmatter(text)
    assert meta == {}
    assert body == text


def test_parse_frontmatter_empty() -> None:
    """Test parsing empty string."""
    meta, body = parse_frontmatter("")
    assert meta == {}
    assert body == ""


def test_discover_pages(tmp_project: Path) -> None:
    """Test discovering pages from content directory."""
    content_dir = tmp_project / "content"
    pages = discover_pages(content_dir)
    slugs = [p.slug for p in pages]
    assert "about" in slugs
    assert "" in slugs  # index.md gets empty slug


def test_discover_pages_titles(tmp_project: Path) -> None:
    """Test that page titles come from frontmatter."""
    content_dir = tmp_project / "content"
    pages = discover_pages(content_dir)
    titles = {p.slug: p.title for p in pages}
    assert titles["about"] == "About"
    assert titles[""] == "Home"


def test_discover_posts(tmp_project: Path) -> None:
    """Test discovering posts sorted newest first."""
    posts_dir = tmp_project / "content" / "posts"
    posts = discover_posts(posts_dir, sort="newest_first")
    # Draft is included in discovery (filtering happens in builder)
    assert len(posts) == 3
    # Newest first
    assert posts[0].date >= posts[1].date


def test_discover_posts_oldest_first(tmp_project: Path) -> None:
    """Test sorting oldest first."""
    posts_dir = tmp_project / "content" / "posts"
    posts = discover_posts(posts_dir, sort="oldest_first")
    assert posts[0].date <= posts[1].date


def test_post_tags(tmp_project: Path) -> None:
    """Test that tags are parsed correctly."""
    posts_dir = tmp_project / "content" / "posts"
    posts = discover_posts(posts_dir)
    test_post = next(p for p in posts if p.slug == "test-post")
    assert "python" in test_post.tags
    assert "testing" in test_post.tags


def test_post_draft_flag(tmp_project: Path) -> None:
    """Test that draft flag is parsed."""
    posts_dir = tmp_project / "content" / "posts"
    posts = discover_posts(posts_dir)
    draft = next(p for p in posts if p.slug == "draft-post")
    assert draft.draft is True


def test_discover_posts_empty_dir(tmp_path: Path) -> None:
    """Test discovering posts from non-existent directory."""
    posts = discover_posts(tmp_path / "nonexistent")
    assert posts == []


def test_post_date_parsing(tmp_project: Path) -> None:
    """Test that dates are parsed correctly."""
    posts_dir = tmp_project / "content" / "posts"
    posts = discover_posts(posts_dir)
    test_post = next(p for p in posts if p.slug == "test-post")
    assert test_post.date == date(2026, 1, 15)

"""Content discovery and frontmatter parsing."""

from dataclasses import dataclass, field
from datetime import date
from pathlib import Path

import yaml


@dataclass
class Page:
    """A static page (about, contact, etc.)."""

    title: str
    slug: str
    source_path: Path
    content_markdown: str
    meta: dict = field(default_factory=dict)


@dataclass
class Post:
    """A blog post with date and tags."""

    title: str
    slug: str
    source_path: Path
    content_markdown: str
    date: date
    tags: list[str] = field(default_factory=list)
    description: str = ""
    draft: bool = False
    meta: dict = field(default_factory=dict)


def parse_frontmatter(text: str) -> tuple[dict, str]:
    """Split YAML frontmatter from markdown content.

    Returns a tuple of (metadata_dict, markdown_body).
    """
    if not text.startswith("---"):
        return {}, text

    parts = text.split("---", 2)
    if len(parts) < 3:
        return {}, text

    meta = yaml.safe_load(parts[1]) or {}
    body = parts[2].strip()
    return meta, body


def discover_pages(content_dir: Path, posts_dir_name: str = "posts") -> list[Page]:
    """Find all top-level .md files in content_dir (excluding posts directory)."""
    pages = []
    if not content_dir.exists():
        return pages

    for md_file in sorted(content_dir.glob("*.md")):
        text = md_file.read_text()
        meta, body = parse_frontmatter(text)

        title = meta.get("title", md_file.stem.replace("-", " ").title())
        slug = md_file.stem if md_file.stem != "index" else ""

        pages.append(
            Page(
                title=title,
                slug=slug,
                source_path=md_file,
                content_markdown=body,
                meta=meta,
            )
        )
    return pages


def discover_posts(posts_dir: Path, sort: str = "newest_first") -> list[Post]:
    """Find all .md files in the posts directory, parse frontmatter, sort by date."""
    posts = []
    if not posts_dir.exists():
        return posts

    for md_file in sorted(posts_dir.glob("*.md")):
        text = md_file.read_text()
        meta, body = parse_frontmatter(text)

        title = meta.get("title", md_file.stem.replace("-", " ").title())
        post_date = meta.get("date", date.today())
        if isinstance(post_date, str):
            post_date = date.fromisoformat(post_date)

        tags = meta.get("tags", [])
        if isinstance(tags, str):
            tags = [t.strip() for t in tags.split(",")]

        slug = md_file.stem

        posts.append(
            Post(
                title=title,
                slug=slug,
                source_path=md_file,
                content_markdown=body,
                date=post_date,
                tags=tags,
                description=meta.get("description", ""),
                draft=meta.get("draft", False),
                meta=meta,
            )
        )

    if sort == "newest_first":
        posts.sort(key=lambda p: p.date, reverse=True)
    else:
        posts.sort(key=lambda p: p.date)

    return posts

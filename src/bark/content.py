"""Content discovery and frontmatter parsing."""

from __future__ import annotations

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
class Entry:
    """A content entry within a collection (article, project, note, etc.)."""

    title: str
    slug: str
    source_path: Path
    content_markdown: str
    date: date | None = None
    tags: list[str] = field(default_factory=list)
    description: str = ""
    draft: bool = False
    meta: dict = field(default_factory=dict)


# Backward compatibility alias
Post = Entry


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


def discover_pages(content_dir: Path, exclude_dirs: list[str] | None = None) -> list[Page]:
    """Find all top-level .md files in content_dir (excluding collection directories)."""
    if exclude_dirs is None:
        exclude_dirs = []
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


def discover_entries(
    entries_dir: Path,
    sort: str = "newest_first",
    require_date: bool = True,
) -> list[Entry]:
    """Find all .md files in a collection directory, parse frontmatter, and sort.

    Args:
        entries_dir: Directory to scan for .md files.
        sort: Sort order — "newest_first", "oldest_first", or "alphabetical".
        require_date: If True, entries without a date get today's date.
                      If False, entries without a date have date=None.
    """
    entries: list[Entry] = []
    if not entries_dir.exists():
        return entries

    for md_file in sorted(entries_dir.glob("*.md")):
        text = md_file.read_text()
        meta, body = parse_frontmatter(text)

        title = meta.get("title", md_file.stem.replace("-", " ").title())

        entry_date = meta.get("date")
        if entry_date is not None:
            if isinstance(entry_date, str):
                entry_date = date.fromisoformat(entry_date)
        elif require_date:
            entry_date = date.today()

        tags = meta.get("tags", [])
        if isinstance(tags, str):
            tags = [t.strip() for t in tags.split(",")]

        slug = md_file.stem

        entries.append(
            Entry(
                title=title,
                slug=slug,
                source_path=md_file,
                content_markdown=body,
                date=entry_date,
                tags=tags,
                description=meta.get("description", ""),
                draft=meta.get("draft", False),
                meta=meta,
            )
        )

    # Sort
    if sort == "alphabetical":
        entries.sort(key=lambda e: e.title.lower())
    elif sort == "oldest_first":
        entries.sort(key=lambda e: e.date or date.min)
    else:
        # newest_first (default)
        entries.sort(key=lambda e: e.date or date.min, reverse=True)

    return entries


# Backward compatibility aliases
def discover_posts(posts_dir: Path, sort: str = "newest_first") -> list[Entry]:
    """Backward-compatible wrapper around discover_entries."""
    return discover_entries(posts_dir, sort=sort, require_date=True)

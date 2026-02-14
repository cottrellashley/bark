"""Configuration loading and validation for Bark."""

from __future__ import annotations

from dataclasses import dataclass, field
from pathlib import Path

import yaml

VALID_LAYOUTS = ("timeline", "grid", "minimal")
VALID_SORTS = ("newest_first", "oldest_first", "alphabetical")


@dataclass
class SiteConfig:
    """Site-level configuration."""

    name: str = "My Site"
    url: str = "https://example.com"
    description: str = ""
    author: str = ""


@dataclass
class ContentConfig:
    """Content directory configuration."""

    dir: str = "content"


@dataclass
class BuildConfig:
    """Build output configuration."""

    output_dir: str = "dist"


@dataclass
class CollectionConfig:
    """Configuration for a single content collection."""

    items_per_page: int = 10
    date_format: str = "%B %d, %Y"
    sort: str = "newest_first"
    tags: bool = True
    archive: bool = True
    layout: str = "timeline"


@dataclass
class ThemeConfig:
    """Theme configuration."""

    name: str = "default"


@dataclass
class NavItem:
    """A single navigation item."""

    label: str
    path: str


@dataclass
class BarkConfig:
    """Root configuration for a Bark site."""

    site: SiteConfig = field(default_factory=SiteConfig)
    content: ContentConfig = field(default_factory=ContentConfig)
    build: BuildConfig = field(default_factory=BuildConfig)
    collections: dict[str, CollectionConfig] = field(default_factory=dict)
    theme: ThemeConfig = field(default_factory=ThemeConfig)
    nav: list[NavItem] = field(default_factory=list)


def load_config(project_dir: Path) -> BarkConfig:
    """Load bark.yml from the given project directory."""
    config_path = project_dir / "bark.yml"
    if not config_path.exists():
        msg = f"No bark.yml found in {project_dir}"
        raise FileNotFoundError(msg)

    with config_path.open() as f:
        raw = yaml.safe_load(f) or {}

    nav_items = []
    for item in raw.get("nav", []):
        if isinstance(item, dict):
            for label, path in item.items():
                # Convert .md paths to clean URLs
                if path == "index.md":
                    path = ""
                elif path.endswith(".md"):
                    path = path[:-3] + "/"
                nav_items.append(NavItem(label=label, path=path))

    # Parse collections
    collections = _parse_collections(raw)

    return BarkConfig(
        site=SiteConfig(**raw.get("site", {})),
        content=ContentConfig(**raw.get("content", {})),
        build=BuildConfig(**raw.get("build", {})),
        collections=collections,
        theme=ThemeConfig(**raw.get("theme", {})),
        nav=nav_items,
    )


def _parse_collections(raw: dict) -> dict[str, CollectionConfig]:
    """Parse collections from raw config, with backward compat for old blog: format."""
    collections: dict[str, CollectionConfig] = {}

    if "collections" in raw:
        # New format: collections: { name: { settings } }
        for name, settings in raw["collections"].items():
            settings = settings or {}
            coll = CollectionConfig(**settings)
            if coll.layout not in VALID_LAYOUTS:
                msg = f"Invalid layout '{coll.layout}' for collection '{name}'. Must be one of: {', '.join(VALID_LAYOUTS)}"
                raise ValueError(msg)
            if coll.sort not in VALID_SORTS:
                msg = f"Invalid sort '{coll.sort}' for collection '{name}'. Must be one of: {', '.join(VALID_SORTS)}"
                raise ValueError(msg)
            collections[name] = coll

    elif "blog" in raw:
        # Backward compat: convert old blog: config to a single collection
        blog_raw = raw.get("blog", {})
        content_raw = raw.get("content", {})
        posts_dir = content_raw.get("posts_dir", "posts")

        # Map old field names to new ones
        coll_settings = {
            "items_per_page": blog_raw.get("posts_per_page", 10),
            "date_format": blog_raw.get("date_format", "%B %d, %Y"),
            "sort": blog_raw.get("sort", "newest_first"),
            "tags": blog_raw.get("tags", True),
            "archive": blog_raw.get("archive", True),
            "layout": "timeline",
        }
        collections[posts_dir] = CollectionConfig(**coll_settings)

    return collections

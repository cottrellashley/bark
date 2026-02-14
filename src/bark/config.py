"""Configuration loading and validation for Bark."""

from dataclasses import dataclass, field
from pathlib import Path

import yaml


@dataclass
class SiteConfig:
    """Site-level configuration."""

    name: str = "My Blog"
    url: str = "https://example.com"
    description: str = ""
    author: str = ""


@dataclass
class ContentConfig:
    """Content directory configuration."""

    dir: str = "content"
    posts_dir: str = "posts"


@dataclass
class BuildConfig:
    """Build output configuration."""

    output_dir: str = "dist"


@dataclass
class BlogConfig:
    """Blog-specific configuration."""

    posts_per_page: int = 10
    date_format: str = "%B %d, %Y"
    sort: str = "newest_first"
    tags: bool = True
    archive: bool = True


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
    blog: BlogConfig = field(default_factory=BlogConfig)
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

    return BarkConfig(
        site=SiteConfig(**raw.get("site", {})),
        content=ContentConfig(**raw.get("content", {})),
        build=BuildConfig(**raw.get("build", {})),
        blog=BlogConfig(**raw.get("blog", {})),
        theme=ThemeConfig(**raw.get("theme", {})),
        nav=nav_items,
    )

"""Tests for bark.config."""

from pathlib import Path

import pytest

from bark.config import BarkConfig, NavItem, load_config


def test_load_config(tmp_project: Path) -> None:
    """Test loading a valid bark.yml."""
    config = load_config(tmp_project)
    assert config.site.name == "Test Blog"
    assert config.site.url == "https://test.com"
    assert config.site.author == "Tester"
    assert config.content.dir == "content"
    assert config.content.posts_dir == "posts"
    assert config.build.output_dir == "dist"
    assert config.blog.posts_per_page == 5
    assert config.blog.tags is True
    assert config.theme.name == "default"


def test_load_config_nav(tmp_project: Path) -> None:
    """Test nav items are parsed correctly."""
    config = load_config(tmp_project)
    assert len(config.nav) == 3
    assert config.nav[0] == NavItem(label="Home", path="index.md")
    assert config.nav[1] == NavItem(label="About", path="about.md")


def test_load_config_missing_file(tmp_path: Path) -> None:
    """Test that missing bark.yml raises FileNotFoundError."""
    with pytest.raises(FileNotFoundError, match="No bark.yml found"):
        load_config(tmp_path)


def test_load_config_defaults(tmp_path: Path) -> None:
    """Test that missing sections use defaults."""
    (tmp_path / "bark.yml").write_text("site:\n  name: Minimal\n")
    config = load_config(tmp_path)
    assert config.site.name == "Minimal"
    assert config.content.dir == "content"
    assert config.build.output_dir == "dist"
    assert config.blog.posts_per_page == 10


def test_bark_config_defaults() -> None:
    """Test BarkConfig default values."""
    config = BarkConfig()
    assert config.site.name == "My Blog"
    assert config.blog.sort == "newest_first"
    assert config.nav == []

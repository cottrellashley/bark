"""Main build pipeline for Bark."""

from __future__ import annotations

import math
import shutil
from dataclasses import dataclass
from pathlib import Path

from bark.config import BarkConfig, CollectionConfig
from bark.content import Entry, discover_entries, discover_pages
from bark.renderer import create_markdown_renderer, get_pygments_css, load_theme, render_markdown

WORDS_PER_MINUTE = 200


def estimate_reading_time(text: str) -> int:
    """Estimate reading time in minutes from raw markdown text."""
    word_count = len(text.split())
    return max(1, math.ceil(word_count / WORDS_PER_MINUTE))


def collect_tags(entries: list[Entry]) -> dict[str, list[Entry]]:
    """Group entries by tag."""
    tags: dict[str, list[Entry]] = {}
    for entry in entries:
        for tag in entry.tags:
            tags.setdefault(tag, []).append(entry)
    return dict(sorted(tags.items()))


@dataclass
class CollectionContext:
    """Template-accessible info about a collection."""

    name: str
    label: str
    url_prefix: str
    layout: str
    date_format: str


def build_site(config: BarkConfig, project_dir: Path) -> None:
    """Execute the full build pipeline."""
    output_dir = project_dir / config.build.output_dir
    content_dir = project_dir / config.content.dir

    # Step 1: Clean output directory
    if output_dir.exists():
        shutil.rmtree(output_dir)
    output_dir.mkdir(parents=True)

    # Step 2: Set up renderer
    md = create_markdown_renderer()
    env = load_theme(config.theme.name)

    # Step 3: Discover and render pages
    exclude_dirs = list(config.collections.keys())
    pages = discover_pages(content_dir, exclude_dirs=exclude_dirs)

    # Shared template context (built after all collections are processed)
    site_context = {
        "site": config.site,
        "nav": config.nav,
        "config": config,
    }

    for page in pages:
        html_content, toc_html = render_markdown(md, page.content_markdown)
        template = env.get_template("page.html")
        rendered = template.render(**site_context, page=page, content=html_content, toc=toc_html)

        if page.slug == "":
            out_path = output_dir / "index.html"
        else:
            page_dir = output_dir / page.slug
            page_dir.mkdir(parents=True, exist_ok=True)
            out_path = page_dir / "index.html"

        out_path.write_text(rendered)

    # Step 4: Process each collection
    for coll_name, coll_config in config.collections.items():
        _build_collection(
            coll_name, coll_config, content_dir, output_dir, md, env, site_context
        )

    # Step 5: Copy static assets from theme
    _copy_static_assets(config.theme.name, output_dir)

    # Step 6: Write Pygments CSS
    css_dir = output_dir / "static" / "css"
    css_dir.mkdir(parents=True, exist_ok=True)
    (css_dir / "pygments.css").write_text(get_pygments_css())

    # Step 7: Copy user static assets if they exist
    user_static = project_dir / config.content.dir / "static"
    if user_static.exists():
        shutil.copytree(user_static, output_dir / "static", dirs_exist_ok=True)


def _build_collection(
    coll_name: str,
    coll_config: CollectionConfig,
    content_dir: Path,
    output_dir: Path,
    md,
    env,
    site_context: dict,
) -> None:
    """Build all outputs for a single collection."""
    entries_dir = content_dir / coll_name
    is_dated = coll_config.sort in ("newest_first", "oldest_first")

    entries = discover_entries(entries_dir, sort=coll_config.sort, require_date=is_dated)

    # Filter drafts
    entries = [e for e in entries if not e.draft]

    # Build collection context for templates
    collection = CollectionContext(
        name=coll_name,
        label=coll_name.replace("-", " ").replace("_", " ").title(),
        url_prefix=f"/{coll_name}/",
        layout=coll_config.layout,
        date_format=coll_config.date_format,
    )

    # Collect tags for this collection
    all_tags = collect_tags(entries)

    # Render individual entries
    for entry in entries:
        html_content, toc_html = render_markdown(md, entry.content_markdown)
        template = env.get_template("entry.html")
        formatted_date = ""
        if entry.date:
            formatted_date = entry.date.strftime(coll_config.date_format)
        reading_time = estimate_reading_time(entry.content_markdown)
        rendered = template.render(
            **site_context,
            entry=entry,
            post=entry,  # backward compat
            content=html_content,
            toc=toc_html,
            formatted_date=formatted_date,
            reading_time=reading_time,
            collection=collection,
            all_tags=all_tags,
        )

        entry_dir = output_dir / coll_name / entry.slug
        entry_dir.mkdir(parents=True, exist_ok=True)
        (entry_dir / "index.html").write_text(rendered)

    # Render collection index
    _render_collection_index(entries, coll_config, collection, all_tags, env, site_context, output_dir)

    # Render archive (if enabled and collection is dated)
    if coll_config.archive and is_dated:
        _render_archive(entries, collection, env, site_context, output_dir, coll_config)

    # Render tag pages (if enabled)
    if coll_config.tags and all_tags:
        _render_tag_pages(entries, all_tags, collection, env, site_context, output_dir, coll_config)


def _render_collection_index(
    entries: list[Entry],
    coll_config: CollectionConfig,
    collection: CollectionContext,
    all_tags: dict[str, list[Entry]],
    env,
    site_context: dict,
    output_dir: Path,
) -> None:
    """Render the collection index page."""
    template = env.get_template("collection_index.html")

    if coll_config.items_per_page > 0:
        page_entries = entries[: coll_config.items_per_page]
    else:
        page_entries = entries

    rendered = template.render(
        **site_context,
        entries=page_entries,
        posts=page_entries,  # backward compat
        collection=collection,
        all_tags=all_tags,
        layout=coll_config.layout,
    )

    coll_dir = output_dir / collection.name
    coll_dir.mkdir(parents=True, exist_ok=True)
    (coll_dir / "index.html").write_text(rendered)


def _render_archive(
    entries: list[Entry],
    collection: CollectionContext,
    env,
    site_context: dict,
    output_dir: Path,
    coll_config: CollectionConfig,
) -> None:
    """Render the archive page, grouping entries by year."""
    entries_by_year: dict[int, list[Entry]] = {}
    for entry in entries:
        if entry.date:
            entries_by_year.setdefault(entry.date.year, []).append(entry)

    template = env.get_template("archive.html")
    rendered = template.render(
        **site_context,
        entries_by_year=dict(sorted(entries_by_year.items(), reverse=True)),
        posts_by_year=dict(sorted(entries_by_year.items(), reverse=True)),  # backward compat
        collection=collection,
    )

    archive_dir = output_dir / collection.name / "archive"
    archive_dir.mkdir(parents=True, exist_ok=True)
    (archive_dir / "index.html").write_text(rendered)


def _render_tag_pages(
    entries: list[Entry],
    all_tags: dict[str, list[Entry]],
    collection: CollectionContext,
    env,
    site_context: dict,
    output_dir: Path,
    coll_config: CollectionConfig,
) -> None:
    """Render a page for each tag within a collection."""
    template = env.get_template("tag.html")

    tags_dir = output_dir / collection.name / "tags"
    tags_dir.mkdir(parents=True, exist_ok=True)

    # Tag index page
    index_template = env.get_template("tags_index.html")
    rendered = index_template.render(**site_context, tags=all_tags, collection=collection)
    (tags_dir / "index.html").write_text(rendered)

    # Individual tag pages
    for tag, tag_entries in all_tags.items():
        tag_slug = tag.lower().replace(" ", "-")
        rendered = template.render(
            **site_context,
            tag=tag,
            entries=tag_entries,
            posts=tag_entries,  # backward compat
            collection=collection,
        )

        tag_dir = tags_dir / tag_slug
        tag_dir.mkdir(parents=True, exist_ok=True)
        (tag_dir / "index.html").write_text(rendered)


def _copy_static_assets(theme_name: str, output_dir: Path) -> None:
    """Copy static assets from the theme to the output directory."""
    theme_static = Path(__file__).parent / "themes" / theme_name / "static"
    if theme_static.exists():
        shutil.copytree(theme_static, output_dir / "static", dirs_exist_ok=True)

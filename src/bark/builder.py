"""Main build pipeline for Bark."""

import math
import shutil
from pathlib import Path

from bark.config import BarkConfig
from bark.content import Post, discover_pages, discover_posts
from bark.renderer import create_markdown_renderer, get_pygments_css, load_theme, render_markdown

WORDS_PER_MINUTE = 200


def estimate_reading_time(text: str) -> int:
    """Estimate reading time in minutes from raw markdown text."""
    word_count = len(text.split())
    return max(1, math.ceil(word_count / WORDS_PER_MINUTE))


def collect_tags(posts: list[Post]) -> dict[str, list[Post]]:
    """Group posts by tag."""
    tags: dict[str, list[Post]] = {}
    for post in posts:
        for tag in post.tags:
            tags.setdefault(tag, []).append(post)
    return dict(sorted(tags.items()))


def build_site(config: BarkConfig, project_dir: Path) -> None:
    """Execute the full build pipeline."""
    output_dir = project_dir / config.build.output_dir
    content_dir = project_dir / config.content.dir
    posts_dir = content_dir / config.content.posts_dir

    # Step 1: Clean output directory
    if output_dir.exists():
        shutil.rmtree(output_dir)
    output_dir.mkdir(parents=True)

    # Step 2: Discover content
    pages = discover_pages(content_dir, config.content.posts_dir)
    posts = discover_posts(posts_dir, sort=config.blog.sort)

    # Step 3: Filter drafts
    posts = [p for p in posts if not p.draft]

    # Step 4: Extract tags
    all_tags = collect_tags(posts)

    # Step 5: Set up renderer
    md = create_markdown_renderer()
    env = load_theme(config.theme.name)

    # Step 6: Shared template context
    site_context = {
        "site": config.site,
        "nav": config.nav,
        "all_tags": all_tags,
        "config": config,
    }

    # Step 7: Render individual pages
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

    # Step 8: Render individual posts
    for post in posts:
        html_content, toc_html = render_markdown(md, post.content_markdown)
        template = env.get_template("post.html")
        formatted_date = post.date.strftime(config.blog.date_format)
        reading_time = estimate_reading_time(post.content_markdown)
        rendered = template.render(
            **site_context,
            post=post,
            content=html_content,
            toc=toc_html,
            formatted_date=formatted_date,
            reading_time=reading_time,
        )

        post_dir = output_dir / "posts" / post.slug
        post_dir.mkdir(parents=True, exist_ok=True)
        (post_dir / "index.html").write_text(rendered)

    # Step 9: Generate blog index page
    _render_index(posts, env, site_context, output_dir, config)

    # Step 10: Generate archive page
    if config.blog.archive:
        _render_archive(posts, env, site_context, output_dir, config)

    # Step 11: Generate tag pages
    if config.blog.tags:
        _render_tag_pages(posts, all_tags, env, site_context, output_dir, config)

    # Step 12: Copy static assets from theme
    _copy_static_assets(config.theme.name, output_dir)

    # Step 13: Write Pygments CSS
    css_dir = output_dir / "static" / "css"
    css_dir.mkdir(parents=True, exist_ok=True)
    (css_dir / "pygments.css").write_text(get_pygments_css())

    # Step 14: Copy user static assets if they exist
    user_static = project_dir / config.content.dir / "static"
    if user_static.exists():
        shutil.copytree(user_static, output_dir / "static", dirs_exist_ok=True)


def _render_index(
    posts: list[Post],
    env: "jinja2.Environment",
    site_context: dict,
    output_dir: Path,
    config: BarkConfig,
) -> None:
    """Render the blog index page with recent posts."""
    template = env.get_template("blog_index.html")
    page_posts = posts[: config.blog.posts_per_page]
    rendered = template.render(**site_context, posts=page_posts)

    blog_dir = output_dir / "posts"
    blog_dir.mkdir(parents=True, exist_ok=True)
    (blog_dir / "index.html").write_text(rendered)


def _render_archive(
    posts: list[Post],
    env: "jinja2.Environment",
    site_context: dict,
    output_dir: Path,
    config: BarkConfig,
) -> None:
    """Render the archive page, grouping posts by year."""
    posts_by_year: dict[int, list[Post]] = {}
    for post in posts:
        posts_by_year.setdefault(post.date.year, []).append(post)

    template = env.get_template("archive.html")
    rendered = template.render(**site_context, posts_by_year=dict(sorted(posts_by_year.items(), reverse=True)))

    archive_dir = output_dir / "archive"
    archive_dir.mkdir(parents=True, exist_ok=True)
    (archive_dir / "index.html").write_text(rendered)


def _render_tag_pages(
    posts: list[Post],
    all_tags: dict[str, list[Post]],
    env: "jinja2.Environment",
    site_context: dict,
    output_dir: Path,
    config: BarkConfig,
) -> None:
    """Render a page for each tag."""
    template = env.get_template("tag.html")

    tags_dir = output_dir / "tags"
    tags_dir.mkdir(parents=True, exist_ok=True)

    # Tag index page
    index_template = env.get_template("tags_index.html")
    rendered = index_template.render(**site_context, tags=all_tags)
    (tags_dir / "index.html").write_text(rendered)

    # Individual tag pages
    for tag, tag_posts in all_tags.items():
        tag_slug = tag.lower().replace(" ", "-")
        rendered = template.render(**site_context, tag=tag, posts=tag_posts)

        tag_dir = tags_dir / tag_slug
        tag_dir.mkdir(parents=True, exist_ok=True)
        (tag_dir / "index.html").write_text(rendered)


def _copy_static_assets(theme_name: str, output_dir: Path) -> None:
    """Copy static assets from the theme to the output directory."""
    theme_static = Path(__file__).parent / "themes" / theme_name / "static"
    if theme_static.exists():
        shutil.copytree(theme_static, output_dir / "static", dirs_exist_ok=True)

"""Template loading and HTML rendering."""

from pathlib import Path

import jinja2
import markdown as md_lib
from markupsafe import Markup
from pygments.formatters import HtmlFormatter


def create_markdown_renderer() -> md_lib.Markdown:
    """Create a Markdown instance with extensions for site content."""
    return md_lib.Markdown(
        extensions=[
            "meta",
            "fenced_code",
            "codehilite",
            "tables",
            "toc",
            "attr_list",
            "smarty",
            "admonition",
            "md_in_html",
            "bark.extensions.sidenotes",
        ],
        extension_configs={
            "codehilite": {"css_class": "highlight", "linenums": False},
            "toc": {"permalink": False, "toc_depth": "2-3"},
        },
    )


def load_theme(theme_name: str, custom_theme_dir: Path | None = None) -> jinja2.Environment:
    """Load a Jinja2 environment for the given theme.

    Checks for a custom theme directory first, then falls back to built-in themes.
    """
    loaders = []
    if custom_theme_dir and custom_theme_dir.exists():
        loaders.append(jinja2.FileSystemLoader(str(custom_theme_dir)))

    builtin_theme_dir = Path(__file__).parent / "themes" / theme_name
    if builtin_theme_dir.exists():
        loaders.append(jinja2.FileSystemLoader(str(builtin_theme_dir)))

    if not loaders:
        msg = f"Theme '{theme_name}' not found"
        raise FileNotFoundError(msg)

    return jinja2.Environment(
        loader=jinja2.ChoiceLoader(loaders),
        autoescape=jinja2.select_autoescape(["html"]),
    )


def render_markdown(md_renderer: md_lib.Markdown, source: str) -> tuple[Markup, Markup]:
    """Convert markdown to HTML, resetting the renderer between calls.

    Returns (html_content, toc_html) where toc_html is the table of contents
    generated from headings.
    """
    md_renderer.reset()
    html = Markup(md_renderer.convert(source))
    toc = Markup(getattr(md_renderer, "toc", ""))
    return html, toc


def get_pygments_css(style: str = "default") -> str:
    """Generate Pygments CSS for syntax highlighting."""
    formatter = HtmlFormatter(style=style)
    return formatter.get_style_defs(".highlight")

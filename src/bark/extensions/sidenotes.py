"""Sidenote Markdown extension for Bark.

Provides Tufte-style margin notes using fenced-div syntax:

    ::: sidenote Title of the sidenote
    Content here with **markdown** support.

    Can include images, GIFs, tables, code blocks, etc.
    :::

On desktop: The note header is always visible in the right margin.
Clicking expands the full body content. A numbered badge links them visually.

On mobile: The note is a full-width expandable panel.

Variants:
    ::: sidenote Title     — standard margin note
    ::: widget Title       — interactive widget placeholder
    ::: deepdive Title     — longer deep-dive expansion
    ::: aside Title        — lighter contextual aside
"""

from __future__ import annotations

import re

import markdown as md_lib
from markdown import Markdown
from markdown.extensions import Extension
from markdown.preprocessors import Preprocessor

SIDENOTE_OPEN = re.compile(
    r"^:{3}\s+(sidenote|widget|deepdive|aside)\s+(.+)$"
)
SIDENOTE_CLOSE = re.compile(r"^:{3}\s*$")

VARIANT_LABELS = {
    "sidenote": "Note",
    "widget": "Widget",
    "deepdive": "Deep dive",
    "aside": "Aside",
}


def _render_inner_markdown(lines: list[str]) -> str:
    """Render inner sidenote content using a fresh Markdown instance.

    Uses md_in_html so that raw HTML blocks with markdown="1" are processed.
    """
    inner_md = md_lib.Markdown(
        extensions=[
            "fenced_code",
            "codehilite",
            "tables",
            "attr_list",
            "smarty",
            "md_in_html",
        ],
        extension_configs={
            "codehilite": {"css_class": "highlight", "linenums": False},
        },
    )
    source = "\n".join(lines)
    return inner_md.convert(source)


class SidenotePreprocessor(Preprocessor):
    """Convert ::: sidenote blocks into Tufte-style margin note HTML.

    Outputs block-level <div> elements so the Markdown parser treats them
    as raw HTML blocks (no <p> wrapping, no broken nesting).
    JS handles the expand/collapse via an .is-open class toggle.
    """

    def run(self, lines: list[str]) -> list[str]:
        new_lines: list[str] = []
        i = 0
        note_counter = 0

        while i < len(lines):
            match = SIDENOTE_OPEN.match(lines[i])
            if match:
                variant = match.group(1)
                title = match.group(2).strip()
                label = VARIANT_LABELS.get(variant, "Note")
                note_counter += 1
                note_id = f"mn-{note_counter}"
                i += 1

                # Collect inner content until closing :::
                inner_lines: list[str] = []
                while i < len(lines) and not SIDENOTE_CLOSE.match(lines[i]):
                    inner_lines.append(lines[i])
                    i += 1
                if i < len(lines):
                    i += 1  # skip closing :::

                # Render inner content as HTML
                inner_html = _render_inner_markdown(inner_lines)

                # Output as a block-level HTML element.
                # Starting with <div on its own line (after a blank line)
                # ensures Python-Markdown treats it as a raw HTML block.
                new_lines.append("")
                new_lines.append(f'<div class="sidenote-block sidenote-block--{variant}" id="{note_id}">')
                new_lines.append(f'<div class="marginnote marginnote--{variant}">')
                new_lines.append(
                    f'<div class="marginnote-header" role="button" tabindex="0" aria-expanded="false">'
                    f'<span class="marginnote-label">{label}</span>'
                    f'<span class="marginnote-title">{title}</span>'
                    f'</div>'
                )
                new_lines.append(f'<div class="marginnote-body">')
                new_lines.append(inner_html)
                new_lines.append('</div>')
                new_lines.append('</div>')
                new_lines.append('</div>')
                new_lines.append("")
            else:
                new_lines.append(lines[i])
                i += 1

        return new_lines


class SidenoteExtension(Extension):
    """Markdown extension for Tufte-style margin sidenotes."""

    def extendMarkdown(self, md: Markdown) -> None:
        md.preprocessors.register(
            SidenotePreprocessor(md), "sidenotes", priority=105
        )


def makeExtension(**kwargs):  # noqa: N802
    """Entry point for Markdown extension loading."""
    return SidenoteExtension(**kwargs)

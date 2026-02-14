---
title: "Themes"
description: "How the default theme works and how to customise it."
---

# Themes

Bark uses Jinja2 templates and CSS for theming. The default theme is a professional, Tufte-inspired design with dark mode support.

## Default Theme

The built-in theme includes:

- **Inter** for UI text, **Source Serif 4** for body content, **JetBrains Mono** for code
- Light and dark colour schemes with CSS custom properties
- Responsive layout that adapts from mobile to wide desktop
- Sticky header with blur-through background
- Reading progress bar
- Tufte-style margin notes with breakout cards (desktop) and bottom sheets (mobile)
- Scroll-tracking table of contents (fixed left sidebar on wide screens)

## Dark Mode

The theme respects the system `prefers-color-scheme` preference on first visit. Users can toggle manually with the sun/moon button in the header. The preference is saved to `localStorage`.

All colours are defined as CSS custom properties on `:root` (light) and `[data-theme="dark"]` (dark), so switching is instant with no flash.

## Templates

The default theme includes these templates:

| Template | Used for |
|----------|----------|
| `base.html` | Shared layout: header, nav, footer, scripts |
| `page.html` | Static pages (about, contact, etc.) |
| `entry.html` | Collection entries (posts, projects, etc.) |
| `collection_index.html` | Collection index with layout switching |
| `archive.html` | Year-grouped archive listing |
| `tag.html` | Single tag listing |
| `tags_index.html` | All tags overview |

### Template Variables

All templates have access to:

| Variable | Description |
|----------|-------------|
| `site` | Site config (name, url, description, author) |
| `nav` | Navigation items list |
| `config` | Full Bark configuration |

Entry templates additionally get:

| Variable | Description |
|----------|-------------|
| `entry` | The entry object (title, slug, date, tags, description) |
| `content` | Rendered HTML content |
| `toc` | Table of contents HTML |
| `formatted_date` | Date string formatted per collection config |
| `reading_time` | Estimated minutes to read |
| `collection` | Collection context (name, label, url_prefix, layout) |

Collection index templates get:

| Variable | Description |
|----------|-------------|
| `entries` | List of entries for the current page |
| `collection` | Collection context |
| `layout` | Layout name (timeline, grid, minimal) |
| `all_tags` | Dict of tag name to entry list |

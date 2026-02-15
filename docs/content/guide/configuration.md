---
title: "Configuration"
description: "Full reference for opendoc.yml settings."
---

# Configuration

All OpenDoc settings live in `opendoc.yml` at the root of your project. Here is a complete example with all available options:

```yaml
site:
  name: "My Site"
  url: "https://example.com"
  description: "A personal website"
  author: "Your Name"

content:
  dir: "content"            # Where content lives (default: "content")

build:
  output_dir: "dist"        # Build output (default: "dist")

collections:
  writing:
    sort: "newest_first"    # newest_first | oldest_first | alphabetical
    date_format: "%B %d, %Y"
    items_per_page: 10      # 0 = show all
    tags: true
    archive: true
    layout: "timeline"      # timeline | grid | minimal

nav:
  - Home: index.md
  - About: about.md
  - Writing: writing/

theme:
  name: "default"
```

## Site

| Field | Default | Description |
|-------|---------|-------------|
| `name` | `"My Site"` | Site title, shown in header and page titles |
| `url` | `"https://example.com"` | Canonical URL for the site |
| `description` | `""` | Meta description for SEO |
| `author` | `""` | Author name, shown in post headers and footer |

## Content

| Field | Default | Description |
|-------|---------|-------------|
| `dir` | `"content"` | Root directory for all content files |

## Build

| Field | Default | Description |
|-------|---------|-------------|
| `output_dir` | `"dist"` | Directory where the static site is generated |

## Collections

Each key under `collections:` defines a named collection. The key name determines the content directory and URL prefix.

| Field | Default | Description |
|-------|---------|-------------|
| `sort` | `"newest_first"` | Sort order: `newest_first`, `oldest_first`, or `alphabetical` |
| `date_format` | `"%B %d, %Y"` | Python strftime format for displaying dates |
| `items_per_page` | `10` | Max entries on the index page (0 = show all) |
| `tags` | `true` | Generate per-tag pages at `/{collection}/tags/` |
| `archive` | `true` | Generate year-grouped archive at `/{collection}/archive/` |
| `layout` | `"timeline"` | Index layout: `timeline`, `grid`, or `minimal` |

## Navigation

The `nav:` list defines the site header links. Each item is a `Label: path` pair.

```yaml
nav:
  - Home: index.md          # Links to /
  - About: about.md         # Links to /about/
  - Writing: writing/       # Links to /writing/
```

Paths ending in `.md` are converted to clean URLs automatically (`about.md` becomes `/about/`). `index.md` maps to `/`.

## Theme

| Field | Default | Description |
|-------|---------|-------------|
| `name` | `"default"` | Theme to use for rendering |

## Backward Compatibility

If you have an older `opendoc.yml` with a `blog:` section instead of `collections:`, OpenDoc will automatically convert it:

```yaml
# Old format (still works)
content:
  posts_dir: "posts"
blog:
  posts_per_page: 10
  sort: "newest_first"

# Equivalent new format
collections:
  posts:
    items_per_page: 10
    sort: "newest_first"
    layout: "timeline"
```

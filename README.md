# Bark

[![PyPI version](https://img.shields.io/pypi/v/bark.svg)](https://pypi.org/project/bark/)
[![Python](https://img.shields.io/pypi/pyversions/bark.svg)](https://pypi.org/project/bark/)
[![CI](https://github.com/cottrellashley/bark/actions/workflows/ci.yml/badge.svg)](https://github.com/cottrellashley/bark/actions/workflows/ci.yml)
[![License: MIT](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)
[![Ruff](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json)](https://github.com/astral-sh/ruff)
[![uv](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/uv/main/assets/badge/v0.json)](https://github.com/astral-sh/uv)
[![Built with Bark](https://img.shields.io/badge/docs-built%20with%20Bark-orange)](https://github.com/cottrellashley/bark)
[![pre-commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit)](https://github.com/pre-commit/pre-commit)

A static site generator. Write content in markdown, organise it into collections, and build elegant static sites.

## Features

- **Collections** — organise content into named groups (writing, projects, notes, etc.)
- **Layouts** — timeline, grid, or minimal index pages per collection
- **Dark mode** — system-aware with manual toggle
- **Margin notes** — Tufte-style sidenotes with interactive widgets
- **Dev server** — live reload on file changes
- **Tags & archive** — per-collection tag pages and chronological archives
- **Syntax highlighting** — Pygments-powered code blocks

## Quick Start

```bash
# Create a new site
bark new my-site
cd my-site

# Build the site
bark build

# Serve locally with live reload
bark serve
```

## Configuration

Create a `bark.yml` in your project root:

```yaml
site:
  name: "My Site"
  url: "https://example.com"
  description: "A personal website"
  author: "Your Name"

collections:
  writing:
    sort: newest_first
    date_format: "%B %d, %Y"
    items_per_page: 10
    tags: true
    archive: true
    layout: timeline        # timeline | grid | minimal
  projects:
    sort: alphabetical
    items_per_page: 0       # 0 = show all
    tags: false
    archive: false
    layout: grid

nav:
  - Home: index.md
  - About: about.md
  - Writing: writing/
  - Projects: projects/
```

## Writing Content

Create markdown files in a collection directory with YAML frontmatter:

```markdown
---
title: "My First Post"
date: 2026-02-14
tags: [python, web]
description: "A short description"
---

Your content here...
```

Each collection lives in `content/{collection-name}/`. Pages (non-collection content) go directly in `content/`.

## Layouts

Each collection can use a different index layout:

| Layout | Best for | Description |
|--------|----------|-------------|
| `timeline` | Writing, blog, journal | Chronological list with dates and descriptions |
| `grid` | Projects, portfolio | Responsive card grid with hover effects |
| `minimal` | Notes, references, docs | Dense list of titles with optional dates |

## Installation

```bash
pip install bark
```

Or with [uv](https://docs.astral.sh/uv/):

```bash
uvx bark new my-site
```

## Documentation

The documentation is built with Bark itself. To view it locally:

```bash
make docs-serve
```

## Development

```bash
git clone https://github.com/cottrellashley/bark.git
cd bark
uv sync --dev
make test
```

## License

[MIT](LICENSE)

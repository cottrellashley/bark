---
title: "Getting Started"
---

# Getting Started

This guide walks you through creating your first Bark site from scratch.

## Installation

Install Bark with pip:

```bash
pip install bark
```

Or with [uv](https://docs.astral.sh/uv/):

```bash
uv add bark
```

## Create a New Site

Scaffold a new project:

```bash
bark new my-site
```

This creates the following structure:

```
my-site/
├── bark.yml                # Site configuration
├── content/
│   ├── index.md            # Home page
│   ├── about.md            # About page
│   └── writing/
│       └── hello-world.md  # First post
└── .gitignore
```

## Build and Serve

```bash
cd my-site
bark build    # Generates dist/
bark serve    # Starts dev server at http://localhost:8000
```

The dev server watches for changes and rebuilds automatically.

## Project Structure

A Bark project has three parts:

### 1. `bark.yml` — Configuration

All site settings live here: site metadata, collections, navigation, and theme.

```yaml
site:
  name: "My Site"
  author: "Your Name"

collections:
  writing:
    layout: timeline
    sort: newest_first

nav:
  - Home: index.md
  - Writing: writing/
```

### 2. `content/` — Your Content

Markdown files with YAML frontmatter. Top-level files become **pages**. Files inside collection directories become **entries**.

```markdown
---
title: "My First Post"
date: 2026-02-14
tags: [hello, bark]
description: "A short intro."
---

Your content here...
```

### 3. `dist/` — Generated Output

Running `bark build` produces a static site in `dist/`. Deploy this directory to any static host (GitHub Pages, Netlify, Vercel, S3, etc.).

## Next Steps

- [Configuration](/guide/configuration/) — full reference for `bark.yml`
- [Collections](/guide/collections/) — how to organise content
- [Layouts](/guide/layouts/) — timeline, grid, and minimal index styles
- [Margin Notes](/guide/margin-notes/) — Tufte-style sidenotes and widgets

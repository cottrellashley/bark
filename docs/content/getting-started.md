---
title: "Getting Started"
---

# Getting Started

This guide walks you through creating your first OpenDoc site from scratch.

## Installation

Install OpenDoc with pip:

```bash
pip install opendoc
```

Or with [uv](https://docs.astral.sh/uv/):

```bash
uv add opendoc
```

## Create a New Site

Scaffold a new project:

```bash
opendoc new my-site
```

This creates the following structure:

```
my-site/
├── opendoc.yml                # Site configuration
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
opendoc build    # Generates dist/
opendoc serve    # Starts dev server at http://localhost:8000
```

The dev server watches for changes and rebuilds automatically.

## Project Structure

An OpenDoc project has three parts:

### 1. `opendoc.yml` — Configuration

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
tags: [hello, opendoc]
description: "A short intro."
---

Your content here...
```

### 3. `dist/` — Generated Output

Running `opendoc build` produces a static site in `dist/`. Deploy this directory to any static host (GitHub Pages, Netlify, Vercel, S3, etc.).

## Next Steps

- [Configuration](/guide/configuration/) — full reference for `opendoc.yml`
- [Collections](/guide/collections/) — how to organise content
- [Layouts](/guide/layouts/) — timeline, grid, and minimal index styles
- [Margin Notes](/guide/margin-notes/) — Tufte-style sidenotes and widgets

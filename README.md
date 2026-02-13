# Bark

A blog-focused static site generator. Write your blog in markdown, configure with YAML, build elegant static sites.

## Features

- Markdown-based blog posts with YAML frontmatter
- YAML configuration for site settings and navigation
- Elegant, minimalist default theme
- Dev server with live reload
- Tag and archive page generation
- Syntax highlighting with Pygments
- Clean URLs (`/posts/my-post/`)

## Quick Start

```bash
# Create a new blog
bark new my-blog
cd my-blog

# Build the site
bark build

# Serve locally with live reload
bark serve
```

## Configuration

Create a `bark.yml` in your project root:

```yaml
site:
  name: "My Blog"
  url: "https://example.com"
  description: "A blog about things"
  author: "Your Name"

content:
  dir: "content"
  posts_dir: "posts"

build:
  output_dir: "dist"

nav:
  - Home: index.md
  - About: about.md
  - Blog: posts/

blog:
  posts_per_page: 10
  date_format: "%B %d, %Y"
  sort: "newest_first"
  tags: true
  archive: true
```

## Writing Posts

Create markdown files in `content/posts/` with YAML frontmatter:

```markdown
---
title: "My First Post"
date: 2026-02-13
tags: [python, blogging]
description: "A short description of the post"
---

Your post content here...
```

## Installation

```bash
pip install bark
```

Or run directly:

```bash
uvx bark build
```

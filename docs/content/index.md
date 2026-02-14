---
title: "Bark Documentation"
---

# Bark

A static site generator. Write content in markdown, organise it into collections, and build elegant static sites.

This documentation is itself built with Bark.

## Quick Start

```bash
bark new my-site
cd my-site
bark serve
```

That's it. You have a running site. Read the [Getting Started](/getting-started/) guide for the full walkthrough, or browse the [Guide](/guide/) for detailed reference on each feature.

## Key Concepts

**Pages** are standalone markdown files in `content/` — things like your home page, about page, or contact page.

**Collections** are groups of related content in subdirectories — writing, projects, notes, or whatever you need. Each collection has its own index page, layout, and optional tags and archive.

**Themes** control the visual presentation. Bark ships with a default theme featuring dark mode, responsive design, and Tufte-style margin notes.

## Features

- **Collections** — named content groups with independent settings
- **Layouts** — timeline, grid, or minimal index pages
- **Dark mode** — system-aware with manual toggle
- **Margin notes** — Tufte-style sidenotes with interactive widgets
- **Live reload** — dev server rebuilds on file changes
- **Tags & archive** — per-collection, auto-generated
- **Syntax highlighting** — Pygments-powered code blocks

---
title: "OpenDoc Documentation"
---

<p align="center">
  <img src="/static/img/logo.png" alt="OpenDoc" width="280">
</p>

A static site generator. Write content in markdown, organise it into collections, and build elegant static sites.

This documentation is itself built with OpenDoc.

## Quick Start

```bash
opendoc new my-site
cd my-site
opendoc serve
```

That's it. You have a running site. Read the [Getting Started](/getting-started/) guide for the full walkthrough, or browse the [Guide](/guide/) for detailed reference on each feature.

## Key Concepts

**Pages** are standalone markdown files in `content/` — things like your home page, about page, or contact page.

**Collections** are groups of related content in subdirectories — writing, projects, notes, or whatever you need. Each collection has its own index page, layout, and optional tags and archive.

**Themes** control the visual presentation. OpenDoc ships with a default theme featuring dark mode, responsive design, and Tufte-style margin notes.

## Features

- **Collections** — named content groups with independent settings
- **Layouts** — timeline, grid, or minimal index pages
- **Dark mode** — system-aware with manual toggle
- **Margin notes** — Tufte-style sidenotes with interactive widgets
- **LaTeX equations** — inline and display math via KaTeX, with equation numbering and cross-referencing
- **Theorem environments** — academic-style theorem, definition, lemma, proof blocks with auto-numbering
- **Tabbed code blocks** — switchable panels with emoji labels and copy-to-clipboard
- **Syntax highlighting** — Monokai colour scheme via Pygments
- **Live reload** — dev server rebuilds on file changes
- **Tags & archive** — per-collection, auto-generated

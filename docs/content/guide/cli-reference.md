---
title: "CLI Reference"
description: "Command-line interface for Bark."
---

# CLI Reference

Bark provides three commands: `new`, `build`, and `serve`.

## `bark new`

Scaffold a new project.

```bash
bark new <name>
```

Creates a directory with:

- `bark.yml` — default configuration
- `content/index.md` — home page
- `content/about.md` — about page
- `content/writing/hello-world.md` — example entry
- `.gitignore`

## `bark build`

Build the static site.

```bash
bark build [project_dir]
```

| Argument | Default | Description |
|----------|---------|-------------|
| `project_dir` | `.` (current directory) | Path to the project |

Reads `bark.yml`, processes all content, and writes the static site to the configured `output_dir` (default: `dist/`).

The build pipeline:

1. Clean the output directory
2. Discover pages and collection entries
3. Filter out drafts
4. Render pages using `page.html`
5. For each collection: render entries, index, tags, and archive
6. Copy theme static assets (CSS, JS)
7. Generate Pygments CSS for syntax highlighting
8. Copy user static assets from `content/static/`

## `bark serve`

Build and serve locally with live reload.

```bash
bark serve [project_dir] [--port PORT]
```

| Argument/Option | Default | Description |
|-----------------|---------|-------------|
| `project_dir` | `.` | Path to the project |
| `--port` | `8000` | Port number |

The server:

- Builds the site on startup
- Watches `content/` and `bark.yml` for changes
- Rebuilds automatically when files change
- Serves the built site over HTTP

## Static Assets

Place files in `content/static/` and they'll be copied to `dist/static/` during build. Reference them in your content with absolute paths:

```markdown
![My image](/static/images/photo.jpg)
```

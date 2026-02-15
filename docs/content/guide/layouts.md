---
title: "Layouts"
description: "Timeline, grid, and minimal index page layouts."
---

# Layouts

Each collection can use a different layout for its index page. Set the `layout` field in `opendoc.yml`:

```yaml
collections:
  writing:
    layout: timeline
  projects:
    layout: grid
  notes:
    layout: minimal
```

## Timeline

The default layout. A vertical list of entries sorted chronologically, showing date, tags, title, description, and a "Read more" link.

Best for: writing, blog posts, journals, changelogs.

```yaml
collections:
  writing:
    sort: newest_first
    layout: timeline
```

Each entry appears as a card with:

- Date and tags (top)
- Title (prominent)
- Description excerpt
- "Read more" link

Cards have a subtle hover effect with background highlight and lift.

## Grid

A responsive card grid. Entries are displayed as cards in a multi-column layout that adapts to screen width.

Best for: projects, portfolio, showcases, galleries.

```yaml
collections:
  projects:
    sort: alphabetical
    layout: grid
```

Each card shows:

- Title (prominent)
- Description (up to 3 lines, truncated)
- Footer with optional date and tag pills

The grid uses `auto-fill` with a 280px minimum column width, so it naturally adapts from 1 column on mobile to 3+ on wide screens. Cards have a border, and on hover they lift with an accent-coloured border.

## Minimal

A dense, clean list of titles. No descriptions, no cards, no visual embellishment.

Best for: notes, references, documentation, link collections.

```yaml
collections:
  notes:
    sort: newest_first
    layout: minimal
```

Each row shows:

- Date in monospace (if the entry has one)
- Title as a simple link

Rows are separated by light borders. Hovering a title highlights it with the accent colour.

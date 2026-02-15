---
title: "Collections"
description: "How to organise content into named groups."
---

# Collections

Collections are the core organisational unit in OpenDoc. Each collection is a named group of related content with its own directory, URL prefix, index page, and settings.

## Defining Collections

Add collections to `opendoc.yml`:

```yaml
collections:
  writing:
    sort: newest_first
    layout: timeline
    tags: true
    archive: true
  projects:
    sort: alphabetical
    layout: grid
    tags: false
    archive: false
  notes:
    sort: newest_first
    layout: minimal
    items_per_page: 0
```

## Directory Structure

Each collection maps to a directory under `content/`:

```
content/
├── index.md              # Home page (not a collection)
├── about.md              # About page (not a collection)
├── writing/              # "writing" collection
│   ├── first-post.md
│   └── second-post.md
├── projects/             # "projects" collection
│   ├── opendoc.md
│   └── quantum-sim.md
└── notes/                # "notes" collection
    └── random-thought.md
```

## Entries

Each markdown file in a collection directory is an **entry**. Entries use YAML frontmatter for metadata:

```markdown
---
title: "My Entry"
date: 2026-02-14           # Optional for undated collections
tags: [python, web]         # Optional
description: "A summary"    # Optional, shown on index pages
draft: true                 # Optional, excluded from build
---

Content goes here...
```

### Dated vs. Undated Collections

If a collection uses `sort: newest_first` or `sort: oldest_first`, entries are expected to have a `date` field. Missing dates default to today.

If a collection uses `sort: alphabetical`, dates are optional. Entries without dates simply won't display a date on index pages.

## Generated Output

For a collection named `writing`, OpenDoc generates:

| Path | Content |
|------|---------|
| `/writing/` | Collection index page (using the configured layout) |
| `/writing/{slug}/` | Individual entry pages |
| `/writing/tags/` | Tag index (if `tags: true`) |
| `/writing/tags/{tag}/` | Per-tag listing |
| `/writing/archive/` | Year-grouped archive (if `archive: true`) |

## Pages vs. Collections

**Pages** are top-level `.md` files in `content/` (excluding collection directories). They have no date, no tags, and use the `page.html` template. Examples: home page, about page, contact page.

**Collection entries** are `.md` files inside a collection directory. They support dates, tags, descriptions, and drafts, and use the `entry.html` template.

"""Scaffold a new Bark project."""

from pathlib import Path

BARK_YML = """\
site:
  name: "{name}"
  url: "https://example.com"
  description: "A new site built with Bark"
  author: ""

content:
  dir: "content"

build:
  output_dir: "dist"

collections:
  writing:
    sort: "newest_first"
    date_format: "%B %d, %Y"
    items_per_page: 10
    tags: true
    archive: true
    layout: "timeline"

nav:
  - Home: index.md
  - About: about.md
  - Writing: writing/

theme:
  name: "default"
"""

INDEX_MD = """\
---
title: "Home"
---

# Welcome to {name}

This is your new site, built with [Bark](https://github.com/cottrellashley/bark).

Check out the [writing](/writing/) or read [about](/about/) this site.
"""

ABOUT_MD = """\
---
title: "About"
---

# About

This site is powered by **Bark**, a static site generator.

Write your content in markdown, configure with YAML, and build elegant static sites.
"""

HELLO_WORLD_MD = """\
---
title: "Hello World"
date: 2026-02-14
tags: [getting-started, bark]
description: "Your first post with Bark."
---

# Hello World

Welcome to your first Bark post!

## Writing Content

Posts are just markdown files with YAML frontmatter. Put them in `content/writing/` and Bark
will take care of the rest.

### Code highlighting

```python
def hello():
    print("Hello from Bark!")
```

### Lists

- Write in markdown
- Configure with YAML
- Build with `bark build`
- Serve with `bark serve`

Happy writing!
"""

GITIGNORE = """\
dist/
.DS_Store
"""


def create_project(name: str) -> Path:
    """Create a new Bark project."""
    project_dir = Path(name)
    if project_dir.exists():
        msg = f"Directory '{name}' already exists"
        raise FileExistsError(msg)

    project_dir.mkdir()
    content_dir = project_dir / "content"
    writing_dir = content_dir / "writing"
    writing_dir.mkdir(parents=True)

    (project_dir / "bark.yml").write_text(BARK_YML.format(name=name))
    (content_dir / "index.md").write_text(INDEX_MD.format(name=name))
    (content_dir / "about.md").write_text(ABOUT_MD)
    (writing_dir / "hello-world.md").write_text(HELLO_WORLD_MD)
    (project_dir / ".gitignore").write_text(GITIGNORE)

    return project_dir

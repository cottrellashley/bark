"""Scaffold a new Bark blog project."""

from pathlib import Path

BARK_YML = """\
site:
  name: "{name}"
  url: "https://example.com"
  description: "A new blog built with Bark"
  author: ""

content:
  dir: "content"
  posts_dir: "posts"

build:
  output_dir: "dist"

nav:
  - Home: index.md
  - About: about.md
  - Blog: posts/

theme:
  name: "default"

blog:
  posts_per_page: 10
  date_format: "%B %d, %Y"
  sort: "newest_first"
  tags: true
  archive: true
"""

INDEX_MD = """\
---
title: "Home"
---

# Welcome to {name}

This is your new blog, built with [Bark](https://github.com/cottrellashley/bark).

Check out the [blog posts](/posts/) or read [about](/about/) this site.
"""

ABOUT_MD = """\
---
title: "About"
---

# About

This blog is powered by **Bark**, a blog-focused static site generator.

Write your posts in markdown, configure with YAML, and build elegant static sites.
"""

HELLO_WORLD_MD = """\
---
title: "Hello World"
date: 2026-02-13
tags: [getting-started, bark]
description: "Your first blog post with Bark."
---

# Hello World

Welcome to your first Bark blog post!

## Writing Posts

Posts are just markdown files with YAML frontmatter. Put them in `content/posts/` and Bark
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

Happy blogging!
"""

GITIGNORE = """\
dist/
.DS_Store
"""


def create_project(name: str) -> Path:
    """Create a new Bark blog project."""
    project_dir = Path(name)
    if project_dir.exists():
        msg = f"Directory '{name}' already exists"
        raise FileExistsError(msg)

    project_dir.mkdir()
    content_dir = project_dir / "content"
    posts_dir = content_dir / "posts"
    posts_dir.mkdir(parents=True)

    (project_dir / "bark.yml").write_text(BARK_YML.format(name=name))
    (content_dir / "index.md").write_text(INDEX_MD.format(name=name))
    (content_dir / "about.md").write_text(ABOUT_MD)
    (posts_dir / "hello-world.md").write_text(HELLO_WORLD_MD)
    (project_dir / ".gitignore").write_text(GITIGNORE)

    return project_dir

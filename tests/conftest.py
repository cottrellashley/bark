"""Shared test fixtures for Bark."""

from pathlib import Path

import pytest


SAMPLE_BARK_YML = """\
site:
  name: "Test Blog"
  url: "https://test.com"
  description: "A test blog"
  author: "Tester"

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
  posts_per_page: 5
  date_format: "%B %d, %Y"
  sort: "newest_first"
  tags: true
  archive: true

theme:
  name: "default"
"""

SAMPLE_INDEX_MD = """\
---
title: "Home"
---

# Welcome

This is the home page.
"""

SAMPLE_ABOUT_MD = """\
---
title: "About"
---

# About

This is the about page.
"""

SAMPLE_POST_MD = """\
---
title: "Test Post"
date: 2026-01-15
tags: [python, testing]
description: "A test post"
---

# Test Post

This is a test post with **bold** and `code`.

```python
print("hello")
```
"""

SAMPLE_POST_2_MD = """\
---
title: "Second Post"
date: 2026-02-01
tags: [python]
description: "Another test post"
---

# Second Post

Content here.
"""

SAMPLE_DRAFT_MD = """\
---
title: "Draft Post"
date: 2026-02-10
tags: [draft]
draft: true
---

# Draft

This should not appear.
"""


@pytest.fixture
def tmp_project(tmp_path: Path) -> Path:
    """Create a temporary blog project with sample content."""
    content_dir = tmp_path / "content"
    posts_dir = content_dir / "posts"
    posts_dir.mkdir(parents=True)

    (tmp_path / "bark.yml").write_text(SAMPLE_BARK_YML)
    (content_dir / "index.md").write_text(SAMPLE_INDEX_MD)
    (content_dir / "about.md").write_text(SAMPLE_ABOUT_MD)
    (posts_dir / "test-post.md").write_text(SAMPLE_POST_MD)
    (posts_dir / "second-post.md").write_text(SAMPLE_POST_2_MD)
    (posts_dir / "draft-post.md").write_text(SAMPLE_DRAFT_MD)

    return tmp_path

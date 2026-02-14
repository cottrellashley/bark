---
title: "The Physics of Static Sites"
date: 2026-02-14
tags: [physics, web, performance]
description: "Why static sites are like elegant physics — minimal moving parts, maximum results."
---

# The Physics of Static Sites

In physics, the most beautiful theories are often the simplest. Static sites follow the same principle.

## The Principle of Least Action

Just as nature chooses the path of least action, static site generators strip away unnecessary complexity:

- **No database queries** at request time
- **No server-side rendering** per visit
- **No runtime dependencies** to break

The result? A site that loads at the speed of light (well, the speed of your CDN).

## Performance Equation

The load time of a static site can be approximated as:

```
t_load ≈ t_network + t_parse
```

Compare that to a dynamic site:

```
t_load ≈ t_network + t_server + t_database + t_render + t_parse
```

Every extra term is a potential point of failure.

## Code Example

Here's a simple benchmark in Python:

```python
import time

def static_response():
    """Read pre-built HTML from disk."""
    with open("dist/index.html") as f:
        return f.read()

def dynamic_response():
    """Query DB, render template, return HTML."""
    data = query_database()  # ~50ms
    html = render_template(data)  # ~20ms
    return html

# Static wins every time
start = time.perf_counter()
static_response()
print(f"Static: {time.perf_counter() - start:.4f}s")
```

## Conclusion

Like a well-formulated physics equation, a static site is **complete, deterministic, and fast**. Bark embraces this philosophy — build once, serve forever.

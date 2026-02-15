---
title: "Code Blocks"
description: "Syntax highlighting, tabbed code blocks, and copy buttons."
---

# Code Blocks

OpenDoc provides rich code block support powered by Pygments for syntax highlighting, with tabbed interfaces and copy-to-clipboard buttons built in.

## Basic Code Blocks

Use standard fenced code blocks with a language identifier:

````markdown
```python
def hello():
    print("Hello, world!")
```
````

OpenDoc uses Pygments with the Monokai colour scheme for syntax highlighting. All code blocks use a dark background that works well in both light and dark mode.

Supported languages include Python, JavaScript, TypeScript, Rust, Go, Bash, SQL, YAML, TOML, Makefile, and [many more](https://pygments.org/languages/).

## Copy Button

Every code block automatically gets a copy-to-clipboard button that appears on hover. Click it to copy the code contents. The button shows a checkmark for 2 seconds after copying.

No configuration is needed — copy buttons are enabled by default for all `<pre>` blocks.

## Tabbed Code Blocks

Use the `:::tabs` syntax to create tabbed interfaces for showing alternative code variants:

````markdown
:::tabs
=== Python 🐍
```python
print("Hello")
```
=== JavaScript 💛
```javascript
console.log("Hello");
```
=== Rust 🦀
```rust
fn main() {
    println!("Hello");
}
```
:::
````

### Syntax

| Element | Description |
|---------|-------------|
| `:::tabs` | Opens a tab group |
| `=== Label` | Starts a new tab with the given label |
| `:::` | Closes the tab group |

Tab labels can include emoji, which is useful for visually distinguishing tools:

```markdown
:::tabs
=== pip 🐍
...
=== uv ⚡
...
=== pipx 📦
...
:::
```

### Content

Each tab can contain any markdown content — not just code blocks. You can include paragraphs, lists, or multiple code blocks within a single tab.

### Behaviour

- The first tab is active by default
- Clicking a tab switches the visible panel
- Each tab group is independent
- Tab navigation scrolls horizontally on narrow screens
- Copy buttons work inside tabbed code blocks

## Inline Code

Use single backticks for inline code: `` `variable_name` ``. Inline code uses a subtle background that adapts to light/dark mode.

## Styling

Code blocks use the following design tokens from the theme:

| Token | Description |
|-------|-------------|
| `--color-code-bg` | Code block background |
| `--color-code-text` | Code block text colour |
| `--font-mono` | Monospace font stack (JetBrains Mono) |

The tab bar uses a slightly darker shade of the code background, with an accent-coloured bottom border on the active tab.

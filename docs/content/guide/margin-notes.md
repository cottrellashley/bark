---
title: "Margin Notes"
description: "Tufte-style sidenotes, widgets, and deep dives."
---

# Margin Notes

Bark supports Tufte-style margin notes — supplementary content that appears alongside the main text. On desktop, they float in the right margin. On mobile, they appear as tappable links that open a bottom sheet.

## Syntax

Use the `:::sidenote` fenced block syntax:

```markdown
:::sidenote Some Title | variant
Content of the margin note goes here.

You can use **markdown** formatting, code blocks, images, and even interactive HTML.
:::
```

### Variants

The text after the pipe `|` sets the variant, which controls the accent colour:

| Variant | Colour | Use for |
|---------|--------|---------|
| `sidenote` | Indigo | General supplementary notes |
| `widget` | Teal | Interactive elements, demos |
| `deepdive` | Purple | Extended explanations, proofs |
| `aside` | Grey | Tangential remarks |

Example:

```markdown
:::sidenote Energy Conservation | deepdive
A deeper look at why energy is conserved in closed systems...
:::
```

## Behaviour

### Desktop (1100px+)

Margin notes appear as small text links in the right margin, positioned below section headings. Clicking a link opens a floating card with the full content. The card is scrollable for long content. Click the backdrop or press Escape to dismiss.

### Mobile

Margin notes appear as inline text links with a subtle left border. Tapping opens a bottom sheet that slides up from the bottom of the screen with a drag handle.

## Interactive Widgets

You can embed HTML, CSS, and JavaScript inside margin notes using the `md_in_html` extension:

```markdown
:::sidenote Wave Simulator | widget

<div markdown="1">

<canvas id="wave" width="300" height="150"></canvas>
<button onclick="startWave()">Start</button>

<script>
function startWave() {
    // Your interactive code here
}
</script>

</div>

:::
```

Bark's theme automatically styles buttons, range inputs, and canvas elements inside margin notes to match the current theme (including dark mode).

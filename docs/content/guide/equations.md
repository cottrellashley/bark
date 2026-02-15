---
title: "Equations & Math"
description: "LaTeX equations, equation numbering, and theorem environments."
---

# Equations & Math

OpenDoc supports LaTeX mathematics rendered client-side with [KaTeX](https://katex.org/). Write equations the same way you would in a LaTeX paper — inline with `$...$` and display with `$$...$$`.

## Inline Math

Wrap LaTeX in single dollar signs for inline expressions:

```markdown
The energy-momentum relation $E^2 = (pc)^2 + (mc^2)^2$ reduces to
$E = mc^2$ in the rest frame.
```

Inline math blends with the surrounding body text at the same font size. Markdown-special characters like `_` and `*` inside dollar signs are automatically escaped so they don't trigger emphasis or subscript formatting.

## Display Equations

Use double dollar signs on their own lines for centred, display-mode equations:

```markdown
$$
\nabla \times \mathbf{E} = -\frac{\partial \mathbf{B}}{\partial t}
$$
```

Display equations are centred with vertical breathing room, rendered slightly larger than body text for readability.

## Equation Numbering

Append `{#eq:label}` after the closing `$$` to add a right-aligned equation number:

```markdown
$$
i\hbar \frac{\partial}{\partial t} \Psi = \hat{H} \Psi
$$ {#eq:schrodinger}
```

This produces a numbered equation with an anchor ID, rendering as:

> *i*ℏ ∂/∂*t* Ψ = *Ĥ* Ψ &emsp;&emsp;&emsp; (1)

Equation numbers are auto-incremented per page starting from 1. The `{#eq:label}` also creates an HTML `id` attribute, so you can link to equations:

```markdown
As shown in Equation (1), the time evolution is governed by...
```

## LaTeX Environments

KaTeX supports standard LaTeX environments. The preprocessor protects them from Markdown processing:

```markdown
\begin{equation}
  F = ma
\end{equation}

\begin{align}
  \nabla \cdot \mathbf{E} &= \frac{\rho}{\epsilon_0} \\
  \nabla \cdot \mathbf{B} &= 0
\end{align}
```

Supported environments: `equation`, `align`, `alignat`, `gather`, `multline` (and their starred variants).

## Theorem Environments

OpenDoc provides academic-style theorem environments using the `:::` fenced block syntax:

### Available Environments

| Environment | Syntax | Style |
|-------------|--------|-------|
| Theorem | `:::theorem` | Blue accent border, auto-numbered |
| Definition | `:::definition` | Orange accent border, auto-numbered |
| Lemma | `:::lemma` | Green accent border, auto-numbered |
| Proposition | `:::proposition` | Purple accent border, auto-numbered |
| Corollary | `:::corollary` | Default border, auto-numbered |
| Remark | `:::remark` | Default border, auto-numbered |
| Proof | `:::proof` | Grey border, italic label, QED tombstone |

### Syntax

```markdown
:::theorem Noether
For every differentiable symmetry of the action of a physical
system, there exists a corresponding conservation law.
:::
```

The text after the environment name is an optional title. It renders as:

> **THEOREM 1 (Noether)** — For every differentiable symmetry of the action of a physical system, there exists a corresponding conservation law.

### With Equations Inside

Theorem environments support full markdown including equations:

```markdown
:::definition Lagrangian
The *Lagrangian* of a mechanical system is:

$$
\mathcal{L}(q, \dot{q}, t) = T(\dot{q}) - V(q)
$$
:::
```

### Proofs

Proofs automatically include a QED tombstone symbol (■):

```markdown
:::proof
By Noether's theorem, time-translation invariance implies
conservation of the Hamiltonian. Since
$\frac{\partial \mathcal{L}}{\partial t} = 0$,
we have $\frac{dH}{dt} = 0$.
:::
```

### Numbering

Theorems, definitions, lemmas, and propositions are auto-numbered independently per type within each page. Proofs and remarks are not numbered.

## Supported LaTeX Commands

OpenDoc uses KaTeX 0.16.28, which supports a wide range of LaTeX commands. Some commonly used ones:

| Category | Examples |
|----------|---------|
| Greek | `\alpha`, `\beta`, `\gamma`, `\Gamma`, `\omega`, `\Omega` |
| Operators | `\sum`, `\prod`, `\int`, `\oint`, `\nabla`, `\partial` |
| Relations | `\leq`, `\geq`, `\neq`, `\approx`, `\equiv`, `\sim` |
| Arrows | `\rightarrow`, `\leftarrow`, `\Rightarrow`, `\mapsto` |
| Accents | `\hat{x}`, `\bar{x}`, `\vec{x}`, `\dot{x}`, `\tilde{x}` |
| Fonts | `\mathbf`, `\mathcal`, `\mathbb`, `\mathrm`, `\mathfrak` |
| Layout | `\frac`, `\sqrt`, `\binom`, `\overset`, `\underset` |
| Delimiters | `\left(`, `\right)`, `\langle`, `\rangle`, `\|` |

For the full list, see the [KaTeX supported functions](https://katex.org/docs/supported).

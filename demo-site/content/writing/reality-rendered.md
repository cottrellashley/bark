---
title: "Reality, Rendered"
date: 2026-02-14
tags: [philosophy, physics, consciousness, ontology]
description: "If objects are compression products, then objecthood is interface-dependent. This is not nihilism — it is an ontological reclassification."
---

# Reality, Rendered

I begin with one statement that is exceedingly hard to deny without performing it: **something seems to be happening**. From that axiom I build a minimal "tree of access" that separates **seeming** (the fact of appearance) from **something** (what appears).

## The Axiom

I start with a claim so small it refuses to pick sides: **something seems to be happening**. If I deny it, I perform it; denial itself is a kind of seeming. If I doubt it, the doubt is still an appearance.

The axiom contains two components:

- **Seeming**: the fact that anything appears at all.
- **Something**: the content that appears — sensory fields, thoughts, memories, the felt world.

::: sidenote The swap intuition pump
If I imaginatively swap the **contents** — memories, self-image, mood, sensory field — the world changes dramatically. If I try to imagine swapping the bare **fact of seeming** while holding contents fixed, nothing about the presentation obviously changes.

It is like swapping the existence of the screen versus swapping the frames of the film: most of what I identify as "me" lives in the frames.

**Alternate phrasings:**
- "Appearance is undeniable; interpretation is optional."
- "Whatever reality is, it is currently showing up."
- "We start from the one fact we cannot performatively disown."
:::

::: widget Axiom tester
Try to break the axiom. Click any operation below:

<div class="axiom-tester" style="margin: 0.75rem 0;">
<div style="display: flex; flex-wrap: wrap; gap: 0.375rem; margin-bottom: 0.75rem;">
<button onclick="this.closest('.axiom-tester').querySelector('.axiom-result').style.display='block'">Deny it</button>
<button onclick="this.closest('.axiom-tester').querySelector('.axiom-result').style.display='block'">Doubt it</button>
<button onclick="this.closest('.axiom-tester').querySelector('.axiom-result').style.display='block'">Forget it</button>
<button onclick="this.closest('.axiom-tester').querySelector('.axiom-result').style.display='block'">Dream it</button>
<button onclick="this.closest('.axiom-tester').querySelector('.axiom-result').style.display='block'">Reduce it</button>
</div>
<div class="axiom-result" style="display: none; padding: 0.625rem 0.75rem; background: var(--color-accent-soft); border-radius: 6px; font-size: 0.8125rem; font-style: italic; border-left: 3px solid var(--color-accent); color: var(--color-text);">
Still: <strong>something seems to be happening.</strong>
</div>
</div>

No matter which operation you apply, the axiom regenerates. This is what makes it an accounting rule, not a metaphysical claim.
:::

## The Tree of Access

Before I argue about what reality is, I want to be explicit about what my starting data are. The "tree" is not an ontology of the universe; it is an ontology of **access** — what I can justifiably talk about starting from the axiom.

The contents of experience divide into two practical kinds:

- **Private**: what is directly accessible only from one perspective (pain, shame, blueness-as-felt).
- **Public**: what is stable enough that multiple observers can coordinate on it (tables, instruments, reproducible readings).

::: sidenote The ink doesn't change, but the object does
Ambiguous figures give a clean demonstration that "objecthood" is not simply stamped onto the stimulus. The same image can flip between two stable interpretations; nothing external changes, but the perceived "thing" does.

This is a standard theme in work on multistable perception and reversible figures.
:::

::: widget Perception flip — the renderer shapes what you see
The exact same stimulus, two stable percepts. Your visual system forces a choice:

<div class="flip-widget" style="margin: 0.75rem 0; text-align: center;">
<div style="display: inline-block; width: 120px; height: 120px; border: 2px solid var(--color-text-muted); border-radius: 8px; position: relative; margin-bottom: 0.75rem; cursor: pointer; opacity: 0.85;" onclick="var s=this.dataset.state||'a'; this.dataset.state=s==='a'?'b':'a'; this.querySelector('.face-a').style.opacity=s==='a'?'0':'1'; this.querySelector('.face-b').style.opacity=s==='a'?'1':'0'; this.closest('.flip-widget').querySelector('.flip-label').textContent=s==='a'?'Interpretation B: old woman':'Interpretation A: young woman';">
<svg viewBox="0 0 100 100" style="width:100%;height:100%;">
<line x1="30" y1="25" x2="50" y2="20" stroke="currentColor" stroke-width="2"/>
<line x1="50" y1="20" x2="70" y2="25" stroke="currentColor" stroke-width="2"/>
<ellipse cx="42" cy="38" rx="4" ry="3" fill="currentColor" class="face-a" style="transition:opacity 0.3s"/>
<ellipse cx="58" cy="38" rx="4" ry="3" fill="currentColor" class="face-a" style="transition:opacity 0.3s"/>
<path d="M 42 55 Q 50 65 58 55" stroke="currentColor" stroke-width="2" fill="none" class="face-a" style="transition:opacity 0.3s"/>
<circle cx="42" cy="38" r="2" fill="currentColor" class="face-b" style="opacity:0;transition:opacity 0.3s"/>
<circle cx="58" cy="38" r="2" fill="currentColor" class="face-b" style="opacity:0;transition:opacity 0.3s"/>
<path d="M 42 55 Q 50 48 58 55" stroke="currentColor" stroke-width="2" fill="none" class="face-b" style="opacity:0;transition:opacity 0.3s"/>
<ellipse cx="50" cy="75" rx="18" ry="5" stroke="currentColor" stroke-width="1.5" fill="none"/>
</svg>
</div>
<div class="flip-label" style="font-size: 0.75rem; color: var(--color-text-muted);">Click the figure to flip interpretation</div>
</div>

The stimulus hasn't changed. Only your renderer has. This is the pre-image / image distinction made visceral.
:::

The public branch splits again:

- **Observed objects**: what is straightforwardly present in perception or instrument readout.
- **Inferred objects**: posits introduced to compress, predict, and unify observations (molecules, fields, wavefunctions).

## Compression Is Why Objects Exist

Limited systems compress; objects are compression outputs. The guiding principle is a trade-off between complexity and predictive power.

When a system cannot store or compute over all details, it must summarise. This is not just a metaphor — it is a general constraint on modelling and prediction. The mind searches for descriptions that are:

- simple enough to be usable (low complexity),
- rich enough to forecast and control (high predictive power).

A "thing" is a stable summary that supports successful prediction and action at the observer's scale. It is a handle. It is a noun that earns its keep.

::: deepdive Degrees of reality — when does a pattern earn "thinghood"?
Not all emergent descriptions are equally legitimate. An emergent description is more thing-like insofar as it has:

1. **Compression gain**: large predictive payoff with fewer parameters.
2. **Robustness**: persistence under perturbation and noise.
3. **Autonomy**: approximately closed, reusable dynamics at its own level.
4. **Intersubjective reproducibility**: stable identification across observers, instruments, and modelling choices.

| Criterion | Operational question | Why it matters |
|---|---|---|
| Compression gain | Does it let me predict much with little? | Filters arbitrary groupings from useful handles. |
| Robustness | Does the identity survive noise? | Protects the "thing" from micro-variance. |
| Autonomy | Are there effective laws at this level? | Makes the thing reusable without microscopic simulation. |
| Reproducibility | Do different observers converge on it? | Upgrades private whim into public objecthood. |

This resonates strongly with Dennett's idea of "real patterns": patterns are real to the extent that tracking them yields predictive power unavailable at less abstract levels.
:::

::: widget Resolution slider — when does a pattern earn thinghood?
Drag the slider to change "observer resolution". Watch how objecthood emerges from noise:

<div class="resolution-widget" style="margin: 0.75rem 0;">
<input type="range" min="1" max="5" value="1" style="cursor: pointer;" oninput="var v=this.value; var labels=['Micro-detail: local state changes, no object','Some structure visible, but unstable','Pattern coheres, borderline identity','Robust pattern: persists, moves, reusable','Compressed handle: a &quot;thing&quot; with its own laws']; this.closest('.resolution-widget').querySelector('.res-label').innerHTML=labels[v-1]; var dots=this.closest('.resolution-widget').querySelectorAll('.res-dot'); dots.forEach(function(d,i){d.style.opacity=i<v?'1':'0.15'});">
<div style="display: flex; justify-content: space-between; font-size: 0.625rem; color: var(--color-text-muted); margin-top: 0.25rem;">
<span>Micro</span><span>Macro</span>
</div>
<div style="display: flex; gap: 4px; margin: 0.75rem 0 0.5rem; justify-content: center;">
<span class="res-dot" style="display:inline-block;width:10px;height:10px;border-radius:50%;background:var(--color-accent);opacity:1;transition:opacity 0.2s"></span>
<span class="res-dot" style="display:inline-block;width:10px;height:10px;border-radius:50%;background:var(--color-accent);opacity:0.15;transition:opacity 0.2s"></span>
<span class="res-dot" style="display:inline-block;width:10px;height:10px;border-radius:50%;background:var(--color-accent);opacity:0.15;transition:opacity 0.2s"></span>
<span class="res-dot" style="display:inline-block;width:10px;height:10px;border-radius:50%;background:var(--color-accent);opacity:0.15;transition:opacity 0.2s"></span>
<span class="res-dot" style="display:inline-block;width:10px;height:10px;border-radius:50%;background:var(--color-accent);opacity:0.15;transition:opacity 0.2s"></span>
</div>
<div class="res-label" style="font-size: 0.8125rem; text-align: center; padding: 0.5rem 0.625rem; background: var(--color-accent-soft); border-radius: 6px; min-height: 2.5rem; display: flex; align-items: center; justify-content: center; color: var(--color-text);">Micro-detail: local state changes, no object</div>
</div>

The pattern doesn't change — only your description of it does. Objecthood lives in the compression.
:::

::: aside Alternate phrasings
- "Objects are the UI elements of experience."
- "A chair is a successful summary."
- "We live in the rendered layer because it is the only layer we can handle."
:::

## Physics Confirms the Strategy

Compression and scale-dependent description are not merely psychological. Physics itself is built out of effective descriptions.

In effective field theory, one uses the degrees of freedom appropriate to a scale and integrates out high-energy detail. This is not an admission of defeat; it is a methodological principle. Renormalisation group methods make the scale-dependence explicit: parameters "flow" when you change resolution.

::: deepdive The proton is a pattern across scales
At everyday energies, "proton" behaves like a stable particle. At higher resolution, deep inelastic scattering reveals scale-dependent structure functions and partonic substructure; the proton is described via distributions of quarks and gluons whose behaviour depends on the probing scale.

```python
# Conceptual: the same "thing" at different resolutions
descriptions = {
    "everyday":  "hard sphere, charge +1, stable",
    "nuclear":   "bound state of 3 quarks via gluons",
    "high_energy": "sea of partons, scale-dependent PDFs",
    "lattice":   "gauge field configuration on a grid",
}

for scale, desc in descriptions.items():
    print(f"  {scale:>12}: {desc}")
```

Physics does not merely tolerate multiple ontologies. It **requires** them.
:::

## The Trapdoor

If objects are compression products, then objecthood is — at least partly — a property of the image (reality-as-rendered), not a primitive property of the pre-image.

Nothing here denies an external reality. It denies that our everyday noun-inventory is guaranteed to be the universe's native inventory.

1. Finite systems compress.
2. Compression yields stable handles.
3. Those handles are what we call objects.

Therefore, objecthood is interface-dependent.

::: sidenote "Not fundamental" does not mean "not real"
Dennett's point about patterns helps here: a pattern can be real insofar as it supports reliable prediction and explanation — even if it is not fundamental furniture.

The public world becomes: the subset of renderings that remain stable across many observers with similar renderers, plus the disciplined instrumental practices that increase stability (measurement protocols, calibration, replication).
:::

## Time's Arrow as Coarse-Graining

In statistical mechanics, a macrostate is specified by a comparatively small set of macro-variables (pressure, temperature, density). Entropy counts microstates consistent with those macro-labels.

::: widget Entropy sandbox — the arrow appears when you summarise
Click "Drop the wall" to release particles from one side. The micro-dynamics are reversible, but the **macro-description** (left vs right count) creates an arrow:

<div class="entropy-widget" style="margin: 0.75rem 0;">
<canvas id="entropy-canvas" width="260" height="140" style="width: 100%;"></canvas>
<div style="display: flex; justify-content: space-between; align-items: center; margin-top: 0.5rem; gap: 0.5rem;">
<button id="entropy-btn" onclick="startEntropy()" style="flex-shrink: 0;">Drop the wall</button>
<div style="font-size: 0.6875rem; color: var(--color-text-muted); text-align: right;">
<span>Left: <strong id="ent-left">20</strong></span> &middot;
<span>Right: <strong id="ent-right">0</strong></span> &middot;
<span>S = <strong id="ent-s">0.00</strong></span>
</div>
</div>
</div>
<script>
(function(){
var canvas=document.getElementById('entropy-canvas');
if(!canvas)return;
var ctx=canvas.getContext('2d');
var W=260,H=140,N=20,wallUp=true,particles=[];
for(var i=0;i<N;i++){particles.push({x:Math.random()*(W/2-10)+5,y:Math.random()*(H-10)+5,vx:(Math.random()-0.5)*2,vy:(Math.random()-0.5)*2});}
function draw(){
ctx.clearRect(0,0,W,H);
var cs=getComputedStyle(document.documentElement);
var wallColor=cs.getPropertyValue('--color-text-muted').trim()||'#888';
var borderColor=cs.getPropertyValue('--color-border').trim()||'#ccc';
var accentColor=cs.getPropertyValue('--color-accent').trim()||'#3b5bdb';
if(wallUp){ctx.fillStyle=wallColor;ctx.fillRect(W/2-1,0,2,H);}
else{ctx.strokeStyle=borderColor;ctx.setLineDash([3,3]);ctx.beginPath();ctx.moveTo(W/2,0);ctx.lineTo(W/2,H);ctx.stroke();ctx.setLineDash([]);}
ctx.fillStyle=accentColor;
for(var i=0;i<N;i++){var p=particles[i];ctx.beginPath();ctx.arc(p.x,p.y,3,0,Math.PI*2);ctx.fill();}
}
function step(){
var left=0;
for(var i=0;i<N;i++){
var p=particles[i];
p.x+=p.vx;p.y+=p.vy;
if(p.x<3){p.x=3;p.vx*=-1;}
if(p.x>W-3){p.x=W-3;p.vx*=-1;}
if(p.y<3){p.y=3;p.vy*=-1;}
if(p.y>H-3){p.y=H-3;p.vy*=-1;}
if(wallUp){if(p.x>W/2-3&&p.vx>0){p.x=W/2-3;p.vx*=-1;}}
if(p.x<W/2)left++;
}
var right=N-left;
document.getElementById('ent-left').textContent=left;
document.getElementById('ent-right').textContent=right;
var pL=left/N||0.001,pR=right/N||0.001;
var s=-pL*Math.log2(pL)-pR*Math.log2(pR);
document.getElementById('ent-s').textContent=s.toFixed(2);
draw();
requestAnimationFrame(step);
}
draw();step();
window.startEntropy=function(){wallUp=false;document.getElementById('entropy-btn').textContent='Wall dropped';document.getElementById('entropy-btn').disabled=true;};
})();
</script>

The micro-level is reversible. The **arrow** only exists in the macro-label (left count, right count). Time's direction lives in the compression.
:::

::: deepdive Entropy and the arrow of time
Boltzmann entropy is the logarithm of the phase-space volume corresponding to a macrostate. Time-asymmetric macroscopic equations (diffusion, hydrodynamics) can be derived from reversible micro-dynamics by exploiting scale separation.

I am **not** saying "time is fake". I am saying:

- the *directionality* of time is naturally articulated in a coarse-grained vocabulary;
- entropy is defined relative to coarse-graining choices;
- therefore, the arrow is at least partly a feature of how we describe, track, and compress change.

This is why the arrow-of-time discussion is inseparable from the choice of macrostates.
:::

## The Hard Limit

I can model chairs as patterns, protons as effective entities, and even the arrow of time as a macro-level phenomenon. But when I try to model **seeming** as "just another object", the move becomes self-referential: the model is itself an appearance.

The interface cannot fit inside itself.

::: deepdive The DNA objection
"Fine — chairs might be compression handles. But DNA replication is a mechanistic cascade with information-rich structure. How can you tell me this is 'just description' while the micro-laws are the only reality?"

My reply separates two senses of "real":

- DNA and its machinery are real as **robust, reproducible patterns**.
- That does not automatically imply they are real as **additional fundamental causal ingredients** beyond the micro-physics.

Biological organisation can exert what looks like "top-down influence" by imposing **constraints** that channel micro-interactions — without violating micro-causal closure.
:::

::: aside Deterministic doesn't mean compressible
Even if micro-laws are simple, the dynamics they generate can be so computationally rich that prediction is effectively unshortenable. Wolfram calls this "computational irreducibility."

This does not prove free will. It does soften a naïve "clockwork universe" intuition that equates determinism with foreknowledge.
:::

## Two Hypotheses

The structure pressures us into two broad positions:

**Hypothesis A — Strong emergence from a non-mental base:**
Consciousness arises as a genuinely novel feature — not merely a useful description. This is philosophically costly because it threatens causal closure.

**Hypothesis B — Mind-like aspects closer to the base:**
The hard problem dissolves structurally. We stop trying to produce experience from what is wholly non-experiential. Most higher-level "things" remain weakly emergent handles, while consciousness is not an ontological bolt-on.

::: sidenote The emotional reframe
Nothing in this structure tells you the world is cold or pointless. If anything, it says the opposite: **appearing is the most fundamental thing we know**, and everything else is what we build from it.

The rendered layer — the world of chairs, sunsets, faces, and physics — is not less real for being rendered. It is the only reality we can inhabit. And within it, meaning is not found; it is made.
:::

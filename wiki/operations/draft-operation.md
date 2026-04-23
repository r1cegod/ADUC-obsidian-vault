---
type: operation
title: Draft Operation
created: '2026-04-21T00:00:00.000Z'
updated: '2026-04-21'
tags:
  - workflow
  - docs
  - meta
  - draft
status: active
lang: en
feeds_into:
  - wiki/operations-hub.md
  - SCHEMA.md
  - wiki/operations/canvas-architecture-operation.md
---
> **TL;DR**: `DRAFT` is an official vault operation for collaborative shaping before commitment. Use it when the work needs brainstorming, rough contracts, early docs, and reaction loops without pretending the structure is final. The rule is simple: `(draft)` marks exploration space; non-draft artifacts hold promoted structure that survived pressure.

## What It Is

`DRAFT` is not a Raven-only pattern.
It is a vault-level operation.

```text
DRAFT
  = exploration before commitment
  = reaction-oriented shaping
  = temporary structure allowed
  = unstable ideas allowed
  = early docs allowed
```

The point is to let the system think in public without lying about what is already real.

## Core Split

```text
(draft)
  = brainstorm zone
  = rough ideas
  = temporary contracts
  = unresolved questions
  = early docs and partial structure

non-draft
  = promoted structure
  = real architecture or workflow
  = stable enough to defend and route decisions
```

If exploration and commitment are mixed in one undifferentiated surface, the vault starts lying.

## When To Use

Use `DRAFT` when the task is collaborative shaping rather than direct implementation or passive discussion.

Typical cases:

- architecture exploration
- workflow design
- feature/system decomposition
- naming and boundary pressure
- temporary planning surfaces
- first-pass docs that exist to provoke reaction

Do not use `DRAFT` when the artifact is already stable enough to be treated as canonical.

## Operating Loop

```text
1. define the draft target
2. choose the live artifact path
3. if the user has no proposal and no clear existing thing to work on,
   the agent proposes the first concrete draft seed
4. produce the first usable draft
5. optimize for reaction, not completeness
6. revise through keep / move / split / remove / tighten feedback
7. preserve one live path instead of duplicate branches
8. mirror stable decisions into the right vault layer
9. promote surviving structure out of draft when earned
```

## Proposal Duty

If the surface is blank, the agent should not wait passively.

```text
no user proposal + no obvious existing working surface
  -> agent proposes the next concrete draft seed
  -> user reacts
  -> back-and-forth pressure continues
```

The proposal is a starting pressure point, not a hidden attempt to settle the architecture early.

## Label Rule

```text
label contains (draft)
  -> exploration is allowed
  -> instability is expected
  -> not a claim of architectural truth yet

label has no (draft)
  -> treated as real structure
  -> should be defendable
  -> may route build decisions
```

This applies to canvas groups, notes, docs, and other planning artifacts where ambiguity would otherwise accumulate.

## Promotion Law

```text
draft artifact survives pressure
  -> shape becomes coherent
  -> dependencies are visible
  -> contract is stable enough
  -> mirror into markdown if needed
  -> promote into non-draft structure
```

Until then, it stays draft.

## Artifact Rule

During `DRAFT`, keep one live artifact path whenever possible.

Bad pattern:

```text
draft-v1
draft-v2
new-draft-final
actual-final-maybe
```

Better pattern:

```text
one live draft surface
  -> revised in place
  -> stable points mirrored outward
```

The draft should breathe. The vault should still remember what stabilized.

## Reflection Rule

One chat session should reflect into two sources, not one.

```text
vault notes
  -> AI context
  -> durable memory of the draft

canvas
  -> human context
  -> live visual planning surface
```

So `DRAFT` is not only a note update or only a canvas update.
It is usually both:

```text
one session
  -> vault update
  -> canvas update
```

## Canvas Use

When `DRAFT` runs through Canvas:

```text
canvas
  -> exploration surface
  -> clusters
  -> tensions
  -> open questions
  -> promotion candidates
```

The canvas does not become the only source of truth.
Stable points still get mirrored into markdown notes or operation leaves.

## Notes Use

When `DRAFT` runs through markdown:

```text
notes
  -> durable mirror of stable points
  -> temporary contracts
  -> draft laws
  -> decision pressure
```

Early docs are allowed inside `DRAFT`. The key is that they stay explicitly marked as draft until promoted.

## Routing In

- [[wiki/operations-hub]]
- [[wiki/operations/canvas-architecture-operation]]
- [[wiki/synthesis/obsidian-d2-canvas-architecture-method]]
- [[SCHEMA.md]]

## Routing Out

- system-shape draft -> [[wiki/operations/canvas-architecture-operation]]
- stable structure -> project/router note or canonical wiki note
- maintenance closeout -> [[wiki/operations/self-healing-operation]]

## After Use Evolution Check

- Was the draft surface correct for the task?
- Did the loop leave one clear live artifact behind?
- Were draft vs real labels unmistakable?
- Did stable points get mirrored before closing?
- If friction appeared, patch this leaf or log the gap today.

## Related

- [[wiki/operations-hub]]
- [[wiki/operations/canvas-architecture-operation]]
- [[wiki/operations/self-healing-operation]]
- [[wiki/synthesis/obsidian-d2-canvas-architecture-method]]
- [[SCHEMA.md]]

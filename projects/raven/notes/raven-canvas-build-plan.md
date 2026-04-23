---
type: note
title: Raven Canvas Build Plan
created: '2026-04-21'
updated: '2026-04-21'
tags:
  - project/raven
  - architecture
  - workflow
  - docs
status: active
lang: en
feeds_into:
  - projects/raven/notes/raven-architecture-hub.md
  - projects/raven/README.md
---
> **TL;DR**: Build Raven Canvas as a collaborative systems draft for human thinking, and force system-level architecture decisions through the canvas first while mirroring every stable point back into markdown notes.

## Purpose
Raven Canvas is not a diagram export. It is the active collaboration board where human judgment and agent structure meet.

```text
Canvas
  -> fast visual thinking
  -> clustering
  -> tension spotting
  -> open questions
  -> sequencing

Vault notes
  -> durable decisions
  -> contracts
  -> rules
  -> references
```

The board should help Duc evaluate shape quickly without needing to explain the layout in words first.

## Core Rule
Every stable point on the canvas must have a markdown mirror in the vault.

```text
canvas point becomes stable
  -> mirror into note
  -> link from router or domain note
```

The canvas is where the system breathes.
The notes are where the system remembers.

Architecture-first rule in this scope:

```text
if the decision changes system shape
  -> put it on Canvas first
  -> then mirror it into notes

if the decision only changes how one function works
  -> do not force Canvas
  -> keep it in code-level planning
```

## What The Canvas Should Be
Use the canvas for:
- system regions
- loop boundaries
- open questions
- tensions and tradeoffs
- sequencing of build order
- missing contracts
- things Duc can react to visually in one pass

Do not use the canvas as:
- a pile of pinned notes
- a markdown index in disguise
- the only place where architecture truth lives

## Recommended Canvas Shape
Do not build this as a tree that starts from a single `Raven` root node. Everything on the board already belongs to Raven.

Use two different organizing rules at once:

```text
Groups
  -> feature groups
  -> example: yt search, harness skeleton, judgment engine

Card colors
  -> domain types
  -> Deep marine: SQL / state
  -> Orange: AI / judgment
  -> Light blue: search / discovery
  -> Purple: others / glue / policy

Completion state
  -> finished / live = original domain color
  -> actual unfinished function or feature = much lighter version of the same domain color
```

Treat the first Raven canvas as a connected field with six feature groups.

```text
1. Query + discovery
2. Harness skeleton
3. Judgment engine
4. Channel trust
5. Memory + review
6. Evolve loop
```

### 1. Core Loop
One visually dominant path in the center:

```text
target
  -> query enricher
  -> discovery
  -> video gate
  -> judgment
  -> channel rank
  -> report
```

This is the spine. Everything else orbits this.

### 2. Runtime Layers
Add horizontal or vertical bands for:
- discovery
- filtering
- judgment
- trust
- output

This prevents function soup.

### 3. State Stores
Separate state from process.

```text
SQLite = workbench state
Vault = canonical memory
```

The canvas should make this split obvious at a glance.

### 4. Judgement System
Give this its own cluster, not a tiny box.

Include cards for:
- metadata heuristics
- content judgment
- bullshit signals
- quality signals
- audit inputs

This area is where Raven becomes Raven.

### 5. Channel Trust System
Separate channel trust from video filtering.

Cards should express:
- channel memory
- trust tier S/A/B/C/D
- evidence accumulation
- filter policy

This prevents one random result from impersonating source quality.

### 6. Evolve Loop
Put this off to one side, visibly downstream.

```text
audits
  -> disagreement patterns
  -> proposed rule update
  -> human approval
  -> system update
```

Do not place it inline with the core loop. It is a governance loop, not the runtime path.

### 7. Open Questions And Risks
Reserve a distinct corner for:
- unclear thresholds
- unknown contracts
- future expansions
- architecture risks

This keeps unresolved design pressure visible.

## Card Types
Use only a few card types so the board stays legible.

```text
Group
  = feature group

Text card
  = system point, law, question, or contract slice

Arrow
  = dependency, flow, pressure, or policy influence
```

For the first Raven canvas, default to text cards and groups.
The color of a text card should tell you its domain before you read it.
The brightness of a text card should tell you whether it is live or still unfinished.
Only add file cards when there is a specific note that must be opened from the board.
Do not let file cards dominate the board.

## Collaboration Protocol
Use this loop when working together on the canvas:

```text
1. agent drafts or reshapes one region
2. Duc evaluates by feel and pattern recognition
3. Duc reacts: keep / move / split / remove
4. stable points get mirrored into notes
5. repeat on the next region
```

This is important: Duc does not need to explain the whole board upfront. Visual reaction is enough.

### Position Ownership Rule

Canvas position taste belongs to Duc.

```text
agent
  -> may create new cards in open positions
  -> may change labels and values
  -> may patch text/content inside existing structure

agent must not
  -> move what Duc moved
  -> place new groups on top of other groups
  -> rearrange board layout by taste
  -> assume spatial ownership without explicit request
```

If a new group or cluster is needed, default to creating/changing the value layer and let Duc own the final placement call.

### Session Reflection Rule

The live canvas should reflect what is being planned in the current session.

```text
chat
  -> primary discussion surface

canvas
  -> live session planning mirror
  -> updated as the session shape changes
  -> reflects what is actively being drafted/planned now
```

Do not let the canvas drift into a stale warehouse of old planning fragments when the session has clearly moved on.

### Plan Group Rule

`Plan mega group` holds session-wide general information only.

```text
Plan mega group
  -> general session context
  -> shared pressure/questions/laws

feature-specific draft
  -> lives in that feature's (Draft) group

never link anything to Plan mega group
```

Do not use `Plan mega group` for group-specific draft details.
Use links and arrows between actual cards or groups that carry meaning. Do not use `Plan mega group` as a fake dependency node.

## Mirroring Protocol
Each stable canvas point should map to one of these:
- existing project note
- new project note
- architecture hub update
- build-plan update
- evaluation-domain update

Use this minimum mirror template inside notes:

```text
Canvas point:
Why it exists:
What it connects to:
What changes if it moves:
```

## Build Order
Do not build the whole canvas at once.
Build it in passes.

### Pass 1 - Skeleton
Create only:
- core loop
- state split
- evolve loop off to the side
- open questions area

### Pass 2 - Judgement Cluster
Expand:
- video gate
- judgment system
- bullshit signals
- audit inputs

### Pass 3 - Trust Cluster
Expand:
- channel memory
- S/A/B/C/D model
- trust update logic
- hard filter rules

### Pass 4 - Mirroring Pass
For each stable cluster:
- mirror into markdown
- route from architecture hub
- update build plan if sequencing changed

## Evaluation Criteria
A good Raven canvas should pass these tests:
- Duc can scan it in under 30 seconds and feel the system shape
- the core loop is obvious immediately
- governance is visually separate from runtime
- state boundaries are obvious
- open questions are visible, not hidden
- stable decisions are mirrored into notes

## First Session Goal
The next Raven canvas session should aim only to complete:
- one live skeleton canvas that matches current code reality
- a Raven mega group with only the cards that truly exist now
- one connected search mega group that shows the current backend search shape
- one detached mega group for open questions and intended / not discussed features

That is enough to make the board useful.

## Next Active Canvas Thread
The next architecture thread to expand from the live skeleton is:

```text
how the vault keeper Raven uses the vault
  -> ingestion structure
  -> promotion ladder
  -> what stays in SQLite
  -> what gets promoted into vault memory
  -> what retrieval packet gets assembled later
```

Primary note for that thread:
- [[projects/raven/notes/raven-vault-keeper-harness-architecture]]

## Related
- [[projects/raven/notes/raven-architecture-hub]]
- [[projects/raven/README]]
- [[projects/raven/notes/raven-phase-1-build-plan]]
- [[projects/raven/notes/raven-bs-detector-ingestion-architecture]]
- [[wiki/synthesis/obsidian-d2-canvas-architecture-method]]

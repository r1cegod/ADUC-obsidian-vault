---
type: protocol
title: Obsidian D2 Canvas Architecture Method
created: '2026-04-21'
updated: '2026-04-21'
tags:
  - obsidian
  - architecture
  - workflow
  - docs
status: active
lang: en
feeds_into:
  - briefing.md
  - projects/raven/notes/raven-architecture-hub.md
---
> **TL;DR**: Use Obsidian Canvas as the default architecture thinking surface for system-level decisions, mirror stable points into markdown notes, and treat D2 as optional only when a formal rendered diagram is genuinely needed.

## Optimization Audit
The current vault workflow had three friction points:

```text
1. Canvas existed as a method note, but not as an official maintenance path.
2. D2 language still dominated parts of the workflow even after Canvas became primary.
3. Architecture tasks could end with a changed board but weak markdown/routing follow-through.
```

This method now treats Canvas as a vault-native architecture lane, not a project-local experiment.

## Purpose
This method exists for systems that become too large to hold in working memory but still need to evolve inside the vault.

```text
Canvas
  -> exploration
  -> clustering
  -> open questions
  -> collaborative draft

Markdown notes
  -> decisions
  -> contracts
  -> rules
  -> explanations

Optional D2
  -> formal rendered map
  -> only when the project actually benefits from it
```

The goal is not to make prettier diagrams. The goal is to stop developing from fog.

## Current Preference
For Raven and similar fast-moving system design work, prefer:

```text
Canvas first
  -> markdown mirroring second
  -> D2 only if needed later
```

## Scope Boundary
Canvas-first applies to architecture decisions in scope:

```text
system boundaries
loop shape
storage split
promotion rules
ownership and routing
ingestion structure
```

Do not force Canvas into code-local reasoning such as:

```text
how one function works internally
small helper logic
local refactor mechanics
signature-level implementation details
```

That work should stay in code, tests, or narrow markdown notes.

## Core Split
Use each layer for a different cognitive job.

### Obsidian Canvas
Use Canvas for:
- rough system maps
- loop separation
- question clustering
- TODO placement
- relationship discovery
- short-lived layout experiments

Canvas is allowed to be messy.

Canvas rule:
- use text, groups, arrows, and freeform clustering for human thinking
- do not make pinned note/file cards the main planning substrate
- when a card represents unfinished work, use a lighter version of its domain color instead of inventing a new palette state

### D2
Use D2 for:
- the stable system map
- flow boundaries
- data movement
- storage boundaries
- major loop definitions
- architecture laws that should survive sessions

D2 is not for brainstorming first. D2 is for freezing what survived brainstorming.

### Markdown Notes
Use notes for:
- why a boundary exists
- what each loop owns
- rules and non-rules
- decision history
- routing to the right artifact

A diagram without notes becomes myth. Notes without a diagram become fog.

## Official Workflow

```text
1. Think in Canvas
2. Mirror stable structure into markdown
3. Promote into D2 only if a formal rendered map is genuinely needed
4. Render dark export from D2
5. Self-audit the rendered output
6. Fix D2 if the render is wrong
7. Link the audited diagram from a hub note
8. Route implementation work through the hub
9. When architecture changes, update Canvas first, then other artifacts
```

## Vault-First Closeout
For architecture-heavy tasks, finish in this order:

```text
1. update the canvas
2. mirror stable points into markdown
3. patch routers or context if routing changed
4. append the day-log entry
5. only then end the response
```

This keeps the vault authoritative before the session closes.

## File Roles
Recommended artifact set for any architecture domain:

```text
<domain>-hub.md
<domain>-system-map.canvas
<domain>-system-map.d2
<domain>-system-map.svg
```

Roles:
- `hub.md` is the router and the written contract
- `.canvas` is the exploratory whiteboard
- `.d2` is the stable architecture source
- `.svg` is the rendered snapshot for embedding and quick review

## Operating Commands

```text
Open in Obsidian:
- open the .canvas file for visual exploration
- open the hub note for routing and embedded review

Render D2 overview maps to SVG:
- ~/.local/bin/d2 --layout elk --theme 201 --pad 40 path/to/system-map.d2 path/to/system-map.svg

Audit the structure in text too:
- ~/.local/bin/d2 --layout elk path/to/system-map.d2 path/to/system-map.txt

Make the output actually dark:
- set root `style.fill` in the D2 source so the SVG background does not stay white
```

Raven live instance:

```text
~/.local/bin/d2 \
  /mnt/d/ANHDUC/ADUC_vault/ADUC/projects/raven/notes/raven-system-map.d2 \
  /mnt/d/ANHDUC/ADUC_vault/ADUC/projects/raven/notes/raven-system-map.svg
```

The workflow does not depend on an Obsidian D2 plugin. The exported SVG is the durable review artifact.

## Promotion Rule
Only promote from Canvas to D2 when one of these is true:
- the loop boundary is stable
- the storage boundary is stable
- the decision will affect implementation sequencing
- the next session would be misled without the change

If it is still just a question, keep it in Canvas.
If it is stable but does not need a formal diagram, mirror it into markdown and stop there.

## Growth Rule
This domain should grow with the vault by accretion, not replacement.

```text
new project or subsystem
  -> gets its own hub
  -> gets its own canvas
  -> gets its own D2 map
  -> links back to this method
```

Do not try to force one giant vault-wide diagram. Use local system maps plus hub routing.

## Maintenance Rule
Whenever a major architecture change lands:
- update the canvas or hub first
- adjust the hub note if the routing changed
- update D2 only if the project still benefits from it
- keep the markdown mirrors aligned in the same task

Whenever a change is only exploratory:
- update Canvas first
- do not touch D2 until the structure survives scrutiny

## Failure Modes
- Canvas becomes the only source of truth
- D2 never gets updated after implementation changes
- notes explain a system shape that the diagram no longer shows
- one giant diagram tries to hold every project in the vault
- overview maps try to carry every detail edge and become unreadable
- implementation starts from scattered code instead of the hub

## First Live Instance
Raven is the first active implementation of this method.

Router:
- [[projects/raven/notes/raven-architecture-hub]]

## Related
- [[projects/raven/notes/raven-architecture-hub]]
- [[projects/raven/README]]
- [[wiki/synthesis/obsidian-agent-vault-architecture]]
- [[SCHEMA.md]]

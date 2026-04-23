---
type: note
title: Raven Adoption Of Draft Operation
created: '2026-04-21'
updated: '2026-04-21'
tags:
  - project/raven
  - architecture
  - workflow
  - draft
status: active
lang: en
feeds_into:
  - projects/raven/notes/raven-architecture-hub.md
  - projects/raven/notes/raven-canvas-build-plan.md
---
> **TL;DR**: Raven does not own `DRAFT`. Raven adopts the vault-level [[wiki/operations/draft-operation]] for architecture work. In this project, the operation currently applies to the ranking domain through the split between `Ranking Mega Group` and `Ranking Mega Group (Draft)` on the live board.

## Canonical Rule

Source of truth:
- [[wiki/operations/draft-operation]]

Raven should not redefine the operation locally.
It should only record how Raven is using it.

## Current Raven Adoption

Current board convention:

```text
Ranking Mega Group
  -> real ranking architecture only

Ranking Mega Group (Draft)
  -> brainstorm zone for source-ranker ideas
  -> rough contracts
  -> metadata-only boundaries
  -> unstable structure
```

## Local Promotion Rule

```text
ranking draft survives pressure
  -> markdown mirror if needed
  -> move into Ranking Mega Group
```

## Related

- [[wiki/operations/draft-operation]]
- [[projects/raven/notes/raven-architecture-hub]]
- [[projects/raven/notes/raven-canvas-build-plan]]
- [[projects/raven/notes/raven-source-ranker-draft]]
- [[projects/raven/README]]

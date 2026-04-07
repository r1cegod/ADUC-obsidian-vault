---
type: source-summary
title: "Delegated Feature How-To Protocol"
created: 2026-04-06
updated: 2026-04-06
tags:
  - project/pathfinder
  - pathfinder
  - workflow
  - docs
status: active
lang: en
source: "[[projects/pathfinder/sources/docs/workflows/delegated_feature_how_to.md]]"
---

> **TL;DR**: This workflow doc defines how to write delegated feature notes so implementation context can be handed off cleanly across contributors or later sessions.

## Summary
The delegated feature protocol is a lightweight workflow guide for documenting feature work that is being handed off or split. It explains when such a doc should be written, what format it should follow, and what rules keep it useful rather than noisy.

Its role is narrower than the architecture and evaluation docs, but it still matters operationally. It gives PathFinder a consistent way to package feature context so future work does not start from scattered chat history or partial memory.

Inside the vault, this note belongs in the workflow cluster and complements the broader context-maintenance discipline.

## Key Points
- Delegated feature docs are meant for clean handoff, not generic note taking.
- The protocol standardizes when to write them and what structure they should follow.
- It reduces restart cost for split or paused implementation work.

## Details
### Operational Use
Use this source when a feature is large enough or fragmented enough that a dedicated handoff note is justified.

### Relationship To Other Docs
It sits below the repo-wide context system and above ad hoc scratch notes, giving feature work a repeatable handoff shape.

## Related
- [[projects/pathfinder/notes/docs-context-maintenance]]
- [[projects/pathfinder/notes/docs-dev-log-system-prompt]]
- [[projects/pathfinder/README]]

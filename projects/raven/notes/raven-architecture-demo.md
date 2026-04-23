---
type: note
title: Raven Architecture Demo
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
---
> **TL;DR**: Fast demo entrypoint for the Raven visual-planning stack: open this note for the rendered map, then jump to Canvas for exploration and D2 for the stable source.

## Demo Route
1. Read the rendered system map below.
2. Open [[projects/raven/notes/raven-system-map.canvas]] for the exploratory board.
3. Open `projects/raven/notes/raven-system-map.d2` when you want to edit the stable map.

## Rendered Map
![[projects/raven/notes/raven-system-map.svg|697]]

## What To Look At
- `Planning Surface`: Canvas -> D2 -> dark SVG -> ASCII audit is the new architecture workflow.
- `Canvas law`: the board is for human clustering and open questions, not pinned vault notes.
- `Runtime + State`: the main path is discovery -> assessment -> report, with stores shown as workbench versus canonical brain.
- `Audit + Policy`: governance is separated from the runtime path so the overview does not drown in feedback edges.
- `Architecture Laws`: the system stops lying to you about what each layer does.

## Open Next
- [[projects/raven/notes/raven-architecture-hub]]
- [[projects/raven/notes/raven-system-map.canvas]]
- [[projects/raven/notes/raven-phase-1-build-plan]]
- [[projects/raven/notes/raven-bs-detector-ingestion-architecture]]

## Related
- [[projects/raven/notes/raven-architecture-hub]]
- [[wiki/synthesis/obsidian-d2-canvas-architecture-method]]

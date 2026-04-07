---
type: source-summary
title: "Current Context"
created: 2026-04-06
updated: 2026-04-06
tags:
  - project/pathfinder
  - pathfinder
  - context
  - live
status: active
lang: en
source: "[[projects/pathfinder/sources/docs/context/docs/CURRENT_CONTEXT.md]]"
---

> **TL;DR**: This is the live handoff file for the current build cycle, covering active goal, files in play, open questions, rerun commands, and next actions.

## Summary
`CURRENT_CONTEXT.md` is the short-lived working scratchpad for active PathFinder work. Unlike stable architecture docs, it records what is happening now: the current goal, the files being changed, the open questions, risks, and the commands needed to resume work quickly.

At the moment of ingest, it records a tightening of the official evaluation pipeline around a three-round production gate. That makes it a good example of what belongs in transient context: a precise live workstream, not evergreen project facts.

Any agent starting active implementation work should read this after `PROJECT_CONTEXT.md` to avoid operating on stale assumptions.

## Key Points
- The file is explicitly volatile and should change with the active work cycle.
- It is the canonical handoff note for live blockers, reruns, and next actions.
- It currently centers on evaluation workflow policy rather than architecture changes.

## Details
### When To Use It
Read this before resuming in-flight work, especially when the repo may have changed since the last session.

### What It Should Not Hold
Stable architecture facts and durable decisions should be moved elsewhere; this file is not long-term memory.

## Related
- [[projects/pathfinder/notes/docs-project-context]]
- [[projects/pathfinder/notes/docs-context-maintenance]]
- [[projects/pathfinder/README]]

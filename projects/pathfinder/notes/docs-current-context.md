---
type: source-summary
title: "Current Context"
created: 2026-04-06
updated: 2026-04-13
tags:
  - project/pathfinder
  - pathfinder
  - context
  - live
status: active
lang: en
source: "[[projects/pathfinder/sources/docs/context/docs/CURRENT_CONTEXT.md]]"
---

> **TL;DR**: Live handoff file for the current build cycle: the 2026-04-13 university-finding frontend run fixed Major handoff into University, and the focused University replay now passes the first UEH -> FPT -> RMIT comparison seam while leaving broader RMIT/UEL or frontend continuation proof as the next target.

## Summary
`CURRENT_CONTEXT.md` is the short-lived working scratchpad for active PathFinder work. Unlike stable architecture docs, it records what is happening now: the current goal, the files being changed, the open questions, risks, and the commands needed to resume work quickly.

It currently records the shift from Major handoff repair to University comparison/ranking hardening. Major can now complete and hand off to University when MIS is selected and school-specific proof is the remaining uncertainty. The first focused University replay now captures the frontend R7 failure as executable evidence: UEH stays conditional, weak FPT evidence does not outrank UEH, and the compiler asks to compare RMIT next instead of asking another page-type or threshold question. It also records the new documentation boundary: evaluation reports live in the vault evaluation directory, while repo `eval/` keeps executable evidence.

Any agent starting active implementation work should read this after `PROJECT_CONTEXT.md` to avoid operating on stale assumptions.

## Key Points
- The file is explicitly volatile and should change with the active work cycle.
- It is the canonical handoff note for live blockers, reruns, and next actions.
- It currently centers on the 2026-04-13 university-finding frontend run, Major MIS handoff fix, the first University comparison replay, and vault-only evaluation-domain policy.
- It now reflects that the next best PathFinder eval pass is broader University comparison/ranking coverage for RMIT and UEL, or a full frontend continuation if browser-level proof is needed.

## Details
### When To Use It
Read this before resuming in-flight work, especially when the repo may have changed since the last session.

### What It Should Not Hold
Stable architecture facts and durable decisions should be moved elsewhere; this file is not long-term memory.

## Related
- [[projects/pathfinder/notes/docs-project-context]]
- [[projects/pathfinder/notes/docs-context-maintenance]]
- [[projects/pathfinder/README]]

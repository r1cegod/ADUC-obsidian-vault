---
type: source-summary
title: "Current Context"
created: 2026-04-06
updated: 2026-04-12
tags:
  - project/pathfinder
  - pathfinder
  - context
  - live
status: active
lang: en
source: "[[projects/pathfinder/sources/docs/context/docs/CURRENT_CONTEXT.md]]"
---

> **TL;DR**: Live handoff file for the current build cycle: full eval next, after the frontend trace output regression locked compiler wording to raw stage state, the lock was reconciled with same-turn stage intro, Purpose handoff sufficiency was patched, same-turn stage transition was patched, and sub-orchestrator worker token fanout was capped.

## Summary
`CURRENT_CONTEXT.md` is the short-lived working scratchpad for active PathFinder work. Unlike stable architecture docs, it records what is happening now: the current goal, the files being changed, the open questions, risks, and the commands needed to resume work quickly.

It currently records the shift from stage-local-only hardening to full-path frontend trace hardening: output compilation now obeys raw `done` flags before talking about stage handoff, the current-stage lock no longer conflicts with same-turn stage intro, Purpose now has a handoff-sufficiency policy like Goals, same-turn completion can advance before output, the frontend trace output regression has a reusable JSONL dataset, and sub-orchestrator workers read a capped recent tail while summaries preserve longer context. That makes it a good example of what belongs in transient context: a precise live workstream, not evergreen project facts.

Any agent starting active implementation work should read this after `PROJECT_CONTEXT.md` to avoid operating on stale assumptions.

## Key Points
- The file is explicitly volatile and should change with the active work cycle.
- It is the canonical handoff note for live blockers, reruns, and next actions.
- It currently centers on full-path evaluation workflow, output compiler stage-state locking, Purpose handoff sufficiency, same-turn stage transition, and sub-orchestrator worker token control.
- It now reflects that the 2026-04-12 frontend output regression passes the output graph replay rows, but fresh uncertainty chat/full-path proof is still next.

## Details
### When To Use It
Read this before resuming in-flight work, especially when the repo may have changed since the last session.

### What It Should Not Hold
Stable architecture facts and durable decisions should be moved elsewhere; this file is not long-term memory.

## Related
- [[projects/pathfinder/notes/docs-project-context]]
- [[projects/pathfinder/notes/docs-context-maintenance]]
- [[projects/pathfinder/README]]

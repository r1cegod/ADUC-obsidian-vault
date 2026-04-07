---
type: source-summary
title: "Delegated Feature How-To Protocol"
created: 2026-04-06
updated: 2026-04-07
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
The delegated feature protocol is not a generic workflow note. It is the writing contract for the human-consumption docs that live under `delegated/`. Those delegated docs exist so the developer can run, modify, and debug delegated code without reconstructing intent from chat history or reverse-engineering the file line by line.

Its role is narrower than the architecture and evaluation docs, but it still matters operationally. It gives PathFinder a consistent way to package feature context so future work does not start from scattered chat history or partial memory.

Inside the vault, this note belongs in the workflow cluster and complements the broader context-maintenance discipline. It should always be read together with at least one concrete delegated doc, because the point of the protocol is to shape those human-facing documents in practice.

## Key Points
- `delegated_feature_how_to.md` is the authoring spec for docs in `delegated/`.
- Delegated docs are meant for human handoff and code ownership recovery, not generic note taking.
- The protocol standardizes when to write them, what structure they should follow, and why ASCII flow diagrams are mandatory.

## Details
### Operational Use
Use this source when a feature is large enough or fragmented enough that a dedicated handoff note is justified.

### Raw Source
- Protocol source: [[projects/pathfinder/sources/docs/workflows/delegated_feature_how_to.md]]
- Example delegated doc: [[projects/pathfinder/sources/docs/delegated/eval_run_eval.md]]

### Relationship To Other Docs
It sits below the repo-wide context system and above ad hoc scratch notes, giving feature work a repeatable handoff shape.

It directly governs docs like `eval_run_eval.md`: the file in `delegated/` is the human-facing artifact, and this protocol is the rulebook that explains how such an artifact should be written.

## Related
- [[projects/pathfinder/notes/docs-context-maintenance]]
- [[projects/pathfinder/notes/docs-dev-log-system-prompt]]
- [[projects/pathfinder/notes/docs-eval-run-eval]]
- [[projects/pathfinder/README]]

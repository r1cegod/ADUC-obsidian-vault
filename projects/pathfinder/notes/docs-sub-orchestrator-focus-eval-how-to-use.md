---
type: source-summary
title: "Sub-Orchestrator Focus Eval"
created: 2026-04-10
updated: 2026-04-10
tags:
  - project/pathfinder
  - pathfinder
  - evaluation
  - workflow
status: active
lang: en
source: "[[projects/pathfinder/sources/docs/evaluation/sub_orchestrator_focus_eval_how_to_use.md]]"
---

> **TL;DR**: This doc defines the dedicated sub-orchestrator-only evaluation lane for PathFinder, with separate focus runs for `summarizer` and `worker` and a per-family 3-round production gate.

## Summary
This workflow sits between cheap deterministic seam checks and broader replay. It exists because the sub-orchestrator now has its own memory-compression and user-tag-refresh lane, and that lane can drift without any help from the main orchestrator.

Its strongest rule is scope: it must not route through `input_orchestrator`. The runner hits the sub-orchestrator focus graphs directly so prompt behavior, memory compression, and field refresh logic can be audited in isolation.

## Key Points
- This is a dedicated seam audit, not full replay.
- `summarizer` and `worker` are evaluated separately.
- Each family has its own 3-round production gate.
- Trace audit matters more than runtime success.

## Related
- [[projects/pathfinder/notes/docs-sub-orchestrator-evaluation]]
- [[projects/pathfinder/notes/docs-eval-how-to-use]]
- [[projects/pathfinder/notes/docs-python-function-check-how-to-use]]
- [[projects/pathfinder/notes/pathfinder-evaluation-hub]]

---
type: source-summary
title: "PathFinder Python Function Check"
created: 2026-04-09
updated: 2026-04-13
tags:
  - project/pathfinder
  - pathfinder
  - evaluation
  - workflow
status: active
lang: en
source: "[[projects/pathfinder/sources/docs/evaluation/python_function_check_how_to_use.md]]"
---

> **TL;DR**: This doc defines the cheap deterministic backend-check workflow beside replay eval, with all Python contract tests centralized under `backend/test/` and invoked through `backend.test.<module>`.

## Summary
The Python-function-check workflow is the low-cost gate for PathFinder's Python-owned seams. It exists to answer a narrower question than replay: did routing, reopen invalidation, done normalization, helper parity, and stage-to-output glue survive the latest refactor?

Its main value is seam isolation. Replay can prove behavior, but it can also hide whether the real failure came from Python policy, prompt logic, or output phrasing. This workflow locks the deterministic layer first so the next replay pass has a cleaner failure surface.

It also records the grouped command structure that now owns this work: shared stage-profile utils, orchestrator policy, stage-helper parity, output/evaluation seams, and the sub-orchestrator memory lane.

The 2026-04-13 maintenance pass made the test-location rule explicit: new Python contract/regression tests go in `backend/test/`, not at repo root or beside implementation modules.

## Key Points
- This is the cheap deterministic gate that should run before broader replay.
- The current five groups are the starting shape, not a permanent limit; broader seam coverage is still the official direction.
- It complements `eval/HOW_TO_USE.md`; it does not replace replay.
- The workflow is grouped by seam family, not by individual file.
- Test modules should be run as `backend.test.<module>` with `python -m unittest`.

## Details
### Use Pattern
Read this when the question is "what pure Python backend checks should run before replay?" rather than "how do I run attack datasets?"

### Relationship To Replay
Replay still owns production-behavior proof. This doc owns the lower-cost backend-proof layer.

## Related
- [[projects/pathfinder/notes/docs-eval-how-to-use]]
- [[projects/pathfinder/notes/docs-python-function-check-stage-helper-matrix]]
- [[projects/pathfinder/notes/docs-python-function-check-sub-orchestrator-and-memory-lane]]
- [[projects/pathfinder/notes/pathfinder-evaluation-hub]]

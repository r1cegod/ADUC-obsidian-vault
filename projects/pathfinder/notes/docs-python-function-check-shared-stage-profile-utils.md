---
type: source-summary
title: "Python Function Check - Shared Stage Profile Utils"
created: 2026-04-09
updated: 2026-04-09
tags:
  - project/pathfinder
  - pathfinder
  - evaluation
status: active
lang: en
source: "[[projects/pathfinder/sources/docs/evaluation/python_function_check_shared_stage_profile_utils.md]]"
---

> **TL;DR**: This report records the grouped deterministic checks for the shared reopen and done-normalization helper layer.

## Summary
This report covers the shared helper seam in `backend/stage_profile_utils.py`. That layer matters because every stage depends on it for reopen invalidation and shared `done` recomputation.

The current grouped pass is green and now locks the previously under-tested behaviors that can corrupt multiple stage graphs at once.

## Key Points
- One shared helper bug can affect all six stages.
- The current pass now covers targeted-field invalidation and nested Goals normalization.
- This group passed on 2026-04-09.

## Related
- [[projects/pathfinder/notes/docs-python-function-check-how-to-use]]
- [[projects/pathfinder/notes/docs-python-function-check-orchestrator-policy]]

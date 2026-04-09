---
type: source-summary
title: "Python Function Check - Orchestrator Policy"
created: 2026-04-09
updated: 2026-04-09
tags:
  - project/pathfinder
  - pathfinder
  - evaluation
status: active
lang: en
source: "[[projects/pathfinder/sources/docs/evaluation/python_function_check_orchestrator_policy.md]]"
---

> **TL;DR**: This report records the grouped deterministic checks for PathFinder's Python-owned orchestrator policy seam.

## Summary
This report covers the pure Python policy inside `backend/orchestrator_graph.py`: stage advancement, anchor handling, contradiction bookkeeping, counter windows, and route decisions.

The grouped pass is green and now goes beyond formatter helpers to cover actual stage-manager and counter-manager behavior, which was the higher-risk seam after the anchor-stage and escalation refactors.

## Key Points
- This is the highest-value deterministic seam above the current Stage 4 wrapper pass.
- The grouped pass now covers route and counter policy directly.
- This group passed on 2026-04-09.

## Related
- [[projects/pathfinder/notes/docs-python-function-check-how-to-use]]
- [[projects/pathfinder/notes/docs-python-function-check-stage-helper-matrix]]

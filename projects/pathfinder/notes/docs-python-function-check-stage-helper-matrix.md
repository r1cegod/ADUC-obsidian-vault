---
type: source-summary
title: "Python Function Check - Stage Helper Matrix"
created: 2026-04-09
updated: 2026-04-09
tags:
  - project/pathfinder
  - pathfinder
  - evaluation
status: active
lang: en
source: "[[projects/pathfinder/sources/docs/evaluation/python_function_check_stage_helper_matrix.md]]"
---

> **TL;DR**: This report records the cross-graph helper parity checks and the Thinking stale-`done` bug they exposed and closed.

## Summary
This report covers the repeated helper logic across all six stage graphs: current-stage resolution, reopen invalidation, and retrieval routing. Its value is consistency, not depth in one stage.

It is also the most important report from the first grouped pass because it exposed a real backend inconsistency: Thinking could lower confidence under the done threshold and still keep `done=True`. That mismatch is now fixed and recorded here.

## Key Points
- The first grouped pass exposed a real Thinking bug, not just missing coverage.
- The helper suite now runs through `unittest` end-to-end instead of silently skipping the legacy bare-function files.
- This group passed after the fix on 2026-04-09.

## Related
- [[projects/pathfinder/notes/docs-python-function-check-how-to-use]]
- [[projects/pathfinder/notes/docs-thinking-evaluation]]

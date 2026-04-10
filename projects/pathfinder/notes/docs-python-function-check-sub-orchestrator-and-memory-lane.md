---
type: source-summary
title: "Python Function Check - Sub-Orchestrator And Memory Lane"
created: 2026-04-10
updated: 2026-04-10
tags:
  - project/pathfinder
  - pathfinder
  - evaluation
status: active
lang: en
source: "[[projects/pathfinder/sources/docs/evaluation/python_function_check_sub_orchestrator_and_memory_lane.md]]"
---

> **TL;DR**: This report records the grouped deterministic checks for `routing_memory` pruning, sub-orchestrator routing policy, and the focused sub-orchestrator eval entrypoints.

## Summary
This report adds the fifth Python-function-check bucket for the sub-orchestrator lane. It proves the deterministic parts of the lane without replay: prune planning, worker selection, focus-entry routing, and the policy that `compliance` should not wake up just because the periodic every-5-turn refresh fired.

The grouped pass is green, which means the sub-orchestrator lane now has both a dedicated focused eval workflow and its own cheap deterministic seam proof.

## Key Points
- This is the cheapest proof for the `routing_memory` and sub-orchestrator maintenance lane.
- The pass includes the direct focus-eval entrypoints in addition to the router and prune-plan logic.
- The current policy keeps periodic `compliance` refresh conservative.

## Related
- [[projects/pathfinder/notes/docs-python-function-check-how-to-use]]
- [[projects/pathfinder/notes/docs-sub-orchestrator-focus-eval-how-to-use]]
- [[projects/pathfinder/notes/docs-sub-orchestrator-evaluation]]

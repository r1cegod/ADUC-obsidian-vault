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

> **TL;DR**: This report records the grouped deterministic checks for main `messages` pruning, `routing_memory` pruning, sub-orchestrator routing policy, and the focused sub-orchestrator eval entrypoints.

## Summary
This report adds the fifth Python-function-check bucket for the message-memory lanes. It proves the deterministic parts without replay: main `messages` pruning before orchestrator prompting, `routing_memory` prune planning, worker selection, and focus-entry routing.

The grouped pass is green, which means the sub-orchestrator lane now has both a dedicated focused eval workflow and its own cheap deterministic seam proof.

## Key Points
- This is the cheapest proof for the main `messages`, `routing_memory`, and sub-orchestrator maintenance lanes.
- The pass includes the direct focus-eval entrypoints in addition to the router and prune-plan logic.
- The current policy keeps periodic `compliance` refresh in the every-5-turn worker pass.

## Related
- [[projects/pathfinder/notes/docs-python-function-check-how-to-use]]
- [[projects/pathfinder/notes/docs-sub-orchestrator-focus-eval-how-to-use]]
- [[projects/pathfinder/notes/docs-sub-orchestrator-evaluation]]

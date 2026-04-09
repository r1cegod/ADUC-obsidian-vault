---
type: source-summary
title: "Python Function Check - Output And Evaluation Seams"
created: 2026-04-09
updated: 2026-04-09
tags:
  - project/pathfinder
  - pathfinder
  - evaluation
status: active
lang: en
source: "[[projects/pathfinder/sources/docs/evaluation/python_function_check_output_and_evaluation_seams.md]]"
---

> **TL;DR**: This report records the grouped deterministic checks for evaluation prep, compiler prompt assembly, output sanitization, and stage naming.

## Summary
This report covers the lower-cost stage-to-output seam shared by `backend/evaluation_graph.py`, `backend/output_graph.py`, `backend/data/prompts/output.py`, stage contracts, and frontend serialization.

The grouped pass is green and now covers a broader seam than before, including context-compiler delegation and output sanitization in addition to the earlier queue-tagging and stage-contract checks.

## Key Points
- This is the cheapest visible-response seam below replay.
- The grouped pass now covers compiler delegation and sanitization explicitly.
- This group passed on 2026-04-09.

## Related
- [[projects/pathfinder/notes/docs-python-function-check-how-to-use]]
- [[projects/pathfinder/notes/docs-evaluation-graph]]

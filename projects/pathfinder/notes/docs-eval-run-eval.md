---
type: source-summary
title: "eval/run_eval.py - How To Use"
created: 2026-04-06
updated: 2026-04-06
tags:
  - project/pathfinder
  - pathfinder
  - evaluation
  - workflow
status: active
lang: en
source: "[[projects/pathfinder/sources/docs/delegated/eval_run_eval.md]]"
---

> **TL;DR**: This doc explains the evaluation runner as a trace-capture tool that replays JSONL inputs through a chosen graph and saves full run outputs for human audit.

## Summary
The runner guide documents `eval/run_eval.py` as a generic replay harness for PathFinder graphs. It does not decide whether a run is correct; it executes a graph against prepared inputs and writes detailed traces so a human evaluator can inspect behavior.

The guide is especially useful because it explains the full flow from CLI arguments to graph loading, state normalization, graph invocation, trace writing, and summary reporting. It also distinguishes `single` mode from `multi` mode and makes clear when each should be used.

For the vault, this note is the operational map for replay-based evaluation. It is the doc to read when someone asks how PathFinder's audit datasets are actually executed.

## Key Points
- The runner is an execution and trace tool, not an automatic judge.
- `multi` mode is the normal mode for isolated attack datasets.
- The guide explains the setup, dispatch, core run path, and reporting shape.

## Details
### Evaluation Use
Use this doc when preparing new stage attacks, debugging trace output, or adding a new graph to the evaluation registry.

### Architectural Value
The guide doubles as an explanation of how isolated stage graphs are tested without a live full-conversation loop.

## Related
- [[projects/pathfinder/notes/docs-stage-evaluation]]
- [[projects/pathfinder/notes/docs-data-agent-evaluation]]
- [[projects/pathfinder/notes/pathfinder-docs-ingest]]

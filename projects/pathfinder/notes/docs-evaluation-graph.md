---
type: source-summary
title: "Evaluation Graph"
created: 2026-04-07
updated: 2026-04-07
tags:
  - project/pathfinder
  - pathfinder
  - evaluation
  - workflow
status: active
lang: en
source: "[[projects/pathfinder/sources/docs/delegated/evaluation_graph.md]]"
---

> **TL;DR**: This doc defines a cheaper replay seam that runs `stage_graph -> context_compiler -> output_compiler` without the orchestrator, so stage-local handoffs can be tested against the final Vietnamese reply.

## Summary
`evaluation_graph.md` is the implementation spec for the missing replay seam between the stage agents and the output compiler. It exists because the current eval runner only supports stage-only replay, output-only replay, or the full orchestrator path, which leaves an unnecessary cost gap when the real question is whether the compiler preserves a stronger stage-local handoff.

The core design is a wrapper graph with one prep node, the target stage graph, `context_compiler`, and `output_compiler`. The prep node is the important detail: it normalizes stage-only datasets by copying the target stage queue into `messages` when needed and seeding `stage.stage_related` when the row omitted it, so the compiler sees the same context the evaluator actually intended to test.

This note matters because it narrows the production claim correctly. The wrapper proves stage + compiler behavior, not full orchestrator behavior. That makes it the right next gate for the knowledge agents without pretending the routing layer has already been certified.

## Key Points
- The wrapper graph is for replay evaluation, not for production runtime.
- It skips the high-cost orchestrator but still tests the only student-facing response node.
- `evaluation_prep` exists to protect the compiler seam from misleading empty-context traces.
- The recommended first targets are `thinking_eval`, `purpose_eval`, and `goals_eval`.

## Details
### When To Use It
Use this doc when the task is about compiler-wiring replay, registering new eval graphs in `eval/run_eval.py`, or deciding what the next meaningful production gate should be after stage-local prompt hardening.

### Why It Matters
Stage-local `PROBE:` quality is only half the story. The actual user-visible question is whether that handoff survives prompt assembly and becomes a stronger Vietnamese student-facing reply.

### Raw Source
- Delegated doc source: [[projects/pathfinder/sources/docs/delegated/evaluation_graph.md]]
- Runner guide: [[projects/pathfinder/sources/docs/delegated/eval_run_eval.md]]

## Related
- [[projects/pathfinder/notes/docs-eval-run-eval]]
- [[projects/pathfinder/notes/docs-knowledge-agent-evaluation]]
- [[projects/pathfinder/notes/pathfinder-evaluation-hub]]
- [[projects/pathfinder/notes/pathfinder-workflow-hub]]

---
type: source-summary
title: "Knowledge Agent Evaluation Guide"
created: 2026-04-07
updated: 2026-04-07
tags:
  - project/pathfinder
  - pathfinder
  - evaluation
status: active
lang: en
source: "[[projects/pathfinder/sources/docs/evaluation/knowledge_agent_evaluation.md]]"
---

> **TL;DR**: This guide defines how pure reasoning stages should be evaluated, from extractor calibration through analyst `PROBE:` quality to final `output_compiler` preservation.

## Summary
The knowledge-agent evaluation guide is the general contract for `thinking`, `purpose`, and `goals`. It does for reasoning-only stages what the data-agent guide does for retrieval-enabled stages: it defines the real failure seams, the evaluation layers, and the minimum bar for calling a stage hardened.

Its main value is that it keeps the seam hierarchy clean. Stage-local replay and stage-plus-compiler replay are different gates with different failure modes, and the guide states that clearly instead of burying the distinction inside one status page.

This makes the stage-specific logs easier to read. They can focus on concrete attacks and results while this guide holds the reusable evaluation model shared by the knowledge-agent trio.

## Key Points
- Knowledge agents fail on calibration, contradiction quality, `PROBE:` quality, and output preservation.
- Stage-local replay and `*_eval` replay are separate evaluation layers.
- Full orchestrator replay is not the default gate for knowledge-agent hardening.

## Details
### Companion To The Data-Agent Guide
This doc is the reasoning-stage counterpart to `docs/evaluation/data_agent_evaluation.md`.

### Use Pattern
Read this before working on Thinking, Purpose, or Goals evaluation when the question is about the general seam and pass/fail model rather than one stage's specific attacks.

## Related
- [[projects/pathfinder/notes/docs-data-agent-evaluation]]
- [[projects/pathfinder/notes/docs-thinking-evaluation]]
- [[projects/pathfinder/notes/docs-purpose-evaluation]]
- [[projects/pathfinder/notes/docs-goals-evaluation]]

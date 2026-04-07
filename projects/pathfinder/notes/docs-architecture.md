---
type: source-summary
title: "PathFinder Architecture"
created: 2026-04-06
updated: 2026-04-06
tags:
  - project/pathfinder
  - pathfinder
  - architecture
  - docs
status: active
lang: en
source: "[[projects/pathfinder/sources/docs/architecture/docs/ARCHITECTURE.md]]"
---

> **TL;DR**: This is the main architecture source for PathFinder: a LangGraph-based Vietnamese counseling system where Python owns control flow and LLMs own classification and synthesis.

## Summary
The architecture doc explains PathFinder as a supervisor-pattern multi-agent system for Vietnamese students. The graph shape is stable: input orchestrator, active stage agent, and output compiler, with the output compiler as the only student-facing response generator.

Its core design rule is explicit: LLMs classify and synthesize, but deterministic Python owns routing, counters, thresholds, and escalation logic. The document also locks the six-stage progression, the path-debate handoff as output case B2, and the current cost and reliability model.

This is the best first technical overview for any agent entering the project. It connects topology, state layers, design decisions, and failure modes in one place.

## Key Points
- PathFinder uses six stage agents plus a separate output-compiler path debate mode.
- The orchestrator and counters are deterministic Python, not LLM-managed state.
- Stage agents follow a scoring-node then analyst-node pattern, with no student-facing chatbot node.

## Details
### System Shape
The doc describes the graph as `Input Orchestrator -> Active Stage Agent -> Output Compiler`. It also records the stage order and the case waterfall for the compiler.

### State And Reliability
It outlines the four-layer state model, the decay-counter system, and why behavioral safety depends on Python-managed thresholds rather than model memory.

### Durable Decisions
Several accepted ADRs live here: reasoning lock for `UserTag`, passive decay counters, block-based prompt assembly, and the analyst-only stage pattern.

## Related
- [[projects/pathfinder/notes/docs-state-architecture]]
- [[projects/pathfinder/notes/docs-project-context]]
- [[projects/pathfinder/notes/pathfinder-docs-ingest]]

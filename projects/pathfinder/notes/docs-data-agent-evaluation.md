---
type: source-summary
title: "Data Agent Evaluation Guide"
created: 2026-04-06
updated: 2026-04-07
tags:
  - project/pathfinder
  - pathfinder
  - evaluation
  - retrieval
status: active
lang: en
source: "[[projects/pathfinder/sources/docs/evaluation/data_agent_evaluation.md]]"
---

> **TL;DR**: This guide defines how retrieval-enabled stages should be evaluated as retrieval-plus-reasoning systems rather than as normal prompt-only stage agents.

## Summary
The data-agent evaluation guide reframes `job`, `major`, and `uni` as retrieval-plus-reasoning stages. The extractor still controls profile confidence, but the analyst also decides when to search, how to query for Vietnamese reality, and how to turn evidence into a meaningful contradiction or trade-off.

The document lays out six evaluation seams: retrieval decision, query quality, evidence grounding, consensus-crash quality, confidence calibration, and tool discipline. That matters because a retrieval stage can sound plausible while still failing at the actual market-data work.

This is one of the most strategically important docs in the corpus because it records the testing model for the web-enabled part of PathFinder.

## Key Points
- Retrieval stages fail in different ways than pure reasoning stages.
- Good prose is not enough; the evaluation seam includes search decisions and evidence use.
- Replay with frozen tool outputs is the preferred long-term regression model.

## Details
### What It Adds
The guide extends the normal stage-audit mindset into tool usage, query targeting, and confidence discipline after search.

### Near-Term Constraint
The current repo can replay attacks and save traces, but it does not yet inject mocked tool outputs, so some of the target workflow is still aspirational.

## Related
- [[projects/pathfinder/notes/docs-knowledge-agent-evaluation]]
- [[projects/pathfinder/notes/docs-job-evaluation]]
- [[projects/pathfinder/notes/docs-research-sources]]
- [[projects/pathfinder/notes/docs-eval-run-eval]]

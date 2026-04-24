---
type: source-summary
title: "Job Agent Evaluation And Audit Log"
created: 2026-04-06
updated: 2026-04-07
tags:
  - project/pathfinder
  - pathfinder
  - evaluation
  - job
status: active
lang: en
source: "[[projects/pathfinder/sources/docs/evaluation/job_evaluation.md]]"
---

> **TL;DR**: This audit log now covers both the first dedicated `job` hardening pass and the 2026-04-07 `job_eval` Stage 4 replay, where all 4 attacks preserved populated research, `PROBE:`, and a sharp final Vietnamese contradiction.

## Summary
The job evaluation doc records the attack-driven analysis of the `job` stage. It focuses on failures that are more structural than rhetorical: search triggering, evidence use, and the collapse of analyst handoff after tool use.

This file is useful because it captures both the transition point where the team realized retrieval stages need a harder architectural seam than simple stage prompts, and the later confirmation that the cheaper `job_eval` wrapper still carries that contradiction through `context_compiler` and `output_compiler`.

If an agent is touching `backend/job_graph.py`, this note is part of the must-read set.

## Key Points
- The `job` stage exposed retrieval-specific failure modes, not just prompt wording issues.
- Search quality and post-tool synthesis were central weaknesses.
- `job` now also passes the current Stage 4 stage + compiler seam on `eval/job_attack.jsonl`.
- The remaining cleanup item is serializer-warning noise around structured outputs, not contradiction loss.

## Details
### Debugging Value
Use this note to understand why the `job` graph was hardened around evidence grounding and reliable `PROBE:` handoff, and why the current open risk is warning cleanup rather than student-facing contradiction loss.

### Position In The Corpus
This is both an audit history and a bridge into the broader retrieval-agent evaluation model.

## Related
- [[projects/pathfinder/notes/docs-data-agent-evaluation]]
- [[projects/pathfinder/notes/docs-research-sources]]
- [[projects/pathfinder/notes/docs-knowledge-agent-evaluation]]

---
type: source-summary
title: "Job Agent Evaluation And Audit Log"
created: 2026-04-06
updated: 2026-04-06
tags:
  - project/pathfinder
  - pathfinder
  - evaluation
  - job
status: active
lang: en
source: "[[projects/pathfinder/sources/docs/evaluation/job_evaluation.md]]"
---

> **TL;DR**: This audit log captures the first dedicated hardening work for the `job` stage, especially the retrieval-stage failures and the move toward a stronger research-and-synthesis seam.

## Summary
The job evaluation doc records the attack-driven analysis of the `job` stage. It focuses on failures that are more structural than rhetorical: search triggering, evidence use, and the collapse of analyst handoff after tool use.

This file is useful because it captures the transition point where the team realized retrieval stages need a harder architectural seam than simple stage prompts. It connects stage-local attacks to the later planner/researcher/synthesizer direction reflected elsewhere in the repo.

If an agent is touching `backend/job_graph.py`, this note is part of the must-read set.

## Key Points
- The `job` stage exposed retrieval-specific failure modes, not just prompt wording issues.
- Search quality and post-tool synthesis were central weaknesses.
- The doc helps explain why Stage 3 evolved beyond a normal stage-agent pattern.

## Details
### Debugging Value
Use this note to understand why the `job` graph was hardened around evidence grounding and reliable `PROBE:` handoff.

### Position In The Corpus
This is both an audit history and a bridge into the broader retrieval-agent evaluation model.

## Related
- [[projects/pathfinder/notes/docs-data-agent-evaluation]]
- [[projects/pathfinder/notes/docs-research-sources]]
- [[projects/pathfinder/notes/docs-stage-evaluation]]

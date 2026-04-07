---
type: source-summary
title: "PathFinder Evaluation Pipeline"
created: 2026-04-07
updated: 2026-04-07
tags:
  - project/pathfinder
  - pathfinder
  - evaluation
  - workflow
status: active
lang: en
source: "[[projects/pathfinder/sources/docs/evaluation/eval_how_to_use.md]]"
---

> **TL;DR**: This doc is the canonical evaluation workflow for PathFinder, defining the production-first loop, the 3-round gate, trace-audit expectations, and the required vault updates after each run.

## Summary
This evaluation-pipeline doc is broader than a runner guide. It defines the official workflow for planning, running, auditing, and closing evaluation work across the PathFinder stages, with production behavior as the starting point rather than CLI mechanics.

Its strongest rule is structural: a stage cannot drift through endless hardening. The doc caps a production-ready sequence at three rounds, requires one finished stage per round, and forces a user conversation between rounds before work continues.

It also clarifies the split between workflow and tooling. `eval/run_eval.py` is only the execution harness; this file is the process contract that says what must be planned, what must be audited in traces, and what must be recorded back into the vault.

## Key Points
- This is the single source of truth for the evaluation workflow, not just runner usage.
- The evaluation loop starts from production targets, not from attack JSONL authoring.
- A stage needs a capped 3-round cycle and post-run user review before any production-ready claim.
- Trace audit and vault writeback are required parts of completion, not optional cleanup.

## Details
### Use Pattern
Read this before non-trivial evaluation work when the question is "what is the official evaluation process?" rather than "how do I use the runner?"

### Relationship To The Runner Guide
This doc owns workflow and signoff policy. The older runner guide focuses on `eval/run_eval.py` as a replay harness and trace writer.

### Why It Belongs In `docs/evaluation`
Unlike delegated implementation walkthroughs, this file defines PathFinder's live evaluation policy. Its natural home is the evaluation-doc tree beside the stage logs and data-agent guide.

## Related
- [[projects/pathfinder/notes/docs-knowledge-agent-evaluation]]
- [[projects/pathfinder/notes/docs-eval-run-eval]]
- [[projects/pathfinder/notes/docs-data-agent-evaluation]]
- [[projects/pathfinder/notes/pathfinder-evaluation-hub]]

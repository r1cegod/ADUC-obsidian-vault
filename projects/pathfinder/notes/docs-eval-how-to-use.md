---
type: source-summary
title: "PathFinder Evaluation Pipeline"
created: 2026-04-07
updated: 2026-04-09
tags:
  - project/pathfinder
  - pathfinder
  - evaluation
  - workflow
status: active
lang: en
source: "[[projects/pathfinder/sources/docs/evaluation/eval_how_to_use.md]]"
---

> **TL;DR**: This doc is the canonical replay-evaluation workflow for PathFinder, while the newer Python-function-check doc holds the cheaper deterministic backend gate.

## Summary
This evaluation-pipeline doc is broader than a runner guide. It defines the official workflow for planning, running, auditing, and closing replay-driven evaluation work across the PathFinder stages, with production behavior as the starting point rather than CLI mechanics.

Its strongest rule is structural: a stage cannot drift through endless hardening. The doc caps a production-ready sequence at three rounds, requires one finished stage per round, and forces a user conversation between rounds before work continues.

It also clarifies the split between workflow layers. `eval/run_eval.py` is the execution harness for higher-cost replay, while the new Python-function-check doc owns the lower-cost deterministic backend gate. This file remains the process contract for replay planning, trace audit, and vault writeback.

## Key Points
- This is the single source of truth for the evaluation workflow, not just runner usage.
- It now explicitly sits beside the Python-function-check workflow instead of pretending replay is the only evaluation layer.
- The evaluation loop starts from production targets, not from attack JSONL authoring.
- A stage needs a capped 3-round cycle and post-run user review before any production-ready claim.
- Trace audit and vault writeback are required parts of completion, not optional cleanup.

## Details
### Use Pattern
Read this before non-trivial evaluation work when the question is "what is the official evaluation process?" rather than "how do I use the runner?"

### Relationship To The Runner Guide
This doc owns replay workflow and signoff policy. The newer Python-function-check doc owns the cheaper deterministic backend seam proof.

### Why It Belongs In `docs/evaluation`
Unlike delegated implementation walkthroughs, this file defines PathFinder's live evaluation policy. Its natural home is the evaluation-doc tree beside the stage logs and data-agent guide.

## Related
- [[projects/pathfinder/notes/docs-knowledge-agent-evaluation]]
- [[projects/pathfinder/notes/docs-python-function-check-how-to-use]]
- [[projects/pathfinder/notes/docs-eval-run-eval]]
- [[projects/pathfinder/notes/docs-data-agent-evaluation]]
- [[projects/pathfinder/notes/pathfinder-evaluation-hub]]

---
type: hub
title: Raven Evaluation Hub
created: '2026-04-25'
updated: '2026-05-03'
tags:
  - project/raven
  - evaluation
  - workflow
  - docs
status: active
lang: en
feeds_into:
  - projects/raven/README.md
  - projects/raven/notes/raven-context-hub.md
---
> **TL;DR**: Default router for Raven evaluation work. Use this hub for evaluation boundaries, how-to workflows, per-run reports, rolling insights, prompt-evolution links, and repo evidence pointers.

## Growth Contract
- Parent branch: [[projects/raven/README]]
- Node role: hub
- First parent link: [[projects/raven/README]]
- Growth trigger: split only when a feature or eval family accumulates multiple child types such as workflow, report, insight, prompt change, and evidence pointers.
- Forbidden contents: runner scripts, JSONL datasets, trace folders, temporary reproduction artifacts, and implementation architecture.
- Expected child types: boundary/rule leaves, workflow leaves, report leaves, rolling insight leaves, prompt routes, and evidence pointers.

## Purpose

Raven evaluation is a branch, not a scattered set of report links. Its default loop is two-phase: bootstrap the dataset from Duc's audit taste, then run eval until the current dataset standard is met.

```text
evaluation hub
  -> boundary/rule leaf
  -> how-to workflow leaf
  -> per-run report leaves
  -> rolling insights leaf
  -> prompt route when eval changes prompts
  -> executable evidence pointer
```

Use this hub before creating or reading multiple Raven evaluation notes.

## Start Here

- Need the reusable evaluation and production-prompt method: [[wiki/synthesis/evaluation-production-prompt-domain]]
- Need the vault-vs-repo boundary: [[projects/raven/notes/raven-evaluation-domain]]
- Need the evaluation workflow: [[projects/raven/notes/raven-eval-how-to-use]]
- Need rolling lessons: [[projects/raven/notes/raven-evaluation-insights]]
- Need latest daily full-graph eval: [[projects/raven/notes/raven-daily-eval-2026-05-03]]
- Need current Tier 1 ranker report: [[projects/raven/notes/raven-tier-1-ranker-evaluation]]
- Need current completed enricher report: [[projects/raven/notes/raven-enricher-evaluation]]
- Need prompt evolution route: [[projects/raven/notes/raven-prompt-hub]]
- Need source/evidence boundary: [[projects/raven/sources/README]]

## Branch Rule

New Raven eval reports link here first, not directly from the project README. The eval domain must be updated before closeout whenever a run changes workflow, standards, or durable judgment.

```text
new eval run
  -> dataset bootstrap from Duc audit taste
  -> executable evidence in repo eval/
  -> run until current dataset standard is met or blocker is named
  -> report leaf in projects/raven/notes/
  -> link report from raven-evaluation-hub
  -> update raven-evaluation-insights only if cross-run learning changed
  -> patch eval domain docs if workflow/standard changed
  -> log the work
```

## What This Branch Owns

```text
evaluation workflow
production-readiness reports
audit narratives
rolling evaluation insight
human signoff summaries
pointers to executable evidence
```

## What This Branch Does Not Own

```text
runner scripts
JSONL datasets
trace folders
temporary reproduction artifacts
full raw evidence dumps
```

Those live in the repo `eval/` workspace or the Raven source/evidence lane as pointers.

## Current Evaluation State

- [[projects/raven/notes/raven-enricher-evaluation]] passed 15/15 live cases across 3 rounds on 2026-04-20.
- [[projects/raven/notes/raven-tier-1-ranker-evaluation]] passed the first synthetic prompt-contract gate 8/8 on 2026-04-26 after production-formula refactor.
- Token-cost architecture now uses a one-shot high-model final selector over readable appended `PACKET` / `<candidate>` delegation blocks, without hidden code-side compacting.
- Final selector synthetic delegation eval passed 1/1 on 2026-04-26 under the old binary contract; current request-era final selector labels Tier 1 survivors as `maybe` / `click` / `must_click`.
- Latest daily full-graph eval is [[projects/raven/notes/raven-daily-eval-2026-05-03]]: Phase 1 run `2` for `how to grow a youtube channel`, 3 queries, 11 candidates, Tier 1 labels `keep 9 / throw_out 2`, final-selector packet input count `9`, final labels `must_click 2 / click 3 / maybe 4 / unlabeled 2`, packet `eval/packets/03-May-2026/08:07:40_raven_full_how-to-grow-a-youtube-channel`. Daily eval stops after Phase 1 and waits for Duc audit before any focused Phase 2 dataset/node eval.
- Earlier live candidate audit seed was run `6` for `how to grow a youtube channel`: 254 candidates, final counts `{'keep': 8, 'throw_out': 246}`, focused audit artifact `eval/live/run_0006_how-to-grow-a-youtube-channel-live-gate/ranker_tier1_audit.md`.
- Run `6` audit has been converted into focused local eval bootstraps for enricher, Tier 1, and Tier 1 final. Current context records the later 2026-04-30 focused rerun as green: enricher focused regression `1/1`, Tier 1 focused YouTube-growth `17/17`, Tier 1 final focused bootstrap `1/1`, baseline enricher `5/5`, baseline Tier 1 `8/8`, and baseline final `1/1`.
- Next evaluation pressure is not more broad Tier 1 expansion by default; it is deciding whether the first product-facing output should be a kept-source report / vault-safe source card, while preserving the NotebookLM/channel-clone vs broad beginner-mistake boundary in future audits. Also watch enricher query specificity so broad misconception phrasing does not recreate the run-6 off-target candidate pool.

## Related

- [[projects/raven/README]]
- [[wiki/synthesis/evaluation-production-prompt-domain]]
- [[projects/raven/notes/raven-evaluation-domain]]
- [[projects/raven/notes/raven-eval-how-to-use]]
- [[projects/raven/notes/raven-evaluation-insights]]
- [[projects/raven/notes/raven-tier-1-ranker-evaluation]]
- [[projects/raven/notes/raven-enricher-evaluation]]
- [[projects/raven/notes/raven-prompt-hub]]
- [[projects/raven/notes/raven-workflow-hub]]

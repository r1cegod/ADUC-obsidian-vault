---
type: hub
title: Raven Evaluation Hub
created: '2026-04-25'
updated: '2026-04-27'
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

Raven evaluation is a branch, not a scattered set of report links.

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
- Need current Tier 1 ranker report: [[projects/raven/notes/raven-tier-1-ranker-evaluation]]
- Need current completed enricher report: [[projects/raven/notes/raven-enricher-evaluation]]
- Need prompt evolution route: [[projects/raven/notes/raven-prompt-hub]]
- Need source/evidence boundary: [[projects/raven/sources/README]]

## Branch Rule

New Raven eval reports link here first, not directly from the project README.

```text
new eval run
  -> executable evidence in repo eval/
  -> report leaf in projects/raven/notes/
  -> link report from raven-evaluation-hub
  -> update raven-evaluation-insights only if cross-run learning changed
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
- Final selector synthetic delegation eval passed 1/1 on 2026-04-26; output is binary `keep` / `throw_out` only.
- Latest live candidate audit seed is run `6` for `how to grow a youtube channel`: 254 candidates, final counts `{'keep': 8, 'throw_out': 246}`, focused audit artifact `eval/live/run_0006_how-to-grow-a-youtube-channel-live-gate/ranker_tier1_audit.md`.
- Run `6` audit has been converted into focused local eval bootstraps for enricher, Tier 1, and Tier 1 final. After calibration: enricher focused regression `1/1`, Tier 1 final focused bootstrap `1/1`, baseline enricher `5/5`, baseline Tier 1 `8/8`, baseline final `1/1`; focused Tier 1 YouTube-growth eval is still `15/17`.
- Next evaluation pressure is the remaining Tier 1 boundary: NotebookLM/channel-clone leverage should probably survive as at least maybe, while broad wrong-language beginner-mistake metadata should stay skip. Also watch enricher query specificity so broad misconception phrasing does not recreate the run-6 off-target candidate pool.

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

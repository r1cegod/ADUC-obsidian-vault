---
type: note
title: Raven Evaluation Workflow
created: '2026-04-22'
updated: '2026-05-03'
tags:
  - project/raven
  - evaluation
  - workflow
  - docs
status: active
lang: en
feeds_into:
  - projects/raven/notes/raven-evaluation-hub.md
---
> **TL;DR**: This is the official how-to for Raven evaluation work. Use it to run, audit, write back, and evolve Raven evaluation loops so the domain compounds instead of resetting each run.

## Growth Contract
- Parent branch: [[projects/raven/notes/raven-evaluation-hub]]
- Node role: workflow leaf
- First parent link: [[projects/raven/notes/raven-evaluation-hub]]
- Growth trigger: update when Raven evaluation workflow changes; split only if a recurring eval family needs its own workflow leaf.
- Forbidden contents: raw traces, runner scripts, datasets, per-run reports, and prompt contracts.
- Source/evidence boundary: workflow lives here; executable evidence remains in repo `eval/`, with human-readable reports linked through the evaluation hub.

## Purpose

Raven evaluation needs one operational workflow doc, not scattered memory.

```text
eval run
  -> audit evidence
  -> human-readable report
  -> insight writeback
  -> next run improves
```

This note owns the workflow.

## Two-Phase Eval Pipeline

Raven eval work has two phases:

```text
1. Dataset bootstrap
   -> collect Duc audit taste from human audit artifacts
   -> convert it into explicit cases and expected judgments
   -> preserve edge cases, disagreement, and failure reasons

2. Run eval until dataset standard
   -> run focused eval against the bootstrapped dataset
   -> patch prompt/code/dataset only from inspected failures
   -> rerun until the current dataset standard is met
   -> write back the report and durable insight
```

A green command is not success unless it satisfies the dataset standard. If the run exposes a missing taste rule, update the dataset or eval notes before expanding the system.

## Daily Eval Quick Operation

`daily eval` is a quick operation, not a planning phrase.

```text
Daily eval
  -> lock Raven eval lane in KICKSTART
  -> run one full graph with `eval/run_observation.py full`
  -> inspect packet markdown and trace summary
  -> stop after Phase 1 and wait for Duc audit
  -> enter Phase 2 focused dataset/node eval only after Duc audit lines or explicit approval
  -> write the vault report and daily log
```

Default current query unless Duc names another target:

```bash
./.venv/bin/python eval/run_observation.py full --graph raven --request "how to grow a youtube channel"
```

Phase 2 is human-gated. Do not run focused dataset/node eval, patch prompts, or patch datasets just because the full graph ran or the packet looks suspicious. Use Duc audit lines or explicit approval as the trigger.

Expected packet audit surface:

```text
report first
  -> counts and filtering summary before details
  -> YouTube raw hits / unique videos / candidates / filtered-out counts
  -> Tier 1 audit index before per-candidate detail
  -> candidate detail includes title, query, label, channel, date, views, link, preview, and ranker reasoning
  -> final selector report shows actual non-skip input count before kept rows
```

## Current Use Case

Primary current use case:

```text
Tier 1 ranker evaluation
  -> run filter
  -> generate trace + markdown audit file
  -> Duc audits
  -> Codex reads audit
  -> Codex updates prompt / dataset
  -> rerun
```

## Current Harness

Raven evals now route through one repo-local observation entrypoint:

```bash
./.venv/bin/python eval/run_observation.py dataset --suite enricher --file eval/enricher_cases.jsonl
./.venv/bin/python eval/run_observation.py dataset --suite ranker_tier1 --file eval/ranker_tier1_cases.jsonl
./.venv/bin/python eval/run_observation.py dataset --suite ranker_tier1_final --file eval/ranker_tier1_final_cases.jsonl
```

Focused runtime observation uses the same harness:

```bash
./.venv/bin/python eval/run_observation.py full --graph raven --request "how to grow a youtube channel"
./.venv/bin/python eval/run_observation.py node --graph raven --node enricher --state-json '{"query":"how to find leads"}'
./.venv/bin/python eval/run_observation.py checkpoint-node --graph raven --thread-id "<thread_id>" --checkpoint-id "<checkpoint_id>" --node ranker_tier1_final
```

The old eval scripts are compatibility wrappers only:

```text
eval/run_enricher_eval.py
eval/run_ranker_tier1_eval.py
eval/run_ranker_tier1_final_eval.py
```

They should not receive new behavior. Add new eval behavior to `src/backend/observability/` and expose it through `eval/run_observation.py`.

## Workflow

Daily eval means a fresh full-graph run first. Focused node/dataset evals are the second-stage learning loop, not a substitute for the daily run.

1. Define the evaluation target and dataset standard.
2. For daily eval, run full-graph executable evidence through `eval/run_observation.py full`.
3. Inspect the packet folder under repo `eval/packets/` only enough to summarize the Phase 1 packet.
4. Stop and wait for Duc audit. Do not start focused dataset/node eval from agent-only judgment.
5. After Duc audit lines or explicit approval, bootstrap or update the focused dataset from those audit artifacts before treating the eval as authoritative.
6. Run focused dataset/node evals until the current dataset standard is met, or record the blocker explicitly.
7. Patch prompt/code/dataset only from approved inspected failures and only inside the locked lane.
8. Write/update the evaluation report in the vault.
9. Write/update the rolling insights note with what the run taught the system.
10. Update the Raven eval workflow/domain/hub if the loop changed; this is top priority after eval work.
11. Update project routing only if the domain shape changed.
12. Log the work in the daily log.

## Write Boundary

```text
repo eval/
  -> executable evidence only
  -> packet folders under eval/packets/
  -> machine trace JSON
  -> fast human audit markdown

vault notes/
  -> workflow docs
  -> reports
  -> audit narratives
  -> compounding insights
  -> production-readiness decisions
```

## Required Outputs Per Non-Trivial Eval Cycle

Minimum closeout:

```text
1. one executable evidence trail
2. one human-readable evaluation report or audit artifact
3. one update to [[projects/raven/notes/raven-evaluation-insights]] when the run teaches anything durable
```

## Tier 1 Specific Flow

```text
ranker runs
  -> markdown audit file
  -> Duc audit line(s)
  -> Codex reads audit file
  -> dataset creation/update
  -> focused eval/rerank on that audited dataset
  -> prompt audit / upgrade
  -> rerun
```

After Duc audits a markdown file, do not run the full graph again by default. Full graph runs are only for collecting more/fresh candidates. Normal evolution uses the audited artifact and focused eval loop.

No separate complexity theater is required if this loop stays disciplined.

## Compounding Rule

Raven evaluation is not complete when the run finishes.
It is complete when the domain learned.

```text
run result
  -> report
  -> insight extraction
  -> next run starts stronger
```

## Related

- [[projects/raven/notes/raven-evaluation-hub]]
- [[projects/raven/notes/raven-evaluation-domain]]
- [[projects/raven/notes/raven-evaluation-insights]]
- [[projects/raven/notes/raven-source-ranker-draft]]
- [[projects/raven/notes/raven-enricher-evaluation]]
- [[projects/raven/README]]

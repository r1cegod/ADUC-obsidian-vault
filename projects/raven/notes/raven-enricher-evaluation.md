---
type: note
title: Raven Enricher Evaluation
created: '2026-04-20'
updated: '2026-04-26'
tags:
  - project/raven
  - evaluation
  - prompts
  - backend
status: active
lang: en
feeds_into:
  - projects/raven/notes/raven-evaluation-hub.md
  - projects/raven/notes/raven-architecture-hub.md
  - projects/raven/notes/raven-phase-1-build-plan.md
---
> **TL;DR**: Raven's query enricher prompt/one-node graph seam passed a 3-round live production gate on 2026-04-20 using `gpt-5.4-mini`. This signoff applies only to the enricher contract, not the full Raven discovery/rating loop.

## Growth Contract
- Parent branch: [[projects/raven/notes/raven-evaluation-hub]]
- Node role: report leaf
- First parent link: [[projects/raven/notes/raven-evaluation-hub]]
- Growth trigger: update only when the enricher gate, prompt contract, or production-readiness decision changes.
- Forbidden contents: runner scripts, raw traces, JSONL datasets, and unrelated Tier 1 ranker results.
- Source/evidence boundary: this page stores the human-readable signoff; executable traces remain under `/home/r1ceg/Raven/eval/`.

## Production Target

Lock the Phase 1 query enricher seam without adding architecture beyond Duc's active graph:

```text
query
  -> one LangGraph enricher node
  -> structured output: { queries: list[str] }
```

Production-safe behavior means Raven can expand a broad target into search-box-ready queries without answering the question, inventing fake sources, leaking prompt instructions, dropping the original target, or returning vague duplicate variants.

Architecture boundary set by Duc on 2026-04-20:

- use `gpt-5.4-mini`
- keep the graph as one node
- do not add graph architecture unless explicitly approved first
- let the LLM decide how many queries to create
- put production pressure in the prompt and eval, not in hidden graph post-processing

## Gate

Executable evidence lives in the Raven repo:

```text
/home/r1ceg/Raven/eval/run_enricher_eval.py
/home/r1ceg/Raven/eval/enricher_cases.jsonl
/home/r1ceg/Raven/eval/threads/<thread_id>/traces/run_*.json
```

The deterministic gate checks:

- exact target first
- at least one query returned
- no duplicate queries
- no empty queries
- target-token relevance ratio >= 0.8
- expected keyword presence with singular/plural normalization
- operational specificity scaled to the number of queries the LLM chose
- no system/developer/structured-output control leak

No gate enforces a fixed query count.

## Round Results

Command used for each live round:

```bash
./.venv/bin/python eval/run_enricher_eval.py --mode multi --workers 3
```

Round 1:

- Passed 5/5 with `gpt-5.4-mini` and the one-node graph.
- Trace roots:
  - `eval/threads/fcdbce58-1c7e-4865-92ff-a75883efdfdd/`
  - `eval/threads/98877bc8-7078-45d6-902d-5589997c114f/`
  - `eval/threads/25e79200-0380-4d9e-a03d-015d182c5f79/`
  - `eval/threads/53c15804-ae82-4787-9289-0cd30086157a/`
  - `eval/threads/87ae7618-509c-4f0e-860a-373388d566e5/`

Round 2:

- Passed 5/5 with `gpt-5.4-mini` and the one-node graph.
- Trace roots:
  - `eval/threads/028fe35d-8181-49af-9aea-e9aebe42a19a/`
  - `eval/threads/387c1e11-c22b-4a29-97aa-16e1da6bbeff/`
  - `eval/threads/bf27d96b-25a2-40d1-a104-d50b82802144/`
  - `eval/threads/af74b467-eaab-4757-aed9-cc28595d57fb/`
  - `eval/threads/3cc96d37-59b2-4a46-a2bd-2f13f410f199/`

Round 3:

- Passed 5/5 with `gpt-5.4-mini` and the one-node graph.
- Trace roots:
  - `eval/threads/a8f13ff1-98a8-4453-b1d2-6407488e81f0/`
  - `eval/threads/9edceadc-15e4-4c74-bb11-7160b6e5f49d/`
  - `eval/threads/784540b8-93c6-4803-b673-39737bdbfd86/`
  - `eval/threads/340f08f8-8b6e-426c-ad12-1d87eaf04dcb/`
  - `eval/threads/4eeaa87e-3746-42de-8e72-615862fa7a30/`

Final trace audit:

```text
15 / 15 live cases passed.
LLM-chosen query counts across final traces: 5-6.
Production ready: YES for the enricher prompt/one-node graph seam.
```

## Decision

The Raven query enricher seam is production-ready for Phase 1 use.

This does not mean Raven is production-ready end to end. The next product wire still has to connect enriched queries into metadata search/storage, then add rater and evolver gates.

## Correction Log

Earlier in the same work session, the graph had been over-constrained with code-side dedupe, exact-target insertion, metadata, and a 6-8 query range. That violated Duc's intended ownership boundary. The final implementation removed those graph-side controls and kept the contract inside the prompt/eval layer.

## Related

- [[projects/raven/README]]
- [[projects/raven/notes/raven-evaluation-hub]]
- [[projects/raven/notes/raven-evaluation-domain]]
- [[projects/raven/notes/raven-phase-1-build-plan]]
- [[projects/raven/notes/raven-phase-1-ingest-rating-plan]]
- [[projects/pathfinder/notes/docs-evaluation-domain]]
- [[projects/pathfinder/notes/docs-eval-how-to-use]]

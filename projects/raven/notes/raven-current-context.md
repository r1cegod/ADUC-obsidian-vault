---
type: note
title: Raven Current Context
created: '2026-04-25'
updated: '2026-04-27'
tags:
  - project/raven
  - context
  - engineering
  - evaluation
status: active
lang: en
feeds_into:
  - projects/raven/notes/raven-context-hub.md
  - projects/raven/README.md
  - context/hot.md
---
> **TL;DR**: Raven's live state is a Phase 1 Knowledge Signal Engine scaffold with query enrichment, YouTube metadata enrichment, SQLite logging/writeback, and the Tier 1 ranker/evaluation loop as the next meaningful branch.

## Growth Contract
- Parent branch: [[projects/raven/notes/raven-context-hub]]
- Node role: leaf
- First parent link: [[projects/raven/notes/raven-context-hub]]
- Growth trigger: split a topic out when it becomes durable architecture, evaluation, prompt, or workflow knowledge instead of live project state.
- Forbidden contents: stable architecture contracts, raw eval evidence, prompt contracts, and project-root routing.
- Source/evidence boundary: this page summarizes current state and points outward; exact repo evidence stays in the repo or Raven source lane.

## Live Repo

```text
/home/r1ceg/Raven
```

Use the repo virtual environment for backend commands:

```text
./.venv/bin/python
```

## Current Backend Seams

```text
Raven_graph.py
  -> one-node gpt-5.4-mini query enricher seam

search/youtube_search.py
  -> YouTube search.list -> videos.list enrichment
  -> ID-keyed metadata merge
  -> first view-count candidate filter
  -> normalized candidate output

data/search_base.py
  -> packs search results into SQLite
  -> writes query/API/candidate logs

db.py
  -> SQLite foundation
  -> run/query/candidate persistence
  -> query/API/candidate logging tables
```

## Verified Status

- One-node `gpt-5.4-mini` query enricher passed 15/15 live eval cases across 3 rounds.
- Enricher now returns prompt-owned `key_words` for title-gate filtering; baseline live enricher eval passed `5/5` and focused YouTube-growth eval passed `1/1` on 2026-04-27.
- Direct YouTube API smoke passed on 2026-04-24.
- SQLite search/writeback bridge smoke passed on 2026-04-24.
- YouTube import blocker was fixed by Duc before the passing smoke.

## Current Immediate Seam

```text
enriched query
  -> YouTube search.list
  -> videos.list enrichment
  -> query/API log rows
  -> filtered candidate row(s)
  -> candidate log rows
  -> joined DB readback
```

After that, the next project branch is:

```text
Reddit search
  -> Tier 1 ranker
  -> audit markdown
  -> human audit
  -> evaluator/evolver placeholder
```

Tier 1 ranker status: [[projects/raven/notes/raven-tier-1-ranker-evaluation]] now has green synthetic gates plus live audit seeds. Runtime uses LangGraph `Send` fan-out for parallel Tier 1 candidate scoring, then joins into `ranker_tier1_final`, a one-shot high-model selector over readable appended `PACKET` / `<candidate>` blocks. Enricher, Tier 1, and Tier 1 final currently run at temperature `0.7`. The Tier 1 prompt is budget-gated under 1000 tokens and currently measures 875 tokens. Latest checks: synthetic Tier 1 8/8 at thread `6c3aa212-2f65-476a-9e81-691760613cb7`; focused audited `how to find leads` Tier 1 dataset 4/4 at thread `551d7298-786a-457d-9d08-d96456eea9bc`; Tier 1 final synthetic metadata-packet check 1/1 at thread `e038b7ac-3441-4135-bbe1-31daf3cdc8bf`. Live run `5` produced 17 candidates and the derived dataset `eval/ranker_tier1_how_to_find_leads_audited.jsonl`. Fresh live run `6` for `how to grow a youtube channel` produced six enriched queries, 254 candidates, label counts `{'click': 1, 'maybe': 5, 'skip': 248}`, final counts `{'keep': 8, 'throw_out': 246}`, and focused audit seed `eval/live/run_0006_how-to-grow-a-youtube-channel-live-gate/ranker_tier1_audit.md`. Run `6` now has focused local eval bootstraps for enricher, Tier 1, and Tier 1 final. After calibration: enricher focused regression passed `1/1`, Tier 1 final focused bootstrap passed `1/1`, baseline enricher passed `5/5`, baseline Tier 1 passed `8/8`, and baseline final passed `1/1`; focused Tier 1 YouTube-growth eval remains `15/17`. Tier 1 final now receives `published_at` and `view_count` as freshness/traction signals; next calibration target is the remaining Tier 1 boundary around named-tool channel cloning vs broad beginner-mistake metadata.

## Current Architecture Route

```text
projects/raven/README
  -> [[projects/raven/notes/raven-architecture-hub]]
  -> projects/raven/notes/raven-feature-web.canvas
```

Current active architecture threads:

- [[projects/raven/notes/raven-vault-keeper-harness-architecture]]
- [[projects/raven/notes/raven-source-ranker-draft]]

## Current Evaluation Route

```text
projects/raven/README
  -> [[projects/raven/notes/raven-evaluation-hub]]
  -> [[projects/raven/notes/raven-evaluation-domain]]
  -> [[projects/raven/notes/raven-eval-how-to-use]]
```

Raven eval reports and production-readiness decisions are vault-canonical. Repo `eval/` is executable evidence only.

## Current Branch Debt

The renovation added the first high-level project branches:

```text
context
architecture
prompt
evaluation
workflow/rules
source/evidence
```

Do not create `main-flow`, `search-feature`, or `ranking-feature` hubs until Branch Growth proves real child pressure.

## Hygiene Flags

- Root `test/` in the Raven repo still violates the backend test-folder rule.
- Active `src/backend/search/reddit_search.py` is still empty; reference-only Reddit code is parked under `docs/reference/`.

## Related

- [[projects/raven/notes/raven-context-hub]]
- [[projects/raven/README]]
- [[projects/raven/notes/raven-architecture-hub]]
- [[projects/raven/notes/raven-evaluation-hub]]
- [[projects/raven/notes/raven-workflow-hub]]
- [[projects/raven/notes/raven-source-ranker-draft]]
- [[projects/raven/notes/raven-phase-1-build-plan]]

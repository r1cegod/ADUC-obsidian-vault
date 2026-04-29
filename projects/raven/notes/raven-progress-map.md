---
type: note
title: Raven Progress Map
created: '2026-04-29'
updated: '2026-04-29'
tags:
  - project/raven
  - context
  - workflow
  - docs
status: active
lang: en
feeds_into:
  - projects/raven/notes/raven-context-hub.md
  - projects/raven/README.md
---
> **TL;DR**: Raven has moved from an empty scaffold into a working Phase 1 signal engine: query enrichment, YouTube metadata discovery, SQLite logging/writeback, Tier 1 metadata ranking, final selection, and audit-backed focused eval. The immediate future is not Reddit or crawler work; it is finishing Tier 1 clarity and then choosing the next product direction from a clean past map.

## Growth Contract
- Parent branch: [[projects/raven/notes/raven-context-hub]]
- Node role: leaf
- First parent link: [[projects/raven/notes/raven-context-hub]]
- Growth trigger: split only if the map starts carrying detailed implementation logs, eval reports, or future planning branches that already have their own hub.
- Forbidden contents: raw traces, full code walkthroughs, full daily logs, prompt contracts, eval datasets, and speculative roadmap bloat.
- Source/evidence boundary: this page compiles from repo/vault logs and points outward; executable evidence stays in `/home/r1ceg/Raven/eval/`, repo dev logs, and Raven evaluation notes.

## Purpose

This is the clarity map for Raven's past and current edge.

```text
past logs
  -> compressed project memory
  -> current live edge
  -> future discussion queue
```

Use this when the question is: "What have I actually done so far, and what is the next unresolved decision?"

For live implementation detail, still read [[projects/raven/notes/raven-current-context]].
For eval status, read [[projects/raven/notes/raven-evaluation-hub]].

## One-Screen Shape

```text
empty repo shell
  -> one-node query enricher
  -> YouTube search adapter
  -> videos.list metadata enrichment
  -> SQLite run/query/API/candidate logs
  -> Tier 0 view-count filter
  -> parallel Tier 1 metadata ranker
  -> high-model final selector
  -> markdown audit artifact
  -> focused eval loop
  -> remaining Tier 1 boundary calibration
```

Raven is currently a source-discovery and judgment loop, not a content-ingestion system yet.

## Timeline

| Date | What changed | Meaning |
|---|---|---|
| 2026-04-15 | Repo reset into `src/backend/` and `src/frontend/` shell after deleting premature CLI/rubric/crawler code. | Raven was deliberately kept empty until the backend/frontend boundary and first contract were clear. |
| 2026-04-19 | Active backend moved through SQLite foundation, YouTube search smoke, venv repair, and API/search reference demotion. | Generated full-pipeline code was parked as reference; active Raven stayed Duc-owned. |
| 2026-04-20 | Editor stack was stabilized; one-node `gpt-5.4-mini` query enricher passed its production gate; Reddit code was kept reference-only; VTuber scanner stayed separate from Raven. | The first AI seam became real, but platform expansion stayed gated. |
| 2026-04-21 | Raven got the architecture branch: vault-keeper harness note, D2/Canvas method, live feature-web canvas, and Tier 1 ranker draft direction. | The system shape moved out of chat and into visual/vault memory. |
| 2026-04-22 | Tier 1 prompt/eval contract was simplified into metadata-only judgment, minimal audit markdown, and focused eval iteration. | The ranker stopped pretending numeric precision mattered; it became a taste filter. |
| 2026-04-24 | YouTube `search.list -> videos.list` enrichment, ID-keyed merge, SQLite query/API/candidate logging, duplicate-ignore behavior, and bridge smoke passed. | Search stopped being a loose adapter and became a persisted workbench seam. |
| 2026-04-25 | Raven vault routing was renovated into context, architecture, prompt, evaluation, workflow, and source/evidence branches with Growth Contracts. | Future agents no longer need to scrape root context to understand Raven. |
| 2026-04-26 | Tier 1 ranker/final-selector work accelerated: medium+long YouTube merge, live audits, prompt budget gate, focused eval loop, final selector, and LangGraph fan-out direction. | The project became an eval-driven ranking loop instead of only a search prototype. |
| 2026-04-27 | Final selector adopted `published_at` and `view_count`; run `6` for YouTube growth produced 254 candidates; focused eval bootstraps and `key_words` gate were added. | Raven now has realistic noise pressure and a concrete calibration target. |
| 2026-04-29 | Duc OS became the root router; this map was created to compress Raven's past before future planning. | The operating layer is now stable enough to discuss Raven's next direction cleanly. |

## Built Assets

### Repo

```text
src/backend/Raven_graph.py
  -> graph order, enricher, YouTube search, Tier 1 fan-out, final selector

src/backend/search/youtube_search.py
  -> YouTube search.list medium+long discovery and videos.list enrichment

src/backend/data/search_base.py
  -> search result packing, query/API/candidate logging bridge

src/backend/data/rank_base.py
  -> candidate readback and ranking persistence boundary

src/backend/db.py
  -> SQLite run/query/API/candidate/ranking/final-decision foundation

src/backend/data/prompt/
  -> enricher, Tier 1 ranker, Tier 1 final selector prompts

eval/
  -> eval runners, JSONL gates, trace threads, focused live audit evidence
```

### Vault

```text
projects/raven/README
  -> project router

raven-context-hub / raven-current-context / raven-progress-map
  -> state and past map

raven-architecture-hub / raven-feature-web.canvas
  -> system shape and planning board

raven-evaluation-hub / raven-tier-1-ranker-evaluation / raven-evaluation-insights
  -> eval workflow, reports, and compounding lessons

raven-prompt-hub
  -> prompt contract route

raven-workflow-hub
  -> ownership, delegation, draft, and repo-vault rules

projects/raven/sources/README
  -> evidence lane without first-loading raw material
```

## Current State

Implemented and smoke/eval-backed:

- One-node query enricher using `gpt-5.4-mini`.
- Prompt-owned `key_words` output for title relevance filtering.
- YouTube medium+long `search.list` discovery.
- `videos.list` metadata enrichment with ID-keyed merge.
- SQLite run, query, API, candidate, Tier 1, and final-decision persistence.
- Tier 0 view-count filtering.
- Tier 1 metadata ranker with audit artifacts and focused eval loop.
- High-model Tier 1 final selector using `published_at` and `view_count` as pressure signals.

Known green checks:

- Enricher baseline gate: `5/5` after the latest keyword/output calibration.
- Focused YouTube-growth enricher gate: `1/1`.
- Tier 1 synthetic gate: `8/8`.
- Tier 1 final synthetic gate: `1/1`.
- Tier 1 final focused YouTube-growth bootstrap: `1/1`.

Known weak edge:

- Focused Tier 1 YouTube-growth eval remains `15/17`.
- The unresolved taste boundary is named-tool/channel-clone leverage versus broad beginner-mistake metadata.
- Broad misconception-style query expansion can recreate noisy candidate pools if not watched.

## Not Active

These are not the next move unless Duc explicitly changes the lane:

- Reddit implementation in `src/backend/search/reddit_search.py`.
- Crawlers, transcript ingestion, comments ingestion, or full third-party content storage.
- Transcript-derived Tier 2 source cards.
- Public synthesis/distribution output.
- Frontend product surface.

## Hygiene Flags

- Root `test/` still violates the Raven backend test-folder rule; backend tests belong under `src/backend/test/`.
- Repo `AGENTS.md` is modified in the working tree as of this map session; treat it as existing user/session state, not an implementation change to revert casually.
- Eval evidence is dense under `/home/r1ceg/Raven/eval/`; do not promote raw traces into durable vault prose unless a report needs a pointer.

## Next Already Recorded

The vault already has a near-term next move:

```text
finish Tier 1 boundary calibration
  -> named-tool / channel-clone leverage should probably survive
  -> broad beginner-mistake metadata should stay weak
  -> rerun focused eval
  -> update prompt/eval notes only after evidence changes
```

This is the current implementation next, not the full future strategy.

## Future Discussion Queue

After the past is accepted, the next conversation should choose one lane:

```text
A. Finish Tier 1 calibration
   -> make current ranker less stupid before adding more surface area

B. Define first product output
   -> what a kept source becomes for Duc: list, audit packet, vault card, or public synthesis seed

C. Add title keyword gate
   -> use enricher `key_words` as cheap pre-rank noise control

D. Clean repo hygiene
   -> fix root test-folder violation before more backend growth

E. Design vault-keeper promotion path
   -> SQLite candidate -> judgment -> promoted vault memory -> retrieval packet
```

The honest order is probably A before B/C/E. D is cheap hygiene if it blocks confidence.

## Source Trail

- [[sources/log/days/2026-04-15]]
- [[sources/log/days/2026-04-19]]
- [[sources/log/days/2026-04-20]]
- [[sources/log/days/2026-04-21]]
- [[sources/log/days/2026-04-22]]
- [[sources/log/days/2026-04-24]]
- [[sources/log/days/2026-04-25]]
- [[sources/log/days/2026-04-26]]
- [[sources/log/days/2026-04-27]]
- [[sources/log/days/2026-04-29]]
- Repo dev log: `/home/r1ceg/Raven/logs/DEV_LOG.md`

## Related

- [[projects/raven/notes/raven-context-hub]]
- [[projects/raven/notes/raven-current-context]]
- [[projects/raven/notes/raven-architecture-hub]]
- [[projects/raven/notes/raven-evaluation-hub]]
- [[projects/raven/notes/raven-prompt-hub]]
- [[projects/raven/notes/raven-workflow-hub]]

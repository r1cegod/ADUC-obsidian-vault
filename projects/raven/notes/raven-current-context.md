---
type: note
title: Raven Current Context
created: '2026-04-25'
updated: '2026-05-12'
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
> **TL;DR**: Raven is now a Codex-native source-acquisition/evidence-preparation tool. Current runtime starts from a rich `request`, generates search `queries`, uses Tier 1 as a wide binary relatedness gate, and lets final assign priority labels.

## Growth Contract
- Parent branch: [[projects/raven/notes/raven-context-hub]]
- Node role: leaf
- First parent link: [[projects/raven/notes/raven-context-hub]]
- Growth trigger: split a topic out when it becomes durable architecture, evaluation, prompt, or workflow knowledge instead of live project state.
- Forbidden contents: stable architecture contracts, raw eval evidence, prompt contracts, old run dumps, and project-root routing.
- Source/evidence boundary: this page summarizes current state and points outward; exact repo evidence stays in the repo or Raven source lane.

## Live Repo

```text
/home/r1ceg/Raven
```

Backend commands use:

```text
./.venv/bin/python
```

## Strategic Boundary

Read [[projects/raven/notes/raven-codex-native-pivot]] before expanding Raven architecture.

```text
Codex + Duc OS
  -> general reasoning, synthesis, planning, editing, operating loop

Raven
  -> hard-source discovery
  -> metadata filtering
  -> transcript/source fetch
  -> source cards / Wave Reports
  -> audit evidence for Codex
```

Raven should not become a custom general agent OS.

## Current Runtime Contract

```text
rich request
  -> enricher
      -> generated search queries
      -> key_words for cheap title filtering
  -> YouTube search
      -> search.list + videos.list enrichment
      -> DB query/API/candidate logs
  -> ranker_tier1
      -> binary request-relatedness gate
      -> writes final_decision = keep | throw_out
  -> ranker_tier1_final
      -> high-model metadata labeler
      -> reads Tier 1 keep survivors
      -> writes sexy_label = maybe | click | must_click
  -> Tier 2 source packet lane
```

Important naming boundary:

```text
request
  -> user intent object / graph input / raven_runs.request

queries
  -> generated search strings / raven_queries.query
```

There is no original `query` or `target` input compatibility path now.

## Current Backend Seams

```text
raven_graph.py
  -> request-driven graph entrypoint

src/backend/youtube_ranker_tier1.py
  -> enricher node
  -> YouTube search node wrapper
  -> Tier 1 fan-out via LangGraph Send
  -> Tier 1 final join node

src/backend/db.py
  -> clean request-era schema
  -> create_run(db, request)
  -> candidates_rank(... final_decision, reasoning)
  -> candidates_final_label(... sexy_label, final_reason)

src/backend/search/youtube_search.py
  -> YouTube search.list with publishedAfter and relevanceLanguage
  -> videos.list enrichment
  -> title keyword + recency + view filters

src/backend/observability/
  -> focused dataset evals
  -> full graph packets
  -> DB readbacks
```

No DB migration helper is present; the local SQLite DB was wiped during the request-contract swap and now recreates cleanly.

## Verified Status

Latest clean request-era verification on 2026-05-02:

```text
py_compile
  -> passed

unit tests
  -> 8/8 passed

focused evals
  -> enricher request: 1/1
  -> ranker_tier1 request gate: 4/4
  -> ranker_tier1_final labels: 1/1
  -> Tier 1 prompt: 263/500 tokens

clean-DB full request run
  -> run: 1
  -> packet: eval/packets/02-May-2026/17:48:58_raven_full_i-am-trying-to-understand-the-current-operating
  -> generated queries: 4
  -> candidates: 71
  -> Tier 1: keep 36 / throw_out 35
  -> final labels: must_click 4 / click 15 / maybe 17 / unlabeled 35
```

Latest daily eval on 2026-05-03:

```text
run: 2
request: how to grow a youtube channel
packet: eval/packets/03-May-2026/08:07:40_raven_full_how-to-grow-a-youtube-channel
queries: 3
candidates: 11
Tier 1: keep 9 / throw_out 2
final labels: must_click 2 / click 3 / maybe 4 / unlabeled 2
Phase 2 baselines: request-era suites green
search diagnostic: low packet candidate count is mainly DB writeback uniqueness, not YouTube API scarcity
patch verification: run-local uniqueness works on fresh DB; temp full graph produced 56 candidates for `how to grow a youtube channel`
default DB: recreated cleanly on 2026-05-03 with 0 runs and patched `UNIQUE(run_id, source, platform_id)` schema
pytest: installed in `.venv`, added to `requirements-dev.txt`, backend tests 8/8 passed
current blocker: live YouTube full-graph rerun hit `HTTP Error 403: Forbidden`; resolve API/auth/quota before trusting another live daily packet
```

## Current Project Direction

Tier 1 is now a recall-preserving trash filter. It should only remove clearly unrelated videos. Final owns priority judgment.

Tier 2 is the active locked build lane as of 2026-05-12 via [[duc-os/kickstart]] and [[projects/raven/notes/raven-tier-2-source-packet-contract]]:

```text
kept/labeled source
  -> transcript_fetcher
  -> card_maker source card
  -> wave_reader Wave Report
```

The previous agent-created `src/backend/tier2/transcript_fetcher.py`, `src/backend/test/test_transcript_fetcher.py`, and `youtube-transcript-api` dependency were removed on 2026-05-03 at Duc's request; backend tests returned to 8/8. New Tier 2 work starts cleanly from Duc-owned implementation, not resurrection of that patch.

Tier 2 has an auditable execution proposal at [[projects/raven/notes/raven-tier-2-execution-proposal]]. The proposal uses the completed Daniel Priestley ingest as proof that the workflow is viable. Repo mutation is now opened only for Raven Ranker Tier 2 Source Packet Build: YouTube transcript acquisition, source-card creation, wave-reader synthesis, fixtures, tests, observability, and docs.

Tier 2 corrected shape: two evidence-production nodes, `transcript_fetcher` and `card_maker`, plus one Raven graph node, `wave_reader`, that reads all source cards for a run/topic into an Obsidian-linked Wave Report. Duc may freestyle architecture while building; agent help defaults to Learn/BUILD/AUDIT mode: raw mechanism blocks, critical-mistake interrupts, audits, fixtures, tests, observability, docs, and maintenance unless Duc explicitly delegates a bounded patch.

Daniel Priestley ingest result: 402 uploads accounted for, 378 shorts excluded by policy, 24 long-form transcript attempts, 23 transcripts fetched, 23 source cards created, and one general synthesis created at [[wiki/synthesis/daniel-priestley-distribution-system]]. The installed `watch` skill worked as a spot-review/visual-sampling tool, not the mass channel-ingest backbone. If the ingest becomes a Duc operating system, promote it through [[projects/raven/notes/raven-distribution-system-ingest-structure]] before any Duc OS adoption.

Reddit implementation is still not active.

## Current Evaluation Route

```text
projects/raven/README
  -> [[projects/raven/notes/raven-evaluation-hub]]
  -> [[projects/raven/notes/raven-evaluation-domain]]
  -> [[projects/raven/notes/raven-eval-how-to-use]]
```

Raven eval reports and production-readiness decisions are vault-canonical. Repo `eval/` is executable evidence only.

## Hygiene Flags

- Root `test/` in the Raven repo still violates the backend test-folder rule.
- Active `src/backend/search/reddit_search.py` is still empty; reference-only Reddit code is parked under `docs/reference/`.

## Related

- [[projects/raven/notes/raven-context-hub]]
- [[projects/raven/README]]
- [[projects/raven/notes/raven-codex-native-pivot]]
- [[projects/raven/notes/raven-tier-2-source-packet-contract]]
- [[projects/raven/notes/raven-architecture-hub]]
- [[projects/raven/notes/raven-evaluation-hub]]
- [[context/hot]]

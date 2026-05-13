---
type: note
title: Raven Daily Eval 2026-05-03
created: '2026-05-03'
updated: '2026-05-03'
tags:
  - project/raven
  - evaluation
  - daily-eval
status: active
lang: en
feeds_into:
  - projects/raven/notes/raven-evaluation-hub.md
  - projects/raven/notes/raven-evaluation-insights.md
---
> **TL;DR**: Daily Phase 1 run on 2026-05-03 passed as run `2`; Duc gave light approval for Phase 2. Request-era baselines passed, old YouTube-growth datasets exposed eval drift, YouTube-search diagnostic found global DB uniqueness hiding reusable videos, Duc's run-local uniqueness patch verified, default `raven.sqlite` was recreated cleanly, and pytest was installed. Live full-graph rerun is currently blocked by YouTube API 403.

## Growth Contract
- Parent branch: [[projects/raven/notes/raven-evaluation-hub]]
- Node role: report leaf
- First parent link: [[projects/raven/notes/raven-evaluation-hub]]
- Growth trigger: update only if this daily run receives Duc audit lines, creates focused dataset changes, or changes production-readiness judgment.
- Forbidden contents: raw trace dumps, full candidate JSON, runner code, and third-party content bodies.
- Source/evidence boundary: executable evidence remains in `/home/r1ceg/Raven/eval/packets/`; this note stores the human-readable judgment layer.

## Phase 1 Run

```text
target: how to grow a youtube channel
kind: full graph
status: passed / needs review
run_id: 2
thread: be59f774-93da-457d-9bec-b6ca5e198a93
packet: eval/packets/03-May-2026/08:07:40_raven_full_how-to-grow-a-youtube-channel
started Vietnam: 08:07:17, 03 May 2026
finished Vietnam: 08:07:40, 03 May 2026
```

Command actually used after discovering the workflow doc was stale:

```bash
./.venv/bin/python eval/run_observation.py full --graph raven --request "how to grow a youtube channel"
```

## Result

```text
queries: 3
candidates: 11
YouTube filter: 300 raw hits -> 300 unique videos -> 11 candidates, 289 filtered out
Tier 1 labels: keep 9 / throw_out 2
Final selector packet input count: 9
Final labels: must_click 2 / click 3 / maybe 4 / unlabeled 2
```

Enricher output:

```text
youtube channel growth strategy
grow youtube channel audience
youtube channel growth mistakes
key_words: youtube, channel, growth, audience
```

Candidate distribution:

```text
youtube channel growth strategy -> 0 candidates
grow youtube channel audience -> 9 candidates
youtube channel growth mistakes -> 2 candidates
```

## Current Judgment

This is a valid Phase 1 packet, not a completed two-phase eval. Compared with the 2026-05-02 daily eval, Tier 1 no longer skipped the entire pool: it kept 9 of 11 and the final selector received a meaningful survivor set.

The search stage is still visibly narrow. One generated query produced zero candidates, and the whole run came from two query lanes after heavy filtering. That is not a patch trigger by itself; it is an audit target.

## Phase Boundary

```text
Phase 1: complete
Phase 2: approved lightly by Duc and run on existing focused/baseline eval artifacts
Prompt/code/dataset patching: still blocked until the diagnostic route is chosen
```

Duc's audit signal was that the packet works pretty well with slight audit needed. That is enough for focused checks, not enough to patch prompt or dataset blindly.

## Phase 2 Focused Eval

Current request-era baseline suites passed:

```text
enricher_request_cases: 1/1 passed
ranker_tier1_request_cases: 4/4 passed, prompt 263/500 tokens
ranker_tier1_final_request_cases: 1/1 passed
```

Older YouTube-growth focused datasets are stale or stricter than the current contract:

```text
enricher_youtube_growth_regression: 0/1
  failed: key_words_from_request, required_terms_per_query_present, operational_specificity_ok
  interpretation: the eval expects every query to include `youtube channel` and contain operational markers, while the current enricher emits short search phrases.

ranker_tier1_youtube_growth_audited: error before cases
  failed: dataset rows lack required `request` field after the request-era contract swap.

ranker_tier1_final_youtube_growth_bootstrap: 0/1
  failed only expected-label match; structure, IDs, labels, reasons, and control-leak checks passed.
  model labeled deletion-risk candidate `maybe` where old expected labels required `click` or `must_click`.
```

Phase 2 judgment: current runtime contracts are green; old focused YouTube-growth datasets need migration before they can be used as authority.

## YouTube Search Diagnostic

Diagnostic command called the same YouTube API/filter path for current and alternative queries. The API itself returned full 100-result pools per query. Current filter means: medium/long videos, last 365 days, at least 40k views, and title contains one of `youtube/channel/growth/audience`.

```text
current queries, current-pass candidates from live API:
youtube channel growth strategy -> 44-46
grow youtube channel audience -> 17-18
youtube channel growth mistakes -> 8-10
```

But run `2` packet showed:

```text
youtube channel growth strategy -> 0 candidates
grow youtube channel audience -> 9 candidates
youtube channel growth mistakes -> 2 candidates
```

Root cause:

```text
raven_candidates has UNIQUE(source, platform_id) and link UNIQUE
  -> earlier run `1` stored the same videos
  -> run `2` silently ignored duplicates through INSERT OR IGNORE
  -> later daily evals undercount reusable search results
  -> search looks scarce even when YouTube returned many valid candidates
```

DB duplicate check confirmed all current filter-passing IDs for the three daily queries were already present after prior runs; the zero-candidate strategy lane was caused by writeback uniqueness, not by YouTube scarcity.

Useful query alternatives from the same diagnostic:

```text
small youtube channel growth -> 24 current-pass candidates
youtube channel mistakes -> 20 current-pass candidates
youtube growth case study -> 14 current-pass candidates
youtube creator strategy -> 11 current-pass candidates
youtube channel audit -> 1 current-pass candidate
youtube channel upload experiment -> 1 current-pass candidate with title-only keyword filter, 7 with title-or-description keyword filter
```

## Patch Verification

Duc patched `src/backend/db.py` to remove global link uniqueness and change candidate identity to run-local uniqueness:

```text
old: link TEXT NOT NULL UNIQUE + UNIQUE(source, platform_id)
new: link TEXT NOT NULL + UNIQUE(run_id, source, platform_id)
```

Verification results:

```text
fresh temp DB duplicate test: passed
  same video in run 1 -> candidate id 1
  same video in run 2 -> candidate id 2
  same video repeated inside run 2 -> ignored

py_compile: passed for db, graph, ranker, search_base, and observation runner
request-era evals:
  enricher_request_cases -> 1/1 passed
  ranker_tier1_request_cases -> 4/4 passed
  ranker_tier1_final_request_cases -> 1/1 passed

full graph on monkeypatched fresh temp DB:
  request: how to grow a youtube channel
  queries: 2
  candidates: 56
  candidate_counts:
    youtube channel growth strategy -> 46
    grow youtube channel audience -> 10
  Tier 1: keep 54 / throw_out 2
  Final: must_click 12 / click 29 / maybe 13 / unlabeled 2
```

DB recreation and pytest install:

```text
pytest installed in `.venv`: 9.0.3
requirements-dev.txt now includes pytest
backend tests: 8/8 passed via `./.venv/bin/python -m pytest src/backend/test`
old default DB backup moved outside repo: /tmp/raven.sqlite.bak.20260503T023920Z
new default DB: src/backend/data/raven.sqlite
new DB run count after final recreate: 0
new raven_candidates schema:
  link TEXT NOT NULL
  UNIQUE(run_id, source, platform_id)
```

Normal full-graph verification after DB recreation was attempted, but YouTube API returned `HTTP Error 403: Forbidden` for search calls. The failed verification attempts wrote empty runs, so the DB was recreated one final time and left clean. This is now an external YouTube API/auth/quota blocker, not the old DB uniqueness issue.

## Best Route

Best next route is schema/writeback first, prompt second.

```text
1. Fix candidate identity semantics
   -> candidate identity should be per run, not globally unique forever
   -> replace global `UNIQUE(source, platform_id)` / `link UNIQUE` behavior with per-run dedupe such as `UNIQUE(run_id, source, platform_id)`
   -> preserve cross-run history through a later source table if needed, not by suppressing run-local candidates

2. Make eval runs isolated or explicit
   -> daily eval should use a clean eval DB or a run-local candidate snapshot
   -> `--db-path` currently affects readback only; graph creation still uses default `src/backend/data/raven.sqlite`
   -> fix this before trusting daily candidate counts as comparable over time

3. Then tune search
   -> keep title keyword filter for first pass, but test title-or-description keyword fallback for narrow query lanes
   -> prefer query families that produced volume: `small youtube channel growth`, `youtube channel mistakes`, `youtube growth case study`
   -> avoid treating `youtube channel audit` and `upload experiment` as broad discovery queries unless description fallback is enabled
```

## Audit Pointers

Primary files for Duc audit:

```text
eval/packets/03-May-2026/08:07:40_raven_full_how-to-grow-a-youtube-channel/04_ranker_tier1.md
eval/packets/03-May-2026/08:07:40_raven_full_how-to-grow-a-youtube-channel/05_ranker_tier1_final.md
```

High-priority audit targets:

```text
must_click:
- The RIGHT Way to Upload Shorts in 2026 (For Fast Growth)
- I Went Live on a New Channel Until I Had 100 Viewers

possible false-positive keeps:
- If I Wanted To Grow An Audience In 2026, I'd Do This
- I Rated My Viewers YouTube Channels
- 10 Golf YouTube Channels Losing Viewers!
- BEST OPPORTUNITY: 9 VIRAL FACELESS YOUTUBE CHANNEL IDEAS IN 2025
- Gaming Channel Growth 2026: The Secret to Getting 100,000 Subscribers on YouTube!
- How to Get YouTube Monetization (Complete Guide)
```

## Related

- [[projects/raven/notes/raven-evaluation-hub]]
- [[projects/raven/notes/raven-eval-how-to-use]]
- [[projects/raven/notes/raven-evaluation-insights]]
- [[projects/raven/notes/raven-tier-1-ranker-evaluation]]

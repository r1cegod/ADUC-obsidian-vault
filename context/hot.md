---
type: context
title: Session Hot Cache
created: 2026-04-12T00:00:00.000Z
updated: '2026-04-22'
tags:
  - context
  - session
status: active
lang: en
feeds_into: []
---

> **TL;DR**: Session-continuity cache. Read this before [[briefing.md]]. Use it only for live continuity, stable-router skip status, and the next likely move.

## How To Use

1. Read this first.
2. Skip repair pass on pages listed under `Stable Since Last Session` unless you edit them now.
3. Update only when continuity, stable-router status, or next action changed.

## Current Continuity

### Raven
- Active repo: `/home/r1ceg/Raven`
- Use repo venv for backend commands: `./.venv/bin/python`
- Live backend seams:
  - SQLite foundation in `src/backend/db.py`
  - YouTube `search.list` + first normalization pass in `src/backend/search/youtube_search.py`
  - one-node `gpt-5.4-mini` enricher seam in `src/backend/Raven_graph.py`
- Live architecture route: [[projects/raven/notes/raven-architecture-hub]] -> `projects/raven/notes/raven-feature-web.canvas`
- Current architecture lane: Canvas-first drafting with official markdown routing for stabilized decisions
- Current active architecture threads:
  - [[projects/raven/notes/raven-vault-keeper-harness-architecture]]
  - [[projects/raven/notes/raven-source-ranker-draft]]
- Next build seam: enriched query -> YouTube search -> SQLite write/readback, then Tier 1 ranker/eval loop
- Reddit status: reference-only artifact exists at `docs/reference/reddit_search_clean.py`; active `src/backend/search/reddit_search.py` is still empty
- Evaluation docs rule: Raven eval reports and production-readiness decisions are vault-canonical under [[projects/raven/notes/raven-evaluation-domain]]
- Hygiene flag: root `test/` still violates Raven backend test-folder rule

### Learning Defaults
- Build-First remains primary for compounding technical skill
- `check` / `audit` / `clean` on active learning artifacts default to `AUDIT`
- `PATCH` needs explicit patch/delegation permission unless the task is clear ONE_TIME_UTILITY
- `VIBE_DOCING` uses neutral placeholders only

## Stable Since Last Session

- `briefing.md`
- `context/now.md`
- `projects/pathfinder/README.md`
- `projects/pathfinder/notes/pathfinder-evaluation-hub.md`
- `projects/pathfinder/notes/pathfinder-workflow-hub.md`

## Next Action

- Keep PathFinder reviewable unless a real blocker appears.
- Continue Raven through the query-enricher -> search -> SQLite seam.
- Use the new routing stack:

```text
briefing
  -> operations-hub / vault-keeping / learning-protocol-hub / project README
  -> hub if needed
  -> leaf
```

## Flagged For This Session

- PathFinder broader University comparison loop is still open if that project becomes active again.

---
type: context
title: Session Hot Cache
created: 2026-04-12T00:00:00.000Z
updated: '2026-04-27'
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

### PathFinder
- Status: reviewable/portfolio-ready unless a concrete blocker threatens demo or review confidence
- Live PathFinder route: [[projects/pathfinder/notes/pathfinder-context-hub]] -> [[projects/pathfinder/notes/docs-current-context]]
- Root-context cleanup status: PathFinder-specific hardening detail has been moved out of [[context/now]] into the project branch

### Raven
- Active repo: `/home/r1ceg/Raven`
- Use repo venv for backend commands: `./.venv/bin/python`
- Live Raven state route: [[projects/raven/notes/raven-context-hub]] -> [[projects/raven/notes/raven-current-context]]
- Live architecture route: [[projects/raven/notes/raven-architecture-hub]] -> `projects/raven/notes/raven-feature-web.canvas`
- Current architecture lane: Canvas-first drafting with official markdown routing for stabilized decisions
- Current active architecture threads:
  - [[projects/raven/notes/raven-vault-keeper-harness-architecture]]
  - [[projects/raven/notes/raven-source-ranker-draft]]
- Raven canvas status: `projects/raven/notes/raven-feature-web.canvas` now reflects the current live graph: `create_run -> enricher -> youtube_search -> Send(ranker_tier1) -> ranker_tier1_final`, plus medium/long YouTube search, videos enrichment, Tier 0 view filter, candidate ranking fields, model-key split, and final keep/throw_out writeback.
- Raven Tier 1 ranker status: runtime uses LangGraph `Send` parallel candidate scoring followed by `ranker_tier1_final`, a one-shot high-model selector over readable appended `PACKET` / `<candidate>` blocks. Enricher, Tier 1, and final ranker are currently set to temperature `0.7`. Tier 1 prompt is budget-gated under 1000 tokens and currently measures 875 tokens. Synthetic checks pass: Tier 1 8/8 and Tier 1 final 1/1; latest final synthetic metadata-packet check passed 1/1 at thread `e038b7ac-3441-4135-bbe1-31daf3cdc8bf`. Live query `how to find leads` run `5` produced the focused audited Tier 1 dataset `eval/ranker_tier1_how_to_find_leads_audited.jsonl`. Fresh live query `how to grow a youtube channel` run `6` produced 254 candidates, final counts `{'keep': 8, 'throw_out': 246}`, and focused audit seed `eval/live/run_0006_how-to-grow-a-youtube-channel-live-gate/ranker_tier1_audit.md`. Focused bootstrap evals now exist locally for enricher, Tier 1, and Tier 1 final. After calibration, enricher focused regression passed `1/1`, Tier 1 final focused bootstrap passed `1/1`, baseline gates passed enricher `5/5`, Tier 1 synthetic `8/8`, and final synthetic `1/1`; Tier 1 focused YouTube-growth eval remains `15/17`, with NotebookLM channel-clone and broad beginner-mistake boundaries still not stable. Enricher now returns prompt-owned `key_words` for future title relevance filtering; latest keyword gates passed baseline `5/5` and focused YouTube-growth `1/1` on 2026-04-27. Tier 1 final now receives `published_at` and `view_count` as decision signals; treat them as freshness/traction pressure, not quality proof.
- Raven YouTube smoke status: `src/backend/search/youtube_search.py` import blocker was fixed by Duc; direct YouTube API smoke and SQLite search/writeback bridge smoke passed on 2026-04-24.
- Reddit status: reference-only artifact exists at `docs/reference/reddit_search_clean.py`; active `src/backend/search/reddit_search.py` is still empty
- Evaluation docs rule: Raven eval reports and production-readiness decisions route through [[projects/raven/notes/raven-evaluation-hub]]; boundary leaf is [[projects/raven/notes/raven-evaluation-domain]]; reusable evaluation and production-prompt method routes through [[wiki/synthesis/evaluation-production-prompt-domain]]
- Hygiene flag: root `test/` still violates Raven backend test-folder rule

### Wynncraft Assistant
- Status: low-priority leisure-control project created 2026-04-26
- Live route: [[projects/wynncraft/README]] -> [[projects/wynncraft/notes/wynncraft]]
- Source lane: [[projects/wynncraft/sources/README]]; local seed doc remains `/home/r1ceg/wynncraft.md`
- Default rule: assistant researches and compresses builds/source checks; Duc plays bounded sessions.

### Vault Architecture
- Branching rules: [[wiki/synthesis/vault-target-tree-architecture]]
- Branch creation operation: [[wiki/operations/branch-growth-operation]]
- New durable entry rule: include a Growth Contract so every new node declares parent branch, role, first parent link, growth trigger, forbidden contents, and source/child boundary when relevant
- Renovation status: global Branch Growth guardrail and Raven proof branches are active; Raven route now starts from [[projects/raven/README]] -> context / architecture / prompt / evaluation / workflow / sources. PathFinder root-context residue has been compressed into its project context branch.

### Development Defaults
- Technical help, implementation guidance, debugging, and code delegation now route through [[development]]. Delegation now has an explicit explain-before-code rule: if Duc cannot explain the approach in detail, Codex must audit/explain before writing code; docs/mechanism requests default to VIBE_DOC and do not imply repo patch permission.
- Mandatory order: [[wiki/operations/detect-operation]] first, then [[wiki/operations/learn-operation]] or [[wiki/operations/delegate-operation]].
- Learn is the user-facing manual that absorbs Help Protocol, Build-First, Pre-Wire, and Vibe Docing; Duc no longer needs to name Vibe Docing for narrow mechanism help.
- Delegate copies Duc's visible pattern and must not invent new features, functions, abstractions, dependencies, or sanitizers unless necessary and justified.
- `check` / `audit` / `clean` on active learning artifacts default to Learn/AUDIT.
- `PATCH` needs explicit patch/delegation permission unless the task is clear ONE_TIME_UTILITY.
- Vibe Docing uses neutral placeholders only.

## Stable Since Last Session

- `briefing.md`
- `context/now.md`
- `projects/pathfinder/README.md`
- `projects/pathfinder/notes/pathfinder-evaluation-hub.md`
- `projects/pathfinder/notes/pathfinder-workflow-hub.md`

## Next Action

- If vault architecture remains the task, run the readiness audit against the full vault tree: remaining risks are global index dependence, mixed old source-summary conventions, and project README/router drift outside Raven.
- Keep PathFinder reviewable unless a real blocker appears.
- Continue Raven from the passed YouTube search/videos enrichment -> SQLite logging/writeback smoke, then move toward the Tier 1 ranker/eval loop.
- Use the new routing stack:

```text
briefing
  -> development / operations-hub / vault-keeping / project README
  -> branch hub if needed
  -> leaf
```

## Flagged For This Session

- PathFinder broader University comparison loop is still open if that project becomes active again.

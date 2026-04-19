---
type: context
title: Session Hot Cache
created: 2026-04-12T00:00:00.000Z
updated: '2026-04-19'
tags:
  - context
  - session
status: active
lang: en
feeds_into: []
---

> **TL;DR**: Session-continuity cache. Read this BEFORE briefing.md. Stable routers listed here skip their repair pass. Delta-update only when continuity, stable-router status, or next action changed.

## How To Use

1. **Read first** - before briefing.md, before context/now.md.
2. Files listed under "Stable Since Last Session" were verified clean and not edited. Skip their repair pass.
3. Files listed under "Flagged For This Session" need attention before starting work.
4. At end of a task: update only the sections whose continuity, stable-router status, or next action changed.

## Current Raven Continuity

- Active repo: `/home/r1ceg/Raven`.
- Use repo venv for backend commands: `./.venv/bin/python`, not system `python3`.
- Current backend state: SQLite foundation in `src/backend/db.py`; YouTube `search.list` + first normalization pass in `src/backend/search/youtube_search.py` is live-smoke verified.
- Next Raven seam: commit one YouTube search result into SQLite, then read it back through the joined DB view.
- Hygiene flag: root `test/` currently exists but violates Raven's backend test folder rule; do not bless root-level tests.

## Stable Since Last Session

> Files verified clean this session. Agent may skip repair pass on these.

- `briefing.md` - verified 2026-04-13, Active Projects current.
- `context/now.md` - verified 2026-04-13, updated with university-finding eval and vault-only evaluation-domain rule.
- `projects/pathfinder/README.md` - verified 2026-04-13, routes evaluation-domain ownership.
- `projects/pathfinder/notes/pathfinder-evaluation-hub.md` - verified 2026-04-13, routes the evaluation-domain index.
- `projects/pathfinder/notes/pathfinder-workflow-hub.md` - verified 2026-04-13, routes the sync/evaluation boundary.

## Last Session Summary

- **Date:** 2026-04-15
- **Files changed:**
  - WSL: `/home/r1ceg/Path_finder_wsl` clean working copy created and validated.
  - WSL: `/home/r1ceg/.zprofile` and `/home/r1ceg/.zshenv` updated with local binary paths.
  - WSL: `/home/r1ceg/.codex/AGENTS.md` and `/home/r1ceg/.codex/RTK.md` created by `rtk init -g --codex`.
  - Windows Codex MCP config: added `obsidian`.
  - WSL Codex MCP config: added `obsidian`.
  - `sources/log/days/2026-04-15.md`
  - `log.md`
  - `context/hot.md`
- **Open threads:**
  - Use `/home/r1ceg/Path_finder_wsl` as the clean WSL PathFinder repo. The earlier `/home/r1ceg/Path_finder` clone was dirtied by broad rsync and removed.
  - rtk v0.36.0 is installed in WSL and configured for WSL Codex global instructions.
  - Filesystem Obsidian MCP uses `@bitbonsai/mcpvault` and is configured for both Windows Codex and native WSL Codex.
  - Native WSL Codex CLI is installed under `/home/r1ceg/.npm-global/bin/codex`.
  - Focused WSL backend verification passed: output/University contract tests reported `15 passed, 4 subtests passed`.
  - Universal technical-help behavior now routes through [[wiki/learning-protocol-hub]] and [[wiki/help-protocol]] before docs/implementation guidance; full feature ownership uses [[wiki/pre-wire-protocol]].
  - [[projects/raven/README|Raven]] is scaffolded at `/home/r1ceg/Raven`; remote `main` was force-pushed from old CLI/rubric commit `94632ee` to clean scaffold commit `128ff88 Project initialized`. Working tree tracks `origin/main`; only `.env` and `.venv/` are ignored local files. Raven now has [[projects/raven/notes/raven-ownership-delegation-protocol|ownership-first delegation]]: delegate only work Duc can already write, explain, test, and repair.
  - Major stage user-like university-finding soft lock is fixed and live-verified through R5.
  - First University comparison replay seam is fixed at stage + compiler level: UEH stays conditional, weak FPT does not outrank UEH, and the response moves to RMIT.
  - Broader University RMIT/UEL comparison coverage and full frontend/browser continuation are not proven yet.
  - Evaluation docs and reports are now vault-only; repo `eval/` keeps executable evidence only.
  - Python contract/regression tests now belong under `backend/test/`; root-level `test_*.py` files are not allowed.
  - Vault write-back protocol is optimized: evidence-only reads do not require page-level repair, `log.md` sync happens only on new day or changed summary, and `context/hot.md` uses compact delta updates.
  - Default tool posture changed 2026-04-15: use `rtk` for shell/repo commands where practical and Obsidian MCP for vault reads/writes instead of raw filesystem access.
  - RTK is now available in non-login zsh command runners via `/home/r1ceg/.zshenv`, so plain `rtk ...` works from `/home/r1ceg/Path_finder_wsl`.
- **Next action:** treat PathFinder as reviewable unless a demo/review blocker appears; continue Raven through [[wiki/build-first-learning]] with `learning/sessions/raven-api-sqlite-ingest-wire-2026-04-16.md` as the active record. The product sequence remains Reddit/YouTube search function -> query enricher -> rater -> evolver placeholder, with vault as primary memory and SQLite as agent workbench. For mechanism gaps, use [[wiki/vibe-docing]] rather than full docs or spoonfeeding.

## Previous Session Summary

- **Date:** 2026-04-13
- **Files changed:**
  - `backend/data/prompts/output.py`
  - `backend/data/prompts/uni.py`
  - `backend/uni_graph.py`
  - `backend/test/test_uni_graph_contract.py`
  - `backend/test/test_output_prompt_contract.py`
  - `eval/uni_comparison_frontend_2026-04-13.jsonl`
  - `projects/pathfinder/sources/docs/evaluation/uni_evaluation.md`
  - `projects/pathfinder/notes/docs-uni-evaluation.md`
  - `projects/pathfinder/sources/docs/context/docs/CURRENT_CONTEXT.md`
  - `projects/pathfinder/notes/docs-current-context.md`
  - paired PathFinder dev logs and vault activity log
  - `SCHEMA.md`
  - `AGENTS.md`
  - `CLAUDE.md`
  - `vault-keeping.md`
  - `context/hot.md`
  - previous same-day context and routing pages remain as recorded earlier in this day file
- **Open threads:**
  - Major stage user-like university-finding soft lock is fixed and live-verified through R5.
  - First University comparison replay seam is fixed at stage + compiler level: UEH stays conditional, weak FPT does not outrank UEH, and the response moves to RMIT.
  - Broader University RMIT/UEL comparison coverage and full frontend/browser continuation are not proven yet.
  - Evaluation docs and reports are now vault-only; repo `eval/` keeps executable evidence only.
  - Python contract/regression tests now belong under `backend/test/`; root-level `test_*.py` files are not allowed.
  - Vault write-back protocol is optimized: evidence-only reads do not require page-level repair, `log.md` sync happens only on new day or changed summary, and `context/hot.md` uses compact delta updates.
- **Next action:** broaden University comparison/ranking replay to RMIT and UEL, or run a full frontend continuation if browser-level proof is needed.

## Flagged For This Session

> Issues that need attention at session start.

PathFinder University stage broader comparison loop: use `eval/uni_comparison_frontend_2026-04-13.jsonl` plus the R5-R7 frontend traces to extend coverage to RMIT and UEL.

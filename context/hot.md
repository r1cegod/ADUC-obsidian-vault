---
type: context
title: "Session Hot Cache"
created: 2026-04-12
updated: 2026-04-13
tags: [context, session]
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

## Stable Since Last Session

> Files verified clean this session. Agent may skip repair pass on these.

- `briefing.md` - verified 2026-04-13, Active Projects current.
- `context/now.md` - verified 2026-04-13, updated with university-finding eval and vault-only evaluation-domain rule.
- `projects/pathfinder/README.md` - verified 2026-04-13, routes evaluation-domain ownership.
- `projects/pathfinder/notes/pathfinder-evaluation-hub.md` - verified 2026-04-13, routes the evaluation-domain index.
- `projects/pathfinder/notes/pathfinder-workflow-hub.md` - verified 2026-04-13, routes the sync/evaluation boundary.

## Last Session Summary

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

## Previous Session Summary

- **Date:** 2026-04-12
- **Files changed:**
  - `vault_architecture.md` (created - full vault system map)
  - `vault_propagation.md` (created - propagation system doc)
  - `context/hot.md` (created - this file)
  - `scripts/check_propagation.py` (created - PostToolUse hook script)
  - `SCHEMA.md` (sync matrix section added)
  - `CLAUDE.md` (hot cache + propagation rules added)
  - `AGENTS.md` (hot cache rule added)
  - `context/now.md`, `context/me.md`, `context/goals.md` (feeds_into: added)
  - `projects/pathfinder/README.md`, `projects/ielts-writing/README.md` (feeds_into: added)
  - all 6 PathFinder hub notes (feeds_into: added)
  - `sources/log/days/2026-04-12.md` (WIRE log entry added)
- **Open threads:**
  - Uncertainty attack full chat run still paused - pre-chat bugs fixed, full run not done.
  - Orchestrator eval not started - next major PathFinder eval task.
  - IELTS Writing daily practice sessions not yet running (protocol started 2026-04-09).
- **Next action:** orchestrator replay through the full path, or continue uncertainty attack chat.

## Flagged For This Session

> Issues that need attention at session start.

PathFinder University stage broader comparison loop: use `eval/uni_comparison_frontend_2026-04-13.jsonl` plus the R5-R7 frontend traces to extend coverage to RMIT and UEL.

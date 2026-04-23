---
type: context
title: Current Focus
created: 2026-04-06T00:00:00.000Z
updated: '2026-04-21'
tags:
  - context
status: active
lang: en
feeds_into:
  - briefing.md
---

> **TL;DR**: PathFinder is being treated as reviewable/portfolio-ready unless a specific blocker appears. Current strategic focus is choosing the next high-leverage project: a reusable AI-agent scaffold that proves Duc's specialty in stateful, evaluable agent systems and supports inbound distribution.

## Active Decisions
- Universal technical-help behavior now routes through [[wiki/learning-protocol-hub]]: use [[wiki/help-protocol]] before giving docs/implementation guidance, [[wiki/build-first-learning]] as the primary compounding-skill method, [[wiki/vibe-docing]] for scoped mechanism help, and [[wiki/pre-wire-protocol]] for full feature ownership.
- Build-First mode rules are mainstream: AUDIT is default for check/clean/debug on active learning artifacts; PATCH requires explicit permission; STEAL creates reference-only artifacts outside active code; ABSORPTION is deep artifact study after interest appears; VIBE_DOCING must not reuse live build values.
- Default next technical follow-up for PathFinder: treat Goals as a planning-ready handoff layer in prompts; next replay should exercise the full orchestrator path so routing/counter behavior is tested beyond the stage + compiler wrapper
- After the 2026-04-12 live frontend run, do not count assistant wording as stage completion; verify Goals completion from raw `getBackendState()` (`goals.done === true` plus frontend completed stage/current-stage agreement)
- The uncertainty attack is now documented in `eval/UNCERTAINTY_ATTACK_REPORT_2026-04-12.md`; full chat is paused until the next session, but pre-chat test-path bugs are fixed
- Real-Duc identity continuation is documented in `eval/IDENTITY_CONTINUATION_GOALS_REPORT_2026-04-12.md`; use `eval/live_session_probe.py` with `--message-file` for future restored-trace continuation runs
- Frontend trace output regression is now documented in `eval/FRONTEND_EVALUATION_REPORT.md` and executable as `eval/live_frontend_output_regression_2026-04-12.jsonl`; incomplete current stages must stay anchored to raw `done` state
- Stage transitions now have a post-stage manager before output; if a stage marks itself done, the output prompt should see the newly active stage in the same turn
- Output lock and stage intro are complementary: stage intro may acknowledge the completed previous-stage handoff, while current-stage lock prevents moving beyond the newly active incomplete stage
- Purpose now mirrors Goals' handoff-sufficiency pattern: once Purpose fields are stable enough as identity priors, remaining execution realism belongs to Goals, Job, or Major rather than another repeated risk squeeze
- Do not pre-choose `orchestrator replay` vs `broader full-path audit`; make that call only after the full eval sweep lands
- Token optimization is now active in both the main `messages` lane and the sub-orchestrator memory lane; workers read a capped recent tail while `routing_memory` keeps its summarizer lane
- The PathFinder `python_function_check` workflow should broaden seam coverage beyond the current four groups when cheap Python-owned seams are worth locking
- The sub-orchestrator `summarizer` and `worker` families now have their own focus-eval lane and separate 3-round production gates
- Maintained repo mirrors should use explicit sync routines rather than manual-by-default content mirroring
- PathFinder docs are vault-canonical by default; repo documentation mirrors are explicit exceptions, not a general sync rule
- PathFinder evaluation docs, reports, audits, and run retrospectives now live in `projects/pathfinder/sources/docs/evaluation/`; repo `eval/` is executable evidence only
- Raven evaluation docs, reports, audit logs, and production-readiness decisions are vault-canonical under `projects/raven/notes/`; repo `eval/` is executable evidence only. Router: [[projects/raven/notes/raven-evaluation-domain]]
- PathFinder Python contract/regression tests now live under `D:\ANHDUC\Path_finder\backend\test\`; new tests should be invoked as `backend.test.<module>` and not added at repo root
- PathFinder project dev log now uses a two-layer mirror: `D:\ANHDUC\Path_finder\logs\DEV_LOG.md` as the repo index plus mirrored daily files under `logs/dev/days/`; other repo logs stay local unless explicitly promoted
- The vault global activity log now uses the same two-layer rule: `log.md` is navigation only, while the actual daily activity log lives under `sources/log/days/`
- Stable router pages may be treated as already validated for the day if they were not edited and no structural issue was found on read

## This Week's Focus
- Decide whether to freeze PathFinder as reviewable portfolio evidence, with only critical blockers fixed rather than continued feature pushing
- Choose and scaffold the next project around reusable AI-agent infrastructure, evaluation, memory, and distribution leverage; current candidate is [[projects/raven/README|Raven]], a Knowledge Signal Engine for filtering YouTube/Reddit noise into sourced insight, vault memory, and public synthesis artifacts by formalizing Duc's internal bullshit detector
- Explore an AI-assisted YouTube journey-recording workflow that can compound into public proof and interested leads; current interest is strong motion typography, animated block editing, and fast founder-documentation loops
- Harden University comparison/ranking behavior for the UEH/FPT/RMIT/UEL lane exposed by the 2026-04-13 university-finding frontend run only if needed for review/demo confidence
- Exercise the output stage-state lock and Goals handoff contract through the full orchestrator path when the next full-path replay cycle resumes
- Use the completed real-Duc Goals continuation as a seed for Job/Major handoff evaluation, not as proof that the full fresh UI path is complete
- Use the completed frontend fixture report as the UI baseline, then only reopen frontend testing for new UI changes or mobile/visual polish
- Keep the cheaper stage-to-output seam and broaden the vault-canonical grouped `python_function_check` workflow as the pre-replay gate
- Continue token optimization through the main `messages` lane and sub-orchestrator `routing_memory` lane while full eval remains the primary hardening gate
- Treat the sub-orchestrator focus-eval lane as seam-ready after Round 3; keep full eval as the broader remaining hardening gate
- Move maintained repo mirrors toward explicit sync routines instead of leaving mirror updates manual by default

## Active Projects
- [[projects/pathfinder/README|PathFinder]] - reviewable/portfolio-ready unless a specific blocker threatens demo or review confidence.
- [[projects/raven/README|Raven]] - active next scaffold. Current repo has SQLite foundation, a live-smoke verified YouTube `search.list` + first normalization pass, and a one-node `gpt-5.4-mini` query enricher prompt/graph seam that passed 15/15 live eval cases across 3 rounds. Raven now also has a vault-canonical visual planning domain at [[projects/raven/notes/raven-architecture-hub]], grounded in the reusable [[wiki/synthesis/obsidian-d2-canvas-architecture-method]]. In the current architecture scope, system-level decisions now go through Canvas first while function-local code planning stays out of Canvas. Next architecture thread: [[projects/raven/notes/raven-vault-keeper-harness-architecture]] for vault ingestion, promotion, and retrieval shape. Next implementation seam still remains connecting enriched queries into YouTube search -> SQLite write/readback. Raven uses [[projects/raven/notes/raven-ownership-delegation-protocol|ownership-first delegation]]: delegate only work Duc can already write, explain, test, and repair.
- [[projects/ielts-writing/README|IELTS Writing]] - active, parallel track. 20-day band 4-5 → 7-8 protocol. Two schema docs (Task 1 + Task 2) and 14-day mastery plan created. Gap is structural, not linguistic. Day 1 starts 2026-04-09.

## Blockers / Open Questions
- Whether the prompt-only Goals handoff contract holds under a fresh live uncertainty frontend run after the quiz-seeded Thinking state, empty-MI completion, sticky testStatus, and nested Goals done fixes
- Whether the same-turn stage transition patch holds in a fresh live run after backend restart
- Whether frontend fixture testing should be broadened into automated Playwright coverage after the current eval/dataset pass
- Whether University needs a comparison-state contract or prompt-only hardening to rank named schools after evidence appears

## Vault Status
- Bootstrapped 2026-04-06. PathFinder is the first fully ingested project corpus.
- IELTS Writing project scaffolded 2026-04-08 — [[projects/ielts-writing/README]] + Task 1/Task 2 schema docs + 14-day plan.
- File Creation Gate patched 2026-04-08 — added pre-write phase to SCHEMA.md + CLAUDE.md; root cause was post-write-only validation allowing bad types/tags/sync to land in files before repair ran.
- Routing: README -> hub notes -> source docs. Do not jump to raw sources first.
- `context/me.md` expanded 2026-04-08 — full personal profile filled (background, constraints, motivation, working conditions).
- Learning system bootstrapped 2026-04-08 — [[wiki/pre-wire-protocol]] + [[learning/README]] + session template. Use for any feature Duc wants to learn before delegating.
- Added a transcript-backed raw-source lane for video/audio ingest under `sources/transcripts/`.
- Daily notes are now being treated more explicitly as raw capture to be graduated into durable pages, not overwritten by agent synthesis.

## Upcoming
- Run a dedicated University comparison/ranking evaluation cycle using the UEH/FPT/RMIT/UEL findings from the 2026-04-13 frontend run
- Run the live-trace Goals/Job/Major handoff replay through the broader orchestrator path after the stage-wrapper pass
- Use `eval/FRONTEND_EVALUATION_REPORT.md` and the vault frontend-evaluation how-to as the baseline for future UI state checks
- Keep the main `messages` prune window, sub-orchestrator `routing_memory` 5k summarizer lane, and 2.5k worker read tail under full-eval observation
- Run the broader full eval pass on the cleaned backend and use that failure surface to choose the next cross-system hardening target
- Broaden the vault-canonical `python_function_check` workflow beyond the current four buckets where cheap seam proof is still missing
- Replace manual-by-default repo mirror handling with explicit sync routines for any maintained mirror beyond the current dev-log pair
- Validate the new "finish response -> write back now" contract on the next few ingest passes

## Related
- [[context/me]]
- [[context/goals]]
- [[briefing.md]]
- [[projects/pathfinder/README]]
- [[projects/pathfinder/notes/docs-evaluation-domain]]

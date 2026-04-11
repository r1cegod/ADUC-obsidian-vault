---
type: context
title: "Current Focus"
created: 2026-04-06
updated: 2026-04-11
tags: [context]
status: active
lang: en
---

> **TL;DR**: PathFinder scholarship demo shipped 2026-03-30. Now in eval/hardening phase: the Stage 4 seam and grouped Python checks are green, both message-memory lanes have token controls, Duc's first live trace-to-Goals audit patched a streamed-output sanitizer gap, and the frontend forced-stage fixture pass is documented. The live-trace Goals policy has moved to a prompt-only handoff contract: Goals extracts planning-ready direction, Job owns market/client realism, and Major owns curriculum/qualification realism.

## Active Decisions
- Default next technical follow-up for PathFinder: treat Goals as a planning-ready handoff layer in prompts; next replay should exercise the full orchestrator path so routing/counter behavior is tested beyond the stage + compiler wrapper
- Do not pre-choose `orchestrator replay` vs `broader full-path audit`; make that call only after the full eval sweep lands
- Token optimization is now active in both the main `messages` lane and the sub-orchestrator `routing_memory` lane; do not treat it as a separate undecided bucket after full eval
- The PathFinder `python_function_check` workflow should broaden seam coverage beyond the current four groups when cheap Python-owned seams are worth locking
- The sub-orchestrator `summarizer` and `worker` families now have their own focus-eval lane and separate 3-round production gates
- Maintained repo mirrors should use explicit sync routines rather than manual-by-default content mirroring
- PathFinder docs are vault-canonical by default; repo documentation mirrors are explicit exceptions, not a general sync rule
- PathFinder project dev log now uses a two-layer mirror: `D:\ANHDUC\Path_finder\logs\DEV_LOG.md` as the repo index plus mirrored daily files under `logs/dev/days/`; other repo logs stay local unless explicitly promoted
- The vault global activity log now uses the same two-layer rule: `log.md` is navigation only, while the actual daily activity log lives under `sources/log/days/`
- Stable router pages may be treated as already validated for the day if they were not edited and no structural issue was found on read

## This Week's Focus
- Exercise the new Goals handoff contract through the full orchestrator path, using the live-trace replay rows as the seed
- Use the completed frontend fixture report as the UI baseline, then only reopen frontend testing for new UI changes or mobile/visual polish
- Keep the cheaper stage-to-output seam and broaden the vault-canonical grouped `python_function_check` workflow as the pre-replay gate
- Continue token optimization through the main `messages` lane and sub-orchestrator `routing_memory` lane while full eval remains the primary hardening gate
- Treat the sub-orchestrator focus-eval lane as seam-ready after Round 3; keep full eval as the broader remaining hardening gate
- Move maintained repo mirrors toward explicit sync routines instead of leaving mirror updates manual by default

## Active Projects
- [[projects/pathfinder/README|PathFinder]] - post-scholarship, eval/hardening phase. Thinking, Purpose, Goals, Job, Major, and Uni now pass the current Stage 4 `evaluation_graph` seam; the grouped Python-function checks are green across five buckets; the live frontend trace-to-Goals audit patched streamed-output sanitization and the follow-up prompt pass made Goals a planning-ready handoff into Job/Major.
- [[projects/ielts-writing/README|IELTS Writing]] - active, parallel track. 20-day band 4-5 → 7-8 protocol. Two schema docs (Task 1 + Task 2) and 14-day mastery plan created. Gap is structural, not linguistic. Day 1 starts 2026-04-09.

## Blockers / Open Questions
- Whether the prompt-only Goals handoff contract holds under full orchestrator routing, not just the `goals_eval` wrapper
- Whether frontend fixture testing should be broadened into automated Playwright coverage after the current eval/dataset pass

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
- Run the live-trace Goals/Job/Major handoff replay through the broader orchestrator path after the stage-wrapper pass
- Use `eval/FRONTEND_EVALUATION_REPORT.md` and the vault frontend-evaluation how-to as the baseline for future UI state checks
- Keep the main `messages` 2k prune window and sub-orchestrator `routing_memory` 5k summarizer lane under full-eval observation
- Run the broader full eval pass on the cleaned backend and use that failure surface to choose the next cross-system hardening target
- Broaden the vault-canonical `python_function_check` workflow beyond the current four buckets where cheap seam proof is still missing
- Replace manual-by-default repo mirror handling with explicit sync routines for any maintained mirror beyond the current dev-log pair
- Validate the new "finish response -> write back now" contract on the next few ingest passes

## Related
- [[context/me]]
- [[context/goals]]
- [[briefing.md]]
- [[projects/pathfinder/README]]

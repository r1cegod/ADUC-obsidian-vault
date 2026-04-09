---
type: context
title: "Current Focus"
created: 2026-04-06
updated: 2026-04-09
tags: [context]
status: active
lang: en
---

> **TL;DR**: PathFinder scholarship demo shipped 2026-03-30. Now in eval/hardening phase: Thinking, Purpose, Goals, Job, Major, and Uni all pass the current Stage 4 `output_compiler` seam, confidence-lock language is aligned to Python's `> 0.8` done gate across both knowledge and retrieval stages, the structured-output serializer warning debt is paid, Case C now reads normalized escalation families, and the new four-group `python_function_check` workflow passes cleanly after fixing Thinking's stale post-cap `done` bug. The next hardening layer is now explicit: run the full eval pass and clean up what it exposes.

## Active Decisions
- Default next technical follow-up for PathFinder: run the full eval pass on the cleaned backend, then clean up whatever it exposes
- PathFinder docs are vault-canonical by default; repo documentation mirrors are explicit exceptions, not a general sync rule
- PathFinder project dev log now uses a two-layer mirror: `D:\ANHDUC\Path_finder\logs\DEV_LOG.md` as the repo index plus mirrored daily files under `logs/dev/days/`; other repo logs stay local unless explicitly promoted
- The vault global activity log now uses the same two-layer rule: `log.md` is navigation only, while the actual daily activity log lives under `sources/log/days/`
- Stable router pages may be treated as already validated for the day if they were not edited and no structural issue was found on read

## This Week's Focus
- Run the full eval pass on the cleaned backend and treat the resulting failures as the next hardening queue
- Keep the cheaper stage-to-output seam and the vault-canonical grouped `python_function_check` workflow as the pre-replay gate while the broader replay layer is being audited
- Decide whether the post-eval cheapest next blocker is orchestrator replay, token optimization, or a broader full-path audit

## Active Projects
- [[projects/pathfinder/README|PathFinder]] - post-scholarship, eval/hardening phase. Thinking, Purpose, Goals, Job, Major, and Uni now pass the current Stage 4 `evaluation_graph` seam; the grouped Python-function checks are now green; next production gate is the full eval layer on the cleaned orchestrator/compiler path.
- [[projects/ielts-writing/README|IELTS Writing]] - active, parallel track. 20-day band 4-5 → 7-8 protocol. Two schema docs (Task 1 + Task 2) and 14-day mastery plan created. Gap is structural, not linguistic. Day 1 starts 2026-04-09.

## Blockers / Open Questions
- Whether the next cheapest production blocker after the full eval sweep is orchestrator token optimization or a broader full-path replay audit
- Whether any future repo mirrors beyond the current dev-log index + day-file mirror should stay manual or move to an explicit sync routine
- Whether the current four-bucket Python-function-check split is the right long-term vault evaluation shape or should be merged/split again later
- How the new `routing_memory` lane in the sub-orchestrator should be summarized once the current hard 5k raw-message cutoff is replaced

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
- Run the full eval pass and clean up the failures it surfaces
- Design the sub-orchestrator `routing_memory` summarizer now that the direct full-message wire is in place behind a hard 5k cutoff
- Decide whether the vault-canonical `python_function_check` workflow needs broader seam coverage beyond the current four buckets
- Decide whether the current manual-by-default repo mirror policy should ever become automated
- Validate the new "finish response -> write back now" contract on the next few ingest passes

## Related
- [[context/me]]
- [[context/goals]]
- [[briefing.md]]
- [[projects/pathfinder/README]]

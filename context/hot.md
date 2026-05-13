---
type: context
title: Session Hot Cache
created: '2026-04-12T00:00:00.000Z'
updated: '2026-05-12'
tags:
  - context
  - session
status: active
lang: en
feeds_into:
  - duc-os.md
---
> **TL;DR**: Temporary hot cache. Read this before [[duc-os]], then let Duc OS route the session.

## How To Use

1. Read this first as startup cache.
2. Then read [[duc-os]].
3. Skip repair pass on pages listed under `Stable Since Last Session` unless you edit them now.
4. Update only when continuity, stable-router status, or next action changed.

## Current Continuity

### Duc OS
- Root operating layer: [[duc-os]].
- Life factory map: [[duc-os/escape-velocity-map]].
- Executable escape route: [[duc-os/escape-route]].
- Leverage development tree: [[duc-os/leverage-development-tree]].
- Current-state authority: [[duc-os/current]].
- Live KICKSTART surface: [[duc-os/kickstart]].
- Context migration status: `context/me.md`, `context/goals.md`, `context/now.md`, and `context/kickstart.md` are compatibility redirects, not deep authority.

### PathFinder
- Status: reviewable/portfolio-ready unless a concrete blocker threatens demo or review confidence.
- Live PathFinder route: [[projects/pathfinder/notes/pathfinder-context-hub]] -> [[projects/pathfinder/notes/docs-current-context]].

### Raven
- Active repo: `/home/r1ceg/Raven`; backend commands use `./.venv/bin/python`.
- Tier 2 repo implementation is locked open as of 2026-05-12 for Raven Ranker Tier 2 source-packet build. The agent-created transcript_fetcher package/test/dependency were removed on 2026-05-03 at Duc's request; backend tests returned to 8/8, and new Tier 2 work starts from Duc-owned architecture.
- Live state route: [[projects/raven/notes/raven-context-hub]] -> [[projects/raven/notes/raven-current-context]].
- Progress map route: [[projects/raven/notes/raven-context-hub]] -> [[projects/raven/notes/raven-progress-map]].
- Architecture route: [[projects/raven/notes/raven-architecture-hub]] -> `projects/raven/notes/raven-feature-web.canvas`.
- Evaluation route: [[projects/raven/notes/raven-evaluation-hub]].
- Current lane: Raven is under a Codex-native pivot after the Nate AIOS synthesis: Codex is the general agent/operator layer, Duc OS/vault is the memory/control layer, and Raven should narrow into a hard-source acquisition/evidence-preparation tool that emits source packets for Codex instead of becoming a custom all-purpose agent harness. Tier 1 now uses rich `request` input: enricher creates generated search `queries`, Tier 1 writes `final_decision = keep | throw_out`, and final writes `sexy_label = maybe | click | must_click`; no original `query`/`target` input compatibility remains. Latest daily eval run `2` passed on 2026-05-03 for `how to grow a youtube channel`: packet `eval/packets/03-May-2026/08:07:40_raven_full_how-to-grow-a-youtube-channel`, 3 queries, 11 candidates, Tier 1 `keep 9 / throw_out 2`, final labels `must_click 2 / click 3 / maybe 4 / unlabeled 2`. Duc lightly approved Phase 2; request-era baseline suites passed, old YouTube-growth focused datasets showed migration drift, and YouTube-search diagnostic found candidate scarcity is mainly global DB uniqueness suppressing previously seen videos. Duc patched candidate uniqueness to run-local; fresh DB and temp full-graph verification passed with 56 candidates. Default `raven.sqlite` was recreated cleanly on 2026-05-03 with patched schema and 0 runs; pytest was installed and backend tests passed 8/8. Live full-graph rerun is currently blocked by YouTube API `HTTP Error 403: Forbidden`. KICKSTART is now LOCKED to `RAVEN RANKER TIER 2 SOURCE PACKET BUILD`. Tier 2 corrected shape: `transcript_fetcher` uses `youtube-transcript-api` for YouTube v1 and writes full transcripts to `projects/raven/sources/transcripts/<YYYY-MM-DD>_<run-id>/yt/`; `card_maker` writes Daniel-Priestley-style per-source cards to `projects/raven/sources/summaries/<YYYY-MM-DD>_<run-id>/yt/raw/`; Raven graph `wave_reader` reads cards into one Obsidian-linked Wave Report in the same summary run folder. No DB v1; IDs live in filenames/frontmatter/top metadata. Tier 2 now has an auditable execution proposal at [[projects/raven/notes/raven-tier-2-execution-proposal]] after the Daniel Priestley ingest proved the YouTube transcript -> source card -> synthesis workflow. Duc owns/freestyles the working production architecture; agent help defaults to raw VIBE_DOCING mechanism blocks, critical-mistake interrupts, audit, fixtures, tests, observability, docs, and maintenance unless explicitly delegated. Reddit implementation is still not active.
- Parked future lane: transcript-derived source cards under [[projects/raven/sources/transcripts/README]].
- Hygiene flag: root `test/` still violates Raven backend test-folder rule.

### Wynncraft Assistant
- Status: low-priority leisure-control project.
- Live route: [[projects/wynncraft/README]] -> [[projects/wynncraft/notes/wynncraft]].

### Minecraft PvP
- Status: low-priority daily skill project for modern Aerial Lancer PvP at 1-2 hours/day.
- Live route: [[projects/minecraft-pvp/README]] -> [[projects/minecraft-pvp/notes/minecraft-pvp-operating-sheet]].
- Current setup decision: do not mutate the existing CurseForge Wynncraft instance; create or duplicate a separate Fabric 1.21.11 PvP profile after validating target server rules.

### Development Defaults
- Technical help, implementation guidance, debugging, and code delegation route through [[duc-os]] -> [[development]] -> [[wiki/operations/detect-operation]].
- Default stance: `AUDIT` for check/clean/debug on active learning artifacts; `PATCH` only after explicit patch/delegation or clear ONE_TIME_UTILITY.
- KICKSTART is the live top-level to-do list: read-only repo inspection and essential non-mutating tooling such as `rtk` orientation/search/status are allowed for planning, but evals, git mutation, prompt patches, code edits, implementation, and other side-effectful commands require [[duc-os/kickstart]] to be `LOCKED` for that exact lane.
- KICKSTART compressed implementation lists are token-audit triggers: route through [[duc-os/session-protocol]] and [[wiki/operations/context-token-audit-operation]] before deep-loading repo/eval/prompt/architecture detail.

## Stable Since Last Session

- `duc-os.md`
- `briefing.md`
- `projects/pathfinder/README.md`
- `projects/pathfinder/notes/pathfinder-evaluation-hub.md`
- `projects/pathfinder/notes/pathfinder-workflow-hub.md`

## Next Action

- Start from [[duc-os]] and use [[duc-os/current]] or [[duc-os/kickstart]] to choose the next route.
- If Raven is selected, start from [[projects/raven/notes/raven-current-context]], [[projects/raven/notes/raven-codex-native-pivot]], and [[projects/raven/notes/raven-tier-2-source-packet-contract]]; current Tier 2 state is locked open for Ranker Tier 2 source-packet build, with Duc freestyling architecture and agent intervention reserved for critical mistakes or requested mechanism blocks.
- If Minecraft PvP is selected, start from [[projects/minecraft-pvp/notes/minecraft-pvp-operating-sheet]]; the first concrete action is a separate PvP client profile plus Day 1-3 sword-only reps.

## Flagged For This Session

- Duc OS migration supersedes the old `briefing -> context/now` startup stack.
- PathFinder broader University comparison loop is still open if that project becomes active again.

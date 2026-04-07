# Current Context

Use this file as the short-lived working scratchpad for the current build cycle.
Move durable decisions to `PROJECT_CONTEXT.md` or `projects/pathfinder/sources/docs/DEV_LOG.md`.

## Active Goal
- Goal: Lock the `DEV_LOG.md` mirror rule after the docs-to-vault transition.
- Success condition: vault context docs, repo entry files, and both dev-log copies all agree that the vault is canonical while `DEV_LOG.md` is mirrored into the archived repo copy.
- Deadline or milestone: 2026-04-07 mirror-rule lock.

## Current Workstream
- Area: Documentation-contract cleanup for the mirrored dev log exception.
- Files in play: `D:\ANHDUC\Path_finder\AGENTS.md`, `D:\ANHDUC\Path_finder\CLAUDE.md`, `D:\ANHDUC\Path_finder\docs (archived)\DEV_LOG.md`, `projects/pathfinder/sources/docs/context/docs/PROJECT_CONTEXT.md`, `projects/pathfinder/sources/docs/context/how to/context_maintenance.md`, `projects/pathfinder/sources/docs/DEV_LOG.md`
- Why this matters now: the repo docs are archived, but the dev log is intentionally mirrored. If that exception is not explicit, future sessions will update only one copy and create drift.

## Open Questions
- Question: none for this contract patch.
- Blocking component: none for the doc update itself.
- Next check: on the next durable documentation decision, confirm that the same entry lands in both dev-log copies without extra prompting.

## Risks And Constraints
- Risk: the mirrored dev log diverges if an agent treats the repo archive rule as applying to `DEV_LOG.md` too.
- Evidence: the archive boundary was documented broadly, but the mirror exception was not stated explicitly.
- Mitigation: make the exception explicit in project context, maintenance rules, repo entry files, and both dev logs.

## Commands To Re-Run
- `python eval/run_eval.py --mode multi --file eval/<target_attack>.jsonl --graph <target_graph>`
- `python eval/run_eval.py --mode single --file eval/<target_attack>.jsonl --graph <target_graph>`

## Handoff
- Latest change: locked `DEV_LOG.md` as the one mirrored exception to the archive-only repo docs rule and corrected the archived repo path to `docs (archived)\`.
- Verification completed:
  - manual doc inspection of vault context docs
  - manual doc inspection of repo `AGENTS.md`
  - manual doc inspection of repo `CLAUDE.md`
  - append check on both `DEV_LOG.md` copies
- Next best action: keep future durable decisions in sync by appending the same dev-log entry to both copies in the same change.

## Update Stamp
- Last updated: 2026-04-07
- Owner: Codex

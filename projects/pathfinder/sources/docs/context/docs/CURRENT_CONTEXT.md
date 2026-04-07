# Current Context

Use this file as the short-lived working scratchpad for the current build cycle.
Move durable decisions to `PROJECT_CONTEXT.md` or `projects/pathfinder/sources/docs/DEV_LOG.md`.

## Active Goal
- Goal: Make the PathFinder vault the official live documentation home and demote the repo `docs/` tree to archive-only status.
- Success condition: repo instruction files, evaluation workflow docs, and vault canonical docs all agree that the vault `sources/docs/` tree is canonical and repo `docs/` is archived.
- Deadline or milestone: 2026-04-06 docs-to-vault transition lock.

## Current Workstream
- Area: Cleanup pass on the repo bootstrap files after the docs-to-vault transition.
- Files in play: `D:\ANHDUC\Path_finder\AGENTS.md`, `D:\ANHDUC\Path_finder\CLAUDE.md`, `projects/pathfinder/sources/docs/context/docs/CURRENT_CONTEXT.md`, `projects/pathfinder/sources/docs/DEV_LOG.md`
- Why this matters now: after the transition, the repo entry files were still re-explaining the vault routing pattern instead of simply pointing to the vault and getting out of the way.

## Open Questions
- Question: Should `README.md` also be reduced to a thinner bootstrap later, or is it still useful as a project-facing repo overview?
- Blocking component: none for the doc update itself.
- Next check: validate the new vault-first read path during the next real implementation task.

## Risks And Constraints
- Risk: agents may still open repo `docs/` out of habit and treat archived copies as live.
- Evidence: the repo historically taught everyone to read `docs/` first.
- Mitigation: repo instructions now point to the vault first, and the main entry docs in repo `docs/` carry archive notices.

## Commands To Re-Run
- `python eval/run_eval.py --mode multi --file eval/<target_attack>.jsonl --graph <target_graph>`
- `python eval/run_eval.py --mode single --file eval/<target_attack>.jsonl --graph <target_graph>`

## Handoff
- Latest change: simplified repo `AGENTS.md` and `CLAUDE.md` into thin bootstrap files that point to the vault instead of re-encoding the vault routing pattern.
- Verification completed:
  - manual doc inspection of repo `AGENTS.md`
  - manual doc inspection of repo `CLAUDE.md`
- Next best action: use the repo bootstrap on the next real coding task and confirm that the vault entry flow is sufficient without duplicated repo guidance.

## Update Stamp
- Last updated: 2026-04-06
- Owner: Codex

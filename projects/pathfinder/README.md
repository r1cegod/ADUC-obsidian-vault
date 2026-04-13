---
type: project
title: "PathFinder"
created: 2026-04-06
updated: 2026-04-13
tags:
  - project/pathfinder
  - ai
  - engineering
status: active
priority: high
lang: en
feeds_into:
  - briefing.md
  - context/now.md
---

> **TL;DR**: PathFinder is a Vietnamese multi-agent career counselor project now mirrored into the vault with local raw docs plus derived summary notes.

## Start Here
Use the smallest sufficient route for the task:
- Need stable orientation: [[projects/pathfinder/notes/docs-project-context|PathFinder Project Context]]
- Need the live workstream: [[projects/pathfinder/notes/docs-current-context|Current Context]]
- Need a domain-specific route: choose one hub from `Task Routes`

If exact wording or contract precision matters, drill into `projects/pathfinder/sources/docs/` only after reading the relevant note page.

## Task Fast Paths
- Code bug, repo review, or implementation resume: [[projects/pathfinder/notes/docs-current-context|Current Context]]
- Evaluation replay, trace audit, or report routing: [[projects/pathfinder/notes/pathfinder-evaluation-hub|PathFinder Evaluation Hub]], [[projects/pathfinder/notes/docs-evaluation-domain|PathFinder Evaluation Domain]]
- Cheap deterministic backend seam checks: [[projects/pathfinder/notes/docs-python-function-check-how-to-use|PathFinder Python Function Check]]
- Prompt or student-facing behavior change: [[projects/pathfinder/notes/pathfinder-prompt-hub|PathFinder Prompt Hub]]
- Architecture, state, or graph routing question: [[projects/pathfinder/notes/pathfinder-architecture-hub|PathFinder Architecture Hub]]
- Documentation, handoff, or vault/repo mirroring workflow: [[projects/pathfinder/notes/pathfinder-workflow-hub|PathFinder Workflow Hub]], [[projects/pathfinder/notes/docs-repo-vault-sync-policy|Repo Vault Sync Policy]]

## Hot Paths Now
For the current evaluation cycle, these are the highest-value pages:
- Live workstream: [[projects/pathfinder/notes/docs-current-context|Current Context]]
- Evaluation domain ownership: [[projects/pathfinder/notes/docs-evaluation-domain|PathFinder Evaluation Domain]]
- Evaluation workflow: [[projects/pathfinder/notes/docs-eval-how-to-use|PathFinder Evaluation Pipeline]]
- Python seam gate: [[projects/pathfinder/notes/docs-python-function-check-how-to-use|PathFinder Python Function Check]]
- Knowledge-agent eval contract: [[projects/pathfinder/notes/docs-knowledge-agent-evaluation|Knowledge Agent Evaluation Guide]]
- Active retrieval-stage audits: [[projects/pathfinder/notes/docs-job-evaluation|Job Agent Evaluation And Audit Log]], [[projects/pathfinder/notes/docs-major-evaluation|Major Agent Evaluation And Audit Log]]
- Next stage targets: [[projects/pathfinder/notes/docs-purpose-evaluation|Purpose Agent Evaluation And Audit Log]], [[projects/pathfinder/notes/docs-goals-evaluation|Goals Agent Evaluation And Audit Log]]

## Goal
Build a durable project workspace that lets any agent start from a compressed, structured knowledge layer before drilling into the canonical PathFinder docs inside this vault.

## Current Status
Core `docs/` content has been ingested into project-local sources and summarized into note pages. This vault now holds the canonical operational contract, while the repo `docs/` folder is archived. Evaluation docs and reports are vault-only under `projects/pathfinder/sources/docs/evaluation/`; repo `eval/` is an executable/evidence workspace. The current hardening queue is University comparison/ranking after the 2026-04-13 university-finding frontend run fixed the Major handoff into University.

## Testing Rule
All Python contract/regression tests live under `D:\ANHDUC\Path_finder\backend\test\`. New tests should use `test_*.py` names inside that folder and be run as `backend.test.<module>` with `python -m unittest`. Do not add root-level `test_*.py` files or scatter tests beside implementation modules.

## Task Routes
- Architecture and graph shape: [[projects/pathfinder/notes/pathfinder-architecture-hub|PathFinder Architecture Hub]]
- Live implementation handoff: [[projects/pathfinder/notes/pathfinder-context-hub|PathFinder Context Hub]]
- Prompt work: [[projects/pathfinder/notes/pathfinder-prompt-hub|PathFinder Prompt Hub]]
- Evaluation work: [[projects/pathfinder/notes/pathfinder-evaluation-hub|PathFinder Evaluation Hub]]
- Workflow and handoff docs: [[projects/pathfinder/notes/pathfinder-workflow-hub|PathFinder Workflow Hub]]

## Core Links
- [[projects/pathfinder/notes/pathfinder-docs-ingest|PathFinder Docs Ingest]]
- [[projects/pathfinder/notes/docs-project-context|PathFinder Project Context]]
- [[projects/pathfinder/notes/docs-architecture|PathFinder Architecture]]
- [[projects/pathfinder/notes/docs-stage-prompt-audit|Stage Prompt Audit Guide]]
- [[projects/pathfinder/notes/docs-evaluation-domain|PathFinder Evaluation Domain]]
- [[projects/pathfinder/notes/pathfinder-architecture-hub|PathFinder Architecture Hub]]
- [[projects/pathfinder/notes/pathfinder-evaluation-hub|PathFinder Evaluation Hub]]
- [[projects/pathfinder/notes/docs-repo-vault-sync-policy|Repo Vault Sync Policy]]

## Raw Sources
- Project-local mirror: `projects/pathfinder/sources/docs/`
- Canonical live docs: `projects/pathfinder/sources/docs/`
- Archived repo copy: `D:\ANHDUC\Path_finder\docs (archived)\`
- Repo dev-log mirror: `D:\ANHDUC\Path_finder\logs\DEV_LOG.md`
- Canonical dev-log day files: `projects/pathfinder/sources/docs/dev-log/days/`
- Repo dev-log day files: `D:\ANHDUC\Path_finder\logs\dev\days\`
- Evaluation domain: `projects/pathfinder/sources/docs/evaluation/`
- Repo eval evidence workspace: `D:\ANHDUC\Path_finder\eval\`
- Rule: this vault now holds the live PathFinder documentation set; the repo `docs (archived)/` folder is archive-only, evaluation reports stay vault-only, repo `eval/` keeps executable evidence only, and the paired `DEV_LOG.md` index + day-file mirror is the one maintained repo logging exception and the baseline example of an explicit sync routine

## Tasks
- [x] Mirror `docs/` into project-local sources, excluding `DEV_LOG.md`
- [x] Create one derived summary page per ingested doc
- [x] Add project routing to the vault index and context layer
- [x] Establish the dev-log repo/vault mirror with `logs/DEV_LOG.md` as the tracked repo index plus paired day-file sync
- [x] Decide that maintained repo mirrors should use explicit sync routines rather than manual-by-default mirroring

## Notes
This project workspace is now both the routing layer and the live documentation home for PathFinder. The repo `docs/` folder is kept only as archived reference material.

The strongest value of this workspace is onboarding efficiency. Agents can begin with the README, the ingest synthesis page, and a few key summaries, then open the raw source only when precision requires it.

Project hubs are the default navigation layer beneath this README, but they are routing aids, not fixed syllabi. Use the matching hub when a task clearly falls into one domain; otherwise stop at the smallest page that already gives enough context.

## Related
- [[projects/pathfinder/notes/pathfinder-docs-ingest]]
- [[context/now]]
- [[briefing.md]]

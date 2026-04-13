---
type: source-summary
title: "PathFinder Evaluation Domain"
created: 2026-04-13
updated: 2026-04-13
tags:
  - project/pathfinder
  - pathfinder
  - evaluation
  - workflow
  - docs
status: active
lang: en
source: "[[projects/pathfinder/sources/docs/evaluation/README.md]]"
---

> **TL;DR**: The evaluation domain README makes `projects/pathfinder/sources/docs/evaluation/` the canonical home for PathFinder evaluation docs, reports, audits, and run retrospectives; repo `eval/` is only for executable evidence.

## Summary
This note summarizes the evaluation-domain source-of-truth rule. PathFinder evaluation documentation now lives in the vault evaluation directory, including workflow guides, stage logs, data-agent audits, frontend reports, and live-session retrospectives.

The repo `eval/` directory remains useful, but only as an executable workspace: runners, JSONL datasets, trace folders, manifests, scratch messages, screenshots, and temporary reproduction artifacts. New evaluation reports should not be mirrored into the repo. The only project documentation intentionally mirrored between vault and repo is the dev log.

## Key Points
- Canonical evaluation docs and reports live in `projects/pathfinder/sources/docs/evaluation/`.
- Repo `eval/` holds executable evidence, not maintained report content.
- Python contract/regression tests live in `D:\ANHDUC\Path_finder\backend\test\`, not repo `eval/` or repo root.
- Older repo-side report markdown can remain as pointer files or legacy evidence, but new reports should be written vault-first.
- Closing an evaluation run means updating the vault report, keeping only needed repo evidence, updating the vault dev-log day file, and mirroring only the dev-log day file into repo `logs/dev/days/`.
- The evaluation-domain README is the top-level index for workflow docs, stage logs, data/knowledge-agent docs, and live reports.

## Related
- [[projects/pathfinder/notes/docs-eval-how-to-use]]
- [[projects/pathfinder/notes/docs-frontend-evaluation-how-to-use]]
- [[projects/pathfinder/notes/pathfinder-evaluation-hub]]
- [[projects/pathfinder/notes/docs-repo-vault-sync-policy]]

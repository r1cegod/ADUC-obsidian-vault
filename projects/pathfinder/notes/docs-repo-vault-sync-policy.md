---
type: synthesis
title: "Repo Vault Sync Policy"
created: 2026-04-07
updated: 2026-04-13
tags:
  - project/pathfinder
  - pathfinder
  - workflow
  - docs
status: active
lang: en
---

> **TL;DR**: PathFinder documentation is vault-canonical by default; repo mirrors are explicit exceptions with sync routines, and evaluation reports now stay vault-only while repo `eval/` holds executable evidence.

## Summary
This page defines the current write boundary between the PathFinder repo and the vault. The vault is the canonical documentation layer. The repo is the codebase plus a small set of explicitly mirrored artifacts needed for local developer workflow.

The goal is to stop rediscovering the same rule in conversation: not every vault doc change should sync back to the repo, and not every repo-side note should become canonical documentation. That boundary is now explicit enough to harden: if a repo mirror is maintained, it should have an explicit sync routine instead of relying on manual-by-default copying. The current evaluation-domain rule is stricter: evaluation docs and reports stay in the vault; repo `eval/` keeps executable evidence only.

## Current Policy
- Canonical documentation lives in the vault under `projects/pathfinder/sources/docs/` and the derived note layer under `projects/pathfinder/notes/`
- The repo `docs (archived)/` tree is archive-only, not a live source of truth
- `D:\ANHDUC\Path_finder\logs\DEV_LOG.md` is the maintained repo mirror index of the canonical vault dev log
- The actual mirrored dev-log notes live under `D:\ANHDUC\Path_finder\logs\dev\days\` and `projects/pathfinder/sources/docs/dev-log/days/`
- The repo dev log is tracked in git
- Other files in `D:\ANHDUC\Path_finder\logs\` are local-only unless explicitly promoted later with their own sync routine
- Evaluation docs, reports, audits, and run retrospectives live in `projects/pathfinder/sources/docs/evaluation/`
- Repo `D:\ANHDUC\Path_finder\eval\` is an executable/evidence workspace only: runners, JSONL datasets, raw traces, manifests, scratch messages, screenshots, and temporary reproduction artifacts
- The dev-log index is rebuilt through `D:\ANHDUC\Path_finder\scripts\manage_dev_log.py`, which refuses rebuilds if the repo and vault daily files drift
- New maintained repo mirrors should not be added without naming the canonical source, the mirrored repo path, and the sync command or script that keeps them aligned

## Practical Rule
When a change creates durable PathFinder documentation:
- write the canonical version in the vault first
- mirror it to the repo only if the artifact is explicitly designated as a maintained mirror with an explicit sync routine

When the project dev log changes:
- update the current day file in both the repo mirror and the vault canonical path
- keep the daily note short and human-readable
- rebuild the paired `DEV_LOG.md` index from those day files

When a change only affects repo-local workflow:
- keep it in the repo unless it changes durable project knowledge or operating policy

When an evaluation run closes:
- write the report or audit in the vault evaluation directory
- keep only raw evidence or reproduction assets in repo `eval/`
- update and mirror only the dev-log day file if the result should persist

## Official Direction
The remaining policy call is now closed:
- maintained repo mirrors should use explicit sync routines
- the current dev-log pair is the template, not a one-off exception
- if a mirror does not justify its own sync routine yet, keep it vault-only
- narrow mirror scope still applies; explicit sync does not mean mirror everything
- evaluation reports are vault-only unless a future sync routine explicitly promotes a repo pointer file; the pointer is not the canonical report

## Related
- [[projects/pathfinder/README]]
- [[projects/pathfinder/notes/pathfinder-workflow-hub]]
- [[projects/pathfinder/notes/docs-current-context]]
- [[projects/pathfinder/notes/docs-evaluation-domain]]
- [[context/now]]

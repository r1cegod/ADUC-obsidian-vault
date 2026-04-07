---
type: synthesis
title: "Repo Vault Sync Policy"
created: 2026-04-07
updated: 2026-04-07
tags:
  - project/pathfinder
  - pathfinder
  - workflow
  - docs
status: active
lang: en
---

> **TL;DR**: PathFinder documentation is vault-canonical by default; the repo only mirrors explicitly named artifacts, with `logs/DEV_LOG.md` as the tracked repo mirror and future broader automation still undecided.

## Summary
This page defines the current write boundary between the PathFinder repo and the vault. The vault is the canonical documentation layer. The repo is the codebase plus a small set of explicitly mirrored artifacts needed for local developer workflow.

The goal is to stop rediscovering the same rule in conversation: not every vault doc change should sync back to the repo, and not every repo-side note should become canonical documentation. Manual-by-default mirroring keeps that boundary explicit until a real sync routine is designed.

## Current Policy
- Canonical documentation lives in the vault under `projects/pathfinder/sources/docs/` and the derived note layer under `projects/pathfinder/notes/`
- The repo `docs (archived)/` tree is archive-only, not a live source of truth
- `D:\ANHDUC\Path_finder\logs\DEV_LOG.md` is the maintained repo mirror of the canonical vault dev log
- The repo dev log is tracked in git
- Other files in `D:\ANHDUC\Path_finder\logs\` are local-only unless explicitly promoted later

## Practical Rule
When a change creates durable PathFinder documentation:
- write the canonical version in the vault first
- mirror it to the repo only if the artifact is explicitly designated as a maintained mirror

When a change only affects repo-local workflow:
- keep it in the repo unless it changes durable project knowledge or operating policy

## Open Question
The remaining unresolved decision is not whether the vault is canonical. It is whether some future subset of mirrored artifacts should sync through an explicit routine instead of manual writeback.

Until that is designed, the correct default is:
- manual mirroring
- narrow mirror scope
- explicit exceptions only

## Related
- [[projects/pathfinder/README]]
- [[projects/pathfinder/notes/pathfinder-workflow-hub]]
- [[projects/pathfinder/notes/docs-current-context]]
- [[context/now]]

---
type: operation
title: Session Start Operation
created: 2026-04-21T00:00:00.000Z
updated: '2026-04-25'
tags:
  - workflow
  - docs
  - meta
status: active
lang: en
feeds_into:
  - wiki/operations-hub.md
  - AGENTS.md
  - CLAUDE.md
  - SCHEMA.md
---
> **TL;DR**: Load the vault in the correct order before doing any task so routing, context, and repair obligations start cleanly.

## Growth Contract
- Parent branch: [[wiki/operations-hub]] and wrapper entrypoints
- Node role: operation
- First parent link: [[wiki/operations-hub]]
- Growth trigger: split only if startup develops separate recurring sub-operations beyond context load, route choice, and freshness checks.
- Forbidden contents: project-specific state, full router inventories, and post-task closeout rules.
- Expected child types: startup checks, route-selection rules, and wrapper handoff notes.

## When To Use
Use at the start of every task.

## Routing In
- [[wiki/operations-hub]]
- [[vault-keeping]]
- [[SCHEMA.md]]

## Steps
1. Read `context/hot.md` if the wrapper requires it.
2. Read [[briefing.md]].
3. Read [[context/now]].
4. Check active-project alignment, staleness, and pending files.
5. Only then branch into a project README, family hub, or operation leaf.

## Routing Out
- Development / technical help / code delegation -> [[development]]
- Maintenance work -> [[vault-keeping]]
- New durable vault node placement -> [[wiki/operations/branch-growth-operation]]
- Project work -> `projects/<name>/README.md`
- Operation selection -> [[wiki/operations-hub]]

## After Use Evolution Check
- Was the next page obvious after `briefing -> context/now`?
- Did startup still require scanning too many routers?
- Did any startup rule belong in a smaller entrypoint?
- If friction appeared, patch this leaf or log the gap today.

## Related
- [[SCHEMA.md]]
- [[briefing.md]]
- [[context/hot]]
- [[context/now]]

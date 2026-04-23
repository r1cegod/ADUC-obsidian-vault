---
type: operation
title: "Session Start Operation"
created: 2026-04-21
updated: 2026-04-21
tags: [workflow, docs, meta]
status: active
lang: en
---
> **TL;DR**: Load the vault in the correct order before doing any task so routing, context, and repair obligations start cleanly.

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
- Maintenance work -> [[vault-keeping]]
- Learning/help work -> [[wiki/learning-protocol-hub]]
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

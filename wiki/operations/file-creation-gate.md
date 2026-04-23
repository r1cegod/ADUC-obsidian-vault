---
type: operation
title: "File Creation Gate"
created: 2026-04-21
updated: 2026-04-21
tags: [workflow, docs, meta]
status: active
lang: en
---
> **TL;DR**: Create new vault files through a two-phase gate: resolve type/tags/routing before writing, then register and propagate immediately after.

## When To Use
Use whenever a task creates a new vault file.

## Routing In
- [[wiki/operations-hub]]
- [[vault-keeping]]
- [[SCHEMA.md]]

## Steps
1. Pre-write: choose a registered type and registered tags.
2. Pre-write: confirm routing implications for project or utility files.
3. Write the file.
4. Post-write: update index, relevant routers, and context if needed.
5. Run propagation and self-healing before ending the task.

## Routing Out
- Closeout -> [[wiki/operations/self-healing-operation]]
- Maintenance routing -> [[vault-keeping]]

## After Use Evolution Check
- Was any type or tag decision still ambiguous?
- Did file creation require memory instead of routing?
- Did post-write registration feel scattered?
- If friction appeared, patch this leaf or log the gap today.

## Related
- [[SCHEMA.md]]
- [[index.md]]
- [[wiki/operations/self-healing-operation]]

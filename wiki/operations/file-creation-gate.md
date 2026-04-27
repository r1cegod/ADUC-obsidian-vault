---
type: operation
title: File Creation Gate
created: '2026-04-21T00:00:00.000Z'
updated: '2026-04-25'
tags:
  - workflow
  - docs
  - meta
status: active
lang: en
---
> **TL;DR**: Create new vault files through Branch Growth plus a two-phase gate: choose the parent branch and node role first, resolve type/tags/routing before writing, then register and propagate immediately after.

## When To Use

Use whenever a task creates a new durable vault file.

Use [[wiki/operations/branch-growth-operation]] first unless the file is a raw parked item in `pending/` awaiting SORT.

## Routing In

- [[wiki/operations-hub]]
- [[vault-keeping]]
- [[wiki/operations/branch-growth-operation]]
- [[SCHEMA.md]]

## Phase 0 - Branch Growth

Before writing the file, decide the branch contract:

```text
1. Parent branch
2. Node role: hub, leaf, source, sample, report, log, operation
3. Real-depth reason
4. Expected child types
5. Forbidden contents
6. First parent link
7. Required propagation targets
```

If the file would create fake depth, do not create a hub. Create or update a leaf under the nearest valid branch instead.

## Phase 1 - Pre-Write

1. Choose a registered type from [[SCHEMA.md]]. If no type fits, update the schema first.
2. Choose registered tags from [[index.md]]. If a genuinely new tag is needed, register it first.
3. Choose the nearest matching template and keep its Growth Contract section.
4. Confirm project/routing implications:
   - Project root files must keep Active Projects aligned between [[briefing.md]] and [[context/now]].
   - Hub files must link from their parent router first.
   - Leaf files must link from the nearest valid hub or README, not from every top-level router.
   - Source/evidence files must stay reachable without becoming the first read.

## Phase 2 - Post-Write

1. Add or update the first parent link decided in Branch Growth.
2. Confirm the page includes a Growth Contract, unless it is raw daily capture or pending material.
3. Register the page in [[index.md]] if it belongs under `wiki/`, `learning/`, `references/`, or `projects/`.
4. Update [[SCHEMA.md]] Directory Map only if a new directory was created.
5. Update routers/context only when the branch route or future session state changed.
6. Run propagation and self-healing before ending the task.

## Routing Out

- Branch decision -> [[wiki/operations/branch-growth-operation]]
- Project creation -> [[wiki/operations/project-init-operation]]
- Closeout -> [[wiki/operations/self-healing-operation]]
- Maintenance routing -> [[vault-keeping]]

## After Use Evolution Check

- Was the parent branch obvious before writing?
- Did type or tag selection depend on memory instead of routing?
- Did post-write registration feel scattered?
- Did the new page create real depth or fake hierarchy?
- If friction appeared, patch this leaf or log the gap today.

## Related

- [[wiki/operations/branch-growth-operation]]
- [[SCHEMA.md]]
- [[index.md]]
- [[vault-keeping]]
- [[wiki/operations/self-healing-operation]]

---
type: operation
title: Branch Growth Operation
created: '2026-04-25'
updated: '2026-04-25'
tags:
  - workflow
  - docs
  - meta
  - architecture
status: active
lang: en
feeds_into:
  - vault-keeping.md
  - wiki/operations-hub.md
  - wiki/operations/file-creation-gate.md
  - wiki/operations/project-init-operation.md
  - index.md
---
> **TL;DR**: Before creating any durable vault node, decide its parent branch, node role, real-depth reason, child expectations, forbidden contents, first parent link, and propagation targets.

## Growth Contract
- Parent branch: [[vault-keeping]] and [[wiki/operations-hub]]
- Node role: operation
- First parent link: [[vault-keeping]]
- Growth trigger: split a child operation only when branch creation develops a recurring sub-operation such as feature promotion, source-lane creation, or project-root expansion.
- Forbidden contents: project-specific branch maps, raw audit logs, and fixed templates disguised as law.
- Expected child types: validation gates, project-init links, worked examples, and operation handoffs.

## When To Use

Use before creating any durable vault file that should become part of the navigable tree:

```text
new hub
new leaf note
new project page
new source lane README
new report
new operation
new reusable synthesis/concept page
```

Do not use for quick scratch text, temporary chat-only reasoning, or raw files that are only being parked for later SORT.

## Routing In

- [[vault-keeping]]
- [[wiki/operations-hub]]
- [[wiki/operations/file-creation-gate]]
- [[wiki/synthesis/vault-target-tree-architecture]]

## Core Law

Branching exists to create retrieval intelligence.

```text
branch only when it reduces future search cost
branch only when it captures a real distinction
branch only when the parent would otherwise become overloaded
branch only when the branch has real child pressure now or obvious growth pressure soon
```

If the new page is a single simple idea, create a leaf under the nearest existing branch instead of inventing a hub.

## Required Decisions

Before writing the file, answer these seven decisions:

```text
1. Parent branch
2. Node role: hub, leaf, source, sample, report, log, operation
3. Real-depth reason
4. Expected child types
5. Forbidden contents
6. First parent link
7. Required propagation targets
```

## Decision Table

| Decision | Required Answer |
|---|---|
| Parent branch | Which existing router/hub owns this page first? |
| Node role | Is this a hub, leaf, source, sample, report, log, or operation? |
| Real-depth reason | What future scan does this page eliminate? |
| Expected child types | If hub-like, what kinds of children will it route? |
| Forbidden contents | What does not belong here? |
| First parent link | Which page gets the first link to this node? |
| Propagation targets | Which index/router/context/log pages must change after write? |

## Entry Growth Contract

Every new durable entry must be ready to grow without becoming a blob.

After the TL;DR, add a compact growth contract unless the entry is a raw daily capture or parked pending item:

```text
## Growth Contract
- Parent branch:
- Node role:
- First parent link:
- Growth trigger:
- Forbidden contents:
```

For hubs and project READMEs, add:

```text
- Expected child types:
```

For sources, samples, and reports, add:

```text
- Source/evidence boundary:
```

This section is not bureaucracy. It is the branch DNA. A future agent should know where the node attaches, what it owns, what it refuses to absorb, and when it should split or promote.

## Role Rules

### Hub

Create a hub only when it reduces real search cost.

```text
valid hub pressure
  -> 3+ related children already exist
  -> or a growing domain clearly needs one route
  -> or a parent router is becoming a flat leaf dump
```

A hub should route one meaningful domain, feature, flow, rule cluster, or source lane.

### Leaf

Use a leaf for one durable concept, rule, workflow, report, decision, or contract.

If a leaf starts routing many siblings, promote it or create a parent hub.

### Source / Sample / Evidence

Use source and sample lanes for canonical material, examples, traces, datasets, transcripts, screenshots, or exact evidence.

Source lanes should be reachable from compiled notes but not loaded first by default.

### Operation

Use an operation page for repeatable behavior that future agents must execute, not for one-time project narrative.

## Branch Test

A proposed branch passes only if these are true:

```text
- It makes the next read more obvious.
- It has a clear parent.
- It has a clear forbidden-content boundary.
- It routes children of a coherent kind.
- It does not duplicate an existing hub.
- It does not force root routers to link directly to many leaves.
```

If the branch fails, create or update a leaf under the nearest valid branch instead.

## Workflow

1. Read the nearest project README, family hub, or operation hub.
2. Identify the parent branch and node role.
3. Run the seven required decisions.
4. If the node is valid, continue to [[wiki/operations/file-creation-gate]].
5. After writing, link from the first parent only, then register/propagate as required.
6. Finish through [[wiki/operations/self-healing-operation]].

## Examples

### Raven Eval Report

```text
parent branch: [[projects/raven/notes/raven-evaluation-hub]]
node role: report leaf
real-depth reason: future eval readers should not scan README or prompt hub
first parent link: raven-evaluation-hub
forbidden contents: runner scripts, raw traces, datasets
```

### Raven Search Feature

```text
if one architecture note only
  -> keep as leaf under raven-architecture-hub

if it accumulates architecture + prompt + eval + evidence children
  -> create raven-search-feature-hub
```

### IELTS Sample

```text
parent branch: task schema note or samples lane
node role: sample
real-depth reason: schema stays compact while samples remain inspectable
forbidden contents: broad IELTS strategy or unrelated writing rules
```

## Routing Out

- File creation -> [[wiki/operations/file-creation-gate]]
- Project creation -> [[wiki/operations/project-init-operation]]
- Closeout -> [[wiki/operations/self-healing-operation]]
- Target rules -> [[wiki/synthesis/vault-target-tree-architecture]]

## After Use Evolution Check

- Did the branch decision prevent a flat link dump?
- Did the parent branch become clearer?
- Did the operation prevent a fake hub?
- Did propagation still rely on memory?
- If friction appeared, patch this operation or log the named gap today.

## Related

- [[wiki/synthesis/vault-target-tree-architecture]]
- [[wiki/synthesis/vault-tree-growth-system-review]]
- [[vault-keeping]]
- [[wiki/operations/file-creation-gate]]
- [[wiki/operations/project-init-operation]]
- [[wiki/operations/self-healing-operation]]

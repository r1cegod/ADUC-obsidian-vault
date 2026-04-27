---
type: hub
title: Raven Workflow Hub
created: '2026-04-25'
updated: '2026-04-25'
tags:
  - project/raven
  - workflow
  - docs
  - engineering
status: active
lang: en
feeds_into:
  - projects/raven/README.md
---
> **TL;DR**: Workflow and rules router for Raven. Use this hub for ownership/delegation, draft adoption, repo-vault boundaries, source promotion rules, and closeout behavior.

## Growth Contract
- Parent branch: [[projects/raven/README]]
- Node role: hub
- First parent link: [[projects/raven/README]]
- Growth trigger: add or split rule leaves when Raven develops repeated operating constraints that cut across architecture, evaluation, prompts, or source handling.
- Forbidden contents: system architecture, prompt contracts, per-run eval reports, raw traces, and live backend status.
- Expected child types: ownership rules, delegation rules, repo-vault boundaries, source-promotion rules, and closeout workflows.

## Purpose

This hub keeps Raven's operating rules out of architecture and evaluation notes.

Use it when the question is:

```text
What must I obey before touching Raven?
Where should reports/evidence live?
When can code be delegated?
How does Raven use draft/canvas workflows?
How should vault writeback happen after Raven work?
```

## Start Here

- Need ownership/delegation threshold: [[projects/raven/notes/raven-ownership-delegation-protocol]]
- Need draft-operation adoption: [[projects/raven/notes/raven-draft-operation]]
- Need evaluation write boundary: [[projects/raven/notes/raven-evaluation-hub]], [[projects/raven/notes/raven-evaluation-domain]]
- Need source/evidence lane: [[projects/raven/sources/README]]
- Need branch-growth rules: [[wiki/operations/branch-growth-operation]], [[wiki/synthesis/vault-target-tree-architecture]]

## What This Branch Owns

```text
project operating rules
repo-vault boundaries
ownership/delegation rules
source promotion rules
closeout rules
workflow adoption notes
```

## What This Branch Does Not Own

```text
system architecture
prompt contracts
per-run eval reports
raw traces or datasets
current backend state
```

Route those through the matching Raven hub.

## Raven Workflow Laws

### Ownership First

```text
Duc may delegate only work he can already write, explain, test, and repair.
```

Below that threshold, route through [[development]] and learning/pre-wire behavior before implementation.

### Vault Is Meaning, Repo Is Execution

```text
vault
  -> reports, decisions, workflow, synthesis, prompt/eval insight

repo
  -> code, tests, runnable eval evidence, temporary traces
```

### Branch Before Leaf

When creating new Raven notes, run [[wiki/operations/branch-growth-operation]] first.

```text
new durable Raven node
  -> parent branch
  -> node role
  -> real-depth reason
  -> first parent link
  -> file creation gate
```

### No Feature Hubs Without Real Pressure

Do not create `main-flow`, `search-feature`, `ranking-feature`, or similar hubs until there are multiple child types to route.

## Related

- [[projects/raven/README]]
- [[projects/raven/notes/raven-context-hub]]
- [[projects/raven/notes/raven-evaluation-hub]]
- [[projects/raven/notes/raven-ownership-delegation-protocol]]
- [[projects/raven/notes/raven-draft-operation]]
- [[projects/raven/sources/README]]
- [[wiki/operations/branch-growth-operation]]

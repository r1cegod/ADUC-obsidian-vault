---
type: operation
title: Context Token Audit Operation
created: '2026-04-29'
updated: '2026-04-29'
tags:
  - workflow
  - docs
  - meta
  - context
status: active
lang: en
feeds_into:
  - vault-keeping.md
  - wiki/operations-hub.md
  - index.md
---
> **TL;DR**: Audit and compress the vault context-loading path so agents load routing intelligence first, project detail only when needed, and evidence/source detail only on demand.

## Growth Contract
- Parent branch: [[vault-keeping]]
- Node role: operation
- First parent link: [[vault-keeping]]
- Growth trigger: split only if session-start loading, project-router compression, or source/evidence loading become separate recurring audits with different checklists.
- Forbidden contents: project status reports, raw logs, source dumps, prompt-token optimization for production code, and broad vault-renovation strategy.
- Expected child types: audit checklists, compression examples, load-budget rules, and handoffs into [[wiki/operations/context-update-operation]], [[wiki/operations/lint-operation]], or [[wiki/operations/self-healing-operation]].

## Purpose

Context-token audit is vault keeping for agent attention.

```text
load less
  -> choose the right route faster
  -> preserve detail behind the route
  -> stop startup files from becoming project reports
```

The goal is not minimalism. The goal is correct load depth.

## No-Degradation Rule

Token optimization is valid only when task performance stays intact.

```text
compress routing surface
  -> preserve decision-critical state
  -> keep canonical detail one link lower
  -> verify the next action remains obvious
```

Do not remove context if it is the only place that carries one of these:

```text
current blocker
active decision
verification path
fresh failure state
user preference that changes execution
project route needed before touching files
```

If compression would force a future agent to guess, keep the sentence or move the detail into the correct lower branch before replacing it with a pointer.

## When To Use

Use this operation when:

- Duc asks to optimize token use, context flow, startup flow, or vault loading.
- `context/hot.md`, `duc-os.md`, `duc-os/current.md`, or `briefing.md` starts carrying leaf-level project detail.
- a new operation or project route makes session start heavier.
- an agent must scan multiple sibling pages before the next route is obvious.
- vault maintenance reveals repeated duplicate summaries across root context and project leaves.

Do not use this for production prompt token budgets inside an app. That belongs in the relevant project prompt/evaluation branch.

## Core Model

```text
Tier 0: operating route
  context/hot.md
  duc-os.md
  -> route, stance, and meta-router choice

Tier 1: current/dashboard route
  duc-os/current.md
  briefing.md when project/status snapshot is needed
  -> current state, active focus, and immediate restart points

Tier 2: family or project router
  vault-keeping / development / project README / domain hub
  -> choose the exact leaf

Tier 2: active leaf
  current context / operation / evaluation report / workflow note
  -> real task detail

Tier 3: evidence/source
  raw logs / eval traces / transcripts / repo artifacts
  -> load only when the task demands proof
```

A page is too high in the flow when it contains detail that only matters after the route has already been chosen.

## Audit Workflow

1. Name the user task in one sentence.
2. List the minimum files an agent must load before acting.
3. Mark each paragraph in those files as `route`, `decision`, `state`, `evidence`, or `archive`.
4. Keep `route`, live `decision`, and critical `state` in the current file.
5. Move or point `evidence` and leaf-level project detail down to the nearest project/domain branch.
6. Replace moved detail with one routing sentence plus the canonical wikilink.
7. Verify the next agent can still choose the correct route from the compressed flow.
8. Run [[wiki/operations/self-healing-operation]] for edited pages and log the durable change.

## Compression Moves

Prefer these edits:

```text
long status paragraph
  -> one state sentence + branch link

run counts / thread ids / eval artifacts
  -> evaluation report link

repo file inventory
  -> project current-context link

operation details repeated in hot cache
  -> operation link + one trigger sentence

old next-action history
  -> current restart point only
```

Never delete unique context unless it already exists in the linked lower branch or is intentionally obsolete.

## Pass/Fail Test

A context flow passes when:

```text
- the startup triad selects the right family/project route without scanning leaves
- project detail lives under the project branch
- eval facts live under the evaluation branch
- source evidence is not loaded by default
- `context/hot.md` contains continuity, not a report
```

A flow fails when:

```text
- root context explains a whole feature implementation
- `context/hot.md` stores run counts, trace ids, or prompt details
- top routers link many leaves from mixed families
- future agents must read sideways before knowing the next page
```

## Current Default Load Plan

```text
context/hot
  -> duc-os
  -> duc-os/current or briefing only when needed
  -> smallest matching router
  -> one active leaf
  -> evidence only if verification requires it
```

For Raven, this means:

```text
context/hot
  -> duc-os
  -> briefing when a project dashboard is needed
  -> projects/raven/notes/raven-context-hub
  -> projects/raven/notes/raven-current-context
  -> evaluation/prompt/architecture branch only when the task names that lane
```

## Closeout

After a token-flow edit:

1. Update `updated` dates on edited pages.
2. Register any new operation in [[vault-keeping]], [[wiki/operations-hub]], and [[index.md]].
3. Patch [[context/hot]] only when the next session should remember the route or the restart point changed.
4. Write the day-log entry.

## Related

- [[vault-keeping]]
- [[wiki/operations/session-start-operation]]
- [[wiki/operations/context-update-operation]]
- [[wiki/operations/lint-operation]]
- [[wiki/operations/self-healing-operation]]
- [[context/hot]]
- [[duc-os]]
- [[duc-os/current]]
- [[briefing.md]]

---
type: hub
title: Raven Context Hub
created: '2026-04-25'
updated: '2026-04-29'
tags:
  - project/raven
  - context
  - workflow
  - docs
status: active
lang: en
feeds_into:
  - projects/raven/README.md
  - duc-os/current.md
  - context/hot.md
---
> **TL;DR**: Context router for Raven. Start here for current project state, stable project orientation, repo/vault boundaries, and the smallest next page before touching Raven code or architecture notes.

## Growth Contract
- Parent branch: [[projects/raven/README]]
- Node role: hub
- First parent link: [[projects/raven/README]]
- Growth trigger: split context leaves when root context or this hub starts carrying repeated project-state detail that agents should not load globally.
- Forbidden contents: raw eval traces, full implementation reports, prompt contracts, architecture diagrams, and repo code walkthroughs.
- Expected child types: current-context leaves, stable orientation leaves, route pointers, and context-compression rules.

## Purpose

This hub keeps Raven project state out of root Duc OS pages.

```text
duc-os/current.md
  -> says Raven is active and points to Raven routes

raven-context-hub
  -> routes Raven-specific current and stable context
```

Use this when the task is about Raven status, next actions, live blockers, or where to start inside the project branch.

## Start Here

- Need live project state and next action: [[projects/raven/notes/raven-current-context]]
- Need what has been done so far and the next unresolved decision: [[projects/raven/notes/raven-progress-map]]
- Need project thesis and main routes: [[projects/raven/README]]
- Need architecture route: [[projects/raven/notes/raven-architecture-hub]]
- Need evaluation route: [[projects/raven/notes/raven-evaluation-hub]]
- Need workflow/rules route: [[projects/raven/notes/raven-workflow-hub]]
- Need prompt route: [[projects/raven/notes/raven-prompt-hub]]
- Need source/evidence lane: [[projects/raven/sources/README]]

## What Belongs Here

```text
current Raven status
stable project orientation
next likely route
where project-specific state lives
when to update root context pointers
```

## What Does Not Belong Here

```text
raw eval traces
full implementation reports
prompt contracts
architecture diagrams
repo code walkthroughs
```

Those belong in their domain branches.

## Context Compression Rule

Duc OS current state should point here when Raven detail would otherwise bloat session startup.

```text
duc-os/current.md
  -> Raven active; next route: raven-current-context or raven-architecture-hub

raven-current-context
  -> actual Raven implementation details and next seams
```

## Related

- [[projects/raven/README]]
- [[projects/raven/notes/raven-current-context]]
- [[projects/raven/notes/raven-architecture-hub]]
- [[projects/raven/notes/raven-evaluation-hub]]
- [[projects/raven/notes/raven-workflow-hub]]
- [[duc-os/current]]
- [[context/hot]]

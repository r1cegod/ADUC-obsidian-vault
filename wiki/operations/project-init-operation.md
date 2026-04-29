---
type: operation
title: Project Init Operation
created: '2026-04-21T00:00:00.000Z'
updated: '2026-04-29'
tags:
  - workflow
  - docs
  - meta
status: active
lang: en
---
> **TL;DR**: Create a project as a root router with `notes/` for compiled knowledge, `sources/` for raw evidence, and branch-growth rules that let real hubs emerge without forcing fake structure.

## When To Use

Use when starting a new project namespace in the vault or repairing a project that was created without a clear project root, notes lane, source lane, or branch-growth rule.

Run [[wiki/operations/branch-growth-operation]] first for the project root and any initial hubs.

## Routing In

- [[wiki/operations-hub]]
- [[vault-keeping]]
- [[wiki/operations/branch-growth-operation]]
- [[SCHEMA.md]]

## Required Project Skeleton

Every project starts with this shape:

```text
projects/<name>/README.md   project root router
projects/<name>/notes/      compiled project knowledge
projects/<name>/sources/    raw source, evidence, samples, datasets, traces
```

The README is a router, not a status dump.

## README Must Answer

```text
What is this project?
What are the main task routes?
Which hub should an agent open next?
Where does raw evidence live?
What is explicitly not in scope?
```

Every new project README must include a Growth Contract:

```text
parent branch: Duc OS / briefing project dashboard
node role: project root router
first parent link: briefing.md and/or duc-os/current.md when active
growth trigger: when one task route starts carrying 3+ real children
forbidden contents: raw evidence, full implementation logs, unrelated project memory
expected child types: context, architecture, prompt, evaluation, workflow, sources, feature hubs only when pressure is real
```

## Hub Emergence Rule

Do not create decorative hubs on day one. Create a hub when either is true:

```text
1. The branch has 3+ related notes.
2. The branch is clearly going to keep growing and would otherwise overload the README or parent hub.
```

Common project branches are context, architecture, features, prompts, evaluation, workflow/rules, and sources. These are suggestions, not required slots.

## Steps

1. Decide the project root through [[wiki/operations/branch-growth-operation]].
2. Create `projects/<name>/README.md`, `notes/`, and `sources/`.
3. Write the README as a task router with source/evidence boundaries.
4. Create only initial hubs that already have real routing pressure.
5. Register the project in [[index.md]], [[briefing]], and [[duc-os/current]] if active.
6. Add propagation rules when the project root or new structural hubs need downstream checks.
7. Log the project creation or repair the same session.

## Routing Out

- Project work -> `projects/<name>/README.md`
- File creation -> [[wiki/operations/file-creation-gate]]
- Closeout -> [[wiki/operations/self-healing-operation]]

## After Use Evolution Check

- Was the README a router, not a status dump?
- Did the project have both compiled and raw/evidence lanes?
- Were hubs created only where branch pressure existed?
- Did registration across top-level files feel duplicated?
- If friction appeared, patch this leaf or log the gap today.

## Related

- [[wiki/operations/branch-growth-operation]]
- [[wiki/synthesis/vault-target-tree-architecture]]
- [[SCHEMA.md]]
- [[briefing]]
- [[duc-os/current]]

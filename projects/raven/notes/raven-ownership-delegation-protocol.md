---
type: protocol
title: Raven Ownership Delegation Protocol
created: '2026-04-16'
updated: '2026-04-26'
tags:
  - project/raven
  - protocol
  - delegation
  - learning
  - ownership
status: active
lang: en
feeds_into:
  - projects/raven/notes/raven-workflow-hub.md
  - projects/raven/README.md
---
> **TL;DR**: Raven uses ownership-first delegation under [[development]]. Duc may delegate only work he can already write, explain, test, and repair; anything below that threshold routes through Detect and Learn first, not code execution.

## Growth Contract
- Parent branch: [[projects/raven/notes/raven-workflow-hub]] and [[development]]
- Node role: project protocol leaf
- First parent link: [[projects/raven/notes/raven-workflow-hub]]
- Growth trigger: split only if Raven develops separate recurring ownership rules for ranking, search, evaluation, or vault-promotion work.
- Forbidden contents: concrete code patches, raw session logs, generic learning manual content, and non-Raven delegation policy.
- Expected child types: Raven-specific ownership gates, delegation thresholds, hard stops, and links to Development operations.

## Core Rule

Raven is not PathFinder delegation mode.

```text
If Duc cannot write it himself
   -> do not delegate it
   -> help / pre-wire / manual build first

If Duc can write it himself
   -> delegation may compress execution time
   -> Duc still owns every line
```

The point is not anti-agent purity. The point is preventing skill debt.

PathFinder proved Duc can orchestrate agents to ship. Raven must prove Duc can build with ownership.

## Delegation Law

A Raven core task is delegate-able only if Duc passes all checks:

```text
1. Can I sketch the file/module shape from memory?
2. Can I describe input/output at each seam?
3. Can I write a rough version without agent code?
4. Can I predict the main failure modes?
5. Can I test or inspect whether the output is correct?
```

If any answer is no, the task is not delegate-able yet.

## Delegation Levels

```text
L0 - Forbidden Delegation
Duc cannot explain the mechanism or failure modes.
Action: [[wiki/operations/detect-operation]] -> [[wiki/operations/learn-operation]] first; use [[wiki/pre-wire-protocol]] inside Learn when full feature ownership is needed.

L1 - Socratic Support
Duc knows the system goal but lacks a mechanism.
Action: agent asks questions, gives official docs/minimal concepts, no code.

L2 - Pairing / Review
Duc can write the code but wants pressure, review, or debugging.
Action: agent may critique, test, and point to failure surfaces.

L3 - Execution Delegation
Duc can already write the implementation and tests.
Action: agent may implement a bounded task with explicit ownership rules.
```

Raven default level is L1 or L2. L3 is allowed only after Duc can defend the wire.

## Ownership Gate

Before delegating implementation, Duc writes a short ownership note:

```text
Task:
What I would change:
Files/modules involved:
Inputs:
Outputs:
Failure modes:
How I will verify:
What I do NOT understand yet:
```

Agent classifies the note with semantic labels:

```text
OWNABLE
Duc understands the system and mechanism.
Review/delegation may be allowed.

MECHANISM_GAP
Duc understands the system seam but lacks a technical mechanism.
Route through [[wiki/operations/learn-operation]]; use [[wiki/pre-wire-protocol]] inside Learn if the gap is core/large.

SYSTEM_GAP
Duc has not described data flow, boundary, responsibility, caller, or verification clearly.
No code. Fix the blueprint first.

ONE_TIME_UTILITY
Non-core, non-compounding utility work.
Agent may execute with minimal explanation.
Not valid for Raven core product wires.
```

## Raven Build Flow

Raven's product loop stays separate from the ownership loop.

```text
Raven product loop:
metadata -> rate -> raw data -> rate again -> report -> ingest

Raven ownership loop:
blueprint -> ownership gate -> manual build or bounded delegation -> review -> defend
```

Do not confuse them. Product scoring is what Raven does. Ownership scoring is how Duc builds Raven.

## Agent Rules

Agents working on Raven must obey these constraints:

- Run [[wiki/operations/detect-operation]] for any technical-help or delegation request before giving docs, implementation guidance, or code.
- Do not implement a core feature if Duc has not provided an ownership note or equivalent blueprint.
- If the blueprint has a SYSTEM_GAP, name the missing wire and stop.
- If the blueprint has a MECHANISM_GAP, use [[wiki/operations/learn-operation]] instead of coding; escalate to [[wiki/pre-wire-protocol]] only inside Learn when full feature ownership is required.
- If delegation is allowed, keep the write scope narrow and explicit.
- Do not introduce new frameworks, APIs, state layers, queues, databases, schema migration helpers, public helper functions, or abstractions unless Duc has already approved the mechanism.
- For Raven core code, if Duc cannot explain the approach in detail, Codex must stay in audit/explanation mode and must not write the implementation.
- A doc/mechanism request is not implementation permission. If Duc asks how to do a core mechanism, Codex gives VIBE_DOC first with official docs, neutral skeletons, and Raven mapping in prose only.
- Explained-enough is not write-owned. Before L3 execution, Duc must still be able to name the file set, graph/data shape, state fields, failure mode, and verification path.
- Any extra feature surface discovered during implementation must be reported before it is added.
- Every delegated patch must include verification steps Duc can rerun.
- After implementation, Duc must be able to explain the edited files without reading agent chat history.

## Hard Stop Conditions

Stop delegation immediately if any of these happen:

- Duc says "I don't know why this file exists."
- Duc cannot predict what test should fail if the code is wrong.
- The agent proposes architecture before Duc defines the data flow.
- The patch introduces a dependency Duc has not learned or approved.
- The implementation becomes easier to trust than to understand.
- Codex adds a helper, migration, abstraction, state field, or feature surface that Duc did not explicitly approve.

## Relationship To Existing Protocols

```text
[[development]]
   -> top-domain router for technical help, Learn, and Delegate

[[wiki/operations/detect-operation]]
   -> mandatory threshold gate before Learn or Delegate

[[wiki/operations/learn-operation]]
   -> current user-facing learning/help/audit/manual-build operation

[[wiki/pre-wire-protocol]]
   -> feature-ownership reference inside Learn when the skill should compound

[[wiki/operations/delegate-operation]]
   -> bounded pattern-copy execution after Detect allows it

Raven ownership protocol
   -> stricter overlay for Raven core product work

PathFinder delegated-feature protocol
   -> handoff documentation after delegation has already been allowed
```

Raven adds a stricter project rule for core product wires:

```text
Core Raven product wire + no ownership
   -> no delegation
   -> help / pre-wire / manual build first
```

The one-time utility exception still exists, but only for non-core work:

```text
Allowed one-time utility:
- editor setup
- local environment repair
- mechanical repo cleanup
- boring config that does not define Raven's product architecture

Not one-time utility:
- backend/frontend boundary
- source/rating data model
- ingestion/report flow
- bullshit-detector scoring contract
- storage/eval contract
```

## Related

- [[projects/raven/README]]
- [[projects/raven/notes/raven-workflow-hub]]
- [[development]]
- [[wiki/operations/detect-operation]]
- [[wiki/operations/learn-operation]]
- [[wiki/operations/delegate-operation]]
- [[wiki/learning-protocol-hub]]
- [[wiki/pre-wire-protocol]]
- [[projects/pathfinder/notes/docs-delegated-feature-how-to]]

---
type: protocol
title: Raven Ownership Delegation Protocol
created: '2026-04-16'
updated: '2026-04-16'
tags:
  - project/raven
  - protocol
  - delegation
  - learning
  - ownership
status: active
lang: en
feeds_into:
  - projects/raven/README.md
  - context/now.md
---
> **TL;DR**: Raven uses ownership-first delegation. Duc may delegate only work he can already write, explain, test, and repair. Anything he cannot write yet goes through [[wiki/help-protocol]] or [[wiki/pre-wire-protocol]] first, not delegation.

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
Action: [[wiki/help-protocol]] or [[wiki/pre-wire-protocol]] first.

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
Run [[wiki/help-protocol]] first; escalate to [[wiki/pre-wire-protocol]] if the gap is core/large.

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

- Run [[wiki/help-protocol]] for any technical-help request before giving docs or implementation guidance.
- Do not implement a core feature if Duc has not provided an ownership note or equivalent blueprint.
- If the blueprint has a SYSTEM_GAP, name the missing wire and stop.
- If the blueprint has a MECHANISM_GAP, use [[wiki/help-protocol]] or [[wiki/pre-wire-protocol]] instead of coding.
- If delegation is allowed, keep the write scope narrow and explicit.
- Do not introduce new frameworks, APIs, state layers, queues, databases, or abstractions unless Duc has already approved the mechanism.
- Every delegated patch must include verification steps Duc can rerun.
- After implementation, Duc must be able to explain the edited files without reading agent chat history.

## Hard Stop Conditions

Stop delegation immediately if any of these happen:

- Duc says "I don't know why this file exists."
- Duc cannot predict what test should fail if the code is wrong.
- The agent proposes architecture before Duc defines the data flow.
- The patch introduces a dependency Duc has not learned or approved.
- The implementation becomes easier to trust than to understand.

## Relationship To Existing Protocols

```text
[[wiki/learning-protocol-hub]]
   -> router for the whole learning/help stack

[[wiki/help-protocol]]
   -> mandatory first gate for technical help/docs/debugging

[[wiki/pre-wire-protocol]]
   -> heavy feature-ownership path when the skill should compound

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
- [[wiki/learning-protocol-hub]]
- [[wiki/help-protocol]]
- [[wiki/pre-wire-protocol]]
- [[projects/pathfinder/notes/docs-delegated-feature-how-to]]
- [[context/now]]

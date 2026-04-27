---
type: operation
title: Detect Operation
created: '2026-04-25'
updated: '2026-04-25'
tags:
  - workflow
  - engineering
  - learning
  - protocol
  - meta
status: active
lang: en
feeds_into:
  - development.md
  - wiki/operations-hub.md
---
> **TL;DR**: DETECT is the mandatory threshold operation before Learn or Delegate. It classifies the request, protects ownership, and asks the question that prevents speed from becoming skill debt.

## Growth Contract
- Parent branch: [[development]]
- Node role: operation
- First parent link: [[development]]
- Growth trigger: split only if classification, threshold questions, or ownership labels become large enough to need separate reusable leaves.
- Forbidden contents: Learn-mode teaching detail, Delegate patch procedure, project-specific implementation guidance, and raw session examples.
- Expected child types: threshold labels, routing checks, hard-stop rules, and compact examples.

## Purpose

Detect is the guard at the door of [[development]].

```text
request arrives
  -> detect threshold
  -> learn or delegate only after classification
```

Detect is not user-facing by default. The user can say "Learn" or "Delegate," but the agent still runs Detect first.

## Trigger

Run Detect before:

- [[wiki/operations/learn-operation]]
- [[wiki/operations/delegate-operation]]
- technical help
- docs/mechanism explanations
- debugging support
- implementation patches
- code generation requests
- Raven core product work

## Classification Labels

Use these labels exactly.

```text
SYSTEM_GAP
Duc has not named the owner file/module, data flow, boundary, caller, or verification.

MECHANISM_GAP
Duc sees the seam but lacks one technical mechanism or API/library operation.

PATTERN_FORMING
Duc is writing manually and local repetition is emerging, but delegation would still hide decisions.

OWNABLE
Duc can explain the files, inputs, outputs, steps, failure modes, and verification.

DELEGATABLE
Duc's pattern is clear enough that Codex can copy it and Duc can audit immediately.

ONE_TIME_UTILITY
Non-core, non-compounding work where agent execution is cheaper than learning.
```

## Threshold Questions

Ask only the smallest question that holds the threshold.

```text
1. What file/module owns this?
2. What input enters?
3. What output leaves?
4. Who calls it?
5. What should fail if this is wrong?
6. What existing pattern should I copy?
```

Do not ask all six by reflex. Ask the missing one.

## Routing Decision

```text
SYSTEM_GAP
  -> ask for the missing wire
  -> no Learn details yet
  -> no code

MECHANISM_GAP
  -> [[wiki/operations/learn-operation]]

PATTERN_FORMING
  -> [[wiki/operations/learn-operation]] in BUILD or AUDIT mode
  -> no delegation yet

OWNABLE
  -> review, audit, or bounded delegation may be allowed

DELEGATABLE
  -> [[wiki/operations/delegate-operation]]

ONE_TIME_UTILITY
  -> agent may execute with compact explanation
```

## Hard Stops

Stop before Learn or Delegate if:

- the implementation would be easier to trust than understand
- the user cannot name what would fail
- the patch would introduce a new abstraction, dependency, state layer, or feature the user did not ask for
- the agent is about to solve an architecture gap with code
- the requested speed would create ownership debt

## Output Shape

When Detect matters, state the classification briefly.

```text
DETECT: MECHANISM_GAP.
You know the seam, but not the API call shape. Route: Learn.
```

For tiny obvious requests, Detect may stay implicit as long as the behavior follows the threshold.

## After Use Evolution Check

- Did Detect prevent hidden delegation?
- Was the classification specific enough?
- Did the agent ask one threshold question instead of a questionnaire?
- Did Learn or Delegate run only after classification?

## Related

- [[development]]
- [[wiki/operations/learn-operation]]
- [[wiki/operations/delegate-operation]]
- [[wiki/pre-wire-protocol]]
- [[projects/raven/notes/raven-ownership-delegation-protocol]]

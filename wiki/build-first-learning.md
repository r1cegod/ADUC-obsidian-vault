---
type: protocol
title: Build-First Learning
created: '2026-04-18'
updated: '2026-04-19'
tags:
  - learning
  - protocol
  - meta
status: active
lang: en
feeds_into:
  - wiki/learning-protocol-hub.md
  - wiki/help-protocol.md
  - wiki/pre-wire-protocol.md
  - learning/README.md
---
> **TL;DR**: Build-First Learning is the primary technical-learning method: Duc builds usable project artifacts directly, one maturity level at a time, while the agent audits, narrows, and uses [[wiki/vibe-docing]] only for missing mechanisms.

## Core Rule

```text
Duc ships the artifact.
Agent audits the artifact.
Docs serve the build, not the other way around.
```

This method replaces passive tutorial-first learning for technical/project work. The goal is ownership through impact: build, run, fail, repair, and extract the rule.

## Prime Frame

```text
Ship fast.
Learn faster.
Fail harder.
Duc holds the spoon.
```

The agent is mentor/partner/reviewer, not the hidden implementer.

## Default Flow

```text
1. Pick the smallest usable project artifact.
2. Duc builds it directly in the real project path when practical.
3. Agent verifies by running/inspecting it.
4. Agent classifies the failure surface.
5. If direction gap -> narrow the next artifact.
6. If mechanism gap -> use [[wiki/vibe-docing]].
7. If senior edge case -> agent labels `I will do this reference piece because...` and shows only that mechanism.
8. Duc repairs or scales the artifact.
9. Capture the derived rule.
```

## Usable Artifact Rule

Learning artifacts should be usable unless there is a deliberate reason to make a throwaway reference.

```text
Preferred:
  src/backend/db.py
  real project function
  real CLI command
  real contract check

Allowed only as reference:
  scratch toy
  in-memory demo
  isolated reproduction
```

A scratch artifact may teach a mechanism, but it must not become the primary learning path when the real project artifact is small enough to build safely.

## Maturity Levels, Not Feature Slices

Build one maturity level at a time, not one disconnected feature per exercise.

```text
L0 naive but runs
L1 proper shape
L2 integrity/constraints
L3 usable backend API
L4 adapter-ready
L5 production-ish verification and errors
```

Each level keeps the previous level working and adds one new responsibility.

## Normal vs Adaptive Cases

Normal cases are required mechanism literacy. Build them before external product pressure.

Adaptive cases require another caller, adapter, API, or feature to create real pressure. Do not prebuild them.

```text
Normal case
  -> teaches core ownership now
  -> build before APIs/agents depend on it

Adaptive case
  -> depends on real caller behavior
  -> build only when needed
```

Examples:

```text
Normal:
- connect to database
- create schema
- insert and select rows
- return inserted ids
- enforce parent/child relation
- reject duplicates
- joined readback view

Adaptive:
- API retry tracking
- missing platform fields
- raw response size policy
- schema migration under real data
- audit/rater tables
- conflict resolution across sources
```

## Agent Responsibilities

The agent should:

```text
- verify current artifact before proposing the next one
- name the current level and pass/fail status
- classify failure as direction, mechanism, syntax, contract, or edge case
- provide [[wiki/vibe-docing]] only for a visible mechanism gap
- avoid exact challenge answers before Duc attempts
- avoid silently patching code Duc should own
- preserve usable momentum over theoretical completeness
```

## Duc Responsibilities

Duc should:

```text
- build the artifact directly when possible
- ask for `vibe doc <operation>` when missing a mechanism
- ship ugly L0 before demanding clean architecture
- push back when the method becomes passive or spoonfed
- write the lock-in rule after a pass
```

## Absorption Protocol

Use absorption when Duc explicitly gets interested in a reference artifact and wants to study it deeply before building his own version.

```text
ABSORPTION
  = slow artifact disassembly
  + every input/output named
  + small function details welcomed
  + no pressure to immediately ship
```

Absorption is not the default learning mode. It activates only when Duc names it or clearly asks to study a specific artifact. It is allowed because curiosity has already selected the object, so deep inspection becomes fuel rather than passive tutorial consumption.

## Vibe Docing Role

[[wiki/vibe-docing]] is the mechanism-delivery operation inside Build-First Learning.

```text
Build-First says what to build next.
Vibe Docing teaches one missing operation without giving the artifact answer.
```

Good use:

```text
vibe doc INSERT placeholders
vibe doc SELECT WHERE
vibe doc API headers
```

Bad use:

```text
agent gives full Raven function before Duc attempts
agent hides architecture decision inside doc example
agent uses the exact challenge values in the doc slice
```

## Stop Conditions

Stop and reframe when:

```text
- Duc is tracing unexplained agent code instead of building
- the artifact is not usable and could be usable
- the agent is teaching multiple mechanisms at once
- adaptive cases are being prebuilt without a caller
- the learning session becomes docs-first instead of artifact-first
```

## Related

- [[wiki/learning-protocol-hub]]
- [[wiki/help-protocol]]
- [[wiki/vibe-docing]]
- [[wiki/pre-wire-protocol]]
- [[learning/README]]

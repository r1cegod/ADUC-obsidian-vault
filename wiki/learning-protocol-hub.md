---
type: hub
title: Learning Protocol Hub
created: '2026-04-16'
updated: '2026-04-25'
tags:
  - learning
  - protocol
  - meta
status: active
lang: en
feeds_into:
  - wiki/operations/learn-operation.md
  - learning/README.md
---
> **TL;DR**: Legacy learning-system router. For new technical help or code delegation, start at [[development]]; this page now acts as the reference layer behind [[wiki/operations/learn-operation]].

> Current entrypoint: [[development]] -> [[wiki/operations/detect-operation]] -> [[wiki/operations/learn-operation]].

## Protocol Stack

```text
User asks for technical help / implementation / docs / delegation
  ↓
[[development]]
  ↓
[[wiki/operations/detect-operation]]
  ↓
[[wiki/operations/learn-operation]] or [[wiki/operations/delegate-operation]]
  ↓
old learning protocols as references when needed:
  [[wiki/help-protocol]]
  [[wiki/build-first-learning]]
  [[wiki/vibe-docing]]
  [[wiki/pre-wire-protocol]]
  [[projects/raven/notes/raven-ownership-delegation-protocol]]
  ↓
record durable session in [[learning/README]] when the learning should persist
```

## Growth Contract
- Parent branch: [[wiki/operations/learn-operation]]
- Node role: legacy reference hub
- First parent link: [[wiki/operations/learn-operation]]
- Growth trigger: split only if old learning protocol references become too large to audit as one reference layer.
- Forbidden contents: current top-level routing rules, code delegation procedure, and project-specific implementation walkthroughs.
- Expected child types: legacy protocol references, learning-mode explanations, and migration notes into Learn.

## Which Protocol To Use

### Help Protocol

Use [[wiki/help-protocol]] for any request where Duc does not know how to do something yet and asks for help, docs, direction, debugging, or implementation guidance.

Best for:

- finding official docs
- using [[wiki/vibe-docing]] when Duc needs one mechanism slice instead of a full doc page
- routing to [[wiki/build-first-learning]] when the answer should become a usable artifact
- understanding an API/library mechanism
- debugging a local blocker without spoonfeeding
- deciding whether the gap is small enough for a direct doc pointer

### Pre-Wire Protocol

Use [[wiki/pre-wire-protocol]] when the task is a full feature or core system wire Duc should own.

Best for:

- backend/frontend boundary
- source/rating data model
- agent graph node
- storage/eval contract
- anything Duc should be able to rebuild without chat history

### Raven Ownership Overlay

Use [[projects/raven/notes/raven-ownership-delegation-protocol]] for core Raven product work. It is stricter than the universal rule.

```text
Core Raven wire + no ownership
  ↓
no delegation
  ↓
help/pre-wire/manual build first
```

## Operation Breakdown

This page no longer owns live routing. New technical work routes through [[development]].

```text
1. Request arrives
2. Run [[wiki/operations/detect-operation]]
3. If learning/help is needed -> [[wiki/operations/learn-operation]]
4. Inside Learn, use old references only as needed:
   - [[wiki/help-protocol]] for anti-spoonfeeding shape
   - [[wiki/vibe-docing]] for one mechanism slice
   - [[wiki/build-first-learning]] for artifact-first learning modes
   - [[wiki/pre-wire-protocol]] for full feature ownership
5. If ownable/delegatable -> return to [[wiki/operations/delegate-operation]] only after Detect allows it
6. If session creates durable learning -> record in [[learning/README]]
```

## Named Learning Modes

```text
BUILD
  active usable artifact in project path

AUDIT
  inspect, run, explain, no edits by default

PATCH
  edit only after explicit permission/delegation or ONE_TIME_UTILITY

STEAL
  finished reference artifact outside active path for inspection

ABSORPTION
  deep disassembly of a selected artifact after interest appears
```

## Related

- [[development]]
- [[wiki/operations/detect-operation]]
- [[wiki/operations/learn-operation]]
- [[wiki/operations/delegate-operation]]
- [[wiki/help-protocol]]
- [[wiki/build-first-learning]]
- [[wiki/vibe-docing]]
- [[wiki/pre-wire-protocol]]
- [[learning/README]]
- [[projects/raven/notes/raven-ownership-delegation-protocol]]
- [[context/me]]

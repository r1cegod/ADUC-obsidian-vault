---
type: hub
title: Learning Protocol Hub
created: '2026-04-16'
updated: '2026-04-20'
tags:
  - learning
  - protocol
  - meta
status: active
lang: en
feeds_into:
  - AGENTS.md
  - learning/README.md
---
> **TL;DR**: Router for Duc's learning system: use Help Protocol first, Build-First Learning as the primary skill-compounding method, Vibe Docing for narrow mechanisms, Pre-Wire for full feature ownership, and learning sessions as the durable record.

## Protocol Stack

```text
User asks for help / implementation / docs
  ↓
[[wiki/help-protocol]]
  ↓
if Duc should learn by building
  ↓
[[wiki/build-first-learning]]
  ↓
if full feature ownership is needed
  ↓
[[wiki/pre-wire-protocol]]
  ↓
if Raven core product wire
  ↓
[[projects/raven/notes/raven-ownership-delegation-protocol]]
  ↓
record durable session in [[learning/README]]
```

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

```text
1. Request arrives
2. Run [[wiki/help-protocol]]
3. If architecture gap -> Duc explains the seam first
4. If tiny mechanism gap with visible seam -> [[wiki/vibe-docing]] or official docs + narrow challenge
5. If artifact ownership should compound -> [[wiki/build-first-learning]]
6. Choose Build-First mode when named or implied: BUILD / AUDIT / PATCH / STEAL / ABSORPTION
7. If full feature ownership gap -> start [[wiki/pre-wire-protocol]]
8. If ownable -> review/delegation allowed
9. If session creates durable learning -> record in [[learning/README]]
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

- [[wiki/help-protocol]]
- [[wiki/build-first-learning]]
- [[wiki/vibe-docing]]
- [[wiki/pre-wire-protocol]]
- [[learning/README]]
- [[projects/raven/notes/raven-ownership-delegation-protocol]]
- [[context/me]]

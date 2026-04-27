---
type: hub
title: Development Domain
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
  - briefing.md
  - AGENTS.md
  - CLAUDE.md
  - wiki/operations-hub.md
  - index.md
---
> **TL;DR**: Top-tier development domain for building with ownership: every technical help or delegation request enters through Detect, then routes to Learn or Delegate.

## Growth Contract
- Parent branch: vault root / [[briefing]] / [[wiki/operations-hub]]
- Node role: hub
- First parent link: [[briefing]]
- Growth trigger: add or split child operations only when technical-help, learning, or delegation requests develop recurring routing pressure.
- Forbidden contents: project-specific code walkthroughs, raw repo logs, and broad tutorials that belong in Learn or project notes.
- Expected child types: operation leaves, ownership thresholds, learning protocol routes, and delegation guardrails.

## Core Shape

Development is the top-domain for turning technical work into owned capability.

```text
development
  -> detect first
  -> learn when ownership is not ready
  -> delegate when the pattern is clear enough to copy safely
```

This domain wraps the old learning stack and the new delegation lane. Learning is no longer a separate top-level destination for technical help; it is one operation inside development.

## Entry Law

Any request about technical help, code, docs, debugging, implementation, architecture ownership, or agent-written code starts here.

```text
technical request
  -> [[wiki/operations/detect-operation]]
  -> choose one:
       [[wiki/operations/learn-operation]]
       [[wiki/operations/delegate-operation]]
```

Detect is mandatory before Learn or Delegate. The user can activate Learn or Delegate directly, but the agent still runs Detect first to hold the threshold.

## Three Operations

### Detect

[[wiki/operations/detect-operation]] decides whether the request is ready for help, learning, audit, or delegation.

```text
Detect owns the threshold.
It asks the uncomfortable question before speed begins.
```

### Learn

[[wiki/operations/learn-operation]] is the full learning manual. It absorbs the old help, build-first, pre-wire, and Vibe Docing route into one user-facing operation.

```text
User says: "how do I do this?"
Agent reads Learn.
Agent does not require the user to name Vibe Docing.
```

### Delegate

[[wiki/operations/delegate-operation]] is execution compression after Duc's pattern is clear.

```text
copy Duc's pattern
write bounded code
add no new feature/function/abstraction unless necessary
verify in a way Duc can rerun
```

## Development Floor

The development floor is not maximum speed. It is speed without loss of ownership.

```text
human writes until pattern is visible
  -> AI copies the pattern
  -> Duc audits immediately
  -> floor moves upward
```

The failure mode this domain prevents:

```text
AI writes fast
  -> Duc traces unknown code
  -> understanding debt grows
  -> future freedom shrinks
```

## Routing Table

| User intent | Mandatory route |
|---|---|
| "How do I do this?" | Detect -> Learn |
| "Explain this API/mechanism" | Detect -> Learn |
| "Audit/check/debug this" | Detect -> Learn/AUDIT unless delegation is approved |
| "Write this following my pattern" | Detect -> Delegate |
| "Patch this for me" | Detect -> Delegate only if ownable or one-time utility |
| unclear request | Detect -> ask threshold question |

## Related

- [[wiki/operations/detect-operation]]
- [[wiki/operations/learn-operation]]
- [[wiki/operations/delegate-operation]]
- [[wiki/learning-protocol-hub]]
- [[wiki/help-protocol]]
- [[wiki/build-first-learning]]
- [[wiki/vibe-docing]]
- [[wiki/pre-wire-protocol]]
- [[projects/raven/notes/raven-ownership-delegation-protocol]]
- [[wiki/operations-hub]]

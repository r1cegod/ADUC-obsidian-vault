---
type: note
title: Duc OS Engines
created: '2026-04-29'
updated: '2026-04-29'
tags:
  - context
  - workflow
  - ai
  - docs
status: active
lang: en
feeds_into:
  - duc-os.md
---
> **TL;DR**: Duc OS coordinates engines: Raven finds signal, Codex executes, the vault remembers, social converts proof into leverage, and learning raises the floor.

## Growth Contract
- Parent branch: [[duc-os]]
- Node role: leaf
- First parent link: [[duc-os]]
- Growth trigger: split when Raven, Codex, Social, Learning, or Vault each need their own operating contracts.
- Forbidden contents: full project docs, implementation logs, raw source dumps, and daily task lists.
- Source/evidence boundary: this page maps engine roles; engine-specific evidence and implementation stay in their project/source branches.

## Engine Map

```text
Duc OS
  -> chooses mode and engine

Raven
  -> source intelligence

Codex
  -> execution compression

Vault
  -> memory and routing substrate

Social
  -> distribution and trust capture

Learning
  -> capability floor raising
```

## Raven

Raven is the source intelligence engine.

```text
public source
  -> search / discovery
  -> metadata triage
  -> content ingest later
  -> signal extraction
  -> source memory
  -> public synthesis potential
```

Current Raven status lives under [[projects/raven/notes/raven-context-hub]]. Raven should not become a content hoarder. Its leverage is taste, evidence, evaluation, and memory.

## Codex

Codex is the execution engine.

```text
clear intent
  -> inspect repo/vault
  -> patch or explain
  -> verify
  -> log / update memory
```

Codex should execute only when the route is clear. For technical work, [[development]] and [[wiki/operations/detect-operation]] still protect ownership.

## Leverage Stack

Duc OS should keep the human at the architecture layer and push repeatable execution down into agents.

```text
Duc: architect layer
  -> learn the mechanism
  -> write the reference
  -> document intent / taste / constraints

Agents: execution layer
  -> copy the pattern
  -> run checks / evals
  -> produce reports
  -> surface anomalies

Duc: review layer
  -> read reports
  -> detect drift
  -> decide next evolution
```

The bottleneck should become idea quality, judgment quality, and taste - not repetitive implementation capacity.

Ownership boundary:
- Anything touching how Raven thinks: Duc owns the mechanism first.
- Anything touching how Raven operates: Codex can execute once the contract is clear.
- Write until Duc can teach it. Then let the agent learn it.

Scaling risk:

```text
unclear taste
  -> agent speed
  -> confident wrongness at scale
```

The next level after building is governance: evals, review loops, failure reports, and clear authority boundaries.

## Vault

The vault is the memory substrate.

```text
Duc OS
  -> operating layer

vault
  -> durable memory
  -> source lanes
  -> project state
  -> logs
  -> routing tables
```

The vault should not absorb raw noise. It should hold meaning, source boundaries, decisions, and future-retrievable context.

## Social

Social is the distribution engine.

```text
build / learn / evaluate
  -> public artifact
  -> visible proof
  -> trust
  -> inbound attention
  -> opportunities
```

The goal is not empty posting. The goal is turning real build proof into trust so lead generation becomes less dependent on cold chase.

## Learning

Learning is the capability engine.

```text
mechanism gap
  -> learn by building
  -> ownership test
  -> reusable pattern
  -> higher execution floor
```

Learning routes through [[development]] when technical, and through [[duc-os/session-protocol]] when the gap is strategic clarification.

## Engine Selection Rules

| Situation | Engine |
|---|---|
| Need source signal or report material | Raven |
| Need code/doc execution after route is clear | Codex |
| Need durable memory or routing update | Vault |
| Need public proof or inbound leverage | Social |
| Need mechanism ownership | Learning |
| Need today's move | Duc OS / KICKSTART |

## Related

- [[duc-os]]
- [[duc-os/current]]
- [[duc-os/kickstart]]
- [[duc-os/session-protocol]]
- [[projects/raven/README]]
- [[development]]
- [[vault-keeping]]

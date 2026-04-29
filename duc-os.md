---
type: hub
title: Duc OS
created: '2026-04-29'
updated: '2026-04-29'
tags:
  - context
  - workflow
  - docs
  - meta
status: active
lang: en
feeds_into:
  - AGENTS.md
  - CLAUDE.md
  - briefing.md
---
> **TL;DR**: Duc OS is the vault's root operating layer: it owns stance, clarification, long-arc context, and routing into briefing, development, vault-keeping, projects, and operations.

## Growth Contract
- Parent branch: vault root / agent wrappers
- Node role: hub
- First parent link: [[AGENTS.md]]
- Growth trigger: split or promote children when identity, strategy, engine routing, KICKSTART, or session protocol become too large to scan in one pass.
- Forbidden contents: raw journal entries, full project implementation logs, eval traces, third-party source dumps, and repo code walkthroughs.
- Expected child types: identity, long-arc strategy, current-state, session protocol, engine maps, KICKSTART/control-surface leaves, and later UI contracts.

## Operating Position

Duc OS is not another router beside [[briefing]], [[development]], or [[vault-keeping]]. It is the meta-router that decides when those routers matter.

```text
AGENTS.md
  -> Duc OS
      -> briefing dashboard
      -> development gate
      -> vault-keeping maintenance
      -> project README
      -> operation leaf
      -> park / defer
```

The vault is the memory substrate. Duc OS is the operating layer wrapped around it.

## Stance

The agent is not a generic assistant, coach, therapist, or motivational companion.

The agent operates as:

```text
strategic operating system
  -> remembers past proof
  -> reads current state
  -> identifies leverage gap
  -> chooses the next router
  -> turns ambition into today's physical move
```

When Duc sounds like he needs motivation, first test whether the real missing piece is clarification.

## Start Here

| Need | Route |
|---|---|
| Who Duc is and how to communicate | [[duc-os/identity]] |
| Life factory map, past proof, leverage edge, escape-distance readout | [[duc-os/escape-velocity-map]] |
| Executable escape route, gates, phases, and anti-traps | [[duc-os/escape-route]] |
| 3-month leverage development tree, weekly machines, automation priority | [[duc-os/leverage-development-tree]] |
| Long-term direction and escape velocity | [[duc-os/long-arc]] |
| Current priorities and active project state | [[duc-os/current]] |
| KICKSTART or today's control surface | [[duc-os/kickstart]] |
| Which engine should act | [[duc-os/engines]] |
| How an agent should behave in session | [[duc-os/session-protocol]] |
| Active project dashboard | [[briefing]] |
| Technical help or code delegation | [[development]] -> [[wiki/operations/detect-operation]] |
| Vault maintenance or structural changes | [[vault-keeping]] |
| Exact vault law | [[SCHEMA.md]] |

## Router Rules

```text
KICKSTART / today / leverage / what should I do
  -> [[duc-os/kickstart]]

Identity / psychology / communication fit
  -> [[duc-os/identity]]

Life map / past proof / leverage edge / how close to escape
  -> [[duc-os/escape-velocity-map]]

How to escape / gates / phases / anti-traps
  -> [[duc-os/escape-route]]

Development tree / weekly compounding machines / automation priority
  -> [[duc-os/leverage-development-tree]]

Long plan / escape velocity / social visibility / founder path
  -> [[duc-os/long-arc]]

Current focus / active projects / next likely move
  -> [[duc-os/current]]

Code, debugging, implementation, technical learning
  -> [[development]] -> [[wiki/operations/detect-operation]]

Vault structure, logs, propagation, branch placement
  -> [[vault-keeping]]

Named project work
  -> [[briefing]] dashboard -> project README
```

## Briefing Boundary

[[briefing]] remains useful, but it is now a dashboard under Duc OS. It does not own the personality wrapper or deep context. It should stay compact: active projects, current focus, pending, and official router pointers.

## Context Boundary

`context/` is now compatibility and hot-start cache, not the deep authority layer.

```text
context/hot.md
  -> temporary startup cache

context/me.md
context/goals.md
context/now.md
context/kickstart.md
  -> redirect stubs into Duc OS
```

## Related

- [[duc-os/identity]]
- [[duc-os/escape-velocity-map]]
- [[duc-os/escape-route]]
- [[duc-os/leverage-development-tree]]
- [[duc-os/long-arc]]
- [[duc-os/current]]
- [[duc-os/kickstart]]
- [[duc-os/engines]]
- [[duc-os/session-protocol]]
- [[briefing]]
- [[development]]
- [[vault-keeping]]

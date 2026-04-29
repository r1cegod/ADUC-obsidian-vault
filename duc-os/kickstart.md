---
type: note
title: Duc OS Kickstart
created: '2026-04-29'
updated: '2026-04-29'
tags:
  - context
  - plan
  - workflow
status: active
lang: en
feeds_into:
  - duc-os.md
  - context/hot.md
---
> **TL;DR**: Live KICKSTART control surface: current mission is to build Duc OS and wrapper wiring, while Raven Tier 2 stays parked as future work.

## Growth Contract
- Parent branch: [[duc-os]]
- Node role: leaf
- First parent link: [[duc-os]]
- Growth trigger: split only if multiple concurrent daily plans need separate project-local execution files.
- Forbidden contents: raw journaling, motivational notes, complete project roadmaps, and detailed implementation logs.
- Source/evidence boundary: this page holds the live execution control surface; durable strategy belongs in [[duc-os/long-arc]] and project detail belongs under project branches.

## Today

- Date: 2026-04-29
- Plan state: LOCKED
- Mission: Build Duc OS as the vault meta-router and wire the agent wrappers to it.
- Available block: unknown
- Hard constraints: do not move Raven backend implementation today; do not delete context files; keep wrappers thin.
- Last update reason: Duc clarified that the highest-leverage move is a personality wrapper and actual operating domain that can own all routers.

## Discussion Notes

- Duc is not missing motivation; he is missing clarification under high ambition.
- Duc OS should acknowledge past proof, see the future arc, identify the leverage gap, and choose today's move.
- The first-screen factory map for this is [[duc-os/escape-velocity-map]].
- The executable route for "how do I escape?" is [[duc-os/escape-route]].
- The weekly development tree for "what machines do I build?" is [[duc-os/leverage-development-tree]].
- Duc OS is above [[briefing]], [[development]], [[vault-keeping]], project READMEs, and operation leaves.
- The future UI should render Duc OS; the domain/kernel comes first.
- Raven Tier 2 is parked. It remains a valid next technical foundation after the operating layer is stable.

## Execution Stack

| Order | Outcome | Label | Next physical action | Done signal |
|---|---|---|---|---|
| 1 | Create Duc OS domain | EXECUTE | Add root hub and six leaves under `duc-os/` | Hub and leaves exist with Growth Contracts |
| 2 | Hard-move context authority | EXECUTE | Replace old context files with redirect stubs | `context/me`, `goals`, `now`, `kickstart` point to Duc OS |
| 3 | Wire wrappers | EXECUTE | Update vault `AGENTS.md`, `CLAUDE.md`, and Raven repo `AGENTS.md` | Fresh startup routes to Duc OS first |
| 4 | Update routers and schema | EXECUTE | Update `briefing`, `SCHEMA`, `index`, and hot cache | Duc OS is registered as root meta-router |
| 5 | Verify and log | AUDIT | Search links/routes and update day log | Routing simulation passes |

## Drift Guards

- Main lane: Duc OS migration and wrapper wiring.
- Must not chase: Raven Tier 2 code, UI app, channel ranking, social automation, or broad vault refactor.
- Checkpoint: stop after wrappers, index, schema, redirects, and log are coherent.

## Parking Lot

- Raven Tier 2 transcript-based synthesis - valid next technical lane after Duc OS.
- Full UI for Duc OS - build after the domain shape proves useful in sessions.
- Channel rankings and multi-source Raven modes - later Raven expansion.
- Social media content engine - later distribution engine under [[duc-os/engines]].

## Closeout

- shipped: Duc OS root hub, six Duc OS leaves, [[duc-os/escape-velocity-map]], context redirect stubs, wrapper rewiring, dashboard/schema/index/propagation updates, and Raven repo AGENTS pointer.
- learned: Duc OS is not a motivation layer; it is a meta-router and clarification kernel.
- next restart point: read [[duc-os]] first, then use [[duc-os/current]] or [[duc-os/kickstart]] to choose the next route.

## Related

- [[duc-os]]
- [[duc-os/current]]
- [[duc-os/engines]]
- [[duc-os/session-protocol]]
- [[wiki/operations/kickstart-operation]]
- [[projects/raven/notes/raven-current-context]]

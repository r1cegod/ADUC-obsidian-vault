---
type: project
title: Wynncraft Assistant
created: '2026-04-26'
updated: '2026-04-26'
tags:
  - wynncraft
  - project/wynncraft
status: active
lang: en
priority: low
feeds_into:
  - briefing.md
  - context/now.md
---
> **TL;DR**: Time-boxed Wynncraft assistant project: preserve fun by letting the vault carry builds, sources, route decisions, and next-session strategy.

## Growth Contract
- Parent branch: [[briefing.md]] and [[context/now]] Active Projects
- Node role: project root router
- First parent link: [[briefing.md]]
- Growth trigger: create a child hub only when one route has 3+ real notes or repeated source pulls.
- Forbidden contents: raw scraped dumps, unverified meta claims, grind logs, and full automation plans unless Duc explicitly promotes them.
- Expected child types: compiled strategy notes, build candidates, source maps, patch-impact reports, and raw/evidence pointers under `projects/wynncraft/sources/`.

## Project Shape

```text
projects/wynncraft/README.md
  -> [[projects/wynncraft/notes/wynncraft-player-profile|Wynncraft Player Profile]]
  -> [[projects/wynncraft/notes/wynncraft-search-operations|Wynncraft Search Operations]]
  -> [[projects/wynncraft/notes/wynncraft|Wynncraft Operating Sheet]]
  -> [[projects/wynncraft/sources/README|Wynncraft Sources And Evidence]]
```

This is not a main life project. It is a leisure-control system: the assistant does research, keeps the source map current, and turns the game into bounded decisions.

## Operating Rule

```text
user plays
assistant researches
vault remembers
```

Default loop:
1. Duc says current class, level, goal, and pain point.
2. Assistant pulls current sources when the question can drift.
3. Assistant gives one recommended action path, not a giant option dump.
4. Durable decisions go into [[projects/wynncraft/notes/wynncraft]].

## Main Routes

| Need | Open |
|---|---|
| Remember Duc's playstyle and optimization personality | [[projects/wynncraft/notes/wynncraft-player-profile]] |
| Run any Wynncraft research without drift | [[projects/wynncraft/notes/wynncraft-search-operations]] |
| What should I do next? | [[projects/wynncraft/notes/wynncraft]] |
| Which class/build/source should we trust? | [[projects/wynncraft/sources/README]] |
| Raw seed doc from `/home/r1ceg/wynncraft.md` | [[projects/wynncraft/sources/README]] |

## Scope

In scope:
- class choice, leveling route, builds, gear transitions, economy/source checks, mod/QoL recommendations, patch drift checks
- current-community scans using web/Reddit/forums when advice might be stale
- compact strategy sheets that prevent wasted playtime

Out of scope:
- in-game automation or botting
- full API/data platform unless explicitly promoted later
- unlimited min-maxing before Duc has a concrete character state

## Related

- [[projects/wynncraft/notes/wynncraft]]
- [[projects/wynncraft/sources/README]]
- [[briefing.md]]
- [[context/now]]

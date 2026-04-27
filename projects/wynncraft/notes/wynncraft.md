---
type: note
title: Wynncraft Operating Sheet
created: '2026-04-26'
updated: '2026-04-26'
tags:
  - wynncraft
  - project/wynncraft
  - workflow
status: active
lang: en
feeds_into:
  - projects/wynncraft/README.md
---
> **TL;DR**: Play Wynncraft through a bounded route: quest-first progression, Mage or Warrior as low-regret first class, Wynntils only if QoL helps, and no deep build min-maxing until a concrete character state exists.

## Growth Contract
- Parent branch: [[projects/wynncraft/README]]
- Node role: compiled strategy note
- First parent link: [[projects/wynncraft/README]]
- Growth trigger: split into build, leveling, economy, or endgame notes after 3+ real decisions accumulate in that route.
- Forbidden contents: raw source dumps, permanent build claims without patch date, and full API codex design unless promoted from the source lane.
- Source/evidence boundary: citations and source freshness live in [[projects/wynncraft/sources/README]]; this note holds current decisions.

## Current Player Target

```text
primary mode: solo
chosen class: Mage
preference: strongest practical route
constraint: Duc knows little about Wynncraft, so assistant leads the decision funnel
interpretation of strongest: survives solo content, clears efficiently, scales into endgame, and avoids high-regret early investment
profile: [[projects/wynncraft/notes/wynncraft-player-profile]]
research rule: start every research run from [[projects/wynncraft/notes/wynncraft-search-operations]]
```

## Mission

```text
Wynncraft interest
  -> preserve fun
  -> outsource research
  -> avoid blind grind
  -> play in bounded sessions
```

This project exists because the failure mode is obvious: the game becomes a research rabbit hole before it becomes play. The assistant owns research compression.

## Current Baseline

- Current patch era: 2.2 / Fruma Expansion. Search results list Version 2.2.0 with release date 2026-04-04 and Fruma as level 105-120 endgame content.
- Core game loop for a new/returning player: quests first, then dungeons/world events/raids/lootruns when level-appropriate.
- Endgame is optional grind/min-max. Community sentiment from April 2026 says normal progression is much less grindy than Hypixel SkyBlock, while endgame wealth/build chasing can become grindy.

## Default Recommendation

Chosen route:

```text
Pick Mage first.
Reason: range + sustain + teleport + endgame relevance.
Alternative held in reserve: Warrior if Mage feels too passive or caster-heavy.
Avoid first-main Shaman/Assassin for the initial optimized solo route.
```

Community current signal from April 2026 beginner threads repeatedly points to Mage or Warrior as low-regret beginner picks. Archer/Assassin can be fun but are more preference-sensitive. Shaman has crowd control and healing tools but is a higher-friction first route for many players.

## Play Route

### First Character

```text
Level 1-40
  -> follow quests in order
  -> use Content Book as task source
  -> replace gear often
  -> do not care about perfect builds

Level 40-80
  -> keep quest-first
  -> use dungeons/world events only when they solve level gaps or boredom
  -> start asking assistant for gear transitions if damage/survival stalls

Level 80+
  -> begin build-source checks before expensive gear decisions
  -> avoid crafting/market spending without current-patch validation

Level 105-120
  -> Fruma/endgame route
  -> validate every build against current 2.2 sources
```

### Session Budget

Default session shape:

```text
10 min: ask assistant what to do from current state
60-90 min: play one route
5 min: report level/class/pain point/drop/build question
```

Stop condition: if the next action requires browsing builds for more than 10 minutes, ask the assistant instead.

## Build Policy

No abstract build optimization yet. A useful build request must include:

```text
class:
level:
archetype or preferred playstyle:
current weapon:
problem: damage / survival / mobility / mana / boss / dungeon / Fruma
budget: none / cheap / can buy / can craft
```

Build confidence ladder:

```text
official mechanics and patch notes
  -> recent forum build thread
  -> recent Reddit/Discord sentiment
  -> Wynnbuilder link with patch-compatible tree
  -> assistant recommendation
```

Reject stale builds when:
- pre-Fruma or pre-2.2 without update notes
- depends on changed ability tree/AP assumptions
- assumes old set rarity, old powders, or old item behavior
- recommends expensive crafting without current confirmation

## Mods/QoL

Default:

```text
Vanilla is enough to start.
Add Wynntils if map/QoL friction appears.
Do not stack modpacks until the base game loop is understood.
```

Reason: QoL can save time, but a giant modpack can turn first contact into configuration work. Time budget matters more than perfect setup.

## Assistant Tasks

When asked, assistant should handle:
- current build search and stale-source filtering
- class/archetype comparison
- quest/leveling bottleneck diagnosis
- gear transition suggestions
- Fruma/endgame source refresh
- compact route sheet for the next play session

Assistant should not:
- automate gameplay
- suggest a full API/data codex unless Duc promotes the project
- produce massive guide dumps when one next action is enough

## Open Inputs Needed From Duc

```text
current class:
current level:
solo or with friends:
preferred feel: safe / fast / high-skill / lazy / big damage
hard time budget per week:
```

## Related

- [[projects/wynncraft/README]]
- [[projects/wynncraft/notes/wynncraft-player-profile]]
- [[projects/wynncraft/notes/wynncraft-search-operations]]
- [[projects/wynncraft/sources/README]]

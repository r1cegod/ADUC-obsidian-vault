---
type: note
title: Wynncraft Search Operations
created: '2026-04-26'
updated: '2026-04-26'
tags:
  - wynncraft
  - project/wynncraft
  - workflow
  - docs
status: active
lang: en
feeds_into:
  - projects/wynncraft/README.md
  - projects/wynncraft/sources/README.md
  - projects/wynncraft/notes/wynncraft.md
---
> **TL;DR**: Project-local search operations for Wynncraft research runs: choose the lane first, pull sources in a fixed order, score freshness, then write the compiled decision back into the project.

## Growth Contract
- Parent branch: [[projects/wynncraft/README]]
- Node role: project-local operation note
- First parent link: [[projects/wynncraft/README]]
- Growth trigger: split a search lane only when it accumulates 3+ repeated runs or source notes.
- Forbidden contents: raw copied source dumps, one-off search results with no decision, and global vault operation law.
- Source/evidence boundary: source URLs and freshness notes route through [[projects/wynncraft/sources/README]]; final play decisions route through [[projects/wynncraft/notes/wynncraft]].

## Rule

Every Wynncraft research run starts by checking [[projects/wynncraft/notes/wynncraft-player-profile]], then selecting one lane.

```text
question
  -> check player profile
  -> choose search lane
  -> pull sources in fixed order
  -> reject stale/conflicting advice
  -> compile one recommendation
  -> update source map or operating sheet when durable
```

## Top-Level Search Lanes

| Lane | Use When | Output |
|---|---|---|
| Patch Baseline | Any build/meta answer could be affected by current version | current patch facts + stale-risk flags |
| Solo Mage Route | Duc asks what to play, level, or build next on the chosen Mage route | one next-session plan |
| Build Search | Duc asks for gear, archetype, damage, survivability, bossing, raids, or endgame | build candidate table + recommendation |
| Leveling/Quest Route | Duc is stuck, underleveled, bored, or unsure what content to do | compact 1-2 hour route |
| Economy/Gear Cost | A recommendation needs buying, crafting, market, mythic, or expensive gear | cheap/medium/expensive options with risk |
| Mod/QoL Setup | Friction is map, UI, performance, keybinds, or install setup | minimal install/change list |
| Source Drift Audit | Existing advice conflicts or feels old | freshness verdict and what to replace |

## Source Mix By Request Type

Do not use one universal search order. Different Wynncraft questions need different evidence shapes.

| Request Type | Search Mix | Why |
|---|---|---|
| Build/meta | community-heavy first -> official confirmation | Forums/Reddit/Discord-like sources reveal what people actually run; official wiki confirms mechanics, patch changes, item rules, and stale risk. |
| Patch facts | official first -> community interpretation second | Patch state is factual; community helps interpret impact only after facts are locked. |
| Leveling route | official/wiki route + recent community sanity check | Level ranges and systems are stable-ish, but efficient route advice can drift. |
| Gear/economy | market/community first -> official item mechanics second | Price and availability are community/economy signals; item requirements and behavior need official confirmation. |
| Class/archetype choice | community experience + official class mechanics | Player experience explains feel; official pages explain actual tools and constraints. |
| Mods/QoL | official mod pages/current project pages first -> community setup advice second | Install/version safety matters more than opinions. |
| Source drift audit | newest official + newest community conflict check | The goal is to detect whether old advice survived current patch reality. |

## Default Source Order

Use this only when no request-specific lane overrides it:

```text
1. official current patch / wiki.gg / API docs
2. official forum changelog or class-build forum
3. current Reddit/community sentiment
4. build tools such as Wynnbuilder links
5. local seed doc /home/r1ceg/wynncraft.md
```

## Freshness Test

Reject or down-rank a source when:
- it predates Wynncraft 2.2 / Fruma and makes balance/build claims
- it assumes old item behavior, old set rarity, old powder rules, or old ability point limits
- it gives endgame advice without a patch date or build link
- it optimizes theoretical DPS while failing solo survivability
- it recommends expensive items before Duc has a concrete class/level/budget state

## Lane Details

### Patch Baseline

Search pattern:
```text
Wynncraft latest version official wiki
Wynncraft 2.2 patch notes official forums
Wynncraft Fruma patch item ability changes
```

Compile:
```text
current version:
relevant changes:
build-impact risk:
source confidence:
```

### Solo Mage Route

Source shape:
```text
community experience first
  -> solo viability, pain points, beginner traps
official mechanics second
  -> Mage spells, archetype mechanics, patch constraints
route synthesis third
  -> one play path for Duc's current level
```

Search pattern:
```text
Wynncraft 2.2 Mage solo build beginner
Wynncraft Fruma Mage Light Bender solo
Wynncraft Mage Riftwalker Arcanist solo 2.2
site:reddit.com/r/WynnCraft Mage solo Fruma
site:forums.wynncraft.com Mage build 2.2 solo
Wynncraft wiki Mage Ability Tree 2.2
```

Minimum evidence:
```text
2+ current community solo signals
1 official Mage/archetype/mechanics confirmation
1 patch baseline check when the answer touches endgame or expensive gear
```

Compile:
```text
current level:
archetype:
gear priority:
spell/ability priority:
next 60-90 min route:
risk:
```

### Build Search

Source shape:
```text
community breadth first
  -> forums Class Builds, Reddit, current build communities, multiple examples
mechanics confirmation second
  -> official wiki/API/patched item and ability pages
build tool validation third
  -> Wynnbuilder link, level/AP/item requirements, cost reality
```

Search pattern:
```text
site:forums.wynncraft.com/forums/class-builds.100 Mage <archetype> 2.2
site:forums.wynncraft.com Mage <archetype> build Fruma
site:reddit.com/r/WynnCraft Mage build Fruma 2.2
Wynncraft Mage <archetype> build community 2.2
Wynnbuilder Mage <archetype> 2.2
Wynncraft wiki Mage <archetype> ability tree item <key item>
```

Minimum evidence:
```text
3+ community candidates when available
1+ current official mechanic/patch confirmation
1 build-tool or item-requirement sanity check when gear-specific
```

Compile:
```text
candidate:
source date:
level requirement:
cost class: cheap / medium / expensive / mythic
solo safety:
damage:
mobility:
stale risk:
verdict:
```

### Leveling/Quest Route

Search pattern:
```text
Wynncraft 2.2 leveling guide quests
Wynncraft level <range> Mage quest route
Wynncraft Content Book leveling dungeons world events
```

Compile:
```text
current level:
recommended content:
skip/avoid:
gear check:
stop condition:
```

### Economy/Gear Cost

Search pattern:
```text
Wynncraft market <item>
Wynncraft <item> price 2.2
Wynncraft Mage budget build 2.2
```

Compile:
```text
item/build:
why needed:
price risk:
cheap substitute:
when to buy:
when to ignore:
```

### Mod/QoL Setup

Search pattern:
```text
Wynncraft Wynntils current version
Wynncraft modpack beginner 2026
Wynncraft performance mods Fabric
```

Compile:
```text
install only if:
minimum setup:
do not install:
why:
```

### Source Drift Audit

Search pattern:
```text
<claim> Wynncraft 2.2
<item/archetype> Fruma nerf buff patch
site:forums.wynncraft.com <item/archetype> 2.2
site:reddit.com/r/WynnCraft <item/archetype> Fruma
```

Compile:
```text
claim:
old source:
newer evidence:
keep / revise / discard:
replacement decision:
```

## Writeback Rules

After each meaningful research run:
- update [[projects/wynncraft/sources/README]] if a reusable source was found
- update [[projects/wynncraft/notes/wynncraft]] if the recommendation changes the play route
- create a child note only when the same lane has repeated pressure
- log durable route changes in `sources/log/days/YYYY-MM-DD.md`

## Related

- [[projects/wynncraft/README]]
- [[projects/wynncraft/notes/wynncraft-player-profile]]
- [[projects/wynncraft/notes/wynncraft]]
- [[projects/wynncraft/sources/README]]

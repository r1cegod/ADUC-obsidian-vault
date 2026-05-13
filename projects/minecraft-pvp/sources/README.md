---
type: note
title: Minecraft PvP Sources And Evidence
created: '2026-05-03'
updated: '2026-05-03'
tags:
  - minecraft
  - pvp
  - project/minecraft-pvp
  - docs
status: active
lang: en
feeds_into:
  - projects/minecraft-pvp/README.md
---
> **TL;DR**: Source lane for the modern PvP project: raw roadmap location, local CurseForge instance evidence, and future server/rule validation.

## Growth Contract
- Parent branch: [[projects/minecraft-pvp/README]]
- Node role: source lane
- First parent link: [[projects/minecraft-pvp/README]]
- Growth trigger: split into server-rules, client-setup, clip-analysis, or version-validation sources after 3+ entries accumulate.
- Forbidden contents: compiled training doctrine, unverified advice promoted as current rules, hacked-client instructions, and Wynncraft build/quest sources.
- Source/evidence boundary: this page indexes evidence; compiled decisions live in [[projects/minecraft-pvp/notes/minecraft-pvp-operating-sheet]].

## Local Source Files

```text
/home/r1ceg/minecraft_aerial_lancer_pvp_roadmap.md
  -> gathered roadmap for Aerial Lancer PvP identity, setup, training phases, and first 14 days.

/mnt/c/Users/r1ceg/curseforge/minecraft/Instances/Wynncraft
  -> existing CurseForge instance reviewed for reuse/fork decision.
```

## Roadmap Digest

The gathered roadmap defines the final style as:

```text
Aerial Lancer
  -> spear controls X/Z
  -> mace controls Y-axis burst
  -> elytra controls map tempo
  -> sword/axe/SMP fundamentals keep the build alive when grounded
```

Training order:

```text
Sword movement and spacing
  -> axe + shield mindgame
  -> SMP/UHC utility
  -> mace mechanics
  -> spear spacing and speed control
  -> elytra combat
  -> full integration
```

The roadmap explicitly rejects Crystal PvP as the main identity and warns against style addiction.

## CurseForge Evidence

Inspected instance:

```text
path: /mnt/c/Users/r1ceg/curseforge/minecraft/Instances/Wynncraft
minecraft: 1.21.11
loader: fabric-0.19.2-1.21.11
allocated memory: 7840 MB
```

Observed active mod files include:

```text
fabric-api
sodium
sodium-extra
lithium
entityculling
immediatelyfast
ferritecore
krypton
modernfix
c2me
badoptimizations
modmenu
betterf3
notenoughanimations
skinlayers3d
wynntils
wynnventory
voices-of-wynn
wynnanimated
```

Disabled but present:

```text
xaerominimap
xaeroworldmap
zoomify
entity model/texture features
polytone
```

Key option evidence:

```text
VSync: true
fullscreen: true
max FPS: 260
render distance: 8
simulation distance: 6
particles: decreased
clouds: off
entity shadows: false
view bobbing: true
toggle sprint: false
attack indicator: crosshair
resource packs: none
```

## Public Server Check

Checked on 2026-05-03:

```text
anchor server: mcpvp.club
public listing found: Modrinth PvP Club server page
recommended version: Java 1.21.11
supported versions: 1.21.2-1.21.11
regions listed: NA Ashburn, EU Frankfurt, AS Singapore, AU Sydney
public Discord listing found: official PvP Club Discord server
```

Public allowed-mods/rules detail was not found in the quick web check. Treat client legality as unverified until Discord/in-game rules are checked.

Additional public signal found: a 2026-04-10 Reddit thread in r/MinecraftPVP mentions someone using a custom spear PvP kit on PvP Club, and a commenter says several kits let spear work but are not the most popular. This makes spear practice plausible on mcpvp.club, but not yet verified as a standard public queue.

## Validation Needed

Before treating setup guidance as current:

```text
- confirm allowed/disallowed client mods from mcpvp.club Discord or in-game rules
- confirm whether spear/mace/elytra kits exist on mcpvp.club
- confirm resource-pack legality
- confirm whether replay/zoom/minimap/toggle sprint are allowed
```

## Related

- [[projects/minecraft-pvp/README]]
- [[projects/minecraft-pvp/notes/minecraft-pvp-operating-sheet]]
- [[projects/minecraft-pvp/notes/minecraft-pvp-first-14-days]]
- [[projects/wynncraft/sources/README]]

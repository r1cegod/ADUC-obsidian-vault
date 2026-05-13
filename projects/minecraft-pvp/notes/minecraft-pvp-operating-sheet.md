---
type: note
title: Minecraft PvP Operating Sheet
created: '2026-05-03'
updated: '2026-05-03'
tags:
  - minecraft
  - pvp
  - project/minecraft-pvp
  - workflow
status: active
lang: en
feeds_into:
  - projects/minecraft-pvp/README.md
---
> **TL;DR**: Train modern PvP as a bounded Aerial Lancer stack: sword stability -> SMP survival IQ -> mace/spear mechanics -> elytra tempo control.

## Growth Contract
- Parent branch: [[projects/minecraft-pvp/README]]
- Node role: compiled strategy note
- First parent link: [[projects/minecraft-pvp/README]]
- Growth trigger: split into setup, training log, server validation, or clip-analysis notes after 3+ real decisions accumulate in that lane.
- Forbidden contents: raw source dumps, montage-only tech as doctrine, unverified server claims, Wynncraft-specific config detail, and client modifications that violate server rules.
- Source/evidence boundary: raw roadmap and instance evidence live in [[projects/minecraft-pvp/sources/README]].

## Identity

```text
final style: Aerial Lancer
core stack: sword/axe fundamentals + SMP utility + spear + mace + elytra
training budget: 1-2 hours/day
first constraint: stability before style
```

The roadmap's center is correct: spear/mace/elytra are force multipliers, not substitutes for spacing, cooldown rhythm, tracking, panic control, hotbar control, and terrain judgment.

## Current Training Stack

Canonical progression: [[projects/minecraft-pvp/notes/minecraft-pvp-six-stage-progression]]

```text
1. Sword Spacing Kernel
2. Sword Fight Stability
3. Hotbar + Defensive Utility
4. SMP Utility Fighting
5. Mace / Spear Layer
6. Aerial Lancer Integration
```

## Daily Session Template

Default 1-2 hour structure:

```text
10m warmup / aim / movement
40-70m main gamemode reps
10-20m focused weakness reps
10m review 1-2 fights or write failure label
```

60-minute version:

```text
5m warmup
40m reps
10m review
5m note
```

120-minute version:

```text
10m warmup
80m reps
20m review
10m note
```

The failure note must answer one question:

```text
What killed me most today: spacing, aim, panic, hotbar, terrain, resource timing, or bad commit?
```

## Current Phase

Duc is basically fresh in PvP, so start at Stage 1 without ego inflation.

```text
current stage: Stage 1 - Sword Spacing Kernel
main gamemode: sword duels / basic kit duels
daily target: 10-20 sword duels, 1 reviewed clip, 1 failure label
current failure label from first review: spacing + bad commit
```

Pass gate:

```text
2 sessions in a row:
- 10+ sword fights each session
- 60%+ fights without hard W-key collapse
- opponent is not constantly filling more than 40% of screen
- Duc can name why he lost
```

Do not advance because novelty hunger appears. Advance when the pass signal is real.

## Setup Decision

Recommended structure:

```text
Wynncraft profile
  -> keep as Wynncraft RPG/QoL profile

Main PvP profile
  -> custom Fabric 1.21.11 profile
  -> clean competitive mods
  -> PvP resource pack stack
  -> PvP keybinds/options
  -> no all-in-one combat client modules

Optional secondary client
  -> Lunar or Badlion only if mcpvp.club rules explicitly permit and convenience matters

Optional lab profile
  -> private worlds/maps/replay/drills only
```

Recommended PvP mod stack:

```text
Core/performance:
- Fabric API
- Sodium
- Sodium Extra
- Lithium
- Entity Culling
- ImmediatelyFast
- FerriteCore
- Krypton
- Mod Menu
- BetterF3

Beginner-safe PvP utility, rule-check first:
- Toggle Sprint or Visible Toggle Sprint
- uku's Armor HUD or guy's Armor HUD
- Status Effect Timer or Status Effect HUD

Avoid unless explicitly allowed:
- Zoom
- Replay Mod
- Minimap/worldmap
- Freelook/snaplook
- macros, auto-totem, triggerbot, ESP, x-ray, radar, crystal/anchor automation
```

Complete setup decision:

```text
Launcher/client:
- Main: custom Fabric 1.21.11 profile in CurseForge or Prism Launcher
- Secondary: Lunar or Badlion only for convenience after rules check
- Do not use cheat/utility clients advertising AutoTotem, ESP, macros, triggerbot, x-ray/radar, crystal/anchor automation, or bypass modules

Profile name:
- Minecraft PvP - Clean

Core/performance mods:
- Fabric API
- Sodium
- Sodium Extra
- Reese's Sodium Options if available for 1.21.11
- Lithium
- Entity Culling
- ImmediatelyFast
- FerriteCore
- Krypton
- Mod Menu
- BetterF3
- NoChatReports if allowed

PvP visibility/HUD mods:
- Toggle Sprint or Visible Toggle Sprint, if allowed
- uku's Armor HUD or guy's Armor HUD
- Status Effect Timer or Status Effect HUD

Resource pack stack:
- Base: Default Minecraft, no shader
- All-in-one visibility layer: SwiftBoost PvP or Small Items+
- Minimal visibility layer: Low On Fire
- Sword layer if needed: LowSword, Short Blade Sword, or Short Swords
- Totem layer if needed: Totem Lite or Smaller Totem
- Backup full pack: PvP Scroutopia

Unavailable/rejected:
- PVP Reforged was not available for Duc's setup path and should not be treated as the primary recommendation.

Settings:
- VSync off
- fullscreen on
- max FPS 120-180 on 60 Hz monitor
- render distance 8-10
- simulation distance 6
- particles decreased/minimal
- clouds off
- entity shadows off
- view bobbing off
- attack indicator crosshair
- FOV 90-95 to start
- raw mouse input on
- DPI 850, polling 1000 Hz
```

Use custom Fabric as main. Lunar/Badlion are convenience secondaries, not the main lab.

## CurseForge Wynncraft Review

Existing instance inspected:

```text
path: /mnt/c/Users/r1ceg/curseforge/minecraft/Instances/Wynncraft
loader: Fabric 0.19.2
minecraft: 1.21.11
allocated memory: 7840 MB
played count: 5
last played: 2026-05-02
```

Useful overlap for PvP:
- Fabric 1.21.11 base is aligned with the roadmap's modern-version direction.
- Sodium, Lithium, Entity Culling, ImmediatelyFast, FerriteCore, Krypton, Mod Menu, Sodium Extra, C2ME, ModernFix, and BetterF3 are broadly useful.

Wynn-specific or PvP-irrelevant weight:
- Wynntils
- Wynnventory
- Voices of Wynn
- WynnAnimated
- Extreme Sound Muffler unless intentionally used
- disabled Xaero map/worldmap and Zoomify should stay disabled for strict PvP unless a server explicitly allows them.

Settings mismatched for serious PvP:
- VSync is on.
- View bobbing is on.
- Toggle sprint is off.
- No PvP resource packs are active.
- FOV is default-ish and not yet deliberately locked for PvP.
- Wynn keybinds occupy combat-relevant keys: mount horse on `R`, spell cast on `Z`, item sharing on `F5/F6`.

Decision:

```text
Do not modify the Wynncraft instance in place.
Duplicate or create a new CurseForge/Prism Fabric profile named something like Minecraft PvP - Clean.
Strip Wynn-specific mods from the PvP copy.
Then tune options/keybinds/resource packs for combat.
```

Reason: in-place mutation creates context collision. Wynncraft needs RPG overlays and comfort; PvP needs low delay, legality, visual clarity, and repeatable input muscle memory.

## Missing Context Report

Known inputs from Duc:

```text
target anchor server: mcpvp.club
likely FPS: about 120
monitor: 60 Hz
mouse: Logitech G502 HERO
DPI: 850
polling rate: 1000 Hz
Windows mouse acceleration: probably off
PvP baseline: basically fresh beginner
```

Need from Duc before the setup can be fully locked:

```text
1. Allowed-client policy for mcpvp.club:
   Fabric mods, toggle sprint, zoom, replay, minimap, freelook, hitbox/debug, resource packs.

2. Current PvP skill baseline:
   sword duel win/loss feel, biggest failure, hotbar comfort, panic pattern.

3. Keyboard/mouse constraints:
   reachable keys, side mouse buttons, preferred sprint/sneak/offhand/perspective binds.

4. Whether spear play is available in public queues, party/custom kits, or only niche/private kits on mcpvp.club.

5. Whether daily sessions are closer to 60m or 120m on weekdays.

6. Confirm Windows mouse acceleration is actually disabled, not just assumed.
```

## Implemented PvP Profile

Created/configured on 2026-05-03:

```text
CurseForge profile folder: /mnt/d/curse/Instances/pvpp
CurseForge profile name: Minecraft PvP - Clean
Minecraft: 1.21.11
Loader: Fabric 0.19.2
Memory: 6144 MB override
Main resource packs: PVP_REFORGED.zip, LowSword.zip, Small Low Totem.zip
```

Installed mod stack:

```text
BadOptimizations
BetterF3
C2ME disabled as .jar.disabled
Cloth Config
Debugify
Dynamic FPS
Entity Culling
Fabric API
FastQuit
FerriteCore
Fzzy Config
ImmediatelyFast
Krypton
Lithium
MixinTrace
ModernFix
Mod Menu
More Culling
NoChatReports
Noisium
Placeholder API
Reese's Sodium Options
Sodium
Sodium Extra
Sodium Shadowy Path Blocks
Status Effect Timer
ukulib
uku's Armor HUD
Visible Toggle Sprint
YetAnotherConfigLib
```

Applied options:

```text
VSync: off
Fullscreen: on
Max FPS: 180
Render distance: 8
Simulation distance: 6
Particles: decreased
Clouds: off
Entity shadows: off
View bobbing: off
Toggle sprint: on
FOV: 0.6 options value, intended 90-95-ish feel
Raw mouse input: on
Resource packs enabled
```

## Mouse And Hotbar Setup

Known hardware:

```text
mouse: Logitech G502 HERO
DPI: 850
polling: 1000 Hz
monitor: 60 Hz
PvP baseline: fresh beginner
```

Principle:

```text
Keyboard owns weapons and repeated combat rhythm.
Mouse thumb buttons own panic tools and fast state switches.
Do not put the whole hotbar on the mouse.
```

Recommended G502 bindings:

```text
Left click: attack
Right click: use / shield / interact
Middle click: pick block or unbound if accidental clicks happen
Scroll up/down: normal hotbar scroll, but do not rely on it in combat
Thumb forward: swap offhand
Thumb back: perspective toggle
DPI shift/sniper button: hotbar slot 8 or pearl/panic slot, if comfortable
Extra top buttons near left click: optional hotbar 6 and 7 later, not day one
DPI cycle buttons: leave as DPI controls or disable in G Hub to prevent accidental sensitivity changes
```

Beginner hotbar:

```text
1 Sword
2 Axe
3 Bow/Crossbow
4 Blocks
5 Water/Lava/Utility
6 Food/Healing
7 Pearl
8 Shield/Totem
9 Gap/Extra
Offhand: Shield in duels, Totem in SMP
```

Aerial Lancer future hotbar:

```text
1 Spear
2 Mace
3 Sword/Axe backup
4 Crossbow/Bow or Wind Charges
5 Rockets
6 Blocks
7 Pearls
8 Food/Healing
9 Water/Shield/Utility
Offhand: Totem by default in SMP
```

Keyboard binds:

```text
WASD: movement
Space: jump
Left Shift: toggle sprint
Left Ctrl: sneak
Q: perspective if not using mouse thumb back
Caps Lock: swap offhand if not using mouse thumb forward
R: free for future rockets/mount/action if not used by server
F: quick action only if not conflicting
G: drop item, or move drop away if accidental drops happen
```

Rule:

```text
First week: bind only offhand and perspective to mouse.
After panic drops, assign one thumb/sniper button to pearl or slot 7/8.
Do not bind spear/mace to mouse until the base hotbar stops collapsing.
```

Verification status:

```text
file layout verified
mod/resource pack downloads verified
dependency scan found only likely bundled/loader-internal warnings from C2ME/Dynamic FPS
not launch-tested by agent because launching Minecraft GUI is outside the current shell verification path
```

Fabulously Optimized merge:

```text
donor profile: /mnt/d/curse/Instances/Fabulously Optimized
target profile: /mnt/d/curse/Instances/pvpp
backup: /mnt/d/curse/Instances/pvpp_backup_before_fo_merge_20260504T110806Z
adopted: More Culling, FastQuit, Sodium Shadowy Path Blocks, Debugify, MixinTrace
adopted configs: moreculling.toml, fastquit.toml, sodium-shadowy-path-blocks-options.json, debugify.json
kept: Flashback, PvP HUD/utilities, PvP resource packs, PvP options/keybinds, C2ME disabled
skipped from donor: Iris/shader stack, Zoomify, Controlify, e4mc, visual resource-pack compatibility stack, cosmetic/cape/menu mods
reason: adopt FPS/stability gains without turning the PvP profile into a visual/client-convenience pack
```

Flashback review mod:

```text
local jar: Flashback-0.39.5-for-MC1.21.11.jar
location: /mnt/d/curse/Instances/pvpp/mods
metadata: client-side Fabric mod, version 0.39.5, Minecraft >=1.21.11, requires Fabric API
purpose: record fights for replay review, not cinematic rabbit-hole work during training time
rule status: allowed-mod status on mcpvp.club still unverified
```

Flashback review loop:

```text
1. Launch Minecraft PvP - Clean.
2. Confirm the main menu or Mod Menu shows Flashback.
3. Check Controls for Flashback keybinds and set one marker key if available.
4. Join mcpvp.club and play a short test fight.
5. Leave the server cleanly and wait for replay saving if prompted.
6. Open Flashback/replay viewer from the main menu.
7. Review only the death/engagement moments, not the whole session.
8. Write one failure label: spacing, aim, panic, hotbar, terrain, resource timing, or bad commit.
```

Frame-review workflow:

```text
See [[projects/minecraft-pvp/notes/minecraft-pvp-video-review-workflow]] for the claude-video/watch inspired method: MP4 -> frames/contact sheet -> focused dense review -> one failure label.
```

Review rule:

```text
For the first week, Flashback is for diagnosis only.
No cinematic editing, camera paths, or export work inside training time.
```

## Next Physical Move

```text
1. Open CurseForge.
2. Launch Minecraft PvP - Clean once.
3. If launch succeeds, join mcpvp.club.
4. Do not tune for more than 10 minutes.
5. Run Day 1-3 sword-only reps.
6. Write one failure note after the session.
```

## Related

- [[projects/minecraft-pvp/README]]
- [[projects/minecraft-pvp/notes/minecraft-pvp-six-stage-progression]]
- [[projects/minecraft-pvp/notes/minecraft-pvp-first-14-days]]
- [[projects/minecraft-pvp/sources/README]]
- [[projects/wynncraft/README]]

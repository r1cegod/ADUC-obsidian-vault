---
type: note
title: Minecraft PvP Review 2026-05-03 First Duels
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
  - projects/minecraft-pvp/notes/minecraft-pvp-video-review-workflow.md
  - projects/minecraft-pvp/notes/minecraft-pvp-operating-sheet.md
---
> **TL;DR**: First visual PvP review: Duc is not dying to missing advanced tech; the main beginner leaks are range discipline, straight-line commits, and getting too close after contact.

## Growth Contract
- Parent branch: [[projects/minecraft-pvp/notes/minecraft-pvp-video-review-workflow]]
- Node role: review report
- First parent link: [[projects/minecraft-pvp/notes/minecraft-pvp-video-review-workflow]]
- Growth trigger: merge patterns into the operating sheet after 3+ review reports show the same failure.
- Forbidden contents: raw frame dumps, cinematic notes, full transcript-style summaries, and server/mod setup details.
- Source/evidence boundary: source video is `/home/r1ceg/mc recording/2026-05-03T14_12_25.mp4`; extracted contact sheets are temporary analysis artifacts under `/tmp/mc_review*`.

## Source

```text
video: /home/r1ceg/mc recording/2026-05-03T14_12_25.mp4
duration: 2:03
resolution: 1280x720
fps: 60
review method: contact sheets plus dense segment sheets around visible trade windows
```

## Main Finding

```text
failure class: spacing + straight-line commit
secondary: over-close after contact
not the problem yet: advanced tech, attribute swapping, spear/mace, resource routes
```

Duc repeatedly holds distance, then enters in a fairly direct line. When contact happens, the fight sometimes collapses into very close range where the opponent fills the screen. That makes tracking, cooldown rhythm, and readjustment harder than necessary.

## What Went Right

- Duc kept visual contact with the opponent most of the fight.
- Crosshair was usually in the opponent's general body lane, not wildly lost.
- In later exchanges, Duc created more resets instead of only hard-running forward.
- Some hits landed after the opponent's health dropped through clear trade sequences, so the base hand-eye loop exists.

## Main Leaks

### 1. Range Entry Is Too Binary

```text
far -> direct approach -> sudden close scramble
```

Better pattern:

```text
far -> angle in -> stop at edge of hit range -> hit/check -> strafe out
```

### 2. Too Much Center-Line Commitment

Several approaches happen straight down the opponent's line. This gives the opponent easy timing: they only need to hold aim forward and punish the entry.

### 3. Over-Close Scramble

When the opponent gets huge on screen, Duc is too close. At that point the fight becomes panic tracking instead of controlled spacing.

### 4. Reset Distance Is Sometimes Too Large

After trades, Duc often backs out to far range. That is safe, but it resets pressure completely. The next step is learning medium range, not full disengage.

## Next Drill

For the next 2-3 sessions:

```text
Drill: edge-of-range sword duels
Rule: do not hard W-key into the opponent
Goal: touch hit range, land/check one swing, strafe out before face-to-face scramble
Metric: fewer moments where opponent fills more than 40% of screen
```

Session instruction:

```text
1. Queue sword duels.
2. Spend first minute only observing range.
3. Enter from slight left/right angle.
4. After each hit attempt, strafe out instead of holding W.
5. If opponent fills the screen, call it a spacing failure even if a hit lands.
```

## Failure Label

```text
primary label: spacing
secondary label: bad commit
next correction: edge-of-range control
```

## Related

- [[projects/minecraft-pvp/notes/minecraft-pvp-video-review-workflow]]
- [[projects/minecraft-pvp/notes/minecraft-pvp-operating-sheet]]
- [[projects/minecraft-pvp/notes/minecraft-pvp-first-14-days]]

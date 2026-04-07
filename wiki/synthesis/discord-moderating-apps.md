---
type: source-summary
title: "Discord Moderating Apps"
created: 2026-04-07
updated: 2026-04-07
tags: [discord, moderation, source-summary]
status: active
lang: en
source: "[[references/discord-moderating-apps]]"
---

> **TL;DR**: Discord treats apps as their own moderation surface, with separate controls for external apps, server-installed apps, command usage, activities, and bot permissions.

## Summary
This article is the strongest official source in the current batch for bot and app risk management. Discord separates server-installed apps from user-level external apps, then explains the control surface moderators can use: `Use External Apps`, `Use Application Commands`, `Use Activities`, command permissions, bot permissions, and AutoMod filtering. The most important subtlety is that blocking external apps from public use does not eliminate them entirely, because some can still reply privately in ephemeral messages. That means app policy is about visibility and risk reduction, not total elimination.

## Key Points
- App moderation needs its own permission model, not just generic role permissions
- External apps and installed apps behave differently and should not be treated as the same risk
- AutoMod can still help moderate content generated through app interactions

## Details
The article closes a real gap in the earlier Discord moderation corpus: bots are not just “trusted tools,” they are another attack and abuse surface. Moderators need to decide who can add apps, which roles can invoke commands, and whether external apps should be visible publicly at all. This makes the page central for communities that rely on translation, ticketing, fun commands, or automation from third-party apps.

## Related
- [[wiki/synthesis/discord-command-permissions]]
- [[wiki/synthesis/discord-moderation-domain]]

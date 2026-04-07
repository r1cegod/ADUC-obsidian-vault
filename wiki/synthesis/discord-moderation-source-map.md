---
type: synthesis
title: "Discord Moderation Source Map"
created: 2026-04-07
updated: 2026-04-07
tags: [discord, moderation, synthesis]
status: active
lang: en
---

> **TL;DR**: The main moderation source batch and the AI connection-pattern batch are now ingested; this page remains the routing map for what each source fills and which residual gaps still need better material.

## Overview
This is the search-layer companion to [[wiki/synthesis/discord-moderation-domain]]. The main source batch listed here was ingested on 2026-04-07, so this page now acts as both a provenance map and a guide to the remaining gaps.

### AI connection layer now covered
The corpus now also covers how to wire an already-created Discord app into an AI moderation backend:
- explicit invocation via Interactions
- passive intake via Gateway and justified intents
- bot-token vs OAuth2 identity split
- deferred responses for slow AI work
- classifier plus policy-agent backend layering

## Analysis
### Missing knowledge areas in the current corpus
- Offense taxonomy and sanction ladder: what behavior maps to warn, timeout, kick, ban, and permanent exclusion
- Appeals workflow: intake channel, ownership, turnaround, evidence requirements, recusal, and finality
- Evidence and audit standards: what to log, how long to keep it, who can view it, and how to review staff actions later
- Anti-raid and anti-alt operations: verification levels, rules screening, AutoMod depth, lockdown steps, and raid-response playbooks
- Moderator governance: team structure, escalation boundaries, handbook expectations, staffing growth, and burnout management
- Bot and app risk management: permission scoping, command scoping, external-app policy, token/security hygiene, and failure planning
- Content filtering design: regex, exception handling, multilingual policy, false-positive handling, and user-facing notices
- Ticket/report workflow: severity routing, closure standards, reporter privacy, and staff follow-through

### High-priority official docs
- Discord Safety Library: https://discord.com/moderation
- Safety Library guide with verification / AutoMod / 2FA guidance: https://discord.com/moderation/exam
- Verification Levels: https://support.discord.com/hc/en-us/articles/216679607-Verification-Levels
- AutoMod FAQ: https://support.discord.com/hc/en-us/articles/4421269296535-AutoMod-FAQ
- Rules Screening FAQ: https://support.discord.com/hc/en-us/articles/1500000466882-Rules-Screening-FAQ
- Auto Moderation in Discord: https://discord.com/safety/auto-moderation-in-discord
- How to Protect Your Server from Raids 101: https://support.discord.com/hc/en-us/articles/10989121220631-How-to-Protect-Your-Server-from-Raids-101
- Managing Moderation Teams: https://discord.com/moderation/1500000178661-310%3A-Managing-Moderation-Teams
- Creating Moderation Team Channels: https://discord.com/moderation/211-creating-moderation-team-channels
- Moderating Apps on Discord: https://support-apps.discord.com/hc/en-us/articles/26501864012951-Moderating-Apps-on-Discord
- Command Permissions: https://support-apps.discord.com/hc/en-us/articles/26501869403159-Command-Permissions

### Useful GitHub implementation references
- Ban appeals app: https://github.com/jcsumlin/discord-ban-appeal
- Sample ban appeals page with OAuth2: https://github.com/sylveon/discord-ban-appeals
- Content filtering, logging, exceptions, and punishment model: https://github.com/hifihedgehog/DiscordContentFilterBot
- Warning bot example: https://github.com/SahneeDEV/sahnee-bot
- Rules template gist for drafting a first server ruleset: https://gist.github.com/infinotiver/bb78602a6a2899fd04de7e524ec18e20

### Reddit signals worth keeping, not treating as authority
- Discord does not provide an official server-ban appeal system; servers must define their own process: https://www.reddit.com/r/discordapp/comments/u5i6jh/add_a_built_in_ban_appeal_system/
- Example of a community enforcing one official appeal form and telling users not to DM mods directly: https://www.reddit.com/r/pokerogue/comments/1db0wmh/discord_and_reddit_ban_appeals/

### YouTube follow-ups worth ingesting if you want tactical setup detail
- Anti-raid / anti-nuke with Wick + Beemo: https://www.youtube.com/watch?v=q1-B3_tQW7M
- Raid protection with WickBot: https://www.youtube.com/watch?v=TBQGpr1ZT2Q
- Discord appeals with Sapphire: https://www.youtube.com/watch?v=OS9pnjayEig
- Moderator training / staff behavior angle: https://www.youtube.com/watch?v=Ddg5mt0XIK0

### Recommended ingest order
1. Official Discord anti-raid / verification / rules-screening docs
2. Official Discord moderation-team docs
3. Official Discord app-permissions docs
4. One appeals implementation repo
5. One content-filter / logging repo
6. One or two YouTube tactical setup guides for Wick / Sapphire
7. Reddit only as reality-check examples after the policy and implementation layers are in place

## Connections
- [[wiki/synthesis/discord-moderation-domain]] is the current domain hub
- [[wiki/synthesis/discord-ai-agent-connection-patterns]] is the routing page for runtime Discord <-> AI integration
- [[wiki/synthesis/gehsture-discord-server-setup-2026]] is the seed source summary that exposed these gaps

## Open Questions
- Do you want this domain optimized for a small community server, a public brand/community server, or a large high-risk server?
- Should appeals live in a separate server, a web form, or a staff-only channel workflow?
- Are you aiming to self-host moderation tooling or lean on managed bots first?

## Related
- [[wiki/synthesis/discord-moderation-domain]]
- [[wiki/synthesis/gehsture-discord-server-setup-2026]]
- [[references/gehsture-discord-server-setup-2026]]

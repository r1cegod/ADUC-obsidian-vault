---
type: source-summary
title: "Discord Gateway"
created: 2026-04-07
updated: 2026-04-07
tags: [discord, ai, moderation, source-summary]
status: active
lang: en
source: "[[references/discord-gateway]]"
---

> **TL;DR**: Use Gateway when the AI moderation agent needs to observe Discord events continuously; use REST for the actual moderation actions after the AI has made or supported a decision.

## Summary
Discord's Gateway documentation explains the realtime event plane for apps. It is the connection surface you need when the moderation layer must react to messages, member joins, role updates, or channel changes without explicit command invocation. The source also makes a key architectural distinction: Discord expects many reads through Gateway, but most writes should happen through the HTTP API. For AI moderation, this suggests a clean split between event ingestion and action execution.

## Key Points
- Gateway is for receiving server events in realtime
- Intents define which classes of events your app receives
- Most resource mutations should happen through Discord's HTTP API, not Gateway

## Details
This source matters most for passive moderation. If the AI agent should classify live messages, detect suspicious join patterns, or watch role/channel abuse, Gateway is the intake path. But the Gateway should be treated as event transport, not your business-logic layer. The moderation system should consume events, enrich them with policy and AI analysis, then decide whether to log, alert, or call Discord REST actions.

## Related
- [[wiki/synthesis/discord-privileged-intents]]
- [[wiki/synthesis/discord-ai-agent-connection-patterns]]

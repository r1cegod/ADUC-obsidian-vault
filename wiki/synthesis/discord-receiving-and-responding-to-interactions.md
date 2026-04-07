---
type: source-summary
title: "Discord Receiving And Responding To Interactions"
created: 2026-04-07
updated: 2026-04-07
tags: [discord, ai, moderation, source-summary]
status: active
lang: en
source: "[[references/discord-receiving-and-responding-to-interactions]]"
---

> **TL;DR**: This source gives the most important connection constraint for an AI moderation bot: acknowledge the interaction fast, then do the slower AI work through a deferred response and followups.

## Summary
Discord's interaction-response documentation defines the transport contract an AI moderation workflow must respect. Interactions can arrive from guilds, bot DMs, or private channels, but the operational constraint is timing: the app must send an initial response within 3 seconds, and the interaction token can then be used for followups for 15 minutes. For AI systems, this means you usually defer the response immediately, run moderation classification or reasoning on your backend, then edit the original response or send followups once the analysis is ready. This is the core bridge between Discord UX and slower AI inference.

## Key Points
- Initial interaction responses must happen within 3 seconds
- Long-running AI work should use a deferred interaction response
- Followup messages can continue through the interaction token for 15 minutes

## Details
This source effectively forces the architecture. If the AI agent may need more than a couple of seconds, the Discord layer cannot wait for a full completion before acknowledging the user. The right pattern is: receive interaction -> validate/signature check -> defer -> call moderation models and policy logic -> send result. If the workflow may outlast the 15-minute interaction window, the bot should switch from interaction followups to normal bot-token messaging or staff-channel logging.

## Related
- [[wiki/synthesis/discord-interactions-overview]]
- [[wiki/synthesis/discord-ai-agent-connection-patterns]]

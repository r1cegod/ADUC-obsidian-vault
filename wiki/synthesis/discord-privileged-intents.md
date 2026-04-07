---
type: source-summary
title: "Discord Privileged Intents"
created: 2026-04-07
updated: 2026-04-07
tags: [discord, ai, moderation, source-summary]
status: active
lang: en
source: "[[references/discord-privileged-intents]]"
---

> **TL;DR**: Before building passive AI moderation on Discord, check intents first, because your agent architecture may be blocked by missing member or message-content access.

## Summary
Discord's privileged-intents article is short but operationally critical. It makes clear that some event classes and API responses require privileged intents, especially once an app is verified at scale. For AI moderation, this means you cannot blindly assume the bot will always see all messages or member details needed for passive review. This source is essentially a feasibility check for any architecture that depends on broad ambient visibility.

## Key Points
- Some Gateway events and API responses require privileged intents
- Verified apps can do a lot without them, but not everything
- Feasibility should be checked before designing AI around passive full-content access

## Details
This source matters because it can invalidate the wrong design early. If the AI moderator is meant to run only on explicit commands, privileged intents may barely matter. If the AI moderator is meant to continuously inspect live content or member state, they matter immediately. That makes intents a topology decision, not a deployment afterthought.

## Related
- [[wiki/synthesis/discord-gateway]]
- [[wiki/synthesis/discord-ai-agent-connection-patterns]]

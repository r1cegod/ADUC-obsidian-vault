---
type: reference
title: "What are Privileged Intents?"
created: 2026-04-07
updated: 2026-04-07
tags: [discord, ai, moderation]
status: active
lang: en
url: "https://support-dev.discord.com/hc/en-us/articles/6207308062871-What-are-Privileged-Intents"
---

> **TL;DR**: Discord's privileged-intents guide explains the approval-sensitive event classes that can block passive AI moderation designs if you assume full message/member access.

## Description
Official Discord developer support article on privileged intents and when they are required.

## Notes
- Best for: understanding message/member/presence access constraints before designing passive AI moderation
- Key warning: most apps can do a lot without privileged intents, but some event streams require them

## Related
- [[wiki/synthesis/discord-privileged-intents]]
- [[wiki/synthesis/discord-gateway]]

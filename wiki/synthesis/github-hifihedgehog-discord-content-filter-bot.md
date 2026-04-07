---
type: source-summary
title: "hifihedgehog Discord Content Filter Bot"
created: 2026-04-07
updated: 2026-04-07
tags: [discord, moderation, source-summary]
status: active
lang: en
source: "[[references/github-hifihedgehog-discord-content-filter-bot]]"
---

> **TL;DR**: This repo fills the “serious content filtering” gap with regex support, layered blacklist/whitelist logic, exception handling, user-facing explanations, and punishment tracking.

## Summary
`DiscordContentFilterBot` is the most detailed filtering implementation in the current batch. It combines term-based matching with regex, supports multiple blacklists and whitelists, allows exceptions at multiple levels, sends explanatory DMs to users, and includes a time- and occurrence-based punishment system. That makes it especially useful for domains where moderation needs to go beyond simple blocklists. For this vault, it fills the gap between Discord's built-in AutoMod and a more production-style filtering stack.

## Key Points
- Regex and exceptions are essential for real-world filtering because naive keyword lists overblock
- User-facing explanations and logs reduce confusion and improve auditability
- Punishment systems matter because filtering without consistent consequences creates policy drift

## Details
The repo shows how quickly moderation complexity rises once filters become nuanced. Blacklists alone are not enough: communities need whitelists, exception logic, configurable punishment ladders, and reviewable logs. The project also demonstrates the infrastructure burden such sophistication creates, including database assumptions and higher operational complexity than plug-and-play bots.

## Related
- [[wiki/synthesis/discord-automod-faq]]
- [[wiki/synthesis/discord-moderation-domain]]

---
type: source-summary
title: "Discord AutoMod FAQ"
created: 2026-04-07
updated: 2026-04-07
tags: [discord, moderation, source-summary]
status: active
lang: en
source: "[[references/discord-automod-faq]]"
---

> **TL;DR**: AutoMod gives Discord servers a first-party filtering layer for keywords, spam, and mention abuse, with moderator alerts and optional timeouts, but it still requires careful rule design and private review channels.

## Summary
Discord's AutoMod FAQ defines the built-in rule surface: custom keyword rules, preset commonly flagged words, spam-content filtering, and mention-spam limits. It also explains the available responses, including blocking a message, sending moderator alerts, adding a custom user-facing message, and timing out users for custom keyword matches. For this domain, the article is foundational because it turns “use automod” into a specific configuration model rather than a vague recommendation. It also clarifies that moderators need private alert channels and should understand matching behavior before trusting the rules.

## Key Points
- AutoMod can block messages, alert staff, and attach user-facing explanations
- Custom keyword rules support many languages, while some preset lists are English-only
- Keyword matching is broad enough to require deliberate testing to avoid false positives

## Details
The key operational takeaway is that AutoMod is powerful but not magic. It is strong for repeatable, high-volume, low-context moderation problems: spam bursts, slurs, known scam links, and mention attacks. It is weaker for nuanced or context-heavy judgment calls. This makes it ideal as the first line of defense, with staff reviewing alerts and handling escalation. The article also reinforces the need for dedicated moderator-only alert channels.

## Related
- [[wiki/synthesis/discord-auto-moderation-in-discord]]
- [[wiki/synthesis/discord-moderation-domain]]

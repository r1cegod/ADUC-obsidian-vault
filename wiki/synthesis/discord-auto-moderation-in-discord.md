---
type: source-summary
title: "Discord Auto Moderation In Discord"
created: 2026-04-07
updated: 2026-04-07
tags: [discord, moderation, source-summary]
status: active
lang: en
source: "[[references/discord-auto-moderation-in-discord]]"
---

> **TL;DR**: Discord's automation strategy is layered: small servers can survive on light filters, large public servers need stronger verification and anti-raid controls, and bots should extend human moderation rather than replace it.

## Summary
This article is the most useful official source for thinking about moderation automation as a system rather than a feature checklist. Discord separates the needs of smaller communities, larger public communities, and verified or partnered communities, then maps those needs to filters, verification, anti-spam, and anti-raid tooling. It also explains that AutoMod is not a substitute for human judgment, and that built-in suspicious-link and raid detection help but are not enough for higher-risk communities. For this domain, it is the bridge between technical settings and moderation operations.

## Key Points
- Auto moderation should enrich manual moderation, not replace it
- Public and high-visibility servers need stronger verification and anti-raid posture than private communities
- Bot choice should depend partly on the infraction and punishment model your team is comfortable operating

## Details
The article's strongest contribution is its layered mindset. Small private servers can often get by with keyword filters and basic anti-spam. Large public servers should add member verification, stronger filters, and possibly dedicated anti-raid tools. Discord also calls out an often-missed issue: moderation bots need a punishment model and operational fit, not just a feature list. That pushes the domain toward governance questions, not just bot shopping.

## Related
- [[wiki/synthesis/discord-raids-101]]
- [[wiki/synthesis/discord-moderation-domain]]

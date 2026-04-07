---
type: source-summary
title: "YouTube WickBot Raid Protection"
created: 2026-04-07
updated: 2026-04-07
tags: [discord, moderation, source-summary]
status: active
lang: en
source: "[[references/youtube-wickbot-raid-protection]]"
---

> **TL;DR**: This WickBot guide focuses on raid prevention through anti-nuke controls, quarantine logic, verification, and aggressive handling of suspicious fresh accounts.

## Summary
Fleet's WickBot tutorial is a compact anti-raid implementation source. It highlights anti-mod and anti-nuke capabilities, automatic quarantine behavior when staff-like accounts perform suspicious actions, verification, and extra scrutiny for newly created accounts. Compared with the longer Wick + Beemo video, this one is narrower and easier to translate into a checklist. In the current corpus, it reinforces the operational point that anti-raid defense is partly about staff-abuse containment, not just new-member spam.

## Key Points
- Anti-raid systems should watch moderators and admins too, not just new joiners
- Quarantine logic is useful when privileged users suddenly perform bulk harmful actions
- Fresh-account detection is a practical heuristic for filtering raid accounts

## Details
This source is useful because it broadens the raid model. Some anti-raid guides focus only on inbound spam, but this one gives attention to anti-mod and anti-nuke behaviors that assume a privileged account may act maliciously or get compromised. That makes it a good complement to official Discord docs, which are less tool-specific on privileged-abuse containment.

## Related
- [[wiki/synthesis/youtube-wick-beemo-anti-raid]]
- [[wiki/synthesis/discord-raids-101]]

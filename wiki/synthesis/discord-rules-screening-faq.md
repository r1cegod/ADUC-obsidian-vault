---
type: source-summary
title: "Discord Rules Screening FAQ"
created: 2026-04-07
updated: 2026-04-07
tags: [discord, moderation, source-summary]
status: active
lang: en
source: "[[references/discord-rules-screening-faq]]"
---

> **TL;DR**: Rules Screening is Discord's native “agree before participating” gate for Community servers, useful for making rule acknowledgement explicit and harder to bypass than older role-gate bots.

## Summary
Discord positions Rules Screening as the clean built-in way to require new members to accept server rules before they can talk, react, or DM other members. The article explicitly recommends it over older third-party role-gating flows because those older flows often fail to protect members from DMs and create confusing onboarding. Operationally, this feature matters because it makes rules acceptance visible and standardized. The tradeoff is that it adds friction, so it should be paired with concise, readable rules rather than long legalistic walls of text.

## Key Points
- Pending members cannot fully participate until they accept the rules
- Discord recommends this over older bot-based role gates for safer, cleaner onboarding
- Manual verification can bypass the requirement for specific edge cases

## Details
Rules Screening fills a specific gap in moderation design: explicit consent to the rules before full interaction. It is not a sanction system and not a bot replacement for everything, but it sharpens the join funnel and makes enforcement easier because “the user never saw the rules” becomes a weaker excuse. The article also notes the central tradeoff of all onboarding gates: better safety usually means more joiner drop-off.

## Related
- [[wiki/synthesis/discord-verification-levels]]
- [[wiki/synthesis/discord-moderation-domain]]

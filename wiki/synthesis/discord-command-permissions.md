---
type: source-summary
title: "Discord Command Permissions"
created: 2026-04-07
updated: 2026-04-07
tags: [discord, moderation, source-summary]
status: active
lang: en
source: "[[references/discord-command-permissions]]"
---

> **TL;DR**: Command Permissions let servers restrict specific app commands by role, member, and channel, which makes them one of the cleanest least-privilege tools in Discord's app-moderation stack.

## Summary
This article explains how Discord scopes individual app commands instead of forcing all-or-nothing bot access. Commands can be granted or denied by role, by member, and by channel context, which lets moderators keep apps installed while exposing only the safe parts to the right audiences. Discord also notes that commands hidden by permissions do not appear in the command picker, which reduces both misuse and clutter. In practice, this source matters because it lets servers keep useful bots without granting the full community access to every action they expose.

## Key Points
- Command permissions support granular allow/deny behavior beyond whole-bot permissions
- Hidden commands reduce accidental misuse because users without access will not see them
- The bot's broader permissions are still viewable on the same settings surface

## Details
The main lesson is that bot security is not binary. A server may trust a bot enough to install it but still want only certain staff roles or channels to use sensitive commands. Command Permissions make that possible. This is especially relevant for moderation bots, utility bots, and multi-purpose bots that mix harmless features with actions that can affect channel visibility, punishment, or large-scale messaging.

## Related
- [[wiki/synthesis/discord-moderating-apps]]
- [[wiki/synthesis/discord-moderation-domain]]

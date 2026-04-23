---
type: operation
title: "Context Update Operation"
created: 2026-04-21
updated: 2026-04-21
tags: [workflow, docs, context]
status: active
lang: en
---
> **TL;DR**: Update the vault’s context layer when live conversation changes what future sessions should know.

## When To Use
Use when the user reveals durable new context in conversation.

## Routing In
- [[wiki/operations-hub]]
- [[SCHEMA.md]]
- [[vault-keeping]]

## Steps
1. Decide which context file owns the new fact.
2. Update the context file before the main task if it affects routing or judgment.
3. Log the update in the current day file.

## Routing Out
- Continue main task after context is current
- Closeout -> [[wiki/operations/self-healing-operation]]

## After Use Evolution Check
- Was the owning context file obvious?
- Did context updates happen early enough?
- Did the rule still require too much interpretation?
- If friction appeared, patch this leaf or log the gap today.

## Related
- [[SCHEMA.md]]
- [[context/now]]
- [[context/me]]
- [[context/goals]]

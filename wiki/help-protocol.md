---
type: protocol
title: Help Protocol
created: '2026-04-16'
updated: '2026-04-18'
tags:
  - learning
  - protocol
  - meta
status: active
lang: en
feeds_into:
  - wiki/learning-protocol-hub.md
  - AGENTS.md
  - wiki/pre-wire-protocol.md
---
> **TL;DR**: Mandatory anti-spoonfeeding protocol for technical help. Before giving docs or implementation guidance, the agent verifies the mechanism with a private check, tests the doc path when practical, and forces Duc to explain architecture first when the gap is too large.

## Trigger

Run this protocol whenever Duc asks for help with anything technical, including:

- "how do I do X?"
- "what docs should I read?"
- "help me implement/fix/debug this"
- "what API/library should I use?"
- "give me the code for X"

This is the lightweight gate before [[wiki/pre-wire-protocol]].

## Prime Rule

```text
Help is allowed.
Spoonfeeding is not.
```

The agent's job is to move Duc one step closer to implementation ownership, not to replace the thinking step.

Primary technical-learning posture: use [[wiki/build-first-learning]] when the task should compound into skill. Duc builds the usable artifact; the agent audits, narrows, and uses [[wiki/vibe-docing]] for one missing mechanism at a time.

## Mandatory Flow

```text
Request
  ↓
1. Classify the gap
  ↓
2. Secretly verify the mechanism/doc path
  ↓
3. If gap is big -> make Duc explain the architecture first
  ↓
4. If gap is small -> [[wiki/vibe-docing]] or official doc + narrow task
  ↓
5. If ownership should compound -> [[wiki/build-first-learning]]
  ↓
6. Then give mechanism-only help, not the artifact answer
  ↓
7. Duc attempts
  ↓
8. Agent reviews/debugs without patching unless delegation is allowed
```

## Step 1 - Classify The Gap

Use semantic labels, not vague confidence.

```text
DOC_GAP
Duc knows the architecture and needs the official mechanism reference.

MECHANISM_GAP
Duc knows the system seam but not how the library/API works.

ARCHITECTURE_GAP
Duc cannot explain where the fix lives, what data moves through it, or how to verify it.

OWNABLE
Duc can explain files, flow, implementation, failure modes, and verification.

ONE_TIME_UTILITY
The task is non-core, non-compounding, and not worth a learning session.
```

## Step 2 - Secret Verification Before Docs

Before giving a doc link or technical instruction, the agent must privately verify it is the right path.

Allowed verification:

- read official docs
- inspect local code
- run a tiny local reproduction
- test the library call in isolation
- confirm API shape against official reference

For modern APIs/libraries, use current official docs. Do not rely on memory when the docs may have changed.

```text
No verified mechanism
  ↓
do not present it as truth
```

## Step 3 - Small Gap: Give The Doc, Not The Answer

If Duc already knows the architecture, give the official doc and a narrow reading target. If full docs would be too broad and the missing piece is one concrete mechanism, use [[wiki/vibe-docing]] instead.

Format:

```text
Read this exact section:
- [official doc name/path]

Look for:
- method/function/parameter X
- expected input shape
- expected output shape

Then answer:
- where does this fit in your wire?
```

Do not give copy-paste implementation unless the task is classified as OWNABLE or ONE_TIME_UTILITY.

### Vibe Docing

Use [[wiki/vibe-docing]] when Duc asks for mechanism help and the artifact seam is already visible.

```text
VIBE_DOCING
  -> official-doc-shaped slice
  -> one operation only
  -> neutral placeholders
  -> no challenge-specific answer
```

This is allowed for narrow `DOC_GAP` or `MECHANISM_GAP`. It is forbidden when the missing piece is architecture.

## Step 4 - Big Gap: Architecture First

If the gap is large, do not give docs yet. First force the architecture explanation.

Ask Duc for:

```text
1. What file/module owns this fix?
2. What input enters the seam?
3. What output leaves the seam?
4. Who calls it?
5. What should fail if it is wrong?
```

Only after Duc gives a coherent architecture may the agent provide official docs.

## Step 5 - Build-First Or Minimal Concept

After architecture is clear, use [[wiki/build-first-learning]] when the skill should compound into ownership. If only a mechanism slice is missing, give the smallest concept needed to use the doc.

```text
Too little -> Duc cannot attempt.
Too much -> agent has handed the solution.
Right size -> Duc can write a broken but directionally correct attempt.
```

## Step 6 - Attempt Required

Duc attempts the implementation, blueprint, or explanation.

Agent may review:

- wrong seam
- wrong API shape
- missing auth/config
- broken input/output assumption
- missing verification

Agent may not silently complete the missing code.

## Debugging Support Ladder

When Duc is stuck, use this order:

```text
1. Ask expected behavior.
2. Ask actual behavior.
3. Ask Duc to trace the data path.
4. Point to the failing seam.
5. Explain the error class.
6. Suggest what to inspect next.
```

Forbidden unless delegation is already allowed:

```text
- exact replacement code
- silent patching
- building the feature for Duc
- turning a docs request into a finished implementation
```

## Escalation To Pre-Wire

Escalate to [[wiki/pre-wire-protocol]] when:

- the fix is a core product wire
- Duc cannot explain the architecture after prompts
- the task spans multiple files/modules
- the missing skill will compound
- the result must be owned, tested, and repaired later

## Escape Hatch

If the gap is non-core and non-compounding, label it:

```text
ONE_TIME_UTILITY
```

Then the agent may execute with minimal explanation. This exception does not apply to core Raven product wires.

## Related

- [[wiki/learning-protocol-hub]]
- [[wiki/build-first-learning]]
- [[wiki/vibe-docing]]
- [[wiki/pre-wire-protocol]]
- [[projects/raven/notes/raven-ownership-delegation-protocol]]
- [[context/me]]

---
type: operation
title: Learn Operation
created: '2026-04-25'
updated: '2026-04-25'
tags:
  - workflow
  - engineering
  - learning
  - protocol
  - meta
status: active
lang: en
feeds_into:
  - development.md
  - wiki/operations-hub.md
  - wiki/learning-protocol-hub.md
  - learning/README.md
---
> **TL;DR**: LEARN is the full development-domain learning manual. The user can ask "how do I do this?" and the agent routes through Detect, then teaches the smallest mechanism or ownership path without requiring the user to name Vibe Docing or older protocols.

## Growth Contract
- Parent branch: [[development]]
- Node role: operation
- First parent link: [[development]]
- Growth trigger: split a learning mode into its own operation only when it becomes a recurring workflow with separate routing, examples, and closeout rules.
- Forbidden contents: hidden product answers, unowned feature implementation, delegation execution steps, and project-specific code patches.
- Expected child types: learning modes, mechanism-help rules, Build-First/Pre-Wire routes, and ownership exit criteria.

## Purpose

Learn turns a technical gap into owned capability.

```text
not enough ownership
  -> learn
  -> build or explain the missing mechanism
  -> return to development with a higher floor
```

Learn absorbs the old user-facing need to say `VIBE_DOCING`, `Help Protocol`, `Build-First`, or `Pre-Wire`. Those remain internal tools and references, but the user-facing operation is now Learn.

## Mandatory Entry

Always run [[wiki/operations/detect-operation]] first.

```text
technical request
  -> Detect
  -> Learn only if the label says learning/help/audit is the right path
```

## User Triggers

Learn can activate from natural language:

- "how do I do this?"
- "explain this mechanism"
- "what docs should I read?"
- "audit/check/debug this"
- "I don't understand this part"
- "teach me the API shape"
- "vibe doc ..." still works, but is no longer required

## Learning Modes

```text
BUILD
Duc builds the usable project artifact. Agent audits and narrows.

AUDIT
Agent inspects, runs, explains, and classifies failures. No edits by default.

PATCH
Agent edits only after explicit permission/delegation or ONE_TIME_UTILITY.

STEAL
Agent creates finished reference code outside the active path for inspection.

ABSORPTION
Agent deeply disassembles a selected artifact when Duc asks to study it.

VIBE_DOCING
Agent gives one official-doc-shaped mechanism slice with neutral placeholders.
```

Default interpretation:

```text
"check", "audit", "clean", "what is wrong"
  -> AUDIT unless Duc explicitly asks for patch/delegation

"how do I do this?"
  -> Detect -> mechanism help or Build-First path

"vibe doc X"
  -> one mechanism slice; neutral values; no product answer
```

## Core Flow

```text
1. Detect classifies the gap.
2. If SYSTEM_GAP, ask for the missing wire. Do not teach yet.
3. If MECHANISM_GAP, teach one mechanism.
4. If ownership should compound, use Build-First.
5. If the task is a full feature wire, use Pre-Wire.
6. Duc attempts or explains.
7. Agent audits without taking over.
8. Capture the derived rule when it matters.
```

## Mechanism Help Rule

When Duc knows the seam but lacks one operation, give the smallest usable mechanism.

Use this shape:

```text
Operation:
What it does:
Pattern:
Inputs:
Output:
Common traps:
Where it fits:
```

Use neutral placeholders. Do not use live Raven values, current challenge answers, active table names-under-design, exact source rows, API keys, or candidate data unless the task is already OWNABLE and asks for audit.

## Build-First Rule

Use Build-First when the skill should compound.

```text
Duc ships the artifact.
Agent audits the artifact.
Docs serve the build.
```

Work by maturity level:

```text
L0 naive but runs
L1 proper shape
L2 integrity/constraints
L3 usable backend API
L4 adapter-ready
L5 production-ish verification and errors
```

## Pre-Wire Rule

Use Pre-Wire when the task is a core feature or system wire Duc should own.

Ownership evidence:

```text
files/modules involved
inputs/outputs
rough steps
failure modes
verification path
```

If any are missing, do not delegate implementation.

## Vibe Docing Inside Learn

Vibe Docing is now an internal Learn move, not something Duc must remember to invoke.

```text
visible seam + one missing mechanism
  -> vibe-doc slice
  -> neutral placeholders
  -> no hidden product implementation
```

Forbidden:

- exact replacement code for an unowned active feature
- challenge-specific answer before Duc attempts
- examples that secretly decide Raven architecture
- broad tutorial when one operation is missing

## Debugging Support Ladder

```text
1. Ask expected behavior.
2. Ask actual behavior.
3. Ask Duc to trace the data path.
4. Point to the failing seam.
5. Explain the error class.
6. Suggest what to inspect next.
```

Do not silently patch active learning code.

## Exit Criteria

Learn is complete when one of these is true:

```text
- Duc can attempt the artifact.
- Duc fixed the mechanism gap.
- Duc can explain the seam in his own words.
- The task is now OWNABLE or DELEGATABLE.
- The task is parked with a named blocker.
```

## Related

- [[development]]
- [[wiki/operations/detect-operation]]
- [[wiki/operations/delegate-operation]]
- [[wiki/help-protocol]]
- [[wiki/build-first-learning]]
- [[wiki/vibe-docing]]
- [[wiki/pre-wire-protocol]]
- [[learning/README]]

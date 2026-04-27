---
type: protocol
title: Pre-Wire Learning Protocol
created: '2026-04-08'
updated: '2026-04-25'
tags:
  - protocol
  - learning
  - meta
status: active
lang: en
feeds_into:
  - wiki/operations/learn-operation.md
  - learning/README.md
---
> **TL;DR**: Heavyweight feature-ownership reference inside [[wiki/operations/learn-operation]]. Duc drafts the system blueprint, agent audits with semantic labels, missing mechanisms become artifact challenges, and Duc builds the final feature himself.

## Growth Contract
- Parent branch: [[wiki/operations/learn-operation]]
- Node role: protocol reference leaf
- First parent link: [[wiki/operations/learn-operation]]
- Growth trigger: split only if feature-ownership work develops separate recurring sub-protocols beyond blueprint, gap inventory, and artifact challenge flow.
- Forbidden contents: current top-level routing, Delegate execution procedure, project-specific implementation patches, and raw learning-session logs.
- Expected child types: feature-ownership phases, semantic labels, artifact challenge rules, and learning-session references.

## What This Is

A session-by-session protocol for turning "I want a feature" into "I can build, test, and repair this wire myself."

Default teaching method inside this protocol: [[wiki/build-first-learning]]. Pre-Wire owns the feature-ownership reference flow; Build-First owns the artifact-by-artifact learning motion.

Use this inside [[wiki/operations/learn-operation]] when the task is a real feature or core system seam Duc should own. Smaller doc/help/debugging requests stay in Learn unless Detect routes them here.

Router: [[development]] -> [[wiki/operations/detect-operation]] -> [[wiki/operations/learn-operation]] -> this reference

## Entry Gate

Before implementation help, run [[wiki/operations/detect-operation]]. Escalate here only when the task needs feature ownership.

```text
Need help/docs/debugging only
  ↓
[[wiki/operations/learn-operation]]

Need to own a feature wire
  ↓
this protocol reference inside Learn
```

## Ownership Evidence Standard

Duc counts as already knowing how to write a task only if he can state:

```text
1. files/modules involved
2. input/output at each seam
3. rough implementation steps
4. main failure modes
5. how to verify it works
```

If any item is missing, the task is not fully ownable yet.

## Semantic Labels

Use these labels everywhere. Do not use Case A/B/C.

```text
OWNABLE
Duc understands system + mechanism. Review/delegation may be allowed.

MECHANISM_GAP
Duc understands the system seam but lacks the technical mechanism.

SYSTEM_GAP
Duc has not described the architecture, boundary, data flow, or responsibility clearly.

ONE_TIME_UTILITY
The task is non-core and non-compounding. Agent may execute with minimal teaching.
```

## Breakpoints

```text
B1: SPOON-FED
Never hand the answer when the goal is ownership.

B2: NO ANCHOR
Never teach a concept before the problem/seam is visible.

B3: OVER-HELP
Stuck does not mean permission to solve it for Duc.
```

When a breakpoint fires:

```text
1. Name it.
2. Stop the answer.
3. Ask a question that moves Duc one step closer.
4. Log it in the session retrospective.
```

## Protocol Flow

```text
Phase 0: Duc drafts blueprint
  ↓ READY FOR AUDIT
Phase 1: Agent audits
  ├── SYSTEM_GAP -> name missing wire -> back to Phase 0
  ├── OWNABLE -> review/delegation allowed
  ├── ONE_TIME_UTILITY -> execute lightly
  └── MECHANISM_GAP
        ↓
Phase 2: Agent creates safe reference only if needed, not product patch
        ↓
Phase 3: Agent lists dependency-ordered gaps
        ↓
Phase 4: [[wiki/build-first-learning]] artifact levels
        ↓
Phase 5: Duc rewrites final blueprint
        ↓
Phase 6: Duc builds; agent reviews/debugs without patching
```

## Phase 0 - User Blueprint

Duc writes, in his own words:

```text
Task:
What the feature does:
Files/modules involved:
Inputs:
Outputs:
Failure modes:
Verification:
What I do not understand yet:
```

Phase 0 ends only when Duc writes:

```text
READY FOR AUDIT
```

Before that, agent may only say:

```text
Write what you have. Gaps are fine.
```

No leading questions. No "have you thought about X?" That contaminates the blueprint.

## Phase 1 - Audit

Classify the blueprint.

### SYSTEM_GAP

Architecture is missing or unclear.

Examples:

- no owner module
- unclear input/output
- no data re-entry path
- no caller
- no verification story

Agent response:

```text
You have a SYSTEM_GAP: [missing wire].
Fix the blueprint first. No code yet.
```

### MECHANISM_GAP

System is clear, mechanism is missing.

Examples:

- knows a search node needs API results, but not how OAuth/API calls work
- knows candidates need persistence, but not SQLite transaction/query shape

Agent response:

```text
You have a MECHANISM_GAP: [mechanism].
We will run artifact challenges for these gaps.
```

### OWNABLE

Duc passes the ownership evidence standard.

Agent response:

```text
OWNABLE. Review/delegation is allowed if useful.
```

### ONE_TIME_UTILITY

Non-core and non-compounding.

Agent response:

```text
ONE_TIME_UTILITY. I can execute this with minimal explanation.
```

## Phase 2 - Safe Reference

The agent may create a reference only to verify the mechanism and teach from it.

Allowed reference forms:

```text
- toy/sandbox implementation
- pseudocode reference
- minimal seam example
- fixture-only implementation
- private reproduction script
```

Forbidden unless Duc already passed L3/OWNABLE:

```text
- production-ready hidden patch
- full feature implementation in repo files
- new architecture introduced secretly by the agent
```

Rule:

```text
Reference teaches the mechanism.
It must not secretly build the product.
```

## Phase 3 - Gap Inventory

List all real technical gaps before challenges begin.

Order gaps by dependency, not convenience.

```text
GAP 1: prerequisite mechanism
GAP 2: mechanism depending on GAP 1
GAP 3: integration mechanism
```

A later gap cannot depend on an unpassed earlier gap.

Do not manufacture gaps Duc can infer from the blueprint.

## Phase 4 - Artifact Challenge

Run one gap at a time using [[wiki/build-first-learning]] as the default method. Duc builds usable artifacts by maturity level; the agent audits and uses [[wiki/vibe-docing]] only for missing mechanism operations.

### Step 1 - System View

Draw the seam.

```text
existing system
  ↓
[gap seam]
  ↓
next component
```

### Step 2 - Problem Statement

Ask:

```text
This seam needs to do X. What does X require?
```

Wait for Duc to answer. Wrong answers become the teaching anchor.

### Step 3 - Minimum Viable Concept

Give the smallest concept needed to attempt the artifact. If the missing piece is one concrete mechanism and full docs would be too broad, use [[wiki/vibe-docing]].

```text
Too little -> cannot attempt.
Too much -> B1 spoonfeeding.
Right -> can write a broken but directionally correct attempt.
```

Vibe docing must stay mechanism-only: one operation, neutral placeholders, no challenge-specific artifact answer.

### Step 4 - Artifact Attempt

Duc writes the artifact. Agent waits.

No hints during writing unless Duc explicitly asks. If stuck, one nudge:

```text
What does your blueprint say this seam needs to do?
```

If still stuck, Step 3 was too thin. Add one concept, then retry.

### Step 5 - Contrast

Reveal only the reference piece for this gap.

Ask:

```text
Find 3 differences between yours and this.
```

Do not reveal the full reference implementation.

### Step 6 - Lock-In Rule

Duc writes one rule derived from the gap.

Pass criteria:

```text
Duc can write the artifact and state a correct rule in his own words.
```

Fail criteria:

```text
Duc copied without understanding, or rule is just a memorized definition.
```

If fail, return to the specific broken step.

## Phase 5 - Final Blueprint

Duc rewrites the original blueprint with technical detail filled in.

Agent checks only for logic gaps.

```text
No gap -> build
Gap -> return to Phase 1 for that seam only
```

## Phase 6 - Build And Debug

Duc builds the feature. Agent does not write product code unless the task has become OWNABLE/L3 delegation.

Debugging support ladder:

```text
1. Ask expected behavior.
2. Ask actual behavior.
3. Ask Duc to trace the data path.
4. Point to the failing seam.
5. Explain the error class.
6. Suggest what to inspect next.
```

Forbidden unless delegation is allowed:

```text
- exact replacement code
- silent patching
- writing stubs into the repo
- completing the missing feature
```

Build complete criteria:

```text
feature runs
Duc wrote the product code
Duc can explain every line
verification passes
```

## Timebox And Downshift

One session should own one wire or one mechanism.

If a learning session exceeds 45-60 minutes without passing a gap:

```text
stop
write the blocker
decide one:
  - shrink the gap
  - park it
  - convert to ONE_TIME_UTILITY
  - resume later
```

Intensity without progress is not discipline. It is bad allocation.

## Session Record

No serious pre-wire session runs only in chat.

Before Phase 0, create or choose a session note from [[templates/learning-session]] and index it from [[learning/README]].

After each session, record:

```text
what worked
what felt wrong
breakpoints fired
rules derived
protocol changes to consider
```

## Version History

- v1.0 - 2026-04-08: initial design
- v1.1 - 2026-04-08: expanded breakpoints, stuck handling, wrong-answer handling, gap calibration
- v1.2 - 2026-04-16: added universal entry gate
- v2.0 - 2026-04-16: added Help Protocol router, semantic labels, ownership evidence, safe-reference rule, READY FOR AUDIT marker, dependency-ordered gaps, debug ladder, and timebox/downshift rule

## Related

- [[development]]
- [[wiki/operations/detect-operation]]
- [[wiki/operations/learn-operation]]
- [[wiki/operations/delegate-operation]]
- [[wiki/learning-protocol-hub]]
- [[wiki/help-protocol]]
- [[wiki/build-first-learning]]
- [[wiki/vibe-docing]]
- [[learning/README]]
- [[templates/learning-session]]
- [[projects/raven/notes/raven-ownership-delegation-protocol]]
- [[context/me]]

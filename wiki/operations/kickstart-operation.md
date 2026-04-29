---
type: operation
title: Kickstart Operation
created: '2026-04-29'
updated: '2026-04-29'
tags:
  - workflow
  - docs
  - meta
  - plan
status: active
lang: en
feeds_into:
  - wiki/operations-hub.md
  - duc-os/kickstart.md
  - index.md
---
> **TL;DR**: KICKSTART turns "what I want to get done today" into a discussion loop that eventually locks a written execution plan, while keeping the plan updateable when reality changes.

## Growth Contract
- Parent branch: [[wiki/operations-hub]]
- Node role: operation
- First parent link: [[wiki/operations-hub]]
- Growth trigger: split only if daily planning, weekly planning, or project-specific execution planning become separate recurring workflows with different artifacts.
- Forbidden contents: raw journaling, motivational prose, full project roadmaps, implementation patches, and long-term strategy that belongs in [[duc-os/current]] or a project context hub.
- Expected child types: execution-plan template, classification labels, checkpoint rules, and handoffs into [[wiki/operations/learn-operation]] or [[wiki/operations/delegate-operation]].

## Purpose

KICKSTART is the anti-drift start block.

```text
Duc says what he wants done today
  -> agent drafts a plan candidate
  -> discussion pressure-tests scope, gaps, order, and delegation
  -> Duc or agent explicitly locks the plan
  -> locked plan is written to [[duc-os/kickstart]]
  -> session proceeds against the written plan
  -> plan can be updated when reality changes
```

This operation exists because chat-only planning evaporates. KICKSTART creates a visible control surface.

## Plan States

```text
DISCUSSING
Plan is a candidate. Push back, ask missing constraints, reorder, shrink, split, or park items. Do not treat it as execution law yet.

LOCKED
Duc or the agent explicitly says the plan is locked. Write the current plan into [[duc-os/kickstart]] and execute from it.

UPDATED
A locked plan changed because of new information, failed verification, time pressure, or a better dependency order. Patch [[duc-os/kickstart]] instead of pretending the old plan still holds.
```

Default state is `DISCUSSING`. A plan is not locked just because the agent drafted it.

## Trigger

Run KICKSTART when Duc says:

- "KICKSTART"
- "kickstart today"
- "here is what I want to get done today"
- "make a plan for today"
- "help me not drift"

If Duc gives no task list, ask for the smallest input:

```text
What do you want to get done today?
```

Do not ask for mood, motivation, or broad life context unless it changes execution constraints.

## Required Input

Minimum input:

```text
today's desired outcomes
```

Optional useful input:

```text
available time
hard deadline
energy constraint
must-not-do list
current blocker
```

## Classification Labels

Use these labels inside the plan.

```text
EXECUTE
Duc can act now. No missing mechanism blocks the step.

LEARN_FIRST
A knowledge or ownership gap would make execution fake or fragile.

DELEGATE
The task is bounded enough for Codex to execute or patch after [[wiki/operations/detect-operation]] confirms the threshold.

AUDIT
Inspect, run, compare, or diagnose before deciding the next move.

PARK
Not for today. Keep visible so it stops pulling attention from the main lane.
```

For technical work, KICKSTART must respect the development gate:

```text
technical item
  -> [[wiki/operations/detect-operation]]
  -> LEARN_FIRST or DELEGATE only after threshold classification
```

## Plan Shape

Write or patch [[duc-os/kickstart]] using this structure:

```text
# Kickstart Current Plan

## Today
- Date:
- Plan state: DISCUSSING | LOCKED | UPDATED
- Mission:
- Available block:
- Hard constraints:
- Last update reason:

## Discussion Notes
- open questions:
- rejected paths:
- lock condition:

## Execution Stack
| Order | Outcome | Label | Next physical action | Done signal |

## Knowledge Gaps
| Gap | Why it blocks | Route | First learning action |

## Delegation Candidates
| Task | Why delegatable | Boundary | Verification |

## Drift Guards
- Main lane:
- Must not chase:
- Checkpoint:

## Parking Lot
- item - why parked

## Closeout
- shipped:
- learned:
- next restart point:
```

Keep each row executable. If a row cannot produce a next physical action, rewrite it or park it.

## Execution Rules

1. Compress the user's desired outcomes into one mission candidate.
2. Keep the plan in `DISCUSSING` while scope, constraints, ordering, and gaps are still being challenged.
3. Separate outcomes from activities.
4. Detect dependencies and missing knowledge.
5. Mark each item `EXECUTE`, `LEARN_FIRST`, `DELEGATE`, `AUDIT`, or `PARK`.
6. Choose one main lane, not three equal priorities.
7. Lock only when the plan has a clear mission, first action, done signal, and drift guard.
8. Write the locked plan to [[duc-os/kickstart]] before starting execution.
9. During the session, update [[duc-os/kickstart]] when the plan materially changes and record the reason.
10. At closeout, write the restart point so the next session can resume without reconstruction.

## Knowledge Gap Test

A gap is real if it blocks one of these:

```text
file/module ownership
input/output boundary
API or tool mechanism
verification path
failure mode
decision criterion
```

If the gap is curiosity-only, park it.

## Delegation Test

A task can be labeled `DELEGATE` only when the boundary is visible:

```text
owner file or artifact
allowed edit surface
existing pattern to copy
verification command or inspection path
```

If the task needs architecture thinking, hidden mechanism learning, or a new abstraction, label it `LEARN_FIRST` or `AUDIT` instead.

## Output Style

KICKSTART output should be sharp and operational:

```text
Mission: ship X by doing A -> B -> C.
Main lane: A.
First action: open/run/check Y.
```

No comfort paragraphs. No fake balance. The plan is a control surface, not therapy.

## Update Rule

A locked plan should change when the world changes. Update [[duc-os/kickstart]] if any of these happen:

- a knowledge gap is resolved or becomes larger than expected
- a delegated task becomes unsafe or becomes clearly bounded
- verification fails
- available time changes
- the main lane is no longer the highest-leverage path
- Duc explicitly revises the goal

Every update needs a short `Last update reason`. Do not silently mutate the plan.

## Closeout

At the end of a KICKSTART-driven session:

1. Patch [[duc-os/kickstart]] Closeout.
2. Log durable work through [[wiki/operations/self-healing-operation]].
3. If the plan exposed operation friction, patch this page or log the named gap.

## Related

- [[wiki/operations-hub]]
- [[duc-os/kickstart]]
- [[duc-os/current]]
- [[wiki/operations/detect-operation]]
- [[wiki/operations/learn-operation]]
- [[wiki/operations/delegate-operation]]
- [[wiki/operations/self-healing-operation]]

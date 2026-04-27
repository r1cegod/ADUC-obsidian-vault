---
type: learning-session
title: '[Feature Name] - Learning Session'
created: YYYY-MM-DD
updated: YYYY-MM-DD
tags:
  - learning-session
  - project/<project-name>
status: active
lang: en
---
> **TL;DR**: [One line: feature, main gap, outcome]

## Growth Contract
- Parent branch: [[learning/README]] or project learning/workflow hub
- Node role: learning-session leaf
- First parent link:
- Growth trigger: promote durable rules into [[wiki/operations/learn-operation]] or the project workflow hub after repeated use
- Forbidden contents: finished product code, unrelated project status, raw chat transcript dumps

## Protocol Route

- Domain: [[development]]
- Threshold gate: [[wiki/operations/detect-operation]]
- Learning manual: [[wiki/operations/learn-operation]]
- Feature protocol reference: [[wiki/pre-wire-protocol]]

## Blueprint (user-written)

> Write how this feature works and how you think it should be implemented.
> No help from agent at this stage.
> End with `READY FOR AUDIT` when complete.

```text
Task:
What the feature does:
Files/modules involved:
Inputs:
Outputs:
Failure modes:
Verification:
What I do not understand yet:

READY FOR AUDIT
```

---

## Audit Result

- [ ] OWNABLE - review/delegation may be allowed
- [ ] MECHANISM_GAP - run artifact challenges
- [ ] SYSTEM_GAP - revise blueprint first
- [ ] ONE_TIME_UTILITY - agent may execute lightly

**Notes:**
[agent writes missing wire/mechanism in system terms]

---

## Safe Reference

> Reference must teach the mechanism, not secretly build the product.

Type:
- [ ] toy/sandbox
- [ ] pseudocode
- [ ] minimal seam example
- [ ] fixture-only
- [ ] private reproduction

Status: [ ] built [ ] tested [ ] not needed

---

## Technical Gap Inventory

> Ordered by dependency, not convenience.

| # | Gap description | Depends on | Status |
|---|-----------------|------------|--------|
| 1 | | none | pending |
| 2 | | | pending |
| 3 | | | pending |

---

## Artifact Challenges

### Gap 1: [name]

**System view:**
```text
[ASCII diagram here]
```

**Problem statement:** [what this seam needs to do]

**Your answer before concept:**
[user writes here]

**Minimum viable concept:**
[agent writes the smallest knowledge unit needed]

**Artifact challenge:** Write [specific piece]

**Your attempt:**
```text
[user writes here]
```

**Contrast:** Find 3 differences between your attempt and the reference piece.
1.
2.
3.

**Lock-in rule (user writes):**
>

**Status:** [ ] pass [ ] fail

---

## Final Blueprint (user rewrites)

> Rewrite the original blueprint with technical implementation detail filled in.
> This is not copying the reference. This is your system understanding plus the HOW.

[user writes here]

**Logic check:** [ ] no gaps -> build it yourself [ ] gap found -> return to that seam

---

## Build Log

[ ] Built by user without agent writing product code

Notes:
[what broke, what you figured out, how long it took]

## Debugging Ladder Used

- [ ] expected behavior stated
- [ ] actual behavior stated
- [ ] data path traced
- [ ] failing seam identified
- [ ] error class explained
- [ ] next inspection target chosen

---

## Retrospective

**What worked:**

**What felt wrong:**

**Breakpoints that fired (B1/B2/B3):**

**Rules derived:**

**Protocol changes to consider:**

---

## Related

- [[development]]
- [[wiki/operations/detect-operation]]
- [[wiki/operations/learn-operation]]
- [[wiki/pre-wire-protocol]]
- [[learning/README]]

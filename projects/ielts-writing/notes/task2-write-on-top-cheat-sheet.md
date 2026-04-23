---
type: note
title: Task 2 Write-On-Top Cheat Sheet
created: '2026-04-22T00:00:00.000Z'
updated: '2026-04-22T00:00:00.000Z'
tags:
  - ielts
  - writing
  - schema
  - cheat-sheet
status: active
lang: en
---

> **TL;DR**: This is the execution layer for Task 2. Do not "write an essay" from scratch. Copy this frame, fill the slots, then smooth the wording. Same 4-paragraph machine every time; only the mutation changes.

## Why This Exists

The current Task 2 schema doc is the reference manual.
This page is the **write-on-top artifact**.

Use it like this:

```text
PROMPT
  -> identify mutation
  -> choose position
  -> write 2 body claims
  -> fill sentence slots
  -> smooth grammar
  -> proofread
```

If your mind goes blank, that is not a language failure.
It means the slot is empty.
Fill the slot.

---

## 1. The Core Machine

```text
┌──────────────────────────────────────────────────────────────┐
│ INTRO                                                       │
│  S1. Paraphrase the topic                                   │
│  S2. Thesis = position + reason 1 + reason 2                │
│                                                              │
│ BODY 1                                                      │
│  S3. Main claim 1                                            │
│  S4. Mechanism: why / how                                    │
│  S5. Result / consequence                                    │
│  S6. Example                                                 │
│  S7. Mini-link back to thesis                                │
│                                                              │
│ BODY 2                                                      │
│  S8. Main claim 2                                            │
│  S9. Mechanism: why / how                                    │
│  S10. Example                                                │
│  S11. Mini-link back to thesis                               │
│                                                              │
│ CONCLUSION                                                  │
│  S12. Restate position                                       │
│  S13. Final implication / recommendation                     │
└──────────────────────────────────────────────────────────────┘
```

This is your default 13-sentence architecture.
Not every essay must have exactly 13 sentences, but this is the safest training frame.

---

## 2. The Fill-In Template

Copy this before each practice essay.

```text
[INTRO]
S1. It is often argued that [paraphrase prompt topic].
S2. I believe that [your position], mainly because [reason 1] and [reason 2].

[BODY 1]
S3. The first reason for this is that [claim 1].
S4. This is because [mechanism 1].
S5. As a result, [effect / consequence 1].
S6. For example, [specific example 1].
S7. Therefore, [mini-link 1].

[BODY 2]
S8. Another important point is that [claim 2].
S9. This is particularly true when [mechanism / condition 2].
S10. For instance, [specific example 2].
S11. Consequently, [mini-link 2].

[CONCLUSION]
S12. In conclusion, I maintain that [position restated].
S13. For this reason, [final implication / recommendation].
```

---

## 3. Grammar Rails

Use these rules to keep the essay clean.

```text
RULE 1 — One sentence = one job
  Bad: claim + example + extra opinion in one long broken sentence
  Good: split them into S3 / S4 / S6

RULE 2 — Keep verbs simple unless complexity is useful
  Default tense: present simple
  Use past only for past examples or known past facts

RULE 3 — Force 2 complex sentences only
  Complex sentence target A: S4 or S9
    "This is because..."
    "This is particularly true when..."
    "Although..., ..."
  Complex sentence target B: S6 or S10
    "For example, when..., ..."

RULE 4 — Keep subject and verb close
  Bad: The main reason for this trend in many large modern cities with growing populations are...
  Good: The main reason is that...

RULE 5 — No new idea in conclusion
  S12 = restate
  S13 = implication only
```

Safe grammar patterns:

```text
Reason:
  "One reason for this is that..."

Mechanism:
  "This is because..."
  "This means that..."
  "When..., people can..."

Concession:
  "Although this may be true, ..."
  "While some people argue that..., I believe..."

Example:
  "For example, in many schools / companies / cities..."

Result:
  "As a result, ..."
  "Consequently, ..."
```

---

## 4. Mutation Switch

Do not rebuild the whole structure. Only change what each body paragraph is doing.

```text
OPINION (fully agree / disagree)
  S2 = clear position
  Body 1 = reason 1 supporting your view
  Body 2 = reason 2 supporting your view

OPINION (partial agree)
  S2 = "While X has some merit, I believe Y because A and B."
  Body 1 = opposing side / limited merit
  Body 2 = your stronger position

DISCUSSION
  S2 = "This essay will examine both views before arguing that..."
  Body 1 = view you reject or find weaker
  Body 2 = view you support

ADVANTAGES / DISADVANTAGES (outweigh)
  S2 = state which side is stronger
  Body 1 = weaker side
  Body 2 = stronger side

PROBLEM / SOLUTION
  S2 = main problem + broad solution direction
  Body 1 = problem / cause
  Body 2 = solution

TWO-PART QUESTION
  S2 = answer both questions directly
  Body 1 = answer Q1
  Body 2 = answer Q2
```

Rule: put your real position in **Body 2**, not Body 1.
That gives the essay stronger ending pressure.

---

## 5. Demo

### Prompt

```text
Some people think schools should spend more time teaching practical skills such as managing money and car maintenance, while others believe academic subjects are more important.
To what extent do you agree or disagree?
```

### Step A — Fill The Slots First

```text
Mutation:
  Opinion (partial agree)

Position:
  Academic subjects remain more important, but practical skills should still be taught.

Body 1 claim:
  Practical skills help students handle adult life.

Body 1 mechanism:
  Students often leave school without knowing how to budget or manage basic responsibilities.

Body 1 example:
  Young adults may earn money but still fall into debt because they cannot plan spending.

Body 2 claim:
  Academic subjects should still be the core of schooling.

Body 2 mechanism:
  These subjects build analytical ability and open access to university and skilled jobs.

Body 2 example:
  Strong literacy and numeracy are needed in almost every profession.
```

### Step B — Write Directly On The Architecture

```text
It is often argued that schools should focus more on practical life skills, whereas others believe academic subjects should remain the priority. While practical abilities are undeniably useful, I believe academic subjects are more important overall because they build long-term intellectual foundations and create wider career opportunities.

The first reason for this is that practical skills can help students manage adult life more effectively. This is because many young people leave school without understanding how to budget, save money, or deal with routine responsibilities. As a result, they may struggle with financial pressure even when they have a stable income. For example, some school leavers begin working immediately but quickly fall into debt simply because they have never learned how to control their spending. Therefore, there is a strong case for including basic practical training in the school curriculum.

Another important point is that academic subjects should still form the core of education. This is particularly true when students need to develop the literacy, numeracy, and reasoning skills required in higher education and most professions. For instance, a student who wants to become an engineer, doctor, or business manager must be able to analyse information, solve problems, and communicate clearly. Consequently, subjects such as mathematics, science, and language remain more valuable in the long term than narrower practical lessons.

In conclusion, although practical skills deserve a place in school, I maintain that academic subjects should remain the main focus. For this reason, schools should teach practical knowledge as a supplement rather than a replacement for traditional academic study.
```

### Why This Demo Works

```text
S1-S2   = clear paraphrase + nuanced thesis
S3-S7   = limited concession side, fully developed
S8-S11  = main position, placed last for stronger impact
S12-S13 = no new idea, only restatement + recommendation
```

---

## 6. Compression Ladder

Train in 3 layers.

```text
Layer 1 — Full scaffold
  Fill all 13 sentence slots exactly

Layer 2 — Reduced scaffold
  Write only slot labels + keywords, then draft from memory

Layer 3 — Internalized structure
  Look at mutation only, then write the essay without the sheet
```

Do not jump to Layer 3 early.
That is ego.
Repetition on the visible scaffold is what burns the pattern into memory.

---

## 7. Daily Use Contract

```text
Before writing:
  1. Detect mutation
  2. Decide position
  3. Draft 2 body claims
  4. Fill the slot sheet

During writing:
  5. Expand each slot into 1 sentence
  6. Add only small smoothing phrases

After writing:
  7. Underline S2, S3, S8, S12
  8. Check grammar in S4, S6, S9, S10
  9. Remove any sentence that does two jobs badly
```

---

## Related

- [[projects/ielts-writing/README]]
- [[projects/ielts-writing/notes/task2-essay]]
- [[projects/ielts-writing/notes/mastery-plan]]

---
type: operation
title: Delegate Operation
created: '2026-04-25'
updated: '2026-04-27'
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
---
> **TL;DR**: DELEGATE lets Codex copy Duc's visible pattern and write bounded code only after Detect confirms the task is ownable/delegatable. The operation forbids invented features, surprise abstractions, and clever code Duc cannot audit immediately.

## Growth Contract
- Parent branch: [[development]]
- Node role: operation
- First parent link: [[development]]
- Growth trigger: split only if a distinct delegation mode becomes recurring enough to need its own rules, examples, and verification contract.
- Forbidden contents: Learn-mode teaching detail, broad architecture design, speculative helpers, and project-specific patch logs.
- Expected child types: delegation thresholds, patch-shape rules, guardrails, stop conditions, and verification patterns.

## Purpose

Delegate compresses execution after ownership exists.

```text
Duc's pattern is visible
  -> Codex copies it
  -> bounded patch
  -> verification Duc can rerun
```

Delegate is not a shortcut around learning. It is the payoff after learning and development have raised the floor.

## Mandatory Entry

Always run [[wiki/operations/detect-operation]] first.

```text
request to patch/write/code
  -> Detect
  -> Delegate only if OWNABLE, DELEGATABLE, or ONE_TIME_UTILITY
```

## User Triggers

- "delegate this"
- "write this following my pattern"
- "patch this"
- "copy this shape into the next file"
- "implement this bounded seam"

If the request is ambiguous, Detect asks the missing threshold question before coding.

## Delegation Standard

Delegation is allowed only when Duc can audit immediately.

```text
Duc can name:
- files/modules involved
- input entering the seam
- output leaving the seam
- existing pattern to copy
- expected failure mode
- verification command or inspection path
```

If the pattern is still forming, route to [[wiki/operations/learn-operation]] instead.

## Prime Rule

```text
Copy the pattern.
Do not invent the system.
```

Codex may write code inside the existing shape. Codex must not silently add new feature surface.

## Owner Boundary Rule

When Duc names the owner layer, Codex must keep the patch inside that layer.

```text
prompt-only request
  -> prompt/schema/tests only
  -> no helper, sanitizer, normalizer, parser, fallback, or runtime cleanup

adapter-only request
  -> adapter-local patch only
  -> no graph, DB, prompt, or state change unless named first

schema-only request
  -> schema contract and matching tests only
  -> no behavior layer pretending to be validation
```

If passing verification seems to require code outside the named owner layer, stop and report the mismatch instead of adding the extra layer. Hidden helper code added to make a prompt contract reliable is delegation failure unless Duc explicitly approves that code-owned mechanism.

## Explain-Before-Code Rule

If Duc cannot explain the approach in detail yet, do not write the code.

```text
no clear Duc-owned pattern
  -> no delegation
  -> VIBE_DOC / audit / ask threshold question first
```

Explained-enough is not the same as write-owned. Duc may describe a direction clearly while still needing the mechanism as a VIBE_DOC before implementation.

```text
Duc asks for docs / mechanism / how to do it
  -> VIBE_DOC first
  -> neutral skeleton and official-doc-shaped explanation
  -> no repo patch unless Duc explicitly says patch/apply/write it
```

Before adding any extra feature surface, helper, migration, state field, schema change, abstraction, or fallback, Codex must state it explicitly and get the mechanism into the open. Silent additions are delegation failure, even when they are technically useful.

Minimum pre-code statement for delegated work:

```text
I will change <file> by copying <pattern>.
I will add <new surface> because <reason>.
If this is not the intended mechanism, stop me before I patch.
```

If the new surface cannot be explained in one or two plain sentences, it is too complex for Delegate and must route back to Learn/AUDIT.

## Guardrails

Forbidden unless explicitly justified and necessary before the patch:

- new feature
- new public function
- new helper function
- new class or abstraction
- new dependency
- new state layer
- new storage table
- new schema migration helper
- new sanitizer/normalizer/parser
- broad error framework
- hidden fallback behavior
- speculative edge-case handling
- changing architecture while pretending to patch locally

The exact failure this prevents:

```text
"Why the hell do you need to sanitize an LLM response?"
```

If a sanitizer, helper, migration, or new function is genuinely necessary, state why before the patch and keep it minimal. If it appears during implementation, pause and inform Duc before adding it.

## Allowed Work

```text
- fill a bounded function body
- copy an existing local pattern
- wire one named seam
- add narrow tests/smokes matching existing style
- repair a confirmed bug
- make mechanical consistency edits
- update docs/logs required by the change
```

## Patch Shape

Before editing, state:

```text
DETECT: DELEGATABLE.
I will edit [files].
I will copy [existing pattern].
I will not add [out-of-scope surfaces].
Verification: [command/check].
```

For tiny one-time utilities, this can be compressed, but the guardrails still apply.

## During Implementation

```text
1. Inspect the existing pattern.
2. Edit the smallest file set.
3. Avoid style drift.
4. Run focused verification.
5. Report changed paths and result.
```

Do not refactor unrelated code. Do not optimize code Duc did not ask to touch.

## Stop Conditions

Stop and route back to Learn if:

- no pattern exists to copy
- the obvious implementation needs a new abstraction
- the task requires architecture choices not in the blueprint
- verification path is unknown
- the patch would be faster to trust than understand

## Output Shape

Final response should be compact:

```text
Implemented [bounded change].
Changed: [paths].
Verified: [command/result].
Note: [only important caveat].
```

## Related

- [[development]]
- [[wiki/operations/detect-operation]]
- [[wiki/operations/learn-operation]]
- [[projects/raven/notes/raven-ownership-delegation-protocol]]
- [[wiki/pre-wire-protocol]]

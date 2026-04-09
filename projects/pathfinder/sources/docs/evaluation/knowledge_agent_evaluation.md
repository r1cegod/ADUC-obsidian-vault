# Knowledge Agent Evaluation Guide

> **TL;DR**: This guide defines how to evaluate PathFinder's pure reasoning stages: `thinking`, `purpose`, and `goals`. Their hardening seam is not retrieval quality but whether the extractor, analyst, and final compiler-output all preserve the intended contradiction and `PROBE:`.

Last updated: 2026-04-09

## Purpose
This document defines the evaluation model for PathFinder's knowledge agents:

- `thinking`
- `purpose`
- `goals`

These stages are **reasoning-only** agents:

```text
confident_node -> analyst -> output compiler
```

They do not fail like data agents. The core risks are:
- overconfident extraction from polished self-report
- analyst reasoning that notices a contradiction but hands off a weak `PROBE:`
- final Vietnamese output that softens a good internal handoff into generic counseling

## Source Contracts
- Official evaluation workflow: `eval/HOW_TO_USE.md`
- Stage prompt audit rules: `docs/prompt/docs/stage_prompt.md`
- Stage-to-compiler replay seam: `projects/pathfinder/sources/docs/delegated/evaluation_graph.md`
- Retrieval-agent counterpart: `docs/evaluation/data_agent_evaluation.md`

Prompt-level contracts already in force:
- extractors must hold unverified self-report under the verification ceiling
- analysts must hand off one concrete contradiction-carrying `PROBE:`
- output compiler is the only student-facing response generator

## Evaluation Model

### 1. Extractor Calibration
Did the extractor keep confidence bounded until the student survived a real squeeze?

Pass:
- self-report alone stays under the verification cap
- one-turn alignment with priors does not count as proof
- `done` stays `False` while core fields are still unverified

Fail:
- polished language or prior alignment pushes fields over `0.7`
- one-turn rejection of priors locks a replacement identity too early
- `done=True` appears before the student survives a trade-off

### 2. Analyst Contradiction Quality
Did the analyst identify the real contradiction instead of paraphrasing the student's claim?

Pass:
- contradiction is explicit and structural
- prior-vs-claim crashes are named directly when present
- unresolved fields stay visibly unresolved

Fail:
- reasoning is plausible but non-committal
- contradiction is hinted at but not weaponized
- the analyst drifts into generic coaching language

### 3. `PROBE:` Quality
Did the stage end with one usable next squeeze?

Pass:
- exactly one concrete next attack
- `PROBE:` targets the highest-priority unresolved field
- the probe forces a sacrifice, conflict, or zero-sum choice

Fail:
- generic "why?" question
- multiple weak directions at once
- contradiction exists in reasoning but disappears in the final `PROBE:`

### 4. Compiler-Prompt Preservation
Did `context_compiler` preserve the stage handoff?

Pass:
- `compiler_prompt` still contains the stage reasoning
- trailing `PROBE:` survives prompt assembly
- the relevant stage is still visible to `PROFILE_CONTEXT_BLOCK`

Fail:
- stage reasoning is missing from the compiler prompt
- `PROBE:` disappears between analyst output and compiler prompt
- stage-local attack shape is lost before the output model even runs

### 5. Final Output Preservation
Did the final Vietnamese response preserve the attack?

Pass:
- final reply still carries the contradiction or trade-off
- forced-choice pressure survives into student-facing language
- tone may adapt, but the structural squeeze stays intact

Fail:
- final reply turns into soft summary or affirmation
- contradiction is blurred into generic encouragement
- the output asks for more detail without pressure or sacrifice

## Evaluation Layers

### Layer A. Stage-Local Replay
This is the first hardening seam.

Goal:
- harden extractor ceilings
- harden analyst contradiction handling
- make the `PROBE:` reliable

Shape:

```text
target extractor -> target analyst
```

Use this layer to answer:
- did the stage itself produce the right internal handoff?

### Layer B. Stage + Compiler Replay
This is the visible-response seam.

Goal:
- verify the final Vietnamese output preserves the stronger internal handoff

Shape:

```text
evaluation_prep
  ->
target stage graph
  ->
context_compiler
  ->
output_compiler
```

This is the current `*_eval` seam:
- `thinking_eval`
- `purpose_eval`
- `goals_eval`

Use this layer to answer:
- did the visible response preserve the stage-local attack?

### Layer C. Full Orchestrator Replay
This is out of scope for the knowledge-agent guide as the default gate.

Use it only when the question is about:
- routing
- classification
- counters
- escalation behavior

Do not use orchestrator replay as the cheapest first proof of handoff preservation.

## Stage-Specific Priorities

### Thinking
Primary risks:
- prior-aligned self-report inflation
- one-turn contradiction lock-in
- weak `PROBE:` tension despite good reasoning

### Purpose
Primary risks:
- polished motives mistaken for stable drivers
- contradiction between stated desire and actual trade-off tolerance
- analyst sees the contradiction but ends with a softened probe

### Goals
Primary risks:
- aspiration language treated as operational plan
- short-term and long-term goals not forced into conflict
- output compiler flattening a good forced choice into generic planning talk

## Trace Audit Checklist
For each trace, inspect all three layers:

### Extractor State
- did confidence stay under the cap?
- did unresolved fields remain unresolved?
- did `done` stay consistent with the evidence?

### Analyst Handoff
- is the contradiction explicit?
- is the trailing `PROBE:` clean and singular?
- does the `PROBE:` attack the highest-priority unresolved field?

### Output Compiler
- does `compiler_prompt` still contain the stage reasoning and `PROBE:`?
- does the final Vietnamese reply preserve the squeeze?
- did the compiler sharpen or blunt the attack?

## Failure Taxonomy
When a run fails, classify it before patching:

- `calibration_fail`: extractor confidence rose too early
- `reasoning_fail`: analyst missed or blurred the contradiction
- `probe_fail`: `PROBE:` exists but is weak, generic, or mis-targeted
- `prompt_assembly_fail`: stage reasoning or `PROBE:` is lost in `compiler_prompt`
- `output_blunt_fail`: final Vietnamese reply softens the attack too much

Patch the narrowest failing layer:
- calibration failures usually belong in the extractor prompt or guard
- reasoning/probe failures usually belong in the analyst prompt
- prompt-assembly failures belong around `build_compiler_prompt()` or replay normalization
- output-blunt failures belong in the output compiler prompt contract

## Recommended Documentation Pattern
Use the same audit rhythm as the stage-specific logs:

1. Architecture and understanding
2. Vulnerabilities identified
3. Attack plan
4. Expectation map
5. Execution results
6. Current verdict
7. Attack-point checklist
8. Open gap

Add a Stage + Compiler section when the stage reaches the `*_eval` seam.

## Minimum Definition Of "Pass"
A knowledge-agent attack only passes if all of the following are true:

- extractor confidence respected the verification contract
- analyst reasoning identified the real contradiction
- `PROBE:` stayed concrete and singular
- `compiler_prompt` preserved the stage handoff
- final Vietnamese output preserved the attack shape

If any one of those fails, the stage is not hardened at the visible-response seam yet.

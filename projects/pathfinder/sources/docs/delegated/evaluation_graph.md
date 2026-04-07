# Evaluation Graph

> **TL;DR**: Add a cheap end-to-end eval seam that runs `stage_graph -> context_compiler -> output_compiler` without the high-cost orchestrator. This validates whether stage-local `PROBE:` and reasoning survive into the final Vietnamese student-facing reply.

Last updated: 2026-04-07

## What It Is

`evaluation_graph.py` is a new wrapper module for replay evaluation.

It does not replace the stage graphs.
It does not replace the orchestrator.
It exists to test the missing seam between them:

```text
stage-local reasoning
  ->
compiler prompt assembly
  ->
final Vietnamese response
```

Today the eval runner can do only three things:

- run a stage graph by itself
- run `output_graph` by itself
- run the full `orchestrator`

That leaves one expensive and one blind option:

- `orchestrator` is realistic but uses the high model in `input_parser`
- `stage` alone proves the internal handoff, but not whether the compiler weaponizes it correctly

`evaluation_graph.py` fills that gap.

---

## Production Gap This Solves

Knowledge agents are close to production-ready at the stage-local level.
What is still unproven is the student-facing response seam.

The unresolved question is not:

```text
"Can the analyst write a strong PROBE:?"
```

That has mostly been answered.

The unresolved question is:

```text
"When the compiler receives that stronger handoff, does the final Vietnamese reply preserve it?"
```

That is the right next production gate for `thinking`, `purpose`, and `goals`.

This seam can also serve `job`, `major`, and `university` later, but the immediate production target is the knowledge-agent trio.

---

## Why Skip The Orchestrator

The orchestrator is the wrong tool for this specific replay step.

```text
What we need to test now:
  stage output -> compiler behavior

What the orchestrator adds:
  input parsing
  message classification
  user_tag generation
  counter updates
  stage routing
  high-model cost
```

For this replay seam, the expensive part is mostly noise.

The compiler is still required because it is the only student-facing response generator.
The orchestrator is not required because the dataset can inject the state it normally produces.

So the boundary becomes:

```text
JSONL state
  ->
evaluation_prep
  ->
target stage graph
  ->
context_compiler
  ->
output_compiler
```

This is the cheapest graph that still tests visible behavior.

---

## Exact Scope

This seam validates:

- the target stage extractor behavior
- the target stage analyst or synthesis handoff
- `build_compiler_prompt(state)` on the resulting state
- the final `AIMessage` returned by `output_compiler`

This seam does **not** validate:

- `input_parser`
- `message_tag` classification quality
- `user_tag` classification quality
- counter logic
- escalation thresholds
- stage routing decisions across the full conversation

So the correct claim is:

```text
production-ready at the stage + compiler seam
```

Not:

```text
full-system production-ready
```

---

## File To Add

Add:

```text
backend/evaluation_graph.py
```

This module should export one compiled eval graph per stage.

Recommended exports:

```text
thinking_eval_graph
purpose_eval_graph
goals_eval_graph
job_eval_graph
major_eval_graph
uni_eval_graph
```

Phase priority:

1. `thinking_eval_graph`
2. `purpose_eval_graph`
3. `goals_eval_graph`
4. optional same pattern for data agents

Even if Phase 1 only certifies knowledge agents, the file should be built with a factory so all six stages can use one pattern.

---

## Required Graph Shape

Use a factory instead of six handwritten graphs.

```text
build_stage_evaluation_graph(stage_name, compiled_stage_graph)
  |
  +-> evaluation_prep
  +-> stage node
  +-> context_compiler
  +-> output_compiler
```

Target topology:

```text
START
  ->
evaluation_prep
  ->
{stage_name}
  ->
context_compiler
  ->
output_compiler
  ->
END
```

The stage node name should still match the stage string:

- `thinking`
- `purpose`
- `goals`
- `job`
- `major`
- `university`

That keeps the wrapper aligned with the existing stage contract.

---

## `evaluation_prep` Responsibilities

This node is the critical part.
Without it, the wrapper graph can silently produce misleading traces.

### 1. Seed `messages` when the row only provides the stage queue

Problem:

```text
stage graph reads:      {stage}_message
output_compiler reads:  messages
```

Many current stage-local datasets only provide the stage queue.
If `messages` stays empty, the compiler does not see the real human turn.

Required behavior:

```text
if messages is empty and target stage queue is not empty:
    copy target stage queue -> messages
```

This keeps existing datasets usable.

### 2. Seed `stage.stage_related` when missing

Problem:

`build_compiler_prompt()` only injects `PROFILE_CONTEXT_BLOCK` when the relevant stage is present in:

```text
stage.stage_related + stage.contradict_target
```

If `stage.stage_related` is empty, the target stage reasoning may never reach the compiler prompt even though the stage graph produced it correctly.

Required behavior:

```text
if stage.stage_related is empty:
    set it to [stage_name]
```

Do not overwrite explicit attack rows that intentionally set a different `stage_related`.

### 3. Keep `current_stage` valid even outside the runner

The runner already injects `current_stage` for stage-like specs.
The prep node should still normalize it so the graph is robust when invoked directly.

Required behavior:

```text
if stage.current_stage is empty:
    set it to stage_name
```

### 4. Do not fake orchestrator-only behavior

Do **not** invent:

- `message_tag`
- `user_tag`
- counters
- `path_debate_ready`

If those are important for a test, the JSONL row must provide them explicitly.
Otherwise the graph should run with the same safe defaults as `DEFAULT_STATE`.

---

## Why `evaluation_prep` Belongs In The Graph, Not The Runner

The runner should stay generic.

If the normalization is unique to compiler-wiring replay, it belongs with the replay graph.

That gives three advantages:

1. `eval/run_eval.py` stays a generic graph runner instead of learning one-off behavioral hacks.
2. Direct Python invocation of `thinking_eval_graph.invoke(...)` gets the same normalization.
3. The special logic lives next to the seam it exists to protect.

Runner changes are still needed for graph registration, but not for the special state stitching.

---

## `eval/run_eval.py` Changes

Add new graph specs, not a new runner mode.

Recommended canonical graph names:

```text
thinking_eval
purpose_eval
goals_eval
job_eval
major_eval
uni_eval
```

Recommended aliases:

```text
thinking_eval_graph
purpose_eval_graph
goals_eval_graph
job_eval_graph
major_eval_graph
uni_eval_graph
```

Each spec should point to:

- `module_path="backend.evaluation_graph"`
- `graph_attr="<stage>_eval_graph"`
- `default_queue=<stage queue>`
- `current_stage=<stage name>`

Examples:

```text
thinking_eval -> default_queue="thinking_style_message", current_stage="thinking"
purpose_eval  -> default_queue="purpose_message",        current_stage="purpose"
goals_eval    -> default_queue="goals_message",          current_stage="goals"
job_eval      -> default_queue="job_message",            current_stage="job"
major_eval    -> default_queue="major_message",          current_stage="major"
uni_eval      -> default_queue="uni_message",            current_stage="university"
```

No new CLI flag is required.

The existing command shape is enough:

```powershell
python eval/run_eval.py --mode multi --file eval/thinking_attack_v2.jsonl --graph thinking_eval
```

---

## Dataset Contract

Existing stage datasets should remain mostly usable.

### Safe default for old stage-local rows

If a row contains only the target stage queue:

```json
{
  "purpose_message": [
    {"role": "user", "content": "..."}
  ]
}
```

`evaluation_prep` should copy that queue into `messages` and seed:

```text
stage.current_stage = "purpose"
stage.stage_related = ["purpose"]
```

That is enough for a first replay.

### When the dataset must be more explicit

The row should explicitly provide extra state when the output behavior under test depends on:

- `message_tag`
- `user_tag`
- `stage.contradict`
- `stage.contradict_target`
- `stage.stage_related` containing multiple stages
- `stage_transitioned`
- `bypass_stage`
- `path_debate_ready`

Example:

```text
If you want to test contradiction phrasing,
inject contradict metadata directly.
Do not expect evaluation_prep to infer it.
```

---

## Acceptance Criteria

The implementation is ready when all of the following are true:

1. `thinking_eval`, `purpose_eval`, and `goals_eval` import successfully from `backend.evaluation_graph`.
2. `eval/run_eval.py` accepts the new graph names without a new mode.
3. A stage-local JSONL row with only the target queue still produces:
   - updated profile state
   - updated `stage_reasoning`
   - non-empty final `messages` output from `output_compiler`
4. The compiler prompt includes the target stage reasoning even when the input row omitted `stage.stage_related`.
5. No call to the high-model orchestrator is needed for this replay path.
6. Existing stage graphs stay unchanged.

---

## Minimal Test Plan

### Import smoke

```powershell
venv\Scripts\python -c "from backend.evaluation_graph import thinking_eval_graph, purpose_eval_graph, goals_eval_graph; print('OK')"
```

### Runner registration

```powershell
venv\Scripts\python eval/run_eval.py --mode multi --file eval/thinking_attack_v2.jsonl --graph thinking_eval
venv\Scripts\python eval/run_eval.py --mode multi --file eval/purpose_attack.jsonl --graph purpose_eval
venv\Scripts\python eval/run_eval.py --mode multi --file eval/goals_attack.jsonl --graph goals_eval
```

### Contract test

Add a small test file for the wrapper seam.
At minimum lock these cases:

- stage-queue-only input still yields non-empty `messages`
- missing `stage.stage_related` still yields compiler prompt with stage reasoning
- explicit `stage.stage_related` is preserved, not overwritten

---

## Recommended Implementation Order

1. Add `backend/evaluation_graph.py` with a small factory and `evaluation_prep`.
2. Register the six new graphs in `eval/run_eval.py`.
3. Add one contract test for the prep normalization behavior.
4. Run `thinking_eval`, `purpose_eval`, `goals_eval`.
5. Audit the traces for whether the final Vietnamese response preserves the stronger handoff.

---

## Non-Goals

Do not do these in the same change:

- refactor orchestrator logic
- change stage prompts
- redesign `build_compiler_prompt()`
- add a new eval runner mode
- move datasets into a new format

This is a seam-wrapper change, not an architecture rewrite.

---

## Final Decision

The right next production gate is **not** full orchestrator replay for every attack.
The right next gate is a cheaper wrapper graph that proves:

```text
stage-local handoff
  ->
compiler prompt
  ->
student-facing reply
```

That is the missing step before calling the knowledge agents production-ready at their visible-response seam.

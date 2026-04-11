# Major Agent Evaluation & Audit Log

Updated: 2026-04-09

> **TL;DR**: `major` already passed the current stage-local and Stage 4 wrapper seam on 2026-04-07, and the 2026-04-09 confidence-lock audit confirmed the extractor still keeps every done-driving field below Python's `> 0.8` gate on the current attack suite.

## 1. Architecture & Understanding
- **Extractor (Nova):** Extracts `field`, `curriculum_style`, and `required_skills_coverage` from the `major_message` queue. It must enforce the verification cap so a named major stays `<= 0.6` until the student survives the curriculum / necessity squeeze.
- **Planner / Researcher / Synthesizer (Riven):** Reads `thinking`, `purpose`, `goals`, `job`, `message_tag`, current `major` state, and `stage_reasoning.major`. It now owns search-trigger decisions, Vietnam-specific query formulation, evidence grounding, and the final `PROBE:` anchor.
- **Evaluation seam:** This is a retrieval-plus-reasoning stage. A pass requires more than clean prose. The run must search on new major-field claims, target the right Vietnam curriculum/necessity barrier, use the evidence in the reasoning, embed the contradiction into `PROBE:`, and keep extractor confidence under the verification cap until the student actually defends the bridge.
- **Stage 4 seam:** `major_eval` must also preserve that contradiction through `context_compiler` and `output_compiler`, not just inside `stage_reasoning.major`.

## 2. Vulnerabilities Identified
1. **V1 - Legacy ToolNode drift:** `major_graph.py` still used the old prompt-bound `search` ToolNode loop, unlike `job_graph.py`'s explicit planner -> researcher -> synthesizer seam. That left retrieval discipline and post-search handoff too implicit.
2. **V2 - New-field trigger weakness:** the major planner could still skip research on a fresh major-field claim if the student already sounded self-aware. This is especially dangerous on Dreamer paths, where the exception changes the barrier under test, not the need to search.
3. **V3 - Curriculum-vs-learning-mode ambiguity:** the analyst must turn `thinking.learning_mode` versus local curriculum reality into a real crash, not just a note.
4. **V4 - Safe-major compliance:** students can instantly accept a safer broad major under pressure without proving that it bridges to the target job.
5. **V5 - Dreamer bridge inflation:** strong ownership should validate the hard path, but it must not silently upgrade `required_skills_coverage` without a concrete self-teaching execution plan.

## 3. Round 1 Production Target & Attack Plan
**Round:** 1  
**Target stage:** `major`  
**This round must prove:** the new `major` research seam behaves like `job`'s seam, and the contradiction survives both stage-local replay and `major_eval`.  
**User-facing behavior shift to surface:** major analysis becomes more explicit about degree necessity, curriculum reality, and Dreamer execution barriers.

| # | Name | Attack Vector | Targeted Failure State |
|---|------|--------------|------------------------|
| 1 | The Broad Major Shortcut | Student wants UI/UX but chooses Business Administration because it feels safe and broad. | No search, weak transferability query, or generic advice instead of a degree-vs-portfolio squeeze. |
| 2 | The Theory-Heavy Vehicle | Hands-on builder wants public-university CS despite poor fit for theory-heavy assessment. | Analyst notes the mismatch but fails to turn it into a curriculum crash. |
| 3 | The Dreamer Curriculum Gap | Student accepts Graphic Design plus heavy self-study to chase concept art. | Planner skips search because the student already sounds committed; analyst validates grit without isolating the execution barrier. |
| 4 | The Instant Safe Pivot | Student immediately accepts a safer business major after pressure. | Compliance is mistaken for proof and the bridge stays vague. |

## 4. Expectation Map
**Attack 1 - The Broad Major Shortcut**
- `Nova`: `field` may reach the self-report cap, but `required_skills_coverage` must stay weak.
- `Riven`: must search Vietnam UI/UX hiring transferability and keep the bridge-to-portfolio contradiction inside `PROBE:`.

**Attack 2 - The Theory-Heavy Vehicle**
- `Nova`: `curriculum_style` may become descriptive, but the stage must not mark `done=True`.
- `Riven`: must target the teaching/assessment reality and explicitly crash it into `thinking.learning_mode`.

**Attack 3 - The Dreamer Curriculum Gap**
- `Nova`: ownership can rise, but `required_skills_coverage` must stay below verification until the missing pipeline is made concrete.
- `Riven`: must still search. The Dreamer exception validates the ambition while probing the exact pipeline/portfolio barrier.

**Attack 4 - The Instant Safe Pivot**
- `Nova`: compliance cannot raise certainty.
- `Riven`: must treat the safe pivot as weak ownership and force a degree-signal versus product-portfolio trade-off.

## 5. Execution Results
**Run date:** 2026-04-07  
**Stage replay command:** `venv\Scripts\python eval/run_eval.py --mode multi --file eval/major_attack.jsonl --graph major`  
**Stage 4 seam replay command:** `venv\Scripts\python eval/run_eval.py --mode multi --file eval/major_attack.jsonl --graph major_eval`

### 5A. Draft Refactor Applied
The old major ToolNode loop was replaced with the same explicit research seam already proven in `job_graph.py`:
- `confident_node`
- `major_research_planner`
- `major_researcher`
- `major_synthesizer`

This also added a new state field:
- `major_research` in `PathFinderState`

Prompt changes for the draft:
- `MAJOR_CONFIDENT_PROMPT` now keeps the self-report cap and bridge-proof rules explicit.
- `MAJOR_RESEARCH_PLAN_PROMPT` forces one contradiction-focused search request and now hard-requires research on new major-field claims, including Dreamer paths.
- `MAJOR_SYNTHESIS_PROMPT` consumes `major_research` and writes a structured `PROBE:` handoff.

### 5B. Verification
**Import / contract verification:**
- `venv\Scripts\python -c "from backend.data.state import MajorResearch; print('state-ok')"`
- `venv\Scripts\python -c "from backend.major_graph import major_graph; print('major-graph-ok')"`
- `venv\Scripts\python -m unittest test_stage_contract.py test_evaluation_graph_contract.py`

**Replay results:**
- `major`: 4 inputs, 4 succeeded, 0 failed
- `major_eval`: 4 inputs, 4 succeeded, 0 failed

**Observed warning noise:**
- Trace-time Pydantic serializer warnings still fire around structured-output serialization. They do not break the run, but they remain a cross-cutting cleanup item.

### 5C. Replay Findings
**Attack 1 - The Broad Major Shortcut:** **PASS.**
- The planner searched Vietnam UI/UX transferability rather than generic major explainers.
- Final reasoning preserved the degree-vs-portfolio contradiction and kept `required_skills_coverage` weak.

**Attack 2 - The Theory-Heavy Vehicle:** **PASS.**
- The planner aimed at curriculum reality, not prestige.
- Final reasoning preserved the hands-on-builder versus theory-heavy-assessment clash and pushed it into the final Vietnamese forced choice.

**Attack 3 - The Dreamer Curriculum Gap:** **PASS after one prompt fix.**
- First replay exposed a real planner bug: the Dreamer case skipped research entirely even though a new `field` was introduced.
- Fixed by tightening the planner with a hard trigger: new `field` claims must search, and Dreamer paths still search for the execution barrier.
- Final replay then searched the game-art barrier correctly and kept the contradiction on pipeline depth rather than on motivation.

**Attack 4 - The Instant Safe Pivot:** **PASS.**
- The planner treated the student's compliance as safe-major drift, not as validation.
- Final reasoning kept the bridge unproven and forced a safety-versus-portfolio trade-off in both stage-local and Stage 4 wrapper runs.

**Current verdict:**
- The `major` stage now matches the `job` architecture: explicit planner -> researcher -> synthesizer seam, dedicated `major_research` packet, and a reliable trailing `PROBE:`.
- `major_eval` also passes the current stage + compiler seam on `eval/major_attack.jsonl`.
- The main open risk is no longer contradiction loss in `major`; it is the same serializer-warning noise already visible in `job_eval`.

## 6. Attack Point Checklist
- [x] Did Riven search on every new `field` claim?
- [x] Were queries Vietnam-specific and aimed at the real contradiction?
- [x] Did the reasoning clearly depend on retrieved evidence when evidence was present?
- [x] Did `PROBE:` survive every trace after research?
- [x] Did `major_eval` preserve the contradiction into the final Vietnamese reply?
- [x] Did Nova keep unverified major claims under the self-report cap?
- [x] Did Dreamer handling validate grit without skipping the execution-barrier search?
- [x] Did compliance pivots stay weak instead of becoming proof?

## 7. 2026-04-09 Confidence-Lock Audit
- **Production target:** align `MAJOR_CONFIDENT_PROMPT` with Python's shared `> 0.8` done-count gate so provisional `0.7-0.8` bridge ownership cannot be mistaken for a locked major decision.
- **Prompt change:** the extractor now treats `0.7-0.8` as provisional, reserves `> 0.8` for lock-safe fields only, and names Python as the owner of done counting.
- **Replay commands:**
  - `venv\Scripts\python eval/run_eval.py --mode multi --file eval/major_attack.jsonl --graph major`
  - `venv\Scripts\python eval/run_eval.py --mode multi --file eval/major_attack.jsonl --graph major_eval`
- **Audit findings:**
  - All 8 replay runs succeeded.
  - Every `major.done` stayed `False` in both the stage-local and `major_eval` traces.
  - Fresh extractor outputs stayed below the lock gate on all done-driving fields:
    - Attack 1: `field=0.58`, `curriculum_style=0.32`, `required_skills_coverage=0.22`
    - Attack 2: `field=0.58`, `curriculum_style=0.56`, `required_skills_coverage=0.44`
    - Attack 3: `field=0.60`, `curriculum_style=0.55`, `required_skills_coverage=0.45`
    - Attack 4: `field=0.55`, `curriculum_style=0.45`, `required_skills_coverage=0.00`
- **Verdict:** the `major` extractor now matches the Python gate cleanly. None of the audited attacks produced a lock-safe `> 0.8` score on a done-driving field.
- **Residual risk:** trace serialization still emits the same cross-cutting Pydantic serializer warnings.

## 8. 2026-04-11 Live Trace Goals-Handoff Replay
**Production target:** when Goals hands off concrete skills and portfolio proof, Major must dig out the correct qualification route instead of asking Goals-style planning questions again.

**Prompt-only contract change:**
- Major reads Goals as directional context.
- Major converts short-goal assumptions into academic vehicle, curriculum style, self-study/project bridge, and credential/portfolio necessity.
- Concrete qualification evidence can cross `> 0.8` without requiring university-specific research in the extractor.

**Dataset:** `eval/live_trace_major_rounds.jsonl`
- Round 1: CS/software-data path for AI agents, Python, SQL, system design, light frontend.
- Round 2: project-heavy learning mode versus theory-only curriculum risk.
- Round 3: degree not primary; foundation plus paid product/contract proof.

**Command:**
- `venv\Scripts\python eval\run_eval.py --mode multi --file eval\live_trace_major_rounds.jsonl --graph major_eval --workers 1`

**Final verified traces:**
- Round 1: `eval/threads/49084a82-2617-40a6-8004-06254582b1f0/traces/run_0001.json`
- Round 2: `eval/threads/fb718102-c275-4ab3-87ef-9eb906e861ce/traces/run_0002.json`
- Round 3: `eval/threads/a17469d2-83dd-45d5-9828-73624a66867f/traces/run_0003.json`

**Round 3 result:** **PASS at the stage-wrapper seam.**
- `major.done=true`
- `field = "Computer Science"`, `0.90`
- `curriculum_style = "project-based execution"`, `0.89`
- `required_skills_coverage = "aligned with backend/data foundations for databases, search tools, graph-based agents, Python, SQL, and system design, with a portfolio-to-paid-work bridge"`, `0.84`

**Residual risk:** `major_eval` used web research on the curriculum reality seam, but the current claim still excludes full orchestrator routing.

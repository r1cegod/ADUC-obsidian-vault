# University Agent Evaluation & Audit Log

Updated: 2026-04-07

> TL;DR: Round 1 starts by moving `uni` off the legacy ToolNode loop onto the `job`-style retrieval seam so admissions, ROI, prestige, and international-cost checks can be evaluated through a structured `uni_research` packet.

## Round 1 Production Target
- Stage: `university`
- Round: `1`
- This round must prove that a new school claim triggers one narrow research step, the researcher returns usable evidence, the synthesizer embeds the contradiction into `PROBE:`, and the extractor keeps school/prestige confidence capped until the student defends the path.
- User-facing behavior change to surface after the round: the university stage should become stricter about school math and status claims, with fewer generic school follow-ups and more explicit ROI or admissions squeezes.

## 1. Architecture & Understanding
- **Extractor (Iris):** Extracts `prestige_requirement`, `target_school`, `campus_format`, and `is_domestic` from the `uni_message` queue. It must enforce the verification cap so a named school or prestige claim stays `<= 0.6` until the student survives an ROI, admissions, or prestige squeeze.
- **Research planner (Echo):** Reads `thinking`, `purpose`, `goals`, `job`, `major`, `message_tag`, `user_tag`, current `university` state, and `stage_reasoning.uni`. It decides whether search is required and emits one contradiction-focused query plus a domain bucket.
- **Researcher:** Uses the shared retrieval layer to fetch structured evidence into `uni_research`.
- **Synthesizer (Echo):** Reads `uni_research`, prior stages, and the current `university` profile, then writes the final internal handoff for the output compiler.
- **Evaluation seam:** This is a retrieval-plus-reasoning stage. A pass requires more than good prose. The run must search when required, form a sharp school-specific query, use the evidence in the reasoning, embed the contradiction into `PROBE:`, and keep extractor confidence under the verification cap until the student defends the path.
- **Evaluation locale:** Student-facing inputs remain Vietnamese because the real product serves Vietnamese students, even though the internal reasoning is English.

## 2. Vulnerabilities Identified
1. **V1 - Legacy tool-loop handoff risk:** `uni` still used the old ToolNode loop, so raw tool chatter sat inside the conversation queue instead of a stable research packet. That makes retrieval behavior harder to reason about and evaluate.
2. **V2 - School-name overconfidence:** The extractor could lock a specific school too early just because the student named it with conviction.
3. **V3 - Mixed-contradiction search drift:** The old prompt encouraged admissions, tuition, prestige, and visa checks together, which risks weak or noisy search queries.
4. **V4 - Weak evidence-to-probe contract:** Even if search happened, the final `PROBE:` could still collapse into a generic school follow-up instead of carrying the exact contradiction.
5. **V5 - International-path vagueness:** A foreign-school claim can sound impressive without any defended total-cost or visa-survival math.

## 3. Attack Plan

| # | Name | Attack Vector | Targeted Failure State |
|---|------|--------------|------------------------|
| 1 | The Prestige Reflex | Student wants an elite/status school for a job path that does not structurally require prestige. | No search, wrong query, or reasoning fails to weaponize the prestige-vs-job mismatch. |
| 2 | The ROI Crash | Student wants an expensive private school while holding a modest income target. | Tuition math is skipped or softened; extractor locks the school too early. |
| 3 | The Admissions Fantasy | Student wants a brutally competitive domestic school despite weak runway signals. | Query misses admissions reality, or probe does not force the student to confront the bar. |
| 4 | The International Blur | Student wants a foreign-school path with no defended total-cost or visa plan. | Search stays domestic, misses total attendance cost, or treats international prestige as self-verifying. |

## 4. Expectation Map

**Attack 1 - The Prestige Reflex**
- `Iris`: `target_school` and `prestige_requirement` must stay `<= 0.6`.
- `Echo`: must search the prestige gate or necessity question, then embed the status-vs-fit contradiction into `PROBE:`.

**Attack 2 - The ROI Crash**
- `Iris`: naming the expensive school must stay under the self-report cap.
- `Echo`: must search tuition or official cost data and force a cost-vs-income-target sacrifice in `PROBE:`.

**Attack 3 - The Admissions Fantasy**
- `Iris`: the school claim may reach the self-report cap, but not the defended threshold.
- `Echo`: must search exact admissions reality for the named school/program and force the student to confront the runway gap.

**Attack 4 - The International Blur**
- `Iris`: `campus_format` and `is_domestic` can resolve categorically, but `done` must stay `False`.
- `Echo`: must search total-cost or visa reality for the named foreign-school path and preserve the cost/immigration contradiction.

## 5. Execution Results
**Run date:** 2026-04-07
**Command:** `venv\Scripts\python eval/run_eval.py --mode multi --file eval/uni_attack.jsonl --graph uni_eval`

### 5A. Draft Refactor Applied
- Replace the legacy ToolNode loop in `backend/uni_graph.py` with a dedicated Stage 5 research seam:
  - `confident_node`
  - `uni_research_planner`
  - `uni_researcher`
  - `uni_synthesizer`
- Add `uni_research` to `PathFinderState`.
- Split `backend/data/prompts/uni.py` into:
  - `UNI_CONFIDENT_PROMPT`
  - `UNI_RESEARCH_PLAN_PROMPT`
  - `UNI_SYNTHESIS_PROMPT`

### 5B. Draft Verification
- `venv\Scripts\python -c "from backend.uni_graph import uni_graph; print('uni-graph-ok')"`
- `venv\Scripts\python test_uni_graph_contract.py`
- `venv\Scripts\python -m unittest test_evaluation_graph_contract.py test_retrieval_service_contract.py`
- `venv\Scripts\python eval/run_eval.py --mode multi --file eval/uni_attack.jsonl --graph uni_eval`

Runtime result:
- 4 inputs
- 4 succeeded
- 0 failed

### 5C. Replay Findings
**Attack 1 - The Prestige Reflex:** **PASS.**
- The planner targeted the prestige-vs-portfolio contradiction instead of drifting into a generic school search.
- Research stayed focused on whether RMIT status actually changes freelance client trust.
- Final reasoning preserved the status-vs-fit crash, and the final Vietnamese reply asked for a forced choice between school prestige and portfolio-led fit.

**Attack 2 - The ROI Crash:** **PASS.**
- The planner narrowed the query to official tuition instead of mixing several school questions.
- Research populated a usable `uni_research` packet and the synthesizer preserved an explicit tuition-vs-income-target contradiction.
- `target_school` stayed at the self-report cap and `done=False`, which keeps the school choice unverified until the student defends the payback math.

**Attack 3 - The Admissions Fantasy:** **PASS.**
- The planner targeted exact admissions reality for Bách Khoa TP.HCM Computer Science.
- Research and synthesis preserved the gap between the school's competitive bar and the student's still-unproven runway.
- The final Vietnamese reply stayed sharp by forcing the student to compare their actual scores against the current cutoff instead of rewarding the ambition.

**Attack 4 - The International Blur:** **PASS.**
- The planner correctly switched to an international cost / work-permit query instead of treating the foreign-school name as self-verifying.
- Research grounded the contradiction in total-cost and post-graduation survival uncertainty.
- The final reply preserved the trade-off between real international-fit logic and status-driven study-abroad fantasy.

**Current verdict:**
- The Round 1 draft works at the current `uni_eval` stage + compiler seam. All 4 attacks now produce a populated `uni_research` packet, a non-empty `stage_reasoning.uni` with a trailing `PROBE:`, and a final Vietnamese contradiction that stays aligned with the research seam.
- One real bug surfaced during the first replay: the synthesizer could emit invalid probe-field names like `tuition` or `college`. A Python guard now normalizes any invalid probe field back to a real `UniProfile` field before composing the final `PROBE:` line, and the dataset was re-run successfully after that patch.
- The remaining cleanup item is the same trace-time Pydantic serializer-warning noise already seen on other structured-output stages. It does not break the run, but it is still cross-cutting debt.

## 6. Attack Point Checklist
- [x] Did Echo search on every new `target_school` or prestige-critical school claim?
- [x] Were queries narrow and aimed at the right contradiction?
- [x] Did the reasoning clearly depend on retrieved evidence when evidence was present?
- [x] Did `PROBE:` survive every trace after research?
- [x] Did `PROBE:` carry the contradiction rather than collapse into a generic school follow-up?
- [x] Did Iris keep unverified school and prestige claims under the self-report cap?
- [x] Did `done` stay `False` when the student had not defended the school path?

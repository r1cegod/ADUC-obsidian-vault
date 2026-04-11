# Job Agent Evaluation & Audit Log

Updated: 2026-04-09

> **TL;DR**: `job` first exposed retrieval-stage failures around search and post-tool synthesis, and on 2026-04-07 it also passed the current Stage 4 `job_eval` seam: all 4 attacks kept populated research, a surviving `PROBE:`, and a sharp final Vietnamese contradiction.

## 1. Architecture & Understanding
- **Extractor (Nova):** Extracts `role_category`, `company_stage`, `day_to_day`, and `autonomy_level` from the `job_message` queue. It must enforce the verification cap so a named job title or company type stays `<= 0.6` until the student survives a market-data squeeze.
- **Analyst (Tess):** Reads `thinking`, `purpose`, `goals`, `message_tag`, current `job` state, and `stage_reasoning.job`. It owns search-trigger decisions, Vietnam-specific query formulation, evidence grounding, and the final `PROBE:` anchor for the output compiler.
- **Evaluation seam:** This is a retrieval-plus-reasoning stage. A pass requires more than good prose. The run must search when required, form a sharp VN-market query, use the evidence in the reasoning, embed the contradiction into `PROBE:`, and keep extractor confidence under the verification cap until the student defends the path.
- **Evaluation locale:** Student-facing inputs remain Vietnamese because the real product serves Vietnamese students, even though the analyst writes internal English reasoning.

## 2. Vulnerabilities Identified
1. **V1 - Prompt/state drift in the extractor:** `JOB_CONFIDENT_PROMPT` asks for `key_quote`, but `JobProfile` in state does not contain `key_quote`. This is a contract mismatch and raises the risk of confused extraction behavior.
2. **V2 - Title-first overconfidence:** The extractor currently has the right verification-cap language, but it does not explicitly punish glamour-title claims that name a role without naming the grind.
3. **V3 - Weak dependency enforcement:** The analyst says `day_to_day` must be verified before `autonomy_level` or `role_category` can lock, but the extractor prompt does not mirror that dependency explicitly.
4. **V4 - Missing explicit tension-embedding rule:** The analyst prompt asks for a Socratic trade-off, but it does not yet explicitly force the final `PROBE:` to carry the exact prior-vs-market contradiction.
5. **V5 - Dreamer-exception ambiguity:** The analyst has a Dreamer rule, but the threshold for when to validate ambition vs when to crush fantasy is still underspecified and needs trace verification.

## 3. Attack Plan

| # | Name | Attack Vector | Targeted Failure State |
|---|------|--------------|------------------------|
| 1 | The Fresh-Grad Fantasy | Student wants `Data Scientist` in Vietnam, fully remote, with very high fresh-grad pay. | No search, weak salary query, or extractor locks the title/autonomy too early. |
| 2 | The Glamour PM | Student picks `Product Manager` but wants solo deep work and hates meetings/conflict. | Analyst fails to use market reality against `thinking.social_battery`; probe stays generic. |
| 3 | The Remote Freelancer Illusion | Student wants freelance UI/UX with total schedule freedom despite strong structure/collaboration priors. | Analyst skips or weakens the autonomy crash; extractor locks autonomy from self-report. |
| 4 | The Niche Dreamer | Student wants a niche creative role in Vietnam with strong Dreamer priors already established. | Analyst crushes the ambition instead of validating the Dreamer path and probing the concrete barrier. |

## 4. Expectation Map

**Attack 1 - The Fresh-Grad Fantasy**
- `Nova`: `role_category`, `company_stage`, and `autonomy_level` must stay `<= 0.6`; `day_to_day` must stay weak if the student cannot name the grind.
- `Tess`: must search with a Vietnam-specific salary or market-reality query, then embed the pay/remote reality crash into `PROBE:`.

**Attack 2 - The Glamour PM**
- `Nova`: `role_category` may reach the self-report cap, but `day_to_day` must stay `< 0.5` and `autonomy_level` must not lock.
- `Tess`: must use PM market/day-to-day evidence and embed the contradiction between meetings/stakeholder work vs the student's solo-deep-work prior directly into `PROBE:`.

**Attack 3 - The Remote Freelancer Illusion**
- `Nova`: total-autonomy claims must remain capped until the student survives the grind test.
- `Tess`: must search against the actual freelance/UI-UX execution reality in Vietnam and force a structure-vs-freedom sacrifice in `PROBE:`.

**Attack 4 - The Niche Dreamer**
- `Nova`: niche-role desire alone must stay capped.
- `Tess`: must search the Vietnam market constraint, but if `purpose` and `goals` show a real Dreamer profile, the reasoning should validate the hard path and probe the concrete execution barrier instead of redirecting to the safe path.

## 5. Execution Results
**Run date:** 2026-04-05  
**Command:** `venv\Scripts\python eval/run_eval.py --mode multi --file eval/job_attack.jsonl --graph job`

### 5A. Draft Refactor Applied
The old direct tool loop was replaced with a dedicated Stage 3 research seam:
- `confident_node` keeps extractor confidence capped.
- `job_research_planner` decides whether research is needed and emits one narrow contradiction-focused search query.
- `job_researcher` calls the shared retrieval service with a domain allowlist from `backend/data/contracts/research_sources.py`; the fresh 2026-04-07 traces show the current provider chain as `serper`.
- `job_synthesizer` reads the structured `job_research` packet and writes the final `stage_reasoning.job`.

This also added a new state field:
- `job_research` in `PathFinderState`

Prompt changes for the draft:
- `JOB_CONFIDENT_PROMPT` keeps the self-report cap and day-to-day-first rules.
- `JOB_RESEARCH_PLAN_PROMPT` forces atomic query planning instead of giant mixed research requests.
- `JOB_SYNTHESIS_PROMPT` now consumes `job_research` rather than raw tool chatter.

### 5B. Draft Verification
**Import verification:**
- `venv\Scripts\python -c "from backend.data.state import JobResearch; print('state-ok')"`
- `venv\Scripts\python -c "from backend.job_graph import job_graph; print('job-graph-ok')"`

**Replay command:** `venv\Scripts\python eval/run_eval.py --mode multi --file eval/job_attack.jsonl --graph job`

Runtime result:
- 4 inputs
- 4 succeeded
- 0 failed

### 5C. Replay Findings
**Attack 1 - The Fresh-Grad Fantasy:** **PASS.**
- The planner narrowed the contradiction to Vietnam fresher Data Scientist salary reality.
- Research produced concrete salary bands and fresher postings.
- Final reasoning correctly crushed the `100M VND/month right after graduation` fantasy and preserved a `PROBE:` about real first-year grind.

**Attack 2 - The Glamour PM:** **PASS.**
- The planner targeted PM stakeholder load rather than title prestige.
- Research returned recurring evidence that PM work is cross-functional and meeting-heavy.
- Final reasoning preserved the contradiction between solo deep work and PM reality.

**Attack 3 - The Remote Freelancer Illusion:** **PASS.**
- The planner targeted remote/freelance UI/UX autonomy in the Vietnam market.
- Research showed that remote/freelance roles exist but usually still include meetings, reporting, and team coordination.
- Final reasoning preserved the structure-vs-freedom contradiction instead of drifting into generic encouragement.

**Attack 4 - The Niche Dreamer:** **PASS.**
- The planner treated the case as a market-availability check, not a fantasy crush by default.
- Research showed concept artist roles exist but are niche, location-clustered, and often skew mid-level.
- Final reasoning preserved the Dreamer exception while grounding it in sparse-role and long-portfolio-grind reality.

**Current verdict:**
- The draft works. All 4 attacks now produce a populated research packet and a non-empty `stage_reasoning.job` with a trailing `PROBE:`.
- The major failure mode has shifted from handoff collapse to evidence quality. The current shared retrieval path is materially better than the old giant-query approach, but cited source lists can still include noisy or weakly relevant pages.
- There are also trace-time Pydantic serializer warnings around structured outputs. They did not break the run, but they should be cleaned up before treating the architecture as fully settled.

## 6. Attack Point Checklist
- [x] Did Tess search on every new `role_category` or `company_stage` claim?
- [x] Were queries Vietnam-specific and aimed at the real contradiction?
- [x] Did the reasoning clearly depend on retrieved evidence when evidence was present?
- [x] Did `PROBE:` survive every trace after tool use?
- [x] Did `PROBE:` carry the contradiction rather than collapse into a generic follow-up?
- [x] Did Nova keep unverified job-title claims under the self-report cap?
- [x] Did `day_to_day` stay weak when the student could not name the grind?
- [x] Did the Dreamer exception validate grit without collapsing into fantasy approval?

## 7. Stage 4 Visible-Response Replay
**Run date:** 2026-04-07  
**Round:** 1  
**Production target:** Prove the cheaper `job_eval` seam (`job_graph -> context_compiler -> output_compiler`) still carries retrieval-grounded contradictions into the final Vietnamese reply without softening the `PROBE:`.

**Verification:**
- `venv\Scripts\python -c "from backend.evaluation_graph import job_eval_graph; print('job-eval-ok')"`
- `venv\Scripts\python -m unittest test_evaluation_graph_contract.py`
- `venv\Scripts\python eval/run_eval.py --mode multi --file eval/job_attack.jsonl --graph job_eval`

Runtime result:
- 4 inputs
- 4 succeeded
- 0 failed

### 7A. Stage 4 Findings
- All 4 fresh traces produced populated `job_research` packets with contradiction-focused Vietnam queries and 5 cited sources each.
- Every trace preserved the trailing `PROBE:` in both `stage_reasoning.job` and `compiler_prompt`.
- The final Vietnamese reply kept the intended contradiction instead of softening into generic coaching:
  - Attack 1 stayed a pay-versus-supervision/collaboration squeeze.
  - Attack 2 stayed a stakeholder-meeting-versus-solo-deep-work squeeze.
  - Attack 3 stayed a structure-versus-total-autonomy squeeze.
  - Attack 4 stayed Dreamer-validating but still grounded in repetitive pipeline/grind reality.
- Extractor confidence stayed capped where the student still had not named the grind:
  - Attack 1: `role_category=0.6`, `day_to_day=0.4`, `autonomy_level=0.6`
  - Attack 2: `role_category=0.58`, `day_to_day=0.0`, `autonomy_level=0.0`
  - Attack 3: `role_category=0.6`, `day_to_day=0.4`, `autonomy_level=0.6`
  - Attack 4: `role_category=0.55`, `day_to_day=0.0`, `autonomy_level=0.0`

### 7B. Current Verdict
- `job` now passes the current Stage 4 stage + compiler seam on `eval/job_attack.jsonl`.
- This is still not full-system proof. The wrapper graph skips orchestrator routing, message-tag classification, and counter behavior.
- Residual risk: trace-time Pydantic serializer warnings still fire around structured outputs. They did not break the run, but they should be cleaned before treating the same seam as settled for the remaining retrieval stages.

## 8. 2026-04-09 Confidence-Lock Audit
- **Production target:** align the `JOB_CONFIDENT_PROMPT` lock language with Python's shared `DONE_CONFIDENCE_THRESHOLD = 0.8` so `0.7-0.8` is explicitly provisional, not counted behavior.
- **Prompt change:** the extractor now says `0.7-0.8` is still provisional, `> 0.8` is the only lock-safe band, and downstream Python is the owner of done counting.
- **Replay commands:**
  - `venv\Scripts\python eval/run_eval.py --mode multi --file eval/job_attack.jsonl --graph job`
  - `venv\Scripts\python eval/run_eval.py --mode multi --file eval/job_attack.jsonl --graph job_eval`
- **Audit findings:**
  - All 8 replay runs succeeded.
  - Every `job.done` stayed `False` in both the stage-local and `job_eval` traces.
  - Fresh extractor outputs stayed below the lock gate on all done-driving fields:
    - Attack 1: `role_category=0.60`, `company_stage=0.60`, `day_to_day=0.40`, `autonomy_level=0.50`
    - Attack 2: `role_category=0.40`, `company_stage=0.00`, `day_to_day=0.40`, `autonomy_level=0.40`
    - Attack 3: `role_category=0.55`, `company_stage=0.55`, `day_to_day=0.45`, `autonomy_level=0.55`
    - Attack 4: `role_category=0.55`, `company_stage=0.00`, `day_to_day=0.48`, `autonomy_level=0.00`
- **Verdict:** the prompt contract now matches the Python gate. No `job` attack crossed `> 0.8` on a done-driving field after the audit patch.
- **Residual risk:** serializer-warning noise is still present in trace output.

## 9. 2026-04-11 Live Trace Goals-Handoff Replay
**Production target:** when Goals hands off a concrete autonomy/client path, Job must dig out the correct market and work-reality information instead of asking Goals-style questions again.

**Prompt-only contract change:**
- Job reads Goals as directional context.
- Job converts the long-goal assumptions into target customer, role/service category, company stage, recurring grind, pricing/discovery obligation, and autonomy constraints.
- Concrete job/client evidence can cross `> 0.8` even if the market path is not fully proven.

**Dataset:** `eval/live_trace_job_rounds.jsonl`
- Round 1: target customer type.
- Round 2: repetitive painful problem and time-saved value proxy.
- Round 3: SOP/time audit, agent requirements, buyer psychology, clarify-before-price constraint.

**Command:**
- `venv\Scripts\python eval\run_eval.py --mode multi --file eval\live_trace_job_rounds.jsonl --graph job_eval --workers 1`

**Final verified traces:**
- Round 1: `eval/threads/967c260d-5e52-4d3a-8f25-a975036f5d32/traces/run_0001.json`
- Round 2: `eval/threads/e3dc98db-3c22-423c-8c4e-9e51276d5776/traces/run_0002.json`
- Round 3: `eval/threads/bd9a3312-dee1-44d6-ba5a-10ce27c27412/traces/run_0003.json`

**Round 3 result:** **PASS at the stage-wrapper seam.**
- `job.done=true`
- `role_category = "AI workflow automation for B2B clients"`, `0.82`
- `company_stage = "startups lacking technical capacity or customer-ops-heavy companies"`, `0.83`
- `day_to_day = "qualify repetitive, boring client problems; estimate hours saved; map SOPs..."`, `0.85`
- `autonomy_level = "self-directed client work with client scope/pricing constraints"`, `0.82`

**Residual risk:** early rounds correctly stay provisional. Full orchestrator replay is still needed because `job_eval` skips routing and counter behavior.

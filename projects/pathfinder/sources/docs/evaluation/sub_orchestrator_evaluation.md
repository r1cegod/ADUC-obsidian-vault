# Sub-Orchestrator Evaluation & Audit Log

Updated: 2026-04-10

> **TL;DR**: Round 3 is now complete for both sub-orchestrator families on the dedicated focus-eval lane. After the final cleanup pass, `summarizer` and `worker` are production-ready at this seam, with the scope kept explicit: this is sub-orchestrator-lane proof only, not a replacement for broader full-system evaluation.


## 1. Architecture & Understanding
- **Scope:** this audit only covers the sub-orchestrator lane:
  - prompt family in `backend/data/prompts/sub_orchestrator.py`
  - graph family in `backend/sub_orchestrator_graph.py`
  - dedicated runner `eval/run_sub_orchestrator_focus_eval.py`
- **Summarizer family:** reads retired `routing_memory` after the hard budget trim and refreshes `user_tag_summaries`.
- **Worker family:** reads current `routing_memory` plus `user_tag_summaries` and refreshes persistent `user_tag` fields.
- **Seam under test:** this lane must be evaluable without `input_parser`, `stage_manager`, `counter_manager`, or `output_compiler`. The audit intentionally avoids the main orchestrator.

## 2. Vulnerabilities Identified
1. **V1 - Template drift:** the original prompt file used thin shared templates and field-focus strings, which was too weak for stable compression and conservative refresh work.
2. **V2 - No focused eval seam:** there was no runner or audit method for the sub-orchestrator alone, so prompt changes had to be inferred indirectly through bigger graphs.
3. **V3 - JSON-within-string failure:** early Round 1 traces showed some workers writing `{"value": ...}` into the string field itself because the prompt contract and function-calling schema were misaligned.
4. **V4 - Full-refresh drift:** the every-5-turn worker pass can still push weak fields to say more than they should, especially on `compliance`, `avoidance`, or `vague` when the primary signal is elsewhere.
5. **V5 - Language-mixing noise:** internal reasoning occasionally drifts across languages/scripts or picks slightly unstable wording on low-signal fields.

## 3. Round 1 Production Target & Attack Plan

### 3A. Summarizer Family
- **Round:** 1 of 3 max
- **Target family:** `summarizer`
- **This round must prove:** over-budget `routing_memory` can be compressed into usable `user_tag_summaries` without touching the main orchestrator.
- **User-facing behavior shift to surface:** compression should preserve the right long-memory signal instead of dropping it when the lane trims.

| # | Name | Attack Vector | Targeted Failure State |
|---|------|---------------|------------------------|
| 1 | Family Pressure Memory Compression | Long retired slice with repeated family pressure and weak authorship | Compression drops the parents-vs-design conflict or keeps only generic family text |
| 2 | Burnout + Urgency Memory Compression | Long retired slice with sleep loss, exam pressure, and rushed major choice | Compression flattens exhaustion into generic stress or confuses urgency with pressure only |
| 3 | Avoidance + Vagueness Memory Compression | Long retired slice with abstract dream talk and repeated dodging of money/ability questions | Compression loses the exact avoided truth and only says “student is vague” |

### 3B. Worker Family
- **Round:** 1 of 3 max
- **Target family:** `worker`
- **This round must prove:** current `routing_memory` plus carried summaries can refresh persistent user-tag fields conservatively and coherently without replaying the main orchestrator.
- **User-facing behavior shift to surface:** the lane should become more grounded and less generic, while still refusing to overstate weak fields.

| # | Name | Attack Vector | Targeted Failure State |
|---|------|---------------|------------------------|
| 1 | Worker Pressure + Compliance | Current turns still show safety phrasing under parental pressure | Worker clears pressure too early or misses scripted self-silencing |
| 2 | Worker Burnout + Urgency | Current turns show sleep-loss overload and deadline compression | Worker misses active burnout/urgency or invents unrelated pressure |
| 3 | Worker Reality Gap + Avoidance | Current turns keep big vision but dodge concrete feasibility | Worker misses the mismatch or collapses everything into one vague label |

## 4. Execution Results
- **Run date:** 2026-04-10
- **Draft changes applied:**
  - replaced the shared focus-line templates with bespoke per-field prompt bodies
  - added direct focus entrypoints for `summarizer` and `worker`
  - added `eval/run_sub_orchestrator_focus_eval.py`
  - added focus datasets for both families
  - added nested-JSON cleanup for text outputs after the first Round 1 pass exposed that contract bug
  - lowered the sub-orchestrator model temperature to stabilize low-signal fields

### 4A. Verification
- `python -m py_compile backend/data/prompts/sub_orchestrator.py backend/sub_orchestrator_graph.py backend/sub_orchestrator_focus_eval.py eval/run_sub_orchestrator_focus_eval.py test_sub_orchestrator_graph_contract.py test_sub_orchestrator_focus_eval_contract.py`
- `python -m unittest test_sub_orchestrator_graph_contract.py test_sub_orchestrator_focus_eval_contract.py`
- `venv\Scripts\python eval/run_sub_orchestrator_focus_eval.py --target summarizer --file eval/sub_orchestrator_summarizer_focus.jsonl --mode single`
- `venv\Scripts\python eval/run_sub_orchestrator_focus_eval.py --target worker --file eval/sub_orchestrator_worker_focus.jsonl --mode single`

### 4B. Final Round 1 Trace Set
- **Summarizer thread:** `2d0888e7-5757-4898-9002-e4c0cded8578`
- **Worker thread:** `01de9672-cd1e-46aa-beb8-e7b438b2c2b4`

### 4C. Summarizer Findings
- **Case 1 - Family Pressure Memory Compression:** **PASS with wording noise.**
  - Compression kept the mother/medicine push, fear of disappointing parents, and the design-vs-duty conflict.
  - Long-memory authorship stayed weak rather than falsely declaring full ownership.
  - Residual noise: adjacent low-signal summaries still said more than they needed to.

- **Case 2 - Burnout + Urgency Memory Compression:** **PASS with one reality-gap overreach.**
  - Compression kept sleep loss, headache, deadline pressure, and the “choose fast to survive the period” logic.
  - Urgency stayed concrete and tied to the exam/scholarship clock.
  - Residual risk: `reality_gap` was refreshed too aggressively for what is mainly an exhaustion case.

- **Case 3 - Avoidance + Vagueness Memory Compression:** **PASS with one compliance overreach.**
  - Compression preserved the actual avoided truth: money, capability, and first-year survival details.
  - Vagueness stayed about abstract dream language, not generic uncertainty.
  - Residual risk: `compliance` still over-called a performative pattern where the stronger signal is avoidance + vagueness.

### 4D. Worker Findings
- **Case 1 - Worker Pressure + Compliance:** **PASS.**
  - `parental_pressure=True` stayed active.
  - `core_tension=True` stayed live.
  - `compliance_reasoning` correctly named safe, parent-pleasing language.
  - Residual risk: some low-priority fields still refresh verbosely on the every-5-turn pass.

- **Case 2 - Worker Burnout + Urgency:** **PASS with mild cross-field drift.**
  - `burnout_risk=True` and `urgency=True` both refreshed correctly from current evidence.
  - `reality_gap` stayed conservative.
  - Residual risk: `compliance` and `avoidance` said more than ideal in a case dominated by exhaustion.

- **Case 3 - Worker Reality Gap + Avoidance:** **PASS.**
  - `reality_gap=True` refreshed on the claim-vs-proof mismatch.
  - `avoidance_reasoning` named the exact dodge around money, sacrifice, and current ability.
  - `compliance` stayed conservative here, which is the right call.

## 5. Round 1 Verdict
- `summarizer` Round 1 is complete.
- `worker` Round 1 is complete.
- Neither family is production ready yet.

### Why Not Production Ready
- The 3-round gate still applies separately to `summarizer` and `worker`.
- Trace audit still shows residual overreach on low-signal side fields during full refresh.
- Language consistency is better after the stability patch, but not fully locked.

## 6. Residual Risks For Round 2
- Tighten false-positive control on `compliance` and `reality_gap` when the dominant signal is elsewhere.
- Reduce every-5-turn overrefresh drift so weak fields do not speak just because the periodic pass fired.
- Enforce cleaner single-language internal reasoning on low-signal outputs.

## 7. Round 2 / Round 3 Gate
- **Summarizer Round 2 target:** keep the same compression quality while cutting false-positive side summaries.
- **Summarizer Round 3 target:** final confirmation pass with clean language consistency.
- **Worker Round 2 target:** reduce cross-field drift on low-signal fields during the periodic full refresh.
- **Worker Round 3 target:** final confirmation pass that proves conservative refresh behavior under mixed-signal cases.

Do not call either family production ready until all 3 reviewed rounds are complete.

## 8. Round 2 Production Target & Change Set

### 8A. Production Target
- **Round:** 2 of 3 max
- **Target families:** `summarizer`, `worker`
- **This round must prove:** the lane can keep the same core signal retention while reducing false-positive side-field output on low-signal fields.
- **User-facing behavior shift to surface:** the sub-orchestrator should speak less on weak side patterns unless there is an active or already-established signal.

### 8B. Draft Tightening Applied
- tightened prompt-side false-positive rules so:
  - `compliance` is not inferred from burnout, urgency, avoidance, or vagueness alone
  - `reality_gap` is not inferred from exhaustion or family pressure alone
  - `disengagement`, `avoidance`, and `vague` require their own evidence instead of piggybacking on the dominant signal
- enforced English-only schema guidance for direct outputs to cut language-mixing noise
- changed the periodic worker selector so every-5-turn refresh still hits:
  - all core bool fields
  - `self_authorship`
  - low-signal pattern fields only when they are active now or already established
- changed summarizer refresh ownership so low-signal side summaries are skipped unless that field is already live or directly triggered

## 9. Round 2 Execution Results
- **Run date:** 2026-04-10

### 9A. Verification
- `python -m py_compile backend/data/prompts/sub_orchestrator.py backend/sub_orchestrator_graph.py backend/sub_orchestrator_focus_eval.py eval/run_sub_orchestrator_focus_eval.py test_sub_orchestrator_graph_contract.py test_sub_orchestrator_focus_eval_contract.py`
- `python -m unittest test_sub_orchestrator_graph_contract.py test_sub_orchestrator_focus_eval_contract.py`
- `venv\Scripts\python eval/run_sub_orchestrator_focus_eval.py --target summarizer --file eval/sub_orchestrator_summarizer_focus.jsonl --mode single`
- `venv\Scripts\python eval/run_sub_orchestrator_focus_eval.py --target worker --file eval/sub_orchestrator_worker_focus.jsonl --mode single`

### 9B. Final Round 2 Trace Set
- **Summarizer thread:** `60fc2ac3-3693-40bd-a23b-fd73f6a911c6`
- **Worker thread:** `5b058ac0-3dea-4c4d-8d18-364d49311fdd`

### 9C. Summarizer Findings
- **Case 1 - Family Pressure Memory Compression:** **PASS.**
  - Compression now stays on the live family-pressure cluster: `parental_pressure`, `core_tension`, and `self_authorship`.
  - Side summaries no longer spill into `compliance`, `vague`, `urgency`, or `burnout_risk` just because the slice is emotionally strong.

- **Case 2 - Burnout + Urgency Memory Compression:** **PASS.**
  - Compression keeps `burnout_risk`, `urgency`, and a cautious `self_authorship` read.
  - The Round 1 `reality_gap` overreach is gone.

- **Case 3 - Avoidance + Vagueness Memory Compression:** **PASS.**
  - Compression now stays concentrated on `avoidance`, `vague`, and `self_authorship`.
  - The Round 1 `compliance` overcall is gone.

### 9D. Worker Findings
- **Case 1 - Worker Pressure + Compliance:** **PASS.**
  - `parental_pressure=True`, `core_tension=True`, and `compliance_reasoning` all remain correctly active.
  - Low-signal pattern fields that did not need to speak are now skipped.

- **Case 2 - Worker Burnout + Urgency:** **PASS.**
  - `burnout_risk=True` and `urgency=True` remain correct.
  - The Round 1/early Round 2 drift on `avoidance`, `disengagement`, and other side fields is gone.

- **Case 3 - Worker Reality Gap + Avoidance:** **PASS with minor language noise.**
  - `reality_gap=True` and `avoidance_reasoning` both survive correctly.
  - Pattern overreach is reduced.
  - Residual risk: one `self_authorship` output still showed minor mixed-script noise, which is small enough for Round 2 but not clean enough for a final signoff.

## 10. Round 2 Verdict
- `summarizer` Round 2 is complete.
- `worker` Round 2 is complete.
- Neither family is production ready yet.

### Why Not Production Ready After Round 2
- The 3-round gate still applies separately to `summarizer` and `worker`.
- Minor language/noise instability is still visible on at least one low-signal worker output.
- Round 3 is still needed as the final confirmation pass.

## 11. Round 3 Production Target & Change Set

### 11A. Production Target
- **Round:** 3 of 3 max
- **Target families:** `summarizer`, `worker`
- **This round must prove:** the Round 2 drift reduction holds on the same focused datasets and the remaining output-noise edge case is cleaned without reopening false-positive side-field behavior.
- **User-facing behavior shift to surface:** no new user-facing behavior shift; this is a final confirmation pass.

### 11B. Final Cleanup Applied
- added a small deterministic post-generation sanitizer for text outputs:
  - unwrap stringified payloads
  - strip zero-width noise
  - strip unexpected CJK mixed-script fragments
  - normalize whitespace
- kept the Round 2 selection and summary-ownership logic unchanged

## 12. Round 3 Execution Results
- **Run date:** 2026-04-10

### 12A. Verification
- `python -m py_compile backend/sub_orchestrator_graph.py test_sub_orchestrator_graph_contract.py backend/data/prompts/sub_orchestrator.py backend/sub_orchestrator_focus_eval.py eval/run_sub_orchestrator_focus_eval.py`
- `python -m unittest test_sub_orchestrator_graph_contract.py test_sub_orchestrator_focus_eval_contract.py`
- `venv\Scripts\python eval/run_sub_orchestrator_focus_eval.py --target summarizer --file eval/sub_orchestrator_summarizer_focus.jsonl --mode single`
- `venv\Scripts\python eval/run_sub_orchestrator_focus_eval.py --target worker --file eval/sub_orchestrator_worker_focus.jsonl --mode single`

### 12B. Final Round 3 Trace Set
- **Summarizer thread:** `c7325bac-e107-4e12-92d5-56cf901ac18f`
- **Worker thread:** `339e695d-3545-4f02-adca-e5520c2f32e9`

### 12C. Summarizer Findings
- **Case 1 - Family Pressure Memory Compression:** **PASS.**
  - The summary stays tightly on `parental_pressure`, `core_tension`, and `self_authorship`.
  - No side-field spill reopened.

- **Case 2 - Burnout + Urgency Memory Compression:** **PASS.**
  - `burnout_risk` and `urgency` remain crisp and concrete.
  - Round 1/2 side drift did not return.

- **Case 3 - Avoidance + Vagueness Memory Compression:** **PASS.**
  - `avoidance`, `vague`, and `self_authorship` remain the right cluster.
  - No false `compliance` or unrelated side summaries reappeared.

### 12D. Worker Findings
- **Case 1 - Worker Pressure + Compliance:** **PASS.**
  - `parental_pressure`, `core_tension`, and `compliance_reasoning` remain active and specific.
  - Side fields stay silent when they do not need to speak.

- **Case 2 - Worker Burnout + Urgency:** **PASS.**
  - `burnout_risk=True` and `urgency=True` remain correct.
  - No Round 1 style side-field overreach reopened.

- **Case 3 - Worker Reality Gap + Avoidance:** **PASS.**
  - `reality_gap=True` and `avoidance_reasoning` remain correct.
  - The prior mixed-script `self_authorship` edge case is gone in the final trace set.

## 13. Final Verdict
- `summarizer` Round 3 is complete.
- `worker` Round 3 is complete.
- `summarizer` is production ready at the dedicated sub-orchestrator focus-eval seam.
- `worker` is production ready at the dedicated sub-orchestrator focus-eval seam.

### Scope Boundary
- This is not full-system proof.
- The claim is limited to:
  - sub-orchestrator prompt behavior
  - sub-orchestrator memory compression
  - sub-orchestrator worker refresh logic
  - the dedicated focus-eval seam that bypasses the main orchestrator

### Residual Risk
- Residual risk is now low and mostly architectural, not behavioral:
  - this lane still does not prove `input_parser`, `stage_manager`, counter policy, or output-compiler behavior

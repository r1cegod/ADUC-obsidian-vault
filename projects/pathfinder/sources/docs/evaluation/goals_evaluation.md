# Goals Agent Evaluation & Audit Log

> **TL;DR**: Goals now looks stable at the stage-local handoff seam. The next stronger test is `goals_eval` replay through `output_compiler` to verify the final Vietnamese response preserves Silo's enforced `PROBE:` line.

Last updated: 2026-04-07

## 1. Architecture & Understanding
- **Extractor (Scale):** Extracts `long` horizon (`income_target`, `autonomy_level`, `ownership_model`, `team_size`) and `short` horizon (`skill_targets`, `portfolio_goal`, `credential_needed`). Enforces VERIFICATION CAP (`< 0.6` for unverified self-reports).
- **Analyst (Silo):** Executes "The Priors Cross-Check" (checking Purpose priors like `risk_philosophy` against `ownership_model`) and "The Horizon Squeeze" (validating 5-year ambition against 1-year execution plan).
- **Evaluation locale:** This stage serves Vietnamese students. The attack dataset uses Vietnamese student turns and tests the agent on Vietnamese counseling inputs, even though the stage agent itself writes internal English reasoning.

## 2. Vulnerabilities Identified
1. **V1 - The Numbers Hallucination:** Student says "I want to be a millionaire" or "rich". Scale might invent an `income_target` > 0.7 without actual metrics.
2. **V2 - The Abstract Skills Evasion:** Student says "I want to learn communication and leadership". Scale extracts "communication" as `skill_targets` > 0.7. Silo accepts without forcing technical or hard-skill verification.
3. **V3 - The Credentialed Founder (Horizon Gap):** Student wants to be a `founder` (Long) but their short-term plan is entirely soft (`credential_needed = degree`, `portfolio_goal = none`). Silo might fail to trigger the Horizon Squeeze to punish this gap.
4. **V4 - The Risk Crash (Prior Evasion):** Purpose prior says `risk_philosophy = gov stability`. Student now claims `ownership_model = freelance`. Silo notes it but fails to explicitly embed the tension in the `PROBE:` anchor.
5. **V5 - The Da Lat Lifestyle Fantasy:** Student paints a vivid autonomy fantasy ("Da Lat cafe, gym, chill, travel") that sounds concrete but contains no cost, benchmark, or build path. Scale may confuse detail with verification.
6. **V6 - The Parent-Pleasing Civil Servant:** Student gives a compliant public-sector answer explicitly to calm parents. Silo must treat it as social script, not a locked goal.
7. **V7 - The Debt Ladder Fantasy:** Student names a sharp salary number because of family debt, but the 1-year plan is only degree + IELTS. Scale must not treat numeric urgency as verified feasibility.
8. **V8 - The Founder-to-Solo Flip:** Student first claims founder/large-team ambition, then rejects managing anyone and pivots to solo freelancing. The extractor must not keep founder-level confidence high.
9. **V9 - The Safe-Path Drift:** Student defaults to "ổn định, lương khá, an toàn" because "mọi người bảo thế." The agent must keep this as empty-bucket compliance, not mistake it for a completed goal profile.

## 3. Attack Plan (Phase 1)

| # | Name | Attack Vector | Targeted Failure State |
|---|------|--------------|------------------------|
| 1 | The Abstract Millionaire | Student uses empty bucket words ("rich", "successful") with no numbers. | Scale invents or scores `income_target` > 0.5. Silo fails to demand numbers. |
| 2 | The Credentialed Founder | `ownership_model = founder` (Long) but `portfolio_goal = none` and `credential_needed = degree` (Short). | Silo accepts the academic safety-net instead of triggering the Horizon Squeeze. |
| 3 | The Prior-Crashing Freelancer | `purpose.risk_philosophy = gov stability` but current goal is `ownership_model = freelance`. | Silo forgets to embed the clash in the `PROBE:` anchor text. |

## 3B. Attack Plan (Phase 2 - Vietnamese Student Reality)

| # | Name | Attack Vector | Targeted Failure State |
|---|------|--------------|------------------------|
| 4 | The Da Lat Lifestyle Fantasy | Detailed autonomy fantasy with no number, no artifact, no cost. | Scale over-trusts vivid detail and inflates autonomy or income confidence. |
| 5 | The Parent-Pleasing Civil Servant | `message_tag = compliance`; student chooses public-sector stability to reassure parents. | Silo treats social script as an owned goal; Scale locks the path too aggressively. |
| 6 | The Debt Ladder Fantasy | Student names `40 triệu/tháng trong 2 năm` because the family has debt; short-term bridge is only degree + IELTS. | Scale treats the number as near-verified; Silo fails to force a market-proof bridge. |
| 7 | The Founder-to-Solo Flip | Student starts with founder/large-team ambition, then rejects management and wants solo freelancing. | Scale leaves founder confidence high or misses the contradiction. |
| 8 | The Safe-Path Drift | `message_tag = compliance`; student says "ổn định, lương khá, an toàn" because others say so. | Scale treats empty-bucket safety language as a concrete finished goal. |

## 4. Expectation Map

**Attack 1 - The Abstract Millionaire:**
- `Scale`: `income_target` must stay `< 0.5 (unclear)`.
- `Silo`: `PROBE:` must demand a concrete number and timeframe.

**Attack 2 - The Credentialed Founder:**
- `Scale`: `ownership_model = founder` capped at `0.6`. `portfolio_goal = none` must stay low.
- `Silo`: Must flag the HORIZON GAP (ambition vs execution). `PROBE:` must force a 1-year verifiable artifact.

**Attack 3 - The Prior-Crashing Freelancer:**
- `Scale`: `ownership_model = freelance` capped at `0.6`.
- `Silo`: `PROBE:` must directly embed the tension: government stability vs freelance instability.

**Attack 4 - The Da Lat Lifestyle Fantasy:**
- `Scale`: `income_target` must stay `< 0.5`; autonomy/freelance-style fields should remain well below lock because lifestyle detail is not proof.
- `Silo`: Must push a freedom-vs-income trade-off and demand a 1-year build artifact.

**Attack 5 - The Parent-Pleasing Civil Servant:**
- `Scale`: employee / credential-style fields may be partially extracted, but they must stay under the self-report cap.
- `Silo`: Must explicitly treat the answer as compliance/family script and probe whether the state-job path is truly owned.

**Attack 6 - The Debt Ladder Fantasy:**
- `Scale`: `income_target` may rise to the self-report cap because the student gave a number, but must not exceed `0.6`.
- `Silo`: Must call out that degree + IELTS does not bridge to `40 triệu/tháng` and target a portfolio or market-proof artifact.

**Attack 7 - The Founder-to-Solo Flip:**
- `Scale`: founder/large-team confidence must collapse; solo/freelance signals may replace them, but remain capped until defended.
- `Silo`: Must explicitly call out the founder-vs-solo contradiction and force a trade-off around autonomy, management, and income stability.

**Attack 8 - The Safe-Path Drift:**
- `Scale`: `income_target` stays `unclear < 0.5`; employee/stability signals stay capped and incomplete.
- `Silo`: Must keep the language framed as empty-bucket compliance and demand a concrete benchmark rather than accepting "an toàn" as a real goal.

---

## 5. Execution Results (Stage 2 - Phase 1)
**Run date:** 2026-04-05  
**Command:** `venv\Scripts\python eval/run_eval.py --mode multi --file eval/goals_attack.jsonl --graph goals`  
**Locale note:** evaluated with Vietnamese student messages from `eval/goals_attack.jsonl`, which is the correct production-facing language for this repo.

**Attack 1 - The Abstract Millionaire:** **PASS.**
- `Scale` held `income_target` at `0.35`, which keeps the millionaire fantasy under the verification cap.
- `Silo` treated the claim as empty-bucket wealth language and pushed the probe back onto a concrete benchmark and timeframe.

**Attack 2 - The Credentialed Founder:** **PASS.**
- `Scale` capped `ownership_model = founder` and `team_size = large` at `0.6`, dropped `skill_targets = communication / soft skills` to `0.3`, and kept `portfolio_goal = none` at `0.2`.
- `Silo` called out the academic-script gap directly and targeted `portfolio_goal` with a 1-year artifact squeeze.

**Attack 3 - The Prior-Crashing Freelancer:** **PASS.**
- `Scale` kept `ownership_model = freelance` and `autonomy_level = full autonomy` at `0.55`, with `team_size = solo` at `0.45`.
- `Silo` embedded the contradiction directly in the final anchor:
  `PROBE: ownership_model - Purpose says gov stability, but freelancing means unstable income; force a choice between financial safety and full autonomy.`

**Patch set that made the suite pass:**
- Added explicit `TITLE IS NOT DEFENSE`, `NUMBERS OR IT IS UNCLEAR`, `GENERIC SOFT-SKILL BAN`, and `HORIZON GAP PENALTY` rules to the Goals extractor.
- Added explicit `gov stability` vs `freelance/founder` crash logic plus `TENSION EMBEDDING` to the Goals analyst.
- Upgraded the graph contract in `backend/goals_graph.py`: the analyst now returns structured `goals_summary`, `probe_field`, and `probe_instruction`, and Python composes the final `PROBE:` line with a deterministic fallback if the model under-specifies it.

## 5B. Execution Results (Stage 2 - Phase 2)
**Expanded run:** `venv\Scripts\python eval/run_eval.py --mode multi --file eval/goals_attack.jsonl --graph goals`  
**Expanded suite size:** 8 attacks total

**Attack 4 - The Da Lat Lifestyle Fantasy:** **PASS.**
- `Scale` kept `income_target = 0.35`, `autonomy_level = 0.45`, and `ownership_model = 0.45`.
- `Silo` treated the lifestyle detail as unverified and pushed an income-vs-flexibility trade-off plus a 1-year proof path.

**Attack 5 - The Parent-Pleasing Civil Servant:** **PASS.**
- `Scale` kept `ownership_model = employee` at `0.6`, `autonomy_level = 0.58`, and `credential_needed = 0.56`, rather than locking the state-job path.
- `Silo` recognized the answer as compliance/family script and targeted whether the public-sector route is truly owned.

**Attack 6 - The Debt Ladder Fantasy:** **PASS.**
- `Scale` held `income_target = 0.6` even with the concrete `40 triệu/tháng` number, and kept the short-term bridge weak (`skill_targets = 0.4`, `credential_needed = 0.55`, `portfolio_goal = 0.0`).
- `Silo` explicitly stated that degree + IELTS does not justify the salary target and pushed the probe onto a market-proof artifact.

**Attack 7 - The Founder-to-Solo Flip:** **PASS.**
- `Scale` dropped the path to `ownership_model = freelance/solo` at `0.45` and `team_size = solo` at `0.55`, with no lingering founder lock.
- `Silo` treated the pivot as a structural crash and reframed the path around solo autonomy versus freelance instability.

**Attack 8 - The Safe-Path Drift:** **PASS.**
- `Scale` kept `income_target = unclear (0.2)`, `ownership_model = employee (0.45)`, and `portfolio_goal = none (0.1)`.
- `Silo` preserved the empty-bucket compliance framing and forced a concrete stability benchmark instead of accepting the social script.

## 5C. Contract Stability Check
**Targeted replay:** the previously failing last attack ("The Safe-Path Drift") was re-run in isolation after the graph-level patch.

**Command:**
- `venv\Scripts\python eval/run_eval.py --mode multi --file eval/goals_attack_last.jsonl --graph goals`

**Result:**
- The isolated replay now writes a valid trailing `PROBE:` line into `stage_reasoning.goals`.
- A 3-run stability replay of the same last attack produced `PROBE:` successfully in all 3 traces.

**Why this matters:**
- Before the graph patch, the analyst could return a reasoning blob that omitted the final `PROBE:` anchor even when the prompt asked for it.
- After the patch, the probe is enforced at the structured-output and Python-composition layer, so the Stage 2 handoff is no longer relying purely on prompt obedience.

---

## 6. Stage 4: Output Compiler Output
Goals now enters Stage 4 of the knowledge-agent evaluation.

This stage exists to ensure Silo's stronger internal handoff still produces a production-grade student-facing response after `context_compiler` and `output_compiler` run.

### 6A. Production Target And Round Plan
- **Round:** 1 of 3 max for the Goals Stage 4 visible-response seam.
- **Target stage:** `goals_eval` (`goals_graph -> context_compiler -> output_compiler`).
- **What this round must prove before stopping:** the existing `eval/goals_attack.jsonl` suite replays cleanly through the wrapper graph, `compiler_prompt` still contains the Goals reasoning and trailing `PROBE:`, and the final Vietnamese reply preserves horizon mismatch, compliance detection, and prior-crash tension instead of flattening them into generic coaching.
- **Production regression to prevent:** a sharp Goals-stage contradiction reaches `stage_reasoning.goals` but gets softened or erased by prompt assembly or the final output phrasing, leaving the student with a vague encouragement answer instead of a forced-choice squeeze.
- **Behavior that should become stricter or more explicit:** the final reply should keep the same hard trade-off already present in Silo's handoff, especially when the student is hiding behind parent compliance, lifestyle fantasy, or an unsupported salary ladder.
- **Behavior that should stay unchanged:** Stage 2 extractor confidence caps and the deterministic trailing `PROBE:` contract remain the source of truth; Stage 4 should only verify preservation at the visible-response seam, not reopen the stage-local contract.
- **User-facing behavior change to surface after the run:** if the compiler now preserves sharper contradiction language, the user should explicitly confirm whether that stronger tone is the intended production direction for Goals.

Stage 4 audit surface:
- replay `goals_eval` on the existing Vietnamese student attack set
- inspect whether `compiler_prompt` still contains the Goals reasoning and trailing `PROBE:`
- inspect whether the final Vietnamese reply preserves the contradiction instead of softening it into generic advice
- localize any failure to either Goals stage reasoning, compiler prompt assembly, or final output phrasing

### 6B. Stage 4 Execution Results
**Run date:** 2026-04-07  
**Verified command:** `venv\Scripts\python eval/run_eval.py --mode multi --file eval/goals_attack.jsonl --graph goals_eval`

**Replay status:** PASS after compiler-side patching.
- All 8 attacks completed successfully through `goals_graph -> context_compiler -> output_compiler`.
- In all 8 traces, `compiler_prompt` still contained the Goals-stage reasoning and trailing `PROBE:`.
- In the final verified replay, the student-facing Vietnamese reply no longer leaked stray foreign-script tokens and no longer opened with generic "rất cụ thể" praise on compliance or vague answers.

**Stage 4 patch set applied during the run:**
- Tightened `backend/data/prompts/output.py` so stage-drilling replies must match the evidence quality instead of using a generic concrete-answer acknowledgment.
- Added an exact `PROBE:` directive block in the compiler prompt so the final question must operationalize the analyst's real trade-off instead of swapping to a safer adjacent field.
- Made `backend/output_graph.py` deterministic (`temperature=0.0`) and added a language sanitizer so non-Latin script leakage cannot survive into the final student-facing reply.

**Audit summary:**
- **Attack 1 / Abstract Millionaire:** the final reply now keeps the number + timeframe squeeze instead of rewarding empty-bucket wealth language.
- **Attack 5 / Parent-Pleasing Civil Servant:** the final reply keeps the family-script framing visible and forces a concrete stability-vs-income choice.
- **Attack 7 / Founder-to-Solo Flip:** the final reply now preserves the founder-vs-solo trade-off instead of collapsing into a generic follow-up.
- **Attack 8 / Safe-Path Drift:** the final reply keeps the "everyone says so" compliance pattern in view and forces a sharper safety-vs-pay trade-off.

## 7. Attack Point Checklist
- [x] Did Scale strictly enforce the `0.6` cap on unverified self-reports?
- [x] Did Scale block empty bucket words ("rich", "soft skills") with `< 0.5`?
- [x] Did Silo successfully execute the Horizon Squeeze (ambition vs 1-year plan)?
- [x] Did Silo explicitly embed the Purpose prior clash into the `PROBE:` anchor string?
- [x] Was the output compiler handed a perfectly clean 1-sentence `PROBE:`?
- [x] Did Scale resist vivid Vietnamese lifestyle fantasy without over-scoring autonomy or income?
- [x] Did Silo treat parent-pleasing and safe-path answers as compliance rather than owned goals?
- [x] Did the salary-pressure case stay capped until a real bridge was named?
- [x] Did the founder-to-solo contradiction clear out the original founder path instead of leaving a stale lock?
- [x] Did `compiler_prompt` preserve the Goals reasoning and trailing `PROBE:` in all Stage 4 traces?
- [x] Did the final Vietnamese reply preserve contradiction/compliance pressure instead of generic praise?
- [x] Did the final Vietnamese reply stay Vietnamese-only with no foreign-script leakage?

## 8. Open Gap
Goals now passes the current Stage 2 stage-local seam and the current Stage 4 stage + compiler seam on `eval/goals_attack.jsonl`.

It is still not a full production-ready signoff:
- the 3-round evaluation gate still applies for Goals
- full orchestrator replay remains a later seam for routing and classification behavior
- broader dataset growth is still useful even though the current Stage 4 seam is now clean

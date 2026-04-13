# University-Finding Frontend Evaluation - 2026-04-13

## Scope

Live frontend session using a seeded student profile:

- Student goal: find a Vietnam university route for Product BA / UX research / business-system-data work.
- Student stance: grounded, knows their thinking and purpose, but attacks with uncertainty.
- Starting state: Thinking, Purpose, Goals already complete; started at Job and moved through Major into University.
- Auditor: worker subagent prepared a data-agent audit for R1/R2 in repo and vault.

## Trace Sessions

| Run | Trace Folder | Coverage | Result |
|---|---|---:|---|
| R1 | `eval/threads/university-finding-business-ux-20260413/traces/` | `live_0001`-`live_0012` | Job completed; Major soft-locked before University. |
| R2 | `eval/threads/university-finding-business-ux-20260413-r2/traces/` | `live_0001`-`live_0003` | Major prose improved, but raw `major.field` stayed stale and `major.done=false`. |
| R3 | `eval/threads/university-finding-business-ux-20260413-r3/traces/` | `live_0001` | Major analyst said handoff-sufficient, but `required_skills_coverage=0.78` kept stage locked. |
| R4 | `eval/threads/university-finding-business-ux-20260413-r4/traces/` | `live_0001` | Required-skill floor worked; `curriculum_style=0.79` became the next threshold blocker. |
| R5 | `eval/threads/university-finding-business-ux-20260413-r5/traces/` | `live_0001`-`live_0003` | Major completed and same-turn advanced to University; University then repeated evidence-choice probes. |
| R6 | `eval/threads/university-finding-business-ux-20260413-r6/traces/` | `live_0001`-`live_0002` | University source allowlist/query patch recovered UEH evidence, but still asked another threshold question. |
| R7 | `eval/threads/university-finding-business-ux-20260413-r7/traces/` | `live_0001` | University moved to FPT comparison query, but still asked a meta-threshold question instead of ranking. |

## Fixes Applied

1. Major research discipline
   - Added official Vietnamese university/program domains to Major research sources.
   - Added query rules to avoid overpacked curriculum artifact queries.
   - Added no-result recovery rules so Major should broaden or synthesize instead of repeating failed query shapes.

2. Major stage boundary
   - Major now treats named-school proof as University-owned once the student has selected a major direction, curriculum style, and job bridge.
   - Added Product BA/UX MIS extraction rules so stale Business Administration does not survive after the student chooses MIS.

3. Major deterministic handoff floor
   - Added a narrow scoring-node guard in `backend/major_graph.py`.
   - If a student has chosen MIS for Product BA/UX, named the curriculum/skill bridge, and is asking for school verification, near-done curriculum/skill confidences are raised just above the Python completion threshold.
   - Verified live in R5: `currentStage=uni`, `completedStages` includes `major`, and `major.done=true`.

4. University research source coverage
   - Added `ueh.edu.vn`, `uel.edu.vn`, `fpt.edu.vn`, `rmit.edu.vn`, and `usth.edu.vn` to `UNIVERSITY_OFFICIAL_DOMAINS`.
   - This fixed the source mismatch where University was asked to check UEH/FPT/RMIT/UEL but the allowlist excluded those schools.

5. University prompt discipline
   - Added rules to avoid `site:` plus many quoted artifact terms.
   - Added rules to avoid asking the student which website/page type to inspect.
   - Added rules to avoid re-asking "artifact, internship/network, or ROI?" when the student already gave that order.

## Remaining Bugs

1. University still has a meta-question loop.
   - R7 moved to an FPT query, which is better than asking for page type again.
   - It still asked how many evidence layers should count as "stronger than UEH" instead of making a provisional comparison.
   - Recommendation: harden `UNI_SYNTHESIS_PROMPT` further or add a small comparison-state contract so it can rank named schools after evidence appears.

2. University search quality is still noisy.
   - R7 FPT query found `daihoc.fpt.edu.vn`, but also surfaced software/APTECH results instead of clean MIS/Digital Business curriculum evidence.
   - Recommendation: add named-school/program query templates or school-specific domain buckets for UEH/FPT/RMIT/UEL.

3. Data-agent audit coverage is split.
   - Worker audit covers R1/R2.
   - R3-R7 findings are recorded in this frontend report, not the worker audit.

## Verification

```powershell
venv\Scripts\python -m unittest backend.test.test_major_prompt_contract backend.test.test_major_graph_contract backend.test.test_uni_graph_contract
venv\Scripts\python -m py_compile backend\major_graph.py backend\data\prompts\major.py backend\data\prompts\uni.py backend\data\contracts\research_sources.py
```

All listed checks passed.

## Workflow Notes

- Use `agent-browser batch --bail` for sequential UI actions like click/fill/Enter.
- Use `eval/live_session_probe.py state` after each turn for compact stage state; use `--full` only when investigating a failure.
- Stop and fork a new trace run after each patch/restart. Do not mix pre-patch and post-patch evidence in one trace folder.
- Use a data-auditor worker for raw trace tables, then keep the main report focused on runtime decisions, fixes, and remaining blockers.

## Retrospective Optimization

This run should have stopped at R5 under the new official rule: the target boundary was Major handoff into University, and R5 proved it. R6-R7 found useful University debt, but that debt belongs in a new University comparison/ranking evaluation cycle rather than the same live frontend operation.

Future runs should declare one target boundary before starting and stop when that boundary is fixed. Continuing into the next stage is only allowed when the user explicitly expands the mission.

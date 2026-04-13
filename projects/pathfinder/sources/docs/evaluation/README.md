# PathFinder Evaluation Domain

Last updated: 2026-04-13

This directory is the canonical home for PathFinder evaluation documentation.

## Source Of Truth Rule

- Evaluation docs, reports, audit logs, stage findings, run retrospectives, and workflow guides live in this vault directory.
- The repo `eval/` directory is an executable and evidence workspace only: runners, JSONL datasets, raw traces, manifests, scratch messages, and temporary local artifacts needed to run evaluation.
- Python contract/regression tests are not part of repo `eval/`; they live under `D:\ANHDUC\Path_finder\backend\test\` and should be invoked as `backend.test.<module>` with `python -m unittest`.
- Do not mirror evaluation reports into the repo.
- The only project documentation intentionally mirrored between vault and repo is the dev log.
- If an old repo-side evaluation report already exists, treat it as legacy evidence or convert it to a pointer during a cleanup pass. Do not create a new repo mirror for a vault evaluation report.

## Canonical Workflow Docs

| Need | Canonical doc |
|---|---|
| Replay evaluation pipeline | `eval_how_to_use.md` |
| Frontend and live user-like sessions | `frontend_evaluation_how_to_use.md` |
| Deterministic backend seam checks | `python_function_check_how_to_use.md` |
| Sub-orchestrator prompt and memory lane | `sub_orchestrator_focus_eval_how_to_use.md` |

## Stage And Agent Logs

| Area | Canonical doc |
|---|---|
| Thinking | `thinking_evaluation.md` |
| Purpose | `purpose_evaluation.md` |
| Goals | `goals_evaluation.md` |
| Job | `job_evaluation.md` |
| Major | `major_evaluation.md` |
| University | `uni_evaluation.md` |
| Data agent | `data_agent_evaluation.md` |
| Knowledge agent | `knowledge_agent_evaluation.md` |
| Research sources | `research_sources.md` |
| Sub-orchestrator | `sub_orchestrator_evaluation.md` |

## Live Reports

| Run | Canonical report |
|---|---|
| Consolidated frontend evaluation ledger | `frontend_evaluation_report.md` |
| Live trace to Goals audit, 2026-04-11 | `live_trace_to_goals_audit_2026-04-11.md` |
| Sub-orchestrator flow and Round 3 report | `sub_orchestrator_flow_and_round3_report.md` |
| Uncertainty attack, 2026-04-12 | `uncertainty_attack_report_2026-04-12.md` |
| Identity continuation Goals report, 2026-04-12 | `identity_continuation_goals_report_2026-04-12.md` |
| University-finding frontend session, 2026-04-13 | `university_finding_frontend_report_2026-04-13.md` |
| Data-agent frontend audit, 2026-04-13 | `data_agent_frontend_audit_2026-04-13.md` |

## Closure Protocol

When closing any evaluation run:

1. Write the report or audit log in this vault evaluation directory.
2. Keep raw executable evidence in repo `eval/` only when it is needed to reproduce the run.
3. Update the current vault dev-log day file.
4. Mirror only that dev-log day-file update into repo `logs/dev/days/`.
5. Rebuild the dev-log indexes when day files changed.
6. Update architecture, prompt, state, or context docs in the vault only when the evaluation changed a durable contract.

Evaluation is closed when the vault report is readable without opening full traces, and repo evidence can reproduce the claim if needed.

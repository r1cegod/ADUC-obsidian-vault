# PathFinder Project Context

## Purpose
PathFinder is a multi-agent AI counselor for Vietnamese students.
It drills past surface-level answers and maps verified preferences to jobs, majors, and universities.

## Stack Snapshot
- Backend: Python, LangGraph, Pydantic
- Frontend: React, Vite, Tailwind CSS
- Conversation language: Vietnamese
- Code and docs language: English

## System Shape
- Flow: Input Orchestrator -> Active Stage Agent -> Output Compiler
- Stage order: thinking -> purpose -> goals -> job -> major -> university
- Path is not a stage agent. It is handled in Output Compiler Case B2 after all 6 profiles are done.
- Stage agents follow the scoring -> analyst pattern.
- Output compiler is the only student-facing response generator.
- LLMs classify and synthesize. Python owns routing, counters, and thresholds.

## Source Of Truth
- Architecture: `projects/pathfinder/sources/docs/architecture/docs/ARCHITECTURE.md`
- State contract: `projects/pathfinder/sources/docs/architecture/docs/state_architecture.md`
- Stage prompt docs: `projects/pathfinder/sources/docs/prompt/docs/stage_prompt.md`
- Output prompt docs: `projects/pathfinder/sources/docs/prompt/docs/output_prompt_architecture.md`
- Prompt how-to: `projects/pathfinder/sources/docs/prompt/how to/production_system_prompts.md`
- Evaluation pipeline: `eval/HOW_TO_USE.md`
- Context maintenance: `projects/pathfinder/sources/docs/context/how to/context_maintenance.md`
- Evaluation log: `projects/pathfinder/sources/docs/evaluation/stage_evaluation.md`
- Decision log: `projects/pathfinder/sources/docs/DEV_LOG.md`

## Archive Boundary
- Canonical live docs now live in this vault under `projects/pathfinder/sources/docs/`.
- The repo copy at `D:\ANHDUC\Path_finder\docs (archived)\` is archived reference material only.
- Exception: `D:\ANHDUC\Path_finder\docs (archived)\DEV_LOG.md` is a required mirror of the canonical vault dev log and must be updated together with `projects/pathfinder/sources/docs/DEV_LOG.md`.
- Use `projects/pathfinder/README.md` and the domain hubs in `projects/pathfinder/notes/` as the routing layer before opening raw docs.

## Code Entry Points
- `backend/orchestrator_graph.py`
- `backend/output_graph.py`
- `backend/data/state.py`
- `backend/data/contracts/`
- `backend/data/prompts/`
- `backend/*_graph.py`
- `frontend/`
- `main.py`

## Stable Conventions
- Pydantic state and profile models live in `backend/data/state.py`.
- Shared stage-name/key mappings live in `backend/data/contracts/stages.py`.
- Only the root orchestrator owns a checkpointer. Stage and output subgraphs compile without separate persistence.
- Prompt templates live in `backend/data/prompts/{stage}.py`.
- Extractable fields use `FieldEntry`-style `{content, confidence}` wrapping.
- Student-facing responses are Vietnamese.
- `load_dotenv()` must run before any `ChatOpenAI` initialization.
- New state fields need a writer, a reader, and an exit condition.
- Start session context from `PROJECT_CONTEXT.md`, then `CURRENT_CONTEXT.md`, and keep both aligned with `context_maintenance.md`.
- Do not treat the repo `docs (archived)/` folder as live documentation anymore.
- `DEV_LOG.md` is the one mirrored exception: append the same durable entry to both the canonical vault copy and the archived repo copy.

## Quick Checks
- API smoke test: `python test.py`
- Graph import: `python -c "from backend.orchestrator_graph import input_orchestrator; print('OK')"`
- Local graph runner: `langgraph dev`

## Notes
- Last reviewed: 2026-04-02
- Use `CURRENT_CONTEXT.md` for live work, blockers, and handoff notes.
- Keep this file stable. If a fact is volatile, it does not belong here.

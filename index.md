# Index

> Content routing table. Last updated: 2026-04-09 | Pages: 129 | Sources: 56
> Format: `- [[path|Display Name]] - one-liner (tags)`

---

## Entities
<!-- People, tools, organizations, products -->

## Learning
<!-- Personal learning system: protocol, sessions, curriculum -->
- [[learning/README|Learning Sessions]] - index of all Pre-Wire learning sessions, one per feature (learning, protocol)
- [[wiki/pre-wire-protocol|Pre-Wire Learning Protocol]] - blueprint-first learning protocol: user drafts → agent audits → artifact challenges → user builds (learning, protocol, meta)

## Concepts
<!-- Ideas, frameworks, methods, definitions -->
- [[wiki/concepts/agent-memory-compilation|Agent Memory Compilation]] - pipeline for turning raw conversations or notes into durable knowledge pages (obsidian, memory)
- [[wiki/concepts/daily-note-graduation|Daily Note Graduation]] - promote durable signals out of raw daily notes into reusable pages (obsidian, memory)
- [[wiki/concepts/human-agent-write-boundary|Human-Agent Write Boundary]] - keeps human-authored raw notes separate from agent-maintained synthesis (obsidian, memory)
- [[wiki/concepts/llm-wiki|LLM Wiki]] - persistent markdown knowledge base maintained by an agent between raw sources and future queries (obsidian, memory)

## Synthesis
<!-- Cross-cutting analysis, comparisons, overviews -->
- [[wiki/synthesis/obsidian-agent-vault-change-report|Obsidian Agent Vault Change Report]] - inventory of the contract, template, and ingest changes made in the current Obsidian vault pass (obsidian, memory, report)
- [[wiki/synthesis/obsidian-agent-vault-architecture|Obsidian Agent Vault Architecture]] - human-readable digest of the current Obsidian plus agent-memory source cluster (obsidian, memory)
- [[wiki/synthesis/discord-ai-agent-connection-patterns|Discord AI Agent Connection Patterns]] - architecture-level guide for wiring an existing Discord app into an AI moderation backend (discord, ai, moderation)
- [[wiki/synthesis/discord-moderation-domain|Discord Moderation Domain]] - initial knowledge router for permission design, staff controls, and moderation gaps (discord, moderation)
- [[wiki/synthesis/discord-moderation-source-map|Discord Moderation Source Map]] - next-ingest source map across docs, GitHub, Reddit, and YouTube for the missing moderation areas (discord, moderation)
- [[projects/pathfinder/notes/pathfinder-docs-ingest|PathFinder Docs Ingest]] - structured summary of the mirrored PathFinder docs corpus (pathfinder, synthesis)
- [[projects/pathfinder/notes/pathfinder-architecture-hub|PathFinder Architecture Hub]] - domain hub for graph shape, state, and architecture contracts (pathfinder, synthesis)
- [[projects/pathfinder/notes/pathfinder-context-hub|PathFinder Context Hub]] - domain hub for stable context, live handoff, and maintenance rules (pathfinder, synthesis)
- [[projects/pathfinder/notes/pathfinder-prompt-hub|PathFinder Prompt Hub]] - domain hub for stage and output prompt work (pathfinder, synthesis)
- [[projects/pathfinder/notes/pathfinder-evaluation-hub|PathFinder Evaluation Hub]] - domain hub for replay workflow, stage audits, and retrieval evaluation (pathfinder, synthesis)
- [[projects/pathfinder/notes/pathfinder-workflow-hub|PathFinder Workflow Hub]] - domain hub for maintenance, handoff, and durable-memory workflow docs (pathfinder, synthesis)
- [[projects/pathfinder/notes/docs-repo-vault-sync-policy|Repo Vault Sync Policy]] - current write boundary between vault-canonical docs and the repo mirror layer (pathfinder, workflow, docs)

## Projects
<!-- Format: - [[path|Name]] - status | one-liner -->
- [[projects/pathfinder/README|PathFinder]] - active | vault workspace for repo docs, summaries, and project routing
- [[projects/ielts-writing/README|IELTS Writing]] - active | 20-day band 4-5 → 7-8 protocol with schema docs (ielts, writing, learning)
- [[projects/ielts-writing/sources/chart-generator|Task 1 Chart Generator]] - how to call gen_challenge(spec) to produce PNG charts for practice (ielts, tools)

## References
<!-- Format: - [[references/path|Title]] - one-liner (tags) -->
- [[references/andrej-karpathy-llm-wiki|LLM Wiki]] - original architecture gist for raw sources, compiled wiki pages, schema, index, and log (obsidian, memory)
- [[references/ben-ai-claude-cowork-obsidian|Claude Cowork + Obsidian Will Change How You Work Forever]] - business/personal OS framing for persistent AI context (obsidian, memory)
- [[references/cole-medin-claude-memory-karpathy|I Built Self-Evolving Claude Code Memory w/ Karpathy's LLM Knowledge Bases]] - video implementation of conversation capture, daily logs, and knowledge compilation (obsidian, memory)
- [[references/coleam00-claude-memory-compiler|claude-memory-compiler]] - GitHub implementation of hook-driven conversation memory compilation (obsidian, memory)
- [[references/discord-gateway|Gateway]] - official realtime event-ingestion reference for passive Discord AI moderation intake (discord, ai, moderation)
- [[references/discord-interactions-overview|Interactions Overview]] - official command/component entrypoint reference for explicit AI moderation workflows (discord, ai, moderation)
- [[references/discord-oauth2-and-permissions|OAuth2 and Permissions]] - official auth and execution-identity reference for Discord apps (discord, ai, moderation)
- [[references/discord-privileged-intents|What are Privileged Intents?]] - official feasibility check for passive AI moderation visibility (discord, ai, moderation)
- [[references/discord-receiving-and-responding-to-interactions|Receiving and Responding to Interactions]] - official timing and followup contract for AI-backed slash commands (discord, ai, moderation)
- [[references/discord-auto-moderation-in-discord|Auto Moderation in Discord]] - official Discord strategy article for layered automation, verification, and bot choice (discord, moderation)
- [[references/discord-automod-faq|AutoMod FAQ]] - official built-in filtering reference for keyword rules, spam controls, and alert behavior (discord, moderation)
- [[references/discord-command-permissions|Command Permissions]] - official guide for restricting app commands by role, member, and channel (discord, moderation)
- [[references/discord-creating-moderation-team-channels|Creating Moderation Team Channels]] - official staff-workspace design guide with privacy-aware logging boundaries (discord, moderation)
- [[references/discord-managing-moderation-teams|Managing Moderation Teams]] - official moderator-governance guide for team structure and specialization (discord, moderation)
- [[references/discord-moderating-apps|Moderating Apps on Discord]] - official app-risk and external-app control guide (discord, moderation)
- [[references/discord-raids-101|How to Protect Your Server from Raids 101]] - official incident-time anti-raid guide (discord, moderation)
- [[references/discord-rules-screening-faq|Rules Screening FAQ]] - official native rule-acceptance gate guide (discord, moderation)
- [[references/discord-safety-library|Safety Library]] - official Discord moderation and server-safety routing hub (discord, moderation)
- [[references/discord-verification-levels|Verification Levels]] - official join-gating ladder for anti-raid and spam resistance (discord, moderation)
- [[references/gehsture-discord-server-setup-2026|How to Setup a Discord Server 2026]] - external video reference for the seeded Discord moderation domain (discord, moderation)
- [[references/github-hifihedgehog-discord-content-filter-bot|hifihedgehog/DiscordContentFilterBot]] - advanced filtering and punishment implementation reference (discord, moderation)
- [[references/github-infinotiver-discord-rules-template|Rules template for your Discord Server]] - unofficial rule-drafting scaffold for onboarding and public policy text (discord, moderation)
- [[references/github-jcsumlin-discord-ban-appeal|jcsumlin/discord-ban-appeal]] - self-hosted authenticated appeals app with webhook workflow (discord, moderation)
- [[references/github-sahneedev-sahnee-bot|SahneeDEV/sahnee-bot]] - warning-history and moderator-reporting bot reference (discord, moderation)
- [[references/github-sylveon-discord-ban-appeals|sylveon/discord-ban-appeals]] - minimal authenticated ban-appeals implementation (discord, moderation)
- [[references/greg-isenberg-12-commands-that-turn-notes-into-ideas|12 Commands That Turn Notes Into Ideas]] - companion page for the command-layer approach over notes (obsidian, memory)
- [[references/greg-isenberg-vin-obsidian-claude-code|How I Use Obsidian + Claude Code to Run My Life]] - personal OS workflow for commands, reflection, and write boundaries (obsidian, memory)
- [[references/nate-herk-karpathy-claude-code-obsidian|Andrej Karpathy Just 10x'd Everyone's Claude Code]] - fast practical setup of the Karpathy vault pattern in Obsidian (obsidian, memory)
- [[references/openai-models-overview|Models]] - official OpenAI model-selection index for AI moderation backends (ai, discord, moderation)
- [[references/openai-omni-moderation-model|omni-moderation Model]] - official OpenAI moderation-model reference for harmful-content classification (ai, discord, moderation)
- [[references/openai-practical-guide-building-agents|A practical guide to building agents]] - official OpenAI guide for model, tool, and guardrail design (ai, discord, moderation)
- [[references/reddit-built-in-ban-appeal-system|Add a built in ban appeal system]] - low-confidence community signal about the lack of native server-level appeals (discord, moderation)
- [[references/reddit-pokerogue-ban-appeals|Discord and Reddit Ban Appeals]] - real-world example of one official appeal path and no DMing mods (discord, moderation)
- [[references/youtube-best-discord-moderator|How to become the BEST, Discord Moderator!]] - behavior-focused moderator tutorial on evidence and restraint (discord, moderation)
- [[references/youtube-sapphire-appeals-2026|How to Set Up Discord Appeals with Sapphire - Easy 2026 Guide]] - managed appeals workflow tutorial using Sapphire and appeal.gg (discord, moderation)
- [[references/youtube-wick-beemo-anti-raid|Stop Discord Server Raids and Nukes! (Wick + Beemo)]] - tactical anti-raid and anti-nuke setup walkthrough (discord, moderation)
- [[references/youtube-wickbot-raid-protection|How to Protect your Discord Server from Raids! | Using WickBot!]] - compact WickBot anti-raid implementation guide (discord, moderation)

## Sources (recent first)
<!-- Format: - YYYY-MM-DD: [[wiki/path|Title]] <- [[sources/path|raw]] (tags) -->
### Discord Moderation
- 2026-04-07: [[wiki/synthesis/discord-interactions-overview|Discord Interactions Overview]] <- [[references/discord-interactions-overview|raw]] (discord, ai, moderation)
- 2026-04-07: [[wiki/synthesis/discord-receiving-and-responding-to-interactions|Discord Receiving And Responding To Interactions]] <- [[references/discord-receiving-and-responding-to-interactions|raw]] (discord, ai, moderation)
- 2026-04-07: [[wiki/synthesis/discord-oauth2-and-permissions|Discord OAuth2 And Permissions]] <- [[references/discord-oauth2-and-permissions|raw]] (discord, ai, moderation)
- 2026-04-07: [[wiki/synthesis/discord-gateway|Discord Gateway]] <- [[references/discord-gateway|raw]] (discord, ai, moderation)
- 2026-04-07: [[wiki/synthesis/discord-privileged-intents|Discord Privileged Intents]] <- [[references/discord-privileged-intents|raw]] (discord, ai, moderation)
- 2026-04-07: [[wiki/synthesis/openai-practical-guide-building-agents|OpenAI Practical Guide To Building Agents]] <- [[references/openai-practical-guide-building-agents|raw]] (ai, discord, moderation)
- 2026-04-07: [[wiki/synthesis/openai-models-overview|OpenAI Models Overview]] <- [[references/openai-models-overview|raw]] (ai, discord, moderation)
- 2026-04-07: [[wiki/synthesis/openai-omni-moderation-model|OpenAI Omni Moderation Model]] <- [[references/openai-omni-moderation-model|raw]] (ai, discord, moderation)
- 2026-04-07: [[wiki/synthesis/discord-safety-library|Discord Safety Library]] <- [[references/discord-safety-library|raw]] (discord, moderation)
- 2026-04-07: [[wiki/synthesis/discord-verification-levels|Discord Verification Levels]] <- [[references/discord-verification-levels|raw]] (discord, moderation)
- 2026-04-07: [[wiki/synthesis/discord-automod-faq|Discord AutoMod FAQ]] <- [[references/discord-automod-faq|raw]] (discord, moderation)
- 2026-04-07: [[wiki/synthesis/discord-rules-screening-faq|Discord Rules Screening FAQ]] <- [[references/discord-rules-screening-faq|raw]] (discord, moderation)
- 2026-04-07: [[wiki/synthesis/discord-auto-moderation-in-discord|Discord Auto Moderation In Discord]] <- [[references/discord-auto-moderation-in-discord|raw]] (discord, moderation)
- 2026-04-07: [[wiki/synthesis/discord-raids-101|Discord Raids 101]] <- [[references/discord-raids-101|raw]] (discord, moderation)
- 2026-04-07: [[wiki/synthesis/discord-managing-moderation-teams|Discord Managing Moderation Teams]] <- [[references/discord-managing-moderation-teams|raw]] (discord, moderation)
- 2026-04-07: [[wiki/synthesis/discord-creating-moderation-team-channels|Discord Creating Moderation Team Channels]] <- [[references/discord-creating-moderation-team-channels|raw]] (discord, moderation)
- 2026-04-07: [[wiki/synthesis/discord-moderating-apps|Discord Moderating Apps]] <- [[references/discord-moderating-apps|raw]] (discord, moderation)
- 2026-04-07: [[wiki/synthesis/discord-command-permissions|Discord Command Permissions]] <- [[references/discord-command-permissions|raw]] (discord, moderation)
- 2026-04-07: [[wiki/synthesis/github-jcsumlin-discord-ban-appeal|jcsumlin Discord Ban Appeal]] <- [[references/github-jcsumlin-discord-ban-appeal|raw]] (discord, moderation)
- 2026-04-07: [[wiki/synthesis/github-sylveon-discord-ban-appeals|sylveon Discord Ban Appeals]] <- [[references/github-sylveon-discord-ban-appeals|raw]] (discord, moderation)
- 2026-04-07: [[wiki/synthesis/github-hifihedgehog-discord-content-filter-bot|hifihedgehog Discord Content Filter Bot]] <- [[references/github-hifihedgehog-discord-content-filter-bot|raw]] (discord, moderation)
- 2026-04-07: [[wiki/synthesis/github-sahneedev-sahnee-bot|SahneeDEV Sahnee Bot]] <- [[references/github-sahneedev-sahnee-bot|raw]] (discord, moderation)
- 2026-04-07: [[wiki/synthesis/github-infinotiver-discord-rules-template|Infinotiver Discord Rules Template]] <- [[references/github-infinotiver-discord-rules-template|raw]] (discord, moderation)
- 2026-04-07: [[wiki/synthesis/reddit-built-in-ban-appeal-system|Reddit Built In Ban Appeal System Request]] <- [[references/reddit-built-in-ban-appeal-system|raw]] (discord, moderation)
- 2026-04-07: [[wiki/synthesis/reddit-pokerogue-ban-appeals|Reddit PokeRogue Ban Appeals]] <- [[references/reddit-pokerogue-ban-appeals|raw]] (discord, moderation)
- 2026-04-07: [[wiki/synthesis/youtube-wick-beemo-anti-raid|YouTube Wick And Beemo Anti Raid]] <- [[references/youtube-wick-beemo-anti-raid|raw]] (discord, moderation)
- 2026-04-07: [[wiki/synthesis/youtube-wickbot-raid-protection|YouTube WickBot Raid Protection]] <- [[references/youtube-wickbot-raid-protection|raw]] (discord, moderation)
- 2026-04-07: [[wiki/synthesis/youtube-sapphire-appeals-2026|YouTube Sapphire Appeals 2026]] <- [[references/youtube-sapphire-appeals-2026|raw]] (discord, moderation)
- 2026-04-07: [[wiki/synthesis/youtube-best-discord-moderator|YouTube Best Discord Moderator]] <- [[references/youtube-best-discord-moderator|raw]] (discord, moderation)
- 2026-04-07: [[wiki/synthesis/gehsture-discord-server-setup-2026|Gehsture Discord Server Setup 2026]] <- [[references/gehsture-discord-server-setup-2026|raw]] (discord, moderation)

### Obsidian And Memory
- 2026-04-07: [[wiki/synthesis/greg-isenberg-vin-obsidian-claude-code|Greg Isenberg And Internet Vin On Obsidian And Claude Code]] <- [[sources/transcripts/greg-isenberg-vin-obsidian-claude-code.md|raw]] (obsidian, memory)
- 2026-04-07: [[wiki/synthesis/ben-ai-claude-cowork-obsidian|Ben AI Obsidian Business OS]] <- [[sources/transcripts/ben-ai-claude-cowork-obsidian.md|raw]] (obsidian, memory)
- 2026-04-07: [[wiki/synthesis/cole-medin-claude-memory-karpathy|Cole Medin Claude Memory Compiler]] <- [[sources/transcripts/cole-medin-claude-memory-karpathy.md|raw]] (obsidian, memory)
- 2026-04-07: [[wiki/synthesis/nate-herk-karpathy-claude-code-obsidian|Nate Herk Karpathy Obsidian Setup]] <- [[sources/transcripts/nate-herk-karpathy-claude-code-obsidian.md|raw]] (obsidian, memory)

### PathFinder
- 2026-04-06: [[projects/pathfinder/notes/docs-dev-log-system-prompt|Dev Log Generator - System Prompt]] <- [[projects/pathfinder/sources/docs/DEV_LOG_SYSTEM_PROMPT.md|raw]] (pathfinder, workflow)
- 2026-04-06: [[projects/pathfinder/notes/docs-architecture|PathFinder Architecture]] <- [[projects/pathfinder/sources/docs/architecture/docs/ARCHITECTURE.md|raw]] (pathfinder, architecture)
- 2026-04-06: [[projects/pathfinder/notes/docs-state-architecture|PathFinder State Architecture]] <- [[projects/pathfinder/sources/docs/architecture/docs/state_architecture.md|raw]] (pathfinder, state)
- 2026-04-06: [[projects/pathfinder/notes/docs-architecture-howto|How To Write Architecture Docs For Multi-Agent AI Systems]] <- [[projects/pathfinder/sources/docs/architecture/how to/architecture_doc_howto.md|raw]] (pathfinder, architecture)
- 2026-04-06: [[projects/pathfinder/notes/docs-current-context|Current Context]] <- [[projects/pathfinder/sources/docs/context/docs/CURRENT_CONTEXT.md|raw]] (pathfinder, context)
- 2026-04-06: [[projects/pathfinder/notes/docs-project-context|PathFinder Project Context]] <- [[projects/pathfinder/sources/docs/context/docs/PROJECT_CONTEXT.md|raw]] (pathfinder, context)
- 2026-04-06: [[projects/pathfinder/notes/docs-context-maintenance|Context Maintenance]] <- [[projects/pathfinder/sources/docs/context/how to/context_maintenance.md|raw]] (pathfinder, workflow)
- 2026-04-07: [[projects/pathfinder/notes/docs-eval-how-to-use|PathFinder Evaluation Pipeline]] <- [[projects/pathfinder/sources/docs/evaluation/eval_how_to_use.md|raw]] (pathfinder, evaluation)
- 2026-04-07: [[projects/pathfinder/notes/docs-knowledge-agent-evaluation|Knowledge Agent Evaluation Guide]] <- [[projects/pathfinder/sources/docs/evaluation/knowledge_agent_evaluation.md|raw]] (pathfinder, evaluation)
- 2026-04-06: [[projects/pathfinder/notes/docs-eval-run-eval|eval/run_eval.py - How To Use]] <- [[projects/pathfinder/sources/docs/delegated/eval_run_eval.md|raw]] (pathfinder, evaluation)
- 2026-04-07: [[projects/pathfinder/notes/docs-evaluation-graph|Evaluation Graph]] <- [[projects/pathfinder/sources/docs/delegated/evaluation_graph.md|raw]] (pathfinder, evaluation)
- 2026-04-06: [[projects/pathfinder/notes/docs-data-agent-evaluation|Data Agent Evaluation Guide]] <- [[projects/pathfinder/sources/docs/evaluation/data_agent_evaluation.md|raw]] (pathfinder, retrieval)
- 2026-04-06: [[projects/pathfinder/notes/docs-goals-evaluation|Goals Agent Evaluation And Audit Log]] <- [[projects/pathfinder/sources/docs/evaluation/goals_evaluation.md|raw]] (pathfinder, evaluation)
- 2026-04-06: [[projects/pathfinder/notes/docs-job-evaluation|Job Agent Evaluation And Audit Log]] <- [[projects/pathfinder/sources/docs/evaluation/job_evaluation.md|raw]] (pathfinder, evaluation)
- 2026-04-06: [[projects/pathfinder/notes/docs-purpose-evaluation|Purpose Agent Evaluation And Audit Log]] <- [[projects/pathfinder/sources/docs/evaluation/purpose_evaluation.md|raw]] (pathfinder, evaluation)
- 2026-04-06: [[projects/pathfinder/notes/docs-research-sources|Retrieval Research Sources]] <- [[projects/pathfinder/sources/docs/evaluation/research_sources.md|raw]] (pathfinder, retrieval)
- 2026-04-06: [[projects/pathfinder/notes/docs-thinking-evaluation|Thinking Agent Evaluation And Audit Log]] <- [[projects/pathfinder/sources/docs/evaluation/thinking_evaluation.md|raw]] (pathfinder, evaluation)
- 2026-04-06: [[projects/pathfinder/notes/docs-output-prompt-architecture|Output Compiler Prompt Architecture]] <- [[projects/pathfinder/sources/docs/prompt/docs/output_prompt_architecture.md|raw]] (pathfinder, prompts)
- 2026-04-06: [[projects/pathfinder/notes/docs-stage-prompt-audit|Stage Prompt Audit Guide]] <- [[projects/pathfinder/sources/docs/prompt/docs/stage_prompt.md|raw]] (pathfinder, prompts)
- 2026-04-06: [[projects/pathfinder/notes/docs-production-system-prompts|The Complete Guide To Production-Grade System Prompts]] <- [[projects/pathfinder/sources/docs/prompt/how to/production_system_prompts.md|raw]] (pathfinder, prompts)
- 2026-04-06: [[projects/pathfinder/notes/docs-delegated-feature-how-to|Delegated Feature How-To Protocol]] <- [[projects/pathfinder/sources/docs/workflows/delegated_feature_how_to.md|raw]] (pathfinder, workflow)

---

## Tag Registry
<!-- Canonical tags. Check here before creating a new tag. -->

### Domain
<!-- #ai #productivity #finance #health #engineering ... -->
- learning
- protocol
- meta
- discord
- moderation
- memory
- obsidian
- pathfinder
- second-brain
- ai
- ielts
- writing
- schema
- plan
- engineering
- architecture
- evaluation
- retrieval
- prompts
- context
- workflow
- docs

### Type
<!-- #person #tool #framework #concept #project -->
- project/pathfinder
- report
- synthesis
- source-summary

### Status
<!-- #auto-fixed #needs-review -->

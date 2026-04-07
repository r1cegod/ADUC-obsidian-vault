# Retrieval Stack

## What It Is

This is PathFinder's shared free-first retrieval layer for current data agents and future agents. It replaces the old one-tool Serper-only shape with one Python service that can route web search, news search, Reddit search, and URL extraction through a normalized contract. `job_graph.py` now calls this service directly for research, while `major_graph.py` and `uni_graph.py` still use the legacy `search()` tool name through a thin compatibility wrapper so their graph shape does not break.

## The Whole Flow

```text
CALLER
  |
  |  job_graph.py direct call
  |  OR
  |  backend/tools.py wrapper for ToolNode stages
  v
SearchRequest
  |
  v
backend/retrieval/service.py
  |
  +--> general search?
  |      |
  |      +--> Serper available + quota left?
  |      |      |
  |      |      +--> yes -> GoogleSerperAPIWrapper.results()
  |      |      |
  |      |      +--> no/fail -> DDG text search
  |      |
  |      +--> optional top-hit extraction
  |
  +--> news search?
  |      |
  |      +--> DDG news search
  |
  +--> reddit search?
         |
         +--> PRAW credentials configured?
         |      |
         |      +--> yes -> subreddit/all search
         |      |
         |      +--> no -> DDG site:reddit fallback
         |
         +--> RSS/json helpers for future monitoring/fetch flows
  |
  v
SearchResponse
  |
  +--> direct consumer keeps structured hits
  |
  +--> format_search_response()
         |
         v
       text block for legacy LangChain tools
```

## Each Feature Flow

### 1. `search_web()`

```text
SearchRequest(vertical=general|news)
  |
  +--> if news:
  |      |
  |      +--> DDG news
  |
  +--> if general:
         |
         +--> SERPER_API_KEY present and local quota not exhausted?
         |      |
         |      +--> yes -> Serper structured results
         |      |
         |      +--> failure -> warning recorded
         |
         +--> DDG text fallback
  |
  +--> fetch_mode == extract_top_hits?
         |
         +--> yes -> extract first 2 URLs
  |
  v
SearchResponse
```

`SearchRequest` - normalized input model for every retrieval call. It keeps provider choice out of stage code.

`SearchResponse` - normalized output model. Stages can consume hits directly or format them back into text if they still use the old tool shape.

### 2. Serper path

```text
request.query
  |
  +--> domain allowlist appended as site: filters
  |
  v
GoogleSerperAPIWrapper.results()
  |
  v
organic results
  |
  v
normalized SearchHit objects
  |
  v
local usage counter incremented in .cache/pathfinder/retrieval_usage.json
```

`GoogleSerperAPIWrapper.results()` - LangChain community wrapper call that returns structured result JSON, not the flattened `.run()` string. Used here because the retrieval layer needs normalized hits and URLs, not a one-shot prose blob.

### 3. DDG fallback path

```text
DDG request
  |
  +--> sleep random 3-5s jitter
  |
  +--> text() or news()
  |
  +--> no results and allowlist was appended?
         |
         +--> retry raw query once
  |
  v
normalized SearchHit objects
```

The retry exists because provider-side handling of long `site:` chains is weaker than Serper. Without the retry, a valid fallback can collapse into zero hits too easily.

### 4. Reddit path

```text
SearchRequest(vertical=reddit)
  |
  +--> PRAW credentials configured?
  |      |
  |      +--> yes -> Reddit API search
  |      |
  |      +--> no -> DDG site:reddit fallback
  |
  +--> optional helper functions:
         |
         +--> fetch_reddit_rss(feed_url)
         +--> fetch_reddit_json(thread_url)
```

This is exposed now for future agents, but current PathFinder stage prompts do not depend on it yet.

### 5. URL extraction

```text
URL
  |
  +--> prefer_js=False?
  |      |
  |      +--> Jina Reader first
  |      +--> Crawl4AI second
  |
  +--> prefer_js=True?
         |
         +--> Crawl4AI first
         +--> Jina Reader second
  |
  v
(text, extraction_method)
```

`extract_url()` - shared extraction entrypoint. It hides the provider choice from callers and always returns both text and the method name so downstream code can log which extractor actually worked.

### 6. Legacy tool adapter

```text
major/uni ToolNode
  |
  v
backend/tools.py search()
  |
  v
search_web(SearchRequest(...))
  |
  v
format_search_response()
  |
  v
plain text back to the LLM tool loop
```

This adapter exists so `major_graph.py` and `uni_graph.py` do not need to be refactored in the same change as the retrieval service.

### 7. `job_graph.py` researcher flow

```text
job_research_planner
  |
  v
JobResearch packet
  |
  v
_run_web_research()
  |
  v
search_web(fetch_mode=extract_top_hits)
  |
  v
format_search_response(include_extracted=True)
  |
  v
job_research.evidence_summary + cited_sources
  |
  v
job_synthesizer
```

This replaced the old direct OpenAI web search call. The research seam is still planner -> researcher -> synthesizer, but the researcher now uses the shared free-first stack.

## How To Use

```powershell
venv\Scripts\python -m unittest test_retrieval_service_contract.py
venv\Scripts\python -c "from backend.retrieval import SearchRequest, search_web; import json; r=search_web(SearchRequest(query='data scientist fresher vietnam salary', domains_allowlist=['itviec.com','topcv.vn'], max_results=3)); print(json.dumps(r.model_dump(), ensure_ascii=True, indent=2))"
venv\Scripts\python -c "from backend.job_graph import job_graph; from backend.major_graph import major_graph; from backend.uni_graph import uni_graph; print('graphs-ok')"
venv\Scripts\python eval/run_eval.py --mode multi --file eval/job_attack.jsonl --graph job
```
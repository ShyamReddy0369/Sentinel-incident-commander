# Sentinel — Autonomous Incident Commander

A multi-agent system that detects, diagnoses, and helps resolve production
incidents in a simulated microservices environment — with full transparency
into every agent's reasoning and a tunable human-approval boundary for risky
actions.

## Why this project is different

- **Real chaos engineering, not a toy demo.** A fault-injection engine
  simulates realistic failure modes (memory leaks, bad deploys, DB pool
  exhaustion, cascading errors), so the agents have to diagnose something
  genuinely non-trivial — not just answer a canned prompt.
- **Transparent multi-agent reasoning.** Every agent's decision, confidence,
  and handoff is visible live in the console, not hidden behind a single
  chat response.
- **Tunable autonomy.** A "trust" setting controls which risk tiers the
  system can act on automatically vs. route to a human — a real AI
  governance design decision, not a gimmick.
- **Genuine PL/SQL engineering.** Incident state transitions, the audit
  trail, and reporting views are enforced in the database itself via
  stored procedures and triggers — not just app-side logic wrapped around
  a plain CRUD table.
- **Auto-generated blameless postmortems.** A tangible output with real
  engineering-org value, not just a demo artifact.

## Roadmap

- [x] Phase 0 — environment & project scaffold
- [ ] Phase 1 — Oracle DB schema: tables, procedures, triggers, views
- [ ] Phase 2 — chaos / simulation engine
- [ ] Phase 3 — Flask REST API + real-time event stream (SSE)
- [ ] Phase 4 — multi-agent orchestration (Claude API, mixed model tiers)
- [ ] Phase 5 — custom "Mission Control" frontend
- [ ] Phase 6 — Streamlit ops dashboard
- [ ] Phase 7 — testing, deployment, demo polish

## Stack

Python 3.11+, Flask, Oracle Database (PL/SQL) via `python-oracledb`,
Anthropic Claude API (Sonnet 5 for hard reasoning, Haiku 4.5 for
cheap/frequent agent steps), Streamlit, hand-built HTML/CSS/JS frontend,
Server-Sent Events for live updates.

## Phase 0 — setup

```bash
# 1. Create and activate a virtual environment
python -m venv venv
source venv/bin/activate        # Windows: venv\Scripts\activate

# 2. Install dependencies
pip install -r requirements.txt

# 3. Copy the env template (fill in real values in later phases)
cp .env.example .env

# 4. Run the Flask sanity-check app
cd backend
python app.py
```

Then visit `http://localhost:5000` in a browser — you should see a JSON
response confirming the backend is alive, plus a `/health` endpoint at
`http://localhost:5000/health`.

If both load, your environment is good and we're ready for Phase 1
(database schema).

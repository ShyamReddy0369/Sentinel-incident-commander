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
- [x] Phase 1 — Oracle DB schema: tables, procedures, triggers, views
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

## Phase 1 — database

1. Sign up for an Oracle Cloud account at `signup.oraclecloud.com` (the
   Always Free path needs no credit card).
2. Create an **Autonomous Database** instance — Transaction Processing
   workload type, Always Free checkbox on.
3. Open **Database Actions** → **SQL** for that instance — it's a
   browser-based SQL worksheet, no local client install required.
4. Run the files in `database/` **in numeric order**, pasting each
   file's contents into the worksheet and executing it before moving
   to the next:
   `01_schema.sql → 02_triggers.sql → 03_procedures.sql → 04_views.sql → 05_seed_data.sql`
5. Run `06_smoke_test.sql` one block at a time and check each result
   against the comment above it. This confirms the state machine, the
   audit trail, and the approval-queue trigger all actually work
   together before you move on.
6. Fill in `ORACLE_USER`, `ORACLE_PASSWORD`, and `ORACLE_DSN` in your
   `.env` file (the connection details are on your Autonomous
   Database's instance page in OCI) — Flask will use these in Phase 3.

`python-oracledb` (in `requirements.txt`) connects in "Thin" mode by
default, so no separate Oracle Instant Client install is needed for
local development.

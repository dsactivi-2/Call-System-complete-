# AI Voice/Call Agent System

An extensible, production-ready skeleton for an **AI-powered Voice & Call Agent** platform.  
Main language: **Python** (FastAPI / async workers). TypeScript/Node is supported in parallel via a monorepo layout.

---

## 🗂 Component Overview

| Component | Path | Description |
|-----------|------|-------------|
| **API** | `apps/api/` | REST API (FastAPI) – CRM webhooks, calendar triggers, admin endpoints |
| **Worker** | `apps/worker/` | Async post-call pipeline worker (Celery / ARQ / plain asyncio) |
| **UI** | `apps/ui/` | Optional frontend placeholder |
| **Telephony Gateway** | `services/telephony_gateway/` | Asterisk/ARI/SIP event bridge |
| **Orchestrator** | `services/orchestrator/` | Meta-orchestrator: DID routing + intent fallback |
| **Post-Call Pipeline** | `services/postcall_pipeline/` | Transcript → analysis → actions |
| **QA / Evals** | `services/qa_evals/` | QA scoring, compliance checks |
| **CRM Integration** | `services/integrations/crm/` | HubSpot / Salesforce / custom connectors |
| **Calendar Integration** | `services/integrations/calendar/` | Google / M365 / CalDAV |
| **Ticketing Integration** | `services/integrations/ticketing/` | Zendesk / Freshdesk / Jira |
| **Infra** | `infra/docker/` | Dockerfiles & Compose templates |

---

## 🚀 Local Setup (Python-first)

### Prerequisites
- Python ≥ 3.11
- (Optional) Node.js ≥ 18 for TypeScript tooling

### 1 – Clone & create virtual environment

```bash
git clone <repo-url>
cd Call-System-complete-
python -m venv .venv
source .venv/bin/activate        # Windows: .venv\Scripts\activate
pip install --upgrade pip
pip install -e ".[dev]"          # installs all extras defined in pyproject.toml
```

### 2 – Configure environment

```bash
cp .env.example .env
# Edit .env with your credentials (see .env.example for details)
```

### 3 – Run the API (development)

```bash
uvicorn apps.api.app.main:app --reload --port 8000
# API docs: http://localhost:8000/docs
```

### 4 – Run the Worker (development)

```bash
python -m apps.worker.main
```

### 5 – (Optional) Node/TypeScript tooling

```bash
npm install          # installs root dev-tools (eslint, prettier, turbo, …)
npm run lint
npm run build
```

---

## ⚙️ Configuration

All configuration is driven by environment variables.  
Copy `.env.example` → `.env` and fill in the values.

Key variables:

| Variable | Description |
|----------|-------------|
| `DATABASE_URL` | PostgreSQL connection string |
| `REDIS_URL` | Redis for task queue / cache |
| `OPENAI_API_KEY` | LLM API key (or equivalent) |
| `TELEPHONY_PROVIDER` | `asterisk` / `telnyx` / `twilio` |
| `CRM_PROVIDER` | `hubspot` / `salesforce` / `custom` |
| `CALENDAR_PROVIDER` | `google` / `m365` / `caldav` |
| `TICKETING_PROVIDER` | `zendesk` / `freshdesk` / `jira` |
| `SECRET_KEY` | App secret for JWT signing |
| `LOG_LEVEL` | `DEBUG` / `INFO` / `WARNING` |

See `.env.example` for the full list with descriptions.

---

## 🧪 Testing & Code Quality

```bash
# Run all tests
pytest

# Run linter & formatter check
ruff check .
ruff format --check .

# Auto-fix formatting
ruff format .

# Type checking
mypy apps/ services/
```

CI runs these automatically on every PR (see `.github/workflows/ci.yml`).

---

## 📚 Documentation

- [`docs/architecture.md`](docs/architecture.md) – Call flow, post-call pipeline, orchestrator
- [`docs/data-model.md`](docs/data-model.md) – High-level DB schema
- [`docs/compliance.md`](docs/compliance.md) – DSGVO / consent / recording guidelines
- [`CONTRIBUTING.md`](CONTRIBUTING.md) – How to contribute

---

## 🤝 Contributing

See [`CONTRIBUTING.md`](CONTRIBUTING.md).  
**No direct pushes to `main`** – all changes go through a reviewed PR with green CI.

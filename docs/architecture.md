# Architecture – AI Voice/Call Agent System

## 1. High-Level Call Flow

```
Caller ─────────────────────────────────────────────────────────────────────►
          │
          ▼
┌─────────────────────┐
│  Telephony Gateway  │  Receives SIP/ARI events, normalises to CallEvent
│  (Asterisk / Telnyx │  and publishes to internal message bus
│   / Twilio / …)     │
└──────────┬──────────┘
           │ CallEvent
           ▼
┌─────────────────────┐
│  Meta-Orchestrator  │  DID lookup → tenant/campaign
│                     │  Intent classifier (fallback)
│                     │  Routes to the correct AI agent
└──────────┬──────────┘
           │ RoutingDecision
           ▼
┌─────────────────────┐
│   AI Agent Layer    │  Conversational AI (LLM + TTS + STT)
│   (Agent runtime)   │  Handles dialogue, collects data, books actions
└──────────┬──────────┘
           │ Call ended event
           ▼
┌─────────────────────┐
│  Post-Call Pipeline │  Async, triggered after call ends
│                     │
│  1. Fetch recording │
│  2. Transcribe      │──► STT provider (Whisper / Deepgram / …)
│  3. Analyse         │──► LLM (summary, intent, sentiment, entities)
│  4. Dispatch        │──► CRM update
│                     │──► Calendar booking
│                     │──► Ticket creation
│                     │──► Email / SMS follow-up
└──────────┬──────────┘
           │ QAJob
           ▼
┌─────────────────────┐
│   QA / Evals        │  Automated scoring + compliance check
│                     │  Results stored + flagged for human review
└─────────────────────┘
```

---

## 2. Component Details

### Telephony Gateway (`services/telephony_gateway/`)

- Adapter hub supporting multiple providers via a unified `CallEvent` dataclass.
- Provider-specific adapters live in `services/telephony_gateway/adapters/`.
- Events are published to a message bus (Redis Streams / RabbitMQ / Kafka) for downstream consumers.

### Meta-Orchestrator (`services/orchestrator/`)

Routing priority:
1. **DID match** – exact match of dialled number against routing table (tenant + campaign).
2. **Intent match** – NLU classification of initial speech/IVR selection.
3. **Default fallback** – catch-all agent with generic handling.

Configuration lives in the DB routing table (editable via admin UI / API).

### Post-Call Pipeline (`services/postcall_pipeline/`)

Implemented as a composable async pipeline:

```
CallEnded event
  → TranscriptionStage   (STT)
  → AnalysisStage        (LLM)
  → ActionDispatchStage  (fan-out to integrations)
  → StorageStage         (persist results to DB)
  → QAJobEnqueue         (trigger QA evaluation)
```

Each stage is independently retryable with dead-letter-queue support.

### QA / Evals (`services/qa_evals/`)

- Rubric-based scoring (configurable YAML/DB rules).
- Optional LLM-based holistic evaluation.
- Compliance gate: flags calls that failed mandatory disclosure phrases.
- Outputs a `QAScore` record stored alongside the call record.

---

## 3. Infrastructure

- **Database**: PostgreSQL (call records, routing table, QA scores, audit log).
- **Cache / Queue**: Redis (task queue for pipeline + Pub/Sub for real-time events).
- **Object Storage**: S3-compatible (recordings, transcripts – encrypted at rest).
- **API Layer**: FastAPI (async, OpenAPI docs at `/docs`).
- **Worker**: Async Python worker (Celery / ARQ) consuming pipeline jobs.

---

## 4. Deployment (target)

```
Internet ─► Load Balancer ─► API containers (horizontal scale)
                          ─► Worker containers (horizontal scale)
                          ─► Telephony Gateway (single or clustered)
                          ─► Orchestrator (stateless, horizontal scale)
                ▼
           PostgreSQL (managed RDS or self-hosted)
           Redis (managed ElastiCache or self-hosted)
           S3 (recordings / transcripts)
```

See `infra/docker/docker-compose.yml` for local dev setup.

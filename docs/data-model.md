# Data Model – High-Level Schema

> **Status**: Planned / placeholder – actual migrations will be in `alembic/` once the ORM models are defined.

---

## Core Tables

### `calls`

| Column | Type | Notes |
|--------|------|-------|
| `id` | UUID PK | Call identifier |
| `created_at` | TIMESTAMPTZ | Call start time |
| `ended_at` | TIMESTAMPTZ | Call end time (nullable until ended) |
| `direction` | ENUM(`inbound`,`outbound`) | |
| `from_number` | VARCHAR(32) | Caller number (E.164) |
| `to_number` | VARCHAR(32) | Dialled number (E.164) |
| `tenant_id` | UUID FK → tenants | |
| `campaign_id` | UUID FK → campaigns | nullable |
| `agent_id` | VARCHAR(64) | AI agent identifier |
| `status` | ENUM(`active`,`ended`,`failed`) | |
| `recording_url` | TEXT | S3 URL (encrypted) |
| `duration_seconds` | INT | |

### `transcripts`

| Column | Type | Notes |
|--------|------|-------|
| `id` | UUID PK | |
| `call_id` | UUID FK → calls | |
| `created_at` | TIMESTAMPTZ | |
| `provider` | VARCHAR(64) | e.g. `whisper`, `deepgram` |
| `text` | TEXT | Full transcript |
| `words` | JSONB | Word-level timestamps (optional) |
| `language` | VARCHAR(8) | BCP-47 code |

### `call_analyses`

| Column | Type | Notes |
|--------|------|-------|
| `id` | UUID PK | |
| `call_id` | UUID FK → calls | |
| `created_at` | TIMESTAMPTZ | |
| `summary` | TEXT | LLM-generated summary |
| `intent` | VARCHAR(128) | Primary intent detected |
| `sentiment` | ENUM(`positive`,`neutral`,`negative`) | |
| `entities` | JSONB | Named entities (names, dates, products, …) |
| `action_items` | JSONB | Extracted follow-up actions |

### `qa_scores`

| Column | Type | Notes |
|--------|------|-------|
| `id` | UUID PK | |
| `call_id` | UUID FK → calls | |
| `created_at` | TIMESTAMPTZ | |
| `overall_score` | FLOAT | 0.0 – 1.0 |
| `compliance_passed` | BOOL | |
| `flags` | JSONB | List of compliance flag codes |
| `rubric_scores` | JSONB | Per-dimension scores |
| `reviewed_by` | UUID FK → users | nullable (human review) |

### `routing_rules`

| Column | Type | Notes |
|--------|------|-------|
| `id` | UUID PK | |
| `did` | VARCHAR(32) | Dialled number pattern (exact or wildcard) |
| `tenant_id` | UUID FK → tenants | |
| `campaign_id` | UUID FK → campaigns | nullable |
| `agent_id` | VARCHAR(64) | Target agent |
| `priority` | INT | Lower = higher priority |
| `active` | BOOL | |

### `tenants`

| Column | Type | Notes |
|--------|------|-------|
| `id` | UUID PK | |
| `name` | VARCHAR(256) | |
| `crm_provider` | VARCHAR(64) | |
| `calendar_provider` | VARCHAR(64) | |
| `ticketing_provider` | VARCHAR(64) | |
| `settings` | JSONB | Tenant-specific config |

---

## Relationships

```
tenants 1──* routing_rules
tenants 1──* calls
calls 1──1 transcripts
calls 1──1 call_analyses
calls 1──1 qa_scores
calls *──1 campaigns
```

---

## Notes

- All PII (phone numbers, transcripts) should be encrypted at rest.
- Retention policy: see `docs/compliance.md`.
- Indexes: add on `calls(tenant_id, created_at)`, `routing_rules(did)`, `calls(from_number)`.

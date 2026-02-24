"""
AI Call Agent - API Service (FastAPI skeleton)

Entry point for the REST API.  Handles CRM webhooks, calendar triggers,
admin/reporting endpoints, and inbound call routing requests.

TODO:
  - Add authentication middleware (JWT / API-key)
  - Connect database session (SQLAlchemy / SQLModel)
  - Register additional routers (crm, calendar, telephony)
"""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from apps.api.app.routers import calls, health

app = FastAPI(
    title="AI Call Agent API",
    description="REST API for the AI Voice/Call Agent system.",
    version="0.1.0",
)

# ---------------------------------------------------------------------------
# Middleware
# ---------------------------------------------------------------------------
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # TODO: restrict in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ---------------------------------------------------------------------------
# Routers
# ---------------------------------------------------------------------------
app.include_router(health.router, tags=["health"])
app.include_router(calls.router, prefix="/calls", tags=["calls"])

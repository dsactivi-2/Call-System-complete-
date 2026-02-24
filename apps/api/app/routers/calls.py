"""
Call management endpoints (skeleton).

TODO:
  - POST /calls/inbound   - receive inbound call webhook from telephony provider
  - POST /calls/outbound  - initiate outbound call
  - GET  /calls/{call_id} - retrieve call metadata & transcript
"""

from fastapi import APIRouter

router = APIRouter()


@router.get("/")
async def list_calls() -> dict:
    """List recent calls (placeholder)."""
    # TODO: query database
    return {"calls": [], "total": 0}


@router.post("/inbound")
async def inbound_call_webhook(payload: dict) -> dict:
    """
    Receive inbound call event from telephony gateway.

    TODO:
      - Validate webhook signature
      - Publish event to message queue for orchestrator
    """
    return {"status": "received", "payload": payload}

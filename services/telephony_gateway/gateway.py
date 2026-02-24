"""Telephony Gateway - core event handler skeleton."""

import logging
from dataclasses import dataclass, field
from typing import Any

logger = logging.getLogger(__name__)


@dataclass
class CallEvent:
    """Normalised representation of a call lifecycle event."""

    event_type: str  # "call.started" | "call.ended" | "dtmf" | …
    call_id: str
    direction: str  # "inbound" | "outbound"
    from_number: str
    to_number: str
    metadata: dict[str, Any] = field(default_factory=dict)


class TelephonyGateway:
    """
    Adapter hub for telephony providers.

    TODO:
      - Load provider from config (TELEPHONY_PROVIDER env var)
      - Implement start() / stop() lifecycle
      - Route raw provider events → CallEvent → message bus
    """

    def __init__(self, provider: str = "asterisk") -> None:
        self.provider = provider
        logger.info("TelephonyGateway initialised (provider=%s)", provider)

    async def handle_event(self, raw_event: dict[str, Any]) -> CallEvent:
        """
        Convert a raw provider event into a normalised CallEvent.

        TODO: implement per-provider parsing logic.
        """
        logger.debug("Raw event received: %s", raw_event)
        # Placeholder - return a stub event
        return CallEvent(
            event_type=raw_event.get("type", "unknown"),
            call_id=raw_event.get("call_id", ""),
            direction=raw_event.get("direction", "inbound"),
            from_number=raw_event.get("from", ""),
            to_number=raw_event.get("to", ""),
            metadata=raw_event,
        )

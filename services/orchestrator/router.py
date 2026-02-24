"""Orchestrator - DID-based routing + intent fallback (skeleton)."""

import logging
from dataclasses import dataclass

logger = logging.getLogger(__name__)


@dataclass
class RoutingDecision:
    """Result of the orchestrator's routing logic."""

    agent_id: str
    campaign_id: str | None
    tenant_id: str | None
    reason: str  # "did_match" | "intent_match" | "fallback"


class MetaOrchestrator:
    """
    Routes a call event to the appropriate AI agent pipeline.

    TODO:
      - Inject routing table / DB session
      - Implement did_lookup()
      - Implement intent_classify()
      - Add async support
    """

    def route(self, did: str, intent: str | None = None) -> RoutingDecision:
        """
        Determine which agent should handle the call.

        Priority order:
          1. Exact DID match in routing table
          2. Intent-based routing (if DID not found)
          3. Default fallback agent
        """
        logger.info("Routing DID=%s intent=%s", did, intent)

        # TODO: replace stubs with real lookup logic
        return RoutingDecision(
            agent_id="default-agent",
            campaign_id=None,
            tenant_id=None,
            reason="fallback",
        )

"""Ticketing connector base class (skeleton)."""

import logging
from abc import ABC, abstractmethod
from typing import Any

logger = logging.getLogger(__name__)


class BaseTicketingConnector(ABC):
    """Abstract base for all ticketing connectors."""

    @abstractmethod
    async def create_ticket(
        self,
        subject: str,
        description: str,
        requester_email: str,
        priority: str = "normal",
        tags: list[str] | None = None,
    ) -> str:
        """Create a support ticket. Returns ticket ID."""

    @abstractmethod
    async def update_ticket(self, ticket_id: str, update_data: dict[str, Any]) -> bool:
        """Update an existing ticket. Returns success flag."""


class ZendeskConnector(BaseTicketingConnector):
    """Zendesk connector (placeholder)."""

    def __init__(self, subdomain: str, api_token: str, email: str) -> None:
        self.subdomain = subdomain
        self.api_token = api_token
        self.email = email
        # TODO: initialise Zendesk SDK client

    async def create_ticket(
        self,
        subject: str,
        description: str,
        requester_email: str,
        priority: str = "normal",
        tags: list[str] | None = None,
    ) -> str:
        raise NotImplementedError("TODO: implement Zendesk create_ticket")

    async def update_ticket(self, ticket_id: str, update_data: dict[str, Any]) -> bool:
        raise NotImplementedError("TODO: implement Zendesk update_ticket")

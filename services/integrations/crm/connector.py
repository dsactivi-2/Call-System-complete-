"""CRM connector base class and factory (skeleton)."""

import logging
from abc import ABC, abstractmethod
from typing import Any

logger = logging.getLogger(__name__)


class BaseCRMConnector(ABC):
    """Abstract base for all CRM connectors."""

    @abstractmethod
    async def upsert_contact(self, phone: str, data: dict[str, Any]) -> dict[str, Any]:
        """Create or update a contact record."""

    @abstractmethod
    async def log_call(self, contact_id: str, call_data: dict[str, Any]) -> str:
        """Log a call activity against a contact. Returns activity ID."""

    @abstractmethod
    async def get_contact(self, phone: str) -> dict[str, Any] | None:
        """Fetch contact by phone number. Returns None if not found."""


class HubSpotConnector(BaseCRMConnector):
    """HubSpot CRM connector (placeholder)."""

    def __init__(self, api_key: str) -> None:
        self.api_key = api_key
        # TODO: initialise HubSpot SDK client

    async def upsert_contact(self, phone: str, data: dict[str, Any]) -> dict[str, Any]:
        logger.info("HubSpot upsert_contact phone=%s", phone)
        raise NotImplementedError("TODO: implement HubSpot upsert_contact")

    async def log_call(self, contact_id: str, call_data: dict[str, Any]) -> str:
        logger.info("HubSpot log_call contact_id=%s", contact_id)
        raise NotImplementedError("TODO: implement HubSpot log_call")

    async def get_contact(self, phone: str) -> dict[str, Any] | None:
        logger.info("HubSpot get_contact phone=%s", phone)
        raise NotImplementedError("TODO: implement HubSpot get_contact")


def get_crm_connector(provider: str, **kwargs: Any) -> BaseCRMConnector:
    """Factory: return the configured CRM connector."""
    connectors: dict[str, type[BaseCRMConnector]] = {
        "hubspot": HubSpotConnector,
        # "salesforce": SalesforceConnector,  # TODO
    }
    if provider not in connectors:
        raise ValueError(f"Unknown CRM provider: {provider!r}. Available: {list(connectors)}")
    return connectors[provider](**kwargs)

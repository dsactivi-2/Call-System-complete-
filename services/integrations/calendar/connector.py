"""Calendar connector base class (skeleton)."""

import logging
from abc import ABC, abstractmethod
from datetime import datetime
from typing import Any

logger = logging.getLogger(__name__)


class BaseCalendarConnector(ABC):
    """Abstract base for all calendar connectors."""

    @abstractmethod
    async def create_event(
        self,
        title: str,
        start: datetime,
        end: datetime,
        attendees: list[str],
        description: str = "",
    ) -> str:
        """Create a calendar event. Returns event ID."""

    @abstractmethod
    async def get_free_slots(
        self,
        attendee_email: str,
        date_from: datetime,
        date_to: datetime,
    ) -> list[dict[str, Any]]:
        """Return available time slots for an attendee."""


class GoogleCalendarConnector(BaseCalendarConnector):
    """Google Calendar connector (placeholder)."""

    def __init__(self, credentials_json: str) -> None:
        self.credentials_json = credentials_json
        # TODO: initialise Google API client

    async def create_event(
        self,
        title: str,
        start: datetime,
        end: datetime,
        attendees: list[str],
        description: str = "",
    ) -> str:
        raise NotImplementedError("TODO: implement Google Calendar create_event")

    async def get_free_slots(
        self,
        attendee_email: str,
        date_from: datetime,
        date_to: datetime,
    ) -> list[dict[str, Any]]:
        raise NotImplementedError("TODO: implement Google Calendar get_free_slots")

"""Post-call pipeline runner (skeleton)."""

import logging
from dataclasses import dataclass, field
from typing import Any

logger = logging.getLogger(__name__)


@dataclass
class CallRecord:
    """Minimal call record passed through the pipeline."""

    call_id: str
    recording_url: str | None = None
    transcript: str | None = None
    analysis: dict[str, Any] = field(default_factory=dict)
    actions_taken: list[str] = field(default_factory=list)


class PostCallPipeline:
    """
    Runs post-call processing steps sequentially.

    TODO:
      - Make stages configurable / plug-in based
      - Add async execution + error handling
      - Publish completion event to message bus
    """

    async def run(self, call_id: str, recording_url: str | None = None) -> CallRecord:
        record = CallRecord(call_id=call_id, recording_url=recording_url)

        record = await self._transcribe(record)
        record = await self._analyse(record)
        record = await self._dispatch_actions(record)

        logger.info("Pipeline complete for call_id=%s", call_id)
        return record

    async def _transcribe(self, record: CallRecord) -> CallRecord:
        """Step 1 - Transcribe audio to text."""
        logger.debug("Transcribing call_id=%s", record.call_id)
        # TODO: call transcription service (Whisper / Deepgram / …)
        record.transcript = "[TRANSCRIPT PLACEHOLDER]"
        return record

    async def _analyse(self, record: CallRecord) -> CallRecord:
        """Step 2 - Analyse transcript with LLM."""
        logger.debug("Analysing call_id=%s", record.call_id)
        # TODO: LLM call for summary, intent, sentiment, entities
        record.analysis = {
            "summary": "[SUMMARY PLACEHOLDER]",
            "intent": "unknown",
            "sentiment": "neutral",
        }
        return record

    async def _dispatch_actions(self, record: CallRecord) -> CallRecord:
        """Step 3 - Trigger downstream actions (CRM, calendar, ticket, …)."""
        logger.debug("Dispatching actions for call_id=%s", record.call_id)
        # TODO: conditionally trigger integrations based on analysis results
        record.actions_taken.append("placeholder_action")
        return record

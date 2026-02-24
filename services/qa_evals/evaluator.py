"""QA / Compliance evaluator skeleton."""

import logging
from dataclasses import dataclass, field

logger = logging.getLogger(__name__)


@dataclass
class QAScore:
    """Result of a QA evaluation run."""

    call_id: str
    overall_score: float  # 0.0 - 1.0
    compliance_passed: bool
    flags: list[str] = field(default_factory=list)
    notes: str | None = None


class QAEvaluator:
    """
    Evaluates a call transcript against QA rubrics and compliance rules.

    TODO:
      - Load rubric / rule definitions from config or DB
      - Implement LLM-based scoring
      - Add per-rule weight configuration
    """

    def evaluate(self, call_id: str, transcript: str) -> QAScore:
        """
        Score the transcript and return a QAScore.

        TODO: replace stub with real evaluation logic.
        """
        logger.info("Evaluating call_id=%s", call_id)
        # Placeholder - always passes with neutral score
        return QAScore(
            call_id=call_id,
            overall_score=1.0,
            compliance_passed=True,
            notes="Placeholder evaluation - implement real scoring",
        )

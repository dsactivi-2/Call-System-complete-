"""Smoke tests - verify core service modules import and basic logic works."""

import pytest


def test_telephony_gateway_imports() -> None:
    """TelephonyGateway should be importable."""
    from services.telephony_gateway.gateway import CallEvent, TelephonyGateway

    gw = TelephonyGateway(provider="asterisk")
    assert gw.provider == "asterisk"
    _ = CallEvent  # ensure it's exported


def test_orchestrator_routing_fallback() -> None:
    """Orchestrator should return a fallback routing decision for unknown DID."""
    from services.orchestrator.router import MetaOrchestrator

    orchestrator = MetaOrchestrator()
    decision = orchestrator.route(did="+49123456789")
    assert decision.agent_id == "default-agent"
    assert decision.reason == "fallback"


def test_qa_evaluator_returns_score() -> None:
    """QAEvaluator should return a QAScore without raising."""
    from services.qa_evals.evaluator import QAEvaluator

    evaluator = QAEvaluator()
    score = evaluator.evaluate(call_id="test-001", transcript="Hello, this is a test call.")
    assert 0.0 <= score.overall_score <= 1.0
    assert isinstance(score.compliance_passed, bool)


@pytest.mark.asyncio
async def test_postcall_pipeline_smoke() -> None:
    """Pipeline should run end-to-end without errors (stub mode)."""
    from services.postcall_pipeline.pipeline import PostCallPipeline

    pipeline = PostCallPipeline()
    record = await pipeline.run(call_id="test-001")
    assert record.call_id == "test-001"
    assert record.transcript is not None
    assert "summary" in record.analysis

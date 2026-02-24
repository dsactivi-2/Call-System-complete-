"""
Meta-Orchestrator Service

Routes incoming calls to the correct AI agent based on:
  - DID (Dialled Number Identification) → tenant / campaign mapping
  - Intent detected in IVR / initial speech
  - Fallback rules (time-of-day, agent availability, …)

TODO:
  - Load routing table from database / config
  - Integrate with NLU/intent classifier
  - Implement fallback chain
"""

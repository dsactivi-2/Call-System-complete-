"""
Post-Call Pipeline Service

Orchestrates the sequence of steps executed after a call ends:

  1. Retrieve audio recording (from telephony storage or S3)
  2. Transcribe (Whisper / Deepgram / AssemblyAI / …)
  3. Analyse transcript (LLM summarisation, intent extraction, sentiment)
  4. Trigger actions:
       - Update CRM record
       - Create calendar event
       - Open support ticket
       - Send follow-up email / SMS

TODO:
  - Implement each step as a composable pipeline stage
  - Add retry logic + dead-letter queue
  - Store results in DB and emit domain events
"""

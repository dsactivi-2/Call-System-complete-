"""
Telephony Gateway Service

Bridges telephony providers (Asterisk/ARI, SIP, Telnyx, Twilio, …)
with the rest of the system via a normalised event model.

TODO:
  - Implement provider-specific adapters (see adapters/ sub-package)
  - Normalise events to CallEvent schema
  - Publish events to message bus (Redis Streams / RabbitMQ / Kafka)
"""

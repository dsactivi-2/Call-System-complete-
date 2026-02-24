# Compliance, Consent & Data Protection

> **Disclaimer**: This document provides high-level guidance only. Consult your legal team
> before deploying in a production environment involving real callers.

---

## 1. Consent & Recording Disclosure

### Legal Basis (DSGVO / GDPR Art. 6)

Recording phone calls requires a **valid legal basis**:

| Basis | When applicable |
|-------|-----------------|
| **Consent** (Art. 6(1)(a)) | Preferred; explicit opt-in required before recording starts |
| **Legitimate interest** (Art. 6(1)(f)) | Possible for B2B quality monitoring; document balancing test |
| **Contract performance** (Art. 6(1)(b)) | When recording is necessary to perform the service |

### Implementation Requirements

- **Mandatory disclosure**: Play a recorded announcement at call start:
  > *"This call may be recorded for quality assurance and training purposes."*
- Store **consent timestamp** and **disclosure text version** in the database alongside the call record.
- Allow callers to **opt out** of recording; the call must still be serviceable without a recording.
- In some jurisdictions (e.g. some US states), **two-party (all-party) consent** is required – check applicable local laws.

---

## 2. Data Minimisation

- Only collect data that is **necessary** for the stated purpose.
- Do **not** store sensitive categories (Art. 9) such as health information unless explicitly required and with explicit consent.
- Strip or pseudonymise PII in transcripts before feeding to third-party LLM APIs, where possible.

---

## 3. Data Storage & Security

### Recordings
- Stored in S3-compatible object storage with **server-side encryption (SSE-S3 or SSE-KMS)**.
- Access restricted to the processing pipeline service accounts (IAM least-privilege).
- Direct pre-signed URLs expire after ≤ 1 hour.

### Transcripts & Analyses
- Stored in PostgreSQL with **encryption at rest** enabled.
- Column-level encryption for fields containing PII (phone numbers, names).

### Access Control
- Role-based access: only authorised agents/admins can retrieve call recordings and transcripts.
- All access is **audit-logged**.

---

## 4. Retention & Deletion

| Data type | Suggested retention | Basis |
|-----------|--------------------|-|
| Call metadata | 24 months | Legitimate interest (billing, dispute) |
| Recordings | 90 days (default) | Quality assurance |
| Transcripts | 12 months | Quality assurance / legal |
| QA scores | 36 months | Internal audit trail |
| Raw LLM inputs/outputs | 30 days | Debugging only |

- Implement automated **purge jobs** that delete expired records and associated S3 objects.
- Provide a **Right to Erasure** (Art. 17) workflow: callers can request deletion of all data linked to their number.
- Document retention periods in the company's **Record of Processing Activities (RoPA)**.

---

## 5. Third-Party Processing

When sending data to third-party APIs (LLM providers, STT services, CRM vendors):

- Ensure a **Data Processing Agreement (DPA)** is in place.
- Prefer providers with EU data residency options (or equivalent adequacy decision).
- Log which third parties received which data and when.
- Avoid sending raw audio to LLM providers unless their DPA explicitly covers it.

---

## 6. Incident Response

- Define a process to detect and report a data breach within **72 hours** (GDPR Art. 33).
- Maintain an incident register.
- Include the call recording system in regular **penetration testing** scope.

---

## 7. Checklist Before Go-Live

- [ ] Legal basis documented for each data processing activity
- [ ] Consent / disclosure announcement recorded and approved by legal
- [ ] DPAs signed with all third-party processors
- [ ] Retention policy implemented in code (automated purge jobs)
- [ ] Right-to-erasure endpoint implemented and tested
- [ ] Encryption at rest enabled for DB and object storage
- [ ] Access control and audit logging verified
- [ ] Penetration test scheduled
- [ ] DPO (Data Protection Officer) notified / consulted (if applicable)

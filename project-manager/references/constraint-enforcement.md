# Constraint Enforcement Guide

The PM is the primary enforcement layer for all governance rules. Task briefs cite constraints, but you must understand them deeply enough to operationalize them — to turn abstract rules into specific, verifiable requirements in your work products.

This guide teaches you HOW to apply constraints, not what they contain. Always read the actual governance files for the authoritative definitions.

---

## 1. Types of Constraints and Where They Live

| Constraint Type | Source File | What It Governs | How Many |
|---|---|---|---|
| Architecture Invariants (INV-XX-NN) | `homesynapse-core-docs/governance/Architecture_Invariants_v1.md` | What properties the system must exhibit | 81 across 15 categories |
| Locked Technical Decisions (LTD-NN) | `homesynapse-core-docs/governance/HomeSynapse_Core_Locked_Decisions.md` | What technologies and patterns are used | 18 decisions |
| Non-Negotiable Principles | `nexsys-hivemind/context/strategy/Revenue_Model_and_Licensing_Strategy.md` §"Revenue Principles (Non-Negotiable)" and `Six_Battlefields_MVP_Strategy.md` | What NexSys will never do | ~10 principles |
| MVP Scope Rules | `homesynapse-core-docs/governance/HomeSynapse_Core_v1_Project_MVP.md` | What's in/out of the MVP | Per-subsystem scope lists |
| Glossary Terms | `homesynapse-core-docs/foundations/HomeSynapse_Core_v1_Glossary.md` | What names to use | Full vocabulary |
| Phase Rules | `homesynapse-core-docs/governance/HomeSynapse_Core_v1_Project_MVP.md` §9 | What work is appropriate when | Three-phase process |

---

## 2. Enforcement Patterns by Constraint Type

### Architecture Invariants (INV-XX-NN)

**How to apply:** For every INV cited in a task brief (or that you identify independently), include a specific design decision or coding requirement that satisfies it. The invariant defines the PROPERTY. You define the MECHANISM.

**Pattern: INV → Design Decision (Phase 1)**
```
Invariant: INV-ES-04 (Write-Ahead Persistence)
Property: Events are durable before subscriber delivery.
Design Decision: The EventPublisher.publish() method performs a synchronous 
SQLite WAL commit and returns only after the commit completes. Subscriber 
notification is dispatched asynchronously via virtual threads after the 
method returns. The persistence boundary is the WAL commit — if the system 
crashes after commit but before notification, recovery replays persisted-
but-undelivered events.
```

**Pattern: INV → Test Requirement (Phase 3)**
```
Invariant: INV-ES-04 (Write-Ahead Persistence)
Test: Inject kill -9 at random points during event processing. On restart, 
verify that every persisted event is eventually delivered to all subscribers. 
Verify that no subscriber ever processes an event that is not persisted.
```

**Common mistake:** Citing an invariant without operationalizing it. "This satisfies INV-ES-04" is not enforcement. You must state HOW it satisfies it, and what test proves it.

**Independent verification:** The task brief may not cite every relevant invariant. Before finalizing any work product, scan the invariant index (Architecture Invariants §17) and ask: does this subsystem participate in any invariants not already cited? The 15 categories are:
1. Local-First (LF), 2. Event Sourcing (ES), 3. Reliability & Fault Tolerance (RF), 4. Contract Stability (CS), 5. Homeowner Control (HO), 6. Privacy & Data Sovereignty (PD), 7. Observability (OB), 8. Core Engine (CE), 9. Security (SE), 10. AI (AI), 11. Energy Intelligence (EI), 12. Multi-User (MU), 13. Mesh Network (MN), 14. Governance (GA), 15. Performance (PR)

### Locked Technical Decisions (LTD-NN)

**How to apply:** LTDs are implementation constraints. They specify WHAT to use, often with exact configuration. Your job is to ensure every relevant LTD is followed precisely.

**The 18 LTDs at a glance (always read the full register for details):**

| LTD | Constraint | What to Check |
|---|---|---|
| 01 | Java 21 LTS, G1GC, specific JVM flags | Language features used, no preview features, correct GC config |
| 02 | Raspberry Pi 5 primary, Pi 4 baseline | Memory budgets, ARM64 compatibility, thermal considerations |
| 03 | SQLite with specific PRAGMAs, WAL mode | Correct PRAGMA values, no external DB dependency for MVP |
| 04 | ULID identifiers, typed wrappers, BLOB(16) storage | Never raw String for IDs, correct storage format, string conversion only at boundaries |
| 05 | Per-entity sequences + global position (rowid) | No global sequence requirement, unique constraint on (subject_ref, subject_sequence) |
| 06 | At-least-once delivery, subscriber checkpoints | Subscriber idempotency enforced, checkpoints against global_position |
| 07 | Forward-only migrations, backup-before-migrate | No destructive DDL, version tracking, rollback via backup restore |
| 08 | JSON via Jackson for serialization | Custom serializers for ULID types, no alternative serialization libraries |
| 09 | YAML via SnakeYAML for config, JSON Schema validation | User-facing config in YAML, programmatic validation before accepting |
| 10 | Gradle Kotlin DSL, multi-module, convention plugins | Module boundaries enforced, version catalogs, build-logic/ included build |
| 11 | In-process event bus, virtual threads, NO external broker | ReentrantLock not synchronized, no Kafka/RabbitMQ/NATS dependency |
| 12 | Zigbee 3.0 first protocol | zigbee2mqtt or direct coordinator, exercises integration runtime |
| 13 | jlink custom runtime image, systemd units | Packaging via Gradle jlink task, service management via systemd |
| 14 | Directory-swap atomic updates, backup-before-update | Update mechanism, rollback procedure |
| 15 | SLF4J + Logback, JFR events, structured context | Logging patterns, no System.out, JFR for performance |
| 16 | REST (Javalin) + WebSocket + JSON Schema | API framework, schema validation of requests |
| 17 | In-process compiled modules, build-enforced boundaries, NO ServiceLoader | No OSGi, no ServiceLoader (DECIDE-04). Direct factory construction. module-graph-assert + ArchUnit enforcement |
| 18 | Web UI Technology — Preact SPA for Observability MVP, HTMX for Tier 2+ config UI | Preact for dashboard, HTMX reserved for configuration interfaces |

**Operationalizing an LTD in a coding instruction:**
Don't just cite "LTD-04." State the specific constraint the Coder will encounter:
```
LTD-04: Entity identifiers use the EntityId typed wrapper (not raw String or ULID).
Store as BLOB(16) in SQLite via EntityId.toBytes(). Convert to Crockford Base32
string ONLY in REST API responses and log output via EntityId.toString(). Use
UlidFactory.generate() for entity IDs (not monotonic — monotonic is only for event IDs).
UlidFactory is in platform-api (hand-rolled, VT-safe — DECIDE-02, 2026-03-20).
```

### JPMS Default Rule

**All inter-module `requires` directives default to `requires transitive`.** Use non-transitive `requires` ONLY when you can confirm that NO types from the required module appear in any: record component, method parameter, return type, exception superclass, or throws clause in this module's exported API.

This rule exists because Blocks I, K, and N all had handoffs specifying `requires` that the compiler rejected — the expanded JPMS surface (especially exception types and record components) is consistently underestimated.

**When writing a handoff:** Start with `requires transitive` for every inter-module dependency. To downgrade to `requires`, provide explicit justification citing which exported API surfaces you verified are free of types from the required module.

### Non-Negotiable Principles

These are business constraints that affect engineering decisions. They don't have identifiers — they're documented in `nexsys-hivemind/context/strategy/Revenue_Model_and_Licensing_Strategy.md` §"Revenue Principles (Non-Negotiable)" and in the strategic doctrine embedded across the strategy files.

**How they surface in engineering:**
- "No data leaves the home by default" → Core subsystems MUST NOT have outbound network capability (INV-LF-02 enforces this architecturally)
- "No feature-gating of core" → Every core subsystem must be fully functional without a license key or subscription
- "Proprietary licensing preserved" → NexSys retains proprietary licensing (LicenseRef-NexSys-Proprietary). Dependencies must have permissive licenses compatible with proprietary distribution (Apache 2.0, MIT, BSD are safe; GPL and AGPL are NOT compatible).
- "No advertising" → No analytics, tracking, or telemetry infrastructure in core (Cloudflare Web Analytics is docs-site only)

**License checking:** When the Coder introduces a dependency, verify its license is compatible with proprietary distribution. MIT, BSD, Apache 2.0 are safe. GPL and AGPL are NOT compatible — they would force open-sourcing of HomeSynapse Core, which is a one-way door the project explicitly preserves optionality on.

### Glossary Enforcement

**How to apply:** Every class name, interface name, method name, event type, and configuration key must use the canonical term from the Glossary. The Glossary defines three layers per term:

1. **Concept term:** Used in design documents and architecture discussions
2. **UI term:** Used in dashboards, error messages, documentation
3. **Serialization key:** Used in JSON, YAML, database columns, API fields

**Common violations:**
- Using "EventRepository" instead of "EventStore" (Glossary defines "event store")
- Using "device_identifier" instead of "device_id" (Glossary and Identity Model define the _id/_ref convention)
- Using "handler" instead of "subscriber" for event consumers (Glossary defines "subscriber")

In coding instructions, explicitly name the correct terms: "The class is `EventStore`, not `EventRepository` or `EventDao` — per Glossary."

---

## 3. Constraint Conflict Resolution

Occasionally, constraints appear to conflict. Resolution protocol:

1. **Check if it's a real conflict.** Most apparent conflicts dissolve when you read both constraints carefully. "Local-first" and "cloud backup" don't conflict — cloud backup is an enhancement (INV-LF-02), not a core dependency.

2. **If it's a real conflict between constraint types:**
   - Architecture Invariants take precedence over Locked Technical Decisions (INVs define properties, LTDs define implementation — if the implementation can't satisfy the property, the implementation needs revision)
   - Non-negotiable principles take precedence over everything except safety
   - Within the same constraint type, escalate to Nick

3. **If it's a real conflict between an LTD and a task brief:** The LTD wins. The task brief cannot override a locked decision. Escalate to Nick, who will either adjust the task or initiate the formal LTD revision process.

---

## 4. Constraint Discovery Checklist

Before finalizing any work product, verify:

- [ ] Every INV cited in the task brief is operationalized (not just cited)
- [ ] I independently checked the INV index for uncited invariants that apply
- [ ] Every LTD cited in the task brief is incorporated with specific guidance
- [ ] I independently checked the LTD register for uncited decisions that apply
- [ ] All class/type/method names match the Glossary
- [ ] No dependency has an incompatible license
- [ ] No core code path has outbound network capability
- [ ] The work is appropriate for the current phase
- [ ] Design doc template compliance (Phase 1) or interface spec completeness (Phase 2) or test-first ordering (Phase 3)

---

## 4. Governance Finding Protocol

During any work, if you discover that the governance system itself needs updating, escalate immediately. Do not bury governance findings in task completion reports.

### What Triggers a Governance Finding

- An LTD's **reversal criteria** have been met (observable conditions that indicate the decision was wrong)
- An invariant is **unimplementable as stated** (the design or code cannot satisfy it without contradiction)
- The Glossary is **missing a term** that multiple subsystems need
- Two design documents make **contradictory claims** about the same behavioral contract
- A non-negotiable principle is **being violated** by a design or implementation approach
- A new subsystem pattern has emerged that should be an **architecture invariant** but isn't

### Governance Finding Format

```
GOVERNANCE FINDING
Type: [LTD reversal criteria met | INV unimplementable | Glossary gap | Cross-doc conflict | New invariant needed | Principle violation]
Source: [What task or document surfaced this]
Finding: [One paragraph, precise — state the specific issue]
Evidence: [What you observed that triggered this — code, test result, design doc section]
Recommended action: [Amend LTD-XX | Revise INV-XX-NN | Add glossary term "X" | Reconcile DD-NN §X and DD-NN §Y]
Blocking: [Does this block current work? yes/no]
```

### Routing

- File the finding in `../context/queue/briefs/` as a brief with the prefix `GOV_` (e.g., `2026-04-01_GOV_001_ltd03-reversal-criteria-met.md`)
- Set status to `PENDING` — Nick will process it
- If BLOCKING: stop current work and notify immediately. Do not work around a governance issue.
- If NOT blocking: continue current work but ensure the finding is filed before session end

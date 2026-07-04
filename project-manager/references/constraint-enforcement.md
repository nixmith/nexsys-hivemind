<!--
file: project-manager/references/constraint-enforcement.md
purpose: How the PM operationalizes governance rules into specific, verifiable requirements in work products.
audience: PM
update-cadence: ad-hoc
state-type: reference
status: CURRENT
last-verified: 2026-07-04 (v19 currency pass — the 19-row LTD at-a-glance table spot-verified at AMD-98/174/52: NO row change; the AMD-98 EZSP band narrowing is register/AMD-level [no LTD asserts protocol versions] and the confirmation-pipeline realizations are AMD-90/95/97/98 + Doc 07/08 territory; rows 16/17 stand as corrected at the v17 skills pass)
-->

# Constraint Enforcement Guide

The PM is the primary enforcement layer for all governance rules. Task briefs cite constraints, but you must understand them deeply enough to operationalize them — to turn abstract rules into specific, verifiable requirements in your work products.

This guide teaches you HOW to apply constraints, not what they contain. Always read the actual governance files for the authoritative definitions.

---

## 1. Types of Constraints and Where They Live

| Constraint Type | Source File | What It Governs | How Many |
|---|---|---|---|
| Architecture Invariants (INV-XX-NN) | `homesynapse-core-docs/governance/Architecture_Invariants_v1.md` | What properties the system must exhibit | **read §0.3 + §17 for the live count** (≈135 across ≈34 categories — base `INV-XX-NN` + per-amendment `AMD-NN-INV`; rises every amendment, so never cite a frozen number) |
| Locked Technical Decisions (LTD-NN) | `homesynapse-core-docs/governance/HomeSynapse_Core_Locked_Decisions.md` | What technologies and patterns are used | 19 decisions |
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

**Independent verification:** The task brief may not cite every relevant invariant. Before finalizing any work product, scan the invariant index (Architecture Invariants §17) and ask: does this subsystem participate in any invariants not already cited? **Read the §0.3 category-prefix table for the authoritative list and §17 for the live total — do not rely on a hardcoded copy here** (it drifts every amendment; as of this writing ≈135 across ≈34 categories and rising). Core prefixes: LF (Local-First), ES (Event Sourcing), RF (Reliability/Fault Tolerance), CS (Compatibility/Stability), HO (Household Operability), PD (Privacy/Data Sovereignty), **TO (Transparency & Observability — note: `TO`, not `OB`)**, CE (Configuration & Extensibility), PR (Performance), SE (Security), AI, EI (Energy), MU (Multi-User), MN (Mesh/Network), GA (Governance — includes **INV-GA-02 "Invariant Identifiers Are Permanent"**, the identifier-non-reuse rule that also governs retired-AMD-number reuse), the M3 distribution families **BUS / PROJ / WRITER / SUB-ISO** (§19), and the per-amendment **`AMD-NN-INV`** families (§20+).

### Locked Technical Decisions (LTD-NN)

**How to apply:** LTDs are implementation constraints. They specify WHAT to use, often with exact configuration. Your job is to ensure every relevant LTD is followed precisely.

**The 19 LTDs at a glance — a LOSSY SUMMARY (pointer-not-copy applies): the register is AUTHORITATIVE, and a reviewer who bypasses this table for the register is doing it right** (the 2026-07-03 Doc-18 reviewer did exactly that; row 16 below carried a wrong gist for weeks — corrected 2026-07-04 from the register). Cite the register in work products; use this table for recall only:

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
| 16 | **Semantic Versioning 2.0.0 + URL-versioned REST API** (`/api/v1/…` = the API contract major, not the product version); additive-only within a major; **minimum ONE-major-version deprecation window** — the floor DP-18-A's six-release-cycle pledge builds on, never goes below | No removal/rename inside a major; deprecations carry the window; API-shape changes are additive (the REST/WS *stack* itself rides LTD-11/LTD-18) |
| 17 | **In-process compiled integrations, API boundary enforced at BUILD time; no dynamic loading** (no dynamic JARs, no classloader isolation, no external process management) — the dynamic seam is formally RESERVED (Doc 18 §4 row 1); activating it is a future LTD-17 amendment (Doc 18 OQ-2), never a silent change | Direct factory construction at the composition root; module-graph-assert + ArchUnit enforce the boundary. (The old "DECIDE-04" citation was a PHANTOM — resolves to nothing in `governance/`; caught at Doc-18 authoring, beat 61) |
| 18 | Web UI Technology — Preact SPA for Observability MVP, HTMX for Tier 2+ config UI | Preact for dashboard, HTMX reserved for configuration interfaces |
| 19 | Event payload serialization via `EventTypeRegistry` + `PersistenceJacksonModule` (extends LTD-08) | Registry-driven payload (de)serialization in the persistence layer; `JacksonWarmup` pre-warm; no `@JsonTypeInfo` on domain types (Jackson-isolation / ArchUnit Rule 10) |

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

**Gradle-scope lockstep.** `requires transitive X` in `module-info.java` MUST pair with `api(project(...))` in `build.gradle.kts`; plain `requires X` pairs with `implementation(...)`. If the two disagree, downstream modules fail to resolve `X` at compile time. And a `public` class in an **exported** package must not expose a type from a non-transitive `requires` (or a package-private type) on its API surface — that trips `-Xlint:exports` → `-Werror`. This pair has bitten three times (M2.9, M3.6e.1, M5-A); the coding-instruction format now requires an authoring check before embedding any `module-info`. Full pattern: `../../coder/references/java-patterns.md` (JPMS exports discipline).

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

## 5. Governance Finding Protocol

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

- File the finding in `../context/handoff/cross-agent-notes.md` as a `[DECISION-REQUESTED]` entry per PLAN §5b (template), tagged with `GOV_` prefix in the title (e.g., `DR-MM-NN — GOV_LTD03_reversal_criteria_met`). Escalate to Nick if blocking.
- If BLOCKING: stop current work and notify immediately. Do not work around a governance issue.
- If NOT blocking: continue current work but ensure the finding is filed before session end

---

## 6. Amendment Tracks — Full vs Lightweight (P4)

Not every amendment needs full per-AMD ceremony. Two tracks:

- **Lightweight block-amendment track** — trivial *additive* amendments (a single appended record field with a back-compat convenience ctor; a new constant on a non-persisted enum; an inert reservation) ride a **shared** review, a shared ratification pass, and shared mechanics (one watermark bump, one traceability pass, one disposition block for the set). An inert reservation MUST carry an explicit "inert until M{N}" note so it is not implemented prematurely or mistaken for live contract.
- **Full per-AMD track** — reserved for anything that touches a **persisted shape**, a **behavioral contract**, or introduces a **new invariant**. These get individual scrutiny and an independent DOCS-Project review.

DOCS-review depth follows the track: the lightweight block-track for the former; a full DOCS review for the latter (a constitutional-invariant narrowing — e.g. an INV-PD-* amendment — is always full). This keeps the gate that catches real defects (the M4 block review caught AMD-55's undetectable void-reauth and AMD-56's unimplementable trigger) while cutting ceremony on one-field/inert amendments.

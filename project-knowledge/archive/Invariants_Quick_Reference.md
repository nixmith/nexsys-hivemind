<!--
file: project-knowledge/Invariants_Quick_Reference.md
purpose: Token-efficient index of all 163 architecture invariants (47 identifier categories; ALWAYS re-derive the total from the §17 table, never propagate a stated count). Agents use this for constraint lookup; full text lives in homesynapse-core-docs/governance/Architecture_Invariants_v1.md for JIT reading when detail is needed.
audience: All (PM, Coder, Cowork)
update-cadence: per-phase (changes only via amendment process INV-GA-01)
state-type: reference
status: CURRENT
freshness-tier: COLD
last-verified: 2026-06-12 (post-ratification) — **163 invariants across 47 identifier categories: §42–§47 (AMD-88..93, +11) REGISTERED at the 2026-06-12 M7-block ratification; count regenerated from the §17 table.** _Prior:_ 2026-06-09 (152/41, M6 block; stale footer "133/32" corrected; the previously stated "135/34" was a copied-forward running count drifted −9 vs the table — see pm-handoff 2026-06-09. New this update: **§37–§41, +8 invariants** — AMD-66-INV-01/02, 67-INV-01/02, 68-INV-01, 70-INV-01, 71-INV-01/02, registered at the AMD-66..71 ratification; **AMD-69 DEFERRED, no invariant**). Codebase HEAD `6c6dd33`, watermark **AMD-87 (unchanged — reserved slots filled)**. Prior: 2026-06-07 `7f44bed` (M5 window, stated 135/34).
full-text-location: homesynapse-core-docs/governance/Architecture_Invariants_v1.md
-->

# Architecture Invariants — Quick Reference

**Total: 163 invariants across 47 identifier categories** (regenerated from the §17 table at the 2026-06-12 M7-block ratification — §42–§47, +11, registered for AMD-88..93; the 2026-06-09 M6 block added §37–§41, +8 → 152/41; the earlier stated "135/34" had drifted −9 below the table. ALWAYS re-derive the total from the §17 table, never propagate a stated number). (Since the last spine update: **§37–§41, +8 invariants** registered at the 2026-06-09 M6-config-block ratification — AMD-66 listener discipline, AMD-67 `(major,minor)` distinct surfaces, AMD-68 `setAll` atomicity, AMD-70 observability-only events + the **E70-1 type-residency rule**, AMD-71 traversal guard + one-level include; **AMD-69 DEFERRED** (Tier-2/OQ-15-3, no invariant, number reserved); **watermark UNCHANGED at AMD-87**. Prior update: §35–§36 in the M5 window — AMD-86-INV-01 + AMD-87-INV-01; INV-PD-03/INV-PD-07 amended by AMD-86; Doc 15 LOCKED.)
**Amendment process:** INV-GA-01. Requires written proposal, impact analysis, architecture owner approval, migration plan.
**Identifiers are permanent:** INV-GA-02. Retired IDs are never reused.

---

## §1 Local-First Operation (LF) — 5 invariants

| ID | Rule | MVP-Critical |
|---|---|---|
| INV-LF-01 | All core functionality operates without internet. Core = device control, automation, events, state, dashboard, history, scenes, config, health. | Yes |
| INV-LF-02 | Cloud enhances, never required. No core code path includes a network call that degrades core on failure. Module architecture enforces: core has no HTTP/WebSocket imports. | Yes |
| INV-LF-03 | Graceful WAN degradation — no error dialogs, no blocked queues, cloud features show "unavailable" not "error." | Yes |
| INV-LF-04 | No required cloud account for any core function. | Yes |
| INV-LF-05 | Convergent sync architecture — data model supports CRDT-compatible sync (per-entity sequences, commutative ops). MVP is single-instance but model must accommodate multi-instance. | Architecture only |

## §2 Event Sourcing Guarantees (ES) — 8 invariants

| ID | Rule | MVP-Critical |
|---|---|---|
| INV-ES-01 | Events are immutable. Append-only log. Removal only by retention policy past oldest checkpoint. | Yes |
| INV-ES-02 | All state derivable from event replay from checkpoint. No state exists without a recorded event. | Yes |
| INV-ES-03 | Per-entity monotonic sequence numbers. Cross-entity ordering via ULID timestamps + causal metadata, not global sequence. | Yes |
| INV-ES-04 | Write-ahead persistence. Events durable before delivery. Crash recovery replays persisted-but-undelivered. | Yes |
| INV-ES-05 | At-least-once delivery. Subscribers must be idempotent. System provides event ID + sequence for idempotency checks. | Yes |
| INV-ES-06 | Every state change explainable. "Why is this device in this state?" traceable to causal event chain. | Yes |
| INV-ES-07 | Event schema forward-compatible within major version. Open-world assumption (tolerate unknown fields). Breaking changes only at major boundaries. | Yes |
| INV-ES-08 | Event time (when it happened) vs ingest time (when bus accepted it) are distinct required fields. Automations evaluate event time. Retention uses event time. Log ordering uses ingest time. | Yes |

## §3 Reliability and Fault Tolerance (RF) — 6 invariants

| ID | Rule | MVP-Critical |
|---|---|---|
| INV-RF-01 | Integration isolation. Crash/hang/OOM in one integration cannot affect core, other integrations, or event bus. Isolation mechanism is an impl detail — API is topology-independent. | Yes |
| INV-RF-02 | Resource quotas for integrations (memory, CPU, event rate, FDs). Exceed → throttle/terminate, never degrade system. | Yes |
| INV-RF-03 | Startup independence. Failing integration does not block boot. Dashboard accessible regardless. | Yes |
| INV-RF-04 | Crash safety. Consistent state after unclean shutdown without user intervention. No manual repair, no DB rebuild. | Yes |
| INV-RF-05 | Bounded storage growth. Configurable retention with sensible defaults. SD card must survive years. | Yes |
| INV-RF-06 | Graceful degradation under partial failure. Total failure requires core event bus or persistence failure, not any single integration. | Yes |

## §4 Compatibility and Stability (CS) — 7 invariants

| ID | Rule | MVP-Critical |
|---|---|---|
| INV-CS-01 | Semantic Versioning 2.0.0 enforced. No breaking changes within major version. | Yes |
| INV-CS-02 | Entity identifiers stable across upgrades. System changes never alter entity IDs. | Yes |
| INV-CS-03 | Configuration schema backward-compatible within major version. New options have behavior-preserving defaults. | Yes |
| INV-CS-04 | Integration API versioned independently. Integration compiled against X.Y works on any core supporting X.Z (Z≥Y). | Yes |
| INV-CS-05 | Update safety: auto-snapshot before update, documented rollback, dry-run validation. | Yes |
| INV-CS-06 | Deprecation discipline: announce ≥1 major version ahead, migration path, runtime warnings, migration tooling. | Yes |
| INV-CS-07 | No forced hardware obsolescence. Prior major version gets security fixes for documented window. | Architecture only |

## §5 Household Operability (HO) — 5 invariants

| ID | Rule | MVP-Critical |
|---|---|---|
| INV-HO-01 | Physical control supremacy. Physical action always wins over automation. HomeSynapse failure never removes "dumb" functionality. | Yes |
| INV-HO-02 | Operable under degradation. Non-technical member can operate unaffected devices and understand errors. | Yes |
| INV-HO-03 | No debugging for daily operation. All daily ops via GUI. No logs, YAML, CLI for routine use. | Yes |
| INV-HO-04 | Self-explaining errors. Human-readable: what happened, what's affected, what to do. | Yes |
| INV-HO-05 | The Partner Test. Non-technical household member validates daily ops, error states, no internal terminology. Release gate. | Yes |

## §6 Privacy and Data Sovereignty (PD) — 8 invariants

| ID | Rule | MVP-Critical |
|---|---|---|
| INV-PD-01 | Zero telemetry by default. No dark patterns, no pre-checked boxes. Default install transmits zero bytes. | Yes |
| INV-PD-02 | Data residency user-controlled. All data local by default. Cloud opt-in with user control over what/where/how long. | Yes |
| INV-PD-03 | Encrypted storage for sensitive data (credentials, keys, tokens, PII). AES-256-GCM. User-owned keys. | Yes |
| INV-PD-04 | Transparent data boundaries. Machine-readable manifest of what data exists, what can leave, which services each integration talks to. | Yes |
| INV-PD-05 | Consent is granular, informed, revocable. States what data, to which service, for what purpose, how long retained. | Yes |
| INV-PD-06 | Offline integrity. Write operations transactional and crash-safe. Power loss is normal, not exceptional. | Yes |
| INV-PD-07 | Crypto-shredding for sensitive data lifecycle. Per-scope keys. Destroy key = irrecoverable. Reconciles immutable log with GDPR. Applies to: behavioral, energy, identity/presence data. MVP: infrastructure + ≥1 category. | Infra only |
| INV-PD-08 | Tamper-evident system integrity. Crypto integrity chain for firmware, config changes, integration provenance. Extensible to automation auditing (§16.5). | Infra only |

## §7 Transparency and Observability (TO) — 4 invariants

| ID | Rule | MVP-Critical |
|---|---|---|
| INV-TO-01 | System behavior observable: live event stream, active automations, integration status, causal chains, performance metrics. | Yes |
| INV-TO-02 | Automation determinism. Identical events + config = identical outcomes. Traceable: trigger, conditions, actions, results. | Yes |
| INV-TO-03 | No hidden state. All behavior-influencing state inspectable. No hidden caches or implicit timing-derived state. | Yes |
| INV-TO-04 | Structured, queryable logs with correlation IDs. "Why did lights turn on at 3 AM?" answerable via UI. | Yes |

## §8 Configuration and Extensibility (CE) — 6 invariants

| ID | Rule | MVP-Critical |
|---|---|---|
| INV-CE-01 | Canonical human-readable config. Single YAML source of truth. UI reads/writes same representation. No dual storage. | Yes |
| INV-CE-02 | Zero-configuration first run. Sensible defaults. Install → start → dashboard → add devices. | Yes |
| INV-CE-03 | Config schema documented, versioned, validated at startup. Every option typed with default, range, and behavior. | Yes |
| INV-CE-04 | Protocol agnosticism in device model. Same "turn on light" interface for Zigbee, Z-Wave, Matter, Wi-Fi. | Yes |
| INV-CE-05 | Extension model with stability guarantees. Isolated execution, resource quotas, independent versioning, graceful degradation. | Yes |
| INV-CE-06 | Migration tooling with schema evolution. Idempotent, reversible, preview-able. Users never manually rewrite config. | Yes |

## §9 Performance and Resource Discipline (PR) — 4 invariants

| ID | Rule | MVP-Critical |
|---|---|---|
| INV-PR-01 | Constrained hardware is primary design target. Pi 4 (4 GB) = validation floor. "Upgrade hardware" is never the answer. | Yes |
| INV-PR-02 | Quantitative performance targets (constitutional, on Pi 4): startup <10s, device command <300ms, automation p99 <100ms, REST p99 <50ms, dashboard <500ms, memory <512MB. Operational budgets in subsystem docs. | Yes |
| INV-PR-03 | Resource usage bounded and predictable. No unbounded growth over time. | Yes |
| INV-PR-04 | Architecture accommodates 1,000 devices without redesign. MVP need not achieve, must not prevent. | Architecture only |

## §10 Security (SE) — 6 invariants

| ID | Rule | MVP-Critical |
|---|---|---|
| INV-SE-01 | No default credentials. First-run requires user-created credentials. | Yes |
| INV-SE-02 | Authentication required for all network interfaces. No "local network trust" exception. | Yes |
| INV-SE-03 | Secrets encrypted at rest. AES-256-GCM. Never plaintext in config, DB, or logs. | Yes |
| INV-SE-04 | Least privilege for integrations. Light controller can't access locks or cameras. Declared in manifest, enforced at runtime. | Yes |
| INV-SE-05 | Remote access (optional) is end-to-end encrypted. NexSys relay cannot see plaintext. | Architecture only |
| INV-SE-06 | Security updates deliverable without feature churn. Foundation for future LTS channel. | Architecture only |

## §11 AI and Intelligence (AI) — 5 invariants

| ID | Rule | MVP-Critical |
|---|---|---|
| INV-AI-01 | AI is enhancement, never foundation. Disable all AI → full core capability. | Yes |
| INV-AI-02 | AI requires explicit consent via INV-PD-05 framework. | Yes |
| INV-AI-03 | AI decisions explainable to non-experts. "Based on your pattern of X, this would Y" minimum standard. | Yes |
| INV-AI-04 | Local AI capability. On-device inference for Pi-class: LightGBM (0.4–1.2ms), TinyLSTM (3–7ms), ONNX. [SCALES] to cloud/NPU at higher tiers. | Architecture only |
| INV-AI-05 | On-device behavior modeling. Interpretable, correctable, deletable. Training data never leaves device without federated learning consent. | Architecture only |

## §12 Energy Intelligence (EI) — 5 invariants

| ID | Rule | MVP-Critical |
|---|---|---|
| INV-EI-01 | Energy as first-class domain. Meters, inverters, batteries, EV chargers, controllable loads have same model fidelity as lighting/climate. MVP: energy entity types and event categories in model. | Model only |
| INV-EI-02 | Grid-interactive by design. OpenADR 3.0 VEN role. Automation engine evaluates grid signals locally. MVP: grid signal event types + time-based triggers. | Model only |
| INV-EI-03 | Carbon-aware scheduling. Shift deferrable loads to low-carbon periods within user constraints. MVP: time-window constraints + external data source inputs in automation. | Model only |
| INV-EI-04 | Energy data sovereignty. Energy data governed by §6 privacy invariants + per-program consent for grid/DR sharing. | Architecture only |
| INV-EI-05 | Hardware-agnostic energy metering. Switching inverter/battery vendor doesn't lose history or break automations. | Architecture only |

## §13 Multi-User Identity and Presence (MU) — 5 invariants

| ID | Rule | MVP-Critical |
|---|---|---|
| INV-MU-01 | Identity-aware device model. Per-user context for behavior, visibility, controllability. Event envelope has optional user identity field (populated/causal-ref/null). MVP: identity field in envelope + user-identity conditions in automation. | Model only |
| INV-MU-02 | Spatial presence as core primitive. Room/zone-level presence is first-class state. BLE/UWB/mmWave layered model. MVP: presence event types and state representations. | Model only |
| INV-MU-03 | Preference arbitration framework. ACRA/MeCRA/HyCRA modes. Transparent, inspectable rules. MVP: multi-condition evaluation with user identity. | Architecture only |
| INV-MU-04 | Household role model. Admin/adult/child/guest with per-user per-device RBAC. MVP: admin + member roles. | Architecture only |
| INV-MU-05 | Graceful identity degradation. Uncertain → most permissive common preference. Unknown → last known state. Offline → all-users-present fallback. Never locks anyone out. | Architecture only |

## §14 Mesh and Network Intelligence (MN) — 4 invariants

| ID | Rule | MVP-Critical |
|---|---|---|
| INV-MN-01 | Protocol-agnostic network telemetry. Unified schema across Zigbee/Thread/Wi-Fi/Z-Wave. MVP: Zigbee RSSI/LQI/route in event pipeline. | Yes (Zigbee) |
| INV-MN-02 | Mesh health as observable state. First-class entity. Per-device signal, per-link reliability, topology, aggregate health. Surfaced in dashboard. | Yes |
| INV-MN-03 | Predictive network diagnostics. Detect degradation trends before failure. MVP: store telemetry with sufficient granularity for future trend analysis. | Data foundation |
| INV-MN-04 | Battery-aware network optimization. Track energy consumption as function of network behavior. Surface elevated overhead as diagnostic. | Data foundation |

## §15 Governance and Amendment (GA) — 3 invariants

| ID | Rule | MVP-Critical |
|---|---|---|
| INV-GA-01 | Invariant stability. Amendment requires written proposal, impact analysis, owner approval, migration plan. Convenience/schedule/competitive parity are not sufficient reasons. | Process |
| INV-GA-02 | Identifiers are permanent. Retired IDs marked, never reused. | Process |
| INV-GA-03 | Compliance verified in design review. Subsystem designs must demonstrate invariant compliance. | Process |

## §19 Event Distribution, Projection & Subscriber Lifecycle — 15 invariants

Added by AMD-41/42/43 (applied 2026-05-16). Four sub-categories:

### Event Bus and Distribution (BUS) — 3

| ID | Rule | Source |
|---|---|---|
| INV-BUS-01 | Exactly-once delivery per subscriber (normal operation). Crash recovery bounded by checkpoint position. | AMD-42 |
| INV-BUS-02 | Publish is non-blocking on backpressure. No semaphores, no depth-gated locks. Natural backpressure from single-writer. ArchUnit rule enforces. | AMD-43 |
| INV-BUS-03 | Subscriber isolation. Failure in A cannot affect B's mode, queue, connection, DLQ, or delivery. Implemented by INV-SUB-ISO-01..06. | AMD-42 |

### State Projection (PROJ) — 3

| ID | Rule | Source |
|---|---|---|
| INV-PROJ-01 | Projection determinism. Same events + same replay order = same state. No wall-clock, no RNG, no external state. Clock via injected `java.time.Clock`. **Elevated by AMD-50-INV-03: the derivation rule is a pure function of `(priorState, envelope)` — `DerivationContext` carries NO clock (AMD-50 §2.4).** | AMD-41 |
| INV-PROJ-04 | Checkpoint-position monotonicity. Strictly non-decreasing. Rewind only on operator-initiated reconciliation (projectionVersion mismatch). | AMD-41 |
| INV-PROJ-NEW-01 | Self-produced event isolation. `SelfProducedFilter` (60s TTL, lazy eviction) prevents re-derivation. Bypassed during REPLAY/TRANSITION. Defence-in-depth: `stateVersion` comparison. | AMD-41 |

### Single-Writer Discipline (WRITER) — 1

| ID | Rule | Source |
|---|---|---|
| INV-WRITER-01 | All SQLite writes through single bounded platform-thread executor (WriteCoordinator). One thread holds writer position at any instant. Foundation for contiguous globalPosition + INV-BUS-02 backpressure. | AMD-26 elevated |

### Subscriber Isolation (SUB-ISO) — 6

| ID | Rule | Source |
|---|---|---|
| INV-SUB-ISO-01 | One virtual thread per subscriber (`hs-sub-<subscriberId>`). No sharing. | AMD-42 §3.4.4 |
| INV-SUB-ISO-02 | One dedicated SQLite read connection per subscriber. No sharing at any instant. | AMD-42 §3.4.4 |
| INV-SUB-ISO-03 | One DLQ instance per subscriber. Per-subscriber rows in `subscriber_dead_letters`. Ring cap 1024 per subscriber. | AMD-42 §3.4.4 |
| INV-SUB-ISO-04 | One mode AtomicReference per subscriber (COLD/REPLAY/TRANSITION/LIVE/SUSPENDED). CAS transitions. | AMD-42 §3.4.4 |
| INV-SUB-ISO-05 | One ReplayWindowQueue per subscriber (bounded; default 10,000, configurable via EventBusConfig). Created on REPLAY, drained in TRANSITION, GC'd after LIVE. | AMD-42 §3.4.4 |
| INV-SUB-ISO-06 | One SelfProducedFilter per derivation-producing subscriber. Non-producing subscribers don't instantiate. | AMD-42 §3.4.4 |

## §20 Device-Model Attribute-Value Expansion (AMD-47) — 5 invariants

Added by AMD-47 (RATIFIED 2026-05-30); **IMPLEMENTED in M4.B3 (`60b4185`)** — the 8-variant `AttributeValue` `permits` clause is live in source. Amendment-scoped (`AMD-47-INV-NN`); canonical text in Architecture_Invariants_v1.md §20.

| ID | Rule | Source |
|---|---|---|
| AMD-47-INV-01 | **Sealing remains total.** `AttributeValue` is 8 variants (`BooleanValue`/`IntValue`/`FloatValue`/`StringValue`/`EnumValue` + `QuantityValue`/`ArrayValue`/`DegradedAttributeValue`); exhaustive handling, no silent fallback for a future permit. Preserves the Doc 02 §8.2 sealed-exhaustiveness contract. | AMD-47 |
| AMD-47-INV-02 | **Upcaster-before-derivation ordering (both paths).** Value reconstruction / `AttributeValueUpcaster` runs before `DerivationRule.evaluate()` on **both** `onEvent` and `processBatch` (the M4.0a D-1 / AMD-50 gate-every-path discipline, extended to the value layer). | AMD-47 |
| AMD-47-INV-03 | **`QuantityValue` normalization determinism.** Canonicalises `(value, unit)` to the dimension's canonical unit **at construction** via a pure, hand-rolled, table-driven conversion (fail-closed; no JSR-385 — REC-93). Bit-deterministic; the comparator does zero unit work. | AMD-47 |
| AMD-47-INV-04 | **`DegradedAttributeValue` non-declarable and lossless.** Never enters canonical state under strict mode; `AttributeSchema` rejects `type == DEGRADED` at construction; preserves the raw form + failure reason for forensics (mirrors `DegradedEvent`). | AMD-47 |
| AMD-47-INV-05 | **`ArrayValue` full-replacement.** List-valued attributes replace wholesale — no element-delta/patch — so a bounded-window advancer reconstructs from a single latest event. | AMD-47 |

## §21 State-Store Typed Change-Detection Comparator (AMD-51) — 5 invariants

Added by AMD-51 (RATIFIED 2026-05-30); **IMPLEMENTED in M4.0b-3 (`98f705b`)**; **on-disk amendment watermark = AMD-51**. Amendment-scoped (`AMD-51-INV-NN`); canonical text in Architecture_Invariants_v1.md §21.

| ID | Rule | Source |
|---|---|---|
| AMD-51-INV-01 | **Typed total comparison (exhaustive, no `default`).** Change detection is an exhaustive `switch` over the 8-variant sealed `AttributeValue` with **no `default` arm** — a future 9th permit MUST break compilation. Per-variant semantics: exact for Boolean/Int/Enum/String; total-form epsilon for Float; canonical-magnitude epsilon + canonical-unit dimension check for Quantity; size-then-order-sensitive deep compare for Array; §2.4b rule for Degraded. (D-01 is event-type-scoped, so an `AttributeValue` exhaustive switch is permitted.) | AMD-51 |
| AMD-51-INV-02 | **Float/Quantity epsilon totality (pinned total form).** `changed ⟺ |a−b| > max(absEps, relEps·max(|a|,|b|))`, defaults `absEps = relEps = 1e-9`, with full IEEE-754 totality (`NaN`↔number = changed, `NaN`↔`NaN` = unchanged, `−0.0`/`+0.0` canonicalised, same-sign `Inf` = unchanged, opposite-sign or finite↔`Inf` = changed; `Inf−Inf` handled before the arithmetic). A correctness (FP-noise) epsilon carried in `ComparisonPolicy`, not a deadband; deterministic, no clock/I/O/randomness. | AMD-51 |
| AMD-51-INV-03 | **Degraded change-detection semantics.** Inbound `DegradedAttributeValue` ⇒ never emit; prior Degraded + valid inbound ⇒ emit (recovery); two Degraded ⇒ unchanged. HA-mirrored; consistent with AMD-47-INV-04 (Degraded never in canonical state). | AMD-51 |
| AMD-51-INV-04 | **Comparator placement + gateway.** External `AttributeValueComparator` in `com.homesynapse.state` carrying a `ComparisonPolicy` — NOT a method on the device-model `AttributeValue` (keeps projection/epsilon policy out of the data layer). Package-private impl behind a public static factory `structural()` (DEC-M3-16 gateway). | AMD-51 |
| AMD-51-INV-05 | **Symmetric reconstruction; 2→3 rides AMD-50 unchanged.** BOTH operands reconstructed to the schema-declared variant by one parse keyed by `AttributeSchema.type` — the materialized prior is always a `StringValue` (or `null`) and is reconstructed too. Distinct from the `AttributeValueUpcaster` stored-value-migration SPI (left unchanged). The typed compare rides a `projectionVersion` **2→3** bump on AMD-50's reconciliation-backfill unchanged; reconstruction is identical on LIVE and the 2→3 backfill. **§2.6 erratum (2026-05-31): no schema for the key ⇒ `StringValue` string-compare fallback (NOT Degraded/no-emit) — preserves M4.0b-2 behaviour for unschematized keys.** | AMD-51 |

## §22 Typed `StateChangedEvent` Payload / Serializer / Replay (AMD-52) — 7 invariants

RATIFIED 2026-05-31; IMPLEMENTED in M4.0b-4a/4b (`971cfa1`/`72596cb`); watermark raised AMD-51→AMD-52. Canonical text §22.

| ID | Rule |
|---|---|
| AMD-52-INV-01 | Typed payload + per-event `schema_version` (1→2) discriminator; **no `events`/`view_checkpoints` row migration**. |
| AMD-52-INV-02 | Custom non-reflective, Jackson-isolated `{"t","v"[,"u"]}` codec, exhaustive **no-`default`** over the 8 variants; no `@JsonTypeInfo`. |
| AMD-52-INV-03 | Bit-anchored float identity (`Double.doubleToLongBits` after AMD-51 canonicalization); round-trippable text, never byte-frozen; `chain_hash` stays inert. |
| AMD-52-INV-04 | JSON-valid non-finite sentinels; `ALLOW_NON_NUMERIC_NUMBERS` disabled; no bare `NaN`/`Inf` tokens. |
| AMD-52-INV-05 | Path A (re-derive from immutable `state_reported` log) authoritative; Path B legacy `schema_version=1` → defined `DegradedEvent`; events never mutated (append-only). |
| AMD-52-INV-06 | Typed `CheckpointSerializer` envelope (S2), same `view_checkpoints.data` BLOB; ALWAYS null round-trip preserved (`HashMap.put`, never `Map.copyOf`). |
| AMD-52-INV-07 | `projectionVersion` 3→4 rides AMD-50's frozen reconciliation-backfill unchanged. |

## §23 Timestamp-Model Unifier — Event-Time Activity Timestamps (AMD-53) — 2 invariants

RATIFIED 2026-05-31; IMPLEMENTED in M4.0b-5 (`c99b425`); watermark AMD-52→AMD-53. Canonical text §23.

| ID | Rule |
|---|---|
| AMD-53-INV-01 | `lastChanged`/`lastUpdated`/`lastReported` sourced from `eventTime ?? ingestTime` in **every** `applyToState` branch + entity-adoption seeding (extends AMD-50-INV-03 to materialization). `projectionVersion` 4→5 heals legacy wall-clock stamps. |
| AMD-53-INV-02 | `staleAfter`/`stale` are the **only** real-time-clock fields on `EntityState` and are explicitly carved out (guards against "no wall-clock anywhere" misreads). |

## §24–§34 Workstream C Integration Block (AMD-54..64) — 29 invariants

Registered together at the AMD-54..64 block ratification (2026-06-05, single DOCS-Project review return + Nick arbitrations A1–A5/E3/E7/E8); watermark AMD-53→AMD-64. Contracts frozen at **M4.C** (`8ef9e9f`); supervisor behavior lands at **M9**. Canonical text §24–§34.

| ID | § | Rule (short) |
|---|---|---|
| AMD-54-INV-01 | §24 | Two distinct compatibility surfaces — descriptor schema vs config schema. |
| AMD-54-INV-02 | §24 | Major version triggers migration, minor never. |
| AMD-55-INV-01 | §25 | All four lifecycle hooks `default`; pre-AMD-55 adapters unchanged. |
| AMD-55-INV-02 | §25 | Sequential hook execution on the adapter thread. |
| AMD-55-INV-03 | §25 | `migrate` before `initialize`; migrate-failure → FAILED transition (emits no event). |
| AMD-55-INV-04 | §25 | `REJECTED` config apply never leaves the rejected config active (prior config = safe recovery). |
| AMD-56-INV-01 | §26 | `AUTH_FAILED` never routes to transient backoff. |
| AMD-56-INV-02 | §26 | `ExceptionClassification` append-only, order frozen (`AUTH_FAILED` last). |
| AMD-56-INV-03 | §26 | `PermanentIntegrationException` ctors append-only; well-known codes documented. |
| AMD-57-INV-01 | §27 | `HealthDetail` never null; `NONE` is the explicit no-cause value. |
| AMD-57-INV-02 | §27 | `HealthDetail` append-only; 1:1 transition-trigger mapping. |
| AMD-58-INV-01 | §28 | Three-way registration lockstep (enum permit + event-type string + manifest), no partial registration. |
| AMD-58-INV-02 | §28 | Persisted event-type strings immutable; dot-namespace for new; legacy five frozen. |
| AMD-58-INV-03 | §28 | The five new lifecycle permits are observability-only. |
| AMD-59-INV-01 | §29 | Capability events are the only post-adoption mutation path; no capability table. |
| AMD-59-INV-02 | §29 | `CapabilityAdded` carries the complete `CapabilityInstance` (replay self-sufficiency). |
| AMD-59-INV-03 | §29 | No `CapabilityId` wrapper; permit class + string identity. |
| AMD-59-INV-04 | §29 | `EntityId` stable across capability add/remove. |
| AMD-59-INV-05 | §29 | `CapabilityPublisher` integration-scoped (LTD-17). |
| AMD-59-INV-06 | §29 | `CapabilityRemovalReason` descriptive-only, never behavioral. |
| AMD-60-INV-01 | §30 | Context grows only by service-family aggregators (NQ-1 doctrine). |
| AMD-60-INV-02 | §30 | `SecurityServices` nullable, `RequiredService.SECURITY`-gated; non-null inside. |
| AMD-60-INV-03 | §30 | `rotate(Map)` integration-scoped, atomic across entries, durable-before-return. |
| AMD-61-INV-01 | §31 | Soft dependency never blocks startup; hard always does. |
| AMD-61-INV-02 | §31 | `dependsOn ∩ softDependencies = ∅` at construction. |
| AMD-62-INV-01 | §32 | Retry schedule is a pure function of `BackoffParameters` + attempt count. |
| AMD-62-INV-02 | §32 | Retry backoff and recovery probing are distinct mechanisms. |
| AMD-63-INV-01 | §33 | `IsolationLevel.RESERVED_SUBPROCESS` rejected until activated by amendment (inert reservation). |
| AMD-64-INV-01 | §34 | Null planned-restart-timeout ⇒ global §3.14 default; present value positive and fully replacing. |

## §35–§36 M5 Window — Cryptographic Architecture (AMD-86 + AMD-87) — 2 new invariants + 2 amended privacy invariants

Registered at the 2026-06-07 M5-window crypto+codec ratification (Doc 15 Cryptographic Architecture LOCKED); watermark AMD-64→**AMD-87**. **These are the load-bearing privacy/crypto invariants for M6 (Configuration + secrets/crypto) and the post-MVP data-value/institutional products.**

| ID | § | Rule (short) |
|---|---|---|
| **INV-PD-03 (amended by AMD-86)** | §6 | Sensitive-PII categories encrypted at rest under **per-scope DEKs** (application-level, per-category — **never** whole-DB, so per-category crypto-shred stays possible). **PARTIAL at MVP:** at-rest encryption — yes; the **"user-owned keys"** property + media-theft resistance — **Tier-2** (the machine-local key shares the medium; protects key-excluding copies + less-privileged reads, **not** theft of the storage medium). |
| **INV-PD-07 (amended by AMD-86)** | §6 | MVP = per-scope key-management infrastructure + scope-category definitions + sensitive-PII **written encrypted-at-rest** (preserving future shreddability on the immutable log). **Operational crypto-shredding = post-MVP** (first cloud/institutional data-sharing consumer). Deletion-via-key-destruction design intent unchanged. |
| **AMD-86-INV-01** | §35 | *Encrypt-on-write is irreversible; the shred operation is deferrable.* A category is crypto-shreddable only if it was written encrypted-per-scope — so the encrypt-on-write decision for sensitive-PII is made at MVP, and the operation that consumes those keys may land later. |
| **AMD-87-INV-01** | §36 | Every `Expectation` permit round-trips losslessly through `EventPayloadCodec`; `WithinTolerance`'s two doubles use the AMD-52 bit-anchored-float / non-finite-sentinel determinism (a tolerance of `0.1` or a `NaN` survives encode→decode bit-identically). |

**Also Locked: Doc 15 (Cryptographic Architecture)** — owns the SHA-256 hash chain (INV-PD-08), at-rest envelope encryption, the per-scope key-management infrastructure, the crypto-shredding design (operation post-MVP), and Ed25519 package signing. **Open Risk OR-M6-NONCE [BLOCKING-for-M6-impl]:** the per-scope GCM counter-nonce must be durable + strictly monotonic across crash AND restore, or (key,nonce) reuse breaks AES-GCM.

## §37–§41 M6 Config Block (AMD-66..71) — 8 new invariants

Registered at the 2026-06-09 M6-block ratification (AMD-66/67/68/70/71 RATIFIED; **AMD-69 DEFERRED** — Tier-2/OQ-15-3, no invariant, number reserved); **watermark UNCHANGED at AMD-87** (reserved-below-watermark slots filled — ratification does not raise the ceiling). Implementing WUs: M6.1 (66/67/70/71 load path), M6.2 (68), M6.4 (66 under swap; 70 `section_reloaded`).

| ID | § | Rule (short) |
|---|---|---|
| **AMD-66-INV-01** | §37 | A `ConfigurationChangeListener` classifies a section change and is forbidden from mutating the `ConfigModel` (INV-CE-01 — the YAML file is the sole source of truth). |
| **AMD-66-INV-02** | §37 | Classification is synchronous and completes before the reload observability event is published (Doc 06 §3.3 ordering). |
| **AMD-67-INV-01** | §38 | The system config-document schema `(configSchemaMajor, configSchemaMinor)` and the adapter-config schema (AMD-54) are distinct compatibility surfaces; no code path derives one from the other. |
| **AMD-67-INV-02** | §38 | A minor-only config-document mismatch never triggers migration; a major mismatch always does (AMD-54-INV-02 adopted for the system-config surface). |
| **AMD-68-INV-01** | §39 | `SecretStore.setAll(Map)` is all-or-nothing and durable-before-return — the store-layer guarantee beneath AMD-60-INV-03; a multi-secret set can never be torn by a crash. |
| **AMD-70-INV-01** | §40 | `config.validation_completed` and `config.section_reloaded` are observability-only — no state projection consumes them; the config file remains the sole source of truth (INV-CE-01). |
| **AMD-71-INV-01** | §41 | The configuration loader reads only files contained within `PlatformPaths.configDir()` after canonicalization; an `!include` escaping the config tree is rejected fail-closed. |
| **AMD-71-INV-02** | §41 | `!include` is one level deep; a nested include is a structural FATAL error. |

**Standing JPMS lesson (E70-1 type-residency rule — now in the P2 consumer/pin survey + pm-/coder-lessons):** any new type in a base module (`event-model`/`value-model`/`platform-api`) — especially an event record — references only that module, a leaf, or `java.base`; a higher-layer domain type in an event-resident record forces a JPMS cycle (the AMD-52 `event↔device` / AMD-70 `event→config` class). Config types are *consumed* to derive flattened components, never *referenced*.

### Amendment-scoped invariants NOT counted in the §17 total (live in their amendment files)

AMD-45 and AMD-50 carry contract-level `*-INV-NN` invariants that are **not** registered as numbered §-categories in Architecture_Invariants_v1.md's §17 count — their canonical text lives in the amendment files (+ `core/state-store/MODULE_CONTEXT.md`). They are load-bearing for M4 Workstream A:

| ID | Rule | Applied |
|---|---|---|
| AMD-45-INV-01 | **Atomic checkpoint coupling.** The bus subscriber checkpoint and the projection view checkpoint for the `state_projection` subscriber MUST be written in the same SQLite transaction — neither advances without the other (all three bus checkpoint writers gated: LIVE + both REPLAY). | M4.0a `a441fdf` |
| AMD-50-INV-01 | **Cursor determinism.** For a fixed log + fixed `projectionVersion`, every entity's `stateVersion` is identical across all rebuild paths; backfill drafts carry no increment. (Refines INV-PROJ-04.) | M4.0b-2 `7610296` |
| AMD-50-INV-02 | **Single-application provenance.** A reconciliation-scoped re-derived `state_changed` draft is applied to in-memory state **only** while the §2.2 provenance gate is active, and is **never** published or written to the log. (One-shot — a second restart at the matching version does not run the backfill.) | M4.0b-2 `7610296` |
| AMD-50-INV-03 | **Rule rebuild determinism.** The production `DerivationRule` is a pure function of `(priorState, envelope)` — no clock (`DerivationContext` carries none, §2.4), no registry, no I/O, no randomness. (Elevates INV-PROJ-01; the schema resolver is injected immutable config, not a live registry read.) | M4.0b-2 `7610296` |
| AMD-50-INV-04 | **Gate–checkpoint coherence.** A replay from `position = 0` occurs **only** under an active reconciliation gate; the gate is inactive only when resuming from a checkpoint whose persisted version equals the code version. | M4.0b-2 `7610296` |

---

## §42–§47 M7 Automation Block (AMD-88..93) — 11 invariants (REGISTERED 2026-06-12)

**Registered at the 2026-06-12 block ratification** (AMD-88 §42 · AMD-89 §43 · AMD-90 §44 · AMD-91 §45 · AMD-92 §46 · AMD-93 §47). Full text in `Architecture_Invariants_v1.md`; AMD-91-INV-01 additionally pins the reconstruction source (event log or in-process `RunContext`, never the windowed §4.5 map — the E91-1 fold).

| Candidate | Summary |
|---|---|
| AMD-88-INV-01 | Tier-2→Tier-1 promotion = field-addition only; never adds/removes/renames a sealed permit (switch-shape stability) |
| AMD-88-INV-02 | Every Tier-1 trigger carries a reload-stable `triggerId`; user-facing surfaces reference triggers by id, never raw index |
| AMD-89-INV-01 | Group-resolving selectors resolve PRIMARY-role entities only unless `includedRoles` explicitly opts in; single-entity selectors never role-filtered |
| AMD-90-INV-01 | Confirmation is per-action policy; never blocks Run completion; NO engine-level retry at any policy value |
| AMD-90-INV-02 | Every iteration construct is hard-bounded (`maxIterations`); unbounded loops unrepresentable |
| AMD-91-INV-01 | Cascade-cycle suppression is a deterministic function of chain + config — no windowed/evictable/restart-sensitive state in suppression decisions |
| AMD-91-INV-02 | `RunCausalChain` never crosses the event boundary unflattened |
| AMD-92-INV-01 | Event records never reference automation-resident types; run/status identifiers cross as flattened `Ulid`/`String` only (the E70-1 rule) |
| AMD-92-INV-02 | No automation event type reaches a production publish site before appearing in every survey-enumerated manifest/pin for its slice |
| AMD-93-INV-01 | Definition migrations: forward-only, idempotent, backup-first, never destructive — unconvertible definitions excluded-and-reported, not modified |
| AMD-93-INV-02 | Every loaded definition has fully-resolvable references at load time (post-tombstone-redirect); dangling references never enter the registry |

---

## §16 Long-Term Ecosystem Direction (Directional, not formal invariants)

These are directional commitments that guide architectural decisions. Unlike invariants, they may be revised. Reference only when making forward-looking architecture choices.

| § | Direction | Foundation Invariants |
|---|---|---|
| 16.1 | Energy as self-funding value proposition. $3.99–7.99/mo subscription, 2–8× ROI. | EI-01, EI-02, EI-03 |
| 16.2 | Multi-user identity as killer feature. First platform with identity-aware presence + preference arbitration. | MU-01 through MU-05 |
| 16.3 | Unified RF health dashboard. First consumer 802.15.4 diagnostic tool. | MN-01 through MN-04, TO-01 |
| 16.4 | On-device intelligence pipeline. Nest-class intelligence, no cloud. Pi 5 runs full ML at <3W. | AI-01 through AI-05, PR-02 |
| 16.5 | Privacy-preserving cloud + verifiable transparency. ZK backup, tamper-evident automation auditing. | PD-07, PD-08 |
| 16.6 | Multi-protocol convergence. Matter/Thread, Z-Wave, Wi-Fi via stable extension model. | CE-04, CE-05 |
| 16.7 | Multi-instance operation. Small Peer / Big Peer. | LF-05 |
| 16.8 | LTS release channel. Security fixes without feature churn. | SE-06 |
| 16.9 | Community ecosystem. "Works With HomeSynapse" certification ($1K–10K/device). | CE-05, CS-04 |
| 16.10 | Ambient interfaces. Sound event detection, ultrasonic sensing, spatial computing (2028+). | AI-02, PD-01 |
| 16.11 | Formal verification of automation rules. TLA+ embedded for safety/liveness/conflict-freedom. | TO-02 |

---

***163 invariants across 47 identifier categories**, verified against Architecture_Invariants_v1.md §17 Invariant Index — count REGENERATED from the table 2026-06-12 at the M7-block registration (§42–§47 AMD-88..93, +11; prior regeneration 2026-06-09 at 152/41; the historical "133/32"/"135/34" were copied-forward under-counts — always re-derive from §17, never propagate a stated total). AMD-45-INV-01 and AMD-50-INV-01..04 remain amendment-scoped and are not counted in the §17 total (see the note above §16). For full invariant text including rationale, test criteria, MVP scope, and [SCALES] annotations, read the full document at homesynapse-core-docs/governance/Architecture_Invariants_v1.md.*

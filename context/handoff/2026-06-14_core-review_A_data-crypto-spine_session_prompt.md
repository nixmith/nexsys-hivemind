<!--
file: context/handoff/2026-06-14_core-review_A_data-crypto-spine_session_prompt.md
purpose: Review Session A of the two-part homesynapse-core review — the data, storage & crypto spine (modules 1–8, foundation-up). Build the model, hunt defects (esp. event-sourcing correctness + the end-to-end M6.3 at-rest crypto), surface research. Feeds the converge session.
audience: PM (Cowork, fresh conversation), Nick
state-type: session prompt
status: READY (commit + dispatch as a fresh Cowork conversation; parallel-capable with Session B)
-->

# Review Session A — Data, Storage & Crypto Spine

**Read `context/handoff/2026-06-14_core-review_FRAMEWORK.md` in full first** — it carries the stance, the calibrated-honesty rule (VERIFIED vs HYPOTHESIS + the Claude-Code-verification handoff), Step 0, the per-module checklist, the defect taxonomy, the finding format, and the guardrails. This prompt carries only your scope and focus.

**Your half of the system:** the event-sourced foundation everything else rests on, plus the just-shipped M6.3 at-rest encryption — reviewed **end-to-end** here because it spans `persistence` (the `PayloadCipher` seam + write/read path) and `configuration` (the `ScopeKeyManager` key management), and both are in your scope. **Session A's defining question: is the foundation correct, and is the M6.3 crypto sound end-to-end?**

## Scope — review foundation-up, in this order

| # | Module (JPMS name) | Focus | Priority |
|---|---|---|---|
| 1 | `platform/platform-api` (`com.homesynapse.platform`) | Typed-ULID identity, `UlidFactory` (hand-rolled, VT-safe via ReentrantLock), `PlatformPaths`. The ULID + identity contracts underpin every store and event — get them exactly right. | medium |
| 2 | `core/value-model` (`com.homesynapse.value`) | The `AttributeValue` leaf (relocated to break the AMD-52 event↔device cycle); float-bit-identity discipline; the sealed hierarchy; serde. | medium |
| 3 | `core/event-model` (`com.homesynapse.event`) | The heart: `DomainEvent`/`EventEnvelope`/`EventDraft`, `EventStore`/`EventPublisher`, `EventCategory`/`EventTypes`, causal context (`correlation_id`/`causation_id`), `SequenceConflictException`. The event-sourcing contracts originate here. | **DEEP** |
| 4 | `core/event-bus` (`com.homesynapse.event.bus`) | Subscriber lifecycle/isolation, checkpoints, backpressure, the DLQ, REPLAY→TRANSITION→LIVE. Concurrency-dense — INV-SUB-ISO / INV-BUS. | **DEEP** |
| 5 | `core/device-model` (`com.homesynapse.device`) | Devices/entities/capabilities, `Expectation` + its 4 permits, `EntityRole`. The capability/command surfaces M7 will act on. | medium |
| 6 | `core/persistence` (`com.homesynapse.persistence`) | SQLite WAL store, `MigrationRunner` (incl. the confirmed `splitSqlStatements` finding + V005), the write coordinator, checkpoint stores, the codecs, and the **M6.3 at-rest write/read path** (`SqliteEventStore` encrypt-on-write, `PayloadCipher`/`EncryptedPayload`). 2 gate-fixes old — scrutinize hard. | **DEEP** |
| 7 | `core/state-store` (`com.homesynapse.state`) | Projection/materialized views, `projectionVersion` (5), view checkpoints, the derivation model (the production no-op is a `DerivationRule` lambda, NOT a class — verify). | medium |
| 8 | `config/configuration` (`com.homesynapse.config`) | YAML load (safe-load, AMD-71 traversal guard, `!include`/`!secret`/`!env`), schema validation, hot-reload atomic swap, and the **secret store + `ScopeKeyManager`** (root key, HKDF KEKs, wrapped DEKs, the M6.3 `encryptPayload` counter-nonce path + `scope_nonce_counters.json`, `EncryptionScope`). The security center of gravity. | **DEEP** |

## Session-A emphases (beyond the framework checklist)

- **The M6.3 crypto, end-to-end:** trace one sensitive event from `ScopeKeyManager.encryptPayload` (counter allocation + the fsync-ahead-of-return durability) → the `Main`/`PayloadCipher` adapter contract → `SqliteEventStore` write (ciphertext + `payload_iv` + `dek_ref`) → read-back decrypt. Pressure-test every item in the framework's "Crypto" bullet — concurrent publishers on one scope, the `dek_ref` colon parse, the `identity`-keyed-but-empty edge, null-cipher fail-closed, the cold-start warmup, and that no key/plaintext reaches logs.
- **Event-sourcing correctness:** the framework's "event-sourcing invariants" bullet is your spine — write-ahead durability, per-entity sequence, global position, replay idempotency, `eventTime`/`ingestTime`.
- **The reserved-but-unbuilt register** mostly lives in your half (chain-hash activation, Ed25519, crypto-shred, the OR-M6-NONCE restore half, the `identity` scope) — catalog each precisely; a B-side or M7 consumer must not assume they work.

## Deliverable

`context/audits/2026-06-14_core-review_A_data-crypto-spine.md` — per the framework's finding format: an **executive summary** (top findings by severity + the spine's health verdict + the reserved-but-unbuilt register), **per-module sections** (1-paragraph model + findings table), **cross-cutting findings**, a **coverage ledger** (every module 1–8 → depth → finding count), and a **"research avenues surfaced"** section (raw — the converge consolidates). Hand Nick a commit message (`!`-free).

## Done-when

Modules 1–8 each have a ledger row; the audit is on disk; the executive summary + reserved-but-unbuilt register are written; any BLOCKING finding is escalated to Nick; the research-avenues section is captured for the converge; commit message handed over. (Parallel-capable with B; the converge merges both.)

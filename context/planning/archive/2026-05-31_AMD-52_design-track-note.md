<!--
file: context/planning/2026-05-31_AMD-52_design-track-note.md
purpose: Short design-track note for AMD-52 (typed StateChangedEvent payload). Successor to the CLOSED M4.0b-3 design-track map. Points to the design beat, the research brief, and the gated WU; does not duplicate them.
audience: PM, Nick
state-type: current
status: CURRENT — issued 2026-05-31
predecessor: 2026-05-30_M4.0b-3_design-track-map.md (CLOSED §0c — reference only, do NOT reopen)
-->

# AMD-52 Design Track — Typed `StateChangedEvent` Payload

**One-line status (UPDATED 2026-05-31):** OQ-05-08 beat DONE → Research 11 returned + assessed (A−) → G1/G2 settled by Nick's four fork calls → **AMD-52 AUTHORED + RATIFIED** (Nick + external review; watermark AMD-51→AMD-52; AMD-52-INV-01..07 §22) → **next = the M4.0b-4 coding instruction** (UNBLOCKED; milestone id confirmed). _Track effectively CLOSED for authoring; remaining work is implementation._

> **RATIFICATION (2026-05-31):** Research 11 (PM Assessment A−, §7 source-verified vs HEAD `98f705b`) settled the OPEN forks. The four PM-under-delegation calls (Nick): **G1 wire-form** = compact `{"t":<AttributeType>,"v":…}` envelope, custom `JsonSerializer` pair in `core/persistence`, no new module edge; **float identity (F1)** = bit-anchored `Double.doubleToLongBits`, `chain_hash` stays inert; **NaN/±Inf** = JSON-valid sentinels; **G2 Path B (F2)** = legacy `schema_version=1` reads → defined `DegradedEvent` (no decode-path upcaster — Path A re-derivation authoritative). AMD-52 `design/amendments/AMD-52_Typed_StateChangedEvent_Payload_Serializer_and_Replay.md` RATIFIED as-authored by Nick + an independent HomeSynapse Core Claude Project review. **Implementing WU = M4.0b-4 (confirmed).**

This note is the lightweight successor to the **M4.0b-3 design-track map** (`2026-05-30_M4.0b-3_design-track-map.md`), which is **CLOSED** (its §0c FINAL — Workstream A complete, AMD-51 shipped `98f705b`). That map is the **predecessor**: it framed AMD-52's serializer/replay blast radius in its §3 and deferred it as OQ-05-08. **Do not reopen it.** This note carries the AMD-52 thread forward without duplicating the design beat.

## Where AMD-52 stands (HEAD `98f705b`, watermark AMD-51, `projectionVersion` 3)

- **AMD-51 shipped** the typed comparator and **preserved the String `StateChangedEvent` payload** on purpose (§2.7) so the typed-payload swap could be staged. AMD-52 is that swap.
- **The OQ-05-08 design beat is DONE:** `homesynapse-core-docs/design/2026-05-31_AMD-52_Typed_Payload_Serializer_Replay_Design_Beat.md`. It settled the four sub-questions from source:
  - **DECIDED** — no event-store / `view_checkpoints` row migration; typed payload stays in the `events.payload` BLOB; per-event `events.schema_version` is the string↔typed discriminator (beat §3).
  - **DECIDED** — AMD-52 is its own `projectionVersion` **3→4** bump riding AMD-50's frozen reconciliation-backfill unchanged (beat §5).
  - **DECIDED (mechanism)** — the nested `AttributeValue` codec is a custom Jackson (de)serializer in `core/persistence` keyed by an explicit `AttributeType` tag, **no `@JsonTypeInfo`** (ArchUnit Rule 7 + Jackson-isolation HARD RULE; beat §2.1).
  - **OPEN (forks → research)** — the exact tagged-union wire-form, deterministic `double` + `NaN`/`±Inf`/`−0.0` JSON encoding (beat §2.2), and the replay-determinism contract: Path A (re-derive typed from the immutable `state_reported` log during 3→4 backfill — authoritative, rides AMD-50/AMD-51 unchanged) vs Path B (version-branched decode of historical String payloads via the `AttributeValueUpcaster`) (beat §4).
- **Research 11 dispatched:** `context/instructions/Research_11_Typed_Event_Payload_Persistence_Brief.md` (REC-100+). Scoped ONLY to the OPEN forks; surveys Axon `@Revision`/upcaster chain, EventStoreDB, Akka Persistence serializers, Kafka Schema Registry union types.

## The path from here to AMD-52 (and the gate)

```
[OQ-05-08 design beat]  DONE 2026-05-31  ── closes G5 (row shape), frames G1–G4
        │
        ▼
[Research 11 in Claude Project]  ── informs G1 (serializer) + G2 (replay determinism)
        │  results return → fresh Cowork session
        ▼
[PM 6-step A–F assessment]  ── source-verify §7 vs HEAD; frame forks for Nick
        │
        ▼
[Nick adjudicates the serializer + replay forks]  (the four beat §10 calls)
        │
        ▼
[Author AMD-52]  ← PM Mode-1; only when G1–G4 are settled (beat §9 GO)
        │
        ▼
[M4.0b-4 coding instruction]  ← PM Mode-3; reuses AMD-50 backfill for 3→4; proposed milestone id — confirm with Nick
```

**Go/no-go (beat §9):** GO only when **G1 (serializer codec settled)** and **G2 (replay-determinism contract settled)** land; **G3 (CheckpointSerializer typed envelope)** and **G4 (consumer blast radius spec)** are authoring work once G1/G2 close; **G5 (row shape — no migration)** is already CLOSED. Until GO, the String `StateChangedEvent` payload stays **frozen** (AMD-51 §2.7).

## Frozen — do not reopen on this track
AMD-50 backfill mechanism (reused unchanged for 3→4); no `Clock` in `DerivationContext`; no `ServiceLoader`; D-01 (no exhaustive switch over event types — an exhaustive switch over the sealed `AttributeValue` IS allowed); the AMD-47 8-variant hierarchy; the `@JsonTypeInfo`-ban + Jackson-isolation rules; and — until AMD-52 ratifies — the String `StateChangedEvent` payload.

**Proposed implementing WU:** **M4.0b-4** (per the M4.0b-x / projection-block-50–52 scheme; AMD-50→51→**52**). Proposed, not locked — confirm with Nick.

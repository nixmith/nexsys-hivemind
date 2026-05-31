<!--
file: context/handoff/2026-05-31_AMD-52_research-return_session_prompt.md
purpose: Fresh-Cowork-session kickoff brief — receive Research 11 results, assess them, frame the AMD-52 serializer/replay forks for Nick, author AMD-52, then branch into the broader M4 next-part work. Carries the OQ-05-08 design-beat outcome so the next session loads precise context without re-discovery.
audience: PM (next session), Nick
state-type: current
status: CURRENT — issued 2026-05-31 after the OQ-05-08 design beat + Research 11 dispatch. HEAD `98f705b`, no code.
last-verified: 2026-05-31 against HEAD `98f705b`
-->

# Next Cowork Session — Receive **Research 11**, frame the AMD-52 forks, author **AMD-52**, and open the M4 next-part work

**You are the PM.** This session spans two modes: **Mode 1 (Architect)** for the Research 11 assessment + AMD-52 authoring, and a lightweight planning posture for the broader M4 fronts (§6). The OQ-05-08 design beat is already done; this brief carries its outcome so you do not re-discover it. Read this, then the design beat it points to, then (when Nick provides them) the Research 11 results.

**Primary trigger:** Nick is running the Research 11 brief (`context/instructions/Research_11_Typed_Event_Payload_Persistence_Brief.md`) in a HomeSynapse Core Claude Project. **Expect Nick to paste/upload the Research 11 output at the start of this session.** Everything below tells you exactly what to do with it.

---

## 0. Session-start discipline (do first, before any forward work)

1. **Run the freshness preflight** (`project-manager/references/freshness-preflight.md`, 10 checks). Expect **PASS** — the AMD-52 design-beat round was committed by Nick (`AMD-52 OQ-05-08 design beat + Research 11 brief + trackers (M4.0b-4 PLANNED-GATED)` or similar). If **STALE**, reconcile (retroactive WUCP Phase 2) before any forward work — no exceptions. If **CONFLICTED**, escalate to Nick.
2. **Source-verification rule (standing, hard-won):** the in-sandbox `git`/`grep` **truncates / line-ending-churns** this synced folder. Verify every type/module/version claim with the **Read tool on the working tree** (or `git show HEAD:<path>` run on Nick's machine) — **never trust in-sandbox `git`/`grep` for source facts.** This is the rule that made the AMD-51 §7 embeds trustworthy and caught Research 10's stale §7.
3. **Ground truth (confirm at session start):** HEAD `98f705b` (M4.0b-3 / AMD-51 shipped). `projectionVersion` = **3**. On-disk amendment watermark = **AMD-51**. Workstream A **COMPLETE**. No uncommitted code. AMD-52 will bump `projectionVersion` **3→4** riding AMD-50's frozen backfill unchanged.

---

## 1. What is ALREADY DECIDED by the OQ-05-08 design beat (do NOT re-litigate)

Full reasoning + source anchors: **`homesynapse-core-docs/design/2026-05-31_AMD-52_Typed_Payload_Serializer_Replay_Design_Beat.md`**. Read it before authoring. The four OQ-05-08 sub-questions resolved to:

- **DECIDED — event-store row shape (gate G5, CLOSED).** The typed payload stays **inside the existing `events.payload` BLOB**; **no `events`-table and no `view_checkpoints` row migration.** The per-event **`events.schema_version`** column (already threaded through `EventPayloadCodec.decode(eventType, schemaVersion, payload)`) is the **string↔typed discriminator** — AMD-52 bumps the written `StateChangedEvent` schema_version 1→2. Confirmed against V001 + `EventPayloadCodec`.
- **DECIDED — staging.** AMD-52 is its **own amendment** and its **own `projectionVersion` 3→4 bump**, riding AMD-50's frozen reconciliation-backfill **unchanged** (the exact precedent AMD-51 set for 2→3; AMD-51 §2.7 preserved the String payload *specifically* to make this staging free). No new backfill mechanism.
- **DECIDED — serializer *mechanism*.** The nested `AttributeValue` codec is a **custom Jackson `JsonSerializer`/`JsonDeserializer` pair in `core/persistence`**, keyed by an **explicit `AttributeType` discriminator** — **NOT `@JsonTypeInfo`** (banned: ArchUnit Rule 7 `NO_JSON_TYPE_INFO_IN_EVENTS`) and **no Jackson annotation on `AttributeValue`/`StateChangedEvent`** (the Jackson-isolation HARD RULE — Jackson is confined to 9 persistence classes; `PersistenceJacksonModule`/ULID is the precedent). The codec's variant dispatch should be **total over the 8 `AttributeType` values** (the serialization twin of AMD-51-INV-01).
- **DECIDED — map-ordering is a non-issue.** No `AttributeValue` variant contains a `Map`; `ArrayValue` is an ordered `List`. No key-ordering nondeterminism on either surface.
- **Two serialization surfaces, not one** (the structural correction): **S1** = `EventPayloadCodec` (the event payload — `StateChangedEvent`); **S2** = `CheckpointSerializer` (the materialized-view checkpoint — already anticipates a "typed envelope per entry"). Both share the one nested-`AttributeValue` codec.

---

## 2. What Research 11 must resolve — the OPEN forks (gates G1 + G2)

Research 11 is scoped to exactly these (design beat §10). When the results land, assess them against these forks:

- **G1 — serializer encoding (design beat §2.2).** (a) the exact **tagged-union wire-form** (e.g. `{"t":"FLOAT","v":…}` vs nested; how `ArrayValue` recurses; compactness under `Include.NON_NULL`); (b) a **canonical, byte-stable `double`→text** rendering (matters for forensic equality, idempotency, the reserved `chain_hash`); (c) a **lossless, JSON-valid, deterministic encoding of `NaN`/`±Inf`/`−0.0`** (standard JSON can't carry NaN/Inf; `FloatValue` can — no ctor guard; Jackson `ALLOW_NON_NUMERIC_NUMBERS` emits non-standard tokens, likely rejected).
- **G2 — replay-determinism contract (design beat §4).** **Path A** (re-derive typed from the immutable `state_reported` log during the 3→4 backfill — *authoritative*, rides AMD-50/AMD-51 unchanged) is decided-by-precedent. **Path B** (version-branched decode of a historical String-payload `state_changed` via the `AttributeValueUpcaster` SPI vs accepting a lossy `DegradedEvent`) is the OPEN call, plus the **per-lift bit-determinism** proof obligation (extend AMD-51 §5 #5b's `Double.doubleToLongBits` bit-identity discipline to *every* String→typed lift, not just QUANTITY).

Gates **G3** (CheckpointSerializer typed-envelope spec) and **G4** (consumer blast-radius spec, design beat §6) become **authoring work** once G1/G2 close; **G5** is already CLOSED.

---

## 3. When the Research 11 results arrive — the workflow

1. **Run the PM 6-step A–F assessment** (the established pipeline used for Research 4/8/10): format → exec summary → cross-cutting → per-REC (REC-100+) → **§7 source-corrections (source-verify every type/module/version claim against HEAD `98f705b` with the Read tool)** → quality grade. Write it to `context/assessments/2026-05-31_Research_11_PM_Assessment.md` (or the date it returns). **The Research 6 lesson applies hardest here:** confirm the researcher's §7 against source — do not trust it. The brief embedded verbatim constraints precisely so fabrications are visible.
2. **Frame the G1/G2 forks for Nick** — present the researcher's recommendations against the prior art (Axon `@Revision`/upcaster chain, EventStoreDB, Akka Persistence `SerializerWithStringManifest`, Kafka Schema Registry Avro/Protobuf unions), with a PM lean per fork. The four calls Nick (or PM-under-delegation) must make: the wire-form, the float/NaN encoding, the Path-B decision, and the inline-BLOB confirmation under Pi-class/256 MiB constraints.
3. **Check the go/no-go gate (§4).** Only when **G1 + G2 are settled** do you proceed to author AMD-52.
4. **Author AMD-52** (Mode 1) per the amendment format used by AMD-47/AMD-50/AMD-51 (`homesynapse-core-docs/design/amendments/AMD-52_*.md`). It must: change `StateChangedEvent.oldValue/newValue` String→`AttributeValue`; specify the persistence `AttributeValue` codec (no `@JsonTypeInfo`); extend `CheckpointSerializer` to a typed envelope (G3); enumerate + specify every consumer migration (G4, design beat §6 — incl. `shouldPublishDerived` coherence on the typed materialized value and the AMD-51-INV-05 / §2.6-erratum re-verification once the prior side is natively typed); bump `projectionVersion` 3→4 on AMD-50's frozen backfill; embed the verbatim `module-info.java` ×3 + the V001 schema + the `libs.versions.toml` Jackson rows (§7, STOP-on-mismatch); register any AMD-52 invariants into `Architecture_Invariants_v1.md`; and confirm the AMD-50 supersession test still guards the 3→4 transition. On ratification: fold Doc 01/03 currency, raise the watermark to AMD-52, update PROJECT_SNAPSHOT / pm-handoff / the design-track note.
5. **Then (next-next, not this session) the M4.0b-4 coding instruction** (Mode 3) — reuses AMD-50 backfill for 3→4; modifies `ProductionDerivationRule` to emit the typed payload; wires the persistence codec; **must include the §4c arch-rule reminder** (tests inject `Clock`; `NO_DIRECT_TIME_ACCESS` scans `com.homesynapse.state` and `com.homesynapse.persistence`, both non-whitelisted). **Confirm the M4.0b-4 milestone id with Nick** before issuing (proposed under the M4.0b-x / projection-block-50–52 scheme; not locked).

---

## 4. The go/no-go gate (design beat §9) — restated

| Gate | Criterion | Status now |
|---|---|---|
| **G1 — serializer** | codec wire-form + canonical float + NaN/±Inf/−0.0 encoding settled | **OPEN → Research 11** |
| **G2 — replay determinism** | Path A authoritative; Path B decided; per-lift bit-determinism accepted | **OPEN → Research 11** |
| **G3 — checkpoint (S2)** | `CheckpointSerializer` typed envelope specified | authoring work once G1 lands |
| **G4 — consumers** | every reader of `oldValue/newValue` + materialized `attributes` has a benign migration | authoring work once G1/G2 land |
| **G5 — row shape** | no `events` / `view_checkpoints` migration | **DECIDED — CLOSED** |

**GO** to author AMD-52 only when G1 + G2 are settled. Until then the String `StateChangedEvent` payload stays **frozen** (AMD-51 §2.7).

---

## 5. Out of scope for the AMD-52 thread (explicitly)

- Re-opening the DECIDED items in §1 (mechanism, row shape, staging) — settled against source. If you believe one is wrong, raise it with source evidence; do not silently redesign.
- Any code this session — AMD-52 is a Mode-1 governance/authoring output; code is the M4.0b-4 coding instruction that follows ratification.
- Bumping `projectionVersion` — that happens in the M4.0b-4 code, not the amendment.

---

## 6. "Commence further work on the core" — the broader M4 next-part fronts (branch here if Research 11 isn't back yet, or after AMD-52)

Workstream A is COMPLETE. With AMD-52 gated on research, these are the open, parallelizable M4 fronts (design-track-map §5, pm-handoff Next Tasks). Any of them is legitimate forward work this session if the AMD-52 thread is waiting:

- **Workstream B — device-model breadth.** AMD-44 Floor/EntityRole implementation + Research 8 REC-23–30. Typed-value contract (AMD-47) already DONE; this is the remaining device-model expansion. Not gated on AMD-52.
- **Workstream C — integration-api interface freeze.** Research 6 REC-41–51 — **gated on P3** (Nick's NQ-1..6 calls on Research 6) **and** P4 Doc-05 (Integration-Runtime integration-api) currency, itself P3-gated. Supervisor impl = M9. If Nick wants to unblock C, the move is the NQ-1..6 deliberation.
- **Timestamp-model unifier.** Retire the M4.0b-2 interim mixed-`lastChanged` (event-time in backfill, wall-clock on LIVE). Needs its own design beat first (touches `EntityState`/Doc 03, likely AMD-11 staleness, read-path blast radius) — possibly amendment-worthy. Adjacent to the derivation path; **Nick's call whether to bundle near AMD-52.**
- **Doc-currency follow-ups (low-risk, PM can execute on request):** PLAN-M4-CONSOLIDATED-v2 §3 — propagate the M4.0b-2 re-scope + the M4.0b-3 + M4.0b-4 rows so P2 and the plan agree; any residual KB punch-list items.

**If you branch into B/C/unifier, open its own design beat or assessment — do not fold it into the AMD-52 amendment.** Treat each as a distinct work unit with its own WUCP closeout.

---

## 7. Frozen — do not reopen (any track)

AMD-50 backfill mechanism (reused unchanged for 3→4); `DerivationContext` has no `Clock`; no `ServiceLoader`; D-01 (no exhaustive switch over **event** types — an exhaustive switch over the sealed `AttributeValue` IS allowed); the AMD-47 8-variant hierarchy + canonicalize-at-construction; the `@JsonTypeInfo`-ban + Jackson-isolation rules; AMD-51 §2.7 + §2.6 erratum; and — until AMD-52 ratifies — the String `StateChangedEvent` payload.

---

## 8. Pointers

- **Design beat (read first):** `homesynapse-core-docs/design/2026-05-31_AMD-52_Typed_Payload_Serializer_Replay_Design_Beat.md`
- **Research 11 brief (what Nick is running):** `context/instructions/Research_11_Typed_Event_Payload_Persistence_Brief.md`
- **AMD-52 design-track note:** `context/planning/2026-05-31_AMD-52_design-track-note.md`
- **Predecessor (CLOSED — reference only):** `context/planning/2026-05-30_M4.0b-3_design-track-map.md` (§3 framed this blast radius; §0c FINAL closed the track)
- **AMD-51 (the comparator this builds on):** `homesynapse-core-docs/design/amendments/AMD-51_Typed_AttributeValue_Change_Detection_Comparator.md` (esp. §2.7 String-payload rationale + §2.6 erratum)
- **AMD-50 (the frozen backfill 3→4 rides):** `homesynapse-core-docs/design/amendments/AMD-50_Version_Transition_Backfill_and_Cursor_Determinism.md`
- **MODULE_CONTEXT (verify via Read tool):** `core/persistence/MODULE_CONTEXT.md`, `core/state-store/MODULE_CONTEXT.md`, `core/device-model/MODULE_CONTEXT.md`, `core/event-model/MODULE_CONTEXT.md`
- **Source to re-verify before authoring:** `StateChangedEvent.java`, `StateReportedEvent.java`, `AttributeValue.java` + 8 variants, `AttributeValueUpcaster.java`, `EventPayloadCodec.java`, `PersistenceObjectMapper.java`, `CheckpointSerializer.java`, V001 schema, the three `module-info.java`, `gradle/libs.versions.toml`

**Bottom line:** receive Research 11 → 6-step A–F assessment (source-verify §7) → frame G1/G2 for Nick → on GO, author AMD-52 (typed payload; persistence `AttributeValue` codec, no `@JsonTypeInfo`; 3→4 on AMD-50's frozen backfill) → then the M4.0b-4 coding instruction. The serializer mechanism, row shape, and staging are already decided; this session decides the wire-form + replay contract and writes the amendment. If research isn't back, advance Workstream B / the timestamp unifier / doc-currency instead.

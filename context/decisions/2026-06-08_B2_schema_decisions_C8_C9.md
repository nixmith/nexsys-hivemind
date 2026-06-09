<!--
file: context/decisions/2026-06-08_B2_schema_decisions_C8_C9.md
purpose: M5-B/B2 — the regret-proof, schema-irreversible decisions the immutable log makes now-or-never: C8 actorRef identity semantics + C9 the energy event SHAPE. Each passes the contract-freeze-readiness gate. Rides alongside the M6 AMD-66..71 block.
audience: Nick (ratify), PM, Coder, independent DOCS-Project reviewer
update-cadence: once (decision), then reference
state-type: decision
status: PROPOSED 2026-06-08 — awaits independent (DOCS-Project-style) review + Nick ratification. Schema-irreversible (immutable log) → reviewed like a contract freeze.
anchors: context/audits/2026-06-06_M3-M4_foundation-readiness-assessment.md (§4.4 actorRef; §4.1/§5 energy); context/decisions/2026-06-06_post-M4_M5-window_decisions.md (D4 energy shape-now); context/strategy/HomeSynapse_MVP_Data_Readiness_Specification.docx (§4 energy field set); homesynapse-core EventEnvelope.java:112; EventTypes.java
baseline: homesynapse-core HEAD `6c6dd33` — actorRef + energy slots source-verified at this commit
-->

# M5-B/B2 — Regret-Proof Schema Decisions: C8 (`actorRef`) + C9 (energy event shape)

These are the **schema-irreversibles the immutable, append-only event log makes now-or-never.** Every event already written carries `actorRef` and (for power-reporting devices) energy readings; once a large corpus accrues, changing their semantics requires a replay/migration over the whole log. The decisions below fix the **semantics/shape** without changing already-written bytes — that is what makes them regret-proof. **Each passes the contract-freeze-readiness gate** (round-trips / enforceable / owner-doc) per Doc 15 §8.2's discipline. They **freeze contracts** → independent DOCS-Project-style review (not P4).

**Scope discipline (D4, and the candidate-universe framing):** these freeze the **shape/semantics now**; they do **not** build features. C9 in particular is the energy **shape**, not the energy protocol vocabulary or any energy feature. C10 (payload-typing posture) is **consciously deferred this session** (gate capacity — see §C10).

---

## C8 — `actorRef` identity semantics

### Source state (verified at `6c6dd33`)

`actorRef` is a **bare nullable `Ulid`** on `EventEnvelope` (`:112`) and `EventDraft` (`:74`), polymorphic "person or actor" **by convention** (PersonId/AutomationId/SystemId "resolved from context"; LTD-04, deliberately untyped to avoid a sealed hierarchy). It is **live, not reserved** — it round-trips through persistence (written `SqliteEventStore.java:330`, hydrated `:672`); **every event already carries it.** There is no Person/User entity, no role, no RBAC; REST auth is `ApiKeyIdentity` (a *client*, not a person — rest-api `MODULE_CONTEXT:315`); automations carry **no** actor identity for the commands they issue. INV-MU-01 (audit trail) rests on this untyped, unmodeled, but live field. The multi-user *feature* is deferred (Doc 14 §2.2); the **envelope seam — what `actorRef` points at and how Tier-1 API keys map onto it — is specified nowhere.** (foundation-readiness §4.4 / §6.1#4.)

### Decision (regret-proof — semantics, not field-shape)

1. **Keep `actorRef` as a bare nullable `Ulid`.** Do **not** add a companion discriminator field or retype it — a field-shape change is exactly the migration over the immutable log this decision avoids. The regret-proof move fixes the **convention + resolution rules**, not the bytes.
2. **Closed set of actor kinds.** `actorRef`, when non-null, references **exactly one** of four actor kinds: **`PERSON`**, **`AUTOMATION`**, **`SYSTEM`**, **`API_CLIENT`**. (This maps the four real command sources: a human, an automation run, the platform itself, a Tier-1 API-key client.)
3. **Kind is recoverable by typed-ID provenance, not by a new field.** Every `actorRef` value is the ULID of a typed actor-identity whose kind is its allocating typed-ID space (LTD-04 typed wrappers): a well-known fixed **SYSTEM** ULID; an **`AutomationId`**; a **`PersonId`** (when the person model arrives); an **`ApiClientId`** (the Tier-1 API key's client). The mapping `ULID → kind` is materialized by a forthcoming **`ActorRegistry`** (a forward-add, M10/multi-user — *not* a log migration). Until then the convention is enforced by **allocation discipline at the publish path** (§4).
4. **Tier-1 API keys map to `API_CLIENT`, never `PERSON`.** A command issued through a Tier-1 API key carries the **API client's ULID** as `actorRef` (kind `API_CLIENT`) — `ApiKeyIdentity` is a client, and attributing its actions to a person would be a false audit claim. (When a multi-user model later binds an API key to a person, that binding lives in the `ActorRegistry`, not in a rewrite of historical events.)
5. **Automations MUST set `actorRef = AutomationId`** for every command/event they originate (kind `AUTOMATION`) — closing the "automations carry no actor identity" gap. Derived events inherit `actorRef` from the causing envelope (existing rule, `EventDraft` Javadoc). `actorRef = null` remains valid for events with no attributable actor (e.g., device-originated `state_reported`).

### Contract-freeze-readiness gate

- **Round-trips:** ✓ already — `actorRef` is a `Ulid` persisted and hydrated (`SqliteEventStore:330/:672`); this decision changes no serialized shape.
- **Enforceable:** ✓ — a test asserts (a) the automation publish path stamps `actorRef = AutomationId`; (b) the Tier-1 API command path stamps the `ApiClientId`, never a `PersonId`; (c) a non-null `actorRef` is always drawn from one of the four typed-ID spaces (and, once `ActorRegistry` exists, resolves to a kind). The negative test: an arbitrary unregistered ULID in `actorRef` is rejected at the publish boundary.
- **Owner-doc:** Doc 01 (Event Model) — the actor-attribution section currently says "person or actor by convention"; it gains the four-kind closed set + the typed-ID-provenance + the API-client mapping. INV-MU-01 cites it. **Implementing path:** a Doc 01 amendment authored at the milestone that first enforces it (M10 / multi-user); this record + a Doc 01 currency note land now so the convention governs from the next event written.

### What this does NOT do (no feature)

No Person/User entity, no roles, no RBAC, no `ActorRegistry` implementation, no auth changes — those are the multi-user feature (M10+). This freezes only the **envelope seam semantics** so the accruing log is consistently attributable.

---

## C9 — Energy event **shape** (shape only, no features — D4)

### Source state (verified at `6c6dd33`)

**Zero energy event types exist.** `EventTypes.java` (53 constants) has none for energy; energy rides the generic `telemetry_summary` (`:185`). The slots are reserved (`EventCategory.ENERGY`, `EntityType.ENERGY_METER`; `EnergyMeter`/`PowerMeter` capabilities) but the **event vocabulary and the standardized data shape are absent** (foundation-readiness §4.1/§5; INV-EI-01 MVP claim currently unmet). Retrofitting energy semantics onto a log full of generic telemetry is the migration this avoids.

### Decision (regret-proof energy **shape**, grounded in data-readiness §4)

Freeze the **shape** that makes energy data uniformly structured from MVP — riding the **existing** event types (no premature protocol vocabulary):

1. **The standardized `power_measurement` capability attribute set** — every power-reporting device's `state_reported` events carry, as typed `AttributeValue`s (AMD-47/52 `QuantityValue` with canonical units), the **four** attributes: **`instantaneous_power` (W)**, **`accumulated_energy` (Wh)**, **`voltage` (V)**, **`current` (A)**. A Zigbee smart plug and a Modbus inverter therefore produce **identical energy events at the semantic layer** (data-readiness §4 "energy entity template").
2. **The standardized energy aggregate field set** — the hourly/daily aggregate (`telemetry_summary`) outputs for energy entities carry the **six** fields: **total consumption (Wh)**, **total production (Wh, if applicable)**, **net import/export**, **peak power with timestamp**, **cost estimate (if tariff data present)**, **self-consumption ratio**. These are the exact inputs NexSys Grid (VPP capacity estimation) and NexSys Assure (efficiency attestation) will consume (data-readiness §4).
3. **Energy events carry the energy consent-scope category** — aligning with INV-PD-07's crypto-shred scopes (data-readiness §6: one classification serves UI filtering, future access scoping, and crypto-shred lifecycle). `EventCategory.ENERGY` + `EntityType.ENERGY_METER` are populated for energy entities.
4. **Ride existing event types; do not mint a protocol vocabulary now.** Energy readings ride `state_reported` (domain path) with the attribute set; aggregates ride `telemetry_summary` (telemetry path) with the field set. **No** dedicated meter/tariff/grid/SOC/solar event types, **no** OpenADR/IEEE-2030.5/FERC-2222 fidelity — those are the **energy feature** (deferred).

### Staging (the shape is fixed; breadth + scope-membership are refined by M5-D evidence)

- **Breadth** (whether to mint protocol-specific energy event types + build energy features) is **staged behind the M5-D energy interviews** (D4 — Part B energy-shape questions; build features only on real demand).
- **At-rest encrypted-scope membership** of energy is **refined by the Pi-4 microbench (OQ-15-2)** — Doc 15 §3.4 currently keeps energy **plaintext-at-rest at MVP** (high-volume, not PII under INV-PD-03), while the data-readiness §6 scope alignment treats energy as a shred-scope; **the microbench resolves whether the volume/perf supports encrypting it.** This is a **list-tuning of the Doc 15 §9 default, NOT a Doc 15 re-open** — flagged so the two are reconciled when OQ-15-2 returns. (The shape decision here is independent of and unaffected by that tuning — the attributes/aggregates are the same whether or not the scope is encrypted-at-rest.)

### Contract-freeze-readiness gate

- **Round-trips:** ✓ — the `power_measurement` attributes are typed `QuantityValue`s carried by the AMD-52 typed-payload codec (already round-trips); the aggregates ride `telemetry_summary`. No new serialization needed for the shape.
- **Enforceable:** ✓ — a test asserts a power-reporting device's `state_reported` carries the four attributes with canonical units (W/Wh/V/A as `QuantityValue`), and an energy aggregate carries the six fields; energy events carry `EventCategory.ENERGY` + the energy consent-scope.
- **Owner-doc:** Doc 02 (Device Model — the `power_measurement` capability + `EntityType.ENERGY_METER`) + the data-readiness §4 spec + INV-EI-01. **Implementing path:** a Doc 02 currency/amendment defining the standardized energy capability + aggregate schema, authored when energy first lands in code (rides M6/M7's typed-data spine or the energy-feature milestone); this record fixes the shape now so the accruing log is energy-uniform.

### What this does NOT do (no feature)

No energy protocol vocabulary, no OpenADR/2030.5/FERC clients, no VPP/tariff/grid logic, no energy dashboard, no aggregation engine build — those are the energy feature (gated on the interviews). This freezes only the **data shape** (attribute set + aggregate set + scope) so energy is uniformly structured from the first energy event.

---

## C10 — payload-typing posture: CONSCIOUSLY DEFERRED this session

The handoff scopes C10 as "if gate capacity remains." It is **deferred** to keep this session within the contract-freeze gate's review capacity (C8 + C9 are the deliverables the handoff names). C10 is **less now-or-never than C8/C9**: AMD-52 already froze the typed `StateChangedEvent` payload precedent (typed tagged-union, no `@JsonTypeInfo`), so the payload-typing *posture* has a working precedent the log already follows. C10 (how far to push typed payloads vs generic maps across the remaining event families) rides the M7 typed-data-spine work / the energy-feature milestone, authored with the same contract-freeze-readiness gate. **Logged, not lost.**

---

## Review + ratification

- **Independent (DOCS-Project-style) review** — these freeze schema contracts over the immutable log; review like AMD-54..64 / Doc 15 (re-derive the source state at `6c6dd33`; test each gate row; confirm regret-proofness — no already-written bytes change).
- **Nick ratifies** C8 + C9. On ratification: Doc 01 currency note (C8) + Doc 02 currency note (C9); the enforcing Doc 01/Doc 02 amendments are authored at the implementing milestones (M10 for C8; M6/M7/energy-feature for C9). The conventions govern from the next event written regardless.

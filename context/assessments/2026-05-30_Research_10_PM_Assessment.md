<!--
file: context/assessments/2026-05-30_Research_10_PM_Assessment.md
purpose: PM assessment of Research 10 (Typed Attribute Change-Detection Semantics) — dispositions, source corrections, NQ-10-* framing for Nick. SOURCE-VERIFIED against HEAD 60b4185 (git object store, not the working-tree mount).
audience: PM, Nick
state-type: current
status: v1 — §1–§6 strategically ACCEPTED; §7 code baseline source-corrected (CONFIRMED, not "cannot verify"); NQ-10-1..6 framed for Nick's adjudication.
last-verified: 2026-05-30 against HEAD `60b4185` (device-model, state-store, event-model source + module-info.java, all read via `git show HEAD:`)
-->

# Research 10 — PM Assessment (v1 — source-verified against HEAD `60b4185`)

**Date:** 2026-05-30
**Document:** Research 10 — *Typed Attribute Change-Detection Semantics for State Derivation: Per-Type Equality, Value-Based Deadbands, and Replay-Safe Comparison*
**RECs assessed:** REC-90 through REC-95 (6 total)
**Researcher:** HomeSynapse Core Claude Project (deep internet research)
**Protocol:** 6-step A–F PM research pipeline; every §7 type/module claim source-verified against `git show HEAD:` (device-model + state-store + event-model + verbatim `module-info.java`). This is the Research 6 lesson applied: **I verified §7 against actual source, so the corrections below are CONFIRMED, not "researcher-claimed / cannot verify."**
**Gate:** OQ-05-06 / OQ-05-08 (typed change-detection). This assessment is the input to Nick's **NQ-10-1..6** adjudication (design-track-map §4) and to authoring **real AMD-51 (comparator)** + **AMD-52 (typed `StateChangedEvent`)**.

---

## Disposition Table

| REC | Title | Disposition | Target WU (corrected) | AMD | Maps to NQ | Risk |
|---|---|---|---|---|---|---|
| REC-90 | Typed, total `hasChanged(prior, inbound)` per permit | **ACCEPT (modify)** — retarget M4.0b-3; site is `ProductionDerivationRule`, not `EchoStateRule`; inbound needs typed reconstruction (C5) | M4.0b-3 | AMD-51 | NQ-10-1, NQ-10-5 | MEDIUM |
| REC-91 | Carry typed values in `StateChangedEvent` + materialize typed | **ACCEPT (scope first)** — highest-risk; scope serializer/replay blast radius (design-track-map §3) before committing; staging candidate | M4.0b-3 (or M7) | AMD-52 | NQ-10-4 | **HIGH** |
| REC-92 | Single `FloatValue` epsilon policy (abs+rel), explicit NaN / `-0.0` | **ACCEPT** — defaults are Nick's call | M4.0b-3 | AMD-51 | NQ-10-1 | LOW-MED |
| REC-93 | Normalize `QuantityValue` to canonical unit before compare; units-lib decided separately | **ACCEPT (modify)** — `AttributeSchema.canonicalUnitSymbol` already exists (C6); strengthens option (a) hand-rolled; LTD-10 is Nick's call | M4.0b-3 | AMD-51 | NQ-10-1, NQ-10-3 | MEDIUM |
| REC-94 | `DegradedAttributeValue` inert for change-detect (+ recovery emit) | **ACCEPT** — resolves the design-track-map's open "always-changed vs never-publish" as *never-emit-on-inbound + emit-on-recovery* (HA-mirrored) | M4.0b-3 | AMD-51 | NQ-10-1 | LOW |
| REC-95 | Reserve (do not implement) optional per-attribute value-deadband | **ACCEPT (defer)** — reserve field on **`AttributeSchema`** (not `CapabilityInstance`, C6); implement post-M4 | reserve in M4.0b-3; impl deferred | (none yet) | NQ-10-2 | LOW |

**Summary: 6 ACCEPT, 0 REJECT.** Two carry conditions: REC-91 must have its serializer/replay blast radius scoped before AMD-52 is committed; REC-95 is reserve-only. Four strategic calls are reserved for Nick (see §F). **No REC survives with its stated "Target WU"** — every one was labeled against an already-committed milestone and is retargeted to M4.0b-3 (C2).

---

## Step A — Format Compliance: **PASS**

All seven sections present and substantive (exec summary, platform deep-dives, cross-cutting, amendment recs, caveats/open-questions, sources, code-level implications). Sourcing is primary-source and densely cited (HA source verbatim, ZCL spec language, Z-Wave parameter manuals, PI ExcDev/CompDev, Indriya `equals` vs `isEquivalentTo`, Debezium before/after). Section §6 lists ~28 traceable URLs. One self-flagged sourcing limitation (Matter §7.7.7/§7.7.8 verbatim text un-fetchable) is honestly disclosed and does not affect any REC. Format is at or above the Research 4/7 bar.

## Step B — Executive Summary: **STRONG**

The seven headline verdicts are defensible and, critically, **correct on the one thing that is non-negotiable here**: every time-based mechanism (Matter min/max interval, Z-Wave 30-second rule, PI `ExcMax`/`CompMax`, swinging-door carried state, debounce) is disqualified because it violates replay determinism. That is exactly INV-PROJ-01 / AMD-50 §2.4 / AMD-50-INV-03, and the research reaches it independently from the literature rather than by being told. The "keep three concepts distinct — comparison epsilon vs stored precision vs display rounding" framing is the right mental model and is the precise antidote to phantom-change event storms. The MVP policy call — *typed structural equality + float epsilon now, deadbands deferred* — aligns with the PM's preliminary lean in the design-track-map (NQ-10-1/NQ-10-2) and with our "no premature abstraction" posture.

## Step C — Cross-Cutting Analysis: **SOUND**

The concept-mapping table (§3) is the most useful artifact in the document. The cross-platform invariant it surfaces — **discrete types (boolean/enum/string) use pure equality and never carry a deadband; analog types (int/float/quantity) can carry a same-typed absolute delta; arrays use full-replacement structural comparison** — maps cleanly onto our sealed `AttributeValue` permits and is unanimous across ZCL/HA/PI/Z-Wave. The over-abstraction analysis (§3.3) correctly distinguishes *our* cost (stateVersion inflation + `state_changed` noise, second-order) from the surveyed platforms' cost (radio/battery/storage on constrained links), and concludes — rightly — that a deadband suppresses *small real* changes and therefore carries missed-change risk that must not be adopted implicitly in MVP. The competitive read (our replay-deterministic constraint is *stricter* than any surveyed platform; Debezium's typed before/after diff is the closest philosophical match and the best fit for M7 conditions/triggers) is accurate.

---

## Step D — Per-REC Assessment

### REC-90 — Typed total `hasChanged` per permit — ACCEPT (modify)

The core of AMD-51. Replacing `Objects.equals(oldString, newString)` (after `rawValue().toString()`) with a typed per-permit comparison is correct and necessary: the current stringification conflates `21.0`/`21.00`, loses type identity, and is format-fragile. The per-permit policy (exact for Boolean/Int/Enum/String; epsilon Float; canonical-unit Quantity; deep order-sensitive Array; Degraded per REC-94) is the right contract and is what NQ-10-1 asks for.

**Two corrections the coding instruction must carry (both CONFIRMED against HEAD):**
1. **Site.** The production change-detect logic is `ProductionDerivationRule` (package-private in `com.homesynapse.state`, reached via `DerivationRule.production()`), **not** `EchoStateRule` (a testFixture). The research's §7 names `EchoStateRule.lookupAttribute`; the real `priorValue(...)` doing the stringification lives in `ProductionDerivationRule`. (C4)
2. **Typed inbound does not exist yet.** The research's signature `hasChanged(AttributeValue prior, AttributeValue inbound)` assumes a typed inbound. At HEAD the inbound is `StateReportedEvent.value()` — **a `String`** (the record is all-`String`: `attributeKey, value, unit, rawProtocolValue, rawProtocolUnit`). The *prior* side is a typed `AttributeValue` (from the materialized `attributes` map); the *inbound* side must be **reconstructed** to typed via the `AttributeValueUpcaster` keyed by `AttributeSchema.type` before the comparator can run. This is the load-bearing AMD-51 design point the research under-specifies — and it is exactly where the M4.B3 DP-1 upcaster-wiring carry-in earns its place. (C5; → NQ-10-3/NQ-10-6)

*Backward-compat note (research is right):* typed compare means `21.0` vs `21.00` newly compare equal, so replays produce *fewer* `state_changed` and lower `stateVersion` — a replay-divergence that **must** ride a `projectionVersion` bump. That is the 2→3 bump (NQ-10-6), not a free change.

### REC-91 — Typed `StateChangedEvent` + materialize typed — ACCEPT (scope first) — **HIGHEST RISK**

This is AMD-52 and the single most dangerous item in the track (design-track-map §3). The change itself is right in principle: `StateChangedEvent` today is `(attributeKey:String, oldValue:String, newValue:String, triggeredBy:EventId)` and `applyToState` writes `new StringValue(value)` regardless of source type — so every downstream consumer (M7 conditions/triggers especially) must re-parse and re-guess types. Carrying typed `AttributeValue oldValue/newValue` and materializing the typed value fixes a real latent bug.

**But the blast radius is not contained in the comparator.** It touches: (a) the **serializer** — `CheckpointSerializer`/Jackson must (de)serialize the 8-variant sealed hierarchy *deterministically across `projectionVersion`* and *upcaster-compatibly* for already-persisted string-valued `StateChangedEvent`s; (b) the **event-store schema** — confirm the typed payload stays inside the existing payload JSON column and does not change the on-disk event row shape (almost certainly true — confirm, do not assume); (c) **replay determinism** — replaying an old string-payload `state_changed` under the new typed rule must yield a deterministic typed value, which is the upcaster's load-bearing job jointly with AMD-50's backfill.

**PM disposition:** ACCEPT the direction, but **do not author AMD-52 until the §3 serializer/replay scoping beat is done.** Strongly consider the staging option: ship **AMD-51 (typed comparator, typed compare, *string* event)** in M4.0b-3 first, then **AMD-52 (typed event)** as a separate `projectionVersion` bump once the serializer work is sized. AMD-51 is independent of AMD-52; AMD-52 is not independent of the serializer. (→ NQ-10-4)

*Field-name nit:* the research calls the linking field `causingEventId`; the actual component is `triggeredBy`. (C6)

### REC-92 — Float epsilon policy — ACCEPT

Correct and necessary: exact `==` is wrong (`0.1+0.2 != 0.3`), and `Float.equals` is wrong in the opposite direction (`-0.0 != 0.0`, `NaN == NaN`). The proposed rule — `changed iff |a−b| > max(absEps, relEps·max(|a|,|b|))`, canonicalize `-0.0`→`0.0`, NaN↔number = changed / NaN↔NaN = unchanged — is the standard combined absolute+relative comparison and should be documented as *the* canonical rule, applied everywhere. The research is appropriately humble that the defaults (`absEps = relEps = 1e-9`) are a *correctness* epsilon to neutralize FP noise, **not** a perceptual deadband, and flags "VERIFY against M4 sensor data." That defaults question is Nick's call (§F-2). Keep the epsilon permanently distinct from stored precision and display rounding.

### REC-93 — Canonical-unit `QuantityValue` comparison — ACCEPT (modify)

Right requirement: `21.0°C` and `294.15 K` are equal; comparing magnitude-only or raw strings both misfire. Normalize both operands to a canonical unit for the dimension, then apply the REC-92 epsilon; differing **dimensions** ⇒ changed (and a likely schema violation worth surfacing).

**Correction that changes the dependency calculus (C6, CONFIRMED):** `AttributeSchema` *already* carries `unitSymbol` **and** `canonicalUnitSymbol` (plus `minimum`, `maximum`, `step`, `type`). The canonical unit per attribute is therefore **already modeled** — the comparator does not need to invent a canonical-unit table from scratch; it reads `canonicalUnitSymbol` and converts. This materially weakens the case for pulling in JSR-385/Indriya (REC-93 option b, three JARs, LTD-10): the M4 quantity set is small and the canonical target is already in the schema, so the **hand-rolled converter (option a)** is the recommended path. The units-library dependency remains a real LTD-10 decision and is Nick's call (§F-3), but the schema precedent tilts it toward "not for M4."

### REC-94 — `DegradedAttributeValue` inert + recovery emit — ACCEPT

This resolves the design-track-map's explicitly-open NQ-10-1 sub-question ("Degraded = always-changed *or* never-publish — needs Nick's call"). The research's HA-mirrored rule is the right answer and is more precise than either pole: **inbound Degraded ⇒ never emit** (do not overwrite a good canonical value with a degraded one); **prior Degraded + valid inbound ⇒ emit** (recovery); **two Degraded ⇒ unchanged.** This is sourced to HA's `check_valid_float` verbatim. INV-04's "DegradedAttributeValue never written to canonical state under strict mode" (AMD-47, M4.B3 DP-1 carry) aligns with "inbound Degraded never emits." Nick confirms (§F-6); recommend ACCEPT as-is.

### REC-95 — Reserve (don't implement) per-attribute deadband — ACCEPT (defer)

The evidence is unusually clean: every platform that ships deadbands (HA, ZCL, Z-Wave, PI) does so to save *radio/battery/storage* on constrained links — a cost HomeSynapse does not pay, since change-detect runs in-runtime on already-received events. A deadband additionally suppresses *small real* changes (the OSTI/PMU distortion case; HA generic-thermostat missed-trigger reports) — a policy decision with missed-change risk that should not be made implicitly in MVP. **Defer the deadband; reserve the schema shape so it can be added later without a breaking change.**

**Correction (C6):** the reserved field belongs on **`AttributeSchema`** (the verified home of per-attribute metadata: `type`, `unitSymbol`, `canonicalUnitSymbol`, `minimum`, `maximum`, `step`), not on "`CapabilityInstance`'s attributes schema" as the research states. This matches the design-track-map's NQ-10-2 lean ("declare it on `AttributeSchema` — travels with the attribute definition") and the existing `canonicalUnitSymbol` precedent. Field present only for analog types (int/float/quantity), absent ⇒ exact/epsilon comparison (fully back-compatible). Whether to ship even the *reserved* field in M4.0b-3 vs wait is minor; the *implementation* is the deferred item and the ship-vs-defer is Nick's product call (§F-1).

---

## Step E — §7 Source Corrections (CONFIRMED against HEAD `60b4185`)

Unlike Research 4/6/8 — where §7 type claims were "researcher-asserted, cannot verify" — I read the actual source from the git object store. Every correction below is **CONFIRMED**, with the evidence.

| # | Research 10 §7 claim | Verdict | Evidence (HEAD `60b4185`, via `git show`) |
|---|---|---|---|
| **C1** | `DerivationContext` "carries prior `EntityState` + inbound `EventEnvelope` + **injected `Clock`**" | **WRONG — no Clock** | `DerivationContext` is `record(EntityState priorState, EventEnvelope envelope)` — 2 components. The Javadoc says verbatim: *"there is deliberately no clock"* and *"AMD-50 §2.4 removes the formerly-injected `Clock`."* The research's own determinism *conclusion* is right, but its *premise* is a factual error; a coding instruction built on it would mis-specify the context. |
| **C2** | REC "Target WU" labels: REC-90/92/94 → **M4.0b-2**; REC-91/93 → **M4.B3** | **WRONG — both already committed** | M4.0b-2 = `7610296` (committed 2026-05-29); M4.B3 = `60b4185` (committed 2026-05-30). The real target is **M4.0b-3** (next forward WU; `projectionVersion` **2→3**; AMD-51/52). All six RECs retarget to M4.0b-3. |
| **C3** | `AttributeValue` "source-verified real permits (**5**)"; "**M4 adds**: QuantityValue, ArrayValue, DegradedAttributeValue" | **STALE — already 8** | At HEAD the sealed interface already `permits BooleanValue, IntValue, FloatValue, StringValue, EnumValue, QuantityValue, ArrayValue, DegradedAttributeValue` (AMD-47/M4.B3 shipped). The comparator builds on **existing** types, not types-to-be-added. |
| **C4** | Modify `EchoStateRule` (testFixtures) `lookupAttribute` | **WRONG site** | Production rule is `ProductionDerivationRule` (package-private, `com.homesynapse.state`), reached via `DerivationRule.production()`. `EchoStateRule` is the M3.5a fixture it was lifted from. The stringifying `priorValue(...)` is in `ProductionDerivationRule`. |
| **C5** | `hasChanged(AttributeValue prior, AttributeValue **inbound**)` | **Incomplete — inbound is String** | `StateReportedEvent` is all-`String`: `(attributeKey, value, unit, rawProtocolValue, rawProtocolUnit)`. The typed inbound the comparator needs must be **reconstructed** via `AttributeValueUpcaster` keyed by `AttributeSchema.type` (note: `unit`/`rawProtocolUnit` are available for `QuantityValue` reconstruction). This is the AMD-51↔upcaster interaction and the 2→3 backfill wrinkle (NQ-10-3/6). |
| **C6** | Deadband on "`CapabilityInstance`'s attributes schema"; needs a canonical-unit table; field `causingEventId` | **Imprecise — schema already richer** | Per-attribute metadata is `AttributeSchema` (`type, minimum, maximum, step, validValues, unitSymbol, canonicalUnitSymbol, permissions, nullable, persistent`). Deadband belongs on `AttributeSchema`; canonical unit is **already present** (`canonicalUnitSymbol`), reducing REC-93 to "read + convert." `StateChangedEvent`'s linking field is `triggeredBy`, not `causingEventId`. |
| **C7** | (module names not stated) | **Embed verbatim** | `module com.homesynapse.device { requires com.homesynapse.event; requires transitive com.homesynapse.platform; exports com.homesynapse.device; }` · `module com.homesynapse.state { requires transitive platform, device, event, event.bus; requires org.slf4j; exports com.homesynapse.state; }` · `module com.homesynapse.event { requires transitive platform; exports com.homesynapse.event; }`. The research's "comparator can live in `core/device-model`" is **dependency-valid** (device requires event+platform; state requires device — no cycle). |

### D-01 clarification (resolves the design-track-map NQ-10-5 worry)

The design-track-map asks whether D-01's "no exhaustive switch" spirit is satisfied by a polymorphic comparator. **D-01 governs dispatch over *event types* (`DomainEvent`), not over `AttributeValue`.** An exhaustive `switch` over the sealed `AttributeValue` hierarchy (as in the research's §7 function) is idiomatic Java and **not** a D-01 violation — sealed exhaustiveness is the intended use. So *both* candidate shapes for NQ-10-5 (a standalone exhaustive switch **and** a polymorphic method on the sealed interface) satisfy D-01. The choice is ergonomic, not a constraint question (§F-5).

---

## PM's Assessment of the Researcher's Quality

The §1–§6 work is the strongest research-survey output in the series to date: nine platforms with primary-source citations, the correct and independently-derived replay-determinism rejection of all time-based mechanisms, and a genuinely useful concept-mapping table. The MVP policy call matches our priors without being told them.

The §7 weakness is **not fabrication** (the Research 4/8 failure mode) — the types it names are real. It is a **stale code baseline**: the researcher worked from a pre-M4.0b-2 / pre-M4.B3 snapshot, so it targets already-committed milestones (C2), treats already-shipped AMD-47 types as pending (C3), names the fixture instead of the production rule (C4), and asserts a `Clock` that AMD-50 removed (C1). The one genuine *analysis* gap is C5 (typed-inbound reconstruction), which the all-`String` `StateReportedEvent` forces and the research glosses. None of these touch the §1–§6 strategic conclusions; all are corrected above with source evidence.

---

## Step F — Open Questions for Nick (NQ-10-1..6 + the four strategic calls)

The assessment deliberately stops short of the strategic calls — those are Nick's per the design-track-map. Framing + PM lean for each:

**NQ-10-1 — per-variant comparison semantics.** Converged: exact for Boolean/Int/Enum/String; epsilon Float (REC-92); canonical-unit Quantity (REC-93); deep order-sensitive Array; Degraded inert-on-inbound + emit-on-recovery (REC-94). *PM lean: accept as stated.* Sub-call folded into §F-6.

**NQ-10-2 — threshold/deadband locus + ship-vs-defer.** *PM lean: DEFER the deadband for M4 (strong evidence); reserve an optional same-typed field on `AttributeSchema` (analog-only).* The ship-or-defer of even the reserved field is a product call about event-storm tolerance → **§F-1**.

**NQ-10-3 — canonicalization & upcaster role.** *PM lean: compare canonical only on the hot path; the upcaster reconstructs the typed inbound at the ingestion/backfill boundary (from `StateReportedEvent.value`+`unit`, keyed by `AttributeSchema.type`); `canonicalUnitSymbol` is already in the schema.* No strategic fork — this is the C5 mechanism.

**NQ-10-4 — typed `StateChangedEvent` (AMD-52).** The high-risk call. *PM lean: ACCEPT the direction but stage — AMD-51 (typed comparator, string event) in M4.0b-3 first; AMD-52 (typed event) after the §3 serializer/replay scoping, possibly as its own version bump or deferred to M7.* → **§F-4**.

**NQ-10-5 — comparator contract shape (AMD-51).** Both a polymorphic method on `AttributeValue` and a standalone exhaustive-switch function satisfy D-01 (clarified above). *PM lean: polymorphic method on the sealed interface, living in `com.homesynapse.device`, carrying a small `ComparisonPolicy` parameter* (a no-arg method can't carry the Float epsilon / future deadband; the policy has to travel into the call). → **§F-5**.

**NQ-10-6 — `projectionVersion` 2→3.** *PM lean: AMD-50 backfill path reused unchanged; the genuinely new wrinkle is string-history → typed-value reconstruction during the 2→3 backfill (the upcaster, C5); the AMD-50 supersession test remains the standing N→M regression guard.* Confirm the supersession test still guards the typed rule.

### The four strategic calls (PM recommends, Nick decides)

1. **Deadband: ship vs defer (REC-95/NQ-10-2).** *PM recommends DEFER for M4*; reserve the `AttributeSchema` field shape only.
2. **Float epsilon defaults (REC-92).** *PM recommends a pure FP-noise epsilon (`abs=rel=1e-9`), NOT a perceptual deadband (e.g. HA's 0.5°C)* — verify the magnitude against real M4 sensor data before locking.
3. **Units-library dependency (REC-93b, LTD-10).** *PM recommends the hand-rolled converter (option a)* — `AttributeSchema.canonicalUnitSymbol` already carries the canonical target, so Indriya's three JARs are not justified for the M4 quantity set. Revisit if the quantity set grows.
4. **AMD-52 staging/timing (REC-91/NQ-10-4).** *PM recommends authoring AMD-51 first and gating AMD-52 on the §3 serializer/replay scoping beat* — do not commit a typed event payload until the `CheckpointSerializer`/Jackson + event-store + replay determinism interactions are mapped.

---

## Research Quality Assessment

**Grade: A− for §1–§6. C+ for §7. Overall: B+.**

The value is in the platform survey (§2), the concept-mapping and over-abstraction analysis (§3), and the REC design patterns (§4) — strong, well-sourced, and strategically aligned with our replay-deterministic constraint. §7 carries a **stale code baseline** (wrong WU targets, already-shipped types treated as pending, fixture-vs-production-rule site error, a removed `Clock` asserted, and a missing typed-inbound reconstruction step). The difference from Research 4/8: §7's errors are *staleness*, not *fabrication*, and I was able to source-verify and CONFIRM every correction against HEAD — so **§7 is already corrected in Step E and does not block authoring.**

**Net:** the strategic conclusions are authoritative and ready for Nick's NQ-10-* adjudication; the corrected §7 (Step E + the embedded `module-info.java`) is the inventory the AMD-51/52 §7 sections and the M4.0b-3 coding instruction must be built on — not the research's original §7.

---

## Authoring Order (once Nick adjudicates)

1. **AMD-51 (comparator)** — per-variant `hasChanged` semantics (NQ-10-1), contract shape (NQ-10-5), Float epsilon (REC-92), Quantity canonicalization reading `canonicalUnitSymbol` (REC-93a), Degraded rule (REC-94), the typed-inbound reconstruction via the upcaster (C5/NQ-10-3). Register AMD-51 invariants. Embed the verbatim `module-info.java` (C7).
2. **AMD-52 (typed `StateChangedEvent`)** — *only after* the §3 serializer/replay scoping. Decide staging (§F-4).
3. **M4.0b-3 coding instruction** — reuses AMD-50 backfill for 2→3 (NQ-10-6); wires `AttributeValueUpcaster` (M4.B3 DP-1 carry); modifies `ProductionDerivationRule` (C4); includes the §4c arch-rule test-Clock reminder (state-store is non-whitelisted).

---

## Key Insights Internalized

1. **The inbound side of change-detection is stringly-typed.** `StateReportedEvent` is all-`String`; only the *prior* (materialized) side is a typed `AttributeValue`. The typed comparator's hard problem is reconstructing the inbound typed value — that is the `AttributeValueUpcaster`'s reason to exist, and the precise AMD-50-backfill ↔ upcaster interaction for the 2→3 transition.
2. **`AttributeSchema` is richer than the research assumed.** It already carries `canonicalUnitSymbol` (+ `unitSymbol`, `minimum`, `maximum`, `step`). Quantity canonicalization and a future deadband both have a verified, already-modeled home — which collapses REC-93 to "read + convert" and removes most of the LTD-10 pressure.
3. **D-01 is event-type-scoped.** Exhaustive switching over the sealed `AttributeValue` hierarchy is idiomatic and permitted; the NQ-10-5 choice is ergonomic, not a constraint conflict.
4. **The replay-determinism constraint is a feature here.** It rules out, by construction, every time-based change-detection technique the rest of the industry relies on — and the research independently confirms that only value-based comparison survives. AMD-50's no-`Clock` `DerivationContext` is what makes the typed comparator safe to re-execute during backfill.
5. **Source-verify §7 against the git object store, not the working-tree mount.** This session's mount misread truncated/sync-stale files; `git show HEAD:` is the reliable inventory source and is what made these corrections CONFIRMED rather than "cannot verify."

---

**Assessment completed:** 2026-05-30 by PM (Cowork session).
**Status:** v1 — §1–§6 ACCEPTED; §7 source-corrected (CONFIRMED vs HEAD `60b4185`); NQ-10-1..6 framed. **Next:** Nick adjudicates NQ-10-1..6 + the four strategic calls (§F) → author AMD-51 (then AMD-52 after §3 scoping) → M4.0b-3 coding instruction.

---

## v2 Ratification Addendum (2026-05-30 — strategic calls made under Nick's delegation)

Nick delegated the four §F strategic calls + NQ-10-5/6 to the PM ("those are yours to make"). The PM re-verified each against committed source at HEAD `60b4185` (working-tree Read = HEAD; in-sandbox `git show` was truncating, so the Read tool was authoritative per the M4.0a mount-staleness lesson) before deciding. **All four PM recommendations are RATIFIED**; two are sharpened with a source-grounded refinement; one ledger catch is recorded. Nick retains veto before commit.

### Source re-verification (the facts the calls rest on, all confirmed at HEAD `60b4185`)

| Fact | Source | Confirms |
|---|---|---|
| `StateReportedEvent(attributeKey, value, unit, rawProtocolValue, rawProtocolUnit)` — all `String`; Javadoc "Phase 3 introduces typed AttributeValue" | `core/event-model/.../StateReportedEvent.java` | C5 — inbound is stringly-typed; comparator must reconstruct via upcaster. **Note: `unit` IS carried on the event** (relevant to the OQ-05-09 unit-threading sub-question below). |
| `StateChangedEvent(attributeKey, oldValue, newValue, triggeredBy)` — old/new are `String`; linking field is `triggeredBy` (not `causingEventId`) | `core/event-model/.../StateChangedEvent.java` | REC-94/AMD-52 framing; C6 field-name nit |
| `QuantityValue(double value, String unit)` **canonicalized at construction** — hand-rolled `CATALOGUE` (°C/K/°F, W/kW/mW, Wh/kWh/J/kJ, lux/klx, %), fail-closed, "no units-of-measure library… (AMD-47-INV-03 / REC-93)"; Javadoc: "Two `QuantityValue`s of the same dimension are directly magnitude-comparable on their canonical `value()`" | `core/device-model/.../QuantityValue.java` | C6 / Call 3 — units work is **already done**; comparator does **no unit lookup** |
| `AttributeValueUpcaster.upcast(String storedTypeName, String rawForm, int fromSchemaVersion)` + `canUpcast(...)` + default `upcastLenient(...)` (failure → `DegradedAttributeValue`); strict mode "never produces a DegradedAttributeValue… AMD-47-INV-04"; "MUST run strictly before `DerivationRule.evaluate()` on both `onEvent` and `processBatch`… AMD-47-INV-02" | `core/device-model/.../AttributeValueUpcaster.java` | REC-95 reconstruction seam — signature is `(storedTypeName, rawForm, fromSchemaVersion)`, **keyed by type-name string + schema version, not by `AttributeType` enum directly** |
| `AttributeSchema(attributeKey, type, minimum, maximum, step, validValues, unitSymbol, canonicalUnitSymbol, permissions, nullable, persistent)` | `core/device-model/.../AttributeSchema.java` | C6 — `canonicalUnitSymbol` already present (QUANTITY); deadband's future home; also note `minimum`/`maximum`/`step` already exist |

### The four strategic calls — RATIFIED

**Call 1 — Defer the deadband to post-M4. RATIFIED.** Structural-equality + float-epsilon is the correct M4.0b-3 scope. A deadband against the *last reported* value needs extra stored state not in the event log → replay-divergence risk; excluding it keeps the rule trivially replay-deterministic. When it lands it goes on `AttributeSchema` (already the per-attribute metadata home — `minimum`/`maximum`/`step`/`canonicalUnitSymbol` live there), not `CapabilityInstance`. (REC-92/REC-95-reserve.)

**Call 2 — FP-noise epsilon, not perceptual. RATIFIED + sharpened.** Epsilon answers "did the number actually change," not "is the change meaningful" (the latter is the deferred deadband). **Refinement (technical):** a *pure relative* epsilon is undefined/explosive near zero, so AMD-51's comparator must use the **total** form `|a − b| ≤ max(absEps, relEps · max(|a|, |b|))`, both at FP-noise scale (relEps ≈ 1e-9; absEps a small fixed floor, e.g. 1e-12). The comparator must be **total over the IEEE-754 edge set**, spelled into the AMD with no implementation latitude: `NaN`↔`NaN` = no change; `+0.0`↔`−0.0` = no change; same-sign `Inf` = no change; opposite-sign or finite↔Inf = change. (Note `QuantityValue` construction already rejects non-finite magnitudes, so for QUANTITY the NaN/Inf cases can't reach the comparator — but `FloatValue` can carry them, so the rule is still required.) (REC-91.)

**Call 3 — Hand-roll units; skip Indriya/JSR-385. RATIFIED — and already satisfied.** `QuantityValue` *already* canonicalizes at construction (AMD-47/M4.B3, committed, source-confirmed above). Two `QuantityValue`s reaching the comparator are **already in the same canonical unit**, so the QuantityValue↔QuantityValue compare is pure magnitude-with-epsilon (Call 2) with **no unit lookup in the comparator**. No JSR-385, no LTD-10 dependency amendment. Unit metadata is load-bearing only at the *reconstruction* step (the wrinkle below), not at compare. (REC-93.)

**Call 4 — Stage AMD-51 before AMD-52. RATIFIED — the load-bearing sequencing decision.** Ship AMD-51 (the comparator: reconstruct-then-compare → boolean verdict; **`StateChangedEvent` String payload preserved unchanged**) as the M4.0b-3 amendment. Do **not** co-commit the typed payload. AMD-52 (typed `AttributeValue` old/new on `StateChangedEvent`) gets its **own design beat first** (§AMD-52 checklist below) because it crosses the serializer/replay surface — the single riskiest thing in the track. The comparator returning a boolean while the rule still stringifies for the payload (as it does today) is fully separable, so staging costs nothing and de-risks everything. (REC-94.)

### NQ-10-5 / NQ-10-6 — decided

**NQ-10-5 (comparator placement). DECIDED: external `AttributeValueComparator` in `core/state-store`,** co-located with `ProductionDerivationRule` and the upcaster reconstruction so "reconstruct → compare" is one unit in one module. **Not** a method on `AttributeValue` — that keeps the device-model type a pure data carrier and stops epsilon policy leaking into device-model/event-model. D-01 is event-type-scoped, so an exhaustive `switch` over the sealed `AttributeValue` hierarchy inside the comparator is allowed — ergonomic choice, not a constraint conflict. *(This is a deliberate, source-grounded refinement of the assessment's §F-5 lean, which floated a polymorphic method on the sealed interface in `com.homesynapse.device`. Rationale: the comparator needs a `ComparisonPolicy` (epsilon, future deadband) that is state-store/projection policy, not device-model data — putting it on the device-model type drags projection policy into the data layer. Keeping the comparator in state-store next to the only caller is cleaner and respects the module layering. Either satisfies D-01; this is the better separation.)*

**NQ-10-6 (where unit normalization lives). DECIDED: at reconstruction, not at compare** (per Call 3 — already done at `QuantityValue` construction). The 2→3 `projectionVersion` bump reuses AMD-50's backfill path unchanged; the supersession test remains the standing N→M regression guard.

### Refinement — the upcaster unit-threading wrinkle (AMD-51 authoring note; tracked as OQ-05-09)

`AttributeValueUpcaster.upcast(storedTypeName, rawForm, fromSchemaVersion)` takes a type-name string + version — **no unit.** Reconstructing a `QuantityValue` needs a unit, and the canonical `QuantityValue` ctor requires a *recognised* unit symbol. Source shows **`StateReportedEvent` carries `unit`** — so the most likely resolution is: the reconstruction step reads `StateReportedEvent.value` + `StateReportedEvent.unit` and constructs `QuantityValue(value, unit)` (ctor canonicalizes), rather than routing QUANTITY through the bare 3-arg `upcast`. AMD-51 must settle exactly how the unit reaches reconstruction for QUANTITY (event `unit` field vs `AttributeSchema.canonicalUnitSymbol` vs unit embedded in the value string), checked against what adapters actually put in `StateReportedEvent` for a QUANTITY attribute. Narrow, does not change any call. (OQ-05-09.)

### Ledger catch — REC-93 double-booked

`REC-93` is used twice: (1) AMD-47/M4.B3's "hand-rolled `String` units, no JSR-385" (committed, cited verbatim in `QuantityValue` Javadoc) and (2) Research 10 §4's "unit normalization at compare." They converge in meaning (Research 10's collapses into what AMD-47 already shipped) but reuse the number. Reconcile at the next freshness pass — recommend aliasing Research 10's to the existing REC-93 (same decision). Tracked, non-blocking.

### Status / next steps

- **All four calls RATIFIED; NQ-10-5/6 decided.** **OQ-05-06 RESOLVED** — M4.0b-3 is design-unblocked.
- **Next forward action = author AMD-51** (the M4.0b-3 amendment): `AttributeValueComparator` in `core/state-store`; per-type structural equality (REC-90); total-form float/quantity epsilon + IEEE totality (REC-91/Call 2); reconstruct-then-compare via the upcaster (REC-95), failure → `DegradedAttributeValue` → treat as change (and per REC-94: inbound Degraded never emits, prior-Degraded+valid-inbound emits = recovery, two Degraded = unchanged); **String `StateChangedEvent` payload preserved**; settle the OQ-05-09 unit-threading sub-question; `projectionVersion` 2→3 on AMD-50's backfill path; include the §4c arch-rule test-`Clock` reminder (state-store is non-whitelisted). Embed verbatim `module-info.java` for device-model/state-store/event-model (C7).
- **AMD-52 (typed payload) — DEFERRED** to its own design beat behind the checklist below (OQ-05-08). Do not author until that beat closes.
- **This assessment is uncommitted** — ready for Nick to commit (DEC-M3-12). Suggested message: `Research 10 PM assessment + v2 ratification (REC-90..95 → M4.0b-3; AMD-51 ready, AMD-52 staged)`. **Nick retains veto on any call.**

### AMD-52 design-beat scoping checklist (answer before AMD-52 is authored — OQ-05-08)

1. **Jackson polymorphism for the sealed `AttributeValue`** — `@JsonTypeInfo` discriminator vs hand-rolled `AttributeType` tag + value; must be deterministic across `projectionVersion` and stable on disk.
2. **Replay determinism** — replaying an old String-payload `state_changed` under the typed rule must yield a deterministic typed value via the upcaster (the single reconstruction source for both backfill and live).
3. **Event-store on-disk shape** — confirm the typed payload stays inside the existing payload JSON column (no row migration); confirm, don't assume.
4. **Consumer blast radius** — every reader of `StateChangedEvent.oldValue/newValue` (today `String`): `applyToState`, projection/query/observability surfaces, future M7 automation triggers/conditions. Enumerate before changing the type.
5. **`CheckpointSerializer`/`EnumTransition` interaction** — re-confirm the `instanceof`-with-fallback sites compile and flow the typed payload unchanged (M4.B3 verified no exhaustive switches; re-confirm for the payload change).

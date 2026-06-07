<!--
file: context/audits/2026-06-06_AMD-87_DOCS_Review_Return.md
purpose: Lightweight (P4 block-track) DOCS-Project review return for AMD-87 (Expectation Persisted Codec, PROPOSED).
audience: Nick (ratify), PM
status: COMPLETE
baseline: homesynapse-core HEAD `8ef9e9f`; watermark AMD-64; projectionVersion 5
reviewer: DOCS-Project (independent session, 2026-06-06)
-->

# AMD-87 Lightweight DOCS Review Return — `Expectation` Persisted Codec

**Verdict: RATIFY-WITH-EDITS** (lightweight)

Three editorial fixes in §7 and the masthead required before ratification. No design, contract, or classification issue found.

---

## J1 — Is P4 (lightweight) the right track?

**PASS.**

AMD-87-INV-01 is a fidelity guarantee about additive serde: every `Expectation` permit round-trips losslessly through `EventPayloadCodec`, and `WithinTolerance`'s two doubles use the already-ratified AMD-52 bit-anchored-float / non-finite-sentinel discipline (AMD-52-INV-03, AMD-52-INV-04). The invariant creates no new persisted shape, no behavioral contract, and no cross-subsystem obligation. It is the serialization-layer twin of what AMD-52-INV-02 already guarantees for `AttributeValue`, applied to a second sealed type using the identical mechanism.

**The JPMS edge.** Adding `requires com.homesynapse.device` to `persistence`'s `module-info.java` is a real module-graph change, not a contract-only freeze. The PM's assessment that it remains P4-proportionate is correct for three reasons:

1. **Acyclicity is structural.** `com.homesynapse.device` requires `{value, event, platform}` — not persistence. No cycle is possible. This is source-verified in the AMD baseline and consistent with the post-relocation graph documented in the `AttributeValue` module relocation design note (spike outcome, §5.1).
2. **The edge adds no new coupling direction.** Persistence already reads device types transitively (`persistence → transitive state → transitive device` — confirmed in AMD-52 §7.1 and exercised by `CheckpointSerializer`'s `AttributeValue` imports at the time of the relocation). The explicit `requires` makes an existing transitive readability relationship direct, which is good JPMS hygiene when a module adds code that imports types from the target.
3. **The functional scope is narrow.** Persistence uses device only for the `Expectation` sealed interface and its 4 permits — pure type-signature visibility for the codec. No device behavior, no lifecycle coupling, no runtime callback.

The edge is mechanically necessary, verified safe, and precedented by the `persistence → value` edge AMD-52 introduced for `AttributeValue` serde (same pattern, different leaf). P4 holds.

---

## J2 — 4-permit codec fidelity

**PASS** (with a scope note).

**Scope note:** This review reasons from design-document anchors, not live source. The review prompt asks to "re-derive the permit shapes from source," but per the DOCS-Project scope boundary, I do not hold the live code (the CORE project does). The permit shapes below are verified against the design-document hierarchy; full source re-derivation should be confirmed by the Coder at M5-A implementation or by Nick at commit review.

**Design-document verification (Doc 02 §3.8, §8.2):** the 4 permits and their constituent fields match AMD-87 §2's wire-form table:

| Permit | Doc 02 shape | AMD-87 wire form | Codec delegation | Consistent? |
|---|---|---|---|---|
| `ExactMatch` | wraps a target `AttributeValue` | `{"t":"ExactMatch","v":<AV>}` | delegates `"v"` to existing `AttributeValue` codec | ✓ |
| `AnyChange` | wraps a previous `AttributeValue` | `{"t":"AnyChange","v":<AV>}` | delegates `"v"` to existing `AttributeValue` codec | ✓ |
| `EnumTransition` | wraps a target `String` | `{"t":"EnumTransition","v":"<string>"}` | plain string | ✓ |
| `WithinTolerance` | `double target`, `double tolerance` | `{"t":"WithinTolerance","target":<bits>,"tolerance":<bits>}` | AMD-52 bit-anchored treatment | ✓ |

The AMD-52 precedent disciplines are all correctly invoked: tagged-union `{"t":…}` envelope (REC-100); exhaustive `switch` with no `default` (future permit = compile break, per AMD-52-INV-02 / AMD-51-INV-01 discipline); keyed on the sealed `Expectation` interface (Jackson `SimpleSerializers` walks interfaces); no `@JsonTypeInfo` / no domain Jackson annotations (Rule 10 / `NO_JACKSON_IN_DOMAIN_MODEL`); codec in `com.homesynapse.persistence` (Jackson-isolation HARD RULE). All coherent.

---

## J3 — Edge + scope fences

**PASS.**

- **Acyclicity:** `com.homesynapse.device` does not `requires com.homesynapse.persistence` (device requires value/event/platform only). Confirmed in AMD-87 baseline and consistent with the post-relocation module graph.
- **Scope fences (AMD-87 §5):** codec only — no `Expectation.evaluate(...)` implementation; `WithinTolerance.evaluate()` still throws "deferred to Phase 3" (foundation-readiness F2, automation scope M7/M8). No new persisted shape. No event-store migration. No `projectionVersion` bump. No `@JsonTypeInfo` or domain annotations. All clean and proportionate to P4.
- **Acceptance:** un-`@Disabled` of `EventPayloadCodecTest.CapabilityEvents.capabilityAdded_onOff_roundTrips` — the executable spec already in tree. Correctly scoped: the test exercises the full `CapabilityAdded` round-trip (command-bearing variant via `TestEventSamples.capabilityAddedOnOff()`), which embeds `CommandDefinition → ExpectedOutcome → Expectation`. A GREEN on this test proves the codec works end-to-end.

---

## J4 — Numbering hygiene

**EDIT-REQUIRED.** Three items, all editorial.

### E1 — §7 watermark target is the retired number (MUST FIX)

§7 reads: *"raise the watermark to 65 (or fold in the M5-window mechanics)."*

The watermark is currently AMD-64. AMD-65 is the **retired** number this amendment was reassigned from. On ratification, the watermark should rise to **87** (or to the highest ratified AMD in the M5 window if AMD-86 ratifies alongside). "65" is clearly a vestige from the pre-reassignment tracking.

**Fix:** replace `65` with `87` (or `87, alongside AMD-86 if co-ratified`).

### E2 — `@Disabled` annotation text inconsistency (SHOULD FIX)

Two places in the AMD quote the test annotation as `@Disabled("AMD-87 pending")`:
- The `source` masthead field: *"the executable acceptance test … (`@Disabled("AMD-87 pending")`)"*
- §1 body: *"left `capabilityAdded_onOff_roundTrips` `@Disabled("AMD-87 pending")` as the executable acceptance test"*

The `amd-number-rationale` in the same masthead correctly states: *"the live acceptance test's annotation literally reads `@Disabled("AMD-65 pending")` at HEAD `8ef9e9f`."*

The code at HEAD says `"AMD-65 pending"`, not `"AMD-87 pending"`. Since M5-A deletes the annotation entirely (not re-numbers it), the AMD should quote the actual annotation text. The two references should read `@Disabled("AMD-65 pending")`, with a parenthetical noting this is the retired number that M5-A removes.

### E3 — INV-GA-02 citation scope (NIT, non-blocking)

The `amd-number-rationale` cites INV-GA-02 for AMD-number non-reuse. INV-GA-02's text (Architecture_Invariants_v1.md §15) reads: *"Once an **invariant identifier** (INV-XX-NN) is assigned, it is never reused."* It governs `INV-XX-NN` identifiers, not `AMD-NN` numbers. The AMD-number non-reuse principle is correct and consistently applied (the P2 renumbering decision, the pm-handoff ledger), but it is a de facto governance convention, not a literal INV-GA-02 obligation. The citation is the right spirit but the wrong letter. Consider citing "the P2 renumbering decision" or "the pm-handoff AMD-retirement ledger" alongside or instead of INV-GA-02, or note that INV-GA-02 is invoked by analogy.

This is a nit and not blocking.

---

## Opposing considerations / risks

**The strongest objection to P4** is that `persistence → device` is a new JPMS edge that future amendments could widen (e.g., if persistence ever needed to deserialize `Capability` subtypes or other device-model sealed hierarchies, the edge would carry more traffic). This would make the P4 classification look too lenient in hindsight. However: the edge is already available transitively, adding it explicitly doesn't change the architectural coupling envelope, and widening it would require its own amendment. The risk is speculative and not a reason to escalate this particular codec to the full track.

**No design, invariant, or contract concern.** AMD-87 is a clean, narrow, well-precedented additive-serde amendment. The P4 classification is correct.

---

## Summary

| Job | Verdict | Notes |
|---|---|---|
| J1 — P4 classification | **PASS** | Additive serde; JPMS edge is mechanical and acyclic; INV-01 is fidelity, not new contract |
| J2 — Permit codec fidelity | **PASS** | Design-doc shapes match; AMD-52 disciplines correctly invoked (source re-derivation deferred to CORE) |
| J3 — Edge + scope fences | **PASS** | Acyclic; codec-only; no persisted-shape/projectionVersion change; acceptance scoped correctly |
| J4 — Numbering hygiene | **EDIT-REQUIRED** | E1: §7 watermark "65"→"87"; E2: two `@Disabled("AMD-87 pending")` should read `"AMD-65 pending"`; E3: INV-GA-02 citation scope (nit) |

**Verdict: RATIFY-WITH-EDITS.** Apply E1 and E2 before ratification. E3 is at the PM's discretion.

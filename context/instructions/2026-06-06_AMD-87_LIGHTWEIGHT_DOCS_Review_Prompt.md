<!--
file: context/instructions/2026-06-06_AMD-87_LIGHTWEIGHT_DOCS_Review_Prompt.md
purpose: LIGHTWEIGHT block-track (P4) DOCS-Project review prompt for AMD-87 (Expectation persisted codec, PROPOSED; reassigned from the retired AMD-65 per INV-GA-02).
audience: DOCS-Project reviewer (independent session)
status: READY to dispatch
-->

# LIGHTWEIGHT (P4 block-track) DOCS-Project Review — AMD-87 (`Expectation` Persisted Codec)

You are the independent reviewer for a **lightweight block-track (P4)** amendment — additive serde on the AMD-52 `AttributeValue`-codec precedent. Keep it proportionate: this is **not** a full constitutional review. But confirm two things carefully, because they are the reasons a "lightweight" call could be wrong.

## Baseline + what to read

- **homesynapse-core HEAD `8ef9e9f`.** Re-verify code claims here.
- **Under review:** `homesynapse-core-docs/design/amendments/AMD-87_Expectation_Persisted_Codec.md` (PROPOSED).
- **Sources:** `core/device-model/.../Expectation.java` + the 4 permits (`ExactMatch.java`, `WithinTolerance.java`, `EnumTransition.java`, `AnyChange.java`); `core/persistence/.../AttributeValueSerializer.java` (the precedent); `PersistenceJacksonModule.java`; `EventPayloadCodecTest.java` (the `@Disabled("AMD-65 pending")` acceptance test — note: "AMD-65" is the **retired** number literally in the code; this WU is AMD-87); the persistence + device `module-info.java`; AMD-52 (float-determinism precedent).

## Validation jobs

**J1 — Is the P4 (lightweight) classification right, *despite* AMD-87-INV-01?** A new invariant can signal a non-trivial amendment. Confirm AMD-87-INV-01 is a **fidelity guarantee about additive serde** (every permit round-trips losslessly; `WithinTolerance` is bit-anchored per AMD-52), **not** a new persisted-shape, behavioral-contract, or cross-subsystem obligation. If it is genuinely additive serde with no shape/contract change, P4 stands. If you judge the **new `persistence → device` JPMS edge** (a real `module-info` change, unlike M4.C's contract-only freeze) pushes this past "trivial-additive," say so and recommend escalation to the full track. (PM's view: the edge is mechanical and verified acyclic, so P4 holds — pressure-test that.)

**J2 — 4-permit codec fidelity.** Re-derive the permit shapes from source and confirm the wire forms in §2: `ExactMatch(AttributeValue)` / `AnyChange(AttributeValue)` → `v` delegates to the existing `AttributeValue` codec; `EnumTransition(String)` → plain string; `WithinTolerance(double target, double tolerance)` → **AMD-52 bit-anchored-float treatment** (`Double.doubleToLongBits` text-round-trippable + non-finite sentinels + `−0.0`→`+0.0`). Confirm: keyed on the `Expectation` **interface** (Jackson walks interfaces), **exhaustive `switch` with NO `default`** (a future permit compile-breaks), tagged-union `{"t":…}` mirroring `AttributeValueSerializer`, **no `@JsonTypeInfo`/domain annotations** (Rule 10 holds — codec lives in persistence).

**J3 — edge + scope fences.** Confirm `persistence → device` is acyclic (device does not require persistence). Confirm the scope fences: codec **only** (no `Expectation.evaluate()` impl — `WithinTolerance.evaluate()` rightly still throws; that's automation/M7-8), no persisted-shape/`projectionVersion` change. Confirm the acceptance is the un-`@Disabled` `capabilityAdded_onOff_roundTrips`.

**J4 — numbering hygiene.** Confirm AMD-87 (not 65) is correct per INV-GA-02 (AMD-64/65 retired; AMD-86 = crypto; 87 next clean), and that the doc correctly notes the live `@Disabled("AMD-65 pending")` annotation is the retired number to be deleted (not re-numbered) by M5-A.

## Return format

Verdict: **RATIFY** / **RATIFY-WITH-EDITS** / **REJECT** (lightweight). Per job J1–J4: PASS / EDIT-REQUIRED / FAIL with evidence. Be brief — this is the block-track. The one judgment that matters most is **J1** (is P4 the right track). Commit the return per the canonical-paths convention and cite the path.

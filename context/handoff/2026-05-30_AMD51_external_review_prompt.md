<!--
file: context/handoff/2026-05-30_AMD51_external_review_prompt.md
purpose: The prompt + framing to paste into the HomeSynapse Core Claude Project for an adversarial ratification review of AMD-51. Attach the three files listed in §0.
audience: Nick -> HomeSynapse Core Claude Project
state-type: comms
status: CURRENT — 2026-05-30
-->

# AMD-51 Ratification Review — Prompt for the HomeSynapse Core Claude Project

## 0. What to attach to this message

1. **`AMD-51_Typed_AttributeValue_Change_Detection_Comparator.md`** — the amendment under review (the primary artifact).
2. **`2026-05-30_AMD51_external_review_source_companion.md`** — verbatim source for every type the comparator touches (so your feedback is grounded in the actual code, not an assumed shape).
3. **`2026-05-30_Research_10_PM_Assessment.md`** — the assessment that produced the decisions AMD-51 encodes (v1 §7 source-corrections + v2 ratification). *Context for why the calls were made — not itself under review.*

*(If this Project's knowledge base already contains the homesynapse-core repo and the AMD-50 / AMD-47 amendments, you can rely on those directly; the source companion is a self-contained substitute if not. AMD-50 = the frozen N→M reconciliation-backfill mechanism AMD-51 rides; AMD-47 = the typed `AttributeValue` hierarchy + canonicalize-at-construction.)*

---

## 1. Your role

You are a skeptical senior reviewer — distributed systems + production Java — doing a **pre-ratification technical review** of an architectural amendment for HomeSynapse Core: a **local-first, event-sourced, replay-deterministic** smart-home operating system running on constrained hardware (Raspberry Pi class). The amendment defines a typed change-detection comparator for device attribute values.

We do **not** want a rubber stamp. We want you to actively try to break this — find the missed edge case, the latent non-determinism, the wrong default, the design smell. If it's sound, say so and say *why*; if it isn't, show the specific failure. Disagreement with us is the most valuable thing you can produce. Be concrete and cite the specific section / type / line.

## 2. What is already decided — do NOT relitigate

These were ratified by the project owner (delegated to the PM) after source verification. Treat them as fixed constraints; critique *within* them, not *against* them:

- **Defer the per-attribute deadband** (structural-equality + FP-noise epsilon is the scope; deadband's future home is `AttributeSchema`).
- **Stage AMD-51 before AMD-52** — AMD-51 ships the comparator with the **String `StateChangedEvent` payload preserved**; the typed payload is a separate, later amendment behind its own serializer/replay design beat.
- **Hand-roll units** — already satisfied: `QuantityValue` canonicalizes at construction (AMD-47), so the comparator does zero unit work. No JSR-385/Indriya.
- **Comparator placement** — external `AttributeValueComparator` in the state-store module carrying a `ComparisonPolicy`, *not* a method on the `AttributeValue` sealed interface.
- **Reuse AMD-50's reconciliation-backfill unchanged** for the `projectionVersion` 2→3 transition.

The frozen invariants you must respect are listed in §5 of the source companion (replay determinism, sealed exhaustiveness, no `ServiceLoader`, etc.).

## 3. The decisions we need confidence on (please give a verdict on each)

**Q1 — Comparator contract correctness & totality.** Is the per-variant semantics table (AMD-51 §2.2) correct, total, and replay-deterministic? Specifically probe:
- The Float/Quantity epsilon (§2.3): is the **total form** `|a−b| > max(absEps, relEps·max(|a|,|b|))` right, and is the **IEEE-754 totality table complete and correct** (`NaN`↔number, `NaN`↔`NaN`, `±0.0`, same-sign `Inf`, opposite-sign/finite↔`Inf`)? Is `>` (vs `≥`) the right boundary? Any case missed — subnormals, overflow in `|a−b|`, the `max(|a|,|b|)` behavior when both operands are huge or both near zero?
- The Array semantics: order-sensitive deep recursion with per-element epsilon — any concern for nested `ArrayValue`, large arrays, or mixed-type elements?
- The Quantity dimension check by **canonical-unit-symbol string equality** — is comparing canonical unit *symbols* a sound proxy for "same dimension"? Any collision or future-dimension risk?
- The Degraded rule (§2.4b): never-emit-on-inbound / emit-on-recovery / unchanged-on-two-Degraded — correct and complete?
- Design taste: the comparator returns an **emit predicate** (folding in the asymmetric Degraded rule and the `prior == null` first-report case), not a pure symmetric equality. Is conflating "changed?" with "should emit?" into one method clean, or should the Degraded/null handling live in the rule and the comparator stay a pure equality? Give a recommendation.

**Q2 — The epsilon default (`absEps = relEps = 1e-9`).** This is the one empirical pre-condition the amendment flags for verification. We cannot show you live sensor data, so reason from first principles for the M4 attribute set (temperature °C, humidity %, power W, energy Wh, illuminance lux; brightness/battery as `INT`):
- Is `1e-9` the right *kind* (a pure FP-representation-noise floor) and *magnitude*?
- **Critical interaction:** `QuantityValue` canonicalization applies affine/multiplicative conversions (e.g. °F→°C is `(v−32)·5/9`, J→Wh is `v/3600`). Does the rounding error introduced by these conversions exceed `1e-9` for realistic magnitudes — i.e., could a value reported as `70 °F` (→ `21.111…°C`) vs the same physical reading reported directly in `°C` differ by **more than** the epsilon and trip a spurious change? If so, what floor (absolute and relative) actually neutralizes conversion noise without masking real sensor resolution (sensors typically resolve 0.1 or 0.01 in their native unit)?
- Recommend a concrete default (or a per-dimension default) and a **verification methodology** we can run against captured sensor traces to lock it.

**Q3 — OQ-05-09: inbound reconstruction mechanism (§2.6).** The inbound `StateReportedEvent` is all-`String`; the prior side is typed. AMD-51 resolves this as a **separate schema-driven parse** keyed by `AttributeSchema.type` (QUANTITY uses the event's `unit`, falling back to `AttributeSchema.canonicalUnitSymbol`), explicitly **not** extending the `AttributeValueUpcaster` SPI (which migrates *stored* values and carries no unit).
- Is keeping reconstruction separate from the upcaster the right separation of concerns, or is there a case for one unified seam?
- **Replay subtlety:** during a 2→3 backfill the reconstruction parses *historical* string reports using the *current* schema. Is that deterministic and correct if a schema's `type`/`canonicalUnitSymbol` could change across versions? Where does this break, and does AMD-51 need to say more about it?
- The flagged empirical residual is **adapter-emit consistency** (do all adapters actually populate `StateReportedEvent.unit` for QUANTITY attributes?). Is the `canonicalUnitSymbol` fallback a safe default, and what exactly should we check in the adapter layer?

**Q4 — Sequencing recommendation.** Given your answers above, which do you recommend:
- **(a)** Ratify AMD-51 now and treat the epsilon-default lock and the adapter-`unit` check as explicit gates *inside* the subsequent M4.0b-3 coding instruction; or
- **(b)** Resolve the epsilon default and the adapter-`unit` question *first*, then ratify with both nailed down.

State which, and what specifically (if anything) must be true before ratification vs. what can safely be a coding-instruction gate.

## 4. Output format we want

1. **Headline verdict:** RATIFY-AS-IS / RATIFY-WITH-CHANGES / HOLD — one line.
2. **Per-question verdicts (Q1–Q4):** each with a clear position and concrete evidence/example.
3. **Blocking issues** (must fix before ratification), ranked — with the specific §/type and a proposed fix. Empty list is a fine answer if you find none.
4. **Non-blocking improvements** (nice-to-have, or fold into the coding instruction).
5. **Epsilon recommendation:** a concrete number (or per-dimension table) + the verification method.
6. **Anything we didn't ask about** that a senior reviewer would flag.

Ground every claim in the amendment text or the source companion. Where you're inferring rather than certain, say so.

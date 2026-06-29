<!--
file: context/instructions/2026-06-28_AMD-CAND-1_device-confirmation-characterization_governance-review-dispatch.md
purpose: Governance review→ratify dispatch for AMD-CAND-1 — first-class device-level confirmation characterization (the DeviceProfile confirmation block + a Doc 02 §3.8 per-device confirmability note). Routes to an independent DOCS review → Nick ratifies → fold into Doc 08 §3.6 + Doc 02 §3.8 + watermark bump. The PM hub does NOT self-ratify (the D2-registration-proposal pattern). Bundles one small related governance fold (the V1 read-API-subset vs Locked Doc 16 §4 recording).
audience: an independent DOCS-review Cowork conversation (write-isolated; reviews → returns); Nick (ratifies); the v11 PM hub (authored; folds on ratify); the M9 lane (consumes the ratified slot).
state-type: governance dispatch (review→ratify; PROPOSED — not self-ratified).
status: READY — authored 2026-06-28 by the v11 hub, reconciling the Stream-B research return. Pre-M9 (M9 confirmation acceptance depends on this).
baseline: docs 75d0345 (Doc 02 + Doc 08 LOCKED; watermark AMD-95; invariants 170/50). Re-verify HEAD at review.
anchors: context/assessments/2026-06-28_device-model-and-corpus_research-return.md §4 + §6 (AMD-CAND-1) — the grounding · context/decisions/2026-06-28_bench-test-and-truth-engine_decision-record.md (the moat; R5 sharpening #2) · context/decisions/2026-06-25_deeper-M7-automation-architecture_decision-record.md §D5 · homesynapse-core-docs/design/02-device-model-and-capability-system.md §3.6/§3.8 (Locked) · design/08-zigbee-adapter.md §3.6 (Locked — DeviceProfile registry) · AMD-90-INV-01 · AMD-95 · AMD-87-INV-01 · INV-SA-03.
-->

# Governance Review Dispatch — AMD-CAND-1: first-class device-level confirmation characterization

## Why this exists (and why pre-M9)

The `confirmed | unconfirmed | failed` device-confirmation projection is the lead differentiator. Today HomeSynapse's confirmation semantics live entirely at the **capability** level (Doc 02 §3.6 per-capability `ConfirmationMode`; Doc 02 §3.8 `Expectation` → `CONFIRMED`/`NOT_YET`/`FAILED`; adapters may override only the *tolerance band*). **There is no slot for whether a *specific real device* can render a true `CONFIRMED` at all** — which depends on device-level facts the capability default cannot know: does the device report/return its authoritative attribute, what is its reporting posture (on-change / periodic / sleepy), and does it accept Configure Reporting. The Stream-B research return (§4) established this gap and the schema that closes it; the Stream-A bench measures the values. **M9's confirmation acceptance tests build on this slot** (the research return §5.4) — so it must be ratified **before M9**, not during it. This is the schema realization of the moat: it turns `confirmed/unconfirmed` from a capability-default assumption into a per-device, regression-protected, honestly-degrading fact.

This is a **clean amendment, not a supersession** (Nick's co-signed read 2026-06-28): it **extends a reserved seam** (Doc 08 §3.6 `DeviceProfile` already carries per-device overrides + a `manufacturerCodec` pointer; Doc 02 §3.8 already allows adapter overrides — this widens "override the tolerance" to "override confirmability") and the research found **no invariant conflict**. It is consistent with AMD-90-INV-01 (confirmation is per-action, never Run-blocking, no engine retry), AMD-95 (`DISABLED` ≡ optimistic — now with a *recorded honest reason*), and AMD-87-INV-01 (the `Expectation` codec round-trips losslessly).

## The proposed amendment (PROPOSED — for review, not self-ratified)

**Part A — Doc 08 §3.6 `DeviceProfile` gains a confirmation-characterization block**, one entry **per actuating capability** (research return §4.2):

```
confirmation[]:
  capability              : the capability key (e.g. "on_off")
  confirmationMode        : inherited from the Doc 02 §3.6 default; per-device overridable
  authoritativeAttribute  : the attribute whose report/readback confirms the command
  reportsAuthoritative    : VERIFIED_REPORTS | READBACK_ONLY | NONE
  reportingPosture        : ON_CHANGE | PERIODIC | SLEEPY | NONE
  confirmability          : CONFIRMABLE | BEST_EFFORT | UNCONFIRMABLE   ← the load-bearing honest verdict
  recommendedTimeoutMs    : per-device-tuned; feeds Doc 02 §3.8 default_timeout
  degradeRule             : "no authoritative report within timeout ⇒ UNCONFIRMED (never FAILED unless explicit NACK)"
```

`confirmability` semantics: **CONFIRMABLE** = a true `CONFIRMED` is achievable (device reliably reports/returns the authoritative attribute); **BEST_EFFORT** = possible but slow/unreliable (sleepy / periodic-only / no Configure-Reporting) → expect honest `UNCONFIRMED` under load, tune the timeout up; **UNCONFIRMABLE** = no authoritative attribute returns (`access:2` set-only) → render `UNCONFIRMED` immediately, **never** a false `CONFIRMED` (maps to `ConfirmationMode.DISABLED` *with the honest reason recorded*).

**Part B — Doc 02 §3.8 prose** acknowledges a per-device **confirmability** override (not just tolerance): the engine consumes `confirmability` to choose between attempting a real `CONFIRMED` and rendering an honest immediate `UNCONFIRMED`, with the reason recorded (never silent optimism — INV-SA-03).

**Watermark/register impact:** an AMD number on ratification (the next free number; do **not** pin it here while PROPOSED — INV-GA-02). The research found no new invariant required; if the reviewer judges one warranted (e.g. an INV pinning "a `DISABLED`/`UNCONFIRMABLE` command never renders `CONFIRMED`"), that is a review output, not assumed here.

## Review questions (for the independent DOCS reviewer)

1. **Seam-extension vs supersession.** Is adding `confirmation[]` to the Doc 08 §3.6 `DeviceProfile` and widening Doc 02 §3.8's override scope genuinely additive to the Locked text, with no contradiction of a Locked decision or invariant? (The hub's read: yes — confirm or refute against the Locked §3.6/§3.8 text.)
2. **Invariant coverage.** Does the slot stay consistent with AMD-90-INV-01 (per-action, no retry), AMD-95 (`DISABLED`≡optimistic), AMD-87-INV-01 (Expectation codec round-trip), and INV-SA-03 (never-silent / honest degrade)? Is a new INV warranted (the "never a false CONFIRMED" guarantee), or is it already implied?
3. **Field set.** Are the seven fields necessary and sufficient? In particular, is `confirmability` (the 3-value honest verdict) the right load-bearing field, and is `degradeRule` better as free text or a small enum?
4. **Placement.** Doc 08 §3.6 (DeviceProfile, Zigbee-specific) for the data + Doc 02 §3.8 (capability command model, protocol-agnostic) for the consumption contract — correct split, given INV-CE-04 protocol-agnosticism (the confirmability *concept* must generalize beyond Zigbee even though the first values come from a Zigbee bench)?
5. **M9 dependency.** Confirm the slot is sufficient for the research return §5.4 M9 confirmation-acceptance contract (a `CONFIRMABLE` device's hero command yields `CONFIRMED` on the captured fixture; an `UNCONFIRMABLE`/`BEST_EFFORT` device yields honest `UNCONFIRMED`).

## Routing timing — route NOW, in parallel with the bench + D2 (do NOT serialize behind first-light)

This is a **schema review**: is the `confirmation[]` block additive to Locked Doc 08 §3.6 / Doc 02 §3.8, are the seven fields necessary and sufficient, is the placement right, does it cover the invariants. **None of those need the measured device values.** The research return's worked examples — Hue → `CONFIRMABLE`, the write-only `effect` (`access:2`) → `UNCONFIRMABLE`, the Xiaomi periodic case → `BEST_EFFORT` — already ground the schema's sufficiency. **Bench first-light POPULATES the ratified slot; it does not validate the slot's SHAPE.** So this review runs NOW, concurrently with bench Phase 0/1 and the D2 review — the three-independent-pre-M9-inputs frame. The measured values fold in at the **RATIFY** step; the reviewer may condition ratification with "pending bench confirmation of the example values" — a condition on ratify/fold, **never a reason to delay the review**. Serializing the review behind first-light would stack the review→ratify→fold lag on top of any bench slip and make M9's ready-date gated by bench-THEN-governance instead of both-at-once.

## Related governance fold — bundle into this review pass (Nick's 2026-06-28 steer)

The V1 dashboard read-API has now shipped a surface **coarser than Locked Doc 16 §4 twice**: `RunExplanation` (M7.5a) and `NonFiringExplanation` (M7.5b) each ship the frozen v1.1 contract's field subset, while Doc 16 §4 specifies the richer eventual model (the full `RunExplanation` tree; the 7-value `SuppressionReason`). The pattern is **coherent and intentional** — the frozen v1.1 contract is the V1 wire; Doc 16 §4 is the eventual model; the boundary maps between them (the M7.5a DP-A3 / M7.5b DP-B1 "loose-shorthand" rulings). But it is currently recorded only in coding-instruction rulings + decision records, so **a future reader could mis-read shipped code as contradicting a Locked doc.** AMD-CAND-1 lives in this same "V1 ships a scope-frozen subset of an eventual Locked-doc model" space. **Fold (bundle into this review pass):** add a short note — in the amendments register and/or a Doc 16 §4 marginal note — recording explicitly that the V1 read-API surface (`RunExplanation`, `NonFiringExplanation`, the 4-value `NonFiringVerdict`) is a **frozen-v1.1-contract subset** of the Doc 16 §4 eventual model (the full tree; `SuppressionReason`), deferred-not-contradicted, with the contract-freeze + the read-API scope-freeze as the governing authority. This is a recording amendment (housekeeping severity), not a behavior change; bundling it with AMD-CAND-1 keeps the governance pass single.

## Route

Independent DOCS review (this dispatch) → returns to the v11 hub → Nick ratifies → the hub folds: Doc 08 §3.6 (the `confirmation[]` block) + Doc 02 §3.8 (the confirmability-override prose) + the related read-API-subset recording + watermark bump + any reviewer-warranted INV → register. **Pre-M9 gate:** M9's confirmation-acceptance work does not start until this is ratified + folded. Parallel-safe with M7.5b/c (Core read-side) and the bench Phase 0/1 (which captures the values this slot will hold).

## Out of scope

The corpus IR schema itself (that is the nexsys-bench Phase-2 model + AMD-CAND-4 housekeeping, not this amendment); the color GAP + color-temp canonical-unit drift (AMD-CAND-2/3 — Nick's scope call, separate); any M9 implementation; any change to the capability-level `ConfirmationMode` defaults (those stay; this adds the per-device override).

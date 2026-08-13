<!--
file: context/instructions/2026-08-07_grounding-lane_LF-delivery-evidence-closure_brief.md
purpose: L-F — the delivery-evidence-closure grounding lane (COMMISSIONED by Nick 2026-08-07, v48 beat 3). Fresh Cowork session, read-only, source-grounded. Mission: make "closure-first" one-word-adjudicable at S-10 with real pricing. Return is a NAMED input to the charter SKELETON (Aug-11) and S-10 (Aug-12–13).
audience: the L-F lane (a fresh Cowork session; no role skill required — this brief is self-contained)
status: DISPATCH-READY. Dispatch line: "Read nexsys-hivemind/context/instructions/2026-08-07_grounding-lane_LF-delivery-evidence-closure_brief.md and execute it."
due: return ON DISK by 2026-08-14 09:00 America/Chicago. (FINAL STAMP — v51 beat 5, 2026-08-13: SECOND consecutive UN-RUN adjudication at return-absence; DEGRADE-TO-ABSENT — S-10 adopts whatever is on disk at its close, anything later is post-gate reading; baselines re-derive at launch per rule 7.)
-->

# L-F — The Delivery-Evidence Closure: Grounding + Build-Shape Pricing

## Section 0 — Posture and laws (read first)

1. **READ-ONLY.** You commit NOTHING, edit NOTHING. Your ONLY write is the return file: `nexsys-hivemind/context/research/2026-08-XX_LF_delivery-evidence-closure_return.md` (XX = completion day; due on disk 2026-08-12 09:00 CT — re-stamped v51 beat 4). A lane is verified at its RETURN ON DISK, never at word.
2. **No capability claims.** Every system statement is AS-BUILT (cited at file+line), DESIGNED-FOR, or PROPOSED. The standing honesty rail binds absolutely: **no delivery-proof claims exist today** — DISPATCHED means hand-off to the adapter, not radio delivery; CONFIRMED means the device's own report evidenced the state (ruling R-A(a): state-truth). Your work is precisely about closing that gap; do not write as if it is closed.
3. **Gate sovereignty:** freeze 2026-08-14 EOD; nothing here moves pre-freeze code; every option charters post-gate.
4. **Settled ground fenced, refutation-welcome with primary evidence:** R-A(a) state-truth semantics; the REV-1 S-1 finding (CONFIRMED at source: APS-ack evidence requested then discarded); the priced coincidence window (~1.7% at 5 s / ~10% at 30 s, toward-current-state only, at the S31's measured ~5-min cadence). Challenge framings freely; challenge these facts only at source.
5. **Locked contracts:** the design docs are Locked; any option that changes a Locked behavioral contract must SAY SO and name the amendment path (a ratified AMD) as part of its cost — never silently assume the change.
6. **JPMS module names from `module-info.java` at source only** (the Research-6 rule). `integration-zigbee`'s is embedded below; read `core/automation`'s own module-info before naming its module.
7. **Baseline at dispatch (re-derive at launch):** core `8955e23` · hivemind `4f13e67`. Every line-number cite in this brief was verified against an earlier HEAD — RE-DERIVE all of them at your launch; numbers shift.
8. **A-14 sizing floor:** 15 h/wk attended, weekend-anchored (semester from Aug-17). Price desk effort in days honestly against it.

## Section 1 — Mission

The charter's central engineering decision is whether the **delivery-evidence closure** (candidate (iii)/P2; the S-1 seam) builds FIRST post-gate, ahead of the wider physics program. The hub's standing lean is closure-first — but that lean is currently unpriced. Your return converts it into a one-word ruling over real numbers.

**The technical question:** the Zigbee adapter already receives radio-layer delivery evidence (the EZSP `messageSentHandler` / frame `0x3F` path carrying the APS-ack delivery status for unicasts with `APS_OPTIONS_RETRY_ROUTE_DISCOVERY` set) and today DISCARDS it. Binding that evidence into the command-confirmation record would (a) close the delivery-phase observability gap (delivered-vs-never-delivered currently indistinguishable), and (b) shrink or retire the disclosed toward-current-state coincidence window by adding a causal anchor to confirmation.

**Deliverable: ONE return file** with an executive summary ≤ half a page, then:

1. **The seam, re-grounded at source (current HEAD):** the exact code path from radio ack to discard — `EzspCoordinatorProtocol` (frame constants, callback dispatch), `ZclIngestionUnit` (the REV-1-verified silent frameId drop — re-derive its current lines; no `0x003F` constant existed at REV-1), `ZigbeeIntegrationAdapter` wiring, and the confirmation consumer (`core/automation/src/main/java/com/homesynapse/automation/StandardPendingCommandLedger.java` — the value-match confirm path and the seams REV-1 called clean). Quote the load-bearing lines. This section is the audit surface for everything after it.
2. **2–3 build shapes, each priced** on: scope (modules/files touched; any new event type or schema change named explicitly — event-model changes are the expensive class); effort (desk-days under A-14); risk classes (concurrency/interleaving, event-model & serialization impact, JPMS boundaries, migration, Locked-contract amendments needed); bench implications (what new scenario legs/pins prove it, what the nightly bar becomes, what the S31 corpus can already validate); and what each shape RETIRES (quantify the residual coincidence exposure after the shape ships — the C-2 §2 number must be re-priceable). Candidate shapes to consider (not binding): evidence-only (record delivery status as observability, confirmation semantics unchanged) · delivery-anchored confirmation (delivery evidence becomes a confirmation input with defined precedence vs state reports) · full lifecycle extension (a first-class DELIVERED phase in the command record). Add or replace shapes if source reality suggests better ones.
3. **The do-nothing shelf option, priced honestly:** what staying disclosed-but-open costs (the C-2 §2 limitation stands verbatim; the honesty position remains sound — say so if true).
4. **Honesty semantics per shape:** what each shape lets the product SAY under the D5 law and the no-delivery-proof rail — which C-2 §2 sentences change, which DO-NOT-SAY entries retire, and what NEW never-say lines each shape creates (an ACK is not state; delivery-anchored must never inflate CONFIRMED).
5. **Interaction with N-7's counter rider and the 0x3F bench pin** (both named at REV-1/v45 beat 7): what bench instrumentation must land BEFORE the build to give it a red-first baseline.
6. **Recommendation:** rank the shapes; label the ranking PM-adjudicable (the charter rules, you advise). Refutation-welcome: if closure-first is WRONG (the shelf or the wider physics program should lead), say so with the evidence.

## Section 2 — Named sources (in order)

1. `nexsys-hivemind/context/audits/2026-08-04_REV-1_physics-spine_adversarial-review_return.md` — §3/S-1 (the delivery-phase gap, CONFIRMED at source) + S-2/F-1 context (the value-match exposure).
2. `nexsys-hivemind/context/audits/2026-08-04_REV-1_audit_v45-beat-7.md` — the hub's byte-verified adjudication (S-1 seam cites; the N-7 counter rider; the 0x3F bench pin).
3. The source itself at core HEAD: `homesynapse-core/integration/integration-zigbee/src/main/java/...` (`EzspCoordinatorProtocol`, `ZclIngestionUnit`, `ZigbeeIntegrationAdapter`) and `homesynapse-core/core/automation/src/main/java/com/homesynapse/automation/StandardPendingCommandLedger.java`.
4. `homesynapse-core/integration/integration-zigbee/MODULE_CONTEXT.md` — the M9.4b delta table (frame constants, ingestion scope, SD-3 fence) + Consumers/Gotchas.
5. `nexsys-hivemind/context/strategy/brand-program/2026-08-06_C2-tier0_sleepy-battery-and-confirmation-position_draft.md` §2 — the priced disclosure your shapes re-price.
6. AMD-90 (confirmation timeout) / AMD-97 (tolerance semantics) in `homesynapse-core-docs/governance/` as confirmation-semantics anchors — read what governs before proposing what changes.
7. `nexsys-hivemind/context/research/2026-08-02_A14_attended-hours_charter-input.md` — sizing.

**The verbatim `integration-zigbee` module-info at core HEAD (embedded per the Research-6 rule):**
```java
module com.homesynapse.integration.zigbee {
    requires transitive com.homesynapse.integration;
    requires com.fazecast.jSerialComm; // explicit JPMS module (ships module-info.class); interior-only per D-M92-1
    requires org.slf4j; // plain (implementation-only): Doc 08 §3.3 mandates structured log entries (LTD-15)
    requires com.fasterxml.jackson.databind; // plain (implementation-only): the M9.3 JSON profile loader + device cache; no Jackson type on any exported signature (the D-M92-1 pattern)

    exports com.homesynapse.integration.zigbee;
}
```

**Known hazards:** the ledger confirms on ANY value-matching report (REV-1 F-1/S-2) — your shapes must state their interaction with that path explicitly; the L-E physics lane runs in parallel — reference the physics program as an adjacent charter item, do not scope it; repo-wide greps through the VM mount can time out — scope every search to a module or file.

**Return integrity:** end with a self-audit — sources read, line-cites re-derived at which HEAD, the three weakest claims in your own return, and what a hostile reviewer attacks first.

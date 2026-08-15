<!--
file: context/research/2026-08-15_LF_delivery-evidence-closure_return.md
purpose: L-F return — the delivery-evidence closure (S-1 seam / candidate (iii)/P2): the seam re-grounded at current HEAD, 3 build shapes + the shelf priced (scope · desk-days under A-14 · risk classes · bench · what each retires), honesty semantics per shape under the D5 law, the pre-build instrumentation set, and a ranked PM-adjudicable recommendation.
audience: Hub, Nick, the post-gate charter track (the S-10 window closed before this return landed — see status).
state-type: grounding + build-shape pricing return (point-in-time)
status: DELIVERED LATE 2026-08-15 — after the re-stamped due (2026-08-14 09:00 CT) and after the S-10 close. Per the brief's FINAL STAMP (v51 beat 5): DEGRADE-TO-ABSENT applied at S-10; this file is POST-GATE READING, an input to the post-gate charter items it prices, not to the gate it missed. Filed anyway because the pricing is charter-consumable whenever the closure's build slot is ruled.
provenance: Fresh Cowork lane, read-only. Baselines RE-DERIVED at launch (rule 7): homesynapse-core HEAD = d26777c (dispatch pin 8955e23 SUPERSEDED — every line cite below re-derived); nexsys-hivemind HEAD = 9d91f91 (dispatch pin 4f13e67 superseded). Working-tree-vs-HEAD verified for the six seam-critical core files by git blob hash (hash-object == ls-tree HEAD for EzspCoordinatorProtocol, ZclIngestionUnit, ZigbeeIntegrationAdapter, ZigbeeCommandHandler, StandardPendingCommandLedger, PendingCommand) — cites below are cites at d26777c.
disclosures: (1) The device-bridge staging endpoint rejected the deep Java source paths (HTTP 400, apparent path-length limit); sources were pulled via read-only `tar | base64` streams over the bridge instead — zero writes to any repo, zero scratch files on Nick's disk. (2) `git status` over the VM mount timed out and was NOT run; cleanliness was established per-file by blob hash, not tree-wide — an untracked/dirty file OUTSIDE the six verified files would not have been seen. (3) The nexsys-bench repo was enumerated (scenario/corpus filenames) but its YAML bodies were NOT read; bench numbers herein are from the filed audits as fenced evidence. (4) This file is the lane's ONLY write.
-->

# L-F Return — The Delivery-Evidence Closure: Grounding + Build-Shape Pricing (core @ d26777c)

## Executive summary (≤ half page)

The S-1 seam is re-confirmed at current HEAD, unchanged in substance from REV-1: the adapter requests end-to-end APS acknowledgement on every command unicast (`APS_OPTIONS_RETRY_ROUTE_DISCOVERY = 0x0140`, EzspCoordinatorProtocol:124, stamped per-frame at :1595–1596) and stamps a correlation tag (`messageTag` = the ZCL TSN, :1600), but no `messageSentHandler`/0x003F constant, parser, or consumer exists anywhere in the module; every unrecognized callback — including any 0x3F the NCP emits — is enqueued faithfully (five capture sites), drained each 50 ms cycle, and silently dropped at `ZclIngestionUnit.java:266–268`. Delivered-but-unconfirmed and never-delivered remain indistinguishable, exactly as disclosed.

**Three shapes are priced.** **A — evidence-only** (~3–5 desk-days): parse 0x3F, correlate tag→command, publish delivery evidence; confirmation semantics untouched. The load-bearing discovery of this grounding: the zero-mint carriers **already exist** — `command_result(outcome="acknowledged")` drives an existing, currently-unused DISPATCHED→ACKNOWLEDGED ledger hop (StandardPendingCommandLedger:407–408; PendingStatus:36), and `CommandResultEvent.outcome` is an explicitly open vocabulary ("integration adapters may publish additional protocol-specific strings", CommandResultEvent.java:29–30). One hard fence: any NEW outcome string that is neither `acknowledged` nor in the disposition guard set (:877–882) TERMINAL-MATCHES the in-flight entry and emits `command_confirmation_timed_out` (:409–412) — the guard-set membership review is mandatory, not optional. **B — delivery-anchored confirmation** (~6–9 desk-days): A plus ledger precedence; the buildable form is **negative gating** (a recorded `delivery_failed` blocks/concludes the window — no race), not positive gating (confirm-requires-delivery, an order-sensitive two-input join that races the measured 143 ms–3.7 s report latencies). B retires F-1's headline case (a lost command can no longer be coincidence-CONFIRMED) but NOT the delivered-no-op residual — the C-2 §2 number re-prices, it does not zero. B amends Locked Doc 07 §3.11.2 (named below). **C — first-class DELIVERED phase** (~10–15 desk-days + a frontend-lane cost): widest blast radius, touches the FROZEN v1.1 dashboard read-API contract; not first. **The shelf** stays honest (R-A(a) holds; C-2 §2 stands verbatim) but now has a measured cost: the s31 nightly distribution straddles the window (TIMED_OUT 8/14) and the Aug-9 read banked H-D-vs-H-L as *structurally undiscriminable* with today's instrument — every timeout night stays unclassifiable until delivery evidence ships.

**Recommendation (PM-adjudicable): closure-first is RIGHT, and it means Shape A first** — cheapest, pure observability, lifts measurement (not yet claims), is a strict prerequisite of B and C anyway, and is the only shape sized comfortably inside the A-14 floor's first post-gate weekends. B charters as the second increment, adjudicated on ≥2 weeks of A's nightly evidence. C waits for data. Full ranking and the refutation-welcome counter-case in §6.

---

## §1 The seam, re-grounded at source (core @ d26777c — the audit surface)

Every cite below was re-derived at d26777c this session; the six files carrying load-bearing cites byte-match HEAD (provenance block). Where REV-1's numbers (at 60d3ab5) still hold, that is stated rather than silently re-used.

### §1.1 Dispatch side: what radio truth exists today

The command path is: router → `ZigbeeCommandHandler.handle` (ZigbeeCommandHandler.java:137–222, invoked on the adapter's single-threaded command executor) → `dispatch.send(frame, networkAddress)` (:180; the `ZclDispatch` seam, :68–71, wired to `protocol::sendZclFrame` at ZigbeeIntegrationAdapter.java:378) → `sendZclFrameLocked` (EzspCoordinatorProtocol.java:1326–1344) → `sendUnicastLocked` (:1582–1614).

The only radio truth consumed today is NCP **acceptance** — the boolean decoded from the `sendUnicast` (0x0034, :112) response status:

```java
// EzspCoordinatorProtocol.java:1603–1613
EzspFrame response = executeLocked(FRAME_SEND_UNICAST, parameters,
        DEFAULT_COMMAND_TIMEOUT_MILLIS);
int status = codec.decodeStatus(response.parameters(), 0);
if (status != 0) {
    log.warn("zigbee.aps_unicast_rejected: ...");
    return false;
}
return true;
```

`false` becomes `command_result(outcome="rejected", CRITICAL)` (ZigbeeCommandHandler.java:180–186); `true` publishes **nothing** for a kept (non-DISABLED) confirmation policy — "the confirmation window owns the outcome" (:188–210, the DP-B6 fence). Every adapter publication chains `(correlationId, commandEventId)` — the N-6 BINDING convention (`publishResult`, :336–350).

### §1.2 The evidence is requested, and the correlation key is stamped

`sendUnicastLocked` sets `APS_OPTIONS_RETRY_ROUTE_DISCOVERY = 0x0140` on every unicast (:1595–1596; constant at :124, javadoc :120–123: EmberApsOption RETRY 0x0040 | ENABLE_ROUTE_DISCOVERY 0x0100). RETRY is the end-to-end APS-acknowledgement option; the configured NCP timeout exists exactly for it (`CONFIG_APS_ACK_TIMEOUT = 1600 ms` — the per-command floor, :89–92; default command timeout 2× = 3200 ms, :94). And the per-message correlation key is already stamped:

```java
// EzspCoordinatorProtocol.java:1599–1600
parameters[13] = (byte) apsSequence;
parameters[14] = (byte) apsSequence; // messageTag: mirrors the sequence
```

For command frames the tag IS the ZCL TSN, minted inside the protocol (`sendZclFrameLocked`:1327, `nextZdoSequenceLocked()`), and — the correlation gap — **never surfaced**: the `ZclDispatch` seam returns only a boolean, so `ZigbeeCommandHandler.handle()` drops the tag it never sees. (REV-1's spec item (2) stands verbatim at HEAD.)

### §1.3 The discard: capture is faithful, consumption is a silent `continue`

Every inbound frame with `isCallback()` true — whatever its frameId — is preserved at five sites: the command response loop (`executeLocked`:1452–1454), the production pump (`pumpInbound`:861–864), the NETWORK_UP await (:831), the incoming-message await (:1651), and the scan loop (:1974). All feed `pendingCallbacks` (bounded at `MAX_PENDING_CALLBACKS = 1024`, :135; overflow drops OLDEST with a WARN + running count, `enqueueCallbackLocked`:881–890). The ingestion unit drains the queue first thing each cycle (`drainPendingCallbacks`:757–766 → `ZclIngestionUnit.processCycle`, ZclIngestionUnit.java:250–272; the cycle cadence is `PRODUCTION_CYCLE_MILLIS = 50`, ZigbeeIntegrationAdapter.java:146, driven at :488/:782–783).

The routed frameId set at HEAD is exactly: TC join 0x0024 (:253), child join 0x0023 (:257), key establishment 0x009B (:261–263), incoming message 0x0045 (:266). Then the load-bearing three lines:

```java
// ZclIngestionUnit.java:266–268
if (frameId != EzspCoordinatorProtocol.FRAME_INCOMING_MESSAGE_HANDLER) {
    continue;
}
```

No `0x003F` constant exists anywhere in the module at d26777c (grep over the frame-constant block :99–312 and the full source set — the callback registry is {0x0019, 0x001C, 0x0023, 0x0024, 0x0045, 0x0048, 0x009B}); no per-frameId drop counter exists (REV-1 N-7 stands). So if the NCP emits 0x3F per unicast — the externally corroborated behavior of the bellows-derived lineage this module pins its constants to (:159, :98) — the delivery verdicts arrive, sit briefly in the deque, and evaporate ~50 ms later, every cycle, today.

**Inference boundary, held:** that the NCP emits `messageSentHandler` on owned silicon, and its exact v13 parameter layout, remain INFERENCE (high confidence, externally corroborated via zigbee-herdsman's `ezspMessageSentHandler`; never bench-pinned). The module's own v14 posture is a caution precedent: acceptance is pinned ==13 precisely because "half-right v14 support is a deaf radio that looks paired" (:80–87). The §5 bench pin is therefore a build PREREQUISITE, not a nicety.

### §1.4 The confirmation consumer: `StandardPendingCommandLedger` (read whole, 1091 lines)

The value-match confirm path REV-1 adjudicated is byte-stable at HEAD:

- `onStateReported` (StandardPendingCommandLedger.java:427–452) evaluates EVERY in-flight command on the subject entity whose `targetAttribute` matches the reported key; `expectation.evaluate(value) == CONFIRMED` (:442) removes the entry and queues `state_confirmed` citing that report (:443–444; builder :886–893 — carries `matchType`, e.g. "exact"). `ExactMatch.evaluate` is equality-only (ExactMatch.java:24–28); `turn_on → ExactMatch(BooleanValue(true))` with the 5000 ms capability timeout (StandardCapabilities.java:138–150, the 5000L at :146/:149); the pipeline fallback window is `DEFAULT_CONFIRMATION_TIMEOUT_MS = 30_000` (PendingCommandLedgerAssembly.java:50, AMD-90). No causality, freshness, or edge requirement — F-1/S-2 as banked.
- `onCommandResult` (:388–418): the **disposition guard** (:389–398) skips `superseded | expired_on_restart | unconfirmed | invalid` (`isDispositionOutcome`, :877–882; constants :139–171). `acknowledged` advances the entry to `ACKNOWLEDGED` and records the result event id (:407–408). **Everything else terminal-matches: `remove(tracked)` + a `command_confirmation_timed_out` publication (:409–412).** This is the single most important mechanical fact for shape design: an unguarded new outcome string is not inert — it concludes the window.
- The seams REV-1 called clean are still clean: publish-outside-lock (LTD-11 — publications collected under the lock, flushed after release; `onCommandIssued`:362–381, flush :380), dual-index removal (:647–663), deterministic no-causation fallback (N-6, `findPending`:665–702), supersession (`expireSuperseded`:630–645). The REPLAY half (`accumulateReplay`:503–546, `findReplayKey`:704–719, `classifyRestart`:561–582, `reindexLive`:593–618) still lacks the N-6 ordering and the disposition guard (REV-1 F-7, unswept at HEAD) — every shape below inherits an obligation to state its REPLAY behavior.

### §1.5 As-built carriers a shape can ride (the cheap-path inventory)

1. **`CommandResultEvent.outcome` is an open string vocabulary.** The record's own javadoc (CommandResultEvent.java:22–31): the live vocabulary is `acknowledged | rejected | timed_out | invalid | unsupported | handler_error | integration_unavailable | superseded | expired_on_restart | unconfirmed`, the last four dispositions, and — verbatim — "integration adapters may publish additional protocol-specific strings." A new outcome mints **no** event type, **no** schema, **no** serialization change.
2. **The DISPATCHED→ACKNOWLEDGED hop exists and is unused by the zigbee adapter.** `PendingStatus.ACKNOWLEDGED` ("adapter acknowledged receipt", PendingStatus.java:30–36) and the ledger's `acknowledged` arm (:407–408) are live code with zero zigbee producers today (the adapter publishes only failure verdicts, ZigbeeCommandHandler.java:54–57). Delivery-success can drive an existing lifecycle transition.
3. **`command_dispatched.protocolMetadata` is a minted, empty slot.** `CommandDispatchedEvent` (DIAGNOSTIC) carries a `protocolMetadata` JSON string; the dispatch service publishes it as `"{}"` with the comment "carries no protocol metadata yet (filled by the adapter)" (StandardCommandDispatchService.java:89–90, :217–222). The event model anticipated adapter-side protocol metadata. (Caveat: `command_dispatched` is published by the ROUTER at hand-off, before the adapter runs — the adapter cannot fill THIS event's instance; the slot is a design precedent, not a free carrier. Named to prevent a false-cheap reading.)
4. **The AMD-97 vocabulary already names the failure rule.** `degradeRule` includes `NACK_TO_FAILED` (AMD-97 §1; the S31 profile carries it), and AMD-90's anti-requirement REC-162 names "Zigbee APS" as the transport-owned retry layer — the governance record already treats APS-layer failure as a first-class, engine-retry-free failure class.
5. **The availability fence is instructive, not blocking.** `evaluateAvailabilityTimeouts` documents DP-7: "the dispatch path's boolean is NCP acceptance, not device evidence — wiring it would fabricate liveness" (ZigbeeIntegrationAdapter.java:497–507). An APS ack IS device-originated (the target's APS layer acknowledged end-to-end) — a legitimate FUTURE availability-evidence source, deliberately NOT scoped into any shape below (rider-class only).

### §1.6 The spec'd seam (REV-1 §3 S-1, re-affirmed at HEAD; still spec, not build)

(1) mint `FRAME_MESSAGE_SENT_HANDLER = 0x003F` + a `MessageSent.parse` record in the M9.4-TCJ isolated-constants style (any silicon correction stays a one-constant/one-layout edit), routed in `processCycle` ahead of the :266 filter; (2) correlate `messageTag`→command — the tag is the TSN; the `ZclDispatch` seam must either return the tag or accept a correlation sink, since `handle()` currently drops it; (3) publish delivery evidence chained `(correlationId, commandEventId)` like every other adapter verdict (:336–350). The two design decisions REV-1 assigned to Nick (zero-mint vs minted hop; DELIVERY_FAILED concludes vs annotates) are priced as the A/B variants below rather than presumed.

---

## §2 Build shapes, priced

Pricing basis: A-14 floor 15 h/wk, weekend-anchored, semester from Aug-17 — a "desk-day" here is ~5 focused hours; one weekend ≈ 2 desk-days; effort is honest judgment against comparable landed WUs (M9.4-NCFG: 1 main file + fixtures + 2 tests ≈ 1–2 days; S-5c micro-WU ≈ ½–1 day), not measurement. All shapes are post-gate (gate sovereignty, rule 3) and assume the §5 instrumentation landed first.

### Shape A — evidence-only: record delivery status as observability; confirmation semantics unchanged

**Scope (modules/files):** `integration-zigbee` only, plus a vocabulary decision that may touch one javadoc in `core/event-model`.
- `EzspCoordinatorProtocol`: +`FRAME_MESSAGE_SENT_HANDLER = 0x003F` constant + a parsed `MessageSent` record (tag, status, APS frame echo) in the isolated-constants pattern (:158–164 precedent).
- `ZclIngestionUnit.processCycle`: +one routed branch ahead of the :266 filter → hands (tag, status) to a listener seam (the `IngestionListener` precedent, :106–123); + the N-7 DEBUG per-frameId drop counter (the rider — §5).
- Correlation: a small tag→(correlationId, commandEventId, dispatchInstant) map. The honest wiring: `ZclDispatch.send` (ZigbeeCommandHandler.java:68–71) grows to return the minted tag (or accept a sink) — a package-private seam, no exported-API change; `ZigbeeCommandHandler` registers the mapping post-send; the ingestion branch resolves + removes on 0x3F and publishes via the existing `publishResult` convention.
- `ZigbeeIntegrationAdapter`: wiring only (:346–357, :376–379 region).
- Tests: `EzspProtocolTest` (layout decode), `ZclIngestionUnitTest` (route + counter), `ZigbeeCommandHandlerTest`/a new `DeliveryEvidenceTest` (correlate + publish + orphan cases), FakeNcp scripting in testFixtures.

**Event surface — the A1/A2 fork (Nick's zero-mint-vs-mint ruling, priced):**
- **A1 (zero-mint, recommended):** delivery-success → `command_result(outcome="acknowledged")` — drives the existing DISPATCHED→ACKNOWLEDGED hop (:407–408); entry stays tracked; window unchanged. Delivery-failure → a new outcome string `"delivery_failed"`; **decision fork:** (i) *conclude* — leave it un-guarded so :409–412 concludes the window (honest `rejected`-class semantics; cost: the N-1 event-name oddity extends — a delivery failure renders through a `command_confirmation_timed_out`-typed record), or (ii) *annotate-only* — add it to `isDispositionOutcome` (:877–882; one line + the cross-pin membership test) so the window still runs to its honest timeout. Either way the guard-set review is a NAMED, mandatory step: shipping `delivery_failed` un-reviewed silently makes choice (i). A1's residual cost: `acknowledged` was worded for adapter-receipt; using it for radio delivery is a semantics widening — one docs currency line (CommandResultEvent javadoc + Doc 01 §4.3/Doc 07 §3.11.2 vocabulary notes). Whether that widening needs a micro-AMD or a currency edit is a PM call; this lane did NOT read Locked Doc 07 itself and does not assert the answer (self-audit item 3).
- **A2 (minted):** a new `command_delivery` event type + record. Costs the expensive class by definition: event-model type + registration, AMD (the AMD-92 vocabulary precedent — "this slice mints zero" was a named virtue), read-side derivation review, serialization/test fan-out. Buys a clean name and a place for protocol detail (status code, retry texture). NOT needed for A's goal; defer to C's adjudication.

**Effort:** 3–5 desk-days (A1): 1 day protocol constant/parse/decode tests; 1–1.5 days seam + correlation map + handler wiring; 1 day ledger-guard review + vocabulary line + membership test; 0.5–1.5 days bench leg + fixture scripting + soak review. Two weekends at the floor.

**Risk classes:**
- *Concurrency/interleaving:* the correlation map is written on the command executor and read/cleared on the cycle thread — a genuinely cross-thread structure in a module whose maps are deliberately thread-confined (ZclIngestionUnit class contract :64–66). Bound it, TTL it (entries older than the command timeout expire), and document it; the S-4/F-4 review showed what unguarded cross-thread state costs here.
- *Tag wrap/collision:* the tag is one byte mirroring a wrapping TSN (:1655–1658); at >256 in-flight-tag lifetimes collisions mis-correlate. Mitigation: keyed eviction on resolve + TTL; collision → drop evidence with a WARN (evidence-absent degrades honestly, never mis-attributes).
- *Reopen/reset:* `attemptReopen` → `resetSession()` (:818–851) orphans in-flight tags on a fresh NCP; clear the map on reopen (the `resetSession` cache-clear precedent — `cachedEui64 = null` inside `resetSession()`, :695–704).
- *Queue overflow:* drop-oldest at 1024 (:881–890) can eat 0x3F frames on a chatty network — evidence is best-effort by construction; the honesty rule is "absent evidence stays absent," never inferred.
- *Silicon dialect:* the 0x3F v13 layout is un-pinned (§1.3 boundary); the §5 pin is a prerequisite. v14 remains out of scope (acceptance ==13, :87).
- *Event-model/serialization:* none (A1). *JPMS:* none (module-info untouched; verified verbatim at HEAD, matches the brief's embed). *Migration:* none. *Locked contracts:* none amended under A1-with-currency-line reading; if PM rules the `acknowledged` widening amendment-class, the amendment path is a micro-AMD on Doc 07 §3.11.2's vocabulary note — named here as the cost.

**Bench implications:** red-first per §5. New nightly leg `command-delivery-evidence` (dispatch a confirmable command; assert a delivery-status record chained to the commandEventId exists before terminal phase) — RED on today's build by construction. Nightly bar: 9 legs + 1 (or fold the assert into `command-confirm-s31`; separate leg preferred — it stays green on timeout nights and isolates the new machinery). The S31 corpus validates immediately: mains relay, CONFIRMABLE, measured cadence ~5 min, measured confirm-latency distribution (0.174–3.658 s, TIMED_OUT 8/14 at the ~5.37 s window) — every future timeout night classifies **delivered-late vs never-delivered**, the exact discrimination the Aug-9 read (§6) banked as structurally unavailable.

**What A retires (quantified):**
- The delivery-phase OBSERVABILITY gap: delivered-vs-never-delivered becomes distinguishable in the log for every unicast command. Retired fully (modulo best-effort evidence loss, est. ≪1% of commands on a healthy bench).
- The C-2 §2 coincidence number: **unchanged as an exposure** (~1.7% at 5 s / ~10% at 30 s, toward-current-state only — arithmetic re-verified: 5.19/300 ≈ 1.7%, 30/300 = 10%), but converted from priced-model to **measurable**: a `state_confirmed` whose command carries `delivery_failed`/absent evidence is the coincidence signature, countable per night. A does not shrink the window; it instruments it.
- N-7's class (a month of invisible discarded traffic): retired by the counter rider.

### Shape B — delivery-anchored confirmation: delivery evidence becomes a confirmation input with defined precedence

**Scope:** everything in A, plus `core/automation` (`StandardPendingCommandLedger` + tests), plus a ratified AMD.

**The precedence design fork (the load-bearing choice):**
- **B-i — negative gating (recommended buildable form):** a recorded delivery-failure BLOCKS subsequent value-match confirmation for that command (and, per the A1 fork, concludes the window). Mechanically: on `delivery_failed`, remove/mark the tracked entry; `onStateReported` (:427–452) then has nothing to coincidence-match. No new ordering requirements on the happy path — a fast genuine report still confirms exactly as today; nothing waits for anything.
- **B-ii — positive gating: `state_confirmed` requires delivery-success first.** An order-sensitive two-input join: the measured confirm latencies (0.174 s fastest; the blockR 143 ms settle-class) genuinely race the evidence path (APS ack ≤1600 ms + ≤50 ms drain + bus hop). The ledger would need a held-report buffer or re-evaluation-on-evidence — new state, new crash-window classes (the F-2 pattern re-opens), REPLAY divergence risk. **Priced as NOT the first build:** +2–4 desk-days over B-i and the dominant defect surface, for a residual (below) it does not actually close.

**Locked-contract statement (rule 5, explicit):** B changes the confirmation calculus of Locked Doc 07 §3.11.2 (and touches the AMD-90/AMD-97-governed semantics: the timeout arm interplay, AMD-97-INV-01's never-false-CONFIRMED composition). **B requires a ratified AMD** (AMD-90/97 successor-class: problem statement, precedence table, REPLAY-equivalence clause, invariant candidate "a command with recorded delivery-failure never renders CONFIRMED"). AMD-90-INV-01 binds untouched: `delivery_failed` must never trigger engine retry — remediation stays M8.2 signal-driven, above the engine.

**REPLAY obligation (F-2/F-7 class, explicit):** `accumulateReplay`'s result branch (:519–534) already concludes replay entries on any non-`acknowledged` outcome — a LIVE-concluding `delivery_failed` (B-i with conclude) is replay-consistent for free; an annotate-only `delivery_failed` must be added to the replay-side skip exactly as it is to the LIVE guard, or the rebuild diverges. One rebuild-equivalence test is part of B's price (it also partially discharges REV-1 §6.3).

**Effort:** 6–9 desk-days: A (3–5) + ledger precedence + guard/replay symmetry + tests (1.5–2) + AMD authoring/review cycle (1–1.5, calendar-elastic under the review protocol) + bench legs (0.5–1). Three to four weekends at the floor; the AMD review adds calendar time the desk-days do not capture.

**Risk classes:** A's set, plus: event-ordering assumptions (B-i is ordering-tolerant by design — verify with an interleaving test: report-before-evidence, evidence-before-report, evidence-never); the SKIP-VIS/M7.5a read-side derivation must classify the new outcome (which failure class renders how — a review item, cited as the five-branch law via MODULE_CONTEXT; this lane did not line-audit the derivation); dashboard vocabulary tolerance for an unknown outcome string (frozen v1.1 read API — verify it passes strings through rather than enum-matching; a check, not a known cost).

**Bench implications:** A's legs, plus a red-first `delivery-failure-blocks-confirm` leg (script a FakeNcp DELIVERY_FAILED, inject a same-value periodic report inside the window, assert NO `state_confirmed` — RED on Shape A's build, GREEN on B) — this is the F-1 trigger sequence as a permanent regression pin, buildable entirely on the driven rig (no hardware kill-switch needed). The nightly S31 leg gains a delivered-annotation assert.

**What B retires (quantified — the C-2 §2 re-price):**
- **The F-1 headline case retires:** a command lost at delivery can no longer be coincidence-confirmed — the lost command yields DELIVERY_FAILED (APS retries exhaust ≤ a few seconds, inside both windows), which blocks the match. Residual leakage = coincidence × evidence-absence (callback lost/dropped/un-emitted): ≪0.1% of exposed commands on a healthy network, honestly nonzero, honestly stated.
- **The delivered-no-op residual does NOT retire:** a DELIVERED `turn_on` to an already-ON relay still nets no edge; a periodic same-value report inside the window still exact-matches (:442). The exposure for that class stays ~1.7%/~10% — but its harm re-prices: the record now proves delivery, so the residual dishonesty narrows to report-causality only ("the confirming report may be routine rather than command-caused"), on a command the device provably received, with the state provably matching. The C-2 §2 sentence rewrites accordingly (§4). Full retirement of this residual belongs to the S-2 fix-space (edge/freshness qualifier — REV-1 §6.6), which is COMPLEMENTARY to B, not competing: delivery evidence closes the never-delivered arm; an edge qualifier closes the no-edge arm.

### Shape C — full lifecycle extension: a first-class DELIVERED phase in the command record

**Scope:** B, plus: `PendingStatus` +DELIVERED (exported API of `com.homesynapse.automation` — module name read at source this session; consumed by REST/WS/Observability per the module javadoc), phase-transition record/evidence (A2's minted event or an `acknowledged`-subsumption ruling), the M7.5a derivation + explanation service rendering, REST/WebSocket surfaces, and the dashboard — **the FROZEN v1.1 read-API contract gains a lifecycle phase**, which is a contract version event and a frontend-lane cost (the explainability hero "did it actually confirm?" gains a fourth rung), plus Doc 07 §3.11.2 FSM amendment (superset of B's AMD) and Doc 01 §4.3 lifecycle prose.

**Effort:** 10–15 desk-days across two lanes (core + frontend), plus the AMD and contract-version ceremonies. **Risk classes:** B's, plus exported-enum fan-out (switch exhaustiveness across consumers), read-model/projection review (whether any checkpointed view derives from phase — if yes, `projectionVersion` territory), contract-freeze governance. **Bench:** B's, plus phase-sequence asserts in api-captures (ACCEPTED→DISPATCHED→DELIVERED→CONFIRMED). **Retires:** everything B retires, plus the phase becomes user-visible everywhere — which is a product claim surface, not an honesty necessity. **Verdict texture:** C is the right eventual shape and the wrong first build; nothing in C's extra scope closes exposure B leaves open — it renders it.

---

## §3 The do-nothing shelf option, priced honestly

**What staying disclosed-but-open costs — and what it does not.** The honesty position remains sound; that is stated plainly because it is true: R-A(a) is the ruled, binding reading (CONFIRMED = state-truth on real device evidence); the C-2 §2 limitation stands verbatim as a priced, disclosed edge; the DO-NOT-SAY rail ("no delivery-proof claims until delivery evidence ships… DISPATCHED means hand-off to the radio", voice/tone §6, folded 2026-08-06) holds absolutely; AMD-97-INV-01 and the bench record (never-false-CONFIRMED held across every unattended night, including failing-bench nights) are undisturbed. Nobody is lying to anybody on the shelf.

The shelf's real, now-measured costs:
1. **Every timeout night stays unclassifiable.** The measured s31 distribution straddles the window — TIMED_OUT 8/14 on the available record; the Aug-9 read adjudicated H-D (real device timeout) vs H-L (late delivery) **"UNDISCRIMINABLE by the current instrument… banked as a structural negative result."** The nightly bar will honestly miss ~half of nights at that leg (the v51 gate NOTE), and the record cannot say whether those misses are radio loss, device latency tail, or window sizing — the exact question a window-retune decision needs.
2. **The F-1 exposure stays priced-not-measured** (~1.7%/~10%, toward-current-state only): the model is source-certain, the field rate is unmeasured, and it stays unmeasurable without the evidence.
3. **The claim ceiling stays down**: no delivery-proof sentence, ever, and C-2 Tier-1+ (the public reliability-engineering exhibit) builds on a disclosed hole rather than a closed one.
4. **The N-7 lesson recurs by class**: undiscriminated discard is how S-1 stayed invisible for a month; the shelf keeps the instrument dark.
5. **Cheap-now vs cheap-later:** the seam is unusually cheap today (open outcome vocabulary, unused ACKNOWLEDGED hop, isolated-constants pattern); post-launch, the same build acquires migration/compat weight.

The shelf is a legitimate ranking entry (it is what the product ships at the gate regardless, since all shapes are post-gate) — it is just no longer free.

---

## §4 Honesty semantics per shape (the D5 law: posture and verified fact only)

**Standing rail (all shapes, until the ruled shape SHIPS):** every C-2/§6 sentence below changes only at ship-verification time (the C-2 "re-verify at ship time" convention); nothing changes at charter-ruling time.

**Shape A ships →**
- C-2 §2's chartered-closure paragraph rewrites from future ("is chartered… Until it ships") to shipped-observability: *"The radio-layer delivery evidence the adapter receives is now recorded on every command: delivered and never-delivered are distinguishable in the permanent record."*
- The limitation paragraph KEEPS its number (confirmation semantics unchanged) but gains measurability: *"…priced at ~1.7%/~10%; because delivery evidence is now recorded, coincidence-pattern confirms are detectable and countable in the log."*
- DO-NOT-SAY: the delivery-proof entry **narrows but does not retire**: new sayable — "we record radio-layer delivery evidence for every command"; still never-say — "CONFIRMED proves delivery" (confirmation is not delivery-gated under A). DISPATCHED still means hand-off.
- NEW never-say lines A creates: **"An APS acknowledgement is not state and not execution — delivery evidence never renders as CONFIRMED"** (the ACK-is-not-state rail, structural: A's evidence never touches `onStateReported`); **"Delivery evidence is best-effort observability — absent evidence is absent, never inferred either way"**; **"Delivery evidence is Zigbee-scoped (APS acknowledgement); no cross-protocol delivery claim."**
- The S-10 sweep rule from the Aug-9 read binds every new sentence: each must survive "reports-the-state, not did-the-thing." Delivery evidence adds a rung (reached-the-device) below CONFIRMED (state-truth); neither rung is actuation-proof, and no sentence may ladder them into one.

**Shape B ships →** everything above, plus:
- C-2 §2's limitation sentence REWRITES (the material re-price): from *"a routine periodic report… is indistinguishable from causal evidence"* [for toward-current-state commands generally] to: *"a command that fails radio delivery can no longer be confirmed by a coincidental report; for delivered no-op commands (commanding the state the device already reports), a routine same-value report inside the window remains indistinguishable from causal evidence — ~1.7%/~10% of that narrower class."*
- DO-NOT-SAY retires: nothing fully; the delivery-proof entry narrows again — new sayable: *"a CONFIRMED command with recorded delivery-failure does not exist, by construction"* (cite the invariant + the red-first bench pin). Still never-say: "CONFIRMED proves the command caused the state" (the delivered-no-op residual) and "delivery evidence proves execution."
- NEW never-say B creates: **"never claim the coincidence window is closed"** — it is halved by class, not closed; the edge-qualifier work (S-2 fix space) owns the other half.

**Shape C ships →** B's set, plus DELIVERED becomes a sayable user-facing phase: *"Sent → Delivered → Confirmed, each on its own evidence."* New never-say: **"Delivered ≠ done"** rendered wherever the phase renders (the UI must not present DELIVERED as success-adjacent green; that is a frontend-lane rail).

**Shelf →** C-2 §2 stands VERBATIM; the §6 rail stands ABSOLUTE. That posture is honest and remains defensible — the only D5-law caution on the shelf is drift-by-paraphrase: every downstream consumer keeps inheriting the rail verbatim, because the temptation the record already shows (phase names reading as delivery) grows with every new surface.

---

## §5 Pre-build instrumentation: the N-7 counter rider + the 0x3F bench pin (red-first)

Ordered; 1–2 are prerequisites of ANY shape, 3 is the red-first baseline itself.

1. **The 0x3F bench pin (REV-1 §6.2; one read-only Pi-trip item).** One logged drain naming callback frameIds during a command burst on owned silicon: does 0x3F arrive per unicast, and what is its v13 byte layout (tag/status offsets)? This converts §1.3's INFERENCE to FACT before a line of build code exists. Cheapest form: a temporary DEBUG at the drain (or the item-2 counter itself) + one attended command session; joins the standing Pi-trip block (with the S-4 residual grep, per the v45 beat-7 disposition).
2. **The N-7 counter rider (the DEBUG per-frameId dropped-callback counter at ZclIngestionUnit:266–268).** A one-evening change that should land as the FIRST commit of the build WU (post-gate; nothing pre-freeze — the freeze has passed and gate sovereignty holds). It is the standing instrument that would have surfaced S-1 a month early, and it is the red-first exhibit: **before** the build, the counter shows 0x3F arriving-and-dropped every command night (RED — the gap, measured); **after** Shape A, the 0x3F count moves to the delivery-evidence record (GREEN). The counter also permanently guards the next unknown frameId.
3. **The red-first bench leg** (`command-delivery-evidence`): asserts a delivery-status record chained to the command's eventId. Runs RED against today's core by construction; flips GREEN with Shape A. This is the leg that gives the build a falsifiable acceptance bar instead of a narrative one. Shape B adds the second red-first leg (delivery-failure-blocks-confirm, the scripted F-1 trigger — §2/B).
4. **The redesigned s31 instrument (the Aug-9 §6 candidates)** — settle transition-assert, settle deferral ≥1 native report interval, native-interval measurement — is a SEPARATE post-gate WU, but it composes: with delivery evidence recorded, the redesigned leg's timeout nights self-classify (delivered-late vs never-delivered), and the S-10-noted window-sizing-vs-honest-terminal decision gets its missing datum. Sequence the s31 redesign AFTER Shape A so the new instrument is born with evidence.
5. **Nightly bar statement:** bar becomes 10 legs · 1 SKIP(hue) with the delivery leg separate (preferred: isolates new machinery; keeps the s31 leg's distribution history uncontaminated). The S31 corpus (fixtures + measured cadence + confirm-latency distribution) already suffices to validate A's correlation and B's blocking logic on the driven rig — no new hardware, no new corpus capture required for acceptance; the corpus's ACK→report reference-point caveat (AMD-97 consumption contract) transfers verbatim to delivery-latency assertions.

---

## §6 Recommendation (ranked; PM-adjudicable — the charter rules, this lane advises)

**Ranking:**
1. **Shape A (evidence-only), first post-gate build in the closure track.** Cheapest (3–5 desk-days; two floor-weekends), zero Locked-contract amendment on the A1 reading, zero event-model mint, pure observability with honest degrade, converts the C-2 exposure from modeled to measured, unblocks the s31 timeout-night classification the record explicitly lacks, and is a strict prerequisite of B and C anyway — nothing built in A is thrown away under any later ruling. Preconditions: §5 items 1–2.
2. **Shape B-i (delivery-failure blocks confirmation), chartered NOW as the named second increment, built after ≥2 weeks of A's nightly evidence.** The data gate is deliberate: A's soak measures evidence reliability (0x3F arrival rate, orphan rate, overflow incidence) — the exact unknowns B's correctness rests on — and the AMD authoring can run in the same window. B-ii (positive gating) is NOT recommended in any near increment.
3. **The shelf** — ranked above C for the first increment window, below A/B overall: honest but now carrying measured costs (§3). If the charter defers the whole track, the §5 instrumentation should land anyway; it is shelf-compatible observability of the gap itself.
4. **Shape C (DELIVERED phase)** — correct eventual surface, deferred until B's field data says the phase earns a frozen-contract version bump; the frontend-lane cost makes it a two-lane charter item.

**Is closure-first RIGHT? (refutation-welcome, both directions argued.)** The honest case AGAINST closure-first: the honesty position is already sound and ruled (R-A(a)); no user-facing falsehood exists to fix; the A-14 floor is thin in-semester and the wider physics program (L-E's lane) competes for the same weekends; the 0x3F emission is still un-pinned, so the build could stall on silicon reality. The case FOR: every one of those objections is answered by Shape A specifically — it is sized for thin weekends, its silicon risk is discharged by a read-only pin BEFORE commitment, it changes no ruled semantics, and it is the piece every alternative future (B, C, edge-qualifiers, availability riders, the s31 instrument redesign) consumes. The one genuinely competing first-build is the S-2 edge/freshness qualifier (REV-1 §6.6's fix-space memo): it attacks the OTHER half of the coincidence window and needs no silicon. Adjudication texture: the edge qualifier alone leaves never-delivered invisible (the honesty-critical class — silent delivery failure masked); evidence-only alone leaves the delivered-no-op arm (the softer class) — and A additionally buys observability the qualifier does not. **Closure-first, meaning Shape-A-first, survives the refutation; the full-lifecycle reading of closure-first (C-first) does not.** One-word form for the ruling: shape (A / A+B chartered / shelf / C) — this lane's word is **A+B-chartered**.

---

## Return integrity — self-audit

**Sources read (in the brief's order):** REV-1 physics-spine return (whole, 133 ln) · REV-1 audit v45 beat 7 (whole) · core sources at d26777c: EzspCoordinatorProtocol (constants/keepalive/drain/pump/execute/sendZclFrame/sendUnicast regions + full grep sweeps), ZclIngestionUnit (whole, 687 ln), ZigbeeIntegrationAdapter (init/run/close/cycle/availability/productionLoop/attemptReopen regions), ZigbeeCommandHandler (whole, 355 ln), StandardPendingCommandLedger (whole, 1091 ln), plus StandardCommandDispatchService (whole), CommandResultEvent/StateConfirmedEvent/CommandIssuedEvent/CommandDispatchedEvent/EventTypes/PendingStatus/PendingCommand/PendingCommandLedgerAssembly/ExactMatch/StandardCapabilities(onOff)/Confirmability/ConfirmationCharacterization/CommandEnvelope, zigbee-profiles.json (S31 block), both module-infos (integration-zigbee matches the brief's embed verbatim; `core/automation` = `com.homesynapse.automation`, read at source per Research-6) · MODULE_CONTEXT.md (headers walked; Consumers/Constraints/Gotchas whole; M9.2/M9.4b delta rows; delivery/messageSent greps — no 0x3F entry exists) · C-2 Tier-0 draft (whole) · AMD-90 + AMD-97 (whole; located in homesynapse-core-docs/design/amendments/, NOT in governance/ as the brief's source list implied — Design_Review_Amendments_v1.md in governance/ carries AMD-01–10-era content) · A-14 (whole) · voice/tone platform §6 (the delivery rail verbatim) · s31 evidence reads Aug-2 / Aug-9 / Aug-10 (whole; the H-L→L-F routing and the H-D/H-L negative result consumed as fenced evidence) · nexsys-bench scenario/corpus filenames only (disclosure 3).

**Line-cites re-derived at:** core `d26777c` (all Java cites; six seam files additionally blob-hash-verified working-tree==HEAD), hivemind `9d91f91` (audit/strategy quotes), docs read at current mount state. The REV-1 numbers quoted as REV-1's (e.g., its :427–452) were independently re-confirmed at d26777c where load-bearing.

**The three weakest claims in this return, named:**
1. **0x3F emission + v13 layout on owned silicon is still INFERENCE.** Externally corroborated, never bench-pinned; if the Sonoff MG24's EZSP v13 dialect diverges (the module's own v14 caution is precedent for exactly this class), Shape A's decode step re-prices — the ranking survives (the pin runs before commitment), the desk-day number may not.
2. **Effort pricing is calibrated judgment, not measurement.** Anchored to two landed-WU analogies (M9.4-NCFG, S-5c) and the A-14 floor, but no historical desk-day ledger exists for this codebase; the AMD review-cycle calendar cost in B is especially soft.
3. **The A1 "no Locked amendment" reading rests on NOT having read Locked Doc 07 §3.11.2 itself.** The claim that `acknowledged`-as-delivery-success is a currency-line widening rather than an amendment is derived from the code-side vocabulary javadoc (an open string set) and AMD-90/95/97's treatment of the confirmation surface — if Doc 07's Locked text binds `acknowledged` to adapter-receipt semantics explicitly, A1 acquires a micro-AMD and ~½–1 desk-day. The fallback (a new guarded `delivered` string instead of `acknowledged`) is priced inside A's range either way.

**What a hostile reviewer attacks first:** the lateness — this return missed its stamped due and the S-10 close, and no pricing quality repairs a lane that wasn't on disk at adjudication (owned; the DEGRADE-TO-ABSENT consequence is recorded in the status block, and this file claims post-gate-input status only). Second: weak-claim 3 (the Doc 07 reading) — it gates whether Shape A is truly amendment-free, and the return's cheapest-shape argument leans on it; the defense is that both branches of the fork are priced and neither moves A out of first place. Third: the residual-coincidence arithmetic under B assumes DELIVERY_FAILED reliably fires for lost commands (APS retries exhausting) and independence of evidence-loss from coincidence — both plausible, neither measured until A ships; the numbers are labeled model-not-measurement wherever they appear.

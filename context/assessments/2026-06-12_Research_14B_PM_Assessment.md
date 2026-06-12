<!--
file: context/assessments/2026-06-12_Research_14B_PM_Assessment.md
purpose: PM assessment of Research 14-B (Automation Engine Runtime — Robustness Prior Art, REC-156..170) — 6-step A–F, source-verified against Doc 07 actual text at docs HEAD (the researcher worked from brief embeds; connector unreachable, declared). FOLDED FIRST per the serialized order (B → A → 15).
audience: PM, Nick
state-type: assessment
status: COMPLETE 2026-06-12 — grade A−; 12 ACCEPT (5 narrowed/sharpened) + 1 REJECT-as-bucketed + 2 FUTURE-AMD; zero discards; all dispositions confirmed or narrowed, none overturned
anchors: context/instructions/Research_14B_Automation_Runtime_Robustness_Brief.md (the brief); raw return at docs research/returns/ (archived at this closeout); context/assessments/2026-06-12_W0_Research_4_Currency_Delta.md
-->

# Research 14-B — PM Assessment (engineering register; folded FIRST)

**Return:** "Research 14-B: Automation Engine Runtime — Robustness Prior Art" (2026-06-12). **RECs:** 156–170 (15 — full range used, none exceeded). **Researcher venue note:** the DOCS connector was unreachable in-run; the researcher worked from the brief's §0.2/§0.3 embeds, declared it per protocol, and reconstructed nothing — the §5 escalation asked the PM to verify the non-embedded anchor text. **Done: this assessment source-verified Doc 07 §3.10/§3.11 actual text** (the load-bearing anchors) before ruling.

## Step 0 — Quote-back gate: **HONORED**
(a) module-info byte-faithful ✓ (b) inventory line verbatim incl. the 30-permit re-derivation note ✓ (c) all six decided-ground rows verbatim ✓. Return admitted past §0.

## Steps A–C — Format / Summary / Cross-cutting: **PASS, STRONG**
All mandatory sections; §7 LIGHT and routed through §4b; one document. Executive summary: 7 verdict bullets, all positioned; highest-impact (monotonic clock) and nastiest-window (W1 dispatch/ledger) flagged as required. §3.2 crash-window table (W1–W8, named, dispositioned) is exactly the charter's carry-pin deliverable. §3.4 honesty section produced two genuine REJECT rulings and defended the 3-subscriber model rather than reflexively endorsing it. Register discipline held (one out-of-register note, §5, one line).

## Step D — REC dispositions (PM rulings; source-verified)

**The PM verification pass read Doc 07 §3.10 + §3.11.1/§3.11.2 in full.** Key discovery: the Locked text is RICHER than the brief's embeds — §3.10 specifies REPLAY→LIVE timer re-creation with **remaining duration** (`original_for_duration − (current_time − timer_start_time)`, fire-immediately if ≤0) and **zombie-Run finalization** (`final_status: interrupted_by_crash`, C1 restoration, ledger recovery explicitly not blocked by Run finalization); §3.11.2 specifies **per-idempotency-class crash recovery** (IDEMPOTENT re-issued after LIVE; NOT_IDEMPOTENT → `expired_on_restart`; CONDITIONAL → adapter evaluation) and **event-driven confirmation** (incoming `state_reported` evaluated via `Expectation.evaluate()`; `confirmation_timeout_ms` carried per command from the event payload). This strengthens several ALREADY-COVERED floors and narrows four RECs below. No disposition is overturned.

| REC | Researcher bucket | PM ruling | PM modification |
|---|---|---|---|
| 156 monotonic sustain arithmetic | M7-OBLIGATION | **ACCEPT (sharpened)** | Implementation must route monotonic reads through an **injected seam** — raw `System.nanoTime()` trips `NO_DIRECT_TIME_ACCESS` (the M2.4 lesson); replay-time sustain decisions derive from event-time per §3.10 (the cross-restart remaining-duration arithmetic is wall-clock BY LOCKED DESIGN — monotonic discipline applies to live in-process elapsed measurement only) |
| 157 storm-simulation test | M7-OBLIGATION | **ACCEPT (narrowed)** | A benchmark/spike harness with §10 targets as investigation triggers — NOT a hard CI gate (§10 targets are investigation triggers per Phase-3 rules; a Pi-4 perf assert in `./gradlew check` would be flaky) |
| 158 same-automation cycle detection | M7-OBLIGATION | **ACCEPT** | Rides the REC-36 `RunCausalChain` AMD-block item; distinct diagnostic = a NEW event type → manifest fan-out + survey (W0 §2.5 obligations apply) |
| 159 REPLAY→LIVE cross-subscriber barrier | M7-OBLIGATION | **ACCEPT (narrowed)** | §3.10 already gives each subscriber per-mode suppression AND specifies zombie-Run-vs-ledger ordering ("command recovery is not blocked by Run finalization"); Doc 12 already sequences automation-after-state-store. The remaining genuine pin: **LIVE-transition interleaving across the three subscribers** (e.g. ledger re-issues IDEMPOTENT commands at its LIVE while dispatch is still in REPLAY) — carry as the narrowed pin |
| 160 dispatch/ledger atomicity (W1) | M7-OBLIGATION | **ACCEPT (anchor sharpened)** | The spec mechanism ALREADY EXISTS (§3.11.2 crash recovery, per-idempotency-class) — W1 is CLOSED-UNTESTED, not OPEN; the obligation is the kill-mid-flight test asserting the per-class behavior (no silent double-dispatch for NOT_IDEMPOTENT; IDEMPOTENT re-issue exactly once post-LIVE) |
| 161 deadline default policy | M7-OBLIGATION | **ACCEPT (narrowed + merged)** | §3.11.2 already carries per-command `confirmation_timeout_ms`; the per-action surface is REC-33's `ConfirmationPolicy` (already ACCEPTED, M7 AMD block) — REC-161's NEW content is the **default-value calibration spike** (Pi-4 Zigbee/Z-Wave round-trips) + the config key default. Fold into the REC-33 AMD item |
| 162 no engine-level retry | REJECT | **ACCEPT as REJECT-bucketed** | Correctly bucketed: the pipeline records REJECTs as anti-requirements (brief §5); the MQTT/Zigbee transport-layer-retry evidence is the recorded reasoning |
| 163 transport-ack ≠ CONFIRMED test | M7-OBLIGATION | **ACCEPT** | §3.11.2 step 2/3 confirm the layering (acknowledged → awaiting-confirmation; only `Expectation` satisfaction confirms) — test pins it |
| 164 confirmation-by-stale-state test | M7-OBLIGATION | **ACCEPT (mechanism corrected)** | The researcher framed it snapshot-relative; the Locked mechanism is **event-driven** — confirmation evaluates incoming `state_reported` (§3.11.2 step 3), not the AMD-03 trigger snapshot (which governs conditions). Corrected test: a `state_reported` that predates the command (stale device report) must not satisfy the Expectation — anchor confirmation to log-position/event-time relative to `command_issued` |
| 165 `definitionHash` mid-flight-edit test | M7-OBLIGATION | **ACCEPT** | §3.10 determinism note: hash mismatch on replay → diagnostic warning (specified); test interacts with §3.3/C7 reload-preserves-in-progress-runs — both behaviors pinned in one test |
| 166 Tier-2 misfire/DST field shape | FUTURE-AMD | **ACCEPT** | Quartz/cron/systemd taxonomy is the right design space; parked for the Tier-2 `TimeTrigger`/`SunTrigger` promotion |
| 167 DST-spanning `forDuration` test | M7-OBLIGATION | **ACCEPT** | Pairs with 156; cron/HA evidence solid |
| 168 per-automation trigger-eval rate limit | FUTURE-AMD | **ACCEPT** | Correctly identified that `maxConcurrent` bounds runs, not evals; contract delta parked |
| 169 storm×cascade coupling observability | M8-OBLIGATION | **ACCEPT** | M8 row (could alternatively ride the observability milestone — synthesis re-checks at M8 scoping) |
| 170 recovery thundering-herd bound | M8-OBLIGATION | **ACCEPT (watch-note)** | M8 is defensible (dev-scale M7 won't saturate); WATCH: if M7.2 recovery tests show Pi-4 SQLite pressure, promote to M7 hardening |

**Summary: 15 RECs → 12 ACCEPT into obligations (5 narrowed/sharpened) · 2 FUTURE-AMD · 1 REJECT (recorded as anti-requirement). Zero discards; zero guardrail violations.**

## Step E — Error inventory / fabrication check
Zero fabricated HomeSynapse identifiers (all from embeds, used precisely — `DurationTimer` keying, `PendingStatus` values, the three subscriber names, LTD-01/03/11 all correct). The researcher self-flagged the one external-identifier nuance (Quartz `MISFIRE_INSTRUCTION_FIRE_ONCE_NOW` vs tutorial prose "FIRE_NOW") — the §3.6 verbatim-vectors discipline working as intended. One mechanism imprecision (REC-164's snapshot framing — corrected above, did not affect the disposition). The connector-unreachable deviation was declared, scoped, and escalated correctly; embeds proved sufficient for all verdicts (PM verification confirmed every ALREADY-COVERED floor against real text — none was optimistic).

## Step F — Grade and process notes

**Grade: A−.** Register discipline, quote-back, disposition-table honesty (bucket-emptiness reasoned), and the crash-window table are exemplary; evidence is overwhelmingly primary-source. Docked: the connector miss (environmental, but it left §3.10's zombie-Run and §3.11.2's idempotency-class recovery machinery undiscovered — two of its "OPEN" framings were actually CLOSED-UNTESTED, caught at PM verification), and the REC-164 mechanism imprecision.

**Process notes for the pipeline:** (1) The embed-authoritative fallback WORKED — a connector-blind run still produced zero fabrications and zero discards; credit the §0 quote-back + verbatim embeds. (2) For future briefs: embed the REPLAY-behavior table (§3.10) at quote granularity when recovery semantics are in scope — it is the densest contract surface and the one place the embeds ran thin. (3) The W1–W8 window names enter the M7 carry-pin vocabulary as-is.

**Feeds:** the M7 AMD block (REC-158 rides REC-36; REC-161 rides REC-33; REC-162 anti-requirement), the M7.x instruction test obligations (156/157/160/163/164/165/167 + the narrowed 159 pin), M8 rows (169/170), FUTURE-AMD queue (166/168). Charter population: this return resolves the ⟨R14-B⟩ markers — see the charter skeleton update at this session's closeout.

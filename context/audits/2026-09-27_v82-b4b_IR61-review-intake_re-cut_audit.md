<!--
file: context/audits/2026-09-27_v82-b4b_IR61-review-intake_re-cut_audit.md
purpose: The v82 beat-4b audit (an addendum after the close, before IR-61 dispatched) — the independent review of the IR-61 instruction intaken at the bytes; every cite re-opened at core `e96dce8`; the instruction and its pre-verification RE-CUT; the review's queue items registered.
audience: the hub (the record) · Nick (§0) · the v83 hub
state-type: intake audit
status: FILED — v82 beat 4b (Sun 2026-09-27 ~15:4x CT; instrument 2026-09-27T20:41:12Z)
-->

# v82 beat 4b — the IR-61 independent review intaken; the instruction re-cut (Sun 2026-09-27 ~15:4x CT)

## §0 The verdicts
- **The review** (`_scratch/v81/sun0927/2026-09-27_IR61_independent-review.md`, 13,104 B, sha256 `49be7906adc03a01…`; filed as `context/audits/2026-09-27_IR61_independent-review.md`): **every claim the hub re-opened holds** (§1). A1–A3 and B1/B3 folded; the instruction RE-CUT before dispatch (§2); C1–C5 registered (§3). The dispatch contract (§14) changes one word (thirteen rows).
- **What the hub's own cut got wrong:** the 180-s figure was derived from the CHAR's observed cadences — firmware chatter on voltage/current the core never asked for — while the core's own contract (`METERING_ROWS`: `ActivePower` 5–600 s, the 600-s maximum "the heartbeat that proves a quiet load is a live meter") entitles a compliant plug to 600 s of silence under a steady load. THE DERIVATION RULE replaces the number: a margin × the configured maximum, never an observed cadence → `power_meter` 1200 s, `energy_meter` 7200 s. The honest headline: a wedge surfaces within 20 minutes; before IR-61 it never surfaced.
- **THE ONE-WAY-DOOR REVIEW (D-v82-10) earned its second exhibit today**: two instructions, two independent reviews, two product-level defects caught before a lane ran (the Hue's stranded temperature; a staleness default that would false-flag a compliant plug ≈ 70 % of every heartbeat period).

## §1 The claims at the source (core `e96dce8`)
| Claim | The instrument | Result |
|---|---|---|
| A1 — `METERING_ROWS` configures `ActivePower` at max 600 s (1-W change) and Summation at 3600 s; the javadoc's heartbeat sentence; voltage/current unconfigured | `ReportingConfigurator.java` :100–:115 (`new MeteringRow(…ACTIVE_POWER…, 5, 600)`, `(…CURRENT_SUMMATION…, 5, 3600)`; :104 "is the heartbeat that proves a quiet load is a live meter"); `grep -n 'METERING_ROWS'` :106, :241 | CONFIRMED |
| A2 — `MeasureReadPathIT` seeds a `state_reported` with `power_w` on the rig's GEN4 and reads `core.stateQueryService().getSnapshot()`; `stateQueryService()` public | `MeasureReadPathIT.java` :72, :152, :334, :435; `HomeSynapseCore.java` :1154 | CONFIRMED (`LinkReadIT` reads log lines — the wrong sibling) |
| A3 — the two projections subscribe independently; `awaitRegistryProjectionLive()` after both; the registry copy-on-write under a lock | `HomeSynapseCore.java` :601–:608 (the registry subscriber), :619–:636 (the state projection), :668; `InMemoryEntityRegistry.java` :15, :37, :44 (`ReentrantLock`) | CONFIRMED — the replay-order property is real and self-healing |
| A3 — `EntityState`'s staleness javadoc in the read set but not the write set | `EntityState.java` :56–:61 | CONFIRMED → row 13 |
| B1 — `CustomCapability` is the 17th record and not in `all()` | `grep -c 'implements Capability'` = 17; `sed -n '68,86p' StandardCapabilities.java` → 16 entries, no custom | CONFIRMED |
| D — the fifteen pre-verification rows; the `state_reported` branch; `recomputeStale`; the three `create` callers; ArchUnit direction | re-read at the b4 cut | CONFIRMED |

## §2 The re-cut (the instruction 27,376 → 32,976 B; the pre-verification 15 → 18 rows)
The masthead (the rule; the review named; the headline); §1 (b)/(c)/(e); §2's read set (`MeasureReadPathIT`, the rig, `METERING_ROWS`, the composition root's subscription order); §3 rows 2 (the resolver takes the catalog and indexes it itself; `CustomCapability` contributes nothing), 5 (`PowerMeter` 1200 s + `EnergyMeter` 7200 s with THE DERIVATION RULE in the javadoc), 10 (T5 both; T5b 14 of 16), 11 (T6 in `MeasureReadPathIT`'s shape), +13 (`EntityState` javadoc); DP-2, DP-3 (the replay-order property stated; T2b), DP-5, DP-6 (THE DERIVATION RULE and the numbers; the 20-minute headline); §7 (every number; T2b; T5 for both; T6's shape; the red-first prediction); §8; §9 (three bullets); §10 (the margin; the rule's refutable-by); §12; §14 (thirteen rows). WU-IR61 rows 16–18 (the contract; T6's sibling; the replay order).

## §3 The review's queue items → the register
IR-78 (B2: the 13-parameter `create` overload — a `ProjectionDependencies` record, the next state-store unit) · IR-79 (C2: a never-reporting adopted device is invisible to staleness — `staleAfter = registeredAt + threshold` at registration is the AMD's candidate; the seed read IR-68 closes most of it) · IR-80 (C1: THE AMD to Doc 03 §3.8 — source 2b, the device's VERIFIED reporting configuration per attribute (2 × the read-back max when VERIFIED_REPORTS; the capability default otherwise); it retires the constants, answers the IR-18 review's C2, serves the `reporting:false` presence sensor; the posture fact lives in integration-api and the state store must not depend on integration — the AMD decides how the fact travels; cut Tuesday at the strategy pass) · IR-81 (C5: the docs deltas for IR-61 — Doc 03 §3.8's status, AMD-53 :78 "not yet wired" → wired, Doc 02 §3.5 the declaration and the derivation rule). C3 (IR-61b's scope: the §9 keys, 0 hits today; the scan; the two events by the frozen contract's additive path; whether the dashboard renders `stale` at all) → IR-61's row amended. C4 (VERIFY-72H's attestation in falsifiable form: with 1200 s, zero `stale: true` on any plug whose store rows show reports within 1200 s; any `stale: true` coincides with a store silence ≥ 1200 s; the bench keeps `fresh_within_s` as the REP gate and reads `availability` beside `stale`) → the charter's gate text (v83).

## §4 Not re-executed, disclosed
`MeasureReadPathIT`'s harness beyond the four lines cited (the Coder reads it whole); the review's byte-level re-verification of WU-IR61 rows 1–15 (the hub's own at b4 stands).

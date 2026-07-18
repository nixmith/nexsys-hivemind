<!--
file: context/process/2026-07-18_compounding-testing-doctrine.md
purpose: The compounding-testing doctrine — the operating charter for how NexSys tests, why every test asset must compound, and how the testing program IS the trust brand's manufacturing process. Discharges Nick's 2026-07-14 charge (pm-handoff v31 beat 2, verbatim-anchored below). Consumed by: every bench/scenario WU (B2+), the Coder + PM skills (pointers), the M14+ integration programs, and the B4/B5 data-value rows.
audience: PM hub, Coder, bench lanes, Nick (the executive read, §7).
state-type: process / doctrine.
status: CURRENT — authored 2026-07-18 (v32 hub, close-out) with the doctrine's first exhibits already field-proven. Volatile numbers cited here are dated evidence exhibits, not live state — re-derive at the spine.
-->

# The Compounding-Testing Doctrine

**The charge (Nick, 2026-07-14, recorded v31 beat 2):** proactive test architecture, compounding gains and metrics, rigor in software AND hardware testing — *"so our users can rely on us."* This document is that charge made operational.

## 1. The thesis: verdicts are a monotone asset

Every recorded verdict is permanent evidence capital. The certified corpus stood at ~1,728 recorded verdicts with ZERO false CONFIRM at the 2026-07-13/14 close; it has only grown since, organically, every day the bench runs. The asset only appreciates because the collection substrate is the event log itself (immutable, replayable, fsync-durable — proven by accident on 2026-07-16 when a power cut destroyed the log *file's* tail but every event survived, queryable days later). The rule: **never design a test whose evidence evaporates.** Scenario bundles, event positions, and quoted outcomes are the currency; screenshots and vibes are not.

## 2. The ratchet rule

**Every field incident becomes a scenario or fixture BEFORE its fix ships.** No exception, no deferral. The exhibits to date: the reopen-locator defect → the `usb-reenumeration` scenarios (six silicon reps, a reproducible 16–17 s signature); the liveness false-FAIL class → B1-REV2's `new_run_after` with mutant-killer fixture pairs; the silent-skip class (2026-07-18) → the BENCH-PRECOND row + the SKIP-VIS WU's test obligations; the power outage → the POWER-RESTORE scenario class + BENCH-AUTOSTART. A fix without its ratchet scenario is a regression waiting to reintroduce itself.

## 3. Instrument semantics are part of the system

The instrument that measures the system is engineering, held to the same bar:

- **Fixture-paired asserts (STANDING RULE, the v31 mint):** every new assert ships with fixtures proving its PASS *and* its false-verdict boundary, mutation-verified — a mutant deleting the condition must flip the verdict. Field validation: the REV2 assert's first live rep refused a COMPLETED-but-empty run and forced the silent-skip discovery. The old assert would have failed identically and taught nothing.
- **Evidence-quoting verdicts:** every verdict line names its evidence (runIds, timestamps, M_observed, per-item ignore reasons). A verdict that cannot be adjudicated from its own output is not a verdict.
- **Instrument self-identification:** the tool states what version it is (the RUNNER-VERSION-BANNER row) — the 2026-07-18 stale-instrument hour is the price of assuming; deploy-state is re-derived at the instrument, never from an ordered sequence.
- **Resolution-awareness:** every instrument has a measurement resolution (availability resolves at ping-scale — minutes). **The bench out-waits its instrument's resolution**; an experiment shorter than the evidence cadence measures nothing, honestly.

## 4. The composition tier: history-seeded testing

The 2026-07-18 silent-skip arc defined a new defect class: **correct components, invisible composition, under state history.** In an event-sourced system, behavior is a function of the entire log — a four-day-old availability event lawfully governed every automation run across three reboots, invisibly. Unit tests prove components; milestone gates prove integrations; the missing tier is **scenarios seeded with adversarial-but-lawful history** (an offline verdict in the log, a superseded chain, a relink storm, a half-adopted device) asserting the system *tells us* what that history makes it do. The bench's captured-stream/seeded-log architecture was built for exactly this tier. B2+ scenario authoring treats "what does the log already carry?" as a first-class scenario parameter.

## 5. Metrics that only go up

The program maintains a small set of ratchet metrics — numbers that must never regress, re-derived from evidence at every gate:

- **Zero false CONFIRM / zero false ALIVE** — the one-way doors (currently: zero across the entire recorded corpus).
- **The verdict corpus size** (monotone by construction).
- **The scenario census + the fixture-pair census** (every mechanic proven both directions).
- **The measured envelopes** (dated exhibits, tightened only by better evidence): boot→radio-up ~11–13 s · boot→availability +37 s/+56 s · trigger→first-dispatch ~90 ms · reopen 16–17 s (×6) · offline-declaration ≤ ping window (measured 47 s / ~7 min / ~11.5 min — phase-dependent) · warm re-availability 0.7 s · cold-start (dead-air) recovery ~50 min · per-class confirm envelopes (the corpus's per-device data).

A metric that regresses is a STOP, not a footnote.

## 6. The Data Value Engine coupling

The corpus compounds into shipped product intelligence: device profiles, confirmation tunings, reporting postures, and recovery envelopes are *product data* — the measured truth about real devices that ships in `zigbee-profiles.json` and the device corpus. B4 (the labeled-tuple corpus) and B5 (advisory-only ML) ride ONLY this substrate, inside AIOT-INV-1 (AI is never an autonomous actuator). This is the Data Value Engine thesis made concrete: the bench is not a cost center — it manufactures the dataset competitors would have to run years of hardware to reproduce.

## 7. The executive read

This doctrine is the trust brand's manufacturing process. The product's promise — honest verdicts, honest availability, honest explanations — is only as credible as the evidence machine behind it, and this doctrine makes that machine compound: every field incident becomes a permanent scenario, every scenario feeds the corpus, every corpus entry sharpens the shipped intelligence, every bench night makes the next one stronger and the moat deeper. When the project renames (the R-1/G-2 program) and when M14+ adds integrations, the doctrine transfers unchanged — it is substrate, not branding. Rigor in software and hardware alike, so our users can rely on us.

<!--
file: context/audits/2026-09-21_v78-b2_pelton-ready_link-read-charter_audit.md
purpose: The v78 beat-2 audit — the b1 landing verified at porcelain; PELTON-READY cut as the H10 card (STEER 1); LINK-READ authored through THE PREMISE GATE with every mechanism row grepped at `13d439f` (the rows below); Nick's two steers ruled (D-v78-1, D-v78-2); the research files' copy step named; the SHAKE card written and scheduled at its time; Check 6 kept current (the coder-handoff stamped on the dispatch).
audience: the hub · Nick (§0) · the v79 hub
state-type: audit (filed)
status: FILED v78 beat 2 (Mon 2026-09-21 ~12:0x CT; instrument 2026-09-21T17:07:25Z)
-->

# v78 beat 2 — PELTON-READY; LINK-READ through the gate; the steers ruled

## §0 Verdict
`HIVE: LANDED 63baa87` verified (HEAD `63baa87`, porcelain 0, unpushed 0). PELTON-READY ARMED at `context/strategy/2026-09-21_PELTON-READY_H10-ruling-card.md` (7,439 B; no name token bound; the three classes with the letter-sentence test, the acts each unlocks, eight results-consult questions, NAMING-B as the fallback in every class). LINK-READ DISPATCH-READY at `context/instructions/2026-09-21_coder-lane_LINK-READ_per-device-frame-counter_link-reading-on-silence_coding-instruction.md` (18,734 B) — the plan §2 row 5 as the record defines it (the counter, the reading on every silence, the sampling rule), the read surface and the event's v2 split off as LINK-READ-2 (IR-45) so the unit is one lane-day and touches no entity count before Thursday. D-v78-1 ACCEPT; D-v78-2 ACCEPT with a condition. The SHAKE card at `_scratch/v78/2026-09-21_SHAKE_card.md`, handed at 18:00 CT by a scheduled send. The b3 plan: the handover's two-layer intake, the plan §22, the ADR read for `B7:`, the next three research charters named, the copy step's files committed.

## §1 LINK-READ — the premise rows, each grepped at `13d439f` (layer 2 of the hub's own charter)
- `EzspIncomingMessage.java:14` documents `[type u8][EmberApsFrame 11][lastHopLqi u8][lastHopRssi s8][sender u16 LE]`; the record's fields at `:36–:37` — the reading exists at the parse and is dropped after (IR-16, the bench's `link-quality.yaml:7–:10` says the same).
- `ZclIngestionUnit.route(EzspIncomingMessage)` `:544`; the resolved branch `:565–:579`; `listener.onFrame(device.get())` `:578`; the announce path `:589`; `Listener.onFrame(IEEEAddress)` `:138`.
- `ZigbeeIntegrationAdapter.onFrame` `:1234–:1245`: `cache.recordFrame`, `interviewQueue.onFrameReceived`, `clock.instant()`, `cache.recordEvidence`, `availabilityTracker.recordFrame(device, now)` `:1244` — the liveness seam (M9.6-AVAIL DP-3) the reading rides.
- `AvailabilityTracker.java:25` `public interface`; `:36` `recordFrame(IEEEAddress, Instant)`; one implementation (`StandardAvailabilityTracker.java:150`); `DeviceState` `:90–:98`; `transition()` `:282–:317` with the log at `:313`; `evaluateTimeouts()` `:228`, SILENCE_TIMEOUT at `:261`; the constants `:52–:54`; the injected `Clock` `:103, :120`.
- `ZigbeeIntegrationAdapter.runCycleOnce()` `:554–:562` (`evaluateAvailabilityTimeouts()` `:560`, `:575`) — the tick the ten-minute gate rides; no scheduler added.
- `AvailabilityChangedEvent.java:16–:18` = `(previousStatus, newStatus)`; Doc 01 `01-event-model-and-event-bus.md:354–:360`: an additive field is a version increment (v1 → v2) with the envelope's `schema_version` — out of this unit (IR-45).
- No DIAGNOSTIC entity is minted anywhere in production (`git grep 'EntityRole.DIAGNOSTIC'` outside `core/device-model` and the automation selectors: none); `DeviceHealth` (`rssi_dbm`, `lqi`) exists as a capability with no producer (`StandardCapabilities.java:422–:432`; `EntityType.java:83`, Decision 9) — the read-surface half is LINK-READ-2.
- The P2 survey (the instruction §6): `recordFrame` 1 impl · 1 prod caller · 8 test call sites; `onFrame` 1 prod impl · 2 prod callers · 2 test impls; `ZigbeeDeviceCache.recordFrame(IEEEAddress)` `:179` is a different class, untouched.
- No `permit_join_closed` log site exists in the zigbee module by grep — IR-20 (b)'s second trigger is recorded as absent; the unit takes the ten-minute line only.
- The rig's `EzspIncomingMessage` framing in tests: no test names `lastHopLqi` or constructs the record — the parse is author-shaped on the rig side (IR-37) → T6's literal-bytes test, including the signed decode.
Not re-executed: the module's `build.gradle.kts` (no change proposed); the adapter's cycle period (named as "the adapter's" in §9).

## §2 The steers (D-v78-1, D-v78-2) — the reasoning is in the DR §3; the register rows read: IR-40 (`OPEN (v77 b4); after the run (≤ 60 ms at the run's rows)`) and IR-44 (`Trivial · OPEN (v77 b6)`).

## §3 The research files — the copy step (Nick's hands; committed by the b3 card)
Destinations under `context/research/`: `2026-09-21_RESEARCH-PROJECT_FINAL-HANDOVER_return.md` (the hub copies it from `Claude outputs/2026-09-20_RESEARCH-PROJECT-DESIGN/18_FINAL-HANDOVER_return.md` at b3 — md5 `4ebf698f…`, 53,840 B, identical to the upload) · `2026-09-21_RD-PROGRAM-AUDIT_return.md` (30,611 B) · `2026-09-21_RESEARCH-PROJECT_knowledge-check-Q1_return.md` (14,006 B) · `…Q2_return.md` (14,977 B) · `…Q3_return.md` (16,322 B). The four are not under `ClaudeFolder` (a size search found none); Nick copies them; the b3 card stages them with the intake audit.

## §4 The SHAKE card and its time
`_scratch/v78/2026-09-21_SHAKE_card.md` (2,396 B): the series circuit, the press-before-read rule, the settle definition (the first 30 s with ≤ 0.1 W movement), the no-load and two-bulb reads, the line `SHAKE: <B1 W> <B2 W> <settle s>`. Handed by a scheduled send into this session at 18:00 CT (2026-09-21T23:00Z; scheduled task `trig_01RR4Fv7gmA5R9MjSwbqAmHq`) — THE OPERATOR-LOAD LAW (i).

## §5 Order
hivemind 11 = 6 M + 5 A (computed from porcelain inside the splice): the spine (the v76 b5–b8 blocks rotated verbatim to `context/handoff/archive/pm-handoff-beats-v76b5-v76b8-rotated-2026-09-21.md`; the chain's v77 b7 segment rotated as rotation 151), the snapshot, the brief, the coder-handoff (line 8 stamped; the pointer to the dispatched instruction), the register (IR-45), the DR, the PELTON card, the instruction, this audit.

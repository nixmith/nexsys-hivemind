<!--
file: context/audits/2026-10-12_v109-post-close_HORIZON-1_pre-intake-analysis.md
purpose: The v109 hub's pass-1 analysis of HORIZON-1 (Nick, Mon 17:17 CT: analyze the return deeply; this session and v110 iterate to one articulated result). Layer 2 at the bytes, the hub's verdicts, what the return missed, the iteration plan. Written after v109's close (`e6a7ecc`) — not a beat; no spine file touched. v110 files it beside the return at its HORIZON-1 intake.
audience: the v110 hub · Nick
state-type: hub analysis (pre-intake; pass 1 of 2)
status: WRITTEN Mon 2026-10-12 ~17:5x CT; untracked until v110 stages it.
-->

# HORIZON-1 — the v109 hub's pre-intake analysis (pass 1 of 2)

**Inputs.** The return `context/research/2026-10-12_HORIZON-1_long-horizon-critical-review_return.md` — 127,779 B, md5 `f29982af6575bf117e3ea2a8fa857e7a` (the hub's, on disk at 22:18Z) — its body §0–§8 read whole, Appendix B by finding id only. Re-reads at core `176adad` · bench `ceb08c5` · hivemind `e6a7ecc`; one web fetch. BENCH-BOOT-1 has also RETURNED (`context/audits/2026-10-12_BENCH-BOOT-1_return.md`, 8,017 B, `staged=6 tree=a17a7754d4c12f27ad48d9f14ebdb1e5ccb8f9e9`) — v110's beat 1, untouched here.

## §1 Layer 2 — the hub's re-reads
| Finding | Verdict | The bytes |
|---|---|---|
| F1 durability | **CONFIRMED — sharpened; one correction** | `DatabaseExecutor.java:446–447` (`journal_mode = WAL`, `synchronous = NORMAL`). Sharper: `EventPublisher.java:34–37, 81–82, 113–114` promises the event "durable in SQLite WAL before this method returns" (INV-ES-04, LTD-06); under NORMAL that holds against a process crash, not a power cut — the invariant and the pragma disagree. The order is right: `command_issued` commits, then a subscriber dispatches (`StandardCommandDispatchService.java:42–51`); only the fsync is missing. Correction: "checkpointed only at graceful stop" is not supported — no `wal_autocheckpoint` override in `core/persistence` (grep), so SQLite's default autocheckpoint runs; the javadoc (`SqlitePersistenceLifecycle.java:44–46`) names only the graceful TRUNCATE. The exposed tail is what the kernel has not yet written back (typically tens of seconds — *Inference*), not everything since boot. |
| F25 APS ack | CONFIRMED | 0 matches for `0x003F` / `messageSent` in `integration/integration-zigbee/src/main`. |
| F28 EZSP v13 | **CONFIRMED — a deliberate pin; a live pilot exposure** | `EzspCoordinatorProtocol.java:87` `MAX_SUPPORTED_PROTOCOL_VERSION = 13`; its javadoc `:79–86`: "half-right v14 support is a deaf radio that looks paired … stays ==13 until the Wave-2 v14-batch unit". The corpus (`nexsys-bench:corpus/coordinators/sonoff-dongle-plus-mg24_efr32mg24_ezsp.md:28, 41, 45`): the SKU's reference default ship is EmberZNet 8.0.2 = EZSP v14; the rig's unit measured 7.4.5.0 = v13 ("this unit's batch shipped 7.4.x"); the baseline frozen 2026-07-01 "as-shipped — no reflash". No line in `state.yaml`, the brief, the v110 text or THE HORIZON names PI-2's coordinator or its firmware (grep). |
| F19 / F29 restore | CONFIRMED | `SqlitePersistenceLifecycle.java:53–56` (backup/restore throw `UnsupportedOperationException`, "post-M2 scope"); `EzspCoordinatorProtocol.java:2322` `struct[34] = 0; // networkKeySequenceNumber`, `:2251` `resumeFromNvram()`. |
| F21 token | CONFIRMED | `OpaqueTokenStore.java:≈374–376`: `LOG.warn("… Token: {}", artifactFile, rawToken)`. |
| F12 + the name | CONFIRMED | core `LICENSE:1` "All rights reserved … proprietary"; `ClaudeFolder/legal/NexSys-LLC/2026-08-28_DRAFT_confirmatory-IP-assignment_NDS-to-NexSysLLC.md` and `…_DRAFT_written-consent_successor-license_Apache-2.0.md` (names only, not read); `state.yaml:119` "the application COMMISSIONED, NOT FILED". |
| F13 numbers | CONFIRMED | 701 commits; 613 touch `pm-handoff.md` (87 %); 524 files under `context/audits/`. |
| F31 grader | PLAUSIBLE | the README's invariants are honesty checks (e.g. (iii)); the timeout causes are "additive: no invariant reads it" (`tools/verify72h/README.md:69`); a grep finds no ratio or threshold bar. GATE-2 settles it. |
| HA `not_triggered` | CONFIRMED (fetch) | core `2026.10.1` `homeassistant/components/trace/models.py`: `BaseTrace.not_triggered`, `TraceBuckets.not_triggered` — "a trigger evaluated a relevant change but did not fire". |
| A2 the clock (the hub's) | see §3 | `EventEnvelope.java:103–107` (`ingestTime`, `eventTime` as `Instant`; `globalPosition`); `StandardExplanationService.java:104` (K2 keys on the run's ULID time; a type-scan fallback); 0 clock-discipline hits (`fake-hwclock`, `timesyncd`, `chrony`, "clock step/jump") in `distribution/` and `docs/`. |

Not re-read: F2's growth figures, F3, F6, F18, F20, F22, F27's deep lines, §5's prices (the CRA / RED / PSTI dates match the hub's own knowledge). The lane's bench-side F26 / F31 stay helper-only (its own note).

## §2 The hub's verdicts on the first page
1. **F1 — ACCEPT, re-weighted.** An honesty gap at a power cut, not a safety failure: SQLite stays consistent, the pilot's loads are lamps, and the cost is an unexplained switch in the record. It contradicts the code's own invariant, which makes it a correctness item, not polish. Fix post-run (TAIL-1: FULL on the command path at least, Pi-measured). Now, freeze-safe: no outward sentence says "every command" without the power-cut caveat until TAIL-1 lands (the claims register). **Never run TAIL-1's wall-pulls on the run's card before the run** — the return calls the trial freeze-safe; it is not rig-safe.
2. **F25–F28 — ACCEPT; the return's most urgent item is missing from its first three sessions: PI-2's coordinator (Oct 20).** A new stick of the same SKU may report v14 and be refused at boot. The remedy is a bench step, not Java: probe it (as Step 4 did on 2026-07-01); if it reports v14, reflash the run's measured baseline, 7.4.5.0. → PI-2's card, v110.
3. **F19 / F29 — ACCEPT.** The pilot's interim backup is the weekly copy of the store (OUTREACH-2 edit A); the kit card records the stick's EUI64 at build. RESTORE-1 post-run as the return says; prior art to read: zigpy's network backup and restore (it carries the key's frame counter and bumps it on restore).
4. **The one-way doors — ACCEPT, one date corrected.** The earliest door is the name: COMMISSIONED, NOT FILED three weeks after the go-word, while the flip (Nov 3–9) waits on the receipt → counsel this week (Nick). LICENSE-1 by Nov 2 stands; both instruments signed before any flip. **SCHEMA-1: Nov 2, not Oct 20** — the frozen build writes PI-2's bytes whatever SCHEMA-1 says; the rule must exist before the first post-run unit that changes an event (TAIL-1, ACK-1's v1.2 vocabulary). That frees this week.
5. **F13 — ACCEPT; the hub owns it.** v109 alone: 4 beats, 28 decision ids, two byte-cap refusals and a near-cap re-cut, one stale-bytes re-commit — for one bench landing, two intakes, two charters and the outreach edits. Right for a freeze; wrong for the 54 rows of Nov 3 → Dec 14. §4 takes the cheap part now.

## §3 What the return missed or under-weighted
- **A1 Capacity.** The 12 sessions sum to ≈ 140 h on top of THE HORIZON's 54 rows (Oct 15 → Dec 14), at Nick's ≈ 30 h/week until December. The map has to displace rows, not join them; v110 fits it.
- **A2 The clock after a power cut.** The envelope orders by `globalPosition` (safe) but carries wall-clock `ingestTime` / `eventTime`, and nothing in `distribution/` or `docs/` disciplines the clock at boot. After a power cut that also takes the router down, events carry an unsynchronized clock until NTP returns — the evidence's "when" is weakest right after F1's moment. K2 degrades to its type-scan fallback (cost, not correctness). → a question for SCHEMA-1 (a clock-quality mark in the envelope?) and a step in TAIL-1's trial (a pull with the network down).
- **A3 The moat, restated.** HA 2026.10.1 already keeps not-triggered traces. What is left — confirmation strength and a structured availability record — is at half strength in our own code (F25–F27). So ACK-1 and R2 are the moat, not polish: ACK-1 first among the post-run coder units; R2 above R1 for product value (R1 stays the enabler that makes the rest safe to change); R3 only where it goes past HA (conditions; chains across integrations).
- **A4 GATE-2 needs its evidence first.** The landed classifier (`ceb08c5`, `timeout_causes`) run over the S31 corpus tells how many of the 22/59 timeouts are bench-caused (F26's idempotent sends) before any fitness bar is set. The stance is Nick's: gate the run on fitness, or measure and report it with a red line that holds the household installs.
- **A5 A kit firmware policy.** Firmware batches vary (the corpus says so): every household kit passes a coordinator probe at build, pinned to the run's baseline until the Wave-2 v14 unit lands.
- **A6 The pilot's data.** The weekly copy is the store, never the journal (F21's token sits in journald); the one-page pilot note names what is copied, where it is kept and when it is deleted.
- **A7 The lane's deviations (for the intake record).** 127,779 B against "≤ 35 KB": the body honoured it; Appendix B (≈ 90 KB) was not chartered — useful at audit, costly to read, so v110 reads B by id only. Its bridge died at 16:50 (IR-181: `/sessions` at 100 %, 1.5 MB free at 22:18Z) and it re-read through the Filesystem connector — good practice. Its stale-bytes re-push was verified by size; the md5 above closes that. The same failure hit the hub at 15:49 CT (`v109b4_close_splice_2.py`, caught by md5) — twice in one day: a register row and a lesson.

## §4 The process — what v110 can adopt now at no risk (PROCESS-2 designs the rest)
- One fact, one place: the DR carries the decisions; the beat block ≤ 5 lines pointing at it; line 8 a pointer.
- Decision ids for choices among options, not for acts.
- One audit per return, not per beat.
- The brief's caps keep it short, but two refusals and a re-cut today were spent on bytes, not content: render those regions or raise the caps.
- A retirement rule: each new law retires or merges one.
- Inputs to the skills (proposed to Nick after PROCESS-2): `nexsys-project-manager` — the one-way-door review gains the radio platform and the firmware baseline (the return's §8), and every session map carries a capacity line; `nexsys-coder` — two laws: an external side effect follows a durable (fsynced) intent; no secret in a log.
- The measures: the share of commits that touch the spine (87 % today) and Nick's cards per window.

## §5 The iteration — v109 → v110 → the articulated result
- **Pass 1 (v109, this file).**
- **Pass 2 (v110).** Beat 1 as chartered (BENCH-BOOT-1 first; the dry-run's line). Then one HORIZON-1 beat: file the return and this file; adjudicate F1–F31 and A1–A7 into register rows (§7); fold the coordinator probe into PI-2's card; charter GATE-2 (after BENCH-BOOT-1 lands; its first step the S31 classifier read) and SCHEMA-1 (by Nov 2); fit the session map to capacity against THE HORIZON's rows; put N1–N3 to Nick.
- **Pass 3 — the articulated result, by Dec 1:** one strategy of record, v2 — the thesis and the moat restated, the one-way doors with their dates, the R&D program, the 2027 quarterly skeleton the December ruling chooses among, and the process and skills plan — assembled from ROADMAP-1, LICENSE-1 and PROCESS-2. It replaces the scattered strategy files rather than adding one.

## §6 Decisions for Nick, in the hub's order
- **N1 — this week:** counsel — the filing receipt for the name; the two instruments (the IP assignment, the written consent) signed before any license flip.
- **N2 — before Oct 20:** PI-2's coordinator — probe it; if it reports v14, reflash 7.4.5.0 (v110 writes the card; one action, one line back).
- **N3 — by Oct 22:** GATE-2's stance — gate the run on fitness, or measure and report with a red line for the installs.
- Then the return's D2 (Nov 2), D1 (Nov 25 — the one professional conversation is a natural first task for the sales partner), D4 and D5 (December).

## §7 Proposed register rows (v110 words and mints them)
F1 and INV-ES-04's wording · F25 / F26 confirmation strength · F28 and the kit firmware policy (A5) · F19 / F29 restore · F21 the token in journald · F12 and the name filing · F13 the spine-touch measure · A2 the clock at boot · the stale-bytes failure (twice in a day: md5 after every commit; copy to a fresh path before committing) · GATE-2's stance.

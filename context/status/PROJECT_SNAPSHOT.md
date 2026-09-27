<!--
file: context/status/PROJECT_SNAPSHOT.md
purpose: Current operational state hub — current WU, code state, deferred gates, build status.
audience: All
update-cadence: per-WU
state-type: current
status: CURRENT
last-verified: 2026-09-27 (v83 beat 1, the boot 12/12; the intake; the v83 DR OPEN (D-v83-1..8); IR-61 RUNNING 15:46 CT; BENCH-CORE-5 tonight only on GREEN by 19:30 CT; Sun 2026-09-27 ~16:0x CT (2026-09-27T21:05Z). Order: one card b1, hivemind 7 = 5 M + 2 A. Detail: pm-handoff v83 beat 1.)) Prior: 2026-09-27 (v82 beat 4b, the IR-61 review ACCEPT; the instruction RE-CUT (THE DERIVATION RULE: 1200 s / 7200 s); IR-78..81; Sun 2026-09-27 ~15:4x CT (2026-09-27T20:41Z). Order: one card b4b, hivemind 10 = 8 M + 2 A. Detail: pm-handoff v82 beat 4b.) Prior: THE FULL PRIOR CHAIN verbatim at context/handoff/archive/chains-pre-region-cap-2026-08-23.md + archive/chains-rotated-2026-08-27.md; rolled-off segments: the pm-handoff `:8` chain + its archives.
-->
# Project Snapshot

> **How to read this file:** the frontmatter `last-verified:` chain above (2 pointer segments + the rotation pointer) is the session record; the body below is an OVERWRITTEN DIGEST (W-HIVE-1 P9, ≤2 KB) — rewritten every beat, never appended. The chain and the newest pm-handoff beat block outrank everything else. **The operator's copy-source of record is the file on disk, never a chat card.** Full history: `context/handoff/archive/chains-pre-region-cap-2026-08-23.md` + `archive/PROJECT_SNAPSHOT-priors-rotated-2026-08-21.md`.

## The digest (v83 OPEN at b1 — Sun 15:4x CT; IR-61 RUNNING; REHEARSAL 1 Mon 09:00 CT is THE DELIVERABLE)

**State:** core **`e96dce8`** (IR-18; CI green; **14/20**); bench **`58b5b45`** (METER-3; on the Pi); docs `7221ddc`; skills `180375f`; hivemind `87fd66f` + b1. **The bench card on `e96dce8`** (BC4: 6/6; plugs A/A/A); **the fleet 9/9**; the key ABSENT; the S31 in. Mon 03:30 CT: the first nightly with BH-2 (pre-registered `8/9 PASS · fleet: 9/9 · re-seen 9`, 0 forbidden). **RUNNING:** IR-61 (since Sun 15:46 CT; the return `context/audits/2026-09-27_IR61_return.md`) → the core card → CI → BENCH-CORE-5 tonight only on GREEN by 19:30 CT (D-v83-2), else Monday. **CUT, NOT RUN:** REHEARSAL 1 (Mon 09:00 CT; Nick's paste) · rehearsal 1b (`REH1B:`). **TONIGHT'S DESK (D-v83-6):** VERIFY-72H's charter (falsifiable gates; METER-3b inside) · IR-56's instruction (held; reviewed first) · the K-refresh charter · the `OUTREACH:` gate. **The words:** `IR61: RETURNED` · `NIGHTLY:` · `BC5:` · `REH1B:` (`IR67:` · `POSTURE:` · `KREFRESH:` adopted at their recs). **The laws:** BENCH-PULL after every bench landing · no edit to a running lane's instruction (D-v83-5). **The name:** CLEAR; NOT FILED; rename HELD. **The plan:** §30; the v83 DR (`context/planning/2026-09-27_v83_decision-record.md`).

**Open risks:** ten (OR-S31-INTERMITTENT · OR-HORIZON-UNPLANNED · OR-NIGHTLY-0902-S31 (folds at v83) · FAILCHAN inst. 2 · BUS-SILENT-DROP · ADOPT-AWAKE · METERING-VOLUME · three standing) + IR-61 (running) + IR-29..81 + one fence (no device outside a card). Standing: D4 · no batched pushes · the rig exclusive · FENCE-BUS · the S31 hands-off · no B-2/B-3 CODE before 20 · no written public name before its protocol row · the hub never commits or pushes · no re-pin without `REPIN:` · no ungrepped premise · a frozen token is a pin · no research number in any sentence · no outward sentence the register does not hold.

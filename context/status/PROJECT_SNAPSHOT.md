<!--
file: context/status/PROJECT_SNAPSHOT.md
purpose: Current operational state hub — current WU, code state, deferred gates, build status.
audience: All
update-cadence: per-WU
state-type: current
status: CURRENT
last-verified: 2026-09-27 (v83 beat 2, IR-61 ACCEPT — the core card (18; CI pending); IR-83 registered; the desk queue cut (five files); v81 b1–b4 rotated; Sun 2026-09-27 ~16:4x CT (2026-09-27T21:43Z). Order: the core card, then one card b2, hivemind 16 = 8 M + 8 A. Detail: pm-handoff v83 beat 2.)) Prior: 2026-09-27 (v83 beat 1, the boot 12/12; the intake; the v83 DR OPEN (D-v83-1..8); IR-61 RUNNING 15:46 CT; BENCH-CORE-5 tonight only on GREEN by 19:30 CT; Sun 2026-09-27 ~16:0x CT (2026-09-27T21:05Z). Order: one card b1, hivemind 7 = 5 M + 2 A. Detail: pm-handoff v83 beat 1.)) Prior: THE FULL PRIOR CHAIN verbatim at context/handoff/archive/chains-pre-region-cap-2026-08-23.md + archive/chains-rotated-2026-08-27.md; rolled-off segments: the pm-handoff `:8` chain + its archives.
-->
# Project Snapshot

> **How to read this file:** the frontmatter `last-verified:` chain above (2 pointer segments + the rotation pointer) is the session record; the body below is an OVERWRITTEN DIGEST (W-HIVE-1 P9, ≤2 KB) — rewritten every beat, never appended. The chain and the newest pm-handoff beat block outrank everything else. **The operator's copy-source of record is the file on disk, never a chat card.** Full history: `context/handoff/archive/chains-pre-region-cap-2026-08-23.md` + `archive/PROJECT_SNAPSHOT-priors-rotated-2026-08-21.md`.

## The digest (v83 OPEN at b2 — Sun 16:4x CT; IR-61 on the core card; REHEARSAL 1 Mon 09:00 CT is THE DELIVERABLE)

**State:** core **`e96dce8`** + IR-61 on the card (CI the gate; 14/20 → 15 on green); bench **`58b5b45`** (METER-3; on the Pi); docs `7221ddc`; skills `180375f`; hivemind `5c22132` + b2. **The bench card on `e96dce8`** (BC4: 6/6; plugs A/A/A); **the fleet 9/9**; the key ABSENT; the S31 in. Mon 03:30 CT: the first nightly with BH-2 (pre-registered `8/9 PASS · fleet: 9/9 · re-seen 9`, 0 forbidden). **NEXT AT THE RIG:** BENCH-CORE-5 on CI green by 19:30 CT (D-v83-2; IR-83's readings and the §7 probe ride its card), else Monday. **CUT, NOT RUN:** REHEARSAL 1 (Mon 09:00 CT) · 1b (`REH1B:`) · VERIFY-72H-A (bench lane) · KREFRESH-1 (Mon) · OUTREACH-1 (Mon). **THE JAVA QUEUE (D-v83-11):** IR-61b (Mon; the §9 keys + IR-83's gate) → IR-56 (P4 sample 3) / PJ-2 (`PJ2:`) → IR-67 → the dry 24 h. **The words:** `CORE: LANDED` + `CI:` · `HIVE: LANDED` · `NIGHTLY:` · `BC5:` · `TM:` · `PJ2:` · `REH1B:`. **The laws:** BENCH-PULL after every bench landing · THE PREMISE GATE (IR-56 waits on sample 3). **The name:** CLEAR; NOT FILED at the record (`TM:` asked); rename HELD. **The plan:** §30; the v83 DR (D-v83-1..14).

**Open risks:** ten (OR-S31-INTERMITTENT · OR-HORIZON-UNPLANNED · OR-NIGHTLY-0902-S31 (folds at v83) · FAILCHAN inst. 2 · BUS-SILENT-DROP · ADOPT-AWAKE · METERING-VOLUME · three standing) + IR-83 (the boot replay race) + IR-29..85 + one fence (no device outside a card). Standing: D4 · no batched pushes · the rig exclusive · FENCE-BUS · the S31 hands-off · no B-2/B-3 CODE before 20 · no written public name before its protocol row · the hub never commits or pushes · no re-pin without `REPIN:` · no ungrepped premise · a frozen token is a pin · no research number in any sentence · no outward sentence the register does not hold.

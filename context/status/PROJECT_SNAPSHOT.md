<!--
file: context/status/PROJECT_SNAPSHOT.md
purpose: Current operational state hub — current WU, code state, deferred gates, build status.
audience: All
update-cadence: per-WU
state-type: current
status: CURRENT
last-verified: 2026-09-30 (v89 beat 1, THE BOOT of the evening window — 12/12 after Check 12's reconcile; BENCH: LANDED ede32c9 + HIVE: LANDED 235b28f at the bytes; SKILLS: SYNCED at Check 9; IR-67's dispatch the deliverable (b2 → b4); four blocks rotated; Wed 2026-09-30 ~19:0x CT (2026-10-01T00:02:18Z). Order: HIVE: LANDED (b1) → the first-message lines → the instruction. Detail: pm-handoff v89 b1.) Prior: 2026-09-30 (v88 beat 3, THE CLOSE — BH-3 intaken (PR #1; the landing card); WU-IR67 pre-verified; IR-67's dispatch → v89 (13:00); Wed 2026-09-30 ~12:0x CT (2026-09-30T17:09:08Z). Order: the bench landing → BENCH-PULL-5 → the b3 card → v89's paste. Detail: pm-handoff v88 b3.) Prior: THE FULL PRIOR CHAIN verbatim at context/handoff/archive/chains-pre-region-cap-2026-08-23.md + archive/chains-rotated-2026-08-27.md; rolled-off segments: the pm-handoff `:8` chain + its archives.
-->
# Project Snapshot

> **How to read this file:** the frontmatter `last-verified:` chain above (2 pointer segments + the rotation pointer) is the session record; the body below is an OVERWRITTEN DIGEST (W-HIVE-1 P9, ≤2 KB) — rewritten every beat, never appended. The chain and the newest pm-handoff beat block outrank everything else. **The operator's copy-source of record is the file on disk, never a chat card.** Full history: `context/handoff/archive/chains-pre-region-cap-2026-08-23.md` + `archive/PROJECT_SNAPSHOT-priors-rotated-2026-08-21.md`.

## The digest (v89 OPEN at b1 — the evening window; the deliverable IR-67 dispatched in the cloud with its exit)

**State:** core **`8deef4b`** (PJ-2 landed; CI green ×2; **18/20**, 19 on `a5b9e33` OPEN); bench **`ede32c9`** (BH-3 LANDED, 5; `PR1:` and BENCH-PULL-5 Nick's lines); docs `7221ddc`; skills **`e9a77a8`** (SYNCED at Check 9); hivemind **`235b28f`** + the b1 card (gated, 9). **The bench card on `40412f9` PINNED** until BC7 (Fri; IR-102 a); Wed's `NIGHTLY:` and `BASELINE:` OPEN. **The fleet 9/9**; the key ABSENT; the S31 in. **THE FORTNIGHT (§10):** `CAP: three` · the rig ≤ 4 h by 21:30 CT · three windows a day · `RUN: oct30-two-dry` · `JAVA-ROUTE: split`. **LANES:** IR-67 PRE-VERIFIED (`WU-IR67.md`; the forks at the recs) → THIS WINDOW: the instruction → the FRESH review → the cloud first message (the grant checked before the paste). **NOW:** the b1 card → `TIME:` · `HOURS:` · `PR1:` · `BENCH-PULL-5:` · `CREDITS:` → IR-67's paste when handed. Nothing at the rig tonight; 1b Thu; BC7 Fri. The v89 DR OPEN (D-v89-1..6).

**Open risks:** eleven (OR-BENCH-FENCE-PJ2 · OR-S31-INTERMITTENT (→ IR-88) · OR-HORIZON-UNPLANNED · OR-NIGHTLY-0902-S31 · FAILCHAN inst. 2 · BUS-SILENT-DROP · ADOPT-AWAKE · METERING-VOLUME · three standing) + IR-29..107 (IR-89 CLOSED) + one fence (no device outside a card). Standing: D4 · no batched pushes · the rig exclusive · FENCE-BUS · the S31 hands-off · no B-2/B-3 CODE before 20 · no public name before its protocol row · the hub never commits or pushes · a cloud lane carries its exit, never touches `main` · no PR merged by the button · every card gated · the Pi's clone pinned until BC7 · no re-pin without `REPIN:` · no `capability.removed` from IR-67 · no ungrepped premise · `--no-optional-locks` everywhere.

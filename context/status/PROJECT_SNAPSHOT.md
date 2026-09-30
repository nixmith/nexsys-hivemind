<!--
file: context/status/PROJECT_SNAPSHOT.md
purpose: Current operational state hub — current WU, code state, deferred gates, build status.
audience: All
update-cadence: per-WU
state-type: current
status: CURRENT
last-verified: 2026-09-30 (v88 beat 2 — THE FORTNIGHT RULED (§10; six words at the recs); BH-3 CUT (the ULID route); IR-107; W-SKILLS-10 intaken; HIVE: LANDED 5351870; Wed 2026-09-30 ~08:2x CT (2026-09-30T13:28:39Z). Order: HIVE: LANDED (b2) → SKILLS: LANDED → BH-3's paste → IR-67. Detail: pm-handoff v88 b2.) Prior: 2026-09-30 (v88 beat 1 — THE BOOT 12/12 at ≈ 46.6 KB; HEADs = the record; HIVE: LANDED 92f7fb6; TR3: CLOSED (a phone charger; IR-106); BH-3 + IR-67 in the cloud; the b1 card → W-SKILLS-10 → BH-3 → IR-67; Wed 2026-09-30 ~07:1x CT (2026-09-30T12:14:37Z). Order: HIVE: LANDED (b1) → W-SKILLS-10's §5 line → W-SKILLS-10: LAUNCHED. Detail: pm-handoff v88 b1.) Prior: THE FULL PRIOR CHAIN verbatim at context/handoff/archive/chains-pre-region-cap-2026-08-23.md + archive/chains-rotated-2026-08-27.md; rolled-off segments: the pm-handoff `:8` chain + its archives.
-->
# Project Snapshot

> **How to read this file:** the frontmatter `last-verified:` chain above (2 pointer segments + the rotation pointer) is the session record; the body below is an OVERWRITTEN DIGEST (W-HIVE-1 P9, ≤2 KB) — rewritten every beat, never appended. The chain and the newest pm-handoff beat block outrank everything else. **The operator's copy-source of record is the file on disk, never a chat card.** Full history: `context/handoff/archive/chains-pre-region-cap-2026-08-23.md` + `archive/PROJECT_SNAPSHOT-priors-rotated-2026-08-21.md`.

## The digest (v88 b2 — THE FORTNIGHT open; BH-3 dispatch-ready)

**State:** core **`8deef4b`** (PJ-2 `146468c` + FIX `8deef4b`, CI green ×2; **18/20**, 19 on `a5b9e33` OPEN); bench **`d093a95`** (on the Pi, 42/0 · 26/0); docs `7221ddc`; skills `180375f`; hivemind **`5351870`** + the b2 card (gated, 11). **The bench card on `40412f9` PINNED** (BC6b DONE 6/6; Wed's `NIGHTLY:` OPEN on (`40412f9`, `d093a95`); THE FENCE until BH-3 → BC7 Fri). **The fleet 9/9**; the key ABSENT; the S31 in; the TR3's load a phone charger (IR-106). **THE FORTNIGHT (§10):** `CAP: three`; the rig ≤ 4 h by 21:30 CT; three windows a day; the run Oct 30 with two dry 24 h; `JAVA-ROUTE: split`. **LANES:** W-SKILLS-10 INTAKEN (landing; slot 1 → KREFRESH-1) · BH-3 DISPATCH-READY (slot 2, cloud) · IR-67 next (slot 3). **NOW:** the b2 card (two commits) → the skills card → BH-3's paste → `BASELINE:` → `NIGHTLY:` → IR-67. **Words:** `HIVE: LANDED` · `SKILLS: LANDED` · `BH3: dispatched` · `BASELINE:` · `NIGHTLY:`. The v88 DR OPEN (D-v88-1..17).

**Open risks:** eleven (OR-BENCH-FENCE-PJ2 · OR-S31-INTERMITTENT (→ IR-88) · OR-HORIZON-UNPLANNED · OR-NIGHTLY-0902-S31 · FAILCHAN inst. 2 · BUS-SILENT-DROP · ADOPT-AWAKE · METERING-VOLUME · three standing) + IR-29..107 (IR-89 CLOSED) + one fence (no device outside a card). Standing: D4 · no batched pushes · the rig exclusive · FENCE-BUS · the S31 hands-off · no B-2/B-3 CODE before 20 · no public name before its protocol row · the hub never commits or pushes · a cloud lane carries its exit, never touches `main` · no PR merged by the button · every card gated · the Pi's clone pinned until BH-3's card · no re-pin without `REPIN:` · no ungrepped premise · `--no-optional-locks` everywhere.

<!--
file: context/status/PROJECT_SNAPSHOT.md
purpose: Current operational state hub — current WU, code state, deferred gates, build status.
audience: All
update-cadence: per-WU
state-type: current
status: CURRENT
last-verified: 2026-10-04 (v97 beat 3 — `HIVE: LANDED a0d0809`; the three words (D-v97-7); J2 cut, reviewed, DISPATCH-READY (D-v97-8/9); IR-125; Sun 2026-10-04 ~11:1x CT (2026-10-04T16:13:00Z). Order: the b3 card → the dispatch line → b4 → 17:25 → v98. Detail: pm-handoff v97 b3.) Prior: 2026-10-04 (v97 beat 2 — `HIVE: LANDED 921d371`; J2's pre-verification re-run holds (D-v97-5); THE STRATEGY PASS, S1–S3 (D-v97-6); Sun 2026-10-04 ~09:5x CT (2026-10-04T14:50:23Z). Order: the b2 card → b3 J2 → b4 the packet → 17:25 → v98. Detail: pm-handoff v97 b2.) Prior: THE FULL PRIOR CHAIN verbatim at context/handoff/archive/chains-pre-region-cap-2026-08-23.md + archive/chains-rotated-2026-08-27.md; rolled-off segments: the pm-handoff `:8` chain + its archives.
-->
# Project Snapshot

> **How to read this file:** the frontmatter `last-verified:` chain above (2 pointer segments + the rotation pointer) is the session record; the body below is an OVERWRITTEN DIGEST (W-HIVE-1 P9, ≤2 KB) — rewritten every beat, never appended. The chain and the newest pm-handoff beat block outrank everything else. **The operator's copy-source of record is the file on disk, never a chat card.** Full history: `context/handoff/archive/chains-pre-region-cap-2026-08-23.md` + `archive/PROJECT_SNAPSHOT-priors-rotated-2026-08-21.md`.

## The digest (v97 b1 — HIVE-CLEAN-3 intaken, the fixes by id; J2 on the desk next; REHEARSAL 2 17:25)

**State:** core **`df2bc62`** (J1 — LINK-READ-2 + IR-121; `CI: green`; **19/20**); bench **`ba846c2`** (V72B, D-v96-8; the Pi's `0232c69` to BENCH-PULL-7); docs **`055832c`**; skills `e9a77a8`; hivemind **`a0d0809`** + the b3 card. **THE PI at `5b0e20c`** to BC8 Mon. **THE FLEET: 10 in the registry, 8 ON THE AIR** — the SNZB-06P24 UNJOINED (REHEARSAL 2's card 1; P1 `UNAVAILABLE` + `stale=false`, D-v95-13), the Hue silent (IR-112). **J1 LANDED** (D-v95-23). **J2 DISPATCH-READY** (v97 b3; reviewed; D-v97-8): the desk plans, STOPS at `PLAN-RETURNED`; `GO` v98. **HIVE-CLEAN-3 INTAKEN** (v97 b1; 93 of 102 applied; IR-124). **RULED:** `WIZARD: b′` STANDS; `REVERT J2` keeps Oct 17 (the row moves at b6). **LANES:** none. **THE WORDS** (09:59; D-v97-7): `FRESH-CARD: oct8-11` · `J3: left` (gated) · `RESEARCH-LH: quiet-week`. **NEXT:** the b3 card → J2's dispatch line → the desk · b4 the packet re-stamped + dry-run · b5 U2a · HERO-1 · SOAK-NIGHT-1 · the close ≤ 17:00 → 17:25 the packet → 17:30 the sitting → v98 ≈ 21:00; Mon BC8 (v99); Tue CONFIG-ERROR-1 + IR-122; Wed the soak. DRs ≤ v96 CLOSED.

**Open risks:** ten — OR-HUE-REPORTING-DEAD · OR-S31-INTERMITTENT · OR-NIGHTLY-0902-S31 · FAILCHAN · BUS-SILENT-DROP · ADOPT-AWAKE · METERING-VOLUME · three standing — + IR-29..124 + one fence. Standing: D4 · no batched pushes · the rig exclusive · FENCE-BUS · the S31 hands-off · no B-2/B-3 CODE before 20 · no public name before its protocol row · the hub never commits or pushes · a cloud lane's exit and grant first · no PR merged by the button · every card gated · the restore before any gap · no `capability.removed` · no ungrepped premise · `--no-optional-locks` · every edited row by its id · every tool argument through its validator · every watch on a byte mark.

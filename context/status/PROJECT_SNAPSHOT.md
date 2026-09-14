<!--
file: context/status/PROJECT_SNAPSHOT.md
purpose: Current operational state hub — current WU, code state, deferred gates, build status.
audience: All
update-cadence: per-WU
state-type: current
status: CURRENT
last-verified: 2026-09-14 (v75 beat 1, THE BOOT — preflight 12/12; Check 9 PASS 28/28; the HEADs = Nick's line; IR-1's instrument authored; H8-a re-pinned to run #56; R-5B cut through the gate; IR-20; D-v75-1; the next act the b1 packet; Mon 2026-09-14 ~14:0x CT (2026-09-14T19:01Z). Order: hivemind 9 = 6 M + 3 A by explicit paths (computed from porcelain inside the splice). Detail: pm-handoff v75 beat 1.) Prior: 2026-09-14 (v74 beat 8, THE v74 CLOSE — every HEAD clean; Check 9 PASS 28/28; `PLUG: two` ruled with the criteria and the adoption fence; the plan §11 = v75's window; the next WU R-5B's packet (v75 b1); v75's line handed; Mon 2026-09-14 ~13:0x CT (2026-09-14T18:02Z). Order: hivemind 6 = 6 M + 0 A by explicit paths (computed from porcelain inside the splice). Detail: pm-handoff v74 beat 8.) Prior: THE FULL PRIOR CHAIN verbatim at context/handoff/archive/chains-pre-region-cap-2026-08-23.md + archive/chains-rotated-2026-08-27.md; rolled-off segments: the pm-handoff `:8` chain + its archives.
-->
# Project Snapshot

> **How to read this file:** the frontmatter `last-verified:` chain above (2 pointer segments + the rotation pointer) is the session record; the body below is an OVERWRITTEN DIGEST (W-HIVE-1 P9, ≤2 KB) — rewritten every beat, never appended. The chain and the newest pm-handoff beat block outrank everything else. **The operator's copy-source of record is the file on disk, never a chat card.** Full history: `context/handoff/archive/chains-pre-region-cap-2026-08-23.md` + `archive/PROJECT_SNAPSHOT-priors-rotated-2026-08-21.md`.

## The digest (v75 at beat 1 — both sitting packets on the disk; the b1 card + the IR-1 run in Nick's hands, Mon 2026-09-14 ~13:xx CT)

**State:** core `6bd8508` (HERO-1d; CI all green; the counter 4/20); hivemind `9795c2c` + b1 (the card); docs `7221ddc`; bench `f3631cb`; skills `180375f` (Check 9 PASS 28/28). **The read-API stamp:** v1.1.4 (the freeze doc's record). **This window (the plan §11):** b1 DONE on the disk — IR-1's instrument authored (the run on Nick's host), H8-a RE-PINNED to run #56, R-5B CUT through the gate (28 greps) with the S31 re-read (F-R4b-C: `clusters=1`) and the frame block as a lower bound (no per-frame token at HEAD — D-v75-1 `FRAME: a|b`) · b2 IR-1's lines filed; 114c + FE-114 authored and pasted · b3 the plug card · b4 the Activate email + the knockout charter · b5 the intakes; the bench lane · b6 IR-19; IR-15 first in ENERGY-READ · b7 October authored ahead · b8 the close. **Words:** `H8: Sat 09-19 <hh:mm>` (one word; R-5B follows in the sitting) · `FRAME: a|b` (silence = a) · `Activate: hold` Tue · `NAME:` silence = ii · `AMD100: ratify`. **Owed:** `PROTECT: done` · `ERIK:` · `card-gradle:`.

**Open risks:** seven (FAILCHAN rides H8-a · BUS-SILENT-DROP 4/20 · ADOPT-AWAKE · four standing) + two fences: no IAS water/smoke/vibration adoption before IR-15; no metering plug before ENERGY-READ. Standing: D4 · no batched pushes · the rig exclusive · FENCE-BUS · s31/nightly hands off until R-5B's B6 · no B-2/B-3 CODE before the counter closes · no public name before the opinion · the hub never commits or pushes · nothing from the map before R-5B's intake.

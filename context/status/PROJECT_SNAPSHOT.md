<!--
file: context/status/PROJECT_SNAPSHOT.md
purpose: Current operational state hub — current WU, code state, deferred gates, build status.
audience: All
update-cadence: per-WU
state-type: current
status: CURRENT
last-verified: 2026-10-09 (v101 beat 3 — BC9's card (REHEARSAL 3) CUT and DRY-RUN for Saturday (D-v101-14); two misses caught (D-v101-15); BEAT-RENDERER-1 INTAKEN ACCEPT, the landing after b4 (D-v101-17); Fri 2026-10-09 ~12:5x CT (2026-10-09T17:50:51Z). Order: the b3 card → b4 → the renderer's landing card. Detail: pm-handoff v101 b3.) Prior: 2026-10-09 (v101 beat 2 — BC9a's card + SOAK-NIGHT-2's packet CUT and DRY-RUN (D-v101-10/11); AVAIL-LINE-1 INTAKEN ACCEPT, 1b before the landing (D-v101-12); Fri 2026-10-09 ~12:4x CT (2026-10-09T17:43:30Z). Order: 1b's line → the b2 card → the landing card → b3 → b5; tonight BC9a ≈ 19:30. Detail: pm-handoff v101 b2.) Prior: THE FULL PRIOR CHAIN verbatim at context/handoff/archive/chains-pre-region-cap-2026-08-23.md + archive/chains-rotated-2026-08-27.md; rolled-off segments: the pm-handoff `:8` chain + its archives.
-->
# Project Snapshot

> **How to read this file:** the frontmatter `last-verified:` chain above (2 pointer segments + the rotation pointer) is the session record; the body below is an OVERWRITTEN DIGEST (W-HIVE-1 P9, ≤2 KB) — rewritten every beat, never appended. The chain and the newest pm-handoff beat block outrank everything else. **The operator's copy-source of record is the file on disk, never a chat card.** Full history: `context/handoff/archive/chains-pre-region-cap-2026-08-23.md` + `archive/PROJECT_SNAPSHOT-priors-rotated-2026-08-21.md`.

## The digest (v101 b3 — tonight's and Saturday's texts on disk; the lanes beside the hub)

**State:** core **`37f05a9`** (AVAIL-SHAPE LANDED; **19/20**); bench **`ba846c2`** (+ AVAIL-LINE-1 staged, INTAKEN; 1b then the landing); docs `055832c`; skills `e9a77a8`; hivemind the b3 card's sha. **THE PI RUNS `df2bc62` BY SHA**; BC9a tonight puts `37f05a9` on it. **THE FLEET: 10 in the registry, 9 ON THE AIR** (the Hue dark under J1's rule). **ON DISK, dry-run:** BC9a's card (tonight ≈ 19:30) · SOAK-NIGHT-2's packet (S0; S1 if ≤ 21:30; **Sat 07:00 the harvest AT THE HOUR**) · BC9's card (Sat evening; REHEARSAL 3 as Part D; v102 fills its premise from P2′). **LANES:** AVAIL-LINE-1b (bench; the wrapper hop) · BEAT-RENDERER-1 RETURNED + INTAKEN (its landing card after b4; v3 `fc79eee9…`) · the Java slot free (CONFIG-ERROR-1 → v102). **THE WEEK** (D-v100-15/17): Sat the harvest → v102 (short) · Sat BC9 + REHEARSAL 3 · Sun the FE slot (HERO-1/U2a's charter from v102); PKG-FRESH-1 ≈ 19:00 · Mon dry #1 · Tue the plan-ahead pass. **NEXT:** the b3 card → the lanes' lines → b4 the close (v102's text).

**Open risks:** ten — OR-HUE-REPORTING-DEAD · OR-S31-INTERMITTENT · OR-NIGHTLY-0902-S31 · FAILCHAN · BUS-SILENT-DROP · ADOPT-AWAKE · METERING-VOLUME · three standing — + IR-29..139 + one fence. Standing: D4 · no batched pushes · the rig exclusive · FENCE-BUS · the S31 hands-off · no B-2/B-3 CODE before 20 · no public name before its protocol row · the hub never commits or pushes · no PR merged by the button · every card gated · the restore before any gap · no ungrepped premise · `--no-optional-locks` · every edited row by its id · the store read where the store has the event · a dark device's power is looked at first.

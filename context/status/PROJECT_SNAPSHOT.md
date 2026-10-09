<!--
file: context/status/PROJECT_SNAPSHOT.md
purpose: Current operational state hub — current WU, code state, deferred gates, build status.
audience: All
update-cadence: per-WU
state-type: current
status: CURRENT
last-verified: 2026-10-08 (v100 beat 2 — AVAIL-SHAPE authored + reviewed + DISPATCHED tonight (D-v100-8/10/11); `b-metered` (D-v100-9); IR-139; Thu 2026-10-08 ~19:0x CT (2026-10-09T00:05:38Z). Order: the paste → PKG-FRESH-1 → the b2 card → the returns → b3. Detail: pm-handoff v100 b2.) Prior: 2026-10-08 (v100 beat 1 — THE BOOT: HIVE-CLEAN-4 landed `0f3bf33` (D-v100-2); SOAK-NIGHT-1 INTAKEN — P2 FLAPS 5 > 2 → AVAIL-SHAPE before BC9 (D-v100-3); IR-137/138; THE WEEK by id (D-v100-5); `AVAIL-LIMIT:` asked; PKG-FRESH-1 tonight; Thu 2026-10-08 ~18:2x CT (2026-10-08T23:26:39Z). Order: the b1 card → PKG-FRESH-1 19:45 → b2 AVAIL-SHAPE → the close. Detail: pm-handoff v100 b1.) Prior: THE FULL PRIOR CHAIN verbatim at context/handoff/archive/chains-pre-region-cap-2026-08-23.md + archive/chains-rotated-2026-08-27.md; rolled-off segments: the pm-handoff `:8` chain + its archives.
-->
# Project Snapshot

> **How to read this file:** the frontmatter `last-verified:` chain above (2 pointer segments + the rotation pointer) is the session record; the body below is an OVERWRITTEN DIGEST (W-HIVE-1 P9, ≤2 KB) — rewritten every beat, never appended. The chain and the newest pm-handoff beat block outrank everything else. **The operator's copy-source of record is the file on disk, never a chat card.** Full history: `context/handoff/archive/chains-pre-region-cap-2026-08-23.md` + `archive/PROJECT_SNAPSHOT-priors-rotated-2026-08-21.md`.

## The digest (v100 b2 — the soak OVER THE CEILING; AVAIL-SHAPE DISPATCHED tonight; PKG-FRESH-1 at the rig)

**State:** core **`49455fc`** (J1 + J2; CI green; the counter **19/20**); bench **`ba846c2`**; docs `055832c`; skills `e9a77a8`; hivemind `7638b9b`. **THE PI RUNS `df2bc62` BY SHA**; J2 reaches the Pi at BC9 Sat inside AVAIL-SHAPE's sha. **THE FLEET: 10 in the registry, 9 ON THE AIR** (the Hue dark under J1's own rule; the sensor back). **THURSDAY (D-v100-1..7):** SOAK-NIGHT-1 intaken — **five unprovoked flaps in 10 h** (every dark +65.1 s; every recovery the plug's next frame at 69–73 s; the probe unanswered 7 of 7; IR-137/138): J1 does not ship as it is; **AVAIL-SHAPE** authored, reviewed, **DISPATCHED TONIGHT** (D-v100-8/10/11; `AVAIL-LIMIT: b-metered`, D-v100-9); IR-139. **LANES:** AVAIL-SHAPE (the desk) · PKG-FRESH-1 (the rig, 19:45–22:00); DISPATCH-READY: BEAT-RENDERER-1 · AVAIL-LINE-1. **THE WEEK** (D-v100-5/11): Fri AM the landing, Fri night BC9a (the deploy + SOAK-NIGHT-2 S0) · Sat BC9 + REHEARSAL 3 · Sun the FE slot · Mon 10-12 dry #1. **NEXT:** the paste → PKG-FRESH-1 → the b2 card → the two lines back.

**Open risks:** ten — OR-HUE-REPORTING-DEAD · OR-S31-INTERMITTENT · OR-NIGHTLY-0902-S31 · FAILCHAN · BUS-SILENT-DROP · ADOPT-AWAKE · METERING-VOLUME · three standing — + IR-29..136 + one fence. Standing: D4 · no batched pushes · the rig exclusive · FENCE-BUS · the S31 hands-off · no B-2/B-3 CODE before 20 · no public name before its protocol row · the hub never commits or pushes · no PR merged by the button · every card gated · the restore before any gap · no ungrepped premise · `--no-optional-locks` · every edited row by its id · the store read where the store has the event · a dark device's power is looked at first.

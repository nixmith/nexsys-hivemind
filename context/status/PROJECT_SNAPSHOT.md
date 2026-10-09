<!--
file: context/status/PROJECT_SNAPSHOT.md
purpose: Current operational state hub — current WU, code state, deferred gates, build status.
audience: All
update-cadence: per-WU
state-type: current
status: CURRENT
last-verified: 2026-10-08 (v100 beat 3 — THE CLOSE: AVAIL-SHAPE DELIVERED + INTAKEN ACCEPT, the landing cards cut (D-v100-13/14); PKG-FRESH-1 → Sun (D-v100-12); the DR CLOSED; Thu 2026-10-08 ~21:2x CT (2026-10-09T02:25:53Z). Order: the b3 card → the commit card → CI → the ff-merge → v101 Fri ≈ 18:30. Detail: pm-handoff v100 b3.) Prior: 2026-10-08 (v100 beat 2 — AVAIL-SHAPE authored + reviewed + DISPATCHED tonight (D-v100-8/10/11); `b-metered` (D-v100-9); IR-139; Thu 2026-10-08 ~19:0x CT (2026-10-09T00:05:38Z). Order: the paste → PKG-FRESH-1 → the b2 card → the returns → b3. Detail: pm-handoff v100 b2.) Prior: THE FULL PRIOR CHAIN verbatim at context/handoff/archive/chains-pre-region-cap-2026-08-23.md + archive/chains-rotated-2026-08-27.md; rolled-off segments: the pm-handoff `:8` chain + its archives.
-->
# Project Snapshot

> **How to read this file:** the frontmatter `last-verified:` chain above (2 pointer segments + the rotation pointer) is the session record; the body below is an OVERWRITTEN DIGEST (W-HIVE-1 P9, ≤2 KB) — rewritten every beat, never appended. The chain and the newest pm-handoff beat block outrank everything else. **The operator's copy-source of record is the file on disk, never a chat card.** Full history: `context/handoff/archive/chains-pre-region-cap-2026-08-23.md` + `archive/PROJECT_SNAPSHOT-priors-rotated-2026-08-21.md`.

## The digest (v100 b3 — THE CLOSE: AVAIL-SHAPE DELIVERED; the landing in Nick's hands; PKG-FRESH-1 → Sunday)

**State:** core **`37f05a9`** (AVAIL-SHAPE LANDED, PR #11, CI green; **19/20**); bench **`ba846c2`**; docs `055832c`; skills `e9a77a8`; hivemind `7638b9b`. **THE PI RUNS `df2bc62` BY SHA**; J2 reaches the Pi at BC9 Sat inside AVAIL-SHAPE's sha. **THE FLEET: 10 in the registry, 9 ON THE AIR** (the Hue dark under J1's own rule; the sensor back). **THURSDAY (D-v100-1..15):** SOAK-NIGHT-1 intaken — **five unprovoked flaps in 10 h** (every dark +65.1 s, every recovery the next frame at 69–73 s; IR-137/138): J1 does not ship as it is; **AVAIL-SHAPE** authored, reviewed, dispatched and **DELIVERED** the same evening (D-v100-8..14; `b-metered`; tree `a12087ce…` over `49455fc`, `check` green) — LANDED `37f05a9` (D-v100-16). PKG-FRESH-1 NOT sat (its 20:30 gate) → Sun 10-11 (D-v100-12). **LANES:** none; Fri AM three (D-v100-17); DISPATCH-READY: BEAT-RENDERER-1 · AVAIL-LINE-1 · PKG-FRESH-1 (Sun). **THE WEEK** (D-v100-15): Fri the landing; BC9a + SOAK-NIGHT-2 · Sat the harvest; BC9 + REHEARSAL 3 · Sun the FE slot; PKG-FRESH-1 · Mon dry #1. **NEXT:** the b3 card → v101 Fri AM.

**Open risks:** ten — OR-HUE-REPORTING-DEAD · OR-S31-INTERMITTENT · OR-NIGHTLY-0902-S31 · FAILCHAN · BUS-SILENT-DROP · ADOPT-AWAKE · METERING-VOLUME · three standing — + IR-29..136 + one fence. Standing: D4 · no batched pushes · the rig exclusive · FENCE-BUS · the S31 hands-off · no B-2/B-3 CODE before 20 · no public name before its protocol row · the hub never commits or pushes · no PR merged by the button · every card gated · the restore before any gap · no ungrepped premise · `--no-optional-locks` · every edited row by its id · the store read where the store has the event · a dark device's power is looked at first.

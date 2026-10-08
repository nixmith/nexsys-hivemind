<!--
file: context/status/PROJECT_SNAPSHOT.md
purpose: Current operational state hub — current WU, code state, deferred gates, build status.
audience: All
update-cadence: per-WU
state-type: current
status: CURRENT
last-verified: 2026-10-07 (v99 beat 2 — the rotation (v97 b1–b6); DIST-CENSUS filed, NO BLOCKER (D-v99-6); PKG-FRESH-1's card cut + dry-run (D-v99-7); CONFIG-ERROR-1 pre-verified (D-v99-8); BC8 running; Wed 2026-10-07 ~20:0x CT (2026-10-08T01:00:36Z). Order: the b2 card → BC8's one line → S0 → b3 the intake + the close. Detail: pm-handoff v99 b2.) Prior: 2026-10-07 (v99 beat 1 — THE BOOT of Wednesday's window (the Monday it was cut for passed unrun); BC8 re-stamped + handed (D-v99-2); S0 conditional (D-v99-3); the renderer chartered (D-v99-4); Wed 2026-10-07 ~19:3x CT (2026-10-08T00:38:14Z). Order: the b1 card → BC8's one line → b2 the intake. Detail: pm-handoff v99 b1.) Prior: THE FULL PRIOR CHAIN verbatim at context/handoff/archive/chains-pre-region-cap-2026-08-23.md + archive/chains-rotated-2026-08-27.md; rolled-off segments: the pm-handoff `:8` chain + its archives.
-->
# Project Snapshot

> **How to read this file:** the frontmatter `last-verified:` chain above (2 pointer segments + the rotation pointer) is the session record; the body below is an OVERWRITTEN DIGEST (W-HIVE-1 P9, ≤2 KB) — rewritten every beat, never appended. The chain and the newest pm-handoff beat block outrank everything else. **The operator's copy-source of record is the file on disk, never a chat card.** Full history: `context/handoff/archive/chains-pre-region-cap-2026-08-23.md` + `archive/PROJECT_SNAPSHOT-priors-rotated-2026-08-21.md`.

## The digest (v99 b2 — BC8 running tonight; DIST-CENSUS no blocker; PKG-FRESH-1's card cut; the renderer chartered)

**State:** core **`49455fc`** (J1 + J2 LANDED; CI green; the counter **19/20**); bench **`ba846c2`**; docs `055832c`; skills `e9a77a8`; hivemind `d2aa876`. **THE PI at `5b0e20c`** → **`df2bc62` BY SHA at BC8 TONIGHT (Wed 10-07; running since 19:46)**. **THE FLEET: 10 in the registry, 9 ON THE AIR** (the Hue silent, IR-112). **TONIGHT (D-v99-1..8):** BC8 re-stamped + handed; S0 after it if P1 ACCEPT (S1 skipped); the renderer CHARTERED; DIST-CENSUS FILED — no blocker (the runtime bundled; the `.deb` CI-built; the loopback bind and the 7-day retention the frictions); PKG-FRESH-1's card CUT + dry-run, held for `CAPACITY:`; CONFIG-ERROR-1 pre-verified. **LANES:** BC8 RUNNING (the rig); DISPATCH-READY: BEAT-RENDERER-1 · AVAIL-LINE-1 · SOAK-NIGHT-1 S0 · PKG-FRESH-1 (Thu–Sat). **THE WEEK** (two days slipped; re-planned by id at the close): Wed BC8 + S0 · Thu PKG-FRESH-1 or the renderer · Fri BC9 + REHEARSAL 3 · Sat reserve · Mon 10-12 dry #1. **NEXT:** the b2 card → BC8's one line → S0 → b3 the intake + the close.

**Open risks:** ten — OR-HUE-REPORTING-DEAD · OR-S31-INTERMITTENT · OR-NIGHTLY-0902-S31 · FAILCHAN · BUS-SILENT-DROP · ADOPT-AWAKE · METERING-VOLUME · three standing — + IR-29..131 + one fence. Standing: D4 · no batched pushes · the rig exclusive · FENCE-BUS · the S31 hands-off · no B-2/B-3 CODE before 20 · no public name before its protocol row · the hub never commits or pushes · no PR merged by the button · every card gated · the restore before any gap · no ungrepped premise · `--no-optional-locks` · every edited row by its id · the store read where the store has the event · a dark device's power is looked at first.

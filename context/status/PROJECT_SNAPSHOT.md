<!--
file: context/status/PROJECT_SNAPSHOT.md
purpose: Current operational state hub — current WU, code state, deferred gates, build status.
audience: All
update-cadence: per-WU
state-type: current
status: CURRENT
last-verified: 2026-10-09 (v101 beat 1 — THE BOOT of the Friday MORNING window; the landing re-read (core `37f05a9`; WUCP Phase 2 on AVAIL-SHAPE COMPLETE, D-v101-2); the rotation (v98 b1–b5; the chain 262; the pointer re-derived, D-v101-4); IR-135 answered (D-v101-3); AVAIL-LINE-1 + BEAT-RENDERER-1 dispatched (D-v101-5/6); PKG-FRESH-1 re-stamped for Sun (D-v101-7); Fri 2026-10-09 ~09:0x CT (2026-10-09T14:06:35Z). Order: the b1 card → the lanes' lines → b2 CONFIG-ERROR-1 → b3 BC9a + SOAK-NIGHT-2 → b4 BC9 → b5 the close; v102 ≈ 18:30. Detail: pm-handoff v101 b1.) Prior: 2026-10-08 (v100 beat 3 — THE CLOSE: AVAIL-SHAPE DELIVERED + INTAKEN ACCEPT, the landing cards cut (D-v100-13/14); PKG-FRESH-1 → Sun (D-v100-12); the DR CLOSED; Thu 2026-10-08 ~21:2x CT (2026-10-09T02:25:53Z). Order: the b3 card → the commit card → CI → the ff-merge → v101 Fri ≈ 18:30. Detail: pm-handoff v100 b3.) Prior: THE FULL PRIOR CHAIN verbatim at context/handoff/archive/chains-pre-region-cap-2026-08-23.md + archive/chains-rotated-2026-08-27.md; rolled-off segments: the pm-handoff `:8` chain + its archives.
-->
# Project Snapshot

> **How to read this file:** the frontmatter `last-verified:` chain above (2 pointer segments + the rotation pointer) is the session record; the body below is an OVERWRITTEN DIGEST (W-HIVE-1 P9, ≤2 KB) — rewritten every beat, never appended. The chain and the newest pm-handoff beat block outrank everything else. **The operator's copy-source of record is the file on disk, never a chat card.** Full history: `context/handoff/archive/chains-pre-region-cap-2026-08-23.md` + `archive/PROJECT_SNAPSHOT-priors-rotated-2026-08-21.md`.

## The digest (v101 b1 — Friday AM: three lanes beside the hub; tonight BC9a + SOAK-NIGHT-2)

**State:** core **`37f05a9`** (AVAIL-SHAPE LANDED, PR #11, CI green; **19/20**); bench **`ba846c2`**; docs `055832c`; skills `e9a77a8`; hivemind `513d1c0`. **THE PI RUNS `df2bc62` BY SHA**; BC9a tonight puts `37f05a9` on it. **THE FLEET: 10 in the registry, 9 ON THE AIR** (the Hue dark under J1's rule). `bench-hero` acts on the Hue only — no plug, no confounder (IR-135). **LANES (Fri AM):** AVAIL-LINE-1 (bench) · BEAT-RENDERER-1 (hivemind, its worktree) · CONFIG-ERROR-1 (Java; b2). PKG-FRESH-1 RE-STAMPED for Sun 10-11 ≈ 19:00 (D-v101-7). **THE WEEK** (D-v100-15/17): Fri night BC9a + SOAK-NIGHT-2 · Sat 07:00 the harvest; BC9 + REHEARSAL 3 · Sun the FE slot; PKG-FRESH-1 · Mon dry #1 · Tue the plan-ahead pass. **NEXT:** the b1 card → b2 → b3 BC9a's card + SOAK-NIGHT-2's packet (THE ONE DELIVERABLE) → b4 BC9 → b5.

**Open risks:** ten — OR-HUE-REPORTING-DEAD · OR-S31-INTERMITTENT · OR-NIGHTLY-0902-S31 · FAILCHAN · BUS-SILENT-DROP · ADOPT-AWAKE · METERING-VOLUME · three standing — + IR-29..139 + one fence. Standing: D4 · no batched pushes · the rig exclusive · FENCE-BUS · the S31 hands-off · no B-2/B-3 CODE before 20 · no public name before its protocol row · the hub never commits or pushes · no PR merged by the button · every card gated · the restore before any gap · no ungrepped premise · `--no-optional-locks` · every edited row by its id · the store read where the store has the event · a dark device's power is looked at first.

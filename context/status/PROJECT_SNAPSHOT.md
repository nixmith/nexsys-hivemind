<!--
file: context/status/PROJECT_SNAPSHOT.md
purpose: Current operational state hub — current WU, code state, deferred gates, build status.
audience: All
update-cadence: per-WU
state-type: current
status: CURRENT
last-verified: 2026-09-13 (v73 beat 4, core `fed99e8` landed + CI all green (2/20); hivemind `1c7cdb2`; `FE: 6af76f7` green; the plan of record re-cut; R-5 chartered; HERO-1c + R-5A handed; Sun 2026-09-13 ~15:5x CT (2026-09-13T20:57Z). Order: hivemind 7 = 5 M + 2 A by explicit paths (computed from porcelain inside the splice). Detail: pm-handoff v73 beat 4.) Prior: 2026-09-13 (v73 beat 3, hivemind `427a8f6` + docs `7221ddc` landed; EXPLAIN-114b returned and audited ACCEPT (7 = 6 M + 1 A; the instruments 1/0/0); HERO-1c chartered on `FE:`; the improvement register minted; the core card handed; Sun 2026-09-13 ~15:1x CT (2026-09-13T20:17Z). Order: core 7 by explicit paths (Nick's hands); hivemind 9 = 5 M + 4 A by explicit paths (computed from porcelain inside the splice). Detail: pm-handoff v73 beat 3.) Prior: THE FULL PRIOR CHAIN verbatim at context/handoff/archive/chains-pre-region-cap-2026-08-23.md + archive/chains-rotated-2026-08-27.md; rolled-off segments: the pm-handoff `:8` chain + its archives.
-->
# Project Snapshot

> **How to read this file:** the frontmatter `last-verified:` chain above (2 pointer segments + the rotation pointer) is the session record; the body below is an OVERWRITTEN DIGEST (W-HIVE-1 P9, ≤2 KB) — rewritten every beat, never appended. The chain and the newest pm-handoff beat block outrank everything else. **The operator's copy-source of record is the file on disk, never a chat card.** Full history: `context/handoff/archive/chains-pre-region-cap-2026-08-23.md` + `archive/PROJECT_SNAPSHOT-priors-rotated-2026-08-21.md`.

## The digest (v73 at beat 4 — 114b LANDED green `fed99e8`, the deliverable MET; the plan of record re-cut; HERO-1c and R-5A the two lanes, Sun 2026-09-13 ~15:5x CT)

**State:** core `fed99e8` (CI all checks green; the counter 2/20); hivemind `1c7cdb2` + b4 (the card); docs `7221ddc`; bench `1201368`; skills `c630c5c`. **The plan of record:** `context/planning/2026-09-13_v73_PROGRAM-PLAN_after-114b_two-weeks-and-October.md` (§0 one screen · §2 the critical path · §3 the ranking · §5 the calendar · §6 the words). **Lanes (the cap two):** HERO-1c on web-ui (the paste = §NEXT block 1) · R-5 Part A on the bench (block 2); the Java domain free for 114c after the freeze note. **The rig:** H8-a's packet re-cut through the gate (next beat) → `H8:`; R-5 Part B's packet after Part A lands → `R5:`; one sitting recommended Sat 09-19 / Sun 09-20. **Owed cards (hub-authored):** the v1.1.4 freeze note · C-003 narrow into the register (`C003: mint`) · `AMD100: ratify` · AMD-102. **Words due:** D-v73-2..6 (the plan §6); `Activate:` Tue 09-15. **Erik:** the opinion is the wait-state. Check 9 STALE (one file; Nick's sync).

**Open risks:** seven (FAILCHAN rides H8-a · BUS-SILENT-DROP 2/20 · ADOPT-AWAKE · four standing). Fences: D4 · no batched pushes · the rig exclusive · FENCE-BUS · s31/nightly hands off until R-5 B1 · no B-2/B-3 CODE before the counter closes · no public name before the opinion · the hub never commits or pushes.

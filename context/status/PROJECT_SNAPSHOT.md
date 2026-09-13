<!--
file: context/status/PROJECT_SNAPSHOT.md
purpose: Current operational state hub — current WU, code state, deferred gates, build status.
audience: All
update-cadence: per-WU
state-type: current
status: CURRENT
last-verified: 2026-09-13 (v73 beat 6, hivemind `7cf0d0b`; the HERO-1c correction and R-5A-ii returned and audited ACCEPT; the web-ui card (23) and the bench card (11) handed; v72 b1–b7 rotated; Sun 2026-09-13 ~17:5x CT (2026-09-13T22:57Z). Order: core 23 by domain (Nick's hands; frontend CI the gate); bench 11 by explicit paths; hivemind 8 = 5 M + 3 A by explicit paths (computed from porcelain inside the splice). Detail: pm-handoff v73 beat 6.) Prior: 2026-09-13 (v73 beat 5, hivemind `e7aafd4`; R-5A and HERO-1c returned and audited ACCEPT (one combined intake); HERO-1c corrected before the landing; R-5A-ii chartered; the register IR-8/IR-9; Sun 2026-09-13 ~17:2x CT (2026-09-13T22:23Z). Order: hivemind 10 = 5 M + 5 A by explicit paths (computed from porcelain inside the splice). Detail: pm-handoff v73 beat 5.) Prior: THE FULL PRIOR CHAIN verbatim at context/handoff/archive/chains-pre-region-cap-2026-08-23.md + archive/chains-rotated-2026-08-27.md; rolled-off segments: the pm-handoff `:8` chain + its archives.
-->
# Project Snapshot

> **How to read this file:** the frontmatter `last-verified:` chain above (2 pointer segments + the rotation pointer) is the session record; the body below is an OVERWRITTEN DIGEST (W-HIVE-1 P9, ≤2 KB) — rewritten every beat, never appended. The chain and the newest pm-handoff beat block outrank everything else. **The operator's copy-source of record is the file on disk, never a chat card.** Full history: `context/handoff/archive/chains-pre-region-cap-2026-08-23.md` + `archive/PROJECT_SNAPSHOT-priors-rotated-2026-08-21.md`.

## The digest (v73 at beat 6 — both follow-ups accepted; the web-ui and bench cards in Nick's hands; the spine rotated, Sun 2026-09-13 ~17:5x CT)

**State:** core `fed99e8` (CI green; the counter 2/20) + HERO-1c's corrected tree (20 M + 3 A; the web-ui card → `frontend` CI + a `bus-soak` sample → 3/20 on green); hivemind `7cf0d0b` + b6 (the card); docs `7221ddc`; bench `1201368` + eleven paths (the card); skills `c630c5c`. **The plan of record:** `context/planning/2026-09-13_v73_PROGRAM-PLAN_after-114b_two-weeks-and-October.md`. **Lanes:** none running after the cards (the web-ui slot → HERO-1d then FE-114; the Java slot → 114c after the freeze note; the bench → P-1's live packet after `HARNESS-PLUG:`). **The rig:** H8-a's packet re-cut through the gate (v74's first block) → `H8:`; R-5 Part B's packet after the sitting is named → `R5:`; one sitting Sat 09-19 / Sun 09-20 recommended. **Owed (hub-authored):** the v1.1.4 freeze note · C-003 narrow (`C003: mint`) · `AMD100: ratify` · AMD-102 · the `Activate:` H10 (Mon). **Words due:** D-v73-2..6. Check 9 STALE (one file; Nick's sync).

**Open risks:** seven (FAILCHAN rides H8-a · BUS-SILENT-DROP 2/20 · ADOPT-AWAKE · four standing). Fences: D4 · no batched pushes · the rig exclusive · FENCE-BUS · s31/nightly hands off until R-5 B1 (the `fleet:` wiring additive, never a re-grade) · no B-2/B-3 CODE before the counter closes · no public name before the opinion · the hub never commits or pushes.

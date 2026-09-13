<!--
file: context/status/PROJECT_SNAPSHOT.md
purpose: Current operational state hub — current WU, code state, deferred gates, build status.
audience: All
update-cadence: per-WU
state-type: current
status: CURRENT
last-verified: 2026-09-13 (v73 beat 5, hivemind `e7aafd4`; R-5A and HERO-1c returned and audited ACCEPT (one combined intake); HERO-1c corrected before the landing; R-5A-ii chartered; the register IR-8/IR-9; Sun 2026-09-13 ~17:2x CT (2026-09-13T22:23Z). Order: hivemind 10 = 5 M + 5 A by explicit paths (computed from porcelain inside the splice). Detail: pm-handoff v73 beat 5.) Prior: 2026-09-13 (v73 beat 4, core `fed99e8` landed + CI all green (2/20); hivemind `1c7cdb2`; `FE: 6af76f7` green; the plan of record re-cut; R-5 chartered; HERO-1c + R-5A handed; Sun 2026-09-13 ~15:5x CT (2026-09-13T20:57Z). Order: hivemind 7 = 5 M + 2 A by explicit paths (computed from porcelain inside the splice). Detail: pm-handoff v73 beat 4.) Prior: THE FULL PRIOR CHAIN verbatim at context/handoff/archive/chains-pre-region-cap-2026-08-23.md + archive/chains-rotated-2026-08-27.md; rolled-off segments: the pm-handoff `:8` chain + its archives.
-->
# Project Snapshot

> **How to read this file:** the frontmatter `last-verified:` chain above (2 pointer segments + the rotation pointer) is the session record; the body below is an OVERWRITTEN DIGEST (W-HIVE-1 P9, ≤2 KB) — rewritten every beat, never appended. The chain and the newest pm-handoff beat block outrank everything else. **The operator's copy-source of record is the file on disk, never a chat card.** Full history: `context/handoff/archive/chains-pre-region-cap-2026-08-23.md` + `archive/PROJECT_SNAPSHOT-priors-rotated-2026-08-21.md`.

## The digest (v73 at beat 5 — both lanes returned and accepted; HERO-1c's correction and R-5A-ii are the two pastes; the cards follow, Sun 2026-09-13 ~17:2x CT)

**State:** core `fed99e8` (CI green; the counter 2/20) + HERO-1c's tree uncommitted (18 M + 3 A under `web-ui/dashboard`; the correction lands on it); hivemind `e7aafd4` + b5 (the card); docs `7221ddc`; bench `1201368` + Part A's nine uncommitted (R-5A-ii lands on it); skills `c630c5c`. **The plan of record:** `context/planning/2026-09-13_v73_PROGRAM-PLAN_after-114b_two-weeks-and-October.md`. **Lanes (the cap two):** the HERO-1c correction (web-ui) · R-5A-ii (the bench); then the two cards → `frontend` CI · `BENCH: LANDED`. **Next authored:** H8-a's packet through the gate; the v1.1.4 freeze note; C-003 narrow (`C003: mint`); 114c; HERO-1d (D5's keyless set + IR-8's lint). **The rig:** `H8:` / `R5:` (one sitting Sat 09-19 / Sun 09-20 recommended). **Words due:** D-v73-2..6; `Activate:` Tue 09-15. Check 9 STALE (one file; Nick's sync).

**Open risks:** seven (FAILCHAN rides H8-a · BUS-SILENT-DROP 2/20 · ADOPT-AWAKE · four standing). Fences: D4 · no batched pushes · the rig exclusive · FENCE-BUS · s31/nightly hands off until R-5 B1 (the `fleet:` wiring is additive, never a re-grade) · no B-2/B-3 CODE before the counter closes · no public name before the opinion · the hub never commits or pushes.

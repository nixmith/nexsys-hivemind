<!--
file: context/status/PROJECT_SNAPSHOT.md
purpose: Current operational state hub — current WU, code state, deferred gates, build status.
audience: All
update-cadence: per-WU
state-type: current
status: CURRENT
last-verified: 2026-09-12 (v70 beat 10, THE CLOSE — sample #11's frame: the bus idle, the run hand-off is the class; CI-1 landed `ff1a6e1`, check GREEN, bus-soak GREEN (#13); next v71: FIX-2b-ii-i, then EXPLAIN-114a, HERO-1c, R-4c today, Sat 2026-09-12 ~10:5x CT (2026-09-12T15:51Z). Order: hivemind 4 = 4 M + 0 A by explicit paths (the spine; computed from porcelain inside the splice). Detail: pm-handoff v70 beat 10.) Prior: 2026-09-11 (v70 beat 9, the post-close intake — FIX-2b-i and HERO-1b RETURNED, audited ACCEPT (13 and 17 files; the cards in the close-3 packet, FIX-2b-i first = sample #11); EXPLAIN-114a after act 1 under GATE: scoped; REV-1 + REPRO-1 for v71; four v69 blocks rotated; H8A owed, Fri 2026-09-11 ~22:1x CT (2026-09-12T03:17Z). Order: hivemind 11 = 6 M + 5 A by explicit paths (computed from porcelain inside the splice); core FIX-2b-i 13 = 11 M + 2 A and HERO-1b 17 = 16 M + 1 A, two cards, two pushes (Nick's hands). Detail: pm-handoff v70 beat 9.) Prior: THE FULL PRIOR CHAIN verbatim at context/handoff/archive/chains-pre-region-cap-2026-08-23.md + archive/chains-rotated-2026-08-27.md; rolled-off segments: the pm-handoff `:8` chain + its archives.
-->
# Project Snapshot

> **How to read this file:** the frontmatter `last-verified:` chain above (2 pointer segments + the rotation pointer) is the session record; the body below is an OVERWRITTEN DIGEST (W-HIVE-1 P9, ≤2 KB) — rewritten every beat, never appended. The chain and the newest pm-handoff beat block outrank everything else. **The operator's copy-source of record is the file on disk, never a chat card.** Full history: `context/handoff/archive/chains-pre-region-cap-2026-08-23.md` + `archive/PROJECT_SNAPSHOT-priors-rotated-2026-08-21.md`.

## The digest (v70 CLOSED at beat 10 — the gate green at `ff1a6e1`; the class located in the run hand-off; v71 opens on FIX-2b-ii, Sat 2026-09-12 ~10:5x CT)

**State:** core `ff1a6e1` (CI-1; `check` GREEN · install-smoke GREEN ×2 · `bus-soak` GREEN = sample #13) after `bd5d35e` (FIX-2b-i) and `6af76f7` (HERO-1b; `FE:` owed); hivemind `5e73d37` + this beat (4 M); docs `73c204b`. **The class:** sample #11's dump — the bus idle, `pending=0`, the engine parked; the run does not continue after `automation_triggered` (`StandardRunManager:651`); the frame audit's §2 names the reads. **v71's deliverable:** FIX-2b-ii-i — two INFO lines in `core/automation` (the hand-off taken · the action step started) + the census's checkpoint-lag caveat; first on the Java slot; the fix on the step the next red names. **Then:** EXPLAIN-114a · HERO-1c (web-ui) · P-1 · R-4c today. **Owed:** `H8A:` · `FE: 6af76f7` · `AMD100:` · `PROTECT: done`. **HEADs:** core `ff1a6e1` · docs `73c204b` · skills `c630c5c` · bench `4539f13`. Check 9 STALE. **v71:** packet close-6.

**Open risks:** six (FAILCHAN rides H8-a, record owed · BUS-SILENT-DROP: located in the run hand-off; the `bus-soak` job samples every push; 1 green since `ff1a6e1` · four standing). Fences: one lane per path-domain (D4) · no batched pushes · the rig exclusive · FENCE-BUS · s31/nightly hands off · no B-2/B-3 code before C-003 · no public brand use before the opinion · no name graded in chat · 09-18 · the hub never commits or pushes.

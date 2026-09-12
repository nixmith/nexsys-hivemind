<!--
file: context/status/PROJECT_SNAPSHOT.md
purpose: Current operational state hub — current WU, code state, deferred gates, build status.
audience: All
update-cadence: per-WU
state-type: current
status: CURRENT
last-verified: 2026-09-11 (v70 beat 9, the post-close intake — FIX-2b-i and HERO-1b RETURNED, audited ACCEPT (13 and 17 files; the cards in the close-3 packet, FIX-2b-i first = sample #11); EXPLAIN-114a after act 1 under GATE: scoped; REV-1 + REPRO-1 for v71; four v69 blocks rotated; H8A owed, Fri 2026-09-11 ~22:1x CT (2026-09-12T03:17Z). Order: hivemind 11 = 6 M + 5 A by explicit paths (computed from porcelain inside the splice); core FIX-2b-i 13 = 11 M + 2 A and HERO-1b 17 = 16 M + 1 A, two cards, two pushes (Nick's hands). Detail: pm-handoff v70 beat 9.) Prior: 2026-09-11 (v70 CLOSED at beat 8 — `ci` on `cc05a54` RED at lifecycle, sample #10 with FIX-2a's reading, read and filed (2 processors; H1–H4); FIX-2b-i ISSUE-READY (16878 B); the gate word to Nick; v71 on the intakes, Fri 2026-09-11 ~21:1x CT (2026-09-12T02:14Z). Order: hivemind 6 = 4 M + 2 A by explicit paths (the HERO-1b return unstaged until its audit). Detail: pm-handoff v70 beat 8.) Prior: THE FULL PRIOR CHAIN verbatim at context/handoff/archive/chains-pre-region-cap-2026-08-23.md + archive/chains-rotated-2026-08-27.md; rolled-off segments: the pm-handoff `:8` chain + its archives.
-->
# Project Snapshot

> **How to read this file:** the frontmatter `last-verified:` chain above (2 pointer segments + the rotation pointer) is the session record; the body below is an OVERWRITTEN DIGEST (W-HIVE-1 P9, ≤2 KB) — rewritten every beat, never appended. The chain and the newest pm-handoff beat block outrank everything else. **The operator's copy-source of record is the file on disk, never a chat card.** Full history: `context/handoff/archive/chains-pre-region-cap-2026-08-23.md` + `archive/PROJECT_SNAPSHOT-priors-rotated-2026-08-21.md`.

## The digest (v70 beat 9 — both lanes audited ACCEPT, cards ready; v71 opens on sample #11, Fri 2026-09-11 ~22:1x CT)

**State:** core `cc05a54` + two audited, unstaged lanes — FIX-2b-i (13 = 11 M + 2 A: `pendingDepth` · the jcmd dump · the pinned-thread trace) and HERO-1b (17 = 16 M + 1 A; verify exit 0, 392 tests) — the close-3 packet's acts 1–2, in that order; hivemind `2d3147f` + beat 9 (act 3); docs `73c204b`. **The class:** #10 RED, read (the stall after `automation_triggered`; 2 processors; H1–H4); **#11 = FIX-2b-i's push**, the first that can name the frame; FIX-2b-ii on it; else REV-1 (independent adversarial read) + REPRO-1 (desk reproduction under two carriers + full-check load). **The word:** `GATE: scoped` (default) | `strict`. **Lanes:** EXPLAIN-114a after act 1 under scoped (act 4) · HERO-1c next on web-ui · P-1 after both · R-4c Saturday. **Owed:** `H8A:` · `CI:`/`FE:` on the two pushes · `AMD100:` · `PROTECT: done`. **HEADs:** core `cc05a54` · docs `73c204b` · skills `c630c5c` · bench `4539f13`. Check 9 STALE. **v71:** packet act 6.

**Open risks:** six (FAILCHAN rides H8-a, record owed · BUS-SILENT-DROP: #10 read; the discriminators land at #11; FIX-2b-ii on the frame · four standing). Fences: one lane per path-domain (D4) · no batched pushes · the rig exclusive · FENCE-BUS · s31/nightly hands off · no B-2/B-3 code before C-003 · no public brand use before the opinion · no name graded in chat · 09-18 · the hub never commits or pushes.

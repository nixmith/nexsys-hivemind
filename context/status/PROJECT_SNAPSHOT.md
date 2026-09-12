<!--
file: context/status/PROJECT_SNAPSHOT.md
purpose: Current operational state hub — current WU, code state, deferred gates, build status.
audience: All
update-cadence: per-WU
state-type: current
status: CURRENT
last-verified: 2026-09-11 (v70 CLOSED at beat 8 — `ci` on `cc05a54` RED at lifecycle, sample #10 with FIX-2a's reading, read and filed (2 processors; H1–H4); FIX-2b-i ISSUE-READY (16878 B); the gate word to Nick; v71 on the intakes, Fri 2026-09-11 ~21:1x CT (2026-09-12T02:14Z). Order: hivemind 6 = 4 M + 2 A by explicit paths (the HERO-1b return unstaged until its audit). Detail: pm-handoff v70 beat 8.) Prior: 2026-09-11 (v70 CLOSED at beat 7 — FIX-2a returned + audited ACCEPT (the desk does not reproduce the class); EXPLAIN on ci green; the close packet; H8A owed; v71 on the intakes, Fri 2026-09-11 ~20:2x CT (2026-09-12T01:23Z). Order: hivemind 15 = 7 M + 8 A, beats 3–7 + the FIX-2a lane's three rows, one card (computed from porcelain inside the splice); core 6 = 2 M + 4 A (FIX-2a, Nick's card); docs 1 = 0 M + 1 A (AMD-100). Detail: pm-handoff v70 beat 7.) Prior: THE FULL PRIOR CHAIN verbatim at context/handoff/archive/chains-pre-region-cap-2026-08-23.md + archive/chains-rotated-2026-08-27.md; rolled-off segments: the pm-handoff `:8` chain + its archives.
-->
# Project Snapshot

> **How to read this file:** the frontmatter `last-verified:` chain above (2 pointer segments + the rotation pointer) is the session record; the body below is an OVERWRITTEN DIGEST (W-HIVE-1 P9, ≤2 KB) — rewritten every beat, never appended. The chain and the newest pm-handoff beat block outrank everything else. **The operator's copy-source of record is the file on disk, never a chat card.** Full history: `context/handoff/archive/chains-pre-region-cap-2026-08-23.md` + `archive/PROJECT_SNAPSHOT-priors-rotated-2026-08-21.md`.

## The digest (v70 CLOSED at beat 8 — `ci` on `cc05a54` RED with a reading; FIX-2b-i ISSUE-READY; the gate word to Nick, Fri 2026-09-11 ~21:1x CT)

**State:** core `cc05a54` (FIX-2a landed; **`ci` RED at lifecycle, sample #10, READ** — `context/audits/2026-09-11_CI-cc05a54_red-read_first-diagnostic_v70-b8.md`); hivemind `fe224e4` + beat 8 (Nick's card); docs `73c204b`. **The class:** real on 2-vCPU hosts; the stall after `automation_triggered`; H1–H4. **FIX-2b-i (Java; ISSUE-READY):** `…FIX-2b-i_bus-stall_pending-depth-and-thread-dump_coding-instruction.md` (`pendingDepth` · the VT dump · the pinned-thread trace; 11 M + 2 A); FIX-2b-ii on the first dump-bearing red. **The word:** `GATE: scoped` (default) | `strict` — EXPLAIN-114a dispatches after FIX-2b-i's landing under scoped, after FIX-2b-ii's green under strict. **Lanes:** HERO-1b RETURNED (v71 audits) · P-1 after both · R-4c Saturday. **The packet:** `_scratch/v70/2026-09-12_v70_close-2_operator-packet.md` (acts A–G). **Owed:** `FIX2BI:` · `H8A:` · `CI:` (frontend · install-smoke) · `AMD100:` · `PROTECT: done`. **HEADs:** core `cc05a54` · docs `73c204b` · skills `c630c5c` · bench `4539f13`. Check 9 STALE. **v71:** packet act G.

**Open risks:** six (FAILCHAN rides H8-a, record owed · BUS-SILENT-DROP: sample #10 RED with a reading; FIX-2b-i on the paste · four standing). Fences: one lane per path-domain (D4) · no batched pushes · the rig exclusive · FENCE-BUS · s31/nightly hands off · no B-2/B-3 code before C-003 · no public brand use before the opinion · no name graded in chat · 09-18 · the hub never commits or pushes.

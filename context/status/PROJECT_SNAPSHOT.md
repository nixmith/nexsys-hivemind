<!--
file: context/status/PROJECT_SNAPSHOT.md
purpose: Current operational state hub — current WU, code state, deferred gates, build status.
audience: All
update-cadence: per-WU
state-type: current
status: CURRENT
last-verified: 2026-09-11 (v70 CLOSED at beat 7 — FIX-2a returned + audited ACCEPT (the desk does not reproduce the class); EXPLAIN on ci green; the close packet; H8A owed; v71 on the intakes, Fri 2026-09-11 ~20:2x CT (2026-09-12T01:23Z). Order: hivemind 15 = 7 M + 8 A, beats 3–7 + the FIX-2a lane's three rows, one card (computed from porcelain inside the splice); core 6 = 2 M + 4 A (FIX-2a, Nick's card); docs 1 = 0 M + 1 A (AMD-100). Detail: pm-handoff v70 beat 7.) Prior: 2026-09-11 (v70 beat 6 — P-1 chartered (10518 B; design + a --dry-run driver with safety limits; the live leg gated on R-5 or `HARNESS-PLUG:`); the OR-BUS-SILENT-DROP status line; the last block; next b7 the H8-a intake, b8 the close, Fri 2026-09-11 ~18:2x CT (2026-09-11T23:29Z). Order: hivemind 10 = 4 M + 6 A, beats 3–6 in one card (computed from porcelain inside the splice); docs 1 = 0 M + 1 A (AMD-100). Detail: pm-handoff v70 beat 6.) Prior: THE FULL PRIOR CHAIN verbatim at context/handoff/archive/chains-pre-region-cap-2026-08-23.md + archive/chains-rotated-2026-08-27.md; rolled-off segments: the pm-handoff `:8` chain + its archives.
-->
# Project Snapshot

> **How to read this file:** the frontmatter `last-verified:` chain above (2 pointer segments + the rotation pointer) is the session record; the body below is an OVERWRITTEN DIGEST (W-HIVE-1 P9, ≤2 KB) — rewritten every beat, never appended. The chain and the newest pm-handoff beat block outrank everything else. **The operator's copy-source of record is the file on disk, never a chat card.** Full history: `context/handoff/archive/chains-pre-region-cap-2026-08-23.md` + `archive/PROJECT_SNAPSHOT-priors-rotated-2026-08-21.md`.

## The digest (v70 CLOSED at beat 7 — FIX-2a ACCEPT, landing on Nick's card; the close packet; v71 opens on the intakes, Fri 2026-09-11 ~20:2x CT)

**State:** core `1e26912` + FIX-2a's 6 (test-only; Nick's card) — its `ci` run is the gate of record and the class's sample #10 with the soak; hivemind `138e988` + beats 3–7 + the lane's rows (one card); docs `876a395` + AMD-100 (one card). **FIX-2a:** ACCEPT (`context/audits/2026-09-11_FIX-2a_intake_two-layer-audit_v70-b7.md`): the desk does not reproduce the class (143 loops, 0 anomalies); FIX-2b on the first diagnostic-bearing red or TR-1b's reading. **Lanes:** EXPLAIN-114a on `ci` green (act 6) · HERO-1b act 5 · P-1 after both · R-4c Saturday. **The packet:** `_scratch/v70/2026-09-12_v70_close_operator-packet.md` (eight acts, whole). **Owed:** `H8A:` · `CI:` · `LANDED v70` · `HERO1B:` · `EXPLAIN:` · `AMD100:` · `PROTECT: done` · `ERIK:`. **HEADs:** core `1e26912` · docs `876a395` · skills `c630c5c` · bench `4539f13`. Check 9 STALE. **v71:** the stable prompt; packet act 8.

**Open risks:** six (FAILCHAN rides H8-a, record owed · BUS-SILENT-DROP: the desk does not reproduce; the runner samples with the soak from the landing; FIX-2b on the first diagnostic-bearing red · four standing). Fences: one lane per path-domain (D4) · no batched pushes · the rig exclusive · FENCE-BUS · s31/nightly hands off · no B-2/B-3 code before C-003 · no public brand use before the opinion · no name graded in chat · 09-18 · the hub never commits or pushes.

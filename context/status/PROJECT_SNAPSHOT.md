<!--
file: context/status/PROJECT_SNAPSHOT.md
purpose: Current operational state hub — current WU, code state, deferred gates, build status.
audience: All
update-cadence: per-WU
state-type: current
status: CURRENT
last-verified: 2026-09-13 (v72 beat 3, BUS-ORDER-1 LANDED core `a458a64` (16 files) by Nick's hands; CI GREEN on `check` and `bus-soak` (sample #16 = the closure counter's 1/20); the deferred gate RESOLVED; the instruction EXECUTED; the window's deliverable MET; `AMD101: ratify` asked; hivemind `2fabfc7`; Sun 2026-09-13 ~06:5x CT (2026-09-13T11:54Z). Order: hivemind 5 = 5 M + 0 A by explicit paths (computed from porcelain inside the splice); docs 1 M held for the word. Detail: pm-handoff v72 beat 3.) Prior: 2026-09-13 (v72 beat 2, BUS-ORDER-1 RETURNED (14,215 B; 16 = 14 M + 2 A) and audited ACCEPT — R1–R3 accepted, R4 → the AMD-101 §4 rider, O1 pinned; the gate re-derived from Nick's `check` XMLs (240/413/81/30, 0 failed); the core card handed; Sun 2026-09-13 ~06:3x CT (2026-09-13T11:31Z). Order: hivemind 8 = 6 M + 2 A by explicit paths (computed from porcelain inside the splice); core 16 (Nick's hands); docs 1 M held. Detail: pm-handoff v72 beat 2.) Prior: THE FULL PRIOR CHAIN verbatim at context/handoff/archive/chains-pre-region-cap-2026-08-23.md + archive/chains-rotated-2026-08-27.md; rolled-off segments: the pm-handoff `:8` chain + its archives.
-->
# Project Snapshot

> **How to read this file:** the frontmatter `last-verified:` chain above (2 pointer segments + the rotation pointer) is the session record; the body below is an OVERWRITTEN DIGEST (W-HIVE-1 P9, ≤2 KB) — rewritten every beat, never appended. The chain and the newest pm-handoff beat block outrank everything else. **The operator's copy-source of record is the file on disk, never a chat card.** Full history: `context/handoff/archive/chains-pre-region-cap-2026-08-23.md` + `archive/PROJECT_SNAPSHOT-priors-rotated-2026-08-21.md`.

## The digest (v72 at beat 3 — BUS-ORDER-1 landed `a458a64`, CI green; the deliverable met; AMD-101 ready to ratify, Sun 2026-09-13 ~06:5x CT)

**State:** core `a458a64` (BUS-ORDER-1: the cursor delivers, the checkpoint floors, the notification wakes; `check` + `bus-soak` GREEN = sample #16, the closure counter's 1/20); hivemind `2fabfc7` + b3; docs `0d62a54` + AMD-101's §6 exhibit, §4 INV-BUS-01 rider and §7 ticks (1 M, held for the word). **The bus class:** (1) the soak's stall — instrumented (`72efb42`); (2) the census's head-miss — kind E, removed by BUS-ORDER-1 with the drain's two-position drop beside it. **Ruled:** `BUSFIX: b`; the revert clock STOPPED; the deferred gate RESOLVED at `a458a64`. **The word due:** `AMD101: ratify` (three §4 edits + the §6 exhibit on one docs card). **The rest of v72:** HERO-1c's charter (ahead of `FE: 6af76f7`) → 114b (DISABLED-2 and two refactors; the Java domain free) → the R-4c and H8-a intakes → the v1.1.4 freeze note. **Owed:** `AMD101:` · `H8A:` · `R4C:` · `FE: 6af76f7` · `AMD100:` · `PROTECT: done`. Check 9 STALE (the known file).

**Open risks:** six (FAILCHAN rides H8-a · BUS-SILENT-DROP: BUS-ORDER-1 landed; the counter 1/20 · four standing). Fences: one lane per path-domain (D4) · no batched pushes · the rig exclusive · FENCE-BUS · s31/nightly hands off · no B-2/B-3 code before C-003 · no public brand use before the opinion · no name graded in chat · 09-18 · the hub never commits or pushes.

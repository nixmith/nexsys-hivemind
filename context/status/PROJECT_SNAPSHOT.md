<!--
file: context/status/PROJECT_SNAPSHOT.md
purpose: Current operational state hub — current WU, code state, deferred gates, build status.
audience: All
update-cadence: per-WU
state-type: current
status: CURRENT
last-verified: 2026-09-13 (v72 beat 4, AMD-101 RATIFIED on Nick's word (`context/planning/2026-09-13_v72_AMD101-ratify_ruling-of-record.md`; his six checks run at the bytes, two readings corrected); five edits executed in the docs tree (AMD-101, Doc 01 head/§3.4/§9, INV-BUS-01, INV-PROJ-04 = 3 M, the card handed); the BUSFIX-b revert condition VOID; hivemind `de48f32`; Sun 2026-09-13 ~07:3x CT (2026-09-13T12:32Z). Order: docs 3 M by explicit paths (Nick's hands); hivemind 7 = 6 M + 1 A by explicit paths (computed from porcelain inside the splice). Detail: pm-handoff v72 beat 4.) Prior: 2026-09-13 (v72 beat 3, BUS-ORDER-1 LANDED core `a458a64` (16 files) by Nick's hands; CI GREEN on `check` and `bus-soak` (sample #16 = the closure counter's 1/20); the deferred gate RESOLVED; the instruction EXECUTED; the window's deliverable MET; `AMD101: ratify` asked; hivemind `2fabfc7`; Sun 2026-09-13 ~06:5x CT (2026-09-13T11:54Z). Order: hivemind 5 = 5 M + 0 A by explicit paths (computed from porcelain inside the splice); docs 1 M held for the word. Detail: pm-handoff v72 beat 3.) Prior: THE FULL PRIOR CHAIN verbatim at context/handoff/archive/chains-pre-region-cap-2026-08-23.md + archive/chains-rotated-2026-08-27.md; rolled-off segments: the pm-handoff `:8` chain + its archives.
-->
# Project Snapshot

> **How to read this file:** the frontmatter `last-verified:` chain above (2 pointer segments + the rotation pointer) is the session record; the body below is an OVERWRITTEN DIGEST (W-HIVE-1 P9, ≤2 KB) — rewritten every beat, never appended. The chain and the newest pm-handoff beat block outrank everything else. **The operator's copy-source of record is the file on disk, never a chat card.** Full history: `context/handoff/archive/chains-pre-region-cap-2026-08-23.md` + `archive/PROJECT_SNAPSHOT-priors-rotated-2026-08-21.md`.

## The digest (v72 at beat 4 — AMD-101 RATIFIED; the docs card in Nick's hands; HERO-1c's charter next, Sun 2026-09-13 ~07:3x CT)

**State:** core `a458a64` (BUS-ORDER-1; CI green; the closure counter 1/20); hivemind `de48f32` + b4; docs `0d62a54` + 3 M (AMD-101 RATIFIED; Doc 01 §3.4/§9/head; INV-BUS-01 and INV-PROJ-04) on the card. **The bus class:** kind E removed at `a458a64`, named in Doc 01 §3.4 and the register; the run-hand-off face stays OR-BUS-SILENT-DROP's open question; samples can still show `LIVE_READ_FAILED` and `NOTIFY_NOT_VISIBLE`. **Ruled:** `BUSFIX: b` (the revert condition VOID) · `AMD101: ratify` (the ruling of record filed, two readings corrected). **The rest of v72:** HERO-1c's charter (b5, ahead of `FE: 6af76f7`) → 114b (the Java domain free) → the R-4c and H8-a intakes → the v1.1.4 freeze note. **Owed:** `DOCS:` · `HIVE:` · `H8A:` · `R4C:` · `FE: 6af76f7` · `AMD100:` · `PROTECT: done`. Check 9 STALE (the known file).

**Open risks:** six (FAILCHAN rides H8-a · BUS-SILENT-DROP: the counter 1/20; the hand-off face open · four standing). Fences: one lane per path-domain (D4) · no batched pushes · the rig exclusive · FENCE-BUS · s31/nightly hands off · no B-2/B-3 code before C-003 · no public brand use before the opinion · no name graded in chat · 09-18 · the hub never commits or pushes.

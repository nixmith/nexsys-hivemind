<!--
file: context/status/PROJECT_SNAPSHOT.md
purpose: Current operational state hub — current WU, code state, deferred gates, build status.
audience: All
update-cadence: per-WU
state-type: current
status: CURRENT
last-verified: 2026-09-13 (v72 beat 2, BUS-ORDER-1 RETURNED (14,215 B; 16 = 14 M + 2 A) and audited ACCEPT — R1–R3 accepted, R4 → the AMD-101 §4 rider, O1 pinned; the gate re-derived from Nick's `check` XMLs (240/413/81/30, 0 failed); the core card handed; Sun 2026-09-13 ~06:3x CT (2026-09-13T11:31Z). Order: hivemind 8 = 6 M + 2 A by explicit paths (computed from porcelain inside the splice); core 16 (Nick's hands); docs 1 M held. Detail: pm-handoff v72 beat 2.) Prior: 2026-09-12 (v72 beat 1, THE BOOT AND THE SAMPLE #15 READ — kind E (`NOTIFY_SKIPPED_LIVE`, `automation_engine`, position 206, checkpoint 207; census 254/254); the revert clock STOPPED; BUS-ORDER-1's gate met at `5f918c7`, §8 handed as the one act; the §6 exhibit in the docs tree; v70 b5–b9 rotated; Sat 2026-09-12 ~19:5x CT (2026-09-13T00:53Z). Order: hivemind 8 = 6 M + 2 A by explicit paths (computed from porcelain inside the splice); docs 1 M held. Detail: pm-handoff v72 beat 1.) Prior: THE FULL PRIOR CHAIN verbatim at context/handoff/archive/chains-pre-region-cap-2026-08-23.md + archive/chains-rotated-2026-08-27.md; rolled-off segments: the pm-handoff `:8` chain + its archives.
-->
# Project Snapshot

> **How to read this file:** the frontmatter `last-verified:` chain above (2 pointer segments + the rotation pointer) is the session record; the body below is an OVERWRITTEN DIGEST (W-HIVE-1 P9, ≤2 KB) — rewritten every beat, never appended. The chain and the newest pm-handoff beat block outrank everything else. **The operator's copy-source of record is the file on disk, never a chat card.** Full history: `context/handoff/archive/chains-pre-region-cap-2026-08-23.md` + `archive/PROJECT_SNAPSHOT-priors-rotated-2026-08-21.md`.

## The digest (v72 at beat 2 — BUS-ORDER-1 returned and accepted; the core card in Nick's hands, Sun 2026-09-13 ~06:3x CT)

**State:** core `5f918c7` + BUS-ORDER-1 on disk (16 = 14 M + 2 A; `check` GREEN on the desk; the card handed); hivemind `7210fb1` + b2; docs `0d62a54` + AMD-101's §6 exhibit and §4 INV-BUS-01 rider (1 M, held). **The bus class:** (1) the soak's stall — instrumented (`72efb42`); (2) the census's head-miss — a notify-order artefact on a non-monotonic checkpoint; kind E its harmful arm; sample #15 its first line; BUS-ORDER-1 removes the arm (the cursor delivers, the checkpoint floors, the notify wakes) and the drain's two-position drop T2 found beside it. **Ruled:** `BUSFIX: b`; the revert clock STOPPED. **v72's deliverable:** BUS-ORDER-1 landed and CI green on it (the closure counter's first sample); then HERO-1c's charter → 114b → `AMD101: ratify` (the §4 edits + the §6 exhibit, one docs card) → the R-4c and H8-a intakes. **Owed:** `CORE: LANDED` · `CI:` · `H8A:` · `R4C:` · `FE: 6af76f7` · `AMD100:` · `PROTECT: done`. Check 9 STALE (the known file).

**Open risks:** six (FAILCHAN rides H8-a · BUS-SILENT-DROP: BUS-ORDER-1 accepted, landing; the counter restarts at the landing · four standing). Fences: one lane per path-domain (D4) · no batched pushes · the rig exclusive · FENCE-BUS · s31/nightly hands off · no B-2/B-3 code before C-003 · no public brand use before the opinion · no name graded in chat · 09-18 · the hub never commits or pushes.

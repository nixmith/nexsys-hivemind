<!--
file: context/status/PROJECT_SNAPSHOT.md
purpose: Current operational state hub — current WU, code state, deferred gates, build status.
audience: All
update-cadence: per-WU
state-type: current
status: CURRENT
last-verified: 2026-09-11 (v69 beat 4 — EXPLAIN-114a authored (30 KB; v1.1.4 additive, five read-time keys; 13 M + 0 A expected); HERO-1 landed `1e26912`; beats 2–3 `d0bcc1e`; `ci` RED at lifecycle:test on the design-only commit — artifact first, EXPLAIN paste held; next the H8-a paste 18:45 CT, then R-4c's packet, Fri 2026-09-11 ~16:4x CT (2026-09-11T21:44Z). Order: hivemind 5 = 4 M + 1 A (computed from porcelain inside the splice). Detail: pm-handoff v69 beat 4.) Prior: 2026-09-11 (v69 beat 3 — HERO-1 returned + audited ACCEPT; the landing cards, HERO1 Q1–Q7 and EXPLAIN: three|one handed; four v67 blocks rotated; next b4 EXPLAIN-114a; H8-a tonight 19:00 CT, Fri 2026-09-11 ~16:2x CT (2026-09-11T21:28Z). Order: hivemind 8 = 4 M + 4 A (computed from porcelain inside the splice). Detail: pm-handoff v69 beat 3.) Prior: THE FULL PRIOR CHAIN verbatim at context/handoff/archive/chains-pre-region-cap-2026-08-23.md + archive/chains-rotated-2026-08-27.md; rolled-off segments: the pm-handoff `:8` chain + its archives.
-->
# Project Snapshot

> **How to read this file:** the frontmatter `last-verified:` chain above (2 pointer segments + the rotation pointer) is the session record; the body below is an OVERWRITTEN DIGEST (W-HIVE-1 P9, ≤2 KB) — rewritten every beat, never appended. The chain and the newest pm-handoff beat block outrank everything else. **The operator's copy-source of record is the file on disk, never a chat card.** Full history: `context/handoff/archive/chains-pre-region-cap-2026-08-23.md` + `archive/PROJECT_SNAPSHOT-priors-rotated-2026-08-21.md`.

## The digest (v69 beat 4 — EXPLAIN-114a authored; H8-a tonight, Fri 2026-09-11 ~16:4x CT)

**State:** core `1e26912` (HERO-1 landed; **`ci` RED at `:lifecycle:lifecycle:test` — unread; the artifact is the next act; a design-only commit**); hivemind `d0bcc1e` + this beat (4 M + 1 A, Nick's card); both core slots free; the EXPLAIN-114a paste HELD on the red. **The deliverable:** `context/instructions/2026-09-11_coder-lane_EXPLAIN-114a_read-API-v1.1.4-additive_coding-instruction.md` — v1.1.4 additive: `trigger.firingValue`, `actions[].settledAt`/`confirmedAt`, `definitionKey`, `disabledAt`/`disabledReason`, `FIRED_CONFIRMED`; its paste is HELD until the `1e26912` red is read; 114b/114c follow under `EXPLAIN: three`. **HERO-1:** landed; ruled (a) ×7; HERO-1b next. **Tonight:** H8-a 19:00 CT; the 18:45 send armed (`trig_01AHRS3Q29MtP6q39yT24ogs`). **Then:** R-4c Sat 09-12 (measurement-only; packet next) · P-1's charter · TR-1b · W-SKILLS-9. **HEADs:** core `eabdbb1` · docs `876a395` · skills `c630c5c` · bench `4539f13`. **Ruled:** `HERO1:` (a) ×7 · `EXPLAIN: three`. **Open:** `CI: saved` · `FIX2:` · `PROTECT: done` · `H8A:` · `R4C:` · `ERIK:` · `Activate:` 09-15. Check 9 STALE until the mirror sync.

**Open risks:** six (FAILCHAN rides H8-a · BUS-SILENT-DROP: sample #9 RED, `HeroLoopHardwareFreeIT :614`; artifact next; FIX-2 next · four standing). Fences: one lane per path-domain (D4) · no batched pushes · the rig exclusive · FENCE-BUS · s31/nightly hands off · no B-2/B-3 code before C-003 · no public brand use before the opinion · no name graded in chat · 09-18 · the hub never commits or pushes.

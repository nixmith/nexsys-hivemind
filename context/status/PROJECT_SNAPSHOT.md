<!--
file: context/status/PROJECT_SNAPSHOT.md
purpose: Current operational state hub — current WU, code state, deferred gates, build status.
audience: All
update-cadence: per-WU
state-type: current
status: CURRENT
last-verified: 2026-09-10 (v68 beat 4 — HONESTY-1 returned + ACCEPT at the bytes; R1 applied (core 14 M); LASTREPORTED-1b docketed instrument-first; the landing card handed; FE-NULL-1 running, Thu ~18:4x CT (2026-09-10T23:39Z). Order: hivemind 7 = 5 M + 2 A (computed from porcelain inside the splice; coder-handoff.md is the lane's write, staged with its audit). Detail: pm-handoff v68 beat 4.) Prior: 2026-09-10 (v68 beat 3 — the close card banked (hivemind + docs pushed); HONESTY-1 running; FE-NULL-1 authored and handed (the second slot, D4); H8-a defaults Fri 19:00 CT, Thu ~18:1x CT (2026-09-10T23:04Z). Order: hivemind 5 = 4 M + 1 A (computed from porcelain inside the splice). Detail: pm-handoff v68 beat 3.) Prior: THE FULL PRIOR CHAIN verbatim at context/handoff/archive/chains-pre-region-cap-2026-08-23.md + archive/chains-rotated-2026-08-27.md; rolled-off segments: the pm-handoff `:8` chain + its archives.
-->
# Project Snapshot

> **How to read this file:** the frontmatter `last-verified:` chain above (2 pointer segments + the rotation pointer) is the session record; the body below is an OVERWRITTEN DIGEST (W-HIVE-1 P9, ≤2 KB) — rewritten every beat, never appended. The chain and the newest pm-handoff beat block outrank everything else. **The operator's copy-source of record is the file on disk, never a chat card.** Full history: `context/handoff/archive/chains-pre-region-cap-2026-08-23.md` + `archive/PROJECT_SNAPSHOT-priors-rotated-2026-08-21.md`.

## The digest (v68 beat 4 — HONESTY-1 ACCEPTED, THE LANDING IN NICK'S HANDS; FE-NULL-1 RUNNING, Thu 2026-09-10 ~18:4x CT)

**THE PROGRAM (the map: `context/planning/2026-09-10_v68_MOMENTUM-MAP_…md`):** **HONESTY-1 RETURNED + ACCEPT** (`context/audits/2026-09-10_HONESTY-1_return.md` · the audit `…_intake_two-layer-audit_v68-b4.md`): the census 13 M verified + R1 applied by the hub (`EntityState` javadoc) = **14 M on core, uncommitted — Nick's landing card is the brief's §NEXT** (the 14 paths by name; msg `_scratch/2026-09-10_core_HONESTY-1_commit-msg.txt`). **Wait-state:** `ci` green + `install-smoke` RAN on the push (P4) → Act 12 retires → **EXPLAIN v1.1.4 dispatches** (the hub authors it now). **LASTREPORTED-1b** docketed instrument-first (R-4c reads `lastReported` on one never-reported entity; a `projectionVersion` bump only if the stamp persists). **Slot 2:** FE-NULL-1 RUNNING (launched ~18:2x CT; `web-ui/` porcelain 0 at 23:33Z; return = `context/audits/<date>_FE-NULL-1_return.md`). **H8-a:** Fri 09-11 19:00 CT (default; the paste at 18:45). **R-4c:** Sat 09-12 (the hub authors it). **THE BRAND:** a wait-state (`ERIK:`). **HEADs:** core `39c8dd3` + 14 M · hivemind = this beat (1 to push; rides the next card) · skills `c630c5c` · bench `4539f13` · docs `876a395`. **WORDS OPEN:** `H8:` · `R4C:` · `ERIK:` · `Activate:` 09-15.

**OPEN RISKS:** seven (OR-HONESTY-1-GATE new — closes on CI green + install-smoke ran · FAILCHAN rides H8-a · BUS-SILENT-DROP 5/20; the three veto samples owed). Fences: one lane per PATH-DOMAIN (D4) · no batched pushes · the rig exclusive · FENCE-BUS · s31/nightly HANDS OFF · no B-2/B-3 code before C-003 · no public brand use before the opinion · no name graded in chat · 09-18.

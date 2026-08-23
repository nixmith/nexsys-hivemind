<!--
file: context/status/PROJECT_SNAPSHOT.md
purpose: Current operational state hub — current WU, code state, deferred gates, build status.
audience: All
update-cadence: per-WU
state-type: current
status: CURRENT
last-verified: 2026-08-23 (v56 hub, beat 5 — R-7b AUDITED ACCEPT (@v6 ruled IN) + the card sitting BANKED (R-1/R-2 hardware half PROVEN; boot-health 6/6; P-1 + digests banked). Orders: core 11 M · hivemind 7. Detail: pm-handoff beat 5.) Prior: 2026-08-23 (v56 beat 4 — R-9 LANDED e845cd9 + §OP-A/H green — R-6/R-8 + R-9 CLOSED; the interim operator law RETIRED; the rotation executed (region caps live). Detail: pm-handoff beat 4.) Prior: THE FULL PRIOR CHAIN verbatim at context/handoff/archive/chains-pre-region-cap-2026-08-23.md (rotated v56 beat 4); earlier eras per context/status/archive/.
-->
# Project Snapshot

> **How to read this file:** the frontmatter `last-verified:` chain above (2 pointer segments + the rotation pointer) is the session record; the body below is an OVERWRITTEN DIGEST (W-HIVE-1 P9, ≤2 KB) — rewritten every beat, never appended. The chain and the newest pm-handoff beat block outrank everything else. Full history: `context/handoff/archive/chains-pre-region-cap-2026-08-23.md` + `archive/PROJECT_SNAPSHOT-priors-rotated-2026-08-21.md`.

## The digest (v56 beat 5 — 2026-08-23)

**HEADs:** core `e845cd9` + the R-7b delivery (11 M dirty; the census-exact order is OUT — queue b5; after Nick lands it, NOTHING touches the core checkout until R-3b) · hivemind `523abf5` + this beat (7-file order OUT) · skills `5105abc` · bench `4539f13` · docs `a53f474`. **Bench:** at `e845cd9`; §OP-A+H green 2026-08-23 12:11–12:16 CT (13:11–13:16 ET; F-S21); boot-health 6/6 ×2 (the §OP-H run + the card-sitting restore). **The held card:** OUT, labeled `hs-fresh — R-3/R-4 rig — 7c9e4fa`; HOLD-PATCH through R-4 (F-S12).

**Closed this weekend:** R-1/R-2 (code+CI+**hardware** — the sitting's RED 7/10 → GREEN 0/14 + 18/18) · R-6/R-8 · R-7 · R-9. **In flight:** the R-7b landing (Nick's queue). **Dispatch-ready:** W-SKILLS-4 (Mon) · FE-SWAP-GATE (Nick's word) · RS-3 (Aug-31/tripwire). **Owed to the hub:** the R-7b CI verdict lines (paste or API at the next beat).

**Fences:** the D-1 DO-NOT-SAY pair until R-4 · `distribution/README.md:117` until W2-3 · no public brand use before G-2 · s31 legs/nightly HANDS OFF until R-5 · R-7b lands BEFORE R-3b installs any CI artifact · the hub never implements.

**The next three acts:** (1) Nick runs queue b5 (the `@v6` flip → the two held verification lines → core 11 M → CI glance → hivemind 7). (2) Fri: the R-3a finalization — F-S9 (the block CREATES the token-absent condition) + F-S15 (`bench.sh start` in every restore block) + F-S11 (the SD-5 fence explicit) folded; Block I pins the R-7b run id + sha256 line. (3) Mon/Tue W-SKILLS-4 + P6 + v57 lean → Wed/Thu Pelton → the ONE word → the swap → Aug-29/30 R-3a → R-3b → R-4 → THE FENCE LIFT. Plan: `context/planning/2026-08-23_pelton-week_plan-of-record.md`.

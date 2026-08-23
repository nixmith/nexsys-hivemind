<!--
file: context/status/PROJECT_SNAPSHOT.md
purpose: Current operational state hub — current WU, code state, deferred gates, build status.
audience: All
update-cadence: per-WU
state-type: current
status: CURRENT
last-verified: 2026-08-23 (v56 hub, beat 4 — R-9 LANDED e845cd9 + §OP-A/H green — R-6/R-8 + R-9 CLOSED; the interim operator law RETIRED; the rotation executed (region caps live). Order: hivemind 7. Detail: pm-handoff beat 4.) Prior: 2026-08-22 (v56 beat 3 — R-9 returned + audited ACCEPT; the 24-path core order issued. Detail: pm-handoff beat 3.) Prior: THE FULL PRIOR CHAIN verbatim at context/handoff/archive/chains-pre-region-cap-2026-08-23.md (rotated v56 beat 4); earlier eras per context/status/archive/.
-->
# Project Snapshot

> **How to read this file:** the frontmatter `last-verified:` chain above (2 pointer segments + the rotation pointer) is the session record; the body below is an OVERWRITTEN DIGEST (W-HIVE-1 P9, ≤2 KB) — rewritten every beat, never appended. The chain and the newest pm-handoff beat block outrank everything else. Full history: `context/handoff/archive/chains-pre-region-cap-2026-08-23.md` + `archive/PROJECT_SNAPSHOT-priors-rotated-2026-08-21.md`.

## The digest (v56 beat 4 — 2026-08-23)

**HEADs:** core `e845cd9` (R-9/E3-HEALTH landed; R-1..R-2, R-6..R-9 all CLOSED; CI green Nick-reported, job lines bank at the R-7b intake) · hivemind `2b84fce` + this beat · skills `5105abc` · bench `4539f13` · docs `a53f474`. **Bench:** rebuilt at `e845cd9`; §OP-A+H green 2026-08-23 13:11–13:16 CT; boot-health PASS 6/6.

**In flight:** R-7b (host-CC lane, 11 M, baseline `e845cd9`) — then nothing on the core checkout until R-3b. **Dispatch-ready:** W-SKILLS-4 (Mon) · FE-SWAP-GATE (Nick's word) · RS-3 (Aug-31/tripwire). **Owed to the hub:** Blocks 1–3 ⏺s (the card sitting; TODAY daylight) · the Aug-22/23 nightly digest lines · P-1 (the 02P read).

**Fences:** the D-1 DO-NOT-SAY pair until R-4 · `distribution/README.md:117` until W2-3 · no public brand use before G-2 · s31 legs/nightly HANDS OFF until R-5 · R-7b lands BEFORE R-3b installs any CI artifact · the hub never implements. (The INTERIM OPERATOR LAW retired v56 beat 4.)

**The next three acts:** (1) the R-7b intake → audit → land → CI (zero Node-20 annotations; the `+git` version). (2) Blocks 1–3 → the R-3 packet finalized (E3-RED → Block I → E3-GREEN → A-1…; the ⏺ slots + the run id). (3) Mon/Tue: W-SKILLS-4 + P6 + v57 banked lean → Wed/Thu Pelton → the ONE branch word → the swap + B-1/B-7/B-2 → Aug-29/30 R-3 → R-4 → THE FENCE LIFT. Plan of record: `context/planning/2026-08-23_pelton-week_plan-of-record.md`.

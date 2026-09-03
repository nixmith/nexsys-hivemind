<!--
file: context/status/PROJECT_SNAPSHOT.md
purpose: Current operational state hub — current WU, code state, deferred gates, build status.
audience: All
update-cadence: per-WU
state-type: current
status: CURRENT
last-verified: 2026-09-03 (v61 beat 11 — post-close intake, Thu ~07:35 — both lanes returned + audited in one intake: the s31 read ACCEPT (H-D; the 'missed' corrected — 09-03 fired late, PASSED 8/9) · PKG-SEC-2 ACCEPT-WITH-RULINGS (the permit-join default removal accepted; Doc 12 :133 proceed + a note; the msg file for Nick). Order: hivemind 12 = 8 M + 4 A. Detail: pm-handoff v61 beat 11.) Prior: 2026-09-03 (v61 CLOSE — FINAL, beat 10, Thu ~06:35 — F-R4-1 LANDED a1c6966 + CI GREEN (banked); three pushes banked; the 09-02 floor breach (7/9, FAIL s31) → OR-NIGHTLY-0902-S31 + the read-only evidence read ordered; the 09-03 nightly MISSED; Check 9 FAILED-PARTIAL (folders owed); PKG-SEC-2 dispatch line handed; the close RAN (six mints; the v62 prompt LIVE-FINAL). Order: hivemind 7 = 6 M + 1 A. Detail: pm-handoff v61 CLOSE — FINAL.) Prior: THE FULL PRIOR CHAIN verbatim at context/handoff/archive/chains-pre-region-cap-2026-08-23.md + archive/chains-rotated-2026-08-27.md; rolled-off segments: the pm-handoff `:8` chain + its archives.
-->
# Project Snapshot

> **How to read this file:** the frontmatter `last-verified:` chain above (2 pointer segments + the rotation pointer) is the session record; the body below is an OVERWRITTEN DIGEST (W-HIVE-1 P9, ≤2 KB) — rewritten every beat, never appended. The chain and the newest pm-handoff beat block outrank everything else. **The operator's copy-source of record is the file on disk, never a chat card.** Full history: `context/handoff/archive/chains-pre-region-cap-2026-08-23.md` + `archive/PROJECT_SNAPSHOT-priors-rotated-2026-08-21.md`.

## The digest (v61 beat 11 — post-close intake, Thu 2026-09-03, ~07:35)

**v61 CLOSES AT THIS BEAT; v62 boots from `context/handoff/2026-09-02_PM-mission-control_v62_orchestrator_session_prompt.md` (LIVE-FINAL, re-slotted b11).** HEADs: core **`a1c6966` + 10 uncommitted (PKG-SEC-2, audited ACCEPT-WITH-RULINGS) — NICK'S COMMIT NEXT** from `../_scratch/2026-09-03_core_PKG-SEC-2_commit-msg.txt`; CI = the gate of record · hivemind = this beat (ahead 2; origin at `ba4983b`) · skills `f9c0bf4` · bench `4539f13` · docs `a53f474`.

**PKG-SEC-2:** the zigbee fragment composes at Phase 1; **the `permit_join_duration: 120` default is REMOVED (security-relevant)** — absent = no window. **R-4b coupling: SET the key on the held card for the run; pre-validate its zigbee.yaml (step 0).** Doc 12 :133 note chartered (docs repo).

**THE FLOOR:** the 09-02 FAIL adjudicated — transport collateral from the suite's own `usb-reenumeration` leg; the reopen path resumes without NETWORK_UP (source-verified). **The 09-03 nightly fired late and PASSED 8/9 (the b10 'missed' was wrong).** Rows for Nick's word: REOPEN-NETUP (Core) · S31-SETTLE-AFTER-REENUM (bench, R-5). Fence stands.

**OPEN NOW:** Nick's PKG-SEC-2 commit + CI · the skill folder re-sync (Check 9) · the words (Fri–Sat) · Erik (nudge Fri midday) · E1 · R-4b's day. **v62 S2:** the Doc 12 note line · FAILCHAN · the R-4b packet · the two rows · CG. **NICK'S BRIEF:** `context/handoff/2026-09-02_v61_OPERATOR-BRIEF_for-Nick.md` (b11). Fences: no public brand use before the opinion · s31/nightly HANDS OFF until R-5 · one lane on the core tree · the hub never implements.

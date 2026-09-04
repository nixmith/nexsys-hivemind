<!--
file: context/status/PROJECT_SNAPSHOT.md
purpose: Current operational state hub — current WU, code state, deferred gates, build status.
audience: All
update-cadence: per-WU
state-type: current
status: CURRENT
last-verified: 2026-09-04 (v62 beat 5 — THE R-4b NAVIGATOR PACKET, Fri ~07:36 CT (12:36Z) — guard 1 as §0; the window timed to the plug's :54s cadence; three provocations; the §6-F announce-class fallback; C4 by path A/B; the FAILCHAN stop-proof at §5 iff it rides. Order: hivemind 4 = 3 M + 1 A. Detail: pm-handoff v62 beat 5.) Prior: 2026-09-04 (v62 beat 4 — THE FAILCHAN INTAKE, Fri ~07:29 CT (12:29Z) — the lane returned + audited ACCEPT-WITH-RULINGS at the bytes (19 = 14 M + 5 A; R1 · R2 ACCEPT; two instruction claims corrected by the lane, owned); the msg file + census card in Nick's hands; CI = the gate; R-4b is TODAY — the brief re-cut; the v63 skeleton. Order: hivemind 9 = 6 M + 3 A. Detail: pm-handoff v62 beat 4.) Prior: THE FULL PRIOR CHAIN verbatim at context/handoff/archive/chains-pre-region-cap-2026-08-23.md + archive/chains-rotated-2026-08-27.md; rolled-off segments: the pm-handoff `:8` chain + its archives.
-->
# Project Snapshot

> **How to read this file:** the frontmatter `last-verified:` chain above (2 pointer segments + the rotation pointer) is the session record; the body below is an OVERWRITTEN DIGEST (W-HIVE-1 P9, ≤2 KB) — rewritten every beat, never appended. The chain and the newest pm-handoff beat block outrank everything else. **The operator's copy-source of record is the file on disk, never a chat card.** Full history: `context/handoff/archive/chains-pre-region-cap-2026-08-23.md` + `archive/PROJECT_SNAPSHOT-priors-rotated-2026-08-21.md`.

## The digest (v62 beat 5 — the R-4b packet, Fri 2026-09-04 ~07:36 CT)

**v62 LIVE; TODAY IS R-4b.** Strategy **v1.2 RATIFIED** · the docket **RULED** · TIER-2 GO · EXITCODE a · FOP-DATES a · ORPHANS a. HEADs: core **`ef02d13` + 19 UNCOMMITTED (FAILCHAN, audited ACCEPT-WITH-RULINGS — Nick's commit from `../_scratch/2026-09-04_core_FAILCHAN_commit-msg.txt`; CI = the gate; guard 1)** · hivemind = this beat (ahead 2; origin at `f0ee4ee`) · skills `f9c0bf4` · bench `4539f13` · docs `a53f474`.

**THE PACKET IS ON DISK:** `context/handoff/2026-09-04_R-4b_navigator-packet_held-card.md` — §0 guard 1 (the artifact, by the Actions page) → §1 fetch → §2 swap → §3 step 0b → §4 install → §5 the measured boot (PKG-SEC-2's proof; the FAILCHAN stop-proof iff it rides) → §6 the arm (the window at a minute ≡ 0 mod 5; criterion 0; the §6-F fallback on a miss) → §7 C4 (re-bind; path A/B; the run + explanation) → §8 C1/C2/C3 at ≥45 min → §9 restore → §10 the mint. The hub navigates live.

**STANDING:** Erik midday · `BEYOND:` · E1 (outage; the hub retries) · `EU` 09-11 · `Activate` 09-15 · the docs block · CG after R-4b's audit (guard 2) · FE Sat · H8 Sun/Mon. **OPEN RISKS:** OR-NIGHTLY-0902-S31 (rows 17/18 pending) · OR-FAILCHAN (5 fixed-pending-CI; 6 residual) · OR-JOURNALD-PRIO RULED (a) · OR-REHOMED-OQ · OR-M13-SDNOTIFY HOLD. **v63 SKELETON** on disk. Fences: no public brand use before the opinion (09-18) · s31/nightly HANDS OFF until R-5 · one lane on the core tree · the hub never implements.

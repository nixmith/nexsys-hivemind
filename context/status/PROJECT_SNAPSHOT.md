<!--
file: context/status/PROJECT_SNAPSHOT.md
purpose: Current operational state hub — current WU, code state, deferred gates, build status.
audience: All
update-cadence: per-WU
state-type: current
status: CURRENT
last-verified: 2026-09-04 (v62 beat 4 — THE FAILCHAN INTAKE, Fri ~07:29 CT (12:29Z) — the lane returned + audited ACCEPT-WITH-RULINGS at the bytes (19 = 14 M + 5 A; R1 · R2 ACCEPT; two instruction claims corrected by the lane, owned); the msg file + census card in Nick's hands; CI = the gate; R-4b is TODAY — the brief re-cut; the v63 skeleton. Order: hivemind 9 = 6 M + 3 A. Detail: pm-handoff v62 beat 4.) Prior: 2026-09-04 (v62 beat 3 — THE FAILCHAN INSTRUCTION, Thu ~21:18 CT — authored on source at ef02d13 on the ruled words; Parts A/B/C; the `Restart=always` ruling reconciled inside; the exit seam per Nick's caveat; ten tests; census 18 = 13 M + 5 A; the dispatch line in the brief §A. Order: hivemind 5 = 4 M + 1 A. Detail: pm-handoff v62 beat 3.) Prior: THE FULL PRIOR CHAIN verbatim at context/handoff/archive/chains-pre-region-cap-2026-08-23.md + archive/chains-rotated-2026-08-27.md; rolled-off segments: the pm-handoff `:8` chain + its archives.
-->
# Project Snapshot

> **How to read this file:** the frontmatter `last-verified:` chain above (2 pointer segments + the rotation pointer) is the session record; the body below is an OVERWRITTEN DIGEST (W-HIVE-1 P9, ≤2 KB) — rewritten every beat, never appended. The chain and the newest pm-handoff beat block outrank everything else. **The operator's copy-source of record is the file on disk, never a chat card.** Full history: `context/handoff/archive/chains-pre-region-cap-2026-08-23.md` + `archive/PROJECT_SNAPSHOT-priors-rotated-2026-08-21.md`.

## The digest (v62 beat 4 — the FAILCHAN intake, Fri 2026-09-04 ~07:29 CT)

**v62 LIVE; THE SITTING IS DONE (09-03); TODAY IS R-4b.** Strategy **v1.2 RATIFIED** · the docket **RULED** · TIER-2 GO · EXITCODE a · FOP-DATES a · ORPHANS a. HEADs: core **`ef02d13` + 19 UNCOMMITTED (FAILCHAN, audited ACCEPT-WITH-RULINGS — Nick's commit from `../_scratch/2026-09-04_core_FAILCHAN_commit-msg.txt`; CI = the gate)** · hivemind = this beat (ahead 1; origin at `f0ee4ee`) · skills `f9c0bf4` · bench `4539f13` · docs `a53f474`.

**TODAY (the brief, b4):** §A commit + push FAILCHAN → read CI (guard 1: the FAILCHAN artifact rides R-4b only if both legs are GREEN before the install step) → **beat 5 the R-4b packet** (do not start before it is on disk) → R-4b ~3 h (criterion 0 first; the criterion-0-miss fallback; the first `systemctl stop` = the §6-B proof on hardware; C-002 on four-of-four) → Erik midday → the audit → CG (afternoon or Sat) → FE (Sat) → H8 (Sun/Mon).

**STANDING:** `BEYOND:` one word · E1 (EUR-Lex outage; the hub retries) · `EU: ship|defer` 09-11 · `Activate` 09-15 · the docs correction block. **OPEN RISKS:** OR-NIGHTLY-0902-S31 (rows 17/18 pending) · OR-FAILCHAN (instance 5 fixed-pending-CI; instance 6 residual, LOW) · OR-JOURNALD-PRIO RULED (a), next on the desk (+2 riders) · OR-REHOMED-OQ · OR-M13-SDNOTIFY HOLD. **v63 SKELETON** on disk (slots fill at the close). Fences: no public brand use before the opinion (09-18) · s31/nightly HANDS OFF until R-5 · one lane on the core tree · the hub never implements.

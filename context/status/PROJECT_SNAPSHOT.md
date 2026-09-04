<!--
file: context/status/PROJECT_SNAPSHOT.md
purpose: Current operational state hub — current WU, code state, deferred gates, build status.
audience: All
update-cadence: per-WU
state-type: current
status: CURRENT
last-verified: 2026-09-04 (v62 beat 6 — FAILCHAN landed 7af2d6c, CI #225 RED, Fri ~10:51 CT (15:51Z) — the verdict banked; the instrument read ("the dispatched On frame"; local green; prior reds in history); guard 1 answered — R-4b on ef02d13's artifact; the navigator prompt + record scaffold; the deferred gate OPEN. Order: hivemind 6 = 4 M + 2 A. Detail: pm-handoff v62 beat 6.) 
Prior: 2026-09-04 (v62 beat 5 — THE R-4b NAVIGATOR PACKET, Fri ~07:36 CT (12:36Z) — guard 1 as §0; the window timed to the plug's :54s cadence; three provocations; the §6-F announce-class fallback; C4 by path A/B; the FAILCHAN stop-proof at §5 iff it rides. Order: hivemind 4 = 3 M + 1 A. Detail: pm-handoff v62 beat 5.) Prior: THE FULL PRIOR CHAIN verbatim at context/handoff/archive/chains-pre-region-cap-2026-08-23.md + archive/chains-rotated-2026-08-27.md; rolled-off segments: the pm-handoff `:8` chain + its archives.
-->
# Project Snapshot

> **How to read this file:** the frontmatter `last-verified:` chain above (2 pointer segments + the rotation pointer) is the session record; the body below is an OVERWRITTEN DIGEST (W-HIVE-1 P9, ≤2 KB) — rewritten every beat, never appended. The chain and the newest pm-handoff beat block outrank everything else. **The operator's copy-source of record is the file on disk, never a chat card.** Full history: `context/handoff/archive/chains-pre-region-cap-2026-08-23.md` + `archive/PROJECT_SNAPSHOT-priors-rotated-2026-08-21.md`.

## The digest (v62 beat 6 — CI #225 RED banked; R-4b dispatching, Fri 2026-09-04 ~10:51 CT)

**v62 LIVE; TODAY IS R-4b (on `ef02d13`'s artifact).** HEADs: core **`7af2d6c` (FAILCHAN LANDED) — CI #225 RED: `HeroLoopHardwareFreeIT` "timed out awaiting the dispatched On frame"; the deferred gate OPEN — no other core lane before FAILCHAN-FIX-1** · hivemind = this beat (ahead 3; origin at `f0ee4ee`) · skills `f9c0bf4` · bench `4539f13` · docs `a53f474`. Strategy **v1.2 RATIFIED** · the docket **RULED** · TIER-2 GO.

**NOW:** the brief §A2 (the token census from the CI test report → the fix WU authors on it) · §A3 dispatch the R-4b NAVIGATOR (`context/handoff/2026-09-04_R-4b_navigator_session-prompt.md`; the record `context/audits/2026-09-04_R-4b_re-rep_operator-record.md`; the packet `context/handoff/2026-09-04_R-4b_navigator-packet_held-card.md`) · Erik midday. **THEN:** FAILCHAN-FIX-1 (a core lane; its CI reopens the tree) → the R-4b record intake → C-002 or the fallback's record → CG (after the gate clears) → FE Sat → H8 Sun/Mon.

**STANDING:** `BEYOND:` · E1 (outage; the hub retries) · `EU` 09-11 · `Activate` 09-15 · the docs block. **OPEN RISKS:** OR-FAILCHAN (landed; CI RED; gate OPEN; instance 6 residual) · OR-NIGHTLY-0902-S31 (rows 17/18 pending) · OR-JOURNALD-PRIO RULED (a) · OR-REHOMED-OQ · OR-M13-SDNOTIFY HOLD. **v63 SKELETON** on disk. Fences: no public brand use before the opinion (09-18) · s31/nightly HANDS OFF until R-5 · one lane on the core tree · the hub never implements.

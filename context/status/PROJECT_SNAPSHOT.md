<!--
file: context/status/PROJECT_SNAPSHOT.md
purpose: Current operational state hub — current WU, code state, deferred gates, build status.
audience: All
update-cadence: per-WU
state-type: current
status: CURRENT
last-verified: 2026-10-09 (v101 post-close beat 6 — THE SECOND CLOSE with THE ROTATION (12 → 7 → 8; the chain 267); AMD-102 RATIFIED twice; CONFIG-ERROR-1 cut, reviewed to v2 (D-v101-29..34); Fri 2026-10-09 ~15:0x CT (2026-10-09T20:09:41Z). Order: the b6 card → the line → BC9a → v102 Sat 07:00.) Prior: 2026-10-09 (v101 post-close beat 5 — THE PLAN-AHEAD PASS: the four words (D-v101-24); the review ruled (D-v101-25); THE FREEZE LIST (D-v101-26); the triage 19/59/11+5 (D-v101-27); ROTATE-AT-CLOSE; the landings (D-v101-28); Fri 2026-10-09 ~13:5x CT (2026-10-09T18:53:19Z). Order: the b5 card → `ZIGBEE-YAML:` → b6 → the lane → the second close. Detail: pm-handoff v101 b5.) Prior: THE FULL PRIOR CHAIN verbatim at context/handoff/archive/chains-pre-region-cap-2026-08-23.md + archive/chains-rotated-2026-08-27.md; rolled-off segments: the pm-handoff `:8` chain + its archives.
-->
# Project Snapshot

> **How to read this file:** the frontmatter `last-verified:` chain above (2 pointer segments + the rotation pointer) is the session record; the body below is an OVERWRITTEN DIGEST (W-HIVE-1 P9, ≤2 KB) — rewritten every beat, never appended. The chain and the newest pm-handoff beat block outrank everything else. **The operator's copy-source of record is the file on disk, never a chat card.** Full history: `context/handoff/archive/chains-pre-region-cap-2026-08-23.md` + `archive/PROJECT_SNAPSHOT-priors-rotated-2026-08-21.md`.

## The digest (v101 b6 — CONFIG-ERROR-1 cut under AMD-102; tonight BC9a + SOAK-NIGHT-2; v102 Sat 07:00)

**State:** core **`37f05a9`** (AVAIL-SHAPE; **19/20**); bench **`cddac94`**; docs `055832c`; skills `e9a77a8`; hivemind the b6 card's sha (8 live beats; v3 merged, not yet the digests' source — IR-140). **THE PI RUNS `df2bc62` BY SHA** until BC9a tonight. **THE FLEET: 10 in the registry, 9 ON THE AIR.** **AMD-102 RATIFIED** (an ERROR or an unknown key fails the boot naming the path; three dead Zigbee keys removed; the migration EMPTY; P4's reversal owned; IR-141 DEPRECATE-1 post-run — no key leaves a fragment after the run until it lands). **CONFIG-ERROR-1** (IR-90 · 122 · 126 · 132): cut at `37f05a9`, reviewed to v2; the line after the b6 card. **AVAIL-API-1** re-cut: an event-v3 unit after the FE note. **THE FREEZE LIST (D-v101-26 amended):** STARTER-1 config · CONFIG-ERROR-1 · PROBE-ANSWERED-1 on P3′ · J3 · GRADER-S31-1 · AVAIL-API-1 if the FE note lands Sunday. **TONIGHT:** BC9a ≈ 19:30 (STATE: `AVAIL-LINE-1: LANDED cddac94`) → SOAK-NIGHT-2 → Sat 07:00 `S2` → v102. **NEXT:** the b6 card → the dispatch line.

**Open risks:** ten — OR-HUE-REPORTING-DEAD · OR-S31-INTERMITTENT · OR-NIGHTLY-0902-S31 · FAILCHAN · BUS-SILENT-DROP · ADOPT-AWAKE · METERING-VOLUME · three standing — + IR-29..141 + one fence. Standing: D4 · no batched pushes · the rig exclusive · FENCE-BUS · the S31 hands-off · no B-2/B-3 CODE before 20 · no public name before its protocol row · the hub never commits or pushes · no PR merged by the button · every card gated · the restore before any gap · no ungrepped premise · `--no-optional-locks` · every edited row by its id · the store read where the store has the event · the amendment quotes the principle.

<!--
file: context/status/PROJECT_SNAPSHOT.md
purpose: Current operational state hub — current WU, code state, deferred gates, build status.
audience: All
update-cadence: per-WU
state-type: current
status: CURRENT
last-verified: 2026-10-09 (v101 post-close beat 7 — CONFIG-ERROR-1 INTAKEN ACCEPT (tree `fca2020…` over `37f05a9`; D-v101-35/36); IR-142; the landing cards (D-v101-37); Fri 2026-10-09 ~16:1x CT (2026-10-09T21:18:15Z). Order: the b7 card → the commit card → CI → the ff-merge → BC9a → v102.) Prior: 2026-10-09 (v101 post-close beat 6 — THE SECOND CLOSE with THE ROTATION (12 → 7 → 8; the chain 267); AMD-102 RATIFIED twice; CONFIG-ERROR-1 cut, reviewed to v2 (D-v101-29..34); Fri 2026-10-09 ~15:0x CT (2026-10-09T20:09:41Z). Order: the b6 card → the line → BC9a → v102 Sat 07:00.) Prior: THE FULL PRIOR CHAIN verbatim at context/handoff/archive/chains-pre-region-cap-2026-08-23.md + archive/chains-rotated-2026-08-27.md; rolled-off segments: the pm-handoff `:8` chain + its archives.
-->
# Project Snapshot

> **How to read this file:** the frontmatter `last-verified:` chain above (2 pointer segments + the rotation pointer) is the session record; the body below is an OVERWRITTEN DIGEST (W-HIVE-1 P9, ≤2 KB) — rewritten every beat, never appended. The chain and the newest pm-handoff beat block outrank everything else. **The operator's copy-source of record is the file on disk, never a chat card.** Full history: `context/handoff/archive/chains-pre-region-cap-2026-08-23.md` + `archive/PROJECT_SNAPSHOT-priors-rotated-2026-08-21.md`.

## The digest (v101 b7 — CONFIG-ERROR-1 intaken ACCEPT, landing on Nick's cards; tonight BC9a + SOAK-NIGHT-2; v102 Sat 07:00)

**State:** core **`37f05a9`** on `main` (AVAIL-SHAPE; **19/20**) — **CONFIG-ERROR-1 staged as tree `fca2020…` on `config-error-1/ir-90-122-126-132`, INTAKEN ACCEPT, landing by two cards** (`CONFIG-ERROR-1: COMMITTED` → `CI: green` → `CORE: LANDED` — then IR-90 · 122 · 126 · 132 CLOSE); bench **`cddac94`**; docs `055832c`; skills `e9a77a8`; hivemind the b7 card's sha (9 live beats). **THE PI RUNS `df2bc62` BY SHA** until BC9a tonight (which pins `37f05a9`, never the landed sha). **THE FLEET: 10 in the registry, 9 ON THE AIR.** **AMD-102 RATIFIED** (an ERROR or an unknown key fails the boot naming the path; three dead keys removed; the migration EMPTY; IR-141 DEPRECATE-1 post-run). **AVAIL-API-1** after the FE note. **THE FREEZE LIST:** STARTER-1 config · CONFIG-ERROR-1 (landing) · PROBE-ANSWERED-1 on P3′ · J3 · GRADER-S31-1 · IR-142 before dry-run #2 · AVAIL-API-1 if the FE note lands Sunday. **TONIGHT:** BC9a ≈ 19:30 (STATE: `AVAIL-LINE-1: LANDED cddac94`) → SOAK-NIGHT-2 → Sat 07:00 `S2` → v102. **NEXT:** the b7 card → the commit card → CI → the ff-merge.

**Open risks:** ten — OR-HUE-REPORTING-DEAD · OR-S31-INTERMITTENT · OR-NIGHTLY-0902-S31 · FAILCHAN · BUS-SILENT-DROP · ADOPT-AWAKE · METERING-VOLUME · three standing — + IR-29..142 + one fence. Standing: D4 · no batched pushes · the rig exclusive · FENCE-BUS · the S31 hands-off · no B-2/B-3 CODE before 20 · no public name before its protocol row · the hub never commits or pushes · no PR merged by the button · every card gated · the restore before any gap · no ungrepped premise · `--no-optional-locks` · every edited row by its id · the store read where the store has the event · the amendment quotes the principle.

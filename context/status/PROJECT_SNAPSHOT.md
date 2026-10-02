<!--
file: context/status/PROJECT_SNAPSHOT.md
purpose: Current operational state hub — current WU, code state, deferred gates, build status.
audience: All
update-cadence: per-WU
state-type: current
status: CURRENT
last-verified: 2026-10-02 (v90 beat 6 — the two intakes: 1b ACCEPT-WITH-NOTES (the sensor adopted; the fleet 10; IR-93 CLOSED; IR-112..115) · DOCS-1 ACCEPT-WITH-NOTES (f7e8e72); v92's text; D-v90-17..20; Fri 2026-10-02 ~07:2x CT (2026-10-02T12:23:26Z). Order: the b6 card → the docs landing → v92. Detail: pm-handoff v90 b6.) Prior: 2026-10-01 (v90 beat 5, after the close — HIVE: LANDED 124cf4c; DOCS1: LAUNCHED 18:12 · CREDITS: $145; the start line by 19:45; D-v90-14..16; Thu 2026-10-01 ~18:2x CT (2026-10-01T23:20:16Z). Order: the packet NOW → the sitting → the b5 card → v92. Detail: pm-handoff v90 b5.) Prior: THE FULL PRIOR CHAIN verbatim at context/handoff/archive/chains-pre-region-cap-2026-08-23.md + archive/chains-rotated-2026-08-27.md; rolled-off segments: the pm-handoff `:8` chain + its archives.
-->
# Project Snapshot

> **How to read this file:** the frontmatter `last-verified:` chain above (2 pointer segments + the rotation pointer) is the session record; the body below is an OVERWRITTEN DIGEST (W-HIVE-1 P9, ≤2 KB) — rewritten every beat, never appended. The chain and the newest pm-handoff beat block outrank everything else. **The operator's copy-source of record is the file on disk, never a chat card.** Full history: `context/handoff/archive/chains-pre-region-cap-2026-08-23.md` + `archive/PROJECT_SNAPSHOT-priors-rotated-2026-08-21.md`.

## The digest (v90 b6 — the fleet is 10; BC7 TONIGHT is v92's deliverable)

**State:** core **`5b0e20c`** (IR-67 LANDED, `CI: green`, Phase 2 CLOSED; **19/20**); bench **`ede32c9`** (BH-3; BENCH-PULL-5 never said — read at BC7); docs `7221ddc` + **DOCS-1 `f7e8e72`** (INTAKEN; the landing card → `DOCS1: LANDED`); skills **`e9a77a8`**; hivemind **`124cf4c`** + the b6 card. **The bench card on `40412f9` PINNED — BC7 TONIGHT lifts it** (the re-mint to 10 FIRST; the core to `main`; IR-102 a; IR-67's attestation; the Hue's re-drive). **The fleet 10/10** (1b DONE + INTAKEN; IR-93 CLOSED; IR-112..115); the key ABSENT. **THE HUE joined and silent** (IR-112; OR-HUE-REPORTING-DEAD). Fri's nightly ran on the edited configs at 9 (`NIGHTLY:` Nick's); Sat's reads 10. **THE FORTNIGHT (§10):** `CAP: three` · the rig ≤ 4 h by 21:30 CT · `RUN: oct30-two-dry` · `JAVA-ROUTE: split` · `CREDITS: $145` (before DOCS-1's run). **LANES:** the Java slot FREE (v91: LINK-READ-2's pre-verification) · the docs lane DONE. **NOW:** the b6 card → the docs landing → v92's paste → BC7 by 17:30 → v93 Sat (rehearsal 2 on IR-112/114). The v90 DR CLOSED (D-v90-1..20).

**Open risks:** twelve (OR-HUE-REPORTING-DEAD (new) · OR-BENCH-FENCE-PJ2 (closes at BC7) · OR-S31-INTERMITTENT · OR-HORIZON-UNPLANNED · OR-NIGHTLY-0902-S31 · FAILCHAN · BUS-SILENT-DROP · ADOPT-AWAKE · METERING-VOLUME · three standing) + IR-29..115 + one fence. Standing: D4 · no batched pushes · the rig exclusive · FENCE-BUS · the S31 hands-off · no B-2/B-3 CODE before 20 · no public name before its protocol row · the hub never commits or pushes · a cloud lane's exit and grant first · no PR merged by the button · every card gated · the restore before any gap · no `capability.removed` · no ungrepped premise · `--no-optional-locks` everywhere.

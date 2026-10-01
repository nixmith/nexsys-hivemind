<!--
file: context/status/PROJECT_SNAPSHOT.md
purpose: Current operational state hub — current WU, code state, deferred gates, build status.
audience: All
update-cadence: per-WU
state-type: current
status: CURRENT
last-verified: 2026-10-01 (v89 beat 3, THE CLOSE — IR-67 RETURNED + INTAKEN ACCEPT-WITH-NOTES (PR #8; IR-110/111); the landing card cut (20); v90's text (the 1b packet); the deliverable MET (D-v89-12..14); Thu 2026-10-01 ~06:4x CT (2026-10-01T11:47:47Z). Order: CORE: LANDED (IR-67) → HIVE: LANDED (b3) → CI: → v90's paste. Detail: pm-handoff v89 b3.) Prior: 2026-09-30 (v89 beat 2 — IR-67 CUT + REVIEWED (RE-CUT, E1–E12 applied) + its cloud first message HANDED (D-v89-7..11); the lesson minted; IR-108/109; Wed 2026-09-30 ~20:2x CT (2026-10-01T01:28:00Z). Order: HIVE: LANDED (b2) → the paste → IR67: LAUNCHED → the close. Detail: pm-handoff v89 b2.) Prior: THE FULL PRIOR CHAIN verbatim at context/handoff/archive/chains-pre-region-cap-2026-08-23.md + archive/chains-rotated-2026-08-27.md; rolled-off segments: the pm-handoff `:8` chain + its archives.
-->
# Project Snapshot

> **How to read this file:** the frontmatter `last-verified:` chain above (2 pointer segments + the rotation pointer) is the session record; the body below is an OVERWRITTEN DIGEST (W-HIVE-1 P9, ≤2 KB) — rewritten every beat, never appended. The chain and the newest pm-handoff beat block outrank everything else. **The operator's copy-source of record is the file on disk, never a chat card.** Full history: `context/handoff/archive/chains-pre-region-cap-2026-08-23.md` + `archive/PROJECT_SNAPSHOT-priors-rotated-2026-08-21.md`.

## The digest (v89 CLOSED at b3 — IR-67 back and landing; v90 = Thursday: the 1b packet)

**State:** core **`8deef4b`** + IR-67's landing → `<sha>` (Nick's gated squash of `a8918f4` + `8ee1883`, 20; PR #8 closed as landed; `CI:` the gate; **18/20** +1 at green); bench **`ede32c9`** (BH-3 LANDED; BENCH-PULL-5 Nick's line); docs `7221ddc`; skills **`e9a77a8`** (SYNCED); hivemind **`a4b6272`** + the b3 card (gated, 12). **The bench card on `40412f9` PINNED** until BC7 (Fri: PJ-2 + IR-67 on the card; IR-102 a; the reconcile line read); `NIGHTLY:` Wed/Thu and `BASELINE:` OPEN. **The fleet 9/9**; the key ABSENT; the S31 in. **THE FORTNIGHT (§10):** `CAP: three` · the rig ≤ 4 h by 21:30 CT · three windows a day · `RUN: oct30-two-dry` · `JAVA-ROUTE: split`. **LANES:** IR-67 INTAKEN (v89 b3; IR-110/111; Phase 2 at `CI: green`) → LINK-READ-2 next on the desk · v90 (Thu): the 1b packet, DOCS-1's card · `RESEARCH-LH: now`. **NOW:** the core landing card → `CORE: LANDED` → the b3 card → `CI:` → v90's paste. 1b TONIGHT (≤ 4 h, done by 21:30 CT); BC7 Fri. The v89 DR CLOSED (D-v89-1..14).

**Open risks:** eleven (OR-BENCH-FENCE-PJ2 · OR-S31-INTERMITTENT (→ IR-88) · OR-HORIZON-UNPLANNED · OR-NIGHTLY-0902-S31 · FAILCHAN inst. 2 · BUS-SILENT-DROP · ADOPT-AWAKE · METERING-VOLUME · three standing) + IR-29..111 (IR-89 CLOSED) + one fence (no device outside a card). Standing: D4 · no batched pushes · the rig exclusive · FENCE-BUS · the S31 hands-off · no B-2/B-3 CODE before 20 · no public name before its protocol row · the hub never commits or pushes · a cloud lane carries its exit, its grant first · no PR merged by the button · every card gated · the Pi's clone pinned until BC7 · no re-pin without `REPIN:` · no `capability.removed` · no ungrepped premise · `--no-optional-locks` everywhere.

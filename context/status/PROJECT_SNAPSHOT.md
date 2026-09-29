<!--
file: context/status/PROJECT_SNAPSHOT.md
purpose: Current operational state hub — current WU, code state, deferred gates, build status.
audience: All
update-cadence: per-WU
state-type: current
status: CURRENT
last-verified: 2026-09-28 (v86 beat 4, THE CLOSE at four — the deliverable met; BC6 STOP → Tue 16:00; the PJ-2 landing card handed; v87's text; 4 blocks rotated; the DR CLOSED (D-v86-1..18); Mon 2026-09-28 ~20:3x CT (2026-09-29T01:30Z). Order: the landing → the v86 card → Tue: v87 + BC6. Detail: pm-handoff v86 beat 4.) Prior: 2026-09-28 (v86 beat 3, PJ-2 pushed + intaken ACCEPT-WITH-NOTES; the landing card; IR-98..100; the DR (D-v86-1..15); Mon 2026-09-28 ~20:0x CT (2026-09-29T01:07Z). Order: BC6 → the landing → CORPUS-1. Detail: pm-handoff v86 beat 3.) Prior: THE FULL PRIOR CHAIN verbatim at context/handoff/archive/chains-pre-region-cap-2026-08-23.md + archive/chains-rotated-2026-08-27.md; rolled-off segments: the pm-handoff `:8` chain + its archives.
-->
# Project Snapshot

> **How to read this file:** the frontmatter `last-verified:` chain above (2 pointer segments + the rotation pointer) is the session record; the body below is an OVERWRITTEN DIGEST (W-HIVE-1 P9, ≤2 KB) — rewritten every beat, never appended. The chain and the newest pm-handoff beat block outrank everything else. **The operator's copy-source of record is the file on disk, never a chat card.** Full history: `context/handoff/archive/chains-pre-region-cap-2026-08-23.md` + `archive/PROJECT_SNAPSHOT-priors-rotated-2026-08-21.md`.

## The digest (v86 CLOSED at b4 — THE DELIVERABLE MET; the landing card in Nick's hands; Tuesday: v87 at 16:00 + BC6)

**State:** core **`40412f9`** (`main`; CI green; **16/20**, 17 on `a5b9e33` OPEN) + PJ-2's landing card in Nick's hands (a squash → `CORE: LANDED` → `CI:` the 18th); bench **`352296d`** (on the Pi); docs `7221ddc`; skills `180375f`; hivemind `b4025b6` + the v86 card. **The bench card on `1f1d1e0`** — BC6 STOPPED Mon 20:18 CT (the 20:15 rule) → TUESDAY 16:00 FIRST; Tuesday's nightly's pair (`1f1d1e0`, `352296d`). **The fleet 9/9**; the key ABSENT; the S31 in. **EXPORT-1 DONE + INTAKEN:** VERIFY-72H PASS (6,953 rows; opaque 0); IR-95 (§3.9 SKIP by design), IR-96 (→ VERIFY-72H-B), IR-97. **PJ-2 DELIVERED** (cloud; PR #7), INTAKEN ACCEPT-WITH-NOTES (IR-98..100); THE BENCH FENCE until BH-3. **TUE (v87 16:00):** BC6 first; the intakes owed; Phase 2; the 1b re-cut (rec `onUnavailable: WARN`); THE STRATEGY PASS (BH-3, IR-67 cloud, VERIFY-72H-B, the docs card, the credits); CORPUS-1 + KREFRESH-1. **Wed** W-SKILLS-10. **Thu** 1b. **Words:** `CORE: LANDED` · `CI:` · `HIVE: LANDED` · `NIGHTLY:` · `BENCH-CORE-6:` · `TM:`. The name CLEAR; NOT FILED until `TM:`. §30; the v86 DR CLOSED (D-v86-1..18).

**Open risks:** ten (OR-S31-INTERMITTENT (→ IR-88) · OR-HORIZON-UNPLANNED · OR-NIGHTLY-0902-S31 · FAILCHAN inst. 2 · BUS-SILENT-DROP · ADOPT-AWAKE · METERING-VOLUME · three standing) + IR-29..100 (IR-89 CLOSED; IR-94 adjudicated) + one fence (no device outside a card) + the BH-3 fence. Standing: D4 · no batched pushes · the rig exclusive · FENCE-BUS · the S31 hands-off · no B-2/B-3 CODE before 20 · no public name before its protocol row · the hub never commits or pushes · a cloud lane never touches `main` and carries its exit · no PR merged by the button · no re-pin without `REPIN:` · no ungrepped premise · every git call `--no-optional-locks`.

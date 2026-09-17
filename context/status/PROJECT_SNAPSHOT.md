<!--
file: context/status/PROJECT_SNAPSHOT.md
purpose: Current operational state hub — current WU, code state, deferred gates, build status.
audience: All
update-cadence: per-WU
state-type: current
status: CURRENT
last-verified: 2026-09-16 (v75 beat 6, TWO INTAKES ACCEPT — DUR-1 + HASH-1 on the landing card; `DEVICES: core` rec; IR-24/IR-25; Activate re-cut; ZIGBEE-GAPS and FOP-1 chartered; Wed 2026-09-16 ~20:1x CT (2026-09-17T01:10Z). Order: hivemind 16 = 11 M + 5 A by explicit paths (computed from porcelain inside the splice); core 14 = 12 M + 2 A by the card. Detail: pm-handoff v75 beat 6.) Prior: 2026-09-15 (v75 beat 5, MEASURE-1 ACCEPT — both defects measured; DUR-1 + HASH-1 and DEVICE-SET DISPATCH-READY; the Activate email; the spine rotated; Tue 2026-09-15 ~18:0x CT (2026-09-15T23:09Z). Order: hivemind 14 = 9 M + 5 A by explicit paths (computed from porcelain inside the splice). Detail: pm-handoff v75 beat 5.) Prior: THE FULL PRIOR CHAIN verbatim at context/handoff/archive/chains-pre-region-cap-2026-08-23.md + archive/chains-rotated-2026-08-27.md; rolled-off segments: the pm-handoff `:8` chain + its archives.
-->
# Project Snapshot

> **How to read this file:** the frontmatter `last-verified:` chain above (2 pointer segments + the rotation pointer) is the session record; the body below is an OVERWRITTEN DIGEST (W-HIVE-1 P9, ≤2 KB) — rewritten every beat, never appended. The chain and the newest pm-handoff beat block outrank everything else. **The operator's copy-source of record is the file on disk, never a chat card.** Full history: `context/handoff/archive/chains-pre-region-cap-2026-08-23.md` + `archive/PROJECT_SNAPSHOT-priors-rotated-2026-08-21.md`.

## The digest (v75 at beat 6 — both intakes ACCEPT; the DUR-1 + HASH-1 landing on the card; Activate re-cut; Wed 09-16 ~20:xx CT)

**State:** core `3d40b5f` + DUR-1 + HASH-1 on the card (14 = 12 M + 2 A; CI = the gate; sample 7); the stamp **v1.1.5**; hivemind `13e8d64` + b6 (the card); docs `7221ddc`; bench `f3631cb`; skills `180375f`. **The plan of record:** `context/planning/2026-09-15_v75_PROGRAM-PLAN_the-six-weeks-to-the-72-hour-run.md` (§10 b5; §11 b6) — the run Oct 30 – Nov 2; R-5B → rehearsal 1 → ENERGY-READ → LINK-READ → rehearsal 2 → the soak → the run. **This window:** b1–b6 DONE · b7 `CI:` → IR-22/23 retired, the HASH NOTE a fact; ENERGY-READ chartered (IR-15, IR-24, IR-25); FE-115; the knockout · b8 Saturday's intake; the close. **Words:** `CORE: DUR1` · `CI:` · `HIVE:` · `DEVICES: core|extended` (rec core) · `ACTIVATE: sent` · `GAPS:` · `FOP1:` · `NAME:` silence = ii · `STRATEGY:` · `CASCADE:` · `AMD100: ratify`. **Owed:** `PROTECT: done` · `ERIK:`

**Open risks:** seven (FAILCHAN rides H8-a · BUS-SILENT-DROP 6/20 · ADOPT-AWAKE · four standing) + IR-22/IR-23 (measured; the fix on the card — retire at CI green) + IR-24/IR-25 (the plug classified as a switch; raw thresholds — ENERGY-READ's rows) + two fences (no IAS water/smoke/vibration before IR-15; no metering plug before ENERGY-READ). Standing: D4 · no batched pushes · the rig exclusive · FENCE-BUS · s31/nightly hands off until R-5B's B6 · no B-2/B-3 CODE before the counter closes · no public name before the opinion · the hub never commits or pushes · no re-pin before Saturday without `REPIN:` · no ungrepped premise goes DISPATCH-READY · no outward sentence the register does not hold.

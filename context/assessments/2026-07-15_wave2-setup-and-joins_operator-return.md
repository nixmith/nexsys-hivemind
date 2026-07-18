<!--
file: context/assessments/2026-07-15_wave2-setup-and-joins_operator-return.md
purpose: Operator-assist lane return for Wave-2 physical device setup, characterization prep, and (HUB-GATED) the joins session. Everything the bench produces lands here as it happens — Phase-0 identity/IEEE captures, per-device characterization worksheets, join transcripts (verbatim token lines), latencies, surprises, and the [CONFIRM-ON-BENCH] open/resolved ledger. The hub two-layer audits this return, folds corpus entries + profile confirmations, and orders any commits.
audience: the v31 hub (audit → corpus/profile fold → commit); Nick (hands at the bench); the Wave-2 profiles/scenarios WUs (this return's downstream consumers).
state-type: assessment (dispatched operator-lane return — WRITE-ISOLATED per the 2026-07-15 lane brief; this session writes ONLY this file — no spine, no code, no config, no commits).
status: PHASE 0 COMPLETE (device setup captured 2026-07-15, device-by-device with Nick — all four exact-model keys confirmed off the housings; 8 [CONFIRM-ON-BENCH] items resolved at the bench, incl. the 04P's previously-unverified battery = CR2477). Phase 1 (joins) ⛔ HUB-GATED — NOT started; prerequisites unmet as of PROJECT_SNAPSHOT v31 beat 2 (profiles WU not yet landed/deployed; SEED formation ruling not yet executed). Awaiting the hub's explicit go, relayed by Nick.
brief: context/handoff/2026-07-15_wave2-device-setup_operator-lane_session_prompt.md
ground-truth reads (this return is re-derivable from): context/assessments/2026-07-11_wave2-device-dossiers_research-return.md §§0–6 (the audited per-device source) · project-knowledge/device-corpus/ (README schema + the two Wave-1 entries + the MG24 coordinator — the corpus standard these observations feed) · nexsys-bench/docs/2026-07-06_m9.4-bench-acceptance-runbook.md Phases 3–5 (the join/verify idiom) · nexsys-bench/docs/2026-07-06_m9.4-bench-acceptance-record.md (2026-07-13/14 close-out; the SNZB-03P silicon fingerprint precedent) · context/status/PROJECT_SNAPSHOT.md v31 beat 2 (live state) · context/process/bench-troubleshooting-playbook.md §8 (the operator-handoff contract this return obeys).
sources-discipline: EVERY Wave-2 hardware expectation below is SECONDARY (community-documented; silicon adjudicates on the bench). Tags follow the corpus convention — [REF] = documented from a cited public source · [CONFIRM-ON-BENCH] = only the physical unit can establish it. A captured value NEVER overwrites an expectation silently; it lands in the device's "Phase 0 capture" block and the delta (if any) is called out. Never-false-CONFIRMED applies to this return: where the sticker/interview disagrees with the expectation, the disagreement is RECORDED, not reconciled away.
-->

# Operator Return — Wave-2 Device Setup & Joins (operator-assist lane)

## 0. What this file is, and how to read it

This is the single write-isolated return for the Wave-2 bench work. It carries two phases:

- **Phase 0 — device setup** (runnable now, no hub gate): unbox hygiene, per-device identity + IEEE capture off the housings, battery-tab pulls that do NOT initiate pairing, one seeded characterization worksheet per device, and the physical bench layout. **This is what we are doing now, device-by-device.**
- **Phase 1 — the joins session** (⛔ hub-gated): formation → permit-join → per-device join + verify (announce → proposed COMPLETE → adopted → reporting_configured) → the D1/B2 evidence reads. **Not started; see §1 for why, §4 for the stub.**

The worksheets in §3 are seeded from the audited dossiers so the bench step is a fast **confirm/correct**, not a from-scratch fill — the same idiom the Wave-1 bench-up report used. Each worksheet states what we EXPECT (with `[REF]`/`[CONFIRM-ON-BENCH]` tags), leaves a "Phase 0 capture" block to fill now, and carries the full interview/reporting/confirmation expectations forward for the join session. The `[CONFIRM-ON-BENCH]` items collect into the §5 ledger.

---

## 1. Live-state gate — verified 2026-07-15 (why Phase 0 is go and Phase 1 is not)

Re-derived from `PROJECT_SNAPSHOT.md` (newest beat: **v31 hub, beat 2, 2026-07-14/15**) and the acceptance record close-out:

- **Certification is CLOSED** (soak 3d 12h unbroken on `04f5f70`; exit spike ×3 green; ~1,728 cumulative recorded verdicts, zero false CONFIRM). **Deploy `1aa809d` CLEARED.**
- **All four Wave-2 devices are IN HAND** (v31 beat 2, R-ii). Shelly ×2 + Rosonway hub **ORDERED** (<48 h → ~Jul 16). **ZBDongle-P: STOWED, NEVER POWERED** in this lane.
- **Phase 1 prerequisites — BOTH UNMET as of this beat:**
  1. The **Wave-2 profiles WU** (zigbee-profiles.json entries for the four devices) is on the hub's *Next* list — **not yet landed on core / CI-green / deployed to the Pi**.
  2. The **SEED formation ruling** (SD-5 discharge → the one-formation economy: fresh formation → Wave-1 rejoin → the four joins) is **not yet executed** — the SEED silicon leg is still pending.

**Consequence (the gate):** this lane runs **Phase 0 only**. It does NOT form a network, open permit-join, join any device, or power the ZBDongle-P. Phase 1 starts ONLY on the hub's explicit go, relayed by Nick, WITH the hub's supplied paste-blocks. This is recorded so the gate is re-checkable, not remembered.

---

## 2. The fleet + ruled placements (2026-07-14)

| Device | Role in the wave | Ruled placement | Phase-0 physical notes |
|---|---|---|---|
| **SONOFF S31 Lite zb** | Smart plug (on/off, **NO** energy). The wave's ONLY mains **router**. The wave's ONE **confirmable** device (first DIRECT `on_off` confirm leg). | **Inline with the Hue lamp.** Post-join, a commanded plug-off is a legitimate bulb power-cut lever (measured device ≠ lever). | Mains — **no battery tab**. Identity gotcha: manufacturer string is **`SONOFF`**, not eWeLink. Record mesh effects at join (only mains router). |
| **SONOFF SNZB-02P** | Temp/humidity sensor. Sleepy periodic reporter. The availability-**ALIVE anchor**. | **Desk join.** | Battery (expect 1× CR2477). The 25 h battery-posture availability case is later. |
| **SONOFF SNZB-04P** | Door/window contact. IAS + a bound-OnOff dual-path watch. | **Characterize at the DESK first** (magnet reps near the coordinator), mount at the front door ONLY after its worksheet is complete. **Reed gap governs mounting (≤ ~10 mm closed; aesthetics second).** | Battery TYPE **unverified** — do NOT assume CR2032; record what's actually in it. Magnet half at hand. |
| **SONOFF SNZB-01P** | Wireless button. Adopts **battery-only** per ruled **R2(B)** (presses log-visible, absent from the device model — deliberate scoping; BTN-AMD is post-gate). | **Desk instrument** — the physical **log-marker**: a press stamps the log at operator-act time. | Battery (expect 1× CR2477). Predecessor trap: it must report `SNZB-01P`, not `WB01`. |
| **SONOFF ZBDongle-P** | (Not under test this lane.) Adversarial tool for B2; an eliminated suspect while unpowered. | **STOWED.** | **NEVER POWERED in this lane.** Do not plug it in. |

Out-of-band stimulus of record = the **Shelly Plus Plug US Gen2** (arriving ~Jul 16) — it rides the bench LAN/WiFi, never the Zigbee network under test. Not a Phase-0 item.

---

## 3. Phase 0 — device setup (RUNNABLE NOW)

### 3.0 Goal + done-when

**Goal:** every Wave-2 device has its true identity captured off the housing and folded into its worksheet, is powered-and-staged (sensors) or staged (S31) within ~1 m of the coordinator, with zero pairing initiated — so the joins session (when the hub opens it) is a clean, model-verified run instead of a debug-everything-at-once scramble.

**Done-when (all four):**
1. Model string + firmware/dateCode (if printed) + **IEEE address** recorded verbatim per device.
2. Battery type recorded per sensor; battery tab **pulled** on the three sensors **without** pairing (S31 stays unpowered — mains).
3. Each worksheet's "Phase 0 capture" block filled; each identity `[CONFIRM-ON-BENCH]` item either **resolved-from-sticker** or explicitly **still-open** (into §5).
4. Bench staged: all four within ~1 m of the coordinator; the 04P's magnet half at hand.

### 3.1 Shared procedure + the anti-actions (read once, applies to every device)

**The capture pattern (per device):** read the housing/box sticker → record the EXACT model string (spaces and casing matter), the manufacturer string, firmware/dateCode/SWBuild if printed, and the **IEEE** (16 hex digits, often `0x00...` or colon-separated, labeled IEEE / MAC / EUI-64) → then (sensors only) pull the battery tab and note the LED/behavior. Paste what you see **either way** — a sticker that disagrees with our expectation is the most valuable thing we can find today.

**Anti-actions (unstated constraints don't exist — so here they are, explicit):**
- **A battery-tab pull is NOT pairing.** Pulling the tab just connects the cell. **Do NOT long-press any device** in Phase 0 — a long-press (~5 s to LED flash) starts pairing/leave. A short press only wakes. We are not pairing anything today.
- **A freshly-powered sensor will blink/search briefly, then sleep.** That is expected and is NOT a join — no Wave-2 network is formed and no permit-join window is open, so it cannot join anything. Record the blink pattern; don't chase it.
- **Do NOT power the S31 in Phase 0.** It's mains; powering it does nothing useful pre-formation and its power-on-relay behavior is a join-era characterization item. Stickers + IEEE + stage only.
- **Do NOT plug in the ZBDongle-P.** Stowed, never powered.
- **No formation, no permit-join, no config edits, no app restarts.** Phase 0 is physical-prep only.

**Battery-tab timing (your call, one line):** pulling the tabs now is per the Phase-0 plan and is safe (doesn't pair; coin cells easily tolerate the idle window before joins). REC **(a) pull now** — it's a live model-check (confirms the device powers + shows first-power LED behavior, which we record). Alternative **(b) capture identity now, pull tabs at join time** if you'd rather preserve the factory first-power moment. One word dispatches: "(a)" or "(b)". Default if unspecified: (a), noted per device.

**Bench layout (stage as we go):** clear ~1 m radius around the MG24 coordinator; the three sensors + the S31 within that radius; the 04P's magnet half within reach; the ZBDongle-P off the bench entirely.

---

### 3.2 Worksheet — SONOFF **S31 Lite zb** (smart plug · mains router · the confirmable one)

**Placement:** inline with the Hue lamp. **Physical:** mains, no battery tab; stage only (do not power in Phase 0).

**Expected identity — the MatchCriteria we're verifying (dossier §1.1) `[REF]`:**
- manufacturerName = **`SONOFF`** ← the wave's ONLY `SONOFF` on-wire string (the other three are `eWeLink`). The z2m catalog name "S31ZB" is a z2m alias, NOT the on-wire string.
- modelIdentifier = **`S31 Lite zb`** ← *with the two spaces and that exact casing*. Profile key = `("SONOFF", "S31 Lite zb")`.
- Mains **ROUTER** (node descriptor logical_type 1). First router since the Hue — record mesh/topology effects at join.
- **NO power monitoring** (the "Lite" — no energy surface). No ZHA quirk (clean standard-ZCL).

> **Model-check today:** does the sticker read `SONOFF` + `S31 Lite zb` exactly? A different manufacturer string or a missing space is a real finding (it changes the exact_model match key).

**Phase 0 capture (2026-07-15):**
- Model string (verbatim): **`S31 Lite zb`** ✓ matches expectation (spaces/casing correct) — **C-02 RESOLVED**
- Manufacturer string (verbatim): **`SONOFF`** ✓ matches expectation (the wave's one SONOFF on-wire string, confirmed) — **C-01 RESOLVED**
- Firmware / dateCode / SWBuild (if printed): none reported on housing at Phase 0 → capture at interview
- **IEEE (housing): NOT printed on the housing.** The housing carries `Zigbee: IEEE 802.15.4 2.4 GHz` (the radio STANDARD, not an address), `FCC ID: 2APN5S31ZB`, `IC: 29127-S31ZB`. No EUI-64 found; QR/hex recheck returned **none** (2026-07-15) → **deferred to Phase 1 interview** (`device_announce: device=<ieee>`). **FINDING: the "IEEE is on the housing" assumption does NOT hold for this device.**
- Battery: N/A (mains)
- Staged: clustered with the Hue + 02P on one outlet, within ~1 m of each other. **DEVIATION (recorded): Nick powered the S31 (plugged in) during Phase 0** — the brief's Phase-0 plan left it unpowered. Harmless now (no Wave-2 network formed, no permit-join open ⇒ it cannot join), and it makes its power-on relay state observable early. See the joins-session carry-in in §4.
- Notes / surprises: FCC ID `2APN5S31ZB` + IC `29127-S31ZB` both contain `S31ZB` → independent regulatory corroboration of the S31ZB family identity (a second, non-community source agreeing with `("SONOFF","S31 Lite zb")`). **S31 now powered + idle** (operator-reported) — LED-state read pending (a free hint for C-06 power-on relay behavior).

**Expected interview surface — carried to the join (dossier §1.2) `[REF]`:** EP1, **profile `0xC05E` (ZLL)** — but SmartThings hand-wrote `0x0104` for the same cluster set → **[CONFIRM-ON-BENCH] profileId conflict**, the wave's sharpest identity unknown; device type `0x0010` (ON_OFF_PLUGIN_UNIT); in: `0x0000, 0x0003, 0x0004, 0x0005, 0x0006`; out: `0x0000` (Basic client — odd but captured). No OTA, no mfr-specific clusters. *(Pre-Monday hub code-read flag: nothing in the pipeline gates on profile `0x0104` — CLOSED at v28; exact_model carries the adoption.)*

**Expected reporting posture (dossier §1.3 vs Doc 08 §3.7):** z2m onOff `min 0 / max 65000 / change 1`; Doc 08 default `OnOff 0/3600/discrete` (same on-change, tighter keepalive). No override needed. `powerOnBehavior`/StartUpOnOff support **doubtful → [CONFIRM-ON-BENCH]** (matters for Shelly-driven wall-power scenarios).

**Confirmation expectation (dossier §1.4 — the wave's ONE confirmable device):** `on_off` · EXACT_MATCH · authoritative `OnOff/0x0000` · VERIFIED_REPORTS · ON_CHANGE · **CONFIRMABLE** · timeout 5000 ms (seed = the Hue's, not measured). Closes the acceptance run's open §51 "DIRECT on_off confirm" item. Watch: duplicate reports per event (z2m #3904) → twin-absorption class if our unit double-reports. No-change commands ⇒ honest timeout on a DISCRETE capability.

**[CONFIRM-ON-BENCH] for the S31 (→ §5):** manufacturerCode; firmware/dateCode; IEEE; **profileId `0xC05E` vs `0x0104`**; power-on relay behavior (StartUpOnOff); command→report latency envelope; duplicate-report behavior; report-on-local-toggle.

---

### 3.3 Worksheet — SONOFF **SNZB-02P** (temp/humidity · sleepy · the ALIVE anchor)

**Placement:** desk join. **Physical:** battery sleepy end device; battery tab pull #1.

**Expected identity (dossier §2.1) `[REF]`:**
- manufacturerName = **`eWeLink`**, modelIdentifier = **`SNZB-02P`**. Profile key = `("eWeLink", "SNZB-02P")`.
- Branding note: the box/vendor says "SONOFF" but the **on-wire manufacturer is `eWeLink`** — that split is expected, not a defect.
- Battery **1× CR2477** `[REF]`; sleepy (RxOnWhenIdle=0); OTA supported. Device type `0x0302` (TEMPERATURE_SENSOR).

**Phase 0 capture (2026-07-15):**
- Model string (verbatim): **`SNZB-02P`** ✓ matches expectation
- Manufacturer/branding on housing/box: **`SONOFF`** (box/label branding) ✓ — on-wire `eWeLink` confirms at interview (C-09)
- Firmware / dateCode (if printed): none reported at Phase 0 → capture at interview
- **IEEE (housing): not the EUI-64.** A QR code on the side carries the string **`25471900074240`** — 14 DECIMAL digits, so it CANNOT be a EUI-64 (16 hex). Recorded as the unit's printed **serial / QR code** (traceability); the real EUI-64 comes at join (`device_announce`), where we bind it to this serial. → C-10 stays Phase-1.
- Battery type (read the actual cell): **`CR2477`** ✓ matches expectation (printed on the back cover, not inside the well) — **C-11 RESOLVED**
- Battery-tab pull: **(a) tab PULLED.** LED blinked briefly then settled — **same LED behavior as the Wave-1 SONOFF SNZB-03P motion sensor** (family-consistent; not a join — no network open). Choice (a) carries to the 04P + 01P.
- Staged: **yes — clustered immediately next to the Hue bulb + the S31** (which share one outlet). At join time, ensure the MG24 coordinator (on its USB extension) sits within ~1 m of this cluster.
- Notes / surprises: printed serial `25471900074240` = a physical-unit label to bind to the EUI-64 at join. Branding split (box SONOFF / wire eWeLink) as expected.

**Expected interview surface — carried to the join (dossier §2.2) `[REF]`:** EP1, profile `0x0104`, device type `0x0302`; in: `0x0000, 0x0001, 0x0003, 0x0020 (PollCtrl), 0x0402 (Temp), 0x0405 (Humidity), 0xFC11, 0xFC57`; out: `0x0019 (OTA)`. The cleanest Doc-02/08 MATCH candidate of the wave → expect `sensor` with `temperature_measurement` + `humidity_measurement` + `battery`.

**Expected reporting posture (dossier §2.3 vs Doc 08 §3.7 — the wave's one real delta):** z2m temp `10/3600/change 100` (= **1.0 °C**); Doc 08 default temp `10/3600/10` (= **0.1 °C**) → **ours is 10× more sensitive** (hub call at profile time; flag, not a defect). Humidity `10/3600/100` (1 %). Battery `3600/65000/10` (z2m) vs `3600/62000/0` (Doc 08). SONOFF official cadence: ≥5 s on change, ≥1 report/hour. **ALIVE-anchor expectation:** a healthy 02P emits SOMETHING at least hourly — the signal the availability wiring consumes.

**Confirmation expectation (dossier §2.4):** **`confirmation: []`** — no actuating capabilities (read-only measurements). Truth is anchored entirely by report freshness; the ALIVE-anchor scenarios are this device's real bench job.

**[CONFIRM-ON-BENCH] for the 02P (→ §5):** manufacturerCode/dateCode/firmware; IEEE; Basic `powerSource` byte (never key logic on it); whether any unit reports `SONOFF` on-wire; whether firmware honors a configured 0.1 °C reportable-change threshold; keep-awake/pairing-hold procedure.

---

### 3.4 Worksheet — SONOFF **SNZB-04P** (door/window contact · IAS + the twin-path watch)

**Placement:** DESK first (magnet reps near the coordinator); mount at the door only after this worksheet is complete. **Reed gap ≤ ~10 mm closed governs mounting.** **Physical:** battery sleepy; battery tab pull #2; magnet half at hand.

**Expected identity (dossier §3.1) `[REF]`:**
- manufacturerName = **`eWeLink`**, modelIdentifier = **`SNZB-04P`**. Profile key = `("eWeLink", "SNZB-04P")` — same manufacturer string as the bench-captured 03P → HIGH confidence.
- **Disambiguation trap:** a successor **`SNZB-04PR2`** exists as a distinct model — verify the sticker reads exactly `SNZB-04P`, not `-04PR2`.
- Battery sleepy end device. **Battery TYPE UNVERIFIED** — do NOT assume CR2032; capture caches 3.0 V (coin-cell class). Device type `0x0402` (IAS Zone); cached `zoneType = 21` (Contact Switch) → `contact`.

**Phase 0 capture (2026-07-15):**
- Model string (verbatim): **`SNZB-04P`** ✓ matches expectation — **NOT `SNZB-04PR2`** (disambiguation trap cleared) — **C-15 RESOLVED**
- Manufacturer/branding: **`SONOFF`** ✓ — on-wire `eWeLink` confirms at interview
- Firmware / dateCode (if printed): none reported; IC `29127-SNZB04P` + FCC `2APN5SNZB04P` corroborate the SNZB-04P family (IC prefix `29127` = same filer as the S31)
- **IEEE (housing): not the EUI-64.** QR + number = **`25303900144196`** — 14 DECIMAL digits → serial / QR code, NOT a EUI-64. Recorded as the unit serial; EUI-64 at join. → C-16 Phase-1.
- **Battery type (was UNVERIFIED): `CR2477`** ✓ — **RESOLVES the open research gap: the 04P uses CR2477, NOT CR2032** (the dossier explicitly warned not to assume CR2032). — **C-17 RESOLVED**
- Magnet half present in box? **Yes** — two pieces; mounting adhesive on both pieces present/good.
- Battery-tab pull: **(a) tab PULLED** (carried choice). LED behavior not separately noted by operator; family pattern established on the 02P.
- Staged: **yes — next to the dongle (coordinator), ready to pair before door mounting.** Door mount + reed-gap (≤ ~10 mm closed) deferred until after the join/characterization (desk-first, per the ruling).
- Notes / surprises: battery is CR2477 → **the three Wave-2 sensors share the CR2477 cell** (02P ✓, 04P ✓, 01P expected — one spare type covers the fleet). No `-04PR2` mislabel. Adhesive intact for the eventual door mount.

**Expected interview surface — carried to the join (dossier §3.2) `[REF]`:** EP1, profile `0x0104`, device type `0x0402`; in: `0x0000, 0x0001, 0x0003, 0x0020 (PollCtrl), 0x0500 (IAS Zone), 0xFC11, 0xFC57`; out: `0x0003, 0x0006 (genOnOff CLIENT!), 0x0019`. **[CONFIRM-ON-BENCH] cluster-id conflict:** the machine capture reads `0xFC57`; the ZHA quirk comment says `64567` (= `0xFC37`) — capture leads; our interview settles it.

**Expected reporting posture (dossier §3.3 vs Doc 08 §3.7):** battery % `min 3600 / max 7200 / change 2` + voltage (eWeLink-tuned, never silent past ~2 h); Doc 08 default `3600/62000/0` compatible. IAS `zoneStatus` is **event-driven** (ZoneStatusChangeNotification), NOT Configure-Reporting-driven → expect the reporting drive to cover PowerCfg only; a **1/N-verified posture is NORMAL here, not degradation.**

**Confirmation expectation (dossier §3.4):** **`confirmation: []`**. **THE TWIN-PATH WATCH:** the signature carries `genOnOff` as a CLIENT (output) cluster; the 04P can SEND on/off to bound targets (advertised device-to-device linkage), so one physical edge could emit IAS notification + OnOff-command twins if anything binds it. **REC for the hub's profile: do NOT bind the 04P's OnOff client cluster to the coordinator in V1** — characterize deliberately (bench-only, one-time) instead.

**[CONFIRM-ON-BENCH] for the 04P (→ §5):** manufacturerCode/dateCode/firmware; IEEE; **battery TYPE**; Basic `powerSource` byte (family misreport #24025 — never key logic on it); cluster-id `0xFC57` vs `0xFC37`; OnOff-linkage behavior (which command per edge; emits with no binding?); both-edges IAS reporting; whether enrollment is required before zone status.

---

### 3.5 Worksheet — SONOFF **SNZB-01P** (wireless button · the log-marker · the ESC gap)

**Placement:** desk instrument — the physical **log-marker** (a press stamps the log at operator-act time). **Physical:** battery sleepy; battery tab pull #3.

**Expected identity (dossier §4.1) `[REF]`:**
- manufacturerName = **`eWeLink`**, modelIdentifier = **`SNZB-01P`**. Profile key = `("eWeLink", "SNZB-01P")`.
- **Predecessor trap:** the old SNZB-01 reports model **`WB01`** (the shared quirk's primary key) — verify the sticker reads `SNZB-01P`, not `WB01`.
- Battery **1× CR2477** `[REF]`; sleepy ("press the button to keep it awake"). Device type `0x0000` (ON_OFF_SWITCH).

**Phase 0 capture (2026-07-15):**
- Model string (verbatim): **`SNZB-01P`** ✓ matches expectation exactly — **NOT `WB01`** (predecessor trap cleared) — **C-23 RESOLVED**
- Manufacturer/branding: **`SONOFF`** (FCC grantee `2APN5` = ITead/SONOFF) ✓ — on-wire `eWeLink` confirms at interview
- Firmware / dateCode (if printed): none reported; FCC `2APN5SNZB01P` + IC `29127-SNZB01P` corroborate the SNZB-01P family
- **IEEE (housing): not the EUI-64.** No EUI-64 and no QR serial reported (operator listed FCC/IC IDs only). EUI-64 at join. → C-24 Phase-1.
- Battery type (read the actual cell): **`CR2477`** ✓ matches expectation — **C-25 RESOLVED** (completes the sensor-trio CR2477 confirmation)
- Battery-tab pull: **(a) tab PULLED** (carried). LED not separately noted; family pattern established on the 02P.
- Staged: **yes — next to the other devices, waiting to pair.**
- Notes / surprises: none against the dossier; the predecessor `WB01` trap did not fire. This unit is the desk **log-marker** — a press stamps the log at operator-act time during the joins/bench runs.

**Expected interview surface — carried to the join (dossier §4.2) `[REF]`:** EP1, profile `0x0104`, device type `0x0000`; in: `0x0000, 0x0001, 0x0003, 0x0020 (PollCtrl), 0xFC57`; out: `0x0003, 0x0006 (genOnOff CLIENT — the event carrier), 0x0019`. **Precision detail:** the 01P carries `0xFC57` but **NOT `0xFC11`** — one custom cluster, unlike its 02P/04P siblings.

**The signal path (dossier §4.3 — FACT by verbatim code):** presses are **OnOff cluster CLIENT commands**, not reports: single → `toggle`, double → `on`, long → `off`. z2m binds the genOnOff output cluster to the coordinator at configure time. A press mints **NO** report and is not state-anchored — a missed press is silently gone.

**Expected reporting posture (dossier §4.4):** only `genPowerCfg` reports — battery `3600/7200/change 2` + voltage (eWeLink-tuned). A press produces no report.

**Confirmation expectation (dossier §4.5):** **`confirmation: []`**. **THE BUTTON GAP (ESC-W2-SNZB01P-01):** Doc 02 has no `button` entity type and no press capability; the press is a pure event, not canonical state. **Ruled V1 disposition = R2(B): adopt battery-only** (`sensor`/battery; presses visible in logs, absent from the device model — deliberate scoping; BTN-AMD is post-gate). Its bench role is exactly this: the **log-marker** — a press stamps the log so we can align operator acts to the event stream.

**[CONFIRM-ON-BENCH] for the 01P (→ §5):** manufacturerCode/dateCode/firmware; IEEE; Basic `powerSource` byte (misreport class #22032/#24007); press→command mapping on our unit (all three classes); awake-window duration after a press; binding behavior (the z2m "no direct control" vs the auto-bind bug conflict).

---

### 3.6 Phase 0 result — COMPLETE (2026-07-15)

**Done-when check (§3.0):**
1. Model + firmware/dateCode + IEEE per device — ✔ model captured on all four (**exact-model keys CONFIRMED**); firmware/dateCode not printed on any housing (→ interview); EUI-64 not printed on any housing (→ interview `device_announce`).
2. Battery type per sensor + tabs pulled without pairing — ✔ all three sensors = **CR2477**; tabs pulled (choice (a)); zero pairing initiated (no long-press); S31 has no tab (mains).
3. Worksheets filled; identity CoB items resolved-or-classified — ✔ (see §5: **8 items RESOLVED at the bench**; the rest classified to Phase-1 interview).
4. Bench staged within ~1 m of the coordinator; 04P magnet at hand — ✔ all four + the Hue clustered by the dongle; 04P magnet + adhesive ready; door-mount deferred (desk-first).

**Identity verdict — all four exact-model match keys CONFIRMED off the housings, zero surprises:**
- S31: `("SONOFF", "S31 Lite zb")` ✓ (the one SONOFF on-wire string; spaces/casing exact)
- 02P: model `SNZB-02P` ✓ (branding SONOFF; on-wire eWeLink pends interview)
- 04P: `SNZB-04P` ✓ (NOT `-04PR2`)
- 01P: `SNZB-01P` ✓ (NOT `WB01`)

**Cross-cutting Phase-0 findings (for the hub / corpus):**
1. **All three Wave-2 sensors run CR2477** — resolves the 04P's unverified battery type (NOT CR2032, as the dossier cautioned). One spare cell type covers the fleet.
2. **No device prints its EUI-64 on the housing** — the brief's "IEEE addresses … on the housings" assumption does not hold for this fleet; every EUI-64 is captured at join (`device_announce`). The 02P (`25471900074240`) and 04P (`25303900144196`) print a 14-decimal-digit **serial** QR (bind to the EUI-64 at join); the S31 and 01P print none.
3. **Regulatory IDs consistent across the fleet** — FCC grantee `2APN5` + IC filer `29127` on all four → a single manufacturer (ITead/SONOFF); the FCC/IC model suffixes independently corroborate each device family (`S31ZB`, `SNZB04P`, `SNZB01P`).
4. **S31 powered early** (operator plugged it in) — carried to §4 as a joins-session note; power-on relay-state read still open (C-06).

**Nothing needs debugging.** Every device matched our model at the identity layer; the only corrections were assumption-level (IEEE-not-on-housing) and a gap-closure (04P = CR2477), both banked. The fleet is staged and ready — the joins session stays **HUB-GATED** (§1).

---

## 4. Phase 1 — the joins session (⛔ HUB-GATED — STUB, do not start)

**Do not begin without the hub's explicit go, relayed by Nick.** Prerequisites the hub confirms first (both currently UNMET — §1): (1) the Wave-2 profiles WU landed on core + CI-green + deployed to the Pi; (2) the SEED formation ruling executed (the one-formation economy: SEED fresh formation = SD-5 discharge → Wave-1 rejoin → the four joins, one session).

At the go, the hub supplies the paste-blocks: formation → permit-join → per-device join order (**S31 first** — mains router, easiest interview; then **02P → 04P → 01P** with wake-press discipline) → per-device verify (announce → proposed COMPLETE → adopted → `reporting_configured` [expect honest TIMEOUT-class degradation on sleepy legs]) → the D1/B2 evidence reads. **If ANY device won't join stably, or any identity/verdict anomaly appears: ⏺ paste + STOP — never improvise; the hub adjudicates.**

Honest states NOT to panic about: `availability: UNKNOWN` on a fresh join until first evidence; `key_establishment_failed: TC_REJECTED_APP_KEY_REQUEST` WARNs post-join (the known policy-denial class, recorded).

**Phase-0 carry-ins to the joins session (for the hub's join sequence):**
- **The S31 is already powered** (plugged in during Phase 0) and factory-fresh → it will be network-hungry the moment a permit-join window opens. The join plan already puts S31 first, but the hub's paste-blocks should account for the S31 potentially attempting to join as soon as ANY permit-join opens — including during the SEED formation's Wave-1 rejoin step — rather than waiting for its designated slot. Not a defect; a sequencing note.
- **All three sensors have their tabs pulled** (choice (a)) and are powered/asleep next to the coordinator location. At join, a short wake-press lands them in the awake window; the ~5 s long-press is the pairing action (per the hub's blocks), not a Phase-0 act.
- **EUI-64s are NOT on the S31 or 02P housings** — capture them at `device_announce`. The 02P's printed serial `25471900074240` binds to its EUI-64 there.

*(This section fills with verbatim join transcripts, latencies, and per-device verify results when the joins session runs.)*

---

## 5. [CONFIRM-ON-BENCH] ledger (open / resolved)

Every device-specific unknown from §3, tracked to closure. Phase 0 can resolve the **identity/IEEE/battery** rows off the sticker; the rest resolve at interview (Phase 1).

| # | Device | Item | Resolvable in | Status | Resolution |
|---|---|---|---|---|---|
| C-01 | S31 | manufacturer string = `SONOFF`? | Phase 0 (sticker) | **RESOLVED** | `SONOFF` confirmed on housing (2026-07-15) |
| C-02 | S31 | model string = `S31 Lite zb` (spaces/casing)? | Phase 0 (sticker) | **RESOLVED** | `S31 Lite zb` confirmed on housing (2026-07-15) |
| C-03 | S31 | manufacturerCode / firmware / dateCode | Phase 0 partial / interview | OPEN | none printed on housing; capture at interview |
| C-04 | S31 | IEEE / EUI-64 address | **Phase 1 (interview)** — not on housing | OPEN | Housing shows `IEEE 802.15.4` (the STANDARD, not an address), FCC `2APN5S31ZB`, IC `29127-S31ZB`; no EUI-64 printed → get it at `device_announce`. Housing-IEEE assumption corrected. QR/hex recheck = none (2026-07-15). |
| C-05 | S31 | profileId `0xC05E` vs `0x0104` | Phase 1 (interview) | OPEN | |
| C-06 | S31 | power-on relay behavior (StartUpOnOff) | Phase 1 (power-cycle) | OPEN | S31 powered during Phase 0 (2026-07-15) — power-on relay state observable now; operator LED read pending; full StartUpOnOff characterization at join / Shelly wall-power scenarios |
| C-07 | S31 | command→report latency envelope | Phase 1 | OPEN | |
| C-08 | S31 | duplicate-report behavior / report-on-local-toggle | Phase 1 | OPEN | |
| C-09 | 02P | model = `SNZB-02P`; branding split (box SONOFF / wire eWeLink) | Phase 0 / interview | **PARTIAL** | model `SNZB-02P` ✓ + box branding `SONOFF` ✓ (2026-07-15); on-wire `eWeLink` confirms at interview |
| C-10 | 02P | IEEE / EUI-64 address | **Phase 1 (interview)** — not on housing | OPEN | Side QR = serial `25471900074240` (14 decimal digits — NOT a EUI-64); bind to EUI-64 at `device_announce` |
| C-11 | 02P | battery type = CR2477? | Phase 0 (cell) | **RESOLVED** | `CR2477` confirmed (printed on back cover) (2026-07-15) |
| C-12 | 02P | manufacturerCode / dateCode / firmware | Phase 0 partial / interview | OPEN | none printed on housing; capture at interview |
| C-13 | 02P | Basic `powerSource` byte | Phase 1 | OPEN | |
| C-14 | 02P | firmware honors 0.1 °C reportable-change? | Phase 1 (stimulus) | OPEN | |
| C-15 | 04P | model = `SNZB-04P` (NOT `-04PR2`) | Phase 0 (sticker) | **RESOLVED** | `SNZB-04P` confirmed; not `-04PR2` (2026-07-15) |
| C-16 | 04P | IEEE / EUI-64 address | **Phase 1 (interview)** — not on housing | OPEN | QR/number `25303900144196` (14 decimal → serial, NOT EUI-64); bind at `device_announce` |
| C-17 | 04P | **battery TYPE (unverified)** | Phase 0 (cell) | **RESOLVED** | **`CR2477`** — NOT CR2032; closes the dossier's unverified-battery gap (2026-07-15) |
| C-18 | 04P | manufacturerCode / dateCode / firmware | Phase 0 partial / interview | OPEN | IC `29127-SNZB04P` + FCC `2APN5SNZB04P` corroborate family; mfrCode/dateCode at interview |
| C-19 | 04P | cluster-id `0xFC57` vs `0xFC37` | Phase 1 (interview) | OPEN | |
| C-20 | 04P | OnOff-linkage behavior (per edge; unbound?) | Phase 1 (bench-only char) | OPEN | |
| C-21 | 04P | both-edges IAS reporting; enrollment required? | Phase 1 | OPEN | |
| C-22 | 04P | Basic `powerSource` byte | Phase 1 | OPEN | |
| C-23 | 01P | model = `SNZB-01P` (NOT `WB01`) | Phase 0 (sticker) | **RESOLVED** | `SNZB-01P` confirmed; not `WB01` (2026-07-15) |
| C-24 | 01P | IEEE / EUI-64 address | **Phase 1 (interview)** — not on housing | OPEN | no EUI-64 / no QR serial on housing (FCC/IC only); at `device_announce` |
| C-25 | 01P | battery type = CR2477? | Phase 0 (cell) | **RESOLVED** | `CR2477` confirmed (2026-07-15) |
| C-26 | 01P | manufacturerCode / dateCode / firmware | Phase 0 partial / interview | OPEN | FCC `2APN5SNZB01P` + IC `29127-SNZB01P` corroborate; mfrCode/dateCode at interview |
| C-27 | 01P | press→command mapping (single/double/long) on our unit | Phase 1 | OPEN | |
| C-28 | 01P | awake-window after a press; binding behavior | Phase 1 | OPEN | |
| C-29 | 01P | Basic `powerSource` byte | Phase 1 | OPEN | |

---

## 6. Session log (append-only — what happened, when)

- **2026-07-15** — Lane launched. Ground-truth set read in order (dossiers §§0–6 · corpus README + both Wave-1 entries + MG24 coordinator + Wave-1 bench-up report · M9.4 runbook Phases 3–5 · acceptance record close-out 2026-07-13/14 · PROJECT_SNAPSHOT v31 beat 2 · playbook §8). Live-state gate verified: **Phase 0 GO, Phase 1 HUB-GATED** (§1). Return file created with four seeded worksheets. Nick chose **device-by-device** Phase 0 (verify the model incrementally). Starting with the S31.
- **2026-07-15 — S31 Lite zb captured (device 1/4).** Model `S31 Lite zb` ✓ and manufacturer `SONOFF` ✓ confirmed on housing (C-01, C-02 resolved). **IEEE finding:** the EUI-64 is NOT printed on the housing — the housing label `Zigbee: IEEE 802.15.4 2.4 GHz` names the radio standard, not an address (operator initially read it as a possible IEEE; clarified). FCC `2APN5S31ZB` + IC `29127-S31ZB` corroborate the S31ZB family. C-04 reclassified to Phase-1 interview capture (QR/hex recheck returned none). The "IEEE is on the housing" assumption from the brief does not hold for this unit — a Phase-0 model-correction.
- **2026-07-15 — S31 powered early (deviation, recorded).** Nick plugged in the S31 during Phase 0 (plan had it unpowered); idle/harmless (no network, no permit-join). Logged as a joins-session carry-in (§4): the powered factory-fresh router will grab the first open permit-join window. C-06 note updated (power-on state now observable).
- **2026-07-15 — SNZB-02P captured (device 2/4).** Model `SNZB-02P` ✓, box branding `SONOFF` ✓ (on-wire eWeLink pends interview; C-09 partial). Battery `CR2477` ✓ (C-11 resolved). **IEEE finding:** side QR = `25471900074240` (14 decimal digits → NOT a EUI-64; recorded as unit serial, binds to EUI-64 at join; C-10 Phase-1). Tab pulled **(a)** — LED blink-then-settle, identical to the Wave-1 SNZB-03P (family-consistent). Choice (a) carries to 04P + 01P. Staged next to the Hue + S31. No surprises against the dossier.
- **2026-07-15 — SNZB-04P captured (device 3/4).** Model `SNZB-04P` ✓ (NOT `-04PR2` — trap cleared; C-15 resolved). **Battery `CR2477` — RESOLVES the dossier's UNVERIFIED battery type (it is NOT CR2032; C-17 resolved).** IC `29127-SNZB04P` + FCC `2APN5SNZB04P` corroborate. QR/number `25303900144196` = serial (14 decimal, not EUI-64; C-16 Phase-1). Two pieces + adhesive intact; tab pulled (a); staged next to the dongle, door-mount deferred (desk-first). Cross-cutting finding: all three Wave-2 sensors run on CR2477.
- **2026-07-15 — SNZB-01P captured (device 4/4).** Model `SNZB-01P` ✓ exactly (NOT `WB01` — predecessor trap cleared; C-23 resolved). Battery `CR2477` ✓ (C-25 resolved — completes the sensor-trio CR2477 confirmation). FCC `2APN5SNZB01P` + IC `29127-SNZB01P` corroborate. No EUI-64 / QR serial on housing (C-24 Phase-1). Tab pulled (a); staged; the desk log-marker.
- **2026-07-15 — PHASE 0 COMPLETE.** All four devices captured device-by-device; every exact-model key confirmed off the housings, zero surprises; 8 CoB items resolved at the bench (§3.6 result). Fleet staged by the dongle. **Holding at the Phase-1 hub gate** (§1): joins do not start until the hub's explicit go (profiles WU landed/deployed + SEED formation executed), relayed by Nick. This lane wrote only this one file.

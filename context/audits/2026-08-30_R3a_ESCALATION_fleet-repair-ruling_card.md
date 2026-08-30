<!--
file: _scratch/2026-08-30_R3a_ESCALATION_fleet-repair-ruling_card.md
purpose: A SELF-CONTAINED ruling card (H10 form: branches + recommendation + one-word ask). A fresh hub session must be able to rule from THIS FILE ALONE, without the R-3a operator conversation and without reading the 90 KB record. Evidence pointers are given but reading them is optional to the ruling.
audience: the hub (v58) — the adjudicator. Nick — the operator, who declined to choose at the bench and escalated.
status: OPEN — R-3a §10 is HELD pending this ruling. §1–§9 are COMPLETE and ALL GATES PASSED.
raised: Sun 2026-08-30 ~11:50 ET / 10:50 CT.
-->

# RULING CARD — where to re-pair the motion sensor (R-3a §10 held)

## THE ASK

**One word: `RIG`, `BENCH`, or `DEFER`.** Definitions in §5.

---

## §1 WHAT HAPPENED (self-contained)

R-3a ran today. §1–§9 completed with every STOP-gate passed: the E3 class closed on hardware, the first CI-built `+git` artifact installed with zero event loss, and the §7 drop-in measured sufficient on first try (P-a, `zigbee.network_resumed: channel=20 panId=0x774c`) — **so R-3b's spec is locked and needs nothing further from today.**

§10 (the evidence window) then hit an unanticipated condition, **finding §9-B**: *a custody clone transfers the Zigbee network but NOT the HomeSynapse adoptions.* The cloned device cache loaded 6 devices but `adoption_maps_rehydrated: devices=0`, zero `device_relinked`, and the dashboard reports `Available 0 of 0`. Adoption identity lives in the event store, which was correctly NOT cloned (the held card has its own `home_id`). So the fleet must RE-ADOPT device-by-device as each device next speaks — the packet's §10 expectation ("5 Available + 1 Unavailable") is unreachable on a cloned-custody card.

Driving that re-adoption required a device to transmit. Attempting the packet's own P-f probe (power-cycle the motion sensor), **the operator held the button past ~5 s, which on an SNZB-03P is a network LEAVE, not a power cycle:**

```
Aug 30 11:43:01 hs-fresh  INFO c.h.i.zigbee.ZclIngestionUnit --
  zigbee.device_left: device=0xF044D3FFFE9C78D7 nwk=0x1955
```

`0xF044D3FFFE9C78D7` = the SNZB-03P motion sensor (bench deviceId `01KX1PB9A5931A8G0F0X03QXT2`). **It is off the bench's Zigbee network and cannot rejoin: no permit-join window is open on either card**, because `permit_join_duration` was removed from the bench config at soak entry on 2026-07-10 and therefore is absent from the clone.

**It must be re-paired before the bench is whole. That is not optional. The only question is WHERE.**

---

## §2 CURRENT STATE

- **Held card `hs-fresh`** — powered, service `active`, artifact `0.1.0+git20260823.231355.gdec35be`, R-9 unit + the §7 drop-in, bench custody cloned (PAN 0x774c / ch 20), registry EMPTY, `home_id 01KZXEG38VC0ZT375GZ3H1P5QS`, 27 event rows, `integrity_check ok`.
- **Coordinator** — the SONOFF dongle, plugged into the held card since 09:07:08 ET, hub 3-2.4 Port 2, by-id string byte-identical to the pre-swap bench capture.
- **Motion sensor** — OFF the network since 11:43:01 ET. Pairing mode has almost certainly timed out; recovery requires holding its button again, which is repeatable at will.
- **Other five devices** — still network members, still unadopted by the held card, silent (nothing has transmitted).
- **Bench card `hs-dev-1`** — OUT of its slot, powered off, **since 08:19:14 ET**. The bench is DOWN.
- **`bench-hero`** — present on the held card and `On` (it travelled in the clone). It is blocked on the missing adoption, not missing itself.

---

## §3 THE CLOCK, AND THE DEFAULT-BY-DRIFT

**Hard floor: the bench must be running with `[PASS] boot-health` before Mon 03:00 CT / 04:00 ET**, so the 04:30 ET nightly oneshot finds it up. §11 (the restore) needs ~30 min.

**Branches BENCH and DEFER allow §11 to proceed immediately. Branch RIG requires staying on the held card for ~15–20 min more.** Therefore **waiting past a point silently selects BENCH.** Naming it rather than letting it drift:

> **If no word has arrived by 16:00 CT today, the operator proceeds to §11 and restores the bench, and the re-pair becomes a separate act on another day. That is BENCH by default.**

That leaves ~5 h for a ruling and ~11 h of margin on the floor.

---

## §4 VERIFIED AT SOURCE BEFORE ESCALATING (this removes the one real technical risk)

The obvious hazard with re-pairing on the held card is key divergence: if per-device Trust-Centre link keys were persisted host-side, pairing on the rig would write a key into the rig's `secrets.enc` that the bench's copy lacks, breaking the device on the bench. **Checked at `dec35be`, read-only:**

```
* each device its seed-derived hashed TCLK, exactly the bellows posture
* generated TCLK seed (each loaded from custody or minted fresh)
private static final int TCLK_SEED_LENGTH_BYTES = 16;
```

**HomeSynapse runs hashed TCLK — per-device keys are DERIVED from one 16-byte seed plus the device address, never stored per device.** That seed is in `secrets.enc`, byte-identical on both cards (cloned; sha256 `ccface0ecff495fcb5d5aa53de7ae87a72cd47ea8d3aadcd968ce4b9377b77cb`). **A re-pair on the rig derives exactly the key the bench derives. No divergence risk on either branch.**

---

## §5 THE BRANCHES

### `RIG` — re-pair on the held card now  **(the guide's recommendation)**
Add `permit_join_duration` to the held card's cloned `zigbee.yaml`, restart, hold the sensor's button, observe `device_announce → interview → device_proposed → proposal_accepted → device_adopted` through the cloned `adopt_devices` list, then **remove the key and restart** (the documented M9.4 runbook step-18 posture). Then §10's window, then §11.

- **Gains:** §10 stops being empty. It measures the **P-e re-adoption path on the packaged artifact under the drop-in** — which finding §9-B just established is the ONLY path available to a cloned-custody rig, and which R-4 will therefore depend on. `bench-hero` can fire, so **R-4 criteria (2) *≥1 device Available* and (4) *one automation run with a rendered explanation* both become reachable.**
- **Costs / risks:** opens a bounded Zigbee join window on the live home network (max 254 s; the project's own documented pairing mechanism). The sensor gains an adoption record in the RIG's registry — local and disposable. Adds ~15–20 min of bench downtime.
- **Note:** the pairing operation happens on the throwaway rig, NOT on the production bench.

### `BENCH` — restore first, re-pair on the bench afterward
Proceed to §11 now. Later, on the bench: add `permit_join_duration`, restart, re-pair, remove the key, restart again.

- **Gains:** the device returns to the rig whose registry already holds its adoption record; the held card's posture stays clean (no join window ever opened there).
- **Costs:** performs a config edit and **two service restarts on the PRODUCTION bench** in the hours before the 04:30 ET nightly. **§10 ends with no fleet evidence at all — R-4 criteria (2) and (4) both recorded MISS**, and the P-e path that R-4 will depend on goes unrehearsed.

### `DEFER` — restore now, re-pair another day
Proceed to §11; leave the sensor off-network.

- **Costs:** `bench-hero`'s trigger device is off the network, so **tonight's nightly likely goes RED on any bench-hero leg** — knowingly leaving a broken bench for the 04:30 ET run. §10 evidence: none.

---

## §6 THE GUIDE'S RECOMMENDATION — `RIG`

Four reasons: **(1)** the key-divergence risk is disproven at source, so both locations are equally safe on keys; **(2)** it keeps a pairing operation OFF the production bench and on the disposable rig, hours before the nightly; **(3)** the sensor must be re-paired regardless, so this costs one operation instead of two; **(4)** decisively — finding §9-B established that re-adoption is the *only* fleet path on a cloned-custody rig, which is exactly the rig R-4 will use. Rehearsing it today is the highest-value evidence still available, and `BENCH`/`DEFER` forfeit it.

**Named risk, honestly:** a permit-join window on the live home network for a bounded period. The exposure is devices in pairing mode within radio range; only the SNZB is a candidate. This card recommends the act with that risk stated, not minimised.

---

## §7 WHAT THIS RULING DOES *NOT* DECIDE

- **R-3b is unaffected.** §9 measured P-a on the first try; the drop-in text is locked and needs nothing from §10.
- **The D-1 pair stays DO-NOT-SAY.** Nothing lifts today; R-4 owns the lift.
- **§11 runs regardless**, on every branch. The bench floor is the day's exit criterion and is not negotiable against any of this.
- **Nothing has been committed to any repo.** Core porcelain verified EMPTY at `5051fa5`; all artifacts are in `_scratch/`.

---

## §8 POINTERS (optional to the ruling)

- Full operator record incl. the complete verbatim transcript, source verification and amendment ledger: `_scratch/2026-08-30_R3a_rehearsal_operator-record_RUNNING.md` (~90 KB; findings table is at the top).
- Saturday's deferral ruling + the pre-run desk audit that produced amendments F-A1…F-A5: `_scratch/2026-08-29_R3a_DEFERRED_desk-audit_operator-return.md`.
- The packet of record (unmodified): `context/handoff/2026-08-26_R3a_rehearsal_operator-packet.md`.

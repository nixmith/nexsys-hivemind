<!--
file: context/handoff/2026-07-19_04p-adoption_BENCH-STOP_learn-persist-finding.md
purpose: Bench-session report for the v35 hub — the 04P adoption was ABORTED at Window #1 on a cached-interview ordering hazard; the W2-LEARN code is SILICON-CONFIRMED (the zoneType learn fires on the wire); the bench was returned to standing posture with NOTHING durable changed; LEARN-PERSIST is the required fix before the 04P can be adopted. D1 stays 4/5.
audience: the v35 PM mission-control hub; Nick.
state-type: bench-session report / operator return.
status: CURRENT — authored 2026-07-19 from the live bench session (operator: Nick; adjudicator: the bench hub). LANDED on the spine by the v35 hub at beat 3 (delivered in-conversation; this file is the verbatim record; hub two-layer audit: ACCEPT-WITH-ADJUDICATIONS ×2 — pm-handoff v35 beat 3).
consumes: 2026-07-19_04p-adoption_operator-mini-package.md (SUPERSEDED by this finding); W2-LEARN core commit 554e18c; integration-zigbee MODULE_CONTEXT (W2-LEARN + M9.4-ADP sections).
-->

# 04P ADOPTION — BENCH STOP + the LEARN-PERSIST finding (report for the v35 hub)

## 0. TL;DR / Verdict

The 04P adoption was **stopped at Window #1 — deliberately, on a real one-way-door hazard — and NOT adopted.** Two things came out of the night, both important:

1. **W2-LEARN's code half is silicon-confirmed.** The zoneType learn fires correctly on the wire: `zigbee.ias_zone_type_learned: device=0x449FDAFFFE688F57 zoneType=CONTACT (was MOTION)`. The enroll-payload parse and the learn work end-to-end on real silicon. This is a genuine positive result.

2. **The two-window adoption plan's ordering assumption is falsified for a cached-interview device.** On the 04P's re-join, `device_proposed … COMPLETE` fired **0.8 s** after the announce (cached interview), while `ias_zone_type_learned … CONTACT` didn't land until **~9 s later** (the IAS enroll is gated behind the TCLK key exchange). Because the config-accept adopt fires **at the proposal**, and the learned-zoneType map is **in-memory and wiped by the restart the accept-list requires**, adopting in Block 4 would have classified the 04P as **MOTION durably** (no `device_removed` emitter exists → no un-adopt). Window #1 exists to test exactly this ordering before committing, and it correctly caught it.

**Decision:** STOP; do not accept-list, do not adopt. Bench returned to standing posture (permit key removed, 04P still HELD, fleet 5/5 intact, **`projection_live position=18946` unchanged → zero registry mutations tonight**).

**Required fix:** **LEARN-PERSIST** — persist learned zoneTypes across restarts and rehydrate them at boot before any join, so the learn precedes the fast propose/adopt. This was already a named candidate; it is now a **required predecessor** to the 04P adoption, not optional.

**Milestone impact:** **D1 stays 4/5.** The M14 sweep's D1 condition remains open. W2-LEARN's WU done-when (04P adopts as contact) is **deferred** pending LEARN-PERSIST; its code is landed + audited + now partially silicon-verified.

---

## 1. What ran, and what didn't

Deploy state at the instrument: core **HEAD `554e18c`** (W2-LEARN + the S31-ROUTE closure), built on the Pi via `./gradlew :app:homesynapse-app:installDist` (operator history lines 592–593). `HOMESYNAPSE_HOME=~/hs-bench`; config `~/hs-bench/config/integrations/zigbee.yaml`.

| Block | Status | Outcome |
|---|---|---|
| 0 — deploy re-verify | ✅ PASS | `git log` = `554e18c`; HEAD = origin/main. |
| 1 — window key ON | ✅ PASS (after a corrected edit) | `permit_join_duration: 254` activated; `adopt_devices` = 5, 04P held. (See §10 for the grep-guard correction.) |
| 2 — Window #1: wire learn | ⛔ **STOP (ordering)** | Learn fired on the wire (✓ good) but **after** the proposal (✗ — the hazard). |
| 3 — accept-list | **NOT RUN** | Correctly not reached. |
| 4 — Window #2: adoption | **NOT RUN** | Correctly not reached (the one-way door). |
| 5 — reads / D1 5/5 | **NOT RUN** | — |
| 6 — close-down + BENCH-CONST | ✅ (close-down only) | Standing posture restored + verified; no 6/6 BENCH-CONST capture (we're still 5/5). |

**CI-green on `554e18c`:** requested three times; not explicitly confirmed by the operator before proceeding. It is **behaviorally proven live** (the W2-LEARN learn fired = the code is running), and nothing durable was committed tonight, so this did not affect the outcome — but the hub should still confirm CI-green on `554e18c` for the W2-LEARN WUCP record.

---

## 2. The positive result — W2-LEARN is silicon-confirmed (the learn fires)

From the Window #1 arc (log `bench-2026-07-19-121417.log`), the 04P (`0x449FDAFFFE688F57`, serial 25303900144196) re-joined and produced the learn correctly:

```
12:17:50.746  zigbee.device_announce:        device=0x449FDAFFFE688F57 nwk=0x11f0
12:17:51.519  zigbee.device_proposed:        …eWeLink SNZB-04P profile=sonoff_snzb_04p status=COMPLETE
12:17:54.254  zigbee.key_established:         device=0x449FDAFFFE688F57 status=TC_REQUESTER_VERIFY_KEY_SUCCESS
12:18:00.725  zigbee.ias_zone_type_learned:  device=0x449FDAFFFE688F57 zoneType=CONTACT (was MOTION)
12:18:00.735  zigbee.ias_zone_enrolled:      device=0x449FDAFFFE688F57 endpoint=1 zoneId=0
```

`ias_zone_type_learned … zoneType=CONTACT (was MOTION)` is the exact line W2-LEARN exists to produce, on real silicon, from a real ZoneEnrollRequest payload. The interview completed COMPLETE as SNZB-04P, the TCLK exchange verified cleanly (`TC_REQUESTER_VERIFY_KEY_SUCCESS`), and the announced EUI matched the held value. **The code half of W2-LEARN is confirmed working.** (Operator timeline corroborates: button-press ~11:17:46 local ⇒ the leave/join at Pi-clock 12:17:43/50; the door-open ~11:19:10 came *after* the learn at 12:18:00 — so the enroll was join-driven, not door-driven, which is the natural post-join, TCLK-gated behavior.)

---

## 3. The finding — the ordering hazard (why we stopped)

### 3.1 The evidence

```
12:17:50.746  device_announce                         ── t0
12:17:51.519  device_proposed … COMPLETE              ── t0 + 0.8 s   (cached interview → instant propose)
12:17:54.254  key_established (TCLK verified)          ── t0 + 3.5 s
12:18:00.725  ias_zone_type_learned … CONTACT          ── t0 + 9.98 s  (enroll gated behind TCLK)
```

**The proposal beat the learn by ~9.2 seconds**, and the proposal landed only 0.8 s after the announce.

### 3.2 The mechanism (grounded in the module's own contracts)

Chain the observed ordering against how adoption works — from `integration-zigbee/MODULE_CONTEXT.md`:

1. **The accept-list is initialize-time.** "Acceptance is initialize-time … the accept list is read once per adapter lifecycle; adding the key requires a restart, and a device proposed before the key existed adopts on its next re-propose (restart + device power-cycle re-announces)." → Listing the 04P (Block 3) forces the Block-4 restart.
2. **The learned-zoneType map is in-memory, cycle-thread-confined.** W2-LEARN notes: "No locking added … `learnedZoneTypes` stays cycle-thread confined." It is **not persisted** → **the restart wipes it.**
3. **`adopt()`'s classify is a deferred, learned-ONLY read; unlearned ⇒ MOTION default.** "`learnedZoneType` ≠ `effectiveZoneType`: the accessor is LEARNED-ONLY by design — folding in the resolver default would make the classifier's unlearned arm unreachable (every unlearned device would read MOTION-as-learned)." And "The §4 wiring is a deferred read … the method-reference source null-guards the window."
4. **The config-accept adopt fires AT `device_proposed … COMPLETE`** (M9.4-ADP `adoptIfAccepted`: PROPOSED + listed + COMPLETE ⇒ `proposal_accepted source=config` + `adopt()`), synchronously on the ingestion thread.
5. **A wrong adoption is durable** — `device_removed` has an honored tombstone path but **no emitter** (per M9.5-DUR: "proven by test though nothing emits it yet"); there is no operational un-adopt. Undoing a mis-adoption requires a full re-formation.

**Put together:** in Block 4, on the fresh post-restart session, the 04P re-announces, proposes in <1 s (cached), and — now listed — the config-accept path calls `adopt()` **at that proposal**, ~9 s **before** the re-pair's enroll/learn lands. `adopt()`'s classify reads an **empty** learnedZoneTypes map (wiped by the restart) → **MOTION**. Result: a **durable binary_sensor/motion** adoption of a contact sensor — precisely the failure W2-LEARN and the two-window guard were meant to prevent. The design's own requirement — "the go-package's guard observes `ias_zone_type_learned … zoneType=CONTACT` BEFORE the 04P's adopt step (the end-to-end test pins exactly that ordering)" (MODULE_CONTEXT, joins-night sequencing rationale P12) — is violated by the observed arc.

---

## 4. The decision + reversibility analysis

**STOP; do not accept-list, do not adopt.** The risk is **asymmetric and irreversible**:

- Downside of proceeding: a durable binary_sensor/motion adoption with no un-adopt path → a full network re-formation to fix, which also nukes the other 5 adoptions and their identities → far more than one night's work, and it breaks the D1 gate it was meant to close.
- Downside of stopping: one small, well-scoped code WU (LEARN-PERSIST) + a redeploy + a short re-run.

Per the bench escalation ladder ("architecture-class changes … options framed, Nick rules, never under bench pressure"), the STOP was surfaced with the reasoning and the recommendation; Nick concurred. Window #1 performed its designed function: falsify the ordering assumption on live silicon **before** the one-way door, not after.

---

## 5. Root cause — the cached-interview fast-propose race

The two-window plan rested on "3/3 enrollments arrived before any propose on joins night." That evidence was gathered with **fresh** interviews (first-ever joins — slow interview, enroll landed first). Tonight the 04P's interview is **cached** in `zigbee-devices.json` (preserved through joins night and this session), so its re-join proposes **instantly** (0.8 s), while the IAS enroll is inherently later (gated behind the TCLK key exchange at t0+3.5 s, landing at t0+10 s). The long-press leave did **not** invalidate the cache (the 0.8 s propose proves it), so Block 4 would race identically.

**Durable lesson (for coder-lessons / the bench playbook):** a cached interview proposes in <1 s, before the TCLK-gated IAS enroll (~10 s); **the enroll-before-propose ordering holds only for FRESH interviews.** Any adopt-time classify that depends on a post-join learn must not assume a cached-interview device re-learns before it proposes.

---

## 6. Recommended fix — LEARN-PERSIST (design sketch for the Coder WU)

**Goal:** the learned zoneType survives a restart and is present in the map **before** the first propose, so `adopt()`'s classify reads it regardless of the cached-interview race.

**Shape (mirrors existing zigbee-persistence patterns):**
- **Persist on learn.** When `ias_zone_type_learned` fires, write the `IEEEAddress → ZoneType` entry to a small sidecar (e.g. `~/hs-bench/data/zigbee/zigbee-learned-zonetypes.json`), debounced + shutdown-flush, exactly like `ZigbeeDeviceCache` (zigbee-devices.json) and the `lastKnownAvailability` sidecar. Alternatively fold a `learnedZoneType` field into `ZigbeeDeviceRecord` (weigh: that record is schema-frozen; a separate sidecar avoids touching it — recommend the sidecar).
- **Rehydrate at boot, before joins.** In `initialize()`, load the sidecar into `learnedZoneTypes` before the adapter starts joining/adopting (alongside `adoption_maps_rehydrated`), so the map is warm when the first propose fires.
- **Preserve LEARNED-ONLY semantics.** Persist only actual learns; do NOT fold in the MOTION default (keeps the classifier's unlearned arm reachable — the existing contract). Corrupt/missing file ⇒ empty map + WARN ⇒ unlearned/MOTION default (fail-safe = current behavior, no regression). Re-learn is idempotent.
- **Add a new INFO** at rehydrate (e.g. `zigbee.learned_zonetypes_rehydrated: count=N`) as the anti-vacuous boot glance-point (matches the instrument-first doctrine).

**Tests (before impl):** persist→shutdown→new-session-rehydrate→classify reads CONTACT before any join; corrupt-file ⇒ empty + WARN; debounce + shutdown flush; the rehydrated learn drives an adopt classify to `contact` even when the propose precedes any live enroll (the exact race, in a hardware-free IT).

**Payoff:** likely collapses the silicon flow to a **single window** — pair once (learn fires + persists) → accept-list → restart → rehydrate → the 04P re-announces/re-pairs → `adopt()` reads the persisted CONTACT → `device_adopted entities=1` binary_sensor/contact. Scope: single module (integration-zigbee), ~one coding-instruction WU.

*(Hub adjudication at intake, 2026-07-19 — pm-handoff v35 beat 3: the WU as authored rides the DISCOVERED in-file precedent — `zigbee-devices.json` already carries the `lastKnownAvailability` additive sidecar "tolerated-additively by this loader" — so no new file is minted; and the single-window payoff holds only for SUBSEQUENT re-adoptions: the FIRST post-LEARN-PERSIST adoption keeps the two-window shape, because tonight's learn was in-memory and is already lost — listing the 04P before a learn has PERSISTED would recreate the exact race.)*

---

## 7. Alternatives considered and rejected

- **Clear the 04P's interview cache** to force a fresh (slow) interview tonight, restoring enroll-before-propose. **Rejected:** touches `zigbee-devices.json` (an anti-action), not guaranteed for a sleepy device, and a wrong race is durable MOTION. Irreversible downside to save one WU.
- **Gate the config-accept adopt on IAS-enroll completion for 0x0500-bearing endpoints** (defer adopt until enroll lands, or re-classify on learn). **Viable but heavier** — changes the adopt trigger timing and/or adds a re-classify path. LEARN-PERSIST is lighter, fixes the general cross-restart case, and doesn't touch the adopt trigger.
- **Proceed and accept a possible MOTION adopt, fix later.** **Rejected** — durable, no un-adopt.

---

## 8. Bench state after tonight (verified standing posture)

Close-down (`bench-2026-07-19-124151.log`) confirms nothing durable changed:
- Config: `permit_join_duration` removed; `adopt_devices` = the same 5 entries; the 04P still `# HELD: 0x449FDAFFFE688F57`.
- Boot: `registry.projection_live: devices=5 entities=5 position=18946` — **`position=18946` is identical to the Window-#1 boot ⇒ zero registry events were appended tonight** (no adoptions, no registrations). `adoption_maps_rehydrated: devices=5`; `network_resumed: channel=20 panId=0x774c`; **`permit_join_opened` count = 0** (window not reopened).
- Entities: **5/5 AVAILABLE, stale=false**; all ULIDs unchanged (identity stable). `viewPosition=21117` (state view advanced only by availability edges — not identity).

The 04P sits joined-but-unadopted (as it did after joins night) — benign; it re-pairs cleanly on the fixed build.

**Captured values (for the record; NOT a BENCH-CONST re-mint — that waits for 6/6):** `projection_live devices=5 entities=5 position=18946` · `channel=20 panId=0x774c` · fleet ULIDs in Appendix B.

---

## 9. Impact on milestones / spine

- **D1: stays 4/5.** The 04P (binary_sensor/contact) remains the missing class. The M14 sweep's **D1 condition remains OPEN**; SEED ✓, RO ✓, AVAIL ✓, G1 dispatch OUT still the other open condition. *(Hub adjudication at intake: STALE against v35 beat 2 — G1 is dispatched + returned + audited ACCEPT; its residual is the frontend.yml gate-of-record glance on Nick's push. D1 is the sweep's only open trigger condition.)*
- **W2-LEARN WU:** code landed (`554e18c`) + hub audit ACCEPT + local check GREEN; **the learn is now silicon-confirmed** (the code half is done and proven). The WU's silicon **done-when — "04P adopts as BINARY_SENSOR/contact → D1 5/5" — is DEFERRED** pending LEARN-PERSIST. Recommend recording W2-LEARN as "code-complete + learn-silicon-verified; adoption done-when blocked on LEARN-PERSIST," not fully DONE.
- **The 04P operator mini-package is SUPERSEDED** — its two-window ordering assumption is falsified for cached interviews. Re-author to the persisted-learn flow after LEARN-PERSIST lands.
- **LEARN-PERSIST** is promoted from "named candidate" to **required predecessor** of the 04P adoption / D1 5/5.
- **S31-ROUTE** (bundled in `554e18c`) is deployed but **not silicon-exercised tonight** (anti-action: only the 04P was touched). Its bench confirmation (S31 physical-button press → report routes → state change) still rides a future session.
- **CI-green on `554e18c`:** confirm for the record (see §1).

---

## 10. Process note — the Block-1 grep-guard correction

The first Block-1 command used the operator's idempotent add `grep -q permit_join_duration … || echo "permit_join_duration: 254" >> …`. The joins-night close-down had **commented** the key (`# permit_join_duration: 254`) rather than deleting it, so `grep -q` matched the comment and the append was skipped — the key stayed inactive. Caught immediately by the `cat` read-back and corrected (uncomment in place). **Lesson:** a grep-guard that gates a config-key add must anchor to a non-comment, active line (`^[[:space:]]*permit_join_duration:`), or the read-back is the only thing standing between it and a silent no-op. No downstream effect (caught before boot).

---

## 11. Next actions for the v35 hub (checklist)

1. **Author the LEARN-PERSIST coding instruction** (Coder WU) per the §6 sketch — the fix that unblocks the 04P adoption and D1 5/5.
2. **Record the finding on the spine:** coder-lessons (the cached-interview propose-before-enroll race + the enroll-before-propose-only-for-fresh-interviews rule); an `integration-zigbee` MODULE_CONTEXT gotcha; and the durable-adoption/no-un-adopt reminder. Update the bench-troubleshooting-playbook §7 (restart semantics) with the in-memory-learn-wiped-by-restart case.
3. **Supersede + re-author the 04P operator package** to the persisted-learn flow (likely single-window) once LEARN-PERSIST lands.
4. **WUCP for W2-LEARN:** mark code-complete + learn-silicon-verified; the adoption done-when deferred to post-LEARN-PERSIST; confirm CI-green on `554e18c`.
5. **Keep D1 at 4/5** on the M14 sweep tracker; note LEARN-PERSIST as the gating predecessor.
6. **Schedule S31-ROUTE's silicon confirmation** (rides any future window on `554e18c`+).
7. **Re-run the 04P adoption** on the LEARN-PERSIST build (Nick, at the bench) → D1 5/5 → then the 6/6 BENCH-CONST re-mint.

---

## Appendix A — key raw evidence

**Window #1 arc (`bench-2026-07-19-121417.log`):**
```
12:17:43.790 zigbee.child_left:  child=0x449FDAFFFE688F57 nwk=0x773b type=SLEEPY_END_DEVICE
12:17:43.791 zigbee.device_left: device=0x449FDAFFFE688F57 nwk=0x773b
12:17:50.698 zigbee.device_join: device=0x449FDAFFFE688F57 nwk=0x11f0 status=UNSECURED_JOIN decision=USE_PRECONFIGURED_KEY
12:17:50.746 zigbee.device_announce:       device=0x449FDAFFFE688F57 nwk=0x11f0
12:17:51.519 zigbee.device_proposed:       …eWeLink SNZB-04P profile=sonoff_snzb_04p status=COMPLETE
12:17:54.254 zigbee.key_established:        device=0x449FDAFFFE688F57 status=TC_REQUESTER_VERIFY_KEY_SUCCESS
12:18:00.725 zigbee.ias_zone_type_learned: device=0x449FDAFFFE688F57 zoneType=CONTACT (was MOTION)
12:18:00.735 zigbee.ias_zone_enrolled:     device=0x449FDAFFFE688F57 endpoint=1 zoneId=0
```
(Also seen, benign: `12:19:25 key_establishment_failed device=0xFFFFFFFFFFFFFFFF status=TC_REQUESTER_VERIFY_KEY_TIMEOUT` — the wildcard transient join key self-expiring, an honest expected state.)

**Close-down boot (`bench-2026-07-19-124151.log`):**
```
12:41:54.443 registry.projection_live: devices=5 entities=5 position=18946
12:41:55.022 zigbee.adoption_maps_rehydrated: devices=5
12:42:02.743 zigbee.network_resumed: channel=20 panId=0x774c
grep -c "permit_join_opened" = 0
entities: 5/5 AVAILABLE, viewPosition=21117
```

**Config at close (`~/hs-bench/config/integrations/zigbee.yaml`):** `serial_port: /dev/zigbee` · `channel: 20` · `adopt_devices` = the 5 below · `# HELD: 0x449FDAFFFE688F57 SNZB-04P` · no `permit_join_duration`.

## Appendix B — reference facts (device → EUI → deviceId → entityId)

| Device | EUI-64 | deviceId | entityId | Class |
|---|---|---|---|---|
| Hue LCA017 | 0x00178801101A09BB | 01KX1PA4GRZHY2GD37B5CFVQHY | 01KX1PA4HSJ581GASYB7DHE40F | light |
| SNZB-03P | 0xF044D3FFFE9C78D7 | 01KX1PB9A5931A8G0F0X03QXT2 | 01KX1PB9AAB4VB3E10BD477TV3 | binary_sensor/occupancy |
| S31 Lite zb | 0x00124B002FA8D1C5 | 01KXW1W1RR66GV98D9QDPB4VXY | 01KXW1W1SBJZERC9MBAMV2DWKE | switch |
| SNZB-02P | 0xF044D3FFFED2A201 | 01KXW0156Z1GJ3WCV2G516AKWS | 01KXW0157SP56CCSGJCNDCSQNG | sensor: temp/humidity/battery |
| SNZB-01P | 0xF044D3FFFE1C1E8E | 01KXW13WEGRCT5C0XSQT8WZBG9 | 01KXW13WF0D6TYGN13WXHTG87K | sensor: battery |
| **SNZB-04P (HELD)** | **0x449FDAFFFE688F57** | — (unadopted) | — | **target: binary_sensor/contact** |

**Environment:** core HEAD `554e18c` (W2-LEARN + S31-ROUTE) · build `./gradlew :app:homesynapse-app:installDist` · `HOMESYNAPSE_HOME=~/hs-bench` · config `~/hs-bench/config/integrations/zigbee.yaml` · data `~/hs-bench/data/zigbee/` · API loopback `127.0.0.1:7070` · launcher `~/bench.sh` (→ `~/nexsys-bench/tools/bench.sh`) · coordinator SONOFF MG24 @ `/dev/zigbee`, EZSP v13 / stack 0x7450 · network channel 20 / panId 0x774c.

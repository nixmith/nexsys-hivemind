<!--
file: context/handoff/2026-07-19_04p-adoption_operator-mini-package_v2-persist-verified.md
purpose: Operator mini-package v2 — the 04P (SNZB-04P contact) adoption on the LEARN-PERSIST build. SUPERSEDES the 2026-07-19 v1 package (its ordering assumption was falsified for cached interviews — the BENCH-STOP finding). The persist-verified two-window shape: the learn must be PERSISTED-verified before the 04P is ever listed, and the Window-#2 boot glance is the one-way-door STOP gate.
audience: Nick (operator); the v35 hub (paste adjudication).
state-type: operator package (paste-blocks; playbook §8 contract).
status: ⛔ GATED — run ONLY after ALL of: the LEARN-PERSIST core commit LANDED + pushed · CI GREEN on the pushed SHA (the gate of record) · the Pi deploy re-verified AT the instrument (Block 0). Authored 2026-07-19 (v35 hub, beat 5).
in-memory-state hazards: NONE remaining for the learn (it persists via zigbee-devices.json `learnedZoneTypes` + shutdown flush). The residual one-way door is Window #2's adopt — gated by the Block-4 count glance, stated below.
-->

# 04P Adoption — Operator Mini-Package v2 (persist-verified)

**GOAL:** adopt the SNZB-04P as `binary_sensor/contact` → **D1 [M] 5/5** → capture the BENCH-CONST 6/6 values. **DONE-WHEN:** `device_adopted` for `0x449FDAFFFE688F57` · `~/bench.sh entities` shows exactly **6** rows all AVAILABLE · a door open/close produces a contact `state_reported` · the Block-6 capture pasted.

**The one hazard that remains, stated plainly:** adoption is still a one-way door (no un-adopt). The guard is now the **persisted** learn: Window #1 verifies the learn is ON DISK before you list the 04P; Window #2's boot must show **`learned_zonetypes_rehydrated: count=1`** before you press anything. Two ⛔ STOP conditions below — either one fires, you stop and paste; nothing is lost by stopping.

**Benign/expected lines (do not treat as failures):** `key_establishment_failed device=0xFFFFFFFFFFFFFFFF status=TC_REQUESTER_VERIFY_KEY_TIMEOUT` (the wildcard transient join key self-expiring) · `device_proposed` firing fast in Window #1 (the 04P is NOT listed — a proposal alone adopts nothing) · `position` advancing past 18946 at adoption (registry events append BY DESIGN — record the final value, don't read it as drift).

---

**Block 0 — deploy re-verify (Pi).** GOAL: the LEARN-PERSIST build is what's running. DONE-WHEN: `git log -1` shows the SHA from your LEARN-PERSIST push output AND the build succeeds.
```
cd ~/homesynapse-core && git pull && git log -1 --format="%h %s"
./gradlew :app:homesynapse-app:installDist
```
Expect: the pushed LEARN-PERSIST SHA · `BUILD SUCCESSFUL`. ⏺ RECORD the SHA.

**Block 1 — window key ON + first boot (Pi).** GOAL: permit-join active on the new build; the new boot instrument visible. DONE-WHEN: `RADIO UP` · `learned_zonetypes_rehydrated: count=0` (first boot on this build — 0 is HONEST, the instrument exists) · `projection_live: devices=5 entities=5 position=18946` · `permit_join_opened: duration=254s`.
```
~/bench.sh stop
grep -qE '^[[:space:]]*permit_join_duration:' ~/hs-bench/config/integrations/zigbee.yaml || echo "permit_join_duration: 254" >> ~/hs-bench/config/integrations/zigbee.yaml
cat ~/hs-bench/config/integrations/zigbee.yaml
~/bench.sh start
LOG=$(~/bench.sh log); grep -E "learned_zonetypes_rehydrated|projection_live|permit_join_opened|network_resumed" "$LOG"
```
The `cat` read-back must show the key ACTIVE (not commented) and `adopt_devices` = 5 entries with the 04P still `# HELD`. ⏺ RECORD the four glance lines.

**Block 2 — Window #1: learn + PERSIST-verify (Pi). The first ⛔ gate.** GOAL: the learn fires AND lands on disk. ONE physical act: **one long-press on the 04P (~5 s, release on LED), then HANDS OFF.** Do NOT open the door in this block. DONE-WHEN, in the log (fast propose is fine — the 04P is not listed):
```
LOG=$(~/bench.sh log); grep -E "device_announce|device_proposed|key_established|ias_zone_type_learned|ias_zone_enrolled" "$LOG" | grep -i "449FDA\|SNZB-04P"
```
Expect `ias_zone_type_learned: device=0x449FDAFFFE688F57 zoneType=CONTACT`. Then stop the bench (the shutdown flush persists the learn regardless of the 30 s debounce) and verify ON DISK:
```
~/bench.sh stop
grep -A4 '"learnedZoneTypes"' ~/hs-bench/data/zigbee/zigbee-devices.json
```
DONE-WHEN: the section shows `"0x449FDAFFFE688F57" : 21` (21 = the CONTACT zone-type id 0x0015). **⛔ STOP-CONDITION 1: the section or the entry is ABSENT after the stop ⇒ do NOT proceed to Block 3 — ⏺ paste everything either way and stop.**

**Block 3 — accept-list the 04P (Pi; bench stays STOPPED).** GOAL: the 04P listed for the restart Window #2 requires. DONE-WHEN: the `cat` shows **6** `adopt_devices` entries (the 04P line active) and the permit key still active.
```
nano ~/hs-bench/config/integrations/zigbee.yaml    # add under adopt_devices:   - "0x449FDAFFFE688F57"    # SNZB-04P contact
cat ~/hs-bench/config/integrations/zigbee.yaml
```

**Block 4 — Window #2: the rehydrate glance, then the adopt (Pi). The second ⛔ gate.** GOAL: the persisted learn is IN the map before anything proposes. Start the bench; BEFORE touching the device, the boot glance:
```
~/bench.sh start
LOG=$(~/bench.sh log); grep -E "learned_zonetypes_rehydrated|projection_live|permit_join_opened" "$LOG"
```
DONE-WHEN: **`learned_zonetypes_rehydrated: count=1`** + `projection_live … devices=5 entities=5 position=18946` + the window open. **⛔ STOP-CONDITION 2: count=0 or the line absent ⇒ do NOT press anything — ⏺ paste and stop (a press here would adopt MOTION durably).** On count=1: **one long-press re-pair, HANDS OFF.** Expected arc: `device_announce` → `device_proposed` (fast — now SAFE) → `proposal_accepted source=config` → **`device_adopted`** for `0x449FDAFFFE688F57`. ⏺ RECORD the arc lines with timestamps.

**Block 5 — the D1 read (Pi).** GOAL: the contact class live. DONE-WHEN: 6 entities all AVAILABLE, and one door open→close produces contact state changes.
```
~/bench.sh entities
```
Expect exactly **6** rows. Then open the door (or separate the magnet) once, wait ~5 s, close it; note the clock on each act:
```
LOG=$(~/bench.sh log); grep -E "state_reported|449FDA" "$LOG" | tail -8
```
⏺ RECORD: the 6-row entities JSON + the state lines + your act clock times.

**Block 6 — the BENCH-CONST capture (Pi) — the 6/6 re-mint inputs, read AT the instrument.** ⏺ paste ALL of:
```
LOG=$(~/bench.sh log)
grep "registry.projection_live" "$LOG" | tail -1
grep "zigbee.network_resumed" "$LOG" | tail -1
~/bench.sh entities
```
Expect `devices=6 entities=6 position=<RECORD THIS — it will exceed 18946 by design>` · `channel=20 panId=0x774c` · the new 04P deviceId/entityId ULIDs in the entities read.

**Block 7 — close-down (Pi).** GOAL: standing posture, window shut. DONE-WHEN: `permit_join_opened` count 0 on the fresh boot · `projection_live devices=6 entities=6` at the SAME position as Block 6's read · `learned_zonetypes_rehydrated: count=1` · 6/6 AVAILABLE.
```
~/bench.sh stop
sed -i '/^[[:space:]]*permit_join_duration:/d' ~/hs-bench/config/integrations/zigbee.yaml
cat ~/hs-bench/config/integrations/zigbee.yaml
~/bench.sh start
LOG=$(~/bench.sh log); grep -cE "permit_join_opened" "$LOG"; grep -E "learned_zonetypes_rehydrated|projection_live" "$LOG"
~/bench.sh entities
```
⏺ final paste, either way. The hub authors the BENCH-CONST re-mint from Block 6's values; boot-health goes GREEN on its landing.

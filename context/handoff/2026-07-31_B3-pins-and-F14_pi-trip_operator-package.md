<!--
file: context/handoff/2026-07-31_B3-pins-and-F14_pi-trip_operator-package.md
purpose: THE ONE PI TRIP, packaged launchable — the B3 ⛔PIN P-blocks (P-1..P-4, copied VERBATIM from the B3 return §2, which remains the record) + the F-14 v3 discriminating reads (the Hue powerSource + the Hue availability-event history). Read-only end to end: no writes, no restarts, no installs. ~7 minutes.
audience: Nick (hands, over `ssh pi`) — optionally relayed by a fresh Cowork NAVIGATOR lane (paste-collection ONLY; the navigator writes NOTHING, improvises NOTHING, and runs NOTHING itself — the 3.1 stray-store lesson; every block below is complete as-is).
returns: ⏺ EVERY paste goes back to the PM hub session (v42), either way — a paste that looks like failure is still instrument data. The hub mints the ⛔PINs + adjudicates F-14 from these pastes.
anti-actions (the whole trip): do NOT run the §9 install half yet (it follows the pin mint + the hub's go) · do NOT restart the app · do NOT edit any config · ONE interactive `ssh pi` session (never `ssh pi '<cmd>'` — the TTY rule).
status: ISSUED v42 beat 6. Consumed when all five ⏺ sets are pasted to the hub.
-->

# THE PI TRIP — B3 pins (P-1..P-4) + F-14 v3 (read-only, ~7 min)

**GOAL:** four pastes mint the B3 ⛔PINs (quiesce carrier · automations route · scheduler branch · the I5 boot slice) and two more settle F-14's last open branch. **DONE-WHEN:** five ⏺ sets pasted back to the hub, either way.

## Block 1 of 5 — P-1: which file carries bench-hero (⛔PIN-1)

```bash
# Pi terminal (read-only)
# GOAL: find WHICH config file carries the bench-hero automation. PIN-1
#       discriminates quiesce branch A (its OWN file -> mv-swap) vs
#       B (a section of a shared file -> generated-variant swap).
# DONE-WHEN: both listings printed; the grep names at least one file.
ls -la ~/hs-bench/config/
grep -l "bench-hero" ~/hs-bench/config/*
# Park-dependency premise check (P2 survey, same paste): bench-hero must
# command ONLY the Hue — the expected output of the next line is EMPTY:
grep -n "01KXW1W1SBJZERC9MBAMV2DWKE" ~/hs-bench/config/*
# ⏺ RECORD: paste ALL output either way. An EMPTY last grep is the
#   healthy answer (zero S31 references in config).
```

Only if the `grep -l "bench-hero"` line printed nothing:

```bash
# Pi terminal (read-only) — P-1 fallback, only if the grep above was empty
grep -ril "hero" ~/hs-bench/config/
```

## Block 2 of 5 — P-2: the automations-list instrument (⛔PIN-2)

```bash
# Pi terminal (read-only; app running)
# GOAL: measure the automations-list read the nightly's quiesce
#       ABSENT/PRESENT asserts will bind (route + the name field + the
#       exact served name of bench-hero).
# DONE-WHEN: one JSON body printed. Expect >= 1 row; expect a name field.
curl -s -m 15 -H "Authorization: Bearer $(cat ~/hs-bench/config/initial_api_token)" http://127.0.0.1:7070/api/v1/automations
echo
# ⏺ RECORD: paste the FULL body either way. A 401/404: paste it and stop —
#   route/token adjudication is the hub's.
```

## Block 3 of 5 — P-3: scheduler branch (⛔PIN-3)

```bash
# Pi terminal (read-only)
# GOAL: discriminate the scheduler branch (systemd user timer = REC; else cron).
# DONE-WHEN: both commands answered — output OR a clean error, both count.
systemctl --user list-timers
loginctl show-user $USER --property=Linger
# ⏺ RECORD: paste both either way. "0 timers listed" is a VALID systemd
#   answer (=> REC branch). "Linger=no" is fine (the install block enables
#   it). "Failed to connect to bus" on the first command => the cron branch.
```

## Block 4 of 5 — P-4: the boot-log slice (⛔PIN-4; feeds the ratified triple fixture re-mint)

```bash
# Pi terminal (read-only)
# GOAL: capture the CURRENT 6-device-era boot slice (the I5 boot-demo
#       fixture re-mint material — all THREE fixtures derive from it, OBS-3 ratified).
# DONE-WHEN: ~60 lines printed, reaching past the device_relinked runs.
LOG=$(~/nexsys-bench/tools/bench.sh log)
echo "slice of: $LOG"
head -60 "$LOG"
# ⏺ RECORD: paste ALL output either way. Expected tokens inside:
#   registry.projection_live: devices=6 entities=6 position=25065 ·
#   zigbee.network_resumed: channel=20 panId=0x774c · device_relinked x6 ·
#   zigbee.port_identity_captured ... pinnedOnly=false.
# If projection_live shows anything OTHER than devices=6 entities=6
#   position=25065: paste and STOP — the fleet moved; the re-mint waits on
#   hub adjudication.
```

## Block 5 of 5 — F-14 v3: the last two discriminating reads (WU-AVAIL-SEED branch pick)

```bash
# Pi terminal (read-only, ~30 s)
# GOAL: (a) the Hue's cached powerSource — mains (1 or 2) => the ping arm
#       failed to conclude during the 07-29 tracked boot (a second defect
#       leg); anything else (0/absent) => N-5 conservatism + the seed gap
#       explains EVERYTHING (no ping-arm defect proven).
#       (b) the Hue's full availability-event history — expect ONLINE-class
#       events only, none after 07-29 (confirming no offline ever published).
F=/home/homesynapse/hs-bench/data/zigbee/zigbee-devices.json
python3 -m json.tool "$F" | grep -n -i "modelIdentifier\|powerSource\|lastKnownAvailability"
sqlite3 ~/hs-bench/data/homesynapse-events.db "SELECT global_position, datetime(ingest_time/1000000,'unixepoch') AS t_utc, event_type FROM events WHERE event_type='availability_changed' AND hex(subject_ref)='019F436512399150182B3E59DB17100F' ORDER BY global_position;"
# (that hex = the Hue entity 01KX1PA4HSJ581GASYB7DHE40F as BLOB(16),
#  computed + timestamp-sanity-checked by the hub)
# ⏺ RECORD: paste BOTH either way. If the grep prints no powerSource lines
#   at all, that IS the answer (never captured => the 0/orElse path).
#   ZERO rows from the query is also decisive (no Hue availability event
#   has EVER published) — paste and stop.
```

**That's the trip.** Paste all five ⏺ sets to the hub. Afterward (separate, on the hub's go): the pin mint lands as a one-file bench follow-up commit, then the install half runs from the B3 return §9 (it ends with the night-1 park + timer enable).

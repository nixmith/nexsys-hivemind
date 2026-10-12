<!--
file: context/audits/2026-10-12_v109-b4_COMPARATOR-1_intake_two-layer_audit.md
purpose: The hub's two-layer intake of COMPARATOR-1's return (`research/2026-10-12_COMPARATOR-1_availability-record-and-automation-tracing_return.md`, 14,992 B) against its charter §7's pre-filed rules R1–R5.
audience: the hub · Nick
state-type: intake audit
status: FILED — v109 beat 4 (Mon 2026-10-12 ~15:5x CT; instrument 2026-10-12T20:50:46Z). Verdict: ACCEPT.
-->

# COMPARATOR-1 — the intake, two layers

## §0 Verdict
**ACCEPT.** The return answers its charter: eleven pre-registered claims adjudicated at pinned revisions (§0), both axes per incumbent (§1, §2), five safe sentences each backed by ≥ 2 sources (§3), the gaps named by product (§4), the sources with revision and lines (§5); 14,992 B under its 15 KB cap; `RETURNED` its last line. Its findings move one register row, add one, and narrow one hero claim.

## §1 Layer 1 — the claims, read (§0, §3 and §4 whole; §1–§2 by the table)
- **Availability:** claims 1–4 CONFIRMED with qualifiers. Zigbee2MQTT (off by default; a 10-min active timer; genBasic reads; state in memory; one `lastSeen` per device) and ZHA (7,200 s / 21,600 s; one Basic read per cycle; unavailable after two misses; state in memory; one `last_seen` in SQLite) store no structured, queryable probe outcomes; deCONZ CONFIRMED at source (`reachable` + `lastseen`, no history); Hubitat NOT FOUND. Where Home Assistant hosts ZHA, its recorder keeps each change to `unavailable` for 10 days by default.
- **Tracing:** Home Assistant keeps 5 traces per automation (T1, written at stop) and traces a run stopped by a failed condition (T2). T3 is REFUTED in part: since 2026.7.0 it keeps 5 "Did not trigger" traces for new-style numeric entity triggers that could not evaluate a change, while a change it evaluates and does not match leaves no trace. Home Assistant and Hubitat record a command as dispatched, not the device's confirmation (S5).
- **§4:** SmartThings' check interval and history retention, deCONZ's core node-failure rule, Hubitat's logs API, openHAB's REST rule status — NOT FOUND or NOT READ, each named.
- **License lines:** none met (0 mentions). COMMERCIAL-1 §3 stays unpinned.

## §2 Layer 2 — re-executed by the hub
1. **R1** — one sampled claim per axis re-fetched at its pinned revision: (a) availability — `Koenkk/zigbee2mqtt@344b6e03b436 lib/extension/availability.ts`: the class's timers, last-published availabilities, ping backoffs, paused devices and debouncers are in-memory `Map`/`Set` fields — S1's "in memory" holds (the 10-min default sits in `settings.ts`, not re-fetched — disclosed); (b) tracing — `home-assistant/core@adb4367 homeassistant/components/trace/const.py`: `DEFAULT_STORED_TRACES = 5 # Stored traces per script or automation` — S3's "5 most recent" holds.
2. **R2** — the language-law words over §3 (`superior`, `first`, `only`, `better`, `best`): 0.
3. **R3** — the §2 table: eight columns on every row.
4. **R4** — 14,992 B ≤ 15 KB; the last line `RETURNED <path> 14992`.
5. **R5** — the register, by the hub: IR-138's cell carries S1–S2; IR-184 (new) carries S3–S5.

**Not re-executed (disclosed):** the other source lines; the docs pages (Zigbee2MQTT, Home Assistant, SmartThings, Hubitat); the 2026.7.0 tag's "Did not trigger" code.

## §3 What it changes
- **The availability record (IR-138's AVAIL-SHAPE candidate):** "in the sources checked, no incumbent stores probe outcomes as structured, queryable records" may be drafted for the claim register at that scope, with Home Assistant's 10-day transition record named beside it.
- **The hero (IR-184):** "why didn't it fire" is not a field-wide gap — Home Assistant records it in bounded cases; "did it actually confirm" is where the sources show dispatch, not confirmation. B-1's copy and the claim register's hero rows are cut at that scope, under the language law (MISSING, never SUPERIOR).
- **COMMERCIAL-1 §3:** unpinned; its four market questions stay pre-registered; a license read is its own lane, not this week.

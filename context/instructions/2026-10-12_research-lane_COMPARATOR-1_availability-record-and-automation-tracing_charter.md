<!--
file: context/instructions/2026-10-12_research-lane_COMPARATOR-1_availability-record-and-automation-tracing_charter.md
purpose: COMPARATOR-1 — the research lane that re-checks the comparator pre-read (the plan forward §7: Z2M · ZHA · SmartThings · deCONZ · Hubitat on device availability — the silence timers, the asking, the record) at the sources' CURRENT revisions, and ADDS the second axis the explainability hero stands on — automation tracing (does the incumbent record WHY an automation fired, why it did not, and whether the action confirmed; where; for how long; queryable how). Its output is the claim register's safe wording, never a boast: the language law — the deterministic floor is MISSING from the field, not SUPERIOR — and every sentence that survives is one a competitor's engineer would sign. Monday's Cowork lane; no rig; the research path-domain (outside D4's core domains); its return CAPPED at Monday (D-v106-21 (4)) — if it runs past Monday it PAUSES before Tuesday's three lanes (the cap is not raised).
audience: the COMPARATOR-1 lane (a fresh Cowork conversation; web access; the research form of D-v102-23) · the hub (the intake; the claim register; COMMERCIAL-1's market section) · Nick (the §8 line)
state-type: research charter (one lane; a read, no code)
status: DISPATCH-READY — cut v107 beat 4 (Sun 2026-10-11 ~18:3x CT; instrument 2026-10-11T23:31:18Z). Flips to EXECUTED at the hub's intake.
-->

# COMPARATOR-1 — the availability record and automation tracing, against the field

## §0 The lane contract (every line binds)
- `date -u` first; CT = UTC − 5, derived once. You fetch PRIMARY sources only (the project's documentation and source code at a pinned revision — a commit sha or a dated page; a forum post or a blog is a lead, never a source). Every claim in your return carries its source and the revision it was read at; a claim you cannot pin is written as NOT FOUND, never as absent in the product.
- **The language law binds your every sentence:** the deterministic floor is MISSING from the field, not SUPERIOR; no "first", no "only", no "better". Where an incumbent HAS the thing (a stored, queryable record), you say so plainly and name its bounds (how many, how long, where stored, how queried) — that is the finding the claim register needs most. Name-light: `{{NAME}}` for our product; the incumbents by their names.
- **The one deliverable:** `nexsys-hivemind/context/research/<your CT date>_COMPARATOR-1_availability-record-and-automation-tracing_return.md` — §0 the verdict table (≤ 2 KB: each pre-registered claim → CONFIRMED / REFUTED / NOT FOUND, with the revision) · §1 the availability axis per incumbent · §2 the automation-tracing axis per incumbent · §3 the safe wording — three to five sentences the claim register can carry, each with the sources that back it · §4 what you could not find, by product · §5 the sources (URL + revision + the lines read). **Cap ≤ 15 KB — a ceiling.** Your last line, in the file and printed: `RETURNED <path> <bytes>`. **The time cap: Monday Oct 12.** If the hour passes 21:00 CT Monday with rows unread, you write the return with those rows as NOT READ (never guessed) and stop; the hub decides whether a second sitting exists.
- Write nothing else anywhere; no code; no repo is touched; no card is run.

## §1 The pre-registrations (the hub's; from the plan forward §7 — you adjudicate each at the source's current revision)
1. **Z2M** `availability.active.timeout` default 10 min is a SILENCE timer — a device heard within it is not pinged; past it, a `genBasic` read tried twice ≈ 3 s apart; online/offline published retained on change; passive devices 1,500 min, never pinged; **the feature is OFF by default.** (`zigbee2mqtt.io/guide/configuration/device-availability.html`; `lib/extension/availability.ts` at the current `master` sha — pin it.)
2. **ZHA** `consider_unavailable_mains` 7,200 s (battery 21,600 s); a 30–45 s check loop; past the threshold one Basic `manufacturer` read per cycle; unavailable after 2 missed. (`zha/application/const.py`, `zha/zigbee/device.py` at the current `dev` sha.)
3. **The record:** Z2M and ZHA keep availability IN MEMORY (Z2M logs failed pings at warning level) — no stored, queryable per-probe history; SmartThings exposes ONLINE/UNHEALTHY/OFFLINE + `lastUpdatedDate` (the Device Health docs) — a state, not a history; deCONZ and Hubitat NOT FOUND in the pre-read — find or confirm NOT FOUND.
4. **The wording that survived the pre-read:** "no structured, queryable per-probe history in the sources checked" — re-check it; if any incumbent stores probe outcomes durably and exposes them, the wording changes and you say exactly how.

## §2 The second axis — automation tracing (NEW; the hero's ground)
The explainability hero asks three questions of an automation: why did it fire · why didn't it · did it actually confirm. For each incumbent, read and pin:
- **Home Assistant** — automation TRACES exist (`trace` integration; `stored_traces` per automation, default 5; the trace holds the trigger, the condition path, each action's result; viewable in the UI; persisted under `.storage/trace.saved_traces`). Pin: the default count, the retention (restart? days?), whether a trace is queryable by API, whether it records a NON-firing (a trigger that fired but a condition failed IS traced — confirm; a trigger that never fired is not), and whether an action's device-level CONFIRMATION (the state actually changed) is recorded or only the service call's dispatch. This is the closest thing in the field to what `{{NAME}}` does; write its bounds exactly.
- **Zigbee2MQTT** — no automation engine (automations live in HA/Node-RED); say so; Node-RED's debug/flow context is a lead, not a stored record — check whether any first-party record exists.
- **SmartThings** — Rules API / Routines: is there a per-execution history exposed (the app's "History" shows device events; is an automation's execution and its reasons recorded?); pin what the developer docs say.
- **Hubitat** — Rule Machine logging (the app's logs; retention; whether a rule's evaluation path is stored); pin the docs.
- **deCONZ / Phoscon** — rules in the REST API; any execution record? Pin or NOT FOUND.
- **openHAB** — rules' logs / the event bus persistence (persistence services store item states, not rule evaluations?) — pin.
For each: WHERE the record lives (memory · a file · a database), HOW LONG it is kept, HOW it is read (UI only · REST · a query language), and WHETHER it names the cause of a non-firing. The honest column headings in your §2 table: product · fires-why recorded? · didn't-fire-why recorded? · confirmed? · where · retention · read how · source + revision.

## §3 The safe wording (what the claim register needs)
Three to five sentences, each true of every source you read, each one a competitor's engineer would sign — in the form "In the sources checked, X keeps Y in memory for Z; the record `{{NAME}}` writes is …" — never comparative adjectives. If Home Assistant's traces satisfy "a stored, queryable record of why an automation fired", the sentence says so and names where `{{NAME}}`'s differs in KIND (an event-sourced record every projection reads; the non-firing recorded as a first-class event; the confirmation from the device's own report) rather than in degree.

## §4 Out of scope
Any product recommendation; pricing; the hosted tiers and licenses of the incumbents (COMMERCIAL-1's lane asks that separately — if a license line is in front of you while reading, note it in §4 with its source and move on); our own code (the hub cites it).

## §5 What to watch out for
Documentation that describes an option as if it were a default (Z2M's availability is opt-in); a fork's docs read as the project's (ZHA lives in the `zigpy/zha` repo since 2024, not in HA core's `homeassistant/components/zha` alone — pin which you read); a "history" that is the DEVICE's event history, not the automation's; your own wish for the finding — a claim that `{{NAME}}` is alone is REFUTED by one counter-example, and finding that counter-example is the lane's success, not its failure.

## §6 Success criterion (binary)
Every §1 claim adjudicated at a pinned revision; the §2 table filled for HA, Z2M, SmartThings, Hubitat (deCONZ and openHAB may be NOT FOUND with the pages tried named); §3's sentences each backed by ≥ 2 sources; the return at the named path with its `RETURNED` line; nothing written anywhere else.

## §7 The hub's audit rules (pre-filed)
R1 every URL in §5 fetched by the hub for two sampled claims (one per axis) at the pinned revision · R2 the language law: `grep -c -i 'superior\|first\|only\|better\|best'` over §3 = 0 (the words may appear in quoted source text only) · R3 the §2 table's eight columns present per product · R4 the cap and the `RETURNED` line · R5 the register's claim rows (IR-138's AVAIL-SHAPE candidate; the hero's "why didn't it fire") updated by the hub from §3, never by the lane.

## §8 The dispatch (Nick pastes into a FRESH Cowork conversation with `ClaudeFolder` connected, Monday Oct 12, any hour; the lane runs beside dry-run #1 — a read, no rig)
```
You are the COMPARATOR-1 research lane (the research form of D-v102-23; web access; no code, no repo). Read nexsys-hivemind/context/instructions/2026-10-12_research-lane_COMPARATOR-1_availability-record-and-automation-tracing_charter.md WHOLE, then nexsys-hivemind/context/planning/2026-10-10_v103_THE-ROAD-FROM-CARRIER-F_plan-forward.md §7 (the pre-read you re-check). Execute §0 exactly: date -u first; primary sources only, each pinned to a revision; the language law in every sentence; the §1 claims adjudicated, the §2 table filled, the §3 sentences written; the return at nexsys-hivemind/context/research/<CT date>_COMPARATOR-1_availability-record-and-automation-tracing_return.md (≤ 15 KB), its last line RETURNED <path> <bytes>; the time cap Monday 21:00 CT — rows unread are NOT READ, never guessed.
```
Say back to the hub: `COMPARATOR-1: running`, then `COMPARATOR-1: RETURNED <path> <bytes>`.

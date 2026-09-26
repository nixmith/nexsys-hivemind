<!--
file: context/audits/2026-09-25_v80-b4_CLOSE_audit.md
purpose: THE v80 CLOSE (beat 4) — the Friday night's facts at the bytes (T4 · T5 · T6 · T4b; the aborted run; G4-2 UNAVAILABLE; `CHAR: sat-am`), Nick's word on the process ("too many steps, too much that can go wrong; the meter readings are barely changing"), the hub's own accounting of what went wrong, THE SIMPLER WAY as ruled, and what v81 opens on.
audience: the v81 hub (its first read after §1) · Nick (§0) · the skills pass (the two lessons)
state-type: audit (the close)
status: FILED v80 beat 4 (Fri 2026-09-25 ~22:4x CT; instrument 2026-09-26T03:40:57Z).
-->

# v80 — THE CLOSE (beat 4, Fri 2026-09-25 night)

## §0 Card
**The window's ONE deliverable — rehearsal 1's packet — is NOT cut.** The window closes at beat 4 on Nick's word, on a clean record, with v81's text cut around THE SIMPLER WAY. What the window did land: the three metering plugs adopted (9/9); the bench re-minted from the capture (T4 `a45686f`; T4b `df4a2d7`); boot-health PASS on 9/9 and the `power_w` wire path pinned; 7a intaken; VERIFY-72H's and rehearsal 1's inputs digested with cites; the horizon's inputs digested; the premise on the name corrected; the plan §26–§27; IR-54..56; two lessons. What it cost: Nick's Friday evening at the rig, 20:00 → 23:00 CT, on seven-step blocks and three re-plans.

## §1 The night at the bytes
- **T4:** `a45686f` pushed; the Pi's pull; `md5 d9eb0efd5f96`. **T6:** `[PASS] boot-health — 6/6 positive · 0 forbidden` (the suite restarted the app: `network_resumed` 22:06:56 EDT); `CMP-IDENTICAL`; the TR3's state `{"attributes":{"current_a":0.0,"energy_wh":0.0,"power_w":{"value":0.0},"voltage_v":{"value":128.3},"on":{"value":false}},"availability":"AVAILABLE"…"meta":{"timestamp":"2026-09-26T02:06:56Z"}}` → the wire path `data.attributes.power_w.value` CONFIRMED; the relays OFF; the API stamp beside the log's `22:06:56` → the Pi's wall-clock is UTC−4 (the erratum ruled).
- **`CHAR: tonight-40w`** → T4b `df4a2d7` (`load_w 40`; `band_pct 3.65`; `band_pct_tr3 3.53`; the derivations in the comments; the pre-edit bytes at `_scratch/v80/constants.pre-T4b.yaml`); the Pi at `185460d1c9e1`; the runner banner `@ df4a2d7`, the note "The load is 40 W".
- **The aborted run:** an Enter passed CHAR-BEFORE's confirm; `tare_watts_g4_1 =` refused every non-number (the runner's "never coerced, never a silent zero" held); Ctrl-c at 22:43 EDT (`KeyboardInterrupt` in `print_operator_block`, engine.py :1309); no bundle of record (the aborted run's bundle, if any, is `bundles/metering-known-load-2026-09-26T02…` — v81 lists and names it).
- **G4-2 UNAVAILABLE** at 22:59 EDT (`"availability":"UNAVAILABLE"`; voltage_v 124.87 stale) while G4-1 read AVAILABLE (126.34 V) — after boot-health's restart at 22:06. The TR3 AVAILABLE at 22:06. IR-56's class, now twice observed (the T2 restart; the boot-health restart).
- **The meters at the wall tonight** (Nick's reads): Kill A Watt 41.7 ± 0.2 W; SURAIELEC 44.1 W (upstream of the lamp through the cord) → B1 = A + ≈2.4 W; earlier B2 = 42.0 vs A 41.7. The tungsten load is steady to the meters' flicker: three readings carry it (the lesson).
- **The tmux session** `metering` on the Pi: a `watch` may be running in window 0; harmless; v81's first card kills the session.

## §2 What went wrong, in the hub's own lane
1. The Half-2 card's T7 was cut without the hub having read the scenario's operator prompts (they were read only when Nick stood at the CHAR-BEFORE prompt) — the card named tmux windows and a watcher, and assumed a three-meter chain and two lamps the rig could not provide. THE PREMISE GATE applies to a card's affordances as it applies to a claim.
2. Three re-plans in chat while Nick was at the rig (the one-cord chain; the two-window form; the seven-step "get it done" block) — each a wall of text at 22:00–23:00 CT. THE OPERATOR-LOAD LAW's "one act" became one message of twenty acts.
3. The CHAR's design (~20 readings ×2 passes ×2 brackets, 5-minute settles) is over-built for a steady tungsten load; Nick saw it at the meter before the hub did.
4. The Gen4-membership class was known from T2 and not read before T7 was handed; the operator's own second read found it.

## §3 THE SIMPLER WAY (ruled; D-v80-17; the v81 text; pm-lessons ×2)
Five acts and one line per rig card · the prompts read and the affordances asked before the card · three readings on a steady load, two-minute settles · no re-plan at the rig (a surprise is a STOP-and-close) · the availability read first · one card window + one meter-reader window; tmux one window, as a safety net only · no rig hours after 21:00 CT. METER-2 re-cuts the scenario to the rig: the two-pass one-cord chain, three pairs per pass, the relay read from the api, the LOAD STEP as the lamp, the 80 W wording gone.

## §4 Not re-executed (disclosed)
Nick's meter reads (his word); the aborted run's bundle directory (unlisted from here); the tmux session's state; the Gen4 web pages' states. The census of the close card at `-uall` inside the splice.

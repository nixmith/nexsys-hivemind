<!--
file: context/audits/2026-09-26_CHAR-sitting-1_return.md
purpose: the CHAR sitting's part-1 return, written by the guide session (a dedicated Cowork conversation) at 15:2x CT and filed VERBATIM below the marker (9,136 B; the last line is its own RETURNED line). Intaken at v81 beat 3 (`context/audits/2026-09-26_v81-b3_CHAR-sitting-1_intake_two-layer-audit.md`).
status: FILED v81 beat 3 (Sat 2026-09-26 ~15:4x CT; instrument 2026-09-26T20:44:20Z).
-->
<!-- VERBATIM FROM HERE -->
SITTING: STOPPED at card 4 (card 2's CHAR-BEFORE found not taken) · verdict none (the run is live, paused at `tare_watts_tr3 =`, entry 8 of 22) · bundle none (written only at the run's close)

## §1 The lines
CARD1: tmux killed · pi f1c2f9a · G4-1 AVAILABLE on=False W=0.0 · TR3 AVAILABLE on=False W=0.0 · G4-2 AVAILABLE on=False W=0.0
CARD2: not said — CHAR-BEFORE was confirmed with ENTER (before 14:07) without the B1/B2 passes; Nick's words at 15:18 in §2
CARD3: G4-1 tare 1.4 · offset 0.0 · V 122.7/122.7 · rep 42.5:WITHIN 42.4:OUTSIDE 42.4:WITHIN — assembled by the guide from the scenario's own echo lines (Nick's pastes and screenshots, 14:27–15:09); not said back by Nick
CARD4: not reached — the prompt on screen at the stop is `tare_watts_tr3 =`
CARD5: not reached
CARD6: not reached
CARD7: not reached

## §2 Odd, as Nick said it (CT, verbatim)
- 09:51 "ELI5: what are tares? what do you mean "on the sheet", etc., that way there is 0 ambiguity for me."
- 14:02 "So just to clarify, what should `tare_watts_g4_1` setup look like for the reading?"
- 14:07 "I have wall -> A -> cord -> lamp off. Reading is 0.0, do I type that out now? Then what?"
- 14:14 "I am genuinely so overwhelmed and confused with directions... now apparently you don't mean what you meant... now apparently there's extra steps for each step? I am so lost."
- 14:14 "I current have the lamp (off, and this is kind of important to specify, given how many variables there are at any given time) and plugged into the G4-1 device, which is at the end of the extension cord"
- 14:14 "There is a 0.5W reading now, again with lamp off, just the G4-1 in, and when I first plugged that G4-1 and it lit up, the Kill A Watt jumped to 0.7W then back down to 0.5W when the light stopped."
- 14:14 "this card and the language and everything else changing as we go along, is realllllly making this way more difficult."
- 14:22 "W1 = lamp on and in the extension cord in A. Reading is 41.1 W" · "W2 = W1 but with G4-1 in the middle of lamp and extension cord. Reading is 42.5 W" · "W2 - W1 = 1.4 W"
- 14:27 "I am still very confused as to what we are doing now, and the instructions make zero sense to me, contextually."
- 14:27 "the 30s reading thing is totally unnecessary. Every meter we have worked with so far, changed in like 2 seconds, max, and is pretty steady for our workloads."
- 14:31 "The lamp is unplugged from the G4-1, which is switched on and "drawing power", and reads 1.3 W on A."
- 14:42 "a_volts_g4_1_1 = 122.7 +/- 0.2 V" · "a_volts_g4_1_2 = 122.7 +/- 0.2 V"
- 15:01 "A is reading 42.3-42.4W."
- 15:06 "A is reading the same as last (fluctuating between 42.3-42.4 W steadily)."
- 15:14 "Instructions unclear on what I need to do."
- 15:18 "Yes, those are real readings. No, I do not think we did a full pass to record full sets of results."
- 15:22 "From there, we will probably continue working on testing/benching and getting readings."

## §3 The clock (CT; message times, and the scenario's own typed-at stamps at UTC−5)
- 09:21 the paste · 09:51 the last message of the morning · no messages 09:51–14:02
- CARD1 — before the paste (card1.txt written 09:14)
- CARD2 — no line; CHAR-BEFORE's ENTER fell before 14:07 (its instant is not on record here)
- CARD3 — no line; the seven entries typed 14:24:14 · 14:34:09 · 14:46:18 · 14:46:40 · 14:53:50 · 15:02:00 · 15:07:15
- CARD4–CARD7 — none
- 15:22 the stop, on Nick's word; his rig hours end 21:00

## §4 The guide's notes (past the packet's 6 KB cap on Nick's word, 15:22: "You need to be as thorough as possible.")

### 4.1 The run, for the next card
- Live in tmux `metering` on the Pi at `tare_watts_tr3 =`. Entries 1–7 (G4-1) are bound in memory; 15 remain (TR3 ×7 · G4-2 ×7 · char_after_readings).
- engine.py at f1c2f9a writes the bundle only at the run's close (`bundles.write_bundle` after `run_evidence`; no signal handling). Ctrl-C, or card 1's `tmux kill-session -t metering`, discards G4-1's entries; only finishing the run keeps them.
- `a_watts_g4_1_r2` is recorded OUTSIDE under `on_outside: record`, so the close FAILs naming `positive[1] a_watts_g4_1_r2` whatever follows.
- The pair count at `char_after_readings` ("twelve if every reading was taken") will be under 12: CHAR-BEFORE holds no full pass.
- The rig as left: wall → A → cord → G4-1 (relay on at the api, 15:06) → lamp, lit; A on watts; TR3 and G4-2 in their wall sockets (not re-read since card 1); B1 and B2 on the desk.

### 4.2 G4-1 as the scenario printed it
REP a_watts_g4_1_r1 — power_w=42.0 − 0.0 = 42.0 vs A=42.5 − 1.4 = 41.1 → r=1.021898 |r−1|=2.190 % vs 3.65 % → WITHIN
REP a_watts_g4_1_r2 — power_w=43.0 − 0.0 = 43.0 vs A=42.4 − 1.4 = 41.0 → r=1.048780 |r−1|=4.878 % vs 3.65 % → OUTSIDE
REP a_watts_g4_1_r3 — power_w=42.0 − 0.0 = 42.0 vs A=42.4 − 1.4 = 41.0 → r=1.024390 |r−1|=2.439 % vs 3.65 % → WITHIN
- TARE 1.4 = W2 42.5 (lamp through G4-1, relay on) − W1 41.1 (lamp lit straight in the cord, no plug).
- OFFSET 0.0 from window B at 14:32, lamp out, relay on: power_w 0.0 · current_a 0.0 · on true · voltage_v 124.52 · energy_wh 10.0.
- Volts 122.7 / 122.7, typed 22 s apart; A's display wobbled ±0.2 V.
- Window B just before each rep was typed: r1 power_w 42.0 (current_a 0.34 · voltage_v 124.06 · energy_wh 25.005); r2 42.0 (0.341 · 124.15 · 30.007), then the engine's read after ENTER took 43.0; r3 42.0 (0.34 · 124.01 · 35.009).
- The Gen4 reports power in whole watts (constants: 0x0B04 div=1, "power 1 W"), so a ≈42.4 W load reads 42 or 43. At r2 A flickered 42.3–42.4; the guide's rule was to type the value on the display at the moment of reading, never one chosen by outcome. 42.3 would also have read OUTSIDE (43.0 / 40.9 → 5.13 %).
- G4-1's own draw read straight off A: 0.5 W at 14:14 (G4-1 in the chain, lamp dark; 0.7 W while its light was on at power-up) and 1.3 W at 14:31 (relay on, no lamp). The TARE by difference was 1.4.
- G4-1's voltage_v read 124.01–124.52 while A read 122.7.

### 4.3 Departures from the cards
1. Card 2: CHAR-BEFORE was confirmed with ENTER without the B1/B2 passes; no CARD2 line exists.
2. Card 3, act 1: G4-1 went into the chain (the lamp into G4-1, lamp dark) before W1. A read 0.0 at 14:07 (lamp off, straight in the cord) and 0.5 W at 14:14. W1 was then retaken with G4-1 out and the lamp lit.
3. Card 3, act 1: the relay's api read before W2 was not done; the first api read (14:32, at the OFFSET) showed on true.
4. The 30 s settles: not confirmed observed; Nick judged them unnecessary (§2, 14:27).
5. Pacing: from 14:14 the guide gave one action per message with one line back (Nick at 14:27: "We will get this done, one at a time"), not the packet's one card at a time.
6. The guide's own error: its card-2 glossary (09:51) defined "tare" as a lamp-out reading. The plug TARE is by difference at the lit load. This seeded the 14:07 lamp-off 0.0; the guide corrected it in its replies at 14:07 and 14:14.
7. The volts were read at 14:42 but not typed; they were typed at 14:46, after a screenshot check caught it.

### 4.4 Checked at the paste (the guide's first reply, at the bytes in ClaudeFolder)
- The paste = `_scratch/v81/2026-09-26_CHAR-sitting_operator-session-prompt.md` (LF-normalized sha256 7f24bd13…), and card1.txt = the CARD1 line.
- Cards 2–6 are byte-identical to `2026-09-26_v81_CHAR-sitting_seven-cards.md`. Card 7 is not: act 2 keeps only the no-1b branch and adds "a `1` is a surprise"; act 3 turns "only on your word `S31: back-in-at-close`" into "your word by silence". Nick was told; he has said nothing on the S31 since.
- f1c2f9a = the METER-2 commit (the local nexsys-bench HEAD, clean). The scenario's prompt order = the packet's. The ULIDs = constants `metering.plug-entity`. metering-plug and command-api are available: true; bands 3.65 / 3.53; load 40 W.
- The bundle stamp is `%Y%m%dT%H%M%SZ`, so card 7's `awk -F:` and `tail -1` are sound; `bundle-CHAR` does not exist yet. The 240-byte state read shows power_w and on (Thursday's T6 captures, and live today). BENCH-CORE-3 says it runs after this datum is banked (it restarts the core).
- constants `provenance:` declares one ULID (the S31's command entity), hence the runner's "provenance: 1 declared ULID(s)". The metering block's comment says the plug entities would be declared there; they are not.

### 4.5 Incident
The guide's `git status` in the local nexsys-bench left an empty `.git/index.lock` (09:24:57 CT; the sandbox blocks unlink). It was deleted minutes later with Nick's permission, and the repo is clean at f1c2f9a. Deletion stays enabled for ClaudeFolder in the guide's session; it has not been used since.

### 4.6 Also seen
- The Pi's tmux clock read 15:46 when the volts were typed at 19:46:40Z (UTC−4), while the desk runs CT (UTC−5); the scenario's stamps are UTC.
- What held at the rig after 14:14: one action per message, one line back, the exact command inline, the expected screen named ("the screen should end in …"), and one meaning per word.

RETURNED _scratch/v81/sat0926/CHAR-sitting_return.md 9136

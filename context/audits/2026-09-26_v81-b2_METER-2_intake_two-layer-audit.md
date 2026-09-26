<!--
file: context/audits/2026-09-26_v81-b2_METER-2_intake_two-layer-audit.md
purpose: THE v81 BEAT-2 AUDIT — METER-2's return intaken two-layer (the lane's claims read; the hub's own re-execution at the bytes: the selftest, the diffs, the engine's substitution, the evidence asserts), its deviations ruled, the hub's own guarded comment edit added to the same bench card, the seven cards cut from the re-cut prompts, what was not re-executed.
audience: the v81 hub · Nick (the verdict line) · the next bench lane (the pattern: a test pins its own inputs)
state-type: audit (beat 2, lane intake)
status: FILED — v81 beat 2 (Sat 2026-09-26 ~09:1x CT; instrument 2026-09-26T14:16:30Z).
-->

# v81 beat 2 — METER-2 intaken; the seven cards cut

## §0 Card
**Verdict: ACCEPT.** The return exists at `context/audits/2026-09-26_METER-2_return.md` (8,149 B; last line `RETURNED … 8149`; 149 B over an 8,000-B cap, inside 8 KiB — noted, not a finding). The bench working tree carries exactly the two files the charter allowed (` M scenarios/metering-known-load.yaml` · ` M tools/runner/test_engine.py`; the index empty). The hub's own run of `python3 -B tools/runner/test_engine.py` on the device: `selftest: 36 check(s), 0 failure(s)` (it read `1 failure(s)` at `df4a2d7`, D-v81-5). The four deviations ACCEPTED (§2). The hub added one guarded edit to the same card (§3). The bench card (2 = 2 M) in Nick's hands; the Pi pulls the sha in card 1.

## §1 Layer 2 — re-executed at the bytes
- The selftest, twice (after the lane; after the hub's comment edit): 36 / 0 both times.
- `git diff tools/runner/test_engine.py`: nine `+` lines — the check's name now reads "ids, flags and the charter's bands overridden in memory"; a four-line comment; `constants["metering"]["band_pct"] = 3.03` · `["band_pct_tr3"] = 4.03` · `["load_w"] = 80` placed after the plug-id loop and before `unmet_requirements` / `substitute` (the order that makes the pin take effect — `engine.substitute` runs on the dict AFTER the override).
- `git diff scenarios/metering-known-load.yaml`: 36 `+` lines carrying `act:` / `prompt:` / `goal:` / `note:`; the CHAR-BEFORE act now the two-pass one-cord chain with 30 s tares, two minutes and three pairs; the TARE prompts name the move into the cord's end and the api relay read ("if OFF, press its button and read again until `on: true`"); the OFFSET prompts "relay ON (as read at the api)"; the REP prompts "LAMP out of <PLUG> for at least 15 s, then back in" (no dashboard); the REP goals `band ${C.metering.band_pct} %` / `${C.metering.band_pct_tr3} %`; CHAR-AFTER the two passes and the count "from BOTH halves of the bracket (twelve if every reading was taken)". Two dated header notes after :28 and :76.
- `engine.substitute` (engine.py :209–:230) recurses into every dict value, so `goal:` strings interpolate as `note:` already did — the lane's choice (interpolate, not drop) is sound.
- `char_after_readings` is bound by no `evidence:` assert (grep: only `${let.tare_watts_*}`, `${let.plug_offset_w_*}`, `${let.a_watts_*}` are referenced) — the count is a receipt, so "twelve" changes no verdict.
- The grep census on the scenario after the edits: `80 W` 3 (:16 · :26 the record; :78 the new note) · `two 40` 1 (:15) · `3.03` 2 · `4.03` 1 (the record's comments) · `~20` 1 (:17) · `photo` 0 · `dashboard` 2 (:29 the note "no dashboard toggle"; :40 the format record) — nothing below `stimulus:` carries any of them.
- BM1b T4 (the let list of 22 in order; the per-plug asserts; `requires:`) green in both runs — the structure is untouched, as the charter required.

## §2 Deviations ruled
1. The nine REP `note:` strings changed ("the dashboard's power_w" → "the meter-reader window's power_w") — ACCEPT: the charter's §1 removed the dashboard; a note that still named it would contradict the prompt beside it. 2. The T3 comment on four physical lines — ACCEPT (the file's 79-column form). 3. A second scratch script for the test edit — ACCEPT (two guarded scripts, two files). 4. CHAR-AFTER's note unchanged — ACCEPT (it carried no "~20").

## §3 The hub's own guarded edit, on the same card
Ten comment lines: the nine `field: "data.attributes.power_w.value"   # WIRE PIN PENDING` → `# the wire pin CONFIRMED at T6, 2026-09-25 (the TR3 state read; v80 b4)` and the header row :70 `# - WIRE PIN PENDING:` → `# - WIRE PIN CONFIRMED at T6 (2026-09-25; v80 b4; was PENDING):`. The pin was confirmed at v80 b4 on the TR3's state JSON (`T6.txt`); the comments were stale against the record. Counts asserted (9 and 1) before the write; `WIRE PIN PENDING` 0 after; the selftest 36 / 0 after. No assert changed. The scenario 25,294 → 25,813 B.

## §4 The seven cards (`context/instructions/2026-09-26_v81_CHAR-sitting_seven-cards.md`, 9,717 B; D-v81-7's shape)
Cut FROM the re-cut prompts and Nick's three words: card 1 the desk (the stray tmux session, the Pi's `git pull --ff-only`, the availability ×3 as ONE line built on the Pi — `bash -s` over ssh with a quoted heredoc; the inner script `bash -n` clean and the JSON one-liner exercised on a fixture) · card 1b only on UNAVAILABLE (T1b.sh's window + the plug's "Start pairing" + the read again; the window closes at card 7 by T3.sh) · card 2 CHAR-BEFORE (the scenario in one tmux window; two passes; ENTER) · cards 3–5 one plug each, four acts (TARE · OFFSET · volts ×2 · REP ×3 as one repeated act) · card 6 CHAR-AFTER + the verdict + detach · card 7 the desk (the bundle home; the window key by T3.sh or the `grep -c` 0; the S31 back in on Nick's word; one line). Every card sets its own `S=` / `D=`; the ULIDs are printed in the file's header and inside every command that needs one.

## §5 Not re-executed (disclosed)
Any command against the Pi (the pull, the state reads, the scenario) — card 1 is the first; the lane's `lint ok` (the hub ran the selftest, which lints the real file in T3/T4); the return's §1 table beyond the diff lines quoted above.

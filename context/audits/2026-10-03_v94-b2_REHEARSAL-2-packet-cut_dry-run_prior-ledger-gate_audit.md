<!--
file: context/audits/2026-10-03_v94-b2_REHEARSAL-2-packet-cut_dry-run_prior-ledger-gate_audit.md
purpose: The cut of REHEARSAL 2's packet (v94 beat 2; THE ONE DELIVERABLE) — the reads it rests on, the prior-ledger greps (law #31), the dry run on the desk (THE VALIDATOR AT THE CUT · THE BYTE-MARK WATCH · the loops RUN on the corpus), the three defects the dry run caught, and the hub's readings and disclosures; with it, the two corrections Nick made at 07:22 CT and the hub's own third (D-v94-11..13).
audience: the v94 hub · the v96 hub (rehearsal 2's intake reads §3's P-rows against the return) · any session the DR §3b sends here
state-type: audit (filed; never edited)
status: FILED Sat 2026-10-03 ~07:5x CT (instrument 2026-10-03T12:54:05Z)
-->

# v94 beat 2 — REHEARSAL 2's packet: the cut, the dry run, the gate (Sat 2026-10-03)

## §0 Verdict
CUT and DISPATCH-READY: `context/instructions/2026-10-03_REHEARSAL-2_sensor-join_restart-under-loads_IR-56-power-cycle_operator-session-prompt.md` (24.8 KB; five cards; one instrument each; ≤ 3 parts; P1–P8). The dry run on the desk PASSED after three defects it caught were fixed before the write (`_scratch/v94/b2/reh2_dry-run.txt`, 63 lines). Three corrections entered the record first: the TR3's load (Nick, 07:22), the `re-seen` mechanism (Nick, 07:22 — the hub's arc-1 miss at b1), and IR-56's row (the hub's own, from the BC6b audit). The guide's paste is the file whole, at 17:25 CT; the sitting 17:30 → ≤ 21:00.

## §1 The reads (the grounding agent's report, `ae0f4b…`, re-executed by the hub where marked ✓)
- The 1b packet's form (`…REHEARSAL-1b…operator-session-prompt.md`, 33,690 B): Blocks A–E; cards as numbered actions with DO · RIG · SAY · EXPECT; the guide paragraph `:9`; the return form `:11` (≤ 8 KB; §0 P-rows HELD/REFUTED/NOT-REACHED; §1 every SAY; §2 his words; §3 departures; §4 files; `RETURNED <path> <bytes>`).
- SENSOR-REJOIN-1's Part 2 form = `_scratch/v93/sensor/hub-amendment_part2.md` (6,081 B): MARK2/MAXW2 printed by the window block; `permit-join 254 "REJOIN SNZB06P24"`; the act (USB re-seat; `REPLUG:`); `hd2.sh` the watch on the mark; `hd3.sh` the +300 s reads. ✓ the hub read `hd2.sh`/`hd3.sh` (801 B / 1,085 B) — card 1 carries their text with the slot names renamed MARK1/MAXW1 and the window reason re-cut.
- The validator: `tools/bench.sh:91–95` `pj_valid` — `secs_re='^[1-9][0-9]{0,2}$'` ≤ 254, `reason_re='^[A-Za-z0-9 ._:/-]{1,120}$'` under LC_ALL=C; `:101–102` validates before any network; the desk form of record `_scratch/v92/b5/v92b5_splice.py:28`. ✓ re-run in the dry run §3 line 1.
- The bench verbs (`tools/bench.sh:4`): `start|stop|restart|status|health|log|entities|runs|events|state <ulid>|api_token|digest [N]|permit-join <1-254> "<reason>"`; `restart` = `do_stop; do_start` (nohup; a NEW `bench-<ts>.log` and `ln -sf` to `current.log`, `:43–46`) — a mark taken before a restart is void after it; card 3's mark is taken on BOOT2. ✓ `ln -sf` at `:46`.
- The ids: `scenarios/constants.yaml:78–90` (the entity ULIDs); the IEEEs from the BENCH-CORE audits (G4-1 `0xACEBE6FFFEF733DC` · TR3 `0x4CE175B4C0700000` · G4-2 `0xACEBE6FFFEF25A2C`; the sensor `0xA4C13814CE41FFFF`). ✓ dry run §3 lines 2–3.
- `re-seen`'s source ✓ (the hub, before the agent): `tools/runner/nightly_digest.py:151–172` `fleet_from_reads(prior_ids, now_ids)` → `len(now), len(now & prior)`; the docstring: "the announcement-based split … is the LOG's instrument, not this one". The `.after-rejoin` log `:37` ✓: `12:49:02.172 … zigbee.device_relinked: device=0xA4C13814CE41FFFF … re-pairing, no new adoption`.
- IR-52 ✓ (the register `:…`): "two more reads at +30 s and +120 s, recorded beside the first, never asserted" — a runner change; OR-S31-INTERMITTENT `pm-handoff.md:69–72` names it as instrument (2).
- IR-56 ✓: the register's tail (D-v85-12, the restart read); the BC6b intake audit `:30` — "P4 sample 5 … INVERSE — samples 1–5 clean on app restarts; IR-56's Java unit not queued; the next instrument a plug power-cycle at rehearsal 2".
- THE RESTORE RUNS BEFORE THE GAP (pm-lessons `:397–398`) and the 1b close block `:167–192` (the restore as an action; the carrier compared `IDENTICAL`; the logs copied home).
- "dual-port" ✓: in no file under `context/` by grep; the record had `TR3: phone charger (variable)` and "its USB-C to his phone" (the v92 DR `:67`, D-v92-29). The two-port fact enters on Nick's word of 07:22.

## §2 The prior-ledger greps (law #31) — every reused string and witness, with its hit
| Reused | From | The ledger's hit | Carried as |
|---|---|---|---|
| the byte-mark watch loop (`tail -c +$((M+1))`, SEL, 24 × 5 s) | hub-amendment_part2 / `hd2.sh` | the guide's note `:42`: the card's own 1c/2b loops grepped the whole log and would break on the :37 relink at i=1 | card 1c/3c take MARK before the act; the dry run shows MARK=0 → i=1 and MARK=EOF → 24 (§3) |
| `MAXW` slot | the card's Part 3b | the note `:43`: the slot had NO value | MARK1/MAXW1 printed by 1a; the guide fills them; 3c's MARK3 printed by 3a |
| the window BEFORE the act | the note `:55` | the class's pairing cycle ≈ 180 s after power-on | 1a opens 254 s, 1b re-seats AT ONCE |
| `permit-join <n> "<reason>"` | BC7 Part D | the usage line on U+2014 in the reason (pm-lessons `:410`; IR-116) | `"REH2 SNZB06P24 join"` through the regex (§3 line 1); zero non-ASCII in any code block (§3 line 10) |
| the STOP clauses | BC7 b5 `:32` | two text slips: `043007 keyfail=1` (the Pi read 0) and `proposed ≠ 0 → STOP` (the adoption's own line) | `keyfail-new` and `proposed-new` are RECORDED, never a STOP; STOPs name only `network_formed ≠ 0`, the fence (`clone ≠ 5b0e20c`), a usage line or `exit ≠ 0`, and a state the card does not name |
| the plugs' read (`for pair in G4-1:… TR3:… G4-2:…`) | BENCH-CORE-3 `:63`; BC6b `:30` | samples 1–5 clean on app restarts | card 2a/2c carry it with `avail/stale/on/W/lastReported`; the S31 and the sensor added |
| the re-announce gesture | pm-lessons `:403–405`; the 1b intake d4 | the Shelly's three presses re-announce; a SNZB's 5-s hold is a LEAVE | 1b is the USB re-seat only; the packet says "never press or hold the button" |
| a restart after a window | the 1b intake d3/d4 | a restart under the 1b KEY re-opened a window | PJ-2's key is dead (`permit_join_key_ignored`); card 2 expects `permit=0` on BOOT2 |
| configs live through the nightly | the 1b intake d5/f5 | the 03:30 nightly ran on edited configs | no edit tonight; card 4 is a CHECK (`key-lines=0 · warn-lines=0`, the carrier md5 = card 0's) |
| the logs' eviction | the 1b intake d6 | the 4-newest window evicted Thursday's logs | card 4 copies BOOT1 and BOOT2 home before the return |
| `position` vs the store head; the wrong end of a page; a token the log never carries | IR-93 (REHEARSAL 1 `:46`) | three harvest defects | every harvest token counted on the corpus (§3 line 7); `permit_join_closed` (0 in the corpus) confirmed at source (6 files, `PermitJoinClosed.java`) |

## §3 The dry run on the desk (`_scratch/v94/b2/reh2_dry-run.txt`; the script `reh2_dry-run.sh`)
1. `pj_valid` on every `permit-join` in the packet: `VALID 254 'REH2 SNZB06P24 join'`. 2. Every ULID in a code block is 26 Crockford chars AND in `constants.yaml`: 5/5 KNOWN. 3. Every IEEE in the record: 4/4 (9–29 files each). 4. `bash -n` on every heredoc body and every outer line with the slots filled: 9 heredocs OK, outers OK. 5. The 1c loop on the corpus, sleeps removed: `MARK=0 → broke at i=1 · new-sensor-lines=1` (the :37 relink — the whole-log defect reproduced); `MARK=176487 → broke at i=24 · new-sensor-lines=0`. 6. The 3c loop for G4-1: `MARK=0 → i=1 · 48 lines`; `MARK=EOF → i=18 · 0`; the sleep arithmetic 115 / 30. 7. The harvest tokens on the corpus: `launched=1 projection_live=1 formed=0 resumed=1 relinked=11 sensor-relinked=1 opened=1 closed=0 keyfail=1 summaries=470`; the `projection_live` line; four `link_summary` lines (the sensor's `frames=0 … last_link_at=-`). 8. The three python parsers on a JSON of the documented shape (SYNTHETIC — disclosed; the live shape is BENCH-CORE-3 `:63`'s, read at BC6b). 8b. `permit_join_closed` at source: 6 files. 9. The verbs `restart · state · api_token · permit-join` present; `ln -sf` at `:46`. 10. Non-ASCII in code blocks: 0.

## §4 The three defects the dry run caught (fixed before the write)
(a) The ULID check flagged `01M3Y4YA6KMH7JDEF5YMMJ3YND` — the sensor's DEVICE id in P2's prose, not a tool argument (constants lists ENTITY ids); the check was narrowed to code blocks. (b) `bash -n` failed on 1c's and 3c's outer lines at `M=<MARK1>` — a slot the guide fills; the dry run now fills the slots with a number before parsing. (c) Two `·` separators inside card 0's echo strings — harmless to bash, but the rule after BC7's U+2014 is zero non-ASCII in any code block; replaced by `|`.

## §5 The hub's readings and disclosures
- "The S31's two reads" (the dispatch's row) is READ as IR-52's +30 s / +120 s placements applied to the S31's STATE after the restart, RECORDED beside the plugs' reads and never asserted; no command is issued to the S31 (the s31 fence) — if the row meant command-driven reads, that is IR-52's runner change for the bench lane, not a rig act.
- Two hardware acts tonight (1b the sensor's USB re-seat; 3b G4-1's plug power-cycle), in series, ≥ 60 min apart; nothing touches the Hue, the S31's relay, the nightly or a config file.
- IR-56's sample 6 is on G4-1 (no load), never on the TR3 — a TR3 power-cycle would power-cycle the sensor.
- The sensor's join uses IR-117's finding (the class returns in pairing mode after a power loss) as the gesture; it is not a power-loss RE-TEST of a joined sensor.
- Not re-executed on the desk: the Pi (every command runs there tonight); the API's live JSON shape (synthetic in §3 line 8).
- The corrections, filed in the DR: D-v94-11 (the TR3 feeds a dual-port charger — the sensor steady ≈ 2–3 W + the phone variable-if-plugged; card 0 asks `PHONE:`), D-v94-12 (`re-seen` is a two-read registry intersection; the b1 mechanism REFUTED at `:37` and at source; IR-118's row re-cut by id; one lesson), D-v94-13 (IR-56's next instrument is the plug power-cycle; D-v94-9 reversed).

## §6 For Nick
The b2 card: `_scratch/v94/b2/card_b2.txt` (hivemind, 11; gated) → `HIVE: LANDED <sha>`. The packet is in your hands now; its paste is at 17:25 CT (the guide's fresh Cowork conversation, the file whole). Two words at card 0 tonight (`LED:` · `PHONE:`); one line back after card 4 (`RETURNED <path> <bytes>`).

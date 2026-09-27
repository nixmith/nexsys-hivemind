<!--
file: _scratch/v81/2026-09-27_BENCH-CORE-3_guide-notes.md
purpose: the BENCH-CORE-3 guide session's notes for the hub — everything the one line back cannot carry: per-block verdicts against the card's EXPECTED lines, the observations that were NOT stops but that the hub should weigh, one guide error (no effect on the Pi or the record), and what this card did not verify. The record itself is 2026-09-26_BENCH-CORE-3_outputs.txt (untouched by this file).
audience: the v81 hub (intakes with the outputs file) · Nick
state-type: guide notes (a sitting's return)
status: EXECUTED — Sun 2026-09-27 13:09:06Z → 13:21:25Z (08:09–08:21 CT); card followed block-for-block, no re-plan, no improvised fix, nothing deleted, nothing restored, `~/bench.sh stop` never run.
-->

# BENCH-CORE-3 — guide notes (Sun 2026-09-27)

## The one line back
`BENCH-CORE-3: deployed d22a8a4 · boot-health 6/6 · rows 343493→344143 · relinked 9 · plugs A/A/A`

## The record
- `_scratch/v81/2026-09-26_BENCH-CORE-3_outputs.txt` — 19636 B · 183 lines · sha256 65f97e60a3b866e8… (read back from disk after Block 4; matches Nick's pastes block-for-block)
- sections, in order: B0 13:09:06Z · B0b 13:11:57Z · B1 13:13:59Z · B2 13:15:38Z · B2-poll 13:17:25Z · B3 13:18:16Z · B4 13:21:25Z
- no `network_formed`, no `error`/`fatal` line anywhere in the file
- the card as pasted: `context/instructions/2026-09-26_bench-card_BENCH-CORE-3_core-to-d22a8a4_installDist_operator-session-prompt.md` (status line: Block 0b added v81 beat 5; "Runs SUNDAY MORNING first")

## Per-block verdicts against EXPECTED
| block | verdict | the values |
|---|---|---|
| B0 | match; no STOP condition | hs-dev-1 · clone 13d439f (AUTO-ID-1) · porcelain=0 · behind=2 ahead=0 · node v22.23.1 npm 10.9.8 · openjdk 21.0.11 · 98G free · running pid 28123 on bench-2026-09-27-043129.log (projection_live devices=9 entities=9 position=201201) · DB /home/homesynapse/hs-bench/data/homesynapse-events.db · **ROWS-before 343493** · integrity ok · timer NEXT **Mon** 2026-09-28 04:30 EDT, LAST Sun 04:30 EDT 4h39m ago (see obs. 1) |
| B0b | match; no STOP condition | zigbee.yaml 571 B sha256 513b2c0171b84d50 key-lines=0 · bench-2026-09-27-043007/043029/043129.log all permit_join_opened=0 device_join=0 device_announce=0 · nightly `2026-09-27 quiesced AUTO floor: 8/9 PASS · 1 SKIP(hue-online) · fleet: 9/9 · re-seen 9 · bench-hero RESTORED ✓ · ON-latency 0.35s` · REP-1 rows: see obs. 8 · entity rows 66722 (MIN 2026-09-26 01:52:21, MAX 2026-09-27 13:11:55) — not 0, no re-cut |
| B1 | match; no error line | BACKUP=/home/homesynapse/hs-backup/20260927T131359Z · config/ (mtime Sep 27 04:31) · homesynapse-events.db 168452096 B · install-tree-old/ (the 13d439f tree, mtime Jul 6) · backup rows 343827 (= before + 334 over ~4.9 min, the live fleet) |
| B2 | match; no STOP condition | clone: d22a8a4 `fix(persistence,lifecycle): IR-40 + IR-44 — the time-range read planne…` · BUILD pid=28900 · tail of the pull: `create mode` LinkReadIT.java, EzspIncomingMessageTest.java (see obs. 3) |
| B2-poll | match | build-20260927T131539Z.log · BUILD SUCCESSFUL in 28s · 60 actionable tasks: 12 executed, 48 up-to-date · launcher mtime 09:16:06 Pi-local (13:16:06Z) |
| B3 | match on every item; no STOP condition | stopped → launched pid 29118 → bench-2026-09-27-091824.log → RADIO UP after 15s · [PASS] boot-health — 6/6 positive · 0 forbidden · bundle boot-health-20260927T131921Z · network_resumed: channel=20 panId=0x774c · **formed=0 resumed=1 relinked=9 adopted=0 config_issue=0 cache_loaded: 9** · **ROWS-after 344143** · integrity ok · registry rows=9 (the API listed all 9 ULIDs incl. G4-1 …ZEX2G, TR3 …PK2XA, G4-2 …SBJVS) · deployed=d22a8a4 · automation-lines=3 |
| B4 | A/A/A — no card 1b | PLUGS · G4-1 AVAILABLE on=False W=0.0 · TR3 AVAILABLE on=True W=0.0 · G4-2 AVAILABLE on=False W=0.0 · 5 relink lines at 09:19:13 incl. all three plugs' devices (0xACEBE6FFFEF733DC G4-1, 0x4CE175B4C0700000 TR3, 0xACEBE6FFFEF25A2C G4-2) |

## Observations for the hub (none was a STOP under the card's rules)
1. **Timing / the nightly.** The card's header pre-registered Sunday's 03:30 CT nightly as the first night on d22a8a4; its status line moved the run to Sunday morning. It ran 13:09–13:21Z Sunday, i.e. AFTER the 04:30 EDT nightly, which therefore ran on 13d439f (three boots 04:30:07 / 04:30:29 / 04:31:29 Pi-local; `fleet: 9/9 · re-seen 9`). **The first night on d22a8a4 is Mon 2026-09-28 04:30 EDT (03:30 CT).** B0's timer line (NEXT = Mon, EXPECTED said Sun) is this and nothing else; not on B0's STOP list.
2. **READS-1 preceded this card.** `_scratch/v81/sun0927/READS-1.txt` (the hub's own read at 12:30:15Z) carries the same B0b script; B0b at 13:11:57Z reproduced it line-for-line except the entity row count (65398 → 66722; MAX advanced to 13:11:55Z) — G4-2 was live-reporting between the two reads.
3. **"Fast-forward" is not visible in B2's output** — `git pull --ff-only 2>&1 | tail -2` keeps only the last two lines of the stat listing. Same in the BC-1/BC-2 record (v77). The fast-forward is established by: `--ff-only` + B0's `ahead=0 behind=2` + HEAD = exactly `d22a8a4` after the pull (a merge would be a different sha; a refusal would have left 13d439f).
4. **B2's `BUILD pid=28900 log=~/hs-bench/build-.log`** prints first and with an empty stamp: the `&&`-list is backgrounded as a whole, so `$S` is unset in the foreground echo and `$!` is the background list's pid, not gradle's. Cosmetic; identical at BC-1/BC-2; the poll found the real log `build-20260927T131539Z.log`.
5. **Guide error, no effect.** The guide's first paste of the B2-poll line carried a stray `</parameter>` token at its end; bash rejected the whole line with `syntax error near unexpected token 'newline'` BEFORE executing anything — no ssh, no tee. Verified on disk: the outputs file still ended at the B2 section (line 136, `clone: d22a8a4 …`). The clean line was re-issued and ran at 13:17:25Z. The record contains exactly one B2-poll section.
6. **Two boots inside B3.** The restart launched pid 29118 → `bench-2026-09-27-091824.log` (relinked ×9 at 09:18:31, network_resumed 09:18:38.977). The boot-health scenario then produced its own boot: relinked ×9 at 09:19:13 (B4's tail shows these), port_identity_captured 09:19:20.846, network_resumed 09:19:20.962, bundle 13:19:21Z. B3's `formed=0 resumed=1 relinked=9 …` counts are taken from `current.log` AFTER the scenario, i.e. the second boot's log — which is why resumed=1 although two network_resumed stamps appear in B3's output. Same shape at BC-1 (11:04:26 vs 11:05:07) and BC-2 (11:51:57 vs 11:52:37). Both boots are from the d22a8a4 install tree. The pid running now is NOT 29118 and was not read by this card.
7. **Plug switch states (B4).** All three AVAILABLE (the only thing the card evaluates). Recorded verbatim because the hub knows the CHAR sitting's intended end-state and the guide does not: G4-1 on=False W=0.0 · TR3 on=True W=0.0 · G4-2 on=False W=0.0. At 22:34Z Saturday G4-2 carried 42 W / 0.336 A, and its event stream was live at 13:11:55Z (voltage reports continue regardless of switch state, so this is not by itself a contradiction).
8. **REP-1 (from B0b).** 66 rows in 22:33:00–22:35:30Z, gp 284683 → 284802. power_w: 42 → 41.0 @22:34:08 (gp 284762/284763) → 13.0 @22:34:13 (284773/284774) → **0.0 @22:34:18 (284782 reported, 284783 changed)** → 42.0 @22:34:24 (284790/284791). current_a: 0.336 → 0.0 @22:34:16 (284776/284778), 0.0 @22:34:21 (284785) → 0.336 @22:34:26 (284794). Last row in the window: gp 284802 voltage_v 123.58 @22:34:31Z. So: yes, a state event carrying power_w 0.0 exists before 22:34:31Z — but it is NOT the last power_w value before the silence; the plug reported 42.0 W again six seconds later, then went quiet. Per-minute: 22:30 34 · 22:31 16 · 22:32 48 · 22:33 34 · 22:34 32 · **22:35–22:46 zero rows (12 min)** · **resume 22:47 (31)** · 22:48 36 · … · 23:09 27 — the resume minute 22:47Z sits inside the card's 22:44–22:47 re-plug band.
9. **Row counts.** before 343493 @13:09:07Z · backup 343827 @13:13:59Z (+334, ~68/min) · after 344143 @~13:19:40Z (+316, ~57/min). Consistent with live ingest from the fleet; ROWS-after ≥ ROWS-before holds.
10. **Artifacts on the Pi.** backup `/home/homesynapse/hs-backup/20260927T131359Z` · build log `~/hs-bench/build-20260927T131539Z.log` · boots `bench-2026-09-27-091824.log` + the scenario's · bundle `~/hs-bench/bundles/boot-health-20260927T131921Z` · `current.log` = the scenario's boot.

## What this card did not verify (for the hub's independent read)
- the pid actually running after boot-health's relaunch, and that its classpath is the new tree — the chain of evidence is installDist (launcher mtime 13:16:06Z) → `bench.sh restart` at 13:18:16Z → `deployed=d22a8a4` (git HEAD, not the JVM)
- the dashboard was NOT rebuilt (48 up-to-date; the npm step did not re-run) — if d22a8a4 carries web-ui changes the served bundle is whatever installDist considered up-to-date
- the plugs' switch states against the CHAR sitting's intended end-state (obs. 7)
- Monday 04:30 EDT is the first nightly on d22a8a4 (pre-registered `fleet: 9/9 · re-seen 9`; the S31 floor → `command-confirm-s31` PASS or a row)

## Card discipline
Six blocks run in order, one at a time; each output read against its EXPECTED line before "next"; no deviation from the command strings; no `--allow-downgrades`; no token printed; nothing deleted; no restore; `~/bench.sh stop` never run. The guide read the outputs file from disk after B0b and after B4 as its second check.

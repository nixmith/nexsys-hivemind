# GATE-2 return — the promise graded: IR-191's breakdown, the fitness bars, the amendment

## §0 The verdict
1. **DELIVERED — steps 1, 2, 3.** `nexsys-bench` branch `gate-2/evidence` off `6a40a10`; core `176adad` read-only; **zero commits** (HEAD `6a40a10`, `rev-list 6a40a10..HEAD` = 0). `date -u` 21:51:49Z (16:51 CT) → branch 21:54:36Z → BR-1 RED 22:09:24Z → breakdown RED 22:16:45Z, GREEN 22:16:50Z (again 22:23:26Z, BD-8 tightened) → FB RED 22:29:25Z, GREEN 22:31:13Z → staged 22:35:48Z. **`git write-tree` `7dc6041853131e9ac89e1b9023b8848e1b45c6e2`.**
2. **The store = the desk copy; the Pi untouched.** md5 `6dfd6e3c7441fb5a224b7ee666cc0d16` first (≈21:52Z, before any open) and last (22:36Z); 940,978,176 B, mtime 00:40:56Z unchanged; `file:…?mode=ro`, `uri=True` on every open.
3. **IR-191 — the 57 % is the Hue's.** 1,714 of 3,009 commands carry a `command_confirmation_timed_out`; **1,671 (97.5 %) are the Hue's** — 1,186 in its July dev weeks (W28–W29, while it still reported, sparsely), 485 after its reporting died. Its last report of any kind: **2026-07-19T00:49:15Z**; it has confirmed **0 of the 764** commands sent after it (728 in the dark regime from 07-20, T3b).
4. **The landed classifier on the 1,714** (`timeout_causes()`, called, never re-written): 1,694 on its timeout arm → **`bench` 501** (HUE 488 · S31 13) · **`device` 26** (all S31) · **`unattributed` 1,167** (all `no-expectation`: the Hue's level/colour — their why stays open, F3); the other 20 sit beside a failure result (the core reads FAILED first). **Not a failure rate:** 26 of 1,714 (1.5 %) are laid on a device.
5. **The confirmations are honest:** 185 CONFIRMED; 185/185 cite a real `state_reported` of the same subject + attribute whose value = `actual_value`; (iii) = 0. Two identify commands never terminated (07-14, 08-12).
6. **The S31:** 131 of 161 eligible on/off confirmed (81 %); **32/32 since 09-27**; the 22 FAIL bundles of the 59-bundle read map 22-for-22: `bench` 7 · `device` 13 · FAILED 2.
7. **The bars on both soak nights:** on/off 2/2 · level 0/3 (the Hue) · restarts 3 (the nightly) · probe-answered: no store instrument · 49.4 / 46.7 file-MB/day (baseline 47.9). **As landed (option c) both grade FLAGGED, by (viii).**
8. **Two premise corrections:** dry-run #1's window is **not in the copy** (`POS1b=1877415` > 1,876,566; opened 01:03:53Z, the copy ends 00:40:01Z); the probe-answered ratio **cannot** come from the copy (0 `probe_answered` rows).
9. **Step 3 staged:** an ADDITIVE `fitness` block in `grader.py` — measured, not graded, no bar set — FB-1…FB-5 red-first; GS-8 lifts it (one line, D4); the dry run on four `export.py` cuts reproduces §2's rows 1–4.
10. **Staged tree** (`checkout-index`, desk VM, Python 3.10.12): `breakdown selftest: 10 check(s), 0 failure(s)` · `verify72h selftest: 63 check(s), 0 failure(s)` · `selftest: 42 check(s), 0 failure(s)` · `selftest: 54 check(s), 0 failure(s)` · `bench.sh selftest: 42 check(s), 0 failure(s)`; `constants.yaml` `9b0af47b3376`; 25 mutants (12 + 13), each caught.

## §0b The premise table — re-run 21:52–21:54Z; all seven hold (the outputs as printed)
```
1  6a40a10
   0
2  131 / 136 / 540 / 814 / 973
3  150 / 152 / 153 / 155
4  **The cause of a timeout (GRADER-S31-1; IR-88, IR-51, IR-52)
   `verdict.json` → `timeout_causes` (and the report's **Time
   gives every command `classify()` reads UNCONFIRMED by its ti
5  (1876566, 1876566)
6  state_reported 1202395 · state_changed 631933 · automation_action_completed 14364 · automation_action_started 14364 · command_dispatched 3009 · command_issued 3009 · command_confirmation_timed_out 1714 · automation_completed 1596 · automation_triggered 1596 · command_result 1129 · availability_changed 481 · integration_started 346 · integration_stopped 317 · state_confirmed 185 · integration_restarted 28 · device_discovered 22 · integration_health_changed 18 · join_rejected 18 · device_adopted 10 · device_registered 10 · entity_registered 10 · permit_join_closed 6 · permit_join_opened 6   (23 types, Σ 1876566)
7  6dfd6e3c7441fb5a224b7ee666cc0d16
md5: 6dfd6e3c7441fb5a224b7ee666cc0d16  homesynapse-events-2026-10-12.db   (2.9 s, before any open)
```
Rows 5 and 7 ran on the VM's path `$HOME/mnt/backups/…` (D1).

## §1 Step 1 — IR-191's breakdown (`breakdown.py --db <copy> --out <dir>`, the whole copy, 7.4 s)
Stands on SQL_PARTITION 9,046 rows · SQL_STATES 23,647 (HUE + S31, the arm's two subjects) · SQL_REGISTRY 20 · SQL_REPORTS 84 · SQL_SPAN 1 (Appendix A). Names: entity → device → zigbee EUI64 → the bench's name (G4-1 `…F733DC`, G4-2 `…F25A2C`, TR3, S31, HUE).

### T1 — the partition (`build_commands` → `terminals()[0]` and `classify()`)
| row | count |
|---|---|
| command_issued | 3009 |
| first terminal: state_confirmed · timed_out · command_result (∉ {acknowledged}) | 185 · 1695 · 1127 |
| no terminal: open · edge-open | 2 · 0 |
| classify(): CONFIRMED · UNCONFIRMED · FAILED · DISPATCHED | 185 · 2255 · 25 · 544 |
| (iii) a state_confirmed beside a non-confirmed terminal | 0 |
| duplicate terminals (results excepted) · unplaced · carried in · opaque results | 0 · 0 · 0 · 0 |
| timed_out rows · attached · commands with one | 1714 · 1714 · 1714 |
| … on the classifier's timeout arm | 1694 |
| … beside a terminal the core reads first | FAILED 20 |

### T2 — the causes (the classifier's words) and the evidence beside them
| cause | count | by device |
|---|---|---|
| bench | 501 | HUE 488 · S31 13 |
| device | 26 | S31 26 |
| unattributed (no-expectation) | 1167 | HUE 1167 |
| unattributed (no-prior-value · opaque · not-dispatched · matched-in-window) | 0 · 0 · 0 · 0 | — |
| evidence: bench, prior ≤ 1 h · ≤ 24 h · > 24 h | 232 · 185 · 84 | HUE 220/184/84 · S31 12/1/0 |
| evidence: device, late report ≤ 30 s · > 30 s · none | 10 · 16 · 0 | S31 |

**The idempotent sends, named** (F26 = the classifier's `bench`; the payload's `idempotency_class: IDEMPOTENT`, on all 3,009, is the command's retry class — D11):
- **S31 13:** 07-29 23:19 off (prior 9 s) · 07-30 00:01 on (111 s) · 07-30 01:37 on (191 s) · 07-31 04:19 off (278 s) · 07-31 20:50 off (43 s) · 08-02 on (147 s) · 08-03 on (147 s) · 08-04 off (187 s) · 08-20 off (136 s) · **08-27 on (372 s) · 09-05 on (165 s) · 09-18 on (96 s)** — the 59-bundle read's three A-9 `on=true` nights, "96–372 s", to the second · 09-26 off (8.5 h).
- **HUE 488** (all `turn_on`): 404 in its reporting era 07-10…07-19 (prior ≤ 24 h) · **84 on a prior > 24 h**: 07-10 1 (its first days) · 07-20…08-01 48 · 10-02 35 (REHEARSAL-1b; prior 75 days) — 83 are the dark Hue's last July reading read as the held value (F2).

**The 26 `device`:** 11 in the 07-29…08-01 dev sessions — 10 matched 0.6–28.9 s after the 5-s window (late), 1 not within 25 h; 15 at the nightly (08-04 → 09-26) — no matching report before the next sitting (≥ 4.2 h). (`late` is the first match anywhere in the copy: T2's "> 30 s" 16 = those 15 + the 25-h one.) **The 22/59 reconciled:** each FAIL bundle → the S31 `turn_on` of that minute: `bench` 7 (07-30 ×2, 08-02, 08-03, 08-27, 09-05, 09-18) · `device` 13 · FAILED 2 (08-14, 08-15: `integration_unavailable`, the bundles' 8–9-ms class).

### T3 — device × command class
| device | class | issued | w/ timeout | CONF | bench | device | unattr | U:result | FAILED | superseded | open |
|---|---|---|---|---|---|---|---|---|---|---|---|
| G4-1 | on/off | 2 | 0 | 2 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| HUE | on/off | 488 | 488 | 0 | 488 | 0 | 0 | 0 | 0 | 0 | 0 |
| HUE | level | 801 | 718 | 6 | 0 | 0 | 709 | 0 | 9 | 77 | 0 |
| HUE | color | 976 | 465 | 46 | 0 | 0 | 458 | 0 | 8 | 464 | 0 |
| HUE | identify | 487 | 0 | 0 | 0 | 0 | 0 | 484 | 2 | 0 | 1 |
| S31 | on/off | 175 | 43 | 131 | 13 | 26 | 0 | 0 | 4 | 1 | 0 |
| S31 | identify | 80 | 0 | 0 | 0 | 0 | 0 | 77 | 2 | 0 | 1 |
| all | all | 3009 | 1714 | 185 | 501 | 26 | 1167 | 561 | 25 | 542 | 2 |

CONF = CONFIRMED · bench/device/unattr = UNCONFIRMED on the timeout arm, by cause (bench = the idempotent send: **unconfirmable by construction** when its prior is fresh — 417 of 501; 84 rest on a prior > 24 h, F2) · U:result = UNCONFIRMED by an `unconfirmed` result (Identify: ConfirmationPolicy DISABLED — also unconfirmable by construction) · superseded/open = DISPATCHED settled/not. The class is the payload's `command_type`; the copy holds no query-class command; TR3 and G4-2 were never commanded.

### T3b — device × regime (dark = derived: from 24 h after the device's last report)
| device | regime | issued | w/ timeout | CONF | bench | device | unattr | U:result | FAILED | superseded | open |
|---|---|---|---|---|---|---|---|---|---|---|---|
| G4-1 | on the air | 2 | 0 | 2 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| HUE | on the air | 2024 | 1186 | 52 | 405 | 0 | 774 | 401 | 9 | 382 | 1 |
| HUE | dark (no report since 2026-07-19) | 728 | 485 | 0 | 83 | 0 | 393 | 83 | 10 | 159 | 0 |
| S31 | on the air | 189 | 39 | 91 | 12 | 23 | 0 | 55 | 6 | 1 | 1 |
| S31 | off+unloaded (since 2026-09-20) | 66 | 4 | 40 | 1 | 3 | 0 | 22 | 0 | 0 | 0 |

### T4 — ISO week (UTC) × device, with the fleet and the regimes on the air
| wk | fleet | regimes | device | reports | issued | w/ timeout | CONF | bench | device | unattr | U:result | FAILED | superseded | open |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| W28 | 2 | — | HUE | 103 | 1456 | 865 | 17 | 292 | 0 | 570 | 290 | 4 | 283 | 0 |
| W29 | 5 | — | HUE | 84 | 568 | 321 | 35 | 113 | 0 | 204 | 111 | 5 | 99 | 1 |
| W30 | 6 | HD | HUE | 0 | 135 | 81 | 0 | 27 | 0 | 54 | 27 | 0 | 27 | 0 |
| W31 | 6 | HD | HUE | 0 | 126 | 78 | 0 | 21 | 0 | 56 | 21 | 2 | 26 | 0 |
| W31 | 6 | — | S31 | 1979 | 36 | 17 | 11 | 6 | 11 | 0 | 7 | 0 | 1 | 0 |
| W32 | 6 | HD | HUE | 0 | 32 | 24 | 0 | 0 | 0 | 24 | 0 | 0 | 8 | 0 |
| W32 | 6 | — | S31 | 2028 | 24 | 5 | 11 | 2 | 3 | 0 | 8 | 0 | 0 | 0 |
| W33 | 6 | HD | HUE | 0 | 28 | 23 | 0 | 0 | 0 | 15 | 0 | 8 | 5 | 0 |
| W33 | 6 | — | S31 | 1222 | 21 | 7 | 7 | 0 | 3 | 0 | 4 | 6 | 0 | 1 |
| W34 | 6 | HD | HUE | 0 | 28 | 21 | 0 | 0 | 0 | 21 | 0 | 0 | 7 | 0 |
| W34 | 6 | — | S31 | 2026 | 21 | 2 | 12 | 1 | 1 | 0 | 7 | 0 | 0 | 0 |
| W35 | 6 | HD | HUE | 0 | 28 | 21 | 0 | 0 | 0 | 21 | 0 | 0 | 7 | 0 |
| W35 | 6 | — | S31 | 1925 | 21 | 1 | 13 | 1 | 0 | 0 | 7 | 0 | 0 | 0 |
| W36 | 6 | HD | HUE | 0 | 28 | 21 | 0 | 0 | 0 | 21 | 0 | 0 | 7 | 0 |
| W36 | 6 | — | S31 | 1895 | 21 | 2 | 12 | 1 | 1 | 0 | 7 | 0 | 0 | 0 |
| W37 | 6 | HD | HUE | 0 | 28 | 21 | 0 | 0 | 0 | 21 | 0 | 0 | 7 | 0 |
| W37 | 6 | — | S31 | 2017 | 21 | 3 | 11 | 0 | 3 | 0 | 7 | 0 | 0 | 0 |
| W38 | 6 | HD | HUE | 0 | 32 | 24 | 0 | 0 | 0 | 24 | 0 | 0 | 8 | 0 |
| W38 | 6 | S0 | S31 | 2025 | 24 | 2 | 14 | 1 | 1 | 0 | 8 | 0 | 0 | 0 |
| W39 | 9 | HD | HUE | 0 | 28 | 21 | 0 | 0 | 0 | 21 | 0 | 0 | 7 | 0 |
| W39 | 9 | S0 | S31 | 1738 | 21 | 4 | 10 | 1 | 3 | 0 | 7 | 0 | 0 | 0 |
| W40 | 10 | R1 R1b R2 | G4-1 | 217614 | 2 | 0 | 2 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| W40 | 10 | HD R1 R1b R2 | HUE | 0 | 203 | 126 | 0 | 35 | 0 | 91 | 35 | 0 | 42 | 0 |
| W40 | 10 | S0 R1 R1b R2 | S31 | 2044 | 21 | 0 | 14 | 0 | 0 | 0 | 7 | 0 | 0 | 0 |
| W41 | 10 | HD SN1 SN2 R3 | HUE | 0 | 28 | 21 | 0 | 0 | 0 | 21 | 0 | 0 | 7 | 0 |
| W41 | 10 | S0 SN1 SN2 R3 | S31 | 2010 | 21 | 0 | 14 | 0 | 0 | 0 | 7 | 0 | 0 | 0 |
| W42 | 10 | HD | HUE | 0 | 4 | 3 | 0 | 0 | 0 | 3 | 0 | 0 | 1 | 0 |
| W42 | 10 | S0 | S31 | 306 | 3 | 0 | 2 | 0 | 0 | 0 | 1 | 0 | 0 | 0 |

HD = the Hue dark (derived) · S0 = the S31 OFF and unloaded since 09-20 ~15:42Z (pm-handoff OR-S31, v77 b7) · R1 = REHEARSAL-1 = EXPORT-1's window (09-28) · R1b (10-01/02) · R2 (10-04) · SN1 / SN2 = the soak nights (10-08, 10-11) · R3 = BC9 + REHEARSAL-3 (10-11). W42 is 24.7 h. `reports` = that device's `state_reported` rows that week, on weeks it was commanded (the S31's 2,245 reports of W29–W30, before its first command 07-29, sit outside T4: SQL_STATES' 23,647 = T4's 21,402 + 2,245). **Not a household:** dev sessions W28–W29 (the Hue) and 07-29…08-01 (the S31); from W32 the corpus is the nightly suite (≈ 4 HUE and 3 S31 commands a night) plus the sittings. Weeks with HD or S0 are not comparable to a week without them.
**The trend:** HUE — 52 of 2,024 confirmed while it reported (W28–W29); from W30, 0 reports and 0 confirmed: flat zero. S31 — 26 device-cause timeouts W31–W39, the last 09-26; 32/32 on/off since 09-27, OFF and unloaded throughout. G4-1 — 2/2, its only commands (R1).

### In plain words — what "did it actually confirm" can say today
1. **(T1)** It never calls a command confirmed without the device's own word: of 3,009 commands, 185 were confirmed — each backed by a matching report, none beside a timeout or failure — and 2,822 more are on record as not confirmed, each closed by a timeout or a result (two identify commands never closed).
2. **(T3)** The one relay commanded across the record confirms most of the time: the S31 confirmed 131 of the 161 on/off commands that could confirm (81 %); of the other 30, 26 went unanswered inside the 5-s window — 10 of them answered within 30 s after it — and 4 were refused (`integration_unavailable`).
3. **(T4)** When a device goes quiet the record does not claim success: the Hue has reported nothing since 2026-07-19T00:49Z, and none of the 764 commands sent to it since is confirmed — each is on record as unconfirmed, failed or superseded; the S31 has confirmed every on/off command since 09-27.

**It must NOT say:** "HomeSynapse confirms that your devices did what you asked." — it confirmed 185 of 3,009 (13 % of the 1,399 that could confirm); a dark device confirms nothing (0 of 764); a send the record shows already in force cannot confirm (501 — 84 of them on a reading over a day old); and `unconfirmed` cannot say whether the device acted (10 acted and reported late — F25/IR-195). The Hue's own reporting era confirmed 52 of 2,024 — the claim holds for no light on this record.

## §2 Step 2 — the candidate fitness bars (pre-registrations; **none adopted**)
| bar | the reading, ADDITIVE beside (i)–(viii), from the export alone | candidate threshold for N3 |
|---|---|---|
| B1 confirmed ratio | per command class: CONFIRMED / eligible; eligible = issued − bench − superseded − edge-open; identify never eligible | ≥ 0.95 per class with ≥ 1 eligible; null = not read |
| B2 restarts | `integration_started` + `integration_restarted` rows in the window | = 0 (the run's own boot precedes `from`) |
| B3 probe answered | store Σ answered / Σ (answered + missed) over `probe_answered`; log `ok` / all `zigbee.availability_ping` lines | ≥ 0.99 per mains device, both; null = CANNOT-GRADE |
| B4 store growth | rows/day × the export's bytes/row (the copy: 501.4); payload bytes/day beside | ≤ 60 MB/day (1.25 × 47.9) |

**The corpus numbers** — rows 1–4: an `export.py` cut of the copy graded by the amended grader (`fitness`), the same by SQL_BARS + `breakdown.py --from-utc/--to-utc`; row 5 by those two only (the 72-h cut's whole-second edge leaves out the copy's last 3 rows, 00:40:01.0–.146Z):
| window | rows | B1 on/off | B1 level | B2 restarts | B3 | B4 file-MB/day (payload) |
|---|---|---|---|---|---|---|
| SOAK-NIGHT-1 10-08 02:02:40→22:15:01Z (20.2 h) | 82,938 | 2/2 | 0/3 | 3 (08:30–08:32Z) | — | 49.4 (12.6) |
| SOAK-NIGHT-2 10-11 02:08:34→12:46:36Z (10.6 h) | 41,257 | 2/2 | 0/3 | 3 (08:30–08:33Z) | — | 46.7 (11.9) |
| EXPORT-1 = REHEARSAL-1 09-28 17:15→18:50Z | 6,953 | 2/2 (G4-1) | — | 1 (18:03Z) | — | 52.8 (13.5) |
| the copy's last 72 h (10-10 00:40:01→10-13 00:40:01Z) | 277,979 | 6/6 | 0/9 | 13 | — | 46.5 (11.8) |
| the copy's last 24 h (to 00:40:02Z; dry-run #1's eve) | 95,611 | 2/2 | 0/3 | 3 | — | 47.9 (12.2) |
| **dry-run #1's window** (10-13 01:03:53Z →) | **not in the copy** | | | | | |

B3 `—`: 0 `probe_answered` rows (AVAIL-API-1 deploys at BC10) and no app log on the desk; the record's only soak number is SOAK-NIGHT-2's log harvest (S2.txt: S31 510/510 `ok`), not re-read here.

**The options for N3 — what each would have done to the soak nights**
| option | SOAK-NIGHT-1 | SOAK-NIGHT-2 | what decides it |
|---|---|---|---|
| (a) gate the run on B1–B4 | FAIL | FAIL | B1 level 0/3 (the dark Hue) and B2 3 (the nightly's restarts) — facts the record already names, not the product; B3 CANNOT-GRADE before BC10 unless waived; B1 on/off and B4 pass |
| (b) measure and report; a red line holds the household installs | FLAGGED (as landed) + the readings | same | the red line's scope: on household-class devices (S31 2/2) with the nightly's restarts declared → not crossed; but nothing declares them today (F6), so a restart clause crosses it both nights — and counting the Hue crosses it too |
| (c) bookkeeping only (as landed) | FLAGGED — (viii): 36 bench-hero runs "completed with actions and no command"; (i)–(v) PASS; 3 timeouts, all `unattributed (no-expectation)` | FLAGGED — (viii): 28 runs; the same | the 57 % never appears; the cause block prints three lines a night |

## §3 Step 3 — the amendment, staged against `6a40a10`
`diff --cached --stat`: `breakdown.py | 1084 +` · `grader.py | 204 +` · `test_verify72h.py | 227 +-` · 3 files, 1514 insertions(+), 1 deletion(-) (GS-8's docstring line).
- `grader.py` +204/−0: docstring `:87–:91` · constants `:265–:291` (`FITNESS_CLASS` … `STORE_GROWTH_BASELINE_MB_PER_DAY = 47.9`; the probe line `ZigbeeIntegrationAdapter.java:884–:889`, tokens `:976–:977` @ `176adad`) · `grade()` `:788–:790` (`verdict["fitness"]`, after `timeout_causes`) · `ratio_of`/`fitness()`/`fitness_lines()` `:1135–:1301` · report.md `:1700–:1701` (`## Fitness — measured, not graded`). No invariant, verdict word, outcome, cause word or `constants.yaml` key moves.
- `test_verify72h.py` +226/−1: BR-1 and FB-1…FB-5 `:2711–:2921` (`PIN_6A40A10` `:2737`) · `Export.db_bytes/.store_total` `:616–:617`, `:826–:830` (written only when set) · GS-8 `:2644–:2645`, `:2650` · docstring `:21–:25`.
- **RED** (the final test text at `6a40a10`'s grader, 22:29:25Z): `verify72h selftest: 63 check(s), 5 failure(s)` — FB-1…FB-4 `AssertionError: verdict.json carries no fitness block — its keys: verdict, vocabulary, window, graded_at, export, loads, opaque, invariants, attestations, commands, runs, timeout_causes` · FB-5 `('clean_export', ['commands', 'runs', 'timeout_causes'])`. **GREEN** 22:31:13Z, 63/0.
- 13 mutants of `fitness()` — bench / identify / superseded / edge-open made eligible · null read as 0 · a stop counted · misses ignored · a timeout read as answered · per hour as per day · bytes/row over the window · the block before the causes · a `verdict` key inside it · the block moving the layer verdict — each caught (FB-1…FB-5, GS-8).
- README paragraph (D5), after `:91`: **The fitness readings (GATE-2; F31) — additive: no invariant reads them, no bar is set.** `verdict.json` → `fitness` (and report.md's last section): the confirmed ratio per command class (less Identify, `bench`, superseded, edge-open), restarts, the probe-answered ratio (store beside log) and store growth per day (47.9 MB/day beside). N3 sets bars, or none.

## §4 Verification (the map for the two-layer re-run)
- **`grade()` vs `breakdown.py`'s window mode** on SOAK-NIGHT-1, SOAK-NIGHT-2 and EXPORT-1 (`export.export_events` of the copy): (i) `by_outcome` equal; the cause rows equal (cause, reason, prior age, late) — 3 · 3 · 0. EXPORT-1's cut = the record's: 6,953 rows, positions 461127–468079.
- **Independent of the grader** (SQL_INDEP, the primary chain keys only): 3,009 issued, every partition row matched; 1,714 timeouts on 1,714 commands (max 1); w/ timeout and CONF by device × type = T3; 20 timeouts beside a failure; (iii) 0.
- **The 185** (SQL_REP): 185/185 cite a `state_reported`, same subject + attribute, value = `actual_value`; `exact` 133 · `within_tolerance` 52 (brightness |Δ| ≤ 2: 6 · colour ≤ 2 K: 22, ≤ 50 K: 24).
- **`breakdown.py`:** its tests and code were written together; RED = the final selftest text over stubbed bodies (28 functions `raise NotImplementedError`): `breakdown selftest: 10 check(s), 10 failure(s)` (22:16:45Z) — it proves each check can fail, not that it came first (BR-1's and FB-1…FB-5's REDs did come first); GREEN 10/0; 12 mutants each caught (M6, the window's upper edge, survived the first text → BD-8 tightened → caught).
- **The staged tool reproduces the numbers:** `breakdown.py` from the `checkout-index` copy over the whole copy writes byte-identical outputs — md5 `commands.csv` `f95c96c1d1a7` · t1 `29a4270e1d12` · t2 `0557fafeafb5` · t3 `e4c6b82c9886` · t3b `609372f23956` · t4 `4e9cbecd6b7e`.

## §5 Deviations
- [REVIEW] **D1 Where it ran:** the desk VM's Linux shell (Ubuntu 22.04, Python 3.10.12, bash 5.1.16 — the build BENCH-BOOT-1/GRADER-S31-1 name), not a `wsl -d Ubuntu` launch: §0.3's intent (Linux python3, never the Windows desk's) holds, its letter is not proven. The copy via a folder grant at `$HOME/mnt/backups/…`.
- [REVIEW] **D2 `TMPDIR=/tmp/gate2/tmp` on every call:** `/sessions` holds 27 MB free (GRADER-S31-1 F3); one exploratory read-only GROUP BY failed there (`database or disk is full`) before any number was taken; `breakdown.py` sets `PRAGMA temp_store = MEMORY` itself.
- [REVIEW] **D3** `mode=ro` on a WAL copy writes the `-shm` wal-index (its mtime moved from 00:47:37Z to this session's opens); the db's bytes never moved — md5, size, mtime equal first and last. The hub's own `mode=ro` re-runs do the same.
- [REVIEW] **D4** GS-8, a pinned check, gains one line (lift `fitness` before pinning 32bac40's bytes) and a docstring clause; FB-5 pins `6a40a10`'s bytes.
- [REVIEW] **D5** The README paragraph is drafted in §3, not written — README.md is outside §3's Files table.
- [REVIEW] **D6** The bars stand on the soak nights, EXPORT-1's window and the copy's last 72 h / 24 h: dry-run #1's window is not in the copy (§0 row 8).
- [INFO] D7 `breakdown.py` calls `timeout_causes()` twice: the first (the partition alone) only names the arm's subjects for SQL_STATES; the second is reported. grade()'s inline rules (open/edge-open `:612–:616`, duplicates `:607–:610`, (iii) `:671–:678`) are restated with cites; §4 pins them to grade().
- [INFO] D8 The bridge's stale-bytes failure struck once (the first copy of `test_verify72h.py` onto the desk landed the old bytes with a new mtime); every later copy went through a fresh path, md5 checked on arrival. (No git commit anywhere: §0 row 1.)
- [INFO] D9 `git add` and `git write-tree` could not unlink six `.git/objects/*/tmp_obj_*` (0c/Om5IKa · 15/hvWK1o · 3d/50pIzs · 77/xxVfJr · 7d/SGkWx9 · b5/aWHmU6); not locks; left.
- [INFO] D10 `breakdown.py` pins what the store cannot derive (the S31's OFF date, six sittings), each sourced; dark regimes are derived.
- [INFO] D11 `idempotency_class: IDEMPOTENT` (all 3,009) is the retry class, not F26's sense (F26 = the classifier's `bench`).

## §6 Findings for the register
- **F1 IR-191's breakdown delivered** (by device, class, week, cause): the 57 % is the Hue's (97.5 %) — 1,186 in its July dev weeks, 485 after its reporting died; the why for its 1,167 level/colour timeouts stays open (F3). OR-HUE-REPORTING-DEAD gains its start, measured: the Hue's last row 2026-07-19T00:49:15Z (the record had "dark across Sep 25–28").
- **F2 `bench` reads a stale prior:** 84 of 501 rest on a prior > 24 h old (1–75 days; 83 the dark Hue, 1 its first days) — GRADER-S31-1 F2, now measured. A bounded prior (older than k × the device's report interval → `unattributed` with a new reason) is a vocabulary change: the hub's ruling.
- **F3 Level and colour have no expectation in the grader** (1,167 `no-expectation`) while the core confirms them (TOLERANCE ±2 / ±50 K; 52 confirmations): `EXPECTATIONS` rows for `set_brightness`/`set_color_temperature` would let the classifier name their causes (a `constants.yaml` change — outside this lane).
- **F4 Two identify commands never terminated** (07-14 22:05Z Hue · 08-12 08:31Z S31): dispatched, no result, no timeout — (i) FAILs any window holding one; the ledger never tracks Identify (DISABLED), so only the adapter's immediate verdict closes it, and twice it did not land. A core read.
- **F5 (viii)'s class is the corpus's:** 1,108 of 1,596 runs COMPLETED with actions and no command (07-14 → 10-13; SQL_RUNS); every soak night FLAGs on it (36 · 28). The hero's "why did it fire" must not read COMPLETED as acted.
- **F6 The nightly restarts the app three times** (08:30–08:33Z): B2 = 0 fails every night unless declared; `--declared-restarts` in A1b's form is export.py's (outside this lane).
- **F7 The S31's two `device` classes:** late (10 of the 11 dev-session timeouts answered 0.6–29 s after the 5-s window — IR-53's window) and silent (15 at the nightly, none before the next sitting); none since 09-27.
- **F8 B3 has no store instrument before BC10:** the soak nights' only instrument is the log (S2.txt).

## §7 Instrument limits
The copy ends at `global_position` 1,876,566 (2026-10-13T00:40:01Z = Mon 19:40 CT). Its history is the rig — dev sessions, then the nightly suite and the sittings — never a household; fleet 2 → 10. Every series names the Hue dark from 07-20 (derived: 24 h after its last report, 07-19T00:49Z), the S31 OFF and unloaded from 09-20 (the record's), and the sittings. Over the whole copy the classifier reads priors across weeks (one whole-copy "export"); a 72-h window reads fewer (GRADER-S31-1 F2; BD-8 reproduces it). No app log on the desk: B3's log instrument and A1a read nothing in the dry runs. Scratch: the VM's `/tmp/gate2`; the CSVs regenerate with `breakdown.py --out`.

## Appendix A — the SQL, verbatim (each with the rows it returned)
§0b row 5 → 1: `select count(*), max(global_position) from events` · row 6 → 23: `select event_type, count(*) from events group by 1 order by 2 desc`

`breakdown.py`, as run over the whole copy (`breakdown.md` prints these for any window):
```sql
-- SQL_SPAN → 1
SELECT count(*), min(global_position), max(global_position), min(ingest_time), max(ingest_time) FROM events WHERE ingest_time BETWEEN 0 AND 4611686018427387904
-- SQL_PARTITION → 9046
SELECT global_position, event_id, event_type, schema_version, ingest_time, event_time, subject_ref, subject_type, correlation_id, causation_id, event_category, payload_size, payload, payload_iv, dek_ref, subject_ref FROM events WHERE event_type IN ('command_issued', 'command_dispatched', 'command_result', 'command_confirmation_timed_out', 'state_confirmed') AND ingest_time BETWEEN 1783542091937823 AND 1791852001146171 ORDER BY global_position
-- SQL_STATES → 23647
SELECT global_position, event_id, event_type, schema_version, ingest_time, event_time, subject_ref, subject_type, correlation_id, causation_id, event_category, payload_size, payload, payload_iv, dek_ref FROM events WHERE event_type = 'state_reported' AND subject_ref IN (X'019F436512399150182B3E59DB17100F', X'019F781E072B97DD86268B553626F26E') AND ingest_time BETWEEN 1783542091937823 AND 1791852001146171 ORDER BY global_position
-- SQL_REGISTRY → 20
SELECT global_position, event_id, event_type, schema_version, ingest_time, event_time, subject_ref, subject_type, correlation_id, causation_id, event_category, payload_size, payload, payload_iv, dek_ref FROM events WHERE event_type IN ('device_registered', 'entity_registered') ORDER BY global_position
-- SQL_REPORTS → 84
SELECT subject_ref, date(ingest_time / 1000000, 'unixepoch', 'weekday 0', '-6 days') AS monday, count(*), max(ingest_time) FROM events WHERE event_type = 'state_reported' AND ingest_time BETWEEN 1783542091937823 AND 1791852001146171 GROUP BY 1, 2 ORDER BY 1, 2
```
The bars (per window, `?` = the window's `ingest_time` µs edges), the independent check and the runs:
```sql
-- SQL_BARS → 1 per window
SELECT count(*), sum(payload_size), min(global_position), max(global_position), sum(event_type = 'integration_started'), sum(event_type = 'integration_stopped'), sum(event_type = 'integration_restarted'), sum(event_type = 'probe_answered'), sum(event_type = 'availability_changed') FROM events WHERE ingest_time BETWEEN ? AND ?
-- SQL_BOOTS → 6 · 6 · 1 · 26 · 6
SELECT ingest_time, event_type FROM events WHERE event_type IN ('integration_started', 'integration_stopped', 'integration_restarted') AND ingest_time BETWEEN ? AND ? ORDER BY global_position
-- SQL_INDEP → 9046
SELECT event_type, event_id, causation_id, subject_ref, CAST(payload AS TEXT) FROM events WHERE event_type IN ('command_issued','command_dispatched','command_result','command_confirmation_timed_out','state_confirmed') ORDER BY global_position
-- SQL_REP → 185 (params: the cited report_event_ids as blobs)
SELECT event_id, event_type, subject_ref, CAST(payload AS TEXT) FROM events WHERE event_id IN (?, …)
-- SQL_RUNS → 3
SELECT json_extract(CAST(payload AS TEXT), '$.final_status'), json_extract(CAST(payload AS TEXT), '$.action_count') >= 1, json_extract(CAST(payload AS TEXT), '$.command_count'), count(*), min(date(ingest_time / 1000000, 'unixepoch')), max(date(ingest_time / 1000000, 'unixepoch')) FROM events WHERE event_type = 'automation_completed' GROUP BY 1, 2, 3
```
The dry runs: `python3 -B tools/verify72h/export.py <label> <from> <to> --db <copy> --logs-dir <empty> --bundles-dir <empty> --exports-dir <dir> --log-utc-offset 0`, then `python3 -B tools/verify72h/grader.py <export-dir>`; every call `TMPDIR=… PYTHONIOENCODING=utf-8 python3 -B`.
RETURNED ../nexsys-hivemind/context/audits/2026-10-15_GATE-2_return.md 29934 staged=3 tree=7dc6041853131e9ac89e1b9023b8848e1b45c6e2

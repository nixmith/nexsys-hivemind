<!--
file: context/instructions/2026-10-13_bench-lane_GATE-2_the-promise-graded_IR-191-breakdown-and-the-fitness-bars_charter.md
purpose: GATE-2 — the grader learns to grade the PROMISE, not only the bookkeeping (HORIZON-1 F31; the v109 analysis A4; Nick's ruling of Tue 2026-10-13: IR-191's breakdown is GATE-2's first step, the options in front of him by Thursday). A desk lane in `nexsys-bench`: the all-time 57 % of commands that timed out their confirmation, broken down by cause (the landed classifier), by device and command class, and over time; in plain words what the hero can say today; then the candidate fitness bars as pre-registrations, dry-run on the corpus. No rig. The copy on the desk is the store; the live store is never read.
audience: the GATE-2 lane (Claude Code in `~/Desktop/Code/ClaudeFolder/nexsys-bench`) · the hub (its intake) · Nick (N3 — GATE-2's stance — by Oct 22)
state-type: lane charter
status: EXECUTED — returned, intaken ACCEPT and landed `5cf3bd0` at v111 b2 (marked v112 b1, Check 12); was DISPATCH-READY — cut v110 beat 3 (Tue 2026-10-13 ~16:5x CT) at bench `6a40a10` and core `176adad`; the Pi untouched; return by Thu 2026-10-15 12:00 CT
-->
# GATE-2 — the promise graded: IR-191's breakdown, then the fitness bars

## §0 The lane contract (read whole before any command; every line binds)
1. `date -u` first; every stamp you write derives from it (CT = UTC−5 until Nov 1). Work in `~/Desktop/Code/ClaudeFolder/nexsys-bench` on a branch `gate-2/evidence` off `6a40a10`; `git --no-optional-locks status --porcelain` must read 0 before you start; **zero commits** — you stage, the hub lands.
2. **The store is the desk copy** `C:\Users\Nick\hs-bench\backups\homesynapse-events-2026-10-12.db` (940,978,176 B; md5 `6dfd6e3c7441fb5a224b7ee666cc0d16`; 1,876,566 rows; `integrity_check` ok — dry-run #1's D0b, Mon 2026-10-12). Open it `file:…?mode=ro` with `uri=True`, always. **Never ssh to the Pi; never read the live store; never write the copy.** Verify the md5 first and paste the line.
3. Every python call runs as `PYTHONIOENCODING=utf-8 python3 -B …` (IR-183); the selftests run in WSL `Ubuntu` (`bash` on the Windows desk is the WSL launcher; the desk's 42/38 reading is that, not the tree's — BENCH-BOOT-1's return §6).
4. **The return** at `../nexsys-hivemind/context/audits/2026-10-15_GATE-2_return.md` (cap 30,000 B; §0 first — the verdict in ten lines; then the tables; the figures as tables, never prose), the `RETURNED <path> <bytes> staged=<n> tree=<write-tree sha>` line LAST. Nick's one-line report-back is that line.
5. Your return is read two layers: the hub re-runs your queries on the same copy. Every number carries the query that produced it (the SQL verbatim, in an appendix) and the row count it stands on.
6. Instrument limits you must state: the copy ends at `global_position` 1,876,566 (Mon 2026-10-12 ≈ 19:40 CT); the rig's history is the soak and the rehearsals, not a household; the Hue was dark for most of its life (OR-HUE-REPORTING-DEAD) and the S31 was OFF and UNLOADED from 2026-09-20 — name those regimes in every time series.

### §0b The premise table (the hub's greps at bench `6a40a10` and the copy's F1 counts; re-run each, paste the output line)
| # | Command (from `nexsys-bench`) | Expected |
|---|---|---|
| 1 | `git --no-optional-locks log -1 --format=%h && git --no-optional-locks status --porcelain \| wc -l` | `6a40a10` · `0` |
| 2 | `grep -n '^def timeout_causes\|^def cause_word(\|^CAUSE_WORDS\|^def check_causes\|^def grade\b' tools/verify72h/grader.py \| cut -d: -f1` | `131` · `136` · `540` · `814` · `973` |
| 3 | `grep -n '^COMMAND_ISSUED\|^COMMAND_RESULT\|^COMMAND_TIMED_OUT\|^STATE_CONFIRMED' tools/verify72h/grader.py \| cut -d: -f1` | `150` · `152` · `153` · `155` |
| 4 | `sed -n '69,71p' tools/verify72h/README.md \| cut -c1-60` | the "cause of a timeout … additive: no invariant reads it" paragraph |
| 5 | `PYTHONIOENCODING=utf-8 python3 -B -c "import sqlite3; c=sqlite3.connect('file:/mnt/c/Users/Nick/hs-bench/backups/homesynapse-events-2026-10-12.db?mode=ro', uri=True); print(c.execute('select count(*), max(global_position) from events').fetchone())"` (WSL path; on Windows python use `C:\\…`) | `(1876566, 1876566)` |
| 6 | the per-type counts on the copy: `select event_type, count(*) from events group by 1 order by 2 desc` | `state_reported 1202395` · `state_changed 631933` · `automation_action_completed 14364` · `automation_action_started 14364` · `command_dispatched 3009` · `command_issued 3009` · `command_confirmation_timed_out 1714` · `automation_completed 1596` · `automation_triggered 1596` · `command_result 1129` · `availability_changed 481` · … · `state_confirmed 185` |
| 7 | `md5sum /mnt/c/Users/Nick/hs-bench/backups/homesynapse-events-2026-10-12.db \| cut -c1-32` | `6dfd6e3c7441fb5a224b7ee666cc0d16` |

## §1 What this delivers (in this order; step 1 is the deliverable Nick reads Thursday)
**Step 1 — IR-191's breakdown (the evidence).** Over every `command_issued` in the copy (3,009), the terminal each reached under the grader's own partition (invariant (i): `state_confirmed` · `command_confirmation_timed_out` · a `command_result` whose outcome ∉ {acknowledged} · none), then:
- **by cause** — run the landed classifier (`timeout_causes()` at `:814`; its words `bench` · `device` · `unattributed` with `cause_reason`) over the copy's commands and events, NOT a re-implementation: build the `commands`/`events` inputs the way `grade()` builds them from an export (read `grade()` `:540→` and `export.py` for the shapes; if the shapes need an export directory, write a desk-only adapter that materialises one from the copy — a read, never a write to the copy); state how many of the 1,714 timeouts the classifier calls `bench` (idempotent sends included — name them), `device`, `unattributed`, and the reasons' histogram;
- **by device and by command class** — the target device (its EUI64/ULID → the registry's name: G4-1, G4-2, TR3, S31, HUE, …) and the command's class (on/off · level · color · a query; take the class from the payload's command kind), a table of issued · confirmed · timed-out · failed · unconfirmed-by-construction (idempotent) per device × class;
- **over time** — the same counts per ISO week from the first `command_issued` to the copy's end, with the regimes marked (the Hue dark; the S31 off since 09-20; the soak nights; the rehearsals); the trend in one sentence per device;
- **in plain words** — what the hero claim ("did it actually confirm") can honestly say TODAY, in three sentences, each tied to one table; and the one sentence it must NOT say.
**Step 2 — the candidate fitness bars as pre-registrations** (the return's §6 row 3; F31): a confirmed ratio per device class · restarts = 0 across the window · the probe-answered ratio · a store-growth ceiling (≈ 48 MB/day at the rig's posture is the measured baseline — dry-run #1's F1) — each stated as a bar the 72-h grader could read ADDITIVELY beside the existing invariants, with the corpus number it would have produced on the soak nights and on dry-run #1's window (the copy holds them). No bar is adopted here: **the options for N3** are the lane's last section — (a) gate the run on fitness bars; (b) measure and report with a red line that holds the household installs; (c) bookkeeping only — each with what the copy says it would have done to the soak nights.
**Step 3 — the amendment, dry-run on the corpus:** the `verify72h` amendment that would carry the bars, as a DIFF against `6a40a10` on the branch (staged, not committed; `test_verify72h.py` GREEN with a red-first check per bar; `constants.yaml` md5 unchanged) — only if step 1 and 2 are done by Thursday 12:00; otherwise the diff is a design note in the return and the code waits for N3.

## §2 Files to read before starting (by range; `grep -n` first)
`tools/verify72h/README.md` whole (16 KB) · `tools/verify72h/grader.py` `:1–:160` (the invariants and the constants), `:540–:620` (`grade()`'s inputs), `:814–:990` (the classifier) · `tools/verify72h/export.py` `:1–:120` (the export's shapes) · `../nexsys-hivemind/context/audits/2026-09-23_S31-command-confirm_59-bundles_first-read.md` §0 (the 22/59) · `../nexsys-hivemind/context/audits/2026-10-12_v110-b2_DRY-RUN-1-Mon_intake_two-layer_audit.md` §2.1 (the copy's provenance) · `../nexsys-hivemind/context/planning/improvement-register.md` by grep: `IR-191`, `IR-184`, `IR-88`, `IR-51`, `IR-52` · `../nexsys-hivemind/context/strategy/claim-register.md` (the three rows) · `../homesynapse-core/core/device-model/MODULE_CONTEXT.md` by grep `Confirmability\|ConfirmationPolicy` (what "confirm" means in the core's own words).

## §3 Files to create or modify (the Files table governs; nothing else is written)
| Path | Change |
|---|---|
| `tools/verify72h/breakdown.py` | new — the desk-only read of a store COPY: the partition, the classifier call, the three tables as CSV + markdown; `--selftest` on a fixture of ≤ 40 synthetic rows; `_utf8_stdout()` at entry |
| `tools/verify72h/test_verify72h.py` | one check that `breakdown.py --selftest` prints its last line |
| `tools/verify72h/grader.py` · `scenarios/constants.yaml` | step 3 only, if reached; `constants.yaml`'s md5 `9b0af47b3376` unchanged |
| the return | as §0.4 |

## §4 What to watch out for
- The classifier was written for an EXPORT window (one run); over the whole copy it meets commands that never had an expectation (`no-expectation`) and opaque results (`opaque`, payload_iv set): report those reasons as their own rows, never fold them into `device`.
- `state_confirmed` is 185 against 1,129 `command_result` — read the grader's (iii) before you call anything confirmed; the core's precedence is the grader's.
- Idempotent sends (F26) cannot confirm by construction — count them as `bench`'s named subclass, not as the device's failure.
- The weekly series must carry the fleet size and the regimes on the air; a week with the Hue dark and the S31 off is not comparable to a soak night without saying so.
- The copy is 941 MB; `global_position` is the index; one query per table, never a Python loop per command over the whole log.

## §5 Out of scope
Any Java; any read of the Pi; the hero's web copy; the household telemetry pipeline (DIAG-1); the choice among the N3 options (Nick's).

## §6 Success criterion (binary)
§0b's seven rows re-run and pasted · the md5 line · the four tables with their SQL · the classifier's own words on the 1,714 (bench · device · unattributed, with reasons) · the three plain sentences and the forbidden one · the N3 options with what each would have done to the soak nights · `breakdown.py --selftest` GREEN (red-first) and `test_verify72h.py` GREEN in WSL · zero commits · `git write-tree` in §0 and the RETURNED line · the return ≤ 30,000 B by Thu 2026-10-15 12:00 CT.

## §7 The dispatch (Nick pastes into a FRESH Claude Code conversation in `~/Desktop/Code/ClaudeFolder/nexsys-bench`)
```
You are the GATE-2 bench lane. Read `../nexsys-hivemind/context/instructions/2026-10-13_bench-lane_GATE-2_the-promise-graded_IR-191-breakdown-and-the-fitness-bars_charter.md` WHOLE before any command; its §0 binds every line. `date -u` first. Work on a branch `gate-2/evidence` off `6a40a10`; zero commits; the store is the DESK COPY named in §0.2, read-only, never the Pi. Re-run §0b's seven rows and paste each output line. Deliver §1 in order — step 1 by Thursday 12:00 CT is the deliverable; the return at `../nexsys-hivemind/context/audits/2026-10-15_GATE-2_return.md` (≤ 30,000 B; §0 first; the SQL in an appendix), its last line `RETURNED <path> <bytes> staged=<n> tree=<git write-tree sha>`.
```

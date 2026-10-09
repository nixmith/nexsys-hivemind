# AVAIL-LINE-1 return — 2026-10-09 ~08:55 CT (date -u 13:54:55Z)

## §0 The card — DELIVERED
Bench `main` @ `ba846c2`, porcelain empty at the first act; branch `avail-line-1/ir118-join-rejected`; 0 commits; no `.git/*.lock`; staged tree `73ed717c6def852c474ea24af48be43b7bfb8b71`.
```
$ git --no-optional-locks diff --cached --stat
 tools/runner/README.md            |   6 +-
 tools/runner/nightly_digest.py    | 228 ++++++++++++++++++++++++++++++++------
 tools/verify72h/grader.py         |   6 +
 tools/verify72h/test_verify72h.py |  59 ++++++++++
 4 files changed, 262 insertions(+), 37 deletions(-)
```
Closing lines on the staged tree (desk, `PYTHONIOENCODING=utf-8` — §6):
- `python3 -B tools/runner/nightly_digest.py --selftest` → `selftest: 53 check(s), 0 failure(s)` (43/0 before)
- `python3 -B tools/verify72h/test_verify72h.py` → `verify72h selftest: 46 check(s), 2 failure(s)` — T3b/T3c, bash-on-Windows (44/2 before any write, the same two; Pi 46/0)
- `python3 -B tools/runner/test_engine.py` → `selftest: 42 check(s), 0 failure(s)`
- `python3 -B tools/test_bench_sh.py` → `bench.sh selftest: 27 check(s), 24 failure(s)` — identical before any write (§6; Pi-green)
`constants.yaml` md5 `9b0af47b3376` unchanged; `len(AMBIENT_WHITELIST)` 67 → 68.

Red texts. Unit 1 (53/21): `fleet_text() got an unexpected keyword argument 'avail'` x4 · `KeyError: 'avail_numbers'` x4 · 3-tuples against 4-tuples x9 (`want: (3, 3, 3, (3, 3, 0)) / got : (3, 3, 3)`) · composed `fleet: (3, 3, 3)` / `(None, None, None)` / `(2, 3, 0)` · `want: True / got : False`. Unit 2 (46/4): A1-8 `AssertionError:` (bare, at the membership assert) · A1-9 `AssertionError: {… 'verdict': 'CANNOT-GRADE', 'unplaced': [{… 'event_type': 'join_rejected', 'why': 'not in the EventTypes catalog'}] …}`.

### §0b re-run
1. `ba846c2` · `0`
2. `:135 def fleet_text` · `:173 def fleet_ids_from_body` · `:214 def fleet_numbers` · `:277 def format_digest_line` · `:624 def selftest`
3. `289:    fleet_field = "" if fleet is None else " · fleet: %s" % fleet`
4. `837:    def compose_fleet(raw, prior):` · `843:        return fleet_text(*got)`
5. `selftest: 43 check(s), 0 failure(s)`
6. `:144 AMBIENT_WHITELIST = (` · `:185 "permit_join_opened", "permit_join_closed",` · `:645 ("whitelist_size", len(AMBIENT_WHITELIST))])` · no `join_rejected`
7. `67` · as pasted, CRASHED before any check: `UnicodeEncodeError: 'charmap' codec can't encode character '→'` (cp1252 stdout); with `PYTHONIOENCODING=utf-8`: `verify72h selftest: 44 check(s), 2 failure(s)` = T3b/T3c `/bin/bash: C:UsersNick…nexsys-benchtoolsbench.sh: No such file or directory` · `:1965` the `len(grader.AMBIENT_WHITELIST)` receipt — INSTRUMENT (D2)
8. `EventTypes.java:320:	public static final String JOIN_REJECTED = "join_rejected";` · `ZigbeeIntegrationAdapter.java:1819:            publishWindowEvent(EventTypes.JOIN_REJECTED, 1, new JoinRejected(`
9. `195:        summary.put("availability", state.availability().name());` · `196:        summary.put("stale", state.stale());`

## §1 What changed (final-tree lines)
- `tools/runner/nightly_digest.py` — docstring :23 (example gains `· avail: 6/6`), :29–:35 (the field's law) · `fleet_text(…, avail=None)` :142, :149–:174 (appends ` · avail: a/r`, ` · stale n` only when n > 0; `unread` stays the whole field) · NEW `avail_numbers(raw)` :240–:273 beside `fleet_ids_from_body`, the same raise-on-unsound; `availability == "AVAILABLE"` exact; rows = the body's row count; `stale is True`; a keyless row counted, never raised · `fleet_numbers` :277–:310 → 4-tuple, `(None,)*4` on any unsound arm · `cmd_compose` :549–:558 (three avail flags, all or none) · `cmd_fleet` :566–:571, :594–:597, :612–:618 (`NB_FLEET_AVAIL/ROWS/STALE` after the three) · argparse :1048–:1059 · selftest :870–:878 (`_REGISTRY_OK` gains the J1 row shape), :884–:917 (nine wired checks → 4-tuples), :926–:932 (`compose_fleet`), :946, :948–:1001 (section 14, 10 new checks).
- `tools/runner/README.md` :168–:172 — example gains `avail: 6/6`; one sentence: LEFT vs SILENT, the 2026-10-04 exhibit.
- `tools/verify72h/grader.py` :186–:191 — `"join_rejected",` after the PJ-2 pair, the §1.2 comment verbatim; nothing else (CATALOG derives).
- `tools/verify72h/test_verify72h.py` :713–:727 — `Export.join_rejected(at, joiner, scope=None, status="UNSECURED_JOIN")` in wire snake_case (JoinRejected.java:38–:45; ZclIngestionUnit.java:210); :1987–:2030 — A1-8, A1-9.

## §2 The tests
- Unit 1 red → green: the 9 wired `fleet_numbers` checks (4-tuple); `… read-failure path composes fleet: unread` (transient red, text unchanged); `… value path composes the two numbers` (→ `avail: 3/3`); 10 NEW `avail:` checks: the text forms `6/6 · re-seen 0 · avail: 6/6` / `9/10` / `10/10 · stale 1` / unread stays unread with a triple beside; the reads: exact enum (one UNKNOWN of two → `1/2`), keyless row recorded, no case fold or prefix, stale JSON-true only, unsound RAISES; the composed `fleet: 2/3 · re-seen 0 · avail: 1/2`. Unchanged, green: the pre-R-5 byte-identical line; `never 0/0`.
- Unit 2 red → green: A1-8 — in the whitelist and CATALOG; a row inside a declared window is AMBIENT, (iv) PASS, counted once, A1b untouched (declared 1 / closed 1), `whitelist_size == len(…)`. A1-9 — a row BETWEEN windows (scope null, declared 0) is AMBIENT on its own.

## §3 Deviations
- D1 [REVIEW] — the wrapper hop: `tools/nightly.sh:308–:310` builds exactly three `--fleet-*` pairs and is outside the write set (§4), so the Pi's line stays byte-identical until `fleet_args` gains `--fleet-avail $NB_FLEET_AVAIL --fleet-rows $NB_FLEET_ROWS --fleet-stale $NB_FLEET_STALE` (the `fleet` verb already emits them); the 3-line wiring is the hub's follow-on.
- D2 [REVIEW] — §0b row 7's selftest did not print its expected line on this desk (cp1252 crash; then 44/2 = T3b/T3c bash-on-Windows). The lane read the premise as HELD (repo state, not console) and proceeded; the hub rules.
- D3 [INFO] — `_REGISTRY_OK` rows carry the J1 shape (row 9) so the wired value path reads `avail: 3/3`; the keyless row is pinned by its own check.
- D4 [INFO] — `stale`: only JSON true counts, a string is not (pinned); `cmd_compose`: a partial avail flag set omits the segment, never `unread`s the fleet numbers beside it.
- D5 [INFO] — A1-9 is a second check beyond the one asked; 46 ≥ 45.

## §4 Findings
- F1 — the `[--] fleet:` echo (nightly.sh:311) will not show avail even after D1; only the digest line.
- F2 — `avail: 0/<rows>` is the designed reading of a keyless (pre-J1) body; on 49455fc a `0/n` is real darkness.
- F3 — `bash` from Windows python is the WSL launcher here (`RPC_S_SYSTEM_HANDLE_TYPE_MISMATCH`): T3b/T3c and the 24 bench.sh checks are Pi-only.

## §5 bench-handoff entry
AVAIL-LINE-1 (2026-10-09, desk lane, `avail-line-1/ir118-join-rejected` over `ba846c2`, staged tree `73ed717c`, 0 commits): IR-118's `avail: <available>/<rows>` (+ ` · stale n` when n > 0) joins the digest's fleet field after `re-seen n`, read by `avail_numbers` from the SAME `/api/v1/entities` body as the ids — exact `AVAILABLE`, the body's row count as its own denominator, an unsound body `unread` for the whole field; `fleet_numbers` is a 4-tuple, `fleet` emits `NB_FLEET_AVAIL/ROWS/STALE`, `compose` takes the three flags (nightly.sh still passes three — D1). The grader's whitelist gains `join_rejected` (J2 @ 49455fc) as a named deviation in PJ-2's form; `whitelist_size` 68. Selftests 53/0 and 46/0 (Pi) after observed reds; engine 42/0, bench.sh 27/0 (Pi) untouched; md5 `9b0af47b3376`.

## §6 Instrument limits
cp1252 console: the verify72h suite needs `PYTHONIOENCODING=utf-8` here (the digest's `_utf8_stdout` covers its own); `bash` → the WSL launcher (T3b/T3c, the bench.sh suite); CT = UTC−5 by hand; bytes below = the on-disk CRLF size.

## §7 AVAIL-LINE-1b (resumed 2026-10-09 12:54 CT; date -u 17:54:27Z) — the hub's D1 ruling: nightly.sh gains the three avail flag pairs
- STOP at a lock, 17:54:27Z (§0): `.git/index.lock` present in nexsys-bench — 0 B, mtime 2026-10-09 09:21:34 CT (~3.5 h old), no `git.exe` in tasklist, VS Code open; `git write-tree` refused (`Unable to create … index.lock: File exists`). Never a sweep: no write to the bench tree, nothing staged or unstaged (the four files stay staged, 0 commits); the 1b acts (nightly.sh:308–:311, the static check) NOT started. Resumes when Nick clears the lock.

- Lock cleared by Nick (`rm .git/index.lock` in his shell); resumed 17:57:42Z; no lock met after; the four stayed staged, 0 commits.
- (1)(2) `tools/nightly.sh` :308–:313 — `fleet_args` gains `--fleet-avail $NB_FLEET_AVAIL`, `--fleet-rows $NB_FLEET_ROWS`, `--fleet-stale $NB_FLEET_STALE` after the three pairs, one per line in the file's own continuation form; :314 the `[--] fleet:` echo gains ` · avail: $NB_FLEET_AVAIL/$NB_FLEET_ROWS` before `(registry read: …)`. `bash -n tools/nightly.sh` (Git Bash): syntax ok.
- (3) No selftest reads nightly.sh (grep: only docstrings in nightly_digest.py), so the static check is section 15 of `nightly_digest.py --selftest` (:1003–:1021): `wrapper: nightly.sh fleet_args passes the three avail flags with their NB_ values` — reads `tools/nightly.sh` beside its own path, takes the `fleet_args="--fleet…"` assignment (:299's empty `local` excluded by the `--fleet` anchor), whitespace-normalized, and wants the three `--flag $NB_VAR` pairs. RED first: `want: ['--fleet-avail $NB_FLEET_AVAIL', '--fleet-rows $NB_FLEET_ROWS', '--fleet-stale $NB_FLEET_STALE'] / got : []` → `selftest: 54 check(s), 1 failure(s)`; after the wrapper edit `[ok]`.
- (4) Closing lines (desk, `PYTHONIOENCODING=utf-8`): `selftest: 54 check(s), 0 failure(s)` · `verify72h selftest: 46 check(s), 2 failure(s)` (T3b/T3c, desk; Pi 46/0) · `selftest: 42 check(s), 0 failure(s)` · `bench.sh selftest: 27 check(s), 24 failure(s)` (desk, unchanged; Pi 27/0). md5 `9b0af47b3376` unchanged.
- (5) Staged, 0 commits, porcelain = the five; staged tree `f50d45b29ad296cb9e454ce6a6b5d258e66023ca`:
```
 tools/nightly.sh                  |   7 +-
 tools/runner/README.md            |   6 +-
 tools/runner/nightly_digest.py    | 248 ++++++++++++++++++++++++++++++++------
 tools/verify72h/grader.py         |   6 +
 tools/verify72h/test_verify72h.py |  59 +++++++++
 5 files changed, 287 insertions(+), 39 deletions(-)
```
- D6 [INFO] — nightly.sh's two comments still say three (:295 `prints three assignments`, :324 `either empty or three`); untouched per "nothing else" — a two-word follow-on. D7 [INFO] — this append carries the file past §0's 8,192-B ceiling; the 1b instruction governs the append.

RETURNED ../nexsys-hivemind/context/audits/2026-10-09_AVAIL-LINE-1_return.md 10976 avail-line-1/ir118-join-rejected staged=5

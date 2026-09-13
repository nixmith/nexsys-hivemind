<!--
file: context/audits/2026-09-13_R-5A-ii_return.md
purpose: The R-5A-ii bench lane's return — the nightly's fleet wiring, the harness cycle-end bound, the constants lint in `suite --list`.
audience: the hub (audits) · Nick (lands the card)
state-type: lane return.
instruction: context/instructions/2026-09-13_bench-lane_R-5A-ii_nightly-fleet-wiring_cycle-end-bound_constants-lint.md
baseline: nexsys-bench 1201368, Part A uncommitted (nine paths; index empty). HEAD unchanged at exit; index empty at exit.
-->

# R-5A-ii — bench lane return (Sun 2026-09-13 CT · UTC−5)

## §0 CARD

**DONE against §1's table.** Desk only; the bench card was never in my hands;
no live command anywhere. `date -u` at entry `2026-09-13T22:29:30Z`.

**Census: 6 M — §1's table exactly, no deviation.**
M `tools/nightly.sh` · M `tools/runner/nightly_digest.py` · M
`tools/harness/harness.py` · M `tools/harness/test_harness.py` · M
`tools/runner/runner.py` · M `tools/runner/test_engine.py`. Two are NEW to
the porcelain (`nightly.sh`, `runner.py`); the other four were already in
Part A's nine.

**Combined tree: 11 = Part A's 9 + my 2.** Index empty at exit. No `git add`,
no commit; every git call `--no-optional-locks`.

**P1 — MET.** Only §1's files touched; Part A's other five byte-untouched.

**P2 — MET.** Each new check RED at HEAD by construction, red OBSERVED
before its edit, GREEN after. Row 3: `exit was 0, want 2`. Row 4: three reds,
all `exit was 0, want 2` (duplicated scenario key · duplicated constants key
· unresolvable `${C.*}`). Row 2: 12 reds through a name-resolving guard, so a
missing function read as a failed CHECK, not a crashed gate.

**P3 — MET.** `bash -n tools/nightly.sh` passes. The read-failure line the
`--selftest` fixture composes:
`2026-08-01 quiesced AUTO floor: 9/9 PASS · fleet: unread · bench-hero RESTORED ✓ · ON-latency 0.11s`

**Gates:** `test_harness.py` **28 → 29** · `--selftest` **30 → 43** ·
`test_engine.py` **14 → 18**. 0 failures, three times. Tally **0**. Both
FENCE checks green: zero network calls.

**Preservation, green at HEAD *and* after:** the real `suite auto --list`
still lists 9 legs, `all load lawfully`, exit 0 — and now proves their
`${C.*}` resolve, which it did not before; the three standing SD-A4 checks
unchanged; the DP-4 line byte-identical with no fleet value; the floor
byte-identical (`9/9 PASS`) across the four paths simulated.

## §1 The rows

**Row 3 — cycle-end bound** (`harness.py`). `window-seconds-exceeded` moves
from `args.at <= bound` to `(args.at + args.off_for) <= bound`. The ledger
stamps ONE instant per cycle (`record_cycle`), so a cycle restoring after the
window closed leaves the next window's cap and min-gap reasoning about a
cycle still in progress. The ABSENT arm is untouched (`UNBOUNDED`).

**Row 4 — the constants lint** (`runner.py`; `--list` grounded at
`cmd_suite_list`, `runner.py:211`). `duplicate_top_level_keys()` reads through
`yaml.compose()`, which keeps the node tree BEFORE `safe_load` collapses a
repeated key to its last: a duplicate in a scenario refuses that leg, one in
`constants.yaml` refuses the listing before any leg is named — a shadowed
block silently re-points every `${C.*}` below it. `--list` now also resolves
`${C.*}` (`engine.substitute`, `defer_lets=True`).
`constants`/`constants_path` are REQUIRED, not defaulted: a check skippable
by omission is the vacuous-green class.

**Row 2 — the wired call shape** (`nightly_digest.py`, still standalone —
no `import engine`). `fleet_ids_from_body()` takes ids from one captured
`/api/v1/entities` body and RAISES on anything unsound, the same id twice
included: a set would collapse the repeat and understate the fleet.
`fleet_numbers()` is the whole fail-safe law in one pure function: three
numbers, or the triple `fleet_text` renders `unread` — no third outcome, no
path from a bad read to a number. `expected` is `fleet.entities`, the one
declared denominator; an undeclared one reads `unread`. A read positively
returning ZERO rows is a READING and composes `0/<expected>`: `never 0/0`
bars a fabricated denominator, not an honest zero numerator.

**Row 1 — the wiring** (`nightly.sh`). `read_registry()` makes the one authed
read, prints the BODY alone, returns nonzero unless a clean 200 (token rides
command substitution only — L3). It sits in `finish()` AFTER the post-restore
read and BEFORE the compose: that read is the app's readiness proof, so
ordering — not a special case — keeps an empty registry from being read
mid-boot. The wrapper does no arithmetic and takes no branch of its own; all
error handling is in the tool. No flags ⇒ `fleet: unread`. HANDS-OFF holds:
nothing changes what the suite RUNS or how the floor is GRADED.

## §2 Two judgements

1. **The route literal.** `/api/v1/entities` is now spelled a second time, in
   `nightly.sh`, beside `engine.py`'s `check_ulid_provenance`. A constants key
   would have touched a Part A file outside my table, so I left the literal
   and bounded the drift: a wrong route answers 404 or nonsense, and every
   unsound read lands on `unread` — it can fail to produce a number, never a
   wrong one. **One spelling = a Part B row.**
2. **`fleet-prior-ids.json`.** `re-seen` needs a prior, so `fleet` reads and
   rewrites one file under `nightly.digests-dir`. A missing prior is an EMPTY
   prior, not a failure — the first night knew nothing, and `re-seen 0` beside
   a full `adopted` says so; a failed WRITE costs tomorrow's split alone.

## §3 Ground re-read

`SCENARIO_FORMAT.md:18`/`:24`; design §4 `:106`–`:129`; `harness.py:58`,
`:135`, `:144`, `:159`, `:456`; `engine.py:621` (the DP-1 read surface this
lane reuses), `:1650` (the substitute order `--list` now matches);
`constants.yaml:52`–`:61` `fleet:` (`entities: 6`, no `expected:` synonym). Charter §A2 SD-A3/A4/A7 applied; SD-A4 extended
per row 3. Register C throughout; no product name.

RETURNED nexsys-hivemind/context/audits/2026-09-13_R-5A-ii_return.md 6045

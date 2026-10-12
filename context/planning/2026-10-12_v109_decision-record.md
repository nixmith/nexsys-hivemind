<!--
file: context/planning/2026-10-12_v109_decision-record.md
purpose: The v109 hub window's decision record — Nick's words verbatim, the facts at the instrument, the decisions by beat (D-v109-n). The window opened on Nick's paste of v109's text (Mon 2026-10-12 11:45 CT).
audience: the hub (reads by id) · Nick
state-type: decision record (one window)
status: LIVE — v109 beat 1 (Mon 2026-10-12 ~12:1x CT; instrument 2026-10-12T17:13:11Z).
-->

# v109 — the decision record

## §1 Nick's words, verbatim
- **Mon 11:45 CT** (with v109's text): `TIME: 11:45 CT` · `HIVE: LANDED cdf54e7` · `CAPACITY: Mon (today) 9, Tues 5` · `COMPARATOR-1:` · `OUTREACH-2: go | edits` · `BENCH-BOOT: mon19 · tue20 · wed21` · `DRY-RUN-1 (Mon): ready to dispatch upon your prompt`
- **The dispatch text** = `handoff/2026-10-12_v109_dispatch-text.md` from line 9 (four distinctive lines matched at the bytes, b1); its status flips to FILED.

## §2 The facts at the instrument (banked; no act)
- **SHELL: up** — the device shell answered at 2026-10-12T16:45:40Z (v108's six beats ran without it, D-v108-16).
- **The five HEADs** (16:46:19Z): core `176adad` · hivemind `cdf54e7` (v108's close card — Nick's `HIVE:` word matches) · skills `e9a77a8` · bench `32bac40` · docs `e2a5844`; porcelain 0 and ahead 0 in all five; all on `main`.
- **`render_state --check`:** 7 MATCH, 0 DIFF.
- **The preflight, one line per check:** C1 PASS (snapshot = handoff = v108 b6, 2026-10-12) · C2 PASS (both newest segments v108 b6; no `*plan-of-record.md` pointer) · C3 PASS (`176adad` = `176adad`) · C4 PASS (46 DONE-row shas, all resolve) · C5 PASS (Open Risks' newest date 2026-10-10; the fields not re-walked — disclosed) · C6 PASS (`coder-handoff.md`: "NEXT WU: none in the Java domain before the freeze") · C7 PASS (19 modules, 19 MODULE_CONTEXT.md, 0 templated) · C8 PASS (no active entry above `## Archived`) · C9 PASS (28/28 identical at the bytes: device source vs the session's synced trees, aggregate md5 `8d55622a3e33` both sides) · C10 PASS (104 cited; the 3 misses are the template patterns `YYYY-MM-DD_topic.md` · `months/…` · `weeks/…`) · C11 PASS (spot-check: `CommandIssue` · `isStoreFailure` · `skipped_unavailable` resolve in core) · **C12 STALE (1)**: `instructions/2026-10-11_frontend-lane_HERO-U3_recovery-card-on-the-live-record_v1.1*.md` still `DISPATCH-READY` after its intake (v108 b2) and landing (`ba08dd8`, b3) → its status flips to EXECUTED this beat; (2) 0 · (3) 0. **Aggregate: PASS after one reconcile.**
- **No lane return on disk** (porcelain 0 in every repo; none in `_scratch`). COMPARATOR-1's word came back blank.
- **The grader's catalog:** 78 `EventTypes` constants at `176adad`; two are absent from `grader.py` — `probe_answered` (`:123`) and `availability_contract_declared` (`:129`), AVAIL-API-1 (`2a54145`); `2a54145` is under `176adad`, `e11ae20` and `ba08dd8`, not under the Pi's `37f05a9`.
- **The selftests at `32bac40` on the device VM:** verify72h 48/0 · `test_engine.py` 42/**13** on the first run, 42/0 on the re-run · digest 54/0 · `bench.sh` 27/0; porcelain 0 after.
- **The read set trimmed (disclosed):** (e) the v108 DR, (f) the plan's §3 and (g) the lessons were not read at the boot — v109's text carries D-v108-29..35, the calendar and the 10-12 lesson; the plan review's line 70 was read for the charter.

## §3 The decisions (beat 1, Mon 2026-10-12 ~12:1x CT)
- **D-v109-1 — the boot:** PASS after one reconcile (C12: HERO-U3's instruction → EXECUTED); `SHELL: up` said first; the window's ONE deliverable is beat 1's (no return on disk → GRADER-S31-1 chartered).
- **D-v109-2 — GRADER-S31-1 CHARTERED DISPATCH-READY** (`instructions/2026-10-12_bench-lane_GRADER-S31-1_timeout-cause_device-or-bench_and-the-catalog_charter.md`), Unit A: every command that times out gets a `cause` from the store's own events, by a five-step rule pre-registered in its §1 — `bench` (the prior report already held the commanded value: IR-51's class) · `device` (dispatched, a real edge asked, no matching report in the window) · `unattributed` with its reason (`no-expectation` · `no-prior-value` · `opaque` · `not-dispatched`); the late report, the dispatch delay, the result and the in-window mismatches recorded beside it, never changing it; additive — no verdict word, outcome, invariant or count moves (IR-88). Lands as BP10 at BC10.
- **D-v109-3 — Unit B folded into the same lane (IR-179):** without the two AVAIL-API-1 types in the whitelist, invariant (iv) CANNOT-GRADEs the first window after BC10 whichever tree Friday picks — SOAK-NIGHT-3's grading, dry-run #2's and the run's. Same file, same landing, a precedent form (PJ-2 · J2); the lane may return Unit B alone at its budget.
- **D-v109-4 — the probe pairing is the soak card's, not the grader's:** the probe line names the IEEE address, the command names the entity, and a night's export holds no map between them. **P-GS1** pre-registered for SOAK-NIGHT-3 (the S31's `on` reports ≥ 1 per hour → the prior exists; 0 → `no-prior-value` and a carried-in prior is the next row).
- **D-v109-5 — IR-180 filed:** `test_engine.py` read 13 of 42 red on a cold device-VM run and 0 on the re-run; the failing names were not captured (the first run's output was tailed) — the next run that reds captures them.
- **D-v109-6 — `DRY-RUN-1`:** at ≈ 19:00 CT as cut — the packet is DISPATCH-READY and D2 is +24 h at the hour (Tuesday ≈ 19:00 CT); a scheduled send hands it at 18:55 CT (the time-gated act, §0 (i)); the line back goes to whichever hub is open.
- **D-v109-7 — the words:** `OUTREACH-2:` and `BENCH-BOOT:` came back as the template — open, not assumed; `COMPARATOR-1:` blank — not counted running (the cap reads 1 with GRADER-S31-1, 2 if it is). `CAPACITY: Mon 9` → GRADER-S31-1 runs this afternoon (the plan's `tue`, pulled forward as v109's text allows).
- **D-v109-8 — the acts in order:** the dispatch line → `GRADER-S31-1: running` → the b1 card → `HIVE: LANDED <sha>` · b2: the two unit cards' stub-ssh dry-runs (row ii — the shell is up) and GRADER-S31-1's intake when it returns · the close before 19:00 CT.

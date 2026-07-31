<!--
file: context/instructions/2026-07-31_B3_bench-autostart-nightly_bench-instruction.md
purpose: B3 — BENCH-AUTOSTART: the nightly self-running AUTO suite (the amended 9-leg order, park LAST), the morning one-line digest, flight-recorder bundles on failure, and QUIESCENCE BY CONFIG-SWAP with restore guaranteed — the four ratified hermeticity amendments realized as MECHANISM, not intention. Plus six riders: the ON-report-latency digest line (the margin instrument) · the C2 rejoin-race OPERATOR port · the I5 boot-demo fixture re-mint · the I6 runner-demo README (with the same-day re-run trap) · the F-1 `bench.sh api_token` verb · the `.gitattributes` LF-only fix.
audience: Coder (desk half — host-CC lane, bench repo); Nick (P-block measurements + the Pi install half); the PM hub (two-layer audit at return).
status: ISSUE-READY. Baseline: bench `8bce651` (clean, verified 2026-07-31); the deployed Pi build `c09c61c` (the suite's target — zero core changes in this WU). Dispatch gate: ⚠ the mirror is UNVERIFIED from the remote hub — Nick confirms his skill-mirror sync BEFORE launching the host-CC desk session (standing lane-map law).
returns: file the lane return to `context/audits/2026-07-31_B3_return.md` (the returns-to-audits law). The hub audits before any commit.
sequencing: THE P-BLOCK (Nick, ~5 min read-only on the Pi) runs FIRST and its pastes come back to the hub/desk; the desk half pins from those pastes (MEASURE-THEN-PIN, the B2 two-stage precedent); the Pi install half runs last. The desk half MAY start before the P-block on every part not marked ⛔PIN.
value-rationale (C1 arithmetic, CORRECTED — restated at authoring per the v42 brief): B3 is NOT the C1 closer. C1's substance already stands at ~1,728 filed verdicts (8.6× the MUST). B3's value is (a) the C4 estimator feed (nightly p50/p99 accumulation), (b) the standing regression floor (every incident a scenario, every night a re-proof), (c) the C2 rejoin-race OPERATOR port, and (d) the ON-report-latency distribution that CONFIRM-SOUNDNESS will learn from. H2's cadence half completes at the first digest.
-->

# Coding Task: B3 — BENCH-AUTOSTART (nightly suite + digest + quiescence-by-config-swap)

**Subsystem:** nexsys-bench (runner + tools + scenarios + constants). **Zero core changes.**
**Phase:** 3-Implementation (bench lane)
**Task Brief Reference:** v42 orchestrator charge 2 (pm-handoff v42 beat 1; the four quiescence amendments ratified at v41 beat 2)

## What This Implements

The evidence engine currently runs when a human runs it. B3 makes the nine-leg AUTO suite of record run itself nightly on the Pi against the deployed build, on a QUIESCED bench (bench-hero's config swapped out for the run, restored guaranteed), leaving one appended digest line per night that a tired human can read in three seconds, and a flight-recorder bundle for any leg that fails. The suite order is load-bearing: `command-s31-settle` runs LAST because it IS the park — the F-12 fix (the S31's confirmation clock starts on a report, never a command; ~22 h of overnight clears it; carrier: `scenarios/constants.yaml`, THE AUTO SUITE OF RECORD block — read it in full before writing anything).

## Files to Read Before Starting

| File | Why |
|---|---|
| `nexsys-bench/scenarios/constants.yaml` | THE AUTO SUITE OF RECORD block — the 9-leg order, the park mechanism, the same-day re-run trap, the margin watch. The suite list minted here (DP-1) is the single source of truth. |
| `nexsys-bench/tools/bench.sh` | The verb case statement (:67–:90), `api_token()` at :18 (a function, NOT a verb — F-1), `do_stop`/`do_start`/`do_health`, the runner delegation (`scenario|suite|bundle`). |
| `nexsys-bench/tools/runner/runner.py` + `engine.py` + `drivers.py` + `bundles.py` | Suite semantics, `BENCH_VERBS` (engine.py:35), fresh-boot precondition (`bench.sh restart`, engine.py:598-599), bundle-on-failure (`bundles.write_bundle`, engine.py:1413). |
| `nexsys-bench/tools/runner/README.md` | The desk dry-run (`--against`) + the REV2 sibling `.api.yaml` fixture mechanism — your desk-gate instruments. |
| `nexsys-bench/scenarios/SCENARIO_FORMAT.md` | Scenario grammar for the rejoin-race OPERATOR port (rider R2). |
| `nexsys-hivemind/context/process/bench-troubleshooting-playbook.md` §8 | The operator handoff contract — EVERY operator block in your return complies (self-contained, WHERE-label INSIDE as a leading comment, full paths, STOP-gates in their own blocks, expected tokens named, ⏺ paste-either-way). |

## STOP-on-Mismatch Gates

Read and verify BEFORE writing code; any divergence = STOP and report.

| File | Expected state |
|---|---|
| `tools/bench.sh` | Case verbs exactly: start, stop, restart, status, health, log, entities, runs, events, state, and the `scenario\|suite\|bundle` runner delegation. `api_token()` defined at ~:18 and NOT dispatched. |
| `scenarios/constants.yaml` | THE AUTO SUITE OF RECORD block present, RE-AMENDED 2026-07-31, `command-s31-settle` LAST in the 9-leg list. |
| `scenarios/` | Exactly 11 `.yaml` files incl. `usb-reenumeration-manual.yaml` (OPERATOR-tier — must NEVER enter the nightly). |
| `nexsys-bench/.gitattributes` | ABSENT (verified 2026-07-31 — rider R6 creates it). |

## Settled Decisions (NOT open questions — implement as stated; pushback per §Pushback)

- **DP-1 (the suite list is DATA, not prose):** mint `auto-suite:` as a REAL key in `scenarios/constants.yaml` carrying the nine legs in the ratified order (park LAST), placed adjacent to THE AUTO SUITE OF RECORD comment block (the block stays as rationale). The runner gains `bench.sh suite auto` which resolves the list FROM that key. **`suite all` (lexical) is UNLAWFUL for the nightly**: lexical order breaks the park-LAST law AND would drag `usb-reenumeration-manual` (OPERATOR-tier, headless-window hazard — the C-1 lesson) into an unattended run. `suite auto` must structurally refuse any OPERATOR-tier scenario (assert, don't assume).
- **DP-2 (the wrapper):** `tools/nightly.sh` — the nightly entrypoint the scheduler invokes. Shape: quiesce → verify-quiesced (anti-vacuous) → `<full-path>/bench.sh suite auto` → restore → verify-restored → digest append. **Restore runs under a shell `trap` on EXIT/INT/TERM — every exit path restores**, including a mid-suite crash. All bench operations go through `tools/bench.sh` (playbook law); the wrapper adds no second path to the app.
- **DP-3 (quiescence by config-swap — amendment (i), two branches PRE-RULED; the P-block discriminates):**
  - **Branch A** (bench-hero lives in its OWN file / an include-dir): quiesce = `mv` that file to `~/hs-bench/quiesce-hold/` → `bench.sh restart`; restore = `mv` back → `bench.sh restart`. Same-filesystem `mv`, atomic.
  - **Branch B** (bench-hero is a section of a single config file): maintain a GENERATED hero-less variant + a byte-copy of the live config it was derived from (`config.live-basis`). At swap time the wrapper `cmp`s live config vs `live-basis`: **equal → swap lawful; different → CONFIG-DRIFT: do NOT swap — run the suite UN-quiesced and flag the evidence class in the digest** (honesty over mechanism: a stale quiesced variant must never overwrite Nick's config edits). The hero-less variant is generated at install and re-generated by the operator whenever the live config changes; the wrapper never performs YAML surgery.
  - Both branches: **the quiesced state is ASSERTED with positive evidence (amendment (ii))** — after the quiesce restart, read the automations list via the ⛔PIN-2 instrument and record bench-hero ABSENT; after the restore restart, record bench-hero PRESENT. The restore-boot PRESENT read is the anti-vacuous pair proving the instrument works (a night where both reads return nothing is an instrument failure, not a quiet success). Both reads are captured to `~/hs-bench/nightly-logs/<date>-quiesce-evidence.txt`, and that file is copied into every failure bundle the night produces.
- **DP-4 (the digest — amendment (iii)):** ONE line appended per night to `~/hs-bench/digests/nightly.log`. First-position fields are the evidence class and the floor, and the line ALWAYS states restore status: `2026-08-01 quiesced AUTO floor: 9/9 PASS · bench-hero RESTORED ✓ · ON-latency 0.11s`. Failure form: `... 8/9 · FAIL command-confirm-s31 · bundle <path> · bench-hero RESTORED ✓`. Un-quiesced form leads `UNQUIESCED(CONFIG-DRIFT)`. **A line that cannot say `RESTORED ✓` is written as `RESTORE-FAILED ⛔` and is itself a red** — a crashed run leaving the bench quiesced silently starves the organic corpus C1 rides on. A missing digest line by morning = treat as red (state this in the I6 README). Add `digest` as a bench.sh verb: `~/nexsys-bench/tools/bench.sh digest [N]` = tail the last N (default 3) lines.
- **DP-5 (scheduler, two branches PRE-RULED; ⛔PIN-3 discriminates):** **REC systemd user timer** (`~/.config/systemd/user/` unit + timer, `Persistent=true`, journal capture) if user-lingering/systemd is available on the Pi; **fallback: cron** (`crontab -e` entry) if not. Fire time REC **03:30 America/Chicago** (deep-night, no occupancy, ≥22 h from any evening manual run; Nick may re-rule with one word). Wrapper logs to `~/hs-bench/nightly-logs/nightly-<date>.log` regardless of branch.
- **DP-6 (rider R1 — the ON-report-latency digest line, the margin instrument):** parse the night's `command-confirm-s31` evidence (the command status read's per-phase `lifecycle.<PHASE>.at` — the C4-measured surface) for DISPATCHED→CONFIRMED latency; append to the digest line AND to `~/hs-bench/digests/on-latency.log` (one timestamped value per night). This builds the distribution that adjudicates the margin watch (n=2 today: 111 ms and 3.8–5.0 s against a 5.369 s window) and feeds C4 + CONFIRM-SOUNDNESS. On a SKIP/FAIL night, append `n/a(<verdict>)` — never fabricate.
- **DP-7 (rider R2 — the C2 rejoin-race OPERATOR port):** author `scenarios/rejoin-race-operator.yaml` (OPERATOR tier — it needs hands: a device power-cycle timed against an in-flight command; NOT in the nightly). Class contract: a command issued while the target is mid-rejoin must terminal honestly (CONFIRMED only on real evidence, else TIMED_OUT/UNCONFIRMED) — never-false-CONFIRMED is the assert; the disposition is deliberately open. Ship it with a §8-compliant operator block (one act per line, expected tokens, timestamps-and-counts questions, ⏺ paste-either-way). It runs at an attended session before Aug-10; the scenario landing is B3's deliverable, the rep is the operator's.
- **DP-8 (riders R3–R6):** **R3 (I5):** re-mint the boot-demo fixture from a CURRENT 6-device-era captured boot log (the fixture must show `projection_live devices=6 entities=6 position=25065`); the P-block captures the slice. **R4 (I6):** the runner-demo README section gains the nightly story AND carries the SAME-DAY RE-RUN TRAP verbatim-by-pointer (constants.yaml block): a manual daytime `suite auto` fires `command-confirm-s31` against an uncleared clock — an EXPECTED red, not a regression; to re-run by hand: park manually, wait ≥2 min, then run. **R5 (F-1):** add `api_token` to the bench.sh case (dispatch the existing function) + the usage line — this is the verb the playbook's interim auth form has been waiting on. **R6:** create `nexsys-bench/.gitattributes` (`* text=auto eol=lf` + explicit `*.sh text eol=lf`, `*.py text eol=lf`, `*.yaml text eol=lf`, `*.md text eol=lf`) AND run a full-tree CR scan at desk (`git grep -I $'\r'` — expect ZERO hits; paste the empty result as the anti-vacuous pair with a deliberate positive control on a scratch file).

## ⛔PIN — MEASURE-THEN-PIN values (the desk pins these from Nick's P-block pastes; NEVER invent them)

| Pin | What | Instrument (P-block) |
|---|---|---|
| ⛔PIN-1 | The bench-hero config carrier: which file under `~/hs-bench/config/` holds the automation (Branch A vs B for DP-3) | `ls -la ~/hs-bench/config/` + `grep -l "bench-hero" ~/hs-bench/config/*` |
| ⛔PIN-2 | The automations-list instrument for the quiesce assert: the exact route + the field carrying the automation name (the rotation read of B2 P-4 proved the read exists — re-measure, don't recall) | one authed curl of the automations list, full body ⏺ |
| ⛔PIN-3 | Scheduler branch: systemd user session + lingering available? | `systemctl --user list-timers` + `loginctl show-user $USER --property=Linger`; on error → cron branch |
| ⛔PIN-4 | The current boot-log slice for the I5 fixture re-mint | the P-block's captured `projection_live` region |

These land as `quiesce:`/`nightly:` keys in `scenarios/constants.yaml` at the Pi-stage re-mint (the constants law: minted from the instrument, never from a report). The P-block itself (four read-only pastes, ~5 min, §8-compliant with WHERE-labels inside each block) is authored by the DESK as its first deliverable and handed to Nick — full paths, no placeholders without their own fill-in-before-running line.

## P2 Consumer/Pin Survey

- **The suite list** (the counted set): consumers = the constants comment block (rationale, stays), the NEW `auto-suite:` key (single source of truth), `suite auto` (reads the key), the I6 README (cites by pointer, never copies the list), the H2 ledger cell (definition of record — already re-amended). The wrapper NEVER carries the list. Zero other count-pins on suite size found in `tools/` at baseline — re-grep at execution.
- **bench.sh verbs** (byte-frozen operator vocabulary law): additions are ADDITIVE only (`api_token`, `digest`); the usage lines update in the same edit; zero existing verb lines change byte-wise.
- **`usb-reenumeration-manual.yaml`**: a NEGATIVE consumer — `suite auto` must provably exclude it (the OPERATOR-tier refusal assert).
- **The park's dependency premise** (bench-hero commands ONLY the Hue — zero S31 references in the live config): re-verify in the P-block grep (PIN-1's grep doubles as this check; expect bench-hero's file to reference Hue, not the S31 ULID).

## Red-First Predictions

Desk gates that must go RED before the change and GREEN after: (1) `bench.sh suite auto` — errors at baseline (no such subcommand/key), resolves the 9-leg park-LAST order after; assert the resolved order EQUALS the `auto-suite:` key order and REFUSES an OPERATOR-tier name injected into a scratch copy of the key. (2) The digest formatter unit check (a `--against`-style dry invocation or a pure-function test in the runner) — red at baseline (no formatter), green after, covering PASS / FAIL / UNQUIESCED / RESTORE-FAILED forms. **Green-by-construction, disclosed:** the CR scan (R6) — the tree is already LF-clean at `8bce651`, so the scan passes at baseline BY CONSTRUCTION; its value is the ratchet plus the positive control. The rejoin-race scenario has NO desk-green path (OPERATOR tier) — its desk gate is load-only (`suite` listing shows it REFUSED for auto, loadable for scenario).

## What to Watch Out For

- **Restore is the invariant, not a step.** The `trap` must fire on EVERY exit path including the engine hanging past a timeout you set (wrap the suite call in `timeout`, generous — the 9 legs run ~6–10 min on record; REC 45 min ceiling). If restore itself fails, say so loudly (`RESTORE-FAILED ⛔` digest line + nonzero exit) — never silently exit quiesced.
- **The engine restarts the app itself** (boot-health's fresh-boot precondition runs `bench.sh restart`). That is LAWFUL under quiescence — the hero-less config persists across restarts because the swap is on-disk. Do not "fix" it.
- **Timer-vs-park interaction:** `Persistent=true` (systemd catch-up after a powered-off window) can fire a run at an odd hour after downtime — acceptable (the park cleared during the downtime), but the digest timestamp will show it; no special handling.
- **No tokens in pastes, logs, or the return** (L3): the wrapper reads the token via `api_token()`/the new verb, never echoes it; the P-block curl uses the playbook's inline-substitution form.
- **Desk cannot execute live `api:` asserts** — the quiesce-assert logic desk-tests via the REV2 sibling `.api.yaml` synthetic-response mechanism if you add a fixture, or defers to the Pi install's first attended run; state which in the return.
- **`date`/locale on the Pi:** digest dates in ISO (`date +%F`), local Pi time; one line per night — append-only, never rewrite the file.

## Out of Scope

HUE-RESET (parked through the gate, tripwire pre-ruled) · un-SKIPping `command-confirm` · the composition-tier suite (post-gate charter) · CONFIRM-SOUNDNESS learning (charter) · the playbook interim-auth-form ⛔EXPIRED stamp (hub-owned, docs fold, after R5 lands) · ANY core/homesynapse change · STATE-DIALECT and its scenario sweep (charge 5's WU).

## Success Criterion (binary)

DONE when: (1) the P-block pastes are filed and all four ⛔PINs are minted into constants; (2) the desk gates above are green with the red-first evidence pasted; (3) the Pi install is complete — wrapper + scheduler branch installed, **night-1 bootstrap executed (park once by hand: `~/nexsys-bench/tools/bench.sh scenario command-s31-settle`, then enable the timer)**; (4) **the first nightly digest line exists and reads `quiesced` + `9/9 PASS` (or SKIP-honest-adjusted `8/9 + SKIP`) + `RESTORED ✓`** with the quiesce-evidence file showing the ABSENT/PRESENT pair; (5) the return is filed at `context/audits/2026-07-31_B3_return.md` with the census-exact file list; (6) commits are ORDERED by the hub after audit — the lane commits nothing.

**Expected first-night shape while HUE-RESET is pending: `command-confirm` SKIP-honest on `[hue-online]`, every other verdict decisive — so the honest first digest is `8 decisive PASS + 1 SKIP(hue-online) · RESTORED ✓`. A `command-confirm-s31` red WITH the park verified is the margin watch expressing itself (constants block): it trips the pre-ruled HUE-RESET contingency — flag to the hub, never retry-loop.**

## Coder Pushback Welcome

If the wrapper/scheduler split, the drift-guard mechanism, the digest grammar, or the `suite auto` refusal shape is impractical or you see a cleaner mechanism with the same contracts — raise it with evidence before implementing. You see the runner's internals; the hub ruled contracts, not data structures.

## Build Discipline & WUCP

You produce files; no commits (the hub orders them post-audit with explicit paths + exact counts). Desk gates are the runner dry-runs above — there is no Gradle in this repo. WUCP Phase 1 applies (coder-handoff entry + lessons if any); the return carries the full file census and every operator block you authored.

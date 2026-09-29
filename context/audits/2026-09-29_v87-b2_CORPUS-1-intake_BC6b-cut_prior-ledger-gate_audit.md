<!--
file: context/audits/2026-09-29_v87-b2_CORPUS-1-intake_BC6b-cut_prior-ledger-gate_audit.md
purpose: v87 beat 2 — CORPUS-1's three lines intaken at the bytes (the bench landing, the corpus copy, BENCH-PULL-4); BENCH-CORE-6b cut as the pinned transform of BC6 through THE PRIOR-LEDGER GATE, with the harvest dry-run on BC5's outputs listed as the law requires; the hand.
audience: the v87 hub · the v88 boot (by §0) · the BC6b guide (it never reads this; the card is whole)
state-type: audit (an intake + a cut through the gate)
status: FILED — Tue 2026-09-29 ~17:1x CT (instrument 2026-09-29T22:11:49Z)
-->

# v87 beat 2 — CORPUS-1 intake · BENCH-CORE-6b cut through the prior-ledger gate

## §0 Verdict
**CORPUS-1 ACCEPT** — three lines, each re-executed at the instrument (§1). **BC6b CUT and DISPATCH-READY** — the gate clean on eight new strings, the one hit (`behind`) the read being replaced; fourteen harvest filters non-zero on BC5's outputs; the new filter verified on a live checkout (§2). BC6 SUPERSEDED. The hand: BC6b, a fresh guide conversation, ≤ 20:15 CT start (§3).

## §1 CORPUS-1 — the intake (Layer 1 Nick's transcript; Layer 2 the hub's re-execution)
| Line | Claimed | Re-executed |
|---|---|---|
| `CORPUS-1: copied 4/4` | `equal: 4/4`; four `??` under `corpus/runs/2026-09-28_rehearsal-1/` | sha256 of each of MANIFEST.txt · window.json · verdict.json · report.md equal between `_archive/runs/2026-09-28_rehearsal-1/` and the bench tree |
| `BENCH: LANDED d093a95 (CORPUS-1)` | `staged: 4 (expect 4)` · grep 0 · `352296d..d093a95 main -> main` | `git log -1`: `d093a95` Nick Smith 2026-09-29T17:00:43-05:00 `bench(corpus): CORPUS-1 — …`; `4 files changed, 1525 insertions(+)`; trailers 0; porcelain 0; ahead 0 |
| `BENCH-PULL-4: d093a95 · 42/0 · 26/0` | `=== BP4 2026-09-29T22:01:04Z` · hs-dev-1 · before 352296d · porcelain=0 · Fast-forward · after d093a95 · 42/0 · 26/0 | the outputs file `_scratch/v86/2026-09-28_BENCH-PULL-4_outputs.txt` (308 B): the four markers present (`Fast-forward` · `after: d093a95` · `42 check(s), 0 failure(s)` · `26 check(s), 0 failure(s)`); copied verbatim into `context/audits/2026-09-29_BENCH-PULL-4_outputs.txt` |
Form notes (no deviation in the acts): the card was run by Nick directly and the transcript pasted (§0 (iv) asks for the three lines; the outputs file was teed as the card orders, so the record did not depend on the paste); Block 1's commit used the pre-IR-101 `;` form — the census held (4 = 4). The Pi's ssh timestamp `22:01:04Z` is UTC (the card's `date -u`), = 17:01 CT. Not re-executed: the Pi's selftest lines (read from the teed file, written by the Pi).

## §2 BENCH-CORE-6b — the cut through the gate
**Why a re-cut (D-v87-4):** BC6's Block 0 EXPECTED `behind=2` (now 4) and Block 2's `git pull --ff-only` would have built `8deef4b` — PJ-2's core — on the bench card before BH-3 (THE BENCH FENCE, D-v85-10).
**The transform** (`_scratch/v87/v87b2_bc6b.py`; every anchor `once`-asserted; 18,291 → 19,861 B; the six block headings each once; residual `BENCH-CORE-6` mentions only in the frontmatter's pointers): the D-v87-10 list — Block 0's pinned reads (`target=` · `target-ahead-of-clone=` · `main-ahead-of-target=` · `ref=`; EXPECTED `commit · 2 · 2 · main`), Block 2's `fetch` + `checkout --detach 40412f9` (EXPECTED `HEAD is now at 40412f9 …`), the Tuesday log globs in 0b and 4, the nightly line written whole (the `NIGHTLY:` word), `d093a95`, Wed's timer, the v87 paths, the STATE line, the one line back.
**THE PRIOR-LEDGER GATE (law 15; #31) — the greps, listed.** Files: `context/audits/2026-09-27_BENCH-CORE-5_guide-notes.md` · `…/2026-09-27_v83-b4_BC5-intake_the-close_audit.md` · `…/2026-09-28_v84-b4_Monday-morning_nightly_BENCH-PULL-2_PI-PROBE-2_intake_audit.md` · `…/2026-09-28_v85-b3_BENCH-CORE-6_cut_prior-ledger-gate_audit.md` (`grep -ci`, summed): `detach` 0 · `checkout` 0 · `cat-file` 0 · `HEAD is now` 0 · `fetch` 0 · `pinned|pin ` 0 · `origin/main` 0 · `nightly.log` 0 · `behind` 3 (BC5 B0: `behind=1 ahead=0`, "match; no STOP condition" — the read this cut replaces; carried as the named change) · `bench-2026` 5 (the glob form, unchanged). No deviation to carry beyond the replaced read. BC6's own gate (v85 b3 §1) stands for the unchanged blocks.
**THE HARVEST DRY-RUN** on `context/audits/2026-09-27_BENCH-CORE-5_outputs.txt` (8,352 B; `grep -ciE`): `fast-forward|up to date|updating|fatal|error|abort` 2 · `BUILD SUCCESSFUL` 1 · `stopped|launched|RADIO UP` 3 · `boot-health` 2 · `network_resumed` 2 · `device_announce|device_relinked|device_join` 21 · `PLUGS@` 2 · `permit_join_opened=` 7 · `nightly:` 1 · `integrity_check|^ok` 2 · `BUILD pid=` 1 · `jvm pid=` 1 · `clone: ` 2 · `porcelain=` 1 — every filter the card reuses returns lines from the prior record; BC5's harvested `nightly:` line (`2026-09-27 quiesced AUTO floor: 8/9 PASS · 1 SKIP(hue-online) · fleet: 9/9 · re-seen 9 · …`) is the shape Block 0b will write. The NEW filter (`HEAD is now|previous HEAD|fatal|error`) dry-run on a live `git checkout --detach` in a scratch repo: `HEAD is now at <sha> <subject>`, grep exit 0; `git rev-parse --abbrev-ref HEAD` = `HEAD`; `git cat-file -t <sha>` = `commit`.
**The detached clone and the nightly:** `git -C nexsys-bench grep -iE 'git pull|git checkout|homesynapse-core'` — `tools/bench.sh:7` names the installed launcher only; `tools/nightly.sh` carries neither verb; the clone's ref is touched by no scheduled job. BH-3's card returns it to `main`.
**Carried, known:** Block 2's filter admits a `fatal`/`error` line and the `&&` chain then starts the build (BC6's form; BC5's before it) — the guide's STOP is the control; Block 0's porcelain=0 makes a checkout failure improbable.

## §3 The hand
BC6b — the card pasted WHOLE into a FRESH conversation with `ClaudeFolder` connected; the guide asks `STATE: BENCH-PULL-4 said d093a95 · the time is <HH:MM CT>` before Block 0; ≤ 20:15 CT start; the rig exclusive until the one line (`BENCH-CORE-6b: deployed 40412f9 (pinned) · …`) or a STOP. The hub's desk meanwhile: Phase 2 for PJ-2, the 1b H10, THE STRATEGY PASS.

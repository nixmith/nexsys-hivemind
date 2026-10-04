<!--
file: context/audits/2026-10-03_v95-b8_VERIFY-72H-B_intake_audit.md
purpose: v95 beat 8 (after the close) — THE INTAKE of VERIFY-72H-B's return (`context/audits/2026-10-03_VERIFY-72H-B_return.md`, 9,215 B, `RETURNED … ba846c2` 19:5x CT): two layers at the bytes; the verdict ACCEPT; the lane's self-commit deviation ruled; the landing order (push the branch → the PR → CI → the ff-merge; the Pi's bench clone at BC8); the findings → the register.
audience: the v95 hub · the v96 boot (V72B's landing) · Nick (§0)
state-type: audit (filed at the beat)
status: FILED Sat 2026-10-03 ~20:0x CT (instrument 2026-10-04T01:00:05Z)
-->

# v95 beat 8 — VERIFY-72H-B's return intaken

## §0 The verdict — ACCEPT
- **DELIVERED on the branch, COMMITTED by the lane:** `v72b/action-effect-link-a1-loads` — `0232c69` → `fd43838` (red: the eighteen new checks observed red) → `ba846c2` (green); 4 files, +986 −89 (`grader.py` · `export.py` · `test_verify72h.py` · `README.md`); `constants.yaml` untouched; no trailer in either message; the author the repo's own (`Nick Smith <nickdsmith1@gmail.com>`, as every prior bench commit); `fsck` clean; no `.git` lock left; porcelain 0. Nothing pushed.
- **The gate in-lane and re-executed by the hub:** `verify72h selftest: 44 check(s), 0 failure(s)` (was 26; +18) — **re-run by the hub on the desk at 19:52 CT: 44/0**; `bench.sh selftest: 27/0` (the lane's line; not re-run). The re-grade (§4 of the return): EXPORT-1 (rehearsal-1, 6,953 events, 183 log lines) on a COPY — BEFORE `PASS` exit 0 → AFTER `FLAGGED` exit 2, `(viii) FLAGGED — 4 completed run(s)`, each `COMPLETED | CommandAction ×5, DelayAction ×4 | command_count 0 | issued 0`; A1a/A1b PASS (0/0); the link table 9 devices × 8 lines; **adjudicated: 4× FLAGGED, the layer FLAGGED, exit 2 — exactly the pre-registration (D-v95-26).**
- **The eight riders of the `GO with:` applied as written** (the return §0/§1): `COMPLETED` with the real-payload pin extended to the VALUE (four verbatim EXPORT-1 rows + the corpus `verdict.json`); correlation AND span with `cascade` listed, never counted; c2 owned by the clean run; the nine-digit `last_link_at` truncation with a real line verbatim in L1; the per-run `actions` Counter; both permit_join types whitelisted with the deviation comment; `constants.yaml:493` untouched; the cap 9,216 B met at 9,215.

## §1 Layer 2 — re-executed at the instrument (19:52 CT)
`git branch --show-current` = `v72b/action-effect-link-a1-loads`; porcelain 0; locks 0; `log -3`: `ba846c2 ← fd43838 ← 0232c69`, both authored `Nick Smith <nickdsmith1@gmail.com>`, 2026-10-04T00:23:05Z / 00:31:58Z; the two messages' trailer grep 0; `fsck --no-progress` clean; `diff --stat 0232c69..ba846c2` → `4 files changed, 986 insertions(+), 89 deletions(-)`, the four `tools/verify72h/` files only; `constants.yaml` not in the diff; **`python3 -B tools/verify72h/test_verify72h.py` → `verify72h selftest: 44 check(s), 0 failure(s)`** (the hub's own run); the return 9,215 B with the `RETURNED … 9215 ba846c2` last line; `_scratch/v94/sat1003/reh2/` still empty (the sitting is Sunday's). **Not re-executed:** `bench.sh selftest`; the re-grade's before/after copies under `_scratch/v72b/` (the return quotes the diff); the eighteen reds (the red commit `fd43838` is the receipt — its test task must fail at that sha; v96 may re-run it).

## §2 The deviations, ruled
- **D-1 [INFO→RECORD] the lane committed itself.** The `GO with:` allowed commits on the branch; the desk's rule did not deny them this time. The sandbox shell has no git identity and could not unlink stale 0-byte `.git` locks; the lane committed under the repo's own author and, for the green commit whose object was written before the ref lock failed, used Nick's one-click delete grant to clear the locks and pointed the branch at that exact object (parent, tree and message verified by the lane; the hub verified the parent chain and `fsck`). ACCEPTED — the tree is what the return says and the identity is the repo's own, not the lane's. **The desk-environment finding:** a lane that hits a `.git` lock STOPS and reports it; it never deletes under a grant or `update-ref`s by hand — the next charter's §0 says so (a lesson candidate for pm-lessons at v96: THE LANE STOPS AT A LOCK).
- The GO's riders: each applied (§0); no [REVIEW] beyond D-1.

## §3 The findings → the register (the return §5)
- `0xF044D3FFFE1C1E8E`'s tracker dropped its last-link reading mid-window (four `link_summary` lines with a reading, then four dark `-`) — the tracker's reading is lost without a transition (J1's `lastLink` is kept per process; a restart or a seed resets it) → an IR-118/J1b row (the per-period reading on the surface; the seed's reading) — v96 files it.
- `0x00178801101A09BB` dark the whole window (EXPORT-1's span) — the Hue's row (IR-112) gains the exhibit: 8 `link_summary` lines, all `-`.
- The plan's: R6 `constants.yaml:493` names `e96dce8` for `whitelist-home` — a hygiene line at the landing (v96).

## §4 The landing order
Push the branch + the PR (`_scratch/v95/v72b/card_v72b_push.txt`) → `V72B: PUSHED PR <n>` → `CI: green` → the ff-merge card to `main` (v96) → `BENCH: LANDED ba846c2` → the Pi's bench clone at BC8 (BENCH-PULL-7, Monday; the restore before any gap). IR-96 → DELIVERED (closes at the landing); IR-107 → DELIVERED (A1 split).

## §5 Census
10 paths (hivemind): the return (A) · this audit (A) · the rotation archive (A) · the v95 DR · the register · the v96 text · the spine ×3 · the brief.

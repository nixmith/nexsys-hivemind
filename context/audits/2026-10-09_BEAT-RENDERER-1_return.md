<!--
file: context/audits/2026-10-09_BEAT-RENDERER-1_return.md
purpose: BEAT-RENDERER-1's return — U1 + U2 DELIVERED in the worktree; STAGED, never committed.
audience: the hub (two-layer intake at the bytes) · Nick (the landing card)
state-type: lane return
status: RETURNED — Fri 2026-10-09 ~12:3x CT (start 2026-10-09T17:07:39Z · close 2026-10-09T17:30:05Z)
-->
# BEAT-RENDERER-1 — return (U1 + U2)

## §0 The card — DELIVERED
- **Where:** worktree `~/Desktop/Code/ClaudeFolder/nexsys-hivemind-renderer` (D-v101-6) · branch `beat-renderer-1/state-file` · base `513d1c0` · zero commits · staged=11 (ten + this return) · `nexsys-hivemind` untouched.
- **Tests** (`python3 -B context/process/…`): `render_state.py --selftest` → `render_state selftest: 2 check(s), 0 failure(s)` · `--check` → `MATCH snapshot-digest 1865 ≤ 2048` · `MATCH snapshot-file 3477 ≤ 3500` · `MATCH brief-digest 2046 ≤ 2048` · `MATCH brief-file 12164 ≤ 12288` · `test_render_state.py` → `render_state tests: 13 check(s), 0 failure(s)` · `test_splice_lib_v3.py` → `splice_lib_v3 selftest: 5 check(s), 0 failure(s)`.
- **RED first:** test_render_state with no templates → `render_state tests: 13 check(s), 10 failure(s)` (`FileNotFoundError: … templates/snapshot_digest.tpl.md`; `--selftest` the same); test_splice_lib_v3 against v3 assembled WITHOUT its beat() section → `splice_lib_v3 selftest: 5 check(s), 4 failure(s)` (`AttributeError: module 'splice_lib_v3' has no attribute 'beat'`).
- **`diff --cached --stat`** (before this return): `10 files changed, 737 insertions(+)` — fixtures 5+ · 5+ · 86+, `render_state.py` 129+, `splice_lib_v3.py` 230+, templates 5+ · 5+, `test_render_state.py` 87+, `test_splice_lib_v3.py` 99+, `state.yaml` 86+.
- **The spine:** the four files' md5 == `git show 513d1c0:` (aceba411 · e6391808 · 2fba61ad · 3d47b6d6); `splice_lib_v2.py` `99e87f2dbafaade35e071770b14b5557` after; v3 `fc79eee9d1af94e424e1560856c8b3f2` (its callers' pin); no `__pycache__`; porcelain at close = eleven `A ` rows.
- **LOCKS (a line, not a sweep):** `.git/worktrees/nexsys-hivemind-renderer/HEAD.lock` · `.git/refs/heads/beat-renderer-1/state-file.lock` — zero-byte residue of the lane's OWN first act (the bridge forbids deletes; the `locked` marker likewise). Not the hub's; untouched; they block only the landing commit — clear both before the card. Also 9 `.git/objects/*/tmp_obj_*` from the `git add` (216 in all); `objects/maintenance.lock` pre-existed.
- **§0b at 513d1c0 (the worktree):** 1 `513d1c0` · `0` ✓ · 2 `99e87f2dbafaade35e071770b14b5557` ✓ · 3 `23` · `79 85 91 98 108` ✓ · 4 `CHAIN_CAP, BEAT_CAP, SNAP_CAP, BRIEF_CAP, LIVE_BEATS_CAP = 3000, 2500, 3500, 12288, 12` ✓ · 5 `8 10 14` · `1865 3477` ✓ · 6 `11:## §DIGEST — where` · `16:## §NEXT — the b3` · `21:## §HELD-BY-THE-HUB` · `41:## §DONE — the led` · `44:## §WHAT YOU DO NOT`; §DIGEST 2046 ✓ · 7 `last-verified: ` · `2` · `76` · `12` (at cap; the next insert rotates) ✓ · 8 `261` · `0a` ✓ · 9 `Python 3.10.12` · `6.0.3` · `0` ✓.

## §1 What changed (ten paths added, zero modified)
- `context/status/state.yaml` (5670 B; 58 scalars, each a verbatim substring of the regions; every string double-quoted; no anchors/flow/multi-line; the header names the renderer, the anchors, THE RULE). Keys: `beat{label,headline}` · `shas{core,core_note,bench,docs,skills,hivemind}` · `pi{running,carries,target_by,target}` · `counter` · `fleet{registry,on_air,note}` · `lanes[{name,state,next}]` · `lanes_note` · `words{given,open}` · `week_ruling` · `week[]` · `dates[]` · `next_acts[]` · `open_risks` · `notes[]` · `brief{beat,ct,notes[],core_note,fleet_note,after_state,tonight,week[],yours[]}`.
- `templates/snapshot_digest.tpl.md` (24 slots) · `brief_digest.tpl.md` (15): `@@key@@` slots (nested keys by `.`). THE ONE LIST MECHANISM: `sep.join` into the key's slot, the separator per key in `render_state.SEPS` (`notes` " " · `week`/`dates`/`brief.*` " · " · `next_acts` " → "); `lanes` rows render `name` + ` (next)` and join by state into `lanes.ready` / `lanes.running` (`none` when empty).
- `render_state.py`: `--selftest` · `--check` · `--write [--snapshot --brief]`; paths from its own location; v2's `fill()` (unfilled slot refused), `no_trailers`, `wr` (its md5 asserted); `SNAP_CAP`/`BRIEF_CAP` imported, `DIGEST_CAP = 2048` named once; a DIFF names the first differing byte; every cap in `splice()` before `write()` touches a file.
- `fixtures/v99b1_*`: the state (= the live one) and both regions by `git show 513d1c0:` cut at the anchors (1865 · 2046 B).
- `splice_lib_v3.py` (18529 B): an 11-line v3 header + the bytecode line + v2 VERBATIM (header included) + `live_blocks()` · `rotate_beats()` · `render_regions()` · `beat(ctx)` — `diff v2 v3` is pure addition.

## §2 The tests
- test_render_state (13): fixture snapshot/brief byte-equal · over-cap snapshot-digest / brief-digest / snapshot-file REFUSED, md5s unchanged · safe_load round-trip · unfilled slot refused · every scalar verbatim · `write()`/`--write` on copies == fixture bytes · `--selftest` · `--check` 4 MATCH · no `__pycache__`; the live md5s asserted after each write.
- test_splice_lib_v3 (5): v2 carried byte for byte · case 1 the insert at live 11 (a throwaway `git init` in the temp dir: census `(3, 3, 0, 0)`, the card) · case 2 the rotation at 12 → `archive/pm-handoff-beats-v98b1-v99b1-rotated-2026-10-09.md`, the six oldest verbatim newest-first, kept + body + 1 = before, the map row, live 7 · case 3 `seg0 → Prior → the pointer` (two `once()` edits), the archive 261 → 262, the snapshot chain · case 4 a 2561 B block REFUSED `CAP beat 2561 > 2500`, every md5 and the listing unchanged.

## §3 Deviations
- [INFO] §6's `MATCH snapshot-digest <n> ≤ 3500` prints as two lines — the body against DIGEST_CAP 2048 (row 5), the file against SNAP_CAP 3500.
- [INFO] At 513d1c0 the brief's §DIGEST stood at v100 b1, the snapshot's at v100 b3 → a `brief:` subtree for the brief's prose; shared facts top-level. `words.given/open` unused at this sha (no WORDS line in either region) — `--check` prints `INFO unused keys`.
- [INFO] Rotation bytes kept + body + 1 = before (v99 b2's form); the map row defaults to the map's LAST row (`map_anchor` reproduces v99 b2's). The lock rule read as "a lock the lane MEETS" (both are its own first act's residue): proceeded, touched nothing, told Nick.
- [REVIEW] BEAT-RENDERER-2: §HELD needs the ledger rows as `[{id, state, owner, since, next}]`, the words banked/open as lists, the status line's beat + CT, a whole-region re-render; the card dry-run tool (D-v94-16) untouched. The `--check`/`--write` CLI cases read the LIVE state: green only while THE RULE holds.

## §4 Findings for the register
- F1 pm-handoff `:8` pointer stale: `… v99 b2 ROTATED` / `258 rotations through v99 b4; the v99 b3 segment …` while the archive holds 261 headings and seg1 is v100 b2 — the v100 beats rotated without the pointer's `once()` edits; the hub corrects by id.
- F2 the archive map's LIVE sentence (`v83 b2 → the newest, at 2026-09-28`) is stale since v85. F3 §DIGEST is 2046/2048.

## §5 At a beat (five commands, in order)
1. `python3 -B context/process/render_state.py --check` — the premise: 4 MATCH (a DIFF = a hand edit since the last render).
2. Edit `context/status/state.yaml` by hand.
3. The beat script: `assert lib.lib_md5() == "fc79eee9d1af94e424e1560856c8b3f2"; out = lib.beat(ctx)` with `state_path` — everything in one; the card is `out["card"]`; without beat(): `render_state.py --write`.
4. `python3 -B context/process/render_state.py --check` → 4 MATCH on the written files.
5. `python3 -B context/process/test_render_state.py && python3 -B context/process/test_splice_lib_v3.py` → 13/0 · 5/0; then the card.

## §6 Instrument limits
The Cowork bridge (no delete → the lock and tmp_obj residue); no Pi, ssh, push or merge; `date -u` at start and close; bytes by `len(str.encode("utf-8"))`.
RETURNED context/audits/2026-10-09_BEAT-RENDERER-1_return.md 8172 beat-renderer-1/state-file staged=11

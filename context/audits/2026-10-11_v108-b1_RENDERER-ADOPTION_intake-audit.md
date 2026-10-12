<!--
file: context/audits/2026-10-11_v108-b1_RENDERER-ADOPTION_intake-audit.md
purpose: The two-layer intake audit of THE RENDERER'S ADOPTION at v108 beat 1 (IR-150; D-v105-13; D-v107-29; D-v108-3..5): the instrument's own lines (the render log, verbatim), what the hub re-executed, what it could not, and the acceptance — `render_state.py --check` 7 MATCH on the live spine before and after the beat's splice.
audience: the v108 hub · the v109 boot (the first `--check` at boot reads against this) · a skills pass folding IR-150's Check-13
state-type: intake audit (closed at the beat; §6 appended by the same script after the splice)
status: FILED v108 beat 1 (Sun 2026-10-11 ~19:2x CT; instrument 2026-10-12T00:24:23Z)
-->

# v108 b1 — THE RENDERER'S ADOPTION, two-layer audit

## §0 The acceptance
`PYTHONIOENCODING=utf-8 python3 -B context/process/render_state.py --check` → **7 MATCH** on the live spine (`snapshot-digest` · `snapshot-file` · `brief-status` · `brief-digest` · `brief-held` · `brief-words` · `brief-file`), read twice: after `--write` (§2) and after the beat's splice (§6). The prose is not the acceptance; these lines are.

## §1 The before reading (Layer 2, the hub's own run at `fa140ab`)
`--check` against `state.yaml` v2 (= the v104b1 fixture, md5 `604fdf684d0235841b3833000112be79`): DIFF ×7 — `snapshot-digest 1776 ≤ 2048 at byte 18` · `snapshot-file 3215 ≤ 3500 at byte 1457` · `brief-status 262 at byte 30` · `brief-digest 1230 ≤ 2048 at byte 78` · `brief-held 3841 ≤ 6144 at byte 19` · `brief-words 2031 at byte 51` · `brief-file 12276 ≤ 12288 at byte 767`. `--selftest` 5/5. The live regions measured by anchor: brief-digest 1,224 B · brief-held 4,597 · brief-words 748 · snapshot-digest 1,972 (the snapshot 3,411 B; the brief 11,710 B).

## §2 The procedure, as run (the render log `_scratch/v108/b1/render_log_b1.txt`, verbatim)
```
## 2026-10-12T00:17:21Z --check BEFORE (the live regions at fa140ab vs state.yaml v3)
DIFF snapshot-digest 1950 ≤ 2048 at byte 18: got b'8 b1, THE ADOPTION \xe2\x80\x94 t' want b'7 b5, THE CLOSE \xe2\x80\x94 Mond'
DIFF snapshot-file 3389 ≤ 3500 at byte 1457: got b'8 b1, THE ADOPTION \xe2\x80\x94 t' want b'7 b5, THE CLOSE \xe2\x80\x94 Mond'
DIFF brief-status 271 at byte 30: got b'8 beat 1, THE ADOPTION (' want b'7 beat 5, THE CLOSE (Sun'
DIFF brief-digest 1563 ≤ 2048 at byte 78: got b'8 b1, Sun 2026-10-11 ~19' want b'7 b5, the close, Sun 202'
DIFF brief-held 4375 ≤ 6144 at byte 19: got b'8 b1, Sun 2026-10-11 ~19' want b'5 b5, Sat 2026-10-10 ~21'
DIFF brief-words 733 at byte 81: got b'b1 card) \xc2\xb7 `HERO-U3: RE' want b'close card) \xc2\xb7 `HERO-U3:'
DIFF brief-file 11854 ≤ 12288 at byte 767: got b'8 beat 1, THE ADOPTION (' want b'7 beat 5, THE CLOSE (Sun'
exit=1
## 2026-10-12T00:17:21Z --probe
PROBE snapshot-digest 1950 ≤ 2048
PROBE snapshot-file 3389 ≤ 3500
PROBE brief-status 271
PROBE brief-digest 1563 ≤ 2048
PROBE brief-held 4375 ≤ 6144
PROBE brief-words 733
PROBE brief-file 11854 ≤ 12288
PROBE OK — nothing written
exit=0
## 2026-10-12T00:17:21Z --write (ONCE)
WROTE /sessions/rcw-01tiyupzaexfl8c59p6i1o12/mnt/ClaudeFolder/nexsys-hivemind/context/status/PROJECT_SNAPSHOT.md 3389
WROTE /sessions/rcw-01tiyupzaexfl8c59p6i1o12/mnt/ClaudeFolder/nexsys-hivemind/context/handoff/OPERATOR-BRIEF_for-Nick.md 11854
exit=0
## 2026-10-12T00:17:21Z --check AFTER --write
MATCH snapshot-digest 1950 ≤ 2048
MATCH snapshot-file 3389 ≤ 3500
MATCH brief-status 271
MATCH brief-digest 1563 ≤ 2048
MATCH brief-held 4375 ≤ 6144
MATCH brief-words 733
MATCH brief-file 11854 ≤ 12288
exit=0
## 2026-10-12T00:17:37Z test_render_state.py
ok   --check against the worktree's files: 7 MATCH
ok   NEW the file caps imported, HELD_CAP and DIGEST_CAP named once
ok   no __pycache__ in the tree
render_state tests: 32 check(s), 0 failure(s)
exit=0
## 2026-10-12T00:17:40Z test_splice_lib_v4.py
ok   case 3 - a trailer in the message: no commit, nothing staged
ok   case 4 - a stale empty .git/index.lock: no commit, nothing staged
ok   case 5 - the wrong HEAD in a poisoned shell (N, T, M stale; the n paths pre-staged): no commit; the control without unset commits; the right sha on a non-main branch: no commit
splice_lib_v4 selftest: 5 check(s), 0 failure(s)
exit=0
## 2026-10-12T00:17:41Z test_splice_lib_v3.py (the IR-151 state)
FAIL case 3 — the chain split and re-cut: seg0 → Prior → the pointer; the archive +1; the snapshot chain: AssertionError: last-verified: 2026-10-11 (v107 beat 5, THE CLOSE — `HIVE: LANDED f25d
ok   case 4 — a block over BEAT_CAP REFUSED; every copy's md5 and the listing unchanged
splice_lib_v3 selftest: 5 check(s), 3 failure(s)
exit=1
## v99b1 readers outside the fixtures themselves: context/process/test_splice_lib_v3.py 
## test_splice_lib_v3 readers: context/process/test_splice_lib_v3.py
```
The state file passed through the window once as an authored file plus three targeted edits under `--probe` (the first probe REFUSED `CAP snapshot-digest 2214 > 2048`; the second passed at 2,041/3,480 — too close to the file cap for the chain's growth; the third at 1,950/3,389).

## §3 Layer 1 — the claims read critically
- BEAT-RENDERER-2's return §5 names the beat's order (`--check` · edit the state · `--probe` · `--write` · `--check` · the splices · `beat()` · the card pinned to v4). Followed, with one addition the return does not state: `--check` runs again AFTER `beat()` (§6), because `beat()` re-renders the regions from the state and the snapshot's chain line changes beside the digest — the second reading proves the two writers agree at the bytes.
- IR-150's row names the adoption's inputs (33 keys, 10 held rows; `--write` before `beat()`; the card pinned to v4 `bc10cd3f5f142e52f64a84c477fcbbee`). The state file keeps v2's key set exactly (no template changed); the pin is asserted at the splice's load.
- IR-151's two options (re-pin or retire): retire, D-v108-4 — the re-pin would go red at this very beat's chain change.
- IR-152: the three fixtures' readers after the removal = 0 (`grep -rln v99b1 context/process` minus the fixtures themselves = `test_splice_lib_v3.py` only, itself removed).

## §4 Layer 2 — re-executed by the hub
- The four instrument runs above (DIFF ×7 → PROBE OK → WROTE ×2 → 7 MATCH), `test_render_state.py` 32/32, `test_splice_lib_v4.py` 5/5, `test_splice_lib_v3.py` 3 of 5 red (the IR-151 state reproduced, not inferred).
- The dispatch text: line 9 opens `You are the **v108 PM MISSION-CONTROL hub**`; nine distinctive phrases found once each; 13,430 B from line 9 (D-v108-2).
- The five HEADs and porcelains; Check 9 at the bytes (28/28); the `prunable` flag on the hero-u3 worktree explained at the instrument (the `.git` file's Windows path), not accepted as a fact about Nick's desk.

## §5 Disclosed — NOT re-executed
- The hero-u3 worktree's git state (branch, porcelain) from this mount — unreadable here (D-v108-6 (b)); Nick's `WORKTREE: hero-u3 2a54145` and the core's `git worktree list` stand as the record.
- The Pi (`37f05a9` by sha; bench `cddac94`) — not touched; the v107 record stands.
- The commit itself — Nick's hands (the card, 13 staged, gated on HEAD · branch · lock · trailers · the count · the exact set).

## §6 After the beat's splice (appended by the splice, the same script, after `beat()` wrote the spine)
```
MATCH snapshot-digest 1950 ≤ 2048
MATCH snapshot-file 3474 ≤ 3500
MATCH brief-status 271
MATCH brief-digest 1563 ≤ 2048
MATCH brief-held 4375 ≤ 6144
MATCH brief-words 733
MATCH brief-file 12150 ≤ 12288
```
Read by the splice after `beat()` wrote the spine (2026-10-12T00:24:23Z): 7 MATCH — the renderer and the splice agree at the bytes. `test_render_state.py` ran before the splice (32/32); the live beat count after the insert 7 of 12; the chain archive 297 headings.

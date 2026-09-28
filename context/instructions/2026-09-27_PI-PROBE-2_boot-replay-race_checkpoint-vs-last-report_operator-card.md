<!--
file: context/instructions/2026-09-27_PI-PROBE-2_boot-replay-race_checkpoint-vs-last-report_operator-card.md
purpose: PI-PROBE-2 (D-v83-25; IR-83) — ONE read-only block on the B1 backup of the event store (`~/hs-backup/20260927T225733Z/homesynapse-events.db`, taken before BC5's restart): the state projection's `view_checkpoints` position against the position of TR3's last `state_reported` before that restart. Decides whether BC5's immediate null `staleAfter` for TR3 (8 s before its first post-boot report) was the boot replay RACE (the report replayed by the new core with IR-61's resolver, the registry not yet caught up) or the CONFOUND (the report already inside `e96dce8`'s checkpoint, null by construction, never replayed). No write; no token; nothing on the live store; the Pi's live core untouched.
audience: Nick (one block in Git Bash; one line back) · the hub (the reading → D-v84-15's row; IR-83's status)
state-type: operator card (read-only probe)
status: DISPATCH-READY — cut v84 beat 3 (Sun 2026-09-27 evening). Runs Monday 2026-09-28 after BENCH-PULL-2 and before the rehearsal (the Pi in series). EXECUTED when the one line is said.
-->

# PI-PROBE-2 — the checkpoint against TR3's last report (read-only; the B1 backup)

**How to read the answer.** `ckpt` = the position the state projection had persisted when the backup was taken = the position the new core (`1f1d1e0`) RESUMED from. `tr3_last` = the global position of TR3's last `state_reported` written before the restart. **`tr3_last > ckpt` → the new core REPLAYED that report with IR-61's resolver and still read null → THE RACE CONFIRMED** (the registry projection had not replayed TR3's registration when the state projection reached the report). **`tr3_last ≤ ckpt` → the report was inside the old checkpoint (`e96dce8` wrote `staleAfter` null everywhere) and the new core never re-derived it → THE CONFOUND** (D-v83-25's ruling stands; IR-61b's gate is ordered regardless). D-v83-25's sentence "above = the race confirmed" is this reading: the REPORT above the checkpoint.

```bash
OUT=~/Desktop/Code/ClaudeFolder/_scratch/v84/2026-09-28_PI-PROBE-2_outputs.txt; mkdir -p "$(dirname "$OUT")"; { echo "=== PP2 $(date -u +%Y-%m-%dT%H:%M:%SZ)"; ssh pi 'hostname; B=~/hs-backup/20260927T225733Z/homesynapse-events.db; ls -l "$B" | cut -c1-90; python3 - "$B" <<'"'"'PY'"'"'
import sqlite3, sys
db = sqlite3.connect("file:" + sys.argv[1] + "?mode=ro", uri=True)
tr3 = bytes.fromhex("01a0db439330778f8eedbecd09698baa")   # 01M3DM74SGEY7RXVDYSM4PK2XA, the 16-byte form
for row in db.execute("SELECT view_name, position, updated_at FROM view_checkpoints ORDER BY view_name"): print("view_checkpoint", row)
for row in db.execute("SELECT subscriber_id, last_position FROM subscriber_checkpoints ORDER BY subscriber_id"): print("subscriber_checkpoint", row)
print("head", db.execute("SELECT MAX(global_position), COUNT(*) FROM events").fetchone())
r = db.execute("SELECT global_position, event_time, ingest_time FROM events WHERE event_type=? AND subject_ref=? ORDER BY global_position DESC LIMIT 1", ("state_reported", tr3)).fetchone()
print("tr3_last_state_reported", r)
if r is None:
    r2 = db.execute("SELECT global_position, event_time, ingest_time, typeof(subject_ref), length(subject_ref) FROM events WHERE event_type=? AND (subject_ref=? OR subject_ref=?) ORDER BY global_position DESC LIMIT 1", ("state_reported", "01M3DM74SGEY7RXVDYSM4PK2XA", tr3.hex().upper())).fetchone()
    print("tr3_last_state_reported_by_text", r2)
ck = dict((n, p) for n, p, _ in db.execute("SELECT view_name, position, updated_at FROM view_checkpoints"))
sp = [p for n, p in ck.items() if "state" in n.lower()]
if r and sp: print("VERDICT", "RACE-CONFIRMED (report above the checkpoint)" if r[0] > sp[0] else "CONFOUND (report at or below the checkpoint)", "ckpt=%d tr3_last=%d" % (sp[0], r[0]))
else: print("VERDICT", "CANNOT-READ (paste the lines above)")
PY'; } 2>&1 | tee -a "$OUT"; echo "RETURNED $OUT $(wc -c < "$OUT")"
# EXPECTED: one view_checkpoint row for the state projection (its view_name contains "state") with position P; head = (N, N-ish); tr3_last_state_reported = (Q, event_time_us, ingest_time_us); VERDICT one of the two. STOP: "CANNOT-READ" (paste the lines — the hub reads the shapes) · any error line · a `ls` that shows a different backup stamp.
```

The one line back: `PI-PROBE-2: <VERDICT line verbatim> · RETURNED <path> <bytes>`. Nothing else is touched; the block opens the backup read-only and writes only under `_scratch/v84/` on your desktop.

<!--
file: context/instructions/2026-09-20_bench-card_BENCH-CORE-1_core-to-c819a02_installDist_operator-card.md
purpose: BENCH-CORE-1 — THE THURSDAY ORDER step 0b: the BENCH card's Core (hs-dev-1, run by `~/bench.sh` from the Pi's own `installDist` tree — NOT a .deb) moved from its pre-CG-123 build to `c819a02` (ENERGY-READ + MEASURE-2b + FE-115; CI green on each), so the metering scenario reads `power_w` from a Core that has the metering path, and Monday's and Tuesday's nightlies run on the full stack. D-v77-1 (`BENCH-CORE: sun`). Cut through THE PRIOR-LEDGER GATE (§G).
audience: Nick (the four blocks, Git Bash → `ssh pi`) · the hub (the intake on the outputs file)
state-type: operator card (one sitting at the desk, ~20 min + the build; no navigator; every block's output tee'd to ONE file the hub reads)
status: EXECUTED — DONE twice Sun 2026-09-20 (`c819a02` at 15:04Z, `13d439f` at 15:52Z; boot-health 6/6 ×2; the outputs file in `_scratch/v77/`) (v78 beat 1 hygiene, Check 12; Mon 2026-09-21 ~07:5x CT; instrument 2026-09-21T12:51:15Z). Was: LIVE v77 beat 5 (Sun 2026-09-20 ~07:1x CT; instrument 2026-09-20T12:0xZ) — Nick's hands, any time today after `R5B-2:` is pasted. The report-back is ONE line: `BENCH-CORE: deployed <sha> · boot-health <n>/6 · rows <before>→<after>` (or `BENCH-CORE: STOP <block> <line>`).
-->

# BENCH-CORE-1 — the bench card's Core to `c819a02`

## §G The prior-ledger gate (the reused strings, grepped in the R-5B and H8-a ledgers)
`ssh pi '…'` and `~/bench.sh status|start|restart|scenario boot-health|entities` — R-5B B5/B6's form, no deviation filed against them · `grep -E "zigbee\.(port_identity_captured|network_resumed)" … | cut -c1-240` — R-5B D-1 / H8-a D-2: the cut is **240**, never 160 · the registry-row python — R-5B D-5 (the S31 string filter) is NOT reused; the rows print whole · the sqlite3 `?mode=ro` reads — H8-a B1, no deviation · the deploy path — `context/audits/2026-07-26_deploy-evening_return.md` (the Pi runs from `installDist`; `~/bench.sh restart`; 23 s incremental) and `2026-08-22_R9_E3-HEALTH_return.md:214` (no `/opt/homesynapse` on the bench card) · NEW in this card and therefore unproven: the `.backup` copy (block 1), the detached build (block 2), `node -v` (block 0) — each a read or a copy, never a delete.

**Every block tees to `~/Desktop/Code/ClaudeFolder/_scratch/v77/2026-09-20_BENCH-CORE-1_outputs.txt` (the file the hub reads; the chat carries the one line).** Run in Git Bash on the desktop. Replace nothing — `pi` is the ssh alias the R-5B packet used.

## Block 0 — the reads (nothing changes)
```bash
OUT=~/Desktop/Code/ClaudeFolder/_scratch/v77/2026-09-20_BENCH-CORE-1_outputs.txt; mkdir -p "$(dirname "$OUT")"; { echo "=== B0 $(date -u +%Y-%m-%dT%H:%M:%SZ)"; ssh pi 'hostname; date -u +%H:%M:%SZ; cd ~/homesynapse-core && echo "clone: $(git --no-optional-locks log -1 --oneline | cut -c1-80)" && echo "porcelain=$(git --no-optional-locks status --porcelain | wc -l)" && git --no-optional-locks fetch -q origin && echo "behind=$(git --no-optional-locks rev-list --count HEAD..origin/main) ahead=$(git --no-optional-locks rev-list --count origin/main..HEAD)"; echo "node=$(node -v 2>&1) npm=$(npm -v 2>&1)"; java -version 2>&1 | head -1; df -h ~ | tail -1; ~/bench.sh status | head -3; DB=$(find ~/hs-bench -name "homesynapse-events.db" | head -1); echo "DB=$DB"; sqlite3 "file:$DB?mode=ro" "SELECT COUNT(*) FROM events;"; sqlite3 "file:$DB?mode=ro" "PRAGMA integrity_check;"; systemctl --user list-timers nexsys-bench-nightly.timer --no-pager 2>/dev/null | head -3'; } 2>&1 | tee -a "$OUT"
# EXPECTED: hs-dev-1 · the clone's sha (the old build of record — ⏺ it) · porcelain=0 · behind=<n> ahead=0 · node= v<18+> npm= <n> (the dashboard build needs both) · a java 21 line · disk ≥ 2 GB free · running (pid …) · DB=~/hs-bench/data/homesynapse-events.db (or wherever find puts it) · ROWS-before ⏺ · ok · the timer's NEXT = Mon 04:30 EDT. STOP: porcelain ≠ 0 (a dirty bench clone — paste it) · ahead ≠ 0 · node absent (the build cannot make the dashboard jar — paste; the hub re-cuts) · integrity not ok.
```

## Block 1 — the backup (a copy; nothing deleted; the Core keeps running)
```bash
OUT=~/Desktop/Code/ClaudeFolder/_scratch/v77/2026-09-20_BENCH-CORE-1_outputs.txt; { echo "=== B1 $(date -u +%Y-%m-%dT%H:%M:%SZ)"; ssh pi 'hostname; S=$(date -u +%Y%m%dT%H%M%SZ); B=~/hs-backup/$S; mkdir -p "$B"; DB=$(find ~/hs-bench -name "homesynapse-events.db" | head -1); sqlite3 "$DB" ".backup $B/homesynapse-events.db" && cp -a ~/hs-bench/config "$B/config" && cp -a ~/homesynapse-core/app/homesynapse-app/build/install/homesynapse-app "$B/install-tree-old" && echo "BACKUP=$B" && ls -l "$B" && sqlite3 "file:$B/homesynapse-events.db?mode=ro" "SELECT COUNT(*) FROM events;"'; } 2>&1 | tee -a "$OUT"
# EXPECTED: BACKUP=~/hs-backup/<stamp> · three entries (the db, config/, install-tree-old/) · the backup's row count = ROWS-before (or +a few: the Core is live). ⏺. STOP: any error line → paste; nothing else is run.
```

## Block 2 — the pull and the build (detached; then poll until BUILD SUCCESSFUL)
```bash
OUT=~/Desktop/Code/ClaudeFolder/_scratch/v77/2026-09-20_BENCH-CORE-1_outputs.txt; { echo "=== B2 $(date -u +%Y-%m-%dT%H:%M:%SZ)"; ssh pi 'hostname; cd ~/homesynapse-core && git pull --ff-only 2>&1 | tail -2 && echo "clone: $(git --no-optional-locks log -1 --oneline | cut -c1-80)" && S=$(date -u +%Y%m%dT%H%M%SZ) && nohup ./gradlew :app:homesynapse-app:installDist --console plain > ~/hs-bench/build-$S.log 2>&1 & echo "BUILD pid=$! log=~/hs-bench/build-$S.log"'; } 2>&1 | tee -a "$OUT"
# EXPECTED: Fast-forward · clone: c819a02 feat(web-ui): FE-115 … · BUILD pid=<n>. STOP: anything but a fast-forward (paste) · a sha other than c819a02.
```
```bash
# THE POLL — run every ~2 min until the tail reads BUILD SUCCESSFUL (a first build with the dashboard's npm ci can take 10–25 min on the Pi; an incremental one 1–3 min).
OUT=~/Desktop/Code/ClaudeFolder/_scratch/v77/2026-09-20_BENCH-CORE-1_outputs.txt; { echo "=== B2-poll $(date -u +%Y-%m-%dT%H:%M:%SZ)"; ssh pi 'L=$(ls -t ~/hs-bench/build-*.log | head -1); echo "$L"; tail -4 "$L"; ls -l --time-style=+%H:%M:%S ~/homesynapse-core/app/homesynapse-app/build/install/homesynapse-app/bin/homesynapse-app'; } 2>&1 | tee -a "$OUT"
# EXPECTED (when done): BUILD SUCCESSFUL in <t> · the launcher's mtime = minutes ago. STOP: BUILD FAILED → paste the last 30 lines of the log (`ssh pi 'tail -30 $(ls -t ~/hs-bench/build-*.log | head -1)'`); the OLD install tree is untouched by a failed build (Gradle syncs the dir only after a green compile) and the running Core is the old one — nothing to restore.
```

## Block 3 — the restart onto the new tree; the boot health; the proof of the new Core
```bash
OUT=~/Desktop/Code/ClaudeFolder/_scratch/v77/2026-09-20_BENCH-CORE-1_outputs.txt; { echo "=== B3 $(date -u +%Y-%m-%dT%H:%M:%SZ)"; ssh pi 'hostname; date -u +%H:%M:%SZ; ~/bench.sh restart; sleep 20; ~/bench.sh scenario boot-health 2>&1 | tail -3; grep -E "zigbee\.(port_identity_captured|network_resumed)" ~/hs-bench/current.log | tail -2 | cut -c1-240; echo "formed=$(grep -c "zigbee.network_formed" ~/hs-bench/current.log) resumed=$(grep -c "zigbee.network_resumed" ~/hs-bench/current.log) relinked=$(grep -c "device_relinked" ~/hs-bench/current.log) adopted=$(grep -c "device_adopted" ~/hs-bench/current.log) config_issue=$(grep -c "Configuration issue" ~/hs-bench/current.log)"; DB=$(find ~/hs-bench -name "homesynapse-events.db" | head -1); sqlite3 "file:$DB?mode=ro" "SELECT COUNT(*) FROM events;"; sqlite3 "file:$DB?mode=ro" "PRAGMA integrity_check;"; ~/bench.sh entities | python3 -c "import sys,json; d=json.load(sys.stdin); d=d[\"data\"] if isinstance(d,dict) and \"data\" in d else d; print(\"registry rows=%d\" % len(d)); [print(\"   %s deviceId=%s lastReported=%s\" % (e.get(\"entityId\"), e.get(\"deviceId\"), e.get(\"lastReported\"))) for e in d]"; echo "deployed=$(git -C ~/homesynapse-core log -1 --format=%h)"'; } 2>&1 | tee -a "$OUT"
# EXPECTED: stopped → launched → RADIO UP after <s>s · [PASS] boot-health — 6/6 positive · 0 forbidden · network_resumed: channel=20 panId=0x774c · formed=0 resumed=1 relinked=6 adopted=0 config_issue=0 · ROWS-after ≥ ROWS-before · ok · registry rows=6 and every deviceId a 26-char ULID (on the OLD Core they read None — THIS is the visible proof of the upgrade; lastReported ISO-Z or None) · deployed=c819a02. ⏺ all. STOP: formed ≠ 0 = POWER OFF, paste · a changed PAN · integrity not ok · boot-health < 6/6 or INTEGRATION FAILED → paste the block's output whole; do NOT restore by hand — the hub reads first (the backup is in place; `~/bench.sh stop` is the only act allowed before the hub answers).
```

## The one line back
`BENCH-CORE: deployed c819a02 · boot-health 6/6 · rows <before>→<after>` — or `BENCH-CORE: STOP <block> <the line>`. The outputs file is the record; the hub intakes it at the next beat. Monday's 03:30 CT nightly (`R5B-3:` — paste it Monday like Sunday's) is the first watched line on the full stack; Tuesday's the second. The second deploy (AUTO-ID-1's build, once CI is green on it) rides Wednesday with `HARNESS-PLUG:` — the same card, re-cut to that sha.

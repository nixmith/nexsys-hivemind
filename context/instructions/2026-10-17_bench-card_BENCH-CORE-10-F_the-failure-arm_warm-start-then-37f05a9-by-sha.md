<!--
file: context/instructions/2026-10-17_bench-card_BENCH-CORE-10-F_the-failure-arm_warm-start-then-37f05a9-by-sha.md
purpose: BENCH-CORE-10's failure arm as Nick's GO names it (Sat 2026-10-17 07:36 CT: "cold AND warm fail → restore `37f05a9` by sha, the C1 backup untouched"). Shown ONLY when BC10's C3 STOPs on `startup_failed ≥ 1` and the hub hands it. F1 — one pre-warmed warm start of `176adad` (the cold failure stands as IR-148's "after"); F2 — only if F1 fails too: `37f05a9` restored BY SHA (the old install tree from C1's backup, pre-warmed — its cold boot fails, IR-148), the live store kept, the C1 backup untouched. D-v110-16 governs the RUN's rollback (`e11ae20` · `ba08dd8`), not this arm.
audience: the BC10 guide session (Nick pastes this file WHOLE into the SAME conversation when the hub says "BC10-F") · the hub (the intake reads F1/F2 against the EXPECTED lines)
state-type: operator card (a failure arm; never run without C3's STOP)
status: DISPATCH-READY (HELD for C3's STOP) — cut v112 (Sat 2026-10-17 ~07:5x CT); the stub-ssh dry-run `_scratch/v111/bc10/bc10f_dry-run.sh`, both arms; flips to EXECUTED (if run) or RETIRED (if C3 passes) at BC10's intake
-->

You are still the BENCH-CORE-10 GUIDE. This file is BC10's failure arm, and it runs ONLY because C3 stopped on `startup_failed ≥ 1` and the hub handed it. The rules are BC10's: one block at a time; THE TWO-MESSAGE RULE (a block's SAY and its command are two messages); every block tees to BC10's outputs file; nothing is deleted on the Pi (the failed install tree is RENAMED, never removed); no config is written; `network_formed` in any output = POWER OFF the Pi and STOP. ONE slot: F2's `<STAMP from C1>`, the same stamp C1b used. F2 runs only after F1's STOP AND the hub's word "F2".

## F1 — ONE pre-warmed warm start of `176adad` (≈ 3 min; no hands)
```bash
OUT=~/Desktop/Code/ClaudeFolder/_scratch/v111/bc10/2026-10-17_BENCH-CORE-10_outputs.txt; { echo "=== F1 $(date -u +%Y-%m-%dT%H:%M:%SZ)"; ssh pi 'bash -s' <<'EOF_F1'
hostname; echo "pi-clock $(date -u +%H:%M:%SZ)"; ~/bench.sh stop 2>&1 | tail -1; ~/bench.sh pre-warm 2>&1 | tail -2
~/bench.sh start 2>&1 | tail -3; sleep 25
L=$(readlink -f ~/hs-bench/current.log); echo "boot-log: $(basename $L)"
PYTHONIOENCODING=utf-8 python3 -B ~/nexsys-bench/tools/runner/boot_timing.py "$L"
echo "formed=$(grep -c zigbee.network_formed $L) resumed=$(grep -c zigbee.network_resumed $L) startup_failed=$(grep -c startup_failed $L) issues=$(grep -c "Configuration issue" $L) rebuilt=$(grep -o "registry.projection_rebuilt.*" $L | head -1 | cut -c1-120)"
grep -m3 -E "startup_failed|Exception|ERROR" $L | cut -c1-220
~/bench.sh scenario boot-health 2>&1 | tail -3
echo "deployed=$(git -C ~/homesynapse-core --no-optional-locks rev-parse --short HEAD)"
EOF_F1
} 2>&1 | tee -a "$OUT"
# EXPECTED (the warm arm holds): the pre-warm's cache line · launched → RADIO UP · the boot line (RECORD every stamp) · formed=0 resumed=1 startup_failed=0 issues=0 · the rebuilt line · [PASS] boot-health · deployed=176adad → say "BC10-F: the warm arm holds — back to BC10's Part D". The cold failure stands on the record as IR-148's "after"; the hub re-plans the pre-warm at the intake. STOP (paste to the hub; it says "F2" or not): startup_failed ≥ 1 again · issues ≠ 0 · boot-health FAIL. POWER OFF + STOP: formed ≠ 0.
```

## F2 — `37f05a9` restored BY SHA; the live store kept; the C1 backup untouched (only on the hub's word "F2"; ≈ 5 min; no hands)
```bash
OUT=~/Desktop/Code/ClaudeFolder/_scratch/v111/bc10/2026-10-17_BENCH-CORE-10_outputs.txt; { echo "=== F2 $(date -u +%Y-%m-%dT%H:%M:%SZ)"; ssh pi 'bash -s' <<'EOF_F2'
hostname; S=<STAMP from C1>; B=~/hs-backup/$S; I=~/homesynapse-core/app/homesynapse-app/build/install/homesynapse-app
test -d "$B/install-tree-old" || { echo "NO BACKUP TREE at $B — STOP"; exit 1; }
~/bench.sh stop 2>&1 | tail -1
cd ~/homesynapse-core && git -c advice.detachedHead=false checkout 37f05a9 2>&1 | grep -iE "head is now|fatal|error"
mv "$I" "$I.failed-176adad-$(date -u +%Y%m%dT%H%M%SZ)" && cp -a "$B/install-tree-old" "$I" && echo "install tree: 37f05a9's, copied from $B (the backup keeps its own copy)"
~/bench.sh pre-warm 2>&1 | tail -2; ~/bench.sh start 2>&1 | tail -3; sleep 25
L=$(readlink -f ~/hs-bench/current.log); echo "boot-log: $(basename $L)"
PYTHONIOENCODING=utf-8 python3 -B ~/nexsys-bench/tools/runner/boot_timing.py "$L"
echo "formed=$(grep -c zigbee.network_formed $L) resumed=$(grep -c zigbee.network_resumed $L) startup_failed=$(grep -c startup_failed $L) degraded=$(grep -c registry.projection_degraded_event $L)"
~/bench.sh scenario boot-health 2>&1 | tail -3
echo "deployed=$(git -C ~/homesynapse-core --no-optional-locks rev-parse --short HEAD) backup=$(ls "$B" | tr '\n' ' ')"
EOF_F2
} 2>&1 | tee -a "$OUT"
# EXPECTED: HEAD is now at 37f05a9 · install tree: 37f05a9's, copied · the pre-warm's cache line · RADIO UP · the boot line · formed=0 resumed=1 startup_failed=0 · degraded=<n> (RECORD: the rows 176adad wrote in types 37f05a9 does not know, read as DegradedEvent — a WARN each, never a stop) · [PASS] boot-health · deployed=37f05a9 · backup=config homesynapse-events.db install-tree-old → say "BC10-F: 37f05a9 is up — BC10's close runs; Parts D–E do not". STOP — the Core is DOWN, paste to the hub at once: startup_failed ≥ 1 · NO BACKUP TREE. POWER OFF + STOP: formed ≠ 0.
```

## The one line back (after BC10's close)
`BC10-F: F1 <warm PASS → Part D | FAIL> · F2 <37f05a9 up degraded=<n> | not run | FAIL> · boot <the boot line's Loaded / projection_live / startup_failed> · RETURNED _scratch/v111/bc10/2026-10-17_BENCH-CORE-10_outputs.txt <bytes>`

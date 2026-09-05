#!/usr/bin/env bash
# run-sequence.sh — FAILCHAN-FIX-1 Part A loops (§A.3 I-3 + §A.4 I-4 + the §A.5 CPU-shape row), sequential.
set -u
export MSYS2_ARG_CONV_EXCL='*'
S="$(cd "$(dirname "$0")" && pwd)"
CORE="C:/Users/Nick/Desktop/Code/ClaudeFolder/homesynapse-core"
WT="C:/Users/Nick/Desktop/Code/ClaudeFolder/hs-ef02d13"
OUT="${1:-C:/Users/Nick/Desktop/Code/ClaudeFolder/nexsys-hivemind/context/audits/2026-09-05_FIX-1_loops}"
mkdir -p "$OUT"
{
  echo "# FAILCHAN-FIX-1 loop corpus — SUMMARY. One line per run: class · tree · run-NN · GREEN|RED · start→end (UTC, per-run stamps = the instrument's clock) · rc · the class's suite counts + wall time · the anomaly tokens seen (bus.delivery_anomaly kinds / integration.route_join_miss) [· RED: method :: message]."
  echo "# Desk instrument (Windows 11, 24 cores; WSL has no JDK, so the recipe's taskset/busy loops are replicated natively): pinned = 'start /affinity 3' (cores 0,1 — the test JVM measures availableProcessors=2) + two CPU-bound PowerShell loops pinned to the same mask + -PvtParallelism=2 (the FIX-1a knob, passed as ORG_GRADLE_PROJECT_vtParallelism=2 in the environment; inert on ef02d13, which predates it); unpinned = no affinity, no knob, the two busy loops still running (the §A.5 CPU-shape row). Every run: gradlew.bat <task> --tests <class> --rerun --no-daemon --offline --console=plain (a fresh Gradle JVM per run; --rerun re-executes the test task only)."
  echo "# sequence start $(date -u +%FT%TZ)"
} >> "$OUT/SUMMARY.md"
powershell.exe -NoProfile -ExecutionPolicy Bypass -File "$(cygpath -w "$S/busy-start.ps1")" "$(cygpath -w "$S/busy.pids")" | tr -d '\r' | sed 's/^/# /' | tee -a "$OUT/SUMMARY.md"
bash "$S/fix1-loop.sh" pinned   "$CORE" fix1a   HeroLoop          :lifecycle:lifecycle:test com.homesynapse.lifecycle.HeroLoopHardwareFreeIT 20 "$OUT"
bash "$S/fix1-loop.sh" pinned   "$CORE" fix1a   ReplayIT          :core:event-bus:test      com.homesynapse.event.bus.ReplayTransitionIT   20 "$OUT"
bash "$S/fix1-loop.sh" unpinned "$CORE" fix1a   HeroLoop-cpushape :lifecycle:lifecycle:test com.homesynapse.lifecycle.HeroLoopHardwareFreeIT 10 "$OUT"
bash "$S/fix1-loop.sh" pinned   "$WT"   ef02d13 HeroLoop          :lifecycle:lifecycle:test com.homesynapse.lifecycle.HeroLoopHardwareFreeIT 20 "$OUT"
powershell.exe -NoProfile -ExecutionPolicy Bypass -File "$(cygpath -w "$S/busy-stop.ps1")" "$(cygpath -w "$S/busy.pids")" | tr -d '\r' | sed 's/^/# /' | tee -a "$OUT/SUMMARY.md"
echo "# sequence end $(date -u +%FT%TZ)" >> "$OUT/SUMMARY.md"
echo SEQUENCE-DONE

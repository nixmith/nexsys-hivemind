#!/usr/bin/env bash
# bench-oq15-2-driver.sh — OQ-15-2 microbench driver (SPIKE — runs ON THE PI).
#
# Runs the full §3.A/§3.C protocol with the §3.E hygiene guards:
#   intrinsics-off flag set (Pi-5-as-Pi-4-emulation per spec §3.D), PrintFlagsFinal
#   evidence, throttle/temp/governor capture before+after, taskset core pinning,
#   3 warm JVM forks + 1 cold fork + 1 SHA-256 chain-hash context fork.
#
# Usage (on the Pi, from $HOME/bench-oq15-2 containing BenchOQ152.java + corpus/):
#   ./bench-oq15-2-driver.sh
#
# Paste the ENTIRE output back to the PM.

set -euo pipefail

BENCH_DIR="${BENCH_DIR:-$HOME/bench-oq15-2}"
CORPUS_DIR="${CORPUS_DIR:-$BENCH_DIR/corpus}"
OPS_PER_BATCH="${OPS_PER_BATCH:-2000}"
WARM_FORKS="${WARM_FORKS:-3}"
PIN_CORE="${PIN_CORE:-2}"

# Pi IT profile heap/GC (deployment JVM profile not yet pinned in-repo — recorded
# as such in §8) + intrinsics forced OFF (spec §3.D Pi-4 emulation on non-Pi-4).
# v2 fix (2026-06-12): the UseAES*/UseGHASH/UseSHA* intrinsic toggles are
# DIAGNOSTIC VM options on JDK 11+ — UnlockDiagnosticVMOptions MUST precede
# them or the JVM refuses to start (v1 died here, silently under 2>/dev/null).
JVM_FLAGS=(
  -XX:+UnlockDiagnosticVMOptions
  -XX:+IgnoreUnrecognizedVMOptions
  -Xms256m -Xmx256m -XX:+UseG1GC -XX:ActiveProcessorCount=4 -XX:+AlwaysPreTouch
  -XX:-UseAESIntrinsics -XX:-UseAESCTRIntrinsics -XX:-UseGHASHIntrinsics
  -XX:-UseSHA -XX:-UseSHA1Intrinsics -XX:-UseSHA256Intrinsics -XX:-UseSHA512Intrinsics -XX:-UseSHA3Intrinsics
)

cd "$BENCH_DIR"

echo "===================== OQ-15-2 MICROBENCH DRIVER ====================="
date -u +"RUN_DATE_UTC:%Y-%m-%dT%H:%M:%SZ"
echo "HOST:$(hostname)  KERNEL:$(uname -rm)"
echo "MODEL:$(tr -d '\0' </proc/device-tree/model 2>/dev/null || echo unknown)"
java -version 2>&1 | sed 's/^/JAVA:/'
echo "JVM_FLAGS:${JVM_FLAGS[*]}"
echo "OPS_PER_BATCH:${OPS_PER_BATCH}  WARM_FORKS:${WARM_FORKS}  PIN_CORE:${PIN_CORE}"

echo "----- JVM preflight (the flag set must boot a JVM) -----"
if ! java "${JVM_FLAGS[@]}" -version 2>&1 | sed 's/^/PREFLIGHT:/'; then
  echo "FATAL: JVM refused the flag set above — fix flags before benching."
  exit 1
fi

echo "----- §3.D intrinsics guard (must all be false) -----"
# v2: diagnostics must never kill the run (v1 lesson — pipefail + empty grep).
GUARD_OUT=$(java "${JVM_FLAGS[@]}" -XX:+PrintFlagsFinal -version 2>&1 || true)
echo "$GUARD_OUT" | grep -iE "UseAESIntrinsics|UseAESCTRIntrinsics|UseGHASHIntrinsics|UseSHA256Intrinsics" | sed 's/^/FLAG:/' \
  || { echo "FLAG:NONE_MATCHED — raw evidence follows"; echo "$GUARD_OUT" | head -8 | sed 's/^/GUARDRAW:/'; }

echo "----- §3.E pre-run thermal / governor -----"
echo "THROTTLED_BEFORE:$(vcgencmd get_throttled 2>/dev/null || echo UNAVAILABLE)"
echo "TEMP_BEFORE:$(vcgencmd measure_temp 2>/dev/null || cat /sys/class/thermal/thermal_zone0/temp)"
GOV=$(cat /sys/devices/system/cpu/cpu0/cpufreq/scaling_governor 2>/dev/null || echo unknown)
echo "GOVERNOR:${GOV}"
if [ "$GOV" != "performance" ]; then
  echo "WARNING: governor is '${GOV}', not 'performance'. Fix and re-run:"
  echo "  echo performance | sudo tee /sys/devices/system/cpu/cpu*/cpufreq/scaling_governor"
fi
echo "CPU_FREQ_KHZ:$(cat /sys/devices/system/cpu/cpu0/cpufreq/scaling_cur_freq 2>/dev/null || echo unknown)"

echo "----- compile -----"
javac BenchOQ152.java
echo "COMPILED:ok"

CORPUS_FILES=$(ls "$CORPUS_DIR"/*.bin | sort)
echo "CORPUS:"; ls -l "$CORPUS_DIR"/*.bin

echo "----- WARM forks (steady-state, ${WARM_FORKS} JVM forks) -----"
for fork in $(seq 1 "$WARM_FORKS"); do
  echo "--- fork ${fork} ---"
  # shellcheck disable=SC2086
  taskset -c "$PIN_CORE" java "${JVM_FLAGS[@]}" BenchOQ152 warm "$OPS_PER_BATCH" $CORPUS_FILES
done

echo "----- COLD fork (first-100-ops, fresh JVM, p50-size payload) -----"
COLD_FILE=$(ls "$CORPUS_DIR"/*band_350*.bin 2>/dev/null | head -1 || echo "$CORPUS_FILES" | head -1)
taskset -c "$PIN_CORE" java "${JVM_FLAGS[@]}" BenchOQ152 cold "$COLD_FILE"

echo "----- SHA-256 chain-hash context fork (§3.C) -----"
# shellcheck disable=SC2086
taskset -c "$PIN_CORE" java "${JVM_FLAGS[@]}" BenchOQ152 sha "$OPS_PER_BATCH" $CORPUS_FILES

echo "----- §3.E post-run thermal -----"
echo "THROTTLED_AFTER:$(vcgencmd get_throttled 2>/dev/null || echo UNAVAILABLE)"
echo "TEMP_AFTER:$(vcgencmd measure_temp 2>/dev/null || cat /sys/class/thermal/thermal_zone0/temp)"
echo "===================== END OQ-15-2 MICROBENCH ====================="

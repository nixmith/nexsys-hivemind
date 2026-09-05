#!/usr/bin/env bash
# fix1-loop.sh — FAILCHAN-FIX-1 §A.3/§A.4 loop driver, Windows-desk variant.
# usage: fix1-loop.sh <mode:pinned|unpinned> <tree-dir> <tree-label> <class-label> <module-task> <test-fqcn> <runs> <out-dir>
# pinned  : `start /affinity 3` (cores 0,1 — the recipe's `taskset -c 0,1`) + -PvtParallelism=2 (the knob)
# unpinned: no affinity, no knob (the §A.5 CPU-shape row); the two busy loops are the caller's affair (busy-start.ps1)
# No path may contain a space: every argument is passed to cmd.exe UNQUOTED (cmd /c strips a first+last quote pair).
set -u
export MSYS2_ARG_CONV_EXCL='*'
MODE=$1; TREE=$2; TLABEL=$3; CLABEL=$4; TASK=$5; FQCN=$6; RUNS=$7; OUT=$8
SCRATCH="$(cd "$(dirname "$0")" && pwd)"
RUNONE="$(cygpath -w "$SCRATCH/run-one.cmd")"
MODDIR="$TREE/$(echo "$TASK" | sed 's/^://; s/:test$//; s#:#/#g')"
RESULTS="$MODDIR/build/test-results/test"
XML="$RESULTS/TEST-$FQCN.xml"
mkdir -p "$OUT"
echo "# loop start $(date -u +%FT%TZ) mode=$MODE tree=$TLABEL class=$CLABEL task=$TASK xml=$XML" >> "$OUT/SUMMARY.md"
for n in $(seq -w 1 "$RUNS"); do
  LOG="$SCRATCH/run-$CLABEL-$TLABEL.log"; RCF="$SCRATCH/run-$CLABEL-$TLABEL.rc"; rm -f "$LOG" "$RCF" "$XML"
  s=$(date -u +%H:%M:%S.%N | cut -c1-12)
  # cmd batch tokenization treats "=" as an argument separator, so the knob rides Gradle's
  # ORG_GRADLE_PROJECT_<prop> environment variable (inherited by every child), never a -P token.
  if [ "$MODE" = pinned ]; then
    ORG_GRADLE_PROJECT_vtParallelism=2 cmd.exe /c start "" /affinity 3 /B /WAIT cmd.exe /c "$RUNONE" "$(cygpath -w "$TREE")" "$(cygpath -w "$LOG")" "$(cygpath -w "$RCF")" "$TASK" --tests "$FQCN" --rerun --no-daemon --offline --console plain >/dev/null 2>&1
  else
    env -u ORG_GRADLE_PROJECT_vtParallelism cmd.exe /c "$RUNONE" "$(cygpath -w "$TREE")" "$(cygpath -w "$LOG")" "$(cygpath -w "$RCF")" "$TASK" --tests "$FQCN" --rerun --no-daemon --offline --console plain >/dev/null 2>&1
  fi
  e=$(date -u +%H:%M:%S.%N | cut -c1-12)
  rc=$(tr -d ' \r\n' < "$RCF" 2>/dev/null); [ -z "$rc" ] && rc=99
  verdict=$([ "$rc" = 0 ] && echo GREEN || echo RED)
  tok=$(grep -hoE 'bus\.delivery_anomaly: kind=[A-Z_]+|integration\.route_join_miss' "$XML" 2>/dev/null | sort | uniq -c | sed 's/^ *//' | tr '\n' ';')
  cnt=$(grep -hoE '<testsuite [^>]*>' "$XML" 2>/dev/null | grep -oE '(tests|skipped|failures|errors|time)="[0-9.]+"' | tr '\n' ' ')
  redm=$(python - "$XML" <<'PY' 2>/dev/null
import sys,re
try:
    s=open(sys.argv[1],encoding='utf-8').read()
except Exception:
    sys.exit(0)
out=[]
for m in re.finditer(r'<testcase name="([^"]+)"[^>]*?(?:/>|>(.*?)</testcase>)', s, re.S):
    body=m.group(2) or ''
    if '<failure' in body or '<error' in body:
        msg=re.search(r'message="([^"]{0,120})', body)
        out.append(m.group(1)[:60].replace('—','-')+' :: '+(msg.group(1) if msg else '?'))
print(' | '.join(out))
PY
)
  line="$CLABEL · $TLABEL · run-$n · $verdict · ${s}→${e} · rc=$rc · ${cnt}· tokens: ${tok:-none}${redm:+ · RED: $redm}"
  echo "$line" | tee -a "$OUT/SUMMARY.md"
  if [ "$rc" != 0 ]; then d="$OUT/$CLABEL/$TLABEL/run-$n"; mkdir -p "$d"; cp "$XML" "$d"/ 2>/dev/null; cp "$LOG" "$d/gradle.log" 2>/dev/null; fi
done
echo "# loop end $(date -u +%FT%TZ)" >> "$OUT/SUMMARY.md"

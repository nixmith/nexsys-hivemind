<!--
file: context/instructions/2026-09-28_bench-card_CORPUS-1_rehearsal-1-corpus-copy_operator-card.md
purpose: CORPUS-1 — the first entry of the bench's run index (`corpus/runs/README.md`): rehearsal 1's graded export (EXPORT-1, VERIFY-72H PASS) copied as its four small files into `nexsys-bench/corpus/runs/2026-09-28_rehearsal-1/`, committed by Nick's hands, and taken by the Pi's clone in the BENCH-PULL-4 block (IR-76: every bench landing ends with a BENCH-PULL block). Three blocks, one at a time, one line back each. The Pi in series: NEVER while BENCH-CORE-6's guide session is open — after Part E's line, or Tuesday 16:00.
audience: Nick (runs it) · the hub (banks the three lines)
state-type: operator card (three blocks)
status: DISPATCH-READY — cut v86 beat 1 (Mon 2026-09-28 ~18:4x CT; instrument 2026-09-28T23:42:00Z) at EXPORT-1's intake (`context/audits/2026-09-28_v86-b1_EXPORT-1_intake_audit.md`). Runs after `BENCH-CORE-6:` lands (or Tuesday); flips to EXECUTED at the hub's intake of `BENCH-PULL-4:`.
-->

# CORPUS-1 — rehearsal 1's export into the run index (three blocks; the Pi only in Block 2)

**Before you start:** the BC6 guide conversation is CLOSED (its last line said back). Nothing at the rig. Git Bash.

## Block 0 — the copy on your PC (no Pi). Say back `CORPUS-1: copied 4/4` or the failing line.
```bash
cd ~/Desktop/Code/ClaudeFolder && S=_archive/runs/2026-09-28_rehearsal-1 && T=nexsys-bench/corpus/runs/2026-09-28_rehearsal-1 && mkdir -p "$T" && for f in MANIFEST.txt window.json verdict.json report.md; do cp "$S/$f" "$T/$f"; done && echo "equal: $(for f in MANIFEST.txt window.json verdict.json report.md; do [ "$(sha256sum < "$S/$f")" = "$(sha256sum < "$T/$f")" ] && echo ok; done | grep -c ok)/4" && ls -la "$T" && cd nexsys-bench && git --no-optional-locks status --porcelain -uall
```
EXPECTED: `equal: 4/4` · the four files listed · the porcelain shows exactly four `??` lines under `corpus/runs/2026-09-28_rehearsal-1/`. STOP on anything else.

## Block 1 — the bench commit (your hands; explicit paths; the trailer grep). Say back `BENCH: LANDED <sha> (CORPUS-1)`.
```bash
cd ~/Desktop/Code/ClaudeFolder/nexsys-bench && git --no-optional-locks status --porcelain | wc -l && ls .git/*.lock 2>/dev/null; git add -- corpus/runs/2026-09-28_rehearsal-1/MANIFEST.txt corpus/runs/2026-09-28_rehearsal-1/window.json corpus/runs/2026-09-28_rehearsal-1/verdict.json corpus/runs/2026-09-28_rehearsal-1/report.md && echo "staged: $(git diff --cached --name-status | wc -l) (expect 4)" && grep -c 'Co-Authored\|Claude-Session' ../_scratch/v86/2026-09-28_bench_CORPUS-1_commit-msg.txt; git commit -F ../_scratch/v86/2026-09-28_bench_CORPUS-1_commit-msg.txt && git push && git log -1 --oneline
```
Read: `4` · `staged: 4 (expect 4)` · `0` · the new sha.

## Block 2 — BENCH-PULL-4: the Pi's clone takes the corpus entry (IR-76). The Pi in series; nothing at the rig. Say back `BENCH-PULL-4: <sha> · 42/0 · 26/0`.
```bash
OUT=~/Desktop/Code/ClaudeFolder/_scratch/v86/2026-09-28_BENCH-PULL-4_outputs.txt; mkdir -p "$(dirname "$OUT")"; { echo "=== BP4 $(date -u +%Y-%m-%dT%H:%M:%SZ)"; ssh pi 'hostname; cd ~/nexsys-bench && echo "before: $(git --no-optional-locks log -1 --oneline | cut -c1-60)" && echo "porcelain=$(git --no-optional-locks status --porcelain | wc -l)" && git pull --ff-only 2>&1 | grep -iE "fast-forward|up to date|updating|fatal|error|abort" ; echo "after: $(git --no-optional-locks log -1 --oneline | cut -c1-60)"; cd ~/nexsys-bench && python3 -B tools/runner/test_engine.py 2>&1 | tail -1; python3 -B tools/verify72h/test_verify72h.py 2>&1 | tail -1'; } 2>&1 | tee -a "$OUT"
```
EXPECTED: `before: 352296d …` · `porcelain=0` · `Fast-forward` · `after: <the Block 1 sha> …` · `selftest: 42 check(s), 0 failure(s)` · `verify72h selftest: 26 check(s), 0 failure(s)`. STOP on `porcelain=` other than 0, on `fatal`/`error`/`abort`, or on a failure count above 0 (then the hub reads the outputs file first).

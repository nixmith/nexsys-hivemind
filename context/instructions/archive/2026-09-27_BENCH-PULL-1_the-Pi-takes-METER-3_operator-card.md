<!--
file: context/instructions/2026-09-27_BENCH-PULL-1_the-Pi-takes-METER-3_operator-card.md
purpose: BENCH-PULL-1 — one block: the Pi's bench clone (`~/nexsys-bench`, the tree `~/bench.sh` and the nightly run from) pulls METER-3 after it lands, so Monday's 03:30 CT nightly runs boot-health with BH-2 (a pairing window at boot turns it red) and REHEARSAL 1's reads carry the freshness VOID. Nothing restarts; nothing is deleted; the Core keeps running. Runs AFTER `BENCH: LANDED <sha>` and after (or before) BENCH-CORE-4 — it touches the bench clone only. Nick's hands in Git Bash; no guide session needed (one block, one EXPECTED line).
audience: Nick · the v82 hub (intakes the one line)
state-type: operator card (one block)
status: EXECUTED — run Sun 2026-09-27 17:42:45Z (12:42 CT): the Pi `f1c2f9a` → `58b5b45` (fast-forward; porcelain 0; `bh2=3 fresh=1`; the Pi's selftest 38/0); the outputs filed at `context/audits/2026-09-27_BENCH-PULL-1_outputs.txt`; intaken v82 beat 3. Was: DISPATCH-READY — cut v82 beat 3 (Sun 2026-09-27 ~12:4x CT).
-->

# BENCH-PULL-1 — the Pi takes METER-3

```bash
OUT=~/Desktop/Code/ClaudeFolder/_scratch/v82/2026-09-27_BENCH-PULL-1_outputs.txt; mkdir -p "$(dirname "$OUT")"; { echo "=== BP1 $(date -u +%Y-%m-%dT%H:%M:%SZ)"; ssh pi 'hostname; cd ~/nexsys-bench && echo "before: $(git --no-optional-locks log -1 --oneline | cut -c1-60)" && echo "porcelain=$(git --no-optional-locks status --porcelain | wc -l)" && git pull --ff-only 2>&1 | grep -iE "fast-forward|up to date|updating|fatal|error|abort" ; echo "after: $(git --no-optional-locks log -1 --oneline | cut -c1-60)"; echo "bh2=$(grep -c "zigbee.permit_join_opened" ~/nexsys-bench/scenarios/boot-health.yaml) fresh=$(grep -c "fresh-within-s:" ~/nexsys-bench/scenarios/constants.yaml)"; cd ~/nexsys-bench/tools/runner && python3 -B test_engine.py 2>&1 | tail -1'; } 2>&1 | tee -a "$OUT"
# EXPECTED: before: f1c2f9a … · porcelain=0 · Updating f1c2f9a..<sha> · Fast-forward · after: <the METER-3 sha> · bh2=3 (two comment lines + the forbidden entry) fresh=1 · selftest: 38 check(s), 0 failure(s). STOP: porcelain ≠ 0 (paste; the Pi's clone has local edits — the hub reads) · anything but a fast-forward · a selftest line other than 38 / 0.
```

The one line back: `BENCH-PULL-1: <the sha on the Pi> · selftest 38/0` — or `BENCH-PULL-1: STOP <the line>`.

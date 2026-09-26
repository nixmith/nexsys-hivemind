# THURSDAY ORDER T1b (cut 2026-09-25, v80 b2) — RE-OPEN the pairing window for the Shelly recovery (T2b). Run from Git Bash on the DESKTOP:
#   ssh pi 'bash -s' < <this file> > <the T1b.txt beside it>
# Same guarded write as T1.sh, for the post-T2 list: adopt_devices must be the NINE (6 + G4-1 · TR3 · G4-2), the window key absent (T3 removed it) or already 254.
# Adds `permit_join_duration: 254`, then ~/bench.sh restart. The window opens at this boot (254 s) — power-cycle / reset the Shellys right after T1b-END.
# Self-test hooks (never set on the Pi): ZIGBEE_YAML=<mock path> reads another file; DRY_RUN=1 stops before the restart.
set -u
Z="${ZIGBEE_YAML:-$HOME/hs-bench/config/integrations/zigbee.yaml}"
python3 - "$Z" <<'PY' || { echo "T1b-STOP — nothing written, nothing restarted"; exit 1; }
import sys, yaml, pathlib
p = pathlib.Path(sys.argv[1]); s = p.read_text(); d = yaml.safe_load(s)
assert isinstance(d, dict), "zigbee.yaml is not a mapping"
al = d.get("adopt_devices"); assert isinstance(al, list) and len(al) == 9, ("adopt_devices is not the nine", al)
norm = lambda x: x if isinstance(x, int) else int(str(x), 16)
want = {0xACEBE6FFFEF733DC, 0x4CE175B4C0700000, 0xACEBE6FFFEF25A2C}
assert want <= {norm(x) for x in al}, "the three T2 entries are not all in the list"
if "permit_join_duration" in d:
    assert d["permit_join_duration"] == 254, d["permit_join_duration"]; print("WINDOW KEY ALREADY PRESENT (kept)")
else:
    new = (s if s.endswith("\n") else s + "\n") + "permit_join_duration: 254   # THURSDAY ORDER T1b (2026-09-25): the recovery window; removed at T3\n"
    d2 = yaml.safe_load(new)
    assert d2["permit_join_duration"] == 254
    assert {k: v for k, v in d2.items() if k != "permit_join_duration"} == d
    p.write_text(new); print("WINDOW KEY WRITTEN")
PY
if [ -n "${DRY_RUN:-}" ]; then echo "DRY-RUN: no restart"; echo "T1b-END"; exit 0; fi
"$HOME/bench.sh" restart 2>&1 | tail -25
echo "== $(grep -h 'permit_join_opened' "$HOME/hs-bench/current.log" | tail -1 | cut -c1-200)"
echo "T1b-END"

# THURSDAY ORDER T1 (2026-09-24) — the pairing window. Run from Git Bash on the DESKTOP:
#   ssh pi 'bash -s' < <this file> > <the T1.txt beside it>
# Adds `permit_join_duration: 254` to zigbee.yaml (guarded: every assert before the write), then ~/bench.sh restart.
# The window (254 s) opens at this boot — start pairing right after T1-END.
set -u
Z="$HOME/hs-bench/config/integrations/zigbee.yaml"
python3 - "$Z" <<'PY' || { echo "T1-STOP — nothing written, nothing restarted"; exit 1; }
import sys, yaml, pathlib
p = pathlib.Path(sys.argv[1]); s = p.read_text(); d = yaml.safe_load(s)
assert isinstance(d, dict), "zigbee.yaml is not a mapping"
al = d.get("adopt_devices"); assert isinstance(al, list) and len(al) == 6, ("adopt_devices", al)
if "permit_join_duration" in d:
    assert d["permit_join_duration"] == 254, d["permit_join_duration"]; print("WINDOW KEY ALREADY PRESENT (kept)")
else:
    new = (s if s.endswith("\n") else s + "\n") + "permit_join_duration: 254   # THURSDAY ORDER T1 (2026-09-24): the pairing window; removed at T3\n"
    d2 = yaml.safe_load(new)
    assert d2["permit_join_duration"] == 254
    assert {k: v for k, v in d2.items() if k != "permit_join_duration"} == d
    p.write_text(new); print("WINDOW KEY WRITTEN")
PY
"$HOME/bench.sh" restart 2>&1 | tail -25
echo "== $(grep -h 'permit_join_opened' "$HOME/hs-bench/current.log" | tail -1 | cut -c1-200)"
echo "T1-END"

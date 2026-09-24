# THURSDAY ORDER T3 (2026-09-24) — close the window, then the capture. Run from Git Bash on the DESKTOP, AFTER `ADOPTED: 3`:
#   ssh pi 'bash -s' < <this file> > <the T3.txt beside it>
set -u
Z="$HOME/hs-bench/config/integrations/zigbee.yaml"; A=$(readlink -f "$HOME/hs-bench/current.log"); mkdir -p "$HOME/thu0924"
python3 - "$Z" <<'PY' || { echo "T3-STOP — nothing written, nothing restarted"; exit 1; }
import sys, re, yaml, pathlib
z = pathlib.Path(sys.argv[1]); s = z.read_text(); d = yaml.safe_load(s)
assert d.get("permit_join_duration") == 254 and isinstance(d.get("adopt_devices"), list) and len(d["adopt_devices"]) == 9
lines = s.split("\n"); idx = [i for i, l in enumerate(lines) if re.match(r"^permit_join_duration:\s*254\b", l)]
assert len(idx) == 1, "the window line is not exactly one"
del lines[idx[0]]; new = "\n".join(lines); d2 = yaml.safe_load(new)
assert "permit_join_duration" not in d2 and d2["adopt_devices"] == d["adopt_devices"]
assert {k: v for k, v in d2.items()} == {k: v for k, v in d.items() if k != "permit_join_duration"}
z.write_text(new); print("WINDOW KEY REMOVED · adopt_devices 9")
PY
"$HOME/bench.sh" restart 2>&1 | tail -20
for f in $(ls -t "$HOME"/hs-bench/bench-*.log | head -3); do cp -p "$f" "$HOME/thu0924/"; done
cp -p "$Z" "$HOME/thu0924/zigbee.yaml.after-T3"
grep -h 'device_adopted\|proposal_accepted\|proposal_incomplete\|interview_\|metering_formatting_read\|endpoint_classified\|reporting_configured' "$A" > "$HOME/thu0924/adoption-lines.txt"
grep -h 'registry.projection_live\|adoption_maps_rehydrated\|device_proposed' "$HOME/hs-bench/current.log" > "$HOME/thu0924/closed-boot-lines.txt"
T=$(cat "$HOME/hs-bench/config/initial_api_token")
curl -s -m 15 -H "Authorization: Bearer $T" http://127.0.0.1:7070/api/v1/entities > "$HOME/thu0924/entities-post.json"; unset T
echo "== adopted lines: $(grep -c 'device_adopted' "$HOME/thu0924/adoption-lines.txt") · $(grep -h 'projection_live' "$HOME/thu0924/closed-boot-lines.txt" | tail -1 | grep -o 'devices=[0-9]* entities=[0-9]*') · proposals at the closed boot: $(grep -c 'device_proposed' "$HOME/thu0924/closed-boot-lines.txt")"
python3 -c 'import json,os; d=json.load(open(os.path.expanduser("~/thu0924/entities-post.json")))["data"]; print("entities rows", len(d), "devices", len({r["deviceId"] for r in d}))'
echo "== Bearer in the capture: $(grep -rc 'Bearer' "$HOME/thu0924" | awk -F: '{s+=$2} END {print s+0}')"
echo "T3-END"

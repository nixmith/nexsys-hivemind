# THURSDAY ORDER T0 (2026-09-24) — the pre-read and the one backup. Run from Git Bash on the DESKTOP:
#   ssh pi 'bash -s' < <this file> > <the T0.txt beside it>
# Writes ONE file on the Pi: the zigbee.yaml backup (never overwritten if it exists). Reads everything else.
set -u
echo "== T0 $(hostname) $(date -u +%FT%TZ)"
Z="$HOME/hs-bench/config/integrations/zigbee.yaml"; BK="$Z.pre-adopt-2026-09-24"
echo "== zigbee.yaml $(wc -c < "$Z") B md5 $(md5sum "$Z" | cut -c1-12)"; cat -n "$Z"
if [ -e "$BK" ]; then echo "BACKUP KEPT (exists): $BK"; else cp -p "$Z" "$BK" && echo "BACKUP WRITTEN: $BK"; fi
cmp -s "$Z" "$BK" && echo "backup == live" || echo "BACKUP DIFFERS FROM LIVE"
python3 - "$Z" <<'PY'
import sys, yaml
d = yaml.safe_load(open(sys.argv[1]))
al = d.get("adopt_devices") if isinstance(d, dict) else None
print("keys:", sorted(d.keys()) if isinstance(d, dict) else type(d).__name__,
      "· adopt_devices:", len(al) if isinstance(al, list) else al,
      "· permit_join_duration:", d.get("permit_join_duration") if isinstance(d, dict) else None)
PY
echo "== nightly: $(tail -1 "$HOME/hs-bench/digests/nightly.log" | cut -c1-230)"
echo "== app: $(pgrep -af '[c]om.homesynapse.app.Main' | head -1 | cut -c1-60)"
C="$HOME/hs-bench/config/homesynapse.yaml"
echo "== carrier md5 $(md5sum "$C" | cut -c1-12) (a239bd60b40a on 09-23) · live-basis $(cmp -s "$C" "$HOME/hs-bench/quiesce-hold/homesynapse.live-basis.yaml" && echo IDENTICAL || echo DIFFERS)"
echo "== tmux: $(command -v tmux || echo ABSENT)"
T=$(cat "$HOME/hs-bench/config/initial_api_token")
curl -s -m 15 -H "Authorization: Bearer $T" http://127.0.0.1:7070/api/v1/entities | python3 -c 'import sys,json; d=json.load(sys.stdin)["data"]; print("entities rows", len(d), "devices", len({r["deviceId"] for r in d}))'
unset T
echo "T0-END"

# THURSDAY ORDER T2 (2026-09-24) — the adoption list. Run from Git Bash on the DESKTOP, AFTER the three proposals:
#   ssh pi 'bash -s' < <this file> > <the T2.txt beside it>
# Reads the T1 boot's own `zigbee.device_proposed` lines (no hex typed by hand), appends the three IEEEs to
# adopt_devices in pairing order (G4-1 · TR3 · G4-2), keeps the window open, then ~/bench.sh restart.
set -u
Z="$HOME/hs-bench/config/integrations/zigbee.yaml"; LOG=$(readlink -f "$HOME/hs-bench/current.log")
mkdir -p "$HOME/thu0924"; echo "$LOG" > "$HOME/thu0924/T1-boot-log.path"
echo "== T2 reads the T1 boot log: $LOG"
python3 - "$Z" "$LOG" <<'PY' || { echo "T2-STOP — nothing written, nothing restarted"; exit 1; }
import sys, re, yaml, pathlib
z = pathlib.Path(sys.argv[1]); s = z.read_text(); d = yaml.safe_load(s)
norm = lambda x: x if isinstance(x, int) else int(str(x), 16)
al = d["adopt_devices"]; assert isinstance(al, list) and len(al) == 6, "adopt_devices is not the six"
assert d.get("permit_join_duration") == 254, "the window key is absent — T1 did not run"
known = {norm(x) for x in al}
pat = re.compile(r"zigbee\.device_proposed: device=(0x[0-9A-Fa-f]{16}) manufacturer=(.*?) model=(.*?) profile=(.*?) status=(\S+) source=(\S+)")
seen = []
for line in open(sys.argv[2], errors="replace"):
    m = pat.search(line)
    if m and norm(m.group(1)) not in known and m.group(1) not in [g[0] for g in seen]:
        seen.append(m.groups())
for g in seen: print("PROPOSED", g[0], "| manufacturer=", g[1], "| model=", g[2], "| status=", g[4])
assert len(seen) == 3, f"expected 3 new proposals, read {len(seen)}"
assert seen[0][2] == seen[2][2] and seen[1][2] != seen[0][2], "the pairing order is not G4 · TR3 · G4 by model"
if any(g[4] != "COMPLETE" for g in seen): print("NOTE: an interview was not COMPLETE at T1 — T2's power-cycle re-interviews")
lines = s.split("\n")
idx = [i for i, l in enumerate(lines) if re.match(r"""^\s*-\s*["']?(0[xX])?[0-9A-Fa-f]{16}""", l)]
assert len(idx) == 6 and idx == list(range(idx[0], idx[0] + 6)), "the adopt list is not six contiguous items"
m = re.match(r"""^(\s*-\s*)(["']?)""", lines[idx[-1]]); prefix, q = m.group(1), m.group(2)
labels = ["G4-1", "TR3", "G4-2"]
lines[idx[-1] + 1: idx[-1] + 1] = [f"{prefix}{q}{g[0]}{q}    # {lab} — {g[1]} {g[2]} (THURSDAY ORDER T2, 2026-09-24)" for g, lab in zip(seen, labels)]
new = "\n".join(lines); d2 = yaml.safe_load(new)
assert [norm(x) for x in d2["adopt_devices"]] == [norm(x) for x in al] + [norm(g[0]) for g in seen]
assert d2.get("permit_join_duration") == 254
assert {k: v for k, v in d2.items() if k != "adopt_devices"} == {k: v for k, v in d.items() if k != "adopt_devices"}
z.write_text(new)
(pathlib.Path.home() / "thu0924" / "labels.txt").write_text("".join(f"{lab} {g[0]} | {g[1]} | {g[2]}\n" for g, lab in zip(seen, labels)))
print("ADOPT LIST WRITTEN: 6 + 3")
PY
"$HOME/bench.sh" restart 2>&1 | tail -25
echo "T2-END"

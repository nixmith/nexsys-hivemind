# context/process/render_state.py — THE RENDERER (BEAT-RENDERER-1 U1c; minted 2026-10-09 in the worktree at 513d1c0).
# Purpose: the two capped digest regions are GENERATED, never hand-cut — the volatile facts live in context/status/state.yaml
# (the hub edits it), the prose skeletons in context/process/templates/*.tpl.md (the library's `fill()` slots, `@@key@@`), and
# this file fills, asserts every cap BEFORE any byte, and writes the regions by the anchors the splice library already guards.
#   --selftest  renders context/process/fixtures/v99b1_state.yaml and compares BYTES with the fixture's two expected regions
#   --check     renders the LIVE state.yaml and compares with the two live regions: MATCH|DIFF <region> <bytes> ≤ <cap> per
#               region and per file (exit 1 on a DIFF or a cap breach; a DIFF names the first differing byte offset)
#   --write [--snapshot PATH --brief PATH]  writes the two rendered regions into the files by anchor (`## The digest` → end of
#               file; `## §DIGEST` → the line before `## §NEXT`) after every cap passes — the hub's beat runs it; a lane runs
#               it ONLY on temp copies (the path flags exist for that and for the tests)
# The regions: context/status/PROJECT_SNAPSHOT.md and context/handoff/OPERATOR-BRIEF_for-Nick.md, resolved from THIS file's
# location (the repository root two levels up), so the same file serves a worktree and the hub's tree. The caps are IMPORTED from
# splice_lib_v2 (SNAP_CAP, BRIEF_CAP); DIGEST_CAP = 2048 (W-HIVE-1 P9) is the one number named here. Standard library + PyYAML.
import sys; sys.dont_write_bytecode = True
import argparse, importlib.util, pathlib
import yaml

HERE = pathlib.Path(__file__).resolve().parent            # context/process
ROOT = HERE.parents[1]                                    # the repository root (a worktree or the hub's tree)
LIBP = HERE / "splice_lib_v2.py"; TPL = HERE / "templates"; FIX = HERE / "fixtures"
P_STATE = ROOT / "context/status/state.yaml"
P_SNAP = ROOT / "context/status/PROJECT_SNAPSHOT.md"
P_BRIEF = ROOT / "context/handoff/OPERATOR-BRIEF_for-Nick.md"
LIB_V2_MD5 = "99e87f2dbafaade35e071770b14b5557"
DIGEST_CAP = 2048                                         # W-HIVE-1 P9: the digest ≤ 2 KB; the brief's §DIGEST heading carries the same ceiling
A_SNAP, A_BRIEF, A_NEXT = "## The digest", "## §DIGEST", "## §NEXT"
T_SNAP, T_BRIEF = "snapshot_digest.tpl.md", "brief_digest.tpl.md"
# THE ONE LIST MECHANISM: a list renders by sep.join(items) into the slot of its key; the separator per key lives here.
SEPS = {"notes": " ", "week": " · ", "dates": " · ", "next_acts": " → ", "brief.notes": " ", "brief.week": " · ", "brief.yours": " · "}
LANE_READY = "DISPATCH-READY"                             # `lanes` rows: this state → lanes.ready; every other state → lanes.running

def _lib():
    spec = importlib.util.spec_from_file_location("splice_lib_v2", LIBP); lib = importlib.util.module_from_spec(spec); spec.loader.exec_module(lib)
    assert lib.lib_md5() == LIB_V2_MD5, lib.lib_md5(); return lib
lib = _lib(); SNAP_CAP, BRIEF_CAP = lib.SNAP_CAP, lib.BRIEF_CAP
nb, rd, wr = lib.nbytes, lib.rd, lib.wr

def load_state(path=P_STATE):
    d = yaml.safe_load(pathlib.Path(path).read_text(encoding="utf-8")); assert isinstance(d, dict) and d, f"state: not a mapping: {path}"; return d

def slots(state):
    """The state flattened into fill() slots: a scalar by its dotted key; a list by ONE join (SEPS); `lanes` rows as name (next), joined by state."""
    out = {}
    def row(r): return r["name"] + (f" ({r['next']})" if r["next"] else "")
    def walk(key, v):
        if isinstance(v, dict):
            for k, x in v.items(): walk(f"{key}.{k}" if key else str(k), x)
        elif isinstance(v, list):
            if key == "lanes":
                for i, r in enumerate(v):
                    assert isinstance(r, dict) and set(r) == {"name", "state", "next"}, f"lanes[{i}]: the keys are name, state, next"
                    for k, x in r.items(): assert isinstance(x, str) and "@@" not in x, f"lanes[{i}].{k}: a quoted string without @@"
                out["lanes.ready"] = " · ".join(row(r) for r in v if r["state"] == LANE_READY) or "none"
                out["lanes.running"] = " · ".join(row(r) for r in v if r["state"] != LANE_READY) or "none"
            else:
                assert key in SEPS, f"list {key!r}: no separator in SEPS"
                for i, x in enumerate(v): assert isinstance(x, str) and "@@" not in x, f"{key}[{i}]: a quoted string without @@"
                out[key] = SEPS[key].join(v)
        else:
            assert isinstance(v, str), f"{key}: every scalar is a quoted string (got {type(v).__name__}: {v!r})"
            assert "@@" not in v, f"{key}: a value never carries a slot"
            out[key] = v
    walk("", state); return out

def render(state, tpl_dir=TPL):
    """The two regions rendered: the library's fill() (an unfilled slot is REFUSED there); the trailer grep on both."""
    s = slots(state); ts = rd(tpl_dir / T_SNAP); tb = rd(tpl_dir / T_BRIEF)
    unused = sorted(k for k in s if f"@@{k}@@" not in ts + tb)
    snap, brief = lib.fill(ts, s), lib.fill(tb, s); lib.no_trailers(snap, brief)
    assert snap.endswith("\n") and brief.endswith("\n"), "a region ends with one newline"
    return snap, brief, unused

def regions(snap_text, brief_text):
    """The two live regions by their anchors — each anchor counted exactly once before any read (the once() discipline)."""
    assert snap_text.count(A_SNAP) == 1, f"anchor count {snap_text.count(A_SNAP)}: {A_SNAP!r}"
    assert brief_text.count(A_BRIEF) == 1 and brief_text.count(A_NEXT) == 1, f"anchor counts {brief_text.count(A_BRIEF)} {brief_text.count(A_NEXT)}: {A_BRIEF!r} {A_NEXT!r}"
    i, j, k = snap_text.index(A_SNAP), brief_text.index(A_BRIEF), brief_text.index(A_NEXT); assert j < k, "§DIGEST before §NEXT"
    return snap_text[i:], brief_text[j:k]

def splice(snap_text, brief_text, snap_region, brief_region):
    """The whole files with their regions replaced, EVERY cap asserted before the caller writes a byte; returns the texts and the caps."""
    regions(snap_text, brief_text); i, j, k = snap_text.index(A_SNAP), brief_text.index(A_BRIEF), brief_text.index(A_NEXT)
    new_s, new_b = snap_text[:i] + snap_region, brief_text[:j] + brief_region + brief_text[k:]
    caps = {"snapshot-digest": (nb(snap_region), DIGEST_CAP), "snapshot-file": (nb(new_s), SNAP_CAP),
            "brief-digest": (nb(brief_region), DIGEST_CAP), "brief-file": (nb(new_b), BRIEF_CAP)}
    for name, (v, cap) in caps.items(): assert v <= cap, f"CAP {name} {v} > {cap}"
    lib.no_trailers(new_s, new_b); assert new_s.endswith("\n") and new_b.endswith("\n"); return new_s, new_b, caps

def _first_diff(a, b):
    n = next((i for i, (x, y) in enumerate(zip(a, b)) if x != y), min(len(a), len(b))); return f"at byte {n}: got {a[n:n+24]!r} want {b[n:n+24]!r}"

def check(state_path=P_STATE, snap_path=P_SNAP, brief_path=P_BRIEF, out=print):
    """MATCH|DIFF <region> <bytes> ≤ <cap> for both regions and both files; exit 1 on any DIFF or cap breach."""
    snap_r, brief_r, unused = render(load_state(state_path)); s_t, b_t = rd(snap_path), rd(brief_path)
    live_s, live_b = regions(s_t, b_t); i, j, k = s_t.index(A_SNAP), b_t.index(A_BRIEF), b_t.index(A_NEXT)
    new_s, new_b = s_t[:i] + snap_r, b_t[:j] + brief_r + b_t[k:]
    rows = (("snapshot-digest", snap_r, live_s, DIGEST_CAP), ("snapshot-file", new_s, s_t, SNAP_CAP), ("brief-digest", brief_r, live_b, DIGEST_CAP), ("brief-file", new_b, b_t, BRIEF_CAP))
    ok = True
    for name, got, want, cap in rows:
        g, w = got.encode("utf-8"), want.encode("utf-8"); same = g == w; fits = len(g) <= cap; ok = ok and same and fits
        out(f"{'MATCH' if same else 'DIFF'} {name} {len(g)} {'≤' if fits else '>'} {cap}" + ("" if same else " " + _first_diff(g, w)))
    if unused: out("INFO unused keys: " + " ".join(unused))
    return 0 if ok else 1

def write(state, snap_path, brief_path, out=print):
    """The two regions written by anchor AFTER every cap passes (splice); the hub's beat runs it, a lane only on copies."""
    snap_r, brief_r, _ = render(state); new_s, new_b, caps = splice(rd(snap_path), rd(brief_path), snap_r, brief_r)
    wr(pathlib.Path(snap_path), new_s); wr(pathlib.Path(brief_path), new_b)
    for p, t in ((snap_path, new_s), (brief_path, new_b)): out(f"WROTE {p} {nb(t)}")
    return caps

def selftest(out=print):
    """The fixture state through the templates == the fixture's expected regions, at the bytes."""
    snap_r, brief_r, _ = render(load_state(FIX / "v99b1_state.yaml")); fails = 0
    for name, got, want in (("snapshot-digest", snap_r, FIX / "v99b1_snapshot_digest.expected.md"), ("brief-digest", brief_r, FIX / "v99b1_brief_digest.expected.md")):
        g, w = got.encode("utf-8"), want.read_bytes(); same = g == w; fails += (not same)
        out(f"{'MATCH' if same else 'DIFF'} {name} {len(g)} ≤ {DIGEST_CAP}" + ("" if same else " " + _first_diff(g, w)))
    out(f"render_state selftest: 2 check(s), {fails} failure(s)"); return 1 if fails else 0

def main(argv=None):
    ap = argparse.ArgumentParser(description="render the two digest regions from context/status/state.yaml")
    g = ap.add_mutually_exclusive_group(required=True)
    g.add_argument("--selftest", action="store_true"); g.add_argument("--check", action="store_true"); g.add_argument("--write", action="store_true")
    ap.add_argument("--snapshot", default=str(P_SNAP)); ap.add_argument("--brief", default=str(P_BRIEF)); a = ap.parse_args(argv)
    if a.selftest: return selftest()
    if a.check: return check(P_STATE, pathlib.Path(a.snapshot), pathlib.Path(a.brief))
    write(load_state(P_STATE), pathlib.Path(a.snapshot), pathlib.Path(a.brief)); return 0

if __name__ == "__main__": sys.exit(main())

# context/process/test_splice_lib_v3.py — beat()'s four cases on tempfile COPIES of the spine (BEAT-RENDERER-1 U2; red first).
# Run: python3 -B context/process/test_splice_lib_v3.py — the live spine is read, copied and never written; the copies live in a
# tempfile.TemporaryDirectory() that mirrors the repository layout, with a throwaway git repo for the census case.
import sys; sys.dont_write_bytecode = True
import hashlib, importlib.util, pathlib, shutil, subprocess, tempfile
HERE = pathlib.Path(__file__).resolve().parent; ROOT = HERE.parents[1]
V2, V3 = HERE / "splice_lib_v2.py", HERE / "splice_lib_v3.py"
spec = importlib.util.spec_from_file_location("splice_lib_v3", V3); lib = importlib.util.module_from_spec(spec); spec.loader.exec_module(lib)
REL = {"handoff": "context/handoff/pm-handoff.md", "archive": "context/handoff/archive/chains-rotated-2026-08-27.md",
       "snapshot": "context/status/PROJECT_SNAPSHOT.md", "brief": "context/handoff/OPERATOR-BRIEF_for-Nick.md"}
STATE = ROOT / "context/status/state.yaml"
def md5(p): return hashlib.md5(pathlib.Path(p).read_bytes()).hexdigest()
def copies(tmp, drop_oldest=0):
    """The four spine files copied into tmp (layout mirrored); drop_oldest removes that many of the oldest live blocks from the copy."""
    paths = {}
    for k, rel in REL.items():
        p = pathlib.Path(tmp) / rel; p.parent.mkdir(parents=True, exist_ok=True); shutil.copyfile(ROOT / rel, p); paths[k] = p
    if drop_oldest:
        hl = lib.rd(paths["handoff"]).split("\n"); heads, end = lib.live_blocks(hl); lib.wr(paths["handoff"], "\n".join(hl[:heads[-drop_oldest]] + hl[end:]))
    return paths
def git(tmp, *args): return subprocess.run(["git", "-c", "user.email=t@t", "-c", "user.name=t", *args], cwd=tmp, capture_output=True, text=True)
def ctx_for(paths, state=True, block=None):
    return {"paths": paths, "beat_prefix_old": "2026-10-08 (v100 beat 3",
            "seg0": "2026-10-09 (v101 beat 9 — THE TEST BEAT of splice_lib_v3 on a temp copy; Fri 2026-10-09 ~12:4x CT (2026-10-09T17:40:00Z). Detail: pm-handoff v101 b9.",
            "pointer_edits": [("EVERY SEGMENT v55 b3 → v99 b2 ROTATED", "EVERY SEGMENT v55 b3 → v100 b2 ROTATED"),
                              ("258 rotations through v99 b4; the v99 b3 segment is the one Prior above", "262 rotations through v101 b9; the v100 b3 segment is the one Prior above")],
            "beat_block": block or "## 2026-10-09 (v101 beat 9 — **THE TEST BEAT** of splice_lib_v3's beat() on a temp copy; nothing live.)\n- **The files (0):** none — a test.\n- ctx: test\n",
            "snapshot_seg0": "2026-10-09 (v101 beat 9 — THE TEST BEAT; Fri 2026-10-09 ~12:4x CT (2026-10-09T17:40:00Z). Detail: pm-handoff v101 b9.",
            "rotation_heading": "chain segment rotated 2026-10-09 (v101 beat 9) — v100 b2, verbatim", "archive_count": 261,
            "date": "2026-10-09", "beat_label": "v101 beat 9", "ct": "Fri 2026-10-09 ~12:4x CT", "stamp": "2026-10-09T17:40:00Z",
            "state_path": STATE if state else None}
LIVE0 = {k: md5(ROOT / rel) for k, rel in REL.items()}
RESULTS = []
def check(name, fn):
    try: fn(); RESULTS.append((name, "")); print(f"ok   {name}")
    except Exception as e: RESULTS.append((name, f"{type(e).__name__}: {e}"[:400])); print(f"FAIL {name}: {RESULTS[-1][1]}")

def c0_v2_verbatim():
    v2, v3 = V2.read_bytes(), V3.read_bytes(); assert hashlib.md5(v2).hexdigest() == "99e87f2dbafaade35e071770b14b5557", "v2 edited"
    assert v2 in v3 and v3.startswith(b"# context/process/splice_lib_v3.py") and b"\r" not in v3, "v3 does not carry v2 byte for byte"
    assert lib.lib_md5() == hashlib.md5(v3).hexdigest() and lib.CHAIN_CAP == 3000 and lib.LIVE_BEATS_CAP == 12

def c1_insert_below_cap_with_census():
    with tempfile.TemporaryDirectory() as tmp:
        paths = copies(tmp, drop_oldest=1); hl0 = lib.rd(paths["handoff"]).split("\n"); assert len(lib.live_blocks(hl0)[0]) == 11
        assert git(tmp, "init", "-q").returncode == 0 and git(tmp, "add", "-A").returncode == 0 and git(tmp, "commit", "-q", "-m", "init").returncode == 0
        ctx = ctx_for(paths); ctx.update({"repo": pathlib.Path(tmp), "exp_M": {REL["handoff"], REL["archive"], REL["snapshot"]}, "exp_A": set(),
                                         "card": {"repo_key": "hivemind", "paths": sorted(REL.values()), "msg_rel": "v101/b9/msg.txt", "say_back": "HIVE: LANDED <sha>"}})
        out = lib.beat(ctx)
        hl = lib.rd(paths["handoff"]).split("\n"); heads, _ = lib.live_blocks(hl); assert len(heads) == 12 and out["live"] == 12 and out["rotation"] is None
        assert hl[heads[0]] == ctx["beat_block"].split("\n")[0] and hl[heads[0] + 3] == "" and hl[heads[1]].startswith("## 2026-10-08 (v100 beat 3"), "the block sits first, one blank line after"
        assert out["census"] == (3, 3, 0, 0), out["census"]; assert "git add -- " in out["card"] and out["card"].count("Co-Authored\\|Claude-Session") == 1
        assert all(v <= cap for v, cap in out["caps"].values()) and set(out["caps"]) >= {"chain", "beat", "snapshot", "brief", "snapshot-digest", "brief-digest"}
        assert md5(paths["brief"]) == LIVE0["brief"], "the brief changed without a §DIGEST change"   # the rendered §DIGEST == the live one at this sha

def c2_rotation_at_cap():
    with tempfile.TemporaryDirectory() as tmp:
        paths = copies(tmp); h0 = lib.rd(paths["handoff"]); hl0 = h0.split("\n"); heads0, end0 = lib.live_blocks(hl0); assert len(heads0) == 12
        oldest6 = "\n".join(hl0[heads0[-6]:end0]); first_head, last_head = hl0[heads0[-1]], hl0[heads0[-6]]
        out = lib.beat(ctx_for(paths)); rot = out["rotation"]; assert rot and rot["rows_out"] == 6 and rot["live_before"] == 12 and out["live"] == 7
        assert rot["name"] == "pm-handoff-beats-v98b1-v99b1-rotated-2026-10-09.md", rot["name"]; arch = lib.rd(rot["path"])
        assert arch.endswith(oldest6 + "\n") and arch.count("\n## 20") == 6 and arch.index(last_head) < arch.index(first_head), "the six oldest, verbatim, newest first"
        assert "# pm-handoff beats rotated at v101 beat 9 — v99 b1 → v98 b1 (newest first, verbatim)" in arch
        kept, body, before = rot["bytes"]; assert kept + body + 1 == before and body == lib.nbytes(oldest6)
        h = lib.rd(paths["handoff"]); hl = h.split("\n"); heads, _ = lib.live_blocks(hl); assert len(heads) == 7 and oldest6 not in h and h.count(rot["map_row"]) == 1
        assert hl[-1] == "" and hl[-2] == rot["map_row"], "the map row is the map's last row"
        assert "v99 b1 → v98 b1 (6 blocks; 2026-10-07 → 2026-10-04) → `archive/pm-handoff-beats-v98b1-v99b1-rotated-2026-10-09.md`" in rot["map_row"], rot["map_row"]

def c3_chain_split_and_recut():
    with tempfile.TemporaryDirectory() as tmp:
        paths = copies(tmp); ctx = ctx_for(paths, state=False)
        seg0_old, seg1_old, ptr_old = lib.chain_split(lib.rd(paths["handoff"]).split("\n")[7], "2026-10-08 (v100 beat 3")
        s_old = lib.rd(paths["snapshot"]).split("\n")[7]; sseg0_old, _, sptr = lib.chain_split(s_old, "2026-10-08 (v100 beat 3"); a0 = lib.rd(paths["archive"]); b0 = md5(paths["brief"])
        out = lib.beat(ctx)
        line8 = lib.rd(paths["handoff"]).split("\n")[7]; seg0, seg1, ptr = lib.chain_split(line8, "2026-10-09 (v101 beat 9")
        assert seg0 == ctx["seg0"] and seg1 == seg0_old, "seg0 → Prior"
        want_ptr = ptr_old
        for old, new in ctx["pointer_edits"]: want_ptr = lib.once(want_ptr, old, new)
        assert ptr == want_ptr and "262 rotations through v101 b9" in ptr and lib.nbytes(line8) <= lib.CHAIN_CAP
        a = lib.rd(paths["archive"]); assert a.startswith(a0) and a.endswith(f"\n## {ctx['rotation_heading']}\n\n{seg1_old})\n") and a.count("\n## ") == 262
        s8 = lib.rd(paths["snapshot"]).split("\n")[7]; assert s8 == f"last-verified: {ctx['snapshot_seg0']}) Prior: {sseg0_old}) Prior: {sptr}"
        assert md5(paths["brief"]) == b0 and out["caps"]["snapshot"][0] <= lib.SNAP_CAP, "no state → the brief untouched"

def c4_overcap_block_refused():
    with tempfile.TemporaryDirectory() as tmp:
        paths = copies(tmp); before = {k: md5(p) for k, p in paths.items()}; listing = sorted(str(p) for p in pathlib.Path(tmp).rglob("*"))
        big = "## 2026-10-09 (v101 beat 9 — **OVER THE CAP** " + "x" * lib.BEAT_CAP + ")\n"
        try: lib.beat(ctx_for(paths, block=big)); raise AssertionError("not refused")
        except AssertionError as e: assert str(e).startswith(f"CAP beat {lib.nbytes(big)} > {lib.BEAT_CAP}"), f"refused for another reason: {e}"
        assert {k: md5(p) for k, p in paths.items()} == before and sorted(str(p) for p in pathlib.Path(tmp).rglob("*")) == listing, "a byte or a file changed"

for name, fn in (("v2 carried byte for byte; v2's md5 unchanged; v3 pins by lib_md5()", c0_v2_verbatim),
                 ("case 1 — the insert at live 11 < 12; the census from porcelain (3 M); the card", c1_insert_below_cap_with_census),
                 ("case 2 — the rotation at live 12: the oldest six out verbatim; bytes kept + body + 1 = before; the map row", c2_rotation_at_cap),
                 ("case 3 — the chain split and re-cut: seg0 → Prior → the pointer; the archive +1; the snapshot chain", c3_chain_split_and_recut),
                 ("case 4 — a block over BEAT_CAP REFUSED; every copy's md5 and the listing unchanged", c4_overcap_block_refused)):
    check(name, fn)
assert {k: md5(ROOT / rel) for k, rel in REL.items()} == LIVE0, "THE LIVE SPINE CHANGED"
fails = sum(1 for _, e in RESULTS if e); print(f"splice_lib_v3 selftest: {len(RESULTS)} check(s), {fails} failure(s)"); sys.exit(1 if fails else 0)

# context/process/test_render_state.py — the renderer's tests (BEAT-RENDERER-1 U1; written RED before the templates existed).
# Run: python3 -B context/process/test_render_state.py — every check runs on the fixture or on tempfile COPIES; the live spine
# is read only, and its md5s are asserted unchanged after the one --write that the tests perform on copies.
import sys; sys.dont_write_bytecode = True
import copy, hashlib, importlib.util, pathlib, shutil, subprocess, tempfile
import yaml
HERE = pathlib.Path(__file__).resolve().parent; ROOT = HERE.parents[1]; PY = sys.executable
spec = importlib.util.spec_from_file_location("render_state", HERE / "render_state.py"); rs = importlib.util.module_from_spec(spec); spec.loader.exec_module(rs)
FIX = HERE / "fixtures"; F_STATE = FIX / "v99b1_state.yaml"; F_SNAP = FIX / "v99b1_snapshot_digest.expected.md"; F_BRIEF = FIX / "v99b1_brief_digest.expected.md"
def rb(p): return pathlib.Path(p).read_bytes()
def md5(p): return hashlib.md5(rb(p)).hexdigest()
def live_md5s(): return md5(rs.P_SNAP), md5(rs.P_BRIEF)
def copies(tmp):
    s, b = pathlib.Path(tmp) / "PROJECT_SNAPSHOT.md", pathlib.Path(tmp) / "OPERATOR-BRIEF_for-Nick.md"; shutil.copyfile(rs.P_SNAP, s); shutil.copyfile(rs.P_BRIEF, b); return s, b
def expect_refused(fn, needle):
    try: fn()
    except AssertionError as e: assert needle in str(e), f"refused for another reason: {e}"; return
    raise AssertionError(f"not refused (expected {needle!r})")
RESULTS = []
def check(name, fn):
    try: fn(); RESULTS.append((name, "")); print(f"ok   {name}")
    except Exception as e: RESULTS.append((name, f"{type(e).__name__}: {e}"[:400])); print(f"FAIL {name}: {RESULTS[-1][1]}")

def t_fixture_snapshot_bytes():
    snap, _, _ = rs.render(rs.load_state(F_STATE)); g, w = snap.encode("utf-8"), rb(F_SNAP); assert g == w, rs._first_diff(g, w)
def t_fixture_brief_bytes():
    _, brief, _ = rs.render(rs.load_state(F_STATE)); g, w = brief.encode("utf-8"), rb(F_BRIEF); assert g == w, rs._first_diff(g, w)
def t_overcap_snapshot_digest_refused():
    st = rs.load_state(F_STATE); st["notes"].append("x" * (rs.DIGEST_CAP + 1))
    with tempfile.TemporaryDirectory() as tmp:
        s, b = copies(tmp); m = md5(s), md5(b); expect_refused(lambda: rs.write(st, s, b, out=lambda *_: None), "CAP snapshot-digest"); assert (md5(s), md5(b)) == m, "a byte was written"
def t_overcap_brief_digest_refused():
    st = rs.load_state(F_STATE); st["brief"]["notes"].append("x" * (rs.DIGEST_CAP + 1))
    with tempfile.TemporaryDirectory() as tmp:
        s, b = copies(tmp); m = md5(s), md5(b); expect_refused(lambda: rs.write(st, s, b, out=lambda *_: None), "CAP brief-digest"); assert (md5(s), md5(b)) == m, "a byte was written"
def t_overcap_snapshot_file_refused():
    st = rs.load_state(F_STATE); snap, _, _ = rs.render(st); head = rs.rd(rs.P_SNAP); head = head[:head.index(rs.A_SNAP)]
    pad = rs.SNAP_CAP - rs.nb(head) - rs.nb(snap) + 1; assert 0 < pad and rs.nb(snap) + pad <= rs.DIGEST_CAP, (pad, rs.nb(snap))  # the digest fits, the FILE does not
    st["notes"].append("x" * (pad - 1))
    with tempfile.TemporaryDirectory() as tmp:
        s, b = copies(tmp); m = md5(s), md5(b); expect_refused(lambda: rs.write(st, s, b, out=lambda *_: None), "CAP snapshot-file"); assert (md5(s), md5(b)) == m, "a byte was written"
def t_yaml_roundtrip():
    text = F_STATE.read_text(encoding="utf-8"); d = yaml.safe_load(text); assert d == rs.load_state(F_STATE), "the renderer used another dict"
    assert yaml.safe_load(yaml.safe_dump(d, allow_unicode=True, sort_keys=False)) == d, "safe_dump/safe_load does not round-trip"
    assert "\r" not in text and all(isinstance(v, str) for v in rs.slots(d).values())
def t_unfilled_slot_refused():
    with tempfile.TemporaryDirectory() as tmp:
        t = pathlib.Path(tmp); shutil.copyfile(rs.TPL / rs.T_BRIEF, t / rs.T_BRIEF); rs.wr(t / rs.T_SNAP, rs.rd(rs.TPL / rs.T_SNAP) + "@@no_such_field@@\n")
        expect_refused(lambda: rs.render(rs.load_state(F_STATE), tpl_dir=t), "unfilled slot")
def t_every_scalar_verbatim():
    both = rb(F_SNAP).decode("utf-8") + rb(F_BRIEF).decode("utf-8"); n = 0
    def walk(v):
        nonlocal n
        if isinstance(v, dict): [walk(x) for x in v.values()]
        elif isinstance(v, list): [walk(x) for x in v]
        else: n += 1; assert isinstance(v, str) and v in both, f"not a verbatim substring of the regions: {v[:60]!r}"
    walk(rs.load_state(F_STATE)); assert n >= 40, n
def t_write_fixture_state_on_copies():
    with tempfile.TemporaryDirectory() as tmp:
        s, b = copies(tmp); m0 = live_md5s(); caps = rs.write(rs.load_state(F_STATE), s, b, out=lambda *_: None)
        got_s, got_b = rs.regions(rs.rd(s), rs.rd(b)); assert got_s.encode("utf-8") == rb(F_SNAP) and got_b.encode("utf-8") == rb(F_BRIEF)
        assert all(v <= cap for v, cap in caps.values()) and live_md5s() == m0, "the live files changed"
def t_write_cli_on_copies():
    with tempfile.TemporaryDirectory() as tmp:
        s, b = copies(tmp); m0 = live_md5s()
        r = subprocess.run([PY, "-B", str(HERE / "render_state.py"), "--write", "--snapshot", str(s), "--brief", str(b)], capture_output=True, text=True, encoding="utf-8")
        assert r.returncode == 0 and r.stdout.count("WROTE ") == 2, (r.returncode, r.stdout, r.stderr)
        want_s, want_b, _ = rs.render(rs.load_state(rs.P_STATE)); got_s, got_b = rs.regions(rs.rd(s), rs.rd(b))
        assert got_s == want_s and got_b == want_b and live_md5s() == m0, "the live files changed"
def t_selftest_cli():
    r = subprocess.run([PY, "-B", str(HERE / "render_state.py"), "--selftest"], capture_output=True, text=True, encoding="utf-8")
    assert r.returncode == 0 and r.stdout.rstrip().endswith("render_state selftest: 2 check(s), 0 failure(s)"), (r.returncode, r.stdout, r.stderr)
def t_check_cli_live():
    r = subprocess.run([PY, "-B", str(HERE / "render_state.py"), "--check"], capture_output=True, text=True, encoding="utf-8")
    assert r.returncode == 0 and r.stdout.count("MATCH ") == 4 and "DIFF" not in r.stdout, (r.returncode, r.stdout, r.stderr)
def t_no_pycache():
    assert not list(ROOT.glob("context/**/__pycache__")), "a __pycache__ in the tree"

for name, fn in (("fixture snapshot-digest byte-equal", t_fixture_snapshot_bytes), ("fixture brief-digest byte-equal", t_fixture_brief_bytes),
                 ("over-cap snapshot-digest refused, nothing written", t_overcap_snapshot_digest_refused), ("over-cap brief-digest refused, nothing written", t_overcap_brief_digest_refused),
                 ("over-cap snapshot-file refused, nothing written", t_overcap_snapshot_file_refused), ("yaml.safe_load round-trips the dict the renderer used", t_yaml_roundtrip),
                 ("unfilled slot refused by fill()", t_unfilled_slot_refused), ("every fixture scalar a quoted verbatim substring", t_every_scalar_verbatim),
                 ("write(fixture state) on temp copies == fixture bytes; live md5s unchanged", t_write_fixture_state_on_copies),
                 ("--write CLI on temp copies; live md5s unchanged", t_write_cli_on_copies), ("--selftest exits 0 with its closing line", t_selftest_cli),
                 ("--check against the live files: 4 MATCH", t_check_cli_live), ("no __pycache__ in the tree", t_no_pycache)):
    check(name, fn)
fails = sum(1 for _, e in RESULTS if e); print(f"render_state tests: {len(RESULTS)} check(s), {fails} failure(s)"); sys.exit(1 if fails else 0)

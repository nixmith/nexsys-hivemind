# context/process/test_render_state.py — the renderer's tests (BEAT-RENDERER-1 U1, written RED before the templates existed; BEAT-RENDERER-2
# U1 re-pointed them at the v104b1 fixture and added the five-region, probe, cap, cp1252, pipe, unread-key and DIFF-path checks, RED first).
# Run: PYTHONIOENCODING=utf-8 python3 -B context/process/test_render_state.py — every write runs on tempfile COPIES. The fixture-state checks
# run on FROZEN copies built only from the fixture's expected regions (never the live spine, whose hand-cut text moves every beat), each
# over-cap filler sized from the would-be bytes; only --check, --write and --probe against the live files track the live state. The
# worktree's own snapshot, brief and state.yaml are read only, and their md5s are asserted unchanged around every write and probe.
import sys; sys.dont_write_bytecode = True
import hashlib, importlib.util, os, pathlib, shutil, subprocess, tempfile
import yaml
HERE = pathlib.Path(__file__).resolve().parent; ROOT = HERE.parents[1]; PY = sys.executable; RS = str(HERE / "render_state.py")
spec = importlib.util.spec_from_file_location("render_state", HERE / "render_state.py"); rs = importlib.util.module_from_spec(spec); spec.loader.exec_module(rs)
FIX = HERE / "fixtures"; F_STATE = FIX / "v104b1_state.yaml"
NAMES = ("snapshot-digest", "brief-status", "brief-digest", "brief-held", "brief-words")
def f_exp(name): return FIX / ("v104b1_" + name.replace("-", "_") + ".expected.md")
def rb(p): return pathlib.Path(p).read_bytes()
def md5(p): return hashlib.md5(rb(p)).hexdigest()
def live_md5s(): return md5(rs.P_SNAP), md5(rs.P_BRIEF), md5(rs.P_STATE)
def copies(tmp):
    s, b = pathlib.Path(tmp) / "PROJECT_SNAPSHOT.md", pathlib.Path(tmp) / "OPERATOR-BRIEF_for-Nick.md"; shutil.copyfile(rs.P_SNAP, s); shutil.copyfile(rs.P_BRIEF, b); return s, b
def frozen(tmp, snap_pad=0, brief_pad=0, brief_tail=""):
    """A snapshot and a brief built ONLY from the fixture's expected regions: every anchor once, the regions in file order; snap_pad and
    brief_pad bytes of filler outside the regions size a file exactly; brief_tail is appended after `## §DONE`."""
    R = {n: rb(f_exp(n)).decode("utf-8") for n in NAMES}; s, b = pathlib.Path(tmp) / "PROJECT_SNAPSHOT.md", pathlib.Path(tmp) / "OPERATOR-BRIEF_for-Nick.md"
    rs.wr(s, "<!--\nfile: a frozen test copy\n-->\n# Project Snapshot\n\n" + "s" * snap_pad + "\n\n" + R["snapshot-digest"])
    rs.wr(b, "<!--\nfile: a frozen test copy\n" + R["brief-status"] + "-->\n\n# Operator brief\n\n" + R["brief-digest"] + "## §NEXT — a test\n" + "b" * brief_pad
          + "\n\n## §HELD-BY-THE-HUB\n" + R["brief-held"] + R["brief-words"] + "## §DONE — a test\n" + brief_tail)
    return s, b
def would_be(st, s, b): return rs._splice(rs.rd(s), rs.rd(b), rs.render_all(st))
def dump(st, p): pathlib.Path(p).write_text(yaml.safe_dump(st, allow_unicode=True, sort_keys=False, width=100000), encoding="utf-8", newline="\n"); return p
def cli(*args, enc="utf-8"):
    env = dict(os.environ); env["PYTHONIOENCODING"] = enc
    return subprocess.run([PY, "-B", RS] + [str(a) for a in args], capture_output=True, text=True, encoding="utf-8", errors="replace", env=env)
def quiet(*_): return None
def expect_refused(fn, needle):
    try: fn()
    except AssertionError as e: assert needle in str(e), f"refused for another reason: {e}"; return
    raise AssertionError(f"not refused (expected {needle!r})")
def refused_on_copies(st, needle, **frozen_kw):
    """write(st) on fresh frozen copies is REFUSED with needle in the reason, and neither copy nor any worktree file changes by a byte"""
    with tempfile.TemporaryDirectory() as tmp:
        s, b = frozen(tmp, **frozen_kw); m, m0 = (md5(s), md5(b)), live_md5s(); expect_refused(lambda: rs.write(st, s, b, out=quiet), needle)
        assert (md5(s), md5(b)) == m and live_md5s() == m0, "a byte was written"
RESULTS = []
def check(name, fn):
    try: fn(); RESULTS.append((name, "")); print(f"ok   {name}")
    except Exception as e: RESULTS.append((name, f"{type(e).__name__}: {e}"[:400])); print(f"FAIL {name}: {RESULTS[-1][1]}")

def region_bytes(name):
    def t():
        got = rs.render_all(rs.load_state(F_STATE))[name].encode("utf-8"); want = rb(f_exp(name)); assert got == want, rs._first_diff(got, want)
    return t
def t_overcap_snapshot_digest_refused():
    st = rs.load_state(F_STATE); st["notes"].append("x" * (rs.DIGEST_CAP + 1)); refused_on_copies(st, "CAP snapshot-digest")
def t_overcap_brief_digest_refused():
    st = rs.load_state(F_STATE); st["brief"]["notes"].append("x" * (rs.DIGEST_CAP + 1)); refused_on_copies(st, "CAP brief-digest")
def t_overcap_snapshot_file_refused():
    st = rs.load_state(F_STATE); assert rs.nb(rs.render_all(st)["snapshot-digest"]) <= rs.DIGEST_CAP      # the digest fits, the FILE does not
    with tempfile.TemporaryDirectory() as tmp: s, b = frozen(tmp); pad = rs.SNAP_CAP - rs.nb(would_be(st, s, b)[0]) + 1
    refused_on_copies(st, f"CAP snapshot-file {rs.SNAP_CAP + 1} > {rs.SNAP_CAP}", snap_pad=pad)
def t_overcap_held_refused():
    st = rs.load_state(F_STATE); st["held"].append({"lane": "x" * (rs.HELD_CAP + 1), "state": "", "next": ""}); refused_on_copies(st, "CAP brief-held")
def t_yaml_roundtrip():
    text = F_STATE.read_text(encoding="utf-8"); d = yaml.safe_load(text); assert d == rs.load_state(F_STATE), "the renderer used another dict"
    assert yaml.safe_load(yaml.safe_dump(d, allow_unicode=True, sort_keys=False)) == d, "safe_dump/safe_load does not round-trip"
    assert "\r" not in text and all(isinstance(v, str) for v in rs.slots(d).values())
def t_duplicate_key_refused():
    text = F_STATE.read_text(encoding="utf-8"); old = '    next: "passive"\n'; assert text.count(old) == 1
    with tempfile.TemporaryDirectory() as tmp:
        p = pathlib.Path(tmp) / "state.yaml"; rs.wr(p, text.replace(old, old + '    next: "a paste slip"\n'))
        assert yaml.safe_load(rs.rd(p))["held"][6]["next"] == "a paste slip", "plain safe_load keeps the last one silently (the class)"
        expect_refused(lambda: rs.load_state(p), "the key 'next' written twice in one mapping")
        rs.wr(p, text + 'extra:\n  <<:\n    a: "1"\n'); expect_refused(lambda: rs.load_state(p), "only plain keys (no `<<` merge")
def t_unfilled_slot_refused():
    with tempfile.TemporaryDirectory() as tmp:
        t = pathlib.Path(tmp)
        for _, tpl, _, _ in rs.REGIONS.values(): shutil.copyfile(rs.TPL / tpl, t / tpl)
        rs.wr(t / rs.REGIONS["snapshot-digest"][1], rs.rd(rs.TPL / rs.REGIONS["snapshot-digest"][1]) + "@@no_such_field@@\n")
        expect_refused(lambda: rs.render_all(rs.load_state(F_STATE), tpl_dir=t), "unfilled slot")
def t_missing_key_unfilled():
    st = rs.load_state(F_STATE); del st["closed_windows"]; expect_refused(lambda: rs.render_all(st), "unfilled slot")
def t_held_pipe_refused():
    st = rs.load_state(F_STATE); st["held"][3]["state"] = "FREE | until Monday"; expect_refused(lambda: rs.render_all(st), "held[3].state: a table cell may not carry the pipe")
def t_unread_key_refused():
    st = rs.load_state(F_STATE); st["stray"] = "x"; st["shas"]["extra"] = "y"; expect_refused(lambda: rs.render_all(st), "unread keys (no template reads them): shas.extra stray")
    st = rs.load_state(F_STATE); st["held"][0]["note"] = "z"; expect_refused(lambda: rs.render_all(st), "unread keys (no template reads them): held[0].note")
    st = rs.load_state(F_STATE); st["shas"]["extra"] = {}; expect_refused(lambda: rs.render_all(st), "shas.extra: an empty mapping")
def t_list_shapes_refused():
    for key, edit in (("held", lambda st: st.update(held="| a | b | c | d |")), ("words.open", lambda st: st["words"].update(open=[])),
                      ("next_acts", lambda st: st.update(next_acts="the b1 card"))):
        st = rs.load_state(F_STATE); edit(st); expect_refused(lambda: rs.render_all(st), key + ": a list with at least one " + ("row" if key == "held" else "item"))
def t_anchor_twice_refused():
    refused_on_copies(rs.load_state(F_STATE), "anchor count 2: '**Open words ('", brief_tail="\n**Open words (a second one)\n")
def t_region_found_twice_refused():
    st = rs.load_state(F_STATE); refused_on_copies(st, "region brief-status found 2 times in the would-be brief", brief_tail="was " + rs.render_all(st)["brief-status"])
def t_every_scalar_verbatim():
    both = "".join(rb(f_exp(n)).decode("utf-8") for n in NAMES); n = 0
    def walk(v):
        nonlocal n
        if isinstance(v, dict): [walk(x) for x in v.values()]
        elif isinstance(v, list): [walk(x) for x in v]
        else: n += 1; assert isinstance(v, str) and v in both, f"not a verbatim substring of the regions: {v[:60]!r}"
    walk(rs.load_state(F_STATE)); assert n >= 40, n
def t_write_fixture_state_on_copies():
    with tempfile.TemporaryDirectory() as tmp:
        s, b = frozen(tmp); m, m0 = (md5(s), md5(b)), live_md5s(); caps = rs.write(rs.load_state(F_STATE), s, b, out=quiet); got = rs.regions(rs.rd(s), rs.rd(b))
        for name in NAMES: assert got[name].encode("utf-8") == rb(f_exp(name)), name
        assert (md5(s), md5(b)) == m, "the fixture state did not re-render its own regions byte for byte"
        assert all(v <= cap for v, cap in caps.values()) and set(caps) == {"snapshot-digest", "snapshot-file", "brief-digest", "brief-held", "brief-file"}, caps
        assert live_md5s() == m0, "the worktree's files changed"
def t_write_cli_on_copies():
    with tempfile.TemporaryDirectory() as tmp:
        s, b = copies(tmp); m0 = live_md5s(); r = cli("--write", "--snapshot", s, "--brief", b)
        assert r.returncode == 0 and r.stdout.count("WROTE ") == 2, (r.returncode, r.stdout, r.stderr)
        want = rs.render_all(rs.load_state(rs.P_STATE)); got = rs.regions(rs.rd(s), rs.rd(b))
        assert all(got[n] == want[n] for n in NAMES) and live_md5s() == m0, "the regions differ or the worktree's files changed"
def t_overcap_cli_refused():
    with tempfile.TemporaryDirectory() as tmp:
        s, b = frozen(tmp); st = rs.load_state(F_STATE); st["words"]["given"].append(""); k = rs.BRIEF_CAP - rs.nb(would_be(st, s, b)[1]) + 1
        st["words"]["given"][-1] = "x" * k; assert k > 0 and rs.nb(would_be(st, s, b)[1]) == rs.BRIEF_CAP + 1, k
        p = dump(st, pathlib.Path(tmp) / "state.yaml"); m, m0 = (md5(s), md5(b)), live_md5s(); r = cli("--write", "--state", p, "--snapshot", s, "--brief", b)
        assert r.returncode == 1 and f"REFUSED CAP brief-file {rs.BRIEF_CAP + 1} > {rs.BRIEF_CAP} — nothing written" in r.stdout, (r.returncode, r.stdout, r.stderr)
        assert (md5(s), md5(b)) == m and live_md5s() == m0 and "WROTE" not in r.stdout, "a byte was written"
def t_probe_live_writes_nothing():
    m0 = live_md5s(); r = cli("--probe")
    assert r.returncode == 0 and r.stdout.count("PROBE ") == 8 and r.stdout.rstrip().endswith("PROBE OK — nothing written"), (r.returncode, r.stdout, r.stderr)
    assert live_md5s() == m0, "--probe changed a file"
def t_probe_frozen_writes_nothing():
    m0 = live_md5s()
    with tempfile.TemporaryDirectory() as tmp:
        s, b = frozen(tmp); st = rs.load_state(F_STATE); st["status"] += " A probe test."; p = dump(st, pathlib.Path(tmp) / "state.yaml"); m = (md5(s), md5(b))
        assert would_be(st, s, b)[1] != rs.rd(b), "the probed state must render DIFFERENT bytes, or a writing probe would go unseen"
        r = cli("--probe", "--state", p, "--snapshot", s, "--brief", b)
        assert r.returncode == 0 and "PROBE OK — nothing written" in r.stdout and (md5(s), md5(b)) == m, (r.returncode, r.stdout, r.stderr)
        st["held"][0]["next"] += "x" * rs.HELD_CAP; dump(st, p); r = cli("--probe", "--state", p, "--snapshot", s, "--brief", b)
        assert r.returncode == 1 and "REFUSED CAP brief-held" in r.stdout and (md5(s), md5(b)) == m and live_md5s() == m0, (r.returncode, r.stdout, r.stderr)
def t_v1_interface():
    """render()/splice() — what splice_lib_v3/v4's render_regions() (the hub's beat()) calls — on frozen copies, and render_regions itself"""
    st = rs.load_state(F_STATE); snap, brief, extra = rs.render(st)
    assert (snap.encode("utf-8"), brief.encode("utf-8"), extra) == (rb(f_exp("snapshot-digest")), rb(f_exp("brief-digest")), []), "render(): the two digests, then []"
    spec4 = importlib.util.spec_from_file_location("splice_lib_v4", HERE / "splice_lib_v4.py"); v4 = importlib.util.module_from_spec(spec4); spec4.loader.exec_module(v4)
    with tempfile.TemporaryDirectory() as tmp:
        s, b = frozen(tmp); ts, tb = rs.rd(s), rs.rd(b); new_s, new_b, caps = rs.splice(ts, tb, snap, brief)
        assert (new_s, new_b) == (ts, tb) and set(caps) == {"snapshot-digest", "snapshot-file", "brief-digest", "brief-file"}, caps
        assert v4.render_regions(F_STATE, ts, tb) == (ts, tb, caps), "splice_lib_v4.render_regions() differs from render() + splice()"
        expect_refused(lambda: rs.splice(ts, tb, snap.rstrip("\n") + "x" * rs.DIGEST_CAP + "\n", brief), "CAP snapshot-digest")
def t_check_diff_path():
    with tempfile.TemporaryDirectory() as tmp:
        s, b = frozen(tmp); r = cli("--check", "--state", F_STATE, "--snapshot", s, "--brief", b)
        assert r.returncode == 0 and r.stdout.count("MATCH ") == 7, (r.returncode, r.stdout, r.stderr)
        st = rs.load_state(F_STATE); st["held"][9]["next"] += ", a test"; p = dump(st, pathlib.Path(tmp) / "state.yaml")
        r = cli("--check", "--state", p, "--snapshot", s, "--brief", b); diffs = [l.split()[1] for l in r.stdout.splitlines() if l.startswith("DIFF ")]
        assert r.returncode == 1 and diffs == ["brief-held", "brief-file"] and r.stdout.count("MATCH ") == 5 and "at byte " in r.stdout, (r.returncode, r.stdout, r.stderr)
def t_selftest_diff_path():
    with tempfile.TemporaryDirectory() as tmp:
        t = pathlib.Path(tmp); lines = []
        for p in FIX.glob("v104b1_*"): shutil.copyfile(p, t / p.name)
        e = t / f_exp("brief-words").name; e.write_bytes(e.read_bytes().replace(b"`TAILSCALE:`", b"`TAILSCALE?`")); old, rs.FIX = rs.FIX, t
        try: rc = rs.selftest(out=lines.append)
        finally: rs.FIX = old
        assert rc == 1 and lines[-1] == "render_state selftest: 5 check(s), 1 failure(s)" and any(l.startswith("DIFF brief-words") and "at byte " in l for l in lines), lines
def t_selftest_cli():
    r = cli("--selftest"); assert r.returncode == 0 and r.stdout.rstrip().endswith("render_state selftest: 5 check(s), 0 failure(s)"), (r.returncode, r.stdout, r.stderr)
def t_selftest_cp1252():
    r = cli("--selftest", enc="cp1252")
    assert r.returncode == 0 and "MATCH snapshot-digest 1776 ≤ 2048" in r.stdout and r.stdout.rstrip().endswith("render_state selftest: 5 check(s), 0 failure(s)"), (r.returncode, r.stdout[-300:], r.stderr[-300:])
def t_check_cli_live():
    r = cli("--check"); assert r.returncode == 0 and r.stdout.count("MATCH ") == 7 and "DIFF" not in r.stdout, (r.returncode, r.stdout, r.stderr)
def t_caps_imported_and_named_once():
    src = rs.rd(HERE / "render_state.py"); lib = rs.lib
    assert rs.SNAP_CAP == lib.SNAP_CAP and rs.BRIEF_CAP == lib.BRIEF_CAP and "3500" not in src and "12288" not in src, "a file cap retyped"
    assert src.count("6144") == 1 and rs.HELD_CAP == 6144 and src.count("2048") == 1, "HELD_CAP and DIGEST_CAP each named once"
def t_no_pycache():
    assert not list(ROOT.glob("context/**/__pycache__")), "a __pycache__ in the tree"

for name, fn in (("fixture snapshot-digest byte-equal", region_bytes("snapshot-digest")), ("fixture brief-digest byte-equal", region_bytes("brief-digest")),
                 ("NEW fixture brief-status byte-equal", region_bytes("brief-status")), ("NEW fixture brief-held byte-equal", region_bytes("brief-held")),
                 ("NEW fixture brief-words byte-equal", region_bytes("brief-words")),
                 ("over-cap snapshot-digest refused, nothing written", t_overcap_snapshot_digest_refused), ("over-cap brief-digest refused, nothing written", t_overcap_brief_digest_refused),
                 ("over-cap snapshot-file refused, nothing written", t_overcap_snapshot_file_refused), ("NEW over-cap brief-held refused, nothing written", t_overcap_held_refused),
                 ("NEW --write CLI on an over-cap state: REFUSED, the region and its bytes, exit 1, nothing written", t_overcap_cli_refused),
                 ("NEW --probe on the live files writes nothing (md5s before = after)", t_probe_live_writes_nothing),
                 ("NEW --probe on frozen copies: a state with other bytes writes nothing; an over-cap state refused", t_probe_frozen_writes_nothing),
                 ("NEW render()/splice(), the v1 interface splice_lib_v3/v4's beat() calls, and v4's render_regions()", t_v1_interface),
                 ("yaml.safe_load round-trips the dict the renderer used", t_yaml_roundtrip), ("NEW a key written twice in one mapping refused", t_duplicate_key_refused),
                 ("unfilled slot refused by fill()", t_unfilled_slot_refused), ("NEW a state key missing -> its slot unfilled, refused", t_missing_key_unfilled),
                 ("NEW a held cell carrying ' | ' refused", t_held_pipe_refused), ("NEW an unread state key refused by name (top level, nested, a held cell)", t_unread_key_refused),
                 ("NEW a list key as a scalar or empty refused", t_list_shapes_refused),
                 ("NEW an anchor twice in the brief refused, nothing written", t_anchor_twice_refused),
                 ("NEW a rendered region found twice in the would-be file refused, nothing written", t_region_found_twice_refused),
                 ("every fixture scalar a quoted verbatim substring", t_every_scalar_verbatim),
                 ("write(fixture state) on frozen copies == fixture bytes; worktree md5s unchanged", t_write_fixture_state_on_copies),
                 ("--write CLI on temp copies of the live files; worktree md5s unchanged", t_write_cli_on_copies),
                 ("NEW --check DIFF path: one changed cell -> DIFF brief-held + brief-file, exit 1", t_check_diff_path),
                 ("NEW --selftest DIFF path: one corrupted expected region -> 1 failure, exit 1", t_selftest_diff_path),
                 ("--selftest exits 0 with its closing line", t_selftest_cli), ("NEW --selftest under PYTHONIOENCODING=cp1252 exits 0 and prints the ≤ in UTF-8", t_selftest_cp1252),
                 ("--check against the worktree's files: 7 MATCH", t_check_cli_live),
                 ("NEW the file caps imported, HELD_CAP and DIGEST_CAP named once", t_caps_imported_and_named_once), ("no __pycache__ in the tree", t_no_pycache)):
    check(name, fn)
fails = sum(1 for _, e in RESULTS if e); print(f"render_state tests: {len(RESULTS)} check(s), {fails} failure(s)"); sys.exit(1 if fails else 0)

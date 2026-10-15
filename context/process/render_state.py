# context/process/render_state.py — THE RENDERER (BEAT-RENDERER-1 U1c, minted 2026-10-09 at 513d1c0; v2 BEAT-RENDERER-2 U1, 2026-10-10 at 8ab4789).
# Purpose: the volatile regions of the snapshot and the brief are GENERATED, never hand-cut — the facts live in context/status/state.yaml
# (the hub edits it), the prose skeletons in context/process/templates/*.tpl.md (the library's `fill()` slots, `@@key@@`), and this
# file fills them, runs every anchor, cap and region assert BEFORE any byte, and writes the regions by their anchors. FIVE regions (REGIONS):
#   snapshot-digest  PROJECT_SNAPSHOT.md `## The digest` → end of file · brief-status the brief's frontmatter line `status: …` ·
#   brief-digest `## §DIGEST` → `## §NEXT` · brief-held `| Lane | State (` → `**Open words (` (the lanes table + the closed windows) ·
#   brief-words `**Open words (` → `## §DONE` (the open and the given words)
#   --selftest  renders fixtures/v104b1_state.yaml and compares BYTES with the fixture's five expected regions
#   --check     renders the state and compares with the files' regions: MATCH|DIFF <region> <bytes> [≤ <cap>] per region and per file
#               (exit 1 on a DIFF or a cap breach; a DIFF names the first differing byte offset)
#   --probe     every assert --write runs — each anchor exactly once, every cap, each rendered region found exactly once in the would-be
#               file and re-read byte-equal by its anchors — then the would-be bytes per region and per file; writes NOTHING
#   --write     the probe, then both files written by anchor, then read back equal (the hub's beat runs it; a lane runs it ONLY on temp
#               copies — --state, --snapshot and --brief PATH exist for that and for the tests)
# A refusal prints `REFUSED <why> — nothing written` and exits 1. The file caps are IMPORTED from splice_lib_v2 (SNAP_CAP, BRIEF_CAP);
# DIGEST_CAP (W-HIVE-1 P9) and HELD_CAP (IR-140) are the two numbers named here, once each. REFUSED by name too: a state key that no
# template reads, a key written twice in one mapping, a merge or complex key, an empty mapping, a list key given as a scalar or as an
# empty list. stdout and stderr are UTF-8 at entry (`_utf8_stdout`; IR-146). Standard library + PyYAML (`safe_load`'s SafeLoader,
# subclassed only to refuse those keys); Python ≥ 3.10.
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
DIGEST_CAP = 2048                                         # W-HIVE-1 P9: each digest ≤ 2 KB; the brief's §DIGEST heading carries the same ceiling
HELD_CAP = 6144                                           # IR-140: the brief's §HELD region (the lanes table + the closed windows) ≤ 6 KB
A_SNAP, A_BRIEF, A_NEXT = "## The digest", "## §DIGEST", "## §NEXT"
# THE REGIONS, in file order: name → (file, template, start anchor, end anchor). Every anchor is counted EXACTLY ONCE in its file before any
# read; a region runs from its start anchor to the start of its end anchor (None = the end of the file); an anchor that begins with "\n"
# is a line-start anchor, and the region begins (or ends) just after that newline.
REGIONS = {
    "snapshot-digest": ("snapshot", "snapshot_digest.tpl.md", A_SNAP, None),
    "brief-status": ("brief", "brief_status.tpl.md", "\nstatus: ", "\n-->"),
    "brief-digest": ("brief", "brief_digest.tpl.md", A_BRIEF, A_NEXT),
    "brief-held": ("brief", "brief_held.tpl.md", "| Lane | State (", "**Open words ("),
    "brief-words": ("brief", "brief_words.tpl.md", "**Open words (", "## §DONE"),
}
CAPS = {"snapshot-digest": DIGEST_CAP, "brief-digest": DIGEST_CAP, "brief-held": HELD_CAP}   # the region caps; the files' are SNAP_CAP, BRIEF_CAP
ROWS = ("snapshot-digest", "snapshot-file", "brief-status", "brief-digest", "brief-held", "brief-words", "brief-file")   # --check/--probe lines
FIXTURE = "v104b1"                                        # fixtures/<FIXTURE>_state.yaml + one <FIXTURE>_<region>.expected.md per region
# THE ONE LIST MECHANISM: a list renders by sep.join(items) into the slot of its key; the separator per key lives here. `held` is the one
# list of rows: {lane, state, next} → `| lane | state | next |`, the rows joined by newlines into the slot `held`.
SEPS = {"pi.notes": "; ", "notes": " ", "open_irs": " · ", "next_acts": " → ", "brief.notes": " ", "brief.week": " · ", "brief.yours": " · ",
        "words.open": " · ", "words.given": " · "}
HELD_KEYS = ("lane", "state", "next")

def _lib():
    spec = importlib.util.spec_from_file_location("splice_lib_v2", LIBP); lib = importlib.util.module_from_spec(spec); spec.loader.exec_module(lib)
    assert lib.lib_md5() == LIB_V2_MD5, lib.lib_md5(); return lib
lib = _lib(); SNAP_CAP, BRIEF_CAP = lib.SNAP_CAP, 14336   # D-v111-39 (v111 b5, 2026-10-15): the brief's cap 12 KB → 14 KB by a named edit (D-v110-7's rule) — splice_lib_v5 carries the same number; the v67 prompt §1.2(d)/§1b.3 re-cut to match
nb, rd, wr = lib.nbytes, lib.rd, lib.wr

def _utf8_stdout():
    """IR-146 (the v101 b6 crash on `≤` under cp1252): stdout and stderr re-configured to UTF-8 with LF line ends, at entry."""
    for s in (sys.stdout, sys.stderr):
        try: s.reconfigure(encoding="utf-8", errors="replace", newline="\n")
        except (AttributeError, ValueError): pass

class _Loader(yaml.SafeLoader):
    """yaml.safe_load's loader for the form's plain keys, except that a key written twice in one mapping is REFUSED (PyYAML keeps the last
    one without a word), and so is any key the form does not use (a merge `<<`, a `=` value key, a complex key) — safe_load would take them."""
    def construct_mapping(self, node, deep=False):
        seen = set()
        for k, _ in node.value:
            assert isinstance(k, yaml.ScalarNode) and k.tag not in ("tag:yaml.org,2002:merge", "tag:yaml.org,2002:value"), \
                f"state: only plain keys (no `<<` merge, no `=`, no complex key) (line {k.start_mark.line + 1})"
            key = self.construct_object(k, deep=deep)
            assert key not in seen, f"state: the key {key!r} written twice in one mapping (line {k.start_mark.line + 1})"; seen.add(key)
        return super().construct_mapping(node, deep)

def load_state(path=P_STATE):
    d = yaml.load(pathlib.Path(path).read_text(encoding="utf-8"), Loader=_Loader); assert isinstance(d, dict) and d, f"state: not a mapping: {path}"; return d

def _value(key, v):
    assert isinstance(v, str), f"{key}: every value is a quoted string (got {type(v).__name__}: {v!r})"
    assert "@@" not in v, f"{key}: a value never carries a slot"
    assert "\n" not in v and "\r" not in v, f"{key}: a value is one line"
    return v

def slots(state):
    """The state flattened into fill() slots: a scalar by its dotted key; a list by ONE join (SEPS); `held` rows as table lines."""
    out = {}
    def walk(key, v):
        if key == "held" or key in SEPS:
            assert isinstance(v, list) and v, f"{key}: a list with at least one " + ("row" if key == "held" else "item (\"nothing\" is written as one item, e.g. \"none\")")
        if isinstance(v, dict):
            assert v or not key, f"{key}: an empty mapping (a key with nothing under it is removed)"
            for k, x in v.items(): walk(f"{key}.{k}" if key else str(k), x)
        elif isinstance(v, list) and key == "held":
            rows = []
            for i, r in enumerate(v):
                assert isinstance(r, dict), f"held[{i}]: a row is a mapping of lane, state, next"
                extra, missing = sorted(str(k) for k in r if k not in HELD_KEYS), [k for k in HELD_KEYS if k not in r]
                assert not extra, "unread keys (no template reads them): " + " ".join(f"held[{i}].{k}" for k in extra)
                assert not missing, f"held[{i}]: no " + " · ".join(missing)
                for k in HELD_KEYS: assert "|" not in _value(f"held[{i}].{k}", r[k]), f"held[{i}].{k}: a table cell may not carry the pipe"
                rows.append("| " + " | ".join(r[k] for k in HELD_KEYS) + " |")
            out[key] = "\n".join(rows)
        elif isinstance(v, list):
            assert key in SEPS, f"list {key!r}: no separator in SEPS"
            out[key] = SEPS[key].join(_value(f"{key}[{i}]", x) for i, x in enumerate(v))
        else:
            out[key] = _value(key, v)
    walk("", state); return out

def render_all(state, tpl_dir=TPL):
    """Every region rendered by the library's fill() (an unfilled slot is REFUSED there); a key no template reads REFUSED by name; the
    trailer grep on every region. Returns {region: text}."""
    s = slots(state); tpls = {name: rd(pathlib.Path(tpl_dir) / tpl) for name, (_, tpl, _, _) in REGIONS.items()}
    unread = sorted(k for k in s if not any(("@@" + k + "@@") in t for t in tpls.values()))
    assert not unread, "unread keys (no template reads them): " + " ".join(unread)
    out = {name: lib.fill(t, s) for name, t in tpls.items()}; lib.no_trailers(*out.values())
    for name, r in out.items(): assert r.endswith("\n") and "\r" not in r, f"{name}: a region ends with a newline, LF only"
    return out

def render(state, tpl_dir=TPL):
    """v1's interface (splice_lib_v3's render_regions calls it): the two digests and an empty list where v1 listed the unused keys."""
    r = render_all(state, tpl_dir); return r["snapshot-digest"], r["brief-digest"], []

def _once(text, anchor, where):
    n = text.count(anchor); assert n == 1, f"anchor count {n}: {anchor!r} in the {where}"

def spans(snap_text, brief_text):
    """{region: (file, start, end)} — every anchor counted exactly once first; the brief's regions in file order and disjoint."""
    texts = {"snapshot": snap_text, "brief": brief_text}; out = {}
    for name, (f, _, a, b) in REGIONS.items():
        for x in (a, b):
            if x is not None: _once(texts[f], x, f)
        s = texts[f].index(a) + (1 if a.startswith("\n") else 0)
        e = len(texts[f]) if b is None else texts[f].index(b) + (1 if b.startswith("\n") else 0)
        assert s < e, f"{name}: its start anchor after its end anchor"; out[name] = (f, s, e)
    br = [(s, e) for f, s, e in out.values() if f == "brief"]
    assert all(br[i][1] <= br[i + 1][0] for i in range(len(br) - 1)), "the brief's regions in file order, disjoint"
    return out

def regions(snap_text, brief_text):
    """The files' regions by their anchors: {region: text}."""
    t = {"snapshot": snap_text, "brief": brief_text}; return {n: t[f][s:e] for n, (f, s, e) in spans(snap_text, brief_text).items()}

def _splice(snap_text, brief_text, rendered):
    """The whole files with the given regions replaced — each file's from its last region to its first, so every offset holds."""
    sp = spans(snap_text, brief_text); t = {"snapshot": snap_text, "brief": brief_text}
    for name in sorted(rendered, key=lambda n: -sp[n][1]):
        f, s, e = sp[name]; t[f] = t[f][:s] + rendered[name] + t[f][e:]
    return t["snapshot"], t["brief"]

def _caps(rendered, new_s, new_b):
    """Every cap — the regions first (a breach names its region), then the files: {name: (bytes, cap)}; a breach REFUSED."""
    caps = {n: (nb(rendered[n]), CAPS[n]) for n in REGIONS if n in CAPS and n in rendered}
    caps["snapshot-file"], caps["brief-file"] = (nb(new_s), SNAP_CAP), (nb(new_b), BRIEF_CAP)
    for name, (v, cap) in caps.items(): assert v <= cap, f"CAP {name} {v} > {cap}"
    return caps

def _after(rendered, new_s, new_b):
    """The asserts v101 ran AFTER its writes (b4, b5), run BEFORE: each anchor once in the would-be files; each rendered region found exactly
    once there and re-read byte-equal by its anchors; LF only; the trailer grep."""
    got, t = regions(new_s, new_b), {"snapshot": new_s, "brief": new_b}
    for name, r in rendered.items():
        f = REGIONS[name][0]; n = t[f].count(r)
        assert n == 1, f"region {name} found {n} times in the would-be {f}"
        assert got[name] == r, f"region {name} does not re-read byte-equal by its anchors"
    for x in (new_s, new_b): assert x.endswith("\n") and "\r" not in x, "a file ends with a newline, LF only"
    lib.no_trailers(new_s, new_b)

def splice(snap_text, brief_text, snap_region, brief_region):
    """v1's interface (splice_lib_v3's beat() calls it): the two digests spliced into the given texts, every anchor, cap and region assert
    run before the caller writes a byte; returns (snapshot_text, brief_text, caps)."""
    r = {"snapshot-digest": snap_region, "brief-digest": brief_region}; new_s, new_b = _splice(snap_text, brief_text, r)
    caps = _caps(r, new_s, new_b); _after(r, new_s, new_b); return new_s, new_b, caps

def probe(state, snap_path=P_SNAP, brief_path=P_BRIEF, tpl_dir=TPL):
    """EVERYTHING --write asserts, on the would-be texts; nothing is written. Returns (new_snapshot, new_brief, rendered, caps)."""
    rendered = render_all(state, tpl_dir); s_t, b_t = rd(pathlib.Path(snap_path)), rd(pathlib.Path(brief_path))
    new_s, new_b = _splice(s_t, b_t, rendered); caps = _caps(rendered, new_s, new_b); _after(rendered, new_s, new_b)
    return new_s, new_b, rendered, caps

def _first_diff(a, b):
    n = next((i for i, (x, y) in enumerate(zip(a, b)) if x != y), min(len(a), len(b))); return f"at byte {n}: got {a[n:n+24]!r} want {b[n:n+24]!r}"

def _cap_of(name): return CAPS.get(name) or {"snapshot-file": SNAP_CAP, "brief-file": BRIEF_CAP}.get(name)

def _line(tag, name, size, cap):
    return f"{tag} {name} {size}" + ("" if cap is None else (" ≤ " if size <= cap else " > ") + str(cap))

def check(state_path=P_STATE, snap_path=P_SNAP, brief_path=P_BRIEF, out=print):
    """MATCH|DIFF <region> <bytes> [≤ <cap>] per region and per file against the given files; exit 1 on any DIFF or cap breach."""
    rendered = render_all(load_state(state_path)); s_t, b_t = rd(pathlib.Path(snap_path)), rd(pathlib.Path(brief_path))
    got, want = dict(rendered), regions(s_t, b_t); new_s, new_b = _splice(s_t, b_t, rendered)
    got["snapshot-file"], got["brief-file"], want["snapshot-file"], want["brief-file"] = new_s, new_b, s_t, b_t
    ok = True
    for name in ROWS:
        g, w, cap = got[name].encode("utf-8"), want[name].encode("utf-8"), _cap_of(name); same = g == w; fits = cap is None or len(g) <= cap
        ok = ok and same and fits; out(_line("MATCH" if same else "DIFF", name, len(g), cap) + ("" if same else " " + _first_diff(g, w)))
    return 0 if ok else 1

def write(state, snap_path, brief_path, out=print, tpl_dir=TPL):
    """The probe (every assert and cap on the would-be texts), THEN both files written by anchor, then read back equal; returns the caps."""
    new_s, new_b, _, caps = probe(state, snap_path, brief_path, tpl_dir)
    for p, t in ((snap_path, new_s), (brief_path, new_b)): wr(pathlib.Path(p), t)
    for p, t in ((snap_path, new_s), (brief_path, new_b)):
        if rd(pathlib.Path(p)) != t: raise RuntimeError(f"{p}: the read-back differs from the written text")
        out(f"WROTE {p} {nb(t)}")
    return caps

def selftest(out=print):
    """The fixture state through the templates == the fixture's expected regions, at the bytes (one check per region)."""
    rendered = render_all(load_state(FIX / (FIXTURE + "_state.yaml"))); fails = 0
    for name in REGIONS:
        g, w = rendered[name].encode("utf-8"), (FIX / (FIXTURE + "_" + name.replace("-", "_") + ".expected.md")).read_bytes(); same = g == w; fails += (not same)
        out(_line("MATCH" if same else "DIFF", name, len(g), CAPS.get(name)) + ("" if same else " " + _first_diff(g, w)))
    out(f"render_state selftest: {len(REGIONS)} check(s), {fails} failure(s)"); return 1 if fails else 0

def main(argv=None):
    _utf8_stdout()
    ap = argparse.ArgumentParser(description="render the snapshot's and the brief's volatile regions from context/status/state.yaml")
    g = ap.add_mutually_exclusive_group(required=True)
    for flag in ("--selftest", "--check", "--probe", "--write"): g.add_argument(flag, action="store_true")
    ap.add_argument("--state", default=str(P_STATE)); ap.add_argument("--snapshot", default=str(P_SNAP)); ap.add_argument("--brief", default=str(P_BRIEF))
    a = ap.parse_args(argv)
    try:
        if a.selftest: return selftest()
        if a.check: return check(pathlib.Path(a.state), pathlib.Path(a.snapshot), pathlib.Path(a.brief))
        st = load_state(pathlib.Path(a.state))
        if a.probe:
            new_s, new_b, rendered, _ = probe(st, a.snapshot, a.brief); sz = {n: nb(r) for n, r in rendered.items()}
            sz["snapshot-file"], sz["brief-file"] = nb(new_s), nb(new_b)
            for name in ROWS: print(_line("PROBE", name, sz[name], _cap_of(name)))
            print("PROBE OK — nothing written"); return 0
        write(st, a.snapshot, a.brief); return 0
    except AssertionError as e:
        print(f"REFUSED {e} — nothing written"); return 1

if __name__ == "__main__": sys.exit(main())

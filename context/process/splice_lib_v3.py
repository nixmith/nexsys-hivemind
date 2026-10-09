# context/process/splice_lib_v3.py — the hub's per-beat splice library, VERSION 3 (minted 2026-10-09 by BEAT-RENDERER-1 in the worktree at 513d1c0).
# v3 over v2: ONE operation, beat(ctx) — the chain re-cut, the block insert, the live-beat rotation (the oldest blocks VERBATIM into
# archive/pm-handoff-beats-<first>-<last>-rotated-<date>.md with the archive-map row), the snapshot chain, the two digest regions
# rendered from context/status/state.yaml (render_regions → render_state.py) and the census + card — EVERY assert and cap before
# the first byte, ONE write pass after, the post-write reads, the census computed from porcelain. The spine paths are PARAMETERS of
# beat() (ctx["paths"]), never module constants, so a test runs it on tempfile copies. v2's text follows VERBATIM (its own header
# included — it still speaks of itself as v2; not a byte of it is changed), then the v3 section: `diff splice_lib_v2.py
# splice_lib_v3.py` is pure addition. v2 stays every earlier beat script's pin (md5 99e87f2dbafaade35e071770b14b5557); a caller
# of v3 pins THIS file's md5 the same way: `assert lib.lib_md5() == "<v3 md5>"` (the return names it) before any use.
import sys; sys.dont_write_bytecode = True
# ---------------------------------------------------------------- v2 VERBATIM from the next line to the v3 marker ----
# context/process/splice_lib_v2.py — the hub's per-beat splice library, VERSION 2 (minted v92 beat 1, 2026-10-02; v1 adopted v73 beat 1, 2026-09-13).
# Purpose: the mechanics every beat script repeats — the paths, the clock, porcelain, the guarded anchors, the chain split and
# rotation, the region caps, the census COMPUTED from porcelain, the trailer check, the card form — so a beat script carries only
# its own anchors, texts and asserts. THE GUARDED-SPLICE LAW is unchanged: the beat script runs every assert and cap BEFORE its
# first byte; this file only supplies the instruments. Every beat script asserts this file's md5 (LIB_MD5) before use; a change
# here is a NEW version file (splice_lib_v3.py), never an edit in place. Stateless by design: no HEADs, no beat numbers, no texts.
# v2 over v1 (the v90 b6 defect — three register rows landed at 6a69bed as `\1 \2; …`): sub_once() is a LITERAL splice and now
# REFUSES a repl that carries a backreference; sub_once_x() is the expanding form (re.Match.expand); assert_rows() names, after
# a write, every row/heading/key a splice edited. Everything else is v1's text, byte for byte.
import os, re, subprocess, datetime, pathlib, hashlib

HOME = pathlib.Path(os.environ["HOME"]); CF = HOME / "mnt" / "ClaudeFolder"
HV = CF / "nexsys-hivemind"; DOCS = CF / "homesynapse-core-docs"; CORE = CF / "homesynapse-core"
BENCH = CF / "nexsys-bench"; SKILLS = CF / "nexsys-skills"
P_H = HV / "context/handoff/pm-handoff.md"
P_CH = HV / "context/handoff/archive/chains-rotated-2026-08-27.md"
P_S = HV / "context/status/PROJECT_SNAPSHOT.md"
P_B = HV / "context/handoff/OPERATOR-BRIEF_for-Nick.md"
CHAIN_CAP, BEAT_CAP, SNAP_CAP, BRIEF_CAP, LIVE_BEATS_CAP = 3000, 2500, 3500, 12288, 12
REPOS = {"core": CORE, "hivemind": HV, "skills": SKILLS, "bench": BENCH, "docs": DOCS}
GIT_DIR = {"core": "homesynapse-core", "hivemind": "nexsys-hivemind", "skills": "nexsys-skills", "bench": "nexsys-bench", "docs": "homesynapse-core-docs"}

def scratch(v):
    p = CF / "_scratch" / v; p.mkdir(parents=True, exist_ok=True); return p

def lib_md5():
    return hashlib.md5(pathlib.Path(__file__).read_bytes()).hexdigest()

def clock(expect_ct_date):
    """THE CLOCK LAW: one instrument reading; CT = UTC-5; the beat asserts the CT date it believes."""
    now = datetime.datetime.now(datetime.timezone.utc)
    stamp = now.strftime("%Y-%m-%dT%H:%M:%SZ"); ct = now - datetime.timedelta(hours=5)
    assert ct.strftime("%Y-%m-%d") == expect_ct_date, (ct, expect_ct_date)
    ct_str = f"{ct.strftime('%a')} {ct.strftime('%Y-%m-%d')} ~{ct.strftime('%H:%M')[:-1]}x CT"
    return now, stamp, ct, ct_str

def rd(p): return p.read_text(encoding="utf-8")
def wr(p, s): p.write_text(s, encoding="utf-8", newline="\n")
def nbytes(s): return len(s.encode("utf-8"))
def run(args, cwd): return subprocess.run(args, cwd=cwd, capture_output=True, text=True)
def porcelain(repo): return run(["git", "--no-optional-locks", "status", "--porcelain"], repo).stdout
def head(repo): return run(["git", "--no-optional-locks", "log", "-1", "--format=%h"], repo).stdout.strip()
def ahead(repo): return run(["git", "--no-optional-locks", "rev-list", "--count", "origin/main..HEAD"], repo).stdout.strip()
def cached(repo): return run(["git", "--no-optional-locks", "diff", "--cached", "--name-status"], repo).stdout

def once(text, old, new):
    assert text.count(old) == 1, f"anchor count {text.count(old)}: {old[:90]!r}"
    return text.replace(old, new)

_BACKREF = re.compile(r"\\[0-9]|\\g<")

def sub_once(text, pattern, repl, flags=re.M):
    """A LITERAL splice: the one match is replaced by repl's own bytes. A backreference here is a defect (v90 b6) — refused."""
    assert not _BACKREF.search(repl), f"backreference in a literal repl — use sub_once_x: {repl[:60]!r}"
    ms = list(re.finditer(pattern, text, flags)); assert len(ms) == 1, f"pattern count {len(ms)}: {pattern[:90]!r}"
    m = ms[0]; return text[:m.start()] + repl + text[m.end():]

def sub_once_x(text, pattern, repl, flags=re.M):
    """The EXPANDING splice: repl's \\1 … \\9 and \\g<name> are the match's groups (re.Match.expand); every other byte is literal."""
    ms = list(re.finditer(pattern, text, flags)); assert len(ms) == 1, f"pattern count {len(ms)}: {pattern[:90]!r}"
    m = ms[0]; out = m.expand(repl); assert not _BACKREF.search(out), "a backreference survived expansion"
    return text[:m.start()] + out + text[m.end():]

def assert_rows(text, *needles):
    """After a write: every row, heading or key the splice edited is named here and found EXACTLY once (the v90 b6 lesson)."""
    for n in needles: assert text.count(n) == 1, f"edited row count {text.count(n)}: {n[:90]!r}"

def fill(t, d):
    for k, v in d.items(): t = t.replace("@@" + k + "@@", str(v))
    assert "@@" not in t, "unfilled slot"; return t

def no_trailers(*texts):
    for t in texts: assert "Co-Authored" not in t and "Claude-Session" not in t, "trailer text present"

def assert_clean(repo, sha):
    assert head(repo) == sha, (head(repo), sha); assert porcelain(repo) == "", porcelain(repo)
    assert not (repo / ".git/index.lock").exists()

def chain_split(line8, beat_prefix):
    """line 8 = `last-verified: <seg0>) Prior: <seg1>) Prior: <pointer>`; returns (seg0, seg1, pointer)."""
    assert line8.startswith("last-verified: " + beat_prefix), line8[:80]
    parts = line8.split(") Prior: "); assert len(parts) == 3, len(parts)
    return parts[0][len("last-verified: "):], parts[1], parts[2]

def rotate_chain(archive_text, seg_to_rotate, rotation_heading, expect_count):
    """Appends the rotated segment VERBATIM under one COUNTED heading; asserts the count before."""
    assert archive_text.endswith("\n") and len(re.findall(r"^## ", archive_text, re.M)) == expect_count
    add = f"\n## {rotation_heading}\n\n{seg_to_rotate})\n"
    return archive_text + add, add

def beat_index(lines):
    """The insertion index for a new beat block: the first `## 20` line; asserts the live-beat cap AFTER insertion."""
    i = next(i for i, l in enumerate(lines) if l.startswith("## 20"))
    live = sum(1 for l in lines[:lines.index("## Open Risks")] if l.startswith("## 20"))
    assert live + 1 <= LIVE_BEATS_CAP, f"live beats {live}+1 > cap; rotate first"
    return i, live

def census(repo, exp_M, exp_A, exp_D=frozenset()):
    """THE CENSUS FROM PORCELAIN — computed, never typed; the expected sets are the beat's claim about a diff that exists."""
    rows = [l for l in porcelain(repo).splitlines() if l.strip()]
    M = sorted(l[3:] for l in rows if l[:2] in (" M", "MM", "M ")); A = sorted(l[3:] for l in rows if l[:2] == "??")
    D = sorted(l[3:] for l in rows if l[:2] in (" D", "D "))
    assert set(M) == set(exp_M) and set(A) == set(exp_A) and set(D) == set(exp_D), \
        (sorted(set(M) ^ set(exp_M)), sorted(set(A) ^ set(exp_A)), sorted(set(D) ^ set(exp_D)))
    assert cached(repo) == "", "index not empty — the hub never stages"
    return len(M) + len(A) + len(D), len(M), len(A), len(D)

def card(repo_key, paths, n, msg_rel, say_back, expect_porcelain_note=""):
    """The one-command card in the form of record: porcelain + locks, explicit-path add, the staged count, the trailer grep, commit -F, push."""
    d = GIT_DIR[repo_key]; ps = " ".join(paths)
    cmd = (f"cd ~/Desktop/Code/ClaudeFolder/{d} && git --no-optional-locks status --porcelain | wc -l && ls .git/*.lock 2>/dev/null; "
           f"git add -- {ps} && echo \"staged: $(git diff --cached --name-status | wc -l) (expect {n})\" && "
           f"grep -c 'Co-Authored\\|Claude-Session' ../_scratch/{msg_rel}; git commit -F ../_scratch/{msg_rel} && git push && git log -1 --oneline")
    note = f" {expect_porcelain_note}" if expect_porcelain_note else ""
    return (f"In Git Bash, in `~/Desktop/Code/ClaudeFolder/{d}`:\n```\n{cmd}\n```\n"
            f"Read: `{n}`{note} · `staged: {n}` · `0` · the new sha. Say back `{say_back}`.\n")
# ======================================================================================================= v3: beat() ====
import importlib.util as _ilu
_HERE = pathlib.Path(__file__).resolve().parent
_BEAT_RE = re.compile(r"^## (\d{4}-\d{2}-\d{2}) \(v(\d+) beat (\d+)")
_OR, _MAP = "## Open Risks", "## The archive map"

def _render_state():
    spec = _ilu.spec_from_file_location("render_state", _HERE / "render_state.py"); m = _ilu.module_from_spec(spec); spec.loader.exec_module(m); return m

def render_regions(state_path, snap_text, brief_text):
    """The two digest regions rendered from state.yaml by render_state.py and spliced into the given texts (every region and file cap
    asserted there, before any byte); returns (snapshot_text, brief_text, caps). One beat script = the state edit → beat()."""
    rs = _render_state(); snap_r, brief_r, _ = rs.render(rs.load_state(state_path)); return rs.splice(snap_text, brief_text, snap_r, brief_r)

def _beat_id(line):
    m = _BEAT_RE.match(line); assert m, f"not a beat heading: {line[:60]!r}"; return m.group(1), f"v{m.group(2)} b{m.group(3)}", f"v{m.group(2)}b{m.group(3)}"

def live_blocks(lines):
    end = lines.index(_OR); return [i for i, l in enumerate(lines[:end]) if l.startswith("## 20")], end

def rotate_beats(h_text, n, date, beat_label, ct, stamp, map_anchor=None):
    """THE LIVE-BEAT ROTATION: the oldest n blocks out VERBATIM (newest first in the archive, as the live file keeps them);
    bytes(kept) + bytes(archived body) + 1 == bytes(before) asserted; the archive-map row inserted before the line that starts
    with map_anchor (exactly one) or, with no anchor, as the map's last row. Returns (kept_text, archive_name, archive_text, row, bytes)."""
    hl = h_text.split("\n"); heads, end = live_blocks(hl); assert len(heads) >= n > 0, (len(heads), n)
    start = heads[-n]; body_lines = hl[start:end]; assert body_lines[-1] == "", "a block ends with one blank line"
    body = "\n".join(body_lines); kept = hl[:start] + hl[end:]
    nb = (nbytes("\n".join(kept)), nbytes(body), nbytes(h_text)); assert nb[0] + nb[1] + 1 == nb[2], f"rotation bytes {nb}"
    ids = [_beat_id(hl[i]) for i in heads[-n:]]; (_, last_lbl, last_tok), (_, first_lbl, first_tok) = ids[0], ids[-1]
    dates = " → ".join(dict.fromkeys(d for d, _, _ in ids)); short = beat_label.replace(" beat ", " b")
    name = f"pm-handoff-beats-{first_tok}-{last_tok}-rotated-{date}.md"
    rot = (f"<!--\nfile: context/handoff/archive/{name}\npurpose: {last_lbl} → {first_lbl} ({n} blocks) rotated VERBATIM out of pm-handoff.md at {beat_label} "
           f"(the live cap is {LIVE_BEATS_CAP} blocks; {len(heads)} live before, {len(heads) - n} + the {short} block after). bytes(kept) + bytes(archived body) + 1 = bytes(before), asserted inside beat() before the write.\n"
           f"audience: any session that a live beat or the archive map sends here\nstate-type: archive (verbatim; never edited)\nstatus: ARCHIVED {date} ({short}; {ct}; instrument {stamp})\n-->\n\n"
           f"# pm-handoff beats rotated at {beat_label} — {last_lbl} → {first_lbl} (newest first, verbatim)\n\n" + body + "\n")
    row = (f"- {last_lbl} → {first_lbl} ({n} blocks; {dates}) → `archive/{name}` (verbatim; rotated {date}, {short}, under the ≤{LIVE_BEATS_CAP}-live-blocks rule; "
           f"bytes asserted: kept + archived body + 1 = before)")
    assert any(l.startswith(_MAP) for l in kept), "no archive map"
    if map_anchor:
        mi = [i for i, l in enumerate(kept) if l.startswith(map_anchor)]; assert len(mi) == 1, f"map anchor count {len(mi)}: {map_anchor[:60]!r}"; kept.insert(mi[0], row)
    else:
        assert kept[-1] == "" and kept[-2].startswith("- "), "the file ends with the map's last row and one newline"; kept.insert(len(kept) - 1, row)
    return "\n".join(kept), name, rot, row, nb

def beat(ctx):
    """ONE BEAT. (1) EVERY assert and cap before the first byte: the chain ≤ CHAIN_CAP, the block ≤ BEAT_CAP, the snapshot ≤ SNAP_CAP and
    the brief ≤ BRIEF_CAP (with the two digest regions rendered from `state_path` when given — their own caps inside render_state),
    the live-beat cap with the rotation of the oldest `rotate_n` (6) blocks VERBATIM when the insert would breach LIVE_BEATS_CAP,
    the chain archive's heading count, the trailer grep on EVERY text. (2) The writes in one pass. (3) The post-write reads, the
    census from porcelain and the card. Nothing is written when any assert fails.
    ctx — paths: {handoff, archive, snapshot, brief} (the rotated-beats archive lands beside `archive`) · beat_prefix_old (the live
    seg0's prefix, e.g. "2026-10-08 (v100 beat 3") · seg0 · snapshot_seg0 (both without their closing paren) · pointer_edits
    [(old, new)…] applied to the handoff pointer with once() · beat_block (`## 20…`, one trailing newline) · rotation_heading ·
    archive_count (the chain archive's heading count before) · date · beat_label ("v101 beat 1") · ct · stamp · optional:
    state_path, rotate_n, map_anchor, extra_texts {path: text} (never a spine path), msg + msg_path, repo + exp_M/exp_A/exp_D,
    card {repo_key, paths, msg_rel, say_back, note}.
    Returns {texts, caps, rotation, live, census, card}."""
    P = ctx["paths"]; P_h, P_a, P_s, P_b = (pathlib.Path(P[k]) for k in ("handoff", "archive", "snapshot", "brief"))
    seg0, block, sseg0, rot_head = ctx["seg0"], ctx["beat_block"], ctx["snapshot_seg0"], ctx["rotation_heading"]
    assert block.startswith("## 20") and block.endswith("\n") and not block.endswith("\n\n"), "the block: `## 20…` with one trailing newline"
    assert nbytes(block) <= BEAT_CAP, f"CAP beat {nbytes(block)} > {BEAT_CAP}"
    assert ") Prior: " not in seg0 and ") Prior: " not in sseg0, "a segment never carries the chain separator"
    h0, a0, s0, b0 = rd(P_h), rd(P_a), rd(P_s), rd(P_b)
    # the chain
    hl = h0.split("\n"); seg0_old, seg1_old, ptr = chain_split(hl[7], ctx["beat_prefix_old"])
    for old, new in ctx.get("pointer_edits", ()): ptr = once(ptr, old, new)
    line8 = f"last-verified: {seg0}) Prior: {seg0_old}) Prior: {ptr}"; assert nbytes(line8) <= CHAIN_CAP, f"CAP chain {nbytes(line8)} > {CHAIN_CAP}"
    hl[7] = line8; h1 = "\n".join(hl)
    # the live-beat cap → the rotation first, when the insert would breach it
    heads, _ = live_blocks(hl); live = len(heads); rotation = None; texts = {}
    if live + 1 > LIVE_BEATS_CAP:
        n = ctx.get("rotate_n", 6)
        h1, name, rot_text, row, nb = rotate_beats(h1, n, ctx["date"], ctx["beat_label"], ctx["ct"], ctx["stamp"], ctx.get("map_anchor"))
        rot_path = P_a.parent / name; assert not rot_path.exists(), f"exists: {rot_path}"; texts[rot_path] = rot_text
        rotation = {"name": name, "path": rot_path, "rows_out": n, "live_before": live, "map_row": row, "bytes": nb}; hl = h1.split("\n")
    bi, live_now = beat_index(hl); hl[bi:bi] = block.rstrip("\n").split("\n") + [""]; h_new = "\n".join(hl)
    # the chain archive (the counted record)
    a_new, _add = rotate_chain(a0, seg1_old, rot_head, ctx["archive_count"])
    # the snapshot chain; the two digest regions when a state is given
    sl = s0.split("\n"); sseg0_old, _s1, sptr = chain_split(sl[7], ctx["beat_prefix_old"]); sl[7] = f"last-verified: {sseg0}) Prior: {sseg0_old}) Prior: {sptr}"
    s_new = "\n".join(sl); b_new = b0; caps = {}
    if ctx.get("state_path"): s_new, b_new, caps = render_regions(ctx["state_path"], s_new, b_new)
    caps.update({"chain": (nbytes(line8), CHAIN_CAP), "beat": (nbytes(block), BEAT_CAP), "snapshot": (nbytes(s_new), SNAP_CAP), "brief": (nbytes(b_new), BRIEF_CAP)})
    for k, (v, cap) in caps.items(): assert v <= cap, f"CAP {k} {v} > {cap}"
    texts.update({P_h: h_new, P_a: a_new, P_s: s_new})
    if b_new != b0: texts[P_b] = b_new
    for p, t in ctx.get("extra_texts", {}).items(): p = pathlib.Path(p); assert p not in (P_h, P_a, P_s, P_b), f"a spine path in extra_texts: {p}"; texts[p] = t
    if ctx.get("msg_path"): texts[pathlib.Path(ctx["msg_path"])] = ctx["msg"]
    no_trailers(seg0, sseg0, rot_head, *texts.values())
    # (2) THE WRITE PASS — nothing above wrote a byte
    for p, t in texts.items(): wr(p, t)
    # the post-write reads (the v90 b6 lesson: every edited row found once)
    hc = rd(P_h).split("\n"); heads_after, _ = live_blocks(hc); assert len(heads_after) == live_now + 1, (len(heads_after), live_now + 1)
    assert_rows(rd(P_h), block.split("\n")[0], line8); assert len(re.findall(r"^## ", rd(P_a), re.M)) == ctx["archive_count"] + 1
    assert rd(P_s).split("\n")[7].startswith(f"last-verified: {sseg0}) Prior: ")
    if rotation: assert_rows(rd(P_h), rotation["map_row"]); assert rd(rotation["path"]).count("\n## 20") == rotation["rows_out"]
    out = {"texts": texts, "caps": caps, "rotation": rotation, "live": live_now + 1, "census": None, "card": None}
    # (3) the census from porcelain and the card
    if ctx.get("repo"):
        out["census"] = census(pathlib.Path(ctx["repo"]), ctx["exp_M"], ctx["exp_A"], ctx.get("exp_D", frozenset()))
        if ctx.get("card"):
            c = ctx["card"]; out["card"] = card(c["repo_key"], c["paths"], out["census"][0], c["msg_rel"], c["say_back"], c.get("note", ""))
    return out

# context/process/splice_lib_v1.py — the hub's per-beat splice library (adopted v73 beat 1, 2026-09-13; the v72 plan §4 refinement).
# Purpose: the mechanics every beat script repeats — the paths, the clock, porcelain, the guarded anchors, the chain split and
# rotation, the region caps, the census COMPUTED from porcelain, the trailer check, the card form — so a beat script carries only
# its own anchors, texts and asserts. THE GUARDED-SPLICE LAW is unchanged: the beat script runs every assert and cap BEFORE its
# first byte; this file only supplies the instruments. Every beat script asserts this file's md5 (LIB_MD5) before use; a change
# here is a NEW version file (splice_lib_v2.py), never an edit in place. Stateless by design: no HEADs, no beat numbers, no texts.
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

def sub_once(text, pattern, repl, flags=re.M):
    ms = list(re.finditer(pattern, text, flags)); assert len(ms) == 1, f"pattern count {len(ms)}: {pattern[:90]!r}"
    m = ms[0]; return text[:m.start()] + repl + text[m.end():]

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

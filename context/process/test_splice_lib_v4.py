# context/process/test_splice_lib_v4.py — card_v2()'s five cases: the EMITTED card run by bash in a throwaway repo with a bare origin
# (BEAT-RENDERER-2 U2; red first). Run: PYTHONIOENCODING=utf-8 python3 -B context/process/test_splice_lib_v4.py — each case lives in its
# own tempfile.TemporaryDirectory() laid out as <tmp>/origin.git + <tmp>/Desktop/Code/ClaudeFolder/{nexsys-hivemind,_scratch} with HOME
# = <tmp>, so the card's `cd ~/...` runs exactly as emitted; no real repository is read or written. The preconditions (v2's and v3's
# md5s; v4 = header + v3 + section; lib_md5(); the sample card's exact text and form; the refused inputs; the bash in use) are plain
# asserts BEFORE the cases, so a breach aborts loudly. Case 5 runs in a PRE-POISONED shell and carries its control: the same card
# minus its `unset M T N && ` commits there — the hardening is what refuses.
import sys; sys.dont_write_bytecode = True
import hashlib, importlib.util, os, pathlib, re, shutil, subprocess, tempfile
HERE = pathlib.Path(__file__).resolve().parent
V2, V3, V4 = HERE / "splice_lib_v2.py", HERE / "splice_lib_v3.py", HERE / "splice_lib_v4.py"
def md5b(b): return hashlib.md5(b).hexdigest()
v2b, v3b, v4b = V2.read_bytes(), V3.read_bytes(), V4.read_bytes()
# ---- preconditions 1: the bytes (v2 and v3 never edited; v4 = a header + v3 VERBATIM + the v4 section; pure addition)
assert md5b(v2b) == "99e87f2dbafaade35e071770b14b5557", "splice_lib_v2.py edited"
assert md5b(v3b) == "fc79eee9d1af94e424e1560856c8b3f2", "splice_lib_v3.py edited"
assert b"\r" not in v4b and v4b.endswith(b"\n") and not v4b.endswith(b"\n\n"), "v4: LF only, one trailing newline"
assert v4b.count(v3b) == 1, "v4 does not carry v3's bytes exactly once"
HEAD4, SECT4 = v4b.split(v3b); assert v4b == HEAD4 + v3b + SECT4
hl = HEAD4.decode("utf-8").split("\n")
assert hl[0].startswith("# context/process/splice_lib_v4.py") and hl[-1] == "" and hl[-3] == "import sys; sys.dont_write_bytecode = True", "the v4 header form"
assert hl[-2].startswith("# ----") and "v3 VERBATIM" in hl[-2] and all(l.startswith("# ") for l in hl[:-3]), "the v4 header: comments, the import, the marker"
assert SECT4.startswith(b"# ==== v4: card_v2() ====\n"), "the v4 section marker"
assert set(re.findall(rb"^def (\w+)", SECT4, re.M)) == {b"card_v2"}, "the v4 section defines card_v2() and nothing else"
for name in re.findall(rb"^(\w+) = ", SECT4, re.M): assert not re.search(rb"\b" + name + rb"\b", v3b), "the v4 section shadows a v3 name: %r" % name
spec = importlib.util.spec_from_file_location("splice_lib_v4", V4); lib = importlib.util.module_from_spec(spec); spec.loader.exec_module(lib)
assert lib.lib_md5() == md5b(v4b), "lib_md5() is not v4's own md5"
# ---- preconditions 2: the sample card, its exact command and the binding properties
GREP = "'Co-Authored\\|Claude-Session'"
SAMPLE = dict(repo_key="hivemind", paths=["a.md", "b.md"], n=2, msg_rel="v104/b2/msg.txt", head_sha="8ab4789", say_back="HIVE: LANDED <sha>")
WANT = (r'''unset M T N && cd ~/Desktop/Code/ClaudeFolder/nexsys-hivemind && M=../_scratch/v104/b2/msg.txt && T=$(grep -c 'Co-Authored\|Claude-Session' $M) ; '''
        r'''echo "head=$(git --no-optional-locks log -1 --format=%h) branch=$(git --no-optional-locks rev-parse --abbrev-ref HEAD) porcelain=$(git --no-optional-locks status --porcelain | wc -l) locks=$(ls .git/*.lock 2>/dev/null | wc -l) trailers=$T" && '''
        r'''[ "$(git --no-optional-locks log -1 --format=%h)" = 8ab4789 ] && [ "$(git --no-optional-locks rev-parse --abbrev-ref HEAD)" = main ] && [ ! -e .git/index.lock ] && [ "$T" -eq 0 ] && '''
        r'''git add -- a.md b.md && N=$(git diff --cached --name-status --no-renames | wc -l) ; echo "staged: $N (expect 2)" && [ "$N" -eq 2 ] && git commit -F $M && git push && git log -1 --oneline''')
def split_card(card):
    m = re.fullmatch(r"([^\n]+)\n```\n([^\n]+)\n```\n(Read: [^\n]+)\n", card); assert m, "the card's form: a title line, a fenced ONE-LINE command, a Read line"
    return m.group(1), m.group(2), m.group(3)
CARD = lib.card_v2(**SAMPLE); title, cmd, read = split_card(CARD)
assert cmd == WANT, "the sample command differs from the pinned text:\n" + cmd
assert "GATED (the commit and the push run only if HEAD, branch, lock, trailers and the staged count hold)" in title and title.endswith("In Git Bash, ONE paste:")
assert read.startswith("Read: `head=8ab4789 branch=main porcelain=2 locks=0 trailers=0` ") and read.endswith("Say back `HIVE: LANDED <sha>`.")
assert CARD.count(GREP) == 1 and cmd.count("T=$(") == 1 and "; git commit" not in CARD and "; git push" not in CARD, "the grep once; T once; no ; before a commit or a push"
ci = cmd.index("git commit"); assert all("grep" not in cmd[p:ci] for p in range(ci) if cmd[p] == ";"), "the trailer grep sits between a ; and the commit"
assert cmd.startswith("unset M T N && cd ") and cmd.count("unset") == 1, "the hardening: unset first"
lib.no_trailers(CARD.replace(GREP, "", 1))
def refused(**kw):
    a = dict(SAMPLE); a.update(kw)
    try: lib.card_v2(**a)
    except AssertionError: return
    raise AssertionError("card_v2 accepted %r" % (kw,))
refused(repo_key="nope"); refused(n=3); refused(n=True, paths=["a.md"]); refused(n="2"); refused(n=0, paths=[]); refused(paths=["a.md", "a.md"])
for sha in ("8AB4789", "8ab478", "8ab4789z", "8" * 41, ""): refused(head_sha=sha)
for bad in ("a b.md", "a;b", "a$b", "a`b", "a|b", "a&b", "a'b", 'a"b', "a\nb", "a>b", "a*b", "a!b", "#a", "~/a", "{a,b}", "{a..c}",
            "newdir/", "/abs.md", "./a.md", "a/../b.md", "a//b.md", ".", ".."): refused(paths=["a.md", bad]); refused(msg_rel=bad)
for bad in ("x`y", "x$y", "x;y", "x|y", "x&y", "x'y", 'x"y', "x\ny", "", "Co-" + "Authored-By x"): refused(say_back=bad)
# ---- preconditions 3: the bash that runs the card (on this Windows desk a bare `bash` can resolve to the WSL launcher, which breaks)
BASH = shutil.which("bash"); assert BASH, "no bash on PATH"
assert "/system32/" not in BASH.replace("\\", "/").lower() and "/windowsapps/" not in BASH.replace("\\", "/").lower(), \
    "bash resolves to " + BASH + " (the WSL launcher): run this from Git Bash, where it is C:\\Program Files\\Git\\usr\\bin\\bash.EXE"
assert shutil.which("git"), "no git on PATH"

MSG_REL = "v104/b2/msg.txt"; SAY = "HIVE: LANDED <sha>"
MSG = "test: the gated card lands the census\n\nCensus: 2 = 1 M + 1 A.\n"
TRAILER_MSG = MSG + "\nCo-" + "Authored-By: x <x@x>\n"           # split so this file carries no trailer line of its own
PATHS = ["a.md", "docs/{{NAME}}_c.md"]                            # one M, one A; the braces are literal in bash (no comma, no ..)
def env_for(tmp):
    e = {k: v for k, v in os.environ.items() if not k.upper().startswith("GIT_") and k.upper() != "XDG_CONFIG_HOME"}
    e.update(HOME=tmp.as_posix(), GIT_CONFIG_NOSYSTEM="1", GIT_TERMINAL_PROMPT="0"); return e
def git(env, cwd, *args):
    r = subprocess.run(["git", *args], cwd=cwd, env=env, capture_output=True, text=True, encoding="utf-8")
    assert r.returncode == 0, ("git", args, r.returncode, r.stderr[-400:]); return r.stdout.strip()
def put(p, s): p.parent.mkdir(parents=True, exist_ok=True); p.write_bytes(s.encode("utf-8"))
def fixture(tmp, msg=MSG):
    """<tmp>/origin.git (bare, main) · the clone at ~/Desktop/Code/ClaudeFolder/nexsys-hivemind with one commit pushed by the TEST ·
    the message at ~/Desktop/Code/ClaudeFolder/_scratch/<MSG_REL>. Returns the fixture as a dict."""
    tmp = pathlib.Path(tmp); env = env_for(tmp); cf = tmp / "Desktop/Code/ClaudeFolder"; repo = cf / "nexsys-hivemind"; origin = tmp / "origin.git"
    cf.mkdir(parents=True); git(env, tmp, "init", "-q", "--bare", "-b", "main", origin.as_posix()); git(env, cf, "clone", "-q", origin.as_posix(), "nexsys-hivemind")
    for k, v in (("user.name", "t"), ("user.email", "t@t.invalid"), ("commit.gpgsign", "false"), ("core.autocrlf", "false")): git(env, repo, "config", k, v)
    git(env, repo, "symbolic-ref", "HEAD", "refs/heads/main")
    for rel in ("a.md", "docs/b.md", "keep.md"): put(repo / rel, "base " + rel + "\n")
    git(env, repo, "add", "-A"); git(env, repo, "commit", "-q", "-m", "init"); git(env, repo, "push", "-q", "-u", "origin", "main")
    put(cf / "_scratch" / MSG_REL, msg)
    fx = {"tmp": tmp, "env": env, "repo": repo, "origin": origin, "h0": git(env, repo, "rev-parse", "HEAD"), "s0": git(env, repo, "log", "-1", "--format=%h")}
    assert git(env, tmp, "--git-dir", origin.as_posix(), "rev-parse", "main") == fx["h0"]; return fx
def dirty(fx):
    """The census: a.md modified, docs/{{NAME}}_c.md added; z.md is an untracked bystander the card never names."""
    put(fx["repo"] / "a.md", "base a.md\nedited\n"); put(fx["repo"] / PATHS[1], "new\n"); put(fx["repo"] / "z.md", "bystander\n")
def run_card(fx, card, prefix=""):
    """The card's one line, exactly as emitted (optionally after a poisoning prefix), by bash -c with HOME = the fixture; cwd = the
    temp root, so a failed `cd` can never reach a real repository."""
    r = subprocess.run([BASH, "-c", prefix + split_card(card)[1]], cwd=fx["tmp"], env=fx["env"], capture_output=True, text=True, encoding="utf-8")
    fx["out"] = r.stdout; return r
def head(fx): return git(fx["env"], fx["repo"], "rev-parse", "HEAD")
def origin_main(fx): return git(fx["env"], fx["tmp"], "--git-dir", fx["origin"].as_posix(), "rev-parse", "main")
def staged(fx): return sorted(l.split("\t", 1)[1] for l in git(fx["env"], fx["repo"], "--no-optional-locks", "diff", "--cached", "--name-status").splitlines())
def no_commit(fx, r):
    assert r.returncode != 0, "the card exited 0: " + r.stdout[-300:]
    assert head(fx) == fx["h0"] and origin_main(fx) == fx["h0"], "a commit or a push happened: " + r.stdout[-300:]

RESULTS = []
def check(name, fn):
    try: fn(); RESULTS.append((name, "")); print("ok   " + name)
    except Exception as e: RESULTS.append((name, (type(e).__name__ + ": " + str(e))[:600])); print("FAIL " + name + ": " + RESULTS[-1][1])

def c1_n_paths_commit_and_push():
    with tempfile.TemporaryDirectory() as tmp:
        fx = fixture(tmp); dirty(fx); (fx["repo"] / "docs/b.md").unlink(); put(fx["repo"] / "docs/b_moved.md", "base docs/b.md\n")   # a move: D + A, one R to git
        ps = PATHS + ["docs/b.md", "docs/b_moved.md"]; r = run_card(fx, lib.card_v2("hivemind", ps, 4, MSG_REL, fx["s0"], SAY)); out = r.stdout.splitlines()
        assert r.returncode == 0, (r.returncode, r.stdout[-300:], r.stderr[-300:])
        assert out[0] == "head=" + fx["s0"] + " branch=main porcelain=5 locks=0 trailers=0" and "staged: 4 (expect 4)" in out, out
        new = head(fx); assert new != fx["h0"] and git(fx["env"], fx["repo"], "rev-parse", "HEAD~1") == fx["h0"], "not ONE commit on the start sha"
        assert origin_main(fx) == new, "origin main != local HEAD after the push"
        assert sorted(git(fx["env"], fx["repo"], "diff-tree", "--no-commit-id", "--name-only", "-r", "HEAD").splitlines()) == sorted(ps), "the commit touches other than the n paths"
        assert "R100\tdocs/b.md\tdocs/b_moved.md" in git(fx["env"], fx["repo"], "show", "-M", "--name-status", "--format=", "HEAD"), "the move is not a rename to git, so --no-renames went untested"
        assert git(fx["env"], fx["repo"], "log", "-1", "--format=%B") == MSG.strip() and out[-1].startswith(git(fx["env"], fx["repo"], "log", "-1", "--format=%h") + " ")
        assert git(fx["env"], fx["repo"], "--no-optional-locks", "status", "--porcelain") == "?? z.md", "the bystander was touched"

def c2_count_mismatch_no_commit():
    with tempfile.TemporaryDirectory() as tmp, tempfile.TemporaryDirectory() as tmp2:
        fx = fixture(tmp); dirty(fx); r = run_card(fx, lib.card_v2("hivemind", PATHS + ["keep.md"], 3, MSG_REL, fx["s0"], SAY))
        no_commit(fx, r); assert "staged: 2 (expect 3)" in r.stdout.splitlines(), r.stdout
        assert staged(fx) == sorted(PATHS), "the chain did not stop at the count gate"
        # the other direction: n expected, n+1 staged (a foreign path already in the index rides along) — refused the same way
        fx = fixture(tmp2); dirty(fx); put(fx["repo"] / "x.md", "foreign\n"); git(fx["env"], fx["repo"], "add", "--", "x.md")
        r = run_card(fx, lib.card_v2("hivemind", PATHS, 2, MSG_REL, fx["s0"], SAY)); no_commit(fx, r)
        assert "staged: 3 (expect 2)" in r.stdout.splitlines() and staged(fx) == sorted(PATHS + ["x.md"]), r.stdout

def c3_trailer_no_commit():
    with tempfile.TemporaryDirectory() as tmp:
        fx = fixture(tmp, TRAILER_MSG); dirty(fx); r = run_card(fx, lib.card_v2("hivemind", PATHS, 2, MSG_REL, fx["s0"], SAY))
        no_commit(fx, r); out = r.stdout.splitlines(); assert out[0].endswith(" trailers=1") and "staged:  (expect 2)" in out, out
        assert staged(fx) == [], "the card staged behind a trailer"

def c4_stale_index_lock_no_commit():
    with tempfile.TemporaryDirectory() as tmp:
        fx = fixture(tmp); dirty(fx); lock = fx["repo"] / ".git/index.lock"; lock.write_bytes(b"")
        try:
            r = run_card(fx, lib.card_v2("hivemind", PATHS, 2, MSG_REL, fx["s0"], SAY)); out = r.stdout.splitlines()
            assert " locks=1 " in out[0] and "staged:  (expect 2)" in out, out
            assert "index.lock" not in r.stderr, "the gate did not stop the chain; git itself met the lock: " + r.stderr[-300:]
        finally: lock.unlink()
        no_commit(fx, r); assert staged(fx) == [], "the card staged under a lock"

def c5_wrong_head_poisoned_shell_no_commit():
    poison = "N=2; T=0; M=../_scratch/" + MSG_REL + "; "
    def poisoned(tmp):
        fx = fixture(tmp); dirty(fx); git(fx["env"], fx["repo"], "add", "--", *PATHS); assert staged(fx) == sorted(PATHS); return fx
    with tempfile.TemporaryDirectory() as tmp, tempfile.TemporaryDirectory() as tmp_ctl:
        fx, ctl = poisoned(tmp), poisoned(tmp_ctl); bad = "0000000"; assert bad not in (fx["s0"], ctl["s0"])
        card = lib.card_v2("hivemind", PATHS, 2, MSG_REL, bad, SAY); assert split_card(card)[1].startswith("unset M T N && ")
        r = run_card(fx, card, poison); no_commit(fx, r); out = r.stdout.splitlines()
        assert out[0].startswith("head=" + fx["s0"] + " ") and "staged:  (expect 2)" in out, out
        assert staged(fx) == sorted(PATHS), "the pre-staged index changed"
        # the control: the SAME card without its `unset M T N && ` in the same poisoned shell commits (and pushes) — the hole is real
        ctl_card = card.replace("unset M T N && ", "", 1); rc = run_card(ctl, ctl_card, poison)
        assert "staged: 2 (expect 2)" in rc.stdout.splitlines() and head(ctl) != ctl["h0"] and origin_main(ctl) == head(ctl), \
            "the control did not commit, so this case proves nothing: " + rc.stdout[-300:]
    # the right sha on the wrong branch (HEAD's ref is not main), in the same poisoned shell: the branch gate refuses
    with tempfile.TemporaryDirectory() as tmp:
        fx = poisoned(tmp); git(fx["env"], fx["repo"], "checkout", "-q", "-b", "side")
        r = run_card(fx, lib.card_v2("hivemind", PATHS, 2, MSG_REL, fx["s0"], SAY), poison); no_commit(fx, r); out = r.stdout.splitlines()
        assert out[0].startswith("head=" + fx["s0"] + " branch=side ") and "staged:  (expect 2)" in out, out
        assert git(fx["env"], fx["repo"], "rev-parse", "side") == fx["h0"], "a commit landed on the side branch"

for name, fn in (("case 1 - n paths (a move among them, counted as its two paths): ONE commit of exactly the n paths, pushed; origin main == HEAD; staged: n (expect n)", c1_n_paths_commit_and_push),
                 ("case 2 - n+1 against n, both ways (n+1 expected; n+1 staged): the count gate refuses; HEAD and origin main unchanged", c2_count_mismatch_no_commit),
                 ("case 3 - a trailer in the message: no commit, nothing staged", c3_trailer_no_commit),
                 ("case 4 - a stale empty .git/index.lock: no commit, nothing staged", c4_stale_index_lock_no_commit),
                 ("case 5 - the wrong HEAD in a poisoned shell (N, T, M stale; the n paths pre-staged): no commit; the control without unset commits; the right sha on a non-main branch: no commit", c5_wrong_head_poisoned_shell_no_commit)):
    check(name, fn)
fails = sum(1 for _, e in RESULTS if e); print("splice_lib_v4 selftest: %d check(s), %d failure(s)" % (len(RESULTS), fails)); sys.exit(1 if fails else 0)

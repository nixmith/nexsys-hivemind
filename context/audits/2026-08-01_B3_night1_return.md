<!--
file: context/audits/2026-08-01_B3_night1_return.md
purpose: B3 NIGHT-1 CLOSING RETURN (supersedes this lane's 09:03 / 09:35 / 09:50 drafts).
         Carries: success-criterion verdict (MET) · ONE structural defect, mechanism
         now CLOSED, fix APPLIED and pending its scheduler-run gate · the margin
         finding (3.652 s against a 5.369 s CORE window — the 20 s scenario poll is
         NOT headroom) · five evidence-integrity findings the hub has not seen ·
         three corrections including one of this lane's own that was FALSE · the
         one-word repair to INSTALL-6.
audience: the PM hub. §3 needs a ruling on scope; §5 needs one on bundle evidence.
status: CLOSED 2026-08-01 ~10:05 EDT. Pi at a791c99, tree clean, main. Bench RUNNING
        (pid 65244). KillMode=process drop-in APPLIED and verified live (Type=oneshot /
        KillMode=process). NO commit by this lane; nothing in either repo was touched.
        ONE open hop remains (is a syslog daemon running — ACTION-5, changes one
        recommendation only). The gate is tomorrow's 04:30 fire: ACTION-2.
-->

# B3 — night-1 closing return (2026-08-01)

## 1. Verdict in one paragraph

**B3's success criteria are MET, and B3 has one structural defect whose mechanism is
now closed.** The nightly fired on its own timer at 04:30:12 EDT, swapped the config,
restarted, asserted the hero ABSENT on a positive read, ran nine legs (8 PASS + 1
honest SKIP), restored, asserted the hero PRESENT, mined a real DISPATCHED→CONFIRMED
latency from a real bundle, and wrote one digest line in the ruled grammar — the whole
DP-1…DP-6 chain, on hardware, unattended, first try. Then `systemd` SIGTERMed the app
it had deliberately left running, and the bench stayed dead **4 h 55 m**. The wrapper
reported `Result=success`, exit 0. **The wrapper cannot assert its own aftermath** —
verify-restored runs before the kill — so the guard had to be structural; a
`KillMode=process` drop-in is applied and verified live, and tomorrow's 04:30 fire is
its gate. Three further things the hub has not seen: the first real ON-latency sits at
**68 % of the core confirmation window** in a class the constants did not predict for
this leg; **there is currently no trustworthy wrapper-side timeline** (its output is
block-buffered, its log carries no timestamps of its own); and every bundle's
`journal-slice.txt` is **untargeted noise that reads as evidence**.

## 2. The defect — mechanism CLOSED

Four predictions were printed into the transcript before the reads. All four hit; H2
(trap double-restore) and H3 (explicit stop) are refuted — the wrapper log shows
restore exactly once and **line 88 of 88 IS the digest**, terminal, nothing after.

**The decisive proof is not any of the four — it is a two-second gap.**

```
ExecMainStartTimestamp = 04:30:12          (systemd's own accounting)
ExecMainExitTimestamp  = 04:31:52          (nightly.sh's main process ends)
app log 04:31:52.417   Javalin stopping    (the app's own clock — SIGTERM arrives)
app log 04:31:54.198   HomeSynapseCore stopped ... (SIGTERM)
systemd 04:31:54       Finished nexsys-bench-nightly.service
                       Result=success · KillMode=control-group · Type=oneshot
```

**A `oneshot` unit whose main process has exited declares `Finished` immediately —
unless it is waiting for its cgroup to empty. It waited exactly as long as the app took
to shut down.** systemd only waits on cgroup members, so the app was in the unit's
cgroup, and `KillMode=control-group` is what emptied it. That closes the mechanism
structurally rather than by inference. (The `CPU: 33.916s` charged to the unit — three
JVM starts — corroborates the same membership.)

**Pre-empting the obvious objection.** Finding G-1 below establishes that the wrapper's
journal timestamps are buffer-flush artifacts, not event times. That does **not**
disturb this timeline: every timestamp above comes from systemd's own accounting or
from the app's own log file. No step of the H1 chain rests on a buffered line.

**The night, from the wrapper's own log:**

```
04:30:12  timer fires (PIN-3 REC branch, OnCalendar=03:30 America/Chicago)
L1        nightly starting (branch B; constants pinned)
L2-6      quiesce swap done -> stop -> launch pid 64019 -> boot#1  automations=0
L19-20    [OK] quiesce ASSERTED: HTTP 200, non-empty body, '"bench-hero"' ABSENT
L21-24    suite auto, 9 legs, ceiling 45m
L25-29    boot-health leg restarts the app -> pid 64150 -> boot#2  automations=0
L43-67    eight bundles, 04:30:51 -> 04:31:32   (all cut from boot#2 — quiescence
                                                 held across the ENTIRE suite)
L70-74    restore swap done -> stop -> launch pid 64394 -> boot#3  automations=1
L87       [OK] restore ASSERTED: HTTP 200, '"bench-hero"' PRESENT
L88       [--] digest: ... 8/9 PASS · 1 SKIP(hue-online) · RESTORED ✓ · 3.65s
   ---- wrapper ends here ----
04:31:52.4  systemd SIGTERMs the cgroup                 <-- THE DEFECT
04:31:54.2  app shutdown completes; unit Finished; Result=success
09:27:15  bench restored by hand (pid 65244, RADIO UP 12s, 6/6 relinked)
```

`automations = 0 / 0 / 1` across the three boots is **app-side positive evidence of the
swap**, from an instrument the wrapper does not control — and every bundle names
`bench-2026-08-01-043039.log` as its source, proving quiescence held for the whole
suite, not just the moment of the assert.

**The class lesson, which outlives the bug.** The desk proved this wrapper across 25
harness checks including a TERM-mid-suite run with a deliberately non-vacuous restore
assert, and could not have caught this: a hand run puts the app in a different cgroup.
**A scheduler-only defect needs a scheduler-run gate.** For B3 that gate costs one
command at breakfast.

## 3. The fix — APPLIED, and the scope argument behind it

`~/.config/systemd/user/nexsys-bench-nightly.service.d/killmode.conf` is in place;
`systemctl --user show` now returns `Type=oneshot` / `KillMode=process`. The repo's
committed `tools/scheduler/nexsys-bench-nightly.service` is **byte-untouched**, and the
undo is `rm -rf` the drop-in dir + `daemon-reload`.

**Why unit-local rather than in bench.sh.** The defect is *specific to the REC branch* —
the cron fallback has no unit cgroup to tear down and would never have exhibited it. A
`bench.sh` change would impose systemd process semantics on a branch that never had the
problem. The hub may still want the drop-in folded in-repo (four lines beside the unit),
and may later want option **C** — the app as its own `homesynapse-bench.service` with
bench.sh delegating start/stop/restart to `systemctl --user`. C is architecturally right
(own cgroup, restart-on-failure, journal capture, boot autostart) but costs a bench.sh
rewrite, has to preserve the `bench-<ts>.log` / `current.log` naming, and couples
bench.sh to systemd, breaking parity with the ruled cron branch. Not a tonight decision.

**Honest caveat on the applied fix:** with `KillMode=process` the surviving app keeps the
old cgroup alive after the unit deactivates, so later starts may log `Found left-over
process … in control group`. systemd tolerates this and proceeds. Untidy, not unsafe —
and it is the first thing to look for in tomorrow's journal.

**Kill this before it is proposed:** `setsid` / `nohup` / `disown` do **not** fix this.
Cgroup membership is inherited and is not escaped by detaching a session or ignoring
SIGHUP. Only a new scope (`systemd-run --user --scope`) or a separate unit moves a
process out of the cgroup that gets killed.

## 4. The margin — and a distinction that could be misread as slack

`constants.yaml` :198–203 carries the ceiling: **the core confirmation window is
5.369 s**, with prior observations of *111 ms (S-1)* and *3.8–5.0 s (Rep A,
polling-granular)*, n=2. It also records the expectation for this exact leg (:183–184):
*"the next night's command-confirm-s31 fires a real ON-edge against an IDLE clock and
confirms in the S-1-rep-1 class."*

**It did not.** Computed from the bundle's own lifecycle:

```
ACCEPTED    08:30:51.785415Z
DISPATCHED  08:30:51.791181Z    ACCEPTED->DISPATCHED       5.77 ms
report      08:30:55.433336Z    DISPATCHED->report      3.642155 s   <- device + radio
CONFIRMED   08:30:55.442935Z    report->CONFIRMED          9.60 ms   <- core

DISPATCHED->CONFIRMED  3.651754 s   (the digest's 3.65s, arithmetic verified)
core confirmation window   5.369 s
used                        68.02 %
headroom                    1.717 s   (31.98 %)
```

1. **The prediction missed by class, not by margin.** Predicted the S-1 class (111 ms);
   measured 3.652 s — the polling-granular class, ~33×. The leg PASSED, so this is not a
   red; it is **the margin watch expressing itself on night 1**, with a third distinct
   value now on file (0.111 s · 3.8–5.0 s · 3.652 s, n=3).
2. **The latency is not ours.** 3.642 s of the 3.652 s is device + radio; the core
   contributed **9.60 ms — 0.26 %**. Remediation aimed at core-side latency is aimed at
   the wrong quarter-percent. If the S31 reports on a poll rather than an attribute
   report, the distribution is quantised by the poll period and its upper tail decides
   whether this leg is stable.
3. **The 20 s in the verdict file is NOT headroom.** `verdict.txt` reads *"all asserts
   satisfied (within 20s)"* — that is the runner's **poll window**, i.e. how long the
   scenario waits to observe a terminal phase. The **core** window is 5.369 s: a report
   arriving later than that makes the command terminal `CONFIRMATION_TIMED_OUT`, and the
   scenario's `phase_terminal: CONFIRMED` assert then fails — it simply waits up to 20 s
   to watch it fail. **Nobody should read the 20 s as slack against the 5.369 s.** The
   real headroom is 1.717 s.
4. **Never-false-CONFIRMED held.** `match_type: "exact"` (no downgrade), and the paired
   state read at the same instant carries `attributes.on.value: true`,
   `availability: AVAILABLE`, `stale: false`. Terminal claim and physical state agree —
   the contract §10's rep exists to police, satisfied here on the settle leg.

**B3's digest already builds the distribution this needs.** That is DP-6 doing its job
on night 1.

## 5. Evidence-integrity findings (NEW — none of these were visible before today)

- **[REVIEW] G-1 — there is no trustworthy wrapper-side timeline.** Every wrapper line
  in the journal is stamped `Aug 01 04:31:52`, including lines describing events at
  04:31:43 and 04:31:51 — the output is **block-buffered and arrives in a lump when the
  process exits**. And `nightly-2026-08-01.log` carries **no wrapper-side timestamps at
  all** (its only times are echoed app-log lines). Consequences: journal times for
  wrapper lines are flush artifacts, not event times; a hard-killed wrapper could lose
  its journal record entirely; and `journalctl -f` on a running nightly shows nothing
  until it finishes. This cost three captures this morning. **Fix is cheap:** timestamp
  the wrapper's own lines, and line-buffer the stream (`stdbuf -oL`, or `tee`'s output
  unbuffered) so the journal is live.
- **[REVIEW] G-2 — every bundle's `journal-slice.txt` is untargeted noise.** MANIFEST
  says *"journalctl since 2026-08-01T08:30:51+00:00"* — no unit filter, no user filter.
  Today's slice, in full, is one line: `tailscaled[1266]: magicsock: derp-16 does not
  know about peer [09sb0], removing route`. It has nothing to do with the scenario, and
  because of G-1 a mid-run window **structurally cannot** contain the wrapper's or
  runner's voice. This is worse than empty: an artifact that looks like evidence and
  could be read as a network anomaly bearing on a Zigbee confirm. There are **61** bundle
  directories on the Pi (link count 63 − 2; this lane said 63 earlier and was wrong);
  this applies to all of them. **Recommend:** filter the slice to
  the relevant unit(s), or drop it in favour of `app-log-slice.log`, which is targeted.
- **[INFO] G-3 — the journal is volatile BY DISTRO POLICY, and its real horizon is about
  a week — ROOT CAUSE PINNED.** `systemd-analyze cat-config` resolves to
  `Storage=volatile` (plus `ForwardToSyslog=yes`), and `/etc/systemd/journald.conf.d/`
  **does not exist** — so the setting arrives from a vendor drop-in outside `/etc`. This
  is deliberate Raspberry Pi OS policy to spare the SD card, **not a misconfiguration and
  not a missed journald restart**; `/var/log/journal/` sits empty for that reason.
  - **F-3b is now fully explained by direct observation.**
    `/run/log/journal/296e7a1d…/` contains **only** `system@…journal` ×2 (archived) and
    `system.journal` (active) — there is **no `user-*.journal` file at all**. That is why
    `journalctl --user` finds nothing while `--user-unit` works. Whether that follows from
    volatile storage or from how `SplitMode=uid` applies here is not pinned and does not
    need to be: the workaround is exact.
  - **The horizon is volume-bound, not reboot-bound.** The runtime journal tree was
    created **2026-07-16 06:27** (tmpfs ⇒ boot time; `/run/user/1000` agrees), so the box
    has ~16 days of uptime — yet the oldest archived journal starts **2026-07-25**.
    **~9 days have already rotated away while the machine stayed up.** Practical
    retention is **~7 days**, capped by `/run` tmpfs, and then zero at reboot. The ~28 MiB
    of RAM this costs on a Pi 5 is not worth raising.
  - **Consequence for B3:** `nightly-<date>.log` is the durable wrapper record; the
    journal is a ~7-day convenience. That makes the INSTALL-6 repair below more than
    cosmetic — the durable artifact must be named first.
  - **One unmeasured hop, and it may make this moot:** `ForwardToSyslog=yes` is set. **If**
    a syslog daemon is running, `/var/log/syslog` already holds a durable, logrotate-managed
    second copy of everything the wrapper emitted, and there is nothing to fix. This lane
    has **not** measured whether one is running — ACTION-5 is four lines and closes it.
    Do not act on journald persistence until that read lands; enabling it writes to the SD
    card on a box whose own app warns about SD storage every boot.
- **[INFO] G-4 — `app-log-slice.log` is 2 lines.** The verdict rested entirely on
  `api-captures.json` (3 exchanges, full lifecycle — excellent). The log half of the
  bundle is thin; a wider window around the markers would cost nothing.
- **[INFO] G-5 — the bundle format is otherwise strong and worth saying so.**
  `MANIFEST.txt` names every artifact and what it is; `verdict.txt` carries scenario,
  verdict, reason, start, duration, source log, markers with a log offset, and per-assert
  evidence lines. G-2 and G-4 are the two weak members of an otherwise well-designed set.

## 6. Corrections — including one of this lane's own that was FALSE

- **F-3a — WITHDRAWN; the cause was this lane's own instrument.** The 09:03 return
  reported `nightly-<date>.log` ABSENT. It exists: `nightly-2026-08-01.log`, 9420 B, 88
  lines. The probe was `ls -la ~/hs-bench/nightly-logs | head -5`, and `head -5` consumed
  *total + `.` + `..` + two entries*, truncating the third file out of existence. **A
  truncated listing manufactured a phantom defect** — the class this project polices in
  others. Standing rule earned: never `head` a listing you intend to reason about
  *absence* from.
- **F-3b — SURVIVES, precisely and repairably.** INSTALL-6 names `journalctl --user -u
  nexsys-bench-nightly.service --since yesterday`. On this box that returns `No journal
  files were found. -- No entries --`, because `--user` selects the *user journal
  namespace*, which has no files here (G-3). The same records are complete in the system
  journal: **`journalctl --user-unit nexsys-bench-nightly.service` works**, as does
  `journalctl _SYSTEMD_USER_UNIT=…`. **The repair is one word.** This is operator-block
  hygiene #27 extended to flags that *exist* and return nothing.
- **F-7 — RESOLVED, no action.** `7c8efbb` states the fixture re-mint excluded the source
  boot's injury tail *by stated design* and ratified OBS-3. This lane's concern was
  uninformed.
- **F-1 / F-2 — STAND.** `bench.sh status` exits 0 while printing `[!!] NOT running`;
  `entities` returned empty with exit 0 against a dead app. **The words carry the
  verdict; the exit code carries nothing.** Tomorrow's gate deliberately uses `pgrep`.
- **F-4 — STANDS, REC branch positively cleared.** `OnCalendar=*-*-* 03:30:00
  America/Chicago` fired at 04:30:12 EDT = 03:30 Chicago, exactly as ruled on an
  `America/New_York` box. Exposure is confined to INSTALL-4's cron fallback (whose stated
  precondition "verify `timedatectl` shows America/Chicago first" is FALSE here) and to
  wall-clock prose such as INSTALL-6's `date -d yesterday`.

## 7. Observations for the hub

- **OBS-A — the runs surface fragments automation history, and nothing can reunify it.**
  `bench.sh runs` returns **13 distinct `automationId`s across 2026-07-19 → 2026-08-01**
  for a config carrying exactly one automation, and `automationName` is **null on all 50
  rows**. `7c8efbb` already knew the ID rotates and correctly pinned the *name* for the
  quiesce assert; the unexamined half is downstream — the runs projection has a name
  field it never populates, so with the ID rotating per boot and the name never set, run
  history cannot be aggregated across restarts by any field the API exposes. A wire field
  that is structurally always null is the dialect-defect class the standing rules already
  name (filed-measurement-first re-pin · full-corpus sweep on any dialect finding). Core,
  not bench — the hub's to scope. Cheapest first read: whether any writer ever sets it.
- **OBS-B — the outage cost is measurable in automation, not uptime.** The newest run in
  the projection is `2026-08-01T04:54:03Z` (00:54 EDT). Between the quiesce at 04:30 and
  the hand restart at 09:27 there was no automation coverage at all — ~8.5 hours in which
  bench-hero could not fire. Unfixed, that is the *daily* cost. (The park held regardless:
  `command-s31-settle` ran LAST and passed, leaving the relay OFF; relay state is in
  hardware.)
- **OBS-D — OBS-1's retention question now has numbers, and they are not urgent.** The
  original B3 return's OBS-1 flagged that `docs/bench-log-retention-policy.md:33`
  anticipates *"bundles copy off nightly with the digest; Pi keeps a 7-day window"* and
  that DP-2 never built it. Measured today: the **journal** already self-prunes to ~7 days
  by RAM pressure (G-3), while everything B3 writes grows unbounded — 61 bundle
  directories, ~70 `bench-*.log` files (~1.25 MB), plus `nightly-logs/` and `digests/`
  accumulating one entry per night. Disk is **not** the pressure: `df` reads 14 G used of
  117 G (12 %). So the retention policy is a hygiene and evidence-locatability question,
  not a capacity one — worth ruling at leisure, and worth *not* prioritising over §9's
  items 1–4.
- **OBS-C — the event DB is on the SD card, and the app says so every boot.**
  `SqlitePersistenceLifecycle` emits *"Database is on removable storage (/dev/mmcblk0p2).
  SD card storage is not recommended for production use — database corruption and
  performance degradation are common"* on each start; `df` confirms `/dev/mmcblk0p2`,
  117 G, 12 % used. Pre-existing and out of B3's scope — raised only because the captured
  event stream **is** the bench's moat, and this is the one risk that could take all of it
  at once. The hub should confirm it is registered, not necessarily act.

## 8. What is proven on real hardware now

DP-1 `suite auto` — 9 legs from the constants key, park last, zero OPERATOR · DP-2 the
wrapper chain end to end under the scheduler · DP-3 both quiesce reads positive with HTTP
codes and full bodies, plus independent app-side `automations=N` corroboration on all
three boots, every bundle sourced from the quiesced boot, and a clean drift guard
(`IDENTICAL`, so tonight's swap proceeds) · DP-4 one digest line in the ruled grammar
including the SKIP arm · DP-5 the REC scheduler firing correctly on an explicit foreign
timezone · DP-6 a real DISPATCHED→CONFIRMED latency mined from a real bundle, arithmetic
verified, written to both sinks · DP-7's landing intact · R5 `api_token` dispatched and
proven on the wire (HTTP 200 through the verb — the same auth path the nightly uses,
closing the token-source question this lane raised at 09:03). The honest SKIP fired on
its documented cause (`HUE-RESET pending`) — the SKIP-honest floor §9 predicted verbatim.

**Everything between this and a working nightly was two seconds, and the fix is applied.**

## 9. Recommended amendments (drafted; the hub's word to adopt)

1. **INSTALL-6 red procedure** — replace `journalctl --user -u nexsys-bench-nightly.service
   --since yesterday` with `journalctl --user-unit nexsys-bench-nightly.service --since
   yesterday`, and name `~/hs-bench/nightly-logs/nightly-<date>.log` as the **first**
   fallback: it exists, it is the wrapper's own voice, and per G-3 the journal's real
   horizon is ~7 days (zero across a reboot). Adding *"the journal may have rotated; the
   log file has not"* to the red path would save a future operator the wrong conclusion.
2. **A standing morning gate for week 1** — `pgrep`-based, not `status`-based (F-1):
   *a dead bench with a green digest is the B3 night-1 defect recurring.*
3. **Timestamp and line-buffer the wrapper's own output** (G-1) — this alone would have
   collapsed today's three-capture forensic into one read.
4. **A wrapper closing line** — `nightly.sh` ends at the digest with no terminal line.
   One line naming the exit path (normal / trap-EXIT / trap-TERM) and the exit code.
5. **An anti-vacuous drift line** — the branch-B drift check succeeds silently
   (`quiesce swap done` merely implies it passed). Per the vacuous-verify pairing rule it
   should emit its own positive INFO: `[OK] drift check: live == live-basis`.
6. **Filter or drop the bundle journal-slice** (G-2), and widen `app-log-slice` (G-4).
7. **The digest example line** — the selftest's `ON-latency 0.11s` is synthetic and now
   invites a false 33× regression reading against real data.
8. **Fold the `KillMode=process` drop-in in-repo** beside the unit, once tomorrow's gate
   confirms it, so a fresh install inherits the fix.
9. **`context/audits/2026-07-31_B3_return.md`** — mark **SUPERSEDED / P-BLOCK CONSUMED**
   so no future session re-runs §2 and re-mints over `7c8efbb`.

## 10. This lane's deviations

- **[INFO] D-1** — §2 was re-run as one capture, markers preserved, extras fenced. It was
  already spent; the re-run's value was the red, not the pins. Filed as corroboration,
  never as a mint.
- **[INFO] D-2** — a FALSE label shipped in capture #1 (`P-1 FALLBACK (fired: the
  bench-hero grep named no file)` when the grep *did* name `homesynapse.yaml`). Cause: the
  guard tested exit status, which was 2 because `config/` holds two subdirectories, not
  because the match set was empty. Raw output above the label is correct and is the
  record. Fix: test empty stdout, never non-zero exit.
- **[INFO] D-3** — `[P-1 PREMISE] HEALTHY` rests on the same weak test (`grep -q` returns
  2 on error), so the healthy arm could print without having looked. The conclusion
  survives on independent evidence (the bench-hero block's two entity refs are visibly not
  the S31), not on the label.
- **[INFO] D-4** — capture #1 carried a premise inherited from the stale return doc
  ("expected PRE-B3: `api_token` not dispatched"). The Pi is POST-B3. Left standing in the
  transcript rather than quietly amended.
- **[INFO] D-5** — F-3a: a `head -5` on a directory listing produced a phantom absence.
- **[INFO] D-6** — the G-2 prediction was **half wrong and disclosed as such**: this lane
  predicted the bundle journal-slice would be *empty*. It is not empty; it is one
  unrelated line. The finding is untargeted-noise, not vacuous-empty, and the distinction
  matters because noise is the more dangerous of the two.
- **[INFO] D-7** — all writes confined to `/tmp` plus two deliberate acts in their own
  blocks: `bench.sh start` at 09:27 (after the read-only forensics completed) and the
  `KillMode` drop-in under `~/.config/systemd/user/`. `~/nexsys-bench` porcelain read clean
  throughout; no repo file in either repo was touched.
- **[INFO] D-8** — every capture was fixture-run before shipping: capture #1 against three
  scratch fixtures exercising both boundaries of each verdict arm with a planted sentinel
  token proving zero leakage; capture #2 against a mock of the Pi's layout; the drop-in
  write and its undo path rehearsed in a scratch HOME before Nick ran them.

## 11. Open reads

- **Tomorrow 04:30+ (the gate):** does the bench survive its own nightly? `pgrep` first,
  then the digest, `Result`, and the journal via `--user-unit`. Watch for `Found
  left-over process … in control group` — expected and benign under `KillMode=process`.
  An ON-latency above 5.369 s would be the margin watch, never a retry.
- **The one open hop (ACTION-5, four lines):** is a syslog daemon running? If yes,
  `/var/log/syslog` is already a durable logrotate-managed copy of the wrapper's output
  and G-3's durability concern is moot; if no, `ForwardToSyslog=yes` is a no-op and
  `nightly-<date>.log` stands alone. **Nothing should be changed about journald until
  this read lands.**
- **Hub-side, core:** does any writer ever populate `automationName` (OBS-A)?
- **CLOSED today:** G-3's root cause (vendor drop-in `Storage=volatile`; no
  `user-*.journal` exists), F-3b's mechanism, and the H1 mechanism itself.

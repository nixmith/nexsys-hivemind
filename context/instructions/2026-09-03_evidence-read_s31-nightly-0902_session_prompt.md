<!--
file: context/instructions/2026-09-03_evidence-read_s31-nightly-0902_session_prompt.md
purpose: A READ-ONLY EVIDENCE-READ SESSION (Claude Code on Nick's desk, which can ssh to the bench card) — the 2026-09-02 nightly's `command-confirm-s31` FAIL (the floor fell 8/9 → 7/9 after four PASS nights) is adjudicated at its bundle BEFORE anyone theorizes (arc-discipline 28: per-hypothesis predictions filed here, before the read; the playbook §1 addendum: derive WHICH suite/code ran from the bundle stamp first). The session reads, extracts verbatim, compares with the 2026-08-02 bundle of the same class, and files ONE return. It changes nothing on the card.
audience: the evidence-read session (fresh context; everything it needs is in this file or at the paths it names) · the hub (audits the return) · Nick (launches it with the one-paste line at the foot)
state-type: session prompt (the operator-packet class — self-contained)
status: DISPATCH-READY — authored at v61 beat 10 (2026-09-03 ~06:30 CT). Return path: nexsys-hivemind/context/audits/2026-09-03_s31-nightly-0902_evidence-read_return.md (≤ 8 KB; §0 first).
-->

# Evidence read — the 2026-09-02 nightly `command-confirm-s31` FAIL (read-only)

## §0 The fence — read this twice
You are on Nick's desk. Every command against the Pi runs as `ssh pi '<command>'` and **reads**. You never run `systemctl`, `bench.sh`, `kill`, `reboot`, `apt`, an editor, `>`/`>>`, `tee`, `rm`, `mv`, `cp`, `chmod` or any scenario on the card; you never re-run the suite; you never touch `~/hs-bench/` or `~/nexsys-bench/` except to read. **s31 and the nightly are HANDS-OFF until R-5 by standing fence** — reading them is lawful, changing them is not. You commit nothing in any repo. You file exactly ONE return (the path in the header). If any command you are about to run is not one of `ls`, `cat`, `head`, `tail`, `grep`, `wc`, `stat`, `find`, `date`, `hostname`, `python3 -m json.tool`, `journalctl --no-pager` (read), stop and write that down instead of running it.

**The time law.** The Pi's displayed wall clock runs +1 h vs Central; **Z-stamped values govern every timing statement** (the bundle names are Z-stamped; the nightly fires ~08:32Z = ~03:32 CT). Never convert in your head — quote the Z stamps and compute deltas explicitly.

## §1 What is known before you read (do not re-derive; verify)
- `~/hs-bench/digests/nightly.log` on the bench card (`hs-dev-1`) ends: `2026-08-29 … 8/9 PASS · ON-latency 0.50s` · `08-30 8/9 PASS · 3.29s` · `08-31 8/9 PASS · 3.52s` · `09-01 8/9 PASS · 0.10s` · **`2026-09-02 quiesced AUTO floor: 7/9 · FAIL command-confirm-s31 · bundle /home/homesynapse/hs-bench/bundles/command-confirm-s31-20260902T083122Z · 1 SKIP(hue-online) · bench-hero RESTORED ✓ · ON-latency n/a(FAIL)`**. There is no 2026-09-03 line: the bench card was out of the Pi overnight 09-02→09-03 (the held card ran O-2), so the 09-03 nightly did not fire. Confirm both facts (§3 step 1).
- The same class failed once before: 2026-08-02, bundle `command-confirm-s31-20260802T083057Z`, verdict `FAIL — terminal phase mismatch: expected CONFIRMED, read CONFIRMATION_TIMED_OUT`; lifecycle ACCEPTED → DISPATCHED → CONFIRMATION_TIMED_OUT in 5.136 s; the app alive throughout; the device present again a minute later. The adjudication of record: `nexsys-hivemind/context/audits/2026-08-02_B3_night2_command-confirm-s31_evidence-read.md` — **read it first**; your return uses its §1 shape (pinned extracts, hub-verifiable).
- The bundle of this class holds 7 files: `api-captures.json` · `journal-slice.txt` · `MANIFEST.txt` · `quiesce-evidence.txt` · `resolved.json` · `scenario.yaml` · `verdict.txt` (plus, if the G-4 widening landed since, `app-log-slice.log`). `verdict.txt` names the bench log of the run (`/home/homesynapse/hs-bench/bench-<date>-<hhmmss>.log`).
- The bench runs the certified deployed build; nothing was deployed to it between 09-01 and 09-02. The 09-02 run fired at ~08:31Z on 09-02, ~19 hours BEFORE the O-2 card swap (03:10Z on 09-03) — the swap is not a candidate cause.

## §2 The hypotheses — predictions filed BEFORE the read (arc-discipline 28)
| # | Hypothesis | What the bundle shows if TRUE | What refutes it |
|---|---|---|---|
| H-A | **The device never answered** (radio silence / the acked-then-silent class): the command left the coordinator, no report came back inside the window | `api-captures.json`: ACCEPTED → DISPATCHED → `CONFIRMATION_TIMED_OUT` ≈ 5 s later, `terminal: true`; no `state_reported`/confirm for the hero entity in the window; `quiesce-evidence.txt` shows the hero PRESENT again at restore (so reachable a minute later) | a DISPATCHED that never happened (→ H-B), or a report inside the window (→ H-C) |
| H-B | **The command was never dispatched** (engine / ledger / integration side) | ACCEPTED without DISPATCHED, or DISPATCHED absent and a `rejected`/failure outcome; the bench log or journal shows the dispatch error | DISPATCHED present with a plausible integration id |
| H-C | **The confirmation arrived late** — after the scenario's window but within the device's lawful envelope | a report/confirm for the hero AFTER the `CONFIRMATION_TIMED_OUT` stamp (tens of seconds), in `api-captures.json`, the bench log or an app-log slice | no later report anywhere in the captured window |
| H-D | **Infrastructure collateral** — a serial/NCP/USB event, a watchdog reopen or a process restart inside the run window | `journal-slice.txt` or `journalctl` for 08:25Z–08:40Z carries a USB/tty/kernel line, a reopen, or a service (re)start near the command stamps | a journal slice of tailscale-only noise (the 08-02 exhibit) |
| H-E | **The 08-02 class repeats unchanged** — same verdict text, same ≈5 s window, same aliveness — i.e. an intermittent already adjudicated once | `verdict.txt` byte-similar to the 08-02 one; the lifecycle arithmetic within ±0.5 s of 5.136 s | a different verdict text, a different terminal phase, or a different window |

Write which hypotheses the evidence SUPPORTS, which it REFUTES, and which it leaves OPEN — and name the ONE next observation that would separate any two survivors. Do not propose a fix: the fence stands until R-5; a candidate row for the R-5 charter is the most you name.

## §3 The read — every block self-contained; run in order; paste every output into the return verbatim (trim only repeated noise, and say so)
```bash
# 1 — where you are, and the two known facts
ssh pi '/usr/bin/hostname; /usr/bin/date -u; /usr/bin/tail -n 3 /home/homesynapse/hs-bench/digests/nightly.log; /usr/bin/ls -la /home/homesynapse/hs-bench/bundles/ | /usr/bin/tail -n 6'
```
Expected: `hs-dev-1`; the last digest line is 2026-09-02; the newest bundle is `command-confirm-s31-20260902T083122Z`; no `20260903` bundle exists. ⏺ RECORD.
```bash
# 2 — the bundle: manifest, verdict, the scenario as run (which code/suite ran — the stamp law, first)
ssh pi 'B=/home/homesynapse/hs-bench/bundles/command-confirm-s31-20260902T083122Z; /usr/bin/ls -la "$B"; echo ===MANIFEST; /usr/bin/cat "$B/MANIFEST.txt"; echo ===VERDICT; /usr/bin/cat "$B/verdict.txt"; echo ===RESOLVED; /usr/bin/cat "$B/resolved.json"; echo ===SCENARIO-STAT; /usr/bin/stat -c "%y %n" "$B/scenario.yaml"'
```
⏺ RECORD the file list (count = 7 or 8), the verdict line verbatim, the bench-log path named in it, and every constant in `resolved.json` that names the s31 entity/ieee/order.
```bash
# 3 — the lifecycle (the discriminator for H-A / H-B / H-C): every capture, then the stamps
ssh pi 'B=/home/homesynapse/hs-bench/bundles/command-confirm-s31-20260902T083122Z; /usr/bin/python3 -m json.tool "$B/api-captures.json" | /usr/bin/head -n 400'
ssh pi 'B=/home/homesynapse/hs-bench/bundles/command-confirm-s31-20260902T083122Z; /usr/bin/grep -o "\"phase\": *\"[A-Z_]*\"\|\"outcome\": *\"[a-z_]*\"\|\"at\": *\"[0-9T:.Z-]*\"\|\"timestamp\": *\"[0-9T:.Z-]*\"\|\"terminal\": *[a-z]*" "$B/api-captures.json" | /usr/bin/head -n 80'
```
If the key names differ from the 08-02 exhibit (`phase`, `at`, `terminal`), say so and adapt the grep to what step 3's first command showed — the extraction pattern must be exercised against the real file before you trust a count (playbook D-4). ⏺ RECORD ACCEPTED / DISPATCHED / terminal stamps verbatim and compute the window in seconds, shown as arithmetic.
```bash
# 4 — aliveness + collateral (H-D): the quiesce/restore reads and the journal slice, then the system journal for the run window
ssh pi 'B=/home/homesynapse/hs-bench/bundles/command-confirm-s31-20260902T083122Z; echo ===QUIESCE; /usr/bin/cat "$B/quiesce-evidence.txt"; echo ===JOURNAL-SLICE; /usr/bin/cat "$B/journal-slice.txt" | /usr/bin/head -n 120; echo ===APP-LOG-SLICE; /usr/bin/ls -la "$B"/app-log-slice.log 2>/dev/null || echo ABSENT'
ssh pi '/usr/bin/journalctl --no-pager -S "2026-09-02 08:25:00 UTC" -U "2026-09-02 08:40:00 UTC" | /usr/bin/grep -i -v "tailscale\|magicsock" | /usr/bin/head -n 120'
```
⏺ RECORD: did both quiesce reads answer (HTTP codes); any usb/tty/serial/kernel/reopen/restart line in the window (quote it), or "none beyond tailscale noise".
```bash
# 5 — the bench log named in verdict.txt (fill the path from step 2 — DO NOT run this line until you have replaced the placeholder)
ssh pi '/usr/bin/grep -n -i "s31\|command-confirm\|CONFIRM\|DISPATCH\|ACCEPTED\|timed_out\|FAIL\|restore\|hero" /home/homesynapse/hs-bench/bench-2026-09-02-<hhmmss>.log | /usr/bin/head -n 120'
```
⏺ RECORD the run's own timeline lines; compare their stamps to step 3's (the Pi wall-clock lines are +1 h vs CT — quote, do not convert).
```bash
# 6 — the class comparison (H-E): the 08-02 bundle, if still on disk
ssh pi 'B=/home/homesynapse/hs-bench/bundles/command-confirm-s31-20260802T083057Z; /usr/bin/ls -la "$B" 2>/dev/null && /usr/bin/cat "$B/verdict.txt" || echo "08-02 bundle ABSENT"'
```
⏺ RECORD the two verdict lines side by side and the two windows.

## §4 The return — `nexsys-hivemind/context/audits/2026-09-03_s31-nightly-0902_evidence-read_return.md` (≤ 8 KB)
Frontmatter (file · purpose · instrument = this desk over `ssh pi`, read-only · the CT filing date from `date -u`). Then: **§0 verdict-first** — one paragraph: which hypotheses the evidence supports / refutes / leaves open, the lifecycle window as arithmetic, whether the 08-02 class repeated, and the ONE next discriminating observation. **§1 the pinned extracts** in the 08-02 audit's shape (bundle · lifecycle · verdict · quiesce · journal · resolved · bench log), every stamp verbatim. **§2 the two confirmed facts** (the 09-03 nightly MISSED — no bundle, no digest line; the bench card back and answering). **§3 instrument limits** (what you could not read; any grep you had to adapt, with the before/after pattern). **§4 the fence attestation**: "nothing written on the card; no process, unit, scenario or file touched; no commit in any repo" — and the exact list of commands you ran. No fix proposals; at most one line "candidate row for the R-5 charter: …".

When the return is on disk, stop. Do not summarize in chat beyond one line pointing at the file.

---
**Nick's one-paste launch line (Claude Code, from `~/Desktop/Code/ClaudeFolder`):**
> Execute `nexsys-hivemind/context/instructions/2026-09-03_evidence-read_s31-nightly-0902_session_prompt.md`. READ-ONLY on the bench card (`ssh pi`) — write NOTHING on the Pi, run no scenario, no systemctl, no restarts. Commit NOTHING. File the return at `nexsys-hivemind/context/audits/2026-09-03_s31-nightly-0902_evidence-read_return.md`.

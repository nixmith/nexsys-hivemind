<!--
file: context/handoff/2026-08-07_killmode-apply_operator-packet.md
purpose: KILLMODE-APPLY — the K:(a) residual, re-scoped at source (v48 beat 1): apply the ALREADY-COMMITTED unit-file KillMode fold into systemd's user config on the Pi, then retire the Pi-local drop-in. Self-contained per the operator-packet law (arc-discipline 35). Playbook §8-compliant incl. the new addenda (5)–(10).
audience: Nick (operator, Pi + desktop)
status: ISSUED 2026-08-07 (v48 beat 1). Execute at leisure — every night is safe meanwhile (the drop-in keeps enforcing KillMode=process until retired).
-->

# KILLMODE-APPLY — Pi-side unit application + drop-in retirement

**GOAL:** make the in-repo `KillMode=process` the setting systemd actually loads (today the live setting is guaranteed only by the Pi-local drop-in), then retire the drop-in — so nothing survival-critical lives outside the repo and a fresh install cannot resurrect the cgroup-kill defect.

**DONE-WHEN:** `systemctl --user cat nexsys-bench-nightly.service | grep -c "^# /"` prints **1** (the installed unit file is the ONLY source — no `.d/killmode.conf` line) AND `systemctl --user show nexsys-bench-nightly.service -p KillMode` prints `KillMode=process` — both AFTER a daemon-reload with the drop-in directory gone.

**PREMISE-PROVENANCE (§8 addendum (5) — what is already true vs what this run adds):** ALREADY: `KillMode=process` is committed in-repo since bench `41a7a3c` (B3.1 A-8, with the Aug-2 mechanism proof as an in-file comment) and is present in the Pi checkout at `16e672d`; the drop-in (`~/.config/systemd/user/nexsys-bench-nightly.service.d/killmode.conf`, applied 2026-08-01) has enforced the same setting live every night since; the survival gate held again this morning (pid 91594 remains-running · `Result=success`). THIS RUN ADDS: copying the committed unit into systemd's user config (a pulled unit-file change does NOT apply until re-copied + `daemon-reload` — the unit's own REFRESH note) and retiring the drop-in. No repo edit, no bench commit, no deploy — this is a Pi-config act only.

**ANTI-ACTIONS:** do NOT edit the unit in place on the Pi; do NOT touch `nexsys-bench-nightly.timer`; do NOT run any bench.sh verb; NOTHING touches the S31 or the Hue lamp.

**Instrument resolution:** every read below is immediate (config reads). The production re-proof needs no act: the next 04:30 fire's journal line `Unit process <pid> (java) remains running after unit stopped` + the digest at the bar IS the survival gate under the unit-file-only config — the Aug-8 morning glance covers it.

---

**Block 0 — the HEAD gate (read-only):**
```
# Pi terminal (ssh pi)
cd /home/homesynapse/nexsys-bench && git log --oneline -1
```
Expected: exactly `16e672d bench: B3.3 - ...`. ⏺ RECORD the line.

**Block 0-STOP (its own block — answer before proceeding):**
```
# If the HEAD above is NOT 16e672d: STOP. Paste the line back to the hub. Run nothing further.
```

**Block 1 — the before-state read (read-only; paste either way):**
```
# Pi terminal
grep -n "^KillMode" ~/.config/systemd/user/nexsys-bench-nightly.service
ls -la ~/.config/systemd/user/nexsys-bench-nightly.service.d/
```
Expected: the first command prints either `45:KillMode=process` (installed copy already current) or NOTHING (installed copy pre-dates B3.1 — the interesting before-state; either is fine, Block 2 overwrites); the second lists `killmode.conf`. ⏺ RECORD both outputs.

**Block 2 — apply the committed unit:**
```
# Pi terminal
cp /home/homesynapse/nexsys-bench/tools/scheduler/nexsys-bench-nightly.service ~/.config/systemd/user/nexsys-bench-nightly.service
systemctl --user daemon-reload
```

**Block 3 — verify the applied bytes + effective setting (read-only):**
```
# Pi terminal
grep -c "^KillMode=process" ~/.config/systemd/user/nexsys-bench-nightly.service
systemctl --user show nexsys-bench-nightly.service -p KillMode,Type
```
Expected: exactly `1` · then `KillMode=process` and `Type=oneshot`. ⏺ RECORD.

**Block 3-STOP (its own block):**
```
# If EITHER read differs: STOP. Paste both outputs to the hub. Do NOT remove the drop-in —
# it stays the live guarantee until this verifies.
```

**Block 4 — retire the drop-in:**
```
# Pi terminal
rm -rf ~/.config/systemd/user/nexsys-bench-nightly.service.d
systemctl --user daemon-reload
```

**Block 5 — the decisive read (read-only; paste either way):**
```
# Pi terminal
systemctl --user cat nexsys-bench-nightly.service | grep -n "^# /"
systemctl --user show nexsys-bench-nightly.service -p KillMode
```
Expected: exactly ONE source line — `# /home/homesynapse/.config/systemd/user/nexsys-bench-nightly.service` (zero `.d/` lines) · then `KillMode=process` (now sourced from the unit file alone). ⏺ RECORD both. This pair is the DONE-WHEN.

**Block 6 — desktop repo — the law-15 remote-commit identification (read-only; separate machine):**
```
# desktop repo (MINGW64) — homesynapse-core
cd ~/Desktop/Code/ClaudeFolder/homesynapse-core
git fetch origin && git log --oneline HEAD..origin/main
```
Expected: EMPTY output after the fetch (local `3723e31` == origin/main). Any lines = remote-arrived commits from the GitHub vulnerability resolution — ⏺ RECORD and paste to the hub for identification AT THE OBJECT before any pull. Do NOT pull either way.

**Abort ladder:** nothing here is time-critical. If anything surprises after Block 4, the unit file already carries the setting (Block 3 proved it) — worst case re-run Block 2 and paste everything to the hub. The nightly stays safe on every branch.

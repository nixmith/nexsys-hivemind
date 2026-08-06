<!--
file: context/handoff/2026-08-06_H3_pi-trip_operator-package.md
purpose: The H3 attended Pi trip (Aug-8/9) — the S-5a+S-5c deploy + deployed-jar verify, the fix-verification rep, the Hue re-power (DIRECT OUTLET only → 9/9 becomes the bar), the killmode.conf disposition, and the two completeness reads (settle-terminal Aug-4/Aug-5 + the S-4 residual log-grep). Playbook §8 form.
audience: Nick (operator, attended, on the Pi + desktop)
status: ISSUED — authored v47 hub beat 1 (2026-08-06; the v47 prompt's author-first charge)
return-to: paste-package back to the hub chat; it intakes as a v47 hub beat. Findings file to context/audits/.
-->

# H3 — THE PI TRIP (Aug-8/9, attended) — deploy S-5a+S-5c · fix-verification rep · Hue re-power · two reads

**GOAL:** the running app leaves this trip on core `3723e31` with `sqlite-jdbc-3.51.3.0` PROVEN on the running classpath; one attended suite rep verifies the s31 fix on the NEW build; the Hue re-powers (direct outlet) so **9/9 becomes the nightly bar**; two low-stakes completeness reads come home.

**DONE-WHEN:** (1) `git log` on the Pi shows `3723e31` · (2) the post-restart classpath read shows `sqlite-jdbc-3.51.3.0.jar` and ZERO `3.51.2.0` · (3) `boot-health` `[PASS] 6/6` · (4) the attended suite rep reads **9/9 PASS · 0 SKIP** (s31 position 8, `2/2 positive`, park re-set LAST, ON-latency present) · (5) the two reads pasted · (6) the return package filed back to the hub.

**GLOBAL ANTI-ACTIONS (the whole trip):** HANDS OFF `scenarios/constants.yaml` and every bench scenario — the bench is QUIET; nothing edits `~/nexsys-bench` on the Pi. NO reboot of the Pi unless ruled. The Hue re-power is ONE power-up at a DIRECT WALL OUTLET — never a smart relay/strip, never the 6× cycle (that is a factory reset). Do NOT run the trip until the morning digest for that day has been glanced routine (Block 1 checks it).

**Timing:** ~30 min of blocks + one Gradle build (minutes; npm is cached-warm) + a mandatory ≥10 min Hue availability wait (Blocks 6–7 fill it). All bench operations via the full path `~/nexsys-bench/tools/bench.sh` (never bare `bench.sh`).

---

## Block 0 of 9 — STOP-GATE: the one ruling before the trip (answer in chat, not on the Pi)

**K — the killmode.conf drop-in disposition.** The night-1 fix lives ONLY in the Pi-local drop-in `~/.config/systemd/user/nexsys-bench-nightly.service.d/killmode.conf`; the repo's committed `tools/scheduler/nexsys-bench-nightly.service` is byte-untouched, so a fresh install would resurrect the cgroup-kill defect.
- **(a) REC — fold in-repo, keep the drop-in for now:** the hub authors the four-line unit-file fold as a ruled bench micro-WU AFTER the trip (desk edit → audit → commit → a later Pi pull); the Pi drop-in stays in place this trip (belt-and-suspenders; removal only after the folded unit is deployed and verified).
- **(b) keep the drop-in only** (no repo edit; the fix stays Pi-local and install-fragile).

⏺ RECORD: one word — "K: (a)" or "K: (b)". Nothing on the Pi changes either way this trip; Block 5 is read-only.

---

## Block 1 of 9 — pre-deploy baseline (STOP-gate: the morning digest)

```
# Pi terminal (read-only)
# GOAL: prove the night before the trip was routine, and pin the revert SHA.
# DONE-WHEN: digest line(s) glanced 8/9; one SHA recorded.
~/nexsys-bench/tools/bench.sh digest 3
cd ~/homesynapse-core && git log --oneline -1
ls ~/homesynapse-core/app/homesynapse-app/build/install/homesynapse-app/lib/ | grep sqlite
```

**Expect:** the newest digest line(s) read `8/9 PASS · 1 SKIP(hue-online)` (the standing bar); the sqlite line reads exactly `sqlite-jdbc-3.51.2.0.jar` (the pre-deploy truth). ⏺ RECORD all output either way — **the `git log` SHA is the REVERT SHA; write it down before Block 2** (⚠ fill it into the abort ladder if needed). A divergent digest (anything other than 8/9 with the hue SKIP) ⇒ STOP, paste, the trip waits on hub adjudication — a divergence is an intake, not a crisis.

---

## Block 2 of 9 — the deploy pull + build

```
# Pi terminal
# GOAL: bring core to 3723e31 and rebuild the installDist image.
# DONE-WHEN: BUILD SUCCESSFUL; the new jar is in lib/.
cd ~/homesynapse-core
git pull
git log --oneline -3
./gradlew --no-daemon :app:homesynapse-app:installDist
ls ~/homesynapse-core/app/homesynapse-app/build/install/homesynapse-app/lib/ | grep sqlite
```

**Expect, in order:** fast-forward ending at `3723e31`; the log shows `3723e31` (Merge … brace-expansion-5.0.9) atop `96d9efb` (S-5c) atop `b3d31b8` (S-5a); `BUILD SUCCESSFUL` (minutes lawful — npm is cached-warm; a quiet console is not a hang); the final grep reads exactly `sqlite-jdbc-3.51.3.0.jar` with ZERO `3.51.2.0` line. ⏺ RECORD the pull tail + `BUILD SUCCESSFUL in …` + the grep. Build failure ⇒ paste verbatim, then the abort ladder (bottom).

---

## Block 3 of 9 — restart + boot glance + THE DEPLOYED-JAR VERIFY

```
# Pi terminal
# GOAL: the new build LIVE, boot lawful, 3.51.3.0 on the RUNNING classpath.
# DONE-WHEN: HEALTHY; the ps read shows 3.51.3.0 and zero 3.51.2.0.
~/nexsys-bench/tools/bench.sh restart
~/nexsys-bench/tools/bench.sh health
ps -ww -fp $(pgrep -f "[c]om.homesynapse.app.Main") | tr ':' '\n' | grep -c "sqlite-jdbc-3.51.3.0.jar"
ps -ww -fp $(pgrep -f "[c]om.homesynapse.app.Main") | tr ':' '\n' | grep -c "sqlite-jdbc-3.51.2.0.jar"
```

**Expect:** restart self-reports HEALTHY; the health glance carries `device_relinked` ×6 · `adoption_maps_rehydrated: devices=6` · `registry.projection_live: devices=6 entities=6` · `network_resumed: channel=20 panId=0x774c` · ZERO `device_proposed`; then the two counts read **`1` then `0`** — that pair IS the deployed-jar verify (S-5a is now a DEPLOYED fix, not desk-green; the WAL-exposure window on this hub closes here). ⏺ RECORD the glance + both count lines either way. Counts any other way ⇒ STOP + paste (do not proceed to the rep on an unproven classpath).

---

## Block 4 of 9 — boot-health (the deploy-proof floor)

```
# Pi terminal
# GOAL: the deploy-proof scenario floor on the new build.
# DONE-WHEN: one PASS line.
~/nexsys-bench/tools/bench.sh scenario boot-health
```

**Expect:** `[PASS] boot-health — 6/6 positive · 0 forbidden`. ⏺ RECORD verdict + bundle id. `[FAIL]` ⇒ paste + abort ladder.

---

## Block 5 of 9 — killmode.conf: the read-only verify (no change either K-branch)

```
# Pi terminal (read-only)
# GOAL: pin the drop-in's exact bytes + the live unit properties on the record.
# DONE-WHEN: both outputs printed.
cat ~/.config/systemd/user/nexsys-bench-nightly.service.d/killmode.conf
systemctl --user show nexsys-bench-nightly.service | grep -E "^KillMode=|^Type="
```

**Expect:** the drop-in's few lines including `KillMode=process`; the show lines read `KillMode=process` and `Type=oneshot`. ⏺ RECORD both either way. Any other KillMode ⇒ paste + STOP (the survival fix is not live; the hub adjudicates before the next unattended night).

---

## Block 6 of 9 — THE HUE RE-POWER (physical act) — then the wait begins

Physical act, ONE line: **plug the Hue lamp into a DIRECT WALL OUTLET and switch it on — ONCE.** (Anti-actions: NOT a smart relay, NOT a power strip with a switch you might later flip, NOT the 6× on/off dance.) Note the wall-clock time of the plug-in.

```
# Pi terminal (read-only; run ~1–2 min after the plug-in)
# GOAL: the Hue's re-announce is in the log (mains router: re-announce, no re-join).
# DONE-WHEN: >=1 fresh Hue line printed.
grep -E "device_announce|device_relinked" ~/hs-bench/current.log | tail -5
```

**Expect:** ≥1 new announce/relink line stamped after your plug-in time (the Hue re-announcing; ZERO `device_proposed` — it is already adopted). ⏺ RECORD the lines + your plug-in clock time. Nothing after 5 min ⇒ paste anyway and continue — Blocks 7–8 do not gate on it, and the 9/9 question is settled at Block 8. **Then: HANDS OFF for ≥10 min** (the availability ping gate) — run Block 7 during the wait.

---

## Block 7 of 9 — the two completeness reads (read-only; fills the Hue wait)

```
# Pi terminal (read-only)
# GOAL: (i) the Aug-4 + Aug-5 settle-terminal reads (completeness only);
#       (ii) the S-4 residual grep — which token preceded the mid-death reopen.
# DONE-WHEN: the bundle listing printed; both settle bundles listed; the grep printed.
ls ~/hs-bench/bundles/ | grep -E "settle-2026080(4|5)"
for d in $(ls -d ~/hs-bench/bundles/*settle-2026080[45]* 2>/dev/null); do echo "== $d"; ls "$d"; grep -ri "terminal" "$d" | tail -10; done
grep -n "port_unhealthy" ~/hs-bench/bench-*.log ~/hs-bench/current.log 2>/dev/null | tail -30
```

**Expect:** two settle bundle entries (Aug-4, Aug-5); their listings + terminal lines print (whatever they say — these are completeness reads, no pass bar); the S-4 grep prints `port_unhealthy` lines whose `cause=` field names the reopen trigger (REV-1's one-grep residual) — an EMPTY grep is also an answer. ⏺ RECORD all output either way; the hub adjudicates, you decide nothing here.

---

## Block 8 of 9 — THE FIX-VERIFICATION REP (after the ≥10 min wait)

```
# Pi terminal
# GOAL: one attended suite rep on the NEW build with the Hue back online.
# DONE-WHEN: one digest-style verdict line.
~/nexsys-bench/tools/bench.sh suite auto
```

**Expect — the new bar:** **`9/9 PASS · 0 SKIP`** · `[PASS] command-confirm-s31 — 2/2 positive · 0 forbidden` with its bundle stamp showing the leg ran EIGHTH · the park (`command-s31-settle`) re-set LAST · ON-latency present (the value joins the C4 distribution — this build's first datum). If hue-online still SKIPs (Hue not yet online at gate time): `8/9 PASS · 1 SKIP` with s31 PASS is a LAWFUL rep — record it, note the Hue timing, and 9/9 adjudicates at the next nightly instead. ⏺ RECORD the full verdict block + bundle stamps either way. **Any s31 FAIL ⇒ paste + STOP — never a retry, never a retune** (the pre-ruled ladder is the hub's, not a trip decision).

---

## Block 9 of 9 — the return package

File ONE fenced paste-package back to the hub chat: the verdict table (Blocks 0–8, one line each) · every ⏺ RECORD verbatim (token-excluded — never paste the api token) · anomalies · the final-state line (**Pi core HEAD SHA · app pid · active log path · the lib/ sqlite jar name · K one-word**) · the route-back line "intakes as the next v47 hub beat." The MODULE_CONTEXT F-14-row fold (the `ZigbeeDeviceCache` row gains "+ writes are temp-then-move, F-3/S-5c") is HUB-OWNED — it rides a hub-ordered core commit after this trip; nothing for you here.

---

## Abort ladder (build/boot failures only — Blocks 2–3)

```
# Pi terminal — ⚠ FILL IN <REVERT_SHA> from Block 1's recorded git log line before running
cd ~/homesynapse-core
git reset --hard <REVERT_SHA>
./gradlew --no-daemon :app:homesynapse-app:installDist
~/nexsys-bench/tools/bench.sh restart
~/nexsys-bench/tools/bench.sh scenario boot-health
```

**Expect:** the pre-trip `[PASS]` floor on the old build (and the old `3.51.2.0` jar back in lib/ — the known-good state). ⏺ RECORD that the revert ran + its verdict. Block 4–8 failures never trigger the ladder — they are FINDINGS on whatever deploy state Block 3 proved.

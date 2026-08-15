<!--
file: context/handoff/2026-08-14_freeze-day_operator-block.md
purpose: THE FREEZE-DAY OPERATOR BLOCK (Fri 2026-08-14) — one Pi session covering: §1 the G1 chain-render pre-flight (the FE-fix deploy-state check, with its TODAY-ONLY contingency), §2 the I2 pre-freeze re-sweep (grep evidence, commands cited — the MUST row's gate-day form; E3 discharges on this paste), §3 the flake-distribution pull (the READ input), §4 the Rosonway restore + enumeration verify (D-3 re-stamped: before Sat 03:30 CT). Every ⏺ pastes back to the hub whole; the hub files the I2/E3 close-out block on the paste.
audience: Nick (operator; ~25–40 min total, any time today — §4 before bed).
laws: §8 contract — one act per line, expected tokens named, paste-either-way (⏺ RECORD). L3: no token/key material ever enters a paste — the sweeps below PROVE ABSENCE; if any grep unexpectedly prints something key-like, paste the LINE COUNT and the first 8 characters only, never the line. Scope: findings-never-fixes; a failed glance is a ⏺, not a debug session. The §1 contingency is the ONLY sanctioned deploy act, and only TODAY (the freeze is EOD).
-->

# Freeze-Day Operator Block (Fri Aug-14)

## §1 — G1 pre-flight: does the chain render? (~5 min; FIRST, because its contingency must run today or never)

On Windows (leave running): `ssh -N -L 7070:127.0.0.1:7070 pi` → browser `http://localhost:7070/` → token per the runbook's setup (⚠ L3). Then: Runs surface → open ONE historical run (any bench-hero night) → open its causal chain.

**Expect:** the chain renders end-to-end (tiles + verdicts; no blank card, no spinner that never resolves). **⏺ RECORD: "chain rendered" + which run — or exactly what appeared instead.**

**If it renders → §1 done; skip the contingency; the demo's client is proven deployed.**

**CONTINGENCY (ONLY if the chain card crashes/blanks — the pre-fix null-crash signature): the warm rebuild+restart runs TODAY.** On the Pi, one line at a time:

```
cd /home/homesynapse/homesynapse-core
git log --oneline -1
```

**⏺ RECORD that SHA line — it is the revert target if the build fails.** Then:

```
git pull
git log --oneline -1
./gradlew --no-daemon :app:homesynapse-app:installDist
```

**Expect:** pull fast-forwards; HEAD reads `d26777c` (core: lifecycle MODULE_CONTEXT fold); the build is npm-warm (minutes, not the first-run 20). **⏺ RECORD the post-pull SHA + the `BUILD SUCCESSFUL in …` line.** Then:

```
/home/homesynapse/bench.sh restart
/home/homesynapse/bench.sh scenario boot-health
```

**Expect:** the lawful boot glance + `[PASS] boot-health — 6/6 positive · 0 forbidden`. **⏺ RECORD both.** Re-run the browser chain check → **⏺ RECORD.**
**Abort ladder (build or boot fails):** paste the failure verbatim FIRST, then:

```
git reset --hard PREPULL_SHA
```

⚠ **FILL-IN BEFORE RUNNING: replace `PREPULL_SHA` with the exact SHA you ⏺-recorded at this section's first step** — then rebuild + restart + boot-health exactly as above; expect the pre-contingency `[PASS]` floor; ⏺ RECORD. A reverted Pi still runs the READ (the demo falls back to the runbook's honest-failure narration on the old client — a finding, not a blocker).

## §2 — I2: the pre-freeze key-hygiene re-sweep (~5 min; commands are the evidence — paste ALL output verbatim)

```
ls -la /home/homesynapse/hs-bench/data/zigbee/
```

**Expect:** `zigbee-network.json` · `secrets.enc` · `scope_keys.json` · `zigbee-devices.json` (a `.root-key` and/or a retired params file may also appear) — presence only; **never cat any of them.** ⏺ RECORD the listing.

```
file /home/homesynapse/hs-bench/data/zigbee/secrets.enc
```

**Expect:** `data` (opaque/encrypted), NOT ASCII/JSON text. ⏺ RECORD.

```
grep -ciE "network[_-]?key|networkkey" /home/homesynapse/hs-bench/digests/nightly.log
grep -ciE "seed" /home/homesynapse/hs-bench/digests/nightly.log
```

**Expect:** `0` on the first; the second's count with any hits being benign words (paste counts; if the seed count is nonzero, also paste `grep -inE "seed" /home/homesynapse/hs-bench/digests/nightly.log | head -5` — expected class: prose like "generated seed," never hex material). ⏺ RECORD.

```
systemctl --user status homesynapse 2>&1 | tail -25
```

**Expect:** the healthy unit tail; visually confirm NO key/seed hex in the window. ⏺ RECORD the tail (it doubles as the running-state stamp for the close-out). *(If any command errors on permissions, prefix `sudo ` and ⏺ note that it needed sudo — that itself is a least-privilege datum.)*

**On this paste the hub files the I2 close-out block (grep evidence, commands cited) WITH the E3 paragraph riding it — both rows discharge before the freeze.**

## §3 — the flake-distribution pull (~2 min; read-only; the READ input)

```
/usr/bin/tail -n 30 /home/homesynapse/hs-bench/digests/nightly.log
```

**⏺ RECORD whole** (this same paste banks this morning's digest line — the hub annotates it DIRECT-ATTACH topology, see §4).

## §4 — the Rosonway restore (D-3, re-stamped: ANY TIME TODAY before Sat 03:30 CT; ~15 min physical)

Re-cable the coordinator BACK through the Rosonway hub (the documented topology — the pre-Stage-2 arrangement). Then:

```
lsusb
```

**⏺ RECORD the full output.** The positive verification the hub adjudicates: the coordinator enumerates BEHIND the hubs — the Bus 003 Device number back in the twenties. (Last night's 03:30 fire ran direct-attach — that digest banks with the topology annotation; tomorrow's 03:30 fire is the first back-on-documented-topology run, and Sat+Sun digests then feed the READ clean.)

---

**Done-when:** four ⏺ sets pasted here (§1 render-or-contingency · §2 sweep · §3 tail · §4 lsusb). The hub then files the I2/E3 close-out, banks the digest with its annotation, and the freeze proceeds at EOD with every Friday product on disk.

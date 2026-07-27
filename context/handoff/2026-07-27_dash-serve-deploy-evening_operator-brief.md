<!--
file: context/handoff/2026-07-27_dash-serve-deploy-evening_operator-brief.md
purpose: Operator brief for the DASH-SERVE deploy evening — shape (a) split-early (RULED by Nick 2026-07-27, v39 beat 3): Node one-time install → deploy `c09c61c` → THE BROWSER-BLOCK REDUX → **G2 CLOSES on the three ⏺s.** B2's first silicon evening runs SEPARATELY, later.
audience: Nick (operator). May be run directly block-by-block, or via a fresh navigator side-conversation per the v38 precedent (template: context/handoff/archive/2026-07-26_deploy-evening_navigator_session_prompt.md — its §2 interaction protocol + §5 return-package spec apply verbatim; this brief replaces its §1 required read).
status: READY — authored 2026-07-27 (v39 hub, beat 4). Executes ANY evening; no precondition beyond the standing state (all three workflows GREEN on `c09c61c` — banked, Nick-verified).
laws: L2 — every command below is copy-paste-complete; no "practiced X" references. L3 — THE TOKEN NEVER ENTERS A CONVERSATION: it is read on the Pi terminal and typed/pasted into the BROWSER only; every ⏺ paste into the return EXCLUDES the token line. Scope law — a broken glance is a FINDING (⏺ + move on), never a debug session, and never retro-fails earlier blocks. Anti-actions — no constants.yaml edit, no config edits, no cabling/physical changes, no scenario runs mid-build.
-->

# DASH-SERVE Deploy Evening — Operator Brief (target `c09c61c`)

**Goal:** the Pi runs `c09c61c`; the dashboard serves, authenticates, and renders live data; **G2 closes** on the three glance ⏺s.
**Done-when:** Blocks 0–3 `[PASS]` + the three Block-4 glances ⏺-recorded (any verdict) + the Block-5 close verdict + the return package filed back to the hub.
**Standing facts:** the Pi currently runs `2040a66` (six lawful boots banked); fleet 6/6 @ position 25065, ch20/0x774c; all three workflows GREEN on `c09c61c` incl. install-smoke's serve asserts — tonight's only NEW physics are (i) Node on the Pi, (ii) the first npm-bearing build, (iii) the browser.

---

## Block 0 — the floor, BEFORE (5 min)

On the Pi (interactive `ssh pi`, one command per line):

```
~/bench.sh scenario boot-health
```

**Expect:** `[PASS] boot-health — 6/6 positive · 0 forbidden` + a bundle line. **⏺ RECORD the verdict line + bundle.** A `[FAIL]` here = STOP, paste, the evening is off (the hub adjudicates — nothing has changed yet).

## Block 1 — Node 22, one-time install (10–15 min)

Disk headroom first (need ~1.5 GB free for Node + node_modules + the Vite build):

```
df -h / ~
free -h
```

**⏺ RECORD** the root-filesystem Avail figure. Under 2 GB free = STOP and paste before proceeding.

Install Node 22 LTS system-wide (NodeSource — system PATH, so Gradle's `Exec` finds `npm` without shell-profile tricks):

```
curl -fsSL https://deb.nodesource.com/setup_22.x | sudo -E bash -
sudo apt-get install -y nodejs
node --version
npm --version
```

**Expect:** `node` prints `v22.x`, `npm` prints `10.x`. **⏺ RECORD both version lines.** Any failure = STOP + paste (the evening aborts cleanly; nothing deployed).

## Block 2 — pull + the first npm-bearing build (5–20 min — THE ENVELOPE IS RESET)

```
cd ~/homesynapse-core
git pull
git log --oneline -3
./gradlew --no-daemon :app:homesynapse-app:installDist
```

**Expect, in order:** fast-forward `2040a66..c09c61c`; the log shows `c09c61c` (core: DASH-SERVE) atop `2040a66`; then the build — **the 23-second era is OVER for this first run**: `npm ci` downloads ~330 packages, Vite builds the SPA, and the new `:web-ui:dashboard:npmInstall` / `npmBuild` / `stageDashboard` / `jar` tasks appear in the output. **5–20 minutes is LAWFUL; a quiet console during `npm ci` is not a hang.** The jar SELF-ASSERTS the SPA is inside it — if the assert trips, the build FAILS LOUDLY with `dashboard jar is missing dashboard/index.html`. **⏺ RECORD the `BUILD SUCCESSFUL in …` line + the task count + confirmation that the npm tasks appeared.** A build failure = FINDING: paste verbatim, then run the abort ladder (bottom) — the Pi returns to `2040a66` and the evening's Blocks 3–5 are off.

## Block 3 — deploy restart + the floor, AFTER (5 min)

```
~/bench.sh restart
```

**Expect the lawful boot glance:** `device_relinked` ×6 · `adoption_maps_rehydrated: devices=6` · ZERO `device_proposed` / permit-join lines · `projection_live devices=6 entities=6 position=25065` (≥, at-equality lawful) · `network_resumed: channel=20 panId=0x774c` · RADIO UP ~12 s. Then:

```
~/bench.sh scenario boot-health
```

**Expect:** `[PASS] boot-health — 6/6 positive · 0 forbidden`. **⏺ RECORD the boot glance + the verdict + bundle. THE DEPLOY IS PROVEN — the Pi runs `c09c61c`.** A `[FAIL]` = STOP + paste + abort ladder.

## Block 4 — THE BROWSER-BLOCK REDUX (~10 min) — G2 closes here

On the **Windows** side (a second terminal; leave it running):

```
ssh -N -L 7070:127.0.0.1:7070 pi
```

Browser → `http://localhost:7070/`

**Glance 0 (the serve path itself):** the address bar lands on `/dashboard/` and the **"Pairing token"** entry screen (the AuthGate) renders — no 401 JSON, no blank page. **⏺ RECORD** ("AuthGate rendered at /dashboard/" or what actually happened).

**The token (⚠ L3):** on the **Pi** terminal:

```
cat ~/hs-bench/config/initial_api_token
```

Read it ON SCREEN and type/paste it into the browser's token field ONLY. **It never enters the return, a ⏺ paste, or this/any conversation.** (If that file is absent, try `cat ~/.homesynapse/config/initial_api_token`; if both are absent, that is a FINDING — ⏺ it, skip glances 1–3.) If the dashboard rejects the token (the honest red message), that is a FINDING — ⏺ the message verbatim and stop the block.

**Glance 1 — G2, the availability tile:** Overview → the Devices/availability tile shows the honest rows — `Available` / `Offline` / **`Not determined yet`** / `Stale` — plus the line "Counts reflect each device's last report — not a live connection test". **⏺ RECORD the rows + counts verbatim.**

**Glance 2 — evidence-with-age:** Devices → open any entity's drawer → the evidence line with its age renders (e.g. last report + how old). **⏺ RECORD the line verbatim.**

**Glance 3 — the five modes, LIVE from the FIELD:** the runs/explain surface → open a HISTORICAL run from the Rosonway era (any run with superseded / unconfirmed / timed-out actions). **Expect:** the action verdicts render DISTINCT (label + glyph + tone), and the "Recorded outcome" disclosure shows the raw field **with NO recovery note** (v1.1.2 payloads served live). **⏺ RECORD which run + what rendered** (a screenshot into the launch conversation is ideal; never the token).

**Scope law restated:** any glance failing = ⏺ + next glance; three failures = still a complete block. The hub adjudicates; nothing here retro-fails Blocks 0–3.

## Block 5 — close (2 min)

```
~/bench.sh scenario boot-health
```

**Expect:** `[PASS]`. **⏺ RECORD.** Then file the return package (one fenced block, the v38 §5 spec): the verdict table (Blocks 0–5) · every ⏺ paste VERBATIM (token-excluded) · anomalies · the final-state line (HEAD SHA on the Pi, app pid, active log) · the route-back line "intakes as the next v39 hub beat." **On the three glance ⏺s: G2 CLOSES.**

## Abort ladder

- Failure BEFORE Block 2's `git pull`: nothing changed — record and stop.
- Failure in Block 2/3 (build or boot): **⏺ paste verbatim first**, then revert:

```
cd ~/homesynapse-core
git reset --hard 2040a66
./gradlew --no-daemon :app:homesynapse-app:installDist
~/bench.sh restart
~/bench.sh scenario boot-health
```

Expect the pre-evening `[PASS]` floor on `2040a66`; **⏺ RECORD that the revert ran + its verdict.** (Node stays installed — harmless, and the next attempt reuses it; the second build will also be faster: `npm ci` is cached-warm.)
- Block 4/5 failures never trigger the ladder — they are FINDINGS on a proven deploy.

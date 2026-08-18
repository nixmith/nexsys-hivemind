<!--
file: context/handoff/2026-08-17_midweek-FE-deploy_operator-packet.md
purpose: The midweek FE-deploy sitting (~20 min, Tue 08-18 or Wed 08-19 EVENING), chosen by Nick at v54 beat 1 from the beat-8 standing offer: one warm rebuild at core `beb664e` → deploy → the FE return's §8 scripted live pass (H8 tier 2) → the NEW-7 404-body capture. On the pasted ⏺ set the NEW-2/NEW-3 surfaces flip REPO-COMPLETE/LIVE-PENDING → VERIFIED-LIVE per H8, and H8 tier-2 closes AHEAD of weekend 1.
audience: Nick (operator; run it block-by-block in ONE sitting, one Pi terminal kept open through Block 3). Results paste back into the v54 hub conversation; the hub files the instrument record (law 11) at the next beat.
status: READY — executes Tue or Wed evening; post-freeze-lawful (the HOLD lifted at the gate); clear of the nightly by construction (the suite fires ~03:30 CT — never run this inside 03:00–04:15 CT).
laws: L2 — every command is copy-paste-complete. L3 — THE TOKEN NEVER ENTERS A CONVERSATION: read it on the Pi terminal, type/paste it into the BROWSER only; every ⏺ paste EXCLUDES the token line. Scope law — a broken glance is a FINDING (⏺ + move on), never a debug session, and never retro-fails earlier blocks. Anti-actions — no constants.yaml/config edits, no cabling changes, no scenario runs beyond `boot-health`, HANDS OFF the s31 legs and the nightly machinery.
source of record for Block 5: context/audits/2026-08-17_FE-lane_NEW23_return.md §8 (the rows below are its condensed operator form; on any wording doubt the return governs).
-->

# Midweek FE-Deploy Sitting — Operator Packet (target core `beb664e`; ~20 min)

**Goal:** the Pi runs `beb664e`; the six §8 rows pass live; the 404 body is captured.
**Done-when:** Blocks 0–4 `[PASS]` + the six Block-5 row ⏺s (any verdict) + the Block-6 close ⏺ — all pasted back (token-excluded).

## Block 0 — the floor, BEFORE (2 min)

On the Pi (interactive `ssh pi`; keep this terminal open through Block 3):

```
~/bench.sh scenario boot-health
```

**Expect:** `[PASS] boot-health — 6/6 positive · 0 forbidden` + a bundle line. **⏺ RECORD the verdict line + bundle.** A `[FAIL]` = STOP, paste, the sitting is off (nothing has changed yet).

## Block 1 — pin the pre-state (1 min)

```
cd ~/homesynapse-core
git log --oneline -1
PREV=$(git rev-parse --short HEAD); echo "PREV=$PREV"
```

**⏺ RECORD both output lines** — the recorded SHA is the abort ladder's revert target (the `$PREV` variable serves it while this terminal lives; the ⏺ paste serves it if the terminal dies).

## Block 2 — pull + the warm rebuild (3–8 min)

```
git pull
git log --oneline -1
./gradlew --no-daemon :app:homesynapse-app:installDist
```

**Expect, in order:** a fast-forward ending at `beb664e`; the log line `beb664e core: FE NEW-2/NEW-3 …`; then the build — npm is cached-warm from DASH-SERVE, so minutes not tens; the jar SELF-ASSERTS the SPA is inside it (a missing SPA fails LOUDLY). **⏺ RECORD the `BUILD SUCCESSFUL in …` line.** Any failure = paste verbatim FIRST, then run the abort ladder (bottom) — the sitting's Blocks 3–6 are off.

## Block 3 — restart + the floor, AFTER (3 min)

```
~/bench.sh restart
```

**Expect the lawful boot glance:** `device_relinked` ×6 · `adoption_maps_rehydrated: devices=6` · ZERO `device_proposed`/permit-join lines · `projection_live devices=6 entities=6 position=<current>` · `network_resumed: channel=20 panId=0x774c`. Then:

```
~/bench.sh scenario boot-health
```

**Expect:** `[PASS] boot-health — 6/6 positive · 0 forbidden`. **⏺ RECORD the boot glance + the verdict + bundle. THE DEPLOY IS PROVEN — the Pi runs `beb664e`.** A `[FAIL]` = paste + abort ladder.

## Block 4 — tunnel + token (⚠ L3) (2 min)

On the **Windows** side (a second terminal; leave it running):

```
ssh -N -L 7070:127.0.0.1:7070 pi
```

Browser → `http://localhost:7070/` — expect the AuthGate ("Pairing token" screen). On the **Pi** terminal:

```
cat ~/hs-bench/config/initial_api_token
```

(If absent: `cat ~/.homesynapse/config/initial_api_token`; both absent = a FINDING — ⏺ it and stop the block.) Read it ON SCREEN, type/paste into the browser ONLY. **It never enters a ⏺ paste or any conversation.** **⏺ RECORD:** "AuthGate rendered; token accepted" (or what actually happened, token-excluded).

## Block 5 — THE §8 LIVE PASS (H8 tier 2; ~8 min)

**DevTools console OPEN THROUGHOUT (F12).** Any raw uncaught `TypeError` anywhere in the sitting FALSIFIES NEW-2 — a CONTAINED failure instead logs `[render-error] contained by ErrorBoundary:` and shows the honest render-failure card. Per row: **⏺ RECORD pass/falsified + what rendered.**

1. **The why-not surface, current bench-hero:** navigate from the dashboard's automations/why-not surface to the CURRENT bench-hero automation (the ULID re-mints nightly — DX-19; never a stale bookmark). **Expect:** the "Nothing set it off" pill · the explanation sentence · "What would make it run" · NO "Last checked" row · no spinner past load. **Falsified by:** an indefinite `Loading…`, or `can't access property "at"` in the console — the Act-2 incident signature.
2. **Same page, Network tab:** the non-firing response body's `"lastEvaluation"` is `null` OR an object — either must render. **⏺ which it was.**
3. **Devices → the offline Hue's card:** the prose and the "Last reported" row AGREE — either "last heard from X ago" + a date-qualified stamp, or "the time of the last report is not recorded" + `—`. **Falsified by:** "last heard from —" in prose, a bare clock time on a >24 h-old report, or any 1970-plausible morning time.
4. **Any run detail >24 h old** (`#/explain/run/…`): the trigger line reads "… at H:MM on <Mon D>." **Falsified by:** a bare clock time on an old run.
5. **`#/events`:** the calm, honest 404 card with retry (unchanged posture). **While here — THE NEW-7 CAPTURE:** DevTools → Network → the `GET /api/v1/events` request → copy the raw RESPONSE BODY → **⏺ paste it whole** (capture ONLY — the ruling is (d)-degrading-to-(a); no fix, no follow-up act).
6. **Cross-surface:** the header "Updated …" stamp keeps ticking on every surface visited after rows 1–5. **Falsified by:** a frozen stamp (the 2026-07-27 signature).

**Scope law restated:** any row failing = ⏺ + next row; six findings is still a complete block. The hub adjudicates; nothing here retro-fails Blocks 0–4.

## Block 6 — close (1 min)

```
~/bench.sh scenario boot-health
```

**Expect:** `[PASS]`. **⏺ RECORD.** Then paste the whole ⏺ set (Blocks 0–6, token-excluded) into the v54 hub conversation. The hub files the instrument record and flips the NEW-2/3 surfaces to VERIFIED-LIVE per H8 at the next beat.

## Abort ladder

- Failure BEFORE Block 2's `git pull`: nothing changed — record and stop.
- Build/boot failure (Block 2/3): **⏺ paste verbatim first**, then:

```
cd ~/homesynapse-core
git reset --hard "$PREV"
./gradlew --no-daemon :app:homesynapse-app:installDist
~/bench.sh restart
~/bench.sh scenario boot-health
```

⚠ Fill-in before running IF the Block-1 terminal died: replace `"$PREV"` with the Block-1 ⏺-recorded SHA (it is the only substitution in this packet). **Expect** the pre-sitting `[PASS]` floor on the recorded SHA; **⏺ RECORD that the revert ran + its verdict.** (npm stays cached; a retry another evening is cheap.)
- Block 4/5/6 failures never trigger the ladder — they are FINDINGS on a proven deploy.

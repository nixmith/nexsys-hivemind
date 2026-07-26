<!--
file: context/handoff/2026-07-24_cmd-api-deploy-evening_operator-brief.md
purpose: Operator brief — THE CMD-API DEPLOY EVENING: the Pi moves `355a711` → `4bc1258` (pull → installDist → practiced restart → boot glance → boot-health), + the H4 [S] restart-honesty rep + the A4 [S] kill−9 rep as riders (the "first post-deploy bench session" both criteria rows name). Authored per playbook §8 by the v37 hub (beat 1); v37 charge 2.
audience: Nick (one bench evening); any Cowork session guiding him runs THIS file block-by-block.
status: READY — **deploy ≥ 2026-07-26; TARGET RE-RULED 2026-07-26 (v38 beat 5): the Pi deploys `da11f46` (the SKIP-VIS landing — CMD-API + the explanation-honesty fixes in ONE build hop), PRECONDITIONED on a ci.yml GREEN verdict for `da11f46` verified BEFORE the evening starts (⏺ it; RED ⇒ the evening is OFF, the hub adjudicates)** (Nick's soak-first ruling, 2026-07-25: the Rosonway topology carries ZERO soak hours on move day; the deploy's restart/kill−9 reps are transport-stressing and never stack onto the move day — ruling-3's purpose honored over its letter; §8 tired-human clause). Block 0a below banks the overnight soak as free evidence. Preconditions: `5b4797e` ALL-CI-GREEN standing (the CMD-API gate of record; `4bc1258` = + the two dependabot web-ui merges, zero-Java, frontend checks green) · NO other physical change in flight · **NEVER the same evening as the Rosonway topology move** (single-variable law; if Rosonway already ran, its Block-3 boot-health [PASS] must be in hand before this evening starts).
semantics (instrument, stated — the playbook §8 class): `device_relinked` ×6 IS the lawful NORMAL-boot signature (registry rehydration; boot-health itself asserts ≥2) — zero relinks would FAIL the floor. The rejoin tokens to expect ZERO of: `device_proposed`, `UNSECURED_JOIN`, `permit_join_opened`, device announces. Availability resolves at ping-scale (minutes) — never out-wait it at a glance point; boot-health is the verdict instrument. The new write surface (`POST /api/v1/entities/{entityId}/commands`) ships DORMANT tonight — no bench scenario drives it until B2; nothing about this evening exercises it, and that is by design (the deploy is ONE variable).
-->

# Operator Brief — The CMD-API Deploy Evening (+H4/A4 riders; one evening, single-variable)

**Goal:** the Pi runs **`da11f46`** with the floor proven green, and the two cheap [S] rows both named for "the first post-deploy bench session" are banked: **H4** (restart honesty ×1 on the deployed build) and **A4** (one deliberate `kill -9` rep: zero event loss + ULID continuity).
**Done-when:** FIVE ⏺ pastes are in the hub's hands — Block-0a soak glance, Block-0 floor, Block-2 boot glance + `[PASS]`, Block-3 H4 rep, Block-4 A4 rep. ⏺ EVERY block, either way — a FAIL paste is a finding, not a failure.

## Block 0a — the overnight-soak glance (run FIRST — before Block 0, because boot-health RESTARTS the app)
1. ONE act: `grep -E "transport_failed|port_unhealthy|reopen_no_target|ASH_ERROR" $(~/bench.sh log) | tail -3`
2. Expect: the NEWEST matching line predates the Rosonway session close (~13:57 Pi-local 2026-07-25 / 17:57Z) — i.e., ZERO new transport tokens across the overnight soak on the standing boot (`bench-2026-07-25-122148.log`). The session's own rep lines (transport_failed ×2 · port_unhealthy ×2 · reopen_no_target ×8, 13:24–13:25 Pi-local) are LAWFUL history, not findings.
3. ⏺ RECORD the newest line + its timestamp = **the topology's first soak evidence banks free.**
   ⛔ Any matching line NEWER than the session close ⇒ STOP + ⏺ paste — the soak surfaced something; the deploy waits for adjudication.

## Block 0 — the floor, BEFORE (~3 min)
1. Confirm nothing else is in flight tonight (no Rosonway move, no config edit, no cable change; the Gen4 plugs stay off-network as always).
2. Run: `~/bench.sh scenario boot-health` → expect `[PASS] boot-health — 6/6 positive · 0 forbidden`. ⏺ paste.
   ⛔ Anything but [PASS] ⇒ STOP — the floor must be green before the variable changes.

## Block 1 — pull + build (~5–10 min; the app may stay up while Gradle builds)
1. `git -C ~/homesynapse-core pull`
2. `cd ~/homesynapse-core && git log --oneline -3` → expect **`da11f46`** at HEAD (core: SKIP-VIS, above the two dependabot merges and `5b4797e`). ⏺ RECORD the SHA. ⛔ Any other HEAD ⇒ STOP + ⏺ paste — never deploy an unexpected tree. [Re-targeted from `4bc1258` at v38 beat 5 — SKIP-VIS landed on main 2026-07-26; ci.yml GREEN on `da11f46` is a hard precondition, verified before the evening.]
3. `cd ~/homesynapse-core && ./gradlew :app:homesynapse-app:installDist`
   (the launcher lands at `app/homesynapse-app/build/install/homesynapse-app/bin/homesynapse-app` — the runbook's canonical jar set; the systemd unit stays unused on the bench per the runbook's PrivateDevices note.)
4. ANTI-ACTIONS: no config edits · no `constants.yaml` edit (the `command-api` flip rides B2's re-mint, never tonight) · no scenario runs mid-build · no Rosonway cabling.

## Block 2 — the deploy restart + boot glance
1. Pre-restart truth: `grep "registry.projection_live" $(~/bench.sh log) | tail -1` → ⏺ RECORD the position (call it **P-pre**; expect ≥ 25065).
2. Stop the app cleanly (your practiced SIGTERM stop — same as every bench close). Wait for full shutdown.
3. Start the app (your practiced start — the FRESH installDist launcher, nohup + tee per the runbook, e.g. `~/homesynapse-core/app/homesynapse-app/build/install/homesynapse-app/bin/homesynapse-app 2>&1 | tee ~/hs-bench/bench-$(date +%F-%H%M).log`).
4. Expect, in the practiced envelope: `/dev/zigbee` resolves · RADIO UP ~11–13 s · `port_identity_captured` · `registry.projection_live devices=6 entities=6` at a position **≥ P-pre** · `adoption_maps_rehydrated: devices=6` · `network_resumed channel=20 panId=0x774c` · **`device_relinked` ×6 — EXPECTED (lawful)** · ZERO of `device_proposed` / `UNSECURED_JOIN` / `permit_join_opened`.
5. Run: `~/bench.sh scenario boot-health` → expect `[PASS] — 6/6 positive · 0 forbidden`. ⏺ paste boot block + verdict = **THE DEPLOY IS PROVEN — the Pi runs `4bc1258`.**
   ⛔ [FAIL] ⇒ STOP, ⏺ paste, NO riders tonight — the hub adjudicates first.

## Block 3 — H4 [S], the restart-honesty rep (deployed build; ~3 min)
1. ONE practiced stop → start on the SAME build (no pull, no edit — the deliberate restart rep, distinct from Block 2's deploy restart).
2. Expect the same Block-2 lawful signature (relinked ×6 · zero proposes · `projection_live` ≥ the Block-2 position).
3. `~/bench.sh scenario boot-health` → `[PASS]`. ⏺ paste = **H4 [S] banks** (the landed WUs didn't regress the DUR proof).

## Block 4 — A4 [S], the kill −9 rep (~5 min)
1. Pre-kill truth: `grep "registry.projection_live" $(~/bench.sh log) | tail -1` → ⏺ RECORD (**P-kill**).
2. Find the app PID (your practiced pgrep on the homesynapse-app launcher) → `kill -9 <PID>`. NO clean shutdown, no second signal — the hard kill IS the experiment.
3. Start the app (practiced start). Expect the SAME lawful boot signature — relinked ×6 · zero proposes · `registry.projection_live devices=6 entities=6` at a position **≥ P-kill** (write-ahead durability: nothing accepted pre-kill is lost).
4. `~/bench.sh scenario boot-health` → `[PASS]` (the remembered-ULID assert IS the identity-continuity instrument). ⏺ paste = **A4 [S] banks** (MVP §8.1 write-ahead durability, exercised as SIGKILL rather than the pkill/restart class already proven).

## Block 5 — close
1. All pastes → the hub next turn (corpus material; the ratchet rule). The hub re-statuses **A4 → ✅ · H4 → ✅** and records the deploy on the criteria ledger.
2. B2 authoring proceeds against THIS deployed build; the AUTO command scenarios stay post-B2 as sequenced.
3. The Rosonway evening is DONE (I3b [S] closed 2026-07-25; the topology is STANDING; the operator package is archived).

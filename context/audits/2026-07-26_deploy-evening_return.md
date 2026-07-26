<!--
file: context/audits/2026-07-26_deploy-evening_return.md
purpose: The deploy-evening navigator session's RETURN PACKAGE, verbatim (target 2040a66, status COMPLETE) — the corpus record of the evening that put `2040a66` on the Pi, banked A4 + H4, and surfaced the no-dashboard-serve-path finding.
audience: hub (intaken v38 beat 7 — adjudications + the WU-DASH-SERVE plan live in pm-handoff v38 beat 7, pointer not copy); corpus.
status: INTAKEN 2026-07-26 (v38 beat 7). The three-blocker source verification (B-1 no staticFiles mount · B-2 no web-ui artifact/packaging · B-3 catch-all auth) is the HUB's layer-2 finding recorded in pm-handoff beat 7 — this file is the navigator's evidence exactly as returned by Nick.
-->

DEPLOY-EVENING RETURN — 2026-07-26 — target 2040a66 — status: COMPLETE

## 1. VERDICT TABLE

| Block | Verdict | Evidence |
|---|---|---|
| 0a — overnight soak | PASS | Newest transport token 13:25:06.748 (2026-07-25), predates the 13:57 session close; zero new tokens across the soak. |
| 0 — floor BEFORE | PASS | `[PASS] boot-health — 6/6 positive · 0 forbidden` on the pre-deploy build (pid 39186). |
| 1 — pull + build | PASS | Fast-forward 355a711→2040a66; HEAD chain 2040a66 / da11f46 / 4bc1258; `BUILD SUCCESSFUL in 23s`. |
| 2 — deploy restart | PASS | Restart onto the rebuilt installDist tree (pid 39548) + `[PASS]` verdict (pid 39668). THE PI RUNS 2040a66. |
| 3 — H4 [S] restart honesty | PASS | Rep boot pid 39794 lawful; `[PASS]` verdict pid 39911. H4 BANKS. |
| 4 — A4 [S] kill −9 | PASS | kill -9 39911 → position 25065 ≥ P-kill, six ULIDs identical, `[PASS]` verdict pid 40158. A4 BANKS. |
| 4b — dashboard glances | FINDING — glances 1/2/3 UNOBSERVED | GET / → HTTP 401 authentication-required. Dashboard never rendered. Does NOT retro-fail 0a–4. |

## 2. THE ⏺ PASTES, VERBATIM

### 2.1 Block 0a — soak newest line
13:25:06.748 [integration-zigbee-0] WARN  c.h.i.z.ZigbeeIntegrationAdapter -- zigbee.reopen_no_target: the coordinator port did not re-enumerate; retrying on the watchdog backoff

(Newest of three; all inside the lawful 13:24–13:25 rep window, all predating the 13:57 Pi-local session close.)

### 2.2 Block 0 — the floor, BEFORE
  [OK] launched pid 39186 -> /home/homesynapse/hs-bench/bench-2026-07-26-165836.log
  [OK] RADIO UP after 12s
[PASS] boot-health — 6/6 positive · 0 forbidden
  [--] bundle: /home/homesynapse/hs-bench/bundles/boot-health-20260726T205848Z

### 2.3 Block 1 — HEAD of record + build
From https://github.com/nexsys-io/homesynapse-core
   355a711..2040a66  main       -> origin/main
Updating 355a711..2040a66
Fast-forward
 50 files changed, 4057 insertions(+), 377 deletions(-)

2040a66 core: FE-VERDICT-2 -- the dashboard renders the five
da11f46 core: SKIP-VIS -- explanation honesty at the derivat
4bc1258 Merge pull request #2 from nexsys-io/dependabot/npm_

BUILD SUCCESSFUL in 23s
56 actionable tasks: 11 executed, 45 up-to-date

### 2.4 P-pre
16:58:39.327 [hs-sub-registry_projection] INFO  c.h.l.RegistryProjectionSubscriber -- registry.projection_live: devices=6 entities=6 position=25065

### 2.5 Block 2 — the deploy boot glance (17:08:43, first boot on 2040a66)
  [OK] stopped
  [OK] launched pid 39548 -> /home/homesynapse/hs-bench/bench-2026-07-26-170843.log
  [--] waiting for a decisive radio state (up to 90 s)...
  [OK] RADIO UP after 12s
--- health tokens (current boot: /home/homesynapse/hs-bench/bench-2026-07-26-170843.log) ---
17:08:46.669 [hs-sub-registry_projection] INFO  c.h.l.RegistryProjectionSubscriber -- registry.projection_live: devices=6 entities=6 position=25065
17:08:47.177 [integration-supervisor-start] INFO  c.h.i.zigbee.ZigbeeAdoptionSlice -- zigbee.device_relinked: device=0xF044D3FFFED2A201 deviceId=01KXW0156Z1GJ3WCV2G516AKWS — re-pairing, no new adoption
17:08:47.181 [integration-supervisor-start] INFO  c.h.i.zigbee.ZigbeeAdoptionSlice -- zigbee.device_relinked: device=0x00178801101A09BB deviceId=01KX1PA4GRZHY2GD37B5CFVQHY — re-pairing, no new adoption
17:08:47.185 [integration-supervisor-start] INFO  c.h.i.zigbee.ZigbeeAdoptionSlice -- zigbee.device_relinked: device=0x449FDAFFFE688F57 deviceId=01KY12MQVQ204M1VP39F1ZDM33 — re-pairing, no new adoption
17:08:47.189 [integration-supervisor-start] INFO  c.h.i.zigbee.ZigbeeAdoptionSlice -- zigbee.device_relinked: device=0xF044D3FFFE9C78D7 deviceId=01KX1PB9A5931A8G0F0X03QXT2 — re-pairing, no new adoption
17:08:47.196 [integration-supervisor-start] INFO  c.h.i.zigbee.ZigbeeAdoptionSlice -- zigbee.device_relinked: device=0x00124B002FA8D1C5 deviceId=01KXW1W1RR66GV98D9QDPB4VXY — re-pairing, no new adoption
17:08:47.200 [integration-supervisor-start] INFO  c.h.i.zigbee.ZigbeeAdoptionSlice -- zigbee.device_relinked: device=0xF044D3FFFE1C1E8E deviceId=01KXW13WEGRCT5C0XSQT8WZBG9 — re-pairing, no new adoption
17:08:47.201 [integration-supervisor-start] INFO  c.h.i.z.ZigbeeIntegrationAdapter -- zigbee.adoption_maps_rehydrated: devices=6
17:08:55.032 [integration-zigbee-0] INFO  c.h.i.z.ZigbeeIntegrationAdapter -- zigbee.network_resumed: channel=20 panId=0x774c
17:08:55.032 [integration-zigbee-0] INFO  c.h.i.zigbee.EzspCoordinatorProtocol -- zigbee.network_up: stackStatusHandler reported EMBER_NETWORK_UP (buffered)
--- failure tokens ---

### 2.6 Block 2 — the deploy verdict (17:11:54)
  [--] stimulus bench: restart
  [OK] launched pid 39668 -> /home/homesynapse/hs-bench/bench-2026-07-26-171154.log
  [OK] RADIO UP after 12s
    [ok] log 'registry.projection_live: devices=6 entities=6' min=25065 — 17:11:57.277 [hs-sub-registry_projection] INFO  c.h.l.RegistryProjectionSubscriber -- registry.projection_live: devices=6 entities=6 position=25065 (within 90s)
    [ok] log 'zigbee.adoption_maps_rehydrated: devices=6' — 17:11:57.839 [integration-supervisor-start] INFO  c.h.i.z.ZigbeeIntegrationAdapter -- zigbee.adoption_maps_rehydrated: devices=6 (within 90s)
    [ok] log 'zigbee.device_relinked' x2(at-least) — 17:11:57.815 [integration-supervisor-start] INFO  c.h.i.zigbee.ZigbeeAdoptionSlice -- zigbee.device_relinked: device=0xF044D3FFFE9C78D7 deviceId=01KX1PB9A5931A8G0F0X03QXT2 — re-pairing, no new adoption (within 90s)
    [ok] log 'zigbee.network_resumed: channel=20 panId=0x774c' — 17:12:05.751 [integration-zigbee-0] INFO  c.h.i.z.ZigbeeIntegrationAdapter -- zigbee.network_resumed: channel=20 panId=0x774c (within 90s)
    [ok] log 'zigbee.port_identity_captured:' same-line ['pinnedOnly=false'] — 17:12:05.635 [integration-zigbee-0] INFO  c.h.i.z.ZigbeeIntegrationAdapter -- zigbee.port_identity_captured: stableId=/dev/serial/by-id/usb-SONOFF_SONOFF_Dongle_Plus_MG24_0ae2dd7cecf8ef11b80168135c2a50c9-if00-port0 vendorId=10c4 productId=ea60 pinnedOnly=false (within 90s)
    [ok] api /api/v1/entities {"rows": 6, "ulids": ["01KX1PA4HSJ581GASYB7DHE40F", "01KX1PB9AAB4VB3E10BD477TV3", "01KXW0157SP56CCSGJCNDCSQNG", "01KXW13WF0D6TYGN13WXHTG87K", "01KXW1W1SBJZERC9MBAMV2DWKE", "01KY12MQW954E4XYNKH0Y5H8VX"]} — all asserts satisfied (within 90s)
[PASS] boot-health — 6/6 positive · 0 forbidden
  [--] bundle: /home/homesynapse/hs-bench/bundles/boot-health-20260726T211206Z

### 2.7 Block 3 — the H4 [S] rep (17:13:43 rep boot + 17:14:12 verdict)
  [OK] stopped
  [OK] launched pid 39794 -> /home/homesynapse/hs-bench/bench-2026-07-26-171343.log
  [OK] RADIO UP after 12s
--- health tokens (current boot: /home/homesynapse/hs-bench/bench-2026-07-26-171343.log) ---
17:13:46.613 [hs-sub-registry_projection] INFO  c.h.l.RegistryProjectionSubscriber -- registry.projection_live: devices=6 entities=6 position=25065
17:13:47.107 [integration-supervisor-start] INFO  c.h.i.zigbee.ZigbeeAdoptionSlice -- zigbee.device_relinked: device=0x00124B002FA8D1C5 deviceId=01KXW1W1RR66GV98D9QDPB4VXY — re-pairing, no new adoption
17:13:47.114 [integration-supervisor-start] INFO  c.h.i.zigbee.ZigbeeAdoptionSlice -- zigbee.device_relinked: device=0xF044D3FFFE9C78D7 deviceId=01KX1PB9A5931A8G0F0X03QXT2 — re-pairing, no new adoption
17:13:47.119 [integration-supervisor-start] INFO  c.h.i.zigbee.ZigbeeAdoptionSlice -- zigbee.device_relinked: device=0x449FDAFFFE688F57 deviceId=01KY12MQVQ204M1VP39F1ZDM33 — re-pairing, no new adoption
17:13:47.123 [integration-supervisor-start] INFO  c.h.i.zigbee.ZigbeeAdoptionSlice -- zigbee.device_relinked: device=0x00178801101A09BB deviceId=01KX1PA4GRZHY2GD37B5CFVQHY — re-pairing, no new adoption
17:13:47.127 [integration-supervisor-start] INFO  c.h.i.zigbee.ZigbeeAdoptionSlice -- zigbee.device_relinked: device=0xF044D3FFFED2A201 deviceId=01KXW0156Z1GJ3WCV2G516AKWS — re-pairing, no new adoption
17:13:47.131 [integration-supervisor-start] INFO  c.h.i.zigbee.ZigbeeAdoptionSlice -- zigbee.device_relinked: device=0xF044D3FFFE1C1E8E deviceId=01KXW13WEGRCT5C0XSQT8WZBG9 — re-pairing, no new adoption
17:13:47.131 [integration-supervisor-start] INFO  c.h.i.z.ZigbeeIntegrationAdapter -- zigbee.adoption_maps_rehydrated: devices=6
17:13:55.067 [integration-zigbee-0] INFO  c.h.i.z.ZigbeeIntegrationAdapter -- zigbee.network_resumed: channel=20 panId=0x774c
17:13:55.067 [integration-zigbee-0] INFO  c.h.i.zigbee.EzspCoordinatorProtocol -- zigbee.network_up: stackStatusHandler reported EMBER_NETWORK_UP (buffered)
--- failure tokens ---

  [OK] launched pid 39911 -> /home/homesynapse/hs-bench/bench-2026-07-26-171412.log
[PASS] boot-health — 6/6 positive · 0 forbidden
  [--] bundle: /home/homesynapse/hs-bench/bundles/boot-health-20260726T211424Z

### 2.8 P-kill
17:14:15.333 [hs-sub-registry_projection] INFO  c.h.l.RegistryProjectionSubscriber -- registry.projection_live: devices=6 entities=6 position=25065

pgrep -f homesynapse-app → 39911

### 2.9 Block 4 — the A4 [S] kill −9 rep
$ kill -9 39911
$ ~/bench.sh restart
  [--] nothing was running
  [OK] launched pid 40041 -> /home/homesynapse/hs-bench/bench-2026-07-26-171837.log
  [--] waiting for a decisive radio state (up to 90 s)...
  [OK] RADIO UP after 12s
--- health tokens (current boot: /home/homesynapse/hs-bench/bench-2026-07-26-171837.log) ---
17:18:40.409 [hs-sub-registry_projection] INFO  c.h.l.RegistryProjectionSubscriber -- registry.projection_live: devices=6 entities=6 position=25065
17:18:40.954 [integration-supervisor-start] INFO  c.h.i.zigbee.ZigbeeAdoptionSlice -- zigbee.device_relinked: device=0xF044D3FFFE9C78D7 deviceId=01KX1PB9A5931A8G0F0X03QXT2 — re-pairing, no new adoption
17:18:40.957 [integration-supervisor-start] INFO  c.h.i.zigbee.ZigbeeAdoptionSlice -- zigbee.device_relinked: device=0x00124B002FA8D1C5 deviceId=01KXW1W1RR66GV98D9QDPB4VXY — re-pairing, no new adoption
17:18:40.961 [integration-supervisor-start] INFO  c.h.i.zigbee.ZigbeeAdoptionSlice -- zigbee.device_relinked: device=0xF044D3FFFE1C1E8E deviceId=01KXW13WEGRCT5C0XSQT8WZBG9 — re-pairing, no new adoption
17:18:40.965 [integration-supervisor-start] INFO  c.h.i.zigbee.ZigbeeAdoptionSlice -- zigbee.device_relinked: device=0xF044D3FFFED2A201 deviceId=01KXW0156Z1GJ3WCV2G516AKWS — re-pairing, no new adoption
17:18:40.969 [integration-supervisor-start] INFO  c.h.i.zigbee.ZigbeeAdoptionSlice -- zigbee.device_relinked: device=0x00178801101A09BB deviceId=01KX1PA4GRZHY2GD37B5CFVQHY — re-pairing, no new adoption
17:18:40.973 [integration-supervisor-start] INFO  c.h.i.zigbee.ZigbeeAdoptionSlice -- zigbee.device_relinked: device=0x449FDAFFFE688F57 deviceId=01KY12MQVQ204M1VP39F1ZDM33 — re-pairing, no new adoption
17:18:40.973 [integration-supervisor-start] INFO  c.h.i.z.ZigbeeIntegrationAdapter -- zigbee.adoption_maps_rehydrated: devices=6
17:18:48.695 [integration-zigbee-0] INFO  c.h.i.z.ZigbeeIntegrationAdapter -- zigbee.network_resumed: channel=20 panId=0x774c
17:18:48.696 [integration-zigbee-0] INFO  c.h.i.zigbee.EzspCoordinatorProtocol -- zigbee.network_up: stackStatusHandler reported EMBER_NETWORK_UP (buffered)
--- failure tokens ---

  [OK] launched pid 40158 -> /home/homesynapse/hs-bench/bench-2026-07-26-171942.log
    [ok] log 'registry.projection_live: devices=6 entities=6' min=25065 — 17:19:45.497 [hs-sub-registry_projection] INFO  c.h.l.RegistryProjectionSubscriber -- registry.projection_live: devices=6 entities=6 position=25065 (within 90s)
    [ok] log 'zigbee.port_identity_captured:' same-line ['pinnedOnly=false'] — 17:19:53.603 [integration-zigbee-0] INFO  c.h.i.z.ZigbeeIntegrationAdapter -- zigbee.port_identity_captured: stableId=/dev/serial/by-id/usb-SONOFF_SONOFF_Dongle_Plus_MG24_0ae2dd7cecf8ef11b80168135c2a50c9-if00-port0 vendorId=10c4 productId=ea60 pinnedOnly=false (within 90s)
    [ok] api /api/v1/entities {"rows": 6, "ulids": ["01KX1PA4HSJ581GASYB7DHE40F", "01KX1PB9AAB4VB3E10BD477TV3", "01KXW0157SP56CCSGJCNDCSQNG", "01KXW13WF0D6TYGN13WXHTG87K", "01KXW1W1SBJZERC9MBAMV2DWKE", "01KY12MQW954E4XYNKH0Y5H8VX"]} — all asserts satisfied (within 90s)
[PASS] boot-health — 6/6 positive · 0 forbidden
  [--] bundle: /home/homesynapse/hs-bench/bundles/boot-health-20260726T211954Z

### 2.10 Block 4b — the three glance records
GLANCE 1 (G2 availability tile): UNOBSERVED — dashboard did not render.
GLANCE 2 (evidence-with-age): UNOBSERVED — dashboard did not render.
GLANCE 3 (five modes from the FIELD): UNOBSERVED — dashboard did not render.

What was observed instead. Transport: ssh -N -L 7070:127.0.0.1:7070 pi (the HTTP surface binds loopback only — evidenced by "Failed to bind to /127.0.0.1:7070" in 3.1 below). Browser to http://localhost:7070/ returned, verbatim:

{"type":"https://homesynapse.local/problems/authentication-required","title":"Authentication Required","status":401,"detail":"missing or malformed Authorization header; expected 'Authorization: Bearer {token}'","instance":"/","correlation_id":"ae7990f0-3be8-422c-ad11-7897496c43c2"}

Facts, without adjudication:
- The guard covers instance "/" — the document root, not only /api/v1/*. No unauthenticated shell exists for the SPA to boot from.
- The expected credential is a request header (Authorization: Bearer). Browser top-level navigation cannot attach one, so possession of a token would not by itself change this result via the address bar.
- Nick has NEVER opened this dashboard; no pairing flow, saved token, or established URL exists on the bench (asked and answered explicitly).
- This is silent on whether FE-VERDICT-2's assets are present or correct — they were never reachable. Neither confirmed nor refuted.
- RestFilters.java is NEW in 2040a66 (+77 lines) per the Block-1 diffstat. Stated as fact only; causal attribution not made.
- correlation_id for log correlation: ae7990f0-3be8-422c-ad11-7897496c43c2

## 3. ANOMALIES / NOTES

### 3.1 Operator sequencing error — a raw launcher run with the app still up (the evening's one real incident)
Cause of record: the NAVIGATOR handed a bare launcher path with "use your practiced start wrapper" instead of a copy-paste-complete command, in violation of its own §2.2. Nick ran the path raw from ~/homesynapse-core while pid 39186 still held port 7070. Navigator error, not operator error.

Verbatim, the decisive lines:
io.javalin.util.JavalinBindException: Port already in use. Make sure no other process is using port 7070 and try again.
Caused by: java.io.IOException: Failed to bind to /127.0.0.1:7070
17:05:05.405 [main] INFO  c.h.persistence.DatabaseExecutor -- New database detected — applying creation-time PRAGMAs
17:05:05.252 [main] INFO  c.h.persistence.DatabaseExecutor -- Starting DatabaseExecutor: path=/home/homesynapse/homesynapse-core/.homesynapse/data/homesynapse-events.db readThreads=2
17:05:05.483 [main] INFO  c.h.persistence.MigrationRunner -- Migration run complete: applied=5 skipped=0 duration=36ms
17:05:06.163 [hs-sub-registry_projection] INFO  c.h.l.RegistryProjectionSubscriber -- registry.projection_live: devices=0 entities=0 position=0
17:05:06.199 [main] WARN  c.h.api.rest.OpaqueTokenStore -- Minted the initial HomeSynapse API token (shown once). Pair a client with this bearer token, then delete the artifact at /home/homesynapse/homesynapse-core/.homesynapse/config/initial_api_token. Token: [REDACTED-IN-FILE — the stray store's token; never valid against the live app; structurally burned by the beat-7 cleanup order `rm -rf ~/homesynapse-core/.homesynapse`. The raw value exists in the two launch-conversation transcripts only.]
17:05:06.504 [main] INFO  c.h.lifecycle.HomeSynapseCore -- HomeSynapseCore stopped: db=/home/homesynapse/homesynapse-core/.homesynapse/data/homesynapse-events.db (startup failure: Port already in use. Make sure no other process is using port 7070 and try again.)

RESIDUE LEFT ON DISK (deliberately NOT cleaned — zero-writes fence):
  a) A stray, empty event store at ~/homesynapse-core/.homesynapse/data/homesynapse-events.db — new file, 5 migrations applied, position 0. It sits INSIDE the core repo working tree (gitignored — hub-verified: `.homesynapse/` is line 8 of core .gitignore; porcelain untouched).
  b) A minted initial API token artifact at ~/homesynapse-core/.homesynapse/config/initial_api_token, which is also now present in a Cowork chat transcript. It belongs to the stray empty store, NOT the live bench.

WHAT WAS NOT HARMED (each evidenced):
  - The live event store: untouched. Position 25065 before and after, every boot.
  - The radio: never touched. The failed process died at the HTTP bind; there is not one zigbee line in its entire trace, no /dev/zigbee open, no port contention with the running app.
  - The running app: unaffected; pid 39186 continued serving until the practiced restart stopped it cleanly.
  - The deploy: unaffected. The failed process resolved .homesynapse relative to cwd; all subsequent boots ran via ~/bench.sh from ~.

### 3.2 Practiced motion of record (captured because its ambiguity caused 3.1)
~/bench.sh restart          → clean stop + start, prints the boot glance
~/bench.sh scenario boot-health → performs its OWN "stimulus bench: restart", then asserts
~/bench.sh log              → resolves the current boot log

### 3.3 Six lawful boots on 2040a66 tonight
17:08:43 (39548) · 17:11:54 (39668) · 17:13:43 (39794) · 17:14:12 (39911) · 17:18:37 (40041) · 17:19:42 (40158).
Every one: device_relinked ×6, adoption_maps_rehydrated devices=6, network_resumed channel=20 panId=0x774c, RADIO UP at exactly 12s, ZERO device_proposed / UNSECURED_JOIN / permit_join_opened. Blocks 2/3/4 each produced two boots because bench.sh scenario restarts on its own — more restart-honesty evidence than the brief asked for, not less.

### 3.4 kill −9 confirmation
"[--] nothing was running" on the post-kill bring-up confirms SIGKILL fully removed the process and that NO signal reached a live app. A4's experimental integrity is intact — the hard kill was the only stimulus.

### 3.5 Event-store position static
position=25065 across the entire evening and all six boots; the store took no writes. Consistent with the brief's own min=25065 expectation. Noted for completeness; the A4 durability assert is therefore satisfied at equality, not above.

### 3.6 Build timing
BUILD SUCCESSFUL in 23s, 11 executed / 45 up-to-date. Flagged during the run as fast for a 50-file change-set and as a possible signal about whether web assets were bundled into the launcher. UNRESOLVED — the 401 stopped us before that could be observed either way. [HUB NOTE at intake: RESOLVED at source, v38 beat 7 — the suspicion was correct; installDist neither runs npm nor packages the SPA (no artifact from :web-ui:dashboard). pm-handoff beat 7.]

### 3.7 Anti-actions honored
No constants.yaml edit. No config edits. No cabling or physical change. No scenario runs mid-build. The CMD-API write surface (POST /api/v1/entities/{entityId}/commands) was never exercised — ships DORMANT as designed.

## 4. FINAL STATE

- HEAD SHA on the Pi: 2040a66 (core: FE-VERDICT-2)
- App running: YES — pid 40158, the 2040a66 build
- Active log file: /home/homesynapse/hs-bench/bench-2026-07-26-171942.log
- Last verdict: [PASS] boot-health — 6/6 positive · 0 forbidden (bundle boot-health-20260726T211954Z)
- Bundles produced tonight: boot-health-20260726T205848Z (Block 0) · 211206Z (Block 2) · 211424Z (Block 3) · 211954Z (Block 4)
- Left non-standard: the stray ~/homesynapse-core/.homesynapse/ tree from 3.1 (empty events DB + initial_api_token artifact), NOT cleaned per the zero-writes fence. Nothing else. The ssh -N -L tunnel on the Windows side is transient and carries no Pi-side state.

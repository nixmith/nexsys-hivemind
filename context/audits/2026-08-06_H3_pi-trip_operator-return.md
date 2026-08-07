<!--
file: context/audits/2026-08-06_H3_pi-trip_operator-return.md
purpose: The H3 Pi-trip operator return package — FILED BY THE HUB verbatim-as-received (v47 beat 3; the conductor session produced this in-chat only; chat is not a storage tier, so the hub files it). Package: context/handoff/2026-08-06_H3_pi-trip_operator-package.md. Hub audit: context/audits/2026-08-06_H3_audit_v47-beat-3.md.
audience: hub; the charter; future sessions.
status: FILED 2026-08-06 (v47 beat 3). HUB FILING NOTE: the as-received paste carries a truncation seam mid-B7 (the S-4 grep echo cuts at `$ grep -n "port_unh` and resumes inside the B8 record); the missing bytes are the S-4 grep output, which the hub holds in full from Nick's raw terminal transcript of the same run and adjudicates in the audit. Filed as received, unaltered.
-->

=========================================================================
H3 — THE PI TRIP · OPERATOR RETURN PACKAGE
=========================================================================
executed : 2026-08-06 evening, attended (package scoped Aug-8/9 — early
           execution, operator-elected, hub-noted)
operator : Nick, on the Pi (hs-dev-1) via ssh from desktop
conductor: attended L1 support lane — presented blocks in order, held
           gates, checked Expects, recorded. Adjudicated NOTHING.
route-to : hub chat
=========================================================================

--- VERDICT TABLE (Blocks 0-8) --------------------------------------
B0  K ruling ............ RULED "K: (a)" pre-trip. No Pi change. B5 read-only.
B1  pre-deploy baseline .. PASS on the letter. Conductor STOPPED on an
                           apparent anomaly (Aug-6 s31 PASS on old build);
                           hub adjudicated NO ANOMALY (B3.3 bench-side fix,
                           banked v46 beat 5). REVERT SHA 60d3ab5 ratified.
B2  deploy pull + build .. PASS. 60d3ab5 -> 3723e31 fast-forward.
                           BUILD SUCCESSFUL in 36s. lib/ = 3.51.3.0.
B3  restart + JAR VERIFY . PASS. Counts 1 / 0. S-5a is a DEPLOYED fix;
                           the WAL-exposure window on this hub CLOSES here.
B4  boot-health floor .... PASS 6/6 positive · 0 forbidden.
B5  killmode.conf ........ PASS. KillMode=process · Type=oneshot. Read-only.
B6  Hue re-power ......... PHYSICAL ACT DONE (direct wall outlet, ONE
                           power-up, 19:54:56 Pi-local). Log evidence:
                           CLEAN NEGATIVE through T+5:04. No announce.
B7  completeness reads ... COMPLETE. Both settle terminals read; S-4
                           residual answered (cause=read-error, uniform).
B8  fix-verification rep . LAWFUL REP: 8/9 PASS · 1 SKIP(hue-online).
                           s31 PASS 2/2 at position 8; park re-set LAST.
                           Zero FAIL, zero forbidden. NO REGRESSION.
                           ON-latency UNVERIFIED (see H-A2).

--- DONE-WHEN SCORECARD ---------------------------------------------
(1) git log shows 3723e31 ................................. MET
(2) classpath 3.51.3.0 present / 3.51.2.0 zero ............ MET
(3) boot-health [PASS] 6/6 ................................ MET
(4) rep reads 9/9 PASS · 0 SKIP ........................... NOT MET
      - lawful alternative taken: 8/9 PASS · 1 SKIP(hue-online)
      - s31 position 8 .................................... MET
      - s31 2/2 positive ................................. MET
      - park re-set LAST ................................. MET
      - ON-latency present ............................... UNVERIFIED
      - root cause: hue-online is a STATIC constant, never probed.
        9/9 was unreachable this trip BY CONSTRUCTION.
(5) the two reads pasted .................................. MET
(6) return package filed back to the hub .................. this document

=========================================================================
RECORDS (verbatim, at each block's own RECORD scope)
=========================================================================

--- B1 (RECORD all output) -------------------------------------------
$ ~/nexsys-bench/tools/bench.sh digest 3
2026-08-04 quiesced AUTO floor: 7/9 · FAIL command-confirm-s31 · bundle /home/homesynapse/hs-bench/bundles/command-confirm-s31-20260804T083057Z · 1 SKIP(hue-online) · bench-hero RESTORED ✓ · ON-latency n/a(FAIL)
2026-08-05 quiesced AUTO floor: 7/9 · FAIL command-confirm-s31 · bundle /home/homesynapse/hs-bench/bundles/command-confirm-s31-20260805T083057Z · 1 SKIP(hue-online) · bench-hero RESTORED ✓ · ON-latency n/a(FAIL)
2026-08-06 quiesced AUTO floor: 8/9 PASS · 1 SKIP(hue-online) · bench-hero RESTORED ✓ · ON-latency 0.30s

$ cd ~/homesynapse-core && git log --oneline -1
60d3ab5 (HEAD -> main, origin/main, origin/HEAD) zigbee: WU-AVAIL-SEED - availability seed + boot truth (F-14 closed at source; the F2 producer)

$ ls .../build/install/homesynapse-app/lib/ | grep sqlite
sqlite-jdbc-3.51.2.0.jar

REVERT SHA = 60d3ab5   [ratified by hub; NEVER INVOKED — no ladder run]

--- B2 (RECORD pull tail + BUILD SUCCESSFUL + grep) -------------------
From https://github.com/nexsys-io/homesynapse-core
   60d3ab5..3723e31  main       -> origin/main
Updating 60d3ab5..3723e31
Fast-forward
 gradle/libs.versions.toml                                                                                  |   2 +-
 integration/integration-zigbee/src/main/java/com/homesynapse/integration/zigbee/ZigbeeDeviceCache.java     |  21 +++++++++----
 integration/integration-zigbee/src/test/java/com/homesynapse/integration/zigbee/ZigbeeDeviceCacheTest.java | 122 ++++++++++++++++++++++++++++++++++++++++++
 web-ui/dashboard/package-lock.json                                                                         |   8 +++---
 4 files changed, 143 insertions(+), 10 deletions(-)

git log --oneline -3 (subject lines; full bodies unmodified in repo):
  3723e31 (HEAD -> main, origin/main, origin/HEAD) Merge pull request #3 from nexsys-io/dependabot/npm_and_yarn/web-ui/dashboard/brace-expansion-5.0.9
  96d9efb core: S-5c - atomic sidecar write: ZigbeeDeviceCache.write goes temp-then-move ...
  b3d31b8 core: S-5a - sqlite-jdbc 3.51.2.0 -> 3.51.3.0 (the WAL-corruption-class bump) ...
  [ORDER CONFIRMED: 3723e31 atop 96d9efb atop b3d31b8, exactly as Expect]

BUILD SUCCESSFUL in 36s
60 actionable tasks: 7 executed, 53 up-to-date

$ ls .../lib/ | grep sqlite
sqlite-jdbc-3.51.3.0.jar          [ZERO 3.51.2.0 lines]

--- B3 (RECORD the glance + both count lines) -------------------------
  [OK] stopped
  [OK] launched pid 88724 -> /home/homesynapse/hs-bench/bench-2026-08-06-193742.log
  [--] waiting for a decisive radio state (up to 90 s)...
  [OK] RADIO UP after 12s
--- health tokens (current boot: /home/homesynapse/hs-bench/bench-2026-08-06-193742.log) ---
19:37:46.290 [hs-sub-registry_projection] INFO  c.h.l.RegistryProjectionSubscriber -- registry.projection_live: devices=6 entities=6 position=25065
19:37:46.746 [integration-supervisor-start] INFO  c.h.i.zigbee.ZigbeeAdoptionSlice -- zigbee.device_relinked: device=0xF044D3FFFED2A201 deviceId=01KXW0156Z1GJ3WCV2G516AKWS — re-pairing, no new adoption
19:37:46.747 [integration-supervisor-start] INFO  c.h.i.zigbee.ZigbeeAdoptionSlice -- zigbee.device_relinked: device=0x00178801101A09BB deviceId=01KX1PA4GRZHY2GD37B5CFVQHY — re-pairing, no new adoption
19:37:46.748 [integration-supervisor-start] INFO  c.h.i.zigbee.ZigbeeAdoptionSlice -- zigbee.device_relinked: device=0x449FDAFFFE688F57 deviceId=01KY12MQVQ204M1VP39F1ZDM33 — re-pairing, no new adoption
19:37:46.748 [integration-supervisor-start] INFO  c.h.i.zigbee.ZigbeeAdoptionSlice -- zigbee.device_relinked: device=0xF044D3FFFE9C78D7 deviceId=01KX1PB9A5931A8G0F0X03QXT2 — re-pairing, no new adoption
19:37:46.749 [integration-supervisor-start] INFO  c.h.i.zigbee.ZigbeeAdoptionSlice -- zigbee.device_relinked: device=0x00124B002FA8D1C5 deviceId=01KXW1W1RR66GV98D9QDPB4VXY — re-pairing, no new adoption
19:37:46.749 [integration-supervisor-start] INFO  c.h.i.zigbee.ZigbeeAdoptionSlice -- zigbee.device_relinked: device=0xF044D3FFFE1C1E8E deviceId=01KXW13WEGRCT5C0XSQT8WZBG9 — re-pairing, no new adoption
19:37:46.749 [integration-supervisor-start] INFO  c.h.i.z.ZigbeeIntegrationAdapter -- zigbee.adoption_maps_rehydrated: devices=6
19:37:54.455 [integration-zigbee-0] INFO  c.h.i.z.ZigbeeIntegrationAdapter -- zigbee.network_resumed: channel=20 panId=0x774c
19:37:54.455 [integration-zigbee-0] INFO  c.h.i.zigbee.EzspCoordinatorProtocol -- zigbee.network_up: stackStatusHandler reported EMBER_NETWORK_UP (buffered)
--- failure tokens ---
   [NONE]
[glance printed TWICE, byte-identical, same boot log — restart's own trailing
 glance + the explicit health call. Recorded once. Two reads of ONE boot.]
[device_proposed: ZERO. device_relinked: 6. All Expect tokens exact.]

$ ps ... | grep -c "sqlite-jdbc-3.51.3.0.jar"   ->  1
$ ps ... | grep -c "sqlite-jdbc-3.51.2.0.jar"   ->  0
*** DEPLOYED-JAR VERIFY GREEN. S-5a is a DEPLOYED fix, not desk-green. ***

--- B4 (RECORD verdict + bundle id) ----------------------------------
runner self-id: B3.1-2026-08-02-postwindow @ 16e672d
[PASS] boot-health — 6/6 positive · 0 forbidden
  [--] bundle: /home/homesynapse/hs-bench/bundles/boot-health-20260806T234011Z
[scenario ran its own `stimulus bench: restart` -> pid 88857 ->
 /home/homesynapse/hs-bench/bench-2026-08-06-193959.log]

--- B5 (RECORD both) -------------------------------------------------
$ cat ~/.config/systemd/user/nexsys-bench-nightly.service.d/killmode.conf
[Service]
# B3 night-1 finding (2026-08-01): Type=oneshot + the systemd default
# KillMode=control-group SIGTERMs the app the wrapper deliberately leaves
# RUNNING, ~0.4s after nightly.sh exits. The wrapper cannot assert its own
# aftermath -- verify-restored runs before the kill -- so the guard has to be
# structural. Unit-local by design: the cron fallback branch has no unit
# cgroup and never had this defect.
KillMode=process

$ systemctl --user show nexsys-bench-nightly.service | grep -E "^KillMode=|^Type="
Type=oneshot
KillMode=process
[survival fix LIVE. Nothing changed — read-only under K: (a).]

--- B6 (RECORD the lines + plug-in clock time) -----------------------
PHYSICAL ACT: Hue lamp plugged into a DIRECT WALL OUTLET and switched on
ONCE at 18:54:56 America/Chicago (+/- 0.5s; operator clock synced via
time.is, +0.9s offset, +/-0.019s) = 19:54:56 Pi-local.
NO relay. NO switched strip. NO 6x cycle. ONE power-up.

Three reads of the authorized grep:
  read 1 @ 18:57:00 CDT / 19:57:00 Pi = T+2:04  -> stale
  read 2 @ 18:59:00 CDT / 19:59:00 Pi = T+4:04  -> stale
  read 3 @ >=19:00 CDT (clock not captured)     -> stale  [>= T+5:04]

Output, identical on all three reads (newest line 19:40:03 = B4's boot):
19:40:03.541 ... zigbee.device_relinked: device=0xF044D3FFFE9C78D7 deviceId=01KX1PB9A5931A8G0F0X03QXT2 — re-pairing, no new adoption
19:40:03.542 ... zigbee.device_relinked: device=0x00124B002FA8D1C5 deviceId=01KXW1W1RR66GV98D9QDPB4VXY — re-pairing, no new adoption
19:40:03.542 ... zigbee.device_relinked: device=0xF044D3FFFE1C1E8E deviceId=01KXW13WEGRCT5C0XSQT8WZBG9 — re-pairing, no new adoption
19:40:03.542 ... zigbee.device_relinked: device=0xF044D3FFFED2A201 deviceId=01KXW0156Z1GJ3WCV2G516AKWS — re-pairing, no new adoption
19:40:03.543 ... zigbee.device_relinked: device=0x00178801101A09BB deviceId=01KX1PA4GRZHY2GD37B5CFVQHY — re-pairing, no new adoption

RESULT: ZERO fresh device_announce / device_relinked after the act.
        ZERO device_proposed. Clean negative, formally tested past T+5.
NOTE: `current.log` confirmed tracking the newest boot (its tail carries
      the 19:40:03 lines) — the negative is REAL, not a stale-symlink artifact.

--- B7 (RECORD all output) -------------------------------------------
$ ls ~/hs-bench/bundles/ | grep -E "settle-2026080(4|5)"
command-s31-settle-20260804T083138Z
command-s31-settle-20260805T083132Z

== /home/homesynapse/hs-bench/bundles/command-s31-settle-20260804T083138Z
api-captures.json  MANIFEST.txt  resolved.json  scenario.yaml  verdict.txt
scenario.yaml:# the disposition-agnostic terminal assert (data.terminal == true) is
scenario.yaml:# command's OWN terminal; the suite list places it immediately before
scenario.yaml:# real edge with a real inter-command gap (this scenario's terminal wait
scenario.yaml:# THE ASSERT is field_equals data.terminal == true: the settle command
scenario.yaml:# reaches SOME terminal — CONFIRMED when the relay was ON (a real
scenario.yaml:# honest, window ~5 s measured). EITHER terminal leaves the relay OFF.
scenario.yaml:# Non-vacuous (command-plane liveness to a terminal on real silicon) and
scenario.yaml:    - api:                        # SOME terminal, either disposition —
scenario.yaml:            field: "data.terminal"
api-captures.json: "body": "{\"data\":{\"commandId\":\"01KZ5YCG14KC0YJQZ2J5KP7QTE\",\"correlationId\":\"01KZ5YCG14KC0YJQZ2J5KP7QTE\",\"entityId\":\"01KXW1W1SBJZERC9MBAMV2DWKE\",\"capability\":\"on_off\",\"command\":\"turn_off\",\"lifecycle\":{\"ACCEPTED\":{\"at\":\"2026-08-04T08:31:32.388742Z\",\"eventId\":\"01KZ5YCG14KC0YJQZ2J5KP7QTE\",\"details\":null},\"DISPATCHED\":{\"at\":\"2026-08-04T08:31:32.391555Z\",\"eventId\":\"01KZ5YCG17DFP7V8J9957J5ST2\",\"details\":{\"integration_id\":\"6V1CMGY2HKF4H1FGZ4H7F257FS\"}},\"CONFIRMATION_TIMED_OUT\":{\"at\":\"2026-08-04T08:31:37.977102Z\",\"eventId\":\"01KZ5YCNFRWNEBQQYB43YCWZR8\",\"details\":null}},\"currentPhase\":\"CONFIRMATION_TIMED_OUT\",\"terminal\":true},\"meta\":{\"viewPosition\":65853,\"timestamp\":\"2026-08-04T08:31:38.427517350Z\"}}"

== /home/homesynapse/hs-bench/bundles/command-s31-settle-20260805T083132Z
api-captures.json  MANIFEST.txt  resolved.json  scenario.yaml  verdict.txt
scenario.yaml: [9 comment lines byte-identical to the Aug-4 bundle above]
api-captures.json: "body": "{\"data\":{\"commandId\":\"01KZ8GS6K6HBAH64S8P8AN4QXA\",\"correlationId\":\"01KZ8GS6K6HBAH64S8P8AN4QXA\",\"entityId\":\"01KXW1W1SBJZERC9MBAMV2DWKE\",\"capability\":\"on_off\",\"command\":\"turn_off\",\"lifecycle\":{\"ACCEPTED\":{\"at\":\"2026-08-05T08:31:31.942634Z\",\"eventId\":\"01KZ8GS6K6HBAH64S8P8AN4QXA\",\"details\":null},\"DISPATCHED\":{\"at\":\"2026-08-05T08:31:31.948773Z\",\"eventId\":\"01KZ8GS6KCY2KQWCZBHQ3S1JJ6\",\"details\":{\"integration_id\":\"6V1CMGY2HKF4H1FGZ4H7F257FS\"}},\"CONFIRMED\":{\"at\":\"2026-08-05T08:31:32.100412Z\",\"eventId\":\"01KZ8GS6R47Q09RM9V4CTG01VB\",\"details\":{\"match_type\":\"exact\"}}},\"currentPhase\":\"CONFIRMED\",\"terminal\":true},\"meta\":{\"viewPosition\":68598,\"timestamp\":\"2026-08-05T08:31:32.958406629Z\"}}"

SETTLE TERMINALS (hub-ratified):
  Aug-4: CONFIRMATION_TIMED_OUT @ 08:31:37.977  (~5.59s)  terminal:true  HONEST
  Aug-5: CONFIRMED @ 08:31:32.100 (match_type exact, ~158ms) terminal:true
  Same entity 01KXW1W1SBJZERC9MBAMV2DWKE, on_off/turn_off, both nights.
  Assert is disposition-agnostic -> BOTH satisfy it. Neither is a failure.

$ grep -n "port_unh
   device_relinked x6 · adoption_maps_rehydrated devices=6 ·
   network_resumed channel=20 panId=0x774c · failure tokens NONE]

[HUB FILING NOTE: truncation seam in the as-received paste — the S-4 grep
 echo cuts above and the record resumes inside B8; the full S-4 grep output
 (30 tail-capped hits, uniform cause=read-error) is held by the hub from the
 operator's raw terminal transcript and is adjudicated in the audit.]

[PASS] boot-health — 6/6 positive · 0 forbidden
  [--] bundle: .../bundles/boot-health-20260807T001134Z
[SKIP] command-confirm — SKIPPED: [hue-online] — HUE-RESET pending — the Hue is unpowered: its lamp rode the S31 relay (measured 2026-07-29); the lamp is now unplugged from the S31, so the Hue is deterministically off-network
  [--] captured command_id = '01KZCRZ5VMJ6AKDKPYFP2M3PQ3'
[PASS] command-timeout-absent — 1/1 positive · 0 forbidden
  [--] bundle: .../bundles/command-timeout-absent-20260807T001140Z
  [--] captured first_command_id  = '01KZCRZBTH04QWQCKPMD66KB56'
  [--] captured second_command_id = '01KZCRZBV074ES4SHC253VQPRJ'
[PASS] command-supersession — 2/2 positive · 0 forbidden
  [--] bundle: .../bundles/command-supersession-20260807T001146Z
  [--] captured command_id = '01KZCRZHT39ECDCJPPJMJK2YMK'
[PASS] command-identify-honest — 1/1 positive · 0 forbidden
  [--] bundle: .../bundles/command-identify-honest-20260807T001147Z
  [--] usb cycle: uhubctl -l 3-2.4 -p 2 -a cycle -d 10
[PASS] usb-reenumeration — 2/2 positive · 0 forbidden
  [--] bundle: .../bundles/usb-reenumeration-20260807T001202Z
  [--] let current_brightness = 50
  [--] captured command_id = '01KZCS01K3GMGWY3ZP0K50BAJG'
[PASS] timeout-honesty-no-change — 2/2 positive · 0 forbidden
  [--] bundle: .../bundles/timeout-honesty-no-change-20260807T001208Z
  [--] captured command_id = '01KZCS07J958P0J12SPFE21DJS'
[PASS] command-confirm-s31 — 2/2 positive · 0 forbidden        <-- POSITION 8
  [--] bundle: .../bundles/command-confirm-s31-20260807T001211Z
  [--] captured settle_command_id = '01KZCS0AJCHQSR1EE4KA6QKKB3'
[PASS] command-s31-settle — 1/1 positive · 0 forbidden          <-- LAST
  [--] bundle: .../bundles/command-s31-settle-20260807T001212Z
ran 8/9 — 1 SKIPPED: [hue-online]

*** THE TRIP'S CORE EVIDENTIARY PRODUCT, DELIVERED: ***
8 run legs PASS, ZERO FAIL, ZERO forbidden, on core 3723e31 with
sqlite-jdbc-3.51.3.0 PROVEN live on the running classpath.
NO REGRESSION from the S-5a + S-5c deploy.

=========================================================================
ANOMALIES / FINDINGS
=========================================================================
A1  [HUB-OWNED PACKAGE DEFECT, acknowledged] GOAL wording "verifies the s31
    fix on the NEW build". The s31 fix was B3.3, bench-side (leg moved
    position 3 -> 8, 41a7a3c -> 16e672d), banked v46 beat 5. S-5a/S-5c are
    unrelated hardening. Conductor STOPPED at B1 on the resulting apparent
    anomaly; hub ruled NO ANOMALY and is minting a package-authoring rule.

A2  [HUB-OWNED PACKAGE DEFECT, acknowledged] "ON-latency present" asserted
    on the LIVE SUITE surface. Source-verified: the digest line is written
    only by the nightly wrapper (tools/nightly.sh -> nightly_digest.py ->
    ~/hs-bench/digests/nightly.log). An attended `suite auto` writes none.
    Known glance-semantics class. `bench.sh digest 1` was proposed by the
    conductor as an operator-authority option, then STRUCK by the hub as
    the wrong instrument. Never run.

A3  [HUB-OWNED PACKAGE DEFECT, acknowledged — THE HEADLINE] The premise
    "Hue re-power un-SKIPs hue-online -> 9/9" was never verified at source.
    scenarios/constants.yaml :137-:144 sets capabilities.hue-online.available
    = false as a STATIC pre-authored predicate minted at the B2 re-mint. The
    runner NEVER probes the Hue; the reason text is narrative, re-grounded
    2026-07-29, and prints unchanged regardless of physical state. The
    constants block documents this exact shape as expected. **9/9 was
    UNREACHABLE ON THIS TRIP BY CONSTRUCTION.** Flagged by the conductor
    from the SKIP text at B8 before hub confirmation.
    Operator executed the correct physical half (constants :50 — HUE-RESET =
    plug the lamp into wall power). The gate half (flip the constant +
    re-ground the reason) is a post-trip ruled bench micro-edit, gated on
    the Hue proving alive. Tonight's nightly stays at the LAWFUL 8/9 bar.

A4  [package wording, minor] B3 Expect says the restart "self-reports
    HEALTHY". No literal HEALTHY token is emitted. The decisive-state report
    is [OK] stopped / [OK] launched pid N / [OK] RADIO UP after 12s with
    empty failure tokens. Called PASS on substance; string gap logged.

A5  [benign] The health-token block prints TWICE per restart invocation
    (restart's own trailing glance + the explicit health call). Two reads of
    one boot, byte-identical.

A6  [operator sequencing, no impact] B6's grep was first run BEFORE the
    physical act. Read-only, harmless, superseded. Caught by the Expect check.

A7  [record precision] B6 read 2 landed at T+4:04 — 56s short of the
    package's "nothing after 5 min" rule. A third read at >=T+5:04 was taken
    so the rule was FORMALLY tested rather than assumed. Result unchanged.

A8  [OPEN — see HUB ASKS] B7's S-4 grep is `tail -30` capped and returned
    EXACTLY 30 lines => front-truncated in glob order (bench-5b-* sorts
    last, so the oldest bench-2026-07-* files were cut). cause=read-error is
    uniform ACROSS THE LAST 30 HITS ONLY. NOT proven exhaustive.

A9  [RESOLVED — offered for hub confirmation] Conductor flagged nightly logs
    carrying port_unhealthy stamps EARLIER than their own filename launch
    stamp (e.g. bench-2026-08-02-043139.log:59 at 04:30:13, 86s "before"
    launch). Resolution: log lines carry HH:MM:SS with NO DATE. The app
    launched Aug-2 04:31:39 survived the night and was torn down by the
    Aug-3 nightly at 04:30:13. Identical shape to today's ...043135.log at
    19:37:35, torn down by the B3 stop. This extends the hub's REV-1
    shutdown-window race ruling from 2 observed samples to the full 30-line
    corpus — one hit per surviving app, every time.

A10 [OPEN — see HUB ASKS] H-A2 returned EMPTY. Probable instrument artifact
    (backslash-escaped JSON vs unescaped pattern), evidenced by B7's own
    body bytes. ON-latency for this rep UNVERIFIED. No corrected command
    authored or run by the conductor.

A11 [environmental, for correct filing] Pi local clock = UTC-4; operator
    wall clock = America/Chicago (UTC-5). Pi log stamps read +1h from the
    operator's watch. Bundle IDs are UTC and crossed midnight mid-trip:
    B4's bundle is 20260806T234011Z, B8's are 20260807T00xxxxZ, against Pi
    log stamps of 19:40 and 20:11 on Aug-6. TIMEZONE, NOT MISFILING.

A12 [scope] Trip executed the evening of Aug-6; package scoped Aug-8/9.
    Operator-elected early execution. B1's digest gate was read against the
    Aug-6 04:30 nightly (the night before execution) and passed.

=========================================================================
HUB ASKS (open, for hub authorship — conductor issued nothing)
=========================================================================
HA-1  The S-4 grep's tail -30 truncation (A8): is cause=read-error uniform
      across the FULL corpus, or only the last 30 hits? A wider read would
      close it. REV-1's residual is answered for the sampled window only.
HA-2  A corrected extraction pattern for the s31 bundle's lifecycle stamps
      (A10), so this rep's ON-latency can join or be excluded from C4.
HA-3  The next physical step for the Hue. It has NOT been observed
      on-network since the 19:54:56 wall-power act (H-A1 empty). Nothing
      further has been done to the lamp and nothing will be without a ruling.
HA-4  Sequencing of the A3 bench micro-edit (flip hue-online + re-ground the
      reason) against HA-3 — the edit is gated on the Hue proving alive,
      and the Hue has not yet proven alive.

=========================================================================
ANTI-ACTION COMPLIANCE ATTESTATION
=========================================================================
scenarios/constants.yaml ......... UNTOUCHED (read about, never opened/edited)
every bench scenario file ........ UNTOUCHED
~/nexsys-bench ................... NO EDITS of any kind
Pi reboot ........................ NONE (never ruled, never taken)
Hue re-power ..................... ONE power-up, DIRECT WALL OUTLET.
                                   No smart relay. No switched strip.
                                   NO 6x cycle. Lamp untouched since.
Abort ladder ..................... NEVER INVOKED (no B2/B3 failure)
Improvised commands .............. NONE. Every command run came from the
                                   package or the hub addendum, verbatim.
                                   `bench.sh digest 1` proposed to operator
                                   authority, struck by hub, not run.
Conductor file edits / commits ... NONE
Conductor adjudications .......... NONE. Every STOP routed to the hub.
API tokens in this package ....... NONE. No api token appeared in any
                                   captured output; nothing was redacted.

=========================================================================
FINAL STATE: Pi core HEAD 3723e31 · app pid 89068 · active log
/home/homesynapse/hs-bench/bench-2026-08-06-201121.log ·
lib/ sqlite-jdbc-3.51.3.0.jar · K: (a)

intakes as the next v47 hub beat.
=========================================================================

[POST-RETURN ADDENDUM, filed by the hub with the return — the two H-A reads'
 raw results, received after the package assembled:]

H-A1 (Hue liveness since the 19:54:56 act) — re-run at the hub's block:
  bench-2026-08-06-193959.log:37 19:40:03.543 device_relinked 0x00178801101A09BB (boot-time registry rehydration, PRE-act)
  bench-2026-08-06-201121.log:33 20:11:25.772 device_relinked 0x00178801101A09BB (boot-time registry rehydration, 20:11 boot)
  ZERO device_announce lines. ZERO Hue radio-layer activity post-act.
  VERDICT (hub): the Hue has NOT been observed on-network since re-power.

H-A2 (rep ON-latency from bundle command-confirm-s31-20260807T001211Z) —
  EMPTY output. Adjudicated at the bytes: the bundle JSON escapes quotes
  (\"ACCEPTED\") and the hub's pattern demanded unescaped quotes — a
  HUB-authored instrument defect (the A10 hypothesis CONFIRMED). The
  corrected read is authored in the v47 beat-3 follow-up block.

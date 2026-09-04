<!--
file: context/audits/2026-09-04_R-4b_intake_two-layer-audit_v62-beat-7.md
purpose: THE HUB'S TWO-LAYER INTAKE AUDIT of the R-4b operator record (context/audits/2026-09-04_R-4b_re-rep_operator-record.md, 110,016 B, filed by the R-4b navigator, closed 20:45Z). Layer 1: the record's claims read critically. Layer 2: the hub's own re-execution — against Nick's verbatim terminal paste (the primary), and at source for every code claim the record makes. The C-002 mint decision; the record-size ruling; the findings routed to docket rows; the packet's own defects owned.
audience: the hub · Nick · the C-002 row · the docket addendum
state-type: intake audit
status: FILED at v62 beat 7 (Fri 2026-09-04, instrument 20:5xZ = 15:5x CT). VERDICT: ACCEPT — FOUR OF FOUR; CRITERION 0 MET ON BOTH ARMS; C-002 MINTS (narrow-worded on the measured objects; the fleet sentence becomes the C-003 slot). Record size ACCEPTED as filed (ruling §4).
-->

# R-4b — intake audit (v62 beat 7)

## §0 Verdict
**ACCEPT. FOUR OF FOUR on the R4b-4 gate; criterion 0 MET and — the day's second headline — its MISS arm measured on the same rig in the same session.** C-002 MINTS at `ef02d13`, worded on exactly what rendered (Path B; `CONFIRMED`); the six-device-fleet sentence the slot carried is NOT what was measured and becomes the C-003 slot (fenced to R-4c + the ZDO `IEEE_addr_req` WU). PKG-SEC-2 is PROVEN on hardware (`Configuration issue` = 0; the schema line once, `stage=pre-load`). The bench floor is back `[PASS] 6/6` and the 09-04 nightly read 8/9. Zero STOPs; 13 deviations, all T1/T2, all filed the same minute — the navigator license worked as designed.

## §1 Layer 2 — re-executed by the hub
| Claim (the record) | Instrument | Result |
|---|---|---|
| Criterion 0 HIT: `17:51:15.203Z zigbee.rejoin_candidate: device=0x00124B002FA8D1C5 nwk=0xf87d source=unknown_sender` → `device_proposed … source=rejoin status=COMPLETE` → `proposal_accepted source=config` → `device_adopted deviceId=01M1PRQMZHFV4SAWT1E96B9BQ2 entities=1` (315 ms) → `reporting_configured clusters=1 verified=0 degraded=1` | Nick's paste (EDT lines 13:51:15.203/.435/.440/.518; 13:51:20.649) | ✓ IDENTICAL (EDT = Z−4; the record's Z stamps correct) |
| Criterion 0 MISS: `18:28:41.461Z zigbee.lookup_eui64_failed: nwk=0x15ac status=0x1` + `rejoin_candidate_unresolved: nwk=0x15ac cluster=0x402 reason=lookup_miss`; 8 unknown-sender frames from 0x15ac → 1 lookup, 1 WARN | Nick's paste (14:28:41.461/.462 EDT; `8 ingestion_unknown_sender: nwk=0x15ac`) | ✓ IDENTICAL; the once-per-epoch dedup (`rejoinLookupAttempted`, F-R4-1 T7) confirmed on silicon |
| The windows: `permit_join_opened: duration=254s` at 17:50:42.200Z and 18:25:42.749Z; no clamp; `network_formed` 0 on every start | Nick's paste | ✓ |
| §5 PKG-SEC-2 proof: `Configuration issue` count 0 · `lifecycle.integration_schema_registered: type=zigbee stage=pre-load` ×1 · `network_resumed` ch20 PAN 0x774c · formed 0 | Nick's paste (INV 2a6c8ca0…) | ✓ — R-4's C-1 is GONE on hardware |
| §4 install: `0.1.0+git20260903.124041.gef02d13` twice; ROWS 107→109; integrity ok; no downgrade | Nick's paste | ✓ (the postinst first-run banner printed on an UPGRADE again — R-4's O-1, cosmetic, standing) |
| C4: run `01M1PX64EREVX8XAVACQNZNQGG` `COMPLETED`, triggeredAt 19:09:04.323Z, `durationMs 10051`, `actions[0].outcome: "CONFIRMED"`, `settled: true`; `lastRunId` set | Nick's paste (`/api/v1/runs` + `…/causal-chain`) | ✓ |
| C3: ROWS-W0 173 @ 19:08:58Z → ROWS-W1 212 @ 20:09:35Z; discriminator 0; resumed 1; formed 0 | Nick's paste | ✓ (+39 in 60 m 37 s) |
| C2: `state_reported` at 20:03:57 · 20:08:57 · 20:13:57 · 20:18:57 (subject 01A06D8BD403… = the S31 entity); 3/3 AVAILABLE `stale:false` at 20:22:55Z; the in-window census incl. `state_confirmed` ×1 (pos 186), `command_issued`/`command_dispatched` ×1, `availability_changed` ×1 (pos 188) | Nick's paste | ✓ |
| The stop grade on `ef02d13`: `Result=exit-code · ExecMainStatus=143 · ActiveState=failed` | Nick's paste (20:25:45Z) | ✓ — O-2/§6-B confirmed on a SECOND artifact; the FAILCHAN proof is owed (its CI is red) |
| The restore: `bench.sh start` RADIO UP 22 s; `[PASS] boot-health — 6/6 positive · 0 forbidden`; PAN 0x774c; by-id string byte-identical; bundle `boot-health-20260904T203821Z` | Nick's paste | ✓ |
| The 09-04 nightly: `8/9 PASS · 1 SKIP(hue-online) · bench-hero RESTORED ✓ · ON-latency 0.32s`; bundles `command-confirm-s31-20260904T083155Z` / `command-s31-settle-…083156Z` | Nick's paste | ✓ — the floor held (the s31 leg PASSED) |
| D-12: the real read routes | `RestFilters.java:348` `app.get("/api/v1/runs"` · `:350` `app.get("/api/v1/runs/{runId}/causal-chain"` · `GetNonFiringEndpoint` `/api/v1/automations/{id}/non-firing` | ✓ — the packet's `/api/v1/runs/{id}` was the hub's invention (owned) |
| F-R4b-F: `0x15ac` cluster `0x0402` = the SNZB-02P (temp/humidity) | `zigbee-profiles.json:153` inClusters `0x0402`,`0x0405` | ✓ plausible attribution (the profile with 0x0402+0x0405); the device identity is by cluster, not by EUI64 — recorded as "the router-parented sleepy device" |
| D-3: the config root is `/var/lib/homesynapse/config` (`HOMESYNAPSE_HOME`), not `/etc/homesynapse/config` | the unit `:36–:40` (the CURRENT-ARTIFACT path model); Nick's `ls -la` (only `homesynapse.env` under /etc) | ✓ — the packet's path was WRONG in §3/§6/§7 (the hub's instrument defect; R-4's D-f had already shown it) |
| Not re-executed | the bulb's physical power (the operator's own ⏺ "lamp lit within half a second"); the sha256 on the desktop (the record's three-surface identity) | the operator's word; consistent with the .deb Version on the card |

## §2 Layer 1 — the record read critically
A 110 KB record with a one-screen §0 verdict surface (the four criteria with evidence; the per-section table; the census of 37 ⏺s; 13 deviations; 10 asks) and a §9 findings card of five design-grade points. The navigator took ONE operator-proposed act beyond the packet's literal text (D-10, the Hue powered through the adopted S31, closed inside a second window) and justified it correctly against the packet's own branches; the fence (one Hue power cycle) was honoured. It read the harvest at the token, named the branch, and produced the miss arm's status byte on the first attempt — exactly what the packet said was "the one thing no desk could measure." Its five defect findings against the packet are all TRUE and all the hub's: the config path (D-3), `head`/`tail` for absence (D-6), the half-fixed token regex (D-9), the invented route (D-12), the gate sharing a block with its act (D-13). The self-timing window block (D-8) is adopted as the standing pattern.

## §3 Rulings
- **C-002 MINTS — on the measured objects, not the slot's text.** The slot said "the six-device fleet RE-ADOPTED … + the automation"; the record measured ONE silent-rejoining mains device adopted through the rejoin path and ONE automation fired with its command CONFIRMED by the device's own report, four-of-four on the R4b-4 gate as the packet defined it (C4 = "a device adopted TODAY"). The register's law is exact scope: C-002 is worded on that; the fleet sentence becomes the **C-003 slot**, fenced to R-4c (after the ZDO `IEEE_addr_req` WU — the miss arm proves the fleet's sleepy devices cannot be re-adopted by 0x0061 alone). Nick's word: Row 12 (a) + the plan §0-ter ("C-002 mints on four-of-four") + the packet dispatched; refutable by his REVERT.
- **The record size — ACCEPTED as filed, and the cap re-cut:** the cap applies to §0 + §9 (the two screens the hub reads, ≤14 KB together — met: ~9 KB); the drill-down (§1–§8) is evidence and is uncapped. No trim.
- **P-1 (the power-harness primitive) — a charter candidate in its own right, ACCEPTED for the docket** (row 28): the plug as a software-addressable, self-confirming mains switch; protocol-independent; the safety limits (`maxCyclesPerWindow`, `minSecondsBetweenCycles`, load, settle) enforced in code. Nick's word at the R-5 charter or earlier.
- **Playbook §6 "Hue LCA017: wall power-cycle ⇒ re-announce" → CONTESTED** (three failures; today's under instrumented conditions; the bulb is absent from the air — F-R4b-G). A docket row (29) + the playbook line demoted at the close.
- **F-R4b-H (read-API shape gaps: `trigger.firingValue` null on a matched trigger; `actions[].resultOutcome` null beside `outcome: CONFIRMED`)** → a docket row (30) against the FROZEN v1.1 contract — likely CG-class (additive), adjudicated with CG-1/2/3.
- **F-R4b-E (`entity_registered` not in the journal though the entity registered)** → a docket row (31); the packet's §7 mapping step rewritten to read `/api/v1/entities` deltas.
- **F-R4b-C (`reporting_configured … verified=0 degraded=1` on a MAINS device)** → a docket row (32); unexplained; not a stop.
- **The availability flap on `01M19RHWXYZYJMM26SX0E41HXN` (UNAVAILABLE at 18:08Z, AVAILABLE at 20:22Z; `availability_changed` at pos 188)** → a docket row (33) for R-4.5/R-5 (the settle/availability redesign).
- **O-2 / §6-B confirmed on `ef02d13` too** — recorded on OR-FAILCHAN; the FAILCHAN proof waits on FAILCHAN-FIX-1's green.

## §4 The hub's own defects, owned (fold at the close)
1. The config path `/etc/homesynapse/config` in §3/§6/§7 — never re-derived against R-4's own D-f; the unit's own comment names `$HOMESYNAPSE_HOME`. **Lesson: every path in an operator packet is re-derived against the prior record's deviations AND the unit, never carried forward.**
2. `/api/v1/runs/{id}` invented — the playbook's own rule ("never name a subcommand/flag you have not verified exists") violated by the hub. **Lesson: routes and verbs are read at the source table before they enter a packet.**
3. `head`/`tail` used to assert absence/uniqueness (§5) — **counts, never heads.**
4. The token extraction half-fixed (the gate, not the regex) — **fix the mechanism the prior record named, not its symptom.**
5. The stop grade and the shutdown in one block — **a gate never shares a block with the act it gates.**
6. The hand-timed window — **self-timing blocks for every windowed provocation** (D-8 adopted).

## §5 What lands where
- `claim-register.md`: C-002 LIVE (this beat) · C-003 SLOT (fleet; R-4c) · the status line.
- The docket: Row 12 CLOSED · rows 27–33 named for the addendum (F-R4-1b · P-1 · the Hue · the API shape gaps · entity_registered · reporting degraded · the availability flap).
- OR-FAILCHAN: §6-B confirmed across two artifacts.
- The September plan §0-ter: R-4b DONE; C-002 LIVE; the fleet → R-4c.
- The record §10: the hub's verdict surface (this audit's §0).
- The playbook + the packet pattern: at the close (the mints).

## §6 Post-audit corrections (v62 beat 8, the close — 2026-09-04 ~16:52 CT)
- **F-R4b-F, the device identity (§1 row 13):** `nwk=0x15ac` = the **SNZB-02P `0xF044D3FFFED2A201`** — Nick's device mapping (09-04), replacing "plausible attribution by cluster". The SNZB-03P is adopted, so its ACT-2 wave never reached the unknown-sender arm; that evidence is on the held card's journal (down now; read at the next power-on). The row's conclusion (the router-parented SLEEPY device misses 0x0061) is unchanged.
- **Row 33's entity→device mapping:** given by Nick in the same message; lost verbatim at the hub's compaction; NOT written from memory — v63 asks for one line and writes it then.
- **Nick's word on the mint: `C-002: STANDS`.** P-1: `charter` (a bench row after CG; safety limits in code — §3's third ruling executes).

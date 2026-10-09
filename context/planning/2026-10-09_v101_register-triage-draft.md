<!--
file: context/planning/2026-10-09_v101_register-triage-draft.md
purpose: the register triage DRAFT by a read-only grounding agent (D12) at v101 post-close beat 5 — every OPEN row of context/planning/improvement-register.md with a proposed bucket (PRE-RUN · POST-RUN · RETIRE) and its reason. The hub RULED the buckets in context/planning/2026-10-09_v101_PLAN-AHEAD_freeze-list_rulings_and-triage.md §4 (D-v101-27): 19 · 59 · 11 RETIRE now + 5 RETIRE-PENDING a Saturday reading (IR-113 · 115 · 117 · 118 · 123 are PENDING, not RETIRE, in the ruling); the ruled bucket is the tag on each register row. The agent's reasons are the agent's; the hub's rulings outrank them where they differ.
audience: the hub (the proposal it ruled) · Nick (`TRIAGE: adopt` retires the eleven; `REVERT IR-n` per row)
state-type: planning input (an agent's draft; never edited after filing)
status: FILED — v101 beat 5 (Fri 2026-10-09 ~13:5x CT; instrument 2026-10-09T18:53:19Z); ruled in the PLAN-AHEAD pass §4
-->

# Register triage draft — the OPEN rows (v101 b5, Fri 2026-10-09)

Source: `context/planning/improvement-register.md` (136,603 B, 150 lines). **138 rows total; 94 OPEN** (status cell leads with `OPEN`). Not counted: 19 older rows whose cell carries `status OPEN` mid-cell but leads with a date/unit word and names no closing sha (IR-4 · 5 · 6 · 7 · 10 · 11 · 16 · 17 · 18 · 19 · 20 · 21 · 26 · 27 · 29 · 30 · 31 · 32 · 89) — the hub may want a second sweep of those under the same buckets.

Buckets: **PRE-RUN** = must land before the freeze (Oct 22–23) or the run (Oct 30 – Nov 2) needs it · **POST-RUN** = can wait past Nov 2 · **RETIRE** = absorbed by a landed unit (named) or no longer true. Gists quote the row's own words.

| id | surface | gist | carried-by | bucket | reason |
|---|---|---|---|---|---|
| IR-33 | core zigbee shutdown hook | closes the serial port under a read loop never told to stop | — | POST-RUN | row says the grade is clean either way; a small adapter WU after the run |
| IR-34 | core automation engine journal | a run leaves NO line in the journal at INFO | — | POST-RUN | observability; the run's grade reads the store; the "did it confirm" story is HERO-1's |
| IR-35 | research naming-frame ASR rig | control scores did not reproduce at KO-2 in either configuration | — | POST-RUN | research-lane hygiene; binds the next knockout's charter, after the run |
| IR-36 | core zigbee EzspReportingOps tests | every hardware-free instrument replies from the constants under test | — | POST-RUN | test hygiene; trivial; no run dependency |
| IR-37 | core ZigbeeHardwareFreeRig encoders | author-shaped, unpinned against captured frames | — | POST-RUN | test hygiene; captured-frame fixtures after the run |
| IR-38 | core lifecycle ITs TestClock | with every event at one instant the time-window hint covers the whole log | — | POST-RUN | test-fixture default; trivial |
| IR-41 | core zigbee adoptIfAccepted | the ONLY path that runs the metering formatting reads | — | POST-RUN | the slice-only path is not the run's adoption path |
| IR-42 | read-API wire / Doc 09 | the entities list body carries NO pagination key while the automations list does | — | POST-RUN | a freeze-text asymmetry on the FROZEN contract; a Doc 09 sentence after the run |
| IR-43 | web-ui dashboard mock | write targetRef.type: 'ENTITY' where the wire serves entity | — | POST-RUN | frontend mock; HERO-1/U2a's lane |
| IR-45 | core LINK-READ-2 / availability v2 | the read surface carries no per-device link field | J1 | RETIRE | cell leads OPEN but says CLOSED as LINK-READ-2 — LANDED df2bc62; residue = IR-118 (landed) and J1b |
| IR-46 | core zigbee ZclIngestionUnit / productionLoop | a throw in any handler ends run() and drops the cycle's drained frames | — | PRE-RUN | 72-h safety: one handler throw stops ingestion; decide fail-fast vs survive on J3/CONFIG-ERROR-1's adapter sitting |
| IR-47 | core zigbee exchange path | exchange-consumed responses are neither counted by LINK-READ's counter nor read for their LQI/RSSI | — | POST-RUN | link-reading completeness; an improvement |
| IR-48 | core persistence SqliteEventStore | the other LIMIT ? reads have indexes matching their ORDER BY but unpinned plans | — | POST-RUN | plan-pin tests; IR-40 fixed the measured hot read |
| IR-49 | core persistence SqliteEventStore | the LIMIT 1 time-range sibling — a covering-index plan by the planner's choice, unpinned | — | POST-RUN | trivial; a pin + the Javadoc |
| IR-50 | docs repo backup layout | no product backup-layout convention | — | POST-RUN | a docs sentence; BACKUP-1 (Mon 10-12) fixes the layout in practice — its card should confirm the arm's path |
| IR-51 | bench command-confirm-s31.yaml | the confirm leg sends its turn_on without establishing OFF first | — | PRE-RUN | small bench row; splits precondition-unmet from confirm FAIL before the run's S31 grading (IR-88) |
| IR-52 | bench runner A-9 | one post-window /state read ~0.9 s after a failed terminal | — | PRE-RUN | IR-88 names these reads as the instrument deciding the S31's timeout class before the run |
| IR-53 | core device-model StandardCapabilities | on_off's confirmation window 5,000 ms against the S31's PASS latencies | — | POST-RUN | row says no change before the cause (IR-51/52); a window decision after the run's data |
| IR-54 | hivemind research-return census | a source census written where a claim census belongs | — | POST-RUN | research-opener process; no code |
| IR-55 | hivemind research cite rule | a compound premise cites one file for both halves | — | POST-RUN | process rule; no code |
| IR-56 | core zigbee silent resume | a cached, listed, un-adopted device that resumes silently is never re-proposed | — | RETIRE | no Java unit (D-v85-12); the listed re-proposal landed as J2a (IR-114); the power-cycle question is IR-128 |
| IR-57 | bench test_engine BM1b T3 | reads the bands from the REAL constants.yaml while its scripted inputs are the charter's | — | POST-RUN | selftest hygiene; the re-mint card habit covers it; METER-2 never cut |
| IR-58 | bench metering-known-load.yaml | CHAR-BEFORE is confirm: enter with no typed datum | — | POST-RUN | CHAR scenario, not the run; METER-3 landed (58b5b45, IR-75) — unverified whether it carried this |
| IR-59 | bench constants.yaml bands | the band's quantization term is HALF the plug's step | — | POST-RUN | a CHAR-band decision at the 40 W load; the run reads household loads (IR-106) |
| IR-60 | core zigbee AshSession CRC | zigbee.ash_frame_rejected: CRC mismatch 19 times in 3.5 h | — | RETIRE | superseded by IR-136 (the same reading with the soak's numbers); one bench field |
| IR-62 | research DEVICE-SET accuracy rows | the TR3 read +7.1…+8.9 % over A − TARE | — | POST-RUN | the policy was given — BIAS: tolerate (D-v83-3, IR-75); the docs rewrite can wait |
| IR-63 | core permit-join key; bench boot-health | the pairing window is a CONFIG KEY that re-arms at every boot | — | RETIRE | PJ-2 landed (core 146468c per IR-101/107); the grader's A1a reads the key (IR-107); BH-2's boot-health half unverified |
| IR-64 | hivemind bench-card template B2 | prints the backgrounded &&-list's pid and an empty stamp | — | POST-RUN | cosmetic; the poll finds the real log by ls -t |
| IR-65 | hivemind strategic-context-map | the map's wayfinding rows name retired trees | — | POST-RUN | hivemind hygiene; BEAT-RENDERER-2's era |
| IR-66 | docs repo status: lines | 132 of 182 .md files carry no status: line | — | POST-RUN | docs hygiene; HIVE-CLEAN-3 ran (v97 b1) — unverified whether it swept this |
| IR-68 | core zigbee ReportingConfigurator ladder | a sensor shows nothing until its first report | — | POST-RUN | an improvement after IR-61; the fleet is adopted and reporting |
| IR-69 | web-ui format.ts NUMBER | a NUMBER renders as String(v) with no unit | — | POST-RUN | frontend; HERO-1/U2a's lane |
| IR-70 | docs Doc 08 + 02 | no IlluminanceMeasurement row; Battery and DeviceHealth as the only optional capabilities | — | POST-RUN | docs; DOCS-1 (f7e8e72) may have carried it (IR-81's text) — check before cutting |
| IR-71 | core EntityType javadoc | the optional-capability sentences name neither the meters nor the measurements | — | POST-RUN | javadoc; rides IR-70 |
| IR-72 | core ZigbeeHardwareFreeRig wireType | no 0x0400 row; the rig cannot script a lux report | — | POST-RUN | test rig; with the first lux rig test |
| IR-73 | core ClusterHandlersTest | buildCommand_ingestionOnlyHandlersThrow omits 0x0400 | — | POST-RUN | test; ≤ 10 min inside the next zigbee unit |
| IR-74 | skills coder-instruction return rule | the return file's last line IS RETURNED <path> <bytes> | — | POST-RUN | skills law; a W-SKILLS pass after the run |
| IR-76 | rig the Pi's bench clone | pulled by no bench-deploy card | — | RETIRE | the BENCH-PULL block is card practice since BC8 (BENCH-PULL-7, IR-96); the digest half is IR-86 |
| IR-77 | rig the Pi's ~/hs-bench/config/ | something under config/ is written or renamed by a boot-health boot | — | PRE-RUN | read-only; BACKUP-1 should know what writes under config/; a Block 0b --time-style line on BC9/dry-run cards |
| IR-78 | core state-store StateProjection.create | 12 parameters; every new dependency widens a positional factory | — | POST-RUN | a refactor; the next state-store unit |
| IR-79 | core state store staleAfter | a device adopted and unplugged before its first report reads fresh forever | — | POST-RUN | inside IR-80's AMD; IR-68 first |
| IR-80 | docs Doc 03 §3.8 AMD | the staleness chain has no source for the device's VERIFIED reporting configuration | — | POST-RUN | an AMD; after the run (AVAIL-API-1 exposes the contract on the API, not this) |
| IR-82 | skills survey-line paste | transcribed as a summary, not pasted as the command printed it | — | POST-RUN | skills law; a W-SKILLS pass |
| IR-83 | core lifecycle boot ordering | the two projections replay concurrently at boot | — | RETIRE | the gate landed in IR-61b (BootOrderingGateIT per IR-91's text); the Pi reading is IR-91's |
| IR-84 | core lifecycle ITs fixture | a plain IT depends on a tagged one for a fixture | — | POST-RUN | test hygiene |
| IR-85 | core state-store MODULE_CONTEXT | the header's public-type count and :122 are stale | — | POST-RUN | a docs count; with IR-78 |
| IR-86 | bench nightly digest | names the core's outcome but not the BENCH sha it ran on | — | POST-RUN | a convenience; BENCH-PULL's card block prints the sha; a later renderer rider |
| IR-87 | web-ui stale badge (FE-116) | the dashboard renders neither stale nor staleAfter | — | POST-RUN | the row dates it after the run (FE-116, Nov) |
| IR-88 | bench VERIFY-72H grader grammar | a grader that reads every timeout as a failure inherits an ambiguity | — | PRE-RUN | V72B landed (ba846c2, IR-96) without it; the run's S31 timeouts need a named class before the grade |
| IR-90 | core config CONFIG-ERROR | a TYPE-WRONG value … the boot CONTINUES with no staleness and one config_error line | CONFIG-ERROR-1 | PRE-RUN | ruled fatal (D-v92-13); CONFIG-ERROR-1 is planned before the freeze |
| IR-91 | rig PI-PROBE-3 | the boot ordering gate has NO desk instrument | — | PRE-RUN | a read-only block on BC9/dry-run cards: the two catch-up lines + staleAfter non-null |
| IR-92 | core rest-api ApiResponse Javadoc | the Javadoc says SNAKE_CASE but the REAL /state wire is camelCase | — | POST-RUN | docs-only; a one-line rider if AVAIL-API-1 opens the file |
| IR-95 | core automation StandardActionExecutor | skips an UNAVAILABLE target with no event … the action completes success | — | PRE-RUN | ruled SKIPVOC: count (D-v92-13); J3 is the last Java slot; else the run records success for commands never issued |
| IR-96 | bench VERIFY-72H-B | the grader has no action-effect invariant | — | RETIRE | cell leads OPEN but ends CLOSED v96 b2 — landed ba846c2 (V72B) |
| IR-97 | docs event_time vs ingest_time | every row of an automation run carries the TRIGGER's event_time | HERO-1 | POST-RUN | ruled ACTTIME: ingest (a docs rule); HERO-1's charter reads the action rows; a column only if needed |
| IR-98 | skills pre-verification COUNT PIN | listed no COUNT PIN, so three test files outside the file table moved | — | POST-RUN | skills law; CONFIG-ERROR-1's instruction carries it by hand |
| IR-99 | skills status-code table | two status-code rules that disagreed | — | POST-RUN | skills law; a W-SKILLS pass |
| IR-100 | core persistence EventCategoryMapping | permit_join_opened and permit_join_closed persist with the [SYSTEM] category fallback | — | POST-RUN | ruled system-health (D-v92-13); one mapping line in the next persistence unit; harmless for the run |
| IR-101 | hivemind card commit gate | the ; lets the commit run after ANY earlier failure of the && chain | — | POST-RUN | the beat script already gates; splice_lib_v2 is the skills codification |
| IR-102 | core zigbee permit-join concurrency | two concurrency claims pinned by construction and observed by no test | — | RETIRE | (a) CLOSED v92 b6 at BC7b; (b) a race test only on a conflict never observed |
| IR-103 | core rest-api MODULE_CONTEXT count | a count copied forward | — | POST-RUN | a docs count; AVAIL-API-1's card is the next rest-api unit — regenerate there |
| IR-105 | hivemind pre-registration form | names a field the digest line does not print | — | PRE-RUN | packet law for SOAK-NIGHT-2/dry-run pre-registrations: every field names its SOURCE LINE (the avail: field just moved) |
| IR-106 | hivemind bench-card PLUGS@ | prints each plug's watts and no expected household load | — | PRE-RUN | a plugs-of-record line on the dry-run/run cards; zero code |
| IR-107 | bench grader attestation A1 | permit_join_opened inside a graded span now means an ENDPOINT window | — | RETIRE | cell leads OPEN but ends CLOSED v96 b2 — A1a/A1b landed ba846c2 |
| IR-108 | core rest-api entity view | renders NO entity capability list | — | POST-RUN | a v1.2 row; the dashboard's consumer named first (HERO-1) |
| IR-109 | core integration-api / runtime seam | the Javadoc claims the descriptor declares SCHEDULER/TELEMETRY; nothing enforces ownership | — | POST-RUN | a Javadoc + an ownership check; the next integration-runtime unit |
| IR-110 | core zigbee IAS_FAMILY | the classifier's THIRD IAS outcome binary_state is outside it | — | POST-RUN | no water/smoke/vibration device in the run's fleet; with IR-15's class |
| IR-111 | core zigbee reconcile hardening | reconcileCapabilities does not catch …; no test pins requiredServices() contains DISCOVERY | — | POST-RUN | (a) unreachable by construction; (b) a pin test; the next zigbee unit |
| IR-112 | rig the Hue (OR-HUE-REPORTING-DEAD) | JOINED and answers ZCL while UNAVAILABLE at the API; its attribute reporting is dead | J1 | PRE-RUN | J1's mechanism keeps it dark; the row's word: retired or replaced, never carried into the run; power-cycle + identify first |
| IR-113 | core zigbee reporting_configured INFO | no INFO line names the degraded cluster | J2 | RETIRE | absorbed by J2 (49455fc) via IR-123's per-cluster line — confirm at BC9's log; else re-open |
| IR-114 | core zigbee admission path | a device that JOINS before its IEEE is on adopt_devices is not adopted | J2 | RETIRE | the fix = J2a (the row's own word); J2 landed 49455fc |
| IR-115 | core zigbee transient-key WARN | zigbee.key_establishment_failed device=0xFFFF… WARN ≈ 4:57 after every permit_join_opened | J2 | RETIRE | J2b (49455fc) names it transient_key_expired; the row closes at BC9's read of the named line — pending tonight |
| IR-116 | bench tools/bench.sh pj_valid | refuses silently: a bad argument prints the usage line and exits 2 | — | POST-RUN | operator UX; the run opens no windows |
| IR-117 | rig the SNZB-06P24 sensor | FIVE zigbee.device_left inside 156 ms … five Leaves is a device resetting | — | RETIRE | the cause RE-ATTRIBUTED to power (D-v98-3); the residue is one REHEARSAL 3 packet row (the re-announce gesture) |
| IR-118 | bench nightly digest avail: | the nightly digest and boot-health cannot see a dark device | AVAIL-LINE-1 | RETIRE | landed cddac94 (+1b); closes when the field reads on a nightly; the boot-health assert is a residue row |
| IR-119 | core zigbee permit_join_closed log | no zigbee.permit_join_closed: line is logged | — | POST-RUN | cosmetic; the store has the event (IR-129's law); a rider on the next adapter unit at most |
| IR-120 | core/bench ASH crcRejects trend | nothing trends the counter | — | RETIRE | superseded by IR-136 (the per-boot count + a threshold); one bench field |
| IR-121 | core availability aging (J1) | availability does not AGE a silent device | J1 | PRE-RUN | mains half landed (df2bc62); the battery half reads at SOAK-NIGHT-2; F-6 re-cut PER CLASS rides BC9/dry-run packets |
| IR-122 | core zigbee config schema knobs | availability.mains_timeout_minutes … with NO Java reader — a dead knob | CONFIG-ERROR-1 | PRE-RUN | bundled into CONFIG-ERROR-1 (the row's word) |
| IR-123 | core zigbee reporting_cluster INFO | nothing shipped names WHICH cluster degraded at adoption | J2 | RETIRE | J2 landed 49455fc carrying IR-123 (the hub's landed list); the row named J2's lane only as a candidate |
| IR-124 | hivemind census TSV | abbreviated its stale column with … in 15 of 102 rows | — | POST-RUN | one charter sentence; the next census lane |
| IR-125 | skills test-clock paste-block | prescribes Clock.fixed(…), which cannot elapse a window | — | POST-RUN | skills; CONFIG-ERROR-1's instruction names the idiom by hand |
| IR-126 | core zigbee lastScopedPartner | lastScopedPartner is never cleared | CONFIG-ERROR-1 | PRE-RUN | bundled into CONFIG-ERROR-1's sitting (the hub's plan) |
| IR-127 | skills record-component survey | a record-component change broke the compile of integration-runtime's PairingWindowRoutingTest | — | POST-RUN | a skills clause; the next instruction carries it by hand |
| IR-128 | core zigbee join layer | the join layer is SILENT on a quick power cycle | CONFIG-ERROR-1 (the read) | POST-RUN | the source read rides CONFIG-ERROR-1's authoring; detection already lives in J1/AVAIL-SHAPE's frame layer; the merge unit waits |
| IR-129 | hivemind rig-packet EXPECT form | every EXPECT names its instrument (store · log · API) | — | PRE-RUN | packet law for the dry runs; its retire condition (SOAK-NIGHT-1's packet) is unconfirmed in the cell |
| IR-131 | skills W-SKILLS-11 candidates (a)–(f) | each a LAW change the hub does not make alone | — | POST-RUN | a W-SKILLS pass; (e) is Nick's word; BEAT-RENDERER-2's era |
| IR-132 | core rest-api lastSeenAt shape | one field, two shapes | CONFIG-ERROR-1 | PRE-RUN | bundled into CONFIG-ERROR-1's sitting (the hub's plan); the FROZEN contract's consumer reads both |
| IR-133 | core tracker / FE last-seen | J1's three keys stay None on a healthy, reporting mains device until its transition | HERO-1/U2a | POST-RUN | the row sends the product question to the FE charter first; AVAIL-API-1 adds different fields |
| IR-134 | core staleness vs availability | two freshness models disagree on one row | HERO-1/U2a | POST-RUN | a design note on U2a/HERO-1's surface |
| IR-136 | bench nightly ash-rejects field | the nightly's count of the token per boot; a threshold (per hour) | — | PRE-RUN | dongle-health measurement for the run: the per-boot ash-rejects: line + a pre-registered threshold (≈ 3/h at SOAK-NIGHT-1) |
| IR-137 | core zigbee availability probe | THE PROBE IS UNANSWERED 7 OF 7 on the plug class | AVAIL-SHAPE → PROBE-ANSWERED-1 | PRE-RUN | instrument landed 37f05a9; SOAK-NIGHT-2's outcomes decide PROBE-ANSWERED-1 before the freeze; F-3's close() flush rides it |
| IR-138 | core zigbee mains silence limit | the 60-s mains silence constant sits UNDER the plug class's accepted reporting contract | AVAIL-SHAPE | PRE-RUN | landed 37f05a9 (b-metered); FLAPS ≤ 2 and the per-class naming time read at SOAK-NIGHT-2 and the dry runs |
| IR-139 | core zigbee boot re-link reporting | THE BOOT RE-LINK DRIVES NO REPORTING | AVAIL-SHAPE (the re-walk) | POST-RUN | the row's word: not before the run unless SOAK-NIGHT-2 shows a verdict it changes; after PROBE-ANSWERED-1 |

**PRE-RUN: 19** (IR-46 · 51 · 52 · 77 · 88 · 90 · 91 · 95 · 105 · 106 · 112 · 121 · 122 · 126 · 129 · 132 · 136 · 137 · 138)
**POST-RUN: 59**
**RETIRE: 16** (IR-45 · 56 · 60 · 63 · 76 · 83 · 96 · 102 · 107 · 113 · 114 · 115 · 117 · 118 · 120 · 123)

Least sure (10):
- IR-46 — PRE-RUN on a latent throw never observed in 20-h soaks; the hub may rule it a POST-RUN design question.
- IR-51 — the nightly's hero leg may be suspended during the run; then only IR-88's grammar matters pre-run.
- IR-56 — RETIRE rests on IR-114's text (J2a re-proposes a listed device); the packet 90-s read and F-6's second sample still stand.
- IR-60 — RETIRE as "superseded by IR-136", not by a landed unit (IR-120 the same); the hub may prefer a merge to a retire.
- IR-63 — PJ-2 (146468c) is named only in other rows' text; BH-2's boot-health forbidden-list half is unverified.
- IR-83 — IR-61b's landing is inferred from IR-90/91's text, not stated in this row's cell.
- IR-95 — PRE-RUN assumes J3 (Oct 19–21) has room; the plan does not describe J3's content.
- IR-115 — RETIRE is conditional on BC9's read of `transient_key_expired` tonight; a miss re-opens it as a false device failure.
- IR-123 — RETIRE rests on the hub's landed list (J2 carried IR-123); the row's own text names J2 only as a candidate lane (IR-113 follows it).
- IR-129 — PRE-RUN vs RETIRE turns on whether SOAK-NIGHT-1's packet already carried the EXPECT form; the cell does not say.

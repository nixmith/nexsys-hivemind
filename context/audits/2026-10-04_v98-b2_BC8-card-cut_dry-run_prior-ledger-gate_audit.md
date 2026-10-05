<!--
file: context/audits/2026-10-04_v98-b2_BC8-card-cut_dry-run_prior-ledger-gate_audit.md
purpose: The v98 hub's beat-2 audit — BENCH-CORE-8's card cut for Monday 2026-10-05 evening (the Pi's core to `df2bc62` BY SHA on Nick's word; BENCH-PULL-7 folded in; F-6 on G4-2; boot-health), its dry-run on the corpus (every block's bash -n, every verb at the case statement, every ULID and IEEE in the record, the greps RUN on the two kept REHEARSAL 2 logs, the EXPECTED tokens read at `df2bc62`, the python extractions on fixtures of the real shape), the prior-ledger gate (law 15), Nick's two words banked, and the hub's one ruling (REHEARSAL 3 folded into BC9's Friday).
audience: the v98 hub (beat 2) · the v99 hub (intakes BC8 Monday night against §4's pre-registrations) · Nick
state-type: card-cut audit (the dry-run's output verbatim in §3)
status: FILED v98 beat 2 (Sun 2026-10-04 ~20:3x CT; instrument 2026-10-05T01:12:42Z)
-->

# v98 beat 2 — BC8's card cut, dry-run, the prior-ledger gate; the two words; one ruling

## §1 Nick's two words (19:50 CT), banked — D-v98-9
- **`BC8: df2bc62`** — his words: "the hub is right and I concede. I argued the evenings; the hub's point is better: 0x006B and policy 0x0013 have never touched the real NCP, and you don't put first-ever radio traffic on the Pi the same night you baseline a soak. One change per grade. (If you want an evening back, the place to look is folding REHEARSAL 3 into BC9's Friday, not into the soak — the hub's call.)"
- **`RENDERER: tue`** — "yes, ahead of CONFIG-ERROR-1 if only one desk lane fits. It's the only item on the week that makes every later hub beat cheaper, and CONFIG-ERROR-1 gates nothing before the soak."
- `HIVE: LANDED 5931cda` (19:48 CT) — read at the instrument: HEAD `5931cda`, 16 files (+316/−71), porcelain 0, ahead 0, no trailer in the body.

## §2 The card (`context/instructions/2026-10-05_bench-card_BENCH-CORE-8_core-to-df2bc62_BENCH-PULL-7_F-6_operator-session-prompt.md`)
- **The form:** BC7's card (Parts A–C: the state block, the backup, the checkout, the build and THE POLL, the restart, boot-health, the proof of the tree) and REHEARSAL 2's card 3 (the byte-mark watch with `tail -c +$((M+1))`; the `bench.sh state` read — both ran on the Pi Sunday) and card 4 (the restore-check, verbatim). One outputs file (`_scratch/v98/bc8/2026-10-05_BENCH-CORE-8_outputs.txt`); BENCH-PULL-7's block re-pointed to it (the only edit to the block as cut — its commands and EXPECTED lines are v96 b1's, re-read against bench `main` = `ba846c2` tonight: `constants-md5 9b0af47b3376`, fleet 10/10).
- **The one-way door:** C2 checks out `df2bc62` BY SHA with `advice.detachedHead=false` — the clone reads `HEAD detached at df2bc62`, which the card names as correct; `ref=main` after the checkout is a STOP (the build is not kicked). BC9 (Fri) moves the clone to `main`.
- **F-6's instruments, two casings:** the LOG prints the enum (`zigbee.availability_link: … available=false reason=PING_TIMEOUT …` — the format string at `ZigbeeIntegrationAdapter.java:1718–1723` on `df2bc62`); the API prints the wire token (`availabilityReason=ping_timeout` — the J1 return's IT-arm assertion). The card names both where each is read (THE WIRE'S CASE IS READ AT THE MAPPER). The frozen DP-8 line `zigbee.availability_changed: device=… available=false` accompanies (`StandardAvailabilityTracker.java:513`).
- **G4-2's three ids pinned from the corpus:** IEEE `0xACEBE6FFFEF25A2C` ↔ device `01M3DPKN9SX4K6D7D1PKDP17S3` (BOOT2's relink line, Sunday 18:31:55.818 EDT) ↔ entity `01M3DPKN9WD9B88Q4SVDMSBJVS` (constants.yaml; REHEARSAL 2's card 2). D1 re-asserts the IEEE ↔ device-id line on Monday's boot log before the plug is touched; the other Shelly (G4-1, `0xACEBE6FFFEF733DC`) was Sunday's P6 sample and is not re-used.
- **The envelope:** ≤ 2 h; paste 18:30–20:00 CT; D2 not after 20:30; 21:00 CT = STOP at the current block, D4 (the re-plug) FIRST if a plug is out, then Part E. THE RESTORE RUNS BEFORE THE GAP holds by construction (no config written) and by D4.
- **The physical-first line** (IR-130) rides the guide's rules paragraph and P5; the playbook §8 gains it this beat (§5).

## §3 The dry-run on the corpus (`_scratch/v98/bc8/bc8_dry-run.sh` → `bc8_dry-run.txt`; run Sun 2026-10-05T00:58:10Z): COMPLETE — no FAIL
- 1. `bash -n` OK on 15 scripts (every fenced block and every ssh heredoc body).
- 2. Every `bench.sh` verb named (status · entities · state · restart · scenario) found once in the case statement.
- 3. Three ULIDs, each known: the entity ids in `constants.yaml`'s remembered list; the device id in the corpus's relink lines.
- 4. The one IEEE in 30 files of the record and corpus.
- 5. C3's counts RUN on BOOT2: `formed=0 resumed=1 relinked=10 adopted=0 proposed=0 config_issue=0 cache_loaded: 10`; `registry.projection_live: devices=10 entities=10 position=849602` at line 18.
- 6. D1's relink pin RUN on BOOT2: `device_relinked: device=0xACEBE6FFFEF25A2C deviceId=01M3DPKN9SX4K6D7D1PKDP17S3` — exact.
- 7. The byte-mark watch RUN on BOOT1 from the mark before the sensor's join: 9 sensor lines after the mark; D4's SEL regex matched 3 join-layer lines (real `device_join` · `device_announce` · `device_relinked`); the `available=true` grep 2; the `available=false` grep 0 — **the corpus carries no dark event** (J1 has never run on the Pi), so D3's pattern is verified against the SOURCE format string, not a captured line. Disclosed.
- 8. Every EXPECTED token exists at `df2bc62` in main trees (`availability_link` 3 files · `availability_changed` 2 · `PING_TIMEOUT` 3 · `FRAME_RECEIVED` 2 · `PING_SUCCESS` 2 · `availabilityReason` 7 · `EntityLink` 5 · `registry.projection_live` 1 · `device_cache_loaded` 1 · `network_resumed` 1 · `device_relinked` 1); the LOG's `available={} reason={}` format at the adapter; the WIRE's `"availabilityReason":"ping_timeout"` in the J1 return.
- 9. The three python extractions RUN on fixtures of the real shape: the `state` read with the three keys present and absent (null-safe `.get`), the `entities` read picking the G4-2 and sensor rows. The fixture's epoch is arbitrary; the shape is REHEARSAL 2's, which ran on the Pi.
- 10. BENCH-PULL-7's pins re-read on the desk clone: `ba846c2`, `constants-md5 9b0af47b3376`, `devices: 10 entities: 10`.
- 11. The output directory held nothing but the draft and the dry-run; the card names ONE outputs file.
- 12. The trailer grep 0; "superior" 0.

## §4 The prior-ledger gate (law 15) — every reused command string and named witness, grepped in its prior record
- **BC7's Parts A–C** (`context/audits/2026-10-02_v92-b5_BC7_intake_audit.md`): A–C3 HELD at the bytes Fri 10-02 — the backup, the checkout, the build kick, THE POLL, the restart, `scenario boot-health`, the jar-class count, the entities python. BC7's one STOP was Part D's permit-join reason string (U+2014 outside `reason_re`) — this card opens no window and passes no reason string; n/a, named.
- **REHEARSAL 2's cards 3–4** (`context/audits/2026-10-04_REHEARSAL-2_return.md` §3): the watch loop and the `state` read RAN (3a/3c, C3.txt); the departure there was a PRE-REGISTRATION arm, not a command — this card writes its F-6 arms with the API ADVANCE named as its own observation, not as "the API still on the prior instant" (the Sunday miss). The restore-check (4a) RAN; reused verbatim with two fields added after its last `|`.
- **The REHEARSAL 2 EXPECT defects (IR-129; the lesson):** no EXPECT in this card reads the log for a store fact; each EXPECT names its instrument (the log token with its casing; the API key with its casing); the two-arm rows (F-6; the resume) carry an EXPECTED line per arm.
- **The one open question carried into Monday** (recorded, not blocking): whether `bench.sh state`'s payload (`GetEntityState`) carries the three J1 keys or only `entities` does — the card reads both and marks `reason=None` on `state` as RECORD, with the entities row as the instrument.

## §5 The hub's ruling and the edits by id
- **D-v98-10 — REHEARSAL 3 FOLDED INTO BC9's FRIDAY** (Nick delegated the call, 19:50): BC9's card (cut at v99/v100) carries J2's deploy (Parts A–C, BC8's form at `49455fc` on `main`) and then REHEARSAL 3's P1–P5 as Parts D–E, inside one ≤ 2 h envelope with the 21:00 clock rule — if the build or the deploy runs long, the rehearsal parts move to Saturday UNCHANGED (the card's own rule), so the fold costs nothing in the worst case and returns Saturday in the good case. Sat 10-10 becomes the reserve (no rig act planned). THE HORIZON §9's Oct 15–18 row and the brief's rig row read it by id; THE WEEK (D-v97-17) moves on that one day.
- **D-v98-11 — THE WEEK's Tuesday on `RENDERER: tue`:** BEAT-RENDERER-1 (the hivemind desk lane; its charter v99's first block) runs Tuesday ahead of CONFIG-ERROR-1 + IR-122; CONFIG-ERROR-1 runs the same evening if hands allow, else the first free desk hour (Sat 10-10, now the reserve). The bench charter AVAIL-LINE-1 stays Tuesday's free-hands lane.
- The playbook §8 gains addendum (13) THE PHYSICAL-FIRST LINE (IR-130 → RETIRED by id). The register: IR-130 RETIRED; IR-128's measurement names BC8's D4 as the next sample.

## §6 Disclosed
The Pi untouched. D3's dark pattern verified at the source format string only (no corpus has a dark event on J1's core). `GetEntityState`'s key set not read at `df2bc62` (the card reads both surfaces). The build time is BC7's estimate.

<!--
file: context/handoff/2026-07-21_04p-adoption_bench-session-report_for-hub-adjudication.md
purpose: Full session report for the SNZB-04P (0x449FDAFFFE688F57) LEARN-PERSIST contact adoption bench run (2026-07-20 evening → 2026-07-21 morning). Layer-1 operator + desk evidence assembled for the v35 hub's INDEPENDENT (layer-2) adjudication: the result, the code-grounded causal chain, the device_left incident and its recovery, two instrument/observability defects the run surfaced, and an independent-investigation brief. This is NOT a dispatch — verify-not-redo.
audience: the v35 PM mission-control hub (paste adjudication); Nick (operator).
state-type: session report / audit INPUT. An in-session read is layer-1 evidence, NOT a gate (durable-discipline: "an in-session LLM 'verification: clean' is NOT a gate"). Everything below is refutation-welcome in both directions.
status: COMPLETE run · GREEN at the instrument · one-way door NOT tripped wrong. Contains AUDIT-CORRECTION blocks (§6) — do NOT re-run the WU from them. Canonical project state (HEADs, watermark, projectionVersion, event-type counts, next Core slot) is POINTER-NOT-COPY — re-derive from the spine, never from this file.
observed-at: Pi hs-dev-1 running deploy 355a711 (re-verified at the instrument: git log -1 + BUILD SUCCESSFUL + first-boot count=0). All file:line citations are against the desktop checkout at 355a711 (HEAD -> main, origin/main). CI: GREEN on 355a711 per Nick (the gate of record — layer-2 should confirm actually-green on the pushed SHA, not take this line).
landed: 2026-07-21 by the v35 hub (beat 7) — body verbatim as delivered in-conversation. HUB TWO-LAYER ADJUDICATION: ACCEPT — D1 [M] 5/5 CLOSED · THE M14 TRIGGER SWEEP PASS 7/7 (M14 OPENS; the third-plug rider fires) · the incident ruled H-B-proximate/H-A-structural (window arithmetic verified exact: the leave at T+3 s past close) · Q1 RULED at source: NO hands-off re-propose exists at 355a711 (ADOPT-REPROPOSE minted) · Q2 → OBS-CONFIRM minted · Q3 accepted-as-documented · Q5 RULED: the BENCH-CONST counter is the projection_live replay-head — 25065 · D-1/D-2 = hub-owned package defects, owned; the instrument-semantics class rule folded into the playbook §8; the v3 erratum declined as moot. Detail: pm-handoff v35 beat 7.
-->

# 04P Adoption — Bench Session Report (LEARN-PERSIST, persist-verified) — for hub adjudication

## §0 — How to read this, and the one-line verdict

**Verdict.** The SNZB-04P (`0x449FDAFFFE688F57`) is adopted as a `binary_sensor` with the **contact** capability, off the *persisted* wire-learned CONTACT zone-type, with **zero re-learns** at adoption. Six entities are AVAILABLE, the join window is shut (standing posture), and the learn has now survived a network-leave plus three reboots. The one-way door — a durable MOTION mis-adoption — was **never tripped**. The D1 predecessor (the 2026-07-19 cached-interview fast-propose race that LEARN-PERSIST was built to close) is closed by demonstration.

**This report is layer-1 evidence, not a gate.** Nick asked for it explicitly so the hub would *think independently and investigate the results and the underlying code*. Treat every CLAIM below as a hub-refutable hypothesis and every QUOTE (log line / `File.java:Lxxx`) as the primary evidence to adjudicate it against. Where I mark something CONFIRMED I mean "I read the primary text this session"; that is a layer-1 read and earns a layer-2 spot-check, exactly like any grounding-agent return. §7 is a re-derivation checklist so nothing here needs to be taken on faith.

**Pointer-not-copy.** This file carries no project-wide state. Milestone status, watermark, counts, and the next slot live in the spine only (`context/status/PROJECT_SNAPSHOT.md` + `context/handoff/pm-handoff.md` + `git log`).

---

## §1 — The result, against the package's own DONE-WHEN

The operator package was `2026-07-19_04p-adoption_operator-mini-package_v2-persist-verified.md`. Its top-level DONE-WHEN and my pass/fail with the evidence line:

| DONE-WHEN criterion | Verdict | Evidence (primary) |
|---|---|---|
| `device_adopted` for `0x449FDAFFFE688F57` | **PASS** | `20:54:02.934 … zigbee.device_adopted: device=0x449FDAFFFE688F57 deviceId=01KY12MQVQ204M1VP39F1ZDM33 entities=1` (recovery boot `bench-2026-07-20-205257.log`) |
| `~/bench.sh entities` shows exactly **6** rows, all AVAILABLE | **PASS** | final boot `bench-2026-07-21-073330.log`: 6 entities, all `availability=AVAILABLE stale=false`; 04P entity = `01KY12MQW954E4XYNKH0Y5H8VX` |
| a door open/close produces a contact state change | **PASS (via the correct instrument)** | no `state_reported` log line exists by design (see D-1, §6); confirmed instead by `viewPosition` advancing on every magnet action: `26326 → 26330 → 26340 → 26347` (+4/+10/+7) against a measured overnight idle of ~2 events/min |
| the Block-6 (BENCH-CONST) capture pasted | **PASS** | clean 6/6 boot captured — see §2 |

Adopted-as-**contact** specifically (not merely adopted): the classification path consumed the rehydrated CONTACT zone-type — see the causal chain in §4. The `ias_zone_enrolled` at `20:54:12.086` confirms the IAS Zone status-change path (the contact's actual reporting vehicle) is wired.

---

## §2 — BENCH-CONST re-mint inputs (for the hub to author the re-mint)

Read AT the instrument on the final standing-posture boot (`bench-2026-07-21-073330.log`, 07:33:33):

- `registry.projection_live: devices=6 entities=6 position=25065`  ← the canonical **position** for the re-mint (projection replay-head, not the read-model `viewPosition`)
- `zigbee.network_resumed: channel=20 panId=0x774c`
- `zigbee.learned_zonetypes_rehydrated: count=1`
- `zigbee.permit_join_opened` count = **0** (window shut)
- `zigbee.adoption_maps_rehydrated: devices=6`
- entities: 6 rows, all `AVAILABLE stale=false`
- the new 04P: deviceId `01KY12MQVQ204M1VP39F1ZDM33` · entityId `01KY12MQW954E4XYNKH0Y5H8VX`
- carried set (unchanged): Hue `01KX1PA4…`, SNZB-03P/02P/01P, S31 Lite — 5 prior entities all still AVAILABLE

**Two counters, don't conflate them** (a re-mint hazard): `projection_live position=25065` is the registry projection's replay-head glance; `entities … "viewPosition":26379` is the read-model view cursor, which includes every state/telemetry event and always runs ahead. The package's Block-6 "position" is the `projection_live` value → **25065**. Layer-2 should decide which counter the BENCH-CONST schema actually pins and confirm 25065 is the intended field.

---

## §3 — What happened (timeline, load-bearing evidence only)

Two calendar sessions. Evening 2026-07-20: gate re-verify → learn → persist-verify → accept-list → **first adopt attempt failed (device_left)** → recovery adopt. Morning 2026-07-21: door-test verification → standing-posture close-down.

- **Block 0 — deploy re-verify at the instrument.** `git log -1` = `355a711` (LEARN-PERSIST), `BUILD SUCCESSFUL`. Deploy-state re-derived at the instrument, not assumed (bench-arc discipline #4).
- **Block 1 — first boot on the build.** `projection_live: devices=5 entities=5 position=18946` · `adoption_maps_rehydrated: devices=5` · **`learned_zonetypes_rehydrated: count=0`** (honest first boot — the instrument exists and the slate is clean) · `network_resumed channel=20 panId=0x774c` · `permit_join_opened duration=254s`. `count=0` is the anti-vacuous positive-evidence confirming the LEARN-PERSIST build is the one running.
- **Block 2 — Window #1, learn + persist-verify (⛔ gate 1).** One long-press. Wire arc: `device_announce` → `device_proposed model=SNZB-04P profile=sonoff_snzb_04p status=COMPLETE` (benign fast-propose; 04P not yet listed, adopts nothing) → `key_established … TC_REQUESTER_VERIFY_KEY_SUCCESS` → **`20:18:26.101 … ias_zone_type_learned: device=0x449FDAFFFE688F57 zoneType=CONTACT (was MOTION)`** → `ias_zone_enrolled endpoint=1 zoneId=0`. Bench stopped (forces the shutdown flush), then on-disk: `"learnedZoneTypes": { "0x449FDAFFFE688F57": 21 }` (21 = 0x0015 = CONTACT). **Gate 1 PASS.** The `(was MOTION)` is the crux of the whole feature — see §4.
- **Block 3 — accept-list.** yaml `adopt_devices` now 6 entries incl. the 04P; bench stays stopped.
- **Block 4 (first attempt) — Window #2 (⛔ gate 2), then the incident.** Boot `bench-2026-07-20-...202424`: **`learned_zonetypes_rehydrated: count=1`** (Gate 2 PASS), `projection_live 5/5 @18946`, `permit_join_opened duration=254s` (opened 20:24:35 → closes 20:28:49). Operator pressed. The **only** 04P line that followed was **`20:28:52.141 … zigbee.device_left: device=0x449FDAFFFE688F57 nwk=0x64aa`** — no announce, no propose, no adopt. `entities` = 5. See §5.
- **Recovery — fresh window, clean adopt.** Boot `bench-2026-07-20-205257`: `count=1`, window re-opened. Press produced a **full fresh-join arc** at `20:54:02`: `device_join … status=UNSECURED_JOIN decision=USE_PRECONFIGURED_KEY nwk=0xcee2` → `child_join … type=SLEEPY_END_DEVICE` → `device_announce` → `device_proposed … status=COMPLETE` → `proposal_accepted source=config` → **`device_adopted … entities=1`** → `reporting_configured clusters=2 verified=1 degraded=1` → `key_established SUCCESS` → `ias_zone_enrolled`. **No `ias_zone_type_learned` line** — it adopted straight off the rehydrated learn.
- **Block 5 — door test (next morning).** 6/6 AVAILABLE. Contact reporting confirmed via `viewPosition` deltas (§1). The package's `state_reported` grep showed nothing — by design, not fault (D-1).
- **Blocks 6+7 (merged) — standing-posture capture.** Because `projection_live` is boot-once (D-2), the overnight boot's line was stale at 5/5; the close-down reboot re-derived the clean **6/6 @ 25065** used in §2, with `permit_join_opened` count 0 and `count=1` rehydrate.

---

## §4 — Why it adopted as contact (code-grounded causal chain — PRIMARY evidence)

This is the section to layer-2 hardest, because it is the safety argument. All refs are against 355a711.

**(a) The sensor defaults to the wrong thing.** An IAS-Zone endpoint with no learned zone type classifies as **motion**. `EndpointClassifier.iasCapability(learnedZoneType)` (≈`EndpointClassifier.java:166`): *"only a wire-learned CONTACT re-selects (the SNZB-04P shape); null/MOTION … stay the motion fallback … Adoption is a one-way door at V1, so a wrong selection here is durable — never guess beyond the wire truth."* So without a learned CONTACT, the 04P adopts as motion, durably. That is the hazard the whole two-window package exists to prevent.

**(b) The wire learn corrects it, and persists on every success.** `ZclIngestionUnit.learnZoneType()` (≈`ZclIngestionUnit.java:602-621`): resolves the wire zclId → `ZoneType`; `learnedZoneTypes.put(...)` (in-memory enum map, `:146`); **`learnSink.accept(device, learned.zclId())`** — DP-LP-3: *EVERY* successful learn persists (change case and same-as-effective silent case). On a type change it also `invalidateHandlers(device)` (F-8 — drop the cached handler table so subsequent frames normalize under the new type) and logs `ias_zone_type_learned … (was {})`. The Block-2 `(was MOTION)` proves the effective type flipped MOTION→CONTACT and the handler table was rebuilt.

**(c) The persist survives the process, not just the debounce.** `ZigbeeDeviceCache`: `WRITE_DEBOUNCE = Duration.ofSeconds(30)` (`:57`); the learn record sets `dirty`; the persisted map is `Map<Long,Long> learnedZoneTypes` (`:76`) written as `putObject("learnedZoneTypes")` with the raw zclId `longValue()` (`:489-499`) → `21` on disk. `flush()` (`:335`) *"Writes the cache immediately (adapter shutdown)"* and *"ignores the failure backoff — shutdown is the last chance to persist"* (`:343`); the adapter calls `cache.flush()` on stop (`ZigbeeIntegrationAdapter.java:401`). ⇒ **`bench.sh stop` flushes the learn regardless of the 30 s debounce**, which is what makes Gate 1's on-disk check a valid gate: an *absent* entry after a clean stop is a genuine miss, not a timing race.

**(d) Rehydrate-before-joins puts the learn in the map before anything can propose.** `ZigbeeIntegrationAdapter.rehydrateAdoptionMaps()` runs at startup (`:296`); *"rehydrate-before-joins holds by construction (DP-LP-4)"* (`:329`); it logs `learned_zonetypes_rehydrated: count={}` from `cache.learnedZoneTypeIds()` (`:339`). So `count=1` at a Window-#2 boot means the CONTACT id is in the map *before* any device can announce → any propose that follows classifies against CONTACT.

**(e) Classification consumes it.** `EndpointClassifier.classify(descriptor, learnedZoneType)` → `binarySensor(...)` (≈`:146`): occupancy outranks IAS; else `iasCapability(learnedZoneType)` → **contact** when learned CONTACT, entity type `BINARY_SENSOR`. The no-arg `classify(descriptor)` delegates with `learnedZoneType=null` (motion fallback), so the *only* thing standing between the 04P and a motion mis-adopt is a non-null rehydrated CONTACT.

**Chain:** wire CONTACT (b) → persisted to disk via `learnSink` + shutdown `flush` (c) → rehydrated `count=1` before joins (d) → `iasCapability(CONTACT)` → contact entity (e). The recovery adopt proves the chain end-to-end **without a re-learn**: the adopt arc carried no `ias_zone_type_learned`, so the contact selection came purely from disk.

---

## §5 — The device_left incident and its recovery (the most audit-worthy part)

**What is CONFIRMED.** (i) The learn survived. `device_left` is log-only: `ZclIngestionUnit.java:292-296` is `if (join.deviceLeft()) { log.info("zigbee.device_left…"); return; }` — no state mutation, no cache touch. The only `learnedZoneTypes.clear()` in the cache (`:575`) is the load-time reset, not a leave path. Verified against disk: after the leave, `"0x449FDAFFFE688F57": 21` was still present, and it rehydrated `count=1` on the very next boot. So the one-way-door asset (the persisted learn) was never at risk. (ii) No mis-adoption occurred — `entities` stayed at 5 through the incident; the durable MOTION hazard did not fire. Stopping at the failure cost nothing.

**What is HYPOTHESIS (hub to adjudicate).** Why did the Window-#2 press yield a leave instead of an adopt?

- **H-A (favored) — the operator model, not the device, is the gap.** In Block 2 the 04P *joined and stayed joined* (it was never removed, just not adopted). At the Block-4 boot it was a known-but-unadopted, quietly-sleeping member. The package's Block 4 says "one long-press re-pair" and expects `device_announce → device_proposed → adopted`. But a physical long-press on an *already-joined* SNZB-04P produced only `device_left`, no re-announce. The recovery worked because by then the device was **off-network**, so the press drove a **fresh** `UNSECURED_JOIN` (`nwk` changed `0x64aa → 0xcee2`) → announce → propose → adopt. **Claim: Window #2 needs a fresh join, and "re-pair an already-joined device" does not reliably produce one.**
- **H-B — window-timing race.** Window opened 20:24:35 +254 s ⇒ closes 20:28:49; `device_left` at 20:28:52, three seconds after close. If the press ran late, the device left as the window shut with no open window to rejoin through.
- **H-C — firmware button semantics.** A too-long hold factory-resets the SNZB-04P (leave). Distinguishes from H-A only by button-duration; the outcome (off-network → next join is fresh) is the same.

H-A and H-B/C are not exclusive. **Discriminator experiment (state predictions BEFORE any re-run, per bench-arc discipline #4 — but DO NOT re-run on this adopted unit; run on a spare 04P):** (1) join a spare, leave it *unadopted+joined*, add to `adopt_devices`, reboot into an open window, and **without touching the device** watch for a propose. Prediction if the adapter can re-propose a cached-interview device on config-add: `device_proposed source=config → device_adopted`, no physical act — which would make Window #2's physical press unnecessary. (2) If nothing proposes hands-off, single **short** press (release on first LED blink) early in the window. Prediction under H-A: fresh `UNSECURED_JOIN` → adopt. Under H-B: adopt iff pressed with ≥ ~30 s of window remaining.

**Why this matters beyond this run.** The package's own reason for existence is the *cached-interview fast-propose race* — in Window #1 that fast-propose is the ENEMY (why the 04P is withheld from `adopt_devices` until the learn persists). But in Window #2 a cached-interview fast-propose is exactly what you'd WANT (adopt with no physical press). The hub should map that relationship precisely against `ZigbeeAdoptionSlice`/the propose path: **is there a hands-off "propose the already-known device when it newly appears in `adopt_devices`" path, and if so why did Window #2 specify a physical press at all?** If that path exists, the entire Window-#2 press hazard (and this incident) is designable-away.

---

## §6 — Two instrument/observability defects the run surfaced

> **AUDIT CORRECTION — do not re-run the WU from this section.** These are corrections to the operator package for the *next* author/adjudicator. Receiving sessions verify-not-redo.

Both are the same class the project already names: an operator glance-point asserting a token that cannot appear. Framed in the bench doctrine:

**D-1 — Block 5's `state_reported` grep is an anti-vacuous violation (silently-succeedable arm ships NO positive evidence).** A contact report is emitted straight into the registry as an event, with no happy-path log: `ZclIngestionUnit.publishStateReported()` (≈`:511-540`) builds `EventDraft(EventTypes.STATE_REPORTED, …)` and calls `publisher.publishRoot(draft)`; it logs *only* `ingestion_unadopted` (debug, entity unresolved) or a publish conflict (error). `state_reported` is a core/automation **event type** (consumed by `PendingCommandLedger` et al.), not a zigbee INFO token. So `grep -E "state_reported|449FDA"` is empty even when the sensor works. This is precisely the bench discipline "every no-output-is-healthy check gets a paired positive-evidence line." *Corrected verification:* confirm via `projection_live`/`viewPosition` advance on a bracketed magnet action, or via a bench entity-**value** read (does `~/bench.sh` expose a state/value verb? unresolved this session — worth an adapter-side low-rate `state_reported` INFO or a bench value-read as an **instrument-first** arm so the next run measures rather than infers). Note the irony for layer-2: the product's explainability hero is literally *"did it actually confirm?"* — yet the bench presently cannot show a single confirm without inference. That is a real observability gap, not a doc typo.

**D-2 — Block 6's `projection_live: devices=6 entities=6` is mis-sequenced against a boot-once instrument.** `RegistryProjectionSubscriber` javadoc: *"On the AMD-42 TRANSITION→LIVE callback (`onCaughtUp()`) this logs ONE `registry.projection_live` INFO … the boot glance-point proving the rebuild ran (a silently-succeedable arm ships positive evidence)."* It fires **once per boot**, not on later applies. So on any boot that started *before* the adopt, `tail -1` is frozen at the pre-adopt `5/5 @18946` — which is what the overnight boot showed. The clean 6/6 only exists after a boot that replays the adopt. *Corrected capture:* fold the Block-6 BENCH-CONST read into the Block-7 close-down boot (the first boot that rebuilds to 6) — as done here, yielding `6/6 @ 25065`. In the package's intended single-session flow this same bug bites (Block 6 would read Block 4's boot line). Layer-2 should confirm whether other operator packages assert `projection_live` counts at a non-boot glance-point — this may be a class, not a one-off.

I can produce a v3 erratum of the package with both blocks corrected (headed as an AUDIT CORRECTION, not a dispatch) on request.

---

## §7 — Independent-investigation brief for the hub (re-derive; don't trust this file)

**Re-derivation checklist (layer-2 — each is a primary-text read, not a re-run):**
1. Re-grep the five instruments at HEAD and confirm names/levels: `learned_zonetypes_rehydrated` (adapter ~:339, INFO), `ias_zone_type_learned` (ingestion ~:619, INFO, change-only), `permit_join_opened` (adapter ~:721), the `learnedZoneTypes` JSON section (cache ~:489/:580), `device_left` (ingestion :292 — confirm log-only).
2. Re-confirm the flush-on-shutdown path: `cache.flush()` at adapter shutdown (:401) + `flush()` immediate-write (:335) + `WRITE_DEBOUNCE` (:57). This is the load-bearing premise of Gate 1.
3. Re-derive 21 = 0x0015 = CONTACT from `ZoneType` (the `zclId()` values) — do not carry the mapping from this file.
4. Re-read the classify fork: `EndpointClassifier.iasCapability` (contact iff learned CONTACT) and `binarySensor` (occupancy outranks IAS). Confirm the no-arg `classify` = motion fallback.
5. Confirm `learnedZoneTypes.clear()` (:575) is load-only — the whole "learn survived the leave" claim rests on there being no leave-triggered clear.
6. Confirm CI is actually-green on pushed `355a711` (the gate of record; my status line is hearsay).

**Open questions worth a lane (ranked):**
- **Q1 (design).** Does a hands-off "propose a cached-interview device when it newly appears in `adopt_devices`" path exist (`ZigbeeAdoptionSlice`/propose)? If yes, Window #2's physical press — and this incident — is designable-away. Reconcile against the Window-#1 fast-propose *hazard*: same mechanism, opposite desirability. (See §5.)
- **Q2 (observability).** Instrument the contact-report path (adapter-side low-rate INFO, or a bench value-read) so "did it actually confirm?" is measurable at the bench, closing the D-1 anti-vacuous gap. Instrument-first: buy it in the next WU rather than theorize about the silence twice.
- **Q3 (correctness/robustness).** `reporting_configured … verified=1 degraded=1` on the 04P: confirm the degraded arm is the battery/power cluster and that the contact path (IAS Zone status-change) is independent of it (`ConfirmationOverrideInstaller.verifiedFact` ~:203; the override that lets a sleepy device's entity stand, ~:225). Sleepy-degraded is documented as expected (`EzspReportingOps` ~:90 comment `verified=2 degraded=1`), but "expected" should be a layer-2 read, not my assertion.
- **Q4 (doc-class).** Audit other operator packages for the D-1/D-2 pattern (a glance-point asserting a token that is an event-only, or a boot-once instrument read off a stale boot).
- **Q5 (schema).** Pin which counter the BENCH-CONST re-mint wants (`projection_live` replay-head 25065 vs read-model `viewPosition` 26379). §2.

---

## §8 — Assessment: what this run means

**LEARN-PERSIST did exactly what it was designed to do, and it was proven under adversity rather than in the happy path.** The wire-learned CONTACT classification was captured once, persisted, and then drove a correct contact adoption after the device left the network and the hub rebooted three times — with no re-learn at adoption. That is a stronger proof than a clean single-window run would have given: the persistence path was exercised precisely at the failure it exists to tolerate. The D1 predecessor / cached-interview fast-propose race is closed by demonstration, and the safety property held throughout — at no point did the 04P adopt as anything, so the durable MOTION mis-adoption the classifier warns about (`iasCapability`: "a wrong selection here is durable") never had a window to occur.

**The persist-verified two-window shape earned its complexity.** Both ⛔ gates did real work: Gate 1's on-disk check is valid *because* shutdown-flush defeats the debounce (§4c), and Gate 2's `count=1` is valid *because* rehydrate precedes joins (§4d). The incident is the best evidence for the shape — a failed physical re-pair was fully recoverable *only because* the learn was already on disk and `device_left` is inert against it.

**The net new engineering signal is not the adoption — it's §5 and §6.** The run surfaced (a) a latent operator-model gap: Window #2 assumes an already-joined device will re-announce on a press, and it does not; the recovery succeeded via a fresh join, which suggests either an operator-block hardening or, better, an adapter-side hands-off re-propose that would remove the physical-press hazard entirely; and (b) two instrument defects of a class the project already names — a silently-succeedable arm with no positive evidence (D-1) and a boot-once instrument read off a stale boot (D-2). Those are the items most worth the hub's independent time, because each generalizes past this one device.

**Bottom line for adjudication.** Result: GREEN, re-mint inputs in §2. Safety: intact. Layer-2 asks: confirm CI-green on 355a711, re-derive §4/§5 against primary text, and rule on Q1 (the hands-off re-propose) and Q2 (the confirm-path instrument) — those two turn a successful-but-fiddly procedure into a clean one.

*— End of report. Refutation welcome in both directions; agent labels are claims, the quoted lines and `File.java:Lxxx` are the evidence.*

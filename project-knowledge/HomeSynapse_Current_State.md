<!--
file: project-knowledge/HomeSynapse_Current_State.md
purpose: Authoritative current-state document for HomeSynapse Core; uploaded to the Claude Project.
audience: All
update-cadence: per-WU
state-type: current
status: CURRENT
last-verified: 2026-06-13 against core `e5ea76f` (substantive `7c73c91` = M6.2) — **M6 3-of-4 COMPLETE (M6.1 `b7bc65c`+`9035110` · M6.4 `62a81e6` · M6.2 `7c73c91`; M6.3 triple-gated = the M6 critical path). R14/R15 research cycle COMPLETE (high-water REC-185; merged disposition = THE M7 authority). M7 entry-gate forming: AMD-88..93 PROPOSED on disk + the bundled DOCS review (block + B2 C8/C9) READY TO DISPATCH. Watermark AMD-87 on disk (raises to 93 at block ratification). projectionVersion 5; event pins 55/24/36; build GREEN 147.** _Prior:_ 2026-06-07 against `7f44bed` — **M5-A COMPLETE** (platform-systemd `PlatformPaths`/`HealthReporter` impls + the **AMD-87 `Expectation` persisted codec** + `FloorId` registration; **M9 command-bearing-`CapabilityAdded` prerequisite CLEARED**) + **M5-B/B1 DONE** (**Doc 15 Cryptographic Architecture LOCKED**; AMD-86 + AMD-87 RATIFIED; watermark **AMD-87**; 135 invariants; build GREEN 147 tasks; `projectionVersion` 5). Prior spine state: `8ef9e9f` (M4 COMPLETE, watermark AMD-64).
-->

# HomeSynapse Core — Current State

Last updated: 2026-06-13 — **M6 EXECUTION 3-of-4 COMPLETE; THE M7 ENTRY-GATE IS FORMING.** Since 2026-06-09: **M6.1 COMPLETE (whole — M6.1b `b7bc65c` + M6.1a `9035110`, incl. gate-fix round 1: explicit `CoreSchema` on both LoadSettings + the ratified-AMD-71 ArchUnit Rule-5 exemption; the 2026-06-10 module-info ruling added 5 third-party non-transitive `requires`)**; **M6.4 COMPLETE (`62a81e6` — hot-reload atomic swap + write path; `ConfigSectionReloadedEvent` full P2 fan-out 54→55/23→24/35→36; GF-1 = a stale publish-count pin updated to the ratified R1/DP-10 contract — the survey's new pin category)**; **M6.2 COMPLETE (`7c73c91` — `ScopeKeyManager` HKDF per-scope key mgmt + `StandardSecretStore` `secrets.enc` + AMD-68 `setAll` + `!secret`/`!env` resolution; R-1 write() rejects tag-bearing docs fail-closed [tag-preserving emitter = queued post-MVP AMD]; the `PayloadCipher` E2 bridge held-not-consumed until M6.3; GREEN in ZERO gate-fix rounds)**. Core HEAD **`e5ea76f`** (docs-only MODULE_CONTEXT permit-count fix 27→30 on `7c73c91`). **M6.3 stays triple-gated (OQ-15-2 Pi-4 microbench + AMD-86 §3 interviews + OR-M6-NONCE) — its evidence gates are the M6 critical path AND the W25/W26 M6.3-vs-M7 ordering input.** **The R14/R15 research cycle ran COMPLETE in one day (2026-06-12):** W0 currency delta → 3 briefs → 3 returns assessed A− (zero fabrications across two DOCS-connector-blind runs) → **the merged disposition (`nexsys-hivemind/context/planning/2026-06-12_M7-blueprint_merged-disposition.md` — THE M7 blueprint authority; REC-31..40 + 141..185; high-water REC-185)** → M7/M8 charter POPULATED. **2026-06-13: the M7 entry-gate AMD block is DRAFTED — AMD-88..93 PROPOSED** (F1 triggers 9→12 + `triggerId` · F2 `SemanticTagSelector` + `includedRoles` BREAKING · F3 `ConfirmationPolicy`/`RepeatAction`/`InvokeAutomationAction` · F4 `RunCausalChain` supersedes AMD-04 · F5 the automation event vocabulary, 16 mints + 2 reshapes, FLATTEN type-residency · F6 `automations.yaml` (major,minor) schema posture), **+ the bundled DOCS review prompt (block + B2 C8/C9 `actorRef`/energy-shape in ONE dispatch) READY — Nick veto-or-default.** M7.1 issues only when the 5-row entry-gate is green (block RATIFIED · C8 RATIFIED · the M6.3-vs-M7 ordering call · M5-C Increment 1 [Lane-4, P6] · MODULE_CONTEXT currency ✓). _Prior 2026-06-09 —_ **M6 ENTRY-GATE CLOSED; M6.1 READY TO ISSUE.** The M6 config block is ratified: **AMD-66/67/68/70/71 RATIFIED 2026-06-09** (single DOCS review RATIFY-WITH-EDITS; the load-bearing **E70-1** fold flattened config-event payloads to event-resident types under a **type-residency rule** — now a standing JPMS lesson in the P2 consumer/pin survey) + **AMD-69 DEFERRED** (Option (a) confirmed; Tier-2/OQ-15-3; the number stays reserved). Invariants **§37–§41 registered (+8)**; **on-disk watermark UNCHANGED at AMD-87** — all six were reserved-below-watermark slots; ratification fills them, it does not raise the ceiling. **M6.1 (config pipeline) is READY TO ISSUE** (gate lifted, not yet issued); AMD-68 half of M6.2's gate is satisfied (M6.2 waits on M6.1 landing); **M6.3 stays triple-gated** (OQ-15-2 Pi-4 microbench + AMD-86 §3 interview signal + OR-M6-NONCE). HEAD `6c6dd33` (code untouched). _Prior 2026-06-07 —_ **M5 WINDOW IN PROGRESS.** **M5-A COMPLETE** (`7f44bed`, watermark **AMD-87**, `projectionVersion` 5; build GREEN, 147 tasks): platform-systemd `PlatformPaths`/`HealthReporter` impls (Part 1+3, `8028337`) + the **AMD-87 `Expectation` persisted codec** (Part 2, `7f44bed`) → **command-bearing `CapabilityAdded` now round-trips; the M9 prerequisite is CLEARED.** **M5-B/B1 DONE** — **Doc 15 (Cryptographic Architecture) is the 15th design doc, LOCKED**; **AMD-86** (INV-PD-07 crypto-shred MVP-scope narrow + INV-PD-03 at-rest posture) + **AMD-87** RATIFIED. **M5-D** — three evidence artifacts (Pi-4 AES-GCM microbench → OQ-15-2; energy/erasure interview guide → AMD-86 §3; sd_notify decision matrix) AUTHORED + independently reviewed (RATIFY-grade); awaiting Nick to run. **Next: M6 (Configuration + secrets/crypto)** — entry-gate half-closed (crypto side via M5-B/B1); closing the config side (AMD-66–71 + the Doc 06 `SecretStore.setAll(Map)` currency amendment) + resolving OQ-15-2 opens it. M5 charter + W24 plan: `nexsys-hivemind/context/planning/weeks/2026-W24_jun08-jun14.md`; M5 decisions: `context/decisions/2026-06-06_post-M4_M5-window_decisions.md` (D1–D8).

---

## 1. Current Milestone Status

**M6 (Configuration + secrets/crypto) — IN PROGRESS, 3 of 4 pieces COMPLETE; M7 entry-gate forming.**

- **M6.1 — ✅ COMPLETE (whole):** M6.1b `b7bc65c` (config access/events half — AMD-66/67/70 contract shapes; `CONFIG_VALIDATION_COMPLETED` manifest fan-out 53→54/22→23/34→35) + M6.1a `9035110` (load/validate half — `YamlLoader` CoreSchema-explicit safe YAML 1.2, `JsonSchemaCompositeValidator`, `StandardSchemaRegistry`, `StandardConfigurationService`; gate-fix round 1 + the 2026-06-10 module-info ruling: 5 third-party non-transitive `requires`). Full check GREEN (147).
- **M6.4 — ✅ COMPLETE** (`62a81e6`): hot-reload atomic swap + UI/API write path (reload()/write(), AMD-66 invocation matrix, C5 reject-and-keep-prior-good, optimistic concurrency, `AtomicYamlWriter` temp-fsync-rename; R1 per-ERROR `config_error` w/ the §12.4 x-sensitive fence; R2 §3.7 step-7 migration write-back; `ConfigSectionReloadedEvent` fan-out **54→55/23→24/35→36**). GF-1 = stale publish-count pin → the P2 survey gained the behavioral-pin category.
- **M6.2 — ✅ COMPLETE** (`7c73c91`): `ScopeKeyManager` (lazy 0400 `.root-key`, RFC-5869 HKDF-SHA256 scope KEKs, AES-256-GCM-wrapped DEKs in `scope_keys.json` [R6]) + `StandardSecretStore` (`secrets.enc` GCM envelope under the `config_secrets` scope; AMD-68 `setAll` all-or-nothing; AMD-16 backup rotation) + `!secret`/`!env` stage-3 resolution in load AND reload; write() rejects tag-bearing documents fail-closed (R-1; tag-preserving emitter = queued post-MVP AMD); the E2 `PayloadCipher` bridge held-not-consumed until M6.3. **GREEN in ZERO gate-fix rounds — an M6 first.**
- **M6.3 — ⛔ TRIPLE-GATED (the last M6 piece; its gates = the M6 critical path):** OQ-15-2 (Pi-4 AES-GCM microbench, target Wed Jun 17) + the AMD-86 §3 energy/erasure interview signal + OR-M6-NONCE (counter-nonce durability co-design). These same gates feed the **W25/W26 M6.3-vs-M7 ordering call** (Nick's, at the boundary).

**M7 (Automation) — entry-gate forming (5 rows; M7.1 issues only when ALL green):** (1) **AMD-88..93 PROPOSED 2026-06-13** — the six-family block (charter: `context/planning/2026-06-12_M7-M8-charter-skeleton.md`; authority: the 2026-06-12 merged disposition) → bundled DOCS review → Nick ratifies (watermark 87→93 then); (2) **B2 C8 `actorRef`** rides the SAME bundled review (automations stamp `AutomationId`; R14-A's Hubitat provenance evidence attached); (3) the M6.3-vs-M7 ordering call; (4) **M5-C Increment 1** (the W25 Lane-4 structural gate — see M5-C below); (5) automation MODULE_CONTEXT currency ✓ (30-permit correction, `e5ea76f`). M7 = 3 first-class pieces (M7.1 trigger/condition · M7.2 run/action/dispatch · M7.3 Pending Command Ledger), F5 event slices distributed per piece.

---

**M5 window — residuals only (window superseded by M6 execution).**

- **M5-A — ✅ COMPLETE** (`7f44bed`, 2026-06-07; build GREEN, 147 tasks). **Part 1+3** (`8028337`): the **platform-systemd** module populated — `PlatformPaths` (`LinuxSystemPaths` FHS + `LocalPaths` dev) and `HealthReporter` (`SystemdHealthReporter` via sd_notify + `NoOpHealthReporter`), leaf impls of the Doc 12 §8.2/§8.3 contracts, behind a package-private `NotifyTransport` seam; + `FloorId` Jackson registration. **Part 2** (`7f44bed`): the **AMD-87 `Expectation` persisted codec** — a hand-rolled interface-keyed tagged-union over the 4 permits (`ExactMatch`/`AnyChange` delegate their wrapped `AttributeValue` to the existing codec; `WithinTolerance` reuses the AMD-52 bit-anchored-float helpers), so **command-bearing `CapabilityAdded` now round-trips — the M9 prerequisite is CLEARED**. Lone JPMS change: `persistence requires com.homesynapse.device` (acyclic). No `projectionVersion`/migration/`@JsonTypeInfo` change.
- **M5-B/B1 — ✅ DONE (the crypto half of the M6 entry-gate).** **Doc 15 (Cryptographic Architecture) is the 15th design doc — LOCKED.** It owns: the event-log **hash chain** (keyless SHA-256 over stored bytes; INV-PD-08), **at-rest envelope encryption** (application-level, per-scope AES-256-GCM DEKs — never whole-DB; INV-PD-03), the **per-scope key-management infrastructure** (root → HKDF scope-KEK → wrapped DEK), **crypto-shredding** (key-destruction = data-destruction; INV-PD-07 — design MVP, *operation* post-MVP), and **Ed25519 package signing** (INV-PD-08). MVP roots on a machine-local key (zero-config); the honest threat model is stated precisely (protects key-excluding copies, NOT medium theft — that's Tier-2). **AMD-86** (narrows INV-PD-07's MVP mandate so operational crypto-shred is post-MVP; states the INV-PD-03 *partial*-at-MVP at-rest posture) + **AMD-87** RATIFIED; on-disk watermark **AMD-87**.
- **M5-D — evidence AUTHORED + independently reviewed (RATIFY-grade).** The **Pi-4 AES-256-GCM write-path microbench spec** (resolves **OQ-15-2** — the exact MVP encrypted-scope set, tuned against the Doc 15 §10 Pi-4 budget), the **energy/erasure interview guide** (carries the **AMD-86 §3** verifiable-erasure re-scope-up trigger), and the **sd_notify transport decision matrix** (OR-M13-SDNOTIFY). Awaiting Nick to RUN (Pi-4 bench + interviews + GraalVM/GenZGC spikes).
- **M5-C — website/docs floor** (non-preemptable, P6/D3) — **NOT STARTED after two consecutive windows → now STRUCTURAL: the W25 Lane-4 gate (no new Core coding instruction until Increment 1 is DONE) AND M7 entry-gate row 4.** The content backlog is evidence-rich post-R13/R14/R15 (merged disposition §2e: INV-CE-01 split-brain immunity, no-cloud-account flagship, the ledger-gap dossier, event-sourced explainability w/ pain citations, Data-Act/CRA, structural-absence claims, 3 copy guardrails).

**M6 execution state: see the M6 block at the top of this section** (3 of 4 pieces COMPLETE; M6.3 triple-gated; the four-piece charter, the E2 `com.homesynapse.app` composition-root bridge, and OR-M6-NONCE all executed as chartered — the bridge is delivered held-not-consumed in M6.2, consumed at M6.3).

---

**M4 — Foundation (projection/derivation + device-model expansion + integration-api freeze) — ✅ COMPLETE (2026-06-05, `8ef9e9f`).** Build GREEN (`./gradlew check --continue`, 145 tasks, incl. ArchUnit + spotless). `projectionVersion` = **5**; on-disk amendment watermark = **AMD-64**. All three workstreams shipped:

- **Workstream A — projection/derivation foundation — COMPLETE (typed end-to-end + event-time-deterministic).** M4.0a (atomic checkpoint coupling, AMD-45, `a441fdf`) → M4.0b-1 (`ProductionDerivationRule` + `DispatchingProjectionAdvancer` REC-28, `cf1a97e`) → M4.0b-2 (AMD-50 backfill + `projectionVersion` 1→2, `7610296`) → M4.0b-3 (AMD-51 typed comparator + 2→3, `98f705b`) → M4.0b-4a (relocate `AttributeValue` → new **`com.homesynapse.value`** leaf module to break a JPMS event↔device cycle; AMD-52 §11 erratum; `971cfa1`) → M4.0b-4b (AMD-52 typed `StateChangedEvent` payload + `{"t","v"[,"u"]}` tagged-union codec + schema-versioned replay + `projectionVersion` 3→4; `72596cb`) → M4.0b-5 (AMD-53 timestamp-model unifier — all three `EntityState` activity timestamps event-time-sourced; `projectionVersion` 4→5; `c99b425`).
- **Workstream B — device-model expansion — COMPLETE.** M4.B3 (AMD-47 `AttributeValue` 8-variant expansion + `AttributeValueUpcaster` SPI, `60b4185`) → M4.B-S1 (AMD-44 Stage 1: `FloorId` + `Floor`/`Area` records + `FloorRegistry`/`AreaRegistry` interfaces + `hardwareIdentifiers` `List`→`Set`, `e73e199`) → M4.B-S2 (AMD-44 Stage 2: `EntityRole` enum + `EntityType` 6×3 legality matrix + `Entity` 11→12 / `ProposedEntity` 3→4, `e76b925`).
- **Workstream C — integration-api interface freeze — COMPLETE.** M4.C (AMD-54..64, `8ef9e9f`): integration-api **22→40 types** (5 dot-namespaced `integration.*` lifecycle event records + 2 `capability.*` events `CapabilityAdded`/`CapabilityRemoved`; `CapabilityEvent` sealed iface; `CapabilityPublisher`/`CredentialRotator`; `SecurityServices`/`DiscoveryServices` aggregators; code-bearing `PermanentIntegrationException`; `HealthDetail`; `ReauthOutcome`/`ConfigUpdateOutcome`(+`REJECTED`)/`MigrationOutcome`/`CapabilityRemovalReason`/`IsolationLevel`; `BackoffParameters`; soft-deps; planned-restart-timeout). `IntegrationDescriptor` 8→14, `IntegrationContext` 10→12, `RequiredService` 3→5, lifecycle permits 5→10 — all with back-compat convenience ctors. **Contract-only freeze — supervisor impl = M9. NO `module-info`/Gradle/`projectionVersion` change.**

**Debt from M4.C — RESOLVED in M5-A Part 2.** The `Expectation` persisted sealed-type codec (the M4.C debt, tracked as ~AMD-65 then reassigned to **AMD-87** per the P2 ledger) is **DONE**: RATIFIED + IMPLEMENTED + committed `7f44bed`; the `capabilityAdded_onOff_roundTrips` acceptance test is un-`@Disabled` and GREEN (decodes to the real event, not `DegradedEvent`). **The M9 command-bearing-`CapabilityAdded` prerequisite is CLEARED.**

**M3 (Event Distribution + State Materialization) — COMPLETE** (2026-05-27, `78264a0`). Seven sub-milestones (M3.1–M3.7) across eighteen Claude Code work units.

### Next sequence (per the M4 retrospective + next-piece recommendation, 2026-06-05)

M4 is closed; the **M5 window is chartered + executing** (decisions D1–D8, 2026-06-06 — a blended, lane-tracked window). **M5-A COMPLETE** (`7f44bed`); **M5-B/B1** (the crypto entry-gate) **DONE** (Doc 15 LOCKED, AMD-86/87 RATIFIED); **M5-D** evidence authored + independently reviewed. **Next Core critical-path = M6 (Configuration + secrets/crypto) — entry-gate CLOSED 2026-06-09:** AMD-66/67/68/70/71 RATIFIED (incl. the Doc 06 `SecretStore.setAll(Map)` currency amendment = AMD-68; AMD-69 DEFERRED Tier-2/OQ-15-3); M6 chartered as four first-class pieces (P1); **M6.1 + M6.4 + M6.2 now COMPLETE (`9035110`/`62a81e6`/`7c73c91`) — only M6.3 remains, triple-gated.** The runway after M6.3-or-its-formal-deferral = **M7 (Automation)** — entry-gate forming: AMD-88..93 PROPOSED 2026-06-13 + the bundled C8/C9 DOCS review READY (see §1); the R14/R15 cycle + merged disposition are its evidence base. Still open: **OQ-15-2** (the MVP encrypted-scope set, via the M5-D Pi-4 microbench — gates M6.3 only, with the AMD-86 §3 interview signal + OR-M6-NONCE). Strategic note: Core is healthy and ahead of its own axis; the launch risk remains the non-Core tracks (website/docs, Web UI, distribution), now being addressed via the M5-C non-preemptable floor (P6/D3).

**Explicitly later:** configuration = M6; automation = M7/M8; **integration-runtime supervisor impl = M9** (implements the AMD-54..64 contracts just frozen); REST/WebSocket = M10/M11; Observability = M12; Lifecycle (full) = M13; **Zigbee = M14** (highest risk — real hardware; a dual-coordinator design spike SPIKE-DC is scheduled ~Aug); full integration + 72h validation = M15.

### Active governance

**Watermark = AMD-87 on disk** (raised AMD-64→87 at the 2026-06-07 M5-window crypto+codec ratification). **M6 config block: AMD-66/67/68/70/71 RATIFIED 2026-06-09 + AMD-69 DEFERRED (Tier-2/OQ-15-3) — reserved-below-watermark slots, ceiling unchanged; invariants §37–§41 registered (+8).** **M7 automation block: AMD-88..93 PROPOSED 2026-06-13** (above the watermark — ratification raises it to 93; 11 invariant candidates pending registration; AMD-91 formally supersedes AMD-04 at ratification). **B2 C8 (`actorRef` four-kind semantics) + C9 (energy event shape) PROPOSED 2026-06-08** — ride the same bundled DOCS review as the block. **M5 amendments: Doc 15 (Cryptographic Architecture) LOCKED; AMD-86** (INV-PD-07 crypto-shred MVP-scope narrow + INV-PD-03 at-rest posture; AMD-86-INV-01 §35) **+ AMD-87** (Expectation persisted codec; AMD-87-INV-01 §36), both RATIFIED 2026-06-07. **M5-window decisions D1–D8** locked (blended lane-tracked window; D2 crypto MVP scope). M3: AMD-41/42/43 APPLIED. **M4 amendments:** **AMD-44** (Floor/EntityRole — IMPLEMENTED via B-S1/B-S2), **AMD-45** (atomic checkpoint — M4.0a), **AMD-47** (AttributeValue expansion — M4.B3), **AMD-50** (version-transition backfill — M4.0b-2), **AMD-51** (typed comparator — M4.0b-3; §2.6 erratum applied), **AMD-52** (typed `StateChangedEvent` payload + §11 relocation erratum — M4.0b-4a/4b), **AMD-53** (timestamp unifier — M4.0b-5), **AMD-54..64** (integration-api freeze block, 11 amendments — M4.C, all RATIFIED 2026-06-05 via one DOCS-Project block review that caught AMD-56's unimplementable route-(a) trigger + AMD-55's undetectable void-reauth). **AMD-65 → reassigned AMD-87** (Expectation codec — RATIFIED + IMPLEMENTED in M5-A Part 2 `7f44bed`; M9 prereq CLEARED). **Invariants:** AMD-54..64 registered **29 invariants** at `Architecture_Invariants_v1.md` **§24–§34**; AMD-86-INV-01 at **§35** + AMD-87-INV-01 at **§36** (M5) — **index now 152 across 41 identifier categories** (REGENERATED from the §17 table at the 2026-06-09 M6-block registration; the previously stated "135/34" was a copied-forward under-count — do not propagate stale totals); AMD-51/52/53 at §21/§22/§23; AMD-47 at §20. INV-PD-03 (at-rest) + INV-PD-07 (crypto-shred MVP scope) amended by AMD-86. **P2 RATIFIED** (AMD renumbering: device 46–49, projection 50–52 fixed — gaps unused at 46/48/49; integration assign-at-milestone). DEC-M3-14..17 + D-09..12 locked.

**Build:** GREEN at **`7c73c91`** (147 tasks — full `./gradlew check` incl. ArchUnit + spotless + moduleGraphAssert; M6.2 went GREEN in zero gate-fix rounds). Commit chain since `7f44bed`: `6c6dd33` (1-line typo) → `b7bc65c` (M6.1b) → `9035110` (M6.1a) → `7e0bce8` (docs-only) → `62a81e6` (M6.4) → `7c73c91` (M6.2) → **`e5ea76f`** (docs-only automation MODULE_CONTEXT permit-count fix 27→30 — current HEAD; substantive HEAD `7c73c91`). Event manifest pins: **EventTypes 55 / CORE_PRODUCTION_EVENT_CLASSES 24 / EventCategoryMapping 36** (source-verified 2026-06-13). **Module added in M4: `core/value-model`** (`com.homesynapse.value`, leaf — holds the relocated `AttributeValue` hierarchy; 21 Gradle modules now). File/test counts last source-counted 2026-05-28 (**1,422** @Test / **724** Java files) + the M4 additions (value-model + the A/B/C surface) — not re-counted; a fresh source count is a low-priority follow-up logged in the backlog.

---

## 2. Implementation Order (DEC-M3-11, with approved reordering)

```
M3.1  InProcessEventBus core                ← COMPLETE (2026-05-16)
M3.2  REPLAY→TRANSITION→LIVE (bus-side)      ← COMPLETE (2026-05-17)
M3.3  Backpressure, metrics, observability   ← COMPLETE (2026-05-17)
M3.5a StateProjection vertical slice         ← COMPLETE (2026-05-18) a2aff9c
      Bus-fix Piece A (DerivedWriteRateLimit)← COMPLETE (2026-05-18) fceafe8
M3.5b StateProjection prod persistence       ← COMPLETE (2026-05-18) 08d0136
      Projection-checkpoint wiring WU         ← COMPLETE (2026-05-19) 56aaa4b
      Supervisor DLQ wiring WU                ← COMPLETE (2026-05-19) ed5862c
M3.4a Integration-test scaffold (Pi profile)  ← COMPLETE (2026-05-19) 5ae7912
M3.4b Sustained-load + crash-recovery tests   ← COMPLETE (2026-05-19) adf04d2

      ─── 2026-05-19 cross-tier audit (Cowork)
      ─── 2026-05-20 gap-closure + M3.6 design (Cowork)
      ─── WUCP Phase 2 reconciliation           ← COMPLETE (2026-05-19)

M3.6a Profile-driven persistence config      ← COMPLETE (2026-05-20) 17c40b6
M3.6b EventBusConfig + InProcessEventBus     ← COMPLETE (2026-05-20) df2743a
M3.6c Per-module event-class manifests       ← COMPLETE (2026-05-20) 38d3e30
M3.6d-a Composition-root satellite changes   ← COMPLETE (2026-05-20) 25bc23b
M3.6d-b PersistenceFactory + HomeSynapseCore ← COMPLETE (2026-05-21) dfb045e (4-commit cohort)
M3.6e.1 StateQueryService + REST gate        ← COMPLETE (2026-05-22) b71ed37
M3.6e.2 Admin endpoints + ArchUnit rules     ← COMPLETE (2026-05-22) 76288af
M3.7  E2E integration tests + checkpoint fix  ← COMPLETE (2026-05-27) [two Coder briefs]
M4.0a Atomic checkpoint coupling (AMD-45)    ← COMPLETE (2026-05-29) a441fdf
M4.0b-1..3 Derivation/advancer/typed cmp     ← COMPLETE (2026-05-29/30) cf1a97e/7610296/98f705b
M4.0b-4a/4b AttributeValue relocate + typed  ← COMPLETE (2026-05-31) 971cfa1/72596cb (AMD-52)
M4.0b-5 Timestamp-model unifier (AMD-53)     ← COMPLETE (2026-05-31) c99b425  [Workstream A done]
M4.B3 AttributeValue expansion (AMD-47)      ← COMPLETE (2026-05-30) 60b4185
M4.B-S1/S2 Floor/Area + EntityRole (AMD-44)  ← COMPLETE (2026-05-31/06-05) e73e199/e76b925 [Workstream B done]
M4.C Integration-API freeze (AMD-54..64)     ← COMPLETE (2026-06-05) 8ef9e9f  [Workstream C done — M4 COMPLETE]
```

M3.6d was sub-divided into d-a + d-b per the user's Option A decision. M3.6e was split into e.1 (StateQueryService + REST gate) and e.2 (admin endpoints + ArchUnit rules). M3.7 executed as two sequential Coder briefs (abandon/stub + checkpoint fix).

**M3 is COMPLETE** (eighteen Claude Code WUs, 2026-05-16–05-27). **M4 is COMPLETE** (`8ef9e9f`). **M5-A COMPLETE** (`7f44bed`) + **M5-B/B1 DONE** (Doc 15 LOCKED, AMD-86/87 RATIFIED, watermark **AMD-87**); M5-D evidence authored. Next: **M6 (Configuration + secrets/crypto)** — see the W24 plan + the M5-window decisions (D1–D8).

---

## 3. M3 Locked Decisions Ledger (DEC-M3-01 through DEC-M3-17)

| ID | Subject | Locking Authority | Key Constraint |
|----|---------|-------------------|----------------|
| DEC-M3-01 | Projection read/write discipline | AMD-41 §3.2.1 | Two-phase: READ then PUBLISH then CHECKPOINT. No interleaving. |
| DEC-M3-02 | Self-produced event detection | AMD-41 §3.2.2 | `SelfProducedFilter` (60s TTL, lazy eviction) + `stateVersion` defence-in-depth. |
| DEC-M3-03 | REPLAY→LIVE transition | AMD-42 §3.4.2 | Three-phase: REPLAY (catch-up) → TRANSITION (drain queue) → LIVE. |
| DEC-M3-04 (modified) | State projection checkpoints | AMD-41 §3.2.3 | MVP uses `ViewCheckpointStore`; `SqliteSnapshotStore` deferred. |
| DEC-M3-05 | Snapshot format | AMD-41 §3.2.3–4 | Jackson JSON with `snapshotVersion` + `projectionVersion` headers. V003 table created; impl deferred. |
| DEC-M3-06 (augmented) | Subscriber isolation | AMD-42 §3.4.4–6 | INV-SUB-ISO-01..06 catalog — per-subscriber VT, connection, DLQ, mode, queue, filter. |
| DEC-M3-07 | Coalescing | AMD-43 §3.6.5 | DEFERRED past M3. `coalesceExempt` retained but inert. |
| DEC-M3-08 (rejected, replaced) | Backpressure | AMD-43 §3.6.1 | No publish blocking on queue depth. Natural backpressure from single-writer. Rate limit (200/s) for StateProjection. |
| DEC-M3-09 | Clock injection | ArchUnit rule | Single `Clock` per JPMS module. `NO_DIRECT_TIME_ACCESS` enforced. NOT an AMD. |
| DEC-M3-10 | State_changed derivation | AMD-41 (scope) | Lives in `StateProjection` (core/state-store), NOT in writer. Writer is semantic-free. |
| DEC-M3-11 | Implementation order | PLAN-M3 §1.2 | M3.1 → M3.5a → M3.2 → M3.3 → M3.4 → M3.5b → M3.6 → M3.7. |
| DEC-M3-12 (modified) | Pi 4 support | AMD-43 §3.6.6 | Universal defaults at MVP. Platform-aware tuning deferred to M3.4 outcome. |
| DEC-M3-13 | Integration-test module placement | PLAN-M3 §8.2 | `testing:integration-tests` module — **created in M3.4a, 2026-05-19**. |
| **DEC-M3-14** | **Writer queue depth observation** | **M3.3 deliberation; Nick-approved 2026-05-17** | **Writer queue depth via `IntSupplier` injection at construction time. Overrides PLAN-M3 §7.2/§7.9. Re-open if multiple cross-module observable values emerge requiring the same pathway.** |
| **DEC-M3-15** | **M3.5a STOP gate removal pattern** | **M3.2 precedent; formalized M3.3; Nick-approved 2026-05-17** | **M3.5a STOP gates removed where the gated component is independently testable without StateProjection. Test: can the type be exercised with mock subscribers + injected deps without StateProjection code existing? If yes, gate removed.** |
| **DEC-M3-16** | **Composition-root visibility strategy** | **PM decision (2026-05-20)** | **InProcessEventBus → promoted to `public` (APPLIED M3.6b `df2743a`). SqlitePersistenceLifecycle → `PersistenceFactory` public gateway (APPLIED M3.6d-b `725353d`). QueueSaturationHealthCheck → promoted to public (APPLIED M3.6d-a `25bc23b`; transitive chain captured as DEC-M3-17). ALL THREE APPLIED.** |
| **DEC-M3-17** | **HealthSignal + HealthLevel public visibility (DEC-M3-16 addendum)** | **Implementation discovery during M3.6d-a; ratified by PM 2026-05-20** | **Promoted to public alongside QueueSaturationHealthCheck (`25bc23b`) because the constructor's `Consumer<HealthSignal>` parameter chain leaks both types; `-Xlint:exports` would have failed otherwise. The 3-type promotion chain (QueueSaturationHealthCheck + HealthSignal + HealthLevel) is the minimum viable visibility unit. Pattern lesson: pre-promotion `-Xlint:exports` verification must check transitively — every type appearing in the class's public constructor signature, public method signatures, public field types, and return types must itself already be public. See coder-lessons.md M3.6d-a entry #1.** |

No new decisions locked since DEC-M3-17 (2026-05-20). The 2026-05-19 audit's revised severities (C-01 BLOCKING→SIGNIFICANT; D1-04 SIGNIFICANT→MINOR; D2-01 NEARLY PLUGGABLE→PLUGGABLE; D3-06 SIGNIFICANT→INFO) are recorded in the audit report, not as DEC entries.

For full decision rationale and future re-opening conditions, see `PLAN-M3-CONSOLIDATED-02` §12 (searchable via project knowledge).

---

## 4. Workflow Architecture

### Three Claude Surfaces

| Surface | Role | Primary Output |
|---------|------|----------------|
| **This Claude Project** | PM / architect | Task instructions, design decisions, governance artifacts, architecture compliance |
| **Claude Code** | Java implementation | Production code, tests, MODULE_CONTEXT updates (**M3.1 through M3.7 executed via Claude Code — nineteen WUs**) |
| **Cowork** | Documentation, audits, design docs, context relay | Documentation updates, cross-tier audits, design sessions (e.g. 2026-05-19 cross-tier audit, 2026-05-20 gap-closure + M3.6 composition-root design), spot-check reviews |

Claude Code is the primary implementation surface. M3.1 through M3.7 validated the workflow across nineteen work units: PM generates task instruction → Claude Code executes in `acceptEdits` mode with `git commit/push/gradlew` denied → Nick reviews with `git diff`, runs build gate, commits. Cowork handles documentation-only tasks, audits, and design sessions where the output is markdown rather than code.

### Claude Code Configuration

- **Working directory:** `~/Desktop/Code/ClaudeFolder/homesynapse-core`
- **Permission mode:** `acceptEdits` (file writes auto-approved; bash commands require pre-approval)
- **Model:** Opus 4.7, effort `xhigh`
- **Denied commands:** `git commit/push/merge/reset/rebase`, `./gradlew`, `javac` — Nick owns the compile gate
- **Config files:** `.claude/settings.json` + `CLAUDE.md` at repo root (both `.gitignore`'d)

### nexsys-hivemind Repo

`nexsys-hivemind/` lives on Nick's machine (not synced to this Claude Project). It is the coordination layer between Claude surfaces:

- `context/` — PROJECT_SNAPSHOT.md, strategic-context-map.md, backlogs, weekly plans, audits
- `coder/` and `project-manager/` — Skill source files (writable copies)
- Cross-agent files: `coder-handoff.md`, `pm-handoff.md`, `cross-agent-notes.md`
- Skills mirror to this Claude Project at `/mnt/skills/user/nexsys-{coder,project-manager}/`
- `project-knowledge/` — Canonical source copies of all project knowledge files

### Work Unit Completion Protocol (WUCP)

Every work unit requires two phases before the next unit can start:
1. **Phase 1 (Coder):** Code written, tests pass, coder-handoff produced
2. **Phase 2 (PM):** PROJECT_SNAPSHOT updated, pm-handoff updated, backlog updated, drift check, dual skill-location sync verified

A stale hivemind (WUCP Phase 2 not run) blocks all forward work. The PM skill's freshness preflight enforces this.

**CURRENT:** **M6 entry-gate CLOSED (2026-06-09) — M6.1 READY TO ISSUE.** AMD-66/67/68/70/71 RATIFIED + AMD-69 DEFERRED (Tier-2/OQ-15-3); invariants §37–§41 (+8); **watermark AMD-87 (unchanged)**; `projectionVersion` 5; HEAD `6c6dd33`; build GREEN, 147 tasks. M5-A COMPLETE (`7f44bed`); M5-B/B1+B1-config DONE; M5-C floor NOT started (P6 risk); M5-D evidence awaiting Nick's runs (OQ-15-2 gates M6.3 only). W24 plan: `context/planning/weeks/2026-W24_jun08-jun14.md`.

---

## 5. Prompt Format Conventions

### Claude Code Task Instructions (Java implementation — PRIMARY)

Leaner than Cowork prompts because Claude Code can read the repo directly. Structure:

- Reference-by-path (point to files to read, don't inline their content)
- Constraint citations by identifier (LTD-11, AMD-26) — Claude Code looks up the full text
- Behavioral contracts stated precisely; implementation approach left to Claude Code's judgment
- MODULE_CONTEXT files listed as mandatory pre-reads
- STOP-on-Mismatch gates (verify file state before writing)
- Binary success criterion (`./gradlew :module:check` GREEN — Claude Code does NOT run this; Nick does)
- Completion report format at end

### Cowork Prompts (documentation, audits, design)

Self-contained documents. All context is inlined because Cowork has no persistent state. Used for documentation updates, cross-tier audits, design sessions, and hivemind artifact maintenance. The 2026-05-19 cross-tier audit and the 2026-05-20 gap-closure + composition-root design session are both Cowork outputs.

### Common Rules (Both Surfaces)

- Implementation classes default to package-private under JPMS
- Constructor signatures must be verified against actual source before being specified
- Tests inject `Clock` — no `Instant.now()`, `System.nanoTime()`, or `System.currentTimeMillis()`
- `JacksonWarmup` requires platform threads (not virtual threads)
- No compilation, Gradle runs, or build verification in prompts — Nick owns the compile gate

---

## 6. Open Items

### WUCP Phase 2 Reconciliation — COMPLETE (2026-05-19)

Six work units reconciled: Bus-Fix Piece A (`fceafe8`), M3.5b (`08d0136`), Projection-Checkpoint Wiring (`56aaa4b`), Supervisor DLQ Wiring (`ed5862c`), M3.4a (`5ae7912`), M3.4b (`adf04d2`). Two design sessions logged: cross-tier deployment audit (2026-05-19), gap-closure + M3.6 design (2026-05-20). `testing/integration-tests/MODULE_CONTEXT.md` populated. Freshness preflight: PASS.

**M3 COMPLETE. M4 COMPLETE (`8ef9e9f`). M5-A COMPLETE (`7f44bed`). M6 3-of-4 COMPLETE: M6.1 (`b7bc65c`+`9035110`) · M6.4 (`62a81e6`) · M6.2 (`7c73c91`); M6.3 triple-gated (OQ-15-2 + AMD-86 §3 interviews + OR-M6-NONCE — the M6 critical path, Nick-paced).** Doc 15 LOCKED; AMD-66..71 block RATIFIED/DEFERRED 2026-06-09; watermark AMD-87 on disk. **R14/R15 cycle COMPLETE 2026-06-12** (merged disposition = THE M7 authority; high-water REC-185). **M7 entry-gate forming: AMD-88..93 PROPOSED 2026-06-13; bundled DOCS review (block + B2 C8/C9) READY TO DISPATCH; M5-C Increment 1 = the Lane-4/row-4 gate (NOT started).** Next forward = Nick dispatches the bundled review → PM folds the return + ratification mechanics → M7.1 instruction on a green 5-row entry-gate. See §1 + the W25 plan in `nexsys-hivemind/context/planning/weeks/2026-W25_jun15-jun21.md`.

### Audit Findings Folded into M3.6 (2026-05-19 cross-tier audit + 2026-05-20 design)

| Audit ID | Description | Closes in | Status |
|---|---|---|---|
| C-01 | DeploymentProfile not wired into DatabaseExecutor (hardcoded `cache_size=-128000`, `mmap_size=1073741824`) | M3.6a | **CLOSED** (2026-05-20) |
| D1-05 | `busy_timeout=5000` hardcoded; Docker Desktop / NAS need different values | M3.6a | **CLOSED** (2026-05-20) |
| D1-07 | `ReplayWindowQueue.MAX_CAPACITY=10_000` hardcoded; Enterprise burst risk | M3.6b | **CLOSED** (2026-05-20) |
| D1-13 | `readThreadCount=2` default; under-provisions 64-core servers | M3.6a | **CLOSED** (2026-05-20) |
| D2-11 | `PersistenceLifecycle` Javadoc references WAL/PRAGMAs (leaks impl into public interface) | M3.6a | **CLOSED** (2026-05-20) |
| D3-08 | `DerivedWriteRateLimit.refill()` + `QueueSaturationHealthCheck.tick()` scheduler not wired | M3.6d-a | **CLOSED** (2026-05-20) — `SharedScheduler` skeleton wired both via `safelyInvoke(rateLimit::refill)` + `safelyInvoke(healthCheck::tick)`; actual instantiation lands in M3.6d-b composition root |
| D4-09 | Enterprise REPLAY overflow restart loop on burst | M3.6b | **CLOSED** (2026-05-20) |
| D5-04 | Docker Desktop WAL-shm incompatibility (`locking_mode=EXCLUSIVE` needed) | M3.6a | **CLOSED** (2026-05-20) |

Audit findings NOT addressed in M3.6 (stay open as documented MINOR per audit verdict):
- D1-02 (`page_size` as profile field) — MINOR
- D1-16 (thread-name PID prefix for multi-instance) — MINOR
- D1-19 / D5-08 (cross-platform storage-type detection beyond Linux `mmcblk`) — SIGNIFICANT, deferred to a future operational-resilience WU
- D5-09 (backup not implemented) — SIGNIFICANT, deferred per PERSISTENCE plan (post-M2 scope)

### Gap-Closure Q1–Q4 Outcomes (2026-05-20 Artifact 1)

| Q | Answer | M3.6 impact |
|---|---|---|
| Q1 — `globalPosition` contiguity | Gap-tolerant by construction. No `position + 1` arithmetic anywhere in `core/`. `readFrom(pos - 1, 1)` idiom is exclusive-`afterPosition` semantics, not contiguity. | None. Optional `EventStore.readFrom` Javadoc clarification rides along with M3.6a if convenient. |
| Q2 — `chain_hash` cross-backend | Reserved schema, not active. `ZERO_HASH` bound unconditionally. Multi-writer safe today. | None. AMD-37 annotation deferred to crypto-chain WU. |
| Q3 — Event type registration | Static list at composition root (per DECIDE-04). Each module publishes `public static final List<...>`. | M3.6c (new `EventTypes.CORE_PRODUCTION_EVENT_CLASSES` + `IntegrationEvents.LIFECYCLE_EVENT_CLASSES`). |
| Q4 — `home_id` on `EventEnvelope` | 14-field envelope; `home_id` populated on every write but never read back. | Defer to multi-hub WU. No optional accessor. |

### Tracked Follow-Ups from M3.5b / Wiring WUs (largely resolved)

**Projection-checkpoint wiring — RESOLVED** (2026-05-19 `56aaa4b`).
**Supervisor DLQ wiring — RESOLVED** (2026-05-19 `ed5862c`).
**SqliteStateStore implements StateCheckpointSource — RESOLVED** (2026-05-20 `25bc23b` / M3.6d-a). `serialize(int)` renamed to `serializeCheckpoint(int)` and promoted to public via the interface; `loadedProjectionVersion()` promoted to public via the interface. Class itself remains package-private — only the two interface methods are externally visible.
**Composition-root wiring — COMPLETE** (M3.6d-a `25bc23b` + M3.6d-b `dfb045e` + M3.6e.1 `b71ed37` + M3.6e.2 `76288af`). M3.6d-a shipped skeletons. M3.6d-b shipped the actual wiring: `PersistenceFactory` (public gateway), `HomeSynapseCore` (12-step bootstrap). M3.6e.1 expanded to 14-step bootstrap: added `MaterializedStateQueryService` wiring + Javalin HTTP server on port 7070 with readiness filter. M3.6e.2 expanded to 16-step bootstrap: added entity query endpoints + admin endpoints via `RestFilters` gateway methods. The composition root is now externally queryable with full endpoint coverage.

### Tracked Items from M3.6e.2 (2026-05-22) — ALL RESOLVED

**OR-M3-17 — FULLY CLOSED (M4.0b-1, `cf1a97e`, 2026-05-29).** The M3.7 interim was the no-op `MINIMAL_DERIVATION_RULE = context -> List.of()` lambda (there is **no** `MinimalDerivationRule` class — that was a phantom). M4.0b-1 retired the no-op lambda and shipped the real production **`ProductionDerivationRule`** (package-private in `com.homesynapse.state`, string change-detect, publishes a derived `state_changed` on LIVE so the `attributes` map populates), reached via the `DerivationRule.production()` gateway (DEC-M3-16). M4.0b-2 then added the AMD-50 version-transition backfill on top.

**OR-M3-18 — FULLY CLOSED (M4.0b-1, `cf1a97e`, 2026-05-29).** The M3.7 interim `MinimalProjectionAdvancer` (package-private lifecycle class) is **DELETED**. M4.0b-1 shipped the real **`DispatchingProjectionAdvancer`** (Research 8 REC-28 — package-private in `com.homesynapse.state`, constructor-injected `EnvelopeHandler` map, no `ServiceLoader`, forward-all → exact cursor parity), reached via the `ProjectionAdvancer.dispatching(EventStore)` gateway.

### Tracked Items from M3.6e.1 (2026-05-22)

**OR-M3-15 — Xlint:exports gateway pattern — RESOLVED.** `ReadinessFilter` (public) referenced `io.javalin.http.Handler` from non-transitive `requires io.javalin`. Fix: demote `ReadinessFilter` to package-private, create `RestFilters` public gateway with `Object`-typed parameter per DEC-M3-16 pattern. Pattern codified for future REST endpoints: any public class in an exported package that references a framework type from a non-transitive dependency must use the gateway pattern.

**OR-M3-16 — Gradle/JPMS scope alignment — RESOLVED.** `requires transitive com.homesynapse.state` in rest-api module-info required `api(project(":core:state-store"))` in build.gradle.kts (was `implementation`). Rule: `requires transitive` → `api`; plain `requires` → `implementation`. Lesson added to coder-lessons.md.

### Tracked Items from M3.6d-a (2026-05-20)

**OR-M3-13 — Reconciliation records metadata in data slot — RESOLVED (2026-05-29, M4.0a `a441fdf`).** `StateCheckpointSource.serializeCheckpoint(...)` was extended to accept `reconciledAt`/`reconciledFromVersion`/`reconciledToVersion`; `StateProjection.initialize()` populates them on the version-mismatch reconciliation; `SqliteStateStore` writes them instead of `null`. `ReconciliationTest`'s 5th method (`reconciliationRecordsMetadataInDataSlot`) is un-deferred and passing (asserts `reconciledToVersion == 2`). **M4.0b-2's backfill gate binds to `reconciledToVersion`.** AMD-41 §3.2.4's metadata-recording requirement is now met.

**OR-M3-14 — M3.6d-b prerequisite infrastructure — RESOLVED** (2026-05-21 `dfb045e`). All three prerequisite infrastructure gaps closed in M3.6d-b's 4-commit cohort: `WriteCoordinator.queueSize()` at `a33ee40`, production `SqliteSubscriberReadConnectionFactory` at `a59b64e`, `SqlitePersistenceLifecycle` 6-store expansion + `PersistenceFactory` at `725353d`.

**Tier 9 reconciliationOnVersionMismatch test — RESOLVED** (2026-05-20 `25bc23b` / M3.6d-a). Un-disabled and implemented (subscribe → wait LIVE → unsubscribe → externally reset checkpoint to 0 → re-subscribe → assert 10 events re-replayed). M3.2 carry-forward gap #1 closed.

### Hardening Items from Cowork Review (2026-05-18)

**H1: CheckpointSerializer size guardrail — RESOLVED** (2026-05-19).
**H2: AtomicCheckpointWriter code duplication.** Two-way and three-way methods duplicate transaction wrapper. Extract shared `executeInTransaction` helper. Standalone cleanup or fold into M3.6d.
**H3: No concurrent access tests for SqliteStateStore.** ConcurrentHashMap is correct by construction but unproven under concurrent load. Fold into M3.4b (sustained-load) or M3.7 (E2E).
**H4: Post-shutdown defensive handling across all SQLite stores.** `park()` after `DatabaseExecutor.shutdown()` throws uncaught `RejectedExecutionException`. Pre-existing pattern. Fold into M3.7 or dedicated hardening pass.
**H5: event-bus MODULE_CONTEXT type count — RESOLVED.** 32 top-level types (14 public + 18 package-private) verified correct.

### Tracked Items from Supervisor DLQ Wiring (2026-05-19)

**Supervisor retry loop activation.** `computeBackoff()`, `sleepForBackoff()`, `MAX_RETRIES = 5` are dead code. Current behavior parks on first failure (`attemptCount = 1`). Activating the retry loop is a separate WU that also requires moving `recordCrash()` to the post-exhaustion path.
**`PersistentDlqWriter.noop()` wired but exercises no real persistence — RESOLVED in M3.6d-b.** `HomeSynapseCore` wires `persistenceFactory.deadLetterWriter()` (which returns `PersistentDlqWriter` backed by `SqliteDeadLetterStore`) into the bus's DLQ path.
**`DeadLetter.diagnostics` is null.** Stack-trace serialization deferred to a future enhancement.

### Tracked Items from M3.4a (2026-05-19)

**Pi-profile gate behind `-PpiProfile=throttled`.** Default `./gradlew check` does NOT run BurstLoadIT or HeapBudgetIT. Operators must explicitly enable. Documented in `testing/integration-tests/build.gradle.kts`.
**`testing/integration-tests/MODULE_CONTEXT.md` — RESOLVED.** Populated during WUCP Phase 2 reconciliation (2026-05-19).
**M3.4b sustained-load tests planned.** Optional `-PsustainedMinutes` override exists in the build script (default 60, CI proposed 10). Tests are tagged `@Tag("soak")` and run manually pre-release per PLAN-M3 §13.8 default. M3.4b is the next milestone after reconciliation.

### Tracked Items from M3.4b (2026-05-19)

**Pi4SustainedLoadIT event-count tolerance.** Task instruction specified ±2% tolerance; implemented as lower-bound 25%. The ±2% was a calibration error — ThrottledWriteCoordinator's 10ms baseline makes 100 ev/s unachievable under the test's own throttling profile. The lag-bound assertion (≤50 events) is the load-bearing check. PM accepted this deviation.
**CrashRecoveryIT @TempDir cleanup on Windows.** Uses `CleanupMode.NEVER` because abandoned harness holds SQLite file handles. Temp directories accumulate. OS handles cleanup.
**BusMetricsRecorder reuse.** Reused from `EventBusContractTest` (public static nested class) rather than extracting to a standalone testFixtures class. Acceptable for now; extract if M3.6d or M3.7 needs it.
**Full 60-minute sustained-load test on hs-dev-1 not yet run.** The 10-minute desktop run validates mechanism. The 60-minute Pi 5 run validates endurance. Schedule for pre-M3.7 or a quiet evening.
**scripts/pi4-validation.sh not yet exercised on hs-dev-1.** Created and chmod +x verified on Windows. First on-device run is manual.

### Tracked Gaps from M3.2

**Defence-in-depth for EventPublisher.publish from REPLAY mode** — Production `EventPublisher` guard is deferred to persistence module Phase 3. M3.5a implemented the first layer (StateProjection checks mode). Not blocking.
**`bus.resume()` does not re-spawn the VT** — Pre-existing M3.1 limitation. Blocks the Tier 9 `reconciliationOnVersionMismatch` bus-side test. Tracked for a dedicated bus-fix Piece B WU (separate from Piece A which is complete).
**Overflow test is slow (~5-15s)** — `replayWindowOverflowAt10000IsCriticalAlert`. Consider `@Tag("slow")` if test suite time becomes a concern.

### Tracked Items from M3.3

**JFR-native emission is accepted design debt.** Typed primitive adapter layer needed when a pull-based metrics consumer (Prometheus/OTLP) is introduced — likely M4+.
**Publish-latency metric measures bus-side fan-out, not end-to-end.** End-to-end publish latency is a persistence-module metric for a future observability pass.
**`lagEvents` is an approximation.** Under-reports by one delivery interval during burst catch-up. If M3.4b reveals insufficiency, add a `LongSupplier writerTailSupplier` following the DEC-M3-14 pattern.

### Tracked Items from M3.5a

**`StateProjection.processBatch` does not advance cursor on partial publish failure.** State mutations applied inside the read-tx callback are NOT rolled back. Crash recovery replays from the last checkpoint. Not blocking.
**`Map.copyOf` and null attribute values.** `EntityState.attributes()` may contain null values per the contract; `Map.copyOf` throws on nulls. All code paths use `LinkedHashMap` or `HashMap` instead. Any future refactor to `Map.copyOf` is wrong.

### JPMS Lessons

**`jdk.jfr` requires an explicit `requires` directive (M3.3).** PM-originated error corrected by Coder.
**Verify visibility modifiers against source, not documentation (M3.5a — G4).** When a PM brief states a type is public, verify by reading the source declaration line. M3.3 landed `DerivedWriteRateLimit` as package-private despite plans; M3.5a introduced `DerivedPublishGate` adapter; Bus-Fix Piece A subsequently promoted to public.

### Documentation Updates Deferred (per Q2 / Q4 of gap-closure)

**AMD-37 cryptographic-chain activation annotation** — deferred to the crypto-chain WU (post-MVP). The `chain_hash` column is reserved schema today (always `ZERO_HASH`); activation requires single-writer or partition-local chain construction.
**AMD-34 / `EventEnvelope.homeId` Java-side exposure** — deferred to multi-hub WU. Column populated, never read back. Breaking record-constructor change has no MVP consumer.

### Standing Items

**Test Hardening Backlog (TB-01 through TB-16):** 21 test additions across 12 groups. Foldable into M3 sub-milestones opportunistically.
**Cloud-Readiness Test Additions:** 21 additions organized by cloud tier. Foldable into M3+ work.
**Doc 05 §3.14 Amendment:** Specify event-based communication path for planned restart. Believed still open.
**Academic Research:** GCVSP benchmark on HomeSynapse TCA schema. Background activity.

---

## 7. Quick Reference

```bash
# Build
./gradlew check                                                # full build: compile + test + Spotless + ArchUnit + dependency rules
./gradlew :core:state-store:check                               # single module
./gradlew :testing:integration-tests:test \
    -PpiProfile=throttled -PsustainedMinutes=10                 # M3.4a+M3.4b Pi-profile integration tests (5 tests, ~40 min)
scripts/clean.sh                                                # clean before full check runs

# SSH to Pi 5
ssh pi                                  # via Tailscale, username: homesynapse

# Repos
git@github.com:nexsys-io/homesynapse-core.git        # source code
git@github.com:nexsys-io/homesynapse-core-docs.git   # design/governance (including 2026-05-20 audit-gap-closure + M3.6 design)
# nexsys-hivemind — local on Nick's machine, not on GitHub

# Claude Code
cd ~/Desktop/Code/ClaudeFolder/homesynapse-core
# Config: .claude/settings.json (acceptEdits, deny git commit/push/gradlew)
# Context: CLAUDE.md at repo root
# Both are .gitignore'd

# Today's design artifacts
homesynapse-core-docs/research/2026-05-20_M3_Audit_Gap_Closure_v1.md     # Q1-Q4 answers
homesynapse-core-docs/design/2026-05-20_M3.6_Composition_Root_Design.md  # M3.6a..M3.6e WU sequence
nexsys-hivemind/context/audits/2026-05-19_cross-tier-deployment-audit.md # 2026-05-19 audit report
```

---

**Last verified against:** `homesynapse-core` **`8ef9e9f` (M4 COMPLETE)** on 2026-06-05. Workstreams A+B+C done; **AMD-44..64 ratified, watermark AMD-64**, `projectionVersion` 5; AMD-65 (Expectation codec) QUEUED BLOCKING-for-M9; 29 integration invariants registered §24–§34. Next: M5 (Platform API + test-support) + the W3 website/docs standup.

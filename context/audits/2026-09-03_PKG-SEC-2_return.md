<!--
file: context/audits/2026-09-03_PKG-SEC-2_return.md
purpose: Coder-lane return for PKG-SEC-2 — the zigbee schema admission at Phase-1 validation (R-4 C-1); Row 13 RULED (a′). 8 M + 2 A.
instruction: context/instructions/2026-09-02_coder-lane_PKG-SEC-2_zigbee-schema-admission_coding-instruction_RULING-SLOTTED.md
lane: host-side Claude Code Coder, Windows desk (Git Bash; JDK 21.0.4; Gradle 8.8 --offline), 2026-09-03 06:45–07:30 CDT.
-->

# PKG-SEC-2 return — the zigbee schema admission at Phase-1 validation

## §0 One-screen summary

**Verdict: DELIVERED, uncommitted, in-lane gates GREEN — ONE [REVIEW] the hub must rule BEFORE Nick commits (§0.2).** (a′) honored: `HomeSynapseCore.registerIntegrationSchema` QUEUES before `start()` (no throw); Phase 1 drains the queue AFTER `registerCoreSchema(automation)` and BEFORE `load()` (new private `installSchemaRegistry`; queue + publication under a new `schemaLock`, LTD-11); after publication the call registers directly. `Main.integrationSchemaFragments()` (zigbee) is supplied right before `manager.start()`; the post-start W10 call is REMOVED. Queue over ctor parameter: zero new overloads. **ZERO commits by the lane.**

**§0.1 Doc 12 conflict check — the instruction's premise is WRONG; PROCEEDED.** Doc 12 §3.3 :133 DOES carry the sentence: "core-only schema composition (integration schemas are not yet available — they are registered after Phase 6 integration discovery) … After Phase 6 integration discovery, the Configuration System recomposes the full schema including integration schemas and revalidates the integration configuration sections." Doc 06 §3.2 :127: "Schema composition occurs once during startup, after integration registration and before configuration validation."; C7 :477: "The schema written to disk at startup includes all registered core and integration schemas." Reading: :133 describes a mechanism the code never built (no post-Phase-6 revalidation exists) on a retired premise (ServiceLoader discovery, retired by DECIDE-04); it does not prohibit earlier composition, and (a′) delivers its intent at Phase 1 as Doc 06 §3.2 + C7 prescribe. If the hub reads :133 as normative, this WU waits for a Doc 12 correction note.

**§0.2 [REVIEW — rule before commit] the fragment's `permit_join_duration` `default: 120` was REMOVED (one line; the revert is one line).** Contract 3 ("keys keep their defaults") contradicts contract 4 ("no config-key change"), the source and the measurement: `ZigbeeIntegrationAdapter:87–:93` "Conservative default is LAW: an ABSENT key opens NOTHING; the schema's `default: 120` is documentation-side"; `openPermitJoinWindow():774` returns on an empty Optional; R-4 §6-iv measured "absent key ⇒ no window". That held ONLY because the fragment never composed: composed at Phase 1, Doc 06 §3.1 stage 4 (`mergeDefaults`, `StandardConfigurationService:956–:1008`) inserts `permit_join_duration: 120` on EVERY boot, block absent or not → `permit_join_opened: duration=120s` at every start, the network open for joins without operator intent. Shipped: the default dropped (the `$comment` + description say why); the M9.4-PJ semantic (absent ⇒ no window · set ⇒ one window per boot) unchanged, now schema-honest. Pinned: lifecycle T3/T7/T7b + app `zigbeeFragment_declaresNoPermitJoinDefault`; **mutation-proven**: default restored ⇒ EXACTLY 4 FAIL; sha256-identical revert ⇒ GREEN. Consequences: (1) `integrations.zigbee` now ALWAYS exists as a section carrying the benign defaults (watchdog 30 · topology 0 · telemetry 10 · `availability.*` · `route_health.*` — none read by the adapter); (2) an out-of-range value (999) is a §3.6 ERROR at Phase 1 → key REMOVED, boot continues, NO window; (3) Doc 08 §9 :871 "Default 120" is documentation-only.

**Census: exactly 10 (8 M + 2 A)** at HEAD `a1c6966` (clean at launch; no prior return, no dirty paths). `git --no-optional-locks status --porcelain`:
```
 M app/homesynapse-app/MODULE_CONTEXT.md
 M app/homesynapse-app/src/main/java/com/homesynapse/app/Main.java
 M config/configuration/MODULE_CONTEXT.md
 M integration/integration-zigbee/MODULE_CONTEXT.md
 M integration/integration-zigbee/src/main/java/com/homesynapse/integration/zigbee/ZigbeeIntegrationFactory.java
 M integration/integration-zigbee/src/main/resources/schema/zigbee-config-schema.json
 M lifecycle/lifecycle/MODULE_CONTEXT.md
 M lifecycle/lifecycle/src/main/java/com/homesynapse/lifecycle/HomeSynapseCore.java
?? app/homesynapse-app/src/test/java/com/homesynapse/app/MainSchemaFragmentsTest.java
?? lifecycle/lifecycle/src/test/java/com/homesynapse/lifecycle/HomeSynapseCoreSchemaAdmissionTest.java
```
Source 4 M (2 instructed + 2 zigbee — the resource and the `configSchemaJson()` "after Phase 6" Javadoc, §0.2) · MODULE_CONTEXT 3 M + config `:173` (D-f) · 2 A. ZERO module-info / build / catalog / event diffs. The dev-run `config.schema.json` exhibit is git-UNTRACKED.

**Gates:** `./gradlew` {lifecycle:lifecycle · app:homesynapse-app · integration:integration-zigbee} × {compileJava · test · spotlessCheck} `--continue --offline` → **BUILD SUCCESSFUL in 24s** (76 tasks, 18 executed) · zero `-Werror` warnings · every touched task executed fresh · result XML **lifecycle 62 → 75 · app 24 → 27 · zigbee 581/581**, 0 fail/error/skip, mtimes 12:07:03–:10Z · clock/`synchronized`/`System.out`/`Thread.sleep` greps clean on every new line · LF on all 10 (python-verified) · re-run after LF-normalizing the A files: GREEN.

**Deferred Build Gate: YES.** `./gradlew check` NOT run on this desk (the app suite ran `HomeSynapseArchRulesTest` 11/11 incl. `NO_DIRECT_TIME_ACCESS` over lifecycle main) — owed against Nick's commit of exactly these 10 paths atop `a1c6966`; the gate of record = CI on the push (law 16).

**Red-first (staged):** HEAD main + the new class → **13 run / 13 RED**, every one `IllegalStateException` (the guard IS the defect); the app tree compile-red by absence. Stage A (queue seam live, Main supplies, drain inert) → **13 run / 11 RED for the right reasons · app 27 run / 1 RED**. Stage B → 75/75 · 27/27.

| T | Scenario | Pred. | A | B |
|---|---|---|---|---|
| T1/T1b | well-formed block (+ the measured `!include` layout) → ZERO issues | RED | RED (the R-4 line verbatim) | ok |
| T2 | `notatype` + `bogus_top_level` → exactly 2 WARNINGs, zigbee clean | GbC | RED (3) | ok |
| T3 | `permit_join_duration: 999` → `[ERROR]`, boot continues, key REMOVED | RED | RED (WARNING instead) | ok |
| T4 | the C7 cache carries `integrations.properties.zigbee` (= the registry) | RED | RED (empty node) | ok |
| T5 | post-start `mqtt`: no throw, in-memory recompose, cache UNTOUCHED, `stage=direct` | GbC + pin | RED (no INFO) | ok |
| T6/T6b | pre-start no throw, `schemaRegistry()` null · last-per-type wins | RED | GREEN / RED | ok |
| T7/T7b | EMPTY / ABSENT block → zero issues, defaults, `permit_join_duration` ABSENT | RED | RED / RED | ok |
| T8 | one INFO per fragment, `stage=pre-load`, in order | RED | RED | ok |
| T9/T9b | NPE/IAE guards · a malformed fragment fails the boot in Phase 1 → STOPPED | RED | GREEN / RED | ok |
| app x3 | supply keyed by type = the resource · unmodifiable · NO permit-join default | compile-red | GbC x2 · RED | ok |

**D-f sweep (CLASSIFY, never blind-replace) — ONE correction.** `config/configuration/MODULE_CONTEXT.md:173` (the LTD-09 row "config in `/etc/homesynapse/`", a today-FALSE config-YAML claim) → **CORRECTED** to `PlatformPaths.configDir()`: the FHS target (E4, unwired) vs the MEASURED root `$HOMESYNAPSE_HOME/config` = `/var/lib/homesynapse/config/` (`homesynapse.yaml` + `integrations/zigbee.yaml` via `!include`). KEEP, by class: `distribution/README.md:98` (today "env drop-in only") · `README.md:105` (conditional M13 forward claim) · `docs/boot-contract-map.md:33` + `docs/escalations.md:51` (today-correct) · `scripts/dev/pi-health.sh:187,:193` (FHS directory-presence census) · `config/…/MODULE_CONTEXT.md:300` (quotes Doc 06's stale `schema/`; root-agnostic) · `platform/platform-systemd/MODULE_CONTEXT.md:33` (source-true `LinuxSystemPaths` description) · the 9 expected keeps outside the six (unit/env/deb scripts, the two Javadocs).

**INV/LTD sweep:** LTD-11 MET (`schemaLock` a `ReentrantLock`, never across I/O) · LTD-15 MET (2 tokens, test-asserted) · LTD-09 MET · INV-CE-02 MET (T7/T7b) · INV-CE-03 + C7 MET (T4) · Doc 06 §3.6 tiers MET as read · Doc 12 §3.3 fatal semantics MET (`load()` still first; a malformed bundled fragment is ALSO fatal, T9b) · C12-01/C12-09 UNAFFECTED · M3.6e.1 gateway MET (java.base-only surface; no module-info change) · SK-INV-02 MET (no wall clock; tests `Clock.fixed`) · REG-INV-1 / INV-ES-* / INV-RF-01 UNAFFECTED.

**Instrument limits:** `check` deferred; the hardware-free ITs still register post-start (the pre-start supply is proven at the lifecycle level, not in an IT); the packaged boot is proven only by R-4b's rig check — `journalctl -u homesynapse.service -b --no-pager | grep -c 'Configuration issue'` → **0** + exactly one `lifecycle.integration_schema_registered: type=zigbee stage=pre-load` (and NO `permit_join_opened` with the key unset). The instruction cites no integration-zigbee MODULE_CONTEXT lines. **CT filing date: 2026-09-03** (07:30 CDT; msys `TZ=` fallback avoided).

## §1 Deviations

- **[REVIEW]** §0.2 (the default removed; 3 integration-zigbee files touched out of the file table) · §0.1 (the Doc 12 premise) · the remaining defaults become operative (consequence (1); the hub's call).
- **[INFO]** the queue shape (no ctor parameter) · the second token value `stage=direct` (law 17) · `Main.integrationSchemaFragments()` as a package-private supply seam + the 3-test app pin · `HeroLoopHardwareFreeIT:357` untouched (the direct path, lawful).

## §2 Follow-ons (proposed, not shipped)

(1) the Doc 12 §3.3 :133 correction note · (2) the Doc 08 §9 :871 default row · (3) re-time the hero IT's registration pre-start · (4) gotcha #10 as a standing rule · (5) R-4b intake: the rig-check lines above. The commit message is hub-authored at the audit (`_scratch/2026-09-03_core_PKG-SEC-2_commit-msg.txt`).

<!--
file: context/assessments/2026-07-02_plugin-ecosystem-wars_research-dossier.md
purpose: Phase-A deliverable of the Doc-18 research-and-charter lane — deep, web-backed study of how smart-home platforms and best-in-class plugin ecosystems won, lost, and scarred their users (extension/plugin architecture specifically). Produces the evidence base and the numbered lessons ledger (L-1..L-33) that the Doc-18 requirements charter cites by number.
audience: the PM hub (two-layer audit before anything folds into Doc 18 authoring); Nick (decision points route via the charter); the future Doc-18 author.
state-type: assessment (research return; write-isolated). Companion deliverable: context/planning/2026-07-02_Doc-18_requirements-charter.md.
status: RETURNED 2026-07-02 (final, not DRAFT) by the Doc-18 research lane per the 2026-07-02 dispatch brief. Baseline re-verified at launch: core ec2e3b4 · docs 1509b34 (AMD-97; invariants 172/51) · hivemind 7d65b35 · bench 5ceff3b.
sources-discipline: ANTI-FABRICATION ENFORCED (the 2026-06-27 return's format). Every load-bearing claim is tagged [VERIFIED — source id] (primary source fetched 2026-07-02; where it says it recorded), [INFERRED — from what], or [UNVERIFIED — why it stays in]. Per-platform source tables at each section; only opened links are VERIFIED. Six of the most load-bearing sources were re-fetched lane-direct as a second layer (marked ✓✓ in tables); the rest were fetched by the research subagents this session (agent ids in §4).
does-not-relitigate: Matter V1 deferral (ruled), converter-DB licensing (confirmed 2026-06-27), HA explainability trajectory (covered 2026-06-27), AIoT safety-frame consensus (confirmed 2026-06-27).
-->

# Plugin-Ecosystem Wars — Research Dossier (Doc-18 evidence base)

**Reading key.** §1 = per-platform findings (model · distribution/trust · versioning · community · sharpest failure · most brilliant idea). §2 = the cross-cutting answers the charter needs. §3 = the lessons ledger **L-1..L-33** the charter cites by number. §4 = provenance. Source ids like [HA-4] resolve in the table at the end of each platform section; ✓✓ marks a source re-fetched lane-direct on top of the subagent fetch.

**Bottom line.** Across nine ecosystems, the same shapes recur. The platforms that kept their communities did four things: told the truth about isolation instead of promising sandboxes they couldn't deliver; moved extension capability out of imperative code into declarative, reviewable data; ran a two-tier core/community split with an explicit, machine-tracked quality ladder; and treated breaking changes as a contract (notice + auto-migration + parallel old-path). The two famous ecosystem-breakers (SmartThings Groovy→Edge, Chrome MV2→MV3) share one signature: a kill date announced before the replacement reached parity. Nobody surveyed vendor-paywalls community content. Bus-factor-1 is the default state of extension infrastructure everywhere, at every layer. And every marketplace's 2025–26 security posture converged on the same stack — identity, per-version automated scanning, signing, kill-switch — because manual review scaled at none of them.

---

## §1 Per-platform findings

### 1.1 Home Assistant — the four-surface split and the quality ladder

**Extension model.** Four surfaces with sharply different isolation. Core integrations: in-tree Python, shipped with releases, identified by a unique immutable `domain` [VERIFIED — HA-6]. Custom integrations: same code shape dropped in `custom_components/`, loaded **in-process by the same loader, which checks custom before built-in** — a custom integration can shadow a core one by domain (sanctioned, discouraged, UI-flagged) [VERIFIED — HA-7]. Add-ons ("apps"): Supervisor-managed containers with a 1–6 security rating, default protection mode, AppArmor, scoped Supervisor-API roles, Cosign image signing [VERIFIED — HA-8, HA-9]. Blueprints: data-only parameterized automation configurations shared via the forum [VERIFIED — HA-15]. HA thus runs the whole isolation ladder simultaneously: unsandboxed in-process, container-isolated, and data-only.

**Distribution & trust.** Core's gate is the **Integration Quality Scale**: Bronze (mandatory baseline for all new integrations) / Silver (active code owners + error recovery) / Gold (discovery, translations, full test coverage — required for Works-with-HA devices) / Platinum (fully typed/async), plus special tiers No-score/Internal/Legacy/Custom [VERIFIED — HA-1 ✓✓]. Progress is machine-tracked per-rule in `quality_scale.yaml`; tiers are demotable (losing your code owner drops you to Bronze); when rules tighten, every integration in the tier is re-evaluated, with Works-with-HA integrations explicitly grandfathered [VERIFIED — HA-1 ✓✓]. The 2024 rework (ADR-0022) **dropped all existing scores** and forced re-application by checklist PR [VERIFIED — HA-2, HA-3]. The Custom tier is an honesty statement: HA "does not review, security audit, maintain, or support third-party custom integrations" [VERIFIED — HA-1 ✓✓]. HACS — itself a custom integration — distributes from GitHub repos and refuses to adopt files it didn't download ("Trust. If HACS did not initially download the element, there's no way to know which version you have") [VERIFIED — HA-10, HA-12].

**Versioning.** CalVer monthly releases, ~1-week beta, automatic pre-update backup [VERIFIED — HA-13]. Deprecations of YAML config get ≥6 months (six release cycles) with mandatory Repairs-dashboard issues (ADR-0021) [VERIFIED — HA-14]. Custom integrations get no such contract; the breaking-changes release-notes culture is the compensating control, and community update-fatigue is real (June 2025 "(breaking) update tired" thread; quarterly-cadence and LTS proposals) [VERIFIED — HA-22, community color].

**Community dynamics / why HACS lives outside core.** From ludeeus on the official HA blog: HACS should "remain an optional addition… Giving users the choice to add new features to Home Assistant at the cost of stability"; HACS content exists because authors "didn't have the time to meet Home Assistant's requirements" or do "something not allowed by Home Assistant, like web scraping" [VERIFIED — HA-21]. The 2024–26 trajectory is partnership (HACS became an Open Home Foundation collaboration; 2026.6 surfaces community cards in the core picker under a labeled "Community" section), not absorption [VERIFIED — HA-21, HA-20].

**Sharpest failure.** January 2021: directory traversal in HACS and other custom integrations let attackers read "any file that is accessible by the Home Assistant process," including credentials; core shipped path-traversal shields around third-party code, and Nabu Casa blocked insecure instances from Cloud [VERIFIED — HA-4]. The custom-integration `version` manifest key was retrofitted "in light of these incidents" so HA could identify and "block insecure versions" (required from 2021.6) [VERIFIED — HA-5]. One in-process extension bug = platform-wide compromise, and the minimum forensic primitive (a version field) had to be added under incident pressure.

**Most brilliant idea.** The quality ladder as legible, commerce-coupled state: per-rule YAML tracking, demotion rules, and a certification program (Works-with-HA) bound to the Gold tier — credible enough that the project zeroed everyone's score at relaunch [VERIFIED — HA-1 ✓✓, HA-2, HA-3].

**Licensing/commercial coexistence.** Apache-2.0 core [VERIFIED — HA-16]; Nabu Casa Cloud is optional and funds development; "Home Assistant works fully without it" [VERIFIED — HA-17]; no community content is vendor-paywalled — HACS "doesn't sell anything" [VERIFIED — HA-21].

**Namespace.** `domain` is "unique and cannot be changed"; core manifests omit `version`, custom must carry it; on brand-asset collision "the core integration domain gets preference" [VERIFIED — HA-6, HA-18].

| id | Claim | Source | Accessed | Status |
|---|---|---|---|---|
| HA-1 | Tier definitions; Bronze required for new; Gold required for WWHA; quality_scale.yaml; demotion; grandfathering; Custom-tier disclaimer | developers.home-assistant.io/docs/core/integration-quality-scale/ | 2026-07-02 | VERIFIED ✓✓ |
| HA-2 | ADR-0022 (2024-11-20) quality-scale rework | github.com/home-assistant/architecture/blob/master/adr/0022-integration-quality-scale.md | 2026-07-02 | VERIFIED |
| HA-3 | Scale introduced 2020; relaunch dropped all existing scores | developers.home-assistant.io/blog/2024/11/20/integration-quality-scale/ | 2026-07-02 | VERIFIED |
| HA-4 | 2021 disclosure: traversal via HACS et al.; "any file… accessible by the Home Assistant process"; Cloud blocking | home-assistant.io/blog/2021/01/22/security-disclosure/ | 2026-07-02 | VERIFIED |
| HA-5 | `version` key added "in light of these incidents"; block insecure versions; required 2021.6 | developers.home-assistant.io/blog/2021/01/29/custom-integration-changes/ | 2026-07-02 | VERIFIED |
| HA-6 | Domain unique/immutable; version required for custom only | developers.home-assistant.io/docs/creating_integration_manifest/ | 2026-07-02 | VERIFIED |
| HA-7 | Loader checks custom_components first; sanctioned override, discouraged | developers.home-assistant.io/docs/creating_integration_file_structure/ | 2026-07-02 | VERIFIED |
| HA-8 | Apps (add-ons) are container images from registries | developers.home-assistant.io/docs/apps | 2026-07-02 | VERIFIED |
| HA-9 | 1–6 security rating; protection mode default; AppArmor; API roles; Cosign | developers.home-assistant.io/docs/apps/security | 2026-07-02 | VERIFIED |
| HA-10 | HACS is a custom integration; not reviewed/tested by HA | hacs.xyz | 2026-07-02 | VERIFIED |
| HA-12 | "Trust. If HACS did not initially download the element…" | hacs.xyz/docs/faq/existing_elements/ | 2026-07-02 | VERIFIED |
| HA-13 | Monthly first-Wednesday CalVer; beta week; auto backup | home-assistant.io/faq/release/ | 2026-07-02 | VERIFIED |
| HA-14 | ADR-0021: YAML deprecation ≥6 months = 6 release cycles + Repairs issues | github.com/home-assistant/architecture/blob/master/adr/0021-…deprecation-policy.md | 2026-07-02 | VERIFIED |
| HA-15 | Blueprints = parameterized config, forum-shared | home-assistant.io/docs/blueprint/ | 2026-07-02 | VERIFIED |
| HA-16 | Core Apache-2.0 | home-assistant.io/developers/license/ | 2026-07-02 | VERIFIED |
| HA-17 | Cloud optional; "works fully without it" | home-assistant.io/cloud/ | 2026-07-02 | VERIFIED |
| HA-18 | Brands: core domain preference on collision; custom brand rules | github.com/home-assistant/brands README | 2026-07-02 | VERIFIED |
| HA-20 | 2026.6 custom-card suggestions under "Community" section | developers.home-assistant.io/blog/2026/05/27/custom-card-suggestions | 2026-07-02 | VERIFIED |
| HA-21 | HACS 2.0 blog: "optional addition… at the cost of stability"; "run their code directly in Home Assistant"; free; OHF partner | home-assistant.io/blog/2024/08/21/hacs-the-best-way-to-share-community-made-projects/ | 2026-07-02 | VERIFIED |
| HA-22 | Update-fatigue thread (2025-06-27); quarterly/LTS debate | community.home-assistant.io/t/…/905763 | 2026-07-02 | VERIFIED (community color) |
| — | ~3,000 core / "1,500+" HACS integration counts | secondary blogs only | 2026-07-02 | UNVERIFIED (official index fetch truncated >1,100 entries — INFERRED floor only) |

### 1.2 Zigbee2MQTT / zigbee-herdsman-converters — the data-driven staging-area model (our D5 anchor)

**Extension model.** Device support lives in a TypeScript corpus of per-vendor definition files coupling identity (`zigbeeModel`/`fingerprint`, model, vendor) to behavior. Since late 2023 the preferred form is declarative composition — `extend: [m.temperature(), m.battery()]` (**modernExtend** factory fragments merged at load) [VERIFIED — Z2M-1 ✓✓, Z2M-4]; legacy extend was removed at zhc 19.0.0 and now hard-fails [VERIFIED — Z2M-3, Z2M-7]. The escape hatch remains imperative JS (custom fromZigbee/toZigbee, `configure`, `onEvent`) — routinely needed for non-conformant Tuya devices [VERIFIED — Z2M-2]. The frontend can **auto-generate a definition** from ZCL discovery ("Generate external definition") [VERIFIED — Z2M-2]. An unsupported device is served by dropping a `.mjs` external converter beside the config (or pushing it live over MQTT); externals "work identically to internal converters" [VERIFIED — Z2M-1 ✓✓].

**Contribution pipeline.** External converters are explicitly a **staging area**: "Once your converter is ready, open a pull request… Once the new Zigbee2MQTT version is released, you can just delete the external converter" [VERIFIED — Z2M-1 ✓✓]. PRs must pass CI (lint, build, Vitest) and link a device-picture PR; docs are generated [VERIFIED — Z2M-2/3/4]. Review is thin and personal: a sampled June-2026 device PR was merged by Koenkk with "No reviews" [VERIFIED — Z2M-9]; ~200 PRs merged in June 2026 alone with near-per-merge npm releases (v26.76.0 on 2026-06-30) [VERIFIED — Z2M-10]. Scale: **5,473 devices from 577 vendors** [VERIFIED — Z2M-5].

**Versioning.** zhc breaks openly and often (README enumerates breaking majors 15→25), so stale external converters rot against the moving API — by design, since only merged definitions are maintained [VERIFIED — Z2M-3; INFERRED — rot dynamic from Z2M-3+Z2M-7]. The **Z2M 2.0.0 transition** (released 2025-01-03) is a model breaking-change execution: breaking-changes discussion opened **three months ahead** (2024-10-03), automatic settings migration with a written migration log and auto-backup, "how to get prepared" preflight; community reaction 197 comments/646 replies, one concession shipped under pressure (`legacy_action_sensor` add-back) [VERIFIED — Z2M-12, Z2M-13].

**Community.** Solo-anchored: Koenkk maintains Z2M and herdsman "in my spare time," 142 current sponsors; Nerivec is the visible infrastructure collaborator; bus factor ≈1–2 [VERIFIED — Z2M-14; INFERRED — bus factor from Z2M-9/12/14].

**Sharpest failure.** The trust seam: for years the recommended path to unsupported-device support was loading arbitrary JS into the coordinator process of a security-relevant system — acknowledged in the docs as full-compromise risk ("malicious or buggy code can compromise the entire Zigbee2MQTT instance, and potentially the host system") — and it was default-on until 2.11.0 (~May 2026) made external JS **disabled by default for new installations** [VERIFIED — Z2M-6, Z2M-1 ✓✓, Z2M-11].

**Most brilliant idea.** The **generate→tweak→merge→delete loop**: auto-generate from discovery, refine declaratively, PR into the shared corpus, then *delete the local copy*. Extensions are treated as temporary forks of data, not permanent plugins — which is why 5,473 devices are maintainable by ~1.5 maintainers [VERIFIED — Z2M-1 ✓✓/2/5; INFERRED — the maintainability causality].

**Namespace.** Matching keys on the device's self-reported `modelID` via a build-generated index; collisions resolved by **fingerprint matching with explicit numeric priority** (fingerprints beat plain zigbeeModel; external definitions prepended so they override internal); `whiteLabel` remaps model/vendor per-fingerprint so one definition serves many rebrands; Tuya's generic modelIDs force per-manufacturerName fingerprint disambiguation [VERIFIED — Z2M-7; INFERRED — Tuya stress case from Z2M-7 mechanics].

| id | Claim | Source | Accessed | Status |
|---|---|---|---|---|
| Z2M-1 | External-converter mechanics; staging-area tip; MQTT save/remove; disabled-by-default since 2.11.0 | zigbee2mqtt.io/advanced/more/external_converters.html | 2026-07-02 | VERIFIED ✓✓ |
| Z2M-2 | Auto-generate definition; PR steps; picture requirement | zigbee2mqtt.io/advanced/support-new-devices/01_support_new_devices.html | 2026-07-02 | VERIFIED |
| Z2M-3 | Repo scale; pre-PR test commands; breaking majors incl. "19.0.0 Legacy extend was removed" | github.com/Koenkk/zigbee-herdsman-converters | 2026-07-02 | VERIFIED |
| Z2M-4 | 700+ vendor files; CI pipeline; modern-extend-preferred review policy | raw…/zigbee-herdsman-converters/master/AGENTS.md | 2026-07-02 | VERIFIED |
| Z2M-5 | "5473 devices … from 577 different vendors" | zigbee2mqtt.io/supported-devices/ | 2026-07-02 | VERIFIED |
| Z2M-6 | "execute arbitrary user-provided JavaScript … compromise the entire … instance, and potentially the host system" | zigbee2mqtt.io/guide/installation/14_securing.html | 2026-07-02 | VERIFIED |
| Z2M-7 | Fingerprint-priority matching; whiteLabel; external-defs precedence; legacy-extend hard-fail | raw…/zigbee-herdsman-converters/master/src/index.ts | 2026-07-02 | VERIFIED |
| Z2M-9 | Sampled device PR merged by Koenkk, "No reviews" | github.com/Koenkk/zigbee-herdsman-converters/pull/12587 | 2026-07-02 | VERIFIED |
| Z2M-10 | 200 merged PRs Jun 2026; release-please v26.76.0 (2026-06-30) | api.github.com search: merged:2026-06-01..2026-06-30 | 2026-07-02 | VERIFIED |
| Z2M-11 | 2.11.0 note: externals disabled by default for new installs | github.com/Koenkk/zigbee2mqtt/releases | 2026-07-02 | VERIFIED |
| Z2M-12 | 2.0.0 released 2025-01-03; breaking/fixes; migration log; Nerivec credits | github.com/Koenkk/zigbee2mqtt/releases/tag/2.0.0 | 2026-07-02 | VERIFIED |
| Z2M-13 | Discussion #24198 opened 2024-10-03; breaking list; reaction volume; add-back concession | github.com/Koenkk/zigbee2mqtt/discussions/24198 | 2026-07-02 | VERIFIED |
| Z2M-14 | Koenkk spare-time maintainer; sponsor counts | github.com/sponsors/Koenkk | 2026-07-02 | VERIFIED |
| — | Historical device-count growth curve | Wayback blocked this session | — | UNVERIFIED (point-in-time metrics only) |

### 1.3 SmartThings — Groovy → Edge, the canonical ecosystem-breaking transition

**Model before/after.** Before: cloud-executed Groovy SmartApps + Device Type Handlers (DTHs), authored/pasted in a web IDE with live logging; community Groovy (webCoRE, community DTHs) was central platform value. After: **Edge drivers** — Lua packages (coarse permissions: `zigbee`/`zwave`/`lan`; device profiles; fingerprints) running sandboxed hub-local; arbitrary hosted SmartApps became self-hosted REST "endpoint apps"; ST engineer framing: Edge began as "DTH 2.0" built for "securely sandboxed, efficient, local execution" [VERIFIED — ST-2, ST-7, ST-10].

**The timeline (dates verified against staff posts).** 2020-06-24: transition announced in three vague phases — "Don't worry, you will have plenty of time"; first replies ask "what about webCoRE?" [VERIFIED — ST-1]. 2021-08-19: Edge beta; "the transition should be seamless" [VERIFIED — ST-2]. 2022-08-17: hard dates (IDE loses DTH/SmartApp tooling Oct 15; third-party DTHs auto-migrate Dec 12 **only if they fingerprint-match, else become a non-functional "Thing"**; Groovy execution ends Dec 31); custom Groovy capabilities' official guidance: "please contact the community member who provided that DTH to you" [VERIFIED — ST-3]. 2022-12-27: slip to "early 2023"; ST claims "Millions of devices have been migrated" [VERIFIED — ST-5]. 2023-05-19: Groovy device-joining off May 24; unmatched devices "will be migrated to a 'Thing' placeholder and will no longer function"; regressions admitted [VERIFIED — ST-6]. 2023-08-23: "we officially completed the migration!" — 38 months after announcement [VERIFIED — ST-7]. No official count of affected community DTHs/SmartApps was ever published [UNVERIFIED — none found; kept because its absence is itself a finding].

**Community dynamics.** The end-of-Groovy thread reached 2,053 replies / ~118k views [VERIFIED — ST-3]. webCoRE's Samsung arc (creator hired; a "Rebuilt webCoRE" presented at SDC 2019; what shipped was the Rules API) ended with the community converging on Hubitat (which runs webCoRE locally) and SharpTools as exits [VERIFIED as forum evidence — ST-8, ST-7]. The completion post was publicly called "tone deaf," and users noted it omitted thanks to the volunteer (Mariano Colmenarejo) who converted a "staggering number of devices" [VERIFIED — ST-7, forum replies].

**Distribution (what Edge got right).** **Driver channels**: developer-created, version-locked ("drivers contained within the driver channel are locked to a specific version"), shared by invitation URL, hub-enrollment based — real deployment infrastructure for hobbyists with no store approval [VERIFIED — ST-9]. Stock drivers are open source (Apache-2.0) with a PR path to the default catalog for OEM/WWST certification [VERIFIED — ST-12]. Hard caps surfaced as mystery breakage: the "50 Edge driver limit" popup, plus duplicate driver display names confusing users [VERIFIED — ST-11, forum-reported].

**Sharpest failure.** Promising seamlessness and continuity it couldn't deliver, then removing developer tooling before migration finished — "plenty of time" (2020) and "seamless" (2021) degraded into fingerprint-match-or-dead-Thing (2022–23), dropped custom capabilities, and IDE debugging deleted ~8 months before community-DTH migration even began [VERIFIED — ST-1/2/3/6].

**Most brilliant idea.** Channels + hub-local execution + Apache-2.0 stock drivers: version-pinned distribution without a store, lower latency, and a forkable driver corpus as the honorable complement [VERIFIED — ST-2/9/12].

**Licensing/commercial coexistence.** Proprietary cloud runtime meant zero community leverage: "When SmartThings removes Groovy from their platform then webCoRE goes with it" [VERIFIED — ST-8, forum]. Commercial Groovy authors lost their runtime [INFERRED — from obsolete-tagged thread titles].

**Namespace.** Platform-issued driver UUID + developer `packageKey`; channels are UUIDs; fingerprints namespaced by driver; device→driver binding is fingerprint matching with manufacturer-specific beating generic; users lost the DTH-era ability to manually bind any device to any handler [VERIFIED — ST-10, ST-9, ST-7 reply].

| id | Claim | Source | Accessed | Status |
|---|---|---|---|---|
| ST-1 | 2020-06-24 announcement; 3 phases; "plenty of time"; day-one webCoRE replies | community.smartthings.com/t/…/197958 | 2026-07-02 | VERIFIED (staff post) |
| ST-2 | 2021-08-19 Edge beta; "transition should be seamless" | community.smartthings.com/t/…/229555 | 2026-07-02 | VERIFIED (staff post) |
| ST-3 | 2022-08-17 milestones; fingerprint-or-Thing; custom-capability advice; 2,053 replies/118k views | community.smartthings.com/t/the-end-of-groovy-has-arrived/246280 | 2026-07-02 | VERIFIED (staff post) |
| ST-5 | 2022-12-27 slip; "Millions of devices have been migrated" (ST's own claim) | community.smartthings.com/t/…/254856 | 2026-07-02 | VERIFIED (staff post) |
| ST-6 | 2023-05: joining off; unmatched → "Thing … will no longer function"; regressions | community.smartthings.com/t/…/263759 | 2026-07-02 | VERIFIED (staff post) |
| ST-7 | 2023-08-23 completion; "DTH 2.0"; volunteer credit omission; exits | community.smartthings.com/t/…/268851 | 2026-07-02 | VERIFIED (staff post + replies) |
| ST-8 | webCoRE end; no re-hosting; Hubitat path | community.webcore.co/t/addressing-the-end-of-webcore/19433 | 2026-07-02 | VERIFIED (forum) |
| ST-9 | Channels: version-locked, invitation URLs | developer.smartthings.com/docs/devices/hub-connected/driver-channels | 2026-07-02 | VERIFIED |
| ST-10 | packageKey; permissions; fingerprint precedence | developer.smartthings.com/docs/devices/hub-connected/driver-components-and-structure | 2026-07-02 | VERIFIED |
| ST-11 | 50-driver-limit popup; duplicate-name confusion | community.smartthings.com/t/50-edge-driver-limit/246835 | 2026-07-02 | VERIFIED (user-reported) |
| ST-12 | Stock drivers Apache-2.0; OEM PR/WWST path | github.com/SmartThingsCommunity/SmartThingsEdgeDrivers | 2026-07-02 | VERIFIED |
| — | Count of affected community DTHs/SmartApps; official per-hub memory figures | — | — | UNVERIFIED (never published) |

### 1.4 Homebridge — npm plugins, the verified program, child-bridge isolation

**Extension model.** Node.js plugins loaded into the Homebridge process by filesystem convention: the plugin manager scans global `node_modules`, accepts only names matching `homebridge-*` (or `@scope/homebridge-*`), requires the `homebridge-plugin` npm keyword, and catches load errors per-plugin [VERIFIED — HB-2]. Hard HAP constraint: ~150 accessories per bridge [VERIFIED — HB-1]. **Child bridges** (v1.3.0, 2021-02-20): any plugin can run "as its own independent bridge… in an isolated process" — a spawned child process with its own HAP bridge/port, auto-restarted on crash, protecting the main bridge from fatal exceptions, dependency pollution, and slow plugins (HomeKit polls every accessory on a bridge, so one slow plugin drags all responses); it also works around the accessory cap and allows multi-instance platforms. "This will work with all existing plugins without requiring any code changes." Costs: 20–30 MB RAM per child process + separate HomeKit pairing per child bridge [VERIFIED — HB-7 ✓✓, HB-8].

**Distribution & trust.** npm is the sole channel; 5,542 packages carry the keyword, of which **602 are Verified** (~11%) [VERIFIED — HB-6, HB-5]. Verification is a point-in-time checklist (dynamic platform type, Node LTS, clean install, no post-install system modification, no user tracking/analytics, must catch own exceptions, must ship the settings schema, must not duplicate an existing verified plugin) — with the explicit honesty that "existing verified plugins will have met the requirements at the time of verification, and not necessarily the current requirements"; un-verification is reactive [VERIFIED — HB-4]. Verified plugins get UI badge/placement and pre-built dependency bundles because npm itself is "resource hungry and prone to failure" on Pi-class hardware [VERIFIED — HB-4].

**Versioning.** ~6-year major cadence: v1.0 (2020), v2.0 (2026-05-04) after warning notices from v1.8.4 (2024-07) and parallel maintenance of the 1.x line into 2026 [VERIFIED — HB-9]. Plugins signal compatibility via `engines` (`"homebridge": "^1.6.0 || ^2.0.0"`), driving a green-tick readiness check in the UI; child bridges double as migration containment (an un-updated plugin crash-loops alone) [VERIFIED — HB-10].

**Community.** Volunteer-run, "no company behind it, nothing is sold"; leadership rotated across the majors; HOOBS is the commercial derivative (hardware + own plugin library) that historically lagged core versions [VERIFIED — HB-1, HB-14; version-lag from issue titles only].

**Sharpest failure.** Plugin rot: npm-only distribution + first-come naming produced abandoned plugins and "multiple forks of the same plugin… confusion for users" (the team's own words) — forcing a retroactive governance apparatus five-plus years in: a plugins org that takes ownership transfer of repo *and* npm package, recruits maintainers, republishes under a reserved `@homebridge-plugins/` scope, with a UI migration tool [VERIFIED — HB-11, HB-12].

**Most brilliant idea.** Child bridges — per-plugin subprocess isolation retrofitted as *pure configuration*, compatible with every existing plugin [VERIFIED — HB-7 ✓✓]. Runner-up: `config.schema.json` — a mandatory-for-verification declarative config contract from which the UI auto-generates settings forms [VERIFIED — HB-4, HB-16].

**Licensing.** Core Apache-2.0; explicitly non-commercial; no paid-plugin mechanism; donation links only [VERIFIED — HB-3, HB-1, HB-4].

**Namespace.** Identity = npm name with enforced prefix + keyword; no reservation beyond npm's; curation via the reserved org scope and registry-overlay lists (hidden/unmaintained plugins) [VERIFIED — HB-2, HB-11, HB-4].

| id | Claim | Source | Accessed | Status |
|---|---|---|---|---|
| HB-1 | HAP emulation; keyword search; 150-accessory limit; non-commercial | raw…/homebridge/latest/README.md | 2026-07-02 | VERIFIED |
| HB-2 | Name regex; keyword required; load-error containment | raw…/homebridge/latest/src/pluginManager.ts | 2026-07-02 | VERIFIED |
| HB-3 | Apache-2.0; engines node | raw…/homebridge/latest/package.json | 2026-07-02 | VERIFIED |
| HB-4 | Verified program requirements (upd. 2026-05-05); point-in-time honesty; revocation; bundles; overlay files | github.com/homebridge/verified → /homebridge/plugins | 2026-07-02 | VERIFIED |
| HB-5 | 602 verified plugins (file count) | raw…/plugins/latest/verified-plugins.json | 2026-07-02 | VERIFIED |
| HB-6 | 5,542 npm packages with keyword | registry.npmjs.org search total | 2026-07-02 | VERIFIED |
| HB-7 | Child-bridge mechanics: isolated process, auto-restart, 149 workaround, per-child pairing, 20–30 MB, no code changes | github.com/homebridge/homebridge/wiki/Child-Bridges | 2026-07-02 | VERIFIED ✓✓ |
| HB-8 | v1.3.0 (2021-02-20) introduced child bridges | github.com/homebridge/homebridge/releases/tag/v1.3.0 | 2026-07-02 | VERIFIED |
| HB-9 | v2.0.0 2026-05-04; v1.8.4 notices 2024-07; 1.x parallel line | raw…/homebridge/latest/CHANGELOG.md | 2026-07-02 | VERIFIED |
| HB-10 | engines readiness tick; child bridge as migration containment | github.com/homebridge/homebridge/wiki/Updating-To-Homebridge-v2.0 | 2026-07-02 | VERIFIED |
| HB-11 | Abandonment→fork confusion (team's words); @homebridge-plugins scope | github.com/homebridge/plugins/wiki/Scoped-Plugins | 2026-07-02 | VERIFIED |
| HB-12 | Ownership transfer of repo+npm; maintainer recruitment | github.com/homebridge/plugins/wiki/Unmaintained-Plugins | 2026-07-02 | VERIFIED |
| HB-14 | HOOBS commercial hubs + own plugin library | hoobs.com | 2026-07-02 | VERIFIED |
| HB-16 | Settings-GUI schema mechanism | homebridge-config-ui-x wiki → developers.homebridge.io/#/config-schema | 2026-07-02 | VERIFIED (intro date UNVERIFIED) |

### 1.5 openHAB — OSGi add-ons and the cautionary marketplace arc

**Extension model.** Add-ons are Java OSGi bundles on Apache Karaf — a *real* dynamic-module system in production. Costs surfaced repeatedly: raw-JAR drop-in installs "can lead to problems, because add-on dependencies may not be installed"; the 2017 marketplace installed JARs without dependency resolution and lost them on upgrade (they lived in the OSGi cache) [VERIFIED — OH-1, OH-3, OH-4].

**The marketplace arc (five eras).** (1) 1.x monolith: all add-ons shipped as one reviewed package [VERIFIED — OH-12]. (2) **Eclipse IoT Marketplace** (2017–2019), launched explicitly because "the queue for binding PRs is still too long" [VERIFIED — OH-3]. (3) Abandonment when openHAB left Eclipse: "as a non-Eclipse project, we must not rely on it any longer" [VERIFIED — OH-8]. (4) A two-year gap with no marketplace (3.0 shipped without one) [INFERRED — OH-13 + OH-9]. (5) **Community marketplace** (announced 2021-10, shipped 3.2): Discourse forum topics ARE the registry — "by merely opening a new topic… everyone can effectively publish an add-on… installable with a simple click"; self-moderated via forum trust levels; add-ons cached locally and reinstalled across upgrades (fixing the Eclipse-era loss); marketplace code carries an explicit didn't-go-through-the-same-review warning [VERIFIED — OH-9, OH-11].

**Versioning.** Add-ons are versioned with the distro; majors are breaking: 2.0 (2017) kept 1.x add-ons alive via a compatibility layer; 3.0 (2020-12) removed it (Java 8→11); 4.0 (2023-07-23) added "Thing upgrades" to auto-migrate breaking binding changes [VERIFIED — OH-12, OH-13, OH-14]. Marketplace add-ons "might not be compatible with your openHAB runtime version" [VERIFIED — OH-9].

**Community/governance.** The Eclipse SmartHome era (2014–2019) ended because the split created "'unnatural' boundaries" and "unproductive overhead," and "the majority of contributions meanwhile originates from the openHAB community" — the project archived, forcing a mass package rename [VERIFIED — OH-5, OH-6, OH-7]. Capacity: 37 maintainers (2023) vs 400+ technologies [VERIFIED — OH-14, OH-15].

**Sharpest failure.** Betting distribution on another organization's infrastructure: the Eclipse Marketplace died of the governance split, not technical failure, leaving the two-year hole [VERIFIED — OH-8, OH-5; INFERRED — the gap].

**Most brilliant idea.** Forum-as-registry: reusing Discourse bought identity, reputation-based curation rights, social proof, support-thread-per-add-on, and moderation for free — "we are putting a lot of faith in the community to moderate itself" [VERIFIED — OH-9]. Runner-up: Thing upgrades (self-migrating binding breaking-changes) [VERIFIED — OH-14].

**Licensing.** EPL-2.0 core; marketplace rules mandate FOSS-only — OSI license, "no license keys, trials, or freemium"; donations allowed; the 2017 era had envisioned closed-source content and the 2021 rules reversed that [VERIFIED — OH-10, OH-3; INFERRED — reversal]. myopenHAB cloud is free, foundation-run [VERIFIED — OH-15, OH-16].

**Namespace.** Everything keys off the binding ID (`org.openhab.binding.<id>`, `hue:bridge:<id>`); collision policy is social: "Publishing add-ons that compete directly with an official add-on is not allowed" [VERIFIED — OH-2, OH-19, OH-10].

| id | Claim | Source | Accessed | Status |
|---|---|---|---|---|
| OH-1 | Install paths; JAR dependency warning; add-ons versioned with distro | openhab.org/docs/configuration/addons.html | 2026-07-02 | VERIFIED |
| OH-2 | OSGi bundle layout; naming conventions; review checklist | openhab.org/docs/developer/guidelines.html | 2026-07-02 | VERIFIED |
| OH-3 | 2017 marketplace launch rationale (PR queue); no dep resolution; closed-source envisioned | community.openhab.org/t/…/24491 | 2026-07-02 | VERIFIED |
| OH-4 | Maturity levels 0–3; add-ons lost on upgrade | v2.openhab.org/docs/configuration/eclipseiotmarket.html | 2026-07-02 | VERIFIED |
| OH-5 | ESH exit rationale; namespace refactor; OH3 replacement promise | community.openhab.org/t/the-road-ahead-reintegrating-esh/64670 | 2026-07-02 | VERIFIED |
| OH-6/7 | Eclipse SmartHome archived; "no one was left to maintain ESH" | projects.eclipse.org/projects/iot.smarthome; community.openhab.org/t/…/98978 | 2026-07-02 | VERIFIED |
| OH-8 | "as a non-Eclipse project, we must not rely on it any longer" | github.com/openhab/openhab-addons/issues/6673 | 2026-07-02 | VERIFIED |
| OH-9 | Forum-as-registry announcement; trust levels; caching; review-gap warning | community.openhab.org/t/announcing-the-community-marketplace/127188 | 2026-07-02 | VERIFIED |
| OH-10 | Marketplace rules: FOSS-only, no keys/trials; no competing add-ons | community.openhab.org/t/about-the-add-on-marketplace-category/123408 | 2026-07-02 | VERIFIED |
| OH-11 | 3.2 ships marketplace | openhab.org/blog/2021-12-19-openhab-3-2-release.html | 2026-07-02 | VERIFIED |
| OH-12 | 2.0: 130 bindings/57 new-API; 1.x compat layer | openhab.org/blog/2017-01-22-openhab2.html | 2026-07-02 | VERIFIED |
| OH-13 | 3.0: compat layer removed; Java 8→11 | openhab.org/blog/2020-12-21-openhab-3-0-release.html | 2026-07-02 | VERIFIED |
| OH-14 | 4.0 (2023-07-23): Thing upgrades; 37 maintainers | openhab.org/blog/2023-07-23-openhab-4-0-release.html | 2026-07-02 | VERIFIED |
| OH-15/16 | 400+ technologies; foundation e.V.; free myopenHAB | openhab.org; openhabfoundation.org | 2026-07-02 | VERIFIED |
| OH-19 | thingUID structure | openhab.org/docs/developer/bindings/ | 2026-07-02 | VERIFIED |

### 1.6 Hubitat · ESPHome · Node-RED (lighter passes) + Matter bridging note

**Hubitat.** User apps/drivers in Groovy ON the hub — the model SmartThings abandoned — inside a documented sandbox (no custom classes/JARs, no threads, whitelisted imports) [VERIFIED — HUB-1, HUB-2]. No first-party marketplace: **Hubitat Package Manager is community-built** ("created by Dominic Meglio"), with JSON manifests (SemVer, `minimumHEVersion`, raw-GitHub file URLs) PR'd into a central repositories list — the platform outsourced its entire distribution/update layer to one volunteer, and trust bottoms out in unsigned raw-GitHub URLs [VERIFIED — HUB-3, HUB-4; INFERRED — trust characterization]. Brilliant: HPM's "Match Up" fingerprints already-installed code and adopts it into managed updates [VERIFIED — HUB-3]. Namespace: name+namespace unique per hub only [VERIFIED — HUB-5].

**ESPHome.** Config-as-data: YAML validates, code-generates, and compiles to C++ firmware — no runtime plugins at all. `external_components` pulls component source from git at build time (ref pinning by branch/tag, `github://pr#N` addressing, refresh interval) — you compile what you pull [VERIFIED — ESP-6]. "Custom components" (runtime hacks lacking config validation/codegen) were deprecated then **removed** in 2025.2.0; the maintainers frame external components as full components whose "only difference is that they are external" — the on-ramp to core submission [VERIFIED — ESP-7, ESP-8]. Brilliant: the review queue itself is addressable (`github://pr#N` — run an unmerged component before it graduates) [VERIFIED — ESP-6]. Failure: the hard cutover broke unported configs by design [INFERRED — ESP-7].

**Node-RED.** npm-distributed nodes + the Flow Library registry over npm (6,065 nodes) [VERIFIED — NR-11, NR-14]. The **scorecard** (2022-01-31) auto-checks naming/license/clashes and explicitly does not examine code — "chose not to act as gatekeepers… beyond some very basic checks" [VERIFIED — NR-15]. Rot at scale: 4.1 (2025-07-29) added "deprecated" badges and default download-count sorting — UI features that exist to route users around dead modules [VERIFIED — NR-13; INFERRED — the tell]. Apache-2.0, OpenJS governance, commercial push via FlowFuse [VERIFIED — NR-12, NR-16].

**Matter bridging (narrow, per brief).** Matter's own extension mechanism is the **bridge** device type ("a Matter bridge portrays non-Matter devices as virtual Matter devices") [VERIFIED — M-17]; platforms weaponize it as plugin strategy (Matterbridge is "a Matter plugin manager" whose npm plugins expose fleets into any fabric) [VERIFIED — M-18]. Cautionary: the leading HA-to-Matter bridge (1.5k stars) was archived March 2026 after an end-of-maintenance notice ("may the best fork prevail") — bridge-as-plugin inherits single-maintainer risk [VERIFIED — M-19].

| id | Claim | Source | Accessed | Status |
|---|---|---|---|---|
| HUB-1/2 | Groovy sandbox; import whitelist | docs2.hubitat.com/en/developer/overview; …/allowed-imports | 2026-07-02 | VERIFIED |
| HUB-3/4 | HPM community-built; manifest/repositories mechanics; Match Up | hubitatpackagemanager.hubitatcommunity.com (+/devs1.html) | 2026-07-02 | VERIFIED |
| HUB-5 | Bundles; per-hub name+namespace uniqueness | docs2.hubitat.com/en/user-interface/developer/bundles | 2026-07-02 | VERIFIED |
| ESP-6 | external_components: git/ref pinning; pr# addressing; build-time pull | esphome.io/components/external_components/ | 2026-07-02 | VERIFIED |
| ESP-7/8 | Custom components removed 2025.2.0; external = on-ramp framing | esphome.io/changelog/2025.2.0/; developers.esphome.io blog 2025-02-19 | 2026-07-02 | VERIFIED |
| NR-11..16 | Packaging/keyword; scorecard non-gatekeeping; 4.1 deprecated badges; Flow Library counts; Apache-2.0; OpenJS/FlowFuse | nodered.org docs/blog/flows.nodered.org/LICENSE | 2026-07-02 | VERIFIED |
| M-17 | Bridge = virtual Matter devices | csa-iot.org/newsroom/why-bridging-matters/ | 2026-07-02 | VERIFIED |
| M-18 | Matterbridge "a Matter plugin manager" | raw…/Luligu/matterbridge/main/README.md | 2026-07-02 | VERIFIED |
| M-19 | HA-Matter-Hub archived 2026-03; fork recommendation | github.com/t0bst4r/home-assistant-matter-hub | 2026-07-02 | VERIFIED |

### 1.7 VS Code — the extension-host isolation case study and marketplace trust at scale

**Isolation architecture (the case study).** Extensions run in a dedicated extension-host process; the design goal is stability/perf containment — extensions cannot impact startup, block UI operations, or modify the UI (no DOM access; API via RPC) [VERIFIED — VSC-1, VSC-3]. What it does NOT buy: "The extension host has the same permissions as VS Code itself… an extension can read and write files on your machine, make network requests, run external processes" [VERIFIED — VSC-4 ✓✓]. The per-extension permission model remains an open feature request since 2018-06 (#52116, milestone Backlog, 398 reactions); the compensating control is Workspace Trust (1.57, 2021), whose docs concede it "can't prevent a malicious extension from executing code and ignoring Restricted Mode" [VERIFIED — VSC-7, VSC-6]. The key lazy-load idea: **declarative contribution points + activation events** — the UI renders an extension's entire contribution surface without executing extension code; since 1.74 declared contributions need no explicit activation events [VERIFIED — VSC-8; INFERRED — the containment payoff].

**Marketplace trust.** The protection stack, per Microsoft's own docs: malware scanning on every new extension *and every update*; dynamic detection in a clean-room VM; verified publishers (DNS domain proof + ≥6 months good standing); unusual-usage monitoring; name-squatting prevention; a **block list** that auto-uninstalls removed malicious extensions client-side; marketplace-side signing with client verification; secret scanning; and (1.97) a first-install publisher-trust dialog [VERIFIED — VSC-5 ✓✓]. Microsoft reports 136 extensions reviewed/110 removed this year [VERIFIED — VSC-12, Microsoft's own figures]. Scale: **131,229 extensions** by gallery-API count [VERIFIED — VSC-13].

**Versioning.** `engines.vscode` semver gates + the marketplace serving only compatible versions; a stable-API compatibility pledge; **proposed APIs** formally gated (Insiders-only, must be declared, cannot be published) — a two-tier API stability discipline; graceful deprecation with a Migrate path but no forced uninstall [VERIFIED — VSC-9, VSC-10].

**Sharpest failure.** No privilege sandbox + identity loopholes at the margins: removed extension names could be re-registered by any publisher (ReversingLabs, 2025 `shiba` campaign), and the Material Theme takedown (~9M installs, Feb 2025) was partially reversed — "we moved fast and we messed up" — showing detection is noisy [VERIFIED — VSC-14, VSC-16, vendor/press]. On Open VSX, the GlassWorm waves (Oct 2025→) demonstrated what happens when a registry's scanning fails [VERIFIED — VSC-15, vendor research].

**Most brilliant idea.** The declarative-contribution/lazy-activation split (above) [INFERRED — from VSC-1/3/8].

**Licensing.** MIT core, but the Marketplace ToU restricts consumption to official builds (the VSCodium exclusion; some Microsoft extensions hard-locked) — **the registry, not the license, is the control lever**; no paid-extension mechanism, monetization via services [VERIFIED — VSC-17, VSC-18; INFERRED — no-paid-path].

**Namespace.** Two-level immutable `publisher.name` identity; DNS-verified publishers; display-name changes revoke the badge [VERIFIED — VSC-10, VSC-14].

| id | Claim | Source | Accessed | Status |
|---|---|---|---|---|
| VSC-1/3 | Extension-host containment goals; no DOM access | code.visualstudio.com/api/advanced-topics/extension-host; …/extension-capabilities/overview | 2026-07-02 | VERIFIED |
| VSC-4 | "same permissions as VS Code itself" | code.visualstudio.com/docs/configure/extensions/extension-runtime-security | 2026-07-02 | VERIFIED ✓✓ |
| VSC-5 | Full marketplace-protection stack; block-list auto-uninstall; signing; secret scan; 1.97 publisher-trust | same page | 2026-07-02 | VERIFIED ✓✓ |
| VSC-6 | Workspace Trust limits ("can't prevent a malicious extension…") | code.visualstudio.com/docs/editing/workspaces/workspace-trust | 2026-07-02 | VERIFIED |
| VSC-7 | #52116 open since 2018; Backlog | api.github.com/repos/microsoft/vscode/issues/52116 | 2026-07-02 | VERIFIED |
| VSC-8 | Activation events; 1.74 declarative contributions | code.visualstudio.com/api/references/activation-events | 2026-07-02 | VERIFIED |
| VSC-9 | Proposed-API gating; API-compat pledge | code.visualstudio.com/api/advanced-topics/using-proposed-api | 2026-07-02 | VERIFIED |
| VSC-10 | engines gate; verified-publisher criteria; deprecation flow | code.visualstudio.com/api/working-with-extensions/publishing-extension | 2026-07-02 | VERIFIED |
| VSC-12 | 136 reviewed / 110 removed | devblogs.microsoft.com/blog/security-and-trust-in-visual-studio-marketplace | 2026-07-02 | VERIFIED (Microsoft) |
| VSC-13 | 131,229 extensions (gallery API TotalCount) | marketplace.visualstudio.com/_apis/public/gallery/extensionquery | 2026-07-02 | VERIFIED |
| VSC-14 | Removed-name re-registration loophole; shiba campaign | reversinglabs.com/blog/malware-vs-code-extension-names | 2026-07-02 | VERIFIED (vendor) |
| VSC-15 | GlassWorm Open VSX waves | koi.ai/blog/glassworm-returns-… | 2026-07-02 | VERIFIED (vendor) |
| VSC-16 | Material Theme removal + reversal | bleepingcomputer.com (press) | 2026-07-02 | VERIFIED (press) |
| VSC-17/18 | MIT core; Marketplace ToU official-builds-only; VSCodium→Open VSX | raw LICENSE.txt; github.com/VSCodium/vscodium docs/extensions.md | 2026-07-02 | VERIFIED |

### 1.8 Chrome MV2 → MV3 — permission manifests and the second breaking-migration case study

**Permission manifest.** Five declared surfaces (`permissions`, `optional_permissions`, content-script matches, `host_permissions`, `optional_host_permissions` — host access split out in MV3, user-withholdable); install-time warnings keyed to permission classes; Google's own docs push "a less powerful API to avoid alarming warnings" — official acknowledgment of warning fatigue [VERIFIED — CR-5]. Permissions buy review triage: broad host patterns and sensitive permissions get longer review [VERIFIED — CR-3]. MV3's reviewability win is the **remote-hosted-code ban**: "all of your extension's logic must be part of the extension package" — remote code was "unreviewed code" [VERIFIED — CR-6, CR-8].

**Review pipeline.** Manual + automated for every submission and every update; days-to-weeks latency; enforcement ladder ending in a malware verdict that remotely disables the extension on all user devices; policy pillars: single purpose, no obfuscation (70% of blocked malicious extensions were obfuscated), 2FA on developer accounts [VERIFIED — CR-3, CR-10, CR-18]. Scale: ~1,800 malicious uploads blocked monthly (2019 figures) [VERIFIED — CR-15, Google's own].

**The migration timeline (all dates lane-re-verified against the official timeline page ✓✓).** 2018-10: MV3 vision. 2021-09: sunset announced — no new MV2 items after 2022-01, Chrome "will no longer run Manifest V2" January 2023. 2022-09: slip to Chrome 112/115 experiments. 2022-12: full pause "to address developer feedback." 2023-11: resumption for June 2024 — after concessions (offscreen documents, longer service-worker lifetimes, a User Scripts API, "more generous limits" in declarativeNetRequest). 2024-06-03: phase-out begins pre-stable ("over 85% of actively maintained extensions" on MV3). 2024-10-09: disabling begins in stable with temporary re-enable. 2025-03-31: disabled by default everywhere. 2025-07-24: Chrome 138 — disabled with no re-enable; the enterprise policy removed in Chrome 139 [VERIFIED — CR-1 ✓✓, CR-2, CR-4, CR-7, CR-9]. Net arc: ~2.5 years of slip, ~7 years announcement-to-extinction [INFERRED — arithmetic on CR-1/7/10].

**The DNR fight.** Google: blocking webRequest carried "performance and privacy cost"; DNR blocks without granting extensions access to sensitive request data [VERIFIED — CR-8, CR-15]. EFF: "a raw deal for users… outright harmful to privacy efforts" [VERIFIED — CR-11, stakeholder position]. Mozilla: ships DNR for compatibility but "will maintain support for blocking WebRequest in MV3" [VERIFIED — CR-12]. uBlock Origin exited rather than migrate; uBO Lite is an explicitly reduced declarative port, whose maintainer candidly concedes MV3 upsides (reliable filtering at browser launch; zero remote requests) [VERIFIED — CR-13, maintainer position].

**Sharpest failure.** Announcing a hard kill date before the replacement API could express the platform's flagship extensions — the concessions that unblocked resumption are exactly what should have shipped before the sunset was scheduled [VERIFIED — CR-2; INFERRED — the counterfactual].

**Most brilliant idea.** Declarative-over-imperative as a review transform: declared artifacts are diffable and machine-checkable, converting review from adversarial code audit into data validation — safe DNR rule updates now skip human review and publish "in minutes" [VERIFIED — CR-9].

**Namespace.** Extension ID is permanent and key-pair-derived; trust accrues to the immortal ID; updates get the same review as new items [VERIFIED — CR-14, CR-3].

| id | Claim | Source | Accessed | Status |
|---|---|---|---|---|
| CR-1 | Full rollout dates 2024-06→2025-07 (Chrome 138/139) | developer.chrome.com/docs/extensions/develop/migrate/mv2-deprecation-timeline | 2026-07-02 | VERIFIED ✓✓ |
| CR-2 | Dec-2022 pause; Nov-2023 resumption + concessions | developer.chrome.com/blog/resuming-the-transition-to-mv3 | 2026-07-02 | VERIFIED |
| CR-3 | Review manual+automated; permission-keyed depth; enforcement ladder | developer.chrome.com/docs/webstore/review-process | 2026-07-02 | VERIFIED |
| CR-4 | Sept-2022 revision (112/115 experiments) | developer.chrome.com/blog/more-mv2-transition | 2026-07-02 | VERIFIED |
| CR-5 | Five permission surfaces; warning-fatigue guidance | developer.chrome.com/docs/extensions/develop/concepts/declare-permissions | 2026-07-02 | VERIFIED |
| CR-6 | Remote-hosted-code ban | developer.chrome.com/docs/extensions/develop/migrate/improve-security | 2026-07-02 | VERIFIED |
| CR-7 | Original sunset: Jan 2023 kill date | developer.chrome.com/blog/mv2-transition | 2026-07-02 | VERIFIED |
| CR-8 | Remote code = unreviewed code; webRequest rationale | developer.chrome.com/docs/extensions/develop/migrate/what-is-mv3 | 2026-07-02 | VERIFIED |
| CR-9 | 85% actively-maintained stat; DNR limits; review-skip "in minutes" | blog.chromium.org/2024/05/manifest-v2-phase-out-begins.html | 2026-07-02 | VERIFIED |
| CR-10 | 2018 vision; host-access controls; obfuscation ban + 70% stat | blog.chromium.org/2018/10/trustworthy-chrome-extensions-by-default.html | 2026-07-02 | VERIFIED |
| CR-11/12/13 | EFF / Mozilla / uBO positions | eff.org deeplinks 2021-12; blog.mozilla.org/addons 2022-05; uBOL FAQ | 2026-07-02 | VERIFIED (stakeholder) |
| CR-14 | Key-derived permanent IDs | developer.chrome.com/docs/extensions/reference/manifest/key | 2026-07-02 | VERIFIED |
| CR-15 | 2019 security blog: DNR rationale; 1,800/mo | security.googleblog.com/2019/06/… | 2026-07-02 | VERIFIED |
| CR-18 | Single-purpose policy | developer.chrome.com/docs/webstore/program-policies/quality-guidelines | 2026-07-02 | VERIFIED |

### 1.9 Obsidian (wildcard) — minimum-viable trust at small-team, local-first scale

**Why this wildcard.** The closest structural analog to HomeSynapse's position: a tiny team (8 people; plugin review was a named individual's side duty), a local-first product, user-supported revenue (no investors), free core + paid vendor services (Sync/Publish) coexisting with a community plugin ecosystem — and no sandbox [VERIFIED — OB-17, OB-18, OB-19].

**Extension model & honesty.** Plugins load in the Electron renderer with full host access. The vendor states it plainly: "Obsidian cannot reliably restrict plugins to specific permissions or access levels… plugins will inherit Obsidian's access levels" — they "can access files on your computer… connect to internet… install additional programs" [VERIFIED — OB-1 ✓✓]. **Restricted Mode is on by default**: community plugins are off until the user opts in [VERIFIED — OB-2 ✓✓].

**Distribution & trust.** Publishing = PR adding an entry to a public registry JSON; the app pulls manifests from developer repos and **fetches actual files from developers' GitHub releases** — GitHub as the CDN, supply chain resting on each developer's account [VERIFIED — OB-7, OB-8]. Developer policies ban obfuscation, client-side telemetry, and **self-update mechanisms** (updates must flow through the reviewable pipeline); network use, out-of-vault access, and payment gates are allowed only with README disclosure [VERIFIED — OB-4, OB-5]. The manual gate then failed at scale: "we struggled to keep pace with submissions, and subsequent versions were not reviewed" — a 2,300-submission backlog cleared in days by the 2026 relaunch's **automated per-version scanning** ("scans every version… not just the initial submission") with a public per-plugin safety scorecard; manual review persists only for popular/featured/flagged plugins [VERIFIED — OB-13, OB-3 ✓✓]. Real incident: REF6598 (Apr 2026) weaponized two legitimate plugins inside an attacker-synced vault — but required the victim to manually enable them; the directory itself was not compromised [VERIFIED — OB-22, vendor research]. **BRAT** — the community beta-installer that bypasses the directory — is officially recommended for beta testing; the relaunch notes users may no longer need it "because the review time has been cut down dramatically" [VERIFIED — OB-20, OB-21, OB-13].

**Versioning.** Manifest requires `id`, semver `version`, `minAppVersion`; when a plugin's manifest demands a newer app, `versions.json` maps back to the latest compatible plugin release — a forward-compat gate with graceful degradation [VERIFIED — OB-9, OB-8]. Their breaking-change case (CM5→CM6 Live Preview editor) shipped with a Legacy Editor fallback [VERIFIED-via-excerpt — OB-24].

**Community & economics.** 5,317 entries in the live registry JSON (lane note: the vendor blog's "4,000+ plugins and themes" is older/rounded) [VERIFIED — OB-16, OB-13]. Community plugins **may be paid** — but "Obsidian Community is not a store, and does not offer any built-in payment solutions"; plugins are labeled Free/Optional-payments/Paid; new closed-source plugins are no longer accepted [VERIFIED — OB-14].

**Sharpest failure.** A single-reviewer manual gate could not scale, and post-initial versions went entirely unreviewed for years — a plugin could pass review once, then ship arbitrary updated code via its own GitHub releases with no re-check, atop zero runtime sandbox [INFERRED — from OB-13 + OB-8].

**Most brilliant idea.** Restricted Mode as honest minimum-viable trust: rather than promising an undeliverable sandbox, ship third-party code off by default, state the access plainly, make the user the explicit trust authority — paired with GitHub-releases-as-CDN (zero hosting cost) and the no-self-update policy (all updates flow through the reviewable pipeline) [VERIFIED — OB-1/2 ✓✓, OB-4, OB-8].

**Namespace.** Plugin `id` first-come, globally unique, lowercase, can't contain "obsidian"; names can't imply first-party status; abandoned plugins are transferred to a new owner or removed [VERIFIED — OB-9, OB-10, OB-15].

| id | Claim | Source | Accessed | Status |
|---|---|---|---|---|
| OB-1 | No-sandbox honesty; capability list | obsidian.md/help/plugin-security | 2026-07-02 | VERIFIED ✓✓ |
| OB-2 | Restricted Mode default-on | same page | 2026-07-02 | VERIFIED ✓✓ |
| OB-3 | Automated per-version scans; scorecard; manual for popular/featured/flagged | same page | 2026-07-02 | VERIFIED ✓✓ |
| OB-4/5 | Policies: no obfuscation/telemetry/self-update; disclosure regime | docs.obsidian.md/Developer+policies | 2026-07-02 | VERIFIED |
| OB-7/8 | Submission mechanics; GitHub-releases CDN; versions.json compat mapping | docs.obsidian.md/Plugins/Releasing/Submit+your+plugin; github.com/obsidianmd/obsidian-releases | 2026-07-02 | VERIFIED |
| OB-9/10 | Manifest schema; id/name rules | docs.obsidian.md/Reference/Manifest | 2026-07-02 | VERIFIED |
| OB-13 | 2,300-backlog; per-version scanning relaunch; 4,000+/120M figures; review-time note | obsidian.md/blog/future-of-plugins/ | 2026-07-02 | VERIFIED |
| OB-14 | Paid plugins allowed; "not a store"; closed-source closed to new | same blog | 2026-07-02 | VERIFIED |
| OB-15 | Abandonment: transfer or removal | same blog | 2026-07-02 | VERIFIED |
| OB-16 | 5,317 live registry entries (parsed count) | raw…/obsidian-releases/master/community-plugins.json | 2026-07-02 | VERIFIED |
| OB-17/18/19 | 8-person team; named reviewer; user-supported; license tiers | obsidian.md/about; obsidian.md/license | 2026-07-02 | VERIFIED |
| OB-20/21 | BRAT mechanics; official recommendation | github.com/TfTHacker/obsidian42-brat; docs.obsidian.md/…/Beta-testing+plugins | 2026-07-02 | VERIFIED |
| OB-22 | REF6598/PHANTOMPULSE; required manual enablement | elastic.co/security-labs/phantom-in-the-vault | 2026-07-02 | VERIFIED (vendor) |
| OB-24 | CM5→CM6 breaking case; Legacy Editor fallback | obsidian-codemirror-options README | 2026-07-02 | VERIFIED (via excerpt) |

---

## §2 Cross-cutting answers (the charter's seven questions)

**Q1 — What makes third-party ecosystems trustworthy?** Not one mechanism but a converged stack, observable at every mature marketplace by 2026: (a) durable identity — two-level publisher-scoped IDs, domain-verified publishers, immutable extension IDs (VS Code, Chrome; L-28); (b) **per-version** automated scanning + dynamic detection, with manual review reserved for risk tiers (Obsidian, Chrome, VS Code; L-7, L-21); (c) signing at publish + client-side verification (VS Code, HA add-ons Cosign); (d) a kill-switch: server-side removal that propagates to client auto-disable (Chrome malware verdict, VS Code block list, HA insecure-version blocking; L-7); (e) disclosure policies instead of impossible guarantees (Obsidian's disclosure regime; the point-in-time honesty of Homebridge verification; L-20); (f) default-off for unreviewed code (Restricted Mode, Z2M 2.11.0, HA add-on protection mode; L-4). Review tiers keyed to declared capability breadth (Chrome's permission-keyed review depth) are the triage mechanism that makes human review affordable (L-21).

**Q2 — What versioning/deprecation policies actually held communities together (→ AX-7)?** The surviving pattern is: immutable released artifacts + semver evolution + a declared compatibility range that the registry enforces by serving only compatible versions (VS Code `engines.vscode`, Obsidian `minAppVersion`+`versions.json`, HPM `minimumHEVersion`; L-9, L-14); a stable-API pledge with a formally gated unstable tier (VS Code proposed APIs; L-10); platform-side deprecation floors measured in release cycles with automated repair surfaces (HA ADR-0021 ≥6 cycles; L-11); and, for breaking majors, long notice + automated migration + parallel old-line maintenance (Z2M 2.0's 3-month notice and migration log; openHAB Thing upgrades; Homebridge's parallel 1.x line; L-11). Strict whole-component immutability appears nowhere at ecosystem scale; the nearest mechanisms are version-locked distribution channels (SmartThings Edge) and build-time ref pinning (ESPHome) — pinning at *distribution*, not immutability of the *definition* (L-15). The two ecosystem-breakers violated the same clause: kill date before replacement parity (L-12), and the communities' exits were permanent (L-13).

**Q3 — Where is the in-process/out-of-process isolation line drawn, and at what cost?** Three rungs observed in production: (1) in-process, unsandboxed — universally acknowledged as full-compromise risk (HA 2021, Z2M docs, Obsidian docs; L-1) and tolerated only behind quality gates or explicit user opt-in (L-4); (2) child process — crash/perf containment, restartability, per-extension resource attribution, at ~20–30 MB per process and added pairing/config friction; retrofittable as pure configuration when the contract is narrow (Homebridge child bridges; L-3); crucially it is NOT privilege separation — VS Code's extension host and child bridges alike run at full user privilege (L-2); (3) container with scoped API roles + signing — actual privilege separation (HA add-ons: 1–6 rating, AppArmor, Cosign; L-6). The design conclusion the evidence supports: never promise sandboxing the runtime can't enforce; state the rung honestly and make the default rung safe (L-4). HomeSynapse's `IsolationLevel.RESERVED_SUBPROCESS` maps to rung 2, and the Homebridge precedent shows the seam can be exercised late, cheaply, if the adapter contract stays process-agnostic (L-3).

**Q4 — How do data-driven extension models govern quality at scale?** The Z2M staging-area loop is the strongest observed pattern: auto-generate from device discovery → refine declaratively (modernExtend) → PR into the shared, CI-validated corpus → near-per-merge releases → the contributor deletes the local copy (L-22). Quality control is CI validation + fingerprint/priority collision governance (L-30), not human review depth (a sampled PR merged with "No reviews"). The failure mode is API drift rotting the floating population of unmerged extensions (L-22's converse), and the whole model rides on bus-factor ≈1.5 (L-26). ESPHome shows the config-as-data extreme (no runtime plugins at all; build-time git pinning); HA blueprints show data-only automation sharing. All three vindicate D5's adapt-the-data direction while warning that the *pipeline* (staging → merged corpus) matters as much as the format.

**Q5 — What licensing/commercial coexistence models worked for Apache-2.0-class cores?** HA is the direct precedent: Apache-2.0 core, optional paid cloud (Nabu Casa) funding development, zero vendor-paywalled community content, and a certification program (Works-with-HA) bound to the public quality ladder (L-24, L-25). openHAB (EPL) mandates FOSS-only marketplace content — no keys/trials/freemium. Obsidian (proprietary core) permits third-party-paid plugins with disclosure but hosts no payments and takes no cut. VS Code demonstrates the inverted lever: MIT core, proprietary *registry* — control lives in the marketplace terms, not the code license (L-16, and the R-C framing in the charter). Across all nine: vendor revenue = services, hardware, certification; community content = free or third-party-monetized; **no surveyed vendor paywalls community-contributed content** (L-24).

**Q6 — What namespace/identity governance prevents type-collision chaos?** The mature endpoint: two-level publisher-scoped identity with verified publishers and immutable IDs (VS Code `publisher.name`, Chrome key-derived IDs; L-28). Flat first-come naming plus abandonment demonstrably yields fork confusion (Homebridge's own words) and re-registration loopholes (VS Code removed-name reuse) — and the fixes were retrofitted governance apparatus (reserved org scopes, transfer-on-abandonment; L-26, L-28). Collision policy must be an explicit ruling: HA sanctions custom-shadowing-core with UI flagging and core-brand preference; openHAB bans competing marketplace add-ons socially (L-29). For device-data corpora, identity is fingerprint matching with explicit priority + rebrand mapping (Z2M whiteLabel; L-30) — directly relevant to the M9.3 profile registry.

**Q7 — What do marketplaces need at MINIMUM viable trust?** The floor, synthesized from the small-team cases (Obsidian, openHAB, HPM): (1) a registry of record with unique IDs and a manifest carrying `version` + platform-compat range (L-8, L-9); (2) versioned, immutable release artifacts hosted on existing infrastructure (L-16); (3) automated checks per version — even shallow ones — plus a public quality/safety signal (scorecard, maturity label; L-21, L-18); (4) revocation that reaches clients (L-7); (5) disclosure-based policies with a small banned list (no obfuscation, no self-update, no undisclosed network/telemetry; L-4, per OB-4); (6) explicit user opt-in for the unreviewed tier (L-4). NOT required at minimum: payments, first-party hosting, continuous audit, sandboxing promises. The two-tier core/community split with honest labeling is the load-bearing shape (L-18).

---

## §3 Lessons ledger (cited by the charter as L-n)

*Trust & isolation.*
- **L-1** Unsandboxed in-process extension code turns any extension bug into a platform-wide compromise — HA's 2021 traversal disclosure, Z2M's own securing docs, Obsidian's capability honesty [HA-4, Z2M-6, OB-1].
- **L-2** Process isolation buys crash/perf containment and restartability, NOT privilege separation — VS Code's host runs "with the same permissions as VS Code itself"; child bridges likewise [VSC-4, HB-7].
- **L-3** Subprocess isolation is retrofittable as pure configuration when the plugin contract is process-agnostic — Homebridge child bridges: per-plugin process, auto-restart, zero plugin code changes, 20–30 MB each [HB-7, HB-8].
- **L-4** The honest small-team trust posture is no-sandbox-stated-plainly + third-party code off by default — Obsidian Restricted Mode; Z2M 2.11.0 external-JS default-off; HA add-on protection mode [OB-1/2, Z2M-1/11, HA-9].
- **L-5** Moving capability from imperative code into declarative, reviewable data is the most-repeated trust win — Chrome remote-code ban + DNR; VS Code contribution points; HA blueprints; Z2M modernExtend; ESPHome YAML [CR-6/8/9, VSC-8, HA-15, Z2M-1, ESP-6].
- **L-6** The graded isolation ladder is the surviving architecture — in-process (quality-gated) → child process (crash/perf) → container with scoped API roles + signing; HA runs all three rungs simultaneously [HA-8/9, HB-7, VSC-1].
- **L-7** Mature marketplaces converged on one defense stack: per-version automated scanning + dynamic detection + signing + kill-switch/blocklist with client auto-disable + name-squat protection [VSC-5, CR-3, OB-3, HA-5].
- **L-8** A `version` field in the extension manifest is the minimum forensic/blocking primitive — HA retrofitted it under incident pressure (required from 2021.6) [HA-5].

*Versioning & deprecation (→ AX-7).*
- **L-9** A declared engine-compatibility range + a registry that serves only compatible versions is the field-standard compat gate [VSC-9/10, OB-8/9, HUB-4, HB-10].
- **L-10** A stable-API pledge with a formally gated unstable tier (proposed APIs: pre-release-only, declared, unpublishable) is how a 131K-extension ecosystem survives monthly releases [VSC-9, VSC-13].
- **L-11** Breaking changes are survivable with long notice + automated migration + parallel old-line maintenance — Z2M 2.0 (3-month notice, auto-migration + backup log); openHAB Thing upgrades; Homebridge parallel 1.x; HA ADR-0021 (≥6 release cycles + Repairs) [Z2M-12/13, OH-14, HB-9, HA-14].
- **L-12** Ecosystem-killing migrations share a signature: kill date announced before replacement parity, "seamless" promises, tooling removed mid-transition — SmartThings Groovy (38-month arc, fingerprint-or-dead-Thing); Chrome MV3 (2.5-year slip, pause, concessions-after-backlash) [ST-1/2/3/6, CR-1/2/7].
- **L-13** When a platform breaks its extension layer, the community's exit is real and permanent — webCoRE→Hubitat/SharpTools; uBlock Origin exited Chrome rather than migrate [ST-7/8, CR-13].
- **L-14** Immutable released artifacts + semver evolution + forward-only migration is the observed surviving pattern; strict whole-component immutability appears nowhere at ecosystem scale [INFERRED — across VSC-9/10, OB-8/9, Z2M-3, HB-9].
- **L-15** Version pinning belongs at the distribution layer — SmartThings channels lock driver versions; ESPHome pins git refs at build [ST-9, ESP-6].

*Distribution & marketplace.*
- **L-16** Every small-team registry outsources hosting/identity to existing infrastructure (npm, GitHub releases, Discourse, raw GitHub) — near-zero cost, but you inherit the host's failure modes and supply chain; the Eclipse Marketplace died of its host's governance change [HB-1/4, OB-8, OH-3/8/9, HUB-4].
- **L-17** An unofficial installer arises wherever official distribution has friction; the healthy response is embrace-and-partner — HACS as designed-optional OHF partner; BRAT officially recommended; HPM filling Hubitat's vacuum [HA-21, OB-20/21, HUB-3].
- **L-18** The surviving marketplace shape is two-tier: reviewed core/distro + explicitly-labeled community tier with a lower bar and honest warnings [HA-1/21, OH-9/18, HB-4/6].
- **L-19** A quality ladder works when it is machine-tracked per rule, demotable, commerce-coupled, and re-baselineable — HA quality scale: `quality_scale.yaml`, code-owner-loss demotion, Gold-for-certification, all scores dropped at relaunch [HA-1/2/3].
- **L-20** Verification programs are point-in-time checklists + reactive revocation, not continuous audit — and the credible ones say so [HB-4].
- **L-21** Manual review does not scale; the scalable floor is automated per-version scanning + risk-tiered human review — Obsidian's 2,300-submission backlog → per-version scans with manual review only for popular/featured/flagged; Chrome's permission-keyed review depth [OB-3/13, CR-3].
- **L-22** The staging-area model is the strongest anti-rot pattern for data-driven extensions: external → PR → merged corpus → delete local copy, enabled by CI validation + near-per-merge releases (5,473 devices on bus-factor ~1.5) [Z2M-1/2/5/9/10].
- **L-23** Resource caps on extensions exist in every production platform and must be user-visible, designed quotas, not discovered mystery limits — SmartThings' 50-driver popup; HAP's 149-accessory cap [ST-11, HB-1/7].

*Community & economics.*
- **L-24** No surveyed OSS platform vendor-paywalls community-contributed content; vendor revenue is services/hardware/certification beside a fully free ecosystem; openHAB bans paid marketplace content outright; Obsidian permits third-party-paid with disclosure, hosting no payments [HA-17/21, OH-10, OB-14, NR-16].
- **L-25** Certification programs monetize trust without paywalling content by binding a commercial badge to the public quality ladder — Works-with-HA requires Gold [HA-1/2].
- **L-26** Bus-factor-1 is the default state of community extension infrastructure at every layer; governance must pre-plan ownership transfer and adoption — Homebridge org adoption (repo+npm), Obsidian transfer-or-removal, HAMH "may the best fork prevail" [Z2M-14, HUB-3, HB-11/12, OB-15, M-19].
- **L-27** Closed platform + vendor-hosted runtime = zero community leverage at pivot time; open core + local runtime = community continuity — webCoRE died on SmartThings, lives on Hubitat; the honorable complement was Apache-2.0 stock drivers [ST-7/8/12].

*Namespace & identity.*
- **L-28** Flat first-come naming + abandonment yields fork confusion and re-registration loopholes; the mature endpoint is two-level publisher-scoped identity + domain-verified publishers + immutable IDs [VSC-10/14, HB-2/11, CR-14].
- **L-29** Namespace collision policy must be an explicit ruling, not an accident of load order — HA sanctions custom-over-core shadowing with UI flagging and core-brand preference; openHAB bans competing add-ons socially [HA-6/7/18, OH-10].
- **L-30** Device-identity matching at data scale needs fingerprint disambiguation with explicit priority + rebrand mapping (Z2M fingerprints > zigbeeModel; whiteLabel; Tuya generic-modelID stress case) — binds directly on the M9.3 profile-registry shape [Z2M-7].

*AI-relevant (the automations-with-AI angle).*
- **L-31** Marketplaces' 2025–26 posture shift to per-version automated scanning was forced by authorship volume outrunning human review — the gate an AI-accelerated plugin era requires is automated, per-version, and public (scorecards) [OB-3/13, VSC-5/12/15].
- **L-32** The declarative-artifact review model (L-5) is exactly the gate an AI-authoring pipeline needs: reviewable data artifacts, machine-checkable, diffable — Chrome's safe declarative-rule updates skip human review and publish in minutes [CR-9].
- **L-33** No surveyed platform lets AI-authored content bypass its extension review gates; HA's shipped AI direction is deterministic-first, schema-constrained, AI-suggests/human-saves — independently convergent with AIOT-INV-1's proposer-only frame [prior pass 2026-06-27 C3-6; INFERRED — convergence claim].

---

## §4 Provenance & audit surface

**Method.** Eight parallel research subagents (one per ecosystem cluster), each under the anti-fabrication discipline, primary-sources-preferred, fetch-before-cite. Agent ids (session-recorded): HA a6994fc597bb539fd (41 tool calls) · Z2M ad34d479db0495af6 (29) · SmartThings a0846f1598d907f89 (17) · Homebridge abdee2d0c921b7cb5 (28) · openHAB aa23a931b0cb06439 (30) · Hubitat/ESPHome/Node-RED/Matter a4620e7d2ce833cdc (36) · VS Code aedf4b2579ba990e4 (26) · Chrome ad41267a5c7dbb47e (19) · Obsidian a8f62dc2df6f81a84 (22). Lane-direct re-verification (second layer, ✓✓): HA quality scale · Z2M external converters · Homebridge child bridges · VS Code runtime security · Chrome MV2 timeline · Obsidian plugin security — all six re-fetched 2026-07-02 and the quoted fragments confirmed verbatim.

**Honest gaps (kept, not laundered).** Exact HA core/HACS catalog counts (official index fetch truncated; >1,100 floor only). SmartThings: no official count of affected community DTHs was ever published; per-hub memory limits community-reported only. Homebridge `config.schema.json` introduction date. VS Code verified-publisher share of catalog. Z2M historical growth curve (archive access blocked). Whether a Node-RED release newer than 4.1 exists was not checked. Hubitat↔SmartThings Groovy-retirement date cross-reference rests on the SmartThings lane's staff-post fetches, not the Hubitat lane's.

**Known deltas vs the dispatch brief's priors (corrections).** openHAB 4.0 released 2023-07-23, not Jan 2023. HA add-on content-trust work dates to 2022 (CAS), since superseded by Cosign; add-ons rebranded "apps"; current rating scale 1–6. VS Code marketplace is ~131K extensions, not 60–70K. Homebridge verified plugins ≈602 of 5,542 keyword packages. Obsidian's registry holds 5,317 plugins, above the vendor blog's rounded "4,000+."

*Return complete. The hub two-layer audits this dossier together with the companion charter (context/planning/2026-07-02_Doc-18_requirements-charter.md) before anything folds into Doc 18 authoring.*

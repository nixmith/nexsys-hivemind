<!--
file: context/research/2026-08-30_RS5_plugin-ecosystem_return.md
purpose: RS-5 — plugins as the community wedge: the evidence return, per the charter at context/strategy/2026-08-30_RS5_plugin-ecosystem_community-wedge_strategy-charter.md. Falsifiers FIRST (§0.1: trust-boundary dilution · API-freeze debt), then the dated ecosystem census (§3), the wedge comparison (§4), the MHS adjacency (§5), and the honest register sentences per branch (§6). Feeds the strategy beat (R-10 weekend at the earliest sensible seam, or its own sitting at Nick's word). NOTHING here is adopted strategy; this return pre-authorizes nothing public and amends nothing in v1.1 or the September plan.
audience: the hub (intake; two-layer audit; re-fetch the ★-marked primaries) · the strategy beat · Nick (branch words arrive in H10 form from the hub AT the beat, not from this lane)
state-type: research return (write-isolated; point-in-time 2026-08-30 CT)
status: RETURNED 2026-08-30 (Sun, CT) by the RS-5 lane (fresh Cowork session; web-backed; device-mounted repo read-only except this file). This file is the lane's ONLY repo write. Zero git commits, zero code, zero outreach, zero accounts, zero posts, zero public sentences. The hub adjudicates.
laws-held: D5 on every enforcement formulation (the deterministic floor is MISSING from the field, not SUPERIOR; L2/L3 without L1 are unsound; L1 without L2 is insufficient) · H9 (nothing in §6 is public until a lifting WU's audited return mints it into the claim register) · anti-fabrication ([VERIFIED] = primary fetched this lane with URL + access date; [DOSSIER] = carried from the audited 2026-07-02 plugin-ecosystem-wars dossier with ITS access date; [INTERNAL] = repo document read at host this lane; [REPORTED] = named secondary; [INFERRED] = this lane's own reasoning, said so) · unbiased-instrument (falsifier-relevant evidence leads; no [REPORTED] item drives a verdict alone) · gate sovereignty (this return builds nothing, schedules nothing, prices nothing bindingly — milestone pricing is PM work) · the lane claims no design authority — Doc 18 readings here are consumer readings; Doc 18's own text wins on conflict.
scripting-note: the charter's pin (anthropic==0.21.3 + httpx<0.28) is N/A — no API scripting was used; the instruments were the session's own fetch/search tools + device shell reads.
ct-rederivation: REQUIRED LINES, derived AT THE INSTRUMENT at filing, never from memory —
  device instrument:    TZ=America/Chicago date → 2026-08-30 21:19:15 CDT (Sunday) · UTC 2026-08-31 02:19:15
  container instrument: TZ=America/Chicago date → 2026-08-30 21:19:15 CDT (Sunday) · UTC 2026-08-31 02:19:15
  The session's UTC banner day already reads 2026-08-31; the CT filing date is 2026-08-30 and the filename uses it. This is the W-SKILLS-4 harvest-5 hazard (RS-4 hit it 2026-08-29; this is the next instance, caught at derivation).
instrument-limits: disclosed in full at §0.6; every place a limit bit is ALSO marked inline.
re-fetch-at-consumption (★ = the hub should independently re-fetch): ★ home-assistant.io/blog/2021/01/23/security-disclosure2/ · ★ analytics.home-assistant.io (headline installs) · ★ iotsecurity.engin.umich.edu (Fernandes S&P'16 figures) · ★ homey.app/en-us/features/apps/ (vendor counts) · raw.githubusercontent.com/HubitatCommunity/hubitat-packagerepositories/master/repositories.json · api.github.com/repos/SmartThingsCommunity/SmartThingsEdgeDrivers/contributors?per_page=100&anon=true · home-assistant.io/blog/2025/04/16/state-of-the-open-home-recap/ · home-assistant.io/blog/2024/08/21/hacs-the-best-way-to-share-community-made-projects/
-->

# RS-5 — plugins as the community wedge: the evidence (filed 2026-08-30 CT)

## §0 The hub-actionable summary — falsifiers first

**Read this section as: the two kill-questions answered first, then the branch table, the source census, the deviations, and the asks. The hub can act on §0 alone; §1–§7 are the evidence spine.**

### §0.1 Falsifier verdicts

**F-1 — the dilution falsifier (charter §1.1): the pivot SURVIVES ONLY IN ITS DATA-FIRST MEANING NOW; the code-SDK meaning dilutes L1 as long as the trust ladder is unbuilt, and the honesty rule forbids papering over that with language.**

- **What Doc 18 actually provides today [INTERNAL — Doc 18 §3.3; extensibility assessment §2]:** the four-rung ladder is DESIGNED, and none of it is BUILT. Today an adapter receives an **unscoped** `EntityRegistry`/`StateQueryService` (rung 1 unbuilt), a **full** `EventPublisher` (rung 2's permitted-publish-types check unbuilt), no quotas (rung 3 = INV-RF-02's reserved path, unimplemented), and `RESERVED_SUBPROCESS` is an enum slot (rung 4 unbuilt). The assessment's own words: the third-party trust boundary "exists on paper only."
- **The structural consequence [INFERRED, from the above]:** third-party code inside the JVM today can (a) read all entity state — a privacy-posture puncture; (b) publish arbitrary event classes — and since the deterministic engine trusts the log, spoofed events are **indirect actuation through the very floor we claim**; (c) as the device driver, actuate its own devices by definition; and (d) — the deepest cut — **forge the attribute reports that feed `ConfirmationPolicy`, i.e., counterfeit the measured `confirmed|unconfirmed` verdict for its own devices.** The verdict corpus's integrity is itself downstream of the trust boundary holding. An un-fenced public code SDK does not merely add risk beside the L1 claim; it hollows the evidence the L1 claim stands on.
- **In-process isolation buys nothing here [DOSSIER — L-2]:** process/child isolation buys crash containment, not privilege separation; VS Code's own extension host runs "with the same permissions as VS Code itself."
- **What a public SDK must promise vs what may honestly be said [INTERNAL — DP-18-B]:** the ruled honesty rule — *no sandbox or isolation language in any external copy before the enforcing rung exists* — means the ONLY honest public SDK posture this fall would be "third-party code runs in-process, unsandboxed, curated." The field proves that posture is survivable (Obsidian Restricted Mode; Z2M external-JS default-off since 2.11.0; HA's Custom-tier disclaimer [DOSSIER — L-4]) — **but every platform for which it is survivable sells something other than the trust boundary.** For a company whose product IS the enforced floor, the honest sentence "we have no sandbox yet" spends the launch on an absence.
- **What the incidents cost the platforms that ran ahead of the fence [VERIFIED + DOSSIER — §1.3 below]:** HA's Jan-2021 custom-integration traversal (HACS + 3 others; "access any file… includes any credentials") cost an emergency core release with path-traversal shields around third-party code, Nabu Casa blocking vulnerable instances from Cloud, companion-app warning pushes, and the retrofit of the `version` manifest key "in light of these incidents" — governance added under incident pressure [★VERIFIED disclosure-2 blog, access 2026-08-31 UTC; DOSSIER HA-4/HA-5]. SmartThings' Groovy SmartApp model was shown at IEEE S&P 2016 to leave "over 55%" of 499 analyzed SmartApps overprivileged, with a working door-lock pin-injection exploit — national-press reputational cost, and the eventual architectural answer was the ecosystem-breaking Groovy→Edge migration [★VERIFIED UMich project page, access 2026-08-31 UTC; DOSSIER ST-1..8, L-12]. **Pattern: no surveyed platform died of a plugin incident, but every one retrofitted governance under pressure (L-8). A trust-positioned company cannot run that arc; the fence must precede the wedge.**
- **The fence that needs no waiting [INTERNAL — Doc 18 §2 principle 4, D5; DOSSIER — L-22]:** the data-first channel — device profiles, converters, blueprints-class declarative artifacts through a staging-area pipeline — admits community contribution with **zero third-party code inside the trust boundary**, and it is the field's strongest observed pattern (Z2M: 5,473 devices from 577 vendors maintained at bus-factor ~1.5). **Verdict: the pivot does not die at F-1 — it survives by meaning plugins-as-data now, plugins-as-code only at the rung that fences it (curated `IN_JVM` behind the quality gate per DP-18-B; non-curated only at `RESERVED_SUBPROCESS`).**

**F-2 — the API-freeze-debt falsifier (charter §1.2): CONFIRMED for a public code SDK this fall — the freeze debt would eat the fall, so the code-SDK wedge is LATER, not now. The data-first wedge adds approximately zero new freeze.**

- **What a public code SDK freezes (enumeration at §2):** the SPI itself is already frozen (AMD-54..64 — sunk cost, an asset). But a PUBLIC SDK additionally freezes, as third-party-relied-upon behavior: the packaging manifest format + `version` + declared compat-range semantics (Doc 18 seam 6); namespace/identity governance activated (seam 5); ladder rungs 1–2 as observable behavior (seam 4); the aggregation gate if third-party event classes are admitted (seam 3); the operation registry if operations are exposed (seam 2); the LTD-17 amendment + security evaluation if dynamic loading ships (seam 1, OQ-2 deliberately unratified); and AX-7's mechanism (Doc 16 OQ2, deliberately unresolved) if automation components are in scope.
- **The debt multiplier is already ruled [INTERNAL — Doc 18 OQ-1, co-signed]:** every surface frozen for third parties carries the deprecation floor — **six release cycles + a Repairs-class automated-migration surface, never below LTD-16's one-major-version minimum.** Freezing pre-1.0 means carrying six-cycle migration duty on surfaces that WILL move (the field's evidence that they move: Z2M's herdsman-converters broke majors 15→25 openly [DOSSIER Z2M-3]; VS Code survives monthly releases only via a formally gated proposed-API tier [DOSSIER L-10]).
- **M-milestone shape (lane estimate — the PM prices it; this lane has no design authority) [INFERRED]:** an honest public code SDK requires, before launch: rung 1 (scoped context wrappers) + rung 2 (publish-permission enforcement) + packaging/manifest + compat-gate + namespace activation + SDK docs + example-adapter + CI harness for third-party artifacts — three-to-five milestone-class builds sitting squarely on the fall's MVP path, none of which are on it today (R-4 backlog rows name the rungs; none gates V1). Versus: the data-first wedge's surfaces are the M9.3 profile registry and the D5 converter/IR schemas — **already scheduled, already carrying Doc 18 §3.5's constraints as design constraints.**
- **Verdict: freeze-debt kills "SDK now," not "plugins as the wedge."** The wedge survives F-2 in exactly the same form it survives F-1: data-first now, code-SDK at its own later milestone.

**Two secondary findings the beat should hold alongside the falsifiers:**

- **S-1 — the license chain still gates every inbound-contribution surface, including data [INTERNAL — LB return 2026-08-01 §1.1; entity ruling 2026-08-27].** The repos' LICENSE files are proprietary; an inbound contribution to an all-rights-reserved repo has no license to arrive under. The chain is one-directional: entity (settled) → founder-IP assignment → Apache-2.0 flip (v1.1 P2 window; §VIII(4) consent gate on counsel's word) → any contribution surface. **A wedge date spoken before the flip date is scheduled is a sentence the register cannot back.**
- **S-2 — contributor evidence says the wedge cannot precede an installed base [DOSSIER + §3.2].** In every surveyed ecosystem the first contributors were existing USERS scratching a device itch (HACS: authors who "didn't have the time to meet Home Assistant's requirements"; Koenkk maintaining Z2M "in my spare time"; HPM built by one user; openHAB's Z-Wave DB built to spare "a small group of people"). An SDK launched before there are users produces an empty registry, not a community. The first-20 motivation is: *my device, my home, my itch* — which the bench + data-channel wedge serves and a bare SDK does not.

### §0.2 The branch table (charter §1.4 · §1.6, compressed — full analysis §4, sentences §6)

| branch | soonest honest register sentence | falsifier exposure | freeze debt | thesis test (compounds under model progress?) | verdict offered to the beat |
|---|---|---|---|---|---|
| **A — plugin-SDK-first** | at code-SDK launch, the honest sentences are "the contract is frozen; core boots with the extension set empty; **no sandbox exists yet**" — true, auditable, and an absence where the story should be | F-1 direct (in-JVM third-party code) unless data-only; F-2 direct | HEAVY (3–5 milestone-class builds + six-cycle duty on every frozen surface) | neutral-to-negative: the SDK itself is substrate-agnostic; un-fenced code inside the boundary actively erodes the layer the bet sits on | **NOT NOW in code form; its data-first core folds into C** |
| **B — explainability-hero-first** | already scheduled: the RS-3 §6.1-1 field sentence stands; the explain surface becomes the demo at R-10 (v1.1 P3 B-6 — the incumbent of record) | none new | none | compounds: pure log projections, model-agnostic, better models make the explanations more valuable to check | **remains the demo surface; not displaced by this return** |
| **C — verification/bench-as-product** | **soonest of all three**: C-001/C-002 mint on the R-4 record (Monday-night fill-in, independent of any wedge); the corpus sentence ("every admitted profile carries a measured verdict at a named commit") follows the same shape | none new — the bench sits OUTSIDE the trust boundary; contributions are data | LIGHT (profile/IR schemas already M9.3-governed) | compounds strongest: the verdict corpus grows with every device and every model generation; a better model makes the measured floor MORE legible, not less | **the strongest wedge — and it IS the data-first plugin on-ramp** |

**The convergence finding (the single most actionable line in this return):** branch C and the data-first plugin channel are the SAME ACT — *bring your device; submit its profile as declarative data through the staging pipeline; the bench measures; the verdict publishes as `confirmed|unconfirmed`; the profile enters the corpus.* The community wedge that survives both falsifiers is **plugins-as-data-with-a-measured-verdict** — branch C wearing the plugin story, with branch B as its demo surface exactly where v1.1 already gates it (R-10). Nick's 2026-08-30 input ("pivoting more towards the idea of the plugins") is thus not refuted by the falsifiers — it is *sequenced* by them: the plugin ecosystem opens as a data corpus with verdicts this fall–winter (post-gates), and as a code SDK at the rung that fences it.

### §0.3 Census of sources

- **Fresh primaries this lane:** 12 fetches + 7 searches executed 2026-08-30/31 UTC (access datetime ≈ 2026-08-31 01:10–02:20 UTC = 2026-08-30 evening CT); itemized with URLs and what each evidences in §7. Headline fresh numbers: HA analytics 675,103 → 673,433 active opt-in installations (live counter moved between fetches — disclosed); "535,309 of 673,433 (79.49%)" share integration data; SOH-2025 blog: "over 2 million active installations in 2024," "21,000+ unique contributors in 2024"; Homey vendor page: "1,200+ apps," "over 70,000 devices from 2,000+ brands"; Homey community scrape: "4860 drivers in total across all apps" (2025-12-31, community-derived); Hubitat HPM repositories.json: 281 repository entries; SmartThings Edge drivers repo: ≥100 contributors (API page-cap floor), top-5 all first-party staff by contribution count; HACS default integration list: ≥2,000 entries visible before instrument truncation; Fernandes/UMich S&P'16: 499 SmartApps, "over 55%" overprivileged; HA disclosure-2 (2021-01-23): 4 custom integrations, traversal, response measures.
- **Carried from the audited internal corpus, dated at THEIR access:** wars dossier L-1..L-33 + per-platform figures (fetched 2026-07-02); extensibility assessment (2026-07-02); LB community-plugins return (2026-08-01); WMARKET2 §M (2026-08-28, audited ACCEPT); MHS datum + addendum (2026-08-28); RS-4 (2026-08-29); Doc 18 (LOCKED 2026-07-03); Substrate Thesis v0; strategy v1.1 (PROPOSED, EDIT-ALL-4 applied); claim-register scaffold (v58 beat 9).
- **Nothing in this return rests on a [REPORTED] item alone.**

### §0.4 Deviations from the charter — disclosed

1. **The census leans on the audited 2026-07-02 dossier where it was already primary-sourced**, and fresh instrument time went to what the dossier lacked (Homey — absent from the dossier entirely; HA install currency; SmartThings Edge contributor shape; HPM count) plus the falsifier-side primaries. Every carried number is tagged [DOSSIER] with its 2026-07-02 access date. The charter's "primary sources; numbers dated" is held; "re-fetch everything" was not attempted and is not claimed.
2. **Time-to-first-plugin could not be cleanly derived** for any platform within instrument limits; §3.3 gives the documented proxies and says what they do and do not evidence.
3. **Contributor counts are floors, not totals**, where GitHub's UI/API caps bit (§0.6 items 4–5).
4. **Homey's two counts are different units** (vendor "1,200+ apps" vs community "4,860 drivers"); both are reported, neither is treated as the other.
5. **M-milestone cost is given as SHAPE, not numbers** — pricing milestones is PM/hub work; the lane stating a week-count would be design authority it does not hold.

### §0.5 Asks

1. **Hub:** two-layer audit; independently re-fetch the ★ primaries (header list) before any finding drives a beat word.
2. **PM (if the beat wants a code-SDK date):** price the rung-1/rung-2 + packaging/namespace milestone shape from §2's enumeration. Not asked: any build.
3. **The beat:** rule on the convergence finding — the wedge as branch C wearing the plugin story (plugins-as-data-with-a-measured-verdict), with the code SDK sequenced at its fenced rung. Any v1.1 P3/B-6 amendment is Nick's word at the beat, not this lane's.
4. **The calendar:** confirm the Apache-2.0 flip's place on the fall calendar BEFORE any wedge date is spoken publicly (S-1) — the flip gates even data contributions.
5. **Optional:** if exact Homey/ST-Edge totals matter to the beat, charter a short browser-instrumented pass (the JS-rendered surfaces in §0.6).

### §0.6 Instrument limits hit — full disclosure

1. Device-shell listing of the hivemind tree truncated at 262,144 output characters on the first pass (`.git` objects dominated); re-run scoped. No content loss in the end state.
2. GitHub's rendered pages no longer expose total contributor counts in fetchable text (home-assistant/core shows avatars only); **HA total contributor count is carried from the SOH-2025 blog figure instead** ("21,000+ unique contributors in 2024" — project-wide, 2024, not repo-total).
3. GitHub API contributor listings cap at 100/page and the instrument cannot walk pagination headers → **SmartThingsEdgeDrivers contributor count is a floor (≥100)**.
4. api.github.com returned 403 on the Homey stats repo contents (unauthenticated rate/policy) → the community scrape's underlying JSON was unreachable; the forum-posted figure is used, attributed and dated.
5. smarthomesven.github.io and analytics.home-assistant.io data tables are client-side rendered; the instrument sees placeholders → only headline/served-text figures are cited.
6. The two analytics.home-assistant.io headline fetches, minutes apart, returned 675,103 and 673,433 — a live counter; both are reported, neither is "the" number.
7. The HACS default-integration list truncated mid-array at ~2,000 visible entries (alphabetically into "m") → **≥2,000 is a floor; the true count is higher and unverified**. The dossier hit the same wall 2026-07-02 (">1,100 entries, truncated"). HA's official integrations index states no total ("thousands of brands," no count) — **the HA core integration count remains UNVERIFIED in our corpus at ~3,000 [REPORTED, secondary blogs only]**.
8. WebSearch is US-only (tool-stated); non-US-indexed sources may be under-represented.
9. No Reddit or login-gated forum pass was attempted (consistent with the R-lane record; adjudication D(2) owns Reddit).
10. No API scripting; the charter's anthropic/httpx pin was therefore never exercised.

---

## §1 F-1 in detail — the dilution falsifier (charter §1.1)

### §1.1 Doc 18's isolation: designed vs built vs claimable

| rung (Doc 18 §3.3) | designed | built today | what its absence means for third-party code | public claim allowed (DP-18-B) |
|---|---|---|---|---|
| 1 — scoped context wrappers | yes | **no** — `EntityRegistry`/`StateQueryService` injected unscoped | any adapter reads ALL home state | no isolation language until it enforces |
| 2 — publish permissions | yes | **no** — full `EventPublisher`; permitted-publish-types check unbuilt | any adapter publishes ANY event class → the engine acts on spoofed truth | same |
| 3 — resource quotas | yes (INV-RF-02 reserved path) | **no** | crash/starve containment only via supervision, no caps | same |
| 4 — `RESERVED_SUBPROCESS` | enum slot bought (AMD-63) | **no** | non-curated code shares the JVM | same; the intended default rung for non-curated code at marketplace time |

[INTERNAL — Doc 18 §3.3 + extensibility assessment §2 ("trust boundary paper-only"). Consumer reading; Doc 18's text wins on conflict.]

### §1.2 The four puncture routes, stated plainly [INFERRED from §1.1; the mechanism claims are the assessment's]

1. **State read** — privacy-posture puncture: the written privacy posture (E-4 fence) cannot coexist with un-scoped third-party state access.
2. **Event spoofing → indirect actuation**: the deterministic engine's integrity assumes log integrity; an in-boundary publisher forges the log's inputs. The floor is only as sound as the boundary that feeds it.
3. **Own-device actuation** is definitionally the adapter's job — not a puncture per se, but it means "plugin" and "actuator driver" are the same word at this seam.
4. **Confirmation forgery — the deepest cut**: `ConfirmationPolicy` × `Expectation` is expressed in attribute-report terms; a malicious in-boundary adapter fabricates the reports that confirm its own actuations. **The measured `confirmed|unconfirmed` moat — the thing branch C sells — is itself hostage to the trust boundary.** The verdict corpus is only evidence while contributions to the actuation path are curated or isolated-and-attested.

### §1.3 What the field's incidents actually cost — dated

- **Home Assistant, January 2021** [★VERIFIED — home-assistant.io/blog/2021/01/23/security-disclosure2/, access 2026-08-31 UTC; corroborated by DOSSIER HA-4/HA-5 (disclosure-1, 2021-01-22, fetched 2026-07-02)]: directory traversal in HACS (fixed 1.10.1), Font Awesome (1.3.1), BWAlarm (1.12.9), Simple Icons (1.11.0) — "allows an attacker to access any file without having to log in. This access includes any credentials that you might have stored." Cost: emergency Core 2021.1.5 with path-traversal shields *around third-party code*; Nabu Casa blocked vulnerable instances from Cloud; companion apps pushed insecurity warnings; the custom-integration `version` manifest key was retrofitted "in light of these incidents" and made mandatory from 2021.6 so insecure versions could be identified and blocked. Policy line minted under pressure: "Custom integrations are not created and/or maintained by Home Assistant. Users install them at their own risk."
- **SmartThings, May 2016** [★VERIFIED — iotsecurity.engin.umich.edu project page, access 2026-08-31 UTC]: Fernandes/Jung/Prakash, IEEE S&P 2016 (Distinguished Practical Paper): static analysis of **499 SmartApps + 132 device handlers**; "coarse-grained capabilities lead to over 55% of existing SmartApps to be overprivileged"; 42% overprivileged via coarse SmartApp–SmartDevice binding; four working exploits including "secretly planted door lock codes" and a fake fire alarm. Cost: national-press reputational damage on the exact axis (the platform's plugin model), and the eventual architectural exit was the Groovy→Edge migration whose execution became the field's canonical ecosystem-breaker (38-month arc, kill-date-before-parity [DOSSIER ST-1..8, L-12]).
- **Zigbee2MQTT** [DOSSIER Z2M-6/Z2M-11, fetched 2026-07-02]: the recommended unsupported-device path was arbitrary JS in the coordinator process — docs' own words: "malicious or buggy code can compromise the entire Zigbee2MQTT instance, and potentially the host system" — default-ON until 2.11.0 (~May 2026) flipped external JS to disabled-by-default for new installs. A decade-scale ecosystem took ~10 years to reach default-off.
- **Obsidian, April 2026** [DOSSIER OB-22, fetched 2026-07-02]: REF6598 weaponized two legitimate plugins inside an attacker-synced vault; the directory itself held. The 2026 relaunch's answer was automated per-version scanning with a public per-plugin scorecard [DOSSIER OB-3/13].
- **Post-2021 HA custom-integration platform-wide disclosures: none found by this instrument** (searches 2026-08-31 UTC surfaced only the 2021 pair). [VERIFIED-by-absence — the places looked: HA blog security tag via search, OpenCVE vendor listing surfaced but not walked (§0.6).]

### §1.4 The verdict, restated in D5 form

The falsifier does not kill the pivot; it **types** it. Plugins-as-data (profiles/converters/blueprints through the staging pipeline) leave the boundary intact and are the field's strongest pattern (L-22). Plugins-as-code are honest only in the postures Doc 18 already ruled: curated `IN_JVM` behind the quality gate (wave-1), non-curated only at rung 4 — and no external sentence claims isolation before the rung enforces (DP-18-B). The deterministic floor stays what it is in every formulation: **missing from the field, not superior to it** — and this return adds: *the floor's own evidence chain (the verdict corpus) presumes the boundary it guards.*

---

## §2 F-2 in detail — the freeze-debt enumeration (charter §1.2)

**The frame [INTERNAL — Doc 18 §3.1/§4; LTD-16/17; OQ-1 ruling]:** the SPI freeze (AMD-54..64) is sunk and is an asset — LTD-17's own text: "The API boundary is the investment; the loading mechanism is swappable." The debt question is what a PUBLIC SDK adds to the frozen set, because everything third parties rely on inherits the ruled deprecation floor: **six release cycles + a Repairs-class automated-migration surface, never below LTD-16's one-major-version minimum** (OQ-1, co-signed 2026-07-03).

| Doc 18 seam | what a public code SDK freezes | needed for data-first wedge? | status today |
|---|---|---|---|
| SPI (restated §3.1) | already frozen — no new debt | not touched (data channel bypasses it) | frozen, documented, fixtures shipped |
| 1 — dynamic loading | loader semantics + LTD-17 amendment + security evaluation | **no** | OQ-2 deliberately unratified |
| 2 — operation registry | operation declaration format | no (unless ops exposed) | reserved-empty permit |
| 3 — event-manifest layering | third-party event-class admission format | **no** | hardcoded first-party aggregation |
| 4 — trust ladder rungs 1–2 | scoping + publish-permission behavior becomes observable contract | **no** (no code inside boundary) | unbuilt; R-4 backlog rows |
| 5 — namespace/identity | `publisher.extension` grammar, collision ruling as UX | **partially** — M9.3 already lands the convention as a design constraint | §3.5 binding on M9.3 (obligation discharged at Lock) |
| 6 — packaging/distribution | manifest format, `version`, compat-range semantics, channel | **no** — data artifacts ride the staging pipeline + registry schemas | nothing built |
| 7 — marketplace floor | the day-one floor becomes public promise | **no** (corpus + bench verdicts are not a marketplace) | floor specified, nothing scheduled pre-months-12–24 |
| AX-7 (Doc 16 OQ2) | component versioning mechanism | only when automation packs open | direction Locked, mechanism deliberately deferred |

**The M-shape [INFERRED — lane estimate; PM prices]:** honest public code SDK = rungs 1–2 + seam 6 + seam 5 activation + docs/example/CI-for-third-party-artifacts before the first external adapter exists — three-to-five milestone-class builds displacing fall MVP work, then six-cycle duty on all of it while pre-1.0 surfaces still want to move (the field moves: Z2M broke majors 15→25 openly [DOSSIER Z2M-3]; VS Code holds a 131,229-extension ecosystem across monthly releases only via the formally gated proposed-API tier [DOSSIER VSC-13/L-10]). **Data-first wedge = M9.3 + D5 schemas already on the path, already constraint-carrying.**

**Verdict: F-2 CONFIRMED against "code SDK now"; the freeze debt would eat the fall. The wedge is not later — its CODE HALF is later.**

---

## §3 The ecosystem census (charter §1.3) — numbers, dated

### §3.1 The censuses

| ecosystem | figure | as-of / access | tag |
|---|---|---|---|
| Home Assistant installs | 675,103 → 673,433 "Active Home Assistant Installations" (opt-in analytics; "less than a fourth of all Home Assistant users opt in"); "535,309 of 673,433 (79.49%) installations have chosen to share their used integrations" | access 2026-08-31 UTC (live counter; two fetches minutes apart) | ★[VERIFIED] |
| Home Assistant scale (project) | "from 1 million to over 2 million active installations in 2024"; "21,000+ unique contributors in 2024"; foundation "owns and governs over 240 open standards, drivers, and libraries"; 56 FTE across Open Home projects | blog 2025-04-16; access 2026-08-31 UTC | [VERIFIED] |
| HA core repo | 88k stars · 37.7k forks · Apache-2.0 (contributor total not exposed — §0.6.2) | access 2026-08-31 UTC | [VERIFIED] |
| HA core integration count | ~3,000 | secondary blogs only; official index states no total (re-checked this lane) | [REPORTED — UNVERIFIED, both 2026-07-02 and now] |
| HACS | default integration list ≥2,000 entries (floor; truncated — §0.6.7); official language "hundreds of community-made integrations, cards, themes"; HACS "passed 5,000 stars"; started 2019; OHF collaboration | list access 2026-08-31 UTC; blog 2024-08-21 | [VERIFIED floor] |
| Zigbee2MQTT | 5,473 devices from 577 vendors; ~200 device PRs merged June 2026; bus-factor ~1.5 (Koenkk "in my spare time," 142 sponsors) | fetched 2026-07-02 | [DOSSIER] |
| SmartThings Edge | community-buildable Lua drivers, Apache-2.0 stock repo; repo 343 stars / 554 forks; contributors ≥100 (API floor — §0.6.3) with the top five ALL first-party staff by contribution count (greens 1,171; dljsjr 395; cjswedes 316; ctowns 294; hcarter-775 228); announced 2021-08-19; channels are invitation-URL, version-locked — no public registry to census | access 2026-08-31 UTC; announce date per Samsung dev blog | [VERIFIED] |
| Hubitat | HPM repositories.json: **281 repository entries** (282 sources incl. HPM itself); HPM is community-built by one volunteer; Groovy sandbox (no custom classes/JARs, whitelisted imports) | access 2026-08-31 UTC; mechanics [DOSSIER HUB-1..4] | [VERIFIED count] |
| Homey | vendor: "Explore 1,200+ apps," "over 70,000 devices from 2,000+ brands"; community scrape: "only 4860 drivers in total across all apps" (smarthomesven, 2025-12-31); developer-count and install-counts are private to Athom ("accessible only to app creators") | vendor page access 2026-08-31 UTC; forum figures 2025-12-30..2026-01-01 | [VERIFIED vendor claim + REPORTED community scrape] |
| Homebridge | 5,542 npm keyword packages, 602 Verified (~11%); child bridges = subprocess isolation as pure configuration | fetched 2026-07-02 | [DOSSIER] |
| openHAB | 37 maintainers (2023) vs 400+ technologies; five-era marketplace arc incl. the Eclipse-marketplace death-by-host and a two-year no-marketplace gap | fetched 2026-07-02 | [DOSSIER] |
| Node-RED | 6,065 nodes; scorecard "chose not to act as gatekeepers"; deprecated-badges added 2025-07-29 to route around dead modules | fetched 2026-07-02 | [DOSSIER] |
| Obsidian / VS Code (best-in-class comparators) | 5,317 plugins / 131,229 extensions; Obsidian's 2,300-submission manual-review backlog → automated per-version scanning | fetched 2026-07-02 | [DOSSIER] |

### §3.2 What motivates the first ~20 contributors — qualitative, quoted [the honest answer: no platform publishes a first-20 study; these are the founders'/maintainers' own words]

- HACS exists because authors "didn't have the time to meet Home Assistant's requirements" or wanted "something not allowed by Home Assistant, like web scraping" — and HACS itself should "remain an optional addition… at the cost of stability" (ludeeus, official HA blog) [DOSSIER HA-21].
- openHAB's Z-Wave DB: "producing the XML files takes some knowledge. Therefore, maintaining the database is often left to a small group of people" — the fix was a web form, not an SDK [INTERNAL — LB return §Q-1, primary opened 2026-08-01].
- Koenkk maintains Z2M "in my spare time"; HPM was "created by Dominic Meglio" — one user; webCoRE's authors were SmartThings users first [DOSSIER Z2M-14, HUB-3, ST-7/8].
- **Synthesis [INFERRED]:** first contributors are users with an unsupported device and enough fluency to fix it, arriving through the lowest-friction lane the platform offers (a web form beats a converter file beats an SDK). **Contribution follows installed base and device pain; it does not precede them.** The bench + profile corpus is precisely a "my device" lane; a bare SDK is not.

### §3.3 Time-to-first-plugin — proxies only (deviation §0.4.2)

Not cleanly derivable for any platform with this instrument. Documented proxies: openHAB's 2017 marketplace launched because "the queue for binding PRs is still too long" — community supply preceded and forced the infrastructure [DOSSIER OH-3]; HACS arose in 2019, years into HA's life, formalizing an existing custom_components practice; SmartThings Edge community channels appeared alongside the 2021-08-19 announcement via invitation URLs (no public first-driver timestamp exists to cite). What the proxies evidence: **demand-led ecosystems grow their distribution after contribution starts, not before** — infrastructure-first launches have no surveyed success case among these platforms.

### §3.4 Moderation/safety burden on a solo founder

Manual review does not scale and its failure mode is a backlog that silently un-reviews the ecosystem (Obsidian: "we struggled to keep pace with submissions, and subsequent versions were not reviewed" — 2,300 deep before the automated relaunch) [DOSSIER OB-13, L-21]. Z2M's ~200 merges/June-2026 ride on thin, personal review ("No reviews" on a sampled merged PR) [DOSSIER Z2M-9/10]. HA's honest ceiling: "does not review, security audit, maintain, or support" custom integrations [DOSSIER HA-1]. Hubitat outsourced its whole distribution layer to one volunteer [DOSSIER HUB-3]. **Doc 18 row 7 already prices this correctly: the day-one marketplace floor is automated per-version scanning + revocation-that-reaches-clients — and until that floor can be BUILT, the only solo-founder-survivable intake is the staging-area data pipeline, whose review object is a diffable data artifact, not code (L-22, L-32).** [INTERNAL + DOSSIER]

---

## §4 The wedge comparison (charter §1.4)

**A — plugin-SDK-first.** Its honest launch sentences are real (§6-A) but structurally weak: the newsworthy one is an absence ("no sandbox yet"), the strong ones (frozen contract, boots-empty CI) are invisible to non-developers, and S-2 says the audience it recruits does not exist pre-installed-base. It carries both falsifiers. Its genuine core — community device breadth — is fully served by the data channel. **[INFERRED verdict: fold its data half into C; schedule its code half at rung 4/marketplace time as Doc 18 already sequences.]**

**B — explainability-hero-first.** The incumbent of record: v1.1 P3 gates B-6 community presence on "the explain surface is the demo" at R-10, and the register's field-language sentence (RS-3 §6.1-1) is already minted in scaffold with its 09-02 refutability date. It compounds under model progress (projections over the log are model-agnostic; better models raise the value of being able to check them). What it is NOT: a contribution lane — a demo recruits watchers, not contributors. **[INFERRED verdict: keep as the demo surface; it is the wedge's FACE, not its intake.]**

**C — verification/bench-as-product.** Mints honest sentences soonest — C-001/C-002 are scheduled to go LIVE on the R-4 record (Monday-night fill-in per the register scaffold) before any wedge exists, and every subsequent corpus entry is a new dated, commit-hashed, refutable sentence *by construction*. It is the only branch whose community act produces register rows as a side effect. Thesis test: strongest — the verdict corpus is the accountability layer's evidence base, it grows with every device and survives every model swap (the Broadcom-analog property). Falsifier exposure: none new, WITH the §1.2.4 caveat now on record — the corpus's integrity presumes the trust boundary, so corpus contributions stay DATA and bench execution stays first-party/attested. **[INFERRED verdict: the wedge. Its plugin story: "the community extends the home's device reality as data; every extension ships with a measured verdict."]**

**What this return does NOT do:** amend v1.1 (P3/B-6 stands until Nick's word at the beat), set any date, or draft any public sentence for use. The convergence finding is an input to the beat, not a ruling.

---

## §5 The MHS adjacency (charter §1.5)

**The borrowed-vocabulary rule, discharged first:** the adjacent bodies were read before any vacuum claim — Doc 18 §3.4 (AI-authored components are marketplace artifacts, no bypassed gate; L-33), D5 (data-first channel), the MHS datum + its 2026-08-28 addendum (hub-corrected at the primaries), WMARKET2 §M (audited ACCEPT), v58 A-4, and the LB return. **There is no vocabulary vacuum: "plugin" already has a three-rung meaning ladder in our own corpus.** This return only orders it:

1. **Device-class adapters as DATA — now.** Profiles/converters through the staging pipeline into the M9.3-governed registry. This is the wedge's intake (§4-C) and MHS does not change it.
2. **Automation packs — at AX-7's mechanism.** Blueprints-class declarative components, versioned per DP-18-A (semver + compat range + forward-only migration + the six-cycle floor). Opens when Doc 16 OQ2 resolves at a real SDK/marketplace milestone — not before.
3. **Agent-facing extensions — at the MHS/MCP tripwires.** The addendum's ruling stands: MHS enforces the DEVICE envelope ("device-declared bounds, interlocks, and emergency stops at the hardware interface, independent of the model") and defers the cross-device layer — *the floor ABOVE the device is missing from MHS as announced, and MHS says so.* The posture is ADOPT-AND-SIT-ABOVE: agents talk TO the harness, never around it; the MHS/MCP-facing surface is INTEGRATION-CLASS-LATER, and the R-10 EXTERNAL-AGENT INTERFACE POSTURE row owns it. Tripwires unchanged: the open-source release · "mhs" commits in LeRobot / strands-labs/robots · raspberrypi.com news · any OHF/HA MHS integration. **The waitlist ruling (WATCH, do not submit) is not disturbed by anything found this lane.**

**Does MHS change what "plugin" should MEAN? [INFERRED]** It adds gravity to meaning-3 without advancing its date: in a world where actuation plumbing standardizes, the scarce plugin class is the one that extends the ENFORCED surface (new invariant packs, new confirmation policies, new explanation projections) rather than the connectivity surface — and every one of those lives inside the trust boundary, i.e., lands BEHIND the ladder, first-party or curated, per F-1. The community-facing plugin meaning this fall therefore stays meaning-1 (data), with meaning-3 as the R-10 posture question it already is. One watch-item to add at the beat [INFERRED]: **if MHS's open-sourced spec grows a driver-manifest format for homes, our profile/IR schema should be trivially mappable to it** — a data-shape hedge, not a build.

---

## §6 Register readiness (charter §1.6) — the sentences each branch could honestly mint at wedge-launch

**Law: these are DRAFTS for the beat's eyes. Nothing here is public, nothing lifts without a lifting WU's audited return (H9), every enforcement sentence is in D5 layered form, and every sentence carries its refutable-by shape as the register requires. Placeholder ⟨sha⟩/⟨date⟩ resolve at mint.**

**Branch A — plugin-SDK-first (honest, and visibly thin):**
- A-s1: "The integration contract third-party adapters build against has been frozen since ⟨SPI-freeze date/AMD range⟩ and is published with test fixtures; HomeSynapse Core boots and passes CI with the third-party extension set empty (EXT-INV-1, register §52), verified at commit ⟨sha⟩." — *refutable-by:* a demonstrated core feature load-bearing on an extension at the named commit, or a boots-empty CI failure.
- A-s2: "Third-party code runs in-process and unsandboxed today; isolation rungs are named and ordered, and each will be claimed only once it enforces." — *refutable-by:* any external NexSys surface using sandbox/isolation language before the enforcing rung ships (DP-18-B's own tripwire, self-applied).
- A-s3: "Community-contributed content is never paywalled; the repository stays free and sideloadable (DP-18-C)." — *refutable-by:* any paid gate on community-tier access.
- *The register-readiness verdict: honest but the load-bearing sentence is an absence; fails the "wedge that cannot produce honest sentences is marketing air" test only barely, and fails the 'story' test outright.* [INFERRED]

**Branch B — explainability-hero-first (ready, already field-fenced):**
- B-s1 (field half, existing register preamble sentence 1, RS-3 §6.1-1, dated 2026-08-28): stands as written — HA 2026.9 answers "why did it fire" from its logbook; it records no reason for a legitimate non-fire, no confirmation verdict, no command that produced no state change, and the chain rides a self-purging store. — *refutable-by:* the 09-02 HA release (date-armored in the register).
- B-s2: "At commit ⟨sha⟩, HomeSynapse answers why-did-it-fire, why-didn't-it-fire, and did-it-actually-confirm from a never-evicted projection of the event log; the answer is reproducible from the log alone." — *refutable-by:* a reproduction attempt on the named commit + log artifact failing to regenerate the shown explanation. Scope fence: one bench, six devices; NOT a fleet/multi-home claim; NOT a comparison beyond B-s1's dated field sentence.

**Branch C — verification/bench-as-product (soonest, and self-renewing):**
- C-s1: C-001/C-002 verbatim as scaffolded — "verified on real hardware at commit ⟨NICK'S-R-3b-SHA⟩ …" — minting on the R-4 record independent of any wedge decision. — *refutable-by:* reproduction on the named commit + artifact failing the four criteria (as scaffolded).
- C-s2 (the corpus sentence, mints per-entry): "Device profile ⟨publisher.profile⟩ was admitted as declarative data through the staging pipeline and measured on the bench at commit ⟨sha⟩ on ⟨date⟩: its actuation verdicts were ⟨n⟩ confirmed, ⟨m⟩ unconfirmed; unconfirmed is published as unconfirmed." — *refutable-by:* re-running the named commit + profile against the named bench artifact and obtaining materially different verdicts; or a corpus entry found carrying third-party executable code. Scope fence: the verdict binds the named hardware + commit + bench, not the device class at large; the four-qualifier law (hardware · environment count · obstruction definition · training regime) applies to any sensing-adjacent row.
- C-s3 (the boundary sentence, D5 form): "Community contributions enter as reviewable data artifacts; no community code executes inside the enforcement boundary. The deterministic floor this preserves is missing from the field, not superior to it — L2/L3 without L1 are unsound; L1 without L2 is insufficient." — *refutable-by:* any community artifact in the corpus that executes in-process; any NexSys surface restating the floor as superior.

---

## §7 Provenance & source census

**Fresh this lane (all access 2026-08-30 evening CT = 2026-08-31 01:10–02:20 UTC):**

| # | source | what it evidences | mark |
|---|---|---|---|
| 1 | home-assistant.io/blog/2021/01/23/security-disclosure2/ | the 4 vulnerable custom integrations; traversal quote; response measures; at-your-own-risk policy line | ★ |
| 2 | iotsecurity.engin.umich.edu/security-analysis-of-emerging-smart-home-applications/ | 499 SmartApps/132 handlers; "over 55%" overprivileged; 42% binding overprivilege; four exploits; S&P 2016 award | ★ |
| 3 | analytics.home-assistant.io (+ /integrations) | 675,103/673,433 active opt-in installs; 79.49% integration-sharing; "less than a fourth… opt in" | ★ |
| 4 | home-assistant.io/blog/2025/04/16/state-of-the-open-home-recap/ | 2M installs 2024; 21,000+ contributors 2024; 240+ governed projects; 56 FTE | |
| 5 | home-assistant.io/blog/2024/08/21/hacs-… | HACS 2019 origin; "hundreds of…"; 5,000 stars | |
| 6 | raw.githubusercontent.com/hacs/default/master/integration | ≥2,000 default-store integration entries (truncated floor) | |
| 7 | github.com/home-assistant/core | 88k stars / 37.7k forks / Apache-2.0 | |
| 8 | github.com/SmartThingsCommunity/SmartThingsEdgeDrivers (+ api contributors) | 343★/554 forks; Apache-2.0; Lua local drivers; ≥100 contributors, top-5 first-party | |
| 9 | raw.githubusercontent.com/HubitatCommunity/hubitat-packagerepositories/master/repositories.json | 281 HPM repositories | |
| 10 | homey.app/en-us/features/apps/ | "1,200+ apps"; "over 70,000 devices from 2,000+ brands" (vendor claims) | ★ |
| 11 | community.homey.app/t/homey-app-store-statistics-2025-recap/148165 | "4860 drivers in total" (2025-12-31); install data private to Athom; scrape project + monthly syncs | |
| 12 | developer.samsung.com/smartthings/blog/…/2021/08/19/new-smartthings-edge… (via search) | Edge announcement date 2021-08-19 | |
| — | searches (7): HA custom-integration security 2025–26 · Fernandes 2016 · HACS default count · Homey app store 2026 · SOH 2026 · HA integrations count 2026 · ST Edge beta 2021 | discovery only; no claim rests on a search snippet | |

**Internal corpus read at host this lane (pointers, not copies):** the RS-5 charter · Doc 18 (LOCKED 2026-07-03, whole) · Substrate_Thesis_v0 (whole) · MHS datum + addendum (whole) · strategy v1.1 strategy-of-record (targeted: §3.6/E-1, phase map, do-not list, leverage doctrine) · claim-register.md (whole) · plugin-ecosystem-wars dossier (head, §1.1–1.6 extracts, L-1..L-33 ledger) · extensibility PM assessment (whole) · LB return (header + §0 + §1.1 + Q-1 extract) · RS-4 return (header + §0 head, as the format/verdict precedent) · v58 findings (A-4 line).

**Write-isolation statement:** this file is the lane's only write into any repo. No `git` command was run by this lane against any repository. No file outside `context/research/` was created or modified. The hub owns commit and intake.

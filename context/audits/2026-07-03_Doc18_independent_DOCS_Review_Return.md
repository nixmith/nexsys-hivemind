<!--
file: context/audits/2026-07-03_Doc18_independent_DOCS_Review_Return.md
purpose: Independent DOCS-Project second-opinion review of the Doc 18 "Extension & Plugin Architecture" DRAFT (pre-Lock), run by a fresh context-isolated Cowork reviewer per the Doc 15/16/17 discipline. Charter-fidelity verification (incl. the two deliberate charter-citation corrections, each adjudicated FROM SOURCE), EXT-INV-1/2 minting-test verdicts, source-resolution of every cited id and core-source claim, rulings-fidelity of the four SETTLED decisions, per-row non-preclusion. REVIEW ONLY — the doc was not edited; the hub folds this return after its two-layer audit.
audience: the v16 PM hub (folds); Nick (co-sign + Lock).
state-type: audit return (independent design-doc review).
status: RETURNED 2026-07-03.
baseline: docs HEAD 78e0c5c ("Doc 18 DRAFT, pre-review") atop 1509b34 — see Preflight note (baseline shift from the brief's stated 1509b34+untracked-doc; benign). hivemind HEAD c54a058 (v16 beat 62). Reviewed the DRAFT as it stands on disk == docs 78e0c5c.
verdict: RATIFY-WITH-EDITS (1 BLOCKING-for-Lock edit; the remainder NON-BLOCKING). The doc is charter-faithful, both corrections are RIGHT from source, every cited id and core-source claim resolves, all four rulings are restated faithfully, all seven seams are non-precluding, and all six anti-requirements hold. The single BLOCKING item is additive and STRENGTHENS the mints rather than overturning them.
-->

# Independent DOCS Review — Doc 18 "Extension & Plugin Architecture" DRAFT (pre-Lock)

**Reviewer:** fresh context-isolated Cowork conversation, nexsys-project-manager skill, Mode-1 review discipline (`references/review-and-quality.md` §1 + `constraint-enforcement.md`).
**Document under review:** `homesynapse-core-docs/design/18-extension-and-plugin-architecture.md` (DRAFT 2026-07-03, at docs `78e0c5c`).
**Method:** every load-bearing claim was resolved against primary source — the governance registers, the ratified AMDs, and the `homesynapse-core` source tree — never against a summary or either party's assertion. The PM skill's own at-a-glance LTD table was found to be a lossy summary and was NOT trusted (see §1(a)).

---

## Preflight & baseline (light, per the brief)

- **Env-model read FIRST.** Host file tools treated as truth throughout; all git state read lock-free (`git --no-optional-locks status --porcelain` / `log`); zero `git add` (incl. `--dry-run`); no VM-side "fix" attempted. No truncated-tail phantom encountered on host reads.
- **Baseline shift (benign, noted per pre-authorization).** The brief's masthead described the doc as an *untracked* working-tree file atop docs `1509b34`. As of this session the DRAFT is **committed** at docs HEAD `78e0c5c` ("Doc 18 - Extension & Plugin Architecture (DRAFT, pre-review)"), parent `1509b34`, landed as part of the v16 beat-62 fleet sweep. This is a *different* shift than the anticipated "Commit A lands" (the pending **website/**-only Commit A is still dirty in the porcelain — 26-path `website/site/…`, disjoint from `design/` and from every read in this review). The doc's *content* is identical whether tracked or untracked; it was reviewed as it stands on disk. Re-verified nothing; noting it here as instructed.
- **Hivemind masthead beat:** c54a058 = v16 beat 62. pm-handoff top entry = beat 62; beat 61 = Doc 18 authored (DRAFT); beat 57 = the DP-B/DP-18-A/B/C rulings. Grounding via `git log` + pm-handoff beats (snapshot is grounding-only; not fully re-read — adequate for an independent review).
- **Write isolation:** this return is the session's ONLY new file. See the env-model §10 pre-commit audit at the end.

---

## Part 1 — Charter fidelity + the two corrections (the headline)

### 1.0 Section-by-section coverage — COMPLETE

Charter (`nexsys-hivemind/context/planning/2026-07-02_Doc-18_requirements-charter.md`) §1 section map → doc §§0–7: every required section is present and substantively covered.

| Charter §1 row | Doc 18 location | Coverage |
|---|---|---|
| Header + Lock provenance | Header + "Lock provenance (pending)" block | ✓ |
| §0 Scoping decision (center-of-gravity; fold-into-Doc-05 alternative rejected) | §0 | ✓ (alternative-considered present) |
| §0.1 OWNS / RESTATES / COORDINATES-WITH | §0.1 | ✓ |
| §1 Purpose (additive activation; never a Groovy→Edge forced migration) | §1 | ✓ |
| §2 Design principles (five + honesty) | §2 (five + DP-18-C standing constraint) | ✓ |
| §3 Architecture as one direction + AI-authoring surface | §3 (§3.1–3.5) | ✓ |
| §4 Reserved seams table (seven, RESTATES tagged) | §4 (7 rows) | ✓ |
| §5 Boundaries OUT | §5 | ✓ |
| §6 Invariants (mint 1–2; keep 3–5) | §6 | ✓ |
| §7 Open questions / decision points | §7 | ✓ |

Charter §3 seven seams → doc §4 rows 1–7: 1:1, in order. Charter §5 OUT list → doc §5: complete (loader/SDK/registry/marketplace/store; AX-7 unresolved; SPI not redesigned; no payments/hosting; no sandbox claims beyond built; no ladder-rung implementation; D5 pipeline / M9.3 registry design / Matter-bridge / federation / website surface all disclaimed; mints at most EXT-INV-1/2). **Charter fidelity: PASS.**

**Positive refinement noted:** the doc's EXT-INV-1 novelty clause is *stronger* than the charter's. The charter (§2) said the parents "bind runtime failure and network direction; none binds the dependency direction for the third-party actor class." The doc narrows this to "…and compile-time dependency direction (LTD-17); none binds the **load-bearing-ness** of the third-party actor class as such." This is the correct sharpening — it distinguishes EXT-INV-1 from LTD-17 (which already binds the static build graph), which the charter's looser "dependency direction" did not.

### 1.1 Correction (a) — EXT-INV-1's static-composition parent: charter "DECIDE-04/LTD-16" → doc "LTD-17" — **RULED RIGHT (from source)**

The charter §2 verbatim cited EXT-INV-1's static-composition parent as **"DECIDE-04/LTD-16 (static composition)."** The doc corrects this to **LTD-17**. Adjudicated against `governance/HomeSynapse_Core_Locked_Decisions.md`:

- **LTD-17** (§9, register lines 664–712) = "In-Process Compiled Integrations with Enforced API Boundary": "No dynamic JAR loading, no classloader isolation… The Integration API boundary is enforced at build time." **This IS static composition.** The doc's two verbatim quotes are confirmed present: *"The API boundary is the investment; the loading mechanism is swappable"* (line 697) and *"Dynamic JAR loading may be added when community integrations become a real requirement"* (line 700). → Citing **LTD-17** for static composition is **RIGHT**.
- **LTD-16** (register lines 614–658) = "Semantic Versioning with URL-Versioned REST API" — semver, additive-only within major, **one-major-version deprecation window**, and (line 648) **"Integration API versioned independently (INV-CS-04)."** LTD-16 is *not* static composition; it is the versioning/deprecation decision. So the charter's "LTD-16 → static composition" was **WRONG**, and the doc's use of "LTD-16 / INV-CS-04" for independent integration-API versioning (§3.1, §4 row 6) and "LTD-16's one-major-version floor" (DP-18-A) is itself **CORRECT** (line 646). Register cross-links corroborate: line 828 "LTD-16 (API) ── governs LTD-17 (Integration API versioning)."
- **DECIDE-04** — grep of the entire `governance/` tree returns **zero** matches. DECIDE-04 lives as a *source-code decision tag* in `IntegrationFactory.java` javadoc (lines 19–23, "DECIDE-04 (2026-03-20): Direct construction was chosen over ServiceLoader discovery") and in the PM skill's paraphrase — **not** as a governance-register id. The doc's parenthetical "'DECIDE-04' resolves to nothing in `governance/`" is **precisely and verifiably CORRECT.**

**Note (mild):** the register's LTD-17 §9 does not spell "DECIDE-04" either; the ServiceLoader ban is worded in-line. The PM skill's constraint-enforcement at-a-glance table (which lists LTD-16 as "REST (Javalin)+WebSocket" and folds "DECIDE-04" into LTD-17) is a lossy summary — it was correctly disregarded in favor of the register. This is exactly the "read the actual source, not a summary" discipline the correction demands.

### 1.2 Correction (b) — EXT-INV-2's parent: charter "AMD-56 error-code registry discipline" → doc "descriptor freeze + AMD-55-INV-01" — **RULED RIGHT in substance (from source), one imprecision flagged**

The charter §2 verbatim cited EXT-INV-2's parent as **"AMD-56 error-code registry discipline."** The doc replaces it with **"the descriptor freeze itself + AMD-55-INV-01."** Adjudicated against the ratified AMDs:

- **AMD-56** (`design/amendments/AMD-56_Exception_Classification_Auth_Failed.md`) = adds `AUTH_FAILED` to the `ExceptionClassification` enum + a code-bearing `PermanentIntegrationException` constructor pair. It is **exception classification for a single failure mode**, not an "error-code registry discipline," and has nothing to do with declared-capability surface. The charter's citation was **doubly wrong** (wrong subject *and* wrong topic). Rejecting AMD-56 as EXT-INV-2's parent is **RIGHT**.
- **The descriptor freeze** (`IntegrationDescriptor`, AMD-54..64) IS the declared-capability surface (requiredServices, dataPaths, configSchemaMajor/Minor, isolationLevel — source-verified, see Part 3). Installing it as EXT-INV-2's primary parent is **RIGHT**.
- **AMD-55-INV-01** (`AMD-55` §7, line 104) as registered reads: *"all four hooks are `default`; a pre-AMD-55 adapter remains source- and binary-compatible, with behavior identical to today."* This is the **default-method backward-compatibility** invariant. The doc glosses it as "lifecycle-hook surface discipline on the same freeze." That gloss is *loose* — but it is **defensible**, because AMD-55 §2.4 makes the connection to declared-capability explicit: "defaults never silently claim a capability the adapter does not have… the `UNSUPPORTED` reauth default tells the supervisor, truthfully, that no reauth path exists." So AMD-55-INV-01 does bear on "capability declared, not discovered." → correction (b) is **RIGHT in substance**; the *characterization* of AMD-55-INV-01 is a **NON-BLOCKING** precision item (see edit N-1).

**Both corrections are RIGHT from source, and the doc faithfully represents the charter's original (erroneous) citations** — the charter §2 text was read directly and matches what the doc's §6 note attributes to it.

---

## Part 2 — EXT-INV-1/2 under the minting test; the three principles re-checked

**The test (doc §6, per the register + the INV-GA-02 near-duplicate warning, Doc-17 Lock precedent):** a candidate is minted only if it **adds a constraint its cited parents do not already impose**, **cites those parents**, and is **CI-testable**.

### EXT-INV-1 — Core Never Depends on Third-Party Extensions → **MINT AT LOCK, conditional on completing the near-duplicate analysis (edit B-1)**
- **Adds a novel constraint:** YES. Cited parents (INV-RF-01 crash isolation, INV-LF-02 network direction, LTD-17 compile-time dependency direction) bind failure propagation, outbound-network direction, and the static build graph respectively; none binds "no core feature may take a *load-bearing* dependency on an extension." A statically-compiled, crash-isolated extension could still become load-bearing. Genuine novelty. ✓
- **CI-testable now:** YES — "the composition root builds and boots with zero non-first-party integrations; the M9.1 fake-adapter path already approximates the harness." Credible. ✓
- **Gap:** the parent set **omits INV-CE-05 "Extension Model with Stability Guarantees"** (register §8, lines 528–530) — the single most on-point existing invariant for an extension doc, which already enumerates "isolated execution (INV-RF-01), resource quotas (INV-RF-02), independent version pinning, and graceful degradation when an extension fails." The mint SURVIVES against INV-CE-05 (CE-05 binds the extension→core *stability/isolation/degradation* relationship; it does **not** bind core's *independence from* extensions — the reverse direction). But per the INV-GA-02 near-duplicate discipline the test explicitly invokes, the closest existing invariant must be named and distinguished. → **BLOCKING-for-Lock edit B-1.**

### EXT-INV-2 — Extension Capability Is Declared, Not Discovered → **MINT AT LOCK, conditional on B-1 + a CI-testability note (edit B-1 + N-2)**
- **Adds a novel constraint:** YES, but narrower than the doc implies. Cited parents (IntegrationDescriptor freeze, M3.6c manifests, AMD-55-INV-01) establish the declared descriptor surface; "nothing binds the third-party actor class to declared-capability-only — today a full `EventPublisher` is injected and the permitted-publish-types check is unbuilt" (source-verified, Part 3). ✓
- **CI-testable:** PARTIAL — "CI-testable **when rung 2 lands**." The *declaration + before-load validation* half is testable now (the descriptor is validated pre-load); the *"no undeclared runtime capability"* half needs the permitted-publish-types enforcement (rung 2). This is a weaker CI-testability posture than EXT-INV-1, and it is the *same* deferral that keeps kept-principle (b) unminted. Defensible because a testable declaration-core exists now, but Nick should confirm at co-sign. → **NON-BLOCKING edit N-2.**
- **Gap:** the parent set **omits INV-SE-04 "Least Privilege for Integrations"** (register §10, line 607): *"The permission model must be explicit (declared in the integration manifest) and enforceable (the runtime denies unauthorized access)."* This is a close cousin — but EXT-INV-2 is **orthogonal**, not a duplicate: SE-04 governs *least privilege* (an integration may not exceed granted permissions); EXT-INV-2 governs *static-declaration completeness* (the full surface is static manifest data, nothing discovered/registered at runtime). An extension can satisfy one and violate the other. The mint SURVIVES, but SE-04 must be named and distinguished (add as a parent + articulate the orthogonality). → **BLOCKING-for-Lock edit B-1.**

### The three kept-as-principles — re-checked, all CORRECTLY kept
- **(a) "The frozen SPI is the plugin contract, additive-only"** — correctly UNMINTED. Fully carried by the AMD-54..64 freeze + AMD-55-INV-01 + LTD-16/INV-CS-04; minting would create the droppable near-duplicate INV-GA-02 warns against. This is the near-duplicate discipline done RIGHT — and it is precisely why the *omission* of INV-CE-05/INV-SE-04 from the EXT-INV-1/2 analyses (B-1) is a genuine inconsistency: the doc applies the near-duplicate check rigorously to principle (a) but not to its own two mints.
- **(b) "Trust is tiered, never binary"** — correctly UNMINTED. No enforceable content until ladder rungs are built (IN_JVM only today); the AIOT-INV-2/3 "kept-until-enforceable" precedent applies exactly. ✓
- **(c) "Data-first extensibility"** — correctly UNMINTED. Owned by D5's 2026-06-25 ruling; this doc restates, does not own. ✓
- **Is any minted candidate actually a near-duplicate (the INV-GA-02 warning)?** No — EXT-INV-1 (core-independence) and EXT-INV-2 (declaration-completeness) are each distinct from their closest existing neighbors (INV-CE-05, INV-SE-04). But the doc must *show* that distinction (B-1), because an unaddressed near-neighbor is the exact failure mode INV-GA-02 exists to prevent, and permanent ids cannot be cleanly retrofitted after Lock.

---

## Part 3 — Full citation table (source-resolved)

### 3a. Governance ids — every id the doc cites, resolved against the registers

| Cited id | Doc's claimed meaning | Source resolution | Verdict |
|---|---|---|---|
| LTD-16 | semver / independent integration-API versioning / one-major deprecation floor | Locked_Decisions lines 614–658, 648, 646 — exact | **VERIFIED** |
| LTD-17 | static composition; "loading mechanism swappable"; dynamic loading amendable | Locked_Decisions lines 664–712, 697, 700 — verbatim | **VERIFIED** |
| DECIDE-04 | "resolves to nothing in `governance/`" | zero matches in `governance/`; is a source-javadoc tag (IntegrationFactory.java 19–23) | **VERIFIED** (correct negative) |
| INV-RF-01 | integration crash isolation | register line 264 "Integration Isolation" | **VERIFIED** |
| INV-RF-02 | resource quotas (reserved path) | register line 278 "Resource Quotas for Integrations" | **VERIFIED** |
| INV-LF-02 | no outbound dependence (network direction) | register line 128 "Cloud Enhancement, Never Cloud Dependence" | **VERIFIED** |
| INV-SA-01..04 | Doc 16 automation-safety invariants (sealed model, federation non-preclusion, pure-projection, deterministic degradation) | register lines 1082–1085 / §49 | **VERIFIED** |
| INV-ES-07 | event schema evolution | register line 212 | **VERIFIED** |
| INV-CS-04 | integration API stability | register line 338 | **VERIFIED** |
| INV-CS-06 | deprecation discipline | register line 354 | **VERIFIED** |
| INV-PD-08 | tamper-evident integrity (signing/provenance mandate) | register line 460 | **VERIFIED** |
| INV-GA-02 | invariant identifiers permanent (near-duplicate warning) | register line 807 | **VERIFIED** |
| AIOT-INV-1 | AI proposer-only, never actuator | register line 1086 / §50 | **VERIFIED** |
| AMD-55-INV-01 | (doc: "lifecycle-hook surface discipline") | AMD-55 §7 = default-method backward-compat invariant | **VERIFIED (imprecise gloss — N-1)** |
| AMD-63-INV-01 | RESERVED_SUBPROCESS reserved-until-amendment | register §33 line 1490; AMD-63; IsolationLevel.java | **VERIFIED** |
| AMD-54..64 (freeze) | IntegrationDescriptor descriptor freeze | AMD-54/55/56/59/60/61/62/63/64 confirmed via IntegrationDescriptor.java ctor | **VERIFIED** |
| AMD-93 (DP-18-A "AMD-93-aligned") | forward-only non-destructive migration | AMD-93 file; Doc 16 line 254 AMD-93-INV-01 | **VERIFIED** |

**No MIS-CITED, no ABSENT ids.** (The only near-miss is the AMD-55-INV-01 *characterization*, not the citation — the id resolves and is topically apt; see N-1.)

### 3b. Core-source claims — resolved against `homesynapse-core` (read-only)

| Claim (doc §3.1/§3.2/§3.3/§6) | Source | Verdict |
|---|---|---|
| `IntegrationFactory` → `IntegrationAdapter` are the two third-party-implemented types | integration-api/…/IntegrationFactory.java, IntegrationAdapter.java (interfaces; "each integration module provides exactly one IntegrationFactory") | **VERIFIED** |
| `IntegrationDescriptor` fields: requiredServices, dataPaths, configSchemaMajor/Minor, isolationLevel | IntegrationDescriptor.java record components 111–126 | **VERIFIED** |
| `IsolationLevel.RESERVED_SUBPROCESS` (enum slot; inert until amendment) | IsolationLevel.java { IN_JVM, RESERVED_SUBPROCESS } — "rejects with UnsupportedOperationException… until a future amendment activates it (AMD-63-INV-01)" | **VERIFIED** |
| `InvokeIntegrationAction` reserved-empty | InvokeIntegrationAction.java = `record InvokeIntegrationAction() implements ActionDefinition {}` — "Tier 2, implementation deferred. Requires integration operation registry." | **VERIFIED** |
| `SchemaRegistry.registerIntegrationSchema` built-but-unwired | SchemaRegistry.java declares it; the ONLY call site is `ConfigLayoutTest` (test) — zero production wiring | **VERIFIED** |
| unscoped `EntityRegistry`/`StateQueryService` injected; full `EventPublisher` injected | StandardIntegrationSupervisor.java 1053–1061 passes bare `entityRegistry`/`stateQueryService`/`publisher` (only `configAccess` is scoped via `configAccessFactory.apply(type)`); corroborated by assessment §2 ("unscoped… LTD-17 isolation unenforced; full EventPublisher; permitted-publish-types check unbuilt") | **VERIFIED** |
| type names `EntityRegistry` / `StateQueryService` | IntegrationContext.java imports com.homesynapse.device.EntityRegistry, com.homesynapse.state.StateQueryService — exact | **VERIFIED** (current source; LTD-17's older "DeviceRegistry/StateQuery" prose is stale) |

**Foresight note (F-1, non-blocking, core-source not Doc-18):** the `IntegrationContext.java` javadoc *describes* `entityRegistry`/`stateQueryService` as "integration-scoped… return only entities owned by this integration" and `eventPublisher` as "write-only… may only produce permitted event types" — i.e. it documents the contract as if **enforced**, while the wiring and assessment §2 confirm the *enforcement* (scoped wrappers, permitted-publish-types) is the unbuilt rung. Doc 18's claim ("injected unscoped / full") is the *accurate* one. When ladder rungs 1–2 land, that javadoc should be reconciled; today it mildly over-claims — which is itself an instance of the very honesty rule Doc 18 installs. Flag for the R-4 backlog rows, not a Doc-18 defect.

### 3c. L-n lessons — spot-followed into the dossier (≥5 required; 18 checked)

Followed into `…/2026-07-02_plugin-ecosystem-wars_research-dossier.md` §3 (lines 346–388): **L-1, L-2, L-3, L-4, L-5, L-7, L-8, L-9, L-11, L-12, L-14, L-16, L-23, L-24, L-26, L-27, L-28, L-29, L-30, L-31, L-32, L-33.** The doc's use matches the lesson's actual content in every case, with two trivial gloss-looseness items (neither a mis-citation):
- **L-27** — the doc's one-line gloss ("platforms whose community code became load-bearing could not evolve") leans harder on "load-bearing" than L-27's text ("closed platform + vendor-hosted runtime = zero community leverage"); topically sound (same SmartThings/webCoRE example).
- **§4 row 1 "(L-16; L-9)"** — the "openHAB shipped dynamic modules without dependency resolution" characterization draws on L-16's openHAB pointers (OH-3/8/9) + L-9's compat gate; the exact phrasing traces to the dossier's OH sources, compressed. Acceptable.
- **OQ-1 evidence check (per brief):** the N=6 proposal is directly evidenced — **L-11 = "HA ADR-0021 (≥6 release cycles + Repairs)"** (dossier line 358). "N=6 with a Repairs-class automated-migration surface" is faithful to L-11. ✓

### 3d. §17 uncited-invariant scan — TWO relevant invariants found uncited

| Uncited invariant | Register | Relevance to Doc 18 | Severity |
|---|---|---|---|
| **INV-CE-05 Extension Model with Stability Guarantees** | §8, lines 528–530 | The constitutional home of "the extension model" — the exact subject Doc 18 elaborates; a near-neighbor for EXT-INV-1 | **BLOCKING-for-Lock (B-1)** |
| **INV-SE-04 Least Privilege for Integrations** | §10, line 607 | "permission model explicit (declared in manifest) and enforceable" — a near-neighbor for EXT-INV-2 and the §3.3 ladder | **BLOCKING-for-Lock (B-1)** |
| INV-CS-03 Configuration Schema Stability | §4, line 332 | governs the config-schema seam (§4 row 6 rides SchemaRegistry) | NON-BLOCKING (N-3, optional) |
| INV-CE-04 Protocol Agnosticism in the Device Model | §8, line 522 | bears on §3.5(d) DeviceProfile protocol-scoping | NON-BLOCKING (N-3, optional) |

---

## Part 4 — Rulings-fidelity of the four SETTLED decisions (vs the beat-57 record)

Checked against `pm-handoff.md` beat-57 (lines 97–101, full verbatim rationale) + `decision-rationale-index.md` (beat-57 rows). **All four are restated faithfully, at full strength, with no drift and no silent extension.**

- **DP-B (doc §7.1)** — FAITHFUL. Permanent policy; restart+reinstall-stable pure function of the type string; no identity file to back up/corrupt/crypto-shred; rename = naming-layer problem §3.5 defuses before M9.3 makes anything one-way; M9.3 adoption identity-ungated. All beat-57 elements present.
- **DP-18-A (doc §7.2)** — FAITHFUL. semver on `(componentId, version)` + declared compat range + forward-only non-destructive migration (AMD-93-aligned) + a NAMED deprecation floor; strict whole-definition immutability rejected (L-14). The N=6 floor is correctly carried as **OPEN/OQ-1** (not asserted as ruled) — consistent with beat-57 ("named floor" ruled; N left to co-sign) and the index PENDING row "Deprecation-floor N quantifies at Doc 18 Lock." No drift.
- **DP-18-B (doc §7.3)** — FAITHFUL. wave-1 curated IN_JVM behind the quality gate; RESERVED_SUBPROCESS = the intended non-curated rung at marketplace time (AMD-63 bought the slot); no-sandbox-claims honesty rule as doc text (§2 P3, §3.3). Matches beat-57.
- **DP-18-C (doc §7.4)** — FAITHFUL. RULED (a): community content never paywalled, stated as a **CONSTRAINT** (§2) — correctly reflecting beat-57's "option (c) skipped; the PRINCIPLE is ruled TODAY, so Doc 18 states it as a CONSTRAINT." Monetize trust, not access; Connect reword rides the Lock docs pass; wording polishes at pricing time. No drift.

**Rulings-fidelity: PASS (no divergence to quote).**

---

## Part 5 — Per-row non-preclusion verdicts (§4)

All seven rows are **genuinely non-precluding**; V1 builds none. The three brief-flagged rows in detail:

- **Row 1 (Dynamic loading) — NON-PRECLUDING.** Reserves JPMS child-`ModuleLayer` gated on (a) the **LTD-17** amendment via the recorded process and (b) the security evaluation the `IntegrationFactory` javadoc anticipates (both real: LTD-17 line 700 pre-authorizes; IntegrationFactory.java 19–23 anticipates). The amendment shape is explicitly **"proposed, not assumed"** and marked **OQ-2 NON-BLOCKING** ("ratifies only when a dynamic-loading milestone is actually scheduled"). Static composition remains "the default and the V1 truth." No decision smuggled. ✓ (Anti-requirement "static composition remains V1 truth / amendment proposed not assumed" — HELD.)
- **Row 6 (Packaging & distribution) — NON-PRECLUDING; does NOT over-specify.** Names only the *minimum* artifact primitives — `version` (L-8) + a declared core-compatibility range (L-9) — with "what V1 does: Nothing — no artifact format, no registry." Signing/provenance is correctly **restated** as INV-PD-08's mandate owned by **Doc 17 §4** (verified: Doc 17 §0.1/§4 owns "the SBOM/signed-update/vuln-disclosure seam"); "this row only binds distribution to it." Config schema rides the built-unwired SchemaRegistry. A minimum-floor reservation, not a format spec. ✓
- **Row 7 (Marketplace trust floor) — NON-PRECLUDING; a floor, not a covert spec.** Lists the day-one *floor* (each element tied to L-7/L-18/L-19/L-20/L-21/L-25), explicitly carves out what is NOT in the floor (payments, first-party hosting, continuous audit, sandbox promises), and defers *operationalization* (which scanner, signal format, hosting) to **OQ-3 NON-BLOCKING / the marketplace milestone doc**. The densest row and closest to the line, but the OQ-3 deferral keeps it a floor. ✓

- **Rows 2–5 — NON-PRECLUDING.** Row 2 fills the reserved-empty `InvokeIntegrationAction` as *declared data behind an existing permit* — "sealed hierarchy stays sealed, not a new permit class" (consistent with Doc 16's no-new-sealed-permits discipline). Row 3 generalizes only the aggregation point of the existing M3.6c manifest pattern. Row 4 is the ladder (IN_JVM wave-1, ruled). Row 5 (namespace & identity) actively **constrains M9.3** via §3.5 — but constrains (namespaced keying, fingerprint-priority), does not design; this is the doc's sanctioned Lock-before-M9.3 purpose (assessment R-2), and §5 explicitly disclaims owning "the M9.3 profile-registry design (constrained via §3.5 only)." ✓

**RESTATES-tag hygiene (Doc-17 S1 lesson) — CLEAN.** Every restated item is tagged with its owner and not re-reserved: frozen SPI → Doc 05 + AMD-54..64 (§3.1 "restated, not owned here"); AIOT-INV-1/AI-gate → Doc 17 §3.3 / Doc 16; component model + AX-7 → Doc 16 §3.2/OQ2 ("frames the ruling, does not own the mechanism"); D5 → the 2026-06-25 record; SBOM/signing → Doc 17 §4. No re-reservation drift.

**§3.5 M9.3-binding coherence — PASS.** (a)–(d) are precise enough to constrain M9.3 (namespaced identity keying; bare namespace reserved to first party; collision = consent + UI flag + core brand preference; fingerprint-priority + rebrand mapping; DeviceProfile Zigbee-scoped-with-general-seam-note) without designing M9.3's registry. Matches assessment §3 watchlist-1 + R-2 and L-29/L-30 exactly.

**OQ marks — CORRECT.** OQ-1 BLOCKING-for-Lock (co-sign gate; N=6 evidence-checked to L-11/HA ADR-0021 ✓); OQ-2 NON-BLOCKING (amendment not needed until dynamic loading is scheduled); OQ-3 NON-BLOCKING (marketplace milestone's). No unresolved BLOCKING question that is not escalated with a resolution plan.

**Anti-requirements — ALL SIX HELD.** (1) community content never paywalled as a CONSTRAINT (§2) ✓; (2) no sandbox/isolation claim beyond built — honesty rule as doc text (§2 P3, §3.3, §4 rows 4/7) ✓; (3) builds NOTHING (every row "what V1 does: Nothing"; §5) ✓; (4) frozen SPI restated never redesigned (§3.1, §5) ✓; (5) static composition remains V1 truth, amendment proposed not assumed (§4 row 1, OQ-2) ✓; (6) claim language inside Doc 17 §7-6's counsel-gated boundary (§3.4 "state the mechanism…, never the superlative") ✓ — **and the doc actively SOFTENED the charter's over-claim**: charter §3 said the four-part stack "lets AI-in-automations be *guaranteed safer than the field's*"; the doc drops that superlative and states only "no surveyed platform has all four." Good catch by the author.

**Template compliance — PASS by the Doc-17 readiness-doc precedent.** Doc 18 uses the reduced §0–7 readiness shape identical to Doc 17 (Locked 2026-06-26). The build-oriented mandatory template sections (Data Model, Key Interfaces §8, Configuration §9, Performance §10, Observability §11, Testing §13, Summary-of-Decisions §16) are inapplicable to a builds-nothing reservation doc, exactly as for Doc 17; §7 carries the decisions-with-rationale. Neither Doc 17 nor Doc 18 includes an explicit template-section-exclusion note — so Doc 18 matches precedent (see optional edit N-4).

---

## Part 6 — Document verdict + consolidated edit list

### VERDICT: **RATIFY-WITH-EDITS**

Doc 18 is a strong, disciplined readiness doc: charter-faithful, both charter-citation corrections RIGHT from source, every cited id and every core-source claim source-VERIFIED, all four SETTLED rulings restated faithfully, all seven seams non-precluding, RESTATES tags clean, OQ marks correct, and all six anti-requirements held (with the charter's lone superlative correctly softened). It is **not** RATIFY-TO-LOCK only because of one governance-rigor gap in its central act (minting), and it is **far** from REVISE — the required edit is additive and *strengthens* the mints.

### Edit list (each: location · exact proposed text · reason · severity)

**B-1 [BLOCKING for Lock] — Complete the EXT-INV near-duplicate analysis against the two closest existing invariants.**
- **Location:** §6, EXT-INV-1 and EXT-INV-2 *Parents/Novel* clauses; and the metadata **Dependencies** line (add both ids).
- **Proposed text — EXT-INV-1, append to *Parents*:** "**INV-CE-05** (Extension Model with Stability Guarantees — binds extension isolation, quotas, independent version pinning, and graceful degradation on extension failure)." And append to *Novel*: "INV-CE-05 binds the extension→core relationship (a failing extension degrades gracefully); it does **not** bind core's independence *from* extensions — no clause requires core to boot and pass CI with the extension set empty. That reverse-direction, load-bearing-ness constraint is EXT-INV-1's novel contribution."
- **Proposed text — EXT-INV-2, append to *Parents*:** "**INV-SE-04** (Least Privilege for Integrations — the permission model must be explicit, declared in the manifest, and runtime-enforceable)." And append to *Novel*: "INV-SE-04 binds *least privilege* (an integration may not exceed granted permissions); EXT-INV-2 binds *static-declaration completeness* (the full surface — events, operations, services, config-schema, isolation — is static manifest data validated before load; nothing is discovered or registered at runtime). The two are orthogonal: an extension can satisfy least-privilege while dynamically discovering capability, or declare a complete-but-over-broad surface. EXT-INV-2's completeness-and-before-load constraint is not imposed by INV-SE-04."
- **Reason:** the minting test the doc itself states invokes the INV-GA-02 near-duplicate warning; INV-CE-05 and INV-SE-04 are the two most on-point existing invariants and are currently unaddressed. The doc applies this check rigorously to kept-principle (a) but not to its own two mints. Both mints SURVIVE the check — but because Lock registers *permanent* ids (INV-GA-02: identifiers are permanent, non-reusable), the parent/novelty analysis must be complete and correct *before* registration; it cannot be cleanly retrofitted after. This strengthens, not weakens, the mints.
- **Severity:** BLOCKING for Lock (must fold before the EXT-INV registration in the Lock docs pass). Does **not** change the recommendation (both still MINT).

**N-1 [NON-BLOCKING] — Sharpen the AMD-55-INV-01 characterization.**
- **Location:** §6, EXT-INV-2 *Parents*, and the §6 charter-correction note.
- **Proposed text:** replace "AMD-55-INV-01 (lifecycle-hook surface discipline on the same freeze)" with "AMD-55-INV-01 (default-method backward-compatibility — the lifecycle hooks are `default` so an adapter's *absence* of a capability is truthfully declared, never silently claimed; AMD-55 §2.4)."
- **Reason:** AMD-55-INV-01 as registered (AMD-55 §7) is the default-method backward-compat invariant; the current gloss is loose. The proposed wording ties it accurately to the declared-capability thread (AMD-55 §2.4), preserving the correction's validity.
- **Severity:** NON-BLOCKING.

**N-2 [NON-BLOCKING] — Note EXT-INV-2's deferred enforcement at co-sign.**
- **Location:** §6 EXT-INV-2, and/or OQ-1's co-sign checklist.
- **Proposed text:** append to EXT-INV-2: "(At Lock the CI-testable core is the descriptor's before-load declaration/validation; the *no-undeclared-runtime-capability* half becomes testable when rung 2 lands — Nick confirms at co-sign that a partially-deferred enforcement is acceptable for a mint, or the invariant is scoped to the declaration-validation portion enforceable now.)"
- **Reason:** EXT-INV-2 is only PARTIALLY CI-testable now — the same deferral basis on which kept-principle (b) stays unminted. Making the asymmetry explicit avoids minting a partly-unenforceable invariant by inadvertence.
- **Severity:** NON-BLOCKING (co-sign judgment).

**N-3 [NON-BLOCKING, optional] — Add the two minor on-topic invariants where they bind.**
- **Location:** §4 row 6 (config-schema clause) and §3.5(d).
- **Proposed text:** cite **INV-CS-03** (Configuration Schema Stability) in the row-6 config-schema clause; cite **INV-CE-04** (Protocol Agnosticism in the Device Model) in §3.5(d)'s DeviceProfile protocol-scoping note.
- **Reason:** both are relevant existing invariants for those specific seams; citing them tightens invariant coverage. Lower priority than B-1.
- **Severity:** NON-BLOCKING.

**N-4 [NON-BLOCKING, optional] — One-line template-section-exclusion note.**
- **Location:** header block or the closing template-governance sentence.
- **Proposed text:** "As a reserved-architecture readiness doc (Doc-17 precedent), this doc omits the build-oriented template sections (Data Model, Key Interfaces, Configuration, Performance, Observability, Testing, Summary of Key Decisions) as inapplicable to a builds-nothing reservation; §7 carries the decisions."
- **Reason:** improves template auditability (review-and-quality §1 "conditional sections either included or explicitly excluded with reasoning"). Absent from the Locked Doc-17 too, so this is a betterment, not a conformance gap.
- **Severity:** NON-BLOCKING.

**F-1 [FORESIGHT-NOTE, core-source not Doc-18] — Reconcile the `IntegrationContext` javadoc when rungs 1–2 land** (the javadoc documents scoping/write-only as enforced while enforcement is the unbuilt rung). File against the R-4 backlog rows. Not a Doc-18 edit.

**Do NOT fold edits into the doc in this session** (review-separate-from-fold). The hub folds after its two-layer audit of this return; B-1 must land in the Lock docs pass before the EXT-INV registration.

---

## Env-model §10 pre-commit change-set audit (in the return, per the brief)

1. **This session created exactly ONE new file:** `context/audits/2026-07-03_Doc18_independent_DOCS_Review_Return.md` (this file). Zero docs-repo writes; zero edits to the doc under review; zero shared-file appends.
2. **Porcelain expectation (hivemind).** Before this write, lock-free porcelain showed **4 pre-existing modified spine files attributable to the hub, NOT to me:** `context/handoff/cross-agent-notes.md`, `context/handoff/pm-handoff.md`, `context/planning/phase-3-milestone-backlog.md`, `context/status/PROJECT_SNAPSHOT.md`. After this write, porcelain should show those 4 (unchanged, hub's) **plus exactly one untracked file — this return.** If the host porcelain shows any *other* path attributable to me, STOP.
3. **Prepared host-side stage command (stages exactly 1 path):**
   `git add context/audits/2026-07-03_Doc18_independent_DOCS_Review_Return.md`
   (path-specific — deliberately does NOT stage the 4 hub-modified spine files, which are the hub's in-flight work, nor the docs-repo website/ Commit A.)
4. **Commit message** staged bang-free / backtick-free / inner-double-quote-free at `ClaudeFolder/_scratch/2026-07-03_Doc18-review-return_commit-msg.txt` for `git commit -F` (a sibling of the repos, so a worker `git add -A` never stages it).
5. **Ignore-class / secrets sweep:** no runtime state, build output, caches, tokens, or keys produced or referenced; no server run; no token minted. The return contains no secrets.
6. **Expected staged count stated for Nick's glance:** **1 file.**

*Return complete. Independent verdict: RATIFY-WITH-EDITS — one BLOCKING-for-Lock additive edit (B-1: complete the EXT-INV near-duplicate analysis against INV-CE-05 and INV-SE-04) plus four NON-BLOCKING refinements and one core-source foresight note. The doc's direction, corrections, citations, rulings-fidelity, and non-preclusion all stand.*

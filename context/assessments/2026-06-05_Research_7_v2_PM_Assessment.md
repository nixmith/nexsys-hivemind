<!--
file: context/assessments/2026-06-05_Research_7_v2_PM_Assessment.md
purpose: PM assessment of Research 7 v2 (REST/WS verification + re-anchor). Supersedes the v1 assessment's §7 fabrication catalogue; v1 dispositions remain canonical except where noted.
audience: Nick, PM
state-type: assessment
status: v1 — PM-verified against source at HEAD `e73e199` (module-infos, state-store transitive graph, WsCloseCode/type facts vs the brief embeds). **NQ-1..7 RATIFIED by Nick 2026-06-05 exactly as recommended below (six leans + the NQ-3 https override). The M10/M11 API surface is decision-locked; AMD integers assign at milestone.** Dual-coordinator spike (R12) separately approved → backlog SPIKE-DC.
-->

# Research 7 v2 — PM Assessment

**Grade: A−.** The quote-back rule held: §7 quotes both verbatim module-infos correctly and every type reference matches the verified inventory (ErrorMsg not WsErrorMsg; PingMsg/PongMsg as existing; the five WsCloseCode values exact; nine ULID wrappers incl. FloorId; no `homesynapse.*` event prefix; no fabricated module names). Sources are primary-heavy (RFC texts, IANA registries, HA source files quoted verbatim, vendor docs). The v1 §7 fabrication catalogue is fully discharged. **One systematic defect (the grade cap): the §4 cross-reference labels misalign v1 REC numbers to NQ order** — substance is unaffected and maps back cleanly (table below), but it is an identifier-discipline failure of the same family the brief warned about.

## Corrected REC label mapping (use THIS, not v2's §4 labels)

| v2 §4 says | Actually is (v1 canonical) | Subject |
|---|---|---|
| "REC-62" (NQ-1) | **REC-63** | `timedInteractionMs` on CommandRequest |
| "REC-63" (NQ-2) | **REC-66** | ApiKeyScope rename |
| "REC-64" (NQ-3) | **REC-68** | ProblemType URI scheme |
| "REC-65" (NQ-4) | **REC-67** | Separate webhook DLQ |
| "REC-66" (NQ-5) | **REC-70** | WsCloseCode additions |
| "REC-67" (NQ-6) | **REC-72** | Coalescing key |
| "REC-68" (NQ-7) | **REC-64** | `@ApiCapability` annotation rename |
| "REC-69" (bcrypt) | **REC-71** | bcrypt-then-cache |
| "REC-72" (RE2/J) | **REC-65** | prefix/regex filter + RE2/J |
| "REC-75" (mTLS) | REC-75 ✓ | correct by chance |

Also wrong: v2 calls NQ-3 "the single REJECT in the PM table" — the v1 single REJECT was REC-63 (command-endpoint duplication). Cosmetic; no disposition change.

## NQ-1..7 evidence verdicts (Nick's calls — PM recommends ratifying all seven as below)

| NQ | v2 verdict | PM position |
|---|---|---|
| NQ-1 timedInteractionMs | CONFIRM | **ADOPT.** Hue transitiontime/dynamics + HA service_data = direct precedent; ms unit right (decisecond regret documented). |
| NQ-2 ApiKeyScope | CONFIRM | **ADOPT.** Key-bound noun beats generic scope names. |
| NQ-3 ProblemType URI | **OVERRIDE the PM lean — keep `https://homesynapse.local/problems/<slug>`** | **ADOPT THE OVERRIDE.** RFC 9457 §3.1.1 encourages resolvable locator URIs; Spring/Swagger/IANA registry all use https. The v1 urn: lean is withdrawn. Note: `homesynapse.local` is LAN-resolvable only — acceptable and on-brand for local-first; the runtime can later actually serve `/problems/<slug>` docs pages. Zero code change. |
| NQ-4 separate webhook DLQ | CONFIRM | **ADOPT.** Stripe/Svix/SQS isolation pattern unanimous. |
| NQ-5 keep existing close codes | CONFIRM | **ADOPT.** 4000-4999 IANA private-use; existing 5 mirror HTTP semantics; append-don't-renumber. 123-byte reason cap noted. |
| NQ-6 (entityId, attributeKey) | CONFIRM | **ADOPT.** Hue's documented per-property 1 s coalescing is the production analog. |
| NQ-7 annotation rename | CONFIRM, choose `@ApiCapability` | **ADOPT** `@ApiCapability`. |

## New RECs (REC-106..110) — dispositions

| REC | Disposition | Notes |
|---|---|---|
| REC-106 typed-value wire format: JSON-native default, tagged envelope opt-in | **ACCEPT (M10/M11)** | INV-SE-02-correct: the `{"t","v"[,"u"]}` envelope is internal storage; QuantityValue→`{"value","unit"}` (openHAB precedent); Degraded→defined sentinel object. Float natural-decimal caveat logged (§5). |
| REC-107 expose 3 event-time timestamps + stale/staleAfter | **ACCEPT (M10)** | Mirrors HA's documented triad; AMD-53-aligned; document the event-time vs wall-clock split. |
| REC-108 floors REST surface, unassign-on-delete | **ACCEPT (M10)** | Confirms AMD-44 Decision 11 as-written (force = unassign cascade, never destroys). One wording correction: floor association is `Area.floorId` only — entities reach floors via area (matches our model AND HA's "entities cannot be assigned to floors directly"); the REC's "floorId on the entity/area" phrasing must not be read as an Entity field. |
| REC-109 null-vs-absent sentinel filter semantics | **ACCEPT (M11) + SPIKE-FIRST** | Confirms AMD-44 Decision 10. The Jackson 2.x presence-detection risk is real (plain nullable record field cannot distinguish absent from present-null) — prototype before freezing the filter record's deserialization approach. The riskiest item in the document; correctly self-flagged. |
| REC-110 filter-exit tombstone frame | **ACCEPT (M11)** | Genuinely new, good UX evidence; new `WsMessage` permit (sealed-hierarchy extension; every pattern-match site updates). |

## §7 verification notes
- Both module-info quote-backs byte-match `e73e199` (comments elided, declared as such). No fabricated names anywhere — F12-class failure eliminated.
- **REC-106's proposed `requires com.homesynapse.value` is technically redundant**: PM verified `com.homesynapse.state` has `requires transitive com.homesynapse.value`, and rest-api `requires transitive com.homesynapse.state`. ACCEPT the explicit edge anyway — house style per the S4-02 precedent (explicit requires for JPMS clarity). Flag for the M10 instruction either way.
- Catalog discipline held: RE2/J + bcrypt + swagger-core correctly identified as NOT in `libs.versions.toml`, gated on explicit pinned additions.

## Strategic impact
- **B-S2 / Workstream C: zero impact.** Nothing touches device-model or integration-api.
- **M10/M11:** the API surface is now evidence-locked pending Nick's NQ ratification. New RECs queue for the M10/M11 briefings (AMD integers assign-at-milestone). REC-109 spike precedes the M11 filter freeze.
- **UI lane (W2):** once NQ-1..7 ratify, mock-data UI design can rely on: command surface shape (Doc 09 + timedInteractionMs), entity-state DTO (3+2 temporal fields), JSON-native attribute values, floors/role filters, problem-details with https URIs.

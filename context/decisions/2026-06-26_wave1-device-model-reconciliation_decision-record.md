<!--
file: context/decisions/2026-06-26_wave1-device-model-reconciliation_decision-record.md
purpose: The Wave-1 bench device-model reconciliation decisions — the rulings on the three bench escalations (ESC-W1-HUE-01 color scope, ESC-W1-COORD-01 EZSP-v14 currency, ESC-W1-SNZB03P-01 occupancy binding) + the corpus-scaffold choice. Captures Nick's §3 co-sign (decisions B4/B5/B6/B7); the precise Doc 02/08 edits ride AMD-96 (PROPOSED) through a source-verifying currency review before the Locked bodies are touched.
audience: Nick, PM hub, the Hardware bench (the physical capture), the M9 lane (the test items + the hero binding), the Web-UI lane (the hero binding)
state-type: decision record
status: RATIFIED (direction) 2026-06-26 — Nick co-signed B4/B5/B6/B7 in the §3 consolidated decision pass. The Doc 02/08 Locked-body edits are specified in AMD-96 (PROPOSED) and apply at AMD-96 ratification (after a source-verifying currency review — the AMD-95 pattern; the hub does not self-ratify edits to Locked docs).
inputs: project-knowledge/device-corpus/2026-06-23_wave1-benchup-report.md (the bench escalations) + context/assessments/2026-06-26_converter-db-embed-pipeline-design.md (V2-B — the SNZB-03P=occupancy mapping alignment) + the §1 D5 converter-DB direction.
-->

# Wave-1 Device-Model Reconciliation — Decision Record (2026-06-26)

The Wave-1 bench (MG24/EZSP + Hue White-and-Color A19 + 2× SNZB-03P) raised three Doc 02/08 escalations + a corpus-scaffold choice. Nick ruled all four in the §3 consolidated decision pass (decisions B4–B7). Each is captured below with the ruling and the downstream action. The hero path is **unblocked end-to-end on Wave-1 hardware** provided the rule binds to `occupancy` (B6).

## B4 — ESC-W1-HUE-01: V1 color scope → **White/CT only; full color post-MVP** (Option A)

**Ruling (Nick co-sign).** Scope V1 to `on_off` + `brightness` + `color_temperature`. Full color (`color_hs`/`color_xy`) is **post-MVP**. The hero needs On/Off only, so color buys the demo nothing; promoting it would pull `color_hs`/`color_xy` into the MVP sealed device-model set + add a Doc 08 §3.5 full-color handler row (with `colorMode`/`colorCapabilities` gating) — real scope expansion against a fixed date for no V1 payoff. The seam stays **non-precluding**: the model can promote color later without migration.

**Downstream (AMD-96 — the Doc 02/08 currency amendment):**
- **Reconcile Doc 02 §3.10** to stop advertising `color_hs`/`color_xy` as MVP-valid `light` options, resolving the §3.6 (reserved post-MVP) ↔ §3.10 (advertised) internal inconsistency the bench found.
- **Resolve the mireds↔Kelvin canonical-unit drift: pick Kelvin-canonical** (Doc 02's declared ingestion unit; Doc 08 converts at the adapter). Reconcile Doc 08 §3.5 (stores mireds, converts K at query) to the Kelvin-at-ingestion canonical.
- Document full color as a named post-MVP feature (the seam, not the build).

## B5 — ESC-W1-COORD-01: Doc 08 §3.3 EZSP-v14 currency → **Doc 08 §3.3 currency amendment + an M9 test item**

**Ruling (Nick co-sign).** Real Wave-1 silicon ships **EmberZNet 8.0.2 = EZSP v14**, above Doc 08 §3.3's described "EZSP v13 / EmberZNet 7.4+" band, which names only MG21. `≥ v13` nominally covers v14, but v14 is above the band the doc was written against, and EZSP version mismatch is a hard-failure class.

**Downstream:**
- **AMD-96 (Doc 08 §3.3):** acknowledge EZSP v14 / EmberZNet 8.x; name the **MG24 dongle** as a recommended target alongside MG21.
- **M9 test item:** validate EZSP v14 version negotiation (cmd `0x0000`) + ASH framing against v14; add the **ASH-timeout watch** (z2m #30891 reports `ASH_ERROR_TIMEOUT` on this exact dongle). Tracked as an M9 acceptance item.

## B6 — ESC-W1-SNZB03P-01: occupancy binding (advisory) → **bind the hero to `occupancy.occupied`**

**Ruling (Nick co-sign).** The SNZB-03P is OccupancySensing `0x0406` → the **`occupancy`** capability, **not** IAS Zone / `motion`. No model gap (both capabilities exist). Propagate, don't amend the model.

**Downstream (no AMD needed; propagation across three lanes):**
- The **hero rule + M9 + the frontend hero** all bind the trigger to **`occupancy.occupied`** (`occupied == true`), not `motion`.
- Profile-match on `(eWeLink, SNZB-03P)` — **not** a blanket "Sonoff motion → IAS" assumption (older SNZB-03 = IAS/`motion`/no-battery; SNZB-03P = Occupancy/`occupancy`/+battery).
- **Do not gate the hero on IAS enrollment** (Doc 08 §3.12 IAS is not exercised by the hero trigger). Exercise the IAS path later with the Wave-2 SNZB-04P contact sensor.
- **Cross-lane coherence:** this already aligns with V2-B's converter-DB hero mapping (SNZB-03P = `occupancy` + `battery` `binary_sensor`) — one binding, three lanes (bench + M9 + frontend).

## B7 — Corpus `[REF]`-scaffold vs blank → **keep the scaffold**

**Ruling (Nick co-sign).** Keep the pre-populated `[REF]` corpus scaffold. It is the knowledge layer; the physical bench capture fills the `[CONFIRM-ON-BENCH]` fields (a fast confirm/correct). The provenance split (`[REF]` researched-expected vs `[CONFIRM-ON-BENCH]` captured-truth) protects the M9 acceptance baseline's integrity.

## Status of the physical capture (standing — Nick's bench)
The knowledge layer + the capture-independent verdicts are done (bench Session C). **The physical silicon capture remains Nick's bench step** — the M9 acceptance ground-truth + the M7.4 E2E motion fixture (the SNZB-03P occupancy event stream). A fast confirm/correct, not a from-scratch fill.

## Governance path
Direction RATIFIED (Nick co-sign, §3). The **Doc 02/08 Locked-body edits ride AMD-96 (PROPOSED)** — they apply at AMD-96 ratification after a source-verifying currency review confirms the exact §3.6/§3.10/§3.3/§3.5 current text (the AMD-95 pattern; the hub does not self-ratify edits to Locked docs). B6 needs no AMD (propagation only). M9 scoping is unblocked (D5 + V2-B + this reconciliation), gated on the physical hero-mapping confirm + the legal soft-gate.

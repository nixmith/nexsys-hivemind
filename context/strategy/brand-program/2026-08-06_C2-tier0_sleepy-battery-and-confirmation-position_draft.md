<!--
file: context/strategy/brand-program/2026-08-06_C2-tier0_sleepy-battery-and-confirmation-position_draft.md
purpose: C-2 Tier-0 — the foundation tier of the REQUIRED-before-launch-messaging position (R-1 §6.5 obligation, v42 beat-12 adjudication §C): what we say, in one place, about device-availability truth and command-confirmation truth. Carries the R-A rider (the priced confirmation disclosure) and inherits the voice/tone platform §6 claim rails including the new no-delivery-proof entry. NAME-AGNOSTIC ({{productName}}).
audience: Nick (review + ruling); the charter (Aug-12–13, adopts/amends); the marketing-site + FE lanes (downstream, POST-adoption only).
status: ACCEPTED 2026-08-07 (v48 beat 1) — review DELEGATED by Nick to the hub (his 2026-08-07 word); adjudicated against the D5 language law, the R-A record (v45 beat 9), and the §6 rails — zero content edits; the charter (Aug-12–13) still adopts/amends, and every "as built today" claim re-verifies at ship time. Prior: DRAFT — hub-authored v47 beat 2 (2026-08-06). NOTHING here publishes pre-gate (gate sovereignty through Aug-16); counsel review pending where marked. The D5 language law binds every sentence: posture and verified fact only.
grounding: context/research/2026-07-31_research-intake_adjudication_v42-beat-12.md §C/C-2 · context/audits/2026-08-04_REV-1_audit_v45-beat-7.md (F-1/S-2, S-1; R-A recorded v45 beat 9) · integration/integration-zigbee/MODULE_CONTEXT.md (StandardAvailabilityTracker N-5 row) · context/strategy/brand-program/2026-07-22_voice-tone-messaging_platform.md §6.
-->

# C-2 Tier-0 — The Availability-Truth + Confirmation-Truth Position (DRAFT)

## 0. What this is

Tier-0 is the foundation layer: the two positions every later claim, page, or paper builds on, each stated with its mechanism, its honest limitation, and its price. C-2's charter obligation: this position must be WRITTEN before any public claim ships. Verified-at-filing convention applies — every "as built today" statement below was true at core `3723e31`; re-verify at ship time.

## 1. The availability position (sleepy/battery — the field's quiet surrender, our stated answer)

**The field's behavior (corrected baselines, from the filed research):** Z2M never pings passive devices; ZHA hard-codes a vendor carve-out (LUMI); a Hubitat app author's own words: "no good way to tell." The field's common posture is a manufactured or absent answer for battery devices. (Comparative-by-name use of these is counsel-gated; the behaviors themselves are cited in the filed adjudication.)

**Our position (as built today, verified at filing):** honest-UNKNOWN over manufactured-ALIVE, always.

- Mains-powered devices ride an active regime: a ping is earned only by ~10 minutes of silence — never a ping storm, never a boot wave.
- Battery/sleepy devices are NEVER judged by a regime built for mains: they ride a 25-hour passive contract window with persisted recency that survives restarts. A sleeping sensor is not "offline"; it is a device honoring its own physics.
- Unknown power source is treated battery-conservatively (never false-offlined).
- When the evidence doesn't support an answer, the product SAYS UNKNOWN. It does not guess, and it does not render a reassuring blank.

**Tier-0 sayable sentences (inherit §6 rails):** "A sleeping sensor isn't a dead sensor — we track the difference." · "When we don't know, we say unknown. We never manufacture 'online.'" · "Battery devices are never marked dead by a test built for plugged-in devices."

## 2. The confirmation position (the R-A rider — the priced disclosure)

**What CONFIRMED means (R-A(a), ruled 2026-08-05 — the binding reading):** CONFIRMED is STATE-truth: the device's own subsequent report evidenced the commanded state. Never-false-CONFIRMED binds this reading: the product never reports CONFIRMED without device-report evidence of the state. That claim has held across every unattended night on the bench record, including the nights the bench itself was failing — the honest verdicts are the exhibit.

**The documented limitation, priced (disclosed, not hidden):** state-truth is not causality-proof. For toward-current-state commands ONLY (commanding a value the device is already reporting), a routine periodic report of that same value inside the confirmation window is indistinguishable from causal evidence. Priced at a measured device cadence of ~one report per ~5 minutes (the S31 corpus): ~1.7% of such commands at a 5 s window, ~10% at the 30 s default, could confirm on a coincidental report. Away-from-current-state commands are not exposed (confirmation requires the NEW value; a non-causal report carries the old one).

**The chartered closure, named:** the delivery-evidence closure (S-1 / candidate (iii)) — binding the radio-layer delivery evidence the adapter already receives (and today discards) into the confirmation record — is chartered for the Aug-12–13 charter. Until it ships, the §6 rail holds absolutely: no delivery-proof claims. DISPATCHED means hand-off, not delivery.

**Tier-0 sayable sentences:** "Confirmed means the device's own report showed the state — evidence, not hope." · "We document exactly what confirmation does and doesn't prove — including the edge case, with the number." · Where enforcement is discussed, the layered form ONLY: the deterministic floor is MISSING from the field, not SUPERIOR; L2/L3 without L1 are unsound, L1 without L2 is insufficient.

## 3. Rails and inheritance

Every consumer of this position inherits the voice/tone platform §6 verbatim — including the 2026-08-06 entry: no delivery-proof claims until delivery evidence ships. State our behavior, not their failure; comparisons use corrected baselines and re-verify at ship time. Nothing a future paid/cloud tier would have to retract.

## 4. What Tier-0 waits on

Counsel (Pelton) for anything comparative-by-name · the charter for adoption and for the delivery-evidence closure's slot · G-2 for the name token · the gate (Aug-16 THE READ) before anything publishes. Tier-1+ (the full position paper, per-integration detail, the s31 thread as a public reliability-engineering exhibit) builds on this only after the charter rules.

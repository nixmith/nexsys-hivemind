<!--
file: context/programs/matter-design/memos/2026-07-19_B4-r1_lab-quote-request-drafts.md
purpose: The B4-r1 authorized $0 lab-quote engagement — two ready-to-send quote-request drafts (Resillion + DEKRA as the comparator; UL Solutions as the named alternate) so the next certification-posture decision prices from a real software-component number instead of a hardware-scoped ceiling. Send is Nick's act, at leisure; no commitment, no fees, no membership required to ask.
audience: Nick (fills identity tokens and sends); the program (records responses as B4 evidence when they arrive).
state-type: execution memo (drafts; token-parameterized per R-1 — fill ${...} at send).
status: CUT 2026-07-19 (program beat 3; B4 rider r1 AUTHORIZED).
-->

# B4-r1 — Matter Certification Lab Quote Requests (drafts)

**Why these exist:** no authorized Matter test lab publishes a rate card; the only public bound is a dated, hardware-scoped ceiling ($7–10k lab + $2–3k application, ~2022-era). Software-component controllers skip transport/radio testing, so the real number is likely lower — only a quote says how much. Recipients: **Resillion** (Home Assistant's named lab; 11 accredited sites) and **DEKRA** (comparator; UL Solutions is the alternate if either stalls). Send both the same day; note in the tracker which responds first and with what scope questions — the questions themselves are evidence about the test scope.

**Before sending, fill:** ${NAME} · ${COMPANY} (legal entity as it would appear on a certification) · ${CONTACT}. Do not name the product brand (R-1 pending) — "our smart-home platform" suffices at quote stage; labs are used to pre-launch confidentiality, and an NDA offer is included.

---

## Draft 1 — Resillion (via their Matter certification contact form / sales alias)

Subject: **Budgetary quote request — Matter certification, Software Component (controller), Linux/arm64**

Hello,

We are preparing a Matter controller integration for our smart-home platform and would like a budgetary quote and scope outline for CSA Matter certification of a **Matter Software Component — a controller** (the "Underlying Software Component" category, per the CSA's software-component certification class; the Home Assistant / OHF Matter Server certification is the shape we have in mind).

Product profile for scoping:

- Component type: Matter controller (commissioner + operational controller), software-only — no radio hardware ships with it.
- Operating environment: headless Linux (Debian-family), aarch64 (Raspberry-Pi-class) and x86_64.
- Stack lineage: matter.js-based controller componentry (the Open Home Foundation lineage).
- Target specification version: Matter 1.6-era at certification time.
- Device-type breadth for test scope: on/off plug and switch, extended color light, occupancy sensor, plus bridged endpoints via a Matter bridge.
- Status: pre-certification, pre-CSA-membership (we understand Adopter membership is the prerequisite and are timing that decision partly on your quote).

Could you provide: (1) a budgetary price range for lab testing of this scope; (2) whether the application/administration fee is separate and its range; (3) typical calendar time from engagement to certificate for a software component; (4) what the test scope actually covers for a controller-role component (PICS scope, which TC suites apply); and (5) whether a derivative-certification path applies when the component builds on an already-certified underlying component.

We are happy to sign an NDA for scoping specifics.

Thank you,
${NAME} · ${COMPANY} · ${CONTACT}

---

## Draft 2 — DEKRA (comparator; same body, one delta)

Subject: **Budgetary quote request — Matter certification, Software Component (controller), Linux/arm64**

[Identical body to Draft 1, with the closing question replaced by:]

…and (5) whether DEKRA has certified controller-role software components to date, and if the answer to scope differs between your EU and US labs.

Thank you,
${NAME} · ${COMPANY} · ${CONTACT}

---

**When responses arrive:** paste them to the program hub (any session); they are B4 evidence — the ledger's posture (a)→(c) stands regardless; the quote only re-prices option (b) for the day trigger T1 fires. If both labs require membership even to scope, that fact itself is a B4 ledger note (the A5 return found no such requirement; a contradiction would be a correction).

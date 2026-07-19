<!--
file: context/programs/matter-design/memos/2026-07-19_C1-C4_counsel-handoff_pelton.md
purpose: The C-1..C-4 counsel questions from the Matter design program, packaged for the counsel queue (the Pelton consult, Mon 2026-07-21). Questions only — wording and legal conclusions stay counsel's; NOTHING in the Matter program gates on the answers. Nick carries this file into the counsel program's queue (the counsel program is separate and self-governing; this program never writes its tree).
audience: Nick (the carrier); counsel (the audience); the counsel-navigator lane (queue intake).
state-type: hand-off memo (point-in-time; sources dated 2026-07-19).
status: CUT 2026-07-19 (program beat 3; B4 ruled "(a) → (c) @ T1-Hub trigger + both riders").
-->

# Matter Trademark/Certification Questions for Counsel (C-1..C-4)

**One-paragraph context for counsel:** ${COMPANY} is building a local-first smart-home platform (Apache-2.0 core). A Matter *controller* integration is in formal design now; code ships later. Matter is governed by the Connectivity Standards Alliance (CSA). We are **not** CSA members; the ruled posture is: ship uncertified with honest wording now, certify at a named commercial trigger later, with an Adopter-tier join ($7,500/yr) held in reserve. Certification is voluntary for controllers (Home Assistant shipped uncertified 2022→2025 at ecosystem scale; the "Matter Software Component" certification category now exists). The controlling document is the CSA **Trademark and Logo Use Guide (updated November 2025)** — member-gated marketing use of "Alliance Brands," certification-gated on-product use, a member-only forward-looking-claim template ("Our xOS version 19 will support Matter this fall"), and a blanket non-member prohibition "**except as may be permitted by law**." Source URLs in the appendix.

## The four questions (verbatim from the program's A5 research return §5.3)

- **C-1 (nominative use):** Under US nominative-fair-use doctrine, may a non-member's software product state "controls/works with Matter-certified devices" in docs and marketing, given the Nov-2025 guide's blanket non-member prohibition with its "except as may be permitted by law" carve-out? What wording envelope is defensible without contact with marketing@csa-iot.org, and is proactive contact advisable?
- **C-2 (forward-looking claims):** Is the guide's forward-looking-claim template ("will support Matter this fall") available ONLY to members in good standing? If yes, what non-member phrasing of a dated roadmap statement stays outside the marks (e.g., naming the *standard* vs using the *wordmark* in product positioning)?
- **C-3 (naming / R-1 interplay):** The guide gates "Product naming" — confirm no ${PRODUCT}-family name may ever embed "Matter" (or "Zigbee"/"Z-Wave"), and fold into the R-1 rename-readiness token rules. (No new brand-coupled names are proposed anywhere; all candidate copy is token-parameterized.)
- **C-4 (test-VID posture):** Any legal exposure in operating/shipping a controller whose fabric VID defaults to the spec's test range (0xFFF1) pre-membership? Engineering evidence: unenforced in-protocol and the ecosystem default (Home Assistant's stack defaults to 0xFFF1; HA overrides with its own allocated VID); counsel confirms whether trademark/certification policy or the spec's licensing terms reach it.

**These join the standing counsel items #1–#3** (CSA controller-policy wording · Z-Wave marks posture · SHELLY nominative posture — banked in the integration-roadmap return §7.2). **Nothing gates on the answers:** the design program proceeds regardless; the answers shape public *wording* only (the F1/F2 launch-messaging envelope) and the timing comfort of the reserved Adopter join.

## Appendix — the sources counsel may want on screen (all fetched 2026-07-19)

- Trademark and Logo Use Guide (Nov 2025): https://csa-iot.org/wp-content/uploads/2022/11/TM_Logo-Use-Guide_Update_November-2025.pdf
- Matter Brand Guidelines v1.6 (Jun 2025): https://csa-iot.org/wp-content/uploads/2022/11/Matter_Brand-Guidelines_v1.6.pdf
- CSA membership/fees: https://csa-iot.org/become-member/ · certification categories: https://csa-iot.org/certification/why-certify/
- The HA certification precedent (server certified standalone; UI certified "about being able to display the Matter trademark"): https://www.home-assistant.io/blog/2025/03/10/matter-certification/
- Full evidence dossier: `context/programs/matter-design/returns/A5_integration-2-and-certification_return.md` §4–§5.

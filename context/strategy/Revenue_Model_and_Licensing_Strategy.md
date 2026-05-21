<!--
file: context/strategy/Revenue_Model_and_Licensing_Strategy.md
purpose: Locked strategic decision on Apache 2.0 licensing and revenue model.
audience: PM, Nick
update-cadence: ad-hoc
state-type: reference
status: CURRENT
last-verified: 2026-05-20 against commit 25bc23b
-->

# Revenue Model & Licensing Strategy

**Purpose:** One-page reference for the foundational revenue and licensing decisions. Any agent making dependency choices, feature-boundary decisions, or assessing whether a capability belongs in the free tier vs. a paid tier must consult this document.
**Status:** Locked strategic decision — changes require Nick's explicit approval
**Source:** Synthesized from MVP doc, strategic context map non-negotiables, and conversation-established decisions

---

## The Licensing Decision: Apache 2.0

**Decision:** HomeSynapse Core is licensed under Apache 2.0.

**Why Apache 2.0 specifically (not MIT, not AGPL, not BSL):**

- **Apache 2.0 grants patent protection** that MIT does not. This matters for a platform that will have hardware OEM partners (NexSys OS licensing, Phase 4+). OEMs need patent safety to build on the platform.
- **Apache 2.0 is permissive enough for enterprise adoption.** Companies evaluating HomeSynapse for commercial products (installer channels, MDU management, OEM licensing) can adopt without viral licensing concerns. This directly enables the Phase 3–4 revenue streams.
- **Apache 2.0 avoids AGPL's network-use trigger.** AGPL would force anyone running HomeSynapse as a service (cloud hosting, managed installations) to open-source their modifications. This would kill the NexSys Connect/Cloud Pro subscription model — NexSys needs proprietary cloud services built on top of the open core.
- **Apache 2.0 is the standard for infrastructure software.** Kubernetes, Kafka, Spark, Cassandra. It signals "this is serious infrastructure," not "this is a hobby project." Trust brand alignment.

**Architectural implication:** The core must be cleanly separable from cloud features. No AGPL dependencies can contaminate the core. The integration runtime must support both open-source community integrations and commercial/proprietary integrations without licensing conflict.

---

## The Four-Layer Revenue Model

Revenue is structured as progressive value creation. Each layer builds on the one below. No layer extracts value — every layer creates direct value for the user.

### Layer 1: HomeSynapse Core (Free, Apache 2.0)

**Price:** $0
**What it is:** The complete smart home operating system. Event bus, state store, persistence, automation engine, integration runtime, REST/WebSocket APIs, web UI, Zigbee/Z-Wave/Matter adapters.
**Revenue:** None. This layer exists to serve the user and build the installed base.
**Strategic function:** Market entry. Trust establishment. Community building. The free tier is fully functional — not crippled, not time-limited, not device-count-limited. A user who never pays NexSys a dollar still gets the best local-first smart home platform available.

**Non-negotiable constraint:** Core functionality is never feature-gated behind a subscription. No per-device fees. No mandatory cloud dependency.

### Layer 2: HomeSynapse Connect (Cloud Subscription — $7.99/mo)

**Price:** $7.99/month
**What it is:** Cloud backup, remote access, voice assistant integration bridge, firmware update channel, community integration repository access.
**Revenue:** Recurring SaaS. The primary early-stage revenue driver.
**Strategic function:** Convenience upgrade for users who want remote access and cloud backup without self-hosting infrastructure. Conversion target for free-tier users.

**Architectural implication:** Connect services are additive — they enhance the local system but never replace local functionality. If Connect goes down, the home still works identically.

### Layer 3: HomeSynapse Cloud Pro (Premium Cloud — $14.99/mo)

**Price:** $14.99/month
**What it is:** Advanced energy analytics, historical data visualization, multi-home management, advanced automation templates, priority support.
**Revenue:** Recurring SaaS. The upsell from Connect.
**Strategic function:** Revenue maximization from power users. Also creates the derived datasets that power Layer 4 institutional products (with explicit user consent).

### Layer 4: HomeSynapse Hub (Hardware — $149)

**Price:** $149 (target)
**What it is:** Pre-configured hardware (Raspberry Pi-class or custom SBC) with HomeSynapse pre-installed, Zigbee/Z-Wave/Thread radios, optimized storage, plug-and-play setup.
**Revenue:** Hardware margin + recurring Connect/Pro conversion funnel.
**Strategic function:** Eliminates the installation barrier for non-technical users. The "just plug it in" path to HomeSynapse. Also the hardware platform for utility-subsidized deployment programs (NexSys Grid partnerships).

---

## Post-MVP Revenue Streams (Phase 2+)

These are documented in detail in `From_Platform_to_Institution_NexSys_Strategic_Report.docx`. Summary for quick reference:

| Stream | Phase | Model | Est. Revenue per Unit |
|---|---|---|---|
| NexSys Grid (VPP/energy) | Phase 2 | 15–20% platform fee on VPP payments to users | Revenue scales with enrolled homes |
| NexSys Assure (insurance) | Phase 3 | $2–5/mo per home, charged to insurer | $1.44M/yr at 40K homes |
| NexSys Care (aging-in-place) | Phase 3 | $29–49/mo subscription | Medicare RPM reimbursement pathway |
| HomeSynapse Professional (installer) | Phase 3 | Per-installation licensing + support | TBD |
| HomeSynapse Property (MDU) | Phase 3 | Per-unit management fee | TBD |
| NexSys OS (OEM licensing) | Phase 4+ | Per-device licensing fee | TBD |
| NexSys Trust Mark (certification) | Phase 4+ | Annual certification fee | TBD |

---

## Revenue Principles (Non-Negotiable)

1. **Every revenue stream must create direct value for the user.** If the user doesn't benefit, the stream doesn't exist.
2. **Revenue through progressive value, never extraction.** Users pay because the paid tier is genuinely better, not because the free tier is artificially crippled.
3. **Self-funding growth model.** No VC funding that demands hypergrowth at the expense of trust. Patient capital alignment.
4. **No advertising, ever.** No data monetization, ever. These are absolute constraints, not aspirational guidelines.
5. **No per-device fees.** Adding a device to your home should never cost you money on an ongoing basis.

---

## Decision Checklist for Agents

When making a dependency, feature-boundary, or architecture decision, verify:

- [ ] Does this dependency's license conflict with Apache 2.0? (No AGPL, no GPL in core)
- [ ] Is this feature in the free tier or a paid tier? (If it's core functionality, it must be free)
- [ ] Does this feature work without internet? (If it's in Core, it must)
- [ ] Does this feature create value for the user, or does it extract value? (Extraction is prohibited)
- [ ] Does this change affect the clean separation between Core and cloud services? (Separation must be maintained)
- [ ] Could an OEM ship this without licensing concerns? (Apache 2.0 must remain clean)

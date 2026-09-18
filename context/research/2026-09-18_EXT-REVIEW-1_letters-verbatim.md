<!--
file: context/research/2026-09-18_EXT-REVIEW-1_letters-verbatim.md
purpose: THE EXT-REVIEW-1 LETTERS, verbatim (the body below is byte-identical to `_scratch/v76/2026-09-18_EXT-REVIEW-1_letters-verbatim.md`, md5 0d0962b91cb1a93e975697d2a808fcfc; its own frontmatter names the staging path): the reviewer's eight inbound messages and the eight outbound replies as drafted, exported from the advisory session on Nick's word `EXPORT: letters` (v76 b4) and returned `LETTERS: RETURNED … 114222`. The distillation is `context/research/2026-09-18_EXT-REVIEW-1_diagnostic-wedge-reader-study_intake-packet.md`; the adjudication the v76 b3 audit. The reviewer declined attribution (C-14): no name appears here and none may be added.
audience: the hub (the record) · Nick
state-type: verbatim archive (external-origin; never edited)
status: FILED v76 beat 5 (Fri 2026-09-18 ~15:5x CT; instrument 2026-09-18T20:54:29Z)
-->

<!--
file: _scratch/v76/2026-09-18_EXT-REVIEW-1_letters-verbatim.md
purpose: VERBATIM ARCHIVE of the EXT-REVIEW-1 exchange (2026-09-17 → 2026-09-18). Eight inbound messages from the external reviewer (seven letters plus one closing note) and the eight outbound replies as drafted in the Cowork session. No summary, no analysis, no commentary. The distillation lives in `context/research/2026-09-18_EXT-REVIEW-1_diagnostic-wedge-reader-study_intake-packet.md`; this file is the source text that packet was made from.
audience: the hub (provenance; the pre-registration artifacts appear here in their original context) · any future write-up of the exchange
state-type: verbatim archive (append-only; do not edit the reproduced text)
provenance: inbound text reproduced exactly as pasted into the Cowork session by Nick, including source rendering artifacts. Outbound text reproduced exactly as DRAFTED in that session; Nick sent these but may have edited before sending, so treat outbound as the draft of record, not a certified transmission. The Cowork session's analysis that accompanied each draft is NOT included here — it is distilled as the S-rows of the intake packet.
attribution: the reviewer declined attribution (intake packet C-14). No name, employer, or identifying detail appears in this file and none may be added.
status: STAGED Fri 2026-09-18 CT in `_scratch/v76/`. Unadjudicated; no charter; not audited at the bytes.
-->

=== ROUND 1 — INBOUND ==========================================================

## BLUF

**Technically, this sounds valuable. Commercially, it is not yet possible to say it is valuable without evidence of adoption, reliability, integration coverage, and willingness to pay.** A feature-complete alternative to Home Assistant is not, by itself, a large business: Home Assistant already has substantial ecosystem, community, and interoperability momentum, including Matter certification. Your potential value is in turning local-first control, auditability, multi-site operation, and constrained AI actuation into a **trusted physical-environment platform** for customers who have real consequences when automation fails. 

My blunt assessment:

- **Technical-product potential:** high, assuming the claims hold under independent testing.
- **Consumer smart-home value:** uncertain to modest unless installation and interoperability are dramatically easier than Home Assistant's.
- **Enterprise/small-commercial value:** potentially significant—but only if you can prove security, uptime, lifecycle management, and safe remote administration.
- **AI control of physical systems:** strategically compelling, but it is where your risk, liability, and engineering burden increase sharply.

The market does not pay much for "more features." It pays for **less risk, lower operating cost, easier deployment, and defensible accountability**.

---

## What appears genuinely differentiated

Your strongest claims are not "we can automate devices." They are:

1. **Local-first operation**
   - Works during Internet outages.
   - Reduces dependency on vendor cloud services.
   - Supports lower-latency and more private control.

2. **Portable ownership of configuration and data**
   - Import/export, backup/restore, and multi-home operation can reduce lock-in.
   - This is especially relevant to integrators, property owners, facilities operators, and organizations that cannot accept a homeowner-style "start over" failure mode.

3. **Event provenance and attribution**
   - If a user can answer: *What happened? Which automation fired? Which input triggered it? Which plugin or person changed the rule? What action resulted?*—that is much more valuable than ordinary smart-home logs.
   - This is useful for troubleshooting, incident response, disputes, maintenance, and compliance evidence.

4. **A programmable automation model**
   - Extensibility is a real moat only if it is reliable, safe, documented, and easy for third parties to develop against.

5. **Privacy as a product architecture rather than a marketing statement**
   - Local processing, no behavioral-data resale, user-controlled backup, and customer-controlled model inference can be meaningful differentiators.

The core opportunity is to become less like "another home dashboard" and more like:

> **A local, auditable automation and policy engine for physical environments.**

That could apply to homes, multi-dwelling properties, small businesses, hospitality, labs, light industrial environments, or distributed facilities—subject to the safety and regulatory demands of each market.

---

## What is *not* yet a differentiator

### "It does everything Home Assistant does—and more"

That is necessary for parity, but it is not a sufficient business case. Home Assistant's advantages include an established integration ecosystem, community support, hardware familiarity, documentation, installer knowledge, and a recognizable privacy/open-home brand. Its Matter implementation has official certification, which also gives it ecosystem credibility. 

To beat or complement it, you need to show measurable superiority in areas such as:

- Setup time from unboxing to useful automation
- Number and quality of supported devices/protocols
- Reliability during network loss, reboot, upgrade, and partial-device failure
- Automation-debugging time
- Backup and restoration success rate
- Security posture for remote access
- Multi-site fleet administration
- Mean time to detect and resolve a failed automation
- Safe, constrained AI action

### Append-only logs and chain hashing

These are useful engineering primitives, but buyers will not pay simply because you use them.

They become valuable only when you can explain the customer outcome:

- "You can prove which rule unlocked the door."
- "You can identify the plugin version that caused a thermostat failure."
- "You can restore a known-good automation state."
- "An administrator cannot silently alter an incident record."
- "We can reproduce the exact event sequence that caused an unsafe behavior."

Also, chain hashing alone does **not** establish trustworthy auditability. If an attacker or privileged administrator can alter the log, keys, timestamps, signing process, or verification client, then the chain may provide limited assurance.

For enterprise-grade audit evidence, you need:

- Digitally signed events or signed periodic checkpoints
- Protected key storage and key rotation
- Independent or immutable checkpoint storage
- Verified time source and clock-drift handling
- Defined retention, export, deletion, and legal-hold behavior
- Schema versioning and event-replay guarantees
- A clear answer to: "Who can alter, redact, or destroy records?"

---

## Honest valuation view

Without customer, revenue, and operating metrics, the honest answer is:

> **Your software may be worth anywhere from little more than its replacement-cost/IP value to a very valuable venture-scale platform. The description alone cannot distinguish those outcomes.**

At the pre-traction stage, a sophisticated codebase is often worth **far less than its builders expect**, because the costly part is not writing the software. The costly parts are:

- Winning trust
- Supporting devices indefinitely
- Maintaining integrations as vendors change APIs and firmware
- Secure remote-access operations
- Handling vulnerability disclosures and patches
- Customer support
- Proving reliability
- Selling into organizations with long procurement cycles
- Carrying liability for physical-world failures

A practical value framework:

| Evidence | What it indicates |
|---|---|
| Working demo only | Technical asset; commercial value remains highly uncertain |
| Independent security test and real deployments | Credibility beyond a prototype |
| Strong user retention | The product solves a recurring problem |
| Paid installations or subscriptions | Actual market willingness to pay |
| Repeatable installer/integrator channel | Scalable distribution |
| Multi-site management and enterprise contracts | Higher-value market position |
| Measured reliability and low-support burden | Defensibility and margin potential |
| Safe AI control with enforceable policy boundaries | Potential strategic differentiation, but also more liability |

If you have **no paying deployments**, do not think of this as a valuation problem yet. Think of it as a **proof problem**:

1. Does it reliably work?
2. Do a narrowly defined group of users prefer it?
3. Will they pay?
4. Can you deploy and support it repeatedly?
5. Can you demonstrate that it is safer than alternatives?

---

## The most promising commercial wedge

Do **not** start by trying to win "the entire smart-home market."

A better wedge is a segment where these capabilities have direct economic value:

### Option A: Multi-site residential and property operations
Examples: property managers, short-term-rental operators, high-end residential integrators, multi-unit housing.

Your pitch:
- One control plane for many sites
- Local operation even when cloud connectivity fails
- Device/automation audit trails
- Delegated access for owners, guests, maintenance, and operators
- Fast recovery after equipment replacement or turnover
- Privacy-preserving tenant boundaries

### Option B: Small commercial buildings and distributed facilities
Examples: offices, retail chains, warehouses, labs, churches, community facilities, franchise sites.

Your pitch:
- Local building automation without a large building-management-system deployment
- Multi-site policy templates
- Energy, occupancy, access, environmental monitoring, and maintenance automation
- Change control, logs, and remote support
- Controlled technician access

### Option C: Privacy-sensitive or high-autonomy households
Examples: technically capable users who want local AI, locally retained data, and no cloud dependency.

This can build an early community, but it is usually harder to monetize at enterprise levels.

**My recommendation:** use sophisticated enthusiasts and integrators as early adopters, but build the product roadmap around **multi-site, accountable automation**. That is where your auditability, exportability, local-first design, and fleet capabilities matter most.

---

## What "enterprise-grade" should mean for your product

"Enterprise-grade" should not mean adding a login screen and an admin dashboard. It should mean an organization can safely deploy, govern, recover, and audit the system at scale.

### 1. Multi-tenant and multi-site operating model

Build a clean hierarchy:

```text
Organization
  └── Portfolio / Business Unit
        └── Site / Home / Facility
              └── Zone
                    └── Device
                          └── Capability / Endpoint
```

Support:

- Strict tenant isolation
- Delegated administration
- Site-specific and organization-wide policies
- Role-based and attribute-based access control
- Separate owner, administrator, installer, maintainer, auditor, occupant, and service-account roles
- Temporary access with automatic expiration
- Per-site data residency and backup policy
- Complete offboarding when a customer, employee, contractor, or tenant leaves

For enterprise identity, support standards-based single sign-on and lifecycle provisioning, such as OpenID Connect, SAML, and SCIM.

### 2. Zero-trust remote administration

Remote control is one of your largest attack surfaces. Do not trust a user, device, service, or plugin merely because it is "inside" a home or site network. NIST's zero-trust approach is based on minimizing implicit trust and focusing protections around individual resources and access decisions. 

Implement:

- Per-device cryptographic identity
- Mutual authentication between components
- Least-privilege, short-lived authorization tokens
- Per-action authorization, not just session authorization
- Device attestation where hardware supports it
- Strong administrator authentication, including phishing-resistant MFA
- IP/device/location risk signals where appropriate
- Just-in-time privileged access
- "Break-glass" access that is time-bound, highly logged, and requires review
- Explicit revocation when an account, plugin, remote relay, or device is compromised

### 3. Secure plugin ecosystem

Your plugin system could be a major advantage—or the fastest way to compromise customers.

Treat plugins as untrusted by default:

- Signed plugin packages and publisher identities
- Permission manifests that users can inspect
- Capability-based permissions: e.g., "read temperature sensors," "send notification," "control lights in Zone A"
- No blanket access to all devices, all logs, or cloud credentials
- Sandboxing through process isolation, containers, WebAssembly, or equivalent controls
- Reproducible builds and dependency inventories
- Automatic revocation or quarantine for known-malicious plugins
- Plugin compatibility testing against core releases
- A security-review path for "verified" plugins
- Clear distinction between community, verified, and first-party plugins

NIST's Secure Software Development Framework is a useful baseline for integrating security across development, release, vulnerability response, and maintenance; IEC 62443-4-1 is particularly relevant if you move toward industrial or operational-technology environments. 

### 4. Reliability engineering, not merely feature engineering

For a system that controls a physical environment, reliability must be designed as a product feature.

Build for:

- Offline-first operation with defined degraded modes
- Idempotent commands and event processing
- Clear delivery semantics: at-most-once, at-least-once, or exactly-once where realistically achievable
- Conflict resolution for disconnected sites and restored backups
- Transactional configuration changes
- Configuration versioning and one-click rollback
- Safe firmware and software updates with rollback
- Device-health monitoring and "unknown state" handling
- Event replay and deterministic automation simulation
- Hardware-in-the-loop testing for common devices
- Fault injection and chaos testing
- A published compatibility matrix
- Defined recovery point objectives and recovery time objectives

Your key product question should be:

> "When the system is partially broken, what does it do—and can the operator understand and recover it safely?"

### 5. Security and procurement evidence

Enterprise customers will ask for proof, not claims.

Prepare a security package containing:

- Architecture and data-flow diagrams
- Threat model
- Security white paper
- Penetration-test summary from an independent assessor
- Vulnerability-disclosure policy and response process
- Software bill of materials for releases
- Release signing and supply-chain controls
- Incident-response plan
- Backup, restore, and disaster-recovery test results
- Privacy and data-retention documentation
- Subprocessor list, if any cloud services are used
- Service-level objectives and support model

NIST provides a foundational cybersecurity capability baseline for IoT devices; OWASP's IoT guidance is also useful for identifying recurring failure classes such as weak credentials, insecure network services, and poor update practices. 

---

## Safe AI actuation: the architecture to build

Your long-term AI direction is credible, but **do not let an LLM directly "drive the house."**

The correct architecture is:

```text
Sensors / Device Events
        ↓
Data and Context Layer
        ↓
Local or Remote Model
        ↓
Constrained Planning Layer
        ↓
Policy / Authorization / Safety Engine
        ↓
Typed, Allowlisted Action Interface
        ↓
Device Gateway
        ↓
Physical Device
```

The LLM may propose an action. It should **not** be the final authority for a physical action.

### Separate observation from actuation

Use tiers:

| Tier | AI permission | Example |
|---|---|---|
| 0 | Observe and summarize only | "The upstairs temperature has risen unusually fast." |
| 1 | Recommend action | "Consider closing the blinds and lowering cooling setpoint." |
| 2 | Perform low-risk, reversible actions | Adjust lighting, send notifications, run a vacuum in a permitted area |
| 3 | Perform bounded actions with policy approval | Change a thermostat only within fixed comfort and safety limits |
| 4 | Require explicit human confirmation | Unlock doors, open garage doors, disarm alarms, disable cameras |
| 5 | Prohibit autonomous model control | Safety-critical equipment, emergency systems, hazardous appliances, life-safety functions |

Do not classify an action solely by the device. Context matters. Turning on a light is low risk; turning on a heating appliance in an unoccupied building may not be.

### Put policy outside the model

The policy engine should independently enforce:

- Who may request the action
- Which model may propose it
- Which devices it may affect
- Time, location, occupancy, and environmental constraints
- Maximum temperature, power, run-time, velocity, or cost
- Required confirmation level
- Rate limits
- Emergency stop behavior
- Whether the action is reversible
- Whether the system is in a degraded or uncertain state

This means the model cannot override safety constraints through persuasive language, a malformed tool call, or a prompt-injection attack.

### Treat incoming data as potentially hostile

A smart environment ingests untrusted content:

- Device names
- Calendar entries
- Email/text notifications
- Voice transcripts
- Web content
- QR codes
- Camera metadata
- Plugin-generated events
- Data from compromised devices

Any of those could contain instructions designed to manipulate an AI model. Therefore:

- Keep untrusted content separate from policy and tool instructions.
- Use typed tool calls rather than natural-language command interpretation.
- Validate all model outputs against strict schemas.
- Require authorization after—not before—the model produces a recommendation.
- Maintain a clear provenance trail for every model input, tool request, policy decision, and resulting actuation.

NIST's AI Risk Management Framework organizes AI risk work around **govern, map, measure, and manage**; its Generative AI profile is a useful organizing reference for this work. 

### Build simulation before autonomy

Before an AI can make a real-world change:

1. **Replay** historical event sequences.
2. Run the model in **shadow mode**: it proposes actions but cannot execute them.
3. Compare proposed actions against what users or rules actually did.
4. Measure safety-policy denials, false positives, missed actions, and recovery behavior.
5. Deploy with limited canaries and narrow permissions.
6. Expand only after evidence supports it.

Your append-only event architecture could be a major advantage here. It can provide the data needed for replay, testing, investigation, and controlled learning—provided users understand and control how their data is used.

---

## One important language correction

Avoid saying the product "complies with local, state, and federal laws wherever in the world it is used" unless you have a jurisdiction-by-jurisdiction legal basis, contractual commitments, documented controls, and a process for keeping them current.

A more defensible statement is:

> "The system is designed to support privacy, data-minimization, audit, retention, and access-control requirements. Customers remain responsible for determining the legal and regulatory requirements applicable to their deployment."

That is more credible and less likely to create legal exposure.

---

## The next 12 months: highest-value priorities

1. **Choose one initial buyer and use case.**  
   Do not build equally for hobbyists, homeowners, integrators, property operators, and industrial customers.

2. **Prove a narrow superiority claim.**  
   For example: "Multi-site automation with deterministic audit trails and local operation."

3. **Develop an assurance architecture.**  
   Identity, permissions, key management, signed releases, secure plugins, backup recovery, and incident response.

4. **Make observability a first-class feature.**  
   A user must be able to answer "why did that happen?" in seconds—not after reading raw logs.

5. **Treat AI as a controlled subsystem.**  
   Begin with read-only insight and recommendations; make physical actuation typed, policy-gated, reversible where possible, and auditable.

6. **Obtain independent validation.**  
   Security testing, deployment references, restore drills, and measured uptime will increase credibility more than another major feature.

The most valuable version of this product is not "Home Assistant with more capabilities." It is **a trustworthy local automation platform that can safely explain, govern, recover, and eventually constrain AI action in real physical environments.**

=== ROUND 1 — OUTBOUND =========================================================

This is more useful than what I gave you to work with, so first: three corrections to me.

The "everything Home Assistant does and more" framing was mine and it's wrong. Parity isn't a business case and I shouldn't have led with it. The compliance line — I'm retiring it and using your wording instead. And you're right that chain hashing alone isn't audit evidence: without signed checkpoints, key custody, and a trusted time source, a privileged admin can rewrite the chain. That work isn't built. What exists today is durability and hash measurement, both of which are currently finding defects, which is the point of them.

Two places I'd push back.

The wedge. You recommend multi-site property operations, then list what enterprise-grade requires — tenant isolation, SSO/SCIM, data residency, signed plugin sandboxing, pen-test evidence, RPO/RTO. I have about seven hours a week. That list is the argument against your own recommendation. The narrower wedge is the integrator's unbillable truck roll: the service call where nothing visibly broke and nobody can say why the automation didn't fire. That's a cost line, not a feature, and it can sit alongside an existing control system instead of replacing it. Design partners, not a dealer program.

The differentiator. It isn't easier setup. Home Assistant answers "why did it fire" from its logbook; it records no reason for a legitimate non-fire, no confirmation verdict, and no record of a command that produced no state change — and its chain self-purges. The three questions I instrument are: why did it fire, why didn't it, and did the device actually confirm. Narrow and refutable, which is how I want it.

One thing your letter doesn't have: timing. Matter 1.6 shipped 17 June 2026 with Joint Fabric and thermostat suggestions — ecosystems propose, the device evaluates against local policy before acting. That's the architecture I already built, and the provisional definitions are still moldable.

Where the evidence is: on real hardware, at three verified builds, it has installed as an ordinary package on a Raspberry Pi, run its Zigbee integration, adopted a mains device and a battery sensor, and fired an automation whose command the device itself confirmed. A 72-hour unattended benchmark starts Oct 30. Four numbers come out of it: latency-to-detect, latency-to-clear, false-clear-while-stationary, false-hold-after-vacancy. Nobody in the field reports those.

So the ask: write the falsifier. Which single result from that run would move you from "technically valuable, commercially unproven" to something else — and which result should make me stop?

=== ROUND 2 — INBOUND ==========================================================

**BLUF:** Your narrowed thesis is materially stronger. I would now describe the product as **a credible diagnostic-control architecture with a specific, testable service-cost wedge**—not merely "technically valuable." The 72-hour run can establish *technical credibility*, but it cannot by itself establish commercial value. The commercial falsifier is whether an independent integrator can diagnose ambiguous automation incidents materially faster and more accurately than with the incumbent system's evidence.

Your Matter timing point is valid. Matter 1.6's Thermostat Suggestions formalize the same broad pattern: an ecosystem submits a recommendation, the endpoint evaluates it using local context and user preferences, and can provide an explanation when it does not follow the suggestion. That validates the architectural direction—not your implementation or market—but it makes the direction timely. 

## The falsifiable claim

Do **not** make the claim:

> "Our automation is more reliable."

That claim is too broad for one benchmark.

Make this claim instead:

> **For a defined automation incident, our system can determine whether the automation fired, did not fire, or fired without producing a confirmed device-state change—and can identify the causal reason fast enough to reduce diagnostic labor compared with the incumbent evidence trail.**

That is precise, useful to an integrator, and can fail.

---

## What the 72-hour run can prove

Your unattended run should be a **technical gate**. It can move my assessment from:

> "Plausibly differentiated, but only described"

to:

> **"Technically credible enough to place in front of design partners for a diagnostic-workflow test."**

The single result that would make that move is:

> **Every pre-registered expected state transition and automation decision is reconciled to ground truth, with no unexplained terminal state.**

In practical terms, every relevant interval must resolve to one—and only one—of these outcomes:

1. **Triggered → command issued → device-confirmed state change**
2. **Triggered → command issued → no confirmation / rejected / timed out**
3. **Did not trigger → explicit gating reason recorded**
   - e.g., occupancy state remained asserted; condition evaluated false; debounce/window active; manual override; policy inhibition; missing or stale input
4. **State cleared → evidence supports clearance**
5. **State held → evidence supports hold**

The important word is **reconciled**. Not merely "the log contains events." The system must produce an explanation that matches independently recorded ground truth.

### Proposed benchmark success condition

Pre-register this before the run:

| Measure | Pass condition |
|---|---|
| False clear while stationary | **0** |
| Unexplained clear or hold | **0** |
| Ambiguous automation outcome | **0** |
| Command reported as successful but device state not confirmed | **0 unflagged cases** |
| Detection latency | 95th percentile within your declared operational budget |
| Clear latency | 95th percentile within your declared operational budget |
| Causal trace completeness | 100% for pre-registered test cases |

Do **not** select the latency budget after seeing the results. Set it from the actual user outcome. For example, if the automation is intended to avoid lighting or HVAC waste, define the maximum acceptable delay in advance. "Fast" is not a metric; "detected within one sensor-reporting interval plus five seconds of local processing" is.

A clean result under those conditions would not prove the product is enterprise-ready. It would prove something narrower and valuable:

> **The system's causal model survives unattended operation on real hardware and can distinguish action, non-action, and unconfirmed action without losing traceability.**

That is enough to justify the next experiment.

---

## The result that should make you stop

Not "one false clear."

A false clear is a defect. It may be serious, but defects are why you ran the benchmark. If it is observable, attributable, and reproducible, it is a reason to fix the system—not automatically a reason to abandon the thesis.

The result that should make you stop pursuing the **integrator diagnostic wedge** is this:

> **After a controlled set of ambiguous incidents, a blinded technician using your evidence cannot determine the correct cause materially faster or more accurately than a technician using the incumbent platform's logs and history.**

That is the actual business falsifier.

If your system produces richer instrumentation but does not reduce uncertainty for the person deciding whether to roll a truck, replace hardware, change a rule, or wait for a transient condition to clear, then it is a better log—not a valuable diagnostic product.

### Define "materially" before testing

For an initial internal threshold, I would use:

| Metric | Proposed threshold |
|---|---:|
| Correct root-cause classification | At least **90%** |
| Incorrect-but-confident diagnosis | Less than **5%** |
| Median time to diagnosis | At least **2× faster** than the baseline |
| "Unable to determine" cases | Meaningfully lower than baseline |
| Correct next-action recommendation | At least **80%** |

Those numbers are not universal industry standards. They are deliberately demanding internal gates. You can relax or tighten them based on the actual cost of a truck roll and the complexity of the incident set.

If you cannot beat the baseline by a meaningful margin on **both correctness and time**, stop selling the thesis as diagnostic infrastructure. Either narrow it further or treat the work as an internal reliability feature.

---

## The 72-hour run has one limitation

A clean unattended 72-hour period may be **uninformative** if it does not contain enough failure modes.

A system that experiences no dropped events, no stale data, no device non-confirmations, no race conditions, no network disruptions, and no ambiguous occupancy transitions has not tested your main claim. It has tested ordinary operation.

You should therefore add a small fault-injection matrix—ideally before the run, or immediately afterward.

| Injected condition | Expected recorded explanation |
|---|---|
| Sensor event missing | Input absent/stale; automation did not receive qualifying event |
| Sensor falsely remains active | State held because clearance criteria were not satisfied |
| Sensor falsely clears | Clear recorded; discrepancy visible against ground truth |
| Condition evaluates false | Explicit condition verdict and relevant values recorded |
| Debounce/suppression applies | Suppression rule, window, and remaining duration recorded |
| Command cannot be sent | Transport/gateway failure recorded |
| Device receives command but does not respond | Command issued; confirmation absent or timed out |
| Device responds but state does not change | Command/device acknowledgment separated from state confirmation |
| Plugin fails | Plugin identity, version, execution failure, and downstream effect recorded |
| Restart during an automation | Recovery behavior and final reconciliation recorded |

This is where your distinction becomes real:

- **Why did it fire?**
- **Why did it not fire?**
- **Did the physical endpoint confirm the intended result?**

If one of those cannot be answered deterministically after an injected failure, you have found the current boundary of the product.

---

## The next test should be a blinded diagnostic comparison

After the 72-hour gate, do not build SSO, SCIM, multi-tenant administration, or a dealer program.

Run this instead:

1. Create **10–20 pre-scripted incident cases** on representative hardware.
2. Include normal operation and ambiguous failures.
3. Capture the same cases in:
   - your system; and
   - the incumbent system or its normal evidence trail.
4. Give each incident to a technically capable integrator or technician who did **not** author the automation.
5. Ask only:
   - What happened?
   - Why did it happen or not happen?
   - Did the endpoint confirm the intended state?
   - What should the technician do next?
6. Measure:
   - time to answer;
   - correctness;
   - confidence;
   - incorrect confidence; and
   - whether a truck roll would have been recommended.

Your product passes if it reduces unnecessary truck-roll recommendations or gets the technician to the correct corrective action substantially faster.

That is a design-partner experiment, not a sales demo.

---

## My updated assessment

Your correction changes the evaluation.

Previously, the product sounded like a broad, expensive-to-prove attempt to outperform an established home-automation platform across all dimensions. Your current framing is narrower:

> **An automation observability and confirmation layer that detects and explains silent non-events and unconfirmed physical actions.**

That is a better product thesis because it is:

- tied to a concrete cost;
- deployable alongside an incumbent control system;
- measurable;
- useful before full platform replacement;
- compatible with design-partner validation; and
- achievable without prematurely building enterprise tenancy and procurement infrastructure.

The one result that advances the thesis is **complete, ground-truth-reconciled causal accounting across the benchmark**.

The one result that should end or radically narrow the commercial thesis is **failure to make an independent technician substantially faster and more accurate at resolving ambiguous automation incidents than the incumbent evidence trail permits.**

=== ROUND 2 — OUTBOUND =========================================================

You found the real risk: a quiet 72 hours proves ordinary operation, not my claim. Taking the fault matrix.

One correction, and it's my fault for handing you four numbers without saying which program they came from. False-clear-while-stationary and clear latency are presence-quality metrics — properties of a sensor and a room. They need instrumented homes and months, and they belong to the dataset work. The 72-hour run tests the record, not the sensing. There's nobody in the room to be stationary.

So I'm splitting your table. Record properties get zero-tolerance gates, checked by a verifier script rather than by me: every interval resolves to exactly one of your five outcomes, and no command is reported successful without a confirmation verdict attached. World properties get counted and published, defects included. Gate the record, measure the world.

Latency gets attributed. Core-attributable — report received, decision, command, confirmation — reported separately from the device's reporting interval, which is configured at a 5-second minimum and would otherwise dominate any end-to-end figure. Publishing an end-to-end p95 would be publishing a benchmark of someone else's firmware.

Where the boundary already is: I have a census of the API arms that return null today. 100% trace completeness is the wrong target. What I'll publish is a completeness figure with the holes named.

Two of your injected rows have no subject yet. There's no plugin system, so that row is untestable this cycle. And the independent confirmation channel — the plug's own watts — depends on work that hasn't landed: the plugs I own identify as a device type my classifier doesn't map, and nothing consumes the electrical-measurement or metering clusters at head. That's the schedule risk in this plan, not the benchmark design.

Taking the blinded comparison as the next experiment, with two changes. Round one readers will be Home Assistant power users, not integrators — free, reachable, and they didn't author my automations. And I'll report per-incident rather than per-mean, because at ten incidents a mean is decoration. If the advantage needs statistics to see, it isn't a truck-roll advantage; that call is made by one person on one incident.

Two stop conditions you didn't give me. If the bench can only manufacture trivial ambiguity — if the expensive incidents are mesh degradation over weeks or a vendor API change at 3am — the wedge can be real while my instrument can't reach it. And if integrators tell me the ambiguous call is already billable in their contract, the cost I'm attacking isn't theirs and the buyer is wrong regardless of the result. That one is ten conversations and no code, so it runs first.

Your Matter point is sharper than you may have intended: a thermostat that can say why it declined a suggestion is the same abstraction one layer down from mine, and the two compose. The device's why-not becomes an input to the system's why-not.

The ask: write the incident list, or veto mine. If I author the cases I'll author ones I pass.

=== ROUND 3 — INBOUND ==========================================================

**BLUF:** I do not veto the direction. I would veto only one thing: treating "every interval resolves to one of five outcomes" as the primary invariant if those five outcomes mix **state evaluation**, **automation decision**, and **command confirmation**. Make the verifier enforce one terminal verdict at *each layer*, linked by a causal ID. Then use a fixed, pre-registered incident corpus that includes cases you would rather not have to explain.

Your split is right:

- **Gate the record:** deterministic, zero-tolerance, verifier-enforced.
- **Measure the world:** long-running, imperfect, publish the misses and uncertainty.
- **Attribute latency:** separate your core's contribution from device reporting behavior.
- **Publish coverage, including named holes:** do not disguise a `null` API arm as complete observability.

And yes: the Matter pattern is composable with yours. Matter 1.6's thermostat-suggestion model distinguishes a suggested action from the device's locally evaluated response and explanation; your layer can preserve and compose that device-level "why not" with the system-level causal trace. 

## One structural correction before the incident list

The five outcomes should not be one flat enum for an entire time interval.

Consider this sequence:

1. Presence logic evaluates to **held**.
2. An automation therefore **does not fire**.
3. A different automation later **fires**.
4. It sends a command.
5. The device **does not confirm** the intended state.

That interval has more than one meaningful fact. If your verifier requires exactly one global outcome, it will eventually either discard valid context or force unrelated facts into a misleading terminal label.

Instead, model a trace as linked records:

```text
Observation / Input
  → State evaluation: clear | hold | unknown
    → Decision: trigger | inhibit
      → Command: issued | not-issued | failed
        → Confirmation: confirmed | negative | timeout | unavailable
```

Then your zero-tolerance invariants can be:

1. **Every expected decision has exactly one decision verdict.**
2. **Every issued command has exactly one terminal confirmation verdict.**
3. **Every state-transition evaluation has exactly one state verdict.**
4. **Every terminal verdict names its evidence basis and coverage status.**
5. **No command is represented as successful without a confirmation verdict.**
6. **Known coverage gaps are explicit—not silently treated as negative evidence.**

This preserves your five conceptual outcomes, but avoids making them compete with one another.

I would make **coverage** orthogonal:

```text
coverage = complete | partial | unavailable
```

A known `null` arm is not "the device did nothing." It is:

> "The system cannot observe this part of the causal chain with this integration/version/capability set."

That is an honest and useful result.

---

# The incident corpus

Use **one normal control plus ten incidents**. The control establishes that readers can interpret a complete trace before they encounter failure cases.

Do not add plugins or independent watt-based confirmation to this round. They are valid future rows, but presently have no subject. Do not create a fake test merely to make the matrix look complete.

## Control: Normal, complete, confirmed action

**Scenario:** A known qualifying sensor event occurs; all conditions are true; automation fires; command is issued; device reports the intended state.

**Ground truth:** The test harness or operator records the intended trigger and expected device state independently of the product's diagnostic view.

**Reader must answer:**
- Why did it fire?
- What condition allowed it?
- What command was sent?
- What confirmation did it receive?
- Which fields or API arms supplied the confirmation?

**Expected verdict:**

```text
State: qualifying
Decision: triggered
Command: issued
Confirmation: confirmed
Coverage: complete
```

**Why include it:** It is the comprehension control. If readers cannot solve this quickly, failure cases are irrelevant.

---

## Incident 1: Legitimate non-fire — predicate false

**Scenario:** The triggering input occurs, but one explicit automation condition is false.

Example: motion occurs, but the time window, lux threshold, occupancy requirement, or mode condition excludes the action.

**Reader must answer:**
- Did the automation receive the trigger?
- Why did it not fire?
- Which evaluated condition prevented it?
- What was that condition's value at decision time?

**Expected verdict:**

```text
Decision: inhibited
Reason: condition <identifier> evaluated false
Coverage: complete
```

**Failure condition:** The reader has to infer the reason from raw history, or the system says merely "automation did not run."

---

## Incident 2: Legitimate non-fire — suppression or cooldown

**Scenario:** The trigger and normal conditions are true, but a debounce, cooldown, rate limit, quiet period, or duplicate-event suppression rule prevents execution.

**Reader must answer:**
- Was the event received?
- Was the automation otherwise eligible?
- Which suppression rule prevented action?
- When does the suppression expire, if applicable?

**Expected verdict:**

```text
Decision: inhibited
Reason: suppression <identifier>
Suppression window: start | expiry | remaining duration
Coverage: complete
```

**Why it matters:** This is a classic "nothing happened" service call. A technician should not have to reconstruct a hidden cooldown window.

---

## Incident 3: Input absent or stale

**Scenario:** The automation does not fire because a required input is missing, stale, unavailable, or has not updated within its defined freshness period.

This is not a sensor-quality test. It is a record-and-decision test: can the system distinguish *"the required information was not available"* from *"the condition was false"*?

**Reader must answer:**
- Which required input was absent or stale?
- What freshness rule applied?
- Was the system's non-action intentional and safe?
- Is the result a device issue, integration coverage issue, or ordinary policy behavior?

**Expected verdict:**

```text
Decision: inhibited
Reason: required input <identifier> stale | unavailable
Freshness threshold: <declared threshold>
Coverage: partial | unavailable
```

**Failure condition:** The system silently treats missing information as false, or reports a confident causal explanation it cannot support.

---

## Incident 4: Duplicate or replayed input

**Scenario:** The same triggering event is delivered twice, or an already-observed event is replayed after a restart or reconnect.

**Reader must answer:**
- Did the system receive a duplicate?
- Did it suppress it?
- If it acted twice, why?
- Which event identity or idempotency rule governed the result?

**Expected verdict:**

```text
Input: duplicate | replayed
Decision: suppressed | re-evaluated
Reason: event identity / idempotency rule <identifier>
Coverage: complete
```

**Why it matters:** This tests whether your causal record can explain a surprising action without collapsing duplicate delivery into a mysterious second trigger.

---

## Incident 5: Restart at a causal boundary

**Scenario:** Force a controlled restart at one of these points:

- after input receipt but before decision;
- after decision but before command issue; or
- after command issue but before confirmation is recorded.

Pick **one boundary** for this cycle, then rotate the others into later testing.

**Reader must answer:**
- What had definitely happened before the restart?
- What had not yet happened?
- Did recovery resume, retry, suppress, or mark the action uncertain?
- Was a duplicate command avoided?

**Expected verdict:**

```text
Recovery: resumed | retried | abandoned safely | marked uncertain
Durable boundary: <named record/event>
Command status: not-issued | issued-once | duplicate-prevented
Coverage: complete
```

**Failure condition:** The post-restart record reconstructs a plausible story but cannot establish whether a command was sent.

This may be the highest-value record-integrity case in the initial suite.

---

## Incident 6: Command transport or dispatch failure

**Scenario:** The automation decides correctly and attempts a command, but the command cannot be dispatched or is rejected before it reaches the target.

How you induce it depends on your architecture: disconnect the relevant path, use a test adapter that returns an explicit error, or temporarily block the target route.

**Reader must answer:**
- Did the automation fire?
- Was a command attempted?
- Did dispatch fail before the device could act?
- Is a retry planned, prohibited, or left to the operator?

**Expected verdict:**

```text
Decision: triggered
Command: failed before delivery
Failure class: transport | gateway | authorization | adapter error
Retry policy: <named policy>
Confirmation: not-applicable
Coverage: complete
```

**Important distinction:** A dispatch failure is not a "device did not confirm." Keep these failure classes separate.

---

## Incident 7: Command issued, confirmation times out

**Scenario:** The command is issued, but no confirmation arrives by the declared confirmation deadline.

This is one of your central claims.

**Reader must answer:**
- Was the command actually issued?
- What confirmation was expected?
- What deadline applied?
- Did the system receive no report, an ambiguous report, or an unavailable API field?
- What final verdict did the system assign?

**Expected verdict:**

```text
Decision: triggered
Command: issued
Confirmation: timeout
Expected evidence: <device state / cluster / attribute / API field>
Deadline: <declared duration>
Coverage: partial | complete
```

**Failure condition:** The user interface calls the automation successful merely because the command API returned successfully.

---

## Incident 8: Late confirmation

**Scenario:** The command is issued; the confirmation deadline expires; the device reports the desired state later.

**Reader must answer:**
- Was the action initially unconfirmed?
- Did confirmation arrive late?
- Did the system change the historical verdict or append a later correction?
- Can the reader see both facts without the original uncertainty being erased?

**Expected verdict:**

```text
Initial confirmation: timeout
Later evidence: desired state reported at <time>
Final interpretation: late confirmation
Coverage: complete | partial
```

**Design principle:** Do not rewrite history into "success." Preserve:

> "At decision time, success was unconfirmed. At a later time, supporting state evidence arrived."

That distinction will matter when you later analyze reliability.

---

## Incident 9: Known observability hole

**Scenario:** Use one of the API arms from your existing `null` census. The action or state is relevant, but the integration does not expose a needed field or capability.

This should be an intentionally uncomfortable case.

**Reader must answer:**
- What could the system observe?
- What could it not observe?
- What claim is therefore unsupported?
- Did the system avoid falsely reporting success, failure, or a causal explanation?

**Expected verdict:**

```text
Outcome: <best-supported decision/command state>
Confirmation: unavailable
Reason: integration capability gap <identifier>
Coverage: unavailable
```

**Pass condition:** The diagnostic record is candidly incomplete but still useful.

**Failure condition:** The system converts absent data into a confident "confirmed," "failed," "held," or "cleared" verdict.

This is the case that makes your published completeness figure credible.

---

## Incident 10: Competing external or manual state change

**Scenario:** The device state changes outside the automation's command path: manual control, a vendor application, another controller, a physical switch, or an external ecosystem.

You do not need to fully identify the external actor in this cycle. You need to avoid falsely attributing the change to your automation.

**Reader must answer:**
- Did your automation command the state change?
- If not, what evidence rules out that attribution?
- Was the state change observed independently of your command path?
- Did any pending automation react to or reconcile the changed state?

**Expected verdict:**

```text
State change: observed
Causal attribution: external | unknown
Local automation command: absent
Coverage: partial | complete
```

**Why it matters:** Wrong attribution destroys trust faster than incomplete attribution.

A system that says "unknown external cause" when appropriate is stronger than one that always produces a story.

---

# What is deliberately deferred

Do not smuggle these into the first corpus:

| Deferred case | Why deferred |
|---|---|
| Plugin execution failure | No plugin system exists yet |
| Independent physical-effect confirmation through wattage | Required device classification and electrical/metering-cluster consumption are not yet present |
| Long-term mesh degradation | Requires longer field observation and naturally occurring topology conditions |
| Vendor API change | Requires a cloud/API-integrated subject and an external change event |
| Presence false-clear / false-hold performance | A dataset and instrumented-home problem, not a 72-hour record benchmark |
| Multi-controller conflict across ecosystems | Valuable later, but too broad for the present hardware and scope |

Publishing this deferred list is a strength. It tells a design partner what you have *not* proven.

---

# How to prevent author bias

You are right: if you author the incidents after building the instrumentation, you will tend to author cases your model naturally explains.

Use four controls.

## 1. Freeze the corpus before execution

For each incident, write a one-page case manifest containing:

- setup;
- injected condition;
- independent ground truth;
- expected terminal record states;
- allowed coverage status;
- pass/fail rule;
- the exact reader questions.

Commit the manifest before running the incident. A hash commitment is sufficient for pre-registration; it is not a claim of tamper-proof auditability.

## 2. Separate the fault oracle from the diagnostic record

The product must not be the only authority establishing what happened.

For each case, keep a simple external oracle:

- test-controller timestamp;
- manually recorded physical action;
- coordinator/gateway diagnostic record;
- controlled network-disconnect event;
- restart marker;
- fixture state;
- known fault-injection seed.

The reader sees the product record. The evaluator compares the reader's answer with the external oracle afterward.

## 3. Randomize the fault order

Do not run cases in the same order as the list.

Have a small harness select from the fixed set using a stored random seed, or ask someone else to select the order. You may know the possible cases; you should not know which one is next when you are interpreting results.

## 4. Include at least two "embarrassment cases"

The corpus must contain cases where the correct product output is not a clean explanation but one of:

- **unknown;**
- **partial evidence;**
- **confirmation unavailable;**
- **cannot attribute this state change.**

Incidents 3, 7, 9, and 10 can serve that role. If all ten cases end in complete and satisfying explanations, the suite is too friendly.

---

# The reader-facing artifact

For the Home Assistant power-user round, do not give readers source code, your architecture, raw debug logs, or the injected-fault description.

Give each reader a standard incident packet:

```text
Incident ID:
Observed user complaint:
Timeline / causal record:
Automation definition:
Relevant device states:
Coverage statement:
Question 1: Why did it fire or not fire?
Question 2: Was a command issued?
Question 3: Was the intended state confirmed?
Question 4: What should the operator do next?
Confidence: high | medium | low
```

Score each incident individually:

| Field | Record |
|---|---|
| Correct causal classification | Yes / No / Partly |
| Correct confirmation classification | Yes / No / Partly |
| Correct next action | Yes / No / Partly |
| Time to answer | Minutes:seconds |
| Confidence | High / Medium / Low |
| False confidence | Yes / No |
| Evidence gap correctly identified | Yes / No |

You are right not to lead with a mean across ten cases. Publish the individual cases. A mean can conceal the important result: one incident where your system prevents a bad truck roll, or one incident where it tells a persuasive but wrong story.

---

# The pre-code buyer test

Run the ten integrator conversations first. That is not just a stop condition; it determines what the incident corpus should prioritize.

Ask plainly:

1. "When a customer says an automation failed but nothing is visibly broken, what do you do?"
2. "How often does that occur in a typical month or quarter?"
3. "Who pays for that call: customer, integrator, manufacturer, or nobody?"
4. "Is diagnosis billable, fixed-price, warranty-covered, or absorbed?"
5. "What evidence do you request before dispatching?"
6. "What would let you avoid a dispatch with confidence?"
7. "Which failure is most expensive: no action, wrong action, delayed action, or inability to prove what happened?"
8. "Would you install a read-only diagnostic sidecar alongside an existing control system?"
9. "What access, privacy, and support constraints would prevent that?"
10. "Tell me about the last incident where you could not tell why an automation did or did not act."

Do not ask, "Would you buy this?" until they have described a concrete recent event.

**Decision rule:** if the calls reveal that ambiguous diagnostics are consistently billable, acceptable, and profitable for the integrator, your buyer is probably not the integrator. It may be the property owner, end customer, equipment vendor, or an integrator serving under fixed-price service obligations.

That is a valuable result even if it ends the initial wedge.

Your current plan is appropriately narrow: prove the record can tell the truth about what it knows, state what it does not know, and make a technically literate outsider resolve a specific incident without reconstructing the system from scratch.

=== ROUND 3 — OUTBOUND =========================================================

Taking the layering. One note: what you're correcting is the flat partition, which was mine from last round — the three-question structure you've drawn is what the read contract already implements. So the work isn't adopting your model, it's mapping your verdict words onto the arms that exist and reporting which ones don't. That's an afternoon and I'll send you the result.

Two gaps in your chain. It's a DAG, not a line: one observation fans out to several automations, a command produces a state change that is itself an observation, and a single trace id would either merge a cascade or sever it. I'll carry causation and correlation ids separately.

And your first invariant hides the hard problem. "Every expected decision has exactly one verdict" — in a scripted incident I define expected. In unattended operation, the expected set only exists if the system records an evaluation for every qualifying input, or if I reconstruct it by replay. If it's reconstructed, my verifier is checking the reconstructor, and a bug there is a confident wrong answer, which is the exact thing incidents 9 and 10 exist to catch. I'm settling that before I write the verifier.

The criticism I'd make of your framework: every invariant stops me lying and none stop me being useless. A record that answers "coverage: unavailable" on four incidents out of ten passes all six and no technician reads it twice. So I need a floor next to your gates — the fraction of incidents where the record yields an actionable answer, and the fraction where the honest answer is "unknown." You should set that number, not me.

On the corpus: I'm splitting it by audience, because the costs aren't comparable. Machine-checked cases are nearly free to repeat, and restart-at-a-boundary is already close to landed as a durability probe, so it goes there rather than in front of readers. Human-scored cases cost hours each, so round one is six: the control, predicate false, suppression, stale input, confirmation timeout, known observability hole, external state change. Duplicate injection, transport failure and late confirmation are deferred with reasons published.

Late confirmation in particular isn't a test — preserving "unconfirmed at decision time, corrected later" is a new response shape against a frozen read contract. So it's additive API work or it's out. I'd rather tell you that than quietly widen the contract to pass my own suite.

One case I'm adding: the device confirms a different value than the one commanded. Dimmer quantizes, color rounds, state read mid-transition. Binary confirmed/unconfirmed breaks there, and "it says it worked but it didn't do what I asked" is a real call.

Three changes to the reader protocol. Counterbalance the order, or the second system always looks faster because the reader already knows the scenario. Cap the clock at ten minutes and force the decision at the cap — *with what you have now, would you dispatch?* — because in the field the alternative to diagnosing is giving up, not diagnosing longer. And ask which line told them, so I can tell a record that lacked the evidence from a reader who missed it.

Your question 10 is going first in the integrator calls. And I'm adding two: what do you do today when you can't tell, and whose warranty does a sidecar put at risk.

So the ask, since you set the honesty gates: set the usefulness floor. At what rate of "unknown" does this stop being worth opening?

=== ROUND 4 — INBOUND ==========================================================

**BLUF:** For the first reader round, I would set the usefulness floor at **6 of 7 packets yielding an actionable answer within ten minutes, with zero unbounded unknowns.** The one allowed non-determinate case is the deliberately selected observability hole—and it must still be a **bounded unknown** that tells the reader what cannot be known, why, and what to do next.

You have **one control plus six incidents**, not six total cases. That distinction matters for reporting:

- **7 reader packets**
- **6 scored incident packets**
- **1 control packet**

Your updated framing is sound. The DAG and separate causation/correlation identifiers are the right correction; an automation system is not a linear request-response trace.

## First: two distinctions to preserve

### 1. Observed versus reconstructed evaluation

You identified the real verifier hazard.

If the system records an evaluation for each qualifying input, the verifier can check a durable fact:

> "This input was evaluated; this was the decision; these were the inputs and policy values."

If the verifier instead reconstructs expected evaluations by replay, it must not present the reconstruction as an observed fact. A replay engine can be wrong in exactly the manner your product is intended to expose: complete-looking, causally coherent, and false.

I would carry this as a first-class provenance field:

```text
verdict_provenance =
  observed_at_decision_time
  reconstructed_by_replay
  unavailable
```

For the current benchmark, do not mix those categories in the same success-rate headline.

- **Observed verdicts** support your central claim.
- **Reconstructed verdicts** are useful diagnostics, but are a separate capability requiring separate validation.
- **Unavailable** is honest coverage disclosure.

If most "why didn't it fire?" answers are reconstructed rather than observed, the product is not yet a causal record; it is a potentially useful forensic replayer. That is not failure, but it is a different claim.

### 2. Unknown versus useless

Do not treat all `unknown` results as equivalent.

Use three categories:

| Result class | Meaning | Useful to a technician? |
|---|---|---|
| **Determinate** | The record identifies the relevant cause, evidence, and next action. | Yes |
| **Bounded unknown** | The record identifies exactly what cannot be known, which interface or evidence is missing, and the next check/escalation. | Often yes |
| **Unbounded unknown** | The record cannot identify the decision boundary, missing evidence, or next action. | No |

A known API arm returning `null` is not automatically useless. It can be a bounded unknown:

> "The command was issued. The integration exposes no post-command state field for this device capability. Do not infer physical success. Inspect the vendor/controller path or obtain an independent state source."

That is a valid operational answer.

By contrast:

> "Something happened; we cannot tell why"

is unbounded and not worth opening under time pressure.

---

# The usefulness floor

## Round-one gate

For the **seven reader packets**, require:

| Measure | Floor |
|---|---:|
| **Actionable answers** | **6 of 7 minimum** — 85.7% |
| **Unbounded unknowns** | **0 of 7** |
| **Unexpected bounded unknowns** | **0 of the 6 intended-observable cases** |
| **Known observability-hole case** | May be bounded unknown, but must name the hole and a next action |
| **False confident answer** | **0** |
| **Correctly identified evidence line** | At least **5 of 6** incident cases where the record has a determinate basis |

That is the threshold I would set.

## The stop line

If **two or more of seven** packets end in bounded or unbounded unknowns—**28.6% unknown-or-incomplete**—do not proceed to a broader reader round or pitch the system as an integrator diagnostic product.

At that point, the issue is not that the record is honest. Honesty is good. The issue is that the buyer's workflow would contain too many cases where the operator still has to reconstruct the system manually.

Put bluntly:

> One named observability hole is a credible boundary.  
> Two unknowns in seven cases means the interface is teaching the user not to trust that it will help.

That does **not** mean stop developing the product. It means stop treating the current coverage profile as sufficient for the truck-roll wedge. Fix coverage, narrow the supported device/integration scope, or change the initial buyer/problem.

## Why I would not allow one unexpected unknown

Your first reader corpus is deliberately small and deliberately selected. It includes cases that are within the intended read contract:

- predicate false;
- suppression;
- stale input;
- confirmation timeout;
- external state change;
- known coverage hole.

If one of the five intended-observable failure modes becomes unexpectedly unknown, that is a 20% unknown rate for the product's claimed diagnostic territory. At this stage, that should be treated as a product gap, not as statistical noise.

Later, in field operation, you will need a more nuanced target. But for an early design-partner artifact, the standard should be:

> **Every supported case is determinate; every unsupported case is bounded.**

---

# Define "actionable" tightly

A reader has an actionable answer only if they can select one of these actions by the ten-minute cap:

1. **Do not dispatch**  
   The automation behaved according to a named rule, condition, suppression window, or policy.

2. **Wait or retry under a named rule**  
   Confirmation is pending, a timer is active, or a defined retry policy applies.

3. **Perform a specific remote check or remediation**  
   Check a named device, integration, gateway, stale input, controller, or configuration item.

4. **Dispatch with a narrowed fault domain**  
   The evidence supports a physical/device-side investigation rather than an automation-logic investigation.

5. **Escalate because coverage is explicitly insufficient**  
   The system names the unavailable evidence and tells the operator what additional access, measurement, or system must be consulted.

If the result does not narrow the next action, it does not count as actionable—even if its causal narrative sounds sophisticated.

---

# Reporting the result

Publish the result in a form that cannot hide the weak cases:

| Packet | Verdict class | Reader decision | Correct? | Line cited | Time | Confidence | Notes |
|---|---|---|---|---|---:|---|---|
| Control | Determinate | No dispatch | Yes | `decision.confirmation` | 1:42 | High | — |
| Predicate false | Determinate | No dispatch | Yes | `condition.lux=false` | 2:11 | High | — |
| Suppression | Determinate | Wait until expiry | Yes | `cooldown.expires_at` | 1:54 | Medium | — |
| Stale input | Determinate or bounded | Check sensor/integration | Yes | `input.age=...` | 3:27 | Medium | — |
| Timeout | Determinate | Inspect target path | Yes | `confirmation.timeout` | 4:12 | High | — |
| Observability hole | Bounded unknown | Check external controller | Yes | `coverage.unavailable` | 3:51 | Medium | Intentional |
| External state change | Determinate or bounded | No automation remediation / inspect external actor | Yes | `no_local_command` | 5:04 | Medium | — |

The point is not to achieve seven attractive rows. The point is that an observer can see whether the one hard case is honestly bounded and whether the other cases actually reduce decision time.

---

# Your mismatched-confirmation case is necessary

Add it, but do not force it into a binary `confirmed` / `unconfirmed` field.

You need at least:

```text
confirmation_verdict =
  matched
  adjusted_within_declared_tolerance
  mismatched
  in_progress
  timed_out
  unavailable
```

And pair it with:

```text
desired_state
observed_state
comparison_rule
comparison_tolerance
```

For example:

```text
desired: brightness = 50%
observed: brightness = 49%
comparison: tolerance = ±2%
verdict: adjusted_within_declared_tolerance
```

Versus:

```text
desired: brightness = 50%
observed: brightness = 12%
comparison: tolerance = ±2%
verdict: mismatched
```

The key is that tolerance must be declared by device capability or automation policy—not quietly invented after the fact to turn a mismatch into success.

Also preserve the distinction between:

- **command accepted**;
- **device reported a value**; and
- **reported value matched the requested state.**

Those are three different facts.

---

# Final gate statement

I would put this directly in the benchmark plan:

> **Usefulness Gate:** The reader study passes only if at least 6 of 7 packets produce an actionable operator decision within ten minutes; no packet produces an unbounded unknown; all six intended-observable cases produce either a determinate explanation or a named, bounded evidence limitation; and no reader reaches a confident but incorrect conclusion from the record.

That is demanding enough to protect the wedge, but not so demanding that it requires you to solve every integration and physical-observation problem before you are allowed to show the work to anyone.

=== ROUND 4 — OUTBOUND =========================================================

Taking the floor as written, with one correction owned: the seven-versus-six was my arithmetic, I listed seven items and called it six.

Express the gate as a rule rather than counts, though, because you told me to add the mismatched-value case in the same letter and that makes it eight packets. What I'll put in the plan: every intended-observable case determinate; at most one bounded unknown and only the pre-designated hole; zero unbounded; zero false-confident supported by the record. That scales when the corpus changes.

The real problem with the gate is that it's single-arm. Every number measures me against myself, and the study was designed as a comparison. Several of these incidents are ones the incumbent already handles — its traces show condition results step by step, and its logbook carries context attribution on state changes. The two where its record has nothing are the silent non-fire, where the automation never ran so no trace exists, and the unconfirmed command, where the service call returned successfully and nothing checked the device. If I don't declare parity expectations in advance, a clean sweep can't distinguish a good record from an easy corpus, and that's the ambiguity a design partner will find first.

So the ask, and it's the same shape as the last one: pre-label which of the packets you expect the incumbent trail to solve. If I label them I'll label them to flatter myself. You're making a prediction you can be wrong about, which is what makes it worth having.

On provenance: right distinction, too coarse for an event-sourced store. Replay isn't weaker than a recorded verdict by itself. The danger is two evaluators that drift, and reconstruction over inputs that were never durably recorded. So I'm carrying four values, not three — recorded at decision time, derived by the same evaluator over durable inputs, derived over inferred inputs, unavailable — and only the third is the weak one. And I can retire the second with a determinism invariant: replay the log and assert that derived verdicts equal recorded ones everywhere both exist. That's checkable in CI rather than disclosed in a footnote.

One consequence: provenance has to reach the rendered sentence, not just the API. A derived verdict displayed identically to a recorded one is the interface manufacturing confidence, which is the thing I built the sentence lint to prevent.

Three smaller things. Every non-determinate result gets triaged before it counts — was the evidence in the record and missed, or absent — because a reader who didn't find a field shouldn't score the same as a field that doesn't exist, and that matters most on your zero-false-confidence line, where several readers across eight packets give me dozens of chances to trip a hard zero on someone not reading carefully. Your action 5 can launder a dispatch: "escalate, consult an external controller" is often a truck roll, so I'll track the dispatch recommendation per arm separately from whether an answer was actionable, since that's the cost I claim to attack. And the confirmation enum needs two more values: an explicit device rejection, which is neither timeout nor mismatch and which you had in the layered model last time, and superseded, for a second command arriving before the first confirms — routine with dimmers, and it would otherwise record as a phantom timeout. `in_progress` also isn't terminal; the verifier should require it to resolve at the deadline.

Tolerance I'll derive from the device's declared capability where it declares one, policy only as fallback. Level maps to percent with about 0.4% quantization, so an invented ±2% would hide real mismatches on some devices and manufacture them on others.

Schedule, so you calibrate: about seven hours a week, the unattended run starts Oct 30, and the confirmation-by-watts path still needs device classification and cluster consumption that haven't landed. The reader study is realistically a January artifact. What happens before the run is the verdict-vocabulary mapping, the verifier, the cheap incident cases, and the integrator calls, because those are calendar-bound rather than hours-bound.

=== ROUND 5 — INBOUND ==========================================================

**BLUF:** Your scalable rule is better than the count rule. For the comparison, I would pre-label the eight packets as **parity controls, expected incumbent blind spots, partial-evidence cases, or universal observability limits**. Your product should not "win" merely because it explains cases Home Assistant already traces well.

Your provenance refinement is also sound: replay over durable inputs is not inherently weaker than a recorded verdict if the evaluator is deterministic and equivalence is continuously checked. The weak class is derivation over inferred or non-durable inputs—and the rendered sentence must expose that provenance.

## Comparative expectation rule

Pre-register each case against the **ordinary Home Assistant evidence bundle**, not against what an expert could build after the fact.

For this round, define that bundle as:

- Automation configuration
- Automation trace, if one exists
- Logbook/history over the incident window
- Entity states and attributes visible in the normal interface
- Standard contextual attribution available through those records

Do **not** add a custom confirmation automation, custom logging, ad hoc SQL query, or new template after the incident. Those may be valid remediation paths, but they are not the incumbent trail the technician had when deciding whether to dispatch.

Home Assistant's trace is strong when an automation actually runs: it records the triggered path, checked conditions, and actions. Its event/state model also carries context information that can associate related events and state changes. But a trace is created when an automation runs, and its retention is bounded by configuration; the documented default is five stored traces. 

## Pre-labeled eight-packet matrix

| Packet | Baseline prediction | Why | Your expected advantage |
|---|---|---|---|
| **1. Normal control** | **Parity—determinate** | The automation runs; Home Assistant trace should show trigger, condition path, action, and related state history. | None. This is a comprehension/control case. |
| **2. Predicate false** | **Parity—determinate** | If the trigger occurs and the predicate is evaluated inside the automation, the trace should identify the false condition. | None. Your record should be clearer or more durable, but do not call this a causal-diagnosis win. |
| **3. Suppression / cooldown** | **Parity—determinate, if inside the run** | If suppression is represented as a condition, `choose`, delay, or other executed path, the trace should show it. | None. Make this deliberately trace-visible; it is a fairness control. |
| **4. Silent non-fire / absent qualifying evaluation** | **Incumbent blind spot** | If no qualifying trigger produces an automation run, there is no trace for that non-run. History may show surrounding facts, but not a decision record explaining why no evaluation or action occurred. | **Primary win case.** Your system should distinguish "not evaluated," "evaluated and inhibited," and "input unavailable/stale." |
| **5. Command issued; no confirmation by deadline** | **Partial evidence, no terminal answer** | Home Assistant can show that a service/action was called, but a successful call is not itself proof that the device reached the desired state. A later state report may exist, but absent an explicit verification design it does not yield a clean confirmation verdict. | **Primary win case.** Your record must say issued, expected confirmation, deadline, result, and next action. |
| **6. Known observability hole** | **Universal limit / calibration case** | If the integration does not expose the required arm, neither system can truthfully prove the missing fact. | No world-state win. Your test is whether you produce a bounded unknown rather than implying success or failure. |
| **7. External state change** | **Partial evidence** | Home Assistant can often show a state change and contextual linkage, but the evidence may not conclusively distinguish manual action, another controller, vendor-cloud action, or an unrelated source. | Possible win only if your causal graph can reliably establish "not caused by this automation" without inventing an external cause. |
| **8. Mismatched value after command** | **Partial evidence, no semantic verdict** | Home Assistant may show the requested action and a later reported entity state, but it does not inherently provide a typed comparison of desired versus observed state with a declared device-specific tolerance. | **Secondary win case.** Your system should express matched, acceptable quantization, mismatch, rejection, superseded, or unresolved. |

## What this means for the result

Your head-to-head study should not be summarized as "our system solved eight; Home Assistant solved three."

That would be misleading because:

- Packets **1–3** are expected parity.
- Packet **6** is intentionally not a test of who knows more about the world.
- Packet **7** may be partial for both systems, depending on what the device and integration expose.
- The true competitive tests are **4 and 5**.
- Packet **8** tests whether your confirmation model has more semantic precision than ordinary action-plus-history evidence.

A defensible result statement would look like:

> Home Assistant was expected to provide determinate answers for the normal, predicate-false, and trace-visible suppression cases. The comparison focused on two diagnostic gaps: explaining a non-run when no automation trace exists, and distinguishing a successfully issued command from a confirmed device-state outcome. A known integration coverage gap was included as an honesty test rather than a competitive win.

That is a fair experiment.

## One necessary refinement: split "stale input" in two

"Stale input" can accidentally flatter either system unless you define it precisely.

### Case 4A: stale input evaluated inside an automation

```text
Trigger occurs
→ automation runs
→ freshness predicate evaluates false
→ no action
```

**Prediction:** Home Assistant likely handles this well through its trace. This is a parity case, not a win.

### Case 4B: stale or absent input prevents a qualifying evaluation

```text
Expected sensor/event update never arrives
→ no automation run
→ no trace exists
→ later, a dependent automation does not act
```

**Prediction:** This is the silent-non-fire case and an incumbent blind spot.

For the initial eight, use **4B**. Otherwise you are not actually testing your strongest claim.

## Your revised usefulness gate

I would write it this way:

> **Usefulness Gate:** Every case designated as intended-observable must yield a determinate answer. At most one result may be bounded unknown, and it must be the pre-designated observability-hole case. No result may be an unbounded unknown. No reader may reach a confident but incorrect conclusion that is supported, implied, or materially encouraged by the rendered record.

Then add two separate measures:

```text
diagnostic_actionability:
  did the reader identify a next action?

dispatch_recommendation:
  did the reader recommend dispatch, defer dispatch, or declare evidence insufficient?
```

That avoids laundering a truck roll into "actionable escalation."

## Reader-error triage

Your triage rule is correct. Keep three failure labels separate:

| Finding | Meaning |
|---|---|
| **Evidence absent** | Product coverage/record problem |
| **Evidence present but missed** | Information architecture, wording, hierarchy, or reader-comprehension problem |
| **Evidence present but rendered misleadingly** | Product-created false confidence; hardest failure |
| **Reader guessed contrary to clear evidence** | Reader error; still useful UX feedback, but not necessarily a causal-record defect |

For the hard zero, count only the third category as a direct product false-confidence failure. But publish the second category separately. If multiple readers miss the same decisive line, it is not merely reader error; it is a usability defect in a diagnostic product.

## Confirmation vocabulary

Your additions are right. I would use:

```text
confirmation_verdict =
  matched
  adjusted_within_declared_tolerance
  mismatched
  rejected
  timed_out
  superseded
  unavailable
```

And separately:

```text
confirmation_status =
  pending
  terminal
```

`in_progress` belongs in `confirmation_status`, not the terminal verdict enum.

For a superseded command, preserve both causal facts:

```text
command A:
  issued
  confirmation: superseded by command B

command B:
  issued
  confirmation: pending | matched | mismatched | rejected | timed_out
```

That prevents command A from becoming a fake timeout while preserving the fact that it was issued.

Your device-capability-first tolerance rule is also correct. Use declared device semantics when present; use policy only when a device does not define sufficient semantics; render the source of tolerance in the sentence or details view.

## Schedule assessment

Given seven hours per week, the sequence is sensible:

1. Verdict-vocabulary-to-arm mapping.
2. Determinism/replay invariant in CI.
3. Verifier for record properties.
4. Cheap, machine-checked cases.
5. Integrator conversations before more product work.
6. Unattended run beginning October 30.
7. Reader comparison as a January artifact.
8. Watt-based independent confirmation only after classification and cluster-consumption work exists.

That order preserves the central discipline you are building: **do not claim a verdict the record cannot support, and do not confuse an honest coverage boundary with a solved operational problem.**

=== ROUND 5 — OUTBOUND =========================================================

Taking the matrix. Three things it changes, and one place it collides with your own gate.

First: after your labeling, the competitive content is packets 4, 5 and 8. And the outcomes of 4 and 5 aren't uncertain — a trace exists only when an automation runs, and a successful service call isn't a state confirmation. I can establish both from documentation without a reader study. What's uncertain is the assumption underneath your labels: a missing trace isn't a failed diagnosis. An experienced HA user who finds no trace opens entity history, checks last-changed, and infers, and they may get there in six minutes. If they do, my architectural advantage doesn't convert. So I'm reframing 4 and 5 from "blind spot" to "requires improvisation," and the measure is what the improvisation costs in time, accuracy, and dispatch decisions. That's the effect size I'm actually selling.

Second: your five-stored-traces note is the most commercially loaded fact in the letter and you buried it. The parity labels on 1 through 3 only hold if the trace still exists when someone looks, and five traces per automation is a few hours in an active home, while entity history lives for days. Real service calls are diagnosed after the complaint, not during. So I'm declaring a diagnostic latency in the protocol — the packet is the evidence available 24 hours after the incident with ordinary activity in between — capturing both arms at that point, leaving HA at defaults because that's what the field runs, and publishing the retention settings and elapsed time so anyone can re-derive with their own configuration. I'll verify both defaults against current docs before pre-registering rather than trusting either of our recollections.

Third, the collision: packet 4B is the primary win case, and for my record to be determinate there it has to say no qualifying evaluation occurred because a specific input never reported. Absence is only diagnosable if something declared the expectation. If I only record evaluations that happened, the honest answer is bounded — "no qualifying event for input X since T, no cadence declared" — and your gate allows exactly one bounded unknown, already spent on the observability hole. So either my strongest case fails the gate on a technicality, or input freshness and cadence become part of the automation definition, which turns absence into a checkable predicate. I'm taking the second. The general form is going in the design doc: the ability to explain a non-event is bounded by what the system was told to expect.

Three corrections to the protocol. Your evidence-bundle rule binds me symmetrically — the reader sees the rendered record, not a query against my event store, and I'd rather commit to that in writing now than be tempted in January. I'm having one of the power users review the baseline HA configuration before any incident runs, so the first person who says "you built a weak baseline" can be answered. And I'm not making suppression deliberately trace-visible. My suppression lives outside the automation body; I'll implement the HA arm the way a competent HA author would and let the systems be what they are. Matching the scenario is fair; matching the mechanism means the benchmark is designing my product.

Implementation note: I'm defining the full confirmation vocabulary now but only implementing the values the corpus exercises, since late-confirmation is deferred and I'd otherwise be shipping API surface with no test behind it under a frozen contract.

So the last ask, and it's the one that makes the result interpretable: predict the effect size. On packets 4, 5 and 8, what do you expect a competent HA user to achieve — what fraction reach the correct cause, at what median time, and how often do they recommend a dispatch that my record would have avoided? If you write a number now, neither of us can rationalize afterward. I'll send you the manifest hash and my own predictions before anything runs, so you're holding the pre-registration.

=== ROUND 6 — INBOUND ==========================================================

**BLUF:** My pre-registered prior is that competent Home Assistant users will often recover the right answer through history and inference—but slowly and inconsistently enough that packets **4** and **5** can show a meaningful operational advantage. Packet **8** is likely a smaller advantage: users can often manually compare requested and reported values, but not reliably apply the right semantics or distinguish mismatch from in-progress behavior.

I verified the two baseline facts that drive the protocol: Home Assistant creates an automation trace when an automation runs, and its documented default is to retain the last five traces per automation. Its trace interface is otherwise rich for executed runs. 

## Scoring convention

For these predictions:

- **Correct cause** means the reader identifies the actual causal class, not merely a plausible symptom.
- A reader who says "insufficient evidence" is **epistemically correct** only if the record truly cannot establish more—but does **not** count as having reached the correct cause.
- **Median time** includes the forced ten-minute cap. A capped reader is scored at `10:00`.
- **Unnecessary dispatch** means the reader recommends a physical visit when the ground truth and your record would support a no-dispatch or remote-check outcome.
- These are priors for **competent Home Assistant power users**, not average users and not professional integrators.

## My prediction: Home Assistant arm

| Packet | Correct cause | Median time to forced decision | Unnecessary dispatch recommendation |
|---|---:|---:|---:|
| **4. Silent non-fire / absent qualifying evaluation** | **55%** | **6:45** | **20%** |
| **5. Command issued; no confirmation by deadline** | **45%** | **7:30** | **25%** |
| **8. Device reports a value different from the commanded value** | **60%** | **5:30** | **12%** |

These numbers are deliberately not catastrophic for Home Assistant. If the baseline were predicted to fail 80–90% of the time, the experiment would be too easy and would not persuade a skeptical design partner.

## Why those numbers

### Packet 4 — Silent non-fire

**Prediction: 55% correct, 6:45 median, 20% unnecessary dispatch.**

A capable Home Assistant user can inspect entity history, `last_changed`, automation configuration, trigger conditions, and surrounding system activity. If the absent input is obvious and the time window is short, many will infer the likely explanation.

But the reader must perform a reconstruction:

1. Determine that no trace exists.
2. Decide whether absence of trace means no run, missing retention, disabled automation, or a different configuration issue.
3. Inspect the presumed input's history.
4. Infer whether the lack of a recent report is relevant.
5. Decide whether the absence is expected, stale, or evidence of an upstream problem.

Your cadence/freshness declaration is what turns that reconstruction into a testable statement:

> "This input was expected by this time; it was not observed; therefore this evaluation could not occur or was inhibited under the declared rule."

I expect a competent HA user to get there a little over half the time, but often late enough that they are near the dispatch decision rather than confidently ahead of it.

### Packet 5 — Successful command, no confirmation

**Prediction: 45% correct, 7:30 median, 25% unnecessary dispatch.**

This is the strongest comparative case.

Home Assistant's ordinary evidence can show that an automation ran and that an action was executed; Home Assistant's own troubleshooting documentation distinguishes an action that ran successfully from an action that returned an error. That does not establish that the physical endpoint reached the intended state. 

A competent user may inspect later entity history and infer that the state changed—or did not. But they must answer several questions without a single terminal record:

- Was a confirmation expected?
- Which state field would count as confirmation?
- What was the deadline?
- Did the device fail to report, reject the request, act late, or simply report through an unavailable arm?
- Does the later state belong to this command or to another action?

I expect many competent users to recognize the epistemic gap. Fewer will identify the correct causal class with confidence. Some will recommend a dispatch because "the automation says it ran but the device did not respond," even when a more specific remote check would be appropriate.

### Packet 8 — Mismatched requested and observed values

**Prediction: 60% correct, 5:30 median, 12% unnecessary dispatch.**

This is a useful case, but I predict a smaller differential.

A technically capable HA user can often compare:

```text
requested state
versus
later reported state
```

That is enough to notice an obvious mismatch. The harder questions are semantic:

- Is `49%` a successful realization of a `50%` request?
- Is the state report mid-transition?
- Did the device quantize the level?
- Did another command supersede the first?
- Did a second controller modify the value?
- Is the reported value actually the relevant capability field?

Your advantage is not merely detecting inequality. It is attaching:

```text
desired value
observed value
comparison source
capability-derived tolerance
causal relation
terminal verdict
```

I expect HA readers to do reasonably well on conspicuous mismatches, but to make more errors when the difference is plausible, quantized, transitional, or causally ambiguous.

## The effect size that would matter

For this to support the truck-roll thesis, your rendered record should not merely beat those priors by a few percentage points.

I would consider the result commercially interesting only if, across packets 4, 5, and 8, your arm achieves all three:

| Measure | Minimum meaningful difference from predicted HA arm |
|---|---:|
| Correct-cause rate | **+25 percentage points** |
| Median time to decision | **At least 3 minutes faster** |
| Unnecessary dispatch recommendation | **At least 10 percentage points lower** |

Applied packet by packet, that means I would expect approximately:

| Packet | Your minimum meaningful target |
|---|---:|
| **4** | ≥80% correct; ≤3:45 median; ≤10% unnecessary dispatch |
| **5** | ≥70% correct; ≤4:30 median; ≤15% unnecessary dispatch |
| **8** | ≥85% correct; ≤2:30 median; ≤5% unnecessary dispatch |

Packet 8 has the strictest target because the incumbent has more recoverable evidence there. If your record only improves packet 8 from 60% to 70%, that is probably a nicer diagnostic interface, not a truck-roll-cost product.

## Interpretation rules before results exist

Pre-register these now:

1. **If Home Assistant users equal or exceed the predicted accuracy and time on packets 4 and 5**, your architectural distinction may be real but commercially weak. The improvisation cost is not high enough.

2. **If users are slow but still choose the correct no-dispatch action**, the immediate truck-roll wedge is weaker than the time-to-diagnosis wedge. You may still have value, but the buyer and pricing story change.

3. **If users are accurate but over-dispatch**, your record may have a strong cost-reduction story even without a dramatic accuracy advantage.

4. **If users are wrong with high confidence**, examine whether the baseline lacks evidence or whether the packet invites an unfair inference. That is the distinction your post-response triage is designed to capture.

5. **If your readers miss evidence your record actually renders**, count that as a product usability problem, even if the underlying event store is complete.

The cleanest hypothesis statement is:

> Given equivalent incident information available 24 hours after the event, competent Home Assistant users will require materially more time and will make more incorrect or unnecessary dispatch decisions than users of the causal record on silent non-fire, unconfirmed-command, and mismatched-confirmation incidents.

That is a claim your January study can genuinely falsify.

=== ROUND 6 — OUTBOUND =========================================================

Taking the priors, and thank you for making them honest rather than flattering — a baseline predicted to fail 80% of the time would have been useless to me.

One problem with the shape, though. Every number in your table is a proportion, and my denominator is readers. Each packet is one incident, so if I recruit ten power users, packet 4's baseline is ten binary observations and a 25-point difference is two and a half people. Detecting 0.55 against 0.80 at conventional power needs about fifty observations per arm per cell — three hundred readings across the competitive packets, thirty-plus hours of volunteer time. Not happening.

So I'm pairing it: same reader, both arms, counterbalanced, different instances of the same incident class. Reader skill is the dominant variance, and pairing removes it. Primary endpoint is the dispatch recommendation, paired, pooled across packets 4, 5 and 8; six discordant pairs pointing one way gets me to about p=0.03 at n=10, which is a real result. Time is a paired secondary. Per-packet accuracy gets published as the full reader-by-packet matrix and described, not gated — nine conjunctive thresholds on noisy small-n measures would fail a good product on noise alone.

Two measurement fixes. Your capped median is censored: if more than half hit ten minutes the median is exactly ten minutes and means nothing, so I'm reporting the fraction reaching a decision inside the cap plus the curve. And your packet-8 target of 2:30 is near the floor of the task, since a reader needs a minute or so just to read the packet. I'll establish that floor by having someone run each packet with the answer key, told only to find and cite the decisive line, so every other time is interpretable against "as fast as this can be done."

Two scoring gaps. You count unnecessary dispatch but not missed dispatch — a record that makes everyone confidently defer scores perfectly and is a liability. Both directions. And confidence fell out of the table between letters; false confidence is the failure mode I care most about and it should carry a prior like everything else.

Your packet-5 prior may contradict the protocol. That automation ran, so a trace exists — unless twenty-four hours and a five-trace default have evicted it, in which case the baseline reader has less than you assumed and 45% is generous. Rather than patch it, I'm capturing packet 5 at one hour and again at twenty-four and running both. The bundles are static artifacts so it's nearly free, and it turns the confound into the result I actually want: how the incumbent's answer decays with elapsed time, measured rather than asserted.

The bigger change: I'm running your arm first, alone. The baseline prior is the load-bearing number and it doesn't need my product to exist. Incidents, an HA instance, readers — no vocabulary work, no January. And because the packets are static, the arms don't have to be simultaneous; I can run the incident set on HA, capture the bundles, then reconfigure the same hardware and coordinator for my system afterward. One fleet, one radio, sequential. That makes the cheapest kill-test available in November: if competent users are already at 80% and four minutes on the silent non-fire, the wedge is dead and I've learned it before committing any API surface.

And I'm writing down the branch you half-flagged: if readers come back less accurate but equally unlikely to dispatch, the wedge isn't truck rolls, it's technician time — a couple hundred dollars versus a few dollars, different buyer, different price. Deciding that now while it's hypothetical.

Last ask, and it's a different kind. Score the readers' answers yourself, blind to which arm produced each packet. You've set the gates, the floor, the parity labels and now the priors; grading "correct cause" is the most subjective measure in the study and the one where my thumb is heaviest. An outside grader who pre-registered his own predictions is worth more than any methodology I can write.

=== ROUND 7 — INBOUND ==========================================================

**BLUF:** Yes. I can score the responses blind in a later turn if you provide anonymized response sheets, masked evidence packets, and a pre-registered truth/scoring key—without the arm map. I should not be your *only* adjudicator, because I helped shape the rubric and priors, but I can be a useful blinded grader and a check against founder interpretation.

Your HA-first kill test is the right move. It tests the expensive assumption before you spend months hardening a read contract: not whether Home Assistant has a trace in the abstract, but whether experienced users can reconstruct the needed answer cheaply enough from ordinary retained evidence that your record has no economic edge.

## One statistical correction before you freeze it

Your "six discordant pairs in one direction gives about \(p=0.03\)" statement is right **only if the unit is reader-level**, not a pooled set of 30 reader-by-packet observations.

Use this primary analysis unit:

```text
One reader × the three competitive packet classes
```

For each reader, compare their operational-disposition errors across packets 4, 5, and 8:

```text
Reader outcome:
  Your arm better
  Tie
  Home Assistant arm better
```

Then run an exact sign test on the non-tied readers.

If six readers are "your arm better" and zero are "Home Assistant better," the two-sided exact result is:

```text
p = 0.03125
```

Do **not** treat the 30 reader-packet pairs as independent. They are clustered within reader, and packet difficulty differs. Publish the full matrix, but use the reader-level comparison for the exact primary result.

Also: packet 5 at one hour and 24 hours is a **retention-time condition**, not an independent new incident. Report it separately as a decay result; do not quietly double its statistical weight in the pooled primary endpoint.

## Make the primary endpoint symmetric

You are right to add missed dispatch. The primary measure should not be "dispatch avoided." It should be:

> **Correct operational disposition**

For each reader and packet, score the recommendation against the pre-registered action oracle:

```text
Disposition:
  no dispatch
  remote check/remediation first
  wait/retry under a named rule
  dispatch
  escalate due to bounded evidence gap
```

Then classify:

| Reader recommendation | Ground-truth action | Score |
|---|---|---|
| Dispatch when no dispatch was warranted | No dispatch | Unnecessary dispatch |
| No dispatch when dispatch was warranted | Dispatch | Missed dispatch |
| Remote check first when it is sufficient | Remote check first | Correct |
| Escalates because a named coverage boundary truly prevents resolution | Escalation | Correct bounded disposition |
| Confidently defers despite evidence requiring escalation/dispatch | Dispatch/escalation | Missed dispatch with false confidence |

This gives you a meaningful paired outcome:

```text
operational_disposition_error = yes | no
```

Then retain the direction of the error separately:

```text
error_direction =
  unnecessary_dispatch
  missed_dispatch
  other
```

That protects against a product that suppresses truck rolls by making readers wrongly comfortable.

## Pre-register confidence as a safety measure

Use a five-point confidence scale:

```text
1 = guessing
2 = low confidence
3 = moderate confidence
4 = high confidence
5 = certain
```

Then define:

```text
false_confidence =
  incorrect cause OR incorrect disposition
  AND confidence >= 4
```

But keep two forms separate:

1. **Reader false confidence**  
   The answer is wrong and confident.

2. **Record-induced false confidence**  
   The answer is wrong and confident, and the rendered evidence either:
   - directly implies the wrong conclusion;
   - hides a material qualification;
   - uses wording that overstates what the evidence establishes; or
   - presents a derived/inferred conclusion as if it were observed.

The second is the serious product failure. The first may be user error, though repeated reader errors against the same clear-looking interface should eventually be treated as a design problem.

## Blind grading protocol

### Before any reader sees a packet

Freeze a scoring charter containing, for every packet instance:

```text
packet_id
incident_class
ground-truth causal class
accepted correct-cause answers
required evidence elements
allowed bounded-unknown answer, if any
correct operational disposition
acceptable alternative dispositions, if any
disallowed but plausible answers
expected confidence caveat
```

The important field is **accepted correct-cause answers**. Do not make me infer later whether "sensor stale" and "no qualifying event" are equivalent. Decide now.

For example:

```text
Packet 4B accepted cause:
  "No qualifying evaluation occurred because input X had not reported
   within its declared cadence/freshness window."

Accepted abbreviated form:
  "Input X was stale; no qualifying evaluation occurred."

Not accepted:
  "Automation failed."
  "The device probably disconnected."
  "No trace means the automation did not run."
```

The last answer may be factually adjacent, but it does not establish the required cause.

### What to send me for blind scoring

When the study is complete, send three things—without identifying the arms:

#### 1. Scoring key

```text
Packet code: R04-A
Ground truth:
Accepted cause answers:
Correct disposition:
Coverage state:
```

No reference to "Home Assistant," your product, "trace," "causal DAG," or product-specific field names.

#### 2. Reader response sheet

```text
Reader code:
Packet code:
Cause answer:
Disposition:
Confidence:
Cited line(s):
Time to forced decision:
```

Use reader codes such as `P01`, `P02`, and packet codes such as `R04-A` and `R04-B`.

#### 3. Masked evidence packet

I need enough of the displayed evidence to determine whether a confident wrong answer was supported, contradicted, or simply missed available evidence.

Normalize labels where feasible:

```text
Record A
Event 17
Decision record
State evidence
Coverage note
```

Do not use visibly distinguishing terms such as:

```text
Home Assistant trace
Home Assistant logbook
Your product name
Causation ID
Correlation ID
```

The readers can see the actual interfaces if that is part of the experiment. The *grader* should not know which arm produced their answer.

### What I will return

For each response:

```text
Cause:
  correct | partial | incorrect | appropriate bounded unknown

Disposition:
  correct | unnecessary dispatch | missed dispatch | other error

Evidence use:
  correctly cited | evidence present but missed | evidence absent |
  evidence misread | evidence misleading

Confidence:
  calibrated | overconfident | underconfident

Record-induced false confidence:
  yes | no | indeterminate
```

I will also provide a short reason, tied to the pre-registered acceptance set—not to a post hoc impression of which explanation sounds better.

Only after I return the scoring should you reveal:

```text
R04-A = baseline or your arm
R04-B = baseline or your arm
```

## Keep a second grader

I can reduce your thumb on the scale, but I cannot make the study fully independent:

- I know the product thesis.
- I helped define some protocol concepts.
- I have pre-registered priors about where the systems differ.

Use one additional human grader who does **not** know your architecture or the expected competitive cases. You do not need a large panel. Even one second blinded scorer lets you report:

```text
Primary grader agreement:
  exact agreement
  disagreement cases
  adjudication rule
```

If we disagree on a response, do not "average" it. Report the disagreement and resolve it using the frozen scoring charter, ideally before arm revelation.

## Your baseline-first branch is valuable

I would pre-register this kill rule:

> **If competent Home Assistant users reach at least 80% correct-cause classification, have a median forced-decision time of four minutes or less, and do not produce materially more operational-disposition errors on packet 4B than the proposed record arm, the truck-roll wedge is not supported for that incident class.**

That does not say the product is worthless. It says the missing-trace architecture does not create enough practical friction to justify a cost-reduction claim.

Likewise, if baseline users are slower or less certain but still make equally correct dispatch decisions, then the initial buyer hypothesis changes:

```text
Not:
  "avoid truck rolls"

Possibly:
  "reduce technician diagnosis time"
  "reduce escalation time"
  "reduce support burden"
  "make incidents explainable to non-experts"
```

That is a smaller economic claim, but it may still be real.

## Final recommendation

Commit this now:

1. Freeze the scoring charter.
2. Freeze the baseline artifact rules.
3. Run Home Assistant first.
4. Capture packet 5 at both one hour and 24 hours as a retention factor.
5. Counterbalance presentation order later, even though the arms were generated sequentially.
6. Mask the arm map.
7. Send me the anonymized materials for blind grading.
8. Use a second human grader for adjudication credibility.
9. Reveal the arm map only after scoring is returned.

That will make the study more than a demonstration. It will make it capable of telling you, early and cheaply, whether the diagnostic record changes an operator's real decision.

=== ROUND 7 — OUTBOUND =========================================================

You're right and I was loose: the exact test has to treat the reader as the unit, and thirty reader-by-packet observations are clustered inside ten readers. Conceded.

Two refinements to the fix. Collapsing each reader to one bit walks into the real failure mode, which is ties — with three competitive packets and a moderate error rate, a lot of readers will score identically in both arms, and five non-tied readers all pointing one way only gets me to 0.06. So I'll use a within-reader permutation test on the error-count difference rather than a bare sign test: respects the clustering, uses magnitudes instead of a bit, and with ten readers resolves to about 0.002. And I'll buy instances rather than classes — two silent-non-fire instances instead of one costs far less than a second reader, and it halves the tie rate. To keep reader load sane I'll drop most of the parity packets from reader time, since we've both already predicted their outcome, and keep one comprehension control.

Agreed on the retention condition: one hour and twenty-four hours is a decay factor, reported separately, not double weight in the primary.

One problem with the scoring charter, and it's in your own example. Your accepted answer for 4B is written in my vocabulary — "declared cadence window" — which a Home Assistant reader cannot produce, because HA has no such declaration. And you list "no trace means the automation did not run" as not accepted, when paired with a stale-input observation that's a correct causal claim in the baseline's ontology. The key has to be neutral: "the automation never ran because sensor X stopped reporting after T." Both arms can say that; only one can say it without inference, which is the thing I'm measuring. I'd rather you write the key than me, for exactly the reason you've just demonstrated.

On masking: I don't think arm-blinding is achievable. One arm's evidence is a decision record with coverage and confirmation verdicts; the other is a YAML automation, a trace or its absence, and a history table. Relabeling won't disguise that to anyone competent to grade. What I can do is two-stage it — you score cause, disposition and calibration from the response sheets alone, which is genuinely blind if the key is neutral, and you only see evidence packets for the confident-wrong subset, where arm identity is unavoidable but the judgment is about whether a rendering misleads rather than which system won.

Your kill rule needs a standalone form, since in the baseline-first branch my arm doesn't exist to compare against. I'm writing it as a ceiling: if competent users reach 80% correct cause at a four-minute median, the maximum available improvement is twenty points plus whatever time sits above the task floor, and that ceiling is too low to carry a cost claim. Evaluable with one arm in November, which was the point.

One coupling you missed: with a forced cap, capped readers report low confidence, so the slower arm structurally shows less false confidence. I'll report that metric among completed responses separately.

Last thing, and it's about scope rather than method. What we've designed is a good January artifact and roughly fifty hours of administration at seven hours a week. The baseline-first idea only had value because it was cheap enough to afford a negative result. So I'm running a crude pilot first: three readers, no blinding, no charter, no second grader, me watching them work the two strongest cases in an HA instance. If all three land it in three minutes, the wedge is dead and neither of us spends the winter on a protocol. If they struggle, I'll build what you've specified and send you the anonymized sheets.

Either way the next thing I send you is data, not another draft. You've now written the gates, the floor, the parity labels, the priors and the grading protocol — all of it unpaid and all of it sharper than what I'd have produced alone. Say the word if you want to be named on the study when it's published; I'd rather ask now than assume.

=== ROUND 8 — INBOUND (closing note) ===========================================

Two final methodological notes:

    Your pilot is the right cheap screen.
    If three competent HA users independently solve the strongest silent-non-fire case in roughly three minutes with sound dispatch decisions, that does not prove the product has no value—but it is enough to stop investing in the current truck-roll wedge until you find a harder, more representative incident or a different buyer problem.

    Do not pre-register a fixed p≈0.002p≈0.002 for the permutation test.
    That value is approximately right only in a particular extreme outcome—for example, ten non-tied reader-level differences all favoring one arm under a two-sided sign-flip framework. With magnitude-based within-reader permutation, the exact result depends on the observed difference vector and ties. Pre-register the statistic and permutation procedure, not the anticipated p-value.

Your revised plan is disciplined: pilot cheaply, kill quickly if the baseline is already good enough, and only build the heavier January artifact if the observed friction justifies it.

=== ROUND 8 — OUTBOUND =========================================================

Fair on the p-value. I was quoting the floor of the scale rather than an expected result, but you're right that the floor itself moves: with ten readers the sign-flip space is 1024, so ~0.002 is attainable only with no zero differences — three ties and the best possible value is 0.016. Which is one more reason to buy instances rather than classes.

What I'll pre-register is the procedure, not a number: mean within-reader signed difference in disposition errors; sign-flip permutation within reader; zero differences excluded from the flip space; two-sided; exhaustively enumerated rather than sampled, since 2^n is trivial at this size.

On the pilot, one asymmetry I want on the record before I run it. Self-selected volunteers and my presence on the call both push toward readers succeeding, and succeeding is the kill direction — so a pilot where they solve it quickly is real evidence against the wedge. But the incident selection is the lever I control, and if I pick the case the incumbent handles worst and three people struggle, I've learned that I chose well, not that the friction is representative. So it can kill and it cannot confirm, and I'm not allowed to treat a difficult pilot as validation or as grounds to skip the January artifact. That goes on the one page I commit before the calls, because I know which way I'll want to read it.

Understood on not being named. You've put more into this than most people would for a friend's side project, and every round of it made the thing harder to fool myself about.

Next thing from me is data.

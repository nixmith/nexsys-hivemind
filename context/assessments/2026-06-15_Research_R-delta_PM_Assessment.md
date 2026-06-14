<!--
file: context/assessments/2026-06-15_Research_R-delta_PM_Assessment.md
purpose: PM assessment + disposition of the R-δ competitive ecosystem deep-dive return. Grades it, runs a verification ledger (spot-checks the load-bearing past-horizon claims), routes every mapped finding to its consuming lock point (app-bootstrap charter / M7 / crypto-backup lane / strategy / performance), surfaces the one genuine tension (field retry-demand vs our REC-162 anti-retry), banks the confirmations, and registers the §5 follow-up briefs.
audience: Nick, PM, the Track-2 app-bootstrap charter session, the M7.x sessions
state-type: assessment
status: COMPLETE 2026-06-15
grade: A-
return: homesynapse-core-docs/research/returns/2026-06-15_Research_R-delta_Competitive_Ecosystem_Architecture_Deep_Dive.md (rehomed from context/handoff/ this session)
brief: context/instructions/2026-06-15_Research_R-delta_Competitive-Ecosystem-Architecture_Deep-Dive_Brief.md
baseline: homesynapse-core HEAD 1eddd9a (M6 COMPLETE 4-of-4); watermark AMD-93; Doc 15 LOCKED.
-->

# PM Assessment — R-δ (Competitive Ecosystem Architecture Deep Dive)

## Grade: A-

A strong, decision-bearing return that hits the brief's deliverable squarely: it leads with the five things, holds the two-lens (mistakes/strengths) discipline, maps every finding to an AX axis + a consuming lock point + a confidence grade, mines primary sources (CVEs, official deprecation notices, maintainer statements, issue trackers, FTC/post-mortems), honors the LOCKED ground (no cloud, no DSL), respects the R-γ boundary (does not re-fight the envelope-tag question), and **declares its own connector-blind gaps and thin spots and turns them into six named follow-up briefs** — which is exactly the assess→follow-up loop the brief was built to feed. The minus: a cluster of load-bearing claims sits past the PM's reliable-knowledge horizon (May 2025) and the return's recency is a feature that needs spot-verification, not blind trust; one B-confidence vocabulary item (Z-Wave JS node-status strings) is corroborated indirectly by its own admission; and it surfaces one finding (retry demand) that **collides with a locked HomeSynapse anti-requirement** and must be adjudicated, not absorbed.

## Why A- (against the research-quality bar)

- **Two lenses, mapped, actionable.** Every major system carries both a cited mistake and a cited strength, each tied to an AX axis, a delta, and a lock point — not a generic survey. "HA has many integrations" never appears; "HA 2026.6 removed template syntax → automations silently fail, maintainer refused to fail-closed (GitHub Disc #3462) → add a definition-validation-at-load gate" does.
- **Primary-source discipline.** Maintainer "out-of-scope" statements, CVE advisories with CVSS + install-percentage, official shutdown notices with dates, FTC closing-letter analysis. Secondary/community sources are labeled and graded B.
- **Honest about its limits.** Connector-blind declared; the 18-call budget ceiling stated; the thin spots (SmartThings Edge internals, discontinued-ecosystem breadth, Ring/Wyze primaries, Z-Wave node-status verbatim) named and routed — not papered over.
- **It earns its confirmations.** The graveyard validates local-first by *mechanism* (cloud-gated first-run = brick), not by assertion; HA's template scar tissue validates no-DSL by *maintainer refusal to fix in place*.

## Verification ledger (load-bearing claims — spot-checked, not trusted)

The return's value is concentrated in recent (2025-2026) events past the PM's May-2025 horizon, so they were treated as claims-to-verify, not ground:

- **CVE-2026-34205 (HA host-network add-ons expose unauthenticated endpoints to LAN; CVSS 9.7; fixed Supervisor 2026.03.02) — VERIFIED this session** via independent web search (SentinelOne / CIRCL / cvedetails corroborate the ID, the 9.7, the host-network/Docker-bridge mechanism, and the 2026.03.02 fix). The headline-#2 bind-posture finding is real, not fabricated. This materially raises confidence in the return's other primary-cited CVEs.
- **Past-horizon, primary-cited, NOT independently re-verified this session (flag, do not block):** HA 2026.6 legacy-template removal + silent-fail (Jun 2026); HA Issue #134162 encrypted-backup hardware-migration key bug; Apple Home old-architecture EOL (Feb 10 2026); Thread 1.3/1.4 cert cutoff (Jan 1 2026); CVE-2023-27482 (CVSS 10.0, within horizon, consistent with prior knowledge). **None is decision-load-bearing in a way the underlying principle doesn't already carry** — loopback-default, auth-before-exposure, fail-closed-at-load, and backup-key-portability are all correct on first principles regardless of the exact CVE/issue numbers. Spot-confirm any of these before it is quoted *as a citation* in a charter or strategy doc.
- **Within-horizon, consistent with prior knowledge (accepted):** openHAB startlevels; HA automation modes (single/restart/queued/parallel, max, max_exceeded); HA continue_on_error; Z2M availability (active/passive) + Z-Wave JS alive/dead/asleep/awake; Z-Shave S0 downgrade (zero-key); Mirai (root/xc3511, Dyn ~1.2 Tbps); Revolv/Insteon/Wink/SmartThings-Groovy/Eufy mechanisms. No fabricated HomeSynapse internals (the return correctly limited itself to the LOCKED ground and flagged the rest as assumptions-to-verify).

**No fabrication found. The grade is A-, not A, because the recency that makes the return valuable also makes ~5 load-bearing claims unverifiable from the PM's own knowledge — verified the single highest-leverage one (CVE-2026-34205); the rest are flagged for spot-confirm-before-citation.**

## Disposition — routing every finding to its lock point (the deliverable)

### → App-bootstrap charter (Track 2)
- **AX-1 (auth/bind, SHARPENS C1/INV-SE-02):** loopback-default bind; LAN exposure is explicit opt-in; auth enforced at the router/middleware **before any path resolves** (canonicalize paths — the CVE-2023-27482 traversal lesson); treat **no** interface as "internal" (the `/internal/*`-outside-the-gate problem the converge already flagged); **zero-config must not leak** (HA's pre-auth username enumeration is the anti-pattern). These become explicit charter requirements on the C1 sub-milestone.
- **AX-2 (lifecycle, SHARPENS C9):** adopt **openHAB's numbered startlevel ladder** (00 framework / 10 bundles / 20 model / 30 state-restore / 40 rules-loaded / 50 engine-active / 70 UI) as the concrete model for `SystemLifecycleManager`'s phases — and **gate cipher activation + HTTP exposure to specific phases** (HTTP must not open before auth is wired; the cipher must activate before any sensitive read/write). This is the cleanest external template for the C9 reconciliation.
- **AX-2 (migration safety):** wire a **pre-migration snapshot + one-click rollback into lifecycle before any schema/chain change** (HA's auto-backup-before-update is the strength; Apple's destructive in-place Home-architecture migration is the anti-lesson). Bears directly on chain activation + the V-series migrations.
- **AX-9 + graveyard (auth brand):** zero-config must remain **authenticated** (Mirai = the default/shared-credential botnet); **no unauthenticated stream/media path ever** (Eufy's VLC-without-auth); and **verify no first-run/onboarding/cipher-activation step makes a network call** (Insteon's reset-needs-server brick vector) — a concrete charter check.

### → M7 (automation engine)
- **AX-5 (fail-closed-at-load gate):** add a definition-validation-at-load gate — an automation referencing an unknown trigger-ID/entity is **rejected and surfaced**, never loaded into a silently-dead state. This is consistent with AMD-89 E89-1 (empty `includedRoles` = load failure) and the Locked §6.1 reject-at-load class; generalize it to a first-class M7 loading contract.
- **AX-5 (bounded-cascade vocabulary):** HA's modes (single-default / restart / queued / parallel, `max`, `max_exceeded`) are the field-proven vocabulary — compare against our §6.7 storm machinery + AMD-91. **Notable confirmation: HA has NO dedicated loop detector** (Issue #115042 froze HA on a `repeat` loop) — **our AMD-91 `RunCausalChain` chain-membership cycle detection is ahead of the field.** Bank it.
- **AX-5 (per-action error policy):** HA `continue_on_error` is the deterministic alternative to a try/catch DSL — fold a per-action error-policy primitive into the M7.2 action model (compare AMD-90).
- **AX-8 (ReachabilityTrigger vocabulary):** model AMD-88's `ReachabilityTrigger` / our `Availability` on **Z2M active/passive + Z-Wave JS alive/dead/asleep/awake** — crucially distinguishing "battery device legitimately asleep" from "mains device dead" to avoid false-alarm triggers. **Action: confirm our `Availability` enum carries this granularity**; if it only has reachable/unreachable, that is an M7/integration gap.
- **AX-8 (Matter lesson):** the field's pain is poor *observability of failure* — ReachabilityTrigger + onboarding must surface explicit failure states, not silent guesswork.

### → Crypto / backup lane
- **AX-4 (backup-key portability — a real, near-term design input):** HA made encrypted backups mandatory and **stranded users** ("no way to restore… Nabu Casa does not store your key"; hardware-migration key bug #134162). **Design the machine-local-root → portable-recovery bridge now** — an exportable recovery artifact tied to crypto-shred scopes — *before* users accumulate an encrypted corpus. This is F2/F1-adjacent and belongs on the charter's `payloadCipher`-activation beat AND the backup/restore WU. It is the most actionable new crypto finding in the return.
- **AX-3 (honest threat-model + Z-Shave):** the machine-local-root posture must be **communicated honestly** (Eufy's "encrypted but…" trust collapse) — disk-theft protection is Tier-2 only; route the wording to strategy. Z-Shave's zero-key downgrade independently **validates our per-scope-DEK + counter-nonce design** and the "surface security downgrades loudly" stance.

### → Strategy
- **AX-7 (versioning/deprecation policy — escalation):** SmartThings-Groovy and HA's monthly breaking-change tax both show that **silently dropping a trigger/capability destroys user trust.** Commit a versioning + deprecation policy (stable trigger IDs — we have them via AMD-88 — plus a surfaced migration window) **before users author definitions** (the AMD-88/89 user-YAML lock-in is the moment this becomes irreversible).
- **AX-9 (trust brand):** "runs during internet outage + user-owned keys" is a sellable property (Hubitat's positioning) — route to the strategy layer.

### → Performance (persistence)
- **AX-6/AX-10:** bounded compaction tested on Pi-class storage; compaction/purge must never block the write path and must not need 2× storage headroom (HA Recorder's repack trap); minimize write amplification on the append-only path (SD-card wear). Route to the persistence/performance pins.

## The one genuine tension (ESCALATE — do not silently absorb)

**AX-5 "retry integration = gold demand evidence" vs our REC-162 anti-retry.** The return reads the popularity of HA's `retry` custom integration (`expected_state`/`retry_id`/`validation`/`state_grace`) as strong demand to "build expected-state verification + bounded retry INTO the action model." **HomeSynapse has an explicit anti-requirement (REC-162): no engine retry, no `command_retried` type.** These are not flatly contradictory — the demand splits in two:
- **Expected-state *verification*** (did the device actually reach the commanded state?) — HomeSynapse arguably already has this via the `Expectation` model (device-model) + AMD-90 confirmation semantics. *Likely satisfied; confirm.*
- **Bounded *re-issue* (retry)** — this is the part REC-162 forbids, on double-actuation-risk grounds. The retry integration itself guards double-actuation with `expected_state`, which weakens the original anti-retry rationale.

**Recommendation: do not overturn REC-162 on this evidence alone, but re-open it as an explicit M7.2 action-model design question** — "is the field's retry demand satisfied by Expectation + confirmation, or does a *guarded* (expected-state-gated, idempotent) bounded re-issue belong in the sealed model?" Escalate to Nick as a scope/strategy call; it is not the PM's to flip unilaterally.

## Confirmations to bank (locked choices the field's scar tissue validates)
- **No-DSL** (HA template silent-fail, maintainer refusal). **Local-first** (the entire graveyard, by mechanism). **Sealed trigger/condition/action model** (Node-RED spaghetti; Hubitat Rule-Machine power-user-only). **Per-scope DEK + counter nonce** (Z-Shave zero-key catastrophe). **Deterministic cycle detection** (AMD-91 ahead of HA's no-loop-detector). These are now externally corroborated, not just internally reasoned.

## Follow-up briefs registered (§5 → the next dispatches; PM-prioritized)
1. **Key-portability mechanics** (crypto/backup lane) — HIGH. Feeds the charter `payloadCipher` beat + the backup WU; the AX-4 stranding lesson is serious and near-term. *Recommend dispatch alongside R-γ.*
2. **Sensitive-data classification benchmarking** (strategy) — MED. Secondary input to F2; the **energy/erasure interviews are the primary instrument** (Thu/Fri), so this supplements, not blocks.
3. **SmartThings Edge/Rules API internals** (integration roadmap / M7 sealed-model comparison) — MED.
4. **HA loop-protection internals** (CORE spike) — LOW-MED (we are already ahead via AMD-91; nice-to-have for the governor's surfaced-vs-capped UX).
5. **Discontinued-ecosystem breadth + Ring/Wyze primaries** — LOW (diminishing returns; the load-bearing lessons are already extracted).

## Escalations to Nick
1. **The retry-vs-REC-162 tension** (above) — re-open as an M7.2 action-model design question; do not flip REC-162 silently.
2. **The versioning/deprecation-policy commitment** (AX-7) — decide before users author definitions; strategy/locked-decision-adjacent.
3. **Which follow-up briefs to dispatch** — recommend #1 (key-portability) now alongside R-γ; #2 supplements the interviews.

## Closeout actions (PM)
- Return REHOMED → `homesynapse-core-docs/research/returns/2026-06-15_Research_R-delta_Competitive_Ecosystem_Architecture_Deep_Dive.md` (from the messy-named `context/handoff/` drop).
- Side-research status: **R-δ → ASSESSED.** The charter-bound findings (AX-1/2/4/9) are inputs to the Track-2 app-bootstrap charter; the M7 findings (AX-5/8) ride the M7.x instructions; the rest route as tabled.
- **Not on the M7 critical path.** R-δ informs the app-bootstrap charter and sharpens M7 design beats; it blocks nothing.

## Commit message (handed to Nick — bang-free, quote-free; use git commit -F)
```
docs(assess): assess R-delta competitive ecosystem deep-dive (grade A-)

PM assessment + disposition of the R-delta return. Grade A-: two-lens,
primary-sourced, mapped to lock points, honest gaps -> six follow-up briefs.
Spot-verified the headline past-horizon claim (CVE-2026-34205, HA host-network
LAN exposure, CVSS 9.7, fixed Supervisor 2026.03.02) via web; flagged the
remaining 2025-26 claims for spot-confirm-before-citation; no fabrication.

Routed: app-bootstrap charter (AX-1 auth-before-exposure + loopback-default;
AX-2 openHAB numbered startlevels as the SystemLifecycleManager phase model +
pre-migration snapshot/rollback; AX-9 zero-config-still-authenticated, no
unauthenticated stream path, verify no network call in first-run/cipher-
activation). M7 (AX-5 fail-closed-at-load gate, HA modes vocabulary,
continue_on_error; AX-8 Z2M/Z-Wave reachability vocabulary for
ReachabilityTrigger). Crypto/backup lane (AX-4 design backup-key portability
NOW; AX-3 honest threat-model wording). Strategy (AX-7 versioning/deprecation
policy before users author). Performance (AX-6/10 bounded compaction, write
amplification).

Banked confirmations: no-DSL, local-first, sealed model, per-scope DEK, and
AMD-91 cycle detection is ahead of HA (which has no loop detector).

Escalations: the field retry-demand vs our REC-162 anti-retry tension (re-open
as an M7.2 action-model question, do not flip silently); the deprecation-policy
commitment; which follow-ups to dispatch (recommend key-portability now).

Return rehomed to research/returns/. R-delta -> ASSESSED. Not on the M7 path.

File: context/assessments/2026-06-15_Research_R-delta_PM_Assessment.md
```

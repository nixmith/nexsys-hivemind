<!--
file: context/handoff/2026-06-15_TRACK3_redteam-reversibility-audit_session_prompt.md
purpose: Track 3 — a fresh Cowork PM session run in ADVERSARIAL RED-TEAM mode. Its job is to try to BREAK the recent decisions (the R-α dispositions above all, plus the M7 AMD block, the crypto posture, FLATTEN type-residency, the encrypted-scope set) — hunting specifically for momentum-driven and ONE-WAY-DOOR (irreversible / costly-to-reverse) choices being baked in now that would propagate into debt or architectural mistakes. Output: a reversibility ledger + per-decision adversarial verdict + independent external-validation brief(s). Guards against the research/governance pipeline rubber-stamping its own momentum.
audience: PM (nexsys-project-manager hat), Nick
state-type: session prompt (adversarial review)
status: READY — paste into a fresh Cowork conversation. RUN THIS BEFORE (or feed it into) the Track-2 app-bootstrap charter, so the charter is built on red-teamed ground.
-->

# Track 3 — Red-Team & Reversibility Audit of the Recent Decisions

**You are the PM and most-senior architect (`nexsys-project-manager` hat), operating in ADVERSARIAL RED-TEAM mode.** Read this framing twice, because it inverts your usual stance:

**Your job is NOT to validate the recent plan. Your job is to try to BREAK it.** Treat every recent decision as a *claim under test*, not settled ground. You are explicitly guarding against a specific failure: that this project's fast research/governance pipeline has been **"going with the flow"** — adopting assumptions and architecturally-flawed, *irreversible* choices on momentum, which then propagate into technical debt and one-way mistakes. **You succeed by the number of genuine irreversible/high-cost risks you surface, not by confirming the plan.** Rubber-stamping is the failure mode. Confirmation is not the goal; *disconfirmation attempts* are.

**Do NOT defer to authority signals.** The R-α return was graded "A"; the converge said "M7 READY." Treat those as **hypotheses that may be wrong**, not as ground. Re-derive; challenge the framing; ask whether each was accepted because it was *correct* or because it *agreed with what we already wanted*.

## Step 0
Invoke `nexsys-project-manager`; run the freshness preflight (baseline: M6 COMPLETE 4-of-4, core HEAD `1eddd9a`; spine reconciled 2026-06-15; R-α assessed). Host Read tools authoritative; no Gradle; sandbox git quarantined.

**Read these as CLAIMS TO ATTACK, not ground to accept:**
- `context/assessments/2026-06-15_Research_R-alpha_PM_Assessment.md` + the raw return (`context/instructions/Prior-Art & Standards Survey…R-α…NEW-1….md`) — the rotate-DEK-on-restore call, the cause-discriminated read contract, the shred tombstone, the GCM-SIV-is-Tier-2 deferral.
- `context/audits/2026-06-15_core-review_CONVERGE_synthesis.md` — the "M7 READY" verdict, the two HIGHs, the app-bootstrap framing.
- The M7 AMD block (`design/amendments/AMD-88..93`) — the breaking changes (AMD-88 `triggerId`, AMD-89 `includedRoles`, AMD-91 `RunCausalChain`) and **AMD-92 FLATTEN type-residency**.
- Doc 15 (crypto) §3.4/§5/§6; the OQ-15-2 disposition (the `encrypted_scopes` set).

## The method — this is the spine of the session

**1. Build the REVERSIBILITY LEDGER.** Enumerate every consequential decision made or queued in roughly the last two weeks. For each, classify three axes:
- **Door type:** one-way (hard/impossible to reverse) vs two-way (cheaply reversible).
- **Cost-to-reverse:** cheap / costly / effectively irreversible — and *why* (e.g., "once written to the immutable log, the wire format/encryption is permanent for that corpus").
- **When it locks:** now / at-first-corpus-write / at-app-bootstrap / at-M7.1 / later.
Then **prioritize scrutiny on the one-way, irreversible, locks-soon cells.** Two-way doors get a quick "fine, reversible" and move on — spend the budget on the doors that don't reopen.

**2. For each high-priority (one-way) decision, run an ADVERSARIAL pass:** steelman the *opposite* choice; name the failure mode the current choice's advocates are under-weighting; state the *specific evidence that would change the call*; give a verdict — **PROCEED** (and the disconfirming evidence you considered) / **PAUSE-FOR-EVIDENCE** / **REVERSE-NOW-WHILE-CHEAP**. For a one-way door, the bar for PROCEED is high and must cite what you tried to disprove.

**3. Interrogate at least these named suspects (do not limit yourself to them):**
- **Crypto-agility / AES-256-GCM vs. GCM-SIV — the flagship one-way door.** M6.3 already shipped AES-256-GCM; the encrypted corpus begins accumulating the moment app-bootstrap activates `payloadCipher`. R-α parked GCM-SIV and committing-AEAD as "Tier-2." **Is that deferral momentum or evidence?** Changing the AEAD — or even adding a crypto-agility *algorithm/version tag* to the encryption envelope — is cheap **now** (corpus empty) and expensive-to-impossible once the corpus + hash chain exist. Does the current envelope (`payload_iv`/`dek_ref`) even carry an algorithm identifier, or is the AEAD choice implicitly hardcoded? If there's no version tag, **is adding one a now-or-never** that should be pulled into app-bootstrap/M6-hardening? This is the highest-value question in the session.
- **The cause-discriminated read contract + shred tombstone (NEW-1).** The crypto-shred *operation* is post-MVP. So: is NEW-1 **solving a post-MVP problem prematurely** and committing us to a contract (degrade-on-intended-shred + a tombstone event type + cause-carrying `DegradedEvent`) we might regret? Would a **flat fail-closed at MVP** (simpler, SQLCipher-style, no tombstone attack surface) be the lower-regret choice, deferring the degrade half until the shred operation actually ships? Attack the tombstone's un-forgeability claim harder than the return did.
- **rotate-DEK-on-restore as binding.** Does re-wrapping or re-encrypting old ciphertext on restore touch stored bytes and thus **break the chain_hash** (Doc 15 §5)? If rotate-on-restore implies re-encryption, the "chain stays valid through key change" assumption may not hold. Find the failure mode the return glossed.
- **AMD-92 FLATTEN type-residency.** Once events are persisted flattened (`RunId`→`Ulid`, `RunStatus`→`String`), the wire format is permanent for that corpus. Is FLATTEN right, or does it foreclose a future need (e.g., richer run lineage in payloads)? Reversibility verdict.
- **The M7 breaking changes (AMD-88/89/91).** Any of these premature or irreversible *before M7.1 has even run*? `triggerId`/`includedRoles`/`RunCausalChain` reshapes — is the construction-site-sweep-is-empty finding a reason they're safe, or a reason we're under-testing them?
- **The `encrypted_scopes` set `[identity, presence_personal]`.** Once written encrypted, a scope can't be retrofitted to plaintext and vice-versa. Is the set right? Is a now-or-never scope missing? (Note the dependency: the energy/erasure interviews bear on widening — flag, don't pre-empt.)
- **META — is the pipeline an echo chamber?** The same authors wrote the R-α brief, ran the assessment, and graded it. Did the brief's framing (the "cause-discriminated" sharpening, the embedded source companion) *steer* the return toward confirming our priors? Did "grade A" reward agreement? Identify any load-bearing claim accepted without independent verification (the assessment already flagged the June-2026 "wGCM" item as unverified — are there others?).

**4. The independent-validation spin-out.** For the load-bearing crypto/architecture calls where *internal* red-teaming is structurally insufficient — because we made them and we're biased — **author a fresh, explicitly-adversarial DOCS-Project brief** whose job is to **challenge** (not confirm) the decision with independent, web-grounded evidence. Name exactly which decisions warrant this (the crypto-agility one almost certainly does). Frame those briefs so the external reviewer is rewarded for finding the flaw, with the quote-back/evidence discipline of the standard research cycle.

## Output discipline
Lead with the **reversibility ledger** and a ranked **"re-examine before it propagates"** list. It is a *good and expected* outcome to conclude that most two-way doors are fine — do not manufacture alarm. But for every one-way door, the verdict must show its work: what opposite was steelmanned, what disconfirming evidence was sought, why PROCEED (if PROCEED). The most valuable possible output is catching **one** genuine reverse-now-while-cheap decision before app-bootstrap locks it.

## Deliverables
1. `context/audits/2026-06-15_redteam_reversibility-audit.md` — the ledger, the per-decision adversarial verdicts, the ranked re-examine list.
2. Any **independent-validation DOCS brief(s)** authored (e.g., a crypto-agility challenge brief) — saved to `context/instructions/`, ready for Nick to dispatch to a fresh DOCS conversation.
3. A completion report to Nick: the one-way doors found, the verdicts, what (if anything) to **PAUSE or REVERSE NOW**, and which briefs to dispatch. Flag anything that should gate the Track-2 app-bootstrap charter. Commit message handed over (`!`-free).

## Done-when
Every consequential recent decision is in the reversibility ledger with a door-type + lock-time + verdict; each one-way/irreversible decision has an adversarial pass citing the disconfirming evidence considered; the echo-chamber meta-check is done; the independent-validation brief(s) are authored (or "none warranted" is justified); the recommendation names what to pause/reverse and what gates the app-bootstrap charter. Success = we proceed knowing which doors are one-way, having genuinely tried to break the ones that don't reopen — not having confirmed our own momentum.

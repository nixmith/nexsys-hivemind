<!--
file: context/assessments/2026-06-15_M5-D_erasure-interview_RESCOPED_brief.md
purpose: The TIGHT, re-scoped erasure-interview ask handed back to Nick after the 2026-06-15 PM adjudication.
         Supersedes the run-instructions of the 2026-06-07 interview guide for the erasure (Track A) track:
         the AMD-86 re-open trigger is MOOT (M6 froze the write path in the correct encrypt-on-write posture);
         Track B (energy) is parked. This is what to still learn, how to recognize it, and the artifact to get.
audience: Nick (runs the interviews)
status: ACTIVE re-scope. Pairs with context/assessments/2026-06-15_M5-D_desk-research_PM_Assessment.md.
guardrail: a qualifying find prioritizes a POST-MVP shred-operation milestone; it is NOT an AMD-86 re-open and
           NEVER an AMD-86 / Doc 15 edit (formal pipeline only). Background calibrates; buyer past-behavior decides.
-->

# Re-scoped erasure interview ask (TIGHT)

## What changed (read once)
The original trigger ("re-open AMD-86 before M6 freezes the write path") is **moot** — M6 shipped, and it shipped **encrypt-on-write** for `[identity, presence_personal]` with per-scope keys, so **shreddability is already preserved**. The only thing still undecided is *when* the shred **operation** (the key-destruction + "prove it to an auditor" capability) ships — a recoverable, post-MVP scheduling call. So: **do not run a dedicated erasure-interview push.** Fold ONE probe into institutional conversations you're already having. **Skip the energy questions entirely (Track B is parked).**

## The one thing still worth learning (and it's a long shot — that's fine)
Does any **real, near-term buyer** have a **contracted, dated clause** requiring **verifiable per-scope/per-subject cryptographic erasure WITH a retained tamper-evident audit log**, that is **go/no-go to sign**? Desk research says this is **rare** (the contractual norm is "return or destroy + certify in writing"). Your honest prior is **NO**. The point is only to catch the one genuine exception (an early Care/HIPAA pilot, an EU institutional partner with a hard Art. 17 + audit clause) — because it would **prioritize the post-MVP shred-operation milestone**, not change anything already built.

Ask, in order, only if each opens the door:
- **A1 (past behavior):** "Last time a customer or regulator made you erase data — what exactly did you have to *prove*, and to whom? What artifact did they accept?" *(Real = names the regulator + the exact artifact. Hand-wave = "compliance reasons.")*
- **A2 (the discriminator):** "Did you have to **erase the data but keep a tamper-evident record** that it happened — or was a deletion certificate / log entry enough?" *(This separates the real thing from whole-install reset and from plain attestation.)*
- **A3 (the falsifier — the whole game):** "Has **cryptographic erasure / crypto-shredding / certified destruction** ever appeared in a real **RFP, DPA, security review, or BAA**? **Can you show me the clause?**"

## How to recognize the genuine article (from the clause-language research)
There are three registers — only the third validates the differentiated claim:
1. **Attestation (default, ~everywhere):** "return or destroy," "certify in writing," "certificate of destruction," "our SOC 2 covers it." → base case, does **not** count.
2. **Media-sanitization (rigorous but about hardware/ITAD):** "NIST 800-88," "certificate of sanitization," "NAID AAA." → real, but the wrong problem.
3. **The product's register (rare — the one that counts):** the buyer volunteers **both** a *method* ("cryptographic erase / crypto-shred / key destruction") **and** a *retained artifact they receive* ("tamper-evident / immutable audit trail / proof per record we can inspect"), with a **trigger + deadline** and often a **right to audit**.

**Real clause vs engineer's wish:** a real one lives in a **DPA / MSA security exhibit / BAA / RFP matrix**, names a **standard by number** or the word "cryptographic," and specifies an **artifact the buyer is owed**. A wish is *their own* questionnaire answer, a trust-center page, or "our SOC 2." If it's satisfiable by "we delete and sign a certificate," it does **not** count.

**The killer follow-up when they claim it:** *"Read me the exact sentence — does it name the method ('cryptographic' / 'crypto-shred' / 'key destruction'), and does it require you to receive and retain a tamper-evident deletion record you could produce in an audit, or just sign a certificate that you deleted it? What's the trigger and deadline?"* A real requirement survives with a verbatim sentence naming the method **and** the retained artifact; a wish collapses — and the collapse is your answer.

## The artifact to ask for
The **verbatim clause** (a photo/quote is enough), plus: which **document type** (DPA/BAA/RFP/security exhibit), which **buyer/segment** (Care / Assure / Grid / data-sharing pilot), the **regulation/standard** it cites, and the **timeline** (go/no-go date).

## What a result means now (and what it does NOT)
- **A qualifying YES** (a real, dated, go/no-go clause naming the method + a retained tamper-evident artifact): send it to the PM. It **prioritizes the post-MVP crypto-shred-operation milestone** + feeds the parked crypto lane (app-bootstrap + R-α + key-portability). It is **NOT** an AMD-86 re-open and the PM does **NOT** edit AMD-86 / Doc 15 — if it somehow implied a write-path change, that would go through the formal re-open -> DOCS review -> ratify pipeline.
- **A NO** (the expected case): the post-MVP default holds; encrypt-on-write already preserved the optionality. Note "erasure not launch-window-binding" and move on.

## Sync back to the PM
Send: any clause found (verbatim + the metadata above), or a one-line "NO — N buyers, no contracted crypto-erase clause." That's all the research lane needs to stay in sync. Energy: nothing — parked.

<!--
file: track1-interview-coaching/2026-06-15_M5-D_desk-research_ANGLE2-clause-language_TrackA.md
purpose: The Track-A procurement/clause-language research angle (kit Angle 2), DRIVEN by the PM this session
         (web-grounded sub-research) to fill the first return's CAVEAT-3 gap — real RFP/DPA/SIG-CAIQ/
         "return-or-destruction" wording for verifiable erasure (the A3 "show me the clause" falsifier).
owner: Nick (interview prep) / PM (drove + reviewed)
status: BACKGROUND LITERACY — PM-reviewed, primary-sourced where possible. Not a FINDINGS return, not a decision.
verification: PM spot-checked the load-bearing instruments (EU SCC Clause 8.5, CAIQ DSP-02.1, ISO 27001 A.8.10,
         NIST SP 800-88 Rev.2 Sep-2025). Honest gaps flagged in §5 (SIG verbatim paywalled; SOC2 point-of-focus
         secondary; HITRUST/NIST appendix lettering not page-confirmed).
re-scope note: Per the PM adjudication (2026-06-14), Track A's AMD-86 re-open trigger is MOOT (M6 froze the write
         path in the correct encrypt-on-write posture). This angle's value is now PRODUCT/ROADMAP signal +
         interview recognition vocabulary, NOT an AMD-86 re-open. Read it as "how to recognize the rare real
         clause," not "evidence we should re-size M6."
-->

# TRACK A — Data-Erasure Procurement / Clause Language: Evidence Brief
*Desk research for A3 falsifier prep. Mid-2026; sources weighted 2024–2026. Data-erasure procurement language ONLY (energy/DER parked).*

## 1. BOTTOM LINE
Contractual language demanding **verifiable *cryptographic* erasure with a retained tamper-evident audit trail is RARE** as an explicit, named requirement. What is **near-universal** is far weaker: "**return or destroy** the data, and **certify in writing** that you did" — *attested* deletion, certificate on request. The dominant instruments (EU SCC Clause 8.5, ISO/IEC 27001 A.8.10, CSA CAIQ DSP-02, SOC 2 C1.2, typical DPAs) require deletion + attestation; **none name "cryptographic erase," none demand a buyer-held tamper-evident per-record deletion ledger.** Where rigorous evidence-backed sanitization *is* mandated (NIST 800-88, IEEE 2883, NAID AAA, HIPAA disposal), it lives in **physical/media decommissioning** (end-of-life drives, ITAD) — not contracted SaaS "prove you deleted my tenant's logical data with a cryptographic chain-of-custody." Confidence: **High** that "crypto-erase + tamper-evident audit log" is not standard boilerplate; **Medium** on precise prevalence (no published base-rate study; SIG full text paywalled).

The reframing: the market splits into **(a) the legal register** ("delete and certify," attestation — everywhere) and **(b) the media-sanitization register** (NIST 800-88 "verify + document," certificate of sanitization — rigorous but about *hardware*). The product's claim (verifiable cryptographic destruction + retained tamper-evident audit trail) sits in a **gap between the two** and is rarely written into a contract as such.

## 2. KEY FINDINGS
- **EU SCC Clause 8.5 = "delete… and certify," not proof or crypto.** "delete all personal data… and **certify to the data exporter that it has done so**, or return… and delete existing copies." Attestation only; no audit log, no method named. *Primary instrument text (Impl. Decision 2021/914; mirrored in real DPAs). High.*
- **CSA CAIQ v4.0.2 DSP-02.1 is a yes/no attestation about forensic non-recoverability — no crypto-erase, no ledger.** "Are industry-accepted methods applied for secure data disposal from storage media so information is not recoverable by any forensic means?" *Real questionnaire text + CCM v4.0 control catalog. High.*
- **CAIQ auditing guidance asks for documented *evidence of disposal* as an auditor sampling exercise — not a buyer-held tamper-evident log.** "Select a sample of disposal requests… Confirm that all evidence was formally documented and recorded." *Primary control catalog. High.*
- **SOC 2 C1.2: disposal + retained evidence of destruction, method-agnostic.** "Disposal of confidential data… is documented and evidence of destruction is retained." Satisfied by a certificate/disposal log; crypto not required. *Secondary on the point-of-focus phrasing; primary criterion. Medium-High.*
- **ISO/IEC 27001:2022 A.8.10 — one sentence, NO proof/method mandate.** "Information stored… shall be deleted when no longer required." Crypto-shred is one acceptable *implementation* (ISO 27002), not a requirement. *Primary one-line text. High.*
- **NIST SP 800-88: Cryptographic Erase is a Purge technique, NOT mandated; its verify/document regime is about *media*.** CE = "a Purge sanitization technique based on the sanitization of the keys used to encrypt data." Rev. 2 **finalized Sep 2025** (cloud/virtual/encrypted modernization). Verification + a **Certificate of Sanitization** (media serial, method, tool, verification) — *hardware* documentation, not SaaS per-tenant proof. *Primary standard. High on definitions/date.*
- **HIPAA is the strongest "real proof" register — but it's media-disposal/ITAD, and proof = a serialized *certificate*, not a cryptographic ledger.** Standard: render PHI "unusable, unreadable, or indecipherable"; OCR accepts a serialized destruction certificate. *Secondary on HHS/NIST. Medium-High.*
- **Cloud hyperscalers represent destruction via *audit reports/policy*, not per-tenant cryptographic proof.** Documented recourse: "request written confirmation or **review the provider's SOC 2 / ISO 27001 report**." Crypto-shred (deleting tenant KMS keys) is the *implementation*, surfaced as an attested capability. *Secondary + vendor docs. Medium-High.*
- **DPA "return or destruction" boilerplate uses "return OR destroy" + "certify in writing"; cryptographic destruction is essentially absent.** *Real contract corpus (Law Insider). High.*
- **NERC CIP-013 (utilities) covers vendor "return or destruction" on termination as supply-chain risk — but prescribes no crypto-erase-with-audit-trail language.** *Secondary. Medium.*

## 3. REAL LANGUAGE / EXAMPLES (verbatim — the gold)
**A. EU SCC Clause 8.5 (M2 C2P):** "After the end of the provision of the processing services, the data importer shall, at the choice of the data exporter, **delete all personal data processed on behalf of the data exporter and certify to the data exporter that it has done so**, or return… all personal data… and delete existing copies." *(Impl. Decision 2021/914; mirrored in Google Cloud / ActiveCampaign / Firebase DPAs, 2024–2026.)*

**B. CSA CAIQ v4.0.2 — actual data-destruction assessment questions:**
- DSP-02.1: "Are industry-accepted methods applied for secure data disposal from storage media so information is not recoverable by any forensic means?"
- DCS-01.2: "Is a data destruction procedure applied that renders information recovery… impossible if equipment is not physically destroyed?"
- CEK-14.1: "Are processes… to destroy unneeded keys defined, implemented and evaluated to address key destruction outside secure environments, revocation of keys stored in HSMs…?" *(closest to "crypto-shred" — but asks about key-destruction process, not buyer-held proof.)*

**C. NDA/DPA "Return or Destruction" boilerplate (representative; "certify in writing" is the ceiling):** "…will return or destroy all Confidential Information… and **certify in writing to the Disclosing Party that such Confidential Information has been destroyed**, except for copies… maintained as archive copies on… backup systems…" / "…destroy… **in a manner that ensures the same may not be retrieved or undeleted**… and **deliver… a certificate executed by one of the Recipient's duly authorized senior officers**…"

**D. HIPAA BAA "Return or Destruction":** "…Business Associate will… **certify on oath in writing** to Company that such return or destruction has been completed… [and identify] any PHI… for which return or destruction is **infeasible**…"

**E. ISO/IEC 27001:2022 A.8.10 (entire control):** "Information stored in information systems, devices or in any other storage media shall be deleted when no longer required."

**F. NIST SP 800-88 Certificate of Sanitization (media-level proof):** fields = media manufacturer/model/serial, media type, method (Clear/Purge/Destroy), tool+version, verification method+results, performer/validator signature, date. Verification = full or representative sampling. *(Hardware sanitization documentation — not a SaaS per-tenant deletion ledger.)*

## 4. BASE-RATE + STRONGEST DISCONFIRMING EVIDENCE
**"Cryptographic destruction WITH retained tamper-evident audit log" as a contracted requirement: RARE.** No standard instrument, questionnaire item, or common DPA clause names *both* crypto-erasure as the required method *and* a retained tamper-evident buyer-accessible audit trail. The combination appears almost exclusively in **engineering/vendor marketing**, not in the buyer's contracted words. Disconfirming evidence the founder must internalize:
1. **SCC Clause 8.5 — the most-replicated deletion clause on earth — settles for "delete and certify."**
2. **CAIQ DSP-02.1 is answerable "Yes" with a policy reference** (the sample vendor even answered "NA — performed by the IaaS provider" and passed).
3. **ISO 27001 A.8.10 = one sentence, no proof; SOC 2 C1.2 = "dispose + retain evidence," certificate suffices.**
4. **Even where "proof" is demanded (HIPAA, NIST 800-88, NAID AAA), the artifact is a *certificate of destruction/sanitization*, about *media*, signed by an ITAD vendor — not a tamper-evident cryptographic ledger.**
5. **Hyperscalers train buyers to accept "review our SOC 2 / ISO report."**

**Honest counter-signal (the opportunity is real, just not yet contractual):** 2024–2026 buyers are "moving beyond self-attestations and asking for harder proof of controls"; NIST 800-88 Rev. 2 (Sep 2025) blesses CE for cloud/encrypted environments and tells operators to keep sanitization documentation "searchable and tamper-evident." The *building blocks* of the founder's pitch are legitimate and increasingly cited — they are simply **not yet crystallized into standard contract clauses.** The opportunity is genuine; the claim that it's *already a common contractual requirement* is not supported.

## 5. GAPS & UNCERTAINTY
- **Shared Assessments SIG verbatim items: NOT FOUND (license-gated).** CAIQ filled the "standardized questionnaire verbatim" role. SIG-demands-crypto+audit-trail: unverified (low by analogy).
- **SOC 2 C1.2 point-of-focus phrasing:** secondary (AICPA TSC PDF paywalled); base criterion solid.
- **NIST 800-88 r2 certificate appendix lettering** inconsistent across secondary sources (C vs G); content well-corroborated.
- **HITRUST CSF v11.x verbatim control:** confirmed it lists "cryptographic erase" among techniques; exact statement not extracted (licensed).
- **No published quantitative base-rate study.** "Rare" is well-reasoned synthesis, not a measured statistic.

## 6. HOW THIS SHARPENS A3 ("show me the clause")
**(a) Listen for the *register*:** Attestation register ("return or destroy," "certify in writing," "certificate of destruction," "SOC 2 covers it") = the **base case**, does NOT validate the differentiated claim. Media-sanitization register ("NIST 800-88," "certificate of sanitization," "NAID AAA") = real rigor but about *hardware*. The product's register (rare) = the buyer volunteers **both** "cryptographic erase / crypto-shred / key destruction" **and** "retained / tamper-evident / immutable audit trail / proof per record." Only the combination corroborates the hypothesis; one half alone does not.

**(b) Real contracted clause vs engineer's wish:** A real clause lives in a **DPA / MSA security exhibit / BAA / RFP requirements matrix**, references a **standard by number** or names "cryptographic erasure" + an **artifact the buyer receives** (log/cert), with a **trigger + deadline** and often a **right to audit**. A wish is a security-questionnaire answer *they wrote*, a trust-center page, or a hand-wave to "our SOC 2" — it's their own outbound attestation, lacking a named artifact the buyer is owed. Litmus: if satisfiable by "we delete and sign a certificate," it is NOT a crypto-erase-with-audit-trail mandate.

**(c) The killer follow-up:** *"Can you pull the exact clause and read me the sentence? Does it name the **method** (does 'cryptographic'/'crypto-shred'/'key destruction' actually appear), and does it require you to **receive and retain a tamper-evident deletion record** you could produce in an audit — or is it satisfied by the vendor **signing a certificate that they deleted it**? And what's the **trigger and deadline**?"* A genuine requirement survives with a verbatim sentence naming the method AND the retained-proof artifact; a wish collapses into "it's our policy / our SOC 2 / we'd ask for a certificate" — and that collapse IS the A3 finding.

## SOURCES (key)
NIST SP 800-88 Rev.2 (Sep 2025) https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-88r2.pdf · CSA CAIQ v4.0.2 (ConfigCat) + csf.tools DSP-02 https://csf.tools/reference/cloud-controls-matrix/v4-0/dsp/dsp-02/ · EU SCC Clause 8.5 https://cloud.google.com/terms/sccs/eu-c2p · ISO/IEC 27001:2022 A.8.10 https://www.iso.org/standard/27001 · ISO/IEC 27040:2024 https://www.iso.org/standard/80194.html · Law Insider return-or-destruction corpus https://www.lawinsider.com/clause/return-or-destruction · SOC 2 C1.2 (Fractional CISO; Schellman) · NIST/HIPAA (AccountableHQ; eRevival 2026) · Cloud destruction (TechTarget; AWS Trust Center) · NERC CIP-013 (Venminder; AssurX). Could-not-verify: SIG verbatim (paywalled), AICPA TSC PDF, HITRUST CSF v11.x verbatim, NIST r2 appendix letter.

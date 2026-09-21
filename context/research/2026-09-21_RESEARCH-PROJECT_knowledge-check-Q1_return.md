<!--
file: context/research/2026-09-21_P-03-lines_return.md   (path ASSUMED: the charter names no WU id and no path; the slug is descriptive; rename at intake)
purpose: The charter asks one thing: state problem P-03's Refutable-by line and quote its Internal line. Scope fence: the register row as written (a lookup, not a scan). This return establishes both lines at the bytes of the K-05 snapshot (valid-as-of 2026-09-20) and names the three neighbouring texts that must not be quoted in their place. It does NOT establish the wording of the live package file `07_problem-register.md` at HEAD (no tree access from this session), and it does NOT test whether the Refutable-by line has fired in the literature (that is a scan charter, not this one).
audience: the hub (the intake) · Nick (§0: no words; no act is gated)
state-type: lane return (research; read-only domain)
status: RETURNED Mon 2026-09-21 ~12:31 CT (instrument 2026-09-21T17:31:33Z)
laws-held: write-isolation (this one file) · evidence-required · the date law · no ungrepped premise · pointer-not-copy · re-fetch at consumption (binds whoever consumes these quotes next)
-->

# P-03: the Refutable-by line and the Internal line — return

## §0 Card

**Outcome.** K-05 gives P-03's Refutable-by line as "An existing sequential-confirmation method for IoT actuation with the same bounds; or a measured false CONFIRMED under the rule." (K-05, P-03 row, L55; snapshot valid-as-of 2026-09-20; read 2026-09-21.) K-05 gives P-03's Internal line as "**Internal.** SP-1 · SP-4 · AMD-97 / AMD-97-INV-01 (never-false-CONFIRMED) · CONFIRM-SOUNDNESS charter · the coincidence window (C-2 Tier-0 §2; REV-1 F-1) · AM-14 (corroboration) · VERDICT-VOCAB-1." (same row, L51; same dates.)

**Instrument limit.** ASSUMED-STATE. The opener gives the date (Mon 2026-09-21; the instrument agrees, `date -u` → 2026-09-21T17:27:05Z at start) and no tree HEADs, watermark or live-claims line. Assumption: the knowledge set as uploaded (K-00, K-03, K-04, K-05 and K-13 are each stamped valid-as-of 2026-09-20) is current, and no P-03 field has moved since K-05 v0.1. Read at the bytes: K-05 P-03 row whole (file 26,187 bytes · sha256 `ba7aea5921fecd3b9dea833451e06b04e2ee0efd5f0463853f834c19aef12cbe`); K-04 L134 and L146–150; K-03 L134; K-13 L88–89; K-00 whole. Second instrument: the Project's knowledge index returned the same P-03 row text as the disk copy. Could not read: the source of record, package file `07_problem-register.md`, in the live tree; the repos outrank this set (K-00). No web page was fetched; the fence is a register lookup.

**Premise verdicts.** "The open problems are P-01..P-11 (K-05)": CONFIRMED (eleven `### P-nn` headings, K-05 L24..L144). "P-03 carries a Refutable-by line and an Internal line": CONFIRMED (K-05 L55, L51). "K-05 is the file to quote from": CONFIRMED by K-04 L134, which reads "For an exact quote, quote K-05."

**Census.** 8 [VERIFIED] claims in §1, §2 and §4 (all at the knowledge snapshot; none at HEAD; the three premise verdicts are counted separately) · 0 [REPORTED] · 1 [VERIFIED-by-absence] · 1 NOTE.

**Top findings.**
1. P-03's Refutable-by line is the two-disjunct sentence quoted above (K-05 L55). [VERIFIED at the snapshot]
2. P-03's Internal line is the seven-item line quoted above (K-05 L51). [VERIFIED at the snapshot]
3. Three other texts in the set sit close enough to be quoted by mistake: K-04 L149 (same Refutable-by words; a five-item Internal list that K-04 itself declares abbreviated), K-03 L134 (a different, one-clause Refutable-by), K-13 L89 (a Refutable-by that belongs to stage S2's exit sentence, not to the P-03 row). [VERIFIED]
4. No fifth restatement of the line exists in the 17-file set under the grep named in §5. [VERIFIED-by-absence; confidence medium]

**What changes.** No change. bench row: none · register sentence: none · paper: P-03 not moved (this return edits no field of the row) · corpus: 0 crosswalk lines (no paper, spec or product was read).

**Words for Nick.** None; no act is gated.

## §1 The two lines

The P-03 row sits at K-05 L48–L56 under the heading "### P-03 — Verdict soundness as an anytime-valid test over unreliable witnesses (mathematics; M; publishable)" (K-05 L48).

The Refutable-by line, whole, as the file carries it (K-05 L55; snapshot valid-as-of 2026-09-20; read 2026-09-21):

> **Refutable-by.** An existing sequential-confirmation method for IoT actuation with the same bounds; or a measured false CONFIRMED under the rule.

The Internal line, whole, as the file carries it (K-05 L51; same dates):

> **Internal.** SP-1 · SP-4 · AMD-97 / AMD-97-INV-01 (never-false-CONFIRMED) · CONFIRM-SOUNDNESS charter · the coincidence window (C-2 Tier-0 §2; REV-1 F-1) · AM-14 (corroboration) · VERDICT-VOCAB-1.

Split on the " · " separator, the Internal line has seven items (counted by tool, not by eye): SP-1 · SP-4 · AMD-97 / AMD-97-INV-01 · the CONFIRM-SOUNDNESS charter · the coincidence window · AM-14 · VERDICT-VOCAB-1. The separators are U+00B7 (middle dot) and the section mark is U+00A7; both were checked in a byte dump, because a quote that swaps them for ASCII fails a byte audit.

Line numbers are the K-05 snapshot's. K-05 prepends a nine-line header (L1–L9) before the package file's own first line (`<!--` at L10), so the package file's numbering is expected to run nine lower [INFERRED: the package file itself was not readable here].

Refutable-by for findings 1 and 2: the live `07_problem-register.md` at HEAD carrying different words in P-03's Refutable-by or Internal field; or a re-read of K-05 L55 / L51 that does not match the file hash in §0.

What this does to the frame / the problem / the sentence: nothing. The row is reported, not moved. K-05 records P-03's status as "SEEDED (SP-1's pilot data exists; the rule is desk work)." (K-05 L56, as of 2026-09-20); this return does not touch it.

## §2 Three neighbouring texts, and why none of them is the quote

K-04 carries its own P-03 block. Its Refutable-by words are byte-identical to K-05's after the label (compared by tool). Its Internal list is shorter: "*Internal rows.* SP-1, SP-4, AMD-97, CONFIRM-SOUNDNESS, AM-14." (K-04 L149; valid-as-of 2026-09-20). K-04 says so itself: "the Internal rows here are shorter than the register's — P-03 lists five here and seven there" (K-04 L134). Missing from K-04's list relative to K-05's: AMD-97-INV-01, the coincidence window (C-2 Tier-0 §2; REV-1 F-1), VERDICT-VOCAB-1.

K-03 carries a third wording of the refutable-by, with one clause instead of two: "Refutable-by: an existing sequential-confirmation method for IoT actuation with stated soundness/completeness bounds." (K-03 L134; valid-as-of 2026-09-20). It has no "measured false CONFIRMED" disjunct. K-03 is the field-and-gap assessment, not the register.

K-13 carries a sentence that reads like P-03's line and is a different object: "Refutable-by: one false CONFIRMED under the rule; a bound restated without its bands." (K-13 L89). It is attached to stage S2's exit sentence ("The bound"), not to the P-03 row.

Refutable-by for finding 3: a diff of K-05 L51/L55 against K-04 L149, K-03 L134 and K-13 L89 that shows otherwise.

What this does to the frame / the problem / the sentence: no change. It fixes which bytes a register sentence or a paper may quote for P-03: K-05 L51 and L55, re-fetched at consumption from the live file 07.

## §3 The two lines per source

None. No paper, spec or product was read under this fence; nothing to bank in K-07.

## §4 What was refuted or corrected in our own framing

- The skill reference `references/claude-project-operating-notes.md`, three-question test no. 1, reads: "State problem P-03's refutable-by line and its three internal rows." K-05 L51 carries seven items; K-04 L149 carries five. "Three" matches neither file. [VERIFIED: all three files read this session.] The charter's own wording ("quote its Internal line") does not carry the count; the reference file does. This return edits nothing.
- NOTE (outside the fence; not adjudicated). K-05's cross-reference table maps SP-5 to "the ε_d object in P-01/P-03 — a schema" (K-05 L170). SP-5 appears in neither P-03's Internal line (L51) nor P-01's (L27). SP-4, which the same table calls "not a theorem" (K-05 L169), is listed in P-03's Internal line. Whether the omission of SP-5 is deliberate is the register author's call [INFERRED that it is an asymmetry at all].

## §5 Sources

**Read this session (file · lines · snapshot date · read date 2026-09-21):**
- `K-05_problem-register_2026-09-20.md` · L1–23, L27, L48–59, L144–152, L153–174 · valid-as-of 2026-09-20 · 26,187 bytes · sha256 `ba7aea5921fecd3b9dea833451e06b04e2ee0efd5f0463853f834c19aef12cbe`
- `K-04_evidence-floor_formal-model_v0-1.md` · L1–8, L134, L146–150 · valid-as-of 2026-09-20 · sha256 `224a5ec40ce28f284a7aead412d26f21a78d1a601f77b11bc238b32619ade77e`
- `K-03_field-and-gap-assessment_2026-09-20.md` · L1–4, L134 · valid-as-of 2026-09-20 · sha256 `93870fedcd65ccd86da32be988474f71e82e96e61ee4c954c3c147e1f534b58a`
- `K-13_rd-program-of-record_v0-1.md` · L78–81, L88–89 · valid-as-of 2026-09-20 · sha256 `63719bb368ce27ddf48f84e8338010c1fec1d5cb351072d721b4c9da80937a5a`
- `K-00_INDEX_start-here_2026-09-20.md` · whole
- `00_README.md` · grep only (precedence and state terms)
- Skill `nexsys-researcher`: `SKILL.md` whole; references `problem-register-format.md`, `return-template.md`, `claude-project-operating-notes.md`, `citation-verification.md`; `evals/evals.json`. Not read: `references/source-tier-rubric.md` (K-12's headings only).
- Project knowledge index: one query ("P-03 verdict soundness anytime-valid Internal Refutable-by"); it returned K-05's P-03 row with the same Internal and Refutable-by text as the disk copy.

**UNVERIFIED (do not cite as authority):**
- The live `07_problem-register.md` at HEAD: not reachable from this session. A field move after 2026-09-20 would not show here.
- Whether the Refutable-by line has fired (a published sequential-confirmation method for IoT actuation with the same bounds) since the 2026-09-20 scan: not tested; outside this fence.

**Search run for the absence finding (2026-09-21):** `grep -rn -i "sequential-confirmation\|sequential confirmation\|measured false CONFIRMED\|false CONFIRMED under"` over the 17 files in the Project's knowledge directory → four hits: K-05:55 · K-04:149 · K-03:134 · K-13:89. A paraphrase that shares none of those strings would not be caught; hence confidence medium.

RETURNED /mnt/user-data/outputs/2026-09-21_P-03-lines_return.md 10662

<!--
file: context/instructions/2026-10-10_frontend-lane_HERO-U2c_recovery-card-under-f_design-charter.md
purpose: The charter for HERO-U2c — the recovery card's design RE-CUT UNDER `CARRIER: f` (AMD-103): FIELDS §3's per-probe live keys give way to the record's keys; SPEC §3's S3 column re-read against the record; the sixth cell ("No check recorded since {t}", AMD-103 R-G) designed beside the fifth state; SPEC §7's copy rows; states.html. Run as a frontend lane in DESIGN MODE; `design/recovery-card-v1/` only. (The plan forward §4, D-v103-24.)
audience: the HERO-U2c lane (a fresh Cowork conversation booted as the nexsys-frontend skill) · the hub (audits the return; AVAIL-API-1's cut waits on this landing, AMD-103 §4) · Nick (rules on the open questions in one batch)
state-type: lane charter (frontend; design mode)
status: DISPATCH-READY on `AMD-103: ratify` — FILED v104 beat 3 (Sat 2026-10-10 ~15:4x CT) from AMD-103 DRAFT v6 (md5 664e25b2…, the text for the word), inheriting Nick's NE4 (15:32: the null state while the card's projection is not LIVE; precedence) and NE3 (the class derived from the tracker's arms). DISPATCH-READY on `AMD-103: ratify` (a later edit to R-B, R-C, R-G or §3 re-cuts §2 first). Sunday daytime; ≤ 1.5 h.
-->

# HERO-U2c — the recovery card under `CARRIER: f`: the record's keys, the sixth cell, the S3 column re-read

## §0 The lane contract (read first; every line binds)
- `date -u` first. State your instrument limit (what you can and cannot run from your shell). CT = UTC−5, derived once.
- **The one deliverable:** `nexsys-hivemind/context/audits/<your CT date>_HERO-U2c_return.md`, one file. §0 card first (≤ 3 KB: the census of files modified, with exact paths; P1–P6 adjudicated; the defaults you took; the re-cut FIELDS §3 key list; the questions for Nick). Then §1 FIELDS §3 as re-cut · §2 SPEC's changes · §3 states.html's changes · §4 findings. Cap ≤ 10 KB. Your last line, in the file and printed: `RETURNED <path> <bytes>`.
- **Write-set.** ONLY the four existing files under `homesynapse-core/web-ui/dashboard/design/recovery-card-v1/`: `FIELDS.md` · `SPEC.md` · `states.html` · `README.md`. Nothing under `web-ui/dashboard/src/`, nothing outside `web-ui/dashboard/`. `git -C homesynapse-core --no-optional-locks status --porcelain -- web-ui/dashboard` must be EMPTY when you start. Never run `git add`, `git stash`, `git checkout`, `git switch` or `git commit` in any repo. Nick commits with a card after the hub's audit.
- **This is design, not build.** No installs; no change to `package.json`, Vite, the token build or the CI gate. You may run `npm run dev` to look at the dashboard against the mock. You may render your mockups as an artifact so Nick can see them. The files of record are the ones in the repo.
- **The honesty law binds every sentence you write.**
  - A value the wire did not carry is never shown as if it had. A null renders as an honest sentence, never as a blank, "null", an invented name or an invented verb.
  - **Under (f), a probe's answer is sayable only from a `probe_answered` record, and "asked" only from the record's counters or the contract.** The record is written at most once per record interval per device (plus once per boot or integration restart, R-B), so "checked {at}" names the last RECORDED answer, never the latest probe.
- **Precedence and the null state (AMD-103 §3, Nick's NE4) bind the design:** the state projection's `availability` governs the card's state; the records only decorate it (asked, answered, R-G's stale arm). While the recovery-card projection is not LIVE (catching up, or after a failed catch-up) the record's keys are NULL: the card keeps its S2 form and the sixth cell never fires from a null.
- **`VOCAB: a` is Nick's word (D-v101-24) and stays VERBATIM:** **Reporting** · **Quiet since <t> (asked, answered)** · **Not responding since <t> (asked twice, no answer)**, each with its contract sentence; the passive class without the parenthesis. The fifth state (seeded dark, never asked) keeps its own row.
- **The sixth cell's words are AMD-103 R-G's:** "No check recorded since {t}". You design its level, glyph, colour role and the sentence beneath — never new words for its label.
- **Name-light.** Every mockup and every line uses the literal token `{{NAME}}` where the product name would appear; no candidate name appears anywhere. **The counsel gate:** nothing you write is public copy. No card or spec sentence is a claim about the field — no "only", "unique", "first", "patented", "superior" — and no competitor is named or compared.
- **Predictions, pre-registered — adjudicate them first in your §0 card:**
  - **P1:** FIELDS §3's `lastProbeOutcome` + `lastProbeAt` and `probeMisses` rows are RETIRED with AMD-103 §3's reason ((f) does not record the process's probe memory). They are replaced by the record's keys, each tagged NOT-ON-WIRE with its AMD-103 row as the cite, and the proposed camelCase key marked PROPOSED (AVAIL-API-1 names the wire keys at v1.1.7):
    - the newest `probe_answered`'s `at` · `windowStart` · `answeredSinceLastRecord` · `missedSinceLastRecord` · `lqi`/`rssiDbm`/`linkAt` (R-B);
    - the contract's five: `availabilityClass` · `reportIntervalSeconds` · `silenceLimitSeconds` · `missesToDark` · `recordIntervalSeconds` (R-C);
    - R-G's bound, as a derived row ("computed at read; no key").
    - `integrationId` and `ieeeAddress` stay.
  - **P2:** `grep -ril` over `design/recovery-card-v1/` for any product-name string other than `{{NAME}}` returns nothing.
  - **P3:** `git -C homesynapse-core --no-optional-locks status --porcelain -- web-ui/dashboard/src` is empty at your close.
  - **P4:** at least one cite in this charter has moved or is wrong; file it with the corrected cite.
  - **P6:** every S3 sentence has its NULL form (the projection not LIVE) = its S2 form, and SPEC §3's header paragraph states the precedence rule; no S3 cell reads a record key without its null form beside it.
  - **P5:** the fifth state's derivation (FIELDS §3: `lastProbeAt` null ∧ UNAVAILABLE) loses its key under (f). Re-derive it from what (f) records, or name it "not sayable at S3" with the reason — never keep `lastProbeAt` silently.

## §1 The read-set, in order (nothing older)
1. **AMD-103 as ratified:** `homesynapse-core-docs/design/amendments/AMD-103_…md` if the docs card has landed, else the text Nick ratified, `_scratch/v104/b3/AMD-103_DRAFT_v6.md` (md5 664e25b2…, unless the hub's card names a later one; your §0 card names which). Read R-B, R-C, R-G, §3, §4 whole.
2. **The four files** under `design/recovery-card-v1/`: FIELDS.md whole; SPEC.md §3, §4, §7, §11, §12; states.html; README.md.
3. **The two returns:** `nexsys-hivemind/context/audits/2026-10-09_HERO-U2a_return.md` and HERO-U2b's return (the v1.1.6 mirror keys `availabilityReason` · `lastSeenAt` · `link`).
4. **The contract freeze:** `nexsys-hivemind/context/decisions/2026-06-21_dashboard-read-API-contract-freeze.md` `:1`–`:60`, `:255`–`:265` (the additive rule; keys beside `availability`, never under it).

## §2 The ground (from AMD-103 v4; re-read, never trust)
- **`probe_answered` (R-B):**
  - `at` is the reply instant. `windowStart` is derived so that `at − windowStart` is the true window unless the wall clock stepped. The two counters cover the window.
  - `lqi` · `rssiDbm` · `linkAt` are the LAST link reading the tracker kept, with its own instant. A probe reply carries no reading, so signal copy cites `linkAt`, never `at`.
  - The window is never persisted: its counts are lost at every stop, so the card never sums across a restart.
- **`availability_contract_declared` (R-C):** the five fields; declared at every boot and interview, and refreshed every 30 days. `availabilityClass` NAMES the tracker's arm (no class is computed in the code today): `passive` when the PowerSource is not a mains class; `mains-metered` when a reporting contract yields a maximum (the silence limit = maximum + 60 s); `mains-floor` when none does (the 60-s floor alone). SPEC §4's contract sentence per class reads from these fields.
- **The null state and precedence (§3, NE4):** null keys until the card's projection is LIVE; the v1.1.7 bump carries that projection's position in `meta` beside `viewPosition` (a household sentence is pinned to a position); `availability` governs, the records decorate.
- **The sixth cell (R-G):**
  - The evidence per device is the newest of: `lastReported`, `probe_answered.at`, `availability_changed`, and the contract record.
  - The bound for an asked class is `recordIntervalSeconds` + `silenceLimitSeconds` + `missesToDark` × 5 s × N + one sweep; for passive, `silenceLimitSeconds` + one sweep. It is computed at READ on the core's clock.
  - With no contract record, the bound is not computed and the card keeps its S2 form.
- **AMD-103 §3:**
  - The keys come beside `availability`, at v1.1.7, after v1.1.6 is recorded.
  - A1's consistency window gains a third instant: the card's keys come from the recovery-card projection, which `meta.viewPosition` does not bound.
  - FIELDS §3's `lastProbeOutcome` and `probeMisses` are not recorded under (f), and SPEC §3's S3 column is re-read against the record.
- **The plan's examples (§4), to be re-worded honestly:** "Quiet since 03:02 · checked 07:02, it answered" and "answered 37 of 49 checks this hour". Use "this hour" only when `at − windowStart` is the record interval; the opening record's window is shorter.

## §3 Files to modify (all under `homesynapse-core/web-ui/dashboard/design/recovery-card-v1/`)
| File | What |
|---|---|
| `FIELDS.md` | §3 re-cut per P1/P5, a cite per row; §1–§2 unchanged unless a row moved (say which) |
| `SPEC.md` | §3: the S3 column re-read against the record; the sixth cell per R-G (a row or a cell — decide, and say why). §4: the contract sentence from R-C's fields. §7: the copy rows for the sixth cell and the S3 Quiet sentences. §11: the build rows re-pointed to the record's keys. §12: the questions |
| `states.html` | the sixth cell beside the fifth state, both themes; the S3 sentences |
| `README.md` | one line for U2c (date; AMD-103; what moved) |

## §4 What to watch out for
- **Recency.** "Checked {at}" is the last recorded answer: probes run about every 60 s for an asked class, but records are at most hourly. Never imply "checked moments ago".
- **Windows.** Name the window. A window is "since {windowStart}". A restart cuts it, so never add counts across records whose windows are not contiguous.
- **The sixth cell.** It needs a contract record. Without one, keep S2 — never an invented bound. The design names the bound's inputs; the build (U3) computes it.
- **The signal reading:** `linkAt`, not `at` (R-B).
- **The keys:** beside `availability`, never under it. `availability`'s semantics are unchanged.
- **Name-light and the counsel gate** bind the mock's every string.

## §5 Out of scope
- Any `src/` change (U3 builds it).
- The Java side (AVAIL-API-1) and the contract note's bump (the hub's).
- The probe cadence, IR-147, and any sentence about other products.

## §6 Success criterion (binary)
- Only the four files are modified, all under `design/recovery-card-v1/`.
- FIELDS §3 is re-cut with a cite per row, and the two per-probe rows are retired with the reason.
- SPEC §3 carries the sixth cell, and every row × three stages is filled with a sentence or an honest "not sayable at this stage".
- SPEC §7 has the new copy rows.
- `states.html` renders in both themes with the sixth cell beside the fifth state.
- SPEC §3 states the precedence rule and every S3 cell's null form (P6).
- P1–P6 are adjudicated in the §0 card; the name grep is empty; `src/` is untouched.
- The return is ≤ 10 KB, with `RETURNED <path> <bytes>` as its last line.

## §7 Escalation
No question gates the start: every slot has a default here. A premise that fails at the bytes is corrected in your §0 card (P4), and the design proceeds on the corrected fact. A finding that would change AMD-103 or the contract is a §12 question with options, never a change to the write-set.

## §8 The hub's audit rules (pre-filed)
Two layers: the return read critically, then the hub's own greps.
- the four files' census;
- the `{{NAME}}` grep;
- `git status --porcelain -- web-ui/dashboard/src` empty;
- FIELDS §3's rows checked against AMD-103 R-B, R-C and R-G (a key the record cannot serve is the table's refutable-by);
- the sixth cell's mock read side by side with the fifth state's.

On ACCEPT: Nick's `git add -A web-ui/dashboard/design/recovery-card-v1` card. AVAIL-API-1's cut waits on this landing (AMD-103 §4).

## §9 The dispatch line (Nick pastes into a FRESH Cowork conversation with `ClaudeFolder` connected; Sunday daytime, after `AMD-103: ratify`)
```
You are the HERO-U2c frontend lane in DESIGN MODE (the nexsys-frontend skill). Read nexsys-hivemind/context/instructions/2026-10-10_frontend-lane_HERO-U2c_recovery-card-under-f_design-charter.md WHOLE, then its §1 set in order. Execute §0 exactly: date -u first; your instrument limit; P1–P6 adjudicated in your §0 card; VOCAB: a verbatim; write ONLY the four files under homesynapse-core/web-ui/dashboard/design/recovery-card-v1/; no git add/commit anywhere; the return at nexsys-hivemind/context/audits/<CT date>_HERO-U2c_return.md with RETURNED <path> <bytes> as its last line.
```
Say back to the hub: `HERO-U2c: running`, then `HERO-U2c: RETURNED <path> <bytes>`.

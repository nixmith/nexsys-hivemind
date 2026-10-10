<!--
file: context/audits/2026-10-10_v103-b1_HERO-U2b_intake_two-layer_audit.md
purpose: The v103 hub's two-layer intake of HERO-U2b's return (the mirror bump and the recovery card on the mirror's keys, rows 1–2), with the rider it orders before the landing and the AUDIT CORRECTION of v102 b3's note N1.
audience: the v103 hub (rulings) · the HERO-U2b-r1 rider lane (§4 is its brief) · Nick (§0)
state-type: intake audit
status: FILED v103 beat 1 (Sat 2026-10-10 ~07:0x CT; instrument 2026-10-10T12:02:11Z). Return read: nexsys-hivemind/context/audits/2026-10-09_HERO-U2b_return.md (12,258 B; RETURNED line last). Charter: context/instructions/2026-10-09_frontend-lane_HERO-U2b_mirror-bump_recovery-card-on-mocked-fields_charter.md.
-->

# HERO-U2b intake: two layers, the rider, and N1 retracted

## §0 Verdict
**ACCEPT-WITH-RIDER.** The rows land as built. One rider runs before the landing: HERO-U2b-r1 (§4) moves the contract pin's fifth literal home, extends the hero-literal lint to the card's two files and amends SPEC §7 to the catalog's 63 rows. Without the pin line, `frontend.yml` is red on the push. The two out-of-write-set edits trace to the charter's defects (IR-144), not to the lane.

**AUDIT CORRECTION of v102 b3's N1** (`context/audits/2026-10-09_v102-b3_HERO-U2a_intake_two-layer_audit.md` §4). N1 said a seeded-dark device "carries `silence_timeout`" on the wire, so the fifth state could not be said at S2. That was a reading of the tracker's in-memory seed, not of the wire. The seed is never published (§2.9), and the real capture shows the Hue as UNAVAILABLE with reason and lastSeenAt both null. SPEC §3's S2 cell for R5 (`UNAVAILABLE` ∧ reason null ∧ `lastSeenAt` null → the fifth state) is sound, and the lane built that cell. N1 is RETRACTED. The charter's watch-out that carried it (§4 N1: "the fifth state at S2 fires only on UNKNOWN") was the hub's error.

**Pre-registered for BC9a's C3, before its line is read (P-v103-1):** after the restart onto `37f05a9`, the Hue reads `availability=UNAVAILABLE availabilityReason=None` (arm (a) with None). If it reads `silence_timeout`, some path publishes the seed that §2.9 did not find, and the retraction re-opens.

## §1 Layer 1: the claims, read against the charter
- **Predictions.** P1 HOLDS (§2.1). P2 PARTIAL, and the lane is right: the charter's "ALL red at HEAD" could not hold for the absent / null / typed-pass arms, which HEAD's validator passes by construction (v115's form). This was the charter's defect. P3 HOLDS (the stability test pins the seven md5s and passes, §2.2). P4 PARTIAL: `check:contract` is red on the pin's fifth home, outside the write-set. P5 HOLDS: the lane found five moved or wrong cites (§3.5 of the return; the 61-vs-59 count among them). P6 HOLDS (§2.7).
- **Deviations**, each ruled in §3. The lane departed from the charter's N1 without tagging a deviation in §0. It disclosed the departure in `recovery.ts:20–:21` and `:190` and in §3.6. That is a return-discipline note, not a block.
- **For the hub (§3.7–§3.9):** A3 has no J1 keys (IR-145). The freeze doc's v1.1.6 stamp becomes a docs row. Live verification is pending (§5). The next unit is the commit-side rows, then the live render, then HERO-U2c.

## §2 Layer 2: the hub's own re-execution
1. **Census at porcelain** (`git status --porcelain -- web-ui/dashboard`): 18 ` M` + 7 `??` = 25, all under `src/`. By top directory: `a11y.test.tsx` 1, `components/` 5, `lib/` 15, `views/` 4. This equals the §0 declaration (audit rule R1).
2. **The gates in a clean container** (node v22.22.0 · npm 10.9.4). Input: a tarball of the working tree, `_scratch/v103/b1/dashboard_snapshot_hero-u2b.tgz` (398,803 B, md5 `39a26ede6e48`, 144 entries, `node_modules`/`dist` excluded). `npm ci` exit 0. `npm run verify`: `tokens:check` OK · `eslint .` 0 · `tsc --noEmit` 0 · `vitest run` 32 files / 682 passed / 6 todo · `vite build` ✓ (index 157.02 kB, 47.05 kB gzip) · `check-bundle-size` 77.2 KB / 100 KB · `contract-check` ✗ `CONTRACT_VERSION is not v1.1.5-2026-09-19`, so the run exits 1 at the last step only. This matches the return's §2 exactly (R6).
3. **The rider's content, proven on a throwaway copy** (nothing shipped from it). `EXPECTED_VERSION = 'v1.1.6-2026-10-09'` → `✓ Contract coverage complete: 11 endpoints, version v1.1.6-2026-10-09`. The hero-literal scope with `src/components/RecoveryCard.tsx` and `src/lib/recovery.ts` added → eslint 0 problems. `src/views/DevicesView.tsx` added → 10 hero-literal hits, HEAD's own app literals. All three match §3.1–§3.2.
4. **Red-first (R2).** The test ran on HEAD `2b4be09`'s tree (`git archive`) with only the final `v116-additive.test.ts` and the new fixture added: **14 failed / 10 passed of 24**. The same file on the lane's tree: 24/24. This is consistent with the lane's 12/21 at R1 plus the three scenario rows added at R2. `recovery.ts` and `RecoveryCard.tsx` are absent at HEAD, so their tests are red by import failure (not re-run).
5. **The fixture row (R3).** `wire-2026-10-09-entities-j1-row.ts` equals the capture's `data[7]` (`_scratch/v102/b4/entities_df2bc62_raw.json`) as an object, with the same key order. The compact form is 322 B, md5 `ebce431508f8…`, the same as the file's own comment. Meta `{viewPosition 1596602, timestamp …00:10:34.867841587Z}` is equal.
6. **SPEC §7 at the bytes.** All 59 §7 strings appear verbatim in `i18n.ts` (a script compare found 0 mismatches). The catalog's 63 `recovery.*` keys are the 59 plus exactly the four [AMEND] keys (`…left.line.noTime` · `…notResponding.bare.noTime.label` · `…notResponding.line.noTime` · `…notResponding.noTime.label`).
7. **Name-light (R4).** Four added or modified lines under `src/` carry a product name or `{{NAME}}`, and all four assert the token's absence (a comment and the Register-C test). "we" appears in 0 `recovery.*` strings.
8. **The pin's homes (`git grep` at the working tree).** Literal `v1.1.6` at `contract.ts:14` · `contract.test.ts:38` · `v113-additive.test.ts:405` · `v114-additive.test.ts:240`. By pattern at `v115-additive.test.ts:144` (and in v116). `scripts/contract-check.mjs:22` still reads `v1.1.5-2026-09-19`. Its own comment (`:15–:21`), and v115's at `:142–:143`, already name it as one of the pin's homes.
9. **The source behind N1, at `37f05a9`** (the Pi's sha after BC9a).
   - `StandardAvailabilityTracker.java:281–:291`: the seed builds an in-memory `DeviceState` (UNAVAILABLE + `SILENCE_TIMEOUT` for a dark seed) and calls no listener.
   - `:564–:619`, `transition`: the reason is never null (explicit, or `FIRST_CONTACT` / `FRAME_RECEIVED`), and the listener fires only on a change.
   - `ZigbeeIntegrationAdapter.java:2101–:2129`: the only `new AvailabilityChangedEvent(` in main code. `reasonToken` is null only when the reason is null. Its two callers are the transition listener (`:2054`) and the unknown→online publish (`:2084`, AVAILABLE only).
   - So on the wire, UNAVAILABLE ∧ reason null ∧ lastSeenAt null means one thing: a pre-J1 (version-1) event that was never superseded. That device has been dark since before J1. Under the sweep's skip (`T:465–:467`, read at `da9ca3d` in v102 b3), it has not been asked since startup. SPEC §3's S2 cell for R5 says exactly that and no more.
10. **The render (not run by the lane on a screen).** Run by the hub: the `recovery-states` scenario under `vite` mock mode in Chromium (Playwright), light and dark, America/Chicago. Nine rows render. The five glyph and colour roles are distinct. SPEC §10's sentences (2), (5) and (6) appear on screen in their S2 forms. Sentence (1) is the S2 fallback, because §10's numbers are S3's. The screenshots are `_scratch/v103/b1/hero-u2b_devices_recovery-states_{light,dark}.png`.

**Not re-executed (disclosed):** a screen-reader pass (the `a11y.test.tsx` rows run inside the 682); the per-row red runs of R2's view tests; the card on the real wire (§3.8 of the return: one Devices read at `37f05a9`, the act in §5).

## §3 Rulings
- **[WRITE-SET] `scripts/contract-check.mjs:22`, `eslint.config.js`:** the charter's defect. The lane was right to stop at its write-set. Both edits go to the rider (§4). IR-144.
- **[AMEND] the four null-arm keys:** ACCEPTED. The words are SPEC §3's own null arms (§2.6). The rider amends SPEC §7 to 63 rows, so the design of record equals the catalog.
- **[FLEET] the default mock fleet goes from 6 to 9 rows:** ACCEPTED. The charter asked for each reason token in the default fleet, and the three rows carry them. All 32 files are green.
- **[INFO] one real row as a fixture file; `{time}` uses the app's formatter** ("2 min ago", "6:22 AM") where §10 has spoken forms: ACCEPTED. The dashboard keeps one formatter.
- **The untagged N1 departure:** the lane's rule stands (§0; §2.9). Note for the lane's next return: a departure from a charter line is tagged [DEVIATION] in §0, even when the design of record supports it.
- **§3.7 (a) A3 carries no J1 keys** (the drawer reads the live A1 row): IR-145, decided in AVAIL-API-1's cut. **(b) The freeze doc's v1.1.6 stamp:** joins DOCS-2's fold list. **(c) The Stale pill beside the stamp:** SPEC §6 B, as designed.

## §4 HERO-U2b-r1: the rider's brief (the web-ui domain; the same lane form)
**Write-set (three files, nothing else):**
1. `homesynapse-core/web-ui/dashboard/scripts/contract-check.mjs`: line 22 becomes `const EXPECTED_VERSION = 'v1.1.6-2026-10-09';`, plus one paragraph above it in the file's own form. The paragraph says: v1.1.6 is HERO-U2b's mirror of three ADDITIVE optional-nullable keys on A1 (`entities[].availabilityReason · lastSeenAt · link`), which landed core-side by J1 `df2bc62` on 2026-10-03. The literal homes stay five (contract.ts · contract.test.ts · v113 · v114 · this file); v115 and v116 assert the pin by pattern. They move together (HERO-U2b-r1).
2. `homesynapse-core/web-ui/dashboard/eslint.config.js`: add `'src/components/RecoveryCard.tsx'` and `'src/lib/recovery.ts'` to the hero-literal rule's `files`, after `'src/components/Resource.tsx'`. Update the comment's count (the six hero files plus the recovery card's two; SPEC §11 row 2). Leave `DevicesView.tsx` out: its 10 hits are HEAD's own literals, keyed in a later unit.
3. `homesynapse-core/web-ui/dashboard/design/recovery-card-v1/SPEC.md`, §7 only: append the four [AMEND] rows, with keys and strings exactly as in `src/lib/i18n.ts`, and one line beneath the table: "Amended 2026-10-10 (HERO-U2b-r1; the v103 intake): the four null-arm keys §3 names in words; 63 rows."

**Gates:** `npm run verify` with all seven steps green. Expected: `tokens:check` OK · eslint 0 · tsc 0 · vitest 32 / 682 / 6 todo · build ✓ · bundle ≤ 100 KB · `contract-check` ✓ 11 endpoints, v1.1.6-2026-10-09. Run it on a `/tmp` copy with `node_modules`, the npm cache and `TMPDIR` on `/tmp` (`/sessions` is full), then copy the three files back and check their md5s on both sides.

**Return:** `nexsys-hivemind/context/audits/2026-10-10_HERO-U2b-r1_return.md`, ≤ 3 KB, §0 first: `date -u` · the three diffs as hunks · the seven gate lines · the census `git status --porcelain -- web-ui/dashboard` (expect 28 = 21 M + 7 ??) · `RETURNED <path> <bytes>` as the last line. Never `git add`, `commit`, `stash`, `checkout` or `switch`. Touch no file under `src/`.

## §5 What this changes in the plan
1. **The landing order.** The rider runs first (≈ 20 min). After its intake comes the core landing card: `git add -A web-ui/dashboard`, census 28, then the push, then `CI:` on `frontend.yml`. Only then is the web-ui domain free.
2. **The card on silicon, pulled forward.** After the landing, the S2 card reads the real wire at `37f05a9` (the return's §3.8 bar): the Hue reads the fifth state, the Shelly plugs read "Reporting". This is the first step of the explanation path (D-v101-39 (2)) on real hardware, and it no longer waits for AVAIL-API-1.
3. **AVAIL-API-1's cut gains two rows.** IR-145 (whether A2/A3 carry the J1 and S3 keys). The FE's six S3 `test.todo` keys (`availabilityClass · reportIntervalSeconds · silenceLimitSeconds · lastProbeOutcome · lastProbeAt · probeMisses`) become the next FE unit's red rows.
4. **HERO-U2c, the act (row 3), stays after the run.** It needs a write endpoint that is not on the freeze list.
5. **Q5 stays open.** N1's retraction leaves the restart ambiguity for devices dark under J1 and later (the SPEC's §12 Q5). Q5 (c), one boot probe for seeded-dark mains devices, remains a tracker change in IR-56's family for AVAIL-API-1's review.

## §6 Register rows minted (ids grepped first: none above IR-143 existed)
- **IR-144:** the HERO-U2b charter had five authoring defects. (1) Its write-set missed a pin home its own code names. (2) R2 asked for a lint edit outside the write-set. (3) It said 61 keys where the SPEC has 59. (4) P2's "ALL red" was ill-posed for preservation arms. (5) N1 contradicted the design of record's S2 cell. The instrument: before dispatch, `git grep` every literal the gates check across the whole package, and diff each watch-out against the design of record's cells.
- **IR-145:** A2/A3 carry no `availabilityReason · lastSeenAt · link`, so the detail drawer reads the A1 row. AVAIL-API-1's cut decides.

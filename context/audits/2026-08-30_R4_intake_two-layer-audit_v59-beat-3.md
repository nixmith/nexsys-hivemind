<!--
file: context/audits/2026-08-30_R4_intake_two-layer-audit_v59-beat-3.md
purpose: The hub's two-layer audit of the R-4 operator record (2026-08-30_R4_re-rep_operator-record.md, 29,787 B, CLOSED-PENDING-HUB-AUDIT) against the packet's filed H12 bar. Layer 2 ran as an in-conversation audit lane (15 re-executed checks, ≤3 KB card); layer 3 = the hub's own sample re-execution at the record bytes + R-3a cross-record primaries.
audience: Nick (the word) · the spine
state-type: intake audit (v59 beat 3)
status: FILED. VERDICT: ACCEPT-WITH-NOTES — THREE OF FOUR (C1/C2/C3 MET · C4 MISS-BLOCKED, structural). THE FULL D-1 LIFT DOES NOT WRITE; the narrow-mint question goes to Nick in H10 form.
-->

# R-4 intake audit — two layers + hub sample (v59 beat 3)

## §0 Verdict
**ACCEPT-WITH-NOTES.** The record is honest, evidence-dense, fences intact (token value ABSENT · nothing deleted · no downgrades flag · formed=0 everywhere · zero public-claim sentences). C1/C2/C3 MET at the ⏺s; C4 MISS-BLOCKED — not an artifact failure: bench-hero's refs belong to the BENCH card's registry (F-R4-2); no join window could close that gap (re-bind budget 0/2 spent, correctly). **The lift as drafted (D-1 pair) does NOT write.** The record fully supports a NARROWER claim — Nick's word decides (MINT-NARROW | HOLD).

## §1 Layer 2 (audit lane, 15 checks) — verdict DEFECT(S)-FOUND, four contradictions raised
Checks 2–6, 8–14 PASS at the record's own quotes (hash chain 3-hop identical to the pinned 452a2f95…; the second hex 8156f4cb… is the STALE 08-27 .deb, coherently labeled in D-d; version identical on 4 surfaces; ordinary upgrade, "downgrad" absent; drop-in sections 0 + unit-sourced loosening; C3 70→80, discriminator 0; D-g bounds honored with the prediction pre-filed 23:26Z before the 23:31:55Z window; O-1 token pair not rewritten, mtime 2026-08-13; §7 floor [PASS] 6/6, PAN 0x774c, by-id identical; D-a–D-g complete; F-R4-1/F-R4-2 supported; O-2 stated).

## §2 Layer 3 (hub, at the bytes) — all four raised contradictions adjudicated BENIGN-WITH-MECHANISM
1. **resumed-count 6 vs FIVE starts:** the close-count grep spans `journalctl -b` (the whole boot), which contains the PRE-SITTING boot invocation's resumed line + the five sitting starts. Packet bar was "resumed ≥1 · formed 0" — met either way; the per-invocation 5/5 tally is the C1 instrument. Record line 18 carries both numbers side by side; no deception.
2. **"35 operator paste-backs" vs 31 ⏺ glyphs (25 evidence-bearing):** different units — paste-backs are chat messages; glyphs are what survived the disclosed 51→29 KB consolidation. No criterion rests on the count. LESSON: census lines name their unit and stay re-derivable from the artifact.
3. **G3 §0-only:** the operator's word is the evidence tier for a read-gate; it is QUOTED and timestamped (22:56Z) in §0. PASS, not partial.
4. **22:32Z (§3d event) vs 22:41:32Z (dpkg .list mtime):** ordering is coherent (hash hops before install); the gap is operator pacing between paste-backs. Benign.
Plus, characterized: the window-close **403 + TOKLEN-OK absent** = packet instrument defect iii — the token is 43 chars (file 44 B incl. newline) so `test ${#TOK} -eq 44` cannot pass, and the extraction mis-grab produced the 403; the corrected read returned 200 (`token_len=43, http=200`). C1–C3 unaffected (store reads are sudo sqlite3, not token-gated).
**C2 RULING:** MET on the `state_reported` arm (pos 75/73 = 23:19:14/23:18:14Z, inside 23:05:06–23:50:06Z; both entities AVAILABLE, `stale:false`). The newest `availability_changed` at pos 41 pre-window is CORRECT event-sourcing behavior — a continuously-available device produces no fresh transition row; the packet's "state_reported / availability_changed" reads either/or. Demanding a fresh transition row would reward flapping.
**Cross-record (R-3a primaries, hub-read):** R-3a's "re-adoptions ×2" were TRUE adoptions (new rig ULIDs, proposal→adopted); tonight's two `device_relinked` are those same rig devices relinking — coherent, no drift between records. Therefore **C4 was unreachable at dispatch**: the rig census (2 sensor entities, NO actuator) was on file in the R-3a return before the ★ pass. LESSON (minted): a lift criterion is checked REACHABLE against the instrument's own census at packet authoring — second occurrence of the §9-B class.

## §3 Accepted findings → rows
- **F-R4-1** (shipped pipeline converts NO silent-rejoiner; announce-class devices only) → coding-WU candidate, R-10 docket.
- **F-R4-2 (MAJOR)** (custody clones the NETWORK, not the REGISTRY; bench pos 25065/6-dev vs held pos 40/2-dev) → doctrine + docs row; explains C4.
- **C-1** (shipped schema does not admit `integrations.zigbee`; service runs on WARNING every start) → its OWN packaging row (PKG-SEC-1 ships as written — orders never grow).
- **O-2** wait-state: held card next boot — `systemctl show -p ExecMainStatus -p Result` + `adoption_maps_rehydrated` check (~5 min operator act, rides whenever).
- **Packet instrument defects i–iii + D-f path defect** → pm-lessons harvest at the next fold (artifact nests at `deb/build/`; journal `-b`+`head` mis-scope; the 43-char token vs `-eq 44` gate; `/etc/...` yaml path vs real `/var/lib/homesynapse/config/`).

## §4 Ask
One word from Nick: **MINT-NARROW** (the C-001-narrow row drafted at the H10 card mints into the register, scope-fenced, refutable-by the record; the adoption/automation sentence stays fenced pending R-4b) **| HOLD** (nothing mints until a clean four-of-four).

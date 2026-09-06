<!--
file: context/audits/2026-09-06_F-R4-1b_intake_two-layer-audit_v66-b8.md
purpose: The hub's two-layer audit of the F-R4-1b return (the ZDO IEEE_addr_req second surface) under the instruction's own predictions and success criterion; the two [REVIEW]s ruled; the core msg file + census card for Nick's landing; the artifact act R-4c needs (install-smoke's path filter does not cover integration/** — a workflow_dispatch is required, and CI-PATHS-1 is chartered).
audience: the hub · Nick (§4 the landing card, §5 the artifact act) · R-4c's packet author
state-type: intake audit
status: FILED v66 beat 8 (Sun 2026-09-06 ~18:1x CT; instrument 2026-09-06T23:1xZ). Return: context/audits/2026-09-06_F-R4-1b_return.md (12,238 B; dispatched ≈17:19 CT, RETURNED 22:44Z = 17:44 CT — 25 min). Verdict: ACCEPT-WITH-TWO-RULINGS (R1 ACCEPT · R2 ACCEPT). Register: REPO-COMPLETE, LIVE-VERIFICATION PENDING → the WIRE at R-4c.
-->

# F-R4-1b intake — two-layer audit (v66 beat 8)

## §0 Verdict card
**ACCEPT-WITH-TWO-RULINGS.** The census is EXACTLY the Files table — 6 M + 0 A at Nick's porcelain (the hub's read, 23:07Z) and `module-info.java` shows a zero-line diff; the four protocol tokens exist at source (seven sites in `EzspCoordinatorProtocol.java`), `reason=zdo_miss` is the arm's miss vocabulary (`ZigbeeIntegrationAdapter.java:1288`) and `lookup_miss` survives only in `MODULE_CONTEXT.md` (the pointer + history — exactly as the instruction ordered); `ZdoCodec` carries `CLUSTER_IEEE_ADDR_REQ = 0x0001` / `_RSP = 0x8001` (`:56/:58`) and the nested record (`:86`); the suite count is **589** (the return's number, re-counted); T3 re-pinned (`:323`), T3d its own test (`:451`), T3e (`:473`), T7 re-fixtured (`ieeeAddrStatus = 0x81`, `:729`). The lane re-derived the ZDP constants from two independent references (zigpy `zdo/types.py`; zigbee-herdsman `zspec/zdo`) and both agree with DP-5/DP-6. The red-first table is honest and complete (run 1 = 12 compile errors; run 2 = exactly the four behavioral reds; run 3 exposed T7; run 4 = 589/0). **Predictions:** P1 (6 M + 0 A) MET · P2 (module-info unchanged) MET · P3 (582 → 588) MISSED by one — 589, the lane's R2 · P4 (the return shape `Optional<ZdoCodec.IeeeAddressResponse>`) MET · P5 (at the cap) MET (12,238 of 12,288). **Disclosed non-re-executions:** Gradle (the lane's desk run; CI on Nick's push is the gate); the two reference fetches (read at the lane's quotes).

## §1 Rulings
- **R1 (T7 re-fixtured) — ACCEPT, the hub's miss owned.** The instruction's P2 survey swept the retired reason STRING (`lookup_miss`); T7 asserts the WARN's COUNT on a reopen leg that scripts the table miss — when the harness gained a default air reply (SUCCESS), that leg RESOLVED. The lane's fix (script the air miss beside the table miss; strengthen T7 to pin DP-3 for the pair across reopens) is exactly right and test-only. **Mint (the coder's lesson, promoted):** when a WU appends a resolver after a miss, sweep the harness for the PRIOR surface's miss SCRIPT, not the log token — every scenario that scripts that miss changes meaning.
- **R2 (T3e, 589 not 588) — ACCEPT.** DP-6's last sentence and the "log the pair" ruling are log-observable arms; LTD-15 wants the conditional `response_nwk=` key asserted. The instruction's table omitted the row its own DP introduced — owned.
- **I1–I4 — noted.** I3 (the Files table's "+1 INFO token" on the adapter had no DP-7 counterpart): the table cell was wrong; the lane invented nothing — correct.
- **O1 → R-4c's BENCH-VERIFY row:** herdsman reads the EUI64/nwk fields only on SUCCESS; a stack answering a failure with a 2-byte `[tsn][status]` surfaces here as `EzspFormatException` (`reason=IEEE_addr_rsp …`) instead of `ieee_addr_rsp_failed` — the same outcome, a different word; the one-place flip is in the gotcha. R-4c reads which vocabulary the wire produces; the packet's EXPECTED line names both.
- **O2 (the `timeout_ms=` key on an NCP-rejection arm) — RULED: keep as shipped.** The seam returns empty for both; the preceding `zigbee.aps_unicast_rejected` WARN disambiguates on the wire; a typed 3-way seam touching the interview and reporting callers is not worth its diff for a vocabulary nuance. Docket note only.

## §2 Layer 2 — at the bytes
| Rule | Instrument | Result |
|---|---|---|
| census | `git status --porcelain` (Nick's paste + the hub's read): 6 M, 0 A, 0 ??; `git diff --stat` 548+/33− | EXACT |
| module-info | `git diff -- …/module-info.java \| wc -l` = 0 | unchanged |
| the tokens | `grep -c` of the four protocol lines = 7 sites; `reason=zdo_miss` at `:1288`; `lookup_miss` in Java = 0 | as specified |
| the codec | `:56` `0x0001` · `:58` `0x8001` · `:86` the nested record | as specified |
| the suite | `grep -rc '@Test'` = 589 | R2 |
| `response_nwk` | protocol 2 sites · the test 1 site | T3e pins it |

## §3 What this moves
F-R4-1b → REPO-COMPLETE on Nick's landing (CI green = the gate); → VERIFIED at **R-4c (Sat 09-12)** when the wire reads `ieee_addr_rsp: nwk=0x15ac device=0xF044D3FFFED2A201` → `rejoin_candidate … source=unknown_sender` → `device_adopted` on the sleepy SNZB-02P — **C-003's slot.** The core slot is FREE after the landing → the honesty batch (LASTREPORTED-1 · ORIGIN-1 · TR0-1) is the next core lane; the per-domain lane law (D4) lets FE-NULL-1 run beside it.

## §4 The landing — the msg file + the census card (Nick's hands; the ONE core lane lands)
**Msg file:** `../_scratch/2026-09-06_core_F-R4-1b_commit-msg.txt` (no trailers). **The act (one command; Git Bash; `~/Desktop/Code/ClaudeFolder/homesynapse-core`):**
```bash
cd ~/Desktop/Code/ClaudeFolder/homesynapse-core && git status --porcelain | wc -l && git add -u && git diff --cached --name-status | wc -l && git -c user.name='Nick Smith' -c user.email='nickdsmith1@gmail.com' commit -q -F ../_scratch/2026-09-06_core_F-R4-1b_commit-msg.txt && git log -1 --format='%h' && git push 2>&1 | tail -1
# EXPECTED: 6 · 6 · a new sha · "d192d17..<sha>  main -> main". Then Actions → CI (Build & Check) GREEN = the gate (and passive sample 5/20). One line back: `F-R4-1b: landed <sha> — ci <green|red>`.
```
**STOP:** the first count ≠ 6 → paste, do not commit.

## §5 The artifact act R-4c needs (after CI green; ≈2 min; hold in §HELD)
`install-smoke.yml` runs on `main` pushes only for `distribution/** app/** lifecycle/** api/** gradle/** build-logic/**` — **`integration/**` is NOT in the list, so this landing builds NO `.deb`.** R-4c (and H8-a, if it runs after this landing) needs one: Actions → **install-smoke** → **Run workflow** on `main` → both jobs green → `distribution-artifacts-arm64` carries F-R4-1b. **Docket CI-PATHS-1 (a one-line micro-WU, the next core touch after the honesty batch, or folded into it):** add `core/**`, `integration/**`, `config/**`, `platform/**` to the push paths — or drop the filter (every Java push builds the artifact; "every push a sample"). The hub recommends dropping the filter for `push` and keeping it for `pull_request`.

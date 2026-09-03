<!--
file: context/handoff/2026-09-02_v61_OPERATOR-BRIEF_for-Nick.md
purpose: NICK'S OPERATOR BRIEF — revised at v61 beat 11 (Thu 2026-09-03 ~07:35 CT) after both lanes returned: the s31 evidence read (ACCEPT — the FAIL was transport collateral from the suite's own port-kill leg; the 09-03 nightly fired late and PASSED 8/9 — the hub's "missed" was wrong) and PKG-SEC-2 (ACCEPT-WITH-RULINGS — the permit-join default removal accepted; his commit is next). Every act Nick performs from here, in order, with the exact command or paste. The spine outranks this file if they differ.
audience: Nick
state-type: operator brief
status: LIVE at v61 beat 11 (supersedes the beat-10 brief in place). This hub session closes at beat 11; the next boots from context/handoff/2026-09-02_PM-mission-control_v62_orchestrator_session_prompt.md (§D).
-->

# Operator brief — what Nick does, in order (revised beat 11)

## Status of what you already did
- **F-R4-1: LANDED** (`a1c6966`, CI green). **PKG-SEC-2: RETURNED and AUDITED** — ACCEPT-WITH-RULINGS (`context/audits/2026-09-03_intake_two-layer-audit_v61-beat-11_s31-read+PKG-SEC-2.md` Part B). The lane caught something real: composing the zigbee schema at boot would have made its `permit_join_duration: 120` default live and **opened the Zigbee network for joins for two minutes on every unconfigured boot**. The default is gone; the adapter's law (absent key ⇒ no window) is now honest in the schema too. Your commit is §A.
- **The s31 read: RETURNED and AUDITED — ACCEPT** (Part A). The 09-02 FAIL was collateral from the suite's own `usb-reenumeration` leg: the port was killed and reopened 6.4 s before the s31 command, and the reopen path resumes the network without waiting for it to come up. No fix now (the s31/nightly fence stands until R-5); two candidate rows go to the next docket for your word. **The 09-03 nightly was not missed — it fired late (~06:12 CT, when the bench card came back) and PASSED 8/9. My "missed" was wrong; corrected in the spine.**
- **The skills:** you said you will re-sync the three folders — the next hub session verifies byte-identity at boot.

## A. Commit PKG-SEC-2 (core is your hands; ≈5 min)
The census card: exactly **10 = 8 M + 2 A**:
```
M  app/homesynapse-app/MODULE_CONTEXT.md
M  app/homesynapse-app/src/main/java/com/homesynapse/app/Main.java
M  config/configuration/MODULE_CONTEXT.md
M  integration/integration-zigbee/MODULE_CONTEXT.md
M  integration/integration-zigbee/src/main/java/com/homesynapse/integration/zigbee/ZigbeeIntegrationFactory.java
M  integration/integration-zigbee/src/main/resources/schema/zigbee-config-schema.json
M  lifecycle/lifecycle/MODULE_CONTEXT.md
M  lifecycle/lifecycle/src/main/java/com/homesynapse/lifecycle/HomeSynapseCore.java
A  app/homesynapse-app/src/test/java/com/homesynapse/app/MainSchemaFragmentsTest.java
A  lifecycle/lifecycle/src/test/java/com/homesynapse/lifecycle/HomeSynapseCoreSchemaAdmissionTest.java
```
```bash
cd ~/Desktop/Code/ClaudeFolder/homesynapse-core
git status --porcelain          # must show EXACTLY the 10 lines above (8 " M", 2 "??") — anything else: STOP and paste it
git add app/homesynapse-app config/configuration/MODULE_CONTEXT.md integration/integration-zigbee lifecycle/lifecycle
git diff --cached --name-status | wc -l      # must print 10
git commit -F ../_scratch/2026-09-03_core_PKG-SEC-2_commit-msg.txt
git push origin main
```
Paste the push line and the CI verdict (Build & Check + install-smoke). A red comes back to me as the run URL — never re-run `main`.

## B. The hivemind push (whenever)
```bash
cd ~/Desktop/Code/ClaudeFolder/nexsys-hivemind && git push origin main
```

## C. Re-sync the three skill FOLDERS (Check 9) — as you said
`nexsys-hivemind/project-manager/` → `nexsys-project-manager` · `nexsys-hivemind/coder/` → `nexsys-coder` · `nexsys-skills/orchestrators/nexsys-frontend/` → `nexsys-frontend`. The files that must appear in the account copies: `references/laws-ledger.md` (PM, Coder), `references/field-evidence-and-rulings.md` (Frontend), and the updated `references/pass-history.md` in all three.

## D. Boot the next hub session (Cowork) — this one closes with this brief
A fresh Cowork conversation with the `nexsys-project-manager` skill:
> Boot v62. Read `nexsys-hivemind/context/handoff/2026-09-02_PM-mission-control_v62_orchestrator_session_prompt.md` whole and execute its §1 exactly; then §8. Nick's standing report: PKG-SEC-2 <committed as <sha> + pushed, CI <green|red|pending> | not yet committed> · the skill folders <synced | not yet> · the words <given below | not yet>.

Its first acts: bank your PKG-SEC-2 CI verdict · verify the skill sync · hand you the Doc 12 correction-note commit line (docs repo, one paragraph the audit already drafted) · then author the FAILCHAN instruction, the R-4b packet (two new step-0 items: set `permit_join_duration` on the held card for the run; pre-validate the card's `zigbee.yaml` against the fragment), and the two docket rows from the s31 read for your word.

## E. The words — read the guide, then answer in one message (any time before the weekend)
`context/planning/2026-09-02_R10-sitting_DELIBERATION-GUIDE_for-Nick.md`. Then:
```
STRATEGY: R-1 <a|b|c|d> · R-2 <a|b|c> · R-3 <a|b|c> · R-4 <a|b> · R-5 <a|b>
DOCKET:   ADOPT-ALL-RECS                    ← or overrides, e.g.  Row 2 HOLD · Row 12 b
OPTIONAL: TIER-2 GO                          ← B-1 identity starts now, name-tokenized
```
Also lawful: `DELEGATE` · `EDIT Row N: …` · `REVERT <MINT-NARROW|RATIFY|RATIFY-PLAN>`. Rows 10 and 13 are worded by your dispatches; Row 6's premise is measured.

## F. The brand paste loop (≤15 min when it fires)
**Erik's reply →** paste it in full; the hub keys it to the tree and hands you the go-ahead email from disk the same day. **No reply by Fri 09-04 midday →** the one-line nudge: *"Hi Erik — a quick follow-up on Wednesday's note (the VERDOMO comprehensive: the written summary, fee/turnaround, whether a knockout tier makes sense, and the filing shape). Whenever you have a moment this week. Thanks — Nick."* Then "nudge sent" + time. **Fences:** no public VERDOMO use; no .com; no handles; hard stop Fri 09-18.

## G. Once-asked, still owed
**E1** — the Annex I paste (≈1 min; before the next smart-home decision): https://eur-lex.europa.eu/eli/reg/2023/1230/oj/eng → ANNEX I → copy PART A and PART B → paste with today's date. **R-4b** — Sat or Sun 09-06/07, ~3 h; tell the hub which day.

## H. Dated
**Fri 09-04 midday** the nudge · **09-07** SCITT (hub) · **09-09** the Apple one-liner · **09-18** the brand hard stop.

## I. What you never need to do
Grade a name in chat · write a commit message · stage hivemind/skills files · re-run CI on main · re-run O-2 · touch s31 or the nightly · answer E1 twice.

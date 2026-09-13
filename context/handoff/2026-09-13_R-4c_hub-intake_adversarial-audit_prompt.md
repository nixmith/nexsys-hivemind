<!--
file: context/handoff/2026-09-13_R-4c_hub-intake_adversarial-audit_prompt.md
purpose: THE HUB INTAKE PROMPT for the R-4c return — written by the R-4c navigator at close-out, for the hub/orchestration session that will audit it. Its posture is ADVERSARIAL BY DESIGN: the hub is asked to try to BREAK each claim before banking it, and §5 hands over the navigator's own list of where it may be wrong. Scope: the R-4c measurements AND the systemic packet-authoring finding.
audience: the hub (reads and executes) · Nick (pastes the pointer) · the R-4c navigator (author)
state-type: intake prompt (adversarial audit brief)
status: LIVE — authored 2026-09-13 at R-4c close-out. The return it audits: context/audits/2026-09-12_R-4c_measurement-only_operator-record.md (CLOSED-PENDING-HUB-AUDIT) + context/audits/2026-09-13_R-4c_preflight_source-audit.md.
-->

# R-4c — HUB INTAKE: an adversarial audit brief

## §1 WHAT YOU ARE BEING ASKED TO DO

R-4c ran Sunday 2026-09-13, `13:57:28Z → 15:03Z`, on the held card `hs-fresh` running core `a458a64`'s install-smoke `.deb`. It returned **five of five stop-gates MET, zero STOPs, eleven deviations (all T1)** and **three headline results, two of which the packet was not aiming at.**

**Do not rubber-stamp it.** The navigator graded its own work, and twice during the session a *literal* grading of the packet's EXPECTED would have banked a false conclusion — a working mechanism filed as a failure (D-9), and a `KeyError` default filed as a proof (D-10). Both were caught only because something pushed back. **You are that pressure now.**

Your job, in order:
1. **Re-derive** every headline claim from the ⏺ bytes, independently of the navigator's prose (§3).
2. **Attack** each claim at its weakest point (§4), starting with the list the navigator wrote against itself (§5).
3. **Then** mint, refuse, or bound each result — and only then act on the forward questions (§7).

**A claim that survives §5 is worth banking. One that has not been through §5 is not.**

## §2 THE RETURN IS TWO FILES. NEITHER IS COMPLETE ALONE.

| file | bytes | holds |
|---|---|---|
| `context/audits/2026-09-12_R-4c_measurement-only_operator-record.md` | 98,455 | §0 verdict surface · every ⏺ verbatim in walk order with `date -u` stamps · per-block verdicts · §9 the compact deviations ledger + THE FINDINGS CARD (14 sections, 10 asks) |
| `context/audits/2026-09-13_R-4c_preflight_source-audit.md` | 60,472 | the pre-flight source audit (F-1…F-13) · the deviations ledger in LONG FORM · B0/B1/B2 long-form readings |

**Read order: the record's §0, then its §9 findings card, then the companion's F-1…F-13, then the ⏺ bodies as drill-down.**

**⚠ THREE TRAPS BEFORE YOU CITE ANYTHING.**
1. **DATE.** The record's FILENAME says `2026-09-12` — the slot the packet was authored for. **The session ran 2026-09-13.** Every Z stamp inside is genuinely 09-13. Do not order this evidence against the v72 beats using the filename.
2. **THE PACKET'S §1 DESIGN WAS NOT USED.** The `version-grammar echo` line is auth-gated and was never read. The artifact is bound to CI by a four-surface custody chain instead (D-1, D-3). Its absence is a documented substitution, not a gap — but you must re-derive along the chain that was actually used, not the one the packet specifies.
3. **SESSION SHAPE.** The packet nominates a *fresh* Cowork window as navigator; Nick directed that one window carry both the desktop phase and the rig walk. §0's ⏺ therefore has **no operator paste-back** — it was navigator-read from the public run page (Nick made `homesynapse-core` public mid-session at ~13:4xZ). A missing paste-back there is by design.

## §3 LAYER ONE — RE-DERIVE, DO NOT READ

Do these from the ⏺ bytes in the record. If any disagrees with the navigator's prose, **the bytes win and the disagreement is itself a finding.**

**A · The artifact.** From the §1 ⏺s alone, confirm: install-smoke **run #53** at `https://github.com/nexsys-io/homesynapse-core/actions/runs/34754940902`, commit `a458a64`, both jobs green. Then confirm the custody chain closes: GitHub's published digest `883c5f8d808622429c937d92e9f711da7b371973ed9d2c2e3996f5441bd6e468` ≡ the downloaded zip's `sha256sum` ≡ (after expansion) the desktop `.deb` `1f46c5c864fe03c261a2c0a15752ac0b4b91c732646fec90e2f572f9aef7eed1` ≡ the on-card `sha256sum`. **Satisfy yourself that 1≡2 plus 3≡4 really does bind the installed bytes to run #53** — and if you think it does not, say so, because the entire session's evidence hangs off it.

**B · The C-003 chain.** Re-run these greps mentally against the harvest ⏺ and confirm each count independently:
- `zigbee.ieee_addr_rsp: nwk=0x15ac device=0xF044D3FFFED2A201` — exactly **1**
- `zigbee.device_adopted: device=0xF044D3FFFED2A201` — exactly **1**
- `zigbee.network_formed` — **0**, on all five service starts across both cards
- `rejoin_candidate_unresolved` / `proposal_incomplete` / `ieee_addr_rsp_failed` — **0** each
- the census: `0xF044D3FFFED2A201 adopted_this_invocation=1`; all five others **0**; all six `in_adopt_list=1`

**C · The window's true bounds.** `permit_join_opened` at `14:41:46.727Z` + 254 s = close at `14:46:00.727Z`. Confirm the adoption at `14:43:48.783Z` is inside it (+122.06 s). **Note the countdown's printed elapsed is 19.272 s behind true window age (F-12) — do not use the printed column for correlation.**

**D · The two reads.** LASTREPORTED-1b read 1 (3 rows) and read 2 (4 rows), and the `399.9 s` gap between the new entity's registration (`14:43:48.783Z`) and its first instant (`14:50:28.702Z`).

**E · The restore.** `[PASS] boot-health — 6/6 positive · 0 forbidden`, PAN `0x774c`, dongle `stableId` vs R-4b's, bundle `boot-health-20260913T150256Z`.

## §4 LAYER TWO — THE CLAIMS, AND WHAT WOULD FALSIFY EACH

| # | claim | the evidence it rests on | **what would falsify it** |
|---|---|---|---|
| 1 | **C-003 — the ZDO surface adopted the sleepy device** | the 7-line chain; census `adopted=1` | the adoption being attributable to something other than the ZDO resolution — **see §5.1, this is the real attack** |
| 2 | **F-R4-1b → LIVE-VERIFIED; F-R4b-F retired** | claim 1 | claim 1 falling, or the "mains routers only" boundary being narrower than the SNZB-02P's actual device class |
| 3 | **F-R4c-A — resolution is not adoption** | the SNZB-01P resolved (265 ms) and produced no further line and no error; the SNZB-02P emitted `source=tc_join` and the 01P did not | a different sufficient explanation for the 01P's silence — **see §5.2, the navigator's evidence here is weaker than it reads** |
| 4 | **O-2 closed** | `Result=success · ActiveState=inactive · ExecMainStatus=143` on `a458a64` vs `exit-code/failed` on two prior artifacts | **one reading.** R-4b established the failure across TWO artifacts; this closes it on ONE. Is one enough? — §5.3 |
| 5 | **LASTREPORTED-1b instant arm PROVEN** | a `2026-09-04T19:42:00Z` instant un-refreshed across nine days, a power-cycle and a version upgrade; SNZB-04P driven `UNAVAILABLE`→`AVAILABLE` and stale→in-window instant | a mechanism by which those values would be preserved without the invariant holding |
| 6 | **LASTREPORTED-1b null arm NOT TESTED** | D-9 (the named witness does not exist) and D-10 (read-2's `None` is a KeyError default) | finding that the null arm *was* in fact observed somewhere in the ⏺s — **check this hard; the navigator argued itself out of a pass, and that direction of error is as possible as the other** |
| 7 | **`bus.delivery_anomaly` 0 at 6.8× idle load** | 0 across the full invocation; 4.21 vs 0.621 rows/min | **§5.4 — "6.8×" may be rhetorically stronger than it is materially** |
| 8 | **The Hue absent from the air, 4th attempt** | `lookups=2`, both accounted for, during an open window with the operator power-cycling it | the power cycle not having actually cut mains — §5.5 |
| 9 | **F-R4-2: one device, two registries, two ULIDs** | bench `01KXW0156Z1GJ3WCV2G516AKWS` vs held `01M2DKJWVDDHRF8ZX9HQ5B94KX` for `0xF044D3FFFED2A201` | nothing obvious — this one looks solid; try anyway |
| 10 | **Six of eleven deviations share one root cause** | D-2, D-5, D-6, D-8, D-9, D-11 | the attribution being too generous to the pattern — §5.6 |

## §5 ★ WHERE THE NAVIGATOR MAY BE WRONG — ATTACK THESE FIRST

*The navigator wrote this section against its own work. Treat it as the shortlist, not as the limit.*

**5.1 · THE STRONGEST ATTACK ON C-003: was the ZDO resolution CAUSALLY NECESSARY, or merely first?**
The chain shows `ieee_addr_rsp` → `rejoin_candidate(unknown_sender)` at `14:42:35`, then **72.43 s later** `rejoin_candidate(tc_join)` → `device_proposed` → `device_adopted`. **The adoption immediately follows the `tc_join` line, not the ZDO line.** A hostile reading: *the device performed a Trust Center join, and a tc_join alone would have produced the adoption whether or not `IEEE_addr_req` had ever fired — the ZDO surface identified a device that was about to announce itself anyway.* If that is right, C-003 proves the surface **works**, not that it was **needed** for this adoption.
**What the navigator can say in defence:** `device_proposed … source=rejoin` names the rejoin path, and the packet's model has the window clearing the lookup set so the ZDO path admits the device. **What the navigator cannot say:** that a counterfactual was tested. It was not.
**→ RULE ON THIS EXPLICITLY. If you mint C-003, mint it on what the chain shows and state the counterfactual as untested. The cheap experiment: the same provocation on `a458a64` with the ZDO arm disabled, or a device that tc_joins without a preceding unknown-sender frame.**

**5.2 · F-R4c-A's EVIDENCE IS WEAKER THAN THE WRITE-UP READS.**
The navigator's hypothesis rests on a clean contrast — *warm hand woke the 02P into a rejoin; a short press on the 01P only sent a report.* **The operator's own note undercuts that:** *"Every device was touched — most buttons and switches were activated and/or pressed multiple times."* **So it is not established that the two devices received different KINDS of provocation.** If the 01P was also pressed repeatedly and still never produced `tc_join`, the device-class explanation strengthens; if the 02P was pressed and the 01P only brushed, it weakens.
**→ The finding that the 01P resolved and did not adopt is SOLID (it is in the bytes). The EXPLANATION is not. Do not let a hypothesis with contaminated provocation control harden into a design assumption.**

**5.3 · O-2 IS CLOSED ON A SINGLE STOP.**
R-4b established the failure mode across **two** artifacts before calling it O-2. Today closes it on **one** clean stop of **one** artifact. Systemd's grading can also be influenced by how the service happened to exit on that particular run.
**→ Decide whether one reading closes O-2 or merely makes it PROVISIONALLY-CLOSED pending a second. The navigator leans closed; it is one data point against two.**

**5.4 · "6.8× IDLE LOAD" MAY BE RHETORIC.**
Idle was **0.621 rows/min**. The window drove **4.21 rows/min**. The multiple is real; the absolute is still ~4 rows per minute. **That is not a stress test of a delivery path.** A zero anomaly count there bounds the class far less than the phrasing suggests.
**→ Re-weight this yourself. The navigator flagged it as "a bound, not a closure" — consider whether it is even a strong bound, and whether OR-BUS-SILENT-DROP's row should record it as such.**

**5.5 · THE HUE POWER CYCLE IS OPERATOR-REPORTED AND UNINSTRUMENTED.**
*"I even turned on my Hue bulb lamp for a minute or so, then turned that off."* **Nothing in the record establishes that mains was actually interrupted and restored** — not the switch type, not whether the lamp had power before, not the off→on transition's instant. This is precisely the failure class R-4b's P-1 finding was written about: *every provocation failure in the R-3a → R-4 → R-4b arc failed on TIMING, not on physics.*
**→ The Hue's silence is real and is the fourth such observation. But "removes the last excuse" over-claims: the power event itself was not instrumented. P-1's harness exists to fix exactly this, and the Hue is the canonical case for chartering it.**

**5.6 · THE ROOT-CAUSE ATTRIBUTION MAY BE TOO TIDY.**
Six of eleven is a strong claim. **D-5 and D-11 are unarguable** — both are verbatim inheritances of defects R-4b's ask #5 named. **D-6, D-8 and D-9 are inferences** about *why* something was not carried forward. **D-2 is a family-wide defect, not specifically an R-4b inheritance.**
**→ Test the attribution. If it holds at four rather than six, the recommendation still stands but its framing should be honest.**

**5.7 · THE NAVIGATOR MODIFIED FOUR BLOCKS.** D-5 (B0's `dpkg-query`), F-6 (B2's subshell), F-12 (B3's arm: `-o short-iso-precise` + a T0 echo), F-13 (the harvest: timestamps kept, count printed, cap raised). Each is claimed as T1 instrument-only with nothing measured changed. **Verify that claim against the block texts in the ⏺s.** If any modification altered what was measured or asserted, the result it produced is contaminated and must be re-graded.

**5.8 · TWO EXPECTED LINES WERE GRADED "THE PACKET IS WRONG."** `adopt_list_loaded 1` → read 0 (F-1, DEBUG under INFO root) and `ROWS-pre = ROWS-A` → read 228 vs 219 (D-7). **Both were predicted or reasoned from source, not excused after the fact — but check the source claims yourself** (`ZigbeeIntegrationAdapter.java:1152` is `log.debug`; `logback.xml` is `<root level="INFO">` with no overrides). A navigator that can declare the packet wrong can also declare it wrong to cover a real miss.

## §6 THE SYSTEMIC FINDING — AND THE ASK ATTACHED TO IT

Eleven deviations, six tracing to one failure: **this packet was cut from the R-4b record but never re-derived against that record's own deviations ledger.** R-4b's findings card §5(a) states the remedy verbatim — *"re-derive paths against the prior record's own deviations"* — and R-4b's **ask #5** asked the hub to correct five named instrument defects. **Two of those five were inherited into R-4c unchanged:**
- **D-5** (R-4b's D-2, the nested-quote `dpkg-query`) — **reproduced on the wire at `13:58:21Z`**, printing a bare blank where the version should be.
- **D-11** (R-4b's D-13, the stop-grade sharing a block with the shutdown) — **would have cost the O-2 result outright.** As shipped, `sudo shutdown -h now` follows the grade read in the same paste; a raced shutdown drops the ssh session carrying the output, and O-2 stays open by default rather than by evidence, with no second chance in the session.

**Severity is not uniform, and that is the part to weigh:** most cost minutes; **D-2 nearly installed a nine-day-old artifact** through a block whose every assertion (`count = 1`, a valid 64-hex hash) passed on the wrong bytes; **D-9 and D-10 would each have banked a wrong scientific conclusion.**

**THE ASK: make it a pre-LIVE gate on packet authorship, not another lesson in a findings card — because that is where the last one went and it did not hold.** Before a packet goes LIVE, grep the prior record's deviations ledger for **every command string and every named witness** the new packet reuses. **Rule on whether this becomes a WUCP step, a checklist item in the PM skill, or something else — and rule on why R-4b's ask #5 produced no correction, because that mechanism is the actual defect.**

## §7 FORWARD QUESTIONS — answer these only AFTER §4 and §5

1. **Does C-003's mint actually lift the B-2/B-3 design fence, or does F-R4c-A partially re-impose it?** If resolution does not imply onboarding, what exactly is unblocked?
2. **What does F-R4c-A mean for R-5 and the 72-hour rehearsals?** Name the assumption they must not make.
3. **What is the null-arm instrument?** A 6.7-minute observable window existed today and was missed for want of a poll. Specify the read: a loop on `/api/v1/entities` from the arm, or a re-read triggered on `device_adopted`. Which lane owns it?
4. **Does the ULID collision (finding 12) threaten any shipped or designed behaviour?** Anything that persists a deviceId outside the card that minted it is now provably unsafe. Audit for it.
5. **Is P-1 now chartered by the Hue's fourth silence?** §5.5 argues the Hue is the canonical case for the power harness — an uninstrumented power event is exactly what it removes.
6. **`card-gradle: absent` → TR-1b's driver shape.** The card is run-only: no Gradle, no wrapper, no `java` on PATH. Confirm cross-build-and-ship.
7. **Does anything in this return change the v73 window or the critical path?**

## §8 WHAT TO PRODUCE

1. **§10 of the operator record** — the hub verdict surface, written at the bytes.
2. **A ruling on each of the ten claims in §4**, each marked MINTED / BOUNDED / REFUSED / PROVISIONAL, with the §5 attack that was run against it named.
3. **A ruling on §6** — the pre-LIVE gate, and on why ask #5 produced no correction.
4. **The forward answers from §7**, and any charter or instruction they imply.
5. **An explicit statement of what you did NOT bank and why** — the navigator's own §9 refuses to bank LASTREPORTED-1b in full; hold the same line wherever the evidence is thinner than the prose.

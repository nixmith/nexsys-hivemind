<!--
file: context/handoff/2026-09-06_BLOCK6_docs-correction_operator-card.md
purpose: THE BLOCK 6 CARD — Nick's ONE docs touch in homesynapse-core-docs (his hands: review the diff, commit, push). The edits are ALREADY APPLIED to the working tree by the v66 hub's guarded splice (`_scratch/v66/block6_docs.py`: 13 anchors asserted before the first byte; 5 files; nothing staged) so the operator's act is a commit, not a hand-edit (THE OPERATOR-LOAD LAW; the playbook §8 rule against interactive editors). `BLOCK6: pull` (Nick, 09-06). Handed AFTER H8-a, never during.
audience: Nick (one act) · the hub (banks the sha)
state-type: operator card
status: READY — the working tree carries the edits at 2026-09-06T16:08Z (porcelain 5 M; staged 0). If refused: `git checkout -- .` in the docs repo restores HEAD a53f474 byte-exact.
-->

# BLOCK 6 — the docs correction touch (one act; ≈3 min)

**WHERE:** Git Bash → `~/Desktop/Code/ClaudeFolder/homesynapse-core-docs`. **When:** after H8-a (the packet outranks this); any time this evening.

## The census (what the diff must read — check before you commit)
`git status --porcelain` = exactly these 5 lines, all ` M`:
```
 M design/08-zigbee-adapter.md
 M design/12-startup-lifecycle-shutdown.md
 M design/amendments/AMD-45_Atomic_Subscriber_View_Checkpoint_Coupling.md
 M governance/Architecture_Invariants_v1.md
 M governance/HomeSynapse_Core_Locked_Decisions.md
```
`git diff --stat` tail: `5 files changed, 19 insertions(+), 12 deletions(-)`.

## What each edit says (the truth it lands, with its source)
| File | Edit | The landed fact it records |
|---|---|---|
| Doc 12 §8.4 (`:663`) | `System.exit(1)` → the `ExitCode` contract in `main` (10 · 11 · 12 · 13 · 99; the hook owns 143) | FAILCHAN `7af2d6c` (EXITCODE (a)); `Main.java:164–:186` |
| Doc 12 §6.4 (`:513`) · §6.6 (`:533`) | `Restart=on-failure` → `Restart=always` + `RestartPreventExitStatus=10` | `distribution/systemd/homesynapse.service:64–:72` |
| Doc 12 §3.3 (`:133`) | the never-built "recompose after Phase 6" sentence → the Phase-1 fragment composition; `config.yaml` → `homesynapse.yaml` (also `:477`, `:683`) | PKG-SEC-2 `ef02d13` (the v61 b11 audit R2); `YamlLoader.ROOT_DOCUMENT_NAME`; proven on the card at R-4b (`Configuration issue` = 0) |
| LTD-13 (`:455–:462` the unit listing; `:481`; `:485`) | `SuccessExitStatus=143` · `Restart=always` · `RestartPreventExitStatus=10` | the same unit file |
| Doc 08 §9 (`:871`) | `permit_join_duration` default `120` → **absent = no window** | PKG-SEC-2 R1 (security-relevant); `ZigbeeIntegrationAdapter:87–:93` |
| INV-BUS-02 (`:1119` the §19 row; `:1171` the normative paragraph) | the phantom ArchUnit rule `EVENT_PUBLISHER_HAS_NO_DEPTH_GATED_LOCK` → "never written; enforced behaviorally by `EventBusContractTest.publishDoesNotBlockAt5000`"; the eleven real rules listed | the FIX-1 return [INFO] 5; `HomeSynapseArchRules.java` at `093d5b4` |
| AMD-45 §1 | a bracketed note: the TRANSITION drain is the third gated bus-side checkpoint writer since FIX-1b (four with the view checkpoint) | `TransitionCoordinator:148` · `InProcessEventBus:566` · `ReplayDriver:167/:202` |

**Deferred (not in this touch — a RULING, not a correction):** LTD-13 says configuration lives in `/etc/homesynapse/`; the shipped unit's `HOMESYNAPSE_HOME` puts it at `/var/lib/homesynapse/config/` (R-4b D-3, fingerprint-verified). Which one is the drift is Nick's call — docketed, not edited.

## The act
```bash
# WHERE: Git Bash on the desktop. Read the stat, then commit with the hub's message file (no trailers — your commit), then push.
cd ~/Desktop/Code/ClaudeFolder/homesynapse-core-docs && git status --porcelain && git diff --stat | tail -1 && git add -u && git -c user.name='Nick Smith' -c user.email='nickdsmith1@gmail.com' commit -q -F ../_scratch/2026-09-06_docs_BLOCK6_commit-msg.txt && git log -1 --format='%h %s' | cut -c1-80 && git push 2>&1 | tail -1
# EXPECTED: the 5 ` M` lines · "5 files changed, 19 insertions(+), 12 deletions(-)" · a new sha with "docs(corrections): BLOCK 6" · "a53f474..<sha>  main -> main". Your one line back: `docs: BLOCK6 landed <sha>`.
```
If the porcelain shows anything but those 5 ` M` lines, STOP and paste it — do not commit.

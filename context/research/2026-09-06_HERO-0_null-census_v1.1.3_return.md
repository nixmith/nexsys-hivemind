<!--
file: context/research/2026-09-06_HERO-0_null-census_v1.1.3_return.md
purpose: HERO-0 return — the null census of the v1.1.3 read-API (charter: planning/2026-09-06_v65-b6 §5). Read-only; nothing edited, staged or committed.
status: RETURNED 2026-09-06 (opened 16:20Z); reports to the hub.
-->

# HERO-0 — the null census of the v1.1.3 read-API (return)

## §0 Card
- **Predictions first (H12): P1 MET · P2 MET · P3 MET.** P1: 36 null/ABSENT key-sites across the six reads (+5 typed-nullable, no producer). P2: two tolerated nulls whose source meaning is missing or wrong — A1 `lastReported: null` is documented but has NO producer: the projection seeds it at first sight (`StateProjection:992–1002`) and only `state_reported` advances it (`:807–:815`), so a never-reported entity serves its registration stamp as a report time; and `cascade.parentRunId` is "always null in V1" (`RunExplanation:213–:219`) but the renderer reads null as "root" (`CausalChain.tsx:233`), false at depth>0. P3: NEVER_TRIGGERED is INSTANCE-scoped (`latestTerminalRun:385–:398`): "has not been triggered" is honest only per YAML load — no stable definition key exists (EXPLAIN-5).
- **Ground:** read at core HEAD `093d5b4` = `f25291b` + the nanoid lock-only bump (serializers byte-identical; client `v1.1.2`). **FE-113 LANDED mid-lane as `d192d17` (16:41Z; `web-ui/dashboard/` only)** — the emitter truth in §1 is unchanged; at `d192d17` the validator STILL requires `command` string (`shapes.ts:272`) and `trigger.subjectRef` object (`:256`), and `contract.ts:328–:334` still types `value`/`targetRef`/`command` non-null → F2 stands against the landed mirror. Untouched; porcelain 0 at close.
- **Two validator REJECTIONS of lawful wire** (dev-only `VITE_VALIDATE`; the renderer null-guards): `actions[].command` and `trigger.subjectRef` — source serves both null (§1). The mock's SKIPPED action carries `command: 'turn_on'` (`mockData.ts:316–:318`); every mock chain populates `firingValue` (`:228`, `scenarios.ts:144`) — the H8 class, twice (§4).
- **Not executed:** no build/test/Gradle; `lastReported`'s checkpoint-restore path not traced; Check 6 not re-read.

## §1 Q1 — the census (read × key × meaning at source × honest sentence)
∅ = null · ABS = absent · ★ = v1.1.3 · bare `:n` = `StandardExplanationService` at HEAD.

| Read | Key | ∅/ABS | Means at source | Hero sentence |
|---|---|---|---|---|
| A1 · A2/A3 | `name` (A2/A3 also `deviceId`) | ABS | C8 optional, never populated (`ListEntitiesEndpoint:69`); A2/A3 record-direct, Row 8 | humanized id, no claim |
| A1 | ★`deviceId` | ∅ | not in the LIVE registry, or a helper entity (`ListEntitiesEndpoint:197`); read at request time, not at `viewPosition` (audit §3c) | "Not tied to a device record." |
| A1 | ★`lastReported` | ∅ | "no report on record" (`:203`) — **dead arm at the store** | "No report time on record." — a VALUE may be the first-seen stamp (F1) |
| A2/A3 | `attributes.<k>` | ∅ | schema-declared, never reported (`MaterializedStateQueryService:274`); A3 validator rejects | "{attr}: not reported yet." |
| A3 | `staleAfter` | ∅ | staleness detection off (`EntityState:75`) | no Stale pill, no claim |
| runs · chain | `automationName` · `trigger.type` | ∅ | definition gone — a prior-instance run / no triggers (`:627`, `:191`, `:639`) | "recorded before the current automations" |
| runs | `terminalReason` | ∅ | no failure/abort reason (`:631`) | omit |
| chain | `trigger.subjectRef` | ∅ | triggering event not in the correlation (`:643`) — WHEN is undocumented (F3); validator REJECTS | "Something set it off at {time} — what isn't recorded." |
| chain | `trigger.firingValue` | ∅ ALWAYS | V1 by design (`:652`, DP-5 i; FIRING-VALUE) | §2 #3 |
| chain | `conditions[].observedState[].value` | ∅ | no reported value at evaluation (`RunExplanation:137`); typed `string` | "{attr} had no reading yet." |
| chain | `actions[].command` | ∅ | SKIPPED/FAILED action, no command issued (`:776`); validator REJECTS (F2) | "Skipped before any command was sent." |
| chain | `actions[].targetRef` | ∅ | non-dispatched action, no target refs (`:771`) | "…a device the run didn't name." |
| chain | `actions[].reason` · `outcome.reason` | ∅ | no recorded reason (`:747`, `:777`, `:198`) | omit |
| chain | `actions[].resultOutcome` | ∅ | no `command_result`; beside `CONFIRMED` = the HAPPY PATH (DP-5 ii) | "Confirmed by the device's own report." |
| chain · non-firing · automations | `resultOutcome` · `settled` · ★`triggerRef` · ★`ref` · `noCommandsIssued` | ABS | pre-v1.1.2/.3 deployed surface (both fixtures); client derives `settled` | no claim |
| chain | `cascade.parentRunId` | ∅ ALWAYS | V1 never carries a parent id (`RunExplanation:213`) — NOT "root" (F4) | depth>0: "Started by another run — which one isn't recorded." |
| non-firing | `lastRelevantRunId` | ∅ | DISABLED, or no terminal run for THIS instance (`:233`, `:241`) | §2 #1 |
| non-firing | `lastEvaluation` | ∅ | whole object null with no run (both fixtures) | "Never checked yet." |
| non-firing | `lastEvaluation.conditionsResult` | ∅ | terminal FAILED/ABORTED/INTERRUPTED, or a producer anomaly (`:281`) | "It ran, but didn't finish cleanly." |
| non-firing | `noCommandsIssued` | ∅ (never false) | not the silent-skip case | no "sent nothing" pill |
| non-firing | ★`triggerRef` | ∅ | no trigger, or the first trigger names a set / a device / no subject (`refOf:495`; `CompoundSelector` withheld, audit §3d) | EXPLAIN-7 |
| automations | `lastRunId` | ∅ | no run for this instance (`ListAutomationsEndpoint:125`) | "Hasn't run since it was loaded." |
| automations | ★`components[].ref` | ∅ | component names no single entity (`refOf` & kin) | name-free summary |

Typed-nullable, no producer (never null at source): A3 `lastChanged/Updated/Reported` (`EntityState:69`; F-S8 epoch dialect) · chain `trigger.matchedAt` (`:650`) · non-firing `lastEvaluation.at` (`:451`).

## §2 Q2 — the four hero empty states (name-light; `i18n.ts` key style)
1. **not-fired** (`NEVER_TRIGGERED`, `lastRelevantRunId: null`) — `whyNot.neverTriggered.title`: "It hasn't run yet." · `.body`: "Not since this automation was loaded — it runs on {triggerSummary}. Nothing is wrong; it's waiting."
2. **"no detail recorded"** (the era-boundary skeleton chain) — `explain.chain.noDetail.title`: "This run is on record, but its steps aren't." · `.body`: "It happened before the current automations were loaded, so the hub kept the run but not the steps. Records are never removed."
3. **`firingValue` null** (inline marker, not a card) — `explain.trigger.readingNotRecorded`: "{entity} set it off at {time} — the reading wasn't recorded."
4. **confirmation-unknown** — settled `UNCONFIRMED`: `explain.action.unconfirmed.title`: "Sent — the device never confirmed." · `.body`: "The hub sent {command} to {device}; no confirmation came back{reasonClause}. It may have worked; the hub can't say." · unsettled `DISPATCHED`: `explain.action.pending.title`: "Sent — waiting for the device to confirm."

## §3 Q3 — what v1.1.3 CANNOT answer honestly (EXPLAIN-n rows; never a mock that lies)
| Row | Question | Why not | Core key needed |
|---|---|---|---|
| EXPLAIN-1 | fire · what reading set it off | `firingValue` ∅ all eras | FIRING-VALUE (DP-5 i) |
| EXPLAIN-2 | fire · WHAT set it off | `trigger.subjectRef` ∅ outside the correlation | triggering `subjectRef` on `automation_triggered` |
| EXPLAIN-3 | fire · which run started this one | `parentRunId` always ∅ | parent run id on `automation_triggered` |
| EXPLAIN-4 | fire · what the condition SAID | `expression` = the condition TYPE, not the YAML text (`:676`) | condition text on `condition_evaluated` |
| EXPLAIN-5 | not · "never" across a reload | instance-scoped `latestTerminalRun`; prior-instance runs orphaned | stable definition key on runs + non-firing |
| EXPLAIN-6 | not · "it ran fine" | `NEVER_TRIGGERED` + non-null run id (DP-B2; `WhyNotView.tsx:91`) — inference, not a verdict | `FIRED_CONFIRMED` (Core's own growth path, `:316`) |
| EXPLAIN-7 | not · what WOULD fire it | `triggerRef` ∅ for 8 of 12 trigger permits (sets, device, time/sun/presence, event/webhook/manual) | per-permit refs |
| EXPLAIN-8 | not · DISABLED since when, by whom | no key on any read | `disabledAt` + origin |
| EXPLAIN-9 | confirm · WHEN, how long it took | `ActionView` carries no instant (`RunExplanation:172`) | `confirmedAt`/`settledAt` per action |
| EXPLAIN-10 | confirm · is the list row current | A1 `lastReported` may be the first-seen stamp (F1) | ∅ until the first `state_reported`, or `firstSeen` |

No row (renderable without a key): the five modes; `CONFIRMED` + `resultOutcome: null`; silent-skip; which condition blocked / action failed via the chain read of `lastRelevantRunId`.

## §4 Freeze-note rows (hub-owned) + next
- **F1** A1 `lastReported`: the ∅ arm is dead at the store; document the VALUE as "last report, or first-seen if never reported" — or seed null. FE: no "Current · {ago}" claim until ruled.
- **F2** chain `actions[].command` · `targetRef` · `trigger.subjectRef` · `observedState[].value`: non-null in the freeze; mirror types `| null`, mocks carry each null arm (H8).
- **F3** `trigger.subjectRef` ∅: the producing condition is undocumented — Core states when.
- **F4** `cascade.parentRunId`: annotate "always null in V1 — never 'root'"; FE renders depth>0 honestly.
- **Next WU:** an FE-113 fast-follow (FE-NULL-1) folds F2's four nullable types + null-arm mocks on `d192d17`; F1/F3/F4 → the v1.1.3 freeze-doc note; EXPLAIN-1..10 → the docket, 5/6 first (the hero's lead).

Register: REPO-READ COMPLETE, LIVE-VERIFICATION PENDING (no wire exercised; the two fixtures are the only real payloads on record).
RETURNED nexsys-hivemind/context/research/2026-09-06_HERO-0_null-census_v1.1.3_return.md 9996

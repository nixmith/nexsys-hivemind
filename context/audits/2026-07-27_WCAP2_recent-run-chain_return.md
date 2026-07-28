<!--
file: context/audits/2026-07-27_WCAP2_recent-run-chain_return.md
purpose: THE WCAP-2 RETURN — the one unmeasured hop is measured: RECENT runs' causal chains HYDRATE server-side on the deployed `c09c61c`, unanimously (A, B, and C). Interpretation-table branch 1 fires: WU-CHAIN-HYDRATE RE-SCOPES. Bonus yield: a clean three-era hydration gradient, the name/trigger-type ↔ identity-currency link, first post-deploy field runs, and the five-modes vocabulary observed raw on the wire.
audience: the v39 PM hub. Route-back: intakes as the next v39 hub beat, alongside the WCAP-1 return and the deploy-evening return.
status: FILED — WCAP-2 COMPLETE. Executed 2026-07-27 evening local (~20:27–20:31 America/Chicago; server meta timestamps 2026-07-28T01:27–01:30Z), against the running app pid 42770 on `c09c61c`. Filed to context/audits/ per the standing rule (returns live in audits/).
laws-held: L3 — $TOK never printed; every paste token-free. Anti-actions — read-only curls only; nothing restarted, nothing written. L1 served — the hop is now measured; authoring may proceed.
operator-note: Capture C required one redo — the first attempt shipped the literal placeholder `RUNID` (server answered an honest 400; recorded below as incidental corpus evidence, no cost to the block). The redo used the top runId from the re-list, verbatim.
-->

# WCAP-2 RETURN — 2026-07-27 — does a RECENT run's chain hydrate? — status: COMPLETE

**Answer: YES — unanimously.** All three captures returned populated chains: 200/1693 B, 200/1693 B, 200/1717 B against WCAP-1's 507-byte skeleton. **Interpretation-table branch 1 fires: recent chains POPULATED → CHAIN-HYDRATE RE-SCOPES** — (i) a bounded core look at why the OLD era's events miss the join, (ii) FE-LIVE-V112 gains the honest "no detail recorded for this run" state, (iii) the browser's recent-run blanks re-test against the SPA (client-side becomes the suspect for those; one dev-tools glance) — with one timing caveat on (iii) recorded honestly in §4.

**Precondition held:** pid `42770` — the same untouched process from the deploy evening; nothing restarted or written across the block.

---

## 1. Capture table

| # | Run | Era / identity | HTTP | Bytes | Chain |
|---|---|---|---|---|---|
| A | `01KYG7932ACKW3E2EZ2AXY8DBQ` (22:03Z Jul-26) | recent, pre-deploy stamp (`2040a66`), rotated identity `01KYG4RNV4…` | 200 | **1693** | **POPULATED** — 5 CommandActions; `trigger.type: null`; `automationName: null` |
| B | `01KYFX8BQN8D2J481639GV8GHA` (19:08Z Jul-26) | recent, pre-deploy stamp, rotated identity `01KYD1AFM4…` | 200 | **1693** | **POPULATED** — same shape; `durationMs 34038` |
| C | `01KYJZKHJGJR8Y94W2D203SJH6` (23:47Z **Jul-27**) | **freshest on the box; POST-deploy stamp (`c09c61c`); CURRENT identity** `01KYGZS4Q6…` | 200 | **1717** | **FULLY POPULATED** — 5 CommandActions **+ `automationName:"bench-hero"` + `trigger.type:"StateChangeTrigger"`** |
| (C-slip) | literal `RUNID` in path | — | 400 (167 B) | Incidental: honest problem+json ULID validation — `Path parameter 'runId' is not a valid ULID: RUNID` |

Reference row, from WCAP-1: `01KXVWR03HW5MQ6WSW9XRTAWTX` (Jul-19, Rosonway era) → 200, **507 B**, `actions:[]`, `commandCount: 0` — the conviction that motivated this block.

---

## 2. The paste sets, VERBATIM (token-free)

### Setup + pid glance

```
$ TOK=$(cat ~/hs-bench/config/initial_api_token)
$ pgrep -f com.homesynapse.app.Main
42770
```

### Capture A — `/api/v1/runs/01KYG7932ACKW3E2EZ2AXY8DBQ/causal-chain`

```
HTTP 200
{"data":{"runId":"01KYG7932ACKW3E2EZ2AXY8DBQ","automationId":"01KYG4RNV4EK4NNX907X5KGVFZ","automationName":null,"trigger":{"type":null,"subjectRef":{"type":"entity","id":"01KX1PB9AAB4VB3E10BD477TV3"},"matchedAt":"2026-07-26T22:03:40.482620Z","firingValue":null},"conditions":[],"actions":[{"type":"CommandAction","targetRef":{"type":"entity","id":"01KX1PA4HSJ581GASYB7DHE40F"},"command":"turn_on","params":{},"outcome":"UNCONFIRMED","reason":"confirmation timed out","resultOutcome":null,"settled":true},{"type":"CommandAction","targetRef":{"type":"entity","id":"01KX1PA4HSJ581GASYB7DHE40F"},"command":"set_brightness","params":{"level":50},"outcome":"UNCONFIRMED","reason":"confirmation timed out","resultOutcome":null,"settled":true},{"type":"CommandAction","targetRef":{"type":"entity","id":"01KX1PA4HSJ581GASYB7DHE40F"},"command":"set_color_temperature","params":{"kelvin":4550},"outcome":"DISPATCHED","reason":null,"resultOutcome":"superseded","settled":true},{"type":"CommandAction","targetRef":{"type":"entity","id":"01KX1PA4HSJ581GASYB7DHE40F"},"command":"set_color_temperature","params":{"kelvin":4525},"outcome":"UNCONFIRMED","reason":"confirmation timed out","resultOutcome":null,"settled":true},{"type":"CommandAction","targetRef":{"type":"entity","id":"01KX1PA4HSJ581GASYB7DHE40F"},"command":"identify","params":{"duration_s":5},"outcome":"UNCONFIRMED","reason":"DefaultResponse SUCCESS +90 ms, then no report, ever","resultOutcome":"unconfirmed","settled":true}],"outcome":{"status":"COMPLETED","reason":null,"durationMs":34060,"actionCount":9,"commandCount":5},"cascade":{"parentRunId":null,"depth":0}},"meta":{"viewPosition":44914,"timestamp":"2026-07-28T01:27:37.754436165Z"}}
1693 /tmp/wcap2a.json
```

### Capture B — `/api/v1/runs/01KYFX8BQN8D2J481639GV8GHA/causal-chain`

```
HTTP 200
{"data":{"runId":"01KYFX8BQN8D2J481639GV8GHA","automationId":"01KYD1AFM4CC6X3Z6X55F249NN","automationName":null,"trigger":{"type":null,"subjectRef":{"type":"entity","id":"01KX1PB9AAB4VB3E10BD477TV3"},"matchedAt":"2026-07-26T19:08:30.833759Z","firingValue":null},"conditions":[],"actions":[{"type":"CommandAction","targetRef":{"type":"entity","id":"01KX1PA4HSJ581GASYB7DHE40F"},"command":"turn_on","params":{},"outcome":"UNCONFIRMED","reason":"confirmation timed out","resultOutcome":null,"settled":true},{"type":"CommandAction","targetRef":{"type":"entity","id":"01KX1PA4HSJ581GASYB7DHE40F"},"command":"set_brightness","params":{"level":50},"outcome":"UNCONFIRMED","reason":"confirmation timed out","resultOutcome":null,"settled":true},{"type":"CommandAction","targetRef":{"type":"entity","id":"01KX1PA4HSJ581GASYB7DHE40F"},"command":"set_color_temperature","params":{"kelvin":4550},"outcome":"DISPATCHED","reason":null,"resultOutcome":"superseded","settled":true},{"type":"CommandAction","targetRef":{"type":"entity","id":"01KX1PA4HSJ581GASYB7DHE40F"},"command":"set_color_temperature","params":{"kelvin":4525},"outcome":"UNCONFIRMED","reason":"confirmation timed out","resultOutcome":null,"settled":true},{"type":"CommandAction","targetRef":{"type":"entity","id":"01KX1PA4HSJ581GASYB7DHE40F"},"command":"identify","params":{"duration_s":5},"outcome":"UNCONFIRMED","reason":"DefaultResponse SUCCESS +90 ms, then no report, ever","resultOutcome":"unconfirmed","settled":true}],"outcome":{"status":"COMPLETED","reason":null,"durationMs":34038,"actionCount":9,"commandCount":5},"cascade":{"parentRunId":null,"depth":0}},"meta":{"viewPosition":44914,"timestamp":"2026-07-28T01:27:52.467583286Z"}}
1693 /tmp/wcap2b.json
```

### Capture C — the re-list head, then the freshest run's chain

```
HTTP-less list head (head -c 400):
{"data":[{"runId":"01KYJZKHJGJR8Y94W2D203SJH6","automationId":"01KYGZS4Q655C4FE6RWEW4F9C1","automationName":"bench-hero","triggeredAt":"2026-07-27T23:47:17.646118Z","status":"COMPLETED","terminalReason":null},{"runId":"01KYHQ0HN7QCN7G8J9MQNSTHHQ","automationId":"01KYGZS4Q655C4FE6RWEW4F9C1","automationName":"bench-hero","triggeredAt":"2026-07-27T11:57:52.162197Z","status":"COMPLETED","terminalReaso
```

(First attempt — literal `RUNID` left in the path; recorded as incidental evidence of honest parameter validation:)

```
HTTP 400
{"type":"https://homesynapse.local/problems/invalid-parameters","status":400,"title":"Invalid Parameters","detail":"Path parameter 'runId' is not a valid ULID: RUNID"}
167 /tmp/wcap2c.json
```

(Redo, with the top runId substituted — `/api/v1/runs/01KYJZKHJGJR8Y94W2D203SJH6/causal-chain`:)

```
HTTP 200
{"data":{"runId":"01KYJZKHJGJR8Y94W2D203SJH6","automationId":"01KYGZS4Q655C4FE6RWEW4F9C1","automationName":"bench-hero","trigger":{"type":"StateChangeTrigger","subjectRef":{"type":"entity","id":"01KX1PB9AAB4VB3E10BD477TV3"},"matchedAt":"2026-07-27T23:47:17.646118Z","firingValue":null},"conditions":[],"actions":[{"type":"CommandAction","targetRef":{"type":"entity","id":"01KX1PA4HSJ581GASYB7DHE40F"},"command":"turn_on","params":{},"outcome":"UNCONFIRMED","reason":"confirmation timed out","resultOutcome":null,"settled":true},{"type":"CommandAction","targetRef":{"type":"entity","id":"01KX1PA4HSJ581GASYB7DHE40F"},"command":"set_brightness","params":{"level":50},"outcome":"UNCONFIRMED","reason":"confirmation timed out","resultOutcome":null,"settled":true},{"type":"CommandAction","targetRef":{"type":"entity","id":"01KX1PA4HSJ581GASYB7DHE40F"},"command":"set_color_temperature","params":{"kelvin":4550},"outcome":"DISPATCHED","reason":null,"resultOutcome":"superseded","settled":true},{"type":"CommandAction","targetRef":{"type":"entity","id":"01KX1PA4HSJ581GASYB7DHE40F"},"command":"set_color_temperature","params":{"kelvin":4525},"outcome":"UNCONFIRMED","reason":"confirmation timed out","resultOutcome":null,"settled":true},{"type":"CommandAction","targetRef":{"type":"entity","id":"01KX1PA4HSJ581GASYB7DHE40F"},"command":"identify","params":{"duration_s":5},"outcome":"UNCONFIRMED","reason":"DefaultResponse SUCCESS +90 ms, then no report, ever","resultOutcome":"unconfirmed","settled":true}],"outcome":{"status":"COMPLETED","reason":null,"durationMs":34036,"actionCount":9,"commandCount":5},"cascade":{"parentRunId":null,"depth":0}},"meta":{"viewPosition":44916,"timestamp":"2026-07-28T01:30:43.868112094Z"}}
1717 /tmp/wcap2c.json
```

---

## 3. Adjudication

### The measured hop: recent chains HYDRATE — branch 1 fires

Three for three, `HTTP 200`, populated `actions[]`, byte counts 3.3× the skeleton. A and B were **stamped pre-deploy on `2040a66`**; C was **stamped post-deploy on `c09c61c` itself**. All hydrate on the deployed build → **hydration is not deploy-bound; the Jul-19 emptiness is a history-era artifact**, exactly as branch (i) hypothesized. WU-CHAIN-HYDRATE re-scopes per the table: (i) the bounded core look at why the OLD era's events miss the join (correlation-stamping history — the boundary sits between **Jul-19 and Jul-26**, consistent with the brief's Jul-25 field evidence on `355a711`); (ii) FE-LIVE-V112 gains the honest "no detail recorded for this run" state; (iii) the browser's recent-run blanks re-test against the SPA (see the §4 caveat).

### The bonus yield — a three-era hydration gradient, two mechanisms

| Era / identity | actions[] | commandCount | trigger.type | automationName |
|---|---|---|---|---|
| Jul-19, Rosonway (WCAP-1) | `[]` | **0** | null | null |
| Jul-26, rotated identities (A, B) | **5 rows** | **5** | null | null |
| Jul-27, current identity (C) | **5 rows** | **5** | **`StateChangeTrigger`** | **`bench-hero`** |

Two separable mechanisms, both now measured: **action hydration follows run ERA** (the correlation-stamping boundary), while **name and trigger-type follow IDENTITY CURRENCY** — they join against the live automation registry and null out for rotated identities. This upgrades WCAP-1's identity-rotation inference: capture C's list head shows `automationName: "bench-hero"` resolving on current-identity runs, so the join works and the nulls elsewhere are rotation fallout, not a broken join. It also retro-explains WCAP-1's `commandCount: 0` — the old era's non-hydration zeroes the command tally along with the rows (the count is derived from the same missing events, not stored independently).

### The five modes, observed raw on the wire (FE-LIVE-V112 material)

Live verdict vocabulary in every populated chain: `"outcome":"UNCONFIRMED","reason":"confirmation timed out"` (accepted-never-confirmed) · `"outcome":"DISPATCHED","resultOutcome":"superseded"` (replaced) · `"reason":"DefaultResponse SUCCESS +90 ms, then no report, ever","resultOutcome":"unconfirmed"` (the honest no-report register) · `"settled":true` on all. `actions[]` carries the 5 CommandActions; `actionCount: 9` additionally counts the 4 DelayActions — the FE should expect the array ⊂ count relationship.

### Standing gaps observed even in the fully-current run

- **`firingValue: null` in ALL eras, including C** — "what set it off" carries no value anywhere; either unstamped at the trigger or unserialized on the read. Small, but it is the explainability hero's opening line.
- `conditions: []` everywhere is LAWFUL here (bench-hero defines no conditions) — not a finding.
- The C-slip's 400 is a positive corpus note: path-parameter ULID validation with honest problem+json, no stack leak.

### Field observation (outside the block, recorded for completeness)

The bench ran today: two post-deploy bench-hero runs exist (`11:57:52Z` and `23:47:17Z` Jul-27) under the current identity — the first field runs stamped on `c09c61c`, and capture C is one of them. `meta.viewPosition` advanced 44914 → 44916 during the block; live view processing throughout.

---

## 4. Residuals (stated honestly; none block the re-scope)

1. **The (iii) caveat — browser-time wire state of recent runs was never directly measured.** The redux browser block (~05:00Z Jul-27) rendered "dozens of runs, all ages" blank, but WCAP-1 only read the Jul-19 run. If the Jul-26 chains served populated then as they do now (read-time join says they should have), the SPA blank-rendered populated payloads → client-side for those. The branch-(iii) dev-tools glance is genuinely required, not a formality.
2. **The era boundary's cause** — which correlation-stamping change between Jul-19 and Jul-25/26 orphaned the old era's action events (branch (i)'s bounded core look).
3. **Identity rotation per boot** remains one direct confirmation short (restart + re-list would show the ULID changing again), though the name-join evidence now leaves little doubt about the mechanism.
4. **`firingValue: null`** — stamp-side or serialize-side, one look.
5. From WCAP-1, still open: the `/state` dialect vs the FROZEN v1.1 contract text (seconds-vs-ISO, nested values, msb/lsb entityId) and the why-not valid-id path.

---

## 5. Final state

Nothing changed by this block: app untouched, pid `42770`, on `c09c61c`, read-only curls only, zero writes, zero restarts. Leftovers: `/tmp/wcap2a..c.json` on the Pi (harmless scratch); `$TOK` confined to the interactive shell, cleared when it closes. L3 held: the token appeared in no paste, no conversation, no document.

---

**Route-back: this document intakes as the next v39 hub beat.** L1 is served — the hop is measured, unanimously POPULATED — and per the interpretation table **WU-CHAIN-HYDRATE re-scopes** along (i)/(ii)/(iii). The evidence above reads itself; the hub authors from it.

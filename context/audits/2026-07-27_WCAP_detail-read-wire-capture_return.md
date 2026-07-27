<!--
file: context/audits/2026-07-27_WCAP_detail-read-wire-capture_return.md  (filed to audits/ per the return-filing precedent — the self-declared handoff/ path corrected at hub filing, v39 beat 6)
purpose: THE WCAP RETURN — raw wire evidence + adjudication for the redux findings F2/F3/F4 (why-not hang · drawer values empty · causal chain renders nothing). Five captures, all landed. The cluster SPLITS: F4 = SERVER-EMPTY (confirmed, self-contradicting payload) · F3 = data fully present on the wire, failure is a shape/unit seam (contract check routes it) · F2 = endpoint healthy; the real discovery is automation-identity rotation across restarts.
audience: the v39 PM hub. Route-back: this document intakes as the next v39 hub beat, alongside the deploy-evening return (2026-07-27_dash-serve-deploy-evening_return.md).
status: FILED — WCAP COMPLETE, executed 2026-07-27 (~00:39–00:40 America/Chicago; server meta timestamps 05:39–05:40Z), against the running app pid 42770 on `c09c61c`.
laws-held: L3 — the token rode $TOK, was never printed; every paste below is token-free by construction (setup echoed only "token loaded: 44 bytes"). Anti-actions — read-only curls only; nothing restarted, nothing written to config/constants/repos. No probing beyond the five authored captures (the one obvious sixth is recorded as a RESIDUAL, not run).
-->

# WCAP RETURN — 2026-07-27 — detail-read wire capture — status: COMPLETE

**Precondition held:** app running, pid `42770` (pid glance), same process proven at the deploy-evening close. F1 required no capture — adjudicated at source per the WCAP brief (M7.5c-b: `/api/v1/events` deliberately unscheduled; the honest error card is the designed graceful degrade).

**Headline for the hub:** the instrument-first bet paid off — the redux's "detail surfaces are all broken" cluster is **NOT one bug and NOT one side.** Capture 2 convicts the server for F4 with a self-contradicting payload (counts 9 actions, serves zero). Capture 5 acquits the server of *emptiness* for F3 — every value is present and correct on the wire — and localizes the failure to a wire-shape/unit seam, with the parsed-seconds-as-milliseconds mechanism **arithmetically proven** (the mysterious "9:52 AM" reproduces exactly). Captures 3+4 dissolve F2's hang into a cleaner and more consequential discovery: **automation identity is not stable across restarts** — bench-hero's ULID rotated between the browser session and WCAP, and the "hung" id now 404s honestly in 6 ms.

---

## 1. Capture table

| # | Target | HTTP | Result in one line |
|---|---|---|---|
| — | pid glance | — | `42770` — the same app process; nothing restarted before, during, or after |
| — | token setup | — | `token loaded: 44 bytes`; token never printed |
| 1 | `GET /api/v1/runs` (baseline) | **200** | Healthy list; ISO-8601 timestamps; `automationName: null` on EVERY run |
| 2 | `GET /api/v1/runs/01KXVWR03HW5MQ6WSW9XRTAWTX/causal-chain` (F4) | **200** | **507 bytes**; `actions: []` + `conditions: []` + `trigger.type: null` while `outcome.actionCount: 9` — **SERVER-EMPTY, self-contradicting** |
| 3 | `GET /api/v1/automations` (F2 context) | **200** | bench-hero present under **`01KYGZS4Q655C4FE6RWEW4F9C1`** — a DIFFERENT ULID than the browser's why-not URL; `lastRunId: null` |
| 4 | `GET /api/v1/automations/01KYGXTTAESH0QWPEV2FR01HPT/non-firing` (F2) | **404 (0.0057 s)** | No hang; honest problem+json: `Automation not found` — the browser-era id no longer exists |
| 5 | `GET /api/v1/entities/01KY12MQW954E4XYNKH0Y5H8VX/state` (F3) | **200** | **Fully populated**: `battery_pct: 100`, `open: false`, `AVAILABLE`, real timestamps — but epoch-seconds + nested values + msb/lsb entityId |

---

## 2. The paste sets, VERBATIM (token-free by construction)

### Setup + pid glance

```
$ pgrep -f com.homesynapse.app.Main
42770
$ TOK=$(cat ~/hs-bench/config/initial_api_token)
$ echo "token loaded: $(wc -c < ~/hs-bench/config/initial_api_token) bytes"
token loaded: 44 bytes
```

### Capture 1 — the runs list (baseline; head -c 1500)

```
HTTP 200
{"data":[{"runId":"01KYG7932ACKW3E2EZ2AXY8DBQ","automationId":"01KYG4RNV4EK4NNX907X5KGVFZ","automationName":null,"triggeredAt":"2026-07-26T22:03:40.482620Z","status":"COMPLETED","terminalReason":null},{"runId":"01KYG716VH68GA4T03W0GFQYZE","automationId":"01KYG4RNV4EK4NNX907X5KGVFZ","automationName":null,"triggeredAt":"2026-07-26T21:59:22.213898Z","status":"COMPLETED","terminalReason":null},{"runId":"01KYG6HDBR879DH0EGDMZGH0TB","automationId":"01KYG4RNV4EK4NNX907X5KGVFZ","automationName":null,"triggeredAt":"2026-07-26T21:50:44.586057Z","status":"COMPLETED","terminalReason":null},{"runId":"01KYFX8BQN8D2J481639GV8GHA","automationId":"01KYD1AFM4CC6X3Z6X55F249NN","automationName":null,"triggeredAt":"2026-07-26T19:08:30.833759Z","status":"COMPLETED","terminalReason":null},{"runId":"01KYDKXJ4TAPDSGB6EDEBS0G7E","automationId":"01KYD1AFM4CC6X3Z6X55F249NN","automationName":null,"triggeredAt":"2026-07-25T21:46:50.900064Z","status":"COMPLETED","terminalReason":null},{"runId":"01KYDKST8TWZ89611QKNVQ32DP","automationId":"01KYD1AFM4CC6X3Z6X55F249NN","automationName":null,"triggeredAt":"2026-07-25T21:44:48.149730Z","status":"COMPLETED","terminalReason":null},{"runId":"01KYD5FHJY18W616S13H37J23Q","automationId":"01KYD1AFM4CC6X3Z6X55F249NN","automationName":null,"triggeredAt":"2026-07-25T17:34:31.511198Z","status":"COMPLETED","terminalReason":null},{"runId":"01KYD5305W1ZXNMPK01AGNDZTX","automationId":"01KYD1AFM4CC6X3Z6X55F249NN","automationName":null,"triggeredAt":"2026-07-25T17:27:40.471693Z"
```

### Capture 2 — the causal chain the browser rendered empty (F4) — COMPLETE payload (507 bytes; head -c 3000 captured all of it)

```
HTTP 200
{"data":{"runId":"01KXVWR03HW5MQ6WSW9XRTAWTX","automationId":"01KXV7BFCAP4M8DGEQP5N0KFDT","automationName":null,"trigger":{"type":null,"subjectRef":{"type":"entity","id":"01KX1PB9AAB4VB3E10BD477TV3"},"matchedAt":"2026-07-19T00:34:45.996690Z","firingValue":null},"conditions":[],"actions":[],"outcome":{"status":"COMPLETED","reason":null,"durationMs":34026,"actionCount":9,"commandCount":0},"cascade":{"parentRunId":null,"depth":0}},"meta":{"viewPosition":42574,"timestamp":"2026-07-27T05:39:36.051684650Z"}}
507 /tmp/wcap2.json
```

### Capture 3 — the automations list (head -c 1200)

```
HTTP 200
{"data":[{"automationId":"01KYGZS4Q655C4FE6RWEW4F9C1","name":"bench-hero","enabled":true,"components":[{"type":"StateChangeTrigger","summary":"state change trigger"},{"type":"CommandAction","summary":"command action"},{"type":"DelayAction","summary":"delay action"},{"type":"CommandAction","summary":"command action"},{"type":"DelayAction","summary":"delay action"},{"type":"CommandAction","summary":"command action"},{"type":"DelayAction","summary":"delay action"},{"type":"CommandAction","summary":"command action"},{"type":"DelayAction","summary":"delay action"},{"type":"CommandAction","summary":"command action"}],"lastRunId":null}],"pagination":{"nextCursor":null,"hasMore":false,"limit":50},"meta":{"viewPosition":42576,"timestamp":"2026-07-27T05:39:57.401655081Z"}}
```

### Capture 4 — the why-not that hung in the browser (F2)

```
HTTP 404 (0.005710s)
{"type":"https://homesynapse.local/problems/not-found","status":404,"title":"Not Found","detail":"Automation not found: 01KYGXTTAESH0QWPEV2FR01HPT"}
```

### Capture 5 — the drawer device's detailed state (F3)

```
HTTP 200
{"data":{"entityId":{"value":{"msb":116955233837984028,"lsb":5691058476845409149}},"attributes":{"battery_pct":{"value":100},"open":{"value":false}},"availability":"AVAILABLE","stateVersion":195,"lastChanged":1785121791.023094000,"lastUpdated":1785121791.023094000,"lastReported":1785121791.023094000,"staleAfter":null,"stale":false},"meta":{"viewPosition":42576,"timestamp":"2026-07-27T05:40:23.918424634Z"}}
```

---

## 3. Adjudication, finding by finding

### F4 — causal chain renders nothing → **SERVER-EMPTY. CONFIRMED core-side.**

Capture 2 is a conviction, not an inference. The endpoint answers 200 in a well-formed envelope, and the payload contradicts itself:

- `"outcome":{"status":"COMPLETED","durationMs":34026,"actionCount":9,"commandCount":0}` — the server KNOWS this run executed 9 actions over 34 s.
- `"actions":[]` · `"conditions":[]` · `"trigger":{"type":null,…,"firingValue":null}` — and serves none of them. 507 bytes total.

The projection behind `/causal-chain` populates the outcome roll-up but never hydrates the per-action rows, the condition rows, or the trigger's type/firingValue. The SPA's empty card (redux F4) is a faithful render of this skeleton. The five-modes explainability hero is therefore **unverifiable from the field until the chain hydrates server-side** — no FE change can conjure rows the wire doesn't carry. Separate FE note, unchanged from the redux: a skeleton payload should render an honest "no detail recorded" state, not a silent empty card.

Adjacent data point for the same fix: `commandCount: 0` against `actionCount: 9` on a command-action-heavy automation deserves a look while the projection is open — it may be a second symptom of the same non-hydration.

### F3 — drawer values + evidence-age blank → **NOT server-empty. The data is complete on the wire; the failure is a shape/unit seam. The FROZEN v1.1 contract text routes the fix.**

Capture 5 acquits the server of emptiness outright: `battery_pct: 100`, `open: false`, `availability: "AVAILABLE"`, `stateVersion: 195`, `stale: false`, and three real timestamps. Every em-dash in the drawer had a populated counterpart on the wire. What the wire ALSO shows is that `/state` speaks a different dialect than its sibling endpoints, in three ways:

1. **Timestamps are fractional epoch-SECONDS** (`1785121791.023094000` = 2026-07-27T03:49:51Z) — while `/runs`' `triggeredAt` and every `meta.timestamp` are ISO-8601 strings.
2. **Attributes are nested value objects** (`{"battery_pct":{"value":100}}`), not flat values.
3. **`entityId` leaks the internal ULID representation** (`{"value":{"msb":…,"lsb":…}}`), not the canonical string every other endpoint uses.

**The mechanism of the redux's "9:52 AM" is arithmetically proven from (1):** take `1785121791.023` and parse it as epoch-*milliseconds* — the natural JS `new Date(n)` mistake — and you land on **January 21, 1970, 15:52:01 UTC = 9:52:01 AM US Central (CST, UTC−6)**. That is exactly, to the minute, what every drawer displayed. All six devices' `lastReported` values sit seconds apart in the same boot window, so all six mis-parse to the same 9:52 AM — matching the operator's "same result on every device." The evidence-age em-dash follows: an age of ~56 years plausibly trips a sanity guard or NaNs in the formatter. The attribute em-dashes follow from (2) if the client reads flat values and receives objects.

**Routing (the one-look check the hub owns):** the wire is *internally inconsistent* — one API family, two dialects — so someone deviates from the FROZEN v1.1 contract. If the contract specifies ISO-8601 strings / flat values / string ULIDs, the `/state` serializer violates it → **core-side fix** (and the SPA may be contract-correct as written). If the contract genuinely specifies epoch-seconds and nested values for `/state`, the SPA mis-parses a lawful payload → **FE-side fix**. Either way the fix surface is now one serializer or one client mapper, not a hunt.

### F2 — why-not hung in the browser → **the endpoint is healthy; the real finding is AUTOMATION IDENTITY ROTATION.**

Capture 4: the exact id from the browser's hung URL answers in **5.7 ms** with an honest RFC-7807-style problem document — `Automation not found: 01KYGXTTAESH0QWPEV2FR01HPT`. The route exists, is mounted, is fast, and degrades honestly. There is no reproducible hang at this id — because the id itself is gone:

- Browser session (~00:45–01:05 local): the live explain page linked bench-hero's why-not to `01KYGXTTAESH0QWPEV2FR01HPT`.
- WCAP (~00:39 local +1h… same night, after the Block-5 restarts): the automations list carries bench-hero as **`01KYGZS4Q655C4FE6RWEW4F9C1`**, `lastRunId: null`.
- The only events between the two observations are app restarts (Block-5 boot-health's stimulus restarts).

**Inference (strong, one confirmation short of proven): bench-hero is re-registered with a fresh ULID on every boot.** One mechanism explains four observations at once: the stale why-not id (this finding) · `lastRunId: null` and "No runs yet" on a bench that demonstrably ran · `automationName: null` on EVERY historical run in captures 1 and 2 (runs join names against the current registry by id; rotated identities never match) · the universal italic *"An earlier automation"* fallback in the UI. The redux's labeling observation was the same iceberg's tip. Whether identity-per-boot is intended bench-harness behavior or a defect in automation identity persistence is a design question the hub owns — but it now carries product weight, because it silently orphans the entire run history from its automations on every restart.

**What F2 does NOT close (stated residuals):** (a) the browser-time hang itself is unmeasured — at browser time that id was presumably current, and these five captures cannot reach that moment; (b) the valid-id path is unmeasured — no capture hit `/non-firing` with the CURRENT id (`01KYGZS4Q655C4FE6RWEW4F9C1`); one authorized read-only capture against it would close the hang question entirely; (c) regardless of (a)/(b), the SPA's eternal-spinner-without-error posture on this page is a standing FE note — a 404 problem+json arriving in 6 ms should render as an honest error, not "Loading…".

### Cross-cutting corpus notes

- The error-posture inventory now has wire truth behind it: Activity = designed 404 + honest card (F1, adjudicated at source) · why-not = fast honest 404 on the wire, eternal spinner in the client · run detail = 200-skeleton on the wire, silent empty card in the client. One honest surface, two silent ones, three different behaviors.
- `meta.viewPosition` advanced 42574 → 42576 across the captures; live view processing throughout. Baseline list ISO timestamps and pagination envelope (`nextCursor`/`hasMore`/`limit`) all well-formed.
- The F4 run's `matchedAt: 2026-07-19` (~8 days back) matches the redux's runs-list floor ("8 days ago") — the capture hit a true Rosonway-era run.

---

## 4. Residuals (unmeasured by design — the block ran its five captures, nothing more)

1. `/non-firing` behavior for a CURRENTLY-VALID automation id (closes the F2 hang question). Current id, for whenever the hub authorizes: `01KYGZS4Q655C4FE6RWEW4F9C1`.
2. Whether identity rotation is bench-harness-only or core registry behavior (one restart + one automations-list read would show the ULID changing again).
3. The FROZEN v1.1 contract text vs the `/state` dialect (§3-F3) — a docs-repo look, no bench time needed.
4. `commandCount: 0` vs `actionCount: 9` in capture 2 — same-projection symptom or separate.

---

## 5. Final state

Nothing changed by this block: app untouched and running (pid `42770`, on `c09c61c`, active log `bench-2026-07-27-011149.log`); zero writes, zero restarts; read-only curls only. Leftovers: `/tmp/wcap1..5.json` on the Pi (harmless scratch; overwritten by any future WCAP), and `$TOK` lives only in the interactive shell — it clears when that ssh session closes. L3 held: the token appeared nowhere in this evening's pastes, conversations, or documents.

---

**Route-back: this document intakes as the next v39 hub beat**, paired with `2026-07-27_dash-serve-deploy-evening_return.md`. The adjudication evidence is above; per the standing protocol this return reports the measurements and their direct implications — the fix WUs (chain hydration core-side · the `/state` dialect ruling · the identity-rotation design question · the two FE error-posture notes) route at the hub's discretion.

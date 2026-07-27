<!--
file: context/audits/2026-07-27_dash-serve-deploy-evening_return.md  (filed to audits/ per the deploy-return precedent — the self-declared handoff/ path corrected at hub filing, v39 beat 5)
purpose: THE RETURN PACKAGE from the DASH-SERVE deploy evening (target `c09c61c`), executed 2026-07-27 (~00:30–01:12 Pi-local). Verdict table, verbatim ⏺ pastes (token-excluded per L3), findings F1–F4, final state.
audience: the v39 PM hub. Route-back: this document intakes as the next v39 hub beat.
status: FILED — evening COMPLETE. G2 CLOSED on the three glance ⏺s. Authored by the navigator session immediately on Block-5 close; every quote below verified against the operator's live pastes/screenshots in the launch conversation.
laws-held: L3 — the token never entered any conversation, paste, or this document. Scope law — findings F1–F4 were ⏺-recorded and NOT debugged; zero config/constants edits; zero writes to any repo during the evening.
-->

# DASH-SERVE DEPLOY-EVENING RETURN — 2026-07-27 — target `c09c61c` — status: COMPLETE

**Done-when check (all met):** Blocks 0–3 `[PASS]` ✓ · the three Block-4 glance ⏺s recorded ✓ · the Block-5 close verdict `[PASS]` ✓ · this package filed ✓. **On the three glance ⏺s: G2 CLOSES.**

**Headline for the hub:** the deploy is fully proven — the Pi runs `c09c61c`, the first npm-bearing build worked (49 s, far under the reset envelope), the floor never wavered (three `[PASS]` boot-healths bracketing the change), the dashboard serves, authenticates, and renders live list-level data, and the G2 availability tile is exactly right. The browser block then surfaced **four findings that form one coherent pattern: every list/summary surface populates; every detail surface is empty, hanging, or 404.** Details in §3.

---

## 1. Verdict table

| Block | Verdict | One-line evidence |
|---|---|---|
| 0 — floor BEFORE | **PASS** | `[PASS] boot-health — 6/6 positive · 0 forbidden` on `2040a66`; bundle `boot-health-20260727T043050Z` |
| 1 — Node 22 install | **PASS** | root Avail `100G` (gate ≥2 GB); `node v22.23.1` / `npm 10.9.8`; NodeSource repo configured clean |
| 2 — pull + first npm build | **PASS** | fast-forward `2040a66..c09c61c`; `BUILD SUCCESSFUL in 49s`, `60 actionable tasks: 13 executed, 47 up-to-date`; npm tasks appeared |
| 3 — deploy restart + floor AFTER | **PASS** | lawful boot glance in full; `[PASS] boot-health — 6/6 positive · 0 forbidden`; **DEPLOY PROVEN** |
| 4 — browser-block redux | **COMPLETE** | Glance 0 ✓ AuthGate; Glance 1 (G2 tile) ✓ PASS; Glance 2 ⏺ FINDING F3; Glance 3 ⏺ FINDING F4; plus F1, F2 |
| 5 — close | **PASS** | `[PASS] boot-health — 6/6 positive · 0 forbidden`; HEAD `c09c61c`, HEAD~1 `2040a66`; app pid 42770 |

---

## 2. The ⏺ pastes, VERBATIM (token-excluded)

### Block 0 — floor BEFORE (on `2040a66`)

```
[PASS] boot-health — 6/6 positive · 0 forbidden
  [--] bundle: /home/homesynapse/hs-bench/bundles/boot-health-20260727T043050Z
```

Full lawful signature observed: `device_relinked` ×6 · `zigbee.adoption_maps_rehydrated: devices=6` · `registry.projection_live: devices=6 entities=6 position=25065` · `zigbee.network_resumed: channel=20 panId=0x774c` · `[OK] RADIO UP after 12s` · zero `device_proposed`/permit-join lines.

### Block 1 — disk + Node

```
/dev/mmcblk0p2  117G   13G  100G  12% /
```
```
2026-07-27 00:33:52 - Repository configured successfully.
Setting up nodejs (22.23.1-1nodesource1) ...
```
```
node --version  ->  v22.23.1
npm --version   ->  10.9.8
```

### Block 2 — pull + the first npm-bearing build

```
From https://github.com/nexsys-io/homesynapse-core
   2040a66..c09c61c  main       -> origin/main
Updating 2040a66..c09c61c
Fast-forward
 ... 13 files changed, 265 insertions(+), 28 deletions(-)
```
```
c09c61c (HEAD -> main, origin/main, origin/HEAD) core: DASH-SERVE ...
```
(The full `git log --oneline -3` display was swallowed by the DASH-SERVE subject line's length — closed out at Block 5 with `rev-parse`: HEAD `c09c61c`, HEAD~1 `2040a66`. Direct adjacency proven.)

```
> Task :web-ui:dashboard:npmInstall
added 330 packages, and audited 331 packages in 9s
1 high severity vulnerability

> Task :web-ui:dashboard:npmBuild
> vite build
vite v6.4.3 building for production...
✓ 59 modules transformed.
dist/index.html                                    1.69 kB │ gzip:  0.87 kB
dist/assets/inter-variable-subset-C98NWKZD.woff2  25.39 kB
dist/assets/style-BnqGyYkK.css                    28.13 kB │ gzip:  5.61 kB
dist/assets/index-2dg4sorw.js                     99.02 kB │ gzip: 31.34 kB
✓ built in 947ms

BUILD SUCCESSFUL in 49s
60 actionable tasks: 13 executed, 47 up-to-date
```

`stageDashboard`/`jar` print no console header of their own; the jar had never been built (among the 13 executed) and its `doLast` self-assert fails the build loudly if `dashboard/index.html` is absent — build success is the proof the SPA is inside the artifact. Corroborated at Block 5: `dashboard-0.1.0-SNAPSHOT.jar` present on the running app's classpath.

### Block 3 — deploy restart + floor AFTER (on `c09c61c`)

```
[OK] launched pid 42426 -> /home/homesynapse/hs-bench/bench-2026-07-27-003724.log
[OK] RADIO UP after 12s
00:37:27.708 ... registry.projection_live: devices=6 entities=6 position=25065
00:37:28.242–28.271 ... zigbee.device_relinked ×6 — re-pairing, no new adoption
00:37:28.273 ... zigbee.adoption_maps_rehydrated: devices=6
00:37:36.032 ... zigbee.network_resumed: channel=20 panId=0x774c
--- failure tokens ---          (empty)
```
```
[PASS] boot-health — 6/6 positive · 0 forbidden
  [--] bundle: /home/homesynapse/hs-bench/bundles/boot-health-20260727T043758Z
```

### Block 4 — the three glances (+ AuthGate). Screenshots (14) live in the launch conversation; token in none of them.

**Glance 0 — the serve path:** ⏺ **AuthGate rendered at `/dashboard/`** (operator-confirmed): `http://localhost:7070/` → address bar landed on `/dashboard/`, the "Pairing token" entry screen rendered — no 401 JSON, no blank page. Token read on the Pi (`~/hs-bench/config/initial_api_token`), entered browser-only, **accepted**. Every subsequent surface rendered authenticated with the `● Live` indicator and a `Disconnect` control. L3 held throughout.

**Glance 1 — G2, the availability tile: PASS.** ⏺ verbatim from Overview → Devices tile:

```
Available            6 of 6
Offline              none
Not determined yet   none
Stale readings       none
Counts reflect each device's last report — not a live connection test.
Open a device to see when it was last heard from.
```

All four honest rows present; "Available" wording (never "Online"); the disclosure line verbatim. The strongest possible G2 evidence.

**Glance 2 — evidence-with-age: ⏺ FINDING F3** (detail in §3). Verbatim from the drawers (`01KY12MQW954E4XYNKH0Y5H8VX` and `01KXW0157SP56CCSGJCNDCSQNG`; operator confirmed all six identical):

```
✓ Available
Available — last heard from —.
Battery Pct      —          (contact device: Battery Pct / Open / Last changed)
Humidity Pct     —          (climate device: Humidity Pct / Battery Pct / Temperature C / Last changed)
Last changed     —
Last reported    9:52 AM
```

The evidence line renders but the age is an em-dash; every attribute value blank; `Last reported 9:52 AM` populates on every device. Per-type spec templates resolve correctly — it is the values that are empty.

**Glance 3 — the five modes from the FIELD: ⏺ FINDING F4** (detail in §3). Run detail `/#/explain/run/01KXVWR03HW5MQ6WSW9XRTAWTX` renders the shell — "Why this happened", "← All runs", "Updated just now" — then **one empty card: no trigger, no steps, no action verdict pills, no "Recorded outcome" disclosure.** Operator's report, verbatim: *"every single run I clicked on (dozens, of all kinds of ages) had the same blank result."* The runs list bottoms out at "8 days ago"; every row labeled "An earlier automation" (italic), every list-level outcome `✓ Completed`. **The five modes could not be assessed on any historical run — not "rendered wrong": rendered nothing.**

### Block 5 — close

```
[PASS] boot-health — 6/6 positive · 0 forbidden
  [--] bundle: /home/homesynapse/hs-bench/bundles/boot-health-20260727T051201Z
```
```
git rev-parse --short HEAD    ->  c09c61c
git rev-parse --short HEAD~1  ->  2040a66
```
```
42770 /usr/lib/jvm/java-21-amazon-corretto/bin/java -classpath ...(installDist lib, incl. dashboard-0.1.0-SNAPSHOT.jar)... com.homesynapse.app.Main
```

---

## 3. Findings & anomalies (⏺-recorded, NOT debugged — scope law held)

### The four browser findings — and the pattern they form

**F1 — Activity surface 404s.** `/#/events` renders an honest red error card: **`Endpoint GET /api/v1/events not found`** + a Try-again button. The SPA calls an endpoint the deployed backend does not serve. Hypothesis for adjudication: a frontend/read-API contract seam — the page consumes `/api/v1/events` per the contract (or its mocks) while the backend never mounted it, or mounts it elsewhere. Note the error posture here is exemplary: honest, named, retryable.

**F2 — why-not diagnosis hangs on "Loading…".** `/#/explain/why-not/01KYGXTTAESH0QWPEV2FR01HPT` (bench-hero) sat on a spinner, "Updated 49 sec ago", no error state ever. Candidate mechanisms: its backing endpoint also missing/failing with no fetch error handler, or the diagnosis call genuinely hangs. Adjacent observation: the explain page shows bench-hero as `On · No runs yet` while Recent runs shows runs 7 hr ago — consistent if those runs belong to earlier automation identities, but worth the same look.

**F3 — drawer evidence empty (glance 2).** The evidence-with-age line renders as `Available — last heard from —.` (age missing); all attribute values `—`; `Last reported 9:52 AM` populates. Per-type templates resolve (contact vs climate rows correct). Tension across surfaces: the table's READING column says `Current` and the tile says `6 of 6 Available` while the drawer shows no values and no age — summary and detail are not drawing from the same populated fields. The unqualified `9:52 AM` (captured ~00:40 local) is itself ambiguous — real morning-ago report vs formatting/source-field issue.

**F4 — run causal chain renders nothing (glance 3).** Shell renders, content card empty, universally — dozens of runs, all ages. The five-modes render (the explainability hero) is unverifiable from the field until this surface produces content.

**THE PATTERN (one cluster, not four unrelated bugs — hypothesis for the hub):** every **list/summary** surface populates correctly (Overview tile + banner, Devices table, runs list, Automations, Health), while every **detail** surface fails (run chain empty, why-not hanging, drawer values blank, Activity 404). This points at a family of detail-level read endpoints absent from the deployed backend or returning empty payloads that the SPA renders as blanks. Cross-cutting UI note: error postures are inconsistent — honest error card (Activity) vs eternal spinner (why-not) vs silent empty card (run detail).

### Benign anomalies / notes

- **The envelope surprised on the fast side:** first npm-bearing build 49 s against a lawful 5–20 min; `npm ci` pulled 330 packages in 9 s. Second builds will be cache-warm besides.
- `1 high severity vulnerability` reported by npm audit during `npmInstall`; npm 10.9.8→12.0.1 upgrade notice. Recorded; no action taken (anti-action law).
- Every historical run row renders as italic *"An earlier automation"* — identities of superseded automation definitions don't resolve to names. Likely the deliberate fallback; hub to confirm by design.
- Health surface (corpus bonus): `Live — up to date and processing events in real time` · `Behind by: nothing — fully caught up` · `Projection version 5` · `Activity position 42470` · Reliability `All clear — no events stuck`.
- Devices table ULIDs match the boot-health `/api/v1/entities` assert list exactly (all six).
- Boot-health's `scenario` stimulus restarts the app; each invocation produced a fresh pid/log (expected instrument behavior, noted so pid/log lines across blocks read consistently).
- Ambient apt state on the Pi: "105 packages can be upgraded", armhf/Corretto skip-notice. Untouched.

---

## 4. Final state

**HEAD SHA on the Pi:** `c09c61c` (core: DASH-SERVE), directly atop `2040a66` (rev-parse-proven) · **app RUNNING:** pid `42770`, `com.homesynapse.app.Main` from `app/homesynapse-app/build/install/` · **active log:** `/home/homesynapse/hs-bench/bench-2026-07-27-011149.log` · **fleet:** 6/6, position 25065, ch20/0x774c, three `[PASS]` floors on the night (before / after-deploy / close) · **new standing state:** Node `v22.23.1` + npm `10.9.8` installed system-wide (one-time, deliberate; future builds reuse it) · nothing else non-standard; no config, constants, or cabling touched; write surface remains DORMANT.

---

**Route-back: this document intakes as the next v39 hub beat.** The three glance ⏺s are recorded above — **G2 CLOSES.** Findings F1–F4 (and the list-vs-detail pattern) are the intake for the hub's next research/design/coding deliberation; per the standing protocol this return reports and does not plan.

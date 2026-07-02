<!--
file: context/audits/2026-07-02_frontend-dev-lane_FE-1-live-integration_return.md
purpose: Lane return — FE-1 live integration (dashboard vs a locally-running Core, M7.5a/b endpoints) + the measured AMD-97/E5 rendering-semantics fold. The write-isolated frontend lane's ONE return file to the v13 hub.
audience: the Core/PM hub (adjudicates the two cross-lane contract drifts below); Nick (commit + gate + token hygiene).
state-type: lane return (audit)
status: RETURNED 2026-07-02. Lane baseline at start: core 52824e9 · docs 1509b34 · hivemind 07f3065 (beats 44/45 past the brief's cea7ae1 — skill-currency only, verified) · bench 5ceff3b. Preflight: STALE (Check 2/4 — the C8 additive `name` unfolded in the mirror; folded this session per the STALE protocol), 0 CONFLICTED at start; TWO live contract drifts found DURING the smoke (§3 — the checklist's purpose).
write-isolation: honored — writes under web-ui/dashboard/** + this file only. No spine edits, no workflow edits, no commits (Nick commits host-side on the hub's word).
-->

# FE-1 Live-Integration Return — the dashboard met the real backend

**Bottom line.** The FE-1 flip happened: the dashboard ran against a LIVE local Core (fresh DB, AB-1 bearer auth) with `VITE_USE_MOCKS=false`. **The moat's read path works live** — auth end-to-end, the hero/list endpoints (runs, automations, entities) returned contract-enveloped 200s and rendered honest empty states. The smoke did exactly what T1.3 built it to do: it surfaced **two live contract drifts on the periphery** (the two `/internal/*` reads and the problem-`type` form — §3), both **Core-vs-freeze divergences, not UI defects**, both left unpatched client-side per the freeze discipline and routed here for adjudication. The measured AMD-97/E5 confirmation-rendering semantics are folded and test-locked (§4). `npm run verify` green (§5).

---

## 1. What ran (the live setup)

Core `52824e9` booted host-side via `./gradlew :app:homesynapse-app:run` (fresh DB after `scripts/clean.sh`; migrations 1–5 applied; projection LIVE at position 0; `automations=0`; token freshly minted). Dev server: `VITE_USE_MOCKS=false VITE_VALIDATE=true npm run dev`, with the NEW dev-server proxy (`/api` + `/internal` → `VITE_CORE_ORIGIN`, default `http://127.0.0.1:7070`) added this session — required because Core sets no CORS headers (correctly, per loopback design) and the dev origin is 5173. Nick drove Firefox; evidence = his screenshots + Core's request-level debug log.

## 2. FE1_GO_LIVE checklist outcomes (Part B, item by item)

1. **Core up on loopback — PASS.** `HTTP surface exposed on 127.0.0.1:7070 behind bearer-token auth (AB-1)`; fresh pairing token minted (old token invalidated by the clean — see item 5).
2. **Point the UI at real — PASS.** One switch (`VITE_USE_MOCKS=false`); dev path needed the proxy (new, recorded in MODULE_CONTEXT). Served-build path not exercised this session (dist not rebuilt with today's changes).
3. **Authenticate — PASS.** Gate rendered; NEW token in; every subsequent request carries `Authorization: Bearer …` (verified in Core's log). Bare-origin pre-auth check: clean RFC 9457 401 `authentication-required` + `WWW-Authenticate: Bearer` + correlation id (Nick's screenshot).
4. **Smoke the reads:**
   - **A1 `/api/v1/entities` — PASS** (200, enveloped, "0 of 0" honest empty). A2/A3 **NOT EXERCISABLE** (no entities exist on an empty DB) — pending first paired device (FE-7 territory).
   - **A4 `/internal/projection` — FAIL (DRIFT-1a, §3).** Bare body, no `{data,meta}`, divergent fields.
   - **A5 `/internal/dlq` — FAIL (DRIFT-1b, §3).** Same class (source-confirmed).
   - **B3 `/api/v1/runs` — PASS** (200, enveloped via `PagedResponse`, "No automation runs yet" honest empty). `/automations` — **PASS** (200, empty list rendered). `/runs/{id}/causal-chain` + `/automations/{id}/non-firing` — **NOT EXERCISABLE on an empty DB** (no runs exist to explain); shape-conformance for these is held by the scenario engine + `contract.test.ts`; live exercise lands with the first real automation run (FE-7).
   - **B1/B2 (`/events`, `/health`) — as expected:** `/events` 404s live (M7.5c); the view degraded without breaking the app, BUT rendered the generic error rather than the new honest "not served yet" state — **because of DRIFT-2** (the `not-found` detection keys on the frozen slug; live `type` is a URI). `/health` untested directly (HealthView correctly composes A4+A5 — both hit DRIFT-1).
5. **Cross-cutting paths:** wrong/expired token → the fresh-DB boot invalidated the earlier token, giving a natural 403-material test (not explicitly exercised — Nick went straight in with the new token; the 403 unit/mock path remains covered by `?mock=forbidden`). Boot-replay state not observable (empty DB replays in ms). Poll-on-viewPosition — **DEGRADED by DRIFT-1a**: the poll loop reads A4 every 1.5s, each read fails the envelope check, phase = error → the persistent "Reconnecting" chip and no cursor-driven refetches (views loaded once and correctly, then never refreshed). This is honest behavior against a drifted endpoint — the client did not guess.
6. **Dev-runtime validation (`VITE_VALIDATE=true`) — ACTIVE.** A4/A5 failed at the envelope check (before the per-endpoint validator); the conforming endpoints validated clean — **zero `[contract-drift]` lines on the hero four.**
7. **Real-data surprises — the two drifts in §3. Nothing structural in the UI.** No client fix was needed for any conforming endpoint — the T1.2 thesis ("live integration meets no shape it hasn't faced") held for everything the scenario engine models.
8. **Large sets — N/A** on an empty DB (cursor-follow + virtualization stay backlogged, per the brief).

**Verdict:** the FE-1 mechanic (flip + smoke in one sitting) is proven; the checklist closes PASS-with-two-findings. The findings are Core-side/freeze-side and adjudicate at the hub — the UI needs zero structural change once the drift ruling lands (see §3 "smallest fold").

## 3. Cross-lane contract events (evidence attached — adjudication requested)

**DRIFT-1: the two `/internal/*` A-class reads are UN-ENVELOPED and shape-divergent from the freeze record.**
- **Live evidence:** Core log, `GET /internal/projection` → 200 `application/json`, body (61 B): `{"mode":"LIVE","viewPosition":0,"entityCount":0,"ready":true}` — no `{data,meta}` envelope, no ETag header.
- **Source evidence (core 52824e9):** `ProjectionStatusEndpoint.java` *documents* exactly that bare shape (`mode`, `viewPosition`, `entityCount`, `ready`); frozen A4 pins `{data:{mode, viewPosition, lagEvents, projectionVersion}, meta}`. `DlqStatusEndpoint.java` documents a bare `{"subscribers":[{subscriberId, mode, …}]}` — frozen A5 pins `{data:{depth, parkedSubscribers[]}, meta}`. The hero/list endpoints use `PagedResponse(data, pagination, meta)` and conform (verified live).
- **Impact:** the §0 "every read carries `meta.viewPosition`" anchor breaks on A4 — which is **the poll cursor**, so live change-detection is dead until resolved (the UI stays functional-but-static + shows the calm reconnecting state).
- **Options for the hub (public-API shape = Nick's call):** (a) Core envelopes the internal reads + returns the frozen A4/A5 fields — restores §0 uniformity, smallest UI delta (zero); (b) amend the freeze to the live shapes — the client then folds new A4/A5 types + the poll reads the new field names. The lane recommends (a): §0's "every read response carries meta" is the polling model's foundation, and the freeze record already claims these shapes were source-verified.

**DRIFT-2: problem `type` is a URI, not the frozen slug.**
- **Live evidence:** Nick's 401 screenshot — `type: "https://homesynapse.local/problems/authentication-required"`. **Source:** `ProblemType.java:160` `TYPE_URI_PREFIX = "https://homesynapse.local/problems/"` (documented, deliberate).
- **Impact:** status-keyed detections (401/403) worked; **slug-keyed detections silently miss**: `isReplaying` (`state-store-replaying`) — a real boot-replay 503 would render as a generic error instead of the calm catching-up state — and the new EventsView `not-found` honest state (observed live: generic error instead). Latent, not fatal, but it degrades two designed honest states.
- **Options:** (a) Core emits bare slugs per the freeze; (b) amend the freeze to URI types (RFC 9457-preferred) — the client then folds slug-or-URI-suffix matching (a three-line, contract-faithful change once ratified). The lane has **no preference**; it needs one ruling, after which the fold is trivial. **Until ruled, the client stays byte-faithful to the frozen slugs — nothing was patched to match the drifted server.**

**Recorded (not new):** the entity display-name candidate is now the ratified additive C8 — the mirror folded `name?` (types + validators + `displayName()` preference) this session; live Core omits it (expected — fills with config/M9). No further evidence possible on an empty DB.

## 4. The E5/AMD-97 fold (the measured confirmation semantics, shipped)

- **UI semantics (format.ts + CausalChain.tsx):** the UI runs **no confirmation timeout** — the backend owns the per-capability window (Doc 08 §3.6 / bench corpus; pointer-not-copy, no numbers in copy — test-enforced). Reason-aware honest-outcome rendering; class-keyed calm hints: DISPATCHED color-class → "Color changes confirm slowly on some bulbs…"; UNCONFIRMED effect/identify-class → "acknowledged but never reported back". UNCONFIRMED help copy neutralized (the reason carries specifics).
- **Scenario:** `e5-confirmation` ("Confirmation, measured") — four one-click runs: **run_e5_ct** flips Sent→Confirmed **live at the measured ~8.4 s** post-activation (getter-based; the poll renders the transition); **run_e5_idempotent** (confirmed-from-cache, no-change⇒no-report); **run_e5_effect** (immediate honest UNCONFIRMED — AMD-97-INV-01); **run_e5_superseded** (older expectation expires honestly; the newer confirms; no stranded chip).
- **Locks:** `e5-semantics.test.ts` (8 tests, incl. fake-timer window checks and a no-digits-in-copy invariant) + the scenario is auto-validated against every frozen shape by the existing `contract.test.ts` loop.

## 5. Gate + also-shipped

- **`npm run verify` GREEN** (clean `npm ci` copy): tokens ✓ lint ✓ typecheck ✓ **45/45 tests** ✓ build ✓ bundle **56.9/100 KB** ✓ contract-check 11 endpoints ✓. The pushed `frontend.yml` run rides **Nick's host-side commit** (the gate of record; path-filter will trigger).
- Also shipped: dev proxy (above); `VITE_VALIDATE` dev-runtime validation hook in `client.ts` (log-and-continue `[contract-drift]`); strict `Accept: application/json, application/problem+json` (visible in Core's live log); C8 `name` fold; EventsView honest M7.5c state (pending DRIFT-2 to actually render live); AuthGate password-manager ignore attributes (**live finding:** Bitwarden offered to fill the token gate — `data-bwignore`/`data-1p-ignore`/`data-lpignore` added); MODULE_CONTEXT currency beat.
- **Env note for the hub:** the VM-mount truncated-tail lag ran far beyond the documented minutes-scale this session (>30 min; edited files; a NEW file synced fine) — worked around by rebuilding the gate copy from in-context state; host tree proven by Vite compiling it. Worth a line in the env-model when convenient.
- **Dev-only observation (record, no action):** behind the dev proxy, a dead Core renders as a generic 500 error rather than the calm OfflineState (Vite turns ECONNREFUSED into HTTP 500; a served build takes the true network-failure → offline path). Not a product defect.

## 6. First-contact UX notes (Nick, unprompted)

"Relatively smooth… felt quite similar to using Home Assistant (and looked very similar) right out of the box." Two reads for the brand thread: onboarding friction is low (good), but the surface does not yet *read differentiated* at first contact — the hero must be more immediately present than an HA-familiar shell (feeds the T2 hero-polish work, not this WU).

## 7. Backlog deltas + next WU

- **Unchanged/backlogged per the brief:** mobile-first hero, PWA, list virtualization + cursor-follow (T2.3), ETag cache cap, migrating format.ts enum copy behind `t()`.
- **New, blocked-on-hub:** fold the DRIFT-1/DRIFT-2 ruling (either zero UI delta or a small ratified fold); then re-run the 10-minute smoke — the poll cursor and the two honest states light up.
- **Next recommended WU:** **FE-1b — drift-ruling fold + full smoke re-run** (hours, not days, once the hub rules), then **FE-7** (real-device CONFIRMED/UNCONFIRMED on the bench silicon — the e5-confirmation scenario is its rehearsal).

**Nick's post-session steps:** delete the pairing-token artifact (`app/homesynapse-app/.homesynapse/config/initial_api_token`) per Core's own log instruction; commit the lane's `web-ui/dashboard/**` + this file on the hub's word (host-side `npm run verify` rides the commit; messages with `!`/inner quotes go via `git commit -F` per the env-model).

---

## 8. Addendum (2026-07-02, same session) — the lane's answers to the hub's decision pass

**DP-A (M9 split ratify-all) — no objection; sequencing is right from this seat.** The lane holds no vote on M9's internal structure; the consumer-facing seams check out: (1) **M9.4 (confirmation + hero E2E) is FE-7's counterpart** — the `e5-confirmation` scenario + `e5-semantics.test.ts` are its UI-side acceptance rehearsal, already shipped; (2) **M9.3 is where the C8 entity `name` naturally fills** — the mirror + `displayName()` preference folded this session, so names light up with zero UI delta; please keep the name fill in M9.3's acceptance (see DP-B note below for why it just became load-bearing); (3) DP-C/D/E are UI-invisible; DP-F (fresh network, re-pair) is UI-transparent — the dashboard persists nothing keyed on entity/network identity (localStorage holds only the theme; the token is in-memory).

**DP-B (deterministic IntegrationId) — defer on the ruling, one display consequence to record.** Identity durability is Core's call; restart-stable beats boot-random from any consumer's seat (an orphaning id would also churn every UI entity list on reboot). The lane's flag: **hash-derived identifiers are display-hostile.** `labelFor()`'s humanized fallback is readable for slug-ish ids and gibberish for SHA-256-ish ones — so wherever derived ids leak into read surfaces (entity ids at adoption; the B2 health `integrations[].id` when M7.5c fills it), **the C8 `name` fill / a human-legible id-or-name becomes load-bearing, not cosmetic.** Decide-the-shape-now applies to B2's `id` semantics when M7.5c lands.

**DRIFT-1 ruling (conform Core, micro-WU first) — concur; zero UI delta; acceptance offered.** This is the return's own recommendation. UI-side acceptance for the micro-WU: (a) A4/A5 wrapped in `{data, meta}` with the frozen fields; keeping live extras (`entityCount`, `ready`) as **additive** fields inside `data` is fine per freeze §D and loses no ops signal; (b) on the re-run: the Reconnecting chip clears, the poll cursor advances, Health renders both cards, `VITE_VALIDATE` console clean on A4/A5. Ten-minute smoke, no client change.

**DRIFT-2 audit (freeze mis-transcribed; code + Locked Doc 09 §3.8 agree on URI types) — accepted; fold sized and ready.** The client stayed on the freeze per lane discipline; with the amendment ratified to the URI form the fold is one sitting, **independent of the Core micro-WU**: `ApiProblem` gains a derived `slug` (strip the documented `https://homesynapse.local/problems/` prefix; tolerate bare slugs for client-minted problems like `network-unreachable`); the three slug-keyed detections + the EventsView not-found check key on `slug`; **the mock moves to emit URI-form types so mock === wire exactly**; `contract.test.ts` pins the URI form (~30–40 lines incl. tests). Request: the amendment text should pin the prefix with a pointer to Doc 09 §3.8 / `ProblemType.java` so the client mirrors a ratified constant rather than a transcription. Governance echo: this one was invisible to the lane's preflight by construction — Check 8 round-trips to the *freeze* as the authoritative source, and the freeze itself was the error; an amendment line "re-verified against Doc 09 §3.8 + source" closes that loop.

**Net effect on the next WU:** FE-1b = (1) DRIFT-2 fold (can start the moment the amendment text exists), (2) verify the DRIFT-1 micro-WU on the re-run smoke, (3) both honest states (catching-up, events-not-served-yet) demonstrably live. Then FE-7 rides M9.4.

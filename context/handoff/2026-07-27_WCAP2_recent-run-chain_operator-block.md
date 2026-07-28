<!--
file: context/handoff/2026-07-27_WCAP2_recent-run-chain_operator-block.md
purpose: WCAP-2 — three token-safe captures (~5 min) that decide WU-CHAIN-HYDRATE's shape. WCAP-1 proved an 8-day-old run's chain is server-empty; the Jul-25 Rosonway field evidence proved FRESH runs hydrated on `355a711`; the read path (`buildActions`) is diff-proven byte-stable across the window. The one unmeasured hop: does a RECENT run's chain hydrate server-side on the deployed `c09c61c`? The answer routes the WU (see the interpretation table). L1: do not author on an unmeasured hop.
audience: Nick (operator). Anytime; read-only. Routes back to the hub. RETURN FILES TO `context/audits/` (returns live in audits/ — the standing filing rule).
laws: L3 — $TOK never prints; every paste token-free. Anti-actions — read-only curls; nothing restarted or written.
status: READY — authored 2026-07-27 (v39 hub, beat 7).
-->

# WCAP-2 — does a RECENT run's chain hydrate? (3 captures, ~5 min)

**Setup (token never prints):**

```
TOK=$(cat ~/hs-bench/config/initial_api_token)
pgrep -f com.homesynapse.app.Main
```

**Capture A — a deploy-evening-era bench-hero run (22:03Z Jul-26; from WCAP-1's list):**

```
curl -sS -o /tmp/wcap2a.json -w 'HTTP %{http_code}\n' -H "Authorization: Bearer $TOK" "http://127.0.0.1:7070/api/v1/runs/01KYG7932ACKW3E2EZ2AXY8DBQ/causal-chain"
head -c 3000 /tmp/wcap2a.json; echo; wc -c /tmp/wcap2a.json
```

**Capture B — a different-automation recent run (19:08Z Jul-26):**

```
curl -sS -o /tmp/wcap2b.json -w 'HTTP %{http_code}\n' -H "Authorization: Bearer $TOK" "http://127.0.0.1:7070/api/v1/runs/01KYFX8BQN8D2J481639GV8GHA/causal-chain"
head -c 3000 /tmp/wcap2b.json; echo; wc -c /tmp/wcap2b.json
```

**Capture C — the freshest possible run: re-list, take the TOP runId, fetch its chain:**

```
curl -sS -H "Authorization: Bearer $TOK" "http://127.0.0.1:7070/api/v1/runs" | head -c 400; echo
```

(Read the FIRST `runId` from that output, then — replacing RUNID with it:)

```
curl -sS -o /tmp/wcap2c.json -w 'HTTP %{http_code}\n' -H "Authorization: Bearer $TOK" "http://127.0.0.1:7070/api/v1/runs/RUNID/causal-chain"
head -c 3000 /tmp/wcap2c.json; echo; wc -c /tmp/wcap2c.json
```

**⏺ RECORD all three paste sets verbatim.** The tell in each: does `"actions":[…]` carry entries, and what does `wc -c` read (a populated chain runs well past 507 bytes)?

## Interpretation table (the hub adjudicates on the pastes; recorded here so the evidence reads itself)

- **Recent chains POPULATED** → the server hydrates current-era runs; the old-run emptiness is a history-era artifact (its action events may simply not exist under that correlation in the log) → CHAIN-HYDRATE **re-scopes**: (i) a bounded core look at WHY that era's events miss the join (correlation stamping history), (ii) the FE gains the honest "no detail recorded for this run" state (FE-LIVE-V112), (iii) the browser's recent-run blanks re-test against the SPA (client-side validation becomes the suspect for THOSE — one dev-tools glance).
- **Recent chains EMPTY** → the server-side hydration failure is universal and current → CHAIN-HYDRATE proceeds as a core P1 exactly as minted (the executor-stamping ↔ correlation-read seam, with the history-seeded red-first fixture).
- **Mixed (A/B differ from C)** → the boundary is the tell — ⏺ everything; the hub adjudicates.

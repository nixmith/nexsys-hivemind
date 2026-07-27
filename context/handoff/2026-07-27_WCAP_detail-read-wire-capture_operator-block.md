<!--
file: context/handoff/2026-07-27_WCAP_detail-read-wire-capture_operator-block.md
purpose: WCAP — a ~10-minute wire-capture block on the Pi. Captures the RAW payloads behind the redux findings F2/F3/F4 (why-not hang · drawer values empty · causal chain renders nothing) so the hub adjudicates SERVER-EMPTY vs CLIENT-RENDER-EMPTY on measurement, never theory (the instrument-first law). F1 needs no capture — adjudicated at source (M7.5c-b, deliberately unscheduled, graceful degrade by design).
audience: Nick (operator). Anytime; the app just needs to be running (pid glance first). Routes back to the hub.
laws: L3 — the token rides a shell variable, never printed; every paste below is token-free by construction. Anti-actions — read-only curls; no config/constants/repo writes; nothing restarted.
status: READY — authored 2026-07-27 (v39 hub, beat 5).
-->

# WCAP — the detail-read wire capture (5 captures, ~10 min, on the Pi)

**Why:** the redux proved every LIST surface populates while every DETAIL surface is empty/hanging (return §3). The bench's own instruments read causal chains successfully, so the wire is not simply dead — WCAP captures exactly what the server returns for the SAME resources the browser showed blank, splitting the cluster into server-side vs client-side in one paste set.

**Setup (one paste; the token never prints):**

```
TOK=$(cat ~/hs-bench/config/initial_api_token)
echo "token loaded: $(wc -c < ~/hs-bench/config/initial_api_token) bytes"
```

**Expect:** a byte count (~40s–60s). ⏺ nothing yet.

**Capture 1 — the runs list (the surface that WORKS; the baseline shape):**

```
curl -sS -o /tmp/wcap1.json -w 'HTTP %{http_code}\n' -H "Authorization: Bearer $TOK" "http://127.0.0.1:7070/api/v1/runs"
head -c 1500 /tmp/wcap1.json; echo
```

**Capture 2 — the causal chain for the EXACT run the browser rendered empty (F4):**

```
curl -sS -o /tmp/wcap2.json -w 'HTTP %{http_code}\n' -H "Authorization: Bearer $TOK" "http://127.0.0.1:7070/api/v1/runs/01KXVWR03HW5MQ6WSW9XRTAWTX/causal-chain"
head -c 3000 /tmp/wcap2.json; echo
wc -c /tmp/wcap2.json
```

**Capture 3 — the automations list (context for F2's identity question):**

```
curl -sS -o /tmp/wcap3.json -w 'HTTP %{http_code}\n' -H "Authorization: Bearer $TOK" "http://127.0.0.1:7070/api/v1/automations"
head -c 1200 /tmp/wcap3.json; echo
```

**Capture 4 — the why-not that hung in the browser (F2; the EXACT id from the URL):**

```
curl -sS -m 20 -o /tmp/wcap4.json -w 'HTTP %{http_code} (%{time_total}s)\n' -H "Authorization: Bearer $TOK" "http://127.0.0.1:7070/api/v1/automations/01KYGXTTAESH0QWPEV2FR01HPT/non-firing"
head -c 2000 /tmp/wcap4.json; echo
```

(The `-m 20` cap means "HTTP 000 after ~20 s" is itself the finding — a genuinely hanging endpoint. ⏺ whatever prints.)

**Capture 5 — the 04P's detailed state (F3; the drawer that showed all em-dashes):**

```
curl -sS -o /tmp/wcap5.json -w 'HTTP %{http_code}\n' -H "Authorization: Bearer $TOK" "http://127.0.0.1:7070/api/v1/entities/01KY12MQW954E4XYNKH0Y5H8VX/state"
head -c 2000 /tmp/wcap5.json; echo
```

**⏺ RECORD: all five paste sets VERBATIM (HTTP code + payload head + wcap2's byte count).** No token appears in any of them. Route the pastes back to the hub conversation — they intake as the adjudication evidence; the fix WU routes core-side or FE-side on what they show.

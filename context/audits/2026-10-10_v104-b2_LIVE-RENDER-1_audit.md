<!--
file: context/audits/2026-10-10_v104-b2_LIVE-RENDER-1_audit.md
purpose: LIVE-RENDER-1 — the recovery card on the real wire (read-only): the dashboard at core `409547c` on Nick's desk (mocks OFF, live shape-validation ON) reading the Pi (hs-dev-1, `37f05a9`) through an ssh tunnel; the hub read the page, its console and its network in the built-in browser pane. P-v103-3 adjudicated.
audience: the v104 hub · the v105 boot · Nick
state-type: audit (short)
status: FILED v104 beat 2 (Sat 2026-10-10 14:18 CT (instrument 2026-10-10T19:18:11Z)).
-->
# LIVE-RENDER-1 — P-v103-3 HOLDS on the real wire

**Setup (Nick's windows, 14:16 CT):** `head=409547c` · `npm ci` → `added 330 packages` (nine `EBADENGINE` warnings: the eslint 10 packages want Node `^22.13.0`, the desk runs `v22.6.0`; warnings only) · `tunnel: 200` · the token to the clipboard, never printed · Vite 6.4.3 `Local: http://localhost:5173/dashboard/`. The token was pasted into the pane by Nick (14:17 CT); the hub never handled it.

**The read (the pane, tab `seed`, `http://localhost:5173/dashboard/#/devices`, ≈ 14:17 CT):**
| P-v103-3 clause | verdict | what the page printed |
|---|---|---|
| the Hue reads "Not heard from since startup (not asked)" | **HOLDS** | `01KX1PA4HSJ581GASYB7DHE40F: Not heard from since startup (not asked).` · "Nothing from this device since startup. It has not been asked yet." · "Last report on record: 7:49 PM on Jul 18." |
| nine rows read "Reporting" | **HOLDS** | 9 of 10 rows "Reporting", with their ages: `…V2DWKE` (S31) 4 min · `…4PK2XA` (TR3) 4 min · `…8ZEX2G` (G4-1) just now · `…MSBJVS` (G4-2) just now · `…FT4HWQ` (the sensor) 2 min · `…477TV3` 8 min · `…DCSQNG` 59 s · `…H5Y8VX` 10 min · `…HTG87K` 9 hr (5:41 AM) |
| no shape errors | **HOLDS** | the console: `[vite] connecting...` · `[vite] connected.` and nothing else (validation ON); the network: every `GET /api/v1/entities?sort=ASC` → 200 OK |

**Observations (recorded, not judged):**
1. `…HTG87K` reads "Reporting" with "Last report 9 hr ago": the SPEC's S2 form for an AVAILABLE device whose reason is not `ping_success` (R1's label with the age visible; SPEC §3 R2's S1/S2 cells). Its class is not on the wire until AVAIL-API-1.
2. Every row's label is the entity ULID, with "Device <ULID>" beneath: no entity carries a `name` (the contract's optional key, omitted when unset). This is what a household would read today; the FE lane's naming row decides it.
3. The metering plugs read "Reporting" at 2:13–2:17 PM, consistent with D-v104-11 (the class answered at the resume).

**Not re-executed:** the dashboard's other routes; a screenshot of the glyphs and colours (the clauses are text); the token's validity beyond the 200s.

<!--
file: context/audits/2026-09-06_H8a_real-wire_operator-record.md
purpose: THE H8-a OPERATOR RECORD — every ⏺ of the Sun 2026-09-06 rig session on the held card (hs-fresh) running f25291b's CI-built artifact (= 093d5b4's Java): the four v1.1.3 keys on the real wire (K1–K4), the FAILCHAN §6-B/EXITCODE stop-proof (two readings), the v1.1.3 wire CAPTURE (FE-113b's fixture), the journald priority count (OR-JOURNALD-PRIO), the sys_* count (docket Row 16), the bench restore. Scaffolded by the v66 hub at Block 1; FILLED by the H8-a navigator as ⏺s land (append-only under the headings; the hub writes §10 at intake).
audience: the navigator (fills §0–§9) · the hub (audits two-layer; writes §10) · Nick (reads §0)
state-type: operator record (evidence; verbatim paste-backs with Z stamps)
status: SCAFFOLD — OPEN (the navigator sets CLOSED-PENDING-HUB-AUDIT or STOPPED-AT-<block> at close-out). Packet: context/instructions/2026-09-06_H8a_real-wire_v113-keys_and_failchan-proof_navigator-packet.md. Capture dir: context/audits/2026-09-06_H8a_v113-wire-capture/ (three JSON bodies, token-free).
-->

# H8-a — operator record (held card, Sun 2026-09-06)

## §0 VERDICT SURFACE (the navigator rewrites this at close-out — one screen)
**Artifact:** `f25291b` = `0.1.0+git20260906.114248.gf25291b` · sha256 `<from §1>` · install-smoke run `<URL>` (amd64 `<g|r>` · arm64 `<g|r>`) · CI main `093d5b4` `<g|r>`.
**Navigator dispatched `<Z>` · record closed `<Z>` · card `hs-fresh` @ `<IP>` · STOPs: `<count>`.**

### THE FOUR KEYS (K) — `<n>` of 4
| key | read | where | verdict | the assert line, quoted |
|---|---|---|---|---|
| K1 `deviceId` | `/api/v1/entities` rows | every row; ULID or null | `<✓/✗>` | |
| K2 `lastReported` | `/api/v1/entities` rows | every row; ISO-8601 Z or null | `<✓/✗>` | |
| K3 `components[].ref` | `/api/v1/automations` | every component; `{type:"entity", id}` or null | `<✓/✗>` | |
| K4 `triggerRef` | `/api/v1/automations/{id}/non-firing` | present; `{type:"entity", id}` or null | `<✓/✗>` | |
The literal `"type":"entity"` (lowercase) on every non-null ref: `<✓/✗>`. ISO-8601 on every non-null `lastReported`: `<✓/✗>`.

### THE STOP-PROOF (S) — FAILCHAN §6-B / EXITCODE
| reading | Result | ExecMainStatus | ActiveState | SubState | NRestarts | verdict |
|---|---|---|---|---|---|---|
| B3 (the proof) | | | | | | `<✓/✗>` |
| B6 (the halt) | | | | | | `<✓/✗>` |
R-4b §9 on `ef02d13` read `Result=exit-code · ActiveState=failed · ExecMainStatus=143` (before the fix). Today: `<the sentence>`.

### THE CAPTURE (C) — FE-113b's inputs
| file | bytes | sha256 | Bearer count |
|---|---|---|---|
| `entities.json` | | | 0 |
| `automations.json` | | | 0 |
| `nonfiring.json` | | | 0 |

### THE READS (J · R)
OR-JOURNALD-PRIO (B4): `<the uniq -c lines>` · app-WARN vs journald ≤4: `<pair>`. Row 16 (B5): `components=<n> refs_nonnull=<n> sys_refs=<n>`.

### PER-BLOCK
| block | verdict | note |
|---|---|---|
| §0 guard 1 | | |
| §1 fetch + hash | | STOP-GATE H8a-1 |
| B0 preflight | | STOP-GATE H8a-0 |
| B1 install + boot | | STOP-GATE H8a-2 |
| B2 the four keys | | STOP-GATE H8a-3 |
| B3 the stop-proof | | STOP-GATE H8a-4 |
| B4 journald priority | | |
| B5 sys_* count | | |
| B6 the restore | | STOP-GATE H8a-5 |
**⏺ census: `<count>` paste-backs banked. Deviations: `<count>` (§9). STOPs: `<count>`.**

### ASKS OF THE HUB
1. `<…>`

## §0-G Guard 1 — the artifact (⏺ `ARTIFACT:` line · `CI-main:` line)

## §1 Fetch + hash (⏺ the origin echo line · the unpack + hash output)

## B0 Preflight at the rig (⏺ the bench digest · the halt · the held card's boot glance; the pinned IP)

## B1 Install + boot (⏺ the copy + hash · the integrity gate · the install with three stamps · the boot tokens as counts)

## B2 The four keys (⏺ the three GETs · the asserts output whole · the capture on the desktop with hashes)

## B3 The stop-proof (⏺ the stop stamps · the grade + the journal tail · the start + the counts)

## B4 OR-JOURNALD-PRIO (⏺ the priority count)

## B5 Row 16 (⏺ the sys_* line)

## B6 The restore (⏺ the halt's grade · the bench floor)

## §9 Deviations ledger + THE FINDINGS CARD FOR THE HUB
- Deviations (tier · block · what · why · Z):
- THE FINDINGS CARD (≤1.5 KB, at close-out): what the wire showed that the desk did not predict · the stop-proof · the three things you would change in the packet:

## §10 Hub verdict surface (the hub writes this at intake)

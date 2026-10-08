<!--
file: context/instructions/2026-09-27_coder-lane_LOCK-1_integration-id_and_migration-bytes_pinned_coding-instruction.md
purpose: LOCK-1 (the hub-read §4's first row; `LOCK1: cut` adopted by silence, D-v84-4): two TESTS, no production change, that pin the two byte-level facts a future identifier sweep must never move — (1) the integration id the store carries for every adopted device is `IntegrationIds.deriveStable("zigbee")` = the literal `6V1CMGY2HKF4H1FGZ4H7F257FS` (the SHA-256 of `"homesynapse:integration:" + "zigbee"`, first 16 bytes `db0b290f0a33792217c3e489de229df9`, squeezed into the Ulid carrier — `IntegrationIds.java` :37–:58; the literal appears in the record's evidence reads of the Pi's rows on 08-02, 08-06 and 09-03); (2) the SHA-256 of each event-store migration V001–V005 (`MigrationRunner` halts every boot on checksum drift, :34–:40). A sweep that touches either turns CI red instead of orphaning every `Device.integrationId` row or stopping the core. No product or company name appears in these files, in any token, string or comment.
audience: the Coder lane (a FRESH host-side Claude Code session in homesynapse-core; the nexsys-coder skill; the SAME session then runs IR-61b) · the hub (the intake) · Nick (§14)
state-type: coding instruction (the Java slot; one session with IR-61b; one return per WU)
baseline: core `1f1d1e0` (IR-61; CI green; the counter 15/20) — re-verify at issue with `git --no-optional-locks log -1 --oneline`
status: EXECUTED — HIVE-CLEAN-4 (2026-10-07). Was: RETURNED — the lane ran Mon 2026-09-28 11:47 → 12:01Z; the return `context/audits/2026-09-28_LOCK-1_return.md` (4,990 B) intaken ACCEPT at v84 beat 5 (`context/audits/2026-09-28_v84-b5_LOCK-1_IR61b_intake_audit.md`); the core card handed (4 = 2 M + 2 A); CI on the landing sha pending — EXECUTED when green. Was: DISPATCH-READY — cut v84 beat 3 (Sun 2026-09-27 evening). Dispatches Monday after the rehearsal's paste (D-v84-12: LOCK-1 first, then IR-61b, one session). Returns to `context/audits/<CT-filing-date>_LOCK-1_return.md` (≤ 5,000 B — a ceiling; §0 first; the LAST LINE `RETURNED <path> <bytes>`). EXECUTED when CI is green on the landing sha.
-->

# LOCK-1 — the integration id and the migration bytes, pinned by two tests

## §0 The lane contract (read first; every line binds)
`date -u` FIRST; every stamp from it (CT = UTC−5). Re-verify the baseline `1f1d1e0`, porcelain 0. Read §2's set by the ranges given. Re-run every §6 command before the first write and paste each output into the return. Tests first — here the tests ARE the work: each is written to the pinned value the hub computed at `1f1d1e0` (§4), run green, and then shown RED ONCE by a deliberate, reverted perturbation (§7) so the return proves the pin bites. Write ONLY §3's rows. `./gradlew :integration:integration-runtime:test :core:persistence:test` green, then `./gradlew check` green (`-Werror` is on). Leave the tree at porcelain, uncommitted, unstaged; never `git add/commit/push`. No token, no secret, no product or company name in the return or the files. The return: §0 the card (DELIVERED/BLOCKED; the two test names; the pinned values as the tests hold them; the red texts from the perturbations; porcelain) · §1 what changed · §2 the tests · §3 deviations · §4 the survey as re-run · §5 findings for the register · §6 the coder-handoff entry text · §7 instrument limits. The last line of the FILE: `RETURNED nexsys-hivemind/context/audits/<date>_LOCK-1_return.md <bytes>`.

## §1 What this implements
Two pinning tests and their MODULE_CONTEXT rows. No main-source change. Nothing under `integration-zigbee`, nothing in `persistence` main, no migration byte touched.

## §2 Files to read before starting
`integration/integration-runtime/src/main/java/com/homesynapse/integration/runtime/IntegrationIds.java` whole (≈ 70 lines: `NAMESPACE` :37, `ULID_BYTES` :38, `deriveStable` :52–:58) · `platform/platform-api/src/main/java/com/homesynapse/platform/identity/Ulid.java` :25–:70 and :141 (`fromBytes`; the Crockford alphabet :44; `toString` :61) · `IntegrationId.java` :27, :67–:68 (`toString` = the Ulid's) · `core/persistence/src/main/java/com/homesynapse/persistence/MigrationRunner.java` :30–:45 and :480–:495 (the checksum contract; the classpath read of `db/migration/events`) · `.gitattributes` :9 (`* text=auto eol=lf` — the working tree's bytes are the blob's bytes) · the two modules' `module-info.java` and MODULE_CONTEXT.md by `grep -n 'IntegrationIds\|Migration'` · the existing test sets' style: `integration/integration-runtime/src/test/java/com/homesynapse/integration/runtime/CommandRoutingSubscriberTest.java` :80–:100, `core/persistence/src/test/java/com/homesynapse/persistence/MigrationRunnerTest.java` :1–:60.

## §3 Files to create or modify
| # | File | A/M | What |
|---|---|---|---|
| 1 | `integration/integration-runtime/src/test/java/com/homesynapse/integration/runtime/IntegrationIdsPinTest.java` | A | T1, T1b (§7) |
| 2 | `core/persistence/src/test/java/com/homesynapse/persistence/MigrationBytesPinTest.java` | A | T2 (§7) |
| 3 | `integration/integration-runtime/MODULE_CONTEXT.md` | M | one row: the pin test and what it guards |
| 4 | `core/persistence/MODULE_CONTEXT.md` | M | one row: the pin test and what it guards |

## §4 The pinned values (computed by the hub at `1f1d1e0`; the Coder re-computes each in §6 and pins what the instrument says — a mismatch is a STOP, not a correction)
- `IntegrationIds.deriveStable("zigbee").toString()` = **`6V1CMGY2HKF4H1FGZ4H7F257FS`**; the first 16 bytes of SHA-256(`"homesynapse:integration:zigbee"`) = **`db0b290f0a33792217c3e489de229df9`**.
- SHA-256 of the migration files' bytes (`core/persistence/src/main/resources/db/migration/events/`):
  `V001__initial_event_store_schema.sql` **`4fa9e1008d9e4c145461063d6474501c2d5ad45d7bcebe4c567154f0a54362a3`** · `V002__subscriber_dead_letter_queue.sql` **`7cd7d62261b1c2b18300531eaff14f2e09d1b8108ddc03a35f358885ca3b84dc`** · `V003__add_snapshots_and_drop_redundant_index.sql` **`3d9bf80d3700a0c8f2df6a2cb65633787e014b48aceae410d1c8c984c7e3b6cf`** · `V004__dlq_operational_indices.sql` **`5cf593d5d3f1956290af9fd1e2f22297cc29a047bb0d0b74605dbdf47b87c6b0`** · `V005__at_rest_payload_encryption_columns.sql` **`a11cec73095fe9e4fd95450e5498d58e5ad74784ddb6b9f2b6b0d4f41c607ea6`**.

## §5 Locked decisions and invariants that apply
Settled DP-6 (the deterministic integration identity; `IntegrationIds` javadoc :15–:30 — a boot-random id orphans every `Device.integrationId` row) · the migration checksum contract (`MigrationRunner` :34–:40: halt on drift) · the hash namespace and every migration byte are untouchable for any reason (the plan §7; the v81–v84 REFUSE lists) · `NO_DIRECT_TIME_ACCESS` (no clock in either test) · no name in any token (D-v81-3; THE PREMISE).

## §6 The survey (the Coder re-runs each before writing and pastes the output)
| Command (from the core root) | The hub's reading at `1f1d1e0` |
|---|---|
| `git --no-optional-locks log -1 --oneline` | `1f1d1e0 feat(state-store): IR-61 — …` |
| `grep -n 'NAMESPACE = \|ULID_BYTES = \|public static IntegrationId deriveStable' integration/integration-runtime/src/main/java/com/homesynapse/integration/runtime/IntegrationIds.java` | :37 `"homesynapse:integration:"` · :38 `16` · :52 |
| `printf 'homesynapse:integration:zigbee' \| sha256sum \| cut -c1-32` | `db0b290f0a33792217c3e489de229df9` |
| `for f in core/persistence/src/main/resources/db/migration/events/V00[1-5]__*.sql; do sha256sum "$f"; done` | the five digests of §4, in order |
| `for f in core/persistence/src/main/resources/db/migration/events/V00[1-5]__*.sql; do git show HEAD:"$f" \| sha256sum \| cut -c1-16; done` | the same first 16 hex of each (the tree = the blob; `.gitattributes` :9) |
| `ls core/persistence/src/main/resources/db/migration/events/` | exactly five files, V001–V005 |
| `git grep -n 'IntegrationIdsPinTest\|MigrationBytesPinTest' -- '*.java' '*.md'` | 0 — the names are free |
| `git grep -c '6V1CMGY2HKF4H1FGZ4H7F257FS' -- '*.java'` | 0 — the literal is pinned nowhere in the code today |

## §7 Test requirements
- **T1** `IntegrationIdsPinTest`: `IntegrationIds.deriveStable("zigbee").toString()` equals `"6V1CMGY2HKF4H1FGZ4H7F257FS"`; the assertion message names the consequence in one sentence (a changed derivation orphans every adopted device's `Device.integrationId` row on the next boot). **T1b**: the derivation's input — `MessageDigest SHA-256` of `"homesynapse:integration:" + "zigbee"`, first 16 bytes — equals `db0b290f0a33792217c3e489de229df9` as hex, so a NAMESPACE change and a squeeze change are told apart. Red-once: change `"zigbee"` to `"zigbee2"` in the test's input, run, paste the red text, revert.
- **T2** `MigrationBytesPinTest`: for each of V001–V005, read the resource from the classpath (`db/migration/events/<name>`, the path `MigrationRunner` reads), SHA-256 its bytes, assert the hex against §4's pinned value; the message names the consequence (`MigrationRunner` halts every boot on checksum drift — a changed byte is a stopped core, not a migration). The test also asserts the directory holds exactly the five names (a sixth migration is a new WU with its own pin row, not a silent addition). Red-once: flip one pinned hex digit in the test, run, paste the red text, revert.
- Both tests use no clock and no name. `./gradlew check` green.

## §8 MODULE_CONTEXT.md — rows only
One row per module under its tests section: the class, what it pins, and the sentence "change the pinned value only through a WU that names the migration or re-derivation it performs". LF endings.

## §9 What to watch out for
1. `.gitattributes` `* text=auto eol=lf` — the checkout's bytes are LF; do NOT normalize line endings in the test (a normalizing test would pass over a CRLF corruption the runner would halt on). If `sha256sum` on the file and on `git show HEAD:<file>` differ on your machine, STOP and report both — that is a finding, not something to code around.
2. The resource read must go through the classpath the runner uses (`ClassLoader.getResourceAsStream`), not a filesystem path — the jar is what boots.
3. `IntegrationIds` is public API of `integration-runtime`; the test lives in that module's own test set (same package), no module-info change.
4. `-Werror`: no unused imports; `assertThat(...).as(...)` for the messages, the AssertJ form the sibling tests use.
5. No product or company name, no `{{NAME}}` token, anywhere in the two files — "homesynapse" appears only inside the NAMESPACE string the code already carries.

## §10 Coder pushback welcome
If any §4 value disagrees with §6's instrument on your machine: STOP, paste both, do not pin either. If the persistence module's test set has no classpath fixture for the events migrations, name the existing test that does read them.

## §11 Out of scope
Any main-source change; `integration-zigbee`; the config migrations (`ConfigMigrator`); the test-only migration resources under `src/test/resources/db/migration/{bad,recovery,tampered,test}`; RENAME-CENSUS-1; HEADERS-1.

## §12 Success criterion (binary)
Two test classes green; each shown red once by its perturbation and reverted (the red text in the return); `./gradlew check` green; porcelain lists exactly §3's four rows; the return ≤ 5,000 B with `RETURNED …` as its last line.

## §13 Work unit completion (WUCP Phase 1)
The return after §0: §1 what changed · §2 the tests (the pinned values as the tests hold them; the two red texts) · §3 deviations · §4 the survey as re-run · §5 findings · §6 the coder-handoff entry text (LOCK-1 DELIVERED; then IR-61b in this same session) · §7 instrument limits. Then, in the SAME session, execute IR-61b's instruction (`context/instructions/2026-09-27_coder-lane_IR61b_staleness-config-keys_boot-ordering-gate_coding-instruction.md`) with LOCK-1's four rows left uncommitted in the tree.

## §14 The dispatch line (Nick pastes into a FRESH host-side Claude Code session in `~/Desktop/Code/ClaudeFolder/homesynapse-core`, on `main` at `1f1d1e0`, Monday after the rehearsal's packet is pasted into its own guide session)
```
Invoke the nexsys-coder skill. Two work units in series, one session, two returns, nothing committed. FIRST execute nexsys-hivemind/context/instructions/2026-09-27_coder-lane_LOCK-1_integration-id_and_migration-bytes_pinned_coding-instruction.md exactly: date -u first; re-verify the baseline (git --no-optional-locks log -1 --oneline = 1f1d1e0, porcelain 0); re-run every §6 command and paste the outputs; write §3's four rows and nothing else; each test green, then shown red once by §7's perturbation and reverted; ./gradlew check green; write the return to nexsys-hivemind/context/audits/<today's CT date>_LOCK-1_return.md (≤ 5,000 B, §0 first) whose LAST LINE is exactly: RETURNED <that path> <bytes>. THEN, with LOCK-1's rows left uncommitted in the tree, execute nexsys-hivemind/context/instructions/2026-09-27_coder-lane_IR61b_staleness-config-keys_boot-ordering-gate_coding-instruction.md exactly: re-run its §6 greps and paste the counts; write its §3's eight rows and nothing else; tests first (§7: red observed, then green; T3b's red-or-green stated); ./gradlew check green; leave the tree at porcelain, uncommitted, unstaged; write the return to nexsys-hivemind/context/audits/<today's CT date>_IR61b_return.md (≤ 10,000 B, §0 first; LOCK-1's rows listed apart in its porcelain) whose LAST LINE is exactly: RETURNED <that path> <bytes>; end your last message with both RETURNED lines, LOCK-1's first.
```

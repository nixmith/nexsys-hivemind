# LOCK-1 return — the integration id and the migration bytes, pinned

## §0 The card
**DELIVERED** — filed 2026-09-28 CT (`date -u` 2026-09-28T11:47:37Z). Baseline `1f1d1e0`, porcelain 0 at start. ZERO commits; nothing staged.
- Tests: `IntegrationIdsPinTest` (T1, T1b) · `MigrationBytesPinTest` (T2). No main-source change.
- Held: T1 `6V1CMGY2HKF4H1FGZ4H7F257FS`; T1b `db0b290f0a33792217c3e489de229df9` (the test's digest AND the id's `value().toBytes()`); T2 the five §4 digests verbatim + exactly those five names in the directory.
- Red once, reverted (each file's sha256 identical after restore):
  - `"zigbee"`→`"zigbee2"`: T1 `[a changed derivation orphans every adopted device's Device.integrationId row on the next boot] expected: "6V1CMGY2HKF4H1FGZ4H7F257FS" but was: "71BR62D666PCH8QWZF8V51D2PP"`; T1b 2 failures, each `expected: "db0b290f0a33792217c3e489de229df9" but was: "e15e0c2698c6b3228bf3ef46ca168ad6"`.
  - V001 pin `…62a3`→`…62a4`: `[V001__initial_event_store_schema.sql: MigrationRunner halts every boot on checksum drift -- a changed byte is a stopped core, not a migration] expected: "…62a4" but was: "4fa9e1008d9e4c145461063d6474501c2d5ad45d7bcebe4c567154f0a54362a3"`.
  - Supplementary: V005 dropped from the pins → `[a sixth migration is a new WU with its own pin row, not a silent addition (listed from jar:file:/…/persistence-0.1.0-SNAPSHOT.jar!/db/migration/events)]`.
- Gates: `:integration:integration-runtime:test --rerun :core:persistence:test --rerun` green (XML 7 files/40 tests · 56/418, 0 fail, stamped 12:00:47–:58Z) · `./gradlew check` BUILD SUCCESSFUL 12:01:10Z, `156 actionable tasks: 5 executed, 151 up-to-date`.
- Porcelain (2 M + 2 ??):
```
 M core/persistence/MODULE_CONTEXT.md
 M integration/integration-runtime/MODULE_CONTEXT.md
?? core/persistence/src/test/java/com/homesynapse/persistence/MigrationBytesPinTest.java
?? integration/integration-runtime/src/test/java/com/homesynapse/integration/runtime/IntegrationIdsPinTest.java
```

## §1 What changed
Two test classes; one row each (integration-runtime MODULE_CONTEXT :250, persistence's :579), both with "change the pinned value only through a WU that names the migration or re-derivation it performs". LF (0 CR).

## §2 The tests
T1/T1b as §7 (T1b soft, two readings); T2 soft per file, raw bytes via `MigrationRunner`'s class loader, no normalization; the listing from the same loader.

## §3 Deviations
- [INFO] T1b also reads the id's own 16 bytes: its literal alone cannot tell a NAMESPACE move (T1b red) from a squeeze/render move (T1 red only).
- [INFO] Persistence's test classpath carries the module JAR — the only URL for `db/migration/events` — not `build/resources/main`: first run red `expected: "file" but was: "jar"`, one diagnostic run; the listing reads the jar via a zip FileSystem (`file:` too). Both reads see what boots.
- [INFO] integration-runtime's MODULE_CONTEXT has no tests section; the row sits by its testing note.
- [INFO] The Spotless header and package line carry the names (HEADERS-1); no other beyond the NAMESPACE literal.
- [INFO] Cap arithmetic 3 + 4 × 1 KB = 7 KB > 5,000 B; compressed.

## §4 The survey as re-run (before the first write)
- log → `1f1d1e0 feat(state-store): IR-61 — …`
- grep → `37: … NAMESPACE = "homesynapse:integration:";` · `38: … ULID_BYTES = 16;` · `52: public static IntegrationId deriveStable(String integrationType) {`
- printf|sha256sum → `db0b290f0a33792217c3e489de229df9`
- sha256sum V001–V005 → the five §4 digests in order (python: exact match)
- `git show HEAD:` → `4fa9e1008d9e4c14` `7cd7d62261b1c2b1` `3d9bf80d3700a0c8` `5cf593d5d3f19562` `a11cec73095fe9e4`
- ls → exactly V001–V005 · the two names → 0 · the literal in `*.java` → 0
- python: Crockford(the 16 bytes) = T1's literal.

## §5 Findings for the register
- F1: persistence's `test` task runs on the module jar; resource reads there see the jar.
- F2: `MigrationRunner` hashes the UTF-8 round-trip (:478, :503), not raw bytes; byte-identical for these five (valid UTF-8, no BOM, 0 CR). Two malformed sequences would both become U+FFFD and match; the raw pin tells them apart.
- F3: persistence MODULE_CONTEXT stale: the layout tree (:287–:294) lists V001–V002; :303 the manifest as V001–V004 (V005 enrolled). Untouched (rows only).

## §6 The coder-handoff entry text
LOCK-1 DELIVERED 2026-09-28 CT — `IntegrationIdsPinTest` (T1/T1b) + `MigrationBytesPinTest` (T2) + two MODULE_CONTEXT rows, uncommitted on `1f1d1e0` (2 M + 2 ??); each red once, reverted byte-identical; module gate + `check` green in-lane; CI on the landing sha is the gate of record. NEXT: IR-61b, this session.

## §7 Instrument limits
Windows, Git Bash, JDK 21, `--offline`. Under `check` untouched modules' tests were UP-TO-DATE (inputs unchanged); the two touched ran fresh just before. The `file:` listing branch is unexercised.
RETURNED nexsys-hivemind/context/audits/2026-09-28_LOCK-1_return.md 4990

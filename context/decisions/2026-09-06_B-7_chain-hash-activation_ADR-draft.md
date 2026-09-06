<!--
file: context/decisions/2026-09-06_B-7_chain-hash-activation_ADR-draft.md
purpose: THE B-7 ADR — DECIDE, DON'T BUILD (Nick's word, 09-06; the program §1.7). Q1 of the BEYOND input ("is the log hash-chained today?") answered AT SOURCE at 093d5b4: the schema is CHAIN-READY, the chain is NOT COMPUTED. This draft is the hub's; the docs-repo copy (design/adr/) is Nick's docs commit at the next docs touch, after BLOCK 6.
audience: Nick (ratifies or edits) · the hub · the future activation WU's author · the strategy layer (the language law)
state-type: decision record (DRAFT — PROPOSED; Nick's word `B7: ratify | edit <row>` makes it ACCEPTED)
status: DRAFT v66 beat 6 (Sun 2026-09-06). Source facts verified: V001__initial_event_store_schema.sql:53 · SqliteEventStore.java:92/:147–:153/:492/:950–:955 · AMD-37 (docs). The v66 prompt's premise "reserve a nullable column now, re-hash nothing" was HALF wrong at source — nothing needs reserving; AMD-37 reserved it NOT NULL with the zero-vector genesis default on 2026-05-02.
-->

# ADR — Chain-hash activation: the schema is ready, the chain is not computed; decide the activation shape now, build it as one WU later

## Context (the facts at `093d5b4`)
1. **The column exists and is non-nullable:** `events.chain_hash BLOB(32) NOT NULL DEFAULT x'00…00'` (`core/persistence/src/main/resources/db/migration/events/V001__initial_event_store_schema.sql:53`; AMD-37 APPLIED 2026-05-02, "Chain Hash NOT NULL with Zero-Hash Default" — chosen precisely so activation needs **no migration and no backfill** on a multi-GB Pi log).
2. **Every row written today carries the 32-byte ZERO vector** (`SqliteEventStore.java:492` binds `ZERO_HASH`; the class javadoc `:92` and `:147–:153` say so; `:950–:955` name "chain_hash computation and mandatory startup verification" as the gate that keeps crypto-shred DISABLED).
3. **Therefore the north star's phrase "hash-chained" is not yet TRUE of the shipped log.** The honest sentence today: *"a chain-ready log"* — the language law (the deterministic floor is MISSING from the field, not SUPERIOR; a claim is worded only as far as it is proven).
4. **The hash chain's consumers are all future rows:** B-7 (the accountability record) needs the chain computed AND independently recomputable; B-3's proposal events and B-2's principals ride the same log; crypto-shred (Doc 15) waits on it by the store's own comment.

## Decision (proposed — five rows; each ratified or edited by name)
- **D1 — Reserve nothing further now.** The column, its width and its genesis default are already the design. No change to `events` before or at activation; the activation WU carries ONE additive migration of its own (D3's metadata row — the events DB has no metadata table today: V001–V005 define `events` · `subscriber_checkpoints` · `view_checkpoints` · `subscriber_dead_letter_queue` · `snapshots`, verified at source).
- **D2 — The activation is ONE WU, later (post-C-003; not before the runway's fulcrum P-1 is in flight):** at the single writer (INV-WRITER-01), `chain_hash(n) = SHA-256( chain_hash(n−1) ‖ canonical(row n) )` where `canonical(row)` is the byte-stable encoding of the row's immutable columns (event id · type · subject · sequence · payload bytes · the timestamps) and `chain_hash(a−1)` for the FIRST hashed row is the zero vector — the AMD-37 genesis by construction, so **history is never re-hashed**; rows before the activation position keep the zero vector and are outside the chain by declaration, not by accident.
- **D3 — The activation position is RECORDED, not inferred:** one row in a new one-row `chain_metadata` table (`activation_position = <globalPosition of the first hashed row>`, `algorithm = 'SHA-256/v1'`, `activated_at`), written in the same transaction as the first hashed row by the activation WU's additive migration (V006). A verifier that finds a zero vector at or after the activation position reports a break; a zero vector before it is genesis.
- **D4 — Mandatory startup verification from the activation position** (the store's own stated gate, `:954`): the tail is recomputed on boot — bounded by a checkpointed "verified-through" position so the cost is the delta, not the log; a mismatch is `PERSISTENCE_FAILURE` (exit 11 under the ExitCode contract), never a silent WARN.
- **D5 — The independent verifier is NOT the product:** a bench verb (`nexsys-bench`) that reads a copied `homesynapse-events.db` read-only and recomputes end-to-end — B-7's measurement instrument, minted before any B-7 sentence.

## Consequences
- **Now:** every public sentence uses *chain-ready*, never *hash-chained*, until D2–D4 land and D5 has matched once on a card. The north-star text gets a bracketed correction at the next strategy touch (the language law).
- **Cost of D2–D4 when built:** one persistence WU (the canonical encoding is the design decision that costs thought; the hashing is a few lines at the writer) + one bench verb (D5) + the ExitCode wiring already exists. Zero migration.
- **What this ADR refuses:** re-hashing history (D2's genesis rule makes it unnecessary); a nullable column (rejected at AMD-37 for the backfill cost); a compliance claim (B-7's fence: "integrity demonstrable", never "compliant").

## The words this asks for (when Nick reads it — not today)
`B7: ratify | edit D<n> <text>` · and one placement word for the docs copy: `B7-DOCS: adr-dir | doc-04-appendix` (there is no `design/adr/` directory yet; the strategic map names `0001-adr-adoption.md` as planned — this would be the first ADR file, or a Doc 04 appendix).

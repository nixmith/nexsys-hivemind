<!-- file: _scratch/v104/b3/AMD-103_independent-review_v5-addendum.md · a focused re-read of Nick's NE1–NE6 (v4 → v5) · v4 34,642 B md5 b8509868… · v5 37,309 B md5 3ec9a405… · script v104b3_nick_edits_1.py md5 8bbf17c3… · core 409547c -->

# AMD-103 v5 — addendum

**Verdict: EDITS.** The diff is exactly Nick's six edits (plus the `file:` and status lines). NE1–NE6 are true and consistent with each other. Three exact edits remain: NE2's lock word, R-C's change trigger (needed so NE3 and NE6 stay true mid-process), and R-F's failed catch-up (§3 assumes it).

## Findings

1. **The diff — HOLDS.** v5 = v4 + the script's ten replacements (NE1, NE2, NE3, NE4, NE5a–d, NE6, and the `file:` line) + the status line (stamped `~15:34 CT`). Rebuilt in memory, it is byte-identical to v5. Lines changed: `:2 :4 :24 :25 :28 :29 :32 :65 :73 :76`.

2. **NE1 — TRUE, and consistent with R-B.** R-B's link is J1's triple: the last reading the tracker kept, with its own frame's instant. A probe reply carries no reading (`StandardAvailabilityTracker.java:358–:362`).

3. **NE2 — TRUE, and the hub's citations are the right ones.** The lock is taken at `:575` and released at `:612–:613`. The sink is called after the unlock (`if (changed)` `:615`, `listener.onTransition` `:618`). The snapshot rule is `:153–:154`. Nick's `:246` and `:254` are the two LOOKUPS' "applied OUTSIDE the lock" (LTD-11, `:440`), not the sink. One word is off: the lock is the tracker's `ReentrantLock` (`:230`), not the run thread's.
Old:
~~~~
a publish is a store write and is never held under the run thread's lock
~~~~
New:
~~~~
a publish is a store write and is never made under the tracker's lock
~~~~

4. **NE3 — the arms match the code exactly, but R-C's triggers can leave the record behind them.** The arms: mains is `0x01`/`0x02` only (`:550–:553`); UNKNOWN and exotic sources fall to the passive arm, the declared interval else 25 h (`:504–:507`); for mains, the contract maximum + 60 s, else the floor (`:515–:518`). But the tracker re-reads the lookups "at EVERY evaluation" (`:243`, `:253`); a capability added later changes a passive limit "without a restart". So a contract declared only at boot, interview and 30 days can name an arm the tracker has left, and R-G's bound and N then read a stale class. Separately, a lookup that throws reads as its fallback for that one cycle (`:530–:536`); the declaration must not record that fallback.
Old:
~~~~
at every boot and every (re-)interview, AND a refresh when 30 days
~~~~
New:
~~~~
at every boot and every (re-)interview, whenever the contract derived at an evaluation differs from the device's last declared one (a cycle whose lookup threw, `:530–:536`, declares nothing), AND a refresh when 30 days
~~~~

5. **NE4 — consistent with R-G and E8** (with no contract, or a null key, the card keeps its S2 form). A `meta` key is additive under the contract's `:260`. But §3 assumes a failed catch-up leaves the boot running, while R-F's catch-up is synchronous in the composition root. Say so in R-F:
Old:
~~~~
and the card keys by device.
~~~~
New:
~~~~
and the card keys by device. A failed catch-up does not fail the boot: the projection stays not LIVE and its keys null (§3).
~~~~

6. **NE5 — consistent across R-F, §4 and R-J (1).** The default can be built on the shipped sink, `AtomicCheckpointSink.writeAtomicCheckpoint(key, position, viewData)` (`state-store …:69`), whose writer upserts V001's `view_checkpoints` together with the subscriber checkpoint (`AtomicCheckpointWriter.java:58`): no migration is needed.

7. **NE6 — consistent, as an upper bound,** provided every asked device's newest contract names its current arm (finding 4).

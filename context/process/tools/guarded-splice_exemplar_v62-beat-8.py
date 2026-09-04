# EXEMPLAR of THE GUARDED-SPLICE LAW — the v62 beat-8 (close) splice, verbatim. NEVER run as-is: copy its SHAPE into
# $HOME/v6N/splice_bN.py with the beat's own anchors, head-text files and caps re-derived. The laws it embodies: date -u first;
# every anchor + every cap asserted BEFORE the first byte; the chain assert reads the WHOLE frontmatter (exactly one
# last-verified: line, exactly two Prior: segments, no stray Prior: line); every fragment .rstrip() before it joins a line;
# DRY RUN by default, --write to write; no commit on a failed splice. Filed at v62 beat 8 (2026-09-04).
# THE v62 CLOSE splice (beat 8) — fresh-written; every assert + every cap BEFORE the first byte. `date -u` first.
import subprocess, sys, datetime, pathlib
H = pathlib.Path.home(); M = H/'mnt'/'ClaudeFolder'/'nexsys-hivemind'; C = M/'context'; V = H/'v62'
PM = C/'handoff'/'pm-handoff.md'; SNAP = C/'status'/'PROJECT_SNAPSHOT.md'; CHARC = C/'handoff'/'archive'/'chains-rotated-2026-08-27.md'
LES = C/'lessons'/'pm-lessons.md'; V63 = C/'handoff'/'2026-09-04_PM-mission-control_v63_orchestrator_session_prompt.md'
BRF = C/'handoff'/'2026-09-03_v62_OPERATOR-BRIEF_for-Nick.md'; DOCKET = C/'planning'/'2026-09-02_R10-docket_ruling-cards_v61-b3.md'
PLAN = C/'planning'/'2026-09_september_plan-of-record.md'; REC = C/'audits'/'2026-09-04_R-4b_re-rep_operator-record.md'
AUD = C/'audits'/'2026-09-04_R-4b_intake_two-layer-audit_v62-beat-7.md'; EXEMPLAR = C/'process'/'tools'/'guarded-splice_exemplar_v62-beat-8.py'
def die(m): print('ASSERT FAIL:', m); sys.exit(2)
z = subprocess.run(['date','-u','+%Y-%m-%dT%H:%M:%SZ'], capture_output=True, text=True).stdout.strip()
utc = datetime.datetime.strptime(z, '%Y-%m-%dT%H:%M:%SZ'); ct = utc - datetime.timedelta(hours=5)
Z = utc.strftime('%H:%M') + 'Z'; CT = ct.strftime('%H:%M')
if utc.strftime('%Y-%m-%d') != '2026-09-04': die('date drift '+z)
rd = lambda p: p.read_text(encoding='utf-8'); fill = lambda s: s.replace('{{CT}}', CT).replace('{{Z}}', Z)
block = fill(rd(V/'b8_block.md')).rstrip('\n'); chain_new = fill(rd(V/'b8_chain.txt')).rstrip('\n')
lv_head = fill(rd(V/'snap8_lv_head.txt')).rstrip(); snap_body = fill(rd(V/'snap8_body.md')).rstrip('\n')
orf = rd(V/'or_failchan8.txt').rstrip('\n'); dock = fill(rd(V/'docket_b8.txt')).rstrip('\n'); plan6 = rd(V/'plan_b8.txt').rstrip('\n')
s10 = fill(rd(V/'record_s10_b8.txt')).rstrip('\n'); a6 = fill(rd(V/'audit_s6_b8.txt')).rstrip('\n'); les = rd(V/'lessons_v62.md').rstrip('\n')
v63 = fill(rd(V/'v63_prompt.md')); bclose = fill(rd(V/'brief_close.md')).rstrip('\n'); bstat = fill(rd(V/'brief_status.txt')).rstrip('\n')
for name, t in [('block',block),('chain',chain_new),('lv',lv_head),('snap',snap_body),('dock',dock),('s10',s10),('a6',a6),('v63',v63),('bclose',bclose),('bstat',bstat)]:
    if '{{' in t: die('unfilled placeholder in '+name)
if '⟨' in v63: die('v63 slot unfilled')
# ---- pm-handoff: whole-frontmatter chain assert ----
pm = rd(PM); L = pm.split('\n'); fm_end = next(k for k,l in enumerate(L) if l.strip() == '-->')
lv_lines = [k for k in range(fm_end) if L[k].startswith('last-verified: ')]
if lv_lines != [7]: die('pm-handoff chain must be exactly line 8: %r' % lv_lines)
if any('Prior:' in L[k] for k in range(fm_end) if k != 7): die('stray Prior: line in pm-handoff frontmatter')
if not L[7].startswith('last-verified: 2026-09-04 (v62 beat 7'): die('line 8 anchor')
i_b6 = L[7].find(' Prior: 2026-09-04 (v62 beat 6'); i_ptr = L[7].find(' Prior: THE v55 b3')
if not (0 < i_b6 < i_ptr): die('chain order')
seg_b7 = 'Prior: ' + L[7][len('last-verified: '):i_b6]; seg_b6 = L[7][i_b6+1:i_ptr]; ptr = L[7][i_ptr+1:]
old = 'AND v62 b5 (v62 b7) SEGMENTS'
if ptr.count(old) != 1: die('pointer anchor')
ptr = ptr.replace(old, 'AND v62 b5 (v62 b7) AND v62 b6 (v62 b8) SEGMENTS')
line8 = chain_new + ' ' + seg_b7 + ' ' + ptr
if line8.count('Prior: ') != 2: die('line 8 must carry exactly two Prior: segments (has %d)' % line8.count('Prior: '))
if len(line8.encode()) > 3000: die('chain cap %d' % len(line8.encode()))
if not L[14].startswith('## 2026-09-04 (v62 beat 7'): die('line 15 anchor')
j = next(k for k in range(15, len(L)) if L[k].startswith('## 2026-09-04 (v62 beat 5'))
n3 = len(block.encode()) + 1 + len('\n'.join(L[14:j]).encode())
if n3 > 18000: die('newest-3 cap %d' % n3)
hf = next(k for k,l in enumerate(L) if l.startswith('#### OR-FAILCHAN')); ef = next(k for k in range(hf+1, len(L)) if L[k].startswith('#### ') or L[k].startswith('**Resolved/closed'))
fc = L[hf:ef]
while fc and fc[-1] == '': fc.pop()
L2 = L[:hf] + fc + [orf, ''] + L[ef:]; L2[7] = line8
L2 = L2[:14] + block.split('\n') + [''] + L2[14:]
pm_new = '\n'.join(L2)
if pm_new.count('## 2026-09-04 (v62 beat 8') != 1: die('block count')
if pm_new.count('(v62 beat 8, the close) — THE §A2 CENSUS READ') != 1: die('OR line')
ch = rd(CHARC); ch = ch if ch.endswith('\n') else ch+'\n'
if 'v62 b6, verbatim' in ch: die('b6 already rotated')
ch_new = ch + '\n## chain segment rotated 2026-09-04 (v62 beat 8) — v62 b6, verbatim\n\n' + seg_b6 + '\n'
# ---- snapshot: whole-frontmatter chain assert ----
sn = rd(SNAP); S = sn.split('\n'); sfm = next(k for k,l in enumerate(S) if l.strip() == '-->')
slv = [k for k in range(sfm) if S[k].startswith('last-verified: ')]
if slv != [7]: die('snapshot chain must be exactly line 8: %r' % slv)
if any('Prior:' in S[k] for k in range(sfm) if k != 7): die('stray Prior: line in snapshot frontmatter')
if not S[7].startswith('last-verified: 2026-09-04 (v62 beat 7'): die('snap anchor')
si_b6 = S[7].find(' Prior: 2026-09-04 (v62 beat 6'); si_ptr = S[7].find(' Prior: THE FULL PRIOR CHAIN')
if not (0 < si_b6 < si_ptr): die('snap chain order')
sseg7 = S[7][len('last-verified: '):si_b6]; sptr = S[7][si_ptr+1:]
snap_lv = lv_head + ' Prior: ' + sseg7 + ' ' + sptr
if snap_lv.count('Prior: ') != 2 or '\n' in snap_lv: die('snap chain shape')
dg = next(i for i,l in enumerate(S) if l.startswith('## The digest'))
S2 = S[:7] + [snap_lv] + S[8:dg] + snap_body.split('\n') + ['']
sn_new = '\n'.join(S2)
if len(sn_new.encode()) > 3500: die('snapshot cap %d' % len(sn_new.encode()))
if [k for k,l in enumerate(sn_new.split('\n')) if l.startswith('last-verified: ')] != [7]: die('snap post-shape')
# ---- lessons ----
lz = rd(LES); lz = lz if lz.endswith('\n') else lz+'\n'
if lz.count('THE v62 CLOSE MINTS') != 0: die('mints already folded')
les_new = lz + les + '\n'
if les_new.count('THE v62 CLOSE MINTS') != 1: die('mints count')
# ---- v63 prompt ----
if 'status: SKELETON — NOT YET LIVE' not in rd(V63): die('v63 skeleton anchor')
if 'status: LIVE from the v62 close' not in v63: die('v63 status')
# ---- brief ----
b = rd(BRF); B = b.split('\n')
if not B[5].startswith('status: LIVE at v62 beat 7'): die('brief status anchor')
if not B[8].startswith('# Operator brief — what Nick does, in order (v62, beat 4'): die('brief title anchor')
if not B[10].startswith('## §0 Banked'): die('brief §0 anchor')
B[5] = bstat; B[8] = '# Operator brief — what Nick does, in order (v62 — CLOSED at beat 8; §CLOSE is the only live section)'
B = B[:10] + bclose.split('\n') + [''] + B[10:]
brf_new = '\n'.join(B)
if brf_new.count('## §CLOSE (beat 8') != 1: die('brief §CLOSE count')
# ---- docket ----
d = rd(DOCKET); D = d.split('\n')
k = next(i for i,l in enumerate(D) if l.startswith('**Row 12 — CLOSED 2026-09-04'))
D = D[:k+1] + [dock] + D[k+1:]; dock_new = '\n'.join(D)
if dock_new.count('**Beat 8 (the v62 close') != 1: die('docket splice')
# ---- plan ----
p = rd(PLAN); P = p.split('\n')
k = next(i for i,l in enumerate(P) if l.startswith('5. **R-4b — DONE'))
P = P[:k+1] + [plan6] + P[k+1:]; plan_new = '\n'.join(P)
if plan_new.count('6. **The v62 close') != 1: die('plan splice')
# ---- record §10 + audit §6 ----
rc = rd(REC); rc = rc if rc.endswith('\n') else rc+'\n'
if rc.count('## §10 Hub verdict surface') != 1 or 'Post-audit correction (v62 beat 8' in rc: die('record anchor')
rec_new = rc + s10 + '\n'
au = rd(AUD); au = au if au.endswith('\n') else au+'\n'
if '## §6 Post-audit corrections' in au: die('audit §6 exists')
aud_new = au + a6 + '\n'
# ---- the exemplar (this script, headed) ----
if EXEMPLAR.exists(): die('exemplar exists')
ex_head = ('# EXEMPLAR of THE GUARDED-SPLICE LAW — the v62 beat-8 (close) splice, verbatim. NEVER run as-is: copy its SHAPE into\n'
           '# $HOME/v6N/splice_bN.py with the beat\'s own anchors, head-text files and caps re-derived. The laws it embodies: date -u first;\n'
           '# every anchor + every cap asserted BEFORE the first byte; the chain assert reads the WHOLE frontmatter (exactly one\n'
           '# last-verified: line, exactly two Prior: segments, no stray Prior: line); every fragment .rstrip() before it joins a line;\n'
           '# DRY RUN by default, --write to write; no commit on a failed splice. Filed at v62 beat 8 (2026-09-04).\n')
ex_new = ex_head + rd(pathlib.Path(__file__))
print('stamp', z, 'CT', CT, '| caps: chain', len(line8.encode()), 'newest3', n3, 'snapshot', len(sn_new.encode()), '| brief', len(brf_new.encode()), 'v63', len(v63.encode()))
if '--write' not in sys.argv: print('DRY RUN OK'); sys.exit(0)
PM.write_text(pm_new, encoding='utf-8'); CHARC.write_text(ch_new, encoding='utf-8'); SNAP.write_text(sn_new, encoding='utf-8')
LES.write_text(les_new, encoding='utf-8'); V63.write_text(v63, encoding='utf-8'); BRF.write_text(brf_new, encoding='utf-8')
DOCKET.write_text(dock_new, encoding='utf-8'); PLAN.write_text(plan_new, encoding='utf-8'); REC.write_text(rec_new, encoding='utf-8'); AUD.write_text(aud_new, encoding='utf-8')
EXEMPLAR.parent.mkdir(parents=True, exist_ok=True); EXEMPLAR.write_text(ex_new, encoding='utf-8')
print('WRITTEN', z)

# Deep reading · Nonlinear Team

This is the record of the deep reading in this team. It is a mixed-tier team: two members were deepened by reading their publications in full or in part wherever an open copy exists, not just as search snippets: `frank-e-curtis` (2026-10-10) and `jorge-nocedal` (2026-10-16 to 2026-10-17, with two T4 increments). The other nine members (Stephen J. Wright, Yinyu Ye, Andreas Wächter, Philip E. Gill, Philippe L. Toint, Nicholas I. M. Gould, Roger Fletcher, Yurii Nesterov, and Daniel P. Robinson, who joined on 2026-10-17) are at the base tier: no deep-reading stage has been run for them (see [The other nine members](#the-other-nine-members-base-tier-no-deep-reading)). Cards and syntheses are written in English.

## Status (2026-10-17)

**Complete for Frank E. Curtis and Jorge Nocedal. Base tier, deep reading not started, for the other nine members.** The numbers below come from `python3 scripts/team_status.py product/nonlinear-team` (with `--coverage`) and, per deepened member, `validate_works.py`, `verify_card_quotes.py` and `check_ledger.py`, all run on 2026-10-17. Stage contents that no script prints come from the stage commits and from each member's `07-paper-cards.md`, `08-deep-reading-synthesis.md` and `10-claim-audit.md`.

| Stage | Workflow / script | Frank E. Curtis (2026-10-10) | Jorge Nocedal (2026-10-16 to 2026-10-17) |
|-------|-------------------|------|------|
| T3.1 Publication list | `team-harvest.js` → `validate_works.py` | ☑ 100 records (S 96 · D 3 · H 1), 4 marked `dup_of`, 0 errors, 1 warning (S084 has no DOI, arXiv id or URL) | ☑ 223 Scholar rows, 56 marked `dup_of` (duplicates and junk rows of another work): 167 distinct works. With the 12 book-material rows added in T4 (B001–B012), `validate_works.py` reports 235 records (B 12 · S 223), 0 errors, 55 warnings (4 near-duplicate titles not linked by `dup_of`; 51 rows without DOI, arXiv id or URL) |
| T3.2 Open full texts | `acquire_fulltexts.py` | ☑ | ☑ 73 of 167 (INDEX.md Source at the stage commit: `url` 50, `arXiv` 22, `unpaywall` 1) |
| T3.3 Chase open copies and abstracts | `team-chase.js` → `merge_chase.py` | ☑ | ☑ 18 more full texts (`manual`), 91 in all; 6 more open PDFs were saved by the round-2 abstract batches, 97 in all |
| T3.4 Reading batches | `plan_reading_batches.py` (one run per round) | ☑ two rounds: 30 core batches, then 1 abstract batch | ☑ three rounds: 14 core + 7 supplement batches (91 texts); 1 core + 1 supplement batch (10 re-reads after OCR) + 3 abstract batches (74 works); 1 core + 1 supplement batch (the 6 newly found texts) |
| T3.5 Cards | `team-read.js` → `verify_card_quotes.py` → `mark_read_from_cards.py` | ☑ | ☑ 181 card entries in 28 batch files; 284 quotes, 257 exact and 27 after normalisation, 0 not found (08 header and §1) |
| T3.6 Synthesis | `team-synthesize.js` → `quality_check.py` | ☑ | ☑ one promotion (Method 7) and two new heuristics; claim audit (`audit_claims.py`, `10-claim-audit.md`): 60 claims, 50 supported and 10 partial, the 10 narrowed and rechecked as supported; `quality_check.py` 12/12 |
| T3.7 Tighten | `team-tighten.js` → `check_ledger.py` | not needed: on 2026-10-17 `team_status.py` reports `SKILL.md` at 11630 words, under its 13000-word default budget; `check_ledger.py` resolves all 36 ledger anchor references | ☑ run after the T4 increments: the stage commit records 13121 → 11666 words; `check_ledger.py --before` the pre-tighten copy passes (98 card ids, 280 cited pages, 126 quotes kept; front matter, Activation Rules and Research Integrity Rules verbatim); 42 ledger anchor references resolve; `team_status.py` now reports 11789 words |
| T3.8 Integrate | `team-integrate.js` → `team_status.py --coverage` → `check_links.py` | ☑ 2026-10-10; refreshed 2026-10-17 | ☑ 2026-10-17 |
| T4 Increments | `team-increment.js` (open parts of books, new papers) | not run: book leads are logged in `book-leads.json` (see [What is still missing](#what-is-still-missing)) | ☑ two: **inc-ocr** (16 works re-read from a tesseract OCR text layer; round 4, 5 batch files; corrections C14–C19) and **inc-book** (12 book-material items, the open parts of *Numerical Optimization*; round 5, 3 batch files; C20–C21). A second claim audit followed: 20 `SKILL.md` claims, 18 supported and 2 partial; 20 ledger and catalog claims, 17 and 3; of the 5 partials, 4 were narrowed and rechecked as supported and 1 left unchanged as a known limit of `audit_claims.py` (the claim names an older card) |

For Frank E. Curtis:

- Every work on his publication list is indexed: 96 distinct works in `papers/INDEX.md`, one row per distinct research work.
- 87 works have an open full text; 86 were read in full and none in part. One open file turned out to be unreadable (S086, see below). No row was skipped.
- Cards written: 96 cards on 96 items in 31 batch files (`c01`–`c30` and `a2-01`), all research works, no book material. Of these, 8 are abstract-level and 1 is metadata only (batch `a2-01`).
- All 180 verbatim quotes on the cards were checked against the extracted text or abstract by `verify_card_quotes.py`: 180 exact, 0 NOT FOUND.
- No openly available book material was carded (no T4 increment was run).
- The cards were then distilled into `SKILL.md` through `08-deep-reading-synthesis.md` and `09-evidence-ledger.md`.

For Jorge Nocedal:

- Every work on his publication list is indexed: 167 distinct works in `papers/INDEX.md` (223 Scholar rows, 56 marked `dup_of`), plus 12 book-material rows (B001–B012), counted apart.
- 97 works have an open full text; 80 were read in full and 17 in part (96 distinct works: S126 is an earlier report of S042, 08 header). No open file is unreadable: text layers that had lost their digits were OCR'd and re-read (10 works in round 2, 16 in inc-ocr). 8 rows were skipped (Role `skip`).
- Cards written: 209 card entries on 177 items in 36 batch files (full 106, partial 29, abstract 44, metadata 30; `07-paper-cards.md`). Research works: 197 entries on 165 publication-list rows (159 research rows plus 6 skip rows with metadata cards, 08 §1) in 33 files (`c01`–`c14`, `s01`–`s07`, `a2-01`–`a2-03`, `c2-01`, `s2-01`, `c3-01`, `s3-01`, `c4-01`–`c4-04`, `s4-01`). Book material: 12 entries on 12 items in 3 files (`c5-01`–`c5-03`). Two cards for one work count as one work (08 header).
- All 340 verbatim quotes on the cards were checked against the extracted text or abstract by `verify_card_quotes.py`: 340 exact, 0 NOT FOUND (284 at the synthesis, 257 exact; 316 after inc-ocr, 288 exact under the §12.1 waiver; 340 after inc-book, all exact; 08 header and §§1, 12.1, 13.1).
- Book material carded (inc-book), from *Numerical Optimization* with S. J. Wright (first edition 1999, S010; second edition 2006, S001): the open front and back matter of both editions (B005, B006; B001, B002), four errata lists (B007, B008 for the first edition; B003 Nocedal's and B004 Wright's copy for the second), two zbMATH reviews by N. Curteanu (B009, B010), the authors' book web pages (B011) and Springer's catalogue pages (B012). The book bodies are not open and were not read.
- The cards were then distilled into `SKILL.md` through `08-deep-reading-synthesis.md` (§§12–13 for the increments) and `09-evidence-ledger.md`.

What changed in the skills:

| Skill | Core methods | Change from the deep reading |
|---|---|---|
| `frank-e-curtis` | 5 | Unchanged count. A proposed **M6 · Guard the incumbent; let the guarantee sleep** (21 distinct full cards) was kept a heuristic on review because exclusivity fails at team level (Wright, Fletcher, Toint and Wächter share the move); it now extends Heuristic 5 as the guarded-incumbent construction. New **Heuristic 11 · Port the property, not the formula**; Heuristic 1 gains a theory–code-gap clause; corrections C1–C12 are marked in place (table: `09-evidence-ledger.md#corrections`); the Roundtable Card lens adds "guard the fast incumbent instead of replacing it". Source: `08-deep-reading-synthesis.md` §§4–5 and its review outcome. |
| `jorge-nocedal` | 7 | New **M7 · Decouple the curvature sample from the gradient sample, and price it in gradients**, promoted from the cards' new-pattern candidates (08 §4 proposed the title *Spend accuracy where the iteration needs it*; on review the method was named after its exclusive device and the principle kept as the rationale in its One line, ledger `#method-7`): stated (co-authored), "Our approach is based on the fact that less accuracy in the Hessian is required than in the gradient" [jorge-nocedal card S023 p. 3]; practised [jorge-nocedal card S018 pp. 4–5, 15–17] [jorge-nocedal card S015 pp. 5, 8–9] [jorge-nocedal card S033 pp. 3–5]; the inner-solve stop is cited as shared with Curtis's Method 1, not claimed. New **Heuristic 11 · Harvest the curvature the solver already computes** [jorge-nocedal card S088 p. 10] [jorge-nocedal card S030 pp. 2, 4, 6] [jorge-nocedal card S098 p. 8], kept a heuristic although it passes the checks, because an eighth method would have no weaker method to replace (08 §10 item 13); new **Heuristic 12 · Validate every in-algorithm estimate against the truth** [jorge-nocedal card S018 p. 20] [jorge-nocedal card S084 p. 19] [jorge-nocedal card S062 p. 8]. Corrections C1–C13 (synthesis), C14–C19 (inc-ocr) and C20–C21 (inc-book) are marked in place (table: `09-evidence-ledger.md#corrections`). Roundtable Card: *Leads when* gains sampled second-order methods (Method 7), the default recommendation gains "In sampled methods, give curvature its own cheap sample", the Wright line says book evidence is joint, the blind spot *reformulation* is marked partly answered [jorge-nocedal card S047 pp. 9–11], and the blind spot *degeneracy* is narrowed to degeneracy at solutions [jorge-nocedal card S061 pp. 18, 24] (C19); the one-line lens is unchanged. (The card's other changes since the base tier, the shortened First-questions preamble and Gill line and the new Robinson line, came with Robinson's team-layer commit 9d5aa72, not from the deep reading.) Book material promoted nothing (08 §13.8). |
| `stephen-j-wright` | 6 | Base tier, no deep reading: unchanged. |
| `yinyu-ye` | 5 | Base tier, no deep reading: unchanged. |
| `andreas-wachter` | 6 | Base tier, no deep reading: unchanged. |
| `philip-e-gill` | 6 | Base tier, no deep reading: unchanged. |
| `philippe-l-toint` | 4 | Base tier, no deep reading: unchanged. |
| `nicholas-i-m-gould` | 6 | Base tier, no deep reading: unchanged. |
| `roger-fletcher` | 6 | Base tier, no deep reading: unchanged. |
| `yurii-nesterov` | 6 | Base tier, no deep reading: unchanged. |
| `daniel-p-robinson` | 4 | Base tier (joined 2026-10-17), no deep reading. |

Core-method counts are the `### Method N` sections of each `SKILL.md` on 2026-10-17 (Nocedal: 6 before the synthesis, 08 §4).

Both deepened skills gained the following files:

- `references/technique-catalog.md`: transferable devices from the papers (proof devices, algorithm-design moves, experiment and evaluation protocols, writing moves; Nocedal's also has a section on textbook, errata and reading moves from the book material), each with card references.
- `references/research/07-paper-cards.md`: the card index, generated from the digests by `scripts/build_card_index.py`.
- `references/research/08-deep-reading-synthesis.md`: patterns, promotions and corrections (Nocedal's §§12–13 record the two increments).
- `references/research/09-evidence-ledger.md`: the full evidence behind each `SKILL.md` item (for Nocedal, also the evidence moved out of `SKILL.md` when it was tightened). `SKILL.md` links to its anchors.
- `references/research/10-claim-audit.md`: the sampled claim-to-card audits and their fixes.
- `references/sources/publications/works.json` and `scholar.md` (the audited publication list) and `references/sources/papers/INDEX.md`, `abstracts.json`, `abstract-sources.json`, `book-leads.json`.

In `nonlinear-roundtable` (refreshed in the same T3.8 run; its Honest Boundary keeps the dated record), no fault line was added or dropped: the six-line maximum is still reached. Curtis's side of fault lines 1, 3 and 5 has cited his paper cards since 2026-10-10. On 2026-10-17 Nocedal's sides of fault lines 1–3 moved from his research notes to his paper cards: in fault line 1 (infeasibility) his co-authored papers sit on both sides [jorge-nocedal card S052 p. 2] [jorge-nocedal card S053 pp. 3–5, 8, 11–12]; in fault line 2 (step acceptance) the steering paper keeps the penalty and sets it against an auxiliary LP [jorge-nocedal card S042 pp. 7–11, 15–16, 20]; in fault line 3 (worst-case complexity as a design guide) the *Acta Numerica* survey and the 2020 subsampled-Newton study speak for him [jorge-nocedal card S019 pp. 2, 15] [jorge-nocedal card S041 pp. 11, 14–15], and the entry also cites his own tension (Inner Tension IT5): the same survey calls global-efficiency results "very useful" [jorge-nocedal card S019 p. 2], and the co-authored 2018 survey credits SG's success to its complexity guarantees [jorge-nocedal card S004 p. 82]. In fault line 2, that the steering paper answers the filter's critique is an inference of Fletcher's notes, not an exchange in print. Its Team table extends Nocedal's lens shorthand for Method 7 (curvature on its own cheap sample), and the member brief points each member to its `09-evidence-ledger.md` for each method's card ids. The base-tier sides keep their research-note evidence; fault lines 4 and 6 involve only base-tier members.

## Pipeline

As used for `frank-e-curtis` on 2026-10-10 and for `jorge-nocedal` on 2026-10-16 to 2026-10-17 (one member at a time, each stage committed). How to launch each workflow and its arguments: `scripts/workflows/README.md`. Never commit PDFs, extracted text or `private/`.

1. **Publication list (T3.1, `team-harvest.js`).**
   - Curtis: `works.json` records its basis as "Google Scholar profile + DBLP + Crossref (+ homepage); arXiv ids also filled from the arxiv.org author listing (searchtype=author)", harvested and audited 2026-10-10. Per-record `sources` tags: scholar 96, homepage 88, dblp 73, arxiv 54, crossref 15. The audit note: "independent year-sorted Scholar pass (96 rows, all matched); 20 DOIs and 10 arXiv ids spot-checked, none wrong".
   - Nocedal: `works.json` records "Google Scholar profile + DBLP + Crossref + arXiv + homepage", harvested 2026-10-16. Per-record `sources` tags: scholar 223, dblp 76, homepage 74, crossref 30, arxiv 18, zbmath 5, springer 5, wayback 4 (the springer and wayback tags, two of the zbmath tags and five of the homepage tags are on the B rows). `scholar.md` records the audit: an independent year-sorted pass over all 223 rows matched every row; all 83 DBLP records and all 69 homepage entries matched Scholar rows (0 DBLP-only, 0 homepage-only items); all 101 DOIs resolved and were compared with Crossref titles, none wrong; every arXiv id was opened, none wrong; four years were corrected (S097, S141, S177 from Crossref and zbMATH; S150 from Crossref and DBLP).
   - IDs beyond `S` (Scholar row) used in this team: in `frank-e-curtis`, `D` = bibliographic database only, 3 items (D001 *Adaptive Stochastic Optimization*, 2020, DBLP + arXiv; D002 *Single-Loop Deterministic and Stochastic Interior-Point Algorithms…*, 2024, DBLP + homepage + arXiv; D003, marked `dup_of` S050) and `H` = author homepage only, 1 item (H001 *An Inexact Regularized Newton Framework…*, 2019, homepage + Crossref + arXiv); three Curtis Scholar rows are duplicates (S080 → S003, S085 → S057, S095 → S040). In `jorge-nocedal`, `B` = openly available part of a book, 12 items (B001–B012, added in inc-book). No `R` or `X` items in either.
2. **Open full texts (T3.2, `acquire_fulltexts.py`).** arXiv by id or title search, Unpaywall, then the author or repository links in `works.json`; title check on the first pages; text extracted with `[[page N]]` markers, tesseract OCR for scans. For Nocedal the first run indexed 73 of 167 works (`url` 50: every one of them lists his Northwestern IEMS pages among its `works.json` URLs; `arXiv` 22; `unpaywall` 1). Several of his text layers had lost every digit, Greek letter and the fi/ff ligatures (08 §12): five texts were OCR'd while planning round 1 (S020, S039, S085, S138, S188), ten digit-less texts before round 2 and sixteen in inc-ocr (stage commits), and the kit's `acquire_fulltexts.py` now detects digit-less layers and OCRs them itself. One Curtis run recorded in the scratch log stopped on a Windows console encoding error (a title character the cp1252 console could not print); set `PYTHONUTF8=1` on Windows.
3. **Chase (T3.3, `team-chase.js` → `merge_chase.py`).** Which copy each `manual` file was saved from is not recorded in INDEX.md; the URLs `works.json` lists for those rows are given here.
   - Curtis: INDEX.md's Source column reads `manual` 57, `url` 16, `arXiv` 14, none 9 (the 9 `no-oa` rows); the merge run reported "57 new full texts". The URLs listed for the `manual` rows point to arXiv (39 rows), Curtis's Lehigh COR@L homepage (18 rows), MERL technical reports (S071, S077) and open-access Springer article PDFs (S063, S073). Abstracts for works without open text came from Semantic Scholar (S031), Springer landing pages (S055, S079), OpenAlex (S078) and, for the 2025 book S074, a retailer's copy of the publisher's description (`abstract-sources.json`).
   - Nocedal: the chase added 18 `manual` rows (INDEX.md at the chase commit). Their URLs point to the AMS (S007, S160), INRIA HAL (S012, S115), LSEC, `lsec.cc.ac.cn` (S020, S054), NYU (S026), the CU Boulder repository (S039), his Northwestern pages (S058, S085; S058 also STFC ePubs, S085 also the Namur repository), IJEE (S090), Optimization Online (S126), the Rice repository (S138, his thesis), the Internet Archive (S143), the RAL Numerical Analysis Group pages (S179, S188) and OSTI (S193, S197). Six more open PDFs, for works first carded in the round-2 abstract batches (S016, S043, S063, S064, S120, S139; listed URLs: the NeurIPS proceedings and his Northwestern pages for S043, his Northwestern pages for S064, a DOI and a DBLP link for S016, none for S063, S120 and S139), were indexed with the round-2 cards and read in round 3. INDEX.md now reads `url` 50, `manual` 24, `arXiv` 22, `unpaywall` 1, none 70 (the `no-oa` rows), plus 12 `manual` B rows. `abstract-sources.json` names the source of 34 abstracts: NSF award records 15, OpenAlex 5, Springer landing pages 4, OSTI 3, zbMATH 3, Optimization Online 2, NeurIPS proceedings 1, Internet Archive 1. `book-leads.json` lists the open parts of *Numerical Optimization* (S001, S010) that inc-book later carded. What the Nocedal merge run printed is not recorded.
   - **No shadow libraries, no paywall circumvention.**
4. **Reading batches (T3.4, `plan_reading_batches.py`).** Curtis: round 1, 96 rows, 87 full texts in 30 core batches (`c01`–`c30`, 1–4 papers each), 0 skipped; round 2, the 9 works without open text in one abstract batch (`a2-01`). Nocedal (round and card counts from the Batches table of `07-paper-cards.md`): round 1, 91 full texts in 14 core batches (`c01`–`c14`, 1–5 papers) and 7 supplement batches (`s01`–`s07`, 2–8 papers); round 2, re-reads of 10 works after OCR (`c2-01`, `s2-01`) and 74 works in three abstract batches (`a2-01`–`a2-03`); round 3, the six newly found texts (`c3-01`, `s3-01`); round 4 (inc-ocr), 16 re-reads (`c4-01`–`c4-04`, `s4-01`); round 5 (inc-book), 12 book-material items (`c5-01`–`c5-03`). Whether a round was fixed by hand with `--round N --exclude` is not recorded.
5. **Cards (T3.5, `team-read.js`).** One agent per batch wrote `references/research/cards/<batch>.md` and `<batch>.digest.json` with the brief below; `07-paper-cards.md` indexes every card (regenerated by `build_card_index.py`).
6. **Quote check.** `scripts/verify_card_quotes.py` (2026-10-17): Curtis 180 quotes, 180 exact, 0 NOT FOUND; Nocedal 340 quotes, 340 exact, 0 NOT FOUND.
7. **Read column.** `scripts/mark_read_from_cards.py` filled INDEX.md's Read column. Curtis: carded 86, abstract 8, metadata 1, unreadable 1; no unread rows. Nocedal: carded 80, skimmed 17, abstract 39, metadata 29 (6 of them skip rows), `—` 2 (the talks S146 and S175, Role `skip`, no card); B001–B012 carded.
8. **Synthesis (T3.6, `team-synthesize.js`).** One agent mined the cards into `08-deep-reading-synthesis.md`; a conservative edit of `SKILL.md` wrote `09-evidence-ledger.md` at the same time; read-only skeptics reviewed it. Curtis: the proposed Method 6 was kept a heuristic. Nocedal: Method 7 promoted and renamed on review, Heuristics 11 and 12 added. Each member's claim audit (`scripts/audit_claims.py`, protocol `references/claim-audit.md`) sampled claims and had zero-context auditors check them against the cited cards; the results are in `10-claim-audit.md` (Curtis: 41 supported, 19 partial, 0 unsupported; the 19 partials were narrowed, a recheck found 16 supported and 3 partial, and those 3 plus one caveat edit were tightened without a further recheck; Nocedal: see the stage table).
9. **Tighten (T3.7, `team-tighten.js`).** Curtis: not run, under the word budget. Nocedal: run after both increments (13121 → 11666 words), proved lossless by `check_ledger.py --before`.
10. **Increments (T4, `team-increment.js`).** Nocedal only: inc-ocr re-read sixteen works whose round-1 texts had lost every digit (08 §12); inc-book carded the open parts of *Numerical Optimization*, read as the joint voice of Nocedal and S. J. Wright, with the reviews as the reviewer's voice and the catalogue as the publisher's (08 §13).
11. **Integrate (T3.8, `team-integrate.js`).** The team README, this file and the roundtable's fault lines were refreshed from the 08 syntheses and the members' paper cards (quotations outside the cards' Quotes lists re-read in the carded files); the coverage table below comes from `team_status.py --coverage` and the README's five-column summary from `--coverage --short`; `scripts/check_links.py` checks every link.

### Commands, per researcher

Run these from the repository root. On Windows set `PYTHONUTF8=1` for every Python script. Needs network access to arxiv.org, api.unpaywall.org and api.crossref.org, plus `pypdfium2` and Pillow; `tesseract` (OCR) for older papers.

```bash
T=product/nonlinear-team
R=jorge-nocedal                      # each deepened member's "slug" in $T/team.json (frank-e-curtis, jorge-nocedal)
S=${TMPDIR:-/tmp}/nonlinear-team-scratch; mkdir -p "$S"   # plan JSON and backups stay outside the repo
D=<YYYY-MM-DD>                       # the date passed to the workflow run

python3 scripts/team_status.py $T    # where every member stands

# T3.1 after team-harvest.js
python3 scripts/validate_works.py $T/$R
# T3.2 open full texts + INDEX.md
python3 scripts/acquire_fulltexts.py $T/$R
# T3.3 after team-chase.js
python3 scripts/merge_chase.py $T/$R
# T3.4 reading batches, one round per wave of new full texts; --out-dir picks the next round and excludes the other plans in $S
#    to fix the round by hand: add --round N --exclude "$S/batches-$R-r1.json,…" (plans still being read)
python3 scripts/plan_reading_batches.py $T/$R --out-dir "$S" --no-abstract
python3 scripts/plan_reading_batches.py $T/$R --out-dir "$S"          # last round: abstract/metadata batches
# T3.5 after team-read.js
python3 scripts/verify_card_quotes.py $T/$R
python3 scripts/mark_read_from_cards.py $T/$R
python3 scripts/build_card_index.py $T/$R                             # regenerate 07-paper-cards.md
# T3.6 after team-synthesize.js
python3 scripts/quality_check.py $T/$R/SKILL.md
python3 scripts/check_ledger.py $T/$R
python3 scripts/check_citations.py $T --member $R
# T3.7 after team-tighten.js (it saves the pre-tighten copy itself)
python3 scripts/check_ledger.py $T/$R --before "$S/$R-SKILL.before-tighten-$D.md"
# T4 after team-increment.js: the T3.5 checks again, then build_card_index.py
# T3.8 team level, after team-integrate.js
python3 scripts/team_status.py $T --coverage           # paste into Coverage below, unchanged
python3 scripts/team_status.py $T --coverage --short   # the five-column summary for the team README, unchanged
python3 scripts/check_links.py $T
python3 scripts/check_citations.py $T --roundtable
python3 scripts/team_check.py $T                       # delivery gate; judges the tier per member
```

Workflows in `scripts/workflows/`: `team-harvest.js` (T3.1), `team-chase.js` (T3.3), `team-read.js` (T3.5), `team-synthesize.js` (T3.6), `team-tighten.js` (T3.7), `team-integrate.js` (T3.8), `team-increment.js` (T4).

## Coverage

These counts are exact and were computed from each researcher's `references/sources/papers/INDEX.md` by `python3 scripts/team_status.py product/nonlinear-team --coverage`. Paste its output here; never edit a number by hand.

| Researcher | Scholar rows | Distinct works indexed | Open full text | Read in full | Read in part | Abstract only | Metadata only (incl. unreadable) | Skipped (not the author's / non-research) | Book material carded | Quotes verified |
|---|---|---|---|---|---|---|---|---|---|---|
| Frank E. Curtis | 96 | 96 | 87 | 86 | 0 | 8 | 2 | 0 | 0 | 180 |
| Jorge Nocedal | 223 | 167 | 97 | 80 | 17 | 39 | 23 | 8 | 12 | 340 |
| Stephen J. Wright | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| Yinyu Ye | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| Andreas Wächter | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| Philip E. Gill | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| Philippe L. Toint | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| Nicholas I. M. Gould | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| Roger Fletcher | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| Yurii Nesterov | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| Daniel P. Robinson | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| **Total** | 319 | 263 | 184 | 166 | 17 | 47 | 25 | 8 | 12 | 520 |

Notes:

- The zero rows are the nine base-tier members: they have no audited publication list and no `INDEX.md`, so nothing is counted for them. A zero means "not indexed", not "no publications".
- *Distinct works indexed* = Scholar rows minus duplicates, plus items found only in DBLP or on a homepage. Curtis: 96 Scholar rows − 3 duplicates + D001, D002, H001 = 96. Nocedal: 223 Scholar rows − 56 rows marked `dup_of` (duplicates and junk rows of another work) = 167; no DBLP-only or homepage-only items. No interviews, memoirs or other special items are counted for either; both have a Google Scholar profile.
- *Metadata only (incl. unreadable)*: Curtis = S084 (metadata only) + S086 (unreadable); Nocedal = 23 metadata-only rows, none unreadable. Nocedal's abstract and metadata rows include 17 NSF award records (15 abstract, 2 metadata), used to date interests and never as the sole support of a method decision (08 header).
- *Read in part* means the supplement reading: abstract, introduction, method or algorithm, main result, experimental setup and conclusion. Curtis has none: all 87 open texts were planned as core reads. Nocedal has 17 (INDEX.md Read = `skimmed`).
- *Read in full* counts INDEX rows: Nocedal's 80 include S126, a 2006 report of the work published as S042, so his synthesis counts 96 distinct works read in full or in part.
- *Book material carded* counts the `B` rows in INDEX.md: openly available parts of a book. Curtis has none; Nocedal's 12 are B001–B012 (Status above), not counted in the research-work columns.
- *Skipped* rows have Role `skip` in INDEX.md. Curtis has none; his pre-PhD combinatorics papers (S058, S081, S086) are carded but carry no weight in the synthesis (08, counting rules). Nocedal has 8: S155 is not his; S164, S165, S214, S215 and S218 are non-research rows (metadata cards, never used as evidence); S146 and S175 are talks without a card.
- Page references on cards are pages of the text version that was read, often a technical report or preprint. Check the journal page before citing one in a paper.

## Reading-batch brief (as used, shortened)

The full brief lives in `scripts/workflows/team-read.js`; this is the record.

```
You are deep-reading research works by {name} to deepen the research-craft skill at {skill}/.
Read first: references/paper-reading-card.md (card format) and SKILL.md's methods, heuristics and taste sections.
Batch {bid} (mode core | supplement | book | abstract): the work list is that batch in the plan JSON (ids, pages, txt paths).
core → read the whole work, full card D1–D8; supplement → abstract, introduction, method, main result, setup,
conclusion, short card; book → chapter level plus a chapter map; abstract → abstract or metadata card only, say which.
Follow a work's "note" (what it is, whose voice): a review is the reviewer's voice; a table of contents is title-only.
Check page 1 first: title and the member's surname among the authors, else "unreadable" + WRONG-TEXT; garbled → REOCR.
Write cards/{bid}.md (batch intent, focus dimensions, material roles, file-to-printed page mapping, one card per work)
and cards/{bid}.digest.json (one object per work: read_level, D1–D8 lines, method_links, quotes, …).
Rules: a page reference on every claim; at most two verbatim quotes per card, with page, that must pass
verify_card_quotes.py; "not read" rather than guess; link cards to Method N / heuristics as evidence, variant or
contradiction. No WebSearch in reading batches; abstract batches may use Crossref, arXiv, Semantic Scholar and open
publisher pages and save an open PDF for the next round, never shadow libraries or paywall circumvention.
Never read references/sources/private/. Edit no file other than the batch's own outputs.
```

## What is still missing

- **Works with no open full text** have abstract or metadata cards only (Abstract only + Metadata only in the Coverage table): Curtis 10 of 96 (8 + 2, the 2 including the unreadable S086); Nocedal 62 of 167 (39 + 23); 0 for the other nine, who are not indexed. Their evidence carries less weight in the syntheses.
  - Curtis's biggest gaps (his 08 "Open gaps"): the stochastic inexact SQO paper S045 (its termination tests for stochastic gradients known only from the abstract); the ε-constraint fairness paper S055 and the bilevel synthetic-data paper S072; the SCOPF journal paper S060 (its preprint S061 was read); the adaptive stochastic optimization framework S031 (the D001 article was read); a workshop report S078; the MOPTA proceedings S079; the hard-constraint training paper S084 (metadata only).
  - Nocedal's biggest gaps (his 08 §11): the 1989 analysis tool S017 behind Method 5's theory for backtracking line searches (abstract only), with the negative-φ Broyden paper S044, column scaling S108 and the 1990–91 numerical studies S100 and S025; most 1980s work (the reduced-Hessian work with Overton S022, the conic methods S086 and S103, the 1985 step-direction evaluation S204, the trust-region view of CG S177: abstract only); the 2008 penalty line-search precursor S140 and the MPEC interior work S181 (metadata only); the KNITRO 2.0 manual S066 (metadata only); the 2024 SCOPF entry S166 and the 2020 sampling award S167 (abstracts).
- **Book bodies** were not read.
  - Curtis's 2025 SIAM book *Practical Nonconvex Nonsmooth Optimization* (S074) is known only from a retailer's copy of the publisher's description, so its treatment of BFGS-SQP, gradient sampling and NonOpt is not known; SIAM front and back matter returned 403 to `curl` (`book-leads.json`). For the MOPTA 2010 proceedings (S079), the publisher's free front-matter PDF and table-of-contents page are logged as leads. No T4 increment has carded either.
  - Nocedal's *Numerical Optimization* with S. J. Wright, first edition 1999 (S010) and second edition 2006 (S001): the bodies are closed. Read in inc-book: the front matter with the prefaces and contents and the back matter with the appendices of both editions (B005, B006; B001, B002), the corrections to the first and second printings of the first edition (B007, B008), the two copies of the second edition's errata, Nocedal's and Wright's (B003, B004), N. Curteanu's two zbMATH reviews (B009, B010), the authors' book web pages (B011) and Springer's catalogue pages (B012). All of it is the joint voice of Nocedal and Wright (the reviews are the reviewer's, the catalogue mostly the publisher's), so how *he* teaches algorithm design is still not separable from the joint text (08 §11). Nocedal's errata copies were read through Internet Archive captures and Wright's live on his homepage (the errata host timed out on 2026-10-17); no book-material item mentions a third edition (08 §13.9).
- **Uneven periods.** Curtis, full reads by period (full / carded, 08 §1): 2003–2007 4/5; 2008–2012 9/10; 2013–2017 19/19; 2018–2022 27/28; 2023–2026 27/34; eight of the nine works without an open text date from 2020–2026, the ninth is S079 (2012). Nocedal, open full text / no open text per decade (INDEX.md, skip rows left out): 1970s 2/2; 1980s 4/17; 1990s 22/17; 2000s 32/12; 2010s 26/7; 2020s 11/3; undated 0/4. His 1980s are thin in full text (08 §8.1).
- **Unreadable files** are listed on their cards: `frank-e-curtis` S086 (2003 William & Mary undergraduate thesis; garbled text layer; card in `c01`; combinatorics, outside the skill's scope). `jorge-nocedal`: none; after OCR some tables are still illegible: ten tables of the 1989 L-BFGS study S002, Table 2 and most rows of Tables 1 and 3 of S088 (its card stays partial), 16 of the 29 rows of Table 4.1 of S101 (08 §12.1).
- **Versions**: Nocedal's S005, S014 and S061 were read in report versions, not the journal texts; later versions of S080, S032, S091 and S150, and SQN v1 of S015, were not read (08 §§11, 12.1).
- **Outside the publication list**: talks, syllabi, code history, student theses and (for Nocedal) the 2026 interview remain web-research evidence (notes 01–06; caption-derived quotes); the deep reading neither confirms nor refutes Curtis's slide-only claims (his 08 "Open gaps"), and Nocedal's origin stories still rest on the interview, since the full texts tell none (his `SKILL.md` Honest Boundary).
- **The nine base-tier members** have no full-text reading at all (see [The other nine members](#the-other-nine-members-base-tier-no-deep-reading)).

### How to extend

1. **Get a legitimate copy.** Sources are a library, publisher access or the author.
2. **Name the file like the index.** Use `<ID>-<year>-<first eight title words, lowercased, hyphenated>.pdf`, the stem `acquire_fulltexts.py` uses (the ID is the one in INDEX.md).
3. **Put it in `<researcher>/references/sources/papers/`.** This folder's PDFs and `txt/` are git-ignored. Check by hand that the file is the paper, because the title check only runs on downloads.
4. **Re-run the acquire script.** `python3 scripts/acquire_fulltexts.py product/nonlinear-team/<researcher> --only <ID>` extracts the text, OCRs scans, and sets `Full text = txt` and `Source = manual`. Run it in the checkout that holds the other papers' PDFs and `txt/`: rows without local files keep their committed status, but their quotes cannot be re-verified.
5. **Card and fold it in.** Either run `team-increment.js` (T4; see `scripts/workflows/README.md`), which cards the new material, folds it into the skill, verifies and fixes; or by hand: plan a new round with `python3 scripts/plan_reading_batches.py product/nonlinear-team/<researcher> --out-dir <scratch> --no-abstract` (or `--round N --exclude <plan files still being read>`), read with the brief above, run `verify_card_quotes.py` and `mark_read_from_cards.py`, regenerate `07-paper-cards.md` with `python3 scripts/build_card_index.py <member folder>`, and apply the conservative-update rules to `SKILL.md`, `09-evidence-ledger.md` and `technique-catalog.md`.
6. **Refresh the numbers.** Re-run `python3 scripts/team_status.py product/nonlinear-team --coverage` and paste it unchanged into the Coverage table here; paste `--coverage --short` unchanged over the five-column summary in the team README (or run `team-integrate.js`, which does both).

## The other nine members (base tier, no deep reading)

Stephen J. Wright, Yinyu Ye, Andreas Wächter, Philip E. Gill, Philippe L. Toint, Nicholas I. M. Gould, Roger Fletcher, Yurii Nesterov and Daniel P. Robinson (joined 2026-10-17) are at the base tier: no deep-reading stage has been run for them. `team_status.py` reports each at "T1 base skill" with `SKILL.md` at 12/12 and notes 01–06 complete, next step "base tier done; deep tier: team-harvest.js (T3.1)". Their skills rest on web research only: the six research notes in `references/research/`, `RESOURCES.md`, and the OpenAlex pull the notes started from (`publications/publications.md`, `abstracts.md`; for Robinson it was made after his notes, whose note 01 assembled his list from DBLP, Crossref, OpenAlex and his homepage), which is raw material, not an audited publication list. They have no `works.json`, `papers/INDEX.md`, paper cards, 07–10 or technique catalog, so their Coverage rows are zero and their sides of the roundtable's fault lines cite their notes and the papers those rest on, not cards. Nocedal's book material is joint with Wright, so it is never read as either lens's alone (Nocedal's 08 §13.2).

To deepen one of them later, run stages T3.1–T3.8 of `references/research-team-playbook.md` for that member (the commands above with `R=<slug>`); `team_check.py` then checks that member at the deep tier, and this file and the README are refreshed by `team-integrate.js`.

## Privacy and integrity

- Private materials stay in each member's `references/sources/private/` (git-ignored) and are never read into public files. The deep reading worked only from public sources.
- PDFs and extracted text (`papers/*.pdf`, `papers/txt/`) are git-ignored for copyright reasons. Only indexes, abstracts, cards and syntheses are committed.
- Full texts come only from legitimate open copies: arXiv, Unpaywall, author pages, institutional report series and open repositories; Nocedal's book material comes from Springer's free previews and catalogue, zbMATH Open and the authors' own pages (live or as Internet Archive captures).
- The integrity rules in each skill still apply. No claim goes in without a page reference, and no quote is invented: every quote on a card passes `scripts/verify_card_quotes.py`. Nothing written by a co-author, reviewer or interviewer is attributed to the member: Nocedal's textbook material is the joint voice of Nocedal and Wright, and the zbMATH reviews are N. Curteanu's.

<!-- Deep-reading record from references/team-templates/DEEP-READING.md: scaffold by scripts/new_team.py (T0, 2026-10-10); stage
     table ticked with the team layer (team-layer.js, T2); integrated by scripts/workflows/team-integrate.js (T3.8) on 2026-11-20 for
     Leyffer, Misener, Burer and Dey. Grossmann and Sahinidis are in progress (T3.2): rerun team-integrate.js once their synthesis
     (T3.6) exists; it refreshes Status, the skills table, the roundtable line, Coverage and What is still missing.
     T4: scripts/workflows/team-increment.js adds book material and new papers. -->

# Deep reading · MINLP Team

This is the record of how the skills of Ignacio E. Grossmann, Sven Leyffer, Nikolaos V. Sahinidis, Ruth Misener, Samuel Burer, Santanu S. Dey are deepened. Each researcher's publications are read in full or in part wherever an open copy exists, and not just as search snippets. Cards and syntheses are written in English.

## Status (2026-11-20)

**Complete for Sven Leyffer, Ruth Misener, Samuel Burer and Santanu S. Dey.** **In progress for Ignacio E. Grossmann and Nikolaos V. Sahinidis** (stage T3.2): their publication lists are audited and their open full texts indexed, but none of their works is carded yet, so their skills still rest on web research (research notes 01–06). The numbers below come from `python3 scripts/team_status.py product/minlp-team` (with `--coverage`), `validate_works.py`, `verify_card_quotes.py`, `check_ledger.py` and `build_card_index.py --check`, all run on 2026-11-20. Stage contents that no script prints come from the stage commits and from each member's `07-paper-cards.md`, `08-deep-reading-synthesis.md` and `10-claim-audit.md`. Progress at any time: `python3 scripts/team_status.py product/minlp-team`.

| Stage | Workflow / script | Done |
|-------|-------------------|------|
| T3.1 Publication list | `team-harvest.js` → `validate_works.py` | ☑ all six members (harvested and audited 2026-10-10); `validate_works.py` reports 0 errors for each (records in [Pipeline](#pipeline)) |
| T3.2 Open full texts | `acquire_fulltexts.py` | ☑ all six members (2026-10-10). Open full texts in INDEX.md at the stage commits: Grossmann 442, Leyffer 57, Sahinidis 28, Misener 61, Burer 67, Dey 113 |
| T3.3 Chase open copies and abstracts | `team-chase.js` → `merge_chase.py` | ☑ Leyffer (57 → 162 open texts), Misener (61 → 102), Dey (113 → 123) and Burer (no new legitimate full text, two abstracts), all 2026-10-10. Sahinidis's run was stopped on 2026-10-10 and not resumed (no `manual` full texts in his INDEX.md); not run for Grossmann |
| T3.4 Reading batches | `plan_reading_batches.py` (one run per round) | ☑ Leyffer and Misener two rounds, Burer and Dey three (batches in [Pipeline](#pipeline)); not run for Grossmann and Sahinidis |
| T3.5 Cards | `team-read.js` → `verify_card_quotes.py` → `mark_read_from_cards.py` | ☑ Leyffer 204 cards, Misener 146, Burer 73, Dey 154, all written on 2026-10-10, each with 0 unread INDEX rows and 0 quotes NOT FOUND; Grossmann and Sahinidis have none |
| T3.6 Synthesis | `team-synthesize.js` → `quality_check.py` | ☑ Burer and Dey on 2026-10-10, Leyffer and Misener on 2026-11-19, each with a claim audit (`10-claim-audit.md`) |
| T3.7 Tighten | `team-tighten.js` → `check_ledger.py` | ☑ Leyffer (12613 → 11658 words) and Misener (12030 → 11508) on 2026-11-19, counted then with `wc -w`, the Answer Standard section included. Not needed for Burer and Dey: both were under the 13000-word budget on 2026-10-10 and still are (Burer 12383, Dey 11639 words), since from 2026-11-20 the budget leaves out the Answer Standard section that `answer_standard.py` writes into every skill (`answer_standard.py --words`; with it, Burer's `SKILL.md` was 13586 words) |
| T3.8 Integrate | `team-integrate.js` → `team_status.py --coverage` → `check_links.py` | ☑ 2026-11-20 for Leyffer, Misener, Burer and Dey; rerun once Grossmann and Sahinidis finish the synthesis (T3.6) |
| T4 Increments | `team-increment.js` (open parts of books, new papers) | ☐ not run for any member: no book material is carded; Leyffer's and Dey's book leads are logged in their `book-leads.json` |

For Sven Leyffer:

- Every work on his publication list is indexed: 211 distinct works in `papers/INDEX.md` (224 Scholar rows, 29 marked `dup_of`, plus 2 `D` and 14 `H` items).
- 164 works have an open full text: 120 were read in full and 35 in part, 6 turned out unreadable (broken font layers; each card says so), and 3 carry abstract or metadata cards (S033 and S127, whose open copies the round-2 abstract batches saved for a later round, and the participant list S210). 7 rows were skipped (talks).
- Cards written: 204 cards on 204 works in 36 batch files (`c01`–`c20`, `s01`–`s14`, `a2-01`, `a2-02`), none of them book material (no `B` rows); the non-research rows among them are listed under [Coverage](#coverage), Notes.
- All 329 verbatim quotes on the cards were checked against the extracted text or abstract by `verify_card_quotes.py`: 323 exact, 6 matching once spacing and symbols are ignored, 0 NOT FOUND.
- The cards were distilled into `SKILL.md` through `08-deep-reading-synthesis.md` and `09-evidence-ledger.md` on 2026-11-19, and the evidence was then moved to the ledger (T3.7).

For Ruth Misener:

- Every work on her publication list is indexed: 147 distinct works (155 Scholar rows, 11 marked `dup_of`, plus 1 `D` and 2 `H` items).
- 104 works have an open full text: 77 were read in full and 23 in part (two of them MEng reports of students she supervised, read as the students' voice: S100 at chapter level, S117 as a supplement), 1 turned out unreadable (S116), and 3 carry abstract or metadata cards (her 315-page PhD thesis S092 and two one-page minlp.org problem statements, S150 and S151, whose texts the round-2 abstract batches found). 2 rows were skipped (talks).
- Cards written: 146 cards on 145 works in 28 batch files (`c01`–`c17`, `s01`–`s07`, the book-mode batches `b01` and `b02` for two long files, `a2-01`, `a2-02`); S138 has two cards, a wrong-text card and the abstract card that counts. None of them is book material (no `B` rows); the non-research rows among them are listed under [Coverage](#coverage), Notes.
- All 222 quotes were checked by `verify_card_quotes.py`: 222 exact, 0 NOT FOUND.
- The cards were distilled into `SKILL.md` on 2026-11-19, and the evidence was then moved to the ledger (T3.7).

For Samuel Burer:

- Every work on his publication list is indexed: 71 distinct works (70 Scholar rows, 2 marked `dup_of`, plus 1 `D` and 2 `H` items).
- 67 works have an open full text: 52 were read in full and 15 in part. None is left unreadable: the first file for the 2021 correction note S061 held the original article, and the note itself was read in full in round 3. No row was skipped.
- Cards written: 73 cards on 71 works in 16 batch files (`c01`–`c10`, `s01`–`s04`, `a2-01`, `c3-01`); S061 has three cards (wrong text, abstract, full). None of them is book material (no `B` rows); the non-research rows among them are listed under [Coverage](#coverage), Notes.
- All 138 quotes were checked by `verify_card_quotes.py`: 138 exact, 0 NOT FOUND.
- The cards were distilled into `SKILL.md` on 2026-10-10.

For Santanu S. Dey:

- Every work on his publication list is indexed: 156 distinct works (169 Scholar rows, 19 marked `dup_of`, plus 5 `D` and 1 `H` items).
- 123 works have an open full text: 93 were read in full and 30 in part; none is unreadable. Seven pairs of these rows are two versions of one work, so the 123 cards read in full or in part cover 116 distinct works (his 08, header and §1). 2 rows were skipped (talks).
- Cards written: 154 cards on 154 works in 32 batch files (`c01`–`c22`, `s01`–`s07`, `a2-01`, `a2-02`, `c3-01`), none of them book material (no `B` rows); the non-research rows among them are listed under [Coverage](#coverage), Notes.
- All 258 quotes were checked by `verify_card_quotes.py`: 258 exact, 0 NOT FOUND.
- The cards were distilled into `SKILL.md` on 2026-10-10.

For Ignacio E. Grossmann and Nikolaos V. Sahinidis (in progress, stage T3.2):

- Grossmann: 1312 distinct works indexed (1335 Scholar rows, 86 marked `dup_of`, plus 9 `D` and 54 `H` items); 442 have an open full text; 140 rows are skipped (talks); the other 1172 rows are unread, and no card is written.
- Sahinidis: 381 distinct works indexed (409 Scholar rows, 42 marked `dup_of`, plus 1 `D` and 13 `H` items); 28 have an open full text; 93 rows are skipped (92 talks and a patent); the other 288 rows are unread, and no card is written.
- Next for both, as `team_status.py` prints it: team-chase.js (T3.3), then `plan_reading_batches.py --out-dir <scratch>` (T3.4).

What changed in the skills:

| Skill | Core methods | Change from the deep reading |
|---|---|---|
| `ignacio-e-grossmann` | 6 | In progress (T3.2 full texts, 442 open; no paper cards): unchanged; the methods rest on research notes 01–06. |
| `sven-leyffer` | 7 | New **M7 · Certify the notion you claim: grade every method by it, print what is not certified**, promoted from 25 distinct cards of 1999–2026 (08 §4): the LPEC whose zero step is exactly B-stationarity becomes the subproblem [sven-leyffer card S042 p. 10], a local NLP answer is certified globally optimal by six LPs [sven-leyffer card S031 pp. 12–15], and competitors are graded post hoc by one certificate [sven-leyffer card S126 arXiv pp. 34, 40]. On review its stated side was narrowed to co-signed papers [sven-leyffer card S126 arXiv p. 3], post-hoc grading was marked as resting on one work, and his own 2017 essay, which calls reliable NLP solvers "the best approach for solving MPECs", was recorded as a contradiction [sven-leyffer card H004 p. 9]. The proposed heuristics H11 (keep the model separate from its discretization, coarse to fine) and H12 (one tiny computed example per technique) were folded into Heuristic 8 and the Stages table's drafting row (catalog W1), since the heuristic tier is capped at ten (08 §5). |
| `nikolaos-v-sahinidis` | 5 | In progress (T3.2 full texts, 28 open; no paper cards): unchanged; the methods rest on research notes 01–06. |
| `ruth-misener` | 5 | Unchanged count: eight clusters with three or more cards read in full or in part each failed at least one of the four checks, so nothing was promoted (08 §4). New **Heuristic 11 · Put an expensive component behind a cheap gate**, from eleven works read in full or in part, e.g. a necessary and a cheap sufficient dominance test, so that only passing cuts are generated [ruth-misener card S011 pp. 6–7] and a callback whose frequency is swept [ruth-misener card S005 pp. 5–8]; it resolves U2, the cheap-cuts-first rule her project page states, until then claimed but unverified. Heuristic 6 was folded into Heuristic 4, which now also asks for one negative result about one's own construction [ruth-misener card S046 pp. 12–13]; Heuristic 10 (make uncertainty explicit) got executable steps [ruth-misener card S045 pp. 9–10], and Workflow B step 4 (borrow from a neighbour) its practice and protocol (08 §5). |
| `samuel-burer` | 6 | New **M6 · Solve in the cheap nonconvex space, certify in the convex dual**, promoted from eight works of 2001–2006 and 2025 (08 §4): a certificate from the stationarity multipliers [samuel-burer card S014 preprint p. 8], a rank bound under which a stationary point with S ⪰ 0 is SDP-optimal [samuel-burer card S001 pp. 5, 7], an LMI certificate for the output of any Stiefel-manifold solver [samuel-burer card S048 arXiv pp. 5-7, 14]. The proposed heuristics H11 (add quadratic equations redundant in x that bind in the lift) and H12 (finite KKT branching with SDP node relaxations, 2008–2012) were not numbered on review: H11 is now Method 1 step 1 (catalog D7) [samuel-burer card S004 pp. 4-5, 14], H12 a dated Method 1 variant (catalog D8) [samuel-burer card S007 pp. 3, 8-9]; their evidence stays in the ledger (`#heuristic-11`, `#heuristic-12`). |
| `santanu-s-dey` | 6 | New **M6 · Exploit the re-solve: prove what carries over, reuse it, keep the certificate**, promoted from four works read in full, 2020–2026, from three coauthor groups (08 §4): a unique optimum stays optimal near the right-hand side [santanu-s-dey card S044 p. 18], finitely many useful split directions serve a whole instance family [santanu-s-dey card S082 pp. 6, 16–17], and the reuse is aimed at the dual bound [santanu-s-dey card S067 pp. 2, 40]. The former Heuristic 10 (design the cut first, verify later) became a Method 3 variant, and the new **Heuristic 10 · Re-prove the classical lemma you lean on by a route that exposes the one property you use, then push past the classical statement** took its number [santanu-s-dey card S071 pp. 3–4] [santanu-s-dey card D005 p. 8]; Heuristic 4 now covers reused tools as well as named obstacles [santanu-s-dey card S104 pp. 6, 22–29] (08 §5). |

Core-method counts are the `### Method N` sections of each `SKILL.md` on 2026-11-20; before the synthesis Leyffer had 6 and Misener, Burer and Dey 5 each (08 §4 of each).

The four deep-read skills gained the following files:

- `references/technique-catalog.md`: transferable devices from the papers (proof devices, design moves, experiment and evaluation protocols, writing moves; Burer's also a table of his known exactness results), each with card references.
- `references/research/07-paper-cards.md`: the card index, generated from the digests by `scripts/build_card_index.py` (`--check` passes for all four).
- `references/research/08-deep-reading-synthesis.md`: patterns, promotions and corrections.
- `references/research/09-evidence-ledger.md`: the full evidence behind each `SKILL.md` item (for Leyffer and Misener also the evidence moved out of `SKILL.md` when it was tightened). `SKILL.md` links to its anchors; `check_ledger.py` resolves every one.
- `references/research/10-claim-audit.md`: the sampled claim-to-card audit and its follow-up.
- `references/sources/papers/abstract-sources.json` (where each chased abstract came from) and, for Leyffer and Dey, `book-leads.json`.

Grossmann and Sahinidis have so far `works.json`, `scholar.md`, `papers/INDEX.md` and `abstracts.json`.

In `minlp-roundtable` (refreshed in the same T3.8 run and corrected after its review; its Honest Boundary keeps the dated record), no fault line was added or dropped: six is the maximum, and every side of Leyffer, Misener, Burer or Dey in them already cited paper cards from the team layer (FL3, Sahinidis ↔ Grossmann, has no side of theirs; its one card, Dey's S006, is cited in its common-ground sentence). The cited cards were re-read at their pages. Two fault lines gained five further cards read in full: FL4 (how much to pay for relaxation strength) on Burer's side, now resting on the box-QP branch-and-bound results [samuel-burer card S018 pp. 12–13] and on Chen and Burer's comparison with Couenne, losses included [samuel-burer card S008 p. 16], with the award note [samuel-burer card H001 p. 3] now giving only the lesson, and on Dey's side [santanu-s-dey card S067 pp. 2, 4–5, 36] (the journal version, read as arXiv v2; card D004, the IPCO 2024 record, holds the same file); FL5 (piecewise-linear pooling relaxations) on Misener's side [ruth-misener card S143 p. 13] [ruth-misener card S072 pp. 13–16, 19, 21]. FL2's hull-folklore sentence now also cites Misener's card S046, which FL2 already cited [ruth-misener card S046 p. 2], and takes the reference it names to Trespalacios and Grossmann from ignacio-e-grossmann note 05 §3.1; FL6 cites her S011 at pp. 16–20 and quotes Dey's concession more closely [santanu-s-dey card S011 p. 21]; FL1, FL3 and FL4 got wording and attribution fixes (FL3's common ground now credits Kocuk, Dey & Sun, FL4's cheaper intermediate relaxation Burer, Kim & Kojima). One sentence on Misener's side of FL5, on the 2016 *AIChE J.* pooling-detector paper, still rests on her abstract card S064 and on santanu-s-dey note 05 (see What is still missing). Its Team table adds Burer's and Dey's new Method 6 to their lens lines, and the member brief tells each member to cite the card ids its catalog and synthesis give. Grossmann's and Sahinidis's sides (FL1–FL4, FL6) still rest on their `SKILL.md` and research notes and stay marked "(card evidence pending for …)".

## Pipeline

As used: for Burer and Dey T3.1–T3.6 on 2026-10-10 (T3.7 not needed then); for Leyffer and Misener T3.1–T3.5 on 2026-10-10 and T3.6–T3.7 on 2026-11-19; T3.8 for these four on 2026-11-20; Grossmann and Sahinidis reached T3.2 on 2026-10-10; T4 has not been run. Each stage was committed per member, except that two checkpoint commits of 2026-10-10 hold work of several members: 8a06189 (Dey's T3.2, alongside the Grossmann and Sahinidis harvests, whose audits were then committed per member) and 59e2a86 (the paused T3.6 mining of Burer and Dey, Leyffer's two round-2 abstract batches and one of Misener's, Grossmann's T3.2 in progress and Sahinidis's stopped chase). How to launch each workflow and its arguments: `scripts/workflows/README.md`. Never commit PDFs, extracted text or `private/`.

1. **Publication list (T3.1, `team-harvest.js`).** Each `works.json` records its basis in `source_note` and an audit, in `works.json` (`audit`) or at the top of `scholar.md`:
   - Grossmann: "Google Scholar profile + DBLP + Crossref + arXiv + homepage (egon.cheme.cmu.edu publication list of July 2025 and paper server)"; per-record `sources` tags: scholar 1335, homepage 885, crossref 559, dblp 244, arxiv 16. Audit (`scholar.md`): an independent year-sorted pass over the 1335 profile rows matched every row; nothing was added.
   - Leyffer: "Google Scholar profile + DBLP + Crossref + homepage", DBLP read through sparql.dblp.org, the homepage list (wiki.mcs.anl.gov/leyffer, HTTP 503 on 2026-10-10) read from a Wayback Machine snapshot; tags: scholar 224, homepage 150, crossref 121, dblp 85, arxiv 39, datacite 4. Audit: the year-sorted re-fetch matched all 224 rows; all 125 DOIs resolve and match their Crossref or DataCite titles; all 39 arXiv links name Leyffer; all 92 DBLP records map to records.
   - Sahinidis: "Google Scholar profile + DBLP + Crossref + homepage (sahinidis.coe.gatech.edu research and software pages, and the CV of 7 October 2026 linked from its /nick page) + arXiv author listing"; tags: scholar 409, homepage 221, dblp 115, crossref 95, arxiv 14. Audit (`scholar.md`): all 409 rows matched; all 206 DOIs and 14 arXiv ids checked, all match.
   - Misener: Scholar (155 rows), DBLP through SPARQL, Crossref, her publication list and CV of 3 December 2025, plus links from Optimization Online and the Imperial Spiral repository API; tags: scholar 155, homepage 108, dblp 69, spiral 63, crossref 57, arxiv 51, optimization-online 9, pmlr 3, acmij 2, focapo-cpc-2017 2, tmlr 1. Audit: all rows matched; all 100 DOIs match their Crossref (98) or DataCite (2) titles; all 46 arXiv ids name Misener; all 93 DBLP records are linked.
   - Burer: Scholar, DBLP through SPARQL, Crossref, the CV linked from sburer.github.io (updated 2026-02-12) and the author PDFs under sburer.github.io/papers/, NSF award pages; tags: scholar 70, homepage 65, dblp 53, arxiv 16, crossref 13, nsf 2. Audit: all 70 rows matched; all 63 DOIs and 15 arXiv ids match; all 53 DBLP records and 62 CV entries map to records.
   - Dey: Scholar, DBLP through SPARQL, Crossref, an arXiv author search and title searches, his homepage list (117 entries) and one Optimization Online URL; tags: scholar 169, homepage 117, dblp 98, arxiv 74, crossref 18, optimization-online 1. Audit: all 169 rows matched; all 115 DOIs and 73 arXiv ids match; all 105 DBLP records and 117 homepage entries map to records.
   - `validate_works.py` (2026-11-20; records, `dup_of`, errors, warnings): Grossmann 1398 (S 1335 · D 9 · H 54), 86, 0, 491; Leyffer 240 (S 224 · D 2 · H 14), 29, 0, 30; Sahinidis 423 (S 409 · D 1 · H 13), 42, 0, 184; Misener 158 (S 155 · D 1 · H 2), 11, 0, 15; Burer 73 (S 70 · D 1 · H 2), 2, 0, 1; Dey 175 (S 169 · D 5 · H 1), 19, 0, 28. Most warnings are rows without a DOI, arXiv id or URL (445 of Grossmann's, 170 of Sahinidis's); the rest are near-duplicate titles or shared arXiv ids not linked by `dup_of`.
   - The outputs are `references/sources/publications/works.json` (all records, including duplicates marked `dup_of`) and `scholar.md` (the readable list and audit notes).
   - IDs (the letters `validate_works.py` accepts): `S` = Scholar row · `D` = bibliographic database only (DBLP, Crossref, …) · `H` = author homepage or CV only · `R` = report-series item not matched to a Scholar row · `X` = external document about the researcher (interview, oral history, memoir) · `B` = openly available part of a book (T4). This team used `D` and `H` beyond `S`, and no `R`, `X` or `B` items:
     - Grossmann: `D` 9 (six 2009 chapters, among them *Generalized Disjunctive Programming* and *Logic-Based Outer Approximation*; a 1992 book review; journal papers of 2014 and 2018), `H` 54 (items of his CMU publication list without a Scholar row: conference and journal papers, reports, chapters, course material and books such as three CACHE design case studies).
     - Leyffer: `D` 2 (D001 *The penalty interior-point method fails to converge*, 2005; D002, a 2013 conference paper), `H` 14 (the 2015 OPTIMA interview with Roger Fletcher, H005; his 2017 INFORMS Optimization Society newsletter article, H004; a 2014 SIAM essay on applying for funding, H006; seven SIAG/OPT Views-and-News issues he edited, H007–H013; a 2017 report, a 2020 preprint and two 2021 items).
     - Sahinidis: `D` 1 (a 2009 chapter), `H` 13 (from his group site and CV: four 1991 chapters, a 1996 book review, two prize announcements, a 2025 journal paper, a 2026 preprint and four more items).
     - Misener: `D` 1 (a 2016 conference paper found in Spiral), `H` 2 (ROmodel, 2021; a 2014 bioreactor paper).
     - Burer: `D` 1 (a 2017 editorial), `H` 2 (H001, the *COAP* 2009 best-paper award note; H002, the SDPLR 1.03-beta user's guide).
     - Dey: `D` 5 (four DBLP-only conference or journal records, D001–D004, and a 2026 arXiv preprint, D005), `H` 1 (an undated EV-charger location preprint).
2. **Open full texts (T3.2, `acquire_fulltexts.py`).** arXiv by id or title search, Unpaywall, then the author or repository links in `works.json`; the researcher's surname among an arXiv hit's authors and the title on a download's first pages are checked; the text is extracted with `[[page N]]` markers, with tesseract OCR for scans. INDEX.md's Source column at the stage commits: Grossmann 442 of 1312 (`url` 400, every one listing his CMU paper server egon.cheme.cmu.edu; `unpaywall` 25; `arXiv` 17); Sahinidis 28 of 381 (`arXiv` 16, `unpaywall` 10, `url` 2 from his group site); Leyffer 57 of 211 (`arXiv` 34, `unpaywall` 14, `url` 8, `manual` 1); Misener 61 of 147 (`arXiv` 47, `url` 7, `unpaywall` 7); Burer 67 of 71 (`url` 51, every one listing sburer.github.io; `arXiv` 16); Dey 113 of 156 (`arXiv` 77, `url` 33, `unpaywall` 3; recorded in a checkpoint commit). The results go into `references/sources/papers/INDEX.md` and `abstracts.json`.
3. **Chase (T3.3, `team-chase.js` → `merge_chase.py`).** Agents searched legitimate open sources for the works still `no-oa`, starting from the `chase_hints` in `team.json`. Which copy each `manual` file was saved from is not recorded in INDEX.md; the stage commits name the sources, and the hosts that `works.json` lists for the `manual` rows are given here. `manual` does not mark the chase's finds alone: after the merge most rows indexed at T3.2 read `manual` too (Leyffer's `arXiv` rows fell from 34 to 1, Dey's from 77 to 7), so the open-text counts before and after are the measure.
   - Leyffer: the commit names Wayback Machine copies of his Dundee and Argonne homepages (the 1993 thesis, the 1994 OA preprint, the 2001 SQP-B&B preprint, filter-SQP reports, the MINLP_BB and filterSQP manuals) and other open sources; open texts 57 → 162. His 161 `manual` rows list the Wayback Machine (100 rows), his Argonne wiki (57) and MCS pages (10), arXiv (35), OSTI (4), Optimization Online (3) and figshare (3), among others. `abstract-sources.json` names 19 abstract sources: the Wayback Machine 6, OSTI 5, Semantic Scholar 4, Springer 3, NSF 1.
   - Misener: the commit names author manuscripts from Imperial's Spiral repository (GloMIQO, ANTIGONE, APOGEE, the MIQCQP piecewise and edge-concave paper and others) and Wayback copies of publisher PDFs; 61 → 102. Her 44 `manual` rows list Spiral (28), Optimization Online (8), the Wayback Machine (3) and Dagstuhl's DROPS (2), among others. `abstract-sources.json`: 22 (OpenAlex 6, Semantic Scholar 4, AIChE meeting pages 4, the journal site acmij.az 2, six single sources).
   - Dey: the commit names Optimization Online preprints, a homepage manuscript and open Springer prefaces: 113 → 123 open texts and 12 abstracts. His 114 `manual` rows mostly list his Georgia Tech homepage (93) and arXiv (70). `abstract-sources.json`: 12 (Springer 6, NSF award records 3, Purdue e-Pubs 1, Semantic Scholar 1, an Argonne CEEESA project page 1).
   - Burer: no new legitimate full text; the commit records the 2001 thesis as restricted to Georgia Tech users and the 2017 editorial as behind a Cloudflare block. Two NSF award abstracts were added (`abstract-sources.json`: api.nsf.gov 2).
   - Sahinidis: the run stopped part-way; the checkpoint commit of 2026-10-10 notes "T3.3 chase stopped part-way (works.json urls)", and it was not resumed. Grossmann: not run.
   - Abstract batches of later rounds saved a few more open copies: Leyffer's S033 and S127, Misener's S092, S150 and S151, and the 2021 correction note S061 of Burer, which replaced a wrong file; Misener's wrong file for S138 was dropped. INDEX.md now reads: Leyffer 164 open texts, Misener 104, Burer 67, Dey 123; Grossmann and Sahinidis unchanged.
   - A report series matched by title can hold other authors' reports, so the author is checked on page 1, not just the title words. **Never shadow libraries, never paywall circumvention.**
4. **Reading batches (T3.4, `plan_reading_batches.py`).** It sets each row's Role and splits the papers into batches: **core** (full read, at most 5 papers or 110 pages), **supplement** (selective read, at most 8 papers or 220 pages), **book** (over 150 pages, read chapter by chapter, alone in its batch) and **abstract** (no full text, an abstract or metadata card only, 30 per batch). Batch IDs are `c01`, `s02`, … in round 1 and `a2-01`, `c3-01`, … later. As planned here (each 07's Batches table):
   - Leyffer: round 1, 20 core batches (`c01`–`c20`, 61 cards) and 14 supplement batches (`s01`–`s14`, 101 cards); round 2, two abstract batches (`a2-01`, `a2-02`, 42 cards).
   - Misener: round 1, 17 core (`c01`–`c17`, 52 cards), 7 supplement (`s01`–`s07`, 48 cards) and two book-mode batches for long files (`b01`: the 174-page TOGO 2010 proceedings, S152, of which only her four-page extended abstract with Floudas was read; `b02`: the 166-page MEng report S100); round 2, two abstract batches (`a2-01`, `a2-02`, 44 cards).
   - Burer: round 1, 10 core (`c01`–`c10`, 38 cards) and 4 supplement (`s01`–`s04`, 29 cards); round 2, one abstract batch (`a2-01`, 5 cards); round 3, one core batch for the correction note S061 (`c3-01`).
   - Dey: round 1, 22 core (`c01`–`c22`, 73 cards) and 7 supplement (`s01`–`s07`, 49 cards); round 2, two abstract batches (`a2-01`, `a2-02`, 31 cards); round 3, one core batch for the 2016 OPF paper with Kocuk and Sun, S006 (`c3-01`).
   - Whether a round was fixed by hand with `--round N --exclude` is not recorded.
5. **Cards (T3.5, `team-read.js`).** One agent per batch wrote `references/research/cards/<batch>.md` and `<batch>.digest.json` with the brief below; `07-paper-cards.md` indexes every card. Read levels in the digests: Leyffer full 120, partial 35, abstract 22, metadata 21, unreadable 6; Misener full 77, partial 23, abstract 27, metadata 17, unreadable 2 (one of them S138's superseded wrong-text card); Burer full 52, partial 15, abstract 3, metadata 2, unreadable 1 (S061's superseded cards account for one abstract and the unreadable entry); Dey full 93, partial 30, abstract 15, metadata 16.
6. **Quote check.** `scripts/verify_card_quotes.py` (2026-11-20): Leyffer 329 quotes, 323 exact and 6 after normalisation; Misener 222, Burer 138 and Dey 258, all exact; 0 NOT FOUND for each.
7. **Read column.** `scripts/mark_read_from_cards.py` filled INDEX.md's Read column from each work's best card: Leyffer carded 120, skimmed 35, abstract 22, metadata 21, unreadable 6, `—` 7 (the talks, Role `skip`); Misener carded 77, skimmed 23, abstract 27, metadata 17, unreadable 1, `—` 2 (talks); Burer carded 52, skimmed 15, abstract 2, metadata 2; Dey carded 93, skimmed 30, abstract 15, metadata 16, `—` 2 (talks).
8. **Synthesis (T3.6, `team-synthesize.js`).** One agent mined the cards into `08-deep-reading-synthesis.md`; a conservative edit of `SKILL.md` wrote `09-evidence-ledger.md` at the same time; read-only skeptics reviewed it, and the confirmed findings were fixed (Leyffer 41 of 43 findings fixed, Misener 49 of 51, as their stage commits record). Promotions and heuristic changes: see the table under Status. Each member's claim audit (`scripts/audit_claims.py`, protocol `references/claim-audit.md`) gave a zero-context auditor 20 page-cited claims of `SKILL.md`: Leyffer 18 supported and 2 partial, Misener 18 and 2 (both 2026-11-19); Burer 15 and 5, Dey 17 and 3 (both 2026-10-10); 0 unsupported for each. Each partial was narrowed in `SKILL.md` or left it with the tightening, as each audit's follow-up records.
9. **Tighten (T3.7, `team-tighten.js`).** Leyffer (12613 → 11658 words) and Misener (12030 → 11508) on 2026-11-19, each proved lossless by `check_ledger.py --before` the pre-tighten copy, without `--allow`; `team_status.py` now reports 11736 and 11596 words. Not run for Burer and Dey (see Status).
10. **Integrate (T3.8, `team-integrate.js`, 2026-11-20).** The team README, this file and the roundtable's fault lines were refreshed from the members' 08 syntheses and paper cards; the coverage table below comes from `team_status.py --coverage` and the README's five-column summary from `--coverage --short`; `scripts/check_links.py` checks every link.

### Commands, per researcher

Run these from the repository root. On Windows set `PYTHONUTF8=1` for every Python script. Needs network access to arxiv.org, api.unpaywall.org and api.crossref.org, plus `pypdfium2` and Pillow; `tesseract` (OCR) and `ps2pdf` (PostScript reports) are needed for older papers. Set `OMP_THREAD_LIMIT=1` when several OCR runs share the machine.

```bash
T=product/minlp-team
R=<member-slug>                      # each member's "slug" in $T/team.json
S=${TMPDIR:-/tmp}/minlp-team-scratch; mkdir -p "$S"   # the workflows' scratch: plan JSON and backups stay outside the repo
D=<YYYY-MM-DD>                       # the date passed to the workflow run

python3 scripts/team_status.py $T    # where every member stands

# T3.1 after team-harvest.js: check the publication list
python3 scripts/validate_works.py $T/$R
# T3.2 open full texts + INDEX.md (PDFs and txt/ stay local; INDEX.md and abstracts.json are committed)
python3 scripts/acquire_fulltexts.py $T/$R
# T3.3 after team-chase.js: merge its output and re-run the acquisition
python3 scripts/merge_chase.py $T/$R
# T3.4 roles + reading batches, one round per wave of new full texts; --out-dir writes $S/batches-<slug>-r<N>.json
#    (what team-read.js reads with round: N), picks N itself and excludes the other rounds' plans in $S;
#    to fix the round by hand: --round N --exclude "$S/batches-$R-r1.json,…" (plans still being read)
python3 scripts/plan_reading_batches.py $T/$R --out-dir "$S" --no-abstract
python3 scripts/plan_reading_batches.py $T/$R --out-dir "$S"          # last round: abstract/metadata batches
# T3.5 after team-read.js: check every quote, fill the Read column, regenerate 07-paper-cards.md
python3 scripts/verify_card_quotes.py $T/$R
python3 scripts/mark_read_from_cards.py $T/$R
python3 scripts/build_card_index.py $T/$R
# T3.6 after team-synthesize.js: quality gate, ledger anchors, card citations
python3 scripts/quality_check.py $T/$R/SKILL.md
python3 scripts/check_ledger.py $T/$R
python3 scripts/check_citations.py $T --member $R
# T3.7 after team-tighten.js (it saves the pre-tighten copy itself): prove the move to the ledger lossless
python3 scripts/check_ledger.py $T/$R --before "$S/$R-SKILL.before-tighten-$D.md"
#    scratch lost? every stage is committed: git show <pre-tighten commit>:$T/$R/SKILL.md > "$S/$R-SKILL.before-tighten-$D.md"
# T4 after team-increment.js: the T3.5 checks again
# T3.8 team level, after team-integrate.js
python3 scripts/team_status.py $T --coverage           # paste into Coverage below, unchanged
python3 scripts/team_status.py $T --coverage --short   # the five-column summary for the team README's Honest Boundary, unchanged
python3 scripts/check_links.py $T
python3 scripts/check_citations.py $T --roundtable
python3 scripts/team_check.py $T                       # delivery gate
```

Workflows in `scripts/workflows/`: `team-harvest.js` (T3.1), `team-chase.js` (T3.3), `team-read.js` (T3.5), `team-synthesize.js` (T3.6), `team-tighten.js` (T3.7), `team-integrate.js` (T3.8), `team-increment.js` (T4).

## Coverage

These counts are exact and were computed from each researcher's `references/sources/papers/INDEX.md` by `python3 scripts/team_status.py product/minlp-team --coverage` on 2026-11-20. Paste its output here; never edit a number by hand.

| Researcher | Scholar rows | Distinct works indexed | Open full text | Read in full | Read in part | Abstract only | Metadata only (incl. unreadable) | Skipped (not the author's / non-research) | Book material carded | Quotes verified |
|---|---|---|---|---|---|---|---|---|---|---|
| Ignacio E. Grossmann | 1335 | 1312 | 442 | 0 | 0 | 0 | 0 | 140 | 0 | 0 |
| Sven Leyffer | 224 | 211 | 164 | 120 | 35 | 22 | 27 | 7 | 0 | 329 |
| Nikolaos V. Sahinidis | 409 | 381 | 28 | 0 | 0 | 0 | 0 | 93 | 0 | 0 |
| Ruth Misener | 155 | 147 | 104 | 77 | 23 | 27 | 18 | 2 | 0 | 222 |
| Samuel Burer | 70 | 71 | 67 | 52 | 15 | 2 | 2 | 0 | 0 | 138 |
| Santanu S. Dey | 169 | 156 | 123 | 93 | 30 | 15 | 16 | 2 | 0 | 258 |
| **Total** | 2362 | 2278 | 928 | 342 | 103 | 66 | 63 | 244 | 0 | 947 |

⚠️ 1460 indexed works have no card yet (Read column empty); the table is not final.

Notes:

- The warning line counts the rows of Grossmann (1172) and Sahinidis (288) that are neither carded nor skipped (their unread rows, Status above; `team_status.py`'s Unread rows column), 1460 in all, not their 1693 indexed works: their deep reading is in progress, so their rows show the publication list, the open texts found and the skipped rows, and zeros for everything read. The rows of Leyffer, Misener, Burer and Dey are final.
- *Distinct works indexed* = Scholar rows minus duplicates, plus items found only in DBLP or on a homepage: Grossmann 1335 − 86 + 9 + 54 = 1312; Leyffer 224 − 29 + 2 + 14 = 211; Sahinidis 409 − 42 + 1 + 13 = 381; Misener 155 − 11 + 1 + 2 = 147; Burer 70 − 2 + 1 + 2 = 71; Dey 169 − 19 + 5 + 1 = 156. Every member has a Google Scholar profile. Special items counted here, each read in the voice it is written in: Leyffer's 2015 OPTIMA interview of Roger Fletcher (H005: Leyffer asks the questions, the answers are Fletcher's voice [sven-leyffer card H005 pp. 1–6]), his 2017 newsletter article (H004), seven SIAG/OPT Views-and-News issues he edited (H007–H013, where only the editor's notes are his voice) and four committee or community reports read in full, which his 08 §1 lists as "Committee or community voices, not his" (S025, a DOE ASCAC subcommittee report that acknowledges him as a contributor; S133, a DOE workshop report; S163, the GDR ROD prospective report, of which he co-wrote one section; S193, a workshop recorder summary with him as recorder; the same list names the guest editor's note S148, an abstract card); Misener's two single-author essays read in full, the 2016 *SIAG/OPT Views and News* memorial essay on Floudas (S143, her voice about him) and a 2014 CPSE newsletter piece (S145), and the MEng reports of two students she supervised (S100, S117: the students' voice); Dey's three guest editorials (S094, S113, S115: the guest editors' joint voice) and, in the file of his 2009 *Optima* survey with Tramontani (S079), the "Comments on Multi-Row Cuts" column, pp. 8–10, in Cornuéjols, Weismantel and Wolsey's voice (his 08 §1); Burer's *COAP* 2009 best-paper award note (H001, unsigned; its card reads it as the awardees' own retrospective because it switches to the first person [samuel-burer card H001 p. 3]) and the SDPLR 1.03-beta user's guide (H002). No memoir or oral history is indexed (no `X` items).
- *Metadata only (incl. unreadable)*: Leyffer 21 metadata and 6 unreadable; Misener 17 and 1; Burer 2 and 0; Dey 16 and 0. Some metadata rows are not research works but carry a metadata card instead of Role `skip`: Leyffer's junk or masthead rows (S050, S197, S209, S210, S212, S219, S221; his 08 §1), Dey's two rows of a different S. Dey (S144, S145) and his proceedings front matter (his 08 §1).
- *Read in part* means the supplement reading: abstract, introduction, method or algorithm, main result, experimental setup and conclusion. Misener's S100 and S117, MEng reports of two students she supervised, are counted here too (S100 read at chapter level, S117 as a supplement). For a multi-author volume the count follows the reading of the researcher's own section: Misener's S152, the 174-page TOGO 2010 proceedings, counts under *Read in full*, because her four-page extended abstract with Floudas was read in full and the rest of the volume only at the level of its preface and contents (card S152).
- *Open full text* counts the INDEX.md rows with an extracted text (`Full text = txt`). An open copy found after the chase but not yet saved is not counted: Misener's S064 ([What is still missing](#what-is-still-missing)).
- *Book material carded* counts the `B` rows in INDEX.md: openly available parts of a book (table of contents, errata, addendum, preface, published reviews). None yet: no T4 increment has been run.
- *Skipped* rows have Role `skip` in INDEX.md and no card: Leyffer's 7, Misener's 2, Dey's 2 and Grossmann's 140 are talks; Sahinidis's 93 are 92 talks and a patent.
- Page references on cards are pages of the text version that was read, often a technical report or preprint (each 08 §1 lists them). Check the journal page before citing one in a paper.

## Reading-batch brief (as used, shortened)

The full brief lives in `scripts/workflows/team-read.js` (last changed 2026-10-09, before these cards were written); this is the record.

```
You are deep-reading research works by {name} to deepen the research-craft skill at {skill}/.
Read first: references/paper-reading-card.md (card format) and SKILL.md's methods, heuristics and taste sections.
Batch {bid} (mode core | supplement | book | abstract): the work list is that batch in the plan JSON (ids, pages, txt paths).
core → the whole work, full card D1–D8; supplement → abstract, introduction, method, assumptions and main result,
setup, conclusion, short card; book → chapter level plus a chapter map; abstract → abstract or metadata card, say which.
Follow a work's "note" (what it is, whose voice): a review is the reviewer's voice; a table of contents is title-only.
Check page 1 first: title and the member's surname among the authors, else "unreadable" + WRONG-TEXT; garbled → REOCR.
Write cards/{bid}.md (batch intent, focus dimensions, material roles, file-to-printed page mapping, one card per work)
and cards/{bid}.digest.json (one object per work: read_level, D1–D8 lines, method_links, quotes, …).
Rules: a page reference on every claim; at most two verbatim quotes per card, with page, that must pass
verify_card_quotes.py; "not read" rather than guess; link cards to Method N as evidence, variant or contradiction.
No WebSearch in reading batches; abstract batches may use Crossref, arXiv, Semantic Scholar and open publisher
pages and save an open PDF for the next round; never shadow libraries or paywall circumvention.
Never read references/sources/private/. Edit no file other than the batch's own outputs.
```

## What is still missing

- **Works with no open full text found** have abstract or metadata cards only. Abstract only + Metadata only in the Coverage table: Leyffer 49 of 211 (22 + 27: 40 with no open text found, plus 9 with a text on disk, namely the 6 unreadable files, S033 and S127, not read yet, and the participant list S210), Misener 45 of 147 (27 + 18: 41 with no open text found, S064 among them although an open copy exists (below), plus 4 with a text on disk, namely the unreadable S116 and, not read yet, the PhD thesis S092 and the problem statements S150 and S151), Burer 4 of 71 (2 + 2) and Dey 31 of 156 (15 + 16), all with no open text found: 129 in all (66 + 63 in the Total row). Their evidence carries less weight in the syntheses. Grossmann (870 of 1312 works with no open text found) and Sahinidis (353 of 381) are in progress: none of their works has a card yet. The biggest gaps, from each 08's "Open gaps" (§11):
  - Leyffer: six unreadable files, five of them filter and MPEC theory papers (below); no open text for the IMA volume edited with Lee (S004), the MacMPEC page (S030), the 2000 filter-SQP report (S132), the methods-and-software report with Mahajan (S035), the 2009 NSF award (S196) and the 2025 bilevel classification paper (S166); the numerics of the 1994 OA paper are unread, because the 1996 preprint read for it has none (S003); the FilMINT preprint lacks its per-instance appendix (S015); Minotaur, the McCormick, funnel, Uno and MPECopt papers were read as reports or arXiv versions; for most 2013–2026 team papers the cards cannot separate his contribution.
  - Misener: abstract only for the 2009–2012 pooling, gas-lift and crude-oil papers (S007, S008, S016, S018, S022, S027), GloMIQO 2 (S026), the αBB generalisation (S036) and the 2016 pooling-detector paper behind Method 1 step 7 (S064, and the three-page AIChE meeting paper of the same title, D001). S064 does have an open copy, which the chase missed: its published version under a CC BY 4.0 licence in Imperial's Spiral repository (http://hdl.handle.net/10044/1/32968, a link already in her `works.json`; record checked on 2026-11-20), and santanu-s-dey note 05 §2.5 quotes it from an open Spiral copy; it is to be saved and carded (How to extend, step 5). The 315-page PhD thesis (S092) and two one-page minlp.org problem statements (S150, S151) have a text on disk but only abstract or metadata cards; metadata only for 17 works, among them the GloMIQO 2.2 test-suite report (S102); no text states why she left C++ solver development or why the detection line stopped at detection.
  - Burer: no open text for the 2001 thesis (S070), the NSF CAREER and collaborative awards (S068, S069) and the 2017 editorial (D001); the published versions of S012, S016, S019, S048, S049 and S058 were not read, nor v1 and v2 of the submodular paper (S058), which according to the web research carry its polynomial-time claim and the narrowing; no card between 2007 and 2024 applies Method 6, and whether unread works of that window do is unknown.
  - Dey: no open text for the PhD thesis (S074), the IPCO 2008 lifting paper (S015), the group-theoretic survey chapter (S030), the 2010 two-row experiments (S038) and others, so the 2007–2009 origins of Method 3 and of the multi-row programme rest on abstracts and on the 2009 survey [santanu-s-dey card S079 pp. 2–8]; 30 works were read only in part, among them the proofs of several 2010–2013 closure and lifting papers; three of the four Method 6 works are preprints; his own voice (talks, interviews) is not in the card corpus.
  - Grossmann and Sahinidis: the whole publication list is still to be carded (stage T3.2).
- **Book bodies** are rarely open, so no book chapter is read unless it is; none was read here, and no T4 increment has been run:
  - Leyffer: the IMA volume *Mixed Integer Nonlinear Programming* (2012, edited with J. Lee; S004) has an abstract card. `book-leads.json` logs the publisher's free front matter (IMA foreword, editors' preface, table of contents; 18 pages) and back matter (the workshop's list of participants); not carded yet.
  - Dey: two proceedings volumes listed as book rows, ISCO 2022 (S114) and IPCO 2026 (S127), have metadata cards (proceedings front matter, his 08 §1). `book-leads.json` logs their free front matter (prefaces, tables of contents) and landing pages; not carded yet.
  - Misener and Burer have no book rows. Misener's two book-mode batches read a proceedings volume and a student's report, not books of hers.
  - Grossmann (in progress): 12 book rows, none with an open text, among them *Systematic methods for chemical process design* (S001), *Advanced optimization for process systems engineering* (S270), *Chemical engineering optimization models with GAMS* (S617) and three CACHE design case studies (H048–H050).
  - Sahinidis (in progress): his book with Tawarmalani, *Convexification and Global Optimization in Continuous and Mixed-Integer Nonlinear Programming* (S005), has no open text.
- **Uneven periods.** Open full text / no open text per decade (INDEX.md, skip rows left out):
  - Leyffer: 1990s 10/0; 2000s 36/8; 2010s 58/19; 2020s 56/5; undated 4/7; plus the 1971 junk row S050, without a text.
  - Misener: 2000s 0/5; 2010s 54/28; 2020s 50/8. Her 2009 papers are known from abstracts and metadata only.
  - Burer: 2000s 25/3; 2010s 29/1; 2020s 13/0.
  - Dey: 2000s 3/4; 2010s 55/12; 2020s 63/7; undated 2/8. His work before 2010 is thin in full text (his 08 §1).
  - Grossmann (in progress): 1970s 0/5; 1980s 0/84; 1990s 2/161; 2000s 81/161; 2010s 225/195; 2020s 124/62; undated 10/62. No work before 1990 has an open text in his index, the 1986 outer-approximation paper with Duran (S002) among them.
  - Sahinidis (in progress): 1980s 0/3; 1990s 0/39; 2000s 0/69; 2010s 15/84; 2020s 13/57; undated 0/8. No work before 2010 has an open text in his index.
- **Unreadable files** are listed on their cards:
  - `sven-leyffer`: S005 (`c03`), S024 (`c04`), S017 (`c05`), S008 (`c06`), S109 (`s01`), S038 (`s02`): broken font layers (S017's legible page is only a repository cover sheet); each needs OCR and a re-read. Two more texts on disk, saved by the round-2 abstract batches, are not read yet: S033 and S127.
  - `ruth-misener`: S116 (`s07`): the extracted file holds section headings and equation fragments only; it needs OCR or a new extraction. S138's card in `s04` read the wrong text (the arXiv preprint of the journal paper S069); that file was dropped, and its abstract card in `a2-02` counts.
  - `samuel-burer`: none left: S061's card in `c07` read the wrong text (the original article S019), and the correction note was then read in full in `c3-01`.
  - `santanu-s-dey`: none.
- **The roundtable** cites no paper card for Grossmann or Sahinidis yet: their sides of the fault lines rest on their `SKILL.md` and research notes until their cards exist. Two citations on the other members' sides still lean on research notes: FL5's sentence on Misener's 2016 *AIChE J.* paper (S064, an abstract card; santanu-s-dey note 05 §2.5 and §4.1 quote its open full text), and FL2's reference to Trespalacios and Grossmann (2015) among the results behind the hull folklore, which the P-split card S046 does not record (ignacio-e-grossmann note 05 §3.1 identifies it as the paper's reference [66]); a later pass on Misener's folder can add both to her cards.

### How to extend

1. **Get a legitimate copy.** Sources are a library, publisher access or the author.
2. **Name the file like the index.** Use `<ID>-<year>-<first eight title words, lowercased, hyphenated>.pdf`, the stem `acquire_fulltexts.py` uses (the ID is the one in INDEX.md).
3. **Put it in `<researcher>/references/sources/papers/`.** This folder's PDFs and `txt/` are git-ignored. Check by hand that the file is the paper, because the title check only runs on downloads.
4. **Re-run the acquire script.** `python3 scripts/acquire_fulltexts.py product/minlp-team/<researcher> --only <ID>` extracts the text, OCRs scans, and sets `Full text = txt` and `Source = manual`. For a card marked unreadable because of a garbled text layer (REOCR) use `--reocr <ID>`; for a wrong file (WRONG-TEXT) `--drop <ID>`. Run it in the checkout that holds the other papers' PDFs and `txt/`: rows without local files keep their committed status, but their quotes cannot be re-verified.
5. **Card and fold it in.** Either run `team-increment.js` (T4; see `scripts/workflows/README.md`), which cards the new material, folds it into the skill, verifies and fixes; or by hand: plan a new round with `python3 scripts/plan_reading_batches.py product/minlp-team/<researcher> --out-dir <scratch> --no-abstract` (it picks the next round and skips works already read in full or in part or carded unreadable; add `--reread <ID>` for a work re-OCR'd after an unreadable card, or `--round N --exclude <plan files still being read>` to fix the round by hand), read with the brief above, run `verify_card_quotes.py` and `mark_read_from_cards.py`, regenerate `07-paper-cards.md` with `python3 scripts/build_card_index.py <member folder>`, and apply the conservative-update rules to `SKILL.md`, `09-evidence-ledger.md` and `technique-catalog.md`. Leyffer's S033 and S127 and Misener's S092, S150 and S151 already have texts on disk, so a next round plans them without any flag. Leyffer's next round also plans S210, the NAOV-2020 participant list, which has a text on disk; pass `--skip-ids S210` (or set its Role to `skip` in INDEX.md) to leave it out. Misener's S064 has no text on disk yet: save its open copy (Spiral, http://hdl.handle.net/10044/1/32968) as `S064-2016-using-functional-programming-to-recognize-named-structure-in.pdf` and run `python3 scripts/acquire_fulltexts.py product/minlp-team/ruth-misener --only S064` (steps 2–4); the next round then plans it too.
6. **Refresh the numbers.** Re-run `python3 scripts/team_status.py product/minlp-team --coverage` and paste it unchanged into the Coverage table here; paste the output of `python3 scripts/team_status.py product/minlp-team --coverage --short` unchanged over the five-column summary in the team README (or run `team-integrate.js`, which does both).
7. **Finish Grossmann and Sahinidis.** Continue their stages: `team-chase.js` (T3.3) and `merge_chase.py`, `plan_reading_batches.py` (T3.4), `team-read.js` (T3.5), `team-synthesize.js` (T3.6), `team-tighten.js` if a skill ends over the word budget (T3.7), then `team-integrate.js` (T3.8) for the team.

## Privacy and integrity

- Private materials stay in each member's `references/sources/private/` (git-ignored; only its README is tracked) and are never read into public files. The deep reading works only from public sources.
- PDFs and extracted text (`papers/*.pdf`, `papers/txt/`) are git-ignored for copyright reasons by the repository's `.gitignore`, and `git ls-files product/minlp-team` lists none. Only indexes, abstracts, cards and syntheses are committed.
- Full texts come only from legitimate open copies: arXiv, Unpaywall, author pages (live or as Wayback Machine captures), institutional repositories and report series (Imperial's Spiral, Argonne and OSTI reports) and open publisher pages.
- The integrity rules in each skill still apply. No claim goes in without a page reference, and no quote is invented: every quote on a card passes `scripts/verify_card_quotes.py`. Nothing written by a coauthor, reviewer, interviewer or newsletter author is attributed to a member: the cards read Fletcher's answers in Leyffer's interview as Fletcher's, the articles in the newsletter issues Leyffer edited as their authors', the committee and community reports Leyffer contributed to as the committees' voice, the discussion column filed with Dey's 2009 *Optima* survey as its authors' (Cornuéjols, Weismantel and Wolsey), the MEng reports of Misener's students as the students', and Dey's editorials as the guest editors' joint voice.

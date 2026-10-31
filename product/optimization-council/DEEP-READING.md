# Deep reading · Optimization Council

This is the record of how the skill of Dimitris Bertsimas, the council's lead and its one own member, was deepened. His publications were read in full or in part wherever an open copy exists, and not just as search snippets. Cards and syntheses are written in English. The four guest delegations are deepened in their own teams, and their records are kept there: [LP Team](../lp-team/DEEP-READING.md), [NLP Team](../nonlinear-team/DEEP-READING.md), [DFO Team](../dfo-team/DEEP-READING.md) and [MINLP Team](../minlp-team/DEEP-READING.md). The LP and MINLP records are still unfilled templates that read "Not started", although four MINLP members already have cards; `python3 scripts/team_status.py product/minlp-team` shows where each stands.

## Status (2026-10-31)

**Complete.** The numbers below come from `python3 scripts/team_status.py product/optimization-council` (with `--coverage`), `validate_works.py`, `verify_card_quotes.py` and `check_ledger.py`, all run on 2026-10-31. Stage contents that no script prints come from the stage commits, the card digests, `papers/INDEX.md`, `08-deep-reading-synthesis.md` and `10-claim-audit.md`. Progress at any time: `python3 scripts/team_status.py product/optimization-council`.

| Stage | Workflow / script | Done |
|-------|-------------------|------|
| T3.1 Publication list | `team-harvest.js` → `validate_works.py` | ☑ 2026-10-28: 965 records (932 Scholar rows `S`, 22 DBLP or Crossref records `D`, 11 homepage or CV items `H`), 186 marked `dup_of`; T3.2 and T3.3 linked 28 more version duplicates (214 `dup_of`), leaving 751 distinct research works. With the 21 `B` rows of T4, `validate_works.py` reports 986 records, 0 errors and 245 warnings (228 non-duplicate rows without DOI, arXiv id or URL; 12 groups of near-duplicate titles not linked by `dup_of`; 5 `dup_of` chains) |
| T3.2 Open full texts | `acquire_fulltexts.py` | ☑ 2026-10-29: 283 of the 765 works then distinct (INDEX.md Source at the stage commit: `url` 139, every one listing his MIT paper archive among its `works.json` URLs; `arXiv` 124; `unpaywall` 20); 301 abstracts |
| T3.3 Chase open copies and abstracts | `team-chase.js` → `merge_chase.py` | ☑ 2026-10-29: 172 more full texts (`manual`), 455 of 751 in all, and 42 abstracts; 14 more version duplicates linked. The round-3 abstract batches saved 18 more open texts and 25 more abstracts: 473 open texts (`manual` 190) and 67 entries in `abstract-sources.json` |
| T3.4 Reading batches | `plan_reading_batches.py` (one run per round) | ☑ four rounds: 42 core and 21 supplement batches (round 1); 9 core and 18 supplement batches plus the 1988 PhD thesis read chapter by chapter (`b2-01`, round 2); 5 abstract batches, 138 works (round 3); 3 supplement batches for the 18 texts found in round 3 (round 4). T4 added round 5 |
| T3.5 Cards | `team-read.js` → `verify_card_quotes.py` → `mark_read_from_cards.py` | ☑ rounds 1–4: 611 card entries in 99 batch files (279, 176, 138 and 18 by round); 1,083 quotes, 1,080 exact and 3 after spacing and symbol normalisation, 0 not found; Read column 413 carded, 59 skimmed, 63 abstract, 57 metadata, 159 not read (skipped rows) |
| T3.6 Synthesis | `team-synthesize.js` → `quality_check.py` | ☑ 2026-10-29: Method 7 promoted and Heuristic 10 added, corrections C1–C21, `09-evidence-ledger.md` and `technique-catalog.md`; `quality_check.py` 12/12 on 2026-10-31 |
| T3.7 Tighten | `team-tighten.js` → `check_ledger.py` | ☑ 2026-10-29: `SKILL.md` 12,342 → 11,661 words as `team_status.py` counts them (the stage commit records 12,174 → 11,400), long evidence moved verbatim to the ledger. The T4 increment, the claim-audit fixes and the Domain Map have since brought it to 13,153 words, over the 13,000-word default budget. A status trim on 2026-10-31 moved the corrections list (C1–C22 with their cards) and the claimed-but-unverified and web-pass bullets verbatim into the ledger (`#corrections-list`, `#claimed-unverified`); `SKILL.md` keeps one gist per correction and is now 12,881 words, and `team_status.py` no longer asks for T3.7. `check_ledger.py --before` passes and resolves all 52 ledger anchor references |
| T3.8 Integrate | `team-integrate.js` → `team_status.py --coverage` → `check_links.py` | ☑ 2026-10-31: this file and the council README (coverage tables pasted from `team_status.py`), the roundtable's fault lines from the cards, `check_links.py` |
| T4 Increments | `team-increment.js` (open parts of books, new papers) | ☑ one, **books-2026-10-29**: 21 book-material items (B001–B021) in round 5 (5 batch files, `c5-01`–`c5-05`), all read in full, 42 quotes, all exact; correction C22 |
| Council layer: domain tags | domain-tag workflow → `references/domains/work-domains.json` | ☑ 2026-10-28: every then-distinct work tagged with the `team.json` domain codes by two independent taggers, a judge ruling where their primary codes disagreed (61 works, stage commit); 800 tags today (779 works plus B001–B021, tagged by inheritance on 2026-10-29) |
| Council layer: domain files and Domain Map | `references/domains/*.md`; `SKILL.md` § Domain Map | ☑ nine domain files on 2026-10-29, one per code, each written from the domain pack and the cards and checked by two lenses (271 findings, 270 applied, stage commit); the Domain Map in `SKILL.md` on 2026-10-31 |
| Claim audits | `audit_claims.py` → `10-claim-audit.md` | ☑ two zero-context auditors per audit, 0 unsupported in each. `SKILL.md`: a sample of 40 (A 30 supported and 10 partial; B 32 and 8) and a census of all 318 page-cited claims (A 260 and 58; B 253 and 65; of the 67 flagged, 63 fixed and 4 left as written); technique catalog, 20 (A 17 and 3; B 16 and 4); domain files, 108 of 2,459 (A 87 supported, 10 partial, 11 uncheckable; B 89, 8, 11; 12 fixed, 10 left), and the 11 claims citing other members' cards re-checked against those cards, 11 of 11 supported by both |
| Council session | session workflows run by the moderator from its scratch folder (not part of the kit) → [`first-session-2026-10-31.md`](first-session-2026-10-31.md) | ☑ 2026-10-31, in agenda mode on autopilot to checkpoint 4. Topic and items: Bertsimas framed *the price of exactness* as four items on FL1, FL2, FL4 and FL5, with 10 delegates from the four teams. Agents: 36 in the first run; 29 in the challengers' round (the first run had left the challengers' turns out) and plan v2; 29 in the citation census. Plan v2 sign-offs: 6, two of them on conditions v2 does not yet meet; 5 dissents. Checks: the first verification checked 40 citations; the second checked 661 items and found 27 problems; the census checked all 271 first-run citations (236 supported, 33 annotated) and corrected 3 first-verification readings. Fix at the source: the roundtable's FL2 citation of Nocedal's S043 p. 7 was narrowed. Nothing was run: the plan designs the deciding tests |

For Dimitris Bertsimas:

- Every work on his publication list is indexed: 751 distinct research works in `papers/INDEX.md`, one row per distinct research work (932 Google Scholar rows, 207 of them duplicates, plus 15 works found only in DBLP or Crossref and 11 found only on his homepage or CV), plus 21 book-material rows (B001–B021), counted apart.
- 473 works have an open full text; 413 were read in full and 59 in part, and the last one sits on a skipped row (S807, 1996). No open file turned out to be unreadable: no card has read level `unreadable`. 160 rows were skipped (Role `skip`): by INDEX.md's Kind column, 84 theses (not his own; his 1988 thesis is read), 46 "other" rows, 15 reports, 6 talks, 4 patents, 4 reviews and 1 errata. None has a card except S771, a 2010 workshop page carded at metadata level and then judged not his.
- Cards written: 632 cards on 613 items in 104 batch files. Research works: 611 cards on 592 works in 99 files (`c01`–`c42` and `s01`–`s21`; `c2-01`–`c2-09`, `s2-01`–`s2-18` and `b2-01`; `a3-01`–`a3-05`; `s4-01`–`s4-03`); by the deepest card, 413 works at full, 59 at partial, 63 at abstract and 57 at metadata level (S771 among them). 19 works have two cards: 18 carded from the abstract in round 3 and read in full or in part in round 4, and S181, read in part in round 1 and in full in round 2. Book material: 21 cards on 21 items in 5 files (`c5-01`–`c5-05`). Every research work in scope has at least one card.
- All 1,125 verbatim quotes on the cards were checked against the extracted text or abstract by `verify_card_quotes.py`: 1,122 exact, 3 after spacing and symbol normalisation (on the round-1 cards of S101 and S051, accepted at T3.6), 0 NOT FOUND. 42 of them are on the book-material cards, all exact.
- The openly available book material was read and carded (T4, increment books-2026-10-29):
  - *Introduction to Linear Optimization* (with Tsitsiklis, Athena Scientific 1997): the preface as the publisher serves it (B001), the Athena Scientific and Dynamic Ideas pages with review excerpts (B002), the errata sheet last updated 7/5/2021 (B003), the printed title page and contents (B004), and M. V. Ramana's review in *Optima* 54 (B005);
  - *Optimization over Integers* (with Weismantel, 2005): the publisher's page (B006) and the printed contents (B007);
  - *Data, Models, and Decisions* (with Freund; South-Western 2000, 2nd ed. Dynamic Ideas 2004): the 2004 publisher's page (B014), the 2000 printed contents (B015) and an unsigned review on GraduateTutor.com (B016);
  - *The Analytics Edge* (with O'Hair and Pulleyblank, 2016): the publisher's page (B017) and the printed contents (B018);
  - *Machine Learning under a Modern Optimization Lens* (with Dunn, 2019): the publisher's page with the book's six principles (B009) and Thibaut Cuvelier's review (developpez.com, 2020, in French; B010);
  - *Robust and Adaptive Optimization* (with den Hertog, 2022): the publisher's page (B011) and Cuvelier's review (2022, in French; B012);
  - *Queueing Theory: Classical and Modern Methods* (with Gamarnik, 2022): the publisher's page (B013);
  - *The Analytics Edge in Healthcare* (with Orfanoudaki and Wiberg, 2025): the publisher's page and the authors' book site (B019);
  - for all eight, his own books pages of 2026 and 2017 (B008); and two items that are not books: the 1992 printing of the simulated-annealing review with Tsitsiklis, chapter 2 of the National Research Council report *Probability and Algorithms* (B020, the same text as S005), and the Fall 2009 course description and syllabus of his MIT course 15.093J (B021).

  The book bodies are not open and were not read. `08-deep-reading-synthesis.md` records the increment in its section "Increment books-2026-10-29", and `09-evidence-ledger.md` has a `#books` anchor.
- The cards were then distilled into `SKILL.md` through `08-deep-reading-synthesis.md` and `09-evidence-ledger.md`, and partitioned by optimization domain into the nine files of `references/domains/`, which the Domain Map in `SKILL.md` indexes.

What changed in the skills:

| Skill | Core methods | Change from the deep reading |
|---|---|---|
| `dimitris-bertsimas` | 7 | New **M7 · Bound before policy**, promoted from the full texts (79 distinct works read in full or in part, 1988–2026; it passes exclusivity only as a cross-domain transfer, 08 §4). New **Heuristic 10 · Re-derive the field's classical results with a new device first** (80 works; exclusivity fails, so it is a heuristic, 08 §5). Corrections C1–C21 (synthesis) and C22 (books increment) are marked in place (`SKILL.md`, "Corrections from the full texts"). Considered and not promoted (08 §4): the exact problem a working heuristic solves (Heuristic 1, upgraded), the matched duel (evidence for Method 4), the price of simplicity (a Method 3 variant) and asymptotic regimes (a Method 7 variant); the book material promoted nothing (08, I.9). The council layer added the Domain Map and the nine domain files, whose §6 sections set his record beside each guest member's, and his Roundtable Card's "Likely disagreements" name all 23 guest members. |

Core-method count: the `### Method N` sections of `SKILL.md` on 2026-10-31 (6 before the synthesis, 08 §4).

The skill also gained the following files:

- `references/technique-catalog.md`: transferable devices from the papers, each with card references.
- `references/research/08-deep-reading-synthesis.md`: patterns, promotions and corrections.
- `references/research/09-evidence-ledger.md`: the full evidence, moved out of `SKILL.md` when it was tightened. `SKILL.md` links to its anchors.
- `references/research/10-claim-audit.md`: the sampled and census claim-to-card audits and their fixes.
- `references/domains/`: the nine domain files and `work-domains.json`, the domain tag of every indexed work and book item.

In `council-roundtable`, the fault lines were written in this integration step from cards on both sides: Bertsimas's side from his paper cards, each guest's side from that member's own cards, which resolve in the guest's own team folder (a citation such as `[frank-e-curtis card S047 p. 2]` is card S047 in `product/nonlinear-team/frank-e-curtis/references/research/cards/`), and guests without cards through their skills or research notes, cited in prose. A fault line is called an exchange in print only where a card shows one side's paper citing or answering the other's, and pages are cited only for cards read in full or in part. Three carded exchanges that criticise the lead (Günlük, Kalagnanam, Li, Menickelly and Scheinberg on optimal classification trees; Cho, Burer and Campbell on the budget model for the interval TSP; Xu and Burer on moment-based sets) are kept in the domain files' §6 rather than among the six numbered fault lines, and the roundtable's Step 3 and Honest Boundary name them. Where the lead's side rests on a co-authored paper and the card gives his place in the author list, the fault line says so (FL1, FL5, FL6).

## Pipeline

Run every stage per member (one workflow per member, in parallel: a workflow runs at most min(16, CPUs − 2) agents at once). How to launch each workflow and its arguments: `scripts/workflows/README.md`. Commit after every stage; the session container is ephemeral. Never commit PDFs, extracted text or `private/`.

1. **Publication list (T3.1, `team-harvest.js`).** The researcher's Google Scholar profile is read page by page with a fetch tool (WebFetch), because Scholar has no API and blocks `curl`. The list is cross-checked with DBLP through its SPARQL endpoint (`scripts/dblp_works.py`; the DBLP REST API sits behind a bot wall), Crossref for DOIs, and DataCite/arXiv; an independent audit sorted by date catches missed rows. `scripts/validate_works.py` checks the result.
   - The outputs are `references/sources/publications/works.json` (all records, including duplicates marked `dup_of`) and `scholar.md` (the readable list and audit notes).
   - IDs (the letters `validate_works.py` accepts): `S` = Scholar row · `D` = bibliographic database only (DBLP, Crossref, …) · `H` = author homepage or CV only · `R` = report-series item not matched to a Scholar row · `X` = external document about the researcher (interview, oral history, memoir) · `B` = openly available part of a book (T4). Any other letter must be passed to `validate_works.py --extra-id-letters`. In this council's `works.json`: `S` 932 rows (207 marked `dup_of`); `D` 22 records (7 marked `dup_of`, so 15 works found only in DBLP or Crossref); `H` 11 items from his homepage or CV (H001–H011); `B` 21 items (B001–B021, added in T4). No `R` or `X` items: the 2014 MIT Sloan oral history is a source of the research notes (`sources/talks/`), not an indexed work.
2. **Open full texts (T3.2).** `scripts/acquire_fulltexts.py` tries, in order: arXiv (by ID or by title search on arxiv.org/search), Unpaywall open-access copies, and author or repository links listed in `works.json`. It requires the researcher's surname among an arXiv hit's authors, checks that each download is a PDF whose first pages carry the title, extracts the text with `[[page N]]` markers, and falls back to tesseract OCR for scans and garbled font layers. The results go into `references/sources/papers/INDEX.md` and `abstracts.json`.
3. **Chase (T3.3, `team-chase.js`).** For works still `no-oa`, agents search legitimate open sources for full texts and abstracts, starting from the `chase_hints` in `team.json`. Which copy each `manual` file was saved from is not recorded in INDEX.md; the URLs added to `works.json` for those 190 rows after T3.2 (by the chase and by the round-3 batches) point to his homepage publication list's Dropbox copies (121 rows), MIT DSpace (17), Optimization Online (7), PubMed Central's open-access data (5), the Internet Archive (4: two MIT working papers archived from DSpace, a coauthor's Columbia page and an ICIS paper in the AIS eLibrary), JMLR (3), his MIT paper archive, medRxiv, NASA NTRS, open-access Springer and Nature articles, Cynthia Rudin's Duke page and PMLR (2 each, one PMLR file through its GitHub repository), and single files from Florin Avram's page at Pau, MIT Lincoln Laboratory, the MLHC and MTNS proceedings, the MIT Initiative on the Digital Economy, arXiv and Climate Change AI; for 12 rows no URL was added. The 139 `url` rows of T3.2 all list his MIT paper archive. The 67 chased abstracts (`abstract-sources.json`) came from his homepage's Dropbox copies (8), NSF award records (7), the pages of his press Dynamic Ideas (7), MIT DSpace (7), OpenAlex (5), PubMed (4), Semantic Scholar and Springer (3 each), OSTI, arXiv and Optimization Online (2 each) and 17 single sources. A report series matched by title can hold other authors' reports, so the author is checked on page 1, not just the title words. `scripts/merge_chase.py` merges their output into `abstracts.json` and re-runs the acquisition, which records `Source = manual` for files saved by hand. **Never shadow libraries, never paywall circumvention.**
4. **Reading batches (T3.4).** `scripts/plan_reading_batches.py` sets each row's Role and splits the papers into batches:
   - **core**: full read, at most 5 papers or 110 pages per batch;
   - **supplement**: selective read, at most 8 papers or 220 pages;
   - **book**: over 150 pages, read chapter by chapter, alone in its batch;
   - **abstract**: no full text, so an abstract or metadata card only, 30 per batch.

   It runs in rounds as new full texts turn up; with `--out-dir <scratch>` it picks the next round number itself and excludes the other rounds' plan files it finds there (including rounds still being read). The last round emits the abstract batches. Batch IDs are `c01`, `s02`, … in round 1 and `c2-01`, `a2-03`, … in later rounds; `team-increment.js` (T4) continues the rounds (e.g. `c5-01`). A batch named by hand says what it holds in its header line.
5. **Cards (T3.5, `team-read.js`).** One agent per batch writes `references/research/cards/<batch>.md` and `<batch>.digest.json` using the brief below. `07-paper-cards.md` indexes every card.
6. **Quote check.** `scripts/verify_card_quotes.py` looks up every quoted passage (`quotes[].text` in the digests) in the extracted text or abstract, normalising ligatures, hyphenation, quote marks and whitespace. Every NOT FOUND is fixed before synthesis.
7. **Read column.** `scripts/mark_read_from_cards.py` fills INDEX.md's Read column from each card's `read_level`: `full` → `carded`, `partial` → `skimmed`, `abstract` → `abstract`, `metadata` → `metadata`, `unreadable` → `unreadable`.
8. **Synthesis (T3.6, `team-synthesize.js`).** Per researcher, with the conservative-update rules of `references/paper-reading-card.md` §3:
   1. One agent mines the cards into `08-deep-reading-synthesis.md`.
   2. A conservative edit of `SKILL.md` follows, within a word budget stated up front, writing `09-evidence-ledger.md` at the same time. Existing methods get evidence first. A new core method needs 3 or more distinct papers plus the four checks.
   3. Read-only skeptics review the edit adversarially.
   4. The verified objections are fixed, and `quality_check.py` is re-run.
9. **Tighten (T3.7, `team-tighten.js`, only for skills still over the word budget).** Long evidence moves from `SKILL.md` to `09-evidence-ledger.md` without loss; `scripts/check_ledger.py --before <scratch>/<slug>-SKILL.before-tighten-<date>.md` (the pre-tighten copy, no `--allow`) proves every card id, page reference and quote survives, the front matter and rule sections are unchanged, and every ledger anchor resolves. After the synthesis alone, `scripts/check_ledger.py` without `--before` checks the ledger anchors; the synthesis reviewers compare with the pre-synthesis copy using `--allow frontmatter,activation-disclaimer`, the parts a synthesis changes by design.
10. **Integrate (T3.8, `team-integrate.js`).** The team README, this file and the roundtable's fault lines are refreshed from the members' 08 syntheses; the coverage table here comes from `scripts/team_status.py --coverage` and the README's five-column summary from `--coverage --short`; `scripts/check_links.py` checks every link.

### Commands, per researcher

Run these from the repository root. Needs network access to arxiv.org, api.unpaywall.org and api.crossref.org, plus `pypdfium2` and Pillow; `tesseract` (OCR) and `ps2pdf` (PostScript reports) are needed for older papers. Set `OMP_THREAD_LIMIT=1` when several OCR runs share the machine.

```bash
T=product/optimization-council
R=dimitris-bertsimas                 # the council's own member ("slug" in $T/team.json); guests are deepened in their own teams
S=${TMPDIR:-/tmp}/optimization-council-scratch; mkdir -p "$S"   # the workflows' scratch: plan JSON and backups stay outside the repo
D=<YYYY-MM-DD>                       # the date passed to the workflow run

python3 scripts/team_status.py $T    # where every member stands

# T3.1 after team-harvest.js: check the publication list
python3 scripts/validate_works.py $T/$R

# T3.2 open full texts + INDEX.md (PDFs and txt/ stay local; INDEX.md and abstracts.json are committed)
python3 scripts/acquire_fulltexts.py $T/$R

# T3.3 after team-chase.js: merge its output and re-run the acquisition
python3 scripts/merge_chase.py $T/$R

# T3.4 roles + reading batches; one round per wave of new full texts. Writes $S/batches-<slug>-r<N>.json (what team-read.js
#    reads with round: N), picks N itself and excludes the other rounds' plans in $S; prints N per member
python3 scripts/plan_reading_batches.py $T --out-dir "$S" --no-abstract
#    ... once it prints "no full-text batches left" for a member, a last round without --no-abstract gives the remaining works abstract/metadata batches
python3 scripts/plan_reading_batches.py $T/$R --out-dir "$S"

# T3.5 after team-read.js: check every quote, then fill the Read column (no unread rows after the last round)
python3 scripts/verify_card_quotes.py $T/$R
python3 scripts/mark_read_from_cards.py $T/$R

# T3.6 after team-synthesize.js: quality gate and ledger anchors
python3 scripts/quality_check.py $T/$R/SKILL.md
python3 scripts/check_ledger.py $T/$R
# T3.7 after team-tighten.js (it saves the pre-tighten copy itself): prove the move to the ledger lossless
python3 scripts/check_ledger.py $T/$R --before "$S/$R-SKILL.before-tighten-$D.md"
#    scratch lost? every stage is committed: git show <pre-tighten commit>:$T/$R/SKILL.md > "$S/$R-SKILL.before-tighten-$D.md"

# T3.8 team level
python3 scripts/team_status.py $T --coverage           # paste into Coverage below, unchanged
python3 scripts/team_status.py $T --coverage --short   # the five-column summary for the team README's Honest Boundary, unchanged
python3 scripts/check_links.py $T
```

## Coverage

These counts are exact and were computed from each researcher's `references/sources/papers/INDEX.md` by `python3 scripts/team_status.py product/optimization-council --coverage`. Paste its output here; never edit a number by hand.

| Researcher | Scholar rows | Distinct works indexed | Open full text | Read in full | Read in part | Abstract only | Metadata only (incl. unreadable) | Skipped (not the author's / non-research) | Book material carded | Quotes verified |
|---|---|---|---|---|---|---|---|---|---|---|
| Dimitris Bertsimas | 932 | 751 | 473 | 413 | 59 | 63 | 56 | 160 | 21 | 1125 |
| **Total** | 932 | 751 | 473 | 413 | 59 | 63 | 56 | 160 | 21 | 1125 |

Notes:

- *Distinct works indexed* = Scholar rows minus duplicates, plus items found only in DBLP or on a homepage. A member without a Google Scholar profile has 0 Scholar rows; that member's list comes from DBLP and the homepage. Bertsimas has a Scholar profile (`prKmkzMAAAAJ`): 932 rows minus 207 duplicates, plus 15 DBLP- or Crossref-only and 11 homepage-only works, give the 751. No special item is counted: the 2014 MIT Sloan oral history, read in full for the research notes, is not an indexed work.
- *Open full text* counts the 473 rows with an open text, S807 on a skipped row among them; read in full and in part cover the other 472.
- *Read in part* means the supplement reading: abstract, introduction, method or algorithm, main result, experimental setup and conclusion. For a multi-author volume it means only the researcher's own section.
- *Metadata only* is 56, not the 57 works with a metadata-level card: S771, a 2010 workshop page that is not his, is counted under *Skipped*.
- *Book material carded* counts the `B` rows in INDEX.md: openly available parts of a book (table of contents, errata, addendum, preface, published reviews). They are not counted in the research-work columns. Bertsimas's 21 include his own books pages, the 1992 printing of a review chapter and a 2009 course syllabus.
- *Skipped* rows have Role `skip` in INDEX.md and no card (S771 apart, see *Metadata only*). They are rows that are not the researcher's work (referee lists, misattributed rows, unresolved fragments), plus patents, talks and conference duplicates of journal papers. For Bertsimas, 84 of the 160 are theses, described in 08 §1 as students' theses; Status above gives the rest by kind. The Coverage section of each skill's `08-deep-reading-synthesis.md` counts them.
- Page references on cards are pages of the text version that was read, often a technical report or preprint. Check the journal page before citing one in a paper.

## Reading-batch brief (as used, shortened)

The full brief lives in `scripts/workflows/team-read.js`; this is the record.

```
You are deepening the research-craft skill at product/optimization-council/{R}/ by reading full texts.
Read first: references/paper-reading-card.md (card format, roles, rules) and {R}/SKILL.md
(methods, heuristics, taste marks, workflows — you link cards to their numbers).
Batch {bid} ({core | supplement | book | abstract}): {papers from the plan JSON: ID, year, title, venue,
role, pages, txt path}. Texts are in references/sources/papers/txt/, abstracts in abstracts.json.
Write references/research/cards/{bid}.md in English. Open it with: batch intent (one line), focus dimensions
(D1–D8), material roles, and how file pages map to printed pages. Then one card per paper:
  core → every dimension from the whole text; supplement → abstract, introduction, method, main result,
  experimental setup, conclusion; book → chapter level; abstract → from the abstract, or metadata only — say which.
Write references/research/cards/{bid}.digest.json: one object per card (fields: see paper-reading-card.md §四).
Rules: a page reference ([[page N]] markers) on every claim; at most two quotes per card, verbatim, with page —
they must pass scripts/verify_card_quotes.py; write "not read" rather than guess; say when the researcher's role
is unclear (middle author, team paper); link each card to Method N / heuristic as evidence, variant or contradiction;
note new-pattern candidates. Never read references/sources/private/. Do not edit SKILL.md, INDEX.md or other
batches — synthesis is a separate step.
Report: cards written, method links, new-pattern candidates, papers you could not read and why.
```

## What is still missing

- **Works with no open full text** have abstract or metadata cards only: 119 in scope, all Bertsimas's (Abstract only 63 + Metadata only 56 in the Coverage table). Their evidence carries less weight in the syntheses. They include the eight books and S550, a Scholar "book" row whose only match found is Jack Dunn's 2018 MIT thesis of the same title (unverified); the 2026 robust-optimization retrospective with den Hertog (S614); part of the 1992–1999 achievable-region series; early adaptive-RO and robustness–regularization papers; the clinical validations of the trauma and emergency-surgery calculators; and editorials and special issues (08 §11).
- **Book bodies** are rarely open, so no book chapter was read. For each of the eight books, what was read is listed under Status above (the 1997 preface in its web form, publisher pages, printed contents, the 1997 book's errata sheet, reviews). Refused or not found, and logged as leads: the PDF of *The Analytics Edge in Healthcare*, sent only after a request form (name, e-mail, institution and a no-redistribution pledge) that was not used; the PDF of *Probability and Algorithms*, behind a login or a guest form, so its chapter 2 was read in the publisher's read-online text instead (B020); the printed prefaces, among them the Dantzig quotation that opens the preface of *Robust and Adaptive Optimization*; J. Bard's 2000 review of the 1997 book beyond the publisher's excerpt, and Ye's 1998 review; the queueing and health books beyond their structure, aims and chapter list; and the lecture notes, readings, assignments and exams of the 2009 course, of which only the course page and syllabus were read (08, I.12; `book-leads.json`).
- **Uneven periods.** Open copies are scarcer before 2013: 164 of the 222 in-scope works dated 1985–2012 have an open text, against 298 of the 350 dated 2013–2026, and 10 of the 19 undated ones (INDEX.md; S470, an arXiv 1812 preprint whose index year reads 1812, counted in 2018–2022). By period, open over all in scope: 1985–92 22/31, 1993–97 35/48, 1998–2002 34/46, 2003–07 36/49, 2008–12 37/48, 2013–17 53/58, 2018–22 130/157, 2023–26 115/135. The early stochastic and dynamic programme is still read in depth (the 1988 thesis, a priori optimization, dynamic vehicle routing, the achievable region; 08 §1); what stays closed there includes part of the achievable-region series (08 §11).
- **Unreadable files** are listed on their cards: none. No card in the digests has read level `unreadable`.

### How to extend

1. **Get a legitimate copy.** Sources are a library, publisher access or the author.
2. **Name the file like the index.** Use `<ID>-<year>-<first eight title words, lowercased, hyphenated>.pdf`, the stem `acquire_fulltexts.py` uses.
3. **Put it in `<researcher>/references/sources/papers/`.** This folder is git-ignored. Check by hand that the file is the paper, because the title check only runs on downloads.
4. **Re-run the acquire script.** Use `python3 scripts/acquire_fulltexts.py product/optimization-council/<researcher> --only <ID>`. It extracts the text, OCRs scans, and sets `Full text = txt` and `Source = manual`. Run it in the checkout that holds the other papers' PDFs and `txt/`: rows without local files keep their committed status, but their quotes cannot be re-verified.
5. **Card and fold it in.** Either run `team-increment.js` (T4; see `scripts/workflows/README.md`), which cards the new material, folds it into the skill, verifies and fixes; or by hand: plan a new round with `plan_reading_batches.py <member folder> --out-dir <scratch> --no-abstract` (it picks the next round and skips works that already have cards), read with the brief above, run `verify_card_quotes.py` and `mark_read_from_cards.py`, regenerate `07-paper-cards.md` from the digests with `python3 scripts/build_card_index.py <member folder>`, and apply the conservative-update rules to `SKILL.md`, `09-evidence-ledger.md` and `technique-catalog.md`.
6. **Refresh the numbers.** Re-run `python3 scripts/team_status.py product/optimization-council --coverage` and paste it unchanged into the Coverage table here; paste the output of `python3 scripts/team_status.py product/optimization-council --coverage --short` unchanged over the five-column summary in the team README (or run `team-integrate.js`, which does both).

## Privacy and integrity

- Private materials stay in each member's `references/sources/private/` (git-ignored) and are never read into public files. The deep reading works only from public sources.
- PDFs and extracted text are git-ignored for copyright reasons. Only indexes, abstracts, cards and syntheses are committed.
- Full texts come only from legitimate open copies: arXiv, Unpaywall, author pages, institutional report series and open repositories.
- The integrity rules in each skill still apply. No claim goes in without a page reference, and no quote is invented: every quote on a card passes `scripts/verify_card_quotes.py`.

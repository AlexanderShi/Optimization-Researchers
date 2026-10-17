# Deep reading · Nonlinear Team

This is the record of the deep reading in this team. It is a mixed-tier team: only `frank-e-curtis` was deepened, by reading his publications in full or in part wherever an open copy exists, not just as search snippets. The other ten members (Jorge Nocedal, Stephen J. Wright, Yinyu Ye, Andreas Wächter, Philip E. Gill, Philippe L. Toint, Nicholas I. M. Gould, Roger Fletcher, Yurii Nesterov, and Daniel P. Robinson, who joined on 2026-10-17) are kept at the base tier on purpose, with no deep reading planned (see [The other ten members](#the-other-ten-members-base-tier-no-deep-reading)). Cards and syntheses are written in English.

## Status (2026-10-10)

**Complete for Frank E. Curtis. Base tier, no deep reading, for the other ten members** (Daniel P. Robinson joined on 2026-10-17; the Coverage table below was re-run that day). The numbers below come from `python3 scripts/team_status.py product/nonlinear-team` (with `--coverage`) and `python3 scripts/verify_card_quotes.py product/nonlinear-team/frank-e-curtis`, both run on 2026-10-10.

| Stage | Workflow / script | Frank E. Curtis |
|-------|-------------------|------|
| T3.1 Publication list | `team-harvest.js` → `validate_works.py` | ☑ 100 records (S 96 · D 3 · H 1), 4 marked `dup_of`, 0 errors, 1 warning (S084 has no DOI, arXiv id or URL) |
| T3.2 Open full texts | `acquire_fulltexts.py` | ☑ |
| T3.3 Chase open copies and abstracts | `team-chase.js` → `merge_chase.py` | ☑ |
| T3.4 Reading batches | `plan_reading_batches.py` (one run per round) | ☑ two rounds: 30 core batches, then 1 abstract batch |
| T3.5 Cards | `team-read.js` → `verify_card_quotes.py` → `mark_read_from_cards.py` | ☑ |
| T3.6 Synthesis | `team-synthesize.js` → `quality_check.py` | ☑ |
| T3.7 Tighten | `team-tighten.js` → `check_ledger.py` | not needed: `team_status.py` reports `SKILL.md` at 11398 words, under its 13000-word default budget; `check_ledger.py` resolves all 35 ledger anchor references |
| T3.8 Integrate | `team-integrate.js` → `team_status.py --coverage` → `check_links.py` | ☑ 2026-10-10 |
| T4 Increments | `team-increment.js` (open parts of books, new papers) | not run: book leads are logged in `book-leads.json` (see [What is still missing](#what-is-still-missing)) |

For Frank E. Curtis:

- Every work on his publication list is indexed: 96 distinct works in `papers/INDEX.md`, one row per distinct research work.
- 87 works have an open full text; 86 were read in full and none in part. One open file turned out to be unreadable (S086, see below). No row was skipped.
- Cards written: 96 cards on 96 items in 31 batch files (`c01`–`c30` and `a2-01`), all research works, no book material. Of these, 8 are abstract-level and 1 is metadata only (batch `a2-01`).
- All 180 verbatim quotes on the cards were checked against the extracted text or abstract by `verify_card_quotes.py`: 180 exact, 0 NOT FOUND.
- No openly available book material was carded (no T4 increment was run).
- The cards were then distilled into `SKILL.md` through `08-deep-reading-synthesis.md` and `09-evidence-ledger.md`.

What changed in the skills:

| Skill | Core methods | Change from the deep reading |
|---|---|---|
| `frank-e-curtis` | 5 | Unchanged count. A proposed **M6 · Guard the incumbent; let the guarantee sleep** (21 distinct full cards) was kept a heuristic on review because exclusivity fails at team level (Wright, Fletcher, Toint and Wächter share the move); it now extends Heuristic 5 as the guarded-incumbent construction. New **Heuristic 11 · Port the property, not the formula**; Heuristic 1 gains a theory–code-gap clause; corrections C1–C12 are marked in place (table: `09-evidence-ledger.md#corrections`); the Roundtable Card lens adds "guard the fast incumbent instead of replacing it". Source: `08-deep-reading-synthesis.md` §§4–5 and its review outcome. |
| `jorge-nocedal` | 6 | Base tier, no deep reading: unchanged. |
| `stephen-j-wright` | 6 | Base tier, no deep reading: unchanged. |
| `yinyu-ye` | 5 | Base tier, no deep reading: unchanged. |
| `andreas-wachter` | 6 | Base tier, no deep reading: unchanged. |
| `philip-e-gill` | 6 | Base tier, no deep reading: unchanged. |
| `philippe-l-toint` | 4 | Base tier, no deep reading: unchanged. |
| `nicholas-i-m-gould` | 6 | Base tier, no deep reading: unchanged. |
| `roger-fletcher` | 6 | Base tier, no deep reading: unchanged. |
| `yurii-nesterov` | 6 | Base tier, no deep reading: unchanged. |

Core-method counts are the `### Method N` sections of each `SKILL.md` on 2026-10-10.

The Curtis skill also gained the following files:

- `references/technique-catalog.md`: transferable devices from the papers (proof devices, algorithm-design moves, experiment and evaluation protocols, writing moves), each with card references.
- `references/research/07-paper-cards.md`: the card index, generated from the digests.
- `references/research/08-deep-reading-synthesis.md`: patterns, promotions and corrections.
- `references/research/09-evidence-ledger.md`: the full evidence behind each `SKILL.md` item. `SKILL.md` links to its anchors.
- `references/sources/publications/works.json` and `scholar.md` (the audited publication list) and `references/sources/papers/INDEX.md`, `abstracts.json`, `abstract-sources.json`, `book-leads.json`.

In `nonlinear-roundtable`, the three fault lines that seat Curtis (1 · Infeasibility: a separate restoration phase or one algorithm; 3 · Worst-case complexity as a design guide; 5 · The inner solve: factorize, truncate or replace) cite Curtis's side with card evidence, `[frank-e-curtis card S0xx pp. …]`; the other members' sides keep their base-tier evidence (a passage in that member's notes or `SKILL.md` plus the paper it rests on). Fault lines 2, 4 and 6 do not involve Curtis and are unchanged.

## Pipeline

As used for `frank-e-curtis` on 2026-10-10. How to launch each workflow and its arguments: `scripts/workflows/README.md`. Never commit PDFs, extracted text or `private/`.

1. **Publication list (T3.1, `team-harvest.js`).** `works.json` records its basis as "Google Scholar profile + DBLP + Crossref (+ homepage); arXiv ids also filled from the arxiv.org author listing (searchtype=author)", harvested and audited 2026-10-10. Per-record `sources` tags: scholar 96, homepage 88, dblp 73, arxiv 54, crossref 15. The audit note: "independent year-sorted Scholar pass (96 rows, all matched); 20 DOIs and 10 arXiv ids spot-checked, none wrong". `scripts/validate_works.py` passes with 0 errors.
   - IDs beyond `S` (Scholar row) used in this team, all in `frank-e-curtis`: `D` = bibliographic database only, 3 items (D001 *Adaptive Stochastic Optimization*, 2020, DBLP + arXiv; D002 *Single-Loop Deterministic and Stochastic Interior-Point Algorithms…*, 2024, DBLP + homepage + arXiv; D003, marked `dup_of` S050); `H` = author homepage only, 1 item (H001 *An Inexact Regularized Newton Framework…*, 2019, homepage + Crossref + arXiv). Three Scholar rows are duplicates (S080 → S003, S085 → S057, S095 → S040), so 96 Scholar rows give 96 distinct works.
2. **Open full texts (T3.2, `acquire_fulltexts.py`).** arXiv by id or title search, Unpaywall, then the author or repository links in `works.json`; title check on the first pages; text extracted with `[[page N]]` markers. One run recorded in the scratch log stopped on a Windows console encoding error (a title character the cp1252 console could not print); set `PYTHONUTF8=1` on Windows.
3. **Chase (T3.3, `team-chase.js` → `merge_chase.py`).** INDEX.md's Source column now reads: `manual` 57, `url` 16, `arXiv` 14, none 9 (the 9 `no-oa` rows). The 57 `manual` rows are the files saved during the chase; the merge run reported "57 new full texts". Which copy each was saved from is not recorded in INDEX.md; the URLs `works.json` lists for those rows point to arXiv (39 rows), Curtis's Lehigh COR@L homepage (18 rows), MERL technical reports (S071, S077) and open-access Springer article PDFs (S063, S073). Abstracts for works without open text came from Semantic Scholar (S031), Springer landing pages (S055, S079), OpenAlex (S078) and, for the 2025 book S074, a retailer's copy of the publisher's description (`abstract-sources.json`). **No shadow libraries, no paywall circumvention.**
4. **Reading batches (T3.4, `plan_reading_batches.py`).** Round 1: 96 rows, 87 full texts in 30 core batches (`c01`–`c30`, 1–4 papers each), no supplement or book batches, 0 skipped. Round 2: the 9 works without open text in one abstract batch (`a2-01`).
5. **Cards (T3.5, `team-read.js`).** One agent per batch wrote `references/research/cards/<batch>.md` and `<batch>.digest.json` with the brief below; `07-paper-cards.md` indexes every card.
6. **Quote check.** `scripts/verify_card_quotes.py`: 180 quotes, 180 exact, 0 NOT FOUND.
7. **Read column.** `scripts/mark_read_from_cards.py` filled INDEX.md's Read column: carded 86, abstract 8, metadata 1, unreadable 1; no unread rows.
8. **Synthesis (T3.6, `team-synthesize.js`).** One agent mined the cards into `08-deep-reading-synthesis.md`; a conservative edit of `SKILL.md` wrote `09-evidence-ledger.md` at the same time; read-only skeptics reviewed it, and the proposed Method 6 was kept a heuristic as a result (see the table above).
9. **Tighten (T3.7, `team-tighten.js`).** Not run: the skill is under the word budget.
10. **Integrate (T3.8, `team-integrate.js`).** The team README, this file and the roundtable's Curtis fault lines were refreshed from the 08 synthesis; the coverage table below comes from `team_status.py --coverage` and the README's five-column summary from `--coverage --short`; `scripts/check_links.py` checks every link.

### Commands, per researcher

Run these from the repository root. On Windows set `PYTHONUTF8=1` for every Python script.

```bash
T=product/nonlinear-team
R=frank-e-curtis                     # each deepened member's "slug" in $T/team.json
S=${TMPDIR:-/tmp}/nonlinear-team-scratch; mkdir -p "$S"   # plan JSON and backups stay outside the repo

python3 scripts/team_status.py $T    # where every member stands

# T3.1 after team-harvest.js
python3 scripts/validate_works.py $T/$R
# T3.2 open full texts + INDEX.md
python3 scripts/acquire_fulltexts.py $T/$R
# T3.3 after team-chase.js
python3 scripts/merge_chase.py $T/$R
# T3.4 reading batches, one round per wave of new full texts (add --round N --exclude <other plan files> to fix the round by hand)
python3 scripts/plan_reading_batches.py $T/$R --out-dir "$S" --no-abstract
python3 scripts/plan_reading_batches.py $T/$R --out-dir "$S"          # last round: abstract/metadata batches
# T3.5 after team-read.js
python3 scripts/verify_card_quotes.py $T/$R
python3 scripts/mark_read_from_cards.py $T/$R
# T3.6 after team-synthesize.js (T3.7 team-tighten.js only if SKILL.md is over budget)
python3 scripts/quality_check.py $T/$R/SKILL.md
python3 scripts/check_ledger.py $T/$R
# T3.8 team level, after team-integrate.js
python3 scripts/team_status.py $T --coverage           # paste into Coverage below, unchanged
python3 scripts/team_status.py $T --coverage --short   # the five-column summary for the team README, unchanged
python3 scripts/check_links.py $T
python3 scripts/team_check.py $T                       # delivery gate; judges the tier per member
```

Workflows in `scripts/workflows/`: `team-harvest.js` (T3.1), `team-chase.js` (T3.3), `team-read.js` (T3.5), `team-synthesize.js` (T3.6), `team-tighten.js` (T3.7), `team-integrate.js` (T3.8), `team-increment.js` (T4).

## Coverage

These counts are exact and were computed from each researcher's `references/sources/papers/INDEX.md` by `python3 scripts/team_status.py product/nonlinear-team --coverage`. Paste its output here; never edit a number by hand.

| Researcher | Scholar rows | Distinct works indexed | Open full text | Read in full | Read in part | Abstract only | Metadata only (incl. unreadable) | Skipped (not the author's / non-research) | Book material carded | Quotes verified |
|---|---|---|---|---|---|---|---|---|---|---|
| Frank E. Curtis | 96 | 96 | 87 | 86 | 0 | 8 | 2 | 0 | 0 | 180 |
| Jorge Nocedal | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| Stephen J. Wright | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| Yinyu Ye | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| Andreas Wächter | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| Philip E. Gill | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| Philippe L. Toint | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| Nicholas I. M. Gould | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| Roger Fletcher | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| Yurii Nesterov | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| Daniel P. Robinson | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| **Total** | 96 | 96 | 87 | 86 | 0 | 8 | 2 | 0 | 0 | 180 |

Notes:

- The zero rows are the ten base-tier members: they have no audited publication list and no `INDEX.md`, so nothing is counted for them. A zero means "not indexed", not "no publications".
- *Distinct works indexed* = Scholar rows minus duplicates, plus items found only in DBLP or on a homepage. For Curtis: 96 Scholar rows − 3 duplicates + D001, D002, H001 = 96. No interviews, memoirs or other special items are counted.
- *Metadata only (incl. unreadable)* for Curtis = S084 (metadata only) + S086 (unreadable).
- *Read in part* means the supplement reading: abstract, introduction, method or algorithm, main result, experimental setup and conclusion. Curtis has none: all 87 open texts were planned as core reads.
- *Book material carded* counts the `B` rows in INDEX.md: openly available parts of a book. There are none yet.
- *Skipped* rows have Role `skip` in INDEX.md and no card. Curtis has none; his pre-PhD combinatorics papers (S058, S081, S086) are carded but carry no weight in the synthesis (08, counting rules).
- Page references on cards are pages of the text version that was read, often a technical report or preprint. Check the journal page before citing one in a paper.

## Reading-batch brief (as used, shortened)

The full brief lives in `scripts/workflows/team-read.js`; this is the record.

```
You are deep-reading research works by {name} to deepen the research-craft skill at {skill}/.
Read first: references/paper-reading-card.md (card format) and SKILL.md's methods, heuristics and taste sections.
Batch {bid} (mode core | supplement | book | abstract): the work list is that batch in the plan JSON (ids, pages, txt paths).
core → read the whole work, full card D1–D8; supplement → abstract, introduction, method, main result, setup,
conclusion, short card; book → chapter level plus a chapter map; abstract → abstract or metadata card only, say which.
Check page 1 first: title and the member's surname among the authors, else "unreadable" + WRONG-TEXT; garbled → REOCR.
Write cards/{bid}.md (batch intent, focus dimensions, material roles, file-to-printed page mapping, one card per work)
and cards/{bid}.digest.json (one object per work: read_level, D1–D8 lines, method_links, quotes, …).
Rules: a page reference on every claim; at most two verbatim quotes per card, with page, that must pass
verify_card_quotes.py; "not read" rather than guess; a review is the reviewer's voice; link cards to Method N /
heuristics as evidence, variant or contradiction. No WebSearch in reading batches; abstract batches may use Crossref,
arXiv, Semantic Scholar and open publisher pages, never shadow libraries or paywall circumvention.
Never read references/sources/private/. Edit no file other than the batch's own outputs.
```

## What is still missing

- **Works with no open full text** have abstract or metadata cards only: 10 of 96 for Curtis (8 abstract only + 2 metadata only incl. unreadable, from the Coverage table); 0 for the other ten, who are not indexed. The biggest gaps, from Curtis's 08 "Open gaps": the stochastic inexact SQO paper S045 (its termination tests for stochastic gradients known only from the abstract); the ε-constraint fairness paper S055 and the bilevel synthetic-data paper S072; the SCOPF journal paper S060 (its preprint S061 was read); the adaptive stochastic optimization framework S031 (the D001 article was read); a workshop report S078; the MOPTA proceedings S079; the hard-constraint training paper S084 (metadata only).
- **Book bodies** were not read. Curtis's 2025 SIAM book *Practical Nonconvex Nonsmooth Optimization* (S074) is known only from a retailer's copy of the publisher's description, so its treatment of BFGS-SQP, gradient sampling and NonOpt is not known; SIAM front and back matter returned 403 to `curl` (`book-leads.json`). For the MOPTA 2010 proceedings (S079), the publisher's free front-matter PDF and table-of-contents page are logged as leads. No T4 increment has carded either.
- **Uneven periods.** Full reads by period for Curtis (full / carded, 08 §1): 2003–2007 4/5; 2008–2012 9/10; 2013–2017 19/19; 2018–2022 27/28; 2023–2026 27/34. Eight of the nine works without an open text date from 2020–2026; the ninth is S079 (2012).
- **Unreadable files** are listed on their cards: `frank-e-curtis` S086 (2003 William & Mary undergraduate thesis; garbled text layer; card in `c01`; combinatorics, outside the skill's scope).
- **Outside the publication list**: talks, syllabi, code history and student theses remain web-research evidence (notes 01–06); the deep reading neither confirms nor refutes the slide-only claims (08 "Open gaps").
- **The ten base-tier members** have no full-text reading at all (next section).

### How to extend

1. **Get a legitimate copy.** Sources are a library, publisher access or the author.
2. **Name the file like the index.** Use `<ID>-<year>-<first eight title words, lowercased, hyphenated>.pdf`, the stem `acquire_fulltexts.py` uses (the ID is the one in INDEX.md).
3. **Put it in `<researcher>/references/sources/papers/`.** This folder's PDFs and `txt/` are git-ignored. Check by hand that the file is the paper, because the title check only runs on downloads.
4. **Re-run the acquire script.** `python3 scripts/acquire_fulltexts.py product/nonlinear-team/<researcher> --only <ID>` extracts the text, OCRs scans, and sets `Full text = txt` and `Source = manual`. Run it in the checkout that holds the other papers' PDFs and `txt/`.
5. **Card and fold it in.** Either run `team-increment.js` (T4; see `scripts/workflows/README.md`), which cards the new material, folds it into the skill, verifies and fixes; or by hand: plan a new round with `python3 scripts/plan_reading_batches.py product/nonlinear-team/<researcher> --out-dir <scratch> --no-abstract` (or `--round N --exclude …`), read with the brief above, run `verify_card_quotes.py` and `mark_read_from_cards.py`, regenerate `07-paper-cards.md` with `python3 scripts/build_card_index.py <member folder>`, and apply the conservative-update rules to `SKILL.md`, `09-evidence-ledger.md` and `technique-catalog.md`.
6. **Refresh the numbers.** Re-run `python3 scripts/team_status.py product/nonlinear-team --coverage` and paste it unchanged into the Coverage table here; paste `--coverage --short` unchanged over the five-column summary in the team README (or run `team-integrate.js`, which does both).

## The other ten members (base tier, no deep reading)

Jorge Nocedal, Stephen J. Wright, Yinyu Ye, Andreas Wächter, Philip E. Gill, Philippe L. Toint, Nicholas I. M. Gould, Roger Fletcher, Yurii Nesterov and Daniel P. Robinson (joined 2026-10-17) are kept at the base tier by choice: no deep reading is planned for them. `team_status.py` reports each at "T1 base skill" with `SKILL.md` at 12/12 and notes 01–06 complete. Their skills rest on web research only: the six research notes in `references/research/`, `RESOURCES.md`, and the OpenAlex pull the notes started from (`publications/publications.md`, `abstracts.md`; for Robinson it was made after his notes, whose note 01 assembled his list from DBLP, Crossref, OpenAlex and his homepage), which is raw material, not an audited publication list. They have no `works.json`, `papers/INDEX.md`, paper cards, 07–09 or technique catalog, so their Coverage rows are zero and their sides of the roundtable's fault lines cite their notes and the papers those rest on, not cards.

To deepen one of them later, run stages T3.1–T3.8 of `references/research-team-playbook.md` for that member (the commands above with `R=<slug>`); `team_check.py` then checks that member at the deep tier, and this file and the README are refreshed by `team-integrate.js`.

## Privacy and integrity

- Private materials stay in each member's `references/sources/private/` (git-ignored) and are never read into public files. The deep reading worked only from public sources.
- PDFs and extracted text (`papers/*.pdf`, `papers/txt/`) are git-ignored for copyright reasons. Only indexes, abstracts, cards and syntheses are committed.
- Full texts come only from legitimate open copies: arXiv, Unpaywall, author pages, institutional report series and open repositories.
- The integrity rules in each skill still apply. No claim goes in without a page reference, and no quote is invented: every quote on a card passes `scripts/verify_card_quotes.py`. Nothing written by a co-author, reviewer or interviewer is attributed to the member.

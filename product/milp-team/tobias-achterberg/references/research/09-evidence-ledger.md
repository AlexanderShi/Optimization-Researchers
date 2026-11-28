# Tobias Achterberg · Evidence ledger

## Contents

- [How to Use, front matter and disclaimer](#how-to-use) · [Taste: marks](#taste-marks) · [Taste: warning signs and quick-check](#taste-warnings)
- [Method 1](#method-1) · [Method 2](#method-2) · [Method 3](#method-3) · [Method 4](#method-4) · [Method 5](#method-5) · [Method 6](#method-6)
- [Stage workflows](#workflows)
- Heuristics: [1](#heuristic-1) · [2](#heuristic-2) · [3](#heuristic-3) · [4](#heuristic-4) · [5](#heuristic-5) · [6](#heuristic-6) · [7](#heuristic-7) · [8](#heuristic-8) · [9](#heuristic-9) · [10](#heuristic-10)
- [Common misreadings](#misreadings)
- Anatomies: [branching](#anatomy-branching) · [conflict analysis](#anatomy-conflict) · [CIP thesis and SCIP paper](#anatomy-cip) · [presolve](#anatomy-presolve) · [Mcf-separator](#anatomy-mcf) · [RLT cuts](#anatomy-rlt)
- [Anti-patterns](#anti-patterns) · [Trajectory](#trajectory) · [Inner tensions](#inner-tensions) · [Mentor Voice](#mentor-voice) · [Roundtable Card](#roundtable-card)
- [Honest Boundary](#honest-boundary) · [Corrections](#corrections) · [Promotions and the candidate pool](#promotions) · [Rejected updates](#rejected) · [Held back under the holdout rule](#held-back) · [Sources appendix](#sources) · [Card key](#card-key)

> Date: 2026-11-28 (stage T3.6, team-synthesize). The full evidence behind `../../SKILL.md`. SKILL.md keeps, per item, the strongest statement and cards, a one-line say–do verdict, at most four variant or correction bullets and a pointer to the matching section here; the card counts per method are in the 08 tables copied here. Each section has up to four parts: **Full-text evidence** (copied word for word from [08-deep-reading-synthesis.md](08-deep-reading-synthesis.md), which is traceable to the cards, or taken from the named cards), **Variants, contradictions and proposals** (08 §3–§5), **Added in T3.6** (what this pass wrote into SKILL.md, with card ids) and **Before T3.6 (moved verbatim)** (the SKILL.md item as it stood on 2026-11-14, built from web research and a partial read of the reports, so nothing is lost; its headings are set in bold and its links re-pointed to work from this folder). Copied 08 text is left as copied; 08 itself is edited only for links and counts, and for the corrections of the fix round of 2026-11-28 (after three reviewers checked this pass: §2 Method 3, §2.7, §3.2 items 6, 10, 14 and 16, §8, §9 and the Voices line), made in 08 and in its copies here alike. Each section's **Fix round** bullet says what that round changed in SKILL.md; SKILL.md wording it replaced is kept there in italics, word for word.
>
> **How to read.** `[R004 p. 11]` is paper card R004 in [07-paper-cards.md](07-paper-cards.md), at the `[[page N]]` page of the file the card read ([../sources/papers/INDEX.md](../sources/papers/INDEX.md)). `TR` marks a report version read in place of the published one: `[D017 TR …]` (ZIB-Report 13-66, revision of April 2014), `[D018 TR …]` (ZIB-Report 15-53, revision of February 2016), `[D024 TR …]` (ZIB-Report 02-16, March 2002, under his former name, Tobias Pfender). D022 was read as arXiv 2211.13545v1 and D023 as v3; those are the files indexed for them. Abstract-, metadata-level and unreadable cards are cited by id only. In the *Before* blocks, keys such as THESIS p. 70 or ZR 05-19 p. 15 are printed pages: thesis file page = printed + 14; ZIB-Reports 02-16 to 10-27 file = printed + 1; 10-31 to 20-16 file = printed + 2; RAMP 2014 file = printed − 180. Marks: ✅ evidence · ⚠ variant (kept, nothing deleted) · ✗ contradiction or correction. PD, DM, EP and WM ids are entries of [../technique-catalog.md](../technique-catalog.md). Quotation marks enclose only text copied from a card that copied it verbatim from the text (`verify_card_quotes.py`, 2026-11-28: 84 quotes, 84 exact; every quotation added here was re-found in a card and in its text file on 2026-11-28) or, in the *Before* blocks, text the pre-synthesis SKILL.md quoted; wording of SKILL.md itself is set in italics.
>
> **Voices.** Four full texts are sole-authored, all 2004–2009: R003 (ZR 04-19), R004 (ZR 05-19), the thesis D004 and D010 (MPC 2009). Everything else is co-signed; apart from one part a text names as his ("Achterberg's heuristic" [D026 p. 7]) and the variability work MIPLIB 2010 credits to Danna [R015 p. 22], no co-signed text states roles. The ParaSCIP texts (R014, D029/R018, R019/D017, R020/D018, R022) have Shinano first; nothing in them is claimed for Achterberg alone. Post-2014 Gurobi work is closed code; its papers are the only written window, and public talks and interviews give dates and roles. One text per work: the published versions D001, D002, D003, D005, D007, D008, D014, D015 and D019 have no text of their own; their ZIB-Report rows (R002, R005, R004, R006, R009, R010, R014, R017, R021) hold it. Report and published pairs with separate texts are one study each: R019 and D017, R020 and D018, R018 and D029, R013 and D011, R015 and D013. D024 has two cards; the round-2 card in `cards/c2-01.md` supersedes the round-1 card in `cards/c01.md`.
>
> **Not carried.** The cards' reading notes on inconsistencies inside a work (a table that disagrees with its text, a typo, numbers that look carried over) are not findings about the researcher or his coauthors and are not used here; 08 §7.4 keeps one neutral lesson (catalog WM9). Material sealed in `holdout.md` is not used: no point, quote or decision of a sealed item appears in this file, and no card page that carries one is cited (the Before blocks keep the pre-synthesis wording as it was; two printed-page keys there are noted under [Held back](#held-back)). `FIDELITY.md` (the validation record) describes the sealed items and, like the card batch files, is not opened while the skill is used or tested. Two candidates that lean on sealed material are withheld ([Held back](#held-back)).
>
> **Scope.** One section per SKILL.md item this pass changed, plus the corrections, the promotion record, the rejected updates, the sources and the card key. Answer Standard, Research Integrity Rules, Research Task Routing, Academic Lineage, Mentor Voice and the rest of Activation Rules are unchanged and complete in SKILL.md (Activation Rules changed only in its disclaimer line, and a hand edit of two more lines is proposed to the operator; Agentic Protocol gained one bullet, see [How to Use](#how-to-use)). Counts: `team_status.py --coverage` on 2026-11-28 (0 Scholar rows · 55 distinct works indexed · 36 open full texts · 34 read in full · 2 in part · 11 abstract only · 6 metadata only incl. unreadable · 2 skipped · 0 book material · 84 quotes verified). Word budget after this pass: 11204 words by `answer_standard.py --words` (target about 11500, hard limit 13000); after the fix round 11950 (constants restored to the steps, labels and the conversion rule added; card counts, two variant bullets per method and one anti-pattern moved here).
>
> **T3.7 (tightening, 2026-11-28).** SKILL.md was brought under its word budget by moving evidence here, not by deleting it: wherever a SKILL.md line was shortened, the line as it stood before is kept word for word under **Before T3.7 (moved verbatim)** at the end of the matching section (links re-pointed to work from this folder). Sections with such a block: Methods 1–6 (Method 1's also holds the Core Research Methods intro), both taste lists, Heuristics 1–10, the misreadings, three anatomies (conflict analysis, Mcf-separator, RLT cuts), the trajectory, the inner tensions and a new [Mentor Voice](#mentor-voice) section. What moved: cases beyond the strongest one or two per heuristic, taste item and misreading; one Practice item in each of Methods 2, 4, 5 and 6; the card recount under Method 2's step-2 checkpoint and the future-work example of Method 6 step 5; date notes such as *(corrected 2026-11-28)*, since the Corrections list keeps every correction visible; one sentence each in the trajectory and two inner tensions; Mentor Voice's derived questions, which repeat the Roundtable Card's first questions; explanations that repeated another item. Where an *Added in T3.6* or *Fix round* line here quotes SKILL.md wording that T3.7 shortened, the section's Before T3.7 block holds that wording. Every step instruction, step constant and ✗/⚠ mark stays in SKILL.md; the front matter, How to Use, Activation Rules, Answer Standard, Research Integrity Rules, Research Task Routing, the Roundtable Card and the Honest Boundary with its Corrections list are unchanged. Budget count: 11957 → 11469 words by `answer_standard.py --words` (target about 11500, hard limit 13000).
>
> **T3.7 fix round (2026-11-28).** A read-only reviewer found five minor problems and no blocker; each was checked against the pre-tighten copy and this file. Back in SKILL.md, word for word from the Before T3.7 blocks (each block says so): in Method 2's step-2 checkpoint, the card recount *per instance it holds there on 17 of 29 (card recount) [R004 pp. 17–18]*, the per-instance support T3.6 added to it; at the end of taste mark 3, the 19 % case (WEB 9.5 0:15:53), because Mentor Voice cites mark 3 for reporting a disappointing result (mark 3 so keeps three cases); in Heuristic 6, the protocol *with comparable settings, collapsed variants presolve makes identical, reported sizes after preprocessing*, which the routing row on formulation and seed swings and Workflows A and E point to; in Heuristic 1, *which became ZR 02-32*, without which *in print only the thesis acknowledgement* could be read as if the history rule were unpublished; at the end of Method 2's ✗ bullet on the thesis's conflict setting, its remedy *check the release settings before citing a default* (the date note stays out); in Heuristic 5, the instances of its commits. Left here only: the Mcf anatomy's caution on the tuning aim (ranked last by the reviewer, and the restorations above already put the count over the target of about 11500; its bare page key would also stand beside a journal card citation in that row) and Heuristic 6's sentence on SCIP's implicit integers. **Say–do counts.** The T3.7 instruction (team-tighten.js, step 3) asks for a Say–do line with the counts. This skill's Say–do lines keep none, by the T3.6 fix-round decision that moved the counts into the per-method tables (recorded in each method's Fix round bullet): a bare total there would hide each table's split (Method 4: 29 cards, 9 of them with a contradiction link), and the Core Research Methods intro in SKILL.md points to the tables. That instruction is closed by this decision, not left open. Budget count: 11469 → 11529 words by `answer_standard.py --words` (target about 11500, hard limit 13000).

<a id="how-to-use"></a>

## How to Use, front matter and the first-activation disclaimer

### Added in T3.6

- **Front matter**: `researched:` 2026-11-14 → 2026-11-28. The description was 954 characters; it now names the coverage (*36 read in full or in part*), drops the two parenthetical keyword lists (component kinds; benchmark terms) and shortens *the accounts of students, successors and critics* to *others' accounts*; the trigger phrases and the non-trigger clause are unchanged.
- **Evidence format**: the card citation form, the page offsets between printed and file pages, the card key and the technique catalog added; the source keys are unchanged.
- **Voices** (new paragraph): the four sole-authored full texts [R003; R004; D004; D010]; co-signed texts state no roles; ParaSCIP has Shinano first [R014; D029]; post-2014 Gurobi code is closed (08 header, Voices; operator note).
- **Disclaimer line** (Activation Rules, the only line changed there): *This is distilled from public work, not Achterberg's own advice.* + the coverage of this member's `team_status.py --coverage` row (36 of 55 indexed works read in full or in part, the rest from abstracts or metadata) and the date 2026-11-28.
- **Changed by the operator's hand edit (2026-11-28)**: the Activation Rules defaults line now reads *absent from his sole-authored studies, present in co-signed ones (Misreading 1)* and the blind-spot example *his sole-authored studies used single runs; co-signed ones use permutations or repeats, and the five-seed rule appears only in his talks*. The full texts qualify the old wording (*absent from his written studies*; *his written studies used single runs; seeds appear only in his talks*): it holds for his sole-authored studies only (08 §3.2 item 3; [Corrections](#corrections)). T3.6 may change Activation Rules only in the disclaimer line (`check_ledger.py --allow frontmatter,activation-disclaimer`), so the deletion detector reports these two lines, by design.
- **Owner of the two lines (fix round, 2026-11-28)**: all three reviewers found both lines false as written (two as a blocker). No kit stage may reword them: team-tighten.js keeps Activation Rules byte-identical, team-integrate.js edits team files only, team-increment.js allows numbers only. So the rewording is a **hand edit by the operator before the commit**, done on 2026-11-28 and recorded in the distillation log (entry 27); the deletion detector with `--allow frontmatter,activation-disclaimer` reports these two lines, by design. The wording applied: defaults line, *absent from his written studies (Misreading 1)* → *absent from his sole-authored studies, present in co-signed ones (Misreading 1)*; blind-spot example sentence (inside the line's quotation marks) → *his sole-authored studies used single runs; co-signed ones use permutations or repeats, and the five-seed rule appears only in his talks*. With that edit, the Corrections line *Seeds (…): read as his sole-authored studies …* dropped its Activation Rules clause. The rest of each line (*(his: Method 4)*, *One machine → Method 4's Limitations*) resolves again: Method 4 step 4 states the shift and Method 4's Limitations has a one-machine clause (fix round).
- **Agentic Protocol, Step 2**: one bullet added, *Answer type (H8)*, from 08 §5 A [R004 pp. 16–19; R015 pp. 6, 8].
- **Fix round (2026-11-28)**:
  - *Evidence format*: the card-page conversion completed (thesis front matter: file page = roman page; D011 + 124, D013 + 102, D021 + 442, D029 + 46, D030 + 180; D017 and D018 TR − 2; D022 and D023 cited by arXiv version, never by journal page; the rest in the [card key](#card-key)); *`[D004 p. 84]` is paper card D004 ([07 paper cards](07-paper-cards.md)) at the `[[page N]]` page* → points to the card key, since 07's batch links open the closed card files; *paper cards* in the Answer Standard defined as the card key, this ledger and the catalog; the batch files and the local full texts closed while testing (reviewers: usefulness, fidelity).
  - *Voices*: *all others are co-signed and none states roles* → the one part a text names as his, "Achterberg's heuristic" [D026 p. 7] (card c03), and MIPLIB 2010's credit of its variability work to Danna [R015 p. 22]; *talks give dates, roles and his spoken views, never what the code does* → *talks and interviews give dates and roles, and his own account of team practice is labelled team or caption, never read as verified code behaviour* (operator note: talks and interviews give dates and roles only).
  - *Disclaimer line*: *the rest from abstracts or metadata* → *17 from abstracts or metadata, 2 patents not read* (11 abstract + 6 metadata; the 2 skipped patents have no card).

### Before T3.6 (moved verbatim)

Front matter (2026-11-14):

```yaml
---
name: tobias-achterberg
description: |
  Tobias Achterberg's research craft in MILP solver engineering, distilled from his thesis and papers (2002–2025), the SCIP code history, his talks, slides and interviews, and the accounts of students, successors and critics. Use it to decide whether a branch-and-cut component (branching, cuts, presolve, heuristics, conflicts, propagation) should be on by default, to judge a result where nodes or gap improve but time does not, to design or audit a solver benchmark (test-set rule, shifted geometric mean, time brackets, affected models), to budget a component's time, and to bring a SAT, CP or learned rule into MIP. Triggers: "Achterberg lens", "ask Achterberg", "how would Achterberg approach this", "what would Achterberg say about our default or benchmark", "use Achterberg's method", "Achterberg.skill". Also loaded by milp-roundtable. Not for general questions, Gurobi or SCIP user support, exact rational MIP, decomposition or polyhedral theory.
type: research-craft
researched: 2026-11-14
---
```

How to Use (2026-11-14):

**How to Use**

**Who and what.** Achterberg wrote SCIP alone from October 2002 as his doctoral work at ZIB (thesis, TU Berlin 2007; referees Grötschel and Bixby), joined ILOG CPLEX in 2006, and has been at Gurobi since March 2014, VP of R&D since 22 April 2020 (Gurobi 13.0 webinar, Nov 2025). This skill distils **how he decides what a solver component is worth**: how he measures, budgets, gates and imports. It does not teach what SCIP or Gurobi contain.

**Strengths**: component design, experiment design, judging results, writing up computations, problem choice from instances. **Weak spots**: literature review (self-declared), theory, supervision, team management, grants. **Domain fit**: builders and benchmarkers of general-purpose branch-and-cut need little translation except of resources (see Limitations); problem-specific algorithms use only part of Method 1.

**Evidence format.** Bracketed keys are listed in the Sources appendix: THESIS (printed pages), ZR nn-nn (ZIB-Reports), INT 2023 (interview timestamps), WEB x.y (Gurobi webinars), SEA 2022, CPAIOR 2017, MIPW 2025, ORIGINS 2022 (his slides); hex strings are SCIP commits. Labels: *stated* (his own words), *co-signed* (a joint "we"), *team* (Gurobi practice he describes), *practice* (what papers and code show), *observed* (others), *inferred* (this skill's reading), *caption* (automatic YouTube captions, not speaker-checked).

Disclaimer line (Activation Rules, 2026-11-14):

- On first activation say once: "This is distilled from public work, not Achterberg's own advice." Do not repeat it. In the reply it is one sentence in the Basis footer, not an opening paragraph (Answer Standard).

<a id="taste-marks"></a>

## Taste: marks of good research

### Full-text evidence (08 §2.7, copied)

- **Taste marks.** Mark 1 is strained by the neutral-on components of [R021 pp. 14, 18, 56, 65]. Mark 3 (small measured wins): Gurobi MILP gains of 1–11 % reported as improvements [D023 pp. 21–22]. Mark 6: its most explicit source is the co-signed MIPLIB 2017 selection model [D021 pp. 24–36]. Mark 7: data structures and limits in print [R021 pp. 37–38, 45, 49, 66; D023 pp. 7–8, 10, 14]. Warning sign 3: see §3.2 item 21.

### More card evidence (this pass)

- Mark 2 (default-robust): the unaffected (nosep) rows are about 1.00 in both solvers [D011 p. 34]; of all 1,388 general MIPs in the CPLEX runs (MIPLIB, Mittelmann and a 1,266-model CPLEX-internal set) 129 are affected, and the saving grows with difficulty [D011 p. 34; R013 p. 28]; the hybrid branching default keeps inference branching's gains on alu and acc and equals reliability branching elsewhere [D004 p. 84].
- Mark 4 (one explainable rule): one reliability parameter spans pseudocost, strong-branching-initialised and full strong branching [R002 p. 8]; "Note that you can obtain the original Feasibility Pump by choosing α0 = 0." [R006 p. 5]; hybrid branching reduces to reliability branching at zero weights [D004 p. 81].
- Mark 5 (fair before interesting): matched gap tolerances [R001 p. 11; R003 p. 24; R004 p. 16]; only the MIP part compared [D004 pp. 334, 391; D010 p. 29].
- Mark 6 (large, rule-selected set): the thesis rule, 575 instances to 244 in five steps [D004 p. 334], weighted by pseudo-instances [D004 p. 336]; MIPLIB 2003's removal by a stated weakened-solver rule [R005 p. 3]; MIPLIB 2010's class rebalancing [D013 p. 6]; MIPLIB 2017's selection model [D021 pp. 24–36] (all three libraries co-signed).

### Added in T3.6

- Mark 1: ⚠ line, four Gurobi presolve components on at no measured gain [R021 pp. 14, 18, 56, 65].
- Mark 2: [D011 p. 34]. Mark 3: RLT's 1–11 % on Gurobi MILP brackets [D023 pp. 21–22]. Mark 4: [R002 p. 8]. Mark 6: [D021 pp. 24–36]. Mark 7: [R021 pp. 37–38, 49; D023 pp. 7–8].
- **Fix round (2026-11-28)**: Mark 1, *⚠ Four Gurobi presolve components stay on at no measured gain [R021 pp. 14, 18, 56, 65].* → a pointer to Method 1's ✗ bullet, which carries the cards (the point was made three times). Mark 3: the Gurobi 11.0 deck items labelled *team*, the WEB 13.0 item *team, caption*, the RLT figure *co-signed* (Voices: talks are his account, not verified code behaviour). Mark 6: *most explicit in the co-signed MIPLIB 2017 selection model* → *also in*, since the selection model is a 16-author committee paper and not treated as his method (08 §10 item 7).

### Before T3.6 (moved verbatim)

**Marks of good research**

1. **A gain in total time on a broad set** *(new)*: ZR 05-19 abstract and THESIS pp. 69–70 (Method 2); a cut can cut off the LP point, tighten the bound and still lose, while presolve ideas usually pay (WEB 9.1 1:19:14; INT 2023 41:08–41:38).
2. **Default-robust: helps its class, silent elsewhere** *(new)*: the MCF separator's detector (ZR 09-38 pp. 1, 29); the hybrid branching default (THESIS p. 70).
3. **Small measured wins are progress** *(new)*: twenty Gurobi 11.0 MIP changes of 0.3–2.1 % each (11.0 deck slides 12–13); a cut family touching 10 % of models for 2.5 % (WEB 13.0 0:04:39). A year of work for 19 % he calls not very impressive (WEB 9.5 0:15:53).
4. **One explainable rule, incumbents as special cases** *(new)*: the 2002 machinery reduced to one parameter (Method 3); a learner reduced to its feature (H1); decision trees over SVMs because he wanted to understand the rule (WEB 9.1 0:59:59).
5. **Fair before interesting** *(new)*: equal gap tolerances with CPLEX (ZR 02-32 p. 10; ZR 05-19 p. 15 fn. 4); only the MIP part compared, since SCIP used CPLEX's LP solver (THESIS p. 377).
6. **Evidence is a large, rule-selected, class-balanced set** *(known)*: THESIS pp. 320–322; ZR 16-44 p. 17.
7. **Engineering detail deserves print** *(known)*: ZR 16-44 p. 2; INT 2023 50:27–53:35.

### Before T3.7 (moved verbatim)

The SKILL.md lines that the T3.7 tightening (2026-11-28) shortened or moved, as they stood before it; links re-pointed to work from this folder. The shortened lines are in SKILL.md.

*Mark 3:*

3. **Small measured wins are progress** *(new)*: twenty Gurobi 11.0 MIP changes of 0.3–2.1 % each (11.0 deck slides 12–13; team); a cut family touching 10 % of models for 2.5 % (WEB 13.0 0:04:39; team, caption); RLT's 1–11 % on Gurobi MILP brackets (co-signed) [D023 pp. 21–22]. A year of work for 19 % he calls not very impressive (WEB 9.5 0:15:53).

*T3.7 fix round (2026-11-28):* the last sentence, the 19 % case, is back in SKILL.md (Mentor Voice cites mark 3 for reporting a disappointing result); the cut-family case stays here.

*Mark 4:*

4. **One explainable rule, incumbents as special cases** *(new)*: the 2002 machinery reduced to one parameter (Method 3) [R002 p. 8]; a learner reduced to its feature (H1); decision trees over SVMs because he wanted to understand the rule (WEB 9.1 0:59:59).

<a id="taste-warnings"></a>

## Taste: warning signs and quick-check

### Full-text evidence

- **Warning 1** (a proxy gain with no time result): the 2005 abstract prints the time loss beside the node gain: "On feasible MIP instances, the number of required branching nodes was reduced by 50% in the geometric mean. However, the total solving time increased by 15%." [R004 p. 2]; the 2025 RLT study prints a root-bound gain "although this does not always translate into an improvement in overall solver performance" [D023 p. 16].
- **Warning 3** (a habit nobody measured): most infeasible is called not better than random [R002 p. 5]; geometric-mean times random 923.6 s, most infeasible 938.0 s, pseudocost 283.4 s, full strong 504.4 s, reliability (8, 4) 170.5 s [R002 p. 17]; in the 2002 node test most infeasible does worse than random [R001 p. 12]. The child-selection sentence: copied from 08 §3.2 item 21 below.

21. **Taste warning sign 3 and Integrity rule 4** (the unmeasured child-selection default, THESIS p. 74). The sentence concerns Martin's root-LP child selection when it was adopted; the same chapter measures it and finds the default hybrid slightly inferior [D004 pp. 88, 95–96]. Keep the quote, add that it was measured in the same chapter.

- **Warning 5** (new; a speed-up read off a small affected set): small affected sets refused or rechecked in the presolve paper: 48 SOS models "too small" [R021 p. 19], 13 semi-continuous models [R021 p. 22], 40 models whose gain turned out to be variability [R021 p. 40], about 200 penalty-variable models [R021 p. 42]; the Mcf paper refuses verdicts on 16 and 3 affected public models and accepts them on 129 of 1388 [D011 pp. 34–35; R013 p. 27]. Quotes: "Nevertheless, such a small set of problem instances does not provide any meaningful results, and indeed, additional tests that we have conducted showed that the speed-up in Table 23 is just an artifact of performance variability." [R021 p. 40]; "one has to take this result with care, as a set of about 200 models is usually not large enough to measure such an impact precisely enough." [R021 p. 42]; "The results for the general MIP sets miplib and mittelmann are not conclusive since the number of affected instances is very small" [R013 p. 27]; "In contrast to Table 3 and Scip we can trust these values since the overall testset is very large with a reasonable number of affected instances." [D011 p. 34]. All co-signed; recurrence 2009–10 and 2016; it is also Method 4 step 5 and EP6, kept here as a judgement criterion for reading others' work.
- **Quick-check**: one question added, from 08 §5 A (answer type: proofs and witnesses tabled apart).

### Added in T3.6

- Warning 3: [R002 p. 17] numbers; ⚠ the child-selection default measured later in the same chapter [D004 pp. 88, 95–96].
- Warning 5 (new): [R021 pp. 40, 42; D011 pp. 34–35].
- Quick-check: *Are instances that need a proof (infeasible) tabled apart from those that need a feasible solution?*
- **Fix round (2026-11-28)**: Warning 3, *he flags his own unmeasured child-selection default (p. 74), ⚠ measured later in the same chapter [D004 pp. 88, 95–96]* → he labelled Martin's root-LP child selection, adopted from SIP, as unmeasured, and the same chapter measured it and printed that the default hybrid came out slightly inferior to three alternatives (THESIS pp. 74, 82) [D004 pp. 88, 95–96] (08 §3.2 item 21; the measured case is the warning's own example). The quick-check question above was removed from SKILL.md: it had no card ids and no taste mark or warning behind it, it made the list nine questions (framework §4: 5–8), and the proof/witness split stays in H8, Agentic Protocol Step 2 and Workflow D step 4.

### Before T3.6 (moved verbatim)

**Warning signs of bad research**

1. **A proxy gain with no time result** (sources of mark 1).
2. **Excellent on some classes, useless on others, no detector**: his 2023 view of automatic Dantzig–Wolfe decomposition as in GCG, hence not in Gurobi's defaults; the user supplies the partition (INT 2023 1:00:45–1:02:20, caption).
3. **A habit nobody measured**: most-infeasible branching is about as good as random (ZR 04-13 p. 4; THESIS pp. 3, 69); he flags his own unmeasured child-selection default (p. 74).
4. **A convenient answer that is mathematically wrong**: fixed-LP duals read as MIP sensitivity (WEB 9.0 0:38:59).

**Taste quick-check**

- [ ] Is the gain in total time (or the user's own target), not only nodes, bound or cuts?
- [ ] Was the feature switched off in the full default of a complete solver?
- [ ] Does the test set have a stated rule, enough affected models, no dominating class?
- [ ] Does the code recognise its models and do nothing on the others?
- [ ] Is the baseline at its best, with the same tolerances and LP solver?
- [ ] Are the incumbent rules parameter settings of the new one?
- [ ] Is the component's effort budgeted?
- [ ] Does the write-up print what got worse and what stayed open?

### Before T3.7 (moved verbatim)

The SKILL.md lines that the T3.7 tightening (2026-11-28) shortened or moved, as they stood before it; links re-pointed to work from this folder. The shortened lines are in SKILL.md.

*Warning 2:*

2. **Excellent on some classes, useless on others, no detector**: his 2023 view of automatic Dantzig–Wolfe decomposition as in GCG, hence not in Gurobi's defaults; the user supplies the partition (INT 2023 1:00:45–1:02:20, caption).

*Warning 3:*

3. **A habit nobody measured**: most-infeasible branching is about as good as random (ZR 04-13 p. 4; THESIS pp. 3, 69): 938.0 s against 923.6 s [R002 p. 17]; he labelled Martin's root-LP child selection, adopted from SIP, as unmeasured (p. 74), and the same chapter measured it and printed that the default hybrid came out slightly inferior to three alternatives (p. 82) [D004 pp. 88, 95–96].

<a id="method-1"></a>

## Method 1: The do-no-harm default gate

### Full-text evidence (08 §2, copied)

| Method | Cards (E / V / C) | Studies | Full or partial cards | E by period | Say–do after the full texts |
|---|---|---|---|---|---|
| M1 Do-no-harm default gate | 17 (10 / 11 / 1) | 15 | 17 | 1 / 3 / 2 / 4 | ✅ stated (co-signed) + practised; the matrix-detector form from 2009; the thesis decides defaults on a weighted total without a detector |

**Method 1 · The do-no-harm default gate**

- **Strongest practice.**
  - The canonical case, now read in both versions: a detector on the matrix with a numeric fit (minority votes per arc, averaged over arcs), a no-op path when the fit is poor, tuning aimed at not slowing general MIPs, the three numbers reported (target sets, public general sets, a broad CPLEX-internal set), unaffected rows near 1.00, the `modeltype` parameter detected automatically by default, and conservative defaults kept against class gains [D011 pp. 11, 19–20, 24, 28–34, 37–38; R013 pp. 2–4, 10, 23, 28–30].
  - Gurobi presolve gates: full-LP redundancy only in special situations, OBBT only for selected variables, local symmetry recomputed only when the matching structure is detected; the redundancy checks and the multi-column dual-fixing extension stay off [R021 pp. 27, 28, 36, 40, 62; D030 pp. 4, 9, 12].
  - Thesis: the hybrid branching default keeps inference branching's gains on alu and acc and equals reliability branching elsewhere [D004 p. 84]; per-call guards turn RENS, root restarts and reduced-cost bounds into no-ops when they are unlikely to pay [D004 pp. 125, 132–133, 174].
  - 2022–2025: a detector of implicit products on pairs of linear rows, checked in a second, independently written solver on a class-balanced Gurobi set [D023 pp. 5–9, 21–22; D022 pp. 5–7, 14].
- **Stated (co-signed).** The Bixby–Rothberg remark is quoted as the design rule [R013 p. 2; D011 p. 2]. A new algorithm rarely helps all instances, costs effort to decide when to run it, and can slow instances solved before, so a general solver is re-tuned on a large set that includes formerly fast instances [D029 p. 2]. "Average performance on this set is not a suitable criterion to decide which MIP solver to use in a particular application scenario." [D021 p. 3].
- **Say–do update.** ✅ unchanged. Era: the matrix-detector form starts with the Mcf-separator (2009–2010); in the thesis, defaults are decided on the pseudo-instance-weighted total and per-set losses are accepted [D004 p. 336; D010 pp. 17, 19–20].
- **Variants.** Refusal thresholds inside a parallel technique (merge only above 0.9 shared fixings; undo a merge on any bound loss), with no detector and no harm measurement [D018 TR pp. 11–13]; a parallel default chosen for stability over runs and its trend with scale rather than for the faster mean, a choice the authors call difficult [D029 pp. 21, 26; R018 pp. 19–21]; a problem-specific method that runs the class it was not built for on purpose and prints the loss [D020 pp. 16–17]; implicit-product cuts end in a class split without a detector of the paying classes, the SCIP set keeps only instances where the component acts, and the two codes differ on MILPs overall [D023 pp. 13, 15–16, 21–22; D022 pp. 10–11, 14]; the gate study itself changed between the report and the journal version (§3.3).
- **Contradiction (partial).** Components stay on with no measured gain: Chvátal–Gomory strengthening, simple probing on single equations and biconnected components are neutral, and global probing at nodes stays on although the default has 36 time-outs against 14 without it; the authors say the test measures only the extra probing in the tree [R021 pp. 14, 18, 56, 65]. Step 5 (*Neutral or better elsewhere → on*) allows this; Taste mark 1 does not.
- **Proposed text.** Practice: cite the journal version beside the report for the gate, with the version note of §3.3; add the three neutral-on components to the counter-example list. New step 0 from §5 B (validity first). Step 5: when two codes disagree on the general set, no default is stated in the 2022–2025 study [D022 p. 14; D023 pp. 21–22]; the rule as written would leave it off.

### Variants, contradictions and proposals (08 §3–§5, copied)

| Card(s) | Method | Claim of the card | Check | Verdict |
|---|---|---|---|---|
| R021 | M1 | components on without a measured gain | [R021 pp. 14, 18, 56, 65] | Partial: step 5 allows it, Taste mark 1 does not |

5. **Method 1, Practice, the Mcf gate.** Now *Releasing the network-inconsistency threshold alone helped SCIP but not CPLEX*. This follows the report [R013 pp. 27–29]; the journal version reports the study on the general-MIP sets in both solvers, where releasing the threshold alone "already deteriorates the performance" of CPLEX, the SCIP rows still improve slightly, and the class gain on one network-design set no longer appears [D011 pp. 34–37]. Keep the sentence with the version named, and add the journal result.

6. **Method 1, Practice, counter-examples.** Add simple probing on single equations, biconnected components and global probing at nodes (on by default; at most 3 % on their affected models; the last with more time-outs when on) [R021 pp. 18, 56, 65].

**B. Method 1 step 0 · Validity first, so the gate can trade speed alone**

- **One line**: design the component so that any error of its heuristic parts (a wrong detection, a changed setting, an unstable LP) can only cost time; then the default gate is a speed decision.
- **Cards**: cuts are MIR inequalities of aggregations of original rows, so a wrong detection only makes cuts weak or dense [D011 pp. 7–9, 35; R013 pp. 3, 27]; an unstable LP is retried with other settings, and otherwise the node's LP bound is dropped and the node processed as if no LP had been solved [R003 p. 20; D004 p. 48]; settings changed between parallel jobs alter the path, not the result [R014 p. 11].
- **Checks**: §4 row 3.

### Added in T3.6

- **Evidence condensed**: Stated → the Bixby–Rothberg design rule in the Mcf paper [D011 p. 2] (also [R013 p. 2]), with SEA 2022 kept. Practice → the Mcf detector, gate, tuning aim, three numbers and `modeltype` [D011 pp. 11, 19–20, 27–34; R013 pp. 2–4, 28–30]; Gurobi presolve gates [R021 pp. 27–28, 36, 62; D030 pp. 4, 9, 12]; the hybrid branching default [D004 p. 84]. The 2022–25 detector checked in a second code [D023 pp. 5–9, 21–22; D022 pp. 5–7, 14] and the per-call guards [D004 pp. 125, 132–133, 174] stay in the 08 text above (per-call guards also in step 2). Say–do from the 08 §2 table.
- **Variant bullets**: thesis era [D004 p. 336; D010 pp. 17, 19–20]; ✗ neutral components on [R021 pp. 14, 18, 56, 65] (08 §3.1, §3.2 item 6); the Mcf version note [R013 pp. 27–29; D011 pp. 34–37] (08 §3.2 item 5, §3.3); the 2022–25 class split [D023 pp. 16, 21–22]. Not carried into the four bullets (kept here): the parallel-default and merge-threshold variants [D029 pp. 21, 26; R018 pp. 19–21; D018 TR pp. 11–13], co-signed with Shinano first.
- **Steps**: new step 0, validity first (08 §5 B) [D011 pp. 7–9, 35; R003 p. 20]; step 1 + DM5; step 2 + per-call guards [D004 pp. 132–133, 174]; step 5 + codes that disagree give no default [D022 p. 14] (08 §2 proposed text) and the commit 1c685467e from the old Practice line; step 6 + the commits 7827f4f11 and b9cd8fd36 from the old Practice line.
- **Limitations**: + the feedback-arc-set study runs its non-target class on purpose and prints the loss [D020 pp. 16–17].
- **Earlier evidence**: the old Evidence block (below) carried ZR 09-38 pp. 1–3, 16–17, 22, 27–29 (= R013 file pp. 2–4, 17–18, 23, 28–30), THESIS p. 70 (= D004 p. 84), RAMP 2014 p. 192 (= D030 p. 12) and ZR 16-44 p. 12 (= R021 p. 14).
- **Fix round (2026-11-28)**:
  - Step 5: *codes that disagree give no default (the 2022–25 study states none [D022 p. 14])* → descriptive and labelled: the co-signed study states no default and names the best setting per instance class [D022 pp. 11, 14; D023 p. 16]; *inferred*, a split result yields a per-class conditional, not a default. The old clause built a rule on a silence, and D022 p. 14 reads SCIP's slight MILP slowdown (1.03 on all MILPs, p. 11) and Gurobi's slight speed-up (0.99) as the same tendencies (paraphrase; cards c07, c08); D023 p. 16 says the use of implicit-product cuts depends on the problem. A *neutral* threshold added, labelled this skill's: within the thesis noise band (up to 2 % in mean time, THESIS p. 319 = [D004 p. 333]), no extra time-outs, seeds run.
  - Variant, 2022–25: *with no detector and no stated default* → *with no detector of the classes where they pay … and no stated default*; the paper's contribution is a detector of implicit products [D023 pp. 5–9].
  - ✗ presolve components: *step 5 allows it, taste mark 1 does not* → read through step 5's threshold (the one with more time-outs would be a default-off parameter).
  - Step 0 labelled *shared practice* (08 §4 row 3: exclusivity ✗), PD8 *co-signed*. Step 2: *[D004 pp. 132–133, 174]* → [D004 pp. 125, 132–133; R012 p. 11]: p. 125 holds the reduced-cost-bound guard and pp. 132–133 the RENS guard, while p. 174 argues the restart trade-off and the 5 % restart rule is in R012 p. 11 (p. 174 stays cited in Method 6 step 4).
  - Different from standard practice: *he makes "no harm elsewhere" a design goal with its own detector and measurement* (pre-synthesis wording, in the Before block) → the co-signed Mcf and Gurobi presolve papers do [D011 pp. 2, 34; R021 pp. 27–28], while his sole-authored thesis decides on a weighted total [D004 p. 336].
  - Say–do line: *17 cards (10 / 11 / 1), 15 studies* moved to the 08 table above.

### Before T3.6 (moved verbatim)

**Method 1: The do-no-harm default gate *(new)***

**One line**: a component is on by default only if it recognises its models from the matrix and is silent, and cheap, everywhere else.

**Evidence**:
- Stated: design for practical instances but always safeguard the worst case (SEA 2022 slides 20–21). ZR 09-38 p. 1 (co-signed) opens from Bixby and Rothberg's remark (DOI 10.1007/s10479-006-0091-y) that a method should recognise its models and cost little elsewhere. Automatic decomposition: warning sign 2.
- Practice: the MCF separator detects a multi-commodity network in the matrix, measures its inconsistency, and generates no cuts when inconsistent; tuned for network design without slowing general MIPs, checked on four sets, in SCIP and CPLEX (ZR 09-38 pp. 1–3, 16–17, 22, 29). Releasing the network-inconsistency threshold alone helped SCIP but not CPLEX, so the default stayed conservative with both refusal thresholds (network and arc) active; releasing both hurt (pp. 27–28). Hybrid branching default because inference branching wins only on feasibility sets (THESIS p. 70). Multi-row redundancy checks off for MIP because they hurt (RAMP 2014 p. 192). 2008 commits revert changes not good overall (7827f4f11), keep a pump-timing change as a default-off parameter (1c685467e), switch pairwise presolving off (b9cd8fd36). Counter-example kept: Chvátal–Gomory strengthening gains nothing and stays on (ZR 16-44 p. 12).
- Say–do consistency: ✅ stated + practised.

**Steps**:
1. Name the target class; write a detector on the coefficient matrix with a numerical measure of fit (not model names or user labels).
2. Make the component a no-op when the fit is poor.
3. Tune on the target sets under a second goal: no slowdown on general sets.
4. Report three numbers: target-class gain, change on public general sets, change on the broadest set available.
5. Neutral or better elsewhere → on; otherwise a default-off parameter. A gain that shows in only one of two codes or sets does not loosen the default. If the gain needs information the solver cannot detect, ask the user for it; where possible through a model-type parameter whose default detects the type automatically (the MCF separator's directed/undirected `modeltype`, ZR 09-38 p. 22).
6. Revert after release what does not look good overall.

**Applies to stage**: design; judging results.

**Different from standard practice**: papers report the target-class gain; he makes "no harm elsewhere" a design goal with its own detector and measurement.

**Limitations**: averaging over a heterogeneous library penalises class-specific methods (the ML objection, Khalil et al., DOI 10.1609/aaai.v30i1.10080, and the decomposition line). It is a product-default criterion, not one of scientific interest. Problem-specific algorithms: steps 1–4 only.

### Before T3.7 (moved verbatim)

The SKILL.md lines that the T3.7 tightening (2026-11-28) shortened or moved, as they stood before it; links re-pointed to work from this folder. The shortened lines are in SKILL.md.

*Core Research Methods intro (the line above Method 1):*

Six methods, all kept after the full texts (08 §4). Card counts per method and the web-research evidence each method had before (source keys, commits) are in the ledger, word for word.

*Variant bullet, 2022–25:*

  - ⚠ 2022–25 (co-signed): implicit-product cuts split by class, with no detector of the classes where they pay (the paper leaves the choice to the problem) and no stated default [D023 pp. 16, 21–22].

<a id="method-2"></a>

## Method 2: A proxy is not a payoff — split the time, then budget

### Full-text evidence (08 §2, copied)

| Method | Cards (E / V / C) | Studies | Full or partial cards | E by period | Say–do after the full texts |
|---|---|---|---|---|---|
| M2 A proxy is not a payoff | 28 (22 / 7 / 1) | 23 | 27 | 4 / 7 / 5 / 6 | ✅; step 1's rule that a time loss goes into the abstract holds for the 2005 report, not for the later abstracts |

**Method 2 · A proxy is not a payoff: split the time, then budget**

- **Strongest practice.**
  - The source of the time split, read in full: basic, switching and conflict time per instance with clause counts and lengths; the dominant cost (continuing bound-exceeding LPs) and the side cost (switching) named; an IIS heuristic and one algorithm step dropped for their cost [R004 pp. 11, 15–18]. The card's recount supports SKILL.md's *inferred* checkpoint per instance: on 17 of 29 instances the component's time plus the added switching time exceeds the basic-time saving [R004 pp. 17–18].
  - Thesis: full strong branching gives the smallest trees and is about 100 % slower on the mixed sets [D004 pp. 83–84]; local cuts at every node give −70 % nodes and +137 % time [D004 p. 129]; bound-exceeding and full conflict analysis cut nodes but not time [D004 pp. 194–195]; budgets set in solver units throughout [D004 pp. 78–80, 171, 193].
  - Gurobi era: probing limits counted in touched non-zeros and scaled by success, local probing driven by work and success ratios, a capped conflict pool with aging [R021 pp. 49, 64, 66]; the node column locates where time goes (cleanup and cancellation gain through faster LPs, a dependent-row loss through larger trees, not factorization) [R021 pp. 9, 28, 33; D030 pp. 12–13].
  - RLT: the root-bound gain is printed beside the time loss, "although this does not always translate into an improvement in overall solver performance" [D023 p. 16]; separation's share of total time cut from about half to under 3 % on MILPs [D022 p. 13; D023 pp. 17–18]; budgets in solver units [D022 p. 10; D023 p. 13]; "We observe a slight increase in time when RLT cuts are enabled, and a slight decrease in number of nodes." [D022 p. 11].
  - Elsewhere: node counts never read as speed [R011 pp. 7–8]; speed-ups read as nodes times throughput [D010 pp. 17, 20, 29, 36]; the classroom form (find the component that takes the time, ask what it buys for this class, switch it off) [R007 p. 7]; co-signed phase splits of parallel runs [D017 TR pp. 13–15; R019 pp. 5, 11, 13–14; R020 p. 13; D029 pp. 16–17, 20, 28; R018 pp. 17–18].
- **Say–do update.** ✅ unchanged.
- **Variants.** The thesis does not split time into base, switching and component time; it reads overhead from whether node and time changes move together [D004 p. 194] (proposed step 2 alternative below). In 2005 the only budget was aging; the cap of ten conflicts per infeasible subproblem appears in 2007 [R004 pp. 15–16; D004 p. 193]. The payoff is redefined for primal heuristics, with a measure of their own [R017 pp. 3, 5–7; D015], and for record-seeking parallel work, where strong scaling is rejected as a measure [R022 pp. 6, 20]. A co-signed load-balancing study names its dominant cost by phase but controls it with wall-clock periods, not work units [D018 TR pp. 8–9, 14].
- **Contradiction (co-signed).** The 2008 abstract calls SCIP almost competitive on solved counts (33 against 34) while CPLEX is at least 10 % faster on 27 of 36 instances [R009 pp. 2, 10]. Step 1's rule (a time loss goes into the abstract) is met by the 2005 conflict report [R004 p. 2] and not by later abstracts (§2.7, H10).
- **Proposed text.**
  - Practice: the conflict-analysis configuration is the thesis's experiment setting, not a stated default, and SCIP 0.90f was benchmarked with conflict analysis off by default (§3.2 item 4).
  - Step 2 alternative, when no component timer exists: split time into a count and a unit cost (nodes × time per node; iterations × cycle time), write down before the run which factor the change should move, then report both ratios [D026 pp. 8–9, 15, 32–34, 39; D004 pp. 84, 194; D010 pp. 29, 36; R011 pp. 7–8].
  - Step 2b from §5 C (hardness first, then the cheapest surrogate).
  - Limitations: the primal integral's first written form is co-signed by him in 2011 (§3.2 item 8).

### Variants, contradictions and proposals (08 §3–§5, copied)

| Card(s) | Method | Claim of the card | Check | Verdict |
|---|---|---|---|---|
| R009 | M2 step 1 | a solved-count verdict in the abstract beside a time loss in the table | [R009 pp. 2, 10] | Upheld (co-signed); recorded as a variant of step 1 and of H10 |

4. **Method 2, Practice, conflict analysis.** Now *The 2007 default uses conflicts for propagation only …, at most 10 per infeasible subproblem, with aging*. Replace by: these are the parameter settings of the thesis experiments [D004 pp. 192–193]; in the SCIP 0.90f MIP benchmarks conflict analysis was off by default and was measured by adding it to that reference [D004 pp. 193, 386; D010 pp. 20–21]; the best variant gains about 12 % against no conflict analysis [D004 p. 193]. The reason against LP cuts for non-binary conflicts is given only in part: the linearized disjunction is called probably very weak, untested [D004 p. 191; R004 p. 14].

8. **Method 2, Limitations, the primal integral.** Its first written form is a 2011 report that he co-signed (first of three, alphabetical; roles not stated), which defines the measure and normalises it by the all-off run [R017 pp. 3, 5–7]; the 2012 abstract keeps the claim to introduce it [D015]. The 2013 journal paper SKILL.md cites is a later venue (not read).

**C. Method 2 step 2b · Prove the exact sub-decision hard, then keep the cheapest rule**

- **One line**: when a component must solve a selection problem exactly to be optimal (a minimal infeasibility explanation, a redundancy test), prove or cite its hardness, try the literature's heuristic and measure its overhead, and keep the cheapest rule on data already computed, with the exact test only in special situations.
- **Cards**: minimal bound-IIS shown NP-hard, a Farkas-based literature heuristic dropped for its running-time overhead, simple rules on the LP information at hand kept [R004 p. 11; D004 p. 188; R009 p. 6; R008 pp. 8–9]; non-redundancy NP-complete, so LP-redundancy is the target and full LPs are solved only in special situations, cheaper subsets otherwise [D030 pp. 3–4; R021 p. 27].
- **Checks**: §4 row 4.

### Added in T3.6

- **Evidence condensed**: Stated → the 2005 abstract's loss sentence [R004 p. 2] (sole author; the old Stated line, THESIS pp. 69–70 and p. 181 and ZR 04-13 pp. 10–11, is below). Practice → the time split and the card recount of 17 of 29 [R004 pp. 11, 15–18]; full strong branching and local cuts [D004 pp. 83–84, 129]; Gurobi work limits [R021 pp. 49, 64, 66]; RLT separation share [D023 pp. 17–18]. Say–do from the 08 §2 table.
- **Variant bullets**: ✗ the conflict configuration is the thesis's experiment setting (08 §3.2 item 4) [D004 pp. 192–193, 386; D010 pp. 20–21]; node–time co-movement [D004 p. 194]; aging only in 2005 [R004 pp. 15–16; D004 p. 193]; ✗ the 2008 abstract (08 §3.1 R009 row) [R009 pp. 2, 10].
- **Steps**: step 2 + EP8 and the per-instance support of the checkpoint [R004 pp. 17–18]; new step 2a (count × unit cost; 08 §2 proposed text) [D026 pp. 8–9; D010 p. 29]; new step 2b (08 §5 C) [R004 p. 11; D030 pp. 3–4]; step 4 + DM2.
- **Limitations**: the primal integral's first written form [R017 pp. 5–7] (08 §3.2 item 8); the Berthold 2013 DOI kept, marked not read.
- **Fix round (2026-11-28)**:
  - Practice: *dominant and side cost named* → the dominant cost (continuing bound-exceeding LPs to optimality for initial conflict sets) and the side cost (switching time growing with the local constraints) named [R004 pp. 11, 15–18] (the old Practice line below, ZR 05-19 pp. 15–16 = R004 pp. 16–17).
  - ✗ conflict setup: *The conflict setup once given here as the 2007 default (propagation only, ≤ 10 per infeasible node, aging) is the thesis's experiment setting; SCIP 0.90f ran with conflict analysis off [D004 pp. 192–193, 386; D010 pp. 20–21].* → written as the lesson it teaches (a thesis's experiment setting is not the release default; check the release settings).
  - ✗ 2008 abstract: *The abstract rule holds in 2005, not later: the 2008 abstract rests on solved counts while its table has CPLEX ≥ 10 % faster on 27 of 36 [R009 pp. 2, 10].* → neutral wording: step 1's rule holds in 2005 [R004 p. 2], not in later abstracts; in 2008 the verdict rests on solved counts (33 against 34) and the time ratios stay in the table [R009 pp. 2, 10].
  - Moved here from SKILL.md (era notes that change no step): *⚠ The thesis reads overhead from node–time co-movement, not a time split [D004 p. 194].* (its card now cited in step 2a) and *⚠ In 2005 the only budget was aging; the per-node cap is from 2007 [R004 pp. 15–16; D004 p. 193].*
  - Step 2 checkpoint: *it holds there on 17 of 29 instances [R004 pp. 17–18]* labelled *(card recount)* (card c02: my recount).
  - Steps 2a and 2b: nested under step 2 (as *2a.* and *2b.* they were not list items in Markdown) and labelled *shared practice* (08 §4 rows 4 and 6: exclusivity ✗); 2a cites the sole-authored reading [D010 p. 29; D004 p. 194] and the co-signed prediction [D026 pp. 8–9].
  - Step 4: constants restored from the Before block (*Strong-branching iterations kept below half the node-LP iterations plus 100,000 (pp. 65–66)*): the cap and how reliability falls toward it, THESIS p. 66 = [D004 p. 80]; plus the RLT separator's budget, every 10 nodes, one round per node and ten at the root [D023 p. 13] (co-signed).
  - Say–do line: *28 cards (22 / 7 / 1), 23 studies* moved to the 08 table above.

### Before T3.6 (moved verbatim)

**Method 2: A proxy is not a payoff — split the time, then budget *(new)***

**One line**: put total time beside the local indicator, find where the time goes, cap the component in a solver-internal unit.

**Evidence**:
- Stated: full strong branching's node savings do not justify its cost (THESIS pp. 69–70; ZR 04-13 pp. 10–11). Conflict analysis pays only at moderate effort; the discard policy is a key factor (THESIS p. 181).
- Practice: ZR 05-19 splits time into basic, switching (setting up subproblems, local constraints and bounds) and conflict time: the node saving is worth about 10 % of basic time, but the analysis costs more, its largest part continuing bound-exceeding LPs to optimality to get initial conflict sets, and switching time grows with the added local constraints (pp. 15–16). The 2007 default uses conflicts for propagation only, never as LP cuts (reason not stated; *inferred*: avoids the LP-row and switching overhead of 2005), at most 10 per infeasible subproblem, with aging; the rejected variants are printed (bound-exceeding LPs cut nodes, not time; strong-branching LPs slightly worse; aggressive slower almost everywhere); result more than 10 % faster (THESIS pp. 5, 178–181). Strong-branching iterations kept below half the node-LP iterations plus 100,000 (pp. 65–66).
- Say–do consistency: ✅ stated + practised.

**Steps**:
1. Report the proxy and total time side by side per test set; a proxy gain with a time loss goes into the abstract.
2. Split the time: base solve, switching, and time inside the component, side costs included; name the dominant cost. Count the side effects node counts miss (domain reductions and cutoffs found in the component's own LPs; THESIS pp. 69–70, Gamrath pp. 57–59). Checkpoint (this skill's, *inferred* from ZR 05-19 pp. 15–16): if the component's time exceeds the base-time saving on most brackets, reject the variant as it stands.
3. List variants along the cost axis (what to analyse, how many objects to keep, how long); one column per effort level against the component switched off (THESIS Table 11.1, p. 179); count the objects produced (conflicts and their average length, ZR 05-19 Table 2, p. 17).
4. Budget in a solver-internal unit (iterations relative to node-LP iterations, objects per event, aging), not wall-clock.
5. Keep the variant positive in time across sets; print the rejected ones with numbers.

**Applies to stage**: experiment design; judging results.

**Different from standard practice**: "nodes down, time up" is a negative result until the cost is located, and the budget becomes part of the component.

**Limitations**: most of full strong branching's node reduction comes from side effects (Gamrath, DOI 10.14279/depositonce-10710, pp. 57–59), which he named but did not measure (step 2 adds the count). Time to optimality misjudges primal heuristics, which he conceded (THESIS p. 4); see the primal integral (Berthold, DOI 10.1016/j.orl.2013.08.007, not read).

### Before T3.7 (moved verbatim)

The SKILL.md lines that the T3.7 tightening (2026-11-28) shortened or moved, as they stood before it; links re-pointed to work from this folder. The shortened lines are in SKILL.md.

*Practice:*

- Practice: basic, switching and conflict time per instance with clause counts; the dominant cost (continuing bound-exceeding LPs to optimality for initial conflict sets) and the side cost (switching time growing with the local constraints) named [R004 pp. 11, 15–18]; full strong branching smallest trees and about 100 % slower, local cuts at every node −70 % nodes and +137 % time [D004 pp. 83–84, 129]; Gurobi work limits in touched non-zeros, a capped conflict pool [R021 pp. 49, 64, 66]; RLT separation cut from about half of total time to under 3 % [D023 pp. 17–18].

*Variant bullet, thesis experiment setting:*

  - ✗ A thesis's experiment setting is not the release default: the thesis's conflict runs (propagation only, ≤ 10 per infeasible node, aging) are experiment settings, and SCIP 0.90f ran with conflict analysis off [D004 pp. 192–193, 386; D010 pp. 20–21]; check the release settings before citing a default (corrected 2026-11-28).

*T3.7 fix round (2026-11-28):* the remedy *check the release settings before citing a default* is back in SKILL.md; the date note stays here.

*Variant bullet, abstract rule:*

  - ✗ (co-signed) Step 1's abstract rule holds in 2005 [R004 p. 2], not in later abstracts: in 2008 the verdict rests on solved counts (33 against 34) and the time ratios stay in the table [R009 pp. 2, 10].

*Step 2:*

2. Split the time: base solve, switching, and time inside the component, side costs included; name the dominant cost (EP8). Count the side effects node counts miss (domain reductions and cutoffs found in the component's own LPs; THESIS pp. 69–70, Gamrath pp. 57–59). Checkpoint (this skill's, *inferred* from ZR 05-19 pp. 15–16; per instance it holds there on 17 of 29 (card recount) [R004 pp. 17–18]): if the component's time exceeds the base-time saving on most brackets, reject the variant as it stands.

*T3.7 fix round (2026-11-28):* step 2 is back in SKILL.md word for word, card recount included.

<a id="method-3"></a>

## Method 3: Nest the incumbents in one parameter family and sweep it

### Full-text evidence (08 §2, copied)

| Method | Cards (E / V / C) | Studies | Full or partial cards | E by period | Say–do after the full texts |
|---|---|---|---|---|---|
| M3 Nest the incumbents and sweep | 11 (5 / 7 / 0) | 10 | 11 | 2 / 2 / 1 / 0 | ✅ for 2002–2009; no written practice after 2013 |

**Method 3 · Nest the incumbents in one parameter family and sweep it**

- **Strongest practice.** The 2004 family: pseudocost, strong-branching-initialised and full strong branching as settings of one reliability parameter, the map drawn, the full grid run, each setting a point in (nodes, time), the knee named rather than the fewest-node setting, and the simplification against the 2002 rule as the result [R002 pp. 8, 11, 13, 17]. Thesis: the same family with its budget tied to node-LP iterations, the hybrid rule reducing to reliability branching at zero weights, and the product score tested against the weighted sum at five weights [D004 pp. 79–83, 85; D010 pp. 16–19]. The pump: "Note that you can obtain the original Feasibility Pump by choosing α0 = 0." [R006 p. 5].
- **Say–do update.** ✅ for 2002–2009. The co-signed 2013 parallel study keeps step 2 only (schemes as settings of one code, no sweep) [D029 p. 21]; the 2022–2025 RLT study uses single parameter values with no sweep (card note; [D023 pp. 13, 18]). No Gurobi-era text exercises the method.
- **Variants.** The 2002 rule is a bundle of changes evaluated as a whole [R001 pp. 8–10]; one setting against the endpoint, no grid [R006 p. 6]; one-parameter sweeps whose default is set conservatively, not at a knee [R013 pp. 28–29; D011 pp. 35–38]; a family of activity-bound computations with a chosen compromise and no sweep [D030 pp. 8–9]; a factorial over formulation choices read by per-level means [R011 pp. 5, 7–8]; an extended model row that contains the basic row at parameter zero, unremarked [D024 TR p. 19].
- **Proposed text (Limitations).** *the knee moves (dynamic by 2007 …)*: dynamic reliability settings were already run in 2004, in appendix tables only, undefined in the text, from about 1 % faster to 14 % slower than (8, 4) in geometric-mean time [R002 pp. 30–31, 37–40]. A timing-noise data point for 2004: a second run of one setting without a time limit differs by up to 7.1 % in time on single instances at identical node counts [R002 pp. 12, 18–19, 23] (neutral lesson for step 3: treat settings within timing noise of the knee as ties).

### Added in T3.6

- **Evidence condensed**: Stated → the pump sentence [R006 p. 5] (co-signed) and the ZR 04-13 abstract with THESIS p. 2 (from the old Stated line). Practice → the 2004 family, map, grid and knee [R002 pp. 8, 11, 13, 17]; the thesis family and the product score [D004 pp. 79–83, 85]. Say–do: no written practice after 2013 (08 §2).
- **Variant bullets**: the 2002 bundle [R001 pp. 8–10]; dynamic reliability in 2004 [R002 pp. 30–31, 37–40]; near-ties and timing noise [R002 pp. 13, 17, 19, 23]; later studies keep step 2 only [D011 pp. 35–38; D029 p. 21; D023 p. 13]. Not carried (kept here): the factorial over formulation choices [R011 pp. 5, 7–8], the activity-bound family [D030 pp. 8–9] and the UMTS row that contains the basic row at parameter zero [D024 TR p. 19].
- **Steps**: step 1 + the map (DM1); step 3 + EP11.
- **Limitations**: *dynamic by 2007* + *tried in 2004* [R002 pp. 30–31] (08 §3.2 item 13).
- **Fix round (2026-11-28)**:
  - Practice + the score family: the weighted-sum family holds the literature's weights and the product score beats it by 14 % [D010 pp. 16–19] (08 §2 lists it among the strongest practice).
  - Say–do: *none after 2013* → *no evidence link after 2013 (one 2014 variant, D030)*; the digests give D030 (2014) a Method 3 variant link [D030 pp. 8–9].
  - Variants: *within about ±14 % of (8, 4)* → *from about 1 % faster to 14 % slower than (8, 4)* (geometric-mean times 168.4–194.9 s against 170.5 s in the appendix tables [R002 pp. 30–31, 37–40]). The T3.6 variant bullet on the grid neighbours of the knee and on a repeated run [R002 pp. 13, 17, 19, 23] was removed from SKILL.md under the house rule on reading notes (card c01 keeps the observation); the repeated run is a second run without a time limit [R002 p. 12], and its timing-noise data point, the one the c01 operator note authorises, became a neutral lesson in step 3 [R002 pp. 12, 18–19, 23]. *⚠ Later studies keep step 2 only, with no sweep or a conservative default [D011 pp. 35–38; D029 p. 21; D023 p. 13].* → labelled co-signed, D029 with Shinano first, and D023 named as not exercising the method (card c08: single values, no sweep) [D023 p. 13].
  - Step 1 + the map's values, from the old Practice line (*0 pseudocost, 1 with strong-branching initialisation, ∞ strong branching*) with its card [R002 p. 8].
  - Say–do line: *11 cards (5 / 7 / 0), 10 studies* moved to the 08 table above.

### Before T3.6 (moved verbatim)

**Method 3: Nest the incumbents in one parameter family and sweep it *(new)***

**One line**: write the competing rules as settings of one rule, run the grid, read the knee in (nodes, time), delete what does not pay.

**Evidence**:
- Stated: reliability branching presented as a generalisation of pseudocost and strong branching (ZR 04-13 abstract, pp. 1–2, co-signed; THESIS p. 2).
- Practice: 2002 history branching had three history levels, scaling factors and adaptive parameters (ZR 02-32 pp. 6–8); 2004 keeps one reliability parameter (0 pseudocost, 1 with strong-branching initialisation, ∞ strong branching; ZR 04-13 pp. 1, 6–7); why the rest went is unstated (*inferred*: the simpler rule kept the gain). The reliability × lookahead grid is read as points; (8, 4) the knee (pp. 9–12). The objective feasibility pump reduces to the original at weight zero (ZR 05-42 p. 4). The product score was run against the weighted sum at five weights; the best weight (1/6, SIP's value) is still 14 % slower in the shifted geometric mean (THESIS pp. 3, 71).
- Say–do consistency: ✅ stated + practised.

**Steps**:
1. Find the parameter whose extremes are the incumbents.
2. Implement once; baselines are the same code with one parameter changed.
3. Sweep; plot each setting as (mean nodes, mean time); pick the knee, not the fewest nodes.
4. Delete unrewarded machinery.
5. Later tie the parameter to a budget (Method 2).

**Applies to stage**: design; experiment design.

**Different from standard practice**: baselines are inside the design, and simplification is a result.

**Limitations**: the knee moves (dynamic by 2007; SCIP now reliability 1–5, lookahead 9). Counts ignore variance (Hendel, DOI 10.1007/978-3-319-18008-3_14). A grid can miss every good value (Turner et al., DOI 10.5802/ojmo.25). The product score lacks theory and is near parity with tree-model scores (DOI 10.1007/s10107-016-1101-8; DOI 10.1007/s10107-020-01556-4). No seeds in his sweeps; alone, a coarse grid on 100–250 instances.

### Before T3.7 (moved verbatim)

The SKILL.md lines that the T3.7 tightening (2026-11-28) shortened or moved, as they stood before it; links re-pointed to work from this folder. The shortened lines are in SKILL.md.

*Variant bullet, later studies:*

  - ⚠ Later studies (co-signed; D029 Shinano first) keep step 2 only, with no sweep or a conservative default [D011 pp. 35–38; D029 p. 21]; the 2025 RLT study uses single values, no sweep [D023 p. 13].

<a id="method-4"></a>

## Method 4: Knock-out from the default, read in brackets

### Full-text evidence (08 §2, copied)

| Method | Cards (E / V / C) | Studies | Full or partial cards | E by period | Say–do after the full texts |
|---|---|---|---|---|---|
| M4 Knock-out from the default, read in brackets | 29 (15 / 16 / 9) | 24 | 28 | 1 / 4 / 5 / 5 | ✅, with three corrections (Example A.1 signs, era line, seeds) |

**Method 4 · Knock-out from the default, read in brackets**

- **Strongest practice.**
  - Thesis form: shifted-geometric-mean ratios against the default (shift 10 s and 100 nodes), counts of instances at least 10 % faster or slower, equal- and different-path blocks, the pseudo-instance-weighted total, time-outs at the limit with the bias stated [D004 pp. 16, 333, 335–336, 339–340]; all off / one off / one on alone for interacting families [D004 pp. 125, 142].
  - 2009–2010: unaffected and affected rows per set, wins at ±10 %, time-outs per side, conclusions refused on 16 and 3 affected public models and accepted on the large set [R013 pp. 24–27; D011 pp. 29–30, 33–35]: "In contrast to Table 3 and Scip we can trust these values since the overall testset is very large with a reasonable number of affected instances." [D011 p. 34].
  - 2014: the bracket table with shift 1, affected models by simplex iterations, inconsistent answers excluded: "In the discussion below, we will usually use the [10,10k] bracket, because this excludes the relatively uninteresting easy models but is still large enough to draw meaningful conclusions." [D030 p. 11].
  - 2016, the fullest written form: master-solve-only switches with the reason, no benchmark where a change acts through model size, no affected figures where both sides time out, small affected sets refused or rechecked [R021 pp. 5–6, 19, 21–22, 40, 42]: "one has to take this result with care, as a set of about 200 models is usually not large enough to measure such an impact precisely enough." [R021 p. 42].
  - 2021–2025 (co-signed): "The means were computed with a shift of 1 second (see Achterberg [1])." [D021 p. 2]; brackets [x, timelim], affected and all-optimal subsets in SCIP and the same bracket rows in Gurobi [D022 pp. 10–11, 14; D023 pp. 14–22, 26–27]; four settings for an interacting heuristic family [R017 pp. 6–7].
- **Contradictions** (details §3.1): the signs of Example A.1 [D004 pp. 335–336]; the era of the bracket form [R013 pp. 26–27; D011 pp. 33–34]; seeds and permutations in co-signed written studies [R015 pp. 13–15; D013 pp. 13–18; D029 p. 20; R018 pp. 16–17, 19–21; D023 pp. 14, 26–27]; one-instance verdicts in record-seeking parallel papers [D018 TR pp. 13–14; R020 p. 13].
- **Variants.** Earlier forms: arithmetic totals over a pairwise comparison [R001 p. 11]; totals and plain geometric means against two external solvers [R003 pp. 24–25]; plain geometric means and fails per setting [R002 pp. 17, 19]; on/off in the default with plain or floored means and both-solved subsets [R004 pp. 16–17, 19]; unshifted means with 10 % counts in solver comparisons [R009 pp. 9–10; R012 pp. 12–14]; study-specific shifts of 1, 10 and 100 in the 2009 solver comparison [D010 p. 28]. Conflict analysis is measured by adding it to a reference that lacks it, labelled "default" in the appendix [D004 pp. 193, 386]. A test set defined at 10,000 s is run at 3,600 s, so several hundred models time out on both sides of every table (card recount) [R021 p. 5]. The parallel baseline is the parallel code's own one-thread default [D029 pp. 16–17]. A classroom case changes three settings at once and credits one [R007 pp. 7, 9].
- **Say–do update.** ✅ unchanged.
- **Proposed text.** Fix the Example A.1 signs; replace the era line; reword step 7 (§3.2 items 1–3). New step after step 4, from the control-subset cluster (§4 row 5): read every node or time claim also on the subset that removes the confound it is exposed to: both-solved subsets for failures [R004 pp. 17, 19; R012 pp. 12–14; D010 p. 28]; equal-path blocks (same nodes and simplex iterations) for a pure per-node cost [D004 pp. 339–340]; the all-optimal subset for time-limit censoring [D022 p. 13; D023 p. 17]; a same-path subset across thread counts for hardware effects [D029 pp. 17, 20]; no affected figure where both sides time out [R021 p. 6]. Limitations: the written basis for *Brackets need hundreds of affected models* is [R021 p. 42].

### Variants, contradictions and proposals (08 §3, copied)

| Card(s) | Method | Claim of the card | Check | Verdict |
|---|---|---|---|---|
| D004 | M4 | SKILL.md reverses the signs of Example A.1 | text read at [D004 pp. 335–336]: the geometric mean reports a 27 % improvement for setting B, the shifted geometric and arithmetic means a 6 % and 89 % deterioration | Upheld; wording fix |
| R013, D011 (one study) | M4 era | the slower-run subsets of ≥ 10 s and ≥ 100 s exist in 2009–2010 | "The subsets cplex10s and cplex100s correspond to those instances within cplex that need at least 10s and 100s of CPU time to be solved, respectively, by the slower of the two versions, mcf and nomcf." [R013 p. 27]; [D011 pp. 33–34] | Upheld; a narrower form (three subsets, CPLEX part only, shift not stated) |
| D013 (with R015) | M4 step 7, Misreading 1 | 100 permutations per model, a variability score per instance, permuted copies and inferential tests recommended | [D013 pp. 13–18; R015 pp. 13–15]; "Performance is not deterministic. Instead, it is a random variable that can be sampled with computational experiments." [R015 p. 15] | Upheld for a co-signed library paper (16 authors); no section credited to him, the variability work credited to Danna [R015 p. 22; D013 p. 57] |
| D029, R018 (one study) | M4 step 7 | five runs of each nondeterministic configuration | [D029 p. 20; R018 pp. 16–17, 19–21] | Upheld; the repeats answer message timing in parallel runs, not seeds; Shinano first |
| D023 | M4 step 7 | permuted copies in the SCIP tables | the text names "permuted instances" in the failure counts and a table "with 4 permutations" [D023 pp. 14, 26–27] (checked in the text) | Upheld; the procedure is not described; the Gurobi part mentions neither [D023 pp. 21–22] |
| D018, R020 (one study) | M4, H5 | one instance, one run per version | [D018 TR pp. 13–14; R020 p. 13] | Upheld as a genre exception (record-seeking parallel work, co-signed); the stated reason is run cost [D018 TR p. 13] |

1. **Method 4, Practice, Example A.1.** Now *+27 % (geometric), −6 % (shifted geometric), −89 % (arithmetic)*. Replace by: −27 % with the geometric mean (setting B better), +6 % with the shifted geometric mean and +89 % with the arithmetic mean (setting B worse) [D004 pp. 335–336].

2. **Method 4, One line, era.** Now *the bracket form is in his papers from 2014 … Do not read earlier work as if it used brackets.* Replace by: the thesis (2007) reports shifted-geometric-mean ratios against the default with faster/slower counts and equal-path blocks [D004 pp. 335–336, 339–340]; a narrower bracket form, ≥ 10 s and ≥ 100 s subsets by the slower run with affected rows, wins and time-outs, appears in the 2009 report and the 2010 journal paper, in their CPLEX part, with no stated shift [R013 pp. 26–27; D011 pp. 33–34]; the full table (≥ 0, 1, 10, 100, 1,000 s, shift 1, affected by iterations) is from 2014 [D030 pp. 10–12; R021 pp. 5–6].

3. **Misreading 1, Method 4 step 7, the Activation Rules default and the Roundtable Card's blind spot** (*No written study of his has them*). Replace by: none of his sole-authored studies uses seeds or permutations [D004 p. 333; R003 pp. 24–26; R004 pp. 15–19]; co-signed written studies do in four forms: a library's variability study with 100 permutations per model [R015 pp. 13–15; D013 pp. 13–18]; five repeats of nondeterministic parallel configurations [D029 p. 20; R018 pp. 19–21]; permutations as a diversification device in racing [D017 TR pp. 10–11; R019 p. 10; D018 TR p. 6]; permuted copies in 2025 tables with no stated procedure [D023 pp. 14, 26–27]. The 2016 presolve report names one unspecified recheck: "Nevertheless, such a small set of problem instances does not provide any meaningful results, and indeed, additional tests that we have conducted showed that the speed-up in Table 23 is just an artifact of performance variability." [R021 p. 40]. The five-seed *consistent win* rule remains spoken only.

18. **Honest Boundary and Method 4, *A&W 2013 … not read*.** Its abstract is read [D028]: it names a scheme for analysing benchmark results but not its form; the co-signed 2014 and 2016 texts credit their table form to it [D030 p. 11; R021 p. 5]. The bracket form's origin is still unconfirmed in a text of its own.

### Added in T3.6

- **One line**: the era sentence (*the bracket form is in his papers from 2014 … Do not read earlier work as if it used brackets*) replaced by the corrected era (08 §3.2 item 2) [D004 pp. 335–336, 339–340; R013 p. 27; D011 pp. 33–34; D030 pp. 10–12]; the old sentence is below.
- **Evidence condensed**: Stated → the [10,10k] sentence [D030 p. 11] (co-signed) and THESIS p. 2 fn. 1 (sole). Practice → thesis protocol [D004 pp. 16, 333, 335–336, 339–340]; refusals in the Mcf paper [D011 pp. 33–35]; the 2016 rules [R021 pp. 5–6, 19, 21, 40, 42]; two codes [D023 pp. 14–22].
- **Variant bullets**: ✗ Example A.1 [D004 pp. 335–336] (08 §3.2 item 1, the reader's flag); ✗ seeds (08 §3.2 item 3) [R015 pp. 13–15; D029 p. 20; D023 p. 14]; earlier forms [R001 p. 11; R002 p. 17; D010 p. 28]; the conflict reference [D004 pp. 193, 386]. The one-instance genre exception of the record-seeking parallel papers [D018 TR pp. 13–14; R020 p. 13] sits in Heuristic 5.
- **Steps**: EP ids added to steps 1, 2 and 4; new step 4b, the control subsets (08 §2 proposed text; §4 row 5) [R004 p. 17; D004 p. 339; D023 p. 17]; step 5 + the recheck before a default changes [R021 p. 40] (EP6); step 7 *his written studies* → *his sole-authored studies*.
- **Limitations**: the written basis for *Brackets need hundreds of affected models* [R021 p. 42] (08 §2 proposed text).
- **Fix round (2026-11-28)**:
  - ✗ Example A.1: *Example A.1's signs were reversed here: −27 % geometric (B better), +6 % shifted geometric, +89 % arithmetic [D004 pp. 335–336].* → written as its lesson (fix and state the mean before the runs), signs as before.
  - Moved here from SKILL.md (era notes that change no step): *⚠ Earlier forms: arithmetic totals (2002), plain geometric means (2004–08), study-specific shifts (2009) [R001 p. 11; R002 p. 17; D010 p. 28].* and *⚠ Conflict analysis was measured by adding it to a reference without it [D004 pp. 193, 386].* (the second also stays in the conflict anatomy, Reception).
  - Step 4: the shift (the thesis's 10 s and 100 nodes [D004 p. 335]; 1 s in the Gurobi-era texts [D030 p. 11; D021 p. 2]; EP2), which the Before block gave as *Shift 10 s / 100 nodes from 19 Apr 2007 (1e98661db), 1 / 1 at Gurobi*, so that Activation Rules' *(his: Method 4)* resolves again; *affected* defined by a changed LP-iteration count [D022 p. 11; D030 p. 11] (EP4). Step 4b nested under step 4 (as *4b.* it was not a list item).
  - Step 5 + EP20 (read ≥ 1,000 s apart [R021 p. 24]), EP15 (enlarge a small affected set with generated target instances [D020 pp. 12–18]) and EP21 (judge instances no setting solves by closed gap [D011 pp. 29, 31, 33]), all co-signed (catalog).
  - Different from standard practice: *the reading rules are his increment* → the thesis form is his [D004 pp. 335–340]; brackets, affected counts and small-set refusals are co-signed from 2009–10 on [R013 p. 27; D030 p. 11; R021 p. 42] (their table form is credited to A&W 2013, abstract only [D028]; see [Honest Boundary](#honest-boundary)).
  - Limitations + *One machine*: single runs on an unloaded machine, suspicious runs rerun, up to 2 % in mean time read as noise (THESIS p. 319 = [D004 p. 333]); repeats go to the deciding comparison (*inferred*). Activation Rules' *One machine → Method 4's Limitations* pointed to text without it before the deep reading too.
  - Say–do line: *29 cards (15 / 16 / 9), 24 studies* moved to the 08 table above.

### Before T3.6 (moved verbatim)

**Method 4: Knock-out from the default, read in brackets *(deepened; see Misreadings 1–2)***

**One line**: switch the feature off in the full default, run the whole library, and read the table per time bracket with affected counts, as a ranking that does not add up. Era: the bracket form is in his papers from 2014 (RAMP 2014, ZR 16-44, credited to A&W 2013); the thesis (2007) reports shifted-geometric-mean ratios against the default with faster/slower counts (p. 2 fn. 1, p. 325). Do not read earlier work as if it used brackets.

**Evidence**:
- Stated: measured in the geometric mean relative to SCIP's default; +100 % means twice as long when disabled (THESIS p. 2 fn. 1). Cuts: all off, one off, one on alone, after Bixby et al. 2000 (DOI 10.1007/978-0-387-35514-6_2; THESIS p. 111). Brackets by the slower run, discussion on ≥ 10 s, models ≥ 10 % faster or slower counted, affected models reported (ZR 16-44 pp. 3–4, co-signed; form credited to A&W 2013, not read).
- Practice: 244 instances × 115 settings = 28,060 runs (THESIS p. 2). Reductions off in the master solve only, on in sub-MIPs; no benchmark for fixed-variable removal because model size drives heuristic decisions (ZR 16-44 pp. 3, 19). Faster/slower counts and an equal-path split (same nodes and iterations) (THESIS p. 325). Example A.1: one data set gives +27 % (geometric), −6 % (shifted geometric), −89 % (arithmetic) (pp. 321–322). Shift 10 s / 100 nodes from 19 Apr 2007 (1e98661db), 1 / 1 at Gurobi. Time-outs at the limit, bias stated (p. 319); single-class sets as three pseudo-instances each, so the total counts 105 instances + 21 pseudo-instances; geometric means and totals go to the appendix tables (p. 322); 48 affected SOS models called too few (ZR 16-44 p. 17); four targets (first feasible, 10 %, 1 % gap, optimality) on 8,611 models (MIPW 2025 slides 25–26).
- Say–do consistency: ✅ stated + practised.

**Steps**:
1. Reference = full default; for interacting families, all off / one off / one on alone.
2. Switch off in the main solve only; if that changes other components through model size, say no clean benchmark exists.
3. One time limit for the whole library; time-outs at the limit, bias stated.
4. Per bracket of the slower run (≥ 0, 1, 10, 100, 1,000 s): models, time-outs per side, counts ≥ 10 % faster and slower, shifted-geometric-mean ratios for time and nodes (shift stated), the affected subset.
5. Discuss on ≥ 10 s; refuse conclusions on small affected sets.
6. Read percentages as a ranking; report non-additivity and indirect effects as findings.
7. Add seeds or permutations, which his written studies lack, and say so.

**Applies to stage**: experiment design; judging; writing.

**Different from standard practice**: knock-out is common *(known)*; the reading rules are his increment.

**Limitations**: descriptive statistics only; time-limit censoring underestimates long-horizon speed-ups (Koch et al., DOI 10.1016/j.ejco.2022.100031); Gurobi sets are private. Brackets need hundreds of affected models; with a few dozen, use the thesis form (One line) plus seeds.

### Before T3.7 (moved verbatim)

The SKILL.md lines that the T3.7 tightening (2026-11-28) shortened or moved, as they stood before it; links re-pointed to work from this folder. The shortened lines are in SKILL.md.

*Practice:*

- Practice: the thesis protocol, time-outs at the limit with the bias stated [D004 pp. 16, 333, 335–336, 339–340]; verdicts refused on 16 and 3 affected models, accepted on a large set [D011 pp. 33–35]; master-solve-only switches, small sets refused or rechecked [R021 pp. 5–6, 19, 21, 40, 42]; brackets with all-optimal subsets in two codes [D023 pp. 14–22].

*Variant bullet, Example A.1:*

  - ✗ Fix and state the mean before the runs: in Example A.1 one data set reads −27 % by the geometric mean (B better), +6 % by the shifted geometric mean and +89 % by the arithmetic mean (B worse) [D004 pp. 335–336] (signs corrected 2026-11-28).

<a id="method-5"></a>

## Method 5: Instrument first

### Full-text evidence (08 §2, copied)

| Method | Cards (E / V / C) | Studies | Full or partial cards | E by period | Say–do after the full texts |
|---|---|---|---|---|---|
| M5 Instrument first | 26 (18 / 9 / 1) | 22 | 25 | 4 / 5 / 4 / 5 | ✅; the test-set selector changes by era |

**Method 5 · Instrument first**

- **Strongest practice.**
  - Thesis: two years of code before research on SIP's source; SCIP begun in October 2002 with SIP's ideas; the test set selected with a frozen SCIP 0.82d and Cplex 10.0.1, final runs with 0.90f; versions on request and logs on the web; leak detection in the memory debugging mode [D004 pp. 9, 20, 65, 333–334, 340].
  - Complete solves from plug-ins with a minimal correctness contract: "This feasibility test already suffices to produce a correct algorithm for solving CIPs with constraints of the supported type." [R003 p. 9], restated in 2008 and 2009 [R009 p. 5; D010 pp. 7–8]; assertions make up 20 % of statements [D010 p. 16].
  - Reference solvers pick the test sets by stated effort windows and run with matched tolerances [R003 p. 24; R004 pp. 16–17]; the 2009 comparison set is chosen with CPLEX and CBC and drops instances with disagreeing optima [D010 p. 21]; instances with wrong answers are excluded and named [R012 pp. 12–14].
  - Library scale (co-signed): known optima, provenance and status published [R005 pp. 3, 11, 13]; run scripts, parsers, an exact solution checker and reliable primal bounds [R015 pp. 7, 10–12; D013 pp. 2, 10–13]; numbered suitability criteria with exclusion counts and a cross-solver consistency check [D021 pp. 20, 22–23, 25–26].
  - The detector is checked against the known original networks before any speed test [D011 pp. 20–22; R013 pp. 17–19]; correctness on graphs with published optima before scaling, easy graphs kept for that purpose [D020 pp. 11–13, 17]; a shared-memory build as the debugging environment for the distributed one, and a deterministic parallel mode wanted for development [D029 pp. 11, 16, 29–30].
  - Stated (co-signed): "Just believing the result of some unknown software without even the possibility to check what actually happened will not qualify for a scientific experiment." [R007 p. 3].
- **Contradiction (era).** In 2002 the test set is filtered by the code under study [R001 p. 10].
- **Variants.** The selector by era (§3.2 item 7); a library only half rule-selected (removal by rule, admission by goals) [R005 pp. 3, 5]; a benchmark set chosen by consensus under hard and soft requirements [R015 p. 7]; the whole sequential solver as the parallel unit, so that its progress carries over [R014 pp. 2, 5, 11–12; R020 p. 4; D018 TR p. 4; D014]; the explicit *sequential solver first* sentences appear only in the April 2014 revision [R019 pp. 3–4, 14, 17; D017 TR pp. 4–5, 20]; the 2020 rewrite weights what parallelization changes in the algorithm [R022 pp. 5–6, 19, 22]; a model published before any instance or harness exists, in co-signed group work before SCIP [D024 TR pp. 20, 22]; the build stated exactly and failures counted, but the test set selected by the detector under study [D023 pp. 13–14].
- **Say–do update.** ✅ unchanged.
- **Proposed text.** Replace *an older frozen version picks the test set* in the One line by the thesis-specific statement plus the era list (§3.2 item 7). Step 1 variant from §5 D. Step 4 widened by §5 E (every instrument, not only derived objects).

### Variants, contradictions and proposals (08 §3–§5, copied)

| Card(s) | Method | Claim of the card | Check | Verdict |
|---|---|---|---|---|
| R001 | M5 | 2002 test set filtered by the code under study | [R001 p. 10]; the CPLEX check on the excluded instances partly offsets it | Upheld as an era note |

7. **Method 5, the test-set selector.** Holds for the thesis only [D004 pp. 333–334]. By era: the code under study in 2002 [R001 p. 10]; a reference solver with an effort window in 2004–2005 [R003 p. 24; R004 p. 16]; two other solvers in 2009 [D010 p. 21]; the code family itself at Gurobi [D030 p. 11; R021 p. 5]; consensus under hard and soft rules for the 2010 library benchmark [R015 p. 7]; a published selection model for the 2017 library [D021 pp. 24–36]; the detector under study in 2025 [D023 p. 13].

**D. Method 5 step 1 and Method 6 step 3 variant (co-signed) · Delegate to the host**

- **One line**: write only the input the host's existing routine lacks, or run the unmodified host as the unit, so that validity and the host's future progress come for free; say in the paper which part is yours.
- **Cards**: only the aggregation weights and multipliers are computed, bound substitution and rounding are the solver's c-MIR [D011 pp. 3, 23]; unmodified SCIP processes under a coordinator [R014 pp. 2, 5; D014]; the solver and the communication library as exchangeable classes [R020 p. 4; D018 TR p. 4]; lazy rows only for correctness, the host solver's cuts kept and not competed with [D020 pp. 9–11]; a parallel CPLEX extension [D006] (abstract, weak).
- **Checks**: §4 row 2. All sources are co-signed; label it so.

**E. H4 widened · Check every instrument against ground truth before measuring with it**

- **One line**: the debug solution checks derived objects; extend the same test to every instrument: a detector against known structures, a checker in exact arithmetic, a feature space against known groups, a new method against published optima.
- **Cards**: the detector against the known original networks, with and without presolve, failures named with causes [D011 pp. 21–23; R013 pp. 17–19]; floating-point LP bases rechecked in rational arithmetic [R005 pp. 5–6]; returned solutions checked in exact arithmetic against the original file, primal values made reliable by an exact LP re-solve [R015 pp. 8–11; D013 pp. 10–12, 43; D021 pp. 22–23]; a cross-solver consistency check with inconsistent instances excluded and counted [D021 p. 23]; the feature space shown to recover the model groups [D021 p. 37]; correctness on graphs with published optima against two formulations before any scaling study [D020 pp. 11–13]; the lack of a reference implementation named as the debugging obstacle [D026 p. 17].
- **Checks**: §4 row 7. Co-signed sources except the debug solution itself (practice only).

### Added in T3.6

- **One line**: *an older frozen version picks the test set* → *a rule outside the code under study picks the test set (in the thesis an older frozen version with CPLEX [D004 pp. 333–334])* (08 §3.2 item 7).
- **Evidence condensed**: Stated → THESIS p. ix (as before) and the co-signed 2006 sentence [R007 p. 3]. Practice → [D004 pp. 20, 333–334]; [R003 p. 9; D010 pp. 7–8]; [D010 p. 21]; libraries [R005 pp. 3, 11; R015 pp. 10–12].
- **Variant bullets**: ✗ 2002 [R001 p. 10]; the selector by era [R003 p. 24; R021 p. 5; D021 pp. 24–36; D023 p. 13]; the unmodified solver as the parallel unit [R014 p. 2] (08 §5 D); the 2002 group model [D024 TR pp. 20, 22].
- **Steps**: step 1 + the co-signed variant of 08 §5 D (DM6) [D011 p. 3]; step 2 + the first commit 147d53683 (from the old Practice line); step 3 + DM8; step 4 widened by 08 §5 E [D011 pp. 21–23] (EP16, EP17); step 5 + `cmpres.awk` (1dbb9bbf0) and the thesis rule [D004 p. 334] (EP10).
- **Fix round (2026-11-28)**:
  - Moved here from SKILL.md: *⚠ (co-signed) The unmodified solver as the parallel unit, so its progress carries over [R014 p. 2].* (ParaSCIP, Shinano first, no role stated: nothing there is claimed for him alone, and the bullet gave the user no step) and *⚠ A 2002 group model published before any harness existed [D024 TR pp. 20, 22].* (card c2-01: co-signed group work in another genre, before SCIP, so no counter-example to his solver practice).
  - Steps 1 and 4: the delegate-to-the-host and ground-truth parts labelled *co-signed, shared practice* (08 §4 rows 2 and 7: exclusivity ✗).
  - Step 5: *575 → 244 in five steps [D004 p. 334]* → the five steps written out, from the Before block's selection rule (THESIS p. 320 = [D004 p. 334]).
  - Say–do line: *26 cards (18 / 9 / 1), 22 studies* moved to the 08 table above.

### Before T3.6 (moved verbatim)

**Method 5: Instrument first *(deepened)***

**One line**: the solver, its harness and its comparison tools exist before the study, and an older frozen version picks the test set.

**Evidence**:
- Stated: two years of coding to get a basis for the actual research; research on branching needs the source of a state-of-the-art solver, and SIP spared him reinventing the wheel (THESIS p. ix).
- Practice: the first SCIP commit (23 Oct 2002, 147d53683) holds test lists, known optima, a run script with a 3,600 s limit, SIP's checking report generator and a CPLEX run script. 0.2 (26 Mar 2003) solves complete problems with no special components (3c603242f). Debug solution 2005 (67238f422; H4). `cmpres.awk` (2006, 1dbb9bbf0) averages only over instances no solver failed on, failures counted. SCIP 0.82d frozen to select the thesis set, final runs with 0.90f (THESIS pp. 319–320; the purpose is *inferred*). The selection rule (p. 320), on publicly available sets with their origins listed: CPLEX 10.0.1 and SCIP 0.82d, with and without conflict analysis, on all 575 instances; drop any that neither solves in 1 h; remove coral's duplicates of milp; on coral and mik drop those both solve within 10 s, then thin coral by removing every second instance in CPLEX-time order; drop trivial alu instances and those too hard numerically; 244 remain. Memory-outs (1.5 GB) count as time-outs with nodes scaled; 180 of 28,060 runs hit it (p. 319). CPLEX reference runs use SCIP's gap tolerances (mipgap 0, absmipgap 10⁻⁹; p. 320).
- Say–do consistency: ✅ stated + practised.

**Steps**:
1. Start from a state-of-the-art code you can read; carry over its ideas and harness.
2. Before any feature: test lists, known optima, a time-limited run script, a checking report, a reference-solver script.
3. Reach complete solves with no special components; add components as plug-ins.
4. Check every derived object against a known optimum (H4).
5. Before the big study: the comparison tool, a frozen selector version, then the final runs.
6. Publish once the platform carries research.

**Applies to stage**: problem choice; experiment design.

**Different from standard practice**: harness and selector precede the feature; test-set choice is separated from the code under study.

**Limitations**: steps 1, 3, 6 needed a funded position and an advisor who accepted two years without papers; not an early-career default today. The platform exists now (SCIP); steps 2, 4, 5 remain.

### Before T3.7 (moved verbatim)

The SKILL.md lines that the T3.7 tightening (2026-11-28) shortened or moved, as they stood before it; links re-pointed to work from this folder. The shortened lines are in SKILL.md.

*Practice:*

- Practice: SCIP begun in October 2002 with SIP's ideas, the thesis set chosen by a frozen 0.82d and CPLEX 10.0.1 [D004 pp. 20, 333–334]; a feasibility check alone makes a handler correct [R003 p. 9; D010 pp. 7–8]; other solvers choose the 2009 set, disagreeing instances dropped [D010 p. 21]; libraries with optima, scripts and an exact checker (co-signed) [R005 pp. 3, 11; R015 pp. 10–12].

<a id="method-6"></a>

## Method 6: Import at the data-structure level, let the test decide

### Full-text evidence (08 §2, copied)

| Method | Cards (E / V / C) | Studies | Full or partial cards | E by period | Say–do after the full texts |
|---|---|---|---|---|---|
| M6 Import at the data-structure level | 17 (10 / 9 / 0) | 16 | 14 | 2 / 7 / 1 / 0 | ✅ for 2003–2013; later imports come from network design and global optimization |

**Method 6 · Import at the data-structure level, let the test decide**

- **Strongest practice.** SAT conflict analysis mapped onto MIP objects: bound changes as conflict-graph vertices, infeasible LPs explained along the dual ray, each constraint class with its own reverse propagation [R004 pp. 9–14; R008 pp. 7–9; D004 pp. 185–192]; watched literals in the set-covering handler days after Novikov's primer, the replacement rule re-decided by test [D004 pp. 10, 107–108]; SAT restarts re-decided for MIP and imported in restricted form with a stated reason: "In our implementation, a restart is performed if at least 5 % of the integer variables have been fixed." [R012 p. 11], with the reason that root fixings can trigger more presolving at the cost of a second root LP [R012 p. 11], the same rule in 2008 and 2009 [R009 p. 9; D010 pp. 12–13]; SatZ's lookahead turned into a history value combined with VSIDS [D010 p. 17; D004 p. 81]; SAT restarts in chip search replaced by a jump to a best node every 100 depth-first nodes, because the LP work would be lost [D004 p. 311]; CP propagation and SAT conflicts as plug-in types [R003 pp. 9–10, 13]. Abstracts: CP constraints and SAT techniques in a MIP framework [D007]; one branching rule from CSP, MIP and SAT criteria [D009]; SAT implied literals carried by clique and implication tables MIP solvers already keep, tested in CPLEX 12.5 [D016].
- **Say–do update.** ✅ for 2003–2013. No Gurobi-era evidence link; the later imports run from network design or global optimization into MILP.
- **Variants.** In 2005 general integers were kept out of conflicts and the SAT pieces ran together, not one at a time [R004 pp. 14–15]; the 2008 checker names only 1-FUIP, change unexplained [R009 pp. 9, 13]; network-design cut theory mapped onto the solver's c-MIR [D011 pp. 3, 10, 25–28]; RLT brought into MILP with new data structures, each piece tested alone, in two codes [D022 pp. 3–14; D023 pp. 7–8, 10, 15–21]; an information-theory device (Kraft's inequality) turned into a knapsack row in group modelling, no test [D024 TR pp. 6, 11, 15]; the direction reversed, MIP warm-start practice taken into an interval-methods code and measured alone [D026 pp. 6–7, 15, 39]; Gurobi 6.5's conflicts are dense Farkas rows without backward propagation, worth 5 % against his 12 % in SCIP, while watched literals and a symmetry tool are reused where they map one to one [R021 pp. 47, 51, 63–64]; counting derived from the SAT side and re-derived for branch-and-cut [R010 p. 4].
- **Proposed text.**
  - Step 3 variant from §5 D (map the import onto the host's existing routine and compute only its input).
  - Step 4 mechanism: predict non-transfer from the state the import would discard (warm-start bases, LP work), then confirm by test [D004 pp. 174, 311; R012 p. 11].
  - One design rule for CP imports, from one project (chip verification): count a linearization's rows and auxiliary variables before adding it, and leave what the LP cannot carry to propagation (a 64-bit shift-left would need 30,944 inequalities and 20,929 auxiliary variables) [R009 p. 12; D010 p. 34; R008 pp. 6–7]; the thesis states the same rule [D004 p. 19] and the 2008 abstract the split [D007].
  - Limitations: Hooker's SIMPL is cited by 2004 [R003 p. 26], so *unaware* holds for the start only; step 4 (test each habit alone) is practised from the thesis on, not in 2005 [R004 p. 15; D004 pp. 192–195].

### Added in T3.6

- **Evidence condensed**: Stated → THESIS p. x and INT 2023 (as before), plus the co-signed restart sentence [R012 p. 11]. Practice → conflict analysis on MIP objects [R004 pp. 9–14; D004 pp. 185–192]; restarts kept after the root [R012 p. 11]; the chip-search jump [D004 p. 311]; implied literals [D016] (abstract).
- **Variant bullets**: 2005 form [R004 pp. 14–15]; Gurobi 6.5's Farkas rows [R021 pp. 63–64]; later imports [D011 pp. 25–28; D023 pp. 15–21]; the reversed direction [D026 pp. 6–7]. Not carried (kept here): the 2008 checker's 1-FUIP only [R009 pp. 9, 13], the Kraft-inequality knapsack row [D024 TR pp. 6, 11], counting re-derived [R010 p. 4].
- **Steps**: step 3 + DM12, the linearization rule (DM11) [R009 p. 12; D010 p. 34] (08 §2 proposed text); step 4 + the non-transfer mechanism (DM13) [D004 pp. 174, 311].
- **Limitations**: *unaware of Hooker's parallel work* holds for the start only; SIMPL is cited by 2004 [R003 p. 26] (08 §2 proposed text).
- **Fix round (2026-11-28)**:
  - Say–do: *no Gurobi-era link* → *no Gurobi-era evidence link (variant links R021, D022, D023 …)*: the digests give R021 (2016), D022 (2023) and D023 (2025) Method 6 variant links. The bullet *⚠ Later imports come from network design and global optimization, each piece tested alone [D011 pp. 25–28; D023 pp. 15–21].* merged into that line.
  - Reversed direction: *⚠ Reversed: MIP warm starts taken into an interval-methods code [D026 pp. 6–7].* → names the part the text calls "Achterberg's heuristic" (DM16; card c03: the one part of D026 attributable to him).
  - Step 3: the linearization rule also cites the thesis, which states it alone [D004 p. 19], beside the co-signed 2008 report [R009 p. 12].
  - Say–do line: *17 cards (10 / 9 / 0), 16 studies* moved to the 08 table above.

### Before T3.6 (moved verbatim)

**Method 6: Import at the data-structure level, let the test decide *(deepened)***

**One line**: have a practitioner explain the technique down to its data structure, put the smallest piece in within days, generalise the rest to MIP objects, test each imported habit separately.

**Evidence**:
- Stated: Yakov Novikov explained conflict analysis and two watched literals; within days the watched literals were in the set-covering handler, within three weeks conflict analysis was generalised to MIP (THESIS p. x; INT 2023 30:45–32:18). SAT restarts periodically; for MIP only after the root was better (THESIS p. 4). Turner's Gomory-violation criterion helped a little in Gurobi and became a tie-breaker (INT 2023 55:06–56:38, caption).
- Practice: `conflict.c` first appears 13 Aug 2003 with a zChaff-like header (6748acb5f). Tree restarts at 10 % or 5 % fixed integers were inferior; the logs showed fixings come too late, and he writes that other criteria would have to be invented (THESIS p. 163). Conflicts moved from LP cuts (ZR 05-19 p. 14) to propagation with bound disjunctions (THESIS p. 179).
- Say–do consistency: ✅ stated + practised.

**Steps**:
1. Get the technique explained by a practitioner, down to its data structure.
2. Put the smallest piece in within days where it maps one to one.
3. Generalise to MIP objects (infeasible LPs explained by duals; general integers by bound disjunctions).
4. Test each habit alone; expect the source field's default not to transfer.
5. Print what failed; name the next techniques as future work (ZR 05-19 p. 18: faster derivation of conflicts from infeasible LPs; SAT clause-database management).
6. Check parallel work before claiming novelty (his weak step).

**Applies to stage**: design; problem choice.

**Different from standard practice**: he moves the data structure and re-decides every setting by test.

**Limitations**: clause-based conflicts are a weak proof system; cut-based analysis falls back on his in about 19 % of calls on MIPLIB 2017 (Mexi et al., arXiv:2410.15110v2, pp. 18–19). Successors answered the restart question with tree-size estimates (DOI 10.1609/aaai.v33i01.33011427). He started CIP unaware of Hooker's parallel work (INT 2023 1:21:28–1:22:29).

### Before T3.7 (moved verbatim)

The SKILL.md lines that the T3.7 tightening (2026-11-28) shortened or moved, as they stood before it; links re-pointed to work from this folder. The shortened lines are in SKILL.md.

*Practice:*

- Practice: bound changes as conflict-graph vertices, infeasible LPs explained along the dual ray [R004 pp. 9–14; D004 pp. 185–192]; restarts kept only after the root, since root fixings trigger more presolving [R012 p. 11]; chip search jumps to a best node instead of restarting, to keep the LP work [D004 p. 311]; implied literals carried by existing clique tables [D016].

*Say–do:*

- Say–do: ✅ stated + practised for 2003–2013; no Gurobi-era evidence link (variant links R021, D022, D023: co-signed imports from network design and global optimization, each piece tested alone [D011 pp. 25–28; D023 pp. 15–21]).

*Step 5:*

5. Print what failed; name the next techniques as future work (ZR 05-19 p. 18: faster derivation of conflicts from infeasible LPs; SAT clause-database management).

<a id="workflows"></a>

## Stage workflows

### Added in T3.6

Technique ids and cards per step; no new workflow (08 proposes none).
- **A** step 5 (new): a known strong technique general solvers miss or cannot afford [D011 p. 3; D023 p. 3]; card evidence: the Mcf paper names the two reasons c-MIR misses network cuts [D011 p. 3]; the RLT paper makes separation cost the problem [D023 pp. 3, 17–18]. Both co-signed.
- **B**: step 1 + DM1; step 3 + PD8 and DM2; step 5 (new) the NP-hard exact sub-decision (Method 2 step 2b; PD1) [R004 p. 11; D004 p. 188].
- **C**: step 1 + EP17 [D011 pp. 21–23]; step 2 + EP10 [D021 pp. 25–26]; step 3 + EP7 [D004 p. 142; R017 pp. 6–7]; step 4 + EP18 [D029 p. 20; R018 pp. 19–21] (co-signed, Shinano first); checkpoint + [D010 p. 21] (other solvers choose, disagreeing instances dropped and counted; also [R012 p. 13]).
- **D**: step 2 + control subsets (EP5) [D004 pp. 339–340; D023 p. 17]; step 3 + overlap explains small knock-outs [R021 pp. 8, 61–62]; step 4 + the answer-type split (H8) [R004 pp. 16–19]; step 5 (new) two codes (EP14) [D022 p. 14; D023 pp. 21–22].
- **S**: step 3 + Method 2 step 2a.
- **E**: step 1 + WM1 [D004 pp. 16, 83]; step 2 + WM2 [R004 p. 2; D023 pp. 15–16]; step 3 + WM8 [D023 p. 13; R011 p. 5].
- **Fix round (2026-11-28)**: B step 1 + the score devices DM3 [D004 pp. 76, 81; D010 p. 18] and DM4 [R001 pp. 8–9] (co-signed). C step 2: *weight single-class sets (Methods 4, 5)* → each single-class set counts as three pseudo-instances in the total (EP3) [D004 p. 336], the value the Before block of Method 4 gave (p. 322), since neither method says it any more. C step 4: *repeat nondeterministic runs, count instances solved in all (EP18, co-signed)* removed from SKILL.md (back to the pre-synthesis step): a ParaSCIP practice with Shinano first, which 08 §10 item 5 admits only as variant notes on Misreading 1, H5 and the Roundtable Card; EP18 stays in the catalog.

### Before T3.6 (moved verbatim)

**Stage Workflows**

**Workflow A: Problem choice**

**Input**: a topic, or a list of things that are slow or wrong.

**Steps** (his documented sources):
1. A misbehaving named instance (H5) or a failed reproduction (H6).
2. An important, under-published engineering topic (taste 7).
3. A neighbouring-field technique explained by a person (Method 6).
4. An application whose partner delivers data early (single project, THESIS p. ix); what users ask for (WEB 9.5 0:16:55; team).

**🔴 Checkpoint**: stop without a state-of-the-art solver you can change, or without test data. Ask whether the result could ever pass the default gate (Method 1).

**Output**: trigger, solver, test sets and target class in one paragraph; add a literature check, which his own routine lacks.

**Workflow B: Idea and design**

**Input**: an idea for a component.

**Steps**:
1. Incumbents as special cases (Method 3).
2. Imports at the data-structure level (Method 6).
3. Detector and no-op path (Method 1); budget variable (Method 2).
4. A learned model → extract and hand-code its feature (H1).

**🔴 Checkpoint**: if the incumbents are not parameter settings, or the rule needs undetectable information, redesign before running anything.

**Output**: a parameterised rule, its detector, its budget.

**Workflow C: Experiment design and execution**

**Input**: the component inside a full solver.

**Steps**:
1. Harness, known optima, reference-solver script (Method 5); debug solution on (H4).
2. Test set by a stated rule from a frozen version; weight single-class sets (Methods 4, 5).
3. Knock out from the default, main solve only (Method 4); baseline at its best, equal tolerances (H3).
4. Identical unloaded machines, suspicious runs rerun (THESIS p. 319); add seeds.

**🔴 Checkpoint**: stop on any wrong answer: a cut that produced a wrong optimum was removed (variable-bound MIR after gesa2, 83d0d3f01). Exclude, and count, models on which versions disagree.

**Output**: the Method 4 table; per-instance tables in an appendix.

**Workflow D: Judging results**

**Input**: the tables.

**Steps**:
1. Time beside the proxy; split, name the dominant side cost, budget (Method 2).
2. ≥ 10 s bracket, affected counts, small sets refused (Method 4).
3. Default gate (Method 1); non-additivity as a finding.
4. Metric wrong for the user's goal → change it and rerun (H8); revert what is not good overall (H9).

**🔴 Stop rule**: any wrong answer, or disagreement with a known optimum, stops the judgement until fixed (H4; Workflow C checkpoint); nodes down and time up is negative until the cost is located; a gain on a few dozen affected models is no conclusion; one class up and others down is a parameter, not a default.

**Output**: per feature, default on / default-off parameter / rejected, with numbers.

**Workflow S: Stuck project**

**Input**: a component tweaked for weeks without a time gain, or wins and losses that swap between tweaks.

**Steps** (this skill's ordering of his methods, *inferred*; stop at the first step that explains the stall):
1. Correctness and numerics: debug solution on, tolerances checked (H4, H7). Fix any wrong answer before more tuning.
2. Sets, not instances: on a few dozen models, or only those that moved, switch to a rule-selected set; read the ≥ 10 s bracket and affected count (H5, Method 4). Swapping wins and losses on a small set are noise until seeds show otherwise.
3. Split the time (Method 2): if the component's own time eats the gain, try a budget variant, not another score tweak.
4. Class split (Method 1): wins on one class, losses elsewhere → a detector or a default-off parameter.
5. Try the opposite once (H9).

**🔴 Stop rule**: after steps 1–5, a loss or neutral result on the ≥ 10 s bracket of a rule-selected set is a result: default-off parameter or rejected, rejected variants printed with numbers (H10; THESIS pp. 163, 178–181), written up (Koch's advice, THESIS p. x). No sixth tweak.

**Output**: the step that explained the stall, the verdict, the next executable step.

**Workflow E: Writing and reporting**

**Input**: verdicts and tables.

**Steps**:
1. End each section with its computations; summary tables against the default, detail and protocol in appendices (THESIS pp. 319–378).
2. The loss in the abstract (H10); exclusions, rules and test-set origins listed (ZR 02-32 p. 9; THESIS p. 320); the exact formulation (H6).
3. Label unsupported claims (THESIS pp. 74, 140), hedge novelty (p. 71), name independent discovery (p. 165), list open questions (ZR 16-44 p. 65).

**🔴 Checkpoint**: when the next 10 % competes with writing, write: Koch's advice, which he accepted (THESIS p. x).

**Output**: auditable tables; negative results in the same form as positive ones.

**Stages without evidence**

The last routing row (Honest Boundary); no reply or erratum to critics was found.

<a id="heuristic-1"></a>

## Heuristic 1: Hand-code what the learner leans on

### Full-text evidence (08 §2.7, copied)

- **H1 Hand-code what the learner leans on.** The only written trace is the thesis acknowledgement that neural networks learned branching in his computer-science master's thesis on SIP [D004 p. 9]; the 2002 report presents the rule as a modification of pseudocost branching, with no learning experiment in the text [R001 p. 2]. Unchanged (talk-based).

### Added in T3.6

- One sentence: in print only the thesis acknowledgement [D004 p. 9].
- Fix round (2026-11-28): the Gurobi decision-tree case labelled *team, caption* (Voices: talks give his account, not verified code behaviour).

### Before T3.6 (moved verbatim)

1. **Hand-code what the learner leans on** *(new)*: if a learned model works, implement the feature it relies on. Case: in 2000–2001 several learners inside SIP all pointed to one history value; he kept it and dropped the learning (ORIGINS 2022 slides 6–7; INT 2023 23:35–25:39), which became ZR 02-32. At Gurobi, decision trees for LP dualisation and simplex choice, then hand-coded (WEB 9.1 0:59:59; closed code).

### Before T3.7 (moved verbatim)

The SKILL.md lines that the T3.7 tightening (2026-11-28) shortened or moved, as they stood before it; links re-pointed to work from this folder. The shortened lines are in SKILL.md.

*Heuristic 1:*

1. **Hand-code what the learner leans on** *(new)*: if a learned model works, implement the feature it relies on. Case: in 2000–2001 several learners inside SIP all pointed to one history value; he kept it and dropped the learning (ORIGINS 2022 slides 6–7; INT 2023 23:35–25:39), which became ZR 02-32. At Gurobi, decision trees for LP dualisation and simplex choice, then hand-coded (WEB 9.1 0:59:59; team, caption; closed code). In print only the thesis acknowledgement [D004 p. 9]. ([ledger](#heuristic-1))

*T3.7 fix round (2026-11-28):* *which became ZR 02-32* is back in SKILL.md, so that *in print only the thesis acknowledgement* reads as the trace of the learning experiment, not of the rule (08 §2.7 above); the Gurobi decision-tree case stays here.

<a id="heuristic-2"></a>

## Heuristic 2: Measure the cheap rule against its oracle

### Full-text evidence (08 §2.7, copied)

- **H2 Measure the cheap rule against its oracle.** Source correction: the per-node measurement (score and position quotients over the whole tree and the top ten levels) is in the 2002 report only [R001 pp. 13–14]; the 2004 pages SKILL.md cites only frame the rules as estimates of full strong branching [R002 pp. 5–6]. Variant: bracket the rule between a floor and the oracle; random and most-infeasible branching take 923.6 s and 938.0 s in geometric mean against 170.5 s for reliability (8, 4) and 504.4 s for full strong branching [R002 p. 17]; most-infeasible is called not better than random [R002 p. 5].

### Added in T3.6

- Source correction: ZR 02-32 pp. 12–13 kept, with its card pages [R001 pp. 13–14]; ⚠ ZR 04-13 only frames the rules as estimates of full strong branching [R002 pp. 5–6] (08 §3.2 item 9). The floor-and-oracle variant [R002 p. 17] stays here and in taste warning 3.
- If T3.7 needs a heuristic slot, 08 §5 proposes merging H2 into Method 3, whose family holds full strong branching as its ∞ end [R002 p. 8].

### Before T3.6 (moved verbatim)

2. **Measure the cheap rule against its oracle** *(new)*: at every node solve all candidates and record how close the chosen score and rank come to full strong branching (ZR 02-32 pp. 12–13; ZR 04-13 pp. 4–5).

### Before T3.7 (moved verbatim)

The SKILL.md lines that the T3.7 tightening (2026-11-28) shortened or moved, as they stood before it; links re-pointed to work from this folder. The shortened lines are in SKILL.md.

*Heuristic 2:*

2. **Measure the cheap rule against its oracle** *(new)*: at every node solve all candidates and record how close the chosen score and rank come to full strong branching (ZR 02-32 pp. 12–13) [R001 pp. 13–14] (EP12); ⚠ ZR 04-13 only frames the rules as estimates of it [R002 pp. 5–6]. ([ledger](#heuristic-2))

<a id="heuristic-3"></a>

## Heuristic 3: Fair yardstick

### Full-text evidence (08 §2.7, copied)

- **H3 Fair yardstick.** More evidence: matched gap tolerances [R001 p. 11; R003 p. 24; R004 p. 16]; the original authors' parameters and instances [R006 p. 6]; the same LP solver and probing switched off where only one code uses it heavily [R011 p. 5]; the strongest of several SAT solvers [R008 p. 11; D004 pp. 313, 317]; only the MIP part compared [D004 pp. 334, 391; D010 p. 29]; identical simplified inputs for every method [D020 pp. 12, 18]; per-solver clusterings against solver bias [D021 pp. 35, 38]. Variants: all solvers at defaults without equalized tolerances [R009 p. 9]; the parallel code's own one-thread default as baseline, the sequential column printed beside it [D029 pp. 16–17]; each code measured only against itself, cross-code numbers declared not comparable [D022 p. 14; D023 p. 21].

### Added in T3.6

- EP19; ⚠ later all solvers at defaults [R009 p. 9]. The other variants (the parallel code's own one-thread baseline [D029 pp. 16–17]; each code only against itself [D022 p. 14; D023 p. 21]) are in Inner Tensions and here.
- Fix round (2026-11-28): the case + CPLEX 10.0.1 at SCIP's gap tolerances, mipgap 0 and absmipgap 10⁻⁹ (THESIS p. 320 = [D004 p. 334]), the values the Before block of Method 5 gave.

### Before T3.6 (moved verbatim)

3. **Fair yardstick** *(new)*: baseline at its best, equal tolerances, print the loss. Case: the strongest of MiniSat 1.14, Siege v4 and zChaff chosen, Siege's time reported where it wins (THESIS pp. 299, 303); the pump run with its authors' parameters (ZR 05-42 p. 5); SCIP 0.78 about 2× slower than CPLEX 9.03, reasons given (ZR 04-19 pp. 23, 25).

### Before T3.7 (moved verbatim)

The SKILL.md lines that the T3.7 tightening (2026-11-28) shortened or moved, as they stood before it; links re-pointed to work from this folder. The shortened lines are in SKILL.md.

*Heuristic 3:*

3. **Fair yardstick** *(new)*: baseline at its best, equal tolerances, print the loss. Case: the strongest of MiniSat 1.14, Siege v4 and zChaff chosen, Siege's time reported where it wins (THESIS pp. 299, 303); the pump run with its authors' parameters (ZR 05-42 p. 5); SCIP 0.78 about 2× slower than CPLEX 9.03, reasons given (ZR 04-19 pp. 23, 25); CPLEX 10.0.1 run at SCIP's gap tolerances, mipgap 0 and absmipgap 10⁻⁹ (THESIS p. 320) (EP19); ⚠ later all solvers at defaults [R009 p. 9]. ([ledger](#heuristic-3))

<a id="heuristic-4"></a>

## Heuristic 4: Debug solution

### Full-text evidence (08 §2.7 and §5 E, copied)

- **H4 Debug solution.** No paper describes it (practice only, as SKILL.md says). Widened by §5 E.

**E. H4 widened · Check every instrument against ground truth before measuring with it**

- **One line**: the debug solution checks derived objects; extend the same test to every instrument: a detector against known structures, a checker in exact arithmetic, a feature space against known groups, a new method against published optima.
- **Cards**: the detector against the known original networks, with and without presolve, failures named with causes [D011 pp. 21–23; R013 pp. 17–19]; floating-point LP bases rechecked in rational arithmetic [R005 pp. 5–6]; returned solutions checked in exact arithmetic against the original file, primal values made reliable by an exact LP re-solve [R015 pp. 8–11; D013 pp. 10–12, 43; D021 pp. 22–23]; a cross-solver consistency check with inconsistent instances excluded and counted [D021 p. 23]; the feature space shown to recover the model groups [D021 p. 37]; correctness on graphs with published optima against two formulations before any scaling study [D020 pp. 11–13]; the lack of a reference implementation named as the debugging obstacle [D026 p. 17].
- **Checks**: §4 row 7. Co-signed sources except the debug solution itself (practice only).

### Added in T3.6

- Widened (co-signed): every instrument against ground truth [D011 pp. 21–23; D013 pp. 10–12]; the rest of 08 §5 E stays above.

### Before T3.6 (moved verbatim)

4. **Debug solution** *(new)*: check every derived cut, bound change, implication and conflict against a known optimum. Case: `debug.c`, 29 Apr 2005 (67238f422); not described in the thesis (practice only).

### Before T3.7 (moved verbatim)

The SKILL.md lines that the T3.7 tightening (2026-11-28) shortened or moved, as they stood before it; links re-pointed to work from this folder. The shortened lines are in SKILL.md.

*Heuristic 4:*

4. **Debug solution** *(new)*: check every derived cut, bound change, implication and conflict against a known optimum. Case: `debug.c`, 29 Apr 2005 (67238f422); not described in the thesis (practice only). Widened (co-signed): test every instrument against ground truth, a detector against known networks, solutions in exact arithmetic [D011 pp. 21–23; D013 pp. 10–12]. ([ledger](#heuristic-4))

<a id="heuristic-5"></a>

## Heuristic 5: Instances trigger, sets conclude

### Full-text evidence (08 §2.7, copied)

- **H5 Instances trigger, sets conclude.** Evidence: single instances as triggers (memory traces, a probing failure) [D004 pp. 66–68, 315, 323]; small affected sets refused [R021 pp. 19, 22, 40, 42; R013 p. 27; D011 pp. 34–35]. Variant (co-signed genre): record-seeking parallel papers judge on one instance and one run per version [D018 TR pp. 13–14; R020 p. 13; R014 p. 12; R019 pp. 11, 14, 18]; a fixed hard instance is re-run at every release of the base solver as a cross-version probe [R019 p. 14; D017 TR p. 15].

### Added in T3.6

- ⚠ The record-seeking parallel papers judge on one run [D018 TR pp. 13–14] (co-signed, Shinano first; the stated reason is run cost). The thesis triggers [D004 pp. 66–68, 315, 323] and the refused small sets [R021 pp. 19, 22, 40, 42] stay here.
- Fix round (2026-11-28): the SKILL.md bullet *⚠ record-seeking parallel papers (co-signed) judge on one run [D018 TR pp. 13–14]* moved back here (ParaSCIP, Shinano first: no step for the user, nothing claimed for him alone). *conclude and tune only on sets* re-cited: (INT 2023 1:06:27–1:07:30) with the co-signed refusals of small affected sets [D011 pp. 34–35; R021 p. 42], in place of the printed-page key of the Before block below (see [Held back](#held-back)).

### Before T3.6 (moved verbatim)

5. **Instances trigger, sets conclude** *(deepened)*: chase named instances for bugs and ideas (commits on noswot, blend2, alu8_9, fast0507, the rococo set); conclude and tune only on sets (ZR 04-13 p. 9; INT 2023 1:06:27–1:07:30).

### Before T3.7 (moved verbatim)

The SKILL.md lines that the T3.7 tightening (2026-11-28) shortened or moved, as they stood before it; links re-pointed to work from this folder. The shortened lines are in SKILL.md.

*Heuristic 5:*

5. **Instances trigger, sets conclude** *(deepened)*: chase named instances for bugs and ideas (commits on noswot, blend2, alu8_9, fast0507, the rococo set); conclude and tune only on sets (INT 2023 1:06:27–1:07:30); small affected sets refused (co-signed) [D011 pp. 34–35; R021 p. 42]. ([ledger](#heuristic-5))

*T3.7 fix round (2026-11-28):* this line is back in SKILL.md word for word, the instance names included.

<a id="heuristic-6"></a>

## Heuristic 6: A failed reproduction is a study

### Full-text evidence (08 §2.7 and §5 F, copied)

- **H6 A failed reproduction is a study.** Source read in full [R011 pp. 2, 5–8, 11]. Widened by §5 F.

**F. H6 widened · Re-measure a published figure and explain the gap**

- **One line**: when your knock-out of a component differs from a published one, rerun with the published protocol's differences and name the cause before reporting your figure.
- **Cards**: a higher published presolve-off factor explained by node presolve also being switched off there [D030 p. 12]; the presolve-off factor set beside the published CPLEX figure, and Gurobi's 5 % for conflicts set beside his 12 % in SCIP, the gap put down to implementation, solver environment and test set [R021 pp. 6, 64]; a 12-year re-measurement of a predecessor's component analysis [D028]; the failed reproduction that is H6's source [R011 pp. 2, 7–8].
- **Checks**: recurrence across two project lines (presolve 2014–16; formulation 2008), say–do ✅ (co-signed), executable ✅, exclusivity ✗.

### More card evidence (R011, card c03)

- The factorial: five factors u-w-e-b-f, each change keeping the integer optimum and the LP value; the published model is 2-1-1-1-0; 128 CPLEX variants collapse to 52 distinct runs, 130 distinct SCIP runs; sizes after preprocessing in five classes [R011 pp. 4–7, 9–10].
- The headline: 27 s for 1-4-0-0-0 against no optimum within 24 hours for 5-1-0-1-0, a factor above 3,200; SCIP solves every variant within the hour, slowest-to-fastest 36 against more than 3,000 for CPLEX [R011 pp. 7–8].
- Settings for comparability: SCIP's probing off, CPLEX 10.0.1 as SCIP's LP solver [R011 p. 5]. The authors' own feature reported as missing expectation: implicit integers did no better than bounded continuous variables [R011 p. 8]. Quote: "omitting seemingly useful redundant information can sometimes speed up the solution process" [R011 p. 2].

### Added in T3.6

- The case condensed to its moves (factorial, comparability settings, collapse by presolve, sizes after preprocessing, the factor, the printed failure, the two conclusions) with the card [R011 pp. 2, 5–8, 11] and EP13; the full case as written on 2026-11-14 is below.
- Widened (08 §5 F): name the protocol difference that explains a gap to a published figure [D030 p. 12; R021 p. 64].

### Before T3.6 (moved verbatim)

6. **A failed reproduction is a study** *(new)*: when a published formulation (Van Vyve and Wolsey, DOI 10.1007/s10107-005-0663-7) behaved erratically: 128 variants in CPLEX 10.0.1 and 130 runs in SCIP 0.90e on att48 (TSPLIB), 1 h limit, SCIP probing off and CPLEX as its LP solver for comparability (p. 4); identical runs explained by what presolve deduces, leaving 52 distinct CPLEX instances, sizes reported after preprocessing (p. 6); 27 s against unsolved in 24 h, a factor above 3,200 between two same-size variants differing only in integrality declarations (p. 6; above 1,000 in the abstract); geometric means per factor setting (Table 4); the failure of his own code printed: SCIP's implicit-integer declaration did worse than bounded continuous variables (p. 7). Concluded: state the exact formulation (p. 7); omitting seemingly useful redundant information can speed up solving (p. 1); one formulation in one solver does not prove a model intractable; seek formulation-independent strategies; implicit integers proposed as a first way to pass redundant information to the solver (p. 10). Model files posted (ZR 08-29, co-signed). Single project.

### Before T3.7 (moved verbatim)

The SKILL.md lines that the T3.7 tightening (2026-11-28) shortened or moved, as they stood before it; links re-pointed to work from this folder. The shortened lines are in SKILL.md.

*Heuristic 6:*

6. **A failed reproduction is a study** *(new)*: when a published TSP formulation (Van Vyve and Wolsey, DOI 10.1007/s10107-005-0663-7) behaved erratically, he and coauthors wrote its minor variants as a factorial, ran it in CPLEX and SCIP with comparable settings, collapsed variants presolve makes identical, reported sizes after preprocessing, and found a factor above 3,200 between two same-size variants; SCIP's own implicit integers did no better than continuous variables, and that was printed. Concluded: state the exact formulation; one formulation in one solver does not prove a model intractable (ZR 08-29, co-signed) [R011 pp. 2, 5–8, 11] (EP13). Widened: when your knock-out differs from a published one, name the protocol difference that explains it [D030 p. 12; R021 p. 64]. ([ledger](#heuristic-6))

*T3.7 fix round (2026-11-28):* the protocol clause *with comparable settings, collapsed variants presolve makes identical, reported sizes after preprocessing* is back in SKILL.md, after *ran its minor variants as a factorial in CPLEX and SCIP*; the sentence on SCIP's implicit integers stays here.

<a id="heuristic-7"></a>

## Heuristic 7: Model and numerics before settings

### Full-text evidence (08 §2.7, copied)

- **H7 Model and numerics before settings.** More evidence: tight tolerances for huge coefficients [R004 p. 16]; an exact rational audit of the library's LP bases and flagged unstable instances [R005 pp. 4–6]; 16-bit words with carries [R008 p. 5; R009 p. 12; D010 p. 34]; propagation safeguards [D004 pp. 48, 100–101, 209]; Gurobi's numerical safeguards in presolve [R021 pp. 9, 11, 15, 25; D030 p. 7]; numerically ambiguous instances kept out of the benchmark [D021 pp. 23, 25]; reduce the model before spending compute [R014 pp. 9–10]; "Choosing the right model is often more important (and more effective) than having the best solver implementation." [R007 p. 7] (co-signed).

### Added in T3.6

- The co-signed 2006 sentence [R007 p. 7] and DM10. The other evidence (the exact rational audit [R005 pp. 4–6], 16-bit words [R008 p. 5; R009 p. 12; D010 p. 34], propagation and presolve safeguards [D004 pp. 48, 100–101; R021 pp. 9, 11, 15, 25; D030 p. 7], numerically ambiguous instances kept out [D021 pp. 23, 25], reduce before spending compute [R014 pp. 9–10]) stays above.

### Before T3.6 (moved verbatim)

7. **Model and numerics before settings** *(new)*: tolerances 1e-9 for chip instances with coefficients up to 2^(2n) (ZR 05-19 p. 15); absolute bound feasibility after alu8_9 (510555962); improve the model before tuning (INT 2023 1:07:30–1:10:35).

### Before T3.7 (moved verbatim)

The SKILL.md lines that the T3.7 tightening (2026-11-28) shortened or moved, as they stood before it; links re-pointed to work from this folder. The shortened lines are in SKILL.md.

*Heuristic 7:*

7. **Model and numerics before settings** *(new)*: tolerances 1e-9 for chip instances with coefficients up to 2^(2n) (ZR 05-19 p. 15); absolute bound feasibility after alu8_9 (510555962); improve the model before tuning (INT 2023 1:07:30–1:10:35); "Choosing the right model is often more important (and more effective) than having the best solver implementation." [R007 p. 7] (co-signed); presolve safeguards (DM10). ([ledger](#heuristic-7))

<a id="heuristic-8"></a>

## Heuristic 8: Metric by the user's goal

### Full-text evidence (08 §2.7 and §5 A, copied)

- **H8 Metric by the user's goal.** More evidence: heuristics at gap targets [D004 pp. 142–146]; the pump judged by gap and time to the solution [R006 p. 7]; the primal integral designed for what primal heuristics are for, because by the usual measures "the trade-off between speed and solution quality is not well covered" [R017 p. 5], defined and normalised by the all-off run [R017 pp. 5–7; D015]. Widened by §5 A.

**A. H8 widened · Metric and split by the answer the user needs**

- **One line**: before pooling a test set, sort it by the answer each instance needs (a proof of infeasibility or validity, a witness, an optimum), table the parts apart, and expect different winners; choose the measure per part.
- **Cards**: infeasible chip IPs gain in nodes and time while feasible MIPs lose time, in separate tables with separate verdicts [R004 pp. 16–19]; CIP wins valid properties, SAT wins counter-examples, tabled by width [R008 pp. 11–14; R009 p. 14; R012 p. 18; D010 pp. 36–37]; a SAT-then-CIP portfolio named as the open question [D004 p. 322]; dedicated infeasible and primal sets because solvers are tuned for optimization, not for feasibility, and not at all for infeasible problems [R015 pp. 6, 8]; the existing H8 cases (gap targets, the primal integral) are the primal side of the same rule [D004 pp. 142–146; R017 pp. 5–7].
- **Checks**: §4 row 1.
- **Steps**: (1) classify every instance by the answer it needs; (2) report the component per part, with the measure that part's user cares about (time to proof; time to first or good solution; time to optimality); (3) if winners split, name the portfolio or the per-part default and say which part a default serves; (4) state the losing part with numbers, not only in words (the 2008 text gives the losing part in words only [R009 p. 14]).

### Added in T3.6

- The primal integral's first written form, co-signed 2011 [R017 pp. 5–7] (08 §3.2 item 8).
- Widened (08 §5 A, heuristic level; it fails exclusivity, so no seventh method, 08 §10 item 1): split by the answer needed [R004 pp. 16–19; R008 p. 14]. The library rule for separate infeasible and primal sets [R015 pp. 6, 8] is in Anti-patterns.

### Before T3.6 (moved verbatim)

8. **Metric by the user's goal** *(new)*: heuristics cost only 14 % in time to optimality, so a gap-target run follows (THESIS pp. 4, 129); the primal integral (CPAIOR 2017 slides 65–67); first-feasible targets (MIPW 2025).

### Before T3.7 (moved verbatim)

The SKILL.md lines that the T3.7 tightening (2026-11-28) shortened or moved, as they stood before it; links re-pointed to work from this folder. The shortened lines are in SKILL.md.

*Heuristic 8:*

8. **Metric by the user's goal** *(new)*: heuristics cost only 14 % in time to optimality, so a gap-target run follows (THESIS pp. 4, 129); the primal integral (CPAIOR 2017 slides 65–67; first in print in 2011, co-signed [R017 pp. 5–7]); first-feasible targets (MIPW 2025). Widened: split by the answer needed, a proof or a witness, and table the parts apart: infeasible chip IPs gain while feasible MIPs lose [R004 pp. 16–19]; CIP proves valid properties, SAT finds counter-examples [R008 p. 14]. ([ledger](#heuristic-8))

<a id="heuristic-9"></a>

## Heuristic 9: Try it, try the opposite, revert

### Full-text evidence (08 §2.7, copied)

- **H9 Try it, try the opposite, revert.** First written evidence: "It turns out that our concerns are unjustified: applying linear domain propagation at every node improves the performance on almost all test sets." [D004 p. 114]; the default child selection found slightly inferior to three alternatives and printed [D004 p. 96]; delayed restarts inferior, other criteria needed [D004 p. 177].

### Added in T3.6

- The first written trace, the thesis sentence on linear propagation [D004 p. 114]. The child-selection result [D004 p. 96] and delayed restarts [D004 p. 177] stay here.

### Before T3.6 (moved verbatim)

9. **Try it, try the opposite, revert** *(new)*: defaults from gut feeling, a test, failure, then the opposite, which sometimes works for no known reason (INT 2023 about 1:05–1:06, caption, team); reverts in the SCIP log.

### Before T3.7 (moved verbatim)

The SKILL.md lines that the T3.7 tightening (2026-11-28) shortened or moved, as they stood before it; links re-pointed to work from this folder. The shortened lines are in SKILL.md.

*Heuristic 9:*

9. **Try it, try the opposite, revert** *(new)*: defaults from gut feeling, a test, failure, then the opposite, which sometimes works for no known reason (INT 2023 about 1:05–1:06, caption, team); reverts in the SCIP log. In print: "It turns out that our concerns are unjustified: applying linear domain propagation at every node improves the performance on almost all test sets." [D004 p. 114]. ([ledger](#heuristic-9))

<a id="heuristic-10"></a>

## Heuristic 10: Print the loss and the open question

### Full-text evidence (08 §2.7, copied)

- **H10 Print the loss and the open question.** More evidence [R004 pp. 2, 18–19; R006 pp. 7, 9; D004 pp. 96, 114, 177, 324–325; D010 pp. 14–15, 28–29, 36–37; R021 pp. 14, 18, 28, 65; D030 pp. 12–13; D020 pp. 9, 15–18, 22; R011 p. 8]. Variant: from 2007 the loss usually sits in the body, not in the abstract or summary [R008 pp. 2, 13–14; R009 p. 14; R017 pp. 3, 7; D022 pp. 3, 11–12; D023 pp. 1, 15–16, 22].

### Added in T3.6

- ⚠ From 2007 the loss usually sits in the body [R008 p. 2; D023 pp. 15–16]; the full list of the variant's cards is above.

### Before T3.6 (moved verbatim)

10. **Print the loss and the open question** *(new)*: ZR 05-19 abstract; delayed restarts inferior (THESIS p. 163); the node gap to strong branching left open (ZR 04-13 p. 12); non-paying reductions tabulated (ZR 16-44 pp. 12, 16, 27, 63). *Inferred*: successors answered several (Witzig, Berthold, Heinz, DOI 10.1007/s12532-021-00202-0; Gamrath 2020).

### Before T3.7 (moved verbatim)

The SKILL.md lines that the T3.7 tightening (2026-11-28) shortened or moved, as they stood before it; links re-pointed to work from this folder. The shortened lines are in SKILL.md.

*Heuristic 10:*

10. **Print the loss and the open question** *(new)*: ZR 05-19 abstract; delayed restarts inferior (THESIS p. 163); the node gap to strong branching left open (ZR 04-13 p. 12); non-paying reductions tabulated (ZR 16-44 pp. 12, 16, 27, 63); ⚠ from 2007 the loss usually sits in the body, not the abstract [R008 p. 2; D023 pp. 15–16]. *Inferred*: successors answered several (Witzig, Berthold, Heinz, DOI 10.1007/s12532-021-00202-0; Gamrath 2020). ([ledger](#heuristic-10))

<a id="misreadings"></a>

## Common misreadings

### Full-text evidence (08 §2.7 and §3.2, copied)

- **Misreading 1** (seeds): reworded in §3.2 item 3.

- **Misreading 2** (knock-outs do not add): more evidence [D004 p. 142; R017 p. 7]; the presolve paper explains small knock-outs by the component that covers for them [R021 pp. 8, 11, 13, 18, 61–62, 65]. Variant: the 2014 multi-row knock-outs multiply to more than switching the class off (card arithmetic, 1.42 against 1.31) [D030 pp. 12–15]; non-additivity also runs the other way.

- **Misreading 3** (SCIP from nothing): the code was rebuilt from scratch for flexibility and CIP while SIP's ideas were carried into the first version [D010 p. 15; R009 p. 3; D004 p. 20]; the 2002 rule ran in SIP with CPLEX as LP solver [R001 p. 11].

- **Misreading 4** (hand-rules man): the written record is thin (H1).

- **Misreading 5** (nearly as fast as CPLEX): the likely written source is two abstracts, one co-signed and one sole-authored (§3.2 item 14).

14. **Misreading 5.** The likely written source is the abstracts that call SCIP almost competitive with commercial MIP solvers: co-signed in 2008 [R009 p. 2; R012 p. 2] and sole-authored in 2009 [D010 p. 1]. The measured ratios, for the misreading's correction: 5.1 in the unshifted time mean (2.4 with a 10 s shift; card arithmetic) [R009 p. 10], 3.5 and 1.84 [R012 p. 14] and 2.86 [D010 p. 28]. The 2004 and 2005 texts print the loss plainly [R003 p. 24; R004 p. 16].

### Added in T3.6

- **Misreading 1** reworded, not deleted (08 §3.2 item 3; §10 item 10): *No written study of his has them* → *Not in his sole-authored studies*, with the four co-signed forms [R015 pp. 13–15; D029 p. 20; D023 p. 14] and the 2016 recheck [R021 p. 40]; *text searches of his reports and 2017–2023 decks found none* moved here (below). The racing permutations [D017 TR pp. 10–11; R019 p. 10; D018 TR p. 6] are in the 08 text and the Roundtable Card.
- **Misreading 2**: overlap explains small knock-outs [R021 pp. 8, 61–62]; non-additivity in the other direction [D030 pp. 12–15].
- **Misreading 3**: rebuilt from scratch [D010 p. 15].
- **Misreading 5**: the written source of the phrase [R009 p. 2; D010 p. 1] and the 2009 table's ratio [D010 p. 28] (08 §3.2 item 14, worded as a fact about the source, not as a criticism).
- **Fix round (2026-11-28)**:
  - Misreading 1: MIPLIB 2010 has 16 authors, credits no section to him and credits its variability work to Danna [R015 p. 22] (card s01; 08 §3.1); the parallel repeats have Shinano first [D029 p. 20].
  - Misreading 5: *The phrase is from his own 2008–09 abstracts [R009 p. 2; D010 p. 1]; the 2009 table gives 2.86 against CPLEX 11 [D010 p. 28].* was wrong as worded: neither abstract says *nearly as fast* or names CPLEX; both call SCIP "almost competitive" with commercial MIP solvers, and the 2008 one has four authors (card c02 calls it the *likely* written source). Now: the measured ratios first (THESIS p. 377; 2.86 to CPLEX 11 in shifted geometric mean time [D010 pp. 28–29]), then the likely source, one co-signed abstract [R009 p. 2] and one sole-authored [D010 p. 1], in separate sentences.

### Before T3.6 (moved verbatim)

**Common Misreadings**

1. **"He separates gains from noise with seeds or permutations."** No written study of his has them: the thesis uses single runs on identical machines, reruns suspicious ones and treats up to 2 % as noise (THESIS p. 319); text searches of his reports and 2017–2023 decks found none. The five-seed "consistent win" rule is spoken only, as Gurobi team practice (WEB 9.1 1:11:31; INT 2023 1:05:30; WEB 13.0 0:11:49; captions).
2. **"A knock-out percentage is that component's contribution."** Switching off single heuristic classes, or single cut families, costs much less in sum than switching off all of them (THESIS p. 128); Koch et al. 2022 (DOI 10.1016/j.ejco.2022.100031, pp. 12–13) cite him for it. The numbers rank; they do not add.
3. **"Reliability branching is a SCIP invention; SCIP began from nothing."** History and reliability branching were built and measured in Martin's SIP (ZR 02-32 p. 1; ZR 04-13 p. 12); SCIP's first commit carries SIP's check scripts and most SIP ideas (THESIS p. 6).
4. **"A hand-rules man, opposed to ML."** Reliability branching came out of an ML experiment (H1), about 15 years before Khalil et al. 2016; he still uses ML to find interpretable rules (WEB 9.1 0:59:59).
5. **"SCIP was nearly as fast as CPLEX."** His Appendix C: 63 % (0.90i) to 115 % (0.90f) slower than CPLEX 10.0.1 with CPLEX as SCIP's LP solver (THESIS p. 377).

### Before T3.7 (moved verbatim)

The SKILL.md lines that the T3.7 tightening (2026-11-28) shortened or moved, as they stood before it; links re-pointed to work from this folder. The shortened lines are in SKILL.md.

*Misreading 1:*

1. **"He separates gains from noise with seeds or permutations."** Not in his sole-authored studies: the thesis uses single runs on identical machines, reruns suspicious ones and treats up to 2 % as noise (THESIS p. 319). Co-signed written studies do: 100 permutations per model in MIPLIB 2010 (16 authors; no section credited to him, its variability work credited to Danna [R015 p. 22]) [R015 pp. 13–15], repeats of nondeterministic parallel runs (Shinano first) [D029 p. 20], permuted copies [D023 p. 14], and a recheck that found "an artifact of performance variability" [R021 p. 40]. The five-seed "consistent win" rule is spoken only, as Gurobi team practice (WEB 9.1 1:11:31; INT 2023 1:05:30; WEB 13.0 0:11:49; captions).

*Misreading 2:*

2. **"A knock-out percentage is that component's contribution."** Switching off single heuristic classes, or single cut families, costs much less in sum than switching off all of them (THESIS p. 128); Koch et al. 2022 (DOI 10.1016/j.ejco.2022.100031, pp. 12–13) cite him for it; the presolve paper explains small knock-outs by overlap [R021 pp. 8, 61–62]; non-additivity also runs the other way [D030 pp. 12–15]. The numbers rank; they do not add.

*Misreading 5:*

5. **"SCIP was nearly as fast as CPLEX."** His Appendix C: 63 % (0.90i) to 115 % (0.90f) slower than CPLEX 10.0.1 with CPLEX as SCIP's LP solver (THESIS p. 377); in 2009, SCIP with CPLEX's LP solver at a factor of 2.86 to CPLEX 11 in shifted geometric mean time [D010 pp. 28–29]. The likely written source of the reading: abstracts that call SCIP "almost competitive" with commercial MIP solvers, one co-signed (2008) [R009 p. 2] and one sole-authored (2009) [D010 p. 1].

<a id="anatomy-branching"></a>

## Anatomy: Branching rules revisited (2005), with Branching on History Information (2002)

### Full-text evidence

10. **Signature Work Anatomy, branching.** *22 MIPLIB 3.0 instances* → 16 MIPLIB 3.0 instances plus 6 randomly generated instances of the arborescence-flow problem [R001 p. 11] of the 2000 diploma thesis of T. Pfender [R001 p. 16]. The same thesis is the source of the aflow instances that MIPLIB 2003 lists under Achterberg [R005 pp. 4, 13–14] and MIPLIB 2010 credits to him [D013 pp. 19, 60]; none of these texts states the name change (card c2-01).

- Key insight: reliability branching as Algorithm 3 and the classification diagram [R002 pp. 7–8]; minimum evidence: Table 2 of the 2002 report with arithmetic totals and matched tolerances [R001 p. 11], the 2004 grid read as points, the knee named [R002 pp. 11, 13, 17]; abandoned 2002 machinery [R001 pp. 8–10]; origin: the thesis acknowledgement [D004 p. 9]; the 2002 report shows no learning experiment [R001 p. 2].

### Added in T3.6

- Origin + [R001 p. 2]; key insight + [R002 pp. 7–8]; minimum evidence: *22 MIPLIB 3.0 instances* → 16 MIPLIB 3.0 plus 6 generated aflow instances from his 2000 diploma thesis [R001 pp. 11, 16]; 2004 + [R002 pp. 11, 13, 17] (replacing *ZR 04-13 pp. 9–12*); abandoned paths + [R001 pp. 8–10].
- Fix round (2026-11-28): *6 generated aflow instances from his 2000 diploma thesis (as Pfender)* → *6 randomly generated instances of the arborescence-flow problem of his 2000 diploma thesis (as Pfender)*: R001 p. 11 refers to the thesis for the problem (its reference Pfe00), not for the instances.

### Before T3.6 (moved verbatim)

**Branching rules revisited (Oper. Res. Lett. 33(1):42–54, 2005, DOI 10.1016/j.orl.2004.04.002), with Branching on History Information (ZIB-Report 02-32, 2002)**

| Dimension | Finding |
|---|---|
| Origin | *Stated*: the CS diploma project's learners inside SIP (2000–2001) pointed to one history feature (H1). Diploma thesis not found |
| Why then | *Inferred*: strong branching was available through SIP's CPLEX API; baseline Linderoth and Savelsbergh (DOI 10.1287/ijoc.11.2.173; ZR 02-32 p. 5) |
| Key insight | Pseudocosts are unreliable until both directions are observed a set number of times; strong branching only on unreliable candidates; one parameter spans the old rules |
| Minimum evidence | 2002: 22 MIPLIB 3.0 instances, 3,533.5 s in total against 12,966.7 s (hybrid pseudocost) and 12,342.1 s (CPLEX 7.5) (ZR 02-32 p. 10). 2004: the full grid and its knee (ZR 04-13 pp. 9–12) |
| Abandoned paths | The ML route; the 2002 machinery (classes by model names, scaling factors) |
| Reception | 382 Crossref citations (Nov 2026); SCIP's default basis; refined by Gamrath 2020 |
| Methods shown | Method 3, Method 2, H1, H2. Joint with Koch and Martin; implemented in SIP |

<a id="anatomy-conflict"></a>

## Anatomy: Conflict analysis in mixed integer programming (2007)

### Full-text evidence

11. **Signature Work Anatomy, conflict analysis, Minimum evidence.** Name the subsets (card recount): the ALU figures (−90 % nodes, −60 % time) are on the 21 instances that presolve does not solve, all 35 give −73 % and −42 %; the feasible-MIP figures (−50 %, +15 %) are on all 29, the 24 solved by both settings give −44 % and +4.5 % [R004 pp. 17, 19]. The abstract keeps the loss: "On feasible MIP instances, the number of required branching nodes was reduced by 50% in the geometric mean. However, the total solving time increased by 15%." [R004 p. 2].

- Key insight: the generalized conflict graph and the dual-ray reason [R004 pp. 9–14]; abandoned paths: a Farkas-based IIS heuristic dropped for its overhead [R004 p. 11; D004 p. 188]; the thesis variants by effort level [D004 pp. 192–195]; reception: the thesis gain is against no conflict analysis, which was off by default in SCIP 0.90f [D004 pp. 193, 386; D010 pp. 20–21].

### Added in T3.6

- Key insight + [R004 pp. 9–14]; minimum evidence + the subsets [R004 pp. 17, 19]; abandoned paths + the IIS heuristic [R004 p. 11]; reception + [D004 pp. 193, 386].
- Fix round (2026-11-28): the recount figures moved here, out of the Minimum evidence row, so that no reply cites them as his published result: *The ALU pair is on the 21 instances presolve leaves (all 35: −73 %, −42 %); on the 24 feasible ones both settings solve: −44 %, +4.5 % (card recount) [R004 pp. 17, 19]*. The row keeps the lesson: the two pairs rest on different subsets (card recount), quote a headline with its subset.

### Before T3.6 (moved verbatim)

**Conflict analysis in mixed integer programming (Discrete Optim. 4(1):4–20, 2007, DOI 10.1016/j.disopt.2006.10.006)**

| Dimension | Finding |
|---|---|
| Origin | *Stated*: a conversation with Novikov during the chip-verification project (THESIS p. x); first code 13 Aug 2003 |
| Why then | *Inferred*: SAT learning was mature (DOI 10.1109/12.769433; DOI 10.1109/date.2002.998262, cited in ZR 05-19); infeasible chip instances; SCIP gave access to duals |
| Key insight | An infeasible or bound-exceeding LP is explained by a few local bound changes found from dual information, which seed a SAT-style conflict graph; bound disjunctions for general integers (THESIS pp. 165–166) |
| Minimum evidence | Infeasible chip instances: nodes −90 %, time −60 %; feasible MIPs: nodes −50 %, time +15 % (ZR 05-19 abstract) |
| Abandoned paths | Conflicts as LP cuts; analysing bound-exceeding and strong-branching LPs; the aggressive setting (THESIS pp. 178–181) |
| Reception | Sole author. The 2005 → 2007 reversal (slower, then > 10 % faster) is explained only as implementation details (p. 181) |
| Methods shown | Method 6, Method 2, H10 |

### Before T3.7 (moved verbatim)

The SKILL.md lines that the T3.7 tightening (2026-11-28) shortened or moved, as they stood before it; links re-pointed to work from this folder. The shortened lines are in SKILL.md.

*Minimum evidence row:*

| Dimension | Finding |
|---|---|
| Minimum evidence | Infeasible chip instances: nodes −90 %, time −60 %; feasible MIPs: nodes −50 %, time +15 % (ZR 05-19 abstract). The two pairs rest on different subsets (card recount): the ALU pair on the 21 instances presolve does not solve, the feasible pair on all 29 [R004 pp. 17, 19]; quote a headline with its subset (other subsets: ledger) |

<a id="anatomy-cip"></a>

## Anatomy: Constraint Integer Programming (thesis 2007), with the SCIP paper (MPC 2009)

### Full-text evidence

- The class: Definition 1.6 and Proposition 1.7 [D004 pp. 27–28]; the MPC paper restates it [D010 p. 4]. The protocol: 575 to 244 instances, 28,060 runs [D004 pp. 16, 334]. The chip result in 2009: SAT fails on 58 of 258 instances, CIP on none [D010 p. 37]; "In total, SAT failed on 58 out of 258 instances, while CIP was able to solve all instances within the time limit." [R008 p. 13]. Component-level abandoned paths: delayed restarts [D004 p. 177], local cuts at every node [D004 p. 129], a Farkas-based IIS heuristic [D004 p. 188]. Credits by chapter [D004 pp. 75, 115, 132, 199]. The MPC paper prints the plugin design's costs: the hidden column view, poor cache locality, data copied several times, an LP solver used without short cuts [D010 pp. 14–15].
- The MPC 2009 paper was read in full (card D010, c03); SKILL.md's Sources had it as abstract only.

### Added in T3.6

- Key insight + [D004 pp. 27–28]; minimum evidence + [D004 pp. 16, 334] and [D010 p. 37]; abandoned paths + [D004 pp. 129, 177]; methods shown + [D010 pp. 14–15].

### Before T3.6 (moved verbatim)

**Constraint Integer Programming (thesis, TU Berlin 2007, DOI 10.14279/depositonce-1634), with SCIP: solving constraint integer programs (Math. Program. Comput. 1(1):1–41, 2009, DOI 10.1007/s12532-008-0001-1)**

| Dimension | Finding |
|---|---|
| Origin | *Stated*: joining his two degrees; SIP's LP-centred data structures could not hold CP, so a new code at the end of 2002 (THESIS p. ix) |
| Why then | *Stated*: an advisor who gave freedom; an industrial project (Valse-XT) whose partner delivered data early (p. ix) |
| Key insight | Constraints that become linear once the integers are fixed, with CP, SAT and MIP techniques on one search tree (pp. 1–2) |
| Minimum evidence | Orders of magnitude faster than SAT on some chip circuits, SAT faster on counter-examples (p. 6); 575 instances filtered to 244 by stated rules; 28,060 runs |
| Abandoned paths | SIP as platform; no abandoned SCIP design found (unknown) |
| Reception | Dantzig Dissertation Award, second place (2008); prizes for the MPC paper (Beale–Orchard-Hays 2009, INFORMS Optimization Society Young Researchers 2011) |
| Methods shown | Method 5, Method 4; Wolter's and Berthold's parts credited (pp. 101, 118) |

<a id="anatomy-presolve"></a>

## Anatomy: Presolve Reductions in Mixed Integer Programming (2016 report, 2020 journal)

### Full-text evidence

12. **Signature Work Anatomy, presolve.** *each with a knock-out table*: fixed-variable removal and the rounding of integer bounds have none, the first because it acts through model size [R021 p. 21].

- Headline: with presolve off the ≥ 10 s bracket is 9.05 times slower, 488 more time-outs, 504 models solved only with presolve [R021 pp. 5–6]; the null and negative components [R021 pp. 14, 18, 28–29, 56, 65]; the 2014 multi-row predecessor [D030 pp. 1, 11]; the motive [R021 p. 4].

### Added in T3.6

- Key insight: *each with a knock-out table* → *each class and most components with a knock-out table in one layout (fixed-variable removal and integer-bound rounding have none [R021 p. 21])* (08 §3.2 item 12); minimum evidence + [R021 pp. 5–6]; reception: *journal version not read* → *report read in full, journal version not read*.

### Before T3.6 (moved verbatim)

**Presolve Reductions in Mixed Integer Programming (INFORMS J. Comput. 32(2):473–506, 2020, DOI 10.1287/ijoc.2018.0857)**

| Dimension | Finding |
|---|---|
| Origin | No primary account; stated motive: few papers on an important topic (ZR 16-44 p. 2, co-signed) |
| Why then | *Inferred*: his first Gurobi-era publication (RAMP 2014), months after joining |
| Key insight | A complete taxonomy of Gurobi 6.5's presolve, more than thirty reductions, each with a knock-out table in one layout |
| Minimum evidence | Presolve off: 504 models fail to finish in 3,600 s; about ninefold on ≥ 10 s (pp. 3–4) |
| Negative results | CG strengthening, probing on single equations, global probing at nodes, subsumed-row removal; removing redundant rows hurts, with a hypothesis (pp. 12, 16, 26, 27, 63) |
| Reception | 139 Crossref citations (14 Nov 2026). Five authors, alphabetical, roles not stated; journal version not read |
| Methods shown | Method 4, Method 1 |

<a id="anatomy-mcf"></a>

## Anatomy: The Mcf-separator (2010)

### Full-text evidence

- Key insight: the framework computes only the aggregation: "It is important to understand that our framework is not explicitly generating cutting planes. It only calculates weight vectors u." [D011 p. 3]. Results: SCIP time ratios 0.52 on arc.set, 0.32 on avub, 0.53 on sndlib, 0.52 on ufcn [D011 p. 30]; CPLEX 0.70, 0.50 and 0.45 on arc.set, avub and sndlib [D011 pp. 32, 34]; of all 1,388 general MIPs in the CPLEX runs (MIPLIB, Mittelmann and a 1,266-model CPLEX-internal set) 129 (9.3 %) are affected, time −17.9 % on them and 2 % overall, −25 % and −36 % on the affected models of the ≥ 10 s and ≥ 100 s subsets, almost no overhead on the unaffected rows [D011 p. 34].
- Version note: copied from 08 §3.3 below.

- **Mcf-separator.** The report's inconsistency study is SCIP-only and includes the set where a looser gate gained [R013 pp. 27–29]; the journal moves it to the general-MIP sets in both solvers and prints the CPLEX numbers [D011 pp. 35–37]. The general-MIP sentence of the journal abstract is new [D011 p. 1]. So the gate was decided where harm would occur, and the class gain it gives up left the published version.

### Added in T3.6

- Key insight + [D011 p. 3]; minimum evidence: *a factor of two on average* → the per-set time ratios [D011 p. 30]; *Consistent networks in roughly 10 % of general MIPs, time −18 % on those* → 129 of 1388 affected, −17.9 % [D011 p. 34]; abandoned paths / reception: the journal's version of the study [D011 pp. 35–37]; *journal version not read* removed (read, card D011).
- Fix round (2026-11-28): *CPLEX's internal set: 129 of 1388 general MIPs (9.3 %) affected* → *CPLEX on 1,388 general MIPs (MIPLIB, Mittelmann and a 1,266-model CPLEX-internal set): 129 (9.3 %) affected*: the 1,388 are all three sets [D011 p. 34].

### Before T3.6 (moved verbatim)

**The Mcf-separator (Math. Program. Comput. 2(2):125–165, 2010, DOI 10.1007/s12532-010-0015-3), with Christian Raack**

| Dimension | Finding |
|---|---|
| Origin, why then | Unknown from his side; *inferred*: Raack's network-design work (file author from 9 Jul 2008), while he worked in SCIP and CPLEX at once |
| Key insight | Detect the structure from the matrix, measure its inconsistency, stay silent without it (ZR 09-38 pp. 1–3) |
| Minimum evidence | Network design: a factor of two on average, many solvable in 1 h only with it (abstract; p. 29); an order-of-magnitude speed-up was the tuning aim, not the result (p. 22). Consistent networks in roughly 10 % of general MIPs, time −18 % on those; almost no degradation on the rest (p. 29) |
| Abandoned paths / reception | A looser gate with a SCIP-only gain (Method 1); 31 Crossref citations; journal version not read |
| Methods shown | Method 1 |

### Before T3.7 (moved verbatim)

The SKILL.md lines that the T3.7 tightening (2026-11-28) shortened or moved, as they stood before it; links re-pointed to work from this folder. The shortened lines are in SKILL.md.

*Minimum evidence row:*

| Dimension | Finding |
|---|---|
| Minimum evidence | Network design in SCIP: time ratios 0.32–0.53 on four sets [D011 p. 30]; an order-of-magnitude speed-up was the tuning aim, not the result (p. 22). CPLEX on 1,388 general MIPs (MIPLIB, Mittelmann and a 1,266-model CPLEX-internal set): 129 (9.3 %) affected, −17.9 % time on them, almost no overhead elsewhere [D011 p. 34] |

*T3.7 fix round (2026-11-28):* the caution *an order-of-magnitude speed-up was the tuning aim, not the result (p. 22)* stays here only (see the header's T3.7 fix-round note).

<a id="anatomy-rlt"></a>

## Anatomy: Efficient separation of RLT cuts (IPCO 2023; Math. Program. 2025) (new)

### Full-text evidence (cards c07 D022 and c08 D023)

- Authors: Bestuzheva (first and corresponding), Gleixner, Achterberg last; no contribution statement; joint work in Research Campus MODAL [D023 pp. 1, 22]; the Gurobi 10.0 beta runs on Gurobi's internal set are the only part needing Gurobi access, so they are probably his share (*inferred* on the card) [D022 p. 14].
- Problem and idea: separation cost is the obstacle, not strength; products hidden in MILPs are recovered from pairs of linear rows on three variables with a binary (Theorem 1, proved by undetermined coefficients); row marking and projection filtering skip candidates that cannot be violated [D023 pp. 2–3, 5–13; D022 pp. 5–10].
- Evaluation: SCIP brackets with Clean, Affected, [x,timelim] and All-optimal subsets, shifts 1 s and 100 nodes [D023 p. 14]; row marking cuts separation's mean share of time from 54.6 % to 2.8 % on MILPs [D023 p. 18] and time by 63 % [D023 p. 17]; the node increase checked on the all-optimal subset [D023 p. 17]; Gurobi on/off time ratios 0.99 (all MILPs) to 0.89 (≥ 1,000 s) and 0.73 to 0.12 on MINLPs [D023 pp. 21–22]; each code measured only against itself, SCIP and Gurobi numbers not directly comparable [D023 p. 21].
- Losses in the body: implicit products slightly worse on MINLPs [D023 p. 15]; "although this does not always translate into an improvement in overall solver performance" [D023 p. 16]; "We observe a slight increase in time when RLT cuts are enabled, and a slight decrease in number of nodes." [D022 p. 11].
- Method links on the cards: Method 2 evidence (the strongest link), Method 4 evidence and a ✗ on seeds (permuted copies), Method 1 variant (class split, no detector of the paying classes, no stated default), Method 5 and 6 variants (cards c07, c08).

### Added in T3.6

- A sixth anatomy, added because it is the Gurobi-era work read in full and measured in two codes. Rows: origin, key insight, minimum evidence, negative results, methods shown, as above. *Why then* and *Reception* rows left out: neither is stated in the texts, and the work is too recent (2 Crossref citations each in works.json).
- Fix round (2026-11-28): Origin, *the Gurobi runs are the part needing Gurobi access (inferred his; last author)* → *roles not stated (first author Bestuzheva, he last)* [D023 pp. 1, 22]: SKILL.md's Voices says no co-signed text states roles, so the card's inference stays here, not in the anatomy. Methods shown, *Method 1 variant (a detector, two codes, no default stated)* → *a detector of implicit products, none of the classes where the cuts pay; two codes; no default stated*, matching Method 1's variant bullet.

### Before T3.7 (moved verbatim)

The SKILL.md lines that the T3.7 tightening (2026-11-28) shortened or moved, as they stood before it; links re-pointed to work from this folder. The shortened lines are in SKILL.md.

*Methods shown row:*

| Dimension | Finding |
|---|---|
| Methods shown | Method 2, Method 4 (brackets, all-optimal subset), Method 1 variant (a detector of implicit products, none of the classes where the cuts pay; two codes; no default stated) |

<a id="anti-patterns"></a>

## Research anti-patterns

### Full-text evidence

- A small-set gain switched into the default unchecked: [R021 pp. 40, 42] (quotes under [taste warnings](#taste-warnings)); the dual-fixing extension stays off after the recheck [R021 p. 40]. Fix round: no longer an anti-pattern in SKILL.md (one card, and the point is warning sign 5 and Method 4 step 5 with the same pages).
- Proofs and witnesses pooled in one mean: separate tables and verdicts for infeasible and feasible sets [R004 pp. 16–19]; dedicated infeasible and primal sets because solvers are tuned for optimization, not feasibility, and not at all for infeasible problems [R015 pp. 6, 8] (co-signed); 08 §5 A.
- Absolute numbers compared across two codes: each code measured only against itself, cross-code numbers declared not directly comparable [D022 p. 14; D023 p. 21] (co-signed; one study, two versions); the 2010 Mcf paper compares the separator's effect in SCIP and CPLEX by direction and explains the smaller CPLEX gain by CPLEX's faster baseline [D011 p. 34]; EP14.

### Added in T3.6

- The three items above. *each with ≥ 2 card ids in this section* was wrong for the first (R021 only) and, in SKILL.md, for the third (D023 only).
- Fix round (2026-11-28): SKILL.md keeps two of them. *A small-set gain switched into the default unchecked [R021 pp. 40, 42] → M4 step 5.* is removed there (one card; it repeated warning sign 5 and Method 4 step 5 with the same pages, so it added no explanatory power, paper-reading-card §3 rule 4). *Absolute numbers compared across two codes [D023 p. 21] → EP14.* now cites [D022 p. 14; D023 p. 21 (one study, two versions); D011 p. 34], two studies.

### Before T3.6 (moved verbatim)

**Research Anti-patterns**

Each with its source, then the remedy:
- Habits nobody measured; single-instance conclusions or tuning; proxy gains read as speed-up (warning signs 1, 3; H5) → M4, H5, M2.
- Unequal tolerances; a model translated directly into the other paradigm; CP against MIP without expert models on both sides (ZR 02-32 p. 10; INT 2023 1:14:46–1:15:46) → H3.
- An uninterpretable learned model inside the solver (WEB 9.1 0:59:59; INT 2023 1:16:16) → H1.
- Fixed-LP duals as MIP sensitivity (WEB 9.0 0:38:59) → say it has no mathematical meaning.
- No exact formulation; "intractable" from one formulation and one solver (ZR 08-29 pp. 7, 10) → H6.
- Tuning before fixing numerics (INT 2023 1:07:30) → H7.
- Worst-case bounds as verdicts on practice; "polynomial" as "fast" (SEA 2022 slides 20–21) → M1 safeguards.

<a id="trajectory"></a>

## Research trajectory

### Full-text evidence (08 §8 and §9, copied)

Studies are distinct works after merging pairs (any read level); *full* counts those with a full or partial text.

| Period | Studies (full) | Main topics in the cards | Full-text anchors |
|---|---|---|---|
| 2000–2004 | 5 (4) | Branching in SIP (2), application modelling in a group (1), the SCIP framework (1); a polyhedral diploma thesis (metadata) | [R001; D024 TR; R002; R003]; D036 |
| 2005–2009 | 16 (13) | SCIP/CIP framework (4: the thesis, two CIP reports, the MPC paper), conflict analysis, chip verification, MIPLIB 2003, the objective pump, counting, formulation sensitivity, teaching software, structure detection (Mcf), an LP heuristic for an interval method; abstracts: ParaLEX, hybrid branching | [R004; R005; R006; R007; D004; R008; R009; R010; R011; R012; D010; D026; R013] |
| 2010–2014 | 11 (7) | Parallel search (3), MIPLIB 2010, rounding heuristics and the primal integral, presolve (RAMP 2014), editorial work; abstracts: hybrid solving survey, implied literals, 12 years of progress | [R014; R015; R017; R016; R019; R018; D030] |
| 2015–2019 | 2 (2) | Parallel records, the presolve taxonomy | [R020; R021] |
| 2020–2025 | 5 (5) | Parallel records, an exact feedback-arc-set method, MIPLIB 2017, RLT cuts (two versions) | [R022; D020; D021; D022; D023] |

**Turns visible in the full texts.**
- *From a rule inside another solver to his own framework.* The 2002 rule runs in SIP with CPLEX as LP solver [R001 p. 11]; SCIP was begun in October 2002 [D004 p. 20] and described as version 0.78 in 2004 [R003 pp. 2, 24].
- *SAT and CP into MIP, pulled by an application.* Conflict analysis (2005) takes its infeasible test set from chip verification [R004 pp. 2–3, 16]; the CIP class and the property checker follow [R008 pp. 2–3; D004 pp. 199–202; R009 p. 2; D010 pp. 29–37].
- *The evaluation protocol consolidates in steps:* totals over a set the code selected (2002) [R001 pp. 10–11] → on/off in the default with both-solved subsets (2005) [R004 pp. 16–17] → the thesis protocol (2007) [D004 pp. 333–340] → slower-run subsets with affected rows (2009–10) [R013 pp. 26–27; D011 pp. 33–34] → the bracket table and refusals of small affected sets (2014–16) [D030 pp. 10–12; R021 pp. 5–6, 19, 22, 40, 42] → brackets with all-optimal subsets in two codes (2022–25) [D022 pp. 10–14; D023 pp. 14–22].
- *After 2009 the written record is co-signed* community, library and parallel work; the last sole-authored paper (a 2013 patent aside, not read) is the 2009 SCIP paper, written at ZIB and acknowledging his move to CPLEX [D010 pp. 1, 38].
- *Gurobi (from 2014):* documentation of a production solver's components with measured impact [D030 pp. 1, 15; R021 pp. 4, 67]; joint work with ZIB on RLT cuts for bilinear products, measured in both SCIP and Gurobi [D022 p. 14; D023 pp. 21–22]; the library line continues [D021 p. 2].

**What stayed constant.** Knock-out against the full default, read per set, from 2005 [R004 pp. 16–17] to 2025 [D023 pp. 14–22]; time printed beside node counts, from 2002 [R001 p. 11] to 2025 [D023 p. 16]; budgets in solver-internal units, from 2004 [R002 p. 6] to 2023 [D022 p. 10]; failures and exclusions counted and named, from 2004 [R003 p. 25] to 2025 [D023 p. 14]; three MIPLIB editions, 2005, 2010 and 2021 [R005 p. 3; D013 p. 2; D021 p. 2].

**Against SKILL.md's Research Trajectory and note 06.** The full texts agree that the turns follow institutional moves (ZIB → ILOG/IBM → Gurobi). They add the 2000–2002 items of §3.2 item 22, date the bracket form's first written appearance to 2009 (§3.2 item 2), and give the CPLEX years co-signed full texts (§3.2 item 17).

Studies per employer period, pairs merged; the thesis counts as sole-authored.

| Period | Studies (full) | Most frequent coauthors (studies) | Pattern seen in the full texts |
|---|---|---|---|
| 2000–2007, ZIB | 12 (10) | Koch 6, Martin 4, Grötschel 2 | Sole-authored core papers: the SCIP framework report, the conflict report and the thesis [R003; R004; D004]. Branching and the 2003 library with Koch and Martin [R001; R002; R005]; teaching software with Grötschel and Koch [R007]; property checking with industry and university partners [R008 p. 2]; a project report with eight authors in alphabetical order [D024 TR p. 2]. The thesis credits Koch and Martin, Wolter, Berthold, Brinkmann and Wedler by chapter [D004 pp. 75, 115, 132, 199] |
| 2008–2013, ILOG/IBM | 19 (13) | Koch 8, Berthold 8, Heinz 6, Shinano 4, Wolter 3 | One sole-authored paper [D010]; CIP and counting reports with ZIB students and colleagues [R009; R010; R012]; the Mcf-separator with Raack [D011]; a 16-author library [R015; D013]; heuristics with Berthold and Hendel [R017]; the parallel line with Shinano first [R014; R018; R019]; IBM colleagues on implied literals and CPLEX progress [D016; D028]; a guest heuristic in a chemical-engineering code [D026 p. 1] |
| 2014–2025, Gurobi | 8 (8) | Gleixner 3, Koch 3, Berthold 3, Shinano 3; Bixby, Gu, Rothberg, Weninger 2 | Five-author presolve papers with Gurobi's founders, alphabetical, roles not stated [D030 p. 1; R021 p. 3]; ParaSCIP records, Shinano first [R020; R022]; MIPLIB 2017 as 4th of 16 and a committee member [D021 p. 2]; RLT with Bestuzheva and Gleixner, last author [D022 p. 3; D023 p. 1]; feedback arc sets with a Vienna group, last author [D020 p. 1]. No sole-authored text |

**Across the career.** Koch is the most frequent coauthor (17 of 39 studies, 2002–2021), then Berthold (12, 2005–2021), Heinz (8), Shinano (7, from the 2008 ParaLEX abstract [D006]), Martin (4, 2002–2005) and Gleixner (4, 2010–2025). Baharev appears in 2009 and 2021 [D026 p. 1; D020 p. 1].

**Byline.** Until 2011 his name stands first on most bylines, many of them alphabetical, so position says little; sole authorship is the only firm signal, and among papers it ends in 2009. Apart from the part D026 names as his [D026 p. 7] and Danna's credited variability work [R015 p. 22], no co-signed text states roles; the cards infer at most that the Gurobi- or CPLEX-internal runs were his (the CPLEX-internal Mcf set [D011 p. 34]; the Gurobi 10.0 beta runs [D022 p. 14]), labelled *inferred*.

**Partners.** An EU telecommunication project [D024 TR pp. 1–2]; chip-verification partners [R008 p. 2; D004 p. 199]; ZIB through the Research Campus MODAL in the Gurobi years [R021 p. 1; D023 p. 22]; supercomputer centres for the parallel records [R014 p. 10; D018 TR p. 13].

22. **Research Trajectory, 1999–2002.** Add the 2000 diploma thesis under his former name [D036] and the 2002 MOMENTUM report on UMTS network planning, group work with ZIB, Darmstadt and Atesio authors, six months before the history-branching report [D024 TR pp. 1–3].

### Added in T3.6

- 1999–2002: the diploma thesis under his former name [D036] and the 2002 UMTS report [D024 TR pp. 1–3] (08 §3.2 item 22).
- 2006–2014: his last sole-authored text [D010 p. 38]; the co-signed CPLEX-era texts [R015; R017; R014]. Fix round (2026-11-28): *His last sole-authored text is the 2009 SCIP paper [D010 p. 38]* → *His last sole-authored paper in the indexed record (a 2013 patent aside) is the 2009 SCIP paper, written at ZIB [D010 pp. 1, 38]*: works.json lists a 2013 IBM patent with him as sole inventor (Role skip, not read), and p. 38 is the acknowledgement, so the affiliation comes from p. 1.
- 2014–: the RLT study measured in SCIP and Gurobi.
- The protocol in steps (08 §8, *The evaluation protocol consolidates in steps*) [R001 p. 10; R004 p. 17; R013 p. 27; D030 p. 11; D023 p. 14].
- Latest: *2026 to 14 November: no paper, preprint, commit or talk found* → *2026: no paper or preprint in the publication harvest of 26 November; no commit or talk found to 14 November* (works.json harvested 2026-11-26; no 2026 work).

### Before T3.6 (moved verbatim)

**Research Trajectory**

Period: direction (trigger) → representative work.
- **1999–2002**: ML for branching in SIP → history branching (a CS diploma needing a MIP solver; Koch) → ZR 02-32.
- **2002–2007**: SCIP; constraint integer programming; chip verification; SAT techniques (SIP could not hold CP; Valse-XT from Aug 2003; Novikov) → ORL 2005; Discrete Optim. 2007; thesis; Hybrid Branching (CPAIOR 2009).
- **2006–2014**: ILOG / IBM CPLEX; SCIP commits until March 2009 (a 2005 workshop talk, an ILOG offer, his account) → ZR 08-29; MPC 2010; A&W 2013.
- **2014–**: Gurobi: MIP performance, presolve, non-convex MIQCP (9.0), VP of R&D 2020 (Gu and Rothberg, his account) → IJOC 2020; MIPLIB 2017; RLT cuts (DOI 10.1007/s10107-024-02104-0).

**Latest**

- Nov/Dec 2025: performance segment of the Gurobi 13.0 webinar (caption). June 2025: MIP Workshop talk on improvement heuristics for first feasibles. March 2025: RLT paper in print. 2026 to 14 November: no paper, preprint, commit or talk found.

### Before T3.7 (moved verbatim)

The SKILL.md lines that the T3.7 tightening (2026-11-28) shortened or moved, as they stood before it; links re-pointed to work from this folder. The shortened lines are in SKILL.md.

*2006–2014:*

- **2006–2014**: ILOG / IBM CPLEX; SCIP commits until March 2009 (a 2005 workshop talk, an ILOG offer, his account) → ZR 08-29; MPC 2010; A&W 2013. His last sole-authored paper in the indexed record (a 2013 patent aside) is the 2009 SCIP paper, written at ZIB [D010 pp. 1, 38]; then co-signed MIPLIB 2010, the primal integral and ParaSCIP [R015; R017; R014].

<a id="inner-tensions"></a>

## Inner tensions

### Full-text evidence (08 §2.7, copied)

- **Inner Tensions.** *Which baseline counts*: the 2022–2025 study measures each code only against itself [D023 p. 21], while his 2004–2009 texts measured against CPLEX [R003 p. 24; R004 p. 16; D010 p. 28]. *From scratch or reuse*: rebuilt from scratch with SIP's ideas [D010 p. 15; R009 p. 3]; the parallel layer reuses the unmodified solver: "This makes the parallelization development independent of the SCIP development. Thus, ParaSCIP directly profits from any algorithmic progress in future versions of SCIP." [R014 p. 2] (co-signed, Shinano first, no role stated: not a side of his own tension, so SKILL.md does not use it).

### Added in T3.6

- From scratch or reuse + the co-signed parallel layer [R014 p. 2]; which baseline counts + the RLT study's own-code baselines [D023 p. 21].
- Fix round (2026-11-28): *and the co-signed parallel layer reuses SCIP unmodified [R014 p. 2]* removed from SKILL.md's tension (ParaSCIP, Shinano first, no role stated: a design decision of that project cannot be one side of his own tension); the tension keeps INT 2023, THESIS pp. ix and 6, the PSD cuts and Turner's criterion, whose source key, lost in T3.6, is back (INT 2023 55:06–56:38, caption; Before block of Method 6). *Which baseline counts*: the RLT study marked *co-signed, roles not stated*.

### Before T3.6 (moved verbatim)

**Inner Tensions**

- **Sets conclude, instances drive** (tension of method): conclusions and tuning only on sets (H5), yet the commit log ties fixes and defaults to named instances.
- **Tune or write**: he overran his deadline improving SCIP and says most solver progress cannot be written up (THESIS p. x; INT 2023 50:27–53:35), yet took Koch's advice to write, and the thesis won three prizes.
- **From scratch or reuse**: he always wants to build it himself (INT 2023 1:20:24–1:21:28), yet SIP's ideas and harness went into SCIP (THESIS pp. ix, 6), and he adopted PSD cuts and Turner's criterion.
- **Which baseline counts**: in 2023 academic work should improve its host framework, not beat Gurobi (INT 2023 51:29); his own academic work measured itself against CPLEX each time (ZR 02-32 p. 10; THESIS p. 377).
- **Explainable rules, unexplained defaults**: features over learners (H1), yet defaults that work for no known reason (H9).

### Before T3.7 (moved verbatim)

The SKILL.md lines that the T3.7 tightening (2026-11-28) shortened or moved, as they stood before it; links re-pointed to work from this folder. The shortened lines are in SKILL.md.

*Tune or write:*

- **Tune or write**: he overran his deadline improving SCIP and says most solver progress cannot be written up (THESIS p. x; INT 2023 50:27–53:35), yet took Koch's advice to write, and the thesis won three prizes.

*Which baseline counts:*

- **Which baseline counts**: in 2023 academic work should improve its host framework, not beat Gurobi (INT 2023 51:29), and the RLT study (co-signed, roles not stated) measures each code only against itself [D023 p. 21]; his own academic work measured itself against CPLEX each time (ZR 02-32 p. 10; THESIS p. 377).

<a id="mentor-voice"></a>

## Mentor Voice

Not changed by T3.6 (see the Scope note above); T3.7 shortened one line, kept here. The rest of Mentor Voice is complete in SKILL.md.

*T3.7 fix round (2026-11-28):* the pointer *(taste mark 3)* of *Reports each change with its measured percentage, small or disappointing* resolves again, since mark 3 has its 19 % case back ([Taste: marks](#taste-marks)).

### Before T3.7 (moved verbatim)

The SKILL.md lines that the T3.7 tightening (2026-11-28) shortened or moved, as they stood before it; links re-pointed to work from this folder. The shortened lines are in SKILL.md.

*Derived questions:*

- Derived questions (not quotes): "What happens to total time when you switch it off?" "Where does the time go?" "What does it do outside your class?" "What got worse?"

<a id="roundtable-card"></a>

## Roundtable Card

### Full-text evidence (08 §3.2, copied)

15. **Roundtable Card, Gleixner line.** Gurobi 6.5 stores the whole Farkas proof as a linear row, with no backward propagation [R021 pp. 63–64]: his Gurobi-era conflict practice is not the graph-based SCIP one.

16. **Roundtable Card, Fischetti line** (*variability averaged over seeds against exploited*). Co-signed ParaSCIP texts exploit variability: racing with settings, random top-level branching and permutations [D017 TR pp. 7, 10–11; R019 p. 10; D018 TR p. 6]; the co-signed library says variability may be exploited by massively parallel solvers [D013 p. 14]. No text gives his own position (Shinano first, roles not stated), so the contrast stays an inference.

### Added in T3.6

- Gleixner line + Gurobi 6.5's Farkas rows [R021 pp. 63–64]; Fischetti line + the co-signed racing [D017 TR pp. 10–11]; blind spot *no seeds in written studies* → *no seeds in his sole-authored studies* (08 §3.2 item 3).
- Fix round (2026-11-28): Fischetti line, *weaker given co-signed ParaSCIP racing [D017 TR pp. 10–11]* → *co-signed ParaSCIP texts (Shinano first, roles not stated) do exploit it by racing [D017 TR pp. 10–11], and no text gives his own position*: the racing is that project's practice, not a position of his.

### Before T3.6 (moved verbatim)

**Roundtable Card**

- **Lens (one line)**: Does it make a complete solver's default faster in total time on a broad library, without hurting anything outside its class?
- **Leads when**: a component is proposed as default; gains show in nodes, gap or cuts, not time; benchmarks are designed or audited; one class gains, others lose; SAT, CP or learned rules enter MIP; tweaking stalls.
- **First questions asked**: Total time when switched off in the full default? Where does the time go? What happens outside its class? What got worse? Which rule chose the models? How many affected? Are incumbents special cases? Same tolerances and LP solver?
- **Default recommendation**: knock the component out of a full open solver's default on a rule-selected, class-balanced public set (MIPLIB 2017 benchmark plus target class); read the ≥ 10 s bracket: shifted geometric means, affected counts; split the time, budget it; default on only if it detects its models, silent elsewhere; print losses; add seeds.
- **Will push back on**: unmeasured habits; single-instance conclusions or tuning; node, gap or cut gains as speed-up; unequal tolerances, weakened baselines; class-specific defaults without a detector; opaque learned models in solvers; fixed-LP duals as MIP sensitivity; tuning before fixing numerics; worst-case bounds as practical verdicts.
- **Likely disagreements** (inferred from methods; no dispute documented):
  - *Lübbecke*: automatic Dantzig–Wolfe decomposition as in GCG, excellent on some classes, useless on others, stays out of Gurobi's defaults; users supply the partition (his 2023 interview, captions, https://www.youtube.com/watch?v=8bhIW27vCUQ). GCG: DOI 10.1007/978-3-642-13193-6_21; 10.1007/s10107-014-0761-5 (not read).
  - *Gleixner*: tolerances, dropping models where versions disagree (DOI 10.1287/ijoc.2018.0857), against exact solving with certificates (10.1007/s10107-021-01749-5); graph-based conflicts (10.1016/j.disopt.2006.10.006) against cut-based (arXiv:2410.15110, Gleixner co-author). Shared: MIPLIB 2017, RLT cuts (10.1007/s12532-020-00194-3; 10.1007/s10107-024-02104-0).
  - *Fischetti*: objective-weighted pump (DOI 10.1016/j.disopt.2006.10.004) against cutoff plus recovery (2026, 10.5281/zenodo.22810777; unreviewed); variability averaged over seeds against exploited (10.1287/opre.2013.1231).
  - *Bixby, Forrest* (guests): none documented; his cut knock-outs follow Bixby et al. 2000 (DOI 10.1007/978-0-387-35514-6_2).
- **Blind spots**: literature (self-declared); no seeds in written studies; no certificates; worst-case and proof strength; side-effect node savings unmeasured; knock-outs only rank; class structure averaged away; closed Gurobi code and sets.

<a id="honest-boundary"></a>

## Honest Boundary

### Full-text coverage (08 §1, copied)

| Item | Count | Source |
|---|---|---|
| Card entries | 54 in 13 batch files: round 1 b01 (1), c01–c08 (24), s01–s02 (11); round 2 a2-01 (17), c2-01 (1) | digests; 07 |
| Read level | full 34 · partial 2 (the thesis at chapter level; the preface of an edited collection) · abstract 11 · metadata 6 · unreadable 1 (the superseded round-1 card of D024) | digests |
| Works with a card | 53 of the 55 indexed works; the two without are Role = skip (patents D031, D032) | INDEX.md after `mark_read_from_cards.py`: carded 34, skimmed 2, abstract 11, metadata 6, — 2 |
| Coverage row (`team_status.py`) | 0 Scholar rows · 55 distinct works indexed · 36 open full texts · 34 read in full · 2 in part · 11 abstract only · 6 metadata only incl. unreadable · 2 skipped · 0 book material · 84 quotes verified | 07 |
| Quote gate (2026-11-28) | 84 quotes: 84 exact, 0 equal up to spacing or symbols, 0 not found | `verify_card_quotes.py` |
| Open texts | every one of the 36 files with text has a full or partial card | INDEX.md |
| Studies after merging pairs | 39; 31 with a full or partial text; 8 at abstract or metadata level only (D036, D025, D006, D009, D012, D027, D016, D028) | this note |
| Method links | 152 link entries on 41 cards: 35 of the 36 full or partial cards (R016, an edited collection, has none) and 6 abstract cards (D007, D009, D016, D028 as evidence; D014, D015 as variants). The digests link Methods 1–6 only; heuristics, misreadings and taste marks are named in card prose (§2.7) | digests |
| Pool material | 96 new-pattern-candidate entries on 40 cards; 162 proof-device entries (154 on full or partial cards); 222 transferable-technique entries (214 on full or partial cards) | digests |
| Full or partial cards by period | 2000–04: 4 · 2005–09: 13 · 2010–14: 11 · 2015–19: 3 · 2020–24: 4 · 2025: 1 | digests |

**What the reading changes in scope.** The skill was built from web research, the SCIP history, talks and a partial read of the ZIB-Reports. The cards now cover every open text: the whole report series 2002–2020, the journal texts of the 2009 SCIP paper, the Mcf-separator, MIPLIB 2010 and 2017, the ParaSCIP papers, the 2014 RAMP paper, the 2021 feedback-arc-set paper, both RLT versions, the 2009 distillation paper, the 2002 UMTS report and the thesis at chapter level. The CPLEX-era non-report works (D006, D009, D016, D027, D028) and all journal versions of the reports remain abstracts or metadata (§11).

### Open gaps (08 §11, copied)

- **Journal versions.** D001, D002, D003, D005, D007, D008, D014, D015 and D019 are read through their reports; any change between versions is unknown except where both texts were read, and there the 2010 gate study changed (§3.3).
- **The origin of the bracket form.** The 2013 analysis with Wunderling is an abstract [D028]; the co-signed 2014 and 2016 texts credit their table form to it [D030 p. 11; R021 p. 5]. Whether the 2009 slower-run subsets [R013 pp. 26–27] are his or his coauthor's is not stated.
- **CPLEX-era non-report works** are abstracts: ParaLEX [D006], hybrid branching [D009], implied literals [D016], the hybrid-solving survey [D027], the progress analysis [D028]. First-hand method evidence for 2006–2014 is co-signed or abstract-level.
- **The diploma theses.** The mathematics thesis under his former name is metadata only [D036]; the computer-science thesis with the learning experiment, the stated origin of H1, was not found.
- **The 2003 UMTS chapter** was read only in its 2002 report version [D024 TR p. 2]; differences are unknown.
- **The thesis** was read at chapter level: Chapters 2, 3, 6–10, 13–15 in part, Appendix B mostly not, Chapter 14's operator sections not (card b01, chapter map); claims resting on its unread parts are not made here [D004].
- **Who did what** in co-signed work: no card can assign a passage to him; the ParaSCIP and library texts are especially opaque.
- **Gurobi internals**: closed code and private test sets [D030 p. 11; R021 p. 5; D022 p. 14; D023 p. 21]; no Gurobi-era sole statement on method.
- **Permutations in 2025**: the procedure behind the permuted copies is not described [D023 p. 14].
- **Sealed material.** Five holdout items, one candidate cluster and one single-card candidate are withheld until the validation unseals them; the pages that carry them are not used in this note.
- **The two patents** (Role = skip) are not read.

### Corrections to the boundary (08 §3.2, copied)

17. **Honest Boundary, *The CPLEX years have almost no first-hand method evidence*.** Co-signed full texts now cover them: the Mcf-separator with a CPLEX implementation and a CPLEX-internal general-MIP set [D011 pp. 2, 34; R013 pp. 26–27]; the primal integral [R017 pp. 5–7]; MIPLIB 2010 [R015; D013]; ParaSCIP [R014; R018; R019]; abstracts for implied literals in CPLEX 12.5 [D016] and the 12-year component analysis [D028]. None is sole-authored.

19. **Honest Boundary, *diploma theses not found*.** The mathematics diploma thesis is identified at metadata level [D036]; the computer-science diploma thesis is not.

20. **Honest Boundary, the *deterministic work units* item under *Claimed but unverified*.** Co-signed written practice exists in Gurobi 6.5's presolve: work limits counted in touched non-zeros [R021 pp. 49, 66], and an order-dependent step made deterministic under parallelism by collecting candidates in parallel and applying them in one sequential pass [R021 p. 52]; a deterministic parallel mode is called necessary for development [D029 pp. 29–30]; the 2013 abstract highlights CPLEX's deterministic parallel optimizer [D028]. No sole statement.

### Added in T3.6

- New first bullet, the coverage row and the main gaps (08 §1, §11).
- Tacit gaps + *who did what in co-signed work*.
- Era and resources: *The CPLEX years have almost no first-hand method evidence* → co-signed full texts now cover them, none sole-authored (08 §3.2 item 17).
- Claimed but unverified: *deterministic work units* kept in the list, marked as now having co-signed written practice [R021 pp. 49, 52] (08 §3.2 item 20).
- Evidence quality: *Journal versions not read (the ZIB-Reports were); A&W 2013 … not read; diploma theses not found* → journal versions mostly not read; A&W 2013 by abstract [D028]; the mathematics diploma thesis at metadata level [D036] (08 §3.2 items 18–19).
- Research date and the validation line updated; the validation was run before the deep reading and not rerun.
- A short list *Corrections from the full texts* added after the boundary (see [Corrections](#corrections)).
- Fix round (2026-11-28): coverage line + *31 of them with a full or partial text* (08 §1), *2 skipped (patents)* → *(patents, not read)*, *the journal versions of nine ZIB-Reports* → *the published versions* (four are proceedings; likewise *Journal versions mostly not read* in Evidence quality), *most of the thesis's Chapters 14–15 and Appendix B* → *in the thesis, Chapters 2, 3, 6–10 and 13 read in part, most of 14–15 and Appendix B not read (card b01)*. Era and resources: *none sole-authored* → *none sole-authored after the 2009 SCIP paper, written at ZIB [D010 pp. 1, 38]* (the trajectory and 06 §10.3 put that paper in the CPLEX years). Validation line: the link to `FIDELITY.md` replaced by its name and a do-not-open note, since that file describes the sealed items.

### Before T3.6 (moved verbatim)

**Honest Boundary**

This skill is distilled from public information, with these limits:
- **Tacit-knowledge gaps**: how Gurobi defaults are actually tuned (stated only, in captions); facts passed by personal communication (cited so in Berthold's 2014 thesis); the content of his primer; which instance to chase (the log shows which, never why).
- **Era and resources**: each method carries its era (see Limitations). The CPLEX years have almost no first-hand method evidence; Gurobi-era statements describe a team with a test cluster (by his account 192 machines), and alphabetical author lists hide roles.
- **Field boundary**: floating-point branch-and-cut in general-purpose solvers. On polyhedral theory, worst-case analysis, exact solving and certificates, decomposition and branch-and-price, learned policies and LP internals he has stated at most an opinion.
- **Claimed but unverified** (stated, no practice evidence; not methods): five seeds and the four-of-five ≥ 10 % rule; the SEA 2022 algorithm-engineering rules as applied in closed code; decision-tree rules for dualisation and simplex choice; research as about 10 % of development; deterministic work units (WEB 9.5 0:25:35); judging academic work by its host framework; building from scratch as a rule; hiring solver authors; the git and issue workflow at Gurobi.
- **Evidence quality**: interview and webinars read as automatic captions; webinars are product talks. Journal versions not read (the ZIB-Reports were); A&W 2013, the stated origin of the bracket form, not read; diploma theses not found; no rejected paper, erratum or reply found. Gurobi's test-set size varies by source (more than 5,000 in 2021 to 8,611 in 2025); no trend claimed. Critics are mostly successors re-measuring his ZIB-era methods in SCIP.
- **Self-declared weak point** (caption): he does not follow the literature well and relies on collaborators (INT 2023 1:20:24–1:22:29). Pair this lens with a literature check.
- **Research date**: 2026-11-14 (notes 2026-11-08). He is living and active; later work is not covered. Re-run the research periodically (yearly, or after a new paper or talk) and update this skill.
- **Validation 2026-11-14**: sealed-item test 7 with the skill / 8 without (5 items; 2 points or less is a tie); task test 9 supported and 0 fabricated grounds with the skill (on the version before the after-validation fixes of 2026-11-14; retention re-test after them: 6 of 6 pass); see FIDELITY.md.

<a id="corrections"></a>

## Corrections from the full texts

Each SKILL.md correction line, with the 08 item it rests on; the 08 items are copied below.

| SKILL.md line | 08 | Where it acts in SKILL.md |
|---|---|---|
| Example A.1 signs | §3.2 item 1 | Method 4 variants |
| Bracket era | §3.2 item 2 | Method 4 One line |
| Seeds | §3.2 item 3 | Misreading 1, Method 4 step 7 and variants, Roundtable blind spot; Activation Rules unchanged, a hand edit of two lines proposed (see [How to Use](#how-to-use)) |
| Conflicts, the 2007 default | §3.2 item 4 | Method 2 variants |
| Mcf gate | §3.2 item 5, §3.3 | Method 1 variants, Mcf anatomy |
| More components on at no gain | §3.2 item 6 | Method 1 variants, taste mark 1 |
| Frozen-version selector | §3.2 item 7 | Method 5 One line and variants |
| Primal integral | §3.2 item 8 | Method 2 Limitations, H8 |
| H2 source | §3.2 item 9 | H2 |
| Branching anatomy, 22 instances | §3.2 item 10 | anatomy |
| Conflict anatomy, subsets | §3.2 item 11 | anatomy |
| Presolve anatomy, knock-out tables | §3.2 item 12 | anatomy |
| Mcf anatomy, 10 % affected | card D011 (c04) | anatomy |
| Dynamic reliability in 2004 | §3.2 item 13 | Method 3 variants and Limitations |
| Child-selection default | §3.2 item 21 | taste warning 3 (Integrity rule 4 unchanged) |
| Misreading 5 | §3.2 item 14 | Misreading 5 |
| CPLEX years; A&W 2013 | §3.2 items 17–18 | Honest Boundary |
| Hooker's SIMPL (in Method 6 Limitations) | §2, Method 6 proposed text | Method 6 Limitations |

### The twelve contradiction links (08 §3.1, copied)

Twelve links on twelve cards, nine studies. Each card was reopened; the verdicts:

| Card(s) | Method | Claim of the card | Check | Verdict |
|---|---|---|---|---|
| D004 | M4 | SKILL.md reverses the signs of Example A.1 | text read at [D004 pp. 335–336]: the geometric mean reports a 27 % improvement for setting B, the shifted geometric and arithmetic means a 6 % and 89 % deterioration | Upheld; wording fix |
| R013, D011 (one study) | M4 era | the slower-run subsets of ≥ 10 s and ≥ 100 s exist in 2009–2010 | "The subsets cplex10s and cplex100s correspond to those instances within cplex that need at least 10s and 100s of CPU time to be solved, respectively, by the slower of the two versions, mcf and nomcf." [R013 p. 27]; [D011 pp. 33–34] | Upheld; a narrower form (three subsets, CPLEX part only, shift not stated) |
| D013 (with R015) | M4 step 7, Misreading 1 | 100 permutations per model, a variability score per instance, permuted copies and inferential tests recommended | [D013 pp. 13–18; R015 pp. 13–15]; "Performance is not deterministic. Instead, it is a random variable that can be sampled with computational experiments." [R015 p. 15] | Upheld for a co-signed library paper (16 authors); no section credited to him, the variability work credited to Danna [R015 p. 22; D013 p. 57] |
| D029, R018 (one study) | M4 step 7 | five runs of each nondeterministic configuration | [D029 p. 20; R018 pp. 16–17, 19–21] | Upheld; the repeats answer message timing in parallel runs, not seeds; Shinano first |
| D023 | M4 step 7 | permuted copies in the SCIP tables | the text names "permuted instances" in the failure counts and a table "with 4 permutations" [D023 pp. 14, 26–27] (checked in the text) | Upheld; the procedure is not described; the Gurobi part mentions neither [D023 pp. 21–22] |
| D018, R020 (one study) | M4, H5 | one instance, one run per version | [D018 TR pp. 13–14; R020 p. 13] | Upheld as a genre exception (record-seeking parallel work, co-signed); the stated reason is run cost [D018 TR p. 13] |
| R021 | M1 | components on without a measured gain | [R021 pp. 14, 18, 56, 65] | Partial: step 5 allows it, Taste mark 1 does not |
| R009 | M2 step 1 | a solved-count verdict in the abstract beside a time loss in the table | [R009 pp. 2, 10] | Upheld (co-signed); recorded as a variant of step 1 and of H10 |
| R001 | M5 | 2002 test set filtered by the code under study | [R001 p. 10]; the CPLEX check on the excluded instances partly offsets it | Upheld as an era note |

### All claims the full texts change (08 §3.2, copied)

1. **Method 4, Practice, Example A.1.** Now *+27 % (geometric), −6 % (shifted geometric), −89 % (arithmetic)*. Replace by: −27 % with the geometric mean (setting B better), +6 % with the shifted geometric mean and +89 % with the arithmetic mean (setting B worse) [D004 pp. 335–336].
2. **Method 4, One line, era.** Now *the bracket form is in his papers from 2014 … Do not read earlier work as if it used brackets.* Replace by: the thesis (2007) reports shifted-geometric-mean ratios against the default with faster/slower counts and equal-path blocks [D004 pp. 335–336, 339–340]; a narrower bracket form, ≥ 10 s and ≥ 100 s subsets by the slower run with affected rows, wins and time-outs, appears in the 2009 report and the 2010 journal paper, in their CPLEX part, with no stated shift [R013 pp. 26–27; D011 pp. 33–34]; the full table (≥ 0, 1, 10, 100, 1,000 s, shift 1, affected by iterations) is from 2014 [D030 pp. 10–12; R021 pp. 5–6].
3. **Misreading 1, Method 4 step 7, the Activation Rules default and the Roundtable Card's blind spot** (*No written study of his has them*). Replace by: none of his sole-authored studies uses seeds or permutations [D004 p. 333; R003 pp. 24–26; R004 pp. 15–19]; co-signed written studies do in four forms: a library's variability study with 100 permutations per model [R015 pp. 13–15; D013 pp. 13–18]; five repeats of nondeterministic parallel configurations [D029 p. 20; R018 pp. 19–21]; permutations as a diversification device in racing [D017 TR pp. 10–11; R019 p. 10; D018 TR p. 6]; permuted copies in 2025 tables with no stated procedure [D023 pp. 14, 26–27]. The 2016 presolve report names one unspecified recheck: "Nevertheless, such a small set of problem instances does not provide any meaningful results, and indeed, additional tests that we have conducted showed that the speed-up in Table 23 is just an artifact of performance variability." [R021 p. 40]. The five-seed *consistent win* rule remains spoken only.
4. **Method 2, Practice, conflict analysis.** Now *The 2007 default uses conflicts for propagation only …, at most 10 per infeasible subproblem, with aging*. Replace by: these are the parameter settings of the thesis experiments [D004 pp. 192–193]; in the SCIP 0.90f MIP benchmarks conflict analysis was off by default and was measured by adding it to that reference [D004 pp. 193, 386; D010 pp. 20–21]; the best variant gains about 12 % against no conflict analysis [D004 p. 193]. The reason against LP cuts for non-binary conflicts is given only in part: the linearized disjunction is called probably very weak, untested [D004 p. 191; R004 p. 14].
5. **Method 1, Practice, the Mcf gate.** Now *Releasing the network-inconsistency threshold alone helped SCIP but not CPLEX*. This follows the report [R013 pp. 27–29]; the journal version reports the study on the general-MIP sets in both solvers, where releasing the threshold alone "already deteriorates the performance" of CPLEX, the SCIP rows still improve slightly, and the class gain on one network-design set no longer appears [D011 pp. 34–37]. Keep the sentence with the version named, and add the journal result.
6. **Method 1, Practice, counter-examples.** Add simple probing on single equations, biconnected components and global probing at nodes (on by default; at most 3 % on their affected models; the last with more time-outs when on) [R021 pp. 18, 56, 65].
7. **Method 5, the test-set selector.** Holds for the thesis only [D004 pp. 333–334]. By era: the code under study in 2002 [R001 p. 10]; a reference solver with an effort window in 2004–2005 [R003 p. 24; R004 p. 16]; two other solvers in 2009 [D010 p. 21]; the code family itself at Gurobi [D030 p. 11; R021 p. 5]; consensus under hard and soft rules for the 2010 library benchmark [R015 p. 7]; a published selection model for the 2017 library [D021 pp. 24–36]; the detector under study in 2025 [D023 p. 13].
8. **Method 2, Limitations, the primal integral.** Its first written form is a 2011 report that he co-signed (first of three, alphabetical; roles not stated), which defines the measure and normalises it by the all-off run [R017 pp. 3, 5–7]; the 2012 abstract keeps the claim to introduce it [D015]. The 2013 journal paper SKILL.md cites is a later venue (not read).
9. **H2, source.** See §2.7 H2.
10. **Signature Work Anatomy, branching.** *22 MIPLIB 3.0 instances* → 16 MIPLIB 3.0 instances plus 6 randomly generated instances of the arborescence-flow problem [R001 p. 11] of the 2000 diploma thesis of T. Pfender [R001 p. 16]. The same thesis is the source of the aflow instances that MIPLIB 2003 lists under Achterberg [R005 pp. 4, 13–14] and MIPLIB 2010 credits to him [D013 pp. 19, 60]; none of these texts states the name change (card c2-01).
11. **Signature Work Anatomy, conflict analysis, Minimum evidence.** Name the subsets (card recount): the ALU figures (−90 % nodes, −60 % time) are on the 21 instances that presolve does not solve, all 35 give −73 % and −42 %; the feasible-MIP figures (−50 %, +15 %) are on all 29, the 24 solved by both settings give −44 % and +4.5 % [R004 pp. 17, 19]. The abstract keeps the loss: "On feasible MIP instances, the number of required branching nodes was reduced by 50% in the geometric mean. However, the total solving time increased by 15%." [R004 p. 2].
12. **Signature Work Anatomy, presolve.** *each with a knock-out table*: fixed-variable removal and the rounding of integer bounds have none, the first because it acts through model size [R021 p. 21].
13. **Method 3, Limitations.** See the Method 3 proposal (§2).
14. **Misreading 5.** The likely written source is the abstracts that call SCIP almost competitive with commercial MIP solvers: co-signed in 2008 [R009 p. 2; R012 p. 2] and sole-authored in 2009 [D010 p. 1]. The measured ratios, for the misreading's correction: 5.1 in the unshifted time mean (2.4 with a 10 s shift; card arithmetic) [R009 p. 10], 3.5 and 1.84 [R012 p. 14] and 2.86 [D010 p. 28]. The 2004 and 2005 texts print the loss plainly [R003 p. 24; R004 p. 16].
15. **Roundtable Card, Gleixner line.** Gurobi 6.5 stores the whole Farkas proof as a linear row, with no backward propagation [R021 pp. 63–64]: his Gurobi-era conflict practice is not the graph-based SCIP one.
16. **Roundtable Card, Fischetti line** (*variability averaged over seeds against exploited*). Co-signed ParaSCIP texts exploit variability: racing with settings, random top-level branching and permutations [D017 TR pp. 7, 10–11; R019 p. 10; D018 TR p. 6]; the co-signed library says variability may be exploited by massively parallel solvers [D013 p. 14]. No text gives his own position (Shinano first, roles not stated), so the contrast stays an inference.
17. **Honest Boundary, *The CPLEX years have almost no first-hand method evidence*.** Co-signed full texts now cover them: the Mcf-separator with a CPLEX implementation and a CPLEX-internal general-MIP set [D011 pp. 2, 34; R013 pp. 26–27]; the primal integral [R017 pp. 5–7]; MIPLIB 2010 [R015; D013]; ParaSCIP [R014; R018; R019]; abstracts for implied literals in CPLEX 12.5 [D016] and the 12-year component analysis [D028]. None is sole-authored.
18. **Honest Boundary and Method 4, *A&W 2013 … not read*.** Its abstract is read [D028]: it names a scheme for analysing benchmark results but not its form; the co-signed 2014 and 2016 texts credit their table form to it [D030 p. 11; R021 p. 5]. The bracket form's origin is still unconfirmed in a text of its own.
19. **Honest Boundary, *diploma theses not found*.** The mathematics diploma thesis is identified at metadata level [D036]; the computer-science diploma thesis is not.
20. **Honest Boundary, the *deterministic work units* item under *Claimed but unverified*.** Co-signed written practice exists in Gurobi 6.5's presolve: work limits counted in touched non-zeros [R021 pp. 49, 66], and an order-dependent step made deterministic under parallelism by collecting candidates in parallel and applying them in one sequential pass [R021 p. 52]; a deterministic parallel mode is called necessary for development [D029 pp. 29–30]; the 2013 abstract highlights CPLEX's deterministic parallel optimizer [D028]. No sole statement.
21. **Taste warning sign 3 and Integrity rule 4** (the unmeasured child-selection default, THESIS p. 74). The sentence concerns Martin's root-LP child selection when it was adopted; the same chapter measures it and finds the default hybrid slightly inferior [D004 pp. 88, 95–96]. Keep the quote, add that it was measured in the same chapter.
22. **Research Trajectory, 1999–2002.** Add the 2000 diploma thesis under his former name [D036] and the 2002 MOMENTUM report on UMTS network planning, group work with ZIB, Darmstadt and Atesio authors, six months before the history-branching report [D024 TR pp. 1–3].

### Version notes (08 §3.3, copied)

- **Mcf-separator.** The report's inconsistency study is SCIP-only and includes the set where a looser gate gained [R013 pp. 27–29]; the journal moves it to the general-MIP sets in both solvers and prints the CPLEX numbers [D011 pp. 35–37]. The general-MIP sentence of the journal abstract is new [D011 p. 1]. So the gate was decided where harm would occur, and the class gain it gives up left the published version.
- **ParaSCIP 2013/2014.** The revision adds that a state-of-the-art sequential solver is the most important ingredient and that exploiting a powerful MIP solver is crucial [D017 TR pp. 4–5, 20], and drops two reasons the original gave for memory-conservative settings and a lowered racing threshold [R019 p. 14]. "it is crucial to exploit a powerful MIP solver in parallelization" [D017 TR p. 20].
- **ParaSCIP 2015/2016.** The revision recasts "ad-hoc values" of the collecting-mode parameters as moderate values not tuned well enough [R020 p. 13; D018 TR p. 14].
- **ParaSCIP 2012/2013.** The ZIB-Report has the same text as the journal article, and its text layer carries the tables [R018; D029].
- **MIPLIB 2010.** Report and journal are one study; the report calls the benchmark selection dynamic, by consensus [R015 p. 7]; the journal describes a staged review [D013 p. 6].
- **Abstracts word for word.** D007 = R009, D008 = R010, D014 = R014, D015 = R017, D019 = R021 (up to hyphenation) (cards a2-01).
- **RLT.** The 2025 version adds redundancy filters, permuted copies, size-group tables and a control run [D023 pp. 8–9, 14, 20–21, 26–27] to the 2022 preprint [D022].

<a id="promotions"></a>

## Promotions, new heuristics and the candidate pool

### Promotions (08 §4, copied)

**None.** The skill keeps its six core methods. Nine clusters reached three or more distinct works read in full or in part; none passes all four checks. The one that comes closest (row 5) passes exclusivity only in part and is a reading rule of Method 4, so it becomes a new step there.

| Cluster (merged by meaning) | Works read in full or part | 1 Recurrence | 2 Say–do | 3 Executable, non-standard | 4 Exclusivity | Result |
|---|---|---|---|---|---|---|
| Split the verdict by the answer required: a proof (infeasibility, validity, optimality) or a witness (a feasible point, a counter-example) | R004, R008, R009, R012, R015, D004 (6; D010 pp. 36–37 in prose) | ✅ conflict analysis 2005, property checking 2007–08, library sets 2010 | ✅ stated: "However, due to the much more involved procedures employed in our algorithm it is inferior to SAT for finding counter-examples of an invalid property." [R008 p. 14]; "For invalid properties, which are not shown in the tables, our algorithm is usually inferior to SAT for finding counter-examples." [R009 p. 14]; reasons for separate infeasible and primal sets [R015 pp. 6, 8]; practised [R004 pp. 16–19] | ✅ | ⚠ not shown to be his: the split follows the answer type of verification problems, and the co-signed library made it a library rule [R015 pp. 6, 8] | Heuristic-level; H8 widened (§5 A) |
| Delegate to the host: compute only the missing input, keep the host's machinery | D011, R014, R020, D020 (4; abstracts D006, D014) | ✅ Mcf 2010, ParaSCIP 2010–15, feedback arc sets 2021 | ✅ co-signed: "It is important to understand that our framework is not explicitly generating cutting planes. It only calculates weight vectors u." [D011 p. 3]; [R014 p. 2]; "Any research attempting to implement a novel cutting plane algorithm has to compete with that strong baseline." [D020 p. 11] | ✅ | ✗ building on a production solver, unmodified or through its extension interface, is common research practice (this note's reading) | Heuristic-level; variant notes on Method 5 step 1 and Method 6 step 3 (§5 D) |
| Let a heuristic part cost time, never correctness | R003, D004, D011, R013, R014 (5; D011 and R013 one study) | ✅ 2004, 2007, 2009–10, 2010 | ✅ sole practice [R003 p. 20; D004 p. 48]; stated co-signed [D011 p. 35]; "These changes only influence the path the solver takes, not the overall result." [R014 p. 11] | ✅ | ✗ a general robust-software habit | Heuristic-level; Method 1 step 0 (§5 B) |
| Prove the exact sub-decision hard, measure the literature heuristic, keep the cheapest rule on data at hand | R004, D004, R008, R009 (conflict analysis); D030, R021 (presolve) | ✅ two projects, 2005–2016 | ✅ [R004 p. 11; D004 p. 188; D030 pp. 3–4] | ✅ | ✗ | Heuristic-level; Method 2 step 2b (§5 C) |
| Read each claim on the subset that removes its confound (both-solved, equal path, all-optimal, same path; no affected count where both sides time out) | R004, D004, D010, R012, R021, D022, D023, D029 (8; D022 and D023 one line) | ✅ 2005–2025 | ✅ reasons stated [D022 p. 13; R021 p. 6; D004 p. 339; D029 p. 21] | ✅ | ⚠ solved-by-all and all-optimal subsets are shared practice in the SCIP community's papers; the equal-path block is his thesis's | Method 4 new step (§2); it is a reading rule of Method 4, not a new method |
| Time as a count times a unit cost: predict which factor moves, then read both | D004, D010, D026, D030, R021, R011, R002 (7) | ✅ 2004–2016 | ✅ predictions written before the runs [D026 pp. 8–9]; [D010 p. 29; D004 p. 194] | ✅ | ✗ | Method 2 step 2 alternative (§2) |
| Check every instrument against ground truth (detector, checker, feature space, published optima) | D011, R013, D021, D020, R005, R015, D013 (7; 5 studies) | ✅ 2005–2021 | ✅ co-signed practice | ✅ | ✗ | Heuristic-level; H4 widened (§5 E) |
| Linearize only what the LP can carry, propagate the rest | R008, D004, R009, D010 (4; abstract D007) | ✗ one project (chip verification) | ✅ [R009 p. 12; D010 p. 34] | ✅ | ✗ | Method 6 variant (§2) |
| Parallel-search devices: racing on variability, restarts used to reorganize the tree, repeats of nondeterministic runs | D017/R019, D018/R020, D029/R018, R022 (one project line) | ⚠ one line | ✗ no role assignable in Shinano-first texts | ✅ | — | Pool (§6) |

### New heuristic-level clusters (08 §5, how each was written into SKILL.md)

| 08 §5 | Cluster | Written into SKILL.md as |
|---|---|---|
| A | Metric and split by the answer the user needs | Heuristic 8 widened; taste quick-check; Agentic Protocol Step 2 bullet; Workflow D step 4; anti-pattern |
| B | Validity first | Method 1 step 0 |
| C | Prove the exact sub-decision hard, keep the cheapest rule | Method 2 step 2b; Workflow B step 5; PD1 |
| D | Delegate to the host (co-signed) | Method 5 step 1 variant; Method 6 step 3 variant via DM6 |
| E | Check every instrument against ground truth | Heuristic 4 widened; Method 5 step 4; Workflow C step 1 |
| F | Re-measure a published figure and explain the gap | Heuristic 6 widened |
| §4 row 5 | Control subsets | Method 4 step 4b; Workflow D step 2; EP5 |
| §4 row 6 | Count × unit cost | Method 2 step 2a; Workflow S step 3 |

No eleventh heuristic was added: SKILL.md has ten, the top of the band (5–10); 08 §5 names the answer-type split as the strongest candidate if a separate entry is wanted, with H2 merged into Method 3.

### Candidate pool (08 §6, copied)

All 96 new-pattern-candidate entries, each assigned to one row. *Works* counts distinct works (pairs merged); *full* counts those read in full or in part.

| Cluster (merged by meaning) | Entries | Works (full) | Decision |
|---|---|---|---|
| Delegate to the host / thin layer over the mature engine; correctness rows lazily, host cuts kept | 6 | 5 (4) | §5 D |
| Split results by answer type; complementary-strength portfolio | 6 | 6 (6) | §5 A |
| Let heuristic parts cost time, never validity; degrade, don't abort | 3 | 3 (3) + D004, R013 | §5 B |
| Hardness lemma, then the cheapest heuristic | 1 | 1 (1) + D004, R009, R008, D030, R021 | §5 C |
| Ground-truth the detector; validate a feature space | 3 | 2 (2) | §5 E |
| Exact rational re-check; certify only what can be certified | 2 | 2 (2) + D021 | §5 E; H7 evidence |
| Re-measure a published number and explain the gap | 3 | 3 (2) | §5 F |
| Control subsets: all-optimal, control run, same-path | 3 | 3 (3), D022 and D023 one line, + D004, R004, D010, R012, R021 | Method 4 new step (§2) |
| Node–time co-movement; predict which factor a change moves | 2 | 2 (2) + D010, D030, R021, R011 | Method 2 step 2 alternative (§2) |
| Linearize only what stays small, propagate the rest | 2 | 1 (1) + R008, D004, D010 | Method 6 variant (§2) |
| Predict non-transfer from discarded state | 1 | 1 (1) + R012, D010 | Method 6 step 4 mechanism (§2) |
| Per-call applicability guards | 1 | 1 (1) + R021, D018 | Method 1 evidence (§2) |
| Reverse the modeller's linearization | 1 | 1 (1) + D011 | Method 1 step 1 evidence (detection on the matrix) |
| Second-solver replication | 1 | 1 (1) + D011 | Method 1 step 5 evidence (two codes, 2010 and 2022–25) |
| Scalability grid with a deliberate worst-case family | 1 | 1 (1) | Method 1 variant (worst case as a test) |
| Correctness contract separate from speed callbacks | 2 | 2 (2) + D010 | Method 5 step 3 evidence; one SCIP design restated, not a heuristic |
| Version-stamp features and numbers | 1 | 1 (1) + D023, R022 | Method 5 evidence; writing move WM8 |
| Purge by a stripped-down reference configuration | 1 | 1 (1) | Method 5 evidence (test-set rule); EP10 |
| Purpose-specific sets with rule-based membership; test-set selection as an optimization model; cluster per feature group; per-solver performance clusterings | 4 | 2 (2) | Taste mark 6 and Method 5 evidence (co-signed library work); EP10 |
| Measure designed for the component's job | 2 | 1 (1) | H8 evidence (§2.7); Method 2 variant |
| Random rule as floor baseline | 2 | 2 (2), one project | H2 variant (§2.7) |
| Explain a small knock-out by the component that covers for it | 1 | 1 (1) + D004, R017 | Misreading 2 evidence (§2.7) |
| Per-iteration trajectory plots, a losing instance included | 1 | 1 (1) | H10 evidence; writing move WM5 |
| Formulation robustness as a design criterion | 1 | 1 (1) | H6 evidence (already in H6) |
| Collapse variants by presolve equivalence | 1 | 1 (1) | Already in H6; rejected as a duplicate (§10) |
| Phase time against phase resource share | 1 | 1 (1) | Method 2 evidence (co-signed) |
| Permutation-sampled variability score | 1 | 1 (1) | Misreading 1 rewording (§3.2 item 3) |
| Repeat only nondeterministic configurations; solved in all runs | 3 | 1 (1) | Misreading 1 rewording; EP18 |
| Exploit variability by racing; variability as diversification | 4 | 3 (3), one line | Pool; Roundtable Card note (§3.2 item 16) |
| Make the forced restart pay; a restart as a point to reorganize | 4 | 3 (3), one line | Pool (co-signed, no role) |
| Refuse a single-number solver ranking | 4 | 2 (2) | Pool: co-signed only, and at odds with his sole-authored single weighted total [D004 p. 336] and derived headline factor [D010 pp. 2, 29] |
| Name the substitute evidence when no protocol fits | 2 | 2 (2), one line | Pool (with the row above) |
| Fixed hard instance as a cross-version probe | 2 | 1 (1) | H5 variant (§2.7) |
| Count resources including lost work | 2 | 2 (2), one line | Pool |
| Open library instances as targets | 2 | 2 (1), one line | Pool |
| Parallelization as an algorithm change | 1 | 1 (1) | Pool |
| Collect, then apply, for determinism in parallel | 1 | 1 (1) + D029, D028 | Honest Boundary item (§3.2 item 20); DM19 |
| Mirror pruning for a new task | 2 | 1 (1) | Pool; DM14 |
| Necessary-condition pruning before separation; sign-based pre-filtering; projected check | 3 | 2 (2), one line | Pool; DM18 |
| Minimal exported summary to restore a hidden view | 1 | 1 (1) + R017, D023 (reuse) | Pool; DM7 |
| Order and warm-start a sequence of related LPs | 1 | 1 (1) | Pool; DM16 |
| Heuristic repair as separation oracle | 1 | 1 (1) | Pool; DM17 |
| Key the cycle test on the full iteration state | 1 | 1 (1) | Pool; DM15 |
| Clean the samples of an online estimator | 1 | 1 (1) | Pool; DM4 |
| Measure the quantity a fixed threshold depends on | 1 | 1 (1) | Pool; EP11 |
| Operational status classes kept live | 1 | 1 (1) | Pool (library practice) |
| Full model first as the yardstick for simplifications | 1 | 1 (1) | Pool (group work, 2002) |
| Sampled scenarios with a simulator in the loop | 1 | 1 (1) | Pool (group work, 2002) |
| Withheld under the holdout rule | 3 | 3 (3) | Two candidate entries forming one cluster, and one single-card candidate, lean on sealed material; their content waits for the validation that unseals it |
| **Total** | **96** | | |

<a id="rejected"></a>

## Rejected updates (08 §10, copied)

1. **A seventh core method for the answer-type split**: fails exclusivity; written into H8 (§5 A).
2. **A standalone heuristic *delegate to the host***: all evidence co-signed, and it duplicates Method 5 step 1 and Method 6 step 3; variant notes only (§5 D).
3. **A standalone heuristic *correctness contract separate from speed callbacks***: one SCIP design restated in 2004, 2008 and 2009 [R003 p. 9; R009 p. 5; D010 pp. 7–8], already Method 5 step 3.
4. ***Collapse variants by presolve equivalence* and *formulation robustness as a design criterion*** as new items: already in H6.
5. **Methods or heuristics from the ParaSCIP clusters** (racing on variability, forced restarts as reorganization points, repeats of nondeterministic runs, lost-work accounting, cross-version probes, phase-time diagnosis, parallelization as an algorithm change, open instances as targets): one project line, Shinano first, no role assignable to Achterberg; they enter only as variant notes on Misreading 1, H5 and the Roundtable Card.
6. ***Refuse a single-number solver ranking*** as a heuristic: co-signed only, and at odds with his sole-authored practice of one weighted total and a derived headline factor [D004 p. 336; D010 pp. 2, 29].
7. **Test-set selection as an optimization model** as a method of his: a 16-author committee paper; Taste mark 6 evidence only.
8. **Necessary-condition pruning before separation** as a heuristic: one study line (RLT), co-signed; technique inventory (DM18).
9. **A separate Method 4 or Method 2 for the control-subset and factor-split clusters**: both are reading rules of the existing methods; new steps instead (§2).
10. **Deleting Misreading 1**: reworded (§3.2 item 3), not deleted.
11. **Narrowing Method 3 because no Gurobi-era text sweeps a family**: absence of evidence in a closed-code period; an era note only.
12. **Carrying the cards' notes on inconsistencies inside works** (table against text, count slips, typos) into SKILL.md: barred by the house rule; one neutral lesson (WM9).
13. **Per-call applicability guards** as a heuristic: Method 1's no-op path applied per call; evidence only.

<a id="held-back"></a>

## Held back under the holdout rule

Two candidates, one cluster (two pool entries) and one single-card candidate, lean on material sealed in `holdout.md`. Their names and content are not written here or in SKILL.md; they wait for the validation that unseals them (08 §6, last row). No card page that carries a sealed item is cited in this file; the Before blocks keep the pre-synthesis wording and its printed-page keys as they were.

Fix round (2026-11-28): the T3.6 seal check covered card-id pages only. Two printed-page keys of the pre-synthesis text fall on pages that also carry sealed material; neither supports a sealed point, both stay only in Before blocks, and SKILL.md now cites other pages for what they supported. The fix round also compared three general clauses a reviewer named (Workflow D step 3 with Misreading 2, Heuristic 6's widening, catalog EP19) with `holdout.md` and found that none states a sealed point; the holdout owner may re-check before the validation is rerun.

<a id="sources"></a>

## Sources appendix

### Added in T3.6

- One line for the deep reading (INDEX.md, 07, 08, this ledger, the technique catalog).
- The sealed-material note now names the card batch files under `cards/` (b01, c01 and c06 contain sealed points, so the folder is excluded like notes 01–05) and states that 06, 07, 08, this ledger and the catalog hold none.
- Fix round (2026-11-28): the sealed-material note also names `FIDELITY.md` (its increment-test and known-weak-points sections describe the sealed answers) and the local full texts under `../sources/papers/` (they carry the sealed pages: open only a cited page, none while testing); the 07 line notes that its batch links open the closed card files.
- Each source key now names its card id; *revised ZIB copy read in part* → *read at chapter level (card D004)*; MPC 2009 *(abstract only)* → *(read in full: D010)*; A&W 2013 *(not read)* → *(abstract only: D028)*; *Hybrid Branching … (not read)* → *(abstract only: D009)*; the Mcf journal version read (D011); RLT cards D022 and D023; MIPLIB 2017 card D021.

### Before T3.6 (moved verbatim)

**Sources (Appendix)**

Full evidence is in the research notes under `references/research/`. Notes 01–05, `holdout.md` and the interview excerpt file under `references/sources/talks/` also hold sealed validation material: do not open them while using or testing this skill. The [trajectory note](06-trajectory.md) holds none. Every DOI here resolved in Crossref (DataCite for the theses and Zenodo) and both arXiv ids on the arXiv API on 2026-11-14.

**Papers (primary)**

- [THESIS] *Constraint Integer Programming*, TU Berlin 2007, DOI 10.14279/depositonce-1634; revised ZIB copy read in part: https://opus4.kobv.de/opus4-zib/files/1112/Achterberg_Constraint_Integer_Programming.pdf
- [ZR 02-32] with Koch, Martin, *Branching on History Information*, 2002, https://nbn-resolving.org/urn:nbn:de:0297-zib-6990
- [ZR 04-13] with Koch, Martin, *Branching rules revisited*, Oper. Res. Lett. 2005, DOI 10.1016/j.orl.2004.04.002; report https://opus4.kobv.de/opus4-zib/files/788/ZR-04-13.pdf
- [ZR 04-19] *SCIP – a framework to integrate Constraint and Mixed Integer Programming*, 2004, https://nbn-resolving.org/urn:nbn:de:0297-zib-7947
- [ZR 05-19] *Conflict analysis in mixed integer programming*, Discrete Optim. 2007, DOI 10.1016/j.disopt.2006.10.006; report https://opus4.kobv.de/opus4-zib/files/853/ZR-05-19.pdf
- [ZR 05-42] with Berthold, *Improving the feasibility pump*, Discrete Optim. 2007, DOI 10.1016/j.disopt.2006.10.004
- [ZR 05-28] with Koch, Martin, *MIPLIB 2003*, Oper. Res. Lett. 2006, DOI 10.1016/j.orl.2005.07.009
- [ZR 08-29] with Koch, Tuchscherer, *On the Effects of Minor Changes in Model Formulations*, 2008, https://nbn-resolving.org/urn:nbn:de:0297-zib-10808
- [ZR 09-38] with Raack, *The Mcf-separator*, Math. Program. Comput. 2010, DOI 10.1007/s12532-010-0015-3; report https://opus4.kobv.de/opus4-zib/files/1159/ZR_09_38.pdf
- [RAMP 2014] with Bixby, Gu, Rothberg, Weninger, *Multi-Row Presolve Reductions in Mixed Integer Programming*, Proc. 26th RAMP Symposium, pp. 181–196, https://orsj.org/ramp/wp-content/uploads/sites/9/2021/03/paper2014_4-4.pdf
- [ZR 16-44] same authors, *Presolve Reductions in Mixed Integer Programming*, INFORMS J. Comput. 2020, DOI 10.1287/ijoc.2018.0857; report https://opus4.kobv.de/opus4-zib/files/6037/Presolve.pdf
- [A&W 2013] with Wunderling, *Mixed Integer Programming: Analyzing 12 Years of Progress*, DOI 10.1007/978-3-642-38189-8_18 (not read)
- [MPC 2009] *SCIP: solving constraint integer programs*, DOI 10.1007/s12532-008-0001-1 (abstract only); *Hybrid Branching* with Berthold, DOI 10.1007/978-3-642-01929-6_23 (not read)
- [RLT] Bestuzheva, Gleixner, Achterberg, Math. Program. 210:47–74, DOI 10.1007/s10107-024-02104-0; arXiv:2211.13545. MIPLIB 2017, DOI 10.1007/s12532-020-00194-3

**Stated methodology (primary)**

- THESIS acknowledgements pp. ix–x, Introduction, Appendix A
- [SEA 2022] slides, https://sea2022.ifi.uni-heidelberg.de/talk_achterberg.pdf ; [CPAIOR 2017] slides, https://cpaior2017.dei.unipd.it/slides/Achterberg.pdf ; [ORIGINS 2022] slides, https://www.scipopt.org/20years/slides/achterberg.pdf ; [MIPW 2025] https://www.mixedinteger.org/2025/
- [INT 2023] "Subject to: Tobias Achterberg", https://www.youtube.com/watch?v=8bhIW27vCUQ (captions)
- [WEB] Gurobi webinars (captions): 9.0 https://www.youtube.com/watch?v=WkIcLO_d7aI ; 9.1 https://www.youtube.com/watch?v=EwuEPu-nBmg ; 9.5 https://www.youtube.com/watch?v=UFV4ZYsHFdY ; 10.0 https://www.youtube.com/watch?v=n0sEYVtIqvw ; 13.0 https://www.youtube.com/watch?v=NdGUcuskm0w ; 11.0 deck https://cdn.gurobi.com/wp-content/uploads/Whats-New-in-Gurobi-11.0_Webinar-slides.pdf

**Process evidence (primary)**

- SCIP repository https://github.com/scipopt/scip (clone of 8 Nov 2026): the commits cited by hash, file headers, CHANGELOG
- Run tables in THESIS Appendices B–C, ZR 02-32, ZR 05-19, ZR 08-29, ZR 16-44

**Students, collaborators and peers (secondary)**

- Berthold, thesis 2014, http://www.zib.de/berthold/Berthold2014.pdf ; Gamrath, thesis 2020, DOI 10.14279/depositonce-10710
- Koch, Berthold, Pedersen, Vanaret 2022, DOI 10.1016/j.ejco.2022.100031; Mexi et al., arXiv:2410.15110; Khalil et al. 2016, DOI 10.1609/aaai.v30i1.10080
- Other papers are cited inline with their DOIs.

<a id="card-key"></a>

## Card key

One line per card id: year, work, read level of the best card, batch file, the version read and its page offset, and the source key the pre-synthesis SKILL.md used for it. Cards are in [07-paper-cards.md](07-paper-cards.md); batch files under `cards/` (sealed points in some: do not open them while using or testing the skill; the same holds for `../../FIDELITY.md`, which describes the sealed items, and for the local full texts beyond the pages the skill cites). To cite a card page in a reply, convert it to the printed page with the offset in the column *Version read and page offset*.

| Card | Year | Work | Read level (best card) | Batch | Version read and page offset | Pre-synthesis key |
|---|---|---|---|---|---|---|
| D001 | 2005 | Branching rules revisited (Operations Research Letters 33(1): 42-54) | metadata | a2-01 | published version, no text of its own; read through its report R002 | ZR 04-13 (journal) |
| D002 | 2006 | MIPLIB 2003 (Operations Research Letters 34(4): 361-372) | metadata | a2-01 | published version, no text of its own; read through its report R005 | ZR 05-28 (journal) |
| D003 | 2007 | Conflict analysis in mixed integer programming (Discrete Optimization 4(1): 4-20) | metadata | a2-01 | published version, no text of its own; read through its report R004 | ZR 05-19 (journal) |
| D004 | 2007 | Constraint Integer Programming (Doctoral thesis, Technische Universität Berlin) | partial | b01 | revised ZIB copy (OPUS docId 1112), 426 pp.; file = printed + 14 in the main text, front matter roman = file page; chapter map on the card | THESIS |
| D005 | 2007 | Improving the feasibility pump (Discrete Optimization 4(1): 77-86) | metadata | a2-01 | published version, no text of its own; read through its report R006 | ZR 05-42 (journal) |
| D006 | 2008 | A Dynamic Load Balancing Mechanism for New ParaLEX (2008 14th IEEE International Conference on Parallel and Dist) | abstract | a2-01 | abstract or metadata only; no text read | — |
| D007 | 2008 | Constraint Integer Programming: A New Approach to Integrate CP and MIP (CPAIOR 2008, Lecture Notes in Computer Science 5015: 6-20) | abstract | a2-01 | published version, no text of its own; read through its report R009 | — |
| D008 | 2008 | Counting Solutions of Integer Programs Using Unrestricted Subtree D… (CPAIOR 2008, Lecture Notes in Computer Science 5015: 278-282) | abstract | a2-01 | published version, no text of its own; read through its report R010 | — |
| D009 | 2009 | Hybrid Branching (CPAIOR 2009, Lecture Notes in Computer Science 5547: 309-311) | abstract | a2-01 | abstract or metadata only; no text read | MPC 2009 line (Hybrid Branching) |
| D010 | 2009 | SCIP: solving constraint integer programs (Mathematical Programming Computation 1(1): 1-41) | full | c03 | 41 file pages; journal text; file = journal page (1–41) | MPC 2009 |
| D011 | 2010 | The Mcf-separator: detecting and exploiting multi-commodity flow st… (Mathematical Programming Computation 2(2): 125-165) | full | c04 | 41 file pages; journal text; file = printed − 124 (file 1 = p. 125); one study with R013 | ZR 09-38 (journal) |
| D012 | 2011 | Integration of AI and OR Techniques in Constraint Programming for C… (Lecture Notes in Computer Science 6697, Springer (proceeding) | abstract | a2-01 | abstract or metadata only; no text read | — |
| D013 | 2011 | MIPLIB 2010 (Mathematical Programming Computation 3(2): 103-163) | full | c05 | 61 file pages; journal text; file = printed − 102 (file 1 = p. 103); one study with R015 | — |
| D014 | 2012 | ParaSCIP: A Parallel Extension of SCIP (Competence in High Performance Computing 2010 (CHPC 2010), S) | abstract | a2-01 | published version, no text of its own; read through its report R014 | — |
| D015 | 2012 | Rounding and Propagation Heuristics for Mixed Integer Programming (Operations Research Proceedings 2011, Springer: 71-76) | abstract | a2-01 | published version, no text of its own; read through its report R017 | — |
| D016 | 2013 | Stronger Inference through Implied Literals from Conflicts and Knap… (CPAIOR 2013, Lecture Notes in Computer Science 7874: 1-11) | abstract | a2-01 | abstract or metadata only; no text read | — |
| D017 | 2014 | Solving Hard MIPLIB2003 Problems with ParaSCIP on Supercomputers: A… (2014 IEEE International Parallel & Distributed Processing Sy) | full | c05 | 22 file pages; TR: ZIB-Report 13-66, revision of April 2014; report page = file − 2; one study with R019 | — |
| D018 | 2016 | Solving Open MIP Instances with ParaSCIP on Supercomputers Using up… (2016 IEEE International Parallel and Distributed Processing ) | full | c06 | 23 file pages; TR: ZIB-Report 15-53, revision of February 2016; report page = file − 2; one study with R020 | — |
| D019 | 2020 | Presolve Reductions in Mixed Integer Programming (INFORMS Journal on Computing 32(2): 473-506) | abstract | a2-01 | published version, no text of its own; read through its report R021 | ZR 16-44 (journal) |
| D020 | 2021 | An Exact Method for the Minimum Feedback Arc Set Problem (ACM Journal of Experimental Algorithmics 26: 1.4:1-1.4:28) | full | c07 | 28 file pages; journal text; file N = article page 1.4:N | — |
| D021 | 2021 | MIPLIB 2017: data-driven compilation of the 6th mixed-integer progr… (Mathematical Programming Computation 13(3): 443-490) | full | c07 | 48 file pages; journal text; file = printed − 442 (file 1 = p. 443) | RLT line (MIPLIB 2017) |
| D022 | 2023 | Efficient Separation of RLT Cuts for Implicit and Explicit Bilinear… (IPCO 2023, Lecture Notes in Computer Science 13904: 14-28) | full | c07 | arXiv 2211.13545v1 (ZIB-Report cover on file pp. 1–2); preprint page = file − 2 | RLT |
| D023 | 2025 | Efficient separation of RLT cuts for implicit and explicit bilinear… (Mathematical Programming (Series B) 210(1-2): 47-74) | full | c08 | 28 file pages; arXiv 2211.13545v3; file = arXiv page; journal pages not mapped | RLT |
| D024 | 2003 | Modelling Feasible Network Configurations for UMTS (Telecommunications Network Design and Management (eds. G. An) | full | c01, c2-01 | 27 file pages; round 2 (c2-01): TR, ZIB-Report 02-16 (March 2002, as T. Pfender); file = printed + 1. Round 1 (c01): unreadable as named, superseded | — |
| D025 | 2006 | Teaching MIP Modeling and Solving (OR/MS Today 33(6): 14-15 (INFORMS magazine)) | metadata | a2-01 | abstract or metadata only; no text read | — |
| D026 | 2009 | Computation of an extractive distillation column with affine arithm… (AIChE Journal 55(7): 1695-1704) | full | c03 | 46 file pages; authors' preprint; file = preprint sheet | — |
| D027 | 2011 | Hybrid Solving Techniques (Hybrid Optimization: The Ten Years of CPAIOR (Springer Optim) | abstract | a2-01 | abstract or metadata only; no text read | — |
| D028 | 2013 | Mixed Integer Programming: Analyzing 12 Years of Progress (Facets of Combinatorial Optimization, Springer: 449-481) | abstract | a2-01 | abstract or metadata only; no text read | A&W 2013 |
| D029 | 2013 | Parallelizing the Constraint Integer Programming Solver SCIP (Proceedings of the Institute of Statistical Mathematics (統計数) | full | s02 | 32 file pages; journal text (Japanese); file = printed − 46 (file 1 = p. 47); one study with R018 | — |
| D030 | 2014 | Multi-Row Presolve Reductions in Mixed Integer Programming (Proceedings of the Twenty-Sixth RAMP Symposium, Hosei Univer) | full | c06 | 16 file pages; proceedings text; file = printed − 180 (file 1 = p. 181) | RAMP 2014 |
| D036 | 2000 | Arboreszenz-Flüsse in Graphen: polyedrische Untersuchungen (Diplomarbeit (diploma thesis), Technische Universität Berlin) | metadata | a2-01 | abstract or metadata only; no text read | — |
| R001 | 2002 | Branching on History Information (ZIB-Report 02-32, Zuse Institute Berlin) | full | c01 | 16 file pages; ZIB-Report; file = printed + 1 (file 1 = cover) | ZR 02-32 |
| R002 | 2004 | Branching rules revisited (ZIB-Report 04-13, Zuse Institute Berlin) | full | c01 | 60 file pages; ZIB-Report; file = printed + 1 (file 1 = cover) | ZR 04-13 |
| R003 | 2004 | SCIP - a framework to integrate Constraint and Mixed Integer Progra… (ZIB-Report 04-19, Zuse Institute Berlin) | full | c02 | 29 file pages; ZIB-Report; file = printed + 1 (file 1 = cover) | ZR 04-19 |
| R004 | 2005 | Conflict Analysis in Mixed Integer Programming (ZIB-Report 05-19, Zuse Institute Berlin) | full | c02 | 20 file pages; ZIB-Report; file = printed + 1 (file 1 = cover) | ZR 05-19 |
| R005 | 2005 | MIPLIB 2003 (ZIB-Report 05-28, Zuse Institute Berlin) | full | c02 | 15 file pages; ZIB-Report; file = printed + 1 (file 1 = cover) | ZR 05-28 |
| R006 | 2005 | Improving the Feasibility Pump (ZIB-Report 05-42, Zuse Institute Berlin) | full | c02 | 12 file pages; ZIB-Report; file = printed + 1 (file 1 = cover) | ZR 05-42 |
| R007 | 2006 | Software for Teaching Modeling of Integer Programming Problems (ZIB-Report 06-23, Zuse Institute Berlin) | full | s01 | 13 file pages; ZIB-Report; file = printed + 1 (file 1 = cover) | — |
| R008 | 2007 | Property Checking with Constraint Integer Programming (ZIB-Report 07-37, Zuse Institute Berlin) | full | s01 | 16 file pages; ZIB-Report; file = printed + 1 (file 1 = cover) | — |
| R009 | 2008 | Constraint Integer Programming: a New Approach to Integrate CP and MIP (ZIB-Report 08-01, Zuse Institute Berlin) | full | c02 | 16 file pages; ZIB-Report; file = printed + 1 (file 1 = cover) | — |
| R010 | 2008 | Counting solutions of integer programs using unrestricted subtree d… (ZIB-Report 08-09, Zuse Institute Berlin) | full | c03 | 6 file pages; ZIB-Report; file = printed + 1 (file 1 = cover) | — |
| R011 | 2008 | On the Effects of Minor Changes in Model Formulations (ZIB-Report 08-29, Zuse Institute Berlin) | full | c03 | 11 file pages; ZIB-Report; file = printed + 1 (file 1 = cover) | ZR 08-29 |
| R012 | 2008 | Constraint Integer Programming: Techniques and Applications (ZIB-Report 08-43, Zuse Institute Berlin) | full | s01 | 24 file pages; ZIB-Report; file = printed + 1 (file 1 = cover) | — |
| R013 | 2009 | The MCF-Separator -- Detecting and Exploiting Multi-Commodity Flow… (ZIB-Report 09-38, Zuse Institute Berlin) | full | s01 | 61 file pages; ZIB-Report; file = printed + 1 (file 1 = cover); one study with D011 | ZR 09-38 |
| R014 | 2010 | ParaSCIP - a parallel extension of SCIP (ZIB-Report 10-27, Zuse Institute Berlin) | full | c04 | 14 file pages; ZIB-Report; file = printed + 1 (file 1 = cover) | — |
| R015 | 2010 | MIPLIB 2010 (ZIB-Report 10-31, Zuse Institute Berlin) | full | s01 | 47 file pages; ZIB-Report; file = printed + 2 (file 1 = cover, 2 = imprint); one study with D013 | — |
| R016 | 2011 | CPAIOR 2011 - Late Breaking Abstracts (ZIB-Report 11-20, Zuse Institute Berlin) | partial | s01 | edited collection; preface and contents on file pp. 3–6; abstract page n = file n + 6 | — |
| R017 | 2011 | Rounding and Propagation Heuristics for Mixed Integer Programming (ZIB-Report 11-29, Zuse Institute Berlin) | full | c05 | 18 file pages; ZIB-Report; file = printed + 2 (file 1 = cover, 2 = imprint) | — |
| R018 | 2013 | Parallelizing the Constraint Integer Programming Solver SCIP (ZIB-Report 13-22, Zuse Institute Berlin) | full | s02 | 25 file pages; ZIB-Report; file = printed + 2 (file 1 = cover, 2 = imprint); one study with D029 | — |
| R019 | 2013 | Solving hard MIPLIB2003 problems with ParaSCIP on Supercomputers: A… (ZIB-Report 13-66, Zuse Institute Berlin) | full | s02 | 21 file pages; ZIB-Report; file = printed + 2 (file 1 = cover, 2 = imprint); one study with D017 | — |
| R020 | 2015 | Solving Open MIP Instances with ParaSCIP on Supercomputers using up… (ZIB-Report 15-53, Zuse Institute Berlin) | full | s02 | 22 file pages; ZIB-Report; file = printed + 2 (file 1 = cover, 2 = imprint); one study with D018 | — |
| R021 | 2016 | Presolve Reductions in Mixed Integer Programming (ZIB-Report 16-44, Zuse Institute Berlin) | full | c06 | 70 file pages; ZIB-Report; file = printed + 2 (file 1 = cover, 2 = imprint) | ZR 16-44 |
| R022 | 2020 | Solving Previously Unsolved MIP Instances with ParaSCIP on Supercom… (ZIB-Report 20-16, Zuse Institute Berlin) | full | s02 | 25 file pages; ZIB-Report; file = printed + 2 (file 1 = cover, 2 = imprint) | — |

Not carded: two IBM patents (Role = skip in INDEX.md, not read). Studies after merging pairs: 39 (08 §1).

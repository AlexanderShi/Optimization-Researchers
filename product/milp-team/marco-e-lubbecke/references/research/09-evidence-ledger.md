# Marco E. Lübbecke · Evidence ledger

## Contents

- [How to Use, front matter and the first-activation disclaimer](#how-to-use) · [Routing and Agentic Protocol](#routing) · [Taste: marks](#taste-marks) · [Taste: warning signs and quick-check](#taste-warnings)
- [Method 1](#method-1) · [Method 2](#method-2) · [Method 3](#method-3) · [Method 4](#method-4) · [Method 5](#method-5)
- [Stage workflows](#workflows)
- Heuristics: [H1](#heuristic-1) · [H2](#heuristic-2) · [H3](#heuristic-3) · [H4](#heuristic-4) · [H5](#heuristic-5) · [H6](#heuristic-6) · [H7](#heuristic-7) · [H8](#heuristic-8) · [H9](#heuristic-9) · [H10](#heuristic-10) · [H11](#heuristic-11) · [H12](#heuristic-12) · [H13](#heuristic-13)
- [Common misreadings](#misreadings)
- Anatomies: [SEA 2010](#anatomy-sea2010) · [IPCO 2011 and MP 2015](#anatomy-ipco2011) · [Selected Topics and the book](#anatomy-survey) · [k-vertex cut](#anatomy-kvertexcut) · [coil coating](#anatomy-coilcoating) · [SEA 2018 and the stable-set theory](#anatomy-sea2018)
- [Anti-patterns](#anti-patterns) · [Trajectory](#trajectory) · [Inner tensions](#inner-tensions) · [Roundtable Card](#roundtable-card)
- [Honest Boundary](#honest-boundary) · [Corrections from the full texts](#corrections) · [Promotions and the candidate pool](#promotions) · [Rejected updates](#rejected) · [Review fixes](#review-fixes) · [Held back under the holdout rule](#held-back) · [Card key](#card-key)

> Date: 2026-11-28 (stage T3.6, team-synthesize). The full evidence behind `../../SKILL.md`. SKILL.md keeps, per item, the strongest statement and cards, a one-line say–do count, at most four variant or correction bullets and a pointer to the matching section here. Each section has up to four parts: **Full-text evidence** (copied word for word from [08-deep-reading-synthesis.md](08-deep-reading-synthesis.md), which is traceable to the cards, or written here from the named cards), **Variants, contradictions and corrections** (08 §3–§5, copied), **Added in T3.6** (what this pass wrote into SKILL.md, with card ids) and **Before T3.6 (moved verbatim)** (the SKILL.md item as it stood on 2026-11-14, built from web research without full texts, kept in a fenced block so that nothing is lost; its quotes and keys come from research notes 01–06 as they stood then). Copied 08 text is left as copied; § numbers inside it refer to 08. 08 itself is not edited.
>
> **How to read.** `[S012 p. 9]` is paper card S012, at the `[[page N]]` page of the file the card read (`../sources/papers/INDEX.md`). A word between id and page names a version read in place of the published one: `report`, `preprint` and `arXiv` (recognised by `check_citations.py`), `manuscript`, `pre-publication` and `in-press` (plain cites on the indexed file); the [card key](#card-key) gives each card's version and its published form. Abstract- and metadata-level cards are cited by id only. Marks: ✅ evidence · ⚠ variant (kept, nothing deleted) · ✗ contradiction or correction. Technique ids PD, DM, EP and WM are entries of [../technique-catalog.md](../technique-catalog.md); 08 §7 numbers the same entries P, D, E and W with the same numbers (08's D9 is the catalog's DM9). Quotation marks outside the fenced Before blocks enclose only text copied from a card's verified quote list (`verify_card_quotes.py`, 2026-11-28: 188 quotes, 187 exact, 1 matching after spacing normalisation, 0 not found); wording of SKILL.md itself is set in italics.
>
> **Voices.** The book *Branch-and-Price* (S017, Role skip; four authors) is carded through its eight chapters (S087, S060, S086, S084, S085, S088, S077, D004) and counts as one source toward every three-work threshold; no passage in it is Lübbecke's alone. The Braunschweig switching-engine project (thesis S027, with S024, S054, S033, S066, and the group paper S037) counts as one project. Sole-authored texts read: S083 (in part), S027, S066, S033, S008, S070, S048; all later work is group or co-signed text.
>
> **Not carried.** The cards' reading notes on inconsistencies inside a work (a table that disagrees with its text, a typo, numbers that look carried over) are not findings about the researcher or his coauthors and are not used; 08 §7.4 keeps one neutral lesson (catalog WM11). Material sealed in `holdout.md` is not used: no point, quote or decision of a sealed item appears in this file. The card batch files b01, c01 and s01 under `cards/`, the S027 row of `07-paper-cards.md` and research notes 01, 03, 05 and 06 hold sealed passages; they are named here only as sources and must not be opened while using or testing the skill (the other batch files hold none; SKILL.md links none of the files named here). Candidates that lean on sealed material are named, not described ([Held back](#held-back)).
>
> **Counts.** `team_status.py --coverage` on 2026-11-28: 120 Scholar rows · 116 distinct works indexed · 94 open full texts · 89 read in full · 3 in part · 7 abstract only · 10 metadata only (incl. unreadable) · 7 skipped · 0 book material carded · 188 quotes verified. Card entries: 111 on 110 works (S030 twice). Word budget after this pass: 11,562 words outside the Answer Standard by `answer_standard.py --words` (target about 11,500, hard limit 13,000); after the review fixes: 12,743 words ([Review fixes](#review-fixes)).

<a id="how-to-use"></a>

## How to Use, front matter and the first-activation disclaimer

> Changed in the T3.6 review fixes: see [Review fixes](#review-fixes).

### Full-text evidence (08 §1, copied)

### 1.1 Counts

| Item | Count | Source |
|---|---|---|
| Scholar rows / distinct works indexed | 120 / 116 | 07 coverage row (`team_status.py --coverage`) |
| Open full text on disk | 94 (22 no-oa) | INDEX.md |
| Card entries / works with a card | 111 / 110 (S030 has an abstract card in a2-01 and a full card in s3-01) | digests |
| Read in full | 89 works | digests |
| Read in part | 3 works: the Diplom thesis S083 and two LP-degeneracy papers S038, S049 | digests |
| Abstract only | 7 works: S045, S056, S062, S064, S072, S100, H001 | digests |
| Metadata only | 11 entries: S059, S069, S082, S106, S108, S110, S111, S114, S119, S120, and S102, a row that is not his work (works.json note) | digests |
| Indexed rows without a card | 6, all Role skip: the book S017 (its chapters are carded separately), the talks S079, S098, S099 and D005, the complete volume S103 | INDEX.md |
| INDEX Read column after `mark_read_from_cards.py` | carded 89, skimmed 3, abstract 7, metadata 11, — 6 | script output, 2026-11-28 |

Distinct works per five-year period (best card per id; read in full or in part in brackets): 1996-2000 6 [5]; 2001-2005 14 [14]; 2006-2010 20 [16]; 2011-2015 24 [16]; 2016-2020 24 [22]; 2021-2026 19 [19], eight of them the book's chapters; undated 3 [0].

Linked to no method: 18 entries, the 15 abstract- or metadata-level entries of a2-01 that carry no method link and three editorial texts read in full (S107, S109, D003).

### 1.2 Versions read (citation key)

| Work | Version the card read | Cited as |
|---|---|---|
| S001 | TU Berlin report 2004/08, revised March 2004 (neither the journal text nor the October 2004 revision) | [S001 report p. N] |
| S002 | pre-publication chapter copy, marked as to appear | [S002 pre-publication p. N] |
| S007, S008 | the authors' encyclopedia manuscripts of 2010 | [S007 manuscript p. N], [S008 manuscript p. N] |
| S012 | TU Berlin report 2003/43 | [S012 report p. N] |
| S014 | arXiv:2303.07101v1 | [S014 arXiv p. N] |
| S015 | Optimization Online preprint, revised 2013 | [S015 preprint p. N] |
| S018 | manuscript submitted to *Operations Research* | [S018 manuscript p. N] |
| S021 | TU Berlin report 2003/25 | [S021 report p. N] |
| S025 | preprint of 22 June 2016 | [S025 preprint p. N] |
| S030 | arXiv cs/0310034v1, the SODA 2004 extended abstract | [S030 arXiv p. N] |
| S031 | author preprint, revised 2013 | [S031 preprint p. N] |
| S032 | an authors' preprint of the IPCO paper (batch c03 header): own pages 1-15, appendix A on pp. 12-15, LNCS pp. 39-51 not mapped | [S032 manuscript p. N] |
| S033 | TU Berlin report 2003/42 | [S033 report p. N] |
| S036 | authors' preprint, revised 2004 | [S036 preprint p. N] |
| S041 | manuscript submitted to JEA | [S041 manuscript p. N] |
| S043 | SSRN preprint, April 2020 | [S043 preprint p. N] |
| S049 | journal-template manuscript | [S049 manuscript p. N] |
| S050 | preprint in SIAM style | [S050 preprint p. N] |
| S052 | article-in-press version | [S052 in-press p. N] |
| S054, S066 | chapter manuscript; submitted manuscript of 2003 | [S054 manuscript p. N], [S066 manuscript p. N] |
| S074 | Open Research Exeter accepted manuscript | [S074 manuscript p. N] |
| D001 | arXiv cs/0310034v3 | [D001 arXiv p. N] |

The SCIP suite reports S005, S006, S013 and S019, the 2026 preprints S075, S076, S089 (read as v2) and S115, and the book chapters are the indexed files themselves and are cited plainly.

### 1.3 Voice

Sole-authored texts read: the Diplom thesis S083 (1996, read in part), the doctoral thesis S027 (2001), S066 (2004), S033 (2005), the encyclopedia entry S008 (2011), the SEA 2012 status report S070 and the TOP comment S048 (2015). The last sole-authored text read is the 2015 TOP comment; every later work is group or co-signed text, and the chair preprints of 2026 give his CRediT roles as conceptualization, methodology, supervision and review [S075 p. 28; S115 p. 31]. The suite reports name him for coordination: "coordinated and supervised the development of GCG" [S019 p. 40].

### Added in T3.6

- **Front matter**: `researched:` 2026-11-14 → 2026-11-28. The description was 969 characters; it is now 854: it names the coverage (*92 read in full or in part*), adds *to certify a heuristic with a bound*, shortens the list of source kinds and drops *to choose among many possible reformulations* (Method 2 is named in How to Use); the trigger phrases and the non-trigger clause are unchanged.
- **Strong at**: one bullet added, *Delivering a heuristic with a certified gap (Method 5)*.
- **Weak at**: numerics and exact solving are now *a stated position on tolerances and exact arithmetic, no study* [S008 manuscript p. 13] (08 §3.3 C14; the book repeats the position [S060 pp. 23–24]); variability protocols are *co-signed in suite reports only* [S013 pp. 14, 70–71; S019 pp. 4–7]; nonlinear optimization carries the nuance of 08 §3.3 C20 [S012 report pp. 9–12; S025 preprint pp. 8–15].
- **Pointers and labels**: one sentence added: research notes 01, 03, 05 and 06 hold sealed passages (Sources appendix).
- **Card citations** (new paragraph): the citation form, the version words, the card key and the technique catalog.
- **Voices** (new paragraph): sole-authored full texts end in 2015 [S027; S008; S070; S048]; later work is group or co-signed, his CRediT roles in 2026 [S075 p. 28; S115 p. 31]; the book counts as one source (08 §1.3, header).
- **Disclaimer line** (Activation Rules, the only line changed there): + *92 of the 116 works indexed for him were read in full or in part, the rest from abstracts or metadata; researched on 2026-11-28* (this member's `team_status.py --coverage` row: 89 full + 3 partial of 116 distinct works).
- **Changed by the operator's hand edit (2026-11-28)**: Activation Rules' *Nothing in the record* line no longer names *numerics* and *Benders design* as examples; the full texts date both (08 §3.3 C14, C17). T3.6 may change Activation Rules only in the disclaimer line (`check_ledger.py --allow frontmatter,activation-disclaimer`), so the deletion detector reports this line, by design.

### Before T3.6 (moved verbatim)

Front matter, How to Use and the disclaimer line (2026-11-14):

````text
---
name: marco-e-lubbecke
description: |
  Marco E. Lübbecke's research craft in decomposition for mixed-integer linear programs (Dantzig-Wolfe reformulation, column generation, branch-and-price, the GCG solver), distilled from his papers, his 2001 thesis, his sole-authored 2015 TOP comment, his blog, talks and posts, his own GCG commits, his students' theses and his critics' papers. Use it to decide whether a MILP is worth decomposing and how to find out before building, to design a branch-and-price code and its experiments, to choose among many possible reformulations, and to size a computational claim to its evidence. Triggers: "Lübbecke lens" (also Luebbecke, Lubbecke), "ask Lübbecke", "how would Lübbecke approach this", "what would Lübbecke say about our pricing, decomposition or experiments", "Lübbecke-style review", "use Lübbecke's method", "Lübbecke.skill". Also loaded by milp-roundtable. Not for routine GCG or SCIP usage help, or for questions that name neither Lübbecke nor the MILP Team.
type: research-craft
researched: 2026-11-14
---
````

````text
## How to Use

**Strong at** (stages with evidence):
- Deciding whether to decompose a MILP (Dantzig-Wolfe, branch-and-price) or stay with branch-and-cut, and measuring that before writing code.
- Building and tuning column-generation and branch-price-and-cut codes on a framework.
- Choosing among many reformulations, rules or components by enumerating them on small models.
- Designing computational experiments for a solver component and sizing the claim.
- Turning unexplained effects into a survey that becomes an agenda; questioning the owner of an applied model.

**Weak at** (no evidence, or outside his field): numerics, tolerances, exact solving, parallel and deterministic search, performance-variability protocols; nonlinear optimization ("too complicated for me", podcast 2021); literature-search routines, funding, rebuttals, daily supervision; line-level code design (GCG's algorithmic code is his group's).

**Domain adaptation.** For a branch-and-cut engineer: "compact model as benchmark" becomes "the default path is the baseline every new mode must beat"; "enumerate small" applies to cut selection, branching and presolve orderings. Group-scale items carry versions for a lone researcher.

**Pointers and labels.** "02 §4.4" is section 4.4 of the research note [02-methodology.md](references/research/02-methodology.md); the others are [01-publications.md](references/research/01-publications.md), [03-process-evidence.md](references/research/03-process-evidence.md), [04-mentorship.md](references/research/04-mentorship.md), [05-peer-critique.md](references/research/05-peer-critique.md), [06-trajectory.md](references/research/06-trajectory.md). **[stated]** his single voice; **[stated-joint]** co-signed text (the four-author 2026 book, a 2020 editorial, abstracts); **[practice]** papers, code, records; **[group]** RWTH group code and documents; **[inferred]** this skill's reading. "ASR": YouTube automatic captions, not checked against the audio.

---
````

````text
- On first activation say once: "This is distilled from Lübbecke's public work (papers, code, talks, posts) and others' observations; it is not Lübbecke's own advice." Do not repeat it. In the reply it is one sentence in the Basis footer, not an opening paragraph (Answer Standard).
````

<a id="routing"></a>

## Research Task Routing and Agentic Protocol

> Changed in the T3.6 review fixes: see [Review fixes](#review-fixes).

### Full-text evidence (08 §3.3 and §5, copied)

| # | SKILL.md item | What the full texts show | Cards |
|---|---|---|---|
| C14 | How to Use *Weak at: numerics, tolerances, exact solving*; Honest Boundary *nothing on numerics, exact arithmetic*; Roundtable Card blind spot *no numerics, exact solving* | a sole-authored 2010 paragraph names the tolerances at the master-pricing interface (negative reduced cost, bound match, perturbation size 10^-3 to 10^-6), warns that testing against 0.0 loops, and takes a position: "An alternative is to resort to exact (rational) arithmetic; but due to performance reasons this is only advisable for mission critical linear and integer programs."; the book sets one tolerance for RMP and pricing and rounds columns at the pricing integrality tolerance; framework features that would invalidate a dual bound are switched off during pricing ("During branch-and-price we have to disable SCIP's preprocessing, cut generation, and propagation functionalities to ensure a correct dual bound."). There is no numerics study; *nothing on* becomes *a stated position, no study* | [S008 manuscript p. 13; S060 pp. 23-24, 48; S029 p. 10; S027 p. 136] |
| C17 | Routing row *Design my Benders decomposition* (*his one Benders paper puts Benders cuts inside pricing*); Activation Rules example *Benders design* under *Nothing in the record* | two 2026 chair preprints design Benders algorithms: a branch-and-Benders-cut for power grids along contingencies, with partial decomposition keeping the base case in the master [S075 pp. 2, 19, 22-23], and an exact, LP-free subproblem solver whose cuts are proved correct: "The efficiency of the subproblem solution algorithm remains a relatively underexplored subject in the Benders context, even though it can contribute significantly to overall running time." [S076 p. 2]. Both are unreviewed and in the group's voice | [S075; S076 pp. 2-4, 9-27] |

The skill has ten heuristics; with H2 moving into Method 5 and four new ones the list would reach thirteen, above the framework's 5-10. Priority for the editor: H11 and H12 first (they fill the Routing rows on branching and on tailing-off), then H13, then H14, which could instead become a sub-step of Method 3 step 2.

### Added in T3.6

- **Benders row**: ✗ dated by two unreviewed 2026 group preprints that design Benders algorithms: a branch-and-Benders-cut for power grids with partial decomposition keeping the base case in the master [S075 pp. 2, 19, 22–23], and an exact, LP-free subproblem solver [S076 pp. 2–4]; the row now points to their devices (catalog DM12), keeps *decompose-or-not only* for Workflow B, and keeps the *Nothing in the record* rule beyond them and the Fischetti seat.
- **Heuristic row**: *Method 5 (H2 points there)*.
- **New row**: *Only theory or metaheuristics exist for this* → Workflow A step 2, H13, Method 5 (08 §5 H13).
- **Tailing-off row**: H12 first (08 §5 H12). **Branching row**: H11 first, *Workflow C steps 3–3a* (08 §5 H11).
- **Experiments row**: *My data are confidential* → Method 3 (step 2a carries the synthesis's H14).
- **Last row**: *numerics: only the stated tolerance position* (08 §3.3 C14).
- **Agentic Protocol, Step 2**: one bullet added, *Bound for a heuristic (Method 5)*.

### Before T3.6 (moved verbatim)

````text
## Research Task Routing

| The user says | Workflow | Main methods |
|---|---|---|
| "Should I decompose this?" "Branch-and-price, Benders or branch-and-cut?" | Workflow B | Method 1, Method 2, H5 |
| "Design my Benders decomposition" | Workflow B, decompose-or-not only | "Nothing in the record" rule (his one Benders paper puts Benders cuts inside pricing, Misreading 3); at milp-roundtable, seat Fischetti |
| "A company gave me a planning problem" "How do I model this?" | Workflow A | H3, Method 1 steps 1–3 |
| "Our heuristic works, can we give it to the company?" | Workflow A step 5 | H2 (ship with a bound), G1; no bound yet → Method 1 step 2 |
| "My column generation tails off / pricing is too slow / the master LP is slow" | Workflow C | H1, H6, Method 1 step 6 |
| "My branch-and-price is stuck" "It doesn't beat the compact model" "The tree explodes" | Workflow G | H6, Method 1 stop rule, H1, H5 |
| "How do I branch without breaking pricing?" "Should I add cuts?" | Workflow C steps 3–5 | Method 1 step 6, H5, H7; cuts only where measured (Tension 6, Misreading 3) |
| "Which decomposition / rule / component should I use?" | Workflow B step 3 | Method 2 |
| "Can ML choose the decomposition for me?" | Workflow B step 3 | Method 2 exit A and checkpoint, G5; Tension 5 is a tension, not a verdict |
| "How do I design the experiments?" "Which baselines?" | Workflow D | Method 3, H7 |
| "Are these results good?" "Review my draft" | Workflow E | Method 3 step 6, Method 2 exit B, B3 |
| "I keep seeing an effect I can't explain" | Workflow F | Method 4 |
| "How do I organize a solver project with students?" | — | H9, H7 |
| Literature search ("Read, read, read.", credited to Skutella: two lines, no practice), funding, rebuttals, choosing between projects, daily supervision, line-level debugging, numerics | — | "Nothing in the record" rule (Activation Rules); generic advice labelled "not Lübbecke-style". |

**When several rows match**, start with the earliest in this order: instrument (H6) → compact baseline and go/no-go (B) → build and tune (C) → evaluate (D) → judge and write (E) [inferred order]. Do not enter C, D or E while the compact model's log is unrecorded: ask for it, and make Method 1 step 2 the next action.
````

````text
### Step 2: Lübbecke-style fact finding

**Use tools (web search, arXiv, Crossref, Optimization Online, the solver repository); never answer from memory.** Run only the items the routed workflow needs (B: compact baseline, decomposition bound, pricing, "does not work" verdicts; C and G: pricing plus the user's logs; D and E: competitor, instances, outside critiques). Stop when each needed item has a source or is written "not found". Keep the search internal.

- **Compact baseline (Method 1).** Solver, version, root bound, nodes, time on the original-variable model (from the user's log if any).
- **Decomposition bound (Methods 1–2).** A published Dantzig-Wolfe or Lagrangian bound for the class; a generic solver run (GCG; the book also names BaPCod and VRPSolver) with detected or supplied structure.
- **Pricing (H1).** The subproblem (knapsack, resource-constrained path, matching, a smaller general MIP) and whether a fast combinatorial algorithm exists.
- **Strongest competitor (Method 3).** Best published exact method, code, instances, solver version, hardware; the latest result going the other way.
- **"Does not work" verdicts (H5).** Which formulation and branching did they use?
- **Instances (B2).** Public library (MIPLIB, strIPlib) or random? Hard but not impossibly hard?
- **Outside critiques.** Which GCG version they used.
````

<a id="taste-marks"></a>

## Taste: marks of good research

> Changed in the T3.6 review fixes: see [Review fixes](#review-fixes).

### Full-text evidence (08 §2.5, copied)

| Item | Cards citing it in their method links (read in full or part) | Update |
|---|---|---|
| G1 A quality claim comes with a proof or a bound | 21: D001 S008 S012 S016 S018 S022 S025 S027 S030 S033 S035 S036 S051 S052 S053 S063 S066 S076 S080 S087 S088 (S025 a contradiction) | becomes Method 5's taste mark |
| G2 Software, data, what did not work | 12: D004 S012 S014 S016 S020 S023 S050 S055 S063 S083 S089 S091 | ✅ "In contrast, we would like to enable the reader to check claims which we do not explicitly support by numerical results." [S012 report p. 9]; code and data on Zenodo [S089 p. 23] |
| G4 Structure, not a pretty decomposition | 16: S010 S011 S015 S020 S028 S030 S031 S042 S043 S057 S070 S076 S084 S085 S086 S090 | ✅ "It is our impression that integer programming has been used for timetabling only because of its modeling power. It was not realized that a deeper understanding of combinatorial properties of the problem may be the key to actually solving large instances to proven optimality." [S028 p. 2]; detected structures sometimes look artificial [S070 p. 6]; "This does not imply that there is no such structure, but rather that it is not obvious." [S003 p. 19] |
| G5 Discrete first; ML for optimization | 3: S012 S043 S077 | ✅ "we use CNNs to study optimization problems, rather than to help solve them." [S043 preprint p. 14] |

| # | SKILL.md item | What the full texts show | Cards |
|---|---|---|---|
| C10 | H2 case: *a genetic algorithm certified within 10% by an IP, then deployed* | the certificate covers short-term instances with FIFO solutions against the FIFO-restricted optimum, on makespan; the module has been in use since December 2009 and the paper was received in March 2010; the text does not say whether the bound came before deployment; the 2009 workshop version states the FIFO condition of its bound | [S035 pp. 1, 13-14, 16-17; D002 pp. 21-22] |

### Added in T3.6

- **G1**: *(new; procedure: Method 5)*; certified gaps 2004–2026 [S030 arXiv pp. 10–11; D002 pp. 21–22]; ✗ one exception, a 2016 MINLP heuristic without a usable bound [S025 preprint p. 21]. The pre-synthesis *the coil-coating certificate (H2) [practice]* is replaced; the case is narrower than H2 said (08 §3.3 C10).
- **G2**: code and data released so that readers can check claims [S012 report p. 9; S089 p. 23].
- **G4**: timetabling IP used *only because of its modeling power* [S028 p. 2] (verbatim fragment of the card's quote).
- **G5**: CNNs used to study optimization problems, not to solve them [S043 preprint p. 14] (paraphrase of the card's quote).

### Before T3.6 (moved verbatim)

````text
### Marks of good research

1. **G1. A quality claim comes with a proof or a bound** (new). "I am a well known supporter (a.k.a. "fan") of exact optimization" (blog, "Know your Heuristics!", 2014-12-19); when someone claims an optimum, "ask them whether they can prove it" (TEDx 2018, ASR) [stated]; the coil-coating certificate (H2) [practice].
2. **G2. Software, data and what did not work are contributions** (new). "who's that guy he only wrote software well only come on that's so valuable so difficult to do" (podcast 2021, ASR); the joint 2020 editorial invites "failed experiments and wrong paths taken to learn from" (p. 2); a chair thesis reports that branch-and-cut "did not work out well on our benchmark instances" (Franzen 2022). Openness is mixed in practice (Tension 7).
3. **G3. The problem needs fundamental research and has an owner** (deepened). "I particularly appreciate problems that cannot be solved "out of the box" but require solid fundamental research." (blog 2014); thesis preface: "solving a practical problem by means of applied mathematics is much more than applying mathematics" (2001, p. v); "motivation -> applicability -> is it implemented -> they make money from it" (Bluesky 2024-12-11).
4. **G4. The algorithm sees structure, not a flat matrix; but a pretty decomposition is not structure** (deepened, new warning). "Most research topics in my head deal with finding and exploiting structures in mathematical programs." (blog 2014-11-04; eight occasions to 2026); the arrowhead form may be "an artifact of the model and algorithm we use to detect/enforce this structure" (2015, DOI 10.1007/s10107-014-0761-5); "But don't be deluded by the beauty" (book p. 237, joint).
5. **G5. Discrete and linear first; ML for optimization, not instead of it** (overturned: not an ML-for-MIP researcher). "i think we are not done with linear yet" (podcast, ASR); "is there also a stream for discrete optimization without machine learning? #orms" (Bluesky 2026-02-27). Against plain rejection: his OR2017 abstract asks "where (and how) can machine learning help in improving methods for solving optimization problems" (02 §1.7).
````

<a id="taste-warnings"></a>

## Taste: warning signs and quick-check

> Changed in the T3.6 review fixes: see [Review fixes](#review-fixes).

### Full-text evidence (08 §2.5, §3.1 V8 and §5.5, copied)

| Item | Cards citing it in their method links (read in full or part) | Update |
|---|---|---|
| B1 Objective of weighted penalties | 9: S010 S018 S028 S035 S042 S048 S075 S080 S115 | variants in §3.1 V8 |
| B2 Random or tiny instances | 10: S003 S030 S040 S046 S047 S051 S057 S088 S112 S115 | the warning sign is broken in his own record [S051 p. 10; S040 p. 9; S115 pp. 23, 27]; §5 H14 gives the constructive side |
| B3 Conclusion that only summarises; self-praise | 7: D002 D004 S014 S052 S075 S078 S089 | a concluding conclusion [S089 pp. 31-32]; summary-type or self-praising endings in co-authored texts [D002; S014; S052; S075; S078] |

- **V8 · Taste B1.** A competition's penalty sum optimised as given in 2012 [S010 pp. 5-6], against his 2015 *apples and oranges* comment [S048 p. 2]: a later warning, not a contradiction. A weighted objective accepted when the owner sets the weights and sees the trade-off [S080 pp. 4, 8-9]; a weighted surrogate used inside the search while results are reported in the owner's measure [S018 manuscript pp. 24-25]; exchange rates set by the authors and owned by no planner [S115 pp. 23-24].

- **Taste warning, proposed B4 *modelled is not solved***: an extension that can be written down is not thereby handled: his sole-voice question to an overview's authors [S048 p. 3], and his own timetabling extensions modelled, with five ITC2007 comp instances left at 70-99% gaps after an hour while the four small test instances ended within 6% [S010 p. 14].

### Added in T3.6

- **B1**: ⚠ a competition's penalty sum optimised as given in 2012 [S010 pp. 5–6], a later warning rather than a contradiction; owner-set weights accepted when the owner sees the trade-off [S080 pp. 4, 8–9] (ledger only).
- **B2**: ✗ broken in his own record [S051 p. 10; S040 p. 9; S115 pp. 23, 27]; remedy: Method 3 step 2a.
- **B3**: ⚠ summary-type endings in co-authored texts [D002; S052]; a concluding conclusion exists too [S089 pp. 31–32].
- **B4** (new, proposed in 08 §5.5): *Modelled is not solved*: the sole-voice question whether a modelled extension is thereby handled [S048 p. 3]; the group's own timetabling extensions left with 70–99% gaps [S010 pp. 8–9, 14]. Review fixes: folded into B2 as a related clause (the taste list keeps eight criteria), with the gaps restated from the table: five ITC2007 comp instances at 70–99% after an hour, the four small test instances within 6% [S010 p. 14].
- **Quick-check**: one item added, *Every delivered heuristic with a gap and its condition; every cut with its effect on pricing?* (Method 5, H11).

### Before T3.6 (moved verbatim)

````text
### Warning signs of bad research

1. **B1. An objective that is a bag of weighted penalties, or that nobody owns** (new). TOP 2015 comment, p. 360: "apples and oranges"; slightly different data give very different timetables (DOI 10.1007/s11750-015-0364-1, sole); "those who design the objective function are the persons in power" (Bluesky 2026-11-07).
2. **B2. Random or tiny instances, unequal conditions, "often" without counts** (deepened). On an RL-based MIP method tested on generated instances: "simply no. I will not accept this as a serious proposal for solving mixed-integer programs, regardless of whether you compared against gurobi or not" (Bluesky 2024-12-04); on comparisons across papers: "This part of the overview needs to be taken with a grain of salt." (TOP 2015, p. 360); for the next MIPLIB, "very hard (but not "impossibly hard")" instances "ideally from a practical application context" (Mastodon 2024-09-09).
3. **B3. Repairing what you broke, a conclusion that only summarises, self-praise** (new). The 2025 referee-report post above; "when your "conclusion" summarizes your work, it is a summary, not a conclusion." (three occasions, 2024–26); "We are proud to release…" removed from GCG 3.0.2 release notes by his commit b147336e [practice].

### Taste quick-check

- [ ] Compact model run in a current solver, bound, nodes and time recorded?
- [ ] A subproblem you solve well, other than "a smaller general MIP"?
- [ ] Instances chosen against the method, plus a general set showing no harm, real or public, hard but not impossibly hard?
- [ ] Every baseline re-run by you under identical conditions?
- [ ] Every quality claim with a proof or bound, every "often" with a count, a conclusion that concludes?
- [ ] Can the owner say which of two solutions is better without penalty weights?
````

<a id="method-1"></a>

## Method 1: Compact model first; decomposition as a measured bet

> Changed in the T3.6 review fixes: see [Review fixes](#review-fixes).

### Full-text evidence (08 §2, copied)

Counts are distinct works whose digest links the method; a card can be evidence and variant at once. The book's chapters are counted as cards and, in the last column, once as a source. One Method 2 evidence link rests wholly on sealed material and is not counted.

| Method | Evidence (read in full/part) | Variant | Contradiction | Distinct works (book once) |
|---|---|---|---|---|
| M1 Compact model first; decomposition as a measured bet | 51 (50; S045 abstract) | 41 | 1 [S032] | 66 (59) |
| M2 Enumerate small, then explain or automate | 23 (23) | 21 | 0 | 39 (33) |
| M3 Adversarial, identical-conditions evaluation | 60 (59; H001 abstract) | 60 (59; S064 abstract) | 13 | 83 (76) |
| M4 Synthesis writing as a research instrument | 21 (20; H001 abstract) | 14 | 0 | 33 (26) |

### Method 1 · Compact model first; decomposition as a measured bet

- **Strongest cards**:
  - Step 1 from the start, in his own voice: the compact formulation is the default and the extensive one has to justify itself [S027 p. 40]; the compact MIP is stated first and shown weak on paper by a uniform fractional solution, and the Dantzig-Wolfe set-partitioning model is proven stronger [S027 pp. 90–94]; "Some imagination is needed to find an appropriate compact formulation, but we strongly recommend to look for one." [S001 report p. 12]; "Always remember that integrality must hold for the original x variables." [S002 pre-publication p. 3]; master and pricing derived from the compact LP rather than written down by construction [S086 pp. 3, 46].
  - Step 2 practised in algorithmic papers across 28 years: a compact MIP on a current solver with the whole data pipeline [S037 pp. 5-6]; plain branch-and-bound as the yardstick of a line-planning heuristic [S012 report pp. 9-11]; the compact three-index IP kept as the baseline table [S028 pp. 4, 11-12]; the compact network-design MIP in CPLEX much faster than the set-partitioning IP, with "To be fair at this point we remark that a true branch-and-price algorithm would probably outmatch the network design MIP in terms of computation time on larger instances." [S051 pp. 5, 7, 10-11]; the compact model run and losing 2 of 12 against 12 of 12 [S065 p. 7]; the compact model in CPLEX under the same conditions, its winning range for small k conceded [S050 preprint pp. 11, 13-14, 28]; the compact model as row 1 of the evaluation [S075 p. 22]; a re-run compact baseline that still wins at k = 5 [S089 pp. 22, 28]; the compact arc-based MILP in Gurobi with the same heuristic and cuts as the tailored code [S115 pp. 17, 22]. Stated in the book: "Evaluating the success of a reformulation essentially lies in comparing how much it can be solved faster than the compact formulation." [S084 p. 25].
  - Workflow B checkpoint (a), marked *[inferred]* in SKILL.md, practised: the reformulation's root bound compared with CPLEX's root bound after its own cuts, the gain shrinking and on some instances turning negative [S026 p. 7]; the IPCO table sets the reformulation bound against CPLEX's LP, root-with-cuts and final values [S032 manuscript p. 8].
  - Step 3: whole patterns, shifts, cuts or paths become the variables because their pricing is a DP, a small shift problem or a min cut [S027 pp. 92-94; S026 pp. 3-4, 10; S065 pp. 3-4]; DP pricing absorbs non-convex industrial rules [D004 p. 4].
  - Step 4 stated in co-signed and book text: "As a research tool, GCG can be used to quickly assess the potential of a decomposition-based algorithm for any problem for which a compact MILP formulation is available." [S014 arXiv p. 14]; PyGCGOpt lowers the hurdle to try branch-and-price on an existing model [S006 p. 76]; GCG as the probe before a costly build, "We should not hide that even a large investment in an implementation may turn out to be fruitless in the end." [S077 p. 67]. The one practised probe in the record is a measuring run over 75 decompositions of an integrated model before any tailored code [S042 pp. 10-17].
  - Step 5: SCIP chosen for its tree management [S029 p. 6]; a framework manages the branch-and-price tree [S008 manuscript p. 13]; part of a competitor's gap attributed to its hand-written depth-first tree [S089 p. 26].
  - Step 6: "Our most valuable source of information are the original variables of the compact formulation; they must be integer, and they are what we branch and cut on" [S001 report p. 24]; a compact formulation exists behind any column-generation model [S021 report pp. 4, 6-9]; "hence branching and cutting decisions can always be defined on the variables of this formulation" [D004 p. 5]; reverse Dantzig-Wolfe as the device [S084 pp. 52-58].
  - Stop rule: "GCG, presented with an arbitrary MIP, successfully detects a decomposition that leads to an improved performance over SCIP on the original model only in a small fraction of cases." [S009 p. 2]; no bound gain when pricing has the integrality property [S084 p. 27; S088 p. 19; S051 p. 7]; a third of MIPLIB 2003 set aside [S032 manuscript p. 6]; a co-signed decomposition heuristic with no general gain on MIPLIB 2017 [S006 pp. 15, 82].
- **Say–do update**: keep ✅ for steps 1, 3, 5 and 6 (full texts: 1998-2026). Step 2 is ✅ in the algorithmic papers above and absent where the decomposition is the field's standard (routing and crew scheduling: "Because of this advantage, the state-of-the-art is to solve this extended formulation of the VRPTW by branch-price-and-cut, see Chapter 7." [S085 p. 10]), where branch-and-price only bounds a heuristic [S035 pp. 11, 13-15; D002 pp. 21-26], or where the toy run stands in for the real one [S023 p. 14; S027 p. 149]. Step 4 stays ⚠: stated in print from 2021 on (and in the CO@Work 2020 lecture, captions), not shown before his own tailored studies [S073 pp. 10-14; S089 pp. 30-31; S115 pp. 9, 11, 37], where the master/pricing split is read after the build [S075 p. 23].
- **Increment dating (correction, §3.3 C1)**: the full texts do not show *since 2017 GCG is a first try and an estimate*. The 2012 sole voice frames the generic solver as needing no user input [S070 pp. 1, 7] but already names the reader who cannot tell whether a hand-built code is worth the effort [S070 p. 4]; in 2016 GCG is a competitor ("We conclude that at the current state of the art, it still considerably pays to consider a problem-specific implementation, even though generic solvers may become competitive soon." [S073 p. 14]); in 2017 it "supports users in employing Dantzig-Wolfe decomposition, even as a non-expert" [S013 p. 5]; in 2018 "It has always been GCG's ambition to not require the user to have any knowledge about problem or model structure or the decomposition algorithms to exploit such structure." [S005 p. 29]. The probe framing appears in print in 2021 and 2023 [S006 pp. 76-77; S014 arXiv p. 14] and in the book [S077 p. 67], while the generic framing continues: "For the user, no expertise in these techniques is needed" [S019 p. 26].
- **Proposed Practice additions**: [S051 pp. 5, 7, 10-11] (2008: the compact model wins, and the text says where it would not); [S026 p. 7] (checkpoint (a) practised); [S089 pp. 22, 26, 28]; [S115 pp. 17, 22].
- **Limitations update**: the stop rule is narrower than the record (§3.1 V1-V3).

### Variants, contradictions and corrections (08 §3, copied)

- **V1 · Method 1 stop rule: go reasons other than a bound gain.** The book recommends Dantzig-Wolfe without a bound gain when the master is far smaller than the compact model (under 0.001% of its rows), when a symmetry disappears or a quadratic cost becomes a column cost [S084 pp. 92-95, 98, 100-102], and names decentralization, a fast pricing algorithm and created structure as reasons in the LP case, where no grouping can change the bound [S086 pp. 13-14]. His group's practice matches: memory on national grids [S075 p. 2], memory against time in an engineering partner's model, "excessive memory usage of solving the original model formulation can be decreased at the cost of solving time" [S078 p. 8], model size and pricing speed [S115 pp. 9, 11], shift calendars that shrink the pricing problems [S026 p. 10], and the planners' own hierarchy kept although the integrated model wins [S036 preprint pp. 8, 10]. The stop rule should name these reasons and ask for the measurement each one implies (memory, time per node), not only the bound.
- **V2 · Method 1 stop rule: *pricing is only a generic MIP*.** The book uses MILP pricing where no combinatorial algorithm exists [S077 pp. 56, 76, 78], and GCG 4.0 adds general-MILP pricing solvers [S019 pp. 31-32]. When that MIP has structure of its own, his record decomposes it again: routes by labelling and quantities by an inner column generation [S029 pp. 3-6, 12]; a nested segment decomposition that keeps the stronger outer master [S115 pp. 13, 23, 26]; recursive pricing in GCG [S019 pp. 29-31]; nested column generation is among the book's deferred subjects [D004 p. 8].
- **V3 · Method 1 step 4: a cheaper probe.** The Lagrangian dual gives the master's bound by a subgradient run with no master implementation, a heuristic lower approximation without primal output [S088 pp. 17, 31, 33-34, 83].
- **V4 · Method 1 step 6: aggregated identical blocks.** With identical pricing problems the aggregated x can be integral while λ is fractional, disaggregation brings the symmetry back, and decisions on original variables alone cannot be stronger than decisions that use extra variables; branch on λ-sums or auxiliary variables there [S077 pp. 22, 27-28, 49-50]; or branch on aggregated original variables with a disaggregation certificate and a Ryan-Foster fallback [S050 preprint pp. 3-6, 22-23].

- **Method 1 step 5 (mild, 2011)**: the IPCO study wrote its own very basic depth-first branch-and-price inside a tool built on CPLEX and hMETIS, called simple-minded in a table caption [S032 manuscript pp. 5, 7]. Later group code is built on frameworks [S050 preprint p. 11; S089 p. 22; S115 p. 22], and the 2026 paper attributes part of a competitor's gap to its hand-written tree [S089 p. 26].

| # | SKILL.md item | What the full texts show | Cards |
|---|---|---|---|
| C1 | Method 1 Increment: *since 2017 GCG is a first try and an estimate* | probe framing in print from 2021 (group) and 2023 (co-signed) and in the book; the generic framing persists to 2025; the 2012 sole voice already names the reader who needs a probe | [S070 pp. 1, 4, 7; S073 p. 14; S013 p. 5; S005 p. 29; S006 pp. 70, 76-77; S014 arXiv p. 14; S019 p. 26; S077 p. 67] |
| C2 | Workflow B checkpoint (a) *[inferred]* | practised in 2011 and 2015 | [S032 manuscript p. 8; S026 p. 7] |
| C3 | Method 1 stop rule | narrower than the record: go reasons beyond a bound gain; MILP pricing; nested decomposition | §3.1 V1-V2 |

### Added in T3.6

- **Increment**: ✗ *since 2017* corrected to *in print from 2021, not 2017* [S006 pp. 76–77; S014 arXiv p. 14] (C1).
- **Evidence** rebuilt in the house format: Stated, the book's sentence [S084 p. 25]; Practice [S051 pp. 5, 7, 10–11; S026 p. 7; S089 pp. 22, 28; S115 pp. 17, 22; S042 pp. 10–17]; Say–do with the counts of 08 §2 (51 / 41 / 1 cards; 59 works with the book once) and the step-4 caveat [S089 pp. 30–31]; four variant bullets from V1–V3 and the 3.2 contradiction [S084 pp. 92–95; S075 p. 2; S029 pp. 3–6; S115 p. 13; S088 pp. 17, 31; S032 manuscript pp. 5, 7].
- **Step 3**: *Pricing with the integrality property cannot raise the bound (PD3)* [S084 pp. 27, 39; S088 pp. 19, 60–61] (catalog PD3).
- **Stop rule**: one sentence added, *narrower than his record* (C3, V1–V2).
- The pre-synthesis Stated and Practice lines (book p. 507, CO@Work 2020 and 2024, the SEA 2010, IPCO 2011, 2015, SSRN and arXiv practice) are kept below; the cards confirm them: SEA 2010 against SCIP [S011 pp. 8–12], the IPCO and 2015 comparisons against CPLEX 12.2 [S032 manuscript pp. 7–8; S015 preprint pp. 10–30], the arc-based model in Gurobi [S115 pp. 17, 22], the natural binaries [S089 p. 7].

### Before T3.6 (moved verbatim)

````text
### Method 1: Compact model first; decomposition as a measured bet

**One line**: Keep the compact model as the benchmark, use a generic decomposition solver or a root-node loop as a measuring instrument, and build a tailored branch-and-price code on a framework only when the probe says it will pay.

**Increment**: overturned. Not "a generic solver so nobody hand-builds branch-and-price": since 2017 GCG is a first try and an estimate; his 2024–26 tailored studies are built on SCIP.

**Evidence**:
- Stated: "Step one is solely on paper. Don't skip this." (book p. 507, joint); "you always have original variables!" (CO@Work 2024 slides, PDF p. 168); GCG gives "intuition" on "whether a fully fledged branch-and-price implementation will pay or not" (CO@Work 2020, 1:35:41); do not write tree management yourself (four occasions; 02 R11).
- Practice: GCG 0.7 against SCIP 1.2.0.5 (SEA 2010); reformulations against CPLEX 12.2 (2011, 2015); Gurobi on the arc-based model next to branch-price-and-cut on SCIP (DOI 10.2139/ssrn.7177419); natural binaries added to the extended model (arXiv:2602.04984).
- Say–do consistency: ✅ stated + practised for steps 1, 2, 5, 6. ⚠️ Step 4 is stated four times and taught, but no record shows the probe was run for his own 2024–26 studies.

**Steps**:
1. Write the compact (original-variable) model on paper as the problem statement, even if you think in columns.
2. Run it in a current MILP solver with the full data-to-solution pipeline; record bound, nodes, time. Every decomposition must beat this (book pp. 507–508). 🔴 If the compact model already solves the user's instances within their limit, stop, or narrow the claim to the instances where it fails [inferred].
3. Ask which larger object could be a variable because its subproblem is solvable: "we model in paths not only in arcs, we model in entire matchings not in edges" (CO@Work 2020, 1:37:02).
4. Probe before you build: a generic Dantzig-Wolfe solver with the structure you know, or a bare root-node column-generation loop. Read iterations, master against pricing time, and tree size (book pp. 494–495).
5. If it pays, build on a framework that manages the tree (SCIP pricer plugins in his group). In his PhD he did column generation without branching because he would have had to write the tree (podcast 0:36:35, ASR).
6. Keep original variables in view for branching and cutting: writing master and pricing directly "may conceal connections which are "there" anyway" (book p. 508).

**🔴 Stop rule**: stay with branch-and-cut when the probe shows no bound gain, or pricing is only a generic MIP. Without structure "it can be detrimental to performance to try to use a decomposition anyways" (GCG `why-gcg.md`, group); "the solver may completely fail" (CPAIOR 2017 abstract, DOI 10.1007/978-3-319-59776-8_16).

**Applies to stage**: problem choice, idea generation, the build decision.

**Different from standard practice**: column-generation papers usually write master and pricing directly and compare with other branch-and-price codes; he keeps the compact model as yardstick.

**Limitations**: supplying the structure beats automatic detection (Yıldız, Boland, Savelsbergh 2022), so probe with the known structure [inferred]. "No tree management" dates from CPLEX 3.0 days.
````

<a id="method-2"></a>

## Method 2: Enumerate small, then explain or automate

> Changed in the T3.6 review fixes: see [Review fixes](#review-fixes).

### Full-text evidence (08 §2, copied)

### Method 2 · Enumerate small, then explain or automate

- **Strongest cards**:
  - The enumerate-the-option-space half: the fullest instance writes the option space down, shrinks instances until every reformulation is computable, names and drops the too-hard ones, reads the map and validates a cheap proxy against full enumeration before using it at scale [S058 pp. 2-11]; random sampling is rejected because "Unfortunately, there is little hope that we even obtain a statistical statement from a random sampling of DW reformulations unless we have further information about the structure of the model: the sample size would need to be too large." [S058 p. 6]; the textbook reformulation is the strong one for bin packing [S058 p. 9]. Earlier: penalty sets, block counts and dummy shares swept on real instances, two measures kept and the rest dropped as inconsistent, and a rule that can be applied a priori, "When looking for a good number of blocks, start with many. As long as this is computationally easy, decrease the number of blocks." [S032 manuscript pp. 6, 8-9]; about 37 candidates per instance on 39 MIPLIB instances, six measures tested and one kept [S015 preprint pp. 8, 11-21]; 75 decompositions on one instance with a known optimum, the proxy scores "only an indicator and no guarantee for good solvability" [S042 pp. 10-17]; ten selection heuristics as settings of one implementation on 73 instances [S006 pp. 70, 73, 113-114].
  - Exit A: the 2015 hand proxy becomes a learned choice [S009 pp. 2-5].
  - Exit B, the older half: computation suggests the theorem from 1998 on, with the general case published as a conjecture [S020 pp. 5-8]; a counterexample found by enumerating the vertices of a tiny instance [S063 pp. 1-3]; "Due to recent computational experiments we conjecture the following." [S057 p. 5]; "It is common that theory is complemented by computational experience. In this paper we did the reverse: We found promising research directions by a careful study of computational experiments." [S053 p. 11]; gap conjectures from computational experience [S112 pp. 6, 8; S046 pp. 8, 11]; the constant-factor claim kept as a conjecture, "We are hopeful that this argument can be completed some time in the future [18]." [D001 arXiv p. 23].
  - The book: nine pricing domains of one instance tabulated, decompositions enumerated over subsets of constraint classes and scored [S084 pp. 63-66, 80-81]; "We do not even know what “good” in this context generally means." [S088 p. 19].
- **Say–do update**: keep ✅ (stated in the talks SKILL.md cites, and in his 2012 sole voice: experiments to guide the design, a theory of good structure to follow [S070 p. 7]). The full texts change the weighting: exit B is the habit of 1998-2008 [S020; S063; S057; S053; S112; S046; S041; D001; S030], the option-space enumeration starts in 2011 [S032] and peaks in 2018 [S058], and exit A occurs once [S009]. The checkpoint (a proxy that looks right is not evidence) is practised where the proxy is validated against enumeration or measured gaps [S058 pp. 7-8, 10; S042 p. 16; S032 manuscript p. 8] and not where scores ship untested [S005 pp. 30, 33-35; S019 pp. 32-33; S043 preprint pp. 23-36; S075 pp. 17-20, 22-23].
- **Proposed Practice additions**: [S053 p. 11] (the stated reversal of theory and computation, 2005); [S042 pp. 10-17]; [S006 pp. 113-114] (the *ten branching variants* now with pages).
- **Report the ex-post best next to the rule**: the virtual-best column beside each fixed setting appears in four works and belongs to step 5 [S016 p. 4; S035 pp. 15-16; S015 preprint p. 22; S009 pp. 5-6].

### Variants, contradictions and corrections (08 §3 and §5.5, copied)

- **V5 · Method 2 order: the theorem of the extremes first.** The characterization of both extremes of the stable-set reformulations is complete in a 2015 manuscript without computation, experiments only announced ("We will report on experiments in future work." [D006 p. 11]); the journal theory paper computes nothing [S052 in-press p. 19]; the SEA study then asks what happens in between [S058 pp. 1-2]. One-parameter families with known algorithms at both ends appear in the LP-degeneracy line [S061 pp. 1, 9, 17; S044 pp. 1-2, 9-10] and in the book [S085 pp. 20-24; S086 pp. 18-20, 28].
- **V6 · Method 2 as a teaching device.** Tiny instances are enumerated completely to explain, not to map an option space [S060 pp. 58-59; S086 pp. 35-46; S087 pp. 36-37, 41-42; S077 pp. 16, 46-49; S088 pp. 23-24, 33].

| # | SKILL.md item | What the full texts show | Cards |
|---|---|---|---|
| C4 | Method 2 step 5: *four dropped in IPCO 2011; border area kept* | IPCO 2011 kept two measures (number of blocks, average integrality gap of the blocks); the border area is the 2015 paper's single kept proxy out of six | [S032 manuscript p. 8; S015 preprint pp. 12-21] |
| C5 | Method 2 Practice: *over a million LPs in about 100 hours* | over one million relaxations, each solved by column generation, so the LP count is larger; no hardware, LP solver or limit stated | [S058 pp. 2-3] |
| C6 | Method 2 Limitations: *the 2018 study starts from a theorem* | the theorem dates to a 2015 manuscript | [D006 p. 11; S058 p. 2] |

- **Method 2 step 5**: report the a-priori rule next to the ex-post best candidate [S015 preprint p. 22; S016 p. 4; S035 pp. 15-16; S009 pp. 5-6].

### Added in T3.6

- **Evidence** rebuilt: Stated [S053 p. 11]; Practice [S058 pp. 2–11; S015 preprint pp. 8, 11–21; S020 pp. 5–8; S063 pp. 1–3]; Say–do with 08's counts (23 / 21 / 0; 33 works) and the weighting by period [S070 p. 7; S009]; variant bullets C4, C5, V5 and the random-sampling rejection [S032 manuscript p. 8; S015 preprint pp. 12–21; S058 pp. 1–3, 6; D006 p. 11].
- **Step 3**: *with structure in view (Variants)* [S058 p. 6].
- **Step 5**: ✗ *four dropped in IPCO 2011; border area kept* corrected to *IPCO 2011 dropped four; the border area is the 2015 proxy* (C4); *report the ex-post best beside the rule* [S015 preprint p. 22] (08 §5.5; also [S016 p. 4; S035 pp. 15–16; S009 pp. 5–6]).
- **Checkpoint**: *Practised in 2018* [S058 pp. 7–8] (also [S042 p. 16; S032 manuscript p. 8]; not where scores ship untested [S005 pp. 30, 33–35; S019 pp. 32–33]).
- **Limitations**: ✗ *the 2018 study starts from a theorem* + *of a 2015 manuscript* [D006 p. 11] (C6).

### Before T3.6 (moved verbatim)

````text
### Method 2: Enumerate small, then explain or automate

**One line**: When success hinges on a discrete choice with many options, compute the whole option space on instances small enough to allow it, read the map for surprises, then score or learn the choice, or prove the pattern for one class and publish the rest as conjectures.

**Increment**: new. The prior had one fragment (learning when to decompose), its weakest step.

**Evidence**:
- Stated: computation suggests the theorem (four occasions, 02 R13); "attempt of an interpretation" and "a formal proof of such results is an open research topic" (CO@Work 2024, PDF p. 136); "Only recently, we fully understood also the reformulations in between the extremes." (2025 keynote abstract).
- Practice: all 2^|I| reformulations of models with at most 18 constraints, over a million LPs in about 100 hours (SEA 2018); the stable-set characterisation (2018); about 1,500 decompositions of 39 MIPLIB instances (2015); ten branching variants (2021; 03 §1.6).
- Say–do consistency: ✅ stated + practised (co-authored).

**Steps**:
1. Write the option space down (which constraints to convexify, which decomposition, which rule) instead of picking by taste.
2. Shrink instances until the whole space is computable; name and drop those that stay too hard.
3. Where shrinking is impossible, sample widely on real instances.
4. Read the map for contradictions of expectation (so far: few distinct dual bounds occur; textbook constraint choices matter most; no single correct decomposition per matrix).
5. Exit A, automate: test proxy measures against measured outcomes and drop inconsistent ones (four dropped in IPCO 2011; border area kept); learn the choice only then (CPAIOR 2017).
6. Exit B, explain: label the reading as a reading, prove it for one class, publish the rest as conjectures.

**🔴 Checkpoint**: a proxy that looks right is not evidence; learned rankers later beat both the border-area score and GCG's score (Weiner et al., *EURO J. Comput. Optim.* 2023, DOI 10.1016/j.ejco.2023.100061). If a learned rule is not carried into the solver, say so: the 2017 selector left no trace in GCG (03 §6).

**Applies to stage**: idea generation, component choice, theory building.

**Different from standard practice**: solver papers pick a rule and tune it; enumerating every reformulation of toy models, ending in conjectures, is unusual.

**Limitations**: toy scale; transfer to real instances is open. The 2018 study starts from a theorem, the 2025 abstract from observations.
````

<a id="method-3"></a>

## Method 3: Adversarial, identical-conditions evaluation, with the claim sized to the measurement

> Changed in the T3.6 review fixes: see [Review fixes](#review-fixes).

### Full-text evidence (08 §2, copied)

### Method 3 · Adversarial, identical-conditions evaluation, with the claim sized to the measurement

- **Strongest cards**:
  - Steps 1-2 (test where the change can fail): in his thesis, "One purpose of our computational testing is to demonstrate the limitations of our implementation as well." [S027 p. 140], with hard and synthetic sets built for that purpose [S027 p. 137]; "We did not experiment on instances with known structure: in these cases the effectiveness of DWR has already been proven, and indeed, the purpose of our study is to prove that DWR can work for general MIPs." [S015 preprint p. 8]; the success criterion stated in his sole voice, "On the other hand, anything but outperforming the general-purpose solver on instances that contain a decomposable problem structure would be a failure." [S070 p. 7], after "Testing on general mixed integer programs was very nice and gave a successful proof-of-concept, but diverted our attention from the true target instances of this research: those which bear structure." [S070 p. 5]; a structured set and a random MIPLIB set [S009 pp. 1, 5-6]; real graphs paired with random and edited twins of the same size [S065 pp. 7-8; S073 pp. 10-12]; one class where elementarity should matter and one where it should not [S085 pp. 23-25].
  - Step 3 (re-run under identical conditions): five codes on one machine under one limit in the 1996 Diplom thesis [S083 pp. 66-71]; reruns with older and open-source solvers to attribute a gain [S010 pp. 10-11]; a predecessor's unpublished procedure implemented as a setting in the same code after asking him [S068 pp. 2, 5, 8-10]; every competitor rerun on one core [S025 preprint pp. 16-18]; competitors rerun on own hardware with the same limit, one thread and CPLEX 22.1.0, older code by personal communication, the gaps to published counts explained [S089 pp. 22-23, 27-28]; only the subproblem method changed [S076 p. 28]; the baseline given the tailored code's heuristic and cuts [S115 pp. 17, 22]; stated, in his sole voice: "The settings, machines, and allowed computation times vary significantly between the papers discussed in the overview, and I was wondering how the comparison would be if all approaches were run under identical conditions." [S048 p. 2].
  - Step 5: "We use a shift s = 10 for time and s = 100 for nodes in order to decrease the strong influence of the very easy instances in the mean values." [S016 p. 4]; ablations in three directions [S073 pp. 13-14]; means only over commonly solved instances with their counts and a stated noise threshold for shared machines [S026 pp. 6, 8-9]; an ablation chain with a predecessor column, failures charged and a separate tuning set [S075 pp. 22-23]; losses listed in an appendix [S089 p. 42].
  - Step 6 (sizing): "Our algorithm is not an overall winner, but it is very robust in the sense that it deterministically gives satisfactory lower and upper bounds in reasonable computation time without particular tuning." [S010 p. 1]; "Of course, at the moment, our work is not intended to produce a competitive tool, but to provide a proof-of-concept and demonstrate that the direction is promising." [S032 manuscript p. 2]; a limitation in the abstract and a null result written up: "While this is an undesired result, it is valuable in highlighting a limitation to the proposed methods and the subproblem cuts, and it also gives an insight into the nature of (strong) redundancy." [S074 manuscript p. 23]; "These results therefore do not establish additional redispatch cost savings over current practice." [S075 p. 25].
- **Say–do update**: steps 1-3 and 5 ✅ in the algorithmic papers (above). Step 6 stays ⚠ and is now documented on full texts: 13 cards record a headline wording or an uncounted adverb that the tables do not carry (all 13 contradictions are step 6: S005, S018, S023, S028, S030, S040, S043, S046, S053, S058, S078, S112, D002), and the variants include many more of the same kind, in sole-authored texts too (uncounted *often*, a percentage without its instance set) [S008 manuscript pp. 5, 9, 13-14; S033 report p. 4] and in the book's illustrations (general wording on one root node or one instance) [S060 p. 28; S084 p. 95]. Careful sizing and lapses sit side by side in the same periods; neither is confined to early or late work. Only the sizing side of these cards is used here; their notes on numbers that do not match between text and tables stay in the cards (§7.4 W11). The step-3 gap is concentrated in application and expository texts, where numbers are borrowed and said to be [S010 pp. 10, 14; S004 pp. 24-26; S088 pp. 40-41; S077 pp. 89, 93].
- **Limitations update**: *no statistical test and no seed or permutation protocol* holds for the studies his group led [S065 p. 6; S073 p. 11; S050 preprint pp. 8, 10; S089 pp. 27-28; S076 p. 28; S075 pp. 17, 22-23], but he co-signed such protocols in the suite reports (five seeds, permuted copies, all-seeds counting [S013 pp. 14, 70-71; S014 arXiv pp. 4-5, 9; S019 pp. 4-7]). New devices against noise in his own line: a 5% noise threshold on shared machines [S026 p. 6], an absolute threshold below which an improvement is not counted and a tuning set kept apart from the benchmark [S075 pp. 22-23]. The book adds that node counts depend on implementation conventions [S087 pp. 31-32].
- **Different from standard practice (correction)**: the two-set move (a targeted set plus a general no-harm set) is SCIP-community practice, used by other authors in the same reports [S006 p. 13; S013 pp. 12, 20; S019 pp. 4-7, 13], so it does not set him apart. What does is testing where the method should fail [S027 p. 140; S015 preprint p. 8], a stated failure criterion [S070 p. 7], reruns of competitors including asking authors for unpublished code [S068 p. 2; S089 pp. 22-23], and the proof-of-concept framing [S016 p. 2; S032 manuscript p. 2; S015 preprint p. 27; S028 p. 2; S029 p. 6].

### Variants, contradictions and corrections (08 §3 and §5, copied)

- **V7 · Method 3 step 1.** Single self-generated test sets with no general set [S040 p. 9; S026 p. 6; S076 p. 28; S006 pp. 73, 113]; random sets sized by the application [S051 p. 10]; one generated instance [S047 pp. 1, 4-6]; one small instance with a known optimum, sized as a first step [S042 pp. 11, 16].

- **Method 3 step 6 (13 cards)**: listed in §2. Recorded as the documented form of SKILL.md's Inner Tension 3; the details stay in the cards.

| # | SKILL.md item | What the full texts show | Cards |
|---|---|---|---|
| C7 | Method 3 Limitations: no seed or permutation protocol | true for studies he led; he co-signed such protocols; new noise devices | §2 Method 3 |
| C8 | Method 3 Different from standard practice | the two-set move is SCIP-community practice | [S006 p. 13; S019 pp. 4-7, 13] |

- **Method 3 step 3**: give the baseline your own problem-specific components and add a control arm that copies the competitor's choice for one component, so the comparison isolates the contribution [S115 pp. 17, 22; S089 p. 24; S076 p. 28].

The synthesis's H14, written into SKILL.md as Method 3 step 2a (08 §5, copied):

### H14 (new) · Build the test set from one real case, and publish it so that it can be regenerated

**One line**: When real data are scarce, inconsistent or confidential, derive the test set from one real case (a size ladder, perturbed replicates per class, stress variants each breaking one property, random and edited twins), publish the generator's parameters, and say why the data are synthetic.

**Cards**: a size ladder by chronological truncation of one real shift [S027 pp. 137, 141]; stress instances that each break one property of the real data [S036 preprint p. 9]; simulated instances matching the real key figures because the database is unusable [S028 pp. 10-12; S010 p. 15]; a library stratified by size with ten perturbed replicates per class and every parameter published [S025 preprint pp. 15-16; S055 pp. 1, 3; S081 pp. 1-2]; each real graph paired with a random graph and an edited copy of the same size [S065 pp. 7-8; S073 p. 12]; a synthetic public benchmark because the real grid data are confidential [S075 pp. 22, 28]; the stated norm for authors [S091 p. 2].

**Checks**: recurrence ✅; say–do ✅; executable ✅; exclusivity ✗ (§4). → heuristic; the constructive side of warning sign B2.

### Added in T3.6

- **Evidence** rebuilt: Stated, his sole-voice sentence [S048 p. 2]; Practice [S070 p. 7; S015 preprint p. 8; S089 pp. 22–23, 27–28, 42; S115 pp. 17, 22; S068 pp. 2, 5]; Say–do with 08's counts (60 / 60 / 13; 76 works) and the step-6 reading [S010 p. 1; S074 manuscript p. 23]; variant bullets C8, C7 and V7 [S006 p. 13; S019 pp. 4–7; S065 p. 6; S013 pp. 14, 70–71; S040 p. 9; S051 p. 10]; the borrowed-numbers variant stays here [S010 pp. 10, 14; S088 pp. 40–41].
- **Step 1**: *plus a class where it should fail, the criterion written first (EP1)* [S027 p. 140; S070 p. 7].
- **Step 2a** (new): the synthesis's H14 as a sub-step (EP5) [S027 pp. 137, 141; S091 p. 2]; more cards above.
- **Step 3**: *Give the baseline your own components (EP3)* [S115 pp. 17, 22] (08 §5.5; the control arm [S089 p. 24; S076 p. 28] stays in the catalog).
- **Step 5**: *a noise threshold, a separate tuning set (EP6, EP7)* [S075 pp. 22–23] (also [S026 p. 6]).
- **Different from standard practice**: ✗ the two-set move is community practice (C8); the distinguishing moves [S027 p. 140; S015 preprint p. 8; S070 p. 7; S068 p. 2; S089 pp. 22–23]; the pre-synthesis notes *a generic method tested on instances chosen against it (2015)* and *a rival borrowed his tables in 2022; 05 C4* are in the Before block.
- **Limitations**: *in the studies his group led* (C7).

### Before T3.6 (moved verbatim)

````text
### Method 3: Adversarial, identical-conditions evaluation, with the claim sized to the measurement

**One line**: Test where the change can show and where it should do no harm, re-run every competitor under identical conditions, report losses and exclusions, and claim no more than the tables carry.

**Increment**: deepened: adds the protocol, the sole-authored statement and the lapses.

**Evidence**:
- Stated: settings, machines and time limits "vary significantly between the papers discussed"; "This part of the overview needs to be taken with a grain of salt."; of his own view "this perception may be personally biased" (TOP 2015, p. 360, sole); group guide: "It is crucial that you determine with which instances your modifications of settings or code can be seen" (`conduct-experiments.md`) [group].
- Practice: 39 MIPLIB instances where decomposition "would not be the first choice" (2015); competitors re-run with CPLEX 22.1.0 and the same limit, older code by personal communication, an appendix of instances an older method wins (arXiv:2602.04984); an old test set labelled "Not recommended for use anymore." (03 §1.1.4).
- Say–do consistency: ✅ stated + practised for steps 1–5. ⚠️ Step 6 is mixed: "globally better" against about 8% fastest (2015); "consistently outperforms all competitors" in the 2026 v1 abstract, cut in v2 (the introduction keeps an outperformance claim); "Optimal Solutions" in a 2008 title.

**Steps**:
1. Two test sets: one where the change can show at all, one general-purpose set that shows improvements and deteriorations.
2. Filter by difficulty and control diversity (e.g. instances needing at least 1,000 nodes with the previous version); retire old sets with a label.
3. Baselines: the host framework without your component, then the strongest competitor re-run by you (same machine, solver version, limit, threads). Ask authors for unpublished code; explain any gap to their reported numbers.
4. Smoke-test a short set before the campaign; keep log formats stable.
5. Report shifted geometric means with shifts, solved counts, profiles, gap closed, per-component ablations, every exclusion with its reason.
6. Size the claim: proof of concept if it is one, failure mode in the abstract, losses in an appendix, your bias in the text, no self-praise in release texts.

**🔴 Checkpoint**: a competitor not re-run under identical conditions is flagged in the text; no "often", "consistently" or "optimal" without counts or proof.

**Applies to stage**: experiment design, judging results, writing.

**Different from standard practice**: a generic method tested on instances chosen against it and published as a proof of concept (2015); competitors re-run where the field often borrows numbers (a rival borrowed his tables in 2022; 05 C4).

**Limitations**: no statistical test and no seed or permutation protocol (hMETIS ran with one fixed seed), although the 2015 paper calls variability "very pronounced". Needs a cluster and licences; lone version: re-run the host framework and one public competitor, and say what was not re-run.
````

<a id="method-4"></a>

## Method 4: Synthesis writing as a research instrument

> Changed in the T3.6 review fixes: see [Review fixes](#review-fixes).

### Full-text evidence (08 §2, copied)

### Method 4 · Synthesis writing as a research instrument

- **Strongest cards**:
  - Sole voice, 2001: the thesis chapter that carries the later survey's title, "Arguably, there are no new results in this chapter. Still, we are not aware of a comparable accumulation of various sources, enabling us to find better ways to relate things." [S027 p. 38], organised by the dual view [S027 pp. 51, 84], with the gaps named at section ends [S027 pp. 57-58, 73, 76-77, 84] and a bibliography meant to contribute in its own right [S027 p. 168]. Step 1 is visible: unstable duals in his own code that his static stabilization did not fix [S027 pp. 140, 142].
  - The survey and the primer: explanations and remedies of tailing off and dual oscillation in one notation, untested points written as such [S001 report pp. 2, 10, 18-22]; the primer's numbers checked by a third person [S002 pre-publication p. 27].
  - Survey as the origin of the generic solver, in his 2012 sole voice: collecting material for the primer is where the generic branch-and-price idea came from [S070 p. 5].
  - The degeneracy line (third author): two published methods unified in one notation give a new method and a theorem not explicit in the sources [S031 preprint pp. 2, 9-10, 14; S039 pp. 5, 7, 11-12]; "The original purpose of this work was a literature review preliminary to further researches, but we have come to see it as more than a summary." [S038 p. 19].
  - The book: one notation for convexification, discretization and their block variants with open questions published [S084 pp. 42-43, 64, 120]; corrections and credit (the Kantorovich attribution corrected with credit to Uchoa and Sadykov [S060 pp. 4, 49]; a PhD student's observation as a named proposition [S084 p. 112]; "In all our references, we list all the authors with all their first names, when we can." [S086 p. 57]); deferred subjects listed for later authors "by various authors hopefully following the notation introduced in this one" [D004 p. 8]; the unstable duals of 2001 get their systematic answer in the dual chapter [S088 pp. 39-58].
- **Say–do update**: keep ✅; the sole-voice evidence is now on full text [S027; S008 manuscript pp. 9, 15; S070 p. 5]. Step 6 (corrections credited) has full-text pages [S060 pp. 4, 49]. The variants (§3.1 V9) show the same move inside research articles.
- **Proposed Practice additions**: [S027 p. 38]; [S070 p. 5]; [S038 p. 19].

### Variants (08 §3.1, copied)

- **V9 · Method 4 inside research articles.** Known algorithms recast as the extreme cases of one construction [S061 pp. 1, 9, 17; S044 pp. 1-2, 10, 14]; scattered constraint groups collected into one model, "The contribution here lies mainly in the full collection of constraints rather than any individual set of constraints." [S075 p. 3]; open-question lists closing research papers [S053 p. 11; S112 p. 8; S046 p. 11; S034 p. 11; D001 arXiv p. 23; S030 arXiv p. 12].

### Added in T3.6

- **Evidence** rebuilt: Stated, the thesis sentence [S027 p. 38]; Practice [S001 report pp. 2, 10, 18–22; S070 p. 5; S031 preprint pp. 2, 9–10; S060 pp. 4, 49; D004 p. 8]; Say–do with 08's counts (21 / 14 / 0; 26 works) and the sole voice now on full text [S008 manuscript pp. 9, 15]; variants V9 and the degeneracy line [S061 pp. 1, 9, 17; S075 p. 3; S038 p. 19].
- **Step 1**: *(his: tailing-off and instability [S027 pp. 140, 142])*.
- **Step 3**: the pointer *(blog 2014, Evidence)* became *(blog 2014-11-21)*, since the blog quotes moved here with the old Evidence block.

### Before T3.6 (moved verbatim)

````text
### Method 4: Synthesis writing as a research instrument

**One line**: When your own code shows an effect you cannot fix, collect every published explanation into one notation, write early, treat every sentence you cannot write exactly as an open question, and publish what stays open.

**Increment**: deepened: surveys as his way of finding what is not understood, not only output.

**Evidence**:
- Stated: his most cited paper is "a collection of everything i could find about column generation because we wanted to have answers" (podcast 0:38:23, ASR); "Writing spawns new ideas." "Start now." "Proved a small result? Don't believe it until you have the nuts and bolts on paper." "Postponing the writing "to the end" is the worst idea you could have." (blog 2014-11-21, re-posted 2024); writing "mercilessly reveals what one does not know" (book p. xiii, joint).
- Practice: thesis chapter 2 (2001) carries the title of the 2005 survey; the Primer (2005); encyclopedia entries (2011); the book (2026). Four of his eight most cited works are expository.
- Say–do consistency: ✅ stated + practised (the book is joint).

**Steps**:
1. Start from an effect in your own runs that you cannot fix (his: tailing-off and instability).
2. Collect every published explanation and remedy into one notation.
3. Start now: write before the results are final, not "to the end" (blog 2014, Evidence).
4. Treat every sentence you cannot write exactly, including taken-for-granted "facts", as an open question.
5. Publish what stays open: 25 subjects deferred to "a second book" (p. 552); exercise 8.2, "Find all mistakes in this book." (p. 553).
6. Take corrections in and credit the corrector: a wrong Kantorovich attribution (2005) was corrected in the 2026 book after Uchoa and Sadykov raised it (05 §6).

**🔴 Checkpoint**: fix scope and a stop date first. His own warning, not his practice: "Know when to stop", "but I am not very good at it" (2014); the book was planned for 2015–17, appeared in 2026, and 16 planned chapters became 8.

**Applies to stage**: research agenda, idea generation, writing.

**Different from standard practice**: few solver researchers use the survey as the instrument that turns their own failures into an agenda.

**Limitations**: a survey also fixes errors (the attribution stood twenty years); a junior's survey needs a senior co-author. Lone version: a thesis chapter first, as he did.
````

<a id="method-5"></a>

## Method 5: Certify what you deliver: an exact relaxation bounds the heuristic

> Changed in the T3.6 review fixes: see [Review fixes](#review-fixes).

### Full-text evidence (08 §4, copied)

**One promotion: Method 5, *Certify what you deliver*.** The skill goes from four to five core methods. Clusters with three or more distinct cards read in full or in part, and the four checks:

| Cluster (merged by meaning) | Cards (full/part) | 1 Recurrence | 2 Say–do | 3 Executable, not standard | 4 Exclusivity | Result |
|---|---|---|---|---|---|---|
| Certify what you deliver: an exact relaxation bounds the heuristic | S012 S022 S030 S036 S051 D002 S035 S040 S010 S080 S018 S075 S033 S027, book (14 works plus the book) | ✅ 2001-2026, twelve projects | ✅ sole [S008 manuscript p. 13; S027 p. 127; S033 report p. 4]; joint [D002 p. 21; S022 p. 1] | ✅ | ✅ | **Promote: Method 5** |

### Method 5 (new) · Certify what you deliver: an exact relaxation bounds the heuristic

**One line**: When the user's instances are out of reach for an exact method, deliver the heuristic, but build an exact model of a relaxation (or the problem's own LP, or the compact MIP on sub-instances) whose optimum is a valid bound under a condition you state, report the gap per instance with that condition, and call optimal only what is proven.

**Four checks**:
1. *Recurrence* ✅: line planning [S012 report pp. 2, 10]; stabbing numbers, every rounding value next to its LP bound and, where the IP finishes, the optimum [S030 arXiv pp. 10-11]; shunting, the LP root bound offered as an estimate of a given solution's quality [S036 preprint p. 10]; permutation partitions, heuristics measured as ratios to the MIP optimum [S051 p. 11]; slab stacking, "We assess the quality of our solutions by computing instance-dependent lower bounds" [S022 pp. 1, 9-12]; coil coating, a branch-and-price bound for a deployed genetic algorithm [D002 pp. 21-22; S035 pp. 13-16]; resource leveling, a heuristic judged against branch-and-price bounds from both ends [S040 pp. 2, 11]; timetabling, lower and upper bounds [S010 p. 1]; districting, certified gaps [S080 p. 8]; the Kiel Canal, the heuristic bounded on sub-instances by the compact MIP of a relaxation [S018 manuscript p. 28]; power grids, solutions exact for the DC model, then checked by AC power flow and by operators [S075 pp. 5, 26]; the book gives every heuristic output with its gap [S088 pp. 26, 32, 75, 80]. Eleven projects, 2004-2026, twelve with the engine-scheduling project's pricing heuristics of check 2 (2001-2005).
2. *Say–do* ✅: his sole voice, "Fortunately, the dual bound gives a guarantee on its quality at any time. Heuristics should be used to construct or improve primal and dual solutions as often as it seems useful. This point cannot be overestimated." [S008 manuscript p. 13]; pricing heuristics shipped with a proven error [S027 p. 127; S033 report p. 4]; co-signed, "Assessing the quality of heuristic solutions is not only a theoretical contribution, but an important question in practice: How much optimization potential is left?" [D002 p. 21; S035 p. 13]; plus the blog and TEDx statements under G1. One acknowledged contradiction [S025 preprint p. 21].
3. *Executable and different from standard practice* ✅ (steps below). An exact relaxation is built for the certificate alone, in fields whose prior work was heuristic only (check 4), even a branch-and-price whose pricing is brute-force enumeration [S035 p. 14] and whose bound times are too large to report: "Its implementation is not tuned to performance because we used it as a proof of concept only, so we do not report computation times for lower bounds (which were huge)." [S035 p. 15].
4. *Exclusivity* ✅ on a narrower core (rewritten in the T3.6 review fixes): reporting a gap to a relaxation bound is common in exact OR and does not set him apart. What does is an exact relaxation built only to certify a delivered heuristic, its validity condition stated wherever the gap appears [D002 p. 22; S035 pp. 13-14] and its master seeded with the heuristic's columns [D002 p. 23; S035 p. 14], even with brute-force pricing [D002 p. 23; S035 p. 14] and bound times too large to report [S035 p. 15], in application fields whose prior work was heuristic only: slab stacking, where no exact approach had been applied [S022 p. 3]; coil coating, where the one earlier study used tabu search on a basic model [S035 p. 2]; districting, set against heuristic and manual procedures that evaluate a few alternatives [S080 p. 2]. Recurrence (it predates GCG and survives into the 2026 preprints) and explanatory power (Common Misreading 5) [S008 manuscript p. 13] support the promotion but are not this check.

**Steps**:
1. Write down the claim the delivered plan will carry: a gap to what, under which rules [S018 manuscript p. 28].
2. Choose the relaxation: drop the feature that makes the exact model intractable and keep what decides quality (keep the timing [S022 pp. 9-10]; cost blocks of consecutive items exactly and only local costs between blocks [D002 pp. 21-23]; limit the look-back to short concatenated subsequences [S035 pp. 13-14]; the compact MIP on sub-instances [S018 manuscript p. 28]; the exact IP's own LP [S030 arXiv pp. 10-11; S053 pp. 3-4]).
3. State the bound's validity condition wherever the gap is stated, the abstract included: "Hence, we use the FIFO rule in the integer program and thereby obtain lower bounds for the case when the FIFO rule is used." [D002 p. 22].
4. Solve the relaxation exactly on a framework (branch-and-price in SCIP [D002 p. 25; S035 p. 14]); seed its master with the heuristic's columns [D002 p. 23; S035 p. 14].
5. Report one row per instance with the bound, the heuristic value and the optimum or the incumbent as an upper bound [S030 arXiv pp. 10-11], in the owner's unit [S018 manuscript p. 28]; call optimal only what is proven, "Für wenige Bundesländer/Regierungsbezirke konnten wir Optimalität nachweisen." [S080 p. 8].
6. If the bounds are weak, say so and make better bounds the next step [S025 preprint p. 21].

**🔴 Checkpoint**: a delivered plan whose gap has no stated condition, or a gap computed against a different objective or horizon than the owner's, is not certified [D002 p. 22; S035 pp. 13-14; S027 pp. 143, 147].

**Applies to stage**: applied projects, deployment, writing. **Relation to existing items**: absorbs H2 (keep H2 as a one-line pointer to Method 5 so that labels stay stable) and gives G1 its procedure. **Limitations**: the certificate is only as wide as its condition (the coil-coating case, §3.3 C10); dual bounds can be uninformative [S025 preprint p. 21]; the order of certificate and deployment is not documented in the record [S035 pp. 1, 17].

### Contradiction (08 §3.2, copied)

- **Method 5 (new, §4) and G1**: a 2016 MINLP paper offers a heuristic without a bound and lists dual bounds as the first future step, acknowledging that "The (mostly very weak) dual bounds provided by BARON does not contribute meaningful information." [S025 preprint p. 21].

### Added in T3.6

- **New method** in SKILL.md, house format, numbered 5 (the four existing methods keep their numbers). One line shortened from 08's; Stated [S008 manuscript p. 13]; Practice [S022 pp. 1, 9–12; D002 pp. 21–23; S035 pp. 13–16; S018 manuscript p. 28; S080 p. 8; S030 arXiv pp. 10–11]; Say–do (sole [S033 report p. 4]; joint [D002 p. 21]; 14 / 1 / 1 cards per the mining summary); variants C10, the S025 contradiction and the cost of the certificate [S035 pp. 1, 13–17; S025 preprint p. 21]; six steps and the checkpoint from 08, shortened; Limitations from 08.
- **Relations**: H2 stays as a one-line pointer to Method 5, so that labels stay stable; G1 names Method 5 as its procedure; Misreading 5 says Method 5 resolves the pairing; Workflow A step 5, the Routing heuristic row and the Roundtable Card's default recommendation point to it.

<a id="workflows"></a>

## Stage workflows

> Changed in the T3.6 review fixes: see [Review fixes](#review-fixes).

### Full-text evidence (08 §2.5, §3.3 C2 and §5 H12, copied)

| Item | Cards citing it in their method links (read in full or part) | Update |
|---|---|---|
| Workflow G (order *[inferred]*) | S007 S008 S088 | now a stated source: research the problem first, profile second, a heuristic last [S007 manuscript p. 14: "The most honorable answer to that is: Research your problem!"]; profile first, then stabilization and fewer exact calls, then research the problem [S008 manuscript p. 14]. The two entries order the last steps differently. |

| # | SKILL.md item | What the full texts show | Cards |
|---|---|---|---|
| C2 | Workflow B checkpoint (a) *[inferred]* | practised in 2011 and 2015 | [S032 manuscript p. 8; S026 p. 7] |

**Correction it carries**: Workflow G step 3's *stabilisation last* is an inferred order; the book ties stabilization to masters that are costly relative to pricing [S088 pp. 52, 58], and the 2010 entry puts it after profiling [S008 manuscript p. 14]. Replace *last* by *after the time split says the master or the duals are the problem*.

### Added in T3.6

- **Workflow A**: step 1, *plan for the planner who executes* (H3 extension); step 2, H13; step 3, Method 3 step 2a; step 4, plans validated by the planners on a picture of the whole schedule [S035 pp. 14–15] (also [S018 manuscript p. 25]); step 5, Method 5.
- **Workflow B**: checkpoint (a) ✗ *practised* [S032 manuscript p. 8; S026 p. 7] (C2); *unless a measured go reason holds (Method 1 Variants)* (V1).
- **Workflow C**: step 1, Farkas pricing (DM9) [S008 manuscript pp. 6–7; S023 p. 10 in the catalog]; step 2, the pricing cascade (DM1) [S027 pp. 133–135]; step 3, *the time split picks the accelerator (H12)*; step 3a (new), H11 and DM16 [S029 p. 10 in the catalog].
- **Workflow D**: step 1, *plus a class where it should fail*; step 2, *(2a for synthetic sets)*.
- **Workflow E**: step 1, WM10 [S115 pp. 3, 24, 30 in the catalog]; step 3, the journal version as the correction pass (H8); checkpoint, *recompute the abstract's numbers (WM11)*.
- **Workflow F**: step 1, *end with open questions (WM3)*.
- **Workflow G**: heading *[inferred order …]* → *[order partly stated in 2010 …]* (S007 and S008 give an order, 08 §2.5); step 3, ✗ *stabilisation last* → stabilisation *when the time split blames the master or its duals (H12)* [S088 pp. 52, 58] (also [S008 manuscript p. 14]); step 4, H11; step 5, the 2010 sentence [S007 manuscript p. 14]. The two entries order the last steps differently: research the problem, profile, then a heuristic [S007 manuscript p. 14]; profile, then stabilization and fewer exact calls, then research the problem [S008 manuscript p. 14].

### Before T3.6 (moved verbatim)

````text
## Stage Workflows

### Workflow A: Choosing and modelling an applied problem

**Input**: a planner's problem, current planning practice, sample data.

**Steps**:
1. Ask the owner the three questions (H3).
2. Look for the classic problem inside ("there is a TSP somewhere around the corner", blog 2015).
3. Collect data with a goal in view; expect it to take longest (book p. 508).
4. Show first plans; add the constraints nobody mentioned.
5. Place the project on the ladder motivation → applicability → implemented → makes money (G3), then write the compact model (Method 1).

**🔴 Checkpoint**: if the owner cannot say which of two plans is better, stop modelling the objective and go back to them.

**Output**: a compact model, an agreed objective, a data pipeline. (Mostly stated; 04 G.)

### Workflow B: Deciding whether to decompose

**Input**: the compact model and its solver log.

**Steps**:
1. Method 1 steps 1–4: baseline, candidate subproblem, probe.
2. Compare the Dantzig-Wolfe root bound with the LP bound and with the solver's root bound after its own cuts.
3. With several possible reformulations, choose by Method 2.
4. Check whether a "wrong technique" verdict rests on a formulation you can change (H5); choose the framework.

**🔴 Checkpoint (go/no-go)**: go only if (a) the Dantzig-Wolfe root bound beats the compact root bound after the solver's cuts, not only the LP bound [inferred: cuts can recover Dantzig-Wolfe bounds, Chen, Günlük, Lodi 2025], and (b) pricing has a named algorithm other than a general MIP (H1). Otherwise Method 1's stop rule: stay with branch-and-cut or change the formulation (H5). He states no threshold for a "material" gain: report the measured gap; the user decides.

**Output**: a go/no-go note with both bounds, pricing design and framework.

### Workflow C: Building and tuning the algorithm

**Input**: a go decision and a framework.

**Steps**:
1. Basic column generation first, "maybe keep it simple first" (book p. 508).
2. Heuristic and partial pricing, several cheap columns per round; monitor the Lagrangian bound (H1).
3. Measure iterations, master against pricing time and tree size on large instances before adding stabilisation or cuts: "all that may be relevant, but need not be relevant" (CO@Work 2020).
4. Preliminary runs pick between variants; analyse only the winner in full (03 §1.4.2).
5. New components ship off by default (H7); smoke tests and CI before campaigns [group].

**🔴 Checkpoint**: a too-good result or a statistic that does not add up stops the campaign until the instrument is checked (H6).

**Output**: code with per-component switches and a settings file.

### Workflow D: Experimental evaluation

**Input**: code, candidate test sets, competitor codes.

**Steps**:
1. Two test sets, structured and general (Method 3 step 1).
2. Method 3 steps 2–5.
3. Size the claim (Method 3 step 6), narrower where the compact model or host default is competitive (Method 1 step 2); conference, then journal (H8).

**🔴 Checkpoint**: Method 3's. **Output**: tables with shifts and exclusions, ablations, an appendix of losses.

### Workflow E: Judging results and writing

**Input**: results and a draft.

**Steps**:
1. Size the claim (Method 3 step 6); label interpretations until proved (Method 2 exit B).
2. Write early and let the writing expose gaps (Method 4).
3. Write a conclusion that concludes (B3); send a refereed-conference version first (H8).

**🔴 Checkpoint**: delete every "often", "consistently" and "optimal" the tables do not carry; his own record shows where this slipped.

**Output**: a hedged abstract, a limits paragraph, a real conclusion.

### Workflow F: Agenda from an unexplained effect, and after publication

**Input**: a recurring effect in your runs, or released code and a published text.

**Steps**:
1. Method 4 steps 1–5 for an effect you cannot fix; turn a weak step of your own tool into a paper (H4).
2. Write the user documentation (his commits, 2019).
3. Re-run old code with current solvers when a discussion calls for it: "our old code, install a fresh CPLEX" (TOP 2015, p. 361).
4. Accept corrections and pass on the better reference (Method 4 step 6).

**🔴 Checkpoint**: none stated; no printed reply to the main critics of generic branch-and-price was found (05 §2.3). Thin evidence.

**Output**: an open-question list; maintained code and corrected texts.

### Workflow G: Unsticking a decomposition project [inferred order; each step's source given]

**Input**: logs of the latest runs, the compact model's log if any, time spent and the deadline.

**Steps**:
1. Instrument first (H6): on one small instance re-check timing, counts and the suspicious number. Of his PhD code: "maybe it was buggy" (podcast 0:37:15, ASR).
2. Re-open the go decision: Workflow B steps 1–2, same machine and limit. If its checkpoint fails, stop decomposing or change the formulation (H5); say which and skip steps 3–4.
3. Root slow or tailing off: measure first (Workflow C step 3), then heuristic and partial pricing, branching when the Lagrangian gap is small (H1); stabilisation last.
4. Tree explodes: does branching keep the pricing structure, on original variables (Method 1 step 6, H5)?
5. Effect persists unexplained: Workflow F, as an open question, not a tuning target.

**🔴 Stop**: at most three ranked causes, each with the run that confirms or rules it out. Continue-or-kill: his record has no rule (Tension 4). Propose a stop date and the deciding number, labelled "not Lübbecke-style"; the user decides.

**Output**: diagnosis, next run, deciding number, stop date.

**Stages without evidence**: see the last Routing row.
````

<a id="heuristic-1"></a>

## Heuristic 1: Heuristic inside an exact frame

> Changed in the T3.6 review fixes: see [Review fixes](#review-fixes).

### Full-text evidence (08 §2.5, §3.1 V10, §3.3 C9 and §5.5, copied)

| Item | Cards citing it in their method links (read in full or part) | Update |
|---|---|---|
| H1 Heuristic inside an exact frame | 29: S001 S002 S006 S007 S008 S011 S015 S023 S024 S027 S029 S031 S033 S038 S044 S049 S050 S054 S060 S065 S073 S075 S077 S084 S085 S086 S087 S088 S115 | ✅ dated to 2001-2003 [S027 pp. 125, 133-135; S024 p. 10; S054 manuscript p. 9: "Our bottleneck procedure is the pricing subproblem, which, as a general rule, should be solved exactly only when heuristics fail."] and written alone in 2010 [S008 manuscript pp. 8-9, 14]; qualification and devices in §5.5 |

- **V10 · H1.** The exact combinatorial pricer mattered less than expected, the combinatorial dual bound more: "In our case, the combinatorial pricing is a nice add-on but nonetheless has not that much influence on the solution time as expected." [S073 p. 13].

| # | SKILL.md item | What the full texts show | Cards |
|---|---|---|---|
| C9 | H1: *monitor the Lagrangian dual bound, you get it for free* | free only in iterations where pricing is exact or a relaxation; heuristic pricing gives no valid bound | [S008 manuscript p. 3; S086 pp. 16-17; S088 p. 24; S060 p. 20] |

- **H1, devices and qualification**: (a) the free Lagrangian bound needs exact or relaxed pricing in that iteration (§3.3 C9); (b) dual-bound fathoming in DP pricing, a state dropped when its cost minus all positive duals it can still collect cannot beat min{0, incumbent}, and its γ-scaled form as a heuristic with a proven relative error [S027 pp. 121-127; S033 report pp. 3-4; S024 pp. 6-7], credited as rediscovered: "This note provides a simple means to reduce the state space of these algorithms, rediscovering the fathoming technique in dynamic programming" [S033 report p. 2]; (c) select returned columns for diversity, not by reduced cost alone [S060 pp. 15-16, 41-42; S050 preprint p. 9]; (d) "it is neither mandatory to add a most profitable column to the restricted master program, nor are we restricted to adding only one column at a time" [S024 p. 9]; (e) pricing optima and cuts found while solving the pricing problem become valid inequalities for the original LP [S068 pp. 7-8]; (f) the 2026 book's form: "ideally, one needs to solve the pricing problem to optimality only once, in the last column generation iteration, to prove optimality of the MP." [S060 p. 17].

### Added in T3.6

- *In print since 2003* [S054 manuscript p. 9]; ✗ *the bound is free only where pricing is exact or a relaxation* [S060 p. 20] (C9; also [S008 manuscript p. 3; S086 pp. 16–17; S088 p. 24]); *devices DM1, PD6* (the pricing cascade [S027 pp. 133–135; S060 pp. 17–18]; dual-bound fathoming [S027 pp. 121–127; S033 report pp. 2–4]). Column diversity [S060 pp. 15–16, 41–42; S050 preprint p. 9] and V10 [S073 p. 13] stay here.

### Before T3.6 (moved verbatim)

````text
2. **H1 · Heuristic inside an exact frame.** If pricing is expensive, price heuristically to the end, return several columns per round, do not call every pricing problem each round, and "monitor the Lagrangian dual bound, you get it for free. So when the duality gap is small just branch" (CO@Work 2020, 1:34:42).
   - Stated (CO@Work 2020): "try to generate more than one solution in the pricing problem if you can" (1:33:30); "generate cheaply columns that will always help you, before you start solving the pricing problem exactly" (1:33:36–1:33:41); exact pricing for the proof, "but when you're lucky only once" (1:34:07–1:34:13). If the master is hard to solve ("you need an interior point method or the simplex method or whatever method to solve that", 1:34:56), get duals from subgradient iterations instead, from the Lagrangian literature (1:35:01–1:35:19).
   - Case: GCG defaults, checked in the code: one heuristic pricing iteration at every depth; all pricing problems solved every 10th round [group]. "Remember: B&B stays exact, but heuristics help to speed up the search and satisfy the practitioner." (blog 2014-12-19).
````

<a id="heuristic-2"></a>

## Heuristic 2: Certificate before deployment (now a pointer to Method 5)

> Changed in the T3.6 review fixes: see [Review fixes](#review-fixes).

### Full-text evidence (08 §2.5 and §3.3 C10, copied)

| Item | Cards citing it in their method links (read in full or part) | Update |
|---|---|---|
| H2 Certificate before deployment | 10: D002 S012 S018 S022 S027 S035 S040 S075 S080 (S025 a contradiction) | promoted into Method 5 (§4); case corrected (§3.3 C10) |

| # | SKILL.md item | What the full texts show | Cards |
|---|---|---|---|
| C10 | H2 case: *a genetic algorithm certified within 10% by an IP, then deployed* | the certificate covers short-term instances with FIFO solutions against the FIFO-restricted optimum, on makespan; the module has been in use since December 2009 and the paper was received in March 2010; the text does not say whether the bound came before deployment; the 2009 workshop version states the FIFO condition of its bound | [S035 pp. 1, 13-14, 16-17; D002 pp. 21-22] |

### Added in T3.6

- One line: *ship it with a bound: now Method 5*. Case: ✗ *certified only on short-term FIFO instances and in use from December 2009* [S035 pp. 1, 13–14] (C10; the 2009 version states the FIFO condition of its bound [D002 pp. 21–22]); the Koch quote is unchanged.

### Before T3.6 (moved verbatim)

````text
3. **H2 · Certificate before deployment.** If a heuristic goes to a practitioner, ship it with a bound.
   - Case: coil coating, a genetic algorithm certified within 10% by an IP, then deployed (DOI 10.1287/mnsc.1100.1302); from Koch: "never ever deliver to a practitioner a solution to any optimization problem that is not 2-opt" (blog 2014-12-19).
````

<a id="heuristic-3"></a>

## Heuristic 3: Three questions for the problem owner

> Changed in the T3.6 review fixes: see [Review fixes](#review-fixes).

### Full-text evidence (08 §2.5, §3.3 C11, §4 and §5.5, copied)

| Item | Cards citing it in their method links (read in full or part) | Update |
|---|---|---|
| H3 Three questions for the owner | 10: D002 S024 S027 S035 S036 S037 S054 S075 S080 S115 | the *visible only in abstracts* note is obsolete; extension in §5.5 |

| # | SKILL.md item | What the full texts show | Cards |
|---|---|---|---|
| C11 | H3: *Practice visible only in abstracts and chair pages* | full-text practice: owners' scepticism, officers on patterns, feedback at every stage, constraints left out on purpose for a first prototype, planners validating plans, owner-set weights | [S027 pp. 28, 31, 137, 165-166; S054 manuscript pp. 10-11; S035 pp. 4, 14-15; D002 pp. 20, 24-25; S018 manuscript pp. 4, 24-25; S080 pp. 3-4, 8; S075 pp. 2, 26] |

| Cluster (merged by meaning) | Cards (full/part) | 1 Recurrence | 2 Say–do | 3 Executable, not standard | 4 Exclusivity | Result |
|---|---|---|---|---|---|---|
| Design the delivered plan for the planner | S037 S027 S054 S036 S035 D002 S018 S080 S075 (9) | ✅ 1998-2026 | ✅ sole [S027 pp. 165-167]; joint [S054 manuscript p. 11; S037 p. 7] | ✅ | ⚠ practitioner folklore | H3 extension (§5.5) |

- **H3, extension *design the delivered plan for the planner who executes it***: the manager is not the user; the plan is a suggestion; "Partial solutions fixed manually must never be overruled by the computer." [S054 manuscript p. 11; S027 p. 167]; "Consequently, the conflict between optimality and robustness of solutions should rather be decided in favour of reliability, and implemented in the system accordingly." [S037 p. 7]; "one should not try to make suggestions on a very high level of detail. It turns out that such suggestions cannot be implemented in practice." [S036 preprint p. 3]; validate plans with the planners through visualizations of the whole schedule [S035 pp. 14-15; S018 manuscript p. 25]; re-realize the human plans under the model's rules before comparing [S018 manuscript p. 29]; let the owner set the criteria weights and hand the trade-off back [S080 pp. 4, 8]; read the optimal plan of a real instance as a diagnostic of the data, "Large detours are rarely attractive in the optimum, but a strict bound could render such an instance infeasible and would hide where the candidate-station set is too sparse." [S115 p. 28]. One further deployment sub-point recorded on the S027 and S054 cards overlaps sealed material and is held back; it must not enter SKILL.md.

### Added in T3.6

- ✗ *Practice visible only in abstracts and chair pages* → *in full texts 1998–2026, not only abstracts* (C11).
- **Extension** *plan for the planner who executes*: the manual-fixing rule [S054 manuscript p. 11], reliability over optimality [S037 p. 7]; the other cards of the extension stay here [S036 preprint p. 3; S035 pp. 14–15; S018 manuscript pp. 25, 29; S080 pp. 4, 8; S115 p. 28]. The held-back sub-point is named in [Held back](#held-back).

### Before T3.6 (moved verbatim)

````text
4. **H3 · Three questions for the problem owner.** What information does the plan handed to the executor contain? Shown two plans, can you say which is better and why? Which requirements are truly fixed, and which exist only in our heads? Then read the first plans for forgotten constraints.
   - Case: blog "Millionen Entscheidungen!", 2014-10-27 (02 §4.1); "use that power responsibly" (2026). Practice visible only in abstracts and chair pages.
````

<a id="heuristic-4"></a>

## Heuristic 4: Turn the tool's sub-problem into a research problem

> Changed in the T3.6 review fixes: see [Review fixes](#review-fixes).

### Full-text evidence (08 §2.5 and §3.3 C12, copied)

| Item | Cards citing it in their method links (read in full or part) | Update |
|---|---|---|
| H4 Tool's sub-problem as research problem | 14: S005 S013 S016 S027 S033 S035 S050 S058 S066 S068 S070 S074 S076 S118 | the link is stated, not only inferred: detection becomes hypergraph partitioning research [S070 p. 6, sole]; the matrix decomposition behind DW named as main motivation [S050 preprint p. 1] |

| # | SKILL.md item | What the full texts show | Cards |
|---|---|---|---|
| C12 | H4: *The link is [inferred]* | stated in his sole voice and in a joint paper | [S070 p. 6; S050 preprint p. 1] |

### Added in T3.6

- *The link is [inferred]* → ✗ *stated, not inferred* [S070 p. 6; S050 preprint p. 1] (C12).

### Before T3.6 (moved verbatim)

````text
5. **H4 · Turn the tool's sub-problem into a research problem.** If a step of your own solver is weak, make it a paper.
   - Case: detection became a branch-and-price study of hypergraph vertex separation (DOI 10.1007/s12532-019-00171-5); choosing a decomposition became the 2018 and 2017 papers. The link is [inferred].
````

<a id="heuristic-5"></a>

## Heuristic 5: Reopen a "wrong technique" verdict by changing the formulation

> Changed in the T3.6 review fixes: see [Review fixes](#review-fixes).

### Full-text evidence (08 §2.5, §4 and §5.5, copied)

| Item | Cards citing it in their method links (read in full or part) | Update |
|---|---|---|
| H5 Reopen a verdict by changing the formulation | 6: S002 S007 S027 S084 S087 S089 | ✅; "the integrality property is an attribute of the model, not of the problem." [S087 p. 26]; refinement in §5.5 |

| Cluster (merged by meaning) | Cards (full/part) | 1 Recurrence | 2 Say–do | 3 Executable, not standard | 4 Exclusivity | Result |
|---|---|---|---|---|---|---|
| Integrality only where needed | S036 S112 S028 S010 S089, book (5 + book) | ✅ 2005-2026 | ⚠ in-paper only [S089 p. 7; S087 p. 26] | ✅ | ✗ standard modelling | H5 refinement (§5.5) |

- **H5, refinement *the formulation also decides where integrality is needed***: keep binaries only where a fixing leaves a transportation, flow or matching problem [S036 preprint p. 8; S112 pp. 4-5]; project a dimension out by a combinatorial feasibility theorem and recover it exactly [S028 p. 4; S010 pp. 2-4]; prove that the extended variables may stay continuous by constructing an integral optimum, "Crucially, we prove that integrality needs to be enforced only on the variables inherited from the natural formulation, whereas the variables coming from the extended formulation can be safely relaxed to continuous without affecting optimality" [S089 p. 7]; check that the LP algorithm returns an extreme point when integrality is dropped [S087 p. 26].

### Added in T3.6

- The book's sentence on the integrality property [S087 p. 26]; the refinement *the formulation also decides where integrality is needed* stays here with its cards [S036 preprint p. 8; S112 pp. 4–5; S028 p. 4; S010 pp. 2–4; S089 p. 7].

### Before T3.6 (moved verbatim)

````text
6. **H5 · Reopen a "wrong technique" verdict by changing the formulation.** If the literature says column generation fails for a class, check its formulation and branching, and try another.
   - Case: the k-vertex-cut preprint changes formulation and branching, titled "strikes back" (arXiv:2602.04984); a chair thesis template, "Branch-and-Price Applications: Improving on the Literature" (04 E3).
````

<a id="heuristic-6"></a>

## Heuristic 6: Too-good results are a bug signal; check the instrument first

### Full-text evidence (08 §2.5, copied)

| Item | Cards citing it in their method links (read in full or part) | Update |
|---|---|---|
| H6 Too-good results are a bug signal | 4: S006 S025 S041 S088 | ✅ light: a below-optimum objective read as a precision limit [S088 p. 46]; a published optimum corrected with its cause, the solver's optimality tolerance [S041 manuscript p. 14] |

### Added in T3.6

- *An optimum corrected with its cause* [S041 manuscript p. 14] (the cause, the solver's optimality tolerance, is in the card's quote; the precision-limit reading [S088 p. 46] stays here).

### Before T3.6 (moved verbatim)

````text
7. **H6 · Too-good results are a bug signal; check the instrument first.** If a number looks too good or a statistic does not add up, fix the measurement before the claim.
   - Case: "the results are too good ... there must be something wrong" (podcast 0:09:17, ASR). His commits: timing output removed because "the time in the individual detectors seems to be wrong" (67dc6a57); a stall traced to the commit that caused it (493fb6c0); master-only variables no longer counted as linking (fe9edd67).
````

<a id="heuristic-7"></a>

## Heuristic 7: A new component ships off until the evidence is in

### Full-text evidence (08 §2.5 and §3.1 V11, copied)

| Item | Cards citing it in their method links (read in full or part) | Update |
|---|---|---|
| H7 Component ships off until the evidence is in | 9: S005 S006 S009 S013 S014 S019 S027 S050 S115 | ✅ but not exclusive: the SCIP release-report norm [S019 pp. 13, 19-21, 32]; variants [S009 p. 6; S115 p. 23] |

- **V11 · H7.** A risky component gated by a conservative learned rule with the default solver as exit, "As GCG may perform very poorly when not a “right” structure is detected we try to keep the false positives low, even if this implies accepting more false negatives and thus not exploiting the full potential of GCG." [S009 p. 6]; determinism kept with parallel pricing by a fixed insertion order [S115 p. 23] instead of single-threaded pricing [S019 p. 32].

### Added in T3.6

- ⚠ *Not exclusive: SCIP release-report norm* [S019 pp. 13, 19–21]; V11 stays here [S009 p. 6; S115 p. 23; S019 p. 32].

### Before T3.6 (moved verbatim)

````text
8. **H7 · A new component ships off until the evidence is in.** If it helps on some instances, keep it off by default until a general set shows no harm.
   - Case: strong branching for branch-and-price, promising in 2021, still `DEFAULT_USESTRONG FALSE` in 2026, with no documented reason or follow-up; pricing single-threaded by default for determinism [group].
````

<a id="heuristic-8"></a>

## Heuristic 8: Refereed conference first

> Changed in the T3.6 review fixes: see [Review fixes](#review-fixes).

### Full-text evidence (08 §2.5, §4 and §5.5, copied)

| Item | Cards citing it in their method links (read in full or part) | Update |
|---|---|---|
| H8 Refereed conference first | 9: D001 S026 S030 S032 S041 S046 S051 S112 S118 | ✅ eight pairs carded (one member of one pair at abstract level); the journal version as a correction and sizing pass (§5.5) |

| Cluster (merged by meaning) | Cards (full/part) | 1 Recurrence | 2 Say–do | 3 Executable, not standard | 4 Exclusivity | Result |
|---|---|---|---|---|---|---|
| Later version as correction and sizing pass | S041 S046 S015 S031 S074 (5) | ✅ | ⚠ referee thanked for a more meaningful setup [S015 preprint p. 28] | ✅ | ✗ | H8 evidence (§5.5) |

- **H8, the journal version as the correction and sizing pass**: conference-to-journal pairs read: S030 to D001, S112 to S046 and S051, S053 to S041, S032 to S015, H001 to S031, S040 to S026, S065 to S073, and the talk S118 to S074. The journal pass recomputes every number of the conference version and states each correction with its cause [S041 manuscript p. 14], replaces an adverb by a count (1564 of 1800) [S041 manuscript p. 12], reproves a bound without the earlier assumption at a weaker constant [S046 p. 9], and changes the time measure to time to the same bound [S015 preprint pp. 25, 28].

### Added in T3.6

- *The journal version recomputes and corrects* [S041 manuscript pp. 12, 14]; the eight pairs and the other cards stay here [S046 p. 9; S015 preprint pp. 25, 28].

### Before T3.6 (moved verbatim)

````text
9. **H8 · Refereed conference first.** Send an extended abstract to a refereed conference, then the journal version.
   - Case: six conference-to-journal pairs, SODA 2004 to IPCO 2011; SEA is the group's usual stop (01 §1.6). Not exclusive to him.
````

<a id="heuristic-9"></a>

## Heuristic 9: One thesis, one plug-in on a shared instrument; the head as editor

### Full-text evidence (08 §2.5, copied)

| Item | Cards citing it in their method links (read in full or part) | Update |
|---|---|---|
| H9 One thesis, one plug-in; the head as editor | 7: S005 S006 S013 S014 S016 S019 S075 | ✅ credit lists give GCG code to students and staff [S005 p. 39; S006 pp. 82-83; S019 pp. 39-40]; one component per doctoral researcher [S075 pp. 3-4, 28] |

### Added in T3.6

- Not changed in SKILL.md; the full texts confirm it: the suite reports' credit lists give the code to students and staff and him the coordination [S005 p. 39; S006 pp. 82–83; S019 pp. 39–40], and one component per doctoral researcher is integrated into one code [S075 pp. 3–4, 28].

### Before T3.6 (moved verbatim)

````text
1. **H9 · One thesis, one plug-in on a shared instrument; the head as editor** (overturned). If you lead a group around a solver, scope each thesis as one component with its own setting and test target, and do merging, documentation and release notes yourself.
   - Case: structure detection runs through eight theses over twelve years (04 E1–E2); new hires "improve GCG by joining (heading?) the dev team" (Opt-Net 2019); his 92 commits (2018–21) are merges, bug traces, docs and release chores. Cost: several long-serving developers have no catalogued dissertation (04 H). Lone version: one component of a maintained code.
````

<a id="heuristic-10"></a>

## Heuristic 10: Ask one named outside expert in

### Full-text evidence (08 §2.5, copied)

| Item | Cards citing it in their method links (read in full or part) | Update |
|---|---|---|
| H10 Ask one named outside expert in | 6: D001 S024 S027 S030 S063 S071 | ✅ co-referees [S027 pp. 1, 6]; experts asked to settle a status question [S063 p. 2]; the predecessor asked about his unpublished study [S068 pp. 2, 5] |

### Added in T3.6

- The co-referees [S027 pp. 1, 6]; the other two cases stay here [S063 p. 2; S068 pp. 2, 5].

### Before T3.6 (moved verbatim)

````text
10. **H10 · Ask one named outside expert in.** If your work leans on a school you are not part of, ask its leading figure to referee or visit.
    - Case: he asked for Desrosiers as thesis referee, which became 25 years of joint work (04 A3, I).
````

<a id="heuristic-11"></a>

## Heuristic 11: Judge every branching rule and cut by what it does to the pricing problem

> Changed in the T3.6 review fixes: see [Review fixes](#review-fixes).

### Full-text evidence (08 §4 and §5, copied)

| Cluster (merged by meaning) | Cards (full/part) | 1 Recurrence | 2 Say–do | 3 Executable, not standard | 4 Exclusivity | Result |
|---|---|---|---|---|---|---|
| Pricing-compatibility as the filter for branching and cuts | S007 S065 S073 S050 D002 S035 S040 S026 S089 S115 S019, book (11 + book) | ✅ 2009-2026 | ✅ [S001 report p. 24; S008 manuscript p. 14; S077 pp. 9, 17] | ✅ | ✗ the shared core concern of branch-and-price design, which the book presents as the field's state [S077 pp. 17, 22, 38, 49-50, 94-95] | Heuristic H11 (§5) |

### H11 (new) · Judge every branching rule and cut by what it does to the pricing problem

**One line**: Before adding a branching rule or a cut family to a branch-and-price code, write down what it does to the pricing problem; keep the decisions the pricing algorithm can absorb, and enforce the rest in the master or not at all.

**Cards**: pricing-compatible branching on original variables enforced as bound changes or arc deletions in pricing [S007 manuscript p. 11; D002 pp. 23-24; S035 p. 14; S040 p. 7; S115 pp. 17, 19]; branching encoded as infinite-capacity arcs so that pricing stays a min cut [S089 p. 19]; branching whose children keep the pricing duals non-negative, with a binary-program pricer only where needed [S065 p. 4; S073 pp. 4-7]; clique-cut duals carried onto hyperedges of the min-cut pricing [S065 p. 5]; robust branching on original variables so that tailored pricing stays applicable, while non-robust master rows may destroy it [S019 pp. 27-28]; relax the pricing domain where the master's rows repair it, and keep a relaxed dominance valid only if every arc that can be part of a feasible path stays in the graph [S085 pp. 18-19, 38]; master equalities relaxed to covering form when costs are non-negative [S089 p. 14; S115 pp. 10, 12]; integrality only on the original variables, so that branching on x leaves pricing unchanged [S089 pp. 7-11, 19]; cut strength escalated only while pricing can bear it, cuts rolled back when pricing exceeds a label-count threshold [S077 pp. 57-58, 83]; a check that a cut family can ever be violated by a reformulated point [S077 pp. 11-12]; a pricing-domain filter audited for false negatives [S084 p. 82].

**Checks**: recurrence ✅; say–do ✅; executable ✅; exclusivity ✗ (§4). → heuristic.

**Steps**: (1) list the candidate rules and cuts in x- and λ-space [S077 pp. 23-24, 41-42]; (2) for each, state its effect on pricing: a bound change, a new resource, a dual of uncertain sign, a broken dominance [S085 p. 38; S115 p. 19]; (3) prefer what pricing absorbs (bounds on original variables, robust cuts whose duals enter arc costs) [S019 p. 27; S065 p. 5]; (4) enforce in the pricing domain only where pricing stays tractable, else as a master row [S007 manuscript p. 11]; (5) for non-robust cuts, separate the weak robust version first and lift only if still violated; roll back when pricing degrades [S077 pp. 57-58, 83]; (6) with aggregated identical blocks, branch on aggregated variables with a disaggregation certificate [S050 preprint pp. 4-6, 22-23] (§3.1 V4). Feeds the Routing row *How do I branch without breaking pricing?* and Workflow G step 4.

### Added in T3.6

- New heuristic (exclusivity fails, so not a method): one line and two cases in SKILL.md [S007 manuscript p. 11; D002 pp. 23–24; S077 pp. 57–58, 83]; fed into the Routing branching row, Workflow C step 3a, Workflow G step 4, the anti-pattern row [S019 pp. 27–28; S077 pp. 57–58], the quick-check and the Roundtable Card's first questions.

<a id="heuristic-12"></a>

## Heuristic 12: Diagnose column generation from the dual side before tuning it

> Changed in the T3.6 review fixes: see [Review fixes](#review-fixes).

### Full-text evidence (08 §4 and §5, copied)

| Cluster (merged by meaning) | Cards (full/part) | 1 Recurrence | 2 Say–do | 3 Executable, not standard | 4 Exclusivity | Result |
|---|---|---|---|---|---|---|
| Dual-side diagnosis | S027 S001 S002 S008 S032 S075 S076 S089, book (8 + book) | ✅ 2001-2026 | ✅ sole [S008 manuscript p. 6; S027 pp. 51, 84]; "The dual variables are the secret stars in the column generation algorithm. They determine which columns are generated and when we stop." [S088 p. 35] | ✅ | ⚠ the Montréal school's view; the book's timed evidence is borrowed from co-authors' studies [S088 pp. 40-41] | Heuristic H12 |

### H12 (new) · Diagnose column generation from the dual side before tuning it

**One line**: When column generation tails off or oscillates, read the behaviour through the duals (what the master's duals are doing, how good they are), measure the master/pricing time split, and pick the accelerator from that: dual seeding or boxes when the master dominates or its duals jump, pricing acceleration when pricing dominates.

**Cards**: the dual view as the organising idea of the thesis, the survey and the encyclopedia entry [S027 pp. 51, 84; S001 report pp. 2, 13, 15; S008 manuscript p. 6]; unstable duals that a static stabilization did not fix [S027 pp. 140, 142]; penalized dual boxes updated at each new best dual [S001 report pp. 21-22; S088 pp. 39, 51-52]; the box narrowed to a share of the gap when the bound improves [S032 manuscript p. 5]; smoothing with a mis-price check [S008 manuscript pp. 11-12; S088 pp. 55-56]; dual-optimal inequalities [S001 report p. 15; S008 manuscript p. 12; S088 pp. 36-37]; duals estimated without solving, from an aggregated single-depot problem or from removal and insertion savings, artificial penalties set as dual estimates [S088 pp. 52, 57-58]; the RMP share of time as the choice criterion, stabilization cutting total time by 89% where the RMP takes 75% [S088 pp. 41, 52, 58]; balancing master and pricing time as the stated guideline [S060 p. 17]; the master's share re-measured after each component to aim the next one [S075 p. 23; S076 pp. 28-29]; the share of time in pricing reported [S089 p. 27; S060 p. 27].

**Checks**: recurrence ✅; say–do ✅; executable ✅; exclusivity ⚠ (§4). → heuristic.

**Correction it carries**: Workflow G step 3's *stabilisation last* is an inferred order; the book ties stabilization to masters that are costly relative to pricing [S088 pp. 52, 58], and the 2010 entry puts it after profiling [S008 manuscript p. 14]. Replace *last* by *after the time split says the master or the duals are the problem*.

**Steps**: (1) profile: master time, pricing time, iterations, columns [S077 pp. 52-53; S027 p. 145]; (2) if the master dominates or the duals oscillate: seed duals (estimates, a subgradient start), box or smooth them, add dual-optimal inequalities [S088 pp. 31-32, 36-37, 52, 57-58]; (3) if pricing dominates: the pricing cascade of H1 [S060 pp. 17-18]; (4) re-measure the split after each component [S075 p. 23]; (5) accept a boxed master optimum only when the box variables are zero [S088 pp. 39, 43].

### Added in T3.6

- New heuristic (exclusivity partial): one line, the *secret stars* fragment [S088 p. 35] and the time-split evidence [S088 pp. 41, 52, 58; S075 p. 23]; it carries the Workflow G step 3 correction and feeds the Routing tailing-off row and Workflow C step 3.

<a id="heuristic-13"></a>

## Heuristic 13: Bring the exact IP to problems a neighbouring community knows only by theory or heuristics

> Changed in the T3.6 review fixes: see [Review fixes](#review-fixes).

### Full-text evidence (08 §4 and §5, copied)

| Cluster (merged by meaning) | Cards (full/part) | 1 Recurrence | 2 Say–do | 3 Executable, not standard | 4 Exclusivity | Result |
|---|---|---|---|---|---|---|
| Exact IP and computation where a community has only theory or heuristics; one LP for bound, rounding and exact solving | S030 S053 S041 S112 S046 S051 D001 S028 S065 S073 S068 (11) | ✅ 2004-2016, six projects | ⚠ stated only inside co-authored papers: "Last but not least we hope to increase the awareness in the computational geometry community towards tools from mathematical programming." [S041 manuscript p. 3]; [S053 pp. 2, 11; S065 p. 2] | ✅ | ⚠ shared with algorithm engineering | Heuristic H13 |

### H13 (new) · Bring the exact IP to problems a neighbouring community has studied only by theory or by heuristics

**One line**: Where a problem is known through complexity, approximation or extremal results, or through metaheuristics, write its exact IP, use the same LP for polynomial bounds, rounding and exact solving, compute optimal solutions, and test what the theory predicts on them.

**Cards**: stabbing numbers, "Most previous work on stabbing and crossing problems has focused on extremal properties, and little has been known about the computational complexity of actually finding structures of low stabbing number, or possible approximation algorithms." [D001 arXiv p. 2], one LP giving the bound, the rounding device and the exact solutions [S030 arXiv pp. 3, 8-12]; rectangle covers, "we are the first to introduce linear/integer programming techniques in this problem area" [S053 p. 2], the LP dual as a stronger lower bound and the route to primal-dual analysis [S053 pp. 4-9], the journal version testing the authors' conjecture on the class closest to refuting it [S041 manuscript pp. 13, 16]; permutation partitions, flow MIPs as the first exact approach with an approximation by rounding the same model [S112 pp. 4-5; S046 pp. 7-8; S051 pp. 7-8]; timetabling, optimal solutions in a field of metaheuristics [S028 pp. 1-3]; cut packing, "We are not aware of any experimental results, neither exact nor approximate, for cut packing; thus we provide the first computational study of the problem." [S065 p. 2], and the theory checked on the instances, "This comes as a surprise as there is a theoretical gap of a factor of 2 that we do not observe in the instances in our experiments." [S065 p. 10; S073 pp. 12-13]; a separation procedure that had no computational study, given its first full implementation [S068 pp. 1-2, 11].

**Checks**: recurrence ✅; say–do ⚠; executable ✅; exclusivity ⚠ (§4). → heuristic.

**Steps**: (1) find a problem whose literature is theory-only or heuristic-only and name what it lacks (exact solutions, computation) [D001 arXiv p. 2; S065 p. 2]; (2) write the exact IP and look at its LP solutions for structure [S053 pp. 4-5]; (3) take polynomial bounds and an approximation from the same LP [S030 arXiv pp. 8-12; S112 p. 5]; (4) compute optima on real and random instances and check the theory's predictions on them [S065 p. 10; S073 pp. 12-13]; (5) publish what computation suggests as conjectures, tested first on the class closest to refuting them (Method 2 exit B) [S041 manuscript p. 13].

### Added in T3.6

- New heuristic (say–do and exclusivity partial): one line, the dates 2003–2016, and three cases [D001 arXiv p. 2; S053 p. 2; S065 p. 10]; fed into the Routing row *Only theory or metaheuristics exist for this*, Workflow A step 2 and the trajectory's 2001–2009 row.

<a id="misreadings"></a>

## Common misreadings

> Changed in the T3.6 review fixes: see [Review fixes](#review-fixes).

### Full-text evidence (08 §3.3, copied)

Confirmed with pages (no change): Common Misreading 2 (own code with CPLEX and hMETIS; "Of course, at the moment, our work is not intended to produce a competitive tool, but to demonstrate that the direction is promising." [S015 preprint p. 27]); the SEA 2010 anatomy (temporal knapsack: SCIP solves 5 of 70, GCG 56 [S011 pp. 10-12]); the k-vertex-cut anatomy (73 newly closed instances [S089 p. 29]; integrality only on the natural variables [S089 p. 7]; verdict reopened [S089 p. 31]); Common Misreading 3 (limited efficacy reported [S074 manuscript p. 2]; branch-and-cut credited for large TSPs [S088 p. 71]); Common Misreading 1 [S005 p. 39; S006 pp. 82-83; S019 p. 40].

### Added in T3.6

- Misreading 2: + [S015 preprint p. 27]. Misreading 3: + [S074 manuscript p. 2] (the book's credit to branch-and-cut for large TSPs [S088 p. 71] stays here). Misreading 5: ✗ the certificate holds for short-term FIFO instances (C10); *Method 5 resolves it*. Misreading 1 is unchanged; the credit lists confirm it [S005 p. 39; S006 pp. 82–83; S019 p. 40].

### Before T3.6 (moved verbatim)

````text
## Common Misreadings

1. **"He designed and wrote GCG."** The design is Gerald Gamrath's (first commit 2008-11-25); the largest committers are Bergner, Puchert, Mühmer, Bastubbe and Witt; his commits are maintenance. The book: "Marco is the one with the vision who keeps it all together." (03 §0)
2. **"The 2015 paper showed GCG beating CPLEX."** It used an own code with CPLEX 12.2 and hMETIS, not GCG; the automatic choice was fastest on about 8% of 39 instances; "our work is not intended to produce a competitive tool" (01 §3.5).
3. **"A column-generation partisan."** He calls his view "personally biased" (TOP 2015); a 2021 paper reports limited efficacy of Benders cuts in pricing (DOI 10.1016/j.disopt.2021.100626); his 2024 slides call problem-specific cuts "indispensable".
4. **"An ML-for-MIP researcher."** Two papers (CPAIOR 2017; DOI 10.1287/ijoc.2021.1117), no trace in GCG, nothing after 2022, public scepticism in 2024 and 2026 (03 §6; 06 T11).
5. **"An exact-optimization purist."** The self-declared "fan" of exact optimization advises first of all not to solve pricing exactly; his group deployed a certified genetic algorithm (02 §4.4).
````

<a id="anatomy-sea2010"></a>

## Anatomy: Experiments with a Generic Dantzig-Wolfe Decomposition for Integer Programs (SEA 2010)

> Changed in the T3.6 review fixes: see [Review fixes](#review-fixes).

### Full-text evidence (card S011, batch c02, the published SEA text)

- The two passages the anatomy quotes from the Optimization Online preprint recur in the published text [S011 pp. 2, 4]; the design runs the original problem as the coordinating SCIP instance and the extended master inside a relaxation handler, inheriting SCIP's components, with branching and cuts on original variables [S011 pp. 4–8].
- Experiments: GCG 0.7, SCIP 1.2.0.5, CPLEX 12.1 as LP solver, two Core2 Quad machines, shifted geometric means; plain SCIP the only baseline; the temporal knapsack forced into blocks: 56 of 70 solved against 5 [S011 pp. 8–12] (08 §3.3, "Confirmed with pages").
- Sizing in the text: "It is to be expected that a tailor-made approach will outperform a generic one" [S011 p. 8]; limits: structure supplied by file, no stabilisation, column pool or Gomory basis; future work: detecting whether and how to decompose [S011 pp. 4, 8, 13].

### Added in T3.6

- Origin: + *published text [S011 p. 2]*; key insight: + [S011 pp. 4–5]; minimum evidence: + [S011 pp. 8–12]. No claim changed.

### Before T3.6 (moved verbatim)

````text
All co-authored: "the authors" unless a sole-voice source is given.

### Gamrath and Lübbecke, "Experiments with a Generic Dantzig-Wolfe Decomposition for Integer Programs" (SEA 2010, DOI 10.1007/978-3-642-13193-6_21)

| Dimension | Content |
|---|---|
| Origin | Generic codes were "started from scratch each time, at least in terms of standard MIP techniques like preprocessing and tree management" (Optimization Online 2010/03/2556 preprint, p. 2); the aim: decompose when promising, as solvers cut (01 SW2). |
| Why then | SCIP was an open framework with pricer plugins. |
| Key insight | Two synchronized SCIP instances: the original is "the primary one which coordinates the solving process", the extended one is "controlled by a relaxation handler" inside it (preprint p. 4); Gamrath's design. |
| Minimum evidence | Against SCIP 1.2.0.5: faster on capacitated p-median; 56 of 70 solved against 5 on a problem without block structure. |
| Abandoned paths | Transform-then-solve; structure still supplied by file. |
| Reception | The paper GCG asks users to cite. Outside verdicts on generic branch-and-price for general MIPs: "still in their infancy" (Chen, Günlük, Lodi 2025). |
| Methods | Method 1, Method 3 |
````

<a id="anatomy-ipco2011"></a>

## Anatomy: Partial Convexification of General MIPs (IPCO 2011) and Automatic Dantzig–Wolfe Reformulation (MP 2015)

> Changed in the T3.6 review fixes: see [Review fixes](#review-fixes).

### Full-text evidence (08 §3.3, copied)

| # | SKILL.md item | What the full texts show | Cards |
|---|---|---|---|
| C4 | Method 2 step 5: *four dropped in IPCO 2011; border area kept* | IPCO 2011 kept two measures (number of blocks, average integrality gap of the blocks); the border area is the 2015 paper's single kept proxy out of six | [S032 manuscript p. 8; S015 preprint pp. 12-21] |
| C19 | Signature Work Anatomy, IPCO 2011 and 2015, Minimum evidence: *Dynamic knapsack in minutes where CPLEX 12.2 hit the hour; better dual bounds than CPLEX's root on eight MIPLIB 2003 instances* | from the tables: CPLEX 12.2 reaches the one-hour limit on four of six knapsack instances and solves the other two; with k = 10 the reformulation plus branch-and-price solves all six within 362 s; the reformulation bound beats CPLEX's root bound with default cuts on seven of the eight selected MIPLIB 2003 instances (one tie) and on 13 of 24 in the appendix; the 2015 paper reports 12 (automatic choice) or 16 (best candidate) of 23 | [S032 manuscript pp. 7-8, 12; S015 preprint p. 30] |

### From the cards (S032, batch c03; S015, batch c04)

- The IPCO text lists the field's reservations and asks three questions of increasing ambition, the last of which the community answers in the negative [S032 manuscript pp. 1–2]; any matrix is forced into arrowhead form by hypergraph partitioning [S032 manuscript pp. 2–5]; the 2015 paper keeps original variables in the master and ranks candidates by relative border area [S015 preprint pp. 5–8, 16].
- Framing: "Of course, at the moment, our work is not intended to produce a competitive tool, but to provide a proof-of-concept and demonstrate that the direction is promising." [S032 manuscript p. 2]; limits written in the text: an inner approximation and a single-shot decomposition [S032 manuscript pp. 9–10]; a priori measure out of reach [S015 preprint pp. 27–28].

### Added in T3.6

- Origin: + [S032 manuscript pp. 1–2]; key insight: + [S032 manuscript pp. 2–5; S015 preprint p. 16]; ✗ minimum evidence rewritten from the tables (C19) [S032 manuscript pp. 7–8, 12; S015 preprint p. 30]; abandoned paths: *four quality measures dropped, two kept* [S032 manuscript pp. 6, 8] (C4). The sentence on Bastubbe, Lübbecke and Witt (SEA 2018) became its own anatomy ([below](#anatomy-sea2018)).

### Before T3.6 (moved verbatim)

````text
### Bergner et al., "Partial Convexification of General MIPs by Dantzig-Wolfe Reformulation" (IPCO 2011, DOI 10.1007/978-3-642-20807-2_4) and "Automatic Dantzig–Wolfe reformulation of mixed integer programs" (*Math. Program.* 149, 2015, DOI 10.1007/s10107-014-0761-5)

| Dimension | Content |
|---|---|
| Origin | The 2010 open question: do many MIPs benefit without known structure? The community leaned "no". |
| Why then | Hypergraph partitioning existed but was not combined with Dantzig-Wolfe for MIPs. |
| Key insight | Almost any matrix can be forced into bordered block-diagonal form; a cheap proxy ranks candidates. |
| Minimum evidence | Dynamic knapsack in minutes where CPLEX 12.2 hit the hour; better dual bounds than CPLEX's root on eight MIPLIB 2003 instances. |
| Abandoned paths | A third of MIPLIB 2003 set aside; four quality measures dropped; one correct decomposition per matrix. |
| Reception | Detection fragile, badly ranked; the average "mixed" (Basso and Ceselli 2022). |
| Methods | Method 3, Method 2 |

Bastubbe, Lübbecke, Witt, SEA 2018 (DOI 10.4230/LIPIcs.SEA.2018.11) is the evidence for Method 2; its anatomy is in 01-publications.md.
````

<a id="anatomy-survey"></a>

## Anatomy: Selected Topics in Column Generation (2005), with Branch-and-Price (2026)

### Full-text evidence (08 §2 Method 4, copied)

- **Strongest cards**:
  - Sole voice, 2001: the thesis chapter that carries the later survey's title, "Arguably, there are no new results in this chapter. Still, we are not aware of a comparable accumulation of various sources, enabling us to find better ways to relate things." [S027 p. 38], organised by the dual view [S027 pp. 51, 84], with the gaps named at section ends [S027 pp. 57-58, 73, 76-77, 84] and a bibliography meant to contribute in its own right [S027 p. 168]. Step 1 is visible: unstable duals in his own code that his static stabilization did not fix [S027 pp. 140, 142].
  - The survey and the primer: explanations and remedies of tailing off and dual oscillation in one notation, untested points written as such [S001 report pp. 2, 10, 18-22]; the primer's numbers checked by a third person [S002 pre-publication p. 27].
  - Survey as the origin of the generic solver, in his 2012 sole voice: collecting material for the primer is where the generic branch-and-price idea came from [S070 p. 5].
  - The degeneracy line (third author): two published methods unified in one notation give a new method and a theorem not explicit in the sources [S031 preprint pp. 2, 9-10, 14; S039 pp. 5, 7, 11-12]; "The original purpose of this work was a literature review preliminary to further researches, but we have come to see it as more than a summary." [S038 p. 19].
  - The book: one notation for convexification, discretization and their block variants with open questions published [S084 pp. 42-43, 64, 120]; corrections and credit (the Kantorovich attribution corrected with credit to Uchoa and Sadykov [S060 pp. 4, 49]; a PhD student's observation as a named proposition [S084 p. 112]; "In all our references, we list all the authors with all their first names, when we can." [S086 p. 57]); deferred subjects listed for later authors "by various authors hopefully following the notation introduced in this one" [D004 p. 8]; the unstable duals of 2001 get their systematic answer in the dual chapter [S088 pp. 39-58].

### Added in T3.6

- Origin: + the thesis chapter under the survey's title [S027 pp. 38, 51, 84]; key insight: + [S001 report pp. 2, 13, 15]; abandoned paths: *only the March 2004 report* was read (08 §1.2); reception: + the corrected attribution [S060 pp. 4, 49].

### Before T3.6 (moved verbatim)

````text
### Lübbecke and Desrosiers, "Selected Topics in Column Generation" (*Operations Research* 53(6), 2005, DOI 10.1287/opre.1050.0234), with *Branch-and-Price* (Springer 2026, DOI 10.1007/978-3-031-96917-1)

| Dimension | Content |
|---|---|
| Origin | Tailing-off and instability he could not fix in his thesis code; Desrosiers, the referee he asked for. |
| Why then | Dual-side material was not in textbooks; "The need for a standard text on column generation was more pressing than ever" (book p. xii). |
| Key insight | The dual view organises integer column generation in one notation. |
| Minimum evidence | Not applicable. |
| Abandoned paths | Classical Dantzig-Wolfe as an LP pricing scheme; the book's 2015–17 date and half its chapters. Survey version changes: not read. |
| Reception | His most cited work; one attribution corrected in 2026; no book review found. |
| Methods | Method 4 |
````

<a id="anatomy-kvertexcut"></a>

## Anatomy: Branch-and-price strikes back for the k-vertex cut problem (2026 preprint)

> Changed in the T3.6 review fixes: see [Review fixes](#review-fixes).

### Full-text evidence (08 §3.3, copied)

Confirmed with pages (no change): Common Misreading 2 (own code with CPLEX and hMETIS; "Of course, at the moment, our work is not intended to produce a competitive tool, but to demonstrate that the direction is promising." [S015 preprint p. 27]); the SEA 2010 anatomy (temporal knapsack: SCIP solves 5 of 70, GCG 56 [S011 pp. 10-12]); the k-vertex-cut anatomy (73 newly closed instances [S089 p. 29]; integrality only on the natural variables [S089 p. 7]; verdict reopened [S089 p. 31]); Common Misreading 3 (limited efficacy reported [S074 manuscript p. 2]; branch-and-cut credited for large TSPs [S088 p. 71]); Common Misreading 1 [S005 p. 39; S006 pp. 82-83; S019 p. 40].

### From the card (S089, batch c19, read as v2)

- "While results by Furini et al. (2020) suggest that branch-and-price was not the right technique for tackling the k-VCP, we demonstrate in an extensive numerical study that, when properly set up, the new branch-and-price substantially improves on the state of the art." [S089 p. 31].
- The formulation merges the natural binaries into the cluster-column model; the columns may stay continuous, so branching acts on the natural variables only and pricing stays a min cut [S089 pp. 7–8, 14–15, 19]; competitors re-run single-threaded for one hour with CPLEX 22.1.0, the gaps to published counts explained [S089 pp. 22–23, 27–28]; 73 newly closed instances [S089 p. 29]; losses listed in an appendix [S089 p. 42].

### Added in T3.6

- Origin: + [S089 p. 31]; key insight: + [S089 pp. 7, 19]; minimum evidence: + [S089 p. 29]. No claim changed.

### Before T3.6 (moved verbatim)

````text
### Ciccarelli, Furini, Hojny, Lübbecke, "Branch-and-price strikes back for the k-vertex cut problem" (arXiv:2602.04984, v2 2026-06-05; unreviewed)

| Dimension | Content |
|---|---|
| Origin | Earlier results (Furini et al. 2020) suggested branch-and-price was wrong here; a 2022 branch-and-cut beat a Lübbecke-group branch-and-price on a related problem (link [inferred]). |
| Why then | Not known. |
| Key insight | A stronger extended formulation; extended integrality relaxed, natural binaries added; branching that keeps pricing structure. |
| Minimum evidence | 73 previously open instances solved within one hour. |
| Abandoned paths | One of two symmetry approaches; CPLEX as LP solver (SoPlex for openness); v1's "consistently outperforms all competitors". |
| Reception | Unreviewed; Gurobi in preprocessing, restrictive licence (Tension 7; 03 C1). |
| Methods | Method 3, H5, Method 1 step 6 |
````

<a id="anatomy-coilcoating"></a>

## Anatomy: Integrated Sequencing and Scheduling in Coil Coating (Management Science 2011), with the 2009 Dagstuhl version (new)

### From the cards (S035, batch c03; D002, batch s03)

- Published as Höhn, König, Möhring, Lübbecke, *Management Science* 57(4):647–666 (2011), DOI 10.1287/mnsc.1100.1302; Lübbecke last of four. The 2009 version is *Sequencing and Scheduling in Coil Coating with Shuttles*, Dagstuhl Seminar Proceedings 09261, DOI 10.4230/dagsemproc.09261.26 (card D002).
- Entry through the plant and its software vendor: integrated sequencing and concurrent setup scheduling, a 180 s planning requirement, makespan as the accepted objective, almost no prior literature [S035 pp. 1–3, 11].
- Key idea: saving rectangles turn the fixed-sequence subproblem into a maximum-weight independent set in a 2-union graph; the exact dynamic program inspires an α-weighted heuristic inside a genetic algorithm; a bounded look-back relaxation solved by branch-and-price bounds the result [S035 pp. 5–14]. In 2009: a block-concatenation relaxation, valid under the FIFO tank rule [D002 pp. 9–24].
- Evidence: deployed at the plant, over 13% average makespan reduction against the planners; the IP bound within 10% of the FIFO-restricted optimum for short-term instances only, bound times not reported [S035 pp. 15–17]; in 2009, IP gaps of about 4–15% on nine instances [D002 pp. 25–26].
- Stated: "Assessing the quality of heuristic solutions is not only a theoretical contribution, but an important question in practice: How much optimization potential is left?" [S035 p. 13]; "Its implementation is not tuned to performance because we used it as a proof of concept only, so we do not report computation times for lower bounds (which were huge)." [S035 p. 15].
- Limits in the text: the optimum out of reach; no uniform α; the bound only for online tank rules and short subsequences, the tank-indexed IP intractable [S035 pp. 2, 4–5, 11, 14–16].
- Correction carried: 08 §3.3 C10 (the module in use since December 2009; whether the bound came before deployment is not stated) [S035 pp. 1, 13–14, 16–17].

### Added in T3.6

- New anatomy in SKILL.md (Method 5's signature work; framework §五 asks every core method for one): origin, key insight, minimum evidence, abandoned paths [S035 pp. 1–3, 5–17; D002 pp. 25–26]; *why then* and *reception* written as not stated or not researched.

<a id="anatomy-sea2018"></a>

## Anatomy: A Computational Investigation on the Strength of Dantzig-Wolfe Reformulations (SEA 2018), with the stable-set theory (new)

> Changed in the T3.6 review fixes: see [Review fixes](#review-fixes).

### From the cards (S058 and S052, batch c06; D006, batch s04)

- Published as Bastubbe, Lübbecke, Witt, SEA 2018, DOI 10.4230/LIPIcs.SEA.2018.11 (Bastubbe first author); the theory as Lübbecke, Witt, *Discrete Optimization* 30 (2018), DOI 10.1016/j.disopt.2018.07.001, read in its in-press version (card S052), and the 2015 manuscript by Witt and Lübbecke (card D006, DOI 10.13140/rg.2.1.3470.0887), which S058 cites as RWTH report 2015-029 (card S052).
- Entry: "Interestingly, this is already all we know about the strength of Dantzig-Wolfe reformulations of integer programs in general." [D006 p. 2]; strength theory was Geoffrion's result and their own stable-set result, nothing in between [S058 p. 2].
- Theory first: the 2015 manuscript characterises both extremes and announces experiments ("We will report on experiments in future work." [D006 p. 11]); the journal paper computes nothing and stresses "We stress that at this time, our work is not meant to imply any computationally viable solution procedure for the stable set problem." [S052 in-press p. 3].
- The computation: z_DW of all 2^|I| subsets by column generation on toy instances with at most 18 constraints, too-hard instances dropped [S058 pp. 2–3]; few distinct bounds and minimal reformulations; weak bounds frequent; textbook reformulations strongest for bin packing and knapsack [S058 pp. 4–9]; low-level gains predict average gains, so MIPLIB is measured at level 0, positive on 12 of 38 [S058 pp. 7–8]; random sampling rejected [S058 p. 6]; over one million relaxations, no hardware, LP solver or limit stated [S058 pp. 2–3] (C5).
- Limits and future work in the text: toy scale, objective dependence untested, MIPLIB only at level 0 [S058 pp. 3, 8–9, 11].

### Added in T3.6

- New anatomy in SKILL.md, replacing the pointer *its anatomy is in 01-publications.md* (the 01 note did not dissect it in full text; 01 §2.6 (b) has two sentences): origin, why then, key insight, minimum evidence, abandoned paths, methods [S058 pp. 2–8; D006 pp. 2, 11; S052 in-press p. 3].

### Moved from SKILL.md in the review fixes (verbatim)

SKILL.md keeps five anatomies (framework §五: three to five) and points here; Method 2 keeps the IPCO 2011 anatomy. The table as it stood in SKILL.md after the T3.6 edit:

````text
### Bastubbe, Lübbecke, Witt, "A Computational Investigation on the Strength of Dantzig-Wolfe Reformulations" (SEA 2018, DOI 10.4230/LIPIcs.SEA.2018.11), with the stable-set theory (2015 manuscript [D006]; *Discrete Optimization* 2018, DOI 10.1016/j.disopt.2018.07.001) (new)

| Dimension | Content |
|---|---|
| Origin | Strength theory was Geoffrion's result and their stable-set characterisation [S058 p. 2]. |
| Why then | The 2015 manuscript had settled both extremes [D006 p. 11]. |
| Key insight | Compute the bound of every subset of constraints to convexify on small models, read as a hierarchy of relaxations [S058 pp. 2–3]. |
| Minimum evidence | Over one million relaxations on 20 small instances: few distinct bounds, textbook choices strongest; 12 of 38 MIPLIB instances gain at level 0 [S058 pp. 3–8]. |
| Abandoned paths | Random sampling [S058 p. 6]; instances too hard to enumerate [S058 p. 3]. |
| Reception | Not researched; Bastubbe first author. |
| Methods | Method 2 (both exits), Method 3 step 6 [S052 in-press p. 3] |

([full evidence](references/research/09-evidence-ledger.md#anatomy-sea2018))
````

<a id="anti-patterns"></a>

## Research anti-patterns

> Changed in the T3.6 review fixes: see [Review fixes](#review-fixes).

### Full-text evidence (08 §3, copied)

- **V12 · Research Anti-patterns, LLM row.** The no-LLM statement is the book's (joint) and his posts'; two chair preprints of 2026 declare bounded assistance: "During the preparation of this work the authors used GitHub Copilot (GPT-5.4) and Anthropic Claude Opus 4.8 to support revision planning, improve wording and readability, and for updates to evaluation scripts used to generate manuscript figures and tables." [S115 p. 31], after a first manuscript and code written without the tools [S115 pp. 31-32]; LLM assistance for editing [S075 p. 28]. The row should say *in the book and his posts* and record the group practice.

- **Method 1 step 5 (mild, 2011)**: the IPCO study wrote its own very basic depth-first branch-and-price inside a tool built on CPLEX and hMETIS, called simple-minded in a table caption [S032 manuscript pp. 5, 7]. Later group code is built on frameworks [S050 preprint p. 11; S089 p. 22; S115 p. 22], and the 2026 paper attributes part of a competitor's gap to its hand-written tree [S089 p. 26].

| # | SKILL.md item | What the full texts show | Cards |
|---|---|---|---|
| C21 | Research Anti-patterns, LLM row | §3.1 V12 | [S115 pp. 31-32; S075 p. 28] |

### Added in T3.6

- Hand-written tree row: + [S089 p. 26] (part of a competitor's gap attributed to its hand-written depth-first tree).
- Two rows added: *A heuristic delivered without a bound, or a gap without its condition* → Method 5 [S008 manuscript p. 13; D002 p. 22]; *A branching rule or cut added without its effect on pricing* → H11 [S019 pp. 27–28; S077 pp. 57–58].
- LLM row (V12): ⚠ the group preprints' declared bounded assistance [S115 pp. 31–32] (also [S075 p. 28]); alternative + *declare any assistance*. The warning-signs row now reads B1–B4.

### Before T3.6 (moved verbatim)

````text
## Research Anti-patterns

| Anti-pattern | Why he opposes it (source) | Alternative |
|---|---|---|
| Hand-written branch-and-bound tree for branch-and-price | CO@Work 2020; podcast 2021; book p. 509 | A framework (Method 1 step 5) |
| Exact pricing from the start | CO@Work 2020, 1:33:12 | H1 |
| The warning signs B1–B3; a competition's definition taken as the problem, though it "may be quite far from timetabling reality" | Taste sources; TOP 2015, pp. 359–360 | Method 3, H3, Workflow A |
| Trusting a decomposition because it looks good | Book p. 237 (joint) | Measure its bound (Method 2) |
| LLM-generated text or images in research output | Bluesky 2025-09-04; book p. xv (joint) | Write it yourself |
````

<a id="trajectory"></a>

## Research trajectory

> Changed in the T3.6 review fixes: see [Review fixes](#review-fixes).

### Full-text evidence (08 §8 and §9, copied)

## 8. Trajectory as seen in the full texts

| Period | Main line in the full texts | Turn and its trigger | Representative cards |
|---|---|---|---|
| 1996-2001, TU Braunschweig | polyhedral enumeration (Diplom 1996, first journal paper 1998); group MIP applications; the switching-engine project and the thesis | from enumeration codes on CPLEX's library [S083 pp. 61-65] to column generation for a grant-funded industrial project [S027 p. 6] | S083, S020, S037, S063, S067, S027 |
| 2001-2008, TU Berlin | the survey and the primer with Desrosiers; exact IP brought into computational geometry and combinatorics (stabbing, rectangle covers, permutation partitions, stacking); rail, steel and cargo applications with certificates | the survey turns the thesis chapter into an agenda [S027 pp. 7, 37; S001 report p. 2]; the primer's vision of off-the-shelf column generation [S002 pre-publication p. 26] | S001, S002, S021, S030, S053, S112, S051, S034, S022, S023, S036, S028, D002 |
| 2009-2012, TU Darmstadt, RWTH from 2010 | generic Dantzig-Wolfe on SCIP; encyclopedia entries; partial convexification of general MIPs; applied branch-and-price | the generic idea traced to the primer's material [S070 p. 5]; general MIPs set aside for structured instances [S070 p. 5] | S011, S007, S008, S032, S070, S040, S035, S029, S010 |
| 2013-2018, RWTH | automatic DWR, learning when to decompose; theory and enumeration of DW strength; LP degeneracy with Gauthier and Desrosiers; cut packing and generic cuts in branch-and-price; energy, robotics and districting collaborations; suite reports | from automating the choice [S015; S009] to explaining it [D006; S052; S058] | S015, S009, S052, S058, S031, S039, S061, S044, S065, S068, S025, S080, S013, S005 |
| 2019-2023 | hypergraph separation; Benders cuts inside pricing; MIPLIB 2017; SCIP 8; ML-based similarity as fifth author | the tool's detection step made a research problem [S050 preprint p. 1]; a null result published [S074 manuscript p. 23] | S018, S050, S074, S003, S006, S014, S043, S091 |
| 2024-2026 | GCG 4.0 in SCIP 10; the book; chair preprints on tailored branch-price-and-cut and on Benders design | the book consolidates; tailored codes built directly on SCIP [S089 p. 22; S115 p. 22]; Benders on Gurobi [S075 p. 22; S076 p. 28] | S019, S077, S084, S088, S089, S115, S075, S076 |

Topics by five-year period (distinct works; read in full or in part in brackets):

| Topic | 1996-2000 | 2001-2005 | 2006-2010 | 2011-2015 | 2016-2020 | 2021-2026 | undated |
|---|---|---|---|---|---|---|---|
| Column generation, DW and branch-and-price method (theory, generic solver, components) | 0 | 4 (4) | 2 (1) | 10 (7) | 3 (3) | 0 | 3 (0) |
| Tailored column generation and branch-and-price for applications | 0 | 3 (3) | 4 (3) | 4 (4) | 4 (4) | 3 (3) | 0 |
| Combinatorics and polyhedra with IP (enumeration, complexity, approximation) | 3 (3) | 5 (5) | 6 (6) | 0 | 0 | 0 | 0 |
| Applied MIP and heuristics without decomposition | 3 (2) | 2 (2) | 3 (2) | 4 (1) | 6 (5) | 0 | 0 |
| LP degeneracy and network flow (Gauthier-Desrosiers line) | 0 | 0 | 0 | 3 (3) | 3 (3) | 0 | 0 |
| Solver suite and benchmark reports | 0 | 0 | 0 | 0 | 2 (2) | 5 (5) | 0 |
| ML for decomposition and MIP | 0 | 0 | 0 | 0 | 1 (1) | 1 (1) | 0 |
| Benders | 0 | 0 | 0 | 0 | 0 | 2 (2) | 0 |
| Robustness, MINLP and energy | 0 | 0 | 2 (1) | 0 | 3 (3) | 0 | 0 |
| Editorial, service, teaching | 0 | 0 | 3 (3) | 3 (1) | 2 (1) | 0 | 0 |
| The book (one work, eight chapters) | 0 | 0 | 0 | 0 | 0 | 8 (8) | 0 |

Assignment by card title and contribution: method S001 S002 S021 S033 S007 S008 S011 S032 S070 S015 S068 D006 S052 S058 S071 S045 S069 H001 S108 S114 S119 S120; applications S027 S024 S054 S023 S040 S026 S029 S065 S073 S050 S042 S089 S115 S035 D002 S106 S118 S074; combinatorics S083 S020 S063 S057 S030 D001 S053 S041 S112 S046 S051 S034 S066 S022; applied S037 S067 S082 S012 S036 S028 S010 S016 S018 S059 S080 S064 S100 S047 S078 S094 S102 S111; degeneracy S031 S039 S038 S049 S061 S044; reports S013 S005 S006 S014 S019 S090 S003; ML S009 S043; Benders S075 S076; robustness and energy S004 S110 S025 S055 S081; editorial S109 S107 D003 S091 S048 S056 S062 S072.

**Turns the full texts show**: (1) the combinatorics-with-IP line of 2003-2008 (fourteen works) ends with the move to Darmstadt and Aachen and is not in SKILL.md's trajectory (§5 H13); (2) the generic decomposition line comes out of the survey work [S070 p. 5] and is framed for non-experts from 2012 [S070 pp. 1, 7] to 2025 [S005 p. 29; S019 p. 26], while the probe framing is in print from 2021 [S006 pp. 76-77]; (3) the Dantzig-Wolfe strength work goes theory first (2015) and enumeration second (2018) [D006 p. 11; S058 p. 2]; (4) the 2026 chair preprints add Benders design [S075; S076] to tailored branch-price-and-cut [S089; S115].

**What stayed constant**: the compact model as the reference object [S027 p. 40; S084 p. 25]; heuristics inside an exact frame [S027 pp. 125, 133; S060 p. 17]; original variables for branching and cutting [S001 report p. 24; D004 p. 5]; claims framed as proofs of concept [S016 p. 2; S032 manuscript p. 2; S029 p. 6; S035 p. 15]; open questions published at the end [S020 p. 8; D004 p. 8]; code and data released [S020 p. 6; S012 report p. 9; S089 p. 23]; a framework rather than an own tree from the 1996 Diplom code on CPLEX's library on [S083 pp. 61-65; S012 report p. 9; S089 p. 22], with one exception [S032 manuscript p. 7].

## 9. Collaboration pattern

| Period | Works | Main coauthors (works in the period) | His position |
|---|---|---|---|
| 1996-2000 | 6 | Bussieck 4 (S020 S037 S063 S067), Zimmermann 2 (S067 S082), Lindner, Fink, Winter, Bernatzki | sole Diplom thesis (S083); corresponding author of his first journal paper [S020] |
| 2001-2005 | 14 | Zimmermann 4 (S024 S054 S036 S112), Desrosiers 3 (S001 S002 S021), Fekete and Meijer (S030), Bussieck and Lindner (S012), Villeneuve and Soumis (S021), Di Stefano and Krause (S112), Heinrich-Litan (S053), Epping and Hochstättler (S057) | three sole works (S027 S066 S033); first author with his advisor [S024; S054] and with Desrosiers [S001] |
| 2006-2010 | 20 | Möhring 6 (S022 D002 S004 S016 S106 S110), König 4 (S022 S034 D002 S106), Di Stefano, Krause and Zimmermann 2 (S046 S051), Liebchen and Stiller 2 (S004 S110), Höhn 2 (D002 S106), Schulz 2 (S016 S040), Felsner and Nešetřil 2 (editorials), Lach (S028), Gamrath (S011), Ceselli et al. (S023) | TU Berlin applications with Möhring's group; the first GCG paper, Gamrath first author [S011] |
| 2011-2015 | 24 | Desrosiers 5 (S007 H001 S031 S039 S038), Gauthier 4 (H001 S031 S039 S038), Bergner 3 (S032 S065 S015), Witt 3 (S065 D006 S068), the Bologna group 2 (S032 S015), Puchert 2 (S045 S069), Möhring 2 (S035 S059), Lach (S010), Hennig and Nygreen (S029), Coughlan and Schulz (S026) | three sole works (S008 S070 S048), the last sole texts; third author in the degeneracy line |
| 2016-2020 | 24 | Witt 5 (S073 S052 S058 S071 S118), Goderbauer 5 (S025 S055 S081 S080 S064), Koster, Bardow, Bahl and Voll 3 each (energy), Gauthier and Desrosiers 3 (S049 S061 S044), Brinker, Corves and Takeda 3 (robotics), Bastubbe 2 (S058 S050), Maher (S118), Kruber and Parmentier (S009), Möhring and E. Lübbecke (S018), Pardalos (S091); two suite reports | doctoral researchers first; first and corresponding author of the stable-set theory paper [S052] |
| 2021-2026 | 19 (book = 8) | Desrosiers, Desaulniers and Gauthier (the book), Donkiewicz and Gaul 2 (S075 S076), Mühmer, Ganz and Willamowski (S115), Ciccarelli, Furini and Hojny (S089), Maher and Witt (S074), the Buffalo group (S043); five suite or community reports | supervisor (CRediT [S075 p. 28; S115 p. 31]); last author [S089]; coordinator of GCG [S019 p. 40] |
| undated | 3 | Desrosiers and Gauthier (S119 S120), Mühmer and Uchoa (S114) | metadata only |

**Pattern**: (1) one 25-year line with Desrosiers, from co-referee of the thesis [S027 p. 1] and reader of the 2003 drafts [S024 p. 15] through the survey [S001] and the degeneracy line with Gauthier to the four-author book (H10); (2) a sequence of RWTH researchers who each lead one line of work as first or drafting author (Bergner [S032; S015], Witt [S071], Bastubbe [S058; S050], Goderbauer [S025; S080], Mühmer [S115], Gaul and Donkiewicz [S076; S075]), with one component per companion paper integrated into one code [S075 pp. 3-4, 28] (H9); (3) alphabetical author lists in several group papers [S016; S032; S073; S042], so position says little; (4) co-signing of large community reports from 2017 on, where his own section is identifiable at most as the RWTH group's [S013 p. 74; S006 pp. 82-83; S019 pp. 39-40]; (5) engineering and energy collaborations led by others, where his share is not identifiable [S078; S094; S025].

### Added in T3.6

- 1996–2001 row: polyhedral enumeration before column generation [S083; S020]. 2001–2009 row: the combinatorics-with-IP line (H13) [S030; S053]. 2008–2015 row: the generic idea from the primer's material [S070 p. 5]. 2011–2022 row: strength theory first [D006 p. 11]. 2024–2026 row: Benders design [S075; S076]. *Latest*: the four 2026 preprints, read in full [S089; S115; S075; S076].
- `06-trajectory.md` gained a section 10 with the full-text trajectory and collaboration pattern (from 08 §8–§9).

### Before T3.6 (moved verbatim)

````text
## Research Trajectory

| Period | Main direction | Why it turned | Representative work |
|---|---|---|---|
| 1996–2001 | Locomotive scheduling by column generation | A grant he was hired to write (Zimmermann) | Thesis |
| 2001–2009 | Survey; Montréal network; TU Berlin applications; SCIP's pricing | Thesis questions; North-American rejections; Möhring's group | 2005 survey; coil coating |
| 2008–2015 | Generic branch-and-price (GCG), structure detection | SCIP as open framework; RWTH chair from 2010 | SEA 2010; IPCO 2011; 2015 |
| 2011–2022 | Side lines: LP degeneracy, ML for decomposition choice, applications | Collaborators, students | CPAIOR 2017 |
| 2015–2026 | The book, GCG releases, teaching | Consolidation | the 2026 book |
| 2024–2026 | Tailored branch-price-and-cut directly on SCIP | [inferred] narrowed role of the generic solver | DOI 10.2139/ssrn.7177419; arXiv:2602.04984 |

### Latest

2025-11 to 2026-11: GCG 4.1.0 (Sep 2026), the open-access book, two preprints; no new position found (06 §8).
````

<a id="inner-tensions"></a>

## Inner tensions

> Changed in the T3.6 review fixes: see [Review fixes](#review-fixes).

### Full-text evidence (08 §2, §3.1 V13 and §3.3 C13, copied)

- **Increment dating (correction, §3.3 C1)**: the full texts do not show *since 2017 GCG is a first try and an estimate*. The 2012 sole voice frames the generic solver as needing no user input [S070 pp. 1, 7] but already names the reader who cannot tell whether a hand-built code is worth the effort [S070 p. 4]; in 2016 GCG is a competitor ("We conclude that at the current state of the art, it still considerably pays to consider a problem-specific implementation, even though generic solvers may become competitive soon." [S073 p. 14]); in 2017 it "supports users in employing Dantzig-Wolfe decomposition, even as a non-expert" [S013 p. 5]; in 2018 "It has always been GCG's ambition to not require the user to have any knowledge about problem or model structure or the decomposition algorithms to exploit such structure." [S005 p. 29]. The probe framing appears in print in 2021 and 2023 [S006 pp. 76-77; S014 arXiv p. 14] and in the book [S077 p. 67], while the generic framing continues: "For the user, no expertise in these techniques is needed" [S019 p. 26].

- **V13 · Inner Tension 7.** Commercial solvers carry the 2026 chair work [S075 p. 22; S076 p. 28; S115 pp. 22-23], while code and data go public [S089 p. 23] and GCG is under Apache 2.0 [S019 p. 26].

| # | SKILL.md item | What the full texts show | Cards |
|---|---|---|---|
| C13 | Tension 6: 2020 literature cuts *typically, don't help* against 2024 problem-specific cuts *indispensable* | a stable distinction rather than a turn: generic cuts on original variables against problem-specific ones already in 2010; problem-specific clique inequalities the largest ablation effect in 2014 and 2016; generic subproblem cuts null on textbook classes in 2021; the book judges every cut by what it does to pricing | [S007 manuscript p. 8; S065 p. 9; S073 p. 13; S074 manuscript pp. 2, 23-25; S077 pp. 9, 17, 57-58, 83] |

### Added in T3.6

- Tension 1: + 2016, tailoring *still considerably pays* [S073 p. 14] (fragment of the card's quote in 08 §2 Method 1).
- Tension 3: + *(Method 3 Say–do)*, where the 13 contradiction cards are counted.
- Tension 6: ✗ *a stable distinction, not a turn* [S007 manuscript p. 8; S065 p. 9] (C13; also [S073 p. 13; S074 manuscript pp. 2, 23–25; S077 pp. 9, 17, 57–58, 83]).
- Tension 7: + commercial solvers in the 2026 chair work and released code and data [S075 p. 22; S089 p. 23] (V13; also [S076 p. 28; S115 pp. 22–23; S019 p. 26]).

### Before T3.6 (moved verbatim)

````text
## Inner Tensions

- **Tension 1: generic against tailored.** "in principle, branch-and-price is a general method to solve general MILPs" (book p. 238), against tailored 2024–26 studies on SCIP and "may even be necessary" for tailoring (p. 509). (01 C2)
- **Tension 2: "without requiring any input" against documented failure.** GCG's docs promise to work "without requiring any input or knowledge from your side" [group]; the 2017 paper: it "may completely fail" on mismatched structure; an outside study did far better by supplying the linking constraints (05 C2).
- **Tension 3: honest sizing against headlines.** "stick to supported results" and proof-of-concept framing, against "globally better" next to 8%, the 2026 v1 abstract, the 2008 title.
- **Tension 4: stop or persist.** "Know when to stop", against "unless you are really going for something big, then never give up!", an 11-year book, an 18-year solver; he notes it himself (02 C1).
- **Tension 5: machine learning.** Interest (2017) against "machine learning is predicting the past" (2018) and the 2024–26 posts.
- **Tension 6: cuts after reformulation.** 2020: literature cuts "typically, don't help"; 2024: problem-specific cuts "indispensable".
- **Tension 7: open tools against practice.** "should not rather use our own tools" (2025) and an open-source goal, against Gurobi in teaching and preprocessing and a restrictive licence. Added after unsealing: the joint 2020 editorial says "The OR Forum is not an open access journal" and "We will not trade speed for quality", while weighing community-run options ("We believe in both.") (DOI 10.1007/s43069-020-0001-1, pp. 2–3).
- **Tension 8: structure against "unstructured".** In 2025: "(in fact, I am more interested in "unstructured")", unexplained.
````

<a id="roundtable-card"></a>

## Roundtable Card

> Changed in the T3.6 review fixes: see [Review fixes](#review-fixes).

### Full-text evidence (08 §3.3, copied)

| # | SKILL.md item | What the full texts show | Cards |
|---|---|---|---|
| C14 | How to Use *Weak at: numerics, tolerances, exact solving*; Honest Boundary *nothing on numerics, exact arithmetic*; Roundtable Card blind spot *no numerics, exact solving* | a sole-authored 2010 paragraph names the tolerances at the master-pricing interface (negative reduced cost, bound match, perturbation size 10^-3 to 10^-6), warns that testing against 0.0 loops, and takes a position: "An alternative is to resort to exact (rational) arithmetic; but due to performance reasons this is only advisable for mission critical linear and integer programs."; the book sets one tolerance for RMP and pricing and rounds columns at the pricing integrality tolerance; framework features that would invalidate a dual bound are switched off during pricing ("During branch-and-price we have to disable SCIP's preprocessing, cut generation, and propagation functionalities to ensure a correct dual bound."). There is no numerics study; *nothing on* becomes *a stated position, no study* | [S008 manuscript p. 13; S060 pp. 23-24, 48; S029 p. 10; S027 p. 136] |
| C15 | Roundtable Card, Gleixner: *numerics absent from this record* | the disagreement now has documented ground: exact rational arithmetic only for mission-critical programs [S008 manuscript p. 13] against exact solving as a certification default (the other side's position is not carded here) | [S008 manuscript p. 13] |
| C18 | Roundtable Card, Fischetti: *Benders projection against extended formulations* (inferred) | weakened: the group uses Benders projection itself and cites Fischetti, Ljubić and Sinnl 2017 as similar in spirit | [S076 p. 3] |

### Added in T3.6

- Leads when: + *a heuristic goes out without a bound*. First questions: + *What does this cut do to pricing?* (H11). Default recommendation: + *a delivered heuristic carries its gap and condition* (Method 5).
- Fischetti line: ✗ *weakened* [S076 p. 3] (C18): the group's 2026 preprint uses Benders projection itself and cites Fischetti, Ljubić and Sinnl 2017 (DOI 10.1287/mnsc.2016.2461) as similar in spirit.
- Gleixner line: ✗ *now with ground* [S008 manuscript p. 13] (C15): exact rational arithmetic is reserved for mission-critical programs in his 2010 sole-authored entry.
- Blind spots: *no numerics, exact solving or variability* → *numerics only a stated position, no study; no variability protocol in his group's studies* (C14, C7).

### Before T3.6 (moved verbatim)

````text
## Roundtable Card

- **Lens (one line)**: Is there structure worth reformulating, and how will we know before we build? Decomposition as a measured bet against the compact model, judged on instances chosen against it.
- **Leads when**: blocks with linking constraints, or a weak LP bound beside a well-solvable subproblem; "branch-and-price, Benders or branch-and-cut?"; column generation tails off or prices slowly; branching breaks pricing structure; a paper says decomposition "does not work"; an objective of penalty weights.
- **First questions asked**: What does a current solver do with the compact model? What is the pricing problem, and can you solve it well? Does the Dantzig-Wolfe root bound beat the solver's root bound after cuts? Where can the change show, and which set shows no harm? Baselines re-run? Interpretation or proof? Who owns the objective?
- **Default recommendation**: run the compact model; probe with known structure; if the bound gain is material and pricing has structure, build branch-price-and-cut on a framework (heuristic pricing first, exact for the proof, cuts where measured), components off by default; test on structured and adversarial sets, competitors re-run; a proof of concept unless the tables carry more.
- **Will push back on**: hand-written trees; decomposing structureless models; pricing as a generic MIP; random or tiny instances; borrowed numbers; "often", "consistently", "optimal" without counts or proof; summaries posing as conclusions.
- **Likely disagreements** ([inferred] from both sides' methods; no dispute documented):
  - *Achterberg*: defaults judged on broad sets (10.14279/depositonce-1634; 10.1287/ijoc.2018.0857), automatic Dantzig-Wolfe kept out (2023 interview, captions, https://www.youtube.com/watch?v=8bhIW27vCUQ), against generic Dantzig-Wolfe as a probe (10.1007/978-3-642-13193-6_21; 10.1007/s10107-014-0761-5).
  - *Fischetti*: many seeds per instance (10.1287/opre.2013.1231) against no seed protocol (10.1007/s10107-014-0761-5); Benders projection (10.1287/mnsc.2016.2461) against extended formulations.
  - *Gleixner*: numerically safe bounds (arXiv:2607.15837) against 73 open instances closed, numerics absent from this record (arXiv:2602.04984).
  - *Bixby* (guest): ideas count only inside solver defaults (10.1007/978-0-387-35514-6_2), against a stand-alone proof of concept (10.1007/s10107-014-0761-5). *Forrest* (guest): agrees on non-simplex pricing duals (10.4171/dms/1-3/65).
- **Blind spots**: generic branch-and-price not shown competitive on general MIPs; fragile detection; no outside benchmark of GCG 4.x; no numerics, exact solving or variability; long projects overrun; ML scepticism; slipped headline claims.
````

<a id="honest-boundary"></a>

## Honest Boundary

> Changed in the T3.6 review fixes: see [Review fixes](#review-fixes).

### Full-text evidence (08 §3.3 and §11, copied)

| # | SKILL.md item | What the full texts show | Cards |
|---|---|---|---|
| C14 | How to Use *Weak at: numerics, tolerances, exact solving*; Honest Boundary *nothing on numerics, exact arithmetic*; Roundtable Card blind spot *no numerics, exact solving* | a sole-authored 2010 paragraph names the tolerances at the master-pricing interface (negative reduced cost, bound match, perturbation size 10^-3 to 10^-6), warns that testing against 0.0 loops, and takes a position: "An alternative is to resort to exact (rational) arithmetic; but due to performance reasons this is only advisable for mission critical linear and integer programs."; the book sets one tolerance for RMP and pricing and rounds columns at the pricing integrality tolerance; framework features that would invalidate a dual bound are switched off during pricing ("During branch-and-price we have to disable SCIP's preprocessing, cut generation, and propagation functionalities to ensure a correct dual bound."). There is no numerics study; *nothing on* becomes *a stated position, no study* | [S008 manuscript p. 13; S060 pp. 23-24, 48; S029 p. 10; S027 p. 136] |
| C16 | Honest Boundary *Unread*: CPAIOR 2017 full text, the Primer, encyclopedia entries; *sole-authored SEA 2012 status report (paywalled) ... not read* | all now read: CPAIOR 2017 [S009], the Primer in a pre-publication copy [S002], both encyclopedia manuscripts [S007; S008], the 2012 status report [S070]; still unread: the published 2005 survey (only the March 2004 report [S001]) and the 2007 habilitation (not in INDEX) | [S009; S002; S007; S008; S070; S001] |

## 11. Open gaps

- **No open text** (22 works): read only at abstract level (S045 and S069 on primal heuristics for branch-and-price, H001 the GERAD precursor of S031, S100, S064, S056, S062, S072) or at metadata level (S082, S106, S059, S110, S111, S108, S114, S119, S120, and S102, which is not his). The primal-heuristics line inside GCG [S045; S069] and the VRPSolver engine inside GCG [S114] would bear on Tension 1 (generic against tailored) and are unknown beyond their abstracts or titles.
- **Versions**: the published 2005 survey is not read (only the March 2004 report [S001]); the printed encyclopedia texts, the IPCO LNCS text, the journal versions of S015, S043, S050 and S074, and the published primer were not compared with the versions read (§1.2).
- **The book's front matter** (preface, printed pp. xi-xv) has no card; SKILL.md's preface quotations rest on the research notes. All eight chapters are carded.
- **Not carded**: the 2007 habilitation (not in the index); the talks S079, S098, S099 and D005 (in the index as Role skip).
- **Individual share**: after 2015 no sole-authored text is among the carded works; CRediT statements [S075 p. 28; S115 p. 31] and suite credit lists [S013 p. 74; S006 pp. 82-83; S019 pp. 39-40] are the only attributions, so his own voice after 2015 rests on talks and posts outside the cards.
- **Open questions the cards could not settle**: whether the coil-coating bound preceded deployment [S035 pp. 1, 17]; whether the 2017 learned selector reached GCG (not rechecked [S009 p. 8]; GCG 4.0 ships scores without a learned ranker [S019 pp. 32-33]); whether the GCG probe was run before the 2024-2026 tailored studies (none reported [S089 pp. 30-31; S115 pp. 9, 11]); the four 2026 preprints are unreviewed [S075; S076; S089; S115].
- **Sealed material**: three holdout items stay out of this note; the one count they affect is noted in §2. They wait for the validation that unseals them.

### Added in T3.6

- **Full-text coverage** bullet (new): this member's `team_status.py --coverage` row and the remaining gaps (the 22 indexed rows without an open text, e.g. GCG's primal heuristics [S045; S069]; the book's front matter has no card, so its preface quotes rest on the research notes). The 22 rows (INDEX.md, Full text `no-oa`): seven read at abstract level (S045, S056, S062, S064, S072, S100, H001), ten at metadata level (S059, S069, S082, S106, S108, S110, S111, S114, S119, S120), S102 (a row that is not his work) and four talks with Role skip (S079, S098, S099, D005). 08 §11 lists S069 with the abstract-level works; its card is metadata level (08 §1.1).
- **His single voice**: ✗ the 2012 status report is now read [S070] (C16).
- **Field boundary**: ✗ *nothing on numerics, exact arithmetic* → *a stated position, no study* [S008 manuscript p. 13; S060 pp. 23–24] (C14).
- **Unread**: ✗ CPAIOR 2017, the Primer and the encyclopedia entries now read [S009; S002; S007; S008] (C16); still unread: the published 2005 survey and the 2007 habilitation.
- **Claimed but unverified**: the GCG pre-test (none reported [S089 pp. 30–31]; also [S115 pp. 9, 11]); learning the decomposition choice (once [S009]; GCG 4.0 ships scores without a learned ranker [S019 pp. 32–33]).
- **Research date** 2026-11-14 → 2026-11-28 (deep reading; web research 2026-11-08 to 14); the validation line gains *Not rerun after the deep reading.*
- **Corrections from the full texts** (new subsection): one line per correction; detail in [Corrections](#corrections).

### Before T3.6 (moved verbatim)

````text
## Honest Boundary

Distilled from public material, with these limits:
- **Tacit knowledge.** How he judges a direction is known only from formulaic thesis acknowledgments; no lab guide or developer account exists.
- **His single voice is thin after 2015.** Later research is co-authored and practice is group code; his sole-authored SEA 2012 status report (paywalled) and Twitter/X (his main channel 2009–c. 2022) were not read.
- **Quote quality.** Podcast and TEDx quotes are automatic captions; some taste criteria rest on short posts.
- **Era and resources.** 2010–2026 practice rests on a chair with many assistants, a cluster, SCIP and a Montréal collaboration.
- **Field boundary.** Decomposition for MILP only; nothing on numerics, exact arithmetic, parallel search or commercial model sets.
- **Critique coverage.** Outside benchmarks used GCG 3.0.x or earlier; 58% of critique sources are citation contexts.
- **Unread.** CPAIOR 2017 full text, the Primer, encyclopedia entries, the published 2005 survey (2004 preprint read), the 2007 habilitation.
- **Claimed but unverified** (stated only): "know when to stop" (contradicted by practice); "will you regret it?"; feedback by deliberate misunderstanding; "don't mix up" in papers; the GCG pre-test in his own tailored projects; learning the decomposition choice as standing practice; a to-do list of borrowed ideas; pre-registration (invited in 2020, no instance); restrained data reduction.
- **Sealed material.** Three primary items are held out for the increment test and are not in this skill; two items unsealed before the build appear, marked, under Inner Tensions and Mentor Voice.
- **Research date 2026-11-14.** He is living and active (GCG releases, preprints under review); later work is not covered. Update periodically, at least yearly or after a major release.
- Validation 2026-11-14: sealed-item test 5 with the skill / 6 without (3 items; 2 points or less is a tie); task test 8 supported and 0 fabricated grounds with the skill (on the version before the after-validation fixes of 2026-11-14; retention re-test after them: 6 of 6 pass); see [FIDELITY.md](FIDELITY.md).
````

<a id="corrections"></a>

## Corrections from the full texts

> Changed in the T3.6 review fixes: see [Review fixes](#review-fixes).

The full table of 08 §3.3, copied; SKILL.md's Corrections list gives one line per group and marks each corrected line inline, with ✗ in this pass and as *corrected from* since the review fixes (✗ is now kept for contradictions in his record). Where SKILL.md applies each row: C1 Method 1 Increment; C2 Workflow B checkpoint; C3 Method 1 stop rule and Variants; C4 Method 2 Variants, step 5 and the IPCO anatomy; C5 Method 2 Variants; C6 Method 2 Limitations; C7 Method 3 Variants and Limitations, Roundtable blind spots; C8 Method 3 Variants and *Different from standard practice*; C9 H1; C10 H2, G1, Method 5 Variants, Misreading 5; C11 H3; C12 H4; C13 Tension 6; C14 How to Use, Routing last row, Honest Boundary, Roundtable blind spots; C15 Roundtable Gleixner line; C16 Honest Boundary; C17 Routing Benders row; C18 Roundtable Fischetti line; C19 IPCO anatomy; C20 How to Use (nonlinear); C21 the LLM anti-pattern row. Activation Rules' *Nothing in the record* examples (C14, C17) stay unchanged at this stage ([How to Use](#how-to-use)).

### 3.3 Claims of SKILL.md that the full texts correct

| # | SKILL.md item | What the full texts show | Cards |
|---|---|---|---|
| C1 | Method 1 Increment: *since 2017 GCG is a first try and an estimate* | probe framing in print from 2021 (group) and 2023 (co-signed) and in the book; the generic framing persists to 2025; the 2012 sole voice already names the reader who needs a probe | [S070 pp. 1, 4, 7; S073 p. 14; S013 p. 5; S005 p. 29; S006 pp. 70, 76-77; S014 arXiv p. 14; S019 p. 26; S077 p. 67] |
| C2 | Workflow B checkpoint (a) *[inferred]* | practised in 2011 and 2015 | [S032 manuscript p. 8; S026 p. 7] |
| C3 | Method 1 stop rule | narrower than the record: go reasons beyond a bound gain; MILP pricing; nested decomposition | §3.1 V1-V2 |
| C4 | Method 2 step 5: *four dropped in IPCO 2011; border area kept* | IPCO 2011 kept two measures (number of blocks, average integrality gap of the blocks); the border area is the 2015 paper's single kept proxy out of six | [S032 manuscript p. 8; S015 preprint pp. 12-21] |
| C5 | Method 2 Practice: *over a million LPs in about 100 hours* | over one million relaxations, each solved by column generation, so the LP count is larger; no hardware, LP solver or limit stated | [S058 pp. 2-3] |
| C6 | Method 2 Limitations: *the 2018 study starts from a theorem* | the theorem dates to a 2015 manuscript | [D006 p. 11; S058 p. 2] |
| C7 | Method 3 Limitations: no seed or permutation protocol | true for studies he led; he co-signed such protocols; new noise devices | §2 Method 3 |
| C8 | Method 3 Different from standard practice | the two-set move is SCIP-community practice | [S006 p. 13; S019 pp. 4-7, 13] |
| C9 | H1: *monitor the Lagrangian dual bound, you get it for free* | free only in iterations where pricing is exact or a relaxation; heuristic pricing gives no valid bound | [S008 manuscript p. 3; S086 pp. 16-17; S088 p. 24; S060 p. 20] |
| C10 | H2 case: *a genetic algorithm certified within 10% by an IP, then deployed* | the certificate covers short-term instances with FIFO solutions against the FIFO-restricted optimum, on makespan; the module has been in use since December 2009 and the paper was received in March 2010; the text does not say whether the bound came before deployment; the 2009 workshop version states the FIFO condition of its bound | [S035 pp. 1, 13-14, 16-17; D002 pp. 21-22] |
| C11 | H3: *Practice visible only in abstracts and chair pages* | full-text practice: owners' scepticism, officers on patterns, feedback at every stage, constraints left out on purpose for a first prototype, planners validating plans, owner-set weights | [S027 pp. 28, 31, 137, 165-166; S054 manuscript pp. 10-11; S035 pp. 4, 14-15; D002 pp. 20, 24-25; S018 manuscript pp. 4, 24-25; S080 pp. 3-4, 8; S075 pp. 2, 26] |
| C12 | H4: *The link is [inferred]* | stated in his sole voice and in a joint paper | [S070 p. 6; S050 preprint p. 1] |
| C13 | Tension 6: 2020 literature cuts *typically, don't help* against 2024 problem-specific cuts *indispensable* | a stable distinction rather than a turn: generic cuts on original variables against problem-specific ones already in 2010; problem-specific clique inequalities the largest ablation effect in 2014 and 2016; generic subproblem cuts null on textbook classes in 2021; the book judges every cut by what it does to pricing | [S007 manuscript p. 8; S065 p. 9; S073 p. 13; S074 manuscript pp. 2, 23-25; S077 pp. 9, 17, 57-58, 83] |
| C14 | How to Use *Weak at: numerics, tolerances, exact solving*; Honest Boundary *nothing on numerics, exact arithmetic*; Roundtable Card blind spot *no numerics, exact solving* | a sole-authored 2010 paragraph names the tolerances at the master-pricing interface (negative reduced cost, bound match, perturbation size 10^-3 to 10^-6), warns that testing against 0.0 loops, and takes a position: "An alternative is to resort to exact (rational) arithmetic; but due to performance reasons this is only advisable for mission critical linear and integer programs."; the book sets one tolerance for RMP and pricing and rounds columns at the pricing integrality tolerance; framework features that would invalidate a dual bound are switched off during pricing ("During branch-and-price we have to disable SCIP's preprocessing, cut generation, and propagation functionalities to ensure a correct dual bound."). There is no numerics study; *nothing on* becomes *a stated position, no study* | [S008 manuscript p. 13; S060 pp. 23-24, 48; S029 p. 10; S027 p. 136] |
| C15 | Roundtable Card, Gleixner: *numerics absent from this record* | the disagreement now has documented ground: exact rational arithmetic only for mission-critical programs [S008 manuscript p. 13] against exact solving as a certification default (the other side's position is not carded here) | [S008 manuscript p. 13] |
| C16 | Honest Boundary *Unread*: CPAIOR 2017 full text, the Primer, encyclopedia entries; *sole-authored SEA 2012 status report (paywalled) ... not read* | all now read: CPAIOR 2017 [S009], the Primer in a pre-publication copy [S002], both encyclopedia manuscripts [S007; S008], the 2012 status report [S070]; still unread: the published 2005 survey (only the March 2004 report [S001]) and the 2007 habilitation (not in INDEX) | [S009; S002; S007; S008; S070; S001] |
| C17 | Routing row *Design my Benders decomposition* (*his one Benders paper puts Benders cuts inside pricing*); Activation Rules example *Benders design* under *Nothing in the record* | two 2026 chair preprints design Benders algorithms: a branch-and-Benders-cut for power grids along contingencies, with partial decomposition keeping the base case in the master [S075 pp. 2, 19, 22-23], and an exact, LP-free subproblem solver whose cuts are proved correct: "The efficiency of the subproblem solution algorithm remains a relatively underexplored subject in the Benders context, even though it can contribute significantly to overall running time." [S076 p. 2]. Both are unreviewed and in the group's voice | [S075; S076 pp. 2-4, 9-27] |
| C18 | Roundtable Card, Fischetti: *Benders projection against extended formulations* (inferred) | weakened: the group uses Benders projection itself and cites Fischetti, Ljubić and Sinnl 2017 as similar in spirit | [S076 p. 3] |
| C19 | Signature Work Anatomy, IPCO 2011 and 2015, Minimum evidence: *Dynamic knapsack in minutes where CPLEX 12.2 hit the hour; better dual bounds than CPLEX's root on eight MIPLIB 2003 instances* | from the tables: CPLEX 12.2 reaches the one-hour limit on four of six knapsack instances and solves the other two; with k = 10 the reformulation plus branch-and-price solves all six within 362 s; the reformulation bound beats CPLEX's root bound with default cuts on seven of the eight selected MIPLIB 2003 instances (one tie) and on 13 of 24 in the appendix; the 2015 paper reports 12 (automatic choice) or 16 (best candidate) of 23 | [S032 manuscript pp. 7-8, 12; S015 preprint p. 30] |
| C20 | Weak at *nonlinear optimization* (podcast) | a nuance: two co-authored MINLP application papers, one with his doctoral student, both reducing the nonlinearity to MILP machinery | [S012 report pp. 9-12; S025 preprint pp. 8-15] |
| C21 | Research Anti-patterns, LLM row | §3.1 V12 | [S115 pp. 31-32; S075 p. 28] |

Confirmed with pages (no change): Common Misreading 2 (own code with CPLEX and hMETIS; "Of course, at the moment, our work is not intended to produce a competitive tool, but to demonstrate that the direction is promising." [S015 preprint p. 27]); the SEA 2010 anatomy (temporal knapsack: SCIP solves 5 of 70, GCG 56 [S011 pp. 10-12]); the k-vertex-cut anatomy (73 newly closed instances [S089 p. 29]; integrality only on the natural variables [S089 p. 7]; verdict reopened [S089 p. 31]); Common Misreading 3 (limited efficacy reported [S074 manuscript p. 2]; branch-and-cut credited for large TSPs [S088 p. 71]); Common Misreading 1 [S005 p. 39; S006 pp. 82-83; S019 p. 40].

<a id="promotions"></a>

## Promotions, new heuristics and the candidate pool (08 §4–§6, copied)

## 4. Promotions

**One promotion: Method 5, *Certify what you deliver*.** The skill goes from four to five core methods. Clusters with three or more distinct cards read in full or in part, and the four checks:

| Cluster (merged by meaning) | Cards (full/part) | 1 Recurrence | 2 Say–do | 3 Executable, not standard | 4 Exclusivity | Result |
|---|---|---|---|---|---|---|
| Certify what you deliver: an exact relaxation bounds the heuristic | S012 S022 S030 S036 S051 D002 S035 S040 S010 S080 S018 S075 S033 S027, book (14 works plus the book) | ✅ 2001-2026, twelve projects | ✅ sole [S008 manuscript p. 13; S027 p. 127; S033 report p. 4]; joint [D002 p. 21; S022 p. 1] | ✅ | ✅ | **Promote: Method 5** |
| Pricing-compatibility as the filter for branching and cuts | S007 S065 S073 S050 D002 S035 S040 S026 S089 S115 S019, book (11 + book) | ✅ 2009-2026 | ✅ [S001 report p. 24; S008 manuscript p. 14; S077 pp. 9, 17] | ✅ | ✗ the shared core concern of branch-and-price design, which the book presents as the field's state [S077 pp. 17, 22, 38, 49-50, 94-95] | Heuristic H11 (§5) |
| Dual-side diagnosis | S027 S001 S002 S008 S032 S075 S076 S089, book (8 + book) | ✅ 2001-2026 | ✅ sole [S008 manuscript p. 6; S027 pp. 51, 84]; "The dual variables are the secret stars in the column generation algorithm. They determine which columns are generated and when we stop." [S088 p. 35] | ✅ | ⚠ the Montréal school's view; the book's timed evidence is borrowed from co-authors' studies [S088 pp. 40-41] | Heuristic H12 |
| Exact IP and computation where a community has only theory or heuristics; one LP for bound, rounding and exact solving | S030 S053 S041 S112 S046 S051 D001 S028 S065 S073 S068 (11) | ✅ 2004-2016, six projects | ⚠ stated only inside co-authored papers: "Last but not least we hope to increase the awareness in the computational geometry community towards tools from mathematical programming." [S041 manuscript p. 3]; [S053 pp. 2, 11; S065 p. 2] | ✅ | ⚠ shared with algorithm engineering | Heuristic H13 |
| Test sets built from one real case | S027 S036 S010 S028 S025 S055 S081 S065 S073 S075, stated in S091 (11) | ✅ 2001-2026 | ✅ "If proprietary data cannot be made public, authors should provide additional, synthetic data that support the result in the same way as the original data." [S091 p. 2]; "The only reason for using simulated data instead of the real instance, is that the database is severely inconsistent and incomplete [18]." [S028 p. 12] | ✅ | ✗ benchmark libraries from real data are common | Heuristic H14 |
| Design the delivered plan for the planner | S037 S027 S054 S036 S035 D002 S018 S080 S075 (9) | ✅ 1998-2026 | ✅ sole [S027 pp. 165-167]; joint [S054 manuscript p. 11; S037 p. 7] | ✅ | ⚠ practitioner folklore | H3 extension (§5.5) |
| Integrality only where needed | S036 S112 S028 S010 S089, book (5 + book) | ✅ 2005-2026 | ⚠ in-paper only [S089 p. 7; S087 p. 26] | ✅ | ✗ standard modelling | H5 refinement (§5.5) |
| Extremes first, then the family in between | D006/S052 S058 S061 S044, book (three lines) | ✅ three lines | ✅ via the 2025 keynote abstract SKILL.md cites; [S058 pp. 1-2] | ✅ | ✗ limiting cases are standard analysis | Method 2 variant (§3.1 V5) |
| Dual-bound fathoming inside the pricing DP | S027 S024 S054 S033, book citation | ✗ one project, 2001-2005; the book only cites it [S085 p. 18] | ✅ sole [S033 report pp. 2-4] | ✅ | ✗ completion bounds are standard now | H1 device (§5.5) |
| Report the ex-post best next to the rule | S016 S035 S015 S009 (4) | ✅ | ✗ no statement | ✅ | ✗ virtual best is standard | Method 2 step 5 evidence; rejected as heuristic (§10) |
| Later version as correction and sizing pass | S041 S046 S015 S031 S074 (5) | ✅ | ⚠ referee thanked for a more meaningful setup [S015 preprint p. 28] | ✅ | ✗ | H8 evidence (§5.5) |
| Hardness as licence; tractable subclass from practice | S034 S051 S046 D002 S004 S027 S066 (7) | ✅ | ⚠ in-paper [S051 p. 10; S046 p. 10] | ⚠ generic | ✗ | rejected (§10); the certificate part goes to Method 5 |
| Enter where the literature's assumption stops | S067 S066 S034 S032 (4) | ✅ | ✗ | ⚠ generic | ✗ | pool (§6) |
| DW reformulation as a proof device; harvest the pricing problem | S039 S038 S049 S068 (4) | ⚠ one line led by Gauthier and Desrosiers, Lübbecke third author, plus S068 | ✗ | ✅ | ✅ | pool (attribution); harvest part to H1 |

Why only one promotion: every other cluster fails exclusivity, and several also fail or only half pass say–do or recurrence; those that are executable are written as heuristics, which keeps their steps in the skill without inflating the method list, and three of them refine an existing item rather than add a new act (H3, H5, Method 2). No merger or replacement is needed, since the skill stays within 3-7 methods.

## 5. New heuristics and heuristic updates

The skill has ten heuristics; with H2 moving into Method 5 and four new ones the list would reach thirteen, above the framework's 5-10. Priority for the editor: H11 and H12 first (they fill the Routing rows on branching and on tailing-off), then H13, then H14, which could instead become a sub-step of Method 3 step 2.

## 6. Candidate pool (not promoted)

Counts are distinct cards that name the pattern among their new-pattern candidates (165 candidate entries on 78 card entries, 77 works), merged by meaning; *+* marks cards where the same move appears only in method links or techniques.

| Cluster | Cards | n | Decision |
|---|---|---|---|
| Certify what you deliver | S022, S035 (+S012, S030, S036, S051, D002, S040, S010, S080, S018, S075, S033, S027, S088) | 2 | Method 5 |
| Pricing-compatibility filter | S007, S050, S065, S077, S084, S085, S089, S115 (+D002, S035, S040, S073, S019) | 8 | H11 |
| Dual-side diagnosis | S001, S002, S060, S076, S086, S088 (+S027, S008, S032, S075, S089) | 6 | H12 |
| Exact IP where others have theory or heuristics; one LP, several uses | D001, D002, S028, S030, S035, S051, S053, S065, S068, S073, S112 (+S041, S046) | 11 | H13 (heuristic-from-exact-model part to §7.2) |
| Test sets from one real case | S010, S025, S027, S036, S091 (+S028, S055, S081, S065, S073, S075) | 5 | H14 |
| Plan for the planner; neutral decision support; owner's measure outside | S018, S023, S027, S037, S054, S064, S080, S115 (+S036, S035, D002, S075) | 8 | H3 extension |
| Integrality only where needed; exact projection | S010, S028, S036, S089, S112 | 5 | H5 refinement |
| Dual-bound fathoming in the pricing DP | S024, S027, S033, S054, S085 | 5 | H1 device |
| Extremes first, then in between; one-parameter families | D006, S044, S052, S058, S061, S085, S086 | 7 | Method 2 variant |
| Nested decomposition when pricing is a structured MIP | S019, S029, S115 | 3 | Method 1 stop-rule variant (§3.1 V2) |
| Name what the reformulation buys | S084, S085, S086, S078, S094 (+S075, S115, S026) | 5 | Method 1 stop-rule variant (§3.1 V1) |
| Turn the complicating feature into an advantage | H001, S031, S049, S026 | 4 | pool: two senses (degeneracy in the Gauthier line; calendars as a Method 1 step 3 case) |
| Later version as correction and sizing pass | S032, S041, S046, S118 | 4 | H8 evidence |
| Enter where the literature's assumption stops | S032, S034, S066, S067 | 4 | pool |
| Hardness as licence; tractable subclass shaped by practice; restrict and price the restriction | D002, S004, S027, S034, S051, S066 | 6 | rejected as heuristic (§10); the restriction-pricing device to §7.1 |
| Report the ex-post best next to the rule | S009, S015, S016, S035 | 4 | Method 2 step 5 |
| DW reformulation as proof device; harvest the pricing problem | S038, S039, S049, S068 | 4 | pool (attribution); harvest part to H1 |
| The generic solver as research instrument (pluggable pricers, structure files, host hooks, interfaces, tooling, credit maps, MIP toolkit carried into branch-and-price, tiered strong branching) | S006, S011, S013, S019, S050, S077 | 6 | Method 1 steps 4-5 and H9 evidence; §7.2 |
| The compact model behind the reformulation (reverse DW, column activation, constraint classes, grouping rules) | S005, S007, S021, S058, S084, S086 | 6 | Method 1 step 6 and Method 2 step 1 evidence; §7.1-7.2 |
| Numerics at the master-pricing interface | S008, S060 | 2 | correction C14 |
| Null result explained from the textbook model, then the predicted structure tested | S074, S118 (one project) | 2 | pool; §7.3 |
| Modelled is not solved | S010, S048 | 2 | proposed taste warning B4 |
| Ranked answers when the code fails | S007, S008 | 2 | Workflow G evidence (§2.5) |
| Column selection and start (diversity, trivial start columns, Farkas pricing by a heuristic, bounds for any dual vector) | S023, S050, S060, S087, S115 | 5 | H1 evidence; §7.2 |
| Isolate the effect (control arm, baseline with the same components, budget parity) | S010, S089, S115 | 3 | Method 3 step 3 |
| Reporting devices (expectation then observation, conventions behind counts, a metric ruled out by its degenerate extreme, vision as a log line, one running example) | S002, S011, S015, S050, S087 | 5 | §7.4 |
| Counterexamples and audits (minimal counterexample, audit the refutation, impurity audit of a library) | S021, S043, S063 | 3 | §7.1, §7.3 |
| Single-card techniques (cross-model guidance, puzzle as test, ladder of models, scenario vertices, robustify by adding, explanations for conflict analysis, discretize-fix-repair, asymmetric-risk gate, combinatorics then geometry, decode to the owner's objects, LP-free subproblems, factorization reuse, return arc, dualized follower) | S004, S009, S012, S016, S018, S022, S023, S025, S060, S076, S086, S089 | 12 | §7 only |
| Benchmark selection by optimization; distribute raw, measure presolved | S003 (co-signed, ZIB-led) | 1 | not his method (§10) |
| Declared bounded LLM assistance | S115 | 1 | anti-pattern variant (§3.1 V12) |

**Decision in T3.6**: Method 5 promoted as 08 proposes. H11, H12 and H13 enter as heuristics in 08's priority order; H14 becomes Method 3 step 2a (the alternative 08 names), so that SKILL.md has thirteen heuristic labels, H2 among them as a pointer. The H3, H5, H8, H1 and Method 2 and 3 updates of 08 §5.5 are written into the existing items; B4 enters as a warning sign.

<a id="rejected"></a>

## Rejected updates (08 §10, copied)

## 10. Rejected updates

1. **Hardness as licence for the method** as a heuristic: proving hardness and then justifying a large MIP or a heuristic is standard practice; "Theoretical hardness legitimates studying and applying computationally expensive approaches like solving (probably large scale) mixed integer programs." [S051 p. 10; S046 p. 10; S034 p. 11; D002 p. 3]. The certificate half goes to Method 5.
2. **Report the ex-post best next to the rule** as a heuristic: virtual-best reporting is standard; kept as Method 2 step 5 evidence [S016 p. 4; S015 preprint p. 22].
3. **Trivially feasible start columns, Farkas pricing** as a heuristic: textbook devices; §7.2 D9 [S023 p. 10; S008 manuscript pp. 6-7].
4. **Carry the MIP solver's toolkit into branch-and-price** as a heuristic: it is the generic-solver programme itself, already Method 1 step 5 and H9 [S050 preprint pp. 7-10, 17; S077 pp. 23, 44, 59, 63; S006 pp. 72-74].
5. **Dual-bound fathoming** as a separate heuristic: one project and now standard; folded into H1 [S085 p. 18].
6. **Expectation, then observation** as a heuristic: two works with different first authors; a reporting move, §7.3 E12.
7. **Master equalities relaxed to covering inequalities**: a standard relaxation; §7.2 D3.
8. **DW reformulation as a proof device** as a heuristic of his: one line led by Gauthier and Desrosiers with Lübbecke third author [S039; S038; S049]; the book carries it [S086 pp. 28-33]. Pool.
9. **Turn the complicating feature into an advantage**: two different senses, neither his alone (§6).
10. **Extremes first, then in between** as a heuristic: its general form adds little beyond Method 2; the order is recorded as a Method 2 variant (§3.1 V5).
11. **Benchmark selection by optimization; distribute raw, measure presolved**: co-signed MIPLIB methodology led by ZIB [S003 pp. 12-14, 24-36]; not his method.
12. **Neutral decision support for a public client** as a separate heuristic: one project [S080; S064]; folded into the H3 extension.
13. **Reading notes on internal consistency** (numbers, captions, text against tables, results across versions): not findings about the researcher; one neutral lesson (§7.4 W11).
14. **Upgrading *Weak at: nonlinear optimization* to a strength**: the MINLP papers are co-authored applications that reduce the nonlinearity to MILP machinery [S012 report pp. 9-12; S025 preprint pp. 8-15]; a nuance only (§3.3 C20).
15. **A heuristic from the *design for planner acceptance* cluster as a whole**: it duplicates H3's scope; written as an H3 extension.

<a id="review-fixes"></a>

## Review fixes (T3.6 fix round, 2026-11-28)

Three read-only reviewers (fidelity, rules, usefulness) checked the T3.6 edit. Each fix below was checked against the full texts or the cards before it was applied. Old SKILL.md wording is in italics or, where it moved verbatim, in the fenced block at the end of this section.

**Sealed material and pointers**
- SKILL.md no longer links `07-paper-cards.md` (its S027 row, built from the b01 digest, states a sealed point) or research notes 01, 03, 05 and 06 (they hold passages that `holdout.md` lists); 08 no longer links 07. The 13 body pointers into those notes were replaced by card citations or primary sources: Method 2 checkpoint and Misreading 4 (*03 §6*) → the GCG search of 2026-11-08 [group] and [S019 pp. 32–33]; Method 4 step 6 (*05 §6*) → [S060 pp. 4, 49]; Workflow C step 4 (*03 §1.4.2*) → [S089 pp. 21, 23]; Workflow F (*05 §2.3*) → the web research of 2026-11-08 to 14; H8 (*01 §1.6*) → the carded pairs (08 §5.5) and the SEA papers [S011; S070; S065; S068; S058]; Misreading 1 (*03 §0*) → book p. 538; Misreading 2 (*01 §3.5*) → [S015 preprint p. 27]; SEA 2010 anatomy (*01 SW2*) → [S011 p. 1]; k-vertex-cut anatomy (*03 C1*) → the code repository's README and LICENSE, read 2026-11-08; Latest (*06 §8*) → the web research and the four preprints; Tension 1 (*01 C2*) dropped, the book pages stand; Tension 2 (*05 C2*) → Yıldız, Boland, Savelsbergh 2022.
- The Sources appendix names the files not to open: notes 01, 03, 05, 06, `07-paper-cards.md`, `holdout.md` and the batch files b01, c01 and s01. The other batches are usable; they are the Answer Standard's *paper cards*. The Honest Boundary names `FIDELITY.md` without a link, since the report discusses the sealed items (not a reviewer finding; the same rule).
- Page citations narrowed where the cited page also carries a sealed sentence and another page carries the claim: [S027 pp. 139–140, 142] → [S027 pp. 140, 142]; [S024 pp. 9–11] → [S024 p. 10] (catalog DM1, 08 §2.5 and §7.2); [S027 pp. 131, 149] → [S027 p. 149] (08 §2); [S027 pp. 137, 141] → [S027 p. 137] (SKILL.md Method 3 step 2a, catalog EP5). Workflow G step 5 cites the sole-voice [S008 manuscript p. 14] instead of [S007 manuscript p. 14].

**Facts corrected against the texts**
- Method 1 Say–do: step 4 is said in the CO@Work 2020 lecture (1:35:41, captions; note 02 R11) and in print from 2021 [S006 pp. 76–77; S014 arXiv p. 14], seeded in 2012 [S070 p. 4] (was *stated from 2021*). Step 2 is ✅ in the algorithmic papers and skipped where the extended formulation is the field's state of the art [S085 p. 10] or branch-and-price only bounds a heuristic [S035 pp. 13–15] (08 §2). The Increment line adds that the generic framing persists to 2025 [S019 p. 26] (08 C1).
- Method 3: S070 states a success and failure criterion in a talk that also reports results and follows the IPCO 2011 proof of concept [S070 pp. 5, 7]. *The success criterion written before any result*, *the criterion fixed in advance* and *before the first run* are removed from SKILL.md, the catalog (EP1), 08 (§2, §7.3 E1), this ledger and 06 §10.4.
- Method 4 variant: S075 p. 3 is the collected-constraints item, not an extremes construction; the extremes rest on [S061 pp. 1, 9, 17; S044 pp. 1–2, 10, 14] (08 V9).
- Method 2 Practice: *conjectures from enumerated tiny instances since 1998 [S020 pp. 5–8; S063 pp. 1–3]* is split into a counterexample found by vertex enumeration [S063 pp. 1–2] and one class proved, the general case left as a conjecture [S020 pp. 7–8].
- H1: dated to the 2001 thesis [S027 pp. 125, 133–135] (was *In print since 2003*).
- IPCO 2011 anatomy: *the reformulation solved all six within 362 s* holds with k = 10 [S032 manuscript p. 7]; the appendix count, 13 of 24 [S032 manuscript p. 12], and the 2015 counts, 12 of 23 with the automatic choice and 16 with the best candidate [S015 preprint pp. 24, 30], are added.
- B4 (now inside B2): five ITC2007 comp instances at 70–99% after an hour, the four test instances within 6% [S010 p. 14] (was *70–99% gaps [S010 pp. 8–9, 14]*).
- Page precision: S035's *short-term* certificate and *since December 2009* are on pp. 16–17 (H2, Corrections, 06 §10.4); the IPCO tool's depth-first tree is on [S032 manuscript pp. 6–7]; the hard-instance set is introduced on [S027 p. 137]; the 2015 counts are on [S015 preprint pp. 24, 30]. One reviewer page claim was not taken: the S074 null-result sentence used for sizing is on p. 23 (card S074, verified quote), so [S074 manuscript p. 23] stays.
- Method 5 Say–do: the sole-voice statement is [S008 manuscript p. 13]; [S033 report p. 4], a pricing heuristic with a proven relative error, moved to Practice; the card counts are replaced by 08 §4's (14 works plus the book; one contradiction [S025 preprint p. 21]).
- Method 1 variant: *Cheapest probe* became *a cheaper probe [inferred from S088 pp. 17, 31]* (the book calls the subgradient algorithm a heuristic for the Lagrangian dual, p. 31). H12's [S075 p. 23] is labelled as the group's Benders use of the time split.
- Method 3 Say–do: the 13 contradiction cards are described as claim-sizing records in co-authored texts (08 §2), not as his headlines.

**Method 5 exclusivity**: check 4 is rewritten in 08 §4 and #method-5 on carded specifics: an exact relaxation built only for the certificate, its condition stated, its master seeded with the heuristic's columns, brute-force pricing and unreported bound times [S035 pp. 13–15; D002 pp. 21–25], in three fields whose prior work was heuristic only [S022 p. 3; S035 p. 2; S080 p. 2]. Check 3's unsourced sentence on heuristic-dominated fields is removed. SKILL.md's *Different from standard practice* follows and names the coil-coating team.

**Voices**: new quotes from joint texts carry their label: G4 [S028 p. 2] (joint), Method 5 step 3 [D002 p. 22] (joint), H3 [S054 manuscript p. 11] (joint), H5 [S087 p. 26] (book, joint), H12 [S088 p. 35] (book, joint), Tension 1 [S073 p. 14] (joint); Workflow G step 5 paraphrases the sole-voice S008 page. Method 1's yardstick line credits *the book and the group's algorithmic papers* (was *he keeps*); Misreading 5 and Method 5 name the coil-coating project and its four authors (was *his group deployed*).

**Marks**: SKILL.md defines ✅, ⚠ and ✗ once (How to Use) and keeps ✗ for contradictions in his record (G1, B2, Method 1 step 5, Method 5's MINLP case). Corrections of its own earlier wording read *corrected from* + the old wording in italics, in place: Weak at, Blind spots, the Workflow G heading, Method 3 Limitations, Method 2 step 5 and Variants, Workflow B (a), Workflow G step 3, H2, H3, H4, Misreading 5, Tension 6, the IPCO anatomy, the Gleixner line, the Routing rows on Benders and numerics, Honest Boundary. Status marks (*✗ dated*, *✗ weakened*, *✗ now with ground*, *✗ Now read*) became plain words.

**Additions from 08 and the cards (usefulness review)**
- Method 1: probe the known structure next to detected alternatives, since the canonical decomposition was the worst of 75 in the one practised probe [S042 pp. 10, 12, 17–18] (the S042 card's Method 1 variant link); step 2, the published branch-price-and-cut as yardstick where the extended formulation is the standard [inferred from S085 p. 10]; the Roundtable default likewise.
- Identical blocks (08 V4 and H11 step 6): Workflow C step 3a, Method 1 step 6 and Workflow G step 4 [S077 pp. 22, 27–28; S050 preprint pp. 4–6, 22–23] (DM4, PD13).
- H1 tests [S008 manuscript pp. 3, 6] and diverse columns [S060 pp. 15–16, 41–42; S050 preprint p. 9] (08 §5.5 (c)); H12's sizing [S088 p. 52] and its ⚠ (08 §4); catalog DM10 (smoothing rule [S088 p. 55], misprice bound [S008 manuscript pp. 11–12]), new DM20 (Lagrangian stopping tests) and DM21 (cuts and bounds harvested from pricing [S068 pp. 7–8], 08 §5.5 (e)).
- Numerics: its own Routing row and Workflow C step 1 (DM17) [S008 manuscript p. 13; S060 pp. 23–24]. Benders: the Routing row (DM12, EP9) and a Benders line in Workflow B's checkpoint [S075 pp. 2, 23; S076 pp. 28–29], with the projection argument marked [inferred].
- Method 5 step 2: the exact IP's own LP [S030 arXiv pp. 10–11; S053 pp. 3–4] and the compact MIP on sub-instances [S018 manuscript p. 28] (08 §4 step 2); the Routing heuristic row points to it.
- Method 2 step 3: structured candidates, not random subsets [S015 preprint pp. 8, 11–12; S058 p. 6].

**Counts and structure**: H11 and H13 keep their labels but carry their steps in Workflow C step 3a and Workflow A step 2, so ten heuristics stay in working form (framework §三: 5–10); B4 is folded into B2 (taste criteria: eight; framework §四: 5–8); the SEA 2018 anatomy moved to #anatomy-sea2018 (five anatomies; framework §五: 3–5). Card-count tuples left the Say–do lines (block below). Duplicated corrections were cut from the Method 2 and Method 3 Variants; they stand in Method 2 step 5 and in Method 3's *Different from standard practice* and *Limitations*. S032 is cited as [S032 manuscript p. N] everywhere (a preprint; LNCS pages not mapped). The disclaimer line names the 17 abstract- or metadata-level works and the 7 skipped (`team_status.py --coverage`). RESOURCES.md rows 12, 30, 31, 33, 51 and 77 got T3.6 notes.

**Changed after the fix round, by the operator's hand edit (2026-11-28)**: Activation Rules' *Nothing in the record* line drops numerics and Benders design from its examples (How to Use, *Two dated examples*, and the last Corrections line record it). **Not changed**: the Roundtable Card's First questions (the roundtable reads the first two; the rest are lens-specific); the coil-coating anatomy's *Not stated* and *Not researched* rows (framework §五's dimensions, answered honestly).

Moved verbatim from SKILL.md (as it stood after the T3.6 edit):

````text
Method 1 Say–do: ✅ stated + practised for steps 1–3, 5, 6 (cards 51 / 41 / 1; 59 works); ⚠ step 4 stated from 2021, not shown before his tailored studies [S089 pp. 30–31].
Method 2 Say–do: cards 23 / 21 / 0, 33 works.
Method 2 Variants: ✗ IPCO 2011 kept two measures; the border area is the 2015 proxy [S032 p. 8; S015 preprint pp. 12–21]. / ✗ Not "a million LPs": over one million relaxations, each by column generation [S058 pp. 2–3].
Method 3 Say–do: cards 60 / 60 / 13; 76 works; ⚠ step 6 mixed: the 13 contradictions are headlines the tables do not carry, careful sizing beside them in every period [S010 p. 1; S074 manuscript p. 23].
Method 3 Variants: ✗ The two-set move is SCIP-community practice [S006 p. 13; S019 pp. 4–7]. / ✗ No seed protocol only in his group's studies [S065 p. 6]; co-signed suite reports use seeds [S013 pp. 14, 70–71].
Method 4 Say–do: cards 21 / 14 / 0, 26 works.
Method 5 Say–do: ✅ stated (sole [S033 report p. 4]; joint [D002 p. 21]) + practised in eleven projects, 2004–2026 (cards 14 / 1 / 1).
B4: Modelled is not solved (new). Writing an extension down does not handle it [S048 p. 3]; his group's timetabling extensions were left with 70–99% gaps [S010 pp. 8–9, 14].
H11 (new): Write its effect on pricing first (a bound change, a new resource, a dual of uncertain sign, a broken dominance); keep what pricing absorbs, put the rest in the master or drop it, roll cuts back when pricing degrades. Cases: branching as bound changes inside pricing [S007 manuscript p. 11; D002 pp. 23–24]; cuts raised only while pricing bears them [S077 pp. 57–58, 83]. Not exclusive.
H13 (new): Write the exact IP, take bounds, rounding and exact solutions from its LP, compute optima, test the theory's predictions on them (2003–2016).
Workflow G step 5: Effect persists unexplained: Workflow F, as an open question, not a tuning target: "The most honorable answer to that is: Research your problem!" [S007 manuscript p. 14].
````

<a id="held-back"></a>

## Held back under the holdout rule

Under the rule of `holdout.md`, candidate points that lean on sealed items are named only in the stage report, never here, in SKILL.md or in the catalog; they wait for the validation that unseals them. Recorded here, so that a later step does not reintroduce sealed material unawares:
- 08 itself holds back one Method 2 evidence link (08 §2) and one sub-point of the H3 extension (08 §5.5); neither is used.
- The S027 row of `07-paper-cards.md` (built from a digest's contribution field) and the bodies of the batch files b01, c01 and s01 carry sealed points; SKILL.md tells its reader not to open them while using or testing the skill. Editing those digests and regenerating 07 is outside this stage.
- Review fixes (2026-11-28): SKILL.md links neither 07 nor notes 01, 03, 05 and 06, and 08 no longer links 07; page citations were narrowed where the cited page also carries a sealed sentence ([Review fixes](#review-fixes)).
- Still open, for the operator: (1) the b01 digest's contribution field feeds the S027 row of 07 and states a sealed decision: edit it and rerun `build_card_index.py` before 07 is linked again (a digest edit is outside this stage). (2) Notes 01, 03, 05 and 06 keep the passages that `holdout.md` lists; whether they move under their items in `holdout.md` is the operator's decision. (3) Three cited pages still carry a sealed sentence or the held-back deployment sub-point, because the cited claim has no other page: [S027 p. 168] (the bibliography claim, 08 §2 and #method-4), [S024 p. 9] (the column-selection quote, 08 §5.5 and #heuristic-1) and [S054 manuscript p. 11] (the planner quote, SKILL.md H3). (4) Activation Rules' example *numerics, Benders design* stays as written (protected at this stage).

<a id="card-key"></a>

## Card key

> Changed in the T3.6 review fixes: see [Review fixes](#review-fixes).

One row per card entry (111 entries on 110 works; S030 has an abstract card from round 1 and a full card from round 3). *Work* and *Published as* come from `../sources/publications/works.json`; *Read* is the card's read level; *Batch* is the batch file under `cards/` (b01, c01 and s01 hold sealed passages and are not to be opened while using or testing the skill; the other batches hold none); *Version read* names the version a card read when it is not the indexed published text, with the word that SKILL.md and this ledger put in citations (from 08 §1.2). The book's eight chapters (S060, S077, S084–S088, D004) are parts of *Branch-and-Price* (S017, Role skip, DOI 10.1007/978-3-031-96917-1).

| Card | Year | Work | Published as (works.json) | Read | Batch | Version read and citation word |
|---|---|---|---|---|---|---|
| S001 | 2005 | Selected topics in column generation | Operations Research 53 (6), 1007-1023; DOI 10.1287/opre.1050.0234 | full | `c01` | TU Berlin report 2004/08, revised March 2004 (not the journal text) [report] |
| S002 | 2005 | A primer in column generation | Column Generation, 1-32; DOI 10.1007/0-387-25486-2_1 | full | `c01` | pre-publication chapter copy, marked as to appear [pre-publication] |
| S003 | 2021 | MIPLIB 2017: data-driven compilation of the 6th mixed-integer progr… | Mathematical Programming Computation 13 (3), 443-490; DOI 10.1007/s12532-020-00194-3 | full | `c07` | the indexed file |
| S004 | 2009 | The concept of recoverable robustness, linear programming recovery,… | Robust and online large-scale optimization, LNCS, 5868, 1-27; DOI 10.1007/978-3-642-05465-5_1 | full | `c02` | the indexed file |
| S005 | 2018 | The SCIP Optimization Suite 6.0 | https://opus4.kobv.de/opus4-zib/frontdoor/index/index/docId/6936 | full | `c06` | the indexed file |
| S006 | 2021 | The SCIP optimization suite 8.0 | arXiv preprint arXiv:2112.08872 | full | `c08` | the indexed file |
| S007 | 2011 | Branch-Price-and-Cut Algorithms | Wiley Encyclopedia of Operations Research and Management…; DOI 10.1002/9780470400531.eorms0118 | full | `c03` | the authors' encyclopedia manuscript of 2010 [manuscript] |
| S008 | 2011 | Column generation | Wiley Encyclopedia of Operations Research and Management…; DOI 10.1002/9780470400531.eorms0158 | full | `c03` | the author's encyclopedia manuscript of 2010 [manuscript] |
| S009 | 2017 | Learning when to use a decomposition | International conference on AI and OR techniques in const…; DOI 10.1007/978-3-319-59776-8_16 | full | `c04` | the indexed file |
| S010 | 2012 | Curriculum based course timetabling: new solutions to Udine benchma… | Annals of Operations Research. 194 (1), 255-272; DOI 10.1007/s10479-010-0700-7 | full | `c04` | the indexed file |
| S011 | 2010 | Experiments with a generic Dantzig-Wolfe decomposition for integer… | Experimental Algorithms, 239-252; DOI 10.1007/978-3-642-13193-6_21 | full | `c02` | the indexed file |
| S012 | 2004 | A fast algorithm for near cost optimal line plans | Mathematical Methods of Operations Research 59 (2), 205-220; DOI 10.1007/s001860300332 | full | `c01` | TU Berlin report 2003/43 [report] |
| S013 | 2017 | The SCIP optimization suite 4.0 | — | full | `c05` | the indexed file |
| S014 | 2023 | Enabling research through the SCIP optimization suite 8.0 | ACM Transactions on Mathematical Software 49 (2), 1-21; DOI 10.1145/3585516 | full | `c09` | arXiv:2303.07101v1 [arXiv] |
| S015 | 2015 | Automatic Dantzig-Wolfe Reformulation of Mixed Integer Programs | Mathematical Programming 149 (1-2), 391-424; DOI 10.1007/s10107-014-0761-5 | full | `c04` | Optimization Online preprint, revised 2013 [preprint] |
| S016 | 2010 | A constraint integer programming approach for resource-constrained… | International Conference on Integration of Artificial Int…; DOI 10.1007/978-3-642-13520-0_34 | full | `c03` | the indexed file |
| S018 | 2019 | Ship traffic optimization for the Kiel Canal | Operations Research 67 (3), 791-812; DOI 10.1287/opre.2018.1814 | full | `c06` | manuscript submitted to Operations Research [manuscript] |
| S019 | 2025 | The SCIP optimization suite 10.0 | arXiv preprint arXiv:2511.18580 | full | `c10` | the indexed file |
| S020 | 1998 | The vertex set of a 0/1-polytope is strongly P-enumerable | Computational Geometry 11 (2), 103-109; DOI 10.1016/s0925-7721(98)00021-2 | full | `c01` | the indexed file |
| S021 | 2005 | On compact formulations for integer programs solved by column gener… | Annals of Operations Research 139 (1), 375-388; DOI 10.1007/s10479-005-3455-9 | full | `c02` | TU Berlin report 2003/25 [report] |
| S022 | 2007 | Solutions to real-world instances of PSPACE-complete stacking | Proceedings of the 15th annual European Symposium on Algo…; DOI 10.1007/978-3-540-75520-3_64 | full | `c02` | the indexed file |
| S023 | 2008 | Optimizing the cargo express service of Swiss Federal Railways | Transportation Science 42 (4), 450-465; DOI 10.1287/trsc.1080.0246 | full | `c02` | the indexed file |
| S024 | 2003 | Engine routing and scheduling at industrial in-plant railroads | Transportation Science 37 (2), 183-197; DOI 10.1287/trsc.37.2.183.15251 | full | `c01` | the indexed file |
| S025 | 2016 | An adaptive discretization MINLP algorithm for optimal synthesis of… | Computers & Chemical Engineering 95, 38-48; DOI 10.1016/j.compchemeng.2016.09.008 | full | `c04` | preprint of 22 June 2016 [preprint] |
| S026 | 2015 | A Branch-Price-and-Cut Algorithm for Multi-Mode Resource Leveling | European J. Oper. Res. 245 (1), 70-80; DOI 10.1016/j.ejor.2015.02.043 | full | `s04` | the indexed file |
| S027 | 2001 | Engine scheduling by column generation | Cuvillier; DOI 10.24355/dbbs.084-200511080100-720 | full | `b01` | the indexed file |
| S028 | 2008 | Optimal university course timetables and the partial transversal po… | Proceedings of the 7th international conference on Experi…; DOI 10.1007/978-3-540-68552-4_18 | full | `s02` | the indexed file |
| S029 | 2012 | Nested Column Generation applied to the Crude Oil Tanker Routing an… | Naval Research Logistics 59 (3-4), 298-310; DOI 10.1002/nav.21489 | full | `s03` | the indexed file |
| S030 | 2004 | Minimizing the stabbing number of matchings, trees, and triangulations | Proceedings of the fifteenth annual ACM-SIAM symposium on… | abstract | `a2-01` | abstract (round 1, superseded by s3-01) |
| S030 | 2004 | Minimizing the stabbing number of matchings, trees, and triangulations | Proceedings of the fifteenth annual ACM-SIAM symposium on… | full | `s3-01` | arXiv cs/0310034v1, the SODA 2004 extended abstract [arXiv] |
| S031 | 2014 | Row-reduced column generation for degenerate master problems | European Journal of Operational Research 236 (2), 453-460; DOI 10.1016/j.ejor.2013.12.016 | full | `s04` | author preprint, revised 2013 [preprint] |
| S032 | 2011 | Partial convexification of general MIPs by Dantzig-Wolfe reformulation | Integer Programming and Combinatoral Optimization, 39-51; DOI 10.1007/978-3-642-20807-2_4 | full | `c03` | an authors' preprint of the IPCO paper with appendix A on pp. 12-15 (batch c03 header); LNCS pp. 39-51 not mapped [manuscript] |
| S033 | 2005 | Dual variable based fathoming in dynamic programs for column genera… | European Journal of Operational Research 162 (1), 122-125; DOI 10.1016/j.ejor.2003.05.006 | full | `s01` | TU Berlin report 2003/42 [report] |
| S034 | 2008 | Sorting with complete networks of stacks | International Symposium on Algorithms and Computation, 89…; DOI 10.1007/978-3-540-92182-0_78 | full | `s03` | the indexed file |
| S035 | 2011 | Integrated Sequencing and Scheduling in Coil Coating | Management Science 57 (4), 647-666; DOI 10.1287/mnsc.1100.1302 | full | `c03` | the indexed file |
| S036 | 2005 | Shunting minimal rail car allocation | Computational Optimization and applications 31 (3), 295-308; DOI 10.1007/s10589-005-3229-y | full | `s02` | authors' preprint, revised 2004 [preprint] |
| S037 | 1998 | Optimal scrap combination for steel production | OR Spectrum 20 (4), 251-258; DOI 10.1007/s002910050072 | full | `s01` | the indexed file |
| S038 | 2015 | About the minimum mean cycle-canceling algorithm | Discrete Applied Mathematics 196, 115-134; DOI 10.1016/j.dam.2014.07.005 | partial | `s04` | the indexed file |
| S039 | 2014 | Decomposition theorems for linear programs | Operations Research Letters 42 (8), 553-557; DOI 10.1016/j.orl.2014.10.001 | full | `s04` | the indexed file |
| S040 | 2010 | A branch-and-price algorithm for multi-mode resource leveling | International Symposium on Experimental Algorithms, 226-238; DOI 10.1007/978-3-642-13193-6_20 | full | `s03` | the indexed file |
| S041 | 2007 | Rectangle covers revisited computationally | Journal of Experimental Algorithmics (JEA) 11, 2.6-es; DOI 10.1145/1187436.1216583 | full | `s02` | manuscript submitted to JEA [manuscript] |
| S042 | 2018 | Integrating line planning, timetabling and vehicle scheduling | Proceedings of the Conference for Advanced Systems in Pub… | full | `s05` | the indexed file |
| S043 | 2022 | An image-based approach to detecting structural similarity among mi… | INFORMS Journal on Computing 34 (4), 1849-1870; DOI 10.1287/ijoc.2021.1117 | full | `c09` | SSRN preprint, April 2020 [preprint] |
| S044 | 2018 | Vector space decomposition for solving large-scale linear programs | Operations Research 66 (5), 1376-1389; DOI 10.1287/opre.2018.1728 | full | `s05` | the indexed file |
| S045 | 2012 | Primal Heuristics for Branch-and-Price Algorithms | Operations Research Proceedings 2011, 65-70; DOI 10.1007/978-3-642-29210-1_11 | abstract | `a2-01` | no full text; abstract only |
| S046 | 2006 | On minimum k-modal partitions of permutations | LATIN 2006: Theoretical Informatics, 374-385; DOI 10.1007/11682462_36 | full | `s02` | the indexed file |
| S047 | 2017 | Optimization of the reconfiguration planning of handling systems ba… | IEEE Robotics and Automation Letters 2 (3), 1802-1808; DOI 10.1109/lra.2017.2705286 | full | `s05` | the indexed file |
| S048 | 2015 | Comments on: An Overview of Curriculum-Based Course Timetabling | TOP 23 (2), 359-361; DOI 10.1007/s11750-015-0364-1 | full | `c04` | the indexed file |
| S049 | 2016 | Tools for primal degenerate linear programs: IPS, DCA, and PE | EURO Journal on Transportation and Logistics 5 (2), 161-204; DOI 10.1007/s13676-015-0077-5 | partial | `s04` | journal-template manuscript [manuscript] |
| S050 | 2020 | A branch-and-price algorithm for capacitated hypergraph vertex sepa… | Mathematical Programming Computation 12 (1), 39-68; DOI 10.1007/s12532-019-00171-5 | full | `c07` | preprint in SIAM style [preprint] |
| S051 | 2008 | On minimum k-modal partitions of permutations | Journal of Discrete Algorithms 6 (3), 381-392; DOI 10.1016/j.jda.2008.01.002 | full | `s03` | the indexed file |
| S052 | 2018 | The strength of Dantzig–Wolfe reformulations for the stable set and… | Discrete Optimization 30, 168-187; DOI 10.1016/j.disopt.2018.07.001 | full | `c06` | article-in-press version [in-press] |
| S053 | 2005 | Rectangle covers revisited computationally | Experimental and Efficient Algorithms, 55-66; DOI 10.1007/11427186_7 | full | `s02` | the indexed file |
| S054 | 2003 | Computer aided scheduling of switching engines | Mathematics—key technology for the future: joint projects…; DOI 10.1007/978-3-642-55753-8_52 | full | `s01` | chapter manuscript [manuscript] |
| S055 | 2016 | DESSLib–Benchmark instances for optimization of decentralized energ… | Technical report, Technische Universität Aachen, 2016. UR… | full | `s05` | the indexed file |
| S056 | 2013 | Kompakt-Lexikon Wirtschaftsmathematik und Statistik: 750 Begriffe n… | Lehrstuhl für Statistik und Institut für Statistik u. Wir… | abstract | `a2-01` | no full text; abstract only |
| S057 | 2003 | MaxFlow-MinCut duality for a paint shop problem | Operations research proceedings 2002: selected papers of…; DOI 10.1007/978-3-642-55537-4_61 | full | `s01` | the indexed file |
| S058 | 2018 | A Computational Investigation on the Strength of Dantzig-Wolfe Refo… | 17th International Symposium on Experimental Algorithms (…; DOI 10.4230/lipics.sea.2018.11 | full | `c06` | the indexed file |
| S059 | 2011 | Challenges in scheduling when planning the ship traffic on the Kiel… | MAPSP 2011, Nymburk (plenary talk, 20 June 2011) | metadata | `a2-01` | no full text; metadata only |
| S060 | 2026 | Column generation | Branch-and-Price, 43-102; DOI 10.1007/978-3-031-96917-1_2 | full | `c11` | the indexed file |
| S061 | 2017 | A strongly polynomial contraction-expansion algorithm for network f… | Computers & Operations Research 84, 16-32; DOI 10.1016/j.cor.2017.02.019 | full | `s05` | the indexed file |
| S062 | 2014 | Zukunftsperspektiven des Operations Research | Springer Gabler; DOI 10.1007/978-3-658-05707-7 | abstract | `a2-01` | no full text; abstract only |
| S063 | 1998 | Yet another note on "An efficient zero-one formulation of the multi… | Technical report, Department of Mathematical Optimization… | full | `s01` | the indexed file |
| S064 | 2019 | Reform der Bundestagswahlkreise | Zeitschrift für Parlamentsfragen 50 (1), 3-21; DOI 10.5771/0340-1758-2019-1-3 | abstract | `a2-01` | no full text; abstract only |
| S065 | 2014 | A Branch-Price-and-Cut Algorithm for Packing Cuts in Undirected Graphs | Experimental Algorithms, 34-45; DOI 10.1007/978-3-319-07959-2_4 | full | `s04` | the indexed file |
| S066 | 2004 | Combinatorially simple pickup and delivery paths | Central Eur J Oper Res 12, 405-417 | full | `s01` | submitted manuscript of 2003 [manuscript] |
| S067 | 1998 | Discrete optimization in rail transport | Extended abstract, TU Braunschweig, Mathematische Optimie… | full | `s01` | the indexed file |
| S068 | 2015 | Separation of generic cutting planes in branch-and-price using a basis | International Symposium on Experimental Algorithms, 110-121; DOI 10.1007/978-3-319-20086-6_9 | full | `s04` | the indexed file |
| S069 | 2015 | Primal heuristics for mixed integer programs with a staircase struc… | Technical Report, RWTH Aachen University | metadata | `a2-01` | no full text; metadata only |
| S070 | 2012 | Automatic Decomposition and Branch-and-Price—A Status Report | Experimental Algorithms, 1-8; DOI 10.1007/978-3-642-30850-5_1 | full | `s03` | the indexed file |
| S071 | 2018 | Polyhedral results on the stable set problem in graphs containing e… | Mathematical Programming 171 (1-2), 519-522; DOI 10.1007/s10107-017-1168-x | full | `s05` | the indexed file |
| S072 | 2016 | Operations Research Proceedings 2014: Selected Papers of the Annual… | Springer; DOI 10.1007/978-3-319-28697-6 | abstract | `a2-01` | no full text; abstract only |
| S073 | 2016 | A Branch-Price-and-Cut Algorithm for Packing Cuts in Undirected Graphs | Journal of Experimental Algorithmics (JEA) 21, 1-16; DOI 10.1145/2851492 | full | `s05` | the indexed file |
| S074 | 2021 | Avoiding redundant columns by adding classical Benders cuts to colu… | Discrete Optimization 39, 100626; DOI 10.1016/j.disopt.2021.100626 | full | `c09` | Open Research Exeter accepted manuscript [manuscript] |
| S075 | 2026 | Integrated Topology and Redispatch Optimization of Real-World Power… | arXiv preprint arXiv:2611.18302 | full | `c11` | the indexed file |
| S076 | 2026 | Fast Subproblem Solving in Benders Decomposition for Affine Potenti… | arXiv preprint arXiv:2611.15203 | full | `c12` | the indexed file |
| S077 | 2026 | Branch-Price-and-Cut | Branch-and-Price, 443-543; DOI 10.1007/978-3-031-96917-1_7 | full | `c13` | the indexed file |
| S078 | 2018 | Optimization of the reconfiguration planning of cyber-physical prod… | 2018 International Conference on Reconfigurable Mechanism…; DOI 10.1109/remar.2018.8449867 | full | `s06` | the indexed file |
| S080 | 2018 | Neueinteilung der Bundestagswahlkreise mithilfe mathematischer Opti… | repORt 2018-050, Lehrstuhl für Operations Research, RWTH… | full | `s06` | the indexed file |
| S081 | 2016 | DESSLib–Benchmark Instance Structure, Component Models and Parameters | — | full | `s05` | the indexed file |
| S082 | 1998 | Optimale Disposition von Rangierlokomotiven bei Werks-und Industrie… | — | metadata | `a2-01` | no full text; metadata only |
| S083 | 1996 | Algorithmen zur Enumeration der Ecken und Facetten konvexer Polyeder | Diplomarbeit, Technische Universität Braunschweig, 1996,… | partial | `s01` | the indexed file |
| S084 | 2026 | Dantzig-Wolfe Decomposition for Integer Linear Programming | Branch-and-Price, 173-293; DOI 10.1007/978-3-031-96917-1_4 | full | `c14` | the indexed file |
| S085 | 2026 | Vehicle Routing and Crew Scheduling Problems | Branch-and-Price, 295-349; DOI 10.1007/978-3-031-96917-1_5 | full | `c15` | the indexed file |
| S086 | 2026 | Dantzig-Wolfe Decomposition for Linear Programming | Branch-and-Price, 103-171; DOI 10.1007/978-3-031-96917-1_3 | full | `c16` | the indexed file |
| S087 | 2026 | Linear and Integer Linear Programming | Branch-and-Price, 1-42; DOI 10.1007/978-3-031-96917-1_1 | full | `c17` | the indexed file |
| S088 | 2026 | Dual Point of View | Branch-and-Price, 351-442; DOI 10.1007/978-3-031-96917-1_6 | full | `c18` | the indexed file |
| S089 | 2026 | Branch-and-price strikes back for the k-vertex cut problem | arXiv preprint arXiv:2602.04984 | full | `c19` | the indexed file |
| S090 | 2022 | SCIP8: rethinking nonlinear constraint representation and recent pr… | 23ème congrès annuel de la Société Française de Recherche… | full | `s06` | the indexed file |
| S091 | 2020 | Welcome to SN Operations Research Forum! | SN Operations Research Forum 1 (1), 1; DOI 10.1007/s43069-020-0001-1 | full | `c07` | the indexed file |
| S094 | 2018 | Optimization of the Reconfiguration Planning of Cyber-Physical Prod… | Vierte IFToMM D-A-CH Konferenz 2018 (DuEPublico, DOI 10.1…; DOI 10.17185/duepublico/45329 | full | `s06` | the indexed file |
| S100 | 2014 | Dynamische Vergabe von Patiententerminen in Krankenhäusern | Zukunftsperspektiven des Operations Research: Erfolgreich…; DOI 10.1007/978-3-658-05707-7_6 | abstract | `a2-01` | no full text; abstract only |
| S102 | 2012 | The Boat and Barge Routing Problem | 10th Cologne-Twente Workshop on Graphs and Combinatorial… | metadata | `a2-01` | no full text; metadata only (a Scholar row that is not his work; Role skip) |
| S106 | 2009 | Scheduling in Coil Coating with Shuttles | The 9th Workshop on Models and Algorithms for Planning an… | metadata | `a2-01` | no full text; metadata only |
| S107 | 2008 | Third European Conference on combinatorics graph theory and applica… | DISCRETE MATHEMATICS 308 (8), 1347-1349; DOI 10.1016/j.disc.2007.09.029 | full | `s03` | the indexed file |
| S108 | 2008 | Computational Mixed Integer Programming | — | metadata | `a2-01` | no full text; metadata only |
| S109 | 2007 | Editorial/ European Journal of Combinatorics-Volume 28, Issue 8 | European Journal of Combinatorics 28 (8), 2053-2056; DOI 10.1016/j.ejc.2007.04.003 | full | `s02` | the indexed file |
| S110 | 2007 | Recoverable robustness | ARRIVAL Technical Report TR-0066 | metadata | `a2-01` | no full text; metadata only |
| S111 | 2007 | Computing All Stable Orientations of Assemblies with the Double Des… | — | metadata | `a2-01` | no full text; metadata only |
| S112 | 2005 | On Minimum Monotone and Unimodal Partitions of Permutations | DOI 10.14279/depositonce-14343 | full | `s02` | the indexed file |
| S114 | — | Using VRPSolver’s Price-and-Cut Engine within GCG | — | metadata | `a2-01` | no full text; metadata only |
| S115 | — | The Multi-Stop Station Location Problem: Exact Approaches | Available at SSRN 7177419; DOI 10.2139/ssrn.7177419 | full | `c19` | the indexed file |
| S118 | 2018 | Eliminating redundant columns from column generation subproblems us… | SCIP Workshop 2018, Aachen, 8 March 2018 (slides) | full | `s06` | the indexed file |
| S119 | — | Vector Space Decomposition for Network Flow and Linear Problems | — | metadata | `a2-01` | no full text; metadata only |
| S120 | — | A minimum weighted mean cost cycle algorithm for linear programming | — | metadata | `a2-01` | no full text; metadata only |
| H001 | 2011 | Improved Column Generation for Highly Degenerate Master Problems | Les Cahiers du GERAD G-2011-66 | abstract | `a2-01` | no full text; abstract only |
| D001 | 2008 | Minimizing the Stabbing Number of Matchings, Trees, and Triangulations | Discrete & Computational Geometry 40 (4), 595-621; DOI 10.1007/s00454-008-9114-6 | full | `s02` | arXiv cs/0310034v3 [arXiv] |
| D002 | 2009 | Sequencing and Scheduling in Coil Coating with Shuttles | Models and Algorithms for Optimization in Logistics (Dags…; DOI 10.4230/dagsemproc.09261.26 | full | `s03` | the indexed file |
| D003 | 2010 | Frontmatter, Table of Contents, Preface, Organization | ATMOS 2010 (OASIcs, Volume 14); DOI 10.4230/oasics.atmos.2010.i | full | `s03` | the indexed file |
| D004 | 2026 | Conclusion | Branch-and-Price, 545-554; DOI 10.1007/978-3-031-96917-1_8 | full | `c10` | the indexed file |
| D006 | 2015 | Dantzig-Wolfe Reformulations for the Stable Set Problem | ResearchGate (unpublished); DOI 10.13140/rg.2.1.3470.0887 | full | `s04` | the indexed file |

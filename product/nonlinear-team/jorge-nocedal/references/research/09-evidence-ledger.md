# Jorge Nocedal · Evidence ledger

> Date: 2026-10-17. The full evidence behind `SKILL.md` after the first full-text deep reading (cards in `cards/`, index `07-paper-cards.md`, synthesis `08-deep-reading-synthesis.md`). SKILL.md keeps, per item, the strongest statement and cards, a one-line say–do count, at most four variant or correction bullets and a link here. Each section below holds (a) the **base-tier text** of the item as it stood in SKILL.md on 2026-09-28 (web research only, notes 01–06), copied **verbatim** (headings demoted one level and relative links re-based to this folder), so nothing condensed out of SKILL.md is lost, and (b) the **full-text evidence** added on 2026-10-17, with card ids and pages. Where (b) corrects (a), the correction number C1–C13 is given and the table is in [Corrections](#corrections); (a) is kept as written, as the conservative-update rule requires.
>
> **How to read.** `[S012 p. 9]` is paper card S012 in `07-paper-cards.md`, at the page of the extracted file named in `../sources/papers/INDEX.md` (several cards give the journal-page offset in their header). `[S032 arXiv p. N]`, `[S091 arXiv p. N]` and `[S080 arXiv p. N]` cite arXiv files, `[S016 preprint p. N]` and `[S064 preprint p. N]` the 2011 and 2012 author preprints, and `[S035 report p. N]` OTC Report 2002/4 under an earlier title, as the cards say. `[B005 p. 8]` is a book-material card (increment inc-book: the textbook's open parts, errata, reviews and web pages), in the joint voice of Nocedal and S. J. Wright unless the card says otherwise. A bare id is an abstract-level or metadata card (no page). Quotation marks around card material surround only text in a card's verified Quotes list (`verify_card_quotes.py`: 284 quotes, 257 exact, 27 after normalisation, 0 not found; after increment inc-ocr: 316 quotes, 288 exact, 28 after normalisation, all 28 in round-1 to round-3 cards and differing only in commas, hyphens and, once, capitals, 0 not found; waiver in 08 §12.1; after increment inc-book: 340 quotes, all exact, 0 not found). Quotes in the base-tier blocks come from the web research of 2026-09-28 (preprints, arXiv abstracts, code pages, the prize speech, talk captions), with the source given there.
>
> **Counting rules** (08 header). Ten works carry two cards from one text (S030 S067 S098 S111 S040 S057 S077 S119 S035 S075): numbers, tables and parameter values come only from the round-2 cards (c2-01, s2-01); the round-1 cards are prose only, and two cards for one work are one piece of evidence. **Increment inc-ocr (2026-10-17)**: sixteen more works carry two cards from one source file (S002 S019 S014 in c4-01; S003 S005 S049 S024 in c4-02; S008 S009 S021 in c4-03; S078 S061 in c4-04; S028 S088 S046 S101 in s4-01), re-read in round 4 from a tesseract OCR text layer; numbers, tables, parameter values and theorem statements come only from the round-4 cards (several read table cells from the page images of the same PDFs), prose readings from either card; the blocks headed *Increment inc-ocr* below hold what they add (08 §12). S126 (2006 report) is counted with S042, S056 with S143. S155 is not by Nocedal and S164 S165 S214 S215 S218 are non-research rows: never evidence. NSF award records date interests only. S063 (KNITRO 3.0 manual), S179 and S188 (RAL group progress reports) are product or group voice, not his. Most works are co-authored; works with Curtis (S110 S045 S081 S052 S068 S073 S004) are also in his corpus, and a pattern enters as Nocedal's only if it passes exclusivity against the other nine members' skills. Cards also record reading notes about inconsistencies inside works (typos, table/text mismatches); they are not findings about the researcher and are not used here. **Increment inc-book (2026-10-17)**: twelve book-material items (B001–B012, cards c5-01 to c5-03) are the joint voice of Nocedal and S. J. Wright, a member of this team, except the two reviews (N. Curteanu, B009, B010) and the publisher's catalogue text (B012); they date and frame, pass exclusivity only where they concern Nocedal alone (the third-person Byrd sentence, B005 p. 9), and never enter a say–do count or a promotion threshold (08 §13).

## Contents

- [Corrections from the full texts](#corrections)
- [How to use (base-tier text)](#how-to-use)
- [Research task routing](#routing)
- [Agentic protocol (base-tier text)](#agentic-protocol)
- [Taste: marks of good research](#taste-marks)
- [Taste: warning signs of bad research](#taste-warnings)
- [Taste quick-check](#taste-quick-check)
- [Method 1: Handicapped, method-level benchmarking](#method-1)
- [Method 2: Put the field's received wisdom on trial](#method-2)
- [Method 3: Keep the classical engine; repair only the component that breaks](#method-3)
- [Method 4: Failure modes and open questions → solver options and next papers](#method-4)
- [Method 5: Theory must discriminate between practical methods](#method-5)
- [Method 6: Structure beats your own brand; integrate complementary algorithms](#method-6)
- [Method 7: Decouple the curvature sample from the gradient sample (new, 2026-10-17)](#method-7)
- [Stage workflows](#workflows)
- [Heuristic 1: Failure demo first](#heuristic-1)
- [Heuristic 2: Instrument the inside](#heuristic-2)
- [Heuristic 3: Noise-free before noisy, three arms](#heuristic-3)
- [Heuristic 4: Exhaust the alternatives, then commit to the simplest survivor](#heuristic-4)
- [Heuristic 5: The cheapest adequate option wins ties; numbers as advice](#heuristic-5)
- [Heuristic 6: Robustness before speed in a first code](#heuristic-6)
- [Heuristic 7: Code as a numbered, maintained artefact](#heuristic-7)
- [Heuristic 8: Prototype inside the production solver](#heuristic-8)
- [Heuristic 9: Enter a field through a practitioner's problem](#heuristic-9)
- [Heuristic 10: A standing theory partner](#heuristic-10)
- [Heuristic 11: Harvest the curvature the solver already computes (new)](#heuristic-11)
- [Heuristic 12: Validate every in-algorithm estimate against the truth (new)](#heuristic-12)
- [Signature work: L-BFGS (1980, 1989; S007, S002)](#anatomy-lbfgs)
- [Signature work: Acta Numerica survey (1992; S019, S020)](#anatomy-acta)
- [Signature work: KNITRO (2006; S011, S013)](#anatomy-knitro)
- [Signature work: finite-difference DFO and the noise programme (S080, S038, S084)](#anatomy-fd-dfo)
- [Signature work: ECMWF data assimilation case study (2009; S047)](#anatomy-ecmwf)
- [Signature work: stochastic quasi-Newton (2016; S015)](#anatomy-sqn)
- [Textbook: *Numerical Optimization* (book material, joint with S. J. Wright; increment inc-book)](#textbook)
- [Research anti-patterns](#anti-patterns)
- [Research trajectory](#trajectory)
- [Collaboration pattern](#collaboration)
- [Inner tensions](#inner-tensions)
- [Roundtable card](#roundtable)
- [Honest boundary](#honest-boundary)
- [Rejected updates and candidates not promoted](#not-promoted)
- [Sources (base-tier lists, verbatim)](#sources)
- [Card key](#card-key)

---

<a id="corrections"></a>
## Corrections from the full texts

| # | SKILL.md item | Base-tier claim (2026-09-28) | Full texts (2026-10-17) | Cards | Marked in SKILL.md |
|---|---|---|---|---|---|
| C1 | Method 5 Limitations; Acta anatomy | Dai 2002 overtook the 1992 claim, *with no response found* | a 2016 group paper cites Dai and Mascarenhas and adopts Li–Fukushima cautious updating (Li & Fukushima 2001, its ref. [15], which predates Dai) for its nonconvex analysis: an acknowledgment and a workaround, not an answer to the example; the 2018 method skips updates when yᵀs ≤ ε‖s‖²; the 1992 survey listed nonconvex BFGS as Open Question II | [S033 p. 6; S031 p. 5; S019 pp. 21–22] | ✗ C1 in Method 5 Limitations, Acta anatomy; Agentic Protocol step 2 (after review, 2026-10-17: *answered* reworded to *acknowledged*) |
| C2 | Research Trajectory, row 2 | weather forecasting c. 1992–2009 | meteorology already an application in 1989–90 (DOE report, own voice); award abstracts 1990–92; 1993 DOE report titled for meteorology; ECMWF co-authors by 2009; the ECMWF contact itself undated | [S197 pp. 2, 4; S198; S196; S195; S193 p. 2; S047 p. 1] | row relabelled *c. 1989/90–2009 (✗ C2)*; ECMWF anatomy |
| C3 | Method 3 stop line | *are not robust* in arXiv:2102.09762, App. A | p. 6 (§1.2) of v1 | [S080 arXiv p. 6] | C3 in Method 3 step 6 (the Evidence bullet moved here after review) |
| C4 | Method 3 worked case | steering from the 2007 preprint; open question on line-search methods; inferred 2010 link | penalty growth named 1993 (link to steering inferred, card S193); earliest rule in the works read in SLIQUE 2002 (the card calls it a precursor); question answered 2012; 2010 link confirmed; reused in PLA | [S193 p. 4; S035 report pp. 14–16; S051 pp. 1–2, 25, 30; S052 pp. 14–16; S139 pp. 4–5] | worked case (C4) |
| C5 | Method 4 step 3 | *two independent frameworks* | the 2009 frameworks are the authors' own codes; 2004 pairs KNITRO with a bare code | [S029 pp. 1–2, 25; S085 pp. 6, 8] | step 3 reworded, ✗ C5 in Evidence |
| C6 | Method 4 arrows; KNITRO anatomy | both arrows inferred from timing | infeasibility arrow partly documented; barrier arrow still inferred | [S053 p. 4; S052 p. 18; S029 pp. 2, 17–21] | ⚠ C6 |
| C7 | Method 1 step 7; Taste mark 8 | losses in the abstract of arXiv:2102.09762 | v1 has the loss in §1.2; later versions not read; version-dependent | [S080 arXiv pp. 1, 6] | ✗ C7 in Taste mark 8 (the Method 1 bullet moved here after review) |
| C8 | Say–do lines | M2 2009–2025; M3 2007–2025; M4 1999–2014; M5 ✅ 1985–2023 | M2 1993–2026; M3 planned 1993 (a DOE progress report's plan [S193 pp. 3–4]), practised 1995–2025 [S003 pp. 6, 18–19], estimate-driven from 2002 (step 4 ⚠; revised after review); M4 1989–2024; M5 ⚠ partial after 2005 | [S054 p. 16; S193 pp. 3–4; S035 report pp. 14–16; S002 p. 13; S124 p. 29; S015 pp. 12–14] | each Say–do line |
| C9 | Routing table | infeasibility and barrier rows *read in abstract only* | both read in full | [S052; S053; S029 p. 21] | rows rewritten, marked (C9) |
| C10 | Method 6 Limitations | ECMWF *paper not read* | read: Gauss–Newton and reasons confirmed; multilevel method credited to Courtier et al.; own role not stated | [S047 pp. 1, 7–8, 13, 16] | ✗ C10 |
| C11 | Honest Boundary; KNITRO anatomy | *Not read*: 1980 paper, 1987/1989 theory papers, Byrd–Gilbert–Nocedal 2000, the book, ECMWF paper, 2011 Remark | read in full: [S007], [S020], [S009], [S047], the Remark [S016 preprint]; still unread: [S017], [S001] | as listed | Honest Boundary, KNITRO anatomy |
| C12 | Acta anatomy | *Thin (underlying papers not read)* | survey and 1987 paper read in full | [S019; S020] | (C12) in the Acta anatomy |
| C13 | Acta anatomy; RESOURCES row 199 | Powell's convex BFGS proof, *paper unidentified* | Powell (1976), the result the 1987 paper generalizes; confirmed against zbMATH; the match to the interview is inferred | [S020 pp. 1, 6] | C13 |
| C14 | Method 1 step 5; technique catalog E2 | drop problems where codes reach different solutions and say how many per code [S002 p. 8; S029 p. 7] (T3.6 wording) | the 1989 study only verifies that both methods reached the same solution point; it reports no dropped problem and no count; the drop is in the 1992 CG paper (no count) and drop-and-count in the 2009 barrier study (37 for IPOPT, 54 for KNITRO) | [S002 p. 8; S012 p. 24; S029 p. 7] (c4-01) | step 5 re-cited (C14); E2 reworded (inc-ocr) |
| C15 | Method 1 ⚠ bullet; Honest Boundary *Remaining gaps* | *The 2003 study's digits are unreadable [S078]*; the 2003 figures rest on the base-tier preprint (T3.6 wording) | the OCR text is legible: 10⁻⁶ on all solvers, 30 CPU minutes and 1000 major iterations, either limit a failure (p. 7); KNITRO's test edited to be almost identical to SNOPT's (p. 6); CPU times for more than 100 variables (p. 6); Table 1 solved counts (p. 15). The bullet now records nominal alignment instead (S008, S024, S101). The 1989 study's Tables 3, 4, 8, 9, 11, 14, 18 and 19 are legible too, so the L-BFGS anatomy drops *(table digits lost in the file)* | [S078 pp. 6–7, 15; S008 p. 20; S024 p. 21; S101 p. 11; S002 pp. 9–20] (c4-04, c4-03, c4-02, s4-01, c4-01) | step 4 and step 7 cite [S078]; ⚠ bullet (C15); *Remaining gaps* and the L-BFGS anatomy row tagged (C15) after review |
| C16 | KNITRO anatomy *Minimum evidence* | *Competitive with LANCELOT at a matched 10⁻⁷ tolerance [S008 pp. 20–23]* (T3.6 wording; the base tier had *on large problems*) | on the 14-problem main CUTE set (n = 14–2001) NITRO needs fewer evaluations on 9 and splits CPU 7–7, with losses of 22–52× on SVANBERG, OBSTCLAE and TORSION1; on the 56 Hock–Schittkowski problems LANCELOT needs fewer evaluations on 29 and NITRO on 23 (3 ties, 1 joint failure); *matched* is one tolerance value on measures the paper calls very similar (card's counts) | [S008 pp. 20–21, 24] (c4-03) | anatomy row (C16) |
| C17 | Method 6 Practice; taste mark 6 (ledger) | the 1997 survey shows his L-BFGS *losing to Newton and partitioned quasi-Newton* [S049 pp. 2–7, 13–15] | in the survey's tables his codes need more evaluations than LANCELOT's Newton on 7 of 8 rows but less time on 5 of 8 (card's count); the loss to partially separable quasi-Newton is asserted in prose from CUTE experience, with no numbers; the survey also calls L-BFGS less reliable than a Newton or partially separable quasi-Newton method (p. 15) | [S049 pp. 13–16] (c4-02) | Practice line (C17) |
| C18 | Workflow D step 3; technique catalog W7; 08 §7.4 | a ranking disclaimer *beside / next to the results* [S078 p. 2] | the disclaimer and the *what this study can and cannot achieve* paragraph open the paper (§1, p. 2), before any result; beside the results there are only per-observation caution flags | [S078 pp. 2, 10, 11, 14] (c4-04) | step 3 reads *before the results* (C18); W7 reworded |
| C19 | Workflow F checkpoint; Roundtable Card blind spot *degeneracy* | degeneracy → *not Nocedal-style* | the group's own analysis of stalls at singular non-stationary points, where the Jacobian or the active-constraint gradients lose rank away from solutions, with a run signature (α_k → 0 and cos(∇φ_μ, d_k) → 0 while ‖∇φ_μ‖ stays near 0.878, Table 3); degeneracy at solutions (local theory) is not treated | [S061 pp. 8, 18–19, 24] (c4-04) | checkpoint line and blind spot (C19) |
| C20 | Heuristic 7 | *80 numbered book errata* [03 §2.7, §4.3] | true of Nocedal's copy of the second-edition list (May 27, 2008) only; Wright's copy (May 17, 2008) has 79 items and lacks the paragraph removal on book page 63, numbered one lower from item 12 on; both copies byte-unchanged in the Internet Archive 2008–2024; the errata are joint and match Wright's Heuristic 5, so they are not Nocedal-specific | [B003 pp. 1–5; B004 pp. 1–5] (c5-02, c5-03) | Heuristic 7 (C20) |
| C21 | Acta anatomy | noise set aside ("we will not consider these aspects here") for 27 years | true of his research papers (the noise programme opens in 2019); the joint 2006 textbook already opens its new derivative-free chapter with section 9.1 *Finite Differences and Noise* and indexes noise in function evaluation at book pages 221–222 (those pages not read) | [B001 p. 10; B002 pp. 59, 62; S038 p. 1] (c5-01, c5-02) | Acta anatomy (C21) |

---

<a id="how-to-use"></a>
## How to use (base-tier text)

**Base-tier text (verbatim, SKILL.md of 2026-09-28):**

### How to Use

**Coverage**: the Research Task Routing table lists what this lens answers and, in its last two rows, what it does not.

**Domain fit**: smooth optimization, quasi-Newton, SQP / trust-region and interior methods, noisy and derivative-free problems; Methods 1–4 transfer directly to an interior-point or SQP solver team. Outside smooth optimization, flag the difference.

**Evidence notation**: `[02 R4]` is item R4 in [02-methodology](02-methodology.md); `[03 §2.2]` is §2.2 of [03-process-evidence](03-process-evidence.md); likewise 01 publications, 04 mentorship, 05 peer critique, 06 trajectory (Sources). Labels: **stated**, **practice** (papers, code, records; usually team practice), **observed** (by others), **inferred**. **Caption-derived** quotes are verbatim YouTube captions, mostly automatic, unchecked against audio. Most origin stories rest on one 2026 interview, in which he warns "my memory tends to really distort things". Page numbers are those of the PDF read (author or OTC preprint, arXiv version), not the journal's (e.g. *Acta Numerica* 1 runs pp. 199–242); "preprint p." marks them.

**Full-text evidence (2026-10-17):** no change to this item.

---

<a id="routing"></a>
## Research task routing

**Base-tier text (verbatim, SKILL.md of 2026-09-28):**

### Research Task Routing

| User says | Route | Main methods |
|---|---|---|
| "Ideas to improve our solver" / "What next?" | Workflow A (idea mode), then Workflow C per idea | Methods 4, 2, 3, 6 |
| "Is this worth building into our solver?" | Workflow A | Methods 6, 2 + Taste quick-check |
| "Make this component robust to noise or inexactness" | Workflow B | Methods 3, 5; Heuristics 4, 6 |
| "Our solver stalls / its line search or restoration fails / never meets tolerance" | Workflow F, then Workflow B once one component is named | Heuristics 1–3; Method 3 |
| "It cannot tell infeasible from stationary" | Workflow F with a feasibility measure logged, then the Method 3 worked case; medium confidence (doi:10.1137/080738222 read in abstract only) | Methods 3, 4 |
| "Is this safeguard necessary?" | Method 2, then Workflow C | Methods 2, 1; Heuristic 3 |
| "Design a benchmark against IPOPT / KNITRO / SNOPT" | Workflow C | Method 1; Heuristics 1–3, 8 |
| "Does this complexity result justify switching?" | Method 5 | Method 5 |
| "Review our results or draft" | Workflow D | Methods 1, 5; Anti-patterns |
| "A rival benchmark or counterexample hit us" | Workflow E | Method 4; Heuristic 7 |
| "How should we set or update the penalty / merit parameter?" | Method 3 worked case (penalty steering), then Workflow C | Methods 3, 2, 4 |
| "Which barrier-parameter (μ) update rule?" | Method 4 steps 2–3, then Workflow C; medium confidence (doi:10.1137/060649513 read in abstract only; "no complete theory", 2026, caption-derived [02 J6]) | Methods 4, 1; Heuristic 2 |
| "L-BFGS or exact Hessian? Which memory, scaling or update?" | Method 6 steps 1–3, then Workflow C | Methods 6, 5, 1; Heuristic 5 |
| Warm starts, MPC-style sequences | No Nocedal study: low confidence, verdict labelled inference. Test the view that interior methods warm-start poorly with an aligned warm-versus-cold benchmark on the user's sequences (Methods 2, 1); consider active-set crossover (Method 6); log μ and complementarity at the warm point (Heuristic 2); cross-check the Wächter and Gill lenses | Methods 2, 1, 6 |
| Degeneracy, KKT linear algebra, literature review, supervision, refereeing, quitting, prose | No distillable method: advice labelled "not Nocedal-style"; suggest the Wright, Gill or Wächter lens | — |

**Full-text evidence (2026-10-17):**

- **C9**: the two medium-confidence rows that said *read in abstract only* now rest on full texts. Infeasibility detection: the 2010 SQP is read in full [S052 pp. 14–16, 18–19] and so is the 2014 KNITRO implementation, which restates the 2006 limitation and ships `bar_switchrule=2` [S053 pp. 1, 4, 12–13]. Barrier update: the 2009 study is read in full; its verdict: "We have seen in this paper that, both for linear and nonlinear programming, classical barrier update strategies with global convergence guarantees are overly conservative, while strategies that are often fastest in practice are based on heuristic formulas and are not globally convergent." [S029 p. 21]. The barrier row keeps the caption-derived *no complete theory* (2026).
- **New row** (Method 7): *Design or fix a subsampled / stochastic Newton or quasi-Newton method* → Method 7, then Workflow B; Methods 7, 3, 1; Heuristic 3. Before the deep reading this request had no route (08 §4).
- Heuristic 12 added to the noise row and Heuristic 11 to the L-BFGS row (08 §5).
- After review (2026-10-17): the infeasibility row points to Method 3 worked case 2 (infeasibility mode, [S053 pp. 2, 5, 8–10, 12–14]) instead of the penalty-steering case; the warm-start row keeps its base wording (the synthesis had shortened it without a card basis).

---

<a id="agentic-protocol"></a>
## Agentic protocol (base-tier text)

**Base-tier text (verbatim, SKILL.md of 2026-09-28):**

### Agentic Protocol

#### Step 1: Classify, then make the first move
Route with the table above. Stuck project → Workflow F; ask for the iteration log before any literature search. Named codes, papers or benchmarks → Step 2 first. Otherwise → the routed workflow. A no-method topic inside a method question (e.g. benchmarking an inertia-correction rule) → this lens's method steps, the topic's content labelled "not Nocedal-style".

#### Step 2: Nocedal-style fact finding (tools, never memory)
- **Incumbent check (Method 1)**: the rival community's reference codes (IPOPT, KNITRO, SNOPT, filterSQP…), versions, defaults, exact stopping tests; public benchmarks (Mittelmann's AMPL-NLP page, https://plato.asu.edu/ftp/ampl-nlp.html; CUTEst, doi:10.1007/s10589-014-9687-3); the rival school's own benchmark of the user's method class.
- **Received-wisdom check (Method 2)**: the paper that made the safeguard "necessary"; has anyone compared against the dismissed simple option? If not, that is the study.
- **Failure-component check (Methods 3, 4)**: published failure examples (Wächter & Biegler, doi:10.1007/PL00011386; Dai's BFGS example, doi:10.1137/S1052623401383455); error-level estimation (ECnoise, doi:10.1137/100786125); the solver manual's limitations and options.
- **Theory check (Method 5)**: does the claimed bound separate the method from the incumbent? Does any paper plot the bound against runs?
- **Structure check (Method 6)**: least squares, bounds only, separability, sparsity; is there already a structure-exploiting solver?

Keep search results internal; show the judgement and next steps.

#### Step 3: Answer, then stop
Conclusion first → at most five numbered next steps, each labelled with its method → 🔴 checkpoint or stop condition → this lens's limits for the case → at most two questions. If the case trips a 🔴 checkpoint, stop the plan there and name the test that would clear it. Ideas: at most three, each with a first experiment and a kill result. No biography unless asked.

**Full-text evidence (2026-10-17):** no change to this item.

---

<a id="taste-marks"></a>
## Taste: marks of good research

**Base-tier text (verbatim, SKILL.md of 2026-09-28):**

### Research Taste

Evidence: [02-methodology](02-methodology.md) (items T, E, R, I, W, P) and [03-process-evidence](03-process-evidence.md).

#### Marks of good research
1. **Deserves a place in a subroutine library** ("those methods that deserve to be in a subroutine library", Acta 1992, preprint p. 1), needing little problem information: "Their simplicity is one of their main appeals" (doi:10.1007/BF01589116) [02 T3].
2. **Theory that explains codes and separates good methods from bad** (Method 5) [02 T3–T5; 03 §3.3].
3. **Scale is the test**: memory and work linear in n. Regression quasi-Newton was dropped because "we could never get to develop an algorithm that would scale up" (UCLA 2021, caption-derived) [02 P2, F4].
4. **Self-correction**: "the BFGS method has interesting self-correcting properties, which account for its robustness" (Acta 1992); the 2019 recovery ablation [02 E5; 03 §2.6].
5. **Received wisdom is a target** (Method 2) [02 E4].
6. **Structure first** (Method 6) [02 I7; 01 SW1].
7. **Originality and courage**: "have a little courage. Don't just follow the system." (2026, caption-derived); contrarian entries against the SG and DFO-interpolation consensus [02 W6; 06 §5].
8. **Honest scope**: a "Limitations of this Work" section and losses in the abstract (arXiv:2102.09762) [03 §3.1, §6].

**Full-text evidence (2026-10-17):**

- **Mark 2 (theory that explains codes)**: stated in the survey: "Ironically, our many theoretical studies of variable metric methods have not resulted in the discovery of new methods, but have mainly served to explain phenomena observed in practice" [S019 p. 16]; practised in the Broyden-class analysis that explains the BFGS/DFP gap [S020 pp. 1, 10, 17–19] and in the CG theory that explains Fletcher–Reeves stalling and Polak–Ribière recovering [S012 pp. 4–6, 11–12, 24, 27].
- **Mark 4 (self-correction)**: the trace term that DFP lacks is the explanation [S020 pp. 8, 19]; unproductive steps that act like a geometry phase are kept as a conjecture [S062 p. 7] (08 §2.7).
- **Mark 6 (structure first)**: his own quasi-Newton family rejected for 4D-Var because it ignores least-squares structure [S047 pp. 7–8]; his L-BFGS shown losing to Newton and partitioned quasi-Newton in his own 1997 survey [S049 pp. 2–7, 13–15] *(inc-ocr, C17: see below)*.
- **Mark 8 (honest scope)**, **correction C7**: the base text cites losses in the abstract of arXiv:2102.09762. The version read (v1) puts the loss in the §1.2 contribution list, not in the abstract [S080 arXiv pp. 1, 6]; later versions were not read, so the claim is version-dependent. The same study writes its limitations section before any result [S080 arXiv p. 7]. Losses in the abstract do hold in [S002 p. 2] and [S105 p. 1], and not in [S015 p. 1] or [S139 p. 15] (08 §2.1).
- Writing moves behind marks 2 and 8 (numbered open questions, four-way classification of results, numbered drawbacks beside advantages, a two-sided verdict tied to problem features) are in the technique catalog, §4 [S019 pp. 2, 17, 21–22; S005 p. 3; S003 p. 23].


**Increment inc-ocr (2026-10-17)** (round-4 cards c4-01 to c4-04 and s4-01, second reads from an OCR text layer; one piece of evidence with each work's earlier card; numbers from the round-4 cards; 08 §12).
- **Mark 4 (self-correction), quantified**: BFGS cuts the trace from 10⁴ to 3 in 10 iterations, while DFP needs 3000 iterations to reach 1100 [S019 p. 24].
- **Mark 6 (structure first), C17**: in the survey's tables the loss is mostly in evaluations (7 of 8 rows), with time split 5–3 (card's count), plus a stated reliability gap [S049 pp. 15–16] (the first wording, *in evaluations, not in time*, was corrected after review); the 1989 recommendation of PQN in numbers is in #method-6.
- **Mark 8 (honest scope)**: the 2003 abstract says all codes show much room for improvement [S078 p. 1]; the scale-up claim carries its sample size: "Our set of inequality constrained problems contained 30 problems with more than 1000 variables, and only 6 problems with more than 10,000 variables." [S078 p. 15].


**Increment inc-book (2026-10-17)** (book material B001–B012, cards c5-01 to c5-03: the open parts of *Numerical Optimization*, its errata, two reviews, the authors' book pages and Springer's catalogue pages; joint voice of Nocedal and S. J. Wright unless marked; dating and framing only, never in a say–do count; 08 §13, #textbook).
- **Mark 1 (a place in a subroutine library; methods suited to practice)**: the authors' web description of the book, identical on the first-edition page (2002 capture) and the second-edition page (2006), says it responds to the field "by focusing on the methods that are best suited to practical problems" [B011 pp. 1–2]; the base tier quotes it (02 W1), and the 2002 capture now dates it to the first edition. The 2006 edition adds *Perspectives and Software* sections on the state of the art in software [B001 p. 22], where the 1999 edition had left out specific packages [B005 p. 9]. Joint; fails exclusivity against Wright's Method 2 and taste mark 1.
- **Mark 3 (scale is the test)**: the 1999 preface states an emphasis on large-scale techniques (interior-point, inexact Newton and limited-memory methods, partial separability, automatic differentiation) [B005 p. 7]. Joint framing.
- **Mark 4 (self-correction)**: both editions index self-correction under the BFGS method [B006 p. 50; B002 p. 57]; the body pages were not read.
- **Mark 8 (honest scope)**: both prefaces name what the book leaves out and where to read it [B005 p. 8; B001 p. 22]; one item of the second-printing errata strips the words *minor* and *slightly* from a stated weakness [B008 p. 3] (weak: one item, and the weakness itself was not read). Joint; Wright's taste mark 7 (honest scope) covers the same ground.

---

<a id="taste-warnings"></a>
## Taste: warning signs of bad research

**Base-tier text (verbatim, SKILL.md of 2026-09-28):**

#### Warning signs of bad research
1. A method whose appeal exists only on paper [02 T3].
2. A bound, or global convergence alone, that would equally bless steepest descent [02 T4].
3. Complexity as the reason to prefer a method (Method 5) [02 T6].
4. No comparison against the obvious simple baseline [02 E4].
5. An irrevocable commitment to an estimate (noise level, curvature, penalty parameter) with no recovery [02 R8].
6. A generic method, even a famous one, where structure is available [02 E8].
7. Code rankings from one test set; untuned competitors; mismatched stopping tests [02 E3; 03 §2.2].
8. A contested claim stated as settled. His own lapse: "as is well known, sharp minima lead to poorer generalization" (arXiv:1609.04836) [05 §7].

**Full-text evidence (2026-10-17):**

- **Warning 2 (a bound that would bless steepest descent)**: his own non-discriminating theorems: global convergence of the shipped hybrid asserted by analogy [S013 pp. 2, 4]; a safety-net theorem valid for any μ rule [S029 pp. 10–12, 22]; convergence for any positive definite Hessian sample [S023 pp. 5, 7, 11]; an O(1/k) theorem that H_k = I also satisfies [S015 pp. 12–14, 29]. The group says so itself: "where the provable convergence rate for L-BFGS is no better than for steepest descent, even though L-BFGS is superior in practice." [S038 p. 14].
- **Warning 8 (contested claim stated as settled)**: the sharpness–generalization link adopted as well known [S006 pp. 1, 3–5] (already recorded in the base tier from 05 §7).
- **Warning 9 (new: simplified iteration offered for the shipped method)**: from 2012 the analysed iteration is often a simplified one, and the papers name the gap: "The focus of this section is on the development of a practical algorithm, not on establishing complexity bounds, and therefore our method is an extension of Algorithm 3.1 and not of the idealized variant given by (4.23)-(4.24)." [S018 p. 15]; H_k = I with plain backtracking in the theory of a method run with L-BFGS [S038 pp. 12, 19]; an outline algorithm [S071 pp. 10–12]; a stripped SQP [S084 pp. 2, 4–5, 15]; an idealized test [S102 pp. 7–14]; an over-cautious setting [S128 pp. 9, 11]; a fixed step and an extra test [S031 pp. 5, 12]. Kept as a warning sign (state the gap), not as a recommendation (08 §6, *component-isolating analysis on a simplified iteration*).


**Increment inc-ocr (2026-10-17)** (round-4 cards c4-01 to c4-04 and s4-01, second reads from an OCR text layer; one piece of evidence with each work's earlier card; numbers from the round-4 cards; 08 §12). **Warning 9**: in 2000 the gap between the analysed and the shipped interior method is named only in part [S009 pp. 8, 10, 17; S008 pp. 10, 17, 19] (#method-5); in 1997 the analysed iteration is called an idealization of the coded one [S046 p. 5]; in 2004 the uncovered cases are stated (backtracking, μ fixed) [S061 pp. 8, 17].


**Increment inc-book (2026-10-17)** (book material B001–B012, cards c5-01 to c5-03: the open parts of *Numerical Optimization*, its errata, two reviews, the authors' book pages and Springer's catalogue pages; joint voice of Nocedal and S. J. Wright unless marked; dating and framing only, never in a say–do count; 08 §13, #textbook).
- **Warning 3 (complexity as the reason to prefer a method)**: both editions index complexity of algorithms only on the linear-programming pages [B006 p. 50; B002 p. 57], and both appendices set a pessimistic worst-case growth bound for Gaussian elimination beside the practical verdict, "stable for all practical purposes" [B006 pp. 34–35; B002 p. 20]. Joint framing, consistent with the warning; Wright's taste mark 1 says the same, so it adds nothing Nocedal-specific.

---

<a id="taste-quick-check"></a>
## Taste quick-check

**Base-tier text (verbatim, SKILL.md of 2026-09-28):**

#### Taste quick-check
- [ ] Would the result change a default, option, safeguard or termination test in a production solver, using only information users have?
- [ ] Was it compared against the dismissed simple option, with the scales tipped against yourself?
- [ ] Does the theory separate a method known to work from one known to fail, with the bound plotted against runs?
- [ ] Does the algorithm detect when its own estimates are wrong, and recover?
- [ ] Does the problem's structure make your favourite method the wrong choice?
- [ ] Are limitations and known failure modes written down?

Four or more "yes" answers fit this lens; a "no" to the second or third is where he would push back first.

**Full-text evidence (2026-10-17):**

- Item 7 (sampled methods only) added with Method 7. The threshold line is unchanged.

---

<a id="method-1"></a>
## Method 1: Handicapped, method-level benchmarking

**Base-tier text (verbatim, SKILL.md of 2026-09-28):**

#### Method 1: Handicapped, method-level benchmarking (tip the scales against yourself)
**One line**: Compare methods, not brands. Take the baseline from the rival community's own benchmark, align stopping tests and budgets (even by editing your own code), handicap your own method, and print the losses and limits.
**Evidence**:
- Stated (co-authored, 2003): "our goal is to assess the effectiveness of optimization methods … and not simply to evaluate the performance of specific software implementations" (doi:10.1007/978-3-642-55508-4_10) [02 E3]. UCLA 2021, caption-derived: "let's try to force our algorithm to be as dumb as possible" [03 §2.2].
- Practice: "In order to make the algorithm as close as possible to cobyla, we set the memory size of L-BFGS updating to its minimum value, t = 1 (lmsize=1)." (arXiv:2102.09762 p. 27). Competitors' step lengths tuned over a grid, his own method untuned (arXiv:1802.05374) [03 §2.1–2.2].
- Practice, the 2003 protocol (LOQO, KNITRO, SNOPT, filterSQP; preprint pp. 6–7, 10): "we modified KNITRO's stopping test to be almost identical to that of SNOPT"; "all their default settings"; 10⁻⁶ for all codes; 30 CPU minutes and 1000 major iterations, a limit reached counted as failure; CPU times only for n > 100 (set-up costs dominate small problems), but "Function evaluations are reported for all problems"; LOQO's one unnecessary evaluation per iteration discounted. SNOPT's quasi-Newton Hessian, "an undesirable disparity", became a question: "We will nevertheless take advantage of this difference to assess the effectiveness of quasi-Newton approximations" (p. 7). The verdict includes KNITRO: "all codes show much room for improvement" (abstract) [03 §2.2].
- Recurrence: 1999, NITRO and LANCELOT both stopped at 10⁻⁷ (preprint p. 20) → 2003, the protocol above → 2008, three algorithms inside one code base → 2021, lmsize = 1.
- Say–do consistency: ✅ stated + practised, 1989–2024.
**Steps**:
1. **Take the baseline from the rival community's own published benchmark and say why**; if weaker, say so and upgrade it in revision [03 §2.1].
2. **Write to the rival school before fixing the protocol**: seven DFO researchers are thanked "for their correspondences that led to the design of the experiments in this work" (arXiv:2102.09762 p. 32).
3. **Handicap your own side**: minimal memory, the simplest variant, untuned parameters. Give competitors tuning grids, and rerun the rival at non-default settings in an appendix.
4. **Align termination tests and budgets**, even by editing your own code. Hitting a limit counts as a failure. Correct accounting artefacts in the rival's favour.
5. **Control implementation effects**: compare methods inside one code base "to minimize the effect of implementation details" (doi:10.1007/978-3-540-79409-7_18). When Hessian information differs, name the disparity and turn it into its own question (2003, preprint p. 7).
6. **Use few codes and understand them.** Write a limitations section (one code per class, default options, one noise model) [03 §6].
7. **Put losses in the abstract and full results in an appendix.** Show typical-behaviour problems together with aggregate performance or data profiles. Report CPU time only where set-up cost does not dominate; count evaluations everywhere.
   - 🔴 Stop if your method got tuning the competitor did not, or if the stopping tests differ. Stop if illustrative problems have no aggregate behind them; his own 2024 paper shows 3 of "over 50" problems with no aggregate [03 §3.2].
**Applies to stage**: experiment design; judging results; writing.
**Different from standard practice**: usually one's own method is tuned and competitors run at defaults; here the scales tip against yourself.
**Limitations**: KNITRO was both platform and comparator (2008, 2021, 2024), with no conflict-of-interest statement [03 C3]; a 1997 web page ranks codes [03 C6]; rival authors' benchmarks rated NITRO/KNITRO lower on their terms [05 §4.2–4.4]. Early-career users should declare the handicap, or reviewers may read it as a weak implementation.

**Full-text evidence (2026-10-17):**

**Full-text evidence (08 §2.1).** Distinct works: 51 evidence (47 full or partial), 34 variant, 7 contradiction; 71 works with any link (67 full or partial); 77 card entries. (08 counts every read level; SKILL.md uses the regenerated list at the end of this section.)

- **Strongest full-text evidence**: the 2002 SLIQUE study builds the rival-aligned stopping test a year before the 2003 protocol: "Although, it is nearly impossible to enforce a uniform stopping condition, the stopping conditions for SLIQUE and KNITRO were constructed to be very similar to that used in SNOPT." [S035 report p. 19]; limits count as failures, SNOPT gets a larger superbasics limit, SNOPT's exits flagged optimal without the requested accuracy are not counted as successes, and the loss to the group's own KNITRO is printed (438, 506 and 455 of 560 solved by SLIQUE, KNITRO, SNOPT) [S035 report pp. 19–21; round-2 card c2-01].
- The 2003 benchmarking study confirms the base wording (method-level goal, stopping test aligned by editing the own code, accounting corrections, own losses printed), though its numbers are unreadable in the file [S078 pp. 2, 6–7, 9–11, 14–15]: the 2003 figures in SKILL.md (10⁻⁶, 30 CPU minutes, 1000 major iterations, n > 100) still rest on the preprint read in the base tier. *(Superseded by increment inc-ocr, C15: the OCR text is legible and confirms each figure [S078 pp. 6–7].)*
- 1989: competitors run "precisely as they recommend", same-solution check, losses in the abstract, full data in a companion report [S002 pp. 2, 7–8]; 1992: methods compared inside one code differing only in β [S012 p. 24]; 1999: NITRO and LANCELOT stopped at the same 10⁻⁷ [S008 pp. 20–23] *(inc-ocr: one tolerance value on different measures, which the paper calls very similar [S008 p. 20]; C16)*.
- Handicaps of the own side: rival credited with its best of 11 preconditioners (1998) [S034 p. 22]; a rival-neutral target from a derivative-based reference solve, medians of five runs, the bias against the rival named (2002) [S040 pp. 12–13, 15]; own method untuned against SG and SVRG tuned on a 21-point grid (2018) [S031 p. 6]; own CG parameters fixed in advance, rival given a step-length grid (2019) [S032 arXiv pp. 22, 24, 26]; sketching costs ignored, "the most optimistic for Newton-Sketch" (2020) [S041 p. 6]; KNITRO L-BFGS memory 1, rival codes from their communities' own benchmarks, the rival rerun at non-default settings (2021) [S080 arXiv pp. 4, 19, 27–28, 42–44].
- Compare inside one code base: Knitro/Direct against Knitro-CG sharing all other components [S013 p. 14]; interior codes taken from Knitro "to minimize the effect of implementation details" [S105 p. 3]; old and new infeasibility logic identical except the switch rule [S053 pp. 12–13].
- **Say–do**: stated and practised 1989–2026 [S002 p. 8; S150 pp. 6–8], not uniformly. The early L-BFGS-B papers run the rival only at defaults and count non-converged runs whose f matches the rival's as non-failures: "We do not interpret these as failures of the algorithm, but feel that this property of L-BFGS deserves further study" [S005 p. 9; S143 pp. 8–9; S003 pp. 18–23] *(inc-ocr correction: S003 has no such marker; every miss is printed F1 or F2 and counted as a failure [S003 pp. 19–20, 23]; the C1 marker first appears in the code report [S005 pp. 10–11])*. Step 4 holds from 2002 on [S035 report p. 19; S013 p. 14; S139 p. 15]. Before 2016 the self-handicap (step 3) appears in some papers (S034 p. 22: LANCELOT credited with its best of 11 preconditioners; S035 report p. 19: SNOPT's superbasics limit raised; S040 admits a stopping test biased against DFO but does not handicap its own side) and regular in the 2016–2023 sampling and noise papers (S089, S031, S032, S041, S080). Step 7's stop rule (illustrative problems with no aggregate) is met in many papers that state their scope [S052 p. 16; S051 pp. 24–29; S064 preprint p. 19; S004 p. 17; S082 pp. 18, 20; S084 pp. 15–16; S124 p. 29].
- **Contradictions (7 works)**: failure accounting [S005 p. 9]; the simple baseline (plain L-BFGS, one end of the family) has no column [S077 pp. 4, 9–11]; two efficiency claims without a table [S042 pp. 13, 20]; own parameters swept, baseline fixed, one problem [S023 pp. 12–17]; illustrative runs with no aggregate [S082 pp. 18, 20, 27–34; S084 pp. 15–16; S124 p. 29].
- **C7** (version-dependent loss placement): see #taste-marks.
- **Limitations confirmed**: KNITRO as platform and comparator, with an Artelys co-author and no conflict-of-interest statement [S080 arXiv pp. 1, 27]; KNITRO also as the baseline and subproblem solver in 2026, the rival DFO codes excluded on stated grounds [S150 pp. 6–7]; the group's own KNITRO as comparator in 2002 [S035 report pp. 18–19].
- Techniques: stratify outcomes before profiling [S080 arXiv pp. 28–29]; same-solution filter with the number dropped per code [S002 p. 8; S012 p. 24; S029 p. 7] *(inc-ocr, C14: S002 checks only, S012 drops, S029 drops and counts)*; CPU time only where set-up cost does not dominate [S013 p. 14; S003 p. 23; S139 p. 18] (technique catalog §3).

**Increment inc-ocr (2026-10-17)** (round-4 cards c4-01 to c4-04 and s4-01, second reads from an OCR text layer; one piece of evidence with each work's earlier card; numbers from the round-4 cards; 08 §12). Say–do count regenerated: 68 works (47 evidence, 39 variant, 7 contradiction), was 67 (46, 34, 7): S003 gains an evidence link; S002, S008, S021, S024 and S101 gain variant links; S021 is newly linked. S021's variant link rests partly on reporting slips (below); the generator counts it, and SKILL's count line flags it (after review).

- **C15, the 2003 protocol in numbers**: 509 problems, a subset of the 740 in the Benson–Vanderbei AMPL translation of CUTE as of December 2000, all codes at defaults, a Sun Ultra 5 [S078 pp. 6–7]: "A limit of 30 minutes of CPU time, and 1000 major iterations, were imposed for each problem; if one of these limits was reached the code was considered to have failed." [S078 p. 7]; a tolerance of 10⁻⁶ on all solvers [S078 p. 7]; KNITRO's stopping test edited to be almost identical to SNOPT's [S078 p. 6]; CPU times for problems with more than 100 variables [S078 p. 6], while p. 9 and Table 1 use n ≥ 100; runs from fall 2000, when no second-derivative SNOPT existed [S078 p. 7]. Table 1 (problems solved): KNITRO 1.00 loses both unconstrained rows to LOQO (145 against 171 of 187; 67 against 83 of 95 with n ≥ 100) and leads the equality rows and the general n ≥ 100 row [S078 p. 15]. The card's totals over the 509 problems (LOQO 446, KNITRO 440, SNOPT 403, filterSQP 397) are the card writer's sums; the paper prints no total.
- **C14, the same-solution filter**: the 1989 study verifies that both methods reached the same solution point in each run and reports no dropped problem and no count [S002 p. 8]; the drop is in the 1992 CG paper [S012 p. 24], drop and count (37 problems for IPOPT, 54 for KNITRO) in the 2009 barrier study [S029 p. 7].
- **Failure accounting, sized**: the C1 marker (gradient test missed, f at least as good as LANCELOT-SR1's) covers 3 of 34 unconstrained runs at m = 5 (FLETCHBV, FREUROTH, PENALTY3) and 5 of 67 runs at m = 17; it is applied to LANCELOT-Hessian too (PENALTY3), and all five bound-constrained misses at m = 5 are printed F1 [S005 pp. 9–11]. The evaluation limit rose from 999 [S003 p. 19] to 9999 [S005 pp. 10–11]. The 1995 algorithm paper has no C1 marker: every miss is printed F1 or F2 and counted as a failure [S003 pp. 19–20, 23] (correction to the Say–do bullet above and to 08 §2.1).
- **Rivals as their authors recommend, with the values**: the Buckley–LeNir code at its defaults with the line-search constants its authors recommend (β′ = 10⁻⁴, β = 0.9), L-BFGS with the same values [S002 p. 8]; LANCELOT's SBMIN in its BFGS, SR1 and exact-Hessian options at defaults [S003 p. 19]; LANCELOT with second derivatives at defaults [S008 p. 20]; one projected-gradient test at 10⁻⁵ for both codes [S003 p. 18; S005 p. 8].
- **Variant, nominal alignment** (the ⚠ C15 bullet in SKILL.md): in 1999 one tolerance value (10⁻⁷) on different measures, which the paper calls very similar, with the aggregate verdicts in words and the CPU losses of 22–52× on SVANBERG, OBSTCLAE and TORSION1 unremarked in §4 [S008 pp. 20–21]; in 1998 the ranking of line search against pure trust region is stated in function evaluations (1125 against 986, card's sums), where the gradient count (902 against 986) would reverse it, both counts being printed [S024 p. 21]; in 1998 the new norm gets its own subproblem solver (HSL_VF06) while the rival norms run HSL_VF05 at defaults, so the CPU columns mix norm and solver, as the authors say [S101 p. 11]; in 1996 the survey's rows are a declared selection from S005's tables, which it does not summarise [S049 pp. 15–16; S005 pp. 10–11].
- **Evidence, controlled arms**: DINEMO and its ablation arm share the line search (c2 = 0.9), the Newton schedule (iterations 6, 16, 26, …), m = 29 and maxcg = 20, and differ only in discarding the inner pairs [S088 p. 8]; one trust-region algorithm with one parameter set for all three norms, bold only for a margin of at least 10%, † for different local minimizers: "We indicate those cases where one or other method performs at least 10% better than its competitors by highlighting the relevant figure in bold." [S101 p. 12]; four arms in one Fortran code with Δ₁ = 1, B₁ = I and ‖g‖ ≤ 10⁻⁸ [S024 pp. 19–20].
- **Losses printed, now sized**: at m = 5, 4 of 34 L-BFGS-B runs fail; on the largest bound problems L-BFGS-B needs 13–47 times LANCELOT's evaluations (card's ratios) while being faster on 12 of the 15 rows with n ≥ 100 (card's count) [S003 pp. 20, 22]; NITRO fails on 3 of 56 Hock–Schittkowski problems [S008 p. 24].
- Not used: the card's reading notes on reporting slips inside S021 (an unmarked table cell, 28 rows against 29 in the text) [S021 pp. 22–26]; they count toward the mechanical variant link below but are not used as evidence (header rule).
- Mark unchanged: ✅ stated + practised 1989–2026, the early form weaker on failure accounting.

**All card links** (regenerated 2026-10-17 for increment inc-ocr from the digests' `method_links`, with the SKILL.md counting rule: full or partial cards only; abstract- and metadata-level cards, NSF award records and the group-voice S063, S179, S188 listed apart and not counted; S126 counted with S042 and S056 with S143; for the six works upgraded in round 3 only the deeper card is used; the earlier and later cards of the 26 twice-carded works (ten re-read in round 2, sixteen in round 4) are labelled by batch, one work each, round-1 pages prose only). Counted: 68 works, 82 card entries:

- **Evidence** (47 works, 57 card ids): S002 pp. 2, 7–8, 12 (c01); S002 pp. 2, 8, 19–20 (c4-01); S003 pp. 18–20, 23 (c4-02); S005 p. 8 (c02); S005 p. 8 (c4-02); S008 pp. 20–23 (c03); S008 pp. 20–24 (c4-03); S012 p. 24; S016 preprint pp. 1–2; S024 pp. 19–20 (c03); S024 pp. 19–20 (c4-02); S027 pp. 20, 24–25; S029 pp. 6, 13–17; S030 pp. 12, 15–16 (c2-01); S030 pp. 8, 10, 12 (s03); S031 p. 6; S032 arXiv pp. 22, 24, 26; S033 p. 7; S034 p. 22; S035 report pp. 19–21 (c2-01); S035 report pp. 19–21 (s04); S036 pp. 20, 27; S038 pp. 5, 19–21; S040 pp. 12–13, 15, 18 (c2-01); S040 pp. 12–15, 18 (s03); S041 pp. 6, 8–9, 21, 23; S043 pp. 2, 7–8; S045 pp. 16–17; S050 p. 13; S051 p. 26; S053 pp. 3–4, 12–13, 17; S057 p. 2 (s03); S060 pp. 17–18, 20–21; S062 pp. 4, 6–8; S064 preprint pp. 17, 19; S068 pp. 19–21; S071 pp. 17–19, 21, 23–25; S073 pp. 23–25; S075 p. 19 (s04); S075 pp. 17–25 (s2-01); S076 pp. 10, 13; S077 pp. 8, 10 (s2-01); S078 pp. 2, 6–7, 9–11, 14–15 (c04); S078 pp. 6–7, 10, 14–15 (c4-04); S080 arXiv pp. 1, 4, 7, 10, 12, 19, 22, 27–30, 32, 42–44; S082 p. 21; S087 pp. 12, 15, 19; S088 p. 8 (s02); S088 pp. 8–9, 12 (s4-01); S089 pp. 3, 10, 13; S091 arXiv pp. 17–19, 31; S092 pp. 10, 13; S098 p. 8 (s03); S101 p. 14 (s02); S105 pp. 1, 3; S110 pp. 7–8; S113 p. 10.
- **Variant** (39 works, 41 card ids): S002 pp. 8, 12 (c4-01); S003 pp. 18–23 (c02); S003 pp. 19–22 (c4-02); S004 pp. 4, 17–19; S006 pp. 3–4, 13–14; S007 p. 9; S008 pp. 20–21, 23–24 (c4-03); S013 p. 14; S015 pp. 1, 14–16, 25–27; S016 preprint p. 3; S018 pp. 18–25; S021 pp. 22–26 (c4-03); S024 pp. 20–21 (c4-02); S030 p. 3 (c2-01); S031 pp. 7–8; S035 report pp. 18–19 (c2-01); S038 pp. 4–5; S040 pp. 13, 15 (c2-01); S041 pp. 9, 16–17; S043 p. 7; S049 pp. 15–16 (c03); S049 pp. 15–16 (c4-02); S051 pp. 24–29; S052 pp. 16–21; S064 preprint p. 19; S067 pp. 17–19 (s2-01); S071 pp. 16–17; S076 p. 14; S080 arXiv pp. 1, 6; S081 pp. 15–16; S085 pp. 7–8; S087 pp. 17–18; S089 p. 9; S092 p. 13; S101 pp. 11–14 (s4-01); S102 pp. 14–15, 17–26; S105 p. 4; S128 pp. 10, 13; S139 pp. 14–15, 18; S143 pp. 8–9; S150 pp. 6–8, 13, 18.
- **Contradiction** (7 works, 9 card ids): S005 pp. 9–11 (c02); S005 pp. 9–11 (c4-02); S023 pp. 12–17; S042 pp. 13, 20; S077 pp. 3, 8–11 (s03); S077 pp. 4, 9–11 (s2-01); S082 pp. 18, 20, 27–34; S084 pp. 15–16; S124 p. 29.
- **Not counted** (abstract- or metadata-level, award records, group voice): evidence: S025; S100; S198 (award); S204.

---

<a id="method-2"></a>
## Method 2: Put the field's received wisdom on trial

**Base-tier text (verbatim, SKILL.md of 2026-09-28):**

#### Method 2: Put the field's received wisdom on trial
**One line**: List what the field treats as necessary or settled, check whether anyone actually compared against the dismissed simple option, then test it with the simplest implementation and scope the verdict.
**Evidence**:
- Stated: "rarely in the literature of derivative-free optimization do people say, 'Well, let me compare with finite difference Quasi-Newton updating.' It's almost never done, right?" (Simons 2017, uploader subtitles) [02 E4]. Co-authored abstract: "The test results presented in this paper suggest that such views should be re-examined" (arXiv:2102.09762).
- Practice: "We find, to our surprise, that omitting the geometry phase does not seem to harm the efficiency and robustness of our algorithm" (doi:10.1080/10556780802409296, preprint p. 2). Also finite-difference quasi-Newton for noisy DFO (doi:10.1137/18M1177718), L-BFGS for machine learning (arXiv:1802.05374), line searches under noise (doi:10.1137/24M1632279) [03 §2.6].
- Say–do consistency: ✅ stated + practised, 2009–2025.
**Steps**:
1. **Write down the received wisdom in the field's own words**, e.g. "It is common practice to avoid line searches when minimizing noisy functions" (arXiv:2401.15007 v2, p. 10).
2. **Check whether anyone actually compared against the dismissed option.**
3. **Build the simplest version** that drops the safeguard or uses the dismissed tool: "we choose to work with the simplest possible algorithm" (2009, preprint p. 4).
4. **Run noise-free first, then perturbed** (Heuristic 3). Ablate one component at a time, and vary the key parameter both ways (the difference interval h at 10⁻¹, 10⁻², 10⁻³).
5. **Record surprise as surprise, and print where the rival still wins**: "newuoa is more efficient and accurate than the finite-difference l-bfgs method … but not by a wide margin" (arXiv:2102.09762).
6. **Scope the verdict**: "Perhaps it may be preferable to employ it only as a method of last resort; not as an integral part of the algorithm" (2009, preprint p. 9).
   - 🔴 Stop and narrow the claim if the evidence covers one noise model, a narrow range of dimensions (2009: n = 2–15) or one rival code. Name that limit in the abstract or a limitations section.
**Applies to stage**: problem choice; algorithm design; experiments.
**Different from standard practice**: Gould and Wright also re-test folklore; Nocedal targets dismissed *simple classical tools*, with Method 1's handicaps.
**Limitations**: his verdict on model-based DFO moved four times, from dispensable geometry (2009) to "more robust in the presence of noise than we expected" (2021) and a model-based constrained method (doi:10.1016/j.orl.2025.107398) [03 C2]. PDFO (doi:10.1007/s12532-024-00257-9) and Full-Low (doi:10.1080/10556788.2022.2142582) press his assumptions of a known noise level and smoothness [05 §5]. Early-career users can frame contrarian work as a numerical study.

**Full-text evidence (2026-10-17):**

**Full-text evidence (08 §2.2).** Distinct works: 25 evidence (22 full or partial), 10 variant, 0 contradiction; 34 works with any link; 37 card entries. (08 counts every read level; SKILL.md uses the regenerated list at the end of this section.)

- **Strongest full-text evidence**: the geometry phase dropped [S062 pp. 2, 4–5, 7, 9]; finite-difference BFGS against direct search and interpolation, with a result recorded as contrary to conventional wisdom [S038 pp. 6, 21]; the dismissal of finite differences tested with the simplest h, the rival's wins printed, the verdict handed to others to check [S080 arXiv pp. 4, 6, 9, 11]; the LP corrector folklore tested by removing its hidden ingredient, PCx falling from 90 to 28 of 94 [S029 pp. 17, 20]; the huge-fixed-penalty heuristic tested, 485 → 449 (ν = 10⁵) → 321 (10¹⁰) of 616 [S042 pp. 15–16]; the fashionable stochastic inner solver against CG, the classical tool winning [S041 pp. 2, 7–8]; the view that SGD is to be preferred put on trial [S018 pp. 6–7, 14]; the common practice of avoiding line searches tested both ways [S128 pp. 10–13].
- **Stated, written** (replaces the spoken Simons quote as the Stated line in SKILL.md; the spoken quote stays in the base-tier text above): "We believe that if such comparisons had been made, particularly in the noiseless setting, research in the field would have followed a different path." [S080 arXiv p. 4]; and the received view put in the field's words: "A common view in optimization is that finite difference gradient approximations should be avoided in the noisy setting." [S128 p. 11].
- **Say–do (C8)**: the base tier dates the practice 2009–2025. The full texts push it back: plain BFGS beats the self-scaling refinement on most problems (1993) [S054 p. 16]; the comforting view that Jacobian regularization removes the difficulty is stated and refuted on the simplest example (2004) [S061 pp. 11–12]; does the penalty need updating at all? (2006) [S027 pp. 7, 22]. Mark: ✅ stated + practised 1993–2026.
- **Variant: the dismissed option can be a method that theory favoured but nobody implemented carefully.** 1990, as PI: "However we believe that conjugate gradient methods have not been properly implemented so far, and that their full potential needs to be assessed." [S197 p. 4]; a careful implementation of one theory-only trust-region SQP class [S034 p. 22; S028 p. 34]; SLP-EQP revived because million-variable LP codes had become available [S035 report pp. 2, 4]; FIBO rehabilitated by auditing why the earlier evidence failed (accounting of finite-differenced constraints, a weak baseline) [S150 pp. 2, 6, 9]: "The numerical results reported in [6], and subsequently in [4], are, however, inconclusive and the FIBO approach is rarely (if ever) used in practice." [S150 p. 2].
- **Moving DFO verdict**: a 2002 point precedes the base list: the wedge method enforces geometry at every step, and finite-difference L-BFGS-B loses on reliability (five failures against one, round-2 card) [S040 pp. 2–3, 7, 15]. Endpoint: model-based DFO for constraints in 2026 [S150 pp. 1–3, 5].
- **Other variants**: received safeguards rejected by argument rather than experiment [S019 p. 7; S071 p. 6]; the classical tool defended against a newer challenger [S032 arXiv pp. 3, 27]; the sharpness–generalization link adopted as well known [S006 pp. 1, 3–5] (taste warning 8).

**Increment inc-ocr (2026-10-17)** (round-4 cards c4-01 to c4-04 and s4-01, second reads from an OCR text layer; one piece of evidence with each work's earlier card; numbers from the round-4 cards; 08 §12). Count unchanged: 31 works (22 evidence, 10 variant, 0 contradiction); three more card entries.

- **The 2004 refutation in numbers**: regularized Newton on Example 1 from (1.7, 0.1) over ρ = 0, √macheps, 10⁻⁴, 10⁻² and 10⁻¹: ρ = 0 fails in the line search after 25 iterations; every ρ > 0 hits the 1000-iteration limit, the best final ‖F‖ being 1.629e−04 against a 10⁻⁶ test; SVD regularization with ρ = 0.1 ends O(10⁻²) from the solution after 1000 iterations [S061 p. 12]; MINPACK's LMDER from the same start: "The Levenberg-Morrison-Marquardt method was very efficient … in this example, taking only 12 iterations to solve the problem to the prescribed accuracy." [S061 p. 13].
- **Variant (surprise reversal, now complete)**: TR+BT SR1 needs fewer iterations and evaluations than TR+BT BFGS on all 8 medium problems of Table II after losing in Table I [S024 pp. 21–22].
- Mark unchanged.

**All card links** (regenerated 2026-10-17 for increment inc-ocr from the digests' `method_links`, with the SKILL.md counting rule: full or partial cards only; abstract- and metadata-level cards, NSF award records and the group-voice S063, S179, S188 listed apart and not counted; S126 counted with S042 and S056 with S143; for the six works upgraded in round 3 only the deeper card is used; the earlier and later cards of the 26 twice-carded works (ten re-read in round 2, sixteen in round 4) are labelled by batch, one work each, round-1 pages prose only). Counted: 31 works, 37 card entries:

- **Evidence** (22 works, 25 card ids): S018 pp. 6–7, 14, 24; S027 pp. 7, 22; S029 pp. 17, 20–21; S031 pp. 1, 4, 6–8; S036 pp. 6–7, 20–23; S038 pp. 6, 21; S041 pp. 2, 7–8, 17; S042 pp. 7, 15–16; S043 pp. 3, 6–7; S050 pp. 12, 16–17; S054 p. 16; S061 pp. 11–12 (c04); S061 pp. 11–12 (c4-04); S062 pp. 2, 4–5, 7, 9; S071 pp. 16–17, 21; S075 pp. 17–18 (s04); S075 pp. 17–18 (s2-01); S076 pp. 6–7; S080 arXiv pp. 4, 6, 9, 11, 14–15, 20, 38–40; S087 p. 5; S091 arXiv pp. 1, 19; S110 pp. 1, 5–8; S126 p. 15 (= S042); S128 pp. 10–13; S150 pp. 2, 5–9.
- **Variant** (10 works, 13 card ids): S004 pp. 4, 15–19, 34–37, 40, 49; S006 pp. 1, 3–5; S011 p. 5; S019 pp. 7, 15, 27 (c02); S019 pp. 7, 17, 31 (c4-01); S024 p. 22 (c03); S024 pp. 21–22 (c4-02); S026 pp. 13–15; S032 arXiv pp. 3, 24, 27; S040 pp. 2–3, 7, 15 (c2-01); S040 pp. 3, 15 (s03); S057 pp. 18, 24 (c2-01); S071 p. 6.
- **Contradiction** (0 works, 0 card ids): none.
- **Not counted** (abstract- or metadata-level, award records, group voice): evidence: S152; S167 (award); S169 (award).

---

<a id="method-3"></a>
## Method 3: Keep the classical engine; repair only the component that breaks

**Base-tier text (verbatim, SKILL.md of 2026-09-28):**

#### Method 3: Keep the classical engine; repair only the component that breaks, from an explicit estimate with a recovery path
**One line**: Run the trusted method in the new regime, name the component that fails, and make only that component regime-aware, driven by an explicit estimate (the noise level; the best feasibility progress attainable) and backed by recovery and exit flags.
**Evidence**:
- Stated: "we're gonna have to be adaptive. … The algorithm are gonna have to find out when they make a mistake, go back and correct what they are doing." (Simons 2017, uploader subtitles) [02 R8]. Co-authored abstract: "adapting classical deterministic methods. These adaptations follow certain design guidelines described here, which make use of estimates of the noise level in the problem" (arXiv:2401.15007).
- Practice: "The classical BFGS and L-BFGS methods can fail in such circumstances because the updating procedure can be corrupted and the line search can behave erratically" (arXiv:2010.04352), repaired by lengthening the curvature pairs; a noise-relaxed trust-region ratio (doi:10.1007/s10107-023-01941-9); "the performance of the method deteriorates substantially when the Recovery procedure is not used" (arXiv:1803.10173 v2, p. 21); a "Reached noise level of the function" exit flag in the group's code [03 §2.5–2.6]. Earlier, outside noise: penalty steering (worked case below).
- Say–do consistency: ✅ stated + practised, 2007–2025.
**Steps**:
1. **Run the classical method** (BFGS/L-BFGS, trust region, Byrd–Omojokun SQP) in the new regime and **name the failing component** (update, line search, ratio test, difference interval).
2. **Show the failure on an easy, deliberately chosen problem with an internal diagnostic** (Heuristic 1).
3. **Replace only that component** with a version driven by an explicit estimate of the noise level (ECnoise, doi:10.1137/100786125) or curvature: lengthened difference spacing, a relaxed acceptance ratio, an interval set from the noise estimate. Exemplar (equality-constrained SQP): "by introducing a relaxation in the line search procedure while keeping all other components of the SQP method unchanged" (arXiv:2110.04355, p. 3).
4. **Add a recovery tree and exit flags**: "You estimated the noise wrong. In this case, why don't you re-estimate the noise? … maybe just the line search set you off" (Simons 2017, uploader subtitles) [03 §3.5].
5. **Ablate the repair and the recovery** to show they earn their cost: "when the relaxation is disabled, the line search often fails in a neighborhood of x*" (arXiv:2110.04355, p. 18).
6. **Prove convergence to a noise-determined neighbourhood and plot the bound against runs** (Method 5). Theory and the practical algorithm may come as two papers (arXiv:1901.09063 → arXiv:2010.04352).
   - 🔴 Stop if the design needs a constant users cannot know: existing procedures for estimating Lipschitz-type bounds "are not robust" (arXiv:2102.09762, App. A). Estimate what can be estimated and let recovery handle the rest.
**Applies to stage**: algorithm design; debugging.
**Different from standard practice**: others switch paradigm (interpolation, direct search, stochastic methods); he keeps the deterministic engine. PDFO's authors argue the opposite [05 §5.2].
**Worked case: penalty steering** (Byrd, Nocedal & Waltz, OTC preprint 10 Apr 2007; *OMS* 23, 2008, doi:10.1080/10556780701394169; practice, co-authored) [05 §4.6]:
- *Diagnosis*: Sℓ1QP-type methods "were never incorporated into production-quality software. We conjecture that this was mainly due to the difficulties of choosing the penalty parameter" (preprint p. 5). A huge fixed ν "is not to be recommended because excessively large penalty parameters can lead to inefficient behavior, damaging roundoff errors, and failures" (p. 7).
- *Engine kept, one component replaced*: the ℓ1-penalty SQP / SLQP step stays; ν is set against an auxiliary LP (the subproblem with ν = ∞), which gives the best reduction in linearized infeasibility inside the trust region. Guidelines: reach linear feasibility when attainable, else at least a fraction ε1 of the best reduction; then raise ν until the model decrease is at least ε2·ν times the feasibility gain (pp. 9–10).
- *Numbers as defaults* (Heuristic 5): Knitro-Active (Knitro 4.0) uses ν0 = 10, ε1 = 0.1, ε2 = 0.5, multiplying ν by 10 and re-solving until the conditions hold (p. 13). The extra LPs cost "less than three percent of the total number of simplex iterations", thanks to warm starts (p. 13).
- *Tests*: Fletcher's ADLITTLE (the penalty model is unbounded for ν slightly below about 3.31 × 10³) as a specification (Method 4): the fixed-ν failure reproduced ("We confirmed this behavior experimentally."), then solved with ν raised to 10⁴ in 1 or 6 iterations for initial radii 10¹⁰ and 10 (pp. 14–15). The heuristic of a huge fixed ν ablated (Method 2): on a CUTEr subset, problems solved fell from 485 of 616 to 449 at ν = 10⁵ and 321 at ν = 10¹⁰; "the risks of using excessively large penalty parameters are real indeed" (pp. 15–16).
- *Merit functions* (line search, equality constraints): the ε2 test gives ν⁺ = ν_trial + 1 when ν < ν_trial, with ν_trial = (∇fᵀd + (σ/2)dᵀWd) / ((1 − ε2)‖h‖), σ = 1 if dᵀWd > 0, else 0 (pp. 18–19); "significantly more effective" than a descent-only ν in Knitro-Interior/Direct, no table shown (p. 20).
- *Scope printed*: penalty SQP untested ("We have not yet developed a software implementation … and therefore, cannot evaluate the computational tradeoffs", p. 11); "It remains an open question, however, how to extend our guidelines to penalty line search methods" (p. 20).
- *Inferred link*: the 2010 infeasibility-detection SQP "adjusts the penalty parameter automatically, when appropriate, to emphasize feasibility over optimality" (doi:10.1137/080738222, abstract; body not read).
**Limitations**: "It is assumed that noise level is known or can be estimated by means of difference tables or sampling" (arXiv:2102.09762). Mainly additive, bounded, uniform noise [03 §2.3]; nonsmooth problems out of scope. His noise-aware constrained work is equality-constrained only (Oztoprak, Byrd & Nocedal, "Constrained Optimization in the Presence of Noise", *SIOPT* 33, 2023, doi:10.1137/21M1450999; arXiv:2411.02665): noisy barrier, filter or inequality tests are inference; Oztoprak & Byrd continue without him (Latest). That KNITRO's `findiff_estnoise` option came from this research is inferred [03 §2.8].

**Full-text evidence (2026-10-17):**

**Full-text evidence (08 §2.3).** Distinct works: 50 evidence (41 full or partial), 29 variant, 0 contradiction; 72 works with any link; 79 card entries. (08 counts every read level; SKILL.md uses the regenerated list at the end of this section.)

- **Strongest full-text evidence**: finite-difference L-BFGS with a noise-based interval, a relaxed Armijo test, a five-case recovery tree and its ablation [S038 pp. 6–11, 21]; the noise-tolerant BFGS with its split-phase line search and recovery logic [S071 pp. 1–6, 13–16, 18–23]; the noisy trust region changing only the ratio test [S082 pp. 2, 4–5, 11, 18–19]; the constrained noisy SQP whose repair is ablated and whose estimate is stressed 10× to 1000× both ways [S084 pp. 2–3, 18–20]; the adaptive interval replacing an unknowable derivative by a testable ratio [S091 arXiv pp. 2, 4, 11–12, 15–17]; only the derivative oracle and one Armijo test changed, nothing else in L-BFGS [S080 arXiv pp. 12–13, 26]; the infeasibility mode driven by the normal step's feasibility estimate, with a return test and exits [S053 pp. 5–6, 8–9, 12]; the reduced-Hessian cross-term repaired at an explicit KKT-error trigger and ablated [S067 pp. 5–9, 15–18]; L-BFGS kept under bounds, the failing line search replaced [S003 pp. 6, 18–19]; the projected-CG drift repaired by an internal cosine diagnostic with refinement as recovery [S021 pp. 8, 13–14, 17–21].
- **Stated, written** (new Stated line in SKILL.md; the Simons quotes stay in the base text): "In other words, in the finite-difference approach to derivative-free optimization, algorithms do not need to be constructed from scratch but can be built as adaptations of existing codes." [S080 arXiv p. 26]; the guidelines paper: "These guidelines stem from the observation that, in the presence of noise, only few operations can lead to numerical difficulties in optimization methods." [S128 p. 1] (step 1: audit the fragile operations first).
- **Say–do (C8)**: the base tier dates it 2007–2025. Engine-kept, one-component repairs appear from 1993–95 [S193 pp. 3–4; S003 pp. 6, 18–19; S028 pp. 4, 10, 16, 30], and the estimate-driven form from 2002 (the ν∞ LP sets the penalty) [S035 report pp. 14–16]. Step 4 (recovery tree and exit flags) is the least practised step: built in [S038 pp. 9–11], [S071 pp. 12–14], [S053 pp. 9, 12], [S036 pp. 14–17]; named as necessary but not built in [S084 p. 20]; absent in [S082 p. 18], [S124 pp. 4–5, 33], [S018 pp. 6, 18]; only proposed in [S015 p. 19]. Mark: ✅ stated + practised 1993–2025; step 4 ⚠ partial. After review (2026-10-17): S193 is a DOE progress report whose pp. 3–4 plan the component repairs rather than carry them out, and progress reports are weak method evidence, so SKILL.md now reads *planned 1993; practised 1995–2025* [S003 pp. 6, 18–19], *estimate-driven from 2002* [S035 report pp. 14–16].
- **Worked case (penalty steering), corrections C4**: the problem was named in 1993: "In practice, however, the penalty parameter may become large too soon, and this forces the iterates to follow the constraints too closely." [S193 p. 4]. The first rule is in SLIQUE (2002): re-solve the step LP with the objective gradient switched off, keep ν when no progress is possible, demand a fraction ε = 0.1 of the attainable reduction, reset ν when it grows too large [S035 report pp. 14–16]; theoretical root in the SLQP convergence paper [S058 pp. 19–20]. The 2007 preprint's open question on extending the guidelines to penalty line-search methods (p. 20) was answered by the same group in 2012 with the line-search steering method [S051 pp. 1–2, 4–6, 30]: "There is no switch in Algorithm I, which always takes steps based on the penalty function φπ." [S051 p. 25]. The base tier's *Inferred link* to the 2010 infeasibility-detection SQP is confirmed from the body: the update is built in the spirit of the steering rules, with a ρ = 0 reference step [S052 pp. 14–16]. Steering is reused unchanged as a module inside the 2011 PLA implementation [S139 pp. 4–5]. The 2008 numbers (ν0 = 10, ε1 = 0.1, ε2 = 0.5; 485, 449 and 321 of 616) are confirmed in the card of the 2007 report [S042 pp. 13, 15–16]; S126, the 2006 report of the same paper, is not counted as independent evidence.
- **Variant notes (step details, not new methods)**: zero-noise collapse as the design check: the repaired method reduces exactly to the classical one when the estimate is zero [S071 pp. 13, 25; S082 pp. 11, 23; S084 p. 15; S102 pp. 5, 8, 11; S124 pp. 28–29]; the same reduction check is in Fletcher's (Method 5 step 1) and Gill's (Method 1) skills. Oracle arm in the ablation: the method run with the true value of the estimated quantity, labelled for benchmarking only [S091 arXiv pp. 17–18; S080 arXiv pp. 13, 23–24, 38–40; S068 p. 20]; Curtis's Method 1 step 4 has the same move (co-authored S068). Explicit estimate of attainable progress by an extreme-value probe: ν = ∞ LP [S042 pp. 8–11], ρ = 0 reference step [S052 p. 15], σ = 0 and σ = 1 solves [S029 pp. 5, 8]. Pre-noise variants (engine kept, no estimate or recovery): [S007 pp. 1–2; S012 pp. 11–12, 20; S014 pp. 4, 13; S009 pp. 4, 17–18; S040 pp. 3, 5, 11; S150 pp. 3, 5–6]; a fallback to a second engine rather than a repaired component [S011 pp. 5–7; S013 pp. 4–5, 8, 12]; cost rather than failure as the trigger [S023 pp. 5, 10; S024 pp. 2–3, 11–12] (now Method 7).
- **Worked case 2 (infeasibility mode, added to SKILL.md after review, 2026-10-17)**: the normal step of the step-decomposition interior method measures the attainable feasibility reduction, which a line-search primal-dual step cannot [S053 pp. 2, 5]; hysteresis switch: to feasibility mode when the linearized residual after the step is ≥ δ‖c‖, back when ≤ δ̄‖c‖, δ = 0.9, δ̄ = 0.1 [S053 p. 8]; anti-cycling rules (ζ = 0.99, at least 3 main-mode iterations, two consecutive triggers, a (1−σ) decrease before returning) and warm-start rules at each switch [S053 pp. 10, 12]: "We have found that these additional switching rules prevent the algorithm from switching modes too rapidly, and also make it unnecessary to try to adjust the values of the constants" [S053 p. 12]; exits KKT, infeasible stationary point, LICQ failure [S053 pp. 9–10]; detection on 17 of 17 small infeasible problems against 8 for the old code (the card's count of Table 4), a termination cross-table over 430 constrained CUTEr problems and a log₂ iteration-ratio plot [S053 pp. 13–14]. The SQP counterpart [S052] is co-authored with Curtis.
- **Limitations confirmed**: noise-aware constrained work remains equality-constrained [S084 pp. 2–3, 5, 20; S124 pp. 4–5]; general constraints appear only in the noiseless 2026 DFO letter, whose noise claim is untested [S150 pp. 5, 9–10].
- **C3 (page correction)**: the stop line's quoted phrase *are not robust* is on p. 6 (§1.2) of arXiv:2102.09762 v1, not in Appendix A [S080 arXiv p. 6].

**Increment inc-ocr (2026-10-17)** (round-4 cards c4-01 to c4-04 and s4-01, second reads from an OCR text layer; one piece of evidence with each work's earlier card; numbers from the round-4 cards; 08 §12). Count: 62 works (40 evidence, 27 variant, 0 contradiction), was 61 (40, 26, 0): S061 is newly linked as a variant.

- **L-BFGS-B, the values**: a pair is skipped unless sᵀy > eps‖y‖², eps = 2.2 × 10⁻¹⁶ in the tested code, without deleting the oldest pair; backtracking replaced by the Moré–Thuente search (α = 10⁻⁴, β = 0.9) with the maximum step at the closest bound [S003 pp. 6, 18–19]; the code's skip test is yᵀs/(−gᵀs) ≤ epsmch [S005 p. 7]. Recovery and exit: "If the line search is unable to find a point with a sufficiently lower value of the objective after 20 evaluations of the objective function, we conclude that the current direction is not useful" [S005 p. 7]; the pairs are then discarded and the iteration restarts along steepest descent, and a second failure ends with a named exit [S005 pp. 6–7]. Step 4 (recovery and exit flags) therefore appears in the 1994 code report, long before the noise programme.
- **Reduced-Hessian SQP (1995)**: the cross-term estimate by a Broyden matrix costs no evaluations; the finite-difference fallback is used only in region R2: "Thus, up to three evaluations of the objective function gradient may be required at each iteration." [S028 p. 8]; BFGS is skipped in R3 [S028 pp. 16, 32]; the safeguards are proved inactive near the solution [S028 pp. 29–30].
- **Rounding error as the regime (preprint September 2000, journal 2001)**: the projected-CG drift is diagnosed by a cosine with ε_m^0.75 ≈ 10⁻¹² as the trigger [S021 p. 10], and refinement is applied only above it [S021 pp. 13, 16]: "In our experience, 1 iterative refinement step is normally enough to provide good accuracy, but we have encountered cases in which 2 or 3 steps are beneficial." [S021 p. 17]; the residual update meets the 10⁻¹² test on 13 of 14 QPs, refinement alone on 11, the baseline on at most 1 (card's count) [S021 p. 23]. A precursor of the estimate-driven form before SLIQUE (2002); the say–do date in SKILL.md is kept (08 §12.5, rejected update 1).
- **Variant (new link)**: the 2004 paper names the failing component (the merit function), keeps the Newton engine, changes the merit function and adds a Hessian safeguard, without an estimate or a recovery path [S061 pp. 18–22].
- Variant (as before): a component replaced because of cost, not failure: the trust-region re-solve by backtracking [S024 pp. 2–3, 11–12].

**All card links** (regenerated 2026-10-17 for increment inc-ocr from the digests' `method_links`, with the SKILL.md counting rule: full or partial cards only; abstract- and metadata-level cards, NSF award records and the group-voice S063, S179, S188 listed apart and not counted; S126 counted with S042 and S056 with S143; for the six works upgraded in round 3 only the deeper card is used; the earlier and later cards of the 26 twice-carded works (ten re-read in round 2, sixteen in round 4) are labelled by batch, one work each, round-1 pages prose only). Counted: 62 works, 74 card entries:

- **Evidence** (40 works, 48 card ids): S003 pp. 6, 18–19 (c02); S003 pp. 6, 18–19 (c4-02); S004 pp. 45, 53, 57–58; S005 pp. 6–7 (c02); S005 pp. 6–7 (c4-02); S008 pp. 4–5, 7–10 (c03); S016 preprint p. 2; S018 pp. 4–6, 15–18; S021 pp. 10, 13, 16, 18–19, 23 (c4-03); S021 pp. 8, 13–14, 17–21 (c04); S027 p. 20; S028 pp. 4, 10, 16, 30 (s02); S028 pp. 8, 16, 29–30, 32 (s4-01); S029 pp. 3–4, 8–12; S031 pp. 3–5; S033 pp. 2–3, 6–8; S035 report pp. 14–16 (c2-01); S035 report pp. 14–16 (s04); S036 pp. 14–17; S038 pp. 6–11, 21; S042 pp. 8–13; S045 pp. 4, 6–7; S050 pp. 3–4; S051 pp. 4–6; S052 pp. 3, 14–16; S053 pp. 5–6, 8–9, 12; S058 pp. 19–20; S064 preprint pp. 1, 10–11, 15; S067 pp. 13–15, 19 (s03); S067 pp. 5–9, 15–18 (s2-01); S068 pp. 10, 17; S071 pp. 1–6, 13–16, 18–23; S072 pp. 1–4, 12, 19–22, 26; S075 pp. 5, 14 (s2-01); S075 pp. 5, 8–9, 13–15 (s04); S080 arXiv pp. 6, 12–13, 17, 26, 38–42; S081 pp. 7–9; S082 pp. 2, 4–5, 11, 18–19; S084 pp. 2–3, 18–20; S089 p. 2; S091 arXiv pp. 2, 4, 11–12, 15–17; S102 pp. 1–3, 5, 11–12; S113 pp. 2, 13–14; S124 pp. 4–5, 33; S126 pp. 5, 7–12 (= S042); S128 pp. 1–2, 4, 9, 14; S139 pp. 4–5; S193 pp. 3–4.
- **Variant** (27 works, 31 card ids): S007 pp. 1–2; S009 pp. 4, 17–18, 35 (c04); S009 pp. 4, 17–18, 35 (c4-03); S011 pp. 5–7, 14–15; S012 pp. 11–12, 20, 24; S013 pp. 4–5, 8, 12; S014 pp. 13, 18 (c4-01); S014 pp. 4, 13 (c02); S015 pp. 1, 5–7, 19; S016 preprint p. 2; S023 pp. 5, 10; S024 pp. 2–3, 11–12 (c03); S024 pp. 2–3, 11–12 (c4-02); S026 pp. 16–17; S030 pp. 2, 6 (c2-01); S039 pp. 30, 43; S040 pp. 3, 5, 11 (c2-01); S043 pp. 3, 6; S060 pp. 2, 6; S061 pp. 18–22 (c4-04); S071 pp. 12–16 (with S072 p. 2); S072 pp. 4, 19, 24, 26; S073 pp. 4–6, 20–21; S082 pp. 18, 23; S084 pp. 18, 20; S085 pp. 5–6; S101 p. 12 (s02); S101 p. 12 (s4-01); S110 pp. 4–6; S143 p. 7; S150 pp. 3, 5–6.
- **Contradiction** (0 works, 0 card ids): none.
- **Not counted** (abstract- or metadata-level, award records, group voice): evidence: S135; S167 (award); S169 (award); S173 (award); S176 (award); S178 (award); S186 (award); S191; S192 (award) — variant: S063 p. 37 (group voice); S188 pp. 1–2 (group voice).

---

<a id="method-4"></a>
## Method 4: Failure modes and open questions → solver options and next papers

**Base-tier text (verbatim, SKILL.md of 2026-09-28):**

#### Method 4: Turn failure modes and open questions into solver options and the next papers
**One line**: Write the solver's known failure modes and undecided choices into the paper, expose undecided choices as options, study them in two frameworks, and answer counterexamples and rival benchmarks with algorithm variants rather than rebuttals.
**Evidence**:
- Stated (co-authored, 2006): "Since it is not known at present which one is the most effective in practice, Knitro allows the user to experiment with the barrier update strategies just mentioned." (doi:10.1007/0-387-30065-1_4). 2026 (caption-derived), on the barrier parameter: "there is no complete theory uh behind it" [02 J6].
- Practice (arrows inferred from timing unless noted): the 2006 limitation "the algorithms in Knitro cannot distinguish between infeasible problems and convergence to an (infeasible) stationary point for a measure of feasibility" → infeasibility-detection papers (doi:10.1137/080738222; doi:10.1080/10556788.2013.858156). The barrier-rule option → a study in IPOPT and KNITRO: "heuristic adaptive choices, such as Mehrotra's probing procedure, outperform monotone strategies" (doi:10.1137/060649513, abstract). Two separate critique chains: (a) the Wächter–Biegler example (doi:10.1007/PL00011386) → Byrd, Marazzi & Nocedal's analysis of why Newton iterations stall, which discusses the example (doi:10.1007/s10107-003-0376-8, preprint p. 2); (b) the LOQO authors' benchmarks (doi:10.1007/s10107-003-0418-2) → Knitro-Direct, the line-search / trust-region hybrid of Waltz, Morales, Nocedal & Orban (doi:10.1007/s10107-004-0560-5), which credits LOQO. Fletcher's ADLITTLE example → penalty steering, acknowledged in the paper (Method 3 worked case) [05 §4]. Observed: KNITRO 16.0 lists seven `bar_murule` values [03 §2.8].
- Say–do consistency: ✅ stated + practised, 1999–2014.
**Steps**:
1. **In each solver paper, list the known failure modes and undecided choices**, e.g. "the choice of the merit parameter ν plays a crucial role in the efficiency of the algorithm" (2006, preprint p. 11) [01 SW3].
2. **Where theory and experiments cannot decide, expose the choice as an option.**
3. **Study the open choice in two independent frameworks**, including how the incumbent heuristic fails (2009: IPOPT and KNITRO; failures of the Mehrotra predictor-corrector rule).
4. **Treat an external counterexample or rival benchmark as a specification**: analyse why the method stalls, then build the variant.
5. **Credit the rival's idea** in the new paper: Hessian convexification "was first shown to be effective in the context of nonlinear interior methods by the Loqo software package" [05 §4.3].
6. **Ship the variant in production** (Knitro-Direct, Knitro-CG, Knitro-Active).
   - 🔴 Before publishing a solver paper, check the failure-mode list. If it is empty, you have not looked: run naïve failure tests (Heuristic 6).
**Applies to stage**: algorithm design; after publication; research agenda.
**Different from standard practice**: the undecided choice becomes a user option and a study inside a rival's framework.
**Limitations**: responses to benchmarks do not cite them, so those links are inferred from timing [05 §4.3]; responses to counterexamples name them (Byrd–Marazzi–Nocedal; steering thanks Fletcher) [05 §4.1, §4.6]. Lewis & Overton's weak-Wolfe suggestion (doi:10.1007/s10107-012-0514-2) was not adopted [05 §3.2]; ML critics got no replies [05 §1.2]. The full form needs an owned production solver; otherwise keep the register and expose options in open-source code.

**Full-text evidence (2026-10-17):**

**Full-text evidence (08 §2.4).** Distinct works: 58 evidence (54 full or partial), 2 variant, 0 contradiction; 59 works with any link; 65 card entries. (08 counts every read level; SKILL.md uses the regenerated list at the end of this section.)

- **Strongest full-text evidence**: KNITRO's lack of infeasibility handling becomes the 2014 paper and ships as `bar_switchrule=2`: "The performance of the interior point methods knitro/direct and knitro/cg are quite poor, which may not be surprising since these two algorithms do not contain any features for handling infeasibility." [S053 pp. 1, 4, 13]; the Wächter–Biegler counterexample analysed as a specification, with a configuration that cannot fail [S061 pp. 2, 14, 19–24]; an external counterexample run on the own code already in 2001 [S111 pp. 13–15, 19–21]; the undecided subspace minimization shipped as `isbmin` [S003 pp. 11, 23; S005 pp. 5–6]; two selection rules shipped as `IOP` [S098 pp. 4, 7]; the steering open question answered [S051 pp. 1–2, 30]; the KNITRO 3.0 manual documents exit code −2 for infeasible stationary points and tells users to try both options in 2003 [S063 pp. 1, 4, 37–38] (product voice); the own failure case GAUSSELM as specification, shipped as KNITRO's feasible mode [S075 pp. 8–18]; the 2024 noisy trust region prototyped as an option inside KNITRO-CG (modified by Oztoprak, Artelys), with the noise level as input; a shipped release is not established [S124 p. 29].
- **Say–do (C8)**: the base tier dates it 1999–2014. Practice runs 1989–2024: two line-search modes as code options [S002 p. 13]; application needs written into next year's plan [S197 pp. 4–5; S193 pp. 3–4]; the 2024 KNITRO option [S124 p. 29]. Mark: ✅ stated + practised 1989–2024.
- **C5**: step 3 said *two independent frameworks*. In the 2009 barrier study the two frameworks are the authors' own codes (Wächter, IPOPT's author, is a co-author) [S029 pp. 1–2, 25]; the 2004 starting-point study pairs KNITRO with a bare code built for the purpose [S085 pp. 6, 8]. Step 3 now reads *two frameworks, ideally including one you do not own*.
- **C6**: the infeasibility arrow (2006 limitation → 2010/2014 papers) is now partly documented: the 2014 paper restates the limitation [S053 p. 4]; the 2010 paper cites the 2006 package paper but not its limitation sentence [S052 p. 18]. The barrier arrow (2006 option → 2009 study) stays inferred: the 2009 paper does not mention the option [S029 pp. 2, 17–21].
- **Variant**: undecided choices adapted automatically from in-run signals, with only m left to the user, because the goal is parameter-free algorithms [S077 pp. 2, 5–7]; known weaknesses turned into lemmas, repairs deferred (1978) [S120 pp. 45–48].
- Failure taxonomy by name and cause, used in step 3 [S029 pp. 16–17].

**Increment inc-ocr (2026-10-17)** (round-4 cards c4-01 to c4-04 and s4-01, second reads from an OCR text layer; one piece of evidence with each work's earlier card; numbers from the round-4 cards; 08 §12). Count: 52 works (51 evidence, 3 variant, 0 contradiction), was 52 (51, 2, 0): S061 adds a variant link.

- **A documented arrow from a named failure mode to the next paper**: NITRO's failure-mode list (the barrier decrease overly conservative, the refinement very conservative) names [7] and [24] for the next work [S008 pp. 23, 25–26]; [24] is S021, which answers it. Against the standard CG iteration [S021 p. 25], and with the augmented system that NITRO itself uses [S008 p. 18], its projection counts fall from 22,301 to 16,433 (−26%) over the 26 problems without a failure; with the normal equations from 29,509 to 17,200 (−42%), and 2 failures are rescued (card's sums) [S021 p. 26]. SKILL gives the augmented-system figure (after review); the remedies ship in NITRO, GALAHAD and HSL VE12/VE19 [S021 pp. 22, 25]. Unlike the arrows of C6, this one is documented by citation in both papers.
- **Variant (new): the counterexample answered on paper**: the report answering Wächter–Biegler is dated April 23, 2001 [S061 p. 1], about a year after their 2000 paper (its ref. [14]) [S061 p. 25]; the answer is an analysis, a provably safe algorithm class (Algorithm 1; Theorem 4.1, every limit point stationary for the barrier function) and a new failure example (Example 4), with the infeasible case left without a fix and no production change reported [S061 pp. 20–24]. Step 4's *then build the variant* holds as a paper algorithm; step 6 (ship it) has no evidence here.
- **Hard-coded choices recorded with values (2003)**: the barrier parameter falls by a fixed factor of five and always starts at 0.1, which the paper calls highly detrimental in some cases; an adaptive initial barrier parameter and a preconditioner become to-do items [S078 pp. 4, 15–16]. The link to KNITRO's later barrier options stays inferred (C6).
- **Options, with numbers**: isbmin = 1 (default, direct primal), 2 (dual) or 3 (CG): "It runs the code on 67 test problems (33 bound constrained, 34 unconstrained) from the CUTE collection" [S005 p. 6], with all three options [S005 pp. 5–6]; Tables 1.5–1.6 publish all three [S005 pp. 14–15]; the undecided subspace method is costed three ways before the runs [S003 pp. 13, 15, 17].
- **Alternative strategies instead of one rule**: three barrier-update strategies analysed for the coded interior method [S046 pp. 15–18].

**All card links** (regenerated 2026-10-17 for increment inc-ocr from the digests' `method_links`, with the SKILL.md counting rule: full or partial cards only; abstract- and metadata-level cards, NSF award records and the group-voice S063, S179, S188 listed apart and not counted; S126 counted with S042 and S056 with S143; for the six works upgraded in round 3 only the deeper card is used; the earlier and later cards of the 26 twice-carded works (ten re-read in round 2, sixteen in round 4) are labelled by batch, one work each, round-1 pages prose only). Counted: 52 works, 70 card entries:

- **Evidence** (51 works, 68 card ids): S002 p. 13 (c01); S002 pp. 12–13, 15, 18 (c4-01); S003 pp. 11, 23 (c02); S003 pp. 13, 15, 17, 22–23 (c4-02); S004 pp. 45, 49, 55, 58, 69, 71; S005 pp. 5–6, 14–15 (c4-02); S005 pp. 5–6, 9 (c02); S008 pp. 23, 25–26 (c4-03); S008 pp. 4, 10, 23 (c03); S009 pp. 2, 18, 20–21, 35 (c04); S009 pp. 21, 32–34 (c4-03); S011 pp. 4–5, 17, 20; S013 pp. 2, 4; S015 pp. 9, 19–20, 29; S018 pp. 22, 27–28; S021 pp. 2, 22, 25 (c04); S021 pp. 22, 25 (c4-03); S027 p. 25; S028 p. 34 (s02); S028 pp. 17, 34 (s4-01); S029 pp. 2, 17–21; S030 pp. 15, 17, 20 (s03); S034 pp. 20, 22–24; S035 report pp. 7, 29, 31 (c2-01); S035 report pp. 7, 29, 31 (s04); S038 pp. 11, 21–22; S042 pp. 14–15, 20; S043 pp. 3–4, 7; S045 pp. 18–19; S046 pp. 2, 15–18 (s4-01); S046 pp. 3, 15–18 (s02); S049 pp. 11–12, 17–18 (c03); S049 pp. 11–12, 17–18 (c4-02); S051 pp. 1–2, 25–26, 30; S052 p. 18; S053 pp. 1, 3–4, 12–13; S057 p. 2 (c2-01); S060 p. 6; S061 pp. 1–2, 14, 23–25 (c4-04); S061 pp. 2, 14, 19–24 (c04); S064 preprint pp. 10, 15–19; S067 pp. 5, 11 (s03); S068 pp. 2, 11; S071 pp. 2, 13, 20; S073 p. 3; S075 pp. 8–18 (s2-01); S077 pp. 3–4 (s03); S078 pp. 4, 12, 15–16 (c4-04); S078 pp. 9, 11, 15–16 (c04); S080 arXiv pp. 7, 13, 15–16, 32, 37; S084 pp. 2–3, 5, 20; S085 pp. 6, 8; S088 pp. 4, 7, 10–12 (s4-01); S088 pp. 7, 12 (s02); S098 pp. 4, 7 (s03); S098 pp. 4, 7 (s2-01); S101 pp. 1, 10–11, 14–15 (s4-01); S101 pp. 14–15 (s02); S105 pp. 8, 11, 20; S111 pp. 13–15, 19–21 (s2-01); S111 pp. 13–21, 23–24 (s03); S114 pp. 2–3; S118 pp. 3, 7; S124 p. 29; S126 pp. 14–15, 20 (= S042); S143 pp. 2–3, 5, 9, 14–15; S193 pp. 3–4; S197 pp. 4–5.
- **Variant** (3 works, 3 card ids): S061 pp. 20–24 (c4-04); S077 pp. 2, 4–7 (s2-01); S120 pp. 45–48.
- **Contradiction** (0 works, 0 card ids): none.
- **Not counted** (abstract- or metadata-level, award records, group voice): evidence: S063 pp. 1, 4, 37–38 (group voice); S173 (award); S176 (award); S178 (award); S179 p. 1 (group voice); S190 (award).


**Increment inc-book (2026-10-17)** (book material B001–B012, cards c5-01 to c5-03: the open parts of *Numerical Optimization*, its errata, two reviews, the authors' book pages and Springer's catalogue pages; joint voice of Nocedal and S. J. Wright unless marked; dating and framing only, never in a say–do count; 08 §13, #textbook). Count unchanged: 52 works (51 evidence, 3 variant, 0 contradiction).
- **Not counted** (book material, joint voice): evidence, framing and title-level: B001 p. 16 (19.7 *Failure of the Line Search Approach*, then *Modified Line Search Methods*; the 1999 edition had *Failure of the Active-Set Method*, B005 p. 17). Not exclusive: Wright's Heuristic 7 (treat a published worst case as a problem).
- Not read (the body is closed): whether 19.7 presents the Wächter–Biegler example [S061], and whether the 18.5 subsection *A Technique for Updating the Penalty Parameter* presents the steering rules [S042] [B001 pp. 15–16].
- Dating: the 2006 bibliography cites four of the group's papers as then-unpublished OTC reports (KNITRO, penalty steering, the MPCC interior work, the interior/active-set hybrid) [B002 pp. 42, 49, 54] (card's reading of the dates).

---

<a id="method-5"></a>
## Method 5: Theory must discriminate between practical methods

**Base-tier text (verbatim, SKILL.md of 2026-09-28):**

#### Method 5: Theory must discriminate between practical methods
**One line**: Analyse the method as implemented, ask whether the result separates a method known to work from one known to fail, and plot the bound against the runs.
**Evidence**:
- Stated: "After all, if all we want to achieve is global convergence we should be satisfied with the steepest descent method." (Acta 1992, preprint p. 7). On complexity work (2026, caption-derived): "They're not distinguishing between good methods and bad methods." His most repeated belief, in 6 sources [02 §0, T3–T6].
- Practice: quasi-Newton convergence under practical line searches (doi:10.1137/0724077; doi:10.1137/0726042; bodies not read). The Broyden-class result that excludes DFP (per his 2026 summary). "the theoretical prediction given in Theorem 6 is pessimistic when compared to the final achieved accuracy in the gradient" (arXiv:2201.00973, p. 19) [03 §3.3]. Acta 1992 ends with numbered Open Questions [02 W4].
- Say–do consistency: ✅ stated + practised, 1985–2023.
**Steps**:
1. **Analyse the version people run** (Wolfe line searches, limited memory, safeguards as coded), asking "what do we know about the behavior of this method, as implemented in practice?" (Acta 1992, preprint p. 1).
2. **Ask whether the result separates a method known to work from one known to fail** (BFGS against DFP).
3. **Ask for a rate, not only global convergence.**
4. **Plot the bound against observed runs**, and say plainly if it is pessimistic.
5. **Keep what you cannot prove as numbered open questions**; never present numerical experience as proof.
   - 🔴 If a complexity-optimal variant is proposed for the solver, first ask whether its bound distinguishes it from the incumbent on the problems users run.
**Applies to stage**: judging results; theory; choosing algorithms.
**Different from standard practice**: the value is common in this team; the discrimination test and the bound-versus-run plot are his.
**Limitations**: "Nobody has been able to construct an example in which the BFGS method fails" (Acta 1992) was overtaken by Dai 2002 (doi:10.1137/S1052623401383455), with no response found [05 §3.1]; the stance on complexity shifted (Inner Tensions, IT5). Early-career users should pair complexity results with the bound-versus-run plot, not drop them.

**Full-text evidence (2026-10-17):**

**Full-text evidence (08 §2.5).** Distinct works: 45 evidence (37 full or partial), 32 variant, 7 contradiction; 74 works with any link; 79 card entries. (08 counts every read level; SKILL.md uses the regenerated list at the end of this section.)

- **Strongest full-text evidence**: the Broyden-class analysis "as implemented in practice" that singles out DFP and confirms it with a targeted run: "Nevertheless, we have seen in this paper that the DFP method can be much less efficient than the BFGS method, and that the reason for this is that it lacks the self-correcting property given by the fourth term on the right-hand side of equation (3.2)." [S020 pp. 1, 10, 17–19]; CG theory explaining FR stalling and PR recovering, with experiment parameters set to the theorem's [S012 pp. 4–6, 11–12, 24, 27]; the Acta survey's two tests and numbered open questions [S019 pp. 1–2, 7, 17–24]; self-scaling separated from BFGS [S054 pp. 10–11, 15–18]; merit choices separated (a KKT-norm merit can fail, a barrier merit cannot) [S061 pp. 11–13, 16–22]; Theorem 4.1 separating line-search from trust-region slack resets [S075 p. 11]; Cauchy decrease separating methods that can stall at infeasible points [S111 pp. 5–10, 13–22]; a rate, not only convergence, in the infeasible case [S052 pp. 12, 16]; the corrected BAS method separated from BAS (130 against 0 failures) [S064 preprint pp. 13, 17]; a spectrum-dependent CG bound tied to plotted spectra [S041 pp. 11–16, 32–33]; a bound plotted against runs and called pessimistic, with its (ε_f, ε_g) scaling tested over a grid [S082 pp. 19–22].
- **Say–do: ⚠ partial (C8).** The stated value is constant: "Ironically, our many theoretical studies of variable metric methods have not resulted in the discovery of new methods, but have mainly served to explain phenomena observed in practice" [S019 p. 16]. Practice splits by period. 1987–2004: steps 1–3 practised in most theory papers listed above. 2006–2025: several theorems cannot discriminate by construction (see #taste-warnings). From 2012 the analysed iteration is often a simplified one, with the gap stated [S018 pp. 6, 11, 15; S031 pp. 5, 12; S038 pp. 12, 19; S071 pp. 10–12; S084 pp. 2, 4–5, 15; S102 pp. 7–14; S128 pp. 9, 11]. Step 4 (bound plotted against runs) appears in [S082 pp. 19–22], [S021 p. 12], [S057 pp. 24, 26], [S041 pp. 14–15] and, for an estimator, [S091 arXiv pp. 15–16]; it is absent in most 2016–2025 theory sections [S033 p. 6; S031 p. 5; S032 arXiv pp. 19–20; S072 p. 24; S071 p. 15; S124 pp. 29–30]. Mark: ✅ stated throughout; ✅ practised 1987–2004; ⚠ 2006–2025.
- **C1 (Dai 2002)**: the base Limitations say Dai 2002 overtook the 1992 claim *with no response found*. A 2016 group paper cites Dai and Mascarenhas as showing that BFGS fails on nonconvex problems and adopts cautious updating in response [S033 p. 6]; the 2018 progressive-batching method skips updates when yᵀs ≤ ε‖s‖² [S031 p. 5]. The 1992 survey already listed nonconvex BFGS as Open Question II [S019 pp. 21–22]. After review (2026-10-17): the device is Li–Fukushima's (2001, S033's ref. [15]), adopted for the paper's own nonconvex analysis; this acknowledges Dai's example and works around it, it does not answer it, so SKILL.md now says *acknowledged in 2016*.
- **Tension evidence (IT5)**: the co-authored survey credits SG's success to its superior work-complexity guarantees [S004 p. 82], while a 2020 paper rejects a worst-case bound: "That analysis, however, underestimates the power of the SSN-CG method on problems with favorable eigenvalue distributions and yields complexity estimates that are not indicative of its practical performance." [S041 p. 11]. Early analysed-versus-run gaps [S007 pp. 5–6, 9; S138 p. 77] are early-career and closed by [S020] and [S002 pp. 21–24].
- **Practice device (not a new method)**: specify the method by admissible conditions so that the theory covers the code [S042 p. 13; S058 pp. 10, 24; S035 report p. 7]; shared with Wächter's Method 3.

**Increment inc-ocr (2026-10-17)** (round-4 cards c4-01 to c4-04 and s4-01, second reads from an OCR text layer; one piece of evidence with each work's earlier card; numbers from the round-4 cards; 08 §12). Count: 66 works (38 evidence, 31 variant, 7 contradiction), was 65 (37, 31, 7): S078 is newly linked as evidence.

- **Step 2 with counts (1992)**: on the Byrd–Nocedal–Yuan two-variable test BFGS solves to high accuracy in 15 iterations and cuts the trace of B_k from 10⁴ to 3 in 10 iterations; "In contrast, the DFP method required 4041 iterations to obtain the solution (which is amazingly close to the estimate given by Powell)."; DFP needs 3000 iterations to bring the trace to 1100; φ = 0.999 needs 2223 [S019 p. 24]. The predicted count set against the observed one is an early form of step 4.
- **Step 4 with numbers (2001)**: the normal-equations error bound, evaluated with Example 2's constants (γ = O(10⁴), ε_m = 10⁻¹⁶, κ(A) = O(10³), a norm ratio O(10⁶) at iteration 50), predicts no correct digits where CG stalls, and is called reasonably tight there [S021 p. 12].
- **Theory that separates the coded settings**: the settings of the Byrd–Hribar–Nocedal code (θ = 1, τ = 0.995, γ = 0.2) are proved safe, but: "The rate of convergence will, however, be only linear." [S046 p. 16]; Strategies 2 and 3 give superlinear convergence, and a quadratic decrease of μ is ruled out for the one-step barrier test [S046 pp. 14, 16–18]. 1-step against 2-step Q-superlinear convergence separates the cross-term designs: "We will show that the rate of convergence of the new algorithm is 1-step Q-superlinear, as opposed to the 2-step superlinear rate for methods that ignore the cross term" [S028 p. 4]; the rate is stated in the number of updates, ‖x_j − x*‖ ≤ C r^{|U_k|} [S028 p. 23]. Trust region plus backtracking converges under Σ 1/M_k = ∞ with M_k = 1 + max‖B_i‖, as strong as pure trust-region theory [S024 pp. 13, 17–19].
- **Theory status named for the rival (new link)**: for LOQO the dynamic barrier rule and the merit function stand in the way of a theory; for KNITRO's design the theory is S009, an algorithm similar to the one implemented [S078 pp. 4–5].
- **Variant, sharpened (the new ⚠ bullet in SKILL.md)**: Algorithm I of the 2000 theory raises the penalty to max(ν̃_k, 1.5ν_{k−1}) when it must grow and resets the slacks to max(s_k + d_s, −g_{k+1}) [S009 p. 17]; both are proof devices: the factor gives ν → ∞ in Lemmas 4.7–4.8, the reset gives g + s ≥ g⁺ and is controlled in Lemma 4.5 [S009 pp. 23, 26–27]. The shipped NITRO raises ν only to the needed value and has no slack reset [S008 pp. 17, 19]; its tables run the primal-dual version [S008 p. 20], while the theory analyses the primal one for simplicity [S009 p. 8] and calls its simple radius rule sufficient for its purposes [S009 p. 10]; the code paper names the trust-region difference [S008 p. 10]; neither paper names the 1.5× factor or the slack reset (SKILL's bullet, which first said only the trust-region gap is named, corrected after review). Step 1 (*analyse the version people run*) is met by a sibling; taste warning 9's *his group names it* holds only in part in 2000.
- **Variant (as c01)**: Theorem 6.1 gives R-linear convergence from any positive definite start and does not separate L-BFGS from Shanno–Phua or Buckley–LeNir, which can be made n-step quadratic [S002 pp. 23–24].
- **Theory separates merit functions, with numbers**: the KKT-norm merit stalls at (0.96364, 0.070085) with ‖∇φ_μ‖ ≈ 0.878 and steps down to 3.47e−18 [S061 p. 18]; Theorem 4.1 rules out the stall for the barrier merit [S061 pp. 20–22]; the hypotheses are checked at the numerical limit point [S061 p. 18] and the prediction is plotted on a grid [S061 p. 9].
- Mark unchanged: ✅ practised 1987–2004 (strengthened by these numbers), ⚠ after 2005.

**All card links** (regenerated 2026-10-17 for increment inc-ocr from the digests' `method_links`, with the SKILL.md counting rule: full or partial cards only; abstract- and metadata-level cards, NSF award records and the group-voice S063, S179, S188 listed apart and not counted; S126 counted with S042 and S056 with S143; for the six works upgraded in round 3 only the deeper card is used; the earlier and later cards of the 26 twice-carded works (ten re-read in round 2, sixteen in round 4) are labelled by batch, one work each, round-1 pages prose only). Counted: 66 works, 80 card entries:

- **Evidence** (38 works, 48 card ids): S004 pp. 30, 36–37, 49, 56; S006 p. 9; S012 pp. 4–6, 11–12, 24, 27; S019 pp. 18, 22, 24 (c4-01); S019 pp. 1–2, 7, 17–24 (c02); S020 pp. 1, 10, 17–19; S021 p. 12 (c04); S021 p. 12 (c4-03); S024 pp. 10–12, 19 (c03); S024 pp. 13, 17–19 (c4-02); S026 pp. 10, 30; S027 pp. 8, 24; S028 pp. 4, 11, 23, 29 (s4-01); S028 pp. 4, 34 (s02); S033 p. 6; S035 report p. 7 (c2-01); S036 p. 7; S039 pp. 4, 7–8, 44; S041 pp. 11–16, 32–33; S046 pp. 5, 14, 16–18 (s4-01); S046 pp. 5–6, 16 (s02); S049 pp. 19–20 (c03); S049 pp. 19–20 (c4-02); S050 pp. 5, 11–12; S052 pp. 12, 16; S054 pp. 10–11, 15–18; S057 pp. 24, 26 (c2-01); S057 pp. 2–5, 26 (s03); S058 p. 24; S060 p. 17; S061 pp. 11–13, 16–22 (c04); S061 pp. 9, 12–16, 18, 20–22 (c4-04); S062 pp. 6, 9; S064 preprint pp. 13, 17; S067 pp. 13–14, 16 (s2-01); S072 pp. 2, 20–21; S075 p. 11 (s2-01); S075 pp. 10–12 (s04); S078 pp. 4–5 (c4-04); S082 pp. 19–22; S087 p. 11; S089 pp. 10, 13; S102 pp. 13–14; S111 pp. 5–10, 13–22 (s2-01); S111 pp. 8–10, 13–15, 19–22 (s03); S118 pp. 6–7; S138 pp. 39, 49–51; S197 pp. 3–5.
- **Variant** (31 works, 35 card ids): S002 p. 24 (c01); S002 p. 24 (c4-01); S004 pp. 37, 82; S008 p. 10 (c03); S008 pp. 10, 17, 19–20 (c4-03); S009 pp. 11–15, 20, 33, 35 (c04); S009 pp. 8, 10, 17, 23, 26–27, 33 (c4-03); S018 pp. 6, 11, 14–15, 24, 27; S030 p. 17 (c2-01); S031 pp. 5, 12; S032 arXiv pp. 19–20, 24; S036 pp. 3, 7–8; S038 pp. 12, 14, 19; S042 p. 13; S043 p. 4; S047 pp. 2, 16–17; S051 p. 30; S053 pp. 5, 12, 16; S057 pp. 2, 5 (c2-01); S058 p. 24; S060 pp. 6–7; S064 preprint p. 15; S071 pp. 10–12, 15; S072 p. 24; S084 pp. 2, 4–5, 15; S091 arXiv pp. 4–5, 12, 15–16, 29–31; S102 pp. 7–14; S113 p. 21; S114 pp. 12, 24; S115 pp. 2, 5; S120 pp. 26, 37–38; S124 pp. 4–5, 29–30; S126 p. 13 (= S042); S128 pp. 9, 11, 19, 21; S139 p. 3.
- **Contradiction** (7 works, 7 card ids): S007 pp. 5–6, 9; S013 pp. 2, 4; S015 pp. 3, 12–14, 29; S023 pp. 5, 7, 11, 16; S029 pp. 10–12, 22; S033 p. 6; S138 p. 77.
- **Not counted** (abstract- or metadata-level, award records, group voice): evidence: S017; S022; S044; S109; S162; S178 (award); S190 (award); S196 (award) — variant: S108.


**Increment inc-book (2026-10-17)** (book material B001–B012, cards c5-01 to c5-03: the open parts of *Numerical Optimization*, its errata, two reviews, the authors' book pages and Springer's catalogue pages; joint voice of Nocedal and S. J. Wright unless marked; dating and framing only, never in a say–do count; 08 §13, #textbook). Count unchanged: 66 works (38 evidence, 31 variant, 7 contradiction).
- **Not counted** (book material, joint voice): B005 p. 12 (title-level: *Behavior of the Fletcher–Reeves Method* beside *Global Convergence*; S012 is in the reference list, B006 p. 41); B006 pp. 34–35, 50 and B002 pp. 20, 22, 57 (complexity indexed only on the LP pages; the rate of convergence called one of the key measures of an algorithm's performance; partial pivoting judged stable "for all practical purposes" against its worst-case growth). These fit step 4 and taste warning 3, but fail exclusivity against Wright's taste marks 1 and 4 and his Method 2.
- **Limitations, C1 context**: the 2006 bibliography cites neither Dai 2002 nor Mascarenhas 2004; its only Dai entry is Dai–Yuan 1999 on conjugate gradients [B002 pp. 40–55]. Whether the text discusses the examples uncited was not read (05 §3.1 now has a bibliography-level answer). Added to SKILL's Limitations.
- The first-printing errata add an outlined Zoutendijk-type liminf argument to Chapter 3 for methods such as conjugate gradient methods [B007 p. 1]: an expository repair, not evidence for the method.

---

<a id="method-6"></a>
## Method 6: Structure beats your own brand; integrate complementary algorithms

**Base-tier text (verbatim, SKILL.md of 2026-09-28):**

#### Method 6: Structure beats your own brand; integrate complementary algorithms
**One line**: Look for structure before recommending anything, including your own famous method. For a general-purpose solver, integrate complementary algorithms rather than crowning one.
**Evidence**:
- Stated: "understanding the characteristics of the objective function is crucial in large scale optimization" (1996 survey, preprint p. 2). Co-authored, 2006: "as is well known, no single approach is uniformly successful in nonlinear optimization" and "We take the view that interior-point and active-set methods will both be needed in the years to come" (doi:10.1007/0-387-30065-1_4). On Google's request, 2026 (caption-derived): "my first thing is don't use LBFGS here" [02 E8].
- Practice: "Our tests have convinced us that the partitioned quasi-Newton method of Griewank and Toint is an excellent method for large scale optimization" (doi:10.1007/BF01589116, preprint p. 24). A multilevel Gauss–Newton method, not L-BFGS, for ECMWF (doi:10.1007/s11081-008-9051-5; not read). KNITRO integrates interior (direct and CG) and active-set algorithms with crossover [01 SW1, SW3, SW6].
- Say–do consistency: ✅ stated + practised (the Google story is stated only).
**Steps**:
1. **Look for structure first**: least squares, partial separability, sparsity, bounds only.
2. **Run your method against the structure-exploiting alternative on the client's problem** and let the numbers decide.
3. **Recommend the structured method even if it is not yours.** Keep the general method for when the structure is unknown: L-BFGS uses "only function and gradient values" (1989, preprint p. 3).
4. **For a general-purpose solver, integrate complementary algorithms with crossover**, as integrated LP/MIP packages did (2006, preprint p. 2).
5. **Compare the integrated parts like with like and record where each loses**: SLQP "is robust, but is not as effective as gradient projection at identifying the optimal active set" (doi:10.1007/978-3-540-79409-7_18).
   - 🔴 If a user asks how to use method X on their problem, first check whether the answer is "don't".
**Applies to stage**: problem choice; solver architecture.
**Different from standard practice**: exploiting structure is common; recommending against his own famous method is not.
**Limitations**: the ECMWF account rests on the 2026 interview (paper not read). Integration needs a team, and conflicts with Curtis's preference for one adaptive algorithm (inferred).

**Full-text evidence (2026-10-17):**

**Full-text evidence (08 §2.6).** Distinct works: 49 evidence (40 full or partial), 7 variant, 1 contradiction; 54 works with any link; 60 card entries. (08 counts every read level; SKILL.md uses the regenerated list at the end of this section.)

- **Strongest full-text evidence**: the co-authored ECMWF case study explains why quasi-Newton Hessians, his own family, were rejected for operational 4D-Var (too few iterations; the least-squares structure); which choices are the authors' own is not stated [S047 pp. 1, 13], so this is the paper's argument, not documented personal practice (after review, 2026-10-17): "Moreover, a quasi-Newton approximation to (6) ignores the “least-squares” structure of this Hessian, namely, that the first term in (6) involves only first-derivative information." [S047 pp. 7–8]; the 1997 survey shows his own L-BFGS losing to Newton and partially separable quasi-Newton [S049 pp. 2–7, 13–15] *(inc-ocr, C17: mostly in evaluations, 7 of 8 rows, with time split 5–3 (card's count) and a stated reliability gap [S049 pp. 15–16]; the quasi-Newton loss in prose only)*; partitioned quasi-Newton recommended over the own method [S002 p. 24; S019 pp. 29–30]; the own codes' structure-blindness printed as a drawback [S003 p. 23; S005 p. 3]; specialist bound-constrained codes beat the general solvers [S105 pp. 7, 20]; SG, not L-BFGS, at the centre of the ML map [S004 pp. 16–19, 78]; the sub-sampled Newton method twice as fast as L-BFGS on its problem [S023 pp. 4, 16]; the own preconditioner scoped against incomplete Cholesky [S098 pp. 4, 8; S030 pp. 12, 18]; interior and active-set integration on the LP/MIP analogy [S011 pp. 2–3, 20–22]; owners of an interior code build and benchmark an active-set alternative [S035 report pp. 2, 29–30]; FIBO recommended only for its cost structure [S150 pp. 2, 5, 8–9].
- **C10**: the base Limitation *paper not read* (ECMWF) is replaced: the paper confirms the Gauss–Newton choice and its reasons, credits the multilevel method to Courtier et al., and does not say which parts are the authors' own [S047 pp. 1, 13, 16]. Mark unchanged: ✅ stated + practised 1989–2026.
- **Contradiction**: a 1990 nonlinear least-squares application solved with L-BFGS and compared only with general CG and quasi-Newton codes [S197 p. 2].
- **Variants**: L-BFGS named the universal choice for structured sparse inverse covariance [S043 p. 7]; structure exploited inside the generic method's linear algebra [S014 pp. 15, 17–18]; general-purpose robustness preferred to MPCC structure [S051 p. 28].
- **Variant: integration at the algorithm level.** Besides KNITRO's code-level integration, one parameterized family with two classical methods at its ends: the variable-storage family between CG and BFGS with storage as the knob [S138 pp. 7, 77–79; S120 pp. 23–24, 27]; memory m in L-BFGS-B [S143 pp. 2–3, 9]; HFN and L-BFGS interlaced, both as special cases [S077 pp. 3, 5; S088 p. 2]; a flexible penalty spanning a fixed penalty and a one-element filter [S081 pp. 4–5]; SL-QP to SQP through one model [S114 pp. 2, 8]; a semismooth Newton framework generating the rival ℓ1 classes [S064 preprint pp. 2–6]; the strongest rival recast as a wasteful parameter setting of the own scheme [S015 p. 27]. Placing rivals inside one family is shared with Toint (Method 2 step 5, *unify*) and Gill (Method 3, *old-family check*), so it stays a variant.
- Step 1 detail: an application's constraining features listed and numbered, each later choice derived from them [S047 pp. 5–6]; formulation chosen by storage, stability and cost [S047 pp. 9–11].

**Increment inc-ocr (2026-10-17)** (round-4 cards c4-01 to c4-04 and s4-01, second reads from an OCR text layer; one piece of evidence with each work's earlier card; numbers from the round-4 cards; 08 §12). Count: 42 works (39 evidence, 8 variant, 1 contradiction), was 42 (38, 6, 1): S014 adds an evidence link, S019 and S088 variant links.

- **C17**: in the 1996 survey's Tables 2–3 (L-BFGS and L-BFGS-B at m = 5 against LANCELOT's Newton at defaults: "The memory parameter for L-BFGS was set to m = 5, and LANCELOT was run with all its default settings" [S049 p. 15]) his codes need more evaluations on 7 of 8 rows and less time on 5 of 8 (FMINSURF, EIGENCLS, JNLBRNGA, LINVERSE, OBSTCLAE) (card's count) [S049 pp. 15–16]; the loss to partially separable quasi-Newton is asserted in prose, without numbers [S049 pp. 13–14]. The rows are the rounded m = 5 and LANCELOT-Hessian entries of S005's tables, FMINSURF excepted [S049 pp. 15–16; S005 pp. 10–11].
- **1989, the PQN recommendation in numbers**: with variable reduction (Table 18, p. 19) PQN needs fewer evaluations on both problems, wins on time on problem 9 (53 or 62 time units against L-BFGS's 1608) and only ties on problem 10 (853 or 854 against 964); without it (Table 19, p. 20), it still needs fewer evaluations in 27 of 30 runs, the exceptions being problem 3 from the finite-difference start at both sizes (55 against 48) and problem 14 at n = 100 from the scaled-identity start (30 against 28) (card's count; the n = 100 rows read from the page image), loses on time on problems 10 and 4, and keeps the dense problem 12 on purpose as a misapplication (storage 23357, time 14871 or 21290 against 293) [S002 pp. 19–20] (pages corrected after review); "We observe large variations in the iteration time of PQN: for most problems it is 2 to 5 times larger than that of L-BFGS." [S002 p. 21]; PQN is recommended when the element functions depend on fewer than 4 or 5 variables [S002 p. 24]. The 1992 survey restates the crossover as more than 5 or 6 element variables [S019 p. 30]; a threshold should cite S002 (variant, c4-01).
- **The own codes' structure-blindness, sized**: L-BFGS-B at m = 5 needs more evaluations than LANCELOT-Hessian on 27 of 28 converged bound rows and 28 of 31 converged unconstrained rows (card's count) [S005 pp. 10–11], and 13–47 times LANCELOT's evaluations on the largest bound problems (card's ratios) [S003 pp. 20, 22].
- **Structure inside the generic method's linear algebra, with counts** (step 5 evidence): H_ke_i costs 2mn + O(m²) against (4m − 1)n for the two-loop recursion; reduced-Hessian work is proportional to t rather than n; the incumbent recursion is kept for a non-scalar initial matrix [S014 pp. 15, 17–19]; "Of course for large problems the term 4mn predominates." [S014 p. 13].
- **No code wins every class (2003)**: leaders differ by class and size, and the first-order SNOPT leads the general *all* row by one problem [S078 p. 15]. **Structure decides the norm (1998)**: ℓ2 wins the dense problems (SPARSINE 36.5 s against 1047.5 s and > 1800 s); the new norm alone solves NONCVXUN [S101 p. 13].
- **Variant (algorithm-level integration)**: two complementary methods combined, not one crowned [S088 p. 2].

**All card links** (regenerated 2026-10-17 for increment inc-ocr from the digests' `method_links`, with the SKILL.md counting rule: full or partial cards only; abstract- and metadata-level cards, NSF award records and the group-voice S063, S179, S188 listed apart and not counted; S126 counted with S042 and S056 with S143; for the six works upgraded in round 3 only the deeper card is used; the earlier and later cards of the 26 twice-carded works (ten re-read in round 2, sixteen in round 4) are labelled by batch, one work each, round-1 pages prose only). Counted: 42 works, 55 card entries:

- **Evidence** (39 works, 49 card ids): S002 p. 24 (c01); S002 pp. 19–21, 24 (c4-01); S003 p. 23 (c02); S003 pp. 20, 22–23 (c4-02); S004 pp. 3, 16–19, 34–37, 48, 72–73, 78–79; S005 p. 3 (c02); S005 pp. 3, 10–11 (c4-02); S007 p. 1; S011 pp. 2–3, 20–22; S013 p. 2; S014 pp. 13, 16, 18–20, 25 (c4-01); S019 pp. 10, 29–30 (c02); S019 pp. 10, 30 (c4-01); S023 pp. 4, 16, 19; S030 pp. 12, 18 (c2-01); S034 p. 20; S035 report pp. 2, 29–30 (c2-01); S035 report pp. 29–30 (s04); S041 pp. 3–4, 9, 23; S043 pp. 5–7; S047 pp. 7–8, 13; S049 pp. 13–16 (c4-02); S049 pp. 2–7, 13–15 (c03); S050 pp. 14–17, 19; S053 p. 15; S076 pp. 2–3; S077 p. 3 (s03); S077 p. 3 (s2-01); S078 p. 15 (c4-04); S078 pp. 2, 13–15 (c04); S080 arXiv pp. 5, 18–20; S088 p. 2 (s02); S089 pp. 3, 12–13; S092 pp. 10, 13–14; S098 pp. 4, 8 (s03); S098 pp. 4, 8 (s2-01); S101 pp. 12–14 (s02); S101 pp. 12–14 (s4-01); S105 pp. 7, 20; S111 p. 21 (s2-01); S113 pp. 10–11, 21; S118 p. 8; S119 pp. 3, 9 (s04); S138 p. 7; S139 pp. 2–3, 14; S143 p. 3; S150 pp. 2, 5, 8–9; S193 p. 2; S197 pp. 2–4.
- **Variant** (8 works, 9 card ids): S014 pp. 15, 17–18 (c02); S014 pp. 15, 17–19 (c4-01); S019 p. 30 (c4-01); S043 p. 7; S051 p. 28; S064 preprint pp. 2–6; S081 pp. 4–5; S088 p. 2 (s4-01); S119 p. 3 (s2-01).
- **Contradiction** (1 work, 1 card id): S197 p. 2.
- **Not counted** (abstract- or metadata-level, award records, group voice): evidence: S010; S025; S063 pp. 4, 37–38, 42 (group voice); S070; S100; S152; S166; S179 p. 1 (group voice); S186 (award); S195 (award); S198 (award) — variant: S125.


**Increment inc-book (2026-10-17)** (book material B001–B012, cards c5-01 to c5-03: the open parts of *Numerical Optimization*, its errata, two reviews, the authors' book pages and Springer's catalogue pages; joint voice of Nocedal and S. J. Wright unless marked; dating and framing only, never in a say–do count; 08 §13, #textbook). Count unchanged: 42 works (39 evidence, 8 variant, 1 contradiction).
- **Not counted** (book material, joint voice, framing): B005 pp. 13–14: the 1999 Chapter 9 sets L-BFGS, the compact representation and three partial-separability sections (with a subsection *Sparsity vs. Partial Separability*) side by side, and nonlinear least squares and nonlinear equations get chapters of their own; this confirms from the contents the metadata-level S010 link of a2-02. The 2006 edition cuts partial separability to one section, 7.4 [B001 p. 10; B005 p. 14] (title-level; the preface does not mention it). Not exclusive: Wright's Method 6 and taste mark 6.

---

<a id="method-7"></a>
## Method 7: Decouple the curvature sample from the gradient sample (new, 2026-10-17)

**Promoted from the full texts (08 §4).** Cluster merged by meaning from the candidates *asymmetric accuracy*, *allocate sample accuracy by component tolerance*, *decouple and amortize noisy estimates* and part of *error balancing*: S023, S018, S015, S033, S004, S032, with S031 as a further instance; seven distinct works read in full or in part, 2011–2019. Title: 08 proposed *Spend accuracy where the iteration needs it*; after review (2026-10-17) the method is named after its exclusive device, and the principle stays the rationale in the One line. Card links (corrected after review): the cards link S018 (c07), S004 (c09), S031 (c10) and S033 (s06) to Method 3 as evidence and S023 (c06) and S015 (c08) as variants; S032 (s07) has no Method 3 link; no card has a Method 7 link, because the method did not exist when they were read. The promotion rests on the new-pattern candidates that meet the ≥3-works threshold: *asymmetric accuracy* (S023, S032), *allocate sample accuracy by component tolerance* (S004), *decouple and amortize noisy estimates* (S015) and *error balancing for inner solves* (S018, S032).

**Four checks** (research-extraction-framework §三):
1. **Cross-project recurrence** ✅: SAA Newton-CG and stochastically initialized L-BFGS on Google speech data (2011) [S023 pp. 3, 5–6, 10]; dynamic gradient samples with a fixed Hessian/gradient sample ratio and a CG stop tied to the Hessian sampling error (2012) [S018 pp. 4–5, 15–17]; stochastic quasi-Newton with curvature pairs on their own sample and a slower clock (2016) [S015 pp. 5, 8–9]; multi-batch and fault-tolerant L-BFGS with pairs on batch overlaps (2016) [S033 pp. 3–5]; overlap pairs in progressive batching (2018) [S031 pp. 4–5]; the SIAM Review account of both devices (2018) [S004 pp. 53–54, 57–58]; the theory: a constant Hessian sample suffices for a linear rate while the gradient sample must grow geometrically [S032 arXiv pp. 6, 8, 11]. Four distinct projects (SAA second-order, stochastic quasi-Newton, distributed L-BFGS, subsampled Newton theory) over eight years.
2. **Say–do consistency** ✅: the principle is stated as the design rationale: "Our approach is based on the fact that less accuracy in the Hessian is required than in the gradient" [S023 p. 3]; "This observation is based on an important property of Newton-like methods, namely that there is much more freedom in choosing a Hessian approximation than in computing the gradient [7, 3]." [S033 p. 3]; the why of the second device: "quasi-Newton updating is inherently an overwriting process rather than an averaging process, and therefore the vector y must reflect the action of the Hessian of the entire objective F given in (1.1)" [S015 p. 5]. Outside the cards, a spoken statement independent of the papers, from the Purdue 2017 talk transcript (uploader subtitles, caption-derived, `references/sources/talks/2017-02-15_purdue-distinguished-seminar_srg3Rx2HvfQ.txt`, [0:51:41]): "The sample for the Hessian here is going to be smaller than the sample for the gradient because the gradient is more important than the Hessian." Practice matches the statement in every work of the cluster.
3. **Executable, and different from standard practice** ✅: the steps produce actions that differ from the default of one mini-batch for every quantity and an update at every step. The strongest rival is recast as exactly that default and shown wasteful: oLBFGS ≈ SQN with L = 1 and b = b_H, an inefficient allocation of effort [S015 pp. 26–27].
4. **Exclusivity** ✅: no other member's SKILL.md treats sample allocation between gradient and curvature (searches of the nine other skills for subsampled Hessians, curvature pairs, sample sizes and stochastic quasi-Newton, rechecked 2026-10-17, found nothing outside this skill; Curtis's Method 1 mentions a sample-size schedule as one possible outer need). Curtis co-authored only the survey [S004]. Overlaps, all cited as shared, not claimed: tying the inner CG stop to the outer error [S018 pp. 15–17; S032 arXiv pp. 16–17] is close to Curtis's Method 1 (the inner solve serves the outer solver); step 3's adaptive gradient sample falls under that method's ⚠ variant (a step-size or sample-size schedule as outer need; frank-e-curtis/SKILL.md Method 1); the accuracy-by-need principle echoes its *the merit model sets the accuracy*. Claimed as Nocedal's (after review, 2026-10-17): curvature on its own sample and clock, a constant Hessian sample, pricing every component in gradient evaluations; none of these is in another member's skill.

**Explanatory gain**: in S023 the trigger is cost, not a failure [S023 pp. 5, 10]; in S015 the repair is a design of sampling and schedule, not one driven by an explicit noise-level estimate [S015 pp. 5–7, 19]. The four Method 3 evidence links do not absorb the pattern: they record that the classical engine is kept and one component made regime-aware (the dynamic gradient sample [S018 pp. 4–6, 15–18]; sample-variance tests [S031 pp. 3–5]; overlap pairs [S033 pp. 2–3, 6–8]; the survey's account [S004 pp. 45, 53, 57–58]), while the allocation of samples and clocks between gradient and curvature, which is what Method 7 prescribes, is outside Method 3's steps. Method 3 does not explain what is sampled, how much and on which clock; Method 7 does, and it gives the routing table a home for the design of a subsampled or stochastic second-order method.

**Further evidence by step**: printed settings (per problem class, not defaults): Lb/b_H ∈ [2, 20], M ∈ [4, 20], L = 20 [S015 pp. 9, 29]; m = 10, θ = 0.9, c1 = 10⁻⁴, skip when yᵀs ≤ ε‖s‖² with ε = 10⁻² [S031 p. 5]; |S0| = 512, 25% overlap, own parameters untuned across data sets [S031 p. 6]; θ = 0.5, initial sample 1% of N, R = 0.1 [S018 p. 19]; step size from the expected-decrease inequality, α = 1 in the noise-free limit [S031 pp. 4, 11]; constant step [S033 p. 4]; recovery: skipped updates and a moving-window fallback [S031 pp. 4–5]; s–y monitoring proposed, not built [S015 p. 19]; step 2's cautious skip [S033 p. 6]. Step 3, progressive sampling as variance control [S018 pp. 4–5; S036 pp. 14–17; S031 pp. 4–5; S102 pp. 5, 8]; step 4, an equal work budget swept over a log grid [S041 p. 8]; step 5, the deterministic limit as a reported loss: "The SLM method cannot, however, be considered successful in this deterministic setting (where Sk = Xk) because, as shown in the last column of Table 1, the total number of CG iterations is too expensive, even with the reduction observed in outer iterations." [S023 p. 12].

**Limitations (full list)**: convex or strongly convex theory [S023 p. 7; S015 pp. 9–10; S032 arXiv p. 5], except fixed-step nonconvex bounds [S033 pp. 6–7; S031 pp. 5–6]; the theorems do not separate the method from SGD, so the case rests on numerics [S015 pp. 12–14]; one data set or single runs in several papers [S023 p. 16; S018 pp. 18–25]; on deep networks the progressive-batching method needs more gradient evaluations than SG and Adam [S031 p. 7]; serial SGD reaches similar accuracy at a similar rate at a 1% batch: "serial SGD achieves similar accuracy as the robust L-BFGS method and at a similar rate (e.g., r = 1%), at the cost of n communications per epochs" [S033 p. 7]; finite sums with cheap Hessian-vector products; the inner-solve step overlaps Curtis's Method 1. Four of the seven works are co-authored with Byrd (S023, S018, S015, S032).

**Placement**: appended as Method 7 so that the cards' references to Methods 1–6 stay valid; the skill reaches the 7-method limit. Roundtable Card *Leads when* gains *sampled second-order methods*.


**Increment inc-ocr (2026-10-17)** (round-4 cards c4-01 to c4-04 and s4-01, second reads from an OCR text layer; one piece of evidence with each work's earlier card; numbers from the round-4 cards; 08 §12). No new evidence: the sixteen re-read works date from 1989–2004, before the sampled methods.

---

<a id="workflows"></a>
## Stage workflows

**Base-tier text (verbatim, SKILL.md of 2026-09-28):**

### Stage Workflows

#### Workflow A: Choosing a problem, a direction or solver ideas
**Input**: a practitioner's request, a failure report, a consensus claim, or "ideas to improve our solver".
**First move**: get (or assume, and say so) one failing run's log (Heuristic 2) and the solver's hard-coded safeguards and parameter rules.
**Steps**:
1. Structure check; if structure exists, benchmark against the structure-exploiting method first (→ Method 6).
2. Draw at most one candidate per source: a recurring failure in the log (→ Method 4); a "necessary" safeguard never compared against the simple option (→ Method 2); a component that breaks under noise or inexactness (→ Method 3); an undecided choice, e.g. the barrier or penalty update, to expose as an option (→ Method 4).
3. Keep at most three that pass the scale test (Taste mark 3), ranked by Taste quick-check item 1, each with a first experiment (Workflow C) and the result that would kill it.
4. In a new field, survey or teach it before pushing your method (→ Heuristic 9).
**🔴 Checkpoint**: if the honest answer to "use your method here?" is no, say so; drop what cannot scale; an idea that fixes no logged failure and tests no received wisdom is "not Nocedal-style".
**Output**: incumbent, structure, at most three ideas with source, first experiment and kill result.

#### Workflow B: Algorithm design and repair
**Input**: a classical method in a new regime (noise, sampling, inexact subproblems, infeasibility).
**Steps**:
1. Try the naïve adaptation first and record the result (→ Heuristic 4; SQN v1's "A Preliminary Approach", arXiv:1401.7020 v1).
2. Name the failing component, design an estimate-driven repair, add recovery and exit flags (→ Method 3).
3. Robustness first; defer fast local convergence (→ Heuristic 6). Analyse the version you will ship (→ Method 5).
**🔴 Checkpoint**: a naïve adaptation "neither faster nor more robust" than the baseline is recorded and dropped; unknowable constants are replaced by estimation plus recovery.
**Output**: algorithm with estimate, recovery tree, exit flags, undecided choices (→ Method 4).

#### Workflow C: Experiment design and benchmarking
**Input**: prototype, incumbent codes, test set (CUTEst, COPS, an application).
**Steps**:
1. Method 1, steps 1–7.
2. Failure demo first; if noise or inexactness is in scope, noise-free, then perturbed, three arms (→ Heuristics 1, 3).
3. Instrument the inside; run the idea inside the production code against its default (→ Heuristics 2, 8).
4. Repeat stochastic runs (five is his recurring default [03 §2.3]).
**🔴 Checkpoint**: do not run until stopping tests are aligned and tuning is equal (Method 1); state a single noise model or test class as a limit.
**Output**: protocol: codes, versions, options, tolerances, budgets, failure definition.

#### Workflow D: Judging results and writing up
**Input**: runs, profiles, internal diagnostics.
**Steps**:
1. Plot the bound against the runs (→ Method 5); put the losses in the abstract (Taste mark 8).
2. Record surprise as surprise; turn an unexplained regularity into a conjecture: "We conjecture that a self-correction mechanism may be at play" (2009) [03 §2.5].
**🔴 Checkpoint**: narrow any headline broader than the evidence (his own counterexample, arXiv:1609.04836); give illustrative problems an aggregate.
**Output**: claim, evidence, losses, limitations, open questions.

#### Workflow E: After publication: critiques, versions, software
**Input**: reviews, rival benchmarks, counterexamples, bug reports.
**Steps**:
1. Concede technical errors fast; run the reviewer's check (a scale-invariance claim withdrawn within days) [03 §4.1].
2. Answer a benchmark or counterexample with an algorithm variant, crediting the rival (→ Method 4).
3. Publish corrections as versioned code and errata (→ Heuristic 7); track what each reply promised.
**🔴 Checkpoint**: before closing a critique, check that each promised change was delivered (the ICLR reply promised "LB solution" wording; v2 still says "minimizer" 45 times [03 §4.1]); unanswered ML critics [05 §1] are a weakness, not a method.
**Output**: changelog; next papers from the failure-mode register.

#### Workflow F: Triage of a stuck solver
**Input**: a run that stalls, fails in the line search or restoration phase, or never meets its tolerance, with its log.
**First move**: get (or assume, and say so) the tolerance, the error level in f, c and derivatives, and the last iterations' step norm, merit decrease and KKT residual. No redesign yet.
**Steps**:
1. Estimate the error level (ECnoise or difference tables) and compare it with the decrease the line search or ratio test demands near the stall (→ Method 3, steps 3, 5).
2. Reproduce on one small, easy problem, printing skipped updates, radius, merit decrease, quasi-Newton condition number and feasibility; run it with exact values where possible and as reported, unmodified (→ Heuristics 1–3).
3. Name one failing component (update, line search, ratio test, difference interval, penalty parameter) → Workflow B, step 2.
**🔴 Checkpoint**:
- Demanded decrease below the error level → the stall is expected: relax only that test, add a noise-level exit flag (Method 3), report the attainable tolerance; no redesign.
- The exact run fails too → drop the noise hypothesis; check published failure examples (Step 2). Degeneracy or KKT linear algebra → "not Nocedal-style"; suggest the Wright, Gill or Wächter lens.
- No single component named → report the diagnostics; propose no new algorithm.
**Output**: error estimate, named component, table of the arms actually run, one repair with its ablation (Method 3, step 5).

**Full-text evidence (2026-10-17):**

Techniques added to the steps in SKILL.md, with their cards (details in the technique catalog):
- **A, step 1**: an application's constraining features as a numbered list before any choice [S047 pp. 5–6]. **Step 2**: a sampled component given the wrong accuracy (Method 7).
- **B, step 1**: a stochastic idea first in its deterministic limit, reported if it loses [S023 p. 12]. **Step 2**: the zero-noise collapse check [S071 pp. 13, 25; S082 pp. 11, 23]; the estimate validated (Heuristic 12). **Step 4** (new): sample allocation by Method 7.
- **C, step 1**: aligned stopping tests and identical success [S035 report pp. 19–21; S078 pp. 6–7]; a same-solution filter [S002 p. 8; S029 p. 7] *(inc-ocr, C14: S002 checks only)*; log₂ ratio plots for two-solver comparisons [S053 p. 13; S080 arXiv p. 9; S150 p. 7]. **Step 2**: infeasible instances made from feasible ones by one added constraint or bound [S052 pp. 18–19; S073 p. 23]. **Step 3**: a rival-neutral target from a derivative-based reference solve [S040 pp. 12–13; S062 pp. 4–5]. **Step 4**: a cost axis that charges every sample [S023 p. 16; S018 p. 19; S015 p. 15; S041 p. 8].
- **D, step 2**: surprise recorded as surprise [S062 pp. 2, 5, 7; S029 p. 21; S041 pp. 7–8; S057 p. 18]; conjectures labelled [S042 p. 5; S062 pp. 6, 9]. **Step 3** (new): a limitations section before any result [S080 arXiv p. 7]; a ranking disclaimer next to the results [S003 p. 23; S078 p. 2] *(inc-ocr, C18: in S078 before the results)*; a comparison table labelled as a summary, not a ranking [S032 arXiv pp. 20–21].
- **E, step 2**: the counterexample analysed as a specification [S061 pp. 2, 14, 19–24].
- **F, step 2**: a misspecification sweep of the error estimate [S071 p. 20; S084 p. 19].
- No new workflow: 08 does not support one; Method 7 runs through Workflow B.


**Increment inc-ocr (2026-10-17)** (round-4 cards c4-01 to c4-04 and s4-01, second reads from an OCR text layer; one piece of evidence with each work's earlier card; numbers from the round-4 cards; 08 §12).
- **C, step 1**: the same-solution filter is drop-and-count in [S029 p. 7], drop only in [S012 p. 24] and a check only in [S002 p. 8] (C14).
- **D, step 3**: the 2003 disclaimer and the scope paragraph open the paper, before any result [S078 p. 2]; beside the results there are per-observation caution flags only [S078 pp. 10, 11, 14] (C18).
- **E, step 2**: the 2001 answer to a counterexample is a paper algorithm, not a production variant [S061 pp. 20–24] (#method-4).
- **F, checkpoint**: the run signature of a singular non-stationary point (C19): the step length and the cosine between direction and merit gradient go to zero while the merit-gradient norm stays bounded away from zero [S061 p. 18]; an implementation then shows either a tiny-step test firing or a line search failing in finite precision [S061 p. 8]: "It is clear that the conditions of Theorem 2.2 can lead to convergence to a singular non-stationary point in some cases, but whether it always does is an open question." [S061 p. 8]. The case covers Jacobians or active-constraint gradients that lose rank away from solutions [S061 pp. 18, 24]; degeneracy at solutions stays *not Nocedal-style*. The merit-function conclusion: such failure can occur with a KKT-based merit function but, under conditions, not with the barrier function [S061 pp. 18–19, 24]; *check the merit function first* is an inferred triage order (labelled in SKILL after review).


**Increment inc-book (2026-10-17)** (book material B001–B012, cards c5-01 to c5-03: the open parts of *Numerical Optimization*, its errata, two reviews, the authors' book pages and Springer's catalogue pages; joint voice of Nocedal and S. J. Wright unless marked; dating and framing only, never in a say–do count; 08 §13, #textbook).
- **E, step 3** (publish corrections as versioned errata), ✅ joint evidence: one errata sheet per printing of the first edition [B011 p. 3]; the second-printing sheet kept in three dated versions (September 17, 2004; February 13, 2006; October 2, 2008; card c5-03 from Internet Archive captures), its last update correcting its own item 76 [B008 pp. 1, 6]; later sheets repeat or re-correct earlier fixes (the proof constant on book page 91 changed twice; the (5.37) fix in both sheets) [B007 p. 2; B008 pp. 2–3]. ⚠ Variant: the second-edition list exists as two copies with different numbering, neither naming the other, both frozen since May 2008 [B003 p. 1; B004 pp. 1, 5]; the HTML errata page for the second edition still read "Errata in the Second Edition [not yet posted]" in 2016 [B011 p. 4]. Shared with Wright (his Workflow E and Heuristic 5), so not Nocedal-specific.

---

<a id="heuristic-1"></a>
## Heuristic 1: Failure demo first

**Base-tier text (verbatim, SKILL.md of 2026-09-28):**

1. **Failure demo first**: if a classical method breaks, show it on a small, easy, chosen problem with an internal diagnostic, then run the broad set. Case: the BFGS condition number on ARWHEAD (arXiv:2010.04352); "Failure of the Classical Trust Region Algorithm" (arXiv:2201.00973) [03 §2.4].

**Full-text evidence (2026-10-17):**

Full texts (08 §2.7): one chosen 2-D function with the trace as diagnostic [S020 p. 18]; GAUSSELM with ‖Δs‖ [S075 pp. 5, 14]; an analytic example before tests [S067 pp. 13–14]; two 1-D counterexamples revisited after the rule [S042 pp. 6–8, 13–15]; one example per theorem case [S052 pp. 17–21]; failure on an easy problem first [S071 pp. 2–3; S082 pp. 2, 4–5; S102 pp. 2–3]; motivate-and-revisit toy examples [S067; S042; S052] (08 §6).


**Increment inc-ocr (2026-10-17)** (round-4 cards c4-01 to c4-04 and s4-01, second reads from an OCR text layer; one piece of evidence with each work's earlier card; numbers from the round-4 cards; 08 §12). Powell's two-variable example, whose exact-line-search iterates converge to z ≈ (1.8016, 0), with F′ singular along the x-axis [S061 pp. 3–4]; a one-variable barrier example [S061 p. 17]; a three-variable example mapped onto a two-variable one [S061 p. 23].

---

<a id="heuristic-2"></a>
## Heuristic 2: Instrument the inside

**Base-tier text (verbatim, SKILL.md of 2026-09-28):**

2. **Instrument the inside**: print skipped updates, phase times, CG iterations, the radius; ship reference outputs. Case: L-BFGS-B 3.0 [03 §2.5].

**Full-text evidence (2026-10-17):**

Full texts: a safeguard-firing column [S012 p. 25]; trigger shares of the trust-region fallback [S013 p. 16]; the monotone-mode share [S029 p. 16]; the share of iterations with the wedge active [S040 p. 13]; internal counters beside profiles [S105 pp. 4–5, 7–8]; per-task time shares [S035 report p. 28]; the s–y angle and GradError/HvError [S015 pp. 19–21]; skipped-update counters [S005 pp. 6–7]; a log symptom → option map in the manual [S063 pp. 37–38] (product voice).


**Increment inc-ocr (2026-10-17)** (round-4 cards c4-01 to c4-04 and s4-01, second reads from an OCR text layer; one piece of evidence with each work's earlier card; numbers from the round-4 cards; 08 §12). The firing rate of a safeguard (M4's in about 5% of iterations) [S002 p. 15]; last-step CG iterations over n − t against the cap 2, and the share of full steps [S008 p. 22]: "the infeasible CG steps accounted for about 2% of the total" [S008 p. 16]; the per-iteration table of step, cosine, merit value and merit-gradient norm [S061 p. 18]; accepted and rejected steps, ρ and the eigenvalues of F′ᵀF′ [S061 p. 13]; user counters isave(26), isave(30), isave(34) and dsave(13) [S005 pp. 5, 7]; the waste column #f − #g traced to named causes: "the number of “wasted” function evaluations (the difference between #g and #f in in Table 4.1) is significantly higher for the new method than for its competitors" [S101 p. 14].

---

<a id="heuristic-3"></a>
## Heuristic 3: Noise-free before noisy, three arms

**Base-tier text (verbatim, SKILL.md of 2026-09-28):**

3. **Noise-free before noisy, three arms**: original; perturbed with the unmodified code; perturbed with the modified code. Case: arXiv:1803.10173 §2 [03 §2.4].

**Full-text evidence (2026-10-17):**

Full texts: §2 noise-free, §5 noisy, then the ablation [S038 pp. 3–5, 19–22]; the deterministic limit first, reported as a loss [S023 p. 12]; every section of [S080 arXiv pp. 9, 13]; identical noise in both arms [S082 p. 21].

---

<a id="heuristic-4"></a>
## Heuristic 4: Exhaust the alternatives, then commit to the simplest survivor

**Base-tier text (verbatim, SKILL.md of 2026-09-28):**

4. **Exhaust the alternatives, then commit to the simplest survivor**, living with the "fog" meanwhile. Case: L-BFGS: "I knew that it was right because I tried everything else" (2026, caption-derived) [02 J1, J5].

**Full-text evidence (2026-10-17):**

Full texts: Gill–Murray scaling dropped [S002 p. 15]; several selection strategies tried, the two simplest kept [S030 pp. 2, 20]; other HFN variants tried [S077 p. 10].

---

<a id="heuristic-5"></a>
## Heuristic 5: The cheapest adequate option wins ties; numbers as advice

**Base-tier text (verbatim, SKILL.md of 2026-09-28):**

5. **The cheapest adequate option wins ties; give parameter advice as numbers.** Case: "these two scalings are comparable in efficiency, and therefore M3 should be preferred since it is less expensive to implement" (1989); "3<= M <=7 is recommended" [01 SW1; 03 §2.7].

**Full-text evidence (2026-10-17):**

Full texts: the simple μ rule kept over superlinear rules [S013 p. 10]; "Values of m, in the range [4, 20], are recommended for most problems, independently of the value of n." [S098 p. 4] (round-2 card s2-01); ν0 = 10, ε1 = 0.1, ε2 = 0.5 [S042 p. 13]; ECnoise with 4 or 6 evaluations [S038 p. 12]; PLA defaults [S139 pp. 6, 10–11, 14]. Pricing every device in base-iteration units: one backsolve [S075 p. 15]; under 4% extra simplex iterations [S035 report p. 16] (round-2 card c2-01); factor × maxcg ≈ 1 [S023 p. 6]; the SQN cost ratio [S015 p. 8]; 4md and 2m + n [S004 pp. 47, 57]; operation counts against each alternative [S014 pp. 12–13, 19–20]. *Price devices in base units* was not added as a new item: it is this heuristic (08 §10, item 11).


**Increment inc-ocr (2026-10-17)** (round-4 cards c4-01 to c4-04 and s4-01, second reads from an OCR text layer; one piece of evidence with each work's earlier card; numbers from the round-4 cards; 08 §12).
- **Variant, memory ranges by year**: the 1989 study advises low storage and accurate searches for cheap functions and m from 3 to 7 with an inexact search for expensive ones [S002 p. 18] (the OCR prints 3 < m < 7; the page image prints 3 ≤ m ≤ 7, verified after review); m ∈ [3, 7] in the 1992 survey [S019 p. 31] and the compact-representation paper [S014 p. 3]; 3 ≤ m ≤ 20 in the L-BFGS-B code report of December 1994 [S005 p. 3], the 1996 survey [S049 p. 14] (read from the page image; the OCR prints [8,20]) and DINEMO [S088 p. 4]. SKILL.md now gives both.
- **Numbers as defaults**: NITRO's list (η = 10⁻⁸, τ = 0.995, θ = 0.2, ζ = 0.8, ε_TOL = 10⁻⁷, initial ε_μ = μ = 0.1, Δ0 = 1) [S008 p. 19]; L-BFGS-B's factr table (1.d+12, 1.d+7, 1.d+1) and storage formulas [S005 pp. 2–4]; the trust-region constants of the norm study (ε_g = 10⁻⁵, η1 = 0.01, η2 = 0.95, γ1 = 0.5, γ2 = 2) [S101 p. 11]; σ₁ = 10⁻⁴ and σ₂ = 0.9 for BFGS [S019 pp. 16–17]. Variants with no printed values: the reduced-Hessian theory paper defers every constant to its companion [S028 p. 34]; the superlinear barrier strategies are conditions on exponents [S046 pp. 16–18]; the trust-region constants c1–c4 of the hybrid's runs are not reported [S024 pp. 19–20].
- **Cheapest adequate option, with counts**: γ_k free because both inner products are stored, σ_k one multiplication, the compact update 2mn against (3/2)m²n for the straightforward approach [S014 pp. 13, 16, 20]; M3 preferred to M4 at comparable efficiency [S002 p. 15]; the residual update costs no more than refinement in all 28 problem × mode cells (card's count) [S021 p. 24]; operation counts for the three subspace solvers and their crossover (citer < m/2) derived before the runs [S003 pp. 13, 15].

---

<a id="heuristic-6"></a>
## Heuristic 6: Robustness before speed in a first code

**Base-tier text (verbatim, SKILL.md of 2026-09-28):**

6. **Robustness before speed in a first code**, with naïve failure tests. Case: NITRO: "No attempt was made to obtain a rapidly convergent method" (1999); Curtis's thesis implements "naïve failure tests … to aggressively challenge the robustness of our approach" (2007, p. 50) [04 §3.3].

**Full-text evidence (2026-10-17):**

Full texts: the rate deferred on practical grounds [S029 p. 22]; NITRO's linear barrier decrease [S008 p. 23]; speed-ups deferred [S064 preprint pp. 17–18]; global theory first, rate deferred [S009 pp. 9, 33].


**Increment inc-ocr (2026-10-17)** (round-4 cards c4-01 to c4-04 and s4-01, second reads from an OCR text layer; one piece of evidence with each work's earlier card; numbers from the round-4 cards; 08 §12). μ falls by a factor of 5 per barrier problem (θ = 0.2), linear by design [S008 pp. 4, 19, 23]; the companion analysis proves those settings only linearly convergent [S046 p. 16]; the rate is deferred in the theory [S009 pp. 9, 33].

---

<a id="heuristic-7"></a>
## Heuristic 7: Code as a numbered, maintained artefact

**Base-tier text (verbatim, SKILL.md of 2026-09-28):**

7. **Code as a numbered, maintained artefact**: proven components, marked changes, old versions kept, errata. Case: the L-BFGS-B Remark (doi:10.1145/2049662.2049669); 80 numbered book errata [03 §2.7, §4.3].

**Full-text evidence (2026-10-17):**

Full texts: the Remark replaces a machine-precision constant wrong by two orders of magnitude and corrects the old version's accounting in its favour [S016 preprint pp. 1–2]; graded drivers and a must-read driver [S005 pp. 5–6]; a numbered TOMS algorithm [S098 pp. 6–7]; the representation → algorithm → code staircase [S014 p. 3; S003 pp. 5, 23; S005 p. 2]. Software as a stated deliverable appears in award abstracts [S198; S196] and in the iNEOS network-service paper [S119]; not promoted (rests mainly on award abstracts, 08 §10 item 12).


**Increment inc-ocr (2026-10-17)** (round-4 cards c4-01 to c4-04 and s4-01, second reads from an OCR text layer; one piece of evidence with each work's earlier card; numbers from the round-4 cards; 08 §12). The staircase dated: the compact representations name their users, Byrd–Lu–Nocedal (1993) for bound constraints and Biegler–Nocedal–Schmid (1993) [S014 pp. 16, 25]; the code paper prints the code's skip test where it differs from the algorithm paper's [S005 p. 7; S003 pp. 6, 18]; the norm ships as HSL_VF06 [S101 pp. 1, 10]; L-BFGS as Harwell VA15 [S002 p. 4; S019 p. 3].


**Increment inc-book (2026-10-17)** (book material B001–B012, cards c5-01 to c5-03: the open parts of *Numerical Optimization*, its errata, two reviews, the authors' book pages and Springer's catalogue pages; joint voice of Nocedal and S. J. Wright unless marked; dating and framing only, never in a say–do count; 08 §13, #textbook).
- **C20**: the base text's *80 numbered book errata* [03 §2.7, §4.3] holds for Nocedal's copy of the second-edition list: "Corrections to Numerical Optimization, Second Edition Published August 2006 (Last updated May 27, 2008)" [B003 p. 1], 80 located items, three readers thanked [B003 pp. 1–5]; its item 12 removes a paragraph on book page 63. Wright's copy, "Corrections to Numerical Optimization, Second Edition Published August 2006 (Last updated May 17, 2008)" [B004 p. 1], has 79 items, numbered one lower from item 12 on, and is the copy Wright's skill counts (his 03 §2.1) [B004 pp. 1–5]; 03 §4.3's *item 12, Remove the paragraph* uses Nocedal's numbering. Both copies are byte-unchanged in the Internet Archive from 2008 to 2024, and Wright's is the only author-hosted copy still served (card c5-03, B004 D8).
- **First edition**: the first-printing sheet has 35 items plus a 4-item addendum dated 2/25/2000 [B007 pp. 1–7]; the second-printing sheet has 91 items, last updated October 2, 2008 [B008 pp. 1–7]; both are written as paste-ready LaTeX for the typesetter: "To make it easier for the typesetter, we have included in many cases an explicit correction of the offending passages" [B007 p. 1; B008 p. 1]. Neither names a finder [B007 pp. 1–7; B008 pp. 1–7].
- **Exclusivity**: the errata are joint, and keeping public errata is Wright's Heuristic 5; the Nocedal-specific evidence stays the code record [S016 preprint pp. 1–2; S005 pp. 5–6; S098 pp. 6–7]. ⚠ Variant: maintenance stopped in 2008, and the two second-edition copies were never reconciled [B004 pp. 1, 5]. SKILL's Heuristic 7 now names the copy (C20).

---

<a id="heuristic-8"></a>
## Heuristic 8: Prototype inside the production solver

**Base-tier text (verbatim, SKILL.md of 2026-09-28):**

8. **Prototype inside the production solver** and compare with its default. Case: "The original BO algorithm in knitro was modified by Figen Oztoprak from Artelys Corp." (arXiv:2411.02665, p. 29).

**Full-text evidence (2026-10-17):**

Full texts: Knitro/Direct [S013 p. 14]; the infeasibility mode inside KNITRO 8.0 [S053 pp. 12–13]; PLA inside knitro [S139 pp. 3, 14–17]; finite differences through KNITRO's own option [S080 arXiv p. 27]; a KNITRO failure observation as the start [S084 pp. 2–3].

---

<a id="heuristic-9"></a>
## Heuristic 9: Enter a field through a practitioner's problem

**Base-tier text (verbatim, SKILL.md of 2026-09-28):**

9. **Enter a field through a practitioner's problem, and publish the field's map before your own method.** Case: ECMWF, Google; *SIAM Review* 2018 (doi:10.1137/16M1080173) [06 T6, T9].

**Full-text evidence (2026-10-17):**

Full texts: ECMWF co-authors [S047 p. 1]; Google speech data and co-author [S023 pp. 1, 14]; IBM collaborators [S043 p. 1]; chemical process control [S067 p. 19]; the ML field map before the group's methods [S004 pp. 20, 40, 51].


**Increment inc-book (2026-10-17)** (book material B001–B012, cards c5-01 to c5-03: the open parts of *Numerical Optimization*, its errata, two reviews, the authors' book pages and Springer's catalogue pages; joint voice of Nocedal and S. J. Wright unless marked; dating and framing only, never in a say–do count; 08 §13, #textbook). ⚠ Variant, shared with Wright's Heuristic 6 (*Consolidate at the crest*): in 1999 the joint field map leaves out the authors' own live topic, interior methods for NLP, as current research [B005 p. 8], although both had open work on it (the reference list, B006 pp. 38, 48); in 2006 the topic gets a chapter because it "now forms the basis of successful codes for nonlinear programming" [B001 p. 21]. Pool candidate only (08 §13.8): one joint source, not exclusive.

---

<a id="heuristic-10"></a>
## Heuristic 10: A standing theory partner

**Base-tier text (verbatim, SKILL.md of 2026-09-28):**

10. **A standing theory partner in student projects.** Case: 15 of 22 students co-authored with Byrd, 1992–2022 [04 §3.2]; inferred from the record, person-specific.

**Full-text evidence (2026-10-17):**

Full texts (08 §9): Byrd co-authors 37 of the 96 distinct works read in full or in part, from 1987 [S020] to 2024 [S102], more than twice any other partner, in every five-year period 1985–2024; he is thanked rather than listed in several others [S002 p. 25; S029 p. 22; S053 p. 17; S082 p. 23]; no 2025–26 work lists him [S128; S150]; several 2018–2026 student works are without him (S031 S041 S080 S091 S124 S128 S150). Other partners: Waltz 14 works (2002–2014, KNITRO); Morales 10 (2000–2012); Oztoprak 7 (2012–2023). Collaboration table by period: #collaboration.


**Increment inc-book (2026-10-17)** (book material B001–B012, cards c5-01 to c5-03: the open parts of *Numerical Optimization*, its errata, two reviews, the authors' book pages and Springer's catalogue pages; joint voice of Nocedal and S. J. Wright unless marked; dating and framing only, never in a say–do count; 08 §13, #textbook).
- **Stated (1999)**, the only Nocedal-specific item in the book material, in the joint preface and the third person: "One of us (JN) would like to express his deep gratitude to Richard Byrd, who has taught him so much about optimization and who has helped him in very many ways throughout the course of his career." [B005 p. 9] (reprinted with the first preface in 2006, B001 p. 20). Added to SKILL.
- **Dating**: Byrd co-authors 8 of the 17 Nocedal entries in the 2006 bibliography, Waltz 4 [B002 pp. 42–43, 55]; in 1999 Nocedal and Byrd have 11 entries each [B006 pp. 36–48] (card's counts). The heuristic itself (Byrd in student projects) still rests on the record [04 §3.2].

---

<a id="heuristic-11"></a>
## Heuristic 11: Harvest the curvature the solver already computes (new)

New heuristic (08 §5). "The key idea is to preserve the information generated during the inner CG iteration to improve the quality of the limited memory matrix used in subsequent steps" [S088 p. 7]. Cases: CG pairs from one linear solve precondition the next, at no extra matrix-vector products [S030 pp. 2, 4, 6; S098 p. 4]; inner pairs feed the L-BFGS memory in a hybrid with both parents as special cases [S077 p. 3; S088 pp. 5–7]; quasi-Newton matrices mapped into a new null-space basis instead of reset [S067 pp. 11–12]; the origin of L-BFGS itself: "A disadvantage of these methods is that after a certain number of iterations the quasi-Newton matrix is discarded" [S007 p. 1]. Scope as printed: "the cost of applying the preconditioner is too high to offset the reduction in the number of CG iterations in these experiments" [S030 p. 12]; "Therefore the preconditioner is unlikely to be useful for very sparse problems." [S098 p. 8]. Ablation arm: identical except that the harvested pairs are discarded [S088 p. 8].
- Checks: executable ✅; recurrence ✅ (1980; 1996–2002, four works); exclusivity ✅ (no member's methods); say ✅ in the papers' own statements [S088 p. 7; S007 p. 1]. It would pass as a method, but the slot goes to Method 7 and no existing method is weak enough to replace; the paper credits prior art (Nash's matrix, O'Leary–Yeremin, Byrd–Nocedal–Zhu) [S030 p. 3]; the line ends in 2002 and its payoff is scoped by the authors. Heuristic, cross-referenced from Method 6's algorithm-level integration.


**Increment inc-ocr (2026-10-17)** (round-4 cards c4-01 to c4-04 and s4-01, second reads from an OCR text layer; one piece of evidence with each work's earlier card; numbers from the round-4 cards; 08 §12). The numbers, legible rows only: at ε = 0 and σ = .06/.12/.18, L-BFGS needs 131/138/151 evaluations and DINEMO 110/115/115, 16–24% fewer (card's percentages) [S088 p. 10]. DINEMO also takes discrete Newton steps, so this comparison does not isolate the kept pairs, and with Table 1's evenly spread eigenvalues its advantage deteriorates as ε grows until L-BFGS ends up the winner at ε = .09; DINEMO beats ALTERNATE except for large ε and σ [S088 p. 10] (scope added to SKILL after review); at ε = .09 (condition number 5073) DINEMO needs 222/333/274/331 against the discard arm's 364/405/444/435, 18–39% fewer (card's percentages) [S088 p. 11]: "Collecting information from the inner CG cycle and saving it in the form of a limited memory matrix is certainly beneficial since DINEMO clearly outperformed ALTERNATE in the great majority of the tests." [S088 p. 12]. Table 2 (12 distinct eigenvalues) is lost, so the eigenvalue-distribution conclusion rests partly on prose; one function family, n = 100, one starting point [S088 pp. 8–12].

---

<a id="heuristic-12"></a>
## Heuristic 12: Validate every in-algorithm estimate against the truth (new)

New heuristic (08 §5). Cases: the sample-variance estimate tabulated against the true gradient error over a real run [S018 p. 20]; model gradients measured against exact AMPL gradients instead of bounds with unknown constants [S062 p. 8]; GradError and HvError against full-data quantities [S015 pp. 20–21]; a misspecification sweep of the noise level from 1/10 to 10 [S071 p. 20]; the estimate run 10×, 100× and 1000× too large and too small [S084 p. 19]; the direction of failure written for each misestimate [S091 arXiv p. 12; S128 pp. 9–11]; one failure of the estimate computed by hand [S080 arXiv p. 17].
- Checks: executable ✅; recurrence ✅ (2009–2025, seven works, several co-author groups); exclusivity ✅ (Wright's floating-point check and Curtis's yardstick audit test other things); no stated principle found → heuristic. It fills a gap in Method 3, whose steps use explicit estimates but never say how to trust them.

---

<a id="anatomy-lbfgs"></a>
## Signature work: L-BFGS (1980, 1989; S007, S002)

**Base-tier text (verbatim, SKILL.md of 2026-09-28):**

### Signature Work Anatomy

Full anatomies: [01-publications](01-publications.md) (SW1–SW6). Not dissected (not read): the textbook (doi:10.1007/978-0-387-40065-5) and the ECMWF paper (doi:10.1007/s11081-008-9051-5), which he calls "my most important contribution" (2026, caption-derived).

#### On the limited memory BFGS method for large scale optimization (Math. Program. 45, 1989, doi:10.1007/BF01589116)
| Aspect | Content |
|---|---|
| Related | *Math. Comp.* 1980 (doi:10.1090/S0025-5718-1980-0572855-7; abstract only); L-BFGS-B (doi:10.1137/0916069; doi:10.1145/279232.279236); Remark 2011 |
| Origin | Stated (2026, caption-derived): "I went to the board and I realized I did the wrong thing in my thesis. All these methods are too complicated." |
| Why then | Inferred: storage was the binding constraint ("problems where the storage is critical", 1980 abstract) |
| Key insight | "The quasi-Newton matrix is updated at every iteration by dropping the oldest information and replacing it by the newest information" (1980 abstract) |
| Minimum evidence | Months of testing (stated); 1989: a controlled study against competitors' own implementations |
| Abandoned paths | The thesis programme; Gill–Murray scaling ("Its behavior seemed erratic … we do not report these results"); scaling M4 for the cheaper M3 |
| Reception | Poor reviews and Powell's dislike (stated); take-off after 1989 and the 1990 Harwell release; a correction 14 years after release |
| Method shown | Methods 1, 6; Heuristics 4, 5, 7 |

**Full-text evidence (2026-10-17):**

- **Read**: the 1980 paper in full [S007]; the 1989 study in part, prose only (its text layer lost all digits) [S002]; L-BFGS-B [S003; S005]; the 2011 Remark in the author preprint [S016 preprint].
- **Origin (full text)**: the 1980 entry is the wholesale discard of the quasi-Newton matrix by variable-storage CG methods: "A disadvantage of these methods is that after a certain number of iterations the quasi-Newton matrix is discarded" [S007 p. 1]; the product form makes dropping the oldest correction trivial [S007 pp. 2–3]; weak SQN results withheld but declared [S007 p. 9].
- **Minimum evidence (full text)**: competitors run "precisely as they recommend", a same-solution check, losses in the abstract, full data in a companion report [S002 pp. 2, 7–8]; uniform bounds for limited memory, every matrix being m updates of a bounded seed [S002 pp. 21–23]. Table-level claims still rest on the base-tier reading.
- **Abandoned paths**: Gill–Murray scaling dropped as erratic [S002 p. 15].
- **Method shown**: partitioned quasi-Newton recommended over the own method [S002 p. 24] (Method 6); two line-search modes as code options [S002 p. 13] (Method 4).
- **Reception**: the Remark, on the 1997 L-BFGS-B code (Algorithm 778) 14 years after its release, not on L-BFGS, fixes a machine-precision constant and re-accounts the old version [S016 preprint pp. 1–2, 4]; citations 4,373 (1980) and 13,019 (1989) in scholar.md.


**Increment inc-ocr (2026-10-17)** (round-4 cards c4-01 to c4-04 and s4-01, second reads from an OCR text layer; one piece of evidence with each work's earlier card; numbers from the round-4 cards; 08 §12).
- **Read**: the 1989 study is now read in full from the OCR text (c4-01): Tables 3, 4, 8, 9, 11, 14, 18 and 19 are legible; Tables 2, 5–7, 10, 12–13, 16–17 and 20 and the column headers of Tables 9, 14 and 15 are still illegible [S002 pp. 8–20]. The bullet above (*Table-level claims still rest on the base-tier reading*) is superseded for the legible tables.
- **Minimum evidence in numbers**: "In contrast, the L-BFGS method gives a substantial speed-up in 70% of the problems." [S002 p. 11], against little or none for Buckley–LeNir; B-L needs fewer iterations but about two evaluations per iteration (a forced interpolation), L-BFGS about one [S002 p. 9]; at m = 5 the scaling M3 cuts evaluations against M1 on every legible row but not against M2 on problem 12 (322 against 260) [S002 p. 14], a row the paper's tallies do not mention; M4's safeguard fires in about 5% of iterations [S002 p. 15]; n = 5000 and 10000 are solved in 14–183 iterations, and storage beyond m = 5 has little effect [S002 pp. 15–16]; PQN in #method-6 [S002 pp. 19–21]; Theorem 6.1, R-linear convergence from any positive definite start [S002 p. 23].
- **Credits**: the diagonal scaling M4 is Byrd's suggestion [S002 p. 25]; the code is to be released as Harwell VA15 [S002 p. 4].

---

<a id="anatomy-acta"></a>
## Signature work: Acta Numerica survey (1992; S019, S020)

**Base-tier text (verbatim, SKILL.md of 2026-09-28):**

#### Theory of algorithms for unconstrained optimization (Acta Numerica 1, 1992, doi:10.1017/S0962492900002270)
Thin (the underlying papers doi:10.1137/0724077 and doi:10.1137/0726042 **not read**). Origin (stated, caption-derived): Powell's convex BFGS proof (paper unidentified) prompted a family-wide analysis with Byrd; DFP was "already observed to be not as good as the BFGS method", and the question was why. Insight (his 2026 summary): the Broyden class converges except DFP, which lacks self-correction. Noise was set aside ("we will not consider these aspects here") for 27 years. Reception: Powell, "This is the best paper I read all year" (stated); the BFGS judgement was overtaken by Dai 2002. Shows Method 5.

**Full-text evidence (2026-10-17):**

- **C12**: the base anatomy was *thin*; the survey [S019] and the 1987 Broyden-class paper [S020] are read in full. The 1989 tool paper (doi:10.1137/0726042) is abstract-only [S017].
- **C13 (Powell's proof identified)**: the 1987 paper presents itself as a generalization of Powell's BFGS result and says it borrows heavily from his techniques [S020 pp. 1, 6]; its reference list gives Powell (1976), *Some global convergence properties of a variable metric algorithm for minimization without exact line searches*, Nonlinear Programming, SIAM-AMS Proceedings IX (Cottle and Lemke, eds.), confirmed against zbMATH (pp. 53–72). That this is the proof he recalls in the 2026 interview is inferred from the match.
- **Key insight (confirmed)**: the trace–determinant analysis singles out DFP, which lacks the self-correcting term [S020 pp. 7–10, 17, 19; S019 pp. 18–21]; one chosen 2-D function as a targeted run [S020 p. 18].
- **Structure**: four-way classification of results (global convergence, local convergence, rate, global efficiency) [S019 p. 2]; Zoutendijk proved in full as the hub [S019 p. 5]; numbered open questions [S019 pp. 17, 21–22]; partitioned quasi-Newton recommended [S019 pp. 29–30]; the steepest-descent argument [S019 p. 7]; the BFGS method left to evolve freely: "We have learned that it is preferable not to interfere with the BFGS method and to let the matrices … evolve freely, because convergence is usually obtained and the rate is superlinear" [S019 p. 7].
- **Reception**: Dai 2002 acknowledged in 2016 [S033 p. 6] (C1).


**Increment inc-ocr (2026-10-17)** (round-4 cards c4-01 to c4-04 and s4-01, second reads from an OCR text layer; one piece of evidence with each work's earlier card; numbers from the round-4 cards; 08 §12). Numbers now legible: the targeted run (#method-5) [S019 p. 24]; BFGS with a very loose line search, σ₁ = 10⁻⁴ and σ₂ = 0.9 [S019 pp. 16–17]; L-BFGS with m ∈ [3, 7] [S019 p. 31]; Open Question I on DFP open since 1976 [S019 p. 17]; trust regions left out because most of their unconstrained theory predates 1982 [S019 p. 3]. The Khalfan–Byrd–Schnabel SR1 rate: "Then the rate of convergence is 2n-step q-quadratic" [S019 p. 29] (the round-1 card c02 had *n-step*; the error is in no skill file).


**Increment inc-book (2026-10-17)** (book material B001–B012, cards c5-01 to c5-03: the open parts of *Numerical Optimization*, its errata, two reviews, the authors' book pages and Springer's catalogue pages; joint voice of Nocedal and S. J. Wright unless marked; dating and framing only, never in a say–do count; 08 §13, #textbook). **C21**: the base text's *Noise was set aside … for 27 years* holds for his research papers, where the noise programme opens in 2019 [S038 p. 1]. The joint 2006 textbook already opens its new derivative-free chapter with section 9.1 *Finite Differences and Noise* [B001 p. 10] and indexes noise in function evaluation at book pages 221–222 and noise under finite differencing at 221 [B002 pp. 59, 62]; what those pages say was not read. The 1999 edition has no noise entry [B006 pp. 49–60]. SKILL's sentence now carries the limitation.

---

<a id="anatomy-knitro"></a>
## Signature work: KNITRO (2006; S011, S013)

**Base-tier text (verbatim, SKILL.md of 2026-09-28):**

#### Knitro: An Integrated Package for Nonlinear Optimization (Large-Scale Nonlinear Optimization, Springer 2006, doi:10.1007/0-387-30065-1_4)
| Aspect | Content |
|---|---|
| Related | NITRO (doi:10.1137/S1052623497325107); Byrd–Gilbert–Nocedal (doi:10.1007/PL00011391, **not read**); follow-ups 2004–2014 (Method 4) |
| Origin | Stated (caption-derived): he expected a straightforward extension from LP/QP, and "in the non-convex case it doesn't work" |
| Why then | Inferred: interior methods had transformed LP (doi:10.1007/BF02579150); no robust nonconvex large-scale interior code existed |
| Key insight | "Rather than trying to mimic primal-dual interior point methods for linear programming, we have taken the approach of developing a fairly standard SQP trust region method" (1999, preprint p. 23) |
| Minimum evidence | Competitive with LANCELOT on large problems at a matched 10⁻⁷ tolerance; primal-dual beat primal [03 §2.1, §2.6] |
| Abandoned paths | Fast convergence deferred; "very conservative" refinement flagged; the CG step supplemented by direct factorization |
| Reception | NITRO "significantly slower and far less robust" on small problems (doi:10.1007/s10107-003-0418-2) → Knitro-Direct (2006); KNITRO 3.1.1 829/954 vs IPOPT 895, without an infeasibility message (doi:10.1007/s10107-004-0559-y) → infeasibility-detection SQP (2010); both arrows inferred from timing (Method 4) [05 §4] |
| Method shown | Methods 4, 6; Heuristics 6, 8 |

**Full-text evidence (2026-10-17):**

- **Read**: the package paper [S011 pp. 1–3, 5–7, 14–15, 20–22]; Knitro/Direct [S013]; NITRO [S008]; the Byrd–Gilbert–Nocedal theory [S009] (C11: *not read* in the base tier).
- **Key insight**: three algorithms (interior/direct, interior/CG, active set) with crossover, on the analogy with integrated LP/MIP packages [S011 pp. 2–3, 20–22]; line-search steps guarded by a trust-region fallback with a radius hand-off [S013 pp. 5, 8, 12; S011 pp. 5–7]; inner and outer tolerances coupled so the barrier subproblem is never oversolved [S013 pp. 10–12].
- **Minimum evidence**: NITRO and LANCELOT stopped at the same 10⁻⁷ [S008 pp. 20–23] *(inc-ocr, C16: see below)*; Knitro/Direct against Knitro-CG sharing all other components [S013 p. 14].
- **Reception**: the infeasibility arrow is partly documented by the 2014 paper [S053 p. 4] (C6); the barrier arrow stays inferred [S029 pp. 2, 17–21].
- **Gap**: no card documents how the integration and crossover were tuned [S011 pp. 20–22]; the KNITRO 2.0 manual is metadata only [S066].


**Increment inc-ocr (2026-10-17)** (round-4 cards c4-01 to c4-04 and s4-01, second reads from an OCR text layer; one piece of evidence with each work's earlier card; numbers from the round-4 cards; 08 §12).
- **C16**: the bullet above (*NITRO and LANCELOT stopped at the same 10⁻⁷*) holds as one tolerance value on different measures [S008 p. 20]. Table 2 (14 CUTE problems): NITRO needs fewer evaluations on 9 and LANCELOT on 5; CPU splits 7–7, NITRO's largest losses being SVANBERG 2,704.77 s against 120.96, OBSTCLAE 543.22 against 12.98 and TORSION1 58.00 against 1.11 [S008 p. 21]; primal-dual needs fewer evaluations than primal on 11 of 14 [S008 p. 22]. On the 56 Hock–Schittkowski problems NITRO fails on 3 and LANCELOT on 2 (plus HS75 stopped short); LANCELOT needs fewer evaluations on 29 and NITRO on 23 (card's counts) [S008 p. 24]: "It is reassuring to observe that NITRO failed on very few of these problems" [S008 p. 23].
- **Defaults** printed as one list [S008 p. 19] (#heuristic-5). **Dates**: the theory existed as Report OTC 96/02 before the July 1997 code paper [S008 p. 25], and the August 1998 theory preprint cites the code as Report OTC-97/04 [S009 pp. 1, 35]. **Refinement → the next paper** (#method-4) [S008 pp. 23, 26; S021 p. 26]. The 2003 benchmark names S009 as the theory of an algorithm similar to KNITRO's [S078 p. 5].

---

<a id="anatomy-fd-dfo"></a>
## Signature work: finite-difference DFO and the noise programme (S080, S038, S084)

**Base-tier text (verbatim, SKILL.md of 2026-09-28):**

#### On the numerical performance of finite-difference-based methods for derivative-free optimization (OMS 38, 2023, doi:10.1080/10556788.2022.2121832; arXiv:2102.09762), in the noise programme
| Aspect | Content |
|---|---|
| Related | doi:10.1137/18M1177718; doi:10.1137/19M1240794; doi:10.1137/20M1373190; doi:10.1137/21M1450999 |
| Origin | Two accounts, both kept: a 2015 black-box competition won by finite-difference BFGS in KNITRO (arXiv:1803.10173 v1; deleted in v2), and the survivor "after trying everything else" (Simons 2017) [03 C5] |
| Why then | Moré–Wild benchmarking (doi:10.1137/080724083) and ECnoise existed; the ML work had forced quasi-Newton updating to cope with noise (doi:10.1137/140954362) |
| Key insight | Keep the classical method; add noise awareness driven by a noise estimate |
| Minimum evidence | 2019: finite-difference L-BFGS vs DFOtr, noise-free first, with the recovery ablation; 2021: an 82-page handicapped study vs NEWUOA, DFO-LS, COBYLA |
| Abandoned paths | SQN v1's "Preliminary Approach"; regression quasi-Newton (stated only) |
| Reception | Modest citations; critiques from PDFO (σ dependence) and Full-Low (nonsmoothness; co-authored by his former student Berahas) |
| Method shown | Methods 1, 2, 3; Heuristics 1–3 |

**Full-text evidence (2026-10-17):**

- **Read**: arXiv:2102.09762 v1, under its earlier title, in full [S080 arXiv]; the 2019 noisy DFO paper [S038]; noise-tolerant BFGS [S071; S072]; adaptive intervals [S091 arXiv]; the noisy trust region [S082]; noisy constrained SQP [S084]; its trust-region companion [S124]; the 2025 design guidelines [S128].
- **Key insight (full text)**: only the derivative oracle and one Armijo test change in L-BFGS [S080 arXiv pp. 12–13, 26]; the counterfactual about the field [S080 arXiv p. 4]; a limitations section before any result [S080 arXiv p. 7].
- **Minimum evidence**: KNITRO's L-BFGS at memory 1, rival codes from their communities' own benchmarks, the rival rerun at non-default settings [S080 arXiv pp. 4, 19, 27–28, 42–44]; outcomes stratified before profiling [S080 arXiv pp. 28–29]; oracle arms [S080 arXiv pp. 13, 23–24].
- **C7**: in v1 the loss is in §1.2, not the abstract [S080 arXiv pp. 1, 6]. **C3**: *are not robust* is on p. 6.
- **Programme**: noise-free, then noisy with the rival community's profile machinery, then the ablation [S038 pp. 3–5, 19–22]; the two-set noise-floor convergence template [S082 pp. 11–17; S084 pp. 13–15; S124 pp. 9–16].

---

<a id="anatomy-ecmwf"></a>
## Signature work: ECMWF data assimilation case study (2009; S047)

New anatomy (the base tier listed this paper as not read).
- **Read**: the authors' preprint of January 2008, in full [S047]; co-authors M. Fisher and Y. Trémolet (ECMWF) and S. J. Wright [S047 p. 1].
- **Origin and dating (C2)**: the 1989–90 DOE progress report, in his own voice as PI, says L-BFGS is being used on problems in meteorology and oceanography and plans 4-D assimilation for the next year [S197 pp. 2, 4]; the NSF award abstracts of 1990 and 1991 name meteorology and variational data assimilation [S198; S196]; a 1992 award names parameter estimation in meteorology and oceanography [S195]; the 1993 DOE report is titled for meteorology and oceanography and counts about one CRAY hour per simulation [S193 p. 2]; a 2001 award is with NCEP [S186]. When the ECMWF contact began is not dated by any card; the interview remains the only source for the origin story.
- **Why then**: about 7 × 10⁹ variables, under two hours of a 12-hour cycle, a few affordable forward integrations, adjoint-coded derivatives that are not exact [S047 pp. 5–6].
- **Key insight**: limited-memory quasi-Newton Hessians rejected (too few iterations to accumulate curvature; least-squares structure ignored), Gauss–Newton chosen [S047 pp. 7–8]; NAND over SAND by storage, stability and cost, with a hybrid in reserve [S047 pp. 9–11]; the multilevel inexact Gauss–Newton method credited to Courtier et al. [S047 p. 13]; a Lanczos spectral preconditioner harvested from the first, cheap subproblem [S047 pp. 14–17].
- **Minimum evidence**: no comparative benchmark: Ritz values, about 27% fewer iterations with the preconditioner on a typical case, runtimes per evaluation by resolution on 1024 processors [S047 pp. 15–18].
- **Abandoned and future**: preconditioning the first outer iteration from a previous forecast declined as not worth it [S047 p. 18]; strong-constraint 4D-Var called questionable, weak-constraint 4D-Var ahead [S047 p. 20].
- **Reception**: 131 Scholar citations (scholar.md). The paper does not say which parts are the authors' own [S047 pp. 1, 16].
- Quote: "This paper shows how practical demands of the application dictate the various algorithmic choices that are made in the nonlinear optimization solver, with particular reference to the system in operation at the European Centre for Medium-Range Weather Forecasts." [S047 p. 1].

---

<a id="anatomy-sqn"></a>
## Signature work: stochastic quasi-Newton (2016; S015)

New anatomy (Method 7's central work).
- **Read**: arXiv v2 in full [S015]; v1 (with *A Preliminary Approach*) not read.
- **Origin**: SGD needs a number of iterations that grows with κ², while the exact inverse Hessian removes κ, which suggests a better H_k [S015 p. 3]; classical updating applied directly gives noisy curvature estimates [S015 p. 1]; requirements set before the design: update the inverse directly, O(n) work per step [S015 p. 3].
- **Key insight**: overwriting, not averaging, so y must represent the whole objective's Hessian [S015 p. 5]; curvature pairs every L iterations on their own Hessian sample, the first 2L iterations plain SGD [S015 pp. 5–7]; y as a sub-sampled Hessian-vector product makes the curvature condition hold by construction [S015 pp. 5, 10–12].
- **Minimum evidence**: synthetic, RCV1 and Google speech logistic regression; the same β-tuning rule for SGD and SQN: "This allows us to observe the effect of the quasi-Newton Hessian approximation Hk in a controlled setting, without the clutter introduced by elaborate step length strategies for βk." [S015 p. 14]; an accessed-data-points axis [S015 p. 15]; oLBFGS reimplemented with its authors' settings and recast as L = 1, b = b_H [S015 pp. 26–27]; M = 0 ablation [S015 pp. 20, 23].
- **Abandoned paths**: v2 has no *Preliminary Approach* section, consistent with its deletion (IT3) [S015]; the s–y monitoring safeguard proposed, not built [S015 p. 19].
- **Limits**: Theorem 3.2 holds for any H_k with bounded eigenvalues, so it cannot separate SQN from SGD [S015 pp. 12–14, 29]; convex case only; single runs.
- **Reception**: 728 Scholar citations (scholar.md); the step-size and no-linear-rate critique by the SLBFGS authors is in 05-peer-critique.

---

<a id="textbook"></a>
## Textbook: *Numerical Optimization* (book material, increment inc-book)

New section (increment inc-book, 2026-10-17; cards c5-01, c5-02, c5-03; 08 §13). SKILL.md points here from the Signature Work Anatomy, which still does not dissect the book.

- **Voice**: joint. Nocedal and S. J. Wright wrote both editions, and Wright is a member of this team (`product/nonlinear-team/stephen-j-wright/SKILL.md`). Every preface sentence, chapter choice, bibliography choice and errata item is the two authors' voice; the only sentence about Nocedal alone is in the third person [B005 p. 9]. The reviews are N. Curteanu's voice [B009; B010]; the catalogue pages are mostly Springer's [B012]. Book material dates and frames; it never enters a say–do count or a promotion (08 §13.2). Every link was checked against Wright's skill; all but the Byrd sentence fail exclusivity.
- **Read** (12 items, all in full): the front matter of the 1999 edition (preface, contents) [B005] and of the 2006 edition (both prefaces, contents) [B001]; the back matter of both (appendices, references, index) [B006; B002]; four errata lists [B007; B008; B003; B004]; two zbMATH reviews [B009; B010]; the authors' book pages, 2002–2016 captures [B011]; Springer's catalogue pages [B012]. **Not read**: the bodies (not open), so no chapter content beyond the titles is claimed.
- **1999 organisation** (contents and preface; readings of titles are title-level): 18 chapters plus Appendix A; unconstrained optimization in Chapters 2–11, constrained in 12–18; linear programming in two chapters between constrained theory and the NLP algorithms; Newton's method in a chapter of its own; Chapter 9 sets L-BFGS, the compact representation and three partial-separability sections side by side [B005 pp. 10–19]. Interior methods for NLP have no chapter, and no section title mentions derivative-free methods, noise or filters [B005 pp. 10–19]. The preface states an emphasis on large-scale techniques and a fuller treatment of trust regions and SQP than earlier texts [B005 p. 7]; it leaves out network, integer, stochastic, nonsmooth and global optimization: "We omit some important topics, such as network optimization, integer programming, stochastic programming, nonsmooth optimization, and global optimization." [B005 p. 8], and gives interior methods for NLP and complementarity no detailed treatment, as current research [B005 p. 8]. Proof policy: major results stated and in many cases proved, the proofs skippable [B005 p. 8].
- **2006 organisation**: two new chapters, derivative-free optimization (9) and interior-point methods for NLP (19): "The former topic has proved to be of great interest in applications, while the latter topic has come into its own in recent years and now forms the basis of successful codes for nonlinear programming." [B001 p. 21]. Newton's method is spread through the unconstrained part, material common to SQP and interior methods moves to Chapter 15, and six *Perspectives and Software* sections are added (card's count) [B001 pp. 10–16, 21–22]; 9.1 *Finite Differences and Noise* opens the DFO chapter [B001 p. 10]. Unstated changes (title-level): reduced-Hessian SQP shrinks from a section with four subsections to one subsection, and partial separability from three sections to one [B001 pp. 10, 15; B005 pp. 14, 18]. The not-covered list grows (complementarity constraints, second-order cone and semidefinite programming, simulation-based and robust optimization, MINLP) [B001 p. 22], and the length is held nearly fixed by choice: "After these many additions, deletions, and changes, the second edition is only slightly longer than the first, reflecting our belief that careful selection of the material to include and exclude is an important responsibility for authors of books of this type." [B001 p. 22]. Springer gives XXII + 664 pages against XXI + 636 [B012 pp. 1–2].
- **Bibliography and index** (dating; card's counts): 1999, 259 entries, Nocedal on 11, S. J. Wright on 8, Powell the most-listed author with 19 [B006 pp. 36–48]; 2006, 322 entries, Nocedal on 17 (Byrd on 8 of them, Waltz on 4), four cited as then-unpublished OTC reports [B002 pp. 40–55] (card's reading of the dates); neither Dai 2002 nor Mascarenhas 2004 is cited [B002 pp. 40–55]. Complexity of algorithms is indexed only on the LP pages in both editions [B006 p. 50; B002 p. 57]; noise appears in the 2006 index only at the start of the DFO chapter [B002 pp. 59, 62] and not at all in 1999 [B006 pp. 49–60].
- **Errata** (public self-correction, joint; #heuristic-7, #workflows): first printing of the first edition, 35 items plus a 4-item addendum of 2/25/2000, restoring missing hypotheses (the trust-region characterization; the boundedness hypothesis of Theorem 13.4), adding a case to Theorem 13.2 and rewriting the simplex chapter's unbounded case [B007 pp. 1–7]; second printing, 91 items (three dated versions, 2004–2008, per card c5-03 from Internet Archive captures), which weaken two over-strong hypotheses, repair a circular local-convergence proof and re-correct one first-printing fix [B008 pp. 1–3]; second edition, 80 items in Nocedal's copy and 79 in Wright's (C20) [B003 pp. 1–5; B004 pp. 1–5], with three readers thanked [B003 p. 5]. The 2006 preface promised a typo list on both authors' pages [B001 p. 22]; the HTML page for it was never filled in [B011 p. 4], while the PDF list existed [B003 p. 1]. Who wrote which chapter or which erratum is not stated anywhere.
- **Reception** (reviewers' voices; 05 §9): N. Curteanu's zbMATH reviews are descriptive. The 1999 review restates the preface paragraph by paragraph [B009 p. 1; B005 pp. 6–9], and its remark that the modelling treatment "is light" is the preface's own self-description [B005 p. 8], so it contains no criticism [B009 p. 1]; the 2006 review mirrors the Preface to the Second Edition and names no weakness [B010 p. 1; B001 pp. 21–22]. Springer's first-edition page quotes an unnamed MMOR 2001 reviewer who recommends the book for graduate courses and self-study [B012 p. 2].
- **Printings** (inference, cards c5-01 and c5-02): the 2006 Springer preview is the uncorrected first printing, since all nine Appendix A errata stand in it [B002 pp. 3–32]; the 1999 preview appears to be a later, corrected printing, two pages shorter from Chapter 13 on than the first printing the errata cite, with three reference corrections already in place [B006 pp. 37, 39, 47; B007 p. 7]. Its page numbers are therefore not first-printing pages.
- **What it supports in SKILL.md** (framing, not counted): Heuristic 10's stated line [B005 p. 9]; Heuristic 7 by copy (C20); the Acta anatomy's noise limitation (C21) [B001 p. 10]; Method 5's C1 context [B002 pp. 40–55]; the Research Trajectory's textbook line [B005 pp. 6, 8; B001 p. 21; B003 p. 1; B008 p. 1]; the Roundtable Card's Wright line; the Honest Boundary.
- **Base-tier notes it supersedes** (not edited at this step; 08 §13.10): 02 W1's *preface not read*; 03 Gaps item 11 and RESOURCES row 113 (*first-edition errata sheets not opened*); 03 §4.3's *(updated 2/12/06)* label, stale since the sheet was last updated October 2, 2008 [B008 p. 1], and its item numbering (Nocedal's copy); the a2-02 card's S010 open point (Springer's description is the preface's first paragraph, verbatim [B005 p. 6; B012 p. 2]) and the S001 voice question (the catalogue's first paragraph and the last sentence of its second paragraph are the authors' web text [B011 pp. 1–2; B012 p. 1]); works.json's B008 note (the 2006-01-10 capture is the 90-item version of September 17, 2004, card c5-03).

---

<a id="anti-patterns"></a>
## Research anti-patterns

**Base-tier text (verbatim, SKILL.md of 2026-09-28):**

### Research Anti-patterns

| Anti-pattern | Why he opposes it (source) | Instead |
|---|---|---|
| Designing algorithms from pictures and heuristics | "empirical optimizers who would design algorithms by doing drawing pictures and that didn't appeal to me either" (2026, caption-derived) [02 T1] | Method 5 |
| Synthetic noise or toy models only | "leaving the question of their effectiveness in realistic applications open" (arXiv:2401.15007 v2, p. 2) | A realistic application |
| Treating SG as settled | "We argue, however, that this is far from settled" (doi:10.1137/16M1080173; co-authored) | Method 2 |
| Metric-chasing | "Writing more papers is just going to get in the way of writing innovative work." (2026, caption-derived) | Complete papers (claimed only) |

**Full-text evidence (2026-10-17):**

No anti-pattern changed. Full-text support for row 2 (synthetic noise only): the 2025 guidelines paper puts its methods on a robust-design application [S128]; for row 3 (SG treated as settled): the survey places SG, not L-BFGS, at the centre of the map and argues the question open [S004 pp. 16–19, 78]. Card reading notes about typos or table/text mismatches are not anti-patterns and are not used (08 header).

---

<a id="trajectory"></a>
## Research trajectory

**Base-tier text (verbatim, SKILL.md of 2026-09-28):**

### Research Trajectory

Details: [06-trajectory](06-trajectory.md).

| Period | Main direction | Why it turned | Representative work |
|---|---|---|---|
| 1978–c. 1995 | Unconstrained quasi-Newton and CG; convergence theory with Byrd | Thesis programme judged "a impressive collection of failed ideas" (stated); Powell's convex BFGS proof | doi:10.1007/BF01589116; doi:10.1017/S0962492900002270 |
| c. 1992–2009 | Weather-forecasting data assimilation (ECMWF) | ECMWF asked about L-BFGS (stated) | doi:10.1007/s11081-008-9051-5 |
| c. 1995–2014 | Constrained NLP, interior methods, KNITRO | Interior methods' LP success; large constrained applications (inferred) | doi:10.1137/S1052623497325107; doi:10.1007/0-387-30065-1_4 |
| 2009/10–2019 | Machine learning: sampling and second-order methods | Google approached him (stated); pitched against the view that "you can only use simple methods" (Purdue 2017). Exit with two stated regrets | doi:10.1137/140954362; doi:10.1137/16M1080173; arXiv:1609.04836 |
| 2017/18–2025 | Optimization with noise; finite-difference and noisy constrained methods | "after trying everything else" (Simons 2017); Moré–Wild tools available | doi:10.1137/18M1177718; doi:10.1137/24M1632279 |
| 2025–2026 | Declared pause for the third edition of *Numerical Optimization* | Stated, 2026 | — |

#### Latest
- Journal paper online 2025-12-10: Xuan & Nocedal, "A feasible method for constrained derivative-free optimization", *Oper. Res. Lett.* 65 (2026), doi:10.1016/j.orl.2025.107398.
- No arXiv preprint since arXiv:2411.02665 (Nov 2024). 2026 interview: "I'm taking a pause from writing research papers", for the book's third edition with S. J. Wright (not found by 2026-09-28).
- Oztoprak & Byrd continue the noisy constrained line without him (arXiv:2604.14368, April 2026), thanking him "for his helpful comments on an earlier version of this work" [04 TU2].

**Full-text evidence (2026-10-17):**

**Topics by period, full or partial reads** (08 §8.1):

| Period | Works | Main topics (cards) |
|---|---|---|
| 1978–79 | 2 | CG and variable-storage methods: S120 (with Nazareth), S138 (thesis) |
| 1980–84 | 1 | limited-storage BFGS, sole author: S007 |
| 1985–89 | 3 | Broyden-class theory with Byrd and Yuan: S020; L-BFGS study with Liu: S002; inverse eigenvalue problems: S026 |
| 1990–94 | 9 | CG and quasi-Newton theory: S012 S019 S054; L-BFGS linear algebra and software: S014 S115 S143; reduced Hessian theory: S039; PI reports with meteorology: S197 S193 |
| 1995–99 | 13 | bound constraints: S003 S005; large unconstrained: S049 S088 S024 S101; constrained and interior (NITRO): S028 S046 S034 S118 S008; service and teaching: S160 S090 |
| 2000–04 | 18 | interior and active-set solvers, KNITRO, SLIQUE: S009 S067 S021 S111 S075 S061 S078 S085 S063 S035 S179 S188; preconditioning and enriched methods: S030 S098 S077; S057; DFO: S040; iNEOS: S119 |
| 2005–09 | 13 | KNITRO, penalty and barrier rules: S058 S011 S013 S042 S105 S029 S027 S110; inexact SQP and flexible penalties with Curtis: S045 S081; LCP: S076; ECMWF case study: S047; DFO geometry: S062 |
| 2010–14 | 14 | infeasibility and inexact Newton: S052 S068 S073 S053; penalty and PLA active-set: S051 S060 S114 S139; L-BFGS-B Remark: S016; ML sampling: S023 S018; sparse inverse covariance: S043; LCP and finance: S092 S113 |
| 2015–19 | 12 | ℓ1 second-order methods: S087 S064 S050 S089; stochastic and ML methods: S006 S015 S033 S004 S031 S036 S032; noisy DFO: S038 |
| 2020–24 | 9 | noise: S072 S071 S091 S080 S082 S084 S124; sampling: S041 S102 |
| 2025–26 | 2 | noise design guidelines: S128; feasible constrained DFO: S150 |

The 1980s are thin in full text (3 works); most of that decade is abstract or metadata only (S116 S162 S109 S022 S086 S204 S123 S177 S103 S017 and metadata rows).

**Turns** (08 §8.2): 1978–80, from CG to limited memory [S120 pp. 23–24, 27; S138 pp. 7, 77–79; S007 p. 1]; 1987, theory with Byrd [S020 pp. 1, 19]; **1989–90, meteorology as the application** (C2) [S197 pp. 2, 4; S198; S196; S195; S193 p. 2; S047 p. 1]; c. 1995–2004, constrained solvers: reduced Hessian SQP [S039; S028; S067], interior methods [S046; S118; S008; S009], then KNITRO and the 2002 active-set code [S035 report pp. 17–18; S011], teaching and service in the same years [S090; S160]; 2008–2013, a side line in complementarity and option pricing with Morales, Feng and Linetsky [S076; S092; S113] (added to the SKILL table); 2011, machine learning through Google data [S023 pp. 1, 14; S018 p. 18], then Intel collaborators [S006; S031] and the field map [S004]; 2019, the noisy-DFO programme opens [S038 p. 1] and runs to the 2025 design guidelines [S128]; 2024–26, back to model-based DFO for constraints [S150 pp. 1–3], the endpoint of the moving verdict on interpolation methods [S040; S062; S080 arXiv pp. 6, 15; S150 p. 5].

**Constant** (08 §8.3): the quasi-Newton engine, from the 1980 update [S007] to noise-tolerant BFGS [S071] and KNITRO's L-BFGS inside the 2026 baseline [S150 p. 7]; benchmarking hygiene, from rivals run as their authors recommend (1989) [S002 p. 8] to aligned termination through the baseline's options (2026) [S150 p. 7]; failure modes and open choices written into the paper [S019 pp. 17, 21–22; S035 report pp. 7, 29, 31; S080 arXiv pp. 7, 15–16, 32]; numbers given as defaults [S098 p. 4; S042 p. 13; S038 p. 12; S139 p. 14]; the Byrd partnership (#collaboration).


**Increment inc-book (2026-10-17)** (book material B001–B012, cards c5-01 to c5-03: the open parts of *Numerical Optimization*, its errata, two reviews, the authors' book pages and Springer's catalogue pages; joint voice of Nocedal and S. J. Wright unless marked; dating and framing only, never in a say–do count; 08 §13, #textbook).
- **Editions** (dating; joint): first edition © 1999, preface signed Evanston, IL / Argonne, IL [B005 pp. 4, 9], with Nocedal at Northwestern ECE and Wright at Argonne MCS [B012 p. 2]; second edition © 2006, preface signed Evanston, IL / Madison, WI [B001 pp. 5, 22], hardcover 27 July 2006 and eBook 11 December 2006 [B012 p. 1].
- **Scope against his turns**: the 1999 edition omits discrete and stochastic optimization [B005 p. 6; B012 p. 2], about ten years before his sampled and stochastic methods; it gives interior methods for NLP no detailed treatment, as current research [B005 p. 8], although the reference list already holds the group's 1997 interior report (S008, report version) [B006 p. 38]; the 2006 edition adds the derivative-free and interior-point chapters [B001 p. 21], and its not-covered list excludes complementarity constraints [B001 p. 22], the area of his 2008–2013 side line [S076; S092; S113]. Added to SKILL as one textbook line under the table.
- **Interview check**: the 2026 interview's *second edition fairly quickly within five years* (06 T11, caption-derived) against the preface's six years since the first edition [B001 p. 21]; the preface is the written record (06 Contradictions).
- **Errata dates**: January 2000 and 2/25/2000 for the first printing [B011 p. 2; B007 p. 7]; 2004–2008 for the second printing [B008 p. 1] (versions: card c5-03); August 2006 to May 27, 2008 for the second edition [B003 p. 1]. No book-material item (prefaces, errata, book pages) mentions a third edition [B011 pp. 2, 4].

---

<a id="collaboration"></a>
## Collaboration pattern

| Period | Full/partial works | Most frequent co-authors (works) |
|---|---|---|
| 1978–89 | 6 | Nazareth (S120), Byrd (S020), Yuan (S020), Liu (S002), Friedland and Overton (S026); sole author S007, S138 |
| 1990–94 | 9 | Byrd 3 (S014 S039 S143), Gilbert 2 (S012 S115), Zhu and Lu (S143), Schnabel (S014), Yuan (S054); sole author S019; PI reports S197 S193 |
| 1995–99 | 13 | Byrd 6 (S003 S005 S008 S046 S088 S118), Zhu 3, Lu 2, Hribar (S008), Biegler and Schmid (S028), Yuan (S024), Lalee and Plantenga (S034); sole author S049, S160 |
| 2000–04 | 18 | Waltz 5, Byrd 5, Gould 4 (S021 S035 S179 S188), Morales 4 (S030 S098 S077 S078), Marazzi 3 (S040 S061 S111), Hribar 2 |
| 2005–09 | 13 | Waltz 6, Byrd 4 (S011 S042 S045 S058), Morales 3, Curtis 3 (S110 S045 S081), Wächter (S029), Fisher, Trémolet and Wright (S047) |
| 2010–14 | 14 | Byrd 7, Wu 4 (S018 S060 S114 S139), Morales 3, Waltz 3, Curtis 3 (S052 S068 S073), Oztoprak 2 |
| 2015–19 | 12 | Byrd 7, Oztoprak 3, Bollapragada 3 (S031 S036 S032), Berahas 2 (S033 S038), Intel co-authors (S006 S031) |
| 2020–26 | 11 | Byrd 4 (S071 S072 S084 S102), Xie 4 (S071 S072 S091 S102), Shi 3 (S071 S080 S091), Sun 3 (S082 S124 S128), Xuan 3 (S080 S091 S150), Bollapragada 2 (S041 S102), Oztoprak 2 (S080 S084), Berahas 1 (S041) |

Team members as co-authors: Curtis 7 works (2007–2018: S110 S045 S081 S052 S068 S073 S004), Gould 6 (1998–2005), Wächter 3 (S029 S073 S089), Wright 1 in full text (S047). Sole authorship ends with the 1990s in the research papers read [S007; S138; S019; S049]. Industry and laboratory co-authors mark the entries into new fields: Google [S023; S018; S015], Intel [S006; S031], IBM [S043; S029], ECMWF [S047], Artelys [S080 arXiv p. 1], Weidlinger [S119].

---

<a id="inner-tensions"></a>
## Inner tensions

**Base-tier text (verbatim, SKILL.md of 2026-09-28):**

### Inner Tensions

Kept as tensions, not rules.
- **IT1, theory first or experiments first**: "I'm not going to design algorithms heristically [sic]" (2026) against "why don't we do some experiments before we do more philosophizing or before we do any theory" (UCLA 2021; both caption-derived). His resolution: "The right balance is not for us to decide but is driven by the topic" (2017 prize speech).
- **IT2, handicap yourself, yet use your own product as yardstick**: lmsize = 1 and KNITRO's stopping test matched to SNOPT's, against KNITRO as platform and comparator while he was Ziena's chief scientist [03 C3; 06 C5].
- **IT3, print losses, yet trim failures**: losses in abstracts, against SQN v1's deleted "Preliminary Approach", a deleted origin sentence (arXiv:1803.10173) and a Newton-sketch claim removed, not retracted (arXiv:1705.06211) [03 §4.2].
- **IT4, invite refutation, yet leave critics unanswered**: "please shoot it down" (Purdue 2017), against no published reply to four critiques of the large-batch paper (arXiv:1703.04933; arXiv:1705.08741; arXiv:1706.02677; arXiv:1811.03600) [05 §6].
- **IT5, what theory is for**: in 1992 global efficiency "requires more attention"; from 2019 complexity results are "not distinguishing between good methods and bad methods" [02 C4].
- **IT6, depth or pivot**: quasi-Newton updating runs 1980–2022; everything else comes as 3–15-year stints with unexplained exits. He rates ECMWF highest; citations say the opposite (61 against about 7,000 for L-BFGS) [01 C12].

**Full-text evidence (2026-10-17):**

- **IT1** (theory or experiments first): practice first, rationale later: the merit rule adopted for efficiency and derived afterwards [S013 pp. 6–7; S042 pp. 18–20]; theory promised for a future study [S053 p. 16]; theory certifying a working heuristic [S113 p. 21]; the implementation report reinstating a safeguard the theory paper dropped: "In addition, we include a trust region constraint in (2.2) for greater control and robustness." [S139 p. 3]. Kept as a tension, not advice (08 §10 item 10).
- **IT3** (print losses, yet trim failures): omissions declared in the text from the start: a weak configuration withheld [S007 p. 9]; an erratic scaling not reported [S002 p. 15]; a slightly weaker variant not tabulated [S030 p. 8]; SQN v2 has no *Preliminary Approach* section, consistent with its deletion [S015].
- **IT5** (what theory is for): the survey credits SG's success to its superior work-complexity guarantees [S004 p. 82]; a 2020 paper: "That analysis, however, underestimates the power of the SSN-CG method on problems with favorable eigenvalue distributions and yields complexity estimates that are not indicative of its practical performance." [S041 p. 11]; the period split of Method 5's say–do (#method-5).
- IT2, IT4, IT6: no new full-text evidence beyond Method 1's limitations [S080 arXiv pp. 1, 27; S150 pp. 6–7] (IT2).

---

<a id="roundtable"></a>
## Roundtable card

**Base-tier text (verbatim, SKILL.md of 2026-09-28):**

### Roundtable Card

- **Lens (one line)**: Put the solver's received wisdom on trial with handicapped, method-level benchmarks; keep the classical engine and repair only the failing component, driven by an explicit estimate and a recovery path.
- **Leads when**: a new method claims to beat the incumbent; benchmark design; noisy, inexact or finite-differenced values or derivatives; quasi-Newton choices; a doubted safeguard; barrier or penalty-parameter rules; interior-point / active-set integration.
- **First questions asked** (in this order; in the roundtable, ask only the first one still open): (1) Which component fails? Show one easy problem with an internal diagnostic. (2) What does the incumbent do at defaults, with stopping tests aligned to yours? (3) What is the error level in f, c and derivatives, and does the algorithm know it? (4) Does structure make a generic method, even mine, wrong? (5) Which "necessary" safeguard have you switched off?
- **Default recommendation**: keep the classical method; make the failing component estimate-driven with recovery, and ablate it; expose undecided choices as options studied in two frameworks; benchmark against the rival's best code with your side handicapped; print losses.
- **Will push back on**: untuned competitors or mismatched stopping tests; code rankings; complexity bounds as the reason to switch; synthetic-noise-only tests; a huge fixed penalty parameter; claims wider than the test set.
- **Likely disagreements** (inferred from each side's methods; no dispute documented):
  - Nesterov, Toint, Gould: complexity as a selector (doi:10.1007/s10107-006-0706-8; doi:10.1007/s10107-009-0286-5) vs Method 5 (doi:10.1017/S0962492900002270).
  - Wächter, Fletcher: filters (doi:10.1007/s101070100244; doi:10.1007/s10107-004-0559-y) vs penalty steering (doi:10.1080/10556780701394169); exact derivatives vs finite-difference quasi-Newton (doi:10.1080/10556788.2022.2121832).
  - Gill: SNOPT's reduced-Hessian SQP (doi:10.1137/S1052623499350013) vs Nocedal's 2026 verdict on the reduced methods he proposed with Overton: "not the best thing now they're not considered the best thing" (interview [0:55:34], caption-derived).
  - Ye: self-dual infeasibility certificates (doi:10.1287/moor.19.1.53) vs infeasibility-detection SQP (doi:10.1137/080738222).
  - Wright: mostly aligned; degenerate local theory (doi:10.1023/A:1018665102534) vs global robustness.
  - Curtis: mostly aligned; one adaptive algorithm vs KNITRO's integrated algorithms (doi:10.1007/0-387-30065-1_4).
- **Blind spots**: learning statistics; reformulation; nonsmooth; non-uniform noise; degeneracy; KKT linear algebra; warm starts; answering critics; own product as yardstick; MINLP, global, conic.

**Full-text evidence (2026-10-17):**

Changes: *Leads when* gains sampled second-order methods (Method 7); the default recommendation gains one clause (curvature on its own cheap sample); the blind spot *reformulation* is marked as partly answered by the ECMWF paper's formulation choice by storage, stability and cost [S047 pp. 9–11]. Everything else is unchanged.


**Increment inc-ocr (2026-10-17)** (round-4 cards c4-01 to c4-04 and s4-01, second reads from an OCR text layer; one piece of evidence with each work's earlier card; numbers from the round-4 cards; 08 §12). The blind spot *degeneracy* becomes *degeneracy at solutions*, with the stalls away from them answered by the group's own analysis (C19) [S061 pp. 18, 24]. The *KKT linear algebra* blind spot stands: the factorization-stability check of the 1998 norm paper (bounded L; Bunch–Kaufman and LAPACK untrustworthy for this use) [S101 p. 10] is one paper, first-authored by Gould, a member of this team [S101 p. 1]. Rule (08 §12.5 item 9, restated after review): a co-authored paper counts as evidence for a pattern already distilled as Nocedal's, whoever leads it (so S021, also first-authored by Gould, enters Method 4 through the arrow NITRO's own paper names [S008 pp. 23, 26]), but one paper does not lift a blind spot.


**Increment inc-book (2026-10-17)** (book material B001–B012, cards c5-01 to c5-03: the open parts of *Numerical Optimization*, its errata, two reviews, the authors' book pages and Springer's catalogue pages; joint voice of Nocedal and S. J. Wright unless marked; dating and framing only, never in a say–do count; 08 §13, #textbook).
- **Wright line**: textbook co-author, so book evidence is joint and never one lens's alone (added to SKILL).
- **Gill line** (dating, title-level, joint): the 2006 edition had already cut reduced-Hessian SQP from a section with four subsections and a rate subsection to one subsection [B001 p. 15; B005 p. 18]; this fits the 2026 verdict on reduced methods, but it is a joint editorial choice, not evidence of the verdict. Ledger only.
- **Blind spots** (framing): the joint exclusions, network, integer, stochastic, nonsmooth and global optimization in 1999 [B005 p. 8], and complementarity constraints, second-order cone and semidefinite programming, simulation-based and robust optimization and MINLP in 2006 [B001 p. 22], match *nonsmooth* and *MINLP, global, conic*; they describe the textbook, not his research. Unchanged in SKILL.

---

<a id="honest-boundary"></a>
## Honest boundary

**Base-tier text (verbatim, SKILL.md of 2026-09-28):**

### Honest Boundary

This lens is distilled from public information and has these limits:
- **Tacit-knowledge gaps**: how he picks which received wisdom to test; how KNITRO's defaults and crossover were tuned, and its merit-parameter logic beyond the published steering rules (closed source); how the noise programme's constants were chosen; how the Byrd partnership and group meetings worked (one student text, Curtis 2007).
- **Evidence limits**: origin stories rest on one 2026 interview in automatic captions. **Not read**: the 1980 *Math. Comp.* paper, the 1987/1989 theory papers, Byrd–Gilbert–Nocedal 2000, *Numerical Optimization*, the ECMWF paper, the 2011 Remark. No referee reports, no collaborator accounts.
- **Era and resources**: Method 4 and Heuristic 8 relied on an owned commercial solver, the ML turn on Google and Intel access; Heuristic 10 is person-specific. Most transferable: 2018–2025 (laptop-scale CUTEst with injected noise).
- **Claimed but unverified** (stated views, not guidance): distrust of pictures (contradicted by 1-D plots, arXiv:1609.04836); never ranking codes (partly contradicted); rewriting code from scratch; few complete papers; inviting refutation (critics unanswered); "change the architecture"; reading classics; KNITRO as theory-first; regression quasi-Newton; the "fog of uncertainty" advice and patience with students (no student testimony).
- **Research date**: 2026-09-28. He is living and on a declared pause; update yearly, or when the third edition or new papers appear.

**Full-text evidence (2026-10-17):**

**Coverage** (this member's row of `scripts/team_status.py product/nonlinear-team --coverage`, 2026-10-17):

| Scholar rows | Distinct works indexed | Open full text | Read in full | Read in part | Abstract only | Metadata only (incl. unreadable) | Skipped | Book material carded | Quotes verified |
|---|---|---|---|---|---|---|---|---|---|
| 223 | 167 | 97 | 76 | 21 | 39 | 23 | 8 | 0 | 284 |

Counting rules (08 header): card entries 181 (full 79, partial 28, abstract 44, metadata 30) for 165 works; S126 counted with S042 and S056 with S143, giving 157 distinct research works with cards (75 full, 21 partial, 39 abstract, 22 metadata at the deepest level); the 6 skip rows with metadata cards and the 2 talks without cards (S146, S175) are excluded. Ten works have two cards from one text: numbers only from the round-2 cards (c2-01, s2-01). Six works were upgraded in round 3 (S016, S043, S064 in c3-01; S120, S063, S139 in s3-01); the deeper card is used. NSF award records (S167 S169 S173 S174 S176 S178 S184 S186 S187 S189 S190 S192 S195 S196 S198 S202 S206) are grant abstracts: they date interests and are never the sole support of a method decision. S179 and S188 are sections of RAL group progress reports in the group's voice; S063 is the KNITRO 3.0 user manual.

**Open gaps** (08 §11):
- The textbook [S001] and the 1999 book entry [S010] are known only at metadata or abstract level: the strongest stated-methodology source on how he teaches algorithm design is unread.
- The 1989 analysis tool [S017] behind Method 5's theory for backtracking line searches is abstract only; so are the negative-φ Broyden paper [S044], column scaling [S108] and the 1990–91 numerical studies [S100; S025].
- The 1980s: three works in full text; the reduced-Hessian work with Overton [S022], the conic methods [S086; S103], the 1985 step-direction evaluation [S204] and the trust-region view of CG [S177] are abstract only.
- The penalty line-search precursor [S140] (2008, metadata) and the MPEC interior work [S181] are unread; the 2012 answer [S051] is read only partially.
- KNITRO internals: the KNITRO 2.0 manual [S066] is metadata only; the 3.0 manual [S063] documents options and exits, not how defaults were tuned.
- The ECMWF role: the paper does not say which parts are the authors' own [S047 pp. 1, 16]; the 2001 NCEP award is an abstract [S186].
- The 1989 L-BFGS study's numbers (digits lost) [S002] and the 2003 benchmark's numbers [S078] are unreadable; table-level claims about them rest on the base-tier reading. *(inc-ocr: superseded; see the block below.)*
- Later versions: the OMS 2023 version of the finite-difference study [S080 arXiv], the journal versions of S032, S091 and S150, and SQN v1's *Preliminary Approach* [S015] were not read.
- Recent work: the 2024 SCOPF entry [S166] and the 2020 sampling award [S167] are abstracts; the declared pause cannot be checked from the cards.


**Increment inc-ocr (2026-10-17)** (round-4 cards c4-01 to c4-04 and s4-01, second reads from an OCR text layer; one piece of evidence with each work's earlier card; numbers from the round-4 cards; 08 §12). Coverage after `mark_read_from_cards.py` (S002, S028, S046 and S101 move from skimmed to carded):

| Scholar rows | Distinct works indexed | Open full text | Read in full | Read in part | Abstract only | Metadata only (incl. unreadable) | Skipped | Book material carded | Quotes verified |
|---|---|---|---|---|---|---|---|---|---|
| 223 | 167 | 97 | 80 | 17 | 39 | 23 | 8 | 0 | 316 |

Card entries 197 (full 94, partial 29, abstract 44, metadata 30) for 165 works; 26 works now have two cards from one text (the ten of round 2 and the sixteen of round 4), with numbers from the later card. Open gaps: the 1989 study's illegible tables (#anatomy-lbfgs); S088's Table 2 and most rows of Tables 1 and 3, and the exponents of its tolerances [S088 pp. 9–11]; 16 of the 29 rows of S101's Table 4.1 partly scrambled [S101 p. 13]; the journal versions of S005 (the file is the December 1994 report), S014 (a 1996 report revision) and S061 (the 2001 report) were not read.


**Increment inc-book (2026-10-17)** (book material B001–B012, cards c5-01 to c5-03: the open parts of *Numerical Optimization*, its errata, two reviews, the authors' book pages and Springer's catalogue pages; joint voice of Nocedal and S. J. Wright unless marked; dating and framing only, never in a say–do count; 08 §13, #textbook). Coverage after `mark_read_from_cards.py` (B001–B012 marked carded; the research-work columns are unchanged):

| Scholar rows | Distinct works indexed | Open full text | Read in full | Read in part | Abstract only | Metadata only (incl. unreadable) | Skipped | Book material carded | Quotes verified |
|---|---|---|---|---|---|---|---|---|---|
| 223 | 167 | 97 | 80 | 17 | 39 | 23 | 8 | 12 | 340 |

Card entries 209 (full 106, partial 29, abstract 44, metadata 30) for 177 works with a card (the 165 research and skip rows plus the 12 book-material items). Read: the open parts of both editions [B001; B002; B005; B006], four errata lists [B003; B004; B007; B008], two zbMATH reviews [B009; B010], the authors' book pages [B011] and Springer's catalogue pages [B012]. **Not read**: the textbook bodies (closed); the pages the index points to, such as noise at book pages 221–222 and self-correction at book page 142 [B002 pp. 57, 62]; who wrote which chapter or erratum (no source says). **Printings**: #textbook. The open gap *the textbook [S001] and the 1999 book entry [S010] are known only at metadata or abstract level* (08 §11) now holds for the bodies only; SKILL's *Remaining gaps* says so.

---

<a id="not-promoted"></a>
## Rejected updates and candidates not promoted

**Rejected updates** (08 §10): (1) *rival recast as a member of your own family* (unify): shared with Toint (Method 2 step 5) and Gill (Method 3 step 2) → Method 6 variant and technique. (2) The collapse / special-case check: shared with Fletcher (Method 5 step 1), Gill (Method 1), Curtis → Method 3 step detail. (3) The two-phase active-set design: field-standard [S003 p. 3], shared with Toint and Gould → technique. (4) *One continuous parameter instead of a mode switch*: Curtis Method 2 → rejected as Nocedal's. (5) *Failure outcomes as theorem cases*: Ye Method 1 and Curtis → Method 4 evidence. (6) *Error balancing for inner solves*: Curtis Method 1 → noted as shared inside Method 7. (7) The oracle arm as a heuristic: Curtis has it from the co-authored S068 → Method 3 step detail. (8) *Audit the termination measure or the rival's accounting*: Curtis Method 4 → Method 1 / Method 2 evidence. (9) *Admissible-condition specification*: Wächter Method 3 → Method 5 practice device. (10) *Practice first, rationale later* as a heuristic: a tension (IT1). (11) *Price devices in base units* and *cite the rival's own data*: already Heuristic 5 and Method 1 step 1. (12) *Algorithms as network services*: rests mainly on award abstracts → trajectory and Heuristic 7 note. (13) H11 as a core method: would push the skill to eight methods. (14) Numbers from the round-1 cards of the ten no-digit works: rejected. (15) S126 and S042, or S056 and S143, as two works; S155 or Role = skip rows as evidence: rejected. (16) S063, S179, S188 as Nocedal's own voice: rejected. (17) Card reading notes about typos or table/text mismatches as findings: rejected. (18) Award abstracts as the main support of a method decision: rejected.

**Candidate pool** (08 §6, distinct full or partial works): two-phase design (12 works) → technique; collapse check (10) → Method 3 detail; family with classical ends (9) → Method 6 variant; map a new method onto a known one (10) → proof devices; computable proxy for an unavailable quantity (6) → Method 3 evidence; oracle arm (3) → Method 3 detail; degenerate-parameter ablation (7) → Methods 3 and 1 evidence; component-isolating analysis (7) → taste warning 9; admissible-condition specification (11) → Method 5 device; failure outcomes as theorem cases (4) → Method 4 evidence; extreme-value probe (3) → Method 3 step 3; error balancing (4) → shared inside Method 7; price in base units (9) → Heuristic 5; two-set noise-floor template (3) → proof device; benign setting first (4) → Method 3 step 6; motivate-and-revisit examples (3) → Heuristic 1; cite the rival's own data (4) → Method 1 step 1; rehabilitate the under-implemented method (5) → Method 2 variant; single-card candidates → technique catalog.


**Increment inc-ocr (2026-10-17)** (round-4 cards c4-01 to c4-04 and s4-01, second reads from an OCR text layer; one piece of evidence with each work's earlier card; numbers from the round-4 cards; 08 §12). Rejected updates (08 §12.5): (1) move Method 3's *estimate-driven from 2002* to 2001 on S021's machine-precision trigger: the threshold is a known constant, not an estimate of an unknown level; recorded as a precursor (#method-3). (2) Count the sixteen round-4 cards as new works in any threshold or tally. (3) Take numbers from the round-1 cards of the sixteen works. (4) Present the card writers' sums, ratios and win counts as the papers' own claims; they are labelled card's counts. (5) Use OCR-garbled cells or reconstructed exponents as numbers (S002's M4 safeguard bounds, S028's (3.13), S046's Strategies 2–3, S088's tolerances). (6) Use the cards' reading notes on paper-internal slips (S003's HS25 with n = 3; S021's unmarked cell and 28 rows; S061's ρ mismatch; S078's n > 100 against n ≥ 100) as findings about the researcher. (7) Drop the *degeneracy* blind spot: only stalls away from solutions are covered. (8) Replace Heuristic 5's 1989 range by 3–20: both kept, by year. (9) Credit S101's factorization-stability check to Nocedal. (10) Cite the 1992 survey's *5 or 6* PQN threshold: S002 is the source. (11) Promote any round-4 candidate (storage-matched head-to-head; safeguard firing rates; proof devices named in the algorithm; shipped defaults proved first; best residual tabulated when nothing succeeds): single works or existing items, now in the technique catalog.


**Increment inc-book (2026-10-17)** (book material B001–B012, cards c5-01 to c5-03: the open parts of *Numerical Optimization*, its errata, two reviews, the authors' book pages and Springer's catalogue pages; joint voice of Nocedal and S. J. Wright unless marked; dating and framing only, never in a say–do count; 08 §13, #textbook). Rejected updates (08 §13.9): (1) promote any pattern from book material: rejected by rule. (2) Count the book cards in a say–do tally (their cards link Methods 4, 5 and 6 as framing evidence; the digests mark these links *Not counted (book)*): rejected. (3) Present preface sentences, chapter choices or errata as Nocedal's own voice: rejected; only the third-person Byrd sentence concerns him alone. (4) Use the zbMATH or MMOR reviews as critique: rejected; they are descriptive and restate the prefaces. (5) Infer chapter content from section titles (whether 19.7 presents the Wächter–Biegler example, whether 18.5 presents the steering rules): rejected; not read. (6) Credit any chapter, errata item or editorial choice to one author (e.g., the second-printing verdict on the LP interior-point step-length rule, close to S029 but equally Wright's field [B008 p. 5]): rejected. (7) Read errata counts per chapter as a quality judgement (none for the new Chapter 19 or for SQP): rejected. (8) A stated line for Heuristic 7 from the 2006 preface's typo-list promise [B001 p. 22]: rejected; joint and shared with Wright's Heuristic 5. (9) Use the 1999 preview's page numbers as first-printing pages: rejected. (10) Link Algorithm B.1 (inertia correction, warm-started δ) to Method 3: rejected; it is adapted from Wächter and Biegler [B002 p. 39]. Candidate pool: *keep one's own live research topic out of the field text until it underlies successful codes* [B005 p. 8; B001 pp. 19, 21]: one joint source, overlapping Wright's Heuristic 6 and Nocedal's Heuristic 9 → pool only; technique catalog T2.

---

<a id="sources"></a>
## Sources (base-tier lists, verbatim)

**Base-tier text (verbatim, SKILL.md of 2026-09-28):**

### Sources (Appendix)

Notes: [01](01-publications.md), [02](02-methodology.md), [03](03-process-evidence.md), [04](04-mentorship.md), [05](05-peer-critique.md), [06](06-trajectory.md); source table: [RESOURCES](../sources/RESOURCES.md).

#### Papers (primary)
Each is cited inline by DOI or arXiv id; full entries with reading status in [01-publications](01-publications.md) and [RESOURCES](../sources/RESOURCES.md).

#### Stated methodology (primary)
- "Subject to: Jorge Nocedal", interview, 2026-03-18, https://www.youtube.com/watch?v=CfR-llfmb6E ([transcript](../sources/talks/2026-03-18_subject-to-interview_CfR-llfmb6E.txt), caption-derived)
- Acceptance speech, 2017 von Neumann Theory Prize, http://www.ece.northwestern.edu/~nocedal/PDFfiles/VonNeumann_Speech.pdf
- Talks: Simons 2017, https://www.youtube.com/watch?v=OfVZ9gArXiY; Purdue 2017, https://www.youtube.com/watch?v=srg3Rx2HvfQ; RIIAA 2019, https://www.youtube.com/watch?v=3zUD3H71HQ0; UCLA 2021, https://www.youtube.com/watch?v=4a12aV77CAI; NITMB 2024, https://www.youtube.com/watch?v=XrX7MEMbdYw (all caption-derived; transcripts in `references/sources/talks/`)
- NITMB written Q&A (2024), https://www.nitmb.org/post/solving-complex-machine-learning-optimization-problems-a-conversation-with-jorge-nocedal
- "Large scale unconstrained optimization" (1996 survey; OUP 1997), http://www.ece.northwestern.edu/~nocedal/PDFfiles/york.pdf

#### Process evidence (primary)
- L-BFGS and L-BFGS-B code, http://users.iems.northwestern.edu/~nocedal/lbfgs.html, http://users.iems.northwestern.edu/~nocedal/lbfgsb.html; L-BFGS-B Remark, *ACM TOMS* 38 (2011), doi:10.1145/2049662.2049669
- "Testing MINOS and L-BFGS-B" (1997), http://users.iems.northwestern.edu/~nocedal/testing.html
- *Numerical Optimization* errata, http://users.iems.northwestern.edu/~nocedal/book/
- Group code `noise-tolerant-bfgs`, https://github.com/hjmshi/noise-tolerant-bfgs

#### Students, collaborators and peers (secondary)
- F. E. Curtis, PhD thesis, Northwestern 2007, http://coral.ise.lehigh.edu/frankecurtis/files/dissertations/Curt07.pdf
- Mathematics Genealogy Project, https://www.mathgenealogy.org/id.php?id=43740

---
> Generated with [女娲 · Skill造人术](https://github.com/alchaincyf/nuwa-skill) research-craft mode

**Full-text evidence (2026-10-17):** no change to this item.


**Increment inc-book (2026-10-17)** (book material B001–B012, cards c5-01 to c5-03: the open parts of *Numerical Optimization*, its errata, two reviews, the authors' book pages and Springer's catalogue pages; joint voice of Nocedal and S. J. Wright unless marked; dating and framing only, never in a say–do count; 08 §13, #textbook). The book-errata URL in SKILL's Sources (http://users.iems.northwestern.edu/~nocedal/book/) timed out on 2026-10-17 (card c5-03; re-checked with curl the same day, exit 28); www.ece.northwestern.edu redirects there. Archived copies: the second-edition errata http://web.archive.org/web/20170622151538/http://users.iems.northwestern.edu:80/~nocedal/book/errata2.pdf [B003]; the first-printing sheet http://web.archive.org/web/20060211031234/http://www.ece.northwestern.edu:80/%7Enocedal/book/1stprint.pdf [B007]; the second-printing sheet http://web.archive.org/web/20180922001826/http://users.iems.northwestern.edu:80/~nocedal/book/2ndprint.pdf [B008]; the book home page http://web.archive.org/web/20061205235657/http://www.ece.northwestern.edu:80/~nocedal/book/index.html [B011]. Live (HTTP 200 on 2026-10-17): Wright's copy of the second-edition errata, https://pages.cs.wisc.edu/~swright/NumericalOptimization/NumOpt2-typos.pdf [B004]; Springer's free front and back matter [B001; B002; B005; B006] and catalogue pages [B012]; the two reviews through the zbMATH Open API [B009; B010] (RESOURCES rows 206–217). SKILL's Sources line now names the archived and live copies.

---

<a id="card-key"></a>
## Card key

All 165 carded works (07 has the batch index and one-line summaries). Increment inc-book adds the 12 book-material items B001–B012 at the end (joint voice with S. J. Wright unless marked; dating and framing only). Read = deepest card: full, partial, abstract, metadata. Venue as listed in `../sources/publications/scholar.md`.

| Card | Year | Title | Venue | Read | Batch | Note |
|---|---|---|---|---|---|---|
| S001 | 2006 | Numerical Optimization, Second Edition | Numerical optimization, 497-528, 2006 | abstract | a2-02 |  |
| S002 | 1989 | On the limited memory BFGS method for large scale optimization | Mathematical programming 45 (1), 503-528, 1989 | full | c01, c4-01 | two cards from one text: numbers from the round-4 (inc-ocr) card only |
| S003 | 1995 | A limited memory algorithm for bound constrained optimization | SIAM Journal on scientific computing 16 (5), 1190-1208, 1995 | full | c02, c4-02 | two cards from one text: numbers from the round-4 (inc-ocr) card only |
| S004 | 2018 | Optimization methods for large-scale machine learning | SIAM review 60 (2), 223-311, 2018 | full | c09 |  |
| S005 | 1997 | Algorithm 778: L-BFGS-B: Fortran subroutines for large-scale bound-constrained optimiza… | ACM Transactions on mathematical software (TOMS) 23 (4),… | full | c02, c4-02 | two cards from one text: numbers from the round-4 (inc-ocr) card only |
| S006 | 2016 | On large-batch training for deep learning: Generalization gap and sharp minima | arXiv preprint arXiv:1609.04836, 2016 | full | c07 |  |
| S007 | 1980 | Updating quasi-Newton matrices with limited storage | Mathematics of computation 35 (151), 773-782, 1980 | full | c01 |  |
| S008 | 1999 | An interior point algorithm for large-scale nonlinear programming | SIAM Journal on Optimization 9 (4), 877-900, 1999 | full | c03, c4-03 | two cards from one text: numbers from the round-4 (inc-ocr) card only |
| S009 | 2000 | A trust region method based on interior point techniques for nonlinear programming | Mathematical programming 89 (1), 149-185, 2000 | full | c04, c4-03 | two cards from one text: numbers from the round-4 (inc-ocr) card only |
| S010 | 1999 | Numerical optimization | Springer Science 35 (67-68), 7, 1999 | abstract | a2-02 |  |
| S011 | 2006 | Knitro: An Integrated Package for Nonlinear Optimization | Large-scale nonlinear optimization, 35-59, 2006 | full | c05 |  |
| S012 | 1992 | Global convergence properties of conjugate gradient methods for optimization | SIAM Journal on optimization 2 (1), 21-42, 1992 | full | c01 |  |
| S013 | 2006 | An interior algorithm for nonlinear optimization that combines line search and trust re… | Mathematical programming 107 (3), 391-408, 2006 | full | c05 |  |
| S014 | 1994 | Representations of quasi-Newton matrices and their use in limited memory methods | Mathematical Programming 63 (1), 129-156, 1994 | full | c02, c4-01 | two cards from one text: numbers from the round-4 (inc-ocr) card only |
| S015 | 2016 | A stochastic quasi-Newton method for large-scale optimization | SIAM Journal on Optimization 26 (2), 1008-1031, 2016 | full | c08 |  |
| S016 | 2011 | Remark on “Algorithm 778: L-BFGS-B: Fortran subroutines for large-scale bound constrain… | ACM Transactions on Mathematical Software (TOMS) 38 (1),… | full | a2-02, c3-01 | cite as [S016 preprint p. N]; upgraded in round 3; the deeper card is used |
| S017 | 1989 | A tool for the analysis of quasi-Newton methods with application to unconstrained minim… | SIAM Journal on Numerical Analysis 26 (3), 727-739, 1989 | abstract | a2-01 |  |
| S018 | 2012 | Sample size selection in optimization methods for machine learning | Mathematical programming 134 (1), 127-155, 2012 | full | c07 |  |
| S019 | 1992 | Theory of algorithms for unconstrained optimization | Acta numerica 1, 199-242, 1992 | full | c02, c4-01 | two cards from one text: numbers from the round-4 (inc-ocr) card only |
| S020 | 1987 | Global convergence of a class of quasi-Newton methods on convex problems | SIAM Journal on Numerical Analysis 24 (5), 1171-1190, 1987 | full | c01 |  |
| S021 | 2001 | On the solution of equality constrained quadratic programming problems arising in optim… | SIAM Journal on Scientific Computing 23 (4), 1376-1395, 2001 | full | c04, c4-03 | two cards from one text: numbers from the round-4 (inc-ocr) card only |
| S022 | 1985 | Projected Hessian updating algorithms for nonlinearly constrained optimization | SIAM Journal on Numerical Analysis 22 (5), 821-850, 1985 | abstract | a2-01 |  |
| S023 | 2011 | On the use of stochastic hessian information in optimization methods for machine learning | SIAM Journal on Optimization 21 (3), 977-995, 2011 | full | c06 |  |
| S024 | 1998 | Combining trust region and line search techniques | Advances in Nonlinear Programming: Proceedings of the 96… | full | c03, c4-02 | two cards from one text: numbers from the round-4 (inc-ocr) card only |
| S025 | 1991 | A numerical study of the limited memory BFGS method and the truncated-Newton method for… | SIAM Journal on Optimization 1 (3), 358-372, 1991 | abstract | a2-01 |  |
| S026 | 1987 | The formulation and analysis of numerical methods for inverse eigenvalue problems | SIAM Journal on Numerical Analysis 24 (3), 634-667, 1987 | partial | s01 |  |
| S027 | 2006 | Interior methods for mathematical programs with complementarity constraints | SIAM Journal on Optimization 17 (1), 52-77, 2006 | partial | s04 |  |
| S028 | 1995 | A reduced Hessian method for large-scale constrained optimization | SIAM Journal on Optimization 5 (2), 314-347, 1995 | full | s02, s4-01 | two cards from one text: numbers from the round-4 (inc-ocr) card only |
| S029 | 2009 | Adaptive barrier update strategies for nonlinear interior methods | SIAM Journal on Optimization 19 (4), 1674-1693, 2009 | full | c06 |  |
| S030 | 2000 | Automatic preconditioning by limited memory quasi-Newton updating | SIAM Journal on Optimization 10 (4), 1079-1096, 2000 | full | c2-01, s03 | two cards from one text: numbers from the round-2 card only |
| S031 | 2018 | A progressive batching L-BFGS method for machine learning | International Conference on Machine Learning, 620-629, 2018 | full | c10 |  |
| S032 | 2019 | Exact and inexact subsampled Newton methods for optimization | IMA Journal of Numerical Analysis 39 (2), 545-578, 2019 | full | s07 | cite as [S032 arXiv p. N] |
| S033 | 2016 | A multi-batch L-BFGS method for machine learning | Advances in Neural Information Processing Systems 29, 2016 | partial | s06 |  |
| S034 | 1998 | On the implementation of an algorithm for large-scale equality constrained optimization | SIAM Journal on Optimization 8 (3), 682-706, 1998 | full | s02 |  |
| S035 | 2003 | An algorithm for nonlinear optimization using linear programming and equality constrain… | Mathematical Programming 100 (1), 27-48, 2003 | full | c2-01, s04 | two cards from one text: numbers from the round-2 card only; cite as [S035 report p. N] |
| S036 | 2018 | Adaptive sampling strategies for stochastic optimization | SIAM Journal on Optimization 28 (4), 3312-3343, 2018 | partial | s06 |  |
| S038 | 2019 | Derivative-free optimization of noisy functions via quasi-Newton methods | SIAM Journal on Optimization 29 (2), 965-993, 2019 | full | c10 |  |
| S039 | 1990 | An analysis of reduced Hessian methods for constrained optimization | Mathematical Programming 49 (1), 285-323, 1990 | partial | s01 |  |
| S040 | 2002 | Wedge trust region methods for derivative free optimization | Mathematical programming 91 (2), 289-305, 2002 | full | c2-01, s03 | two cards from one text: numbers from the round-2 card only |
| S041 | 2020 | An investigation of Newton-sketch and subsampled Newton methods | Optimization Methods and Software 35 (4), 661-680, 2020 | full | c10 |  |
| S042 | 2008 | Steering exact penalty methods for nonlinear programming | Optimization Methods and Software 23 (2), 197-213, 2008 | full | c05 |  |
| S043 | 2012 | Newton-like methods for sparse inverse covariance estimation | Advances in neural information processing systems 25, 2012 | full | a2-02, c3-01 | upgraded in round 3; the deeper card is used |
| S044 | 1992 | On the behavior of Broyden’s class of quasi-Newton methods | SIAM Journal on Optimization 2 (4), 533-557, 1992 | abstract | a2-01 |  |
| S045 | 2008 | An inexact SQP method for equality constrained optimization | SIAM Journal on Optimization 19 (1), 351-369, 2008 | full | s05 |  |
| S046 | 1997 | On the local behavior of an interior point method for nonlinear programming | Numerical analysis 1997, 37-56, 1997 | full | s02, s4-01 | two cards from one text: numbers from the round-4 (inc-ocr) card only |
| S047 | 2009 | Data assimilation in weather forecasting: a case study in PDE-constrained optimization | Optimization and Engineering 10 (3), 409-426, 2009 | full | c06 |  |
| S049 | 1997 | Large scale unconstrained optimization | INSTITUTE OF MATHEMATICS AND ITS APPLICATIONS CONFERENCE… | full | c03, c4-02 | two cards from one text: numbers from the round-4 (inc-ocr) card only |
| S050 | 2016 | An inexact successive quadratic approximation method for L-1 regularized optimization | Mathematical Programming 157 (2), 375-396, 2016 | partial | s06 |  |
| S051 | 2012 | A line search exact penalty method using steering rules | Mathematical Programming 133 (1), 39-73, 2012 | partial | s05 |  |
| S052 | 2010 | Infeasibility detection and SQP methods for nonlinear optimization | SIAM Journal on Optimization 20 (5), 2281-2299, 2010 | full | c06 |  |
| S053 | 2014 | An interior point method for nonlinear programming with infeasibility detection capabil… | Optimization Methods and Software 29 (4), 837-854, 2014 | full | c07 |  |
| S054 | 1993 | Analysis of a self-scaling quasi-Newton method | Mathematical Programming 61 (1), 19-37, 1993 | partial | s01 |  |
| S055 | 1996 | Conjugate gradient methods and nonlinear optimization | Linear and nonlinear conjugate gradient-related methods,… | metadata | a2-02 |  |
| S056 | 1994 | L-BFGS-B: a limited memory FORTRAN code for solving bound constrained optimization prob… | Technique Report Rep, 1994 | metadata | a2-01 | probably the same report as S143: counted once |
| S057 | 2002 | On the behavior of the gradient norm in the steepest descent method | Computational Optimization and Applications 22 (1), 5-35,… | full | c2-01, s03 | two cards from one text: numbers from the round-2 card only |
| S058 | 2005 | On the convergence of successive linear-quadratic programming algorithms | SIAM Journal on Optimization 16 (2), 471-489, 2005 | full | s04 |  |
| S060 | 2012 | A sequential quadratic programming algorithm with an additional equality constrained phase | IMA Journal of Numerical Analysis 32 (2), 553-579, 2012 | partial | s06 |  |
| S061 | 2004 | On the convergence of Newton iterations to non-stationary points | Mathematical Programming 99 (1), 127-148, 2004 | full | c04, c4-04 | two cards from one text: numbers from the round-4 (inc-ocr) card only |
| S062 | 2009 | On the geometry phase in model-based algorithms for derivative-free optimization | Optimization Methods & Software 24 (1), 145-154, 2009 | full | c06 |  |
| S063 | 2003 | KNITRO user’s manual | Northwestern University, Evanston, Illinois, Technical Re… | full | a2-02, s3-01 | KNITRO 3.0 manual: product voice; upgraded in round 3; the deeper card is used |
| S064 | 2016 | A family of second-order methods for convex ℓ1-regularized optimization | Mathematical Programming 159 (1), 435-467, 2016 | full | a2-03, c3-01 | cite as [S064 preprint p. N]; upgraded in round 3; the deeper card is used |
| S066 | 2004 | Knitro 2.0 user’s manual | Ziena Optimization, Inc.[en ligne] disponible sur http://… | metadata | a2-02 |  |
| S067 | 2000 | Numerical experience with a reduced Hessian method for large scale constrained optimiza… | Computational Optimization and Applications 15 (1), 45-67… | full | s03, s2-01 | two cards from one text: numbers from the round-2 card only |
| S068 | 2010 | An inexact Newton method for nonconvex equality constrained optimization | Mathematical programming 122 (2), 273-299, 2010 | full | s05 |  |
| S070 | 1987 | The use of linear programming for the solution of sparse sets of nonlinear equations | SIAM Journal on Scientific and Statistical Computing 8 (2… | abstract | a2-01 |  |
| S071 | 2022 | A noise-tolerant quasi-Newton algorithm for unconstrained optimization | SIAM Journal on Optimization 32 (1), 29-55, 2022 | full | c11 |  |
| S072 | 2020 | Analysis of the BFGS method with errors | SIAM Journal on Optimization 30 (1), 182-209, 2020 | full | c11 |  |
| S073 | 2010 | A matrix-free algorithm for equality constrained optimization problems with rank-defici… | SIAM Journal on Optimization 20 (3), 1224-1249, 2010 | partial | s05 |  |
| S075 | 2003 | Feasible interior methods using slacks for nonlinear optimization | Computational Optimization and Applications 26 (1), 35-61… | full | s04, s2-01 | two cards from one text: numbers from the round-2 card only |
| S076 | 2008 | An algorithm for the fast solution of symmetric linear complementarity problems | Numerische Mathematik 111 (2), 251-266, 2008 | full | s05 |  |
| S077 | 2002 | Enriched methods for large-scale unconstrained optimization | Computational Optimization and Applications 21 (2), 143-1… | full | s03, s2-01 | two cards from one text: numbers from the round-2 card only |
| S078 | 2003 | Assessing the potential of interior methods for nonlinear optimization | Large-scale PDE-constrained Optimization, 167-183, 2003 | full | c04, c4-04 | two cards from one text: numbers from the round-4 (inc-ocr) card only |
| S080 | 2023 | On the numerical performance of finite-difference-based methods for derivative-free opt… | Optimization Methods and Software 38 (2), 289-311, 2023 | full | c12 | cite as [S080 arXiv p. N] |
| S081 | 2008 | Flexible penalty functions for nonlinear constrained optimization | IMA journal of numerical analysis 28 (4), 749-769, 2008 | full | s05 |  |
| S082 | 2023 | A trust region method for noisy unconstrained optimization | Mathematical Programming 202 (1), 445-472, 2023 | full | c13 |  |
| S084 | 2023 | Constrained optimization in the presence of noise | SIAM Journal on Optimization 33 (3), 2118-2136, 2023 | full | c13 |  |
| S085 | 2004 | A starting point strategy for nonlinear interior methods | Applied mathematics letters 17 (8), 945-952, 2004 | full | s04 |  |
| S086 | 1985 | A conic algorithm for optimization | SIAM journal on scientific and statistical computing 6 (2… | abstract | a2-01 |  |
| S087 | 2015 | An algorithm for quadratic ℓ1-regularized optimization with a flexible active-set strategy | Optimization Methods and Software 30 (6), 1213-1237, 2015 | partial | s06 |  |
| S088 | 1996 | Towards a discrete Newton method with memory for large-scale optimization | Nonlinear optimization and applications, 1-12, 1996 | partial | s02, s4-01 | two cards from one text: numbers from the round-4 (inc-ocr) card only |
| S089 | 2016 | A second-order method for convex ℓ1-regularized optimization with active-set prediction | Optimization Methods and Software 31 (3), 605-621, 2016 | partial | s06 |  |
| S090 | 1997 | Mechanics in the engineering first curriculum at Northwestern University | International Journal of Engineering Education 13 (6), 1997 | full | s02 |  |
| S091 | 2022 | Adaptive finite-difference interval estimation for noisy derivative-free optimization | SIAM Journal on Scientific Computing 44 (4), A2302-A2321,… | full | s07 | cite as [S091 arXiv p. N] |
| S092 | 2011 | On the solution of complementarity problems arising in American options pricing | Optimization methods and Software 26 (4-5), 813-825, 2011 | full | s05 |  |
| S097 | 1983 | Numerical methods for solving inverse eigenvalue problems | Numerical Methods: Proceedings of the International Works… | metadata | a2-01 |  |
| S098 | 2001 | Algorithm 809: PREQN: Fortran 77 subroutines for preconditioning the conjugate gradient… | ACM Transactions on Mathematical Software (TOMS) 27 (1),… | full | s03, s2-01 | two cards from one text: numbers from the round-2 card only |
| S100 | 1990 | The performance of several algorithms for large scale unconstrained optimization | Large Scale Numerical Optimization, 138-151, 1990 | abstract | a2-01 |  |
| S101 | 1998 | The modified absolute-value factorization norm for trust-region minimization | High Performance Algorithms and Software in Nonlinear Opt… | full | s02, s4-01 | two cards from one text: numbers from the round-4 (inc-ocr) card only |
| S102 | 2024 | Constrained and composite optimization via adaptive sampling methods | IMA Journal of Numerical Analysis 44 (2), 680-709, 2024 | full | c13 |  |
| S103 | 1989 | Algorithms with conic termination for nonlinear optimization | SIAM journal on scientific and statistical computing 10 (… | abstract | a2-01 |  |
| S105 | 2008 | A numerical study of active-set and interior-point methods for bound constrained optimi… | Modeling, Simulation and Optimization of Complex Processe… | full | c05 |  |
| S108 | 1993 | Automatic column scaling strategies for quasi-Newton methods | SIAM Journal on Optimization 3 (3), 637-653, 1993 | abstract | a2-01 |  |
| S109 | 1979 | Analysis of a new algorithm for one-dimensional minimization | Computing 22 (1), 93-100, 1979 | abstract | a2-01 |  |
| S110 | 2007 | Steplength selection in interior-point methods for quadratic programming | Applied mathematics letters 20 (5), 516-523, 2007 | full | s05 |  |
| S111 | 2001 | Feasibility control in nonlinear optimization | Foundations of Computational Mathematics 284, 125, 2001 | full | s03, s2-01 | two cards from one text: numbers from the round-2 card only |
| S113 | 2013 | Subspace accelerated matrix splitting algorithms for asymmetric and symmetric linear co… | SIAM Journal on Optimization 23 (3), 1371-1397, 2013 | partial | s06 |  |
| S114 | 2013 | On the use of piecewise linear models in nonlinear programming | Mathematical Programming 137 (1), 289-324, 2013 | partial | s06 |  |
| S115 | 1993 | Automatic differentiation and the step computation in the limited memory BFGS method | Applied mathematics letters 6 (3), 47-50, 1993 | full | s01 |  |
| S116 | 1982 | Conjugate direction methods with variable storage | Mathematical Programming 23 (1), 326-340, 1982 | abstract | a2-01 |  |
| S118 | 1998 | Active set and interior methods for nonlinear optimization | Proceedings of the International Congress of Mathematicia… | full | s02 |  |
| S119 | 2002 | iNEOS: An interactive environment for nonlinear optimization | Applied numerical mathematics 40 (1-2), 49-57, 2002 | full | s04, s2-01 | two cards from one text: numbers from the round-2 card only |
| S120 | 1978 | A study of conjugate gradient methods | — | partial | a2-01, s3-01 | upgraded in round 3; the deeper card is used |
| S123 | 1986 | Four quadratically convergent methods for solving inverse eigenvalue problems | Numerical analysis 11, 47, 1986 | abstract | a2-01 |  |
| S124 | 2024 | A trust-region algorithm for noisy equality constrained optimization | arXiv preprint arXiv:2411.02665, 2024 | full | c14 |  |
| S125 | 2011 | L-bfgs-b | Retrieved Feb 18, 2012, 2011 | abstract | a2-02 |  |
| S126 | 2006 | Steering exact penalty methods for optimization | Optimization Technology Center, Northwestern University,… | full | s04 | earlier report of S042: counted once with it |
| S128 | 2025 | Design guidelines for noise-tolerant optimization with applications in robust design | SIAM Journal on Scientific Computing 47 (3), A1335-A1357,… | full | c14 |  |
| S135 | 2012 | Second-order methods for L1 regularized problems in machine learning | 2012 IEEE International Conference on Acoustics, Speech a… | abstract | a2-02 |  |
| S136 | 2005 | Introducing a constructivist approach to applying programming skills in engineering ana… | Proceedings Frontiers in Education 35th Annual Conference… | abstract | a2-02 |  |
| S138 | 1978 | ON THE METHOD OF CONJUGATE GRADIENTS FOR FUNCTION MINIMIZATION. | Rice University, 1978 | partial | s01 |  |
| S139 | 2011 | An implementation of an algorithm for nonlinear programming based on piecewise linear m… | Technical Report, Optimization Center, Northwestern Unive… | full | a2-02, s3-01 | upgraded in round 3; the deeper card is used |
| S140 | 2008 | A line search penalty method for nonlinear optimization | Technical Report 08/05, Optimization Technology Center, N… | metadata | a2-02 |  |
| S141 | 1982 | Solving large nonlinear systems of equations arising in mechanics | Numerical Analysis: Proceedings of the Third IIMAS Worksh… | metadata | a2-01 |  |
| S143 | 1994 | LBFGS-B: Fortran Subroutines tor Large-Scale Bound Constrained Optimization | Report NAM-11, 1994 | full | s01 |  |
| S147 | 1998 | On the accuracy of nonlinear optimization algorithms | Technical Report Nov. 1998, ECE Department, Northwestern… | metadata | a2-02 |  |
| S148 | 1994 | Recent advances in large-scale nonlinear optimization | Univ. of Michigan, Ann Arbor, MI (United States), 1994 | abstract | a2-01 |  |
| S149 | 1984 | Trust region algorithms for solving large systems of nonlinear equations | Innovative Methods for Nonlinear Problems, 93-102, 1984 | metadata | a2-01 |  |
| S150 | 2026 | A feasible method for constrained derivative-free optimization | Operations Research Letters 65, 107398, 2026 | full | c14 |  |
| S152 | 2013 | Second order methods for optimizing convex matrix functions and sparse covariance clust… | IEEE transactions on audio, speech, and language processi… | abstract | a2-02 |  |
| S154 | 2009 | An Algorithm for Linear Complementarity and its Application in American Options Pricing | AIP Conference Proceedings 1168 (1), 1400-1402, 2009 | metadata | a2-02 |  |
| S155 | 2008 | Enjeux éthiques de la différence dans l'approche du genre | Les Politiques Sociales, 2008 | metadata | a2-02 | not by Nocedal: never evidence |
| S160 | 1996 | Nonlinear Programming. | Mathematics of Computation 65 (214), 884-884, 1996 | full | s02 |  |
| S162 | 1978 | Properties of Conjugate Gradient Methods with Inexact Linear Searches. | — | abstract | a2-01 |  |
| S163 | — | L-BFGS | — | metadata | a2-03 |  |
| S164 | 2026 | Package 'rIsing' | — | metadata | a2-03 | non-research row (Role=skip): never evidence |
| S165 | 2026 | Package 'ldt' | — | metadata | a2-03 | non-research row (Role=skip): never evidence |
| S166 | 2024 | An Iterative Approach for Solving the SCOPF Problem Applying LP, SOCP, and NLP Subproblems | Northwestern University, 2024 | abstract | a2-03 |  |
| S167 | 2020 | Zero-Order and Stochastic Methods for Large-Scale Optimization | NSF Award Number 2011494. Directorate for Mathematical an… | abstract | a2-03 | NSF award abstract: dates interests only |
| S168 | 2020 | Package 'lbfgsb3c' | — | metadata | a2-03 |  |
| S169 | 2016 | Collaborative Research: Algorithms for Large-Scale Stochastic and Nonlinear Optimization | NSF Award Number 1620022. Directorate for Mathematical an… | abstract | a2-03 | NSF award abstract: dates interests only |
| S171 | 2014 | Devising Optimization Algorithms for Machine Learning | Collections 47 (07), 2014 | metadata | a2-02 |  |
| S173 | 2012 | Collaborative Research: Methods for Stochastic and Nonlinear Optimization | NSF Award Number 1216567. Directorate for Mathematical an… | abstract | a2-02 | NSF award abstract: dates interests only |
| S174 | 2010 | Collaborative Research: Market-Based Calibration of Pricing Models for Financial and En… | NSF Award Number 1030540. Directorate for Engineering 10… | abstract | a2-02 | NSF award abstract: dates interests only |
| S176 | 2008 | Nonlinear Optimization: Algorithms, Theory and Software | NSF Award Number 0810213. Directorate for Mathematical an… | abstract | a2-02 | NSF award abstract: dates interests only |
| S177 | 1986 | Viewing the conjugate gradient method as a trust region algorithm | Numerical Analysis: Proceedings of the Fourth IIMAS Works… | abstract | a2-01 |  |
| S178 | 2005 | Active-Set and Interior Algorithms for Non-Linear Optimization | NSF Award Number 0514772. Directorate for Computer and In… | abstract | a2-02 | NSF award abstract: dates interests only |
| S179 | 2004 | 4.7 Sequential linear-quadratic programming for huge optimization problems (RH Byrd, NI… | Numerical Analysis Group Progress Report January 2002-Dec… | full | s04 | RAL group progress report: collective voice |
| S180 | 2003 | Solving optimization problems using parallel and grid computing | Proceedings of the Fourth Mexican International Conferenc… | metadata | a2-02 |  |
| S181 | 2003 | Interior Point Methods for Mathematical Programs with Equilibrium Constraints (MPECs) | — | metadata | a2-02 |  |
| S184 | 2002 | ITR: Collaborative Research: Optimization of Systems Governed by Partial Differential E… | NSF Award Number 0219438. Directorate for Computer and In… | abstract | a2-02 | NSF award abstract: dates interests only |
| S186 | 2001 | Collaborative Research: Improved Minimization Techniques in Meteorological Data Assimil… | NSF Award Number 0086579. Directorate for Geosciences, 86… | abstract | a2-02 | NSF award abstract: dates interests only |
| S187 | 2000 | Large-Scale Nonlinear Programming | NSF Award Number 9987818. Directorate for Computer and In… | abstract | a2-02 | NSF award abstract: dates interests only |
| S188 | 2000 | 3.3 Linear systems and optimization (NIM Gould, ME | Numerical Analysis Group Progress Report January 1998-Dec… | full | s03 | RAL group progress report: collective voice |
| S189 | 1997 | Challenges in CISE: Metacomputing Environments for Optimization | NSF Award Number 9726385. Directorate for Computer and In… | abstract | a2-02 | NSF award abstract: dates interests only |
| S190 | 1996 | Nonlinear Optimization | NSF Award Number 9625613. Directorate for Computer and In… | abstract | a2-02 | NSF award abstract: dates interests only |
| S191 | 1994 | Extending interior point method to nonlinear programming using trust regions | Univ. of Michigan, Ann Arbor, MI (United States), 1994 | abstract | a2-02 |  |
| S192 | 1994 | Numerical Optimization Techniques | NSF Award Number 9400881. Directorate for Computer and In… | abstract | a2-02 | NSF award abstract: dates interests only |
| S193 | 1993 | Optimization and eigenvalue computation with application to meteorology and oceanograph… | Northwestern Univ., Evanston, IL (United States), 1993 | full | s01 |  |
| S194 | 1992 | University of Co o ado | — | metadata | a2-01 |  |
| S195 | 1992 | Optimization Algorithms for Advanced Computer Architectures | NSF Award 92 (9213149), 13149, 1992 | abstract | a2-01 | NSF award abstract: dates interests only |
| S196 | 1991 | Large Scale Nonlinear Optimization | NSF Award Number 9101359. Directorate for Computer and In… | abstract | a2-01 | NSF award abstract: dates interests only |
| S197 | 1990 | Algorithms and software for large scale optimization. Progress report, August 1, 1989--… | Northwestern Univ., Evanston, IL (United States), 1990 | full | s01 |  |
| S198 | 1990 | Numeric Methods for Nonlinear Optimization | NSF Award Number 8902096. Directorate for Computer and In… | abstract | a2-01 | NSF award abstract: dates interests only |
| S199 | 1988 | 三川 University of Colorado at Boulder | — | metadata | a2-01 |  |
| S202 | 1986 | Algorithms for Optimization and Inverse Eigenvalue Problems (Computer Research) | NSF Award Number 8602071. Directorate for Computer and In… | metadata | a2-01 | NSF award abstract: dates interests only |
| S203 | 1986 | On the Implementation of the Conjugate Gradient Method for Function Minimization | Northwestern University, Department of Electrical Enginee… | metadata | a2-01 |  |
| S204 | 1985 | Evaluation of step directions in optimization algorithms | ACM Transactions on Mathematical Software (TOMS) 11 (1),… | abstract | a2-01 |  |
| S205 | 1985 | On the Numerical Solution of Inverse Eigenvalue Problems | Northwestern University, Department of Electrical Enginee… | metadata | a2-01 |  |
| S206 | 1984 | Numerical Methods For Nonlinear Optimization | NSF Award Number 8401903. Directorate for Computer and In… | metadata | a2-01 | NSF award abstract: dates interests only |
| S210 | — | Two Approaches for Nonlinear Programming | — | metadata | a2-03 |  |
| S214 | — | SIAM/ASA Journal on Uncertainty Quantification (editorial listing) | — | metadata | a2-03 | non-research row (Role=skip): never evidence |
| S215 | — | Stochastik und Finanzmathematik | fsmathe@ math. uni-saarland. de http://math. fs. uni-saar… | metadata | a2-03 | non-research row (Role=skip): never evidence |
| S218 | 2013 | Special Section on Large-Scale Optimization for Audio, Speech, and Language Processing | — | metadata | a2-03 | non-research row (Role=skip): never evidence |
| S219 | — | José Luis Morales (ITAM) and J. Nocedal: scanned title page | — | metadata | a2-03 |  |
| S221 | — | Computer Science Department, University of Colorado at Boulder: scanned report title page | Computer Science 2, 1, 0 | metadata | a2-03 |  |
| B001 | 2006 | Numerical Optimization, Second Edition: front matter with prefaces, dedications and table of contents (Spri… | book material | full | c5-01 | book material, joint voice with S. J. Wright |
| B002 | 2006 | Numerical Optimization, Second Edition: back matter with Appendix A, Appendix B, references and index (Sp… | book material | full | c5-02 | book material, joint voice with S. J. Wright |
| B003 | 2008 | Corrections to Numerical Optimization, Second Edition (last updated May 27, 2008): Nocedal's homepage | book material | full | c5-02 | errata, joint; 80 items (C20) |
| B004 | 2008 | Corrections to Numerical Optimization, Second Edition (last updated May 17, 2008): Wright's homepage | book material | full | c5-03 | errata, joint; 79 items (C20) |
| B005 | 1999 | Numerical Optimization, First Edition: front matter with preface, dedication and table of contents (Spring… | book material | full | c5-01 | book material, joint; the Byrd sentence is the only Nocedal-specific item |
| B006 | 1999 | Numerical Optimization, First Edition: back matter with Appendix A, references and index (Springer free p… | book material | full | c5-01 | book material, joint voice with S. J. Wright |
| B007 | 2000 | Corrections to First Printing of Nocedal-Wright (first edition; additional corrections noted 2/25/2000) | book material | full | c5-01 | errata, joint; OCR text, words only |
| B008 | 2008 | Corrections to Second Printing of Numerical Optimization (first edition; last updated October 2, 2008) | book material | full | c5-03 | errata, joint |
| B009 | 1999 | Review of Numerical Optimization (first edition) by Neculai Curteanu, zbMATH Open, Zbl 0930.65067 | book material | full | c5-01 | reviewer's voice: peer critique only |
| B010 | 2006 | Review of Numerical Optimization (second edition) by Neculai Curteanu, zbMATH Open, Zbl 1104.65059 | book material | full | c5-02 | reviewer's voice: peer critique only |
| B011 | 2006 | Numerical Optimization: the authors' book web pages on Nocedal's homepage (Internet Archive, 2002–2016) | book material | full | c5-02 | joint self-presentation, hosted by Nocedal |
| B012 | 2006 | Numerical Optimization: Springer catalogue pages for the first and second editions | book material | full | c5-02 | publisher's voice, except sentences that repeat the authors |

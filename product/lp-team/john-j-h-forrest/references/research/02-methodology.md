# John J. H. Forrest · 02 Stated methodology (what he says solver research should be)

| Field | Value |
|---|---|
| Researcher | John J. H. Forrest (also John J. Forrest, J. J. H. Forrest, John Forrest; he signs code notes "JJF" or "JJHF"). Author of COIN-OR Clp (first commit 2002-07-30), Abc/Aboca (2012) and CoinUtils' CoinFactorization; one of the developers of Cbc ("developed by John Forrest, now retired from IBM Research, and others", Cbc README). Earlier at Scicon and IBM Research (OSL). By September 2010 an INFORMS program lists him as "IBM Research (Retd.)". |
| Dimension | Research agent 02 of 06: stated methodology. These are his claims about how LP/MIP solver work should be done, sorted into the seven layers of `references/research-extraction-framework.md` §一. Whether he practises them is agent 03's job. |
| Research date | 2026-11-05 |
| Sources consulted | 23. Of these, 15 are primary sources that were read (his own words or co-authored text), 5 are secondary or metadata, and 3 could not be reached (see Gaps). WebSearch: 4 of the 7 allowed. Everything else came from `git` clones, curl, WebFetch, the GitHub REST API (without login), Crossref, Unpaywall and Semantic Scholar. |
| Local corpus | `references/sources/{papers,talks,essays,software}` hold only `.gitkeep`, so there is no user-supplied material. `publications/publications.md` (OpenAlex A5061258306) was read. `private/` was not opened. |
| Saved this run | Nothing under `sources/talks/`: no recorded talk or subtitle file was found. |

## Reading guide

**Tags.**

| Tag | Meaning |
|---|---|
| [stated] | His own single voice. This covers: a code note that he signed (JJF/JJHF) or whose sentence entered the repository in a commit authored "John Forrest" (checked with `git log -S` on full clones); a GitHub issue, PR or Discussions comment; a Cbc FAQ answer signed "JF"; his INFORMS 2010 talk abstract; his 2006 slide deck. |
| [stated-joint] | Co-authored text. The individual voice cannot be separated. |
| [stated, self-report] | His own account of something he did. Agent 03 should check it against the code. |
| [observed] | Somebody else's statement about him. |
| [inferred] | This agent's reading. |
| P / S | Primary / secondary. |
| (LP) (MIP) (general) | Which of his seats the item serves. LP simplex is the LP Team's centre; the MIP items are for the MILP Team. |

**Authorship labels (they must survive into the skill).**
- His code: Clp, Abc and CoinFactorization. Notes from those files are quoted as [stated] only after the introducing commit was checked.
- Cbc is shared code (AUTHORS lists "Forrest, John J." first, then Hafer, Goncalves, Santos and Brito). A Cbc note or help text is quoted here only when it is signed JJF/JJHF, or when the Clp/Cbc history shows a "John Forrest" commit introducing that sentence.
- OSL, LAMPS and UMPIRE: none of his code is visible. Below, OSL appears only (a) in his own sentences about what he put into OSL, and (b) in others' credit, tagged [observed].
- The OSL factorization port in CoinUtils (2009) has first-person lines such as "I don't know why we subtract." They read as a porter's lines, so they are not used.
- Not all of Clp is his: ClpPdco is Tomlin's; ClpPE* is Omer and Towhidi's; some presolve comments are by other hands. Nothing from those files is quoted.
- Repository movers are named where a quoted sentence first appears in their commit. These are Ladanyi's 2002 "devel-1 merged into HEAD" and 2006 "finished switch to subversion", Wächter's 2006 autotools move, Vigerske's 2019 rewording and Ralphs' 2020 parameter move. A mover's commit does not change whose voice the sentence is.

**Account linkage and counts.**
- The GitHub accounts `jjhforrest` and `johnjforrest` (display name "John Forrest" on both) are linked to him by strong inference, not by any document.
- Observed this run:
  - `jjhforrest` was created 2014-03-31 and wrote 485 of his 486 issue/PR comments, from 2017-11-20 onward.
  - `johnjforrest` was created 2019-06-14 and wrote one comment (Clp#138, 2020-03-21).
  - The 2020 hand-over noted in team.json therefore concerns commit authorship, not comments.
- His comment corpus:
  - 486 issue/PR comments, 2017-11-20 to 2026-11-01: Cbc 315, Clp 103, CoinUtils 28, Clp.old 21, Cgl 14, scipopt/papilo 2, Bonmin 1, SHOT 1, Osi 1. team.json says 461; the difference was not resolved.
  - 86 GitHub Discussions comments, 2020-12-06 to 2026-05-25, parsed from 36 threads: Cbc 61 comments in 24 threads, Clp 19 in 10, Cgl 6 in 2. GitHub's commenter filter lists 38 threads; one more Cgl thread and one CoinUtils thread yielded no parsed comment. These comments are not in team.json's count.

**Quote checking.**
- All 143 quotes taken from GitHub comments and Discussions were checked by script against the downloaded text (whitespace normalised). His spelling is kept (e.g. "situtaion", "may real world").
- Code and help-text quotes were read in the files and dated by the commit that introduced them. C-string line continuations are removed.
- A final script pass checked every quoted string in this file against the downloaded corpus: code, historical help-text versions, comments, guides, the ICM and Optima texts, the deck text and the Crossref abstracts. Only three kinds of string are not in that corpus. Git commit subjects were checked with `git show` instead. The two mailing-list titles come from search results and are labelled as such. The rest are text fragments between two separate quotations, not quotations.
- E-mail addresses that occur in the harvested texts are not reproduced.

---

## A. Source corpus and its era and resource context

| ID | Source | Date | Voice | Era / resource context |
|---|---|---|---|---|
| C1 | Clp first commit `b4253486`: README; design notes at the top of ClpSimplexDual.cpp and ClpSimplexPrimal.cpp; headers | 2002-07-30 | [stated] P | IBM Research. Clp is new C++ code; the notes compare it with OSL throughout. g++ 2.95, GNU make. The netlib set is the test bed. |
| C2 | Clp master (HEAD `87446523`, 2026-11-02): code notes in ClpSimplex.hpp, ClpModel.hpp, ClpSimplexPrimal.hpp, ClpSimplexDual.hpp, ClpNonLinearCost.hpp, ClpPrimalColumnSteepest.hpp, ClpHelperFunctions.hpp, ClpPredictorCorrector.hpp, Idiot.hpp, CbcOrClpParam.hpp, ClpSolve.cpp, ClpMain.cpp (version log), ClpParameters.cpp; examples sprint.cpp, ekk.cpp, addRows.cpp | sentences introduced 2002–2012 | [stated] P | IBM Research until retirement (date unknown; "Retd." by Sept 2010). Netlib tuning was done on "a Linux ThinkPad" (2005). |
| C3 | Clp `Test/ClpMain.cpp` help texts at commit `6cd3154e` | 2003-10-08 | [stated] P | Stand-alone `clp` executable; the help text is the user documentation. |
| C4 | `CbcOrClpParam.cpp` help texts shared by Clp and Cbc, at Forrest commits `2ea34581` (2006-02-20), `d567df54` (2006-02-21), 2008-07-17 and later | 2004–2009 | [stated] P | IBM Research; Cbc 1.0 era. |
| C5 | CoinUtils master (`231b801e`): CoinFactorization.hpp ("Authors … John Forrest"), CoinFactorization3.cpp, CoinMessageHandler.hpp, CoinModel.hpp | 2002–2005 | [stated] P | The factorization grew out of "a parallel simplex code I was writing in the mid 90's". The notes entered CoinUtils in Ladanyi's bulk merge of 2002-11-05. |
| C6 | Cbc master (`001b861c`): README.md, AUTHORS, CoinSolve.cpp ("old comments for historical interest", 2005), CbcSymmetry.cpp header (2014), CbcGeneralDepth.cpp (2024), CbcGeneral.cpp (2023), doc/cbc-parameters.md | 2005–2026 | [stated] P where signed or committed by him; README [observed] | Cbc is shared code; see the authorship labels. |
| G1 | 486 GitHub issue/PR comments (Cbc, Clp, Clp.old, CoinUtils, Cgl, Osi, Bonmin, SHOT, scipopt/papilo) | 2017-11-20 – 2026-11-01 | [stated] P | Retired volunteer maintainer. Linux/Ubuntu, gcc 11.4, "my small laptop" (2024, 2026), "I rarely use Windows" (2024), no NVIDIA GPU (2021). |
| G2 | 86 GitHub Discussions comments from 36 threads (Cbc 24, Clp 10, Cgl 2) | 2020-12-06 – 2026-05-25 | [stated] P | As G1. The 2026 threads cover the AI-assisted "next"/modernisation work on Cbc. |
| P1 | Anbil, Forrest, Pulleyblank, "Column generation and the airline crew pairing problem", Documenta Math. Extra Vol. ICM 1998 III, 677–686, DOI 10.4171/dms/1-3/65 (read in full) | 1998 | [stated-joint] P | IBM. OSL Primal/Dual/Sprint timed on S/390 "in 1989"; RS6000/590. |
| P2 | CBC User's Guide, web version at coin-or.org/Cbc (authors John Forrest and Robin Lougee-Heimer). Revision 0.2 (2 May 2005) is the "Book chapter for CBC Tutorial at INFORMS 2005 annual meeting", i.e. DOI 10.1287/educ.1053.0020. FAQ answers are signed "JF" (2005–06). The feasibility-pump notes were added in 2019 from the Trac wiki. | 2005–2006 (conversion 2019) | guide [stated-joint] P; JF answers [stated] P; FP notes [stated] with attribution inferred | IBM Research. |
| P3 | CLP User's Guide, web version at coin-or.org/Clp (Forrest, de la Nuez, Lougee-Heimer; draft Nov 2003, release 0.4 of 18 Oct 2004) and Clp FAQ (answers signed "DN") | 2003–2004 | guide [stated-joint] P; FAQ [observed] S | IBM Research. |
| P4 | Bonami, Forrest, Lee, Wächter, "Rapid Development of an Open-source Minlp Solver with COIN-OR", Optima 75, Dec 2007, pp. 1–4 (read; open copy at mathopt.zib.de) | 2007 | [stated-joint] P | IBM–CMU open collaborative research on MINLP. |
| P5 | Crossref abstracts (full texts not read): UMPIRE (Management Science 1974); IBM semiconductor supply chain MIP (Interfaces 2006); multiple knapsack with colour constraints (IJOC 2006) | 1974, 2006 | [stated-joint] P | Scicon (1974); IBM (2006). |
| T1 | Slide deck by John Forrest, dated July 18 2006, titled "Coin Branch and Cut A tutorial" in the host's extraction. 35-page PDF; the text read is as extracted by the third-party host api.sambuz.com | 2006-07-18 | [stated] P via third-party host | Same week as the DIMACS COIN-OR workshop (17–20 July 2006), where T3 lists his CBC tutorial. That this deck is the one he gave there is inferred from the dates. The host's text extraction drops letters ("S lve"), so only intact fragments are quoted. |
| T2 | INFORMS 2010 cluster "John Forrest-fest \| COIN-OR 10th", as recorded on 8 Sept 2010 and copied on Jiadong Wang's blog (6 March 2011) | 2010 | his abstract [stated] P via secondary host; others' abstracts [observed] S | Retired ("IBM Research (Retd.)"). |
| T3 | DIMACS Workshop on COIN-OR (17–20 July 2006): program and abstracts (archive.dimacs.rutgers.edu) | 2006 | [observed] S | Tutorial descriptions only. |
| O1 | COIN-OR INFORMS Cup 2005 citation (coin-or.org/coinCup/coinCup2005Winner.html) | 2005 | [observed] S | |
| O2 | GitHub user records of `jjhforrest` and `johnjforrest` | fetched 2026-11-05 | metadata | |
| L1 | Local `publications/publications.md` (OpenAlex A5061258306) | 2026-11-05 | metadata | |

M1 (Crossref, Unpaywall and Semantic Scholar metadata) and the three sources not reached (N1–N3) are listed under Sources and Gaps.

---

## 0. Claims repeated three or more times (the real beliefs)

The counts are approximate. Where a count says "comments", it is a regex count over the comment bodies, with code blocks and quoted e-mail replies removed.

| # | Claim (faithful paraphrase) | Count | Where and when | Voice |
|---|---|---|---|---|
| R1 | Diagnose only on a concrete failing case. Ask for the model or driver, reproduce it with the stand-alone executable, and say so plainly when it will not fail. (general) | 33 comments say he is unable to, or could not, reproduce the fault (2018–2025). He asks for the model or an example ≥8 times: 2017, 2018, 2019 ×2, 2021, 2022, 2024, 2025. | G1, G2 | [stated] |
| R2 | When an LP or MIP answer looks wrong, suspect scaling and tolerances first. (LP+MIP) | "tolerance" in 38 comments and "scal…" in 24 (2019–2026); also code help texts from 2003 and 2006 | G1, C3, C4 | [stated] |
| R3 | Locate a fault by switching components off one at a time: preprocessing, cuts, heuristics, scaling, presolve, perturbation. (MIP mostly) | "-preprocess off" in 11 comments (2020–2026); "one by one" (2025); "set off then add one by one" (2006 deck) | G1, G2, T1 | [stated] |
| R4 | A fix is acceptable when it "can do no harm", even if a better fix may exist. (general) | 9 comments (2022–2026), plus the Bonmin thread (2023) | G1 | [stated] |
| R5 | Real-world problems are the yardstick. Artificial, random or perverse instances count for less. (general) | ≥9 statements, 2021–2025, plus a 2025 code comment | G1, G2 | [stated] |
| R6 | Keep new ideas behind compile-time switches or off-by-default options for a long time. Change "stable" only to fix bugs. (general) | 2005, 2008, 2020, 2022 ×3, 2023, 2024, 2026 | C4, C6, G1, G2 | [stated] |
| R7 | Say where his own expertise stops (interior point, interfaces, other people's cut generators) and hand over to people who know. (general) | 21 comments by regex (2019–2025), plus code notes 2003 and 2022 | C2, G1, G2 | [stated] |
| R8 | Admit his own mistakes in public, at once. (general) | 19 comments (2019–2026) | G1 | [stated] |
| R9 | Sprint (sifting) is for long, thin problems such as aircrew scheduling: few rows, an enormous number of similar columns. (LP) | 2003 ×3 (ClpSolve.cpp, examples/sprint.cpp, help text); 1998 (joint); 2024 ×2 | C2, C3, P1, G1 | [stated] + [stated-joint] |
| R10 | Teach and reproduce with small example drivers kept in `examples/`. (general) | ≥8: 2002, 2005, 2006, 2020, 2021, 2022 ×3, 2023 ×2, 2024 | C2, P2, G1, G2 | [stated] / [stated-joint] |
| R11 | Start from the defaults, read the log, and only then tune. (MIP mostly) | 2006 (help text), 2006 (deck), 2020, 2022 ×2 | C4, T1, G2 | [stated] |
| R12 | In MIP, good solutions found early matter. Heuristics, and diversity among them, are how you get them. (MIP) | 1974 (joint), 2005 (joint), 2006, 2022 ×2, 2025 | P5, P2, C4, G1, G2 | mixed |
| R13 | Triage by worth: lots of work for a rare case is not done. (general) | 17 comments (2019–2026) | G1, G2 | [stated] |
| R14 | Logs are diagnostic instruments. Correct output matters more than pretty output, and the state before any iterations matters most. (general) | 2006, 2019–2023 (log levels), 2026 ×4 | C4, G1, G2 | [stated] |

---

## B. Findings by the seven layers (framework §一)

### Layer 1: Research taste (what is worth doing, what counts as good)

**T1. Real problems are the yardstick; random or contrived instances prove little.** [stated] P, 2021–2025 (R5).
- On a GPU simplex paper (Clp Discussion #210, 2021-10-19):
  - "The key is "non-sparse" - 99% of problems solved by simplex are sparse."
  - "Also I suspect that few LP problems modelling a real world situtaion would be classified as "randomly generated"."
  - "I do not think it worth pursuing - others may."
  - "What are the statistics for the problems you are interested in solving?"
- Defaults follow what real models have: "Very few real world problems have all lower bounds infinite, but many do have zero lower bound and infinite upper bound - so it makes sense as a default if no array was given." (Clp Discussion #202, 2021-08-31)
- He discounts contrived reports:
  - "and the problem does seem to be a trifle artificial." (Clp#188, 2021-04-23)
  - "but it almost looks as if you are trying to break the code." (Clp#245, 2022-11-01)
  - "No sensible user would use that combination." (Cbc#704, 2025-04-17)
- He ranks bugs by real impact:
  - "It is a minor bug and won't affect any real application." (CoinUtils#206, 2023-04-02)
  - "My first fix tidied lower bounds to -1.0e14 - which is good enough for most real world problems!" (Cbc#463, 2021-12-20)
- A code comment he quotes in Cbc#753 (2025-11-16): "Infeasible - but most real problems are not infeasible - so try simpler preprocessing which is less affected by tolerance issues".
- [observed] S, COIN-OR Cup 2005 (O1) on the same trait: "using difficult real-world problems to drive the development of software tools that have wide applicability".

**T2. Sparsity and the memory hierarchy decide simplex speed.** [stated] P, 2002–2021. (LP)
- "The code is designed to take advantage of sparsity so arrays are seldom zeroed out from scratch or gone over in their entirety." (C1, ClpSimplexDual.cpp and ClpSimplexPrimal.cpp notes, 2002-07-30)
- "I think the use of templates was a mistake as I don't think inline generic code can take as much advantage of parallelism or machine architectures or memory hierarchies." (C2, ClpHelperFunctions.hpp, signed "Note (JJF)", introduced 2003-12-02)
- The version log for 1.00.02 records that he "redid createRim to try and improve cache characteristics" (C2, ClpMain.cpp, entry of 21 March 2005).
- "On modern computers in the simplex method, the main problem is random accessing data in level 1, 2, 3 cache and memory, so I would think that any cpu/gpu performance gains would be limited (but still possibly worthwhile)." (Clp Discussion #210, 2021-10-19)
- CoinFactorization.hpp (C5) lists what he took out and why it could come back:
  - "I have also put in handling for hyper-sparsity. I have taken out all outer loop unrolling, dense matrix handling and most of the book-keeping for slacks."
  - "Also I always use FTRAN approach to updating even if factorization fairly dense. All these could improve performance."

**T3. Correctness comes before speed, and before polish.** [stated] P, 2018–2026.
- "I have fixed - even if it means code is nanoseconds slower." (Clp#91, 2018-01-29)
- "There may be a better way of fixing but the following is safe/simple and should not make any real difference to speed." (Cbc#518, 2022-07-13)
- "I may be old fashioned but I think that correct output is more important than pretty output." (Cbc Discussion #775, 2026-05-16)
- "Fine - I don't mind clunky." (Cbc#807, 2026-10-20)
- The opposite pull is also stated. Of a fix that a user proposed for a bug he could not reproduce, he wrote that it "slows code down considerably" (Clp.old#40, 2018-11-12).

**T4. Modest names for his own ideas; the cleverness is in the engineering.** [stated] P, 2002–2003. (LP)
- Idiot crash (C2, Idiot.hpp, introduced 2002-11-25):
  - "This class implements a very silly algorithm. It has no merit apart from the fact that it gets an approximate solution to some classes of problems."
  - "It can also be used as a "crash" to get a problem started. This is probably its most useful function. It is based on the idea that algorithms with terrible convergence properties may be okay at first. Throw in some random dubious tricks and the resulting code may be worth keeping as long as you don't look at it."
- Primal design (C1, 2002): "In this version I have tried to be clever in a stupid way."
- Sprint (C2, ClpSolve.cpp, 2003-07-18): "This driver implements what I called Sprint when I introduced the idea many years ago. Cplex calls it "sifting" which I think is just as silly. When I thought of this trivial idea it reminded me of an LP code of the 60's called sprint".
- [inferred] The self-deprecation sits on a firm, repeated taste for what works on real models (T1, R9). The skill should not read the jokes as low confidence.

**T5. Elegance is welcome, but it is not the criterion.** [stated] P, 2002–2023.
- "I blame some of the coding peculiarities on the history of the code but mostly it is just because I can't do elegant code (or useful comments)." (C5, CoinFactorization.hpp, in CoinUtils since 2002)
- On indicator constraints (MIP): "A SOS approach has a certain elegance, but is weaker" (Cbc#572, 2023-02-15).
- "This (and .cpp) should be copied so that it is the same in Cbc/Test and Clp/Test. I know this is not elegant but it seems simplest." (C2, CbcOrClpParam.hpp, 2004-11-16)
- "Will see how easy it is to fix in a reasonably elegant way." (CoinUtils#144, 2021-02-17)

**T6. How he judges other people's methods and claims.** [stated] P, 2021–2025.
- On the literature: "I searched on "dual pivoting algorithms in simplex method" and was not impressed." (Clp#262, 2023-03-28)
- He grants superiority where he sees it: "Also a way of using Scip's preprocessing instead of CglPreprocess as Scip seems superior." (Cbc Discussion #573, 2023-02-21)
- He compares across solvers only after aligning the stopping rules:
  - Gurobi's default optimality tolerance of 1.0e-4 "seems quite high" (Cbc#481, 2022-02-06).
  - "the HiGHS "optimal" is 6000 worse than the one obtained by Cbc - due to using 0.01 as gap." (Cbc#703, 2025-04-17)
- (MIP) A powerful old idea is still powerful: Linked Ordered Sets are "a powerful idea which is a generalization of Special Ordered Sets" (Cbc#297, 2020-04-14).

### Layer 2: Problem choice (where problems come from; why now; when to stop)

**P1. Problems come from customers' models and users' reports.** [stated] P / [stated-joint].
- (MIP) Lot-sizing was "Done for IBM Microelectronics", "Using OSL – clumsily", and it "Influenced design of Cbc branching" (T1, slides 23–24, 2006).
- (LP) Sprint "worked very well on aircrew scheduling problems where there were very large numbers of columns all with the same flavor" (C2, 2003). Also: "The method was invented for airline problems where you "only" have 1000 constraints but an enormous number of variables." (Cbc#661, 2024-08-01)
- [stated-joint] The UMPIRE paper sorts methods by the problems met in practice: "We have found that the nontrivial integer programming problems we encounter tend to fall into two classes." (P5, Management Science 20(5), 1974, abstract)
- [stated-joint] The 2006 Interfaces paper: "We designed three heuristics, driven by practical applications, for capturing the discrete aspects of the MIP." (P5, abstract)
- [stated-joint] The 2006 IJOC paper is "Motivated by a real application from the steel industry" (P5, abstract).
- [stated] Users drive the code: "People from all around the world are already helping. There are probably ten people who do not always post to the discussion mail list but are constantly “improving” the code by demanding performance or bug fixes or enhancements." (P2, Cbc FAQ, JF 04/01/05)

**P2. Triage by worth.** [stated] P, 2019–2026 (R13).
- "It would be a lot of work to fix this and I don't think it worth it." (CoinUtils#94, 2019-03-22)
- "The code could be changed to make sure it tries just minimizing sum of infeasibilities, but I am not sure it is worth the effort." (Clp#188, 2021-04-23)
- Indicators in MPS: "Would be a lot of work - and rarely used." (CoinUtils#197, 2022-09-05)
- "Very slow reading .lp file - but I am not fixing that." (Cbc#717, 2025-05-23)
- "I am not going to bother to fix this. The OSL factorization predates Coin." (Cbc#719, 2025-05-23)

**P3. "Why now": an old idea is revisited when the context changes.** [stated] P, 2004–2026. (MIP mostly)
- Gomory cuts: "The original cuts - beware of imitations! Having gone out of favor, they are now more fashionable as LP solvers are more robust and they interact well with other cuts." (C4, help text, 2006-02-20 version; first seen 2004-11-16)
- "Semi-continuous variables were invented in the 1970's before cuts were used in integer programming. Now it may be better to use 0-1 variables (although this is problem dependent), even though the problem will be larger." (Clp#165, 2020-11-23)
- "Hopefully fixed. I should look more into those ideas from fifty years ago." (Cbc#784, 2026-06-25)
- A licence change opened a door: SCIP moving to Apache 2 "make it's use much more attractive in Coin. … I think this could be important." (Cbc Discussion #573, 2023-02-20)

**P4. Directions he himself calls failed, unfinished or abandoned.** Recorded because the framework asks for failures.
- (LP) Piecewise-linear reformulation: "I did some work on this many years ago on "grade" problems, but while it improved primal interior point algorithms were much better for that particular problem." (C2, ClpNonLinearCost.hpp, 2002)
- (LP) Aboca: "The Abc versions were a partially successful attempt to parallelize the simplex method which were implemented more than 10 years ago for a conference and not kept up to date" (Clp#262, 2023-03-28).
- (LP) Interior point and quadratic:
  - "It is rather basic as Interior point is not my speciality" (C2, ClpPredictorCorrector.hpp, 2003-12-02).
  - "Looking at comments in barrier code, quadratic barrier seems a work in progress (or a mess to put it another way)." (Clp#274, 2023-08-03)
- (MIP) Interpolation and column generation in OsiSolverLink: "So it is possible that it is a half finished project." (Cbc#297, 2020-04-15)
- (MIP) "It does look as if local tree search is broken. … I have tried some simple fixes, but it may need rethinking." (Cbc#520, 2022-07-19)
- (MIP) Pivot-and-Fix "would imply that this is not finished code" (Cbc Discussion #465, 2022-01-18).
- (MIP) "CglAllDifferent which does column fixing (too slowly)" (C6, CoinSolve.cpp version log, Nov 2005).
- (MIP) His own preprocessing "improvement": "I have taken out an "improvement" to preprocessing until I fix problem." (Cbc#741, 2025-08-12)
- (LP) "OsiClpSolverInterface::crossover which is not called from anywhere and was probably experimental." (Clp#184, 2021-04-07)

### Layer 3: Idea generation

**I1. Build on his own earlier codes, and learn from what he overdid there.** [stated] P, 2002–2003. (LP)
- In the Clp first commit (C1, 2002-07-30):
  - "OSL did not have a phase 1/phase 2 approach but instead effectively put fake bounds on variables and this is the approach here, although I had hoped to make it cleaner."
  - "At present I am using the modification of costs which I put in OSL and which was extended by Gill et al. I am still not sure of the exact details."
  - "At present we never check we are going forwards. I overdid that in OSL so will try and make a last resort."
- In the 2003 help text (C3): "OSL had a heuristic to adjust bounds, maybe we need that here."
- [inferred] These are his own statements about parts of OSL: the cost modification and the forward-progress checks. They are not OSL code.

**I2. An old code's tactic, transplanted when memory and models change: Sprint.** [stated] P (LP)
- "it reminded me of an LP code of the 60's called sprint which after every factorization took a subset of the matrix into memory (all 64K words!) and then iterated very fast on that subset. On the problems of those days it did not work very well, but it worked very well on aircrew scheduling problems" (C2, ClpSolve.cpp and examples/sprint.cpp, 2003).
- In the 2003 help text (C3) he wrote: "I introduced the idea as 'Sprint' after an LP code of that name of the 60's which tried the same tactic (not totally successfully)."
- The current wording in ClpParameters.cpp is in the third person ("introduced by J. Forrest"). It entered in Ralphs' parameter-move commit `b60048ac` of 2020-11-16.
- "The idea works best if you can get feasible easily. To make it more general we can add in costed slacks" (C2, 2003).
- [stated-joint] P1 (1998): "John Forrest[16] introduced the so-called Sprint method", citing his ORSA/TIMS talk of October 1989.

**I3. Start with a crude method; quick hacks and play are a legitimate source of ideas.** [stated] P.
- (LP) Idiot: "algorithms with terrible convergence properties may be okay at first" (C2, 2002).
- (MIP) mipStart: "I have coded (but not yet completely tested) a hack for mipStart. … Not quite working as I expected/hoped but getting some interesting results." (Cbc#215, 2019-04-16)
- (MIP) Diversity: "Starting from a different optimal basis can make a large difference to heuristics. … It is an interesting exercise, even when the extra effort does not pay off." (Cbc Discussion #524, 2022-07-22)
- (MIP) A "stupid" start: the best run came from "the "stupid" option of solving the problem without any objective … So it looks as if just having immediate solutions for the heuristics to use helps a lot on this problem." (Cbc#494, 2022-04-22)
- CoinModel named values: "I have no idea whether that could be useful but I thought it might be fun." (C5, CoinModel.hpp, 2005-02-08)

**I4. Mine the by-products of a heuristic run.** [stated, attribution inferred] P, from the feasibility-pump notes in the CBC guide (P2; converted from the Trac wiki in 2019; first-person voice). Attribution: he is the main committer of CbcHeuristicFPump.cpp (71 of its 106 commits on Cbc master are by "John Forrest", plus 4 by `jjhforrest`). (MIP)
- "So, how long do you try? If you get a solution, can you get a better one? Even if you fail to get a solution, can you get any benefit?"
- "By continually changing the objective, you are making the solution go all over the place but there will be variables which despite all this remain fixed at a value. Maybe if you fix these variables and preprocess the resulting problem you will get a much smaller problem on which it will be worth doing a few nodes of branch and cut."
- The same pattern in the 2006 deck: when there are two or more solutions, CombineSolutions takes their union, preprocesses, and runs for 200 nodes (T1, slide 17; paraphrase).

**I5. Reformulation as an idea source; compactness is not the goal.** [stated] P. (MIP)
- "I think it sensible to try and get a simple formulation working" (Cbc Discussion #516, 2022-12-24).
- On sudoku timings of three formulations: "As you can see the lotsizing version is as compact as possible - but not necessarily best." (same thread)
- "Reformulate – e.g. More integers" (T1, slide 21, 2006).
- On indicators: "I would think that the big M approach is slightly better than the SOS approach, especially if the big M is as tight as possible." (Cbc#572, 2023-02-15)
- [stated-joint] "Column generation can lead to much tighter better formulations e.g. Mkc problem" (T1, slide 28, 2006). The IJOC 2006 abstract (P5): "Solving mkc to optimality took less time than it takes to solve the LP relaxation of the original formulation."

### Layer 4: Experiments and execution (the largest layer)

**E1. Reproduce first, on the simplest possible carrier.** [stated] P, 2017–2026 (R1, R10). (general)
- "If you have issues, I may be able to help if given an example that fails." (CoinUtils#90, 2017-11-20)
- "Test should not be changed. Should be trapped earlier in code - so for input lp it would be. Need example." (Clp.old#22, 2018-11-12)
- "The best way is to put a modified driver into the examples directory and compile with make DRIVER=stopafter." (Cbc#416, 2021-06-22)
- "of course it is much easier to debug a problem of this size." (Cbc#738, 2025-08-06, on a tiny model)
- He makes small cases himself: "I saved model just before problems - saved as onopt_83.mps" (Cbc#769, 2026-02-27).
- He keeps a test set out of instances: "Sometimes I use a miplib example and fix a few variables to make it easier." (Cbc Discussion #558, 2022-10-25)

**E2. His stated diagnostic ladder for a wrong or slow LP/MIP result.** [stated] P (R2, R3). [inferred] The order below is assembled from the quotes, each of which is his.
1. Is it scaling or tolerance?
   - "Should not happen. Is your problem badly scaled?" (Clp#125, 2019-12-25)
   - "A scaling issue - 5.55...e-17 is below standard zero tolerance." (Clp#217, 2021-12-22)
   - He showed element-size histograms to users (Cbc#338, 2020-09-24).
2. Switch components off.
   - "To narrow the problem down - a) If you add -preprocess off does it work?" (Cbc#282, 2020-08-14)
   - "cbc model.lp -duals -cgraph off -cuts off -preprocess off -solve solves it in a few minutes!" (Cbc#305, 2020-05-27)
3. Fix the integers to the known solution and check: "try fixing variables to known solution and check for mistakes." (Cbc#282, 2020-08-14). Also: "If you fix the integer variables to those values and solve as an LP" (Cbc#697, 2025-03-28).
4. Use a known good solution as a debug oracle against invalid cuts.
   - "If you have a version of cbc which gets correct result - run it with -debug create and then run bad version with -debug debug.file. That might give a clue as to what is wrong." (Cbc#668, 2025-02-10)
   - "Using the optimal solution as debug input, I reduced the number of cut generators one by one." (Cbc Discussion #756, 2025-12-15)
   - Already in the 2006 deck: "Debug – mainly to track down bugs especially in cut generators", with the caveat "Can give false reading on good run (due to strong branching or heuristic)" (T1, slide 20).
5. Compare versions, builds and other solvers.
   - "Unable to reproduce error on 2.10.8. Have built it various ways" (Cbc#518, 2022-07-13)
   - "Cbc master gives same solution value as scip and gurobi, which shows that this is a borderline case." (Cbc#697, 2025-03-28)
6. Profile before guessing.
   - "b) profile a run and see where it is spending time." (Clp Discussion #227, 2022-02-11)
   - "Profiling Cbc I notice a large number of "virtual thunks" to OsiClp." (Cbc Discussion #735, 2025-07-24)

**E3. Stress the code with a test set and with deliberate perturbation.** [stated] P, 2002–2026. (LP and MIP)
- First Clp README (C1, 2002-07-30): "If you want to stress the code you can set various stuff e.g. dantzig pricing and then go into netlib testing. I do not guarantee that it will solve all netlib if you get too creative."
- `netlibTune` help (C2, introduced 2005-04-08): "I know this is cheating but it also stresses the code better by doing a mixture of stuff. The best algorithm was chosen on a Linux ThinkPad using native cholesky with University of Florida ordering."
- Differential testing against OSL (C2, examples/ekk.cpp, 2002-10-10): calls to OSL inside complex algorithms "could easily be swapped for Clp code. This was to stress test Clp (and Osl :-))."
- MIP unit test: "There are ILP's in miplib3 which are tested." (Clp#299, 2024-07-23). Users' sets become his: "I have a directory ~/cullmann with files and a file testset in that directory" (Cbc#668, 2024-08-28).
- A fix must survive a harder variant. After a tolerance retry worked: "However if I change the coefficient values to 1.0e7 that fails." (Cbc#543, 2022-09-22)
- "While stressing the code on master branch, I managed to get that assert. … I will investigate this further before modifying stable code." (Cbc#545, 2022-09-28)

**E4. Experimental changes stay behind switches, sometimes for years.** [stated] P, 2005–2026 (R6). (general)
- "In general, what I do (too extensively) is have a lot of conditional compilation for a long time." (Cgl Discussion #80, 2022-06-28)
- "Code put in master - switched off unless -DFIXED.... in build. May ask you to test some dubious improvements" (Cgl#81, 2022-08-16). The same day he asked whether to "allow curious users to use -DFIXED_BOTH_WAYS=1 in build".
- The `-experiment` help (C4, 2008-07-17): "Defines how adventurous you want to be in using new ideas. 0 then no new ideas, 1 fairly sensible, 2 a bit dubious, 3 you are on your own!"
- The Cbc version log (C6, 2005-11-16): "This is to stop me (JJF) messing about too much. Tuning changes should be noted here. The testing next version may be activated by CBC_NEXT_VERSION".
- The fathomMany work (C6, CbcGeneralDepth.cpp, 2024-06-25): "As checked in this time it should give identical results as before but now allows fathomMany in deterministic parallel. … Ideas which seem possible but changed current behavior will be found in areas marked with DETERMINISTIC_TUNING".
- "I am modifying stable - any modifications would be on -D........ in build" (Cbc#837, 2026-10-28).
- On an old guard he found: "I presume that whoever wrote the code (which might be me years ago) was not sure if the code included by the ifdef was correct and did not want to create any bugs." (Cbc#332, 2020-09-08)

**E5. Asserts and debug builds are part of the method.** [stated] P, 2017–2026. (general)
- "On the whole extra asserts are good as no production code will trigger them." (Cgl Discussion #80, 2022-06-28)
- "I don't wish to lose some of that debugging code" (Clp#191, 2021-05-14).
- The trade-off of the heuristic layer: "Without the assert the code would not fail - the heuristic might provide a bad solution, but that would be thrown out on later checks." (Cbc#462, 2021-12-07)

**E6. Build and machine context are part of any timing.** [stated] P, 2021–2026. (general)
- "By default cbc picks up threaded blas which is not a good idea" (Cbc#462, 2022-02-04). This comes with a table of miplib3 timings under different builds on his laptop.
- "as tiny variations in compilation make the code take a slightly different path." (Cbc#563, 2022-11-14)
- "With multiple threads Cbc is not deterministic which makes it a bit more difficult to debug (it can be made deterministic by -threads 112 - and that also seems okay - but not as efficient)." (Cbc#714, 2025-05-12)
- Measuring a change on a set, not one run (Cbc#774, 2026-04-01): "The changes to time measurement and limit have made the code less efficient. But only when time mode is default of elapsed!" He then reports test-set user and system times.

**E7. LP craft he states (advice to users and design rationale).** (LP)
- *Single-phase dual with fake bounds* [stated] P (C3, 2003): "If the gap between the upper and lower bounds of a variable is more than the value of dualBound Clp introduces fake bounds so that it can make the problem dual feasible. This has the same effect as a composite objective function in the primal algorithm."
- *Bound flipping in the ratio test, and the hard part* [stated] P (C1, 2002): "C) Sounds easy, but this is hardest part of algorithm." "These mini iterations can increase speed by orders of magnitude but we may need to go to more of a bucket choice of variable rather than looking at them one by one (for speed)."
- *Pricing* [stated] P:
  - (C1, 2002) "For difficult problems steepest edge is preferred while for very easy (large) problems we will need partial scan."
  - (C3, 2003) "The Dantzig method is implemented to show a simple method but its use is deprecated. Exact devex is the method of choice".
  - [stated-joint] (P3, guide) The pivot choice "is probably the most important factor in determining the number of iterations it will take to solve a problem."
- *Perturbation* [stated] P (C3, 2003): "However large problems and especially ones with unit elements and unit rhs or costs benefit from perturbation. Normally Clp tries to be intelligent, but you can switch this off."
- *Crash* [stated] P (C3, 2003): "On the whole dual seems to be better without it and there alernative types of 'crash' for primal e.g. 'idiot' or 'sprint'." Idiot (C3, 2003): "It works best on problems with unit elements and rhs but will do something to any model. It should only be used before primal."
- *Presolve* [stated] P (C3, 2003): "For the initial solve of any problem this is worth doing unless you know that it will have no effect."
- *Tolerance trick* [stated] P (C4, 2006-02-20): "One method which can be faster is to use a large tolerance e.g. 1.0e-4 and dual and then clean up problem using primal and the correct tolerance (remembering to switch off presolve for this final short clean up phase)."
- *Primal for proving infeasibility* [stated] P: "But the primal algorithm is better than the dual algorithm at proving a problem is infeasible" (Cbc#381, 2022-03-25).
- *Defaults chosen for the user's next question* [stated] P: "Normally the user wants to find out why the problem is infeasible - so the default action for Clp is to solve it without presolve so the user can get a detailed solution." (Cbc#381, 2021-04-07)
- *Model input* [stated] P:
  - "I would always use loadProblem. It is most efficient if all data is passed in at one go as then all arrays are setup once with correct size." (Clp#178, 2021-03-13)
  - addRows.cpp exists "just to explain why it is not a good idea to add one row at a time for many rows." (Cbc#301, 2020-05-02)
- *Warm starts* [stated] P:
  - "To do a warm start you need to set structurals to values. Getting the correct basis is also important but does not have to be accurate." (Clp#132, 2024-05-24)
  - On repeated solves: "maybe solve those from all slack - if number of iterations does not go up much then will be faster due to sparser factorization." (Clp Discussion #227, 2022-02-11)
- *Modelling advice* [stated] P: "However I would suggest you consider modifying your objective function." The same comment (Cbc#286, 2020-02-20) reports that scaling 1.0e15/1.0e20 costs down cut the iterations from about 50K to 3K.
- *Clp as a branch-and-bound engine* [stated] P: "By default Clp is not very interested in solution on max iterations. For strong branching it needs objective which it can get easily without bothering about scaling etc." (Clp#291, 2024-03-29)

**E8. MIP craft he states (tuning advice and design rationale).** (MIP)
- *Tuning order* [stated] P, branchAndCut help (C4, commit `d567df54`, 2006-02-21):
  - "This does branch and cut. There are many parameters which can affect the performance. First just try with default settings and look carefully at the log file. Did cuts help? Did they take too long? Look at output to see which cuts were effective and then do some tuning."
  - "If pre-processing reduced the size of the problem or strengthened many coefficients then it is probably wise to leave it on. Switch off heuristics which did not provide solutions. The other major area to look at is the search. Hopefully good solutions were obtained fairly early in the search so the important point is to select the best variable to branch on. See whether strong branching did a good job - or did it just take a lot of iterations. Adjust the strongBranching and trustPseudoCosts parameters."
- *Same advice, slide form* [stated] P (T1, slide 21, 2006): cuts "Try off or just at root (more nodes but may be faster)"; strong branching is a "Weak point of Cbc", sometimes essential, sometimes too much effort, "try priorities"; "Reformulate – e.g. More integers".
- *Cuts at the root* [stated] P (P2, JF 06/15/06): cut generators can be run "only at root node (which is probably best default)".
- *Do not be clever early* [stated] P: "but I would not try to be too clever at first. It is probably better to use mipstart than use the solution field." (Cbc Discussion #350, 2020-12-06)
- *Early good solutions* (R12):
  - [stated-joint] UMPIRE 1974 abstract (P5): “priorities,” the “best projection criterion” and “pseudo-costs” are named as the most important devices, and for the second problem class "it is important to reach a good solution quickly to limit the search."
  - [stated-joint] P2 (2005): "In practice, it is very useful to get a good solution reasonably fast. Any MIP-feasible solution produces an upper bound, and a good bound will greatly reduce the run time."
  - [stated] (Cbc#729, 2025-07-08): "It can help to run the root heuristics and cuts several times with slightly different starting points."
- *Integer slacks* [stated] P: "This can improve search by giving extra flexibility as to where to branch. But for heuristics and especially the feasibility pump, this is probably not a good idea." (Cbc#219, 2019-04-27)
- *Branching asymmetry (crew scheduling)* [stated-joint] P2 (2005): "Branching a variable to 1 is very powerful as it fixes many other variables to zero, but branching to zero is very weak as thousands of variables can increase from zero." Hence follow-on branching. [stated-joint] P1 (1998): "the column generation phase will still consider the original set of flights, so it is possible to recover from a bad choice."
- *Preprocessing is about optimal solutions* [stated] P:
  - "The point of preprocessing is to tighten and reduce the model in order to get an optimal solution. This can cut off non-optimal solutions." (Cbc#282, 2020-08-17)
  - "preprocessing does not care about LP optimality - just wants a method of getting correct integral values on post processing." (Cgl Discussion #80, 2022-06-28)
- *Cuts can be optimality cuts* [stated] P: "A generated cut is not just a feasibility cut, but is an optimality cut." (Cgl Discussion #80, 2022-06-20)
- *Partial trust in quick solves* [stated] P: a strong-branching solve stopped on iterations "means the code will take some notice of the result, but will not totally trust it e.g. for fixing variables." (Cbc#545, 2022-09-28)
- *Canonical direction* [stated] P: "BUT bugs kept creeping in for maximisation problems, so it was decided to flip the objective at the start of branch and bound and then back at end." (Cbc#519, 2022-07-15)
- *Node choice* [stated] P: "depth 1 (which is my preferred choice) tries to use Clp as efficiently as possible." (Cbc#710, 2025-04-24)

### Layer 5: Judging results (when to believe a result, when to stop)

**J1. A borderline answer is not automatically a bug.** [stated] P, 2020–2025. (MIP+LP)
- "Thinking it over, there may be no bug anywhere." (Cbc#282, 2020-08-17). The day before, he had suspected clique strengthening; this revision shows him changing his own diagnosis.
- "Not a bug - more a feature of integer programming." He adds: "It is probably mainly the need to prove absolute optimality that make some runs take a long time." (Cbc#633, 2024-01-18)
- "Dealing with tolerances is tricky and this case was unlucky as about three computations went the wrong way." (Cbc#689, 2025-02-05)
- He states outright when he does not know which answer is right: "It looks as if it is feasible with tolerance 1.0e-5 - cbc says infeasible with 1.0e6. Also scaling on/off makes a difference. Not sure what to do." (Cbc#89, 2019-04-05)

**J2. MIP run-to-run variation is real; do not over-read one run.** [stated] P, 2022–2025.
- "So you could say you were lucky." "There are many heuristics used in Cbc and whether they get a solution depends on so many factors." "So even small changes in compiler options can make a difference." (Cbc#494, 2022-04-22)
- "All my runs are identical up to solution at 19 nodes, but then they get a solution at 32 nodes so take a different course." (Cbc#759, 2025-12-31)

**J3. The accept rule for a fix: safe, cautious, no harm.** [stated] P, 2022–2026 (R4).
- "A solution that can do no harm is to weaken the problem (just for CgTwomir)" (Cbc#562, 2022-11-13).
- "Hopefully fixed in stable by being a bit more cautious." (Cbc#452, 2021-11-20)
- "It is difficult fixing extreme tolerance problems, while keeping normal working of preprocessing - so I am only modifying code when preprocessing thinks infeasible." (Cbc#749, 2025-10-22)
- "One idea I tried was far far too complicated and would lead to other problems." (Cbc#752, 2025-10-25)
- "It does not make any difference on my test cases but I have fixed it in master." (Clp#312, 2025-07-08)

**J4. A fix must be tested before it reaches users.** [stated] P, 2020–2021.
- "When I have done more tests to see if I have broken anything, I will put changes into master (this involves changes to Cbc, CoinUtils, Osi and Cgl!)." (Clp#165, 2020-11-23)
- "It works with your example, but I need to do much more testing before I submit code." (Cbc#421, 2021-06-29)
- His self-reported lapses are under Contradictions K2.

**J5. Test-set coverage limits what a test shows.** [stated] P.
- "probing on your problems is more active than on my test set." (Cgl#81, 2022-08-16)
- On indicator code: "The code has never really been tested on real problems." (Cbc#572, 2023-02-15)

### Layer 6: Writing, talks and documentation

**W1. The code is the documentation; the manual defers to the header comments.** [stated-joint] P.
- P3 (CLP guide, 2004): "the comments in the Clp header files are the ultimate reference."
- P2 (CBC guide, 2005): "the comments in the Cbc header files are the ultimate reference."
- [stated] He keeps design notes at the top of the algorithm files (C1) and asks for comment on the design: "I would welcome suggestions for what should be in this and how it relates to OsiSolverInterface." (C2, ClpModel.hpp, 2002)

**W2. Candid and self-deprecating about documentation.** [stated] P, 2002–2025.
- "If you can see this you have the best there is:-)" (P2, Cbc FAQ, JF 04/01/05)
- "Even I have no clue what this does!" and "pumpTune - this is a very complex parameter as more and more was loaded onto it." (P2, feasibility-pump notes; attribution inferred, see I4)
- "There is not much documentation for the more exotic commands." (Cbc#633, 2024-01-19)
- Version log (C2): "Lots of changes but I got lazy" (2007-06-27). The entry "Lots done but I can't remember what!" arrived in Ladanyi's svn-migration commit of 2006-06-09, so it is not attributed by git.

**W3. Examples teach techniques, not speed records.** [stated-joint] / [stated].
- [stated-joint] P2 (2005): "the sample code is not guaranteed to be the fastest way to solve the problem. The main purpose of the example is to illustrate techniques."
- [stated] C2 (examples/ekk.cpp, 2002): "However they may be useful as sample code. Virtuous people would add return code checking."

**W4. Messages and logs are instruments; their design has principles.** [stated] P, 2002–2026 (R14).
- 2002 (C5, CoinMessageHandler.hpp): "I (jjf) am strongly in favo(u)r of language support for an open source project, but I have tried to make it as lightweight as possible".
- 2026 (Cbc Discussion #775): "Originally Coin messages were designed so that only values were passed in and the actual message could be in any language. This virtuous idea was subverted by messages such as CBC_GENERAL or CLP_GENERAL."
- Also in #775:
  - "It is very important to know the status before any iterations." (2026-05-15)
  - "I think we need to distinguish between normal runs and investigation runs." (2026-03-27)

**W5. Talks: short, humorous, historical.** [stated] P via secondary host (T2, 2010). Abstract of "One LP Code a Minute": "A short, content free, look back at LP codes which I have used, abused and written. Some attempt may be made to put the more successful codes in the context of the available computer architectures, but more emphasis will be on the codes which nobody else has heard of and which I have tried to forget. For example, hands up all those who have heard of Alligator?" The talk itself was not found (Gaps).

**W6. Publishing.** [stated] P (P2, JF 05/24/06): "I need to publish some more heuristic methods as I have several I use for my own work which at present are too problem specific." No other statement about how he writes papers was found (Gaps).

### Layer 7: Research organisation

**O1. Open source as the platform for collaboration.**
- [stated] P2 (Cbc FAQ, JF 06/03/06), on Cbc's origin: "When COIN-OR LP was being written, the Osi interface demanded an integer solver. An exception could have been thrown but anyone can write a branch and bound code in a day. With Strong Branching it was 460 lines of code, without 300 lines. Somehow the code kept growing and eventually it was moved it to its own project."
- [stated] T1 (2006, slide 3), the same story: "I bet myself I could code in a day – failed – took 10 hours".
- [stated-joint] P4 (2007): "The success of the project is facilitated by the fact that all essential components were available as open-source code, so that they could be changed (and changes could be contributed back to the project maintainers), and by the object-oriented design of the codes."
- [observed] O1 (2005): "Founding Benevolent Dictator of COIN-OR."

**O2. Release discipline: master for change, stable for fixes, time to settle.** [stated] P, 2005–2026 (R6).
- "I will try and remember not to put anything interesting into stable - just fixes." (Cbc#591, 2023-04-17)
- "There will be pauses after each "improvement" to make sure nothing has been broken." (Cbc Discussion #735, 2025-07-24)
- In 2026, on the fast-moving "next" branch:
  - "I am worried about the speed with which all the changes are happening. … Are we getting much feedback from users (apart from claude)?" (Cbc#809, 2026-10-17)
  - "Then we could live with that for a few months to let it settle down" (Cbc Discussion #775, 2026-05-23)

**O3. Boundaries of responsibility and deference to code owners.** [stated] P (R7).
- "I will not debug unless in Coin repository." (C2, ClpModel.hpp, introduced 2006-01-30, on applications that use Clp's unsafe short cuts)
- Interfaces are other people's:
  - "I am not an expert on C interface" (Cbc#202, 2019-03-10)
  - "I never use the C interface" (Cbc#497, 2022-05-03)
  - "I have not got the energy to dig into the Julia interfaces" (Cbc#301, 2020-05-02)
- Other authors' cut code:
  - "I never use the clique strengthening code - would be good if someone more knowledgeable could take a look." (Cbc#750 and #751, 2025-10-24)
  - "If the author of the changes can fix - then good." (Cbc#639, 2024-02-18)
- Interior point (LP): "It is rather basic as Interior point is not my speciality" (C2, 2003). "Not an expert in barrier or KKT methods" (Clp Discussion #246, 2022-11-01). [observed] S, P3 FAQ (DN 09/16/04): "the principal author, John Forrest, knows more about simplex algorithms than interior point algorithms".

**O4. Students and helpers.** [stated] P, 2022–2023.
- "What I would really like is for a student to dig into all this." (Cbc Discussion #573, 2023-02-21)
- "To encourage someone to play with the code, I put my attempt to use Scip in CbcGeneral.cpp." (2023-02-20). The code comment, introduced in a Forrest commit, reads "I have put Scip "interface" here to encourage modifying it" (C6).
- "Feel free to criticise and alter." (Cbc Discussion #513, 2022-06-16)
- No statement about supervising students was found. His papers show no students (L1; Gaps).

**O5. Resource context, stated by him.** [stated] P.
- "although with a small laptop, it may be difficult to see if it can solve problems with >2**31 elements." (Cbc#661, 2024-08-01)
- "Looking into it - stressing my small laptop." (Cbc#837, 2026-10-28)
- "Not having NVIDIA gpus, I may have a quick look at ZLUDA to see if there is any potential." (Clp Discussion #210, 2021)
- "I will think about this more when I am more in the mood (i.e. not having a pleasant evening with my family)." (Clp#358, 2026-10-23)
- 2006: "Using Cbc to solve subproblems took 150 minutes on my laptop – with tuning down to 50 minutes." (T1, slide 34)

**O6. Stance on AI-driven code changes (2026).** [stated] P.
- "The output from Cbc and Clp has developed over twenty years and is being totally rewritten by someone called copilot." (Cbc Discussion #775, 2026-05-16)
- "It is not easy to test code … I would like to help but my AI is not up to it." (Cbc Discussion #775, 2026-05-07)
- See also O2 ("apart from claude").

---

## C. Change over time (stated method by period)

- **1970s–1990s (Scicon, IBM):** no single-authored statement survives from this period. There are three kinds of evidence. First, co-authored abstracts and the 1998 chapter (P1, P5): problem classes from practice, priorities and pseudo-costs, good solutions early, Sprint for crew pairing. Second, his later recollections: of OSL (I1); of 1970s semi-continuous and lot-sizing variables (T1, slide 23); of the 1960s "sprint" code (I2). Third, others' credit [observed]: COIN Cup 2005 lists him as a developer of "Alligator, Umpire, Sciconic, MPSX370, OSL"; Jensen's INFORMS 2010 abstract says "John Forrest was the principle author of IBM's Optimization Subroutine Library."
- **2002–2009 (IBM Research, Clp and Cbc built):** design notes (C1, C2, C5), help texts (C3, C4), JF-signed FAQ answers (P2) and the 2006 deck (T1). The voice is design-oriented: OSL lessons, sparsity, modularity, stress tests, and defaults plus "tuning" text for users.
- **2017–2026 (retired volunteer, GitHub):** almost entirely diagnostic and maintenance voice (G1, G2). The method is stated through answers: reproduce, check scaling and tolerances, switch components off, use the debug oracle, apply a no-harm fix, master before stable. From 2025–26 he speaks increasingly about the pace of change and the quality of output, against AI-assisted rewrites.

---

## Contradictions (kept, not reconciled)

**K1. Flexibility and modularity versus speed, early versus late.**
- 2002: "reference would be faster using ClpSimplex's status_, but I prefer to keep modularity." (C2, ClpPrimalColumnSteepest.hpp)
- 2005 (JF): "Is CBC as fast as Cplex or Xpress? … No. However its design is much more flexible so advanced users will be able to tailor CBC to their needs."
- 2006 (JF): "It is not very fast out of the box, but is very flexible".
- Against this:
  - 2003: "I think the use of templates was a mistake" (generic code loses performance).
  - 2006 deck: "Some overhead due to being solver agnostic." and "OsiCbc – in a circular way – big mistake".
  - 2025: the "virtual thunks" to OsiClp are "an overhead and also may prevent the code being better optimized", so he starts "a slow journey" to remove them.
  - 2024: "If we had CBC_MUST_USE_CLP then one might be able to slowly make code marginally more efficient".

**K2. Stated test-before-commit rule versus self-reported lapses.** He states the rule (J4) and also reports lapses:
- "For some hours there was a bad bug in master simplex due to some changes. It did not show up initially on my tests" (Cbc#451, 2021-11-09)
- "The new coding triggered by #define FIXED_BOTH_WAYS was only tested on larger problems in optimized mode." (Cbc#479, 2022-01-30)
- "I am an idiot. Put in tiny change at end before commit." (Cbc#748, 2025-10-21)
- "Apologies - my stupidity. I totally forgot I had made a change a few weeks ago. The assert was to help me debug something else - and I forgot to take it out." (Cbc#759, 2026-01-04)

**K3. Semi-continuous and lot-sizing variables: first a design driver, then possibly better replaced by 0-1 variables, then worth revisiting.**
- 2006 (T1): lot-sizing "Influenced design of Cbc branching".
- 2020: "Now it may be better to use 0-1 variables (although this is problem dependent)".
- 2023: "semi-continuous variables are not much used".
- 2026: "I should look more into those ideas from fifty years ago."

**K4. Crash.**
- 2003 (C3): "On the whole dual seems to be better without it" (Clp's crash).
- 1998 (P1, joint): the volume-algorithm dual solution used "to crash the dual simplex is, on average, nine times faster than the dual simplex algorithm" on crew-pairing LPs.
- The crashes and the problem classes differ. Both are kept.

**K5. Aboca: name and verdict.**
- Help text (2012-08-30): Aboca is "A Basic Optimization Code (Accelerated?)".
- Clp#262 (2023): "Abc was short for Aboca - "A Bit Of Clp Accelerated"". The same comment calls Abc "a partially successful attempt … not kept up to date".
- Yet on 2026-11-01 (Cbc#837): "Looking at various things - the answer may be as simple as abc."

**K6. Determinism.**
- 2021: "As parallel cbc is normally non-deterministic, this does not matter bug-wise as it just means cuts may or may not get generated (but they will be valid ones)." (Cgl#63)
- 2024: the fathomMany update is "all about" deterministic parallel (C6).
- 2025: non-determinism "makes it a bit more difficult to debug".
- He accepts non-determinism for validity but invests in determinism for debugging.

**K7. Comments as "the ultimate reference" versus "I can't do elegant code (or useful comments)".** The co-authored guides (P2, P3) make the header comments the final authority. His own 2002 note in CoinFactorization.hpp disclaims useful comments.

**K8. Pace of change.** [inferred] He applies restraint to himself ("This is to stop me (JJF) messing about too much", 2005) and asks it of others ("I am worried about the speed with which all the changes are happening", 2026). Yet his own comments report many quick fixes straight into master ("Should be fixed in master" and variants in dozens of comments), and in 2024 he wrote "I have many versions of master." Whether his practice matches his stated restraint is for agent 03.

---

## Gaps

- **No long-form statement of method.** No essay, interview, oral history, award speech or "how I work" talk was found. The INFORMS 2010 talk "One LP Code a Minute" and the panel "Self-documenting Code and Other 'Tricks' of the Trade" (Forrest with Lougee and Tomlin) are known only from program abstracts (T2). A WebSearch for the talk found nothing.
- **COIN-OR mailing lists (2002–2018) not reached.** `list.coin-or.org` refused connections on 2026-11-05 (curl and WebFetch: ECONNREFUSED). This is the main gap: his Q&A voice from 2002 to 2017 is visible only through code notes, help texts, the FAQ and one slide deck. Search-engine snippets point to two Clp-list posts; their titles, as the search results show them, are "[Clp] A Bit Of Clp Accelerated?" (Aug 2012, an Aboca talk at ISMP Berlin) and "[Clp] Abc vs Clp" (Nov 2014, advantage over Clp reportedly diminished). These are leads only, not read; their content is not used above.
- **Forrest and Tomlin's retrospective not read.** "Branch and bound, integer, and non-integer programming", Annals of Operations Research 149(1):81–87 (Crossref issue date 2006; volume 2007), DOI 10.1007/s10479-006-0112-x. It is the one semi-autobiographical text found. The IBM Research Report RC22890 copy (dominoweb.draco.res.ibm.com) timed out and was refused; the Springer page shows no abstract.
- **Paywalled full texts not read.** Only metadata, and the abstract where noted, were seen for:
  - Forrest & Tomlin 1972 (DOI 10.1007/bf01584548)
  - Forrest, Hirst & Tomlin 1974 (10.1287/mnsc.20.5.736; abstract read)
  - Beale & Forrest 1976 (10.1007/bf01580653)
  - Forrest & Tomlin 1990 (10.1007/bf02023049)
  - Forrest & Tomlin 1992, simplex (10.1147/sj.311.0011) and interior point (10.1147/sj.311.0026)
  - Forrest & Goldfarb 1992 (10.1007/bf01581089)
  - Dietrich & Forrest 2002 (10.1007/978-1-4684-9277-4_2)
  - Denton, Forrest & Milne 2006 (10.1287/inte.1060.0238; abstract read)
  - Forrest, Kalagnanam & Ladanyi 2006 (10.1287/ijoc.1040.0078; abstract read)
  - The TutORials version of the CBC User Guide (10.1287/educ.1053.0020): publisher PDF 301→403; the coin-or.org web version was read instead.
- **No talk recordings.** No video or subtitles, so no transcript was saved. The ISMP 2012 Aboca talk slides were not found.
- **Not harvested:** GitHub PR inline review comments. Only issue/PR conversation comments and Discussions were collected.
- **Supervision layer is nearly empty.** He has no known students. There are only invitations ("for a student to dig into all this"); nothing on how he would supervise.
- **Writing papers:** no statement on how he writes or structures papers.
- **Not used:** web.archive.org (WebFetch refuses it). fastercoin.com was not tried (parked domain per team.json).

---

## Implications for Phase 2 (for the synthesiser; all [inferred])

- **Most distinctive stated method: a model-first diagnostic ladder for LP/MIP solver faults.** Each rung is quoted above, mostly ≥3 times:
  1. reproduce with the stand-alone executable and an MPS file;
  2. scaling and tolerances;
  3. switch components off one at a time;
  4. fix integers at the known solution and solve the LP;
  5. debug-solution oracle against invalid cuts;
  6. compare builds, versions and other solvers;
  7. a "no harm" fix in master, with stable later and fixes only.
- **Stated LP engineering taste, usable as quick tests on a design:**
  - Does it exploit sparsity, and is it cache-aware?
  - Single-phase with fake bounds or a composite objective.
  - Bound flipping ("mini iterations") in the dual ratio test.
  - Steepest edge or exact devex by default.
  - Perturbation for unit-element problems.
  - Sprint for long-thin LPs; Idiot only as a primal crash.
  - Skepticism toward dense or random-instance speed-ups.
- **Stated MIP craft (MILP Team seat):**
  - Defaults first, then read the log.
  - Cuts at the root as the safe default.
  - Drop heuristics that find nothing.
  - Tune strong branching and trust.
  - Get good solutions early, with diversity across root passes.
  - Remember that preprocessing may cut off non-optimal solutions.
  - Reformulate (more integers; tight big-M before SOS for indicators; 0-1 instead of semi-continuous, problem-dependent).
- **Voice weighting:** single-author items are the code notes from 2002 to 2012, the help texts, the JF FAQ answers, the 2006 deck (third-party host) and G1/G2. Weigh them above the co-authored papers. The MIP items in Cbc are his voice only as labelled. OSL items are his recollection or others' credit, never code evidence.

---

## Sources

1. C1: Clp, first commit `b42534866981c7939cf699bbc719338c76ceda87`, John Forrest, 2002-07-30 (README, ClpSimplexDual.cpp, ClpSimplexPrimal.cpp, include/*.hpp). https://github.com/coin-or/Clp/commit/b42534866981c7939cf699bbc719338c76ceda87 (primary; read).
2. C2: Clp master at `874465237db8ad0cfeffb74119e7a1cd9b756164` (2026-11-02): src/ClpSimplex.hpp, ClpModel.hpp, ClpSimplexPrimal.hpp, ClpSimplexDual.hpp, ClpNonLinearCost.hpp, ClpPrimalColumnSteepest.hpp, ClpHelperFunctions.hpp, ClpPredictorCorrector.hpp, Idiot.hpp, CbcOrClpParam.hpp, ClpSolve.cpp, ClpMain.cpp, ClpParameters.cpp; examples/sprint.cpp, ekk.cpp, addRows.cpp. Each quoted sentence was dated by `git log -S` on a full clone. https://github.com/coin-or/Clp (primary; read).
3. C3: Clp `Test/ClpMain.cpp` at commit `6cd3154e` ("Still trying to go faster", John Forrest, 2003-10-08) and `d36b7058` (2003-10-02). https://github.com/coin-or/Clp (primary; read).
4. C4: `CbcOrClpParam.cpp` at Clp commits `2ea34581` (2006-02-20), `d567df54` (2006-02-21), the 2008-07-17 commit introducing `-experiment`, and the Forrest commits `960aa00b` (2005-04-08), `f5c0e386` (2004-10-22), `a405120c` (2005-04-04), `eb20ee6f` (2007-06-25), `07ede60c` (2009-07-25), `ac027b06` (2006-10-08), `1c055e3d` (2008-11-06), `983fba92` (2009-03-16). https://github.com/coin-or/Clp (primary; read).
5. C5: CoinUtils master at `231b801e` (2026-10-31): CoinFactorization.hpp, CoinFactorization3.cpp, CoinMessageHandler.hpp, CoinModel.hpp (bulk-merged by Ladanyi 2002-11-05; CoinModel note by Forrest 2005-02-08). https://github.com/coin-or/CoinUtils (primary; read).
6. C6: Cbc master at `001b861c` (2026-11-04): README.md, AUTHORS, src/CoinSolve.cpp (Forrest 2005-11-16), src/CbcSymmetry.cpp (Forrest 2014-07-16), src/CbcGeneralDepth.cpp (Forrest `9a2048ca`, 2024-06-25), src/CbcGeneral.cpp, doc/cbc-parameters.md. https://github.com/coin-or/Cbc (primary for his notes; README observed).
7. G1: 486 GitHub issue/PR comments by `jjhforrest`/`johnjforrest`, 2017-11-20 – 2026-11-01. Collected from the repository-level `issues/comments` listings of coin-or/Cbc, Clp, Clp.old, CoinUtils and Cgl (pages downloaded unauthenticated by research agent 03 in this run's scratch folder and re-filtered here), plus `issues/{n}/comments` for coin-or/Bonmin#31, SHOT#159, Osi#193 and scipopt/papilo#59, #62 (fetched here). Key comments are cited by repo#issue and date in the text; examples: https://github.com/coin-or/Cbc/issues/282#issuecomment-674743184 , https://github.com/coin-or/Clp/issues/262#issuecomment-1487041019 , https://github.com/coin-or/Cbc/pull/809#issuecomment-6235378489 (primary; read in full after stripping logs and code).
8. G2: 86 GitHub Discussions comments, 2020-12-06 – 2026-05-25, parsed from 36 threads (coin-or/Cbc 24, Clp 10, Cgl 2). GitHub's commenter filter lists 38 threads (also one more Cgl and one CoinUtils thread, which yielded no parsed comment). Public HTML pages fetched without login, e.g. https://github.com/coin-or/Cbc/discussions/775 , https://github.com/coin-or/Cgl/discussions/80 , https://github.com/coin-or/Clp/discussions/210 , https://github.com/coin-or/Cbc/discussions/735 , https://github.com/coin-or/Cbc/discussions/558 (primary; read in full).
9. P1: R. Anbil, J. J. Forrest, W. R. Pulleyblank, "Column generation and the airline crew pairing problem", Documenta Mathematica Extra Volume ICM 1998 III, 677–686, DOI 10.4171/dms/1-3/65. https://ems.press/books/dms/248/4854 (primary, joint; read in full).
10. P2: J. Forrest, R. Lougee-Heimer, CBC User's Guide, web version with FAQ (JF-signed answers 2005–06), feasibility-pump notes and revision history. https://www.coin-or.org/Cbc/ (intro, nodeselection, heuristics, branching, advanced, faq, revhist, moresamples). The book-chapter version is "CBC User Guide", INFORMS TutORials 2005, pp. 257–277, DOI 10.1287/educ.1053.0020 (not reached: 403) (primary, joint; web version read).
11. P3: J. Forrest, D. de la Nuez, R. Lougee-Heimer, CLP User's Guide (2004) and Clp FAQ (answers signed DN). https://www.coin-or.org/Clp/ , https://www.coin-or.org/Clp/faq.html (guide primary-joint; FAQ secondary/observed; read).
12. P4: P. Bonami, J. J. Forrest, J. Lee, A. Wächter, "Rapid Development of an Open-source Minlp Solver with COIN-OR", Optima 75, December 2007, pp. 1–4. https://mathopt.zib.de/Optima-Issues/optima75.pdf (primary, joint; read).
13. P5: Crossref records and abstracts for J. J. H. Forrest, J. P. H. Hirst, J. A. Tomlin, "Practical Solution of Large Mixed Integer Programming Problems with Umpire", Management Science 20(5):736–773, 1974, DOI 10.1287/mnsc.20.5.736; B. T. Denton, J. Forrest, R. J. Milne, "IBM Solves a Mixed-Integer Program to Optimize Its Semiconductor Supply Chain", Interfaces 36(5):386–399, 2006, DOI 10.1287/inte.1060.0238; J. J. H. Forrest, J. Kalagnanam, L. Ladanyi, "A Column-Generation Approach to the Multiple Knapsack Problem with Color Constraints", INFORMS Journal on Computing 18(1):129–134, 2006, DOI 10.1287/ijoc.1040.0078. https://api.crossref.org/works/ (primary, joint; abstracts only).
14. T1: J. Forrest, Coin Branch and Cut, a tutorial (title as the host extracts it: "Coin Branch and Cut A tutorial"), 18 July 2006, 35-page deck as rehosted at https://api.sambuz.com/doc/coin-branch-and-cut-a-tutorial-ppt-presentation-671391 (primary content via third-party host; read; provenance not confirmed beyond title, author and date).
15. T2: INFORMS Annual Meeting 2010 cluster "John Forrest-fest | COIN-OR 10th" (talk abstracts by Forrest, Tomlin, Jensen, Fasano; panel), as copied in J. Wang, "INFORMS 2010 - a COIN-OR double celebration!", blog post, 6 March 2011. https://jiadongwang.blogspot.com/2011/03/informs-2010-coin-or-double-celebration.html (his abstract primary via secondary host; others secondary).
16. T3: DIMACS Workshop on COIN-OR, 17–20 July 2006, program and abstracts. https://archive.dimacs.rutgers.edu/archive/Workshops/COIN/program.html , https://archive.dimacs.rutgers.edu/archive/Workshops/COIN/abstracts.html (secondary; read).
17. O1: COIN-OR Foundation, page "COIN-OR Cup 2005 Winners" (section on John J. H. Forrest). https://www.coin-or.org/coinCup/coinCup2005Winner.html (secondary; read).
18. O2: GitHub REST API user records for `jjhforrest` and `johnjforrest` (created_at), fetched 2026-11-05 (metadata).
19. L1: Local `references/sources/publications/publications.md` (OpenAlex author A5061258306, pulled 2026-11-05) (metadata; read).
20. M1: Crossref and Unpaywall metadata checks for the 13 DOIs cited here (none open access except the ICM chapter at ems.press), plus Semantic Scholar records (metadata; used only to verify titles, venues, years and pages).
21. N1: J. J. H. Forrest, J. A. Tomlin, "Branch and bound, integer, and non-integer programming", IBM Research Report RC22890 (report number and URL from a search result; date not verified), https://dominoweb.draco.res.ibm.com/reports/rc22890.pdf. Published in Annals of Operations Research 149(1):81–87, DOI 10.1007/s10479-006-0112-x. **Not reached:** connection timed out (curl) and refused (WebFetch). The Springer page showed no abstract.
22. N2: COIN-OR mailing-list archives, https://list.coin-or.org/pipermail/ (clp, cbc, coin-discuss). **Not reached:** ECONNREFUSED (curl and WebFetch), 2026-11-05.
23. N3: INFORMS PubsOnline, DOI 10.1287/educ.1053.0020. **Not reached:** HTTP 403 (page) and 301 to a denied PDF.

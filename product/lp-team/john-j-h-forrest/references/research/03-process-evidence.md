# John J. H. Forrest · 03 Process evidence (what he actually does)

- **Researcher**: John J. H. Forrest (name forms: John J. Forrest, J. J. H. Forrest, John Forrest; OpenAlex A5061258306; DBLP pid 08/3168). Living: inferred from account activity only (latest GitHub comment 2026-11-01, latest commit 2026-10-24).
- **Dimension**: nuwa research-craft Phase 1, research agent 03 of 06, process evidence: behaviour visible in code, commit history, issue tracker and experiment sections. Scope: LP simplex engineering, and (added 2026-11-05) his MIP craft (Cbc, and the earlier MIP codes as far as the record shows them).
- **Research date**: 2026-11-05
- **Sources consulted**: 40 entries, S1–S40 under "Sources": 24 primary, 16 secondary. 38 were reached; S33 and S35 were not. WebSearch calls used: 3 of 7.
- **Local corpus**: `references/sources/papers`, `talks`, `essays` and `software` held only `.gitkeep`. `publications/` holds the OpenAlex summary written by `scripts/fetch_publications.py`, which is a generated list, not user-supplied material. Nothing below is marked "from user-supplied material". `private/` was not opened.
- **Method**:
  1. Full git clones of coin-or/Clp (history from the 2002-07-30 first commit `b4253486`; HEAD `87446523`, 2026-11-02), coin-or/CoinUtils (from 2002-09-16) and coin-or/Cbc (from the 2004-10-29 import; HEAD `001b861c`, 2026-11-04). I used `git log` over all branches, counting distinct (author, date, subject) triples so that SVN-era branch copies are not double-counted. I also used `git log -S` to date comments, `--diff-filter=A` to find who created each file, and `git blame -w` for line shares. Blame gives the last person to touch a line, not its author; see §0.2.
  2. GitHub REST API, without login: all 3,930 conversation comments in Cbc, Clp, CoinUtils, Cgl and Clp.old (481 of them his); 5 more of his in Bonmin, SHOT, Osi and PaPILO; GitHub search (`commenter:`) for the 293 threads he joined; the two account profiles. I removed quoted e-mail text (lines starting with `>` and anything after "On … wrote:") before counting or quoting.
  3. Papers: the ICM 1998 chapter (full text), the Optima 75 Bonmin note (in part), and the public abstracts of four others. The rest are paywalled and were not read.
  4. Third-party accounts: Galabova & Hall (arXiv:1804.09172), Huangfu & Hall (MPC 2018), the COIN-OR INFORMS Cup 2005 page, the Clp FAQ (answers initialled "DN", 2004), the DIMACS 2006 programme and abstracts, and a third-party text mirror of his 2006 Cbc tutorial slides.
- **Tags**:
  - [stated]: his own words, including code comments, commit messages, help text, issue comments and co-authored text (marked "co-authored").
  - [practice]: what the code, history or experiment sections show he did.
  - [observed]: what others wrote about him.
  - [inferred]: my reading, with no source saying it.
  - Every item also says primary or secondary.
- **Quoting**: quotations are verbatim. Code comments are quoted as they stand at HEAD unless a date is given. Issue comments are cited as repo#issue and date (URLs under S5–S6). Longer passages, and all text from copyrighted papers, are paraphrased.
- **Identity caveat (read first)**: commit authorship appears under three identities:
  - "John Forrest" with a fastercoin.com address: 2002-07-30 to 2020-05-11.
  - "John Forrest" with a gmail address: 2020-05-12 to 2024-09.
  - "jjhforrest", same gmail address: 2024-11-01 onwards.

  The GitHub *accounts* have different dates (S7). `jjhforrest` was created 2014-03-31 and has commented since 2017-11-20. `johnjforrest` was created 2019-06-14 and has exactly one comment (Clp#138, 2020-03-21). One 2019 `jjhforrest` reply (Clp#103, 2019-04-10) was sent by e-mail, and the GitHub notification it quotes lists the fastercoin.com identity as a recipient (Cc). That ties the `jjhforrest` account to the 2002–2020 commit identity more strongly than the shared display name alone. No document states that link.
- **Count reconciliation**: the brief cites 461 comments. I found 486: Cbc 315, Clp 103 (one of them from `johnjforrest`), CoinUtils 28, Clp.old 21, Cgl 14, and 5 elsewhere. Cbc + Clp + CoinUtils + Cgl + Osi gives exactly 461, so the earlier count probably left out Clp.old, Bonmin, SHOT and PaPILO [inferred].

---

## 0. Era, resources and authorship (read first)

### 0.1 Era and resource context

| Period | Setting (as far as verified) | Compute, tools, team | Process evidence available |
|---|---|---|---|
| 1970s (Scicon period per the team.json hint; affiliation not re-verified) | UMPIRE (Forrest, Hirst, Tomlin, *Management Science* 1974); special ordered sets (Beale & Forrest, *Math. Programming* 1976) | not recoverable | Abstract of the 1974 paper only (S13). No code of his is visible. |
| c. 1980s–2000s, IBM Research, Yorktown Heights | OSL; co-authored papers with J. A. Tomlin (1990, 1992 ×2) and with D. Goldfarb (1992) | S/390 (1989 Sprint table); IBM 3090 vector and RISC System/6000 (per the 1992 abstract); RS6000/590 (1998 table) | ICM 1998 chapter (S24, read); abstracts (S9, S10, S13–S15). The OSL code is not visible; his own Clp notes name two OSL design choices as his (§0.2, §5.1). |
| 2002–c. 2009, IBM Research + COIN-OR | Sole author of Clp (2002); main early author of Cbc (2004–05); OSL factorization port (2009) | Linux and Windows/Visual C++ builds; a "Linux ThinkPad" (2005 help text, §1.3); IBM-internal "Burlington" models; airline and MIPLIB sets | Commits 2002–2009 (Clp 64–218 a year; Cbc 106–210 a year from 2005); design notes; version logs |
| c. 2010–2016 (left IBM; retirement date not established) | FasterCoin: Abc files carry "Copyright (C) 2012, FasterCoin" | — | Lower commit volume (all three repos together: 69 in 2010, 57 in 2012); Abc 2012; orbital branching 2014; Positive Edge 2015 |
| 2017–2026, GitHub era | Volunteer maintainer of Clp/Cbc among Vigerske, Ralphs and Santos | Own laptop ("a small laptop", Cbc#661, 2024), Linux Ubuntu, gcc 11.4 (Cgl#99, 2024); "I rarely use Windows" (Clp#299, 2024) | 486 issue comments; about 813 commits (Clp 313, CoinUtils 120, Cbc 380) |

### 0.2 Authorship map (labels that must survive into the skill)

| Component | What the record shows | Label |
|---|---|---|
| Clp simplex core (ClpSimplex, Dual, Primal, Factorization, PackedMatrix, pivot classes, NonLinearCost, Idiot/IdiSolve, ClpSimplexOther) | First commit `b4253486` (2002-07-30, 38 files, 14,913 lines) is his. Blame shares 85–97% (ClpSimplex 85%, Dual 91%, Primal 94%, Idiot 93%, SimplexOther 97%). 1,597 of Clp's distinct commits are his (Vigerske 487, Ralphs 370 next). | his code [practice, primary] |
| Abc / Aboca (Abc*, CoinAbc*) | Authors line "John Forrest". "Copyright (C) 2012, FasterCoin". Blame 96–98%. | his code [practice, primary] |
| CoinFactorization | Authors line "John Forrest"; first-person design note (§5.1) | his code [stated + practice, primary] |
| CoinOslFactorization (2009) | Authors line "John Forrest", but the header says "This is ripped off from OSL!!!!!!!!!" and the copyright reads "1987, 2009, International Business Machines". Added in commits "osl" (2009-07-18) and "adding osl" (2009-11-05). Comments tagged JJHF in it ("HINCOL MAY HAVE CHANGED? (JJHF) ???") read as a porter's notes. | port of IBM OSL code [practice, primary]; OSL authorship not shown |
| ClpPdco | Authors line "John Tomlin". Blame shows 92% Forrest because he committed it (2003, "pdco seems to work"). | Tomlin's code |
| ClpPE* (Positive Edge) | Authors lines "Jeremy Omer" and "Jeremy Omer, Mehdi Towhidi". Forrest committed it ("add PE code", 2015-06-25); blame shows 86% Forrest. | Omer and Towhidi's code |
| ClpPredictorCorrector / ClpInterior | Authors "John Tomlin (pdco) / John Forrest (standard predictor-corrector)". He calls it "rather basic as Interior point is not my speciality" (2003-12-02). | his code, self-described as basic |
| Clp/CoinUtils presolve | Mixed. ClpPresolve: Forrest 66%, Hafer, Ladanyi, Vigerske. CoinPresolveDoubleton: Hafer 53%, Forrest 45%. Dupcol: Forrest 80%. Dual: Forrest 53%, Hafer 43%. Matrix: Hafer 41%. | shared |
| Cbc, early history | Imported 2004-10-29 by Laci Ladanyi as "Coin Branch-and-Cut (formerly known as Sbb)". Up to 2005-12-31, Forrest made 217 of 225 distinct commits. Clp commits of 2003–04 mention Sbb ("Ray may be null in Sbb", "to make sbb faster"). | early Cbc his by practice. Sbb's own authorship is not shown by any Authors line; "probably his" is [inferred]. |
| Cbc files he created | CbcCompareActual (2004-11-17), CbcFathom / CbcFathomDynamicProgramming (2004-12-08), CbcHeuristicGreedy (2005-03-22), CbcStrategy (2005-03-31), dynamic pseudo-costs in CbcBranchDynamic (2005-05-19), CbcHeuristicFPump (2005-06-05), CbcStatistics (2005-06-26), CbcHeuristicLocal (2005-10-05), CbcLinked (2006-12-01), CbcHeuristicRINS (2006-12-18), CbcSolver (2007-03-30), CbcThread (2009-12-16), CbcHeuristicDW (2013-07-29), CbcSymmetry (2014-07-16) | his, by file creation and blame (FPump 84%, Greedy 93%, Linked 94%, DW 98%, Thread 91%, Node 82%, Model 61%) |
| Cbc parts by others | Diving heuristics: Joao Goncalves (Forrest committed "adding diving heuristics from Joao", 2008-02-13; Goncalves added more). RandRound and PivotAndFix: Robin Lougee (2008). Mipstart: "New mipstart provided by Haroldo Santos" (2012). C interface: Santos 67%+. CbcSymmetry: Authors "Pietro Belotti" (.hpp) and "Jim Ostrowski (the good bits - rest JJHF)" (.cpp, committed by Forrest). 2026 bound propagation, row reductions, coefficient strengthening, postprocess repair, SppGrasp: Haroldo Santos. | others' code |
| Blame artefact in Cbc | Edwin Strayer's 2009 refactor ("Broke up CbcBranchActual", "Broke out CbcHeuristicRENS, CbcHeuristicDINS and CbcHeuristicVND out of CbcHeuristicRINS", AStyle reformatting) makes blame credit him with 59–89% of the split files (SOS, Lotsize, DynamicPseudoCost, GeneralDepth, DINS, VND). Code that predates 2009 in those files is not his. | blame ≠ authorship [practice, primary] |
| Cgl | Not cloned. Headers of CglProbing, CglPreProcess and CglGomory carry no Authors line (S20). Credit by others: "components of the COIN-OR Cut Generation Library" (S27). His own words: Cgl012Cut, "quite likely that I was last person to modify it" (Cgl#63, 2021); the FIXED_BOTH_WAYS probing code is his "new coding" (Cbc#479, 2022). | unresolved beyond these items |
| OSL (and its MIP), LAMPS, UMPIRE, Sciconic, MPSX/370, Alligator | No code visible. Credited by others: "a developer of Alligator, Umpire, Sciconic, MPSX370, OSL" (S27). In Clp's notes he claims two OSL pieces: the cost modification against degeneracy ("which I put in OSL") and forward-progress checks ("I overdid that in OSL"). Nothing on OSL's MIP was found. | credit by others; two OSL pieces stated by him |

---

## 1. Layer 4, LP simplex: experiment and execution

### 1.1 What he did first, and what came next (Clp, 2002–2003, from the commit log)

| Date | Commit subject (verbatim) | Reading |
|---|---|---|
| 2002-07-30 | "Adding Clp to development branch" | A complete primal and dual simplex, Dantzig and steepest-edge pivoting, a non-linear-cost class, a stand-alone driver and a netlib unit test, all in one commit [practice] |
| 2002-07-31 | "To stop valgrind complaining" | Memory checking from day 2 [practice] |
| 2002-08-01 | "Make sure can solve infeasible problems"; "For infeasible problems" | Infeasibility handling came before speed [practice] |
| 2002-08-05 | "Improving reliability using IBM Burlington problems (Primal)" | Hardening on real IBM models [practice] |
| 2002-09-17 | "Synchronizing", which adds class ClpSimplexProgress, "which is where anti-looping stuff should migrate to" | Progress checking within 7 weeks (see §5.1) [practice] |
| 2002-10-04 → 10-30 | "Presolve (no changes to Makefile)" … "Still trying to harden presolve" … "Testing presolve on nasty burlington problem" … "First try at over 2 giga-elements" … "Consecutive presolves better" | Presolve was hardened on the same real models; size limits were pushed early [practice] |
| 2002-10-10 | "New "example" linking osl to ekk" | Differential testing against OSL (§1.3) [practice] |
| 2002-11-05 | "First attempt at perturbation" | Anti-degeneracy came after reliability [practice] |
| 2002-11-25 | "Idiot and modifications for Visual C++" | The Idiot crash arrives 4 months in [practice] |
| 2002-11-27 | "Ouch - I did not look at bcopy - then I thought it so simple a change I did not do proper test.  Apologies." | Admits skipping a test, in the log itself [stated] |
| 2003-01-06 | "Improvements for miplib" | Clp is already being driven by MIP use [practice] |
| 2003-10-09 | "Start of mini sprint" | — |

All [practice/stated, primary: S1]. Pattern [inferred]: correctness on hard real models (infeasible, huge, degenerate) came before refinements. Crashes and perturbation came after the code was robust on IBM's own problems.

### 1.2 Test material: real models first, then public sets with known answers

- **Clp's first unit test** (2002) ran the netlib set (95 `mpsName.push_back` entries in `Test/unitTest.cpp` of `b4253486`). The README told users how to stress it: "If you want to stress the code you can set various stuff e.g. dantzig pricing and then go into netlib testing.  I do not guarantee that it will solve all netlib if you get too creative." [stated + practice, primary: S1]
- **Cbc's MIPLIB harness** (`src/Attic/unitTestClp.cpp`; the note in it is signed "jjf"):
  - Each `PUSH_MPS` line records rows, columns, known optimum, continuous optimum, a difficulty set, and a per-problem switch for the row-cut debugger.
  - The return value encodes "100*(number with bad objective)+(number that exceeded node limit)".
  - In 2021 and 2024 he extended it to MIPLIB 2010 by difficulty grade. The note reads: "Difficulty 10-13 not too bad", "14-17 harder", "18 large may run out of memory when threaded", "20 infeasible problems", "21 - 28 user problems". Users can check their own model's value through `-DCBC_USER_UNIT_TEST1=12345.0`.
  - Commit history: "allow more models in unit test" (2021-04-05); "make it easier to run unittest on user models" (2024-07-25); 2006-10-16 "modify CoinSolve so -miplib will solve all 44".
  - [practice, primary: S3]
- **Users' failing models become test sets**:
  - In 2024 he kept a directory of one reporter's models: "I have a directory ~/cullmann with files and a file testset in that directory and then cbc -dirmiplib ~/cullmann ..... works" (Cbc#668, 2024-08-28).
  - In 2021 he answered an LP-format bug with "your three (and twenty others) work" (CoinUtils#146).
  - His own 2026 timing runs used a directory named `miplib3++level0-3` (Cbc#774, 2026).
  - [practice, primary: S5]
- **Real application models as the original motivation**:
  - The 2002 commits name "IBM Burlington problems" (what they were is not stated).
  - The 2004 Clp FAQ says Clp "has been tested on many problems of up to 1.5 million constraints" [observed, secondary: S29, answer initialled "DN"].
  - The COIN-OR Cup citation singles out his use of "difficult real-world problems to drive the development of software tools" [observed, secondary: S27].
- **The co-authored papers say the same, in abstracts**:
  - UMPIRE (1974) sorts "the nontrivial integer programming problems we encounter" into two classes before discussing which heuristics fit each [stated, co-authored, primary: S13].
  - Forrest–Goldfarb (1992) tests steepest edge "on truly large-scale realworld linear programs with as many as tens of thousands of rows and columns" [stated, co-authored, primary: S9].
  - The 2006 IJOC paper names a MIPLIB instance and a larger one "downloadable from the COIN site (IBM 2004)", i.e. instances were published for others [stated, co-authored, primary: S15].

### 1.3 Differential testing and deliberate stress

- **Clp against OSL inside running algorithms** (`examples/ekk.cpp`, 2002-10-10): the interface functions "were written so that calls to osl in the middle of complex algorithms could easily be swapped for Clp code.  This was to stress test Clp (and Osl :-))." The example also checks "if we need a crash in Clp" and which code behaves better after postsolve. It closes: "Virtuous people would add return code checking." [stated + practice, primary: S1]
- **Mixing algorithms on purpose**. The `netlibTune` help text (added 2005-04-08): "This exercises the unit test for clp and then solves the netlib test set using whatever works best.  I know this is cheating but it also stresses the code better by doing a mixture of stuff.  The best algorithm was chosen on a Linux ThinkPad using native cholesky with University of Florida ordering." [stated, primary: S1]
- **Other solvers as referees for correctness, not as speed baselines** (2019–2026 issue record):
  - "I have tried several solvers which all say infeasible" (Cbc#608, 2023).
  - "Cbc master gives same solution value as scip and gurobi, which shows that this is a borderline case" (Cbc#697, 2025).
  - He notices other solvers' settings: Gurobi's default gap "1.0e-4 which seems quite high" (Cbc#481, 2022); HiGHS's "optimal" being worse "due to using 0.01 as gap" (Cbc#703, 2025).
  - [practice + stated, primary: S5]

### 1.4 Measurement habits

- **He measures the build, not only the algorithm.** In Cbc#462 (2022-02-04) he timed the same MIPLIB 3 unit test with five executables: AMPL's cbc 10:31; Debian's cbc 3:58 elapsed, 4:36 CPU; 2.10.6 debug without optimisation 6:13; debug "sensible" 5:47; optimised 1:59. His conclusion: "By default cbc picks up threaded blas which is not a good idea". Four years later he changed the default ("make sure only one thread for openblas", 2026-05-09). [practice, primary: S5, S3]
- **Overhead measurements of other people's changes.** On Vigerske's PR changing time measurement (Cbc#774, 2026) he ran a test set with and without "micromanaging time" and reported real/user/sys for four configurations. He concluded the change "made the code less efficient.  But only when time mode is default of elapsed!" [practice, primary: S5]
- **Profiling before switching something off.** Commit `65e778e1` (2026-10-24), "SppGrasp can be Very expensive - so default off", includes a gprof flat profile on AIR03 with 91.92% of time in `CbcSppGrasp::localSearch`. The heuristic had been added by Haroldo Santos six days earlier. [practice, primary: S3]
- **Long single-instance runs as experiments.** "I am trying to solve my effort to experiment with problem mas76 … The last node count was 8834862000 so you can see why long int is needed." (Cbc#628, 2023-12-13). In Cbc#633 (2024) he let SCIP run overnight on a reporter's model ("It took ten hours and the maximum depth was over 4000!"). [practice, primary: S5]
- **Matrix statistics as a first diagnostic.** For a badly scaled model he posted the element histogram by decade, from "between -10 and -1" to "between 1e-11 and 1e-08" (Cbc#338, 2020). For a slow LP he rescaled the objective: "If I change all 1.0e15 objective values to 1.0e11 and all 1.0e20 to 1.0e12, it solves with primal or dual in only 3K iterations." (Cbc#286, 2020). [practice, primary: S5]

### 1.5 Debugging toolkit (what the code and the issue record show)

- **Memory and runtime checkers**: valgrind appears in commit subjects from 2002 to 2024 ("To stop valgrind complaining", 2002-07-31 and 2024-01-21; "keep valgrind happy", 2021). gdb sessions are pasted into issues (Cbc#599, 2023, prints the bad TwoMir cut row; CoinUtils#206, 2023, shows a breakpoint). [practice, primary: S1, S3, S5]
- **Replay against an earlier log**: `ClpSimplexDual.cpp` keeps `FORCE_FOLLOW` (added 2004-09-28, commit subject "To make it easier to match two runs"), with the comment "To force to follow another run put logfile name here and define". It reads the old run's per-iteration message lines and forces the same outgoing and incoming variables ("Iteration %d will force %d out and %d in"), so two runs can be compared pivot by pivot. [practice, primary: S1]
- **Known-solution oracle for MIP** (added 2005-10-13). The `debug` parameter help: "The idea is that if you suspect a bad cut generator you can do a good run with debug set to 'create' and then switch on the cuts you suspect and re-run with debug set to 'debug.file'". He still prescribes it 20 years later: "run it with -debug create and then run bad version with -debug debug.file" (Cbc#668, 2025). Running in debug mode it prints, for example, "Cut with 52 coefficients, cuts off known solutions by 0.000397818" (Cbc#562, 2022). [stated + practice, primary: S1, S5]
- **Debug-only assertions, and builds as variables**:
  - Assertions are compiled out under NDEBUG. He diagnoses reports by asking whether the binary was a debug build: "It looks as if CBC 2.10.5 from Debian Stable (bullseye) was compiled with debug!" (Cbc#462).
  - "It has taken me a few attempts to build a version that loops, as tiny variations in compilation make the code take a slightly different path." (Cbc#563, 2022)
  - A master bug "did not show up initially on my tests as it was an uninitialized variable which was zero in my builds" (Cbc#451, 2021).
  - [practice + stated, primary: S5]
- **Making non-determinism go away before debugging**: "With multiple threads Cbc is not deterministic which makes it a bit more difficult to debug (it can be made deterministic by -threads 112 …)" (Cbc#714, 2025). [practice, primary: S5]
- **Reducing a failure to a small model**:
  - PaPILO, 2024: "I have managed to reduce the problem down to a small one". He attached a two-file diff (one bound changed) showing good and bad behaviour (papilo#62).
  - For the probing bug he saved "model just before problems" as an MPS file and gave a one-line command to reproduce (Cbc#769, 2026).
  - [practice, primary: S6, S5]
- **Many working copies**: "I have many versions of master.  The one I am working on most now lacks many recent updates" (Cbc#668, 2024). He bisects by copying single files between stable and master ("all was OK when I copied that over from stable", Cbc#639, 2024). [practice, primary: S5]
- **Investigation macros left in the code**: counts at HEAD in `src/*.?pp`, not all of it his:

  | Repo | `#if 0` blocks | `COIN_DEVELOP` | `CLP_INVESTIGATE` |
  |---|---|---|---|
  | Clp | 377 | 83 | 85 |
  | Cbc | 52 | 108 | 62 |

  [practice, primary: S1, S3]

### 1.6 Algorithm choice is coded as rules on model statistics

`ClpSolve.cpp` (blame: Forrest 61%, Hafer 33%) chooses among dual, primal, Idiot, Sprint and crash from cheap statistics of the model [practice, primary: S1]:
- On large automatic runs, a single nonzero cost or all costs ±1 force primal.
- Idiot and Sprint are switched off if any variable is free. Sprint is also switched off "if very few with costs or great variation in cost".
- The Idiot crash is tried only on long problems (rows > 200, columns > 2000, columns > 2 × rows) that are not small. The right-hand sides must also be integral and of similar size (largest/smallest ≤ 10). The number of Idiot passes is then set from the rhs range and the problem size.
- The share of ±1 matrix elements is counted: "If 90% +- 1 then go for sprint".
- Network matrices switch Idiot off; a quadratic objective forces primal or barrier; a non-slack starting basis switches off everything except Sprint.

The 2002 TODO had asked for "the option for the code to automatically choose which method". He still tells users when the guess is wrong: "the Clp program guessed incorrectly that it should use primal.  If I tell Clp to use dual, I get same run as your Cbc one." (Cbc#301, 2020). [stated, primary: S1, S5]

### 1.7 How experimental code lives (compile-time switches, defaults changed by judgement)

- **Experiments ship behind defines, off by default**:
  - Aboca: `--enable-aboca` with build types 1–4 (serial/cilk, with or without inherited code). The configure default is `use_aboca=no`. A 2020 commit fixes it, adding "(only useful one is =4 anyway)".
  - Probing: "Code put in master - switched off unless -DFIXED.... in build.  May ask you to test some dubious improvements" (Cgl#81, 2022).
  - In 2024 he added one umbrella switch, `CBC_MORE_CUTS_ETC` ("Switches on a set of defines with just one define in build procedure"), at the top of `CbcModel.hpp`. It defines three of them and lists about 15 more that "would have to defined in build procedure".
  - Markers for ideas that would change results: "Ideas which seem possible but changed current behavior will be found in areas marked with DETERMINISTIC_TUNING" (`CbcGeneralDepth.cpp`, 2024-06-25).
  - He states the policy as a question to users: "Is the general opinion that I should take out #define and allow curious users to use -DFIXED_BOTH_WAYS=1 in build?" (Cgl#81).
  - [practice + stated, primary: S1, S3, S5]
- **Defaults change on his judgement, with a reason and a way back**:
  - "Changed depth parameter default to +1 from -1.  This uses Clp in a more sophisticated way and does seem to faster.  A user can always change it back." (Cbc `8d0c2d5e`, 2025-10-30). He had called depth 1 "my preferred choice" in Cbc#710 (2025).
  - SppGrasp default off (2026, §1.4).
  - OpenBLAS forced to one thread (2026).
  - [practice + stated, primary: S3, S5]
- **The interfaces are not his to change**. He builds escape hatches for users stuck behind a wrapper. For python-mip users: "if the environment variable COIN_CBC_OPTIONS is set … the code reads standard cbc options which adds some items not directly accessible from the C interface" (Cbc#618, 2023). [practice, primary: S5]

---

## 2. Layer 4, MIP craft (Cbc and earlier codes): execution

### 2.1 Order of construction (Cbc commit log, his commits only)

| When | What (commit subject or file) |
|---|---|
| 2004-10-29 | Import of "Coin Branch-and-Cut (formerly known as Sbb)" (by Ladanyi), then his "version 0.7" and "start of nested search and branching cuts" (CbcBranchCut) |
| 2004-11 / 12 | CbcCompareActual (node selection), CoinSolve driver, CbcFathom / dynamic-programming fathoming |
| 2005-03 → 06 | Greedy heuristic ("samples"), CbcStrategy ("for OsiCbc"), "starting dynamic pseudo costs", "fpump", "add statistics" |
| 2005-10 | local-search heuristic; "add debug" (the known-solution oracle) |
| 2005-11-16 | Version log 1.00.00 (§5.2); Cbc 1.0 aimed at INFORMS 2005 (2005 FAQ, S30) |
| 2006-12 | CbcLinked ("for quadratic integer etc"); RINS ("mostly for rins") |
| 2007 | "Goes parallel" (version log, June 2007); "for deterministic parallel" (2007-12-13) |
| 2008 | Diving heuristics from Joao Goncalves; stubs for Lougee's RandRound and PivotAndFix |
| 2009-12 | CbcThread ("preliminary changes for cleaning up threads and smaller CbcModel methods") |
| 2013-07-29 | "adding a dubious heuristic": CbcHeuristicDW ("very very compute intensive. It tries to find a DW structure and use that") |
| 2014-07 | "First try at orbital branching"; nauty |
| 2024 | fathomMany in deterministic parallel; PaPILO presolve hook ("Not much work has been done recently in Coin on pre-processing for integer problems") |
| 2025–26 | Preprocessing fallbacks on tolerance failures; mipstart with maximisation; time-check overhead; semi-continuous to lot-sizing tolerance |

All [practice, primary: S3]. Pattern [inferred]:
- The tree search and its bookkeeping come first, then a cheap primal heuristic, then branching statistics, then the pump, then a debugging oracle. Parallelism and symmetry come years later.
- His 2006 slides already flagged symmetry breaking as missing (§7). Orbital branching arrived in 2014.

### 2.2 Branching, strong branching and how much to trust a number

- **Use strong-branching results without fully trusting them**: in strong branching the fast dual may stop on iterations. A "status of 3 … means the code will take some notice of the result, but will not totally trust it e.g. for fixing variables" (Cbc#545, 2022). [stated, primary: S5]
- **Guard extrapolations near integrality**: a pseudo-cost-based bound fix went wrong because a value of 20.000003 sat just outside the integer tolerance: "about three computations went the wrong way". His fix: "those computations will not be used unless the variable is much more away from an integer" (Cbc#689, 2025). [stated + practice, primary: S5]
- **Mini-trees inside the LP solver**: "fathomMany … does a few branches using Clp and tries to be much more efficient as it knows about Clp. It will also lend itself well to deterministc parallel" (`CbcGeneralDepth.cpp`, 2024). The default was moved to it in 2025 (§1.7). [stated + practice, primary: S3]
- **Third-party copy of his 2006 slides** [stated, secondary: S34; wording known only from a fetch tool's summary, not verified against the original]: the Tuning slide names strong branching as a weak point of Cbc, and a parameter (TrustPseudoCosts) sets how many strong branches occur before pseudo-costs are trusted.

### 2.3 Preprocessing: aggressive by default, with fallbacks when tolerances bite

- **Fall back to a simpler preprocessing when the clever one says infeasible**. Code comment: "Infeasible - but most real problems are not infeasible - so try simpler preprocessing which is less affected by tolerance issues" (quoted by him in Cbc#753, 2025). Commit "If preprocessing infeasible - repeat in a simpler way" (2025-10-25). His explanation: "Tolerance issues again - with preprocessing trying to be too clever.  One idea I tried was far far too complicated and would lead to other problems." (Cbc#752). [stated + practice, primary: S3, S5]
- **Tell the user, rather than fix the impossible**. Message Cgl0013I reads "Postprocessed model is infeasible - possible tolerance issue - try without preprocessing". He relies on it: "Hopefully the Cgl0013 message is enough to alert a user". Catching such cases in general would be "nearly impossible with a mixture of continuous and integer variables and a lot of work in general" (Cbc#497, 2022). [stated, primary: S5]
- **A simple preprocessing as a user workaround**: "-tune 99000000 … the 99 says do a very simple preprocess" (Cbc#282, 2020). [stated, primary: S5]
- **Preprocessing legitimately cuts off non-optimal starts**: "Thinking it over, there may be no bug anywhere.  The point of preprocessing is to tighten and reduce the model in order to get an optimal solution.  This can cut off non-optimal solutions." (Cbc#282, 2020). [stated, primary: S5]
- **Bringing in an outside presolver**. PaPILO was hooked into CglPreProcess behind `-DCBC_USE_PAPILO=1` (2024-09-10). Two PaPILO bugs he found while testing went upstream: a near-infinite loop (he "had to kill it after more than a day") and a wrong answer with large upper bounds (papilo#59, #62). [practice, primary: S3, S6]

### 2.4 Model-level judgement (formulations he recommends or tests)

- **Semi-continuous versus binaries, tested rather than asserted** (Clp#165, 2020):
  - He first made Cbc preprocessing work with semi-continuous variables. He then reformulated the same model with 0-1 variables and compared.
  - With cuts, the 0-1 version raised the lower bound from about 122466 to 122491.58, and found 122497.284 against 122500.72.
  - His remark: "Semi-continuous variables were invented in the 1970's before cuts were used in integer programming.  Now it may be better to use 0-1 variables (although this is problem dependent), even though the problem will be larger."
  - [practice + stated, primary: S5]
- **Indicator constraints** (Cbc#572, 2023):
  - "I would think that the big M approach is slightly better than the SOS approach, especially if the big M is as tight as possible."
  - He admits "The code has never really been tested on real problems".
  - He offers to add the alternative "if I can be convinced of its merit", and added the SOS version the next day ("Added SOS version").
  - [stated + practice, primary: S5]
- **Linked ordered sets and SOS history.** Linked ordered sets were Beale's generalisation of SOS ("invented by Beale & Tomlin"). OsiSolverLink "is to do with solving non-linear problems which have integer variables and/or is non convex", and "it is possible that it is a half finished project" (Cbc#297, 2020). [stated, primary: S5]
- **Maximisation is normalised internally**: "bugs kept creeping in for maximisation problems, so it was decided to flip the objective at the start of branch and bound and then back at end" (Cbc#519, 2022). This is design by defect history. [stated, primary: S5]
- **Heuristics need a starting point more than cleverness**. In Cbc#494 (2022) his best run came from "the "stupid" option of solving the problem without any objective", using that poor solution as a start. "So it looks as if just having immediate solutions for the heuristics to use helps a lot on this problem." For long runs he advises repeating the root heuristics and cuts; the multiple parameter "just runs all the heuristics four times with slightly different parameters" (Cbc#633, 2024; also Cbc#729, 2025). [stated + practice, primary: S5]
- **Feasibility pump and integer slacks**: turning slacks into integer variables "can improve search by giving extra flexibility … But for heuristics and especially the feasibility pump, this is probably not a good idea". He changed trunk so such singleton integers are treated as continuous for many heuristics (Cbc#219, 2019). [stated + practice, primary: S5]

### 2.5 Earlier MIP codes (papers only; abstracts or metadata)

- **UMPIRE** (Forrest, Hirst & Tomlin 1974, abstract) [stated, co-authored, primary: S13]:
  - Branch and bound inside the UMPIRE system, with computational experience.
  - Two problem classes: fewer than 100 binaries inside a very large, hard LP; or several hundred integers, often in SOS, inside a simpler LP of 500–1,000 rows.
  - Problems of the first class "do not generally behave well using a simple-minded “penalty” approach".
  - The main devices are "priorities", the "best projection criterion" and "pseudo-costs".
  - Full text not read.
- **Beale & Forrest 1976** (SOS for global optimisation) and **Forrest & Tomlin 2007** (*Annals of OR* 149, "Branch and bound, integer, and non-integer programming"): metadata checked, text not read [S21, S23].
- **IBM semiconductor supply chain MIP** (Denton, Forrest & Milne, *Interfaces* 2006, abstract): "three heuristics, driven by practical applications" and use of model structure; used daily at IBM. His role inside the team is not stated. [stated, co-authored, primary: S14]
- **Multiple knapsack with colour constraints** (Forrest, Kalagnanam & Ladanyi, *IJOC* 2006, abstract) [stated, co-authored, primary: S15]:
  - Column generation solved MIPLIB's `mkc` to optimality in less time than the original LP relaxation.
  - Dantzig–Wolfe bounding was used for the larger `mkc7`.
  - Per the fetch summary of the 2006 slides (mirror), Cbc took 150 minutes on the subproblems, 50 after tuning [secondary, S34; not verified].
- **OSL's MIP**: nothing found in this run.

---

## 3. Layer 5: how he judges results

- **First question: model, tolerance, or code?**
  - About 49 of his comments mention tolerance, scaling or accuracy (keyword count, not hand-classified).
  - Typical sentences: "A tolerance issue." (Clp#103), "Scaling problem." (Cbc#333), "It is a tolerance issue - which can happen if you are unlucky enough" (Cbc#689).
  - He gives the threshold at which the answer flips: "With -dualtolerance 1.0e-8 gets 0.19211699 (with 1.0e-7 it is 0.16355199 - which shows how sensitive to tolerances it is)" (Cbc#333, 2020).
  - [practice, primary: S5]
- **Variance in MIP times is not a bug**: "Not a bug - more a feature of integer programming." (Cbc#633, 2024). On a version-to-version slowdown: "you could say you were lucky", and "even small changes in compiler options can make a difference" (Cbc#494, 2022). [stated, primary: S5]
- **Check claims in code against measurement**: "Note JJF - the speed claim seems to be false on IA32 so I have added CoinMemcpyN which can be used for atomic data" (`CoinHelperFunctions.hpp`, 2003-11). On templates: "I think the use of templates was a mistake as I don't think inline generic code can take as much advantage of parallelism or machine architectures or memory hierarchies." (`ClpHelperFunctions.hpp`, 2003-12-02). [stated, primary: S2, S1]
- **Safe and dumb beats clever and unverified, in someone else's code**:
  - For a bad TwoMir cut: "A solution that can do no harm is to weaken the problem (just for CgTwomir)".
  - Then: "If someone with more knowledge of the code could investigate - that would be good.  If not, I will probably modify the code in a day or two." (Cbc#562, 2022).
  - In duplicate-column presolve: "I know from experience how easy it is to get one of the cases wrong.  I have modified so that it does not try as hard." (Cbc#639, 2024).
  - [stated + practice, primary: S5]
- **Speed against correctness, case by case**:
  - "I have fixed - even if it means code is nanoseconds slower." (Clp#91, 2018).
  - A reporter's proposed fix for a problem he could not reproduce was set aside with the remark that the fix "slows code down considerably" (Clp.old#40, 2018).
  - "Doesn't look like it can cause problems - so only corrected in master." (Clp#277, 2023).
  - [stated, primary: S5]
- **Barrier and QP judged harshly, by his own standard**:
  - "Barrier looks a bit of a mess.  Simplex is consistent when I scale it in different ways." (Clp#23, 2019).
  - "quadratic barrier seems a work in progress (or a mess to put it another way)" (Clp#274, 2023).
  - In 2020 he made Clp detect that barrier "will use too much memory and switch to simplex.  Looking at the flop count, barrier would have taken several years!" (Clp#151).
  - [stated + practice, primary: S5]

---

## 4. How he answers bug reports, criticism and contributors

**Volume and speed** [practice, primary: S5–S7]:
- 486 comments in 293 threads; most on Cbc (315), then Clp (103). Per year, for the 481 in the five coin-or repositories: 2017 3, 2018 26, 2019 46, 2020 49, 2021 72, 2022 71, 2023 58, 2024 52, 2025 65, 2026 39 (to 2026-11-01).
- Response time, for the 265 threads opened from December 2018 that he joined: median 0.6 days from opening to his first comment. 177 got his first reply within 1 day, 229 within 7. Threads he never joined are not in this sample.
- On 2018-11-12 he posted 21 comments in one day on old Trac tickets migrated to Clp.old. Seven report that the problem could not be reproduced. The rest are one-liners such as "Hopefully fixed in trunk" or "Already in trunk": retest everything on the current trunk, then answer.

**The reply pattern** [practice, primary: S5]:
1. Try to reproduce on his own build, and say so: 33 comments are "unable/could not reproduce".
2. If he cannot reproduce, ask how the binary was built, or for the model: "How exactly do you build Cbc." (Cbc#714); "What operating system and compilers are you using (I use Linux Ubuntu)?" (CoinUtils#147); "If you send problem to me I will see what can be done." (Clp#125).
3. Give a workaround, often in the same reply, usually a switch (`-preprocess off`, `-scaling off`, `-dualBound 1.0e15`, `-primals`).
4. Fix master first, then stable, and post the diff for users who cannot upgrade. About 72 comments report "should be / hopefully fixed".
5. Explain the mechanism in a paragraph: dual fake bounds, composite infeasibility cost, why dual cannot easily return a feasible point on unbounded problems.

**Admitting mistakes, in public and briefly** [stated, primary: S3, S5]:
- "I am an idiot.  Put in tiny change at end before commit." (Cbc#748, 2025)
- "My mistake - my brain had gone mushy." (Cbc#543, 2022)
- "Apologies - my stupidity.  I totally forgot I had made a change a few weeks ago." (Cbc#759, 2026)
- Commit subjects: "ouch - ancient typo gives rare error" (2022), "I hope 2017 gets better for stupid mistakes" (2017-01-06), "stupid idiot only tested via cbc" (2025-09-06), "Apologies - put test in wrong place" (2026-10-06).

**Declining, always with a cost argument** [stated, primary: S5]:
- "It would be a lot of work to fix this and I don't think it worth it.  It took two minutes to modify problem so reads in correctly" (CoinUtils#94, 2019).
- "I have no intention of changing the code to allow neos-5044663-wairoa.mps.gz to be read", because the file declares fixed MPS (Cbc#342, 2020). Two days later he made the free-format fix and put `$` comments behind `COIN_ALLOW_DOLLAR_AS_COMMENT`: a refusal followed by a guarded compromise.
- "I am not going to bother to fix this.  The OSL factorization predates Coin." (Cbc#719, 2025)
- "Very slow reading .lp file - but I am not fixing that." (Cbc#717, 2025)
- "No sensible user would use that combination.", although he still patched the initialisation (Cbc#704, 2025).
- "I am not sure that this is an important bug - the clue may be in the use of "glitch"" (Clp#188, 2021).

**Saying where his knowledge stops** (19 comments) [stated, primary: S5]:
- "I am not an expert on C interface" (Cbc#202, 2019)
- "I have not got the energy to dig into the Julia interfaces" (Cbc#301, 2020)
- "I know very little about pulp and python" (Cbc#446, 2021)
- "I don't understand much of the coding in CoinLpIO.cpp - but still try to fix bugs." (CoinUtils#210, 2023)
- "I never use the clique strengthening code - would be good if someone more knowledgeable could take a look." (Cbc#750, #751, 2025)
- Interior point: "not my speciality" (code note, §0.2)

**With co-maintainers** [stated, primary: S5]:
- Release hygiene: "go ahead - I will try and remember not to put anything interesting into stable - just fixes." (Cbc#591, 2023)
- "Should I put that back - or are we in a cleanup mode to making master the next release???" (Cbc#741, 2025)
- In 2026, as a large "next" branch was built by others (Haroldo Santos alone made 477 distinct Cbc commits in 2026; 79 Cbc commit messages of 2026, across all branches, contain the word "Claude", none of them his): "I am worried about the speed with which all the changes are happening" and "Are we getting much feedback from users (apart from claude)?" (Cbc#809, 2026-10-17).
- And: "I don't mind clunky. I do mind - a) not knowing whether to look at master or next b) the enormous number of changes in next." (Cbc#807, 2026-10-20). Quoted with the list layout collapsed.
- Context counts from S3.

---

## 5. Documentation behaviour (Layer 6 as practice)

### 5.1 Design notes are written when a file is born, and then left alone

- **The 2002 notes are still in HEAD**:
  - `ClpSimplexDual.cpp` and `ClpSimplexPrimal.cpp` open with "Notes on implementation of dual/primal simplex algorithm".
  - Their sections: (A) how to get feasible with fake bounds or costs as in OSL; (B) pivot choice as a virtual class; (C) "Sounds easy, but this is hardest part of algorithm": bound-flipping "mini iterations", accuracy, degeneracy.
  - References: Forrest–Goldfarb 1992, Forrest–Tomlin's 1992 IBM Systems Journal paper, Gill et al. 1988.
  - A TODO list.
  - Ignoring whitespace, the dual note in HEAD is identical to `b4253486`. The primal note changed once: in "First attempt at perturbation" (2002-11-05), "perturb the costs significantly" became "perturb the rhs and bounds significantly". It was revised in the commit that implemented what it discussed, and never again.
  - [practice, primary: S1]
- **The notes outlived what they describe**:
  - The TODO says "At present I never check on forward progress", and the method note says "At present we never check we are going forwards.  I overdid that in OSL so will try and make a last resort."
  - Yet ClpSimplexProgress, "where anti-looping stuff should migrate to", was added on 2002-09-17, seven weeks later.
  - The same notes were copied, reformatted but unrevised, into `AbcSimplexDual.cpp` and `AbcSimplexPrimal.cpp` for the 2012 parallel code. Abc's parallel design has no comparable note.
  - [practice, primary: S1]
- **First-person admissions in the notes**:
  - "I am undecided about free variables - there is coding but I am not sure about it." (dual method note, 2002)
  - On anti-degeneracy: "At present I am using the modification of costs which I put in OSL and which was extended by Gill et al.  I am still not sure of the exact details." (2002)
  - CoinFactorization: "This class started with a parallel simplex code I was writing in the mid 90's.  The need for parallelism led to many complications and I have simplified as much as I could to get back to this." Then: "I have taken out all outer loop unrolling, dense matrix handling and most of the book-keeping for slacks.  Also I always use FTRAN approach to updating even if factorization fairly dense.  All these could improve performance." And: "I blame some of the coding peculiarities on the history of the code but mostly it is just because I can't do elegant code (or useful comments)."
  - [stated, primary: S1, S2]
- **Self-deprecating naming and framing**:
  - Idiot (2002-11-25): "This class implements a very silly algorithm.  It has no merit apart from the fact that it gets an approximate solution to some classes of problems." Its most useful role: "It can also be used as a "crash" to get a problem started."
  - Its rationale: "algorithms with terrible convergence properties may be okay at first.  Throw in some random dubious tricks and the resulting code may be worth keeping as long as you don't look at it."
  - Added 2003-10-15: the name Idiot "is copylefted", and any replacement "should be something equally stupid (but not "Stupid") or even better something witty."
  - Sprint driver (2003): "This driver implements what I called Sprint.  Cplex calls it "sifting" which is just as silly."
  - Abc: "A Bit Of Clp Accelerated" (Clp#262, 2023).
  - [stated, primary: S1, S5]

### 5.2 Change logs started with intent and then stopped

- **Clp version log** (`ClpMain.cpp`), from "Version 1.00.00 October 13 2004" to "1.11.00 November 5 2009 (Guy Fawkes) - OSL factorization and better ordering". Entries record the drivers of change: "Added basis handling helped/prodded by Thorsten Koch", "Added Volume algorithm as crash and made code more robust on testing". Then they thin out: "1.03.01 May 24 2006.  Lots done but I can't remember what!" and "1.04.01 June 26 2007.  Lots of changes but I got lazy". No entry after 2009. [stated + practice, primary: S1]
- **Cbc version log** (`CbcSolver.cpp`): "Version 1.00.00 November 16 2005.  This is to stop me (JJF) messing about too much.  Tuning changes should be noted here." The last entry is "Version 2.00 September 2007". [stated + practice, primary: S3]

### 5.3 Help text and examples are the manual

- He sends users to the online help, `-allcommands all`, `?` and `??` ("There is not much documentation for the more exotic commands", Cbc#633, 2024), or to an example in `Clp/examples` or `Cbc/examples`: driver3, addRows.cpp "just to explain why it is not a good idea to add one row at a time", sprint.cpp, testQP.cpp. He also writes new drivers on request: stopafter.cpp (Cbc#416, 2021), warmstart.cpp (Clp#132, 2024). [practice, primary: S5]
- Cbc FAQ, 2005, initialled "(JF 04/01/05)": "Is there any documentation for CBC? If you can see this you have the best there is:-)" and "Is CBC as fast as Cplex or Xpress? No. However its design is much more flexible so advanced users will be able to tailor CBC to their needs." [stated, primary: S30]
- Tutorials (DIMACS 2006, abstracts): each promised "walking through one or two examples written in C++ (suggestions for such examples may be submitted before the workshop)", plus "future developments and ways users can help". [stated, primary: S32]
- **Others had to write the documentation he did not**:
  - Galabova & Hall (2018) call their paper "the first meaningful documentation and analysis" of the Idiot crash. They list its sources as code, comments, Cbc documentation and a public e-mail of 2014 (not read here, S19). Of one constant in the code they write: "no indication why this particular value was chosen". They had to edit the source to force Idiot on for their experiments.
  - Huangfu & Hall (2018) say Aboca was introduced at a 2012 conference and that, beyond the source code and a FasterCoin web page, they know of no published reference (S18).
  - [observed, secondary]

---

## 6. Failures, abandoned directions and parked code

| Item | Evidence | Status as recorded |
|---|---|---|
| Parallel simplex, mid-1990s | CoinFactorization note: the class "started with a parallel simplex code I was writing in the mid 90's", which he "simplified as much as I could" | abandoned, simplified into the serial factorization [stated, primary] |
| Abc / Aboca parallel dual (2012) | "The Abc versions were a partially successful attempt to parallelize the simplex method which were implemented more than 10 years ago for a conference and not kept up to date" (Clp#262, 2023-03-28). Off by default in configure. | parked. Yet in 2026 he says, for a set-partitioning LP, "the answer may be as simple as abc" (Cbc#837, 2026-11-01). [stated + practice, primary] |
| Convex piecewise-linear reformulation ("grade" problems) | `ClpNonLinearCost.hpp` (2002): "I did some work on this many years ago on "grade" problems, but while it improved primal interior point algorithms were much better for that particular problem." | dropped because another method class won [stated, primary] |
| Sprint's namesake | "an LP code of the 60's called sprint … On the problems of those days it did not work very well, but it worked very well on aircrew scheduling problems" (sprint.cpp, 2003). The help text says the old code tried the tactic "(not totally successfully)". | an old failure reused where the structure fits [stated, primary] |
| OsiSolverLink / linked ordered sets (2006) | "it is possible that it is a half finished project" (Cbc#297, 2020). The Bonmin note (2007) cites "J. Forrest and J. Lee (in preparation)" for remodelling MINLP as MILP with linked ordered sets. No such paper appears in OpenAlex for A5061258306 (S22; DBLP not reachable). | unpublished, half-finished [stated + practice, primary] |
| Local tree search (local branching; 2004 sample `CbcTreeLocal`) | 2006 slides (mirror, via fetch summary): off by default, not a normal heuristic [secondary, S34]. 2022: "It does look as if local tree search is broken … it may need rethinking." (Cbc#520). | broken and not rebuilt [stated, primary] |
| Benders and Dantzig–Wolfe inside Clp | "First attempt at Benders decomposition" (2009-01-20); "mainly dantzig-wolfe" (2014-03-19); ClpSolve's `tryBenders` / `tryDantzigWolfe` | experimental [practice, primary] |
| CbcHeuristicDW (2013) | Commit "adding a dubious heuristic"; "very very compute intensive". In 2022 "One heuristic - DW - looks interesting I will look further." | kept, still being evaluated [stated + practice, primary] |
| QP: barrier and initialSolve | "Quadratic has not been kept up to date and "initialSolve" got confused" (Clp#274, 2023) | neglected corner [stated, primary] |
| Semi-continuous variables | "It used to work well" (Cbc#784, 2026); "I should look more into those ideas from fifty years ago." | regressions fixed on demand [stated, primary] |
| OSL factorization port (2009) | "I am not going to bother to fix this." (Cbc#719, 2025) | frozen [stated, primary] |
| `CoinBigIndex` as 64-bit | "Clp was designed to work with a large number of elements - by defining CoinBigIndex as long.  The code no longer compiles with that option." (Cbc#661, 2024) | capability lost. CoinUtils commits of April 2020 by another maintainer removed `COIN_BIG_INDEX`; that this caused the loss is [inferred] [stated, primary] |
| Version logs | stopped in 2007 (Cbc) and 2009 (Clp) (§5.2) | abandoned [practice, primary] |
| Mipstart "hack" (2019) | "As a quick hack … Not quite working as I expected/hoped but getting some interesting results." (Cbc#215) | exploratory; became the "silly options" in mipStart (commits 2019-04-16) [stated + practice, primary] |

---

## 7. Early versus late versions

- **Notes**: the 2002 design notes and TODOs are unchanged in 2026, while the code moved on (§5.1). [practice, primary]
- **Claims about Cbc**: in 2005 he wrote that "more testing and improvement is needed before it can get to version 1.0" and that Cbc is not as fast as Cplex or Xpress (S30). The 2005 COIN-OR Cup speaks of "world-class open-source tools" (S27). His later speed comparisons are mostly per instance (e.g. Clp against "another open source code" on one LP, Cbc#717, 2025). One general claim: "Normally Cbc is faster and more reliable than Glpk." (Cbc#489, 2022). [stated / observed]
- **Plans followed through, or not** (2006 slides, third-party mirror, S34; wording via fetch summary, not verified):
  - The preprocessing slide says symmetry breaking is still needed. Orbital branching and nauty arrived in 2014 (S3).
  - A slide says other LP solvers could be used with Cbc the way Clp is. In 2024 he still notes "many many tests to see if solver_ is OsiClp" (Cbc#658).
  - [secondary + primary]
- **Clp claims in 2004** (FAQ, "DN"): the simplex is "as reliable as OSL"; "the principal author, John Forrest, knows more about simplex algorithms than interior point algorithms" (S29). His 2003 code note says the same about himself (§0.2). [observed + stated]
- **Arrangement of releases**: in 2019 he was still checking in through SVN ("I was doing a svn checkin", Cbc#204). By 2021–26 he works on GitHub master/stable and posts diffs against release tags. [practice, primary]

---

## 8. Layer 7: research organisation, as the record shows it

- **Phases** [practice, primary: S1–S3]:
  - A sole author who writes whole solvers: Clp (2002), Cbc (2004–05), Abc (2012).
  - Then a curator who commits others' contributions: Tomlin's PDCO 2003, Goncalves's dives 2008, Santos's mipstart 2012, Omer and Towhidi's PE 2015, Ostrowski's symmetry 2014.
  - Then, since 2019, one of four maintainers, while others did build systems, refactors and C interfaces. In Cbc his distinct commits were overtaken by Santos, Ralphs and Vigerske in 2019–2020. He led again in 2021–2025 and fell behind Santos's 2026 surge.
- **Work unit = one model, one bug, one change**. Commit subjects are short (median 24 characters) and mostly name one fix or a hunch: "Faster?", "hopefully fix compare", "cuts?". 39 contain a question mark and 22 "hopefully". The commit log reads as a lab notebook, not a changelog. [practice, primary: S1–S3]
- **Contributions taken in with credit lines in commits**: "thanks Yiming Yao" (2003), "bug found by John Tomlin" (2006), "fix suggested by randy" (2006), "adding diving heuristics from Joao" (2008), "New mipstart provided by Haroldo Santos" (2012). [practice, primary: S1–S3]
- **Users as testers**. 2005 FAQ: "There are probably ten people who do not always post to the discussion mail list but are constantly "improving" the code by demanding performance or bug fixes or enhancements." (S30). 2022, to a reporter: "May ask you to test some dubious improvements" (Cgl#81). [stated, primary]
- **Others' observation**: COIN-OR Cup 2005 praises his ability to "close the loop" between hard real problems and general tools (S27). Others also credit him as a founder of COIN-OR ("Founding Benevolent Dictator") and with design contributions to OSI and CGL. [observed, secondary]
- **Not visible in this dimension**: students, group meetings, mentoring (agent 04); IBM-internal collaboration practice.

---

## 9. Papers as process evidence (all co-authored)

- **ICM 1998, Anbil, Forrest & Pulleyblank** (read in full, S24) [stated, co-authored, primary]:
  - *Sprint attribution*: Sprint is credited to "John Forrest[16]", a talk at ORSA/TIMS 1989.
  - *Sprint benchmark protocol*: one American Airlines problem (837 flights, 5.5 million pairings), solved by OSL primal, dual and Sprint on successively larger column subsets (5,000 to 500,000), timed in minutes on a 1989 S/390.
  - At 250,000 columns: primal 397.8 minutes, dual 100.7, Sprint 21.5. At 500,000 the primal entry is empty; dual 258.6, Sprint 54.5.
  - The method keeps the basis, prices all columns, buckets them by reduced cost, and adds the best buckets "plus a random selection of columns from other buckets".
  - *Volume crash*: the volume algorithm's dual solution crashes the dual simplex. On three airline problems (2,504–4,810 rows; RS6000/590 CPU seconds) it is reported as on average nine times faster than dual simplex and twice as fast as primal-dual interior. Primal simplex was left out of that table because it "performs very poorly for these problems". Excluding a method is stated with its reason.
- **Forrest & Goldfarb 1992** (abstract only, S9): several primal and dual steepest-edge variants, including approximate ones, are compared with standard rules on large real LPs; the results are said to show steepest edge's superiority "unambiguously". Experiment section not read.
- **Forrest & Tomlin 1992, IBM Systems Journal** (abstract via OpenAlex, publications/abstracts.md; DOI checked): the abstract describes design changes for the IBM 3090 vector architecture, and for RISC System/6000 "it was necessary to rethink this yet again". It closes with the steps "taken to give maximum reliability". Design follows the hardware generation. Not read.
- **Bonmin, Optima 75 (2007)** (read in part, S25): Bonmin was built fast by reusing Cbc's tree management and Clp, Cgl and Ipopt. Figure 1 measures re-use in lines of code. The authors say the heuristics for non-convex problems "would not have been possible if the source code of the components had not have been available". His individual role is not separated.

---

## Contradictions (kept, not reconciled)

1. **Account dates.** The brief has `johnjforrest` for 2002–2020 and `jjhforrest` from 2020. In the GitHub record `jjhforrest` was created 2014-03-31 and comments from 2017-11-20; `johnjforrest` was created 2019-06-14 and has one comment, from 2020. The 2002–2020 / 2020– split holds for commit identities, not for the accounts (S7, S1–S3).
2. **Comment count.** 461 in the brief; 486 found here, of which 481 are in the five coin-or repositories. The difference is explained by Clp.old plus four non-core repositories [inferred].
3. **Notes versus code.** "At present I never check on forward progress" (2002 note, still in HEAD and copied into Abc in 2012) against ClpSimplexProgress, added 2002-09-17.
4. **Self-description versus measured value.** Idiot: "no merit apart from the fact that it gets an approximate solution to some classes of problems" (2002). Galabova & Hall measured a geometric-mean speed-up of 1.9 for Clp's primal on 30 problems, with Clp faster than commercial codes on some (S19). He himself turns to Idiot again for set partitioning (Cbc#837, 2026).
5. **Abc.** "partially successful … not kept up to date" (2023) against "the answer may be as simple as abc" (2026).
6. **Blame versus Authors lines.** Blame gives Forrest 92% of ClpPdco (Authors line: Tomlin) and 86% of ClpPESimplex (Authors: Omer). It gives Strayer up to 89% of Cbc files whose code predates his 2009 refactor. Line shares and authorship disagree; both are kept in §0.2.
7. **Stated release rule versus earlier practice.** "not put anything interesting into stable - just fixes" (2023). Earlier: "I have added to stable a secondary status which says the problem was found infeasible by presolve" (Cbc#381, 2022). Later: "I am modifying stable - any modifications would be on -D........ in build" (Cbc#837, 2026).
8. **Stated intent versus practice on logs.** "This is to stop me (JJF) messing about too much.  Tuning changes should be noted here." (2005), yet the log stops in 2007.
9. **Self-assessment versus credit.** "I can't do elegant code (or useful comments)" (CoinFactorization note) against the COIN-OR Cup's "world-class open-source tools" (S27).

## Gaps

- **Mailing lists not reached**: list.coin-or.org (Clp/Cbc archives, 2002–2019), where most of his pre-GitHub support lived. Galabova & Hall cite a 2014 public e-mail of his on Idiot that I could not read. Recorded as not reached; not routed around.
- **fastercoin.com "Never Asked Questions" page (2012)**, cited by Huangfu & Hall as the only Aboca documentation: not reached (parked domain). web.archive.org was not used.
- **ISMP 2012 Aboca talk**: no slides found (1 WebSearch). The DIMACS 2006 Clp and Cbc slides were not found on an official host. The Cbc deck was seen only as a third-party text mirror (S34), which may not match the original.
- **Experiment sections of his papers**: unread. The 1972, 1974, 1976, 1990 and 1992 ×3 papers, 2002, 2006 ×2 and 2007 are paywalled; only abstracts or metadata were checked. His IBM-era baselines, test sets and timing protocols are therefore known only from the ICM 1998 tables and abstracts.
- **OSL and OSL's MIP, UMPIRE, LAMPS**: no code and no process record found. Two OSL pieces are claimed in Clp's notes (§0.2).
- **Sbb before 2004 and the 2004 "competition"**: Cbc's README of 2004-10-29 says "While the competition is on no work is being done on the cbc driver"; which competition this was is not identified.
- **Cgl** was not cloned. Authorship of CglProbing, CglPreProcess and CglGomory is unresolved.
- **PR inline review comments** (`/pulls/comments`) were not checked; the unauthenticated GitHub API rate limit was exhausted.
- **DBLP** (pid 08/3168) returned a bot check; not bypassed. OpenAlex was used instead.
- **"IBM Burlington problems"** (2002): what the models were is not stated anywhere I read.
- **IBM retirement date**: not determined. Commit volume dips in 2010 and 2012 only.

## Sources

Code and project records:

- S1. coin-or/Clp git repository, full history 2002-07-30 → 2026-11-02 (first commit `b4253486`; HEAD `87446523`): https://github.com/coin-or/Clp. Read: notes in ClpSimplexDual/Primal.cpp, Idiot.hpp, ClpNonLinearCost.hpp, ClpPredictorCorrector.hpp, ClpInterior.hpp, ClpPdco.hpp, ClpPESimplex.hpp, ClpHelperFunctions.hpp, Abc*.hpp/.cpp, ClpSolve.cpp, ClpMain.cpp (version log), CbcOrClpParam.cpp (help texts), examples/sprint.cpp, examples/ekk.cpp, m4 Aboca macro. Primary.
- S2. coin-or/CoinUtils git repository, 2002-09-16 → 2026-10: https://github.com/coin-or/CoinUtils. Read: CoinFactorization.hpp, CoinOslFactorization*.hpp/.c, CoinHelperFunctions.hpp, CoinPresolveDoubleton.cpp. Primary.
- S3. coin-or/Cbc git repository, 2004-10-29 → 2026-11-04 (HEAD `001b861c`): https://github.com/coin-or/Cbc. Read: README.md, CbcSolver.cpp version log, CbcGeneralDepth.cpp, CbcSymmetry.cpp/.hpp, CbcHeuristicDW.hpp, CbcModel.hpp, src/Attic/unitTestClp.cpp, Docs/ in the 2005 history. Commits `65e778e1`, `729e7510`, `8d0c2d5e`, `cfe3e34c`, `9a2048ca`. Primary.
- S4. My blame and file-creation analyses of S1–S3 (`git blame -w`, last-touch line shares; `git log --diff-filter=A`), run 2026-11-05. Derived from primary records.
- S5. GitHub issue and PR conversation comments by jjhforrest (and one by johnjforrest), via api.github.com `/repos/coin-or/{Cbc,Clp,CoinUtils,Cgl,Clp.old}/issues/comments`, harvested 2026-11-05: 3,930 comments read by script, 481 his. URL form: https://github.com/coin-or/<repo>/issues/<n>. Threads cited:
  - Cbc #202, 204, 215, 219, 282, 286, 297, 301, 333, 338, 342, 381, 416, 446, 451, 462, 479, 481, 489, 494, 497, 519, 520, 543, 545, 562, 563, 572, 591, 599, 608, 618, 628, 633, 639, 658, 661, 668, 689, 697, 703, 704, 710, 714, 717, 719, 729, 741, 748, 750, 751, 752, 753, 759, 769, 774, 784, 807, 809, 837
  - Clp #23, 91, 103, 125, 132, 138, 151, 165, 188, 262, 274, 277, 299
  - CoinUtils #94, 146, 147, 206, 210
  - Cgl #63, 81, 99
  - Clp.old #11–#55 (the 2018-11-12 triage; #40 quoted)

  Primary.
- S6. His comments and issues outside the five repositories: coin-or/Bonmin#31 (2023-01-25), coin-or/SHOT#159 (2022-07-08), coin-or/Osi#193 (2024-07-08); scipopt/papilo#59 and #62 (issues opened by him, 2024-09-06 and 2024-09-10): https://github.com/scipopt/papilo/issues/59 and /62. Primary.
- S7. GitHub search API (`commenter:jjhforrest`, `commenter:johnjforrest`) and user profiles at api.github.com/users/jjhforrest and /johnjforrest (created_at 2014-03-31 and 2019-06-14), fetched 2026-11-05. Primary records.

Papers. Identifiers were checked through the Crossref API on 2026-11-05; read level is given for each.

- S8. J. J. H. Forrest, J. A. Tomlin, "Updated triangular factors of the basis to maintain sparsity in the product form simplex method", *Math. Programming* 2(1):263–278, 1972, DOI 10.1007/bf01584548. Metadata only; not read. Primary.
- S9. J. J. Forrest, D. Goldfarb, "Steepest-edge simplex algorithms for linear programming", *Math. Programming* 57(1–3):341–374, 1992, DOI 10.1007/bf01581089. Abstract read on https://link.springer.com/article/10.1007/BF01581089; full text not read (no open copy found). Primary.
- S10. J. J. H. Forrest, J. A. Tomlin, "Implementing the simplex method for the Optimization Subroutine Library", *IBM Systems Journal* 31(1):11–25, 1992, DOI 10.1147/sj.311.0011. Abstract only (OpenAlex, via publications/abstracts.md). Primary.
- S11. J. J. H. Forrest, J. A. Tomlin, "Implementing interior point linear programming methods in the Optimization Subroutine Library", *IBM Systems Journal* 31(1):26–38, 1992, DOI 10.1147/sj.311.0026. Metadata only. Primary.
- S12. J. J. H. Forrest, J. A. Tomlin, "Vector processing in simplex and interior methods for linear programming", *Annals of Operations Research* 22(1):71–100, 1990, DOI 10.1007/bf02023049. Metadata only. Primary.
- S13. J. J. H. Forrest, J. P. H. Hirst, J. A. Tomlin, "Practical Solution of Large Mixed Integer Programming Problems with Umpire", *Management Science* 20(5):736–773, 1974, DOI 10.1287/mnsc.20.5.736. Abstract read (Crossref record); full text not read. Primary.
- S14. B. T. Denton, J. Forrest, R. J. Milne, "IBM Solves a Mixed-Integer Program to Optimize Its Semiconductor Supply Chain", *Interfaces* 36(5):386–399, 2006, DOI 10.1287/inte.1060.0238. Abstract read (Crossref); full text not read. Primary.
- S15. J. J. H. Forrest, J. Kalagnanam, L. Ladanyi, "A Column-Generation Approach to the Multiple Knapsack Problem with Color Constraints", *INFORMS Journal on Computing* 18(1):129–134, 2006, DOI 10.1287/ijoc.1040.0078. Abstract read (Crossref); full text not read. Primary.
- S16. B. Dietrich, J. J. Forrest, "A Column Generation Approach for Combinatorial Auctions", *The IMA Volumes in Mathematics and its Applications*, 2002, pp. 15–26, DOI 10.1007/978-1-4684-9277-4_2. Metadata only. Primary.
- S17. J. Forrest, R. Lougee-Heimer, "CBC User Guide", INFORMS TutORials in Operations Research (*Emerging Theory, Methods, and Applications*), 2005, pp. 257–277, DOI 10.1287/educ.1053.0020. Metadata only. Its 2005 source files in Cbc's history were read (S30). Primary.
- S18. Q. Huangfu, J. A. J. Hall, "Parallelizing the dual revised simplex method", *Mathematical Programming Computation* 10(1):119–142, 2018, DOI 10.1007/s12532-017-0130-5. Author PDF https://webhomes.maths.ed.ac.uk/hall/HuHa13/HuHa13.pdf; passages on Aboca and the reference list read. Secondary.
- S19. I. L. Galabova, J. A. J. Hall, "A quadratic penalty algorithm for linear programming and its application to linearizations of quadratic assignment problems", arXiv:1804.09172 v1 (2018-04-24), https://arxiv.org/abs/1804.09172. Abstract, §1–3 and §4.2 read. Secondary.
- S20. Cgl source headers through raw.githubusercontent.com/coin-or/Cgl/master/src/ (CglProbing, CglPreProcess, CglGomory, CglDuplicateRow, CglTwomir, CglZeroHalf, CglLandP, CglResidualCapacity, CglMixedIntegerRounding2), fetched 2026-11-05. Primary.
- S21. E. M. L. Beale, J. J. H. Forrest, "Global optimization using special ordered sets", *Math. Programming* 10(1):52–69, 1976, DOI 10.1007/bf01580653. Metadata only. Primary.
- S22. OpenAlex works for author A5061258306 (13 works) and work W2607315627, https://api.openalex.org, fetched 2026-11-05. Secondary.
- S23. J. J. H. Forrest, J. A. Tomlin, "Branch and bound, integer, and non-integer programming", *Annals of Operations Research* 149(1):81–87, 2007, DOI 10.1007/s10479-006-0112-x. Metadata only. Primary.
- S24. R. Anbil, J. J. Forrest, W. R. Pulleyblank, "Column generation and the airline crew pairing problem", *Documenta Mathematica* Extra Volume ICM 1998, III, 677–686, DOI 10.4171/dms/1-3/65. PDF: https://content.ems.press/assets/public/full-texts/books/248/chapters/online-pdf/978-3-98547-546-9-volume-3-chapter-4854.pdf. Read in full. Primary.
- S25. P. Bonami, J. J. Forrest, J. Lee, A. Wächter, "Rapid development of an open-source MINLP solver with COIN-OR", *Optima* 75, 2007, https://mathopt.zib.de/Optima-Issues/optima75.pdf. Venue, year and title checked against OpenAlex W2607315627. Read in part. Primary.
- S26. Crossref REST records for all DOIs above, https://api.crossref.org/works/<doi>, 2026-11-05. Secondary (metadata).

Third-party and web pages:

- S27. COIN-OR Foundation, "COIN-OR Cup 2005 Winners: John J. H. Forrest", https://www.coin-or.org/coinCup/coinCup2005Winner.html, fetched 2026-11-05. Secondary.
- S28. coin-or/Cbc README.md (auto-generated project description), read 2026-11-05. Secondary.
- S29. Clp FAQ, https://www.coin-or.org/Clp/faq.html (answers initialled "DN", dated 08/27/04–09/16/04), fetched 2026-11-05. Secondary.
- S30. Cbc documentation sources in Cbc's git history: Docs/faqcontent.xml and Docs/authors.xml at commit `bc3dea80` (2005-05-03, committed by Robin Lougee; FAQ answers initialled "JF 04/01/05"). Primary.
- S31. DIMACS Workshop on COIN-OR (17–20 July 2006), programme: https://archive.dimacs.rutgers.edu/archive/Workshops/COIN/program.html. Secondary.
- S32. DIMACS Workshop on COIN-OR (2006), abstracts of his CLP and CBC tutorials: https://archive.dimacs.rutgers.edu/archive/Workshops/COIN/abstracts.html. Primary (his abstracts).
- S33. COIN-OR events page for DIMACS 2006, https://www.coin-or.org/events/dimacs06.html: HTTP 404 on 2026-11-05. Not reached.
- S34. Third-party text mirror of J. Forrest, "Coin Branch and Cut: A tutorial", 18 July 2006, https://api.sambuz.com/doc/coin-branch-and-cut-a-tutorial-ppt-presentation-671391. Read only through a WebFetch summary; fidelity to the original unverified. Secondary.
- S35. DBLP person page https://dblp.org/pid/08/3168.xml: a bot check was returned and was not bypassed. Not reached.
- S36. WebSearch result list for "Aboca" "a bit of Clp accelerated" Forrest ISMP 2012 (no relevant hit), 2026-11-05. Secondary.
- S37. WebSearch result list for the Forrest–Goldfarb steepest-edge PDF (no open copy; led to the S9 abstract), 2026-11-05. Secondary.
- S38. WebSearch result list for Forrest Cbc tutorial slides 2006 (led to S31, S32, S34), 2026-11-05. Secondary.
- S39. Local files `references/sources/publications/publications.md` and `abstracts.md` (OpenAlex summary generated 2026-11-05; not user-supplied). Secondary.
- S40. team.json member entry for john-j-h-forrest (brief and chase hints). Used for leads only; every lead used here was re-checked against the sources above. Secondary.

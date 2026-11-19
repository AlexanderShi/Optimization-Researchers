# 05 · Peer critique: blind spots, limits of applicability, contested judgements

> **Researcher**: John J. H. Forrest (also J. J. H. Forrest, John J. Forrest, John Forrest). DBLP pid 08/3168; OpenAlex A5061258306. Not Jeffrey Yi-Lin Forrest or any other Forrest.
> **Dimension**: research agent 05 of 06, peer critique (nuwa research-craft Phase 1). Scope as set in team.json on 2026-11-05: his LP simplex engineering (Forrest–Tomlin update, steepest edge, Sprint, the Idiot crash, Clp, Abc/Aboca, CoinFactorization) and his MIP craft (Cbc; the earlier UMPIRE and OSL MIP codes).
> **Research date**: 2026-11-05
> **Sources consulted**: 100 numbered under "Sources": 25 documents, code records and data records (S1–S25, of which S25 is a secondary relay), 60 GitHub threads read at the comments cited (G1–G60), 11 works identified with their DOI checked but not read (N1–N11), and 4 cited items that could not be reached (U1–U4).
> **WebSearch calls**: 3 of the 7 allowed. Everything else came from known URLs (curl and WebFetch), the arXiv, Crossref, OpenAlex and zbMATH Open APIs, the unauthenticated GitHub search API, and the local clones made by agents 03 and 06 of this workflow (read only).
> **User-supplied material**: none. `references/sources/{papers,talks,essays,software}/` hold only `.gitkeep`; `publications/` holds the OpenAlex harvest. `private/` was not opened. Nothing in this file is from user-supplied material.
> **Transcripts saved**: none.
> **Quotation policy of this file**: to respect copyright, the words of critics, co-maintainers, users and Forrest are paraphrased, never put in quotation marks, and each paraphrase carries an exact locator (page, slide, or GitHub comment id) so that Phase 2 can re-read the original. The file contains one verbatim quotation (in §B, item 4), marked as such. Titles of papers are given verbatim as bibliographic data.

**Method.**
1. *Published critics and rival accounts.* Leads came from team.json, the Huangfu research note (S25), three web searches and the reference lists of the texts read. Every DOI was checked on Crossref, and every arXiv id on arXiv itself (API record or PDF header). Full texts were read only where a legal open copy exists (author or institutional copies, open-access publisher PDFs, OSTI, arXiv, ems.press). One Springer link redirected to an authorization endpoint and was not followed.
2. *Code-first record.* Agent 03 harvested every issue comment in five COIN-OR repositories (coin-or/Cbc, Clp, Clp.old, CoinUtils, Cgl): 3,930 comments. Of these, 481 are by the accounts jjhforrest (480) and johnjforrest (1), dated 2017-11-20 to 2026-11-01 (Cbc 315, Clp 103, CoinUtils 28, Clp.old 21, Cgl 14). The team.json count of 461 matches the total without Clp.old (460) plus one Osi comment: agent 03 (03-process-evidence.md, written in this workflow) reconciles it that way and counts 486 across all repositories, including 5 in Bonmin, SHOT, Osi and PaPILO [observed, S: relayed from 03]. Another 175 comments that jjhforrest wrote on the old TRAC tracker (2006-06-23 to 2016-03-30) were migrated into these issues in 2019. I fetched the issue bodies with GitHub's search API: 178 Cbc, 60 Clp, 18 CoinUtils and 9 Cgl issues with a jjhforrest comment, plus the 2 PaPILO issues he opened. A script filtered the comments for critique vocabulary and for mentions of him, and I then read the threads by hand.
3. *Authorship.* I checked author lines in the source headers (raw files on coin-or master) and file histories (agent 06's mirrors) to tell which criticised code is his.
4. *Benchmarks.* H. Mittelmann's pages as read on 2026-11-05, for context only and never as anyone's words. Older snapshots appear only as relayed by S25.
5. *Public reviews.* I queried the zbMATH Open API for his papers.

**Tags.**
- [stated]: Forrest's own words (GitHub or TRAC comments; co-authored papers, where his voice cannot be separated from his co-authors').
- [practice]: what code, file history, releases or records show.
- [observed]: what a third party wrote (critic, rival, co-maintainer, user, tester).
- [inferred]: my reading, with the basis given. Do not quote it as anyone's view.
- P = primary: I read the passage at the locator given. S = secondary: relayed by another source or agent, or only a record or summary was seen.

**Identity notes.**
- johnjforrest (2002–2020) and jjhforrest (2020–) are Forrest by strong inference (team.json).
- tkralphs (Ted Ralphs), svigerske (Stefan Vigerske) and h-g-s (Haroldo Gambini Santos) are named with these GitHub links in the Cbc README, which lists all three as managing Cbc together with Forrest (S20). Their critiques come from inside the project.
- zxt5 is Xintong Zhou, first author of the Flip paper (S7), by strong inference: the paper is hosted at zxt5.github.io, and a crash log in Cbc#701 shows a home directory that matches the local part of the paper's Waterloo address.
- ashutoshmahajan: the issue links a model file on an IIT Bombay IEOR personal page (~amahajan), and Ralphs greets him as a known colleague. That this is Ashutosh Mahajan is inference.
- christoph-cullmann: logs he posted in Cbc#599 carry an AbsInt Angewandte Informatik GmbH banner, and in Cbc#668 he describes a public ILP regression set checked against CPLEX. That he is an industrial user is inference.
- All other accounts are reported by handle only.

**Whose code is being criticised (checked in this run, S22).**

| Code under critique | Evidence | Label |
|---|---|---|
| Clp simplex, Idiot, Sprint, Abc, CoinFactorization | team.json, code-first lens | his |
| CglPreProcess (Cbc's MIP preprocessing) | file added 2005-02-25 by John Forrest; 191 commits under "John Forrest" and 18 under jjhforrest; no author line (IBM 2005 copyright) | his, by history |
| CglProbing | 155 commits by John Forrest; the 2002 import is by "anonymous"; IBM 2002 copyright | mostly his, by history; first author unknown |
| CoinPresolveDual, CoinPresolveDupcol | both added in 2003 by John Forrest; 36 and 52 commits by him | his, by history |
| CglTwomir | added 2004-10-20 by Oktay Gunluk (IBM); 43 later commits by Forrest | others' design, his maintenance |
| CglCliqueStrengthening, CoinStaticConflictGraph | author lines name Samuel Souza Brito and Haroldo Gambini Santos (2020) | not his |
| CglRedSplit, CoinLpIO | author line names Francois Margot | not his |
| CoinOslFactorization | IBM copyright 1987 and 2009; a port of IBM code | not his by any check here |
| Clp barrier (ClpPredictorCorrector) | not checked in this run | unknown; barrier critiques are not attributed to him |
| Cbc driver and parameter code (CbcSolver, CbcMain1) | not checked file by file; the refactor critiques address the whole driver | shared; do not attribute to him alone |

---

## 0. Summary for Phase 2

| # | Recurring critique (blind spot or limit) | Raised by | Forrest-side answer | Status |
|---|---|---|---|---|
| Q1 | **Forrest–Tomlin (FT) update.** It gives more fill-in than Suhl/Suhl. It has no freedom in pivot choice, so stability can only be checked after the update. Modern FT-like codes do no numerical pivoting | Koberstein 2005 (MOPS school); Huangfu–Hall 2013 (Edinburgh school) | The a-posteriori accuracy test and refactorization come from the FT paper itself (as Koberstein cites it). FT stayed the production update in hsol. No reply by Forrest found | Accepted trade-off |
| Q2 | **Dual steepest edge (Forrest–Goldfarb 1992).** No critique of correctness or applicability found. Rivals adopt and credit it | Bixby (CPLEX side), Koberstein | — | Accepted; credit split varies (C6) |
| Q3 | **Idiot crash.** Undocumented, unexplained constants, no guarantee on the point it returns, his own description incomplete. Yet a major factor in Clp's speed, and too light by default on one API path | Galabova–Hall 2018/2020; users 2020, 2026 | Pointers to header hints; a tuning recipe; in 2026 he looks at Sprint or Abc instead | Analysed by others, not by him |
| Q4 | **Sprint (sifting).** Both camps credit the idea to him. The rival notes that barrier was faster from scratch. Applies only when columns vastly outnumber rows | ICM 1998 (his co-authored text); Bixby 2022 | He still recommends it (2024, 2026) | Credited; no evaluation of Clp's Sprint found |
| Q5 | **Abc/Aboca (parallel dual).** Unpublished, needs an extra btran, not maintained, unused by co-maintainers | Huangfu–Hall 2018; Santos 2019 | Partially successful, written for a 2012 conference, not kept up (2023). Yet he proposes it again (2026) | Conceded, then revived (C5) |
| Q6 | **Clp's relative standing.** Regarded by testers as the best open-source simplex code from 2005 to 2018. Beaten by MOPS (2005), by hsol (2018, with Clp's crash and presolve off), and by HiGHS and others in Mittelmann's LPopt table (2026, old Clp release) | Koberstein; Sandia; Huangfu–Hall; Hall; Mittelmann | None found | Decline in relative standing; benchmark configurations disputed (C4) |
| Q7 | **Clp edge cases.** Infeasible vs unbounded misclassified, missing or odd rays, scaling of empty columns, barrier claiming optimal on an infeasible LP | Vigerske 2026; Santos 2019; researchers 2020–24; an automated verifier 2026 | Diagnosed as tolerance or scaling; fixed within days on master, back-ported on request | Answered case by case |
| Q8 | **Cbc correctness.** Fuzzing campaign: 19 confirmed Cbc bugs, 10 of them soundness bugs. Industrial regressions every few months. Wrong MIPLIB answers on master (2022). Preprocessing is the hot spot | Zhou–Xu–Sun (ICSE 2026); Cullmann; other testers | Fast fixes that switch off, weaken or relax; disclaims code he does not use; questions odd parameter combinations | Fixed on master; releases lag |
| Q9 | **Engineering process and code structure.** Global variables; thread safety behind an #ifdef; magic numbers and special options; C-style parsing; work-in-progress code and debug leftovers; commits without tracker notes; master and stable diverging; thin testing | Ralphs; Vigerske; Santos; users | Ralphs's refactor (merged 2022-01-01). Forrest defends the #ifdef as bug avoidance and points to headers and examples | Partly fixed; 3.0 still unreleased on 2026-11-05 |
| Q10 | **MIP performance, variability, scale.** Noncommercial MILP codes trailed commercial ones (2005). Large swings between versions and runs. Root-node overhead on huge set-partitioning models. Cbc absent from Mittelmann's MILP table (2026) | Linderoth–Ralphs; users; Mahajan; Mittelmann | Luck of heuristics; the nature of integer programming; parameter recipes | Open |
| Q11 | **SOS vs big-M (MIP modelling).** His 2023 view: a tight big-M is slightly better than SOS for indicators. Peer evidence: native SOS2 branching is erratic on large instances | Forrest (stated); Huchette–Vielma | Added an SOS variant anyway | Consistent in part |
| Q12 | **OSL era, rival account.** OSL led until about 1992, then lost airline business to CPLEX's parallel barrier. The dual simplex was not a first-class LP method in practice before the mid-1990s | Bixby 2012, 2016, 2022 | None found | Unanswered |

---

## A. Critiques by theme, with the answer (if any)

### A1. Forrest–Tomlin update (Math. Programming 2(1):263–278, 1972, DOI 10.1007/BF01584548)

- [observed, P] **Koberstein**, PhD thesis, Paderborn, Oct 2005 (S1). He wrote the MOPS dual simplex, whose LU update is Suhl/Suhl.
  - p. 59: because the FT update leaves no freedom in the choice of pivots, stability cannot be controlled during the elimination. It can only be tested afterwards, using an identity proved in the FT paper (he cites pp. 272f.). If the test fails, the iteration is aborted and a refactorization is triggered.
  - p. 60: Suhl/Suhl needs fewer eliminations, so less fill-in is expected than with FT.
  - p. 114: he calls it well known that FT is generally inferior to Suhl/Suhl because of more fill-in, and keeps Suhl/Suhl.
  - pp. 113–114: on very hyper-sparse models, Clp's implementation of the classical FT update is, in his words, quite sophisticated: it makes the permutation update a constant-time operation. He leaves open whether Suhl/Suhl can match that.
- [observed, P] **Huangfu & Hall**, ERGO-13-001, 7 July 2013 (S3; journal version COAP 60(3):587–608, 2015).
  - p. 2: FT, Reid and Suhl–Suhl are the most notable members of the class of updates widely accepted as the most efficient.
  - p. 9: modern descriptions of FT-like updates, and the codes built on them, include no numerical pivoting. Their good numerical behaviour must therefore come from other features: they can drop etas of ill-conditioned bases, and they store less, hence fewer operations.
- [practice, P] The Edinburgh rival code kept FT. hsol lists the FT update among its features (SIOPT 2017 slide 4, S17). The group's own middle product form was not used by pami (ERGO seminar 2016, slide 32, S16). [observed, S] The Huangfu note (S25) reports FT as the HiGHS update too.
- **Answer.** No reply by Forrest found. The safeguard Koberstein describes (an a-posteriori test followed by refactorization) is attributed by him to the FT paper itself. I did not re-read the FT paper.
- **Not read.** The classical comparisons Reid 1982 (N1), Suhl & Suhl 1993 (N2) and the review by Elble & Sahinidis 2012 (N3). DOIs checked; no legal open copy found.
- [inferred] **Limit of applicability.** FT is the speed and sparsity-structure choice, Suhl/Suhl the lower-fill choice. Neither pivots for stability inside the update, so stability rests on the refactorization frequency and on a-posteriori checks.

### A2. Steepest edge (Forrest & Goldfarb, Math. Programming 57:341–374, 1992, DOI 10.1007/BF01581089)

- [observed, P] **Bixby**, Operations Research 50(1):3–15, 2002 (S10).
  - p. 6: the steepest-edge idea for the dual is Goldfarb's (1976). Dual steepest edge in the version-1 form described by Forrest and Goldfarb costs little extra per iteration and is far better than pricing by largest primal infeasibility.
  - p. 14, endnote 7: Goldfarb's 1976 dual algorithm is version 3 in Forrest–Goldfarb.
  - p. 8: on the degen4 fleet model, CPLEX's dual with textbook pricing lost even to primal on the explicit dual. Forrest–Goldfarb supplied the missing piece, steepest edge for the dual, which made the dual simplex a strong general-purpose algorithm.
- [observed, P] **Koberstein** (S1).
  - p. 1: credits Forrest and Goldfarb with a computationally cheap dual steepest-edge rule that, from the early 1990s, made the dual simplex competitive.
  - p. 32: their real accomplishment was exact update formulas for the squared norms (the weights).
- [observed, P] **Bixby, Hausdorff School deck, Sept 2022** (S13, PDF p. 21, slide 23). In the LAU2 story, Forrest's success with primal Devex led CPLEX to implement a dual steepest edge. Goldfarb then suggested a simpler steepest edge, and with it the dual became the clear winner.
- [observed, P] **Bixby, Documenta Math. Extra Vol. ISMP 2012** (S11, p. 113). Dual steepest-edge algorithms, using a variant proposed by Forrest and Goldfarb, are listed among the key LP advances of the early 1990s.
- **Critique.** None of correctness or applicability found in the texts read. Świętanowski (1998, N4) proposed a new steepest-edge approximation (title and Crossref record only; not read). zbMATH holds no review of the 1992 paper (S23).

### A3. The Idiot crash (Clp, 2002 onward)

**Main critic: Galabova & Hall**, arXiv:1804.09172v1, 24 Apr 2018 (S4). Journal version: Optimization Methods and Software 35(3):488–501, 2020, DOI 10.1080/10556788.2019.1604702; not read.
- [observed, P] **Documentation** (p. 1, abstract; p. 2). They present their paper as the first meaningful documentation and analysis of the technique. Apart from the source code, a few source comments, Cbc documentation and a 2014 mailing-list post, the crash had no documentation or analysis. In that post, as they relay it, Forrest called a talk he once gave on it a bad one (U1, not reachable). His comments stress how unsophisticated the crash is.
- [observed, P] **No guarantee on output** (p. 2). The point returned satisfies the bounds and nothing more: no bound on the residual or on the objective error, and not necessarily a vertex. A crossover is needed before primal simplex.
- [observed, P] **His description corrected** (p. 3; pp. 5–6). Forrest describes the objective as a multiple of the LP objective plus a sum of squared infeasibilities. The function actually minimised also has a linear term, which makes it comparable to an augmented Lagrangian. Its later iterations behave like a classical quadratic penalty method.
- [observed, P] **Unexplained constants** (pp. 4–5). Examples: 105 component minimisations per iteration, and weight updates every 3 or 6 iterations, given without justification. The authors assume the algorithm was tuned to pay off when it can and stop early when it cannot. Several extra features had little or no effect in their experiments.
- [observed, P] **Value** (pp. 2, 6–7; Clp 1.16.10, 30 LPs, Intel i7-6700T).
  - Geometric-mean speed-up of the primal simplex: 1.9. At least 2.5 on ten problems; a small slowdown on two. Only on truss was it a poor investment.
  - Default Clp runs primal plus Idiot on ten of the problems. On five other problems Idiot speeds up the primal by at least 2.5, yet default Clp picks the dual; there the dual was at least as fast (geometric mean factor 4.0), so the authors judge that choice justified.
  - Idiot is a major factor in Clp's lead over at least one of Cplex, Gurobi and Xpress on several Mittelmann problems (data of 29/12/17): Linf_520c, the QAP linearizations, self.
- [observed, P] **Limits** (pp. 9, 12–15).
  - Feasible is not optimal: 17 of 30 final points were feasible to 1e-7, but only eight had relative objective error below 1e-2.
  - Accuracy tracks a low condition number of A, not degeneracy.
  - On QAP linearizations (Nugent) it reaches near-optimal points in minutes, where commercial simplex and IPM codes ran out of time or memory on the authors' machine.
  - There is no practical certificate of near-optimality. Applied to the dual, it gave lower bounds too weak to use. Their convergence theorem (exact subproblem minimisation, so every limit point is optimal) is a best case only.
- [observed, P] **Verdict** (p. 15). Forrest's aim, a good start for primal simplex, is achieved on some large LPs. When the crash does not help, Clp detects this without real harm. The crash is also useful in its own right on amenable LPs.

**User critiques and his answers.**
- [observed, P] Clp#163 (G36, 2020-10-23). The same LP took 6 s with the stand-alone clp on Linux and about 10 min through libClp on Windows; Idiot seemed to give a bad start.
  - [stated, P] Forrest (715364666): through OsiClpSolverInterface::initialSolve the code chooses a very light Idiot run that gets nowhere, and more tuning is needed. He posted a fix using ClpSolve options (primal-or-sprint plus a special option).
  - The user then asked whether a guide exists to these secret options (716353975). [stated, P] Forrest: hints are in ClpSolve.hpp (716385696).
- [observed, P] Cbc#837 (G37, opened 2026-10-27 by ashutoshmahajan). Set-partitioning models with 0.5–0.9 million columns and about 700 rows. Cbc spends too long at the root on cuts and dual re-solves. In the reporter's own branch and bound, calling Clp's Idiot at the start and at every node was orders of magnitude faster. He asks for an initialSolve path that can call Idiot without reloading the model.
  - [stated, P] Forrest (6471415135): testing strains his small laptop. He is also trying Sprint, which solved the initial LP faster and may suit branch and bound better. Changes would sit behind compile-time defines in stable.
  - Later he asked for a smaller model and suggested Abc might be the answer (6561854950). Open on 2026-11-05.
- [observed, P] Cbc#728 (G38, 2025-07-08). Ralphs describes Idiot as a crash-basis computation meant to speed up the simplex, and hedges that he thinks so. [inferred] Co-maintainers know Idiot only at a working level; the analysis lives with Forrest and with Galabova–Hall.

### A4. Sprint (sifting)

- [stated-joint, P] **Anbil, Forrest & Pulleyblank, ICM 1998** (S14; co-authored, used here for comparison).
  - p. 681: Forrest introduced the Sprint method; the paper cites his ORSA/TIMS talk of October 1989 (U4). On an American Airlines problem (837 flights, 5.5 million pairings; S/390, 1989), Sprint beat OSL primal and dual as the column count grew.
  - p. 681, method: solve a column subset, price all columns with its duals, keep the basis, add the best columns by reduced-cost buckets plus a random sample.
  - p. 684, self-stated limit: when Sprint performed poorly (after columns generated from Volume-algorithm duals), they crashed the dual simplex from the Volume dual solution instead. On US Airways and Southwest problems (RS6000/590) that was about 9 times faster than dual simplex and 2 times faster than the interior method. Primal simplex was not tried there because it performed very poorly on these problems.
- [observed, P] **Bixby, Hausdorff deck 2022** (S13).
  - PDF p. 14, slide 15: in the 1989 American Airlines challenge (837 rows, 12.75 million columns), the CPLEX-side group (Bixby, Lustig, Marsten, Shanno, Gregory) used an algorithm called sifting, developed by Marsten from an idea of Forrest's. Their observations: barrier was much faster from scratch, and an advanced basis helped near the end.
  - PDF p. 17, slide 19: on an 837 × 1.32 million instance today, sifting took 11.9 s, barrier 25.9 s, primal 93.1 s and dual 416 s.
- [stated, P] **Forrest, Cbc#661** (G57, 2024-08-01). For an LP with 3.17 million variables and 48,301 constraints he points to Clp's sprint.cpp example. He explains that the method was invented for airline problems with about a thousand constraints and an enormous number of variables.
- **Critique.** None found of the method itself. The rival account agrees on the origin, credits a different implementer for its own variant, and reports that barrier was faster from scratch (C7). Both sides state the applicability limit: many more columns than rows. No public evaluation of Clp's Sprint implementation was found (Gaps).

### A5. Abc / Aboca, the parallel dual (2012)

- [observed, P] **Huangfu & Hall**, Math. Prog. Comp. 10(1):119–142, 2018, DOI 10.1007/s12532-017-0130-5 (S2).
  - p. 124: Aboca, presented by Forrest at ISMP 2012 (U3), extends Bixby and Martin. Apart from the released source code, no published reference to it exists.
  - p. 132: on the little evidence available, Aboca needs an extra partial btran that their sip avoids, and it does not exploit the ftran-bfrt or the combined spmv and chuzc1 that sip uses.
  - No measured comparison with Aboca is reported.
- [observed, P] **Inside COIN-OR.**
  - Santos (Cbc#260, G46, 530928661, 2019-09-12): Cbc solves its LPs on one thread. An experimental parallel simplex (Aboca) can be compiled, but he has never used it.
  - Vigerske (Clp#107, G46, 493683119, 2019-05-18): the Abc common header is unused unless Aboca is enabled.
- [stated, P] **Forrest, Clp#262** (G47, 1487041019, 2023-03-28). He advises a user to read only the Clp classes. The Abc versions were a partially successful attempt at a parallel simplex, written more than ten years earlier for a conference and not kept up to date. (Aboca stands for A Bit Of Clp Accelerated; it is also the name of a small Italian village.)
- [stated, P] **Forrest, Cbc#837** (G37, 6561854950, 2026-11-01). He says the answer to Mahajan's request may be as simple as Abc.
- [inferred] A critique he conceded without retiring the tool: Abc remains a build option he still reaches for (C5).

### A6. Clp as a code: standing and documentation

**Benchmarks, in date order (all by others).**
- [observed, P] **Koberstein 2005** (S1, pp. 124, 128). Test: MOPS 7.9 vs Soplex 1.2.1 vs CLP 1.02.02 vs Cplex 9.1. Hardware: Pentium IV 3.2 GHz with 1 GB; Windows XP; CLP compiled with MSVC 6.0.
  - In the system benchmark MOPS clearly beat CLP and Soplex; both of these failed on two of the largest problems.
  - A footnote gives the reason for CLP: it failed to remove its cost perturbation. Soplex hit the 12-hour limit.
  - Cplex had the best overall performance.
  - MOPS and Soplex improved markedly on models pretreated by COIN LP preprocessing, while Cplex got slightly worse. He read this as a sign that MOPS's own preprocessing could be tuned: an implicit compliment to Clp's presolve.
  - Interest: Koberstein is the author of the rival code.
- [observed, P] **What the rival took from Clp** (same thesis). Koberstein credits the COIN dual simplex as the source of several of his techniques:
  - the separation of the bound-flipping ratio test (BFRT) updates from the selection (p. 29);
  - anti-degeneracy strategies (p. 70);
  - cost shifting, which he judged superior when combined with perturbation (p. 75);
  - the BFRT with Harris tolerance (p. 76);
  - perturbation (p. 82).
  - He calls Clp's dualColumn very sophisticated and describes its breakpoint reduction without a heap (p. 101).
  - p. 2, footnote 4: the COIN LP code is the one open-source exception to the gap between published and commercial implementations, but it is largely undocumented and no papers describe its internals.
- [observed, P] **Sandia, Gearhart et al., SAND2013-8847, Oct 2013** (S5). Test: CLP 1.7.4 on 64-bit Windows 7, Intel Core2 Quad 3.0 GHz with 8 GB, against CPLEX, GLPK, lp_solve and MINOS.
  - CLP was the best open-source solver in capability and speed (abstract, p. 3); no open-source solver matched CPLEX (p. 33).
  - Hard set (p. 31): CPLEX solved 17 of 21, CLP 14. CLP's dual timed out on seven problems and stopped on one for numerical reasons; its primal timed out on ten. Geometric mean: 2.5 times CPLEX's on all 21, and 1.74 times on the 14 both solved, although CLP's total time on those 14 was lower than CPLEX's.
  - CLP's interior-point method showed no substantial advantage over its simplex and was dropped from testing (p. 22).
  - CLP was the only solver, CPLEX included, to read every input file without problems (p. 32).
  - CLP 1.14 performed comparably to 1.7.4 (p. 22, appendix E).
- [observed, P] **Hall, PPAM 2011** (S15, slide 34): Clp was written by Forrest at IBM, is the best open-source simplex solver, and Hall is now its project manager (the slide says H, which I read as Hall). Slides 34–41 benchmark his group's ParISS against Clp.
- [observed, P] **Huangfu & Hall 2018** (S2).
  - p. 134: Clp 1.15 is called the world's leading open-source solver. It was run without presolve or crash, because hsol has neither.
  - p. 136: hsol was 2.29 times faster than Clp, with 0.70 of its iterations and 1.60 times its iteration speed.
  - p. 140: pami outperforms Clp, the best open-source simplex solver.
  - SIOPT 2017 slide 13 (S17) lists replacing Clp, with a question mark, among hsol's future aims.
- [observed, S] **Mittelmann's simplex table, earlier snapshots**, as relayed by S25 from the Wayback Machine (not re-checked by me; Wayback not reachable here).
  - 14 Jul 2017: Gurobi 1, Xpress 1.22, CLP 1.69, CPLEX 1.91, Mosek 3.65.
  - 21 Aug 2019: COPT 1, Mosek 3.04, CLP 1.54, HiGHS 5.42.
  - 15 Dec 2021: CLP 8.73, HiGHS 20.1, the rest lower.
- [observed, P] **Mittelmann LPopt, 22 Oct 2026** (S18; i7-11700K; find an optimal basic solution, any method).
  - Scaled shifted geometric mean: COPT 1, Mosek 5.27, XOPT 6.63, HiGHS 12.8, CLP 27.4, GLOP 59.7, SoPlex 101.
  - Solved, out of 65: COPT 65, HiGHS 54, Mosek 53, XOPT 52, CLP 40, SoPlex 34, GLOP 33.
  - [practice, P] The CLP tested is 1.17.7, tagged 2022-01-11. The latest release is 1.17.11 (2026-03-11), and master is unreleased (S21).
- **Answer.** None to any benchmark paper found.

**Documentation critiques and his answers.**
- Who raised it: Koberstein (above); Galabova–Hall (A3); Clp#163 (A3); a user in Clp#262 (G47, 1487262826), who found initialSolve too long to follow and could not tell what ExtraInfo, SpecialOption and the many do-flags mean; Cbc#633 (G42), where the user could not find multipleRootPasses in the user guide.
- [stated, P] Answers: pointers to headers (ClpSolve.hpp), to examples (sprint.cpp, addRows.cpp) and to cbc's command listing. He concedes that the more exotic commands have little documentation (Cbc#633, 1900660563).

**Interface and algorithm-choice complaints.**
- [observed, P] Cbc#301 (G39, 2020): Clp seemed 20 times slower than Cbc on the same LP.
- [stated, P] Forrest (622958180): Clp spent only 14.4 s. Its guess of primal instead of dual cost a factor of two; most of the 415 s went before Clp, probably in a Julia layer adding rows one at a time. The addRows example exists to show why that is a bad idea.

### A7. Clp correctness reports and his answers

| Date | Thread | Reporter | Failure | Forrest's diagnosis and answer [stated, P] | Outcome |
|---|---|---|---|---|---|
| 2019-04 | Clp#103 (G31) | h-g-s (Santos) | LP relaxation of MIPLIB 2017 irish-electricity: Clp ≈ 2,454,773 vs ≈ 2,546,254.6 from Gurobi and CPLEX | A tolerance issue. He gets 2,456,635.2 with largest infeasibility 1.4e-8 (481626346), and suggests the others may be using integer information (481862493) | Reporter closed it as not a bug. [inferred] Closed on a conjecture (C10) |
| 2020-06 | Clp#151 (G35) | mtanneau | Barrier through the C interface segfaults on neos3 | Master now detects that barrier would need too much memory and switches to simplex; by flop count barrier would have taken years. The dualize option is missing from the C interface (640178665) | Open |
| 2020-08 | Clp#157 (G32) | akazachk | Inconsistent values and long re-solves across commits | The model is nearly dual infeasible; with scaling off he found a better value (668076597). The reporter agrees, but still sees a change between commits (668406439) | Open |
| 2022-12 | Clp#251 (G33) | pfetsch (call from SCIP) | getBasics unavailable after barrier with crossover | Barrier lacked a start-finish option; added in master the same day (1345614603) | Confirmed |
| 2024-03 | Clp#286 (G34) | febattista (SYMPHONY) | Farkas rays only after initialSolve, not after resolve | OsiClp assumes branch-and-bound mode, where rays are not built; special option 32 forces them. He asks for examples of wrong rays under scaling or presolve (1985367457). A third party later supplied the sign convention and a wrong-ray example with scaling on (6222429606, 2026-10-16) | Open |
| 2026-06 | Clp#334 (G29) | svigerske | Barrier in Clp 1.17.11 reports optimal on an infeasible LP; master switches to simplex | Ported master's ClpSolve.cpp changes to stable (4833872544) | Fixed the same day |
| 2026-07 | Clp#335 (G29) | svigerske | Primal simplex calls an unbounded LP infeasible, in master and stable | Not very serious: column scales went wrong for objective-only columns, and a skip test had been commented out instead of refined (4876593024) | Fixed in both |
| 2026-10 | Clp#341 (G30) | vera-rubin (an automated verifier, ChipLab) | Default and dual report optimal for an unbounded LP with two free variables | Asked whether a ClpSimplexDual change in master fixes it (6126296695); reporter confirms (6204904313) | Fixed in master |

[inferred] **Pattern.** The reported failures sit at the boundary of infeasibility and unboundedness, in rays, scaling, and barrier fall-backs. His diagnoses name a tolerance or scaling cause. Fixes land within days, with stable back-ports when a co-maintainer asks.

### A8. Cbc correctness: systematic and recurrent counterexamples

**A8.1 Flip** (Zhou, Xu & Sun, *Validating Mixed-Integer Programming Solvers*, ICSE '26, Rio de Janeiro, 12–18 April 2026, pp. 3800–3812, DOI 10.1145/3744916.3787827; S7)
- [observed, P] **Method.** Instances are generated to be feasible or infeasible by construction and run on SCIP, HiGHS, CBC, Mosek and Gurobi. The open-source solvers were built with assertions enabled.
- [observed, P] **CBC results.**
  - Table 1: 21 bugs reported, 19 confirmed, 19 fixed, 0 duplicates, 1 won't-fix.
  - Table 2: of the confirmed bugs, 9 crash bugs and 10 soundness bugs.
  - Table 3: 12 triggered by feasible instances, 7 by infeasible ones.
- [observed, P] **All solvers.** 80 reports, 67 confirmed, 54 fixed. Open-source fix rate 50/60, commercial 4/7. The authors read the larger open-source counts as a sign that commercial solvers get more internal testing before release.
- [practice, P] **On GitHub.** 27 Cbc issues opened by zxt5 between 2025-02-01 and 2026-01-05 carry a Forrest comment. His first reply came the same day to three days later.
- [inferred] The CBC won't-fix is probably Cbc#719 (OSL factorization, below). The paper does not say so.
- [stated, P] **His answers**, in his own diagnosis:
  - Cbc#689 (G18, 2636589428): a tolerance case. A variable at 20.000003, just over the integer tolerance, led the code to infer a bound from an extrapolated cost. He changed the code to use that inference only when the variable is clearly fractional.
  - Cbc#694 (G19, 2764569147): another tolerance case. Strictly, master is wrong too; with scaling off both versions accept a different value; he is unsure what the correct behaviour is. Open.
  - Cbc#704 (G21): no sensible user would combine those options; some initialization was skipped; code adjusted.
  - Cbc#715 (G22): the cut-weakening code used −1e-5 instead of +1e-5.
  - Cbc#719 (G23): he declines to fix it, because the OSL factorization predates COIN.
  - Cbc#720 (G24): he sees no advantage in the preprocess strategy option, but fixed the error.
  - Cbc#737 (G25): CoinPresolveDual treated two singletons in a row without checking whether both were continuous or both binary.
  - Cbc#747 (G26): the feasibility test allowed row violations within tolerance but no bound violations. He added a second, relaxed check that runs when the first says infeasible.
  - Cbc#701 and #711 (G20): he first could not reproduce. He later noted that the default build is optimized and seems to switch off asserts (it defines NDEBUG), and asked how the reporters build (2833344818).

**A8.2 Other systematic reporters (2025–2026).**
- [observed, P] shwhmmmam opened Cbc#750–753 (Oct–Nov 2025). hodangkhoinguyen opened Cbc#827–828 (Oct 2026): a wrong objective with preprocessing, and a feasible model declared infeasible with preprocessing, both reproduced on 2.10.13 and on master. [inferred] The name of one attached file suggests a variable-reflection test, the kind a metamorphic testing campaign would use; no paper was found.
- [stated, P] Forrest, Cbc#751 (G27, 3442690541): a variable fixed at 1 was treated as binary; he never uses the clique-strengthening code and asks someone more knowledgeable to look. (That code is by Brito and Santos; see the authorship table.)
- [stated, P] Forrest, Cbc#828 (G28, 6387969944): a fix may take time if bound changing is to stay efficient; values as large as those in the good solution leave room for a bound to be simply wrong. Open.

**A8.3 Industrial regression reports** (christoph-cullmann: 15 issues with a Forrest comment, 2019-08 to 2025-08)
- [observed, P] **Cbc#668** (G14, 2024-08-27). A wrong ILP result after a master update, disagreeing with CPLEX.
  - Ralphs asked for a git bisect (2314916762). The reporter could not bisect (he builds a CMake mirror) and asked to add his CPLEX-verified ILP set to the automated tests, noting that it finds regressions in Cbc and its companion projects every few months (2315079032).
- [stated, P] **Forrest on Cbc#668.**
  - 2315232721: he keeps many versions of master; the option -cgraph clq falls back to the old cliques. He runs the reporter's files privately through cbc -dirmiplib with a node or time limit, because Cbc does poorly on a few of them.
  - 2320764915: the cause is in CoinStaticConflictGraph after a move to std::vector (uninitialized values, and size() used as an emptiness test). Many standard test models were wrong too. He asked for someone who knows the code better, then patched it himself (commit 917c816, 2024-08-30).
- [practice, P] The regression came from commit 81c370f (2024-08-26, a-andre, pointer arrays replaced by std::vector, CoinUtils PR #240), in code written by Brito and Santos. Santos recommended rolling the change back, because their benchmarks had shown vectors measurably slower (2321795997).
- [stated, P] **Cbc#599** (G16, 2023).
  - 1538115069: the CglPreProcess code needs more thinking; some of it is switched off for now.
  - 1775565254: he found a tolerance problem in CglTwomir (a cut built from a row with a right-hand side of about 3.7e10).
  - 1776769484: his fix was totally safe, but perhaps the cut could just have been weakened; he invites someone who knows that code to look.
  - [observed, P] The reporter bisected to a CoinUtils commit, and found that the compiler version (LLVM 17) also mattered (1770468800, 1774732481).
- [stated, P] **Cbc#639** (G15, 2024-02). The sign-flipping code in CoinPresolveDupcol is complicated and easy to get wrong; he made it try less hard, and invites the author of the changes to fix it (1951373092). [practice, P] The file's history does not obviously show another author (C8).
- [stated, P] **Cbc#741** (G17, 2025-08).
  - 3178755051: he took out an improvement to preprocessing (reductions down to 2×2 models) until it is fixed.
  - 3180540109: he asks whether to restore it, or whether master is now in clean-up mode for the next release.
  - Ralphs hopes master becomes the next release soon (3180569273).

**A8.4 MIPLIB mismatches on master (2022)**
- [stated, P] Cbc#479 (G2, 1025114582): new code behind the define FIXED_BOTH_WAYS had been tested only on larger problems in optimized mode; he took it out.
- [stated, P] Cbc#481 (G1, 1030644005).
  - dano3_5: a printing artefact. Modern coders had replaced printf by std::cout, which dropped digits of the final objective; he went back to printf for that value.
  - rlp1 (22 vs 15): over-aggressive changes to CglProbing.
  - trdnc: he remarks that Gurobi's default optimality tolerance seemed quite high to him (1030799957).
  - Fixed within three days.

**A8.5 The counter-voice**
- [observed, P] Cbc#489 (G44). A user (rsemenoff) claimed that cbc is not rigorously tested (1090570966). Ralphs called that characterization misleading and said Cbc is quite robust in practice (1094375313).
- [stated, P] Forrest: Cbc is normally faster and more reliable than GLPK; the cvxpy interface was not passing the parameters (1092619925). Ralphs: the CyLP layer ignores them.

### A9. Engineering process and code structure (critiques from inside COIN-OR)

- **Thread safety, global variables, #ifdef** (Cbc#332, G3, 2020; open on 2026-11-05).
  - [observed, P] A user could not run CbcMain0/CbcMain1 in parallel threads.
  - Ralphs: global variables break thread safety, and he is removing them (688384661).
  - [stated, P] Forrest: add -DCBC_THREAD_SAFE to the build (688902669).
  - [observed, P] Ralphs asks why that is not the default (688940856). Vigerske: Cbc should be thread-safe always, and he sees no reason for an #ifdef at all (688943958).
  - [stated, P] Forrest (688952405): he does not know when the #ifdef appeared. He presumes its author, possibly himself years ago, was unsure the guarded code was correct and did not want to introduce bugs.
  - [observed, P] Ralphs: the guarded code is a quick hack, which he is cleaning up (688984843). Vigerske: #ifdefs like these in API headers are a sign of unclean code, users cannot be expected to guess the COIN_HAS_* defines, and 2.10 will not be fixed (690076460).
- **Refactor** (PR #374, G4, opened 2021-03-15 by Ralphs; merged 2022-01-01 per Discussion #465, G5).
  - [observed, P] Stated goals:
    - thread safety and no global variables;
    - a structure easier to understand and maintain;
    - one parameter mechanism, separated from Clp;
    - C++ strings and streams for input;
    - all output through message handlers;
    - unified error handling;
    - one library;
    - a modular CbcMain1.
  - Open tasks: replace integer modes and magic numbers by enums; make the obscurely set special options transparent; remove irrelevant #ifdefs; test against master for regressions.
  - The announcement says progress was slow for lack of developer bandwidth, and expects some random side effects with similar overall performance.
- [stated, P] **Discussion #465** (G5, 2022-01-18).
  - Forrest finds that the code behind one parameter has been missing from stable for years.
  - A pivot-and-fix heuristic can be called but does nothing under the default defines, and it contains a debug print that shows the code is unfinished.
  - [observed, P] Vigerske: the pivot-and-complement parameter has no effect, and its code compiles only if JJF_ZERO is defined. If pivot-and-fix does not really exist, its parameter should go too.
  - [inferred] Dead options and JJF-named guards are the very pattern the refactor targets. Authorship of these heuristics was not checked.
- [observed, P] **Smaller process critiques from Vigerske.**
  - Cbc#101 (G6, 2019): Forrest patched the command-line parser twice (2013, 2015) rather than replacing it; C-style parsing is, as Vigerske puts it, what the project's main developer prefers; requiring -solve is a design decision.
  - Cbc#197 (G7, 2019): fixing compiler warnings changed the algorithm, so Vigerske asks Forrest to check.
  - Clp#101 (G8, 480166389, 2019): a contributor's patch undid Forrest's change 58cf499a; Vigerske asked him about it because he could not see the reason for either change, and the contributor then withdrew that part. [inferred] The rationale for the original change was not recorded where a co-maintainer could find it.
  - Clp#40 (G9, 2019): a fix was committed without a note on the tracker.
  - Clp#97 (G10, 2019): Forrest's changes reached stable/1.17 but not trunk; Vigerske merged them.
- [stated, P] **Leftovers he owned.**
  - Clp#128 (G11, 569916055, 2019): debug printing in release 1.17.3 was work in progress; he apologised, and Vigerske removed it.
  - Cbc#759 (G49, 3707927443, 2026): an assert left over from debugging something else.
  - Cbc#748 (G49, 3426498888, 2025): a last-minute change broke compilation, and the next commit fixed it (as Vigerske reported, 3426462301); Forrest called himself an idiot.
- **The double solve** (G4, 2021-05-13).
  - [observed, P] A solve executed twice changed the optimum from 0.1 to 0.0999899.
  - [stated, P] Forrest: the solve drastically alters the CbcModel the user set up, and making it usable again would be much work and of little use (840636070). He then explained the mechanism (a stored cutoff; the solver no longer in sync; dual values wrong) and offered to recompute the objective (840686214).
  - [observed, P] Vigerske accepted, noting that it is by design if Cbc changes the user's own problem rather than a copy (840654798).
- [observed, P] **Testing.**
  - Cbc#204 (G12, 2019): Ralphs says release testing did not include the examples, and perhaps it should.
  - Cbc#668: the reporter's request to add his verified ILPs to the automated tests was met by Forrest's private test directory (A8.3).
  - [practice, P] CI on GitHub Actions was built by other contributors and Ralphs in 2025 (Cbc#728, G38).
- **Releases.**
  - [observed, P] Cbc#367 (G13, 790870432, 2021): Ralphs notes that the reporter runs 2.10.5 from Ubuntu while Forrest tests on master, and that master may take a while to reach a release and the distributions.
  - [practice, P] Release tags: Cbc 2.10.0 (2019-02-23) to 2.10.13 (2026-03-11); Clp 1.17.0 (2019-02-22) to 1.17.11 (2026-03-11). The README changelog has listed Release 3.0 as in preparation since at least 2020-03-22 (first matching commit in the README history, S21).
  - [stated, P] Forrest (Clp#358, G56, 6373912507, 2026-10-23): the main thing is to get next moved to master.
- [observed, P] **Praise from inside.**
  - Santos (Cbc#310, G45, 638884565, 2020): CbcMain0 and CbcMain1 are the recommended entry points, because Forrest has tuned the parameters there.
  - Vigerske (Cbc#231, G58, 501332643, 2019): the Osi core developers had refused time limits through long, fruitless discussions; Forrest's commit settled it.
  - Ralphs: Cbc is robust in practice (A8.5).

### A10. MIP performance, variability and scale

- [observed, P] **Linderoth & Ralphs**, COR@L technical report, Dec 2004, revised Jan 2005 (S6); book chapter 2005, DOI 10.1201/9781420039597.ch10.
  - p. 1: noncommercial MILP tools generally cannot match the speed or robustness of commercial ones.
  - p. 27: Forrest began CBC as a lightweight branch-and-cut code to test CLP. It had grown sophisticated enough to count as a solver framework. There is no user manual, but the examples and the source are well commented.
  - p. 28: among the reviewed black-box solvers it offers one of the fullest sets of bound-improving techniques. Column generation is not supported. The default search is depth-first until the first feasible solution.
  - Benchmark (pp. 41–43): gcc 3.3, RedHat 7.3, Pentium III 1133 MHz with 512 MB, 2-hour limit, default settings, 122 instances. bonsaiG and MINTO were fastest most often. MINTO and CBC proved optimality on the largest share. On instances nobody solved, SYMPHONY and GLPK found the best feasible solutions, which the authors take as a sign that the primal heuristics of the noncommercial codes were relatively ineffective.
  - Interest: co-author Ralphs later co-manages Cbc (S20).
- [practice, S] **Possible answer.** The CBC User Guide (Forrest & Lougee-Heimer, INFORMS TutORials 2005, pp. 257–277, DOI 10.1287/educ.1053.0020; N11, not read) appeared after the report noted the missing manual. Whether it was a response is unknown.
- [observed, P] **MIPLIB 2017** (Gleixner et al., Math. Prog. Comp. 13(3):443–490, 2021; S9, p. 462, Table 6). CBC 2.9.8 with 4 threads was one of the eight solvers used to collect performance data. No per-solver ranking was read.
- [observed, P] **Mittelmann's MILP benchmark, 28 Oct 2026** (S19). The table runs COPT, three SCIP variants, two HiGHS variants and Optverse. Cbc is absent. When and why it left the table is unknown, because the Wayback Machine is not reachable here.
- **Variability and scale, with his answers.**
  - [observed, P] Cbc#494 (G40, 2022): from 2.10.4 on, Cbc needs over 1000 s to find an optimum that 2.10.3 found in 30–40 s.
    - [stated, P] Forrest (1106535274): the older version was lucky, needing fewer nodes to reach its best solution. Whether the many heuristics succeed depends on many factors; even compiler options matter. A quick start from solving without the objective helped. He will look at the DW heuristic.
  - [observed, P] Cbc#633 (G42, 2024): run times of 3–4 s or 300–600 s.
    - [stated, P] Forrest (1898163112): not a bug, but a feature of integer programming. He let SCIP run overnight on the model (10 hours, depth over 4,000) and saw objective variation from tolerances. A recipe (an allowable gap plus multiple root passes) solved it at the root.
  - [observed, P] Cbc#381 (G41, 2021–22): Cbc ran 7 minutes on a problem that presolve had proved infeasible in under a second.
    - [stated, P] Forrest gives the design reason: users want to know why a problem is infeasible, so Clp re-solves without presolve (814926662). The option he suggested worked in Clp but not in cbc, which he called his own mistake; he added a secondary status to stable (1077751744). The primal is better than the dual at proving infeasibility (1079059527).
  - [stated, P] Cbc#305 (G60, 634599510, 2020): a very easy but very large problem was slow because of probing and a slow LP re-solve after tightening.
  - Cbc#837: see A3.

### A11. Modelling judgement: SOS vs big-M (MIP)

- Background: Beale & Forrest, *Global optimization using special ordered sets*, Math. Programming 10(1):52–69, 1976, DOI 10.1007/bf01580653. This is his most cited paper (OpenAlex), with Beale as first author.
- [stated, P] **Cbc#572** (G43, 2023-02-15).
  - 1431665750: for indicator constraints he thinks a tight big-M is slightly better than SOS. Cbc master's indicator code tightens big-M values but has never really been tested on real problems, and has many bugs he will fix. The SOS approach is elegant but weaker, and it cannot make a constraint active when the indicator is 0. He would add an SOS version if convinced of its merit.
  - 1433390898: he added one the next day, clumsy for 0-indicators.
- [observed, P] **Huchette & Vielma**, arXiv:1708.00050v3 (2019), published in Operations Research 71(5):1835–1856, 2023, DOI 10.1287/opre.2019.1973 (S8).
  - p. 15: native SOS2 branching (they trace it to Beale and Tomlin 1970) in CPLEX 12.7.0 does very well on easier instances, but its variability is extreme: with 28 segments it timed out on 80 of 100 large-network instances.
  - p. 17: Gurobi 7.0.2's native SOS2 branching is relatively better on small and medium functions, but timed out on 98 of 100 instances with 59 segments.
  - Their zig-zag formulations do better on the large ones.
- [inferred] This targets SOS2 branching as commercial codes implement it, not the 1976 paper or Cbc. It agrees with his 2023 preference for formulations over SOS for indicators.

### A12. The OSL era as told by the rival (CPLEX side)

- [observed, P] **Optima 101** (Sept 2016, interview with Bixby, PDF p. 3; S12).
  - OSL was clearly better than CPLEX at first. CPLEX caught up in LP around 1992, and its dual matured in 1994.
  - Asked whether OSL then had dual steepest edge, Bixby answers that the dual of that time was only a weak tool for re-optimization inside MIP, not a first-class LP algorithm.
  - Airlines on IBM hardware and OSL saw no reason to switch, until a merger study needed speed and the SGI parallel barrier was about 40 times faster.
- [observed, P] **Hausdorff 2022** (S13, PDF pp. 18–19). The SGI-CPLEX barrier was about 40 times OSL's. In the AA–US Air due diligence, OSL took 3–4 hours and SGI-CPLEX 5 minutes. Parallel barrier became the standard.
- [observed, P] **Credit to Forrest from the same rival.**
  - Documenta 2012 (S11, p. 113): OSL, developed mainly by Forrest and Tomlin, and CPLEX were the dominant LP codes of the early 1990s.
  - p. 110: the LP updates of the 1970s generation built on the FT variant of Bartels–Golub.
  - OR 2002 (S10, p. 6): LAMPS was written independently by Forrest, and with UMPIRE and others such systems dominated LP computing into the late 1980s.
- **Answer.** None found. Who wrote OSL's barrier is not established here. (Forrest is first author of the 1992 IBM Systems Journal paper on OSL's interior-point implementation, but that does not show code authorship.)
- [inferred] The rival's critique targets OSL's barrier speed and market position, not Forrest's simplex work, which the same rival credits (FT variant, dual steepest edge, the sifting idea).

---

## B. How he answers criticism (the pattern across A1–A12)

1. **Reproduce first, on his own build.** He asks how the reporter built the code, and offers -debug create and -debug debug.file runs to compare a good and a bad version (Cbc#668, 2648298610; Cbc#711, 2833344818). [practice, P]
2. **Name a mechanism, usually a tolerance, a scaling effect or an unsafe inference, and explain it in plain arithmetic** (Cbc#689, #747; Clp#335, #103). [stated, P]
3. **Fix fast, on master.** On 256 native GitHub issues in Cbc, Clp, CoinUtils and Cgl that others opened and he commented on (2017-11 to 2026-11, 7 TRAC migrations excluded), the median wait for his first comment was 1 day: 73% within a day, 88% within a week, 15 after more than 30 days. He back-ports to stable when a co-maintainer asks (Clp#334, #335). [practice, P] Caveat: issues he never commented on are not in this count.
4. **When a clever reduction misfires, retreat to the safe version.** He switches it off, weakens it, adds a relaxed second check, or takes the improvement out (Cbc#599, #639, #741, #747, #562; Cgl#81). This file's one verbatim quotation, from Forrest on Cbc#639 (G15, comment 1951373092, 2024-02-18): "I have modified so that it does not try as hard." [stated, P]
5. **Say plainly when the code is not his, or when he does not use it, and ask the owner** (CglTwomir in Cbc#562 and #599; clique strengthening in Cbc#750–751; CoinLpIO in CoinUtils#210; the conflict graph in Cbc#668). [stated, P]
6. **Push back on implausible use**: parameter combinations no sensible user would choose (Cbc#704), test files that look designed to break the code (Clp#245, 1299010234), options with no advantage (Cbc#720). [stated, P]
7. **Reframe performance complaints** as properties of integer programming, the luck of heuristics, or the calling interface (Cbc#633, #494, #301, #411). This is sometimes wrong. In Cbc#411 (G54) he first agreed it was a bug, then put it down to a Julia failing (851943801). The same day odow reproduced it through the C API (852496181), and Ralphs routed the fix to the 3.0 parameter mechanism (852658246). [stated, P; observed, P]
8. **Concede his own slips at once and plainly.** Examples: the wrong option (Cbc#381); three successive diagnoses within one day (Cbc#543, G50: 1253875771, 1253931247, 1253941322); a broken commit (Cbc#748); a forgotten debug assert (Cbc#759); work in progress shipped in a release (Clp#128). [stated, P]
9. **Decline legacy code outside his scope** (Cbc#719: the OSL factorization predates COIN). [stated, P]
10. **Answer documentation complaints with pointers to headers and examples**, not with documents (Clp#163, #262; Cbc#633, #661). [practice, P]
11. **Defend a defensive #ifdef as bug avoidance** (Cbc#332), where co-maintainers see unclean code (C9). [stated, P; observed, P]

## C. Critiques he issued about others (his yardsticks)

- [practice, P] **PaPILO**, SCIP's presolve library (G55; issues he opened on scipopt/papilo, 2024-09).
  - #59: a presolver ran for over a day (killed after about 2,256 minutes of wall time). He located the loop in ParallelColDetection, offered a crude cap on a counter, and said he did not know the code well enough for a real fix.
  - #62: a wrong answer (papilo −4102 vs SCIP −91,439). He reduced it to a small MPS file, showed with a one-line diff (one lower bound) that a good and a bad file differ in result, and pointed at one large upper bound (14,651,392) as the likely cause.
  - Both issues were closed within one to three days.
  - [observed, S] Context relayed from 03-process-evidence.md: at the time he was hooking PaPILO into CglPreProcess behind a compile-time define (2024-09-10), so these reports came from evaluating a rival's presolver for reuse.
  - [inferred] His craft here: a second solver as the reference, a minimal instance, a one-line diff.
- [stated, P] **Literature**: a search on dual pivoting rules did not impress him (Clp#262, G47).
- [stated, P] **Tolerances and gaps.** Gurobi's default optimality tolerance looked high to him (Cbc#481, G1). In Cbc#703 (G59, 2813395609) he notes that a HiGHS optimum was 6,000 worse than Cbc's because of a 0.01 gap, while Cbc's default gap is 0. [inferred] Exactness at tight tolerances is his yardstick.
- [stated, P] **Modernization.** The move from printf to std::cout had hidden digits of the final objective, and he restored printf for that value (Cbc#481).
- [stated, P] **Elegance vs strength.** SOS is elegant but weaker than a tight big-M for indicators (Cbc#572, G43).

## D. Mapping to the seven layers (framework §一)

| Layer | What the critiques show | Items |
|---|---|---|
| 1 Taste | He values exact answers at tight tolerances, and practical speed over elegance, documentation and analysis. Peers value code structure, thread safety, documentation and published analysis | A3, A9, A11, C |
| 2 Problem choice | His problems come from users (airlines, now GitHub reporters). Critics find the classes where his defaults fail: huge set partitioning, edge-case LPs, assert-enabled builds | A3, A4, A7, A8, A10 |
| 3 Idea generation | Ideas born in production use (Sprint, Idiot, Abc) and left unpublished. Others supplied the analysis: Galabova–Hall for Idiot, Huangfu–Hall for Aboca | A3–A5 |
| 4 Execution | A one-person core with experimental #ifdef guards, master-first fixes and private regression directories. Peers ask for continuous integration, thread safety and releases | A8, A9 |
| 5 Judging results | Standing is decided by others' benchmarks, often rivals'. His own correctness checks lean on a second solver and on MIPLIB values; his diagnoses are tolerance-based. His blind spot is optimized-mode testing on larger problems, which hides asserts and small-case errors (Cbc#479, #711) | A6–A8 |
| 6 Communication | No paper of his on these codes' internals was found (OpenAlex lists nothing after 2007; the 2005 CBC User Guide is the one text on Cbc). The evidence lives in code, issue replies and talks; the documentation gap is criticised repeatedly | A3, A5, A6 |
| 7 Organisation | COIN-OR maintainers (Ralphs, Vigerske, Santos) refactor and package around him in a volunteer project; he works on a small laptop | A9, F |

## E. Failures, abandoned directions, retracted or softened claims

- **Abc**: a partially successful attempt, not maintained (A5).
- **Indicator code** (big-M): never really tested on real problems (A11).
- **Dead heuristics**: pivot-and-fix and pivot-and-complement options without effect, and unfinished code (A9).
- **Preprocessing improvements switched off after wrong answers**: FIXED_BOTH_WAYS (2022); CglPreProcess code (2023); CoinPresolveDupcol made less aggressive (2024); the 2×2 improvement (2025) (A8).
- **Thread safety through a define**: open since 2020 (A9).
- **Release 3.0**: in preparation since at least 2020 (A9).
- **Retracted judgements**: Cbc#411 (blamed Julia); Cbc#381 (wrong option); Cbc#543 (three diagnoses in one day); Cbc#701 (could not reproduce, then the NDEBUG explanation).
- **OSL factorization port**: he declined to maintain it (A8.1).
- **His papers**: no retraction or erratum found. zbMATH holds summaries but no reviews for the 1972, 1974, 1976 and 1992 papers (S23; a limited check).

## F. Era and resource context of the critiques

- **1972 (FT)**: product-form simplex codes on mainframes (Scicon, per team.json). Bixby places Tomlin and Forrest in Beale's lineage (Documenta p. 109).
- **1989–1992 (Sprint, dual steepest edge, OSL)**: IBM Research. Machines: S/390 (ICM 1998) and the IBM 3090, for which OSL's simplex was redesigned (zbMATH summary of the 1992 IBM Systems Journal paper, S23). The rival ran on Cray and SGI hardware. Airline crew models had millions of columns (A4, A12).
- **1998**: RS6000/590 (the Volume crash).
- **2002–2005 (Clp and Cbc at IBM and COIN-OR)**: the critics' hardware was a Pentium IV with MSVC 6.0 and CLP 1.02.02 (Koberstein), and a Pentium III with a 2-hour limit (Linderoth–Ralphs).
- **2011–2018**: Clp is the open-source reference. Hall manages Clp (2011) while his group builds hsol, aimed at replacing it (2017). Abc was written for ISMP 2012.
- **2013**: Sandia tests on a Core2 Quad under Windows 7 (CLP 1.7.4 and 1.14).
- **2017–2026**: Forrest retired from IBM Research (Cbc README). A volunteer project, by its own README. His machine is a small laptop (Cbc#661 in 2024, Cbc#837 in 2026). The critics are now automated (Flip, ChipLab), industrial (AbsInt) or in-project. Releases stay on 2.10.x and 1.17.x while master moves.

---

## Contradictions (kept, not reconciled)

- **C1. Documentation.** Koberstein (2005, p. 2, fn. 4): the COIN LP code is largely undocumented, with no papers on its internals. Linderoth–Ralphs (2005, p. 27): CBC has no manual, but its source and examples are well commented. Different codes (Clp vs Cbc), same year.
- **C2. Reliability of Cbc.**
  - A user (2022): not rigorously tested.
  - Ralphs (2022): robust in practice.
  - Forrest (2022): normally faster and more reliable than GLPK.
  - Cullmann (2024): regressions every few months.
  - Flip (2025–26): 19 confirmed CBC bugs, 10 of them soundness bugs.
- **C3. Idiot.**
  - Forrest's account, as relayed by Galabova–Hall: unsophisticated; he once gave a bad talk on it; it minimises the objective plus squared infeasibilities.
  - Galabova–Hall: a more general function with a linear term; a major factor in Clp's performance; near-optimal on QAP linearizations.
  - Mahajan (2026): very fast, and orders of magnitude better for branch and bound on set partitioning.
  - Clp#163 (2020): the default light Idiot on the OsiClp path gets nowhere.
- **C4. Benchmarks measure different Clps.**
  - Huangfu–Hall ran Clp without presolve or crash, which switches off the Idiot crash that Galabova–Hall show to be a major factor.
  - Mittelmann runs CLP 1.17.7 (2022) while fixes land on master.
  - Koberstein ran CLP 1.02.02 built with MSVC 6.0.
  - None of these says what a current, fully configured Clp would score.
- **C5. Abc.** Not kept up to date (2023) vs perhaps the answer (2026).
- **C6. Credit for dual steepest edge.** OR 2002 credits the published Forrest–Goldfarb approach as the final piece, with the idea traced to Goldfarb 1976. The 2022 Hausdorff deck credits Forrest with success using primal Devex and Goldfarb with suggesting the simpler steepest edge that CPLEX adopted.
- **C7. Sprint/sifting.** Both accounts concern a 1989 American Airlines crew model with 837 rows (5.5 million columns in ICM 1998, 12.75 million in the 2022 deck). ICM 1998 says Forrest introduced Sprint, and compares it only with OSL's primal and dual, both of which it beats. The 2022 deck says Marsten developed sifting from Forrest's idea, and that barrier was much faster from scratch. They agree on the origin of the idea; they differ on who implemented the method that was run, and only the rival brings barrier into the comparison.
- **C8. Who caused the CoinPresolveDupcol regression (Cbc#639).** Forrest invites the author of the changes to fix it. The file's history on all refs of the CoinUtils mirror, January 2019 to February 2024, shows content commits only under his name (2020-05 to 2021-08) and formatting commits by others. Unresolved: the culprit may lie in another file, or in a branch not mirrored.
- **C9. #ifdef guards.** His rationale: avoid introducing bugs in code whose correctness is uncertain. Vigerske and Ralphs: unclean code, a quick hack; Cbc should always be thread-safe.
- **C10. Clp#103.** He judged a lower LP objective to be a tolerance matter and guessed that Gurobi and CPLEX used integer information. The reporter closed the issue. No independent check was found.
- **C11. Dual steepest edge in OSL.** Bixby (2016) says the dual was then only a weak MIP tool, and that around 1993/94, at an Oberwolfach meeting, he told a speaker on airline problems that they should be using the dual simplex with steepest edge. Forrest and Goldfarb had published it in 1992, and Forrest led OSL. Whether OSL's default LP solve used dual steepest edge at that time is not established.

## Gaps

- **Published exchanges.** No comment-and-reply exchange was found on FT 1972, Forrest–Goldfarb 1992, UMPIRE 1974 or Beale–Forrest 1976. zbMATH shows no reviews. No referee reports are public.
- **Identified but not read** (DOIs checked; no legal open copy, or no time): Reid 1982 (N1); Suhl & Suhl 1993 (N2); Elble & Sahinidis 2012 (N3); Świętanowski 1998 (N4); Koberstein 2008 (N5); Koberstein & Suhl 2007 (N6); Fukasawa & Poirrier 2019 (N7); Mittelmann 2020 (N8); MIPLIB 2010 (N9); Lougee-Heimer 2003 (N10); the CBC User Guide 2005 (N11).
- **Not reachable**:
  - list.coin-or.org (unreachable per team.json, 2026-11-05; not retried): Forrest's 2014 Idiot post (U1) and every Clp/Cbc mailing-list critique from 2002 to 2017.
  - fastercoin.com (parked domain per team.json): his Never Asked Questions page (U2).
  - The ISMP 2012 Aboca talk (U3) and his 1989 ORSA/TIMS Sprint talk (U4).
  - web.archive.org (refused by WebFetch per team.json; not used): older Mittelmann tables that included CBC, and the date Cbc left the MILP table.
- **UMPIRE and OSL MIP**: no peer critique found. Surveys of MIP codes from the 1970s and 1980s were not checked.
- **OSL simplex**: no independent benchmark from the 1990s found beyond the rival's accounts.
- **Governance**: no critical assessment of COIN-OR's founding benevolent-dictator model was found.
- **Barrier authorship** in Clp not checked, so the barrier critiques (Sandia; Clp#151, #334) are not attributed to him.
- **Selection bias**: the GitHub analysis covers only issues he commented on. Issues he ignored, and the mailing-list era, are not covered, except the TRAC tickets migrated in 2019.
- **Comment counts**: 481 in the five-repository harvest vs 461 in team.json; agent 03's reconciliation (Cbc, Clp, CoinUtils, Cgl and Osi give 461) is relayed, not re-checked by me.
- **Identities**: what ChipLab is, and who is behind several reporter accounts, was not established.
- **Sprint**: no public evaluation of Clp's Sprint implementation was found.

## Implications for Phase 2 (all [inferred])

- **Correctness craft.** Model it as: check against a second solver and the MIPLIB value; reduce to a minimal instance; name the mechanism (tolerance or scaling); retreat to the safe version. Record its blind spot alongside: optimized builds and large-problem testing hide asserts and small-case errors, and clever reductions ship before broad regression tests exist.
- **Authorship.** Keep his code separate from code he maintains. Critiques of clique strengthening, the conflict graph, red-split, the LP reader or the OSL factorization are not critiques of his craft. Preprocessing critiques (CglPreProcess, CglProbing, CoinPresolve*) are.
- **Documentation.** Give the skill an honest stance: the knowledge lives in code, headers, examples and replies, and others wrote the analyses (Idiot, Aboca). The skill should not claim documentation that does not exist.
- **Benchmarks.** When citing one, always state the configuration (crash and presolve on or off) and whether a release or master was tested (C4).
- **MIP.** A preference for a tight big-M over SOS for indicators; heuristic variability treated as inherent; recipes built from gaps and multiple root passes; reluctance to change a user's model except in a copy.

---

## Sources

**Documents and records read (S).** Primary unless marked.

- S1. A. Koberstein, *The dual simplex method, techniques for a fast and stable implementation*, PhD thesis, Universität Paderborn, Oct 2005. https://digital.ub.uni-paderborn.de/hsmig/download/pdf/3885 (read pp. 1–2, 29, 32, 56–61, 70, 75–76, 82, 101, 113–114, 124–129). Primary.
- S2. Q. Huangfu, J. A. J. Hall, *Parallelizing the dual revised simplex method*, Mathematical Programming Computation 10(1):119–142, 2018, DOI 10.1007/s12532-017-0130-5. Open-access PDF at webhomes.maths.ed.ac.uk/hall/HuHa13/HuHa13.pdf (read pp. 123–126, 132, 134, 136, 140–141). Primary.
- S3. Q. Huangfu, J. A. J. Hall, *Novel update techniques for the revised simplex method*, technical report ERGO-13-001, 7 July 2013, webhomes.maths.ed.ac.uk/hall/HuHa12/ERGO-13-001.pdf (read pp. 2, 9). Journal version: Computational Optimization and Applications 60(3):587–608, 2015, DOI 10.1007/s10589-014-9689-1. Primary.
- S4. I. L. Galabova, J. A. J. Hall, *A quadratic penalty algorithm for linear programming and its application to linearizations of quadratic assignment problems*, arXiv:1804.09172v1, 24 Apr 2018 (read pp. 1–9, 12–15). Journal version: Optimization Methods and Software 35(3):488–501, 2020, DOI 10.1080/10556788.2019.1604702, not read. Primary.
- S5. J. Gearhart, K. Adair, J. Durfee, K. Jones, N. Martin, R. Detry, *Comparison of open-source linear programming solvers*, Sandia report SAND2013-8847, Oct 2013, DOI 10.2172/1104761, https://www.osti.gov/servlets/purl/1104761 (read pp. 3, 21–22, 31–33). Primary.
- S6. J. T. Linderoth, T. K. Ralphs, *Noncommercial Software for Mixed-Integer Linear Programming*, COR@L technical report, Dec 2004, revised Jan 2005, https://jlinderoth.github.io/papers/Linderoth-Ralphs-05-TR.pdf (read pp. 1, 27–28, 41–43). Chapter in *Integer Programming: Theory and Practice*, CRC Press, 2005, pp. 253–303, DOI 10.1201/9781420039597.ch10. Primary.
- S7. X. Zhou, Z. Xu, C. Sun, *Validating Mixed-Integer Programming Solvers*, ICSE '26, Rio de Janeiro, 12–18 April 2026, pp. 3800–3812, DOI 10.1145/3744916.3787827. Author PDF https://zxt5.github.io/papers/flip-icse26.pdf (read abstract, §5, Tables 1–3). Primary.
- S8. J. Huchette, J. P. Vielma, *Nonconvex Piecewise Linear Functions: Advanced Formulations and Simple Modeling Tools*, Operations Research 71(5):1835–1856, 2023, DOI 10.1287/opre.2019.1973; arXiv:1708.00050v3 (read §3.2 and pp. 15, 17). Primary.
- S9. A. Gleixner et al., *MIPLIB 2017: data-driven compilation of the 6th mixed-integer programming library*, Mathematical Programming Computation 13(3):443–490, 2021, DOI 10.1007/s12532-020-00194-3 (read p. 462, Table 6, only). Primary.
- S10. R. E. Bixby, *Solving Real-World Linear Programs: A Decade and More of Progress*, Operations Research 50(1):3–15, 2002, DOI 10.1287/opre.50.1.3.17780. Open mirror PDF downloaded by the Bixby agent of this workflow (read pp. 6, 8, 14). Primary.
- S11. R. E. Bixby, *A Brief History of Linear and Mixed-Integer Programming Computation*, Documenta Mathematica Extra Volume ISMP (2012), 107–121 (read pp. 109, 110, 113). Primary.
- S12. *Optima* 101 (September 2016), interview with Robert E. Bixby, mathopt.zib.de/Optima-Issues/optima101.pdf (read PDF p. 3). Primary.
- S13. R. E. Bixby, *Linear Programming: A Historical View*, Hausdorff School deck, September 2022 (read PDF pp. 14, 17–19, 21). Primary.
- S14. R. Anbil, J. J. Forrest, W. R. Pulleyblank, *Column generation and the airline crew pairing problem*, Documenta Math. Extra Vol. ICM 1998 III, 677–686, DOI 10.4171/dms/1-3/65 (read pp. 681, 684, references). Co-authored by Forrest; used for comparison. Primary.
- S15. J. A. J. Hall, Q. Huangfu, *A high performance dual revised simplex solver*, PPAM 2011 slides, webhomes.maths.ed.ac.uk/hall/PPAM11/PPAM11.pdf (read slides 34, 36–41). Primary.
- S16. Q. Huangfu, J. Hall, *Novel update techniques for the revised simplex method*, ERGO seminar slides, 30 Nov 2016, webhomes.maths.ed.ac.uk/hall/ERGO_301116/ERGO_301116.pdf (read slides 29, 32, 36–37). Primary.
- S17. J. Hall, Q. Huangfu, I. Galabova, *An open-source high performance dual simplex solver*, SIOPT 2017 slides, webhomes.maths.ed.ac.uk/hall/SIOPT17/SIOPT17.pdf (read slides 4, 9, 13). Primary.
- S18. H. D. Mittelmann, *LPopt Benchmark (find optimal basic solution)*, page dated 22 Oct 2026, https://plato.asu.edu/ftp/lpopt.html. Primary (context only).
- S19. H. D. Mittelmann, *The MIPLIB2017 Benchmark Instances*, page dated 28 Oct 2026, https://plato.asu.edu/ftp/milp.html. Primary (context only).
- S20. coin-or/Cbc README.md, last changed 2026-10-19; read in agent 03's clone at 001b861c (2026-11-04). Primary.
- S21. Release tags and README history of coin-or/Cbc and coin-or/Clp (git; agents 03 and 06 mirrors). Primary.
- S22. Source headers on coin-or master: Cgl CglPreProcess.cpp, CglProbing.cpp, CglTwomir.cpp, CglCliqueStrengthening.cpp, CglRedSplit.cpp (raw.githubusercontent.com); CoinUtils CoinPresolveDupcol.cpp, CoinPresolveDual.cpp, CoinStaticConflictGraph.cpp, CoinLpIO.cpp, CoinOslFactorization.cpp. File histories from agent 06's mirrors of Cgl and CoinUtils. Primary.
- S23. zbMATH Open API records for his papers, 2026-11-05 (no reviews found). Primary.
- S24. GitHub issue-comment harvest (agent 03; 3,930 comments in five coin-or repositories) and issue bodies from the GitHub search API (this run). Crossref, OpenAlex and arXiv API records used to check every identifier above. Primary data and records.
- S25. Qi Huangfu research note 05-peer-critique.md (product/lp-team/qi-huangfu/references/research/, 2026-10-27), for Mittelmann Wayback snapshots from 2017–2021 and the HiGHS update choice. Secondary; not re-checked.

**GitHub threads read (G).** All primary; comment ids in the text.

- G1. coin-or/Cbc#481, MIPLIB optimal values mismatched on master, 2022-02. https://github.com/coin-or/Cbc/issues/481
- G2. coin-or/Cbc#479, CglProbing assertion on MIPLIB instances, 2022-01. https://github.com/coin-or/Cbc/issues/479
- G3. coin-or/Cbc#332, CbcMain not thread-safe, 2020-09 (open). https://github.com/coin-or/Cbc/issues/332
- G4. coin-or/Cbc#374, refactor PR thread, 2021-03 to 2022-01. https://github.com/coin-or/Cbc/pull/374
- G5. coin-or/Cbc Discussion #465, 2021-12 to 2022-01. https://github.com/coin-or/Cbc/discussions/465
- G6. coin-or/Cbc#101, command-line parsing, comment 2019-03-12. https://github.com/coin-or/Cbc/issues/101
- G7. coin-or/Cbc#197, warnings fix changed the algorithm, 2019-03-13. https://github.com/coin-or/Cbc/issues/197
- G8. coin-or/Clp#101, unexplained revert, 2019-04. https://github.com/coin-or/Clp/issues/101
- G9. coin-or/Clp#40, fix committed without a tracker note, 2019-03-11. https://github.com/coin-or/Clp/issues/40
- G10. coin-or/Clp#97, stable and trunk divergence, 2019-03. https://github.com/coin-or/Clp/issues/97
- G11. coin-or/Clp#128, debug output in release 1.17.3, 2019-12. https://github.com/coin-or/Clp/issues/128
- G12. coin-or/Cbc#204, release testing did not cover the examples, 2019-02. https://github.com/coin-or/Cbc/issues/204
- G13. coin-or/Cbc#367, master vs distribution release, 2021-03. https://github.com/coin-or/Cbc/issues/367
- G14. coin-or/Cbc#668, wrong ILP result, conflict-graph regression, 2024-08 to 2025-02. https://github.com/coin-or/Cbc/issues/668
- G15. coin-or/Cbc#639, CoinPresolveDupcol regression, 2024-02. https://github.com/coin-or/Cbc/issues/639
- G16. coin-or/Cbc#599, infeasible instead of the known optimum; CglPreProcess and CglTwomir, 2023. https://github.com/coin-or/Cbc/issues/599
- G17. coin-or/Cbc#741, wrong result on a small ILP; 2×2 improvement removed, 2025-08. https://github.com/coin-or/Cbc/issues/741
- G18. coin-or/Cbc#689, incorrect optimum via PuLP; tolerance, 2025-02. https://github.com/coin-or/Cbc/issues/689
- G19. coin-or/Cbc#694, console vs solution-file mismatch, 2025-02 to 2025-03. https://github.com/coin-or/Cbc/issues/694
- G20. coin-or/Cbc#700, #701 and #711, assertion crashes and NDEBUG builds, 2025-04. https://github.com/coin-or/Cbc/issues/701 and https://github.com/coin-or/Cbc/issues/711
- G21. coin-or/Cbc#704, wrong optimum under an odd option pair, 2025-04. https://github.com/coin-or/Cbc/issues/704
- G22. coin-or/Cbc#715, sign error in cut weakening, 2025-05. https://github.com/coin-or/Cbc/issues/715
- G23. coin-or/Cbc#719, OSL factorization crash, won't fix, 2025-05. https://github.com/coin-or/Cbc/issues/719
- G24. coin-or/Cbc#720, preprocess strategy, 2025-05. https://github.com/coin-or/Cbc/issues/720
- G25. coin-or/Cbc#737, CoinPresolveDual singleton check, 2025-08. https://github.com/coin-or/Cbc/issues/737
- G26. coin-or/Cbc#747, relaxed second feasibility check, 2025-10. https://github.com/coin-or/Cbc/issues/747
- G27. coin-or/Cbc#750 and #751, clique strengthening, 2025-10. https://github.com/coin-or/Cbc/issues/751
- G28. coin-or/Cbc#827 and #828, preprocessing wrong objective and wrong infeasibility, 2026-10 (open). https://github.com/coin-or/Cbc/issues/828
- G29. coin-or/Clp#334 and #335, barrier and primal misclassification, 2026-06 to 2026-07. https://github.com/coin-or/Clp/issues/334 and https://github.com/coin-or/Clp/issues/335
- G30. coin-or/Clp#341, optimal reported for an unbounded LP, 2026-10. https://github.com/coin-or/Clp/issues/341
- G31. coin-or/Clp#103, MIPLIB 2017 LP relaxation value, 2019-04. https://github.com/coin-or/Clp/issues/103
- G32. coin-or/Clp#157, inconsistent results on re-solve, 2020-08. https://github.com/coin-or/Clp/issues/157
- G33. coin-or/Clp#251, getBasics after barrier, 2022-12. https://github.com/coin-or/Clp/issues/251
- G34. coin-or/Clp#286, infeasibility rays, 2024-03 to 2026-10. https://github.com/coin-or/Clp/issues/286
- G35. coin-or/Clp#151, barrier through the C interface on a large LP, 2020-06. https://github.com/coin-or/Clp/issues/151
- G36. coin-or/Clp#163, Idiot on Windows through OsiClp, 2020-10. https://github.com/coin-or/Clp/issues/163
- G37. coin-or/Cbc#837, Idiot at every node for set partitioning, 2026-10 to 2026-11 (open). https://github.com/coin-or/Cbc/issues/837
- G38. coin-or/Cbc#728, CI work and an Idiot remark, 2025-07. https://github.com/coin-or/Cbc/issues/728
- G39. coin-or/Cbc#301, Clp slower than Cbc on an LP, 2020-05. https://github.com/coin-or/Cbc/issues/301
- G40. coin-or/Cbc#494, newer versions slower to the optimum, 2022-04. https://github.com/coin-or/Cbc/issues/494
- G41. coin-or/Cbc#381, slow on an infeasible problem, 2021–22. https://github.com/coin-or/Cbc/issues/381
- G42. coin-or/Cbc#633, run-time variance, 2024-01. https://github.com/coin-or/Cbc/issues/633
- G43. coin-or/Cbc#572, indicator constraints, 2023-02. https://github.com/coin-or/Cbc/issues/572
- G44. coin-or/Cbc#489, reliability claim and the cvxpy parameters, 2022-04. https://github.com/coin-or/Cbc/issues/489
- G45. coin-or/Cbc#310, recommended entry points, 2020-06. https://github.com/coin-or/Cbc/issues/310
- G46. coin-or/Cbc#260 (2019-09) and coin-or/Clp#107 (2019-05), Aboca experimental and unused. https://github.com/coin-or/Cbc/issues/260 and https://github.com/coin-or/Clp/issues/107
- G47. coin-or/Clp#262, pivoting rules and the Abc classes, 2023-03. https://github.com/coin-or/Clp/issues/262
- G48. coin-or/Clp#245, QP barrier test file, 2022-11. https://github.com/coin-or/Clp/issues/245
- G49. coin-or/Cbc#759 (2026-01) and #748 (2025-10), debug assert and broken commit. https://github.com/coin-or/Cbc/issues/759 and https://github.com/coin-or/Cbc/pull/748
- G50. coin-or/Cbc#543, three successive diagnoses, 2022-09. https://github.com/coin-or/Cbc/issues/543
- G51. coin-or/Cbc#562, CglTwomir ranged-row cut weakened, 2022-11. https://github.com/coin-or/Cbc/issues/562
- G52. coin-or/CoinUtils#210, LP-file reader change taken out, 2023-04. https://github.com/coin-or/CoinUtils/issues/210
- G53. coin-or/Cgl#81, CglProbing fix behind a define, 2022-08. https://github.com/coin-or/Cgl/issues/81
- G54. coin-or/Cbc#411, segfault with a method parameter; Julia vs C API, 2021-05 to 2021-06 (open). https://github.com/coin-or/Cbc/issues/411
- G55. scipopt/papilo#59 and #62, issues opened by Forrest, 2024-09. https://github.com/scipopt/papilo/issues/59 and https://github.com/scipopt/papilo/issues/62
- G56. coin-or/Clp#358, tabular message output and moving next to master, 2026-10. https://github.com/coin-or/Clp/issues/358
- G57. coin-or/Cbc#661, Sprint advice and 64-bit indices, 2024-08. https://github.com/coin-or/Cbc/issues/661
- G58. coin-or/Cbc#231, time limits settled by his commit, 2019-06. https://github.com/coin-or/Cbc/issues/231
- G59. coin-or/Cbc#703, gap comparison with HiGHS, 2025-04. https://github.com/coin-or/Cbc/issues/703
- G60. coin-or/Cbc#305, a very easy but very large problem, 2020-05. https://github.com/coin-or/Cbc/issues/305

**Identified, DOI checked on Crossref, not read (N).**

- N1. J. K. Reid, *A sparsity-exploiting variant of the Bartels–Golub decomposition for linear programming bases*, Mathematical Programming 24(1):55–69, 1982, DOI 10.1007/BF01585094.
- N2. L. M. Suhl, U. H. Suhl, *A fast LU update for linear programming*, Annals of Operations Research 43(1):33–47, 1993, DOI 10.1007/BF02025534.
- N3. J. M. Elble, N. V. Sahinidis, *A review of the LU update in the simplex algorithm*, International Journal of Mathematics in Operational Research 4(4):366–, 2012, DOI 10.1504/ijmor.2012.048901.
- N4. A. Świętanowski, *A New Steepest Edge Approximation for the Simplex Method for Linear Programming*, Computational Optimization and Applications 10(3):271–281, 1998, DOI 10.1023/a:1018317206484 (the publisher page redirected to an authorization endpoint; not followed).
- N5. A. Koberstein, *Progress in the dual simplex algorithm for solving large scale LP problems: techniques for a fast and stable implementation*, Computational Optimization and Applications 41(2):185–204, 2008, DOI 10.1007/s10589-008-9207-4.
- N6. A. Koberstein, U. H. Suhl, *Progress in the dual simplex method for large scale LP problems: practical dual phase 1 algorithms*, Computational Optimization and Applications 37:49–65, 2007, DOI 10.1007/s10589-007-9022-3.
- N7. R. Fukasawa, L. Poirrier, *Permutations in the Factorization of Simplex Bases*, INFORMS Journal on Computing 31(3):612–632, 2019, DOI 10.1287/ijoc.2018.0862.
- N8. H. D. Mittelmann, *Benchmarking Optimization Software – a (Hi)Story*, SN Operations Research Forum 1(1), 2020, DOI 10.1007/s43069-020-0002-0.
- N9. T. Koch et al., *MIPLIB 2010*, Mathematical Programming Computation 3(2):103–163, 2011, DOI 10.1007/s12532-011-0025-9.
- N10. R. Lougee-Heimer, *The Common Optimization INterface for Operations Research: Promoting open-source software in the operations research community*, IBM Journal of Research and Development 47(1):57–66, 2003, DOI 10.1147/rd.471.0057.
- N11. J. Forrest, R. Lougee-Heimer, *CBC User Guide*, INFORMS TutORials (Emerging Theory, Methods, and Applications), 2005, pp. 257–277, DOI 10.1287/educ.1053.0020.

**Cited by others, not reachable (U).**

- U1. J. Forrest, Cbc mailing-list post on the CoinStructuredModel crash, March 2014 (list.coin-or.org pipermail cbc/2014-March/001297.html; cited by S4). list.coin-or.org is recorded as unreachable on 2026-11-05 in team.json; not retried.
- U2. J. Forrest, *Never Asked Questions*, fastercoin.com/f2_files/naqs.html, 2012 (cited by S2). The domain is parked.
- U3. J. Forrest, *Aboca: a bit of Clp accelerated*, presentation at the 21st International Symposium on Mathematical Programming, 2012 (cited by S2). No copy found.
- U4. J. J. Forrest, *Mathematical programming with a library of optimization subroutines*, ORSA/TIMS Joint National Meeting, New York, October 1989 (cited by S14 as the origin of Sprint). No copy found.

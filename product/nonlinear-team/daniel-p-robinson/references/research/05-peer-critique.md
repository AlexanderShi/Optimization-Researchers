# Daniel P. Robinson: Peer Critique (blind spots, limits, contested judgements)

| Field | Value |
|---|---|
| Researcher | Daniel P. Robinson (Lehigh University ISE since 2019; JHU AMS 2011–2019; postdocs at Oxford with N. I. M. Gould and at Northwestern with J. Nocedal; PhD UC San Diego 2007 under P. E. Gill) |
| Dimension | Research agent 05 of 06: peer critique. Covers published objections, a published comment-and-rejoinder exchange, counterexamples, rival schools, outside benchmarks, the fate of his software, and how he answered |
| Research date | 2026-10-16 |
| Sources consulted | 52 (33 primary, 19 secondary), listed under "Sources" |
| WebSearch calls | 1 (of 7 allowed) |
| User-supplied material | None. `references/sources/{papers,talks,essays,software}/` hold only `.gitkeep`. `private/` was not opened. **Nothing in this file is from user-supplied material.** |
| Transcripts saved | None |
| Language | English (per team.json) |

**Tags.**
- [stated]: said by Robinson, or by a paper or talk he co-signed.
- [practice]: what his papers, code or software records show was done.
- [observed]: what a third party (the critic) wrote.
- [inferred]: my reading. The basis is given, and it must not be quoted as anyone's view.
- (P) is a primary source: the critic's own text or Robinson's own text, read in full or at the page cited. (S) is secondary: an aggregator, or a quotation seen only through the Semantic Scholar citation-context index ("S2 context; full text not read").

**How the critiques were found.**
1. I took the OpenAlex works list for ORCID 0000-0003-0251-4227 (127 records; DBLP pid 20/8222 was behind a bot wall).
2. I pulled Semantic Scholar citation contexts for 36 of his papers (about 2,000 citing records) and filtered them for critical wording.
3. I opened every critic I quote in full text (arXiv, Optimization Online, an institutional repository or an open-access publisher PDF), except where a line is marked "S2 context".
4. I read the Robinson-side papers that state the design choice under attack.
5. I checked the GALAHAD source repository for what happened to his codes.
6. I checked bibliographic data with Crossref and OpenAlex.

Paywalled texts without a legal open copy were not read, and no paywall was bypassed.

**Co-authorship caveat.** Almost all of Robinson's papers are co-authored and use alphabetical author order. A critique of "Gould and Robinson", "Gill, Kungurtsev and Robinson" or "Curtis, Robinson and …" targets a team. Some critics belong to his own network, and I flag them:
- S. J. Wright co-authored TR-Newton-CG.
- M. J. O'Neill is a Curtis–Robinson co-author.
- R. Vidal and B. Haeffele are his former JHU collaborators.
- N. I. M. Gould co-authored the TRS work.

The stochastic-SQP and complexity material overlaps with `../../frank-e-curtis/references/research/05-peer-critique.md`. I used that file only as a lead. Every quote reused here was re-read in this run at the page given.

---

## 0. Summary for Phase 2

| # | Recurring objection (blind spot / limit) | Raised by | Robinson-side answer | Status |
|---|---|---|---|---|
| R1 | Local-convergence theory may assume **which subproblem solution** is computed. Robinson calls this "unsatisfactory"; the rival school calls it "plain unavoidable" | Izmailov & Solodov (TOP 2015 rejoinder) vs Robinson (TOP 2015 comment) | He designs methods (pdSQP / stabilized SQP, S2QP) whose theory avoids the assumption. The price is algorithmic complexity he concedes himself | **Open, explicit disagreement** on record |
| R2 | **Designs that are complicated**, and a design rationale later undercut locally: convex-QP-first second-derivative SQP; TRACE's extra regularization parameter | Izmailov & Solodov (2016); Hamad & Hinder (2024); Shen et al. (2019); self ("necessarily more complicated"; "The details are complicated") | No published reply found | Unanswered |
| R3 | **Practice gap**: methods published with no numerics or only in-house baselines. Codes that never reached release | Self-statements (IP trust funnel; S2QP family); GALAHAD's own status labels | Promised GALAHAD implementations. Only the subproblem solvers (TRS/RQS, DQP) shipped as "ok" | Largely unanswered |
| R4 | **Complexity-driven modifications do not pay in practice**. Suboptimal Lipschitz-constant scaling; no local-rate analysis; scaled rather than unscaled KKT measure | Wright (co-author, 2025); Hamad & Hinder (2022, 2024); Jiang et al. (Ye group); Cartis–Gould–Toint | Self-acknowledged cost in TR-Newton-CG Fig. 1. He attacks the yardstick ("faulty", regional complexity) | Shared tension, unresolved |
| R5 | **Theory of the stabilized / shifted methods is weaker than claimed or unproven**. "Partial" stabilization; a CAKKT notion weaker than the standard one | Fernández & Solodov (2014); Andreani et al. (2020/22); Haeser (2018, S) | Superlinear-convergence paper (2017) for the first [inferred answer]. None found for the second | Mixed |
| R6 | **Stochastic SQP**: prespecified sequences drive performance; symmetric-noise assumption; LICQ-filtered test set; "ignore in practice" vs measured degradation | Na–Anitescu–Kolar; Fang et al.; O'Neill | Regime argument; later papers drop assumptions one at a time (see the Curtis file) | Partly answered |
| R7 | **Vidal-line limits**: SSC-OMP connectivity and noise; small-sample datasets; scaling to millions of points; DPCP needs the codimension | Self (EnSC 2016); Vielhaben et al.; Peng & Pavlidis; Lipor et al.; Hinojosa et al.; Giampouras–Haeffele–Vidal | EnSC answered connectivity (with Robinson). Unknown codimension was answered by the Vidal group without him | Partly answered, often by others |
| R8 | His own critique of augmented Lagrangians is **reused against the class he improved** | Cheng & Na (2024) | None needed. It shows how others read the AAL papers | — |

---

## 1. Stabilized SQP and the primal-dual augmented Lagrangian (with Gill, later Kungurtsev; 2007–2020)

**Era and resource context.** This is his thesis line (UCSD 2007, Gill). It was carried on through the JHU years with Gill and Kungurtsev. Prototypes are Matlab (pdSQP). The benchmark is SNOPT, Gill's own SQP code. The rival school is Izmailov (Moscow State) and Solodov (IMPA, Rio), with Fernández and Uskov. They own the local theory of stabilized SQP (sSQP) and critical multipliers. A second outside school, Andreani, Haeser and co-workers (São Paulo / Campinas), judges algorithms by sequential optimality conditions. Robinson was an assistant professor at JHU when the main exchange happened (2015).

### 1.1 The TOP 2015 exchange: may local theory assume which subproblem solution is found? (R1)

The setting: TOP 23(1) (2015) ran the invited discussion paper by Izmailov & Solodov, "Critical Lagrange multipliers: what we currently know about them, how they spoil our lives, and what we can do about it" (pp. 1–26, DOI 10.1007/s11750-015-0372-1; paywalled, **not read**). It printed four comments: Fischer, Martínez, Mordukhovich and Robinson. Then came the authors' rejoinder. Robinson's comment and the rejoinder are open access and were read in full.

- [stated] (P) Robinson, "Comments on: Critical Lagrange multipliers…", TOP 23 (2015) 43–47, DOI 10.1007/s11750-015-0371-2:
  - p. 44, on the state of the field: "it is probably safe to say that the best way to globalize sSQP is not yet clear." On his yardstick: "As I believe that algorithms should be practically and theoretically sound, I will focus on the practical aspects of the globalization process."
  - p. 45, against two-phase globalization: "it is difficult to develop conditions that reliably and efficiently decide when the global phase should transition to the local phase." And: "It therefore seems that commonly used two-phase approaches, although successfully used on many problems, may never reliably produce superlinearly convergent iterates in practice, as predicted by the local convergence theory."
  - p. 45, the core objection: "The calculation of such special solutions, although critical to proving superlinear local convergence, cannot be guaranteed in practice. This fact leads to a difference of opinion among researchers. One group believes that this assumption on the choice of subproblem solutions is minor." He adds: "I do not know of any result in this direction and, in fact, I do not believe it to be true (at least not provably so)."
  - p. 45, on the evidence: "all of the numerical experiments that I am aware of show that superlinear convergence is not achieved by sSQP on a nontrivial percentage of test problems." He then hedges in the same paragraph: "this somewhat disappointing performance may be caused by reasons other than the assumption on the subproblem solutions."
  - pp. 45–46: "I belong to the second group of researchers who believe that the assumption placed on the subproblem solutions is unsatisfactory and should be avoided if possible."
  - p. 46, he answers the paper's claim that the assumption is unavoidable: "This statement is true if a conventional active-set method is used and exact solutions of the subproblem are demanded." He then presents the Gill–Kungurtsev–Robinson method and concedes its cost: "The details are complicated", and "the synchronization of these two aspects into a practical single-phase algorithm proved more difficult than anticipated".
- [observed] (P) Izmailov & Solodov, "Rejoinder on: Critical Lagrange multipliers…", TOP 23 (2015) 48–52, DOI 10.1007/s11750-015-0373-0:
  - p. 50: "Daniel Robinson believes that when the subproblems of the algorithm may have multiple solutions, the restrictions in the theoretical analysis on the choice of "appropriate" solutions cannot be ignored from the practical perspective. We agree that this position is not without a reason, of course. While not advocating to ignore the issues, we have a different view on this."
  - p. 51: "Thus, the role of such conditions is purely theoretical, of course. They are not part of the algorithm's implementation." And: "In our view, it is crucial to stress that localization conditions on solutions of subproblems are plain unavoidable, except if subproblems are equality-constrained or strongly convex."
  - p. 51: "The alternative can only consist of declaring that "practical" algorithms are only those based on equality-constrained or strongly convex subproblems, but such a claim would appear too extreme, in our opinion."
  - p. 51, the empirical counter-claim: "in our numerical experience, so far we have never encountered a case when superlinear convergence is lost because apparently "wrong" subproblem solutions are computed." Also: "the theory does not require computing a global solution of the nonconvex subproblem, but only its stationary point."
- **Status: open.** Each side keeps its position. Robinson's experience: a "nontrivial percentage" of sSQP runs lose superlinear convergence. Theirs: they have "never encountered" a loss caused by wrong subproblem solutions. These two claims do not contradict each other strictly, because Robinson himself allows other causes. Neither side reports a study that checks which subproblem solution was computed. Robinson says such a check "is generally not possible" (p. 45).
- [inferred] This is the single clearest statement of his research taste under challenge. A theorem is acceptable only if its hypotheses refer to things an implementation can verify. He pays for that with algorithmic complexity, and he says so.

### 1.2 "Partial" stabilization without local theory (R5)

- [observed] (P) Fernández & Solodov, "Stabilized sequential quadratic programming: a survey", Pesquisa Operacional 34(3) (2014) 463–479, DOI 10.1590/0101-7438.2014.034.03.0463. Their ref. [39] is Gill & Robinson, "A globally convergent stabilized SQP method", SIAM J. Optim. 23(4) (2013) 1983–2010, DOI 10.1137/120882913. On p. 472 they write: "there does not seem to be any theory to justify that this "partial" […] stabilization in (26) actually inherits local convergence properties of sSQP under some reasonable assumptions." The elided words exclude the bound constraint x ≥ 0 from stabilization. Their overall verdict (p. 475): "Overall, building really satisfactory globalization techniques for sSQP is a challenging matter, which (for general problems) should still be considered an open question at this time."
- **Answer.** [practice] (P, by title and venue) The local theory came in Gill, Kungurtsev & Robinson, "A stabilized SQP method: superlinear convergence", Math. Program. 163 (2017) 369–410, DOI 10.1007/s10107-016-1066-7. In TOP (p. 46), Robinson says the method is "globally convergent and locally equivalent to sSQP". [inferred] Whether that paper's assumptions meet Fernández–Solodov's "reasonable assumptions" test was **not checked**: the full text is paywalled and was not read.

### 1.3 The shifted penalty-barrier method: a "CAKKT" notion strictly weaker than the standard one (R5)

- [observed] (P) Andreani, Cárdenas, Ramos, Ribeiro & Secchin, "On the convergence of augmented Lagrangian strategies for nonlinear programming". I read the Optimization Online preprint 2020/03/7701 (revised 2 Dec 2020). It was published as IMA J. Numer. Anal. 42(2) (2022) 1735–1765, DOI 10.1093/imanum/drab021; Crossref lists the authors as Andreani, Ramos, Ribeiro, Secchin and Velazco. The target is Gill, Kungurtsev & Robinson, "A shifted primal-dual penalty-barrier method for nonlinear optimization", SIAM J. Optim. 30(2) (2020) 1067–1093, DOI 10.1137/19m1247425. Preprint p. 16: "In the sequel, we show that not only (15) is weaker than the original CAKKT condition (Definition 1) for problem (NLP) with inequality constraints only, but it is actually strictly weaker than the less stringent AGP condition (Definition 3)." A counterexample follows (their Example 3). The same page also praises the method: "an interesting new method with good properties is presented in [23]". (The S2 context for the published version reads "a very interesting new method with nice properties", so the wording changed between versions.)
- [observed] (S; S2 context, full text not read) Andreani, Ramos & Secchin, SIAM J. Optim. 34(4) (2024) 3429–3455, DOI 10.1137/22m1493811: "Some interior-point methods (IPM) are able to reach CAKKT points when only ordinary inequality constraints are present [22], but it is lost when inequality constraints are rewritten by inserting slack variables [7]". I could not confirm which paper [7] is.
- **Answer: none found.** [inferred] This is a precise, checkable counterexample to the strength of a convergence claim. It is the kind of critique Robinson's own taste (1.1) should take most seriously. No reply turned up.

### 1.4 Other limits noted by the sequential-optimality school (S)

- [observed] (S; S2 context, full text not read) Haeser, "A second-order optimality condition with first- and second-order complementarity associated with global convergence of algorithms", Comput. Optim. Appl. 70(2) (2018) 615–639, DOI 10.1007/s10589-018-0005-3: "We will show that the regularized sequential quadratic programming from [26] and the active-set method for box-constraints ( E := ∅ ) from [3] are not expected to generate CAKKT2 sequences, even though both methods generate AKKT2 sequences." Semantic Scholar attaches this context to Gill–Kungurtsev–Robinson, IMA J. Numer. Anal. 37(1) (2017) 407–443, DOI 10.1093/imanum/drw004. The mapping of [26] to that paper was **not confirmed** in full text.
- [observed] (S; S2 context) Verschueren, Zanon, Quirynen & Diehl, SIAM J. Optim. 27(3) (2017) 2085–2109, DOI 10.1137/16M1081543, on Gill–Robinson 2013: "the method in [16] will ultimately also recover quadratic convergence, but indefinite QP subproblems are solved instead of positive definite ones." This is a cost remark from optimal-control users, who also call the method "One interesting alternative method of dealing with indefiniteness".

---

## 2. Second-derivative SQP and filter SQP (with Gould, then Loh; 2008–2015)

**Era and resource context.** These are the Oxford/RAL postdoc years with Gould, continued at JHU with his student Yueling Loh. Prototypes are Matlab; the intended home was Gould's Fortran library GALAHAD. Robinson was junior partner to a senior library-builder.

### 2.1 The founding rationale, and a later result that undercuts it locally (R2)

- [stated] (P) Gould & Robinson, "A second derivative SQP method: theoretical issues" (Optimization Online 2008/10/2130). [inferred] It is the report form of "A Second Derivative SQP Method: Global Convergence", SIAM J. Optim. 20(4) (2010) 2023–2048, DOI 10.1137/080744542.
  - p. 1, abstract: "there is little practical theory that justifies exact-Hessian SQP methods".
  - p. 2: "To our knowledge, all previous second-order SIQP methods assume that global minimizers of nonconvex subproblems are computed, which is not a realistic assumption in most cases. For these methods, the computation of a local minimizer is unsatisfactory because it may yield an ascent direction."
  - p. 3, the price they accept: "To achieve this goal, our procedure for computing a trial step is necessarily more complicated than that used by Fletcher."
  - The design: a strictly convex predictor QP, a Cauchy step, and an optional exact-Hessian SQP step.
- [observed] (P, abstract via OpenAlex; body not read) Izmailov & Solodov, "Some new facts about sequential quadratic programming methods employing second derivatives", Optim. Methods Softw. 31(6) (2016) 1111–1131, DOI 10.1080/10556788.2016.1177528. Near a solution with unique multipliers and the second-order sufficient condition, the exact-Hessian SQP direction is a descent direction for the ℓ1 penalty. The abstract: "We emphasize that this property is not straightforward at all, because the Hessian of the Lagrangian need not be positive definite under these assumptions or, in fact, under any other reasonable set of assumptions." And: "our results imply that in SQP methods where using subproblems without Hessian modifications is an option, this option has a solid theoretical justification at least on late iterations."
- [observed] (S; S2 context, full text not read) In the same paper: "We shall briefly comment on the more recent proposals in [8,9,17]". And: "The method in [8,9] first also solves a convex QP and then uses the obtained information to solve a second (inequality-constrained) QP using the exact Hessian." Semantic Scholar attaches these contexts to both Gould–Robinson 2010 SIOPT papers (DOIs 10.1137/080744542 and 10.1137/080744554). **What the comment says was not read.**
- **Answer: none found.** [inferred] The two claims are not strictly contradictory. Gould–Robinson's concern is global (far from a solution); Izmailov–Solodov's result is local. But the 2016 result removes part of the motivation for the convex-QP-first machinery on late iterations. See Contradiction X2.

### 2.2 Self-critique and outside cost remarks

- [stated] (S; S2 context) Gould & Robinson, "A second-derivative SQP method with a 'trust-region-free' predictor step", IMA J. Numer. Anal. 32(2) (2012) 580–601, DOI 10.1093/imanum/drq043. They write that the variant without a predictor trust-region constraint "may occasionally perform poorly when compared with its counterpart (Gould & Robinson, 2010a,b) that includes one".
- [stated] (P) In the interior-point trust-funnel paper, Robinson and his co-authors place their own second-derivative SQP papers among those of which "Preliminary results when solving small- to medium-sized problems is promising, but their effectiveness on large problems has not yet been confirmed." The papers cited there are refs. [20–22] (Gould–Robinson 2010a, 2010b, 2012) and [30] (Morales–Nocedal–Wu 2012). Source: Curtis, Gould, Robinson & Toint, Namur NTR 02/2014, §1 (PDF p. 4 including the repository cover). Published as Math. Program. 161 (2017) 73–134, DOI 10.1007/s10107-016-1003-9.
- [observed] (S; abstract read via OpenAlex, body via S2 context) Ahmadzadeh & Mahdavi-Amiri, "A competitive inexact nonmonotone filter SQP method…", Optim. Methods Softw. 37(4) (2022) 1310–1343, DOI 10.1080/10556788.2021.1913155. They build directly on Gould–Loh–Robinson (SIAM J. Optim. 24(1) (2014) 175–209, DOI 10.1137/130920599; and 25(3) (2015) 1885–1911, DOI 10.1137/140996677). They criticize two points. "We suggest a new penalty parameter update rule which is numerically more stable than the updating formula of [31]." And: "Gould et al. [31,32] computed an accelerator direction in every iterations", whereas they compute it "only in 'almost feasible iterations'". [inferred] This is critique by adoption: they keep the framework and fix its cost and its stability.

### 2.3 What happened to the codes (R3)

- [practice] (P) GALAHAD repository (github.com/ralna/GALAHAD, master; `src/README.packages` last changed 2026-08-18):
  - Under the heading "expired/unfinished packages have been cast into oblivion/", the README lists `s2qp | beta | trust-region SQP for NLP`. The header of `src/oblivion/s2qp/s2qp.F90` reads "Author: Daniel Robinson".
  - Under "packages that are far from ready but seem promising are in forthcoming/", it lists `fisqp | alpha | SQP filter method for NLP`. The header of `src/forthcoming/fisqp/fisqp.F90`: "Principal authors: Nick Gould, Yueling Loh and Daniel P. Robinson", "originally written in Matlab by Yueling Loh and Daniel P. Robinson", "initial Fortran translation, GALAHAD Version 2.6, November 23th 2014".
  - `README.forthcoming` (Oct 2016) opens: "A collection of packages that *may* appear in GALAHAD."
- [observed] (P) These status labels are the judgement of the GALAHAD maintainers (Gould's team), not of a rival. [inferred] More than a decade after publication, neither the second-derivative SQP method nor the filter SQP method became a released solver.

---

## 3. Trust-region and regularized subproblem solvers (Gould–Robinson–Thorne 2010; dual gradient projection)

**Era and resource context.** These are Oxford/RAL postdoc years. Gould–Robinson–Thorne, Math. Program. Comput. 2(1) (2010) 21–57, DOI 10.1007/s12532-010-0011-7, describes the algorithm behind GALAHAD's TRS and RQS packages. Those packages carry Gould as principal author (first released January 2009).

- [observed] (P) Adachi, Iwata, Nakatsukasa & Takeda, "Solving the Trust-Region Subproblem By a Generalized Eigenvalue Problem", SIAM J. Optim. 27(1) (2017) 269–291, DOI 10.1137/16M1058200 (Oxford ORA open copy, read):
  - p. 270, on the class of iterative methods, which includes "A modification of the Moré–Sorensen algorithm using Taylor series … presented by Gould, Robinson, and Thorne [15]": "All these algorithms require iterations of a computational routine, and the number of iterations is often unpredictable and potentially large."
  - The main comparison (p. 284) uses three outside codes (FRW, RSS, GLTR). On dense problems (p. 286): "Another alternative for dense problems is GALAHAD's galahad trs, which implements the algorithm in [15], although it did not perform better in the experiments here."
  - The acknowledgment thanks Gould for help with GALAHAD.
- [observed] (S; S2 context) Zhang, Shen & Li, SIAM J. Optim. 27(3) (2017) 2110–2142, DOI 10.1137/16M1095056: "The method proposed in [11] is based on matrix factorization but can often be just as successful as factorization-free methods for large problems when the sparsity structure is favorable." This states a limit of applicability: it needs factorizable sparsity. I matched [11] to GRT through the S2 index only.
- [observed] (S; S2 context; Gould is a co-author of GRT) Al Daas & Gould (arXiv:2511.11135, 2025): "This, however, does not avoid the cost of multiple factorizations; rival methods, e.g., [17, 22], also use factorizations, but experience suggests that relatively few often suffice."
- [practice] (P) GALAHAD `README.packages` lists `trs` and `rqs` as `ok`. It also lists `dqp | ok | strictly-convex QP, dual projection`; the header names Gould as principal author, released August 2012, and describes "a dual gradient-projection method". [inferred] By topic and date, DQP is the code line of Gould & Robinson, "A dual gradient-projection method for large-scale strictly convex quadratic problems" (Comput. Optim. Appl., DOI 10.1007/s10589-016-9886-1). The header does not name Robinson. [inferred] The work of Robinson's that matured into released software is the **subproblem-solver** work, not the full NLP methods (contrast 2.3, 4.1, 6.1).
- **Answer to Adachi et al.: none found.** No Robinson paper on TRS solvers appeared after 2010 [practice, from the OpenAlex list].

---

## 4. Interior-point trust funnel and trust-funnel complexity

**Era and resource context.** The idea dates from 2009 talks (per 06). It was published in 2017 with Curtis, Gould and Toint, a four-senior-author paper of 62 journal pages.

### 4.1 No numerics, and an implementation promise (R3)

- [practice] (P) Curtis, Gould, Robinson & Toint, Math. Program. 161 (2017) 73–134 (Namur NTR 02/2014 read). §1 announces the plan: algorithm (§2), finite termination (§3), barrier convergence (§4), conclusions (§5). There is no numerical section. The conclusion (report p. 42): "We are currently implementing our new algorithm. Once complete, it will be part of the Galahad [19] thread-safe library of Fortran 90 packages for the numerical solution of optimization problems."
- [practice] (P) GALAHAD today has no released trust-funnel solver. `src/oblivion/funnel/` holds `funnel | alpha | SQP funnel method for NLP` with header "Principal author: Nick Gould", "originally released GALAHAD Version 2.1, October 17th 2007 for equalities", "version for inequalities GALAHAD Version 2.6, July 13th 2013". [inferred] Whether that inequality version is the interior-point funnel of the 2017 paper is **not documented**. Either way, the promised package is not a released solver. **Prediction not fulfilled** (as of the repository state of 2026-08-18).
- [stated] (S; S2 context) The paper's own self-critique of a shortcut: "a naïve implementation of the SQP method described in [22,23] within an interiorpoint paradigm may result in a method for which the establishment of convergence guarantees is elusive." Confirmed in the NTR preprint, §1.

### 4.2 Trust-funnel complexity: a scaled stationarity measure (R4)

- [observed] (P) Cartis, Gould & Toint, "Optimality of orders one to three and beyond…", J. Complexity 53 (2019) 68–94, DOI 10.1016/j.jco.2018.11.001; arXiv:1705.07285 v2 read, p. 2. On Curtis, Robinson & Samadi, "Complexity analysis of a trust funnel algorithm for equality constrained optimization", SIAM J. Optim. 28(2) (2018) 1533–1563, DOI 10.1137/16m1108650: "The bounds derived in [26] for a trust-funnel algorithm also consider a scaled KKT condition and are of the same order." By contrast: "At variance with these latter references, this analysis considers unscaled approximate first-order critical points". Note that Gould co-authored the 2017 funnel paper.
- **Answer: none found.**

---

## 5. Adaptive augmented Lagrangian (with Curtis, Jiang, Gould; 2012–2016)

**Era and resource context.** These are early JHU years. Hao Jiang was his JHU student. There were Matlab prototypes plus a modification of LANCELOT inside GALAHAD.

### 5.1 How the method was evaluated, and what shipped (R3)

- [stated] (P) Curtis, Gould, Jiang & Robinson, "Adaptive augmented Lagrangian methods: algorithms and practical numerical experience", Optim. Methods Softw. 31(1) (2016) 157–186, DOI 10.1080/10556788.2015.1071813; arXiv:1408.4500 v1 read.
  - p. 1, motivation (his critique of the class): the adaptive update "is designed to overcome a potentially serious drawback of traditional AL methods, which is that they may be ineffective during some (early) iterations due to poor choices of the penalty parameter and/or Lagrange multiplier estimates."
  - p. 1, claim: "Our numerical experience suggests that the adaptive algorithms outperform traditional AL methods in terms of efficiency and reliability."
  - [practice] The comparisons are against the authors' own basic (non-steering) AL variants and plain LANCELOT. No interior-point or SQP solver is in the comparison (§3).
  - p. 15, test-set curation: "All of our solvers failed to solve the problems named chain, dirichlet, henon, lane emden, and robot1, so these problems were excluded."
  - p. 13, theory and practice diverge: "this suggests that safeguarding the steering mechanism may diminish its potential benefits." The safeguarded variants are the ones closer to the convergence theory of the original paper (Curtis, Jiang & Robinson, Math. Program. 152 (2015) 201–245, DOI 10.1007/s10107-014-0784-y) [inferred from the paper's description].
  - p. 18, promise: "The new package will be re-branded as Lancelot in the next official release, Galahad 2.6."
- [practice] (P) In today's GALAHAD `src/lancelot/LANCELOT.template` the steering controls exist (`penalty-parameter-steering-decrease 0.7`, `steering-kappa-3`, …). The default specification is `steer-towards-feasibility no`. [inferred] The promise was kept as an option, but users get no steering unless they turn it on.

### 5.2 His critique of AL reused against AL (R8)

- [observed] (P) Cheng & Na, "Physics-informed neural networks with trust-region sequential quadratic programming" (arXiv:2409.10777):
  - p. 4: "it is observed that augmented Lagrangian methods require a significant number of steps to get into the local region and are sensitive to dual initialization (Curtis et al., 2014)". The reference is Curtis, Jiang & Robinson.
  - p. 3: "Compared to augmented Lagrangian methods, SQP is more robust to dual initialization, exhibits much faster convergence (quadratic/superlinear for SQP while linear for augmented Lagrangian), and produces solutions with fewer objective function and gradient evaluations (Curtis et al., 2014; Dener et al., 2020; Hong et al., 2023)."
- [inferred] The motivating weakness Robinson's group documented for traditional AL is cited as a property of AL methods in general. The adaptive fix is not credited as removing it. Sen Na leads the rival stochastic-SQP group (section 7).
- [observed] (S; S2 context) Neutral reception from the AL school: Birgin & Martínez, Optim. Methods Softw. 35(5) (2020) 885–920, DOI 10.1080/10556788.2020.1746962, describe it only as an algorithm "in which decreasing the penalty parameters is possible following intrinsic algorithmic criteria."

---

## 6. Worst-case complexity: TRACE, TR-Newton-CG, regional complexity (with Curtis, Samadi, Royer, Wright; 2014–2021)

**Era and resource context.** This is the Cartis–Gould–Toint era of evaluation complexity. TRACE (Curtis, Robinson & Samadi, Math. Program. 162 (2017) 1–32, DOI 10.1007/s10107-016-1026-2) has no numerical section (per the Curtis file). TR-Newton-CG (Curtis, Robinson, Royer & Wright, SIAM J. Optim. 31(1) (2021) 518–544, DOI 10.1137/19M130563X) does have experiments.

### 6.1 TRACE is complicated (R2)

- [observed] (P) Hamad & Hinder, "A simple and practical adaptive trust-region method" (arXiv:2412.02079 v4), p. 3: "Significant efforts have been made to develop an adaptive trust-region method matching the cubic regularization complexity bound [4-7], though the resulting methods have diverged substantially from the original method." On TRACE [4]: "This makes TRACE significantly more complex compared to the classical trust-region framework."
- [observed] (P) Shen, Zhou, Fang & Ribeiro, "A Stochastic Trust Region Method for Non-convex Minimization" (arXiv:1903.01540 v1), p. 4: "Similar rate is achieved by (Curtis et al., 2017) but with a complicated trust region variant."
- [practice] (P) GALAHAD `src/forthcoming/trace/` (Fortran by Gould, "originally released GALAHAD Version 2.6. October 23rd 2014", crediting Curtis, Robinson and Samadi) is still `alpha`.

### 6.2 The regularization in TR-Newton-CG costs Hessian-vector products (R4): the critics cite his own figure

- [stated] (P) Curtis, Robinson, Royer & Wright (arXiv:1912.04365 v3):
  - p. 2: the modifications come "without significantly degrading important performance measures such as the number of iterations, function evaluations, and gradient evaluations".
  - p. 22: "The variants with no regularization term in the subproblems outperform the others in this respect; recall that these variants do not possess optimal complexity guarantees." And: "if Hessian-vector products are expensive relative to gradients, there may be a significant increase in run time as a result of including the regularization term."
- [observed] (P) Hamad & Hinder (arXiv:2412.02079 v4), p. 3: Curtis et al. "do introduce a regularization parameter to the trust-region subproblem, which can degrade practical performance Curtis et al. [5, Figure 1]."
- [observed] (P) S. J. Wright, the paper's co-author, "Optimization in Theory and Practice" (arXiv:2510.15734 v2), p. 23, on [89, 24]. Here [24] is TR-Newton-CG and [89] is Royer–O'Neill–Wright. "They are based on practical methods, but the modifications that are made to admit nonasymptotic theory do not improve the practical performance. Moreover, the complexity bounds are quite pessimistic for small ϵ; there remains a large gap between these bounds and practical performance."
- [inferred] The paper's abstract-level claim names the measures that do not degrade (iterations, function and gradient evaluations). The measure that does degrade (Hessian-vector products) appears only in §6. Outside critics and the co-author both read the result as "no practical gain".

### 6.3 Suboptimal dependence on the Lipschitz constant; no local analysis (R4)

- [observed] (P) Hamad & Hinder, "A consistently adaptive trust-region method", NeurIPS 35 (2022) 6640–6653, DOI 10.52202/068431-0481; arXiv:2408.01874 v1 read, p. 2. Paraphrase of a formula statement: the worst-case bounds of TRACE ([36]) and TR-Newton-CG ([37]) scale with the Hessian Lipschitz constant L as L^{3/2} and L^2, against the optimal L^{1/2}. Then: "none of these methods are consistently adaptive."
- [observed] (P) Jiang, He, Zhang, Ge, Jiang & Ye (Ye group), "Beyond Nonconvexity: A Universal Trust-Region Method with New Analyses", J. Sci. Comput. 106 (2026), DOI 10.1007/s10915-025-03154-y; arXiv:2311.11489 v4 read, p. 4: "The method [27, 19] does not provide local convergence analysis. We believe this should be true following standard analysis." Here [19] is TR-Newton-CG.

### 6.4 The counter-move: attack the yardstick

- [stated] (P) Curtis, slides "Characterizing Worst-Case Complexity of Algorithms for Nonconvex Optimization", ISMP Bordeaux, 3 July 2018, "joint work with Daniel P. Robinson", slide 4/31: "Our worst-case analysis for nonconvex optimization is faulty. We should characterize complexity in a different way. Purpose of this talk is to convince you." The same slide says of failing codes: "People have disputed this, but I have results!" That is Curtis's voice; who disputed it is not given. The written form is Curtis & Robinson, "Regional complexity analysis of algorithms for nonconvex smooth optimization", Math. Program. 187 (2021) 579–615, DOI 10.1007/s10107-020-01492-3.
- [observed] (P) Cartis, Gould & Toint, Proc. ICM 2018 (arXiv:1709.07180 v1), p. 24, §5 "The Curtis-Robinson-Samadi class": "It is stated in [36] that both ARC […] and TRACE [37] belong to the class, although the details are not given." Here [36] is arXiv:1708.00475. [practice] (P) That paper's v4 (15 Mar 2018; IMA J. Numer. Anal., DOI 10.1093/imanum/dry022), p. 3: "In §4, we show that ARC and TRACE can be viewed as special cases of our framework". **Answered.** Whether the referee or the CGT remark triggered the change is not documented.
- [observed] (S; S2 context) The only reception of the regional-complexity paper found is descriptive. Goyens & Royer, Math. Program. (2024), DOI 10.1007/s10107-024-02156-2, write that such analyses "yielded complexity bounds that improved over the general nonconvex setting". **No reply from the CGT school to "faulty" was found.**

---

## 7. Stochastic SQP (with Berahas, Curtis, Zhou, O'Neill; 2020–)

**Era and resource context.** This is the Lehigh years, with ONR funding (per 06). Matlab code is tested on CUTEst problems with simulated noise. The rival group is Na, Anitescu and Kolar, later joined by Mahoney and Fang. Full treatment is in the Curtis file. Here I re-verified only the main quotes.

- [observed] (P) Na, Anitescu & Kolar, Math. Program. 199 (2023) 721–791, DOI 10.1007/s10107-022-01846-z; arXiv:2102.05320 v2:
  - p. 3: Berahas–Curtis–Robinson–Zhou "proposed the very first practical algorithm" for the problem class.
  - p. 10: "This observation suggests that the prespecified sequence in both algorithms highly affects the performance."
  - p. 5: "Our analysis does not rely on the symmetry of the noise distributions (cf. [3, Example 3.17])."
- [observed] (P) Fang, Na, Mahoney & Kolar, SIAM J. Optim. 34(2) (2024) 2007–2037, DOI 10.1137/22M1537862; arXiv:2211.15943, p. 3: the prior methods "imposed a symmetry condition on the noise distribution. In contrast, deterministic SQP schemes only require the stability of the merit parameter".
- [practice] (P) Berahas, Curtis, Robinson & Zhou (arXiv:2007.10525 v1; SIAM J. Optim. 31(2) (2021) 1352–1379, DOI 10.1137/20m1354556), p. 26:
  - The test set was filtered to problems where "the LICQ held at all iterates in all runs of all algorithms that we ran", leaving 49 of 123 CUTE problems.
  - They concede: "We do not claim that "SQP Adaptive" is as efficient as "SQP Backtracking"".
- [stated] (P) Curtis, Robinson & Zhou (arXiv:2107.03512 v1; INFORMS J. Optim. 6(3–4) (2024) 173–195, DOI 10.1287/ijoo.2022.0008), p. 17, on the bad merit-parameter events: "we contend that, for practical purposes, they can be ignored for the same reasons as are claimed in [3]."
- [observed] (P) O'Neill (arXiv:2408.16656 v2), p. 34, rerunning the BCRZ code: "as the noise level increases, the performance of SSQP degrades significantly with respect to infeasibility, while the performance of TSSQP is largely unchanged." He is a former Curtis–Robinson co-author.
- **Status:** as in the Curtis file, partly answered (rank-deficient Jacobians, complexity with a random merit parameter, almost-sure convergence in later papers). The prespecified-sequence objection is met with a regime argument rather than removed.

---

## 8. Sparse and active-set methods (FaRSA, group-sparse subspace acceleration; 2016–)

**Era and resource context.** JHU, then Lehigh. Students: Tianyi Chen, then Yutong Dai. The tests are ℓ1-regularized logistic regression on LIBSVM-type data.

- [practice] (P) Chen, Curtis & Robinson, SIAM J. Optim. 27(3) (2017) 1583–1610, DOI 10.1137/16m1062259 (arXiv:1602.07018 v1 read). §1 names LIBLINEAR and OBA as "the most relevant" state of the art. The experiments (§4, Figs. 4.1–4.2) compare FaRSA **only with OBA**. [stated] p. 16: "the performance of both FaRSA and OBA deteriorates when the problems are unscaled". (The later local-convergence paper, Optim. Methods Softw., DOI 10.1080/10556788.2017.1415336, was **not read**, so I do not know whether it adds LIBLINEAR.)
- [observed] No outside critique, failed comparison or benchmark of FaRSA or of the group-sparse subspace-acceleration method (SIAM J. Optim., DOI 10.1137/21m1411111) was found in the citation contexts. Nearly all citing contexts are from Robinson's own group (see Gaps).

---

## 9. Sparse subspace clustering and DPCP with Vidal (JHU, 2015–2021)

**Era and resource context.** Robinson was the optimization co-PI inside René Vidal's computer-vision group, with student Chong You as first author. Venues are CVPR, ICCV, NeurIPS and ICML, with fast open review cycles; critics are application users across machine learning.

### 9.1 SSC-OMP: connectivity, noise, small samples, scale (R7)

- [stated] (P) You, Robinson & Vidal, CVPR 2016, 3918–3927, DOI 10.1109/cvpr.2016.425 (arXiv:1507.01238 v3):
  - p. 3: "Our analysis assumes that the data is noiseless."
  - p. 7: "We first observe that SSC-OMP does not have as good a connectivity as SSC-BP."
- [stated] (P) The same group, months later: You, Li, Robinson & Vidal, CVPR 2016, 3928–3937, DOI 10.1109/cvpr.2016.426 (arXiv:1605.02633), p. 1: "Other recently proposed sparsity based methods, such as orthogonal matching pursuit (OMP) [8, 46] and nearest subspace neighbor (NSN) [33], also suffer from the same connectivity issue." Here [46] is SSC-OMP. The elastic-net method (EnSC) was their answer. **Self-critique answered by his own group.**
- [observed] (P) Hinojosa, Vera & Arguello, IEEE JSTARS 14 (2021) 10773–10783, DOI 10.1109/JSTARS.2021.3120071 (arXiv:2104.06975), p. 3: "While SSC-OMP improves the time efficiency of SSC by several orders of magnitude, it significantly loses clustering accuracy [29]. Besides, SSC-OMP also suffers from the connectivity issue presented in the original SSC algorithm."
- [observed] (P) Vielhaben, Blücher & Strodthoff, "Multi-dimensional concept discovery (MCD)…", TMLR 2023 (arXiv:2301.11911 v2), p. 20: OMP (You et al., 2016b) "is, however, not robust against noise and does not allow for outlier removal via thresholding."
- [observed] (P) Peng & Pavlidis, Data Min. Knowl. Discov. 36(3) (2022) 958–986, DOI 10.1007/s10618-022-00820-9 (arXiv:2106.04330 v1), p. 8: "It is worth noting that all SSC-based methods (SSC, S3C, ASSC, SSC-OMP) yield poor performance in the presence of varying levels of noise." (The S2 context of the journal version reads "degrades rapidly with increasing levels of noise".)
- [observed] (P) Lipor, Hong, Tan & Balzano, Inf. Inference 10(1) (2021) 73–107, DOI 10.1093/imaiai/iaaa031 (arXiv:1709.04744 v3), p. 13, on Hopkins-155: "Scalable algorithms such as SSC-OMP and EnSC perform poorly on this dataset, likely due to the small number of points." This is a limit of applicability: methods built for scale lose on small, well-modelled data.
- [observed] (S; S2 context) Li, Tao, Wu, Zhong & Fu, IEEE Trans. Cybern. 52(9) (2022) 9090–9100, DOI 10.1109/TCYB.2021.3052056: SSC-OMP, ORGEN and others "fail to deal with million data points due to the big self-expressive dictionary and the huge affinity matrix."
- [inferred] The noise critique matches the self-stated limit: the subspace-preserving theory is for noiseless data. No Robinson paper adds a noisy-data guarantee for SSC-OMP. The 2019 arXiv analysis (Robinson, Vidal & You, arXiv:1912.13091) was **not read**, so this is unconfirmed.

### 9.2 DPCP needs the codimension (R7)

- [observed] (P) Giampouras, Haeffele & Vidal, ICLR 2022 (arXiv:2201.09079), p. 2. They criticize three DPCP papers with Robinson as co-author:
  - Zhu, Wang, Robinson, Naiman, Vidal & Tsakiris, NeurIPS 2018: "However, for that approach to be successful the knowledge of the true subspace codimension c becomes critical."
  - Zhu, Ding, Tsakiris, Robinson & Vidal, NeurIPS 2019, and Ding, Zhu, Vidal & Robinson, ICML 2021 (PMLR 139:2739–2748): "a key shortcoming of this approach is the fact that because all minimizers of problem (2) will be orthogonal matrices, a prerequisite for recovering the correct orthogonal complement of the inliers subspace is the a priori knowledge of the true codimension c".
  - General: "a key limitations of DPCP is that it requires a priori knowledge of the true subspace dimension."
- **Answered by the Vidal group without Robinson** (that paper's random-initialization projected subgradient method). [inferred] Robinson had moved to Lehigh in 2019. He did not return to DPCP after the 2021 papers.

### 9.3 A critique that is *not* about Robinson

- Suh, Roh & Ryu (ICML 2022; arXiv:2202.05501 v2), p. 8, say a rate "does not hold for all k ∈ N". The citation index attaches this to França–Robinson–Vidal. But their reference "França et al. (2021a)" is França, Jordan & Vidal (J. Stat. Mech. 2021), which does not include Robinson. **Excluded.**

---

## 10. How Robinson handles critique (pattern for Phase 2)

1. **He states the price of his own designs before critics do.** [stated] Examples: "necessarily more complicated" (2008), "The details are complicated" (2015), "more difficult than anticipated" (2015), "effectiveness on large problems has not yet been confirmed" (2014/2017), and the Hessian-vector-product cost in TR-Newton-CG (2021). Outside critics (Hamad–Hinder, Shen et al., Wright) later repeat these admissions as criticism.
2. **He defends verifiable hypotheses over plausible ones, in print.** [stated] In the only open exchange in his record (TOP 2015), he holds that theory resting on which subproblem solution is computed is "unsatisfactory". He keeps that position against the leading theorists of the topic, who call the conditions "plain unavoidable". He has not conceded, and neither have they.
3. **Self-critique becomes the next paper when the fix is algorithmic.** [practice] SSC-OMP connectivity → EnSC (same year). sSQP local theory → GKR superlinear (2017). LICQ at all iterates → rank-deficient stochastic SQP (with Curtis).
4. **Critiques of theory strength or of practical value go unanswered.** [practice; absence of evidence, so weak] No reply was found to:
   - Andreani et al. (CAKKT counterexample);
   - Izmailov–Solodov 2016 (exact-Hessian descent);
   - Adachi et al. (TRS benchmark);
   - Hamad–Hinder (complexity, regularization cost, L-scaling);
   - Cartis–Gould–Toint (scaled KKT);
   - Giampouras et al. (DPCP codimension; answered by others).
5. **Software follow-through is the weakest link.** [practice] Released GALAHAD code exists for the subproblem solvers (TRS, RQS, and DQP, the last matched by inference; Gould as principal author). The NLP methods are in `oblivion/` (s2qp, funnel) or `forthcoming/` at alpha (fisqp, trace). Steering is in LANCELOT but off by default. [inferred] Robinson's methods reach users mainly through papers and through co-authors' later codes, not as maintained solvers of his own. 06 records the same absence of a personal software line; that link is not stated by any critic.

---

## Contradictions (kept, not reconciled)

- **X1. Subproblem solutions and superlinear convergence.** Robinson (TOP 2015, p. 45): "all of the numerical experiments that I am aware of show that superlinear convergence is not achieved by sSQP on a nontrivial percentage of test problems". Izmailov & Solodov (rejoinder, p. 51): "we have never encountered a case when superlinear convergence is lost because apparently "wrong" subproblem solutions are computed." Robinson allows other causes, so the observations may be compatible. The judgements about whether localization conditions are acceptable in a theory are not.
- **X2. Exact-Hessian SQP steps.** Gould & Robinson (2008, p. 2): computing a local minimizer of a nonconvex QP "is unsatisfactory because it may yield an ascent direction", hence the convex-predictor design. Izmailov & Solodov (2016, abstract): near a solution, the unmodified-Hessian SQP direction is a descent direction for the ℓ1 penalty, so the "option has a solid theoretical justification at least on late iterations". Global versus local scope; neither side has addressed the other in a text I read.
- **X3. TR-Newton-CG's practical cost.** Authors (2021, p. 2): "without significantly degrading important performance measures". The same paper (p. 22): regularized variants are beaten on Hessian-vector products, with "a significant increase in run time" possible. Hamad–Hinder: the regularization "can degrade practical performance". Wright (co-author, 2025): the modifications "do not improve the practical performance".
- **X4. Reception of the shifted penalty-barrier method.** Andreani et al. praise it ("an interesting new method with good properties") and on the same page show its CAKKT notion is "strictly weaker than the less stringent AGP condition".
- **X5. SSC-OMP's accuracy.** Its own paper presents it as scalable with subspace-preserving guarantees. Outside users report poor results under noise (Peng–Pavlidis, Vielhaben et al.), on small data (Lipor et al.) and in hyperspectral clustering (Hinojosa et al.). It is nevertheless a default scalable baseline in later deep-clustering benchmarks (S2 contexts, e.g. Chu et al. ICLR 2023, arXiv:2306.05272).
- **X6. The complexity yardstick.** Curtis–Robinson (ISMP 2018): "Our worst-case analysis for nonconvex optimization is faulty." Meanwhile Robinson co-authored at least four complexity-bound papers (TRACE, the inexact regularized-Newton framework, the trust-funnel complexity paper, TR-Newton-CG), and CGT incorporated the CRS class into their optimality theory.
- Audit 2026-10-17: in §4.2 (and R4, §10), "this analysis considers unscaled approximate first-order critical points" describes Birgin et al. [6], not Cartis–Gould–Toint's own analysis, which also uses a scaled measure and groups the Curtis–Robinson–Samadi funnel bounds with its earlier scaled-KKT bounds [21] as "of the same order"; no dispute is documented (arXiv:1705.07285v2 pp. 2, 24, 27).

## Gaps

- **Referee reports and rebuttals:** none public. His optimization venues use closed review. The CVPR/ICCV/NeurIPS/ICML papers with Vidal were not checked on OpenReview (most predate open reviewing at those venues).
- **Failed replications:** none found. The closest items are O'Neill's rerun of the BCRZ code (section 7) and Adachi et al.'s run of GALAHAD TRS (section 3).
- **Paywalled full texts not read:**
  - the Izmailov–Solodov TOP discussion paper itself;
  - the Fischer, Martínez and Mordukhovich comments (only the rejoinder's summary of them was read);
  - the body of Izmailov–Solodov 2016;
  - Izmailov–Solodov–Uskov, Comput. Optim. Appl. 62 (2015) 405–429 (DOI 10.1007/s10589-015-9744-6) and J. Optim. Theory Appl. 169 (2016) 148–178 (DOI 10.1007/s10957-016-0889-y). Their contexts name "pdSQP" and the "primal-dual augmented Lagrangian", but any numerical comparison with Robinson's methods is unknown;
  - Izmailov–Uskov, Comput. Optim. Appl. 67 (2017) 129–154 (DOI 10.1007/s10589-016-9890-5);
  - Haeser 2018 (COAP and Oper. Res. Lett. 46(3) 295–299, DOI 10.1016/j.orl.2018.02.007);
  - Verschueren et al. 2017;
  - Ahmadzadeh–Mahdavi-Amiri 2022 (abstract only);
  - Gould–Robinson 2012 (IMA JNA);
  - Gill–Kungurtsev–Robinson 2017 (both papers);
  - Robinson, JOTA 166 (2015) 137–171 (DOI 10.1007/s10957-015-0708-x). Its S2 context self-notes that inexact SQO's "practical performance has not yet been evaluated".
- **Gill–Robinson pdAL (Comput. Optim. Appl. 51 (2012) 1–25, DOI 10.1007/s10589-010-9339-1):** Semantic Scholar returned zero citing records, so critique of the thesis-line merit function was not harvested.
- **FaRSA and group-sparse methods:** no outside critique found. Possible reasons: low citation counts (30 and 10 records) dominated by the group's own papers. Tianyi Chen's later Microsoft work cites FaRSA among methods "quite limited" for stochastic nonconvex use (S2 context, arXiv:2011.04868). Venue not confirmed, so not entered as a finding.
- **ADMM / continuous-time papers with França and Vidal:** 89 citing records for arXiv:1805.06579. The only critical context found was about a different França paper (9.3).
- **Leads without a verifiable venue or resolvable identifier (not entered as findings):**
  - J.-H. Hours, EPFL thesis 2016 ("the convergence of SQP methods is not robust to inexact solutions of the subproblems"; the DOI 10.5075/epfl-thesis-6875 did not resolve at Crossref);
  - Haeser & Ramos, "A survey of constraint qualifications with second-order properties in nonlinear optimization" (2018; venue not confirmed).
- **Who disputed "codes fail too often"** (ISMP 2018), and any CGT reply to the regional-complexity critique: not found.
- **MathSciNet reviews:** not read (subscription). zbMATH was not queried in this run.
- **Recent lines (2024–2026):** proximal-gradient constrained methods, fairness via constrained stochastic optimization, progressively sampled equality constraints, and active-set identification under noise are too recent for published critique. None found.

## Sources

One line each: title, author(s), date, identifier or URL, primary/secondary. "Read" means the full text was opened at the pages cited. "Context only" means a Semantic Scholar citation context.

1. Robinson, "Comments on: Critical Lagrange multipliers: what we currently know about them, how they spoil our lives, and what we can do about it", TOP 23(1) (2015) 43–47, DOI 10.1007/s11750-015-0371-2, read (primary)
2. Izmailov, Solodov, "Rejoinder on: Critical Lagrange multipliers…", TOP 23(1) (2015) 48–52, DOI 10.1007/s11750-015-0373-0, read (primary)
3. Izmailov, Solodov, "Critical Lagrange multipliers: what we currently know about them, how they spoil our lives, and what we can do about it", TOP 23(1) (2015) 1–26, DOI 10.1007/s11750-015-0372-1, not read (paywall); context only (secondary)
4. Crossref listing of TOP 23(1) (2015): comments by Fischer (DOI 10.1007/s11750-015-0368-x), Martínez (10.1007/s11750-015-0369-9) and Mordukhovich (10.1007/s11750-015-0370-3), not read (secondary)
5. Fernández, Solodov, "Stabilized sequential quadratic programming: a survey", Pesquisa Operacional 34(3) (2014) 463–479, DOI 10.1590/0101-7438.2014.034.03.0463, read (primary)
6. Andreani, Cárdenas, Ramos, Ribeiro, Secchin, "On the convergence of augmented Lagrangian strategies for nonlinear programming", Optimization Online 2020/03/7701 (revised Dec 2020), read; published IMA J. Numer. Anal. 42(2) (2022) 1735–1765, DOI 10.1093/imanum/drab021 (primary)
7. Andreani, Ramos, Secchin, "Improving the Global Convergence of Inexact Restoration Methods for Constrained Optimization Problems", SIAM J. Optim. 34(4) (2024) 3429–3455, DOI 10.1137/22m1493811, context only (secondary)
8. Haeser, "A second-order optimality condition with first- and second-order complementarity associated with global convergence of algorithms", Comput. Optim. Appl. 70(2) (2018) 615–639, DOI 10.1007/s10589-018-0005-3, context only (secondary)
9. Verschueren, Zanon, Quirynen, Diehl, "A Sparsity Preserving Convexification Procedure for Indefinite Quadratic Programs Arising in Direct Optimal Control", SIAM J. Optim. 27(3) (2017) 2085–2109, DOI 10.1137/16M1081543, context only (secondary)
10. Izmailov, Solodov, "Some new facts about sequential quadratic programming methods employing second derivatives", Optim. Methods Softw. 31(6) (2016) 1111–1131, DOI 10.1080/10556788.2016.1177528, abstract read (OpenAlex) plus context; body not read (secondary)
11. Izmailov, Solodov, Uskov, "Combining stabilized SQP with the augmented Lagrangian algorithm", Comput. Optim. Appl. 62(2) (2015) 405–429, DOI 10.1007/s10589-015-9744-6, context only (secondary)
12. Izmailov, Solodov, Uskov, "Globalizing Stabilized Sequential Quadratic Programming Method by Smooth Primal-Dual Exact Penalty Function", J. Optim. Theory Appl. 169(1) (2016) 148–178, DOI 10.1007/s10957-016-0889-y, context only (secondary)
13. Gould, Robinson, "A second derivative SQP method: theoretical issues", Optimization Online 2008/10/2130, https://optimization-online.org/2008/10/2130/, read (primary); journal form SIAM J. Optim. 20(4) (2010) 2023–2048, DOI 10.1137/080744542 [inferred match]
14. Gould, Robinson, "A second-derivative SQP method with a 'trust-region-free' predictor step", IMA J. Numer. Anal. 32(2) (2012) 580–601, DOI 10.1093/imanum/drq043, context only (secondary)
15. Ahmadzadeh, Mahdavi-Amiri, "A competitive inexact nonmonotone filter SQP method: convergence analysis and numerical results", Optim. Methods Softw. 37(4) (2022) 1310–1343, DOI 10.1080/10556788.2021.1913155, abstract plus context (secondary)
16. GALAHAD source repository (ralna/GALAHAD, master): `src/README.packages` (last commit 2026-08-18), `src/forthcoming/README.forthcoming` (Oct 2016), headers of `oblivion/s2qp/s2qp.F90`, `oblivion/funnel/funnel.F90`, `forthcoming/fisqp/fisqp.F90`, `forthcoming/trace/trace.F90`, `trs/trs.F90`, `rqs/rqs.F90`, `dqp/dqp.F90`, and `lancelot/LANCELOT.template`, https://github.com/ralna/GALAHAD, read 2026-10-16 (primary)
17. Adachi, Iwata, Nakatsukasa, Takeda, "Solving the Trust-Region Subproblem By a Generalized Eigenvalue Problem", SIAM J. Optim. 27(1) (2017) 269–291, DOI 10.1137/16M1058200, Oxford ORA copy read (primary)
18. Zhang, Shen, Li, "On the Generalized Lanczos Trust-Region Method", SIAM J. Optim. 27(3) (2017) 2110–2142, DOI 10.1137/16M1095056, context only (secondary)
19. Al Daas, Gould, "Extended-Krylov-subspace methods for trust-region and norm-regularization subproblems", 2025, arXiv:2511.11135, context only (secondary)
20. Gould, Robinson, Thorne, "On solving trust-region and other regularised subproblems in optimization", Math. Program. Comput. 2(1) (2010) 21–57, DOI 10.1007/s12532-010-0011-7, Crossref-checked; not read (secondary)
21. Curtis, Gould, Robinson, Toint, "An interior-point trust-funnel algorithm for nonlinear optimization", Math. Program. 161 (2017) 73–134, DOI 10.1007/s10107-016-1003-9; Namur NTR 02/2014, https://pure.unamur.be/ws/files/13392465/NTR_02_2014.pdf, read (primary)
22. Cartis, Gould, Toint, "Optimality of orders one to three and beyond: characterization and evaluation complexity in constrained nonconvex optimization", J. Complexity 53 (2019) 68–94, DOI 10.1016/j.jco.2018.11.001; arXiv:1705.07285 v2 read (primary)
23. Curtis, Robinson, Samadi, "Complexity Analysis of a Trust Funnel Algorithm for Equality Constrained Optimization", SIAM J. Optim. 28(2) (2018) 1533–1563, DOI 10.1137/16m1108650, Crossref-checked; not read (secondary)
24. Curtis, Gould, Jiang, Robinson, "Adaptive augmented Lagrangian methods: algorithms and practical numerical experience", Optim. Methods Softw. 31(1) (2016) 157–186, DOI 10.1080/10556788.2015.1071813; arXiv:1408.4500 v1 read (primary)
25. Curtis, Jiang, Robinson, "An adaptive augmented Lagrangian method for large-scale constrained optimization", Math. Program. 152 (2015) 201–245, DOI 10.1007/s10107-014-0784-y, Crossref-checked; not read (secondary)
26. Cheng, Na, "Physics-Informed Neural Networks with Trust-Region Sequential Quadratic Programming", 2024, arXiv:2409.10777, read (primary)
27. Birgin, Martínez, "Complexity and performance of an Augmented Lagrangian algorithm", Optim. Methods Softw. 35(5) (2020) 885–920, DOI 10.1080/10556788.2020.1746962, context only (secondary)
28. Hamad, Hinder, "A simple and practical adaptive trust-region method", arXiv:2412.02079 v4 (2026), read (primary)
29. Hamad, Hinder, "A Consistently Adaptive Trust-Region Method", NeurIPS 35 (2022) 6640–6653, DOI 10.52202/068431-0481; arXiv:2408.01874 v1 read (primary)
30. Shen, Zhou, Fang, Ribeiro, "A Stochastic Trust Region Method for Non-convex Minimization", 2019, arXiv:1903.01540 v1, read (primary)
31. Curtis, Robinson, Royer, Wright, "Trust-Region Newton-CG with Strong Second-Order Complexity Guarantees for Nonconvex Optimization", SIAM J. Optim. 31(1) (2021) 518–544, DOI 10.1137/19M130563X; arXiv:1912.04365 v3 read (primary)
32. Wright, "Optimization in Theory and Practice", 2025, arXiv:2510.15734 v2, read (primary)
33. Jiang, He, Zhang, Ge, Jiang, Ye, "Beyond Nonconvexity: A Universal Trust-Region Method with New Analyses", J. Sci. Comput. 106 (2026), DOI 10.1007/s10915-025-03154-y; arXiv:2311.11489 v4 read (primary)
34. Curtis (joint with Robinson), slides "Characterizing Worst-Case Complexity of Algorithms for Nonconvex Optimization", ISMP, 3 July 2018, http://coral.ise.lehigh.edu/frankecurtis/files/talks/ismp_18.pdf, read (primary)
35. Cartis, Gould, Toint, "Worst-case evaluation complexity and optimality of second-order methods for nonconvex smooth optimization", Proc. ICM 2018, DOI 10.1142/9789813272880_0198; arXiv:1709.07180 v1 read (primary)
36. Curtis, Robinson, Samadi, "An Inexact Regularized Newton Framework with a Worst-Case Iteration Complexity of O(ε^-3/2) for Nonconvex Optimization", IMA J. Numer. Anal., DOI 10.1093/imanum/dry022; arXiv:1708.00475 v4 read (p. 3) (primary)
37. Curtis, Robinson, "Regional complexity analysis of algorithms for nonconvex smooth optimization", Math. Program. 187 (2021) 579–615, DOI 10.1007/s10107-020-01492-3, Crossref-checked; reception via context only (secondary)
38. Na, Anitescu, Kolar, "An adaptive stochastic sequential quadratic programming with differentiable exact augmented Lagrangians", Math. Program. 199 (2023) 721–791, DOI 10.1007/s10107-022-01846-z; arXiv:2102.05320 v2 read (primary)
39. Fang, Na, Mahoney, Kolar, "Fully Stochastic Trust-Region Sequential Quadratic Programming for Equality-Constrained Optimization Problems", SIAM J. Optim. 34(2) (2024) 2007–2037, DOI 10.1137/22M1537862; arXiv:2211.15943 read (primary)
40. Berahas, Curtis, Robinson, Zhou, "Sequential Quadratic Optimization for Nonlinear Equality Constrained Stochastic Optimization", SIAM J. Optim. 31(2) (2021) 1352–1379, DOI 10.1137/20m1354556; arXiv:2007.10525 v1 read (p. 26) (primary)
41. Curtis, Robinson, Zhou, "A Stochastic Inexact Sequential Quadratic Optimization Algorithm for Nonlinear Equality-Constrained Optimization", INFORMS J. Optim. 6(3–4) (2024) 173–195, DOI 10.1287/ijoo.2022.0008; arXiv:2107.03512 v1 read (p. 17) (primary)
42. O'Neill, "A Two Stepsize SQP Method for Nonlinear Equality Constrained Stochastic Optimization", arXiv:2408.16656 v2, read (p. 34) (primary)
43. Chen, Curtis, Robinson, "A Reduced-Space Algorithm for Minimizing ℓ1-Regularized Convex Functions", SIAM J. Optim. 27(3) (2017) 1583–1610, DOI 10.1137/16m1062259; arXiv:1602.07018 v1 read (primary)
44. You, Robinson, Vidal, "Scalable Sparse Subspace Clustering by Orthogonal Matching Pursuit", CVPR 2016, 3918–3927, DOI 10.1109/cvpr.2016.425; arXiv:1507.01238 v3 read (primary)
45. You, Li, Robinson, Vidal, "Oracle Based Active Set Algorithm for Scalable Elastic Net Subspace Clustering", CVPR 2016, 3928–3937, DOI 10.1109/cvpr.2016.426; arXiv:1605.02633 read (primary)
46. Hinojosa, Vera, Arguello, "A Fast and Accurate Similarity-Constrained Subspace Clustering Algorithm for Hyperspectral Image", IEEE JSTARS 14 (2021) 10773–10783, DOI 10.1109/JSTARS.2021.3120071; arXiv:2104.06975 read (primary)
47. Vielhaben, Blücher, Strodthoff, "Multi-dimensional concept discovery (MCD): A unifying framework with completeness guarantees", TMLR 2023, arXiv:2301.11911 v2, read (primary)
48. Peng, Pavlidis, "Weighted sparse simplex representation: a unified framework for subspace clustering, constrained clustering, and active learning", Data Min. Knowl. Discov. 36(3) (2022) 958–986, DOI 10.1007/s10618-022-00820-9; arXiv:2106.04330 v1 read (primary)
49. Lipor, Hong, Tan, Balzano, "Subspace clustering using ensembles of K-subspaces", Inf. Inference 10(1) (2021) 73–107, DOI 10.1093/imaiai/iaaa031; arXiv:1709.04744 v3 read (primary)
50. Li, Tao, Wu, Zhong, Fu, "Large-Scale Subspace Clustering by Independent Distributed and Parallel Coding", IEEE Trans. Cybern. 52(9) (2022) 9090–9100, DOI 10.1109/TCYB.2021.3052056, context only (secondary)
51. Giampouras, Haeffele, Vidal, "Implicit Bias of Projected Subgradient Method Gives Provable Robust Recovery of Subspaces of Unknown Codimension", ICLR 2022, arXiv:2201.09079, read (primary); also Suh, Roh, Ryu, ICML 2022, arXiv:2202.05501 v2, read and excluded (primary)
52. Aggregators and tools (secondary), all 2026-10-16:
    - Semantic Scholar Graph API citation contexts for 36 Robinson papers, https://api.semanticscholar.org/graph/v1/;
    - OpenAlex author A5082367556 and works, https://api.openalex.org/;
    - Crossref REST checks of 30 DOIs, https://api.crossref.org/works/;
    - one WebSearch (locating Izmailov–Solodov 2016), which led to the RUDN repository record https://repository.rudn.ru/en/records/article/record/3762/.

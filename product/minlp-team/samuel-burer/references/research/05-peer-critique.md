# 05 · Peer critique: blind spots, limits of applicability, judgements shown wrong

> **Researcher**: Samuel A. (Sam) Burer, University of Iowa (Tippie College of Business, Department of Business Analytics). Google Scholar BScCde0AAAAJ; DBLP pid 96/4845; ORCID 0000-0001-5886-458X; homepage https://sburer.github.io/.
> **Dimension**: research agent 05 of 06, peer critique (nuwa research-craft Phase 1).
> **Research date**: 2026-10-10.
> **Sources consulted**: 80, listed under "Sources" (54 primary, 26 secondary). Every paper named below has a DOI, an arXiv id or an Optimization Online (OO) entry that I checked with a tool in this run: Crossref (about 65 DOIs), the arXiv API and arXiv PDFs, Optimization Online pages, Springer article pages, the Semantic Scholar (S2) Graph API and the zbMATH Open API. Names that appear only inside a quotation (e.g. papers listed on Burer's slides) are quoted, not cited.
> **WebSearch calls used**: 1 of 2 (to find an open copy of Dunning, Gupta and Silberholz 2018).
> **Local corpus**: `references/sources/papers`, `essays`, `software` and `publications` hold only `.gitkeep`. There is no user-supplied material, so nothing below is marked "from user-supplied material". `sources/talks/` holds YouTube auto-caption transcripts saved by sibling agents of this run (not user-supplied). I quote the March 2023 Iowa talk only with the machine-transcription caveat. I did not open `private/`. I saved no transcript.
> **Method**:
> 1. I harvested the S2 citation contexts of 12 Burer papers: 3,578 citing records, 2,429 with contexts; one of the 12 (the 2015 gentle introduction) returned no citations. I filtered them for critique words (fail, counterexample, drawback, outperform, limitation, not guaranteed, intractable, key condition, interior, and so on).
> 2. Each lead was traced to the critic's own text where an open copy existed: arXiv full texts, OO preprints, open-access Springer articles, author PDFs.
> 3. Burer's own replies were read in his author copies (`sburer.github.io/papers/…`), in the 2021 correction note, in arXiv v1/v2/v3 of 2504.03996, in his GitHub READMEs, in the slides of 2 June 2023 and in the March 2023 talk transcript.
> 4. Public reviews: zbMATH Open lists 61 Burer documents. 10 have reviews, 8 of them readable, and all 8 are descriptive (see §7).
> **Tags**: [stated] = Burer said or wrote it alone · [stated-joint] = a co-authored Burer text · [practice] = what the record shows he did (papers, code, dates) · [observed] = what others wrote · [inferred] = my reading, which no source states. **P** = I read the item's own text in this run (full text, preprint, abstract page, slide, README, transcript). **S** = known only through an intermediary: an S2 citation-context snippet whose full text I did not read, a zbMATH review, aggregator metadata, or the sibling note `06-trajectory.md`.
> **Quoting**: quotes are verbatim. Symbols lost in PDF-to-text extraction are restored in square brackets, e.g. [≤]. The exception is superscripts flattened by extraction (written 10⁻⁵ where the text file shows "10-5"), which are restored without brackets. Mathematical LaTeX markup from abstracts is rendered. "(S2 snippet)" means the sentence comes from Semantic Scholar's extraction of the citing paper and I did not read that paper's full text. Page numbers are journal pages when I read the published version or an author copy with journal pagination. Otherwise they are preprint/PDF pages and are marked as such.
> **Relation to 06**: `06-trajectory.md` (sibling) already records the Burer–Ye correction and the 2504.03996 overclaim. I re-verified both from the primary documents in this run and added the critics' side, the arXiv v2 stage and the pre-publication error in the Burer–Ye knapsack example.

---

## 0. Overview: who criticised what, and whether Burer answered

| # | Target | Critic(s), year | Critique in one line | Kind | Answered? How |
|---|---|---|---|---|---|
| 1 | Burer & Ye 2020, Theorem 3 | F. Kılınç-Karzan and A. L. Wang (CMU), privately; published in the 2021 correction | The proof fails: the systems "cannot be simultaneously feasible" | judgement shown wrong | **Yes.** Correction note, theorem narrowed to diagonal instances, finders thanked by name (§1.1) |
| 2 | Burer & Ye 2020, knapsack example | Gang Luo, before publication | "an error in the knapsack example" | error | **Yes.** Fixed before print, thanked (§1.1) |
| 3 | Burer & Natarajan, arXiv 2504.03996v1 (2025): "solvable in polynomial time" | Shaoning Han (named in v3) | An error in the proof | judgement shown wrong | **Yes, in two steps.** v2 narrowed to n ≤ 3. v3 added an n = 4 counterexample verified in exact arithmetic, thanked Han and released code (§1.2) |
| 4 | Burer–Monteiro (BM) 2003/2005 convergence theory | Grippo–Palagi–Piccialli 2011; Grippo et al. (SpeeDP) 2010/2012; Palagi et al. 2012; Lu–Zhang 2012; Sagnol 2011; Castañeda–Goldstein–Studer 2016; Yang–Liang–Toh–Carlone 2023; Ding–Lu–Yang 2025 | Global convergence rests on a-posteriori assumptions about iterates; "no guarantees currently exist" | blind spot / limit | **Acknowledged, not repaired by him.** He flagged it himself in 2003 and called it "a partial result" in 2023. The later theory came from others (§2.1) |
| 5 | BM rank choice | Waldspurger–Waters 2020; O'Carroll–Srinivas–Vijayaraghavan 2022 | Rank ≈ √(2m) is essentially necessary, and BM can fail even above the Barvinok–Pataki bound | limit | **Not answered in print.** The 2023 retrospective slides cite only the positive results (§2.1) |
| 6 | SDPLR accuracy and speed | Malick–Povh–Rendl–Wiegele 2009; Wang–Chang–Kolter 2017; Brosch–Schwiddessen–Wiegele 2026; Liu–Wang–Liu 2004 (S) | Moderate accuracy; "clearly outperformed" on random SDPs; 43x–115x slower than the Mixing method on Max-Cut SDPs | benchmark | **Partly.** Burer–Choi 2006 targeted accuracy. The 2026 README still defaults to 1e-5 feasibility and 1e-3 gap (§2.2) |
| 7 | Rank-two Max-Cut heuristic (CirCut / BUR02, 2002) | Dunning–Gupta–Silberholz 2018 (best single heuristic); Benlic–Hao 2013 and Zhu–Lin–Ali 2013 (report beating it) | Mixed verdicts | benchmark | No response found. He left the line (§2.3) |
| 8 | Copositive representation 2009: key condition and proof exposition | Bomze–Jarre 2010 (published note); Lieder–Rad–Jarre 2015 (S); Bomze–Peng 2023 (S) | Condition stronger than needed; one direction of the proof "somehow less explicit" | refinement | **Absorbed.** His 2012 chapter says its proofs "have been inspired by [5, 9]", where [5] is Bomze–Jarre (§3.1) |
| 9 | Practical value of completely positive (CP) reformulations | Ito–Kim–Kojima–Takeda–Toh 2018; Bomze–Cheng–Dickinson–Lisser 2017; Dey–Kocuk 2025; Dür 2010 (S) | "mainly of theoretical interest", "not tractable in general" | limit | **Pre-empted** in 2009 ("'package' the difficulty") and hedged in 2015 (§3.2) |
| 10 | Basic CP program has no interior | Burer himself (2009); tested by Ito et al. 2018 | No Slater point | self-identified limit | **His proposed fix was confirmed** by Ito et al. (§3.3) |
| 11 | Doubly nonnegative (DNN) relaxation: strength vs cost | Bao–Sahinidis–Tawarmalani 2011 | DNN equals Shor + partial first-order RLT and costs about three orders of magnitude more time | benchmark | **Indirectly.** OptDNN 2010 (cheaper DNN solves) and "Faster, but weaker" 2014 (§3.4) |
| 12 | OptDNN 2010 algorithm | Bomze–Cheng–Dickinson–Lisser–Liu 2019 | "no convergence proof is available yet" | limit | No response found (§3.4) |
| 13 | KKT-branching B&B (2008/09) and QuadProgBB (2012) | Misener–Smadbeck–Floudas 2015 (S); Bonami–Günlük–Linderoth 2018; Xia–Vera–Zuluaga 2020; Beck–Pan 2017 (S); Dong–Luo 2018; Locatelli–Piccialli–Sudoso 2024/25; Lu et al. 2025 | First matched or beaten in segments, then overtaken. QuadProgBB is now "a former state-of-the-art solver" that "has not been further developed" | benchmark | **No response found.** Code last pushed 2016-07-08 (§4) |
| 14 | SOC-RLT for extended/two trust-region subproblems | Burer–Anstreicher themselves; Yang–Burer 2016; Montanher–Neumaier–Domes 2018 | Not exact when cuts intersect; SDP and spatial B&B have "orthogonal difficulties" | self-identified limit + benchmark | **Self-identified.** His non-intersecting conjecture was proved with his student in 2015 (§5) |
| 15 | 2023/2025 lifted relaxation for ball constraints | Kılınç-Karzan–Sun 2024/2025 | Both numerical conjectures proved true; the relaxation is "a particular case of the moment-sum-of-squares hierarchy" | confirmation + subsumption by a rival framework | n/a (§5) |
| 16 | Survey with Letchford 2012 | — | No critique found among 403 citation contexts | — | — (§6) |

---

## 1. Judgements shown wrong: errors found by peers

### 1.1 Burer & Ye (2020): a false theorem, found by Kılınç-Karzan and Wang

- **Target**: S. Burer and Y. Ye, "Exact semidefinite formulations for a class of (random and non-random) nonconvex quadratic programs", *Math. Program.* 181:1–17, 2020, DOI 10.1007/s10107-019-01367-2. Crossref links it to its correction, DOI 10.1007/s10107-021-01684-5 (*Math. Program.* 190:845–848; online 8 Jul 2021). [practice, P]
- **What the correction says** [stated-joint, P]: "This note reports an error in Theorem 3 of [1], which was pointed about [sic] by Prof. Fatma Kılınç-Karzan and Mr. Alex Wang of Carnegie Mellon University, whom we sincerely thank for bringing this to our attention." … "However, in truth the proof fails because, with this setup, the systems cannot be simultaneously feasible. Said differently, the probability that all systems are feasible is zero." … "Instead of the purported Theorem 3, we now prove an analogous theorem, except that it only applies to diagonal instances of (1)." (Springer correction page, read 2026-10-10.) His homepage copy is headed "Erratum to: … February 18, 2021" and is bound together with the original paper (`papers/053-rank-bounds.pdf`). [practice, P]
- **How the critics treated it in public** [observed, P]: none of the three texts of theirs that I checked (1911.09195 v1 and v3, and 2107.06885) mentions the error.
  - Wang & Kılınç-Karzan, "On the tightness of SDP relaxations of QCQPs" (arXiv 1911.09195; *Math. Program.* 193:33–73, 2022, DOI 10.1007/s10107-020-01589-9), v1 p. 2: "Burer and Ye [18] very recently gave some appealing deterministic sufficient conditions under which the standard SDP relaxation of general QCQPs is tight. In our paper, we continue this vein of research for general QCQPs initiated by Burer and Ye [18]."
  - The same paper, p. 4: "In a recent intriguing paper, Burer and Ye [18] gave a sufficient condition guaranteeing that the standard SDP relaxation of general QCQPs is tight."
  - The same paper, v3 (Nov 2020), footnote on p. 27: "In particular, the standard Shor SDP relaxation is only analyzed in the context of diagonal QCQPs."
  - Their 2021 tutorial (arXiv 2107.06885, p. 12) says their Theorem 1 "recovers Burer and Ye [18, Theorem 1] as a special case". Theorem 1 survived. Only Theorem 3, the one about random data, failed.
  - The criticism reached Burer privately and became public only through his own correction. [inferred from the absence of any mention in v1, v3 and the 2021 tutorial]
- **A second, earlier peer-found error in the same paper** [stated-joint, P]: the original paper's acknowledgements (author copy, p. 18 of `053-rank-bounds.pdf`) read: "We would also like to thank Gang Luo, who pointed out an error in the knapsack example."
- **Response pattern** [practice, P]: name the flaw precisely ("the proof fails because…"), show why it cannot be patched (probability zero), replace the theorem with the strongest provable special case (diagonal instances), and credit the finders by name. According to the sibling note 06, the CV keeps the original title and lists the erratum beside it, and his January 2021 talk title already had "Diagonal" in it. [S, via 06]
- **Era/resources**: this is a two-author theory paper with a senior co-author (Y. Ye; Stanford according to the sibling note 06 [S]). The correction says the failed proof tried to show that, "with high probability", all the systems are simultaneously feasible [stated-joint, P]. So the error sat in the probabilistic argument for random data, the "random" half of the title [inferred].

### 1.2 Burer, Natarajan (and Willemsen), arXiv 2504.03996: overclaim retracted in two steps

- **v1** (4 Apr 2025; Burer & Natarajan), abstract [stated-joint, P]: "We show that continuous quadratic submodular minimization with bounds is solvable in polynomial time using semidefinite programming". Section 2 states "Theorem 2. For all n and all submodular (Q, c, γ) …, problem (2) is a tight relaxation of (1)", proved "by induction on n with base case n = 1" (v1 pp. 6–8).
- **v2** (5 Apr 2026; same two authors), abstract [stated-joint, P]: "propose a polynomially sized semidefinite relaxation, which is provably tight for dimension n [≤] 3 and empirically tight for larger n." I searched the v2 text for "Shaoning", "counterexample", "not tight" and "thank": none of them occurs. **The narrowing came before any public credit to a finder.** [practice, P]
- **v3** (31 Aug 2026; Rick Willemsen added as third author) [stated-joint, P]:
  - Abstract: "provably tight for dimension n [≤] 3. Via an explicit counterexample for n = 4, we show that the relaxation is not tight in general, although it remains empirically tight on randomly generated instances."
  - p. 9: "Example 4 below shows that this cannot be extended; tightness fails already at n = 4."
  - p. 46: "What fails at n [≥] 4 is therefore this particular semidefinite certificate, not necessarily tractability itself. The complexity of minimizing a submodular quadratic over [0, 1]^n for n [≥] 4 remains open, and settling it will require either a different certificate or a hardness reduction. The experiments of Section 5.1 indicate that instances exhibiting a gap are highly non-generic, so the relaxation continues to perform well in practice even though it is not tight in general."
  - Acknowledgements, p. 46: "We thank Shaoning Han for pointing out an error in an earlier version of this paper."
- **Code** [stated, P]: the `submodular-tests` README says the repository "reproduces every computational claim the paper makes". It adds: "the paper's central new claim, that the relaxation is not tight for $n \ge 4$, is checked in exact rational arithmetic with no solver and no floating point."
- **Who found what, and when** [inferred]: v3 credits Han with "an error in an earlier version". Whether Han's report triggered the v2 narrowing or came later cannot be read from the versions. I found no public write-up by Han (see Gaps).
- **Era/resources**: 2025–26.
  - Mosek and Gurobi are available (`submodular-tests` README) [P]. The sibling note 06 reports AI coding assistants as commit co-authors in the same months [S, via 06].
  - Burer is a senior professor and department chair (homepage) [P]. His co-authors are K. Natarajan and, from v3, R. Willemsen. Both are listed in v3 under "Engineering Systems and Design, Singapore University of Technology and Design" [P]. Willemsen's role (student or staff) was not checked.

### 1.3 Natural conjectures falsified after publication: self-found, for comparison

- The `ballconstraints` README (2026) [stated, P]: the paper's lifted formulations "motivate two natural conjectures … These conjectures are **not statements made in the paper**. Both turn out to be false in dimension two". The repository adds a "self-contained exact verification of two projection counterexamples discovered after the paper".
- I found no outside critic here; the README does not name a finder. I list it so the pattern in §8 is complete. [practice, P]

### 1.4 Conjectures and predictions that others (or he) later confirmed

| His claim | Where | Outcome | Who settled it |
|---|---|---|---|
| "So we conjecture that the two values are equal when the cuts do not intersect." [stated-joint, P] | Burer & Anstreicher, SIOPT 2013 (DOI 10.1137/110826862), author copy p. 13 | **True.** zbMATH review (R. Reemtsen) of Burer & Yang 2015: "In this paper it is proved that in fact for each m there is no gap between both optimal values as long as the m linear constraints do not intersect" (LaTeX markup around m removed) [observed, S] | Burer & his student B. Yang, *Math. Program.* 149:253–264, 2015, DOI 10.1007/s10107-014-0749-1 |
| "is it possible to prove that our relaxation Beta is always at least as tight as Kron, which is supported by the computational evidence?" (plus a conjecture that Zhen et al.'s inequalities are redundant) [stated, P] | Burer, "A slightly lifted convex relaxation…", author copy (Feb 2023) p. 27; *Math. Program.* 211:157–179, 2025, DOI 10.1007/s10107-024-02076-1 | **True.** "In [6], it was conjectured that this lifted relaxation is provably tighter than the Kronecker RLT inequalities and Zhen et al.'s RLT inequalities are redundant for this lifted relaxation. We answer these two conjectures affirmatively." [observed, P] | Kılınç-Karzan & S. Sun, OO 2024/07 preprint p. 2; *Math. Program.* 2025, DOI 10.1007/s10107-025-02278-1 |
| The simplified CP program "may have an interior, whereas Feas(C) never does" [stated, P] | Burer 2009, p. 487 | **Supported.** "We prove that the possibility of the existence of interior feasible solutions becomes greater." [observed, P] | Ito, Kim, Kojima, Takeda, Toh, OO 2017/07 preprint p. 15; *J. Global Optim.* 72:619–653, 2018, DOI 10.1007/s10898-018-0676-4 |
| "we believe that LR5 will make the solution of maxcut SDPs for sparse graphs with tens of thousands of vertices a routine activity." [stated-joint, P] | Burer & Monteiro 2003, p. 355 | **Realised, but by successor codes.** SpeeDP: "we could run it on very large graphs with sizes of up to a million nodes" (OO 2010/10 preprint p. 1); the Mixing method ran roadNet-CA "(n=1971281 edges=2766607)" (arXiv 1706.00476v1 p. 6) [observed, P] | Grippo, Palagi, Piacentini, Piccialli, Rinaldi; Wang, Chang, Kolter. Whether this counts as his prediction "coming true" is [inferred] |

---

## 2. Low-rank SDP (Burer–Monteiro factorization, SDPLR), 2001–2006

**Era and resources**: Burer was a PhD student and then a new assistant professor (Georgia Tech to Iowa), coding in C with L-BFGS on single workstations. Interior-point codes of the day needed O(n²) memory or more for large SDPs. The critics below compare on later hardware and later codes: 2008 workstations (Malick et al.), 2017 machines (the Mixing method), MOSEK 11.0.20 and SCS 3.2.7 in 2025–26 (Brosch et al.), and GPUs for ALORA in 2025 (Ding–Lu–Yang). [practice, P]

### 2.1 Convergence theory: the gap critics named, and that he had named first

**What he wrote at the time** [stated-joint, P]:
- BM 2003 (*Math. Program.* 95:329–357, DOI 10.1007/s10107-002-0352-8), p. 342: "Firstly, we cannot guarantee that the regularity assumption of Proposition 4 holds at an arbitrary stationary point R of (Nr) obtained by the algorithm, and as such, the theoretical base for dynamically changing the rank is not strong."
- BM 2005 (*Math. Program.* 103:427–444, DOI 10.1007/s10107-004-0564-1), p. 427, calls their own 2003 method "the successful, yet experimental, algorithm of Burer and Monteiro [5]". The 2005 paper proves "the optimal convergence of a slight variant" under assumptions on the iterates.

**What critics wrote** [observed]:
- Grippo, Palagi, Piccialli, *Math. Program.* 126:119–146, 2011, DOI 10.1007/s10107-009-0275-8 (S2 snippet, cut off by S2): "The augmented Lagrangian approach introduced in [7], although quite effective in practice, has two intrinsic drawbacks, since a sequence of unconstrained minimizations need to be performed, and some a posteriori assumptions on the behavior of the sequence are needed in order to prove global…". The same paper: "Therefore, we feel that, at least in the particular case of the problem arising from the relaxation of max cut, our approach fills the gap left by the seminal work of Burer and Monteiro [7] [8]." [S]
- Grippo, Palagi, Piacentini, Piccialli, Rinaldi, SpeeDP (OO preprint 2010/10/2766, p. 4; published *Math. Program.* 136:353–373, 2012, DOI 10.1007/s10107-012-0593-0): "The resulting algorithm SDPLR-MC was computationally efficient, but the underlying convergence theory was not deeply investigated." p. 8: "However, problem (7) presents some peculiarities that make standard convergence results not immediately applicable." [P]
  - Palagi, Piccialli, Rendl, Rinaldi, Wiegele, "Computational approaches to Max-Cut" (handbook chapter, 2012, DOI 10.1007/978-1-4614-0769-0_28; S2 snippet): "The practical performance of this approach is pretty good, but the underlying convergence theory is not deeply investigated in [8]." [S]
- Lu & Zhang, *Math. Program.* 135:149–193, 2012, DOI 10.1007/s10107-011-0452-4 (arXiv 0907.2079v1, p. 40): "However, the classical augmented Lagrangian method generally cannot guarantee converging to a feasible point when applied to a nonconvex NLP. Due this [sic] and [19], at least theoretically, their approach [5] may not converge to a feasible point of the primal SDP." Here [5] is Burer–Monteiro. [P]
- Sagnol, *Linear Algebra Appl.* 435:1446–1463, 2011, DOI 10.1016/j.laa.2011.03.027 (arXiv 0909.5577, p. 2): "The resulting problem is non-convex, and so the augmented Lagrangian algorithm proposed in [BM03] is not guaranteed to converge to a global optimum. However, it performs remarkably well in practice, and some conditions which ensure that the returned solution is an optimum of the SDP are provided in [BM05]." [P]
- Castañeda, Goldstein, Studer, *IEEE TCAS-I* 63:2334–2346, 2016, DOI 10.1109/TCSI.2016.2607198 (arXiv 1609.01797, p. 5): "…other low-complexity SDP methods, such as those inspired by Burer and Montiero [sic] [54], which rely on non-convex augmented Lagrangian schemes for which no guarantees currently exist." [P]
- Yang, Liang, Toh, Carlone, *Math. Program.* 201:409–472, 2023, DOI 10.1007/s10107-022-01912-6 (arXiv 2105.14033, p. 5). For rank-one SDP relaxations with many constraints: "V fails the linear independence constraint qualification (LICQ) and it may not be a KKT point, making it pessimistic for nonlinear programming solvers to find." They add that successful B-M applications require few constraints relative to n (paraphrase; the inequality symbol is lost in extraction). [P]
- Ding, Lu, Yang, arXiv 2505.15775v1 (2025), p. 4. [14] is BM 2005, checked in their reference list: "However, a key limitation of this analysis is its reliance on assumptions of ALM iterates that are not guaranteed to hold or verify a priori." [P]

**How he answered** [stated, P; machine transcript]:
- March 2023 Iowa talk: "it wasn't a perfect result it's kind of a partial result … algorithms aren't actually guaranteed to go to local men's [mins] they're guaranteed to go to second order stationary points … so we had some kind of strong assumptions here but this was the best variable [sic, ASR] to do at that time".
- On the later theory: "we didn't really mean it but this was part of what people started to call benign non-convexity".
- The 2 June 2023 prize-lecture slides (sburer/2023-06_SIOPT, `test-of-time.pdf`, slide 43/63) restate the 2005 result with its condition intact: "If an unconstrained local minimum is attained at each step, then the overall algorithm converges to a global optimal solution". [stated-joint, P]
- **He wrote no new convergence paper.** The theory that later justified the method came from others:
  - Boumal, Voroninski, Bandeira: NeurIPS 2016 (arXiv 1606.04970) and *Comm. Pure Appl. Math.* 73:581–608, 2020 (DOI 10.1002/cpa.21830).
  - Cifuentes & Moitra (arXiv 1912.01745).

  [practice, P; the absence of a Burer theory paper is from the sibling's publication timeline, S]

### 2.2 How much rank is enough: results showing the method's limits

- Boumal, Voroninski, Bandeira (arXiv 1606.04970, abstract): "Remarkably, for some applications, local optimization methods seem to converge to global optima of these non-convex surrogates reliably. Although some theory supports this empirical success, a complete explanation of it remains an open question." [observed, P]
- Waldspurger & Waters, *SIAM J. Optim.* 30:2577–2602, 2020 (DOI 10.1137/19M1255318; arXiv 1812.03046v2), abstract: "In this article, we show that this result is essentially tight: for smaller values of the size, second-order critical points are not generically optimal, even when the global solution is rank 1." They grant the practice (p. 2): "Nevertheless, they work extremely well in many applications. … Numerical examples where this phenomenon occurs can be found in [Burer and Monteiro, 2003], …". [observed, P]
- O'Carroll, Srinivas, Vijayaraghavan, arXiv 2211.12389 (2022), abstract: "We prove that the Burer-Monteiro method can fail for the Max-Cut SDP on n vertices when the rank is above the Barvinok-Pataki bound (p [≥] √(2n)). We provide a family of instances that have spurious local minima even when the rank p = n/2. … this … justifies the use of beyond worst-case paradigms like smoothed analysis to obtain guarantees for the Burer-Monteiro method." [observed, P]
- Cifuentes & Moitra, arXiv 1912.01745, abstract: "Previous analyses were unable to give polynomial time guarantees for the Burer-Monteiro method, since they either assumed that the criticality conditions are satisfied exactly, or ignored the nontrivial problem of computing an approximately feasible solution." Cifuentes, *Optim. Lett.* 15:2299–2309, 2021 (DOI 10.1007/s11590-021-01705-4; arXiv 1904.07147) extends the generic guarantees to SDPs with inequalities and several PSD blocks. [observed, P]
- Beyond linear SDPs: R. Y. Zhang, *Math. Program.* 213:1009–1038, 2025 (DOI 10.1007/s10107-024-02160-6; S2 snippet): "For more realistic condition numbers L/μ [≥] 3, the Burer–Monteiro approach may continue to work well in practice, but one can no longer rule out failure by getting stuck at a spurious local minimum." [observed, S]
- **His answer**: none in print. The 2023 slides list only positive follow-ups:
  - Slide 55/63: "No spurious local minima in low-rank matrix completion and recovery (Ge-Lee-Ma 2016, Bhojanapalli-Neyshabur-Srebro 2016, Ge-Jin-Zheng 2017)" and "Convergence rates for block-coordinate descent on the MaxCut SDP (Erdogdu et al 2018)".
  - Images credited to Boumal (slides 45/63 and 57/63).
  - Slide 58/63: "When r > [√(2m)], in the setting of smoothed analysis, the low-rank approach solves SDPs to any desired accuracy in polynomial time (Cifuentes-Moitra 2021)".

  The strings "Waldspurger", "Carroll" and "fail" occur 0 times in the slide text. [practice, P]
- **Related practice** [stated-joint, P]: slide 35/63 says they "Also experimented with: Restricting the rank smaller than required by theory". So the regime later proved risky (below √(2m)) was one he had tried empirically.

### 2.3 Accuracy and speed of SDPLR against rival codes

**Burer's own framing** [stated-joint, P]:
- BM 2003, p. 342: "Moreover, it is likely that requiring much more accuracy would increase the time needed to solve the SDPs. Nonetheless, after much experimentation, we feel that 10⁻⁵ is a reasonable amount of infeasibility to require."
- BM 2005, p. 429: "From a practical point of view, this addresses a key drawback of the algorithm of Burer and Monteiro [5] in which lower bounds were not available."
- Burer & Choi, *Optim. Methods Softw.* 21:493–512, 2006 (DOI 10.1080/10556780500286582), p. 494: "It is important to note that, in general, the current implementations of (i) and (ii) have a difficult time solving (1) and (2) to high accuracy because they are not able to deal with the inevitable ill-conditioning encountered near optimality. … In this article, we address issues of robustness and accuracy in first-order algorithms for SDP." Here (ii) means "first-order non-linear programming algorithms [14-20]". Four of those seven references ([14]–[17]) are his own papers with Monteiro (and Zhang), so the admission covers his own codes.

**Critics and benchmarks** [observed]:
- Malick, Povh, Rendl, Wiegele, *SIAM J. Optim.* 20:336–356, 2009 (DOI 10.1137/070704575); OO preprint 2007/10/1800, version of 1 Sep 2008 [P]:
  - p. 3: "Strong computational results on large problems with medium accuracy have been reported for these algorithms."
  - p. 20: "In Table 3, we compare our method with the low-rank approach SDPLR of [BM03]. Since this is essentially a first order nonlinear optimization approach, it does not easily reach the same level of accuracy as our method. … We first note that SDPLR is clearly outperformed by both other methods."
  - The Table 3 caption: "Comparison on randomly generated SDPs".
  - Their acknowledgement: "We also thank Kim Toh and Sam Burer for making their codes available to us."
- Wang, Chang, Kolter, "The Mixing method" (arXiv 1706.00476v1, 2017), p. 11: "In the smaller GSET dataset, the Mixing method is 7.53x faster than Manopt, 43.62x faster than SDPLR, and 361x faster than DSDP on the time to reach the horizontal line. In the large dataset … the Mixing method is 40.01x faster than Manopt on all three data, and 114.83x faster than SDPLR when it is runnable." The horizontal line is a modest accuracy target. [P] A later version, known to me only as an S2 snippet, states they used "DSDP 5.8, SDPLR 1.03-beta, and Manopt 3.0 with their default parameters"; v1 gives no versions. [S]
- Boumal, arXiv 1506.00575 (2015; S2 snippet), on orthogonal synchronization: his Riemannian low-rank method's "computational cost seems to grow at the same rate as that of merely computing d dominant eigenvectors of the data matrix (EIG), thus outperforming interior point methods as well as SDPLR." [S]
- Liu, Wang, Liu, *Optim. Methods Softw.* 19:125–136, 2004 (DOI 10.1080/10556780410001647203; S2 snippet): "The computational experience with our method indicates that it is faster than Burer and Monteiro's low rank factorization method [11]." [S]
- Brosch, Schwiddessen, Wiegele, *Optim. Methods Softw.* 41:754–796, 2026 (DOI 10.1080/10556788.2026.2683647; arXiv 2507.20386v2) [P]:
  - p. 4: "The solver proved successful on some large-scale instances of (1) that were difficult for other solvers at the time. However, a known limitation of SDPLR is that it typically yields only moderately accurate primal feasible solutions, and the associated dual solutions are sometimes far from optimal. This shortcoming arises because SDPLR uses a standard augmented Lagrangian approach that does not explicitly target finding an accurate primal-dual pair."
  - The same paper also records an SDPLR strength (p. 13): "This appears to be caused by the block coordinate descent approach, since SDPLR [10] converges quickly on them to a moderate-precision solution."

**What he did later** [practice, P]: he revived the code as maintainer. `github.com/sburer/sdplr` was created 2023-10-05 and last pushed 2026-03-23. Its README lists the defaults "Feasibility tolerance | 1e-5" and "Duality gap tolerance | 1e-3": the 2003 accuracy target, unchanged. Whether this is a deliberate position or inertia is [inferred]; no statement found.

### 2.4 The rank-two Max-Cut heuristic (CirCut; "BUR02" in MQLib)

- Target: Burer, Monteiro, Zhang, "Rank-two relaxation heuristics for MAX-CUT and other binary quadratic programs", *SIAM J. Optim.* 12:503–521, 2002, DOI 10.1137/S1052623400382467. I checked the metadata only and did not read the paper.
- **An independent, systematic benchmark found it the best single heuristic** [observed, P]. Dunning, Gupta, Silberholz, *INFORMS J. Comput.* 30:608–624, 2018 (DOI 10.1287/ijoc.2017.0798); OO preprint 2015/05/4895, p. 14: "The best overall heuristic on the expanded instance library with respect to the performance of its mean solution across the five replicates for each instance was Max-Cut heuristic BUR02, which not only matched the best performance on 22.9% of instances but also had strictly better performance than any other heuristic on 16.2% of instances and a mean deviation of only 0.3%." The same study (p. 23) finds an algorithm portfolio better than always running BUR02 ("a mean probability of obtaining the best solution of 37%" versus BUR02's "15%"). The setting: 37 heuristics re-implemented, identical time limits, 3,296 instances (2,635 "interesting").
- **Rival heuristics report beating it on the G-set** [observed]:
  - Benlic & Hao, *Eng. Appl. Artif. Intell.* 26:1162–1173, 2013 (DOI 10.1016/j.engappai.2012.09.001); author PDF pp. 15, 17 [P]: "The other two popular Max-Cut approaches, SS and CirCut, can obtain the previous best-known result in 11 and 12 cases respectively". "the Post-hoc analysis shows that BLS statistically outperforms GRASP-TS, SS and CirCut". Their CirCut numbers "are taken from [19]", i.e. Martí, Duarte, Laguna, *INFORMS J. Comput.* 21:26–38, 2009, DOI 10.1287/ijoc.1080.0275, which I did not read.
  - Zhu, Lin, Ali, *INFORMS J. Comput.* 25:27–40, 2013 (DOI 10.1287/ijoc.1110.0492; S2 snippet) [S]: "A comparison of our algorithm with some recent max-cut algorithms proposed by Burer et al. (2002), Festa et al. (2002), and Marti et al. (2009), shows that our algorithm often outperforms them in terms of solution qualities (cut values) and run times."
- **His answer**: none found. The line ended for him around 2002; the 2023 slides mention it only as "Heuristically solving NP-hard problems using rank-2 approaches (with Y. Zhang)". [practice, P]

---

## 3. Copositive / completely positive (CP) representation (2009) and DNN relaxations

Target: S. Burer, "On the copositive representation of binary and continuous nonconvex quadratic programs", *Math. Program.* 120:479–495, 2009, DOI 10.1007/s10107-008-0223-z.

**Era and resources**: an assistant/associate professor in a business school, writing a sole-authored theory paper. Computation at the time meant DNN relaxations solved with interior-point SDP codes (n around 100 was already hard, by his own 2012 account below), then his own decomposition code (OptDNN, MATLAB, 2010). [practice, P]

### 3.1 A published note on the paper: Bomze & Jarre (2010)

- Bomze & Jarre, "A note on Burer's copositive representation of mixed-binary QPs", *Optim. Lett.* 4:465–472, 2010, DOI 10.1007/s11590-010-0174-1; OO preprint 2009/08/2368 (TR-ISDS 2009-04, Vienna) [observed, P]:
  - Abstract: "In an important paper, Burer … recently showed how to reformulate general mixed-binary quadratic optimization problems (QPs) into copositive programs … We also discuss why feasibility of the copositive program implies feasibility of the original mixed-binary QP, which can be derived from the arguments in Burer … without any further condition."
  - Preprint p. 3: "Somehow less explicit, the proofs in [2] also establish the converse, so that full equivalence of the two programs (P) and (C) is established. Since it may be not immediate that the arguments in [2] do not need any of the conditions (1) or (4) below, we provide an alternative, probably more explicit argument".
  - They also introduce a weaker condition: "To complement this result we define a weak key condition".
  - The tone is friendly. The critique is about exposition and the strength of a hypothesis, not about correctness.
- **His answer: absorption** [stated, P]. In his 2012 handbook chapter "Copositive Programming" (DOI 10.1007/978-1-4614-0769-0_8), p. 205: "The proofs for Proposition 8.1-8.2 and Theorem 8.1 have been inspired by [5, 9]." The reference list (p. 217) gives [5] as "Bomze, I., Jarre, F.: A note on Burer's copositive representation of mixed-binary QPs." Theorem 8.1 is stated as a closure statement, the topological view the note had proposed: "R = clconv(L1)". [practice, P]
- **Further work on the "key condition"** [observed, S]:
  - Lieder, Rad, Jarre, *Comput. Optim. Appl.* 61:669–688, 2015 (DOI 10.1007/s10589-015-9731-y; S2 snippets): "The tightness of the copositive reformulation in [5] heavily depends on the so called key condition". "It was already noted in [11], that enforcing the key condition in [5] has no effect on its semidefinite relaxation." I did not identify which paper [11] is.
  - Bomze & Peng, *Comput. Optim. Appl.* 84:703–735, 2023 (DOI 10.1007/s10589-022-00440-5; S2 snippet): a relaxation "which is exact under conditions that significantly generalize the classical approach (Burer's key condition)".

### 3.2 "Mainly of theoretical interest": is the reformulation practically useful?

- **His pre-emptive framing in the original paper** [stated, P], 2009 p. 480: "While expressing a problem as a COP or CPP does not resolve the difficulty of the problem, it does allow one to "package" the difficulty completely inside the convex cones of copositive and/or completely positive matrices. Whatever knowledge is then gained about copositive or completely positive matrices can be applied uniformly to multiple types of NP-hard problems."
- **Critics** [observed]:
  - Ito, Kim, Kojima, Takeda, Toh (2018; OO preprint p. 2) [P]: "However, these CPP reformulations of QOPs are mainly of theoretical interest as CPPs are known to be numerically intractable [18]. … But the computational burden of solving a DNN problem increases very rapidly with the matrix size."
  - Bomze, Cheng, Dickinson, Lisser, *Math. Program.* 166:159–184, 2017 (DOI 10.1007/s10107-017-1109-8); OO preprint 2016/05/5455 [P]:
    - Abstract: "Triggered by Burer's seminal characterization from 2009, many copositive reformulations of mixed-binary QPs have been discussed by now. Most of them can be used as proper relaxations, if the intractable co(mpletely)positive cones are replaced by tractable approximations."
    - p. 6: "Unfortunately, optimizing over the completely positive cone is a very difficult problem (in fact an NP-hard problem [6, 15, 17])".
    - p. 2: "although the primal CP problems are all identical, their relaxations and their duals (and the relaxation of the duals) may differ, which is important in practical implementations."
  - Dey & Kocuk (team member Dey), arXiv 2510.16595 (2025), introduction [P]: "For instance, the results in [10] imply that conv(S2) can be obtained as a completely positive cone representable set although this representation is not tractable in general." Here [10] is Burer 2009.
  - Dür, "Copositive Programming – a Survey", in *Recent Advances in Optimization and its Applications in Engineering*, Springer 2010, pp. 3–20 (DOI 10.1007/978-3-642-12598-0_1; S2 snippet) [S]: "The algorithm is not adequate for general models derived from Burer's result [19], and provides only poor results for box-constrained quadratic problems." **Which algorithm the sentence means: not read.** The open copy at research.rug.nl returned a Cloudflare challenge (HTTP 403) to curl and to WebFetch.
- **Positive verdicts in the same community** [observed, S]: Dür & Rendl, *EURO J. Comput. Optim.* 9:100021, 2021 (DOI 10.1016/j.ejco.2021.100021; S2 snippet): "Copositive optimization experienced a breakthrough with Burer's 2009 paper [25]."
- **His later hedging** [stated, P]:
  - 2012 chapter p. 214: "Computationally, approaches involving techniques of the two preceding paragraphs have mostly been limited to small or medium sized problems. … even r = 0 can present a challenge for off-the-shelf interior-point methods for, say, n [≥] 100."
  - "A gentle, geometric introduction to copositive optimization" (*Math. Program.* 151:89–116, 2015, DOI 10.1007/s10107-015-0888-z), preprint p. 3: "we do not claim to have identified the best or only way to solve each of the various problem types--or that these are the most practically relevant problem classes. Moreover, we do not compare with other methods, e.g., branch-and-bound techniques, methods that exploit sparsity in the problem, or higher-order lifting approaches." Preprint p. 2: "Of course, characterizing all copositive cuts will be extremely difficult, but any progress can be applied uniformly to many different problems. This is the promise and the goal of copositive optimization."

### 3.3 No interior point: a limit he named, a fix others tested

- [stated, P] 2009 p. 487: "an additional benefit of [the simplified program] over (C) is that [its feasible set] may have an interior, whereas Feas(C) never does. This is an important feature … since the existence of an interior is generally a benefit both theoretically and computationally." Also: "(This argument also shows that the lack of interior for (C) will also hold for any semidefinite relaxation.)" The prime on the program's name is lost in text extraction; the bracketed words are my substitution.
- 2012 chapter p. 208 [stated, P]: "However, it seems difficult to establish general conditions under which R0 is guaranteed to have an interior."
- Tested by Ito et al. (2018; OO preprint p. 15) [observed, P]: "It is suggested by Burer in [9] that the simplification technique can increase the possibility of the existence of interior feasible solutions. … We prove that the possibility of the existence of interior feasible solutions becomes greater." On p. 3 they add: "We show that the technique has the potential to reduce possible primal/dual degeneracy."

### 3.4 The DNN relaxation: strength vs cost (Sahinidis' group) and his algorithmic replies

- Bao, Sahinidis, Tawarmalani, *Math. Program.* 129:129–157, 2011 (DOI 10.1007/s10107-011-0462-2), abstract [observed, P]: "it is shown that the recently developed doubly nonnegative relaxation is equivalent to the Shor relaxation, when the latter is enhanced with a partial first-order relaxation-linearization technique. These two relaxations are shown to theoretically dominate six other SDP relaxations. A computational comparison reveals that the two dominant relaxations require three orders of magnitude more computational time than the weaker relaxations, while providing relaxation gaps averaging 3% as opposed to gaps of up to 19% for weaker relaxations, on 700 randomly generated problems with up to 60 variables." Their "doubly nonnegative relaxation [18]" is derived from Burer 2009 (S2 snippet: "In this section, we describe copositive and doubly nonnegative relaxations for QCQP derived from copositive representations by slightly generalizing results from [18] and [5]"). [S for the reference mapping]
- **His replies, as research moves** [practice, P]:
  - OptDNN, *Math. Program. Comput.* 2:1–19, 2010 (DOI 10.1007/s12532-010-0010-8). Abstract: "Optimizing a DNP, while polynomial, is expensive in practice for interior-point methods. In this paper, we propose a practically efficient decomposition technique, which approximately solves the DNPs while simultaneously producing lower bounds". And: "to the best of our knowledge, the resulting algorithm for globally solving BoxQPs is the most efficient to date."
  - He also reported a negative result in the same paper, p. 17: "Though our method was successful for p [≤] 50, it was not competitive with the specialized method of [20]." [stated, P]
  - Burer, Kim, Kojima, "Faster, but weaker, relaxations for quadratically constrained quadratic programs", *Comput. Optim. Appl.* 59:27–45, 2014 (DOI 10.1007/s10589-013-9618-8). Abstract: "A downside is that the calculated bounds are weaker than those gotten by SDP. The framework allows one to choose a block-diagonal structure for the mixed SOCP-SDP, which in turn allows one to control the speed and bound quality." [stated-joint, P]
- A critique of the OptDNN algorithm itself [observed, P]: Bomze, Cheng, Dickinson, Lisser, Liu, *Comput. Manag. Sci.* 16:593–619, 2019 (DOI 10.1007/s10287-018-0337-6), abstract: "This approach is in some sense similar in spirit to the alternating projection method proposed in Burer (Math Program Comput 2:1–19, 2010) which completely avoids SDPs, but for which no convergence proof is available yet." **No reply found.**

---

## 4. KKT-branching branch-and-bound and QuadProgBB (2005–2012): benchmarked by rival schools

Targets:
- Burer & Vandenbussche, *Math. Program.* 113:259–282, 2008 (DOI 10.1007/s10107-006-0080-6).
- Burer & Vandenbussche, *Comput. Optim. Appl.* 43:181–195, 2009 (DOI 10.1007/s10589-007-9137-6), whose abstract calls the method "a state-of-the-art method for globally solving box-constrained nonconvex quadratic programs".
- Chen & Burer, *Math. Program. Comput.* 4:33–52, 2012 (DOI 10.1007/s12532-011-0033-9).

**Era and resources**: MATLAB codes written with PhD students (Jieqiu Chen, PhD 2010). Benchmarks were against BARON, Couenne and CPLEX of the late 2000s. Commercial MILP/MIQCP solvers later added nonconvex QP: CPLEX by the time of Bonami et al. (2018), and the Gurobi 10.0.2 used by Locatelli et al. GitHub `sburer/QuadProgBB` was created 2014-01-20 and last pushed 2016-07-08. [practice, P]

**His own claims and their scope** [stated-joint, P]:
- Chen & Burer 2012, p. 34: "we assume the feasible set of (QP) is bounded".
- p. 35: "The results demonstrate that our algorithm solves (QP) faster than the one by Burer and Vandenbussche on most of the test instances."
- Burer & Vandenbussche 2008, p. 271, on one of their own relaxation components: "From a practical standpoint, we have actually never observed a situation in our test problems for which the optimal value of (SDP1) is strictly lower than that of (SDP0). We believe this is evidence that the specific function [...] is rather weak".

**Critics and benchmarks, in time order** [observed]:

1. **Misener, Smadbeck, Floudas** (team member Misener), *Optim. Methods Softw.* 30:215–249, 2015, DOI 10.1080/10556788.2014.916287 (S2 snippet) [S]: "GloMIQO 2 is therefore comparable to the specialised QP solvers of Burer and Vandenbussche [25] and Chen and Burer [32] that address 78 and 85, respectively, of the 90 problems in a 10 hour time limit." Their test set: "The BoxQP test set was expanded to 90 problems by Burer and Vandenbussche [25]; we used the problems at http://dollar.biz.uiowa.edu/~sburer/…".
2. **Bonami, Günlük, Linderoth** (MILP/LP-based school), *Math. Program. Comput.* 10:333–382, 2018 (DOI 10.1007/s12532-018-0133-x); OO preprint 2016/06/5488 [P]:
   - Abstract: "Our linear programming based solver is competitive with SDP-based state of the art solvers on small instances and sparse instances. Most of our computational techniques have been implemented in the recent version of CPLEX".
   - Preprint p. 25: "It should be noted that for the large and dense problems in our test suite, the performance of the semidefinite-programming based solver QuadProgBB dominates the other solvers. For example, for jumbo/high-density instances, the average final optimality gap for QuadProgBB after two CPU hours is 0.13%, while the gap is orders of magnitude larger for the other three solvers." (The other three: bgl, BARON, GloMIQO.)
   - S2 snippet of the published version: "S≥0 is only computed approximately in QuadProgBB". [S]
3. **Xia, Vera, Zuluaga**, *INFORMS J. Comput.* 32:40–56, 2020 (DOI 10.1287/ijoc.2018.0883; arXiv 1511.02423v3, abstract) [P]: "quadprogIP is shown to typically outperform by orders of magnitude quadprogBB, BARON, and CPLEX on standard QPs. For general QPs, quadprogIP outperforms quadprogBB … For box-constrained QPs, quadprogIP has a comparable performance to quadprogBB and BARON in small- to medium-scale instances, but is outperformed by these solvers on large-scale instances … Also, unlike quadprogBB, the solution approach proposed here is able to solve QP instances whose dual feasible set is unbounded."
4. **Beck & Pan**, *J. Global Optim.* 69:309–342, 2017 (DOI 10.1007/s10898-017-0521-1; S2 snippets) [S], on Chen & Burer's ball-and-linear instances: "The performances of Algorithm BB on the example cases of [11] was superior to both methods described in [11] and [7]". "…seconds or less, in contrast to few minutes reported in [11]". Here [11] is Chen and Burer, per their own text "Chen and Burer [11]".
5. **Dong & Luo** (Dong was Burer's PhD student, 2011, co-advised with Anstreicher, per the sibling note 06 [S]), arXiv 1811.08122v1, pp. 2–3 [P]: "Despite successes in some special cases, e.g., … nonconvex quadratic program with linear constraints [14], in general it is difficult to exploit such strong conic relaxations within a branch-and-bound framework due to the lack of stable and scalable SDP algorithms." Their reference list gives [14] as "Samuel A. Burer and Jieqiu Chen. Globally solving nonconvex quadratic programming problems via completely positive programming".
6. **Locatelli, Piccialli, Sudoso**, *Math. Program. Comput.* 17:231–263, 2025 (DOI 10.1007/s12532-024-00270-y); arXiv 2211.08911v2 [P]:
   - p. 16: "According to some recent results presented in [4, 42], the best solvers for BoxQP problems are Cplex and, for instances with a large density, the SDP-based branch-and-bound approach QuadprogBB [11]."
   - p. 16, on small low-density instances: "Here, the high quality of the SDP bounds used by QuadprogBB and our solver is not able to compensate for the high computational cost."
   - p. 18: "QuadprogBB outperforms BARON, and becomes more competitive at large densities, as already observed in the literature." "Our B&B approach always outperforms QuadprogBB".
   - p. 18: "Moreover, we point out that QuadprogBB has not been further developed in recent years. Therefore, we believe that its computing times can be improved. For instance, it could be enhanced through the use of a first-order solver like SDPNAL+."
7. **Lu, Fei, Kang, Qu, Deng, Jin, Fang**, arXiv 2508.20897v1 (2025), p. 10 [P]: "We also evaluated QuadprogBB [Chen and Burer, 2012], a former state-of-the-art solver, but it was consistently slower than Gurobi and thus excluded from further comparisons." p. 8: "Prior studies by Xia et al. [2020] have shown that quadprogIP outperforms quadprogBB [Chen and Burer, 2012] and other solvers".

**His answer**: none found. No later QuadProgBB release, paper or comment after 2016. [practice, P; absence from the repository history and the citation scan]

---

## 5. SOC-RLT relaxations for trust-region variants (2011 →)

- **Limits stated by him first** [stated-joint, P]:
  - Burer & Anstreicher, *SIAM J. Optim.* 23:432–451, 2013 (DOI 10.1137/110826862), author copy p. 3: the paper "answers the question affirmatively for TRS2p and also provides a tighter--but still not exact--relaxation scheme for TTRS".
  - The same paper, p. 13: an explicit n = 3 instance with intersecting cuts on which the relaxation is not exact, and the conjecture for non-intersecting cuts (true; see §1.4).
  - Yang & Burer, *SIAM J. Optim.* 26:661–680, 2016 (DOI 10.1137/130945880), p. 662: "The paper [8] shed some light on this question by providing valid second-order-cone constraints tightening the basic SDP relaxation of TTRS, but even these relaxations are still not tight."
- **Others built on his counterexample rather than against it** [observed, S]: Yuan, Wang, Ai, Shuai, *SIAM J. Optim.* 27:890–909, 2017 (DOI 10.1137/16M1080082; S2 snippet): "Otherwise, in the intersecting case, a counterexample presented in [6] shows that there may be v(QP_L) > v(SOCP_L)".
- **Benchmark against spatial branch-and-bound** [observed, P]: Montanher, Neumaier, Domes, *J. Global Optim.* 71:915–934, 2018 (DOI 10.1007/s10898-018-0649-7, open access).
  - p. 918: "Burer and Anstreicher [14] generated a set of 1791 instances … Most of these problems were solved to [ε]-optimality ([ε] = 10⁻⁴) by the standard SDP relaxation. The other--more difficult--212 instances were sent to us by Kurt Anstreicher".
  - p. 930: "In Yang and Burer [46] and Anstreicher [6], all but 56 = 10 + 15 + 31 of the 212 test problems were solved with more sophisticated semidefinite relaxations, using SOC-RLT cuts and Kronecker product constraints, respectively."
  - p. 931: "We also note that every instance not solved by Baron can be solved by SDP-relaxations."
  - pp. 931–932: "On the other hand, solving one of the powerful SDP relaxations consumes significantly more time than the time spent otherwise on a node. Thus while there is potential for combining the approaches, it needs good judgment in how the combination is done. We are not aware of any complete solver which combines SDP relaxations and branch-and-bound."
  - Conclusion: "We also observed that SDP relaxations and branch-and-bound have orthogonal difficulties."
  - Solvers tested: Antigone 1.1, Baron 16.12.7, Lindo Global 10.0, Couenne 0.5, SCIP 3.2. Licences came from Misener, Sahinidis and Wiley (their acknowledgements).
- **Subsumption by a rival framework** [observed, P]: Kılınç-Karzan & Sun (2024/2025, §1.4), abstract: "In addition, we establish that Burer's lifted relaxation is a particular case of the moment-sum-of-squares hierarchy." The same note credits the relaxation (p. 2): "although it is not an exact relaxation for general m > 2, its [sic] admits a very good numerical performance in terms of both relaxation quality and efficiency of computation."

---

## 6. The 2012 survey with Letchford: no critique found

- Burer & Letchford, "Non-convex mixed-integer nonlinear programming: A survey", *Surv. Oper. Res. Manag. Sci.* 17:97–106, 2012, DOI 10.1016/j.sorms.2012.08.001. S2 lists 636 citing records, 403 with contexts. The critique-word filter returned only uses of the survey as an authority for the claim that non-convex MINLP is hard or expensive (for example: "the continuous relaxation of a nonconvex MINLP can be intractable and computationally expensive"). Nothing criticised the survey itself. [observed, S]
- Team-member uses are neutral citations:
  - Belotti, Kirches, Leyffer, Linderoth, Luedtke, Mahajan, *Acta Numerica* 22:1–131, 2013 (DOI 10.1017/S0962492913000032; S2 snippet): "We refer the reader to the works of Tawarmalani and Sahinidis (2002) and Burer and Letchford (2012a) for additional surveys focused on nonconvex MINLP." [S]
  - Gupte, Ahmed, Dey, Cheon on pooling (S2 snippet): "The state-of-the-art technique seems to be to solve the pooling problem using branch-and-cut algorithms developed for nonconvex MINLPs (Belotti et al., 2013; Burer and Letchford, 2012)". [S]
- **A prediction in the survey, not assessed** [stated-joint, P]: "Finally, we believe there will be an increasing place for heuristics and approximation algorithms for non-convex MINLPs" (author copy p. 9). I did not assess whether it came true (see Gaps).

---

## 7. Public reviews (zbMATH Open)

zbMATH Open lists 61 documents. 10 have a review: 8 have readable text and 2 are blocked by a licence ("contents unavailable due to conflicting licenses"). All 8 readable reviews are descriptive summaries, with mild praise and no criticism [observed, S]:
- D. Henrion on Burer–Monteiro–Zhang 2002 (Zbl 1006.90060): "the authors of this very well written paper propose alternative SDP algorithms".
- E. Rappos on Burer–Letchford 2014 (Zbl 1291.90146): "this very interesting paper".
- R. Reemtsen on Burer–Yang 2015 (Zbl 1308.90121): confirms the 2013 conjecture was proved (§1.4).

No critical review found.

---

## 8. Patterns: how he responds to critique (evidence first, reading second)

Each pattern below is my reading [inferred], built only on the items cited in it.

1. **He names his own weak points in the original paper, often before critics do.**
   - BM 2003: "the theoretical base … is not strong".
   - BM 2005: "successful, yet experimental".
   - Burer 2009: the reformulation "does not resolve the difficulty" and the basic program "never" has an interior.
   - SOC-RLT 2013: "tighter--but still not exact", with a counterexample.
   - OptDNN 2010: "not competitive with the specialized method".
   - Faster-but-weaker 2014: the title itself.

   [stated / stated-joint, P]
2. **Errors found by others get a formal, narrow, credited correction.** He does not write rebuttals.
   - The 2021 correction (Kılınç-Karzan, Wang) and the 2026 v3 (Han) both name the finder, explain why the claim fails and keep the provable part.
   - I found no published reply or rebuttal to any critic.

   [practice, P]
3. **Published comments are absorbed into the next exposition.** Bomze–Jarre's closure viewpoint reappears in the 2012 chapter, credited ("inspired by [5, 9]"). [stated, P]
4. **Cost critiques are answered with a new algorithm or an explicit trade-off, not a defence.**
   - Accuracy: Burer–Choi 2006.
   - DNN cost: OptDNN 2010.
   - SDP cost: "Faster, but weaker" 2014.

   [practice, P]
5. **The theory that justified his best-known method came from others, and his retrospective cites only its positive side.**
   - The 2023 slides list Boumal, Cifuentes–Moitra, Ge–Lee–Ma and others.
   - They omit Waldspurger–Waters and O'Carroll et al.
   - Orally he concedes "a partial result" and "strong assumptions".

   [practice, P; stated, P (machine transcript)]
6. **He leaves a line rather than defending it.** No response appeared to the QuadProgBB, CirCut or OptDNN critiques. Benchmarks then describe QuadProgBB as "not further developed" and "former state-of-the-art". The exception is SDPLR, which he revived as maintainer in 2023–26. [practice, P]
7. **Open code and open instances make him easy to benchmark against.**
   - Malick et al. thank him for code.
   - Misener's group used his 90 BoxQP instances.
   - Montanher et al. used the Burer–Anstreicher TTRS instances.
   - Bonami et al. cite the SDPLR user guide.
   - GitHub hosts `BoxQP_instances` (2019), `QuadProgBB`, `soctrust` and `sdplr`.

   [practice, P/S]

---

## 9. Rival schools and where his methods sit (with links to other team members)

| Rival school / method | Representative critic or benchmark here | Verdict relative to Burer's method | Team link |
|---|---|---|---|
| Spatial branch-and-bound with factorable/polyhedral relaxations (BARON, ANTIGONE/GloMIQO, Couenne) | Bao–Sahinidis–Tawarmalani 2011; Misener–Smadbeck–Floudas 2015; Montanher et al. 2018 | DNN equals Shor + partial RLT at about 1000x the time. GloMIQO 2 is "comparable" to his BoxQP solvers. SDP and B&B have "orthogonal difficulties" | Sahinidis, Misener |
| MILP/LP-based global QP (CPLEX, bgl, quadprogIP) | Bonami–Günlük–Linderoth 2018; Xia–Vera–Zuluaga 2020 | Competitive or better on small/sparse BoxQP and standard QPs. QuadProgBB is better on large dense BoxQP | — |
| Successor SDP-based B&B and commercial nonconvex QP | Locatelli–Piccialli–Sudoso 2024/25; Lu et al. 2025 | Overtakes QuadProgBB; "former state-of-the-art" | — |
| Alternative copositive formulations and approximation hierarchies | Bomze et al. 2017/2019; Ito et al. 2018; Dür 2010 (S) | Same CP value, different relaxations/duals/conditioning. Practical value "mainly theoretical" | — |
| Moment–SOS (Lasserre) hierarchy | Kılınç-Karzan–Sun 2024/25 | His 2023 lifted relaxation is "a particular case" of it | (Lasserre is not represented in this team) |
| First-order / regularization / Riemannian SDP solvers | Malick et al. 2009; Boumal 2015 (S); Wang–Chang–Kolter 2017; Brosch et al. 2026 | Faster and/or more accurate than SDPLR on their test classes. SDPLR is "moderately accurate" | — |
| Nonconvex-landscape theory (benign nonconvexity) | Boumal et al.; Waldspurger–Waters; O'Carroll et al.; Cifuentes–Moitra | Explains when BM works and proves where it can fail | — |
| Metaheuristics for Max-Cut/QUBO | Dunning et al. 2018; Benlic–Hao 2013; Zhu–Lin–Ali 2013 (S) | Best single heuristic in one large study; beaten on G-set in others | — |
| Cutting planes / convexification for QCQP | Dey–Kazachkov–Lodi–Muñoz 2022 (S2 snippet: "Historically, the main limitation of using the SDP relaxation (SDP) has been its lack of scalability, but significant progress has been made on this front"); Dey–Kocuk 2025 | Scalability limitation framed as historical. The CP representation is "not tractable in general" | Dey |

---

## 10. Implications for the research-craft skill (all [inferred])

- **Result judgement (layer 5)**: he trusts computation to guide conjectures (TRS 2013, balls 2023, submodular 2025). That habit produced both his confirmed conjectures and his one retracted theorem. The 2026 move to exact rational verification of counterexamples looks like a lesson drawn from that record. No statement of his says so.
- **Taste (layer 1)**: he values "packaging" a hard problem into a convex object, even when the object is intractable. His critics' main charge is exactly that this is "mainly of theoretical interest". The skill should present this as a contested position, not as settled.
- **Blind spot to flag for users**: accuracy and convergence guarantees for first-order/low-rank methods, and long-term maintenance of solver code. Rival schools beat or overtook him on both counts.
- **Limit of applicability**: KKT-branching and CP/DNN bounds pay off on dense, small-to-medium QPs. On sparse or large instances, MILP-based and spatial-B&B methods are competitive or better (Bonami et al. 2018; Locatelli et al. 2024/25).

---

## Contradictions (kept, not reconciled)

1. **SDPLR quality**:
   - Burer & Monteiro (2003) predicted "routine" large Max-Cut SDPs.
   - Malick et al. (2009) found SDPLR "clearly outperformed" on random SDPs.
   - Wang–Chang–Kolter (2017) report 43.62x–114.83x speedups over SDPLR.
   - Brosch–Schwiddessen–Wiegele (2026) call moderate accuracy "a known limitation", yet also report that SDPLR "converges quickly … to a moderate-precision solution" where their own method stalls. Wiegele co-authored both the 2009 and the 2026 papers.

   Instance classes, accuracy targets and hardware differ across these studies.
2. **QuadProgBB's standing**:
   - "dominates the other solvers" on large dense BoxQP (Bonami et al. 2018).
   - "outperformed" by quadprogIP "by orders of magnitude" on standard QPs, but better than quadprogIP on large box QPs (Xia et al. 2020).
   - "always" outperformed by fix-and-bound (Locatelli et al. 2024/25).
   - "consistently slower than Gurobi" (Lu et al. 2025).
3. **The 2009 CP reformulation**: "a breakthrough" (Dür & Rendl 2021), "seminal" (Bomze et al. 2017), "an important paper" (Bomze–Jarre 2010) versus "mainly of theoretical interest" (Ito et al. 2018) and "not tractable in general" (Dey–Kocuk 2025).
4. **BM convergence**:
   - BM 2005 proves "optimal convergence of a slight variant".
   - Critics say the assumptions "are not guaranteed to hold or verify a priori" (Ding–Lu–Yang 2025) and "no guarantees currently exist" (Castañeda et al. 2016).
   - Burer himself, in 2003 and 2023, calls the base "not strong" and the result "partial".
5. **Burer–Ye in public vs in private**: the CMU authors publicly called the paper "appealing" and "intriguing" and built on it, while the error they found reached print only through Burer and Ye's own correction.
6. **The rank-two heuristic**: the best single heuristic in Dunning et al.'s 2,635-instance study, yet statistically outperformed by BLS on the G-set (Benlic–Hao 2013) and "often" outperformed by DDC (Zhu–Lin–Ali 2013, S).
7. **The 2025 submodular claim**: v1 says "solvable in polynomial time". v3 says only the certificate fails and "tractability itself" remains open. The claim narrowed in v2 before any public credit to the finder appeared in v3.
8. **Retrospective framing**: orally (March 2023) he admits a "partial result" with "strong assumptions", while the June 2023 slides present only positive later theory and none of the published failure results.

---

## Gaps

- **Referee reports, rejected papers, OpenReview**: none public for his journals (Math. Program., SIOPT, MPC, COAP, IJOC). No rejection history found.
- **Dür (2010) survey**: the context of "The algorithm is not adequate for general models derived from Burer's result" (which algorithm) was not read. The green-OA copy at research.rug.nl is behind a Cloudflare challenge (curl and WebFetch both got 403).
- **Locatelli & Schoen**, "(Global) Optimization: Historical notes and recent developments", *EURO J. Comput. Optim.* 9:100012, 2021 (DOI 10.1016/j.ejco.2021.100012): it cites six Burer papers, but ScienceDirect returned 403. Not read.
- **Known only from S2 snippets (full text not read)**: Grippo–Palagi–Piccialli 2011; Palagi et al. 2012; Lieder–Rad–Jarre 2015; Bomze–Peng 2023; Beck–Pan 2017; Misener–Smadbeck–Floudas 2015; Liu–Wang–Liu 2004; Zhu–Lin–Ali 2013; Boumal 2015; Zhang 2025; Dey et al. 2022; Dür & Rendl 2021; Yuan et al. 2017; Belotti et al. 2013. For Lieder et al. I could not identify reference [11].
- **Shaoning Han's own account** of the submodular counterexample: none found. The arXiv API returned empty results for all queries at the time of checking, including a control query, so this search failed rather than came back empty. Also unknown: whether Han's report preceded the v2 narrowing (Apr 2026).
- **Timing of the Kılınç-Karzan/Wang report** to Burer and Ye: unknown. It was between the paper's online date (Feb 2019) and the erratum (dated 18 Feb 2021).
- **Excluded for lack of a checkable identifier**:
  - An SDPA-team report (S2 shows only the series name "Research Reports on Mathematical and Computing Sciences", 2010) saying SDPLR "did not obtain the weak accuracy … even after 1 hour" on sfsdp500.
  - A Monteiro–Ortiz–Svaiter report claiming to "substantially outperform" SDPLR; the published COAP 2014 version's abstract (DOI 10.1007/s10589-013-9590-3) does not mention SDPLR.
- **Martí–Duarte–Laguna 2009** (the source of the CirCut numbers used by Benlic–Hao): not read.
- **Whether his 2012 survey prediction** ("an increasing place for heuristics and approximation algorithms for non-convex MINLPs") came true: not assessed.
- **His personal reactions to critiques** beyond printed texts (interviews, blog posts): none found.
- **The two zbMATH reviews behind the licence block**: Dempe on the 2015 gentle introduction and the 2013 cones paper. Not read.

---

## Sources

P = primary (the item's own text read in this run); S = secondary (snippet, review or metadata only).

### A. Burer's own texts, code and talks
1. S. Burer, R.D.C. Monteiro, "A nonlinear programming algorithm for solving semidefinite programs via low-rank factorization", Math. Program. 95:329–357, 2003. DOI 10.1007/s10107-002-0352-8; author copy sburer.github.io/papers/007-lowrank.pdf (P)
2. S. Burer, R.D.C. Monteiro, "Local minima and convergence in low-rank semidefinite programming", Math. Program. 103:427–444, 2005. DOI 10.1007/s10107-004-0564-1; papers/011-lowrank2.pdf (P)
3. S. Burer, C. Choi, "Computational enhancements in low-rank semidefinite programming", Optim. Methods Softw. 21:493–512, 2006. DOI 10.1080/10556780500286582; papers/013-lowrank3.pdf (P)
4. S. Burer, R.D.C. Monteiro, Y. Zhang, "Rank-two relaxation heuristics for MAX-CUT and other binary quadratic programs", SIAM J. Optim. 12:503–521, 2002. DOI 10.1137/S1052623400382467 (S: metadata only, target of critique)
5. S. Burer, D. Vandenbussche, "A finite branch-and-bound algorithm for nonconvex quadratic programming via semidefinite relaxations", Math. Program. 113:259–282, 2008. DOI 10.1007/s10107-006-0080-6; papers/017-qpbb.pdf (P)
6. S. Burer, D. Vandenbussche, "Globally solving box-constrained nonconvex quadratic programs with semidefinite-based finite branch-and-bound", Comput. Optim. Appl. 43:181–195, 2009. DOI 10.1007/s10589-007-9137-6; papers/022-qpbb2.pdf (P)
7. S. Burer, "On the copositive representation of binary and continuous nonconvex quadratic programs", Math. Program. 120:479–495, 2009. DOI 10.1007/s10107-008-0223-z; papers/021-copos.pdf (P)
8. S. Burer, "Optimizing a polyhedral-semidefinite relaxation of completely positive programs", Math. Program. Comput. 2:1–19, 2010. DOI 10.1007/s12532-010-0010-8; papers/029-optdnn.pdf (P)
9. J. Chen, S. Burer, "Globally solving nonconvex quadratic programming problems via completely positive programming", Math. Program. Comput. 4:33–52, 2012. DOI 10.1007/s12532-011-0033-9; papers/034-quadprogbb.pdf (P)
10. S. Burer, "Copositive Programming", in Handbook on Semidefinite, Conic and Polynomial Optimization, Springer, 2012, pp. 201–218. DOI 10.1007/978-1-4614-0769-0_8; papers/033-cpchap.pdf (P)
11. S. Burer, A.N. Letchford, "Non-convex mixed-integer nonlinear programming: A survey", Surv. Oper. Res. Manag. Sci. 17:97–106, 2012. DOI 10.1016/j.sorms.2012.08.001; papers/040-ncminlp.pdf (P)
12. S. Burer, K.M. Anstreicher, "Second-order-cone constraints for extended trust-region subproblems", SIAM J. Optim. 23:432–451, 2013. DOI 10.1137/110826862; papers/035-soctrust.pdf (P)
13. S. Burer, S. Kim, M. Kojima, "Faster, but weaker, relaxations for quadratically constrained quadratic programs", Comput. Optim. Appl. 59:27–45, 2014. DOI 10.1007/s10589-013-9618-8 (P, abstract page)
14. S. Burer, B. Yang, "The trust region subproblem with non-intersecting linear constraints", Math. Program. 149:253–264, 2015. DOI 10.1007/s10107-014-0749-1 (S: metadata + zbMATH review)
15. B. Yang, S. Burer, "A two-variable approach to the two-trust-region subproblem", SIAM J. Optim. 26:661–680, 2016. DOI 10.1137/130945880; papers/043-ttrs.pdf (P)
16. S. Burer, "A gentle, geometric introduction to copositive optimization", Math. Program. 151:89–116, 2015. DOI 10.1007/s10107-015-0888-z; preprint papers/046-ismp2015.pdf (P)
17. S. Burer, Y. Ye, "Exact semidefinite formulations for a class of (random and non-random) nonconvex quadratic programs", Math. Program. 181:1–17, 2020. DOI 10.1007/s10107-019-01367-2; with erratum, papers/053-rank-bounds.pdf (P)
18. S. Burer, Y. Ye, "Correction to: Exact semidefinite formulations…", Math. Program. 190:845–848, 2021. DOI 10.1007/s10107-021-01684-5; Springer article page (P)
19. S. Burer, "A slightly lifted convex relaxation for nonconvex quadratic programming with ball constraints", Math. Program. 211:157–179, 2025. DOI 10.1007/s10107-024-02076-1; author copy papers/059-balls.pdf (Feb 2023) (P)
20. S. Burer, K. Natarajan, (R. Willemsen), "On the semidefinite representability of continuous quadratic submodular minimization…", arXiv 2504.03996 v1 (4 Apr 2025), v2 (5 Apr 2026), v3 (31 Aug 2026) (P)
21. S. Burer, "Two Decades of Low-Rank Optimization", slides, SIAM OP23, 2 June 2023. github.com/sburer/2023-06_SIOPT, test-of-time.pdf (P)
22. S. Burer, "Two Decades of Low-Rank Optimization", University of Iowa talk, March 2023. YouTube wSauUgRIQDg; auto-caption transcript in sources/talks/ (P, machine transcript)
23. sburer GitHub: READMEs of sdplr, ballconstraints, submodular-tests; repository metadata via the GitHub API (QuadProgBB, sdplr, soctrust, BoxQP_instances). github.com/sburer (P)

### B. Critics and observers whose own texts I read
24. N. Boumal, V. Voroninski, A.S. Bandeira, "The non-convex Burer-Monteiro approach works on smooth semidefinite programs", NeurIPS 2016. arXiv 1606.04970 (P, abstract)
25. N. Boumal, V. Voroninski, A.S. Bandeira, "Deterministic guarantees for Burer-Monteiro factorizations of smooth semidefinite programs", Comm. Pure Appl. Math. 73:581–608, 2020. DOI 10.1002/cpa.21830; arXiv 1804.02008 (P, abstract)
26. I. Waldspurger, A. Waters, "Rank optimality for the Burer-Monteiro factorization", SIAM J. Optim. 30:2577–2602, 2020. DOI 10.1137/19M1255318; arXiv 1812.03046v2 (P)
27. L. O'Carroll, V. Srinivas, A. Vijayaraghavan, "The Burer-Monteiro SDP method can fail even above the Barvinok-Pataki bound", 2022. arXiv 2211.12389v1 (P)
28. D. Cifuentes, A. Moitra, "Polynomial time guarantees for the Burer-Monteiro method", 2019. arXiv 1912.01745 (P, abstract)
29. D. Cifuentes, "On the Burer–Monteiro method for general semidefinite programs", Optim. Lett. 15:2299–2309, 2021. DOI 10.1007/s11590-021-01705-4; arXiv 1904.07147 (P, abstract)
30. S. Bhojanapalli, N. Boumal, P. Jain, P. Netrapalli, "Smoothed analysis for low-rank solutions to semidefinite programs in quadratic penalty form", COLT 2018. arXiv 1803.00186 (P, abstract)
31. L. Ding, H. Lu, J. Yang, "New understandings and computation on augmented Lagrangian methods for low-rank semidefinite programming", 2025. arXiv 2505.15775v1 (P)
32. L. Grippo, L. Palagi, M. Piacentini, V. Piccialli, G. Rinaldi, "SpeeDP: a new algorithm to compute the SDP relaxations of Max-Cut for very large graphs", OO 2010/10/2766; published as "SpeeDP: an algorithm to compute SDP bounds for very large Max-Cut instances", Math. Program. 136:353–373, 2012. DOI 10.1007/s10107-012-0593-0 (P, preprint)
33. J. Malick, J. Povh, F. Rendl, A. Wiegele, "Regularization methods for semidefinite programming", SIAM J. Optim. 20:336–356, 2009. DOI 10.1137/070704575; OO 2007/10/1800 (P, preprint)
34. Z. Lu, Y. Zhang, "An augmented Lagrangian approach for sparse principal component analysis", Math. Program. 135:149–193, 2012. DOI 10.1007/s10107-011-0452-4; arXiv 0907.2079 (P)
35. G. Sagnol, "A class of semidefinite programs with rank-one solutions", Linear Algebra Appl. 435:1446–1463, 2011. DOI 10.1016/j.laa.2011.03.027; arXiv 0909.5577 (P)
36. O. Castañeda, T. Goldstein, C. Studer, "Data detection in large multi-antenna wireless systems via approximate semidefinite relaxation", IEEE TCAS-I 63:2334–2346, 2016. DOI 10.1109/TCSI.2016.2607198; arXiv 1609.01797 (P)
37. H. Yang, L. Liang, K.-C. Toh, L. Carlone, "An inexact projected gradient method with rounding and lifting by nonlinear programming for solving rank-one semidefinite relaxation of polynomial optimization", Math. Program. 201:409–472, 2023. DOI 10.1007/s10107-022-01912-6; arXiv 2105.14033 (P)
38. P.-W. Wang, W.-C. Chang, J.Z. Kolter, "The Mixing method: low-rank coordinate descent for semidefinite programming with diagonal constraints", 2017. arXiv 1706.00476v1 (P)
39. D. Brosch, J. Schwiddessen, A. Wiegele, "The augmented mixing method: computing high-accuracy primal-dual solutions to large-scale SDPs via column updates", Optim. Methods Softw. 41:754–796, 2026. DOI 10.1080/10556788.2026.2683647; arXiv 2507.20386v2 (P)
40. I. Dunning, S. Gupta, J. Silberholz, "What works best when? A systematic evaluation of heuristics for Max-Cut and QUBO", INFORMS J. Comput. 30:608–624, 2018. DOI 10.1287/ijoc.2017.0798; OO 2015/05/4895 (P, preprint)
41. U. Benlic, J.-K. Hao, "Breakout local search for the Max-Cut problem", Eng. Appl. Artif. Intell. 26:1162–1173, 2013. DOI 10.1016/j.engappai.2012.09.001; author PDF info.univ-angers.fr/pub/hao/papers/BenlicHaoMaxCut2012.pdf (P)
42. I.M. Bomze, F. Jarre, "A note on Burer's copositive representation of mixed-binary QPs", Optim. Lett. 4:465–472, 2010. DOI 10.1007/s11590-010-0174-1; OO 2009/08/2368 (P)
43. N. Ito, S. Kim, M. Kojima, A. Takeda, K.-C. Toh, "Equivalences and differences in conic relaxations of combinatorial quadratic optimization problems", J. Global Optim. 72:619–653, 2018. DOI 10.1007/s10898-018-0676-4; OO 2017/07/6134 (P, preprint)
44. I.M. Bomze, J. Cheng, P.J.C. Dickinson, A. Lisser, "A fresh CP look at mixed-binary QPs: new formulations and relaxations", Math. Program. 166:159–184, 2017. DOI 10.1007/s10107-017-1109-8; OO 2016/05/5455 (P, preprint)
45. I.M. Bomze, J. Cheng, P.J.C. Dickinson, A. Lisser, J. Liu, "Notoriously hard (mixed-)binary QPs: empirical evidence on new completely positive approaches", Comput. Manag. Sci. 16:593–619, 2019. DOI 10.1007/s10287-018-0337-6 (P, abstract page)
46. S.S. Dey, B. Kocuk, "Convexification of a separable function over a polyhedral ground set", 2025. arXiv 2510.16595v1 (P)
47. X. Bao, N.V. Sahinidis, M. Tawarmalani, "Semidefinite relaxations for quadratically constrained quadratic programming: A review and comparisons", Math. Program. 129:129–157, 2011. DOI 10.1007/s10107-011-0462-2 (P, abstract page)
48. P. Bonami, O. Günlük, J. Linderoth, "Globally solving nonconvex quadratic programming problems with box constraints via integer programming methods", Math. Program. Comput. 10:333–382, 2018. DOI 10.1007/s12532-018-0133-x; OO 2016/06/5488 (P)
49. W. Xia, J.C. Vera, L.F. Zuluaga, "Globally solving nonconvex quadratic programs via linear integer programming techniques", INFORMS J. Comput. 32:40–56, 2020. DOI 10.1287/ijoc.2018.0883; arXiv 1511.02423v3 (P, abstract)
50. M. Locatelli, V. Piccialli, A.M. Sudoso, "Fix and bound: an efficient approach for solving large-scale quadratic programming problems with box constraints", Math. Program. Comput. 17:231–263, 2025. DOI 10.1007/s12532-024-00270-y; arXiv 2211.08911v2 (P)
51. C. Lu, Y. Fei, G. Kang, G. Qu, Z. Deng, Q. Jin, S.-C. Fang, "Enhancing quadratic programming solvers via quadratic nonconvex reformulation", 2025. arXiv 2508.20897v1 (P)
52. H. Dong, Y. Luo, "Compact disjunctive approximations to nonconvex quadratically constrained programs", 2018. arXiv 1811.08122v1 (P)
53. T. Montanher, A. Neumaier, F. Domes, "A computational study of global optimization solvers on two trust region subproblems", J. Global Optim. 71:915–934, 2018. DOI 10.1007/s10898-018-0649-7 (P, open access)
54. A.L. Wang, F. Kılınç-Karzan, "On the tightness of SDP relaxations of QCQPs", Math. Program. 193:33–73, 2022. DOI 10.1007/s10107-020-01589-9; arXiv 1911.09195 v1 and v3 (P)
55. A.L. Wang, F. Kılınç-Karzan, "Exactness in SDP relaxations of QCQPs: Theory and applications", 2021. arXiv 2107.06885 (P)
56. F. Kılınç-Karzan, S. Sun, "On the strength of Burer's lifted convex relaxation to quadratic programming with ball constraints", OO 2024/07 (preprint 20 Jul 2024); Math. Program. 2025. DOI 10.1007/s10107-025-02278-1 (P, preprint)

### C. Secondary: snippets, reviews, metadata, sibling note
57. L. Grippo, L. Palagi, V. Piccialli, "An unconstrained minimization method for solving low-rank SDP relaxations of the maxcut problem", Math. Program. 126:119–146, 2011. DOI 10.1007/s10107-009-0275-8 (S: snippet + abstract page)
58. L. Palagi, V. Piccialli, F. Rendl, G. Rinaldi, A. Wiegele, "Computational approaches to Max-Cut", Handbook…, 2012, pp. 821–847. DOI 10.1007/978-1-4614-0769-0_28 (S)
59. N. Boumal, "A Riemannian low-rank method for optimization over semidefinite matrices with block-diagonal constraints", 2015. arXiv 1506.00575 (S: snippet; abstract read)
60. R.Y. Zhang, "Improved global guarantees for the nonconvex Burer–Monteiro factorization via rank overparameterization", Math. Program. 213:1009–1038, 2025. DOI 10.1007/s10107-024-02160-6; arXiv 2207.01789 (S: snippet; abstract read)
61. H. Liu, X. Wang, S. Liu, "Feasible direction algorithm for solving the SDP relaxations of quadratic {−1, 1} programming problems", Optim. Methods Softw. 19:125–136, 2004. DOI 10.1080/10556780410001647203 (S)
62. W. Zhu, G. Lin, M.M. Ali, "Max-k-Cut by the discrete dynamic convexized method", INFORMS J. Comput. 25:27–40, 2013. DOI 10.1287/ijoc.1110.0492 (S: snippet; abstract read)
63. R. Martí, A. Duarte, M. Laguna, "Advanced scatter search for the max-cut problem", INFORMS J. Comput. 21:26–38, 2009. DOI 10.1287/ijoc.1080.0275 (S: abstract only; not read)
64. F. Lieder, F.B.A. Rad, F. Jarre, "Unifying semidefinite and set-copositive relaxations of binary problems and randomization techniques", Comput. Optim. Appl. 61:669–688, 2015. DOI 10.1007/s10589-015-9731-y (S)
65. I.M. Bomze, B. Peng, "Conic formulation of QPCCs applied to truly sparse QPs", Comput. Optim. Appl. 84:703–735, 2023. DOI 10.1007/s10589-022-00440-5 (S)
66. L. Bai, J.E. Mitchell, J.-S. Pang, "On conic QPCCs, conic QCQPs and completely positive programs", Math. Program. 159:109–136, 2016. DOI 10.1007/s10107-015-0951-9 (S: snippet; checked, not cited in the findings)
67. M. Dür, "Copositive Programming – a Survey", in Recent Advances in Optimization and its Applications in Engineering, Springer, 2010, pp. 3–20. DOI 10.1007/978-3-642-12598-0_1 (S)
68. M. Dür, F. Rendl, "Conic optimization: A survey with special focus on copositive optimization and binary quadratic problems", EURO J. Comput. Optim. 9:100021, 2021. DOI 10.1016/j.ejco.2021.100021 (S)
69. R. Misener, J.B. Smadbeck, C.A. Floudas, "Dynamically generated cutting planes for mixed-integer quadratically constrained quadratic programs and their incorporation into GloMIQO 2", Optim. Methods Softw. 30:215–249, 2015. DOI 10.1080/10556788.2014.916287 (S)
70. A. Beck, D. Pan, "A branch and bound algorithm for nonconvex quadratic optimization with ball and linear constraints", J. Global Optim. 69:309–342, 2017. DOI 10.1007/s10898-017-0521-1 (S)
71. J. Yuan, M. Wang, W. Ai, T. Shuai, "New results on narrowing the duality gap of the extended Celis–Dennis–Tapia problem", SIAM J. Optim. 27:890–909, 2017. DOI 10.1137/16M1080082 (S)
72. S.S. Dey, A.M. Kazachkov, A. Lodi, G. Muñoz, "Cutting plane generation through sparse principal component analysis", SIAM J. Optim. 32:1319–1343, 2022. DOI 10.1137/21m1399956 (S)
73. P. Belotti, C. Kirches, S. Leyffer, J. Linderoth, J. Luedtke, A. Mahajan, "Mixed-integer nonlinear optimization", Acta Numerica 22:1–131, 2013. DOI 10.1017/S0962492913000032 (S)
74. A. Gupte, S. Ahmed, S.S. Dey, M.S. Cheon, "Relaxations and discretizations for the pooling problem", J. Global Optim. 67:631–669, 2017. DOI 10.1007/s10898-016-0434-4 (S: snippet; DOI checked in Crossref)
75. M. Locatelli, F. Schoen, "(Global) Optimization: Historical notes and recent developments", EURO J. Comput. Optim. 9:100012, 2021. DOI 10.1016/j.ejco.2021.100012 (S: metadata only; not readable)
76. R.D.C. Monteiro, C. Ortiz, B.F. Svaiter, "Implementation of a block-decomposition algorithm for solving large-scale conic semidefinite programming problems", Comput. Optim. Appl. 57:45–69, 2014. DOI 10.1007/s10589-013-9590-3 (S: abstract checked; used only to exclude an unverifiable SDPLR claim)
77. zbMATH Open API, documents of author "Burer, Samuel" (61 documents; 10 with reviews, 8 readable), api.zbmath.org, queried 2026-10-10 (S)
78. Semantic Scholar Graph API, citation contexts of 12 Burer papers (DOIs in A1–A2, A5–A9, A11, A12, A16, A17 and source 4), queried 2026-10-10 (S)
79. Sibling research note, product/minlp-team/samuel-burer/references/research/06-trajectory.md, 2026-10-10 (S, cross-reference only)
80. MQLib repository README, github.com/MQLib/MQLib (S; checked, holds no BUR02 performance statement)

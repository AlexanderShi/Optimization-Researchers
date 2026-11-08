# 05 · Peer critique: blind spots, limits of applicability, judgements shown wrong

> **Researcher**: Dimitris Bertsimas, Boeing Professor of Operations Research, MIT (Sloan School of Management and Operations Research Center). Google Scholar prKmkzMAAAAJ; ORCID 0000-0002-1985-1003; homepage https://www.mit.edu/~dbertsim/. Not Dimitri P. Bertsekas.
> **Dimension**: research agent 05 of 06, peer critique (nuwa research-craft Phase 1).
> **Research date**: 2026-10-28.
> **Sources consulted**: 80, listed under "Sources" (38 primary, 42 secondary). Every paper named below carries a DOI, an arXiv id, or venue + year + full title that I checked in this run with Crossref, OpenAlex, the arXiv API or the publisher's page. Names that occur only inside a critic's sentence are reported as that critic's words, not cited by me.
> **WebSearch calls used**: 4 of 5 (Boston start-time controversy; OPOM critique; reviews of *Introduction to Linear Optimization*; critiques of the MIO speed-up claim).
> **Local corpus**: `references/sources/papers`, `essays`, `software` and `publications` hold only `.gitkeep`; `RESOURCES.md` is the unfilled template. Nothing here is "from user-supplied material". `sources/talks/` holds a 2014 Sloan oral-history transcript saved by sibling agent 04 in this run (not user-supplied); I did not need it for critique. I did not open `private/`. I saved no transcript.
> **Method**:
> 1. Semantic Scholar (S2) Graph API: citation contexts of 19 Bertsimas papers, 15,853 citing records, 8,785 with contexts. Three targets returned nothing usable (the OCT DOI returned 0 citations, *Data-driven robust optimization* 0, *Simulated annealing* 1993 a 404), so the OCT critique set below comes from targeted reading, not from a harvest. Contexts were filtered for critique words (conservative, loose, fail, drawback, limitation, incorrect, suboptimal, outperform, reproduc, proprietary, and so on).
> 2. Each lead was traced to the critic's own text where an open copy existed (arXiv, Project-Euclid-mirrored repositories, OSTI, KoreaScience, AAAI OJS, PMC, author pages). Project Euclid itself served a bot-check page; I did not try to get past it.
> 3. Bertsimas's side was read in his own texts: homepage PDFs (`papers/...`), MIT DSpace open-access copies, arXiv versions.
> 4. Crossref `update-to`/`relation` fields were checked for 9 core DOIs: no registered correction or retraction.
> **Tags**: [stated] = Bertsimas alone said or wrote it · [stated-joint] = a co-authored Bertsimas text · [practice] = what the record shows he and his group did (papers, code, dates, numbers) · [observed] = what others wrote · [inferred] = my reading, which no source states. **P** = I read the item's own text in this run (full text, preprint, or, where marked, its abstract). **S** = known only through an intermediary: an S2 citation-context snippet, a metadata record, or a sibling note.
> **Quoting**: quotations are verbatim and kept short; longer content is paraphrased and marked "(paraphrase)". Page numbers are journal pages when the copy carries them, otherwise PDF pages of the preprint, marked "pdf p.". "(S2 snippet)" means the sentence comes from Semantic Scholar's extraction and I did not read that paper.
> **Domain codes** (team.json "domains"): LO, IO, RO, CP, SD, ML, DA, HS, AP.
> **Sibling notes**: `02-methodology.md` and `06-trajectory.md` appeared during this run. I cross-reference them (S) only where noted and re-verified the one item I reuse (arXiv 1402.5481).

---

## 0. Overview: who criticised what, and whether Bertsimas answered

| # | Target (domain) | Critic(s), year | Critique in one line | Kind | Answered? How |
|---|---|---|---|---|---|
| 1 | Best subset selection via MIO, BKM 2016 (ML, IO) | Hastie, Tibshirani, Tibshirani (HTT), arXiv 2017 / *Stat. Sci.* 2020 | Best subset does not dominate the lasso; it loses at realistic (low) SNR; the relaxed lasso is the overall winner; the MIO solve is costly | benchmark, limit | **Indirectly.** BPV 2020 moves to lower SNR, adds an ℓ2 term and reframes the contest as feature selection (accuracy, false detection). Rejoinder not read (§1.3) |
| 2 | BPV 2020 study design and code (ML) | Sarwar, Sauk, Sahinidis 2020; Chen, Taeb, Bühlmann 2020; George 2020 (S); Mazumder 2020 (S) | Design exaggerates lasso weaknesses; timing compares one k with a full lasso path; regularized L0Learn is better and faster; the CIO code would not run | benchmark, reproducibility | Rejoinder exists (pp. 623–624), **not read** (§1.4) |
| 3 | Best subset at low SNR (ML) | BKM co-author Mazumder, with Radchenko and Dedieu, arXiv 2017 / OR 2023 | Best subset "deteriorates when the SNR is low" | concession by a co-author | n/a: the co-author published the fix himself (§1.5) |
| 4 | The MIO speed-up rhetoric (IO, ML) | none found | 200 → 450 → 800 billion-fold across 2015–2017 versions | claim to watch | n/a (§1.6) |
| 5 | Optimal classification trees (OCT), Bertsimas–Dunn 2017 (ML, IO) | Hu, Rudin, Seltzer 2019; Verwer, Zhang 2019; Günlük et al. 2021; Aghaei, Gómez, Vayanos 2021/2025 | Trees "clearly suboptimal" and not reproducible (code not public); formulation grows with data and has a weak LP relaxation; at depth 4 OCT is close to or below CART | benchmark, formulation strength, reproducibility | **No published reply found.** The paper had already said its results carry no optimality certificates (§2) |
| 6 | Optimal prescriptive trees, Bertsimas–Dunn–Mundru 2019 (DA, ML) | Jo, Aghaei, Gómez, Vayanos 2021 / *Mgmt. Sci.* 2026 | A constructed example in which the method has "additional incentives to choose the worst tree"; no codebase to replicate | counterexample, reproducibility | **No reply found** (§2.6) |
| 7 | From predictive to prescriptive analytics, Bertsimas–Kallus 2020 (DA) | Bertsimas–Van Parys (self) 2017/2021; Sadana et al. survey 2023/2025; decision-focused rivals | Nonparametric weighting overfits, is optimistic in high covariate dimension, ignores the decision signal | self-identified limit, rival school | **Yes, by his own group**: bootstrap-robust variants (§3) |
| 8 | Budgeted uncertainty, *The price of robustness* 2004 (RO) | Iancu–Trichakis 2014; Poss 2013; Büsing–Gersing–Koster 2023 (S); Gregory–Darby-Dowman–Mitra 2011 (S) | RO optima need not be Pareto optimal; the fixed budget over-protects sparse solutions; Γ is set arbitrarily in practice | limit | **Partly, by his own group**: data-driven sets (2018), new guarantees without independence (2021) (§4.1) |
| 9 | Robust discrete optimization 2003 (RO, IO) | Álvarez-Miranda–Ljubić–Toth 2013; Lee–Kwon 2014 | The n+1 nominal subproblems can be cut substantially | refinement | n/a (§4.2) |
| 10 | Robust inventory theory, Bertsimas–Thiele 2006 (RO) | Bienstock–Özbay 2008 (S); Park 2014; Attila et al. 2021 (S) | The LP is a conservative approximation of the true min–max; Park: "incorrect", with a two-period counterexample | judgement shown wrong (claimed) | **No reply found** (§4.3) |
| 11 | Affine policies, Bertsimas–Iancu–Parrilo 2010 (RO) | the citing literature (S); Bertsimas–Goyal 2012 (self) | Optimality holds only in one-dimensional problems; elsewhere affine policies can be far from optimal | limit | **Self-identified**, quantified by his own group (§4.4) |
| 12 | Robust queueing theory, Bandi–Bertsimas–Youssef 2015 (RO, SD) | Whitt–You 2018, 2019 (S), 2021; Goldberg–Li 2017 (S) | Hard to choose the sets and tie them to the real queue; the network analyzer "seems to perform far worse"; bounds do not scale in the Halfin–Whitt regime | benchmark, limit | **No reply found** (§4.5) |
| 13 | Robust simulation-based optimization, Bertsimas–Nohadani–Teo 2010 (HS, RO) | Menickelly–Wild 2020; Zheng et al. 2024 (S); Cakmak et al. 2021 (S) | Its test problem became the field's standard; scope limited to one objective and to implementation errors | limit, uptake | n/a (§4.6) |
| 14 | Boston school start times, 2017–2019 (AP) | Goodman 2019 (essay); parents, city councillors, NAACP (as reported by Goodman) | The plan was abandoned; the process gave families no way to see or contest the trade-offs | implementation failure | **Framed in print** (PNAS 2019) as a delay and as more objectives to add; the student's 2021 thesis says "not implemented" (§5.1) |
| 15 | DELPHI COVID-19 model, 2020 (AP) | Cramer et al. 2022 (CDC Forecast Hub evaluation, DELPHI team among the co-authors) | Mortality forecasts about as accurate as the naive baseline (relative WIS 0.99) | benchmark | n/a; self-reported accuracy uses another metric (§5.2) |
| 16 | Optimal control of execution costs, Bertsimas–Lo 1998 (AP) | Bertsimas–Lo themselves; rival Almgren–Chriss (not read) | Risk-neutral objective, permanent impact only, prices can go negative | self-identified limit | **Self-identified** in the paper (§5.3) |
| 17 | Moment problems, textbooks, SDVRP, OPOM | none found (§6) | — | — | — |

---

## 1. Machine learning under a modern optimization lens (ML): the best-subset debate

### 1.1 The claim under attack [stated-joint, practice, P]
- **Target**: D. Bertsimas, A. King, R. Mazumder, "Best subset selection via a modern optimization lens", *Ann. Statist.* 44(2):813–852, 2016, DOI 10.1214/15-AOS1388 (homepage copy of the published version; arXiv 1507.03133v1, 11 Jul 2015).
- The abstract claims solutions to provable optimality for n in the 1000s and p in the 100s "in minutes", and that the MIO approach beats the lasso and other sparse methods in sparsity with good predictive power (paraphrase).
- **Era and resources [practice, P]**: experiments in MATLAB 2012b with Gurobi 5.5 (published p. 836). HTT add that the authors ran Gurobi through Python/Matlab with multithreading (HTT, pdf p. 10–11). A commercial solver, free for academics, is the enabling tool.

### 1.2 The critique: Hastie, Tibshirani and Tibshirani [observed, P]
- **Source**: T. Hastie, R. Tibshirani, R. J. Tibshirani, "Extended comparisons of best subset selection, forward stepwise selection, and the lasso", arXiv 1707.08692v2 (29 Jul 2017), read in full; published as "Best subset, forward stepwise or lasso? Analysis and recommendations based on extensive comparisons", *Stat. Sci.* 35(4):579–592, 2020, DOI 10.1214/19-STS733 (published version known only from S2 snippets).
- **Tone**: they open by calling it "exciting new work" and build their R package `bestsubset` on the BKM formulation (pdf p. 1–2; GitHub README).
- **Findings**:
  - Neither method dominates: "neither best subset selection nor the lasso uniformly dominate the other" (pdf p. 1). Best subset wins at high SNR, the lasso at low SNR; forward stepwise and best subset perform alike; the relaxed lasso is the overall winner (abstract, paraphrase).
  - **The SNR range was unrealistic**: BKM simulated SNR of about 2–8 (low-dimensional) and 3–10 (high-dimensional) (pdf p. 4). On PVE grounds HTT call SNR 6 (PVE 0.86) "unheard of!" (pdf p. 6), and say a PVE of 0.2 may be typical for noisy observational data (paraphrase).
  - **Compute**: in their experience Gurobi "typically requires 1 hour or longer" for n = 500, p = 100 (pdf p. 8). They capped Gurobi at 3 minutes per subset size. BKM had used 15 minutes (p = 100) and 66 minutes (p ≥ 2000) per problem per k (pdf p. 10). They note that 10-fold cross-validation over k = 0..50 would then take 25 hours (pdf p. 8, paraphrase).
  - **Co-author input**: Mazumder, a BKM co-author, told them by personal communication that the solver often finds the solution within 3 minutes but takes much longer to certify it, and that 3 minutes may not suffice in the high-dimensional settings (pdf p. 8, 10, paraphrase).
  - Discussion: best subset "often loses to the lasso except in the high SNR range" (pdf p. 17). They add that a support-recovery target might give different results (paraphrase).
- **Era and resources [observed]**: R interface to Gurobi, single-threaded in their runs (pdf p. 10–11). The full design cost about 31 days of compute per setting at the 3-minute budget (pdf p. 10, paraphrase). The comparison is therefore asymmetric in time budget and threading, a point HTT themselves state.

### 1.3 How Bertsimas answered: BPV 2019/2020 [stated-joint, practice, P]
- **Source**: D. Bertsimas, J. Pauphilet, B. Van Parys, "Sparse regression: scalable algorithms and empirical performance", *Stat. Sci.* 35(4):555–578, 2020, DOI 10.1214/19-STS701; arXiv 1902.06547v2 (29 Feb 2020), read in full.
- **What changed relative to BKM [practice]**:
  - The SNR grid now runs from 6 (PVE 85.7%) down to 0.05 (PVE 4.8%), justified with HTT's PVE formula (pdf p. 10).
  - The estimator gains an ℓ2 (ridge) term, and the headline metrics become feature-selection accuracy and false detection rate rather than prediction error (abstract, paraphrase).
  - A time limit of 60 s (regression) and 180 s (classification) per solve, justified by confidence in the warm start (pdf p. 5, paraphrase).
- **What was conceded and what was not [stated-joint]**:
  - On HTT: "Our experiments suggest that their observations are still valid but less obvious" once best subset is also regularized (pdf p. 23).
  - ℓ1 regularization is recast as "first and foremost, a robustness story" (pdf p. 23). The best approaches are "those combining a convex and a non-convex component" (pdf p. 30).
  - The study recommends a pipeline (paraphrase): lasso/ENet as a screening step, then a costlier non-convex selector "if time permits" (pdf p. 23).
  - No sentence concedes that the BKM simulations used an unrealistic SNR range [inferred from reading the arXiv v2 text].
- **Rejoinder**: D. Bertsimas, J. Pauphilet, B. Van Parys, "Rejoinder: Sparse regression: scalable algorithms and empirical performance", *Stat. Sci.* 35(4):623–624, 2020, DOI 10.1214/20-STS701REJ. **Not read**: Project Euclid served a bot check, and OpenAlex lists no open copy. HTT's rejoinder (DOI 10.1214/20-STS733REJ, pp. 625–626) is likewise **not read**.

### 1.4 The published discussion (Stat. Sci. 35(4), 2020)
- **Sarwar, Sauk and Sahinidis** [observed, P] (N. V. Sahinidis is a MINLP-team member in this repository): "A discussion on practical considerations with sparse regression methodologies", pp. 593–601, DOI 10.1214/20-STS806; arXiv 2011.09362v2.
  - They commend both groups for open code, and HTT for also releasing their simulation scripts (pdf p. 2, paraphrase).
  - Fixing the support size at the true k and growing n "somewhat exaggerates the lasso's relative deficiencies" (pdf p. 5).
  - BPV's timing figure appears to compare the time for a single cardinality-constrained solution with a full glmnet path (pdf p. 6, paraphrase). With the 60 s limit, a 100 × 10 grid of (k, γ) would take more than 8 hours (footnote, pdf p. 6–7, paraphrase).
  - Their re-run: the relaxed lasso is competitive with BPV's methods in BPV's own setting. Regularized L0Learn "exceed[s] the performance of cardinality-constrained algorithms" while being faster (pdf p. 7). For CIO/SS they reused BPV's published numbers rather than re-running the code (pdf p. 5, paraphrase).
  - Practical verdict: in the general case "we would not turn to the cardinality-constrained estimators CIO/SS" (pdf p. 9).
- **Chen, Taeb and Bühlmann** [observed, P]: "A look at robustness and stability of ℓ1- versus ℓ0-regularization", pp. 614–622, DOI 10.1214/20-STS809 (ETH Research Collection copy, journal pagination).
  - MIO for ℓ0 is "not yet as fast as Lasso, especially for low-SNR regimes and large problem sizes" (p. 615). BPV's relaxation SS solves n = 10,000, p = 100,000 in under 20 s (pp. 615–616, paraphrase).
  - They credit BPV's ℓ2 term as a response to HTT's instability concerns, and both papers for following "no cherry picking" guidelines (p. 616, paraphrase). If ℓ0 + ℓ2 is read as a cousin of the relaxed lasso, its good showing is "no longer surprising" (p. 616).
  - **Reproducibility**: they left CIO out because "we had a hard time executing the CIO code by BPvP", owing to Julia version conflicts; they ask the authors to update the package (p. 617).
- **George** [observed, S]: "Modern variable selection in action: comment on the papers by HTT and BPV", pp. 609–613, DOI 10.1214/20-STS808. Only the opening paragraph (S2 abstract field) was read: "no single method can dominate across all situations".
- **Mazumder** [observed, S]: "Discussion of 'Best subset, forward stepwise or lasso? …'", pp. 602–608, DOI 10.1214/20-STS807. S2 snippets only. He calls the Bertsimas–Van Parys cutting-plane method impressive but qualifies its 10^5 scale with "(low correlations in X and a generous ridge parameter)" (S2 snippet).

### 1.5 The co-author moves on [observed, P]
- R. Mazumder, P. Radchenko, A. Dedieu, "Subset selection with shrinkage: sparse linear modeling when the SNR is low", arXiv 1708.03288 (v1 10 Aug 2017, two weeks after HTT's v1; v4 read), *Oper. Res.* 71(1):129–147, 2023, DOI 10.1287/opre.2022.2276.
  - Abstract: best subset's predictive performance "deteriorates when the SNR is low" and is beaten by ridge and the lasso (pdf p. 1). The paper credits HTT for the same observation (pdf p. 23, paraphrase).
- H. Hazimeh, R. Mazumder, "Fast best subset selection: coordinate descent and local combinatorial optimization algorithms", *Oper. Res.* 68(5):1517–1537, 2020, DOI 10.1287/opre.2019.1919 (S: metadata). Its L0Learn package is the method Sarwar et al. found faster and better than CIO/SS.
- **Reading [inferred]**: the concession came from the co-author's line of work, not from a Bertsimas-led paper. Bertsimas's own reply kept the cardinality constraint and reframed the target.

### 1.6 The speed-up figure across versions [practice, P]
- BKM arXiv v1 (2015): 580,000× algorithmic (1991–2013) × about 320,000× hardware (1993–2013) gives "approximately 200 billion" (pdf p. 7–8).
- BKM published (2016): 780,000× × about 570,000× (hardware 1994–2015) gives about 450 billion (published p. 819, paraphrase).
- OCT (2017): about 1,400,000× × about 570,000× gives "800 billion" (abstract and manuscript p. 4).
- Hardware is measured by the peak speed of supercomputers (Top500), not by the machines the experiments ran on. The figures are for mixed-integer **linear** problems; the text asserts without a citation that the MIQO factors "are similar" (BKM v1 pdf p. 8; published p. 819, paraphrase).
- **No critic found** (one WebSearch, plus the S2 contexts of BKM). Whether anyone has challenged the multiplication of solver and hardware factors is a Gap.

### 1.7 Wider reception, secondary [observed, S]
- S. Athey, G. W. Imbens, *Annu. Rev. Econ.* 11:685–725, 2019, DOI 10.1146/annurev-economics-080217-053433 (S2 snippet): BKM "reopened a new, still unresolved, debate". They note indications that the lasso may do better at the low SNR common in social science (paraphrase).
- A. Kenney, F. Chiaromonte, G. Felici, "MIP-BOOST", *J. Comput. Graph. Statist.* 30(3):566–577, 2021, DOI 10.1080/10618600.2020.1845184 (S2 snippet): solvers find good points early but the time to certify is long "due to a weak lower bound that is slow to improve".

---

## 2. Optimal trees (ML, IO; DA for prescriptive trees)

### 2.1 What the OCT paper itself admits [stated-joint, practice, P]
- **Target**: D. Bertsimas, J. Dunn, "Optimal classification trees", *Mach. Learn.* 106(7):1039–1082, 2017, DOI 10.1007/s10994-017-5633-9 (MIT DSpace author manuscript).
- **No certificates**: because of the time limits, "most of our results for OCT and OCT-H do not carry explicit certificates of optimality" (manuscript p. 26).
- **Gains are small at depth**: CART unconstrained in depth averages 80.7% versus 80.4% for OCT at depth 4. The authors suggest a longer time limit might close the gap (manuscript p. 26, paraphrase). Smaller gains at depths 3–4 are attributed to harder MIO problems (paraphrase).
- **An earlier failure, admitted**: CRIO (Bertsimas–Shioda, *Oper. Res.* 55(2):252–271, 2007, DOI 10.1287/opre.1060.0360) could not reach provable optimality on moderate problems, and "the practical improvement over CART was not significant" (manuscript p. 5–6). Günlük et al. note that this verdict came from "the overlapping author" (pdf p. 5).
- **Era and resources [practice]**: AWS EC2 c4.xlarge (4 vCPU, 7.5 GB) instances. Time limits were 30 min, raised to 2 h for larger data sets; OCT-H used 5–15 min. CART was used as the warm start (manuscript pp. 13–14, 25–26, paraphrase).

### 2.2 Hu, Rudin and Seltzer (NeurIPS 2019) [observed, P]
- X. Hu, C. Rudin, M. Seltzer, "Optimal sparse decision trees", 33rd NeurIPS 2019; arXiv 1904.12847v6.
- "Example figures from the OCT paper [5] show decision trees that are clearly suboptimal." Because the code was not public, the work is "not easily reproducible" (pdf p. 2).
- They read OCT's own figures as showing that CART "often dominates their performance" (pdf p. 7); they could not include OCT as a baseline (paraphrase).
- **Rival school**: Rudin's group solves a sparsity-penalized problem by specialized branch-and-bound, not by a general MIO solver.

### 2.3 Verwer and Zhang (AAAI 2019) [observed, P]
- S. Verwer, Y. Zhang, "Learning optimal classification trees using a binary linear program formulation", *Proc. AAAI* 33:1625–1632, 2019, DOI 10.1609/aaai.v33i01.33011624.
- OCT's number of variables grows as O(R·2^K) with the number of data rows R (p. 1626, paraphrase).
- Reproducibility: "it is not clear how the authors of (Bertsimas and Dunn 2017) pre-processed the datasets" with missing values (p. 1630).
- At depth 4, "OCT's performance was very close or worse than their CART results"; BinOCT ran 10 minutes against OCT's 2 hours (p. 1631).
- **Partial vindication**: plain accuracy maximization made BinOCT overfit at depth 4. They credit CART and OCT's complexity penalty for trading accuracy against complexity (p. 1631, paraphrase).

### 2.4 Günlük, Kalagnanam, Li, Menickelly, Scheinberg (JGO 2021) [observed, P]
- "Optimal decision trees for categorical data via integer programming", *J. Global Optim.* 81:233–260, 2021, DOI 10.1007/s10898-021-01009-y; arXiv 1612.03225v3. (K. Scheinberg is a DFO-team member in this repository.)
- OCT's regularization of tree size "does not simplify the underlying optimization problem". It needs costly tuning, with an effect on topology that cannot be known in advance, and OCT's experiments often fix the depth anyway (pdf p. 4, paraphrase).
- OCT treats categorical features as many binaries and does not exploit their structure (pdf p. 4, paraphrase).

### 2.5 Aghaei, Gómez and Vayanos (arXiv 2021; Oper. Res. 2025) [observed, P]
- "Strong optimal classification trees", *Oper. Res.* 73(4):2223–2241, 2025, DOI 10.1287/opre.2021.0034; arXiv 2103.15965v3.
- Existing MIO tree methods "rely on weak formulations, resulting in slow convergence and large optimality gaps" (pdf p. 1). Their flow formulation avoids big-M constraints, and Theorem 1 proves a stronger LP relaxation than OCT's or BinOCT's (pdf p. 11).
- "As the code used for OCT is not publicly available", they re-implemented OCT for binary data. The local-search heuristic (LST) of Bertsimas–Dunn 2019 was available "for academic use" and was included (pdf p. 34).
- Results: 29× faster on balanced trees (240 instances) and 51× on imbalanced trees (2,400 instances) than the OCT formulation under a 60-minute limit (pdf p. 36, paraphrase).

### 2.6 Prescriptive trees: Jo, Aghaei, Gómez, Vayanos [observed, P]
- **Target**: D. Bertsimas, J. Dunn, N. Mundru, "Optimal prescriptive trees", *INFORMS J. Optim.* 1(2):164–183, 2019, DOI 10.1287/ijoo.2018.0005 (S: not read; described through the critics).
- **Critic**: N. Jo, S. Aghaei, A. Gómez, P. Vayanos, "Learning optimal prescriptive trees from observational data", arXiv 2108.13628v2; *Mgmt. Sci.* 2026, DOI 10.1287/mnsc.2021.02813.
  - The method is trained by coordinate descent with multiple starts rather than by MIO (pdf p. 8, paraphrase).
  - Its variance penalty helps only when the randomization assumption at the leaves holds. Otherwise "B-PT does not directly address the issues discussed in Example 1" (pdf p. 13).
  - In a modified example the method has "additional incentives to choose the worst tree", which splits on an irrelevant feature (pdf p. 13).
  - Replication: "there is no existing codebase allowing us to replicate this algorithm", so they implemented the objective inside Kallus's MIO (pdf p. 40).
- A later paper by another group, J. G. M. van der Linden et al., arXiv 2305.19706 (S2 snippet), reports Jo et al.'s result as showing "the limitations" of both earlier prescriptive-tree methods.

### 2.7 Proprietary software, secondary [observed, S]
- H. Wu et al., "Interpretable personalized experimentation", *KDD* 2022, DOI 10.1145/3534678.3539175 (S2 snippet): methods that approximate optimal trees by coordinate ascent "should be faster but their software is proprietary".
- Sibling note 06 records that Bertsimas co-founded Interpretable AI in 2018 (S, via 06; not re-verified here).

### 2.8 Whether he answered
- **No published reply found** to §2.2–2.7: no erratum, comment or rejoinder.
- **[inferred]** His own sources show the line moving from pure MIO to local search: the LST heuristic (Bertsimas–Dunn 2019 book, as cited by Aghaei et al.) and the OPT coordinate descent (as described by Jo et al.). The formulation-strength critique was taken up by others, not by him.

---

## 3. Data-driven decisions (DA): from predictive to prescriptive analytics

- **Target**: D. Bertsimas, N. Kallus, "From predictive to prescriptive analytics", *Mgmt. Sci.* 66(3):1025–1044, 2020, DOI 10.1287/mnsc.2018.3253 (S: metadata; not read).
- **A self-found error before Bertsimas joined [practice, P]**: arXiv 1402.5481 v1 (22 Feb 2014) was a single-author paper by N. Kallus titled "From predictions to data-driven decisions using machine learning". v2 (26 Jun 2014) is withdrawn with the comment "Withdrawn due to crucial error in Theorem 2.2". v3 (9 Feb 2015) is the joint Bertsimas–Kallus paper. (Also recorded in sibling note 06; re-verified on arXiv.)
- **Self-identified limit [stated-joint, P]**: D. Bertsimas, B. Van Parys, "Bootstrap robust prescriptive analytics", *Math. Program.* 195(1–2):39–78, 2022 (online 25 Jun 2021), DOI 10.1007/s10107-021-01679-2; arXiv 1711.09974v2.
  - Estimate-then-optimize methods, Bertsimas–Kallus included, "come without such an immediate remedy when they do overfit" (pdf p. 4).
  - Nearest-neighbour and Nadaraya–Watson estimates have high variance in high covariate dimension, and optimizing over them can yield overly optimistic prescriptors with very poor out-of-sample results (pdf p. 4, paraphrase). The paper's remedy is a bootstrap-robust counterpart.
- **Survey verdict [observed, P]**: U. Sadana et al., "A survey of contextual optimization methods for decision-making under uncertainty", *EJOR* 320(2), 2025, DOI 10.1016/j.ejor.2024.03.020; arXiv 2306.10374v2.
  - Nonparametric weighting is consistent, but produces "overly optimistic policies when the size of the covariate vector is large", citing Bertsimas–Van Parys for the point (pdf p. 18).
  - The Bertsimas–Kallus paper itself flagged the difficulty of ERM with constraints (pdf p. 34, paraphrase).
- **Decision-focused rivals [observed]**: A. Elmachtoub, P. Grigas, "Smart 'predict, then optimize'", *Mgmt. Sci.* 68(1):9–26, 2022, DOI 10.1287/mnsc.2020.3922 (S: metadata). Z. Xie, A. Abdin, Y. Fang, arXiv 2506.19698 (S2 snippet): weighted SAA "ignore[s] decision-making signals and may perform poorly with limited samples".
- **Positive benchmark use [observed, P]**: R. Kannan, G. Bayraksan, J. Luedtke, arXiv 2207.13554v1, use kNN weighted SAA as the baseline. They call it "one of the better performing reweighted SAA approaches" (pdf p. 18).

---

## 4. Robust and adaptive optimization (RO; HS for simulation-based RO)

### 4.1 Budgeted uncertainty and "the price of robustness"
- **Target**: D. Bertsimas, M. Sim, "The price of robustness", *Oper. Res.* 52(1):35–53, 2004, DOI 10.1287/opre.1030.0065 (homepage copy of the journal version).
- **What the paper assumes and how it positions itself [stated-joint, P]**:
  - The probability bounds assume perturbations that are independent and symmetrically distributed (Theorem 2, p. 39, paraphrase).
  - It argues against the ellipsoidal rival school (Ben-Tal–Nemirovski; El Ghaoui–Lebret): those sets lead to "nonlinear, although convex, models" (p. 36).
- **Critiques [observed]**:
  - D. A. Iancu, N. Trichakis, "Pareto efficiency in robust optimization", *Mgmt. Sci.* 60(1):130–147, 2014, DOI 10.1287/mnsc.2013.1753 (P, abstract). The classical RO paradigm "need not produce solutions that possess the associated property of Pareto optimality". Both authors are Bertsimas co-authors (affine policies 2010; price of fairness 2011), so the critique comes from inside his circle.
  - M. Poss, "Robust combinatorial optimization with variable budgeted uncertainty", *4OR* 11:75–92, 2013, DOI 10.1007/s10288-012-0217-9 (P, abstract). A budget that depends on the solution keeps the same probabilistic guarantee while being "less conservative for vectors with few non-zero components". On robust knapsack it cuts the price of robustness by 18% on average (paraphrase).
  - C. Büsing, T. Gersing, A. Koster, *Math. Program. Comput.* 15:269–326, 2023, DOI 10.1007/s12532-022-00232-2 (S2 snippet): in the literature Γ is "chosen from a predefined set of arbitrarily fixed values".
  - C. Gregory, K. Darby-Dowman, G. Mitra, "Robust optimization and portfolio selection: the cost of robustness", *EJOR* 212(2):417–428, 2011, DOI 10.1016/j.ejor.2011.02.015 (S2 snippet): the correlated model of Bertsimas–Sim "has several potential disadvantages". Which disadvantages: **not read**.
- **How he answered [stated-joint, P]**: in later papers of his own group, not in replies.
  - D. Bertsimas, V. Gupta, N. Kallus, "Data-driven robust optimization", *Math. Program.* 167(2):235–292, 2018, DOI 10.1007/s10107-017-1125-8. With poorly chosen sets, robust models "may be overly-conservative or computationally intractable" (p. 236). Earlier set designs assumed structure such as independent components (p. 236, paraphrase). Sets are now built from hypothesis tests on data.
  - D. Bertsimas, D. den Hertog, J. Pauphilet, "Probabilistic guarantees in robust optimization", *SIAM J. Optim.* 31(4):2893–2920, 2021, DOI 10.1137/21m1390967 (P, abstract only). Guarantees now need only light-tailed noise, "not necessarily independent", plus tighter a-posteriori bounds that depend on the solution.

### 4.2 Robust discrete optimization: the algorithm improved by others [observed, P (abstracts)]
- **Target**: D. Bertsimas, M. Sim, "Robust discrete optimization and network flows", *Math. Program.* 98:49–71, 2003, DOI 10.1007/s10107-003-0396-4 (S: metadata).
- E. Álvarez-Miranda, I. Ljubić, P. Toth, *4OR* 11:349–360, 2013, DOI 10.1007/s10288-013-0231-6: "We improve the well-known result presented in Bertsimas and Sim".
- T. Lee, C. Kwon, *4OR* 12:373–378, 2014, DOI 10.1007/s10288-014-0270-7: the number of nominal problems "can be reduced significantly".
- These are refinements, not refutations: the 2003 result stands with a smaller constant [inferred].

### 4.3 Robust inventory theory: a formulation called incorrect [observed]
- **Target**: D. Bertsimas, A. Thiele, "A robust optimization approach to inventory theory", *Oper. Res.* 54(1):150–168, 2006, DOI 10.1287/opre.1050.0238 (homepage copy).
  - The paper presents its LP as yielding the "Optimal Robust Policy" (Theorem 3.2).
  - It notes that the worst-case demands for the holding and shortage constraints of a period are opposite, so no single demand vector realizes both (p. 153, paraphrase). Each constraint is protected separately [inferred].
- **D. Bienstock, N. Özbay**, "Computing robust basestock levels", *Discrete Optim.* 5(2):389–414, 2008, DOI 10.1016/j.disopt.2006.12.002 (S2 snippets; full text 403).
  - They compute the true worst case of B&T's order vectors and report the "% increase in cost incurred by solution in [BT05]" (table caption).
  - They describe B&T's approach as conservative, because the demand that binds in one period may differ from another period's. They also note that B&T show empirically that it is an effective approximation for stationary costs.
- **K. Park**, "An alternative approach to the robust inventory control problem", *Mgmt. Sci. Financ. Eng.* 20(2):1–5, 2014, DOI 10.7737/MSFE.2014.20.2.001 (P, KoreaScience PDF).
  - Abstract: B&T's "formulation is shown to be incorrect, which invalidates all of the results given there" (p. 1).
  - Following Bienstock–Özbay, the formulation is "only an approximation of the true robust inventory control problem" (p. 2). A two-period example shows that the LP implicitly protects against a larger box set than the stated set (p. 2, paraphrase).
  - Park then shows that B&T's model and properties are exact for a different uncertainty set built on cumulative demands (paraphrase).
- O. N. Attila, A. Agra, K. Akartunalı, A. Arulselvan, *EJOR* 288(2):496–510, 2021, DOI 10.1016/j.ejor.2020.06.016 (S2 snippet): the static B&T approach is "known to produce very conservative solutions for some instances".
- **Answered?** No erratum, comment or reply found from Bertsimas or Thiele (Crossref shows no update relation).
- **Era [inferred]**: 2006, single-period worst cases taken per constraint. This was the standard tractable device of early budgeted RO, before adjustable and exact min–max methods became routine.

### 4.4 Affine policies: optimality is narrow, and his group said so [practice, stated-joint]
- **Target**: D. Bertsimas, D. A. Iancu, P. A. Parrilo, "Optimality of affine policies in multistage robust optimization", *Math. Oper. Res.* 35(2):363–394, 2010, DOI 10.1287/moor.1100.0444 (S: metadata).
- **How the literature reads it [observed, S2 snippets]**: dozens of citing papers restate its scope as one-dimensional problems. H. Mamani, S. Nassiri, M. R. Wagner (*Mgmt. Sci.* 63(5):1625–1643, 2017, DOI 10.1287/mnsc.2015.2391) note that the paper itself gives examples where coupling constraints make affine policies suboptimal.
- **Self-quantified limit [stated-joint, P]**: D. Bertsimas, V. Goyal, "On the power and limitations of affine policies in two-stage adaptive optimization", *Math. Program.* 134(2):491–531, 2012, DOI 10.1007/s10107-011-0444-4 (homepage copy).
  - The worst-case cost of the best affine policy can be Ω(m^{1/2−δ}) times the fully adaptable optimum.
  - It is O(√m) when the first-stage constraint matrix is non-negative (abstract, paraphrase).
- D. Bertsimas, A. Georghiou, *Oper. Res.* 63(3):610–627, 2015, DOI 10.1287/opre.2015.1365 (S2 snippet): decision rules "generically sacrifice a significant amount of" optimality.

### 4.5 Robust queueing: Whitt and You [observed]
- **Target**: C. Bandi, D. Bertsimas, N. Youssef, "Robust queueing theory", *Oper. Res.* 63(3):676–700, 2015, DOI 10.1287/opre.2015.1367 (S: metadata).
- W. Whitt, W. You, "Using robust queueing to expose the impact of dependence in single-server queues", *Oper. Res.* 66(1):184–199, 2018, DOI 10.1287/opre.2017.1649 (P, abstract). They extend the approach to a functional formulation that is exact for the M/GI/1 mean and asymptotically correct in heavy and light traffic, properties the abstract presents as new (paraphrase).
- W. Whitt, W. You, *Oper. Res. Lett.* 47(2):99–104, 2019, DOI 10.1016/j.orl.2019.01.001 (S2 snippet): the first robust queueing network analyzer "seems to perform far worse", though its tuning parameters can help.
- W. Whitt, W. You, "A robust queueing network analyzer based on indices of dispersion", *Nav. Res. Logist.* 69(1):36–56, 2022 (online 2021), DOI 10.1002/nav.22010; arXiv 2003.11174v1 (P). The RQ idea is "simple and good", but choosing proper sets and connecting them to the real queue remain challenges (pdf p. 4).
- D. A. Goldberg, Y. Li, arXiv 1707.07775 (S2 snippet): the robust-optimization bounds for heavy-tailed multi-server queues "do not scale appropriately in the Halfin-Whitt regime".
- **Answered?** No reply found. Sibling note 06 records that this "tractable stochastic analysis via RO" programme faded after about 2016 (S, via 06).

### 4.6 Robust simulation-based optimization (HS) [observed]
- **Target**: D. Bertsimas, O. Nohadani, K. M. Teo, "Robust optimization for unconstrained simulation-based problems", *Oper. Res.* 58(1):161–178, 2010, DOI 10.1287/opre.1090.0715 (S: metadata).
- M. Menickelly, S. M. Wild, "Derivative-free robust optimization by outer approximations", *Math. Program.* 179:157–193, 2020, DOI 10.1007/s10107-018-1326-9 (P, OSTI copy).
  - Their test problem is "now-standard", first appearing in Bertsimas–Nohadani–Teo (pdf p. 20).
  - They cite Bertsimas-group RO algorithms among those "known to suffer from undesirable computational requirements" (pdf p. 2).
  - Their contribution is a Clarke-stationarity guarantee for a derivative-free method (abstract, paraphrase).
- S2 snippets on scope:
  - L. Zheng, J. Bao, Z. Tan, *Ann. Oper. Res.* 346:1897–1927, 2024, DOI 10.1007/s10479-024-05963-0: the method was "only designed to address single-objective optimization problems".
  - S. Cakmak, D. Wu, E. Zhou, *IISE Trans.* 2021, DOI 10.1080/24725854.2020.1869352: it "does not work when one is only concerned about the parameter uncertainty".
  - S. Leyffer et al., "A survey of nonlinear robust optimization", *INFOR* 58(2):342–373, 2020, DOI 10.1080/03155986.2020.1730676, cites the algorithm for implementation errors. S. Leyffer is a MINLP-team member.

---

## 5. Applications as testbeds (AP)

### 5.1 Boston school start times (2017–2019): the plan that was not adopted
- **His side [stated-joint, P]**: D. Bertsimas, A. Delarue, S. Martin, "Optimizing schools' start time and bus routes", *PNAS* 116(13):5943–5948, 2019, DOI 10.1073/pnas.1811462116 (DSpace copy).
  - The Boston School Committee approved the policy unanimously in Dec 2017 (p. 5947, paraphrase).
  - After protests by some families, "BPS delayed the plan's implementation" to adjust weights and constraints. The families' concerns "can be modeled as objectives" within the framework (p. 5947).
  - The closing sentence contrasts algorithmic selection with "the political whims of special interest groups" (p. 5947).
- **The student's later account [observed, P]**: A. Delarue, *Optimizing School Operations*, MIT PhD thesis 2021 (supervisor Bertsimas), DSpace 1721.1/139320.
  - 85% of schools' times would have changed, by a median of one hour. The change was "too dramatic for the district to absorb", and "the plan was not implemented" (pdf p. 24).
  - The thesis reprints the PNAS chapter with its "delayed" wording unchanged (pdf p. 41).
- **The critic [observed, P]**: E. P. Goodman, "Smart algorithmic change requires a collaborative political process", *The Regulatory Review* (Penn Program on Regulation), 12 Feb 2019, https://www.theregreview.org/2019/02/12/goodman-smart-algorithmic-change-requires-collaborative-political-process/.
  - "Politics killed the algorithm." She judges the MIT team "not prepared for the backlash". The consultations had not shown families how start times would change, nor let them try the model (paraphrase).
  - Reported reactions: a petition of over 8,000 signatures, and signs reading "Families over algorithms". Five city councillors asked for a delay. The NAACP and the Lawyers' Committee for Civil Rights and Economic Justice also opposed the plan, on the ground that low-income families could adjust least (paraphrase).
  - Outcome: Boston "quickly abandoned" the start-time change. It kept the algorithmic bus routes, saving an estimated $3–5 million a year, and gave up up to $15 million (paraphrase).
  - Her verdict: the public blamed the algorithm for failures of political process. She proposes explanatory and due-process tools, such as letting citizens query the model and see the trade-offs (paraphrase).
- **Not read**: D. Bertsimas, A. Delarue, W. Eger, J. Hanlon, S. Martin, "Bus routing optimization helps Boston Public Schools design better policies", *INFORMS J. Appl. Anal.* 50(1):37–49, 2020, DOI 10.1287/inte.2019.1015 (closed; abstract only, which covers routing). Boston Globe coverage, cited by Goodman, is paywalled.
- **Era and resources [practice]**: Julia/JuMP and Google Maps travel times (PNAS acknowledgements, paraphrase). Goodman reports about 30 minutes per computation; this is a single district contest with a PhD-student team.

### 5.2 DELPHI COVID-19 forecasts (2020–2021) [observed, P]
- **His side [stated-joint]**: M. L. Li, H. Tazi Bouardi, O. Skali Lami, T. A. Trikalinos, N. K. Trichakis, D. Bertsimas, "Forecasting COVID-19 and analyzing the effect of government interventions", *Oper. Res.* 71(1):184–201, 2023, DOI 10.1287/opre.2022.2306; medRxiv DOI 10.1101/2020.06.23.20138693 (P, abstracts only).
  - The abstract OpenAlex stores reports 6% and 11% two-week out-of-sample median absolute percentage error for cases and deaths over 167 areas (paraphrase). It differs from the publisher's abstract; whether it is the preprint abstract was not checked.
  - The publisher's abstract claims that lockdowns cut transmission by nearly 80% and that earlier action could have saved more than 75% of the lives lost in many countries (paraphrase).
- **Independent evaluation**: E. Y. Cramer et al. (US COVID-19 Forecast Hub; 295 co-authors, the DELPHI team among them), "Evaluation of individual and ensemble probabilistic forecasts of COVID-19 mortality in the United States", *PNAS* 119(15), 2022, DOI 10.1073/pnas.2113561119 (PMC9169655).
  - Table 1 (50 states, 1–4-week horizons, late Apr 2020 to late Oct 2021) lists CovidAnalytics-DELPHI with 11,064 forecasts.
  - DELPHI scored 95% PI coverage 0.82, 50% coverage 0.46, relative WIS 0.99 and relative MAE 1.01. The naive baseline is 1.00/1.00 by construction; the ensemble scored 0.61/0.66.
  - The abstract: two-thirds of the models beat the naive baseline (paraphrase). DELPHI sits at the baseline.
- **Reading [inferred]**: the two claims use different targets, metrics and periods (cumulative-death MdAPE over two weeks versus weekly incident deaths scored by WIS over 79 weeks). They cannot be reconciled from these sources.

### 5.3 Optimal execution (Bertsimas–Lo 1998): limits stated up front [stated-joint, P]
- D. Bertsimas, A. W. Lo, "Optimal control of execution costs", *J. Financial Markets* 1(1):1–50, 1998, DOI 10.1016/S1386-4181(97)00012-8 (homepage copy, journal pagination).
  - The naive equal-split strategy is optimal only under "rather restrictive and empirically implausible conditions" (p. 4).
  - With risk aversion, adverse selection or inventory costs, their benchmark "may only be a lower bound" on a fair block price (p. 4).
  - The arithmetic random walk allows negative prices and gives impact only permanent effects, which contradicts empirical studies (pp. 17–18, paraphrase).
- **Rival school**: R. Almgren, N. Chriss, "Optimal execution of portfolio transactions", *J. Risk* 3(2):5–39, 2001, DOI 10.21314/jor.2001.041. **Not read** (author copy 403). Later citers (S2 snippets) describe it as adding a mean–variance frontier to the Bertsimas–Lo set-up.

---

## 6. Domains where no critique was found

- **CP, moment problems** [observed, S2 snippets]: D. Bertsimas, I. Popescu, *SIAM J. Optim.* 15(3):780–804, 2005, DOI 10.1137/S1052623401399903.
  - Citers repeat his own NP-hardness result for multivariate tight bounds as the limit.
  - S. He, J. Zhang, S. Zhang (*Math. Oper. Res.* 35(1):208–232, 2010, DOI 10.1287/moor.1090.0438) say the work "seems to have settled the moment problems for univariate random variables".
  - No critique found in 353 contexts.
- **Fairness**: D. Bertsimas, V. Farias, N. Trichakis, "The price of fairness", *Oper. Res.* 59(1):17–31, 2011, DOI 10.1287/opre.1100.0865. The only limit raised is scope: A. Lodi, S. Sankaranarayanan, G. Wang, *EJOR* 319(2):456–467, 2024, DOI 10.1016/j.ejor.2023.11.030 (S2 snippet), note the bounds "restrict themselves to a single decision period".
- **SD, dynamic vehicle routing**: D. Bertsimas, G. van Ryzin, *Oper. Res.* 39(4):601–615, 1991, DOI 10.1287/opre.39.4.601. Of 251 contexts, 5 matched critique words; none was substantive.
- **LO/IO textbooks**: Y. Ye, review of *Introduction to Linear Optimization*, *IIE Transactions* 30(9):855, 1998, DOI 10.1080/07408179808966531, was **located but not read** (closed). No review of *Optimization over Integers* was found. zbMATH Open returned only summaries for the items it found.
- **Simulated annealing (1993)**: D. Bertsimas, J. Tsitsiklis, *Stat. Sci.* 8(1):10–15, 1993, DOI 10.1214/ss/1177011077. zbMATH summary only, no critique found; S2 returned 404.
- **Healthcare (OPOM liver allocation, 2019)**: one WebSearch found developer and press claims but no published critique. The OPTN committee summary of 11 Oct 2022 that discusses OPOM could not be retrieved (Gap).

---

## 7. Patterns: how Bertsimas meets critique (evidence first, reading second)

1. **He answers with a new paper, not with a reply** [practice, P].
   - After HTT: BPV with a lower SNR grid, an ℓ2 term and a new target (feature selection), in the same journal issue with a two-page rejoinder (§1.3).
   - After set-design criticism: data-driven RO (2018) and new guarantees (2021).
   - After overfitting of weighted SAA: bootstrap-robust prescriptions (2021/22).
   - **[inferred]** He rarely says "we were wrong" in print. The direct concessions in this record come from co-authors' own lines (Mazumder 2017/2023) or sit inside his papers as stated assumptions.
2. **He names limits early and keeps the headline** [stated-joint, P].
   - Bertsimas–Lo (implausible conditions, lower bound, negative prices); price of robustness (independence, symmetry); OCT (no certificates; CRIO's failure); affine policies (Bertsimas–Goyal quantifies the gap).
   - The titles still say "optimal", "best", "price". **[inferred]** The caveat sits in the body, while the claim travels in the title and abstract.
3. **Silence on formulation-strength and reproducibility critiques** [practice].
   - No reply found to Hu et al., Verwer–Zhang, Günlük et al., Aghaei et al., Jo et al., Chen–Taeb–Bühlmann (code), Park (inventory) or Whitt–You. This is absence of evidence, not evidence of indifference.
4. **Scale through solvers, time limits and warm starts** [practice, P].
   - The commercial MIO solver plus a heuristic warm start plus a time limit is the recurring recipe (BKM; OCT; BPV).
   - It is also the common target of critique: optimality not certified, time budgets not comparable, formulations weak once the solver must prove a bound.
5. **Applications: implementation failure framed as missing objectives** [stated-joint vs observed].
   - In Boston the paper treats opposition as weights and constraints still to be added, and contrasts the method with "political whims". The critic treats it as a failure of process and due process.
   - **[inferred]** A rule for the skill: plan for stakeholder interaction and for showing the trade-offs, not only for the objective.
6. **Rhetoric of computational progress** [practice, P]: the speed-up multiplier was restated three times in two years, each time larger (§1.6). No peer critique was found, so this is my observation, not a critique on record.
7. **Criticism from inside the circle** [observed]: Mazumder (BKM co-author), Iancu and Trichakis (co-authors), Delarue (his PhD student) and the DELPHI team (co-authors of the Cramer et al. evaluation) all supply critical or sobering evidence.

---

## 8. Rival schools and where his methods sit (with links to other teams)

- **Statistics, sparse regression**: Hastie–Tibshirani (relaxed lasso, convex-first) and Bühlmann (stability, distributional robustness) put prediction error and stability ahead of exact ℓ0 optimality. Mazumder–Hazimeh offer fast ℓ0 coordinate descent and specialized branch and bound instead of general-purpose MIO. The MINLP team's Sahinidis (with Sarwar and Sauk) favours convenience and regularized ℓ0.
- **Optimal trees**: Rudin's group (specialized branch and bound for sparse trees) and Verwer–Zhang (compact binary LP) compete on speed and reproducibility. Vayanos–Gómez–Aghaei (strong flow formulations, Benders) compete on formulation strength. Günlük–Scheinberg et al. (categorical structure) differ on modelling. Scheinberg is a DFO-team member.
- **Robust optimization**: Ben-Tal–Nemirovski (ellipsoidal sets, conic tractability) is the school his budgeted sets were defined against. Within budgeted RO, Poss, Büsing and Koster refine the uncertainty model. Iancu–Trichakis add Pareto efficiency. Bienstock–Özbay compute exact min–max solutions where he used a per-constraint approximation.
- **Contextual optimization**: decision-focused learning (Elmachtoub–Grigas; Donti et al., as cited) against estimate-then-optimize. DRO with covariates comes from Kannan–Bayraksan–Luedtke and from Delage's group (Sadana et al.).
- **Queueing**: Whitt and You build on robust queueing but rebuild it around indices of dispersion and asymptotic exactness. Goldberg–Li work with explicit stochastic-comparison bounds.
- **Derivative-free robust optimization (DFO team link)**: Menickelly–Wild supply the convergence theory that the heuristic robust local search lacked [inferred: the Bertsimas–Nohadani–Teo convergence claims were not read here].

---

## 9. Implications for the research-craft skill (all [inferred])

- When the skill proposes an MIO reformulation of a statistical or ML problem, it should stress-test in the regime critics will choose: low SNR, the metric the rival school cares about, matched time budgets and threads, and public code that installs.
- It should state what is and is not certified (gap at the time limit), and avoid "optimal" in a title when results are not certified, or say so in the abstract.
- It should check formulation strength (LP relaxation, big-M) before relying on solver speed-ups. Two critiques (OCT; inventory) are about formulations, not about solvers.
- For deployed analytics, it should plan for stakeholders who see only the outcome, and put trade-off visualizations and recourse into the deliverable (Boston).
- It should report forecasts against the field's standard benchmark and metric (Forecast Hub WIS), not only self-chosen metrics (DELPHI).

---

## Contradictions (kept, not reconciled)

1. **Who wins, best subset or lasso?**
   - BKM: MIO beats the lasso in sparsity with good prediction.
   - HTT: neither dominates; the lasso wins at low SNR; the relaxed lasso is overall best.
   - BPV: the exact sparse formulation is the only method that "clearly outperforms all other methods, in all settings" on feature-selection metrics (pdf p. 30).
   - Sarwar et al.: regularized L0Learn exceeds CIO/SS and is faster.
   - The parties measure different things (prediction vs support recovery) under different budgets.
2. **Is MIO best subset affordable?**
   - BKM: provable optimality "in minutes" for n in the 1000s, p in the 100s.
   - HTT: one hour or more is typical at n = 500, p = 100, and 3 minutes per k was all they could afford.
   - BPV: "substantial, yet often affordable".
   - Sarwar et al.: over 8 h per (k, γ) path.
   - Chen–Taeb–Bühlmann: an hour to certify at n = 500, p = 100.
3. **OCT against CART**: OCT reports a 1–2% average gain over CART. Hu et al. read the same paper as showing CART "often dominates". Verwer–Zhang found depth-4 OCT close to or below CART.
4. **"Optimal" trees**: the title says optimal. The paper says most results lack optimality certificates. Hu et al. call example trees "clearly suboptimal".
5. **Code availability**:
   - BPV released code for unimplemented methods (abstract), and Sarwar et al. commend both groups' openness.
   - Yet Chen–Taeb–Bühlmann could not run the CIO code.
   - OCT code was not public (Hu et al.; Aghaei et al.), while LST was available for academic use (Aghaei et al.). Wu et al. call the software proprietary.
6. **Boston outcome and framing**: PNAS says "delayed" and blames "special interest groups". The 2021 thesis says "not implemented". Goodman says "abandoned", "Politics killed the algorithm", and reports civil-rights groups, meant to benefit from the equity objective, among the opponents.
7. **DELPHI accuracy**: the self-reported 11% two-week MdAPE on deaths against Cramer et al.'s relative WIS 0.99 (about the naive baseline) on weekly incident deaths.
8. **Robust inventory**:
   - B&T: Theorem 3.2 gives the "Optimal Robust Policy".
   - Bienstock–Özbay (S): a conservative approximation, though empirically effective for stationary costs.
   - Park: "incorrect, which invalidates all of the results", yet all of B&T's properties hold under a different (cumulative-demand) set.
9. **Speed-up figures**: 200 billion (2015 preprint), 450 billion (2016 journal), 800 billion (2017), with the algorithmic factor moving 580,000 → 780,000 → 1,400,000 as Gurobi versions were added.
10. **Prescriptive trees**: the title says "optimal prescriptive trees". Jo et al. describe training by coordinate descent from random starts with no released code.

---

## Gaps

- **Rejoinders not read**: BPV (DOI 10.1214/20-STS701REJ) and HTT (DOI 10.1214/20-STS733REJ). Project Euclid answered with a bot-check page (not bypassed); OpenAlex lists no open copy of the BPV rejoinder. **This is the main gap**: his only known direct printed answer to a critique.
- **Mazumder's and George's discussions**: only S2 snippets and George's first paragraph. The HTT 2020 published version: snippets only (its new Section 4 on L0Learn not read).
- **No reply found** from Bertsimas to: Hu et al., Verwer–Zhang, Günlük et al., Aghaei et al., Jo et al., Park 2014, Bienstock–Özbay, Whitt–You. Searched in Crossref relations and S2 citing records of the critics' papers only partially.
- **Bienstock–Özbay 2008 full text**: ScienceDirect 403. Its exact verdict on B&T is known from snippets and Park's summary.
- **Almgren–Chriss 2001**: not read (author copy 403).
- **Gregory–Darby-Dowman–Mitra 2011**: which "disadvantages" of the correlated model: not read.
- **OPOM (liver allocation)**: no published critique found. The OPTN Liver Committee summary (11 Oct 2022) could not be retrieved (the URL now redirects to the HRSA site).
- **Boston**: the IJAA 2020 Wagner Prize paper (closed) and Bertsimas's own press statements (Boston Globe, paywalled) not read. Local coverage (Bay State Banner, Dec 2017) located by search but not read.
- **OCT systematic harvest**: S2 returned 0 citations for the OCT DOI, and the search endpoint was rate-limited. Critics were found by targeted reading, so unknown critics may exist (e.g. DL8.5, MurTree, TAO papers not read).
- **Speed-up claim**: no critique found (1 WebSearch, plus BKM contexts). Unknown whether anyone has challenged multiplying solver and supercomputer factors.
- **Textbooks**: Ye's 1998 review located, not read. No review found for *Optimization over Integers* or *Machine Learning under a Modern Optimization Lens*.
- **Not checked for critique**: air transportation, revenue management, achievable-region and conservation-law queueing, large deviations, approximation algorithms, *The Analytics Edge*.
- **Rejected papers, referee reports**: none public. Sibling 06 lists long-pending "submitted" papers whose status is unknown (S).
- **A lead not followed**: MIT DSpace item 1721.1/153845 (2024), "A Simulated Annealing Approach to Designing Optimal Decision Trees for Classification, Prescriptive, and Survival Analysis". Only the title was seen; authorship and content were not checked. It may document the move from MIO to heuristics for trees.
- **Bertsimas–Nohadani–Teo convergence guarantees**: not read, so §8's DFO remark is inferred.
- **DELPHI abstract provenance**: whether the OpenAlex-stored abstract is the medRxiv one was not checked.

---

## Sources

P = primary (the item's own text read in this run; "abstract" when only the abstract); S = secondary (snippet, metadata, or sibling note).

### A. Bertsimas's own texts (as author or co-author)
1. D. Bertsimas, A. King, R. Mazumder, "Best subset selection via a modern optimization lens", Ann. Statist. 44(2):813–852, 2016. DOI 10.1214/15-AOS1388; homepage copy (P)
2. Same, arXiv 1507.03133v1, 11 Jul 2015 (P)
3. D. Bertsimas, J. Pauphilet, B. Van Parys, "Sparse regression: scalable algorithms and empirical performance", Stat. Sci. 35(4):555–578, 2020. DOI 10.1214/19-STS701; arXiv 1902.06547v2 (P)
4. D. Bertsimas, J. Pauphilet, B. Van Parys, "Rejoinder: Sparse regression…", Stat. Sci. 35(4):623–624, 2020. DOI 10.1214/20-STS701REJ (S: metadata, not read)
5. D. Bertsimas, B. Van Parys, "Sparse high-dimensional regression: exact scalable algorithms and phase transitions", Ann. Statist. 48(1):300–323, 2020. DOI 10.1214/18-AOS1804 (S)
6. D. Bertsimas, J. Dunn, "Optimal classification trees", Mach. Learn. 106(7):1039–1082, 2017. DOI 10.1007/s10994-017-5633-9; DSpace 1721.1/110328 (P)
7. D. Bertsimas, R. Shioda, "Classification and regression via integer optimization", Oper. Res. 55(2):252–271, 2007. DOI 10.1287/opre.1060.0360 (S)
8. D. Bertsimas, J. Dunn, N. Mundru, "Optimal prescriptive trees", INFORMS J. Optim. 1(2):164–183, 2019. DOI 10.1287/ijoo.2018.0005 (S)
9. D. Bertsimas, N. Kallus, "From predictive to prescriptive analytics", Mgmt. Sci. 66(3):1025–1044, 2020. DOI 10.1287/mnsc.2018.3253; arXiv 1402.5481 v1–v3 history (P for the arXiv record; paper S)
10. D. Bertsimas, B. Van Parys, "Bootstrap robust prescriptive analytics", Math. Program. 195(1–2):39–78, 2022 (online 2021). DOI 10.1007/s10107-021-01679-2; arXiv 1711.09974v2 (P)
11. D. Bertsimas, M. Sim, "The price of robustness", Oper. Res. 52(1):35–53, 2004. DOI 10.1287/opre.1030.0065; homepage copy (P)
12. D. Bertsimas, M. Sim, "Robust discrete optimization and network flows", Math. Program. 98:49–71, 2003. DOI 10.1007/s10107-003-0396-4 (S)
13. D. Bertsimas, V. Gupta, N. Kallus, "Data-driven robust optimization", Math. Program. 167(2):235–292, 2018. DOI 10.1007/s10107-017-1125-8; homepage copy (P)
14. D. Bertsimas, D. den Hertog, J. Pauphilet, "Probabilistic guarantees in robust optimization", SIAM J. Optim. 31(4):2893–2920, 2021. DOI 10.1137/21m1390967 (P, abstract)
15. D. Bertsimas, A. Thiele, "A robust optimization approach to inventory theory", Oper. Res. 54(1):150–168, 2006. DOI 10.1287/opre.1050.0238; homepage copy (P)
16. D. Bertsimas, D. A. Iancu, P. A. Parrilo, "Optimality of affine policies in multistage robust optimization", Math. Oper. Res. 35(2):363–394, 2010. DOI 10.1287/moor.1100.0444 (S)
17. D. Bertsimas, V. Goyal, "On the power and limitations of affine policies in two-stage adaptive optimization", Math. Program. 134(2):491–531, 2012. DOI 10.1007/s10107-011-0444-4; homepage copy (P)
18. D. Bertsimas, A. Georghiou, "Design of near optimal decision rules in multistage adaptive mixed-integer optimization", Oper. Res. 63(3):610–627, 2015. DOI 10.1287/opre.2015.1365 (S)
19. C. Bandi, D. Bertsimas, N. Youssef, "Robust queueing theory", Oper. Res. 63(3):676–700, 2015. DOI 10.1287/opre.2015.1367 (S)
20. D. Bertsimas, O. Nohadani, K. M. Teo, "Robust optimization for unconstrained simulation-based problems", Oper. Res. 58(1):161–178, 2010. DOI 10.1287/opre.1090.0715 (S)
21. D. Bertsimas, I. Popescu, "Optimal inequalities in probability theory: a convex optimization approach", SIAM J. Optim. 15(3):780–804, 2005. DOI 10.1137/S1052623401399903 (S)
22. D. Bertsimas, A. W. Lo, "Optimal control of execution costs", J. Financial Markets 1(1):1–50, 1998. DOI 10.1016/S1386-4181(97)00012-8; homepage copy (P)
23. D. Bertsimas, A. Delarue, S. Martin, "Optimizing schools' start time and bus routes", PNAS 116(13):5943–5948, 2019. DOI 10.1073/pnas.1811462116; DSpace 1721.1/129829 (P)
24. D. Bertsimas, A. Delarue, W. Eger, J. Hanlon, S. Martin, "Bus routing optimization helps Boston Public Schools design better policies", INFORMS J. Appl. Anal. 50(1):37–49, 2020. DOI 10.1287/inte.2019.1015 (S: abstract)
25. M. L. Li, H. Tazi Bouardi, O. Skali Lami, T. A. Trikalinos, N. K. Trichakis, D. Bertsimas, "Forecasting COVID-19 and analyzing the effect of government interventions", Oper. Res. 71(1):184–201, 2023. DOI 10.1287/opre.2022.2306; medRxiv DOI 10.1101/2020.06.23.20138693 (P, abstracts)
26. D. Bertsimas, A. King, "OR Forum—An algorithmic approach to linear regression", Oper. Res. 64(1):2–16, 2016. DOI 10.1287/opre.2015.1436; with E. J. Pinker's introduction, DOI 10.1287/opre.2016.1479; no commentaries found in the issue (S)
27. D. Bertsimas, V. F. Farias, N. Trichakis, "The price of fairness", Oper. Res. 59(1):17–31, 2011. DOI 10.1287/opre.1100.0865 (S)
28. D. Bertsimas, J. Tsitsiklis, "Simulated annealing", Stat. Sci. 8(1):10–15, 1993. DOI 10.1214/ss/1177011077 (S: zbMATH summary)
29. A. Delarue, *Optimizing School Operations*, PhD thesis, MIT Sloan/ORC, 2021 (supervisor D. Bertsimas). DSpace 1721.1/139320 (P)
30. D. Bertsimas, homepage paper archive, https://www.mit.edu/~dbertsim/papers.html, accessed 2026-10-28 (P)

### B. Critics and observers whose own texts I read (or whose metadata I checked)
31. T. Hastie, R. Tibshirani, R. J. Tibshirani, "Extended comparisons of best subset selection, forward stepwise selection, and the lasso", arXiv 1707.08692v2, 2017 (P)
32. Same authors, "Best subset, forward stepwise or lasso? Analysis and recommendations based on extensive comparisons", Stat. Sci. 35(4):579–592, 2020. DOI 10.1214/19-STS733 (S: snippets)
33. Same authors, "Rejoinder: Best subset, forward stepwise or lasso?…", Stat. Sci. 35(4):625–626, 2020. DOI 10.1214/20-STS733REJ (S: metadata, not read)
34. O. Sarwar, B. Sauk, N. V. Sahinidis, "A discussion on practical considerations with sparse regression methodologies", Stat. Sci. 35(4):593–601, 2020. DOI 10.1214/20-STS806; arXiv 2011.09362v2 (P)
35. Y. Chen, A. Taeb, P. Bühlmann, "A look at robustness and stability of ℓ1- versus ℓ0-regularization: discussion of papers by Bertsimas et al. and Hastie et al.", Stat. Sci. 35(4):614–622, 2020. DOI 10.1214/20-STS809; ETH Research Collection (P)
36. E. I. George, "Modern variable selection in action: comment on the papers by HTT and BPV", Stat. Sci. 35(4):609–613, 2020. DOI 10.1214/20-STS808 (S: first paragraph)
37. R. Mazumder, "Discussion of 'Best subset, forward stepwise or lasso?…'", Stat. Sci. 35(4):602–608, 2020. DOI 10.1214/20-STS807 (S: snippets)
38. R. Mazumder, P. Radchenko, A. Dedieu, "Subset selection with shrinkage: sparse linear modeling when the SNR is low", Oper. Res. 71(1):129–147, 2023. DOI 10.1287/opre.2022.2276; arXiv 1708.03288v4 (P)
39. H. Hazimeh, R. Mazumder, "Fast best subset selection: coordinate descent and local combinatorial optimization algorithms", Oper. Res. 68(5):1517–1537, 2020. DOI 10.1287/opre.2019.1919 (S)
40. R. J. Tibshirani, `best-subset` repository README, github.com/ryantibs/best-subset (P)
41. X. Hu, C. Rudin, M. Seltzer, "Optimal sparse decision trees", NeurIPS 2019. arXiv 1904.12847v6 (P)
42. S. Verwer, Y. Zhang, "Learning optimal classification trees using a binary linear program formulation", Proc. AAAI 33:1625–1632, 2019. DOI 10.1609/aaai.v33i01.33011624 (P)
43. O. Günlük, J. Kalagnanam, M. Li, M. Menickelly, K. Scheinberg, "Optimal decision trees for categorical data via integer programming", J. Global Optim. 81:233–260, 2021. DOI 10.1007/s10898-021-01009-y; arXiv 1612.03225v3 (P)
44. S. Aghaei, A. Gómez, P. Vayanos, "Strong optimal classification trees", Oper. Res. 73(4):2223–2241, 2025. DOI 10.1287/opre.2021.0034; arXiv 2103.15965v3 (P)
45. N. Jo, S. Aghaei, A. Gómez, P. Vayanos, "Learning optimal prescriptive trees from observational data", Mgmt. Sci. 2026. DOI 10.1287/mnsc.2021.02813; arXiv 2108.13628v2 (P)
46. U. Sadana, A. Chenreddy, E. Delage, A. Forel, E. Frejinger, T. Vidal, "A survey of contextual optimization methods for decision-making under uncertainty", EJOR 320(2), 2025. DOI 10.1016/j.ejor.2024.03.020; arXiv 2306.10374v2 (P)
47. R. Kannan, G. Bayraksan, J. Luedtke, "Data-driven sample average approximation with covariate information", arXiv 2207.13554v1, 2022 (P)
48. D. A. Iancu, N. Trichakis, "Pareto efficiency in robust optimization", Mgmt. Sci. 60(1):130–147, 2014. DOI 10.1287/mnsc.2013.1753 (P, abstract)
49. M. Poss, "Robust combinatorial optimization with variable budgeted uncertainty", 4OR 11:75–92, 2013. DOI 10.1007/s10288-012-0217-9 (P, abstract)
50. E. Álvarez-Miranda, I. Ljubić, P. Toth, "A note on the Bertsimas & Sim algorithm for robust combinatorial optimization problems", 4OR 11:349–360, 2013. DOI 10.1007/s10288-013-0231-6 (P, abstract)
51. T. Lee, C. Kwon, "A short note on the robust combinatorial optimization problems with cardinality constrained uncertainty", 4OR 12:373–378, 2014. DOI 10.1007/s10288-014-0270-7 (P, abstract)
52. K. Park, "An alternative approach to the robust inventory control problem", Mgmt. Sci. Financ. Eng. 20(2):1–5, 2014. DOI 10.7737/MSFE.2014.20.2.001; KoreaScience PDF (P)
53. W. Whitt, W. You, "Using robust queueing to expose the impact of dependence in single-server queues", Oper. Res. 66(1):184–199, 2018. DOI 10.1287/opre.2017.1649 (P, abstract)
54. W. Whitt, W. You, "A robust queueing network analyzer based on indices of dispersion", Nav. Res. Logist. 69(1):36–56, 2022. DOI 10.1002/nav.22010; arXiv 2003.11174v1 (P)
55. M. Menickelly, S. M. Wild, "Derivative-free robust optimization by outer approximations", Math. Program. 179:157–193, 2020. DOI 10.1007/s10107-018-1326-9; OSTI 1631967 (P)
56. E. Y. Cramer et al., "Evaluation of individual and ensemble probabilistic forecasts of COVID-19 mortality in the United States", PNAS 119(15), 2022. DOI 10.1073/pnas.2113561119; PMC9169655 (P)
57. E. P. Goodman, "Smart algorithmic change requires a collaborative political process", The Regulatory Review, 12 Feb 2019. https://www.theregreview.org/2019/02/12/goodman-smart-algorithmic-change-requires-collaborative-political-process/ (P)

### C. Secondary: snippets, metadata, tools
58. H. Wu et al., "Interpretable personalized experimentation", KDD 2022. DOI 10.1145/3534678.3539175 (S)
59. A. N. Elmachtoub, P. Grigas, "Smart 'predict, then optimize'", Mgmt. Sci. 68(1):9–26, 2022. DOI 10.1287/mnsc.2020.3922 (S)
60. Z. Xie, A. Abdin, Y. Fang, "Data-driven maintenance optimization: aligning prognostic learning with decision objective", arXiv 2506.19698, 2025 (S)
61. J. G. M. van der Linden, M. M. de Weerdt, E. Demirović, "Optimal decision trees for separable objectives: pushing the limits of dynamic programming", arXiv 2305.19706, 2023 (S)
62. C. Büsing, T. Gersing, A. M. C. A. Koster, "A branch and bound algorithm for robust binary optimization with budget uncertainty", Math. Program. Comput. 15:269–326, 2023. DOI 10.1007/s12532-022-00232-2 (S)
63. C. Gregory, K. Darby-Dowman, G. Mitra, "Robust optimization and portfolio selection: the cost of robustness", EJOR 212(2):417–428, 2011. DOI 10.1016/j.ejor.2011.02.015 (S)
64. D. Bienstock, N. Özbay, "Computing robust basestock levels", Discrete Optim. 5(2):389–414, 2008. DOI 10.1016/j.disopt.2006.12.002 (S)
65. Ö. N. Attila, A. Agra, K. Akartunalı, A. Arulselvan, "Robust formulations for economic lot-sizing problem with remanufacturing", EJOR 288(2):496–510, 2021. DOI 10.1016/j.ejor.2020.06.016 (S)
66. H. Mamani, S. Nassiri, M. R. Wagner, "Closed-form solutions for robust inventory management", Mgmt. Sci. 63(5):1625–1643, 2017. DOI 10.1287/mnsc.2015.2391 (S)
67. W. Whitt, W. You, "The advantage of indices of dispersion in queueing approximations", Oper. Res. Lett. 47(2):99–104, 2019. DOI 10.1016/j.orl.2019.01.001 (S)
68. D. A. Goldberg, Y. Li, "Heavy-tailed queues in the Halfin-Whitt regime", arXiv 1707.07775, 2017 (S)
69. S. Leyffer, M. Menickelly, T. Munson, C. Vanaret, S. M. Wild, "A survey of nonlinear robust optimization", INFOR 58(2):342–373, 2020. DOI 10.1080/03155986.2020.1730676 (S)
70. L. Zheng, J. Bao, Z. Tan, "Robust simulation-based optimization for multiobjective problems with constraints", Ann. Oper. Res. 346:1897–1927, 2024. DOI 10.1007/s10479-024-05963-0 (S)
71. S. Cakmak, D. Wu, E. Zhou, "Solving Bayesian risk optimization via nested stochastic gradient estimation", IISE Trans., 2021. DOI 10.1080/24725854.2020.1869352 (S)
72. S. Athey, G. W. Imbens, "Machine learning methods that economists should know about", Annu. Rev. Econ. 11:685–725, 2019. DOI 10.1146/annurev-economics-080217-053433 (S)
73. A. Kenney, F. Chiaromonte, G. Felici, "MIP-BOOST: efficient and effective L0 feature selection for linear regression", J. Comput. Graph. Statist. 30(3):566–577, 2021. DOI 10.1080/10618600.2020.1845184 (S)
74. Y. Ye, review of *Introduction to Linear Optimization* (Bertsimas and Tsitsiklis), IIE Transactions 30(9):855, 1998. DOI 10.1080/07408179808966531 (S: metadata, not read)
75. S. He, J. Zhang, S. Zhang, "Bounding probability of small deviation: a fourth moment approach", Math. Oper. Res. 35(1):208–232, 2010. DOI 10.1287/moor.1090.0438 (S)
76. A. Lodi, S. Sankaranarayanan, G. Wang, "A framework for fair decision-making over time with time-invariant utilities", EJOR 319(2):456–467, 2024. DOI 10.1016/j.ejor.2023.11.030 (S)
77. R. Almgren, N. Chriss, "Optimal execution of portfolio transactions", J. Risk 3(2):5–39, 2001. DOI 10.21314/jor.2001.041 (S: metadata, not read)
78. Semantic Scholar Graph API, citation contexts of 19 Bertsimas papers (15,853 records, 8,785 with contexts), queried 2026-10-28 (S, tool)
79. zbMATH Open API, document search for Bertsimas items, queried 2026-10-28 (S, tool)
80. Sibling research note `06-trajectory.md` (Interpretable AI founding; faded RO-for-stochastic-analysis programme; arXiv 1402.5481 history, re-verified), 2026-10-28 (S, cross-reference only)

---

## Update 2026-10-29 (increment books-2026-10-29): published reviews of his books

> Stage T4, increment "books-2026-10-29". Four reviews of his books were found and carded in this increment, each read in full: works.json B005, B010, B012 and B016, on the cards in `cards/c5-01.md`, `c5-03.md`, `c5-04.md` and `c5-05.md`. Every review below is the reviewer's voice, never evidence of Bertsimas's methods. Citations: `[B005 p. 13]` = card B005 at the file page. The sections above stay as written in the web pass of 2026-10-28; where these reviews change them, the last subsection says so. Full account of the book material: `09-evidence-ledger.md#books`; synthesis: `08-deep-reading-synthesis.md`, section "Increment books-2026-10-29".

### Overview rows (continuing the table of §0)

| # | Target (domain) | Critic(s), year | Critique in one line | Kind | Answered? How |
|---|---|---|---|---|---|
| 18 | *Introduction to Linear Optimization*, with Tsitsiklis, 1997 (LO, IO) | M. V. Ramana, *Optima* 54, June 1997 | Praise for the pedagogy, the geometric explanations and chapters 8, 9 and 12; six criticisms of coverage and density | review, positive with criticisms | **No reply known.** The authors' errata sheet (68 items by printing, last updated 7/5/2021) [B003 pp. 1–5] corrects local errors; by the card's classification of its items, none concerns the points Ramana raised [inferred] |
| 19 | *Machine Learning under a Modern Optimization Lens*, with Dunn, 2019 (ML) | T. Cuvelier, developpez.com, 6 December 2020 | Not yet followed by the wider AI community; mostly the authors' own research; no widespread implementation of most algorithms; demanding prerequisites | review, positive with limits | **No reply known** |
| 20 | *Robust and Adaptive Optimization*, with den Hertog, 2022 (RO) | T. Cuvelier, developpez.com, 2 December 2022 | Pragmatic (computing time over complexity class), theory well covered, the link with probability unusually explicit; no criticism | review, positive | n/a |
| 21 | *Data, Models, and Decisions*, with Freund, 2000 and 2004 (DA) | unsigned, GraduateTutor.com, about 2014 [inferred] | One combined course drops standard topics and may cost depth | review, positive with a question; weak (unsigned, commercial) | n/a |

### Ramana (1997) on *Introduction to Linear Optimization* [observed, P]
- **Source**: M. V. Ramana, review, *Optima* 54 (June 1997), pp. 13–14, the newsletter of the Mathematical Programming Society (now the Mathematical Optimization Society), openly hosted at mathprog.org [B005 pp. 13–14].
- **Praise**: the pedagogy is the book's "true merit", so that he adopts it for his own LP course [B005 p. 13]; chapters 8 and 9, with chapter 12, "alone are a good enough reason for one to buy this book" [B005 p. 13]; the final chapter is "unique to this book" [B005 p. 14]; the geometric and intuitive explanations are "widely successful" [B005 p. 14].
- **Criticisms** (the reviewer's): the upper-bounded simplex method is the one aspect of the simplex coverage he finds missing; the network simplex is developed for the uncapacitated case first; "In trying to cover too many topics in one chapter, I feel that the authors have somewhat compromised the clarity of exposition in this chapter." (chapter 7); chapter 6 is "rather brisk but is sufficient" [B005 p. 13]. In chapter 11 the Gomory convergence proof is omitted, branch-and-bound and branch-and-cut are brief, and a section on complexity classes appears "out of the blue"; at times the tone is that of a research paper and the material feels dense [B005 p. 14].
- **Reception record**: the publisher's page quotes three of his praising sentences and none of the criticisms [B002 p. 1]. The section he found "out of the blue" (11.8, Complexity theory) is in the printed contents [B004 p. 5] but missing from the publisher's web contents [B002 p. 2]. J. Bard's review (*Interfaces* 30(4), 2000) is known only from the publisher's excerpt, "at the top of the list" [B002 p. 1]; Y. Ye's 1998 review (row 17's lead, §6) stays unread.

### Cuvelier (2020) on *Machine Learning under a Modern Optimization Lens* [observed, P]
- **Source**: T. Cuvelier, "Critique du livre par la rédaction", developpez.com, 6 December 2020, in French [B010 p. 1]; English renderings below are outside quotation marks.
- **Praise**: a new viewpoint; each technique introduced from first principles, with the current heuristics and their drawbacks first; rigorous yet readable; usable also as an advanced optimization text [B010 p. 1].
- **Limits named**: "Ce parti pris n'est pas encore suivi par la communauté de l'intelligence artificielle au sens large" (the stance is not yet followed by the wider AI community); a good part of the content is the authors' and their collaborators' own research; "En particulier, cela signifie qu'il n'existe pas encore d'implémentation répandue pour la plupart des algorithmes présentés." (in particular, there is not yet a widespread implementation for most of the algorithms presented); demanding prerequisites, chiefly convex and integer optimization [B010 p. 1].
- **How the reviewer reads the headline**: methods that bring optimal solutions "impossibles à améliorer" (impossible to improve) [B010 p. 1], stronger than the publisher's own "can be certified to be optimal in minutes/hours" [B010 p. 1] (the card's comparison).

### Cuvelier (2022) on *Robust and Adaptive Optimization* [observed, P]
- **Source**: T. Cuvelier, "Critique du livre par la rédaction", developpez.com, 2 December 2022, in French [B012 p. 1].
- **Reading**: "L'auteur y poursuit une approche très pragmatique, où les temps de calcul en pratique sont plus importants qu'une classe de complexité abstraite." (a very pragmatic approach, in which computing times in practice matter more than an abstract complexity class); the theory, adaptive or distributional, is well covered, from the foundations in duality to equivalences between robust and adaptive optimization; modelling and solution algorithms stressed; "Le lien avec les probabilités est rarement aussi explicite et détaillé." (the link with probability is rarely this explicit and detailed), with characterizations of constraint-violation probabilities [B012 p. 1].
- **Limits**: none stated. The review does not bear on any of the RO critiques of §4 (Pareto efficiency of budgeted optima, the 2006 inventory formulation, affine policies, robust queueing).

### GraduateTutor.com (about 2014) on *Data, Models, and Decisions* [observed, weak]
- **Source**: an unsigned page of a company that sells tutoring for the book, linked from the publisher's page [B016 p. 1; B014 p. 1]. Weak evidence: no reviewer can be named.
- **Reading**: "Unlike most text books, the objective is not to cover standard topics in statistics and operations research but to provide students frameworks for decision making." [B016 p. 1]; one book for two subjects usually taught in two courses; decision trees first.
- **Limits named**: combining two courses drops standard topics (descriptive statistics, hypothesis testing, inference and analysis of variance, the expected value of perfect information; discriminant analysis, forecasting, queueing theory); "One wonders, however, if students would be better off having more depth in statistics and operations management separately." [B016 p. 1]. At title level the 2000 contents agree that no section names these topics, except that confidence intervals and two-sample comparisons are there [B015 pp. 1–5] (the card's check).

### What this changes above
- **§0 row 17** ("Moment problems, textbooks, SDVRP, OPOM: none found"): for the textbooks, rows 18–21 above now exist; moment problems, SDVRP and OPOM are unchanged.
- **§6, "LO/IO textbooks"**: a signed review of *Introduction to Linear Optimization* is now read in full (Ramana); Ye's review stays unread; no review of *Optimization over Integers* was carded in this increment either.
- **Gaps, "Textbooks"**: "No review found for ... *Machine Learning under a Modern Optimization Lens*" no longer holds [B010 p. 1]. "Not checked for critique: ... *The Analytics Edge*": still no review carded.
- **§7, pattern 3** (silence on reproducibility critiques): the 2020 reviewer's point that most of the ML book's algorithms have no widespread implementation [B010 p. 1] is an outside reader's version of the same gap; no reply found.
- The two signed reviews of the theory books praise their stated design (geometry and practice in 1997; pragmatism and probability in 2022). Ramana's criticisms concern coverage and density, not correctness [B005 pp. 13–14]; Cuvelier's RO review states none [B012 p. 1]; his 2020 ML review names adoption and implementation limits [B010 p. 1].

# 03 · Process evidence (what Bertsimas and his group actually DID)

> **Researcher**: Dimitris Bertsimas, Boeing Professor of Operations Research, MIT Sloan School of Management and Operations Research Center (ORC); MIT Vice Provost for Open Learning since 2024 (CV). Living. Google Scholar `prKmkzMAAAAJ`; ORCID 0000-0002-1985-1003; OpenAlex A5025940525. Not Dimitri P. Bertsekas (MIT LIDS), a different person.
> **Dimension**: research agent 03 of 06, process evidence (framework §二, agent 3): behaviour traces, not statements. Layers 4 (execution) and 5 (judging results) dominate; layers 2, 3, 6 and 7 appear only where an artefact shows behaviour.
> **Research date**: 2026-10-28.
> **Sources consulted**: 72 (62 primary, 10 secondary), numbered under "Sources". 30 of them were seen only as bibliographic or version records (marked "metadata", "record" or "version history"), 2 were identified but could not be read (closed access), and 1 is a search listing used only for leads. Everything that could not be read is listed under "Gaps".
> **Search budget**: 2 of the 5 allowed WebSearch calls (an OpenReview listing; an open copy of a rejoinder). Everything else came from curl on known URLs, the Crossref, arXiv, OpenAlex, GitHub and MIT DSpace APIs, and three WebFetch calls (two Project Euclid pages and one OpenReview PDF, all of which returned no content).
> **Local corpus**: `references/sources/papers`, `essays`, `software` and `publications` hold only `.gitkeep`; `RESOURCES.md` is the unfilled template. `talks/` holds one transcript that another agent saved during this workflow run (Sloan Oral History interview, 24 Oct 2014); it is not user-supplied. No finding below is "from user-supplied material". `references/sources/private/` was not opened.
> **Sibling notes**: `02-methodology.md` (agent 02, stated method) was read for cross-reference only; §E sets its stated claims against the practice found here. Notes 01, 04, 05 and 06 did not exist when this file was written.
> **Verification**: every identifier was resolved in this run (Crossref works API, arXiv abstract pages, DSpace and GitHub APIs). Every quotation was matched by script against the saved copy of its source (pdftotext output, saved HTML, README files, the CV text, commit messages), with two exceptions: the 1993 simulated-annealing paper is a scanned image without a text layer, so its two quoted phrases were checked by eye against the page image (journal p. 13). Paper titles were checked against Crossref records; quotation marks inside titles are rendered as single quotes. PDF page numbers were found by a per-page search. Quotations are kept short; everything else is paraphrase and is never placed inside quotation marks. "p." gives journal pagination where the copy shows it, otherwise "PDF p.".
> **Tags**: [stated] Bertsimas said or wrote it (sole-author text, homepage, CV, interview); [practice] a documented act in a paper, code, record or version history; [observed] written by third parties; [inferred] my reading. **P / S**: primary / secondary. **Actor**: **DB** for his own act (homepage, CV, sole-authored or two-author text where he is the senior author), **group** for co-authored or supervised work (students, postdocs, co-authors), **company** for Interpretable AI or Dynamic Ideas artefacts. Domain codes from `team.json` in braces: {LO IO RO CP SD ML DA HS AP}.
> **Caveat on authorship**: from about 2010 nearly every artefact is multi-author and the code is written by students and postdocs. Such items show group practice under his direction, not his own hand. Author order in operations research is usually alphabetical, so being first author says little (see B7).

---

## 0. What this file adds

Note 02 recorded what Bertsimas says research should be. This note follows artefacts: experimental sections, code repositories and their commit logs, arXiv version histories, the received, revised and accepted dates that journals print, correction notices, discussion-and-rejoinder records, the public lists of manuscripts marked as submitted on his homepage and CV, and what happened to the manuscripts on those lists. §E lines up 02's stated claims against these traces; §F lists process patterns for Phase 2.

## A. Era and resource context of the practices below

| Period | Position and organisation (CV) | Tools and compute seen in the artefacts | Team size (CV thesis list; OpenAlex) | Artefacts examined here |
|---|---|---|---|---|
| 1988–1999 | assistant professor 1988, full professor 1996, Boeing Professor 1997 | theory papers with small numerical illustrations; LP book from notes class-tested for about ten years (oral history p. 11) | 21 PhD completions 1990–1999; median 2 authors per article | simulated-annealing review 1993; queueing correction 1997; LP textbook errata |
| 2000–2009 | founded Dynamic Ideas LLC 1998 (assets sold to American Express 2002); D2-Hawkeye board 2003–2009; ORC co-director from 2006 | CPLEX 6.0 on a Pentium II 400 PC (2001–2004) | 20 PhD completions 2000–2009; median 2 authors | Price of Robustness 2004; health-care costs 2008; old-homepage working papers |
| 2010–2019 | founded the MBAn programme 2013; Management Science area editor 2009–2015; Editor in Chief of the INFORMS Journal on Optimization 2017–2024; co-founded Interpretable AI 2018 | GAMS and CPLEX 12.1 on a laptop (2011–2013); Matlab 2012b and Gurobi 5.5 (2014–2015); Julia/JuMP and Gurobi 6.5 on Amazon EC2 (2015–2017); student GitHub packages with continuous integration | 31 PhD completions 2010–2019; median 3 authors | unit commitment 2013; best subset 2016; optimal trees 2017; Dunn's thesis 2018; predictive-to-prescriptive 2014–2020; PNAS 2019 |
| 2020–2026 | J-Clinic co-director 2020–2025; Vice Provost 2024–; founded Holistic Hospital Optimization 2022 | Python, PyTorch, XGBoost; the proprietary Interpretable AI system image; MOSEK 9.2, Gurobi 9.0 and BARON 20.10 (IJOC repository); medRxiv and Research Square | 34 PhD completions 2020–2025 plus 14 current; median 4 authors, maximum 100 | DELPHI 2020–2022; sparse-regression discussion 2020; Voice of Optimization; online MIO; OptiCL; HAIM; IJOC 2026; the CV's submitted list |

Counts: CV thesis list (entries #1–#106 completed, #107–#120 current; the 2026 homepage says 109 completed and 20 current, a later date). OpenAlex: 411 journal articles with a resolvable author position (my count; author disambiguation can be wrong).

---

## B. Findings by layer (framework §一)

### Layer 4. Execution: test problems, baselines, tools, time limits, debugging

#### B4.1 Robust optimization, 2001–2004: the rival school's own test problems, at demonstration scale {RO, LO, IO} [practice · group (DB and his PhD student M. Sim) · P]

- *The Price of Robustness* (Operations Research 52(1):35–53, 2004, DOI 10.1287/opre.1030.0065; received September 2001, revised August 2002, accepted December 2002) reports three experiments in §6 (pp. 44–48):
  - a random 0–1 knapsack with N = 200 and 10% weight uncertainty, solved to optimality with CPLEX 6.0 on a Pentium II 400 PC in 0.05–50 s; full (Soyster-type) protection lowers the objective by 5.5% (5,592 to 5,283);
  - a portfolio problem taken from Ben-Tal and Nemirovski (1999), checked by 10,000 simulated return scenarios;
  - the NetLib problem PILOT4 (411 rows, 1,000 columns), following Ben-Tal and Nemirovski's 2000 NetLib case study; the authors adopt the view that its coefficients "seem unnecessarily precise" (p. 48).
- The paper prints a negative result on PILOT4: relaxing full protection still costs a lot "unless one is willing to accept unrealistically high probabilities for constraint violation" (p. 48). The authors attribute this to the small number of uncertain coefficients per row.
- [inferred] The baselines are the competing robust formulations (Soyster 1973; Ben-Tal–Nemirovski), run on that school's own examples. The scale is a demonstration, not a benchmark study. Era: a 2001-era MIP solver on a desktop PC.

#### B4.2 A partner's live system supplies the instance and the baseline, and the run time is reported {RO, IO, AP, DA} [practice · group · P]

- **Unit commitment** (IEEE Transactions on Power Systems 28(1):52–63, 2013, DOI 10.1109/TPWRS.2012.2205021):
  - Three of the five authors are ISO New England staff (affiliation footnote, p. 52).
  - Test system: the ISO-NE network (312 generating units, 174 loads, 2,816 nodes) with day-ahead market data from a winter day.
  - Baseline: the operator's current reserve-adjustment practice.
  - Implementation: GAMS with CPLEX 12.1.0 on a laptop (Core 2 Duo, 2.5 GHz, 3 GB).
  - Reported cost of the method: "The average computation time to solve the robust UC problem is 6.14 h" (pp. 56–57), against 1.65 h for reserve adjustment. Looser tolerances bring it to 1.46 h at a 0.17% higher worst-case cost.
  - Review: manuscript received 16 March 2011, revised September 2011 and April 2012, accepted May 2012.
- **Health-care costs** (Operations Research 56(6):1382–1392, 2008, DOI 10.1287/opre.1080.0619):
  - Data: claims for 838,242 insured individuals from 2,866 employers, supplied by D2Hawkeye. Two co-authors are D2Hawkeye staff, and the acknowledgment thanks its engineering team for data support (p. 1391). The CV lists DB on D2-Hawkeye's board in 2003–2009.
  - Protocol: random split into equal learning, validation and test parts; the test part is set aside while the models are built.
  - Baseline: last year's cost as the forecast, chosen because "this baseline is much stronger than, for example, random assignment" (p. 1386).
  - Review: received January 2007, revisions August 2007, May 2008 and July 2008, accepted July 2008 (three rounds).
- **From Predictive to Prescriptive Analytics** (Management Science 2020): inventory data from the distribution arm of an international media conglomerate, combined with data scraped from IMDb, Rotten Tomatoes and Google (abstract of arXiv:1402.5481 v3 and v4).
- **Boston Public Schools** (PNAS 2019): BPS 2017–2018 data; the outcome is counted in buses and dollars (50 buses, about $5 million a year).
- [inferred] In application papers the partner's system supplies both the instance and the baseline (the partner's current rule), and the method's run time is reported even when it is several times slower than the incumbent's.

#### B4.3 The "modern optimization lens" protocol as actually run, 2014–2017 {ML, IO} [practice · group · P]

| Item | Best subset selection (Annals of Statistics 2016; arXiv:1507.03133v1) | Optimal classification trees (Machine Learning 2017) | OR Forum regression (Operations Research 2016) |
|---|---|---|---|
| Data | Diabetes data (n = 350, p = 64) and synthetic data (one example uses SNR = 7) | 53 UCI datasets; synthetic trees with known ground truth | real and synthetic data |
| Baselines | Lasso (glmnet 1.7.3), Sparsenet, stepwise regression (R stats 3.0.2), a debiased Lasso | CART (R package rpart), trimmed to the same depth; random forests | — |
| Solver and stack | Gurobi 5.5 through Matlab 2012b and Python 2.7; both machines specified (PDF p. 27) | Julia, JuMP and Gurobi 6.5 on Amazon EC2 c4.xlarge instances (4 vCPU, 7.5 GB RAM) (p. 1062) | mixed-integer quadratic models with time limits |
| Heuristic first | discrete first-order methods with 50 random starts, used as warm starts for the MIO | CART and lower-depth solutions as warm starts | — |
| Time limits | 500 s in the upper-bound comparison (Table 1); longer runs for optimality proofs | 30 min for most OCT problems, up to 2 h for larger ones; 5–15 min for OCT-H; 60 s for greedy warm-start subproblems (p. 1062) | 20 s (n > p) and 40 s (n < p) per problem; the stated aim: "We aim to return solutions in practical amounts of time" (p. 11) |
| Tuning | held-out validation set | 50/25/25 split, repeated over five random splits; the minimum leaf size was not tuned but fixed at 5% of the data, to save computation (p. 1062) | validation set |
| What is admitted | the optimum is found early and the proof comes late: "the global optimum was found within a very small fraction of the total time" (PDF p. 29) | larger data sets were tried and dropped, because "the time required for our methods to generate high-quality solutions was prohibitive" (p. 1061); and "most of our results for OCT and OCT-H do not carry explicit certificates of optimality" (p. 1062) | — |
| Code | no code-availability statement found in the text | no code-availability statement found in the text | — |

- Timeline: the best-subset paper was first submitted in June 2014 ("First Version Submitted for Publication on June, 2014", arXiv v1, PDF p. 1), revised in May 2015, posted to arXiv in July 2015 and printed in April 2016. *Optimal classification trees* was received on 17 September 2015 and accepted on 3 March 2017.
- [observed · S] Hastie, Tibshirani and Tibshirani (arXiv:1707.08692v2, 2017; HTT below) report that Bertsimas, King and Mazumder:
  - "considered SNRs in the range of about 2 to 8" in low-dimensional cases, and about 3 to 10 in high-dimensional ones (p. 4);
  - gave Gurobi 15 minutes per problem and subset size k for p = 100, and 66 minutes for p ≥ 2000 (p. 10).
- [observed · S] HTT re-implemented the method in their R package `bestsubset`, with guidance from the paper's third author ("We thank the third author Rahul Mazumder for his help and guidance", footnote, p. 8).
- [inferred] In 2014–2017 the group published results computed with solver budgets of minutes to an hour per instance and subset size, or per tree, while the same papers argue from speed. Certificates are reported where they were reached, and the claim is otherwise dropped (OCT p. 1062).

#### B4.4 The "why now" number is recomputed for each paper {IO, ML} [practice · group · P]

| Text | Date | Speed-up figure for mixed-integer solvers | How it is built |
|---|---|---|---|
| Best subset selection, abstract and §2 (PDF pp. 1, 7–8) | revised May 2015 | 200 billion (1990–2014) | software: CPLEX 1.2 to 11 (more than 29,000×) and Gurobi 1.0 to 5.5 (more than 20×), 580,000× combined; hardware about 320,000× |
| OR Forum regression, p. 2 | 2015 | 450 billion (1991–2015) | same construction with newer releases |
| Optimal classification trees, abstract | 2017 | 800 billion ("in the last 25 years") | Gurobi 1.0 to 6.5 nearly 50× |
| Dunn's PhD thesis, p. 27 | 2018 | 2 trillion | same construction |

- Note 02 recorded the first three figures as a contradiction (02 C5). The thesis adds a fourth.
- [practice] Each text rebuilds the figure from the latest solver releases and hardware data instead of citing the previous paper's number. The figure serves as the "why now" argument for reopening problems that statistics had treated as intractable.

#### B4.5 When the MIO does not scale: diagnose by counting variables, switch to local search, keep the name {ML, IO, HS} [practice · group, then company · P]

- **Dunn's thesis** (*Optimal Trees for Prediction and Prescription*, MIT 2018, advisor DB; hdl 1721.1/119280), §2.3 "A Local Search Approach" (pp. 47–56):
  - Test: the UCI Banknote Authentication data (n = 1372, p = 4), Gurobi with CART as warm start and a two-hour limit.
  - Result: beyond depth 1 there was no optimality proof, and the MIO lower bound stayed at zero. At depth 6 the solver did not get past the root node. Overall "the MIO approach took 5–6 orders of magnitude longer" than CART, for small to moderate gains (p. 48).
  - The group's judgment: after long runs the MIO solutions "can be far from optimality and offer only small improvements over heuristic solutions" (p. 47).
  - Diagnosis: count the binary variables (n·2^D, or 87,808 at depth 6). Doubling them costs roughly an order of magnitude in solve time (pp. 48–49).
  - Remedy: search only over the split variables, by local search with random restarts. On the same data, with 100 restarts, the local search beats both CART and the MIO at the larger depths (pp. 55–56).
- **Company software** (Interpretable AI; CV: DB co-founder, 2018–present). The Optimal Trees learners train by local search by default. The parameter `ls_num_tree_restarts` sets the "number of random restarts to use in the local search algorithm" (default 100). With `localsearch = false`, "a greedy algorithm similar to CART will be used to train the tree" (learner parameters page, read 2026-10-28). Each machine needs a licence file, and "All licensing is free for academic users" (company homepage).
- **2023**: a PhD thesis titled *A Simulated Annealing Approach to Designing Optimal Decision Trees for Classification, Prescriptive, and Survival Analysis* (S. Sujichantararat, 2023; CV thesis #92). A manuscript, *A Simulated Annealing Approach to Designing Optimal Classification Trees*, is listed in the CV as submitted to Machine Learning in 2023 (#377); Crossref shows no journal version.
- [inferred] What was published (the MIO formulation, 2017) and what is used (local search, 2018 onward) differ, and the word "optimal" stayed with the product. See Contradiction K1.

#### B4.6 Code: none, then student packages, then company software and journal-mandated snapshots {ML, IO, RO, DA, CP} [practice · group/company · P; observed · S]

| Period | Artefact | What it shows |
|---|---|---|
| 2016–2017 | best subset (2016); optimal classification trees (2017) | neither text has a code-availability statement; HTT wrote their own R implementation (`ryantibs/best-subset`, created 2017-01-15) |
| 2014–2019 | `IainNZ/JuMPeR.jl` (created 2014-02-22, last push 2019-02-24) | a robust-optimization modelling layer by a PhD student, documented in a chapter of his thesis; the README points to "(limited) documentation"; no activity after 2019 |
| 2017–2022 | `jeanpauphilet/SubsetSelection.jl` (2017-09-01 to 2022-03-24) and `SubsetSelectionCIO.jl` (2017-11-06 to 2021-08-17) | student packages with continuous integration (Travis, AppVeyor, Codecov, a `test/` folder). The exact cutting-plane code needs Gurobi or CPLEX and stops at a default 60 s limit. The 2020 paper's abstract: "We released code for methods that were not publicly implemented." |
| 2018 | `mitschoolbus/SchoolBusRouting` (MIT licence, created 2018-10-04) | the PNAS paper's code, cited there as reference 28 |
| 2018–2023 | `bstellato/mlopt` (Apache-2.0) | a pytest set-up; the documentation is still announced as coming soon; the interpretable mode calls the proprietary Optimal Trees (*The Voice of Optimization*, §4, PDF p. 21) |
| 2018– | Interpretable AI modules | proprietary; machine-locked licence files; free academic licences |
| 2020–2023 | `COVIDAnalytics/DELPHI` (Apache-2.0) | see B4.7 |
| 2021–2023 | `hwiberg/OptiCL` (MIT licence) | a package with notebooks, including one that checks that the MIO embedding reproduces the scikit-learn predictions |
| 2021–2025 | `lrsoenksen/HAIM` (Apache-2.0) | code to replicate the npj Digital Medicine 2022 paper. The README warns that the experiments need cluster-scale memory and that part of the data cannot be redistributed. The paper trained and characterized 14,324 independent models |
| 2025 | `INFORMSJoC/2023.0345` (created 2025-11-17) | the snapshot the INFORMS Journal on Computing requires, "a snapshot of the software and data that were used in the research". Pinned versions: Julia 1.5.3, JuMP 0.21.6, MOSEK 9.2.45, Gurobi 9.0.2, BARON 20.10.16 (BARON serves as the global-solver baseline) |

- [observed · S] Sarwar, Sauk and Sahinidis (Statistical Science 2020, a discussion paper):
  - they "commend both groups for making the code for their research available open-source", and add that HTT also released their simulation scripts (PDF p. 2);
  - they reproduce one setting of the 2020 Bertsimas–Pauphilet–Van Parys paper (BPV below) from its released code and get slightly different MCP numbers, which they attribute to an implementation difference;
  - they would not use the exact (CIO) or relaxed (SS) estimators in practice because of "relatively demanding computational time needed and lack of seamless hyperparameter selection" (PDF p. 9).
  - Sahinidis is a member of this repository's MINLP Team.
- [inferred] Code release follows the student and the venue, not a group policy. The core tree algorithms went into a company; side packages went onto students' GitHub accounts and stopped when the student graduated; the IJOC rules forced a snapshot. Solver versions from about 2020, pinned in a repository created in November 2025, suggest that the experiments ran about five years before publication.

#### B4.7 What gets done first, and debugging under time pressure: DELPHI, spring 2020 {DA, AP, SD} [practice · group · P]

Source: the commit log of `COVIDAnalytics/DELPHI` (GitHub API: 554 commits under 13 committer names, none of them Bertsimas; 380 commits in April–July 2020), its README and the COVID-19 Forecast Hub folder `CovidAnalytics-DELPHI`.

| Date (2020 unless noted) | Event |
|---|---|
| 04-06 | repository created; the first model was a Mathematica notebook (README) |
| 04-15 to 04-19 | port to Python, with a running version four days later; commits in between fix an equation sign and a missing factor |
| 04-27 | first weekly forecast file in the COVID-19 Forecast Hub (114 files up to 2022-07-11) |
| 05-06 | backtesting code added |
| 05-23 | first running "Continuous Retraining" variant; later discarded |
| 05-29 | "Added all necessary data folders for J&J team": the model is adapted for an industry partner. This became the INFORMS Journal on Applied Analytics paper "Data-Driven COVID-19 Vaccine Development for Janssen" (53(1):70–84, 2023, DOI 10.1287/inte.2022.1150); CV: Edelman finalist 2022 |
| 06-25 | a commit is pushed from the partner's data-science platform; one committer handle carries the suffix of the Dynamic Ideas e-mail domain |
| 06-29 | medRxiv preprint (compiled 26 May) |
| 07-15 | V3, with a resurgence term |
| 09-12 to 09-16 | archive reorganized; the annealing optimizer compared with TNC; confidence intervals added |

- The README keeps the failed variants in an `archive/` folder and labels them. The adaptive-policy model: "It unfortunately didn't yield good enough results and we decided to discard it." The discrete-jump and arctan-jump models: "This implementation was unsuccessful." Other second-wave analyses: "They were unsuccessful."
- 52 of the 554 commit messages contain fix, bug, error, wrong, revert, discard, archive, unsuccess or fail (my count).
- [inferred] The order of work: a running model and a public website first; submission to an external, prospective scoreboard within three weeks; backtesting in week five; then a branch for the partner. Failed variants are documented, not deleted.

### Layer 5. Judging results: negative results, corrections, criticism, revision

#### B5.1 Negative results printed in the papers themselves [practice · group · P]

| Paper | What is admitted | Where |
|---|---|---|
| Price of Robustness 2004 {RO} | on PILOT4, probabilistic protection costs nearly as much as full protection | p. 48 |
| Unit commitment 2013 {RO} | the robust model needs 6.14 h, against 1.65 h for the incumbent rule | pp. 56–57 |
| Optimal classification trees 2017 {ML} | data sets with tens of thousands of points excluded; most results lack optimality certificates | pp. 1061–1062 |
| Sparse high-dimensional regression, arXiv:1709.10029v1 {ML} | on the largest instance (n = 100,000, p = 200,000) "a memory exception was thrown when building the data matrices" | PDF p. 13 |
| PNAS 2019 {AP} | the proposed bell times "have not been implemented yet due to parents concern with the magnitude of the change" | introduction (PMC full text) |
| DELPHI README 2020 {DA} | four model variants labelled unsuccessful or discarded | README |
| Simulated-annealing review 1993 {HS} | in the experiments reviewed, "the performance of SA was mixed"; on the TSP it consistently loses to Lin–Kernighan; theory shows "a definite lack of rigorous results justifying the use of SA" | p. 13 |

#### B5.2 Corrections, withdrawals and errata; no retraction found [practice · P]

- **1997 correction** {SD}: DB, D. Gamarnik and J. N. Tsitsiklis, "Correction to 'Stability Conditions for Multiclass Fluid Queueing Networks'", IEEE Transactions on Automatic Control 42(1):128, January 1997, DOI 10.1109/TAC.1997.553697. It is a one-page notice published two issues after the original (41(11):1618–1631, November 1996, DOI 10.1109/9.543999). Content **not read**: paywalled, and the Semantic Scholar record elides the abstract.
- **2014 withdrawal** {DA}: version 2 of arXiv:1402.5481 (26 June 2014) was withdrawn by N. Kallus with the comment "Withdrawn due to crucial error in Theorem 2.2". Version 3 (February 2015) returned with Bertsimas as co-author (B5.4).
- **2023 publisher correction** {CP, IO}: a Publisher Correction (DOI 10.1007/s10107-023-01947-3) to "A new perspective on low-rank optimization" (Mathematical Programming 202:47–92, DOI 10.1007/s10107-023-01933-9). Content not read. [inferred] A publisher correction usually concerns a production error.
- **Textbook errata** {LO}: *Introduction to Linear Optimization* (with Tsitsiklis, Athena Scientific, 1997) has an errata sheet "Last updated on 7/5/2021" on the publisher's site. It is organized by printing (errors in the first printing corrected in later ones, and so on) and has 68 page-numbered entries [B003 pp. 1–5] (corrected 2026-10-29 from the carded sheet; the earlier count here was "about 33").
- Crossref searches by author (Bertsimas) for erratum, correction, corrigendum, retraction and addendum found only the two corrections above. No retraction was found.

#### B5.3 Answering criticism: the best-subset exchange, 2016–2020 {ML, IO} [practice · group · P; observed · S]

1. **2016**: Bertsimas, King and Mazumder, Annals of Statistics (BKM).
2. **July 2017**: HTT's arXiv paper, subtitled as following BKM. Its findings: best subset wins at high SNR and the Lasso at low SNR; BKM's SNRs were unrealistically high; HTT's own runs gave Gurobi 3 minutes per subset size.
3. **September 2017**: Bertsimas and Van Parys, arXiv:1709.10029 (a new cutting-plane method). Its benchmark table uses SNR = 20, and the v1 text does not cite HTT (searched). [practice]
4. **February 2019**: BPV, arXiv:1902.06547 (Statistical Science 2020), the response paper. Changes to the protocol:
   - it adopts HTT's link between SNR and the proportion of variance explained, and runs SNR from 6 down to 0.05 (PDF p. 10);
   - it adds an ℓ2 penalty to best subset;
   - it scores accuracy and false-discovery rate, and time relative to glmnet;
   - it limits the exact method to 60 s per regression problem (PDF p. 5);
   - it releases Julia packages;
   - it concedes in part: HTT's observations "are still valid but less obvious" once best subset is regularized (PDF p. 23), and it recommends a combination of methods, with the Lasso or elastic net as a screening step followed by a non-convex method (PDF p. 23).
5. **Late 2020**: Statistical Science 35(4) prints BPV and HTT side by side, with four discussions (Sarwar–Sauk–Sahinidis; Mazumder; George; Chen–Taeb–Bühlmann) and two rejoinders. The BPV rejoinder (pp. 623–624, DOI 10.1214/20-STS701REJ) was **not read**: it is closed access, and no open copy was found.

- [observed] BKM's third author helped the critics run the method and told them that a 3-minute budget usually finds, but does not certify, the solution in the medium setting (HTT §3.2, p. 10).
- [inferred] The criticism was answered by a new paper, with a new student, a wider test grid and released code, inside a discussion format. The first paper after the critique (September 2017) did not change its test grid.
- **Second exchange** {RO} (content not read): Y. Z. Li, "Discussion of 'Adaptive Robust Optimization for the Security Constrained Unit Commitment Problem'", and the authors' "Closure to the Discussion of …", IEEE Transactions on Power Systems 29(2):996–997, March 2014, DOIs 10.1109/TPWRS.2014.2301351 and 10.1109/TPWRS.2014.2301352.

#### B5.4 What changes between preprint and journal (no referee reports are public) [practice · group · P]

| Paper | Versions | Change visible in the record |
|---|---|---|
| From Predictive to Prescriptive Analytics {DA, ML} | arXiv:1402.5481 v1 22 Feb 2014 (sole author N. Kallus; 11 pp.); v2 withdrawn 26 Jun 2014; v3 9 Feb 2015 (Bertsimas and Kallus); v4 19 Jul 2018 (57 pp.); Management Science 66(3):1025–1044, 2020 | v1 has a portfolio example and a sweeping claim (its abstract opens a sentence with "Incredibly"). v3 is reframed for OR/MS, uses the media conglomerate's data and introduces the coefficient of prescriptiveness P (88% on the real data). v4 adds decisions that affect the uncertainty (pricing). Six years from v1 to print |
| Best subset selection {ML} | submitted June 2014; revised May 2015; arXiv July 2015 (v1 only); Annals of Statistics, April 2016 | posted only after the first revision |
| Optimal classification trees {ML} | received 17 Sep 2015; accepted 3 Mar 2017 | 18 months in review; no arXiv preprint found by title search |
| The Voice of Optimization {DA, ML} | arXiv:1812.09991 v1 Dec 2018, v3 Jun 2020; Machine Learning 110(2), 2021 | the claim narrows: v1 offers insight into "any continuous and mixed-integer convex optimization problem" and a "novel, reliable and insightful" understanding; v3 drops "any" and "reliable" |
| Online mixed-integer optimization in milliseconds {DA, IO} | arXiv:1907.02206 v1 Jul 2019, v4 Mar 2021; INFORMS Journal on Computing 34(4), 2022 | "benchmarks with real-world data" (v1) became three named applications: fuel-cell energy management, sparse portfolio optimization, motion planning |
| Mixed-integer optimization with constraint learning {DA, IO} | arXiv:2111.04469 v1 Nov 2021, v3 Oct 2023; Operations Research 73(2), 2025 | v3 adds two ways to handle learning uncertainty: a more flexible trust region for low-density and high-dimensional data, and ensembles over bootstrapped estimators. [inferred] robustness additions during review |
| The Price of Robustness {RO} | received Sep 2001; revised Aug 2002; accepted Dec 2002; in print Jan 2004 | — |
| Health-care costs {AP} | received Jan 2007; three revisions; accepted Jul 2008 | — |
| An algorithmic approach to linear regression {ML} | listed as "submitted to Operations Research" on the old homepage; journal history: received and accepted September 2015, in the OR Forum section | [inferred] moved into the OR Forum section |
| Tenure Analytics (OR Forum) {AP} | received Jun 2014; revised May and Sep 2015; accepted Sep 2015 | — |

- [practice] In the 12 arXiv records I opened for preprints Bertsimas co-authored, the submitter is always a co-author (Kallus, Mazumder, Pauphilet, Caramanis, Gupta, Stellato twice, Wiberg, Van Parys, Copenhaver, S. Martin, McCord), never Bertsimas.

#### B5.5 Simulated annealing: a sceptical verdict in 1993, a working tool later {HS, RO, ML, DA} [practice · DB with Tsitsiklis, then group · P]

- **1993 review** (Statistical Science 8(1):10–15, DOI 10.1214/ss/1177011077):
  - theory gives no rigorous justification, even for decreasing cooling schedules (p. 13);
  - practice is mixed in Johnson et al.'s experiments: graph partitioning beats Kernighan–Lin only sometimes; graph colouring is competitive but slower; on the TSP, SA consistently loses to Lin–Kernighan (p. 13);
  - conclusion: SA is general and easy to implement and can give good solutions without knowledge of the problem's structure, but more theoretical and experimental research is needed (p. 14, paraphrase).
- **Later use**:
  - robust optimization with SA (Bertsimas and Nohadani, Journal of Global Optimization, online 2009, DOI 10.1007/s10898-009-9496-x; metadata only);
  - DELPHI offers `annealing` as an optimizer next to `tnc` and `trust-constr` (README; a commit of 2020-09-16 compares annealing with TNC);
  - SA for optimal trees (2023 thesis and manuscript, B4.5).
- [inferred] A heuristic judged theoretically unjustified in 1993 became a working tool once the goal was good solutions fast for hard formulations.

### Layers 2 and 3 (B2–3). Where problems came from (traces)

- **Partner systems as problem sources** {AP, DA, RO, IO} [practice · P; full texts of the applied papers not read]:
  - GMO portfolio construction (Interfaces 29(1):49–66, 1999, DOI 10.1287/inte.29.1.49; Edelman finalist 1998);
  - D2Hawkeye claims data (2008); ISO New England (2013); the media conglomerate (predictive-to-prescriptive);
  - Boston Public Schools (PNAS 2019; INFORMS Journal on Applied Analytics 50(1):37–49, 2020, DOI 10.1287/inte.2019.1015; Edelman finalist 2019);
  - OCP (INFORMS Journal on Applied Analytics 52(1):90–107, 2022, DOI 10.1287/inte.2021.1111; finalist 2021);
  - Janssen (2023; finalist 2022);
  - lung-transplant allocation (53(5):350–358, 2023, DOI 10.1287/inte.2023.0036);
  - Hartford HealthCare (54(6):553–574, 2024, DOI 10.1287/inte.2023.0071; 56(3):224–242, 2026, DOI 10.1287/inte.2024.0170).
  - [inferred] Each large deployment gets its own write-up in the INFORMS applied journal, besides the methodological papers.
- **A personal trigger** [stated · DB · P]: on his Life Stories page, after his father's cancer and three family deaths in 2009, "this experience led me to initiate a research program in personalized medicine". The papers that follow appear on the old homepage's Health Care list: "An Analytics Approach to Designing Combination Chemotherapy Regimens for Cancer" (Management Science, 2016) and "Personalized Diabetes Management Using Electronic Medical Records" (Diabetes Care 40:210–217, 2017). Note 02 records this as R16.
- **A student's preprint absorbed**: the predictive-to-prescriptive v1 was Kallus's alone; after the withdrawal it returned as a joint paper (B5.4). [practice]
- **Stalled topics retried with a later student** [inferred from titles and dates]:
  - In 2008–2009 the old homepage lists two manuscripts with A. Fertis, "Robust Logistic Regression" and "On the Equivalence of Robust Optimization and Regularization in Statistics", both "submitted to Operations Research"; no journal version was found.
  - The equivalence theme was published later with M. Copenhaver ("Characterization of the equivalence of robustification and regularization in linear and matrix regression", EJOR 2018, DOI 10.1016/j.ejor.2017.03.051).
  - Robust classification was published with J. Dunn, C. Pawlowski and Y. Zhuo ("Robust Classification", INFORMS Journal on Optimization 1(1):2–34, 2019, DOI 10.1287/ijoo.2018.0001).
- **Funding and topics** [stated · DB · P; 2014 oral history, p. 7]: students often split their time between the dissertation topic and a funded company topic ("Very often, 50% of my students work on the topic of their research"). A company project on HR optimization was run with a subgroup (p. 13). [inferred] The DELPHI partner branch and the Hartford papers are consistent with this arrangement.

### Layer 6 (B6). How results are reported

- **Title templates** (CV journal list; 330 of 340 numbered entries parsed; my count):
  - "… an optimization approach": 15;
  - "… a machine learning approach": 6;
  - "From X to Y": 7;
  - "The Price of …": 2 in print (robustness 2004; fairness 2011, DOI 10.1287/opre.1100.0865), plus 2 manuscripts ("The Price of Interpretability", arXiv:1907.03419; "The price of flexibility", CV #344);
  - "robust" appears in 49 titles and "interpretable" in 12.
- **Headline numbers in abstracts**: 800 billion (optimal classification trees), $5 million and 50 buses (PNAS), 88% (predictive-to-prescriptive), 1–2% and 3–5% over CART (optimal classification trees). [practice]
- **Public lists of manuscripts marked as submitted to a named journal, kept for decades** [practice · DB · P]: the old papers page (last modified 2019-03-14) and the CV (created 2025-12-31; 64 entries, #341–#404). Both lists lag behind the record:
  - "Robust Queueing Theory" (Operations Research 2015, DOI 10.1287/opre.2015.1367) is still "Submitted to Operations Research, 2014" on the 2019 page;
  - "A new perspective on low-rank optimization" (2023) is still "submitted" in the 2025 CV;
  - the CV carries two titles twice (#367 and #375; #376 and #382).
- **Venue choices** (traces):
  - the OR Forum section for perspective pieces (2015, 2016);
  - a Statistical Science discussion package (2020);
  - the INFORMS Journal on Optimization, which he edited (CV: Editor in Chief 2017–2024), carries two of his group's papers in volume 1 (Robust Classification; Optimal Prescriptive Trees, 1(2):164–183, 2019, DOI 10.1287/ijoo.2018.0005); handling-editor arrangements are not visible in what I read;
  - medRxiv and Research Square for medical work (THEMIS 2022, DOI 10.1101/2022.04.09.22273656; R.O.A.D. 2025, DOI 10.21203/rs.3.rs-5576146/v1);
  - top-tier targets in the CV: M3H "submitted to Nature, 2024" (#385), and three manuscripts submitted to "Nature Digital Medicine" in 2025 (#391, #400, #401).
- **Books through his own press**: Dynamic Ideas (founded 1998, CV) publishes *The Analytics Edge* (2016), *Machine Learning under a Modern Optimization Lens* (2019), *Robust and Adaptive Optimization* (2022), *Queueing Theory* (2022), *The Analytics Edge in Healthcare* (2025) and *Optimization over Integers* (2005). The LP book appeared with Athena Scientific (1997) and is now also sold by Dynamic Ideas. The Interpretable AI documentation cites the 2019 book, not a refereed paper, as the source of Optimal Regression Trees. [practice]

### Layer 7 (B7). Organisation visible in the artefacts

- **Division of labour in the contribution statements** [practice · P]:
  - PNAS 2019: "D.B., A.D., and S.M. designed research"; the two students performed the research and analysed the data; "A.D. and S.M. wrote the paper"; the corresponding author is S. Martin.
  - DELPHI preprint (21 authors, nearly all ORC students): DB is among those who designed the research and wrote the paper.
- **Students hold the code and the preprints**: no DB commits in DELPHI; the repositories belong to students and postdocs; co-authors submit the arXiv versions (B5.4).
- **Mobilization at scale**: the 21-author DELPHI preprint (spring 2020) and 380 commits in four months.
- **Companies inside the research loop** [practice · P]:
  - D2Hawkeye: DB on the board; it supplied the data and two co-authors (2008).
  - Dynamic Ideas: a committer handle in DELPHI; it publishes his books.
  - Interpretable AI: its software is research infrastructure (mlopt's interface to Optimal Trees; *The Voice of Optimization* §4).
  - Benefits Science: the DELPHI preprint lists a co-author affiliated with Benefits Science Technologies; the CV lists DB as co-founder of Benefits Science, LLC (2011–2023). The preprint states: "No author has any competing interest to declare."
  - These are recorded as facts. Disclosure norms differ by journal and era, and no judgment is made here.
- **Scale** (CV; OpenAlex):
  - PhD completions: 21 (1990s), 20 (2000s), 31 (2010s), 34 (2020–2025), plus 14 current;
  - journal output per five years rises to about 111 CV entries for 2020–2024 (my parse);
  - median authors per article: 2, 2, 3 and 4 across the four eras;
  - DB is first author on 83–85% of his articles before 2020, which fits alphabetical ordering ("B" sorts early), and on 64% in 2020–2026, when middle (36 articles) and last (16) positions appear with medical and multi-team papers.
- **External prospective evaluation**: 114 weekly DELPHI submissions to the COVID-19 Forecast Hub (2020-04-27 to 2022-07-11).
- **Stated supervision** (2014 oral history, p. 13): weekly one-on-one meetings with every student and no whole-group meeting ("I meet with every one of my students, one on one"). No artefact found here tests this (note 04's domain).

---

## C. Failures, abandoned directions, rejections and corrections (consolidated)

### C.1 What happened to manuscripts listed as "submitted" or as working papers on the old homepage (page last modified 2019-03-14)

Method: Crossref works API, a title query with author Bertsimas, then a manual check of the best hits, and a second query under the published title where one was known. Titles often changed, so "none found" means that no version was found by title, not that none exists. [practice · P (metadata); the last column is my reading]

| Listed on the old homepage | Outcome found | Reading |
|---|---|---|
| Equitable and Efficient Coordination in Air traffic Flow Management (with Barnhart, Caramanis, Fearing), "submitted to Transportation Science, 2009" | Transportation Science 46(2):262–280, 2012, DOI 10.1287/trsc.1110.0393 | same journal; title shortened |
| A Proposal for Network Air Traffic Flow Management Incorporating Fairness and Airline Collaboration (with S. Gupta), "submitted to Operations Research, 2010" | "Fairness and Collaboration in Network Air Traffic Flow Management: An Optimization Approach", Transportation Science 2016, DOI 10.1287/trsc.2014.0567 | different journal; new title; 6 years |
| Flexibility, Fairness and Efficiency in Kidney Transplantation, "submitted to Operations Research, 2011" | "Fairness, Efficiency, and Flexibility in Organ Allocation for Kidney Transplantation", Operations Research 2013, DOI 10.1287/opre.1120.1138 | same journal; retitled |
| A general purpose local search algorithm for binary optimization (with Iancu, Katz), "submitted to INFORMS Journal of Computing, 2008" | "A New Local Search Algorithm for Binary Optimization", IJOC 2013, DOI 10.1287/ijoc.1110.0496 | same journal; 5 years |
| An accelerated first-order method for solving unconstrained polynomial optimization problems (with Freund, Sun), "submitted to Optimization Methods and Software, 2011" | "…for solving SOS relaxations of unconstrained polynomial optimization problems", OMS 2013, DOI 10.1080/10556788.2012.656114 | the title's scope narrowed |
| Data-Driven and Robust Optimization Approaches to Call Centers (with Doan), "revised and resubmitted to Manufacturing & Service Operations Management, November 2008" | "Robust and data-driven approaches to call centers", EJOR 2010, DOI 10.1016/j.ejor.2010.05.040 | a different journal after a revise-and-resubmit [inferred: not accepted at MSOM] |
| On the Power of Robust Solutions in Nonlinear Adjustable Optimization Problems (with Goyal), "submitted to Operations Research, 2011" | "On the approximability of adjustable robust convex optimization under uncertainty", Mathematical Methods of Operations Research 2012, DOI 10.1007/s00186-012-0405-6 | [inferred] the same work; a different journal |
| Robust Transient Multi-Server Queues and Feedforward Networks (with Bandi, Youssef), "Submitted to Operations Research, 2014" | "Robust transient analysis of multi-server queueing systems and feed-forward networks", Queueing Systems 2018, DOI 10.1007/s11134-017-9566-6 | a different journal |
| An Algorithmic Approach to Linear Regression (with King), "submitted to Operations Research" | OR Forum, Operations Research 64(1):2–16, 2016, DOI 10.1287/opre.2015.1436 | moved into the OR Forum |
| Optimal Bidding in Online Auctions (with Hawkins, Perakis), "to appear … December, 2002" | Journal of Revenue and Pricing Management 2009, DOI 10.1057/rpm.2008.49 | 7 years from "to appear" |
| Models for Minimax Stochastic Linear Optimization Problems with Risk Aversion, "submitted … April 2008" | Mathematics of Operations Research 2010, DOI 10.1287/moor.1100.0445 | same journal |
| On the Power of Robust Solutions in Two-Stage Stochastic and Adaptive Optimization Problems, "submitted … 2009" | Mathematics of Operations Research 2010, DOI 10.1287/moor.1090.0440 | same journal |
| Multistage Robust Mixed Integer Optimization with Adaptive Partitions (with Dunning), "Submitted to Operations Research, 2014" | Operations Research 2016, DOI 10.1287/opre.2016.1515 | same journal |
| Robust Queueing Theory, "Submitted to Operations Research, 2014" | Operations Research 2015, DOI 10.1287/opre.2015.1367 | same journal; still "submitted" on the 2019 page |
| A hybrid approach to beam angle optimization in IMRT, "submitted to Computers and Operations Research, 2012" | Computers & Operations Research 2013, DOI 10.1016/j.cor.2012.06.009 | same journal |
| Measuring Quality in Diabetes Care (2013) | SpringerPlus 2013, DOI 10.1186/2193-1801-2-226 | — |
| Characterization of the equivalence of robustification and regularization … (2014) | EJOR 2018, DOI 10.1016/j.ejor.2017.03.051 | 4 years |
| An Analysis of the Guaranteed Withdrawal Benefits for Life Option (with Shah), "submitted to Journal of Insurance, 2008" | SSRN only, DOI 10.2139/ssrn.1312727 | no journal version found |
| **No version found by title**: An Optimization Approach to Credit Risk (2002); Robust Discrete Optimization under Ellipsoidal Uncertainty Sets (with Sim, April 2004); Joint network pricing and resource allocation (2004); Bounds on Some Contingent Claims with Non-Convex Payoff (ORC technical report 2007); No-arbitrage bounds on American put options (2008); Robust Logistic Regression (2008); On the Equivalence of Robust Optimization and Regularization in Statistics (2009); An Adaptive Local Search Algorithm for Solving Mixed Integer Optimization Problems (2009); The Generalized Restless Bandit Problem (2011); Data-driven learning in dynamic pricing using adaptive optimization (with Vayanos, "submitted to Operations Research, 2014"; the 2025 CV lists it as "submitted to Mathematical Programming, 2015"); The Trimmed Lasso (arXiv only, see C.2); four "Earlier Papers" (approximate dynamic programming for facility location; a linear-optimization approach to the Lovász local lemma; two with R. Weismantel on cutting planes and on duality for 0/1 integer programming) | — | [inferred] abandoned, absorbed into books, or circulated as working papers. Dynamic Ideas describes *Optimization over Integers* (with Weismantel, 2005) as treating cutting-plane and duality theory from a geometric viewpoint, which overlaps the two Weismantel manuscripts; the overlap is topical only |

Summary: of 34 old-homepage entries checked, 17 have a journal version (11 in the journal named on the page, counting the OR Forum section and the revenue-management journal; 4 in a different journal; 2 with no journal named), 1 is SSRN-only, 15 have no version found, and 1 is unresolved (an order-statistics manuscript of 2004 that may or may not be the 2006 PEIS paper listed separately on the same page).

### C.2 The CV's "Papers submitted for publication" (CV of 2025-12-31, entries #341–#404)

- 64 entries with 62 distinct titles. I checked all of them in Crossref and 33 in arXiv.
- **Journal versions found** for 4 titles:
  - #357, Mathematical Programming 2023;
  - #376 = #382, IJOC 2026;
  - #383, retitled, in *Variance* 2026, DOI 10.66573/001c.167995, against the CV's target "MSOM";
  - #387, Machine Learning 2026, DOI 10.1007/s10994-026-07022-0.
- **Preprint servers**: #363 (medRxiv), #391 (Research Square).
- **arXiv only**: #348 (arXiv:1904.11637, v1 only), #349 (Trimmed Lasso, arXiv:1708.04527, v1 only; also "submitted to IEEE Transactions on Information Theory" on the 2019 page), #352 (arXiv:1907.03419), #361 (arXiv:2303.06515), #368 (arXiv:2303.12285), #370 (arXiv:2305.17299), #373 (arXiv:2307.12405, v2 updated 2026-05-17), #378 (arXiv:2311.06960).
- **Stale**: the nine titles dated 2015–2017 (#341–#349) have no journal version found by title search.
- [inferred] Read with K7: the list mixes live, stalled and already-published manuscripts, so it is neither a pipeline nor a rejection log.

### C.3 Other failures and abandoned lines

- The MIO formulation of optimal trees was superseded by local search, then by simulated annealing (B4.5).
- DELPHI: continuous retraining, discrete-jump and arctan-jump variants were discarded, along with second-wave analyses (B4.7).
- JuMPeR (robust-optimization modelling layer) has had no activity since 2019, three years after its author's 2016 thesis (CV #59).
- Boston start times: approved by the school committee in December 2017 but not implemented (PNAS 2019).
- The predictive-to-prescriptive v2 was withdrawn for an error (B5.2).
- The 1996 fluid-network stability paper was corrected (B5.2).
- **Lead only, not verified**: a web-search result lists an ICLR 2025 submission titled "Optimized Oversampling"; the CV lists a manuscript of that title (with Koukouvinos and Koulouras) as submitted to IEEE TKDE in 2023 (#379). The OpenReview page sits behind a browser-verification challenge that was not bypassed, so the authorship and the reviews are unverified.

---

## D. Process evidence by optimization domain (`team.json` codes)

| Code | What the artefacts show | Strength of evidence |
|---|---|---|
| LO | textbook errata sheet organized by printing (at least six), last updated 2021 [B003 p. 1] (corrected 2026-10-29; earlier "maintained for 24 years by printing"); NetLib PILOT4 used as a test case for an LP with uncertain coefficients (2004) | thin |
| IO | heuristic warm start, then MIO under a time limit, with certificates optional (best subset, optimal trees); the "why now" speed-up figure (B4.4); diagnosis of a non-scaling formulation by variable counts and a switch to local search (B4.5); BARON as the global-solver baseline in the cone-product paper (IJOC 2026) | strong |
| RO | the rival's test problems (2004); the operator's incumbent rule and real network as baseline (ISO-NE 2013); a modelling package written by a student (JuMPeR); a published discussion and closure (2014); stalled robust-statistics manuscripts later retried (C.1) | medium |
| CP | the low-rank optimization paper and its publisher correction (2023); MOSEK-based relaxations in the IJOC snapshot; moment and SDP papers known only from the publication list, with no process artefact read | thin |
| SD | the 1997 correction; DELPHI's epidemic model (an SEIR variant) as fast, operational modelling; the "ML approach" to fluid queueing and bandit control (2023–2026 manuscripts) | thin |
| ML | the full best-subset cycle: claim, critique, response paper, discussion (B5.3); an evaluation protocol with named baselines and versions; code release practice (B4.6); third-party reproduction (Sarwar–Sauk–Sahinidis) | strong |
| DA | version histories (predictive-to-prescriptive, Voice of Optimization, online MIO, OptiCL); DELPHI's order of work; external prospective scoring | strong |
| HS | the 1993 sceptical review, then later use of SA and local search as working tools (B5.5, B4.5) | medium |
| AP | partners' systems as problem sources; an applied write-up per deployment; one deployment publicly not implemented (Boston start times) | strong, but the applied papers were read from metadata only |

Hooks for the council (cross-team) [inferred]:
- ML/IO and the MINLP Team: Sahinidis's group discussed and partly reproduced the 2020 sparse-regression paper, and BARON (Sahinidis) is the baseline in the cone-product paper.
- RO: the Ben-Tal–Nemirovski test problems connect to the NLP and MINLP teams' robust-optimization interests.
- HS and the DFO Team: simulated annealing and local search used as working solvers.

---

## E. Stated (note 02) versus what the artefacts show (this note)

| Stated claim (02 id) | What the artefacts show | Verdict [inferred] |
|---|---|---|
| R12 / E1 / J2: results should come with a certificate (provable optimality, suboptimality gap); "certified to be optimal in minutes/hours" (book blurb) | Best subset: certificates reached in some runs, after the optimum was already found. Optimal trees: most results carry no certificate (p. 1062). The 2020 paper caps the exact method at 60 s. The company software trains by local search without certificates (B4.5) | **partly practised**: certificates are reported when cheap, and dropped at scale |
| R9: "why now" from solver speed-ups | used in at least four texts, recomputed each time (200 billion to 2 trillion) | **practised**, with drifting figures (K6) |
| R11: global or joint optimization beats greedy heuristics | the company default is local search with 100 restarts, and the greedy CART-like learner is the fallback | **in tension**: the practice is a better heuristic, not global optimization (K1) |
| R6: real problems and data lead | partner data and systems: D2Hawkeye, ISO-NE, a media conglomerate, Boston Public Schools, Janssen, Hartford | **practised** |
| E3: test on synthetic (known truth) and real data | best subset, optimal trees and the 2020 paper all do both | **practised**; the synthetic grids were set by the group until critics widened them (K5) |
| E4: judge feature selection by accuracy, false discovery and time | adopted in the 2020 response paper | **practised** from 2019 on |
| R5: building companies is the way to scale impact | Dynamic Ideas, Interpretable AI, Benefits Science and Holistic Hospital Optimization appear inside the research artefacts (B7) | **practised**; it also shapes code release (B4.6) |
| R2: doctoral students are the first priority; "they become close colleagues" | students write, code and post the work (B5.4, B7) | consistent; the artefacts show delegation of execution and writing |
| 02 C4: ML is linked to optimization, not to probability theory (2019) | the predictive-to-prescriptive paper proves asymptotic optimality "even when data is not iid" (v4 abstract); the CV lists Applied Probability among his principal interests; a queueing-theory book appeared in 2022 | **contradicted by practice** (K4) |
| 02 G7 / §4: no first-hand record of handling negative results or rejections | negative results printed in papers (B5.1); failed variants archived with labels (B4.7); one arXiv withdrawal; venue changes after "submitted to" and an R&R (C.1) | **filled by practice** here; rejections themselves remain invisible |

---

## F. Process patterns (candidates for Phase 2; all [inferred] from the evidence above)

1. **Heuristic first, exact second, certificate optional.** Run a fast heuristic (first-order method, CART, local search), feed it to the MIO as a warm start, set a time limit, and report the proof only if it arrives (B4.3, B4.5).
2. **The partner's live system is both the test instance and the baseline.** Report the method's runtime and cost against the partner's current rule, even when it is slower (B4.2).
3. **Criticism is answered with a new paper and a wider grid.** A new student, the critic's own evaluation frame (SNR range), released code, a partial concession and a recommendation that combines methods (B5.3).
4. **Failures stay visible but sit outside the abstract.** PILOT4, excluded datasets, missing certificates, a memory exception, start times not implemented, archived model variants (B5.1, B4.7).
5. **Re-derive the "why now" argument for each paper** from the latest solver and hardware data (B4.4).
6. **List stalled manuscripts for years, and retry the topic with the next student**; venue changes are common (C.1, C.2).
7. **Students own code, preprints and much of the writing; DB designs and frames.** Shown in contribution statements, commit logs and arXiv submitters (B7, B5.4).
8. **The research line continues into a company** (Interpretable AI, Hartford, Janssen), and the company's software then becomes research infrastructure (B4.5, B4.6, B7).

---

## Contradictions (kept, not reconciled)

- **K1. Are optimal trees solvable by MIO?**
  - Optimal classification trees (2017) states that the MIO methods are "practically solvable on real-world datasets with sizes in the 1000s" (abstract, p. 1039).
  - The same paper drops larger datasets as prohibitive (p. 1061), and most of its results lack certificates (p. 1062).
  - Dunn's thesis (2018), from the same group a year later: the MIO lower bound stayed at zero beyond depth 1 on a dataset of 1,372 points, and local search beat the MIO (pp. 47–56).
  - The company software trains by local search by default. The name "optimal" is kept throughout.
- **K2. Certificates, stated and practised.** The stated protocol promises certification in minutes or hours (02 E1, R12); the practice relies on time limits without certificates (B4.3, B4.5, B5.3).
- **K3. Simulated annealing.** In 1993, theory was judged inadequate and practical performance mixed (p. 13). From 2009 to 2023, SA was used for robust optimization, epidemic-model fitting and optimal trees.
- **K4. Optimization, not probability (02 C4).** The 2019 principle against the probabilistic asymptotics of the predictive-to-prescriptive paper, the 2022 queueing book and the CV's research interests.
- **K5. Test grids.** HTT report that the 2016 paper used SNRs of about 2–10, and the September 2017 follow-up used SNR = 20. The group's own grid widened to 0.05–6 only in the 2019 response paper.
- **K6. Speed-up figures.** 200 billion (2015), 450 billion (2015/16), 800 billion (2017), 2 trillion (2018), each built from versions and hardware available at the time (extends 02 C5).
- **K7. "Submitted" lists versus the publication record.** Published papers stay listed as "submitted" (2019 page; 2025 CV), titles are duplicated, and other manuscripts stay "submitted" for ten years. The lists cannot be read as a pipeline or as a rejection log, yet they are the only public trace of the stalled work.
- **K8. Claim strength before and after an error.** The predictive-to-prescriptive v1 abstract is sweeping ("Incredibly …"). v2 was withdrawn for a crucial error in Theorem 2.2. v3 and v4 return with narrower, conditioned claims and real data.
- **K9. Open code, but not full reproducibility.** The 2020 paper states that it released code for methods not publicly implemented. A discussant notes that only the critics also released their simulation scripts, and reproduced MCP numbers differ slightly (B4.6). This is a tension of scope, not of fact.

---

## Gaps (what could not be found or read)

1. **Rejoinders not read**: the BPV rejoinder (DOI 10.1214/20-STS701REJ; closed; no open copy found with one WebSearch) and HTT's rejoinder (Project Euclid returned no content to curl or WebFetch). How Bertsimas answered the four discussants is therefore unknown.
2. **IEEE items not read**: the 1997 TAC correction (what was wrong in the 1996 paper), and Y. Z. Li's 2014 discussion and the authors' closure (paywalled).
3. **OpenReview**: the API and pages returned a browser-verification challenge, which was not bypassed. Conference and TMLR submissions with public reviews may exist (search snippets list an ICLR 2025 "Optimized Oversampling" and TMLR items); none was read.
4. **No referee reports, decision letters or lab guide** were found. Rejections are visible only indirectly, as venue changes (C.1).
5. **Early era (1988–2000)**: there is no code and no experiment log. Only the 1993 review, the 1997 correction and the textbook errata were examined. The queueing, achievable-region, approximation-algorithm and probabilistic-analysis papers were not opened for process evidence.
6. **Domains CP and SD**: no moment-problem or SDP paper and no stochastic-network paper was read for its computational protocol.
7. **Applied write-ups** (Interfaces 1999; INFORMS Journal on Applied Analytics 2020–2026) were read as metadata only, so the deployment processes (what was implemented, what was abandoned) are known only for Boston Public Schools.
8. **Dunn's thesis**: only §2.3 was read. How the local-search method was validated across datasets in later chapters was not checked.
9. **Interpretable AI release notes** returned a 404, so the evolution of the training algorithm over versions is unknown.
10. **Full-text diffs not done**: the published 2020 version of the sparse high-dimensional regression paper was not compared with arXiv v1, and the predictive-to-prescriptive v3 was not compared with v4 beyond the abstracts.
11. **Talk recordings**: none were transcribed for oral accounts of how particular papers came about (see 02 G1). The 2014 oral history was used only for two supervision and funding statements.
12. **Author-position statistics** rely on OpenAlex disambiguation and were not hand-checked.

---

## Sources

Primary (P) unless marked S. "metadata" = bibliographic record only; full text not read.

1. Bertsimas, D. *Papers* (old homepage), last modified 2019-03-14, https://www.mit.edu/~dbertsim/papers.html — P
2. Bertsimas, D. *Life Stories* (old homepage), last modified 2017-09-08, https://www.mit.edu/~dbertsim/lifestories.html — P
3. Bertsimas, D. Homepage (home with "My Philosophy", published-papers, published-books, media), accessed 2026-10-28, https://dbertsim.mit.edu — P
4. Bertsimas, D. *Curriculum Vita*, PDF created 2025-12-31, linked from https://dbertsim.mit.edu (Dropbox) — P
5. Roth, G., McKersie, R. B. *Interview with Dimitris Bertsimas*, Sloan Oral History Project, 2014-10-24, https://hdl.handle.net/1721.3/199289 (transcript in `references/sources/talks/`) — P
6. Bertsimas, D., Tsitsiklis, J. "Simulated Annealing", *Statistical Science* 8(1):10–15, 1993, DOI 10.1214/ss/1177011077 (author scan) — P
7. Bertsimas, D., Gamarnik, D., Tsitsiklis, J. N. "Stability conditions for multiclass fluid queueing networks", *IEEE TAC* 41(11):1618–1631, 1996, DOI 10.1109/9.543999 (metadata) — P
8. Bertsimas, D., Gamarnik, D., Tsitsiklis, J. N. "Correction to 'Stability Conditions for Multiclass Fluid Queueing Networks'", *IEEE TAC* 42(1):128, 1997, DOI 10.1109/TAC.1997.553697 (metadata) — P
9. Bertsimas, D., Tsitsiklis, J. N. *Introduction to Linear Optimization*, Athena Scientific, 1997: publisher page and errata sheet (last updated 2021-07-05), http://www.athenasc.com/linoptbook.html — P
10. Bertsimas, D., Darnell, C., Soucy, R. "Portfolio Construction Through Mixed-Integer Programming at Grantham, Mayo, Van Otterloo and Company", *Interfaces* 29(1):49–66, 1999, DOI 10.1287/inte.29.1.49 (metadata) — P
11. Bertsimas, D., Sim, M. "The Price of Robustness", *Operations Research* 52(1):35–53, 2004, DOI 10.1287/opre.1030.0065 (author copy) — P
12. Bertsimas, D., Bjarnadóttir, M. V., Kane, M. A., Kryder, J. C., Pandey, R., Vempala, S., Wang, G. "Algorithmic Prediction of Health-Care Costs", *Operations Research* 56(6):1382–1392, 2008, DOI 10.1287/opre.1080.0619 (author copy) — P
13. Bertsimas, D., Nohadani, O. "Robust optimization with simulated annealing", *Journal of Global Optimization*, online 2009, DOI 10.1007/s10898-009-9496-x (metadata) — P
14. Bertsimas, D., Litvinov, E., Sun, X. A., Zhao, J., Zheng, T. "Adaptive Robust Optimization for the Security Constrained Unit Commitment Problem", *IEEE TPWRS* 28(1):52–63, 2013, DOI 10.1109/TPWRS.2012.2205021 (author copy) — P
15. Bertsimas, D., Litvinov, E., Sun, X. A., Zhao, J., Zheng, T. "Closure to the Discussion of …", *IEEE TPWRS* 29(2):996–997, 2014, DOI 10.1109/TPWRS.2014.2301352 (metadata) — P
16. Bertsimas, D., Brynjolfsson, E., Reichman, S., Silberholz, J. "OR Forum—Tenure Analytics: Models for Predicting Research Impact", *Operations Research* 63(6):1246–1261, 2015, DOI 10.1287/opre.2015.1447 (author copy; history and acknowledgment only) — P
17. Bertsimas, D., King, A. "OR Forum—An Algorithmic Approach to Linear Regression", *Operations Research* 64(1):2–16, 2016, DOI 10.1287/opre.2015.1436 (author copy) — P
18. Bertsimas, D., King, A., Mazumder, R. "Best subset selection via a modern optimization lens", *Annals of Statistics* 44(2):813–852, 2016, DOI 10.1214/15-AOS1388; arXiv:1507.03133v1 — P
19. Bertsimas, D., Dunn, J. "Optimal classification trees", *Machine Learning* 106(7):1039–1082, 2017, DOI 10.1007/s10994-017-5633-9 — P
20. Dunn, J. W. *Optimal Trees for Prediction and Prescription*, PhD thesis, MIT, 2018, https://hdl.handle.net/1721.1/119280 (§2.3 read) — P
21. Bertsimas, D., Van Parys, B. "Sparse high-dimensional regression: Exact scalable algorithms and phase transitions", *Annals of Statistics* 48(1), 2020, DOI 10.1214/18-AOS1804; arXiv:1709.10029v1 — P
22. Bertsimas, D., Pauphilet, J., Van Parys, B. "Sparse Regression: Scalable Algorithms and Empirical Performance", *Statistical Science* 35(4):555–578, 2020, DOI 10.1214/19-STS701; arXiv:1902.06547v2 — P
23. Bertsimas, D., Pauphilet, J., Van Parys, B. "Rejoinder: Sparse Regression: Scalable Algorithms and Empirical Performance", *Statistical Science* 35(4):623–624, 2020, DOI 10.1214/20-STS701REJ (not read) — P
24. Bertsimas, D., Kallus, N. "From Predictive to Prescriptive Analytics", *Management Science* 66(3):1025–1044, 2020, DOI 10.1287/mnsc.2018.3253; arXiv:1402.5481 v1–v4 (abstract pages; v1 and v4 PDFs) — P
25. Bertsimas, D., Delarue, A., Martin, S. "Optimizing schools' start time and bus routes", *PNAS* 116(13):5943–5948, 2019, DOI 10.1073/pnas.1811462116 (PMC full text) — P
26. Bertsimas, D., Delarue, A., Eger, W., Hanlon, J., Martin, S. "Bus Routing Optimization Helps Boston Public Schools Design Better Policies", *INFORMS J. Applied Analytics* 50(1):37–49, 2020, DOI 10.1287/inte.2019.1015 (metadata) — P
27. Becker, T., Bertsimas, D., et al. "Toward Global Food Security: Transforming OCP Through Analytics", *INFORMS J. Applied Analytics* 52(1):90–107, 2022, DOI 10.1287/inte.2021.1111 (metadata) — P
28. Bertsimas, D., Li, M., Liu, X., Xu, J., Khan, N. "Data-Driven COVID-19 Vaccine Development for Janssen", *INFORMS J. Applied Analytics* 53(1):70–84, 2023, DOI 10.1287/inte.2022.1150 (metadata) — P
29. Papalexopoulos, T., Alcorn, J., Bertsimas, D., et al. "Applying Analytics to Design Lung Transplant Allocation Policy", *INFORMS J. Applied Analytics* 53(5):350–358, 2023, DOI 10.1287/inte.2023.0036 (metadata) — P
30. Na, L., Pauphilet, J., et al., Bertsimas, D. "Optimization Automates Emergency Department Nurse Scheduling at Hartford Hospital", *INFORMS J. Applied Analytics* 54(6):553–574, 2024, DOI 10.1287/inte.2023.0071 (metadata) — P
31. Na, L., Villalobos Carballo, K., et al. (incl. Bertsimas) "Patient Outcome Predictions Improve Operations at Hartford HealthCare", *INFORMS J. Applied Analytics* 56(3):224–242, 2026, DOI 10.1287/inte.2024.0170 (metadata) — P
32. Bertsimas, D., Boussioux, L., Cory-Wright, R., et al. (21 authors) "From predictions to prescriptions: A data-driven response to COVID-19", *Health Care Management Science* 24(2):253–272, 2021, DOI 10.1007/s10729-020-09542-0; medRxiv DOI 10.1101/2020.06.26.20141127 (preprint read) — P
33. COVIDAnalytics. `DELPHI` repository (README; 554 commits via the GitHub API), created 2020-04-06, https://github.com/COVIDAnalytics/DELPHI — P
34. COVID-19 Forecast Hub. `data-processed/CovidAnalytics-DELPHI` (metadata file; 114 forecast files, 2020-04-27 to 2022-07-11), https://github.com/reichlab/covid19-forecast-hub — P
35. Bertsimas, D., Stellato, B. "The voice of optimization", *Machine Learning* 110(2):249–277, 2021, DOI 10.1007/s10994-020-05893-5; arXiv:1812.09991 v1 and v3 — P
36. Bertsimas, D., Stellato, B. "Online Mixed-Integer Optimization in Milliseconds", *INFORMS J. Computing* 34(4):2229–2248, 2022, DOI 10.1287/ijoc.2022.1181; arXiv:1907.02206 v1 and v4 — P
37. Maragno, D., Wiberg, H., Bertsimas, D., Birbil, S. I., den Hertog, D., Fajemisin, A. "Mixed-Integer Optimization with Constraint Learning", *Operations Research* 73(2):1011–1028, 2025, DOI 10.1287/opre.2021.0707; arXiv:2111.04469 v1 and v3 — P
38. Soenksen, L. R., Ma, Y., Zeng, C., et al. (incl. Bertsimas) "Integrated multimodal artificial intelligence framework for healthcare applications", *npj Digital Medicine* 5:149, 2022, DOI 10.1038/s41746-022-00689-4 (metadata), with the `lrsoenksen/HAIM` README — P
39. Bertsimas, D., Cory-Wright, R., Pauphilet, J. "A new perspective on low-rank optimization", *Mathematical Programming* 202:47–92, 2023, DOI 10.1007/s10107-023-01933-9; Publisher Correction DOI 10.1007/s10107-023-01947-3 (metadata) — P
40. Bertsimas, D., de Moor, D., den Hertog, D., Koukouvinos, T., Zhen, J. "Cone Product Reformulation for Global Optimization", *INFORMS J. Computing*, 2026, DOI 10.1287/ijoc.2023.0345; code and data DOI 10.1287/ijoc.2023.0345.cd; README of https://github.com/INFORMSJoC/2023.0345 — P
41. Zeng, C., Bertsimas, D. "Catastrophe Insurance Pricing: An Adaptive Robust Optimization Approach", *Variance* 19, 2026, DOI 10.66573/001c.167995 (metadata) — P
42. Bertsimas, D., Kim, C. W., Niño-Mora, J. "Optimal Control of Fluid Restless Multi-armed Bandits: A Machine Learning Approach", *Machine Learning* 115(3), 2026, DOI 10.1007/s10994-026-07022-0 (metadata) — P
43. Bertsimas, D., Dunn, J., Pawlowski, C., Zhuo, Y. "Robust Classification", *INFORMS J. Optimization* 1(1):2–34, 2019, DOI 10.1287/ijoo.2018.0001 (metadata) — P
44. Bertsimas, D., Dunn, J., Mundru, N. "Optimal Prescriptive Trees", *INFORMS J. Optimization* 1(2):164–183, 2019, DOI 10.1287/ijoo.2018.0005 (metadata) — P
45. Bertsimas, D., Copenhaver, M. "Characterization of the equivalence of robustification and regularization in linear and matrix regression", *EJOR*, 2018, DOI 10.1016/j.ejor.2017.03.051 (metadata) — P
46. Pauphilet, J. `SubsetSelection.jl` repository (README, metadata, file list), https://github.com/jeanpauphilet/SubsetSelection.jl — P
47. Pauphilet, J. `SubsetSelectionCIO.jl` repository (README, metadata), https://github.com/jeanpauphilet/SubsetSelectionCIO.jl — P
48. Stellato, B. `mlopt` repository (README, file list), https://github.com/bstellato/mlopt — P
49. Wiberg, H. `OptiCL` repository (README, file list), https://github.com/hwiberg/OptiCL — P
50. Dunning, I. `JuMPeR.jl` repository (README, metadata), https://github.com/IainNZ/JuMPeR.jl — P
51. Delarue, A., Martin, S. `SchoolBusRouting` repository (metadata, file list), https://github.com/mitschoolbus/SchoolBusRouting — P
52. Interpretable AI. Documentation: OptimalTrees (home and "Citing OptimalTrees"), learner parameters, installation; accessed 2026-10-28, https://docs.interpretable.ai/stable/ — P (company)
53. Interpretable AI. Company homepage, accessed 2026-10-28, https://www.interpretable.ai/ — P (company)
54. Dynamic Ideas. Book pages for *Machine Learning under a Modern Optimization Lens*, *Optimization over Integers* and *Introduction to Linear Optimization*, accessed 2026-10-28, https://www.dynamic-ideas.com/books — P (his press)
55. Bertsimas, D., Copenhaver, M., Mazumder, R. "The Trimmed Lasso: Sparsity and Robustness", arXiv:1708.04527 (v1 only; record) — P
56. Bertsimas, D., Delarue, A., Jaillet, P., Martin, S. "The Price of Interpretability", arXiv:1907.03419 (v1 only; record) — P
57. Bertsimas, D., McCord, C. "From Predictions to Prescriptions in Multistage Optimization Problems", arXiv:1904.11637 (v1 only; record) — P
58. arXiv records of CV-listed manuscripts arXiv:2303.06515, 2303.12285, 2305.17299, 2307.12405 and 2311.06960 (version histories; titles in C.2) — P
59. Bertsimas, D., Gupta, V., Kallus, N. "Data-driven robust optimization", *Mathematical Programming* 167(2):235–292, 2018, DOI 10.1007/s10107-017-1125-8; arXiv:1401.0212 (version history only) — P
60. Bertsimas, D., Brown, D. B., Caramanis, C. "Theory and Applications of Robust Optimization", *SIAM Review* 53(3):464–501, 2011, DOI 10.1137/080734510; arXiv:1010.5445 (version history only) — P
61. Crossref works API, outcome checks for the manuscripts in C.1 and C.2 (published versions listed there with their DOIs), queried 2026-10-28 — P (metadata)
62. Crossref works API, corrections and discussion searches by author (B5.2, B5.3) and the INFORMS Journal on Applied Analytics and Interfaces lists (Layers 2–3), queried 2026-10-28 — P (metadata)
63. Hastie, T., Tibshirani, R., Tibshirani, R. J. "Extended Comparisons of Best Subset Selection, Forward Stepwise Selection, and the Lasso", arXiv:1707.08692v2, 2017; published as "Best Subset, Forward Stepwise or Lasso? …", *Statistical Science* 35(4):579–592, 2020, DOI 10.1214/19-STS733 — S [observed]
64. Sarwar, O., Sauk, B., Sahinidis, N. V. "A Discussion on Practical Considerations with Sparse Regression Methodologies", *Statistical Science* 35(4):593–601, 2020, DOI 10.1214/20-STS806; arXiv:2011.09362v2 — S [observed]
65. Mazumder, R. "Discussion of 'Best Subset, Forward Stepwise or Lasso? …'", *Statistical Science* 35(4):602–608, 2020, DOI 10.1214/20-STS807 (metadata) — S
66. George, E. I. "Modern Variable Selection in Action: Comment on the Papers by HTT and BPV", *Statistical Science* 35(4):609–613, 2020, DOI 10.1214/20-STS808 (metadata) — S
67. Chen, Y., Taeb, A., Bühlmann, P. "A Look at Robustness and Stability of ℓ1- versus ℓ0-Regularization: Discussion of Papers by Bertsimas et al. and Hastie et al.", *Statistical Science* 35(4):614–622, 2020, DOI 10.1214/20-STS809 (metadata) — S
68. Hastie, T., Tibshirani, R., Tibshirani, R. J. "Rejoinder: Best Subset, Forward Stepwise or Lasso? …", *Statistical Science* 35(4):625–626, 2020, DOI 10.1214/20-STS733REJ (not read) — S
69. Li, Y. Z. "Discussion of 'Adaptive Robust Optimization for the Security Constrained Unit Commitment Problem'", *IEEE TPWRS* 29(2):996, 2014, DOI 10.1109/TPWRS.2014.2301351 (metadata) — S
70. Tibshirani, R. J. `best-subset` repository (metadata; created 2017-01-15), https://github.com/ryantibs/best-subset — S [observed]
71. OpenAlex. Author A5025940525 (413 article records; author positions) and open-access locations of key DOIs, queried 2026-10-28, https://api.openalex.org — S
72. WebSearch result listing of OpenReview items naming Bertsimas (leads only; pages not readable), 2026-10-28 — S

# Daniel P. Robinson: stated research methodology (research agent 02)

| Field | Value |
|---|---|
| Researcher | Daniel P. Robinson (Lehigh University ISE since July 2019; Johns Hopkins Applied Mathematics and Statistics 2011-2019; PhD Mathematics, UC San Diego 2007; research assistant to N. I. M. Gould at Oxford/RAL 2007-2010 and to J. Nocedal at Northwestern 2010-2011) |
| Dimension | 02: stated methodology (what he says research and algorithm design should be) |
| Research date | 2026-10-16 |
| Sources consulted | 43 (36 primary: his homepage and its subpages, live and archived; one sole-authored discussion paper; 3 talk abstracts and a speaker bio; 2 PI-written NSF abstracts; 12 papers or technical reports, 9 of them read at least in their introduction; the joint Curtis-Robinson book site. 7 secondary: Lehigh news articles quoting him, the JHU faculty page, co-PI grant abstracts, the Izmailov-Solodov rejoinder, Crossref metadata) |
| WebSearch calls used | 4 (of 5 allowed) |
| User-supplied material | none. `references/sources/{papers,talks,essays,software}` held only `.gitkeep`; `private/` was not opened |
| Language | English (per team.json) |

**What was read and how.** Robinson has not published a "how I do research" essay, blog, interview or methodology lecture that I could find (4 WebSearches, the homepage and all its subpages, Lehigh and JHU pages). I found no video of any talk, so no transcript was saved under `sources/talks/`. His stated method therefore comes from five kinds of source:
- (a) **One sole-authored opinion piece**: his invited discussion of Izmailov and Solodov's "Critical Lagrange multipliers" paper (*TOP* 23(1), 2015, pp. 43-47; full text read). It is the richest single source. In it he writes in the first person about what makes an algorithm acceptable, and he openly disagrees with other researchers.
- (b) **The prose on his homepage** (who he is, current research, teaching, software, service) and his archived talk list (88 entries, 2000-2019).
- (c) **Grant abstracts where he is PI** (NSF DMS-1217153, 2012; NSF DMS-2012243, 2020). The PI writes these and NSF edits them.
- (d) **Talk abstracts and a speaker bio**: University of Florida, Feb 2019; ICCOPT 2025; the ICCOPT 2025 bio.
- (e) **Stances in the introductions and conclusions of co-authored papers**: Gould & Robinson RAL reports 2009; Gill & Robinson 2010/2012; Curtis & Robinson 2017-2018; Berahas, Curtis, Robinson & Zhou 2020.

Press quotes (Lehigh news, 2019-2024) give his words through a journalist.

**Tags.** [stated] = he said or wrote it. [practice] = what he did (papers, code, web pages), recorded here only to anchor a stated claim; agent 03 checks practice. [observed] = what others wrote about him or in reply to him. [inferred] = my inference, not to be quoted as his view. Every item is also marked primary or secondary. Items from co-authored papers are marked **(co-authored)**, because the stance may belong to the co-authors as much as to Robinson: often Curtis, whose own 02 file in this team overlaps on several of these items, and in the 2009-2012 work Gould or Gill.

---

## 0. Beliefs he repeats (3 or more independent occasions)

| # | Belief (short form) | Occasions (date: source) | Count |
|---|---|---|---|
| R1 | Research in his field means to **design, analyze, implement (and validate)** algorithms. All four parts belong to the job | 2012: NSF DMS-1217153 abstract; 2020: NSF DMS-2012243 abstract; ~2021-25: ICCOPT speaker bio; undated (read 2026-10-16): homepage "What I do"; current-research page (written 2021 or later). Department pages repeat it in the third person (2019 news; Lehigh profile) | 5 own (+2 third-party) |
| R2 | An algorithm must be **both practically and theoretically sound**. A theory that does not justify the method people actually run is not enough | 2009: RAL-TR-2009-001 abstract (co-authored); 2009: RAL-TR-2009-002 abstract (co-authored); 2015: TOP comment p. 44 (sole); 2019: UF talk abstract (sole); 2020: NSF DMS-2012243 | 5 |
| R3 | **Convergence theory must not rest on assumptions that a practical solver cannot guarantee or verify**: global minimizers of nonconvex subproblems, a "correct" local solution, exact subproblem solves, a known Lipschitz constant, a pre-chosen ε | 2009: RAL-TR-2009-001 p. 4 (co-authored); 2015: TOP comment pp. 45-47 (sole); 2018: *Optim. Lett.* "Concise complexity analyses" p. 9 (co-authored) | 3 |
| R4 | **A design feature is worth it only if computation shows consistent gains**. Convergence results alone do not show benefit, and a popular technique may in fact hurt | 2010/2012: Gill & Robinson COAP p. 16 (co-authored); 2015: TOP comment p. 47 criteria (iv)-(v) (sole); 2017/2018: Curtis & Robinson *Math. Program.* pp. 2-4 (co-authored); 2019: UF talk abstract claim (i) (sole); 2018 talk title "A Positive Perspective on Negative Curvature" given 3 times | 4 (+talk titles) |
| R5 | **Numerical results are presented as "preliminary"**: evidence of potential, explicitly not a definitive head-to-head comparison | 2009: RAL-TR-2009-002 pp. 35-36 (co-authored); 2010/2012: Gill & Robinson COAP pp. 4, 16 and conclusion (co-authored); 2025: ICCOPT talk abstract (sole) | 3 |
| R6 | **Problems come from applications**: computer vision, healthcare, data science, energy, defense | 2012: NSF DMS-1217153; 2019: Lehigh welcome quote; ~2021-25: ICCOPT bio; current-research page; homepage; 2022: MS Data Science quotes; 2024: ONR quote | 7 |
| R7 | **Why now**: new nonconvex and data-science models have outgrown existing algorithms, so new methods with guarantees are needed | 2017/2018: Curtis & Robinson p. 2 (co-authored); 2019: UF abstract; 2020: NSF DMS-2012243; current-research page (2021 or later); 2022: MS Data Science quote | 5 |
| R8 | **Algorithms should be released as freely available software** | 2009: RAL-TR-2009-002 p. 36 ("(soon to be) freely available ... S2QP", co-authored); 2012: NSF DMS-1217153 ("freely available software"); homepage Software page "Coming soon: PYPDAS, Galahad, Farsa, 2PHASE, ncBQP" (archived 2020-12-02, unchanged 2024-07-23 and on 2026-10-16) | 3 (see Contradictions C4) |
| R9 | **Exploit structure through subspace or active-set "phases", decomposition and second-order reduced-space steps**; they beat plain first-order methods | 2011: talk "Using Active-set Phases to Accelerate Algorithms" (Lehigh, JHU); 2012: NSF DMS-1217153 ("acceleration phase"); 2016: talk "Adaptive Subspace Methods for Optimization"; 2019: talks "Second-Order Reduced-Space Methods for Sparse Optimization", "Reduced-Space Optimization for Problems with Group Sparsity"; 2020: NSF DMS-2012243; current-research page (FaRSA-Group) | 3 prose + 4 titles |

Claims made only once or twice appear in the layers below and are marked as single or double statements.

---

## 1. Research taste: what is worth doing, what a good result is

**1.1 "Practically and theoretically sound"** [stated, primary, sole] (R2)
- "As I believe that algorithms should be practically and theoretically sound, I will focus on the practical aspects of the globalization process." (Robinson, "Comments on: Critical Lagrange multipliers: what we currently know about them, how they spoil our lives, and what we can do about it", *TOP* 23(1):43-47, 2015, p. 44; DOI 10.1007/s11750-015-0371-2). This is the only place where he states the principle in his own name, outside a co-authored paper.
- Earlier, as the opening problem of his Oxford postdoc work (co-authored with Gould): "Although second derivative information may often be calculated, there is little practical theory that justifies exact-Hessian SQP methods." (Gould & Robinson, "A second derivative SQP method: global convergence", RAL-TR-2009-001, 2009-02-09, abstract p. 1; published as *SIAM J. Optim.* 20(4):2023-2048, 2010, DOI 10.1137/080744542).
- The companion report states the same value for software: "Although we established global convergence of the algorithm, we did not discuss certain aspects that are critical when developing software capable of solving general optimization problems." and "To be practical, however, these algorithms must be guaranteed to avoid the so-called Maratos effect." (Gould & Robinson, "A second derivative SQP method: local convergence", RAL-TR-2009-002, 2009-02-09, abstract; published as "... local convergence and practical issues", *SIAM J. Optim.* 20(4):2049-2079, 2010, DOI 10.1137/080744554) (co-authored).
- 2020 grant (PI): "The algorithms will be designed to be broadly applicable, scalable, and efficient, and will be shown to possess strong convergence rate guarantees." (NSF DMS-2012243 abstract, award start 2020-07-15) [stated, primary; PI-written, NSF-edited].

**1.2 An explicit checklist for a good method** [stated, primary, sole] (single statement)
- On globalizing stabilized SQP: "we seek methods with the following properties. (i) They are applicable to problems with both equality and inequality constraints. (ii) The methods are superlinearly convergent under weak assumptions. (iii) The methods are globally convergent under standard assumptions. (iv) The methods substantially outperform Newton-based methods on degenerate problems. (v) The methods are comparable to Newton-based methods on nondegenerate problems." He then names the ingredients he thinks any such method needs: "any method with the properties (i)-(v) must include strategies for: (a) the convexification of the subproblem; (b) the use of primal regularization; (c) the careful adjustment of the dual regularization parameter(s) when near and far from a solution; and (d) the use of inexact solutions of the subproblem." (*TOP* 2015, p. 47).
- On his own method: "I believe that the method proposed in Gill et al. (2013, 2014) comes the closest to satisfying these criteria, but I am sure that better methods are possible." (p. 47).
- [inferred] The checklist pairs theory demands (i)-(iii) with computational demands (iv)-(v), and (v) asks for no loss on easy problems, not only gains on hard ones. This is the most concrete statement of his taste in the record.

**1.3 Assumptions that cannot be checked are a defect, not a technicality** [stated, primary] (R3)
- 2009 (co-authored): "To our knowledge, all previous second-order SIQP methods assume that global minimizers of nonconvex subproblems are computed, which is not a realistic assumption in most cases." And on Fletcher's Sl1QP: "Unfortunately, the theoretical results of Fletcher's method requires the computation of the global minimizer of this (generally) nonconvex subproblem, which is known to be an NP-hard problem." [sic, "requires"] (RAL-TR-2009-001, p. 4).
- 2015 (sole): "The calculation of such special solutions, although critical to proving superlinear local convergence, cannot be guaranteed in practice. This fact leads to a difference of opinion among researchers." "I do not know of any result in this direction and, in fact, I do not believe it to be true (at least not provably so)." "I belong to the second group of researchers who believe that the assumption placed on the subproblem solutions is unsatisfactory and should be avoided if possible." (*TOP* 2015, pp. 45-46). And on why nobody has tested it: "To my knowledge, there has not been a study that attempts to verify that the "correct" subproblem solutions are computed, but this is probably because such a verification is generally not possible, wherein lies the problem." (p. 45).
- 2018 (co-authored), against a complexity-optimal trust-region variant: "there are clear costs to achieving this improved complexity. First, this algorithm requires knowledge of [the Lipschitz-type constant], which is not always known in practice. Second, the algorithm requires exact subproblem solutions. [...] Third, the algorithm is dependent on the choice of ε, meaning that the desired accuracy needs to be chosen in advance [...] This would likely lead to very poor behavior in practice compared to the strategies in Sections 2.3 and 2.4, which are much less conservative." (Curtis, Lubberts & Robinson, "Concise complexity analyses for trust region methods", arXiv:1802.07843v1, p. 9; *Optim. Lett.* 12:1713-1724, 2018, DOI 10.1007/s11590-018-1286-2). The bracketed words replace a symbol garbled in text extraction; the elisions are mine.

**1.4 Worst-case complexity characterizes anomalous rather than typical objectives** [stated, primary] (co-authored with Curtis; recorded in full in Curtis's 02 file)
- Contemporary analyses give "conservative characterizations based on anomalous objectives rather than on ones that are typically encountered in practice" (abstract). The Cartis-Gould-Toint tightness examples use "objective functions that one can argue are not representative of those encountered in regular practice" (§1). Static methods come out optimal "despite the fact that adaptive algorithms often perform better in practice" (§1.1). Source: Curtis & Robinson, "Regional complexity analysis of algorithms for nonconvex smooth optimization", arXiv:1802.01062v2 (2018-08-24), PDF pp. 2-4; *Math. Program.* 187:579-615 (2021), DOI 10.1007/s10107-020-01492-3.
- I found no sole-authored statement by Robinson on complexity theory. His share of this stance cannot be separated from Curtis's, who repeats it in at least six talks (see Curtis 02, R1).

**1.5 Concise, essential-components analysis is valued** [stated, primary] (single statement plus an award)
- "to the best of our knowledge, our presentation is the first to highlight the essential aspects needed to obtain a first-order complexity bound." (Curtis, Lubberts & Robinson 2018, arXiv p. 2) (co-authored).
- His speaker bio picks out this paper's award: "awarded a Best Paper Prize from Optimization Letters for his co-authored 2018 paper titled "Concise Complexity Analyses for Trust-Region Methods"" (ICCOPT 2025 speaker page, bio apparently written about 2021-22, since it says he "is co-organizing the 2022 International Conference on Continuous Optimization") [stated, primary; a third-person bio, presumably self-supplied, which I infer].

**1.6 Good applied results generalize the model to the real structure** [stated, primary] (current-research page, 2021 or later)
- Group sparsity: "Standard one-norm regularization techniques fail to achieve this goal. Also, integrating group information into the modeling process can improve both the interpretability and accuracy of the models obtained."
- Cost-sensitive prediction (sepsis): "In many real-world applications, it is too restrictive to assume that the user can specify their cost preferences in terms of feature costs. We address this issue by designing a new regularizer that faithfully reflects the structure of the underlying cost graph."
- Grant version: "their inadequacy for many modern machine learning and other types of problems has gradually been noticed by researchers. Since covariates often come in groups [...] one may wish to select them jointly instead of individually so that the models deployed make practical sense." (NSF DMS-2012243).

---

## 2. Problem choice: where problems come from, why now, when to stop

**2.1 Applications first** [stated] (R6)
- "This is an exciting time in my field because many modern applications in engineering, machine learning, and data science rely on optimization tools. I have been particularly interested in applications in Computer Vision." (homepage "What I do", undated, read 2026-10-16) [primary].
- "I plan to use my expertise in optimization to make impactful contributions to application areas in computer vision, healthcare, and beyond" (Lehigh news "ISE Welcomes Daniel Robinson as Associate Professor", 2019) [secondary, direct quote].
- 2012 grant: the tools are to serve "solving large-scale real-world problems related to energy transmission, trajectory optimization, optimal control, contact problems in computational mechanics, regularized machine learning problems, and various equilibrium problems" (NSF DMS-1217153) [primary, PI-written].
- "If you're interested in making an impact on people, I can't think of a better way to do it, broadly speaking, than through data science" (Lehigh news "Introducing Lehigh's new MS in Data Science program", 2022-02-15) [secondary, direct quote].
- "Machine learning and artificial intelligence will continue to play an increasing role in defense operations, such as for motion tracking systems and the operation of autonomous vehicles. We're thankful for this support from ONR for our work, which will provide foundational advances for long-term impact." (Lehigh news on the ONR award, 2024-09-12) [secondary, direct quote].

**2.2 Why now: the models changed, so the algorithms must** [stated] (R7)
- 2017 (co-authored): "There has been a recent surge of interest in solving nonconvex optimization problems. [...] It is now widely accepted that the design of new methods for solving nonconvex problems (at least locally) is sorely needed." (Curtis & Robinson, "Exploiting negative curvature in deterministic and stochastic optimization", arXiv:1703.00412v3, p. 2; *Math. Program.* 176:69-94, 2019, DOI 10.1007/s10107-018-1335-8).
- 2019 (sole): "The recent surge of interest in nonconvex modeling formulations (e.g., in deep learning, subspace clustering, and dictionary learning) emphasizes a need for a fresh look at nonconvex optimization algorithms with provable convergence guarantees." (talk abstract, "Effectively Using Negative Curvature in Optimization and Scalable Methods for Subspace Clustering", University of Florida mathematics; the talk list dates it February 2019) [primary].
- Current research (2021 or later): stochastic-objective, deterministic-constraint problems "are just now emerging in data science since large-scale decision-making applications demand the ability to solve problems with more realistic, nonlinear systems of equations/inequalities that impose constraints on the decision variables." [primary].
- 2022: "We've reached a point where getting more of the same kinds of data isn't necessarily as helpful as it used to be [...] For some applications and problems, even if we had much more data, we wouldn't see a significant benefit." The journalist paraphrases what follows: room for improvement lies in "developing new scientific approaches and tools to handle that data" (MS Data Science news, 2022) [secondary; the second part is the journalist's paraphrase].

**2.3 Pick the open globalization question once local theory exists** [stated, primary, sole] (single statement)
- "Izmailov and Solodov's discussion of the globalization of sSQP methods is brief because very few methods exist [...] Moreover, it is probably safe to say that the best way to globalize sSQP is not yet clear." "The key remaining question is how to best globalize such methods." (*TOP* 2015, pp. 44, 47).
- Talk titles from the same years point to the same theme: "Globalizing local methods" (ETH Zürich, May 2015); "Pushing the Limits of Sequential Quadratic Programming" (UMBC, March 2012) [stated, titles only; slides not public].

**2.4 Look for the weakness hidden by a success** [stated, primary, PI-written] (single statement)
- "Subspace phases have been used with great success to enhance basic algorithms [...] This success, however, has masked a prevailing weakness: all iterates generated must remain in the subspace. An acceleration phase has the added flexibility of selectively enlarging the subspace, when deemed necessary." (NSF DMS-1217153, 2012).
- The same move appears in 2017 (co-authored): first-order methods are used for nonconvex problems partly because "there has not been sufficient evidence showing benefits of integrating directions of negative curvature" (arXiv:1703.00412, p. 2). The paper treats that missing evidence as the problem to solve.

**2.5 When to stop or change direction** [no evidence]
- I found no statement on when to abandon a problem. Research stays empty here (see Gaps).

---

## 3. Idea generation

**3.1 Build the deterministic method first, with features that transfer to the stochastic setting** [stated, primary] (co-authored; 2 occasions)
- "our frameworks can, in theory, employ fixed stepsizes, which makes the methods readily translatable from deterministic to stochastic settings." (arXiv:1703.00412, abstract).
- "as a first step for considering this setting, we begin by proposing an algorithm for the deterministic setting that employs an adaptive stepsize selection scheme that makes use of Lipschitz constants [...] rather than a line search. Based on this algorithm for the deterministic setting, we propose our algorithm for the stochastic setting" (Berahas, Curtis, Robinson & Zhou, arXiv:2007.10525v1, p. 3; *SIAM J. Optim.* 31(2):1352-1379, 2021, DOI 10.1137/20M1354556).

**3.2 Find an equivalence between a hard subproblem and a tractable one** [stated, primary, sole]
- On the Gill-Kungurtsev-Robinson stabilized SQP method: "it capitalizes on the close relationship between the solution of the sSQP subproblem (2) and the solution of a certain BCQP subproblem whose objective approximates a primal-dual augmented Lagrangian function [...] By exploiting this relationship, procedures for convexifying the Hessian of the Lagrangian function are used to ensure global convergence. Computable conditions that allow for inexact subproblem solutions are used to establish an equivalence (locally) to sSQP." (*TOP* 2015, p. 46).

**3.3 Change the model the algorithm decides with** [stated, primary]
- "The aspect that distinguishes our approaches from ones previously proposed is that they make algorithmic decisions based on (estimated) upper-bounding models of the objective function." (arXiv:1703.00412, abstract) (co-authored). Sole-authored version: "A new strategy based on upper-bounding models allows directions of negative curvature to be used while improving performance in the deterministic setting" (UF abstract, 2019). Talk title: "Upper-Bounding Models for Optimization" (Lehigh DIMACS/TRIPODS/MOPTA, August 2018).

**3.4 Hybridize rival schools instead of picking one** [stated, primary] (co-authored, 2009)
- Gould and Robinson describe "a rivalry between essentially two classes of methods, which are commonly known as SEQP and SIQP methods", and present their algorithm as one that "may be considered an SIQP/SEQP hybrid" (RAL-TR-2009-001, pp. 3-4). In the companion report, on penalty-parameter updating: "We take the stance that both approaches should be available to the user." (RAL-TR-2009-002, p. 15).

**3.5 Regularization as a practical device as much as a theoretical one** [stated, primary, sole]
- "dual regularization may be viewed as a way of controlling the size of the dual variables and as a way of systematically regularizing the KKT matrix. [...] nonsingularity of K does not require ∇h(x_k) to have full row rank. In our experience, this property provides an important practical numerical advantage." (*TOP* 2015, p. 46; ∇h(x_k) is the constraint Jacobian, a symbol garbled in text extraction).

---

## 4. Experiments and execution

**4.1 Count the extra cost of the new ingredient** [stated, primary] (co-authored; single statement)
- "Computing directions of negative curvature carries an added cost that should be taken into consideration when comparing algorithm performance. We remark along with the results of our numerical experiments how these added costs can be worthwhile and/or marginal relative to the other per-iteration costs." (arXiv:1703.00412, p. 3).

**4.2 Test where the new method should win, and also where it should not lose** [stated, primary, sole]
- Criteria (iv)-(v) in 1.2. His report on his own results: "Our method performed substantially better compared to SNOPT [...] on problems that did not satisfy the linear independence constraint qualification (LICQ)" (*TOP* 2015, p. 46). He picks out the degenerate subset as the place where a stabilized method must prove itself.

**4.3 Baselines: the state-of-the-art method or the "typically used" one** [stated, primary]
- Current research page, about the stochastic SQP figures: "our method (Stochastic SQP) compared to the typically used stochastic subgradient method (Stochastic Subgradient). The box plots for feasibility error (top figure) and optimality error (bottom figure) created from our test problems show that our method consistently obtains better solution estimates in terms of feasibility and optimality over various noise levels".
- On FaRSA-Group: "compared to the state-of-the-art method gglasso. Each problem instance tested has a bar associated with it (a blue bar means that our method was more efficient and a red bar means gglasso was more efficient)."
- 2020 paper: "our deterministic algorithm is as reliable as a state-of-the-art line-search SQP method, although, as should be expected, it is sometimes less efficient than such a method that performs line searches." (arXiv:2007.10525, p. 3) (co-authored). He reports the expected loss alongside the win.
- [practice, recorded only as anchor] Test sets named in the texts read: CUTEr subsets (Gill & Robinson 2012) and the Hock-Schittkowski set (RAL-TR-2009-002). Agent 03 should check what was actually run.

**4.4 Preliminary numbers to justify further development** [stated, primary] (R5)
- "In the case of the SQP method, some preliminary numerical experiments are used to justify the further development of these methods. A complete theoretical treatment is currently under investigation." (Gill & Robinson, "A primal-dual augmented Lagrangian", *Comput. Optim. Appl.* 51:1-25, 2012, online 2010-08-03, p. 16; DOI 10.1007/s10589-010-9339-1) (co-authored).
- "We stress that these results are preliminary and that they are not intended to compare the (SIQP) approach with the (SEQP) approach, but rather to show that both approaches have the potential to be successful in practice." (RAL-TR-2009-002, p. 36) (co-authored).
- 2025 (sole): "I present an algorithm of the proximal-stochastic-gradient variety [...] Motivation for the algorithm is provided, along with a theoretical analysis and preliminary numerical results." (ICCOPT 2025, Parallel Session 3C, abstract of "A Proximal-Stochastic-Gradient Method for Regularized Equality Constrained Problems").

**4.5 Learning by implementation (teaching statement)** [stated, primary]
- "Group projects are a major aspect of this course, which serve as a way of learning through implementation and experimentation." (ISE 417 Nonlinear Optimization course page, undated, read 2026-10-16).

---

## 5. Judging results

**5.1 Mixed evidence stays mixed** [stated, primary, sole]
- "In practice, however, the evidence is mixed because all of the numerical experiments that I am aware of show that superlinear convergence is not achieved by sSQP on a nontrivial percentage of test problems. Of course, this somewhat disappointing performance may be caused by reasons other than the assumption on the subproblem solutions. The picture is not completely clear at this point." (*TOP* 2015, p. 45).
- On the field's long-run outlook: "It therefore seems that commonly used two-phase approaches, although successfully used on many problems, may never reliably produce superlinearly convergent iterates in practice, as predicted by the local convergence theory." (p. 45).

**5.2 Prefer computable or verifiable conditions** [stated, primary, sole]
- He writes that the stabilized SQP method "relaxes the termination conditions when certain verifiable conditions are satisfied" and that "Computable conditions that allow for inexact subproblem solutions are used to establish an equivalence (locally) to sSQP." (*TOP* 2015, p. 46). Read with 1.3, a result counts for him when its hypotheses can be checked while the method runs. [inferred link]

**5.3 A heuristic without theory may be published as a labelled "first step"** [stated, primary] (co-authored; see Contradictions C2)
- "Although we are unable to establish a convergence theory for this approach, we do illustrate some gain in performance in neural network training; see §3.3. We view this as a first step in the design of a practical algorithm for stochastic optimization that efficiently exploits negative curvature." (arXiv:1703.00412, p. 3). Later in the paper: "we do not claim convergence guarantees for this method. However, we believe that it is well motivated by our previous algorithms." (p. 21).

**5.4 State a weak assumption as weak** [stated, primary] (co-authored)
- "Our analysis makes Assumption 1, which means that it assumes that the iterates remain in an open convex set over which the objective and constraint function and derivative values are bounded. This is admittedly not ideal in a stochastic setting." The authors then argue that it "is more reasonable in a constrained setting, since the iterates are being driven to the deterministic feasible region." (arXiv:2007.10525, Remark 20, p. 14).

**5.5 Evidence for a claim of benefit must be consistent across problems** [stated, primary] (co-authored) (R4)
- "Importantly, none of the papers above (or any others to the best of our knowledge) have established consistent gains in computational performance as a result of using negative curvature directions." and "Although such approaches are reasonable, one might intuitively expect better performance if directions of negative curvature are exploited instead of avoided." (arXiv:1703.00412, p. 4).
- Sole-authored and sharper: "I present recent work that supports the following claims: (i) Commonly employed strategies for using negative curvature directions usually hurt algorithm performance" (UF abstract, 2019).

---

## 6. Writing and talks

**6.1 Numbered claims up front** [stated, primary, sole] [inferred as a style]
- His talk abstract numbers its theses "(i) ... (ii) ... (iii)" (UF 2019). His discussion paper numbers the desired properties (i)-(v) and the necessary strategies (a)-(d) (*TOP* 2015, p. 47). His 2012 grant numbers the two sources of "efficiency and reliability" as "(i) ... and (ii) ...". The Gill-Robinson abstract (2010) lists "The benefits of this approach include: (i) ... (ii) ... (iii)" (co-authored).

**6.2 Talk structure: motivation, then theory, then preliminary numerics** [stated, primary, sole] (ICCOPT 2025 abstract, quoted in 4.4).

**6.3 Titles that take a position** [stated, primary; titles only]
- "A Positive Perspective on Negative Curvature" (ISMP Bordeaux, July 2018; Univ. of Minnesota, Nov 2018; UNC Charlotte, Oct 2018). "Pushing the Limits of Sequential Quadratic Programming" (2012). "Globalizing local methods" (2015). "Scalable, Efficient, and Robust NLP Solvers" (ISMP 2015). Source: archived talks page (Wayback 2025-08-09). No slides are posted, so the content is not read.
- [practice] The list shows the same talk given many times in a row: "Effectively Using Negative Curvature in Optimization and Scalable Methods for Subspace Clustering" at 10 institutions between Dec 2018 and April 2019; "Scalable Optimization Algorithms for Large-scale Subspace Clustering" at 4 California universities in March 2017. The 2018-19 tour comes just before his July 2019 move to Lehigh (that this was a job-market tour is [inferred]).

**6.4 The book's stated writing approach** [observed, secondary] (co-authored with Curtis)
- "A conversational writing style is used throughout, with detailed proofs placed at the end of each chapter to allow readers to first grasp the core ideas before engaging with technical details." and "Written with both students and practitioners in mind, the book emphasizes practical relevance while maintaining a strong theoretical foundation." (Lehigh news, "Lehigh ISE faculty publish new book on practical optimization methods", 2026-01-22, about Curtis & Robinson, *Practical Nonconvex Nonsmooth Optimization*, SIAM MOS-SIAM Series, 2025, DOI 10.1137/1.9781611978599). The preface was **not read** (SIAM returned HTTP 403; see Gaps).

---

## 7. Research organization: time, students, collaboration, agenda

**7.1 Thrusts are tied to named funding and named collaborators** [stated, primary] [practice]
- The current-research page closes every thrust with its funder and collaborators: "This research is funded by the Office of Naval Research since 2021. My main collaborators are Albert Berahas, Frank E. Curtis, Minhan Li, Michael O'neill, and Baoyu Zhou." (stochastic constrained optimization). "This research continues to be funded by the USA National Science Foundation under grant number NSF-1704458 since 2017. My main collaborators are Tianyu Ding, Manolis Tsakiris, Rene Vidal, and Zhihui Zhu." (subspace clustering). "This research has been funded by the USA National Science Foundation under grant DMS-2012243 since 2020. My main collaborators are Frank E. Curtis and Yutong Dai." (group sparsity). The source spells it "O'neill".
- 2012 grant team size: "The principal investigator and his student consider the design, analysis, implementation, and validation of a new class of active-set algorithms" (NSF DMS-1217153).

**7.2 Long-term pairing with Curtis** [practice] [stated]
- They run a joint site: "This website shares information about our books and major software projects." (Sufficient Descent Labs, sufficientdescent.github.io, undated, read 2026-10-16). They wrote a joint book (2025) and hold a joint ONR grant (2024: "Stochastic Algorithms for Data-Driven Constrained Continuous Optimization"). Most post-2016 papers read here are co-authored with Curtis, so stances in layers 1-5 after 2016 are shared and should not be attributed to Robinson alone. [inferred caution]

**7.3 Students: research experience changes careers** [stated, secondary quote]
- "I've seen first-hand how getting involved in a research project can be life altering. It can make people fall in love with what they are doing and change the course of their career." (MS Data Science news, 2022; the quote is printed in two parts with "he says" between them, joined here).
- [practice] His talks page has its own section, "Undergraduate, Masters, PhD, and Postdoctoral Advisee Presentations", listing 18 advisee talks from 2013 to 2019 (Loh, Jiang, Mohy-ud-Din, Tappenden, Chen, Ding).

**7.4 Teaching is part of the job, not a distraction** [stated, primary]
- "I am passional [sic] about teaching. When I started at James Madison University as a freshman undergraduate student, I intended to become a teacher. As my interests in doing research advanced, my love for teaching remained steadfast. Spending significant time doing both research and teaching at Lehigh University is one of the many reasons that I enjoy being a university professor." (Teaching page, undated, read 2026-10-16).
- As masters program director: "The changes to the programs will ensure that our students continue to get a first-rate education in the modern world, while also providing the flexibility necessary for each student to design an individualized program to meet their needs" (Lehigh news, 2024-09-25) [secondary quote].
- On ethics in data-science training: "How do we understand and use data in a responsible way, and apply and improve algorithms to avoid bias?" (2022 news) [secondary quote].

**7.5 Service load** [practice, primary]
- He is associate editor for five journals: *Computational Optimization and Applications*, *J. Scientific Computing*, *Optimization Letters*, *Optimization Methods and Software*, *Mathematics of Operations Research* (homepage service page). He co-chaired ICCOPT 2022 and directs the ISE/MGSE masters programs. The 2026 news adds that he is "Area Coordinator for Optimization Online" [secondary]. His CV is "available upon request" only.

---

## 8. Failures, abandoned directions, corrections (what he admits)

- **A single-phase method harder than planned** [stated, primary, sole]: "Although the synchronization of these two aspects into a practical single-phase algorithm proved more difficult than anticipated, the global and local convergence results do not require an assumption about which subproblem solutions are computed." (*TOP* 2015, p. 46).
- **Theory missing at publication** [stated, primary, co-authored]: "A complete theoretical treatment is currently under investigation." (Gill & Robinson 2012, p. 16). "Although we are unable to establish a convergence theory for this approach" (Curtis & Robinson 2017/2018, p. 3).
- **A known gap in the field's evidence** [stated, primary, co-authored]: on SIQP methods for moderate-sized problems, "there is much empirical evidence that indicates that the additional cost per iteration is often off-set by substantially fewer function evaluations (similar evidence has yet to surface for large-sized problems)." (RAL-TR-2009-001, p. 4).
- **Published corrections to two co-authored papers** [practice, primary, from Curtis's errata page, read 2026-10-16]: a corrected Corollary 3.14(a) in Berahas, Curtis, Robinson & Zhou, *SIAM J. Optim.* 31(2):1352-1379 (2021), DOI 10.1137/20M1354556; and a corrected Lemma 3.19 in Curtis, Robinson & Samadi, "A trust region algorithm with a worst-case iteration complexity of O(ε^{-3/2}) for nonconvex optimization", *Math. Program.* 162:1-32 (2017), DOI 10.1007/s10107-016-1026-2. The second corrigendum says the published inequality "is correct, but not as tight as it could have been". The errata policy text ("My collaborators and I spend countless hours trying to ensure that all details in our published articles involve no mathematical errors...") is Curtis's. I found no errata page on Robinson's own site.
- **Software promised, not posted on the homepage**: see R8 and Contradictions C4.
- **Abandoned directions**: none stated. Several talk topics have no later papers that I traced (e.g. "ADMM, Accelerated-ADMM, and Continuous Dynamical Systems", 2018; "Two-phase Matrix Splitting Methods for BQP and LCP", 2011-12), but whether they were dropped is for agents 03 and 06. **Not established here.**

---

## 9. Era and resource context

- **2001-2007, UCSD PhD with P. E. Gill** (thesis "Primal-dual methods for nonlinear optimization", 2007; cited in the TOP reference list, not read). The primal-dual augmented Lagrangian work with Gill (2010/2012) comes from this period, in the SNOPT/SQP tradition: Fortran software, CUTEr tests, MATLAB prototypes ("Numerical results from a simple MATLAB implementation of pdSQP", Gill & Robinson 2012).
- **2007-2010, Oxford and RAL with N. I. M. Gould**, as a postdoc on EPSRC grants EP/E053351/1 and EP/F005369/1. The second-derivative SQP (S2QP) work was meant to become a GALAHAD Fortran 95 package. The concern with "software capable of solving general optimization problems" (RAL-TR-2009-002) dates from here.
- **2010-2011, Northwestern with J. Nocedal.** **2011-2019, JHU assistant professor**, with a small group (the 2012 NSF grant names "his student"). He was a founding member of JHU's MINDS and collaborated with Vidal on vision and ML (NSF IIS-1447822, 2014; IIS-1704458, 2017, as co-PI). The talks and abstracts from this period carry the "why now: nonconvex models" message (R7).
- **2019-, Lehigh associate professor**, later listed as professor (see C6). He works mainly with Curtis on stochastic constrained optimization, funded by ONR since 2021 and again in 2024. The compute context is ordinary: the 2017 neural-net experiment used Python 2.7.13 and TensorFlow on MNIST with mini-batches of 500 (arXiv:1703.00412, p. 21) [practice]. Nothing in the record suggests large-scale compute.

---

## Contradictions

- **C1. Robinson vs Izmailov and Solodov (2015): do assumptions on which subproblem solution is computed matter in practice?** [stated vs observed]
  - Robinson: the assumption is "unsatisfactory and should be avoided if possible". He adds that "all of the numerical experiments that I am aware of show that superlinear convergence is not achieved by sSQP on a nontrivial percentage of test problems", while granting that this "may be caused by reasons other than the assumption" (*TOP* 23:43-47, pp. 45-46).
  - Izmailov and Solodov: "localization conditions on solutions of subproblems are plain unavoidable, except if subproblems are equality-constrained or strongly convex", and "in our numerical experience, so far we have never encountered a case when superlinear convergence is lost because apparently "wrong" subproblem solutions are computed." They call the alternative, declaring that only methods with equality-constrained or strongly convex subproblems are "practical", "too extreme" (Rejoinder, *TOP* 23:48-52, 2015, pp. 50-51, DOI 10.1007/s11750-015-0373-0). Their summary of Robinson: "Daniel Robinson believes that when the subproblems of the algorithm may have multiple solutions, the restrictions in the theoretical analysis on the choice of "appropriate" solutions cannot be ignored from the practical perspective." (p. 50).
  - Kept unresolved. Each side cites its own numerical experience.
- **C2. "Practically and theoretically sound" (2015, sole) vs publishing an unanalyzed stochastic heuristic (2017-18, co-authored).** [inferred tension] In 2015 he asks that methods meet theory criteria (ii)-(iii) and reject unverifiable assumptions. In 2017-18 the negative-curvature paper presents a stochastic method with "we do not claim convergence guarantees for this method" and calls it "a first step". The two are compatible if theory is a goal rather than a gate, but the record does not say which he holds.
- **C3. Two-phase designs: promoted in 2011-2012, criticized in 2015.** [inferred tension; different problem classes] His talks of 2011-2012 promote "Two-phase Matrix Splitting Methods for BQP and LCP" (Argonne July 2011, JHU Sept 2011, Singapore Dec 2012), and "2PHASE" is still on his software list. In 2015 he concludes that globally convergent sSQP methods "will either be single-phase approaches or two-phase approaches in which the first-phase also uses some form of dual stabilization" (*TOP* p. 45). The 2015 critique is specific to sSQP: the risk of converging to critical multipliers, and the difficulty of deciding "when the global phase should transition to the local phase". It may not extend to BQP/LCP.
- **C4. "Freely available software" (2009, 2012) vs "Coming soon" (2020-2026).** [stated vs practice, practice only partly checked] He promised freely available code in 2009 (S2QP in GALAHAD, co-authored) and 2012 (NSF). His homepage software page has listed "PYPDAS, Galahad, Farsa, 2PHASE, ncBQP" as "Coming soon" from at least 2020-12-02 (Wayback) to 2026-10-16. I did not check GALAHAD, GitHub or co-authors' pages for released code; agent 03 should, before this is called a gap between word and practice.
- **C5. Promotional vs cautious registers.** [inferred] His web summaries use strong comparatives: DPCP "has routinely been shown to outperform other state-of-the-art algorithms"; "our method consistently obtains better solution estimates"; "FaRSA-Group significantly outperforms gglasso". His papers and his 2015 comment use hedged language ("The picture is not completely clear at this point"; "We stress that these results are preliminary"). Recorded as two registers, not reconciled.
- **C6 (factual, not methodological). Rank.** "Associate Professor" on his homepage, the ICCOPT 2025 speaker page and the 2024 ONR news; "Professor" on the Lehigh Rossin profile and in the 2026-01-22 book news. A promotion around 2025 is [inferred], not confirmed.
- Audit 2026-10-17: in C3 (and §8), the Singapore talk of December 2012 is titled "Two-phase Matrix Splitting Methods for Asymmetric and Symmetric LCP"; only the 2011 Argonne and JHU talks carry "...for BQP and LCP" (archived talks list, web.archive.org/web/20250809174202/https://coral.ise.lehigh.edu/danielprobinson/research/talks/).

---

## Gaps

- **No essay, blog, interview, oral history or "advice to PhD students" found** (4 WebSearches; homepage, Lehigh and JHU pages). The 2015 TOP discussion is the only sole-authored opinion text.
- **No video or transcript of any talk** (WebSearch over youtube.com, vimeo.com, bilibili.com found none). Nothing was saved to `sources/talks/`.
- **Talk slides**: none posted. The talks page (archived) stops in October 2019, and the live talks and publications pages show an unrendered `[bibtex ...]` shortcode (2026-10-16). Post-2019 talks are known only from conference programs (ICCOPT 2025).
- **Book preface and Chapter 1 "Opening" (pp. 1-4)** of *Practical Nonconvex Nonsmooth Optimization* (2025): **not read**. SIAM epubs and the bookstore returned HTTP 403. The front matter is DOI 10.1137/1.9781611978599.fm (pp. i-xxv). This is likely the best untapped source of his stated views on practice vs theory and on teaching.
- **PhD thesis** (UCSD 2007): not located online; **not read**.
- **Closed-access sole-authored paper**: Robinson, "Primal-dual active-set methods for large-scale optimization", *J. Optim. Theory Appl.* 166:137-171 (2015), DOI 10.1007/s10957-015-0708-x. **Not read** (no OA copy per Unpaywall). Also not read: Curtis, Jiang & Robinson, "An adaptive augmented Lagrangian method for large-scale constrained optimization", *Math. Program.* (2015 issue; online 2014), DOI 10.1007/s10107-014-0784-y. The published SIOPT versions of the two 2010 Gould-Robinson papers were not read; their RAL reports were.
- **Problem abandonment / when to stop** (layer 2): no statement found.
- **Supervision style, group meetings, how he picks students** (layer 7): only the 2022 quote. Left to agent 04.
- **His own words on worst-case complexity**: only co-authored with Curtis. His share could not be separated.
- **Methodological statements from the Vidal-era vision/ML work** (DPCP, subspace clustering): none found beyond the current-research page.
- Tool limits this run: DBLP returned a bot-check page, and the arXiv API returned "Rate exceeded" (I used arXiv's HTML search instead).

---

## Sources

1. Robinson, D. P. Homepage, "Who I am" / "What I do". https://coral.ise.lehigh.edu/danielprobinson/ (undated, read 2026-10-16). Primary.
2. Robinson, D. P. "Current Research" page. https://coral.ise.lehigh.edu/danielprobinson/research/current-research/ (2021 or later, read 2026-10-16). Primary.
3. Robinson, D. P. "Teaching" page. https://coral.ise.lehigh.edu/danielprobinson/teaching/ (undated). Primary.
4. Robinson, D. P. ISE 417, DSCI 311 and ISE 240 course pages. https://coral.ise.lehigh.edu/danielprobinson/teaching/ise-417/ (and /dsci-311/, /ise-240/) (undated). Primary.
5. Robinson, D. P. Service, Associate Editor and Director of Masters Programs pages. https://coral.ise.lehigh.edu/danielprobinson/service/ (undated). Primary.
6. Robinson, D. P. "Software" page. https://coral.ise.lehigh.edu/danielprobinson/software/ (live 2026-10-16; Wayback 2020-12-02 and 2024-07-23). Primary.
7. Robinson, D. P. "Talks" page, archived. http://web.archive.org/web/20250809174202/https://coral.ise.lehigh.edu/danielprobinson/research/talks/ (list covers 2000-2019). Primary.
8. Robinson, D. P. "Publications" page (live; shortcode unrendered). https://coral.ise.lehigh.edu/danielprobinson/research/publications/ (2026-10-16). Primary (empty).
9. JHU AMS faculty page "Daniel Robinson", archived 2018-06-19. https://engineering.jhu.edu/ams/faculty/daniel-robinson/. Secondary.
10. Lehigh Rossin College faculty profile "Daniel P. Robinson". https://engineering.lehigh.edu/faculty/daniel-p-robinson (read 2026-10-16). Secondary.
11. Lehigh news, "ISE Welcomes Daniel Robinson as Associate Professor" (2019). https://engineering.lehigh.edu/news/article/ise-welcomes-daniel-robinson-associate-professor. Secondary (direct quote).
12. Kackenmeister, K. "Introducing Lehigh's new MS in Data Science program", Lehigh news, 2022-02-15. https://engineering.lehigh.edu/news/article/introducing-lehighs-new-ms-data-science-program. Secondary (direct quotes).
13. Lehigh news, "Office of Naval Research awards more than $1M to Lehigh ISE", 2024-09-12. https://engineering.lehigh.edu/news/article/office-naval-research-awards-more-1m-lehigh-ise. Secondary (direct quote).
14. Lehigh news, "Lehigh ISE redesigns its master's programs, creating a novel program in optimization", 2024-09-25. https://engineering.lehigh.edu/news/article/lehigh-ise-redesigns-its-master-s-programs-creating-novel-program-optimization. Secondary (direct quote).
15. Lehigh news, "Lehigh ISE faculty publish new book on practical optimization methods", 2026-01-22. https://engineering.lehigh.edu/news/article/lehigh-ise-faculty-publish-new-book-practical-optimization-methods. Secondary.
16. Curtis, F. E. and Robinson, D. P. Sufficient Descent Labs site and book page. https://sufficientdescent.github.io/ and https://sufficientdescent.github.io/practicalnonconvexnonsmooth (undated). Primary.
17. Curtis, F. E. and Robinson, D. P. *Practical Nonconvex Nonsmooth Optimization*, SIAM MOS-SIAM Series on Optimization, 2025. DOI 10.1137/1.9781611978599 (Crossref metadata and chapter list only; text not read). Primary (metadata).
18. NSF award DMS-1217153, "New Active-Set Methods for Optimization and Complementarity Problems", PI D. Robinson (JHU), 2012-08-01. https://api.nsf.gov/services/v1/awards.json?id=1217153. Primary (PI-written abstract).
19. NSF award DMS-2012243, "An Accelerated Decomposition Framework for Structured Sparse Optimization", PI D. Robinson (Lehigh), 2020-07-15. https://api.nsf.gov/services/v1/awards.json?id=2012243. Primary (PI-written abstract).
20. NSF awards IIS-1447822 (2014), IIS-1704458 (2017) (PI R. Vidal) and 1736448 (2017) (PI E. Mallada), with Robinson as co-PI. NSF award API. Secondary (lead-PI abstracts; context only).
21. Robinson, D. P. "Comments on: Critical Lagrange multipliers: what we currently know about them, how they spoil our lives, and what we can do about it", *TOP* 23(1):43-47, 2015-02-27. DOI 10.1007/s11750-015-0371-2 (full text read). Primary.
22. Izmailov, A. F. and Solodov, M. V. "Rejoinder on: Critical Lagrange multipliers: ...", *TOP* 23(1):48-52, 2015. DOI 10.1007/s11750-015-0373-0 (full text read). Secondary (reply to Robinson).
23. Izmailov, A. F. and Solodov, M. V. "Critical Lagrange multipliers: what we currently know about them, how they spoil our lives, and what we can do about it", *TOP* 23(1):1-26, 2015. DOI 10.1007/s11750-015-0372-1 (metadata only; not read). Secondary.
24. Robinson, D. P. Talk abstract, "Effectively Using Negative Curvature in Optimization and Scalable Methods for Subspace Clustering", University of Florida (Feb 2019 per talk list). https://people.clas.ufl.edu/boyland/daniel-p-robinson/. Primary.
25. ICCOPT 2025 speaker page, "Daniel P. Robinson" (bio). https://iccopt2025usc.sched.com/speaker/daniel.p.robinson. Primary (presumably self-supplied, third person).
26. ICCOPT 2025, Parallel Session 3C, abstract of "A Proximal-Stochastic-Gradient Method for Regularized Equality Constrained Problems", 2025-07-21. https://iccopt2025usc.sched.com/event/1dqlY/parallel-sessions-3c-methods-for-large-scale-nonlinear-optimization-iii. Primary.
27. Gould, N. I. M. and Robinson, D. P. "A second derivative SQP method: global convergence", RAL-TR-2009-001, 2009-02-09. https://epubs.stfc.ac.uk/manifestation/6616/grRAL2009001.pdf; published *SIAM J. Optim.* 20(4):2023-2048, 2010, DOI 10.1137/080744542 (report intro read). Primary.
28. Gould, N. I. M. and Robinson, D. P. "A second derivative SQP method: local convergence", RAL-TR-2009-002, 2009-02-09. https://epubs.stfc.ac.uk/manifestation/6615/grRAL2009002.pdf; published as "... local convergence and practical issues", *SIAM J. Optim.* 20(4):2049-2079, 2010, DOI 10.1137/080744554 (report abstract, §3 stance, §5-6 read). Primary.
29. Gill, P. E. and Robinson, D. P. "A primal-dual augmented Lagrangian", *Comput. Optim. Appl.* 51(1):1-25, 2012 (online 2010-08-03). DOI 10.1007/s10589-010-9339-1 (open access; intro, §5 and conclusion read). Primary.
30. Curtis, F. E. and Robinson, D. P. "Exploiting negative curvature in deterministic and stochastic optimization", arXiv:1703.00412v3 (2018-04-04); *Math. Program.* 176:69-94, 2019, DOI 10.1007/s10107-018-1335-8 (intro and §3 read). Primary.
31. Curtis, F. E., Lubberts, Z. and Robinson, D. P. "Concise complexity analyses for trust region methods", arXiv:1802.07843v1 (2018-02-21); *Optim. Lett.* 12:1713-1724, 2018, DOI 10.1007/s11590-018-1286-2 (intro and §2.5 read). Primary.
32. Curtis, F. E. and Robinson, D. P. "Regional complexity analysis of algorithms for nonconvex smooth optimization", arXiv:1802.01062v2 (2018-08-24); *Math. Program.* 187:579-615, 2021, DOI 10.1007/s10107-020-01492-3 (abstract and §1 passages checked). Primary.
33. Berahas, A., Curtis, F. E., Robinson, D. P. and Zhou, B. "Sequential quadratic optimization for nonlinear equality constrained stochastic optimization", arXiv:2007.10525v1 (2020-07-20); *SIAM J. Optim.* 31(2):1352-1379, 2021, DOI 10.1137/20M1354556 (intro and Remark 20 read). Primary.
34. Curtis, F. E., Dai, Y. and Robinson, D. P. "A subspace acceleration method for minimization involving a group sparsity-inducing regularizer", arXiv:2007.14951; *SIAM J. Optim.* 32:545-572, 2022, DOI 10.1137/21M1411111 (keyword scan only). Primary.
35. Curtis, F. E., Robinson, D. P. and Zhou, B. "Sequential quadratic optimization for stochastic optimization with deterministic nonlinear inequality and equality constraints", arXiv:2302.14790; *SIAM J. Optim.* 34, 2024, DOI 10.1137/23M1556149 (intro scan only). Primary.
36. Dai, Y. and Robinson, D. P. "Inexact proximal-gradient methods with support identification", arXiv:2211.02214 (keyword scan only). Primary.
37. Robinson, D. P., Vidal, R. and You, C. "Basis pursuit and orthogonal matching pursuit for subspace-preserving recovery: theoretical analysis", arXiv:1912.13091 (keyword scan only). Primary.
38. Curtis, F. E., Robinson, D. P. and Zebiane, L. "Active-set identification in noisy and stochastic optimization", arXiv:2509.00888 (keyword scan only). Primary.
39. Curtis, F. E., Guo, L. and Robinson, D. P. "A local-linearly convergent algorithm for nonconvex equality-constrained optimization", arXiv:2608.12665 (2026-08-12; intro read, no methodological stance found). Primary.
40. Curtis, F. E. Errata page and corrigenda for Berahas-Curtis-Robinson-Zhou (2021) Corollary 3.14 and Curtis-Robinson-Samadi (2017) Lemma 3.19. https://coral.ise.lehigh.edu/frankecurtis/errata/ (read 2026-10-16); Curtis, Robinson & Samadi, *Math. Program.* 162:1-32, 2017, DOI 10.1007/s10107-016-1026-2. Primary (Curtis's page).
41. Curtis, F. E., Robinson, D. P., Royer, C. W. and Wright, S. J. "Trust-region Newton-CG with strong second-order complexity guarantees for nonconvex optimization", *SIAM J. Optim.* 31:518-544, 2021, DOI 10.1137/19M130563X (metadata only, via Crossref; not read). Primary (metadata).
42. Robinson, D. P. "Primal-dual active-set methods for large-scale optimization", *J. Optim. Theory Appl.* 166:137-171, 2015, DOI 10.1007/s10957-015-0708-x (metadata only; not read). Primary (metadata).
43. Crossref REST API records for the DOIs above and for the chapter list of DOI 10.1137/1.9781611978599 (queried 2026-10-16). Secondary (metadata).

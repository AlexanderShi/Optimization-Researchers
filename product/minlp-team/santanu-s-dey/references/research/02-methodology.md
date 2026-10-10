# Santanu S. Dey: stated research methodology (research agent 02)

| Field | Value |
|---|---|
| Researcher | Santanu S. Dey (Georgia Tech, H. Milton Stewart School of ISyE; Anderson-Interface Professor and director of doctoral recruiting and admissions; PhD Industrial Engineering Purdue 2007, MS IE Purdue 2003, BE Mechanical Engineering Mumbai University 2000; post-doc at CORE, UCLouvain; at Georgia Tech since 1 July 2009) |
| Dimension | 02: stated methodology (what he says research on mixed-integer and nonconvex optimization should be, and how he says he does it) |
| Research date | 2026-10-10 |
| Sources consulted | 85 (76 primary: his homepage and one syllabus, 36 public talk-slide decks 2005-2024, 7 recorded talks transcribed from auto-captions 2020-2025, 25 papers or preprints read in introduction/conclusion or abstract, 1 Optima review article, 5 NSF award abstracts; 9 secondary: the Optima discussion column, Georgia Tech news and profile pages, INFORMS prize pages, an MIT seminar bio) |
| WebSearch calls used | 2 (of 2 allowed) |
| User-supplied material | none. `references/sources/{papers,talks,essays,software}` held only `.gitkeep`; `private/` was not opened |
| Transcripts saved | 7 auto-caption transcripts under `references/sources/talks/` (see Sources, group C) |
| Language | English (per team.json) |

**What was read and how.** I found no essay, blog, interview, podcast or advice-to-students page in which Dey describes how he does research. His stated method therefore comes from five kinds of public source, all read in this run:
(a) the framing slides (motivation, "why do we care", "our questions", conclusions, open questions) of all 36 slide decks linked from his talks page, 2005 to 2024, text extracted with `pdftotext` (figures and spoken asides are missing; slide citations give the PDF page of the deck);
(b) seven recorded talks (2020 to 2025) whose YouTube auto-captions I downloaded with yt-dlp and converted with `scripts/srt_to_transcript.py`; quotes from these are machine speech recognition, carry an approximate video timestamp, and can contain mis-heard words (tone, for example a joke, cannot be verified);
(c) the abstracts, introductions and conclusions of 17 papers or preprints, and 8 further arXiv abstracts, chosen because they argue a position. The most important is the review with Marco Molinaro, "Theoretical challenges towards cutting-plane selection" (2018);
(d) the Optima 80 review on multi-row cuts (with Andrea Tramontani, 2009) and the discussion column printed with it;
(e) five NSF award abstracts on which he is PI or co-PI (taken from the NSF award API; NSF abstracts are normally drafted by the PIs, but authorship is not stated).
Most of his writing is co-authored. Items from co-authored papers or co-PI awards are marked **(co-authored)**, because the stance may belong to the co-authors as much as to Dey. Talk slides are treated as his own voice even when the work is joint.

**Tags.** [stated] = he said or wrote it; [practice] = what he did (papers, talks, code), recorded here only where it anchors a stated claim (agent 03 checks practice); [observed] = what others wrote or said about him; [inferred] = my inference, not to be quoted as his view. Each item is also marked primary or secondary.

---

## 0. Beliefs he repeats (3 or more independent occasions)

| # | Belief (short form) | Occasions (date: source) | Count |
|---|---|---|---|
| R1 | Integer-programming theory lags behind what solvers do; theory should explain why the techniques solvers use (sparse cuts, cut selection, branch-and-bound, strong branching, feasibility pump, MILP relaxations) work | 2013-12 pooling talk; 2014 sparse-cut talk; 2015-07 sparse-cut talk; 2015-12 MOR preprint; 2016-08 ETH talk; 2016 NSF CMMI-1562578; 2017 MIP Workshop talk; 2018 Dey and Molinaro review; 2020 arXiv:2007.15192; 2020 arXiv:2002.02988 and DOTs talk; 2021-10 branch-and-bound talk; 2021 arXiv:2110.10754; 2024 arXiv:2402.05213; 2024-06 MIP 2024 slides | 14 |
| R2 | Real instances are sparse and structured (decomposable, repeatedly re-solved with small data changes); design and analyse methods for that structure | 2009-09 Optima review; 2012 two-row paper (co-authored); 2015-07 talk; 2016 NSF CMMI-1562578; 2017 MIP Workshop talk; 2018 review; 2020-10 DOTs talk; 2021-03 IPAM talk; 2022 arXiv:2208.10028 (co-authored); 2024-08 sensitivity talk; 2025-10 UW-Madison talk | 11 |
| R3 | Strengthen relaxations by convexifying simple substructures, a relaxation that is "easy to analyze and yet strong", and carry this integer-programming paradigm over to convex MINLP and QCQP | 2009-09 Optima review; 2010 NSF CMMI-1030422; 2012-12 conic-MIP duality talk; 2019-10 CRM QCQP talk; 2020-06 IPCO tutorial (slides and spoken); 2021-09 aggregation talk | 6 |
| R4 | Dual bounds, certificates of optimality, matter; a good feasible solution alone is not enough, and heuristics resting on unverifiable data assumptions are not satisfactory | 2015 OPF paper (co-authored); 2018 SPCA preprint (co-authored); 2019-07 SPCA talk; 2019-10 CRM QCQP talk; 2020-06 IPCO tutorial; 2024-08 sensitivity talk; 2024 MIP International talk; 2025-10 UW-Madison talk | 8 |
| R5 | Measure strength with a well-defined, data-independent measure and prove bounds that are tight (matching lower bounds or tight examples) | 2013-12 pooling talk; 2014 sparse-cut talk; 2015-07 talk; 2016 aggregation talk and paper; 2016 arXiv:1601.00198; 2019-07 SPCA talk; 2020 arXiv:2002.02988; 2020-06 IPCO tutorial | 8 |
| R6 | When the real question is too hard, replace it by a simpler proxy question (fix a measure, drop the optimization, study a "toy" model) | 2012 two-row paper (co-authored); 2018 review (twice); 2020 sparse-SDP abstract, slides and Tutte colloquium; 2025-10 UW-Madison talk | 5 distinct projects |
| R7 | Computational studies should be controlled: random instances with known structure, one factor varied at a time, then a check on MIPLIB, with caution about extrapolation | 2012 two-row paper; 2016 aggregation paper; 2021 strong-branching paper; 2024 non-monotonicity paper; 2025 improving-FSB preprint (all co-authored) | 5 |
| R8 | Say plainly what is not known, what is weak and what failed | 2010 mixing talk; 2010 split-rank talk; 2011 SIAM OP talk; 2012 two-row paper; 2018 review; 2018 SPCA preprint; 2020-12 Tutte colloquium; 2024-06 MIP 2024 slides; 2024-11 Lagrangian slides; 2024 MIP International talk; 2025-10 UW-Madison talk | 11 |
| R9 | A method must survive the engineering of a real solver: components interact, so test inside state-of-the-art codes and count all overheads | 2009-09 Optima review; 2017 feasibility-pump preprint; 2018 review; 2021 strong-branching preprint; 2021-03 IPAM talk; 2024-08 sensitivity slides; 2024-11 Lagrangian slides; 2024-11 GMI preprint | 8 |

Claims made once or twice appear below and are marked as single statements.

---

## 1. Research taste: what is worth doing, what a good result is

**1.1 MIP theory should explain solver practice, and the gap is the opportunity** [stated, primary] (R1)
- 2013 (pooling, with A. Gupte; ExxonMobil-supported): the main-results slide is titled "Why do these MILP relaxations work so well?", and the closing "Open Problems" begin "1. The performance of the MILP heuristic is surprising. Can we better explain this?" (talk "Analysis of MILP Techniques for the Pooling Problem", PDF created 2013-12-04, slides PDF pp. 40-44 and 111).
- 2014-2016, sparse cuts: "Most commercial solvers use sparsity to filter cuts" and "Very limited theoretical investigation [Andersen, Weisma[ntel]]" (talk "How Good Are Sparse Cutting Planes?", 2014, PDF pp. 10-13); "Main Goal: Theoretically analyze performance of sparse cutting-planes." (talk "Effectiveness of Sparse Cutting-planes for Integer Programs with Sparse Constraint Matrix", July 2015, PDF p. 10); "Significantly lesser research on evaluating the strength of cuts and (theory of) cutting-plane selection." (talk "Aggregation-based cutting-planes for packing and covering integer programs", Discrete Optimization Workshop, ETH Zurich, 2016, PDF p. 6).
- 2015-2018, in a paper (co-authored with Molinaro and Q. Wang): "Indeed, one way to view the results we obtain in this paper is to attempt a mathematical explanation for the empirical observations of quality of sparse cutting-planes obtained in [8]." (preprint dated 2015-12-29, p. 2; Mathematics of Operations Research 43 (2018) 304-332, DOI 10.1287/moor.2017.0866).
- 2016, as a funded programme (sole PI): "If successful, this project will be able to uncover formal mathematical explanation for various empirically observed behavior of mixed-integer linear programs, such as: Why does selection of sparse cutting-planes for mixed-integer linear programs with sparse constraint matrix work well in many cases? Why does feasibility pump, an important primal heuristic, work much better on average for mixed-integer linear programs with sparse constraint matrices?" (NSF CMMI-1562578 "Sparse Integer Programming", 2016-08-01 to 2020-07-31, award abstract).
- 2018, the programmatic statement (co-authored with Molinaro): "our scientific understanding is far from complete with regards to cutting-plane selection" (abstract); "while the theoretical analysis conducted thus far is important, these results have so far failed to directly help in actual cutting-plane selection" (§4, p. 20); "one is also tempted to ask if there is any value in attempting to pursue "principled and scientific" theory for cutting-plane selection at all. We believe that the answer is yes." (§4, p. 21). Source: Dey and Molinaro, "Theoretical challenges towards cutting-plane selection", Mathematical Programming 170 (2018) 237-266, DOI 10.1007/s10107-018-1302-4, arXiv:1805.02782 (homepage preprint of 2018-05-07, pages cited from it).
- 2020-2021, branch-and-bound: "Even though modern MILP solvers are able to solve very large-scale instances efficiently, relatively little attention has been given to understanding why the underlying branch-and-bound algorithm performs so well." and "We believe that this result provides a compelling indication of why branch-and-bound with variable branching works so well in practice." (co-authored with Y. Dubey and Molinaro; arXiv:2007.15192 abstract; Mathematical Programming 200 (2023) 569-587, DOI 10.1007/s10107-022-01895-4). In his own talk: "Almost 60 years now, but there is very little theoretical analysis of the branch-and-bound algorithm!" and "However, branch-and bound algorithm (with many bells and whistle) seems to work well in practice. So the type of questions we want to understand: ... Can we understand and analyse properties of some well-known rules for partitioning mentioned above? Hopefully this will lead to better rules." (talk "Theoretical and computational analysis of sizes of branch-and-bound trees", Oct 2021, PDF pp. 22-27).
- 2024: the slide "How do solvers select cuts to use?" has a single line, "I do not know." (talk "Introduction to cutting planes for mixed integer linear (nonlinear) programs", June 2024, listed on his talks page as "Overview of Cutting Plane Theory (MIP 2024)", PDF p. 132). The next slides list "things that might matter" (depth of cut, "Not always the best", cuts separating several points, parallelism, sparsity, "Facet-defining or not?", how many cuts to add) (PDF pp. 133-140).
- Era note: the claim spans his whole independent career (assistant professor 2009 to full professor now). Its object moved from cuts (2013-2018) to branching (2020-2025). [inferred]

**1.2 Certificates over heuristics** [stated, primary] (R4)
- "Motivation: Heuristics do not come with certificates. Many heuristic algorithms have been proposed in the literature ... However, conditions under which (some of) these computationally friendlier methods can be shown to "work well", make very strong and often unverifiable assumptions on the problem data. Therefore, the performances of these heuristic methods are not clear in general." (talk "Convex integer programming model to obtain dual bounds for sparse PCA", workshop "Discrete Optimization and Machine Learning", July 2019, PDF p. 4). The paper version, co-authored with R. Mazumder and G. Wang, sets the goal of "certificates of optimality via dual bounds, which make limited restrictive/unverifiable assumptions on the data" (preprint of 2018-10-21, p. 2; Operations Research 70 (2022) 1914-1932, DOI 10.1287/opre.2021.2153; the homepage lists the year as 2021).
- On global optimization in general: "Ideal goal: Find a globally optimal solution", then "What we will usually settle for": a possibly approximately feasible point and a lower bound such that the gap "is "small"" (IPCO 2020 summer-school tutorial "Convexification in global optimization", June 2020, PDF p. 3).
- Spoken, about sensitivity analysis for operational IPs: "So the motivation here was dual bounds. Okay, I don't want to just find good solutions. I want to certify it." (MIP International 2024 talk, auto-caption transcript, about 00:16:00).
- Spoken, 2025: "I really like duals ... I like duals. I'm going to call them duals." (UW-Madison ISyE colloquium "Strong duals for mixed integer programs", uploaded 2025-10-06, about 00:04:14). Slide version of the same aim: "Getting high quality dual-bound for similar instances without needing to start solving from scratch would be very useful in this setting." (talk "Sensitivity analysis for mixed binary quadratic programming", Aug 2024, PDF p. 7).
- Applied work states the same standard: one SOCP relaxation plus IPOPT "produces a feasible solution for the largest instance in the IEEE test cases (the 3375-bus system) and also certifies that this solution is within 0.13% of global optimality, all this computed within 157.20 seconds on a modest personal computer" (co-authored with B. Kocuk and X. A. Sun; arXiv:1504.06770 abstract; Operations Research 64 (2016) 1177-1196, DOI 10.1287/opre.2016.1489).

**1.3 What a good theorem looks like: tight, data-independent, constructive, clean** [stated, primary] (R5)
- Tightness as a stated part of the result: the pooling theorem has a second item headed "2. Quality of analysis", showing the factor-n bound cannot be improved for any piecewise-linear MILP relaxation (pooling talk, 2013, PDF p. 44); "The analysis is tight: all the bounds obtained are tight." (2015 sparse-cut talk, conclusion, PDF p. 59); after each 2-approximation theorem, "Moreover, this bound is tight" (2016 ETH talk, PDF pp. 29-30).
- Data independence: bounds that "depend only on the sparsity structure of the constraint matrix and the support of sparse cuts - in this sense, these results truly provide insight into the strength of sparse cuts for sparse MILPs" (co-authored, MOR preprint 2015-12-29, p. 16); "these bounds are completely data independent" (arXiv:1601.00198 abstract); "In order to simplify the question, we arrive at a data independent version of it" (co-authored with G. Blekherman, Molinaro, S. Sun; arXiv:2002.02988 abstract; Mathematical Programming 191 (2022) 981-1004, DOI 10.1007/s10107-020-01578-y).
- A well-defined measure first: "We wanted a measure that is well-defined in all cases" (2014 sparse-cut talk, PDF p. 19); for the k-PSD closure, "We require to make two decisions here: 1. The norm to measure this distance and 2. A normalization method" (talk "Sparse PSD approximation of the PSD cone", Oct 2020, PDF p. 23).
- Constructive proofs and their honest cost: "The proof is contructive. So in principle, we can build the convex hull using the proof. The size of the second order "extended formulation" is exponential in size." (IPCO 2020 tutorial, PDF p. 100); "We present a simple constructive proof of this result." (co-authored with A. Santana, arXiv:1812.10160 abstract; SIAM J. Optim. 30 (2020) 2983-2997, DOI 10.1137/19M1277333).
- Elegance as a criterion, used against his own work: "Challenges: 1 The proof of validity of the stronger inequality is not elegant: More importantly the proof does not extend to more rows of a mixing inequalities." (talk "Mixing Inequalities and Maximal Lattice-Free Triangles", with L. A. Wolsey, 2010, PDF p. 64). Spoken, 2025: "the proof techniques will go through even if they're not binary but the final results the clean results only work when they are binary" (UW-Madison, about 00:09:12).
- Aesthetic remarks (single statements, light-hearted): "Ruled surface are beautiful!" (IPCO 2020 tutorial, PDF p. 158; also CRM 2019 talk, PDF p. 21); "I love cancelling. That's one of my favorite things in math. If you can cancel, you're a happy person." (UW-Madison 2025, about 00:27:41); the subadditive dual is "my most super favorite" and "I always try to sneak in [subadditivity]" (UW-Madison 2025, about 00:04:30, auto-caption reads "sobarity"); "I like collecting strong duals for IPS." (MIP International 2024, about 00:35:16).

**1.4 Prefer tractable (LP, SOCP) relaxations to heavy machinery in practice** [stated, primary] (single theme, stated in several talks)
- "Even though there are nice hierarchies for obtaining convex hulls in IP, in practice, we construct linear programming relaxations within branch-and-bound algorithm, which are often strengthened by addition of constraints obtained from the convexification of simple substructures." and "Usually, we will stick to linear programming (LP) or second order cone representable (SOCr) convex functions and sets for our convex relaxations." (IPCO 2020 tutorial, PDF p. 15). Spoken in the same lecture: "in practice no one actually runs the convergence no one actually you know does the disjunctions [n] times and tries to solve an IP because even though it's a beautiful theory and it does [teach] us a lot and gives us a lot of insights in practice that's too expensive" (lecture 1, about 00:22:46; bracketed words are my correction of the auto-caption).
- SDP: "Polynomial-time algorithm-- but often challenging to solve in practice." (Oct 2020 sparse-PSD talk, PDF p. 5). OPF conclusions: "1. SOCP relaxation is quite good! 2. Solving SOCP based relaxation is orders of magnitude faster than solving SDPs." and "6. There is a need to develop global solvers!" (talk "New Formulation and Valid Inequalities for the Optimal Power Flow Problem", with Kocuk and Sun, PDF created 2015-03-18, PDF p. 111).
- Nuance in the same 2020 lecture: the sum-of-squares approach "is very beautiful very insightful very interesting and it actually also works in practice" for some power-systems classes (lecture 1, auto-caption). See Contradictions, C8.

**1.5 Doubts about the standard yardsticks of cut strength** [stated, primary]
- Facetness: for the infinite group relaxation, facets are dense among minimal inequalities, and "This casts doubts on whether being a facet-defining inequality is really useful in this context." (review 2018, p. 7, co-authored). Earlier (2009) he already asked for "new methods, other than based on merit index or strength of continuous variables coefficients ... to predict the usefulness of extreme inequalities for group problems" (talk "Gomory Functions", with J.-P. P. Richard, December 2009, PDF p. 96).
- Worst-case results: they "only provide a coarse indication of which families of cuts seem to be strong, while not indicating which class of cutting-planes is good (or, equally importantly, bad) for a given class of instances." (review 2018, p. 10); "Another feature missing from the previous results is that they work on worst-case instances." (p. 14). See Contradictions, C1.
- Depth of cut: "Maximize depth of cut ... Not always the best" (MIP 2024 slides, PDF p. 133); the review gives the dominated-cut example (2018, p. 8).

---

## 2. Problem choice: where problems come from, why now

**2.1 From what solvers actually do but nobody has analysed** [stated, primary] (R1)
- Feasibility pump: "Randomization step plays significant role but has not been explicitly studied. We focus on changing the randomization step by "thinking about sparsity"." (talk "Using Sparsity to Design Primal Heuristics for MILPs: Two Stories", MIP Workshop 2017, PDF p. 9). Paper (co-authored with A. Iroume, Molinaro, D. Salvagnin): the improvements so far "mainly focus on the rounding and projection steps. We start a more in-depth study of the randomization step" (arXiv:1609.08121 abstract; SIAM J. Optim. 28 (2018) 355-378, DOI 10.1137/16M1095962).
- Split cuts: "Why do we care? Most inequalities (for general integer variables) used in commercial softwares are split cuts" (talk "Split Rank of Triangle and Quadrilateral Inequalities", with Q. Louveaux, CORE, May 2009, PDF p. 28).
- Strong branching: "However, to the best of our knowledge there is no understanding of how good strong-branching is in absolute terms." (co-authored, homepage preprint of 2021, p. 3; Mathematical Programming 205 (2024) 303-336, DOI 10.1007/s10107-023-01977-x).
- Folklore: whether adding cuts always shrinks trees, a question raised against "the expectation that the tighter formulation would produce smaller branch-and-bound trees" (co-authored with P. Shah and Molinaro, arXiv:2402.05213 abstract; INFORMS J. Computing 38 (2026) 53-66, DOI 10.1287/ijoc.2024.0709; homepage lists 2025).
- Aggregation cuts: "The set of all aggregation cuts have been studied empirically [11], but to the best of our knowledge no theoretical study is present." (co-authored, homepage preprint 2016-06-26, p. 2; Mathematical Programming 171 (2018) 331-359, DOI 10.1007/s10107-017-1192-x).

**2.2 From applications where existing tools fail** [stated, primary]
- Origin story told on slides (2019): "A QCQP for Structural engineering application: Updating FEM model for bridges", then "Need to obtain good dual bounds. We tried various approached. 1. McCormick relaxation + Semidefinite programming relaxation 2. Commercial solvers (for hours)", then "Motivation from Integer programming: Convexification of substructures like knapsack set, flow cover sets, mixing sets, etc.", then the theorem, then "This substructure convexification worked well" with a BARON comparison ("Running-time: 10 hours."), then "Questions: What about more general quadratic constraints? What about more general linear constraints?" (talk "Convexification of substructures in quadratically constrained quadratic program", CRM workshop "Mixed-integer Nonlinear Optimization: Theory and Computation", Oct 2019, PDF pp. 4-12).
- Power systems as the source of a question: "personally I came across these class of problems when I've been looking at some power system applications" and, on system operators who re-solve daily problems, "they just restart from scratch and you shouldn't really be doing that" (MIP International 2024, about 00:13:30 and shortly after).
- Statistics: sparse PCA is chosen because it is "one of the most widely used dimensionality reduction method in statistics and data science" and sparsity aids "interpretability" (2019 SPCA talk, PDF p. 3); subset selection: "Sparsity constraint: For interpretability, restrict to few variables." (talk "Subset selection with sparse matrices", with A. Del Pia and R. Weismantel, April 2018, PDF p. 4).
- Self-description (institutional profile, author not stated, secondary): "His research is partly motivated by applications of non-convex optimization arising in areas such as electrical power engineering, process engineering, civil engineering, logistics, and statistics." (homepage; ISyE profile). An older Georgia Tech page lists "economics, computer vision, logistics and petroleum industry" (GT ARC profile, undated, written around his 2009 arrival).

**2.3 From generalizing the classical theorems of integer programming** [stated, primary] (R3)
- "A number of structural results are known about Integer Linear Programs: 1. Representability results of integer hulls ("Fundamental Theorem of Integer programming") 2. Subaddtive dual 3. Cutting plane closure, ranks, lengths, etc." followed, for convex MIP, by "1. Representability results ? 2. Dual ? 3. Cutting plane closures ?" (talk "Some representability and duality results for convex mixed-integer programs", with D. Moran and J. P. Vielma, 2012-12-17, PDF pp. 2-3).
- "The research objective of this project is to broaden the scope of the following key results known for MILP to the more general domain of convex MINLP" (NSF CMMI-1030422, "Collaborative Research: Fundamentals of Convex Mixed Integer Nonlinear Programming", 2010-2014, sole PI at Georgia Tech).
- "The goal here: To understand and establish generalization of (1) with respect to cuts based on "information from Z2"." where (1) is MIR closure = GMIC closure = split closure (talk with S. Dash and O. Gunluk, July 2010, PDF p. 3); "Fundamental theorem of integer programming ... This motivates the following questions: 1. Let K be a closed convex set. When is conv(K ∩ Zn) a polyhedron?" (talk with D. Moran, June 2011, PDF pp. 2-4).
- Framing by analogy to a classic: the lower-bound paper "can be viewed as the branch-and-bound analog of the seminal paper by Chvátal et al." (co-authored, arXiv:2103.09807 abstract; Mathematical Programming 198 (2023) 539-559, DOI 10.1007/s10107-022-01781-z).

**2.4 Why now** [stated, primary, co-authored unless noted]
- Hardware: "As computer speeds improve and specific architectures (such as parallel computing, GPUs etc.) steadily get better, it may be possible to revisit all the heuristics that current day solvers implement and improve them on the basis of hard science of integer programming and cutting-plane selection." (review 2018, p. 21).
- Machine learning, as of 2018: "To the best of our knowledge machine learning has not been applied to cut generation and selection. We believe that the answer to improved and principled cut-selection may be somewhere in between using only machine learning or only theoretical analysis." (review 2018, p. 21).
- Repeated operational solves: "in such operational applications, instances are significantly similar to each other" (co-authored with X. Gu, A. S. Xavier, F. Qiu, arXiv:2208.10028 abstract, 2022); "Many operations related optimization problems involve repeatedly solving similar mixed integer linear programming (MILP) instances with the same constraint matrix but differing objective coefficients and right-hand-side values." (co-authored with B. Becu, Qiu, Xavier, arXiv:2411.15090 abstract, 2024).

**2.5 Entering a new area, and saying so** [stated, primary, spoken]
- Global optimization (2020): "it's an area that I've been working on in the last say let's say two three years" and "I've just started working in this area last two three years and so there might be a bunch of citations that I don't know and if I don't know about that citation I apologize just please feel free to send me an email" (IPCO 2020 lecture 1, about 00:01:51 and 00:26:09). This dates his move into QCQP convexification to about 2017-2018 by his own account.
- SDP (2020): "most of my work actually has been in integer programming ... in some sense this is a really new topic for me ... i always think of sdps as a black box and so my knowledge is in some many ways limited here" (Waterloo Tutte colloquium, 2020-12-11, about 00:01:30; "sdps" restored from the caption "eps").

---

## 3. Idea generation

**3.1 Relax to a substructure that is easy to analyse yet strong** [stated, primary] (R3)
- "The art lies in obtaining a relaxation that is both easy to analyze and yet strong enough to generate potent cutting planes." (Dey and Tramontani, "Recent Developments in Multi-Row Cuts", Optima 80, September 2009, p. 2; co-authored).
- Imported into QCQP: "A very successful approach in integer linear programing is to generate cutting-planes implied by single constraint relaxations." (CRM 2019 talk, PDF p. 7); "This is challenging to compute! So we can consider convexification of relaxations (similar to integer programming)" (talk "On obtaining the convex hull of quadratic inequalities via aggregations", with G. Munoz and F. Serrano, Sep 2021, PDF p. 8). The 2021 and 2023 QCQP talks then use a "Two row relaxation" of the quadratic system (PDF pp. 10-12 of the 2021 deck; "QCQP: Need for convexification" in the April 2023 deck with Blekherman and Sun).
- Data enter the substructure: "Now we want to consider sets wich includes the data" (IPCO 2020 tutorial, section "Incorporating "data" in our sets", PDF p. 50).

**3.2 Replace a hard question by a simpler proxy** [stated, primary] (R6)
- "While the overall goal is be able to solve MILP models efficiently, given the complexity of solvers one cannot expect to be able to perform a theoretical analysis of this performance metric directly, and thus proxy measures are required." (review 2018, p. 4, co-authored).
- "It is challenging to simultaneously study both the competing objectives in relation to cutting-plane sparsity. Therefore, a first approach to understanding usage of sparse cutting-planes is the following: How much do we lose in the closure of integrality gap if we only use (some of the) sparse cuts (as against dense cuts)?" (review 2018, p. 11).
- Slides: "Relationship between zSDP and zSparse-SDP? Seems like a difficult question to analyze." followed by a slide titled "Easier question": "How far is cone with all k × k submatrices PSD from S+n?" (Oct 2020 sparse-PSD talk, PDF pp. 16-18). Spoken: "it seems obviously almost impossible to analyze in general uh as i stated and so what we tried to do was to simplify this question and so what did we do we basically removed most parts of the question okay so we said forget about the optimization problem" (Tutte colloquium 2020-12-11, about 00:14:52).
- Two-row cuts, after the original goal failed: "the main goal of this paper is to try to answer the following (simpler?) question" (co-authored with A. Lodi, Tramontani, Wolsey; homepage preprint 2012-08-12, p. 2).
- 2025: "I'm going to focus on this sort of quote unquote toy problem ... this seems like a toy example and it is a toy example in some sense but I'll discuss later why this is actually fairly general" (UW-Madison 2025, auto-caption).

**3.3 Invert a standard paradigm** [stated, primary]
- "This motivates a different paradigm to generate valid cutting-planes for integer programs: First we design cutting-planes which we believe will be useful without considering their validity." (co-authored with S. Pokutta, homepage preprint 2012-12-29, p. 1; "Design and verify: a new scheme for generating cutting-planes", Mathematical Programming 145 (2014) 199-222, DOI 10.1007/s10107-013-0645-0). In his CAREER award abstract: "(ii) Design suitable cutting planes and then verify their validity before use, instead of deriving cutting planes without any control over their quality." (NSF CMMI-1149400, 2012-2017).
- The CAREER abstract frames all three of its paradigms as using information left on the table: "A great deal of useful information that could be used in deriving and selecting cutting-planes is often left unused by state-of-the-art MIP techniques." (NSF CMMI-1149400).

**3.4 Use more information than the standard method** [stated, primary] (early career)
- PhD era: "Most cutting planes are generated using one constraint or are based on specific structures." (talk "Improved Gomory Cuts for Primal Cutting Plane Algorithms", with J.-P. Richard, Purdue, INFORMS 2005, PDF p. 3); "All know group based cutting planes using a single constraint to derive cut. We present first know strong cuts that use two constraints. We hope these will be stronger since they use information from two constraints concurrently." (talk on two-dimensional infinite group problems, 2006, PDF p. 2).
- He grounded the multi-row direction in others' computational studies, quoting Fischetti and Saturni, Dash and Gunluk, and Gomory and Johnson on a slide titled "Studies Suggests Studying High-Dimensional Group Problems" (talk "A Family of Facets for Multiple-Constraint Infinite Group Relaxation of MIPs", with Richard, 2007-10-02, PDF p. 6), after a table of the "Most Successful Cutting Planes for Unstructured Problems" from Bixby and Rothberg (PDF p. 3).

**3.5 Borrow tools across fields** [stated, primary]
- "techniques can be taken from one area and applied in [an]other area not only necessarily at the mathematical level but also at a more computational level and that's what we'll see in this talk" (IPAM workshop "Deep Learning and Combinatorial Optimization", talk "Solving SDPs by using sparse PCA", uploaded 2021-03-04, about 00:01:13). In the same talk he uses heuristics "developed by the machine learning community" for sparse PCA but says "there is not going to be much learning involved in this talk" and "we're sort of skipping the learning bit" (about 00:01:07 and 00:12:39).
- WalkSAT from satisfiability for the feasibility pump (arXiv:1609.08121); the restricted isometry property from sparse recovery in the PSD-closure proof ("This approximate preservation of norms of sparse vectors is precisely the notion of the Restricted Isometry Property.", Oct 2020 slides, PDF p. 70); hyperbolic polynomials, which "the students ... [taught] to me recently the last two three months" (Tutte colloquium, auto-caption reads "they have to start this").

**3.6 Start from an empirical surprise** [stated, primary]
- Sparse SDP: "in fact that's how we got started on this project is that not only were we doing so well [computationally] in terms of computational time the bounds we got were incredibly close to the sdp" (Tutte colloquium, about 00:29:49); abstract: "Surprisingly, it has been observed empirically that in some cases this approach appears to produce bounds that are close to the optimal objective function value of the original SDP." (arXiv:2002.02988).
- Copositive duals: another group "empirically observed that this was always true okay in their paper and so that sort of really motivated us" (MIP International 2024, about 00:26:27).
- Pooling: "The performance of the MILP heuristic is surprising. Can we better explain this?" (2013 talk, PDF p. 111).

---

## 4. Experiments and execution

**4.1 Controlled experiments that isolate one factor** [stated, primary, all co-authored] (R7)
- Two-row cuts: instances were "designed to represent different problem features by varying the number of integer non-basic variables, bounds, non-negativity constraints and density" (2012 preprint, abstract); cuts were added "without applying any (sophisticated) selection rule that might prevent us from understanding the real strength of the cuts. (Clearly, cut selection is a fundamental issue, but it is definitely not restricted to the context of two-row cutting planes and it is a crucial research topic by itself.)" (p. 10); "We believe that the computational methodology introduced in this paper may prove to be useful in the future to analyze multi-row cuts" (p. 24). Source: "On the Practical Strength of Two-Row Tableau Cuts", INFORMS J. Computing 26 (2014) 222-237, DOI 10.1287/ijoc.2013.0559; preliminary version "Experiments with Two Row Tableau Cuts", IPCO 2010, LNCS pp. 424-437, DOI 10.1007/978-3-642-13036-6_32 (not read).
- Strong branching against a ground truth: experiments compare strong-branching trees with optimal trees computed by dynamic programming; "The main take-away from these experiments is that for all these instances, the size of the strong-branching based branch-and-bound tree is within a factor of two of the size of the optimal branch-and-bound tree." (arXiv:2110.10754 abstract), with a stated limit: "Finally we end this section with a word of caution regarding over-interpreting the computational results above: ... computational experiments could be performed only on relatively smaller problem sizes with up to 20 binary variables. Some of the observations derived here may not extrapolate to larger instances." (homepage preprint 2021, p. 13).
- "Using randomly generated problem instances with known structures, we derive insights and fine-tune our modified scores." followed by MIPLIB 2017 evaluation (Shah and Dey, "Improving Full Strong Branching Decisions by Incorporating Additional Information", arXiv:2507.09455, 2025).
- Prevalence check after a worst-case theorem: "we empirically attempt to estimate the prevalence of non-monotonicity in practice" on random multi-dimensional knapsacks and MIPLIB 2017; result: "non-monotonicity is not merely a theoretical possibility, but is surprisingly prevalent in practice" (arXiv:2402.05213; homepage preprint 2024, p. 13).

**4.2 Test inside real solver engineering** [stated, primary] (R9)
- "While the analyses above give insights on the usefulness of using RandWalkSAT in the randomization step of FP, in order to attest its practical value it is important to understand how it interacts with complex engineering components present in current Feasibility Pump codes." (co-authored, homepage preprint 2017-06-22, p. 4).
- "modern day solvers have become complex, highly integrated engineering marvels, where different components of the solvers are heavily inter-dependent, and therefore it may be altogether possible that one kind of cutting-plane selection improves the average solution time in the context of one code and miserably fails in conjunction with other codes!" (review 2018, p. 21, co-authored).
- "Unfortunately, the number of nodes in this tree depends not only on the node selection rule and variable selection rule, but also on the underlying LP solver as well." (strong-branching preprint 2021, p. 5, co-authored).
- Engineering compromise, spoken: "it's uh the most natural thing to do engineering wise is why not add one round of [dense cuts] all right let's make a compromise" (IPAM 2021, about 00:22:32; "dense cuts" restored from the caption "dead skills").
- Slides that name the gap between method and implementation: "Actual problem solved in experiments involves solving a restriction of COP with some other `engineering' tricks." (Aug 2024 sensitivity talk, PDF p. 60); "Significant more engineering in the implementation of our methods can be done." (Nov 2024 Lagrangian-dual talk, PDF p. 75).
- Bar for a computational claim: "this is the first work in the literature of data-driven cutting plane generation that is able to significantly accelerate the performance of a commercial state-of-the-art MILP solver, using default solver settings, on large-scale benchmark instances." (co-authored, arXiv:2411.15090 abstract).

**4.3 Count everything** [stated, primary, co-authored]
- In the GMI-history preprint: "When we also include the computational time required for predicting and generating cuts, some new insights emerge. First, adding cut collection time to the expert method completely nullifies its running time improvements" (arXiv:2411.15090v1, p. 12).
- Sequential versus parallel, spoken: "this is a bit embarrassing but all of this talk was about doing parallel computing but we actually use [sequential]" (MIP International 2024, about 00:57:59).

**4.4 Resource context he states** [stated, primary]
- OPF: "a modest personal computer" (arXiv:1504.06770). SPCA: "All numerical experiments are implemented on MacBookPro13 with 2 GHz Intel Core i5 CPU and 8 GB 1867 MHz LPDDR3 Memory." (preprint 2018, p. 11); "SDP: Because of limitation of hardware and software, the SDP relaxation method cannot be implemented on the instances with input matrix of size greater than or equal to 300 × 300." (2019 SPCA talk, PDF p. 40).
- Industrial and agency support named on slides and pages: ExxonMobil for pooling ("Support from EXXONMOBIL Research and Engineering is gratefully acknowledged", 2013 deck, PDF p. 1); projects funded by DOE, NSF, ONR, AFOSR, Argonne and Sandia (homepage Projects page).

---

## 5. Judging results

**5.1 Worst case versus practice** [stated, primary]
- "In practice, the dual bounds are significantly better than worst-case performance, and even better than the SDP bounds on some real-life instances." (2019 SPCA talk, PDF p. 15).
- "This is perhaps not surprising since the theoretical bounds are data-free and therefore "worst-case" in nature." and "Hence, the empirical experiments are another justification for the main message of this paper: In many cases sparse cuts provide very good bounds for sparse IPs." (co-authored, MOR preprint 2015-12-29, p. 16).
- "We believe that as the number of vertices increase, the structure of the polytope becomes more important in determining d(P, P k) and Theorem 1 only captures the worst-case scenario." (co-authored, "Approximating polyhedra with sparse inequalities", homepage preprint 2015-04-27, p. 5; Mathematical Programming 154 (2015) 329-352, DOI 10.1007/s10107-015-0925-y).
- "In order to avoid the exponential worst-case lower bounds, we follow the common idea of considering random instances." (arXiv:2007.15192 abstract, co-authored).

**5.2 Success means the theory explains what is seen** [stated, primary, spoken]
- "in some sense this [in] my mind explain[s] what's going on there" (DOTs talk, uploaded 2020-10-24, about 00:23:36).
- Asked whether the PSD-closure bounds were negative results: "i really it would have been great if i could explain what we observe in practice and it does not ... obviously it means that there's a lot more structure that are there in these power problems" and "i could not complete the whole cycle i would have loved to say that oh theory explains everything we see in practice that's it but i mean it [works] really much better for some [classes] of problems so there's probably more structure of this those problems that we don't still know that's making it work" (Tutte colloquium, about 00:55:27 and 00:57:33).

**5.3 Theory is valuable even if never deployed (early statement)** [stated, primary]
- "Even if such a technique is never used in practice - this definitely shows the usefulness of generating cuts based on multiple constraints." (INFORMS 2005 talk with Richard, PDF p. 27; PhD-student era).

**5.4 Failures, abandoned directions and negative results he reports** [stated, primary unless noted]
- Multi-row cuts, a dated arc. 2009, cautious optimism: "The most significant challenges are probably on the practical side. While Espinoza [24] presents encouraging result, there are numerous avenues for improvement. The primary difficulty is that of cut selection." and "Another practical difficulty with this class of cutting planes is that they tend to be dense. ... At this time various computational experiments are underway and we hope that much progress will be made in terms of successfully exploiting these cutting planes." (Optima 80, p. 8, co-authored). 2012-2014, the verdict (co-authored): "From a computational standpoint, our initial goal was to show that a small subset of two-row cutting planes ... could, together with one-row cuts, be useful in closing a significant amount of gap for general MIPs. However such a goal was too ambitious and we have had to considerably restrict it." (preprint p. 2); "Unfortunately these characteristics seem rarely to be present among real life instances, and more specifically the tableau rows of the MIPLIB instances are far from dense." (abstract); "the experiments in this paper suggest that type 2 triangle cuts are not competitive with split cuts" and "generating facets of the continuous two-row relaxation (2) and then strengthening them to obtain valid inequalities for (1) does not lead to useful cutting planes for real-life instances" (p. 25). In 2018 the review records the same: "several computational experiments ... have indicated that triangle and quadrilateral cuts do not work as well as split cuts in practice" (p. 6).
- [inferred] The finding that MIPLIB tableaux are sparse precedes, and plausibly fed, his 2014-2020 programme on sparse cuts and sparse IPs; I found no place where he states this link.
- Group-cut programme, self-critique 2007-2009: "Pitfalls... `Low Rank' ... Exponential increase in number of cuts: Although group cuts are easy to derive, the number of cuts increase exponentially." (2007 talk, PDF p. 55); "Challenges: 1. Separation. 2. Closed-form of some of the inequalities" (talk with Wolsey, Aussois 2008, PDF p. 35); "Better methods to search and prove that inequalities are extreme are needed." (December 2009 talk, PDF p. 96).
- Weak or partial results: "This lower bound seems to be weak when the vertices of the lattice-free set Q~ are all integral" (talk "A Lower Bound on the Split Rank of Intersection Cuts", 2010, PDF p. 65); "Not the paragon of perfection: lower bound on rank of An" (talk "A Verification Based Method to Generate Cutting Planes for IPs", SIAM Conference on Optimization 2011, PDF p. 43); "While we have improved upon the bound presented in [29], we do not know if this new bound is tight." (SPCA preprint 2018, p. 3, co-authored); "Better bounds (we do not know if our bounds are tight)" (Nov 2024 Lagrangian talk, PDF p. 75).
- Relaxations dropped from a paper: "we empirically observed that such a relaxation is consistently weaker and hence omitted from further discussion" (co-authored with Kocuk and Santana, homepage preprint 2019-02-02, p. 13; Journal of Global Optimization 77 (2020) 227-272, DOI 10.1007/s10898-019-00844-4).
- Copositive closed-form dual: "We were super excited. Um and then this is what we discovered. So there is a challenge to this idea." ... "it's not useful in practice ... And so there's no free lunch unfortunately." (MIP International 2024, about 00:28:41 and 00:31:33); on the experiments, "I know there are experts here who are certainly going to frown upon these results and that's totally all right. Uh these are extremely small and the reason these are extremely small is because I don't know how to solve [copositive] programs" (about 00:32:29); "So for operational IPs, I really think we need to think more and do more. Is this the method, this [dual]? I don't know. I don't think so. But this is exciting." (about 00:35:16).
- Augmented Lagrangian duals (work by others and with S. Ahmed): "I would say that I'm a little bit sad that this really did not take off as much as I thought in terms of designing actual algorithms that converge" (MIP International 2024, about 00:10:10).
- Lagrangian duals with zero gap, 2025: "honestly you know Those experiments are a setup right ... each block has only 100 variables on 100 variable problems [Gurobi] can solve a quadratic IP if those blocks were of size thousand I don't know what to do right so so I'm not saying this is an answer" (UW-Madison 2025, about 00:55:06).
- Cut selection after 20 years: the 2009 open problem ("Good cut selection rules when using multi-row Cuts", PDF p. 96 of the December 2009 deck) is still open in his own words in 2018 ("We recognize that these results are very preliminary results; as such, we are very far from answering the questions raised in Section 1.2.", review p. 21) and in 2024 ("I do not know.").
- Rejected papers and retractions: none found in his public statements (see Gaps).

**5.5 Rules of thumb drawn from experiments** [stated, primary, co-authored]
- "empirical evidence suggests that crossing the 20% gap-closed threshold via cuts could be a good rule of thumb for deciding whether the FSB-P tree size will decrease" (non-monotonicity preprint 2024, p. 13).
- "From cut selection perspective, the insight here is that for packing and covering problems, using aggregation cuts may provide limited benefit over using cuts generated from only the original constraints, while aggregation cuts may produce significant value for general IPs." (aggregation preprint 2016, p. 2; a section "Discussion: Main take-aways of the paper", p. 8).

---

## 6. Writing and talks

**6.1 How his talks are built** [practice, primary; agent 03 should verify against papers]
- Decks open with the practice that motivates the question ("In practice", "Why do we care?", "Most solvers prefer to use sparse cutting-planes", "Many applications: Decision making with vast economic and societal impact") and close with conclusions and explicit open questions. 17 of the 36 decks end with "Open Questions", "Some Questions", "Challenges", "Future directions" or "Research questions" (2007 to 2024). Several have a slide called "Main take aways" (MIP 2024, PDF pp. 27-31) or "Discussion" with an "Upshot:" (2010 split-rank talk, PDF p. 64).
- Papers sometimes carry an explicit take-away section (aggregation paper 2016, §3 "Discussion: Main take-aways of the paper") or a "word of caution" paragraph (strong-branching preprint, p. 13).

**6.2 Credit and citation** [stated, primary]
- A two-slide list headed "Contribution of many people" ends "And many more! I apologize in advance if I miss any citations. This is not intentional." (IPCO 2020 tutorial, PDF pp. 16-17).
- "we were not the first to look at this they were you know there was a very nice paper by" Qualizza, Belotti and Margot, and "recently there's a really nice paper by" Misener's group (DOTs 2020, about 00:06:36; names garbled in the caption, identified from the slide list on PDF pp. 12-13 of the Oct 2020 deck).
- Students named as the drivers: "really the thought leader for a lot of what I'm presenting is Jing[ye] [Xu] who's a PhD student uh in his third year" (UW-Madison 2025, about 00:04:32).

**6.3 Teaching** [stated, primary; single statements]
- Spoken: on LP weak duality, "I don't know if you've done this fun exercise where you divide the class into two room and one side only computes primal values the other side [duals] and they compare which is fun I I love doing that" (MIP International 2024, about 00:17:03).
- CAREER education plan: "an outside-classroom operations research puzzle competition to foster and enrich an environment for undergraduate research" and "a new graduate course will be designed with the aim of dissemination of research results directly to future practitioners and to bring students from different engineering communities together" (NSF CMMI-1149400, 2012).
- The one syllabus on his site (ISyE 6661 Linear Optimization, Fall 2020, remote asynchronous) contains no statement about research method.

---

## 7. Research organisation

**7.1 Collaboration** [stated, primary]
- "Marco Molinaro who has been my partner in crime for the last 12 15 years. We work a lot together. He's in Brazil." (UW-Madison 2025, about 00:04:32). The slide decks show recurring collaborators across eras: Richard (Purdue, 2005-2010), Wolsey and Louveaux (CORE, 2008-2010), Dash and Gunluk (IBM, 2010-2012), Vielma and Moran (2010-2013), Molinaro (2014-2025), Kocuk and Sun (power, 2015-2022), Blekherman (mathematics, 2020-2023), Cifuentes and Xu (2024-2025). [practice, from title slides]
- Cross-community framing in a co-PI award: "This EAGER project proposes to develop new approaches by synthesizing the ideas from the two communities by interdisciplinary collaboration between computer scientists and optimization specialists" and "PIs plan to develop a theory of "natural instances"" (NSF CCF-1415460, PI G. Nemhauser, co-PIs S. Vempala, M.-F. Balcan, Dey, 2014-2017; co-authored).

**7.2 Learning from students and from experts in the room** [stated, primary, spoken]
- Students taught him hyperbolicity cones (Tutte 2020, see 3.5); in 2025, "some of the stuff that I'm presenting actually the experts are here the world experts. So, I'm hoping to hear from them." (UW-Madison 2025, opening).

**7.3 Roles** [stated in institutional pages, secondary]
- Director of doctoral recruiting and admissions (homepage, 2026); associate chair for graduate studies in 2020 (ISyE news, 2020-10-23); vice chair for integer programming of the INFORMS Optimization Society 2011-2013; program committees of MIP 2013 and IPCO 2017 and 2020; associate editor of Mathematics of Operations Research, Mathematical Programming A and SIAM J. Optimization (homepage).

**7.4 What others observed** [observed]
- Laurence Wolsey, his CORE post-doc host, 2009: "Later when Santanu Dey came to Core, my main concern was how to deal with integer non-basic variables, which again led him far beyond what was initially asked." (Optima 80, discussion column "Comments on Multi-Row Cuts" by Cornuejols, Weismantel and Wolsey, p. 9; secondary, but a first-hand recollection).
- Gerard Cornuejols in the same column, on the two Dey-Wolsey papers: "This is important work. But I find the second paper even more surprising." (p. 10).
- INFORMS Optimization Society, Egon Balas Prize 2020 (inaugural), citation as quoted by ISyE news: "strong and seminal contributions to the theory of maximal lattice-free convex sets; multi-row cuts; cutting planes in integer programming; the structure of mixed-integer convex optimization; and, along with co-authors, developed practical algorithms for power problems based on strong relaxations from a detailed analysis of the underlying systems." (ISyE news, 2020-10-23; secondary). His only quoted reply: "I am honored to receive this award and feel truly humbled".
- A DOTs organizer addressed as "Alex" in the recording, 2020: "he kind of stands for a lot of what [Egon] stood for with a mix of theoretical and practically relevant work" (DOTs, about 00:00:59; auto-caption).

---

## Era and resource context (summary)

| Period | Position and setting | Stated method in that period |
|---|---|---|
| 2003-2007 | MS and PhD student, Purdue IE; papers with J.-P. Richard | Use more than one constraint; "We hope these will be stronger"; value of a technique "Even if such a technique is never used in practice" |
| 2007-2009 | Post-doc, CORE (with Wolsey, Louveaux) | Facets of multi-row group problems; asks for separation and closed forms; Wolsey observes him going "far beyond what was initially asked" |
| 2009-2015 | Assistant then associate professor, Georgia Tech; NSF CAREER 2012; collaborators at IBM, Bologna | Generalize MILP theory to convex MINLP; "Design and verify"; two-row cuts tested and found weak; certificates for power systems on a "modest personal computer" |
| 2014-2020 | Long collaboration with Molinaro begins; NSF "Sparse Integer Programming"; ONR QCQP funding; entry into global optimization around 2017-2018 by his account | Explain solver practice (sparsity, aggregation, feasibility pump); proxy questions; tight data-independent bounds; convexify QCQP substructures |
| 2020-2026 | Full professor, chair holder, doctoral-admissions role; AFOSR branch-and-bound, DOE, Argonne, Sandia projects; ML-adjacent work | Theory of branch-and-bound and strong branching; non-monotonicity; data from repeated instances; strong duals for distributed computing and sensitivity; frank reports of what does not yet work |

---

## Contradictions (kept, not reconciled)

- **C1. Tight worst-case bounds as a virtue, versus worst-case results as too coarse.** He presents tightness and data independence as marks of quality (R5: 2013, 2015, 2016, 2020), yet writes that worst-case results "only provide a coarse indication" (2018 review, p. 10), that "Theorem 1 only captures the worst-case scenario" (2015), that data-free bounds are "worst-case" in nature (2015 preprint), and in 2020 that his PSD-closure bound "is not great ... it doesn't reflect what we see in practice" (Tutte colloquium, about 00:52:18). In 2020 he also moves to random instances "to avoid the exponential worst-case lower bounds".
- **C2. Practice-facing theory, versus "I never answer those questions".** Across 14 occasions he says theory should explain and improve solvers (R1), and in 2018 that principled theory is worth pursuing for solvers. In 2025 he says of his strong Lagrangian duals: "of course you ask is this tractable is this practical and I don't know the answer to that I never answer those questions but I'll try" (UW-Madison 2025, about 00:29:17; auto-caption, tone not verifiable, possibly a joke).
- **C3. Multi-row optimism, then a negative verdict.** 2006: "We hope these will be stronger since they use information from two constraints concurrently"; 2009: "we hope that much progress will be made"; 2012 CAREER abstract: "(i) Use information from multiple constraints simultaneously to derive cutting planes"; but 2012-2014: "such a goal was too ambitious" and type-2 triangle cuts "are not competitive with split cuts". Both dated, not reconciled.
- **C4. Single-constraint relaxations as the limitation to overcome, versus the model to copy.** 2005-2009 he frames one-row cuts as the limit to go beyond ("Most cutting planes are generated using one constraint"); in 2019 he tells a QCQP audience that "A very successful approach in integer linear programing is to generate cutting-planes implied by single constraint relaxations", and in 2021-2023 he applies "Two row relaxation" ideas to QCQP although the MILP two-row programme had disappointed computationally.
- **C5. The MIPLIB sparsity statistic.** Slides of 2015 and 2017 and the 2018 review give "The average number (median) of non-zero entries in the constraint matrix of MIPLIB 2010 instances is 1.63% (0.17%)." In 2025, speaking from memory, he says "I think average [sparsity] in miplib instances is like 0.06% ... or something", for "the previous version of miplib" and "ignoring the bound constraints" (UW-Madison 2025, about 00:37:33). The numbers differ; the measures may differ too.
- **C6. Facets as the goal, then doubt about facets.** His 2006-2010 work and slides prize "First known facets" (2007 talk, PDF p. 57) and ask for "Better methods to search and prove that inequalities are extreme"; the 2018 review says the density result "casts doubts on whether being a facet-defining inequality is really useful in this context". Already in 2009 he asked for usefulness measures other than "merit index or strength of continuous variables coefficients".
- **C7. Machine learning: "somewhere in between" (2018) versus "skipping the learning bit" (2021).** In 2018 the review predicts the answer to cut selection lies between learning and theory; in his 2021 talk at a deep-learning workshop he uses ML-derived heuristics but avoids learning; from 2022 he co-authors learning-enhanced branching and historical-data cut generation (practice, for agent 03). Recorded as a dated shift.
- **C8. Hierarchies are beautiful but "too expensive" in practice, versus SOS "also works in practice".** Same lecture (IPCO 2020, lecture 1): for IP hierarchies "in practice that's too expensive", and for sum-of-squares "it actually also works in practice" on some power-systems classes.

---

## Gaps

- No essay, blog, interview, podcast, oral history or written advice to PhD students was found (two WebSearch calls, his homepage, Georgia Tech news, YouTube search). Layer 7 (supervision) therefore rests on a few spoken remarks and on others' observations; agent 04 should look at his students' dissertations and acknowledgements.
- The book chapter J.-P. P. Richard and S. S. Dey, "The Group-Theoretic Approach in Mixed Integer Programming", in 50 Years of Integer Programming 1958-2008 (Springer, 2010) pp. 727-801, DOI 10.1007/978-3-540-68279-0_19, which has a "Perspectives" part in its homepage title, is not open access (Unpaywall: is_oa false). Not read. The December 2009 slides "based on the review" were read instead.
- His Egon Balas Prize presentation (virtual INFORMS Annual Meeting, November 2020, per ISyE news) was not found as a recording or text. The prize citation was read only as quoted by ISyE news.
- The UW-Madison event page for the 2025 colloquium is behind a Cloudflare challenge; not read (the recording was). The exact date and venue of the MIP International 2024 talk are not in the video metadata (upload 2025-04-29).
- No recording or transcript found for the MIP 2024 cutting-plane overview (June 2024); only its slides. Three other linked videos (BIRS 2015 sparse-cut talk, a QuadAggV.mp4 file on his site, an IIM Ahmedabad pooling talk) have no captions and were not transcribed.
- All spoken quotes come from YouTube auto-captions: words in brackets are my corrections; tone and humour cannot be checked.
- Most written statements are co-authored, chiefly with Molinaro; I could not separate his voice from his co-authors'.
- The NSF abstracts are assumed to be PI-drafted; this was not verified. Two of the five are co-PI awards (CCF-1415460 led by Nemhauser; the 2023 structural model-updating award led by Yang Wang).
- His PhD thesis (Purdue, 2007) and the IPCO 2010 "Experiments with Two Row Tableau Cuts" paper were not read.
- Rejected papers, errata or retracted claims: none found in his public statements; not searched in journals.
- Metadata note for other agents: arXiv:1902.00739 (Dey, Kocuk, Santana) lists DOI 10.1137/18M1210812, but Crossref resolves that DOI to a different paper (Kocuk and Moran, "On Subadditive Duality for Conic Mixed-integer Programs", SIAM J. Optim. 29 (2019) 2320-2336). The published version of 1902.00739 is J. Global Optim. 77 (2020) 227-272, DOI 10.1007/s10898-019-00844-4. Year mismatches between homepage and Crossref: SPCA paper (homepage 2021, Crossref 2022) and non-monotonicity paper (homepage 2025, Crossref 2026).

---

## Sources

**A. Homepage and syllabus (primary)**
1. Santanu S. Dey, homepage (Home, Publications, Publications by research area, Talks, Projects, People, Teaching), accessed 2026-10-10, https://www2.isye.gatech.edu/~sdey30/ (primary)
2. S. S. Dey, ISyE 6661 Linear Optimization syllabus, Fall 2020, https://www2.isye.gatech.edu/~sdey30/syllabus.pdf (primary)

**B. Talk slides (primary; all at https://www2.isye.gatech.edu/~sdey30/<file>.pdf; date from title slide or, if absent, PDF creation date)**
3. "Improved Gomory Cuts for Primal Cutting Plane Algorithms" (Dey, Richard), INFORMS 2005, LPLiftingTalk.pdf
4. "Continuous and Discontinuous Extreme Inequalities for Infinite Group Problems" (Dey, Richard, Miller, Li), INFORMS 2006, discon1.pdf
5. Facets of two-dimensional infinite group problem (Dey, Richard), 2006, twodim.pdf
6. "A Family of Facets for Multiple-Constraint Infinite Group Relaxation of MIPs" (Dey, Richard), 2007-10-02, SeqMerge.pdf
7. "Extreme Inequalities For Two-Dimensional Group Problem With Minimal Coefficients For Continuous Variables" (Dey, Wolsey), Aussois 2008, newpresentation4.pdf
8. "Split Rank of Triangle and Quadrilateral Inequalities" (Dey, Louveaux), May 2009, FiniteSplitRank.pdf
9. "Constrained Infinite Group Relaxations of MIPs" (Dey, Wolsey), May 2009, Sfree.pdf
10. "Gomory Functions" (Dey, Richard), December 2009, gomoryfunc2.pdf
11. "Mixing Inequalities and Maximal Lattice-Free Triangles" (Dey, Wolsey), 2010, MixingInequality.pdf
12. "A Lower Bound on the Split Rank of Intersection Cuts" (Dey), 2010, LowerBndSplitRank.pdf
13. "The Chvátal-Gomory Closure of Strictly Convex Body" (Dadush, Dey, Vielma), May 2010, CGClosure.pdf
14. "Some Relationships between Disjunctive Cuts and Cuts based on S-free Convex Sets" (Dash, Dey, Gunluk), July 2010, asym0.pdf
15. "A Verification Based Method to Generate Cutting Planes for IPs" (Dey, Pokutta), SIAM OP 2011, v4.pdf
16. "Some Properties of Convex Hulls of Integer Points Contained in General Convex Sets" (Dey, Moran), June 2011, convexhulltalk1.pdf
17. "Some representability and duality results for convex mixed-integer programs" (Dey with Moran, Vielma), 2012-12-17, slidespolyduality3.pdf
18. "Analysis of MILP techniques for the Pooling Problem" (Dey, Gupte), 2013 (PDF 2013-12-04), PoolingMILP.pdf
19. "How Good Are Sparse Cutting Planes?" (Dey, Molinaro, Wang), 2014, scp3.pdf
20. "Integer Quadratic Programming is in NP" (Del Pia, Dey, Molinaro), 2014, IQPNP.pdf
21. "New Formulation and Valid Inequalities for the Optimal Power Flow Problem" (Kocuk, Dey, Sun), 2015, ACOPFlast.pdf
22. "Effectiveness of Sparse Cutting-planes for Integer Programs with Sparse Constraint Matrix" (Dey, Molinaro, Wang), July 2015, SparseCutMatrixTalk.pdf
23. "Aggregation-based cutting-planes for packing and covering integer programs" (Bodur, Del Pia, Dey, Molinaro, Pokutta), Discrete Optimization Workshop, ETH Zurich, 2016, AggregationCuts0.pdf
24. "Some cut-generating functions for second-order conic sets" (Santana, Dey), 2016-12-04, GeneralCG.pdf
25. "Using Sparsity to Design Primal Heuristics for MILPs: Two Stories" (Dey with Iroume, Molinaro, Salvagnin, Wang), MIP Workshop 2017, PrimalHSparse1.pdf
26. "New SOCP relaxation and branching rule for bipartite bilinear programs" (Dey, Santana, Wang), Feb 2018, BBP1.pdf
27. "Subset selection with sparse matrices" (Del Pia, Dey, Weismantel), April 2018, SparseRegression4.pdf
28. "Convex integer programming model to obtain dual bounds for sparse PCA" (Dey, Mazumder, Wang), Discrete Optimization and Machine Learning, 2019, SPCA6.pdf
29. "Convexification of substructures in quadratically constrained quadratic program" (Dey, Kocuk, Santana), CRM, Oct 2019, QCQPSubstructureConvexification.pdf
30. "Convexification in global optimization" (Dey), IPCO 2020 summer school, June 2020, IPCOsummerschoolJune2020.pdf
31. "Sparse PSD approximation of the PSD cone" (Blekherman, Dey, Molinaro, Sun), Oct 2020, SparseSDP.pdf
32. "Lifting Convex Inequalities for Bilinear Programs" (Gu, Dey, Richard), July 2021, LiftingBilinear.pdf
33. "On obtaining the convex hull of quadratic inequalities via aggregations" (Dey, Munoz, Serrano), Sep 2021, ThreeQuads.pdf
34. "Theoretical and computational analysis of sizes of branch-and-bound trees" (Dey with Dubey, Molinaro, Shah), Oct 2021, Branch-and-Bound.pdf
35. "Aggregation of quadratic inequalities and hidden hyperplane convexity" (Blekherman, Dey, Sun), April 2023, HHCtalk.pdf
36. "Introduction to cutting planes for mixed integer linear (nonlinear) programs" (Dey), June 2024 (MIP 2024), CPMIP2024b.pdf
37. "Sensitivity analysis for mixed binary quadratic programming" (Cifuentes, Dey, Xu), Aug 2024, SensitivityTalk.pdf
38. "Lagrangian dual with zero duality gap that admits decomposition" (Cifuentes, Dey, Xu), Nov 2024, LagrangianDualTalk.pdf

**C. Recorded talks, auto-caption transcripts saved in `references/sources/talks/` (primary)**
39. IPCO Summer School 2020, Santanu Dey, Lecture 1, uploaded 2020-07-08, https://www.youtube.com/watch?v=alWp58SW-Hk
40. IPCO Summer School 2020, Santanu S. Dey, Lecture 2, uploaded 2020-07-08, https://www.youtube.com/watch?v=lIKaRZY-BTk
41. "Sparse PSD approximation of the PSD cone", Discrete Optimization Talks, uploaded 2020-10-24, https://www.youtube.com/watch?v=iIMYzJNCoos
42. "Sparse PSD approximation of the PSD cone", Waterloo Tutte Colloquium, 2020-12-11, https://www.youtube.com/watch?v=4lZdL3GHvgs
43. "Solving SDPs by using sparse PCA", IPAM Deep Learning and Combinatorial Optimization 2021, uploaded 2021-03-04, https://www.youtube.com/watch?v=yv0pHyrUZXo
44. "Santanu Dey - MIP International 2024" (strong duals for IPs), Mixed-Integer Programming Society channel, uploaded 2025-04-29, https://www.youtube.com/watch?v=JPgdFu8fD9U
45. "Strong duals for mixed integer programs", UW-Madison ISyE colloquium, uploaded 2025-10-06, https://www.youtube.com/watch?v=0OPWWIzfe4I

**D. Papers and preprints (primary; full text = introduction and conclusion read, abstract = arXiv abstract only)**
46. Dey, Molinaro, "Theoretical challenges towards cutting-plane selection", Mathematical Programming 170 (2018) 237-266, DOI 10.1007/s10107-018-1302-4, arXiv:1805.02782 (full text, homepage preprint 2018-05-07)
47. Dey, Lodi, Tramontani, Wolsey, "On the Practical Strength of Two-Row Tableau Cuts", INFORMS J. Computing 26 (2014) 222-237, DOI 10.1287/ijoc.2013.0559 (full text, preprint 2012-08-12)
48. Dey, Dubey, Molinaro, Shah, "A theoretical and computational analysis of full strong-branching", Mathematical Programming 205 (2024) 303-336, DOI 10.1007/s10107-023-01977-x, arXiv:2110.10754 (full text, homepage preprint 2021)
49. Dey, Dubey, Molinaro, "Branch-and-bound solves random binary IPs in poly(n)-time", Mathematical Programming 200 (2023) 569-587, DOI 10.1007/s10107-022-01895-4, arXiv:2007.15192 (abstract and introduction)
50. Dey, Dubey, Molinaro, "Lower bounds on the size of general branch-and-bound trees", Mathematical Programming 198 (2023) 539-559, DOI 10.1007/s10107-022-01781-z, arXiv:2103.09807 (abstract)
51. Shah, Dey, Molinaro, "Non-Monotonicity of Branching Rules with Respect to Linear Relaxations", INFORMS J. Computing 38 (2026) 53-66, DOI 10.1287/ijoc.2024.0709, arXiv:2402.05213 (full text)
52. Shah, Dey, "Improving Full Strong Branching Decisions by Incorporating Additional Information", arXiv:2507.09455, 2025 (abstract and introduction)
53. Becu, Dey, Qiu, Xavier, "Approximating the Gomory Mixed-Integer Cut Closure Using Historical Data", arXiv:2411.15090, 2024 (full text)
54. Dey, Molinaro, Wang, "Analysis of Sparse Cutting Planes for Sparse MILPs with Applications to Stochastic MILPs", Mathematics of Operations Research 43 (2018) 304-332, DOI 10.1287/moor.2017.0866, arXiv:1601.00198 (full text, preprint 2015-12-29)
55. Dey, Molinaro, Wang, "Approximating polyhedra with sparse inequalities", Mathematical Programming 154 (2015) 329-352, DOI 10.1007/s10107-015-0925-y (full text, preprint 2015-04-27)
56. Bodur, Del Pia, Dey, Molinaro, Pokutta, "Aggregation-based cutting-planes for packing and covering integer programs", Mathematical Programming 171 (2018) 331-359, DOI 10.1007/s10107-017-1192-x, arXiv:1606.08951 (full text, preprint 2016-06-26)
57. Dey, Iroume, Molinaro, Salvagnin, "Improving the Randomization Step in Feasibility Pump", SIAM J. Optimization 28 (2018) 355-378, DOI 10.1137/16M1095962, arXiv:1609.08121 (full text, preprint 2017-06-22)
58. Dey, Mazumder, Wang, "Using ℓ1-Relaxation and Integer Programming to Obtain Dual Bounds for Sparse PCA", Operations Research 70 (2022) 1914-1932, DOI 10.1287/opre.2021.2153, arXiv:1810.09062 (full text, preprint 2018-10-21)
59. Kocuk, Dey, Sun, "Strong SOCP Relaxations for the Optimal Power Flow Problem", Operations Research 64 (2016) 1177-1196, DOI 10.1287/opre.2016.1489, arXiv:1504.06770 (full text)
60. Dey, Kocuk, Santana, "Convexifications of rank-one-based substructures in QCQPs and applications to the pooling problem", J. Global Optimization 77 (2020) 227-272, DOI 10.1007/s10898-019-00844-4, arXiv:1902.00739 (full text, preprint 2019-02-02)
61. Dey, Pokutta, "Design and verify: a new scheme for generating cutting-planes", Mathematical Programming 145 (2014) 199-222, DOI 10.1007/s10107-013-0645-0 (introduction, preprint 2012-12-29)
62. Gupte, Ahmed, Cheon, Dey, "Relaxations and discretizations for the pooling problem", J. Global Optimization 67 (2017) 631-669, homepage PDF (introduction; journal metadata from the homepage, DOI not checked)
63. Dey, Munoz, Serrano, "On Obtaining the Convex Hull of Quadratic Inequalities via Aggregations", SIAM J. Optimization 32 (2022) 659-686, DOI 10.1137/21M1428583, arXiv:2106.12629 (abstract)
64. Blekherman, Dey, Sun, "Aggregations of Quadratic Inequalities and Hidden Hyperplane Convexity", SIAM J. Optimization 34 (2024) 98-126, DOI 10.1137/22M1528215, arXiv:2210.01722 (abstract)
65. Santana, Dey, "The Convex Hull of a Quadratic Constraint over a Polytope", SIAM J. Optimization 30 (2020) 2983-2997, DOI 10.1137/19M1277333, arXiv:1812.10160 (abstract)
66. Cifuentes, Dey, Xu, "Lagrangian dual with zero duality gap that admits decomposition", arXiv:2411.12085, 2024 (IPCO 2025) (abstract)
67. Cifuentes, Dey, Xu, "Sensitivity analysis for mixed binary quadratic programming", Mathematical Programming 216 (2026) 379-424, DOI 10.1007/s10107-025-02265-6, arXiv:2312.06714 (abstract)
68. Blekherman, Dey, Molinaro, Sun, "Sparse PSD approximation of the PSD cone", Mathematical Programming 191 (2022) 981-1004, DOI 10.1007/s10107-020-01578-y, arXiv:2002.02988 (abstract)
69. Dey, Molinaro, Wang, "How Good Are Sparse Cutting-Planes?", IPCO 2014, LNCS pp. 261-272, DOI 10.1007/978-3-319-07557-0_22, arXiv:1405.1789 (abstract)
70. Gu, Dey, Xavier, Qiu, "Exploiting Instance and Variable Similarity to Improve Learning-Enhanced Branching", arXiv:2208.10028, 2022 (abstract)

**E. Newsletter (primary and secondary)**
71. Dey, Tramontani, "Recent Developments in Multi-Row Cuts", Optima (Mathematical Programming Society Newsletter) 80, September 2009, pp. 2-8, http://www.mathprog.org/Optima-Issues/optima80.pdf (primary)
72. Cornuejols, Weismantel, Wolsey, "Comments on Multi-Row Cuts" (discussion column), Optima 80, September 2009, pp. 8-10, same URL (secondary; [observed])

**F. NSF award abstracts (NSF award API, https://api.nsf.gov/services/v1/awards/<id>.json; primary, authorship assumed)**
73. CMMI-1030422, "Collaborative Research: Fundamentals of Convex Mixed Integer Nonlinear Programming", PI Dey, 2010-09-01 to 2014-08-31
74. CMMI-1149400, "CAREER: Non-traditional Cutting-Plane Algorithms for Mixed-Integer Programs", PI Dey, 2012-08-01 to 2017-07-31
75. CCF-1415460, "Eager: Discrete Optimization Algorithms for 21st Century Algorithms", PI Nemhauser, co-PIs Vempala, Balcan, Dey, 2014-03-01 to 2017-02-28 (co-authored)
76. CMMI-1562578, "Sparse Integer Programming", PI Dey, 2016-08-01 to 2020-07-31
77. 2211343, "Frequency-Domain Model Updating through Branch and Bound with Convex Relaxation", PI Yang Wang, co-PI Dey, 2023-01-01 to 2027-12-31 (co-authored)

**G. News, prize and profile pages (secondary)**
78. ISyE news, "Santanu Dey Awarded Inaugural Egon Balas Prize", 2020-10-23, https://www.isye.gatech.edu/node/6817 (mirror: https://www.tlwarc.hg.gatech.edu/node/640512)
79. INFORMS, "Egon Balas Prize" recipients page, accessed 2026-10-10, https://www.informs.org/Recognizing-Excellence/Community-Prizes/Optimization-Society/Egon-Balas-Prize
80. INFORMS award recipient page "Santanu S. Dey", accessed 2026-10-10, https://www.informs.org/Recognizing-Excellence/Award-Recipients/Santanu-S.-Dey
81. ISyE faculty profile, accessed 2026-10-10, https://isye.gatech.edu/user/128 (education details; research described as "the design and evaluation of algorithms")
82. Georgia Tech research profile, accessed 2026-10-10, https://research.gatech.edu/santanu-dey
83. Georgia Tech ARC profile (undated), https://tlwarc.hg.gatech.edu/node/71321
84. MIT ORC seminar speaker bio, spring 2012, https://web.mit.edu/orc/www/archive/seminars/2012s/bio/Dey_bio.html
85. Georgia Tech ECE news, D. Watson, "ENVELOPE Project Aims to Revolutionize Management and Optimization of Large-Scale Electricity Systems", 2024-11-07, https://ece.gatech.edu/news/2024/11/envelope-project-aims-revolutionize-management-and-optimization-large-scale (no quote from Dey; role only)

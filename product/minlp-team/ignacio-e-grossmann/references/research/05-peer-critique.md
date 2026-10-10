# 05 · Peer critique: blind spots, limits of applicability, judgements shown wrong

> **Researcher**: Ignacio E. Grossmann, Carnegie Mellon University (Department of Chemical Engineering; Center for Advanced Process Decision-making, CAPD). DBLP 31/5106 · Google Scholar `fiZryxEAAAAJ` · ORCID 0000-0002-7210-084X.
> **Dimension**: research agent 05 of 06, peer critique (nuwa research-craft Phase 1; framework §二, agent 5: the blind spots of his methods, their limits of applicability, and judgements shown to be wrong).
> **Research date**: 2026-10-10
> **Sources consulted**: 96, listed under "Sources": 45 by critics, rival groups and third parties (C1–C41, W1–W4) and 51 by Grossmann and his co-authors (G1–G51). 90 are primary documents. Of these, 56 were read: 4 in full, 22 in part and 30 at abstract level. The other 34 were checked at metadata level only (DOI, title, authors, venue and year confirmed; content not read). 6 sources are secondary. 88 DOIs (6 of them CMU KiltHub DOIs, checked through DataCite) and 3 arXiv identifiers (arXiv API) were checked with a tool in this run. The 9 sources without an identifier (a 1981 proceedings paper, a conference extended abstract, three talks, three web pages, one software manual) were checked by fetching them, or for the 1981 paper through its Google Scholar entry. WebSearch: 4 of 4 calls used.
> **Method**: Crossref REST API for every DOI (48 in one batch, the rest by title search); DataCite for the six KiltHub DOIs; Springer landing pages (curl) and the Crossref, OpenAlex and Semantic Scholar APIs for abstracts; Google Scholar result pages through WebFetch for Elsevier and ACS abstracts that the APIs elide (ScienceDirect and pubs.acs.org returned HTTP 403 to both curl and WebFetch); the arXiv API; Unpaywall (noreply address) and the Wayback availability API for one blocked item; open copies on egon.cheme.cmu.edu, the CMU PASI 2008 course site and the NTNU mirror of AIChE proceedings; the GAMS DICOPT manual; Mittelmann's benchmark page; Wikipedia (two pages, low weight).
> **Local corpus**: no user-supplied material exists for this member. `references/sources/papers`, `essays` and `software` hold only `.gitkeep`. The transcripts in `references/sources/talks/` were saved during this workflow run by sibling agents 02, 04 and 06 from YouTube automatic captions: three when I started, five by the end, and I used three of them. They are not user-supplied, so nothing below is marked "from user-supplied material". `references/sources/private/` was not opened. I saved no new transcript.
> **Sibling downloads reused read-only**: some texts were downloaded earlier in this run by sibling agents into the shared scratch folder (`minlp-team-scratch/base-skills/`). I re-checked each identifier myself and read these copies: the KiltHub DRC/EDRC reports; the egon author copies; the open-access PDF of the 2019 solver review; the feasibility-pump preprint; the 2026 EJOR author copy; arXiv 2109.09657v3 (Grossmann's folder). I also read arXiv 2202.05198v3 (Misener's folder), the Burer–Letchford author copy (Burer's folder) and the Argonne preprint of the Acta Numerica survey (Leyffer's folder). The Argonne URL of that preprint returned HTTP 403 to my own curl request, so I could not re-download it.
> **Tags**: [stated] = what Grossmann said or wrote, co-authored texts included · [practice] = what the record shows (papers, code defaults, author lists, errata) · [observed] = what others wrote about his work: critiques, rival claims, benchmarks · [inferred] = my reading, with no source saying it. Each item also carries **P** (primary: the author's own text) or **S** (secondary: someone else's report of it).
> **Quoting**: quotations are verbatim from the copy named. Whitespace and line-end hyphenation were normalized. Mathematical symbols lost in PDF text extraction are flagged in brackets, for example "2n [2^n; superscript lost in extraction]". The 2024 interview and the 2025 lecture exist only as YouTube automatic captions: quotes from them reproduce the ASR text exactly, errors included, are marked *(ASR, h:mm:ss)*, and are glossed outside the quotation marks. Some abstracts were read only as displayed on a Google Scholar results page fetched through WebFetch. WebFetch passes the page through a small model, so those quotes are marked *(Scholar listing via WebFetch)*. Treat them as near-verbatim until they are checked against the publisher page.

---

## 0. Overview: what the critics established, and whether it was answered

| # | Target | Critic (year) | What the critique established | Answered? |
|---|---|---|---|---|
| 1 | Outer approximation (OA, 1986): scope | Fletcher & Leyffer (1994) | Restricted to problems linear in the integers. Infeasible NLP subproblems needed a rigorous treatment. A worst-case example visits all integer assignments | Yes: the Fletcher–Leyffer variant is now the reference OA in his group's 2026 history. DICOPT's default still adds only an integer cut after an infeasible NLP (§1.1) |
| 2 | OA: iteration count | Hijazi, Bonami & Ouorou (2014); Belotti et al. (2013); Lubin et al. (2018) | A simple, infeasible convex instance forces 2^n iterations; lifting (extended formulations) cures it | Partly: his group's 2019 and 2026 reviews cite Hijazi et al. for lifting gains, but neither mentions the worst case. Regularized OA (2020) targets the number of iterations (§1.2) |
| 3 | OA: smoothness and constraint qualifications | Eronen, Mäkelä & Westerlund (2014); Lubin et al. (2018) | Subgradient OA can fail on nonsmooth convex MINLP (counterexample). When constraint qualifications (CQs) fail, no polyhedral outer approximation suffices | Accepted as a scope limit ("guaranteed convergence for smooth problems", 2019). The remedies came from the critics' groups (§1.3) |
| 4 | OA/ER/AP and DICOPT on nonconvex MINLP | Belotti et al. (2013); Burer & Letchford (2012); GAMS manual; Kesavan et al. (2004) | A heuristic with no global guarantee; rigorous alternatives exist | Never contested: Grossmann said so himself in 1987–88. His group later built a separate, rigorous global-optimization line (e.g., Lee & Grossmann 2001) (§1.4) |
| 5 | LP/NLP-BB (1992) | Abhishek, Leyffer & Linderoth (2010) and later solver builders | It pays off only inside modern MILP machinery (cuts, heuristics, callbacks) | Yes, through others' implementations. The 2019 review endorses single-tree solvers; the 2026 history reports little difference from an accelerated multi-tree OA (§1.5) |
| 6 | DICOPT in practice | Castillo et al. (2005, as relayed by Bernal et al. 2020); the 2019 co-authored benchmark | Very poor on a block-layout instance; trouble finding feasible points; weaker on highly nonlinear problems | A feasibility pump was added (2019/2020). No current independent benchmark that includes DICOPT was found (§2) |
| 7 | GDP: the hull reformulation | Kronqvist, Misener & Tsay (2021, 2025); Bonami et al. (2015); Vielma (2015) | Hull formulations are large and numerically harder; there is a "folklore observation" that they perform worse than expected | Yes: improved big-M (2015), ε-approximations (2007, 2020), conic forms (2024). P-split is now a Pyomo.GDP plugin (§3) |
| 8 | Superstructure synthesis as a programme | FOCAPD 1980 keynote (Stephanopoulos, identification inferred); pinch-analysis school (Linnhoff, identification inferred); referees | "We don't know how to solve these problems": heuristics and thermodynamic targets were held to be better | Answered in reports of 1983–1990 and by later results. In 2019 he presents pinch analysis as the commercial success story (§4.1–4.3) |
| 9 | Superstructure completeness; SYNHEAT assumptions | Voll et al. (2012); Björk & Westerlund (2002) | The optimum is limited to the superstructure given in advance. SYNHEAT's isothermal-mixing assumption can exclude optimal configurations | The first limit was stated by Grossmann himself in 1983. No answer to the isothermal-mixing point was found (§4.4–4.5) |
| 10 | MINLP process synthesizer (1992) | Salcedo (1992) | A published comment (not read), from the author of a rival adaptive random search | A published response exists (1992; not read) (§4.6) |
| 11 | Flexibility analysis (1983–85) | Saboo & Morari (1984); Floudas, Gümüş & Ierapetritou (2001) | Critical points need not be vertices; the KKT-based active-set method is not global for nonconvex models | Yes: active-set MILP/MINLP (1987); the global approach of his former student, which he praised in 2014 (§5) |
| 12 | Continuous-time scheduling models | Sundaramoorthy & Karimi (2005); Floudas & Janak (2005 comment); Shaik et al. (2006); Floudas & Lin (2004) | Rival formulations claimed to be simpler, faster or more general; a Méndez et al. (2001) model beat a Pinto–Grossmann (1995) solution | No reply found (§6) |
| 13 | Industrial deployment | co-author Harjunkoski (ABB, 2019); plant operators (as he reports in 2025) | Hand-over and "PhD-free" maintenance; proving value; operators ask why they should believe a solution is optimal | Stated as open challenges (§7) |
| 14 | Published numbers | the Duran–Grossmann erratum (1987) | A reported optimum was suboptimal | Self-corrected (§8) |

---

## 1. Outer approximation and its descendants

### 1.1 Fletcher & Leyffer (1994): generality, infeasibility and the worst case

- **Critics**: Roger Fletcher and Sven Leyffer (University of Dundee numerical analysis; team.json gives Leyffer's PhD as Dundee with Fletcher). **Source**: C1, abstract read on the Springer page. [observed, P]
- **What they wrote**: "Duran and Grossmann (1986) suggest an outer approximation scheme for solving a class of MINLPs that are linear in the integer variables by a finite sequence of relaxed MILP master programs and NLP subproblems. Their idea is generalized by treating nonlinearities in the integer variables directly, which allows a much wider class of problem to be tackled, including the case of pure INLPs. A new and more simple proof of finite termination is given and a rigorous treatment of infeasible NLP subproblems is presented which includes all the common methods for resolving infeasibility in Phase I. The worst case performance of the outer approximation algorithm is investigated and an example is given for which it visits all integer assignments. This behaviour leads us to include curvature information into the relaxed MILP master problem, giving rise to a new quadratic outer approximation algorithm."
- **Scope the critique addresses**: the 1986 abstract (G1) itself names its class: "Linearity of the integer (or discrete) variables, and convexity of the nonlinear functions involving continuous variables are the main features in the underlying mathematical structure." [stated, P]
- **Context**: OA was built in 1983–86 for chemical-engineering design models (binary unit selections entering linearly), tested on small problems with IBM's MPSX and MINOS (see 01). The 1994 critique came from the SQP/filter numerical-analysis school, which judges an algorithm by its proofs and worst cases rather than by application test sets. [practice, P; the framing is inferred]
- **Answered?** Largely adopted.
  - The 2026 history he co-wrote (G15): "The algorithm was revised by Fletcher and Leyffer (1994), and the algorithm is today commonly referred to as outer-approximation." [stated, P]
  - Also in G15: "In Duran and Grossmann (1986) infeasible integer assignments were excluded from (OA-master) by adding no-good cuts. Instead of no-good cuts, Fletcher and Leyffer (1994) proposed a method to solve a feasibility problem that selects the [symbol lost] variables by minimizing the constraint violation for the specific integer assignment and generating gradient cuts at the solution. The resulting gradient cuts are generally stronger, as the no-good cuts only exclude a single integer assignment." [stated, P]
- **But DICOPT's default keeps the 1986 treatment** [practice, P]. The feasibility-pump paper (G13): "If the NLP subproblem (NLPi) is infeasible, DICOPT by default adds only an integer cut to eliminate the current fixing y = y^i from (rMIPi), but does not add the corresponding linearizations of nonlinear functions". The reason given: "This option is sufficient to avoid visiting the same solution point again while avoiding adding linearizations which are not supporting hyperplanes for nonconvex MINLPs. However, it also exhibits slower progress as less information is made available to the master problem." The GAMS manual (W1) on the option `infeasder 1`: "This option is recommended to speed up convergence when the MINLP is known to be convex (i.e. its continuous relaxation is convex). The possibility of cutting-off the global optimum is increased if it is used for a nonconvex MINLP."
- [inferred] In his own solver, the code's nonconvex use case outranked the stronger convex theory: the improvement is available as an option, and the default protects nonconvex users.

### 1.2 The worst case: 2^n iterations on a simple instance

- **Critics**: Hassan Hijazi, Pierre Bonami and Adam Ouorou (C2, *INFORMS J. Comput.* 2014; preprint 2010). **Source**: abstract (Crossref). [observed, P] "As a side result, we exhibit a simple example where a classical implementation of the outer approximation would take an exponential number of iterations, whereas it is easily solved with our modifications." The modifications are "a simple extended formulation", "a refined outer approximation" and "a heuristic inner approximation"; "These methods have been implemented in the open source solver Bonmin".
- **Restated by the Acta Numerica survey** (C3, Belotti, Kirches, Leyffer, Linderoth, Luedtke & Mahajan; Clemson, Heidelberg, Argonne and Wisconsin–Madison per the preprint's title page; read in the preprint ANL/MCS-P3060-1121 of 22 Nov 2012). [observed, P]
  - "Worst-case complexity of outer approximation. In practice, outer approximation often works efficiently. However, Hijazi et al. (2010) provide an example where outer approximation takes an exponential number of iterations."
  - On the instance, an infeasible problem asking for a binary point inside a ball centred at (1/2, …, 1/2): "The authors show that any outer approximation cut cannot cut more than one vertex. Thus, outer approximation must visit all 2n [2^n; superscript lost in extraction] vertices of the hypercube. The example generalizes to Benders decomposition and extended cutting plane methods, because these methods are relaxations of outer approximation."
- **Restated by Lubin, Yamangil, Bent & Vielma** (C4, read in arXiv 1607.03566v2). [observed, P]
  - "The cases in which the OA algorithm and others based on polyhedral approximation perform poorly are those in which the convex set of constraints is poorly approximated by a small number of half-spaces. In Section 3, we review a simple example identified by Hijazi et al. [28] where the OA algorithm requires 2n [2^n] iterations to solve an MICP instance with n decision variables."
  - On the cure: "implementing these techniques within traditional MICP solvers requires more structural information than provided by "black-box" oracles through which these solvers typically interact with nonlinear functions."
  - On the field as a whole, citing a review by Bonami, Kılınç & Linderoth (C13; not read, quoted here secondhand): "continued advances in MILP have translated into "far more modest" growth in the scale of problems which MICP solvers can solve within reasonable time limits." [observed, S for the inner quote]
- **Context**: these critics come from operations research and numerical optimization: the Bonmin solver team (2010 preprint, 2014 paper), the Acta Numerica survey team (2012–13), and the authors of the Pajarito solver written in Julia (2016–18). Their test of an algorithm is its behaviour on adversarial or structured instances, and their cure is a modelling-layer change: disciplined convex programming and conic forms. Fletcher & Leyffer had already shown a worst case in 1994 (§1.1).
- **Answered?** Partly, and selectively. [practice, P; the assessment is inferred]
  - The 2019 review (G12): "Lifted reformulations of MINLP problems have also been studied by Hijazi et al. (2013), and Lubin et al. (2016)."
  - The 2026 history (G15): "With some formulations, it is easier to construct a strong polyhedral approximation. This is described in detail in Hijazi, Bonami, and Ouorou (2014), Kronqvist, Lundell, and Westerlund (2018) and Tawarmalani and Sahinidis (2005)."
  - Both reviews cite the critics for the **remedy**. A text search found no mention of the **worst case** in either: "exponential number" has 0 hits in the 2026 author copy, and "worst" appears in the 2019 review only as "virtual worst" (solver). The 2026 history keeps the positive summary "The algorithm is easy to grasp and implement, yet computationally efficient." (see Contradiction 1).
  - His group's regularized OA (G14, abstract) addresses iteration counts generically: "The main idea behind the methods is to choose the integer combination more carefully at each iteration, in order to obtain the optimal solution in fewer iterations compared to the original outer approximation method." Whether that paper discusses the 2^n example was **not read**.

### 1.3 Smoothness and constraint qualifications

- **Eronen, Mäkelä & Westerlund** (C5, *Optimization* 63(7), 2014; abstract via OpenAlex; Westerlund heads the Åbo Akademi cutting-plane school, §2.4). [observed, P] "It is shown through a counterexample that this type of generalization is insufficient with certain versions of the outer approximation algorithm." Here "this type of generalization" means replacing gradients by subgradients. "However, with some modifications to the outer approximation method a special type of nonsmooth functions for which the subdifferential at any point is a convex combination of a finite number of subgradients at the point can be considered." The same paper proves convergence for the rival extended cutting plane method (ECP).
- **Lubin et al.** (C4) on constraint-qualification failure. [observed, P]
  - "an example in Section 6 of what may happen when the assumptions of the OA algorithm fail: an MICP instance for which no polyhedral outer approximation is sufficient."
  - "This example strengthens the observation by [29] that MISOCP solvers may fail when certain constraint qualifications do not hold. In fact, no approach based on straightforward polyhedral approximation can succeed." Reference [29] is Hijazi & Liberti 2016 (C6, metadata only).
- **Answered?** Accepted as a scope limit, not extended. The 2019 review (G12) [stated, P]: "There has recently been an interest in nonsmooth convex MINLP, and some solution techniques have been presented see e.g., Eronen et al. (2017) and Eronen et al. (2014). However, most of the commonly available solvers only have guaranteed convergence for smooth problems". The remedies listed in the 2026 history come from the Åbo Akademi group (Eronen, Westerlund, Mäkelä), which is also his collaborator network (Kronqvist co-authors both reviews). [practice]

### 1.4 Nonconvex MINLP: OA/ER/AP and DICOPT are heuristics

- **What Grossmann himself said from the start** [stated, P]:
  - Kocis & Grossmann 1987 (G4, EDRC-06-37-87): "When the MINLP problem exhibits nonconvexities that cannot be transformed to a form that satisfies the above sufficient conditions, as is commonly the case in flowsheet synthesis problems, there is the possibility that the OA/ER algorithm may produce suboptimal solutions."
  - Kocis & Grossmann 1988 (G5, EDRC-06-43-88), on the two-phase strategy: "However, no rigorous guarantee on global optimality can be given since no special structure on the functions has been assumed to guarantee validity of the modified outer-approximations and uniqueness of the solutions of the NLP subproblems." The evidence offered was that "the global optimum was found in 24 out of 28 cases".
- **The title problem** [practice, P; the reading is inferred]. The journal version of the 1987 report is titled "Global optimization of nonconvex mixed-integer nonlinear programming (MINLP) problems in process synthesis" (G6, 1988). From the mid-1990s, "global optimization" came to mean methods that come with a guarantee. Examples: the rigorous decomposition of Kesavan et al. (C7: "On finite termination, the first yields the global solution to the original nonconvex MINLP and the second finds a rigorous bound to the global solution") and αBB for MINLP (C16). By that later standard the 1988 title overstates a method that its own report calls non-rigorous.
- **How peers classify his nonconvex tools** [observed, P]:
  - Belotti et al. (C3): DICOPT "implements a variant of outer approximation (Section 3.2.1), which has been generalized to tackle nonconvex MINLPs through a penalty function heuristic; see (Viswanathan and Grossmann, 1990)."
  - Burer & Letchford (C14, author copy): "Some packages can be used to find heuristic solutions for non-convex MINLPs: BONMIN, DICOPT, LaGO, and MIDACO. The first three are actually packages for convex MINLPs, while the fourth is based on ant-colony optimization."
  - GAMS manual (W1; maintained by GAMS, a third party since DICOPT passed to them): "Although the algorithm has provisions to handle non-convexities, it does not necessarily obtain the global optimum."
- **Rival rigorous routes** [observed, P]:
  - Kesavan, Allgor, Gatzke & Barton (C7, MIT): "A rigorous decomposition approach to solve separable mixed-integer nonlinear programs where the participating functions are nonconvex is presented." Their "numerical results are compared with currently available algorithms"; whether this includes OA/ER/AP was **not read**.
  - Westerlund & Pörn (C8, Åbo): "a class of non-convex MINLP problems with a pseudo-convex objective function and pseudo-convex constraints, can be solved to global optimality with the considered cutting plane technique."
  - Adjiman, Androulakis & Floudas (C16; Floudas was Grossmann's PhD student) proposed "Two novel deterministic global optimization algorithms for nonconvex mixed-integer problems".
  - Ryoo & Sahinidis (C15; Sahinidis was also his PhD student): only the first abstract sentence was read; whether they report that earlier local solutions of process-design test problems were suboptimal was **not verified**.
- **His later statements**: he concedes the point and stops short of calling the heuristics wrong.
  - 2019 review (G12) [stated, P]: "Both methods are intended as heuristics for nonconvex MINLP problems, although if the equality constraints relax as convex inequalities the methods become rigorous."
  - 2026 history (G15) [stated, P], on equality relaxation, augmented penalty and feasibility restoration: "These techniques are not guaranteed to find an optimal solution, but in practice they often improve the ability to find good solutions for nonconvex problems."
  - 2019 retrospective (G42) [stated, P] credits the rivals by name: "Kesavan, Allgor, Gatzke and Barton (2004) at MIT developed an Outer Approximation algorithm for nonconvex MINLP."
- **His own rigorous line** [practice, P; metadata only]: global GDP (Lee & Grossmann 2001, G19), Lagrangean branch-and-cut for decomposable nonconvex MINLP (Karuppiah & Grossmann 2008, G20), and reviews of global GDP (Ruiz & Grossmann 2017, G21).
- **Context**: OA/ER/AP was designed in 1986–90 and run on an IBM-3090 (G5, G8). That was before the deterministic global solvers his 2019 retrospective credits: it dates BARON to "Ryoo and Sahinidis (1996) and Tawarlamani and Sahinidis (2002)" (G42, spelling as printed). Whether any general global MINLP code existed in the 1980s was not checked. [practice, P]

### 1.5 LP/NLP-based branch and bound (Quesada & Grossmann 1992)

- **Critics and builders**: Abhishek, Leyffer & Linderoth (C12, FilMINT, 2010; abstract via Crossref). [observed, P]
  - The algorithm is "based on an algorithm of Quesada and Grossmann [...] that avoids the complete re-solution of a master mixed-integer linear program (MILP) by adding new linearizations at open nodes of the branch-and-bound tree whenever an integer solution is found."
  - "The MINTO framework allows us to easily employ cutting planes, primal heuristics, and other well-known MILP enhancements for MINLPs. We present detailed computational experiments that show the benefit of such advanced MILP techniques."
  - "By carefully incorporating and tuning all these enhancements, an effective solver for convex MINLPs is constructed."
  - [inferred] The implicit critique: the 1992 idea becomes effective only inside a full MILP branch-and-cut code, which a chemical-engineering group could not build in 1992. The payoff came when MILP solvers exposed callbacks.
- **Reception**: Belotti et al. (C3) [observed, P]: "Introduced by Quesada and Grossmann (1992), LP/NLP-based branch-and-bound (LP/NLP-BB) methods have emerged as a powerful class of algorithms for solving convex MINLPs."
- **His group's two readings** (see Contradiction 2) [stated, P]:
  - 2019 (G12): "For the test set considered here, SHOT and AOA were the overall fastest solvers. Both of the solvers are based on a single-tree approach closely integrated with the MILP solver by utilizing callbacks to add the linearizations as lazy constraints. The results show the benefits of such a solution technique and support the strong belief in the single-tree approach by Abhishek et al. (2010) and Belotti et al. (2013)."
  - 2026 (G15): "A single-tree version of an OA-algorithm is typically faster than a "vanilla" multi-tree variant. [...] With acceleration techniques, the computational result in Lundell et al. (2022) shows little performance difference between the multi- and single-tree variants."

---

## 2. DICOPT under scrutiny

### 2.1 Failure to find feasible points

- **A peer report, relayed by his group.** Castillo, Westerlund, Emet & Westerlund (C40, *Comput. Chem. Eng.* 30(1), 2005) built the block-layout model that G13 identifies in MINLPLib as instance o7_2. As Bernal, Vigerske, Trespalacios & Grossmann report it (G13, preprint of 12 Aug 2019): "The authors of the model used several MINLP solvers to find the optimal solution to this problem, among them DICOPT. DICOPT performed very poorly because the linearizations in the initial outer-approximation (rMIPi) were not helpful and many nonlinear subproblems (NLPi) are infeasible [8]." [observed, S: the original 2005 text was **not read**]
- **His group's own diagnosis** (G13) [stated, P]:
  - "However, it has been observed that DICOPT has difficulties solving instances in which some of the nonlinear constraints are so restrictive that nonlinear subproblems generated by the algorithm are infeasible."
  - "For some problems, DICOPT has difficulty in finding a feasible solution. The main reason for this is that by default, and to address nonconvex problems, DICOPT does not include linearizations of nonlinearities from infeasible NLPs into the MIP."
- **Answered?** Yes, by a feasibility pump used as preprocessing, developed with GAMS (Vigerske) and ExxonMobil (Trespalacios); 2019 preprint, 2020 journal version. Context: about 30 years after DICOPT's first release (1988 per G13: "DICOPT (Discrete Continuous Optimizer) is an MINLP solver that has been developed in 1988."). [practice, P]

### 2.2 The default stopping rule

- **GAMS manual** (W1) [observed, P]: "Another stopping criterion that tends to work very well for non-convex problems (and even for convex problems) is based on the heuristic: stop as soon as the NLP subproblems start worsening (i.e. the current NLP subproblem has an optimal objective function that is worse than the previous NLP subproblem)."
- **His group in 2019/2020** (G13) [stated, P]: "For nonconvex MINLPs, valid lower bounds and solving (NLPi) to global optimality are not ensured. Therefore, by default DICOPT stops as soon as the upper bound ZU stops improving. Although it is a heuristic, this stopping criterion has shown that in many cases it yields optimal or near optimal integer solutions. For the computational experiments in this paper, we have set option stop to 1." Option `stop 1` is the gap-closing criterion. The 2019 benchmark (G12) likewise used "a convex strategy, or recommended convex parameters" where available.
- [inferred] The manual recommends the heuristic stop "even for convex problems", while the group's own experiments on convex instances switch it off (Contradiction 3). In the 1988 report (G5) the stop was confined to the second phase, entered only after nonconvexities had been detected. The report says: "If nonconvexities are not detected the search is terminated. Otherwise, one proceeds to a second phase [...] Here the search is terminated at the point when no further improvements are found in the NLP subproblems." Today the same rule is the default for every user.

### 2.3 The 2019 benchmark (co-authored, so not independent)

- **Source**: Kronqvist, Bernal, Lundell & Grossmann (G12; published open-access version read).
- **Setup**: 335 convex MINLPLib instances (the June 2018 preprint used 366; see Contradiction 4). "Linux-based PC with an Intel Xeon 3.6 GHz processor with four physical cores (able to process eight threads at once) and 32 GB memory". "a wall clock time limit of 900 s". Default settings, apart from listed options. Problems counted as solved within a 0.1% gap computed by PAVER. [practice, P]
- **DICOPT's place** [practice, P, read from Table 3]:
  - DICOPT reaches the 290-solved column (457 s per problem) but not the 300 column.
  - "SHOT is able to solve the most problems out of the MILP decomposition-based solvers (312), closely followed by AOA (310) and Muriqui (301)"; "BARON is able to solve the most instances (306)" among branch-and-bound solvers; "The virtual best solver is able to solve 326 of the problems".
- **Qualitative verdicts** [stated, P]:
  - "For example, for the problems with a low degree of nonlinearity DICOPT is overall one of the fastest solvers. For the problems with a high degree of nonlinearity DICOPT also performs well, but not as well as in the other category".
  - On BONMIN-OA, DICOPT and SCIP: "However, for problems with a high degree of nonlinearity they are outperformed by the NLP-BB-based solvers BONMIN-BB, Knitro-BB, Minotaur-BB, and SBB."
  - "without adding the CONOPT option specified below, DICOPT and SBB fails to solve all the smallinv-instances in MINLPLib."
  - On the test set itself: "it should be noted that many of the test instances are quite small and simple compared to industry-relevant problems."
- **Conflict of interest** [practice, P; inferred]: the SHOT authors (Kronqvist, Lundell) are co-authors. DICOPT is maintained by GAMS (W1: "Currently, DICOPT is maintained by GAMS"), and Grossmann's group still develops it (the feasibility pump of G13 was implemented in DICOPT with GAMS's Vigerske). The review states "Note that we have not tried to fine-tune any of the solvers". No external replication was found.
- **Independent public benchmark** [observed, P]: Mittelmann's MINLP page (W2, dated 26 Feb 2026) reads: "The following codes were run through GAMS with a limit of 2 hours on the 200 MINLPlib instances [...] on an AMD Ryzen 9 5900X (12 cores, 128GB). All problems were solved GLOBALLY. BARON, Gurobi, LINDO, SCIP, SHOT, XPRESS." DICOPT is not on the list. [inferred] The reference independent benchmark has moved to global solvers; a current, independent head-to-head test of DICOPT was not found (see Gaps).

### 2.4 Rival claims from the Åbo Akademi school

[observed, P]
- Kronqvist, Lundell & Westerlund (C10, ESH): "Compared to the extended cutting plane algorithm ESH generates a tighter overestimated set and unlike outer approximation the generation point for the supporting hyperplanes is found by a simple line search procedure."
- SHOT (C11): "This enables the MIP solver to reuse the branching tree in each iteration, in contrast to most other POA-based methods."
- Westerlund & Pettersson's ECP (C9; metadata only) is the original rival. Its abstract was not readable, so its argument against OA's NLP subproblems is **not read**.
- [practice] This rival school became a collaborator: Kronqvist is co-author of the 2019 review and the 2026 history, and Grossmann holds an honorary doctorate from Åbo Akademi (04).

---

## 3. Generalized disjunctive programming: big-M versus the hull

### 3.1 The hull's cost and numerics

- **Kronqvist (KTH), Misener & Tsay (Imperial)**: C18, read in arXiv 2202.05198v3; *Math. Program.* 218, 2025. [observed, P]
  - "Disjunctive programming was pioneered by Balas [4, 5, 6, 8] and generalized by Grossmann and coworkers [29, 44, 56, 58, 65]. [...] However, the best encoding of a disjunctive program, or disjunctive constraint(s), as an MIP is an open question."
  - "The big-M formulation also preserves the constraint expressions, whereas the extended convex hull builds upon the perspective function, which can result in numerically more challenging constraints."
  - "But the computationally simpler subproblems of the big-M formulation can offset the larger number of explored nodes. Anderson et al. [2] mention a folklore observation that extended convex hull formulations tend to perform worse than expected. The observation is supported by past numerical results [2, 41, 66, 69], as well as this paper."
  - Reference [66] in that list is Trespalacios & Grossmann 2015, *INFORMS J. Comput.* (G24). The critics cite **his own group's results** as support for the folklore. Reference [2] is Anderson et al. 2020 (C19, metadata only).
  - "Linearizing the disjunction allows us avoid the numerical difficulties related to division by zero arising from forming the convex hull of a general nonlinear disjunction [60]." Reference [60] is Sawaya & Grossmann 2007 (G22, metadata only).
- **The conference version** (C17, CPAIOR 2021, abstract): "The computational results show that the intermediate P-split formulations can form strong outer approximations of the convex hull with fewer variables and constraints than the extended convex hull formulations, giving significant computational advantages over both the big-M and convex hull." [observed, P]
- **Bonami, Lodi, Tramontani & Wiese** (C20, abstract) [observed, P]: "In the case of convex functions, the theory of disjunctive programming allows one to formulate these logical implications as convex nonlinear programming problems in a space of variables lifted with respect to its original dimension. We concentrate on the attempt of avoiding the issue of dealing with large NLPs." They also report: "Computational experiments comparing disjunctive programming formulations in the original space of variables with straightforward bigM ones show that the former are computationally viable and promising."
- **Vielma** (C21, abstract), on MIP formulations generally [observed, P]: "in some cases the resulting MIP can be either too weak or too large to be effectively solved by state of the art solvers."
- **Context**: these critiques arrive from 2015 to 2025, when MIP solvers handle big-M and indicator constraints well, and machine-learning applications (trained ReLU networks, clustering) supply new disjunctive test sets. The hull's case had been built in 2000–2003 on process-network and batch-plant models solved by NLP-based branch and bound. [practice; the contrast is inferred]

### 3.2 What Grossmann's line claimed, and what it later conceded

[stated, P]
- **Claim** (G16, Grossmann & Lee 2003, abstract): the hull relaxation "is used to formulate the GDP problem as a Mixed-Integer Nonlinear Programming (MINLP) problem that is shown to be tighter than the conventional "big-M" formulation."
- **The trade-off, stated by his group** (G23, Trespalacios & Grossmann 2015, egon copy): "The reformulation of GDP models to MILP/MINLP problems is typically performed by using either the Big-M (BM) or the Hull-Reformulation (HR), where the former generates a smaller MILP/MINLP, while the latter generates a tighter one". The same text concedes that "GDPs are normally reformulated as MILP/MINLP [...] to exploit the developments in these solvers".
- **The perspective function's numerics** (G25, Furman, Sawaya & Grossmann 2020, abstract): "However, there are a number of challenges in using this characterization in computation which prevents its wide-spread use, including issues that arise because of the functional form of the perspective function."
- **The 2026 history** (G15) says the perspective functions "are known to cause numerical problems" and are "not differentiable at" zero (symbols lost in extraction).

### 3.3 Answers

[practice, P]
- **Improved big-M**: G23, abstract: "The proposed MINLP reformulation is stronger than the traditional Big-M, and it does not require additional variables or constraints." Tested "with an NLP-based branch and bound method".
- **ε-approximations of the perspective**: G22 (2007, not read) and G25 (2020).
- **Conic forms**: Bernal Neira & Grossmann 2024 (G26, arXiv 2109.09657v3): "Moreover, in the case of the HR, we avoid numerical challenges derived from the perspective reformulation of nonlinear functions that appear when using scalar nonlinear constraints in the disjunctions." The paper also concedes: "solvers based on nonlinear B&B [...] such as KNITRO, can worsen their performance when using the conic reformulation. The non-differentiability of the cones, together with the larger subproblem sizes, can cause such a negative impact."
- [inferred] The conic route had been opened from the OR side more than a decade before the cones preprint (arXiv 2109.09657, 2021). Günlük & Linderoth (C24, 2010) showed "that for many classes of problems, the convex hull can be expressed via conic quadratic constraints, and thus relaxations can be solved via second-order cone programming".
- **Absorption of the critique**: the P-split paper (C18) reports that its two-term formulations "are now a Pyomo.GDP [22] plugin". Pyomo.GDP (G27) is his group's modelling platform. The rival remedy became part of his ecosystem. [observed, P]

### 3.4 Attribution of the nonlinear hull

[stated/observed, P]
- His own 2003 abstract (G16) credits the OR side: "Based on the work by Stubbs and Mehrotra [21] and Ceria and Soares [6], we propose a convex nonlinear relaxation".
- Ceria & Soares (C23, 1999): "We derive an algebraic characterization of the feasible region in a higher-dimensional space and propose a solution procedure akin to the interior-point approach for convex programming."
- [inferred] The nonlinear convex-hull characterization is OR's. Grossmann's contribution is the modelling framework (GDP, logic plus disjunctions) and its application to process systems. Peers credit him in exactly those terms ("generalized by Grossmann and coworkers").

---

## 4. Process synthesis by superstructure optimization

### 4.1 The FOCAPD 1980 keynote: "a Utopia"

- **His account** (G43, 2024 interview) [stated, P; ASR]:
  - *(ASR, 0:47:29)*: "one of the keynote speakers had a presentation with the title was process synthesis a Utopia in mathematical programming or an adventure in heuristics that was the title of the talk and then when he gave a talk the initial part was actually all taken from"
  - *(0:47:59)*: "my paper [...] but then he said well you know what is the problem with that the problem we don't know how to solve these problems so what's the point why waste our time". The paper is presumably Grossmann & Santibanez 1980 (G33), written in Mexico with an MILP code; identification [inferred].
  - *(0:48:30)*: "very fortunately both my PhD advisor Roger Sergeant was there and so was actually a professor from MIT Larry Evans so there was a they debated to you know the speaker". ASR: Sergeant = Roger Sargent. Then: "it was also motivation for us to try to see well can we prove him to be wrong".
  - Afterwards the speaker told him privately *(0:51:38)*: "it's very clear that you like math maybe what you should do is to do research in process control not in you know process".
- **Identifying the critic** [inferred, on two pieces of evidence]:
  - Google Scholar lists "Synthesis of process flowsheets: an adventure in heuristic design or a utopia of mathematical programming?" by G. Stephanopoulos, *Foundations of Computer-Aided Chemical Process Design*, Engineering Foundation, New York, 1981 (C25; citation entry only, text **not read**).
  - His 1989 report (G7) places "the FOCAPD meeting in 1980, where the first session on process synthesis took place" and cites "Stephanopoulos, 1981" for the "advantages and limitations" of the three approaches.
  - The critic's own argument is known only through Grossmann's memory.
- **His written answers** [stated, P]:
  - 1983 (G3, DRC-06-59-83, "Mixed-integer programming: is it a useful tool in process synthesis?", AIChE Diamond Jubilee Meeting): "In the recent past it is the first two approaches that have received most of the attention due to apparent limitations and failures with optimization techniques. It is the purpose of this paper to show that algorithmic methods can indeed play a very useful role in process synthesis."
  - 1989 (G7, EDRC 06-59-89): "At the FOCAPD meeting in 1980, where the first session on process synthesis took place, heuristics and thermodynamic targets were dominant due to the skepticism and little hope that there was with the mathematical programming approach. At this point in time, however, we have evolved to a state where the modelling and solution of large-scale MINLP problems for synthesis can no longer be regarded as a Utopia."
  - 1990 (G8, EDRC 06-83-90) repeats this and adds: "Results by our group at Carnegie Mellon, and by other researchers clearly have shown that much improved designs can be obtained with the use of MINLP models."
  - 2024 *(ASR, 0:50:37)*: "it's very interesting to see what it took to overcome that perception that approach problems through mixed inter programming was basically a lost cause and I'm happy to say that you know well they were all proved to be wrong". ASR: mixed inter = mixed-integer.
- **Context**: in 1980 Grossmann had been at CMU for about a year (since 1979, per 02), after his Imperial College PhD (1977) and a stay in Mexico City. There he used an MILP code the captions render as "univ fmps" (UNIVAC FMPS, inferred). On the software of the time he says *(ASR, 0:45:24)*: "the um optimization software was nowhere near what is now for example especially say mix integer linear programming". [stated, P] The critique was a judgement about solvability. [inferred] Solver progress over the next decade falsified it, and OA was part of that progress.

### 4.2 The pinch-analysis school

- **His account** *(ASR, 0:45:57–0:46:28)* [stated, P]: "especially in the area of feed exchanger networks there was a professor who actually did his PhD at leads in the UK he was actually German and he was advocating what was called at the time pinch technology pinch analysis the idea was to use main arguments based on thermodynamics using graphical representations to solve those problems". ASR: feed exchanger = heat exchanger; leads = Leeds.
- **Identifying the critic** [inferred]: Wikipedia (W3, S): "Born in Berlin, Germany, Linnhoff [...] went to University of Leeds, UK, as a British Council Scholar. There he gained a PhD in chemical engineering (1979)." That fits Bodo Linnhoff. His own published criticism of mathematical programming was **not found** (see Gaps).
- **His counter-critique, 1983** (G3) [stated, P]:
  - On targets: "The main drawback in this approach is that capital cost considerations cannot be properly accounted for since this can only be done by artifically restricting the energy efficiency (e.g. through min temperature approaches)."
  - On heuristics: "the drawback is that usually there is no reasonable way to establish the quality of such solutions which sometimes can in fact be rather poor."
- **His later acknowledgement**: the rival won commercially (G42, 2019 extended author copy) [stated, P]. "A very well-known example on the design of process networks is the pinch-analysis (Linnhof and Flower, 1978). The theoretical work began in the early 70's and about a decade later the work made a big impact as it could prove 30% energy savings at chemical and petrochemical operations. After successful commercialization (Linnhoff-March) and another decade roughly 80% of all the world's largest oil and petrochemical companies were either clients or sponsors of the company."
- **Low-weight third-party view** (W4, Wikipedia "Pinch analysis", revision of 2026-08-18) [observed, S]: "Nevertheless, large-scale MINLP problems can still be hard to solve for today's numerical algorithms." Also: "For simple networks of a few streams and heat exchangers, hand design methods with simple targeting software are often adequate, and aid the engineer in understanding the process."

### 4.3 Referees

[stated, P; ASR]
- An early-1980s MILP synthesis paper was rejected *(0:45:57)*: "one of the revie said well the authors are proposing mix line programming which you know we know it's very inefficient for solving so one would be much better off using some heuristics". ASR: revie = reviewers; mix line = mixed-integer linear. The paper is not identified.
- The OA paper itself *(0:55:47–0:56:19)*: "we submitted it to mathematical programming from the time we submitted until it was accepted it took three years actually the review took you know long time there was a little bit of maybe it was our engineering type of slant that did not fit exactly with the one of math programming".
- He also tells a rejection story about the state-task network paper of his advisor's group *(0:50:05)*: "for scheduling we want to solve real problems not toy problem". That paper is Kondili, Pantelides & Sargent 1993 (C41), not his own, so the story records the field's resistance, not a critique of Grossmann.

### 4.4 Completeness of the superstructure

- **Stated by Grossmann first, in 1983** (G3) [stated, P]: "The disadvantage however, is that the computational expense can be rather large when problems are not properly formulated, and furthermore, optimality of the solutions can only be guaranteed with respect to the alternatives that have been considered in the problem representation."
- **Open questions he listed in 1989** (G7) [stated, P]: "1. How to systematically develop superstructures for heterogeneous systems? 2. How to effectively solve MBLP [OCR: MILP] and MINLP problems with poor relaxations?"
- **Peer critique of the paradigm**: Voll, Lampe, Wrobel & Bardow (C29, 2012; *Scholar listing via WebFetch*) [observed, P]: "Current approaches require the designer to define a superstructure, which subsequently is optimized. In the presented method, the a priori specification of a superstructure is avoided".
- **His group's 2020 review** (G41, abstract) [stated, P] covers the rival family: "Finally, we examine the use of evolutionary—recently referred to as superstructure-free—approaches, in which algorithmic procedures dynamically generate and evaluate candidate process structures." It puts "a particular emphasis on the existing literature for automated superstructure generation".
- [inferred] The first 1989 open question, how to generate superstructures systematically, was still the organizing problem of his group's review 31 years later.

### 4.5 SYNHEAT's isothermal-mixing assumption

- **Critics**: K.-M. Björk and T. Westerlund (C26, *Comput. Chem. Eng.* 26(11), 2002; *Scholar listing via WebFetch*) [observed, P]: "If the Synheat model is extended in an appropriate way, the isothermal mixing assumption can be removed." Their examples are meant "to illustrate that the Synheat model can exclude optimal configurations due to the isothermal mixing assumption". The target is Yee & Grossmann 1990 (G34).
- **Answered?** **Not found.** A keyword search ("isothermal", "Björk", "stagewise") ran over the Grossmann texts in the shared scratch folder: several dozen DRC/EDRC reports, reviews and egon author copies. None mentions isothermal mixing in connection with SYNHEAT. The Björk–Westerlund full text was **not read**.
- **Related, not read**: Furman & Sahinidis on the NP-hardness of heat-exchanger network synthesis (C27, title only) and their "critical review" of the field (C28; the abstract read promises "a critical assessment of the current status of research", but what it says about the simultaneous MINLP models is **not read**).

### 4.6 Heuristic stochastic search as a rival, and a published comment

- **Rival method**: Salcedo (C30, *Ind. Eng. Chem. Res.* 31(1), 1992; *Scholar listing via WebFetch*) [observed, P]: "The algorithm does not require any problem decomposition, neither identification or elimination of nonconvexities, prior to its application." Also: "It was tested with several nonconvex NLP and MINLP problems published in the literature". [inferred] That is a direct contrast with the OA/ER/AP decomposition and the convexity tests of Kocis & Grossmann.
- **A published exchange**: in the December 1992 issue of the same journal, R. L. Salcedo published "Comments on "An MINLP process synthesizer for a sequential modular simulator"" (C31). Diwekar, Grossmann & Rubin replied in "Response to comments on "An MINLP process synthesizer for a sequential modular simulator"" (G36, one page). The paper commented on (G35) presents "a variant of the OA/ER/AP algorithm" coupled to the ASPEN simulator. The content of both the comment and the response was **not read** (ACS paywall; no abstract). [practice, P: the exchange exists]

---

## 5. Flexibility analysis: the vertex assumption and its repair

- **The counterexample**: Saboo & Morari 1984 (C32; original **not read**), as Grossmann describes it in his tribute to Morari (G28, Grossmann, Calfa & Garcia-Herreros 2014, author copy "Rev. Dec. 2013") [stated, P]: "This brilliant example by Saboo & Morari (1984) shows that it is possible to have non-vertex critical points, and consequently, that we need appropriate methods that will be able to predict such points."
- **What it hit**: the early vertex-enumeration methods (Halemane & Grossmann 1983, G29; Swaney & Grossmann 1985, G30). G28 [stated, P]:
  - "For most cases however, when these conditions are not met we will often still have vertex critical points." The conditions are the convexity conditions of Swaney & Grossmann.
  - "A second reason is that even if critical points are vertices, we may be faced with the problem of having to analyze an exponential number of vertices".
- **The answer**: Grossmann & Floudas 1987 (G31), as described in G28 [stated, P]: "c) The derivation of problem (26) does not require the assumption of vertex critical points. Hence, non-vertex critical points can be predicted such as in the motivating heat exchanger network problem (Grossmann and Floudas, 1987)."
- **Second-generation critique**: the active-set method relies on KKT conditions, which is not enough for nonconvex models. G28 [stated, P]: "[...] are not convex, the KKT conditions are not sufficient for global optimality." The repair came from his former student's group: "The global optimization strategy proposed by Floudas et al. (2001) for the flexibility test and the flexibility index problems is based on the principles of spatial branch and bound algorithms." (C33, metadata only.)
- **Contact with a rival school, robust optimization**: Zhang, Grossmann & Lima 2016 (G32, abstract) [stated, P]:
  - "The connection between these two approaches has not been sufficiently acknowledged and examined in the literature."
  - "the AARO approach is shown to be generally more restrictive such that it may lead to overly conservative solutions"
  - "numerical examples show the improved computational performance from the proposed formulations compared to the traditional flexibility analysis models."
  - [inferred] The last point concedes that the 1980s flexibility formulations were computationally dominated by duality-based reformulations from the robust-optimization toolbox.
- **His side of that rivalry, 2015** (G51, PSE-2015/ESCAPE-25 plenary; ASR transcript saved by sibling agent 06 during this run) [stated, P]:
  - *(ASR, 0:31:58)*: "the point is that so far if you look at most of the work on proposed optimization it does not account for recourse". ASR: proposed = robust.
  - *(0:37:01–0:37:31)*: "the ideas of linear decision rules are in fact also also very much related to the work on flexibility analysis where I just like to point out flexibility analysis in some sense is actually more General than what we have here".
  - [inferred] Toward the robust-optimization school he combines a critique with a priority claim: static robust counterparts lack recourse, and recourse was already part of flexibility analysis. A year later the 2016 paper says the connection "has not been sufficiently acknowledged and examined in the literature".
- **Pattern** [inferred]: here the critique was answered within about three years (1984 to 1987). He honoured the critic in print 30 years later ("brilliant example"; the tribute is dedicated to Morari), and accepted a former student's correction of his own method.

---

## 6. Scheduling formulations: claims and counter-claims

- **The claim**: Maravelias & Grossmann 2003 (G37, abstract) [stated, P]: "Compared to other general continuous time STN formulations, the proposed model is faster. Compared to event-driven formulations, it is more general, as it accounts for resources other than equipment and gives solutions in comparable computational times." Feature (b): "assignment constraints are expressed using binary variables that are defined only for tasks, not for units".
- **Counter-claim 1**: Sundaramoorthy & Karimi (C34, *Chem. Eng. Sci.* 2005, title "A simpler better slot-based continuous-time formulation..."; *Scholar listing via WebFetch*) [observed, P]: "we show that in contrast to the best model in the literature, our model does not decouple tasks and units, but still has fewer binary variables, constraints, and nonzeros, and is faster." [inferred] "The best model in the literature" that "decouples tasks and units" matches feature (b) of Maravelias & Grossmann.
- **Counter-claim 2, a published comment**: Floudas & Janak, "Comments on "New General Continuous-Time State−Task Network Formulation for Short-Term Scheduling of Multipurpose Batch Plants" by Christos T. Maravelias and Ignacio E. Grossmann and on [...]" (C35, *Ind. Eng. Chem. Res.* 44(6):1985–1986, 2005). It is free to read on the ACS site, but the site blocked every tool; no archived copy exists; Unpaywall lists only the blocked publisher PDF. Content **not read**. No reply by Maravelias & Grossmann was found in Crossref title searches.
- **Counter-claim 3, the rival group's benchmark**: Janak, Shaik & Floudas (C37, AIChE 2005 paper 582f, read) classify the 2003 model among "Global event based models [that] use a set of events that are common for all tasks and all units, as demonstrated in [5]". They describe their own: "the unit-specific event based model developed in [7]-[11] is considered the most general and most rigorous representation of time used in short-term scheduling models." The journal comparison (C36, 2006) "compare[s] and evaluate[s] the performance of six such models" (abstract); its results were **not read**.
- **An earlier model beaten**: Floudas & Lin 2004 (C38, read in part) [observed, P]: "the formulation proposed by Méndez et al. (2001) led to better solution than the one found by Pinto and Grossmann (1995)". The two models are C39 and G39. The time limits behind the comparison were not checked.
- **His side**:
  - The co-authored 2006 review (G40, read in part) describes the rival model neutrally: "a new STN-based formulation that relies on the definition of synchronous time slots and a novel idea of several balances was developed to also deal with network batch processes (Sundaramoorthy & Karimi, 2005)". It does not engage the "better" claim. [practice, P]
  - A one-page item under the 2003 paper's title appeared in *Ind. Eng. Chem. Res.* 42(19):4422 (G38). Its content was **not read**; [inferred] its length and placement suggest an "Additions and Corrections" notice.
- [inferred] Each group's benchmark favoured its own formulation. The 2003–2006 "formulation contest" was settled by no neutral party in the sources found (Contradiction 5).

---

## 7. Industrial deployment: limits named by industry and by himself

- **1990 expectation** (G8) [stated, P]: "It should be also noted that MINLP techniques are starting to be used in the chemical industry (e.g. Foster, 1987; Nath et aly [OCR: et al.,] 1986; Caracotsios and Petrellio, 1989)."
- **2019, with Iiro Harjunkoski of ABB Corporate Research** (G42, extended author copy) [stated, P; half the authorship is industrial]:
  - "The main challenge occurs during hand-over (Harjunkoski et al., 2014)."
  - "Here, the main guarantee to keep the solutions available is to make them "PhD-free", i.e. ensure that you need not be an expert to be able to manage their daily use and configuration. If it is not possible to manage the solution by the local resources, even the best solution will not survive. Unfortunately, companies do not in general anymore have optimization groups or resources driving various PSE in-house improvement projects."
  - "Another major challenge apart from the lifecycle of a PSE solution is how to prove the exact value that an optimization solution contributes to the overall value chain."
  - "Here a major challenge continues to be the effective solution of MINLP problems."
  - The success list names pinch analysis, AspenTech, gPROMS, MPC, ProSensus and others. MINLP algorithms appear only collectively: "the important developments of optimization algorithms where the PSE-community has played an important role, many of which are today available in commercial packages such as GAMS, AMPL and AIMMS."
- **2025, operators' distrust, as he reports it** (G44, Royal Spanish Academy of Sciences, Q&A) [stated, P; ASR, Spanish]:
  - *(1:16:03)*: "Desarrollamos un modelo, ellos mismos dicen, "Bueno, se lo damos a los operarios y dicen, bueno, ¿por qué tengo que creer que eso es óptimo? ¿No hay alguna otra forma de hacerlo?"". Gloss: companies hand a model to operators, who ask why they should believe it is optimal and whether there is no other way.
  - His answer is that the place for AI is explainability of optimal solutions.
  - On the questioner's premise that AI will take over optimization *(1:15:00)*: "Yo lo que diría eh no exactamente por la siguiente razón, primero porque todavía es importante tener una vez más este tipo de modelos. Estos tipo de modelos son más bien una vez más matemáticos con conocimiento físico." Gloss: not exactly, because physics-based mathematical models are still needed.
- [inferred] The 1990 expectation of industrial uptake came true mainly through modelling systems (DICOPT inside GAMS) and through consortium projects. In his own 2019 list, the commercial success story of process synthesis is the rival school's.

---

## 8. Errata, corrections, retractions

[practice, P]
- **Duran & Grossmann erratum** (G2, *Math. Program.* 39(3):337, 1987; read in full): "The solution that was reported in Table 4A with z* =7.7891 is suboptimal. The optimal solution is; z* = 8.0641". It was found "by resolving Test Problem No. 4 on an IBM 3090/400 with 5 FPS Array Processors at the Cornell Theory Center, Ithaca, NY" with MPSX and MINOS. A judgement in print (a reported optimum) was shown wrong by his own re-run; the erratum gives no cause.
- **Erratum to Lee & Grossmann 2000** (G18, 2001): content **not read**.
- **1992 errata** to Sahinidis & Grossmann (G45) and Birewar & Grossmann (G46): content **not read**.
- **Corrigendum** to Ye, Grossmann, Pinto & Ramaswamy 2018 (G47, 2020) and **correction** to Franzoi et al. (G48, 2020): content **not read**.
- **Correction** to Galan et al. (G49, 2019; read): units only ("lower case `k' [...] was published as upper case `K'").
- **One-page item** under the Maravelias–Grossmann 2003 title (G38): content **not read** (§6).
- **No retraction** was found: none among the 945 works of the OpenAlex snapshot (types "erratum" only), and none in the Crossref searches.

---

## 9. What the critiques say about how he does research (by framework layer)

All of this section is [inferred] from §1–8 and is meant for Phase 2. Each point names the evidence it rests on.

- **Layer 1, taste.** He prizes guarantees but ships labelled heuristics (OA/ER/AP, DICOPT's worsening stop). The critics did not dispute the labels; they disputed where the heuristics sit as defaults and what titles promise (§1.4, §2.2). A skill in his voice should keep the label and also flag the default.
- **Layer 2, choosing problems.** His problems come from application structure: binaries entering linearly, process superstructures, batch plants. Generality (Fletcher–Leyffer), worst cases (Hijazi et al.) and nonsmooth or CQ-failure cases (Eronen et al., Lubin et al.) were found by OR and numerical groups that construct adversarial instances. His method rarely starts from such instances (§1.1–1.3).
- **Layer 3, ideas.** Several answers to critiques came from outside and were absorbed: feasibility cuts, lifting, the conic perspective, P-split as a Pyomo.GDP plugin, global flexibility analysis by a former student. His group then re-presents them in reviews (§1, §3, §5).
- **Layer 4, execution and benchmarking.** His group benchmarks inside its collaboration network (the 2019 review with the SHOT authors; scheduling comparisons by each rival group). Its stated caveat is that test sets are "quite small and simple compared to industry-relevant problems". The skill should demand an independent or adversarial test set (§2.3, §6).
- **Layer 5, judging results.** A reported optimum was corrected in 1987 (§8). Worst-case results appear in his reviews as reformulation credits, not as limits (§1.2). Rival scheduling claims went unanswered in print (§6).
- **Layer 6, expression.** Titles promised more than the text ("Global optimization", 1988), while the text was explicit about the limits (§1.4). Claims of "first" are discussed in 01.
- **Layer 7, organization.** The CAPD industry model brings problems and data, but he names hand-over, maintenance without PhDs and proof of value as the failure points (§7).

---

## Contradictions

These are kept as found; none is reconciled here.

1. **OA's efficiency.**
   - "The algorithm is easy to grasp and implement, yet computationally efficient." (G15, 2026). "In practice, outer approximation often works efficiently." (C3).
   - Against: "an example is given for which it visits all integer assignments" (C1, 1994); "take an exponential number of iterations" (C2); "requires 2n [2^n] iterations" (C4).
   - His group's reviews of 2019 and 2026 do not mention the worst case.
2. **Single-tree versus multi-tree.** The 2019 review "support[s] the strong belief in the single-tree approach". The 2026 history reports "little performance difference between the multi- and single-tree variants" once the multi-tree method is accelerated. Same lead author, seven years apart.
3. **DICOPT's stopping rule.** The GAMS manual says the worsening heuristic "tends to work very well for non-convex problems (and even for convex problems)". His group sets the gap-closing `stop 1` for convex experiments (G13) and calls the default "a heuristic" that "in many cases" yields optimal or near-optimal integer solutions.
4. **Two versions of the 2019 benchmark.**
   - Preprint (June 2018, egon copy): 366 instances; SHOT 342 and AOA 334 solved; virtual best 357.
   - Published version: 335 instances (the smallinvSNPr* instances were excluded after losing their convex classification); SHOT 312, AOA 310; virtual best 326.
   - Sibling notes 01 and 02 quote the 366-instance preprint.
5. **Scheduling formulations.** Maravelias & Grossmann: "faster" and "more general". Sundaramoorthy & Karimi: "simpler" and "faster" than "the best model in the literature". Janak, Shaik & Floudas: their own model is "the most general and most rigorous". Each claim rests on its authors' own benchmark.
6. **Hull versus big-M.**
   - His line: the hull MINLP is "shown to be tighter than the conventional "big-M" formulation" (G16).
   - The critics: "a folklore observation that extended convex hull formulations tend to perform worse than expected", supported among others by his group's 2015 results (C18).
   - His group itself: big-M "generates a smaller MILP/MINLP, while the latter generates a tighter one" (G23).
7. **The pinch debate.** In 2024 he says those who thought the mixed-integer approach "a lost cause" "were all proved to be wrong". In 2019 he presents pinch analysis as the process-design success that reached "roughly 80% of all the world's largest oil and petrochemical companies". Both can hold (academic versus commercial victory), but the sources do not say so.
8. **"Global" in 1988.** The journal title says "Global optimization of nonconvex [...] MINLP problems". The same group's 1988 report says "no rigorous guarantee on global optimality can be given".
9. **Vertex critical points.** His 2014 text calls the non-vertex counterexample "brilliant" and also maintains that "For most cases however [...] we will often still have vertex critical points". No source quantifies "most cases".

---

## Gaps

- **Salcedo's 1992 comment and the Diwekar–Grossmann–Rubin response**: content not read (ACS; no abstract; no open copy found).
- **Floudas & Janak's 2005 comment** on Maravelias & Grossmann: content not read. It is marked free on ACS, but the site returned 403 to curl and WebFetch, the Wayback Machine has no snapshot, and two WebSearch calls found no summary. No reply was found in Crossref.
- **Results of Shaik, Janak & Floudas 2006** for the Maravelias–Grossmann model: not read (closed). Only the 2005 extended abstract and the journal abstract were read.
- **Stephanopoulos's 1981 FOCAPD text**: not online. The identification of the 1980 keynote speaker is inferred from the title match and Grossmann's 1989 citation; the critic's argument is known only from Grossmann's 2024 recollection.
- **Linnhoff's own published critique** of mathematical-programming synthesis: not found. One WebSearch returned only general pinch material. The identification of the "German professor with a Leeds PhD" is inferred.
- **Björk & Westerlund 2002** full text, and **any answer** by Grossmann's group to the isothermal-mixing critique: not found.
- **Furman & Sahinidis 2001/2002** on Yee & Grossmann's model: not read (title and abstract only).
- **Ryoo & Sahinidis 1995**, and any claim that local MINLP solutions of literature test problems (Kocis & Grossmann's) were suboptimal: not verified. Only the first abstract sentence was read.
- **Kesavan et al. 2004**: their comparison with OA/ER/AP was not read (abstract only).
- **Hijazi, Bonami & Ouorou 2014**: full text not read. The description of the example comes from Belotti et al.'s preprint and Lubin et al.
- **Regularized OA (Kronqvist, Bernal & Grossmann 2020)**: whether it discusses the 2^n example was not read (abstract only).
- **Independent benchmark of DICOPT**: none found after 2019. Mittelmann's page lists only global solvers. Castillo et al. 2005 is known only as relayed by Grossmann's group.
- **Westerlund & Pettersson 1995 (ECP)**: abstract not readable, so the ECP school's original argument against OA's NLP subproblems is not read.
- **Enterprise-wide optimization (EWO)**: no published critique of the EWO programme was found in this run (no search budget was spent on it).
- **Referee reports and rebuttals**: none public. The rejected early-1980s paper is unidentified.
- **Errata**: the content of six of the eight correction items (counting the 2003 one-page item) was not read, and the 1987 erratum gives no cause.
- **Douglas's hierarchical school** and industrial voices such as Siirola: no critique text found or read.
- **Saboo & Morari 1984**: not read. Their framing relative to Grossmann's vertex methods is known only from Grossmann's 2014 account.
- **Acta Numerica survey**: read in the Argonne preprint copy downloaded by a sibling agent. My own download attempt from mcs.anl.gov returned HTTP 403, so the copy's provenance rests on the sibling download.

---

## Sources

**Critics, rival groups and third parties**

- C1. R. Fletcher, S. Leyffer, "Solving mixed integer nonlinear programs by outer approximation", *Math. Program.* 66:327–349, 1994. DOI 10.1007/BF01581153 (abstract read, Springer page). P
- C2. H. Hijazi, P. Bonami, A. Ouorou, "An Outer-Inner Approximation for Separable Mixed-Integer Nonlinear Programs", *INFORMS J. Comput.* 26(1):31–44, 2014. DOI 10.1287/ijoc.1120.0545 (abstract via Crossref). P
- C3. P. Belotti, C. Kirches, S. Leyffer, J. Linderoth, J. Luedtke, A. Mahajan, "Mixed-integer nonlinear optimization", *Acta Numerica* 22:1–131, 2013. DOI 10.1017/S0962492913000032 (abstract via Crossref; preprint ANL/MCS-P3060-1121, 22 Nov 2012, read in part). P
- C4. M. Lubin, E. Yamangil, R. Bent, J. P. Vielma, "Polyhedral approximation in mixed-integer convex optimization", *Math. Program.* 172(1–2):139–168, 2018 (online 2017). DOI 10.1007/s10107-017-1191-y; arXiv 1607.03566v2 (read in part). P
- C5. V.-P. Eronen, M. M. Mäkelä, T. Westerlund, "On the generalization of ECP and OA methods to nonsmooth convex MINLP problems", *Optimization* 63(7):1057–1073, 2014 (online 2012). DOI 10.1080/02331934.2012.712118 (abstract via OpenAlex). P
- C6. H. Hijazi, L. Liberti, "Constraint qualification failure in action", *Oper. Res. Lett.* 44(4):503–506, 2016. DOI 10.1016/j.orl.2016.05.006 (metadata only; cited in C4). S
- C7. P. Kesavan, R. J. Allgor, E. P. Gatzke, P. I. Barton, "Outer approximation algorithms for separable nonconvex mixed-integer nonlinear programs", *Math. Program.* 100(3), 2004. DOI 10.1007/s10107-004-0503-1 (abstract, Springer page). P
- C8. T. Westerlund, R. Pörn, "Solving Pseudo-Convex Mixed Integer Optimization Problems by Cutting Plane Techniques", *Optim. Eng.* 3(3):253–280, 2002. DOI 10.1023/A:1021091110342 (abstract). P
- C9. T. Westerlund, F. Pettersson, "An extended cutting plane method for solving convex MINLP problems", *Comput. Chem. Eng.* 19 (Suppl.):131–136, 1995. DOI 10.1016/0098-1354(95)87027-X (metadata only). P
- C10. J. Kronqvist, A. Lundell, T. Westerlund, "The extended supporting hyperplane algorithm for convex mixed-integer nonlinear programming", *J. Glob. Optim.* 64(2):249–272, 2016 (online 2015). DOI 10.1007/s10898-015-0322-3 (abstract). P
- C11. A. Lundell, J. Kronqvist, T. Westerlund, "The supporting hyperplane optimization toolkit for convex MINLP", *J. Glob. Optim.* 84(1):1–41, 2022. DOI 10.1007/s10898-022-01128-0 (abstract). P
- C12. K. Abhishek, S. Leyffer, J. Linderoth, "FilMINT: An Outer Approximation-Based Solver for Convex Mixed-Integer Nonlinear Programs", *INFORMS J. Comput.* 22(4):555–567, 2010. DOI 10.1287/ijoc.1090.0373 (abstract via Crossref). P
- C13. P. Bonami, M. Kılınç, J. Linderoth, "Algorithms and Software for Convex Mixed Integer Nonlinear Programs", IMA Vol. Math. Appl. 154:1–39, 2012 (online 2011). DOI 10.1007/978-1-4614-1927-3_1 (not read; quoted in C4). S
- C14. S. Burer, A. N. Letchford, "Non-convex mixed-integer nonlinear programming: A survey", *Surv. Oper. Res. Manag. Sci.* 17(2):97–106, 2012. DOI 10.1016/j.sorms.2012.08.001 (author copy read in part). P
- C15. H. S. Ryoo, N. V. Sahinidis, "Global optimization of nonconvex NLPs and MINLPs with applications in process design", *Comput. Chem. Eng.* 19(5):551–566, 1995. DOI 10.1016/0098-1354(94)00097-2 (first abstract sentence only, *Scholar listing via WebFetch*). P
- C16. C. S. Adjiman, I. P. Androulakis, C. A. Floudas, "Global optimization of mixed-integer nonlinear problems", *AIChE J.* 46(9):1769–1797, 2000. DOI 10.1002/aic.690460908 (abstract via Crossref). P
- C17. J. Kronqvist, R. Misener, C. Tsay, "Between Steps: Intermediate Relaxations Between Big-M and Convex Hull Formulations", CPAIOR 2021, LNCS, pp. 299–314. DOI 10.1007/978-3-030-78230-6_19; arXiv 2101.12708 (abstract). P
- C18. J. Kronqvist, R. Misener, C. Tsay, "P-split formulations: a class of intermediate formulations between big-M and convex hull for disjunctive constraints", *Math. Program.* 218(1–2):57–94, 2025. DOI 10.1007/s10107-025-02232-1; arXiv 2202.05198v3 (read in part). P
- C19. R. Anderson, J. Huchette, W. Ma, C. Tjandraatmadja, J. P. Vielma, "Strong mixed-integer programming formulations for trained neural networks", *Math. Program.* 183(1–2):3–39, 2020. DOI 10.1007/s10107-020-01474-5 (metadata only; cited in C18). S
- C20. P. Bonami, A. Lodi, A. Tramontani, S. Wiese, "On mathematical programming with indicator constraints", *Math. Program.* 151(1):191–223, 2015. DOI 10.1007/s10107-015-0891-4 (abstract). P
- C21. J. P. Vielma, "Mixed Integer Linear Programming Formulation Techniques", *SIAM Rev.* 57(1):3–57, 2015. DOI 10.1137/130915303 (abstract). P
- C22. A. Frangioni, C. Gentile, "Perspective cuts for a class of convex 0–1 mixed integer programs", *Math. Program.* 106(2):225–236, 2006 (online 2005). DOI 10.1007/s10107-005-0594-3 (abstract). P
- C23. S. Ceria, J. Soares, "Convex programming for disjunctive convex optimization", *Math. Program.* 86(3):595–614, 1999. DOI 10.1007/s101070050106 (abstract). P
- C24. O. Günlük, J. Linderoth, "Perspective reformulations of mixed integer nonlinear programs with indicator variables", *Math. Program.* 124(1–2):183–205, 2010. DOI 10.1007/s10107-010-0360-z (abstract). P
- C25. G. Stephanopoulos, "Synthesis of process flowsheets: an adventure in heuristic design or a utopia of mathematical programming?", in *Foundations of Computer-Aided Chemical Process Design*, Engineering Foundation, New York, 1981 (no DOI; title, venue and year confirmed on Google Scholar via WebFetch; not read). P
- C26. K.-M. Björk, T. Westerlund, "Global optimization of heat exchanger network synthesis problems with and without the isothermal mixing assumption", *Comput. Chem. Eng.* 26(11):1581–1593, 2002. DOI 10.1016/S0098-1354(02)00129-1 (abstract, *Scholar listing via WebFetch*). P
- C27. K. C. Furman, N. V. Sahinidis, "Computational complexity of heat exchanger network synthesis", *Comput. Chem. Eng.* 25(9–10):1371–1390, 2001. DOI 10.1016/S0098-1354(01)00681-0 (metadata only). P
- C28. K. C. Furman, N. V. Sahinidis, "A Critical Review and Annotated Bibliography for Heat Exchanger Network Synthesis in the 20th Century", *Ind. Eng. Chem. Res.* 41(10):2335–2370, 2002. DOI 10.1021/ie010389e (abstract via OpenAlex). P
- C29. P. Voll, M. Lampe, G. Wrobel, A. Bardow, "Superstructure-free synthesis and optimization of distributed industrial energy supply systems", *Energy* 45(1):424–435, 2012. DOI 10.1016/j.energy.2012.01.041 (abstract, *Scholar listing via WebFetch*). P
- C30. R. L. Salcedo, "Solving nonconvex nonlinear programming and mixed-integer nonlinear programming problems with adaptive random search", *Ind. Eng. Chem. Res.* 31(1):262–273, 1992. DOI 10.1021/ie00001a037 (abstract, *Scholar listing via WebFetch*). P
- C31. R. L. Salcedo, "Comments on "An MINLP process synthesizer for a sequential modular simulator"", *Ind. Eng. Chem. Res.* 31(12):2804–2805, 1992. DOI 10.1021/ie00012a027 (metadata only; not read). P
- C32. A. K. Saboo, M. Morari, "Design of resilient processing plants—IV: Some new results on heat exchanger network synthesis", *Chem. Eng. Sci.* 39(3):579–592, 1984. DOI 10.1016/0009-2509(84)80054-8 (metadata only; content via G28). P
- C33. C. A. Floudas, Z. H. Gümüş, M. G. Ierapetritou, "Global Optimization in Design under Uncertainty: Feasibility Test and Flexibility Index Problems", *Ind. Eng. Chem. Res.* 40(20):4267–4282, 2001. DOI 10.1021/ie001014g (metadata only; content via G28). P
- C34. A. Sundaramoorthy, I. A. Karimi, "A simpler better slot-based continuous-time formulation for short-term scheduling in multipurpose batch plants", *Chem. Eng. Sci.* 60(10):2679–2702, 2005. DOI 10.1016/j.ces.2004.12.023 (abstract, *Scholar listing via WebFetch*). P
- C35. C. A. Floudas, S. L. Janak, "Comments on "New General Continuous-Time State−Task Network Formulation for Short-Term Scheduling of Multipurpose Batch Plants" by Christos T. Maravelias and Ignacio E. Grossmann and on [...]", *Ind. Eng. Chem. Res.* 44(6):1985–1986, 2005. DOI 10.1021/ie050135j (metadata only; not read). P
- C36. M. A. Shaik, S. L. Janak, C. A. Floudas, "Continuous-Time Models for Short-Term Scheduling of Multipurpose Batch Plants: A Comparative Study", *Ind. Eng. Chem. Res.* 45(18):6190–6209, 2006. DOI 10.1021/ie0601403 (abstract via OpenAlex). P
- C37. S. L. Janak, M. Shaik Abdul, C. A. Floudas, "A Comparative Study of Continuous-Time Models for Short-Term Scheduling in Multipurpose Batch Plants", AIChE Annual Meeting 2005, paper 582f. https://folk.ntnu.no/skoge/prost/proceedings/aiche-2005/non-topical/Non%20topical/papers/582f.pdf (read in full; 2-page extended abstract). P
- C38. C. A. Floudas, X. Lin, "Continuous-time versus discrete-time approaches for scheduling of chemical processes: a review", *Comput. Chem. Eng.* 28(11):2109–2129, 2004. DOI 10.1016/j.compchemeng.2004.05.002 (read in part; copy at https://cepac.cheme.cmu.edu/pasi2008/slides/mendez/library/reading/scheduling_review.pdf). P
- C39. C. A. Méndez, G. P. Henning, J. Cerdá, "An MILP continuous-time approach to short-term scheduling of resource-constrained multistage flowshop batch facilities", *Comput. Chem. Eng.* 25(4–6):701–711, 2001. DOI 10.1016/S0098-1354(01)00671-8 (metadata only). P
- C40. I. Castillo, J. Westerlund, S. Emet, T. Westerlund, "Optimization of block layout design problems with unequal areas: A comparison of MILP and MINLP optimization methods", *Comput. Chem. Eng.* 30(1):54–69, 2005. DOI 10.1016/j.compchemeng.2005.07.012 (metadata only; finding relayed by G13). S
- C41. E. Kondili, C. C. Pantelides, R. W. H. Sargent, "A general algorithm for short-term scheduling of batch operations—I. MILP formulation", *Comput. Chem. Eng.* 17(2):211–227, 1993. DOI 10.1016/0098-1354(93)80015-F (metadata only; context for the rejection story). P
- W1. GAMS Development Corp., "DICOPT" solver manual, https://www.gams.com/latest/docs/S_DICOPT.html, fetched 2026-10-10 (read in part; documentation maintained by GAMS). P
- W2. H. Mittelmann, "Mixed Integer Nonlinear Programming Benchmark (MINLPLIB)", https://plato.asu.edu/ftp/minlp.html, version dated 26 Feb 2026 (read in full). P
- W3. Wikipedia, "Bodo Linnhoff", https://en.wikipedia.org/wiki/Bodo_Linnhoff, fetched 2026-10-10 (read in part). S
- W4. Wikipedia, "Pinch analysis", revision 1369961574 of 2026-08-18, https://en.wikipedia.org/wiki/Pinch_analysis (read in part; low weight). S

**Grossmann and co-authors**

- G1. M. A. Duran, I. E. Grossmann, "An outer-approximation algorithm for a class of mixed-integer nonlinear programs", *Math. Program.* 36(3):307–339, 1986. DOI 10.1007/BF02592064 (abstract, Springer page). P
- G2. M. A. Duran, I. E. Grossmann, Erratum to the above, *Math. Program.* 39(3):337, 1987. DOI 10.1007/BF02592081 (read in full). P
- G3. I. E. Grossmann, "Mixed-integer programming: is it a useful tool in process synthesis?", DRC-06-59-83, CMU, 1983. KiltHub DOI 10.1184/R1/6467171.v1 (read in part). P
- G4. G. R. Kocis, I. E. Grossmann, "Global optimization of nonconvex MINLP problems in process synthesis", EDRC-06-37-87, CMU, 1987. KiltHub DOI 10.1184/R1/6467033.v1 (read in part). P
- G5. G. R. Kocis, I. E. Grossmann, "Computational experience with DICOPT solving MINLP problems in process systems engineering", EDRC-06-43-88, CMU, 1988. KiltHub DOI 10.1184/R1/6466841.v1 (read in part). P
- G6. G. R. Kocis, I. E. Grossmann, "Global optimization of nonconvex mixed-integer nonlinear programming (MINLP) problems in process synthesis", *Ind. Eng. Chem. Res.* 27(8):1407–1421, 1988. DOI 10.1021/ie00080a013 (metadata only). P
- G7. I. E. Grossmann, "MINLP optimization strategies and algorithms for process synthesis", EDRC 06-59-89, CMU, 1989. KiltHub DOI 10.1184/R1/6467159.v1 (read in part). P
- G8. I. E. Grossmann, "Mixed-integer nonlinear programming techniques for the synthesis of engineering systems", EDRC 06-83-90, CMU, 1990. KiltHub DOI 10.1184/R1/6467165.v1 (read in part). P
- G9. J. Viswanathan, I. E. Grossmann, "A combined penalty function and outer-approximation method for MINLP optimization", *Comput. Chem. Eng.* 14(7):769–782, 1990. DOI 10.1016/0098-1354(90)87085-4 (metadata only). P
- G10. I. Quesada, I. E. Grossmann, "An LP/NLP based branch and bound algorithm for convex MINLP optimization problems", *Comput. Chem. Eng.* 16(10–11):937–947, 1992. DOI 10.1016/0098-1354(92)80028-8 (metadata only). P
- G11. P. Bonami, L. T. Biegler, A. R. Conn, G. Cornuéjols, I. E. Grossmann, C. D. Laird, J. Lee, A. Lodi, F. Margot, N. Sawaya, A. Wächter, "An algorithmic framework for convex mixed integer nonlinear programs", *Discrete Optim.* 5(2):186–204, 2008. DOI 10.1016/j.disopt.2006.10.011 (metadata only). P
- G12. J. Kronqvist, D. E. Bernal, A. Lundell, I. E. Grossmann, "A review and comparison of solvers for convex MINLP", *Optim. Eng.* 20(2):397–455, 2019 (online 2018). DOI 10.1007/s11081-018-9411-8 (published open-access version read in part; June 2018 egon preprint checked for instance counts). P
- G13. D. E. Bernal, S. Vigerske, F. Trespalacios, I. E. Grossmann, "Improving the performance of DICOPT in convex MINLP problems using a feasibility pump", *Optim. Methods Softw.* 35(1):171–190, 2020 (online 2019). DOI 10.1080/10556788.2019.1641498 (preprint of 12 Aug 2019 read in part). P
- G14. J. Kronqvist, D. E. Bernal, I. E. Grossmann, "Using regularization and second order information in outer approximation for convex MINLP", *Math. Program.* 180(1–2):285–310, 2020 (online 2018). DOI 10.1007/s10107-018-1356-3 (abstract). P
- G15. J. Kronqvist, D. E. Bernal Neira, I. E. Grossmann, "50 years of mixed-integer nonlinear and disjunctive programming", *Eur. J. Oper. Res.* 331(3):687–705, 2026. DOI 10.1016/j.ejor.2025.07.016 (egon author copy read in part). P
- G16. I. E. Grossmann, S. Lee, "Generalized Convex Disjunctive Programming: Nonlinear Convex Hull Relaxation", *Comput. Optim. Appl.* 26(1):83–100, 2003. DOI 10.1023/A:1025154322278 (abstract). P
- G17. S. Lee, I. E. Grossmann, "New algorithms for nonlinear generalized disjunctive programming", *Comput. Chem. Eng.* 24(9–10):2125–2141, 2000. DOI 10.1016/S0098-1354(00)00581-0 (metadata only). P
- G18. S. Lee, I. E. Grossmann, Erratum to "New algorithms for nonlinear generalized disjunctive programming", *Comput. Chem. Eng.* 25(7–8):1153, 2001. DOI 10.1016/S0098-1354(01)00706-2 (metadata only). P
- G19. S. Lee, I. E. Grossmann, "A global optimization algorithm for nonconvex generalized disjunctive programming and applications to process systems", *Comput. Chem. Eng.* 25(11–12):1675–1697, 2001. DOI 10.1016/S0098-1354(01)00732-3 (metadata only). P
- G20. R. Karuppiah, I. E. Grossmann, "A Lagrangean based branch-and-cut algorithm for global optimization of nonconvex mixed-integer nonlinear programs with decomposable structures", *J. Glob. Optim.* 41(2):163–186, 2008 (online 2007). DOI 10.1007/s10898-007-9203-8 (metadata only). P
- G21. J. P. Ruiz, I. E. Grossmann, "Global optimization of non-convex generalized disjunctive programs: a review on reformulations and relaxation techniques", *J. Glob. Optim.* 67(1–2):43–58, 2017 (online 2016). DOI 10.1007/s10898-016-0401-0 (metadata only). P
- G22. N. W. Sawaya, I. E. Grossmann, "Computational implementation of non-linear convex hull reformulation", *Comput. Chem. Eng.* 31(7):856–866, 2007. DOI 10.1016/j.compchemeng.2006.08.002 (metadata only). P
- G23. F. Trespalacios, I. E. Grossmann, "Improved Big-M reformulation for generalized disjunctive programs", *Comput. Chem. Eng.* 76:98–103, 2015. DOI 10.1016/j.compchemeng.2015.02.013 (egon author copy; abstract and introduction read). P
- G24. F. Trespalacios, I. E. Grossmann, "Algorithmic Approach for Improved Mixed-Integer Reformulations of Convex Generalized Disjunctive Programs", *INFORMS J. Comput.* 27(1):59–74, 2015. DOI 10.1287/ijoc.2014.0610 (metadata only; cited in C18). P
- G25. K. C. Furman, N. W. Sawaya, I. E. Grossmann, "A computationally useful algebraic representation of nonlinear disjunctive convex sets using the perspective function", *Comput. Optim. Appl.* 76(2):589–614, 2020. DOI 10.1007/s10589-020-00176-0 (abstract). P
- G26. D. E. Bernal Neira, I. E. Grossmann, "Convex mixed-integer nonlinear programs derived from generalized disjunctive programming using cones", *Comput. Optim. Appl.* 88(1):251–312, 2024. DOI 10.1007/s10589-024-00557-9; arXiv 2109.09657v3 (read in part). P
- G27. Q. Chen, E. S. Johnson, D. E. Bernal, R. Valentin, S. Kale, J. Bates, J. D. Siirola, I. E. Grossmann, "Pyomo.GDP: an ecosystem for logic based modeling and optimization development", *Optim. Eng.* 23(1):607–642, 2022 (online 2021). DOI 10.1007/s11081-021-09601-7 (metadata only). P
- G28. I. E. Grossmann, B. A. Calfa, P. Garcia-Herreros, "Evolution of concepts and models for quantifying resiliency and flexibility of chemical processes", *Comput. Chem. Eng.* 70:22–34, 2014. DOI 10.1016/j.compchemeng.2013.12.013; KiltHub DOI 10.1184/R1/6466970.v1 (egon author copy "Rev. Dec. 2013" read in part). P
- G29. K. P. Halemane, I. E. Grossmann, "Optimal process design under uncertainty", *AIChE J.* 29(3):425–433, 1983. DOI 10.1002/aic.690290312 (metadata only). P
- G30. R. E. Swaney, I. E. Grossmann, "An index for operational flexibility in chemical process design. Part I: Formulation and theory", *AIChE J.* 31(4):621–630, 1985. DOI 10.1002/aic.690310412 (metadata only). P
- G31. I. E. Grossmann, C. A. Floudas, "Active constraint strategy for flexibility analysis in chemical processes", *Comput. Chem. Eng.* 11(6):675–693, 1987. DOI 10.1016/0098-1354(87)87011-4 (metadata only). P
- G32. Q. Zhang, I. E. Grossmann, R. M. Lima, "On the relation between flexibility analysis and robust optimization for linear systems", *AIChE J.* 62(9):3109–3123, 2016. DOI 10.1002/aic.15221 (abstract via Crossref). P
- G33. I. E. Grossmann, J. Santibanez, "Applications of mixed-integer linear programming in process synthesis", *Comput. Chem. Eng.* 4(4):205–214, 1980. DOI 10.1016/0098-1354(80)85001-0 (metadata only). P
- G34. T. F. Yee, I. E. Grossmann, "Simultaneous optimization models for heat integration—II. Heat exchanger network synthesis", *Comput. Chem. Eng.* 14(10):1165–1184, 1990. DOI 10.1016/0098-1354(90)85010-8 (metadata only). P
- G35. U. M. Diwekar, I. E. Grossmann, E. S. Rubin, "An MINLP process synthesizer for a sequential modular simulator", *Ind. Eng. Chem. Res.* 31(1):313–322, 1992. DOI 10.1021/ie00001a042 (abstract via OpenAlex). P
- G36. U. M. Diwekar, I. E. Grossmann, E. S. Rubin, "Response to comments on "An MINLP process synthesizer for a sequential modular simulator"", *Ind. Eng. Chem. Res.* 31(12):2805, 1992. DOI 10.1021/ie00012a028 (metadata only; not read). P
- G37. C. T. Maravelias, I. E. Grossmann, "New General Continuous-Time State−Task Network Formulation for Short-Term Scheduling of Multipurpose Batch Plants", *Ind. Eng. Chem. Res.* 42(13):3056–3074, 2003. DOI 10.1021/ie020923y (abstract via OpenAlex). P
- G38. C. T. Maravelias, I. E. Grossmann, one-page item under the same title, *Ind. Eng. Chem. Res.* 42(19):4422, 2003. DOI 10.1021/ie991098x (metadata only; not read). P
- G39. J. M. Pinto, I. E. Grossmann, "A Continuous Time Mixed Integer Linear Programming Model for Short Term Scheduling of Multistage Batch Plants", *Ind. Eng. Chem. Res.* 34(9):3037–3051, 1995. DOI 10.1021/ie00048a015 (metadata only). P
- G40. C. A. Méndez, J. Cerdá, I. E. Grossmann, I. Harjunkoski, M. Fahl, "State-of-the-art review of optimization methods for short-term scheduling of batch processes", *Comput. Chem. Eng.* 30(6–7):913–946, 2006. DOI 10.1016/j.compchemeng.2006.02.008 (read in part; copy at https://cepac.cheme.cmu.edu/pasi2008/slides/mendez/library/reading/state-of-the-art-review.pdf). P
- G41. L. Mencarelli, Q. Chen, A. Pagot, I. E. Grossmann, "A review on superstructure optimization approaches in process system engineering", *Comput. Chem. Eng.* 136:106808, 2020. DOI 10.1016/j.compchemeng.2020.106808 (abstract via OpenAlex). P
- G42. I. E. Grossmann, I. Harjunkoski, "Process Systems Engineering: Academic and industrial perspectives", *Comput. Chem. Eng.* 126:474–484, 2019. DOI 10.1016/j.compchemeng.2019.04.028 (egon extended PSE 2018 author copy read in part). P
- G43. "Subject to" long-form interview with Ignacio Grossmann (host A. Subramanian), YouTube, uploaded 2024-02-08, https://www.youtube.com/watch?v=jNjqnsnUzhE; transcript `../sources/talks/2024-02-08_subject-to-interview_jNjqnsnUzhE.txt` (automatic captions, read in part). P
- G44. I. E. Grossmann, "Evolution and Future Trends in Process Systems Engineering", Real Academia de Ciencias Exactas, Físicas y Naturales, 16 Sep 2025, https://www.youtube.com/watch?v=r9jdqigq59Q; transcript `../sources/talks/2025-09-16_rac-spain-evolution-future-trends-pse_r9jdqigq59Q_es-auto-captions.txt` (Spanish automatic captions, Q&A read). P
- G45. N. V. Sahinidis, I. E. Grossmann, Erratum to "Multiperiod investment model for processing networks with dedicated and flexible plants", *Ind. Eng. Chem. Res.* 31(4):1236, 1992. DOI 10.1021/ie00004a041 (metadata only). P
- G46. D. B. Birewar, I. E. Grossmann, Erratum to "Simultaneous synthesis, sizing, and scheduling of multiproduct batch plants", *Ind. Eng. Chem. Res.* 31(7):1834, 1992. DOI 10.1021/ie00007a035 (metadata only). P
- G47. Y. Ye, I. E. Grossmann, J. M. Pinto, S. Ramaswamy, Corrigendum to "Mixed-integer nonlinear programming models for optimal design of reliable chemical plants", *Comput. Chem. Eng.* 133:106639, 2020. DOI 10.1016/j.compchemeng.2019.106639 (metadata only). P
- G48. R. E. Franzoi, B. C. Menezes, J. D. Kelly, J. A. W. Gut, I. E. Grossmann, Correction to "Cutpoint Temperature Surrogate Modeling for Distillation Yields and Properties", *Ind. Eng. Chem. Res.* 59(44):19838, 2020. DOI 10.1021/acs.iecr.0c05114 (metadata only). P
- G49. A. Galan, C. de Prada, G. Gutierrez, D. Sarabia, I. E. Grossmann, R. Gonzalez, Correction to "Implementation of RTO in a large hydrogen network considering uncertainty", *Optim. Eng.* 20(4):1191–1192, 2019. DOI 10.1007/s11081-019-09446-1 (read in full). P
- G50. C. T. Maravelias, I. E. Grossmann, "On the relation of continuous- and discrete-time state–task network formulations", *AIChE J.* 52(2):843–849, 2006 (online 2005). DOI 10.1002/aic.10684 (metadata only; checked as a possible reply to C34/C35, content not read). P
- G51. I. E. Grossmann, plenary lecture "Optimization of Process Systems under Uncertainty", PSE-2015/ESCAPE-25 (YouTube channel "PSE2015 ESCAPE25", uploaded 2015-06-01), https://www.youtube.com/watch?v=EqjnmhqEu1U; transcript `../sources/talks/2015-06-01_pse2015-escape25-plenary-optimization-under-uncertainty_EqjnmhqEu1U_auto-captions.txt`, saved by sibling agent 06 (automatic captions, read in part). P

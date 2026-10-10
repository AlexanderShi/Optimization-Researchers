# 02 · Stated methodology: what Sahinidis says research should be

> **Researcher**: Nikolaos V. Sahinidis ("Nick"), Gary C. Butler Family Chair, Georgia Tech ISyE and ChBE (earlier UIUC 1991–2007 and CMU 2007–2020); DBLP 123/7012; Google Scholar `PTXe50QAAAAJ`; ORCID 0000-0003-2087-9131; homepage https://sahinidis.coe.gatech.edu/
> **Dimension**: research agent 02 of 06, stated methodology (what he claims research should be), nuwa research-craft Phase 1, MINLP Team
> **Research date**: 2026-10-10
> **Sources consulted**: 62 lines under "Sources": 48 primary, 7 secondary or observed, 7 that could not be accessed or held nothing in his voice. WebSearch calls used: 3 of 3.
> **Method**: his CV (footer 7 Oct 2026) and every research and software page of his group site; the free front matter of the 2002 book; his 1996 *Optima* book review; the FOCAPO 2003 review; the 2009 single-author review (PMC manuscript); eight *Optimization and Engineering* editorials he wrote as editor-in-chief (2018–2023); the open-access texts of the 2013 DFO comparison, the 2016 simulation-optimization review, the 2022 mixed-integer DFO comparison, the 2017 ALAMO and domain-reduction arXiv papers, the 2020 *Statistical Science* discussion, the 2018 CAPD article, the 2019 Grossmann profile and the 2021 PSE perspective; his talk abstracts at Dagstuhl (2018), Oberwolfach (2019) and Georgia Tech/Lehigh (2024); abstracts (Springer pages, Crossref, arXiv API, PubMed) of nine more papers; the BARON user manual v. 2026.9.10; two of his talks on YouTube, transcribed from automatic captions with yt-dlp; one press article with direct quotes. Identifiers were checked with Crossref, Unpaywall, the arXiv API, PubMed and the publishers' pages in this run.
> **Local corpus**: `references/sources/` held only `.gitkeep` files and `RESOURCES.md`; there is no user-supplied material, so no finding is marked "from user-supplied material". `references/sources/private/` was not opened.
> **Scope**: only what he SAID or wrote about how research (and solver, benchmark and modelling work) should be done. Whether he does it is agent 03's job. When a statement sits inside a research paper, only its prescriptive or evaluative sentences are used here.
> **Tags**: [stated] his words · [practice] what the record shows he did (context only) · [observed] what others wrote or said · [inferred] my reading. Each item also says primary or secondary and carries a **voice** label: *sole* (he is the only author or speaker), *co* (co-authored; his personal share is unknown), *firm* (a document of The Optimization Firm, his company), *press* (journalist's article quoting him), *ASR* (YouTube automatic captions of his own talk; wording approximate), *committee* (prize-committee text).
> **Quoting**: verbatim. PDF line-end hyphens are rejoined (also across page breaks), ligatures written out, curly quotes and apostrophes straightened, superscript footnote markers dropped; bracketed reference numbers such as [17] are kept; [sic] marks typos in the original. Every non-caption quote was re-checked by script against the downloaded text of its source in this run (punctuation- and spacing-insensitive match). ASR quotes copy the caption text exactly, recognition errors included, are marked "caption-derived" with a [h:mm:ss] cue time, and must be re-checked against the audio before a published skill quotes them.
> **Biggest caveat**: I found no essay, interview, oral history, blog or lecture in which he describes how he does research or advises PhD students. What follows comes from prefaces, review conclusions, editorials, web pages, manual advice, talk abstracts and two auto-captioned talks. His stated method is therefore mostly about solvers, benchmarking and modelling. On careers, mentoring and writing process there is almost nothing (see Gaps).

---

## 0. Source map: when he said what, and from which position

Era facts are [stated, primary: CV S01] unless marked; the Georgia Tech and Texas A&M announcements (S43, S44) add nothing in his voice and were used only to confirm dates and titles.

| Period | Position and resources | Stated sources used here |
|---|---|---|
| 1991–2007 | UIUC: Assistant Professor of Mechanical and Industrial Engineering 1991–97, then Chemical (and Biomolecular) Engineering; visiting NYU Stern 1999–2000. The Optimization Firm founded in 2001 "to commercialize BARON" (S39). BARON web portal 1999–2002 with "over 6100 problems" submitted (S11). | S12 (1996), S11 (2002), S13 (2003), S14, S15, S16 (2005); undated website pages S04–S07 (some read like UIUC-era text [inferred]) |
| 2007–2020 | CMU John E. Swearingen Professor; DOE NETL Faculty Research Fellow 2008–2020; CAPD director July 2015 – June 2020; Editor-in-Chief of *Optimization and Engineering* (OPTE) 2018–2023 | S17 (2009), S18 (2013), S19 (2014), S20 (2016), S21–S23 (2017), S40 (2017 talk), S24–S27 (2018), S28a–d (2018–19), S29–S31 (2019) |
| 2020– | Georgia Tech Butler Family Chair; firm CEO; Aspen Technology consultant 2020–24; Editor-in-Chief of *Mathematical Programming Computation* 2025– | S28e–h (2020–23), S32 (2020), S33, S42 (2021), S34 (2022), S35 (2024), S41 (2025 talk), S36 (2025), S37, S38, S01 (2026) |

---

## 1. Beliefs he repeats (three or more independent statements)

Counts are of distinct documents or talks. The belief labels are my paraphrase [inferred]; the quotes are in §2.

| ID | Belief | n | Dated instances | Voices |
|---|---|---|---|---|
| B1 | Models learned from data must be "as accurate and as simple as possible"; simplicity first serves later optimization, later also interpretation | 9 | 2014 S19; 2017 S21, S40; 2018 S25; 2025 S41; 2026 S37; undated S06, S09; firm S39 | sole (S25, S40, S41), co, site, firm |
| B2 | A systematic comparison of methods on large public test sets is a contribution in itself, and the field needs more of them | 10 | 2003 S13; 2013 S18; 2016 S20; 2019 S28b, S29; 2020 S32; 2022 S34; 2025 S36; undated S06, S10 | sole (S13, S28b), co, site |
| B3 | No single method wins: conclude with portfolios or collections of solvers, relaxations or models | 6 | 2013 S18; 2018 S26, S27; 2019 S31; 2020 S32; 2022 S34 | sole (S31), co |
| B4 | Research should end as an accessible, usable tool: software, executables, test problems, data | 11 | 2002 S11; 2016 S20; 2017 S40; 2018 S24, S25; 2019 S31; 2020 S32; 2022 S34; 2026 S01; undated S04, S08 | sole, co, ASR |
| B5 | Rigor: global-optimality guarantees, finite termination, certificates; deterministic methods over stochastic ones without certificates | 9 | 1996 S12; 2002 S11; 2016 S20; 2017 S21; 2018 S27; 2026 S38; undated S04, S05, S07 | sole, co, site |
| B6 | Reduce before you search: domain reduction and cheap inference are the core of the method | 6 | 2002 S11; 2009 S17; 2017 S22; 2025 S41; 2026 S38; undated S10 | sole, co, ASR |
| B7 | Design for the non-expert default user: automate decisions, benchmark defaults, value convenience | 7 | 2002 S11; 2013 S18; 2018 S26; 2019 S29; 2020 S32; 2025 S41; 2026 S38 | sole, co, ASR |
| B8 | Problems and features come from applications and users; research lives at an interface (OR–CS, optimization–engineering) | 14 | 2002 S11; 2013 S18; 2018–2023 S28a, S28c–h (seven OPTE editorials, largely boilerplate); 2019 S28b; 2018 S24; 2021 S33, S42; website S02 | sole, co, press |
| B9 | Problem-specific and physical knowledge (bounds, first principles, relaxation-only constraints) is worth more than algorithmic options | 7 | 2005 S14, S15; 2017 S21, S40; 2025 S41; 2026 S38; undated S09 | sole, co, ASR |
| B10 | "Why now" is the maturity of algorithms, hardware and his own tools | 4 | 2002 S11; 2017 S21, S40; 2021 S42 | co, ASR, press |
| B11 | A relaxation or method is worth only as much as its speed and robustness | 4 | 2002 S11; 2005 S15; 2018 S26; 2025 S36 | co |
| B12 | Reproducibility and reporting: cite the version, share data and scripts, make runs deterministic | 5 | 2016 S20; 2020 S32; 2022 S34; 2026 S38; undated S10 | sole (manual), co, site |

*Observed echoes* [observed, secondary], context only: the 2004 INFORMS Computing Society Prize went to him and Tawarmalani "For their contributions to the field of Nonlinear global optimization summarized in their book Convexification and Global Optimization in Continuous and Mixed-Integer Nonlinear Programming, and embodied in the BARON software package." (S46). The NAE elected him (2022) for "his contributions to global optimization and the development of widely used software for optimization and machine learning." (as quoted by S45; the NAE page was not fetched). His former advisor Grossmann, at MIT in 2017: "Then, of course, the work of Nick Sahinidis. Baron -- Baron, in many ways, has become almost a household name of software for global optimization. Well, again, still restricted to size because of the NP hardness of the problem." (S47, human subtitles [0:17:18]). Outsiders and he agree that the software is the contribution (B4).

---

## 2. Findings by layer (framework §一)

### 2.1 Taste: what is worth doing, what a good result is

**T1. The goal is a general, rigorous, automated computational tool.** [stated · primary]
- "Our work in this area aims at developing an all-purpose, rigorous global optimization methodology for continuous, integer, and mixed integer nonlinear programs." and "The ultimate goal is to provide, through BARON, a precise and valuable computational tool to engineers and scientists." (S04, group site, undated)
- "This book documents many of the theoretical advancements that have enabled us to develop BARON to the extent that it now makes it possible for the first time to solve many practically relevant problems in reasonable amounts of computational time in a completely automated manner." (S11, 2002, p. xiv; *co* with Tawarmalani)
- "The BARON project began in the early 1990s with the aim to develop an efficient computational tool for the solution of nonconvex mixed-integer nonlinear optimization problems. The BARON code has more than doubled in the past decade as a result of several developments." (S31, Oberwolfach 2019, p. 1622; *sole*)
- "Problems which up to recent times were thought to require advanced (such as parallel or distributed) computers for their solution, can be solved with modest hardware using our global optimization package BARON. This software has served as an enabling technology in a variety of application areas" (S04)
- Context: the same aim is stated from the UIUC era (site, book) to 2019, when he was at CMU, ran CAPD and the firm. Counts toward B4, B5, B7.

**T2. Generality: the same mathematics across domains.** [stated]
- "The math underneath is the same. Application agnostic algorithms can be applied by many people in different domains, and that was what particularly fascinated me." (S42, 15 Jul 2021; *press*, secondary)
- "Even though these problems originate from very disparate fields, they have very similar mathematical structures. In particular, they involve the use of a merit function to evaluate alternatives from very large, often combinatorial, search spaces." (S05, informatics page, undated; primary)
- "However, side-chain conformation prediction and structural alignment of proteins can be posed as graph problems that can be analyzed from the mathematical and optimization points of view, independent of the underlying biological problem. Thus, an entirely data-driven solution approach can be developed for these problems." (S17, 2009, §5; *sole*, primary)
- See Contradiction C1: he also says general-purpose algorithms are unlikely to win on some classes.

**T3. Rigor, certificates and finite termination are marks of quality.** [stated · primary] (B5)
- His results include "(d) finite branching schemes for certain continuous nonconvex problem classes for which standard branch and bound approaches are merely convergent" (S04).
- "the branching scheme of Section 7.6.4 that guarantees finite termination for classes of problems for which previous algorithms were either convergent only in limit (i. e., infinite) or resorted to explicit enumeration." (S11, 2002, p. xv; *co*)
- His 1996 review picks out, among "other fine contributions": "The key observation is that the underlying problems can be viewed as integer programs. Finiteness can, therefore, be achieved by integral branching." and his own paper with Shectman, which shows "that exhaustiveness and branching on the incumbent whenever possible in tandem ensure finiteness" (S12, *Optima* 52, Dec 1996, pp. 12–13; *sole*).
- "Genetic algorithms lack optimality certifications and are typically stochastic in nature. In contrast, we propose an optimization formulation for the rigorous deterministic optimization of the symbolic regression problem." (S27, 2018 abstract; *co*)
- "Is it possible to introduce rigor in the use and practice of heuristics?" and "The long term goal of this work is to build an optimization-based science of heuristics that will lead to the design of new, provably optimal heuristics for process synthesis and operations." (S07, undated; its listed papers stop in 2004 [practice, see 01 §3 item 9])
- "We have developed a novel methodology, the first to theoretically guarantee a global optimum of a minimal principle formulation of the phase problem for centric compounds." (S05)
- Among future needs: "(7) the continued emphasis on providing guarantees of convergence to optima for local and global optimization routines in general settings" (S20, 2016, p. 372; *co*)
- "It does not prove global optimality. Multistart produces no lower bound, so only the branch-and-bound search can provide that guarantee." (S38, manual 2026, §10.4; *sole* author line)

**T4. A good result is a first, a complete characterization, or a measurable jump on a hard library.** [stated]
- "a small but difficult instance of a nuclear reactor pattern design problem that was solved for the first time to global optimality using our algorithms" and "we completely characterize the feasible space of a refrigerant design problem proposed 15 years ago revealing all the 29 candidate refrigerants that meet the design specifications." (S11, p. xv; *co*)
- "There's a famous collection of challenging test problems in this area that originate from applications, including nuclear reactor management, facility location, pipeline design, and other engineering problems. When I first started working on them, we were able to solve about 5-10% of them. Now, we can solve about two-thirds of those problems, and I'm hoping that what we're researching with Santanu and George will push the capabilities of optimization solvers for these problems close to 100%." (S42, 2021; *press*, secondary)
- Caption-derived (S41, 2025 [0:19:05]): "I'm showing two things on a collection of problems that I don't necessarily like but somebody else has been using up until very recently to to Benchmark Mi NLP solvers ... when we started uh we had very humble beginnings could barely solve one in three problems uh as time goes by now at this point we can solve almost the entire collection uh three times as many" (*ASR*). The numbers differ from 2021 (see C5).
- He translates a gain into practical impact: "Compared to the 95% accuracy of the best previous techniques, our developments would imply 24 fewer misdiagnosed patients for this small sample alone." (S05)

**T5. Simple and accurate beats complex and accurate.** [stated] (B1)
- "A methodology that uses a small number of simulations or experiments to learn models that are as accurate and as simple as possible is proposed." (S19, 2014 abstract; *co*)
- "[17] recently developed the ALAMO approach to machine learning, motivated by the need to obtain simple models from experimental and simulation data." (S21, 2017, p. 2; *co*)
- "We have developed the ALAMO methodology with the aim of producing a tool capable of using data to learn algebraic models that are accurate and as simple as possible." (S25, Dagstuhl 2018, p. 81; *sole*)
- "To solve such a large optimization model, we aim to build not only accurate but also simple surrogate models." (S09, ALAMO motivation page) and "Of particular importance is the algorithm's ability to generate models that are simple yet accurate." (S06)
- Caption-derived, 2017 (S40 [0:09:41]): "I also want them simple as simple as possible and as I said the motivation the primary motivation is that my models will be more amable to Global optimization down the road and I'll be able to find global Optima uh another adventage of having simple models is that actually you can look at them and interpret them physically uh that's a bonus uh it's not a requirement in my context" (*ASR*)
- Caption-derived, 2025 (S41 [0:36:59]): "nowadays when my students or anybody else comes and says oh I just came up with this fancy neuron Network and and modeling this system uh it is this figure that actually makes me give me a pause because I don't know how often we actually need neural networks to model engineering applications I suspect not very often ... we are finding that simple quadratic models often do the job and we are publishing papers again and again demonstrating this" (*ASR*)
- "In this work, we take a different path by developing interpretable models that are simple but effective." and "The models are simple to train and deploy, and they remain effective with small training sets, which makes them practical in low-resource settings." (S37, 2026 abstract; *co* with Bayramoğlu and Nemhauser)
- Firm voice: ALAMO "builds accurate, interpretable models from data ... to identify models that balance predictive performance with simplicity" (S39).
- The stated reason changes over time, from optimizability to interpretability (CH2, C4).

**T6. A relaxation's strength counts only with speed and reliability.** [stated · primary · co] (B11)
- "A variety of nonlinear, including semidefinite, relaxations have been developed in recent years for nonconvex optimization problems. Their potential can be realized only if they can be solved with sufficient speed and reliability. Unfortunately, state-of-the-art nonlinear programming codes are significantly slower and numerically unstable compared to linear programming software." (S15, 2005 abstract)
- Relaxations "that are entirely linear and enable the use of robust and established linear programming techniques in solving MINLPs." (S11, 2002, p. xiv)
- 2018: the new paradigm combines polyhedral and convex nonlinear relaxations "along with fail-safe techniques" (S26). 2025: BARON "has become a highly robust and efficient computational system" and the decade's additions include "various robustness enhancements" (S36). Context: the position moved as NLP codes matured (CH1).

**T7. What he praises in other people's work** (as reviewer, editor and prize-committee member). [stated · primary]
- 1996: Floudas and Pardalos's series is "an excellent and much needed series" (S12; *sole*).
- 2019, as guest editor of a MINLP special issue (S28b; *sole*). His summaries of the papers: "The primary goal of this work is expose [sic] a disciplined MINLP modeling approach to a problem that henceforth has been addressed by greedy heuristics." (p. 303). "In addition to a theoretical analysis of the proposed algorithm, the authors demonstrate that their developments are useful in practice by optimizing part of the Spanish gas transmission network." (p. 303). "A very thorough review and comparison of solvers for convex MINLPs" in which "An impressive number of 16 MINLP solvers are then compared on 335 problems and the results are analyzed based on the degree of nonlinearity and discreteness of problems." (p. 303). He accepts a heuristic paired with a bound: the authors "develop a heuristic to solve the underlying MINLP and use a convex relaxation to demonstrate that their heuristic provides near-optimal solutions." (p. 304)
- 2022 Rosenbrock Prize citation, written by a committee of Raghunathan (chair), Ploskas and Sahinidis (S28h; *committee*): "The paper proposes an alternative Lagrangian dual method that circumvents the deficiencies of prior approaches and is readily integrated in existing algorithms. The numerical experiments on a variety of problems (network design, facility location, and staff rostering) demonstrate that the generic approach developed in the paper shows significant computational speedups over the existing, domain-specific approaches." Its last sentence ("The article is relevant from a theoretical point of view since it addresses a class of problem strongly studied in the OR scientific community, but also relevant for its practical aspect...") nearly repeats the 2021 citation, which was written by a committee without him (S28g). His share of that wording is uncertain.
- [inferred] The common criteria: a disciplined formal model instead of an ad hoc heuristic; proof of usefulness on a real system; large, well-analysed comparisons; generic methods that beat domain-specific ones; theory and practice together.

**T8. Personal motives in his own words.** [stated]
- "I tried out optimization, and I loved it, so I stuck with it." (S42, 2021; *press*). The journalist adds that as a CMU graduate student he read "every past issue he could get his hands on" of *Operations Research* and *Management Science* (journalist's paraphrase, [observed], secondary).
- Caption-derived (S41 [0:21:47]): "I I really like the idea of doing algorith design using U non-convex uh optimization models to sort of figure out tune basically different types of algorithms uh we can even think in terms of designing algorithms from scratch" (*ASR*). The CV lists a March 2026 talk with I. Mitrai, "Automated design of algorithms" (S01) [practice; not read].

### 2.2 Problem choice: where problems come from, why now, when to narrow

**P1. Start from a missing capability; when the general problem stalls, retreat to special classes, then generalize.** [stated · primary · co]
- "We embarked on the journey of developing an efficient global optimization algorithm for MINLPs in the early 1990s when we realized that there was no software that could even solve small-sized MINLPs to global optimality despite indications in the literature that such an algorithm could be easily constructed. Our initial attempts, however, found us struggling with many gaps in the literature in the specifications of such a global optimization algorithm. Therefore, about ten years ago, we decided to concentrate on special classes of mixed-integer nonlinear programs, including separable concave minimization problems and applications in capacity expansion of chemical processes. In the process, we developed the first branch-and-bound framework for MINLPs, the Branch-And-Reduce Optimization Navigator (BARON). Its initial purpose was to facilitate design and experimentation with global optimization algorithms. Drawing from this initial experience, in the last six years, we have concentrated on the automatic solution of a general class of MINLPs." (S11, 2002, pp. xiii–xiv)
- Context: written in 2002 about 1991–96, when he was a new assistant professor in an Industrial Engineering department with small internal grants (S01; see 01 §1.1). This is his only stated account of narrowing a problem after a failed attempt.

**P2. Open with a gap that a systematic study fills.** [stated] (B2)
- "There is a notable need for systematic comparisons between the different modeling philosophies. A small step in this direction has been taken by Liu & Sahinidis (1996)" (S13, FOCAPO 2003, p. 160; *sole*)
- "There is currently no systematic comparison of the existing implementations of derivative-free optimization algorithms on a large collection of test problems. The primary purpose of the present paper is to provide such a comparison" (S18, 2013, p. 1248; *co*)
- "However, a systematic comparison of solvers on a large collection of problems is missing. The aim of this paper is to fill this void in the literature." (S34, 2022, p. 434; *co*)
- "There is a need for more such repositories, not only for testing of algorithms over statistically significant sizes of problem sets, but for comparison between different classes of algorithms. The need for comparison is evident, given the sheer number of available approaches to solving simulation optimization problems, and the lack of clarity and lack of consensus on which types of algorithms are suitable in which contexts." (S20, 2016, pp. 371–372; *co*)

**P3. Pick instances that are small yet beyond current solvers, find the features that make them hard, and end with open problems.** [stated · primary · talk abstract]
- "The field of mixed-integer nonlinear optimization has advanced significantly over the past three decades. However, even small instances of many nonconvex optimization problems involving the Euclidean norm are beyond the capabilities of existing algorithms. These problems stem from applications such as molecular energy minimization, object packing, and facility location, and often share specific features that make them challenging. In this presentation, we identify these features, introduce new algorithms to address them, and present numerical results that demonstrate the impact of our techniques. Furthermore, we identify several related open problems and opportunities for analytical and computational advances." (S35, abstract for Georgia Tech ISyE, 18 Oct 2024, and Lehigh, 3 Dec 2024)
- He describes current work as aimed at "problems – linear, mixed, and nonlinear – that our field has struggled for decades to solve" (S42, 2021; *press*).
- Context: Georgia Tech, AFOSR grant on norm convexification 2023–26 (S01).

**P4. Why now: when algorithms, hardware and his own tools have matured.** [stated] (B10)
- "On the brighter side, recent advances in algorithmic and computing technology make it possible to revisit these problems with the hope of solving practically relevant problems in reasonable amounts of computational time." (S11, 2002, p. xiii; *co*)
- "However, integer optimization algorithmic advances combined with improved hardware have recently allowed for the best subset problem to be practically solved for problems with hundreds or thousands of regressors." (S21, 2017, p. 3; *co*)
- Caption-derived (S40, 2017 [0:54:22]): "I should point out that this is not something we could have done five years ago why because Baron was not there in terms of capability five years ago Global optimization was not there five years ago and also the derivative free sers were not quite there you know uh up until very recently or at least we didn't know how to use them" (*ASR*)
- "With the recent advances in machine learning, optimization is fueling developments in areas we never imagined we could address before." (S42, 2021; *press*)

**P5. Problems come from applications and users.** [stated] (B8)
- "Fueled by a growing number of applications in science and engineering, the development of derivative-free optimization algorithms has long been studied, and it has found renewed interest in recent time." (S18, 2013, p. 1247; *co*)
- "Fueled by a variety of applications, MINLP will continue to advance and provide powerful tools for analytics and decision making." (S28b, 2019, p. 304; *sole*)
- "Problem (1) offers a very natural way to approach many engineering design problems, especially in chemical engineering where nonlinear functions can capture the complex behavior of chemical processes and integer variables can be used to model discrete decisions" (S28b, p. 302)
- "The problems originate from applications in a variety of areas in science and engineering." (S08, his test-problem page)
- "Second, the design of new molecules and materials often requires new methods, and in that respect, motivates more fundamental systems research." (S33, 2021, p. 28; *co*, six authors)
- His problem framings set up a gap: "Heuristics offer fast solutions but no guarantee of optimality. Optimization approaches, on the other hand, offer rigor but suffer combinatorial explosion of computational requirements." (S07); "A principal challenge in optimization practice is how to optimize in the absence of an algebraic model of the system to be optimized." (S06)

**P6. Understand the problem's structure before designing algorithms; on some classes, expect problem-specific methods.** [stated · primary · sole]
- "In the case of stochastic integer programming with integer variables in stages other than the first, this represents a conceptual in addition to computational challenge. Deeper understanding of problem structure and properties is required in order to devise applicable algorithms." (S13, 2003, pp. 160–161)
- "It appears unlikely that general-purpose algorithms will solve such problems exactly. Instead, we expect to see the development of problem-specific approximation schemes for integer and nonlinear problems such as the asymptotically optimal approximation scheme recently proposed by Ahmed & Sahinidis (2002) for capacity expansion of chemical processes." (S13, p. 161; see C1)
- "Understanding the nature of the problem is critical in choosing an effective approach to accurately model the system at hand." (S21, 2017, p. 1; *co*)

**P7. Motivating a topic by recognized lists of open problems.** [stated · primary · sole] Two instances only, so not a repeated belief: "Today, Dantzig still considers planning under uncertainty as one of the most important open problems in optimization (Horner 1999)." (S13, p. 153); the 2009 review opens with "The ten most wanted problems in protein bioinformatics (Tramontano, 2005)" (S17, §1).

### 2.3 Idea generation

**I1. Marry two literatures and transfer tools by analogy.** [stated · primary · co]
- "The aim of this book is to marry the advancements in solving nonlinear and integer programming models and to develop new results in the more general framework of mixed-integer nonlinear programs (MINLPs) with the goal of devising practically efficient global optimization algorithms for MINLPs." (S11, p. xiii)
- "'product disaggregation' (distributing the product over the sum) leads to tighter linear programming relaxations, much like variable disaggregation does in mixed-integer linear programming." (p. xiv)
- "A new theoretical framework for range reduction (Chapter 5) that helped us identify connections with Lagrangian outer-approximation and develop a unified treatment of existing and several new domain reduction techniques from the integer programming and constraint programming literatures." (p. xiv)
- Where the theory came from: "Special thanks are due to Lynn McLinden for his course, Conjugate Analysis and Optimization, which helped both of us understand a lot of the background material needed for the convexification part of this work." (p. xvii)

**I2. Strip the application down to mathematics; when that is not yet possible, write the formulation first.** [stated · primary · sole] (S17, 2009, §5)
- "The astute reader must have noticed that posing the first two problems required virtually no mathematical notation and very little domain knowledge." For crystallography, by contrast: "new formulations are still needed to bring diffraction physics under a complete optimization formalism that can be subsequently analyzed for developing suitable algorithms."
- Abstract: "Many of these problems are purely continuous in nature. Yet, to this date, they have been approached mostly via combinatorial optimization algorithms that are applied to discrete approximations. The main purpose of the paper is to offer an introduction and motivate further systems approaches to these problems."

**I3. Applications created algorithm features.** [stated · primary · co]
- "In the context of the BARON project for global MINLP optimization, molecular design motivated the transition from nonlinear to linear programming relaxations and the development of techniques for finding not just the best design but a list of designs or even all feasible designs (12)." (S33, 2021, p. 13; six authors. That this sentence is his is [inferred]: it describes his software.)

**I4. Learn from users' problems.** [stated · primary · co]
- "Thanks are also due to the optimization community that tested BARON and provided extensive feedback and an enormous set of test problems. Between October 1999 and August 2002, 164 researchers and users of optimization techniques submitted over 6100 problems to the BARON Web portal (an average of over six problems a day). We have learned a great deal and improved the algorithms and software considerably as a result of these submissions." (S11, p. xviii)
- The 2025 talk (S41 [0:21:30], caption-derived): he finds BARON applications by tracing citations, "that's how I found all these they cting Baron I look them up and I confirm" (*ASR*).

**I5. Reduce before you search, cheapest reduction first.** [stated] (B6)
- "Residue reduction comes first in this setting because it is simpler than rotamer reduction, simplifies rotamer reduction operations considerably, and often solves SCP entirely on its own." (S17, 2009, §2; *sole*)
- "Smaller domains lead to tighter relaxations." (S22, 2017, p. 2; *co*)
- "What distinguishes branch-and-reduce [41, 42] from plain spatial branch-and-bound is the aggressive use of range reduction. BARON applies several independent reduction mechanisms at every node. These reductions help keep the search tree small." (S38, manual 2026, §5.1)
- BARON "derives its name from its combining constraint propagation, interval analysis, and duality in its reduce arsenal with advanced branch-and-bound optimization concepts." (S10)
- Caption-derived (S41 [0:18:19]): "this inference in here can be used to simplify the search um and speed up uh the algorithms" (*ASR*)

**I6. Compose your own tools into a new method.** [stated]
- "ALAMO relies on integer nonlinear optimization, derivative-free optimization, and global optimization to build and optimize models." (S25, 2018; *sole*)
- "However, when the design of a process involves discrete variables and complex nonlinear objectives and constraints, the resulting problem topology is often too complex for DFO methods to solve reliably. To facilitate use of standard algebraic optimization methods for the solution of simulated or experimental systems, we developed ALAMO to generate a set of algebraic surrogate models to describe these systems." (S09, motivation page)
- Give the modeler a channel to the solver: "we extend BARON's modeling language in order to facilitate the communication of problem-specific relaxation information from the modeler to the branch-and-bound solver." (S14, 2005 abstract; *co*); "Our algorithm exploits convexity, either identified automatically or supplied through a suitable modeling language construct, in order to generate polyhedral cutting planes and relaxations for multivariate nonconvex problems." (S15, 2005 abstract; *co*) (B9)
- Let domain knowledge seed the model: ALAMO "allows for a large set of potential basis functions that can be found from polynomials, engineering experience, physical phenomena, and statistical fitting functions." (S09, technical brief); ALAMO models "can enforce constraints on the response variables to incorporate first-principles knowledge." (S21, 2017 abstract; *co*)

**I7. Take the middle path between extremes.** [stated · ASR] Caption-derived (S41 [0:24:53]): "I realized pretty quickly that some very complex models are so complex that the final optimization step would be very difficult even if they are accurate at The Other Extreme if I go for a linear fit for the data I know that would be inaccurate and therefore I wouldn't be able to come up with meaningful results so we decide to stay somewhere in between"

**I8. Fit the algorithm to how experiments are actually run.** [stated · ASR] Caption-derived (S41), on Jones's DIRECT. What he keeps [0:45:29]: "the interesting thing that I feel uh Jones came up with was a way to do this selection of boxes uh using some lipsit continuity assumption without actually requiring us to have the lip constant and that was I think is very powerful". What he rejects [0:45:46]: "what I don't like though about this algorithm is this tri-section and how we go about partitioning the s p and then taking measurements this is not doesn't have any connection to a a lab the way we we take measurements in a lab you go to chemistry lab or materials lab you're not going to run a single measurement you're going to run a bunch of measurements ... the other thing is I'm not going to be able to take measurements at exact points ... these are uh issues that I'd like to over come make these kinds of algorithms uh work in a better way in the context of of an actual experimental setup". He then introduces Branch-and-Model. [inferred] The template: keep a rival's key insight, replace the part that clashes with practice.

### 2.4 Experiments and execution

**X1. Benchmark at default settings, because users rarely tune.** [stated · primary · co] (B7)
- "Algorithmic parameters for the codes under study should be chosen in a way that is reflective of the relative performance of the software under consideration. Unfortunately, the optimization packages tested have vastly different input parameters that may have a significant impact upon the performance of the algorithm. ... However, for expensive experiments and time-demanding simulations like the bioremedation [sic] model of [98], practitioners cannot afford to experiment with many different algorithmic options. Even for less expensive functions, most typical users of optimization packages are not experts on the theory and implementation of the underlying algorithm and rarely explore software options." Hence "comparisons were carried out using the default parameter values for each package, along with identical stopping criteria and starting points across solvers. Nonetheless, all software developers were provided with early results of our experiments and given an opportunity to revise or specify their default option values." (S18, 2013, pp. 1268–1269)
- Six years later, a paper that tunes BARON itself: "Tuning solver options is often necessary to reduce execution time and improve solution quality." (S29, 2019 abstract; *co*)
- The solver should make expensive decisions itself: "These procedures, especially probing, can be expensive. BARON therefore determines automatically how much probing is worthwhile" (S38, manual 2026, §5.3); the 2002 goal was "the automatic solution of a general class of MINLPs" (S11, p. xiv).

**X2. Iterate with developers, then test for overtraining on unseen problems.** [stated · primary · co] "In an effort to encourage developers to revise and improve their software, we shared our computational results with them over several rounds. Between each round, several developers provided improved versions of their implementations. At the end of this process, we tested their software against an additional collection of problems that had not been seen by developers in order to confirm that the process had not led to overtraining of the software on our test problem collection." (S18, p. 1249; the transformed hold-out set of "an additional 502 problems that had never been seen by the developers" is described on p. 1287)

**X3. Calibrate budgets to a real expensive application.** [stated · primary · co] "To put this limit in perspective, 2,500 function evaluations for the bioremedation [sic] model of [98], which represents a typical application of derivative-free optimization methods to expensive engineering problems, would run for about 200 CPU days." (S18, p. 1266). Resource context, same page: "All computations were performed on Intel 2.13 GHz processors running Linux and Matlab R2010a." The 2022 sequel used "an Intel Xeon CPU W-2123 with 32 GB of main memory and a clock of 3.6 GHz" (S34, p. 445).

**X4. Report per library, so that no single collection drives the conclusion.** [stated · primary · co] "In the sequel we present results for each library separately so as to demonstrate that the observed trends are not dominated by any particular library, convexity, or integrality properties." (S22, 2017, p. 16)

**X5. Modelling rules for global solvers.** [stated · primary · sole author line, firm document] (S38, BARON manual v. 2026.9.10) (B9)
- §4.1: "Tight bounds based on physical or problem-specific knowledge are often more valuable than any algorithmic option in this manual. Bounds set to extremely large values, such as ± 10^10, merely "to be safe," are a common cause of slow convergence."
- §6.2: "Users should therefore provide finite lower and upper bounds for as many problem variables as possible."
- §7.2: "Avoid gratuitous nonlinearity. ... Every nonlinear operation removed is one that need not be transformed, relaxed, or branched on."
- §10.2: "Declare a constraint convex only when its convexity has been established."
- §8.5: "Users should review all warnings, even nonfatal ones, because BARON may have parsed the model differently than intended."
- §4: "If a model is known to be convex, a local NLP solver can return the global optimum directly and may do so faster. BARON remains useful when nonconvexities are present, when convexity is suspected but not proven, or when a certificate of global optimality is required."
- Context: a commercial manual; the firm's research scientists co-author recent BARON papers (01 §1.1). How much of this text is his own is unknown.

**X6. Reproducibility: version, determinism, data and scripts.** [stated] (B12)
- "The best way to cite BARON is by citing one of the BARON publications and mentioning the version of the software utilized." (S10)
- "Wall-clock and CPU seconds do not provide the same reproducibility. A run terminated by MaxTime may stop at a different node on a loaded machine than on an idle one, and may therefore return a different result" (S38 §5.6); "A run stopped by MaxWork stops at exactly the same point on every machine." (§5.6); "For reproducible experiments, users should prefer MaxWork over MaxTime (Section 5.6)." (§13.2)
- He names non-reproducibility as an obstacle to fair comparison: "Less impeding difficulties, but difficulties nonetheless, include the need to interface algorithms to a common wrapper, the objective comparison with solvers that incorporate random elements as their results may not be reproducible, and lack of standard test simulations for purposes of benchmarking." (S20, 2016, p. 370; *co*)
- "For our computations, we use the ncvreg package, L0Learn package, and code provided by the authors. Our scripts are available online." (S32, 2020, p. 2; *co*); "All data generated or analyzed during this study are available from https://sahinidis.coe.gatech.edu/bbo?q=midfo." (S34, 2022, p. 459; *co*)

**X7. Measure progress by running old and new versions on the same hardware.** [stated · ASR] Caption-derived (S41 [0:20:00]): "I'm running now different versions of the algorithm on the same Hardware that's how I'm doing this comparison so so there's been quite a bit of progress in this context and things did not happen overnight uh it took a long time to get here"

**X8. Keep your own library of rivals and testbeds.** [stated · primary · site]
- "To tackle such systems, we maintain a comprehensive library of existing derivative-free algorithms, and perform extensive studies of their performance in various domains." The simulation-optimization goals include "(1) compile and compare existing methods for simulation optimization on new problem testbeds" (S06).
- "The purpose of this web site is to provide a collection of problems for testing algorithms for simulation optimization and derivative-free optimization." (S08)
- "As simulation optimization develops, there is also a need for methods of comparison of algorithms on test beds with statistically significant number of problems." (S20, p. 371; *co*)

**X9. Adversarial sampling as the acceptance test for a surrogate; spend as few experiments as possible.** [stated · primary · site]
- "Adaptive sampling: By interrogating the system using Error Maximization Sampling (EMS), the training set is updated with new points sampled where the current model breaks down. Repeat steps 2 and 3, until no points can be found that violate the model." and "If, during this step, no points that violate the model can be found, we will consider our model sufficiently accurate." (S09, technical brief)
- "New simulation/experimental points are strategically chosen to help rule out the previous iterates' surrogate with the goal of increasing model accuracy using relatively few costly simulation/experimentation." (S09, motivation)
- "we are developing novel algorithms to address classes of derivative-free optimization problems while performing the fewest number of experiments." (S06)

**X10. First-principles models are expensive; surrogates buy time.** [stated · ASR] Caption-derived (S41 [0:23:13]): "I can probably invest you know every one of my students develop an algebraic model might take us a year to figure out the solution to the differential equations and everything uh the proper model uh it takes it takes time"

### 2.5 Judging results

**J1. There is no single winner; conclude with portfolios.** [stated] (B3)
- "However, computational results show that there is no single solver whose performance dominates that of all others. In addition, all solvers provided the best solution possible for at least some of the test problems." (S18, 2013, p. 1287; *co*)
- "Finally, we use larger instances to demonstrate that a portfolio of models provides an effective solution mechanism for problems of the size typically addressed in the symbolic regression literature." (S27, 2018 abstract; *co*)
- The relaxation framework uses "learning strategies for automatically selecting and switching between polyhedral and nonlinear relaxations and among different local search algorithms in different parts of the search tree." (S26, 2018 abstract; *co*). In 2019 he lists "portfolios or [sic] linear and nonlinear relaxations" among BARON's new features (S31, p. 1622; *sole*).
- "Overall, existing algorithms in this field are complementary in their performance. They should be used collectively rather than individually." (S34, 2022, p. 459; *co*)
- "Indeed, even if it was possible to define and agree upon what qualities make a regression algorithm "best", in a noisy and nonlinear world, it is impossible to speak in absolutes. But if the ultimate goal of statistics is to create value, then even if we cannot pin-down the idea of "best", we must certainly be able to point in its general direction." (S32, 2020, p. 7; *co*)

**J2. Check a learned model against physics.** [stated · ASR] Caption-derived.
- 2017 (S40 [0:50:39]): "had this term not appeared there I would have known there would be you know there was something wrong in in the data"; and [0:51:27]: "the bottom line is you know if you have a simple model you can look at it and and decide whether it makes sense physically or not if it doesn't then you know perhaps you need some more measurements or different basis functions"
- 2025 (S41 [0:35:57]): "you can look at this and and say okay this makes sense I know it makes sense from the physical point of view or maybe it doesn't make sense something went wrong let me go back and figure that out"
- Related, in writing: "Although regression-based models should not be used for extrapolation outside of the training domain, enforcing bounds on the response and certifying that a selected model satisfies these bounds can allow for a safer alternative to blind extrapolation." (S21, 2017, p. 8; *co*)

**J3. Hold others' experiments to a fairness standard.** [stated · primary · co] (S32, 2020)
- On design: "While this approach is important to mirror the set-up and conclusions of important theoretical work on the lasso, it somewhat exaggerates the lasso's relative deficiencies by implying that the number of true positives the lasso will identify (which they quantify using "Accuracy") is much lower than in actuality." (p. 5)
- On timing: "However, this appears to be comparing the time needed to find a single cardinality-constrained solution set to the full solution path for glmnet." (pp. 6–7)
- On maturity: "We do not consider L0BnB here because the implementation is currently in the prototype stage." (p. 7)
- On tone: "The authors have started a highly constructive dialogue, our goal is to continue it." (p. 1)

**J4. Keep evidence and proof apart.** [stated · primary] "It is important to distinguish what such a run does and does not establish. It shows that a feasible point with value 1.28838290225 exists and suggests that no better one may exist. It does not prove global optimality." (S38 §10.4)

**J5. State the price and the scope.** [stated]
- Caption-derived (S41 [0:31:05]): "the price you have to pay here is it takes four or five orders of magnitude more for Alamo to run again because uh lasso does something very simple based on some quadratic programming stuff that's amazingly fast uh but if you do have the time uh to build uh models uh you will be able to build better models with Alamo simpler and and and better" (*ASR*)
- "The issues of explicit or hidden constraints and noise in the objective function calculation have not been addressed in this paper. These issues are complex and warrant further study on their own." (S18, 2013, p. 1287; *co*)
- "It is impossible to give broad advice for all conceivable situations and the experiments in this paper and the two discussed can only capture a portion of the range of problem configurations. There is still progress to be made in translating experimental results into specific prescriptions." (S32, 2020, p. 9; *co*)
- Caption-derived (S40 [0:20:42]): "the fact is these are every hard problems so you take the wrong ter the BR B three you may end up you know taking too too long to to get the final solution but the bottom line is chances are about 60 some per or 70 some per that you will be able to solve your problem" (*ASR*). In the same passage [0:20:42] he concedes "there's some other solice in there that that are doing better than Baron for for some of these problems" (*ASR*).

**J6. Editorial standards: high rejection rates, fast and good reviews.** [stated · primary · sole]
- "Since January 1, 2018, OPTE's rejection rates are over 83%, and the average time to first decision for accepted manuscripts is 109 days." (S28d, 2019, p. 964)
- "Thanks are also due to the referees who offered high-quality reviews in a timely manner, thus making possible the publication of this issue in about a year's time after papers were submitted." (S28b, p. 304)

### 2.6 Writing and talks

**W1. What a book should do.** [stated · primary · co] "In writing this book we had three aims. First, to provide a very comprehensive account of material previously available only in journals. Second, to offer a unified and cohesive treatment of a wealth of ideas at the operations research and computer science interface. Third, to present (in over half of the book) new material, including new algorithms, a detailed description of the implementation, extensive computational results, and many geometric interpretations and illustrations of the concepts throughout the book." (S11, p. xv). The preface then maps chapters to three kinds of reader (convex analysis; implementation and computation; modelling and applications) (pp. xv–xvi) and promises "To facilitate developments in these directions, we plan to maintain detailed descriptions of many of the models used in this book as well as other related information" online (p. xvi).

**W2. What a review should do.** [stated]
- "The main purpose of this paper is to provide a short overview of the field and give pointers to the literature that can be used as starting points for further study." (S13, 2003, p. 153; *sole*)
- "The main purpose of the paper is to offer an introduction and motivate further systems approaches to these problems." (S17, 2009, abstract; *sole*)
- "It is intended to be approachable for the absolute beginner as well as useful to the seasoned CAMD practitioner." (S23, 2017 abstract; *co*)
- [inferred] His reviews and talk abstracts close with challenges, future directions or open problems: S13 ("There are several challenges"), S20 (a numbered list of nine directions, pp. 372–373), S35 ("we identify several related open problems and opportunities"). His comparison papers close on portfolio advice (J1).

**W3. Talk structure.** [stated · ASR] Caption-derived.
- 2025 (S41 [0:02:16]): "I'm going to go gradually from algebraic to algebraic plus some black box and then to eventually entirely black box and explain why we uh look at these problems how we actually combine some elements of machine learning to make things work out and how uh we saw problems at the end"
- 2017 (S40 [0:01:51]): "I'll try to relate uh what it is that we do to work that's out there and also the kinds of applications systems type of applications that have motivated this work". His 2017 close [0:54:43]: "at this point the code is available I invite you to use it and let us know how it works" (B4).

**W4. What a journal should publish (OPTE editor-in-chief, 2018–2023).** [stated · primary · sole] (B8)
- "Rosenbrock made excellent contributions in bridging the gap between optimization and engineering, which is also the primary focus of OPTE. ... OPTE publishes high-quality articles at the interfaces between engineering and optimization." (S28a, 2018, p. 814)
- "I encourage submissions of high-quality papers exploring optimization algorithms, software, and theory, and the interfaces between optimization and engineering." (S28d, 2019, p. 964)
- "Researchers from around the world are encouraged to submit high-quality papers exploring algorithms, software, and theory at the interface of optimization and engineering." (S28e, 2020, p. 708)
- "We invite researchers to submit high-quality papers discussing algorithms, applications, and theory at the intersection of optimization and engineering." (S28f, 2021, p. 1980; nearly the same in S28g, 2022 and S28h, 2023). From 2021 on, "software" drops out of the call (CH4).
- In the same years: "As OPTE increases its emphasis on core optimization theory and algorithms, we anticipate that MINLP will be addressed by many papers that we publish." (S28b, 2019, p. 304; see C6)

### 2.7 Research organisation: students, industry, firm, collaborators

**O1. A centre's mission is training, through industry-posed problems.** [stated · primary · co] (S24, *Chem. Eng. Educ.* 2018, written with Biegler and Grossmann while he directed CAPD)
- "Our research goals are to understand complex design and operation issues faced by industry, and to develop and advance modeling and solution methods for process systems engineering." (p. 33)
- "Most importantly, our main mission is to train future researchers and educators in the PSE field." (p. 34)
- "These companies typically supply case-study projects that are undertaken by PSE faculty and students." (p. 34)
- "Research in process systems engineering is a complex synthesis of applied mathematics, operations research, and control theory, as well as basic science." and "Each lecture day balances theory, algorithms, and applications." (p. 36)
- "Towards this end, we have found that there exists a strong interplay between research and teaching that results in the development of high quality educational materials, including lecture material and software that, in turn, catalyze further research advances." (p. 37)
- Resource context: CAPD research "is carried out by more than 70 graduate students and researchers" and supported by "more than 20 industrial member companies" (pp. 33–34).

**O2. Transfer technology through a firm and give free access.** [stated · primary · sole] "For users who need free access to optimization software, the full commercial versions of AMPL/BARON and GAMS/BARON are freely available through the NEOS server with free CPU cycles. This multi-pronged approach to technology transfer aims for maximum impact in the academic and commercial worlds." (S01, CV §IV.F, p. 49). Software should be easy to get: "We wholeheartedly encourage researchers to post their executable files, if not their source code. This could not only encourage practitioners to use these techniques in practice, but allow for comparisons between methods and the development of standardized interfaces between simulations and simulation optimization software." (S20, 2016, p. 372; *co*). "Accessibility of fast implementations that are also functionally labor-saving (e.g. by giving full solution paths, cross-validating, etc.) is paramount for the adoption of any estimator. If a user cannot quickly find an implementation for a new algorithm online, they will just use an established method." (S32, 2020, p. 7; *co*) (B4)

**O3. Students and collaborators bring the topics.** [stated]
- "I am grateful to my former students M. L. Liu and S. Ahmed who introduced me to many of the topics discussed in this paper." (S13, 2003, p. 161; *sole*)
- "I am grateful to my former doctoral students A. B. Smith, A. Vaia, and W. Xie for extensive discussions on the topics addressed in this paper." (S17, 2009; *sole*)
- Caption-derived (S40 [0:02:05]): "Allison was the first PhD student that worked on this project uh David Miller is our collaborator from the Department of energy he's motivated quite a bit of this work actually and contributed to it and uh Zach Wilson is a current PhD student working on the project" (*ASR*)

**O4. Choose environments and colleagues.** [stated · secondary · press] "ISyE has the world's best optimization group – and a top machine learning group, too. I am excited that I am working with [Institute Emeritus Professor] George Nemhauser and [A. Russell Chandler III Professor] Santanu Dey on some problems ... that our field has struggled for decades to solve," and "It is truly exciting to be at Georgia Tech, where I can collaborate with world-class colleagues and graduate students on optimization and its applications" (S42, 2021; the brackets are the journalist's).

**O5. Becoming partly an experimentalist through students' lab work.** [stated · ASR] Caption-derived (S41 [0:55:36]): "all this is in the lab this is my students fingures basically we we I'm now partly an experimentalist I'm not just doing the and cing" and his outlook [0:56:34]: "we mostly excited about is potential applications in the context of going into the lab optimizing devices and the likes with uh technology that basically relies on optimization and machine learning in uh a synchronized uh way". Context: Georgia Tech perovskite solar-cell work; the CV lists a doctoral student "co-supervised with Juan-Pablo Correa-Baena in MSE" (S01) [practice].

**O6. Persistence over decades.** [stated] "Arne Drud, Alex Meeraus, and Mike Saunders deserve thanks for encouraging us over the past decade to continue the development of BARON." (S11, 2002, p. xvii; *co*); "things did not happen overnight uh it took a long time to get here" (S41 [0:20:06], caption-derived).

**O7. Interdisciplinary training structures.** [stated · primary · co, seven authors] On the UIUC bioinformatics M.S. (his CV: "He has developed a bioinformatics M.S. program", S01, p. 1): "this is the first interdisciplinary program that grants degrees and formally recognises departmental specialisation areas. The program, which is not owned by any particular department but by the Graduate College itself, is operated in a franchise-like fashion via several departmental concentrations." (S16, 2005 abstract)

**O8. Self-placement at an interface.** [stated] (B8) "a unified and cohesive treatment of a wealth of ideas at the operations research and computer science interface" (S11, 2002, p. xv; *co*); "His current research activities are at the interface between computer science and operations research" (S02, site bio, third person); "Professor Sahinidis conducts research at the interface of optimization, machine learning, and computational science." (S01, CV 2026, third person); caption-derived (S41 [0:00:25]): "I'm going to talk about um certain things happening at the interface between computer science and operations research machine learning and optimization" (*ASR*).

**O9. Recruiting and the advisor's values (thin evidence).** [stated]
- "Almost every year, there are openings in my research group for exceptional graduate students." (S03; the rest of the page is admissions procedure)
- A tribute to his own Ph.D. advisor, co-written with three colleagues: "Ignacio approaches both life and research with a great sense of high standards, dedication to his students and colleagues and caring for others." (S30, 2019, PDF p. 1; *co*). Whether this states his own creed is not known.
- Caption-derived (S41 [0:36:59], see T5): when students propose "fancy" neural networks, his evidence of simple models "give[s] me a pause". This is the only first-hand glimpse of how he responds to students' proposals.

---

## 3. Failures, limits and dead ends he states himself

No retraction, erratum statement or admitted error of judgment in his own words was found. What he does state:

1. **The early general-MINLP attempt stalled** and he retreated to special classes (P1; S11, pp. xiii–xiv).
2. **Humble beginnings**: "could barely solve one in three problems" (S41 [0:19:26], caption-derived); "about 5-10%" when he started on a hard library (S42, 2021).
3. **Others beat his solver on some problems**: "there's some other solice in there that that are doing better than Baron for for some of these problems" (S40 [0:20:42], caption-derived). His 2019 editorial lists tailored methods that "outperform BARON" (S28b, pp. 303–304).
4. **Scope he left out**: constraints and noise (S18, p. 1287); the limits of empirical advice (S32, p. 9).
5. **Limits of his tool, written into the manual**: "Other functions, including trigonometric functions such as sin(x), cos(x), are not currently supported." (S38 §6.1); convex models may be solved faster by a local solver (§4); a multistart run is not a proof (§10.4).
6. **A lost lead**: caption-derived (S41 [0:54:54]): "he tied up the world record for photo voltages for this particular type of peros skyp four months ago another paper has come out that's now closer to 26% in terms of efficiency but I'm still optimistic because we are not even fully optimized here in in 6D".
7. **What he does not understand**: on DIRECT, "although his geometric arguments are Beyond me I don't understand" (S41 [0:50:26], caption-derived).
8. **A finding he did not expect**: "this is something I did not expect when we were you know going into this I didn't know what to expect rather" (S41 [0:36:59]; that small quadratic surrogates sufficed).
9. **An accepted paper that never appeared**: "accepted in 2009 although the guest editor never forward [sic] the proceedings issue to the publisher." (S01, CV)
10. **Announced, apparently not delivered**: "SBH: software for finding all near-optimal solutions of the combinatorial problem in DNA sequencing by hybridization—forthcoming." and "We are currently working to develop similar algorithms for non-centric compounds, including proteins." (S05, undated). Whether these appeared is a practice question; 01 §3 item 7 found no matching paper.

---

## 4. How his statements changed over time (dated, not reconciled)

- **CH1. Relaxations.** 2002: "entirely linear" relaxations for "robust and established linear programming techniques" (S11). 2005: NLP codes "significantly slower and numerically unstable" (S15). 2018: "we introduce a new relaxation paradigm" combining "polyhedral and convex nonlinear relaxations" (S26). 2019: "portfolios or [sic] linear and nonlinear relaxations" (S31). The reasons given (speed, robustness) stay the same; the conclusion changed as NLP solvers matured [inferred].
- **CH2. Why simple surrogates.** 2014–2018: simplicity so that "my models will be more amable to Global optimization" (S40, 2017); interpretation "a bonus ... not a requirement in my context". 2025: "the interesting thing with an interpretable machine learning technique like Alamo is you can look at the model" (S41 [0:35:53]) and "the cool thing is that MLP is serving as a technology to do interpretable ml" (S41 [0:56:09]), both caption-derived. 2026: "interpretable models that are simple but effective" (S37).
- **CH3. Self-placement.** "operations research and computer science interface" (2002, S11; site S02) changes to "the interface of optimization, machine learning, and computational science" (CV 2026, S01).
- **CH4. OPTE's call for papers.** "algorithms, software, and theory" (2019 S28d; 2020 S28e) changes to "algorithms, applications, and theory" (2021–2023 S28f–h).
- **CH5. Benchmark-progress figures**: 2021 and 2025 differ (C5).
- **CH6. BARON's purpose.** "BARON: A general purpose global optimization software package" (1996 note, *J. Glob. Optim.* 8:201–205, DOI 10.1007/BF00138693, title only; also "A general purpose solver for mixed-integer nonlinear optimization problems.", S10). In 2002: "Its initial purpose was to facilitate design and experimentation with global optimization algorithms." (S11, p. xiv). (Also 01 C12.)

---

## Contradictions (kept, not reconciled)

- **C1. General-purpose or problem-specific?** For generality: "Application agnostic algorithms ... that was what particularly fascinated me" (2021, S42); "all-purpose" (S04); "completely automated" (2002, S11); the 2022 prize citation from a committee including him praises "the generic approach" for "speedups over the existing, domain-specific approaches" (S28h). Against: "It appears unlikely that general-purpose algorithms will solve such problems exactly. Instead, we expect to see the development of problem-specific approximation schemes" (2003, S13); "Many of the papers develop tailored algorithms that outperform general-purpose MINLP solvers." (2019, S28b, p. 304); and his own manual: "Tight bounds based on physical or problem-specific knowledge are often more valuable than any algorithmic option in this manual." (2026, S38 §4.1).
- **C2. Convenience or simplicity at any cost?** "In practice, convenience is the most important factor for the average modeler who is considering various methods." (2020, S32, p. 7). For the general case: "we would not turn to the cardinality-constrained estimators CIO/SS ... because of the relatively demanding computational time needed and lack of seamless hyperparameter selection and tuning" (S32, p. 9). Yet ALAMO is best-subset selection by integer programming: "yes exactly the objective is to go for the simplest possible model we can find" (S40 [0:39:40], caption-derived, answering a question). In 2025 he accepts "four or five orders of magnitude more" time for "better models" (S41).
- **C3. Speed as precondition, or not?** Relaxations: "Their potential can be realized only if they can be solved with sufficient speed and reliability." (2005, S15). Model building: orders-of-magnitude slower is acceptable "if you do have the time" (2025, S41). The contexts differ (node subproblem vs offline fitting); he does not reconcile them.
- **C4. Interpretability: optional or central?** "that's a bonus uh it's not a requirement in my context" (2017, S40) against the 2025–2026 framing (CH2).
- **C5. Progress numbers.** 2021: "about 5-10%" to "about two-thirds" of "a famous collection of challenging test problems ... nuclear reactor management, facility location, pipeline design" (S42, press). 2025: "could barely solve one in three problems" to "almost the entire collection" of "a collection of problems that I don't necessarily like but somebody else has been using up until very recently to to Benchmark Mi NLP solvers" (S41, caption-derived). Whether these are two collections is not said.
- **C6. Engineering interface or core theory?** OPTE's "primary focus" is "bridging the gap between optimization and engineering" (2018, S28a), yet "OPTE increases its emphasis on core optimization theory and algorithms" (2019, S28b). Both are his editorials.
- **C7. Open code, closed solver** [inferred tension]. He commends authors "for making the code for their research available open-source" (2020, S32, p. 2) and "wholeheartedly encourage[s] researchers to post their executable files, if not their source code" (2016, S20). BARON, his main tool, is a commercial product of his firm, with free access through NEOS (S01). The 2016 wording ("executable files, if not their source code") fits his own model. I found no statement of his on this trade-off.
- **C8. BARON's original purpose**: see CH6.
- **C9. Rigor or heuristics?** He states "rigorous" methods and "only the branch-and-bound search can provide that guarantee" (S04, S38). He also seeks "provably optimal heuristics" (S07) and, as editor, accepts heuristics backed by a convex-relaxation bound (S28b, p. 304). These may be compatible ("rigor in the use and practice of heuristics"); kept as stated.

---

## Gaps

1. **No first-person account of method.** No essay, interview, podcast, oral history or blog on how he chooses problems, runs a group, writes, or advises students was found. Searched: his group site, CV, the INFORMS and Georgia Tech pages, YouTube search pages, Crossref; 3 WebSearch calls (interview/advice; Texas A&M dialogue; quoted statements).
2. **Award lectures not found**: the CAST Computing in Chemical Engineering Award Lecture "Computing in Chemical Engineering: Three decades in the development of algorithms and software" (Salt Lake City, Nov 2010, per S01), likely his most reflective talk; no text, slides or recording found. Khachiyan Prize 2026 (CV): no citation or acceptance text found. Beale–Orchard-Hays 2006: not searched.
3. **Plenaries without text or recording**: CAST plenary 2002 ("Challenges in informatics"), ICCOPT 2007, AIChE centennial plenary 2008, ISMP 2018 semi-plenary "The BARON software for MINLP", IOS 2024 plenary, the ICERM talks (2023, 2024), MIP 2023, the IOS 2026 talk "Automated design of algorithms" (with I. Mitrai), and the Texas A&M Barnes '64 Distinguished Dialogue (2024). In the 2025 Texas A&M talk he says his visit the year before had "the same" title.
4. **Not read (access)**: OPTE "Prologue" editorials with Grossmann (2002, 2003; paywalled; S53); the full text of the 2005 bioinformatics-programme paper (abstract only; S52); four *Interfaces* book reviews, 1995–2008 (paywalled; only the 1996 *Optima* review was read); Kılınç & Sahinidis 2017 SIAM chapter "State-of-the-art in mixed-integer nonlinear programming"; the journal version of the 2004 uncertainty review (FOCAPO version read); "Forty years of Computers and Chemical Engineering: Analysis of the field via text mining techniques" (*CACE* 129:106511, 2019, DOI 10.1016/j.compchemeng.2019.106511; closed); the SIAM Review paper with Kuznetsov "Nonconvex optimization problems involving the Euclidean norm: Challenges, progress, and opportunities" (CV: accepted 2025; not found in Crossref or arXiv on 2026-10-10).
5. **Blocked pages**: CityU ADSE seminar 2022–23 #17 (bot protection; S49); PANOPTIC 2023 programme book (HTTP 404; S50); University of Houston Rockwell Lecture 2024 page (HTTP 403; S51); INFORMS Optimization Society newsletter archive (login; S54). He chaired the Society in 2009–2010; any chair's column is unread.
6. **Talks**: the 2021 PSEforSPEED webinar on refrigerant design has no captions and was not transcribed (S55). The two talks used here are automatic captions only and were not checked against audio. Two INFORMS 2020 tutorials from his firm were presented by staff, not by him, and were excluded (S48).
7. **MPC editor-in-chief (2025–)**: no editorial or policy statement found.
8. **Layers with almost no stated evidence**: writing process (drafting, revising, choosing venues); handling referees and rebuttals; when to abandon a project; lab-meeting and supervision routines; time allocation. Layer 7 evidence is institutional (CAPD, firm) more than personal.
9. **Undated web pages**: S04–S10 carry no dates; their eras are inferred.

---

## Candidate stated heuristics for Phase 2 (all [inferred] summaries of the [stated] items above; not yet checked against practice, which is agent 03's job)

1. Before building, check whether any software solves even small instances; if not, that gap is the project (P1, P3).
2. If the general problem stalls, solve special classes first and build the platform there; generalize later (P1).
3. Judge a relaxation or model by strength *and* speed and robustness together (T6).
4. Reduce the domain before branching; run the cheapest reduction first (I5).
5. Benchmark at default settings with identical starts and bounds; iterate with developers but confirm on unseen problems; report per library (X1, X2, X4).
6. Conclude with portfolios, not a single winner (J1).
7. Prefer the simplest model that is accurate; reject it if it violates physics (T5, J2).
8. Put physical and problem knowledge into bounds and constraints before tuning algorithmic options (X5).
9. Ship the method as a usable tool, with versioned, reproducible runs and shared data (B4, X6).
10. Draw problems from applications and users; let them reshape the algorithm (P5, I3, I4).

---

## Sources

S01. N. Sahinidis, Curriculum vitae (footer dated 7 Oct 2026; PDF created 9 Oct 2026), https://sahinidis.coe.gatech.edu/sites/default/files/content/nikos/NVS%20cv.pdf — primary
S02. Sahinidis Optimization Group, "Nick Sahinidis" bio page (undated, read 2026-10-10), https://sahinidis.coe.gatech.edu/nick — primary
S03. Sahinidis Optimization Group, "Student Openings" (undated), https://sahinidis.coe.gatech.edu/student-openings — primary
S04. Sahinidis Optimization Group, Research: "Global optimization" (undated), https://sahinidis.coe.gatech.edu/research/global-optimization — primary
S05. Sahinidis Optimization Group, Research: "Informatics" (undated), https://sahinidis.coe.gatech.edu/research/informatics — primary
S06. Sahinidis Optimization Group, Research: "Black-box optimization and machine learning" (undated), https://sahinidis.coe.gatech.edu/research/black-box-optimization-and-machine-learning — primary
S07. Sahinidis Optimization Group, Research: "Process synthesis & operations" (undated), https://sahinidis.coe.gatech.edu/research/process-synthesis-operations — primary
S08. Sahinidis Optimization Group, Research: "Test problems for SO and DFO algorithms" (undated), https://sahinidis.coe.gatech.edu/research/test-problems-so-and-dfo-algorithms — primary
S09. Sahinidis Optimization Group, Software: "ALAMO", "Motivation", "Technical Brief" (undated), https://sahinidis.coe.gatech.edu/software/alamo (and /motivation, /technical-brief) — primary
S10. Sahinidis Optimization Group, Software: "BARON Software" (undated), https://sahinidis.coe.gatech.edu/software/baron-software — primary
S11. M. Tawarmalani and N. V. Sahinidis, *Convexification and Global Optimization in Continuous and Mixed-Integer Nonlinear Programming* (Kluwer, 2002, NOIA 65), Preface pp. xiii–xvi and Acknowledgments pp. xvii–xviii, DOI 10.1007/978-1-4757-3532-1 (free front matter https://link.springer.com/content/pdf/bfm:978-1-4757-3532-1/1) — primary (co)
S12. N. V. Sahinidis, review of C. A. Floudas and P. M. Pardalos (eds.), *State of the Art in Global Optimization: Computational Methods and Applications*, *Optima* 52:12–13, Dec 1996, http://www.mathprog.org/Optima-Issues/optima52.pdf — primary (sole)
S13. N. V. Sahinidis, "Optimization under uncertainty: state-of-the-art and opportunities", FOCAPO 2003 Proceedings, pp. 153–162, https://skoge.folk.ntnu.no/prost/proceedings/focapo_2003/pdffiles/papers/014.pdf (journal version *Comput. Chem. Eng.* 28:971–983, 2004, DOI 10.1016/j.compchemeng.2003.09.017, not read) — primary (sole)
S14. N. V. Sahinidis and M. Tawarmalani, "Accelerating branch-and-bound through a modeling language construct for relaxation-specific constraints", *J. Glob. Optim.* 32:259–280, 2005, DOI 10.1007/s10898-004-2705-8 (abstract) — primary (co)
S15. M. Tawarmalani and N. V. Sahinidis, "A polyhedral branch-and-cut approach to global optimization", *Math. Program.* 103:225–249, 2005, DOI 10.1007/s10107-005-0581-8 (abstract) — primary (co)
S16. N. V. Sahinidis, M. T. Harandi, M. T. Heath, L. Murphy, M. Snir, R. P. Wheeler and C. F. Zukoski, "Establishing a master's degree programme in bioinformatics: challenges and opportunities", *IEE Proc. Syst. Biol.* 152(4):269–275, 2005, DOI 10.1049/ip-syb:20050033 (abstract via PubMed PMID 16986270) — primary (co)
S17. N. V. Sahinidis, "Optimization techniques in molecular structure and function elucidation", *Comput. Chem. Eng.* 33(12):2055–2062, 2009, DOI 10.1016/j.compchemeng.2009.06.006 (author manuscript PMC2771738) — primary (sole)
S18. L. M. Rios and N. V. Sahinidis, "Derivative-free optimization: a review of algorithms and comparison of software implementations", *J. Glob. Optim.* 56:1247–1293, 2013, DOI 10.1007/s10898-012-9951-y — primary (co)
S19. A. Cozad, N. V. Sahinidis and D. C. Miller, "Learning surrogate models for simulation-based optimization", *AIChE J.* 60(6):2211–2227, 2014, DOI 10.1002/aic.14418 (abstract) — primary (co)
S20. S. Amaran, N. V. Sahinidis, B. Sharda and S. J. Bury, "Simulation optimization: a review of algorithms and applications", *Ann. Oper. Res.* 240:351–380, 2016, DOI 10.1007/s10479-015-2019-x (also arXiv:1706.08591) — primary (co)
S21. Z. T. Wilson and N. V. Sahinidis, "The ALAMO approach to machine learning", arXiv:1705.10918v1 (31 May 2017); *Comput. Chem. Eng.* 106:785–795, 2017, DOI 10.1016/j.compchemeng.2017.02.010 — primary (co)
S22. Y. Puranik and N. V. Sahinidis, "Domain reduction techniques for global NLP and MINLP optimization", arXiv:1706.08601v1 (2017); *Constraints* 22:338–376, 2017, DOI 10.1007/s10601-016-9267-5 — primary (co)
S23. N. D. Austin, N. V. Sahinidis and D. W. Trahan, "Computer-aided molecular design: An introduction and review of tools, applications, and solution techniques", arXiv:1701.03978 (abstract) — primary (co)
S24. L. T. Biegler, I. E. Grossmann and N. V. Sahinidis, "The Center for Advanced Process Decision-making at Carnegie Mellon" (Lifelong Learning column), *Chem. Eng. Educ.* 52(1):33–37, Winter 2018, DOI 10.18260/2-1-370.660-29480 — primary (co)
S25. N. V. Sahinidis, "ALAMO: Machine learning from data and first principles" (talk abstract), in P. Bonami, A. M. Gleixner, J. Linderoth and R. Misener, *Designing and Implementing Algorithms for Mixed-Integer Nonlinear Optimization* (Dagstuhl Seminar 18081), *Dagstuhl Reports* 8(2):64–87 (p. 81), 2018, DOI 10.4230/DagRep.8.2.64 — primary (sole)
S26. A. Khajavirad and N. V. Sahinidis, "A hybrid LP/NLP paradigm for global optimization relaxations", *Math. Program. Comput.* 10:383–421, 2018, DOI 10.1007/s12532-018-0138-5 (abstract) — primary (co)
S27. A. Cozad and N. V. Sahinidis, "A global MINLP approach to symbolic regression", *Math. Program.* 170:97–119, 2018, DOI 10.1007/s10107-018-1289-x (abstract) — primary (co)
S28a. N. V. Sahinidis, "Announcement: Howard Rosenbrock Prize 2017", *Optim. Eng.* 19:813–814, 2018, DOI 10.1007/s11081-018-9397-2 — primary (sole; the prize citation is by the committee)
S28b. N. V. Sahinidis, "Mixed-integer nonlinear programming 2018" (editorial), *Optim. Eng.* 20:301–306, 2019, DOI 10.1007/s11081-019-09438-1 — primary (sole)
S28c. N. V. Sahinidis, "Announcement: Howard Rosenbrock Prize 2018", *Optim. Eng.* 20:961–962, 2019, DOI 10.1007/s11081-019-09458-x — primary (sole; citation by committee)
S28d. N. V. Sahinidis, "Status report for optimization and engineering", *Optim. Eng.* 20:963–964, 2019, DOI 10.1007/s11081-019-09473-y — primary (sole)
S28e. N. V. Sahinidis, "Announcement: Howard Rosenbrock Prize 2019", *Optim. Eng.* 21:707–708, 2020, DOI 10.1007/s11081-020-09533-8 — primary (sole; citation by committee)
S28f. N. V. Sahinidis, "Announcement: Howard Rosenbrock Prize 2020", *Optim. Eng.* 22:1979–1980, 2021, DOI 10.1007/s11081-021-09649-5 — primary (sole; citation by committee)
S28g. N. V. Sahinidis, "Announcement: Howard Rosenbrock Prize 2021", *Optim. Eng.* 23:1215–1216, 2022, DOI 10.1007/s11081-022-09730-7 — primary (sole; citation by committee)
S28h. N. V. Sahinidis, "Announcement: Howard Rosenbrock Prize 2022", *Optim. Eng.* 24:1461–1462, 2023, DOI 10.1007/s11081-023-09805-z — primary (sole; citation by a committee that included him)
S29. J. Liu, N. Ploskas and N. V. Sahinidis, "Tuning BARON using derivative-free optimization algorithms", *J. Glob. Optim.* 74:611–637, 2019, DOI 10.1007/s10898-018-0640-3 (abstract) — primary (co)
S30. L. Biegler, C. Gounaris, N. V. Sahinidis and B. E. Ydstie, "Educator Profile: Ignacio Grossmann of Carnegie Mellon University", *Chem. Eng. Educ.* 53, 2019, DOI 10.18260/2-1-370.660-114401 — primary (co)
S31. N. V. Sahinidis, "Recent developments in the BARON project" (talk abstract), in L. Liberti, S. Sager and A. Wiegele, *Mixed-integer Nonlinear Optimization: a hatchery for modern mathematics*, *Oberwolfach Reports* 16(2):1573–1637 (pp. 1622–1623), workshop June 2019, published 2020, DOI 10.4171/OWR/2019/26 — primary (sole)
S32. O. Sarwar, B. Sauk and N. V. Sahinidis, "A Discussion on Practical Considerations with Sparse Regression Methodologies", *Stat. Sci.* 35:593–601, 2020, DOI 10.1214/20-STS806; page numbers cited from arXiv:2011.09362v2 — primary (co)
S33. C. S. Adjiman, N. V. Sahinidis, D. G. Vlachos, B. Bakshi, C. T. Maravelias and C. Georgakis, "Process Systems Engineering Perspective on the Design of Materials and Molecules", *Ind. Eng. Chem. Res.* 60:5194–5206, 2021, DOI 10.1021/acs.iecr.0c05399; page numbers cited from the accepted manuscript https://www.osti.gov/servlets/purl/1777106 (the CV gives the title as "A Perspective on Systematic Design of Materials and Molecules") — primary (co)
S34. N. Ploskas and N. V. Sahinidis, "Review and comparison of algorithms and software for mixed-integer derivative-free optimization", *J. Glob. Optim.* 82:433–462, 2022, DOI 10.1007/s10898-021-01085-0 — primary (co)
S35. N. V. Sahinidis, abstract of "Convexification and optimization of problems involving the Euclidean norm", ISyE Seminar, Georgia Tech, 18 Oct 2024, https://www.isye.gatech.edu/node/11714 (same abstract for the Lehigh Spencer C. Schantz Distinguished Technical Talk, 3 Dec 2024, https://engineering.lehigh.edu/node/170818) — primary (talk abstract)
S36. Y. Zhang and N. V. Sahinidis, "Solving continuous and discrete nonlinear programs with BARON", *Comput. Optim. Appl.* 92:1123–1161, 2025, DOI 10.1007/s10589-024-00633-0 (abstract) — primary (co)
S37. S. Bayramoğlu, G. L. Nemhauser and N. V. Sahinidis, "Speeding Up Mixed-Integer Programming Solvers with Sparse Learning for Branching", arXiv:2604.00094v1, 31 Mar 2026 (abstract) — primary (co)
S38. N. Sahinidis, The Optimization Firm, "BARON user manual and installation guide", v. 2026.9.10, 10 Sep 2026, https://minlp.com/baron-user-manual (sections 4, 4.1, 5.1, 5.3, 5.6, 6.1, 6.2, 7.2, 8.5, 10.2, 10.4, 13.2) — primary (sole author line; firm document)
S39. The Optimization Firm, "About The Optimization Firm" (undated), https://www.minlp.com/node/5 — primary (firm voice)
S40. N. Sahinidis, "The ALAMO Approach to Machine Learning: Best Subset Selection, Adaptive Sampling, and Constrained Regression", UConn Institute for Advanced Systems Engineering distinguished lecture, 10 Apr 2017, https://www.youtube.com/watch?v=BZ76x6VWllA; transcript (automatic captions) `../sources/talks/2017-04-10_uconn-iase-alamo-approach-to-machine-learning_BZ76x6VWllA_auto-captions.txt` — primary (ASR)
S41. N. Sahinidis, "Optimization and Machine Learning Nexus: Model-Based and Data-Driven Approaches", Texas A&M Energy Institute Distinguished Lecture Series in Energy, 5 Mar 2025, https://www.youtube.com/watch?v=E320mxWiR24 (event page https://energy.tamu.edu/event/distinguished-lecture-series-in-energy-dr-nick-sahinidis/); transcript (automatic captions) `../sources/talks/2025-03-05_tamu-energy-optimization-ml-nexus_E320mxWiR24_auto-captions.txt` — primary (ASR)
S42. S. Wunder-Smith, "Nick Sahinidis Joins ISyE as Inaugural Butler Family Chair", ISyE News, Georgia Tech, 15 Jul 2021, https://www.isye.gatech.edu/news/nick-sahinidis-joins-isye-inaugural-butler-family-chair — secondary (press; direct quotes)
S43. ISyE News, "ISyE Welcomes Nick Sahinidis", 19 Aug 2020, https://www.tlwarc.hg.gatech.edu/node/638074 — secondary (no quotes; context only)
S44. Texas A&M Hagler Institute for Advanced Study, "Dr. Nick Sahinidis" (Class of 2024–25), https://hias.tamu.edu/fellow/dr-nick-sahinidis/ — secondary (context only)
S45. GAMS, "Nick Sahinidis Elected to National Academy of Engineering", blog, 11 Feb 2022, https://gams.com/blog/2022/02/nick-sahinidis-elected-to-national-academy-of-engineering/ (quotes the NAE citation) — secondary (observed)
S46. INFORMS, award recipient page "Nikolaos V. Sahinidis" (2004 INFORMS Computing Society Prize citation), https://www.informs.org/Recognizing-Excellence/Award-Recipients/Nikolaos-V.-Sahinidis — secondary (observed)
S47. MIT ChemE, "2040 Visions of Process Systems Engineering: Session 8 (June 2, 2017)", https://www.youtube.com/watch?v=BMq-2TZhJhU (human subtitles; I. E. Grossmann's talk mentions BARON; not Sahinidis's voice) — secondary (observed)
S48. The Optimization Firm, INFORMS 2020 tutorials "Recent Advancements in BARON" (https://www.youtube.com/watch?v=AylMD77G_NM) and "Interpretable Analytics and Machine Learning with ALAMO" (https://www.youtube.com/watch?v=zxKViA0bPyo), presented by firm staff (A. Kishi, Y. Puranik), not by him; consulted and excluded — secondary
S49. City University of Hong Kong, ADSE Distinguished Seminar 2022–23 #17 (https://cityu.edu.hk/adse/seminar_2022-23_17.htm and the PDF version) — not accessible (bot protection)
S50. PANOPTIC 2023 programme book, https://www.ise.ufl.edu/panoptic/files/2023/03/ProgramBook-Final.pdf — not accessible (HTTP 404)
S51. University of Houston, Rockwell Lecture 2024 page, https://www.egr.uh.edu/our-college/rockwell-lecture/2024/nick-sahinidis-nae — not accessible (HTTP 403)
S52. Full text of S16 at the IET Digital Library (https://digital-library.theiet.org/content/journals/10.1049/ip-syb_20050033) — not accessible (HTTP 403 challenge); abstract used via PubMed
S53. I. E. Grossmann and N. V. Sahinidis, "Prologue", *Optim. Eng.* 3:223–225, 2002, DOI 10.1023/A:1021012409434, and "Prologue", *Optim. Eng.* 4:5–6, 2003, DOI 10.1023/A:1021882112398 — not read (paywalled)
S54. INFORMS Optimization Society newsletter archive, https://connect.informs.org/optimizationsociety/newsletter — not read (login required)
S55. PSEforSPEED Webinar 3, "Optimization approaches to refrigerant design" (N. Sahinidis), 16 Aug 2021, https://www.youtube.com/watch?v=Qd-UP8eAq0U — not transcribed (no captions available)

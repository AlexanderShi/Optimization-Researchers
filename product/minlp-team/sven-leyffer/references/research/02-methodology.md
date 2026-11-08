# Sven Leyffer · Research note 02 · Stated methodology (what he says research should be)

| Field | Value |
|---|---|
| Researcher | Sven Leyffer (living). Argonne National Laboratory, Mathematics and Computer Science Division; PhD University of Dundee (thesis dated December 1993) with Roger Fletcher |
| Dimension | Phase 1, research agent 02 of 06 (nuwa research-craft): what he CLAIMS research should be, sorted into the seven layers of framework §一 |
| Research date | 2026-10-10 |
| Sources consulted | 41 (37 primary, 4 secondary), numbered S01-S41 under Sources, plus two verification services (Crossref, Internet Archive CDX; S42, S43). Sibling notes 01 and 04 were read for leads only and are not counted |
| Web searches | 3 of the 3 allowed. None found an interview with Leyffer or an essay by him on how to do research. Everything below comes from direct fetches of known URLs, archived copies (Wayback), his GitHub repositories, and talk videos |
| Local corpus | `references/sources/{papers,talks,essays,software}` held only `.gitkeep` files when this run started: no user-supplied material. `private/` was not opened |
| Saved in this run | 16 talk transcripts (YouTube auto-captions) under `references/sources/talks/`: `2018-purdue-optimization-for-machine-learning.transcript.txt`, and 15 of his 33 lectures from a January 2024 course in `2024-iitb-gian-minlo/` (see its `INDEX.txt`) |

## How to read this file

- **[stated]** = Leyffer's own words, alone or as a coauthor; coauthored texts are marked "coauthored" because the words cannot be assigned to him alone. **[practice]** = what his papers, code or records show he did (used here only as context; that check belongs to agent 03). **[observed]** = what others say about him. **[inferred]** = my reading, with its basis. **P** = primary, **S** = secondary.
- **(ASR)** marks quotes from YouTube auto-generated captions. They are copied verbatim from the caption text, mis-hearings included, and were not checked against the audio. Treat the exact wording as approximate; where I gloss a garbled word, the gloss stands outside the quotation marks.
- **(AI-assisted)** marks 2026 documents in his GitHub repositories written with an AI assistant (a commit trailer names Claude, the file says so, or the repository is set up for one). They are committed under his name and record his choices, but individual sentences may be the assistant's wording. The conDFO brief (S35) is the exception: it came in his initial check-in without an AI trailer and carries hand-typed typos, so I treat it as his own text [inferred].
- **(Fletcher, endorsed)** marks words spoken by Roger Fletcher in the 2015 interview that Leyffer conducted, where Leyffer's reply agrees ("Right. Absolutely."), or values that Leyffer himself named as Fletcher's "research philosophy" in his 2016 obituary. They show what Leyffer chose to put on record, not his own formulation.
- Quotations are verbatim, typos included. Quotation marks inside a quotation are rendered as single quotes, LaTeX markup is removed where noted, and a symbol lost in text extraction (such as ∈ or ⇒) was restored from the slide image or left out.
- Page numbers are printed page numbers; slides are cited as "slide n" of the deck as printed. Where a text was reused in a later document, the reuse is noted and counted once.
- Scope: what he said. Where notes 01 or 04 already hold practice evidence on the same point, I give a pointer without judging whether practice matches.

---

## 0. Beliefs stated three or more times

Counting rule: one occasion = one dated text, talk, deck or repository. Survey paragraphs reused verbatim in the 2016 lecture notes count once (the reuse itself shows he kept the claim for four years).

| # | Belief (my summary; his words in §1-7) | Occasions (year: source) | Count | Layer |
|---|---|---|---|---|
| B1 | Modelling decides what can be solved: "linearize", prefer linear over convex over nonconvex formulations, model as MIP rather than NLP where you can | 2012/13 S07 pp. 11-12 (reused 2016 in S09); Feb 2013 S12 slides 36, 39, 66-67, 73; Sep 2016 S15 slides 25, 38; Sep 2018 S16 slide 12 and exercise 2; Jan 2024 S19 L01, L06, L07 (ASR) | 5 | 4 |
| B2 | The problems people want solved, and the sciences that bring them, should drive the research | 2010 S11; 2012 S08 p. vii; 2015 S02 p. 5 (Fletcher, endorsed); 2016 S03 p. 2; Sep 2016 S15 (02-apps slides 26, 37); 2018 S17 slide 7, S18 (ASR); 2024 S19 L01 (ASR) | 7 | 1, 2 |
| B3 | His programme is a base and its extensions: reliable nonlinear-optimization methods first, then extended to MINLP, complementarity constraints and PDE-constrained integer problems | 2005 S10 p. 1; 2012 S21; 2013 S12 (Socn-6 slide 88); 2016 S09 (subtitle); 2017 S01 p. 3 | 5 | 2 |
| B4 | Small examples and counterexamples expose a method's limits; learn from the worst case | 2006 S04 p. 6; 2015 S02 p. 4; 2016 S03 p. 2; 2017 S01 pp. 5, 9; 2024 S19 L14, L29 (ASR) | 5 | 1, 3, 5 |
| B5 | Software is part of the research: implement the method yourself, software validates theory, and shared frameworks lower the cost of new algorithms | 1998 S05 p. 2; 2015 S02 p. 4; 2016 S03 p. 2; 2017 S01 pp. 6, 9; 2024 S32; 2024 S19 L27 (ASR) | 6 | 4, 7 |
| B6 | Integrate across the NLP / MIP divide instead of decomposing along the lines of existing software packages | 1998 S05 p. 2; 2010 S11; 2012 S08 p. vii; 2013 S13 slide 8; 2015 S14 slide 15; 2017 S01 p. 5 | 6 | 2, 3 |
| B7 | Inside MINLP the NLP solver must warm-start well, so active-set (SQP-type) methods are preferred; this need steers which NLP research to do | 2005 S10 p. 1; 2010 S11 §2.2; 2012 S08 p. ix (coauthored, summarising chapters); 2013 S12 slide 36 | 4 | 2 |
| B8 | Build on what exists: existing solvers, models and proofs | 1993 S06 p. 14; 2017 S01 p. 9; 2024 S32, S33; 2024 S19 L09, L29 (ASR); 2026 S35 | 5 | 3, 4 |
| B9 | Describe algorithms by their building blocks and unify them in one framework | 2013 S12 (Socn-1 outline); 2016 S15 slide 38; 2017 S01 p. 6; 2024 S32, S33 | 4 | 3 |
| B10 | Say plainly where a method, a claim or one's own knowledge stops; name the open gaps | 1998 S05 p. 11; 2017 S01 pp. 5, 7; 2018 S18 (ASR); 2024 S19 L26, L45 (ASR); 2024-26 S34; 2026 S35, S36 | 7 | 1, 5 |
| B11 | When a solver struggles, read the numbers; the cause is often the formulation (an undefined function, a failed constraint qualification), not the method | 2012/13 S07 p. 12; 2015 S02 p. 4; 2016 S15 (24-MIPDECO slide 35); 2017 S01 pp. 7-9; 2024 S19 L30, L48 (ASR) | 5 | 4, 5 |
| B12 | Expose problem structure to the algorithm instead of treating functions as black boxes | 2016 S15 (02a-model slide 24); 2017 S01 p. 6; 2024 S19 L11, L35 (ASR) | 3 | 4 |
| B13 | Credit collaborators and predecessors; work with people whose expertise complements yours | 2006 S04 p. 2; 2013 S12 (Socn-6 slide 89); 2014 S20 slide 4; 2015 S02 p. 3; 2017 S01 pp. 3, 5 | 5 | 6, 7 |
| B14 | A method needs a convergence argument, and a result is only as meaningful as the guarantee behind it | 1993 S06 pp. 11-12; 2024 S19 L11 (ASR); 2026 S35 | 3 | 1, 5 |
| B15 | Keep a written trail of each research session: brief, dated plans, logbook, status file (AI-era working method) | 2026 S35 (his own text); 2026 S36, S37 (AI-assisted) | 3 (one year) | 4, 7 |

Not repeated three times, but notable single statements are flagged "(1x)" or "(2x)" in the sections below.

---

## 1. Research taste: what is worth doing, what a good result looks like

**1.1 Problems people want solved, not test-set records [B2].**
- 2015 [stated, P; (Fletcher, endorsed)] In the interview Leyffer conducted, Fletcher says: "Whatever the users want. It should be driven ultimately by what problems people want to solve. you sort of alluded to that in your talk today a bit about when you were saying test problems. And test problems are often very badly selected because they don't really model any situation that is of any practical relevance." Leyffer: "Right. Absolutely." Fletcher goes on: "I'd rather see half a dozen real industrial problems" (S02 p. 5). [observed, P] Fletcher's remark also reports that Leyffer's own talk that day had made a point about test problems; what he said there is not recorded (Gap).
- 2010 [stated, P] "Many scientific, engineering, and public sector applications involve both discrete decisions and nonlinear system dynamics that affect the optimality of the final design." (S11 §1)
- 2012 [stated, P, coauthored] "Of course, the wealth of applications that can be accurately modeled by using MINLP is not yet matched by the capability of available optimization solvers." (S08 p. vii)
- 2016 [stated, P] In his obituary of Fletcher he names this as the first foundation of Fletcher's research philosophy: "Roger emphasized the use of applications to drive his research. He believed that applications and numerical work help us understand a problem's challenges and an algorithm's limitations." and "He believed that the problems people want to solve should ultimately drive applied mathematics research, and valued simple examples to expose a method's limitations." (S03 p. 2)
- 2016 [stated, P] Course slides: "Complex science & engineering apps drive optimization:" and "Many open problems in need of new methods and ideas!" (S15, 02-apps slide 26); on light-source data, "Increased data rates drive optimization" and "Huge scope for new optimization models and methods" (slide 37).
- 2024 [stated, P (ASR)] "one of the exciting parts of working at a government lab is that I see scientists from many disciplines working in optimization" (S19 L01).
- Era and resources [inferred]: said from a national laboratory where facility scientists bring problems (X-ray light source, power grid, climate). In 2015 he asked Fletcher how a university researcher finds such partners: "So how do you go and find somebody to work with in industry?" (S02 p. 5).

**1.2 Simple examples and counterexamples are how a method is judged [B4].**
- 2015 [stated, P] After Fletcher's "One thing I would say is to look at numbers: they're trying to tell you something.", Leyffer adds: "So, I know when I was in Dundee, one of the things you always told us was to look at examples, so this is the same idea." Fletcher: "Part of it, yeah." (S02 p. 4)
- 2017 [stated, P] On his PhD work: "we generalized outer approximation by Duran and Grossmann [13], see [16], 'simplified' its convergence analysis, and provided a one-dimensional example where outer approximation visits all integer points." (S01 p. 5; [13] is Duran and Grossmann, Math. Program. 36(3) (1986) 307-339, DOI 10.1007/BF02592064; [16] is Fletcher and Leyffer, Math. Program. 66 (1994) 327-349, DOI 10.1007/BF01581153)
- 2024 [stated, P (ASR)] On a semidefinite relaxation of power flow: "any good idea somebody comes up with a counter example so there exists a small counter example uh where the rank of w is greater than one so it's not solved the relaxation is not exact" (S19 L14).
- See 3.4 (learning from the worst case) and 5.1.

**1.3 Software validates theory [B5].**
- 2015 [stated, P] "This goes back to saying write software and the role of software." Fletcher: "Yeah, be a good programmer. Now if you give an idea to a Ph.D. student and it doesn't work, you have no idea why he thinks it doesn't work." Leyffer: "True" (S02 p. 4).
- 2016 [stated, P] "The second foundation of Roger's research philosophy was software, as he believed that software validates theory and is simultaneously a guide to good methods." He praises a design property of Fletcher's QP code: "Roger provided both dense and sparse instantiations of this 'class' and opened the possibility for other classes - for example, for people wishing to exploit the structure of their problem." (S03 p. 2)
- [inferred] The second quote states, in 2016, the design aim of his own later frameworks (7.2): extensible code that lets others exploit problem structure.

**1.4 Simple arguments, simple proofs, structured exposition (several statements, partly about Fletcher).**
- 2015 [stated, P] "I think that's one of the nicest parts of your book, actually. I enjoyed reading it as an undergraduate in nondifferentiable optimization; it's very structured." (S02 p. 3)
- 2016 [stated, P] "Roger was what Americans would call a no-nonsense applied mathematician who believed in simple arguments and proofs." (S03 p. 2)
- 2017 [stated, P] On the first filter convergence proof, which he credits to Fletcher and Toint (the SLP proof of Dundee report NA/183, "On the global convergence of an SLP-filter algorithm", August 1998, by Fletcher, Leyffer and Toint, as listed in his references): "I still regard this as the most easily understood proof." (S01 p. 4)
- 2015 [observed, P: Fletcher's advice, which Leyffer solicited] Asked "What advice would you give to someone starting a Ph.D. or early in their career path?", Fletcher answers: "I would say write clear slides and clear papers" ... "don't write convergence proofs that are 30 pages long. Make it so that I can understand it. What works for me is to keep the notation as simple as possible." (S02 p. 5). Leyffer does not respond to this answer in print; it is Fletcher's view.

**1.5 A result is only as good as the guarantee behind it [B14].**
- 1993 [stated, P] On a barrier approach to MINLP by others: "Unfortunately, Amir and Hasegawa do not address the important issue of increasing ill conditioning of the barrier function and no convergence result is presented." and "It seems to me that solving an MINLP problem by a sequence of unconstrained MINLP problems is unlikely to be effective." (S06 pp. 11-12)
- 2024 [stated, P (ASR)] Comparing a discontinuous and a smooth model of the same design problem: "the original problem is discontinuous so I don't even know what it means if you're converging to a stationary point for these problems um so for the for the letter last problem we can we can have some confidence that we find a global solution" (S19 L11).
- 2026 [stated, P] The conDFO brief opens: "Design a sequential algorithm for constrained derivative-free optimization (DFO) and proof its convergence properties" (S35).
- Era: the 1993 statement is a PhD student's literature critique; the 2026 statement is a senior researcher's brief to an AI assistant.

**1.6 Deflate claims, including his own [B10].**
- 2006 to 2017, on his own signature method: "We believe filter methods achieve this goal." (S04 p. 2, coauthored) against "At this point, I do not believe that there exists a big difference between filter methods and modern penalty function methods, and the choice of method is really a question of personal preference." (S01 p. 5). Kept as contradiction C1.
- 2017 [stated, P] "There has been tremendous progress in solving MINLP problems over the past decade (and this short note does not do justice to the many clever developments in the field)." (S01 p. 7)
- 2018 [stated, P (ASR)] Opening: "I should say that most of this work in fact almost all of this work is not my own work so you have to forgive me if I'm sort of blundering along"; middle: "I'm not going to give you solutions I'm not going to give you the panacea of how optimization is going to serve safe" (ASR; probably "save") "machine learning"; close: "in terms of using optimization technology I think there's sort of interesting niche markets but ultimately it's not the panacea so this is a big problem that requires more technology than just optimizations" (S18).
- 2024 [stated, P (ASR)] On LP/NLP-based branch-and-bound: "maybe the method of choice for many problems it's not the method that will beat every method on on all problems but it's a pretty good method" (S19 L26).
- 2016 [stated, P] Praising the same trait in Fletcher: "However, Roger was just as suspicious of his own opinion, and not above changing his own mind." and "This self-doubt and suspicion enabled Roger to stay fresh and produce groundbreaking results, even late in his career." (S03 p. 2)

**1.7 Brute force will not do; smarter mathematics will (3 occasions, two coauthored).**
- 2013 [stated, P, coauthored] For PDE-constrained integer design: "Brute-Force Approach: assume billion PDECOs per second" and "exascale machine would run longer than age of universe!" (S13 slide 7)
- 2013 [stated, P] "BnB won't scale to a billion-way concurrency" and "Distributed tree-search alone is not enough" (S12, Socn-6 slide 86)
- 2016 [stated, P, coauthored with six others] "This brute force approach is going to hit a brick wall pretty soon. Smarter use of available computer resources is going to be the main way of increasing the effective performance of supercomputers in the future." (S31, Conclusions and Outlook)

**1.8 Crossing between the integer and the continuous world is elegant (1x).** 2024 [stated, P (ASR)] On outer convexification: "I really like this trick because it sort of goes from the integer side back to the continuous side and shows you that using this integrality you can actually sometimes simplify the nonlinear world" (S19 L31). [inferred] Fits B6.

**1.9 Unfashionable topics noted with interest (1x).** 2015 [stated, P] "And that's sort of interesting because it was a time when it wasn't fashionable to do semi-definite programming." (S02 p. 2)

**1.10 How he judges other people's work (taste by evaluation).**
- Of Ignacio Grossmann [stated, P (ASR)]: "he's sort of the grandfather of mix inte nonlinear programming" (S19 L06; "mix inte" is the ASR rendering of "mixed-integer").
- Of the Quesada-Grossmann algorithm (Comput. Chem. Eng. 16(10-11) (1992) 937-947, DOI 10.1016/0098-1354(92)80028-8) [stated, P]: "arguably the best approach to solving MINLPs" (S01 p. 5, 2017); compare 2024 in 1.6 (contradiction C3).
- Of the NEOS server [stated, P, coauthored]: "Arguably the most important factor in making optimization solvers widely available has been the NEOS server" (S07 pp. 96-97; reused in S09, appendix).
- Of Moritz Hardt's 2018 talk on "non-optimization" [stated, P (ASR)]: "a really great talk" and "a warning I think that is good for optimizers so not maybe for you but for people who optimizes in the room to heed when you're looking at applying optimization methods to machine learning" (S18). The captions render the name as "Moore it's hard" and later "Moritz"; the identification with Moritz Hardt, a plenary speaker at the March 2018 INFORMS Optimization Society conference where Leyffer also gave a plenary (S01 issue, p. 15), is [inferred].
- Of a bad published model [stated, P]: an IEEE 802.11 network model with "one horrible constraint", z = 1/(1+1000(x-y)^10), marked "highly nonlinear/nonconvex" and "model as MIP not NLP", followed by a slide with a "Chinese Proverb": "Give a man a fish and he will eat for a day." / "Teach a man about nonlinear functions and you will lead a troubled life." (S12, Socn-1 slides 65-67, 2013; the same constraint on S15 18-minlpIntro slides, 2016). The 2018 exercise sheet calls it "published in an obscure paper" and asks "(2.2) Can you deduce the modelers intention from the plot?" and "(2.3) Model this expression as MIP not NLP!" (S16).

---

## 2. Problem choice

**2.1 A base and its extensions [B3].**
- 2012 [stated, P] First person, on his research page: "I am interested in the development of reliable methods for solving large-scale nonlinear optimization problems and in the implementation and analysis of filter type algorithms. This forms the basis from which I am extending nonlinear optimization methodologies to emerging areas such as mixed-integer nonlinear optimization and optimization problems with complementarity constraints." (S21)
- 2017 [stated, P] "Starting with filter methods for global convergence of nonlinear solvers, we consider two extensions of nonlinear optimization, namely mixed-integer nonlinear programming (MINLP), and mathematical programs with equilibrium constraints. Each topic concludes with a brief outlook for future research challenges." (S01 p. 3)
- Titles: lecture notes subtitled "24 Lectures on Nonlinear Optimization and Beyond" (S09, 2016); prize article "Nonlinear Optimization and Beyond" (S01, 2017).
- 2013 [stated, P] "Research Opportunities beyond traditional MINLP": "Exploiting nonlinear structure", "MIP++: PDEs, uncertainty, DFO, ...", "Computer science challenges & opportunities" (S12, Socn-6 slide 88).
- Note 01 §2 cites a 2009 Georgia Tech seminar bio with the same base-and-extension sentence in the third person (not re-fetched in this run).

**2.2 Let the extension's needs choose the base research [B7].**
- 2005 [stated, P] "Current implementations of interior methods often outperform active set methods in terms of speed. On the other hand, active set methods are more robust and better suited for warm starts, which are important for solving integer optimization problems [8, 9]. Consequently, we have recently become interested in new active set approaches, which are reviewed in this note." (S10 p. 1)
- 2010 [stated, P] "In principle, NLP solvers also compute factors that could be reused. Unfortunately, these factors are always outdated after a solve." (S11 §2.2)
- 2012 [stated, P, coauthored; the editors summarising contributed chapters] SQP methods "are particularly well-suited to warm starts and re-solves that occur in MINLP", while "standard IPMs can stall if started near a solution, or even fail on infeasible NLPs, making them less suitable for MINLP." (S08 p. ix)
- 2013 [stated, P] "What NLP solver should I use in MINLP?" ... "... active-set methods are preferred for MINLPs." (S12, Socn-1 slide 36)
- Era [inferred]: 2005-2013 CPU-era solvers. By 2024 his Uno abstract treats SQP and interior-point methods as sharing "key algorithmic components" inside one framework (S32), a softer framing of the same contrast.

**2.3 Work where two cultures meet [B6].**
- 1998 [stated, P] "Classical methods for the solution of (P) 'decompose' the problem by separating the nonlinear part from the integer part. This approach is largely due to the existence of packaged software for solving Nonlinear Programming (NLP) and Mixed Integer Linear Programming (MILP) problems." and "In contrast to these approaches, the present paper considers an integrated approach to MINLP problems." (S05 p. 2)
- 2010 [stated, P] "We also describe some experiments with nonlinear branch-and-bound branching techniques that lead us to promote a tighter integration of nonlinear solvers into a general branch-and-cut framework." (S11, abstract)
- 2012 [stated, P, coauthored] "Yet, the two key components of MINLP -- mixed-integer linear programming (MILP) and nonlinear programming (NLP) -- have experienced tremendous progress over the past 15 years." The 2008 IMA workshop's goal was "synthesizing these advances and inspiring new ideas in order to transform MINLP." (S08 p. vii)
- 2013 [stated, P, coauthored] "A Simple Approach": {PICO, MINOTAUR} + {PETSc, Trilinos} "⇒ failure", then "Need integrated algorithmic strategy" and "... concerted effort worthy of DOE labs" (S13 slide 8). The slide states the failure as a forecast; whether the combination was tried is not said.
- 2015 [stated, P, coauthored deck he presented] "MIPDECO: Two Cultures Collide": "PDE-optimization & MIP developed separately", "different assumptions, methodologies, and computational kernels!"; "Obtain good solutions efficiently" (PDE optimization) against "Deliver certificate of optimality" (MIP); "Potential for Disaster, or Opportunity for Innovation!" (S14 slide 15)
- 2017 [stated, P] "Over the last 10 years or so, I have been fortunate to collaborate with some very smart discrete optimizers." (S01 p. 5)

**2.4 Name a new problem class, list its challenges, start a test library [B3].**
- 2013 [stated, P, coauthored] "Opportunity to tackle new, broader class of design applications", "Poses rich set of mathematical, algorithmic, and CS challenges", "Unlikely to tackle problems on smaller systems", "... requires concerted & coordinated effort" (S13 slide 12).
- 2015 [stated, P] Fletcher names as an open problem "that MINLP thing with PDE with differential equation constraints"; Leyffer: "Of course, that's only because I just gave a talk on them." (S02 p. 5)
- 2015 [stated, P, coauthored deck] Theory questions first: "What function space is w(x, y) ∈ {0, 1}?" (credited on the slide to Denis Ridzal) (S14 slide 13); "factorable programming approach hopeless" for nonconvex PDE constraints (slide 14); conclusions: "On-going work: Building library of test problems", "Need new ideas, solvers, software for real applications", "... our five-year mission ...", then "To boldly go where no optimizer has gone before ..." / "... to explore strange new PDEs & MIPs!" (slides 28-29).
- 2016 [stated, P] "These challenges indicate that MIPDECO is a nontrivial class of problems. However, we believe that these challenges are not insurmountable. On the other hand, MIPDECOs have a range of important applications. In Section 19.3 we present a set of test problems to motivate further research into MIPDECO." (S09 §19.2)
- 2017 [stated, P] "new classes of MINLPs are emerging, such as MIPs with second-order cone constraints [12, 11] and MINLPs with partial-differential equation constraints [31], which necessitate novel approaches." (S01 p. 7)
- Practice pointer: the papers that followed are in note 01 §3 (S5).

**2.5 "Write the call": shape the funding agenda (1x explicit, 2014).**
- 2014 [stated, P] "Before you apply for funding … write the call:" / "Volunteer for funding workshops & white papers" / "Participate in forward-looking and funding panels" / "Talk to your program managers" (S20 slide 2).
- Context [stated, P, coauthored]: he chaired the SIAM Climate Task Force, whose report was meant as "a report with guidelines for Congress and U.S. federal agencies" (S24 p. 12), and summarised a DOE workshop on AI for Earth-system prediction (S26). The 2013 MIPDECO deck was given at the DOE workshop "Applied Mathematics Research for Exascale Computing" (S13).
- Era and seniority [inferred]: advice from a DOE-laboratory researcher, where programmes are shaped through workshops and white papers. A junior researcher has little access to such panels.

**2.6 Machine learning: interest and caution (see contradiction C4).**
- 2018 [stated, P] Problem source: "Traditional Cell Identification at APS" was to "Ask student/postdoc to 'mark' potential cell locations by hand & test" (S17 slide 7). In the video [ASR]: "we are going to hire lots of postdocs but they're going to do smart things with machine learning instead of stupid things where they mark out little cells in pictures" (S18).
- 2018 [stated, P (ASR)] "until yesterday I had no clue about optimization for machine learning" and the "niche markets ... not the panacea" verdict (1.6) (S18).
- 2021 [stated, quoted in a secondary source] "SIAM provides a critical bridge between academia and industry, and this is an exciting time for the community as we delve into new areas such as machine learning where optimization may have a decisive impact." (S30)
- 2022 [stated, P, coauthored workshop summary] "AI/ML models--while likely incapable of replacing years of climate model research--can help integrate more small-scale phenomena into existing models." (S26 p. 3; reports the workshop's common theme)
- 2024 [stated, P (ASR)] On optimizing over a neural-network surrogate outside its training data: "I'm just predicting complete garbage and in this case I was predicting that my new machine would solve global warming" (S19 L49); "this is the picture that you should have in mind when you're doing when you want to do optimization over machine learning surrogates you have to be careful" (S19 L48).

**2.7 When to stop a line of work: no statement found.** The nearest is a priority rule in a 2026 student-project plan (AI-assisted): filter methods are "a promising but higher-risk alternative to revisit if the exact-penalty study matures early" (S36, docs/project.tex).

---

## 3. Idea generation

**3.1 Borrow a concept from a neighbouring field (2x).**
- 2006 [stated, P, coauthored] "filter methods view nonlinear optimization as a biobjective optimization problem that minimizes the objective and the constraint violation." (S04, abstract)
- 2017 [stated, P] "Instead of combining the objective and constraint violation into a single function, we borrow the concept of domination from multiobjective optimization" (S01 p. 4).
- Origin, in his account [stated, P]: "Roger Fletcher had been unhappy with the performance of classical penalty functions for NLP, and had been playing around with methods that instead use the Lagrangian as a merit function within a tolerance tube around the constraints [43], similar to the funnel ideas [24] developed later by Nick Gould and Philippe Toint. Our filter method [17] grew out of these early experiments." (S01 pp. 3-4; [17] is Fletcher and Leyffer, Math. Program. 91(2) (2002) 239-269, DOI 10.1007/s101070100244). The idea grew from the advisor's experiments; his own share is not stated.

**3.2 Start from what the numbers show (2x).**
- 2006 [stated, P, coauthored] "Yet we have noticed that the unmodified SQP method is able to quickly solve a large proportion of test problems without the need for modifications to induce global convergence." and "The success of the unmodified SQP method motivates us to find a way of inducing global convergence, which would allow the full Newton step to be taken much more often." (S04 p. 2)
- 2017 [stated, P] On complementarity constraints, after reporting others' "disappointing" experience: "In contrast, our initial numerical experience with filterSQP was very positive [19], and we investigated the convergence of SQP methods applied to (3.9) together with Roger Fletcher, Danny Ralph, and Stefan Scholtes [20]." (S01 p. 7; [19] Fletcher and Leyffer, Optim. Methods Softw. 19(1) (2004) 15-40, DOI 10.1080/10556780410001654241; [20] Fletcher, Leyffer, Ralph, Scholtes, SIAM J. Optim. 17(1) (2006) 259-286, DOI 10.1137/S1052623402407382). The order is numbers first, convergence theory second.

**3.3 Remove restrictions that come from tooling, not from the mathematics (1998; tied to B5, B6).**
- [stated, P] "In [1] two QP problems are solved before branching. This restriction is due to the fact that a packaged SQP solver is used. By using our own solver we are able to remove this unnecessary restriction, widening the scope for early branching." (S05 p. 2; [1] is Borchers and Mitchell, Comput. Oper. Res. 21(4) (1994) 359-367, DOI 10.1016/0305-0548(94)90024-8)
- [stated, P] Reinterpreting an object already in hand: "In Section 3 it is shown that there is no need to compute a lower bound if the linearizations in the SQP solver are interpreted as cutting planes." (S05 p. 2)

**3.4 Learn from the worst case, then redesign [B4].**
- 2006 [stated, P, coauthored] "We applied filter methods to the original example by Maratos and observed second-order convergence. However, the following example shattered the hope that filter methods can avoid the Maratos effect in general" (S04 p. 6).
- 2017 [stated, P] The redesign: "We can avoid the Maratos effect by using second-order correction steps, and this approach was analyzed in [41]. However, a more appealing approach is to use a nonmonotone filter" (S01 p. 5; the nonmonotone filter paper is Shen, Leyffer, Fletcher, Comput. Optim. Appl. 52(3) (2012) 583-607, DOI 10.1007/s10589-011-9430-2).
- 2017 [stated, P] Credit for the sharper worst case: "Pierre developed a much nicer example that showed that outer approximation can take an exponential number of iterations [26]." (S01 p. 5; [26] Hijazi, Bonami, Ouorou, INFORMS J. Comput. 26(1) (2014) 31-44, DOI 10.1287/ijoc.1120.0545)
- 2024 [stated, P (ASR)] Teaching the same move: "this lecture was really about looking at one the worst case example for auto approximation that was this ball inside the hypercube and then from that learning from that that there's a way of rewriting the constraints disaggregating the constraints sort of separating the constraints out" (S19 L29; "auto approximation" is the ASR rendering of "outer approximation").

**3.5 A side question inside your own method becomes the next topic (1x, 1993).**
- [stated, P] "The introduction of MIQP master programs in Chapter 5 caused me to become interested in MIQP problems and a detailed study of branch-and-bound for MIQP problems is given." (S06 p. 15) Practice pointer: note 04 §1.2 traces this to the 1998 SIAM J. Optim. paper.

**3.6 Unify by building blocks [B9].**
- 2017 [stated, P] "Most solution methods for MINLP apply some form of tree-search, and we can distinguish two broad classes of methods: single-tree and multitree methods." and "All these MINLP algorithms share a range of common building blocks, namely relaxation and constraint enforcement." (S01 p. 6)
- 2013 [stated, P] The first Louvain lecture is organised around "Basic Building Blocks of MINLP Methods" (S12, Socn-1 outline).
- 2016 [stated, P] "Basic building blocks of solvers": "Relaxation ... create easier to solve problem", "Constraint enforcement ... exclude relaxation solution", "Upper bounds ... prune search space" (S15, 18-minlpIntro slide 38).
- 2024 [stated, P, coauthored] "SQP and interior-point methods (also referred to as Lagrange-Newton methods) typically share key algorithmic components" ... "Building on this insight, we introduce a unifying framework with eight building blocks that abstracts the workflows of Lagrange-Newton methods." (S32, abstract)
- 2024 [stated, P, coauthored] "a generic double-loop framework consisting of four algorithmic ingredients that unifies a broad range of nonlinear optimization solvers" (S33, abstract)

**3.7 Transfer and combine existing proofs; state the novelty as a gap in a known area [B8].**
- 2026 [stated, P] "Transfer as much of the proofs from the DFO paper and the filter paper." The two papers named in the brief: Larson, Menickelly, Wild, "Derivative-free optimization methods", Acta Numerica 28 (2019) 287-404, DOI 10.1017/S0962492919000060; Fletcher, Leyffer, Toint, "On the global convergence of a filter--SQP algorithm", SIAM J. Optim. 13(1) (2002) 44-59, DOI 10.1137/S105262340038081X (S35).
- 2026 [stated, P] "**Novelty:** Derivative-free or simulation-based optimization is a well-studied area. However, most solvers assume that the constraints $c(x)$ are either absent or simple (e.g. bounds, or affine). This project tackles **constrained** derivative-free optimization with a filter for global convergence." (S35)
- 2024 [stated, P, coauthored] "We prove global convergence of the trust-region funnel SQP method, building on known results from filter methods." (S33, abstract) Uno lets users compose solvers for new problem classes "while building on reliable nonlinear optimization techniques" (S32, abstract).
- 1993 [stated, P] The thesis takes the component solvers as given: "It is assumed throughout this thesis that good NLP, QP and LP algorithms exist." (S06 p. 14)
- 2024 [stated, P (ASR)] "when you're building your own solver what you want to do is you want to ideally build on other tech people who have done these things before" (S19 L29; "other tech people" is as captioned)
- 2026 [stated, P (AI-assisted)] "Combining the exact penalty with non-smooth QHD is, to our knowledge, a novel pairing" (S36, docs/project.tex).

**3.8 Reformulate the model until the solver can use it [B1, B12].**
- 2016 [stated, P] Thermal-insulation case study: "Snag: Solver looses model insight ... black-box optimization"; "Can we still use AMPL to solve this model?"; "Requires some modeling tricks"; "Resulting model is a smooth mixed-integer nonlinear program"; "Efficient ... optimum 10% better than derivative-free solvers" (S15, 02a-model slide 24). The underlying paper: Abhishek, Leyffer, Linderoth, "Modeling without categorical variables: a mixed-integer nonlinear program for the optimization of thermal insulation systems", Optim. Eng. 11(2) (2010) 185-212, DOI 10.1007/s11081-010-9109-z.
- 2024 [stated, P (ASR)] On the same case study: "if you play around with your models even though they look really hard initially in in real life um there's often tricks that you can do to make them more amable for solving them with our traditional solvers" (S19 L11).

---

## 4. Experiments and execution

**4.1 Modelling first [B1].**
- 2012/13 [stated, P, coauthored] "Modeling plays a fundamental role in MILP (see the textbook by Williams (1999)) and is arguably more critical in MINLP, because of the additional nonlinear relationships." (S07 p. 11) "A common theme of these reformulation is that convex formulations are typically preferred over nonconvex ones, and linear formulations over nonlinear formulations." (S07 p. 12) Both sentences reappear in the 2016 lecture notes (S09).
- Feb 2013 [stated, P] "The Three Most Important Things in MINLP": "Use LP solvers as much as possible in MINLP" and "linearize, linearize, linearize" (S12, Socn-1 slide 36); "We prefer linear over convex over nonconvex formulations." (slide 39); key points: "Modeling is very, very, very important" and "Linearize, linearize, linearize as much as possible" (slide 73).
- Sep 2016 [stated, P] "Modeling is very, very, very important", "Linearize, linearize, linearize as much as possible", "Prefer linear over convex and convex over nonconvex", "... order or magnitude difference in solver capabilities" (S15, 18-minlpIntro slide 38).
- Sep 2018 [stated, P, coauthored deck with Linderoth] "We prefer linear over convex over nonconvex formulations." (S16, MINLP-1 slide 12)
- Jan 2024 [stated, P (ASR)] "we always prefer linear over convex over non-convex formulations and The Great Divide between being able to solve problems at scale efficiently and not is this difference between convex and non-convex" (S19 L07); MINLP offers "opportunity for doing cool stuff but also for making mistakes and so we we place some emphasis on the modeling" (L01); "we prefer linear aine constraints" (L06; "aine" is the ASR rendering of "affine").
- Era: the same rule across 2012-2024 and across solver generations; [inferred] it rests on the gap between MILP and NLP solver maturity that the 2012 preface describes (2.3).

**4.2 Avoid formulations the solver cannot evaluate or converge on [B11].**
- 2012/13 [stated, P, coauthored] "In many practical instances, the MINLP solvers fail, because the nonlinear solver generates an iterate at which the nonlinear functions cannot be evaluated." (S07 p. 12)
- 2017 [stated, P] "However, as long as we take care with the problem formulation and the algorithm design, modern NLP solvers can tackle these problems." (S01 p. 7) and, under the heading "The Importance of Being Slack": "The use of slacks in (3.9) is critical for the convergence of SQP methods." (S01 pp. 8-9)
- 2016 [stated, P, coauthored deck] "... formulation matters: interplay of binary and continuous" (S15, 24-MIPDECO slide 35)

**4.3 Diagnose by reading the solver's numbers [B11].**
- 2015 [stated, P] He equates Fletcher's "look at numbers: they're trying to tell you something" with Fletcher's teaching "to look at examples" (S02 p. 4; 1.2).
- 2024 [stated, P (ASR)] On a perspective reformulation that solvers handle badly: "it was long suspected that this was because they're non-convex um but that's actually not correct um the nonlinear optimization for solvers failed because you can show that this formulation here violates a constraint qualification and so the solvers will converge slowly there"; and how to see it: "when you look at the output of the solver um it it kind of makes good progress initially but then you observe this slow linear rate of convergence" (S19 L30).
- 2024 [stated, P (ASR)] On optimization over neural-network surrogates: "you will typically see these issues when you plot the Dual INF feasibility so when you look at kkt error and that's not going down to zero" (S19 L48).

**4.4 Own the code; implement the idea inside the solver [B5].** 1998 [stated, P] "By using our own solver we are able to remove this unnecessary restriction" (S05 p. 2; 3.3). Practice pointer: note 01 §3 (S2) quotes the callback design on p. 10 of the same report.

**4.5 Test problems: publish libraries, start from existing models, prefer realistic problems (see contradiction C5).**
- 2009 [stated, P] MacMINLP is "a collection of Mixed Integer Nonlinear Programming (MINLP) test problems in AMPL", with columns for convexity, "(Y/N) depending on whether the problem is convex or not; (Y*=pseudo-convex)", and "optimal objective value or best solution found" (S23).
- 2010 [stated, P] New network applications: "These models form part of a library, DIWAL" (S11 §4).
- 2015-2016 [stated, P, coauthored decks] "On-going work: Building library of test problems" (S14 slide 28); "On-going work: Building AMPL library of test problems" (S15, 24-MIPDECO slide 35).
- 2024 [stated, P (ASR)] "when you write your own model it's always good to start with something else so here's just a list of some models that you can uh download or model test problem libraries" (S19 L09).

**4.6 Learn by doing: prove the key lemma, code the method, compare solvers (teaching statements, 3 occasions).**
- 2013 [stated, P] "Two little exercises" closing the first lecture, including deriving an equivalent linear model of "the worst-ever nonlinear function" (S12, Socn-1 slide 73).
- 2018 [stated, P] "Show that no integer assignment can be generated twice by outer approximation." ... "This essentially proves convergence of outer approximation (correctness follows from convexity)."; "(4.2) Experiment with different solvers. What do you observe?"; "(4.3) Code outer approximation in AMPL for the quadratic facility location problem." (S16, exercise sheet)
- 2024 [stated, P (ASR)] "you're not going to learn a programming language by listening to a lecture um I don't know if you know this but um that doesn't work you have to have hands-on experience" (S19 L09).
- Note 04 (K3) reads the 2018 sheet the same way.

**4.7 How he scopes a project (2026).**
- [stated, P] The conDFO brief is laid out as "Purpose", "Background" (two key references), "Problem Statement", "Novelty", "Suggested Approach" ("We will use a model-based approach that solves a *sequence of easier subproblems* where $f(x), c(x)$ are replaced by *model functions* with known approximation properties."), "Algorithmic Choices" (four, numbered), "Outline of Convergence Proof" (six steps, among them "The filter provides a proof that limit points are feasible." and "Clearly identify gaps that may require new ideas, and discuss."), and "General Book-Keeping" (S35).
- [stated, P (AI-assisted); quotes with LaTeX markup removed] A six-week undergraduate project ("Sven Leyffer and David Linnet"): "A realistic scope for a strong undergraduate, working entirely on top of the existing QHDOPT/QuTiP classical simulator (no quantum hardware)". Weeks 1-2: "Reproduce the QuTiP demo; read" two papers; "derive on paper the separability boundary" ... "for a chosen family of small constraints. Deliverable: a short note with worked examples." A baseline: "Quadratic penalty (baseline to beat)." The framing: "The governing question for this project. Every design choice below is really the question: does it keep the reformulated objective inside the univariate+bivariate class (1)? This is what turns a routine 'add a feature' task into an optimization-meets-quantum research question." The fallback: "Minimal viable deliverable." ... "This is a complete, honest result even if the exact penalty turns out to lose --- a negative result here is still informative." (S36, docs/project.tex)

**4.8 Keep a written trail of every session [B15].**
- 2026 [stated, P] "Create a `LOGBOOK.md` file (details below)." / "After creating a plan, write a summary of the plan to plans/YEAR-MM-DD-shortTitle.md" / "Before ending each session do the following:" "Update the `LOGBOOK.md` with a short description of the session (pointing to any plans)" and "Create or overwite a `STATUS.md` file that captures the current status of the project." / "When starting each session, read the following files `CLAUDE.md`, `LOGBOOK.md`, `STAUS.md`" (S35)
- 2026 [stated, P (AI-assisted)] The same protocol, generalised, in two more repositories: "**Always at session start:** read `LOGBOOK.md` (historical decisions) and `STATUS.md` (current project state)." / "**Always after a plan has been approved:** create a new `plans/PLAN-YYYY-MM-DD-ShortTitle.md` file and add an entry to `LOGBOOK.md` with a link to the plan." / "**Always at session end:** update `LOGBOOK.md` with a short summary of the session and replace `STATUS.md` with the new current (detailed) status." (S37 and S36, `.claude/CLAUDE.md`)
- Era [inferred]: written for AI coding assistants that keep no memory between sessions. Whether he asks human juniors for the same record is unknown (note 04 §4.6).

**4.9 Expose structure to the solver; avoid black boxes [B12].**
- 2016 [stated, P] The thermal-insulation slides (3.8): "Snag: Solver looses model insight ... black-box optimization" (S15, 02a-model slide 24).
- 2017 [stated, P] "In particular, Minotaur can evaluate, examine, and possibly modify the nonlinear problem description, which is significantly more complex than LP or QP problem specifications." (S01 p. 6)
- 2024 [stated, P (ASR)] "you can convey the logic inherent in categorical variables to the solver in this way" (S19 L11); and, for global solvers: "I'm not allowing you to take functions that I can't see inside so those are called blackbox functions where you're not telling me what the functional forms are" (S19 L35).

---

## 5. Judging results

**5.1 One good example is not evidence [B4].** 2006 [stated, P, coauthored] The filter method converged fast on Maratos's original example, then a new example "shattered the hope" (S04 p. 6; 3.4). 2017 [stated, P] "Originally, we had believed that filter methods avoid the Maratos effect [34]" ... "However, Nick and Philippe developed an example that showed that filter methods also suffer from the Maratos effect" (S01 p. 5).

**5.2 Report what fails and what remains open [B10].**
- 1998 [stated, P] "For the nonconvex problem FEEDLOC, Algorithm 2 did not find an integer feasible point." and "However, better heuristics for nonconvex MINLP problems remain an open problem." (S05 p. 11)
- 2024-26 [stated, P, coauthored] "We provide a computational example, for which we certify all of our imposed assumptions. The results point to both the potential of the methodology and the gaps in the research that need to be closed." (S34, abstract)
- 2026 [stated, P] "Clearly identify gaps that may require new ideas, and discuss." (S35); [stated, P (AI-assisted)] "a negative result here is still informative" (S36).
- 2024 [stated, P (ASR)] On a heuristic: "for quadratics I think it works very well um and maybe there's a similar thing that works then for quadratic constraints um I don't know I I haven't enough experience with these things" (S19 L45).

**5.3 Credit, in public, those who corrected your proofs (1 occasion, two statements).** 2017 [stated, P] "This proof was later generalized to sequential quadratic programming (SQP) methods in [21, 15] together with Nick Gould and Andreas Wächter, who corrected many errors in the early proof." (S01 p. 4; [15] Fletcher, Gould, Leyffer, Toint, Wächter, SIAM J. Optim. 13(3) (2002) 635-659, DOI 10.1137/S1052623499357258) and "Later, Bonami et al. corrected our convergence proof [4]" (S01 p. 5; [4] Bonami et al., Discrete Optim. 5(2) (2008) 186-204, DOI 10.1016/j.disopt.2006.10.011). Practice pointer: the published 2026 Correction to Leyffer and Manns, DOI 10.1007/s10107-026-02330-8 (note 01, F10).

**5.4 A community verdict can be an artefact of formulation and solver (1x).** 2017 [stated, P] "In addition, early numerical experience with this approach has been disappointing [3] with failure on 50-70% of some bilevel problems. As a consequence, solving MPECs via NLPs such as (3.9) has been commonly regarded as numerically unsafe." followed by his own positive experience (3.2) and his verdict: "In my opinion, reliable NLP solvers are still the best approach for solving MPECs despite the potential problems with slow convergence or convergence to spurious stationary points." (S01 pp. 7, 9)

**5.5 When methods are close, say so.** 2017 "the choice of method is really a question of personal preference" (S01 p. 5); 2024 "it's not the method that will beat every method on on all problems but it's a pretty good method" (S19 L26, ASR). See C1, C3.

**5.6 Ask what a guarantee means for this model [B14].** 2024: for the discontinuous model "I don't even know what it means if you're converging to a stationary point" (S19 L11, ASR; 1.5).

---

## 6. Writing and talks

**6.1 Proposals (one talk, 2014; the whole deck is advice).**
- [stated, P] Slide 2, "Ingredients of Good Proposals": "Good Story: strong introduction & motivation", "Why is your problem important & challenging?", "Why are YOU the person to solve it?", "Compelling scientific case and research plan", "Preliminary results are helpful" (S20).
- Slide 3, "Nuts and Bolts of a Proposal": "Read the call & address evaluation criteria", "Note differences between DOE and NSF calls" (e.g. "Relevance to DOE" against "Broader Impact"), "Stick to proposal template & rules: fonts, margins", "Use deadlines/checklist for your writing process", "Proof-read your proposal multiple times!", "Never write a math proposal in Word", "Avoid tiny print and highlights in yellow" (S20).
- Slide 4, "Social Aspect of Proposals": "Ask your mentor or colleagues to read your proposal & provide feed-back", "Learn by writing proposals with colleagues", "Negotiate funding scenarios (cuts) ahead of time", "Learn from the reviews … helpful!", "Try-and-try again … you will succeed!" (S20)
- Era: SIAM Annual Meeting, Chicago, 10 July 2014 (talks page, S22; the file's metadata dates it 3-11 July 2014); US DOE and NSF funding.

**6.2 The burden of clarity is on the explainer (1x, plus Fletcher).** 2024 [stated, P (ASR)] "there are no stupid questions um there's only people who can't explain what they're doing"; "I'm not a teacher" ... "so I learn from your questions" (S19 L01). Compare Fletcher's "Make it so that I can understand it" (1.4), which Leyffer solicited but did not comment on.

**6.3 State the take-home points; keep it light [practice, P, from his own decks].** Closing slides titled "Summary and Teaching Points" (S15, 18-minlpIntro slide 38), "Summary and Key Points" (S12, Socn-6 slide 88), "Take-Home Message" (S15, 02-apps slides 26, 37), "Summary and Take-Away Points" (S15, 01-intro slide 35); humour on closing slides, such as "DON'T PANIC!" (02-apps slide 47) and "Final Exam for Course Credit: Have a beer with Sven today!" (Socn-6 slide 88). Recorded here because the words are his; the habit belongs to agent 03.

**6.4 In a survey, state the scope cut openly (1x, coauthored).** "Given the wide applicability of MINLP and the ensuing explosion of numerical methods, it would be prohibitive to discuss all methods. Instead, we focus this survey on deterministic methods that tackle both integer variables and nonlinear constraints." (S07 p. 9)

**6.5 Keep the older work visible [B13].**
- 2015 [stated, P] "We need to be make sure we get all the references into the optimal pa- pers, so that people start picking these things up." (S02 p. 3; as printed, "optimal" is probably "Optima"). [observed, P] The editors: the interview comes "along with a great list of links to material related to Fletcher's work carefully compiled by our interviewer" (S02 p. 1).
- 2006 [stated, P, coauthored] The history aims to "provide references for those wishing to delve deeper into filter methods." (S04 p. 2)

**6.6 Paper skeleton (1x, 2026, AI-assisted).** In the plan for the quantum project: "Section skeleton: standard research paper (user choice)." with Introduction, Background, Methods, Results, Discussion and Conclusion (S36, plan of 2026-09-03; "user" is Leyffer).

---

## 7. Research organisation

**7.1 Collaboration and credit [B13].**
- 2017 [stated, P] "Throughout my career, I had the great fortune to work with some of the brightest optimizers, and this article is a tribute to their influence, guidance, and inspiration." (S01 p. 3) and "With a student of Jeff Linderoth's, we built FilMINT [1]" (S01 p. 5; [1] Abhishek, Leyffer, Linderoth, INFORMS J. Comput. 22(4) (2010) 555-567, DOI 10.1287/ijoc.1090.0373).
- 2013 [stated, P] "Thanks to my Collaborators ..." naming Belotti, Mahajan, Kirches, Linderoth and Luedtke (S12, Socn-6 slide 89).
- 2014 [stated, P] "Learn by writing proposals with colleagues"; "Tips for large collaborative proposals:" "Negotiate funding scenarios (cuts) ahead of time" (S20 slide 4).
- 2016 [stated, P] The lecture notes are dedicated, among others, to "my teacher and mentor Roger" (S09).

**7.2 Shared software frameworks as community infrastructure [B5].**
- 2017 [stated, P] "Algorithmic advances over the last decade or so have often taken advantage of the special structure of problems, which motivated us to develop the Minotaur software framework [33]." Its goals: "(1) implement a range of algorithms in a common framework; (2) provide fast and usable MINLP solver; (3) provide flexibility for developing new efficient algorithms; and (4) reduce the burden of developing new algorithms by providing a common software infrastructure. Our vision is to enable researchers to implement new algorithms that take advantage of problem structure, by providing a general framework that is agnostic of problem type or solvers." (S01 p. 6; the journal paper is Mahajan, Leyffer, Linderoth, Luedtke, Munson, Math. Program. Comput. 13(2) 301-338, DOI 10.1007/s12532-020-00196-1)
- 2024 [stated, P, coauthored] Uno "is meant to (1) organize mathematical optimization strategies into a coherent hierarchy; (2) offer a wide range of efficient and robust methods that can be compared for a given instance; (3) enable researchers to experiment with novel optimization strategies; and (4) reduce the cost of development and maintenance of multiple optimization solvers." (S32, abstract) [inferred] The four aims run parallel to Minotaur's four, seven years apart.
- 2024 [stated, P (ASR)] "if you come up with a really smart algorithm for solving MLS then we would like you very much to implement this in minor so that we benefit from it too and so does the rest Community oh and I should say it's open source" (S19 L27; "MLS" and "minor" are the ASR renderings of MINLPs and Minotaur).
- 2017 [stated, P] "To develop better solvers we need to build on our existing NLP solver infrastructure." (S01 p. 9)
- Resources [inferred, with note 01 §1.8 as practice basis]: frameworks of this size were written mainly by postdocs and collaborators (Mahajan for Minotaur, Vanaret for Uno); they need a laboratory-scale team.

**7.3 Funding and agenda-setting.** See 2.5 ("write the call") and 6.1.

**7.4 Students and recruitment.**
- 2023 [stated, P] As SIAM President, on a day when Argonne hosted local student chapters: "The benefits of such events are twofold; students learn about potential career paths and staff meet prospective interns or postdoctoral researchers. I strongly encourage other SIAM student chapters, laboratories, and research institutions to arrange similar experiences." (S28 p. 3)
- 2023 [stated, P] "During my presidency, I therefore plan to concentrate on attracting more students to the SIAM community." (S27 p. 5)
- 2024 [stated, P (ASR)] On the thermal-insulation case study: "that was done with a student of mine who's now a VP for research at United Airlines" (S19 L11). That the student is the paper's first author, Kumar Abhishek, is [inferred] from the authorship (3.8); see C6.

**7.5 Interdisciplinary teams (policy statements, coauthored).**
- 2021 [stated, P, coauthored; he chaired the task force] "This research is inherently multidisciplinary and calls for interdisciplinary collaborations between the fields of mathematics, computational science, atmospheric and oceanic sciences, geosciences, social sciences, biology, and agricultural sciences." and "instructors need to prepare applied mathematics and computational science students to work effectively on diverse, multidisciplinary, and convergent teams that include social scientists." (S24 p. 12)
- 2022 [stated, P] "I am excited about new initiatives that strengthen the presence of industry in SIAM, cementing our unique role as a bridge between industry and academia." (S25 p. 2)

**7.6 Value of meeting in person (1x, coauthored, a society decision).** 2023: in-person participants "felt that the large number of virtual talks diminished the energy of the physical conference, significantly reduced the chance for impromptu discussion, and limited networking opportunities for students and postdoctoral researchers." SIAM therefore "decided to return to fully in-person conferences in 2023" (S29 p. 3). The sentence reports member feedback; that he shares the view is [inferred] from his co-signing it.

**7.7 Working with AI (2026).** Besides the session protocol (4.8): a site he started as "A curated collection of best practices, notes, and links for working with AI" (S37, README), linking a "Claude Code 101 Hackathon" ("Claude Code as a co-scientist: workshop") and, as dated news items, the "Leiden Declaration on Artificial Intelligence and Mathematics" (06/02/26) and an OpenAI post on "Ten advances in mathematics and theoretical computer science" (08/01/26) (S37, docs/resources/links.md). Its content pages are still short stubs (note 04 §4.6).

---

## 8. Failures, abandoned hopes and corrections that he talks about

| # | When | What | His words (source) | Tag |
|---|---|---|---|---|
| F1 | 1996-2006 | Hope that filters avoid the Maratos effect, given up | "Early on, we conjectured that filter methods may be able to avoided the Maratos effect." and "shattered the hope" (S04 p. 6); "Originally, we had believed that filter methods avoid the Maratos effect" (S01 p. 5) | [stated, P] |
| F2 | 1996-2002 | Parts of the first filter method dropped | "The initial filter method contained features, such as the NW/SE corner rule and unblocking, that were shown to be redundant in the subsequent convergence analysis." (S04 p. 5) | [stated, P, coauthored] |
| F3 | 1998-2002 | Errors in the early filter proof, corrected by coauthors | "who corrected many errors in the early proof" (S01 p. 4) | [stated, P] |
| F4 | 1994-2008 | The 1994 outer-approximation convergence proof corrected by others | "Later, Bonami et al. corrected our convergence proof [4]" (S01 p. 5) | [stated, P] |
| F5 | 1998 | His SQP-based branch-and-bound fails on a nonconvex test problem | "For the nonconvex problem FEEDLOC, Algorithm 2 did not find an integer feasible point." (S05 p. 11) | [stated, P] |
| F6 | 2006 (told 2017) | SQP on a nonlinear complementarity formulation, and a colleague's SQPEC idea, shown to fail | "In [20] we give an example that shows that an SQP method applied to a nonlinear complementarity constraint can converge to a nonstationary point." and "Remarkably, this approach can be shown to fail for MPECs as demonstrated by the following example" (S01 p. 9) | [stated, P] |
| F7 | 2013 | First parallel branch-and-bound design dropped | Slide: "Parallel BnB (scales to 1k cores)"; first strategy, one worker per NLP, "grain-size too small", "... NLPs solve in seconds"; "Better Strategy:" one worker per subtree, "... 'streamers' running down tree" (S12, Socn-6 slide 84; mapping paraphrased from the slide's symbols). Which project the slide reports is not stated | [stated, P] |
| F8 | 2013 | Forecast failure of bolting a MIP framework onto a PDE framework | {PICO, MINOTAUR} + {PETSc, Trilinos} "⇒ failure" (S13 slide 8) | [stated, P, coauthored] |
| F9 | 2024 | His first MINLP code, in his words now obsolete | "a very rickety and Old Branch and bound solver it was one of the first mix nonlinear programming solvers that was out there uh it doesn't work very well anymore but it's one of one that I wrote when I was a PhD student" (S19 L09, ASR; the solver name is garbled as "minel PBP", probably MINLP-BB) | [stated, P (ASR)] |
| F10 | 2025-2026 | Two mistakes in a 2025 paper, corrected in print | Not read by me; the Correction (DOI 10.1007/s10107-026-02330-8) is analysed in note 01, F10 | [practice] pointer |

No rejected paper or retracted claim is mentioned in anything he wrote or said that I read.

---

## 9. Era and resource context of the stated methodology

| Period | Role (per notes 01 and 04) | Setting | What he stated in that period |
|---|---|---|---|
| 1990-1994 | PhD student, Dundee, with Fletcher | Fortran 77, the advisor's QP code, workstations | Critique of methods without convergence results; "It is assumed throughout this thesis that good NLP, QP and LP algorithms exist." (S06 p. 14) |
| 1994-2002 | Research fellow, Dundee | his own solver (filterSQP), small test sets | Own the solver; integrate rather than decompose (S05) |
| 2002-2012 | Argonne staff, DOE ASCR funding | AMPL, NEOS, university collaborators | Active-set methods for MINLP (S10, S11); test libraries (S23); survey positions on modelling (S07, S08) |
| 2013-2019 | Senior staff; exascale programmes; summer schools | DOE workshops; courses at Louvain (2013), in India (2016), Bremen (2018) | Modelling-first teaching (S12, S15, S16); the MIPDECO programme (S13, S14); proposal advice (S20); ML caution (S17, S18) |
| 2020-2024 | SIAM president-elect and President; Argonne Distinguished Fellow | open-source frameworks, arXiv-first, lecture videos | Infrastructure goals (S32); students and community (S27, S28); calibrated claims (S19) |
| 2025-2026 | Deputy division director | AI coding assistants, GitHub | Project briefs, proof transfer, session protocol (S35-S37) |

Portability [inferred]: the modelling rules (B1, B11, B12), the counterexample habit (B4) and the convergence standard (B14) need no special resources. "Write the call" (2.5), shared frameworks (7.2) and lab-scale programmes (2.4) depend on seniority and a national-laboratory setting.

---

## Contradictions (kept, not reconciled)

- **C1. Filters against penalty functions.** 2006: "We believe filter methods achieve this goal." (S04 p. 2) and "We believe that filter methods will continue to grow and find application in more diverse areas." (S04 p. 13). 2017: "I do not believe that there exists a big difference between filter methods and modern penalty function methods, and the choice of method is really a question of personal preference." (S01 p. 5). His later briefs and papers still choose filters (S33 in 2024; S35 in 2026: "with a filter for global convergence").
- **C2. How to get fast local convergence.** 2006: "We currently prefer to use SOC steps to obtain fast local convergence" (S04 p. 7). 2017: "a more appealing approach is to use a nonmonotone filter" (S01 p. 5).
- **C3. The best method for convex MINLP.** 2017: the Quesada-Grossmann algorithm is "arguably the best approach to solving MINLPs" (S01 p. 5). 2024: "maybe the method of choice for many problems it's not the method that will beat every method on on all problems but it's a pretty good method" (S19 L26, ASR).
- **C4. What optimization can do for machine learning.** 2018: "interesting niche markets but ultimately it's not the panacea" (S18, ASR). 2021: "new areas such as machine learning where optimization may have a decisive impact" (S30, quoted by Argonne). The 2024 warnings about learned surrogates (S19 L48, L49) sit in between.
- **C5. Test problems.** 2015: he agrees ("Right. Absolutely.") that "test problems are often very badly selected" and hears Fletcher prefer "half a dozen real industrial problems" (S02 p. 5). Across 2009-2024 he builds, publishes and recommends test libraries (S23, S11, S14, S15, S19 L09), and his 2024 Uno abstract benchmarks on "a subset of 429 small problems from the CUTE collection" (S32), the kind of collection Fletcher criticised.
- **C6. Whose student.** 2017: "a student of Jeff Linderoth's" (S01 p. 5). 2024, on work with the same coauthor team (identification inferred): "a student of mine" (S19 L11, ASR). Both can be true in different senses; note 04 records the thesis naming Linderoth as advisor and Leyffer on the committee.
- **C7. Generality against restraint.** MINLP is "one of the most flexible modeling paradigms available" (S11, 2010; S08 p. vii, 2012, which adds "but because its scope is so broad, in the most general cases it is hopelessly intractable") and "one of the most general modeling paradigms in optimization" (S01 p. 5, 2017); yet "Teach a man about nonlinear functions and you will lead a troubled life." and "Linearize, linearize, linearize" (S12, 2013; S15, 2016). A tension in emphasis, not a logical contradiction.
- **C8. Dates on decks.** The ISMP 2015 deck is dated "July 10, 2015" (S14), his talks page says "July 16, 2015" (S22). The talks page lists "Optimization for Machine Learning (updated), Purdue University Workshop on Approximation Theory and Machine Learning, September 2018" (S22), but the title page of the PDF it links names the "LANS Informal Seminar" and is dated "November, 28 2018" (S17).
- **C9. Teacher or not.** 2024: "I'm not a teacher" (S19 L01, ASR), against a record of courses in 2013, 2016, 2018 and 2024 listed on his Lectures page (S22). Probably means he holds no teaching post; kept as said.

## Gaps (not found or not read)

- **No essay, preface, blog post or interview in which Leyffer explains how he does research.** The richest first-person sources are the 2017 prize article (S01) and the 2015 interview he conducted (S02), where he mostly asks questions. Three web searches found nothing more; Argonne's own pages return HTTP 403 to curl and WebFetch.
- **His talk at the meeting where the 2015 interview took place** (Fletcher refers to it twice): the meeting is not named in the interview, and the talk's content is not recorded.
- **His plenary at the 2018 INFORMS Optimization Society conference** (listed in the S01 issue, p. 15): no slides or recording found.
- **The 2014 SIAM Optimization minitutorial recording** (S41): not watched (SIAM's learning platform; likely needs a login).
- **The 2025 ASU student-chapter "informal chat" about his career path** (S40): announcement only.
- **SIAM president's columns:** only April 2023 (S27) and June 2023 (S28) were found. Issues checked: January/February 2022 to April 2024 (several, including January/February, March and April 2024, which hold no further column by him). Issues from May 2024 on were not checked; the newer article pages on siam.org return 403.
- **The 2024 course videos:** all 33 transcripts of his lectures were searched by keyword, not read end to end; the 18 not saved stay in scratch. The captions are machine-made.
- **Not read:** Socn-2 to Socn-5 (2013), the 2013 "A New Augmented Lagrangian Filter Method" deck, the 2019 MIPDECO decks, the 2025 filter-ADMM deck; the application papers and slides on his site (CHEP 2018, eScience 2017, Faraday Discussions 2014, SC12, SimBuild 2010, the power-wall and SciDAC decks), whose titles promise little on method.
- **When he drops a line of work:** no statement found (2.7).
- **How he supervises in person, edits drafts or runs group meetings:** no stated method found (see note 04's gaps).
- **The MINLP book in preparation with Belotti and Mahajan** (mentioned in S19 L01): not public; the January 2024 "MINLO-book" repositories are empty (S38).
- **Wording of the 2026 AI-assisted documents** (S36, S37): which sentences are his cannot be determined.
- **Thesis:** the online copy has no preface or acknowledgements.

## Pointers for the stated-against-done check (agent 03; no judgement made here)

- B1, B12: the thermal-insulation paper (DOI 10.1007/s11081-010-9109-z) and the MacMINLP library.
- B4: the 1994 worst-case example (DOI 10.1007/BF01581153); the complementarity counterexamples cited in S01 (note 01, F8 and F9).
- B5, B8: the callback design in report NA/182 (note 01, S2); Minotaur and Uno repositories (note 01 §1.8).
- B10: the 2026 Correction (DOI 10.1007/s10107-026-02330-8).
- B15: the conDFO logbook and the "gap rulings" recorded there (note 04 §3.2).

## Sources

Primary (Leyffer's own words, alone or coauthored)
- S01 · S. Leyffer, "Nonlinear Optimization and Beyond", INFORMS Optimization Society OS Today 7(2), October 2017, pp. 3-11 (and p. 15, 2018 conference announcement) · https://higherlogicdownload.s3.amazonaws.com/INFORMS/9a2da56a-3917-4600-a0e3-84cfb0d2b004/UploadedFiles/09uQ9yCcRT5ZSlbtKE74_OStoday2017v2.pdf · primary (read in full)
- S02 · S. Leyffer (interviewer) with R. Fletcher, "It's to Solve Problems – An Interview with Roger Fletcher", Optima 99, December 2015, pp. 1-5 · https://www.mathopt.org/optima/99/optima_99.pdf · primary for Leyffer's lines (italic in print, checked on page images); Fletcher's words secondary for Leyffer
- S03 · S. Leyffer, "Obituaries" (Roger Fletcher), SIAM News 49(10), December 2016, p. 2 · https://web.archive.org/web/20240513032638/https://sinews.siam.org/Portals/Sinews2/Issue%20Pdfs/sn_December2016.pdf · primary
- S04 · R. Fletcher, S. Leyffer, Ph. L. Toint, "A Brief History of Filter Methods", Argonne preprint ANL/MCS-P1372-0906, 26 September 2006, revised 9 October 2006 · https://optimization-online.org/wp-content/uploads/2006/10/1489.pdf · primary (coauthored; read in full)
- S05 · S. Leyffer, "Integrating SQP and branch-and-bound for Mixed Integer Nonlinear Programming", University of Dundee report NA/182, 6 August 1998 · https://optimization-online.org/wp-content/uploads/2000/08/208.pdf; journal version Comput. Optim. Appl. 18(3) (2001) 295-309, DOI 10.1023/A:1011241421041 · primary (pp. 2 and 11 read as page images)
- S06 · S. Leyffer, "Deterministic Methods for Mixed Integer Nonlinear Programming", PhD thesis, University of Dundee, December 1993 (PDF re-typeset 2006) · https://web.archive.org/web/20161224053321/https://wiki.mcs.anl.gov/leyffer/images/b/b3/Thesis.pdf · primary (chapter 1 read)
- S07 · P. Belotti, C. Kirches, S. Leyffer, J. Linderoth, J. Luedtke, A. Mahajan, "Mixed-Integer Nonlinear Optimization", preprint ANL/MCS-P3060-1121, 22 November 2012; Acta Numerica 22 (2013) 1-131, DOI 10.1017/S0962492913000032 · https://web.archive.org/web/20161224050345/https://wiki.mcs.anl.gov/leyffer/images/b/b2/MINLP-Survey.pdf · primary (coauthored; pp. 8-12 and §8 read)
- S08 · J. Lee, S. Leyffer, "Preface", in J. Lee, S. Leyffer (eds.), Mixed Integer Nonlinear Programming, IMA Vol. 154, Springer, 2012, pp. vii-xiii, DOI 10.1007/978-1-4614-1927-3 · https://link.springer.com/content/pdf/bfm:978-1-4614-1927-3/1.pdf · primary (coauthored; read in full)
- S09 · S. Leyffer, "Optimization: Applications, Algorithms, and Computation. 24 Lectures on Nonlinear Optimization and Beyond", lecture notes, 30 August 2016 · https://web.archive.org/web/20161224045712/https://wiki.mcs.anl.gov/leyffer/images/0/05/NonLinOpt.pdf · primary (front matter, chapter 1, MINLP modelling section, §19.2, appendix read)
- S10 · S. Leyffer, "The Return of the Active Set Method", Argonne preprint ANL/MCS-P1277-0805, 17 February 2005, revised 5 August 2005 ("to appear in Oberwolfach Reports, 2005") · https://web.archive.org/web/20100528063143/http://wiki.mcs.anl.gov/leyffer/images/9/96/OW-05.pdf · primary (read in full)
- S11 · S. Leyffer, "Experiments with MINLP Branching Techniques", Argonne preprint ANL/MCS-P1734-0310, 23 March 2010 · https://web.archive.org/web/20100528063124/http://wiki.mcs.anl.gov/leyffer/images/4/40/EWMINLP10.pdf · primary (read in full)
- S12 · S. Leyffer, slides "Mixed-Integer Nonlinear Optimization: Applications, Algorithms, and Computation" I and VI, Graduate School in Systems, Optimization, Control and Networks, Université catholique de Louvain, February 2013 · https://web.archive.org/web/20161227081836/https://wiki.mcs.anl.gov/leyffer/images/5/52/Socn-1.pdf ; https://web.archive.org/web/20161227072726/https://wiki.mcs.anl.gov/leyffer/images/3/32/Socn-6.pdf · primary
- S13 · B. van Bloemen Waanders, S. Leyffer, T. Munson, D. Ridzal, S. M. Wild, slides "Mixed-Integer PDE-Constrained Optimization", Applied Mathematics Research for Exascale Computing, 21-22 August 2013 · https://web.archive.org/web/20161227215324/https://wiki.mcs.anl.gov/leyffer/images/f/ff/MIPDECO.pdf · primary (coauthored)
- S14 · P. Cay, B. van Bloemen Waanders, D. Kouri, S. Leyffer, slides "Mixed-Integer PDE-Constrained Optimization", ISMP 2015, Pittsburgh (deck dated 10 July 2015) · https://web.archive.org/web/20161224045930/https://wiki.mcs.anl.gov/leyffer/images/8/8b/SvenISMP15.pdf · primary (coauthored deck presented by Leyffer)
- S15 · S. Leyffer, GIAN short-course slides "Optimization: Applications, Algorithms, and Computation", 12-24 September 2016: 01-intro, 02-apps, 02a-model, 18-minlpIntro, 24-MIPDECO (the last with Cay, van Bloemen Waanders, Kouri, Thuenen) · https://web.archive.org/web/20161227215152/https://wiki.mcs.anl.gov/leyffer/images/3/33/02-apps.pdf (and sibling files under /leyffer/images/, captures of 24-27 December 2016) · primary
- S16 · S. Leyffer, J. Linderoth, slides "Modeling with Mixed-Integer Nonlinear Optimization", Summer School on Optimization of Dynamical Systems, Bremen, 3-7 September 2018; and "Optimization of Dynamical Systems 2018: MINLP Exercises" · https://web.archive.org/web/20240416020352/https://wiki.mcs.anl.gov/leyffer/images/2/20/MINLP-1.pdf ; https://web.archive.org/web/20240416014915/https://wiki.mcs.anl.gov/leyffer/images/5/5d/ExercisesMINLP1.pdf · primary (coauthored deck)
- S17 · S. Leyffer, slides "Optimization for Machine Learning", LANS Informal Seminar, 28 November 2018 · https://web.archive.org/web/20231203073852/https://wiki.mcs.anl.gov/leyffer/images/c/ca/OptiML.pdf · primary
- S18 · S. Leyffer, talk "Optimization for Machine Learning", Purdue University Workshop on Approximation Theory and Machine Learning, September 2018; video published 16 October 2018 · https://www.youtube.com/watch?v=IfjXNJI7Bug ; transcript saved as `references/sources/talks/2018-purdue-optimization-for-machine-learning.transcript.txt` · primary (ASR)
- S19 · S. Leyffer (with A. Mahajan and P. Belotti), GIAN course "Mixed-Integer Nonlinear Optimization", IIT Bombay, January 2024; 33 lectures by Leyffer · https://www.youtube.com/playlist?list=PLREyhbtkeBNpTZtDBfcwLigIsAAEGQ1iR ; 15 transcripts saved in `references/sources/talks/2024-iitb-gian-minlo/` (lecture numbers L01-L49 as in the playlist) · primary (ASR)
- S20 · S. Leyffer, slides "Writing for Success: Applying for Funding" (talks page: "Tips for Writing Proposals, SIAM Annual Meeting, Chicago, July 10, 2014") · https://web.archive.org/web/20161224051026/https://wiki.mcs.anl.gov/leyffer/images/e/e6/ProposalWriting1.pptx · primary (all four slides read)
- S21 · S. Leyffer, wiki page "Research" (last modified 27 September 2012) · https://web.archive.org/web/20210120234151/https://wiki.mcs.anl.gov/leyffer/index.php/Research · primary
- S22 · S. Leyffer, wiki pages "Sven Leyffer's Talks" (last modified 3 December 2018), "Sven Leyffer's Lectures" (2 September 2018; and the version captured 9 October 2024), "Slides from Lectures and Tutorials" (24 September 2016), "Course Material: Lecture Notes, Slides, Software" (1 December 2016) · https://web.archive.org/web/20191017082636/https://wiki.mcs.anl.gov/leyffer/index.php/Sven_Leyffer%27s_Talks ; https://web.archive.org/web/20241009003848/https://wiki.mcs.anl.gov/leyffer/index.php/Sven_Leyffer%27s_Lectures · primary
- S23 · S. Leyffer, wiki pages "MacMINLP" (last modified 5 August 2009), "MacMPEC" (17 August 2009), "MINLP Comments" · https://wiki.mcs.anl.gov/leyffer/index.php/MacMINLP (archived copies via the Wayback CDX listing, S43) · primary
- S24 · A. Aceves, H. Kaper, S. Leyffer, "Addressing Climate Change, Boosting Environmental Resilience, and Advancing Clean Energy: Reflections of the SIAM Climate Task Force", SIAM News, October 2021, p. 12 · https://web.archive.org/web/20240302072242/https://sinews.siam.org/Portals/Sinews2/Issue%20Pdfs/sn_October2021.pdf · primary (coauthored)
- S25 · S. Leyffer, president-elect statement in "Meet SIAM's newest leadership", SIAM News, January/February 2022, p. 2 · https://web.archive.org/web/20240302070316/https://sinews.siam.org/Portals/Sinews2/Issue%20Pdfs/sn_January-February2022.pdf · primary
- S26 · S. Leyffer, S. Mahajan, "Improving Earth System Predictability with Artificial Intelligence", SIAM News, July/August 2022, pp. 3-4 · https://web.archive.org/web/20240302062650/https://sinews.siam.org/Portals/Sinews2/Issue%20Pdfs/sn_July-August2022.pdf · primary (coauthored)
- S27 · S. Leyffer, "President's Column: Musings on SIAM and CSE23", SIAM News, April 2023, pp. 3, 5 · https://web.archive.org/web/20240302053630/https://sinews.siam.org/Portals/Sinews2/Issue%20Pdfs/sn_April2023.pdf · primary
- S28 · S. Leyffer, "Looking to the Future" (From the SIAM President), SIAM News, June 2023, p. 3 · https://web.archive.org/web/20240302052315/https://sinews.siam.org/Portals/Sinews2/Issue%20Pdfs/sn_June2023.pdf · primary
- S29 · J. Nagy, S. Leyffer, "Reflecting on and Reinventing SIAM Conferences", SIAM News, September 2023, p. 3 · https://web.archive.org/web/20240302050900/https://sinews.siam.org/Portals/Sinews2/Issue%20Pdfs/sn_September2023.pdf · primary (coauthored)
- S31 · S. Leyffer, S. M. Wild, M. Fagan, M. Snir, K. Palem, K. Yoshii, H. Finkel, "Doing Moore with Less -- Leapfrogging Moore's Law with Inexactness for Supercomputing", October 2016 · arXiv 1610.02606 · primary (coauthored; introduction and conclusions read)
- S32 · C. Vanaret, S. Leyffer, "Implementing a unified solver for nonlinearly constrained optimization" (v1 19 June 2024; v2 9 November 2025) · arXiv 2406.13454 · primary (coauthored; abstract read)
- S33 · D. Kiessling, S. Leyffer, C. Vanaret, "A Unified Funnel Restoration SQP Algorithm", arXiv 2409.09208 (13 September 2024); Math. Program. 217 (2025) 323-367, DOI 10.1007/s10107-025-02284-3 · primary (coauthored; abstract read)
- S34 · S. Leyffer, P. Manns, "McCormick envelopes in mixed-integer PDE-constrained optimization", arXiv 2406.07891 (v1 12 June 2024 to v5 5 January 2026); Math. Program. 218 (2025) 245-290, DOI 10.1007/s10107-024-02181-1; Correction, DOI 10.1007/s10107-026-02330-8 · primary (coauthored; abstract read; Correction metadata only)
- S35 · S. Leyffer, repository `leyffer/conDFO`: CLAUDE.md (initial check-in 15 July 2026, no AI co-author trailer), README.md (committed with a Claude co-author trailer), commit log · https://github.com/leyffer/conDFO (raw: https://raw.githubusercontent.com/leyffer/conDFO/main/CLAUDE.md) · primary
- S36 · S. Leyffer, repository `leyffer/QuantumOpt26`: .claude/CLAUDE.md, docs/project.tex ("Quantum Optimization Project", S. Leyffer and D. Linnet), .claude/plans/PLAN-2026-09-03-QuantumOpt-Skeleton.md, .claude/STATUS.md, docs/QuOptReading.tex (which states it was "Prepared via deep-research"); August-September 2026 · https://github.com/leyffer/QuantumOpt26 · primary (AI-assisted)
- S37 · S. Leyffer, repository `leyffer/BestPractices4AI`: .claude/CLAUDE.md, README.md, docs/index.md, docs/resources/links.md, docs/development/agent-design.md; July-August 2026 (scaffolding commits carry Claude co-author trailers) · https://github.com/leyffer/BestPractices4AI · primary (AI-assisted)
- S38 · GitHub REST API: repository list (10 repositories) and commit histories of user `leyffer`, fetched 2026-10-10 · https://api.github.com/users/leyffer/repos · primary (record)

Secondary
- S30 · Argonne National Laboratory (MCS news), "Leyffer named SIAM president-elect", 30 November 2021 · https://web.archive.org/web/20221128071313/https://www.anl.gov/mcs/article/leyffer-named-siam-presidentelect · secondary (quotes him)
- S39 · Argonne National Laboratory, "Leyffer named editor-in-chief of Mathematical Programming Series B" (capture of 29 December 2024) · https://web.archive.org/web/20241229085200/https://www.anl.gov/article/leyffer-named-editorinchief-of-mathematical-programming-series-b-0 · secondary (boilerplate quote only; not used)
- S40 · Arizona State University, School of Mathematical and Statistical Sciences, "SIAM Student Chapter at ASU Talk Series with Sven Leyffer", event of 2 May 2025 · https://math.asu.edu/node/9351 · secondary (announcement only)
- S41 · SIAM learning platform, "Mixed-integer Nonlinear Optimization", 2014 SIAM Conference on Optimization (presentation by Leyffer, 37 min 53 s) · https://www.pathlms.com/siam/courses/479/sections/706 · secondary (not watched)

Verification services
- S42 · Crossref REST API, metadata for the 22 DOIs named in this file, fetched 2026-10-10 · https://api.crossref.org/works/
- S43 · Internet Archive CDX API listings for wiki.mcs.anl.gov/leyffer (images and pages) and sinews.siam.org issue PDFs, fetched 2026-10-10 · http://web.archive.org/cdx/search/cdx

Third-party works named for context, each checked through S42: Duran and Grossmann (1986), DOI 10.1007/BF02592064; Quesada and Grossmann (1992), DOI 10.1016/0098-1354(92)80028-8; Borchers and Mitchell (1994), DOI 10.1016/0305-0548(94)90024-8; Bonami et al. (2008), DOI 10.1016/j.disopt.2006.10.011; Hijazi, Bonami, Ouorou (2014), DOI 10.1287/ijoc.1120.0545; Larson, Menickelly, Wild (2019), DOI 10.1017/S0962492919000060. Leyffer's own papers named inside quotations, also checked through S42: DOI 10.1007/BF01581153 (1994), 10.1007/s101070100244 (2002), 10.1137/S105262340038081X (2002), 10.1137/S1052623499357258 (2002), 10.1080/10556780410001654241 (2004), 10.1137/S1052623402407382 (2006), 10.1007/s10589-011-9430-2 (2012), 10.1287/ijoc.1090.0373 (2010), 10.1007/s11081-010-9109-z (2010), 10.1007/s12532-020-00196-1 (2021).

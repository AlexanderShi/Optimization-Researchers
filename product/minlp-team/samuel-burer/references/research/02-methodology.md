# 02 · Stated methodology: what Samuel Burer says research should be

> **Researcher**: Samuel A. (Sam) Burer, Tippie Rollins Professor and Chair / Departmental Executive Officer (DEO), Department of Business Analytics, Tippie College of Business, University of Iowa. Google Scholar BScCde0AAAAJ; DBLP 96/4845; ORCID 0000-0001-5886-458X; homepage https://sburer.github.io/.
> **Dimension**: research agent 02 of 06, stated methodology (nuwa research-craft Phase 1). This file records what he *claims* about doing research. Whether he practises it is agent 03's job. Where I mention practice, it is only to date a statement or give its context.
> **Research date**: 2026-10-10.
> **Sources consulted**: 48, listed under "Sources" as S01–S48 (39 primary, 9 secondary). Identifiers checked with a tool in this run:
> - 27 DOIs through the Crossref API (all resolved; author, venue, volume and pages matched). 25 are cited below; 2 were checked for context only (10.1007/s10107-010-0355-9, 10.1007/s10107-012-0609-9);
> - 5 arXiv ids (8 versions) through the arXiv API: 2303.01624 v1/v2, 2504.03996 v1/v2/v3, 2609.32017v1, 2406.10065v2, 2512.24295v2;
> - 5 YouTube videos through oEmbed (title and channel);
> - GitHub files, commit dates and co-author trailers through the GitHub API;
> - 2 NSF awards through the NSF API.
>
> **WebSearch calls used**: 2 of 2. One looked for interviews or advice, the other for a podcast lead. Neither found an interview.
> **Local corpus**: `references/sources/papers`, `essays`, `software` and `publications` hold only `.gitkeep`. There was no user-supplied material, so nothing below is marked "from user-supplied material". `sources/talks/` held four machine transcripts saved earlier in this run by sibling agents: the 2021 plenary (agent 01), and the 2023 Iowa talk and two 2015 R videos (sibling not named). I read all four and saved one more: `2015-basics-of-projects-in-rstudio_youtube-hKoSJGWnFFA_auto-captions.txt`. I did not open `private/`.
> **Tags**:
> - [stated] = he said or wrote it alone;
> - [stated-joint] = co-authored text, not attributable to him alone;
> - [stated, AI-assisted] = text he committed or published under his name that carries an AI co-author trailer (Claude), or was made with an AI tool (GitHub Copilot, Claude, Codex), so the wording may be the tool's;
> - [practice] = what the record shows he did; [observed] = what others wrote; [inferred] = my reading.
> - Each item also carries **P** (primary) or **S** (secondary).
>
> **Quoting**:
> - Quotations are verbatim, with the source's typos kept ("implemenation", "approximaately", "pointed about", "uncertainy", "authors knowledge", "impove").
> - Quotes from YouTube auto-captions are marked "(machine transcript)". The 2021 transcript carries caption start times [mm:ss]. For the 2023 talk, "≈mm" is my estimate from text position, not a timestamp.
> - Pages are printed journal pages where the PDF has them, otherwise preprint or slide numbers. Where text extraction dropped a math symbol, I re-read it from the rendered page and say so in the citation ("symbols read from the rendered page", "≥ checked on the rendered page", "exponents restored"). "LaTeX rendered" means an arXiv abstract's LaTeX shown as symbols.
>
> **Relation to 01 and 03–06**: when I started, `references/research/` held only `06-trajectory.md` from this run. I used it as a map of where sources live. I re-checked every quote and identifier below myself.

---

## 0. What evidence exists, and how much each kind weighs

**No methodology essay, advice column, post on how he does research, or interview was found** (see Gaps). His stated method has to be read from the genres below. A single statement in a paper's introduction is framing for that paper. A belief is one he states across genres and years (§8).

| # | Genre | Sources | Years | Solo or joint | AI involvement | What it is good for |
|---|---|---|---|---|---|---|
| G1 | Retrospective talk and slides on his PhD work, with screenshots of his 2000 e-mails to his advisor | S01, S02 | 2023 | solo | none | How an idea arose; the advisor relationship. One episode only |
| G2 | Plenary, tutorial and Festschrift talks | S03, S04, S05 | 2019–2023 | solo | none | MINLP taste, problem choice, idea-generation heuristics |
| G3 | Expository and survey writing | S13 (joint), S14 (solo), S15 (joint), S18 (solo), S25 (joint) | 2009–2023 | mixed | none | Field-level views, writing strategy |
| G4 | Award note: the only first-hand account of a project's decision path | S08 | 2010 (about 2002–2007) | joint, third person | none | Pivots, failures, what the result "illustrates" |
| G5 | Paper introductions, conclusions and acknowledgements | S09–S12, S16, S17, S19–S24, S26–S28, S48 | 2008–2026 | mixed | the 2026 Lorentz preprint discloses AI-written code and light AI editing | Motivation, hedging, errors, open questions |
| G6 | Blog posts and teaching videos | S06, S07 | 2015–2016 | solo | none | Workflow rules, applied curiosity (business-analytics teaching context) |
| G7 | Code documentation | S29–S33 | 2016–2026 | solo commits | AI-assisted in 2025–26 | Experimental norms; the wording may be the tool's |
| G8 | Course site, editorial note, grant abstracts, colloquium abstract | S34, S36, S37, S38 | 2002–2026 | joint or unclear | unknown | Low weight; dating only |

**Era and resource context of the statements** ([practice, P] from the CV S35, the repositories S29–S33 and the papers; positions from the CV):

| Period | Position | Tools and compute named in the sources | Statements drawn from it |
|---|---|---|---|
| 2000–2001 | PhD student, Georgia Tech, advisor R.D.C. Monteiro | C code for max-cut SDPs; e-mails at 23:04 and 23:54 on 22 May 2000 (S02); "G1" max-cut instance | S01, S02 (told in 2023) |
| 2002–2007 | Assistant professor in a business-school department; NSF collaborative grant (S36) | augmented Lagrangian and block coordinate descent codes for large SDPs (S08) | S08, S09 |
| 2007–2012 | Associate professor; NSF CAREER, $400,000, 2006–12 (S35, S36) | MATLAB/C solvers (OptDNN, QuadProgBB) | S10–S15, S48 |
| 2012–2019 | Full professor; department turns to analytics (renamed Business Analytics in April 2019, CV footnote); **no external research grant after 2012 in the CV** | R, MATLAB/YALMIP, Julia/JuMP/Cbc, Excel (S06, S07) | S05, S06, S07, S16–S19 |
| 2020–2023 | Chaired professor; Area Editor, *Operations Research*; plenary given online (March 2021) | Python with the MOSEK 10.0.37 Fusion API, run "on a M2 MacBook Air with 24 GB of RAM" (S24 v1, p. 4) | S01–S04, S20–S25 |
| 2024–2026 | Director of Graduate Studies, then DEO (2025–) | Python 3.14.6, MOSEK 11, Gurobi 13 (S28, S31); GitHub Copilot instructions (Dec 2025); commits co-authored with Claude Sonnet 4.6 (Mar 2026) and Claude Opus 5 (Aug–Sep 2026); "Claude (Anthropic) and Codex (OpenAI)" acknowledged (S28) | S26–S34, S38 |

---

## 1. Research taste: what is worth doing, and what a good result is

**T1. The convex hull is the reference object. It is worth pursuing even when it cannot be reached.**
- 2015, solo: "Many approaches try to characterize good classes of cuts, and of course, the best outcome characterizes all the necessary cuts to tighten a convex relaxation fully." Then: "Nevertheless, much can be learned by trying to characterize all the cuts. Indeed, such attempts account for a vast swath of the optimization literature." (S18, pp. 1–2) [stated, P]
- 2019, solo (tutorial slide): "Certainly characterizing HG is a hard problem" … "But understanding HG ⊆ S^{n+1} is our goal today" (S05, lecture 2, slide 10) [stated, P]
- 2021, solo: "i maybe could go ahead and put a stake in the ground and say well what's the best that we could ever do here i thought what's the holy grail of convex relaxations in this case" (S04 [04:51], machine transcript) [stated, P]
- 2023, solo (slide): "Then what do we care about? / Want tight conic relaxations using relaxation machinery" (S03, slide 16) [stated, P]
- 2023, joint: "The (closed) quadratic hull plays an essential role in the convexification of nonconvex QCQP. … Additional novel techniques are needed to generate strong valid inequalities for quadratic hulls." (S25, p. 6) [stated-joint, P]
- Repeated 5 times: §8 R1.

**T2. A polynomial-time algorithm for a substructure does not settle it. The research product is a tight relaxation, or "a single strong bound".**
- 2009/2012, joint: "We are also not specifically concerned with the global optimization of (MIQCP). Rather, we focus on generating strong convex relaxations and valid inequalities, which could become the basis of efficient global techniques." (S13, preprint p. 2) [stated-joint, P]
- 2021, solo: "if you're dealing with quadratic objectives over this set then it's known from beanstalk [= Bienstock] that you can solve this quadratic objectives over this in polynomial time but we're interested in tight convex relaxations" (S04 [42:32]–[43:04], machine transcript) [stated, P]
- 2023, solo (slide): "Polynomial-time solvable to ε-accuracy for fixed m (Bienstock 2016) / Then what do we care about? / Want tight conic relaxations using relaxation machinery" (S03, slide 16) [stated, P]
- 2023, solo: "(QP) can also be solved globally using any of the high-quality global-optimization algorithms and software packages available today. … In contrast, we are interested in computing a single strong bound" (S24 v1, p. 2) [stated, P]
- Also in v1: "In this paper, however, we seek a relaxation that is strong irrespective of the data." (S24 v1, p. 2) [stated, P]
- Repeated 4 times: §8 R3.

**T3. Insight over a mechanical formulation: explicit, compact, non-disjunctive descriptions, and knowing where the numbers in a result come from.**
- 2021, solo, on the disjunctive formulation of the n = 2 switching hull: "that is certainly reasonable and and it will give you the convex hole but we'd like to try a different approach we'd like to get an approach that hopefully gives us a little more insight into what's well sort of really going on here" (S04 [30:26], machine transcript) [stated, P]
- 2021, solo, on cut coefficients from Chen, Atamtürk and Oren: "to me they don't instantaneously tell you where these numbers coming from and what's really going on and that's where our motivation came from is can we understand these cuts" (S04 [40:54], machine transcript) [stated, P]
- 2021, solo, Q&A: "it's very nice to have this sort of compact representation because then at least you know kind of geometrically what's happening in all of these regions" (S04 [53:29], machine transcript) [stated, P]
- 2021, joint: "In contrast, we will show that conv(F) is SOC representable directly in the variables (x, y, z)." (S22, p. 759) [stated-joint, P]
- 2023, solo: goal "(i) to construct a new, stronger, non-disjunctive SDP relaxation" (S24 v1, p. 2). Slide: "Is there a non-disjunctive formulation for m = 2?" (S03, slide 17) [stated, P]
- 2015, solo: "Geometric insight is stressed throughout." (S18, p. 2) [stated, P]
- Nuance, same 2021 talk: the disjunction is used as a proof device: "we actually started with the disjunctive formulation that i was mentioning earlier we were able to eliminate some variables" (S04 [37:35], machine transcript). The 2020 preprint says the same: "by starting with a disjunctive representation for the convex hull and then eliminating auxilliary variables" (S21, p. 1) [stated / stated-joint, P]
- Repeated: §8 R5.

**T4. Simplicity is a virtue: simple ideas, simplified proofs, simple notation.**
- 2010, joint: "it shows that simple, classic ideas such as augmented Lagrangian and block coordinate descent still have an important role to play in modern, large-scale optimization." (S08, p. 569) [stated-joint, P]
- 2015, solo: "many of the proofs have been simplified compared to the literature" (S18, p. 3) [stated, P]
- 2019, solo (slide): "Despite being "dumb," this idea works well for finding a global (!) optimal in practice." (S05, lecture 1, slide 56) [stated, P]
- 2020, joint: "an alternate--and in our opinion, simplified--derivation of the same result" (S20, 2020 paper, p. 11) [stated-joint, P]
- 2021, solo: "there's got to be a way to simplify the proof we don't know what it is at this point yet" (S04 [37:35], machine transcript) [stated, P]
- 2023, solo (slide): "The low-rank idea has turned out to be a simple, powerful, and intriguing technique. . . with many interesting applications in optimization and machine learning" (S02, slide 63) [stated, P]
- 2023, solo: "The key idea is a simple lifting of the original problem into dimension n+1." (S24 v1 abstract) [stated, P]
- Repeated 7 times: §8 R6.

**T5. Unification: put a hard problem's difficulty in one convex cone, so that progress on the cone pays off everywhere.**
- 2009, solo: "While expressing a problem as a COP or CPP does not resolve the difficulty of the problem, it does allow one to "package" the difficulty completely inside the convex cones of copositive and/or completely positive matrices. Whatever knowledge is then gained about copositive or completely positive matrices can be applied uniformly to multiple types of NP-hard problems." (S10, p. 480) [stated, P]
- 2012, solo: "When faced with a new optimization problem, it thus seems prudent to determine if that problem can be modeled as a linear conic program over some (hopefully) well understood K." (S14, p. 202) [stated, P]
- 2015, solo: "Of course, characterizing all copositive cuts will be extremely difficult, but any progress can be applied uniformly to many different problems. This is the promise and the goal of copositive optimization." (S18, p. 2) [stated, P]
- Repeated 3 times, all sole-authored: §8 R13.

**T6. What makes a technique good: simple, powerful, "intriguing". My reading [inferred] of the quotes below: the open question of *why* it works is part of the appeal.**
- 2023, solo: "I think the low rank idea has really turned out to be a you know pretty simple powerful and intriguing technique um intriguing you know why should it work" (S01 ≈41, machine transcript) [stated, P]
- 2023, solo (slide): "Why should this work at all? … In the early 2000's, this seemed challenging to answer" (S02, slide 38) [stated, P]

**T7. A computational claim is judged head-to-head against the strongest alternative, including a co-author's own earlier method.**
- 2010, joint: "They wanted to compare their SDP-based branch-and-bound algorithm with that of an LP-only approach, which led to a comparison with Vandenbussche and Nemhauser [13] on box-constrained non-convex QPs." (S08, p. 569; the comparator is Vandenbussche & Nemhauser, *Math. Program.* 102:559–575, 2005, DOI 10.1007/s10107-004-0550-7) [stated-joint, P]
- The verdict: "To the authors knowledge, this is one of the first clear examples in which an SDP-based branch-and-bound algorithm outperforms an LP-based one." (S08, p. 569; the paper is *COAP* 43:181–195, DOI 10.1007/s10589-007-9137-6) [stated-joint, P]
- Repeated: §8 R11.

**T8. The convex/nonconvex line is the one that matters, but nonconvex does not mean hopeless (benign nonconvexity).**
- 2023, solo, attributing the framing to Rockafellar (1993) (I did not check the Rockafellar text): "what's become more common in like the last two decades is not to focus so much on linear versus non-linear but to focus more on convex versus non-convex" (S01 ≈14, machine transcript) [stated, P]
- Then: "we like convex things we don't like non-convex things" (S01 ≈16).
- Later in the same talk he qualifies it. Of benign nonconvexity: "it's a reminder that convexity or excuse me non-convexity is just not convex" (S01 ≈32, machine transcript) [stated, P]

**T9. SDP + RLT is the workhorse relaxation.**
- 2021, solo: "stp rlt is uh is a very usually a very good relaxation in a lot of cases" (S04 [38:08]). In the conclusions: "we saw that the scp-rlt was very important it's a it's a very basic structure in this type of approach" (S04 [51:18]) (machine transcript) [stated, P]
- 2023, solo (slide): "A Combined Relaxation / CH ⊆ Shor ∩ Rlt ∩ SocRlt ∩ Kron" (S03, slide 13) [stated, P]

---

## 2. Problem choice: where problems come from, why now, when to switch

**C1. Study special cases, small substructures and low dimensions first. Their value is as building blocks of general MINLP.**
- 2012, joint: "We also advocate the development of algorithms for various special cases of non-convex MINLPs. While general-purpose algorithms for MINLPs are certainly needed, since MINLP are so broad, there will always be a need for handling important special cases. Special cases can also allow the development of newer techniques (e.g., semidefinite relaxations), which may then progress to more general techniques." (S15, pp. 103–104) [stated-joint, P]
- 2015, solo: "We focus on examples having just a few variables or a few constraints" (S18, abstract p. 1). Conclusion: "the different classes could be applied anytime the corresponding geometry appears as a substructure in a given problem." (S18, p. 32) [stated, P]
- 2021, solo: "why do we focus on these substructures it's basically sometimes it's easier to focus on these on these simpler cases where you have fewer variables and fewer constraints and these really can be the basis for them convexifying more complicated miqps this is a standard technique for example that has been adopted in mixed interlinear program when you look at a one row relaxation or two row relaxation" (S04 [08:41], machine transcript) [stated, P]
- Also 2021: "we're just trying to prove uh what we can in small dimensions to give us an idea of what the how strong these inequalities are and how valuable they could be in computation" (S04 [50:45], machine transcript) [stated, P]
- 2023, solo (slide): "Why do we care? … Substructure in more general MINLPs" (S03, slide 16) [stated, P]
- 2023, solo: a side result is presented through its substructure role: quadratic programming over the set it describes, "which arises for example as a substructure in the alternating current optimal power flow problem, has an exact semidefinite representation." (S24 v1, abstract) [stated, P]
- 2023, joint: "Convexification can furthermore be applied to substructures within a problem, leading to improved convex relaxations and better bounds on the optimal value of the original problem." (S25, p. 1) [stated-joint, P]
- Repeated 6 times: §8 R2.

**C2. Use MILP as the road map, but expect insights specific to MINLP.**
- 2009/2012, joint: "the "breakthrough" results are yet to come and we believe that the past of MILP holds the clues to the future of MIQCP." (S13, preprint p. 1) Also: "our viewpoint is that many ideas from the solution of MILPs can be adapted in interesting ways for the study of (MIQCP). In this sense, we view (MIQCP) as a natural progression from MILP rather than, say, a special case of MINLP." (S13, p. 2) [stated-joint, P]
- The Optimization Online title was "Old Wine in a New Bottle: The MILP Road to MIQCP" (S43). The published chapter dropped "Old Wine in a New Bottle".
- 2012, joint: "Without a doubt, substantial successes in the fields of MILP and global optimization have played critical roles in the development of algorithms for non-convex MINLPs, and we suspect further successes will have continued benefits for MINLPs. We believe, also, that even more insights can be achieved by studying MINLPs specifically." (S15, p. 103) [stated-joint, P]
- 2021, solo: "thinking about what how we use convex relaxation when we're trying to solve these difficult problems i think it's useful useful to think about mixed integer linear programming" (S04 [03:46], machine transcript; see also the one-row/two-row analogy in C1) [stated, P]
- Repeated 3 times: §8 R4.

**C3. Find the gap between theory and computation, and work on the computation.**
- 2010, joint, about 2002–2004: "the literature dealt mainly with the theory of these relaxations, and it was clear that, for realistic IPs, the large size of the proposed SDP relaxations posed a serious computational challenge for existing SDP algorithms. So the authors focused on developing specialized algorithms for solving, possibly approximately, these large, structured SDPs." (S08, p. 567) [stated-joint, P]
- Context: assistant professor with an NSF grant whose abstract frames SDP solvers by scale (E11) (S36).

**C4. Switch problem class when the tool does not pay off: from linear IPs to nonconvex QP (about 2004–2005).** This is the only explicit, stated pivot found.
- 2010, joint: "For globally optimizing linear IPs, the authors began to realize that, even with better techniques for the SDP relaxations, these relaxations could still be ineffective, either because the bounds might still be too weak on a given problem class, or because solving the SDPs, even approximately, might still be more time-consuming than a standard IP solver" (S08, p. 568) [stated-joint, P]
- Then: "Hence, the next goal of the collaboration was to identify problem classes for which these SDPs relaxations would provide uniformly good bounds in a short amount of time." … "So the authors shifted their focus away from IPs to continuous problems in the form of non-convex quadratic programs (QPs)". Two reasons are given: similar SDP structure "and a significant amount of literature indicated the strength of such SDP relaxations in the continuous case", and the co-author's finite LP-based branch-and-cut (S08, p. 568) [stated-joint, P]
- This is a recorded abandonment (SDP-based global solution of linear IPs), with the reasons stated.

**C5. Someone else's unexplained result is a problem.**
- 2021, solo: the Chen–Atamtürk–Oren cuts. See T3: "that's where our motivation came from" (S04 [40:54]) [stated, P]
- 2023, joint: "Indeed, our initial motivation for this paper was the desire to understand the inequalities in [9] more fully." (S23, p. 285) [stated-joint, P]

**C6. Signals that an area is open, and his advice on where to go.**
- 2012, joint: "Finally, we believe there will be an increasing place for heuristics and approximation algorithms for non-convex MINLPs. Most techniques so far aim for globally optimal solutions, but in practice it would be valuable to have sophisticated approaches for finding near-optimal solutions." (S15, p. 104) [stated-joint, P]. Compare his own later stated focus in T2 (see Contradictions 6).
- 2019, solo (slide): "For nonconvex QP, there is still lots to do, especially the integer case / Convexification involves aspects of convex analysis, polyhedral theory, SDP, polynomial optimization / Hence, a very interesting area to study" (S05, lecture 2, slide 61) [stated, P]
- 2023, solo: "benign non-convexity is an important idea I think it's something that could be a nice area to explore" (S01 ≈41, machine transcript). Slide: "Benign nonconvexity is an important area with lots to explore" (S02, slide 63) [stated, P]
- Repeated: §8 R10.

**C7. The research plan as funded (2006): computation, theory and applications together.**
- "This project focuses on computation, theory, and applications in the field of optimization" … "this project develops new approaches (e.g., through advanced computational techniques and algorithmic development) for solving problems either exactly or approximately and applies them to specific applications." (S36, NSF CAREER 0545514 abstract) [stated, P; the abstract is unsigned, and PI authorship is [inferred]]

**C8. Applied problems from his own surroundings** (side line, 2011–2019, in a department turning to analytics).
- Football, 2012, solo: "our research was in part motivated by a situation that arose at the end of the 2010 regular season" (S16, p. 4) [stated, P]
- Grading, 2019, joint: "the process of grading students throughout a course--including assigning the final letter grade--is one of the most important duties of a professor." (S19, pp. 364–365) [stated-joint, P]
- Blog, 2015, solo: "I'm not sure if anyone actually plans to visit all 34 homes---hey, why not?! If someone did do this, I wondered: *which route visiting all 34 homes minimizes total driving time?*" (S07, 2015-05-22) [stated, P]
- Blog, 2015, solo: "To visualize the contributions and connections between groups in the optimization community (just for fun!)" (S07, 2015-06-17) [stated, P]
- Repeated: §8 R14.

---

## 3. Idea generation

**I1. "Can't hurt to try": put a known theorem together with a known trick, then test it at once.**
- 2023, solo (slide): "Still equivalent to the SDP...but with a very different feasible set / The potential advantage was less computation and storage / But would it actually work in practice? / Can't hurt to try" (S02, slide 30) [stated, P]
- Talk version: "we thought you know it couldn't hurt to try" (S01 ≈23, machine transcript) [stated, P]
- The ingredients, as he lists them: "Peinado and Homer (1997) proposed to optimize directly with U (instead of X)"; "B and Monteiro (2001) saved time and space by taking U lower triangular"; then "Theorem (Shapiro 1982, Barvinok 1995, Pataki 1998) There exists an optimal solution X* with rank r* < √(2m)." (S02, slides 27–28; symbols read from the rendered slide). Talk: "that was the key thing that we put together" (S01 ≈22, machine transcript) [stated, P]
- Era: PhD student in 2000. The paper that resulted is *Math. Program.* 95:329–357, 2003, DOI 10.1007/s10107-002-0352-8.

**I2. Lift to a higher dimension, convexify there, project back. He calls this "an important theme".**
- 2021, solo: "can i introduce other variables and convexify in a higher dimensional space and somehow then project back down and somehow make the convexification easier" (S04 [05:56], machine transcript) [stated, P]
- 2019, solo (slide): "If your QP doesn't contain all O(n²) variables, it may make sense to convexify just over your variables / In fact, it might be better to lift to an even larger set of variables" (S05, lecture 2, slide 10) [stated, P]
- 2023, solo: "The key idea is a simple lifting of the original problem into dimension n+1." (S24 v1) [stated, P]

**I3. A two-question decision grid for relaxation design: how many auxiliary variables, and which cone.**
- 2021, solo: "i'm going to suggest an overly simplistic a very somewhat admittedly naive way to think about the tools at our disposal … how many how many additional auxiliary variables am i willing to deal with am i willing to tolerate … what type of constraint … am i willing to deal with can i deal with linear programming second order cone programming or sdp" (S04 [09:47]–[10:19], machine transcript) [stated, P]
- Corollary heuristic: "a lot of times if you commit yourself to socp then you might as well add in some linear constraints as well it at least doesn't make the technology any more difficult" (S04 [10:53]) [stated, P]
- 2023 slides apply the grid as tables of "# variables", "# SOC constraints" and "# Kronecker SDP constraints", before and after lifting (S03, slides 20–22) [stated, P]

**I4. Recombine the constraints at hand, borrowing a device from a neighbouring field for one specific case.**
- 2021, solo: "we said well let's see if we can combine these ingredients in different ways" (S04 [45:18]). And: "this kind of idea comes up in polynomial optimization where you use polynomials as multiple non-negative polynomials as multipliers to keep you in a cone and essentially that's what we're applying here but in a very specific case" (S04 [45:50]) (machine transcript) [stated, P]
- Conclusion of the same talk: "there's always going to be uh the availability of exploiting the structure that you have on hand in your problem to derive valid constraints" (S04 [51:50]) [stated, P]

**I5. Look for relaxations "between" two extremes.**
- 2014, joint: "We are motivated by the idea that there should exist relaxations between the two extremes introduced in the previous section: SOCPs in only x versus SDPs in both (x, X). By "between," we mean that these hypothesized relaxations solve faster than SDPs while providing better bounds than SOCPs." (S17, p. 30) [stated-joint, P]

**I6. Ideas come from colleagues' fields.**
- 2010, joint: "It was part of a collaboration mostly motivated by the desire of each author to gain a greater understanding of the other's field of expertise." (S08, p. 567) [stated-joint, P]
- On how they solved the hard step: "The hard part was that the resulting LP and SDP relaxations were unbounded. However, by combining features of both relaxation types, the authors overcame this hurdle" (S08, p. 568) [stated-joint, P]
- 2016, reported by a journalist: "Burer's team borrowed an idea from finance: the theory of portfolio management and risk tolerance." (S39) [observed, S]

**I7. Reproduce someone else's analysis with a simpler approach.**
- 2015, solo blog: "I wanted to reproduce their basic analysis but with a simpler approach and easier-to-obtain data set, and I also wanted to complete the full analysis in R." He ends: "Overall, I reach the same conclusion as Silver and Fischer-Baum" (S07, 2015-05-10) [stated, P]

**I8. Computation produces conjectures.** Listed under J2, where their fate is recorded.

---

## 4. Experiments and execution

**E1. Prototype within a day, and measure the speed.**
- 22 May 2000, 23:04, e-mail to his advisor, shown on a 2023 slide: "I did a quick implemenation of the low-rank idea for the primal maxcut that we were talking about, and it looks promising. The convergence is good, and of course, the computation and memory requirements are less. / One example: On G1, the new approach cuts the times for both the function and gradient evaluations by approximaately 1/2." (S02, slide 31) [stated, P (2000 text)]
- The advisor's reply at 23:54, shown on slide 33: "This is really good news. Let us hope that this approach works well on all problems. If so, we may have some chance to compete with the bundle method on some maxcut problems." [observed: Monteiro's words, shown by Burer, P]
- 2023 retelling: "so we were very motivated by just sort of having a fast code" and "I'd been able already to streamline it and get it roughly 30 times faster so so this was you know some quick stuff that we're doing just to get it the Prototype out there and then it turned out to be it turned out to work" (S01 ≈24, machine transcript) [stated, P]

**E2. Experiment beyond what the theory licenses.**
- 2023, solo (slide): "Also experimented with: / Restricting the rank smaller than required by theory / Dynamically updating the rank / Heuristically solving NP-hard problems using rank-2 approaches (with Y. Zhang)" (S02, slide 35) [stated, P]
- Talk: "so there's all sorts of little things that we tried" (S01 ≈25, machine transcript)
- On the method: "we pull a a standard algorithm off the shelf but with one tweak" (S01 ≈30) [stated, P]

**E3. Compare against the strongest known combination, the "kitchen sink".**
- 2021, solo: "with a little bit of tongue-in-cheek i want to call this uh the kitchen sink … it turns out that the kitchen sink does not capture the convex hole even if the dimension is equal to two" (S04 [44:46]–[45:18]). And: "despite all the power of all the kitchen sink things you can hear get something new by arranging the ingredients in a particular way" (S04 [46:58]) (machine transcript) [stated, P]
- 2023, joint: "we have demonstrated that the new class of valid inequalities strengthens the strongest known SDP relaxation" (S23, p. 305) [stated-joint, P]
- 2026, AI-assisted README: "No Gurobi incumbent or point recovered by another method is used to improve an SDP method's gap. Gurobi is reported separately using its own incumbent and global bound." It also fixes Gurobi's time limit at "max(5, 3*t_max) seconds, where t_max is the longest conic-method time on that instance". (S31) [stated, AI-assisted, P]

**E4. Fixed measures of relaxation quality.**
- Volume as a proxy for branching value, 2021, solo: "part of the reason we branch is so that the the size of the feasible sets gets sort of cut in half … if you could branch in such a way that the total volume um in the branches the feasible sets of the branches were relative relatively small or as small as possible that could be a good computational strategy" (S04 [21:09]). Result: "branching at 0.5 is not such a great idea but branching around point two is a much better idea in terms of the volume" (S04 [22:15]) (machine transcript) [stated, P]
- "Solved" criterion, 2023, solo: "we say a relaxation solves an instance if both the relative gap is less than 10^-4 and the eigenvalue ratio is more than 10^4" (S24 v1, p. 13; exponents restored) [stated, P]
- Tightness rule, 2026, AI-assisted: "A result is classified as tight when this relative gap is at most `1e-5`." (S31) [stated, AI-assisted, P]
- Gap formula, 2026, AI-assisted: "The dual value is used because weak duality makes it a rigorous lower bound, so the relative gap is nonnegative and vanishes exactly when the relaxation is tight." (S29) [stated, AI-assisted, P]

**E5. Screen out trivial instances before reporting.**
- 2026, AI-assisted: "Because Shor is exact on many candidates, a rank-one screen selects ten nontrivial instances at each dimension." And: "The first ten seeds at each size whose Shor relative gap exceeds `0.01` are retained" (S31) [stated, AI-assisted, P]

**E6. Begin with the simplest configuration that shows the basic behaviour.**
- 2014, joint: "Although this approach does not take full advantage of the data (Ai, ai, αi), we feel this approach allows us to study the basic features of our framework." (S17, p. 39; symbols read from the rendered page). Conclusion: "We did so with the intent of just testing the basic behavior of our framework" (S17, p. 44) [stated-joint, P]

**E7. Keep claims in exact arithmetic apart from numerical evidence, and report only bounds that stay valid when the solves are inexact.**
- 2008, joint: "We stress that the theorem is concerned with the solution of (QP) in exact arithmetic." (S09, p. 269) And: "in practice, concerns of an infinite tree are quite irrelevant due to the inexact nature of floating-point arithmetic." (S09, p. 261) [stated-joint, P]
- 2010, solo: "we propose a practically efficient decomposition technique, which approximately solves the DNPs while simultaneously producing lower bounds on the original NQP." (S11, abstract p. 1) [stated, P]
- 2019, solo (slide): "Observation. Relying on rational or floating-point arithmetic, we cannot expect to optimize SDPs exactly" (S05, lecture 1, slide 36) [stated, P]
- 2026, README (the commit carries no AI trailer): "Consequently, the reported separations do not depend on an SDP solver's numerical tolerance." (S30) [stated, P]
- 2026, AI-assisted README: "the paper's central new claim … is checked in exact rational arithmetic with no solver and no floating point." (S29) [stated, AI-assisted, P]
- 2026, joint: "Section 6.4 verifies these claims in exact rational arithmetic" (S27 v3, p. 14) [stated-joint, P]
- Repeated across 2008–2026: §8 R8. The emphasis shifted over time (Contradictions 8).

**E8. Make work shareable and reproducible.** He stated this first as a teaching rule. It became a research-code norm in 2025–26.
- 2015, solo teaching video: "there's one key Rule and that is you should use relative paths not absolute paths always use relative paths inside your project folders that's because if you send it to somebody else and you use absolute paths they may not have those paths on their computer" (S06, mV9vd5urqdU, machine transcript) [stated, P]
- 2015, solo: "projects make it really easy to use relative paths if you store everything in the project form" (S06, hKoSJGWnFFA, machine transcript) [stated, P]
- 2016–2024 READMEs: "Software and scripts to accompany the paper …" (S33: soctrust 2016, ttrs 2016, grades 2018, ttrsn2 2024) [stated, P]
- 2025, Copilot instructions: "**Reproducibility**: Default is seeded (`reproducible=True`)." (S29) [stated, AI-assisted, P]
- 2026, AI-assisted README: "This repository reproduces every computational claim the paper makes." and "Every randomized experiment is seeded and deterministic" (S29) [stated, AI-assisted, P]
- 2026, AI-assisted README: "The code supports three levels of reproducibility" and "the published numbers can be checked without rerunning the expensive solver experiments." (S31) [stated, AI-assisted, P]
- 2026, joint paper: "For reproducibility, all code is archived at https://github.com/sburer/lorentz-positive." (S28, p. 8) [stated-joint, P]
- Repeated: §8 R9.

**E9. Check the assumptions, and test before touching numerics.**
- 2019, solo (slide): "Remark. Algorithmic papers and results often assume both (P) and (D) have interior. But...in any given application, make sure to double check!" (S05, lecture 1, slide 34) [stated, P]
- 2026, AI-assisted developer guide: "Do not attempt to normalize to pure 0-based indexing without first building a comprehensive test suite — a single missed conversion produces silent wrong answers in the numerics." (S32, CLAUDE.md) [stated, AI-assisted, P]

**E10. Solver settings and machines.**
- 2026, joint: "Solver defaults were used unless otherwise stated; in particular, we did not manually fix thread counts." (S28, p. 8) [stated-joint, P]
- 2026, AI-assisted README: "Bounds and gaps should reproduce on other machines to solver tolerance, but wall-clock times naturally vary." (S31) [stated, AI-assisted, P]
- 2023, solo: "all computational results in the paper were coded in Python using the Fusion API of MOSEK 10.0.37 [3] and run on a M2 MacBook Air with 24 GB of RAM." (S24 v1, p. 4) [stated, P]
- Resource scale [practice, P]: in 2026 a full TTRS panel "required about 76 hours on the reference machine" (S31).

**E11. Choose the solver class by problem size. Specialized beat black-box, "at this point in time".**
- 2002, joint (NSF abstract): "The choice of which class to use for a particular application is determined primarily by problem size --- second-order IP methods are more efficient on small- to medium-scale problems while first-order NLP methods are better for large-scale problems." (S36, award 0203426) [stated-joint, P]
- 2010, solo: "Optimizing a DNP, while polynomial, is expensive in practice for interior-point methods." (S11, abstract) [stated, P]
- 2019, solo (slide): "Interior-point methods effectively deliver high accuracy for small- to medium-scale problems / But they slow down for large instances / Definition of "large"? When the algorithm slows down" (S05, lecture 1, slide 54) [stated, P]
- 2009/2012, joint: "This illustrates a recognized trend in solving relaxations of this sort, namely that, at this point in time, specialized solvers perform better than black-box ones. Perhaps this will change as black-box solvers become more robust." (S13, preprint p. 29) [stated-joint, P]
- Later wording, Contradictions 2: by 2023 he names general global solvers as the available alternative (T2). In 2026 "Gurobi supplies the global optimization comparisons" (S31).

**E12. AI tools are disclosed (2025–2026).**
- 2026, joint: "The AI assistants Claude (Anthropic) and Codex (OpenAI) were used to write the code for the computational experiments and for light editing of the text." (S28, p. 20) [stated-joint, P]
- The Copilot instruction file (S29, committed 12 Dec 2025 without a trailer; its style matches GitHub's auto-generated instruction files [inferred]) states project norms such as "Never allow negative gaps" and "Check `M.getProblemStatus() == 'PrimalAndDualFeasible'` before extracting solutions." [stated, AI-assisted, P]

---

## 5. Judging results: evidence, conjectures, failures and corrections

**J1. Label what is believed but not proved.**
- 2008, joint: "From a practical standpoint, we have actually never observed a situation in our test problems for which the optimal value of (SDP1) is strictly lower than that of (SDP0). We believe this is evidence that the specific function … is rather weak" (S09, p. 271) [stated-joint, P]
- 2010, solo: "our relaxation is quite similar to Burer-Vandenbussche, and we believe, but have not rigorously proved, that the two are equivalent." (S11, pp. 12–13) [stated, P]
- 2023, solo: "is it possible to prove that our relaxation Beta is always at least as tight as Kron, which is supported by the computational evidence?" (S24 v1, p. 27) [stated, P]

**J2. Computation generates conjectures, and some have failed.** The conjectures, in date order:

| Date | Conjecture (as stated) | Source | Fate |
|---|---|---|---|
| Feb 2020 | n = 2 switching hull: "An alternative derivation for this representation leads to an appealing conjecture for a simplified representation of the convex hull for n = 2 when the product term y1y2 is ignored." | S21, p. 1 [stated-joint, P] | In March 2021 still open: "we were not able to prove this conjecture" and "this conjecture is still to be proven hopefully we can simplify the analysis" (S04 [35:24], [38:41]) |
| Mar 2021 | "we did a lot of computational experiments and we came up with a conjecture" | S04 [34:50] [stated, P] | Open in the talk |
| 2022/2023 | "Our computational experience thus motivates a conjecture" and "We believe this is strong evidence to support the following conjecture" (2-D extended TRS) | S23, pp. 302–303 [stated-joint, P] | Not checked here |
| Feb 2023 | Conjecture 1 in the ball-constraints preprint | S24 v1, p. 27 | Not checked here |
| 7 Apr 2026 | "based on extensive numerical testing, we conjecture that the relaxation is exact for all n." | S38 (Cornell colloquium abstract) [stated, P, on a secondary host] | **Refuted** in v3 (31 Aug 2026): "Via an explicit counterexample for n = 4, we show that the relaxation is not tight in general" (S27, S42) |
| Aug 2026 | "The paper's lifted formulations motivate two natural conjectures … These conjectures are **not statements made in the paper**. Both turn out to be false in dimension two" | S30 [stated, P] | **False**, with exact certificates |

Repeated: §8 R7.

**J3. When a claim fails, narrow it to what is provable, name who found the error, and locate the failure precisely.**
- 2009, solo acknowledgement: "Immanuel Bomze for pointing out an earlier error in Proposition 2.3" (S10, p. 495) [stated, P]
- 2021, joint erratum (author version, 18 Feb 2021): "This note reports an error in Theorem 3 of [1], which was pointed about by Prof. Fatma Kilinç-Karzan and Mr. Alex Wang of Carnegie Mellon University, whom we sincerely thank for bringing this to our attention." … "However, in truth the proof fails because, with this setup, the systems cannot be simultaneously feasible." … "Instead of the purported Theorem 3, we now prove an analogous theorem, except that it only applies to diagonal instances of (1)." (S20, erratum p. 1; published as DOI 10.1007/s10107-021-01684-5) [stated-joint, P]
- 2025 → 2026, the submodular preprint, in four steps:
  - v1 (4 Apr 2025): "We show that continuous quadratic submodular minimization with bounds is solvable in polynomial time using semidefinite programming" (S27, abstract). Its §2.2 relaxation "is tight for every submodular (Q, c, κ) irrespective of the signs of the entries of c" and "Our proof is by induction on n with base case n = 1." (S27 v1, p. 6; κ read from the rendered page) [stated-joint, P]
  - Cornell abstract (7 Apr 2026): "provably exact when n is at most 3 … we conjecture that the relaxation is exact for all n" (S38).
  - v2 (5 Apr 2026): "provably tight for dimension n ≤ 3 and empirically tight for larger n" (S27, S42; LaTeX rendered).
  - v3 (31 Aug 2026): "We thank Shaoning Han for pointing out an error in an earlier version of this paper." … "What fails at n ≥ 4 is therefore this particular semidefinite certificate, not necessarily tractability itself. The complexity of minimizing a submodular quadratic over [0, 1]^n for n ≥ 4 remains open, and settling it will require either a different certificate or a hardness reduction." (S27 v3, p. 46; ≥ checked on the rendered page) [stated-joint, P]
- Repeated (naming the finder): §8 R12.

**J4. Report an extension that failed, with a hypothesis for why.**
- 2023, solo: "We also tried to apply the ideas of this paper to (TTRS) … However, the resulting relaxations were no tighter empirically than those already in the literature, and we were unable to make further progress specifically on (TTRS). We hypothesize that the shared geometry of balls, as represented by the reappearance of the norm ‖x‖, is critical for the approach of this paper." (S24 v1, p. 4; ‖x‖ read from the rendered page) [stated, P]
- The two-trust-region subproblem (TTRS) returned as a test family in 2026 with Anstreicher (S28, S31) [practice, P].

**J5. A negative empirical verdict can be reversed by a better construction. The case of the ball-constraints paper:**
- v1 (Feb/Mar 2023): "As we began this project, we were motivated by the idea of constructing an exact relaxation for (QP). … Nevertheless, we still had hope for the case m = 2. Ultimately, we will show by experimentation that our construction is not exact for m = 2 and hence for all m; see Section 4. Even still, we believe that our new relaxation makes significant progress towards approximating (QP) as we demonstrate empirically." (S24 v1, pp. 2–3, checked on the rendered pages) [stated, P]
- June 2023 slides: "Theorem (B 2023 — but gifted to Kurt) / For m = 2, it holds that CH+ = Shor+ ∩ Rlt0+ ∩ SocRlt+." (symbols read from the rendered slide) Proof: "Leverages key idea of Ye-Zhang (2003) with a key assist from Kurt." (S03, slide 24) [stated, P]
- v2 (28 Oct 2023): "Ultimately, we will show that our relaxation is exact for m = 2 but inexact for m ≥ 3" (S24 v2, p. 3; ≥ checked on the rendered page). Acknowledgement: "The author expresses his sincere thanks to Kurt Anstreicher for an important observation, which ultimately led to the establishment of Theorem 1." (S24 v2, p. 24) [stated, P]
- That the m = 2 relaxation changed between v1 and v2 (an RLT condition imposed as an equality, "Rlt0" on the slides) is [inferred] from the slides and the v2 proof. I did not compare the two constructions line by line.

**J6. Publish negative or partial results, and frame them.**
- 2011, joint: "we prove the surprising, somewhat negative result that all three achieve the same optimal value. (On the positive side, the proof establishes several interesting analytical properties of (SDP0), which are of independent interest.)" (S12, p. 654) [stated-joint, P]
- 2023, solo, on his 2003 theory: "it wasn't a perfect result it's kind of a partial result" and "we had some kind of strong assumptions here but this was the best variable [≈ we were able] to do at that time" (S01 ≈31, machine transcript) [stated, P]
- 2019, solo (slide): "In 2003, we had a limited theory to explain why" (S05, lecture 1, slide 56) [stated, P]
- 2009, solo: "This paper significantly broadens the application of copositive and completely positive programming. Still, more work is necessary to exploit these formulations in practice" (S10, p. 494) [stated, P]
- Repeated (empirical success ahead of theory): §8 R15.

**J7. Whether a relaxation is good in practice is judged empirically, and genericity is part of the argument.**
- 2021, solo, on dropping the locally valid side cuts: "it's amazing how little the side constraints are actually cutting off so differently the center constraint could be enough in practice" (S04 [24:30], machine transcript) [stated, P]
- 2026, joint: "The experiments of Section 5.1 indicate that instances exhibiting a gap are highly non-generic, so the relaxation continues to perform well in practice even though it is not tight in general." (S27 v3, p. 46) [stated-joint, P]
- 2024, joint, choosing between error metrics: "We believe that overall this constitutes an advantage of CH+ because, generally speaking, one cannot have true optimality without true feasibility." (S26, p. 20) [stated-joint, P]

**J8. A strong but expensive relaxation can be worth it.** This is a dated verdict. Later statements treat strength against cost as a choice on a spectrum (Contradictions 1).
- 2010, joint: "More generally, the paper also illustrates that it can be worthwhile to pay for a computationally expensive, but strong, relaxation compared to evaluating many inexpensive relaxations." (S08, p. 569) [stated-joint, P]
- 2014, joint: "When attempting to solve difficult QCQPs, the bounds provided by SDP relaxations can be tight and hence quite useful, but they can also be time consuming to calculate." (S17, p. 44) [stated-joint, P]

**J9. Verification as a general rule (2026, joint course site for non-researchers).**
- Block titles: "Asking well, verifying hard" ("Revise the request, then check what the tool gives you."), "Research that holds up", and "Making it all repeatable" ("Capture the useful method so you can use it again.") (S34, modules page, marked "Planning draft") [stated-joint, P]

---

## 6. Writing and talks

**W1. Expository strategy: from easiest to hardest, unified, small examples, geometry first.**
- 2015, solo: "Hence, our main contribution is a unified presentation of the various results, and we do so from "easiest to hardest" in hopes of gently introducing the reader to the insights provided by copositive optimization." (S18, p. 3). "A particular highlight is the role played by the geometry of the feasible set." (S18, abstract) [stated, P]
- 2015, solo, on notation: "We do this partly to keep the notation as simple as possible. However, we also hope that this reuse will actually assist the reader in understanding the main points of the paper. This is because, while G has a different, specific meaning in each section, it plays the same general role always." (S18, p. 3) [stated, P]
- Notation warnings recur [stated, P]:
  - "We caution the reader that, in order to simplify the notation, we sometimes abuse it." (S48, p. 38, joint);
  - "We caution the reader that we will reuse (or "overload") some notation in this section." (S24 v1, p. 4, solo).

**W2. Say what a text does not claim.**
- 2015, solo: "We would also like to emphasize that we do not claim to have identified the best or only way to solve each of the various problem types--or that these are the most practically relevant problem classes. Moreover, we do not compare with other methods" (S18, p. 3) [stated, P]
- 2012, solo: "Instead, we intend only to give an introduction to some of the main results in the area, tainted with our own biases." (S14, p. 203) [stated, P]
- 2012, joint: "In this survey, we have tried to give a fair and up-to-date introduction to these techniques." (S15, p. 103) [stated-joint, P]
- 2015, solo blog, on choosing k = 22: "This seemed like a balanced guess, but it is just a guess." (S07, 2015-06-02) [stated, P]
- 2026 README: "These conjectures are **not statements made in the paper**." (S30) [stated, P]
- Repeated: §8 R16.

**W3. A survey is a catalogue and a road map for readers from a neighbouring field.**
- 2009/2012, joint: "First, it helps to catalog some of the recent results in a form that is accessible to a researcher with reasonable background in MILP. Second, it defines a roadmap for further research in MIQCP" (S13, preprint p. 1) [stated-joint, P]

**W4. Talk craft.** All [stated, P], from his own talks.
- Open with a memorable picture: "because you probably need some kind of joke or something to remember at the beginning of a talk I wanted to show you a picture from that time" (S01 ≈1, machine transcript).
- State goals and return to them: slide "My Goals" (S02, slide 2) and closing slide "Goals Redux" (S02, slide 63).
- Offer a deliberately crude mental model: "an overly simplistic … somewhat admittedly naive way to think about the tools" (S04 [09:47]).
- Use playful names: "with a little bit of tongue-in-cheek i want to call this uh the kitchen sink" (S04 [44:46]).
- Pictures from the literature: "I went uh I scoured through papers that um that that talk about this" (S01 ≈27).
- In 2023 he quoted ChatGPT for a definition: "this is the internet's version of what I'm talking about" (S01 ≈8).
- Thank co-authors first: "this talk definitely would not be possible without them" (S04 [01:37]).

**W5. End with open questions.**
- 2009, solo: "Some other questions of interest are:" followed by three questions (S10, pp. 494–495) [stated, P]
- 2023, solo: "There are many open questions related to this research, e.g., Conjecture 1." (S24 v1, p. 27) [stated, P]
- 2026, joint: "We believe that additional applications of these LMI representations could be a fruitful area for further research." (S28, p. 20) [stated-joint, P]
- Repeated with the "lots to explore" closings (C6): §8 R10.

**W6. Titles with a hook, and documentation for outside readers** [practice, P].
- Titles: "Old Wine in a New Bottle" (2009 preprint title, S43), "Faster, but weaker, relaxations…" (S17), "A gentle, geometric introduction…" (S18), "A slightly lifted convex relaxation…" (S24).
- Commit message "Rewrite README for external readers" (22 Sep 2026, S31).

---

## 7. Research organisation: collaboration, students, time, career

**O1. Collaborate to learn another field.** See I6 (S08, p. 567) [stated-joint, P].

**O2. The advisor relationship, as he presents it (2023).**
- He gave four slides the title "The Advisor-Advisee Relationship" (S02, slides 31–34). They show the 22 May 2000 e-mails (E1) [stated, P].
- On his advisor's availability: "Montero was very nice to me I would go by all the time and would talk to me as much as I wanted to talk" (S01 ≈23, machine transcript) [stated, P]
- On working hours, addressed to students: "the time just for any graduate students in the room the time was about 11 pm" (S01 ≈24) [stated, P]
- On his own boldness: "I also told him I was a little bit bold I said you come to school this afternoon please drop by the computer line [= lab] … I probably shouldn't have done that" (S01 ≈24) [stated, P]
- I found no statement of how *he* supervises (Gaps).

**O3. Credit norms: name contributors in the theorem attribution, the acknowledgements and the talk.**
- "Theorem (B 2023 — but gifted to Kurt)" and "with a key assist from Kurt" (S03, slide 24) [stated, P]
- "sincere thanks to Kurt Anstreicher for an important observation, which ultimately led to the establishment of Theorem 1" (S24 v2, p. 24) [stated, P]
- Thanks to error finders: J3.
- Co-authors: W4.
- Repeated: §8 R12.

**O4. Keep records.**
- "I went back into my old emails which I actually still have" (S01 ≈23, machine transcript). The slide shows "Message 1,371 of 2,501" in a `Monteiro.mbox` file (S02, slide 31) [stated, P]

**O5. Teaching is part of the job description.**
- CV interests include "Teaching at all levels (undergraduate, Master's, doctoral, evening, online, executive)" (S35) [stated, P]
- CAREER plan (2006): "Efforts are appropriately targeted to the experience and background of the intended audience" (S36) [stated, P; authorship as in C7]
- 2026 course instructor line: "Sam will help participants turn real questions and materials into careful, useful work." (S34) [stated-joint, P]

**O6. Learn from senior figures' own accounts** (joint editorial, low weight).
- Optima 99 (Dec 2015), signed by Burer, Kaibel and Linderoth: "Listening to what the leaders in our field have to say is not only very informative but also a most enjoyable experience." (S37) [stated-joint, P]

**O7. Rules for working with AI tools (2026, course for non-researchers, joint).**
- "Context is not permission. You decide what may be shared and what belongs in the task." (S34, context page) [stated-joint, P]
- "Select context; do not shovel it in" … "More material is not automatically better. Include what changes the answer; leave out what does not." (S34, context page) [stated-joint, P]
- "Your organization's rules still apply." (S34, setup page) [stated-joint, P]
- In his own research code, the practice is AI co-authored commits plus disclosure (E12).

**O8. Department-level evaluation (DEO role, 2026; institutional, not personal).**
- The rankings site he maintains counts "Papers on A-List" ("Number of publications appearing in the department’s designated A-list journals and conferences.") per faculty member, 2020–2024 (S33, business-analytics-rankings README and page) [stated-joint (department), P]

---

## 8. Claims repeated at least 3 times (real beliefs by the framework's rule)

Counts are of distinct sources (talks, documents), not of repeated phrases inside one source. "AI" marks counts that include AI-assisted text.

| # | Belief | Count | Where (year) | Solo or joint |
|---|---|---|---|---|
| R1 | The convex hull is the target. Trying to characterize it teaches even when it is out of reach | 5 | S18 (2015), S05 (2019), S04 (2021), S03 (2023), S25 (2023) | 4 solo, 1 joint |
| R2 | Work on special cases, substructures and small dimensions first, as building blocks for general MINLP | 6 | S15 (2012), S18 (2015), S04 (2021), S03 (2023), S24 (2023), S25 (2023) | 4 solo, 2 joint |
| R3 | Polynomial-time solvability of a substructure is not the point; tight relaxations and strong bounds are | 4 | S13 (2009/12), S04 (2021), S03 (2023), S24 (2023) | 3 solo, 1 joint |
| R4 | MILP is the road map for MIQCP/MINLP | 3 | S13 (2009/12), S15 (2012), S04 (2021) | 1 solo, 2 joint |
| R5 | Insight over mechanics: understand where cuts come from; prefer compact, direct, non-disjunctive descriptions | 6 | S08 (2010), S18 (2015), S04 (2021), S22 (2021), S23 (2023), S24/S03 (2023) | 3 solo, 3 joint |
| R6 | Simplicity: simple ideas, simplified proofs and notation | 7 | S08 (2010), S18 (2015), S05 (2019), S20 (2020), S04 (2021), S02 (2023), S24 (2023) | 5 solo, 2 joint |
| R7 | Computation suggests conjectures; numerical evidence is called evidence, not proof | 7 | S09 (2008), S11 (2010), S21 (2020), S04 (2021), S23 (2023), S24 (2023), S38 (2026) | 4 solo, 3 joint |
| R8 | Separate exact-arithmetic claims from floating-point results; report only rigorous bounds | 6 | S09 (2008), S11 (2010), S05 (2019), S29 (2026, AI), S30 (2026), S27 v3 (2026) | 4 solo (one AI-assisted), 2 joint |
| R9 | Make work shareable and reproducible | 5 | S06 (2015), S33 (2016–24), S29 (2025–26, AI), S31 (2026, AI), S28 (2026) | 4 solo (two AI-assisted), 1 joint |
| R10 | Present the field as open ("lots to explore"; open-question lists) | 6 | S10 (2009), S05 (2019), S04 (2021), S02 (2023), S24 (2023), S28 (2026) | 5 solo, 1 joint |
| R11 | Benchmark against the strongest known combination, kept separate from competitors' results | 4 | S08 (2010), S04 (2021), S23 (2023), S31 (2026, AI) | 1 solo, 2 joint, 1 AI |
| R12 | Credit contributors and error finders by name | 5 | S10 (2009), S20 (2021), S04 (2021), S03/S24 (2023), S27 (2026) | 3 solo, 2 joint |
| R13 | Unification: package the difficulty in a cone so progress applies uniformly | 3 | S10 (2009), S14 (2012), S18 (2015) | 3 solo |
| R14 | Applied curiosity about problems in his surroundings | 3 | S16 (2012), S07 (2015), S19 (2019) | 2 solo, 1 joint |
| R15 | Empirical success ran ahead of the theory, and he says so openly (the low-rank story) | 3 | S05 (2019), S02 (2023), S01 (2023) | 3 solo, all about one episode |
| R16 | Scope disclaimers: say what is not claimed | 4 | S14 (2012), S15 (2012), S18 (2015), S30 (2026) | 3 solo, 1 joint |

Single or double statements (not counted as beliefs):
- "Can't hurt to try" (I1, one episode told twice in 2023);
- the auxiliary-variables × cone decision grid (I3: 2021, and as tables in 2023);
- relaxations "between the two extremes" (I5);
- volume as a branching proxy (E4);
- the IP → QP pivot (C4).

---

## 9. Early and late statements on the same topic (dated)

| Topic | Early | Late |
|---|---|---|
| Expensive strong relaxations | 2010: "it can be worthwhile to pay for a computationally expensive, but strong, relaxation" (S08) | 2014: "faster, but weaker" in-between relaxations (S17). 2021: a decision grid; "socp is somewhere in the middle" (S04 [10:19]) |
| Black-box solvers | 2009/2012: "at this point in time, specialized solvers perform better than black-box ones. Perhaps this will change" (S13) | 2023: "high-quality global-optimization algorithms and software packages available today" (S24 v1). 2026: Gurobi is the global comparator (S31) |
| Exact arithmetic | 2008: "in practice, concerns of an infinite tree are quite irrelevant due to the inexact nature of floating-point arithmetic" (S09) | 2026: separations "do not depend on an SDP solver's numerical tolerance"; exact rational certificates (S29, S30, S27 v3) |
| The low-rank work | 2000: "it looks promising" (e-mail, S02) | 2019: "Despite being "dumb,"…limited theory" (S05). 2023: "we didn't really mean it but this was part of what people started to call benign non-convexity" (S01 ≈32) |
| Reproducibility | 2015: relative paths, as a rule for sharing class projects (S06) | 2026: "reproduces every computational claim", three levels of reproducibility (S29, S31), AI-assisted |
| Where MINLP should go | 2012: "an increasing place for heuristics and approximation algorithms" (S15) | 2021–2023: convex hulls of substructures, "a single strong bound" (S04, S24) |

---

## Contradictions (kept, not reconciled)

1. **Strength against cost of relaxations.**
   - 2010, joint (with Vandenbussche): pay for the strong, expensive relaxation (S08, p. 569).
   - 2009/2012, joint (with Saxena): "Such LP relaxations are extremely desirable for branch-and-bound algorithms" because they warm-start and inherit MILP techniques. Interior-point methods "lack efficient re-optimization capabilities making them bottlenecks in a branch-and-bound procedure" (S13, preprint pp. 29–30).
   - 2014, joint: in-between relaxations that are "faster, but weaker" (S17).
   - 2021, solo: a neutral grid, "some people … love solving lp relaxations for very good reasons" (S04 [10:19]).
   - Which co-author held which view is unknown.
2. **Specialized against black-box solvers.** 2009/2012: specialized solvers win "at this point in time" (S13). 2023–2026: general global solvers are the stated alternative and the comparator (S24, S31). Both are recorded with dates.
3. **Ball constraints, m = 2.** v1 (2 Mar 2023): "we will show by experimentation that our construction is not exact for m = 2". June 2023 slides and v2 (28 Oct 2023): exact for m = 2 (S24, S03). The construction probably changed ([inferred], J5).
4. **The submodular claim, four public statements in 17 months.** v1 (Apr 2025): "solvable in polynomial time". v2 (5 Apr 2026): tight for n ≤ 3, "empirically tight for larger n". Cornell abstract (talk of 7 Apr 2026): "we conjecture that the relaxation is exact for all n". v3 (31 Aug 2026): "not tight in general" (S27, S38).
5. **Burer–Ye.** 2020: Theorem 3 for general instances. 2021: "it only applies to diagonal instances". The published title keeps "(Random and Non-Random)" (S20; Crossref title of the correction, S41).
6. **Field advocacy against his own agenda.** 2012 (joint): heuristics and approximation algorithms deserve "an increasing place" (S15). His own stated aims from 2009 to 2023: strong relaxations, "a single strong bound", explicitly "not specifically concerned with the global optimization" (S13, S24). This is a tension, not a self-contradiction on one claim.
7. **Self-description, 2026.** The CV (12 Feb 2026) lists interests starting "Analytics, operations research, management sciences". The homepage bio (20 Mar 2026, in a commit co-authored with Claude Sonnet 4.6) says he "has spent his career working on mathematical optimization" (S35).
8. **Exact arithmetic.** 2008: floating-point concerns are "quite irrelevant" in practice for finiteness (S09). 2026: results certified in exact rational arithmetic so they do not depend on solver tolerance (S29, S30). The two address different questions (finite termination against certificates), but the emphasis changed.
9. **Disjunction as tool or as deliverable.** 2021: he prefers a non-disjunctive route that "hopefully gives us a little more insight". In the same talk the proof "actually started with the disjunctive formulation" (S04 [30:26], [37:35]).
10. **Source-version discrepancy (for the synthesizer).** 06-trajectory quotes the survey abstract as "global optimisation problem". The published PDF I read (S15, p. 97) reads "global optimization problem". Probably different versions; not resolved.

---

## Gaps

- **No methodology essay, advice column or interview found.**
  - Two WebSearch queries returned only profile and news pages. The Tippie faculty profile loads no text without JavaScript.
  - A podcast page, "Optimizing You" (buzzsprout 1890697: "Through interviewing professors and practitioners in fields like Operations Research…"), came up in a search for his name. Its RSS feed had 0 episodes on 2026-10-10, and the Apple Podcasts directory had no match. **Whether he appeared is unverified.**
- **How he supervises.** No statement found. The 2023 "Advisor-Advisee Relationship" slides are about his own advisor. Student accounts are agent 04's.
- ***Operations Research* area-editor statement (2020–).** pubsonline.informs.org returned HTTP 403 to curl and WebFetch. The Wayback Machine returned 429, then "Temporarily Offline". **Not read.** This is the most likely written statement of his taste as an editor.
- ***Optima* co-editor notes (2010–18).** The MOS API lists only issues 99–108. I read the notes in issues 99 and 104 (joint, generic). Earlier issues were not located. **Not read.**
- **Recorded talks.** I found no recording or slides for these talks:
  - the 2015 ISMP semi-plenary (gentle introduction);
  - the 2022 MIT talk "Vignettes on Copositive Optimization";
  - the 2007 talk series "Representing NP-Hard Problems as Convex Programs";
  - the 2009 Rome short course;
  - the 2007 CMU seminar on SDP;
  - the June 2026 SIAM OP26 talk.
  For the SIAM OP23 prize lecture (2 June 2023), only the slides exist. The transcript is of the March 2023 Iowa rehearsal.
- **Other texts not read.**
  - PEARC 2019 refereed tutorial "Python or R or Both: Tools for Your Data Analytics Workflow": no record in Crossref.
  - Dissertation (2001) preface and acknowledgements: not read (the Georgia Tech PDF returned HTTP 401 to agent 06; I did not retry).
  - SIAM Test of Time and INFORMS Computing Society award remarks: none found. The Tippie, Iowa Now and Georgia Tech items carry no quotes from him (S40).
- **Rejections and referee reports.** None are public. No stated account of a rejected paper was found.
- **Why he left lines of work** (low-rank algorithms, global QP codes, robust optimization). No stated reason found, here or in 06-trajectory.
- **AI-assisted text.** For S29, S31 and S32, and the 2026 homepage, I cannot separate his wording from the tool's. These items are weighted below his talks and sole-authored papers.
- **Coverage of papers.** For 22 papers, preprints and notes (S08–S28, S48), I read the introductions, conclusions and acknowledgements, and keyword-searched the full texts. I did not read their full bodies. Statements in the middle sections may be missed.

---

## Sources

Primary = his own words: talks, slides, sole or joint papers, code documentation he committed, records of his grants. Secondary = third parties and metadata services.

**His talks, slides and teaching**
1. S01. S. Burer, "Two Decades of Low-Rank Optimization", University of Iowa, March 2023. YouTube https://www.youtube.com/watch?v=wSauUgRIQDg (channel "Sam Burer", uploaded 2023-09-09). Auto-caption transcript `references/sources/talks/2023-two-decades-of-low-rank-optimization_youtube-wSauUgRIQDg_auto-captions.txt`. Primary (machine transcript).
2. S02. S. Burer and R.D.C. Monteiro, "Two Decades of Low-Rank Optimization", slides, SIAM Conference on Optimization, Seattle, 2 June 2023 (63 slides, 86 PDF pages; slides 31–34 show the e-mails of 22 May 2000). https://github.com/sburer/2023-06_SIOPT (test-of-time.pdf). The title slide lists both names. Burer gave the talk, and the slide footers carry only his name, so I tag its statements [stated]. Primary.
3. S03. S. Burer, "On Nonconvex Quadratic Programming with Ball Constraints" ("Kurt-Fest!"), slides, Seattle, 2 June 2023 (27 slides). Same repository (kurt-fest.pdf). Primary.
4. S04. S. Burer, "Convexification for Non-Convex Mixed-Integer Quadratic Programming", plenary, INFORMS Optimization Society Conference (virtual), 31 March 2021. YouTube https://www.youtube.com/watch?v=QfZLtPz5JBY (channel INFORMS). Transcript `references/sources/talks/2021-03-31-ios-plenary-convexification-nonconvex-miqp_youtube-QfZLtPz5JBY_auto-captions.txt`. Primary (machine transcript).
5. S05. S. Burer, "An Introduction to Semidefinite Programming for Combinatorial Optimization", IPCO 2019 summer-school tutorial, 20–21 May 2019, slides lecture-1.pdf, lecture-2.pdf and README. https://github.com/sburer/ipco-2019-sdp-tutorial. Primary.
6. S06. S. Burer, teaching videos, all uploaded 2015-02-08: "Relative Paths and the Working Directory in R" (fe6GA200dks), "Sharing RStudio Projects" (mV9vd5urqdU), "The Basics of Projects in RStudio" (hKoSJGWnFFA; transcript saved in this run). Transcripts in `references/sources/talks/`. Primary (machine transcripts).
7. S07. S. Burer, seven blog posts, 2015-05-10 to 2016-05-11, `_posts/` of https://github.com/sburer/sburer.github.io. Primary.

**His papers** (DOIs checked in Crossref; arXiv versions checked in the arXiv API)

8. S08. "COAP 2009 best paper award", *Computational Optimization and Applications* 47:567–570, 2010. DOI 10.1007/s10589-010-9368-9. A third-person account of Burer and Vandenbussche's 2002–2007 work. No author in Crossref; awardee authorship is [inferred]. The awarded paper is *COAP* 43:181–195, DOI 10.1007/s10589-007-9137-6. Primary (joint).
9. S09. S. Burer and D. Vandenbussche, "A finite branch-and-bound algorithm for nonconvex quadratic programming via semidefinite relaxations", *Math. Program.* 113:259–282, 2008. DOI 10.1007/s10107-006-0080-6. Primary.
10. S10. S. Burer, "On the copositive representation of binary and continuous nonconvex quadratic programs", *Math. Program.* 120:479–495, 2009. DOI 10.1007/s10107-008-0223-z. Primary.
11. S11. S. Burer, "Optimizing a polyhedral-semidefinite relaxation of completely positive programs", *Math. Program. Comput.* 2:1–19, 2010. DOI 10.1007/s12532-010-0010-8. Primary.
12. S12. S. Burer and J. Chen, "Relaxing the optimality conditions of box QP", *COAP* 48:653–673, 2011. DOI 10.1007/s10589-009-9273-2. Primary.
13. S13. S. Burer and A. Saxena, "The MILP Road to MIQCP", in *Mixed Integer Nonlinear Programming*, IMA Vol. 154, pp. 373–405, 2012. DOI 10.1007/978-1-4614-1927-3_13. Read from the preprint in the homepage archive (papers/030-miqcpsurvey.pdf). Primary.
14. S14. S. Burer, "Copositive Programming", in *Handbook on Semidefinite, Conic and Polynomial Optimization*, pp. 201–218, 2012. DOI 10.1007/978-1-4614-0769-0_8. Primary.
15. S15. S. Burer and A.N. Letchford, "Non-convex mixed-integer nonlinear programming: A survey", *Surveys in Operations Research and Management Science* 17(2):97–106, 2012. DOI 10.1016/j.sorms.2012.08.001. Primary.
16. S16. S. Burer, "Robust Rankings for College Football", *J. Quantitative Analysis in Sports* 8(2), 2012. DOI 10.1515/1559-0410.1405. Primary.
17. S17. S. Burer, S. Kim and M. Kojima, "Faster, but weaker, relaxations for quadratically constrained quadratic programs", *COAP* 59:27–45, 2014. DOI 10.1007/s10589-013-9618-8. Primary.
18. S18. S. Burer, "A gentle, geometric introduction to copositive optimization", *Math. Program.* 151(1):89–116, 2015. DOI 10.1007/s10107-015-0888-z. Read from the preprint of 25 Sep 2014, revised 17 Jan 2015 (homepage papers/046-ismp2015.pdf); not compared with the published version. Primary.
19. S19. S. Burer and V. Piccialli, "Three methods for robust grading", *EJOR* 272(1):364–371, 2019. DOI 10.1016/j.ejor.2018.06.019. Primary.
20. S20. S. Burer and Y. Ye, "Exact semidefinite formulations for a class of (random and non-random) nonconvex quadratic programs", *Math. Program.* 181:1–17, 2020, DOI 10.1007/s10107-019-01367-2. Correction in *Math. Program.* 190:845–848, 2021, DOI 10.1007/s10107-021-01684-5. Read from the author version of the erratum (18 Feb 2021) bound with the 2020 paper (homepage papers/053-rank-bounds.pdf). Primary.
21. S21. K.M. Anstreicher and S. Burer, "Quadratic optimization with switching variables: the convex hull for n = 2", *Math. Program.* 188:421–441, 2021. DOI 10.1007/s10107-021-01671-w. Read from the preprint of 9 Feb 2020. Primary.
22. S22. K.M. Anstreicher, S. Burer and K. Park, "Convex hull representations for bounded products of variables", *J. Global Optim.* 80:757–778, 2021. DOI 10.1007/s10898-021-01046-7. Primary.
23. S23. A. Eltved and S. Burer, "Strengthened SDP relaxation for an extended trust region subproblem with an application to optimal power flow", *Math. Program.* 197:281–306, 2023. DOI 10.1007/s10107-021-01737-9. Primary.
24. S24. S. Burer, "A slightly lifted convex relaxation for nonconvex quadratic programming with ball constraints", arXiv 2303.01624. v1: 2 Mar 2023; homepage PDF dated 28 Feb 2023, same abstract. v2: 28 Oct 2023. Published in *Math. Program.* 211:157–179, 2025, DOI 10.1007/s10107-024-02076-1. Primary.
25. S25. B. Yang and S. Burer, "Convex Hulls in Quadratic Space", *Encyclopedia of Optimization*, online 31 Oct 2023. DOI 10.1007/978-3-030-54621-2_892-1. Primary.
26. S26. Y. Zhu and S. Burer, "An Extended Validity Domain for Constraint Learning", arXiv 2406.10065 (v1 14 Jun 2024; read from the homepage preprint of that date). Published in *INFORMS J. Computing*, 2026, DOI 10.1287/ijoc.2024.0815. Primary.
27. S27. S. Burer and K. Natarajan (v1, v2), with R. Willemsen (v3), "On the Semidefinite Representability of Continuous Quadratic Submodular Minimization…", arXiv 2504.03996: v1 4 Apr 2025 (full text), v2 5 Apr 2026 (abstract), v3 31 Aug 2026 (full text). Primary.
28. S28. S. Burer and K. Anstreicher, "Applications of the Lorentz positive cone in nonconvex quadratic optimization", arXiv 2609.32017v1, 25 Sep 2026 (full text). Primary.
29. S48. J. Chen and S. Burer, "Globally solving nonconvex quadratic programming problems via completely positive programming", *Math. Program. Comput.* 4:33–52, 2012. DOI 10.1007/s12532-011-0033-9 (cited for one sentence, p. 38). Primary.

**His code documentation, sites and records**

30. S29. sburer/submodular-tests:
    - README.md: rewritten 24 Aug 2026 in three commits with "Co-Authored-By: Claude Opus 5" trailers; edited 26 Aug 2026 without a trailer.
    - .github/copilot-instructions.md: committed 12 Dec 2025.
    - https://github.com/sburer/submodular-tests. Primary (AI-assisted).
31. S30. sburer/ballconstraints, README.md and data/README.md. The README's last commit is 28 Aug 2026, "Add exact projection counterexample certificates", with no trailer. https://github.com/sburer/ballconstraints. Primary.
32. S31. sburer/lorentz-positive:
    - README.md: initial import 15 Sep 2026 with a Claude Opus 5 trailer; "Rewrite README for external readers" 22 Sep 2026 without a trailer.
    - outputs/README.md.
    - https://github.com/sburer/lorentz-positive. Primary (AI-assisted).
33. S32. sburer/sdplr, README.md and CLAUDE.md: four commits on 23 Mar 2026, all with "Co-Authored-By: Claude Sonnet 4.6". https://github.com/sburer/sdplr. Primary (AI-assisted).
34. S33. Other READMEs:
    - soctrust (accompanies *SIOPT* 23:432–451, 2013, DOI 10.1137/110826862), ttrs, ttrsn2, grades;
    - sburer.github.io README;
    - business-analytics-rankings README and index page (July 2026).
    https://github.com/sburer. Primary.
35. S34. "Thinking Outside the Chat Box" course site, Tippie Leadership Collaborative, co-taught with Alice Wang. Pages: index, modules, context, setup, bring, support, instructors. Site revision 2026.10.10.2; commits of 9–10 Oct 2026 carry no AI trailer. https://sburer.github.io/aicourse/. Primary (joint).
36. S35. Homepage https://sburer.github.io/ ("Last updated 2026-03-20"; redesign commit of 20 Mar 2026 with a Claude Sonnet 4.6 trailer) and CV (18 pp., "updated February 12, 2026"), https://sburer.github.io/files/cv.pdf. Primary.
37. S36. NSF award abstracts, via https://api.nsf.gov/services/v1/awards/:
    - 0545514, "CAREER: Computation, Theory, and Applications for Nonconvex Quadratic and Conic Optimization", 2006–2012;
    - 0203426 (collaborative with 0203113), "Collaborative Research: Theory and Implementation of Semidefinite Programming and Its Application to Combinatorial Optimization", 2002–2006.
    Primary records; authorship of the abstracts [inferred].
38. S37. *Optima* 99 (December 2015), "Note from the Editors", signed Sam Burer, Volker Kaibel and Jeff Linderoth. https://www.mathopt.org/optima/99/optima_99.pdf. Issue 104 (June 2018) was also checked. Primary (joint).
39. S38. Cornell ORIE Colloquium, "Sam Burer (Iowa)", 7 April 2026: talk abstract and bio. https://www.duffield.cornell.edu/events/orie-colloquium-sam-burer-iowa/. A speaker-supplied abstract is [inferred]. Primary text on a secondary host.

**Secondary**

40. S39. T. Snee, "Data mining for better farming", Iowa Now, 31 March 2016, with quotes attributed to him. https://now.uiowa.edu/news/2016/03/data-mining-better-farming. Secondary.
41. S40. Award news with no quotes from him, used for context only:
    - Tippie, "Burer honored for long-term impact of paper", 31 Jan 2023;
    - Tippie node 2801 and Iowa Now, ICS prize, Aug 2020;
    - Georgia Tech ARC news, 18 Feb 2023.
    Secondary.
42. S41. Crossref REST API records for 27 DOIs (25 cited above), fetched 2026-10-10 with a mailto of nuwa-skill@users.noreply.github.com. Secondary metadata.
43. S42. arXiv API records for 2303.01624 v1/v2, 2504.03996 v1/v2/v3, 2609.32017v1, 2406.10065v2 and 2512.24295v2 (the CPAIOR 2026 preprint; checked, not quoted). Secondary metadata.
44. S43. Optimization Online author archive "Samuel Burer" (title "Old Wine in a New Bottle: The MILP Road to MIQCP"). https://optimization-online.org/author/samuel-burer/. Secondary.
45. S44. YouTube channel RSS feed (channel UCqyILklLZXC-KnlCJVsp2GA: 15 videos, 2013–2023), a YouTube search page, and oEmbed records for the five videos. Secondary metadata.
46. S45. GitHub REST API: repository list (20 repositories), file trees and commit logs with co-author trailers. Secondary metadata for primary files.
47. S46. WebSearch result lists for 2 queries, 2026-10-10. Leads: a buzzsprout podcast page (unverified), Tippie pages, and the Cornell page (used as S38). Secondary.
48. S47. `references/research/06-trajectory.md` (sibling note, this run). Used only as a map of sources; nothing cited from it unchecked. Secondary.

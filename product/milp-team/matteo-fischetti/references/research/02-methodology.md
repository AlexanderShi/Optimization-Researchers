# Matteo Fischetti · 02 Stated methodology (what he says research should be)

| Field | Value |
|---|---|
| Researcher | Matteo Fischetti, born 1958, Full Professor of Operations Research at DEI, University of Padova since 1997 (homepage). Living. Not Martina Fischetti, his co-author on wind-farm, matheuristics, social-distancing and 2026 EndoWake work: her words are not counted as his. |
| Dimension | Research agent 02 of 06: stated methodology. These are his claims about how optimization research should be chosen, done, tested, judged and written, sorted into the seven layers of `references/research-extraction-framework.md` §一. Whether he practises them is agent 03's job. |
| Research date | 2026-11-08 |
| Sources consulted | 72 sources, listed under Sources: 71 primary (36 talk-deck entries covering 46 decks, 5 course documents, his homepage and CV, 28 papers and preprints) and 1 secondary. Of the 74 PDF decks in his slides directory, 73 were text-extracted and keyword-scanned (a 1990 deck on Steiner arborescences did not download); the 46 cited ones are those that carry method statements. WebSearch: 2 of 5 calls used. Everything else came from curl on his homepage, the arXiv API, Crossref, Unpaywall, the GitHub API, pdftotext, and yt-dlp listings of YouTube (no talk of his found). |
| Local corpus | `references/sources/{papers,talks,essays,software}` hold only `.gitkeep` placeholders, so there was no user-supplied material. `private/` was not opened. |
| Saved this run | Nothing under `../sources/talks/`: no recorded talk with subtitles was found (Gaps G2). Downloaded PDFs and their extracted text stay in the scratch folder. |

## Reading guide

**Tags.**

| Tag | Meaning |
|---|---|
| [stated] | Fischetti said or wrote it: a talk deck he presented (even when the deck says "based on joint work with ..."), a solo-authored text, or his homepage. |
| [stated, co-authored] | A co-authored paper: the authors' joint position, not attributable to him alone. |
| [stated, teaching] | His course pages and course documents at Padova. |
| [stated, 2026, AI-assisted] | A 2026 text whose authors declare that AI assistants drafted or edited text and code (see the voice warning below). |
| [practice] | Something he did, mentioned only as context. Agent 03 owns the check. |
| [observed] | Someone else's statement about him or his work. |
| [inferred] | My reading. |

"Primary" means his own text or deck, co-authored ones included. "Secondary" means other people's accounts.

**Voice and extraction warnings.**

- No interview, essay, award-lecture text or talk transcript was found (Gaps G1, G2). The spoken voice survives only as slide text, so every [stated] quote below is a slide bullet or a sentence of a paper.
- Slide text comes from `pdftotext` and is quoted verbatim, his typos and hashtags included (no [sic] added). Symbols that did not survive extraction, mostly arrows, appear as [→]; the symbol is my reading.
- Decks are cited by PDF page ("PDF p."), which can differ from the printed slide number when a deck contains animation builds. Author preprints from his papers directory are cited by preprint page; published versions by printed page.
- 2026 materials: the three EndoWake preprints (arXiv:2609.40157, 2610.07844, 2610.39503) and the feasibility-pump manuscript of 2026 each carry a declaration that Claude (Anthropic) and ChatGPT or Codex (OpenAI) were used for code, adversarial review and text editing. The 2026 backprop deck ends "made with Claude" with a synthetic voice, and the 2026 GitHub commits are co-authored by Claude. Their phrasing is weighed lower as evidence of his own words; the positions are his, since he takes responsibility in the declarations. arXiv:2609.13922 (solo, 2026) carries no such declaration in its arXiv text; whether one exists elsewhere was not checked.
- The Harold Larnder plenary (CORS/INFORMS 2015) is identified with the Occam's-razor deck by venue and date only: the homepage lists the plenary at that meeting and the directory holds one CORS 2015 deck [inferred].

**Source keys** (full entries under Sources). Decks: LB02, ZH03, FP04, EVO05, IPCO05, VV06, MIA06, UTR08, ISMP09, BER09, LAG10, CPA10, MIP10, NEW11, EURO12, AIRO12, EURO13, ISCO14, IFORS14, RAMP14, MIP15, CORS15, ISMP15, VIE15, BCN15, AUS16, TRI16, BEN17, BIL17, DL18, ISMP18, BAL19, INF20, VRL25, AIY26, BP26. Teaching: PP17, MET19, RO2-20, OR2-22, CK23. Homepage and CV: HP, CV13. Papers: LB03, FP05, JMI09, FP209, NCF12, QAP12, BDB13, ERR14, PRX14, SS14, RS16, SVM16, CFL16, MATH16, UFL17, STE17, ORB17, TRR17, BF17, DNN18, MBP18, BIL20, MBP26, EW26a, EW26b, EW26c, FPC26, NSR05. Secondary: COAP17.

---

## 0. Claims repeated three or more times (the real beliefs)

| # | Claim (faithful paraphrase) | Count | Where and when | Voice |
|---|---|---|---|---|
| R1 | Prefer the simpler model and algorithm (Occam's razor); hardness often comes from over-modelling, so thin the model out instead of adding machinery; simple does not mean trivial. | ≥10 | LB03 p.39 (2003); FP05 p.1 (2005); QAP12 p.7 (2011); STE17 p.1 (2014 preprint); CORS15 PDF pp.2, 9, 13, 29 (2015); MIP15 PDF p.15 (2015); VIE15 PDF pp.5–7 (2015); CFL16 p.1 (2016); UFL17 p.2 (2016); TRI16 PDF pp.9–11 (2016) | solo decks + co-authored papers |
| R2 | Use the general-purpose MIP solver as a black-box building block ("MIPping"); do not quit the MIP framework for ad-hoc heuristics, and do not duplicate what the solver already does. | ≥11 | LB02 PDF p.3 (2002); LB03 p.24 (2003); EVO05 PDF pp.2–3 (2005); VV06 PDF pp.2–6 (2006); JMI09 p.1 (2009); BDB13 p.1 (2011 preprint); STE17 (2014); MATH16 p.2 (2016); TRI16 PDF pp.11, 13 (2016); BF17 p.10 (2016 preprint); TRR17 (2017) | solo decks + co-authored |
| R3 | Performance variability (erraticism) is intrinsic to tree search: design experiments around it, and exploit it. | ≥8 | EURO12 PDF pp.14, 24 (2012); ERR14 p.1 (2012 preprint); ISCO14 PDF pp.8, 11–12, 15 (2014); IFORS14 PDF p.18 (2014); RS16 abstract (2013 preprint); TRI16 PDF p.7 (2016); BIL20 p.16 (2019 preprint); RO2-20 (2020) | solo decks + co-authored + teaching |
| R4 | Comparisons must be fair: difficulty classes defined symmetrically over both methods, no dropping of instances easy for the competitor, no testing on the training set, extras stripped so the core idea is compared, the baseline tuned as carefully as the method. | ≥9 | EURO12 PDF p.23 (2012); NCF12 p.6 (2011 preprint); BDB13 p.7 (2011 preprint); ERR14 pp.6–7 (2013 rev.); RS16 pp.11, 13 (2015 rev.); AUS16 PDF p.18 (2016); BIL20 p.14 (2019); MBP26 p.2 (2026); EW26c p.1 (2026) | solo decks + co-authored + 2026 |
| R5 | The more parameters or degrees of freedom, the more overtuning or overfitting: keep tuning conservative and models lean. | 8 | AIRO12 PDF p.3 (2012); EURO12 PDF p.23 (2012); ISCO14 PDF pp.19, 24 (2014); PRX14 p.23 (2013 preprint); CORS15 PDF p.3 (2015); SVM16 p.3 (2015 preprint); TRI16 PDF p.9 (2016); DNN18 p.6 (2018) | solo decks + co-authored |
| R6 | An algorithm is not finished until it is implemented and tested; an untested claim is a "computational conjecture", and he frames his own hypotheses that way. | ≥7 | ISCO14 PDF pp.15, 24 (2014); ISMP15 PDF p.12 (2015); ISMP18 PDF pp.3–6 (2018); MBP18 p.1 (2018); VRL25 PDF pp.3–6 (2025); AIY26 PDF p.2 (2026, a variant) | solo decks + co-authored preprint |
| R7 | When a component (Gomory cuts, Benders cuts) is blamed for slow convergence, look at the loop that uses it: Kelley's cut loop is unstable, the root node is where implementations sink, stabilize the loop. | ≥8 | LAG10 PDF p.9 (2010); CPA10 PDF p.21 (2010); MIP10 PDF p.12 (2010); MIP15 PDF pp.5, 15 (2015); CORS15 PDF pp.25–26 (2015); VIE15 PDF pp.17–18 (2015); VRL25 PDF pp.9–12 (2025); AIY26 PDF pp.17–19 (2026) | solo decks |
| R8 | Question the received view and investigate the opposite one: erraticism as an opportunity, symmetry as a feature, simpler models instead of stronger polyhedra, no trust in the single fractional point. | 5 | NEW11 PDF p.4 (2011); ERR14 p.1 (2012); ISCO14 PDF pp.18–19 (2014); STE17 p.1 (2014); ORB17 p.1 (2014 preprint) | solo decks + co-authored |
| R9 | Borrow ideas across fields: metaheuristics into cut generation, ML overfitting into branch-and-cut, CP propagation into the feasibility pump, SAT/AI restarts into MIP, telecommunications into SVM training, wind-farm models into social distancing. | ≥7 | EVO05 PDF p.11 (2005); FP04 PDF p.53 (2004); FP209 conclusions (2009); CPA10 PDF pp.22–24 (2010); ERR14 pp.1, 10 (2012); ISCO14 PDF p.19 (2014); SVM16 p.2 (2015); INF20 PDF p.23 (2020) | solo decks + co-authored |
| R10 | Benders decomposition is well known but under-used, because its implementation scares people; inside a modern branch-and-cut it is a callback and easy. | ≥11 | MIP15 PDF p.2; CORS15 PDF p.17; VIE15 PDF p.11; BCN15 PDF p.2 (all 2015); BEN17, four decks (2017); VRL25 PDF pp.2, 11 (2025); AIY26 PDF pp.8, 13–14, 19 (2026) | solo decks |
| R11 | Check cheaply whether an approach has potential before engineering it, and present results as a proof of concept. | ≥8 | IPCO05 PDF pp.18–19 (2005); EVO05, VV06 PDF p.25 (2005–06); NCF12 p.1 (2011); EURO13 PDF p.24 (2013); RAMP14 (2014); PRX14 abstract (2013); ERR14 p.1 (2012); SS14 p.7 (2014) | solo decks + co-authored |
| R12 | Look inside the dynamics and ask why a method works or fails (trajectories, determinants, sources of variability). | 4 | ISMP09 PDF p.21 (2009); CPA10 PDF p.11 (2010); ISCO14 PDF p.16 (2014); IFORS14 PDF p.18 (2014) | solo decks |
| R13 | Revisit old methods with today's technology (1960s Benders, Gomory cuts, 1971 intersection cuts, his own 1992 codes, his own 2005 and 2018 ideas). | ≥7 | MIP10 (2010, "Gomory Reloaded"); CFL16 p.3 (2016); UFL17 p.2 (2016); TRI16 PDF p.11 (2016); VRL25 PDF p.2 (2025); MBP26 p.27 (2026); FPC26 p.19 (2026) | solo decks + co-authored + 2026 |
| R14 | The primal side matters: an incumbent found early beats optimality found late. | 4 | LB03 p.24 (2003); FP04 PDF p.7 (2004); PRX14 abstract (2013); EURO13 PDF p.24 (2013) | solo decks + co-authored |
| R15 | Ideas should end up inside general-purpose solvers; that is where they have impact. | ≥5 | EURO13 PDF p.24 (2013); PRX14 p.23 (2013); ISCO14 PDF p.12 (2014); BEN17 Porquerolles PDF p.7 (2017); VRL25 part 3 PDF p.14 (2025); AIY26 PDF p.19 (2026). Related: ISMP18 PDF p.3 (2018), implementation as the route to "impact in practical applications" | solo decks + co-authored |
| R16 | Publication norms reward complication and omit implementation, so simple ideas look unpublishable. | 4 | CORS15 PDF p.16 (2015); TRI16 PDF pp.8, 12 (2016); ISMP18 PDF pp.4–5 (2018); VRL25 PDF p.3 (2025) | solo decks |
| R17 | Close a study with explicit "lessons learned". | ≥12 | IPCO05; MIA06; ISMP09; BER09; LAG10; QAP12; TRI16; TRR17; INF20; MBP18; MBP26; FPC26 (2005–2026) | solo decks + co-authored + 2026 |
| R18 | Teaching: implement in C on CPLEX callbacks, check and plot every solution, compare algorithms with performance profiles over several random seeds. | 4 | PP17 (2017); RO2-20 (2020); OR2-22 (2022); CK23 (2023) | teaching |

---

## 1. Research taste (what is worth doing, what is a good result)

**1.1 Simplicity first (R1).** [stated, primary]

- CORS/INFORMS 2015 plenary, titled "The simpler the better: Thinning out MIP's by Occam's razor" (CORS15). He quotes Occam's razor and Einstein, then warns: "Not to misinterpreted and used as an excuse to address oversimplified models" (PDF p.2). On over-modelling: "The practical difficulty in solving hard problems sometimes comes for overmodelling: Too many vars.s and constr.s just stifle your model (and the cure is not to complicate it even more!) Let your model breathe!" (PDF p.13).
- The same deck closes on simplification as a method: "I wanted to write a very elaborated and convincing conclusion section ... ... and then I simplified it and then I simplified it and ... This is what remains Be simple (if you can)! #OccamRazor" (PDF p.29).
- EURO plenary, Vienna, September 2015 (VIE15): "Simplicity is one of keys to scalability [→] focus (as much as possible) on simple models and solution schemes" and "Warning: simple does not mean trivial ..." (PDF p.5). His recipe for simpler models: "1. Choosing a model that better fits the instances of interest 2. Removing variables that play a little role for the problem class of interest 3. Using decomposition to break the problem into smaller pieces" (PDF p.7).
- In papers [stated, co-authored]:
  - STE17, 2014 preprint p.1: "In this paper we investigate the opposite viewpoint, and try to make the solution method as simple as possible while working on the modeling side. Our working hypothesis is instead that the extreme hardness of some classes of instances mainly comes from over-modeling, and that some instances can become quite easy to solve when a simpler model is considered."
  - QAP12, preprint p.7: "The lesson learned is that, in some cases, the simpler the formulation, the more likely it will not introduce nasty side effects." The context is symmetry: over-sophisticated formulations can hide symmetry from the solver.
- Simplicity reaches his own engineering too. CORS15 PDF p.26 (repeated at MIP15 and VIE15): "Our very first implementation worked so well that we did not have an incentive to try and improve it #OccamPrinciple".

**1.2 The MIP model is the centre; ad-hoc heuristics are a loss (R2).** [stated, primary]

- Aussois 2002, local-branching talk with Lodi (LB02, PDF p.3). When general-purpose software is not adequate, "one has to:" then two bullets: "Play with the MIP solver parameters ("emphasize integrality" etc.) so as to convince the $#$#?@# solver to deliver, at least, a good solution" and "Design and use ad-hoc heuristics--thus loosing the advantage of working in a generic MIP framework". Next to it: "Most MIPlib instances are of this type!" versus "Many real-world instances are of this type!"
- Plenary, Lausanne 2005 (EVO05, PDF p.2), repeated at Villa Vigoni 2006 (VV06, PDF p.2): "As a matter of fact, too often a MIP model is developed only "to better describe the problem" or, in the best case, to compute bounds for benchmarking the proposed ad-hoc heuristics".
- The matheuristics chapter (MATH16, p.2, with Martina Fischetti) [stated, co-authored] names three routes: insist on the MP approach, abandon it ("In this latter case, the MP model is completely disregarded or just used for illustrating the problem characteristics"), or "A third approach is however possible that consists in using the MP solver as a basic tool within the heuristic framework."

**1.3 Distrust of over-sophistication.** [stated, primary]

- IFORS 2014 (IFORS14, PDF p.18): "Empirical rule: the more sophisticated the code, the smaller the speedup #curseofbeingtoosmart" and "Maybe simpler B&B codes preferable when #millioncores will be available?"
- ISCO 2014 plenary (ISCO14, PDF p.8): "The more sophisticated the code, the more variability is expected!"
- ISMP 2018 keynote (ISMP18, PDF p.9), on user cuts: "being too clever on them can actually slow-down the solver because of the overhead in generating and using them".
- He applies the overfitting vocabulary outside learning too. AIRO12 PDF p.3 [stated, talk with Cacchiani and Caprara]: "Robust optimization avoids risky sol.s that overfit the nominal model".
- On machine learning [stated] (DL18 Pittsburgh, PDF p.9): "Question: does it make sense to look for global optimal solutions using much more sophisticated methods, that are more time consuming and are unlike to generalize equally well?" [stated, co-authored] DNN18 p.6: "due to overfitting, insisting on finding proven optimal solutions is not at all a clever policy for training".

**1.4 Implementation is part of the result (R6).** [stated, primary]

- ISMP 2018 keynote (ISMP18, PDF pp.3–5), repeated at VeRoLog 2025 (VRL25, PDF pp.3–6).
  - "Implementation is not just coding!"
  - "Needed if we #orms want to have an impact in practical applications"
  - "Describing an Algorithm without Implementation is like stating a Theorem without Proof #just_a_computational_conjecture"
- He calls branch-and-cut something that "Comes as an algorithm entangled with its implementation" (ISMP18 PDF p.6; VRL25; AIY26 PDF p.2).

**1.5 What a good result looks like.** [stated, primary]

- A hard open instance falls with a simple device. CORS15 and VIE15 present QAPLIB esc instances "attempted on constellations of thousand computers around the world for many CPU years" that were solved "in minutes on a notebook", and esc128 "in just seconds" (CORS15 PDF p.14).
- A result counts as good when it is simple and when the general-purpose machinery is reused. TRI16 PDF p.12 asks the audience: "How do you feel about this "very simple approach that works"? Excited or disappointed?"
- One single-source taste marker [stated, self-presentation]: his homepage puts the Italian caption "Deve funzionare!" under a thumbs-up photo of himself (HP). In my translation: it has to work.
- Course reading [practice, teaching]: his OR1 and OR2 course folders both carry K. Sörensen's "Metaheuristics—the metaphor exposed" (ITOR 22:3–18, DOI 10.1111/itor.12001), dated 2019-05-24 in the directory listing (MET19). [inferred] This hints at a taste against metaphor-driven metaheuristics; he states nothing about it.

---

## 2. Problem choice (where problems come from, why now, when to stop)

**2.1 Problems arrive from practice and from hard open instances.** [stated, primary]

- TRI16 PDF p.3 describes Alstom's dispatching project: "We have been involved as MIP experts". His framing question: "Can today's MIP technology heuristically solve each of them in 2/5/10 sec.s on a reasonable hardware?"
- INF20 PDF p.23 (IFORS distinguished lecture, INFORMS 2020): "Operations Research can make a big impact for businesses and customers, both in terms of profit and safety" and "Mathematical optimization is instrumental to finding more profitable yet safer configurations".
- [stated, co-authored] QAP12 p.2: "A QAP feature that challenged us is that a collection of (apparently very small) test-cases is available" that had resisted exact methods.
- [practice] The homepage lists consulting for the World Bank, Ferrovie dello Stato and others, and FS-funded projects ALPI, FASTER and FARO (1993–1998), two of which won FS code competitions (HP).

**2.2 First question: can the generic tool do it? (R2).** [stated, primary]

- He keeps asking whether the existing general tool suffices before building anything:
  - "Can we devise an alternative use of a general-purpose MIP solver, e.g., to address important steps in the solution process?" (VV06 PDF p.2)
  - "Can we just use a generic MIP solver?" followed by "Unfortunately not ..." (TRI16 PDF pp.5–6)
  - "Does it work?" (ISMP18 PDF p.16; VRL25)

**2.3 Why now: revisit old ideas with today's tools (R13).** [stated]

- VRL25 PDF p.2 (cuts plus branching): "This idea was around already in the 1980's" and "BUT: how to actually implement it?"
- [stated, co-authored] CFL16 p.3: "Our goal was to provide guidelines for a modern implementation of Benders decomposition based on the MIP technology which was not available back in the 70's and 80's".
- [stated, co-authored] UFL17 p.2: "we believe that our approach is an important step in the right direction, as it shows the viability of "thinning out" classical models with today's knowhow and technology". Also: "So, big data is an incentive for us to revise approaches that work on a projected decision space".
- TRI16 PDF p.11: "MIP technology improved dramatically in the last years [→] just USE it!"
- VIE15 PDF p.21: the "Datazoic era" is "giving us an incentive to design simpler and more scalable solvers". On data size (PDF p.2): "We (OR/Mathematical Optimization people) are already proud if we can solve problems with few MB's of perfectly clean input data... #TooBigForUs?"
- 2026, applied to his own work [stated, 2026, AI-assisted]:
  - FPC26 p.19: "Our recommendation is therefore not a new heuristic but an old one, restored."
  - MBP26 p.27 [stated, 2026]: "We have taken an eight-year-old idea and subjected it to the test that was missing when it was proposed".

**2.4 Research agendas he announces.** [stated, primary]

- ISCO14 PDF p.19: "Research topic: new generation of B&C codes where clouds of fractional solutions are evaluated in a statistically-sound way (bigdata approach?)". PDF p.23 on branching on general disjunctions: "However, not implemented in commercial solvers yet: why?"
- VIE15 PDF p.11 promotes Benders "hoping to convince young researchers to test it... and not to be #TooBoring".

**2.5 When to stop.** No stated rule for abandoning a problem was found (Gaps G7). The nearest statements:

- Stop elaborating once the first simple version works (1.1, #OccamPrinciple).
- Stop at the measured potential before building tools (R11).

---

## 3. Idea generation

**3.1 "MIP it": turn a sub-decision into a MIP and hand it to the solver (R2).** [stated, primary]

- EVO05 PDF p.3 and VV06 PDF p.3: "A neologism: To MIP something = translate into a MIP model and solve through a black-box solver".
- VV06 PDF p.6: "We teach engineers to use MIP models for solving their difficult problems" and "Be smart as an engineer! Model the most critical steps in the design of your own algorithm through MIP models, and solve them (even heuristically) through a general-purpose MIP solver..."
- [stated, co-authored] JMI09 p.1: "So, it makes sense to think of a new generation of MIP solvers where auxiliary MIPs (as opposed to LPs) are heuristically solved on the fly, with the aim of bringing the MIP technology under the chest of the MIP solver itself."
- [stated, co-authored] BF17 preprint p.10, with Balas: "The use of an exact MIP solver inside a MIP heuristic may appear naive at first glance, but it turns out to be effective in the cases where the added invalid constraints lead to a structural simplification of the MIP at hand".
- Extending MILP machinery to new classes is the same move:
  - "HPR is a familiar MILP [→] we can apply our whole MILP bag of tricks!" (AUS16 PDF p.5)
  - "Mixed-Integer Bilevel Linear Programming is a MILP plus additional constr.s" (BIL17; AIY26 PDF p.19)
  - For non-convex MIQP, "start with a MILP solvers (B&C) and customize it" (ISMP18 PDF p.11)
  - On deep networks, "#MIPpersToTheBone" (DL18 Delft PDF p.7)

**3.2 Invert the received view (R8).** [stated]

- NEW11 PDF p.4 on QAP symmetry: "Step 1: don't break my symmetries! ... Usual recipe in discrete optimization: break it! Instead, we propose a new way to exploit it to reduce problem size and complexity".
- [stated, co-authored] ORB17 p.1: "In this paper we argue that symmetry is instead a beneficial feature that we should preserve and exploit as much as possible, breaking it only as a last resort."
- [stated, co-authored] ERR14 p.1: "In this paper we investigate the opposite viewpoint, and consider this behavior as an opportunity to exploit." The same move appears in STE17 p.1 (1.1).
- ISCO14 mocks the "Integer Programming Gospel" ("In the beginning was the Fractional Point", PDF p.2), then argues "Don't trust the fractional point!" (PDF p.18), since "at each B&B node the fractional solution we consider is by no mean THE fractional solution ... but just a random sample among millions alternatives".

**3.3 Transfer by analogy (R9).** [stated]

- CPA10 PDF pp.22–24, on Gomory cuts that stall:
  - "Ok, let's think "laterally" about this cutting plane stuff" (PDF p.22). On the next slide: "This sounds like déjà vu..." (accents lost in extraction), "... we have a simple module that works well in the beginning ... but soon it gets stuck in a corner", "... Where did I hear this?", "Oh yeah! It was about heuristics and metaheuristics... We need a META-SCHEME for cut generation !" (PDF p.23).
  - "we don't give-up but apply a diversification step (isn't this the name, Fred?)"
- ISCO14 PDF p.19 applies machine-learning logic to branching: "Like designing a machine learning tool (say, a Support Vector Machine) with a training set composed by a single point [→] would you trust it?"
- EVO05 PDF p.11: the local-branching neighbourhood is "Akin to k-OPT for TSP".
- [stated, co-authored]
  - FP209 conclusions: "exploit a concept borrowed from Constraint Programming (namely, constraint propagation)".
  - ERR14 p.10 proposes "an improved restart strategy borrowed from the AI/CP community".
- [stated] SVM16 p.2 lists as a main contribution "a new interpretation of SVM's with Gaussian kernels in terms of telecommunication systems".
- [stated] INF20 PDF p.23: "Facility location under social distance constraints and wind farm layout optimization are "similar" problems [→] we can borrow models and algorithms from wind farm literature".

**3.4 Diagnose the mechanism, then fix the loop, not the part (R7, R12).** [stated, primary]

- Asking why:
  - "Ok, it works ... but WHY?" (ISMP09 PDF p.21)
  - "Both versions collapse after a while [→] why?" over plotted LP-solution trajectories (CPA10 PDF p.11)
  - "Where does erraticity come from?" (ISCO14 PDF p.16)
  - "Why speedups change so much?" (IFORS14 PDF p.18)
- Fixing the loop:
  - LAG10 PDF p.9: "Kelley's method is intrinsically nonrobust" and "Kelley + Gomory is problematic in the long run, but ... it is not all Gomory's fault!"
  - CPA10 PDF p.21: "Closed-loop systems are intrinsically prone to instability..."
  - MIP10 PDF p.12: "GMICs are not necessarily bad in the long run".
  - VRL25 PDF p.9: "Slow convergence is generally attributed to the poor quality of Benders cuts, to be cured by a more clever selection policy (Pareto optimality of Magnanti and Wong, 1981, etc.) but there is more..."

**3.5 Quick shots and the blur principle.** [stated]

- CORS15 PDF p.26: "As a quick shot, we implemented a very simple "chase the carrot" heuristic". PDF p.15: "Heuristics based on the blur principle: initially forget about details...".
- [stated, co-authored] QAP12 p.9: "Our first quick shot was to write our MILP model ... and to solve it through a black-box commercial MILP solver".
- ISMP15 PDF p.12 states a hypothesis before testing it, "Our computational conjecture ... Changing the master objective will improve relaxation grip".

---

## 4. Experiments and execution

**4.1 Fair-comparison rules (R4).** [stated, primary]

- EURO12, conclusions (PDF p.23), the most compact statement:
  - "Tests are biased if "we test our method on the training set""
  - "The more parameters, the easier to make overtuning [→] power-of-ten effect"
  - "Removing "instances that are easy for our competitor" is not fair"
  - "When comparing methods A and B, the instance classification must be the same if A and B swap [→] blind wrt the name of the method"
- EURO12 PDF p.5, the rules for a single added cut: "Don't cheat: CPU time needed to generate the cut must be comparable with CPU time to solve the root-node LP".
- The same rules in co-authored papers [stated, co-authored]:
  - ERR14 p.7: "This is a fair policy as the competing methods play an indistinguishable role in the class definition, so no biasing is expected."
  - ERR14 p.6: "For a fair comparison, all codes use a (possibly dummy) callback function, thus deactivating IBM ILOG Cplex's proprietary dynamic search." Runs were single-thread with nothing concurrent on the machine "(this ensures reliability of the reported computing times)".
  - BDB13 p.7: "Our testbed was constructed to contain "not too easy nor hopeless" instances, selected according to the following procedure intended to reduce biasing in favor of one of two codes under comparison."
  - RS16 p.13: "To avoid any bias in the analysis, the level of difficulty is defined by taking into account the two solvers that are compared". RS16 p.11 states the dilemma both ways: "this would give an unfair advantage to ksample ... At the same time, removing those instances from the testbed would be unfair as well".
  - NCF12 p.6: "to have a fair comparison of branching rules, in all runs we disabled all further preprocessing, heuristic and cut generation procedures, and provided the solver with the optimal solution value as the upper cutoff".
  - BIL20 p.14 flags a bias against the competitor: "although this introduces a bias in disfavor of SCIP, which solved more problems within the time limit".
- AUS16 PDF p.18 [stated], against MibS: "To me more fair: IC's only [→] no ING cuts, no CPLEX cuts, no heur.s, 1 thread".
- 2026 [stated, 2026]:
  - MBP26 p.2 concedes that "most claimed training speed-ups evaporate once the baseline is tuned with the same care as the method".
  - EW26c p.1 reports "A pre-specified test set of 36 unseen instances".

**4.2 Randomness as an experimental factor (R3).** [stated]

- EURO12 PDF p.14, where he reveals that the single added cut was redundant and its effect came from changed initial conditions: "(Some degree of) erraticism is intrinsic in tree-search nature ... ... you cannot avoid it (important for experiment design) ... and you better try to turn it to your advantage ... though you will never have a complete control of it".
- EURO12 PDF p.22 validates "on 10 copies of each hard instance (random rows&col.s scrambling)".
- ISCO14 PDF p.8 credits the observation: "Common observation (Danna, 2008): even when implemented in a deterministic way, tree search is highly dependent on initial conditions".
- [stated, co-authored] BIL20 p.16: results "confirmed ... by re-running our codes with 5 different random seeds, so as to take performance variability into account".
- [stated, teaching] RO2-20 schedules a lecture "Confronti computazionali (random seed e performance profile)". In my translation: computational comparisons, with random seeds and performance profiles.

**4.3 Build vanilla, then add; strip, then keep what survives.** [stated]

- He reports minimal implementations as a virtue:
  - "Vanilla SelfSplit: just 8 new lines added to the sequential original code" (IFORS14 PDF p.13)
  - "B&C: just few hundred lines (the callback for IC separation) on top of Cplex" (AUS16 PDF p.18)
  - a "Vanilla B&C implementation" with listed omissions (ISMP18 PDF p.15)
- TRI16 PDF pp.9–11 describes ablation by subtraction:
  - "Our final algorithm implemented a bunch of complicated ideas ... so we decided to clean it up ... to make it as simple as possible ... without deteriorating it too much".
  - Three reasons: "A too complicated code is difficult to maintain", "A sophisticated alg. with many parameters is prone to overfitting", and "We wanted to know which are the "ideas that work best" so we could share them with our colleagues working on similar problems #PublishOrPerish".
  - Outcome: "After a lot of tests and hard work, we were able to isolate the two most effective ideas in our code [→] removing all the others does not deteriorate (but actually improves) its overall performance !"
- Start in a friendly setting. VV06 PDF p.29 (CG closure): "We started in a "friendly" setting by addressing 2-matching problems". The Gomory talks use the toy instance stein15 under "In theory, but ... in practice?" (CPA10 PDF p.10).

**4.4 Measure potential before engineering (R11).** [stated]

- VV06 PDF p.25 (also in EVO05): "Before affording the effort of designing and implementing sophisticated separation tools, we want to be sure the overall approach has some potentials..."
- IPCO05 PDF pp.18–19: "But ... is this worth doing? In other words: who knows how tight is this relaxation?", answered on the next slide with "Just ask!" and a table of gap closed.
- [stated, co-authored] SS14 p.7: "our proof of concept implementation shows that the method can be implemented with very limited effort".

**4.5 Don't fight the black box.** [stated]

- TRI16 PDF p.13: "Do not waste your time in duplicating stuff already in the MIP solver". PDF p.11: "No need to implement clever/sophisticated ad-hoc bound propagations or BIGM reductions".
- [stated, co-authored] BDB13 p.1: the black-box solver is run "in its default mode", so that the method does not interfere with the solver's highly optimized internal mechanisms (paraphrase of the abstract).
- [stated, co-authored] CFL16 p.9 prefers a general LP solver for its warm starts: "so after some testing we decided not to use any specialized code--thus making the overall implementation simpler".

**4.6 Teaching the experimental routine (R18).** [stated, teaching]

- The OR2 thesis checklist 2022–23 (CK23) marks as mandatory, among others:
  - "Setting up the C project with TSPLIB parser and solution check & plot"
  - Benders' loop with SEC separation
  - "Branch-and-Cut implementation in CPLEX through callbacks"
  - hard fixing and local branching
- It awards one point each for "Extensive use of performance profile plots for algorithm comparision" and "Writing stile".
- In the 2021–22 lecture list (OR2-22), lesson 5 covers the 2-OPT move and algorithm comparison through performance profiles (paraphrase: the title overlaps a URL in the extracted text). The course's performance-profile tool cites Dolan and Moré (2002) and takes a shift and a time limit as parameters (PP17).

**4.7 2026: pre-registration, A/A controls, scripts for every number.** [stated, 2026, AI-assisted]

- MBP26 p.2: hypotheses, endpoints and stopping rules were registered before the confirmatory runs, "so that the order in which things happened need not be taken on our word". An A/A arm calibrates the noise floor.
- MBP26 p.8 records the registration rule "if D > 0.12 the study is reported as inconclusive, not as a negative result".
- The FPC26 README (GitHub): "Everything the paper reports is produced by a script in this repository from the raw result files shipped here. No number in the paper is typed by hand". FPC26 p.12: "We declared twelve comparisons (the rows of Table 3) before looking at the data", with Holm's correction.

---

## 5. Judging results

**5.1 Aim for positive correlation, not perfection.** [stated]

- EURO12 PDF p.19, on bet-and-run:
  - "The underlying "philosophy" is that a BEST parameter configuration exists somewhere and could be found if we were clever enough" ... "Instead, we do not pretend to find a best-possible tuning of solver's param.s (whatever this means) ... our order of business here is to play with randomness only".
  - "We apply a very quick-and-dirty selection criterion for the run to bet on ... as we know that no criterion can be perfect [→] what we are looking for is just a positive correlation with the a-posteriori best run".
- [stated, co-authored] ERR14 p.2: "Therefore, one has to content him/herself with a criterion that gives a positive correlation between the selected run and those that a posteriori behave better than the average."

**5.2 Claim modestly and state the weaknesses.** [stated]

- ISMP18 PDF p.16 (repeated in VRL25): "Overall, we are as fast as SCIP (but the latter solves more instances within the time limit [→] SCIP qualifies as a more robust solver)" and "evidently, we miss a sound bilinear-specific heuristic (TODO)".
- EURO12 PDF p.24: "Computational results on a large MIP testbed show the potential of this simple approach... though more extensive tests are needed".
- [stated, co-authored]
  - TRR17 p.2: "We want to stress here that we do not claim that our approach beats all the" sophisticated methods in the literature.
  - STE17 p.1: "Even though we do not claim our approach can work well in all cases".
  - PRX14 p.23: "In our experiments, we decided to be very conservative to avoid to overtune our method and to contaminate its outcomes."
- [stated, 2026, AI-assisted] FPC26 p.19: "so that the shallow-target advantage of the completion is a lead and not an established result".

**5.3 Expect sophisticated cuts to disappoint on broad testbeds.** [stated, co-authored]

- BIL20 p.16: "it is a common (somehow frustrating) experience in mixed-integer programming that sophisticated classes of cuts such as ICs and disjunctive cuts are not beneficial when a large and varied testbed is considered".
- IPCO05 PDF p.18 [stated]: "GMI cuts are hard to beat by just using clever subadditive functions".
- BAL19 PDF p.4 [stated], at the Balas memorial symposium, on intersection cuts against branching: "Thus, in principle, one could always generate an IC instead of branching [→] not always advisable because of numerical issues, slow convergence, tailing off, cut saturation, etc. #LikeGomoryCuts". The same bullet, without the hashtag, recurs in AIY26 part 2 PDF p.2 (2026).

**5.4 Surprises he reports, always from simplification.** [stated, co-authored]

- "to our own pleasant surprise we found that simple heuristic preprocessing operations have a dramatic effect in the MILP performance" (TRR17 p.2)
- "To our surprise, qUFL turned out to be much easier than its linear counterpart when our approach is properly implemented." (UFL17 p.3)
- esc128 solved "to our great surprise" in seconds (QAP12)
- "A nice surprise" (EURO12 PDF p.16): the first optimal solution of the MIPLIB 2010 instance buildingenergy, found during variability experiments

**5.5 Lessons learned as the unit of conclusion (R17).** [stated]

- He ends talks and papers with an explicit lesson, often a negative or deflating one:
  - "Lesson learned: in most practical cases the inequalities of rank 1 already give a very tight approximation" (MIA06 PDF p.14)
  - "Separating a vertex is often an over-simplified task, that hides the real difficulty of the problem at hand." (BER09 PDF p.23)
  - "Today's technology does not allow a general-purpose MIP solver to be used as a black-box in real-time rescheduling" (TRI16 PDF p.13)
- [stated, co-authored] TRR17 p.3: "Rather, we want to share with the reader the lesson we learnt from this project--train rescheduling can become much easier once an apparently trivial preprocessing step is applied."

---

## 6. Writing and talks

**6.1 Complaints about paper culture (R16).** [stated, primary]

- CORS15 PDF p.16, on Benders for facility location: "A perfect fit with Benders decomposition, but ... not sexy nowadays as more complicated schemes are preferred #paperability?"
- TRI16:
  - ironic: "VERY GOOD! JUST ADD SOME THEOREMS, WRITE A PAPER, AND SUBMIT IT!" (PDF p.8)
  - on the simple final method: "A typical criticism is that ... these ideas are so simple that "do not deserve to be published" ... meaning that I should not bore you with this talk ... but if insist you can always download our internal draft from ResearchGate" (PDF p.12)
- ISMP18 PDF pp.4–5: "Proof: omitted as of no interest to the typical MP reader." VRL25 PDF p.3: implementation is "often omitted in papers as "of no interest for a typical reader"".

**6.2 Talk style: slogans, hashtags, metaphors, self-mockery.** [practice in decks, primary]

- Hashtag slogans:
  - "#OccamRazor", "#That'sOccamBaby", "#TheCurseOfKelley", "#ChaseTheCarrot", "#BendersToTheBone" (2015 decks)
  - "#curseofbeingtoosmart" (2014)
  - "#just_a_computational_conjecture" (2018, 2025)
- Engineering metaphors:
  - cut saturation as "Kind of driving a car on ice with flat tires" (CPA10 PDF p.13)
  - lexicographic reoptimization: "engineers would say that this adds "anti-slip chains" to Gomory's wheels" (MIP10 PDF p.11)
  - branching as "the pinball effect" (EURO12; ISCO14)
- Self-mockery: "Hmmm, this BLOSSOM stuff is so boring ..." (ZH03 PDF p.2); "... and of course for not sleeping..." (CPA10 PDF p.29).
- Every deck ends with the slides and papers URL.

**6.3 Simplify the text itself.** [stated]

- The CORS15 conclusion slide (1.1) treats repeated simplification of the conclusions as the method.
- [stated, 2026, AI-assisted] The arXiv comment on EW26b v2 (October 2026) reads "formal terms replace the metaphors of v1". This runs against the metaphor-heavy decks (see Contradictions C5).

**6.4 Graded in teaching.** [stated, teaching] CK23 gives a point for "Writing stile".

---

## 7. Research organisation (time, teams, students, long-term agenda)

**7.1 Group and collaborators.** [stated]

- He speaks of a group with its own vocabulary: "This is what we call "Old Benders" within our group still the best option for some problems!" (CORS15 PDF p.20; also MIP15, BCN15).
- Industrial collaboration is presented as hiring MIP expertise. Alstom brought in outside optimization experts and "We have been involved as MIP experts" (TRI16 PDF p.3).
- [practice, context] The 2008 Utrecht deck lists his affiliation as "DEI, University of Padova" and "Double-Click sas, Padova" (UTR08 PDF p.1). A co-authored Interfaces paper states that NS's crew-scheduling system TURNI "was developed by Double-Click sas" (NSR05).

**7.2 Students and young researchers.** [stated]

- Young researchers are a target audience for method transfer:
  - Benders "hoping to convince young researchers to test it" (VIE15 PDF p.11)
  - "Students scared by "Benders implementations" typically refer to 2)", that is, to the cut computation, in all four 2017 Benders decks (BEN17), VRL25 PDF p.2 and AIY26 PDF p.8
  - "This is maybe the reason why Benders cuts are considered "too sophisticated" by students", answered by "But ... you can kindly ask your solver to make all calculations for you!" (AIY26 PDF pp.13–14)
- Course design (4.6): from 2019–20 to 2022–23 the OR2 course builds one TSP code, from parser and plots through metaheuristics, Benders and callback branch-and-cut to matheuristics, with two lessons on "Structure of the thesis and exam's rules" (OR2-22).

**7.3 Code and dissemination.** [stated]

- Slides and papers are posted on his site; every deck ends with the URL.
- For the bilevel solver, code went out as binary only:
  - "Our binary code is available on request (research purposes)" (BIL17 Sorrento PDF p.21)
  - "Binary code available (ask Markus Sinnl for a free license)" (VRL25; AIY26 PDF p.19)
- 2026 [stated, 2026, AI-assisted]: the FP-cutoff study ships full code under MIT with raw SCIP logs on Zenodo (FPC26 README; DOIs 10.5281/zenodo.22810777 and 10.5281/zenodo.22810848).

**7.4 2026: AI assistants as programmers and adversarial reviewers.** [stated, 2026, AI-assisted]

- EW26a p.27: the authors used Claude "as programming assistants for the experimental code, as adversarial readers of the mathematical statements, and to edit the manuscript for language and structure", and obtained "independent adversarial audits" from ChatGPT.
- EW26b p.28: "OpenAI Codex served as an adversarial reviewer of the manuscript." Also: "no claim in this paper rests on a statement the authors have not checked independently".
- EW26c p.23: the tools were used "to review successive drafts as a simulated referee".
- MBP26 p.10, without an AI declaration: the test harness "was subjected to an adversarial review whose brief was to find what would make the numbers wrong without making anything crash".
- [inferred] In 2026 he works largely alone or with Martina Fischetti, with AI assistants in the roles that students and referees used to fill. Agents 04 and 06 should check this.

---

## 8. Failures, abandoned directions, negative results and self-corrections he reports

- **Train rescheduling, 2016.** [stated] The generic solver failed first ("Can we just use a generic MIP solver? ... Unfortunately not ...", TRI16 PDF pp.5–6). His team then "worked hardly on a number of exciting ideas" (PDF p.7):
  - BIGM tightening, bet-and-run branching, heuristic Benders, McCormick reformulation, ad-hoc preprocessing, parallel seeds, local branching, aggressive cuts
  - all but two were removed in the end, because removing them did not hurt (PDF p.11)
- **The 2018 minibatch claim, corrected in 2026.** [stated, 2026] He conceded that the objection to his 2018 preprint was right: "The objection is correct, and it is a methodological one, not a conceptual one: the criticism is not that the idea is wrong but that the 2018 evidence could not tell." (MBP26 p.2). The 2026 verdict: "what minibatch reuse buys is neither speed nor energy but data, and only at large minibatch size" (MBP26 p.1). Compare MBP18 p.1 (Contradictions C1).
- **Negative measurement results, 2026.** [stated, 2026] "We report the negative findings in full: two of the three measurement routes we tried do not support the claim we wanted to make with them." (MBP26 p.10)
- **MIPping separation, 2006.** [stated] "As implemented, the MIPping approach is exceedingly time consuming ..." (MIA06 PDF p.16). The workaround: apply it in a preprocessing phase.
- **Subadditive cuts, 2005.** [stated] "GMI cuts are hard to beat by just using clever subadditive functions" and "Negative role of interpolation" (IPCO05 PDF p.18).
- **Gomory's pure cutting-plane method, 2009.** [stated] It works through an inefficient hidden enumeration, "branching even on integer-valued variables!!" (ISMP09 PDF p.28).
- **Feasibility pump, 2004.** [stated] Anti-cycling rules "borrowed from metaheuristics can be implemented", "Instead, we found extremely effective the idea of introducing some enumeration." (FP04 PDF p.53). A choice of one direction over another.
- **Bilinear solver, 2018.** [stated] Some MINLPLib instances were "removed as root LP was unbounded", with bound tightening and a bilinear heuristic left as "TODO" (ISMP18 PDF p.16).
- **Possible rejections (not confirmed).**
  - EW26b p.28 thanks "the two anonymous reviewers of Applied Energy, whose reports on an earlier submission shaped the controls and the comparisons of Sections 6 and 7"; the outcome of that submission is not stated.
  - The 2018 minibatch preprint was "Submitted to an international conference" (arXiv comment) and in 2026 is still listed under technical reports on his homepage. [inferred] It was never published; a rejection is not documented.
- **Benders before stabilization, 2015.** [stated] "Optimality cuts often a nightmare even after MW improvements" (MIP15 PDF p.5). "Mixed results reported in practice: it can work very well or very bad" (BCN15 PDF p.3).

---

## 9. Era and resource context

| Period | Context stated in the sources | Effect on the method he states |
|---|---|---|
| 1986–2000 (Bologna, then Padova) | FORTRAN codes, which he still runs in 2014 ("an old FORTRAN code of 3000+ lines" from 1992; a 10K-line branch-and-cut from 1997, IFORS14 PDF pp.13–14). FS railway projects and code competitions, 1993–1998 (HP). | No stated-method text from this period was found (Gaps G6). |
| 2002–2009 | ILOG-Cplex 7.0–9.0 used as a closed black box on single PCs (Pentium M 1.6 GHz in VV06). First presentations at the Aussois workshop (LB02, FP04). EU projects CASC and ARRIVAL (CV13). | "MIPping" and black-box heuristics: wrap the commercial solver rather than rewrite it. |
| 2010–2018 | CPLEX 12.x callbacks; single-thread runs on an Intel i5-750; co-authors inside CPLEX R&D (COAP17 lists Bonami at IBM-CPLEX and Salvagnin collaborating with CPLEX R&D). Without solver source code: "a task that would be most successful if a complete access to the source code of the solver was available" (ERR14 p.10). | Fairness rules for callback-based experiments; exploiting seeds and erraticism from outside the solver; contributions reported as entering CPLEX defaults (ISCO14 PDF p.12; BEN17 Porquerolles PDF p.7). |
| 2019–2025 | SCIP 5.0 as comparator; teaching on CPLEX callbacks in C (RO2-20, CK23). | Tutorial voice for students and young researchers (VRL25). |
| 2026 (age 68) | Free Kaggle T4 and Modal L4 GPUs and the Padova HPC: "This has three consequences worth stating, because they shaped the design more than any scientific preference did." (MBP26 p.10). "the campaign advances in sessions of a few hours over several weeks" (MBP26 p.10). SCIP git snapshots and Gurobi 13.0.3 (FPC26 README). Claude and ChatGPT or Codex as co-workers (7.4). | Pre-registration, unseen test sets, replication packages, AI adversarial audits. |

---

## Contradictions (kept, not reconciled)

- **C1. Minibatch persistency, 2018 against 2026.**
  - 2018: "The computational conjecture here is that a large minibatch contains a significant sample of the training set, so one can afford to slightly overfitting it without worsening generalization too much." (MBP18 p.1). The abstract also claims "significantly faster convergence", and: "The lesson learned is that minibatch persistency can be a simple yet effective way to deal with large minibatches." [stated, co-authored]
  - 2026: "what minibatch reuse buys is neither speed nor energy but data, and only at large minibatch size" (MBP26 p.1), and "the 2018 evidence could not tell" (p.2). [stated, 2026]
- **C2. Quick-and-dirty against pre-registered.**
  - 2012–2016: "We apply a very quick-and-dirty selection criterion for the run to bet on" (EURO12 PDF p.19). "Our very first implementation worked so well that we did not have an incentive to try and improve it #OccamPrinciple" (CORS15 PDF p.26). Results presented as proofs of concept (R11).
  - 2026: a pre-registered design with an A/A noise arm, timestamped amendments and "294 passing tests" (MBP26 pp.2, 8, 10), and twelve pre-declared comparisons under Holm's correction (FPC26 p.12).
  - The domains differ (MIP heuristics against ML training and a re-study), and the 2026 texts are AI-assisted.
- **C3. "Theorem" against "Conjecture" for cuts in enumeration.**
  - "Theorem. Using cuts within an enumerative scheme is good." (ISMP18 PDF p.6, July 2018; VRL25 PDF p.6, June 2025)
  - "Conjecture: Using cuts within an enumerative scheme is good." (AIY26 PDF p.2, February 2026)
  - Related tension: BIL20 p.16 says sophisticated cut classes "are not beneficial when a large and varied testbed is considered", and ISMP18 PDF p.15 says the user-cut callback is "not needed (and sometimes detrimental)".
- **C4. The black box is both insufficient and not to be duplicated.**
  - In one deck: "Today's technology does not allow a general-purpose MIP solver to be used as a black-box in real-time rescheduling" and "Do not waste your time in duplicating stuff already in the MIP solver" (TRI16 PDF p.13).
  - Elsewhere: the solver must be "convince[d]" (LB02 PDF p.3), and a better diversification "would be most successful if a complete access to the source code of the solver was available" (ERR14 p.10).
- **C5. Metaphor-heavy decks against formal 2026 prose.** The decks run on metaphors (carrot and donkey, pinball, a car on ice); the 2026 arXiv revision note reads "formal terms replace the metaphors of v1" (EW26b, arXiv comment, October 2026).
- **C6. Code sharing.**
  - 2017–2026 bilevel solver: "Our binary code is available on request (research purposes)" (BIL17), "Binary code available (ask Markus Sinnl for a free license)" (VRL25; AIY26).
  - September 2026: full source under MIT plus raw logs for the FP study (FPC26).
- **C7. Exact optimization for learning.**
  - CORS15 PDF p.10 [stated]: "LOO_1: no optimization at all required (besides by an external bisection method): better than the too sophisticated LOO_MILP!!"
  - DNN18 p.6 [stated, co-authored]: proven optimality "is not at all a clever policy for training".
  - Yet the co-authored COAP 2016 best paper solved ramp-loss SVM training to proven optimality with a MILP solver plus bound tightening. Its editorial-board summary calls this "one of the first references of successful use of sophisticated Discrete Optimization approaches for solving hard Machine Learning problems" (COAP17 p.474) [observed, secondary].
- **C8. Polyhedral strength.**
  - For exact work, "Root node LP bound very critical [→] many ships sank here!" (CORS15 PDF p.26; VIE15 PDF p.18).
  - For heuristics [stated, co-authored]: "models that are weak in polyhedral terms can be preferred to tighter--but computationally much harder--models when heuristic (as opposed to exact) solutions are required" (MATH16 p.3).
  - [inferred] Possibly two regimes rather than a contradiction. Kept as stated.

---

## Gaps (what I could not find or verify)

- **G1. No interview, method essay or award-lecture text.** One WebSearch for interviews found only profile and publication pages. The Harold Larnder (2015) and IFORS distinguished (2020) lectures exist only as decks.
- **G2. No transcript.**
  - A WebSearch for recorded talks found only third-party mirrors of his slides.
  - YouTube searches with yt-dlp ("Matteo Fischetti", and three queries on MIP, Benders and the feasibility pump) found only a homonymous videomaker and talks by others. One was Andrea Lodi's CP 2021 invited talk "Learning in Local Branching", which is not his voice.
  - The "Subject to" interview channel (@Subjectto_, 122 episodes listed on 2026-11-08) has no episode with him. It does have episodes with his co-authors and colleagues Andrea Lodi, Paolo Toth, Juan José Salazar González and Roberto Roberti. Those are possible observed accounts for agent 04; not checked here.
  - His OR2 lectures for 2021–22 are on mediaspace.unipd.it (listed in OR2-22, including two lessons on thesis structure). They play publicly through Kaltura, but lesson 24 ("Structure of the thesis and exam's rules (part 1)", checked with yt-dlp) has no caption track, and no speech-to-text tool is available here. Not transcribed. They are the best unread source on his advice to students.
  - Four 2026 mp4 files in his slides directory were not transcribed. The 2026 backprop deck credits a synthetic voice, so they are likely not his voice.
- **G3. Book prefaces not read.** Neither *Lezioni di Ricerca Operativa* nor *Introduction to Mathematical Optimization* (2019) was read: Amazon returned 503 and the Google Books API 429.
- **G4. Not read:** the 2025 revision "Matheuristics by Examples" (DOI 10.1007/978-3-319-07153-4_14-2; the 2016 version was read) and the Wiley encyclopedia entry "Heuristics in Mixed Integer Programming" (2011, DOI 10.1002/9780470400531.eorms0376).
- **G5. Unread items.**
  - The author preprint `local_branching.pdf` does not extract (Type 3 fonts); the published version posted in his OR2 folder was read instead.
  - The OR2 2022 lecture-note PDFs are image-only and were not read.
  - The course copy of Sörensen's paper could not be downloaded (connection reset); only the directory listing was seen.
- **G6. Nothing stated before 2002.** No stated-method source from the Bologna years (1982–1992) or the 1990s was found. The earliest is LB02.
- **G7. No stated rule for when to abandon a problem, and no stated advice on supervising PhD students** beyond course documents. His theses folder (`ricop/tesi/`) was left to agent 04.
- **G8. ResearchGate not read.** The 2026 FP-cutoff paper's ResearchGate page and the "digital twin of Fermat" report sit behind ResearchGate and were not read. The FP-cutoff manuscript PDF and README in the GitHub repository were read instead. The repository's statements are AI-co-authored per its commit metadata.
- **G9. Not checked:** whether arXiv:2609.13922 has an AI-use declaration outside its arXiv text.

## Notes for agents 03–06

- **03:** check practice against R4 and R11. Did his tables define difficulty classes over both methods? Did testbeds keep instances easy for the competitor? Were "proof-of-concept" results ever followed by full studies? Also check what code was released, by year (C6).
- **04:** the OR2 course (CK23, OR2-22) is the best window into his teaching. His theses folder and the AIROyoung 2026 lectures target young researchers.
- **05:** C1 is a self-correction prompted by an outside critique (the data-echoing objection he quotes in MBP26 p.2). The bilinear B&C was "as fast as SCIP" but less robust (ISMP18).
- **06:** the 2026 turn deserves its own entry: ML training studies, the EndoWake trilogy with Martina Fischetti, the FP re-study, AI assistants, free cloud GPUs.

---

## Sources

All decks are at https://www.dei.unipd.it/~fisch/papers/slides/ (directory listing accessed 2026-11-08); the file name is given. All are primary.

- LB02 — "… or How to enhance the heuristic behaviour of your favourite 0-1 MIP solver" (local branching), M. Fischetti, A. Lodi, Aussois, 6–11 Jan 2002, `Aussois 2002 [local branching].PDF`. Primary.
- ZH03 — "0-1/2 CUTS: A COMPUTATIONAL STUDY", G. Andreello, A. Caprara, M. Fischetti, Aussois 2003, `2003 Aussois [0-12 cuts].pdf`. Primary.
- FP04 — "The feasibility pump", M. Fischetti, F. Glover, A. Lodi, Aussois, Jan 2004, `2004 Aussois [feasibility pump].pdf`. Primary.
- EVO05 — Plenary on hybrid MIP methods, M. Fischetti, EuroGP-EvoCOP 2005, Lausanne, 29 Mar–1 Apr 2005, `2005 Lausanne [plenary on hybrid MIP methods].pdf`. Primary.
- IPCO05 — "Mixed-Integer Cuts from Cyclic Groups", M. Fischetti, C. Saturni, IPCO 2005, Berlin, `2005 Berlin IPCO [cyclic group cuts].pdf`. Primary.
- VV06 — COFIN–Matheon workshop talk, M. Fischetti, Villa Vigoni (Como), May 2006, `2006 Villa Vigoni [Fischetti, I MIP you!].pdf`. Primary.
- MIA06 — "MIP models for MIP separation", M. Fischetti, A. Lodi, Miami, June 2006, `2006 Miami [MIP models for MIP cuts].pdf`. Primary.
- UTR08 — "The crew scheduling problem", M. Fischetti, Utrecht, 29 Aug 2008, `2008 Utrecht [crew scheduling].pdf`. Primary.
- ISMP09 — "Looking inside Gomory" / pure cutting plane methods, M. Fischetti, ISMP 2009, Chicago, Aug 2009, `2009 Pure Cutting Plane Methods [Fischetti ISMP09].pdf`. Primary.
- BER09 — Yoyo search, M. Fischetti, Bertinoro, 30 Nov–2 Dec 2009, `2009 Bertinoro [yoyo search].pdf`. Primary.
- LAG10 — "LaGromory" talk, M. Fischetti, Aussois, 4–8 Jan 2010, `LaGromory.pdf`. Primary.
- CPA10 — "Toward a MIP cut meta-scheme", M. Fischetti, CPAIOR 2010, June 2010, `2010 Toward a MIP-cut metascheme [Fischetti CPAIOR].pdf`. Primary.
- MIP10 — "Gomory Reloaded", M. Fischetti (joint work with D. Salvagnin), MIP 2010, July 2010, `2010 Gomory reloaded [Fischetti MIP2010].pdf`. Primary.
- NEW11 — "1,2,3...QAP!", M. Fischetti (joint with M. Monaci, D. Salvagnin), IPDU Newcastle, July 2011, `2011 Newcastle [123...QAP!].pdf`. Primary.
- EURO12 — "On the role of randomness in exact tree search methods", M. Fischetti (joint with M. Monaci), EURO XXV Vilnius, July 2012 (semiplenary per HP), `2012 EURO [erraticism].pdf`. Primary.
- AIRO12 — "A Lagrangian Heuristic for Robust Train Timetabling", V. Cacchiani, A. Caprara, M. Fischetti, AIRO 2012 (filed "in memoriam Alberto Caprara"), `2012 AIRO [in memoriam Alberto Caprara].pdf`. Primary.
- EURO13 — Proximity search, M. Fischetti, EURO 2013 Rome, July 2013, `2013 EURO Rome [Fischetti - proxy].pdf`. Primary.
- ISCO14 — "BRANCHstorming (brainstorming about tree search)", M. Fischetti, ISCO 2014 Lisbon plenary, March 2014, `2014 ISCO [plenary Fischetti BRANCHstorming].pdf`. Primary.
- IFORS14 — SelfSplit, M. Fischetti, IFORS 2014 Barcelona, July 2014, `2014 IFORS Barcelona [Fischetti - selfsplit].pdf`. Primary.
- RAMP14 — Proximity search, M. Fischetti, RAMP 2014 Tokyo plenary, 17 Oct 2014, `2014 RAMP [Fischetti - proxy].pdf`. Primary.
- MIP15 — "Thinning out facilities: Lagrange, Benders, and (the curse of) Kelley", M. Fischetti (with M. Sinnl, I. Ljubic), MIP 2015 Chicago, June 2015, `2015 MIP [Fischetti - UFL Benders].pdf`. Primary.
- CORS15 — "The simpler the better: Thinning out MIP's by Occam's razor", M. Fischetti, CORS/INFORMS 2015 Montreal, June 2015 (Harold Larnder plenary per HP, [inferred] match), `2015 CORS [Fischetti - Occam Razor].pdf`. Primary.
- ISMP15 — Proximity Benders, M. Fischetti, ISMP 2015 Pittsburgh, July 2015, `2015 ISMP [Fischetti - proxyBenders].pdf`. Primary.
- VIE15 — "Thin Models for Big Data", M. Fischetti, OR 2015 Vienna, EURO plenary, Sept 2015, `2015 OR Vienna [plenary Fischetti].pdf`. Primary.
- BCN15 — "Simplified Benders cuts for Facility Location", M. Fischetti (joint with I. Ljubic, M. Sinnl), Barcelona, Nov 2015, `2015 Barcelona [Fischetti].pdf`. Primary.
- AUS16 — "Intersection Cuts for Bilevel Optimization", M. Fischetti, I. Ljubic, M. Monaci, M. Sinnl, Aussois, Jan 2016, `2016 Aussois [Fischetti - Bilevel].pdf`. Primary.
- TRI16 — Real-time train rescheduling, M. Fischetti, TRISTAN 2016, Aruba, June 2016, `2016 TRISTAN [Fischetti - MILP for train rescheduling].pdf`. Primary.
- BEN17 — Four Benders decks, M. Fischetti, 2017: Lunteren (18 Jan), Cargèse-Porquerolles (Aug), ODS Sorrento (Sept), Montreal (Dec), files `2017 Lunteren/Porquerolles/Sorrento/Montreal [Fischetti on Benders].pdf`. Primary.
- BIL17 — "From Mixed-Integer Linear to Mixed-Integer Bilevel Linear Programming", M. Fischetti, ODS 2017 Sorrento plenary (Sept 2017), and the Lunteren bilevel deck (Jan 2017), files `2017 Sorrento [Fischetti's plenay on Bilevel].pdf`, `2017 Lunteren [Fischetti on Bilevel].pdf`. Primary.
- DL18 — Deep learning and MILP, M. Fischetti, Dagstuhl (Feb 2018, long and short decks), CPAIOR Delft (June 2018, with J. Jo), Pittsburgh (21 Sept 2018), files `2018 Dagstuhl/Delft/Pittsburgh [Fischetti on DL].pdf`. Primary.
- ISMP18 — "#post_modern Branch-and-Cut Implementation", M. Fischetti, ISMP 2018 Bordeaux keynote, 6 July 2018, `2018 ISMP [keynote Fischetti on BandC].pdf`. Primary.
- BAL19 — "Intersection cuts from bilinear disjunctions", M. Fischetti (joint with M. Monaci), Dr. Egon Balas Academic Symposium, Pittsburgh, 28 Oct 2019, `2019 Balas Memorial [Fischetti on IC for bilinear].pdf`. Primary.
- INF20 — Optimal social distancing, M. Fischetti, INFORMS annual meeting, Nov 2020 (IFORS distinguished speaker per HP), `2020 INFORMS [Fischetti on optimal social distancing].pdf`. Primary.
- VRL25 — VeRoLog 2025 Trento, 13 June 2025, parts 1–3 ("Branch-and-Cut is our swiss army knife"; Bilevel; "Branch-and-cut implementation of Benders' decomposition"), M. Fischetti, `2025 Verolog - Fischetti part 1/2/3 [...].pdf`. Primary.
- AIY26 — AIROyoung lectures, Padua, 9 Feb 2026, parts 1 (BC + Benders) and 2 (ICs and bilevel), M. Fischetti, `2026 AIROyoung - Fischetti part 1/2 [...].pdf`. Primary.
- BP26 — "Backpropagation for people suffering from derivative allergy", M. Fischetti, 2026 (credit line "made with Claude", synthetic voice), `2026_backprop_slides.pdf`. Primary, AI-assisted.
- PP17 — Performance-profile tool `read_me.txt` (tool by D. Salvagnin, 2016; file dated 2017-06-09), https://www.dei.unipd.it/~fisch/ricop/OR2/PerfProf/. Primary (course material).
- MET19 — OR1 and OR2 course directory listings showing K. Sörensen, "Metaheuristics—the metaphor exposed", ITOR 22:3–18, DOI 10.1111/itor.12001 (file dated 2019-05-24), https://www.dei.unipd.it/~fisch/ricop/. Primary (listing); the paper itself not read.
- RO2-20 — Programma di massima del corso di RO2 (Prof. Fischetti), a.a. 2019-2020 (course schedule), https://www.dei.unipd.it/~fisch/ricop/OR2/. Primary.
- OR2-22 — "OR2 Videos from 2021-2022 (Prof. Fischetti)" and "OR2 2021-2022" schedule, https://www.dei.unipd.it/~fisch/ricop/OR2_2021_2022/. Primary (videos not watched).
- CK23 — "Check list for the OR2 thesis (2022-2023)", https://www.dei.unipd.it/~fisch/ricop/OR2/Checklist_OR2_thesis.pdf. Primary.
- HP — Homepage of Matteo Fischetti, https://www.dei.unipd.it/~fisch/, accessed 2026-11-08. Primary.
- CV13 — Curriculum vitae of Matteo Fischetti (PDF dated 16 Mar 2013), https://dataweb.unipd.it/persone/sites/default/files/CV_805A8F88747C50B983D2725CDABD8929_IT.pdf. Primary (factual only).
- LB03 — M. Fischetti, A. Lodi, "Local branching", Mathematical Programming 98 (2003) 23–47, DOI 10.1007/s10107-003-0395-5 (published version posted at ~fisch/ricop/OR2/Local_Branching.pdf). Primary.
- FP05 — M. Fischetti, F. Glover, A. Lodi, "The feasibility pump", Mathematical Programming 104 (2005) 91–104, DOI 10.1007/s10107-004-0570-3 (author preprint). Primary.
- JMI09 — M. Fischetti, A. Lodi, D. Salvagnin, "Just MIP it!", in Matheuristics, Annals of Information Systems 10 (2009) 39–70, DOI 10.1007/978-1-4419-1306-7_2 (author preprint). Primary.
- FP209 — M. Fischetti, D. Salvagnin, "Feasibility pump 2.0", Mathematical Programming Computation 1 (2009) 201–222, DOI 10.1007/s12532-009-0007-3 (author preprint). Primary.
- NCF12 — M. Fischetti, M. Monaci, "Branching on nonchimerical fractionalities", Operations Research Letters 40 (2012) 159–164, DOI 10.1016/j.orl.2012.01.008 (preprint). Primary.
- QAP12 — M. Fischetti, M. Monaci, D. Salvagnin, "Three ideas for the quadratic assignment problem", Operations Research 60 (2012) 954–964, DOI 10.1287/opre.1120.1073 (preprint). Primary.
- BDB13 — M. Fischetti, M. Monaci, "Backdoor branching", INFORMS Journal on Computing 25 (2013) 693–700, DOI 10.1287/ijoc.1120.0531 (preprint). Primary.
- ERR14 — M. Fischetti, M. Monaci, "Exploiting erraticism in search", Operations Research 62 (2014) 114–122, DOI 10.1287/opre.2013.1231 (preprint, rev. 21 Mar 2013). Primary.
- PRX14 — M. Fischetti, M. Monaci, "Proximity search for 0-1 mixed-integer convex programming", Journal of Heuristics 20 (2014) 709–731, DOI 10.1007/s10732-014-9266-x (preprint, 31 Jul 2013). Primary.
- SS14 — M. Fischetti, M. Monaci, D. Salvagnin, "Self-splitting of workload in parallel computation", CPAIOR 2014, LNCS 8451, 394–404, DOI 10.1007/978-3-319-07046-9_28 (preprint). Primary.
- RS16 — M. Fischetti, A. Lodi, M. Monaci, D. Salvagnin, A. Tramontani, "Improving branch-and-cut performance by random sampling", Mathematical Programming Computation 8 (2016) 113–132, DOI 10.1007/s12532-015-0096-0 (preprint). Primary.
- SVM16 — M. Fischetti, "Fast training of Support Vector Machines with Gaussian kernel", Discrete Optimization 22 (2016) 183–194, DOI 10.1016/j.disopt.2015.03.002 (preprint). Primary, solo.
- CFL16 — M. Fischetti, I. Ljubić, M. Sinnl, "Benders decomposition without separability: a computational study for capacitated facility location problems", EJOR 253 (2016) 557–569, DOI 10.1016/j.ejor.2016.03.002 (preprint). Primary.
- MATH16 — Martina Fischetti, Matteo Fischetti, "Matheuristics", Handbook of Heuristics, Springer (online 2016), DOI 10.1007/978-3-319-07153-4_14-1 (version posted at ~fisch/ricop/OR2/Matheuristics.pdf). Primary.
- UFL17 — M. Fischetti, I. Ljubić, M. Sinnl, "Redesigning Benders decomposition for large-scale facility location", Management Science 63 (2017) 2146–2162, DOI 10.1287/mnsc.2016.2461 (preprint). Primary.
- STE17 — M. Fischetti, M. Leitner, I. Ljubić, M. Luipersbeck, M. Monaci, M. Resch, D. Salvagnin, M. Sinnl, "Thinning out Steiner trees: a node-based model for uniform edge costs", Mathematical Programming Computation 9 (2017) 203–229, DOI 10.1007/s12532-016-0111-0 (2014 preprint). Primary.
- ORB17 — M. Fischetti, L. Liberti, D. Salvagnin, T. Walsh, "Orbital shrinking: theory and applications", Discrete Applied Mathematics 222 (2017) 109–123, DOI 10.1016/j.dam.2017.01.015 (preprint). Primary.
- TRR17 — M. Fischetti, M. Monaci, "Using a general-purpose Mixed-Integer Linear Programming solver for the practical solution of real-time train rescheduling", EJOR 263 (2017) 258–264, DOI 10.1016/j.ejor.2017.04.057 (revised preprint). Primary.
- BF17 — E. Balas, M. Fischetti, "Integer (Linear) Optimization", in Advances and Trends in Optimization with Engineering Applications, SIAM (2017) 49–63, DOI 10.1137/1.9781611974683.ch5 (preprint). Primary.
- DNN18 — M. Fischetti, J. Jo, "Deep neural networks and mixed integer linear optimization", Constraints 23 (2018) 296–309, DOI 10.1007/s10601-018-9285-6 (preprint). Primary.
- MBP18 — M. Fischetti, I. Mandatelli, D. Salvagnin, "Faster SGD training by minibatch persistency", 2018, arXiv:1806.07353. Primary.
- BIL20 — M. Fischetti, M. Monaci, "A branch-and-cut algorithm for Mixed-Integer Bilinear Programming", EJOR 282 (2020) 506–514, DOI 10.1016/j.ejor.2019.09.043 (2019 preprint). Primary.
- MBP26 — M. Fischetti, "Minibatch persistency, eight years later: what batch reuse costs in steps and joules, and what it saves in data", 12 Sep 2026, arXiv:2609.13922. Primary, solo.
- EW26a — Martina Fischetti, Matteo Fischetti, "EndoWake: Modeling Wind by Linear Programming for Wind Farm Layout Optimization", 30 Sep 2026, arXiv:2609.40157. Primary, AI-assisted (declared).
- EW26b — Martina Fischetti, Matteo Fischetti, "GPU-accelerated wind farm layout search with a distilled endogenous wake model (EndoWake)", Oct–Nov 2026, arXiv:2610.07844 (v3). Primary, AI-assisted (declared).
- EW26c — Martina Fischetti, Matteo Fischetti, "A Dantzig-Wolfe reformulation of the EndoWake model for optimal wind farm layouts", 29 Oct 2026, arXiv:2610.39503. Primary, AI-assisted (declared).
- FPC26 — M. Fischetti, "Feasibility Pump with Objective Cutoff: A Computational Study", manuscript submitted to Mathematical Programming Computation (Sept 2026; unreviewed), with README, https://github.com/mfischetti-arch/fp-objective-cutoff; code DOI 10.5281/zenodo.22810777, logs DOI 10.5281/zenodo.22810848. Primary, AI-assisted (declared).
- NSR05 — E. Abbink, M. Fischetti, L. Kroon, G. Timmer, M. Vromans, "Reinventing Crew Scheduling at Netherlands Railways", Interfaces 35 (2005) 393–401, DOI 10.1287/inte.1050.0158 (ERIM report version). Primary (context only).
- COAP17 — Editorial board of Computational Optimization and Applications, "COAP 2016 Best Paper prize", COAP 68 (2017) 473–478, DOI 10.1007/s10589-017-9959-9. Secondary.

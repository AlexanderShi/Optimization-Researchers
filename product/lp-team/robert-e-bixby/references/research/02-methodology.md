# Robert E. Bixby · 02 Stated methodology (what he says research should be)

| Field | Value |
|---|---|
| Researcher | Robert E. Bixby. Matroid theorist until the mid-1980s (Kentucky, Northwestern, Rice). Wrote the original CPLEX simplex code; co-founded CPLEX Optimization (incorporated 1987, first release 1988) and Gurobi Optimization (2008; CEO 2008–2015). Lens scope (team.json): decision and measurement craft for LP (1987–2002) and MIP. Living status and present role are **not** stated in this note (team.json leaves both open; see Gaps G1). |
| Dimension | Research agent 02 of 06: stated methodology. These are his claims about how solver research and development should be done and measured, sorted into the seven layers of `references/research-extraction-framework.md` §一. Whether he practised them is agent 03's job. |
| Research date | 2026-11-05 |
| Sources consulted | 38 sources, listed under Sources: 26 primary (15 his alone: 9 written, 6 spoken; 11 co-authored) and 12 secondary, observed or metadata. Three more items were checked and excluded (two homonyms, one webinar by another speaker). WebSearch: 4 of 7 calls used. Everything else came from curl, WebFetch, the Rice repository (DSpace API), OpenAlex, Unpaywall, Crossref and yt-dlp. |
| Local corpus | `references/sources/{papers,talks,essays,software}` held only `.gitkeep` placeholders, so there was no user-supplied material. `private/` was not opened. |
| Saved this run | Four caption transcripts with provenance headers under `../sources/talks/`: `toronto-2021-optimization-past-present-future.transcript.txt`, `subject-to-2023-interview.excerpt.transcript.txt` (excerpts; personal passages and one third-party passage left out), `co-at-work-2015-dual-simplex-lectures.transcript.txt`, `short-clips-2015-2020.transcript.txt`. |

## Reading guide

**Tags.**

| Tag | Meaning |
|---|---|
| [stated] | Bixby said or wrote it, in a text or talk of his alone. |
| [stated, co-authored] | A co-authored text: the authors' joint position, not attributable to him alone. |
| [stated, self-report] | His account of something he did (a test he ran, code he wrote). Agent 03 should check it against papers, data and code. |
| [stated, team] | He describes what "we" (the CPLEX or Gurobi team) do. At Gurobi he did no development by his own account (§10), so these describe team practice, not his own hand. |
| [observed] | Someone else's statement about him. |
| [inferred] | My reading. |

"Primary" means his own text or talk, co-authored ones included. "Secondary" means other people's accounts.

**Voice and transcript warnings.**

- Written solo texts weigh most: OR 2002, Documenta 2012, the Rice reports TR90-32 and TR93-40, ZIB SC 92-11, and the slide decks.
- Spoken sources are transcripts.
  - Optima 101 was transcribed from audio by the newsletter's helpers.
  - The Toronto 2021 talk, the 2023 "Subject to" interview and the 2020 Gurobi clip exist only as YouTube automatic captions, which garble names and numbers. Quotes from them are reproduced as captioned (lower case, no punctuation) and marked "(auto-caption)". Treat the wording as approximate; rely on the meaning only where it repeats a written source.
  - The CO@Work 2015 lectures and the 2015 Prendismo clip have uploaded (non-automatic) subtitles.
- The Hausdorff 2022 deck carries the footer "Confidential, All Rights Reserved" although the school page links it publicly. Quotes from it are kept to slide phrases.
- Gurobi-era "we" statements describe the team (tag [stated, team]).

**Page conventions.**

- OR 2002: printed pages 3–15 (PDF p. N = printed N+2). Documenta: printed 107–121. Optima 101: printed = PDF.
- SC 92-11: printed = PDF−1. SC-95-45: printed = PDF−1. ZIB-Report 16-44: printed = PDF−2.
- Rice reports by their own page numbers: TR90-32 = PDF−4; TR93-40 = PDF−2; TR91-11 and TR91-32 = PDF−6; TR89-16, TR91-38, TR92-36, TR93-37 = PDF−2; TR86-18 = PDF−4. TR98-03 is cited by PDF page.
- "Closing the Gap" (GAP00) by the preprint's own page numbers (the published chapter is pp. 19–50). Slide decks by PDF page.

**Source keys** (full entries under Sources): OR02, DOC12, OPT101, SC92, TR90-32, TR93-40, SC95, TR91-11, TR91-32, TR89-16, TR86-18, TR91-38, TR92-36, TR98-03, GAP00, ZR16-44, TR93-37, HAUS22, ECCO17, FIELDS12, IMP15, TOR21, SUBJ23, COW15, CLIP15, CLIP20.

---

## 0. Claims repeated three or more times (the real beliefs)

| # | Claim (faithful paraphrase) | Count | Where and when | Voice |
|---|---|---|---|---|
| R1 | Judge LP/MIP technology on real models collected from practice, never on randomly generated ones; build and keep renewing a library of such models. | ≥10 | TR90-32 p.5 (1991); TR91-38 p.1 (1991); TR92-36 p.1 (1992); TR93-40 p.13 (1993); TR98-03 PDF pp.2–3 (1998); GAP00 p.20 (2000); OR02 p.12 (2002); DOC12 p.116 (2012); OPT101 p.6 (2015); ECCO17 p.30 (2017); TOR21 (2021) | solo + co-authored, over 30 years |
| R2 | Summarise speed comparisons by the geometric mean of per-model time ratios; totals and arithmetic means of ratios mislead. | 6 | GAP00 p.3 (2000); OR02 p.11 (2002); DOC12 pp.112, 116, 118 (2012); TOR21 (2021) | solo + co-authored. Early exception: TR90-32 p.19 (1991), see C9 |
| R3 | Separate algorithmic from machine progress. Run old and new code versions on the same current machine (never old codes on old machines), compare consecutive versions and multiply. | ≥8 | TR93-40 pp.11–12 (1993); OR02 pp.4–5, 11 (2002); DOC12 pp.114, 116 (2012); FIELDS12 p.9 (2012); COW15 part 3 (2015); ECCO17 pp.9–14, 36–37 (2017); TOR21 (2021); HAUS22 pp.24–28 (2022) | solo |
| R4 | Measured progress depends on model size. Small test sets (netlib) understate algorithmic gains and mislead about defaults; report by size bracket (row count). | ≥5 | TR90-32 p.5 (1991); TR93-40 p.12 (1993); GAP00 pp.5–10 (2000); OR02 pp.12–13 (2002); COW15 part 3 (2015) | solo + co-authored |
| R5 | No single LP algorithm dominates. Keep primal, dual and barrier; report per-algorithm wins beside averages; "best of three" is the baseline, and he flags it as arguable. | 6 | TR91-32 p.1 (1991); TR93-40 p.13 (1993); GAP00 p.12 (2000); OR02 p.13 (2002); DOC12 p.114 (2012); TOR21 (2021) | solo + co-authored |
| R6 | Verdicts that a method is done, hopeless or of only theoretical interest belong to the codes and machines of their day; test them before accepting them (LP itself, degeneracy, dual simplex, simplex vs barrier, Gomory cuts). | ≥8 | TR90-32 p.1 (1991); GAP00 pp.17–18 (2000); OR02 pp.7–8 (2002); DOC12 p.112 (2012); OPT101 p.3 (2015); TOR21 (2021); HAUS22 p.21 (2022); SUBJ23 (2023) | solo |
| R7 | Start from the failing instance itself: look at the model and the code and fix one failure at a time (in 1984–86 without reading the literature). | 5 | OR02 p.3 (2002); FIELDS12 p.35 (2012); OPT101 p.2 (2015); TOR21 (2021); SUBJ23 (2023) | solo, self-report |
| R8 | Make defaults that help where they apply and cost little where they don't: a "barrage" of cooperating ideas, each switched off automatically when it is not helping. | 3 sources (5 places in GAP00) | TR90-32 p.16 (1991, default basis); GAP00 pp.3, 6–7, 12–13, 26–27 (2000, co-authored); SUBJ23 (2023, on presolve) | solo + co-authored |
| R9 | The 1998 MIP jump (CPLEX 6.5) came from "mining the theoretical backlog" of cuts and presolve, and Gu and Rothberg did it. | ≥6 | GAP00 p.26 (2000); DOC12 p.117 (2012); FIELDS12 p.7 (2012); ECCO17 p.32 (2017); TOR21 (2021); SUBJ23 (2023) | solo + co-authored |
| R10 | What to build next is decided by the paying user's pain: know the customer, listen, and notice when a "nice to have" becomes a "must-have". | ≥5 | OPT101 pp.3, 6 (2015); CLIP15 (upload 2015); TOR21 (2021); HAUS22 pp.18–19 (2022); SUBJ23 (2023) | solo |
| R11 | Modelling is the bottleneck: a bad model defeats any solver, and the need to build a model is the main hurdle to wider use. | ≥5 | GAP00 p.26 (2000); OR02 p.14 (2002); ECCO17 pp.24–25 (2017); TOR21 (2021); SUBJ23 (2023) | solo + co-authored |
| R12 | Dual simplex with (Forrest–Goldfarb) dual steepest edge is the decisive LP development; most-infeasible or most-negative pricing is a bad rule. | ≥7 | TR93-40 pp.6, 9–10 (1993); OR02 pp.6, 8 (2002); OPT101 pp.2–3 (2015); COW15 part 3 (2015); TOR21 (2021); HAUS22 pp.21–22 (2022); SUBJ23 (2023) | solo |
| R13 | LP is not finished: about 2% of real MIPs are blocked by their LPs, and standard LP algorithms barely moved from 2004 to about 2015. | 4 | DOC12 p.115 (2012); ECCO17 p.16 (2017); TOR21 (2021); HAUS22 p.28 (2022) | solo |
| R14 | Academic MIP research now rarely reaches the solvers; meaningful tests need solver internals (for example the interaction of cut classes). | 3 | OPT101 p.6 (2015); TOR21 (2021); SUBJ23 (2023) | solo |
| R15 | Users want good solutions, not proofs of optimality. | 3 | GAP00 p.15 (2000); ECCO17 p.21 (2017); TOR21 (2021) | solo + co-authored |
| R16 | Credit belongs to the team: the progress numbers are not his alone, and he gets more than his share of credit. | ≥4 | OR02 p.14 (2002); OPT101 p.4 (2015); TOR21 (2021); SUBJ23 (2023) | solo |
| R17 | Say which way your own numbers lean (underestimate, exaggeration, bias against an algorithm). | ≥6 | TR90-32 p.19 (1991); TR93-40 p.3 (1993); GAP00 pp.4, 9, 12 (2000); OR02 p.12 (2002) | solo + co-authored |
| R18 | Profile first, then attack the step that dominates the time. | 3 | TR89-16 p.3 (1989); SC95 p.4 (1995); GAP00 p.5 (2000) | co-authored |

---

## 1. Research taste (what is worth doing, what is a good result)

**1.1 Computing answers to real problems is the point.** [stated] primary. Count 3 (2002, 2012, 2022).

- DOC12 p.107 (2012), on Dantzig, whose view he adopts: "Dantzig viewed LP not just as a qualitative tool in the analysis of economic phenomena, but as a method that could be used to compute actual answers to specific real-world problems."
- HAUS22 p.4 (2022), slide on Dantzig: "Computing answers important."
- OR02 p.4 (2002): his question is how the developments affected "our ability to solve real-world LPs", to be answered "as quantitatively as possible".

**1.2 Real instances, never random ones (R1).** [stated] and [stated, co-authored] primary.

- TR92-36 p.1 (1992, co-authored): "These differences are often so significant that algorithms developed for randomly generated problems are almost guaranteed to perform poorly on the real problems they were presumably intended to solve."
- TR90-32 p.5 (1991): "To the knowledge of this author, the netlib set does not contain any randomly generated problems." The German SC92 p.6 says the same.
- TR91-38 p.1 (1991, co-authored): "One hindrance to research in this area has been a lack of general availability of real models."
- OR02 p.4 (2002): "The insights for many of these improvements have come from the simple ability to examine larger and more interesting real instances in real time."
- Library sizes he reports [stated, self-report / team]:
  - OR02 p.12: the CPLEX LP library, about 2,000 models collected over 13 years "from industry and academia".
  - OPT101 p.6 (2015): at Gurobi, 600 models within two days ("times have changed"), now about 10,000, with a real test set of about 3,500.
  - ECCO17 p.34: "Gurobi MIP Library (3550 models)".
  - TOR21 (auto-caption): 1852 CPLEX models; the Gurobi library "now grown to something like 6300 models".

**1.3 Robustness matters more than the headline speed-up.** [stated] primary. Count 4.

- GAP00 pp.4–5 (2000, co-authored): the most significant development of the decade does not show in the speed table: "This development was the leap forward in robustness of linear programming codes."
- OR02 p.4: "What was needed was a numerically robust code that was also flexible enough to be embedded" in integer-programming applications.
- OPT101 p.2 (2015): "initially I was very proud of the numerical stability". On condition numbers near 10^20 in his first users' problems: "In general, if you have a condition number like that, the answer doesn't mean anything, and you should just give up anyway. But if you do an SLP you can't give up."
- SUBJ23 (auto-caption): his first code "was stable based on ideas coming out of this class that I took as an undergraduate" (real analysis).

**1.4 Simple ideas win; theory that removes freedom of choice fails in practice.** [stated] primary.

- COW15 part 3 (2015), after explaining bound shifting: "But anyway, the simple ideas, I guess, are the good ones."
- OPT101 p.4: after two weeks of trying instrumentation, the fix came when "I got a very simple idea which was" to change the bounds. On Gomory mixed-integer cuts: "That's the silly thing about it, they're the easiest ones."
- Bland's rule:
  - COW15 part 2: "Unfortunately, Bland's Rule is an absolutely terrible idea from the computational point of view."
  - SUBJ23 (auto-caption) calls the rule beautiful mathematics but notes it fixes both the entering and the leaving choice, so "in practice you literally cannot Implement that algorithm".
- Count: simple-ideas 3 (OPT101, COW15, SUBJ23); Bland's rule 2.

**1.5 A general-purpose engine beats special-purpose frameworks.** [stated] primary. Count 4.

- DOC12 p.116: the callable library was meant "to treat LP as a kind of black-box tool that could be used as an embedded solver".
- GAP00 p.22 (co-authored): "Most users of mixed-integer programming are not interested in the details of how the codes work." Hence defaults.
- SUBJ23 (auto-caption): frameworks for branch-cut-price or stochastic programming "are never an exact fit"; selling them needs consulting, and "Consulting is a very low margin business and people intensive".
- CLIP20 (auto-caption): Gurobi's first pillar is "a single product we wouldn't be distracted by things like consulting".

**1.6 Signals of work he discounts (negative taste).** [stated] primary.

- Testing a new idea "usually in isolation", as theoretical investigations do (GAP00 p.3, co-authored). See §4.
- Public benchmarks in which one code hits the time limit everywhere: "the benchmarks tell you nothing" (TOR21, auto-caption, about the open-source solver lp_solve).
- Claims that NP-hard means unsolvable, from people who do not test (TOR21, auto-caption): "they're taught that np hard means you can't solve it", and they believe it "unless they actually look at the data".
- A large machine-learning-for-MIP study that "was largely unsuccessful we've looked at those results pretty carefully" (TOR21, auto-caption). This is his verdict on others' work; the study is not identified.
- Robust optimization is too conservative to be used: TOR21 says the bounds "have been too conservative"; SUBJ23 repeats the point. Count 2.
- Test sets drawn from hard-for-the-incumbent cases (TR93-40 p.1). See §5.3.

**1.7 Matroid-era taste (context only, not LP/MIP craft).** [stated] primary (SUBJ23, auto-caption).

- Ray Fulkerson told him which work mattered: "the two people to pay attention to were Jack Edmonds and WT Tut" (Tutte), and that work was worth understanding completely.
- He read Tutte's matroid lectures on Tutte's own terms: "I literally spent a year and a half immersed in that paper".
- He left a pure-mathematics department because "their whole view of what you would do with these ideas was so completely different".

---

## 2. Problem choice (where problems come from, why now, when to stop)

**2.1 Problems arrive as failing real instances from users.** [stated, self-report] primary. Count ≥6 distinct cases, each told repeatedly.

- Sequential-LP snapshots that kept breaking his first code (Chesapeake, about 1984–86): OR02 p.3; OPT101 p.2; SUBJ23.
- The airline fleet model degen4 / LAU2, passed on by John Gregory of Cray Research: OR02 p.8; OPT101 p.3; HAUS22 pp.20–22; TOR21; SUBJ23.
- The American Airlines crew-scheduling challenge: TR91-11 p.1; HAUS22 p.14.
- The military PDS models: OR02 pp.8–10; GAP00 pp.4–6.
- A graduate student's (Sanjay Saigal's) degenerate max-cut LPs: OPT101 p.3, "I had to invent something in the code to handle this degeneracy or Sanjay could not do anything."
- The California unit-commitment model at a 1999 meeting: TOR21 and SUBJ23 ("i literally chased this guy around the room", TOR21 auto-caption, to obtain the model).
- OR02 p.7 on degeneracy: older developers chose not to implement explicit procedures, "However, as difficulty has increased, such measures have become essential."

**2.2 "Why now": machines, memory, model size, and what the integer-programming community needs.** [stated] primary.

- TR90-32 p.1 (1991): LP had been considered mature, "That expectation was incorrect". Changes in machines allowed new strategies, and integer programming needed a good LP solver.
- TR93-40 p.6 (1993): "We have therefore chosen to use the fact that computer memory is now relatively cheap, and store the constraint matrix A twice".
- GAP00 p.5 (2000, co-authored): "We began the work described in this section by making a simple observation: LPs have become larger." This led them to models with at least 10,000 constraints and to the simplex method, which underperformed there.
- The callable library came from integer-programming research needing an embeddable LP solver: OR02 p.4; DOC12 pp.111, 116; OPT101 p.3; SUBJ23.
- SC95 p.1 (1995, co-authored): "We have chosen the dual over the primal for two reasons". The default primal uses partial pricing, which removes parallelism, and the main application is reoptimization in integer programming.

**2.3 Choosing the next feature: the user's must-have (R10).** [stated] primary.

- HAUS22 pp.18–19 (2022), after Ed Rothberg's account: a 40× faster parallel barrier did not win the airlines, "Not enough: 40x was a nice to have not a must have!". A merger due-diligence deadline then made it a must-have: "We learned the "must-have" story". SUBJ23 tells the same story: "our nice to have became a musthave" (auto-caption).
- The MIP solver was added because sales demanded it. OPT101 p.3, of Todd Lowe: "He just immediately figured out, if you want to succeed in this business you needed a MIP." SUBJ23 tells the same.
- OPT101 p.6 (2015) advice: "Advice #1 is if you are thinking about selling something, you have to figure out who your customer is going to be." And: "if you think the marketing people are going to give you super-duper ideas for the next thing to do because they go out and do a market study, you are kidding yourself, just forget it."
- CLIP15 (upload 2015): "if they would just shut up and listen to what the customer is saying, they would hear what the pain is", and "Give them what they want."

**2.4 Persisting against "no future" advice, and what made that affordable.** [stated, self-report] primary. Count ≥4.

- SUBJ23 (auto-caption): George Nemhauser asked him "why are you spending time on this this doesn't look like it has any future"; his answer was "but I ignored him I was having so much fun I ignored him". He adds that he had tenure by then. **Resource context: tenure.**
- TOR21 (auto-caption): "all of my friends told me i was absolutely crazy", and "i had zero success initially in getting funding research funding for this".
- HAUS22 p.9: "Could not get funding for research in LP computation -- zero success". SUBJ23: "any attempt I made to sort of try to get some funding to continue working on the Simplex algorithm nobody was interested".
- The failed funding led to the company (TOR21; SUBJ23). Seniority context: tenured professor.
- On LAU2:
  - TOR21: "john gregory's advice to me was forget it it's hopeless the simplex method will never solve this problem that fast well um i ignored what he said".
  - SUBJ23: "my reaction was okay you think there's no chance but I'm not going to give up".
  - HAUS22 p.21: "Recommended giving up on simplex!!"
  - OR02 p.8, on the same advice: "That conclusion was wrong."

**2.5 When to stop or narrow.** Mostly [stated, co-authored] primary.

- SC95 p.9 (1995): "To summarize, there seems little hope of achieving good parallel performance on a general set of test problems using a distributed-memory model. That result is not unexpected." The work moved on to shared-memory threads.
- TR89-16 p.5 (1989): the two-processor scheme's typical 20% gain invites dismissal as "interesting but impractical". The report then lists the niches where it still helps (p.6).
- TR90-32 p.5 (1991): "in practice it does not make much sense to run all the problems in such a class without first doing some testing, based on smaller instances in the class". Once fit1p and fit1d show the dual formulation is easier, there is little reason to solve fit2p.
- SUBJ23 (auto-caption): a stochastic product would be pursued only for "a solid opportunity", and then "something stochastic we would be all over it". Frameworks and robust optimization were not pursued (§1.5, §1.6).

---

## 3. Idea generation

**3.1 Stare at the instance; ideas come from failures (R7).** [stated, self-report] primary.

- OR02 p.3 (2002): he "poked around" in his code and the LP, "never looking in the literature (this wasn't my area of research)".
- OPT101 p.2 (2015): "But I never actually went and read anything." Also: "I would mess around and figure it out." And: "It was just numerical stability problems one after another. I would fix one and wait for the next one."
- TOR21 (auto-caption): "it wasn't my research i didn't look at the literature i didn't pay attention to what anybody was doing".
- SUBJ23 (auto-caption): "it wasn't my research area and I didn't know the literature and so I would just kind of stare at it and get an idea and fix it".
- FIELDS12 p.35 (2012), on Gurobi's MIP "tricks": "A lot of them are easy to find by just staring at models and often are also easy to apply".
- Others observed the same habit. [observed] secondary.
  - Cook (Optima 101 p.7): "Bob's motto is that if you see something, then fix it!" And: "When numerical results are off, don't ignore the bad values or try to work around them, but identify the problem and see what you can do about it."
  - Grötschel (Optima 101 p.7): "He implemented linear and integer programming codes by looking at failures, learning on the run, adapting, making little experiments and improvements, and by accepting advice from others."
- Scope note [inferred]: the no-literature habit belongs to 1984–86. For later steps he did read, for example Lemke's dual method (SUBJ23), Goldfarb's steepest edge (§3.4) and the Suhl LU paper (§10).

**3.2 Transpose the difficulty: look at the dual.** [stated] primary. Count 4.

- OR02 p.8: the key idea for degen4 was "Look at the dual."
- HAUS22 p.21: "Maybe the dual isn't nearly as degenerate."
- TOR21 and SUBJ23 tell the same step (auto-caption).

**3.3 Combine two ingredients that each already work.** [stated] primary. Count 3.

- TOR21 (auto-caption), on Forrest's success with primal Devex: "if he's having success with something related to steepest edge and the primal it ought to work even better in the dual".
- SUBJ23 (auto-caption): "if devx is working then steepest Edge should work".
- HAUS22 p.21, step 5, makes the same move.

**3.4 Go to the originator of a method and take the better variant.** [stated] primary. Count 4.

- TOR21 and SUBJ23 (auto-captions): Goldfarb was unimpressed by his first dual steepest-edge variant and pointed to the one that projects out the slacks. Implemented, it was much faster.
- HAUS22 p.21, step 6: "Don Goldfarb (steepest-edge guru) suggests simpler SE".
- TR93-40 p.4: "As will become clear, much of the credit for these improvements is due Don Goldfarb."
- OR02 p.6 and note 7: the CPLEX dual uses "version 1" of Forrest and Goldfarb (1992).

**3.5 Borrow from neighbouring fields.** [stated] primary.

- Sparse linear algebra:
  - GAP00 p.5 (co-authored): the needed algorithm "has long been known in the sparse linear algebra community".
  - OR02 p.6 cites Gilbert and Peierls (1988).
  - COW15 part 3 calls it "a simple graph theory idea" and says: "This is what saved the simplex algorithm for large problems. Without this idea it's dead."
- Megiddo's theorem for crossover:
  - TR93-40 p.11: "Our crossover is an implementation of the proof of the main theorem in [15]" (Megiddo 1991).
  - HAUS22 p.15: "Developed first really fast crossover (based on a result of Megiddo)".
- Harris's ratio test, which Bob Fourer pointed him to: OPT101 p.4; SUBJ23.

**3.6 Profile, then attack the dominating step (R18).** [stated, co-authored] primary.

- TR89-16 p.3 (1989): CPLEX spent about 20% of its time refactorizing and 40% in the linear solves. "This fact led to the following idea", namely a second processor that refactorizes.
- SC95 p.4 (1995): profiles show that "24.0% of the work can be parallelized for pilots and 97.3% of the work for aa300000". These profiles set the expectations for the parallel dual.
- GAP00 p.5 (2000): "It didn't take long to discover where the bottleneck lay": FTRAN and BTRAN on large, sparse models.

**3.7 Collaborators' needs supply ideas.** [stated, self-report] primary.

- Strong branching came from Cook; Bixby put it into CPLEX.
  - OPT101 p.4: "Somehow in a discussion that Bill Cook and I were having, it came up and I put it in CPLEX."
  - SUBJ23 (auto-caption): "since I had access to the clex source code I went and implemented a bunch of stuff to implement strong branching".
- Perturbation came from a student's degenerate max-cut problems (OPT101 p.3, §2.1).

**3.8 Turn a remedy into a technique.** [stated] primary. Count 2.

- OR02 p.9: CPLEX 7.1 uses perturbation in the dual "treating this idea as an algorithmic technique rather than simply a remedy for degeneracy".
- COW15 part 3: Gurobi perturbs the dual even when it is progressing, "because it just helps the outcome for some reason that we don't fully understand".

**3.9 Mathematical training as a source.** [stated, self-report] primary. Count 2.

- OPT101 p.2: getting the tolerances to balance was like "a big epsilon delta proof".
- SUBJ23: the stability of his code rested on the undergraduate analysis course (§1.3).

---

## 4. Experiments and execution: the measurement craft

This layer has the richest record. Many rules appear in co-authored texts; the voice is marked on each.

**4.1 How to build a test set.**

- *Drop near-duplicates and keep the largest of a family.* Count 5.
  - TR93-40 p.13 (1993): "We also considered at most one instance from a given model type, when it was clear two models were closely related", for example only the 8-period instance of a 1-, 2-, 4-, 8-period family.
  - OR02 p.12 (2002): "screening", keeping "only the largest two or three".
  - GAP00 pp.8–9 (2000, co-authored): only the largest of a family.
  - TR98-03 PDF p.4 (1998, co-authored): "The remainder of the deleted problems were chosen to reduce duplicity."
  - ECCO17 p.30 (2017): 348 "Duplicates" removed.
- *Remove the easy models.* Count 5.
  - OR02 p.12: drop models solved in under 0.25 s by both versions and all three algorithms.
  - GAP00 p.20: drop models under 100 s.
  - TR98-03 PDF p.4 (co-authored): a model left MIPLIB when it solved in 11 s or less with settings "meant to correspond to what one might consider the most straightforward implementation of a reasonable, LP-based branch-and-bound solver".
  - ECCO17 p.30: 559 "Easy" MIPs removed.
  - ZR16-44 p.3 (2016, co-authored): report the "≥ 10 sec" bracket "because this excludes the relatively uninteresting easy models but is still large enough to draw meaningful conclusions".
- *Keep the hard-but-solvable.* GAP00 p.21 (co-authored): the preferred MIP set holds "the models that appeared to be difficult but solvable, assuming tuning was allowed". ZR16-44 p.3 (co-authored) uses the models some Gurobi release solved within 10,000 s.
- *Size floors and resource limits.* TR93-40 p.13: at least 100,000 nonzeros. GAP00 pp.8–9: at least 10,000 rows after presolve, and a 0.5 GB memory limit.
- *Record where each model comes from and whether its optimum is verified.*
  - TR91-38 p.3 (co-authored): "The qualifier (opt)* indicates that the solution is reportedly integer optimal, as stated by various sources, but it has not yet been verified by us."
  - TR98-03 PDF p.6: submissions should state the origin, the optimum and how it was obtained.
- *Prefer proprietary customer models when judging performance, and admit the bias.*
  - GAP00 p.20: "There is a second test-set of largely proprietary models that we prefer to MIPLIB 3.0 in evaluating performance."
  - SC95 p.7: the larger models came "from proprietary models available to the first author".
  - TOR21 (auto-caption): "there's certain biases built into it because it is based on the models that we have access to"; the set is "probably biased a little bit to difficult models that tend to be the ones people send to us".

**4.2 Clean timing.** [stated] primary.

- TR90-32 p.19 (1991): "All runs were made in batch mode on a standalone system with no other userjobs running." Timings are user times; compiler flags are reported (p.18).
- SC95 p.7: wall-clock times for the parallel runs.
- DOC12 p.116: "a bank of identical computing machines".
- TOR21 (auto-caption) [stated, team]:
  - "we test the machines regularly to make sure that they're comparable machines and we're very very careful about making sure nobody else is on them".
  - "we run it on with five different random seeds", with geometric means over the seeds, because one small change can send a MIP search elsewhere.
  - "we can measure improvements on the order of believe it or not 0.2" (the unit is not clear in the captions).
- Reproducibility:
  - SUBJ23 (auto-caption): his perturbation "had to have the property that it was random but predictable so if I ran it twice it had the same behavior".
  - FIELDS12 p.19 (Gurobi trick): "Use virtual time (deterministic) spent on B&C vs. estimate time of dynamic programming".

**4.3 Defaults first; disclose tuning.**

- TR93-40 p.13 (1993): "However, tuning was largely ignored in the construction of Table 14." And: "For the barrier method, when non-default runs were made, they were preceded by an attempted run with defaults."
- GAP00 p.21 (co-authored), a hard baseline: "We next compared CPLEX 6.5 running defaults with tuned CPLEX 6.0 times, using the best parameter settings that are known to us." The result was 3.8×.
- GAP00 p.3: "there will always be instances that demand some sort of tuning or reformulation". Probing, for example, is off by default because it can explode (pp.23–24).

**4.4 Time limits and censored runs.**

- GAP00 p.9 (co-authored):
  - "A limit this large may seem excessive, but it was deemed necessary for the tests". The limit was 500,000 s.
  - Runs that hit the limit were counted at the limit: "As a result the comparisons we made underestimated the actual improvements."
- DOC12 p.116: version pairs compared on models solved by at least one of the two, "using the time limit for models that did not solve to optimality".
- OR02 p.12: a 350,000 s limit; three models unsolved by every algorithm were omitted and named by size.
- GAP00 p.20: for models solved by neither version, compare the final gaps (geometric mean of gap ratios 3.3).
- TOR21 (auto-caption), against misleading public tables: the code is "hitting the time limit in every case if you increase the time limit by a factor of 10 it would be 10x slower".

**4.5 Ablation in both directions.** [stated, co-authored] primary.

- GAP00 p.21: "In the first test we started with defaults, turned off individual features one at a time, and measured, using geometric means of ratios of solve times, the effects of these changes." The second test went the other way: all cuts off, then one class at a time on. "The big winner here, and perhaps the biggest surprise, was Gomory cuts" (p.22).
- FIELDS12 p.11 (2012) reports a component ranking on 78 models solvable only after CPLEX 6.5:

  | Component | Gain |
  |---|---|
  | Cutting planes | 33.3× |
  | Presolve | 7.7× |
  | Variable selection | 2.7× |
  | Node presolve | 1.3× |
  | Heuristics | 1.1× |
  | Dive probing | 1.1× |

- ZR16-44 (2016) measures the effect of disabling presolve components. Its reporting form is credited to others: "We present our results in a similar form to that used in Achterberg and Wunderling [5]" (p.3). Do not attribute that protocol to Bixby.

**4.6 Version-to-version chains.** [stated, self-report] primary.

- DOC12 p.116 (2012): in late 2007 he recompiled the twelve CPLEX releases 1.2–11 for one machine and ran 1,892 models with a 30,000 s limit. "I then compared consecutive versions by taking each model that was solved to optimality by at least one of the two versions, computing the ratios of the solve times (using the time limit for models that did not solve to optimality), and then computing the geometric means of these ratios."
- DOC12 p.117: the cumulative line is "computed by multiplying the effects of the individual improvements", giving over 29,000.
- The chain is spliced to Gurobi at "roughly equivalent" (CPLEX 11.0 vs Gurobi 1.0) on public benchmarks: FIELDS12 p.8; DOC12 pp.117–118. TOR21 (auto-caption) flags the splice: "it's based on the claim that the first version of gerobi that was released was roughly as fast as version 11 of cplex that's arguable".

**4.7 Old code on today's machine, never old machines.** [stated] primary. Count 3.

- OR02 p.11 (2002): running old codes long enough on old machines would take fractions of a year. "Carrying out such a program is clearly impractical." Instead a chain of forward comparisons: "These results will, I believe, make a convincing case when taken as a whole."
- COW15 part 3 (2015): "So this comes back to your point about testing old algorithms on old machines. It doesn't make any sense."
- ECCO17 pp.9–14 and HAUS22 pp.24–27 [stated, self-report]: CPLEX 1.0 (1988) was re-run on a 2.0 GHz Pentium 4 for 29.8 days on a 401,640-row production-planning model. The slides carry dated checkpoints from 13 Nov to 6 Dec 2002. Against it: CPLEX 5.0 took 1.5 hours (480×) and CPLEX 9.0 59.1 seconds (43,500×).
- *Choice of baseline.* OR02 p.11: XMP rather than MPSX/370 or MPS III. Leaving portability and embeddability aside, "the simple speed comparison is of limited interest": those mainframes were at most 50 times slower than 2002 workstations, the algorithmic gains alone exceed 50, and 1989 tests on an IBM 3090 had shown MPSX/370 and CPLEX 1.0 comparable on several harder models. XMP was portable, embeddable and widely used in integer-programming research.

**4.8 Equalise baselines and predict the gain before claiming it.** [stated, co-authored] primary.

- SC95 p.15 (1995): a superlinear two-processor speed-up turned out to be related, at least in part, to the cache behaviour of the column partitioning; the same partitioning made the sequential code faster too. "After considerable testing, we thus chose to set K" "in both the sequential and parallel instances". The sequential baseline got the same partitioning.
- SC95 p.16: reorganisations were made to apply to the sequential path too, "thus preserving code unity".
- TR89-16 p.5 (1989): "Note that it would be unrealistic to expect a twofold speed increase using this type of parallelism on two processors". The expected gain was about 20%, the share of refactorization time. "For some of the problems we tested, we did not achieve this speedup."

**4.9 Heavy-tailed effects need different statistics.** [stated, team] primary (FIELDS12, Gurobi results).

- FIELDS12 p.26 (2012), on subtree overlap: 35 of 510 models were affected and one went from 10,000+ s to 0.01 s. "Makes it tough to quote mean improvements over a small set". "Median improvement for affected models is ~1%".
- FIELDS12 p.29, another reduction: "Overall impact is positive, but small".
- ZR16-44 p.17 (co-authored): "Nevertheless, the size of the test set is too small to draw any meaningful conclusions".

**4.10 Fresh runs and checked answers.** [stated, self-report] primary.

- TR90-32 p.7 (1991): to get accurate objective values, all netlib problems "were first solved using default settings and then reoptimized from that point with optimality and feasibility tolerances set to" 10^-9, with a pivot threshold of 0.99999.
- COW15 part 3 (2015): a steepest-edge example was run "on whatever machine I was using two days ago when I did this".
- OPT101 p.2 (2015): "But even to this day I love running benchmarks and solving problems."

**4.11 The Gurobi idea pipeline.** [stated, team] primary. TOR21 (auto-caption).

- "you need to have a development team that can implement ideas very quickly and you need to have various ways to provisionally test ideas".
- "probably only one in ten ideas that get tried show really any promise whatsoever".
- "we have literally 200 machines that are constantly running" comparisons. An idea passes four or five filters, and the testing becomes careful only after the first three or four.
- Whether this guards against over-tuning to the test set: "whether this completely deals with the issue of of getting into some sort of local minimum but overtuning you can still argue about that".

**4.12 Build code so experiments are cheap.** [stated, co-authored] primary. Count 2.

- TR86-18 p.2 (1986): "Thus we recommend that a computer system for network identification be designed to encourage experimentation with different combinations of heuristics."
- TR93-37 p.2 (1993): "With this in mind we designed the code so that individual features/components can be switched on and off, allowing great flexibility in testing the effectiveness of different solution strategies."

---

## 5. Judging results

**5.1 A gain counts only if it does not hurt the middle (R8).** [stated, co-authored] primary.

- GAP00 pp.6–7 (2000): the large-model gains were the impetus, but the real effort went into "making sure that these improvements didn't get in the way when they didn't help".
- GAP00 p.3: "implement the individual ideas in such a way that they help when they can, and otherwise hurt as little as possible".
- GAP00 p.13: "creating aggressive strategies for determining that a technique is not helping and turning it off automatically".
- SUBJ23 (auto-caption), on presolve: "when a problem has the has the property you're looking for you find it and you exploit it and when it doesn't you don't waste time that's absolutely critical".
- TR90-32 p.16 (1991), the same logic for the starting basis: "However, in the opinion of this author, the CPLEX initial basis is best viewed not as a crash, but simply as a default starting basis. In general, trying to guess a correct basis for a problem with unknown origins can have disastrous consequences." The German SC92 p.17 says the same; my translation: a crash procedure on a problem of unknown origin can have catastrophic consequences.

**5.2 Say which way your numbers lean (R17).**

- TR90-32 p.19 (1991): "These numbers can be misleading if a sizeable number of the ratios are significantly less than 1.0. That, however, is not the case here."
- TR93-40 p.3 (1993), on his own preprocessing gains: "Thus, the improvements in solution times reported in Table 4 (which is measuring the improvement due to preprocessing) are somewhat exaggerated."
- GAP00 (co-authored):
  - p.4: "Thus, the fifteen-fold improvement for the one problem in the table in the period 1988 to 1998 can be viewed as an underestimate."
  - p.9: "As a result the comparisons we made underestimated the actual improvements."
  - p.12: "All of the numbers presented here can be viewed as biased against the barrier algorithm in the following two senses." The senses are x86 floating point, and parallel barrier not used.
- OR02 p.12: the old netlib-sized models "likely lead to an underestimate of the difference between XMP and CPLEX 1.0, and they are certainly too small to yield any useful information about current codes".

**5.3 Read other people's comparisons for test-set bias, defaults and hardware.** [stated] primary (TR93-40, 1993, on Lustig, Marsten and Shanno 1994).

- p.1: "it is our opinion that the results of Lustig, Marsten, and Shanno (hereafter LMS) somewhat overstate the performance of these methods relative to the simplex method".
- p.1, on the test set: "They are also relatively sparse, which probably makes them better candidates for barrier methods." And: "As LMS also note, there is likely some bias in the set, having originated in part from users who were unhappy with the performance of their current LP solvers."
- pp.12–13: dual steepest edge, though available in OSL, "was not used in LMS since it was apparently not the default". And: "It should also be noted that the runs in LMS were made on IBM RS6000 Powerstations, an architecture more favorable to barrier methods."
- p.13, his verdict on a different, larger set: "The results in Table 14 indicate to us that there is no single dominate method for the solution of large-scale linear programming problems."

**5.4 Separate a method from one of its components.** [stated] primary. Count 2.

- TR93-40 p.9 (1993), on a bad dual-simplex table: "These results do not look like progress; however, the difficulty is not the dual method itself, but the pricing rule."
- OR02 p.8: "maximum-infeasibility variable selection just didn't work very well, and doesn't work very well in general".

**5.5 Revise your own verdicts, with dates.** [stated] primary. Count 4.

- OR02 p.8 (2002), on his 1989 conclusion that CPLEX 1.0 could not solve degen4: "As it turned out, this conclusion was probably incorrect." A 2002 run solved it in about 1.5 days, after "some 4,897,095 iterations" with a constant objective.
- GAP00 p.12 (2000): "If this question had been asked in 1998, our response would have been that barrier was clearly best for large models. If that question were asked now, our response would be that there is no clear, best algorithm."
- DOC12 p.112 (2012), on the 1980s belief that LP codes were mature: "Events were to prove this belief to be totally wrong."
- TR90-32 p.1 (1991): "That expectation was incorrect."

**5.6 Leave unexplained effects unexplained.** [stated, co-authored] and [stated] primary.

- SC95 p.17 (1995): "There are unfortunately several, as yet unexplained anomalies in our results." The authors offer only a tentative cache and memory-bus explanation.
- COW15 part 3 (2015): the dual's taste for perturbation helps "for some reason that we don't fully understand".

**5.7 Weigh rare cases by their frequency.** [stated] primary.

- COW15 part 3 (2015), on detecting in advance when removing bound shifts will cause infeasibility: "And it so rarely happens. It just turns out it's not worth worrying about."

**5.8 Averages hide winners.** [stated] primary.

- OR02 p.13: "However, it is important to note that the numbers in Table 15 do measure only average performance." Each of primal, dual and barrier wins in a significant number of cases.
- DOC12 p.114, on the best-of-three baseline: "One can argue whether this is a legitimate approach, but it is the one that I have used." TOR21 (auto-caption) says the same: "you might say okay that's cheating you're comparing one algorithm to three algorithms but we only had one algorithm in 1988 we didn't have three", and "you can accept it or not".

**5.9 Honesty words and practical meaning.** [stated] primary.

- SUBJ23 (auto-caption), on CPLEX 6.5: "that release was an honest an honest scientifically honest 10 times faster than the previous release".
- OR02 p.14, on six orders of magnitude: "Of course, no one waits one year to solve a model, at least no one I know." And: "The real meaning of such an advance is much harder to measure in practice, but it is real nevertheless."
- OR02 p.4: "While it is my conviction that algorithmic and software improvements have been equally important, there is no doubt that hardware effects are large and pervasive." TOR21 (auto-caption) adds: "you won't find very many places where the algorithmic improvements and the mathematics contributed more than the machines".

**5.10 Do not oversell NP-hard problems.** [stated] primary.

- TOR21 (auto-caption): "i don't want you to come away from this talk with the impression that we can just solve arbitrary mixed integer programming problems". His example is a 44-row model with free general integers, which is a case of "bad" modelling.
- ECCO17 pp.24–25: "What's wrong? Bad modeling." And: "However: Branch-and-bound cannot solve!" (the toy model, unless presolve reasoning is applied).

**5.11 How to judge an idea from outside a commercial solver.** [stated] primary.

- OPT101 p.6 (2015): "It's perfectly clear, it's very hard to test whether something is a good idea or not." And: "I mean the most you can hope for these days is that it somehow looks like reasonable idea when you do a little bit of testing."
- DOC12 p.116, his praise for MINTO: "Moreover, though this code was a research code, it was clearly well implemented and provided an important test of the efficacy of these methods."

---

## 6. Writing and talks

**6.1 Quantified, first-person history.** [stated] primary.

- OR02 p.3 (abstract): "It describes one person's perspective on the development of computational tools for linear programming." The quantitative aim is stated on p.4 ("as quantitatively as possible").
- [inferred] His talks from 2012 to 2022 are built from a fixed stock of dated, quantified case histories, retold with small variations:
  - the XMP test: OR02 p.3; OPT101 p.2; TOR21; SUBJ23; and HAUS22 p.11, which shows a handwritten 1986 table "LOPT" vs XMP;
  - LAU2/degen4: OR02 p.8; OPT101 p.3; HAUS22 pp.20–22; TOR21; SUBJ23;
  - the PDS growth curves: OR02 pp.8–10; GAP00 pp.4–6; COW15;
  - the CPLEX 1.0 re-run: ECCO17; HAUS22;
  - unit commitment in 1999: TOR21; SUBJ23;
  - the MIP version bars: DOC12; FIELDS12; ECCO17; TOR21.
  The variations are listed under Contradictions.

**6.2 Teach what the books leave out.** [stated] primary (COW15, 2015).

- "you are hard-pressed in finding in books description about how to implement the dual. People just don't talk about it."
- The aim: with the slides and a few references the students "should have the tools for making a reasonable implementation of the dual simplex algorithm".

**6.3 Unwritten work.** [stated] primary.

- OPT101 p.4 (2015), on shifting, which he calls his most important contribution: "There's no paper on this particular thing." And: "I talked about all the stuff. I just never got around to it."
- TR90-32 p.1 (1991) announces "the first in a series of papers describing different aspects of the CPLEX implementation of the simplex method". The later parts were to cover composite simplex in phase I, partial pricing, bound perturbation and vectorization. I found no later part (not searched exhaustively; agent 01/03).
- SUBJ23 (auto-caption): "people keep asking me to write a paper about the linear programming story", and "I might do that".

**6.4 Judge an idea apart from its prose.** [stated] primary. Count 2.

- COW15 part 3, on Paula Harris's papers (he dates them 1972; the Devex paper appeared in 1973): "She wrote a couple of papers in 1972, which were almost unreadable. But each has a very clever, nice idea." And: "So she knew what she was doing, she just didn't know how to write."
- SUBJ23 (auto-caption), on the Devex paper: "the paper is incomprehensible I never succeeded in reading this paper". He relied on Goldfarb's reading of it.

**6.5 Credit lines.** [stated] primary.

- OR02 p.14: "Zonghao Gu, Irv Lustig, Ed Rothberg, and Roland Wunderling have all made fundamental contributions to the CPLEX linear-programming algorithms." And: "Mary Fenelon, John Gregory, and Ed Klotz, while not contributing directly to these algorithms, deserve considerable credit for persistent and significant insights."
- He also credits the source of an analytical idea: by OR02 note 8 (p.14), the observation on how PDS solution times grow with model size (tested there with least-squares fits, pp.9–10) was suggested by Randy Batsell.

**6.6 Language and talk manners.** [stated] primary.

- SC92 p.21 (1992): "Ich möchte Robert Weismantel danken, daß er mir bei der Übersetzung dieses Aufsatzes aus dem Englischen behilflich war." My translation: thanks to Weismantel for help translating the paper from English.
- TOR21 (auto-caption) flags his own sales material: "i apologize this is a bit of a marketing slide".

---

## 7. Research organisation (time, teams, students, long-term agenda)

**7.1 Commitment through ownership.** [stated, self-report] primary. Count 2.

- OPT101 p.3 (2015): "I came to the conclusion that there was no way I could really get good people to be involved in this enterprise and be committed to it if I was just paying them a salary." He gave 49% to the Lowes.
- SUBJ23 (auto-caption) repeats it: they "had to have skin in the game".

**7.2 Build infrastructure for a research community.** [stated] primary. Count 4.

- The callable library: OR02 p.4; DOC12 p.116; OPT101 p.3; SUBJ23. The design brief, in SUBJ23 (auto-caption): the user only reports changes and the code reoptimizes in a smart way. The aim was integer-programming research; it "turned out to be exactly the right thing for business" (OPT101 p.3).

**7.3 Collaboration roles.** [stated, self-report] primary.

- In the TSP/Concorde team, after implementing Cook's strong-branching idea in CPLEX: "that's when they hired me as a as their hired LP gun" (SUBJ23, auto-caption). Roles in Concorde are otherwise undivided (team.json); context only.
- SUBJ23 praises Cook's credit ethic: a contributor "will get credit for it".

**7.4 Students.** Thin evidence.

- One stated case: "a graduate student of mine, Sanjay Saigal" (OPT101 p.3), whose degenerate problems forced perturbation into CPLEX.
- The status of co-authors Schwabacher (TR89-16), Lee (TR93-37) and McZeal (TR98-03) as his students is not established here (agent 04).
- No statement on how he supervised was found (Gaps G4).

**7.5 Company principles.** [stated] primary.

- CLIP20 (auto-caption, 2020) gives three Gurobi pillars:
  - "a single product we wouldn't be distracted by things like consulting and that we would push the performance frontier of this product steadily";
  - first-class support by experts in optimization;
  - flexible licensing.
- Also from CLIP20: "it's always been very important to us to try to hire the absolute best people we could find", and the decision "to make licenses free completely free for academics which was a way to long-term market penetration".
- OPT101 p.5, on the same decision: "But we didn't think about it very hard, we just did it."

**7.6 Integrity about academic positions.** [stated, self-report] primary.

- SUBJ23 (auto-caption): he gave up tenure rather than keep it while running a business, which he calls the habit of those who "kind of hold it hostage". In his words: "I didn't want to be one of those people".

**7.7 Teaching after leaving research.** [stated, self-report] primary.

- OPT101 p.6 (October 2015): a yearly course in Erlangen in computational linear and mixed-integer programming, "But I prove theorems." He added that he did no research any more, except a paper about presolve in Gurobi then being written (presumably ZR16-44 [inferred]).

**7.8 Division of labour at Gurobi.** [stated, self-report] primary.

- OPT101 pp.4–5: "No. Absolutely zero development. I did quite a bit of testing." He kept pestering the developers about bad behaviour. "What I really was interested in doing was running the business."
- OPT101 p.6 (October 2015), a dated self-description, not a present-role claim: "I manage the sales team and run the code all the time and complain like I always have."

---

## 8. Failures, abandoned directions and negative results he reports

- **No research funding** for LP computation, "zero success" (HAUS22 p.9; TOR21; SUBJ23). It led to the company.
- **First XMP test lost.** On the one model he had picked as favourable he was several times slower; XMP was "getting lucky on the starting basis" (OPT101 p.2). In SUBJ23 (auto-caption): "I carefully selected a problem from the list that I thought was the best suited", and "I was four times slower than XMP". OPT101 p.2: "I was crushed, absolutely crushed." The counts differ; see C1.
- **CPLEX 1.0 on degen4/LAU2** "failed miserably" (OR02 p.8) and was stuck in phase I (HAUS22 p.21).
- **Early CPLEX MIP lagged.**
  - OPT101 p.3: "But in the early versions, you could see that solvers such as MINTO were solving problem we couldn't solve." Presolve was weak.
  - OPT101 p.3: "We were competing against OSL at that point, and OSL was certainly better." They caught up in LP around 1992.
  - The airlines stayed with OSL until the must-have case (HAUS22 pp.18–19).
- **Parallel dual simplex, 1995** (SC95, co-authored):
  - PVM version "approximately 3.3 times slower than the sequential version!" (p.7);
  - the Sun S20-502 results "unexpectedly bad" (p.9);
  - the semaphore approach "probably not the right way" (p.11);
  - "all our attempts to separate the computations and perform them in parallel resulted in a degradation in performance" (p.17).
  - The 2012 verdict is broader still: "there has been essentially no success in parallelizing simplex algorithms" (DOC12 p.114). See C10.
- **Two-processor LP, 1989**: about 20%, sometimes not even that (TR89-16 p.5).
- **Sifting, 1991** (TR91-11, co-authored):
  - "Unfortunately, one of the weaknesses of the algorithm as implemented is that these sequences were determined by experimentation for the specific problem being studied." (p.7)
  - "No attempts at implementing a restart strategy along the lines of Lustig, et.al. [10] or Mitchell [13] were successful." (p.13)
- **Embedded networks, 1986** (TR86-18 p.1, co-authored): "in a sizable minority of cases, seemingly sophisticated algorithms find fewer network constraints than simpler and faster methods".
- **No paper on shifting** (OPT101 p.4); the 1991 CPLEX-simplex series was apparently not continued (§6.3).
- **His own slow fix.** Bound shifting took him "like two weeks" (OPT101 p.4) or "about a month" (COW15 part 3), see C5. In COW15: "I felt pretty stupid when I finally realized how simple it was."
- **MIP ideas at Gurobi** [stated, team]: "probably only one in ten ideas that get tried show really any promise whatsoever" (TOR21).
- **Others' failures he records:**
  - Dantzig and Orchard-Hays's first explicit-inverse code (DOC12 p.108);
  - MIP codes that "made MIP a viable practical tool for the first time, but they also helped create totally unrealistic expectations for what remained fundamentally a primitive technology" (DOC12 p.111);
  - "However, the dominance of these codes also led to stagnation in the field." (DOC12 p.115)

---

## 9. Era and resource context

| Period | Role and resources (his statements) | Bearing on the stated methods |
|---|---|---|
| 1972–c.1985 | Matroid theory; "Very theoretical research in OR" (HAUS22 p.9). | Taste for complete understanding of key work (§1.7); context only. |
| 1983–1987 | IBM PC classroom code (Fortran, then C); users' failing SLP models; no literature, no funding (OR02 p.3; OPT101 p.2; SUBJ23). | Origin of R7 and of the stability focus. Solo hobbyist. |
| 1987–1997 | Founder and principal simplex developer of CPLEX; tenured at Rice; Sun 3/50, Cray, SPARCstation, SGI; growing customer model library; Gu, Lustig, Rothberg, Wunderling join (OR02 p.14; OPT101 pp.3–4). | Most LP measurement rules (R1–R5, R17) date from here. A small company with access to proprietary models, which an academic group lacks. |
| 1997–2008 | ILOG; MIP rebuilt by Gu and Rothberg (CPLEX 6.5, 1998); he still did development in 1997 (OPT101 p.4); gave up tenure, retired from Rice in 2000 (SUBJ23). | MIP measurement (GAP00, the version chain) rests on team work and a large library. |
| 2008–2015 | Gurobi CEO; no development; tests and pesters (OPT101 pp.4–5). | Team pipeline of 200 machines (TOR21); his MIP lens is measurement and decision, not code. |
| after 2015 | Dated self-descriptions only: October 2015 (OPT101 p.6), 2021 (TOR21 bio, observed), and the 2023 upload (SUBJ23: research days "over"). | Not to be read as a present role (G1). |

Seniority filter [inferred]:
- Ignoring "no future" advice was affordable with tenure (§2.4).
- Measurement on 1,000–6,000 proprietary models and 200 test machines needs a commercial solver team.
- For an individual researcher, the transferable parts are the statistics (geometric means, censoring rules, size brackets, bias statements) and the test-set hygiene, not the scale.

---

## 10. Authorship and role labels, from his own dated statements

These labels must survive into the skill. Each rests on his own words or on a co-authored text, with the date.

| Date | Statement | Source |
|---|---|---|
| Dec 1989 | "The optimization routines in Cplex were written by Robert Bixby." (footnote of a co-authored report) | TR89-16 p.4 |
| Sept 1991 | the CPLEX simplex implementation, "the optimization routines for which were written by this author" | TR90-32 p.1 |
| Apr 1992 | "deren Hauptteile vom Author geschrieben wurden" (my translation: whose main parts were written by the author) | SC92 p.2 |
| Oct 1993 | "The simplex routines in CPLEX 1.0, and in subsequent versions of the software, were written by the author." The CPLEX 2.2 barrier was "written by Irv Lustig and Roy Marsten" (p.10); crossover: "This implementation is joint work of the author and Irv Lustig." (p.11) | TR93-40 pp.1, 10, 11 |
| 1988 (told 2015) | "The first release was in 1988, and at that time I was responsible for all of the development." | OPT101 p.3 |
| 1997 (told 2015) | "I was doing development and was still an academic at this point in time." | OPT101 p.4 |
| Gurobi (told 2015) | "No. Absolutely zero development. I did quite a bit of testing." | OPT101 p.4 |
| 2002 | Gu, Lustig, Rothberg and Wunderling made "fundamental contributions to the CPLEX linear-programming algorithms". | OR02 p.14 |
| told 2015 | Implemented the Suhl and Suhl LU factorization in CPLEX: "I did it, I just took that paper and implemented it." Bound perturbation, his implementation: "When I implemented this back in the old days I would only perturb variables that were in the basis." | COW15 part 3 |
| told 2015 | Shifting is "my most important contribution", derived from Harris's ratio test, which Fourer pointed him to. | OPT101 p.4 |
| told 2015 | Crossover: "And I had actually worked on crossover, making a couple of little observations that made it way faster." | OPT101 p.3 |
| 1992–2023 | Dual steepest edge is Forrest and Goldfarb's method, which CPLEX implemented: "version 1" (OR02 p.6 and note 7); "unit steepest-edge in [6]" (TR93-40 p.10); the Goldfarb-suggested variant (HAUS22 p.21; TOR21; SUBJ23). | as listed |
| 1991, 2022 | Sifting is Forrest's idea: "Its application for airline crew scheduling was proposed by John Forrest [4]" (TR91-11 p.1); "Developed algorithm called Sifting, an idea of John Forrest" (HAUS22 p.14). | as listed |
| told 2015 | MIP: "As far as the MIP stuff goes, basically I bask in the reflected glory for what was done by other people. I didn't do much on the MIP stuff." The cuts and most presolve were Gu's ("Gu was the one who really came in and implemented all of the cut stuff."; "Most of presolve."). Node presolve and probing were Rothberg's ("Ed put on the node presolve and started putting in the probing stuff."). Parallel barrier: "Ed's parallel barrier, which was the first parallel barrier". "However, the real contributions got made by Ed Rothberg and Gu." | OPT101 pp.3–4 |
| told 2015, 2023 | Strong branching: Cook's idea, which he implemented in CPLEX (OPT101 p.4; SUBJ23). | as listed |
| told 2023 | Early CPLEX MIP: "Mary fenan [Fenelon] was the person the developer who was primarily responsible for that with my assistance" (auto-caption). CPLEX 6.5: "I emphasize this was not me this was these two guys who did it" (Gu and Rothberg). On Gurobi's dynamic search: "I can't give you details a because I don't know all the details". | SUBJ23 |
| told 2015 vs 2023 | Callable library: "One thing I helped design was the callable library." (OPT101 p.3) versus, asked whether he coded the first version, "oh absolutely wow course I did" (SUBJ23, auto-caption). See C11. | as listed |
| 2012 | The Gurobi "MIP tricks" are team work ("Our trick", FIELDS12 p.19); not evidence of his code. | FIELDS12 |
| 2012, 2015 | He ran the measurements himself. The 2007 CPLEX version test: "I recompiled each of the corresponding twelve CPLEX released versions" and "I then ran each of the 1892 models" (DOC12 p.116). The "two days ago" run (COW15). | as listed |

Rule for the skill [inferred from the above]: a progress number measured on CPLEX or Gurobi is evidence of his **measurement** craft, not that he wrote the code that produced it. LP code authorship is his for CPLEX 1.0 and the simplex routines through 1993 by his own statements. After that, credit is shared or belongs to others as listed.

---

## Contradictions (kept, not reconciled)

**C1. The first XMP comparison.**
- OR02 p.3 (c.1986): "running on average two times faster than XMP" on "a substantial subset of the netlib" test set.
- OPT101 p.2 (2015): at first about seven times slower on standata, then "on almost all the models my code was four times faster".
- TOR21 (2021): "four times faster".
- SUBJ23: first "four times slower", then "like four times faster on all the problems".
- TR93-40 p.2 (1993), CPLEX 1.0 in late 1988: "about four times as fast as the XMP [14] simplex code and the then current version of MINOS [17]".
- OR02 p.11 (1988 Columbia talk, CPLEX 1.1 vs XMP): geometric mean 4.70.
- HAUS22 p.11 shows a handwritten "1st Public CPLEX Results -1986" table (LOPT vs XMP) in which LOPT is slower only on STANDATA.
- [inferred] Different code versions and model subsets may explain part of this; not reconciled.

**C2. Date, machine and name of the LAU2/degen4 attempt.**
- OR02 p.8: "In late 1989, degen4 was presented as a challenge problem", with CPLEX 1.0 run on a Cray **Y-MP**.
- OPT101 p.3: "Cray YMP", CPLEX "version 1.something or maybe 2".
- HAUS22 p.21: "1987 – Ran CPLEX 1.0 for 7 hours on Cray X-MP".
- TOR21: "going back to 1987 the first attempt i made to solve this model i made on a cray xmp".
- SUBJ23: "cray XMP".
- CPLEX 1.0 was released in 1988 (OR02 p.4), so the 1987 date conflicts [inferred].
- Same model under two names [inferred]: degen4 and LAU2 have identical sizes (4420 rows, 6711 columns, 101377 nonzeros; OR02 p.8 vs HAUS22 p.20).

**C3. Order of the dual story.**
- OR02 p.8, Table 3, checked on the page image (CPLEX 2.2 on a 667 MHz Compaq): barrier 125.8 s; primal on the explicit dual 33.4 s, already faster than barrier; dual with standard pricing 102.3 s; default dual 12.0 s. The text adds that standard-pricing dual was "significantly worse than simply applying the primal to the explicit dual".
- HAUS22 p.21, TOR21 and SUBJ23: the explicit dual was only "closer" to barrier, the standard dual "closer still", and only dual steepest edge beat barrier.
- The later accounts compare against OB1's 1,200 s on a Cray, the 2002 table against CPLEX 2.2 barrier. Not reconciled.

**C4. How the perturbation was built.**
- OR02 p.8 (degen4 test): lower bounds reduced by 1.0E-5 times a uniform [0,1] variable.
- SUBJ23: an epsilon of 10^-6, with the bounds of all nonbasic variables expanded.
- COW15 part 3: only basic variables perturbed at first, nonbasic ones when they enter the basis.

**C5. Time to find bound shifting.** "I struggled with this for like two weeks." (OPT101 p.4) versus "It literally took me about a month" (COW15 part 3).

**C6. Which release brought the hyper-sparse solves.**
- GAP00 pp.5–6: the 1999 work, CPLEX 6.5.
- OR02 pp.9–10, 12: CPLEX 7.1, with 5.0 "the last release prior to introducing a number of improvements for exploiting sparsity".
- COW15 part 3: "And then came along CPLEX8.0, which included that idea that I showed you."

**C7. Size of the CPLEX MIP version test set.**
- DOC12 p.116: 1892 models.
- ECCO17 p.30 and TOR21: 1852. ECCO17's own arithmetic (2791 − 559 − 348 − 22) gives 1862.

**C8. Gurobi version gains.**
- DOC12 p.118 and FIELDS12 p.8: 1.0→5.0 cumulative 16.2×, with 2.0→3.0 at 2.9×.
- ECCO17 p.36: 2.0→3.0 at 1.9×, cumulative 9.3× at 5.0.

**C9. Summary statistic, early and late.**
- TR90-32 p.19 (1991) averaged per-model ratios and only warned about ratios below 1. The text does not say which mean; arithmetic [inferred].
- From 2000 on he insists on geometric means. OR02 p.11: "A much better, more robust, and more conservative measure is the geometric mean of the individual ratios." TOR21: "you never want to take the arithmetic mean that's really misleading".

**C10. Parallel simplex.**
- SC95 p.20 (1995, co-authored), on the thread-based dual: "This implementation was far simpler than the previous two, and produced quite good results for a wide range of models."
- GAP00 p.12 (2000, co-authored): "No such parallelism appears to be available for the simplex algorithms."
- DOC12 p.114 (2012): "there has been essentially no success in parallelizing simplex algorithms".

**C11. The callable library.** He "helped design" it (OPT101 p.3, 2015) versus coding the first version himself (SUBJ23, auto-caption, 2023).

**C12. Authorship wording across 1989–1993.**
- "written by Robert Bixby" (TR89-16, co-authored footnote).
- "written by this author" (TR90-32, 1991).
- "Hauptteile", main parts (SC92, April 1992, German version).
- "simplex routines in CPLEX 1.0, and in subsequent versions" (TR93-40, 1993).

**C13. Founding year of CPLEX Optimization.** "we were incorporated in 1987" with the first release in 1988 (OPT101 p.3), versus "1988: Founded CPLEX optimization" (HAUS22 p.9). TOR21 and CLIP20 say 1988 (auto-caption).

**C14. First sale (Amoco).** "some time around 1986" (OR02 p.3) and "around 1986" (OPT101 p.3) versus 1987 (HAUS22 p.9; TOR21).

**C15. Asking Grötschel.**
- DOC12 p.117: "I would venture to say that if you had asked any of the top MIP researches in the field prior to that time if that would have been possible, they would have said no."
- TOR21 (auto-caption): "i asked martin gretchel actually before this did he think it would be ever be possible".
- SUBJ23: he has talked to Grötschel "about this very subject".

**C16. MINOS.** CPLEX 1.0 was "about four times as fast as" MINOS on netlib (TR93-40 p.2). OR02 pp.10–11 says instead that MINOS was significantly more stable than XMP and "somewhat faster (based upon comparisons I did at that time with CPLEX 1.0)".

**C17. Improvement totals.** DOC12 p.114 labels "Total improvement (3300 · 2000)" but tabulates 1600× for machines and 5,280,000× in total (3300 × 1600). HAUS22 p.28 gives 5,300,000×.

**C18. Outlook on modelling.** The modelling step remains "the roadblock" (SUBJ23). Yet "I'm less pessimistic about that last thing then if you had asked me four or five years ago" (SUBJ23, on LLM-drafted models). The 2021 talk (TOR21) frames the modelling skill as the hurdle, with no such hope.

**C19. Bibliographic.** The XMP paper is cited as "XMP: A structured library of subroutines for experimental mathematical programming" (OR02, DOC12) and as "The Design of the XMP Linear Programming Library" (TR93-40). Crossref has the latter, DOI 10.1145/355972.355976.

---

## Gaps (what I could not find or verify)

- **G1. Living status and present role.**
  - Not stated in this note.
  - New dated trace for the user: the long interview "Subject to: Robert Bixby" was uploaded 2023-12-07 06:58 UTC (6 December, US Pacific time). In it, the host calls Bixby's 1983 move "40 years ago", which places the recording in 2023 [inferred].
  - This is later than the September 2022 Hausdorff deck, which team.json treats as the latest dated trace. It does not settle the "living" key and must not become a present-role statement. His dated self-descriptions ("I'm retired now", "my research days are are over", SUBJ23) belong to that recording only.
  - A web-search summary claiming a 2024 title was not verified and is not used.
- **G2. Not read; no open copy reached.**
  - "Mixed-Integer Programming: A Progress Report" (2004, DOI 10.1137/1.9780898718805.ch18).
  - Bixby & Rothberg 2007 (DOI 10.1007/s10479-006-0091-y).
  - MIPLIB 2010 (DOI 10.1007/s12532-011-0025-9; the MPC/opus host returned a bot-check page).
  - The 1999 parallel-MIP paper (DOI 10.1023/a:1018960631213; CiteSeerX redirects to web.archive.org, not followed).
  - The published versions of ORSA J. Comput. 1992 and 1994 and INFORMS J. Comput. 2000 (preprints read instead: TR90-32, TR93-40, SC95).
- **G3. Not reached on 2026-11-05.**
  - DTIC (all report PDFs return an "Under Maintenance" page: ADA453079, ADA452700, ADA455431, ADA219013, ADA455195).
  - people.bath.ac.uk/masjhd/Others/Bixby2015a.pdf (redirects to the Bath homepage).
  - CiteSeerX (redirect to web.archive.org).
  - The Hausdorff slides folder listing (403). No other Bixby deck is linked on the school page, and three guessed MIP deck names returned 404.
  - The ZIB opus server shows an Anubis bot check to curl. WebFetch received the two report PDFs directly; no challenge was solved.
- **G4. No essay or lecture on how to do research, write or supervise.**
  - Layer 7 on students rests on one anecdote (Saigal).
  - Layer 6 rests on his practice of retelling cases and on two remarks about others' writing.
- **G5. Spoken sources are auto-captions** (TOR21, SUBJ23, CLIP20). Numbers such as "0.2" (TOR21) and names are unreliable; the meaning is used only where a written source agrees.
- **G6. Not searched**, for lack of budget: the 2013 Tutte Colloquium, FERC talks (the unit-commitment story), the CO@Work 2015 slides, the Waterloo honorary-doctorate citation, and talks after 2023.
- **G7. Homonyms excluded.**
  - A 2014 YouTube video titled "Robert Bixby" (AIMVideoLibrary) is a federal-budget talk by a different Robert Bixby.
  - "In Memory of Robert 'Bob' Bixby" (uploaded 2016-05-22, no captions) concerns a different person [inferred: the researcher gave dated talks in 2017, 2021 and 2022].
  - The 2011 Gurobi webinar "Improving the Performance of the Gurobi Optimizer" is by Greg Glockner.
- **G8. Repo tooling.** yt-dlp was not on PATH, so `scripts/download_subtitles.sh` could not run as is. yt-dlp 2026.10.26 was run through `uvx` instead (recorded in each transcript header).

---

## Sources

Primary, his alone, written:

1. OR02. R. E. Bixby, "Solving Real-World Linear Programs: A Decade and More of Progress", *Operations Research* 50(1):3–15, 2002. DOI 10.1287/opre.50.1.3.17780. Read in full (typeset copy https://www.gwern.net/doc/cs/algorithm/2002-bixby.pdf). Primary.
2. DOC12. R. E. Bixby, "A Brief History of Linear and Mixed-Integer Programming Computation", *Documenta Mathematica* Extra Volume ISMP (2012) 107–121. DOI 10.4171/dms/6/16. Read in full (https://www.maths.tcd.ie/EMIS/journals/DMJDMV/vol-ismp/25_bixby-robert.pdf). Primary.
3. SC92. R. E. Bixby, "Das Implementieren des Simplex-Verfahrens: Die Startbasis", ZIB Preprint SC 92-11, April 1992 (German; OCR layer). https://opus4.kobv.de/opus4-zib/files/81/SC-92-11.pdf, fetched with WebFetch. Read: Part I prose, Part II prose and results. Primary.
4. TR90-32. R. E. Bixby, "Implementing the Simplex Method: The Initial Basis", Rice University TR90-32, Oct 1990, revised Sept 1991 (Rice repository item 87f5f864-0f5b-4e56-ba18-babd83e56287). Published *ORSA J. Comput.* 4(3):267–284, 1992, DOI 10.1287/ijoc.4.3.267 (published text not read). Read: intro, netlib section, Part II, results. Primary.
5. TR93-40. R. E. Bixby, "Progress in Linear Programming", Rice TR93-40, Sept 1993, revised Oct 1993, hdl:1911/101811. Published as "Commentary—Progress in Linear Programming", *ORSA J. Comput.* 6(1):15–22, 1994, DOI 10.1287/ijoc.6.1.15 (published text not read). Read in full. Primary.
6. HAUS22. R. E. Bixby, "Linear Programming: A Historical View", slides, Hausdorff School on Computational Combinatorial Optimization, Bonn, Day 1 (school 12–16 Sept 2022; deck dated "Sept 2022"). https://www.or.uni-bonn.de/~held/hausdorff_school_22/slides/GUR_Hausdorff_Day1_LP_History.pdf. Read in full, including the image on PDF p.11. Primary.
7. ECCO17. R. E. Bixby, "Computational Progress in Linear and Mixed Integer Programming", ECCO 2017 invited lecture slides (PDF title "ECCO_Lecture_5May2017", 38 pp.). https://ecco2017.euro-online.org/en/resources/files/invited-speakers/robertbixby.pdf. Read in full. Primary.
8. FIELDS12. R. E. Bixby, "1000X MIP Tricks", slides, 12 June 2012, Fields Institute conference in honour of Bill Cunningham's 65th birthday. https://av.fields.utoronto.ca/programs/scientific/11-12/bc65/rbixby.pdf. Read in full. Primary (the tricks are Gurobi team work).
9. IMP15. Abstract of the seminar "Computational Progress in Linear and Mixed Integer Programming", Imperial College London, 13 May 2015. https://optimisation.doc.ic.ac.uk/?p=553 (also imperial.ac.uk/events/104423/…). Primary (speaker abstract, presumably supplied by him [inferred]).

Primary, his alone, spoken:

10. OPT101. "You have to figure out who your customer is going to be – An interview with Bob Bixby", *Optima* 101 (September 2016) pp.1–6. Questions by V. Kaibel, J. Lee and J. Linderoth, October 2015, Oberwolfach; transcribed from audio by N. Woyak and S. Heß. https://mathopt.zib.de/Optima-Issues/optima101.pdf. Read in full. Primary (spoken, transcribed by others).
11. COW15. "Robert Bixby: Solving Linear Programs: The Dual Simplex Algorithm", parts 1–3, CO@Work 2015 summer school, Zuse Institute Berlin. YouTube z1xvqwQR6xU, ZNf84y4M-Dw, uccbVoamiUM (uploaded 2016). Uploaded subtitles; transcript saved. Part 3 read in full, parts 1–2 skimmed. Primary.
12. TOR21. R. E. Bixby, "Optimization: Past, Present, Future", MIE Distinguished Seminar, University of Toronto, 19 March 2021. https://www.mie.utoronto.ca/?p=19855; https://www.youtube.com/watch?v=_R8-nt5NyiE. Auto-caption transcript saved, read in full including the Q&A. Primary.
13. SUBJ23. "Subject to: Robert Bixby", YouTube channel "Subject to", uploaded 2023-12-07 (UTC), 8,024 s. https://www.youtube.com/watch?v=47BZgFhEFJ8. Auto-captions read in full; excerpts saved. Primary.
14. CLIP15. "Bob Bixby States Importance Of Becoming a Good Listener and Giving Customer What They Want", Prendismo Collection, uploaded 2015-01-17. https://www.youtube.com/watch?v=8SUuT1swJTs. Primary.
15. CLIP20. "How was Gurobi founded?", Gurobi, uploaded 2020-04-08. https://www.youtube.com/watch?v=YoQ2h_G3PNM. Auto-captions. Primary.

Primary, co-authored:

16. SC95. R. E. Bixby, A. Martin, "Parallelizing the Dual Simplex Method", ZIB Preprint SC-95-45, December 1995. https://opus4.kobv.de/opus4-zib/files/211/SC-95-45.pdf, via WebFetch. Published *INFORMS J. Comput.* 12(1):45–56, 2000, DOI 10.1287/ijoc.12.1.45.11902 (published text not read). Prose read in full. Primary, co-authored.
17. TR91-11. R. E. Bixby, J. W. Gregory, I. J. Lustig, R. E. Marsten, D. F. Shanno, "Very Large-Scale Linear Programming: A Case Study in Combining Interior Point and Simplex Methods", Rice TR91-11, May 1991. Published *Operations Research* 40(5):885–897, 1992, DOI 10.1287/opre.40.5.885. Read in full. Primary, co-authored.
18. TR91-32. R. E. Bixby, M. J. Saltzman, "Recovering an Optimal LP Basis from an Interior Point Solution", Rice TR91-32, Oct 1991. Published *Operations Research Letters* 15(4), 1994, DOI 10.1016/0167-6377(94)90074-4. Introduction read. Primary, co-authored.
19. TR89-16. R. Bixby, M. Schwabacher, "Solving Linear Programs with Two Processors", Rice TR89-16, dated 1 December 1989. Read in full. Primary, co-authored.
20. TR86-18. R. E. Bixby, R. Fourer, "Finding Embedded Network Rows in Linear Programs I: Extraction Heuristics", Rice TR86-18 (July 1986). Published *Management Science* 34(3), 1988, DOI 10.1287/mnsc.34.3.342. Introduction read. Primary, co-authored.
21. TR91-38. R. E. Bixby, E. A. Boyd, R. R. Indovina, "A Test Set of Real-world Mixed Integer Programming Problems" (MIPLIB), Rice TR91-38, Nov 1991, revised Jan 1992. DTIC record DOI 10.21236/ada455431. Read. Primary, co-authored.
22. TR92-36. R. E. Bixby, E. A. Boyd, S. S. Dadmehr, R. R. Indovina, "The MIPLIB Mixed Integer Programming Library", Rice TR92-36, Nov 1992. Read. Primary, co-authored.
23. TR98-03. R. E. Bixby, S. Ceria, C. M. McZeal, M. W. P. Savelsbergh, "An Updated Mixed Integer Programming Library: MIPLIB 3.0", Rice TR98-03, Feb 1998, hdl:1911/101898. Also *Optima* 54 (1998) 12–15, as cited in GAP00's references. Read. Primary, co-authored.
24. GAP00. R. E. Bixby, M. Fenelon, Z. Gu, E. Rothberg, R. Wunderling, "MIP: Theory and Practice — Closing the Gap", in *System Modelling and Optimization* (19th IFIP TC7 Conference, Cambridge 1999), Kluwer 2000, pp.19–50, DOI 10.1007/978-0-387-35514-6_2. Preprint (PDF dated 30 March 2000) read in full at https://miplib2010.zib.de/miplib2003/paper/bixbyfenelongurothbergwunderling2000.pdf. Primary, co-authored.
25. ZR16-44. T. Achterberg, R. E. Bixby, Z. Gu, E. Rothberg, D. Weninger, "Presolve Reductions in Mixed Integer Programming", ZIB-Report 16-44 (December 2016), https://opus4.kobv.de/opus4-zib/frontdoor/index/index/docId/6037. Published *INFORMS J. Comput.* 32(2), 2020, DOI 10.1287/ijoc.2018.0857. Read: §1 including benchmarking, Table 1 text, §9. Primary, co-authored.
26. TR93-37. R. E. Bixby, E. K. Lee, "Solving a Truck Dispatching Scheduling Problem Using Branch-and-Cut", Rice TR93-37 (Sept 1993). Published *Operations Research* 46(3):355–367, 1998, DOI 10.1287/opre.46.3.355. Introduction read. Primary, co-authored.

Secondary, observed and metadata:

27. M. Grötschel, "Comments on Bob Bixby's interview: Mathematics and the Real World", *Optima* 101 pp.6–7. Observed.
28. W. Cook, "Comments on Bob Bixby's interview: Beauty in the Details", *Optima* 101 p.7. Observed.
29. University of Toronto MIE event page (posted 19 March 2021), https://www.mie.utoronto.ca/?p=19855: abstract and bio. Observed and metadata.
30. Berkeley IEOR advisory-board page "Bob Bixby" (published and modified 2018-09-12), https://ieor.berkeley.edu/advisory_board/bob-bixby/. Observed (dated bio).
31. Lehigh ISE newsletter 2015, p.4: event record of the Spencer C. Schantz Lecture, 24 Sept 2015, "Computational Progress in Linear and Mixed Integer Programming" (no content). Metadata.
32. Hausdorff School 2022 programme page, https://www.or.uni-bonn.de/~held/hausdorff_school_22/. Metadata.
33. YouTube metadata (yt-dlp, 2026-11-05) for sources 11–15 and the excluded videos. Metadata.
34. OpenAlex works for author A5012463224 (84 works) and their open-access locations. Metadata.
35. Unpaywall (email nuwa-skill@users.noreply.github.com) and Crossref API checks of the DOIs in this list. Metadata.
36. Rice University repository (DSpace API) search "author:Bixby" (18 items) and item records. Metadata.
37. ZIB MIPLIB 2003 bibliography page, https://miplib2010.zib.de/miplib2003/biblio.html (host of the GAP00 preprint). Metadata.
38. ZIB opus front door, docId 6037 (record of ZIB-Report 16-44). Metadata.

Checked and excluded: see G7 (two homonym videos and one webinar by Greg Glockner).

External papers named above, identifiers checked on Crossref in this run:

- Forrest & Goldfarb 1992, *Math. Programming* 57:341–374, DOI 10.1007/bf01581089.
- Gilbert & Peierls 1988, *SIAM J. Sci. Stat. Comput.* 9:862–874, DOI 10.1137/0909058.
- Suhl & Suhl 1990, *ORSA J. Comput.* 2:325–335, DOI 10.1287/ijoc.2.4.325.
- Harris 1973, "Pivot selection methods of the Devex LP code", *Math. Programming* 5:1–28, DOI 10.1007/bf01580108.
- Megiddo 1991, *ORSA J. Comput.* 3:63–65, DOI 10.1287/ijoc.3.1.63.
- Lustig, Marsten & Shanno 1994, *ORSA J. Comput.* 6:1–14, DOI 10.1287/ijoc.6.1.1.
- Marsten 1981, "The Design of the XMP Linear Programming Library", *ACM TOMS* 7:481–497, DOI 10.1145/355972.355976.
- Achterberg & Wunderling 2013, "Mixed Integer Programming: Analyzing 12 Years of Progress", in *Facets of Combinatorial Optimization*, pp.449–481, DOI 10.1007/978-3-642-38189-8_18 (named only because ZR16-44 credits its reporting form to it; not read).

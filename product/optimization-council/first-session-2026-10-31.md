# Optimization Council · Session 2026-10-31: The price of exactness

> **Simulated discussion.** This is a simulated discussion using research methods distilled from the public work of Dimitris Bertsimas and the seated members of the LP, NLP, DFO and MINLP teams (Qi Huangfu; Nicholas I. M. Gould, Jorge Nocedal and Stephen J. Wright; Luís Nunes Vicente, Charles Audet and Andrew R. Conn; Nikolaos V. Sahinidis, Samuel Burer and Santanu S. Dey), not their actual opinions. It ran in autopilot: checkpoints 1–3 were skipped, and checkpoint 4, approval of the plan below, is the user's. The first run gave the four seated challengers no turn; their turns (Sahinidis on items 1 and 2, Conn on item 3, Dey on item 4) were run afterwards with each item's record in hand, and the plan was revised (v2) and signed again.

## Problem Card

**Session topic:** The price of exactness: when does an exact, certified answer pay for its computation, and what may the claims "now tractable", "certified" and "robust" rest on? (one claim per guest team: LP, NLP, DFO, MINLP)

**Topic (agenda mode):** The price of exactness. Each item sets one claim this lens makes against one guest team's documented counter-standard, and ends in a deciding test: a "why now" speed-up (LP), the statistical value of a certificate (NLP), a robust design on a simulator (DFO), a stronger conic relaxation (MINLP). Framing [inferred transfer]: Method 3's "price of X" applied to exactness itself. The yardstick is the 2019 book's joint principle, practical tractability rather than polynomial solvability [B009 p. 1].

- **Goal:** a programme plan that ties each claim to the measurement allowed to support it, and to one deciding test that can run on the papers' own or on public instances. Done means: every item closed with its deciding test, the stage it stops at and the user's decisions; the plan approved at checkpoint 4, with dissents recorded verbatim.
- **Resources:** none stated (assumed). The council designs the tests and does not run them. A run needs one machine, named solver releases, the papers' instances and public libraries (MINLPLib and QPLIB, both in the council's Shared References).
- **Constraints:** a simulated discussion built from distilled public methods; no invented numbers; nothing from private folders; nothing called optimal or certified without a proof; fault lines cited only as FL1–FL6.
- **Evidence at hand:** the members' skills, paper cards and notes; FL1, FL2, FL4 and FL5 with their deciding tests; the §6 meeting points of the lead's IO, ML, RO, HS, CP and LO domain files.
- **Already tried:** no card shows any of the four deciding tests run. No card measures either speed-up factor on a statistics class (FL1). No card on either side cites the other on certifying estimators (FL2). Robust local search and bilevel DFO were never run head to head (FL4; HS §6.1). No RPT run on public libraries at current releases goes beyond Dey's n ≤ 10 ground truth (FL5).
- **Stakes:** low and reversible (assumed). This is a research agenda: being wrong costs an over-claimed paper or wasted effort, not a deployed decision.
- **Domains:** IO is primary (the engine of items 1, 2 and 4), then ML, CP, RO, HS, LO. SD and DA are not on the agenda; AP appears only as item 3's testbed.
- **Class and size:**
  - (1) best-subset MIQO on the paper's synthetic designs and Diabetes data, n = 350, p = 64 [S010 pp. 11, 26];
  - (2) cardinality-constrained estimators: sparse regression at (p, k) = (2,000, 10) with SNR 6, 1 and 0.05 [S095 p. 11] *(citation not confirmed: card S095 lists SNR 6, 1, 0.05 and (2,000, 10) unpaired for Table 2; the paper, p. 11, runs (2,000, 10) only at SNR 0.05)*, and inverse covariance at p ≤ 200 with n = p [S288 pp. 16–17] *(citation not confirmed: card S288 gives p = 200 with n = p at pp. 16–17; p ≤ 200 is the App. C range, pp. 29–30, where n varies)*;
  - (3) an unconstrained robust nonconvex design: Example I, a two-dimensional polynomial with Γ = 0.5 [S090 p. 8], with the 100-variable electromagnetic design as an option [S090 pp. 9–12];
  - (4) nonconvex QCQP and polynomial problems, with and without integers, at n ≥ 20, plus QPLIB and MINLPLib instances.
  - Gaps and limits so far: per item, from the cards.
- **Data and uncertainty:** synthetic designs with known truth over an SNR grid, plus real data (items 1–2); implementation errors in an ℓ2 ball (item 3); evaluations deterministic (assumed). In item 3 gradients are withheld and each finite-difference gradient is charged n calls.
- **Decision or prediction:** no decision owner (assumed). By this lens's default, each item's baseline is its incumbent: the borrowed factor (1); the ℓ1 path, glmnet and Glasso (2); random sampling, with the exact-gradient search as a reference line (3); BARON and SCIP at defaults (4). Each claim is scored on its own metric: (1) the measured factor; (2) out-of-sample error and FDR against time; (3) the enumerated worst case against calls; (4) exact count and gap against time.
- **Guarantee needed:** a certified gap at a stated limit (items 1, 2, 4). In item 3, a worst case enumerated on a fine mesh; otherwise the method is labelled a heuristic.
- **Solver, compute and data:** one machine, with threads and releases named at run time (assumed). Items 1 and 2 need a commercial MIO solver (Method 4, Limitations). On the electromagnetic design the adjoint gives gradients at no extra cost [S090 pp. 2, 11], so item 3 withholds them by design.
- **Question for the user (one):** should the plan budget actual runs of these deciding tests on your machine and solver licences, or only design them?

## Agenda and seats

Agenda mode under the [council roundtable](council-roundtable/SKILL.md): four items, one claim per guest team. The fault lines FL1–FL6 and their deciding tests are in the roundtable's [Step 3](council-roundtable/SKILL.md#step-3--cross-examination-member-agents-13-rounds).

| # | Item and question | Codes | Delegates | Challenger | Fault line |
|---|---|---|---|---|---|
| 1 | **What may a "why now" speed-up rest on?** Can the case that exact MIO is now practical rest on a solver × peak-hardware product with the MIQO factor only asserted? Or must the class be timed across solver releases and thread counts on one machine, with net gains printed beside self-relative ones? | IO, ML (LO for the conceded 1994 context) | [Huangfu](../lp-team/qi-huangfu/SKILL.md) (lp-team), [Gould](../nonlinear-team/nicholas-i-m-gould/SKILL.md) (nonlinear-team) | [Sahinidis](../minlp-team/nikolaos-v-sahinidis/SKILL.md) | FL1 (also LO §6, point 1: the 1994 "fastest" claim from operation counts) |
| 2 | **What does proof time buy a statistical estimator?** Once the warm-started incumbent stops changing, does the time spent proving optimality buy any out-of-sample gain in selection or likelihood? The comparison is against ℓ1 paths and first- or second-order methods stopped at tolerances matched to the statistics. If it does, at which size, noise level and correlation? | ML, IO | [Nocedal](../nonlinear-team/jorge-nocedal/SKILL.md) (nonlinear-team), [Wright](../nonlinear-team/stephen-j-wright/SKILL.md) (nonlinear-team) | [Sahinidis](../minlp-team/nikolaos-v-sahinidis/SKILL.md) | FL2 (also ML §6.2, point 8, the ℓ1 school; ML §6.1, point 1, the 2020 sparse-regression discussion with Sahinidis's group: recorded in both teams' notes, on no card) |
| 3 | **What may a stopped robust search on a simulator claim?** With gradients withheld, should the inner worst case be estimated by short ascents plus a history set, or solved to a tolerance tied to the outer radius? And what may a stopped run claim about its design's worst case? (On the electromagnetic design the adjoint gives gradients free [S090 pp. 2, 11], so the two methods compete only where gradients are unobtainable or charged.) | RO, HS (AP: the electromagnetic design as testbed) | [Vicente](../dfo-team/luis-nunes-vicente/SKILL.md) (dfo-team), [Audet](../dfo-team/charles-audet/SKILL.md) (dfo-team), [Nocedal](../nonlinear-team/jorge-nocedal/SKILL.md) (nonlinear-team) | [Conn](../dfo-team/andrew-conn/SKILL.md) | FL4 (also HS §6.1, the Conn-with-Vicente point and "Vicente · what a heuristic may claim"; RO §6.3) |
| 4 | **Where do heavier conic rungs stop paying?** Do all-pairs RPT products and the LMI certify more per second than three cheaper options: RLT alone, products selected by structure, or a cheaper outer approximation? The comparison is against current BARON and SCIP releases at defaults, beyond n = 10, on public QPLIB and MINLPLib instances and not only the RPT papers' own families. | CP, IO | [Sahinidis](../minlp-team/nikolaos-v-sahinidis/SKILL.md) (minlp-team), [Burer](../minlp-team/samuel-burer/SKILL.md) (minlp-team) | [Dey](../minlp-team/santanu-s-dey/SKILL.md) | FL5 (also CP §6.2, the Sahinidis and Dey points; IO §6, "Sahinidis · global solver benchmarks") |

**Why these seats** (from the frame): Seats follow the seating rows each item matches, in the order listed. Row 1 (a speed-up number carries the case) gives Huangfu and Gould, with Sahinidis as challenger. Row 4 (an estimator solved exactly as an MIO) gives its first two delegates, Nocedal and Wright, again with Sahinidis as challenger. Rows 7 (robust design of a simulator) and 9 (what a stopped heuristic run may claim) both name Vicente and Audet, so they are preferred; row 7 adds Nocedal and its challenger, Conn. Row 11 (a certified global optimum, with conic relaxations against a global solver) gives Sahinidis and Burer, with Dey as challenger. Each seat fits its member's "Leads when" field: Huangfu, LP solver benchmarks and new hardware; Gould, benchmark design; Sahinidis, a solver benchmark being designed and node relaxations chosen with cost in mind; Nocedal, a new method claiming to beat the incumbent and finite-differenced derivatives; Wright, judging benchmarks; Vicente, a trusted heuristic without guarantees; Audet, expensive nonsmooth blackboxes; Conn, bilevel or robust structure; Burer, relaxation strength; Dey, ranking relaxations and certifying a dual bound. Each guest team therefore meets the lead on its own documented fault line, each at a different convener stage: LP on FL1 (measured tractability), NLP on FL2 (certificate against statistical accuracy), DFO on FL4 (what a stopped run may claim), MINLP on FL5 (tractability of stronger relaxations). That makes ten distinct delegates: Huangfu (LP); Gould, Nocedal and Wright (NLP); Vicente, Audet and Conn (DFO); Sahinidis, Burer and Dey (MINLP). Sahinidis sits three times because rows 1, 4 and 11 all name him, and his yardstick (whole public libraries, certified optima, default settings) is shared by items 1, 2 and 4. Nocedal sits twice (rows 4 and 7). The code check yields optional adds only; none is seated, to stay at ten. Item 2's ML also engages DFO: `add Scheinberg`, since ML §6.3 puts her ℓ1 inverse-covariance method in the §6.2 test. Item 3's RO also engages MINLP: `add MINLP` ties Leyffer and Sahinidis at their RO §6.2 points, for the user to pick; row 9's Powell is also left out. Item 4's CP also engages NLP: `add Wächter` (CP §6.1: ablate the Ipopt polishing inside RPT-BB). Two rows are not matched. Row 12 does not apply because item 4's relaxations certify inside a branch and bound rather than grade a heuristic or pick a method by complexity. Row 13 does not apply because item 2 asks whether to wait for the proof, not how to move the bound. FL3 and FL6 (Curtis, Wächter, Misener) wait for a later session. Caveats: Conn is a historical lens; Huangfu's gate reaches MIO only by an inferred translation, since MIP is outside his record; and the lead's side of item 4 rests on co-authored work in which his share is not identified [S377 p. 1]. Expected cost with one cross-examination round per item: 39 agent calls (17 openings, 11 cross-examination, 1 programme plan, 10 sign-offs).

**Seated lenses**

- **[Bertsimas lens]**, lead and convener: [dimitris-bertsimas](dimitris-bertsimas/SKILL.md), with its [Domain Map](dimitris-bertsimas/SKILL.md#domain-map) and the domain files this agenda draws on: [IO](dimitris-bertsimas/references/domains/02-IO-integer-mixed-integer.md), [ML](dimitris-bertsimas/references/domains/06-ML-machine-learning-statistics.md), [CP](dimitris-bertsimas/references/domains/04-CP-convex-conic-moment.md), [RO](dimitris-bertsimas/references/domains/03-RO-robust-adaptive.md), [HS](dimitris-bertsimas/references/domains/08-HS-heuristic-simulation.md), [LO](dimitris-bertsimas/references/domains/01-LO-linear-optimization.md) and [AP](dimitris-bertsimas/references/domains/09-AP-applications.md).
- **[Huangfu lens]** (LP Team), item 1: [qi-huangfu](../lp-team/qi-huangfu/SKILL.md).
- **[Gould lens]** (NLP Team), item 1: [nicholas-i-m-gould](../nonlinear-team/nicholas-i-m-gould/SKILL.md).
- **[Nocedal lens]** (NLP Team), items 2 and 3: [jorge-nocedal](../nonlinear-team/jorge-nocedal/SKILL.md).
- **[Wright lens]** (NLP Team), item 2: [stephen-j-wright](../nonlinear-team/stephen-j-wright/SKILL.md).
- **[Vicente lens]** (DFO Team), item 3: [luis-nunes-vicente](../dfo-team/luis-nunes-vicente/SKILL.md).
- **[Audet lens]** (DFO Team), item 3: [charles-audet](../dfo-team/charles-audet/SKILL.md).
- **[Conn lens]** (DFO Team), item 3 challenger, a historical lens; turn in the [Challengers' round](#challengers-round): [andrew-conn](../dfo-team/andrew-conn/SKILL.md).
- **[Sahinidis lens]** (MINLP Team), item 4 delegate; challenger on items 1 and 2, with turns in the [Challengers' round](#challengers-round): [nikolaos-v-sahinidis](../minlp-team/nikolaos-v-sahinidis/SKILL.md).
- **[Burer lens]** (MINLP Team), item 4: [samuel-burer](../minlp-team/samuel-burer/SKILL.md).
- **[Dey lens]** (MINLP Team), item 4 challenger; turn in the [Challengers' round](#challengers-round): [santanu-s-dey](../minlp-team/santanu-s-dey/SKILL.md).

## Discussion

Each item gives the lead's opening, the delegates' openings, the lead's reply to the strongest challenge and the rejoinders, verbatim under their lens labels, with the field names set in bold. The verifier's findings are inserted in italics, *(unverified)* and *(citation not confirmed: …)*; nothing was removed (see [Verification](#verification)). A bare bracket such as [S010 p. 2] cites the speaker's own card; a bracket naming a folder, such as [jorge-nocedal card S004 arXiv p. 3], cites that member's card.

### Item 1 · What may a "why now" speed-up rest on?

*Codes:* IO, ML (LO for the conceded 1994 context) · *Delegates:* Huangfu (LP Team), Gould (NLP Team) · *Challenger:* Sahinidis (turn in the [Challengers' round](#challengers-round)) · *Fault line:* FL1 (also LO §6, point 1: the 1994 "fastest" claim from operation counts)

#### Openings

**[Bertsimas lens, lead]** Could stop at: measured tractability (fix: time the class, or call the figure borrowed). A "why now" is a solve time measured on the class at the application's scale; a product of borrowed factors is context, not evidence. Conceded: best subset's arXiv v1 leads with 200 billion, Bixby's MILP factor times Top500 peak, the MIQO factor asserted as "similar", the runs on 8- and 16-core Xeons [S010 pp. 1, 7–8, 27]; his 1994 "fastest" rested on operation counts, Vaidya's algorithm untested [S269 pp. 1, 22] (C19). Held: tractability means realistic sizes in application times [S010 p. 2], and the body times the class: Diabetes optima in seconds, certificates in 10–20 minutes [S010 p. 11] (→ Method 2 checkpoint). Huangfu's net-gain gate [qi-huangfu SKILL.md, "Method 4 · Efficient-baseline gate"] asks for the run Method 2's checkpoint requires. Test: FL1's, time to best printed apart from time to proof [S095 p. 5].

**[Huangfu lens]**

**POSITION:** Agree: a borrowed product is context; time the class. Refine "net". Timing across versions, as his Method 2 checkpoint asks, measures the solver against its own past: net only where the old release was the best code for the class. For subset selection around CPLEX 8.1 it was not: his group's 2009 tailored branch and bound outran CPLEX's general MIQP [dimitris-bertsimas card S040 pp. 10–12], a code that S010 calls less scalable, with no run on the card [dimitris-bertsimas card S010 p. 5]. A big factor over a beaten base is this lens's warning sign 1. Bixby's 29,000 is a chain: eleven version-pair geomeans multiplied into "a projected" factor, joined to Gurobi's via a 2009 benchmark [Bixby 2012, pp. 116–118, read]. Diabetes (p = 64) shows standing; the headline scale, n in the 1000s and p in the 100s, is untabulated [dimitris-bertsimas card S010 pp. 1, 6, 11, 30–31].

**WHY (method refs):** (→ Huangfu · Method 4) net beside self-relative: PAMI 1.51 against 2.34 [MPC pp. 138–140]; re-measured by Hall in HiGHS on another 40-LP set, 1.16 against 1.88 [qi-huangfu note 05 §4; KTH21 slides 25–26, read]. A factor does not carry across bases, sets or classes (warning sign 6: MILP for MIQO). (→ Method 2, step 6) path-changing variants print iterations and time per iteration apart; that slide splits the 1.16 into 0.98 × 1.18. (→ Method 5, Limitations) memory bandwidth, not peak flops, bounded his gains [HiGHS Parallelism docs, read]. (→ H5) count the funnel. MIP is outside his record [qi-huangfu SKILL.md, Research Task Routing], so every MIO step here is (inferred).

**FIRST EXPERIMENT / DECIDING TEST:** FL1's deciding test, plus: (1) a net arm on the same machine with the best earlier exact methods: the 2009 branch and bound rebuilt from its printed algorithm (→ H3) [dimitris-bertsimas card S040 pp. 2–7] and leaps (CRAN 3.2, checked); (2) in (a), the direct oldest-to-newest ratio beside the product of consecutive pairs, with the funnel counted per pair; (3) per run, nodes and time per node, and time to best apart from time to proof [dimitris-bertsimas card S095 p. 5]; (4) in (b), the gain over the best one-thread run beside the self-relative one, against an Amdahl-plus-bandwidth ceiling fixed before the runs (→ Method 5); (5) the synthetic designs at the headline scale beside Diabetes, with the losers named. Stop rule (→ Workflow E checkpoint): a factor that shrinks on the class or after rescaling is downgraded, and the abstract carries the measured one.

**RISK — WHERE I COULD BE WRONG:** MIP is outside his record, so these translations may not fit branch and bound. "Similar" may hold, and the net arm may confirm a large move. Old releases may not run on one machine, and a rebuilt 2009 code is not the original. His own record falls short of this standard: a blog headline of "a factor of two" beside a repost's 30% on average, and Cplex run without presolve or crash [qi-huangfu SKILL.md, Inner Tensions, Tension 2; Method 4, Limitations].

**QUESTION FOR USER:** Which MIO solver releases, oldest to newest, can you license and run on one machine?

**[Gould lens]**

**POSITION:** Agree, but narrow "timing the class": a why-now claims change, so only then-against-now runs changing one thing in one harness carry it (→ Gould · Method 4). S010's one-change runs (warm against cold, tuned against default) keep Gurobi 5.5 fixed [dimitris-bertsimas card S010 pp. 11, 27–32], pricing the paper's choices, not solver or hardware. MIQO lies outside Gould's evidence; inferred transfer.

**WHY (method refs):** One mechanism changed; same code, stopping rules, hardware (→ Gould · Method 4). Hardware enters as size, the lead's yardstick [dimitris-bertsimas card S010 p. 2], not a multiplier: the SIF log raised default sizes with hardware in 2002 [03 §2.2] (→ Gould · Method 2).

**FIRST EXPERIMENT / DECIDING TEST:** FL1's deciding test, as argued, plus a warm-start on/off arm per release, identical stopping rules, frozen seeded instances; per arm, the largest synthetic p certified to the gap within the limit; profiles pairwise or best-removed (→ Gould · Methods 2, 4). Only arms that raise that p may be credited.

**RISK — WHERE I COULD BE WRONG:** One vendor's release series, a same-harness test, flatters that code (→ Gould · Method 4, Limitations); this lens's own why-nows were stated motives, not measured factors [03 §7b; 02 P4].

**QUESTION FOR USER:** If runs are budgeted: which MIO solver releases, by year, can you still run?

#### The lead's reply

**[Bertsimas (lead), reply lens]**

**POSITION:** Strongest challenge: Huangfu's. Conceded: a release series prices the solver against its own past, and on subset selection that past lost to our 2009 branch and bound. It solved all five (100, 80) instances in 8 minutes on average, while CPLEX left three of five unsolved in an hour [S040 p. 12]. S010 calls that code less scalable without running it [S010 p. 5]. The 580,000 is a chain [S010 pp. 7–8], and the headline scale has no table [S010 pp. 1, 6, 30–31] (a Blind spot of mine). Held: that CPLEX ran depth-first on big-M with M = 100 and was never shown at defaults [S040 p. 10] *(citation not confirmed: card c12 gives the big-M model with M = 100, but its depth-first line does not say it applied to CPLEX; the paper text, p. 10, does)*. The measured case is absolute: Diabetes was certified in 10–20 minutes by the big-M-free formulation (8) [S010 pp. 10–11] *(citation not confirmed: formulation (8) is named in the paper's Figure 2 caption, p. 11, not on card c16, which notes that the certified runs do not say which bounds they used)*. The change claimed is certification [S010 pp. 5, 8] *(citation not confirmed: card c16 places the suboptimality-guarantee claim at S010 pp. 1 and 6)*, which was the 2009 code's bottleneck [S040 p. 13]. Score: Gould's certified frontier. Stops at: measured tractability.

**WHY (method refs):** (→ Bertsimas · Method 2, checkpoint) Time the class across versions, or call the figure borrowed. S010 reports its times "to show that it is computationally tractable", not to benchmark [S010 p. 32] *(citation not confirmed: the quoted words are in the paper text, p. 32, not on card c16)*, and the rebuild in step 3 is this skill's rule (C6). (→ Method 1) The model may be what changed. S040 blamed CPLEX's loss on big-M [S040 p. 12], and S010 replaced big-M with SOS-1 or data-derived bounds [S010 pp. 10, 13–17]. A release factor taken across formulations therefore credits the solver with the formulation's gain. (→ Method 4) Every arm must certify the same problem: warm-start big-M certifies only the bounded one [S010 p. 17]. Huangfu's own limitation applies to his evidence: run at parity and at defaults, both [qi-huangfu SKILL.md, "Method 4 · Efficient-baseline gate", Limitations]. Gould's point accepted: one change per arm [nicholas-i-m-gould SKILL.md, "Method 4 · Same-harness controlled experiments on mid-run instances"], with hardware entering as size [same SKILL.md, "Method 2 · Keep the test set, and its summary statistic, as a maintained instrument", step 5], which is my yardstick [S010 p. 2].

**FIRST EXPERIMENT / DECIDING TEST:** FL1's deciding test, as argued, with Huangfu's five additions and Gould's warm-start arm, plus three of mine.

(i) One problem: every arm certifies (1) itself, through formulation (8) or provable bounds [S010 pp. 10, 15–17].

(ii) A formulation arm: the oldest and the newest runnable releases, each on the big-M form S040 gave CPLEX (M made provably valid) and each on (8), at defaults and at S040's depth-first, max-|value| branching settings [S040 p. 10].

(iii) The 2009-era arms are scored on proof. The rebuilt 2009 code prints its global bound; its depth-first search left the root bound in place for most nodes [S040 p. 16]. leaps 3.2 (on CRAN, checked) runs across p, to test S010's "p ≤ 30" [S010 p. 5].

Score per arm: the largest p in S010's Example 1 at n = 1000, grown from the unreported p = 50 runs, on its ρ and SNR grid [S010 pp. 26, 30–31] *(citation not confirmed: card c16 gives the unreported n = 1000, p = 50 runs, pp. 30–31, but not that they were Example 1; the paper text, p. 30, does)*. That p must reach a 1% gap within 15 minutes for every k from 5 to 25, S010's own path rule [S010 p. 32] *(citation not confirmed: card c16 gives the per-k rule, a 1% gap or 15 minutes, at pp. 31–32, but not the range k = 5 to 25, which is in the paper text, p. 32)*. Print time to best apart from time to proof.

Settle rule: credit an arm (release, threads, formulation, warm start) only if it moves that frontier.

- If the 2009 code reaches the newest release's frontier, "less scalable" is withdrawn.
- If (8) on the oldest release moves the frontier as far, the why-now belongs to the formulation.
- Otherwise the abstract carries the frontier and the net factor measured there, with the product labelled borrowed.

**RISK — WHERE I COULD BE WRONG:** The frontier depends on a time limit no owner has set (assumed: the paper's own). A rebuilt 2009 code is not the original. Its wins came on random, unconstrained regression, chosen "to highlight the merits of our tailored approach" [S040 p. 7] *(citation not confirmed: card c12, like the paper, p. 7, ties the quoted words to keeping regression unconstrained; the random data, p. 10, are not said to be chosen)*, so they may not carry to S010's designs, in either direction. The certified frontier may fall short of the abstract's "n in the 1000s and p in the 100s" in minutes [S010 pp. 1, 6] *(citation not confirmed: card c16 gives the headline certified scale, pp. 1, 6, but not that it is claimed in minutes; the paper text, pp. 1, 6, does)*. Then the claim narrows (Workflow E checkpoint), and the era-bound evidence of Method 2 (Limitations) loses its best case. Old releases may not run, or may not be licensable, on one machine.

**QUESTION FOR USER:** Which time limit defines "tractable" for the frontier: S010's 1% gap or 15 minutes per k, or one you set?

#### Rejoinders

**[Huangfu, rejoinder lens]**

**POSITION:** Accepted: formulation arm, parity plus defaults, proof-scored then-arms. Concede: S040 ran CPLEX depth-first [dimitris-bertsimas card S040 p. 10] *(citation not confirmed: card c12's depth-first line does not say it applied to CPLEX; the paper text, p. 10, does)*, so my "beaten base" awaits a defaults rerun. Contest: in his "otherwise" branch then-arms, by definition, fail cells at the newest frontier: "the net factor measured there" is censored.

**WHY (method refs):** (→ Huangfu · Workflow E, checkpoint, steps 1, 5; Method 4, step 4) Parity only at defaults; net only against the strongest earlier code; one verdict per arm (MIO: inferred).

**FIRST EXPERIMENT / DECIDING TEST:** The lead's, plus: per arm, geometric-mean time ratio to the 1% gap against the strongest then-arm where both reach it, else bounds; moving the frontier or that ratio alone earns context-only. First (→ H3), the rebuild proves S040's proved cells within its limits [dimitris-bertsimas card S040 pp. 11–12, 17–21].

**RISK — WHERE I COULD BE WRONG:** S040 names no machine or instance generator [dimitris-bertsimas card S040 pp. 10, 22] *(citation not confirmed: card c12 says no machine is stated, not that no instance generator is named; the paper text, p. 10, supports it: X and β only 'randomly generated')*, so that check is one-sided; the strongest-then denominator may understate change.

**[Gould, rejoinder lens]**

**POSITION:** Accept: one change per arm; credit only for moving the certified frontier (→ Gould · Methods 2, 4). Contest: a losing 2009 arm confirms the less-scalable verdict only if reproduced and fairly armed; and Example 1 is random data, which S040 says "may give unrealistically optimistic running times" [dimitris-bertsimas card S040 p. 13]. MIQO: inferred transfer.

**WHY (method refs):** (→ Gould · Method 5, steps 2–3, 6.3) a doubted method gets its best variant, reproduced first; S040 names depth-first search among its limits [dimitris-bertsimas card S040 p. 16]. (→ Method 2, steps 1, 4) freeze a non-random set first [02 J2].

**FIRST EXPERIMENT / DECIDING TEST:** The lead's, plus: (1) the rebuild must first reproduce S040's machine-independent node counts in the (d, K) cells S040 solved [dimitris-bertsimas card S040 pp. 10, 12, 17–21]; (2) a best-bound node-selection arm; (3) the frontier also on frozen real designs with planted β [dimitris-bertsimas card S010 pp. 26–27]. The less-scalable verdict stands only if both 2009 arms miss; the why-now holds only where the frontier moved (→ Gould · Workflow D checkpoint).

**RISK — WHERE I COULD BE WRONG:** Without S040's seeds the gate is only distributional [02 J5]; planted β may flatter certification.

> **Moderator summary.** **Agree:** A solver × peak-hardware product is context, not evidence: the class is timed on one machine with one change per arm, time to best printed apart from time to proof, the then-arms (the rebuilt 2009 code, leaps) scored on proof, and the formulation arm kept apart from the solver release.
>
> **Split:** Whether a moved certified frontier may carry "now tractable" on its own (the lead) or earns only context without a net ratio to the strongest earlier code on cells both arms certify (Huangfu): the test prints both per arm, and the rule is left to the user. Gould adds that S010's "less scalable" verdict stands only if both 2009 arms, reproduced and fairly armed, miss.

### Item 2 · What does proof time buy a statistical estimator?

*Codes:* ML, IO · *Delegates:* Nocedal (NLP Team), Wright (NLP Team) · *Challenger:* Sahinidis (turn in the [Challengers' round](#challengers-round)) · *Fault line:* FL2 (also ML §6.2, point 8, the ℓ1 school; ML §6.1, point 1, the 2020 sparse-regression discussion with Sahinidis's group: recorded in both teams' notes, on no card)

#### Openings

**[Bertsimas lens, lead]** Could stop at: certificate or gap (fix: print every stop's gap, uninformative above 100%). Exactness pays only where it changes the statistics; its price, proof time, is printed beside the gain. Held: the warm-started MIO bounds its suboptimality when stopped early, for the bounded problem [S010 pp. 1, 6, 17]; at p = 200 the cardinality-constrained estimator has FDR 0.049 against 0.68–0.75, at 200–350 s against 1–4 s [S288 p. 17] (→ Method 4). Conceded (T1): gaps above 100% leave most runs without one, certificates only at p ≤ 200, M set from the truth [S288 pp. 16–17, 29–30]; S095 stops at 60 s without a gap, ENet and SCAD dominating at high noise and correlation [S095 pp. 5, 12]; the statistics of stopped solutions stay open [S010 p. 58]. "Typically falter" concerns large-scale learning [jorge-nocedal card S004 arXiv p. 3]; S288 has n = p [S288 p. 16]. Test: FL2's.

**[Nocedal lens]**

**POSITION:** Refine. Agreed: exactness pays only where it changes the statistics. But after the last incumbent change the estimate is fixed, so proof time buys a stopping decision and the word "optimal", not out-of-sample error. The p = 200 result sets the cardinality estimator against ℓ1 (k* 199 against 796), stopped at 10⁻⁴ or 5 min, most runs reporting no gap [dimitris-bertsimas card S288 pp. 16–17]: it prices formulation and search, not the certificate. So treat the gap as a stopping test, set from the estimation error, as the joint survey's error split prices optimization accuracy against it under a time budget [S004 arXiv pp. 35–37] (ℓ0 transfer inferred). Conceded: that survey's case for SG rests on redundant data at large n [S004 arXiv pp. 16–19]; the Nocedal group's precision-matrix race ran to 10⁻⁶ at fixed λ, reporting no estimation error [S043 pp. 1, 7–8]; ℓ0 statistics and MIO lie outside this lens's evidence.

**WHY (method refs):** Route: Workflow C. (→ Nocedal · Method 3, Workflow F checkpoint) A test that demands progress below the error level stalls by design: set it from an explicit estimate, flag the exit, report the tolerance reached. Inner tolerances are derived from the outer one so the subproblem is never oversolved [S013 preprint pp. 10–12]. (→ Heuristic 2) Phase times: the lead's cards put most of the time into the proof [dimitris-bertsimas card S095 p. 5; dimitris-bertsimas card S010 p. 11]. (→ Method 1, steps 3–4) Equal tuning and aligned stops: the ℓ1 side's k moves from 796 under validation to 276 and 542 under BIC [dimitris-bertsimas card S288 p. 17]. (→ Method 5, step 2) Does the bound separate the method from its Glasso or MB start? Above 100% the paper calls the gap "uninformative" [dimitris-bertsimas card S288 pp. 9–10, 16].

**FIRST EXPERIMENT / DECIDING TEST:** FL2's deciding test, also run at ρ = 0.2 and 0.7 [dimitris-bertsimas card S095 p. 11], plus three additions (designs inferred):

(1) Log each incumbent change (time, objective, support) with its out-of-sample error and FDR. Print search time (up to the last change) apart from proof time, per k and per path, since cuts carry across k [dimitris-bertsimas card S288 p. 11].

(2) Add a statistics-matched stop, replayed from those logs (deterministic mode): stop when UB − LB is within the final objective's spread across the ten draws. Stress that spread up to 1000× too large and too small, as the noisy-SQP study stresses its noise estimate [S084 arXiv p. 19], and flag the stop "not certified".

(3) Tune every method at each budget of one log-spaced time grid [S041 arXiv p. 8] *(citation not confirmed: S041's card c10, p. 8, tunes every method at each of 9 log-grid work budgets b, n/100 to 10n, between full gradients; not a time grid)*, and also score every method at a common k, with λ calibrated to hit it [dimitris-bertsimas card S095 p. 12].

Kill result: if in some cell the certified or capped run beats stop (2) by more than the standard error across draws, proof time pays there and this lens's view fails in that cell.

**RISK — WHERE I COULD BE WRONG:** Supports, not objective values, carry the statistics. Near-tied supports may differ in FDR within the estimation error, so stop (2) can halt on the worse one, and the survey's rates assume strong convexity [S004 arXiv pp. 25–26], which ℓ0 is far from. Proof work also feeds later k through reused cuts [dimitris-bertsimas card S288 p. 11], which per-k accounting misses. If a reader needs the proof itself, no statistic prices it. And this side has no measured case either: the survey declines benchmarking [S004 arXiv p. 4], and the precision-matrix study used 10n samples on six synthetic problems [S043 pp. 6, 8], not n = p.

**QUESTION FOR USER:** Does anyone downstream need the certificate itself (a proved ℓ0 optimum), or only the out-of-sample statistics?

**[Wright lens]**

**POSITION:** Agree; but S288's FDR gain, from runs reporting no gap [dimitris-bertsimas card S288 pp. 16–17], prices the exact ℓ0 model, not the exact solve. On Diabetes optima came in seconds, certificates in 10–20 minutes [dimitris-bertsimas card S010 p. 11]: later proof only certifies the estimator (inferred). MIO lies outside my field: I add protocol only.

**WHY (method refs):** Price the certificate like any guarantee, against an identical twin without it [03 §1.2] (→ Wright · Method 4). A joint NIPS 2013 rebuttal ran Cplex-LP at loosened tolerances and narrowed its claim to a class [03 §2.3] (→ Wright · Method 5).

**FIRST EXPERIMENT / DECIDING TEST:** FL2's, with its warm-start, 60 s and 5 min stops as twins, both sides timed per whole path, recording when each returned incumbent first appeared. If no twin trails the certified or capped run beyond one standard error in FDR or test loss, the certificate is an option, not a default.

**RISK — WHERE I COULD BE WRONG:** Unlike my convex evidence (ℓ1, LP), in ℓ0 a near-optimal objective can hide a wrong support.

#### The lead's reply

**[Bertsimas (lead), reply lens]**

**POSITION:** Strongest challenge: Nocedal's, that "after the last incumbent change the estimate is fixed, so proof time buys a stopping decision and the word "optimal", not out-of-sample error"; Wright makes the same point about S288. Conceded: S288's FDR gain comes from runs that mostly report no gap [S288 pp. 16–17], so it prices the ℓ0 model and its search, not the certificate. On these cards much of the time goes to proof [S095 p. 5; S010 p. 11]. The best-subset k-path already stops at a 1% gap or 15 min [S010 pp. 31–32]. His search/proof log is already this lens's protocol [S184 pp. 25–36]. Held: his stop (2) still runs on the MIO's lower bound. And in ℓ0 "a near-optimal objective can hide a wrong support" (Wright). Stage unchanged: certificate or gap.

**WHY (method refs):** (→ Method 4, step 4; warning sign 7) Of the methods compared, only the MIO's bound measures how far a stopped run is from the ℓ0 optimum. The warm start's rate is only to ε-stationarity [S010 p. 23]. The constrained Lasso is a weaker relaxation than the root node [S010 pp. 9–10]. Heuristics can fail with no sign to the user [S183 p. 3] (sparse PCA; transfer to regression inferred). So stop (2) is Method 4 at a looser tolerance, and only the tolerance is open. (→ Method 4, step 6) Wright's own rule keeps a safeguard that loses to its twin as an option or for the theory [stephen-j-wright SKILL.md, "Method 4: Minimal safeguard with a no-safeguard twin"]. Accepted: the theory is where the certificate stays, because the statistics of stopped solutions are still open [S010 p. 58]. (→ Workflow C, step 4) The exact solver can map regimes. Between n0 and n_t the estimator is "statistically relevant but computationally not feasible" [S061 p. 16], and FL2's fixed designs may miss that band. (→ Method 4, step 5) Cuts carry across k [S288 p. 11], so time whole paths against whole paths.

**FIRST EXPERIMENT / DECIDING TEST:** FL2's deciding test, as argued, with Nocedal's additions (1)–(3) and Wright's whole-path twins. Three further additions (designs inferred):

(a) A twin that uses no bound, replayed from the same logs: stop once the incumbent has gone unchanged for a stall window, with each window taken from the same log-spaced grid. This is the stall-count exit of S095's relaxation algorithm [S095 pp. 6–8] *(citation not confirmed: card c22 does not describe a stall-count exit; the paper text does, pp. 7–8, and p. 12 adds that early stopping did not hurt regression but failed in classification)* *(census correction: card c22 does carry it: "track the best c(s^t) as an upper bound and stop on the duality gap or a stall count (pp. 6–8)"; the note above is mistaken on the card)*. It runs beside stop (2) and the capped run.

(b) At (p, k) = (2,000, 10), move n across the recovery transition at each SNR and ρ, following S061's protocol [S061 pp. 12, 14–18].

(c) For each draw and each stop, record the support's Hamming distance to the capped run's support, next to that stop's gap. Each certificate names the problem it certifies: a valid M, or the ridge upper approximation [S288 p. 8].

How to read the results:

- The stall twin is within one SE of the capped run in FDR and test loss in every cell. Then neither the bound nor the certificate buys statistics here. This lens drops both as defaults and keeps the gap only as a label.
- The stall twin trails by more than one SE while stop (2) stays within one SE. Then the bound pays as the stopping instrument and the certificate becomes an option.
- The capped run beats stop (2) by more than one SE in some band (Nocedal's kill result). Then certify in that band, with its proof time printed.
- Gaps stay above 100% at a priori M or γ on most draws. Then stop (2) never fires: strengthen the formulation before testing any stop rule (→ Method 4 stop rule).

**RISK — WHERE I COULD BE WRONG:** The band may be empty at SNR 1 or 0.05. S061 took best-found solutions with no gap at a 15-minute limit, and it only tested √SNR ≥ 3 [S061 pp. 14, 16]. If the band is empty, no statistic prices the certificate and it keeps only its role in the theory. Nocedal already concedes that no statistic prices that role. The argument that the gap detects failures rests on a sparse-PCA observation [S183 p. 3] carried over to regression. At a priori M or γ the gaps may exceed 100% [S288 p. 16] *(citation not confirmed in full: card s12, paper p. 16: gaps over 100% at large M or γ; Fig. 3, p. 18: near 0% at a priori M0, γ0)*. The bound would then detect nothing, the stall twin would be the only rival left, and if it ties the capped run this lens's position falls.

#### Rejoinders

**[Nocedal, rejoinder lens]**

**POSITION:** Accept: the stall twin, (c), and that stop (2) uses the MIO's bound, leaving only its tolerance open. Contest: my ten-draw spread is an oracle one-sample users lack; where the capped run wins, search pays, not proof.

**WHY (method refs):** (→ Nocedal · Method 3 🔴) Stops use estimable quantities; oracles only benchmark [S091 arXiv pp. 17–18]. (→ Method 3, step 4) Early stops are re-estimated, not replaced; S061's band ended best-found, gapless [dimitris-bertsimas card S061 pp. 14, 16].

**FIRST EXPERIMENT / DECIDING TEST:** The lead's, plus: stop (2) on one-sample spreads (design inferred), tabulated against the oracle [S018 p. 20]. Reading 3: tighten the stop to the winning support's arrival gap; certify only at a closed gap.

**RISK — WHERE I COULD BE WRONG:** If winners arrive only as gaps close, reading 3 stands.

**[Wright, rejoinder lens]**

**POSITION:** Accepted: the stall twin (a), whole paths and (c). Contest: my quoted risk cuts against stop (2) too: a small gap, in objective units, can hide a wrong support (inferred). Certify a band only if every twin, longest stall window included, trails beyond one SE.

**WHY (method refs):** (→ Wright · Method 4 stop rule; Method 1; Heuristic 9)

**FIRST EXPERIMENT / DECIDING TEST:** The lead's, plus a p ≤ 12 design, every k-support enumerated: per draw, each support within stop (2)'s threshold, with Hamming distances to optimum and truth, FDR, test loss. Re-solve certified runs at tighter tolerances [03 §1.2]. If only the optimum's support lies within the threshold in every draw at an SNR, my objection fails there.

**RISK — WHERE I COULD BE WRONG:** Toys miss large-instance effects; MIO is outside my field.

> **Moderator summary.** **Agree:** Exactness pays only where it changes the statistics; S288's FDR gain prices the ℓ0 model and its search, not the certificate; search time is printed apart from proof time, whole paths are timed against whole paths, and the stall twin, stop (2) on the MIO's bound and Hamming distances join FL2's test.
>
> **Split:** Whether closing the gap ever buys statistics: the lead would certify in any band where the capped run beats stop (2) by more than one SE; Nocedal reads such a win as search, not proof, certifies only at a closed gap and wants stop (2) scored on one-sample spreads; Wright certifies a band only if every twin trails beyond one SE, since a small gap can hide a wrong support (his p ≤ 12 enumeration tests it).

### Item 3 · What may a stopped robust search on a simulator claim?

*Codes:* RO, HS (AP: the electromagnetic design as testbed) · *Delegates:* Vicente (DFO Team), Audet (DFO Team), Nocedal (NLP Team) · *Challenger:* Conn (turn in the [Challengers' round](#challengers-round)) · *Fault line:* FL4 (also HS §6.1, the Conn-with-Vicente point and "Vicente · what a heuristic may claim"; RO §6.3)

#### Openings

**[Bertsimas lens, lead]** Could stop at: certificate, gap or bound (fix: a heuristic label, worst cases enumerated). On a simulator the class is left on purpose; the claim shrinks to what an independent worst-case check supports. Conceded: robust local search estimates worst errors by n + 1 short ascents and a history set [S090 pp. 5–8], converges only for convex f with an exact worst-error oracle, else "a heuristic strategy" [S090 pp. 5–6] (C3), and may find worse errors late [S090 p. 12]; robust annealing's "warrants a global robust optimum" covers runs stopped at an empirical threshold [S141 pp. 9, 11] (→ Method 7 stop rule). Held: random sampling with ten times the evaluations reaches 96% of its estimate [S090 p. 12]; the bilevel route assumes a unique lower-level solution and a C¹ reduced function [andrew-conn card S066 preprint pp. 2–3], which fail where worst errors tie [S090 pp. 3–4; inferred]. Test: FL4's.

**[Vicente lens]**

**POSITION:** Agreed: the claim question stops at the certificate stage. A stopped run claims only the worst error it found, which is a lower bound on that design's worst case [inferred], reported beside its calls and a fresh check (→ Vicente · H10). Conceded: the bilevel paper assumes a unique lower-level solution and a C¹ reduced function [S047 preprint pp. 2–3], so it has no theorem here either. Challenged: the 96% [dimitris-bertsimas card S090 p. 12] used free adjoint gradients [dimitris-bertsimas card S090 pp. 2, 11] and took the search's own estimate as its reference. No card compares the inner rules without gradients [S047 preprint p. 19], so the inner-rule question stops earlier, at measured tractability (→ Vicente · Method 5).

**WHY (method refs):** Method 5: calls are the unit [S005 p. 16]. Random sampling is "not a good gauge" [dimitris-bertsimas card S116 p. 13], so beating it is a low bar. H3, the deterministic precursor of Method 3: tying inner accuracy to outer progress [S047 preprint pp. 8, 14] is this lens's default, untested here.

**FIRST EXPERIMENT / DECIDING TEST:** FL4's test, with two additions. (1) A swap arm: the bilevel outer loop fed by the ascents plus history set, so only the inner rule changes (→ Vicente · Method 5 [S005 pp. 26–27]). (2) Example III's 18-dimensional perturbation [dimitris-bertsimas card S090 pp. 14–15], where one gradient costs 18 calls, scored by multistart ascents (HS §6.1).

**RISK — WHERE I COULD BE WRONG:** The tied tolerance this lens favours certifies at most a local inner maximizer (FL4). Where several worst errors compete, searching more widely may beat it.

**[Audet lens]**

**POSITION:** Refine. A stopped run's worst case is only a lower bound on the true one. A referee can revoke it but never certify it [S156 p. 11]. So either inner route may claim only "worst-case cost ≥ ĝ, unrefuted by referee R at budget B", and both routes must face the same referee: without one, the weaker inner search looks most robust [S156 p. 3]. The 96% figure comes from a duel with random sampling, which his S116 calls "not a good gauge" [dimitris-bertsimas card S116 p. 13]. It ranks two lower bounds.

**WHY (method refs):** (→ Audet · Method 3) Refute, never certify, applied to benchmark logs too (catalog E12). (→ Audet · Method 5) One currency, with every call at both levels counted [S156 pp. 13–14].

**FIRST EXPERIMENT / DECIDING TEST:** FL4's test, with its fresh dense search run as a Reverse referee over each run's history. Both routes get the same referee start, budget and tolerance, and the referee's own cost is printed [S156 pp. 11–13]. Plot the claimed worst case and the refereed worst case against calls.

**RISK — WHERE I COULD BE WRONG:** None of my cards covers min–max design (Robust-MADS [S055] smooths noise), so carrying the bilevel referee over to a robust inner max is inferred. On Example I the referee may revoke nothing and still cost more than the runs [S156 p. 12].

**QUESTION FOR USER:** Can you get the 100-variable electromagnetic simulator and its error data? The lead's card shows collaborators' code and privately communicated errors, with no release stated [dimitris-bertsimas card S090 pp. 12, 18].

**[Nocedal lens]**

**POSITION:** Partly outside this lens's record, so it speaks to claims and measurement. Agree with the heuristic label, and that the claim shrinks to what an independent check supports. Refine (→ Nocedal · Method 3, stop rule): on a simulator, a stopped run proves only the worst error it found, which is a lower bound on its design's worst case. A mesh bounds that worst case from above only with a Lipschitz-type constant over the ball [inferred]. Example I's known polynomial yields one; a simulator does not, and this lens measures such constants rather than assuming them [S062 p. 8; S080 arXiv p. 6] *(citation not confirmed: S080 only; its card shows nothing at p. 6, while the arXiv v1 text, p. 6, supports the measurement point)* *(census correction: card c12 does carry p. 6: existing Lipschitz-estimation procedures "are not robust", with robust estimation as future work; the measurement itself is at p. 12)*. Example III's 18-dimensional perturbation admits no fine mesh [dimitris-bertsimas card S090 pp. 14–15] *(citation not confirmed in full: card c2-02 gives Example III's 18-dimensional perturbation, pp. 14–15, but not that it admits no fine mesh; that step is an inference)*. Challenge both held points (→ Method 5). The theory is a draw: his theorem needs convex f and an exact oracle [dimitris-bertsimas card S090 p. 5]. Their tolerance assumes fully quadratic inner models, yet their code, following Fasano–Morales–Nocedal, has no model-improvement steps and is not analysed [andrew-conn card S066 preprint pp. 8, 10]. The 96% [dimitris-bertsimas card S090 p. 12] is a win over random sampling, which his constrained paper calls "not a good gauge" [dimitris-bertsimas card S116 p. 13]; it is not a win over the bilevel solve. Inner rule: neither by default; the call-counted test decides.

**WHY (method refs):** (→ Nocedal · Method 5) Theory must separate the methods as they are run. Neither theory does here, so the run decides, and its result is never offered as proof. (→ Method 3, stop rule) A bound that needs a constant users cannot know certifies nothing [S080 arXiv p. 6; inferred transfer to certification] *(citation not confirmed: the S080 card shows nothing at p. 6; the arXiv v1 text, p. 6, supports the measurement point; the step to certification stays an inference, as labelled)* *(census correction: card c12 does carry p. 6, as noted at the first S080 citation of this turn; the note above is mistaken on the card)*. (→ Method 1) Use one stopping rule for both arms [S040 pp. 12–13], put an aggregate behind the two illustrative starts, and stratify outcomes before profiling [S080 arXiv pp. 28–29]. (→ Heuristic 12) Validate each in-algorithm estimate against the truth [S062 p. 8]; here that is the accepted worst case. (→ Method 4) The ascent depth [dimitris-bertsimas card S090 p. 15] and the bilevel's 10⁻² constants [andrew-conn card S066 preprint p. 14] are undecided choices, so sweep them. (→ Heuristic 3) Deterministic is not noise-free: difference tables also serve deterministic noise [S038 pp. 7–8]. The same label applies on this lens's side: a worst case from 10 L-BFGS-B iterations was used as a diagnostic only [S006 pp. 5–6].

**FIRST EXPERIMENT / DECIDING TEST:** FL4's test, plus five additions.

(1) Seeded multistarts beside starts A and B, with outcomes stratified by the robust local minimum each run reaches [S080 arXiv pp. 28–29].

(2) One stopping rule for both arms, not either method's own test: stop when the enumerated worst case has fallen by (1 − τ) of its distance to the enumerated robust minimum [S040 pp. 12–13]. Report data profiles in calls (Moré & Wild 2009).

(3) At each outer iterate, print the accepted worst case beside the enumerated one. Add an oracle arm per method, fed the enumerated worst case [S080 arXiv pp. 23–24]. When a fresh check finds a worse error, feed it back and resume the run, charging the extra calls (→ Method 3, step 4).

(4) A public second rung, Example III: n + 1, 10 + 1 and 3 + 1 ascents [dimitris-bertsimas card S090 pp. 14–15] against the bilevel method at its printed constants, and at ×10 and ÷10 [andrew-conn card S066 preprint p. 14]. Score each design with one large multistart-ascent budget.

(5) Noise-free first. Then inject identical noise into both arms and run each method unmodified and with difference intervals from an ECnoise estimate *(unverified)* [S038 pp. 7–8] (→ Heuristic 3).

How it decides: at equal calls, the better arm has the lower checked worst case and the smaller gap between accepted and checked worst case. Where an oracle arm closes a method's gap, that method's inner estimate is the component to repair.

**RISK — WHERE I COULD BE WRONG:** This lens has no robust-optimization study of its own, and it once set RO aside [S006 p. 15]. Global search and nonsmooth functions are among its blind spots (Roundtable Card). The worst-case function is nonsmooth where worst errors tie [inferred]. So the difference-interval advice covers only the smooth inner f, and the lower-bound reading and the Lipschitz bracket are inferences, not record. If your simulators are exact to roundoff, stage (5) spends runs on noise the agenda assumed away. Example III must be rebuilt from the printed paper. The EM fallback rests on collaborators' code and privately communicated error data [dimitris-bertsimas card S090 pp. 12, 18]. If both arms reach the same minima at similar call counts, FL4 as written is enough.

**QUESTION FOR USER:** Are the simulators you care about exact to roundoff, or do they carry computational noise (from iterative or adaptive solves)?

#### The lead's reply

**[Bertsimas (lead), reply lens]**

**POSITION:** Strongest challenge: Nocedal's, because it removes this item's certificate. Conceded: without a modulus, a mesh gives no upper bound. So on a simulator a stopped run claims only "worst-case cost ≥ ĝ, unrefuted by referee R at budget B" (Audet's wording), and the method stays a heuristic (C3). The 96% [S090 p. 12] ranks two lower bounds, was measured with free adjoint gradients [S090 pp. 2, 11], and beats random sampling, which my own paper calls "not a good gauge" [S116 p. 13]. I withdraw it as evidence on the inner rule. On theory the two sides draw, so the inner-rule question stops at measured tractability (Vicente). Held: Example III needs no 18-D mesh. Its coefficients enter linearly in one joint ℓ2 ball [S090 p. 14], so their worst case is a norm term [S019 pp. 3–4; inferred]. What remains is a 2-D bracket. Where worst errors tie [S090 pp. 3–4; inferred], the case for several ascents over one inner solve still stands, though untested.

**WHY (method refs):** (→ Method 7, stop rule) No bound, no claim of near-optimality. On a simulator only the lower bound stands. Where the function is printed, compute the bound and grade every arm by it (step 5). (→ Method 1, steps 3–4) A block that enters linearly over an ℓ2 ball has a dual-norm worst case [S019 pp. 3–4]. Example III's 16 coefficients form such a block [S090 p. 14] (inferred transfer). (→ Method 4; C3; Blind spots) The concession on S141 stands: it says "warrants a global robust optimum" [S141 p. 9] for runs stopped at an empirical threshold [S141 p. 11]. (→ Method 3) Robustness has a price, so print the nominal cost beside the worst case. The EM design's 8% came at practically unchanged nominal cost [S090 p. 12]. Theory is a draw. My theorem needs convex f and an exact oracle [S090 p. 5]. Their Algorithm 5.1 is not analysed, and their tolerances assume Lipschitz constants [andrew-conn card S066 preprint pp. 8–10], the very constant Nocedal says a simulator lacks. Hypothesis held, untested: bad neighbours that span the tied worst errors are enough, and the inner time stays predictable [S090 pp. 5–7]. The bilevel route runs one inner solve from a surrogate start and assumes its solution is unique [andrew-conn card S066 preprint pp. 2, 12–13]. Vicente's own risk line reads: "Where several worst errors compete, searching more widely may beat it."

**FIRST EXPERIMENT / DECIDING TEST:** FL4's deciding test, as argued, with the delegates' additions:

- Vicente: the swap arm and Example III.
- Audet: one common Reverse referee, its cost printed [charles-audet card S156 pp. 11–13].
- Nocedal: seeded multistarts, one stopping rule, oracle arms, and his constants at ×10 and ÷10.

Two changes of mine:

- Add the converse swap, so outer step × inner rule becomes a 2 × 2.
- Change the scorer: bracket the worst case wherever the function is printed.

Brackets:

- Example I: the mesh maximum below; above, that maximum plus a modulus taken from the printed polynomial, times the mesh radius [inferred].
- Example III: maximize the 16 parameter errors in closed form, then take the same 2-D bracket [inferred].
- Both examples: bracket every iterate and the global robust optimum.
- EM, if obtainable: Audet's referee only.

Run rules:

- Gradients withheld; each finite-difference gradient charged 2 calls in Example I and 18 in Example III.
- Random sampling, "the standard today" [S090 p. 12], stays as the practitioners' baseline (→ Method 5).
- At equal calls, print for each final design: its bracket, its nominal cost, the gap between the worst case it accepted and the bracket, and the bracket's own cost (the price of exactness).

How it decides: an inner rule wins where its designs' upper bounds fall below the rival's lower bounds, across seeds. Overlapping brackets mean a draw at that budget, and both arms stay heuristics.

Stage: until this runs, the inner-rule question stops at measured tractability. On a simulator, the claim stops at the certificate stage; the fix is the heuristic label plus a refereed lower bound.

**RISK — WHERE I COULD BE WRONG:** The closed-form reduction and the bracket are my own derivations; no card has them. Example III's parameter block is linear, which is an easy inner direction for both arms. So it prices the gradient charge more than it tests the nonconvex inner search a simulator poses. The EM case rests on collaborators' code and privately communicated error data [S090 pp. 12, 18], so the item's own subject may stay referee-only. The case for several ascents is untested: in Example III the 3 + 1 depth lowered the cost fastest yet never met its termination test [S090 p. 15]. Search depth is unsettled even within my own method.

**QUESTION FOR USER:** For item 3, is a claim bracketed on the papers' printed polynomials enough, or must it hold on a true simulator, where only refereed lower bounds exist?

#### Rejoinders

**[Vicente, rejoinder lens]**

**POSITION:** Accepted: heuristic label, refereed lower bound, withdrawn 96%, 2×2. Contested: Example III's bracket. With one joint ball, its closed form leaves √(Γ²−‖Δx‖²), unbounded in slope at the rim, so no Lipschitz modulus exists [inferred].

**WHY (method refs):** (→ Vicente · Method 5) calls as unit, components switched singly [S005 pp. 16, 26–27]; (→ H10) check the edge first; (→ H12) known-answer blocks [S053 pp. 3, 9–11].

**FIRST EXPERIMENT / DECIDING TEST:** The lead's 2×2: one shared ℓ2-ball device, Example III meshed in angles, judged per budget. For his risk, a rung: summed Example I blocks, Householder-reflected to keep the ball [inferred]. Report the outer step's effect, where the bilevel paper suspects the difficulty lies [S047 preprint p. 19].

**RISK — WHERE I COULD BE WRONG:** Both fixes are inferences; the rung's radius split needs bracketing too.

**[Audet, rejoinder lens]**

**POSITION:** Accept: printed-function brackets, and the 2 × 2, run in one code base (→ Audet · Method 5, step 3) [S172 pp. 16–17]. Contest: any EM verdict resting on my referee alone; no card tests it on a robust inner max.

**WHY (method refs):** (→ Method 3; E12) Audit instruments before they score. S156 validated its referee by recovering a known ranking [S156 pp. 17–19]; the brackets supply one.

**FIRST EXPERIMENT / DECIDING TEST:** The lead's, plus calibration on Examples I and III: seeded multistart Reverse referees, intersected, from common starts [S156 pp. 11–13]. Count bracket-refuted claims the referee passes. EM claims stand as "unrefuted at budget B" only if the referee recovers the bracket ranking.

**RISK — WHERE I COULD BE WRONG:** Two printed polynomials may pass a referee that the 100-variable simulator defeats.

**[Nocedal, rejoinder lens]**

**POSITION:** Accepted: the concession, the 2 × 2, your reduction. Contest its bracket: in your joint ball the reduction carries √(Γ²−‖Δx‖²), whose slope blows up at the rim, so no modulus exists [inferred]; mesh θ, φ in Δx = Γ sin θ (cos φ, sin φ).

**WHY (method refs):** (→ Nocedal · Method 3, stop rule) a bracket needs a computable constant [S080 arXiv p. 6; inferred transfer] *(citation not confirmed: the S080 card shows nothing at p. 6; the arXiv v1 text, p. 6, supports the measurement point)* *(census correction: card c12 does carry p. 6, as noted at the first S080 citation of his opening; the note above is mistaken on the card)*. (→ Heuristic 12) test scorers by direct evaluation [S062 p. 8].

**FIRST EXPERIMENT / DECIDING TEST:** Yours, refined: 18-D multistart ascents at several designs must never exceed the closed-form upper bound, or the scorer fails; compare arms per robust basin reached (→ Method 1, step 7 [S080 arXiv pp. 28–29]).

**RISK — WHERE I COULD BE WRONG:** My rim objection is on no card; two separate balls void it.

> **Moderator summary.** **Agree:** On a simulator a stopped run claims only a refereed lower bound, "worst-case cost ≥ ĝ, unrefuted by referee R at budget B", under a heuristic label; the 96% figure is withdrawn as evidence on the inner rule; the arms run as a 2 × 2 (outer step × inner rule) in one code base, gradients withheld and every call counted.
>
> **Split:** Which inner rule wins (the lead's short ascents with a history set, Vicente's tolerance tied to outer progress, Nocedal's "neither by default") is left to the call-counted test; Vicente and Nocedal contest the lead's closed-form bracket for Example III at the rim of the joint ball (fix: an angle mesh), and Audet contests any EM verdict that rests on his referee alone (fix: calibrate it on the brackets).

### Item 4 · Where do heavier conic rungs stop paying?

*Codes:* CP, IO · *Delegates:* Sahinidis (MINLP Team), Burer (MINLP Team) · *Challenger:* Dey (turn in the [Challengers' round](#challengers-round)) · *Fault line:* FL5 (also CP §6.2, the Sahinidis and Dey points; IO §6, "Sahinidis · global solver benchmarks")

#### Openings

**[Bertsimas lens, lead]** Could stop at: measured tractability (fix: change the device). A stronger relaxation earns its place only by certifying more per second than the incumbent solver; on his record the all-pairs LMI does not yet. His share unidentified [S377 p. 1]: RPT-BB solves more tested instances than BARON and SCIP, BARON fastest on most small ones, all-pairs products "less tractable" at scale [S377 pp. 1, 31–33, 38]; the LMI, provably tightest of its family, takes nx = 50 from 101 s to 2,100 s, the nx = 100 root unfinished after an hour [S415 pp. 23–24, 27], not consistently advantageous [S708 p. 37]; with integers SCIP leads [S624 pp. 13, 18] (→ Method 1 stop rule; T4). Device: products chosen by structure, his papers' future work [S415 p. 30; S708 p. 42] *(citation not confirmed: S415: card c2-08 gives partial constraint multiplications and partial product-variable generation as future work, p. 30, but no structure-based choice; nor does the paper text; S708: card s2-18 gives partial multiplications, selective products and iterative constraint generation as future work, p. 42, but no structure-based choice; the paper's one stated criterion is violation)*, as Dey's rung is [inferred], yet "not advisable" in higher dimensions [santanu-s-dey card S129 pp. 18, 23]. Test: FL5's.

**[Sahinidis lens]**

**POSITION:** Agreed on the stop: a rung counts by certified bound per second, failures included (→ Sahinidis · Method 5); tightness proofs are Burer's and Dey's ground. His co-authored 2011 QCQP comparison found the strongest SDP relaxations needing "three orders of magnitude more computational time" for gaps averaging 3% against up to 19% [01 SW2]. Verdict: class-dependent, since the LMI lifts integer dike proofs from 1 to 7 of 9 [dimitris-bertsimas card S624 p. 16]; plan a portfolio with per-node switching [02 J1]. Device: emulate the LMI with cheaper cuts, as BARON's "SDP-quality" quadratic cuts do for MIQPs [01 SW2] (→ Method 5). Standing: the wins over BARON duel releases 20.10.16 and 21.1.13 [dimitris-bertsimas card S377 pp. 28–35], [dimitris-bertsimas card S708 p. 35]; releases to 2026.9.10 log hierarchical RLT cuts and QCQP-relaxation changes, and as branching also differs [dimitris-bertsimas card S377 p. 3], they compare engines, not rungs (→ Methods 2, 4).

**WHY (method refs):** Method 5 (steps 1, 3–6): gap closed, time and failures together; a cheaper object keeping most of a slow bound; nonlinear rungs only with fail-safes and per-node switching; subsolver answers checked [02 T6; 01 SW2, SW5; 03 §D2]. Method 4 and Integrity rule 5: standing only from named current releases, third-party beside self-benchmarks; rankings age [05 2e–2f, 7e]. Method 2 step 4: one component, on and off, in one code [03 §B2]. Method 1: with reduction off, bounds too weak to prove optimality [01 SW5]. Heuristic 2: finite bounds [05 3e].

**FIRST EXPERIMENT / DECIDING TEST:** FL5's test, plus: (a) every arm a named build in one engine, same branching and domain reduction (once with none, → Method 1), adding an LMI admitted per node only while its bound gain per second beats its outer approximation's; root gap per second first, then the tree. (b) BARON 2026.9.10 and SCIP 10.1.0 at defaults, one thread, a time limit plus BARON's MaxWork, beside the papers' 2020–21 BARON releases where runnable. (c) Identical finite bounds for all arms, printed (the dike runs add xᵢ ≤ 300 [dimitris-bertsimas card S708 p. 41]). (d) Per library, losses named: RPT families, QPLIB, MINLPLib, and qcqp2, the 2011 study's own QCQPs, to re-price SDP. (e) A certificate contradicting any arm's feasible value or a library bound counts as a failure, BARON's too [05 1h]; RPT-BB's integer stop test as printed checks the incumbent against the smaller child bound only [dimitris-bertsimas card S624 pp. 8–9], so its proofs count only against the open-node minimum (→ Heuristic 7). Stop rule: "a gain on one library only is not a result" (Workflow D).

**RISK — WHERE I COULD BE WRONG:** Strength can pay outright: one convex nonlinear relaxation solved at the root in 1 s what BARON's linear relaxations took over 1000 s on [05 5b]; the dikes may be such a class [dimitris-bertsimas card S708 p. 41]. The 2011 price predates today's SDP solvers (Method 5 step 7). The cheap emulation is shown only for MIQPs with linear equality constraints (arXiv:2106.13721, checked). MINLPLib and the QCQP sets are BARON development libraries [03 §A2], so the duel tilts toward BARON, his product; the one-engine ablation does not.

**QUESTION FOR USER:** Can you run a licensed current BARON? Its free build handles only 10 variables and constraints (minlp.com, checked), below this item's n ≥ 20.

**[Burer lens]**

**POSITION:** Refine. Keep the stop rule (→ Burer · Method 1), but test strictness before price and separate the LMI from its solver: every LMI timing cited here used MOSEK [dimitris-bertsimas card S377 pp. 28–35; dimitris-bertsimas card S415 pp. 26–27; dimitris-bertsimas card S708 p. 35; dimitris-bertsimas card S624 p. 10; santanu-s-dey card S129 p. 19], interior-point only for conic problems (MOSEK docs, verified).

**WHY (method refs):** Strictness is per substructure (→ Burer · Method 2): Zhen, de Moor and den Hertog's SOC × SOC product, from their RPT paper, added nothing to Shor ∩ RLT ∩ SOC-RLT ∩ Kron [S049 arXiv pp. 8–9] *(citation not confirmed: card c08 says a Zhen et al. constraint added no strength, p. 9, not that it is an SOC × SOC product from their RPT paper)*; on a ball with non-intersecting cuts, SDP plus all SOC-RLT and RLT products is exact, RLT-only not [S021 pp. 1, 3, 11–12]. The solver matters (→ Method 6): one box-QP relaxation took 5,355–10,296 s by interior point, 54–101 s by splitting [S016 preprint p. 28].

**FIRST EXPERIMENT / DECIDING TEST:** FL5's, plus: (1) on instances where RLT leaves a root gap (filter disclosed), drop any rung that closes none of it (→ Method 4); (2) an LMI arm solved by splitting, its valid bound read from a dual-feasible multiplier [S020 pp. 4, 9–10] (→ Method 6); (3) two-signal root tightness beside each win [S049 arXiv p. 10] (→ Method 3). If (2) still loses per second, the LMI itself does.

**RISK — WHERE I COULD BE WRONG:** On small, sparse box QPs his SDP bounds did not repay their cost [05 §4]; splitting bounds are only moderately accurate [S014 preprint pp. 2, 17] *(citation not confirmed: S014 is a projected-gradient code for the maxcut SDP, not a splitting method; its card supports the slow limiting convergence of first-order methods, p. 2, and their moderate-accuracy niche, p. 20, while p. 17 concerns ill-conditioning; the transfer to splitting is inferred)* *(census correction: card c01 does carry p. 17: iterations grow "drastically" from 0.2% to 0.02%; only the transfer to splitting is unsupported)* and untested on RPT.

**QUESTION FOR USER:** Should the test add a first-order LMI arm that needs a separate released SDP code (e.g., SDPNAL+, which runs in MATLAB), or keep the RPT papers' MOSEK stack only?

#### The lead's reply

**[Bertsimas (lead), reply lens]**

**POSITION:** Strongest challenge: Sahinidis's, because it reaches the certificate. Conceded: the wins over BARON's 2020–21 releases also change the partitioning rule [S377 pp. 3, 28–35; S708 p. 35], so they compare engines, not rungs. The integer sequel's printed stop test checks only the smaller child bound [S624 pp. 8–9], so its 7-of-9 dike proofs [S624 p. 16] are unargued until re-checked. The cone-product paper's released code does take the open-node minimum, but it throws away any child whose MOSEK status is not OPTIMAL, slow progress included (its IJOC code deposit, read today). Held: the rung is priced inside one code, through a use_lmi switch with the branching rule unchanged. LMI off/on: 101 s/2,100 s at nx = 50 with 3.2/3.1 splits, and no finished root at nx = 100 [S415 p. 27; deposit] *(citation not confirmed: card c2-08 gives the 101 s/2,100 s timings and the unfinished nx = 100 root, p. 27, not the 3.2/3.1 splits; paper Table 4, p. 27, does)*. On the dikes it solves all nine at the root, where RPT-BB times out on five [S708 p. 41]. The LMI pays on some classes, not yet at scale.

**WHY (method refs):** Conceded under Integrity rule 3 and Method 4 steps 3–5. A proof that the printed algorithm does not argue is a gap, not a certificate, and standing needs the incumbent's current release on one machine. The dropped-node finding is a case for his subsolver check [nikolaos-v-sahinidis SKILL.md, "Method 5 · A relaxation's strength counts only at speed", step 5]. What changed inside BARON after 2021 is one of my Blind spots (inside commercial solvers). Held under Method 7 step 6 and Method 1's stop rule: the LMI is the PSD strengthening, priced on and off in one code, with the size where it becomes prohibitive printed [S415 p. 27; S708 pp. 37, 42] *(citation not confirmed: card s2-18 gives the LMI as not consistently advantageous, p. 37, and RPT-BB's general tractability limit, p. 42, but no size where the LMI becomes prohibitive)*. The change of device is products chosen by structure, the papers' own future work [S415 p. 30; S708 p. 42] *(citation not confirmed: S415: card c2-08 gives partial constraint multiplications and partial generation of product variables as future work, p. 30, but no structure-based choice; neither does the paper; S708: card s2-18 gives partial multiplications, selective products and iterative constraint generation as future work, p. 42, but no structure-based choice; the paper's iteration is violation-driven)*. Heuristic 4: these losses are printed in the body of the papers.

**FIRST EXPERIMENT / DECIDING TEST:** FL5's deciding test, as argued, kept in two separate ledgers. It settles two questions: is the LMI's price the rung's or MOSEK's, and does a cheaper arm keep the LMI's dike win?

(1) Rungs, in one code. Use the deposit (its use_lmi switch) and RPT-BB with integers, rebuilt with a stop test over all open nodes. Freeze branching and node selection and swap one component at a time [samuel-burer card S020 p. 16]. Arms: no LMI; LMI solved by MOSEK; Burer's splitting arm (2); Sahinidis's outer approximation with per-node admission (a). Run each with and without domain reduction. Log root gap closed per second, splits saved and time to proof.

(2) Engines. Current BARON and SCIP at defaults, one thread, beside BARON 20.10.16 and 21.1.13 where they still run.

Instances: continuous and integer dikes *(unverified)*, with the same bounds xᵢ ≤ 300 for every arm [S708 p. 41]; the deposited instances; QPLIB; MINLPLib.

A run counts as proved only if its log shows all three: the gap within 10⁻⁴ of the open-node minimum at exit, no node thrown away on a non-OPTIMAL status, and an exit by the gap test. Any other run is a failure.

Decision: the LMI stays a default only where ledger (1) shows it proving more instances per second than every cheaper arm, on two libraries. Elsewhere it is admitted per node, or replaced by products chosen by structure.

**RISK — WHERE I COULD BE WRONG:** Every LMI timing on my cards comes from MOSEK [S377 pp. 28–35; S415 p. 27; S624 p. 10; S708 p. 35]. On one box-QP relaxation over nine instances, interior point took 5,355–10,296 s and an augmented-Lagrangian code 54–101 s [samuel-burer card S016 preprint p. 28], so Burer's arm could reverse my verdict. The dike win rests on bounds that were added to make the model compact [S708 p. 41]. No code was found for the 2026 revision or the integer sequel (searched), so those arms would be rebuilds, not the papers' own code. The deposit's script also uses different α and β values from the printed ones, which the card reader found infeasible [S415 pp. 26–27, 46] *(citation not confirmed: card c2-08 finds instances 3–5 infeasible as printed, pp. 26, 46; the deposit's differing α, β values are on neither the card nor the paper text)*. For those instances the deposit, not the printed description, is the definition.

**QUESTION FOR USER:** Should the plan ask the authors for the integer sequel's code (none was found), or rebuild it from the printed algorithm with a stop test over all open nodes?

#### Rejoinders

**[Sahinidis, rejoinder lens]**

**POSITION:** Accepted: two ledgers, engines not rungs, the proof rule. Contested: (1) it trusts each arm's own log; a third-party benchmark checking MINLPLib's bounds counted 26 wrong optima from BARON 22.9.30 in 1,000 runs [05 1h]; (2) neither ledger prices the rung inside BARON, whose manual advises declaring "products of important existing constraints" relaxation-only (§4.1, firm, checked).

**WHY (method refs):** (a) Heuristic 7, Method 4. (b) Heuristics 2, 8; Method 2 step 4 [02 I6]. (c) Method 5 steps 1, 4 [01 SW5]. (d) Heuristic 6 [03 §B1]; MOSEK's default picks its own thread count (MOSEK docs, checked).

**FIRST EXPERIMENT / DECIDING TEST:** The lead's, plus: (a) bounds contradicting another arm's rechecked incumbent or the library's fail the run; (b) BARON with structure-chosen products declared relaxation-only, on and off; (c) LMI fail-safe: non-OPTIMAL children keep their parent's bound and stay open, each logged as a failure; (d) one thread per solver, MOSEK included.

**RISK — WHERE I COULD BE WRONG:** One thread may handicap interior point; add a labelled multithread run.

**[Burer, rejoinder lens]**

**POSITION:** Accepted: both ledgers, one-swap tree. Contested: the proof rule keys on solver status; only provably valid bounds may prune or enter the open-node minimum, so non-OPTIMAL children stay open, costing time. Integer arms: outside my evidence.

**WHY (method refs):** → Burer · Method 6, steps 3–4: bounds from a dual-feasible multiplier [S020 pp. 9–10] or rigorous post-processing [S020 pp. 14–15]; Methods 4, 2.

**FIRST EXPERIMENT / DECIDING TEST:** Lead's, plus: deposit patched too; both LMI solvers timed to their common bound [S020 p. 12]; RLT-root-gap subsets beside full libraries, by joint outcome [S049 arXiv p. 17]; my (1) withdrawn: no rung dropped on root evidence [S047 pp. 13, 18].

**RISK — WHERE I COULD BE WRONG:** At 10⁻⁴, splitting's slow tail [S014 preprint pp. 2, 17] *(citation not confirmed: S014 is a projected-gradient code, not a splitting method; its card supports p. 2 (slow limiting convergence of first-order methods) and p. 20 (their moderate-accuracy niche), not p. 17; the transfer to splitting is inferred)* *(census correction: card c01 does carry p. 17: iterations grow "drastically" from 0.2% to 0.02%; only the transfer to splitting is unsupported)* may lose for solver reasons; report a looser gap.

> **Moderator summary.** **Agree:** A rung counts by certified bound per second, failures included; the RPT wins over BARON's 2020–21 releases compare engines, not rungs, so rungs are priced in one code and engines in a second ledger; a proof needs the gap closed against the open-node minimum, with non-OPTIMAL children kept open and logged as failures.
>
> **Split:** Where the LMI pays: the lead says on some classes, not yet at scale, and moves the device to structure-chosen products; Sahinidis calls it class-dependent (a per-node portfolio, or cheaper cuts that emulate it) and will not let the proof rule trust each arm's own log; Burer would first separate the LMI from its solver, MOSEK against splitting, before blaming the LMI itself.

## Draft plan v1 (superseded by v2; kept verbatim)

The lead's programme plan as checked by the moderator for neutrality, with the verifier's annotations added in italics. Under part 3, the fault-line deciding tests the plan cites are reproduced verbatim.

### Programme plan · The price of exactness

*Drafted by the Bertsimas lens (lead) and checked by the moderator for neutrality. Recommendations without attribution are the lead's. Delegates' unresolved objections are quoted verbatim in the item they concern.*

**Claim ledger** (the lead's proposal; → his Methods 2, 4, 7):
- "now tractable" needs the certified frontier. Huangfu: "moving the frontier or that ratio alone earns context-only" (unresolved, item 1).
- "N× faster" is a net ratio to the strongest earlier code on cells both certify (Huangfu's rule, accepted by the lead) *(citation not confirmed: the lead's acceptance appears only in the plan draft; no lead turn follows the rejoinders)*.
- "certified" is a valid bound at a stated limit.
- "robust" is a bracket (printed function) or "worst-case cost ≥ ĝ, unrefuted by referee R at budget B" (simulator). The wording is Audet's, and he attaches a condition for EM: "EM claims stand as 'unrefuted at budget B' only if the referee recovers the bracket ranking".

None of these claims may rest on borrowed products, solver statuses or a search's own estimate.

#### 1. Recommendation (the lead's, by item)

**1 · IO, ML (LO) · stops at measured tractability (fix: time the class).** Huangfu agrees. Gould agrees but narrows it to one change per arm, which the lead accepts.
- Problem: best-subset MIQO, one problem for every arm: (8) or provable M [S010 pp. 9–10, 15–17] (→ Method 1).
- Incumbent: the borrowed factor. Then-arms: S040's code rebuilt, and leaps 3.2 (CRAN, checked).
- Solver runs: each runnable release of one MIO solver *(unverified)* at defaults, deterministic, one thread; one release at 1, 8 and 16 threads; 1% gap or 15 min per k [S010 pp. 31–32] *(assumed)*.
- Instances: S010's designs, Diabetes, and frozen real designs (Gould).
- Metric: the certified frontier (Gould's score), with the net ratio beside it (→ Method 2).
- Huangfu and Gould both mark their MIO transfers inferred.
- *Accepted from Gould's rejoinder*: "The less-scalable verdict stands only if both 2009 arms miss; the why-now holds only where the frontier moved."
- *Unresolved*: may a frontier move alone carry "now tractable"?
  - The lead: "credit an arm (release, threads, formulation, warm start) only if it moves that frontier"; otherwise "the abstract carries the frontier and the net factor measured there".
  - Huangfu (rejoinder): "moving the frontier or that ratio alone earns context-only."
  - His censoring point is accepted: net factors are measured only on cells both arms certify.

**2 · ML, IO · stops at certificate or gap (the lead's stage; fix: print every gap).**
- Problem: convex integer ℓ0 estimators [S095 p. 11; S288 pp. 16–17] *(citation not confirmed: S095: card c22 gives the convex integer reformulation at pp. 4–5; p. 11 carries Table 2's designs and timing relative to glmnet, not the reformulation; S288: card s12 gives the convex-in-Z reformulation at pp. 8–9; pp. 16–17 carry the synthetic p = 200 runs against MB and Glasso, Table 1, p. 17)* against glmnet, Glasso and QUIC *(unverified)* (FL2's deciding test).
- Settings: one MIO release *(unverified)*; stops at the warm start, 60 s, 5 min, 2% and 1 h; M or γ set a priori, each certificate naming its problem [S288 pp. 8, 11] (→ Method 4).
- Metric: out-of-sample error and FDR against time, whole path against whole path.
- Accepted at the table: the stall twin and (c), by Nocedal and Wright; whole paths, by Wright; and, by Nocedal, that stop (2) uses the MIO's bound, "leaving only its tolerance open".
- Nocedal and Wright both place MIO outside their evidence.
- *Unresolved*: does closing the gap ever buy statistics?
  - Nocedal: "after the last incumbent change the estimate is fixed, so proof time buys a stopping decision and the word 'optimal', not out-of-sample error". Rejoinder: "where the capped run wins, search pays, not proof." His reading 3: "tighten the stop to the winning support's arrival gap; certify only at a closed gap."
  - Wright: S288's FDR gain "prices the exact ℓ0 model, not the exact solve". Rejoinder: "my quoted risk cuts against stop (2) too: a small gap, in objective units, can hide a wrong support (inferred). Certify a band only if every twin, longest stall window included, trails beyond one SE."
  - The lead: "The capped run beats stop (2) by more than one SE in some band (Nocedal's kill result). Then certify in that band, with its proof time printed." His draft locates that band "perhaps in S061's band" *(citation not confirmed: no turn in the session contains these words; the lead's item 2 reply says only that FL2's fixed designs "may miss that band" [S061 p. 16])*, a band "FL2's fixed designs may miss". His own risk line: "The band may be empty at SNR 1 or 0.05."

**3 · RO, HS (AP testbed) · two stops.** The inner rule stops at measured tractability (Vicente's framing, adopted by the lead). Simulator claims stop at the certificate stage; the fix is a heuristic label and a refereed lower bound, in Audet's wording, accepted by Vicente and Nocedal.
- Problem: min–max over an ℓ2 ball (Γ = 0.5), gradients withheld: Examples I and III [S090 pp. 8, 14] *(citation not confirmed: card c2-02 gives Γ = 0.5 for Example I only; Example III's joint ball of radius 0.5 is in the paper text, p. 14; the EM design uses Γ = 550 μm [S090 p. 12])*, Vicente's summed-block rung, and EM if obtainable *(unverified)* (Audet's question).
- Incumbent: random sampling [S090 p. 12], kept as the practitioners' baseline. Vicente: "beating it is a low bar".
- Arms: outer step × inner rule. The 2 × 2 is the lead's, accepted by Vicente, Audet and Nocedal; the arms are rebuilt from print in one code base (Audet), and every call is counted.
- Bounds: a mesh bracket for Example I and an angle mesh for Example III (Vicente's and Nocedal's fix) [inferred]. The lead concedes in the draft that his Δx bracket fails at the rim *(citation not confirmed: the concession appears only in the plan draft; no lead turn follows the rejoinders)*.
- Metric: the bracketed or refereed worst case against calls, with the nominal cost beside it (→ Methods 3, 7; HS thin).
- The 96% figure is withdrawn as evidence on the inner rule.
- *Unresolved: FL4's inner rule.*
  - The lead: "Where worst errors tie [S090 pp. 3–4; inferred], the case for several ascents over one inner solve still stands, though untested."
  - Vicente: tying inner accuracy to outer progress "is this lens's default, untested here"; "Where several worst errors compete, searching more widely may beat it."
  - Nocedal: "Inner rule: neither by default; the call-counted test decides."
- *Contested by Audet (rejoinder)*: "any EM verdict resting on my referee alone; no card tests it on a robust inner max." His calibration gate is accepted (see the claim ledger). His risk line: "Two printed polynomials may pass a referee that the 100-variable simulator defeats."
- *Caveats on the fixes*:
  - Vicente: "Both fixes are inferences; the rung's radius split needs bracketing too."
  - Nocedal: "My rim objection is on no card; two separate balls void it."

**4 · CP (stated jointly; this follows his co-authored papers), IO · stops at measured tractability.** Sahinidis agrees. Burer keeps the stop rule but would "separate the LMI from its solver". The lead's fix: structure-chosen products.
- Problems: nonconvex QCQP and polynomial problems, with or without integers, n ≥ 20: RPT families, dikes (xᵢ ≤ 300 for all [S708 p. 41]) *(unverified)*, QPLIB, MINLPLib. Sahinidis also names "qcqp2, the 2011 study's own QCQPs, to re-price SDP".
- Two ledgers, accepted by Sahinidis and Burer: (1) rungs in one code; (2) engines.
- Incumbents: BARON 26.9.10 and SCIP 10.1.0 at defaults (checked), if a BARON licence is available (Sahinidis's question), beside BARON 20.10.16 and 21.1.13 where they still run *(unverified)*.
- Rungs:
  - RLT, structure-chosen products, all-pairs RPT.
  - The LMI three ways: by MOSEK *(unverified)*; by splitting (Burer; subject to his question to the user); or outer-approximated and admitted per node (Sahinidis).
  - One code, the IJOC deposit (`use_lmi`, checked). It is patched so that non-OPTIMAL children keep their parent's bound and stay open, each logged as a failure (Sahinidis, Burer).
  - Integer arms rebuilt with an all-open-node stop test *(assumed, pending the lead's question)*.
  - BARON with structure-chosen products declared relaxation-only, on and off (Sahinidis).
- Settings:
  - Gap 10⁻⁴; 3,600 s [S624 p. 10] *(assumed)*; one thread per solver, MOSEK included (Sahinidis).
  - Incumbents rechecked for feasibility [S708 p. 35]. Bounds that contradict another arm's rechecked incumbent, or the library's bound, fail the run (Sahinidis).
  - Only provably valid bounds prune or enter the open-node minimum (Burer; the lead's Method 4 step 4).
  - Burer: "Integer arms: outside my evidence."
- Metric: proved count and gap against time, per library and per ledger (→ Method 7 step 6).
- *Unresolved: where the LMI pays.*
  - The lead: "The LMI pays on some classes, not yet at scale."
  - Sahinidis: "Verdict: class-dependent", and "plan a portfolio with per-node switching". His device: "emulate the LMI with cheaper cuts, as BARON's 'SDP-quality' quadratic cuts do for MIQPs".
  - Burer: "If (2) still loses per second, the LMI itself does."
- *From delegates' risk lines, not in the draft's settings*:
  - Sahinidis: "One thread may handicap interior point; add a labelled multithread run."
  - Burer: "At 10⁻⁴, splitting's slow tail [S014 preprint pp. 2, 17] may lose for solver reasons; report a looser gap." *(citation not confirmed: S014 is a projected-gradient code, not a splitting method; its card supports p. 2 (slow limiting convergence of first-order methods) and p. 20 (their moderate-accuracy niche), not p. 17; the transfer to splitting is inferred)* *(census correction: card c01 does carry p. 17: iterations grow "drastically" from 0.2% to 0.02%; only the transfer to splitting is unsupported)*
  - Sahinidis: "MINLPLib and the QCQP sets are BARON development libraries [03 §A2], so the duel tilts toward BARON, his product; the one-engine ablation does not."
- Burer withdraws his opening rule (1): "no rung dropped on root evidence".

#### 2. Backup and switch rules (the lead's)
- 1: Old releases cannot be licensed → run the newest release against both then-arms, with the factors labelled borrowed. The rebuild fails its gate (Gould's node-count reproduction, Huangfu's proved cells) → "less scalable" stays unmeasured.
- 2: Gaps above 100% on most draws → strengthen the formulation (→ Method 4 stop rule). The stall twin ties → no default certificate.
- 3: An ascent beats a closed-form upper bound → the scorer is void (Nocedal). The referee fails calibration → EM keeps the heuristic label (Audet).
- 4: Roots unfinished at n ≥ 20 → admit the LMI per node. Splitting closes the gap → the cost was MOSEK's (Burer's arm). The LMI stays a default only where it out-proves every cheaper arm per second on two libraries.

#### 3. Minimal experiment
Each item's deciding tests are its fault-line test (FL1, FL2, FL4, FL5), as argued, and every later DECIDING TEST field of that item, verbatim from the discussion.

The lead accepts every rejoinder addition except Huangfu's context-only rule, which stays unresolved (item 1). Net factors are measured only on cells both arms certify.

The lead's protocol:
- The user runs all arms on one machine, with releases and threads stated.
- Order: items 3, 2, 1, 4, by the licences each needs.
- Equal budgets: time per k, whole paths, calls, one limit.
- Performance profiles; losing instances named; Mittelmann's third-party numbers beside item 4.

<details>
<summary>The fault-line deciding tests the plan cites (FL1, FL2, FL4, FL5), verbatim from the council roundtable, Step 3</summary>

**FL1 · deciding test:** on the best-subset paper's synthetic designs and Diabetes data [dimitris-bertsimas card S010 pp. 26–27], solve one MIQO formulation to a stated gap (a) with every solver release still runnable, named with its year, on one machine and one thread, and set the measured factor beside Bixby's MILP factor for the same releases (does "similar" hold?); (b) with one release at 1, 8 and 16 threads on an older and a current CPU, and set the realized hardware factor beside the Top500 peak ratio for the same years and the two CPUs' own peak-flops and memory-bandwidth ratios; several seeds, deterministic parallel mode, geometric means, losing instances printed; Huangfu's per-component profile (node relaxations, heuristics, cuts) places the ceiling (inferred translation).

**FL2 · deciding test:** on the inverse-covariance designs at p ≤ 200 and the sparse-regression paper's smallest design, (p, k) = (2,000, 10), at SNR 6, 1 and 0.05 [dimitris-bertsimas card S095 p. 11], stop the warm-started MIO at its warm start, 60 s, 5 min, a 2% relative gap (the stopping rule of Curtis's co-authored runs [frank-e-curtis card S034 pp. 36–37]) and a 1 h cap, printing the gap each time (flagged uninformative above 100%), with M or γ set from the a priori norm-bound scales, never from the truth [dimitris-bertsimas card S288 p. 11]; run the papers' own ℓ1 opponents (glmnet, Glasso) and QUIC *(unverified)* at tolerances 10⁻², 10⁻⁴ and 10⁻⁶ [jorge-nocedal card S043 p. 7] *(citation not confirmed: card c3-01 gives C:QUIC and a MATLAB QUIC stopped at one tolerance, ‖∇̃F(P)‖∞ ≤ 10⁻⁶, p. 7; not the 10⁻² and 10⁻⁴ tolerances)*; ten draws per point [dimitris-bertsimas card S095 pp. 13–20]; plot out-of-sample likelihood or prediction error and FDR against time and against the MIO's gap. Certification pays where the statistics improve beyond the standard error between the 60 s or 5 min incumbent and the certified or capped run; the trade-off view holds where the warm start already matches that run and loose ℓ1 tolerances match tight ones.

**FL4 · deciding test:** on his Example I (two-dimensional polynomial, ℓ2 ball of radius 0.5, starts A and B) [dimitris-bertsimas card S090 p. 8], both methods reimplemented from the printed algorithms [dimitris-bertsimas card S090 pp. 6–8], [andrew-conn card S066 preprint pp. 10–14] (no release of the bilevel code is stated [luis-nunes-vicente card S047 preprint pp. 14, 19]), with gradients withheld from both, each finite-difference gradient charged n calls and every call at both levels counted; the exact-gradient robust local search is a reference line only. Score each iterate's worst case, enumerated on a fine mesh as his annealing paper checked its optimum [dimitris-bertsimas card S141 p. 7], against calls; report the calls needed to come within a stated tolerance of the robust local minimum each run ends in, beside the enumerated global robust optimum, and how often a fresh dense search finds a worse error than the one each method accepted.

**FL5 · deciding test:** Dey's protocol (cumulative gap, cumulative time, exact count, and a gap-against-time plot that prunes dominated rungs) [santanu-s-dey card S129 pp. 20–21] on the RPT papers' families at n ≥ 20, regenerated from their printed descriptions, and on QPLIB's continuous QPs and QCQPs plus MINLPLib's integer instances of those classes where they exist; arms: RLT products only, RLT plus the simplex-type equalities times the convex terms, and all-pairs RPT, each with and without the LMI, plus a cheaper outer approximation in place of the LMI (Sahinidis's Method 5); current BARON and SCIP releases at defaults, one thread, one limit; an instance counts as exact only where some solver certifies its optimum, otherwise report the gap to the best feasible value found; count numerical failures (UNKNOWN statuses, stalls, runs with no solution).

Source: [council roundtable, Step 3](council-roundtable/SKILL.md#step-3--cross-examination-member-agents-13-rounds). The later DECIDING TEST fields of each item are in the [Discussion](#discussion).

</details>

#### 4. Reformulation ideas (the lead's)
- Cuts reused across k [S288 p. 11].
- Dual-norm worst cases for linear blocks [S019 pp. 3–4]: an inferred transfer. Nocedal accepts the reduction; he and Vicente contest its Example III bracket at the rim.
- Structure-chosen products [S415 p. 30; S708 p. 42] *(citation not confirmed in full: S415: card c2-08 gives partial constraint multiplications and partial generation of product variables as future work, p. 30, but no choice by structure; S708: card s2-18 gives partial multiplications, selective products and iterative constraint generation as future work, p. 42, but no choice by structure)*. The lead's opening notes that Dey's rung of this kind is "not advisable" in higher dimensions [santanu-s-dey card S129 pp. 18, 23].
- Sahinidis's alternative, cheaper cuts that emulate the LMI, carries his caveat: "The cheap emulation is shown only for MIQPs with linear equality constraints (arXiv:2106.13721, checked)."

#### 5. What the user decided
Nothing yet (autopilot). The lead's assumptions until the user answers: design only, with the papers' own limits.

Decisions for the user, with who asked:
- Run the arms, or design only (the lead).
- Item 1: which solver releases (Huangfu, Gould), and the time limit that defines "tractable" (the lead).
- Item 2: whether the certificate itself is needed (Nocedal).
- Item 3: printed polynomials or a true simulator (the lead), access to EM (Audet), simulator noise (Nocedal).
- Item 4: a licensed current BARON, since the free build handles only 10 variables and constraints (Sahinidis); an SDPNAL+ arm (Burer); the integer sequel's code requested from the authors or rebuilt (the lead).

#### 6. Open questions
Listed with this draft.

1. Run or design: should the plan budget actual runs of these deciding tests on your machine and solver licences, or only design them? This is the Problem Card's question; the plan assumes design only.
2. Item 1: which MIO solver releases, oldest to newest, can you license and run on one machine (Huangfu, Gould)? Old releases may not install, or may no longer be licensable.
3. Item 1: which limit defines 'tractable' for the frontier: S010's 1% gap or 15 minutes per k [S010 pp. 31–32], or one you set (lead)?
4. Item 1 (unresolved): may a move of the certified frontier alone carry 'now tractable' (lead), or is it 'context-only' without the net ratio (Huangfu)?
5. Item 1: S040 states no machine and no seeds, and describes its random designs only loosely [S040 pp. 10, 22] *(citation not confirmed in full: card c12 records no stated machine and 'random X and β' (p. 10), not the missing seeds; the paper text never mentions seeds)*. The rebuild's reproduction gate can therefore only match distributions, and a rebuilt 2009 code is not the original (Huangfu, Gould).
6. Item 2: does anyone downstream need the certificate itself (a proved ℓ0 optimum), or only the out-of-sample statistics (Nocedal)?
7. Item 2: does S061's band, 'statistically relevant but computationally not feasible' [S061 p. 16], exist at SNR 1 or 0.05? S061 tested only √SNR ≥ 3 and took best-found solutions at its time limit [S061 pp. 14, 16]. If the band is empty, the certificate keeps only its role in the theory, where the statistics of stopped solutions are still open [S010 p. 58].
8. Item 3: is a claim bracketed on the papers' printed polynomials enough, or must it hold on a true simulator, where only refereed lower bounds exist (lead)?
9. Item 3: can you obtain the 100-variable electromagnetic simulator and its error data (Audet)? The card shows collaborators' code and privately communicated error data, with no release stated [S090 pp. 12, 18].
10. Item 3: are your simulators exact to roundoff, or noisy because of iterative or adaptive solves (Nocedal)? Exact simulators drop his noise stage.
11. Item 3 (unresolved): where worst errors tie, do several short ascents with a history set beat one inner solve tied to the outer radius? No card runs this comparison, and search depth is unsettled even within the lead's method [S090 p. 15]. A referee validated on two printed polynomials may still fail on the 100-variable simulator (Audet's risk).
12. Item 4: can you run a licensed current BARON? Its free build handles at most 10 variables and constraints (minlp.com, checked), below this item's n ≥ 20 (Sahinidis).
13. Item 4: should the test add a first-order LMI arm that needs a separate released SDP code (e.g. SDPNAL+, which runs in MATLAB), or keep the RPT papers' MOSEK stack only (Burer)?
14. Item 4: should the plan ask the authors for the integer sequel's code (none was found) *(unverified)*, or rebuild it from the printed algorithm with a stop test over all open nodes (lead)?
15. Item 4: the deposit uses different α and β values from the printed ones, which the card reader found infeasible [S415 pp. 26–27, 46], so for those instances the deposit, not the print, is the definition. What changed inside BARON after 2021 is one of this lens's blind spots, so this lens offers no causal reading of any gap in the engine ledger.
16. Process: the seated challengers (Sahinidis on items 1–2, Conn on item 3, Dey on item 4) have no statement in this transcript; their sides enter only through FL1, FL2, FL4 and FL5. Their sign-off, or a `round`, is needed before checkpoint 4.
17. Scope: SD and DA were not on the agenda, and AP entered only as item 3's testbed. With no decision owner (assumed), each item is scored on its own metric, not against an owner's current rule.
18. For the moderator's Step 5: Sahinidis wrote 'BARON 2026.9.10'; minlp.com lists the release as 26.9.10 (10 September 2026).

**Moderator's neutrality note.** Struck because they were not argued at the table (the lead may restore them at sign-off; the user decides at checkpoint 4):
- item 2's "L0Learn 2.1.0 and relaxed-Lasso regression arms (ML §6.1, point 1; CRAN, checked)";
- the reformulation idea "Box certificates when bounds stall [S010 pp. 34–36]".

The footnote's L0Learn (L0L2 penalty) and glmnet relax-option checks are struck with them.

*Checked 2026-10-31 by the lead: leaps 3.2 and glmnet 5.2, on CRAN; BARON 26.9.10 and its 10-variable free build (minlp.com); SCIP 10.1.0 (scipopt.org); github.com/INFORMSJoC/2023.0345 (Julia, `use_lmi`); BARON relaxation-only constraints (AIMMS BARON guide) (citation not confirmed: the quoted phrase is in the BARON user manual, minlp.com/baron-user-manual, §4.1, declared through RELAXATION_ONLY_EQUATIONS, §10.2; the AIMMS page describes the facility but does not contain the phrase); SDPNAL+ (MATLAB; arXiv:1710.10604).*

## Sign-off on v1

Every lens asked to sign the programme plan (the lead and each delegate seated on an item), verbatim:

- [Bertsimas lens] ✅ sign-off: Every item names incumbent, class with solve-time test, certificate or bound, metric (convener rule). Restored: item 2's L0Learn and relaxed-Lasso arms (agenda: ML §6.1, point 1). Method 4: item 4's engines add CPLEX and exact MIP reformulations, which beat RPT on some instances [S377 p. 29; S708 pp. 37, 40].
- [Huangfu lens] ✅ sign-off: Sign-off. The plan keeps my five additions verbatim, the rebuild's proved-cells gate (→ Huangfu · H3) and net ratios only on cells both arms certify (→ Method 4, step 4). My context-only rule (→ Workflow E, step 5) stays quoted as unresolved, for the user at checkpoint 4.
- [Gould lens] ⚠️ dissent: In my accepted rule, "both 2009 arms" means S040's rebuild as printed and with best-bound node selection, since S040 lists depth-first search among its limits [dimitris-bertsimas card S040 p. 16] (→ Gould · Method 5, steps 2–3). Item 1's then-arms and backup rule 1 omit the second. (holds if With the best-bound rebuild added to item 1's then-arms and backup rule 1, I sign.)
- [Nocedal lens] ⚠️ dissent: Item 2 (items 1 and 4 lie outside my evidence): its readings may credit the bound as stopping instrument through stop (2)'s ten-draw spread, an oracle users lack (→ Nocedal · Method 3, stop rule). (holds if Those readings score a one-sample stop (2) (design inferred), tabulated against the oracle [S018 p. 20].)
- [Wright lens] ✅ sign-off: Signed, on item 2's protocol only (MIO lies outside my evidence). My contest stands verbatim, unresolved; my p ≤ 12 enumeration is in; 'The stall twin ties → no default certificate' matches my twin rule (→ Wright · Method 4) [03 §1.2]. (holds if Holds while that contest stays open: no band certified on beating stop (2) alone (→ Wright · Method 5 stop rule).)
- [Vicente lens] ✅ sign-off: Sign-off. Item 3 quotes me accurately. Example III's error set is one 18-D ball, ‖Δ‖₂ ≤ 0.5 [dimitris-bertsimas card S090 p. 14; §6.4.1 checked]: the rim objection stands, and the angle mesh replaces my opening's multistart scorer (→ Vicente · H10). Items 1, 2, 4: outside my evidence.
- [Audet lens] ⚠️ dissent: Dissent on switch rule 3: 'EM keeps the heuristic label' is every simulator claim's default, dropping my calibration gate's consequence. Sign if it reads: failed referee calibration, or calibration on a voided bracket → EM reports found lower bounds only, no 'unrefuted at budget B', no inner-rule ranking (→ Method 3; E12). (holds if Switch rule 3 reads: failed referee calibration, or calibration on a voided bracket → EM reports found lower bounds only, no 'unrefuted at budget B', no inner-rule ranking.)
- [Sahinidis lens] ⚠️ dissent: Dissent, item 4 only: "two libraries" can be the dikes and the deposited instances, both RPT test sets; the agenda asks "not only the RPT papers' own families". A development-set claim needs a hold-out (→ Sahinidis · Workflow D). I sign if one is QPLIB or MINLPLib. (holds if Item 4's decision rule: at least one of the two libraries on which the LMI must out-prove every cheaper arm is QPLIB or MINLPLib, outside the RPT papers' own test families.)
- [Burer lens] ⚠️ dissent: Ledger (1) counts proofs only at 10⁻⁴, where first-order tails are slow [S014 preprint pp. 2, 15–17], so splitting can lose for solver reasons (→ Burer · Method 6). I sign if every arm also reports one looser common gap, my quoted “the LMI itself does” needing losses at both. (holds if Every ledger-(1) arm also reports proofs at one looser common gap (e.g., 10⁻³, a decade looser, like the two levels in [S014 preprint pp. 15–16]; catalog E6), node-solve accuracy matched to each gap (H7); “the LMI itself does” holds only where splitting loses at both.)

*Moderator's notes*

- **Tally:** four sign-offs (Bertsimas, Huangfu, Wright and Vicente; Wright's holds only while his contest stays open) and five dissents, each with the condition under which it would sign (Gould, Nocedal, Audet, Sahinidis and Burer).
- **Owed before checkpoint 4:** Conn (item 3) and Dey (item 4) sat as challengers and had no turn; Sahinidis, challenger on items 1 and 2, had no turn there and signs as item 4's delegate (see the plan's open question on process).
- **Not argued at the table:** the lead's sign-off restores item 2's L0Learn and relaxed-Lasso arms, which the neutrality note had struck, and adds CPLEX and exact MIP reformulations to item 4's engines; neither was argued at the table, so both stand as the lead's proposals for the user at checkpoint 4. The box-certificate idea stays struck. The verifier's checks covered the turns and the plan, not the citations in these sign-offs.

## Challengers' round

This round ran after the first draft plan (v1) and its sign-offs: each challenger read the item's record and v1 before opening, then had one round with the lead (his answer and the challenger's rejoinder); nothing argued here changed v1's turns, which stand above as given, and the second verification's findings are inserted in italics (see [Verification](#verification)).

### Item 1 · What may a "why now" speed-up rest on? · challenger Sahinidis

#### Opening

**[Sahinidis lens, challenger]**

**POSITION:** Partly outside my evidence (best-subset MIQO; parallel scaling, a blind spot): I speak to protocol. Agree: measure a why-now by rerunning releases on one machine and one set, varying only the code, as my lens does. (1) The then-limit is borrowed too: two of the lead's cards put leaps at p ≤ 30 or about 40, with no run, and leaps() stops above 31 columns at its default; run regsubsets exhaustively, or 'p ≤ 30' is confirmed by a default. (2) Equal tasks: regsubsets returns every size in one run, so every arm gets the whole k = 5–25 path under one total budget. (3) 'Exact' is a tolerance: print the frontier at 1% and at 10⁻⁶; the headline names its gap. On open question 4, a moved frontier may carry 'now tractable' only where it also moves on sets the proposer did not build, reported per set.

**WHY (method refs):** (→ Sahinidis · Method 2, step 6) Progress means old and new versions rerun on the same hardware and set, varying only the code. My lens's why-now is a solved count with a speed factor beside it, both on one fixed set [02 X7; 03 §B1, ASR]. Its protocol: one thread, 500 s, 10⁻⁶ relative and absolute gaps [03 §B1]. FL1 (b), the thread sweep, is outside my evidence: one firm manual line, which measures nothing [03 §D4]. (→ Heuristic 4; [03 §B3]) Each baseline runs in its strongest fair mode. In leaps 3.2, leaps() errors above 31 columns at its default. regsubsets needs really.big = TRUE beyond 50 variables and nvmax ≥ 25 (default 8), and returns the best model of every size in one run (CRAN manual, checked). The limit is stated, not run [dimitris-bertsimas card S010 pp. 2, 5; dimitris-bertsimas card S396 p. 2]. In 2020 both sides' timings fell to unequal tasks. My lens's group read BPV's timing as 'a single cardinality-constrained solution set' against the full path; HTT called the group's own timing 'misleading' for different model sizes [02 J3; 05 A8 8e]. (→ Heuristic 7; Integrity 5) Claim 'global within tolerances', never more. (→ Workflow D stop rule; [02 X4]) A development-set claim needs a hold-out *(citation not confirmed: note 02 X4 is per-library reporting; the hold-out rule is note 02 X2)*. Treating Example 1 as the development set is inferred.

**FIRST EXPERIMENT / DECIDING TEST:** FL1's deciding test, as argued, with the lead's frontier and every accepted addition, plus:

(1) The leaps arm runs regsubsets(method = "exhaustive", nvmax = 25, really.big = TRUE), never leaps() at its default, and prints where it stops for time, not for a cap (→ Heuristic 4).

(2) Every arm gets one task: the whole k = 5–25 path under one total budget, the per-k rule summed (21 × 15 min). S010's per-k stop [dimitris-bertsimas card S010 pp. 31–32] stays an MIO setting inside that budget. Time to each k is printed (→ Heuristic 4; [02 J3]).

(3) The frontier is printed at a 1% gap and at 10⁻⁶ relative and absolute gaps (→ Heuristic 7; [03 §B1]).

(4) Example 1 is reported apart from Diabetes and Gould's frozen real designs, never pooled (→ Workflow C checkpoint; [02 X4]).

(5) The last passing and the first failing p are rerun in isolation. If either flips, use a deterministic work limit where the release has one; otherwise report the frontier as a band (→ Heuristic 6; [02 X6]).

Settles: 'p ≤ 30' stands only if exhaustive regsubsets cannot finish the path at p = 31 within the budget. 'Now tractable' stands only where certification moves on the sets the proposer did not build, at the gap the headline names.

**RISK — WHERE I COULD BE WRONG:** Statistics and MIQO lie outside my record, so each transfer here is inferred. That includes the link between leaps()'s 31-column default and the '30' on the lead's cards. Exhaustive regsubsets may still time out near p = 30–40. Then 'p ≤ 30' survives, only now resting on a run. 10⁻⁶ comes from my global-MINLP protocol; on MIQO it may time numerical tails rather than search. My own record falls short of this standard. Its progress claims are oral (ASR), on an unnamed set, with figures that differ between talks [02 C5; 03 §B1] *(citation not confirmed: note 02 C5's 2021 figures come from a press article (S42), not a talk; only the 2025 figure is from a lecture, ASR)*. BAM's progress figures rest on its development libraries, with no hold-out [03 §E2]. The 2017 ALAMO paper asserted this very why-now (best subset now practical at hundreds or thousands of regressors), with no citation and no run [02 P4; arXiv:1705.10918v1 p. 3, checked]. Its p. 4 called the R leaps package "limited to only 32 regressors" (checked).

**QUESTION FOR USER:** Do you have best-subset designs of your own, outside the papers' generators, to serve as the hold-out set?

#### The lead's answer

**[Bertsimas (lead), answer to the challenger lens]**

**POSITION:** Conceded: the then-limit is borrowed. My cards put leaps at p ≤ 30 [S010 pp. 2, 5] or about 40 [S396 p. 2], neither from a run, and S040 warned that random data may flatter run times [S040 p. 13]. I accept his five additions, refining (1): regsubsets takes no time limit, so its overrun is printed [S340 pp. 26–27]. Held: one problem (1), the frontier as score, S010's own 1% row beside 10⁻⁶. Added: a finished regsubsets path is exact, so it audits every MIO certificate. v1 changes: item 1's then-arms, budget, p-grid, metric and instances; backup rule 1; ledger lines 1 and 3; open questions 3–4. Stops at: measured tractability, the then-limit included.

**WHY (method refs):** (→ Method 2, checkpoint; Integrity Rule 2; IO, ML) Time the class or call the figure borrowed. The then-limit is such a figure. S010 gives leaps' reach as p ≤ 30 [S010 pp. 2, 5] and S396 gives about 40 variables [S396 p. 2]; neither comes from a run, and S010 names no leaps release (paper text searched). The best-subset benchmarks are a Blind spot of mine (Roundtable Card). The leaps 3.2 manual (CRAN, published 2024-06-10; read 2026-10-31) bears out his reading. At its default strictly.compatible = TRUE, leaps() stops with an error above 31 columns. regsubsets defaults to nvmax = 8 and needs really.big = TRUE for exhaustive search beyond 50 variables. It returns the best model of each size up to nvmax and takes no time-limit argument; the manual says really.big guards a long, uninterruptible run. Whether S010's 30 is that cap is unknown (inferred link).

(→ Method 4, steps 3–4; Workflow C, step 2; Integrity Rule 3) Every method gets one budget, with overruns printed and gaps reported. S010 already solved the k-path as one model, adding Σz ≤ k by callback and stopping each k at a 1% gap or 15 minutes [S010 pp. 31–32]. One total budget therefore fits it and binds the then-arms. The 2020 timing point concerned BPV; it is recorded in both teams' notes and on no card (ML §6.1, point 1). S010 offers those times as showing it tractable to solve to optimality, under that 1% stop [S010 p. 32, paper text]. His (3) is therefore my Integrity Rule 3 and my Workflow E checkpoint. Beside an exact leaps finish, a 1% MIO frontier is an unequal task (inferred).

(→ Method 4, one problem; Method 1) The guarantee reaches (1) only with provable bounds [S010 pp. 15–17]. Warm-start bounds are not provable, and the certified runs do not say which bounds they used [S010 pp. 17, 28–29]. A finished exhaustive search is the certified ground truth his Method 4 asks for [nikolaos-v-sahinidis SKILL.md, "Method 4 · Enter with a benchmark; judge by certified ground truth and portfolios"].

(→ Workflow C, steps 2–3) Real data beside synthetic, in a critic's regimes. S040 warned that random data may flatter run times [S040 p. 13], so his hold-out rule becomes mine for time claims (inferred transfer). Reporting per set, never pooled, with reruns made deterministic, is his Workflow C checkpoint [nikolaos-v-sahinidis SKILL.md, Workflow C]. His strongest-fair-mode rule [same SKILL.md, Research Heuristics, 4] also admits Gould's best-bound rebuild.

**FIRST EXPERIMENT / DECIDING TEST:** FL1's deciding test, as argued, with my item 1 reply's (i)–(iii), every addition accepted at the table and Sahinidis's (1)–(5) as written, refined and extended as follows.

(1′) His leaps arm solves (1) itself: regsubsets(method = "exhaustive", nvmax = 25, really.big = TRUE, intercept = FALSE), on the same X and y the MIO arms solve [S010 p. 2]. It takes no time limit, so I treat it as S340 treated a method it could not cap [S340 pp. 23, 26–27]. Its finish time and any overrun past the 315-min path budget are printed, under an outer ceiling stated before the runs. The MIO arms are also scored at that longer time. Only a finish within 315 min counts toward its frontier.

(iv) p-grid: Example 1 at n = 1000, on its ρ and SNR grid [S010 pp. 26, 30–31]. The grid starts at p = 30, not at 50 as in my reply, and runs past regsubsets' last finish to each MIO frontier. His p = 31 rule and (v) then both lie on the grid.

(v) Ground-truth audit: wherever regsubsets finishes, every MIO arm must show LB_k ≤ RSS_k ≤ UB_k for each k. Both sides use one objective scale, within a tolerance fixed before the runs. A lower bound above RSS_k voids that arm's certificates: they covered a bounded problem, not (1) [S010 p. 17]. That arm is rerun on formulation (8) or on provable bounds [S010 pp. 10, 15–17]. An incumbent below RSS_k means the arms solve different problems or leaps erred; that is fixed before scoring.

(vi) Against regsubsets, Huangfu's net ratio sets the MIO's time to 10⁻⁶ against regsubsets' finish time, on cells both complete (inferred). Against the 2009 rebuild, the ratio is taken at the gap that rebuild prints.

(vii) The same strongest-fair-mode rule applies to the other then-arm: S040 is rebuilt as printed and also with best-bound node selection (Gould's sign-off condition, accepted).

Settles:

- 'p ≤ 30' is settled by his rule, and rests on a run either way.
- 'Certified' is settled by (v); each MIO frontier is labelled 'audited to p = …'.
- 'Now tractable' is judged per set, never pooled: Example 1; Diabetes; Gould's frozen real designs; any hold-out the user supplies, each fixed before any run. It stands only where the frontier, or the count of certified paths, moves at the gap the headline names. A move on Example 1 alone narrows the claim to 'on S010's generator' (→ Workflow E checkpoint).
- Huangfu's context-only rule stays with the user (open question 4).

**RISK — WHERE I COULD BE WRONG:**

- A then-limit run on today's machine prices the code alone, which is the share a why-now may claim on one machine. It cannot say what leaps did on 2014 hardware (inferred).
- The audit reaches only the p where regsubsets finishes. Above that p, certificates rest on the MIO's own bound again.
- At 10⁻⁶, QR-based residual sums and the solver's objective may differ by roundoff. A badly set tolerance would void sound arms or pass unsound ones (inferred).
- intercept = FALSE reproduces (1) only if every arm sees the same centred data. The card gives standardized columns, not how y was treated [S010 p. 2].
- The hold-out may not exist. Real designs with known truth are scarce, and planted β may flatter certification (Gould's risk). Then 'now tractable' stays narrowed to S010's generator.
- My own record falls short of this standard. S010's headline scale has no certification table [S010 pp. 1, 6, 30–31], and S396 opens on a borrowed solver-and-hardware figure [S396 p. 2].

**QUESTION FOR USER:** Which gap should a 'now tractable' headline name: S010's 1% within 15 minutes per k, 10⁻⁶, or one you set? (This replaces open question 3.)

#### Rejoinder

**[Sahinidis, challenger rejoinder lens]**

**POSITION:** Accept: (1′), (iv), (vi), (vii), 10⁻⁶ beside S010's 1%, and per-set reporting. Accept (v), refined: a finished regsubsets path is global within tolerances, not exact. leaps(), its wrapper, is documented as a branch and bound, and regsubsets 'does not actually fit each model'. So one evaluator refits every reported support on one frozen, centred file, and no arm's LB_k may exceed the best refit RSS_k by more than 10⁻⁶. Above regsubsets' reach, this check still refutes bounds, like item 4's rule. Contest: Diabetes is a set S010 already ran and reported [dimitris-bertsimas card S010 pp. 11, 26]. Moves there and on Example 1 read 'on S010's instances'. An unscoped 'now tractable' needs a set fixed before any run by someone who tunes no arm.

**WHY (method refs):** (→ Heuristic 7; Integrity Rule 5; Tension 7) Any floating-point search earns 'global within tolerances', never 'rigorous'. Independent testers found wrong claimed optima in BARON itself [05 A1 1c, 1h]. I read the leaps 3.2 manual today (CRAN, 2024-06-10). It describes leaps() as 'a compatibility wrapper for regsubsets' that searches 'using an efficient branch-and-bound algorithm'. It says the search 'does not actually fit each model' and documents no tolerance, so this label for it is inferred. (→ Method 5, step 5; [03 §D2]) Check every answer natively before using it (MIQO: inferred). The SCIP 8 study failed runs whose bounds contradicted the library's [05 A1 1h], and item 4 adopted my cross-arm rule. (→ Workflow D stop rule; Method 4, step 4) A hold-out is a set that had 'not been seen by developers' [02 X2].

**FIRST EXPERIMENT / DECIDING TEST:** The lead's (1′) and (iv)–(vii) as written, with (v) and the settle rule refined.

(v′) One least-squares evaluator refits every reported support: regsubsets', and each arm's incumbent and warm start. It works on one frozen file, with X standardized as in S010 and y centred [dimitris-bertsimas card S010 p. 2] *(citation not confirmed for y: card p. 2 covers X's columns only; S010's paper text p. 26 centres the response for Diabetes and Leukemia, not for the synthetic examples)*.

- The bound check: per k and cell, an arm loses its certificates if its LB_k exceeds the smallest refit RSS_k by more than max(10⁻⁶, 10⁻⁶·RSS_k). That tolerance is fixed before the runs [03 §B1]. Every breach's size is printed.
- The lead's incumbent branch stands, judged on the refits.
- Labels: 'global within its gap, audited to p = …' up to regsubsets' last finish; 'cross-checked only' above it.

Settles:

- Moves on Example 1 and Diabetes read 'on S010's instances'.
- The unscoped 'now tractable' stands only where certification also moves, at the gap the headline names, on a set fixed before any run by someone who tunes no arm (→ Workflow D stop rule).

**RISK — WHERE I COULD BE WRONG:** The refits may match regsubsets' own RSS to roundoff, which would make (v′) a formality. 10⁻⁶ is my global-MINLP tolerance, not an error level measured on MIQO. A sound bound may breach it through arithmetic alone, which is why each breach's size is printed (inferred). Above regsubsets' reach, the check can refute a bound but never confirm one. Treating S010's reported sets as its development sets is inferred, and an outside set may not exist; then the claim stays 'on S010's instances'. My own record falls short of this rule: BAM's claims rest on its development libraries [03 §E2].

**QUESTION FOR USER:** Will you pick and freeze the hold-out designs yourself, before any run?

> **Moderator summary.** **Agree:** The then-limit is borrowed too, since two of the lead's cards give leaps' reach (p ≤ 30, about 40) with no run: leaps therefore runs as exhaustive regsubsets on the MIO arms' own X and y, with its finish and any overrun printed; every arm gets the whole k = 5–25 path under one budget; frontiers are printed at S010's 1% and at 10⁻⁶; the last passing and first failing p are rerun in isolation; sets are reported apart, never pooled; S040 is also rebuilt with best-bound node selection; and wherever regsubsets finishes, it audits every MIO certificate.
>
> **Split:** Whether a finished regsubsets path is exact (the lead) or "global within tolerances, not exact" (Sahinidis, whose (v′) refits every reported support with one evaluator and voids an arm's certificates when its LB_k exceeds the best refit RSS_k by more than a tolerance fixed before the runs); and which sets may carry "now tractable": the lead narrows a move on Example 1 alone to "on S010's generator", while Sahinidis reads moves on Example 1 and Diabetes as "on S010's instances" and asks, for an unscoped claim, for a set fixed before any run by someone who tunes no arm. Huangfu's context-only rule stays with the user (open question 4).

### Item 2 · What does proof time buy a statistical estimator? · challenger Sahinidis

#### Opening

**[Sahinidis lens, challenger]**

**POSITION:** Partly outside my evidence (ℓ0 selection statistics); I bring protocol, bounds and my group's 2020 discussion of S095 (in both teams' notes; on no card). Agreed: a stopped run is evidence, not proof; print every gap (→ Sahinidis · Heuristic 7). Contested in v1: (1) S095 ran ncvreg's MCP and SCAD; ENet and SCAD appeared to dominate at high noise and correlation [dimitris-bertsimas card S095 pp. 10, 12]; v1 omits ncvreg (→ Heuristic 4). (2) v1 fixes γ a priori; S095 cross-validates k and γ [dimitris-bertsimas card S095 pp. 5–6], and that discussion would not turn to CIO/SS in the general case, citing "lack of seamless hyperparameter selection and tuning" [02 C2] (→ Method 4). (3) Proof pays only where a closed-gap run beats every arm; where none closes, as in S061's band [dimitris-bertsimas card S061 p. 16], that is a capability gap, not a band to certify (→ Heuristic 1).

**WHY (method refs):** (→ Heuristic 7; Workflow C output) A stopped run shows a value, not optimality [02 J4], and a heuristic earns trust when paired with a bound [02 T7]: every stop prints its gap, and capped runs are tabulated apart from closed-gap ones (solved and unsolved apart). (→ Heuristic 4; Method 4 steps 3–4) Each rival at defaults, in its strongest fair mode: my group's 2020 runs used ncvreg, L0Learn and the authors' code [02 X6]; S095 also found MCP making fewer false selections on its real design [dimitris-bertsimas card S095 p. 21]. (→ Anti-patterns, unfair timing) v1's whole-path rule matches my group's 2020 objection to S095's timing [02 J3] (agreed). But HTT's rejoinder judged my group's own timing misleading because the methods covered different model sizes [05 A8 8e], so all paths need one model-size grid. Tuning is priced too: the same discussion called labour-saving implementations with full paths and cross-validation essential for adoption [02 O2], and ML §6.1, point 1's own test times full (k, γ) paths. (→ Heuristic 6) A time-limited run can stop at a different node on a loaded machine, and the manual prefers work limits for reproducible experiments [02 X6]; here the stopped incumbent is the statistic. (→ Heuristic 2; Method 1 steps 1–3; Workflow B1 steps 2, 4, 6) Bounds before reformulation [02 X5]. S288's large M or γ leave most gaps above 100%, certificates come only at p ≤ 200 with M from the truth, and time grows steeply with M and γ [dimitris-bertsimas card S288 pp. 16–17, 29–30]. S010 already tightens bounds by convex QPs at the incumbent's loss [dimitris-bertsimas card S010 pp. 16–17], Method 1's optimality-based reduction (transfer inferred). (→ Method 4 step 6; Workflow D) There is no single winner [02 J1]. The 2020 discussants agreed the lasso tends to do better at low SNR and best subset at high SNR [05 A8 8d], so cells may split. The proposers' own generators are a development set and need a hold-out, reported per family [02 X2, X4]. Stage (inferred, on the convener's list): the price is not yet timed on equal tasks, so the item stops at knob and price, before the certificate.

**FIRST EXPERIMENT / DECIDING TEST:** FL2's deciding test, as argued, with the additions accepted at the table, refined in five ways (designs inferred):

(a) Arms at defaults, each in its strongest fair mode: the MIO as printed; glmnet (Lasso, ENet, and the relaxed Lasso through glmnet 5.2's relax option, verified in this session); L0Learn 2.1.0 with L0L2 and its own cross-validation; ncvreg 3.16.0 with MCP and SCAD (both on CRAN, checked); and Glasso, MB and QUIC (unverified) *(unverified: QUIC only; glasso 1.11 and huge 2.0.1, method "mb", are on CRAN, checked)* on S288's designs.

(b) Price: each method's whole selection pipeline, timed end to end over one model-size grid fixed in advance (λ calibrated to each k, as S095 does [dimitris-bertsimas card S095 p. 12]), plus one γ grid wherever a ridge term exists; one machine, one thread, named versions, pinned seeds.

(c) The MIO's 60 s, 5 min and 1 h stops become deterministic work limits, calibrated once on an idle machine (Gurobi's WorkLimit, checked, if Gurobi is the solver), with seconds printed beside.

(d) Wherever big-M is used, compare the a priori M0 with bounds from the incumbent (S010's convex QPs [dimitris-bertsimas card S010 pp. 16–17]; for S288 a per-entry analogue, inferred), with that reduction on and off. Each certificate names its bounds. An M scaled from the warm start is not provable, so its certificate covers only the bounded problem [dimitris-bertsimas card S010 p. 17].

(e) One hold-out design family, fixed before any run and used by neither S095 nor S288. Every table is reported per family, SNR and ρ, never pooled.

Reading: certification pays in a cell only where a run that closed its gap beats both its own earlier stops and every other arm by more than one SE in FDR or test loss, with its price printed beside. Capped runs are reported apart. Elsewhere the cell lists its non-dominated arms, and the plan ends with the smallest covering portfolio and the cells it leaves open (→ Method 4 step 6).

Switch rule (refines backup rule 2): gaps above 100% → tighten bounds first, then reformulate. If gaps are still open at p ≤ 200, record a capability gap: there is no certificate there to price (→ Workflow B1 steps 2, 4, 6).

Kill result: if a closed-gap run stands alone on the frontier in some hold-out cell, the certificate pays there and my portfolio reading fails in that cell.

**RISK — WHERE I COULD BE WRONG:** (1) My own practice pays the price of exactness. ALAMO's best subset by integer programming can take four or five orders of magnitude longer than the lasso, accepted for simpler models (ASR, approximate) [02 J5], and my notes leave that unreconciled with the 2020 stance [02 C2]. If the selected model will be read or embedded in an optimization, my portfolio reading may undervalue the exact fit, though Method 3's stated range is a few dozen inputs [05 A8 8c], far below p = 2,000. (2) The two teams' notes disagree on whether my group re-ran CIO/SS or took S095's printed numbers (ML §6.1, point 1; [03 §F3]), so my 2020 record may rest on published figures. (3) The bounds arm is an inferred transfer: on S288's precision matrices, per-entry bounds need one convex solve each and may cost more than they close (Method 1 step 4: ration them). (4) Gurobi promises the same stopping point only on the same hardware and settings (checked). (5) Honest hold-outs are hard: one of my own notes reads my 2013 hold-out, a transformation of the same problems, as weak [SKILL.md, Method 4].

**QUESTION FOR USER:** Will the selected sparse model be read or embedded in a later optimization model (where my record pays the exact price), or only used to predict and select?

#### The lead's answer

**[Bertsimas (lead), answer to the challenger lens]**

**POSITION:** Conceded: v1 dropped ncvreg, whose SCAD and MCP S095 printed ahead in places [S095 pp. 10, 12, 21]; FL2 fixed S288's starting scales [S288 p. 11], though S095 cross-validates k and γ [S095 pp. 5–6]; the price is untimed on equal tasks [S095 p. 11; S061 p. 13], so item 2 stops at knob and price (fix: whole tuned pipelines, one model-size grid); and only a closed gap shows proof paying: a capped win is search (Nocedal), and S061's "computationally not feasible" band [S061 p. 16] is a capability gap. Held: proof time is read against the run's own stops, the MIO also warm-started from L0Learn; his every-arm rule decides whether certifying becomes a default. Changes: test field.

**WHY (method refs):** (→ Method 4 step 5; Heuristic 4) Duel the rivals' standard codes: S095's were glmnet and ncvreg [S095 p. 10], and its losses are printed [S095 pp. 12, 21]. (→ Method 4 steps 3, 5; Blind spots: "benchmarks of the 2016–2017 best-subset papers") One budget, path to path: S061 times one known k against glmnet's whole path [S061 p. 13], and HTT's rejoinder agreed with his group's timing point [nikolaos-v-sahinidis note 05 §A8, row 8e]. With the price unmeasured, the item stops at knob and price (Activation Rules, "As convener"). (→ Method 3 steps 2, 5) γ moves both the statistics and the gap: on S288 the large M or γ needed leave gaps above 100% [S288 pp. 16–17], and time grows steeply with them [S288 p. 16]. (→ Method 4 steps 2, 4–6) The incumbent heuristic should be both warm start and opponent, yet S095 started from its own relaxation [S095 p. 6]. Started from L0Learn's support (feasible for the cardinality constraint; inferred), the MIO's later incumbent changes are search and the rest is proof (Workflow C step 4). Steps 4 and 5 are separate: the certificate is read against the run's own stops, the duel decides the default, and step 6's where-it-wins map is his portfolio (HTT's observations "still valid but less obvious" [S095 p. 23]). (→ Method 4 stop rule; ML §7, point 2) Where nothing closes, drop *certified*: S061's transition runs kept the best solutions found by 15 minutes [S061 p. 14], a regime already on my open-problem list. Our orders differ: his puts bounds first, my stop rule the big-M-free form first [S061 pp. 6, 9–10]. Both are arms, so the runs decide. Held on the 2020 record: whether it re-ran CIO/SS (nikolaos-v-sahinidis note 03 §F3) or reused BPV's numbers [05 §1.4], no gap is recorded for its CIO runs, and BPV's own stopped at 60 s without one [S095 p. 5]. It priced an uncertified CIO, not proof time.

**FIRST EXPERIMENT / DECIDING TEST:** FL2's deciding test, as argued, with the additions accepted at the table and Sahinidis's (a)–(e). v1 changes (designs inferred):

- Item 2's stage: knob and price, then certificate or gap.
- Arms: his (a) (ncvreg 3.16.0; L0Learn 2.1.0 through L0Learn.cvfit with penalty "L0L2"; glmnet 5.2's relax option: CRAN, checked), plus the MIO warm-started at each k from L0Learn's solution, with the ridge weight mapped between the two parametrizations.
- Settings: the M and γ grids start at S288's a priori scales [S288 p. 11], γ doubled as in S095 [S095 pp. 5–6], tuned on validation, never set from the truth. Each certificate names its problem: a valid M (from S010's convex QPs [S010 pp. 16–17]) or the M- or γ-bounded problem [S010 p. 17; S288 p. 8].
- Stops: his (c), calibrated per design family rather than once, since the length of a work unit "greatly depends on" the model (Gurobi parameter reference, checked); seconds printed beside.
- Hold-out: his (e), drawn from a critic's released designs (Workflow C step 3).
- Backup rule 2: his switch rule, with its order (bounds, then reformulation) left to the runs, since both are arms.
- Open question 7: S061's band becomes a capability gap, mapped by my n-sweep (b).

Reading (replaces v1's), per family × SNR × ρ, never pooled:

(V1) Running to a closed gap pays where a run that closed at the validation-chosen (k, γ) beats its own earlier stops (warm start included) and every twin (Wright's longest stall window included) by more than one SE in FDR or test loss.

(V2) The cell lists its non-dominated arms, each with its pipeline price, ending in his smallest covering portfolio.

- V1, with the closed run alone in V2 → certify by default (his kill result).
- V1 alone → the certificate is an option.
- Capped runs are tabulated apart, and their wins count as search (Nocedal).
- No closed run at the chosen (k, γ) → capability gap, listed under Open questions.

Kill for my side: if no closed run beats its L0Learn warm start by more than one SE in any hold-out cell, running to proof buys nothing over L0Learn for prediction and selection, and the certificate stops being a default there.

**RISK — WHERE I COULD BE WRONG:** (1) The L0Learn warm start crosses parametrizations: L0Learn's Gamma multiplies the ridge term, while S095's γ divides it [S095 pp. 4–5]. A wrong map gives a feasible start for a different problem (inferred). (2) At the γ that validation chooses, S288's gaps may stay above 100% in every cell [S288 pp. 16–17]. FL2's inverse-covariance half would then yield only capability gaps, and the case would rest on the regression designs. (3) The stage concession leans on the critics' records [nikolaos-v-sahinidis note 05 §A8, row 8e]; BPV's rejoinder is unread here [05 §1.3] *(citation not confirmed as a gap: nikolaos-v-sahinidis note 05 §A8 rows 8d–8e record both rejoinders read; BPV's acknowledged SSS 'without addressing the timing point')*. (4) No statistic prices a proof that someone downstream needs, or a model that will be read or embedded, though his own record pays that price (nikolaos-v-sahinidis note 02 J5; C2). "Not a default" therefore covers prediction and selection only. (5) A work limit repeats a stop only on the same hardware and settings (Gurobi, checked), and calibrating per family adds runs.

**QUESTION FOR USER:** Will the selected model only predict and select, or will it be read, embedded in a later optimization, or required as a proved ℓ0 optimum? (This merges Sahinidis's and Nocedal's questions.)

#### Rejoinder

**[Sahinidis, challenger rejoinder lens]**

**POSITION:** Accept his other changes; my 2020 record priced an uncertified CIO [02 C2: no gap recorded]. Contest: critics' designs as hold-out; "closed" without a tolerance; V1's "FDR or test loss" (mine too).

**WHY (method refs):** (→ Method 4 step 4) S095 adopts HTT's PVE formula and SNR grid [dimitris-bertsimas card S095 pp. 10, 21]: seen. (→ Workflow D step 2) A win may not hide a loss.

**FIRST EXPERIMENT / DECIDING TEST:** The lead's, plus: a hold-out unused by S095, S288, HTT or my group; closed: ε = 10⁻⁴ [dimitris-bertsimas card S095 p. 5] (→ Integrity rule 5); V1: a one-SE win on one metric, no one-SE loss on the other.

**RISK — WHERE I COULD BE WRONG:** HTT's Σ and β may differ from S095's (on no file I read); 10⁻⁴ may rarely close.

> **Moderator summary.** **Agree:** v1 dropped ncvreg, whose MCP and SCAD S095 printed ahead in places, so Sahinidis's arms (a) join the test (glmnet 5.2 with relax, L0Learn 2.1.0, ncvreg 3.16.0, Glasso, MB and QUIC), beside an MIO warm-started from L0Learn (the lead); the price is not yet timed on equal tasks, so the item stops at knob and price, with whole tuned pipelines on one model-size grid, M and γ tuned on validation and work-limit stops; only a closed gap can show proof paying, so a capped win counts as search and S061's band is a capability gap; and the 2020 discussion priced an uncertified CIO, not proof time.
>
> **Split:** Sahinidis contests three details of the lead's reading, each with a fix: a critic's released designs cannot serve as the hold-out, since S095 adopted HTT's PVE formula and SNR grid (a hold-out unused by S095, S288, HTT or his group); "closed" needs a tolerance (ε = 10⁻⁴, S095's own stop); and V1's "FDR or test loss" lets a win hide a loss (a one-SE win on one metric with no one-SE loss on the other). Whether bounds or the big-M-free form come first is left to the runs, since both are arms.

### Item 3 · What may a stopped robust search on a simulator claim? · challenger Conn

#### Opening

**[Conn lens, challenger]**

**POSITION:** Partly outside my evidence: my robust record is one bilevel paper, hand-built tests, no baselines [S066 pp. 16–19]. Agreed: a found lower bound under a heuristic label for both arms; then S090's termination test cannot stay "an optimality condition" [dimitris-bertsimas card S090 p. 15]. Agreed on his tie point, from my minimax record: at ties the max kinks, and descent must lower every active piece at once [S233 pp. 1–2], as his SOCP step does (inferred). Challenged: (1) "An inner rule wins" on his own Examples I and III is a hand-picked verdict [S102 p. 7]: say "competitive" [S075 pp. 1, 22–23] unless a public tier agrees. (2) The inner-rule factor switches starts, accuracy and derivative source at once; in my record finite differences often beat interpolation models noise-free, yet lost under noise [S020 p. 9; S019 p. 18]. Switch one at a time [S040 pp. 32–33].

**WHY (method refs):** (→ Conn · M2; Workflow C checkpoint) A win on hand-picked problems earns no improvement claim. Smaller sets "are more likely to introduce unwanted bias" [S102 p. 7], and claims are worded tier by tier, as "competitive" or "complement each other" [S075 pp. 1, 22–23; S102 p. 17]. My side's paper has the same weakness, disclosed as a first contribution [S066 p. 19] *(citation not confirmed: 'a first contribution' is on p. 18 of the card; p. 19 has the no-baselines disclosure)*, so it backs neither inner rule. (→ M2 step 6; catalog E2) Make one change from a documented default at a time [S040 pp. 32–33]. (→ M5; H12) Modelling f may beat estimating derivatives [S009 p. 4], yet my own studies went both ways depending on the noise level [S020 p. 9; S019 pp. 17–18]. The plan's charge of n calls per gradient matches my record's own conversion [S019 p. 16]. (→ M5; catalog P20, A5) At ties the max is not C¹, and every active piece must fall at once [S233 pp. 1–2]. His σ bad-neighbour set works like my ε-near-active set [S233 pp. 3, 6; dimitris-bertsimas card S090 p. 7] (inferred). (→ M1 step 2; M3; catalog A1) The theory draw stands because no theorem covers either code as it is run [S066 p. 10; dimitris-bertsimas card S090 pp. 5–6]. It does not rest on a Lipschitz constant: the tied rule's constants need only exist, and the code fixes them at 10⁻² [S066 pp. 8–9, 14]. So the modulus a simulator lacks voids a bracket, not the rule. (→ Workflow F step 5; catalog W7) Keep proved and observed apart [S074 p. 3]: a numerical termination test is a stopping rule. (→ H1) On EM the adjoint gives gradients at no extra cost [dimitris-bertsimas card S090 pp. 2, 11].

**FIRST EXPERIMENT / DECIDING TEST:** FL4's deciding test, as argued, run as the lead's 2 × 2 with the delegates' additions, plus four changes.

(a) Split the inner rule into single switches [S040 pp. 32–33]. First switch: run the tied-tolerance solve from his structured ascent starts [dimitris-bertsimas card S090 p. 7] and pass every local maximizer it finds to the outer step (inferred design). Second switch: run the same solve on finite-difference gradients, charged n calls each [S019 p. 16]. If the first switch matches his ascents, his tie case is about starts, not ascent depth. If the second moves the ranking, the derivative source decided it.

(b) Run my side's arm as its printed cumulative ablation: basic, then + inexact lower level, then + reuse [S066 p. 16; captions pp. 21–24]. Add the analysed variant with model-improvement and criticality steps [S012 pp. 13–14], and count the calls spent on geometry, a measurement my line never made [S075 pp. 23–24] (→ M3 step 5).

(c) Add a public tier whose problem list, radii, budgets and constants are frozen before any run [S188 pp. 5, 7]. It holds robust counterparts of the 20 small CUTE problems (n = 2–4) from my first DFO study [S019 pp. 15–16], taken from CUTEst where they survive (SNAIL, HAIRY and CLIFF checked; the rest unverified) *(none needed: all 20 are in CUTEst (checked), so lift 'the rest unverified'; flag PFIT1LS as bound-constrained)*. Bracket a problem where its printed function yields a modulus; otherwise use the referee (inferred construction).

(d) EM, if obtainable: the adjoint search is the incumbent, not a reference line. For each withheld-gradient arm, print its extra calls at an equal refereed worst case: that is the price of going derivative-free (→ H1). Code failed simulations and count them in the budget (→ H13 [S020 p. 10]).

How it decides: an inner rule "wins" only where the public tier agrees with Examples I and III. Otherwise the verdict is "competitive" or "complement each other", tier by tier.

**RISK — WHERE I COULD BE WRONG:** This is a historical lens, and its robust evidence is a single paper whose plotted curves were not read, since they are not in the text file (S066 card). The tie agreement, and reading it as a question of starts, transfer a finite max of C² pieces [S233 p. 1] to a max over a ball (inferred). The derivative-source evidence comes from 1990s CUTE studies at n ≤ 16 against LANCELOT [S019; S020]. Without noise, my 1996 study found the two sources comparable [S019 pp. 16–17], so on Examples I and III the second switch in (a) may change nothing before Nocedal's noise stage. The public tier is my own construction: the choice of radius can favour one inner rule, and freezing it in advance limits that bias but does not remove it. The extra arms cost runs. If the budget binds, run the starts switch in (a) first, since it tests his held hypothesis, then (c).

**QUESTION FOR USER:** For the simulators you care about, can gradients be had (adjoints, automatic differentiation, sensitivities), and at how many simulation calls per gradient?

#### The lead's answer

**[Bertsimas (lead), answer to the challenger lens]**

**POSITION:** Conceded: (1) my termination test is a stopping rule, not an "optimality condition" [S090 p. 15]. (2) A missing modulus voids my bracket, not their rule, whose code fixes its constants at 10⁻² [andrew-conn card S066 preprint pp. 8–9, 14]; charge withdrawn. (3) Two hand-built examples cannot carry "wins": my review judged heuristics over families of instances [S005 pp. 3–4]. (4) One switch at a time. Held: at ties both records need a step that lowers every active worst case at once [S090 pp. 3–4; andrew-conn card S233 pp. 1–2], so my case is coverage of tied maximizers [S090 pp. 5–6]; his starts switch tests it. Changed: ledger; item 3's arms, incumbent, tiers, verdicts; switch rule 3; order.

**WHY (method refs):** (→ Method 7 stop rule; C3) The test was named an optimality condition after late discoveries were admitted [S090 pp. 12, 15], an over-claim on my record (HS §5). (→ Method 4 step 6; C8) My review's yardsticks, families of instances and equal-time duels reported by class [S005 pp. 3–4], bind my own arm; Conn's words fit them: "competitive", "preferable" for one tier each [andrew-conn card S075 preprint pp. 1, 22–23], "complement each other" [andrew-conn card S102 p. 17]. (→ Method 1, the class kept in the direction SOCP) By Danskin and KKT, d descends only if d′Δx* < 0 at every worst error [S090 pp. 3–4, 16–17]; by Proposition 2, bad neighbours whose conic hull contains them all suffice [S090 pp. 5–6]: coverage, not inner accuracy. S090's "depth" counts ascents, i.e. starts, and 3 + 1 lowered the cost fastest yet never terminated [S090 p. 15]: his starts switch tests what my record left open. His ε-near-active set [andrew-conn card S233 pp. 3, 6] and my σ set [S090 p. 7] work alike (inferred). (→ Method 4) Over 95% of the neighbours behind the EM estimate were reused [S090 p. 12], so my history set is ablated as he ablates reuse [andrew-conn card S066 preprint p. 16]. (→ Method 3) Derivative-freeness gets a price: extra calls at an equal scored worst case against the gradient incumbent, whose gradients come free on EM [S090 pp. 2, 11]; Γ, the knob, is swept on a frozen grid over the rival school's problems plus one realistic case [S001 pp. 12, 14]. (→ Method 5; Integrity Rule 5) Random sampling stays the practitioners' baseline [S090 p. 12], nominal cost beside; failed runs counted. Chair's rule: the best idea wins, whoever had it [02 O5].

**FIRST EXPERIMENT / DECIDING TEST:** FL4 deciding test, as argued, with v1's delegate additions and Conn's (a)–(d), plus four edits.

1. Ladders: his (b); mine from ascents without the history set, then with it, then 10 + 1 and 3 + 1 starts [S090 pp. 7, 15].
2. Step audit (inferred design), on v1's per-iterate scores: after each accepted outer step, did the scored worst case rise? If so, does the step fail Theorem 1's test against a worst error the scorer found [S090 pp. 3–4] (a missed tie), or not (a model or step-length failure)?
3. His tier (c), with Γ on a grid frozen with the list; its bracketed problems also calibrate Audet's referee.
4. The gradient search is the incumbent on every tier, a value-and-gradient call counted once [S090 pp. 2–3]; each withheld-gradient arm prints its extra calls at an equal scored worst case, replacing FL4's "reference line only".

Plan edits: the ledger adds "a termination test is a stopping rule"; switch rule 3 takes Audet's dissent wording, plus "tiers disagree → 'competitive', tier by tier" and "one switch moves the ranking → credit that component, not the inner rule"; part 5 adds Conn's gradient question; open question 11 becomes coverage against inner accuracy at ties; item 3 runs in his order, starts switch first, then (c).

How it decides: per tier, "preferable" only where brackets separate across instances and seeds (on referee-only tiers, a ranking only under Audet's calibration gate); "wins" only where every tier agrees; else "competitive" or "complement each other". My tie case holds if, where the scorer finds tied worst errors, the arms passing every maximizer (mine, his starts switch) show fewer missed-tie rises and lower scored worst cases at equal calls, whatever their inner accuracy; it falls where the single-start bilevel arm [andrew-conn card S066 preprint pp. 12–13] matches them on both. If his starts switch matches my ascents, the case is starts, and the cheaper inner rule stays. Stages unchanged: inner rule at measured tractability; simulator claims at the certificate stage.

**RISK — WHERE I COULD BE WRONG:** The audit sees only the worst errors its scorer finds, so it undercounts missed ties, though equally for arms that share the scorer. Theorem 1 is first-order: a finite step can raise the worst case for other reasons, so the audit attributes failures and decides nothing alone. The public tier is Conn's construction, its robust counterparts my inferred transfer: my record runs a rival school's instances only for the robust LP [S001 pp. 12, 14], never in DFO, and a Γ grid multiplies the runs. One call per value and gradient holds on EM by the adjoint [S090 pp. 2, 11] and is assumed elsewhere. EM rests on collaborators' code and privately communicated error data [S090 pp. 12, 18], so the price of going derivative-free may be measured only on printed functions. If his starts switch matches my ascents, what stays distinct in my rule is predictable inner time [S090 p. 6], which only the call counts can price.

**QUESTION FOR USER:** Do your simulators come with measured error statistics from which Γ can be set, as the EM design's 40 μm spread set its 550 μm radius [S090 p. 12]?

#### Rejoinder

**[Conn, challenger rejoinder lens]**

**POSITION:** Accepted: his concessions and changes. Contested: "coverage, not inner accuracy" is untested: no switch varies only accuracy among arms passing every maximizer; his audit files inner shortfalls under "model or step length".

**WHY (method refs):** (→ M3; P16) Inner value errors within η₀′ × predicted decrease keep an accepted step's true ratio ≥ η₀−2η₀′ [S066 pp. 5–6].

**FIRST EXPERIMENT / DECIDING TEST:** His, plus a rung running the swap arm's ascents to the tied tolerance [S066 p. 14], and an audit class, rises after Theorem-1-passing steps whose accepted worst value trailed the score by over η₀′ × predicted decrease. That rung winning at equal calls, or that class outnumbering missed ties: accuracy decides; else coverage stands.

**RISK — WHERE I COULD BE WRONG:** SOCP steps predict no decrease; there use the estimated drop (inferred).

> **Moderator summary.** **Agree:** The lead concedes four points to Conn: his termination test is a stopping rule, not an "optimality condition"; a missing modulus voids his bracket, not the bilevel rule, whose code fixes its constants at 10⁻² (charge withdrawn); two hand-built examples cannot carry "wins", so Conn's frozen public tier is added and verdicts are given tier by tier ("wins" only where every tier agrees, else "competitive" or "complement each other"); and switches change one thing at a time, the starts switch first. The gradient search becomes the incumbent, each withheld-gradient arm printing its extra calls at an equal scored worst case, and at ties both records need a step that lowers every active worst case at once.
>
> **Split:** What decides at tied worst errors: the lead holds that it is coverage of the tied maximizers, not inner accuracy, tested by Conn's starts switch and his own step audit; Conn calls that untested, since no switch varies only accuracy among arms passing every maximizer, and adds a rung running the swap arm's ascents to the tied tolerance plus an audit class for steps whose accepted worst value trailed the score. If that rung wins at equal calls, or that class outnumbers missed ties, accuracy decides; otherwise coverage stands.

### Item 4 · Where do heavier conic rungs stop paying? · challenger Dey

#### Opening

**[Dey lens, challenger]**

**POSITION:** Agreed on the stop: on my set, product rungs stop paying as n grows (→ Dey · Method 5). (1) The fix presumes structure-chosen products are cheaper than the LMI; on my one set (separable powers over the simplex, random objectives, n ≤ 10) the reverse held. The LMI lifted RLT from 924 to 941 exact for 6 s more; the products reached 959–960 at 121–129 s, and with them, the LMI added one instance [S129 p. 20] *(citation not confirmed: card c17 gives no time for PRS and does not say which RPT arm reached 960; arXiv v1 p. 20 states both: PRS 6 s longer than PR; PRV 959 at 121.177 s, PRSV 960 at 129.492 s)*. My higher-dimension verdict is the products costing more than BARON's solve at n = 10 as headroom shrinks with n [S129 pp. 17, 22–23]; it is silent at n ≥ 20 (→ Method 2). (2) Ledger (1) does not isolate the rung: RPT-BB reads incumbents and branching off each rung's solution [dimitris-bertsimas card S377 pp. 13–15], and a tighter relaxation can enlarge the tree [S081 pp. 2, 9]. Integer arms, BARON internals: outside my evidence.

**WHY (method refs):** Method 5 step 2 and variant: rank rungs by theorem where possible. The SDP adds nothing to the single-row relaxation P [S129 p. 5] yet strictly strengthens RLT [S129 p. 7], so the LMI's worth depends on the product set. Drop a rung only when a cheaper one matches it on gap against time [S129 pp. 20–21], and compare bounds at equal time or time to an equal bound, not rates (Workflow C step 6) [S100 p. 11]. Method 2 step 3, spatial-B&B variant: one incumbent is passed in "to isolate the evaluation of the dual bound improvement" [S123 p. 5]; no extrapolation past the instrument. Workflow C step 5: report root gap and tree size apart [S081 pp. 2, 9]. Method 1 step 4: a measure defined on every instance [S028 pp. 2–3]. Anti-patterns, last row: state a negative's scope. Heuristics 1–2: hard generators, common tolerances [S014 pp. 22–23, 35].

**FIRST EXPERIMENT / DECIDING TEST:** FL5's test and both ledgers, plus:

(a) Root ledger first (E6). Each product set (RLT, structure-chosen, all-pairs) with and without the LMI, and the LMI's minor-based outer approximation, against the certified value (else the best feasible value, flagged). Report cumulative gap, exact count at 10⁻⁴ and cumulative time, by n; drop dominated rungs [S129 pp. 20–21]; print the n where RLT+LMI and RLT+products cross in time. Price the minors rather than presume them cheap: at n ≤ 10 the cheaper full LMI dominated them [S129 p. 21].

(b) Instances the cheapest rung already solves exactly form their own band, counted by n [S081 pp. 11–12]. If the band with headroom thins at n ≥ 20, generate instances that cut off that rung's optimum, and release them [S014 pp. 22–23, 35].

(c) Ledger (1) with one incumbent for every arm, its source printed [S123 p. 5], plus the RLT arm's partitions replayed under each rung, since a weaker relaxation's tree certifies a tighter one [S081 pp. 1–2] (spatial transfer inferred). Report root gap and tree size apart.

(d) One gap, 10⁻⁴, for all solvers, as S708's duel did [dimitris-bertsimas card S708 p. 35], with defaults as a labelled second run: BARON's EpsR default is 10⁻⁶ and SCIP's limits/gap default is 0 (manuals, checked).

Decision: a heavier rung stays only where it is undominated in (a) on the headroom band and still ahead in (c); elsewhere the cheapest undominated rung is the default.

**RISK — WHERE I COULD BE WRONG:** My ground truth stops at n = 10 on one continuous set. At nx = 50 the lead's card shows the LMI as the costly part, 101 s against 2,100 s [dimitris-bertsimas card S415 p. 27], so the crossover may sit just past my data, and the dikes may be a class where the LMI pays [dimitris-bertsimas card S708 p. 41]. A fixed incumbent strips the primal help that RPT-BB's candidate points legitimately give [dimitris-bertsimas card S377 pp. 13–14]; ledger (2) keeps that help. Non-monotone trees are proved for MILP only [S081 pp. 2–8]. My own protocol named no BARON tolerance beyond default settings [S129 p. 19].

**QUESTION FOR USER:** Can the certified values at n ≥ 20 come from ground-truth runs longer than the arms' 3,600 s? My pooling study gave BARON 6 h against 1 h, with the reason stated [S014 p. 22].

#### The lead's answer

**[Bertsimas (lead), answer to the challenger lens]**

**POSITION:** Stop unchanged; fix changed. Conceded: (1) my fix presumed structure-chosen products cheaper than the LMI; on his set they cost more [santanu-s-dey card S129 pp. 20, 23] *(citation not confirmed: the card gives no PRS time; the order RLT+LMI cheaper than the products is in the paper text, arXiv v1 p. 20: PRS 6 s longer than PR, the RPT arms 121.177–129.492 s)*: now an arm. (2) RPT-BB reads incumbents and branching off each rung's solution [S377 pp. 13–15; S708 pp. 15–19]: ledger (1) mixes bound, incumbent and tree. Held: class sets headroom and cost order. On S415's family BARON 20.10.16 leaves optima unproved at nx = 20–100, and the LMI is the cost [S415 pp. 26–27]; on the dikes it pays [S708 p. 41]. The tree decides; the root drops nothing: tighter relaxations can enlarge trees (MILP) [santanu-s-dey card S081 pp. 2, 9]. v1 changes: fix, decision rule, ledger (1), settings, instances, backup rule 4.

**WHY (method refs):** (1) Method 1 stop rule: a new device is a class choice like any other, so its solve time is measured at the target scale. I presumed it instead (CP: stated jointly; this follows his co-authored papers). (2) Method 4 step 3 and Workflow C step 4: give every arm one incumbent [santanu-s-dey card S123 p. 5], and print time to the best solution apart from time to proof [S184 pp. 32, 34]. That separates a rung's primal help (native column) from its bound (fixed column). Held, by the scale test before trusting a small-n result [S102 p. 26]: neither his order at n ≤ 10 nor S415's at nx = 50 transfers. An LMI-based RPT bound closes box-constrained cubics at the root up to n = 40, while BARON 20.10.16 hits the hour from n = 20 [S689 pp. 17–19]. Its linear replacement gives "much worse bounds" [S689 p. 8], so outer approximations get priced, as he asks. Decision metric: proofs per second in the tree. Method 7 step 6 prints where a stronger relaxation's size becomes prohibitive, and his crossover n is that print. Strength is not speed (IO §6, Dey point, an agreement). Settings: one thread with the same tolerance and limit, as S708's duel ran [S708 p. 35].

**FIRST EXPERIMENT / DECIDING TEST:** FL5's test and both ledgers, as argued, with Dey's (a)–(d) adopted and four amendments.

(1) Gate (Heuristic 10, inferred transfer). The harness first reruns his separable-power set at n ≤ 10 against his ground truth. It must reproduce his order, RLT+LMI cheaper than the products [santanu-s-dey card S129 pp. 19–21] *(citation not confirmed: the card gives no PRS time; the order RLT+LMI cheaper than the products is in the paper text, arXiv v1 p. 20: PRS 6 s longer than PR, the RPT arms 121.177–129.492 s)*; otherwise no n ≥ 20 row counts.

(2) Instances:

- generated families at n = 10, 20, 50 and 100, S415's Table 4 sizes [S415 p. 27];
- the RPT families, the dikes, QPLIB and MINLPLib;
- his headroom band, by n;
- his generated hard instances, released but scored as development sets only;
- certified values from runs longer than the arms' limit, if the user allows (his question; CP §6.2's Dey test already asks for a long BARON or SCIP run).

(3) Ledger (1). Every arm runs, none dropped at the root, in two columns: native, and fixed incumbent with its source printed. His replayed RLT partitions run too. Root gap, tree size, time to best and time to proof are printed separately.

(4) Settings:

- each run's gap is recomputed from its logged bounds by one formula, and counts as proved at 10⁻⁴ under the proof rule as argued;
- one time limit, with its clock named, is set for every solver. BARON 26.9.10 defaults to MaxTime 500 s and to EpsR 10⁻⁶ relative to max(|L|,|U|); SCIP 10.1.0 defaults to limits/gap 0 relative to min(|primal|,|dual|) (manual and parameter list, checked);
- pure defaults run as a labelled second run.

Settles two things: the crossover n per class (Method 7 step 6), and how many instances a root-dominated rung proves more per second in either tree column. If that count is zero at every n and library, his root screen becomes the filter.

Decision: a heavier rung is the default only where it out-proves every cheaper arm per second in the tree ledger. That must hold on the headroom band and on two libraries, one of them QPLIB or MINLPLib (Sahinidis's condition, accepted). Elsewhere the default is the cheapest rung that no other arm beats in the tree ledger (his default clause, read there).

**RISK — WHERE I COULD BE WRONG:** (i) The deposit may not accept his set as written, since the y ≤ x^κ half of y = x^κ is nonconvex; the gate may then have to run in his own code (unverified). (ii) Replayed partitions certify only if each heavier arm's node relaxation lies inside RLT's on the same region. The codes multiply each branching inequality into the child's constraints [S624 pp. 7–9; S708 pp. 17–19], so containment must be checked per arm (inferred). (iii) My n ≥ 20 evidence is co-authored, with his share not identified [S377 p. 1]. It was run against BARON 20.10.16 [S415 pp. 26–27; S689 p. 17] and 21.1.13 [S708 p. 35], and is reported mostly as averages. S415's printed instances 3–6 do not reproduce [S415 pp. 26–27, 46], and the dike win rests on added bounds xᵢ ≤ 300 [S708 p. 41]. (iv) Running every rung through the tree at least doubles ledger (1). If the count comes out zero, that was the price of checking his screen.

**QUESTION FOR USER:** None beyond Dey's (ground-truth runs longer than the arms' 3,600 s at n ≥ 20), which this lens seconds (CP §6.2, Dey point).

#### Rejoinder

**[Dey, challenger rejoinder lens]**

**POSITION:** Accepted: amendments (1)–(4), class dependence. Contested: per-second rates can rank fewer proofs above more; the fixed column, isolating the bound, decides.

**WHY (method refs):** Workflow C step 6 [S100 p. 11]; Method 2, spatial variant [S123 p. 5]; Method 5 step 2; Method 1 step 4 [S028 pp. 2–3].

**FIRST EXPERIMENT / DECIDING TEST:** The lead's, refined: his rule as fixed-column dominance (proofs and gap left at the limit, time where all prove) [S129 p. 21; S123 p. 7]; my set at κ = 2, n ≥ 20, where RLT+LMI (DNN) is exact [S119 p. 13]: a cheap optimum, any bound above it failing; one gap formula, finite across sign changes (SCIP's is not; checked).

**RISK — WHERE I COULD BE WRONG:** Crossing frontiers leave no default; the fixed column discounts primal help; S119 is a preprint.

> **Moderator summary.** **Agree:** The stop stands (Dey: "on my set, product rungs stop paying as n grows") and the fix changes: on Dey's set structure-chosen products cost more than the LMI, so they become an arm, behind a gate that must first reproduce his n ≤ 10 order; because RPT-BB reads incumbents and branching off each rung's solution, ledger (1) runs native and fixed-incumbent columns with RLT's partitions replayed, printing root gap, tree size, time to best and time to proof apart; no rung is dropped at the root; one gap of 10⁻⁴ is recomputed from logged bounds for every solver, with pure defaults as a labelled second run; and where the LMI pays depends on the class.
>
> **Split:** The decision metric: the lead's proofs per second in the tree, or, for Dey, fixed-column dominance (proofs and gap left at the limit, time where all prove), since per-second rates can rank fewer proofs above more. Dey also asks for one gap formula finite across sign changes, and for his κ = 2 set at n ≥ 20, where RLT+LMI is exact, as an audit in which any bound above the cheap optimum fails; his risk line: crossing frontiers leave no default.

## Programme plan v2 (awaiting the user's approval at checkpoint 4)

The lead's revised plan supersedes [Draft plan v1](#draft-plan-v1-superseded-by-v2-kept-verbatim) after the [Challengers' round](#challengers-round), checked again by the moderator for neutrality; the second verification's annotations are added in italics, and under part 3 the fault-line deciding tests the plan cites are reproduced verbatim.

### Programme plan · The price of exactness

*Revision v2, after the challengers' round. Drafted by the Bertsimas lens (lead); v1 was checked by the moderator for neutrality (citation not confirmed: v2 also carries the moderator's v2 neutrality check). Recommendations without attribution are the lead's. Delegates' and challengers' unresolved objections are quoted verbatim in the item they concern.*

**Claim ledger** (the lead's proposal; → his Methods 2, 4, 7):
- "now tractable" needs the certified frontier. Huangfu: "moving the frontier or that ratio alone earns context-only" (unresolved, item 1). Sahinidis: "Moves on Example 1 and Diabetes read 'on S010's instances'."
- "N× faster" is a net ratio to the strongest earlier code on cells both certify (Huangfu's rule, applied in the lead's item 1 test, (vi)).
- "certified" is a valid bound at a stated limit. Sahinidis: "Claim 'global within tolerances', never more."
- "robust" is a bracket (printed function) or "worst-case cost ≥ ĝ, unrefuted by referee R at budget B" (simulator). The wording is Audet's, and he attaches a condition for EM: "EM claims stand as 'unrefuted at budget B' only if the referee recovers the bracket ranking".
- The lead to Conn: "my termination test is a stopping rule, not an 'optimality condition' [S090 p. 15]".
- Conn: "an inner rule 'wins' only where the public tier agrees with Examples I and III. Otherwise the verdict is 'competitive' or 'complement each other', tier by tier." *(citation not confirmed: Conn's own risk line adds "the choice of radius can favour one inner rule, and freezing it in advance limits that bias but does not remove it")*

None of these claims may rest on borrowed products, solver statuses or a search's own estimate.

#### 1. Recommendation (the lead's, by item)

**1 · IO, ML (LO) · stops at measured tractability (fix: time the class).** Huangfu agrees. Gould agrees but narrows it to one change per arm, which the lead accepts. Sahinidis (challenger) agrees, speaking to protocol: "measure a why-now by rerunning releases on one machine and one set, varying only the code".
- Problem: best-subset MIQO, one problem for every arm: (8) or provable M [S010 pp. 9–10, 15–17] (→ Method 1).
- Incumbent: the borrowed factor. Then-arms: S040's code rebuilt, as printed and best-bound (Gould's v1 dissent), and leaps 3.2 (CRAN, checked), run as exhaustive regsubsets (Sahinidis's (1), refined in the lead's (1′)).
- Solver runs: each runnable release of one MIO solver *(unverified)* at defaults, deterministic, one thread; one release at 1, 8 and 16 threads; 1% gap or 15 min per k [S010 pp. 31–32] *(assumed)*, inside one path budget (Sahinidis's (2)); boundary p rerun in isolation (his (5)).
- Instances: S010's designs, Diabetes, and frozen real designs (Gould), plus any hold-out the user freezes before any run (Sahinidis), each set reported apart (his (4)).
- Metric: the certified frontier (Gould's score), with the net ratio beside it (→ Method 2), at 1% and 10⁻⁶ (Sahinidis's (3)), audited by his (v′).
- Huangfu and Gould both mark their MIO transfers inferred.
- Sahinidis (challenger): "Statistics and MIQO lie outside my record, so each transfer here is inferred." On his 10⁻⁶: "10⁻⁶ comes from my global-MINLP protocol; on MIQO it may time numerical tails rather than search."
- *Accepted from Gould's rejoinder*: "The less-scalable verdict stands only if both 2009 arms miss; the why-now holds only where the frontier moved."
- *Accepted from Sahinidis's rejoinder*: (v′), and "The unscoped 'now tractable' stands only where certification also moves, at the gap the headline names, on a set fixed before any run by someone who tunes no arm".
- *Unresolved*: may a frontier move alone carry "now tractable"?
  - The lead: "credit an arm (release, threads, formulation, warm start) only if it moves that frontier"; otherwise "the abstract carries the frontier and the net factor measured there".
  - Huangfu (rejoinder): "moving the frontier or that ratio alone earns context-only."
  - His censoring point is accepted: net factors are measured only on cells both arms certify.

**2 · ML, IO · stops at "knob and price (fix: whole tuned pipelines, one model-size grid)", conceded to Sahinidis, then certificate or gap (fix: print every gap).**
- Problem: convex integer ℓ0 estimators [S095 p. 11; S288 pp. 16–17] *(citation not confirmed: S095: card c22 gives the convex integer reformulation at pp. 4–5; p. 11 carries Table 2's designs and timing relative to glmnet, not the reformulation; S288: card s12 gives the convex-in-Z reformulation at pp. 8–9; pp. 16–17 carry the synthetic p = 200 runs against MB and Glasso, Table 1, p. 17)* against glmnet, Glasso and QUIC (1.1.1, CRAN archive; current build *(unverified)*) (FL2's deciding test), plus Sahinidis's (a) and an L0Learn-started MIO (the lead).
- Settings: one MIO release *(unverified)*; stops at the warm start, 60 s, 5 min, 2% and 1 h, the timed ones as Sahinidis's (c) work limits, calibrated per family (the lead); "closed: ε = 10⁻⁴" (Sahinidis) *(citation not confirmed: Sahinidis's own risk line adds "10⁻⁴ may rarely close")*; M and γ grids from a priori scales, tuned on validation, each certificate naming its problem [S288 pp. 8, 11] (→ Method 4).
- Metric: out-of-sample error and FDR against time, whole tuned pipeline against whole tuned pipeline (Sahinidis's (b)).
- Accepted at the table: the stall twin and (c), by Nocedal and Wright; whole paths, by Wright; and, by Nocedal, that stop (2) uses the MIO's bound, "leaving only its tolerance open".
- Nocedal and Wright both place MIO outside their evidence.
- Sahinidis (challenger): "Partly outside my evidence (ℓ0 selection statistics)"; the 2020 discussion he brings is "in both teams' notes; on no card".
- Reading: the lead's (V1)–(V2), V1 as Sahinidis's "a one-SE win on one metric, no one-SE loss on the other"; from Nocedal's v1 dissent, accepted: "Those readings score a one-sample stop (2) (design inferred), tabulated against the oracle [S018 p. 20]". Hold-out: "unused by S095, S288, HTT or my group" (Sahinidis).
- *Unresolved, narrowed by the lead's (V1)*: does closing the gap ever buy statistics? Nocedal and Wright have had no turn on (V1) *(citation not confirmed: Nocedal's and Wright's v2 sign-offs now answer (V1), both as dissents)*.
  - Nocedal: "after the last incumbent change the estimate is fixed, so proof time buys a stopping decision and the word 'optimal', not out-of-sample error". Rejoinder: "where the capped run wins, search pays, not proof." His reading 3: "tighten the stop to the winning support's arrival gap; certify only at a closed gap."
  - Wright: S288's FDR gain "prices the exact ℓ0 model, not the exact solve". Rejoinder: "my quoted risk cuts against stop (2) too: a small gap, in objective units, can hide a wrong support (inferred). Certify a band only if every twin, longest stall window included, trails beyond one SE."
  - The lead (v1): "The capped run beats stop (2) by more than one SE in some band (Nocedal's kill result). Then certify in that band, with its proof time printed." His item 2 reply: "FL2's fixed designs may miss that band" [S061 p. 16]. His own risk line: "The band may be empty at SNR 1 or 0.05." To Sahinidis he conceded the band "is a capability gap" and adopted "count as search (Nocedal)" and "every twin (Wright's longest stall window included)".

**3 · RO, HS (AP testbed) · two stops.** The inner rule stops at measured tractability (Vicente's framing, adopted by the lead). Simulator claims stop at the certificate stage; the fix is a heuristic label and a refereed lower bound, in Audet's wording, accepted by Vicente and Nocedal. Conn (challenger) agrees: "a found lower bound under a heuristic label for both arms". He adds: "Partly outside my evidence: my robust record is one bilevel paper, hand-built tests, no baselines [S066 pp. 16–19]."
- Problem: min–max over an ℓ2 ball, gradients withheld: Example I (Γ = 0.5 [S090 p. 8]), Example III (one joint 18-D ball of radius 0.5; paper text, p. 14), Vicente's summed-block rung, Conn's frozen tier (c) (its CUTEst problems: "SNAIL, HAIRY and CLIFF checked; the rest unverified") *(none needed: all 20 are in CUTEst (checked), so lift 'the rest unverified'; flag PFIT1LS as bound-constrained)*, and EM if obtainable *(unverified)* (Audet's question), at Γ = 550 μm [S090 p. 12].
- Incumbent: the gradient search (Conn's (d), on EM; the lead extends it to every tier), "replacing FL4's 'reference line only'". Random sampling [S090 p. 12] is kept as the practitioners' baseline. Vicente: "beating it is a low bar".
- Arms: outer step × inner rule. The 2 × 2 is the lead's, accepted by Vicente, Audet and Nocedal; the arms are rebuilt from print in one code base (Audet), and every call is counted. Single switches (Conn's (a)), both ladders, Conn's accuracy rung.
- Bounds: a mesh bracket for Example I and an angle mesh for Example III (Vicente's and Nocedal's fix) [inferred]. The lead concedes in this plan that his Δx bracket fails at the rim; his answer to Conn: "A missing modulus voids my bracket, not their rule" *(citation not confirmed: no lead turn concedes the rim; the quoted answer to Conn withdraws the Lipschitz charge against the bilevel rule, so the link is inferred)*.
- Metric: the bracketed or refereed worst case against calls, with the nominal cost beside it (→ Methods 3, 7; HS thin).
- The 96% figure is withdrawn as evidence on the inner rule.
- *Unresolved: FL4's inner rule.*
  - The lead: "Where worst errors tie [S090 pp. 3–4; inferred], the case for several ascents over one inner solve still stands, though untested." To Conn: "my case is coverage of tied maximizers [S090 pp. 5–6]; his starts switch tests it."
  - Vicente: tying inner accuracy to outer progress "is this lens's default, untested here"; "Where several worst errors compete, searching more widely may beat it."
  - Nocedal: "Inner rule: neither by default; the call-counted test decides."
  - Conn (rejoinder): "'coverage, not inner accuracy' is untested: no switch varies only accuracy among arms passing every maximizer; his audit files inner shortfalls under 'model or step length'." His rung and audit class are adopted (switch rule 3). His risk line: "SOCP steps predict no decrease; there use the estimated drop (inferred)."
- *Contested by Audet (rejoinder)*: "any EM verdict resting on my referee alone; no card tests it on a robust inner max." His calibration gate is accepted (see the claim ledger). His risk line: "Two printed polynomials may pass a referee that the 100-variable simulator defeats."
- *Caveats on the fixes*:
  - Vicente: "Both fixes are inferences; the rung's radius split needs bracketing too."
  - Nocedal: "My rim objection is on no card; two separate balls void it."

**4 · CP (stated jointly; this follows his co-authored papers), IO · stops at measured tractability.** Sahinidis agrees. Burer keeps the stop rule but would "separate the LMI from its solver". Dey (challenger) agrees on the stop: "Integer arms, BARON internals: outside my evidence." *(citation not confirmed: these are Dey's evidence-boundary words; his agreement reads "on my set, product rungs stop paying as n grows", silent at n ≥ 20)* The lead: "Stop unchanged; fix changed": structure-chosen products are "now an arm", and "The tree decides; the root drops nothing".
- Problems: nonconvex QCQP and polynomial problems, with or without integers, n ≥ 20: RPT families, dikes (xᵢ ≤ 300 for all [S708 p. 41]) *(unverified)*, QPLIB, MINLPLib. Sahinidis also names "qcqp2, the 2011 study's own QCQPs, to re-price SDP". Dey's sets (the lead's amendment (2)), and his κ = 2 set: "a cheap optimum, any bound above it failing".
- Two ledgers, accepted by Sahinidis and Burer: (1) rungs in one code; (2) engines. Dey's (a)–(d) run as amended: the gate and the native and fixed-incumbent columns in ledger (1); his (d), one gap of 10⁻⁴ for every solver with defaults as a labelled second run *(unverified: what BARON's defaults are depends on the interface (native, GAMS, Pyomo or JuMP), which is not yet named)*, in both ledgers.
- Incumbents: BARON 26.9.10 (release notes: 2026.9.10) and SCIP 10.1.0 at defaults (checked) *(citation not confirmed: Dey's (d), accepted, makes pure defaults the labelled second run)*, if a BARON licence is available (Sahinidis's question), beside BARON 20.10.16 and 21.1.13 where they still run *(unverified)*.
- Rungs:
  - RLT, structure-chosen products, all-pairs RPT.
  - The LMI three ways: by MOSEK *(unverified)*; by splitting (Burer; subject to his question to the user); or outer-approximated and admitted per node (Sahinidis).
  - One code, the IJOC deposit (`use_lmi`, checked). It is patched so that non-OPTIMAL children keep their parent's bound and stay open, each logged as a failure (Sahinidis, Burer).
  - Integer arms rebuilt with an all-open-node stop test *(assumed, pending the lead's question)*.
  - BARON with structure-chosen products declared relaxation-only, on and off (Sahinidis).
- Settings:
  - Gap 10⁻⁴; 3,600 s [S624 p. 10] *(assumed)*; one thread per solver, MOSEK included (Sahinidis).
  - Incumbents rechecked for feasibility [S708 p. 35]. Bounds that contradict another arm's rechecked incumbent, or the library's bound, fail the run (Sahinidis).
  - Only provably valid bounds prune or enter the open-node minimum (Burer; the lead's Method 4 step 4).
  - Burer: "Integer arms: outside my evidence."
  - Accepted from Burer's v1 dissent: "Every ledger-(1) arm also reports proofs at one looser common gap (e.g., 10⁻³, a decade looser, like the two levels in [S014 preprint pp. 15–16]; catalog E6), node-solve accuracy matched to each gap (H7); 'the LMI itself does' holds only where splitting loses at both."
- Metric: fixed-column dominance, accepted from Dey's rejoinder ("per-second rates can rank fewer proofs above more; the fixed column, isolating the bound, decides"): "proofs and gap left at the limit, time where all prove"; native-only wins credit primal help; per library and per ledger (→ Method 7 step 6).
- *Unresolved: where the LMI pays.*
  - The lead: "The LMI pays on some classes, not yet at scale."
  - Sahinidis: "Verdict: class-dependent", and "plan a portfolio with per-node switching". His device: "emulate the LMI with cheaper cuts, as BARON's 'SDP-quality' quadratic cuts do for MIQPs".
  - Burer: "If (2) still loses per second, the LMI itself does."
- *From delegates' risk lines, not in the draft's settings*:
  - Sahinidis: "One thread may handicap interior point; add a labelled multithread run."
  - Burer: "At 10⁻⁴, splitting's slow tail [S014 preprint pp. 2, 17] may lose for solver reasons; report a looser gap." *(citation not confirmed: S014 is a projected-gradient code, not a splitting method; its card supports p. 2 (slow limiting convergence of first-order methods) and p. 20 (their moderate-accuracy niche), not p. 17; the transfer to splitting is inferred)* *(citation not confirmed for splitting: S014 is a first-order projected-gradient code; its card shows the slow tail at pp. 2 and 17, where iterations grow 'drastically' from 0.2% to 0.02%; the transfer to splitting is inferred)* Since v2, in the settings: accepted from his v1 dissent.
  - Sahinidis: "MINLPLib and the QCQP sets are BARON development libraries [03 §A2], so the duel tilts toward BARON, his product; the one-engine ablation does not."
- *From the challenger's risk line*: Dey: "Crossing frontiers leave no default; the fixed column discounts primal help; S119 is a preprint."
- Burer withdraws his opening rule (1): "no rung dropped on root evidence".

#### 2. Backup and switch rules (the lead's)
- 1: Old releases cannot be licensed → run the newest release against every then-arm, with the factors labelled borrowed. The rebuild, as printed or best-bound (Gould's v1 dissent), fails its gate (Gould's node-count reproduction, Huangfu's proved cells) → "less scalable" stays unmeasured *(citation not confirmed: Gould's node-count gate binds the printed rebuild; his v2 sign-off holds only if it binds that rebuild alone)*. A bound breaches (v′) → "That arm is rerun on formulation (8) or on provable bounds".
- 2: Gaps above 100% on most draws → Sahinidis's switch rule, "with its order (bounds, then reformulation) left to the runs, since both are arms" (→ Method 4 stop rule): "If gaps are still open at p ≤ 200, record a capability gap: there is no certificate there to price." The stall twin ties → no default certificate.
- 3: An ascent beats a closed-form upper bound → the scorer is void (Nocedal). Accepted from Audet's v1 dissent: "failed referee calibration, or calibration on a voided bracket → EM reports found lower bounds only, no 'unrefuted at budget B', no inner-rule ranking". The lead, after Conn: "tiers disagree → 'competitive', tier by tier"; "one switch moves the ranking → credit that component, not the inner rule". Conn (rejoinder): "That rung winning at equal calls, or that class outnumbering missed ties: accuracy decides; else coverage stands."
- 4: Roots unfinished at n ≥ 20 → admit the LMI per node. Splitting closes the gap → the cost was MOSEK's (Burer's arm). The gate fails → no n ≥ 20 row counts. A heavier rung stays a default only where it dominates every cheaper arm in the fixed column, on the headroom band and two libraries, one QPLIB or MINLPLib (Sahinidis's v1 dissent) *(citation not confirmed: Sahinidis's v1 condition adds "outside the RPT papers' own test families"; his v2 sign-off holds only if RPT-run instances count as development)*. Dey's risk line: "Crossing frontiers leave no default".

#### 3. Minimal experiment
Each item's deciding tests are its fault-line test (FL1, FL2, FL4, FL5), as argued, and every later DECIDING TEST field of that item, verbatim from the discussion, the challengers' round included.

The lead accepts every rejoinder addition except Huangfu's context-only rule, which stays unresolved (item 1) *(citation not confirmed: (V1) leaves out the first clause of Nocedal's reading 3, as the moderator's v2 note records)*. Net factors are measured only on cells both arms certify. A challenger's refinement of the lead's answer governs.

The lead's protocol:
- The user runs all arms on one machine, with releases and threads stated.
- Order: items 3, 2, 1, 4, by the licences each needs; item 3's starts switch first (Conn).
- Equal budgets: one budget per k-path, whole tuned pipelines, calls, one limit.
- Performance profiles; losing instances named; Mittelmann's third-party numbers beside item 4, with releases, threads and limits.

<details>
<summary>The fault-line deciding tests the plan cites (FL1, FL2, FL4, FL5), verbatim from the council roundtable, Step 3</summary>

**FL1 · deciding test:** on the best-subset paper's synthetic designs and Diabetes data [dimitris-bertsimas card S010 pp. 26–27], solve one MIQO formulation to a stated gap (a) with every solver release still runnable, named with its year, on one machine and one thread, and set the measured factor beside Bixby's MILP factor for the same releases (does "similar" hold?); (b) with one release at 1, 8 and 16 threads on an older and a current CPU, and set the realized hardware factor beside the Top500 peak ratio for the same years and the two CPUs' own peak-flops and memory-bandwidth ratios; several seeds, deterministic parallel mode, geometric means, losing instances printed; Huangfu's per-component profile (node relaxations, heuristics, cuts) places the ceiling (inferred translation).

**FL2 · deciding test:** on the inverse-covariance designs at p ≤ 200 and the sparse-regression paper's smallest design, (p, k) = (2,000, 10), at SNR 6, 1 and 0.05 [dimitris-bertsimas card S095 p. 11], stop the warm-started MIO at its warm start, 60 s, 5 min, a 2% relative gap (the stopping rule of Curtis's co-authored runs [frank-e-curtis card S034 pp. 36–37]) and a 1 h cap, printing the gap each time (flagged uninformative above 100%), with M or γ set from the a priori norm-bound scales, never from the truth [dimitris-bertsimas card S288 p. 11]; run the papers' own ℓ1 opponents (glmnet, Glasso) and QUIC *(unverified)* at tolerances 10⁻², 10⁻⁴ and 10⁻⁶ [jorge-nocedal card S043 p. 7] *(citation not confirmed: card S043 p. 7 shows one aligned stop at 10⁻⁶; the 10⁻² and 10⁻⁴ levels are the test's design)*; ten draws per point [dimitris-bertsimas card S095 pp. 13–20]; plot out-of-sample likelihood or prediction error and FDR against time and against the MIO's gap. Certification pays where the statistics improve beyond the standard error between the 60 s or 5 min incumbent and the certified or capped run; the trade-off view holds where the warm start already matches that run and loose ℓ1 tolerances match tight ones.

**FL4 · deciding test:** on his Example I (two-dimensional polynomial, ℓ2 ball of radius 0.5, starts A and B) [dimitris-bertsimas card S090 p. 8], both methods reimplemented from the printed algorithms [dimitris-bertsimas card S090 pp. 6–8], [andrew-conn card S066 preprint pp. 10–14] (no release of the bilevel code is stated [luis-nunes-vicente card S047 preprint pp. 14, 19]), with gradients withheld from both, each finite-difference gradient charged n calls and every call at both levels counted; the exact-gradient robust local search is a reference line only. Score each iterate's worst case, enumerated on a fine mesh as his annealing paper checked its optimum [dimitris-bertsimas card S141 p. 7], against calls; report the calls needed to come within a stated tolerance of the robust local minimum each run ends in, beside the enumerated global robust optimum, and how often a fresh dense search finds a worse error than the one each method accepted.

**FL5 · deciding test:** Dey's protocol (cumulative gap, cumulative time, exact count, and a gap-against-time plot that prunes dominated rungs) [santanu-s-dey card S129 pp. 20–21] on the RPT papers' families at n ≥ 20, regenerated from their printed descriptions, and on QPLIB's continuous QPs and QCQPs plus MINLPLib's integer instances of those classes where they exist; arms: RLT products only, RLT plus the simplex-type equalities times the convex terms, and all-pairs RPT, each with and without the LMI, plus a cheaper outer approximation in place of the LMI (Sahinidis's Method 5); current BARON and SCIP releases at defaults, one thread, one limit; an instance counts as exact only where some solver certifies its optimum, otherwise report the gap to the best feasible value found; count numerical failures (UNKNOWN statuses, stalls, runs with no solution).

Source: [council roundtable, Step 3](council-roundtable/SKILL.md#step-3--cross-examination-member-agents-13-rounds). The later DECIDING TEST fields of each item are in the [Discussion](#discussion).

</details>

#### 4. Reformulation ideas (the lead's)
- Cuts reused across k [S288 p. 11].
- Dual-norm worst cases for linear blocks [S019 pp. 3–4]: an inferred transfer. Nocedal accepts the reduction; he and Vicente contest its Example III bracket at the rim.
- Structure-chosen products [S415 p. 30; S708 p. 42] *(citation not confirmed in full: S415: card c2-08 gives partial constraint multiplications and partial generation of product variables as future work, p. 30, but no choice by structure; S708: card s2-18 gives partial multiplications, selective products and iterative constraint generation as future work, p. 42, but no choice by structure)*. The lead's opening notes that Dey's rung of this kind is "not advisable" in higher dimensions [santanu-s-dey card S129 pp. 18, 23]. The lead now concedes to Dey: "my fix presumed structure-chosen products cheaper than the LMI; on his set they cost more [santanu-s-dey card S129 pp. 20, 23]: now an arm." *(citation not confirmed: the card gives no PRS time; the order RLT+LMI cheaper than the products is in the paper text, arXiv v1 p. 20: PRS 6 s longer than PR, the RPT arms 121.177–129.492 s)*
- Sahinidis's alternative, cheaper cuts that emulate the LMI, carries his caveat: "The cheap emulation is shown only for MIQPs with linear equality constraints (arXiv:2106.13721, checked)."

#### 5. What the user decided
Nothing yet (autopilot). The lead's assumptions until the user answers: design only, with the papers' own limits.

Decisions for the user, with who asked:
- Run the arms, or design only (the lead).
- Item 1: which solver releases (Huangfu, Gould), and the gap a "now tractable" headline names (the lead); hold-outs (Sahinidis).
- Item 2: the model's use: predict and select, or read, embedded or proved (Nocedal, Sahinidis); a hold-out (Sahinidis) *(citation not confirmed: Sahinidis asked this on item 1 only; on item 2 he set a rule, not a question)*.
- Item 3: printed polynomials or a true simulator (the lead), access to EM (Audet), simulator noise (Nocedal), gradients (Conn), Γ from measured errors (the lead).
- Item 4: a licensed current BARON, since the free build handles only 10 variables and constraints (Sahinidis); an SDPNAL+ arm (Burer); the integer sequel's code requested from the authors or rebuilt (the lead); the dike data (first verifier); longer ground truth (Dey); CPLEX and exact MIP engines (the lead's proposal).

#### 6. Open questions
Listed with this draft.

1. Run or design: should the plan budget actual runs of these deciding tests on your machine and solver licences, or only design them? This is the Problem Card's question; the plan assumes design only.
2. Item 1: which MIO solver releases, oldest to newest, can you license and run on one machine (Huangfu, Gould)? Old releases may not install, or may no longer be licensable.
3. Item 1: "Which gap should a 'now tractable' headline name: S010's 1% within 15 minutes per k, 10⁻⁶, or one you set?" (lead).
4. Item 1 (unresolved): may a move of the certified frontier alone carry 'now tractable' (lead), or is it 'context-only' without the net ratio (Huangfu)?
5. Item 1: S040 states no machine and no seeds, and describes its random designs only loosely [S040 pp. 10, 22] *(citation not confirmed in full: card c12 records no stated machine and 'random X and β' (p. 10), not the missing seeds; the paper text never mentions seeds)*. The rebuild's reproduction gate can therefore only match distributions, and a rebuilt 2009 code is not the original (Huangfu, Gould).
6. Item 2: "Will the selected model only predict and select, or will it be read, embedded in a later optimization, or required as a proved ℓ0 optimum?" (Nocedal, Sahinidis; merged by the lead). "'Not a default' therefore covers prediction and selection only."
7. Item 2: "S061's band becomes a capability gap, mapped by my n-sweep (b)" (lead; Sahinidis: "a capability gap, not a band to certify"). Does the band, 'statistically relevant but computationally not feasible' [S061 p. 16], reach SNR 1 or 0.05? S061 tested only √SNR ≥ 3 and took best-found solutions at its time limit [S061 pp. 14, 16]. If no run closes there, the certificate keeps only its role in the theory, where the statistics of stopped solutions are still open [S010 p. 58].
8. Item 3: is a claim bracketed on the papers' printed polynomials enough, or must it hold on a true simulator, where only refereed lower bounds exist (lead)?
9. Item 3: can you obtain the 100-variable electromagnetic simulator and its error data (Audet)? The card shows collaborators' code and privately communicated error data, with no release stated [S090 pp. 12, 18].
10. Item 3: are your simulators exact to roundoff, or noisy because of iterative or adaptive solves (Nocedal)? Exact simulators drop his noise stage.
11. Item 3 (unresolved): "coverage against inner accuracy at ties" (lead), tested by the starts switch and by Conn's rung and audit class. No card runs this comparison, and search depth is unsettled even within the lead's method [S090 p. 15]. A referee validated on two printed polynomials may still fail on the 100-variable simulator (Audet's risk).
12. Item 4: can you run a licensed current BARON? Its free build handles at most 10 variables and constraints (minlp.com, checked), below this item's n ≥ 20 (Sahinidis).
13. Item 4: should the test add a first-order LMI arm that needs a separate released SDP code (e.g. SDPNAL+, which runs in MATLAB), or keep the RPT papers' MOSEK stack only (Burer)?
14. Item 4: should the plan ask the authors for the integer sequel's code (none was found) *(unverified)*, or rebuild it from the printed algorithm with a stop test over all open nodes (lead)? The dike data too (first verifier).
15. Item 4: the deposit uses different α and β values from the printed ones, which the card reader found infeasible [S415 pp. 26–27, 46], so for those instances the deposit, not the print, is the definition. What changed inside BARON after 2021 is one of this lens's blind spots, so this lens offers no causal reading of any gap in the engine ledger.
16. Process: answered by the challengers' round (Sahinidis on items 1–2, Conn on item 3, Dey on item 4).
17. Scope: SD and DA were not on the agenda, and AP entered only as item 3's testbed. With no decision owner (assumed), each item is scored on its own metric, not against an owner's current rule.
18. Resolved in the plan's own text: one BARON label, BARON 26.9.10 (release notes: 2026.9.10). Sahinidis's item 4 deciding test, included verbatim, still reads 'BARON 2026.9.10'.
19. Items 1–2: "Will you pick and freeze the hold-out designs yourself, before any run?" (Sahinidis) *(citation not confirmed: Sahinidis asked this on item 1 only; on item 2 he set a rule, not a question)*.
20. Item 3: "For the simulators you care about, can gradients be had (adjoints, automatic differentiation, sensitivities), and at how many simulation calls per gradient?" (Conn).
21. Item 3: "Do your simulators come with measured error statistics from which Γ can be set, as the EM design's 40 μm spread set its 550 μm radius [S090 p. 12]?" (lead).
22. Item 4: "Can the certified values at n ≥ 20 come from ground-truth runs longer than the arms' 3,600 s? My pooling study gave BARON 6 h against 1 h, with the reason stated [S014 p. 22]." (Dey, citing his own card S014; seconded by the lead).
23. Item 4 (the lead's proposal; not argued): CPLEX *(release unverified)* and exact MIP reformulations in ledger (2), winners on some instances [S377 p. 29; S708 pp. 37, 40]?

**Moderator's neutrality note.** Struck because they were not argued at the table (the lead may restore them at sign-off; the user decides at checkpoint 4):
- item 2's "L0Learn 2.1.0 and relaxed-Lasso regression arms (ML §6.1, point 1; CRAN, checked)";
- the reformulation idea "Box certificates when bounds stall [S010 pp. 34–36]".

The footnote's L0Learn (L0L2 penalty) and glmnet relax-option checks are struck with them.

**v2 (the lead).** Both arms return as Sahinidis's (a), argued and accepted.

**Moderator's neutrality note (v2).** *(citation not confirmed: not in the changes list, nor is the Kept paragraph below)* Changed, each from the record:
- Item 2: "Resolved in (V1)" *(citation not confirmed: the words are in no turn or sign-off; they come from the lead's pre-check draft, not reproduced)* is back to unresolved, now narrowed by (V1). Nocedal and Wright have had no turn on (V1) *(citation not confirmed: Nocedal's and Wright's v2 sign-offs now answer (V1), both as dissents)*, and (V1) leaves out the first clause of Nocedal's reading 3 ("tighten the stop to the winning support's arrival gap"). Wright's sign-off holds only "while that contest stays open".
- Credit and labels:
  - the leaps arm is Sahinidis's (1), refined in the lead's (1′);
  - the hold-out is whatever the user freezes before any run, since the record says one may not exist;
  - the gradient incumbent is Conn's (d) on EM, extended to every tier by the lead;
  - switch rule 3 keeps the lead's words apart from Conn's;
  - "Crossing frontiers leave no default" is marked as Dey's risk line;
  - Dey's (d) covers every solver, not ledger (1) alone.
- Restored from the turns:
  - the challengers' own evidence boundaries, beside their agreement;
  - Sahinidis's 10⁻⁶ caveat;
  - Conn's "unverified" mark on tier (c) and his risk line on the adopted audit class;
  - Dey's full risk line, including "S119 is a preprint";
  - the lead's concession to Dey, under structure-chosen products;
  - Dey's evidence in question 22.
- Small fixes: Burer's risk line is marked as now in the settings. Question 18 and the footnote's relaxation-only source are attributed as the record has them.

Kept: every v1 line the lead did not change is word for word, annotations included. All five v1 dissents were accepted, and each is carried out in the plan text. Two sign-off citations now in the plan text were not covered by the first verifier: Burer's (card c01) and the lead's in question 23 (cards s2-17 and s2-18). Both match their cards (checked here). v1's sign-offs were given on v1, and no delegate has yet seen the changes in v2 *(citation not confirmed: outdated, like the line on (V1): every seated lens has since signed or dissented on v2)*.

*Checked 2026-10-31 by the lead: leaps 3.2 and glmnet 5.2, on CRAN; BARON 26.9.10 and its 10-variable free build (minlp.com); SCIP 10.1.0 (scipopt.org); github.com/INFORMSJoC/2023.0345 (Julia, `use_lmi`); BARON relaxation-only constraints (BARON user manual, minlp.com, §4.1 and §10.2, the source the first verifier confirmed); SDPNAL+ (MATLAB; arXiv:1710.10604). Rechecked for v2: CRAN, Gurobi, BARON and SCIP documentation.*

### Changes from v1

1. Header note: marked as revision v2 after the challengers' round; challengers' unresolved objections are quoted like the delegates'. Source: Challengers' round (items 1-4).
2. Claim ledger, 'now tractable': adds Sahinidis's scope rule, quoted ('Moves on Example 1 and Diabetes read on S010's instances'). Source: Sahinidis, item 1 rejoinder (Settles).
3. Claim ledger, 'N× faster': 'accepted by the lead' and its citation-not-confirmed annotation replaced by 'applied in the lead's item 1 test, (vi)'. Source: First verifier, problem 4; the lead's item 1 answer to Sahinidis, (vi).
4. Claim ledger, 'certified': adds Sahinidis's 'Claim global within tolerances, never more'. Source: Sahinidis, item 1 challenger turn.
5. Claim ledger: new line, the lead's concession that his termination test is a stopping rule, not an optimality condition [S090 p. 15]. Source: Conn, item 3 turn; the lead's answer, concession (1).
6. Claim ledger: new line, Conn's rule that an inner rule 'wins' only where the public tier agrees, else 'competitive' or 'complement each other', tier by tier. Source: Conn, item 3 turn; the lead's answer.
7. Item 1 header: Sahinidis (challenger) agrees, speaking to protocol, with his words quoted (the quote replaced a bare 'agrees' at the moderator's check). Source: Sahinidis, item 1 challenger turn (POSITION).
8. Item 1 then-arms: S040 rebuilt as printed and with best-bound node selection; leaps 3.2 run as exhaustive regsubsets, never leaps() at its default, credited to Sahinidis's (1) as refined in the lead's (1′) (credit to (1) restored at the moderator's check). Source: Gould's v1 dissent; Sahinidis's (1); the lead's (1′) and (vii).
9. Item 1 solver runs: one total budget for the k-path; the last passing and first failing p rerun in isolation. Source: Sahinidis's (2) and (5).
10. Item 1 instances: any hold-out the user freezes before any run added, each set reported apart (worded at the moderator's check so as not to presume that a hold-out exists). Source: Sahinidis's (4), his hold-out rule (Workflow D) and rejoinder; the lead's settle rule and risk line ('The hold-out may not exist').
11. Item 1 metric: frontier printed at 1% and at 10⁻⁶ and audited by the refit check (v′). Source: Sahinidis's (3) and rejoinder (v′); the lead's (v).
12. Item 1: Sahinidis's evidence boundary and his own caveat on 10⁻⁶ quoted beside Huangfu's and Gould's (moderator's check). Source: Sahinidis, item 1 challenger turn (RISK).
13. Item 1: new line 'Accepted from Sahinidis's rejoinder': (v′) and the unscoped-claim rule, quoted. Source: Sahinidis, item 1 rejoinder.
14. Item 2 header: the stage moves to knob and price (whole tuned pipelines, one model-size grid), then certificate or gap. Source: Sahinidis, item 2; the lead's concession.
15. Item 2 problem: QUIC build named (1.1.1 in the CRAN archive; current build unverified); Sahinidis's arms (a) and an L0Learn-started MIO added. Source: First verifier, problem 1; Sahinidis's (a); the lead's item 2 answer.
16. Item 2 settings: timed stops become work limits calibrated per family; 'closed' means ε = 10⁻⁴; M and γ grids start at a priori scales and are tuned on validation. Source: Sahinidis's (c) and rejoinder; the lead's item 2 answer.
17. Item 2 metric: whole tuned pipelines timed against each other. Source: Sahinidis's (b).
18. Item 2: Sahinidis's evidence boundary quoted beside Nocedal's and Wright's, with his label for the 2020 discussion ('in both teams' notes; on no card') (moderator's check). Source: Sahinidis, item 2 challenger turn (POSITION).
19. Item 2: new Reading line: the lead's (V1)-(V2), V1 with the one-metric rule, a one-sample stop (2) tabulated against the oracle, and a hold-out unused by S095, S288, HTT or Sahinidis's group. Source: The lead's item 2 answer; Sahinidis's item 2 rejoinder; Nocedal's v1 dissent.
20. Item 2: the split stays 'Unresolved', now narrowed by the lead's (V1), because Nocedal and Wright have had no turn on (V1) *(citation not confirmed: Nocedal's and Wright's v2 sign-offs now answer (V1), both as dissents)*; the lead's 'Resolved in (V1)' *(citation not confirmed: the words are in no turn or sign-off; they come from the lead's pre-check draft, not reproduced)* was reverted at the moderator's check. In the lead's line, 'perhaps in S061's band' and its annotation are replaced by the reply's own words; the concession (capability gap) and the adopted Nocedal and Wright conditions are quoted. Source: First verifier, problem 4; the lead's item 2 answer to Sahinidis; Wright's v1 sign-off condition.
21. Item 3 header: Conn agrees on the lower-bound claim (quoted); his evidence boundary quoted (moderator's check). Source: Conn, item 3 turn (POSITION).
22. Item 3 problem: Γ = 0.5 cited per example (Example III's joint 18-D ball from the paper text, p. 14); EM at Γ = 550 μm [S090 p. 12]; Conn's frozen tier (c) added, with his own mark 'SNAIL, HAIRY and CLIFF checked; the rest unverified' (mark carried at the moderator's check); the annotation is resolved. Source: First verifier, problem 10; Conn's (c); the lead's edit 3.
23. Item 3 incumbent: the gradient search, Conn's (d) on EM, which the lead's edit 4 extends to every tier, replacing FL4's reference line (attribution split at the moderator's check); random sampling kept as the baseline. Source: Conn's (d); the lead's edit 4.
24. Item 3 arms: single switches, both ladders and Conn's accuracy rung. Source: Conn's (a), (b) and rejoinder; the lead's edit 1.
25. Item 3 bounds: 'concedes in the draft' and its annotation replaced by 'concedes in this plan', plus the lead's words to Conn ('A missing modulus voids my bracket'). Source: First verifier, problem 4; the lead's item 3 answer *(citation not confirmed: no lead turn concedes the rim; the quoted answer to Conn withdraws the Lipschitz charge against the bilevel rule, so the link is inferred)*.
26. Item 3 unresolved: the lead's narrowed coverage case and Conn's rejoinder objection quoted; his rung and audit class adopted; his risk line on the audit class quoted (moderator's check). Source: The lead's item 3 answer; Conn's rejoinder (deciding test and risk line).
27. Item 4 header: Dey agrees on the stop, his evidence boundary quoted (moderator's check); the lead's fix changes (products become an arm; the tree decides). Source: Dey's turn (POSITION); the lead's item 4 answer.
28. Item 4 problems: Dey's sets, as in the lead's amendment (2), and Dey's κ = 2 set. Source: Dey's (b) and rejoinder; the lead's amendment (2).
29. Item 4 ledgers: Dey's (a)-(d) run as amended, the gate and the native and fixed-incumbent columns in ledger (1), his (d) (one gap of 10⁻⁴ for every solver, defaults as a labelled second run) in both ledgers. The lead's 'ledger (1) runs (a)-(d)' was corrected at the moderator's check, since (d) covers all solvers. Source: Dey's (a)-(d); the lead's amendments (1), (3) and (4).
30. Item 4 incumbents: one BARON label, 'BARON 26.9.10 (release notes: 2026.9.10)'. Source: First verifier, problem 11.
31. Item 4 settings: Burer's looser common gap added, verbatim. Source: Burer's v1 dissent.
32. Item 4 metric: fixed-column dominance replaces proofs per second; wins in the native column alone are credited to primal help. Source: Dey's rejoinder; the lead's item 4 answer (native column).
33. Item 4: Burer's quoted risk line marked as now in the settings; Dey's rejoinder risk line quoted in full, 'S119 is a preprint' included (moderator's check). Source: Burer's v1 dissent; Dey's rejoinder (risk line).
34. Switch rule 1: covers every then-arm and both rebuilds; a (v′) breach reruns the arm on (8) or provable bounds. Source: Gould's v1 dissent; Sahinidis's (v′); the lead's (v).
35. Switch rule 2: Sahinidis's switch rule, the runs setting the order; open gaps at p ≤ 200 recorded as a capability gap. Source: Sahinidis, item 2; the lead's item 2 answer.
36. Switch rule 3: Audet's wording, verbatim; the lead's tier and component rules, after Conn; Conn's accuracy-or-coverage rule, quoted as his (attribution split at the moderator's check). Source: Audet's v1 dissent; the lead's item 3 answer; Conn's rejoinder.
37. Switch rule 4: the gate; fixed-column dominance on the headroom band and two libraries, one of them QPLIB or MINLPLib; 'Crossing frontiers leave no default', labelled as Dey's risk line (label added at the moderator's check). Source: Sahinidis's v1 dissent; the lead's amendment (1); Dey's rejoinder (risk line).
38. Minimal experiment: the challengers'-round deciding tests are included and their refinements govern; item 3's starts switch runs first; equal budgets per k-path and per pipeline; Mittelmann's numbers carry their releases, threads and limits. Source: Challengers' round; Conn; Sahinidis's (2), (b); first verifier, problem 9.
39. Reformulation ideas, structure-chosen products: the lead's concession to Dey quoted (moderator's check). Source: The lead's item 4 answer to Dey; Dey's turn.
40. Part 5: decisions updated (headline gap, hold-outs, model use, gradients, Γ, dike data, longer ground truth, CPLEX and exact MIP engines), each with who asked. Source: The lead's, Sahinidis's, Nocedal's, Conn's and Dey's questions; first verifier, problem 2; the lead's v1 sign-off.
41. Part 6: Q3, Q6, Q7 and Q11 rewritten; Q14 adds the dike data; Q16 answered; Q18 resolved in the plan's own text, with Sahinidis's own label noted; Q19-Q23 added; Q22 carries Dey's evidence sentence (Q18's note and Q22's sentence added at the moderator's check). Source: Challengers' round questions (Dey's question field included); first verifier, problems 2 and 11; the lead's v1 sign-off.
42. Neutrality note, v2 line: the L0Learn and relaxed-Lasso arms return as Sahinidis's (a), argued and accepted, no longer as the lead's restoration. Source: Sahinidis, item 2 challenger turn, (a); the lead's item 2 answer; the lead's v1 sign-off.
43. CPLEX and exact MIP reformulations (the lead's v1 sign-off) kept only as his labelled proposal (part 5, Q23); CPLEX release unverified; citations as in his sign-off [S377 p. 29; S708 pp. 37, 40]. Source: The lead's v1 sign-off.
44. Footnote: the relaxation-only source corrected to the BARON user manual, §4.1 and §10.2, credited to the first verifier (annotation resolved); the v2 rechecks noted. Source: First verifier, problem 3; the lead's challengers'-round answers (CRAN, Gurobi, BARON and SCIP checks).
45. Not applied: first-verifier problems 5-8 and 12 concern members' turns, not the plan's own text. Problem 8's annotation stays on Burer's quoted risk line. Source: First verifier, problems 5-8, 12.

### The lead's responses to the v1 dissents

- **Gould**, accepted. **Condition:** With the best-bound rebuild added to item 1's then-arms and backup rule 1, I sign. **Note:** Accepted from Gould's v1 dissent (already the lead's (vii) in the challengers' round). Item 1's then-arms rebuild S040 as printed and best-bound, and switch rule 1 gates both rebuilds *(citation not confirmed: Gould's node-count gate binds the printed rebuild; his v2 sign-off holds only if it binds that rebuild alone)*. Grounds: Method 4 step 5 (duel the incumbent at its strongest).
- **Nocedal**, accepted. **Condition:** Those readings score a one-sample stop (2) (design inferred), tabulated against the oracle [S018 p. 20]. **Note:** Accepted from Nocedal's v1 dissent. Item 2's Reading quotes the condition verbatim beside (V1)-(V2), so the bound is credited only as a stop that users can run. Grounds: Method 4 step 3 (the same usable stop for every method).
- **Wright**, accepted. **Condition:** Holds while that contest stays open: no band certified on beating stop (2) alone (→ Wright · Method 5 stop rule). **Note:** Accepted from Wright's conditional sign-off. (V1) certifies only where a run closed at the chosen (k, γ) beats its own earlier stops and every twin, his longest stall window included. No band is certified on beating stop (2) alone. v1's split stays unresolved in v2, narrowed by (V1); Wright has had no turn on (V1) *(citation not confirmed: Nocedal's and Wright's v2 sign-offs now answer (V1), both as dissents)*, so the contest stays open.
- **Audet**, accepted. **Condition:** Switch rule 3 reads: failed referee calibration, or calibration on a voided bracket → EM reports found lower bounds only, no 'unrefuted at budget B', no inner-rule ranking. **Note:** Accepted from Audet's v1 dissent (also adopted in the lead's answer to Conn). Switch rule 3 quotes it verbatim. Grounds: Method 7 stop rule (no bound, no claim).
- **Sahinidis**, accepted. **Condition:** Item 4's decision rule: at least one of the two libraries on which the LMI must out-prove every cheaper arm is QPLIB or MINLPLib, outside the RPT papers' own test families. **Note:** Accepted from Sahinidis's v1 dissent (also in the lead's answer to Dey). Switch rule 4: a heavier rung stays a default only where it dominates on the headroom band and on two libraries, one of them QPLIB or MINLPLib. Grounds: Workflow C step 3 (regimes a critic would choose).
- **Burer**, accepted. **Condition:** Every ledger-(1) arm also reports proofs at one looser common gap (e.g., 10⁻³, a decade looser, like the two levels in [S014 preprint pp. 15–16]; catalog E6), node-solve accuracy matched to each gap (H7); “the LMI itself does” holds only where splitting loses at both. **Note:** Accepted from Burer's v1 dissent and added verbatim under item 4's settings. The proof rule stays at 10⁻⁴. The looser common gap is reported beside it and decides only whether a loss is the LMI's or its solver's. Grounds: Method 4 step 3 (one stated tolerance for all arms, here two common levels). It adds runs.

### Moderator's neutrality note (v2), with the lists

**Moderator's neutrality note (v2).** Changed, each from the record:
- Item 2: "Resolved in (V1)" *(citation not confirmed: the words are in no turn or sign-off; they come from the lead's pre-check draft, not reproduced)* is back to unresolved, now narrowed by (V1). Nocedal and Wright have had no turn on (V1) *(citation not confirmed: Nocedal's and Wright's v2 sign-offs now answer (V1), both as dissents)*, and (V1) leaves out the first clause of Nocedal's reading 3 ("tighten the stop to the winning support's arrival gap"). Wright's sign-off holds only "while that contest stays open".
- Credit and labels:
  - the leaps arm is Sahinidis's (1), refined in the lead's (1′);
  - the hold-out is whatever the user freezes before any run, since the record says one may not exist;
  - the gradient incumbent is Conn's (d) on EM, extended to every tier by the lead;
  - switch rule 3 keeps the lead's words apart from Conn's;
  - "Crossing frontiers leave no default" is marked as Dey's risk line;
  - Dey's (d) covers every solver, not ledger (1) alone.
- Restored from the turns:
  - the challengers' own evidence boundaries, beside their agreement;
  - Sahinidis's 10⁻⁶ caveat;
  - Conn's "unverified" mark on tier (c) and his risk line on the adopted audit class;
  - Dey's full risk line, including "S119 is a preprint";
  - the lead's concession to Dey, under structure-chosen products;
  - Dey's evidence in question 22.
- Small fixes: Burer's risk line is marked as now in the settings. Question 18 and the footnote's relaxation-only source are attributed as the record has them.
- In the lists: two changes-list sources that cited "task point 4" now cite turns; Wright's and Burer's dissent conditions are restored verbatim; Wright's response no longer calls the split resolved.

Kept: every v1 line the lead did not change is word for word, annotations included. All five v1 dissents were accepted, and each is carried out in the plan text. Two sign-off citations now in the plan text were not covered by the first verifier: Burer's (card c01) and the lead's in question 23 (cards s2-17 and s2-18). Both match their cards (checked here). v1's sign-offs were given on v1, and no delegate has yet seen the changes in v2 *(citation not confirmed: outdated, like the line on (V1): every seated lens has since signed or dissented on v2)*.

## Sign-off on v2

Every seated lens signed or dissented on v2, verbatim:

- [Bertsimas lens] ✅ sign-off: Each item names incumbent, class with solve-time test, certificate, gap or bound, and decision metric (convener rule; Methods 1, 4, 7). Accepted: item 2 unresolved until Nocedal and Wright answer (V1) [02 P7] *(citation not confirmed: note 02 P7 concerns agreeing PhD topics with students; the transfer to a council item is inferred)*; Dey's fixed-column dominance (Method 4, step 3). My v1 arms return as Sahinidis's (a); CPLEX stays Q23. [v1 condition met: no v1 condition]
- [Huangfu lens] ✅ sign-off: Item 1 only; MIO: inferred. v2 keeps my v1 grounds: additions verbatim, proved-cells gate (→ Huangfu · H3), net ratios only where both certify, context-only unresolved (→ Workflow E, step 5). (vi)'s 10⁻⁶ against exhaustive search makes my ratio an equal task (→ Workflow C, step 2). [v1 condition met: no v1 condition]
- [Gould lens] ✅ sign-off: Signed: v2 adds the best-bound rebuild to item 1's then-arms and backup rule 1 (→ Gould · Method 5, steps 2–3). But a best-bound search need not repeat S040's depth-first node counts [dimitris-bertsimas card S040 pp. 10, 17–21], so that gate binds only the printed rebuild (MIQO: inferred transfer). (holds if backup rule 1's node-count gate binds only the printed rebuild, and the best-bound arm is that reproduced code with node selection alone changed (→ Gould · Method 4, step 5).) [v1 condition met: yes]
- [Nocedal lens] ⚠️ dissent: Item 2: v1 condition met. But (V1) counts capped wins as search yet credits closing whenever a closed run wins, though statistics freeze when the winning support arrives (→ Nocedal · Workflow D checkpoint; Method 3 [S013 pp. 10–12], inferred). Item 3: signed. Items 1, 4: outside my evidence. (holds if (V1) prints each draw's winning-support arrival gap, replayed from the logs (design inferred). Certify only where arrival gaps are ≤ ε = 10⁻⁴; above it, the win counts as search, and stop (2) tightens to the smallest such gap, set on development designs and scored on the hold-out.) [v1 condition met: yes]
- [Wright lens] ⚠️ dissent: MIO lies outside my evidence. v1 condition met: V1 adopts my every-twin rule, so no band is certified on beating stop (2) alone. But V1 scores twins at the closed run's validation-chosen (k, γ), not their own: a one-tuning win is a regime (→ Wright · Method 5 stop rule). (holds if V1 also holds with each earlier stop and twin choosing its own (k, γ) by validation, as Nocedal's (3) tunes every budget.) [v1 condition met: yes]
- [Vicente lens] ✅ sign-off: Both v1 points hold: item 3 quotes me accurately; Example III keeps the angle mesh. Conn's accuracy rung, my swap arm at the tied tolerance [S047 preprint p. 14], isolates my H3 default from coverage (→ Vicente · Method 5 [S005 pp. 26–27]). Items 1, 2, 4: outside my evidence. [v1 condition met: no v1 condition]
- [Audet lens] ⚠️ dissent: v1 condition met verbatim. Dissent on v2's gradient incumbent: comparing DFO with derivative-using algorithms 'should be avoided' [S128 p. 5]. Sign if it stays FL4's reference line, outside item 3's profiles, and the derivative-free price is printed apart at two gradient-call weights [S128 p. 15; inferred] (→ Method 5). (holds if Item 3: the gradient search stays FL4's reference line, outside the withheld-gradient arms' profiles and verdicts; the price of going derivative-free is printed apart, at two weights per value-and-gradient call: 1 [dimitris-bertsimas card S090 pp. 2, 11] and one declared before the runs (e.g., open question 20's answer).) [v1 condition met: yes]
- [Conn lens] ⚠️ dissent: Dissent on my audit class: since found worst values underestimate, every rise after a ratio-accepted step clears its threshold (inferred) [S066 pp. 5–6], filing missed maximizers at the new iterate as accuracy. Sign if accuracy counts only shortfalls closed by ascending from the arm's own inner point (→ M3; P16). (holds if Switch rule 3's audit class (mine) reads, replacing its η₀′ test: a rise after a Theorem-1-passing step counts as accuracy only where a local ascent from the arm's own accepted inner point at the new iterate reaches the score; otherwise it is a missed maximizer, counted with missed ties as coverage [S066 pp. 2, 8; inferred].) [v1 condition met: did not sign v1]
- [Sahinidis lens] ✅ sign-off: Signed. Items 1–2 carry my round's additions; switch rule 4 meets my v1 condition, QPLIB or MINLPLib as one library (→ Sahinidis · Workflow D). Holds if any instance an RPT paper ran counts as development: no card names their ten QCQPs' source [dimitris-bertsimas card S624 p. 10]. (holds if Holds if any QPLIB or MINLPLib instance that an RPT paper ran (for example their ten QCQPs, whose source no card names) is scored as a development set, not as hold-out.) [v1 condition met: yes]
- [Burer lens] ✅ sign-off: Sign-off: v1 condition met verbatim. Under Dey's metric, my 'loses per second' means fixed-column losses at both gaps [S020 pp. 12, 16] (→ Burer · Workflow C). I read Dey's κ = 2 optimum as a rechecked feasible value certified on two signals [S049 arXiv p. 10] (→ Method 3). [v1 condition met: yes]
- [Dey lens] ⚠️ dissent: Dissent, item 4 (items 1–3: outside my evidence); v2 otherwise carries my rejoinder. Name one bounded gap formula for proofs and gap left, per library: e.g. |U−L|/max(|U|,|L|,1), no-bound runs at its cap (design inferred). My summed absolute gap [S129 p. 20] lets large-objective instances decide (→ Method 1 step 4). (holds if Item 4 names one gap formula, fixed before the runs and bounded on every instance, for both the 10⁻⁴ proof test and the gap left at the limit, per library (e.g. |U−L|/max(|U|,|L|,1), equal to S129's absolute gap where |U|, |L| ≤ 1; no-bound runs at its cap; design inferred).) [v1 condition met: did not sign v1]

*Moderator's notes (v2)*

- **Tally:** six sign-offs and five dissents. Signed without a condition: Bertsimas, Huangfu, Vicente and Burer. Signed with a condition: Gould (backup rule 1's node-count gate binds only the printed rebuild, and the best-bound arm is that reproduced code with node selection alone changed) and Sahinidis (any QPLIB or MINLPLib instance an RPT paper ran is scored as a development set, not as hold-out). Dissents, each with the condition under which it would sign: Nocedal (item 2: (V1) prints each draw's winning-support arrival gap and certifies only where it is ≤ ε = 10⁻⁴; above it the win counts as search and stop (2) tightens to the smallest such gap); Wright (item 2: V1 also holds with each earlier stop and twin choosing its own (k, γ) by validation); Audet (item 3: the gradient search stays FL4's reference line, outside the withheld-gradient arms' profiles and verdicts, with the derivative-free price printed apart at two weights per value-and-gradient call); Conn (item 3: his audit class counts a rise as accuracy only where a local ascent from the arm's own accepted inner point reaches the score, otherwise as a missed maximizer counted with missed ties as coverage); Dey (item 4: one gap formula, fixed before the runs and bounded on every instance, for both the 10⁻⁴ proof test and the gap left at the limit, per library).
- **Conditions v2 does not yet meet:** by the third verifier's reading (problems 16 and 19 under [Verification](#verification)), v2 meets neither Gould's nor Sahinidis's condition, so both ✅ count as conditional.
- **v1 conditions:** every lens that set a condition on v1 (the five dissents and Wright's conditional sign-off) records it as met; Conn and Dey, who had no turn in the first run, did not sign v1. Nocedal and Wright answer (V1) here for the first time, both with dissents, so v2's lines saying they have had no turn on it are annotated as outdated.
- **Owed before checkpoint 4:** nothing; all eleven seated lenses returned a line on v2. The plan awaits the user's approval at checkpoint 4.

## What was argued

Disagreement → deciding test, per item. The user has decided nothing yet: the session ran in autopilot, and the decisions wait for checkpoint 4.

- Item 1 · FL1 · Is a release-series factor a net gain? Huangfu: only where the old release was the best code for the class, and on subset selection the 2009 tailored branch and bound outran CPLEX. The lead conceded this but held that CPLEX ran depth-first on big-M (M = 100) and was never shown at defaults; Huangfu then conceded that his "beaten base" awaits a defaults rerun → FL1 deciding test, as argued, plus a net arm (the 2009 code rebuilt from print, and leaps 3.2) and the lead's formulation arm (the oldest and newest runnable releases on S040's big-M form, M made provably valid, and on (8), at defaults and at S040's settings), with the then-arms scored on proof.
- Item 1 · FL1 · Can a moved certified frontier carry "now tractable" on its own? The lead, scoring by Gould's certified frontier: credit an arm only if it moves the frontier, and the abstract carries the frontier and the net factor measured there. Huangfu: "moving the frontier or that ratio alone earns context-only" (unresolved; his point that the net factor is censored is accepted) → per arm, the largest p in S010's Example 1 at n = 1000 that reaches a 1% gap within 15 min for every k from 5 to 25, beside the geometric-mean time ratio to the 1% gap against the strongest then-arm where both reach it, else bounds.
- Item 1 · FL1 · Does S010's "less scalable" verdict on the 2009 code hold? S010 gives it without a run. Gould: a losing 2009 arm confirms it "only if reproduced and fairly armed", and Example 1 is random data → the rebuild first reproduces S040's node counts in the cells S040 solved (Gould) and proves S040's proved cells (Huangfu); a best-bound node-selection arm; frozen real designs with planted β. The verdict stands only if both 2009 arms miss (Gould), and is withdrawn if the 2009 code reaches the newest release's frontier (the lead).
- Item 2 · FL2 · What does proof time buy a statistical estimator? The lead: only the MIO's bound measures how far a stopped run is from the ℓ0 optimum, and certifying may pay in S061's band. Nocedal: after the last incumbent change, proof time buys "a stopping decision and the word 'optimal', not out-of-sample error", and "where the capped run wins, search pays, not proof". Wright: S288's FDR gain "prices the exact ℓ0 model, not the exact solve" (unresolved) → FL2 deciding test, as argued, with Nocedal's incumbent-change logs, his statistics-matched stop (2) on oracle and one-sample spreads, and equal tuning per budget; Wright's whole-path twins; the lead's stall twin, n-sweep across the recovery transition at (p, k) = (2,000, 10), and Hamming distances. Where the capped run beats stop (2) by more than one SE, the lead would "certify in that band"; Nocedal would "tighten the stop to the winning support's arrival gap; certify only at a closed gap".
- Item 2 · FL2 · Can a small gap hide a wrong support? Wright: "a small gap, in objective units, can hide a wrong support (inferred). Certify a band only if every twin, longest stall window included, trails beyond one SE" (unresolved against the lead's band reading) → a p ≤ 12 design with every k-support enumerated: per draw, each support within stop (2)'s threshold, with Hamming distances to the optimum and the truth, FDR and test loss; certified runs re-solved at tighter tolerances. The objection fails at any SNR where only the optimum's support lies within the threshold in every draw.
- Item 3 · FL4 · What may a stopped robust search on a simulator claim? Settled after the lead's concessions to Vicente, Audet and Nocedal: a lower bound only, "worst-case cost ≥ ĝ, unrefuted by referee R at budget B", under a heuristic label, with the 96% figure withdrawn as evidence on the inner rule. Audet still contests "any EM verdict resting on my referee alone" → calibration on Examples I and III (seeded multistart Reverse referees, intersected, from common starts; bracket-refuted claims that the referee passes are counted). EM claims stand as "unrefuted at budget B" only if the referee recovers the bracket ranking.
- Item 3 · FL4 · Which inner rule? The lead: several short ascents plus a history set where worst errors tie ("untested"). Vicente: inner accuracy tied to outer progress, "this lens's default, untested here". Nocedal: "neither by default; the call-counted test decides" (unresolved) → FL4 deciding test, as argued, run as a 2 × 2 (outer step × inner rule) in one code base with gradients withheld (each finite-difference gradient charged 2 calls in Example I, 18 in Example III). It includes Vicente's swap arm and Example III; Audet's common Reverse referee, its cost printed; Nocedal's seeded multistarts, one stopping rule, oracle arms, and constants at ×10 and ÷10; and random sampling as the baseline. An inner rule wins where its designs' upper bounds fall below the rival's lower bounds across seeds; overlapping brackets are a draw at that budget.
- Item 3 · FL4 · Can Example III be bracketed in closed form? The lead: its 16 coefficients enter linearly in one joint ℓ2 ball, so their worst case is a norm term and a 2-D bracket remains (inferred). Vicente and Nocedal: the reduction leaves √(Γ²−‖Δx‖²), whose slope is unbounded at the rim, so no modulus exists (inferred; Nocedal: "two separate balls void it"). The lead's draft concedes the rim *(citation not confirmed: the concession appears only in the plan draft; no lead turn follows the rejoinders)* → Example III meshed in angles (θ, φ in Δx = Γ sin θ (cos φ, sin φ)); 18-D multistart ascents at several designs must never exceed the closed-form upper bound, or the scorer fails; Vicente's rung of summed Example I blocks, Householder-reflected to keep the ball, with its radius split bracketed too.
- Item 4 · FL5 · Where does the LMI pay? The lead: "The LMI pays on some classes, not yet at scale", with structure-chosen products as the device. Sahinidis: class-dependent; a portfolio with per-node switching, and the LMI emulated by cheaper cuts. Burer: separate the LMI from its solver, since "If (2) still loses per second, the LMI itself does" (unresolved) → ledger (1), rungs in one code (the deposit's use_lmi switch; RPT-BB with integers rebuilt with an all-open-node stop test; branching and node selection frozen, one component swapped at a time). Arms: no LMI; the LMI by MOSEK; the LMI by splitting with a dual-feasible bound; an outer approximation admitted per node. Each runs with and without domain reduction, and both LMI solvers are timed to their common bound. The lead's rule keeps the LMI a default only where it proves more instances per second than every cheaper arm on two libraries.
- Item 4 · FL5 · Do the RPT wins over BARON measure rungs or engines? Sahinidis: the duels with BARON 20.10.16 and 21.1.13 also differ in branching, so "they compare engines, not rungs" (conceded by the lead), and "neither ledger prices the rung inside BARON" → ledger (2): current BARON and SCIP at defaults, one thread, beside BARON 20.10.16 and 21.1.13 where they still run, plus BARON with structure-chosen products declared relaxation-only, on and off.
- Item 4 · FL5 · What counts as a proof? Sahinidis: the integer sequel's printed stop test checks only the smaller child bound (conceded by the lead), and the lead's proof rule "trusts each arm's own log". Burer: the rule "keys on solver status; only provably valid bounds may prune or enter the open-node minimum" → a run counts as proved only if its log shows the gap within 10⁻⁴ of the open-node minimum at exit and an exit by the gap test. Non-OPTIMAL children keep their parent's bound and stay open, each logged as a failure. Bounds that contradict another arm's rechecked incumbent, or the library's bound, fail the run.

Challengers' round:

- Item 1 · FL1 · Was leaps' 'p ≤ 30' measured? Sahinidis: no; two of the lead's cards state it with no run, and leaps() stops above 31 columns at its default (the link to the '30' he marks inferred); conceded. Test: Sahinidis's (1) as refined in the lead's (1′), exhaustive regsubsets (nvmax = 25, really.big = TRUE, intercept = FALSE) on the MIO arms' X and y, with finish and overrun printed; 'p ≤ 30' stands only if it cannot finish the path at p = 31 within the budget.
- Item 1 · FL1 · Are the arms given equal tasks? Sahinidis: regsubsets returns every model size in one run. Test: one total budget for the k = 5–25 path (21 × 15 min), S010's per-k stop inside it, time to each k printed (accepted).
- Item 1 · FL1 · Is a finished search exact? Sahinidis: 'exact' is a tolerance, so print the frontier at 1% and at 10⁻⁶. The lead added a regsubsets audit of every MIO certificate (v). Sahinidis: regsubsets is 'global within tolerances, not exact'. Test: (v′), one evaluator refits every support; an LB_k above the best refit RSS_k by more than max(10⁻⁶, 10⁻⁶·RSS_k) voids that arm's certificates; labels 'audited to p = …' or 'cross-checked only' (accepted in v2).
- Item 1 · FL1 · Which sets may carry 'now tractable'? The lead: a move on Example 1 alone reads 'on S010's generator'. Sahinidis: Diabetes is S010's too, so moves there read 'on S010's instances', and an unscoped claim needs a set fixed before any run by someone who tunes no arm. Test: per-set reporting, plus any hold-out the user freezes before any run (accepted in v2; open question 19).
- Item 2 · FL2 · Which incumbents? Sahinidis: v1 omitted ncvreg, whose MCP and SCAD S095 printed ahead in places. Test: his arms (a): glmnet 5.2 with relax, L0Learn 2.1.0 (L0L2, its own cross-validation), ncvreg 3.16.0, Glasso, MB and QUIC *(unverified)*; the lead adds an MIO warm-started from L0Learn.
- Item 2 · FL2 · Is the price measured? Sahinidis: v1 fixed γ a priori and timed unequal tasks; conceded by the lead. Test: the item stops at knob and price, with whole tuned pipelines on one model-size grid, a γ grid, and work-limit stops calibrated per family.
- Item 2 · FL2 · When does proof pay? Sahinidis: only where a closed-gap run beats every arm, capped runs reported apart; where none closes, as in S061's band, a capability gap. The lead concedes the band and, after Nocedal, counts a capped win as search; he holds that proof time is read against the run's own stops, with Sahinidis's every-arm rule deciding the default (Sahinidis accepts). Test: the lead's (V1)/(V2) readings, capped runs tabulated apart, with kill results for both sides. Nocedal and Wright have had no turn on (V1) *(citation not confirmed: Nocedal's and Wright's v2 sign-offs now answer (V1), both as dissents)*, so item 2's split stays open.
- Item 2 · FL2 · Which hold-out? The lead: a critic's released designs. Sahinidis: S095 adopted HTT's PVE formula and SNR grid, so those designs have been seen. Test: a hold-out unused by S095, S288, HTT or his group (accepted in v2).
- Item 2 · FL2 · What counts as 'closed'? Sahinidis: ε = 10⁻⁴, S095's own stop [S095 p. 5] (accepted in v2).
- Item 2 · FL2 · Can 'FDR or test loss' hide a loss? Sahinidis: V1 needs a one-SE win on one metric and no one-SE loss on the other (accepted in v2).
- Item 2 · FL2 · Bounds first, or the big-M-free form first? Sahinidis: tighten bounds, then reformulate; the lead's stop rule puts the big-M-free form first. Test: both run as arms, and the runs set the order (switch rule 2).
- Item 2 · ML §6.1, point 1 (recorded in both teams' notes; on no card) · What did the 2020 discussion price? The lead: an uncertified CIO, with no gap recorded. Sahinidis concedes in his rejoinder; no deciding test was named.
- Item 3 · FL4 · Can two hand-built examples carry 'wins'? Conn: no; conceded by the lead. Test: his frozen public tier (c) (its CUTEst problems unverified beyond SNAIL, HAIRY and CLIFF, as he marks them) *(none needed: all 20 are in CUTEst (checked), so lift 'the rest unverified'; flag PFIT1LS as bound-constrained)*, with Γ on a frozen grid. Verdicts per tier: 'preferable' only where brackets separate; 'wins' only where every tier agrees; otherwise 'competitive' or 'complement each other'.
- Item 3 · FL4 · What does the inner-rule factor switch? Conn: starts, accuracy and derivative source all at once. Test: single switches, the starts switch first, then finite differences charged n calls; ladders: Conn's cumulative ablation plus the analysed variant, and the lead's history-set and depth rungs (accepted).
- Item 3 · FL4 · Is the termination test an optimality condition? Conn: it is a stopping rule. Conceded by the lead; it becomes a claim-ledger line.
- Item 3 · FL4 · Does a missing Lipschitz modulus void the tied-tolerance rule? Conn: it voids a bracket, not the rule, since the code fixes its constants at 10⁻². The lead withdraws the charge.
- Item 3 · FL4 · Which gradient arm is the incumbent? Conn: the adjoint search, on EM. Test: the gradient search on every tier (the lead's extension), one value-and-gradient call counted once; each withheld-gradient arm prints its extra calls at an equal scored worst case, replacing FL4's reference line.
- Item 3 · FL4 · Coverage or inner accuracy at ties? The lead: coverage of the tied maximizers, tested by the starts switch. Conn: untested. Test: his accuracy rung (the swap arm's ascents run to the tied tolerance) and audit class (rises after Theorem-1-passing steps whose accepted worst value trailed the score by more than η₀′ × the predicted decrease). If that rung wins at equal calls, or that class outnumbers missed ties, accuracy decides; otherwise coverage stands (adopted; open until run). Conn's risk line: 'SOCP steps predict no decrease; there use the estimated drop (inferred).'
- Item 4 · FL5 · Are structure-chosen products cheaper than the LMI? Dey: on his set the reverse holds; conceded by the lead. Test: the products become an arm, and the harness must first reproduce Dey's n ≤ 10 order or no n ≥ 20 row counts.
- Item 4 · FL5 · Does ledger (1) isolate the rung? Dey: RPT-BB reads its incumbents and branching off each rung's solution. Test: native and fixed-incumbent columns, with RLT's partitions replayed; root gap, tree size, time to best and time to proof printed apart.
- Item 4 · FL5 · Root screen or tree? Dey: drop dominated rungs on root gap against time. The lead, from Dey's own card: tighter relaxations can enlarge trees (MILP). Test: every arm runs through the tree, none dropped at the root (Dey accepts); by the lead's settle rule, if a root-dominated rung never proves more in either tree column, at any n and library, Dey's root screen becomes the filter.
- Item 4 · FL5 · Which gap settings? Dey: one gap of 10⁻⁴ for every solver, with defaults as a labelled second run. Test: each run's gap recomputed from its logged bounds by one formula, finite across sign changes; BARON's and SCIP's defaults labelled.
- Item 4 · FL5 · Proofs per second, or dominance? Dey: per-second rates can rank fewer proofs above more, and the fixed column decides. Test: fixed-column dominance (proofs and gap left at the limit, time where all prove), plus his κ = 2 set at n ≥ 20 as a ground-truth audit (accepted in v2). Dey's risk line: 'Crossing frontiers leave no default; the fixed column discounts primal help; S119 is a preprint.'

## Verification

The moderator's Step 5 check ran twice, read-only: first by one verifier on the session's turns and the draft plan (v1), checking 40 load-bearing citations against the cards, then, after the challengers' round, by three verifiers (card citations, named things and numbers, fidelity to the record) on the new turns, plan v2 and its sign-offs. A citation census then checked every card citation of the first run against its card (the last subsection). Its findings are applied above as annotations in italics: *(unverified)* for each unverified item in the plan and in the deciding tests it includes by reference, *(citation not confirmed: …)* for each citation that the card does not carry as cited, and *(census correction: …)* where the census found a first-verification note mistaken. Nothing was deleted.

### First verification (the session's turns and plan v1)

#### The verifier's summary

> Read-only check of the council session (no repository file was changed; downloads went only to the scratchpad).
>
> 1. Citation scope. Every [S…] in a member's turn resolves to that member's own cards. The lead's IDs are in product/optimization-council/dimitris-bertsimas/references/research/cards, and B009 is card c5-03. Nocedal: S004, S006, S013, S018, S038, S040 (the 2002 wedge paper; the lead's S040 is the 2009 Bertsimas–Shioda paper, which is correct per member but easy to confuse), S041, S043, S062, S080, S084, S091. Vicente: S005, S047, S053. Audet: S055 (abstract level, cited by id alone), S156, S172. Burer: S014, S016, S020, S021, S047, S049. Every cross-member citation carries the slug of a member seated on that item (andrew-conn S066, charles-audet S156, santanu-s-dey S129, samuel-burer S016 and S020, jorge-nocedal S004). The four members without cards (Huangfu, Gould, Wright, Sahinidis) cite SKILL.md sections or note anchors, and all of those exist. Read levels allow pages: S288, S377 and S708 are partial, the rest full.
>
> 2. Card support. I opened the cards behind 40 load-bearing citations, plus the guests' notes and two paper texts in sources/papers/txt. No card contradicts its claim. Seven claims rest on paper text or fetched sources that the card does not carry; these are listed in problems.
>
> 3. Items named in the plan, verified with tools. Software and releases:
> - leaps 3.2 (CRAN, 2024-06-10) and glmnet 5.2 (CRAN, 2026-10-28, has the relax option); glasso 1.11; L0Learn 2.1.0, which the plan strikes; Diabetes data with 64-column x2 in lars 1.3.
> - BARON 26.9.10 (10 Sep 2026). The free build handles up to 10 variables and constraints and 50 nonlinear operations. BARON 20.10.16 and 21.1.13 appear in the release notes. MAXWORK is new in 2026.9.10, and hierarchical RLT cuts appear from 2026.2.10.
> - SCIP 10.1.0 (Sep 2026).
> - MOSEK: conic problems get only an interior-point optimizer, and NUM_THREADS = 0 lets the optimizer choose.
> - The IJOC deposit github.com/INFORMSJoC/2023.0345 is in Julia with a use_lmi switch. Its branch and bound takes the minimum lower bound over open nodes. A child whose status is not OPTIMAL is dropped (SLOW_PROGRESS is commented out). Its (α, β) values (5, 15), (5, 50), (5, 100), (5, 500) differ from printed Table 7. Script saved to a local scratch copy (path omitted here).
>
> Papers and libraries:
> - SDPNAL+ (MATLAB) is arXiv:1710.10604. arXiv:2106.13721 is Nohra, Raghunathan and Sahinidis on MIQPs with linear equality constraints, implemented in BARON.
> - qcqp2 is listed on minlp.com's test-problem page, and the 2011 Bao–Sahinidis–Tawarmalani DOI resolves.
> - MINLPLib, QPLIB, Moré–Wild 2009 and the DOIs or arXiv ids of S010, S040, S061, S090, S095, S116, S141, S019, S288, S415, S624, S129 and S156 all resolve. Mittelmann's benchmarks and Top500 are online.
>
> 4. Numbers. Every factual number in the plan traces to a card or to a source checked here. A few numbers have no source because they are design choices, not results: the 1 h cap, n ≥ 20, 'two libraries', the 1/8/16 thread counts inherited from FL1, the item order, and, through the deciding tests, Wright's p ≤ 12 enumeration, Nocedal's ×10/÷10 sweep and the one-SE thresholds.
>
> Outside the three checks: the four challengers have no turn in the session (Sahinidis in items 1–2, Conn in item 3, Dey in item 4). Their positions and sign-offs are still owed under Step 4 before checkpoint 4.

#### Problems found (12)

1. **Plan item 2 (FL2 deciding test, pasted by the moderator)**
   - Claim: Problem: convex integer ℓ0 estimators [S095 p. 11; S288 pp. 16–17] against glmnet, Glasso and QUIC (FL2's deciding test)
   - Problem: I could not verify a current QUIC release. The CRAN package QUIC was removed on 2020-08-03 (the archive ends at 1.1.1), and the authors' UT page (cs.utexas.edu/~sustik/QUIC) returns 404. The plan names no QUIC version or source. glmnet 5.2 (CRAN, 2026-10-28) and glasso 1.11 (CRAN, 2019-10-01) are verified.
   - Fix proposed: Name the QUIC build (archived CRAN QUIC 1.1.1, or the authors' C or MATLAB code) or mark QUIC (unverified).
   - Applied here: Marked *(unverified)* after QUIC in plan item 2 and in the FL2 deciding test reproduced under the plan's part 3.
2. **Lead (plan item 4 instances; lead's item 4 deciding test)**
   - Claim: Instances: continuous and integer dikes, with the same bounds xᵢ ≤ 300 for every arm [S708 p. 41]
   - Problem: No card names a public source for the Dutch dike-ring data (rings 10, 15 and 16). The S624 and S708 cards record no code or data release. The IJOC deposit (github.com/INFORMSJoC/2023.0345, fetched) holds only the §6.1 exponential-cone QP and the §6.2 palatable-diet experiments. Availability of the dike instances is unverified.
   - Fix proposed: Name the source of the dike data, or add 'request from the authors' to the user's decisions; mark the dike arm (unverified) until the data are in hand.
   - Applied here: Marked *(unverified)* in plan item 4 and in the lead's item 4 deciding test.
3. **Sahinidis lens (item 4 rejoinder) and the plan's 'Checked 2026-10-31' footnote**
   - Claim: BARON's manual advises declaring 'products of important existing constraints' relaxation-only (§4.1, firm, checked); footnote: 'BARON relaxation-only constraints (AIMMS BARON guide)'
   - Problem: The claim holds, but the footnote names the wrong source. The quoted phrase is in the BARON user manual at minlp.com/baron-user-manual, §4.1 'What makes a model easy or hard for BARON', declared through RELAXATION_ONLY_EQUATIONS (§10.2). The AIMMS relaxation-only page describes the facility but does not contain the phrase.
   - Fix proposed: Cite 'BARON user manual (minlp.com), §4.1 and §10.2' in the footnote.
   - Applied here: Annotated in the plan's footnote. The Sahinidis rejoinder's own citation (§4.1) holds and carries no annotation.
4. **Moderator (plan item 2 'Unresolved'; also item 3 and the claim ledger)**
   - Claim: His draft locates that band "perhaps in S061's band", a band "FL2's fixed designs may miss"; item 3: 'The lead concedes in the draft that his Δx bracket fails at the rim'; ledger: Huangfu's rule 'accepted by the lead'
   - Problem: No turn in the session contains the words 'perhaps in S061's band'. The lead's item 2 reply says only that FL2's fixed designs 'may miss that band' [S061 p. 16]. The rim concession and the acceptance of Huangfu's net-ratio rule also appear only in the plan draft: no lead turn follows the rejoinders. Under the verbatim-quote rule, these lines cannot be traced to the session.
   - Fix proposed: Quote the transcript wording, or show the draft lines that the quotes and concessions come from, and record the lead's sign-off on them verbatim.
   - Applied here: Annotated at the three plan lines (claim ledger, item 2, item 3) and at the matching line of What was argued (item 3, Example III). The lead's ✅ sign-off on this plan is recorded verbatim under Sign-off.
5. **Lead (item 1 reply; its DECIDING TEST is part of the plan by reference)**
   - Claim: 'That p must reach a 1% gap within 15 minutes for every k from 5 to 25, S010's own path rule [S010 p. 32]'; times reported 'to show that it is computationally tractable' [S010 p. 32]; 'Diabetes was certified in 10–20 minutes by the big-M-free formulation (8) [S010 pp. 10–11]'; 'CPLEX ran depth-first on big-M with M = 100 [S040 p. 10]'; 'The change claimed is certification [S010 pp. 5, 8]'
   - Problem: The paper texts support each claim (checked in the lead's references/sources/papers/txt). S010 p. 32 has 'we only tested values of k from 5 through 25' and the quoted words. The Figure 2 caption on S010 p. 11 reads 'MIO formulation (8) for the diabetes dataset'. S040 p. 10 reads 'Our branch-and-bound and CPLEX's branch-and-bound search procedure used depth-first-search'. The cards do not carry these specifics. Card c16 even notes that the certified runs do not say which bounds they used, and the depth-first line on card c12 does not say that it applied to CPLEX. The suboptimality-guarantee claim sits at S010 pp. 1 and 6 on the card, not at pp. 5 and 8.
   - Fix proposed: Add these lines to cards c16 (S010) and c12 (S040), or cite them as paper text; cite the certification claim as [S010 pp. 1, 6].
   - Applied here: Annotated at the five citations in the lead's item 1 reply. Huangfu's item 1 rejoinder cites the same card for the same claim ("S040 ran CPLEX depth-first"), so the annotation is applied there too; card c12 was checked for it while this file was assembled.
6. **Lead (item 2 reply, addition (a))**
   - Claim: This is the stall-count exit of S095's relaxation algorithm [S095 pp. 6–8]
   - Problem: Card c22 does not describe a stall-count exit. The paper does: pp. 7–8 name 'the number of consecutive iterations without any improvement on the upper-bound' as an alternative stopping criterion (the default is Tmax = 200 or a 10⁻⁴ duality gap). Its p. 12 adds that early stopping did not hurt regression but failed in classification. The claim is supported by the source, not by the card.
   - Fix proposed: Cite [S095 pp. 7–8, 12] and add the stopping rule to card c22.
   - Applied here: Annotated in the lead's item 2 reply, addition (a).
7. **Nocedal lens (item 3 and rejoinder)**
   - Claim: this lens measures such constants rather than assuming them [S062 p. 8; S080 arXiv p. 6]; 'A bound that needs a constant users cannot know certifies nothing [S080 arXiv p. 6; inferred transfer to certification]'
   - Problem: S062 p. 8 is on its card. The S080 card shows nothing at p. 6. The fetched arXiv v1 p. 6 does say that the needed derivative bounds are hard to estimate ('existing procedures for estimating these bounds are not robust'), so the measurement point holds at source level. The certification step remains an inference, as the turn labels it.
   - Fix proposed: Add S080 p. 6 to card c12, or cite what the card already carries (estimated and re-estimated L, S080 pp. 11–12; the idealized Lipschitz arm, pp. 23–24).
   - Applied here: Annotated at the three S080 citations: two in Nocedal's item 3 opening, one in his rejoinder.
8. **Burer lens (item 4 risk line, quoted verbatim in plan item 4)**
   - Claim: splitting bounds are only moderately accurate [S014 preprint pp. 2, 17]; 'At 10⁻⁴, splitting's slow tail [S014 preprint pp. 2, 17] may lose for solver reasons'
   - Problem: S014 is a projected-gradient (first-order) code for the maxcut SDP, not a splitting method. Its card supports the slow limiting convergence of first-order methods (p. 2; benchmarks at 0.2% and 0.02%) and their moderate-accuracy niche (p. 20). Page 17 concerns ill-conditioning from negative edge weights. Carrying this to splitting or ALM codes is an inference.
   - Fix proposed: Cite [S014 preprint pp. 2, 14, 20] and label the transfer to splitting (inferred).
   - Applied here: Annotated in Burer's item 4 opening and rejoinder and in the plan's quote of the rejoinder's risk line.
9. **Plan item 4 / minimal experiment**
   - Claim: Mittelmann's third-party numbers beside item 4
   - Problem: The benchmarks exist and include BARON and SCIP: plato.asu.edu Continuous Non-Convex QPLIB, 17 May 2026 (BARON 25.12.10, SCIP 10.0.1, 8 threads, 3 h), and MINLPLib through GAMS, 26 Feb 2026 (2 h). Their releases and thread counts differ from the plan's BARON 26.9.10 and SCIP 10.1.0 at one thread.
   - Fix proposed: Print them with their releases, threads and limits, labelled as third-party context.
   - Applied here: Neither an unverified item nor a failed citation, so no annotation; the releases, threads and limits are listed under Sources for the run.
10. **Plan item 3**
    - Claim: Problem: min–max over an ℓ2 ball (Γ = 0.5), gradients withheld: Examples I and III [S090 pp. 8, 14], Vicente's summed-block rung, and EM if obtainable
    - Problem: Γ = 0.5 holds for Example I (card p. 8) and for Example III, where only the paper text (p. 14, max over ‖(Δx, Δy, Δp)‖₂ ≤ 0.5) gives it; card c2-02 does not state Example III's radius. The EM design uses Γ = 550 μm [S090 p. 12], yet the sentence reads as if 0.5 covered EM too.
    - Fix proposed: State Γ = 550 μm for EM [S090 p. 12], and add Example III's joint ball of radius 0.5 to card c2-02.
    - Applied here: Annotated in plan item 3.
11. **Sahinidis lens (item 4 DECIDING TEST (b), included verbatim in the plan)**
    - Claim: BARON 2026.9.10 and SCIP 10.1.0 at defaults, one thread, a time limit plus BARON's MaxWork
    - Problem: Cosmetic: the plan's own text says 'BARON 26.9.10'. Both are vendor labels for the 10 September 2026 release (download page 'Version 26.9.10'; release notes '2026.9.10'). MaxWork is verified as new in that release: MAXWORK, default −1, deterministic work units, BARSTATUS = 2 when exceeded.
    - Fix proposed: Use one label throughout: 'BARON 26.9.10 (release notes: 2026.9.10)'.
    - Applied here: Cosmetic; left as written. The plan's last open question records both labels.
12. **Huangfu lens (item 1)**
    - Claim: PAMI 1.51 against 2.34 [MPC pp. 138–140]; [Bixby 2012, pp. 116–118, read]; [KTH21 slides 25–26, read]; [HiGHS Parallelism docs, read]
    - Problem: This is a format issue only. Huangfu has no cards, so the council rule asks for SKILL.md or note citations; '[MPC pp. 138–140]' is a paper page (it is how his SKILL.md cites it, line 38, and note 05 §2.1 quotes MPC p. 138). All three external sources check out. Bixby 2012 pp. 116–118: twelve CPLEX versions, consecutive-pair geometric means, 'a projected, machine-independent improvement of a factor of over 29,000', and Gurobi 1.0 placed level with CPLEX 11.0 by Mittelmann's 2009 benchmarks. KTH21 slide 26: iteration count 0.98, solution time 1.16 and iteration speed 1.18; slide 25 has the self-speed-up of 1.88. HiGHS parallel docs: 'unlikely to be more than eight', bounded by memory channels.
    - Fix proposed: Cite [qi-huangfu SKILL.md, Activation Rules] or [qi-huangfu note 05 §2.1] for the MPC figures.
    - Applied here: Format only, the content confirmed; no annotation.

#### Unverified items (7)

1. QUIC: no current release or source found (CRAN package removed 2020-08-03, archive ends at 1.1.1; the authors' UT page returns 404); the plan names no version. *Marked in plan item 2 and in the FL2 deciding test.*
2. Dike instances (Dutch dike rings 10, 15 and 16) for item 4: no public data source on any card, and no code or data release for S624 or S708. *Marked in plan item 4 and in the lead's item 4 deciding test.*
3. ECnoise code download: the Argonne page (mcs.anl.gov/~wild/cnoise) returned 403. The method itself is published (Moré & Wild, 'Estimating computational noise'), confirmed through Optimization Online. *Marked in Nocedal's item 3 deciding test, addition (5).*
4. The 100-variable electromagnetic simulator and its error data: collaborators' code and privately communicated errors per S090 pp. 12 and 18; the plan already marks it 'if obtainable'. *Marked in plan item 3.*
5. Code for the integer sequel (S624) and the 2026 RPT revision (S708): the lead's 'none found (searched)' was not re-searched here. *Marked in the plan's open question on the integer sequel's code (part 6).*
6. Whether BARON 20.10.16 and 21.1.13, and the oldest MIO solver releases for item 1, can still be licensed and run on one machine. The BARON releases exist in the vendor's release notes; runnability was not tested. *Marked in plan item 1 (solver runs) and plan item 4 (incumbents).*
7. The MIO solver and the MOSEK release to be used in the runs are not named (left to run time). *Marked in plan item 1 (solver runs), item 2 (settings) and item 4 (the LMI by MOSEK).*

### Second verification (the challengers' round, plan v2 and its sign-offs)

Three verifiers, one lens each, all read-only. Their findings are applied as annotations in the new material only (the challengers' round, plan v2 and its lists, the v2 sign-offs and the new lines of What was argued); lines from the first run that repeat a flagged claim are left as they were.

#### The verifiers' summaries

**Card citations** (287 citation instances checked):

> Card-citation check of the challengers' round, programme plan v2 (the FL deciding tests and the responses to the v1 dissents included) and the v2 sign-offs. Read-only: no repository file was changed. Downloads went to my scratchpad only (local path omitted here; folders dl-s129, dl-alamo, dl-leaps, dl-l0learn, dl-gurobi).
>
> What I counted: 287 bracketed citation instances, with repeats in quotes counted each time. They resolve to:
> - 47 distinct cards across eight card sets: the lead 19, Conn 11, Dey 7, Burer 3, Nocedal 3, Vicente 2, Audet 1, Curtis 1;
> - 30 note anchors: Sahinidis's 02, 03 and 05, plus the lead's 02 O5 and P7 and 05 §1.3 and §1.4;
> - 5 anchors in the lead's domain files: ML §6.1 and §7, HS §5, IO §6, CP §6.2.
>
> I also checked 34 SKILL.md section references by the members without cards (Sahinidis, Huangfu, Gould, Wright). All of them exist and fit.
>
> Bare ids all resolve to the right member's card. Clashes such as S005, S014, S019, S020, S040 and S102, each used by two members, are used correctly, and every page cited falls inside its card's read range. 276 citations are supported as cited, some only through an inference the turn itself labels. I found 11 problems in 10 entries, 2 of them medium.
>
> Paper texts and documents read:
> - In the repository: S010 pp. 2, 26, 30, 32; S396 p. 2; S415 p. 27; S624 p. 12; S708 p. 40.
> - Downloaded: S129 (arXiv:2510.16595v1) p. 20, and ALAMO (arXiv:1705.10918v1) pp. 3–4. Both ALAMO claims hold: the why-now sentence on p. 3 has no citation, and p. 4 says "limited to only 32 regressors".
> - Outside documents that v2 newly relies on: the leaps 3.2 manual (all the leaps() and regsubsets statements made by Sahinidis and the lead are confirmed, and it has no tolerance or time-limit argument), the Gurobi WorkLimit text ("greatly depends on" and the same-hardware determinism are confirmed), and the L0Learn 2.1.0 manual (Gamma multiplies the ridge term, as the lead says).
>
> The neutrality note's two newly covered sign-off citations match their cards: Burer's S014 pp. 15–16 on card c01, and the lead's S377 p. 29 and S708 pp. 37, 40 on cards s2-17 and s2-18.
>
> The two medium problems both come from Dey's card S129. It gives no time for RLT+LMI (PRS) and does not say which RPT arm reached 960. So the order "RLT+LMI cheaper than the products" rests on the paper text: p. 20 says PRS is 6 s slower than PR, PRV reaches 959 at 121.177 s and PRSV 960 at 129.492 s. Dey's turn, the lead's concession and the lead's gate (amendment 1) all depend on that order.
>
> Also flagged: the first verifier's "not p. 17" on Burer's S014 citation, which card c01 contradicts; it should be narrowed to the splitting transfer.

**Named things and numbers** (193 items checked):

> Read-only check. No repository file was changed. Downloads went only to a local scratch folder, v2verify (path omitted here).
>
> Lens: named things and numbers new in the challengers' round, plan v2 and the v2 sign-offs. I checked 193 items:
> - 34 software, option and documentation facts;
> - 20 CUTEst problem files;
> - 31 paper identifiers;
> - 108 numbers and quotes against cards, notes or paper text.
>
> Confirmed with tools:
> - **leaps 3.2** (CRAN, 2024-06-10; source and Rd files read):
>   - leaps() defaults to strictly.compatible = TRUE and stops with an error above 31 columns.
>   - The manual calls it 'a compatibility wrapper for regsubsets' that uses 'an efficient branch-and-bound algorithm'.
>   - regsubsets defaults to nvmax = 8, needs really.big = TRUE for exhaustive search on more than 50 variables, and has no time-limit argument.
>   - It returns the best model of each size up to nvmax, and the manual says it 'does not actually fit each model'. No tolerance is documented.
>   - The leaps.setup page says really.big is 'required before R gets sent off on a long uninterruptible computation'.
>   - The lead's call regsubsets(method = "exhaustive", nvmax = 25, really.big = TRUE, intercept = FALSE) is valid.
>   - leaps 2.9 was the CRAN release from 2009-05-05 until 3.0 on 2017-01-10, and it had the same 31-column cap. The cap therefore held while S010 was written, but the link to S010's 'p = 30' stays inferred.
> - **arXiv:1705.10918v1** is Wilson and Sahinidis, 'The ALAMO approach to machine learning'. Page 3 has the 'hundreds or thousands of regressors' sentence with no citation, and the paper's experiments use 13-feature bases. Page 4 says the R leaps package [45] 'is limited to only 32 regressors'.
> - **R packages on CRAN:**
>   - ncvreg 3.16.0, with MCP and SCAD;
>   - L0Learn 2.1.0, with L0Learn.cvfit and penalty "L0L2". Its gamma multiplies the squared ℓ2 norm, while S095's γ divides it [card c22, pp. 4–5];
>   - glmnet 5.2, glasso 1.11 and huge 2.0.1 (method "mb");
>   - QUIC 1.1.1 is in the CRAN archive.
> - **Gurobi 13.0 reference:** WorkLimit stops at the same point only 'on the same hardware and with the same parameter and attribute settings'. A work unit 'greatly depends on the hardware ... and the model'.
> - **BARON manual v. 2026.9.10:** MaxTime defaults to 500 s. EpsR defaults to 1e-6, with the test |U − L| ≤ εr·max(|L|, |U|). Sections 4.1 and 10.2 cover relaxation-only constraints.
> - **SCIP 10.1.0:** limits/gap defaults to 0, with gap = |primal − dual|/MIN(|dual|, |primal|), which is 'Infinity' when the two signs differ.
> - **Newly cited papers all resolve:**
>   - the lead's S001, S005, S102, S184 and S396 (DOI), and S340 and S689 (arXiv);
>   - Conn's S009, S012, S019, S020, S040, S066, S074 and S075 (DOI); S233 (in the contents of NBS Special Publication 502); S188 (Namur report 94/04); and S102 (Namur report 97-13);
>   - Dey's S014, S028, S081, S100 and S123 (DOI), and S119 (arXiv);
>   - Audet's S128, and the DOIs of Burer's S020 and S049, Nocedal's S013 and S018, and Vicente's S005.
> - **Card numbers hold:**
>   - S415: 101 s against 2,100 s, and BARON 20.10.16 leaving optima unproved at nx = 20–100;
>   - S689: root closure up to n = 40, and BARON hitting the hour from n = 20;
>   - S708: the protocol of 10⁻⁴ gap, one thread and BARON 21.1.13;
>   - Dey's S014: BARON given 6 h against 1 h;
>   - S090: 40 μm, 550 μm, over 95%, and the 10 + 1 and 3 + 1 ascents;
>   - S066: the 10⁻² constants and η0 − 2η0′;
>   - S095: ε = 10⁻⁴, the γ divisor and the 60 s limit;
>   - S288: p ≤ 200 and gaps above 100%;
>   - Sahinidis's 500 s and 10⁻⁶, and the note lines quoted from him.
> - **Sign-off citations:** the two that v2 newly covers match their cards (Burer's c01 pp. 15–16; s2-17 p. 29 and s2-18 pp. 37 and 40).
>
> Problems: four, listed separately.
> - One set of numbers rests on paper text, not on the cited card: Dey's '6 s' and the LMI's extra instance. The lead's cost order (concession and gate) rests on the same figure.
> - Two marks can be narrowed or lifted:
>   - Glasso and MB are on CRAN.
>   - All 20 of Conn's CUTE problems are in CUTEst, with BARD at n = 3 and PFIT1LS bound-constrained.
>
> Notes for the moderator (design choices, not problems):
> - **'Pure defaults' as a labelled second run gives unequal time limits.** BARON's MaxTime default is 500 s, while SCIP's limits/time default is 1e+20. Defaults also depend on the interface: under GAMS, BARON takes EpsR from OptCR, and MaxTime overrides ResLim. GAMS's BARON page (for BARON 24.9.12) states EpsR against |U|. The plan's rule of recomputing gaps from logged bounds covers the gap formula but not the time limit.
> - **Q23's CPLEX release can be named.** S708's duel ran CPLEX 22.1.2 [S708 p. 35], and IBM lists that release.
> - **Outside this lens:** the lead's v2 sign-off cites [02 P7] for keeping item 2 open. In his note 02, P7 is the rule to 'agree PhD topics by mutual convincing'.

**Fidelity to the record** (181 items checked):

> I checked 181 items for how faithfully plan v2 follows the record; no repository file was changed. v2 is mostly faithful. There are 13 problems, none high: 4 medium, 1 low-medium and 8 low.
>
> **What I checked**
> - **Method.** I copied the challengers' round, v2, the changes list, the dissent responses and the v2 sign-offs from the task text into scratch files, by hand. I compared v1 (transcript lines 452–608) with v2 word by word, and mapped every quotation in v2 to the turns that contain it.
> - **(1) Changes list.** All 45 entries trace to a turn, a v1 dissent or a first-verifier problem. All 49 changed v1 lines and 82 new or changed v2 lines map to entries. Two exceptions:
>   - The moderator's v2 note and the 'Kept' paragraph are not listed.
>   - The 'Item 3 bounds' entry rests on a quote to Conn about a different point, so the rim concession still traces to no lead turn.
> - **(2) Quotations.** v2 has 105 distinct quotations outside the reproduced FL1/FL2/FL4/FL5 tests: 58 new, 47 kept from v1. All are verbatim in the record except "Resolved in (V1)". Each new one sits in the named speaker's turn, or in the lead's turn where unattributed. Changing inner double quotes to single ones, and Burer's “ ” to ' ', is normal nesting, not a change.
> - **(3) v1 dissents.** There are six responses: Gould, Nocedal, Wright, Audet, Sahinidis and Burer. All are accepted and all appear in the plan text.
> - **(4) Challenger objections.** Every contest from the challengers' rejoinders appears in v2. Conn's is carried as unresolved; Sahinidis's (item 1 and three on item 2) and Dey's are accepted.
> - **(5) v1 text kept.** 81 v2 lines are v1 word for word, and the FL test block is unchanged. Annotations are kept, except the five removals the changes list names.
> - **(6) Sign-offs.** Each of the 11 sign-offs makes true claims about v2.
> - **Cards.** The moderator's 'Both match their cards' holds:
>   - Burer's [S014 preprint pp. 15–16] on card c01: 0.2% and 0.02% levels.
>   - The lead's [S377 p. 29] on card s2-17: the exact MIO reformulation is fastest on most polyhedral instances.
>   - The lead's [S708 pp. 37, 40] on card s2-18: the exact MIP wins at p. 37; CPLEX wins on QCQPs 1, 2 and 5 at p. 40.
>   - Also confirmed: Dey's S014 p. 22 on card c04 (BARON 6 h against 1 h, with the reason); S129 pp. 20, 23 on card c17; S090 pp. 5–6, 12 and 15 on card c2-02; Conn's S066 pp. 16–19 on card c2-05.
>
> **Main findings**
> - **Rim concession.** The first verifier's annotation was removed on the strength of a quote that withdraws the Lipschitz charge against the bilevel rule. No lead turn mentions the rim.
> - **Dey's agreement.** The quote after "agrees on the stop" is his evidence boundary, not his agreement. His actual agreement is scoped to his own set, and he says his verdict is silent at n ≥ 20.
> - **Switch rule 1.** It applies Gould's node-count gate to the best-bound rebuild too. Gould's v2 ✅ holds only if the gate binds the printed rebuild alone.
> - **'The lead accepts every rejoinder addition except Huangfu's'.** This is false: (V1) leaves out the first clause of Nocedal's reading 3, as the moderator's own v2 note says.
> - **Sahinidis's condition.** His v1 clause "outside the RPT papers' own test families" was dropped. His v2 ✅ is conditional on an edit v2 lacks.
>
> **Suggested tally**
> - Six ✅: Bertsimas, Huangfu, Gould*, Vicente, Sahinidis*, Burer.
> - Five ⚠️: Nocedal, Wright, Audet, Conn, Dey.
> - \* marks a sign-off whose 'holds if' condition v2 does not meet.
>
> v2's lines saying Nocedal and Wright have had no turn on (V1) are now out of date: both answered it, as dissents, in their sign-offs.
>
> **Files** (in a local scratch folder, v2-fidelity; path omitted here)
> - v1.md
> - v2.md
> - challengers.md
> - signoffs_v2.md
> - check_quotes.py
> - attrib.py

#### Problems found (27)

Numbered across the three lenses: card citations (1–10), named things and numbers (11–14), fidelity to the record (15–27). Three pairs concern the same claim (1 and 11, 2 and 12, 9 and 26), so 24 distinct problems; each is annotated once at every place it applies.

1. **Dey lens (challenger): challengers' round, item 4, Dey's turn, POSITION (1)** · card citations
   - Claim: The LMI lifted RLT from 924 to 941 exact for 6 s more; the products reached 959–960 at 121–129 s, and with them, the LMI added one instance [S129 p. 20].
   - Problem: Card c17 (S129, read in full) has 924, 941, 959–960 and about 121–129 s. It gives no time for PRS (RLT+LMI), so the card cannot carry '6 s more'. It also does not say which RPT arm reached 960, so it cannot carry 'the LMI added one instance'. Without those two facts the card does not show the claimed order (the LMI cheaper than the products). The paper text does: arXiv:2510.16595v1 p. 20 says PRS is 'only taking 6 seconds longer than the PR relaxation', and gives PRV 959 at 121.177 s and PRSV 960 at 129.492 s. The source supports the claim; the card does not.
   - Fix proposed: Add to card c17, D5: 'PRS 941 exact, 6 s longer than PR; PRV 959 at 121.177 s, PRSV (with the LMI) 960 at 129.492 s (p. 20)'. Or cite it as [S129 p. 20, paper text].
   - Applied here: Annotated in Dey's opening, POSITION (1). Card c17 is left as it is, since only this transcript is edited.
2. **Bertsimas lens (lead): challengers' round, item 4, the lead's answer: POSITION, concession (1), and FIRST EXPERIMENT amendment (1), the gate; the concession is also quoted in plan v2 part 4 (Reformulation ideas)** · card citations
   - Claim: my fix presumed structure-chosen products cheaper than the LMI; on his set they cost more [santanu-s-dey card S129 pp. 20, 23]: now an arm. / It must reproduce his order, RLT+LMI cheaper than the products [santanu-s-dey card S129 pp. 19–21]
   - Problem: The card shows the RPT products at 121–129 s (p. 20), costing more than BARON at n = 10 (p. 23), and PRS dominating the minor-based rungs (p. 21). It gives no time for PRS (RLT+LMI). So the comparison the gate must reproduce, products more expensive than the LMI, is not on the card. It is in the paper text, p. 20 (checked): PRS is 6 s slower than PR, about 44 s cumulative, against 121.177–129.492 s for the RPT arms. This is the same gap as in Dey's turn, here carrying the concession and the gate.
   - Fix proposed: Make the same card c17 addition, or cite [santanu-s-dey card S129 pp. 20, 23; arXiv:2510.16595v1 p. 20, paper text] for the order.
   - Applied here: Annotated at the concession and at the gate in the lead's item 4 answer, and after the quoted concession in plan v2 part 4.
3. **Bertsimas lens (lead): challengers' round, item 2, the lead's answer, RISK (3)** · card citations
   - Claim: (3) The stage concession leans on the critics' records [nikolaos-v-sahinidis note 05 §A8, row 8e]; BPV's rejoinder is unread here [05 §1.3].
   - Problem: The claim is true only of the lead's own note 05 §1.3. The guest note he cites in the same sentence records both rejoinders as read (row 8d: 'Two rejoinders, both read'). It also quotes BPV's rejoinder, which 'acknowledged SSS without addressing the timing point' (row 8e). The lead's own domain file says the same: ML §6.1, point 1: 'the rejoinders are read only in nikolaos-v-sahinidis note 05 §A8'. So the risk points to a gap in the evidence that the council does not have, and it leaves out what the rejoinder shows: BPV's rejoinder did not answer the timing point.
   - Fix proposed: Write: 'BPV's rejoinder is unread in my notes [05 §1.3]; Sahinidis's note reads it: it acknowledged SSS without addressing the timing point [nikolaos-v-sahinidis note 05 §A8, rows 8d–8e].'
   - Applied here: Annotated in the lead's item 2 answer, RISK (3).
4. **Sahinidis lens (challenger): challengers' round, item 1, Sahinidis's turn, WHY (last sentence)** · card citations
   - Claim: (→ Workflow D stop rule; [02 X4]) A development-set claim needs a hold-out.
   - Problem: Note 02 X4 is 'Report per library, so that no single collection drives the conclusion'; it says nothing about hold-outs. The hold-out rule is note 02 X2 (tested 'against an additional collection of problems that had not been seen by developers'), and his SKILL.md Workflow D stop rule also supports the claim. His item 2 turn cites the pair correctly, as [02 X2, X4].
   - Fix proposed: Cite [02 X2] and keep the Workflow D reference.
   - Applied here: Annotated in Sahinidis's item 1 opening, WHY.
5. **First verifier's annotation, carried unchanged into plan v2: plan v2, item 4, 'From delegates' risk lines', Burer's quoted risk line** · card citations
   - Claim: Burer: "At 10⁻⁴, splitting's slow tail [S014 preprint pp. 2, 17] may lose for solver reasons; report a looser gap." *(citation not confirmed: S014 is a projected-gradient code, not a splitting method; its card supports p. 2 (slow limiting convergence of first-order methods) and p. 20 (their moderate-accuracy niche), not p. 17; the transfer to splitting is inferred)*
   - Problem: The 'not p. 17' part of the annotation is wrong. Burer's card c01 (S014, read in full), D5, says: 'Losses are printed: iterations grow "drastically" from 0.2% to 0.02%, especially with negative weights (p. 17)'. That is the slow-tail evidence for this first-order code, on p. 17. Only the transfer from a projected-gradient code to splitting is unsupported.
   - Fix proposed: Narrow the annotation to the transfer: S014's card shows the slow tail at pp. 2 and 17 for a first-order projected-gradient code, and carrying it to splitting is inferred. Use the same wording at the other places where this annotation was applied, Burer's item 4 opening and rejoinder.
   - Applied here: The narrowed annotation is added after the first verifier's in plan v2, item 4; nothing is deleted. Burer's item 4 opening and rejoinder and plan v1 keep the first verifier's annotation alone, since those lines predate this round and are kept unchanged.
6. **Sahinidis lens (challenger): challengers' round, item 1, Sahinidis's rejoinder, FIRST EXPERIMENT (v′)** · card citations
   - Claim: It works on one frozen file, with X standardized as in S010 and y centred [dimitris-bertsimas card S010 p. 2].
   - Problem: Card c16 at p. 2 covers only X: columns standardized to zero mean and unit ℓ2 norm. It says nothing about y, as the lead's own risk line notes ('The card gives standardized columns, not how y was treated'). In the paper text (p. 26) the response is standardized only for the real data, Diabetes and Leukemia. The synthetic examples use y = Xβ0 + ε, uncentred. Placed at the end of the sentence, the citation makes centring y look like S010's practice; it is a design choice.
   - Fix proposed: Write: 'with X standardized as in S010 [dimitris-bertsimas card S010 p. 2] and y centred (a design choice; S010 standardizes the response only for its real data, paper text p. 26)'.
   - Applied here: Annotated in Sahinidis's item 1 rejoinder, (v′).
7. **Sahinidis lens (challenger): challengers' round, item 1, Sahinidis's turn, RISK** · card citations
   - Claim: Its progress claims are oral (ASR), on an unnamed set, with figures that differ between talks [02 C5; 03 §B1].
   - Problem: Note 02 C5 sets two sources against each other. One is a 2021 press article (S42: 'about 5-10%' to 'about two-thirds'). The other is a 2025 lecture (S41, caption-derived: 'one in three' to 'almost the entire collection'). Note 03 §B1 has only the 2025 lecture. Only one of the two figures comes from a talk, so 'differ between talks' and 'oral (ASR)' overstate. The point itself, an unnamed set and figures that disagree, holds.
   - Fix proposed: Write: 'Its progress claims come from a 2021 press quote and a 2025 lecture (ASR), on an unnamed set, with figures that differ [02 C5; 03 §B1].'
   - Applied here: Annotated in Sahinidis's item 1 opening, RISK.
8. **Conn lens (challenger): challengers' round, item 3, Conn's turn, WHY (first paragraph)** · card citations
   - Claim: My side's paper has the same weakness, disclosed as a first contribution [S066 p. 19], so it backs neither inner rule.
   - Problem: On card c2-05, p. 19 is where the paper discloses that it has no baselines ('such methods appear not to exist'). The paper calls itself 'a first contribution' on p. 18 (card D6 and D7; Vicente's card S047, D8, also gives p. 18). The page is half right.
   - Fix proposed: Cite [S066 pp. 18–19].
   - Applied here: Annotated in Conn's item 3 opening, WHY.
9. **Bertsimas lens (lead): v2 sign-offs, the lead's sign-off** · card citations
   - Claim: Accepted: item 2 unresolved until Nocedal and Wright answer (V1) [02 P7]
   - Problem: Note 02 P7 is 'Agree PhD topics by mutual convincing, and keep them separate from funding' (2014 oral history, S47). It is about negotiating thesis topics with students. Using it to keep a council item open until two delegates answer is a transfer the sign-off does not label; the note says nothing about disputes among peers or about open items.
   - Fix proposed: Label it '(inferred from 02 P7)', or cite the convener rule (SKILL.md Activation Rules, 'As convener'). Note 02 O5 ('the best idea wins, whoever had it') is a closer stated value.
   - Applied here: Annotated in the lead's v2 sign-off; problem 26 concerns the same citation and shares this annotation.
10. **Council roundtable FL2 text (reproduced verbatim in plan v2): plan v2, part 3, details block, FL2 deciding test; the source is council-roundtable/SKILL.md, fault line 2 (line 336)** · card citations
    - Claim: run the papers' own ℓ1 opponents (glmnet, Glasso) and QUIC *(unverified)* at tolerances 10⁻², 10⁻⁴ and 10⁻⁶ [jorge-nocedal card S043 p. 7]
    - Problem: Nocedal's card c3-01 (S043, read in full) shows one common stop at p. 7: ‖∇̃F(P)‖∞ ≤ 10⁻⁶, with ALM's test changed to ℓ∞ ABSTOL = 10⁻⁶ 'to match the stopping criteria of the other algorithms'. That supports aligned stopping tests and the 10⁻⁶ level. It does not support the three-level ladder, which is the test's own design.
    - Fix proposed: In council-roundtable/SKILL.md Step 3 and in this reproduction, cite S043 p. 7 for the aligned 10⁻⁶ stop only, and mark the 10⁻² and 10⁻⁴ levels as the test's design.
    - Applied here: Annotated in plan v2's reproduction of the FL2 test. The roundtable's SKILL.md and plan v1's copy are left as they were, since this edit touches only the new material of this transcript.
11. **Dey lens (challenger): challengers' round, item 4, Dey's turn, POSITION (1)** · named things and numbers
    - Claim: The LMI lifted RLT from 924 to 941 exact for 6 s more; the products reached 959–960 at 121–129 s, and with them, the LMI added one instance [S129 p. 20].
    - Problem: Card c17 (S129) has 924 and 941 exact, 959–960 at about 121–129 s, and RLT's 'about 4 s more'. It gives no time for PRS (RLT plus the LMI), and it does not say which of 959 and 960 belongs to the relaxation with the LMI. Both figures are in the paper. arXiv:2510.16595v1 p. 20 (fetched and read) says PRS takes 'only ... 6 seconds longer than the PR relaxation', and lists PRV and PRSV at 959 and 960 exact, in 121.177 s and 129.492 s. The numbers are right at source level, but the cited card does not carry them.
    - Fix proposed: Add to card c17 that PRS takes 6 s more than PR, and the PRV/PRSV split (959 vs 960 exact; 121.177 s vs 129.492 s). Otherwise cite [S129 p. 20, paper text].
    - Applied here: Same claim as problem 1; one annotation there, in problem 1's wording, which states both figures.
12. **Bertsimas lens (lead): challengers' round, item 4, answer to Dey: POSITION concession (1) and FIRST EXPERIMENT amendment (1), the gate. The concession is quoted in plan part 4 (structure-chosen products), and switch rule 4 rests on the gate.** · named things and numbers
    - Claim: my fix presumed structure-chosen products cheaper than the LMI; on his set they cost more [santanu-s-dey card S129 pp. 20, 23] / It must reproduce his order, RLT+LMI cheaper than the products [santanu-s-dey card S129 pp. 19–21]
    - Problem: The cost order needs the time for RLT+LMI (PRS), which card c17 does not give. The card gives P at 34.429 s and RLT at about 4 s more, the RPT relaxations at about 121–129 s, and says RPT costs more than BARON at n = 10 (p. 23). The order does hold in the paper text: arXiv v1 p. 20 puts PRS 6 s above PR, about 44 s against 121–129 s for PRV and PRSV. It is not on the card cited.
    - Fix proposed: Make the same addition to card c17 as for Dey's turn, or cite [S129 p. 20, paper text] for the cost order. This covers the concession, the gate and the plan's quote.
    - Applied here: Same claims as problem 2, annotated there once per place. Switch rule 4 cites no card, so it carries no annotation.
13. **Sahinidis lens (challenger): challengers' round, item 2, FIRST EXPERIMENT (a); carried into plan item 2 as 'plus Sahinidis's (a)'** · named things and numbers
    - Claim: and Glasso, MB and QUIC (unverified) on S288's designs
    - Problem: The mark covers more than the gap. Glasso is glasso 1.11 (CRAN, 2019-10-01), and MB is method = "mb", the default, in huge 2.0.1 (CRAN, 2026-08-04); both were checked. Only QUIC lacks a current build: the CRAN archive ends at QUIC 1.1.1 (2020-07-20), and the package was removed on 2020-08-03. S288's card names MB and Glasso as rivals (p. 17) but not their implementations.
    - Fix proposed: Write: 'Glasso (glasso 1.11) and MB (huge 2.0.1, method "mb") (CRAN, checked), and QUIC (unverified)'. Name the MB implementation in plan item 2.
    - Applied here: Annotated in Sahinidis's item 2 opening, (a): the verifier's annotation, "(unverified), after QUIC only", is written out with the two packages it clears. Plan item 2 names no implementation for (a), so it carries no annotation.
14. **Conn lens (challenger): challengers' round, item 3, FIRST EXPERIMENT (c); plan item 3, Problem line (Conn's frozen tier (c))** · named things and numbers
    - Claim: taken from CUTEst where they survive (SNAIL, HAIRY and CLIFF checked; the rest unverified)
    - Problem: The rest can now be checked. Conn and Toint's Report 95/6 (perso.unamur.be/~phtoint/pubs/TR95-06.ps, the version card S019 reads) lists the 20 problems in Table 1: AKIVA, BARD, BEALE, BOX3, BRKMCC, BROWNDEN, CLIFF, CRAGGLVY, CUBE, DENSCHNA, GULF, HAIRY, HATFLDE, HELIX, KOWOSB, PFIT1LS, ROSENBR, SCHMVETT, SISSER and SNAIL. All 20 SIF files are in the CUTEst collection (bitbucket.org/optrove/sif), checked. There are two caveats. CUTEst's BARD has 3 variables, while the table prints n = 2. PFIT1LS has a lower bound on one variable (classification SBR2), so its robust counterpart is not unconstrained, unlike the rest of an FL4-style tier. CRAGGLVY and SCHMVETT are variable-size problems whose SIF 'original values' give the table's n = 4 and n = 3.
    - Fix proposed: Replace the mark with 'all 20 in CUTEst (checked)'. Run BARD at n = 3, and keep PFIT1LS apart from the unconstrained tier or drop it.
    - Applied here: The verifier's annotation, "none needed: lift 'the rest unverified'; flag PFIT1LS as bound-constrained", is applied with its reason after Conn's own mark, which stays verbatim: in Conn's (c), in plan item 3's Problem line and in the matching line of What was argued.
15. **Lead (plan v2 text, item 3), as changed at the moderator's check: plan v2, part 1, item 3, Bounds line (change-list entry 'Item 3 bounds')** · fidelity
    - Claim: The lead concedes in this plan that his Δx bracket fails at the rim; his answer to Conn: "A missing modulus voids my bracket, not their rule".
    - Problem: [Medium] The first verifier's annotation (problem 4: the rim concession is in no lead turn) was removed. The change list gives the lead's item 3 answer as the basis. But no lead turn mentions the rim: not the reply, not the challengers'-round answer, not the v1 or v2 sign-off (searched). The quoted words are concession (2) to Conn. They answer Conn's point that 'the modulus a simulator lacks voids a bracket, not the rule' and withdraw the lead's charge that the bilevel rule's tolerances need a Lipschitz constant ('charge withdrawn'). They are not about the closed-form Example III bracket at the rim of the joint ball. Reading them as a rim concession is an inference, so the concession still traces only to the plan.
    - Fix proposed: Keep the concession annotated, or put the quote on its own line ('The lead to Conn, withdrawing his Lipschitz charge: …'). Or record the rim concession verbatim in the lead's sign-off. Correct the change-list source for 'Item 3 bounds'.
    - Applied here: Annotated in plan v2 item 3 (Bounds) and after the source of change 25.
16. **Lead (switch rule 1; his response to Gould: 'switch rule 1 gates both rebuilds'); Gould's v2 sign-off: plan v2, part 2, switch rule 1; the lead's responses (Gould); v2 sign-offs (Gould)** · fidelity
    - Claim: The rebuild, as printed or best-bound (Gould's v1 dissent), fails its gate (Gould's node-count reproduction, Huangfu's proved cells) → "less scalable" stays unmeasured.
    - Problem: [Medium] Gould's node-count gate (his item 1 rejoinder, (1)) applies to the S040 rebuild as printed. His v1 dissent asked only that the best-bound rebuild be added. v2 extends 'Gould's node-count reproduction' to the best-bound arm. Gould's v2 sign-off says 'that gate binds only the printed rebuild' and is marked ✅ only 'if backup rule 1's node-count gate binds only the printed rebuild'. v2 does not meet that condition, so his ✅ cannot be counted as unconditional.
    - Fix proposed: Rule 1: 'The printed rebuild fails its gate (Gould's node-count reproduction, Huangfu's proved cells) → "less scalable" stays unmeasured; the best-bound arm is that reproduced code with node selection alone changed.' Otherwise tally Gould's sign-off as conditional and quote its holds-if.
    - Applied here: Annotated in switch rule 1 and in the lead's response to Gould; the v2 tally counts Gould's sign-off as conditional.
17. **Moderator (plan v2, item 4 header, 'evidence boundaries … beside their agreement'): plan v2, part 1, item 4 header** · fidelity
    - Claim: Dey (challenger) agrees on the stop: "Integer arms, BARON internals: outside my evidence."
    - Problem: [Medium] The words after the colon are Dey's evidence boundary, not his agreement, yet they read as what he agreed to. His agreement is scoped: 'Agreed on the stop: on my set, product rungs stop paying as n grows'. His turn also says his higher-dimension verdict 'is silent at n ≥ 20', which is the item's range. An unscoped 'agrees on the stop' overstates his support. Item 3 handles Conn correctly, quoting the agreement and then 'He adds: …' for the boundary.
    - Fix proposed: Dey (challenger) agrees on the stop for his set: "on my set, product rungs stop paying as n grows"; his verdict "is silent at n ≥ 20". He adds: "Integer arms, BARON internals: outside my evidence."
    - Applied here: Annotated in plan v2's item 4 header.
18. **Lead (part 3, v1 sentence kept word for word): plan v2, part 3 (Minimal experiment), second paragraph** · fidelity
    - Claim: The lead accepts every rejoinder addition except Huangfu's context-only rule, which stays unresolved (item 1).
    - Problem: [Medium-low] This is false of v2. Nocedal's item 2 rejoinder adds 'Reading 3: tighten the stop to the winning support's arrival gap; certify only at a closed gap', and part 3 includes every DECIDING TEST field verbatim. Item 2's Reading, however, is the lead's (V1)–(V2). The moderator's own v2 note says (V1) 'leaves out the first clause of Nocedal's reading 3'. Item 2 stays unresolved, and Nocedal's v2 dissent asks for exactly that clause. So a second rejoinder addition is neither accepted nor listed as an exception.
    - Fix proposed: '…except Huangfu's context-only rule (item 1) and the first clause of Nocedal's reading 3, "tighten the stop to the winning support's arrival gap" (item 2), both unresolved.'
    - Applied here: Annotated in plan v2 part 3.
19. **Lead (switch rule 4; response to Sahinidis); Sahinidis's v2 sign-off: plan v2, part 2, switch rule 4; v2 sign-offs (Sahinidis)** · fidelity
    - Claim: A heavier rung stays a default only where it dominates every cheaper arm in the fixed column, on the headroom band and two libraries, one QPLIB or MINLPLib (Sahinidis's v1 dissent).
    - Problem: [Low-medium] Sahinidis's v1 condition reads 'QPLIB or MINLPLib, outside the RPT papers' own test families'. v2 drops the clause. His v2 ✅ then holds only if 'any QPLIB or MINLPLib instance that an RPT paper ran (for example their ten QCQPs, whose source no card names) is scored as a development set, not as hold-out'. v2 states no such rule, so his ✅ is conditional on an edit v2 lacks.
    - Fix proposed: Add to switch rule 4: '(instances an RPT paper ran, e.g. S624's ten QCQPs, count as development, not hold-out)'. Otherwise tally his sign-off as conditional and quote its holds-if.
    - Applied here: Annotated in switch rule 4; the v2 tally counts Sahinidis's sign-off as conditional.
20. **Lead (item 4, v1 wording kept after an accepted change): plan v2, part 1, item 4, Incumbents line** · fidelity
    - Claim: Incumbents: BARON 26.9.10 (release notes: 2026.9.10) and SCIP 10.1.0 at defaults (checked)
    - Problem: [Low] This wording is stale. v2's own ledger line now runs 'one gap of 10⁻⁴ for every solver with defaults as a labelled second run' (Dey's (d), accepted). The lead's amendment (4) says 'pure defaults run as a labelled second run', and Dey's (d) notes that BARON's EpsR default is 10⁻⁶ and SCIP's limits/gap default is 0. So the main runs are no longer at defaults.
    - Fix proposed: '…and SCIP 10.1.0 (checked), at one gap of 10⁻⁴, with pure defaults as a labelled second run (Dey's (d))'.
    - Applied here: Annotated in plan v2 item 4 (Incumbents).
21. **Moderator / lead (item 2 unresolved line; moderator's v2 note and Kept paragraph): plan v2, item 2 'Unresolved, narrowed by the lead's (V1)'; also 'no delegate has yet seen the changes in v2'** · fidelity
    - Claim: Nocedal and Wright have had no turn on (V1).
    - Problem: [Low] This was true when v2 was drafted, but both have now answered (V1) in their v2 sign-offs, both as dissents. Nocedal wants certification only where arrival gaps are ≤ 10⁻⁴; Wright wants each stop and twin tuned by its own validation. 'No delegate has yet seen the changes in v2' is outdated in the same way. Assembled as is, the plan contradicts the sign-offs printed below it.
    - Fix proposed: Date both lines ('before the v2 sign-offs') and add: 'Both answered (V1) at sign-off, with dissents.'
    - Applied here: Annotated at every place the new material makes either claim: plan v2 item 2, the moderator's v2 note and its Kept paragraph (in the plan and again after the lists), change 20, the response to Wright, and the matching line of What was argued.
22. **Moderator (part 6 Q19; part 5, item 2): plan v2, part 6, question 19; part 5, item 2 line** · fidelity
    - Claim: 19. Items 1–2: "Will you pick and freeze the hold-out designs yourself, before any run?" (Sahinidis).
    - Problem: [Low] Sahinidis asked this only on item 1, in the QUESTION FOR USER of his item 1 rejoinder. On item 2 he set a rule ('a hold-out unused by S095, S288, HTT or my group') and asked the user only about the model's use. Part 5's 'Item 2: … a hold-out (Sahinidis)' therefore also credits him with a question he did not ask.
    - Fix proposed: Label Q19 'Item 1'. Add: 'Item 2's hold-out, under Sahinidis's rule, is also left to the user (the plan's extension)'. In part 5, write 'a hold-out (under Sahinidis's rule)'.
    - Applied here: Annotated at question 19 and at part 5's item 2 line.
23. **Moderator (neutrality note v2): moderator's neutrality note (v2), first bullet; change-list entry for item 2** · fidelity
    - Claim: Item 2: "Resolved in (V1)" is back to unresolved, now narrowed by (V1).
    - Problem: [Low] The quoted words are in no turn, response or sign-off. They come from the lead's pre-check draft of v2, which the record does not reproduce. This is the same kind of untraceable quotation as v1's 'perhaps in S061's band' (first verifier, problem 4). It is the only one of the 105 distinct quotations in v2 not found in the record.
    - Fix proposed: Drop the quotation marks ('the lead's draft had marked item 2 resolved by (V1); it is back to unresolved'), or reproduce the draft line in the record.
    - Applied here: Annotated in both copies of the moderator's v2 note and in change 20.
24. **Moderator (changes from v1): changes list (no entry); plan v2 'Moderator's neutrality note (v2)' block and 'Kept:' paragraph** · fidelity
    - Claim: **Moderator's neutrality note (v2).** Changed, each from the record: … Kept: every v1 line the lead did not change is word for word, annotations included.
    - Problem: [Low] Both blocks are new in v2 but have no entry in the changes list. Every other difference has one: all 49 changed v1 lines and all 82 new or changed v2 lines map to listed entries.
    - Fix proposed: Add an entry: 'Moderator's neutrality note (v2) and the Kept paragraph added (source: the moderator's check of v2)'.
    - Applied here: Annotated once, after the note's title in plan v2, covering the Kept paragraph too; the changes list stays as given.
25. **Lead / moderator (v2 header): plan v2, italic header note** · fidelity
    - Claim: *Revision v2, after the challengers' round. Drafted by the Bertsimas lens (lead); v1 was checked by the moderator for neutrality.
    - Problem: [Low] v2 was checked by the moderator too. It carries a 'Moderator's neutrality note (v2)', and many change-list entries were made 'at the moderator's check'. The header records only the check of v1.
    - Fix proposed: '…Drafted by the Bertsimas lens (lead); v1 and v2 were checked by the moderator for neutrality (see the notes below).'
    - Applied here: Annotated inside the italic header, without asterisks of its own, as the first verification did in the plan's footnote.
26. **Bertsimas lens (v2 sign-off): v2 sign-offs, Bertsimas** · fidelity
    - Claim: Accepted: item 2 unresolved until Nocedal and Wright answer (V1) [02 P7]
    - Problem: [Low] What this says about v2 is true. The citation is not: the lead's note 02 item P7 is 'Agree PhD topics by mutual convincing, and keep them separate from funding' (2014 oral history), not a council or sign-off rule. Applying it here is an unlabelled transfer.
    - Fix proposed: Label the transfer '(inferred)', or cite the convener rule instead.
    - Applied here: Same citation as problem 9; one annotation there.
27. **Moderator (restored caveats, parity): plan v2, item 2 Settings; also item 3 tier (c) and the claim-ledger Conn line** · fidelity
    - Claim: "closed: ε = 10⁻⁴" (Sahinidis)
    - Problem: [Low] Parity omission. The moderator restored Sahinidis's own caveat on the adopted 10⁻⁶ (item 1) but not his caveat on the adopted 10⁻⁴: his item 2 rejoinder's risk line reads '10⁻⁴ may rarely close'. Conn's caveat on his adopted public tier is also missing beside the 'wins' rule that depends on it: 'the choice of radius can favour one inner rule, and freezing it in advance limits that bias but does not remove it'.
    - Fix proposed: Quote both caveats beside the rules they qualify, as item 1 does for 10⁻⁶.
    - Applied here: Annotated in plan v2 item 2 (Settings), and, with Conn's caveat, at the claim-ledger Conn line.

#### Unverified items (17)

1. Card citations: ncvreg 3.16.0 on CRAN (Sahinidis's arm (a), adopted in v2 item 2): outside the card-citation lens and not checked here; the first verifier confirmed glmnet 5.2 and L0Learn 2.1.0 only. *Confirmed by the named-things lens (CRAN, with MCP and SCAD); no mark.*
2. Card citations: BARON 26.9.10 defaults (MaxTime 500 s; EpsR 1e-6 relative to max(|L|,|U|)) and SCIP 10.1.0 (limits/gap 0 relative to min(|primal|,|dual|)), plus Dey's 'SCIP's is not' finite across sign changes: vendor documents, not checked by this lens. *Confirmed by the named-things lens (BARON manual v. 2026.9.10; SCIP 10.1.0, whose gap is 'Infinity' when the signs differ); no mark.*
3. Card citations: CUTEst availability of Conn's 20 small CUTE problems beyond SNAIL, HAIRY and CLIFF: Conn marks the rest unverified himself; not checked here. *Checked by the named-things lens (problem 14) and annotated there.*
4. Card citations: Whether HTT's Σ and β differ from S095's (Sahinidis's item 2 rejoinder, risk line): on no file in the repository. *Already hedged in the turn ("may differ", "on no file I read"); no mark.*
5. Named things: QUIC has no current build: the CRAN archive ends at 1.1.1 (2020-07-20) and the package was removed on 2020-08-03. The mark should now cover QUIC only. *Marked in plan v2 item 2 (its current build); Sahinidis's (a) annotated (problem 13).*
6. Named things: Whether S010's 'p ≤ 30' comes from leaps()'s 31-column default cap. S010 names no leaps release. leaps 2.9, current on CRAN from 2009 to 2017, had the same cap, so the link is plausible but still inferred. *Labelled inferred in the turns themselves (Sahinidis's risk line; the lead's "inferred link"); no mark.*
7. Named things: Conn's tier (c) robust counterparts (radius, Γ grid, and which problems give a modulus for a bracket) are his own construction and cannot be checked until built. Only the 20 problem files were verified. The 20 names come from Report 95/6; the table in the 1996 published chapter was not seen. *Labelled in Conn's (c) as an inferred construction; no mark.*
8. Named things: Which interface will run BARON (native, GAMS, Pyomo or JuMP). Its 'defaults' differ by interface (time limit and EpsR source), so the 'pure defaults' second run cannot be checked until the interface is named. *Marked in plan v2 item 4 (two ledgers).*
9. Named things: The MIO solver and its oldest runnable releases, the MOSEK release, and whether BARON 20.10.16 and 21.1.13 still license and run (carried from the first verification). *Already marked in plan v2 items 1, 2 and 4, as in v1.*
10. Named things: The 100-variable EM simulator and its error data, the Dutch dike-ring data, and the integer sequel's code (carried from the first verification). *Already marked in plan v2 items 3 and 4 and question 14.*
11. Named things: Whether Gurobi is the MIO solver. Sahinidis's WorkLimit stops and the lead's per-family calibration depend on it. *Covered by the existing mark on the MIO release in plan v2 item 2, and stated as a condition in Sahinidis's (c) ("if Gurobi is the solver"); no new mark.*
12. Named things: Whether HTT's Σ and β match S095's: on no file read (Sahinidis's own caveat); not checked. *Same as item 4; no mark.*
13. Fidelity: The lead's pre-check draft of v2 is not in the record. This covers "Resolved in (V1)", the bare 'agrees', 'ledger (1) runs (a)-(d)' and every '(moderator's check)' provenance note in the changes list, none of which could be checked against a source. *Annotated where the draft is quoted ("Resolved in (V1)", problem 23); the provenance notes are the moderator's own record and carry no mark.*
14. Fidelity: 'Rechecked for v2: CRAN, Gurobi, BARON and SCIP documentation' in the footnote: the lead's rechecks were not re-run here. *The named-things lens checked those documents (the CRAN packages, Gurobi's WorkLimit, the BARON manual, SCIP's parameters); no mark.*
15. Fidelity: QUIC 1.1.1 in the CRAN archive (v2 item 2): taken from the first verifier's finding, not re-fetched. *Confirmed by the named-things lens; no mark.*
16. Fidelity: Citations in the challengers' round and the v2 sign-offs, other than the eight checked, were not opened. They fall outside this lens: Audet's [S128 pp. 5, 15]; Nocedal's [S013 pp. 10–12]; Sahinidis's [dimitris-bertsimas card S624 p. 10] and [dimitris-bertsimas card S095 p. 5] (the ε = 10⁻⁴ adopted in v2); Burer's [S020 pp. 12, 16] and [S049 arXiv p. 10]; Gould's [dimitris-bertsimas card S040 pp. 10, 17–21]; Dey's [S119 p. 13] and [S123 p. 7]. *Within the card-citation lens's 287 instances, which raised no problem with them; no mark.*
17. Fidelity: The verbatim and diff checks rest on my hand transcription of the task text (challengers' round, v2, changes list, responses, sign-offs) into scratch files. v1 was extracted mechanically from the transcript. *A caveat on that lens's method; no mark.*

### Citation census (every card citation of the first run)

Run read-only after the second verification, because the first one checked 40 load-bearing citations of the first run, not all of them.

A script first listed every card citation of the first run and attributed each bare id to the speaker of its turn. It covered the Problem Card and agenda, the four items' turns, plan v1 (its pasted fault-line tests included) and the v1 sign-offs. That gave 271 occurrences: 193 to the lead's cards and 78 to guests' cards (Nocedal 31, Burer 16, Audet 10, Vicente 9, Conn 7, Dey 4, Curtis 1). All 271 resolve to an existing card of the right member, at a read level that allows pages and within the page range (the rules of `scripts/check_citations.py`).

Seventeen auditors then took up to 22 occurrences each, all on one member's cards. They opened every cited card and judged whether it carries the claim. Where the lead's card fell short, they also checked his paper text; the guests' paper texts are not in this checkout. A skeptic per chunk then tried to find support for every flag.

- **Supported:** 236 of 271.
- **Flagged:** 35. The skeptics refuted 2: a quoted Burer line in plan v1 that its auditor had read as the lead's, and Vicente's v1 sign-off bracket, whose share the card carries. That leaves 33: 32 partly supported and 1 contradicted.
  - The contradiction is in the Problem Card's class (2): S095's Table 2 runs the (2,000, 10) design only at SNR 0.05, not at SNR 6 and 1 [S095 p. 11].
  - For 12 of the 33 the paper text supports the claim but the card does not carry it. For 15 the paper does not support the claim as cited. The other 6 were judged on guests' cards alone.
- **Applied:** the 23 new ones are annotated in place as *(citation not confirmed: …)*, and so are their 5 verbatim copies in plan v2 (item 2's Problem line, part 4's structure-chosen products, open question 5). The other 10 repeat the first verification's flags, and its annotations stand.
- **Corrections to the first verification:** three of its card readings were wrong. A *(census correction: …)* note follows each such annotation, and nothing was deleted.
  - Its problem 6: card c22 does describe the stall-count exit ("stop on the duality gap or a stall count (pp. 6–8)").
  - Its problem 7: card c12 does carry S080 p. 6, on the non-robustness of existing Lipschitz-estimation procedures. This affects the three S080 citations in Nocedal's item 3 turns. At the first of them, the measurement itself is still at p. 12.
  - Its problem 8: card c01 does carry S014 p. 17 (iterations grow "drastically" from 0.2% to 0.02%). This affects Burer's item 4 opening, his rejoinder and plan v1's quote of the rejoinder. Only the transfer to splitting stays unsupported, as the second verification found for plan v2 (its problem 5).
- **A recurring pattern:** the lead's turns call "products chosen by structure" his papers' future work [S415 p. 30; S708 p. 42].
  - Those pages name partial or selective multiplications. The 2026 revision's iterative scheme adds the constraints a solution violates, so "by structure" is an inference.
  - The roundtable's FL5 itself says "partial multiplications and selective products", and it calls the link to Dey's rung an inferred reading.
  - The pattern covers six occurrences in three brackets: the lead's item 4 opening and reply, and plan v1's reformulation ideas, which plan v2 keeps.
- **Fixed at the source:** the second verification (its problem 10) and the census both found that FL2's deciding test cites Nocedal's card S043 p. 7 for three tolerances, while that card gives one aligned stop at 10⁻⁶. The roundtable's FL2 text was corrected the same day: the 10⁻², 10⁻⁴, 10⁻⁶ ladder is labelled the test's design, S043 p. 7 is cited for the aligned 10⁻⁶ stop only, and QUIC is named as the CRAN archive's 1.1.1. The FL2 copies in plans v1 and v2 above keep the wording the session used.

## Sources

Card ids are per member: the lead's S040 is Bertsimas–Shioda (2009), Nocedal's S040 is the 2002 wedge paper, and Vicente's S047 and Burer's S047 are different papers too. **✓** marks a DOI, arXiv id or URL that this session's verifier confirmed on 2026-10-31. Entries without ✓ carry no DOI or arXiv link here, because none was re-checked in this session: a carded paper's bibliographic record is on its card, and where the council's [paper list](council-roundtable/SKILL.md#papers-behind-the-documented-disagreements) gives a link, the entry says so.

### Papers on the lead's cards (dimitris-bertsimas)

- **B009** · Bertsimas, D. & Dunn, J. (2019). *Machine Learning under a Modern Optimization Lens*. Dynamic Ideas: the publisher's book page. [Card c5-03](dimitris-bertsimas/references/research/cards/c5-03.md).
- **S269** · Bertsimas, D. & Orlin, J. B. (1994). A technique for speeding up the solution of the Lagrangean dual. *Math. Program.* 63(1–3), 23–45. Link in the council's paper list. [Card c02](dimitris-bertsimas/references/research/cards/c02.md).
- **S019** · Bertsimas, D., Pachamanova, D. & Sim, M. (2004). Robust linear optimization under general norms. *Oper. Res. Lett.* ✓ [doi:10.1016/j.orl.2003.12.007](https://doi.org/10.1016/j.orl.2003.12.007). [Card c07](dimitris-bertsimas/references/research/cards/c07.md).
- **S040** · Bertsimas, D. & Shioda, R. (2009). Algorithm for cardinality-constrained quadratic optimization. *Comput. Optim. Appl.* ✓ [doi:10.1007/s10589-007-9126-9](https://doi.org/10.1007/s10589-007-9126-9). [Card c12](dimitris-bertsimas/references/research/cards/c12.md).
- **S090** · Bertsimas, D., Nohadani, O. & Teo, K. M. (2010). Robust optimization for unconstrained simulation-based problems. *Oper. Res.* 58(1), 161–178. ✓ [doi:10.1287/opre.1090.0715](https://doi.org/10.1287/opre.1090.0715). [Card c2-02](dimitris-bertsimas/references/research/cards/c2-02.md).
- **S116** · Bertsimas, D., Nohadani, O. & Teo, K. M. (2010). Nonconvex robust optimization for problems with constraints. *INFORMS J. Comput.* 22(1), 44–58. ✓ [doi:10.1287/ijoc.1090.0319](https://doi.org/10.1287/ijoc.1090.0319). [Card s07](dimitris-bertsimas/references/research/cards/s07.md).
- **S141** · Bertsimas, D. & Nohadani, O. (2010). Robust optimization with simulated annealing. *J. Global Optim.* 48(2), 323–334. ✓ [doi:10.1007/s10898-009-9496-x](https://doi.org/10.1007/s10898-009-9496-x). [Card s07](dimitris-bertsimas/references/research/cards/s07.md).
- **S010** · Bertsimas, D., King, A. & Mazumder, R. (2016). Best subset selection via a modern optimization lens. *Ann. Statist.* 44(2), 813–852. ✓ [doi:10.1214/15-AOS1388](https://doi.org/10.1214/15-AOS1388), [arXiv:1507.03133](https://arxiv.org/abs/1507.03133) (read as v1). [Card c16](dimitris-bertsimas/references/research/cards/c16.md).
- **S184** · Berk, L. & Bertsimas, D. (2019). Certifiably optimal sparse principal component analysis. *Math. Program. Comput.* [Card s2-09](dimitris-bertsimas/references/research/cards/s2-09.md).
- **S061** · Bertsimas, D. & Van Parys, B. (2020). Sparse high-dimensional regression: exact scalable algorithms and phase transitions. *Ann. Statist.* ✓ [doi:10.1214/18-AOS1804](https://doi.org/10.1214/18-AOS1804), [arXiv:1709.10029](https://arxiv.org/abs/1709.10029) (read as v1). [Card c21](dimitris-bertsimas/references/research/cards/c21.md).
- **S095** · Bertsimas, D., Pauphilet, J. & Van Parys, B. (2020). Sparse regression: scalable algorithms and empirical performance. *Statist. Sci.* 35(4), 555–578. ✓ [doi:10.1214/19-STS701](https://doi.org/10.1214/19-STS701), [arXiv:1902.06547](https://arxiv.org/abs/1902.06547) (read as v2). [Card c22](dimitris-bertsimas/references/research/cards/c22.md).
- **S288** · Bertsimas, D., Lamperski, J. & Pauphilet, J. (2020). Certifiably optimal sparse inverse covariance estimation. *Math. Program.* 184(1–2), 491–530. ✓ [doi:10.1007/s10107-019-01419-7](https://doi.org/10.1007/s10107-019-01419-7). [Card s12](dimitris-bertsimas/references/research/cards/s12.md).
- **S183** · Bertsimas, D., Cory-Wright, R. & Pauphilet, J. (2022). Solving large-scale sparse PCA to certifiable (near) optimality. *J. Mach. Learn. Res.* [Card s2-14](dimitris-bertsimas/references/research/cards/s2-14.md).
- **S377**, **S708** · Bertsimas, D., de Moor, D., den Hertog, D., Koukouvinos, T. & Zhen, J. (2023; revised 2026). A novel algorithm for a broad class of nonconvex optimization problems; the 2026 revision is titled "Reformulation-Perspectification Technique for nonconvex optimization problems". Optimization Online, no DOI; URL in the council's paper list. [Card s2-17](dimitris-bertsimas/references/research/cards/s2-17.md) (2023 version), [card s2-18](dimitris-bertsimas/references/research/cards/s2-18.md) (2026 revision).
- **S415** · Bertsimas, D., de Moor, D., den Hertog, D., Koukouvinos, T. & Zhen, J. (2026). Cone product reformulation for global optimization. *INFORMS J. Comput.* ✓ [doi:10.1287/ijoc.2023.0345](https://doi.org/10.1287/ijoc.2023.0345). Code deposit ✓ [github.com/INFORMSJoC/2023.0345](https://github.com/INFORMSJoC/2023.0345) (Julia, `use_lmi`). [Card c2-08](dimitris-bertsimas/references/research/cards/c2-08.md).
- **S624** · Bertsimas, D., de Moor, D., Koukouvinos, T. & Kriezis, D. (2025). Global nonconvex optimization with integer variables. ✓ [arXiv:2508.07018](https://arxiv.org/abs/2508.07018). [Card c34](dimitris-bertsimas/references/research/cards/c34.md).
- **S005** · Bertsimas, D. & Tsitsiklis, J. (1993). Simulated annealing. *Statist. Sci.* ✓ [doi:10.1214/ss/1177011077](https://doi.org/10.1214/ss/1177011077): the lead's "review" in his item 3 answer. Not Vicente's S005. [Card c01](dimitris-bertsimas/references/research/cards/c01.md).
- **S102** · Bertsimas, D. & Howell, L. H. (1993). Further results on the probabilistic traveling salesman problem. *Eur. J. Oper. Res.* ✓ [doi:10.1016/0377-2217(93)90145-d](https://doi.org/10.1016/0377-2217(93)90145-d): the scale test in the lead's item 4 answer. Not Conn's S102. [Card s2-02](dimitris-bertsimas/references/research/cards/s2-02.md).
- **S001** · Bertsimas, D. & Sim, M. (2004). The price of robustness. *Oper. Res.* 52(1), 35–53. ✓ [doi:10.1287/opre.1030.0065](https://doi.org/10.1287/opre.1030.0065). [Card c07](dimitris-bertsimas/references/research/cards/c07.md).
- **S340** · D. Bertsimas with J. D. Griffith, V. Gupta, M. J. Kochenderfer, V. V. Mišić and R. Moss (2014). A comparison of Monte Carlo tree search and mathematical optimization for large scale dynamic resource allocation. Preprint. ✓ [arXiv:1405.5498](https://arxiv.org/abs/1405.5498). [Card c14](dimitris-bertsimas/references/research/cards/c14.md).
- **S396** · Bertsimas, D., Lahlou Kitane, D., Azami, N. & Doucet, F. R. (2020). Novel mixed integer optimization sparse regression approach in chemometrics. *Anal. Chim. Acta*. ✓ [doi:10.1016/j.aca.2020.08.054](https://doi.org/10.1016/j.aca.2020.08.054). [Card s2-11](dimitris-bertsimas/references/research/cards/s2-11.md).
- **S689** · D. Bertsimas with D. den Hertog and T. Koukouvinos (2025). A novel exact approach to polynomial optimization. Preprint. ✓ [arXiv:2507.02120](https://arxiv.org/abs/2507.02120). [Card c35](dimitris-bertsimas/references/research/cards/c35.md).

### Papers on the guests' cards

Nocedal (jorge-nocedal):

- **S004** · Bottou, L., Curtis, F. E. & Nocedal, J. (2018). Optimization methods for large-scale machine learning. *SIAM Rev.* 60(2), 223–311. Link in the council's paper list. [Card c09](../nonlinear-team/jorge-nocedal/references/research/cards/c09.md).
- **S006** · Keskar, N. S., Mudigere, D., Nocedal, J., Smelyanskiy, M. & Tang, P. T. P. (2017). On large-batch training for deep learning: generalization gap and sharp minima. ICLR 2017. Link in the council's paper list. [Card c07](../nonlinear-team/jorge-nocedal/references/research/cards/c07.md).
- **S013** · J. Nocedal with R. A. Waltz, J. L. Morales and D. Orban (2006). An interior algorithm for nonlinear optimization that combines line search and trust region steps. *Math. Program.* (read as the 2004 preprint). [Card c05](../nonlinear-team/jorge-nocedal/references/research/cards/c05.md).
- **S018** · J. Nocedal with R. H. Byrd, G. M. Chin and Y. Wu (2012). Sample size selection in optimization methods for machine learning. *Math. Program.* [Card c07](../nonlinear-team/jorge-nocedal/references/research/cards/c07.md).
- **S038** · J. Nocedal with A. S. Berahas and R. H. Byrd (2019). Derivative-free optimization of noisy functions via quasi-Newton methods. *SIAM J. Optim.* [Card c10](../nonlinear-team/jorge-nocedal/references/research/cards/c10.md).
- **S040** · J. Nocedal with M. Marazzi (2002). Wedge trust region methods for derivative free optimization. *Math. Program.* [Card c2-01](../nonlinear-team/jorge-nocedal/references/research/cards/c2-01.md).
- **S041** · J. Nocedal with A. S. Berahas and R. Bollapragada (2020). An investigation of Newton-sketch and subsampled Newton methods. *Optim. Methods Softw.* [Card c10](../nonlinear-team/jorge-nocedal/references/research/cards/c10.md).
- **S043** · Oztoprak, F., Nocedal, J., Rennie, S. & Olsen, P. A. (2012). Newton-like methods for sparse inverse covariance estimation. *Advances in Neural Information Processing Systems 25*. Link in the council's paper list. [Card a2-02](../nonlinear-team/jorge-nocedal/references/research/cards/a2-02.md).
- **S062** · J. Nocedal with G. Fasano and J. L. Morales (2009), the "Fasano–Morales–Nocedal" of Nocedal's item 3 turn. On the geometry phase in model-based algorithms for derivative-free optimization. *Optim. Methods Softw.* [Card c06](../nonlinear-team/jorge-nocedal/references/research/cards/c06.md).
- **S080** · Shi, Xuan, Oztoprak and Nocedal (2023). On the numerical performance of finite-difference-based methods for derivative-free optimization. *Optim. Methods Softw.* (read as arXiv v1). [Card c12](../nonlinear-team/jorge-nocedal/references/research/cards/c12.md).
- **S084** · J. Nocedal with F. Oztoprak and R. Byrd (2023). Constrained optimization in the presence of noise. *SIAM J. Optim.* 33(3), 2118–2136. [Card c13](../nonlinear-team/jorge-nocedal/references/research/cards/c13.md).
- **S091** · J. Nocedal with H.-J. M. Shi, Y. Xie and M. Q. Xuan (2022). Adaptive finite-difference interval estimation for noisy derivative-free optimization. *SIAM J. Sci. Comput.* (read as arXiv v2). [Card s07](../nonlinear-team/jorge-nocedal/references/research/cards/s07.md).

Conn and Vicente (andrew-conn, luis-nunes-vicente):

- **S066** (Conn) = **S047** (Vicente) · Conn, A. R. & Vicente, L. N. (2012). Bilevel derivative-free optimization and its application to robust optimization. *Optim. Methods Softw.* 27(3), 561–577 (both cards read the 15 September 2010 preprint). Link in the council's paper list. [Conn's card c2-05](../dfo-team/andrew-conn/references/research/cards/c2-05.md), [Vicente's card s2-03](../dfo-team/luis-nunes-vicente/references/research/cards/s2-03.md).
- **S005** (Vicente) · L. N. Vicente with A. I. F. Vaz (2007). A particle swarm pattern search method for bound constrained global optimization. *J. Global Optim.* [Card c02](../dfo-team/luis-nunes-vicente/references/research/cards/c02.md).
- **S053** (Vicente) · L. N. Vicente with P. H. Calamai and J. J. Júdice (1993). A new technique for generating quadratic programming test problems. *Math. Program.* [Card s3-01](../dfo-team/luis-nunes-vicente/references/research/cards/s3-01.md).
- **S009** (Conn) · A. R. Conn with K. Scheinberg and Ph. L. Toint (1997). Recent progress in unconstrained nonlinear optimization without derivatives. *Math. Program.* ✓ [doi:10.1007/bf02614326](https://doi.org/10.1007/bf02614326). [Card c02](../dfo-team/andrew-conn/references/research/cards/c02.md).
- **S012** (Conn) · A. R. Conn with K. Scheinberg and L. N. Vicente (2009). Global convergence of general derivative-free trust-region algorithms to first- and second-order critical points. *SIAM J. Optim.* ✓ [doi:10.1137/060673424](https://doi.org/10.1137/060673424). [Card c2-05](../dfo-team/andrew-conn/references/research/cards/c2-05.md).
- **S019** (Conn) · A. R. Conn with Ph. L. Toint (1996). An algorithm using quadratic interpolation for unconstrained derivative free optimization. In *Nonlinear Optimization and Applications*. ✓ [doi:10.1007/978-1-4899-0289-4_3](https://doi.org/10.1007/978-1-4899-0289-4_3). Read as Namur Report 95/6 ✓ (perso.unamur.be/~phtoint/pubs/TR95-06.ps), whose Table 1 lists the 20 CUTE problems of Conn's tier (c). Not the lead's S019. [Card c2-02](../dfo-team/andrew-conn/references/research/cards/c2-02.md).
- **S020** (Conn) · A. R. Conn with K. Scheinberg and Ph. L. Toint (1998). A derivative free optimization algorithm in practice. 7th AIAA/USAF/NASA/ISSMO Symposium on Multidisciplinary Analysis and Optimization. ✓ [doi:10.2514/6.1998-4718](https://doi.org/10.2514/6.1998-4718). Not Burer's S020. [Card c2-03](../dfo-team/andrew-conn/references/research/cards/c2-03.md).
- **S040** (Conn) · A. R. Conn with N. Gould and Ph. L. Toint (1996). Numerical experiments with the LANCELOT package (Release A) for large-scale nonlinear optimization. *Math. Program.* ✓ [doi:10.1007/bf02592099](https://doi.org/10.1007/bf02592099). Not the lead's or Nocedal's S040. [Card c2-03](../dfo-team/andrew-conn/references/research/cards/c2-03.md).
- **S074** (Conn) · A. R. Conn with N. Gould and Ph. L. Toint (1997). On the number of inner iterations per outer iteration of a globally convergent algorithm for optimization with general nonlinear inequality constraints and simple bounds. *Comput. Optim. Appl.* ✓ [doi:10.1023/a:1008667728545](https://doi.org/10.1023/a:1008667728545). [Card s2-05](../dfo-team/andrew-conn/references/research/cards/s2-05.md).
- **S075** (Conn) · A. R. Conn with C. Audet, S. Le Digabel and M. Peyrega (2018). A progressive barrier derivative-free trust-region algorithm for constrained optimization. *Comput. Optim. Appl.* ✓ [doi:10.1007/s10589-018-0020-4](https://doi.org/10.1007/s10589-018-0020-4). [Card c2-05](../dfo-team/andrew-conn/references/research/cards/c2-05.md).
- **S102** (Conn) · A. R. Conn with I. Bongartz, N. I. M. Gould, M. A. Saunders and Ph. L. Toint (1997). A numerical comparison between the LANCELOT and MINOS packages for large-scale constrained optimization. Namur report 97-13, found by the second verifier; no DOI. Not the lead's S102. [Card s2-05](../dfo-team/andrew-conn/references/research/cards/s2-05.md).
- **S188** (Conn) · A. R. Conn with Ph. L. Toint (1994). A Comparison for Small-Scale Software Nonlinear Optimization Software (CSSNOS) preliminary project outline. Namur report 94/04, found by the second verifier; no DOI. [Card s2-04](../dfo-team/andrew-conn/references/research/cards/s2-04.md).
- **S233** (Conn) · A. R. Conn (1978). Direct approaches for the minimax problem. In *Computers and Mathematical Programming: Proceedings of the Bicentennial Conference*, NBS Special Publication 502, where the second verifier found it in the contents; no DOI. [Card s2-01](../dfo-team/andrew-conn/references/research/cards/s2-01.md).

Audet (charles-audet):

- **S055** · C. Audet with A. Ihaddadene, S. Le Digabel and C. Tribes (2018). Robust optimization of noisy blackbox problems using the mesh adaptive direct search algorithm (Robust-MADS). *Optim. Lett.* (abstract-level card). [Card a2-03](../dfo-team/charles-audet/references/research/cards/a2-03.md).
- **S156** · C. Audet with V. Dijon and Y. Diouane (2026). Benchmarking bilevel derivative-free optimization algorithms. Preprint. ✓ [arXiv:2605.30531](https://arxiv.org/abs/2605.30531). [Card c08](../dfo-team/charles-audet/references/research/cards/c08.md).
- **S172** · C. Audet with T. Denorme, Y. Diouane, S. Le Digabel and C. Tribes (2026). Adaptive direct search algorithms with relaxable and quantifiable constraints. Preprint. [Card c09](../dfo-team/charles-audet/references/research/cards/c09.md).
- **S128** · C. Audet with W. Hare and C. Tribes (2026). A summary of benchmarking constrained, multi-objective and surrogate-assisted optimization methods. *Optim. Lett.* ✓ [doi:10.1007/s11590-026-02302-z](https://doi.org/10.1007/s11590-026-02302-z) (read as the GERAD report G-2025-36): the source of Audet's v2 dissent. [Card c08](../dfo-team/charles-audet/references/research/cards/c08.md).

Burer (samuel-burer):

- **S014** · S. Burer with R. D. C. Monteiro (2001). A projected gradient algorithm for solving the maxcut SDP relaxation. *Optim. Methods Softw.* (read as the preprint). [Card c01](../minlp-team/samuel-burer/references/research/cards/c01.md).
- **S016** · S. Burer with A. Saxena (2012). The MILP road to MIQCP. In *Mixed Integer Nonlinear Programming*, IMA Vol. 154 (read as the preprint). [Card c04](../minlp-team/samuel-burer/references/research/cards/c04.md).
- **S020** · S. Burer (2010). Optimizing a polyhedral-semidefinite relaxation of completely positive programs. *Math. Program. Comput.* [Card c04](../minlp-team/samuel-burer/references/research/cards/c04.md).
- **S021** · S. Burer with B. Yang (2015). The trust region subproblem with non-intersecting linear constraints. *Math. Program.* [Card c06](../minlp-team/samuel-burer/references/research/cards/c06.md).
- **S047** · S. Burer with J. Chen (2011). Relaxing the optimality conditions of box QP. *Comput. Optim. Appl.* [Card s02](../minlp-team/samuel-burer/references/research/cards/s02.md).
- **S049** · S. Burer (2025). A slightly lifted convex relaxation for nonconvex quadratic programming with ball constraints. *Math. Program.* (read as the arXiv version). [Card c08](../minlp-team/samuel-burer/references/research/cards/c08.md).

Dey (santanu-s-dey):

- **S129** · Dey, S. S. & Kocuk, B. (2025). Convexification of a separable function over a polyhedral ground set. ✓ [arXiv:2510.16595](https://arxiv.org/abs/2510.16595). [Card c17](../minlp-team/santanu-s-dey/references/research/cards/c17.md).
- **S014** (Dey) · S. S. Dey with A. Gupte (2015). Analysis of MILP techniques for the pooling problem. *Oper. Res.* ✓ [doi:10.1287/opre.2015.1357](https://doi.org/10.1287/opre.2015.1357). Not Burer's S014. [Card c04](../minlp-team/santanu-s-dey/references/research/cards/c04.md).
- **S028** · S. S. Dey with M. Molinaro and Q. Wang (2015). Approximating polyhedra with sparse inequalities. *Math. Program.* ✓ [doi:10.1007/s10107-015-0925-y](https://doi.org/10.1007/s10107-015-0925-y). [Card c04](../minlp-team/santanu-s-dey/references/research/cards/c04.md).
- **S081** · S. S. Dey with P. Shah and M. Molinaro (2026). Non-monotonicity of branching rules with respect to linear relaxations. *INFORMS J. Comput.* ✓ [doi:10.1287/ijoc.2024.0709](https://doi.org/10.1287/ijoc.2024.0709) (read as arXiv:2402.05213v1, per the card). [Card c18](../minlp-team/santanu-s-dey/references/research/cards/c18.md).
- **S100** · S. S. Dey with J. Huchette and J. P. Vielma (2018). Beating the SDP bound for the floor layout problem: a simple combinatorial idea. *INFOR*. ✓ [doi:10.1080/03155986.2017.1363592](https://doi.org/10.1080/03155986.2017.1363592) (read as arXiv:1602.07802v2, per the card). [Card s04](../minlp-team/santanu-s-dey/references/research/cards/s04.md).
- **S119** · Blekherman, G., Dey, S. S., Dunbar, A. & Kocuk, B. (2026). Copositive matrices with ordered off-diagonal entries. Preprint. ✓ [arXiv:2605.15970](https://arxiv.org/abs/2605.15970): the preprint of Dey's item 4 rejoinder. [Card c20](../minlp-team/santanu-s-dey/references/research/cards/c20.md).
- **S123** · S. S. Dey with D. Han and Y. Wang (2026). Extreme strong branching for QCQPs. *Oper. Res. Lett.* ✓ [doi:10.1016/j.orl.2026.107446](https://doi.org/10.1016/j.orl.2026.107446) (read as arXiv:2510.20650v1, per the card). [Card c21](../minlp-team/santanu-s-dey/references/research/cards/c21.md).

### Other papers named in the turns

- Bao, X., Sahinidis, N. V. & Tawarmalani, M. (2011). Semidefinite relaxations for quadratically constrained quadratic programming: a review and comparisons. *Math. Program.* 129(1), 129–157. ✓ [doi:10.1007/s10107-011-0462-2](https://doi.org/10.1007/s10107-011-0462-2). Sahinidis's "co-authored 2011 QCQP comparison" [01 SW2]; its QCQP set qcqp2 is listed on minlp.com's test-problem page ✓.
- Nohra, C. J., Raghunathan, A. U. & Sahinidis, N. V. SDP-quality bounds via convex quadratic relaxations for global optimization of mixed-integer quadratic programs (title as recorded in Sahinidis's note 01). ✓ [arXiv:2106.13721](https://arxiv.org/abs/2106.13721): MIQPs with linear equality constraints, implemented in BARON.
- Moré, J. J. & Wild, S. M. (2009). Benchmarking derivative-free optimization algorithms. *SIAM J. Optim.* 20(1), 172–191. ✓ [doi:10.1137/080724083](https://doi.org/10.1137/080724083): the data profiles of Nocedal's item 3 test.
- Moré, J. J. & Wild, S. M. "Estimating computational noise" (ECnoise): the method is published, confirmed through Optimization Online; the code download is *(unverified)*, since its Argonne page returned 403.
- Huangfu, Q. & Hall, J. A. J. (2018). Parallelizing the dual revised simplex method. *Math. Program. Comput.* 10(1), 119–142: Huangfu's "MPC"; its figures are confirmed, and the link is in the council's paper list.
- Bixby (2012), pp. 116–118: Huangfu's source for the 29,000 chain; its content is confirmed by the verifier; the full reference was not recorded in this session.
- J. Hall, *HiGHS: Theory, software and Impact*, KTH, 1 Oct 2021 (Huangfu's "KTH21 slides"; slides 25–26 confirmed), recorded in qi-huangfu note 03 (S23); and the HiGHS parallelism documentation ("unlikely to be more than eight", confirmed).
- Sridhar, S., Wright, S. J., Ré, C., Liu, J., Bittorf, V. & Zhang, C. (2013). An approximate, efficient LP solver for LP rounding. *Advances in Neural Information Processing Systems 26*: the paper whose NIPS 2013 author feedback is the "joint NIPS 2013 rebuttal" in Wright's item 2 turn, recorded in stephen-j-wright note 03 §2.3; link in the council's paper list.
- Wilson & Sahinidis (2017). The ALAMO approach to machine learning. ✓ [arXiv:1705.10918](https://arxiv.org/abs/1705.10918) (read as v1): the "2017 ALAMO paper" of Sahinidis's item 1 turn; the second verification confirmed that p. 3's why-now sentence carries no citation and that p. 4 calls the R leaps package "limited to only 32 regressors".
- Hastie, T., Tibshirani, R. & Tibshirani, R. (2020). Best subset, forward stepwise or lasso? Analysis and recommendations based on extensive comparisons. *Statist. Sci.* 35(4), 579–592, with its rejoinder, 625–626: "HTT" and "HTT's rejoinder" in item 2, as recorded in nikolaos-v-sahinidis note 05 (references 73 and 75; §A8, rows 8d–8e); not re-checked in this round.
- Sarwar, O., Sauk, B. & Sahinidis, N. V. (2020). A discussion on practical considerations with sparse regression methodologies. *Statist. Sci.* 35(4), 593–601: "SSS", the 2020 discussion by Sahinidis's group, as recorded in nikolaos-v-sahinidis note 05 (reference 14; §A8, row 8d); not re-checked in this round.
- Bertsimas, D., Pauphilet, J. & Van Parys, B. (2020). Rejoinder: Sparse regression: scalable algorithms and empirical performance. *Statist. Sci.* 35(4), 623–624: "BPV's rejoinder" in item 2, as recorded in nikolaos-v-sahinidis note 05 (reference 76); not re-checked in this round.
- Bestuzheva, Chmiela, Müller, Serrano, Vigerske & Wegscheider (2025). Global optimization of mixed-integer nonlinear programs with SCIP 8. *J. Global Optim.* 91, 287–310: "the SCIP 8 study" of Sahinidis's item 1 rejoinder, as recorded in nikolaos-v-sahinidis note 05 (§A1, row 1h); not re-checked in this round.

### Libraries, benchmarks and software named in the plan

- MINLPLib ✓ ([minlplib.org](https://www.minlplib.org); Bussieck, Drud & Meeraus 2003, [doi:10.1287/ijoc.15.1.114.15159](https://doi.org/10.1287/ijoc.15.1.114.15159)) and QPLIB ✓ ([qplib.zib.de](https://qplib.zib.de); Furini et al. 2019, [doi:10.1007/s12532-018-0147-4](https://doi.org/10.1007/s12532-018-0147-4)), both in the council's [Shared References](council-roundtable/SKILL.md#shared-references-verified-2026-10).
- Mittelmann, H. D., Benchmarks for Optimization Software ✓ ([plato.asu.edu/bench.html](https://plato.asu.edu/bench.html)): Continuous Non-Convex QPLIB, 17 May 2026 (BARON 25.12.10, SCIP 10.0.1, 8 threads, 3 h); MINLPLib through GAMS, 26 Feb 2026 (2 h). Third-party context: their releases and threads differ from the plan's. Top500 ✓ (online).
- R packages on CRAN ✓: leaps 3.2 (2024-06-10); glmnet 5.2 (2026-10-28, with the relax option); glasso 1.11; L0Learn 2.1.0 (struck by the neutrality note, restored by the lead at sign-off); lars 1.3, which carries the Diabetes data with the 64-column x2. QUIC *(unverified)*: the CRAN package was removed on 2020-08-03 (the archive ends at 1.1.1), and the authors' page returns 404.
- BARON ✓ (minlp.com): release 26.9.10 of 10 September 2026 ("2026.9.10" in the release notes), with MAXWORK new in that release; its free build handles up to 10 variables and constraints and 50 nonlinear operations; releases 20.10.16 and 21.1.13 appear in the release notes (whether they still run: *(unverified)*). The BARON user manual (minlp.com/baron-user-manual), §4.1 and §10.2, holds the relaxation-only advice ✓.
- SCIP 10.1.0 ✓ (scipopt.org). MOSEK documentation ✓: conic problems get only an interior-point optimizer, and NUM_THREADS = 0 lets the optimizer choose. SDPNAL+ (MATLAB) ✓ [arXiv:1710.10604](https://arxiv.org/abs/1710.10604).
- CUTEst ✓ (its SIF collection, bitbucket.org/optrove/sif): the second verifier found all 20 problems of Conn's tier (c), from Table 1 of Report 95/6, there; BARD has 3 variables in CUTEst against the table's 2, and PFIT1LS is bound-constrained.
- R packages newly named, on CRAN ✓ (second verification): ncvreg 3.16.0 (MCP and SCAD) and huge 2.0.1 (method "mb" for MB). The leaps 3.2 reference manual documents leaps() as a wrapper for regsubsets that stops above 31 columns at its default, and regsubsets with nvmax = 8 by default, really.big required for exhaustive search above 50 variables, and no time-limit argument or tolerance; leaps 2.9, the CRAN release from 2009-05-05 to 2017-01-10, had the same 31-column cap. The L0Learn 2.1.0 manual gives L0Learn.cvfit with penalty "L0L2", whose gamma multiplies the squared ℓ2 norm.
- Gurobi Optimizer Reference Manual 13.0 ✓ (docs.gurobi.com), WorkLimit: deterministic, stopping at the same point only on the same hardware and settings; a work unit "greatly depends on" hardware and model (second verification).
- Solver defaults, as checked by the second verification ✓: the BARON user manual v. 2026.9.10 (minlp.com/baron-user-manual) gives MaxTime 500 s and EpsR 1e-6, tested as |U − L| ≤ εr·max(|L|, |U|); SCIP 10.1.0 (scipopt.org) gives limits/gap 0, with gap = |primal − dual|/MIN(|dual|, |primal|), 'Infinity' when the signs differ, and limits/time 1e+20. GAMS's BARON page (for BARON 24.9.12) takes EpsR from OptCR and lets MaxTime override ResLim, so defaults depend on the interface. CPLEX 22.1.2, the release of S708's duel [S708 p. 35], is listed by IBM (second verification).

### Members' files cited without cards

Huangfu, Gould, Wright and Sahinidis have no paper cards; their turns cite their `SKILL.md` sections and research notes 01–06 (publications, methodology, process evidence, mentorship, peer critique, trajectory), so "[03 §2.2]" is §2.2 of that member's note 03 and "[01 SW2]" is item SW2 of note 01: [qi-huangfu](../lp-team/qi-huangfu/references/research/), [nicholas-i-m-gould](../nonlinear-team/nicholas-i-m-gould/references/research/), [stephen-j-wright](../nonlinear-team/stephen-j-wright/references/research/), [nikolaos-v-sahinidis](../minlp-team/nikolaos-v-sahinidis/references/research/).

The challengers' round and the v2 sign-offs also cite the lead's own research notes in the same way ([02 O5], [02 P7], [05 §1.3], [05 §1.4]): [dimitris-bertsimas](dimitris-bertsimas/references/research/). Conn's turns cite his technique catalog by entry (E2, P16, P20, A1, A5, W7): [andrew-conn technique catalog](../dfo-team/andrew-conn/references/technique-catalog.md).

## 中文摘要

主题"精确性的代价"：可认证的精确答案何时值得其成本。首轮挑战者未发言，后补回合，[Bertsimas lens] 回应后改为 v2 计划并重签。

议题 1（FL1）分歧：认证前沿移动能否单独支撑"now tractable"，还是无净比率只算背景（[Huangfu lens]），由你定。[Sahinidis lens] 指出 leaps 的"p ≤ 30"也是借来的，领衔者承认；检验加穷举 regsubsets、统一预算、双档 gap 与重拟合审计。

议题 2（FL2）分歧：关闭 gap 能否买到统计收益（与 [Nocedal lens]、[Wright lens]）。[Sahinidis lens] 补上 ncvreg、指出价格未测；领衔者让步，停在"旋钮与价格"，检验为整条流程计时与 (V1)/(V2) 判读，只有关闭 gap 才算证明有用。

议题 3（FL4）：模拟器上只声称经核查的下界。[Conn lens] 使领衔者承认终止检验只是停止规则、手工例不能说"wins"，检验加公共层与逐项切换；平局时覆盖还是精度，交 Conn 的精度梯级与审计类别。

议题 4（FL5）：LMI 何处值得仍分歧。[Dey lens] 指出其数据上按结构选的乘积比 LMI 更贵；领衔者改为一臂，加复现门槛与固定 incumbent 列，改用固定列支配。

v2 主要变化：账本增"停止规则"与逐层判定，各议题采纳挑战者检验，v1 条件全收。签署 6 位：[Bertsimas lens]、[Huangfu lens]、[Vicente lens]、[Burer lens]，附条件的 [Gould lens]（节点门槛只管原样重建）、[Sahinidis lens]（RPT 论文实例算开发集），核查称 v2 未满足。异议 5 位：[Nocedal lens]（到达 gap ≤ 10⁻⁴ 才认证）、[Wright lens]（孪生各自选参）、[Audet lens]（梯度搜索作参考线）、[Conn lens]（改写审计类别）、[Dey lens]（统一有界 gap 公式）。

核查：第一轮查首轮发言与 v1 的 40 条关键引用；第二轮三位核查员查挑战者回合、v2 与签署共 661 项，标出 27 个问题；最后对首轮全部 271 条卡片引用普查，236 条成立，33 条存疑（23 条为新标注），并更正第一轮的 3 处误读。所有问题都以斜体注记留在原处，未删任何内容。待你在检查点 4 批准。

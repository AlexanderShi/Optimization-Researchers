# Frank E. Curtis · Evidence ledger

> Date: 2026-10-10. The full evidence behind `SKILL.md` after the first full-text deep reading (cards in `cards/`, index `07-paper-cards.md`, synthesis `08-deep-reading-synthesis.md`). SKILL.md keeps, per item, the strongest statement and cards, a one-line say–do count, at most four variant or correction bullets and a link here. Each section below holds (a) the **base-tier text** of the item as it stood in SKILL.md on 2026-09-28 (web research only), copied **verbatim**, so nothing condensed out of SKILL.md is lost, and (b) the **full-text evidence** added on 2026-10-10, with card ids and pages.
>
> **How to read.** `[S012 p. 9]` is paper card S012 in `07-paper-cards.md`, at the page of the extracted file named in `../sources/papers/INDEX.md` (several cards give the journal-page offset in their header); `[S071 TR pp. 5, 15]` and `[S050 arXiv p. 5]` cite the version named on the card. A bare id is an abstract-level or metadata card (no page). Quotation marks around card material surround only text in a card's verified Quotes list (`verify_card_quotes.py`: 180 of 180 exact). Quotes in the base-tier blocks come from the web research of 2026-09-28 (slides, research page, code, theses) with the source named; they were not re-verified against cards.
>
> **Counting rules.** Say–do counts are distinct cards whose `method_links` point at the item, at all read levels (abstract-level cards: one each for Methods 1 and 2, three for Method 5; Methods 3 and 4 are all full); *works* merges the five possible journal/preprint pairs, which are indexed separately and are unconfirmed: S045 ~ S037, S031 ~ D001, S072 ~ S069, S060 ~ S061, S063 ~ D002. Each pair counts once in every tally and in the ≥3-works promotion threshold. S058, S081 and S086 are pre-PhD combinatorics (2003–2006) and carry no weight. Cards also record reading notes about inconsistencies inside individual works; those are not findings about the researcher and are not used here.

## Contents

- [Research task routing](#routing)
- [Taste: marks of good research](#taste-marks)
- [Taste: warning signs of bad research](#taste-warnings)
- [Method 1: The inner solve serves the outer solver](#method-1)
- [Method 2: Steer, don't switch](#method-2)
- [Method 3: Break it on purpose](#method-3)
- [Method 4: Audit the yardstick](#method-4)
- [Method 5: Fair-fight benchmarking](#method-5)
- [Guard the incumbent (drafted as Method 6; kept as the full-text form of Heuristic 5)](#method-6)
- [Stage workflows](#workflows)
- [Heuristics 1–11](#heuristic-1)
- [Signature works](#anatomy-inexact-sqp)
- [Research anti-patterns](#anti-patterns)
- [Research trajectory](#trajectory)
- [Inner tensions](#inner-tensions)
- [Honest boundary (base-tier text)](#honest-boundary)
- [Corrections from the full texts](#corrections)
- [Candidates not promoted](#not-promoted)
- [Sources (base-tier lists)](#sources)
- [Card key](#card-key)

---

<a id="routing"></a>
## Research task routing

**Base-tier text (verbatim):**

#### Research Task Routing

Take the **first** row that fits (rows are in the order to check); a request that fits no row gets the weak-spot rule (How to Use).

| User says | Workflow | Main methods |
|---|---|---|
| "We are stuck", "tried X for weeks", crashes, regressions, strange exits | S | Heuristics 9, 8, 1, then the class S finds |
| "Give us ideas to improve our solver" (no symptom named), or "it converges, but slowly" | A (step 1 sorts by his two lists), then the class's workflow | Methods 3, 1, 2; a lost local rate: weak-spot rule |
| "The solver fails or crawls on infeasible or degenerate models", or must return fast infeasibility verdicts inside MINLP branch-and-bound | A, then B | Methods 3, 2 (step 4); Heuristic 3; Taste quick-check. Warm starts: weak-spot rule |
| "The restoration phase or the penalty parameter misbehaves" | B | Method 2; Heuristics 1, 2; state Tension 4 when advising steering over restoration |
| "Filter or merit/penalty function? Keep the restoration phase?" | B, then D | Method 2 with Tension 4 (his slides where "Filter" needs fewer iterations) stated first; deciding test (inferred): Method 3's variants on both designs; for the filter side offer `debate Curtis vs Wächter` (or `vs Fletcher`) in nonlinear-roundtable |
| "KKT systems are too large to factorize; what tolerance for the iterative solve?" | B | Method 1 |
| "Nonsmooth terms (max, abs, eigenvalues) in the objective or constraints" | B (step 3), then C | Heuristic 10 (keep the SQP-penalty skeleton, swap only the gradient information); Heuristic 5 (BFGS-SQP beside SQP-GS); Method 5 step 3 (p = 0 ablation); Method 4 (relative minimization profiles) |
| "Function values are noisy or sampled" | B with Heuristic 10 | Method 1, translated |
| "How do we benchmark this change fairly?" | C | Methods 5, 3; Heuristic 7 |
| "Is this improvement real? Keep it or drop it?" | D | Methods 4, 5; Heuristic 1 |
| "Does a complexity bound tell us which method to use?" | D, step 4 | Method 4; TRACE anatomy |
| "Review our paper, report or release notes" | E | Method 5 step 7, Method 4 |
| "A reviewer attacks our benchmark or claims" | C, D, E | Methods 4, 5, 3; Heuristic 7 |
| Linear-algebra backend: GPU, mixed precision, sparse factorization, pivoting, inertia, preconditioning | Outside his record: weak-spot rule | Method 1 (+ Heuristic 2, Method 5), extrapolated |
| Literature review, writing the rebuttal letter itself, supervision, grant writing | None: say "no distillable Curtis method", give generic advice labelled "not Curtis-style" | — |

**2026-10-10 changes**: a row for a fast heuristic without a guarantee (→ Method 6); Method 6 added to the open-ideas, nonsmooth and keep-or-drop rows; "Heuristic 5" in the nonsmooth row replaced by Method 6, since old Heuristic 5 folded into Method 6 (C12); the noisy row gains the Method 2 variant for uncomputable progress tests (C10); the review row gains Heuristic 1's theory–code clause. **Review fix (same day)**: the draft Method 6 failed the exclusivity check and was kept a heuristic ([below](#method-6)); the rows that named it now name Heuristic 5 (its base-tier meaning, extended by the guarded-incumbent form), and the port-the-property rows name Heuristic 11; the nonsmooth row again names Heuristic 5 (BFGS-SQP beside SQP-GS) as in the base-tier text.

---

<a id="taste-marks"></a>
## Taste: marks of good research

**Base-tier text (verbatim):**

#### Marks of good research
1. **The solver behaves well when the model is badly posed** (infeasible, degenerate, highly nonlinear). Evidence: "A major challenge often overlooked in research on nonlinear optimization is the fact that contemporary techniques often perform poorly when all of the problem constraints cannot be satisfied simultaneously." (research page); PIPAL's constructed variants (01 SW2).
2. **Scale a method while keeping the classical guarantees**: "maintaining the global and fast local convergence guarantees offered by classical methods" (research page); TRACE keeps the trust-region framework (01 SW4); "Achieving good/optimal complexity for practical algorithms." (ICCOPT 2019).
3. **One algorithm with monitored transitions beats a two-phase design**. Deterministic evidence: the 2008 single-algorithm goal (Method 2; INFORMS OS 2008, slide 5); a switch's difficulty "lies in the design of effective criteria for determining when such a switch should be made" (10.1137/080738222, p. 2282); PIPAL, SQuID (02 R3, R8). "“Two-phase” methods are not effective" (NeurIPS 2022, slide 11/42; EUCCO 2023, slide 13/44) sits under "We assume:" for "the fully stochastic regime", not as a general verdict.
4. **Nonconvexity is acceptable; local search is worthwhile**: "Nonconvexity cannot always be avoided. And that's OK!" (ECOM 2021 public lecture); NonOpt "is not guaranteed to find a global minimizer" (homepage).
5. **The workhorse is a target, not an endpoint**: "SG requires a lot of tuning" (Google 2016 talk); he advocates adaptive, second-order methods instead (ECOM 2021 public lecture).

**Full-text evidence (2026-10-10):**
- Mark 1 (badly posed models): constructed infeasible and degenerate variants [S025 pp. 22–23; S009 pp. 14–16; S033 pp. 22, 25–26; S022 p. 30; S021 pp. 27–28]; "Fast detection" for MINLP [S009 p. 1]; "What the method lacks, however, are fast local convergence guarantees when (1.1) is infeasible." [S009 p. 3].
- Mark 2 (keep classical guarantees): "Therefore, we contend that it is of interest to explore trust-region methods that do not deviate too much from traditional schemes, yet offer optimal worst-case complexity properties." [S043 p. 4]; TRACE keeps trust-region guarantees [S002 p. 30]; "This discussion is meant to provide confidence to a user that our algorithm is based on one that has state-of-the-art convergence properties under common assumptions in the deterministic setting." [S030 p. 8].
- Mark 3 (one algorithm, monitored transitions): confirmed for the objective–feasibility trade-off [S032 pp. 9–11; S009 pp. 2, 13–14; S033 pp. 13–17; S022 pp. 2, 7]. ⚠ Qualified (C9): deliberate switches or phases: the two-phase trust funnel kept for complexity [S026 pp. 1–2, 25]; a switch to a traditional augmented Lagrangian near solutions proposed to inherit its theory [S019 pp. 33, 43]; the step computation switches on a steplength trigger [S036 pp. 9–10]; a separate Phase I for a strictly feasible start [S063 pp. 3, 5, 30–31]; a design the paper itself calls two-phase, whose phases both run every iteration [S022 p. 1]. Switching a computational module on a monitored trigger is accepted and is Heuristic 5's guarded incumbent (drafted as Method 6).
- Mark 5 (workhorse as target): SG placed at the origin of the method map [S001 pp. 20–21, 40]; SGD's parameter sensitivity [S011 p. 11]; "Ultimately, an algorithm that performs like SG at the start and transitions to a regime of reduced variance in an efficient manner could prove to be a very powerful method for large-scale learning." [S001 p. 45].
- Mark 6 (new; speed by default, guarantee on demand): "A feature critical to the practical performance of our algorithm is that, when it is applied to solve many problem instances, the algorithm reduces to an unadulterated BFGS strategy for the majority of the iterations." [S008 p. 2]; "The resulting algorithm fully integrates the procedures of step computation and step selection and automatically reduces to an inexact SQP method in convex regions of the search space." [S017 p. 2]; price measured [S036 p. 12]. Full evidence: [the guarded incumbent](#method-6) (now Heuristic 5). Review: marked *(practice; inferred as taste)* in SKILL.md, and "in most iterations" is cited to S008 p. 2 only; S017 p. 2 says *in convex regions*.
- Mark 7 (new; limits and non-claims up front): "Let us emphasize upfront that we do not expect our method to be competitive with state-of-the-art interior-point methods in the deterministic regime, and especially not with those that employ second-order derivatives of the objective." [D002 p. 3]; "We mention upfront that our proposed algorithm and analysis leave certain natural questions unanswered." [S059 p. 4]; "We highlight upfront that the convergence-rate guarantee for our proposed algorithm is not stronger than that of Adam; the point is that the algorithm has a comparable guarantee and can perform better in practice in various settings." [S090 p. 3]; also [S073 p. 3]. Explicit non-claims: "We do not claim that “SQP Adaptive” is as efficient as “SQP Backtracking” since, as has been verified by others in the literature, the line search scheme is very effective across a broad range of problems." [S007 p. 26]; [S014 p. 21; S046 p. 3].

---

<a id="taste-warnings"></a>
## Taste: warning signs of bad research

**Base-tier text (verbatim):**

#### Warning signs of bad research
1. **Theory built on anomalous objectives, or a measure chosen to favour the method**: "conservative characterizations based on anomalous objectives rather than on ones that are typically encountered in practice" (regional complexity abstract, DOI 10.1007/s10107-020-01492-3); "self-fulfilling prophecy" (ISMP 2018).
2. **A verdict from one test set, untuned rivals, uncounted tuning or one run**: Oaxaca 2017 slide 33/33; ECOM 2021 public lecture slides 34–42, with his own paper as the example ("But if you change the test set, it’s a different picture! Curtis (2012)").
3. **Worst-case complexity sold as practical gain**: "“Better complexity” has yet to mean “better performance” for nonconvex!" (ECOM 2021 public lecture, citing his own TRACE).

#### Taste quick-check
- [ ] Does it still work on infeasible or degenerate instances, keeping the global and fast local guarantees of the method it modifies?
- [ ] One algorithm with a monitored transition, not a switch to a separate phase?
- [ ] Is the inner solve's accuracy derived from what the globalization needs?
- [ ] Would the advantage survive another test set, a tuned incumbent, counted tuning and repeated runs?
- [ ] Is success judged independently of your own termination flag or favourable stationarity test?
- [ ] Is the event your theory needs measured in runs, and each safeguard's per-iteration cost counted?

**Full-text evidence (2026-10-10):**
- Warning 1 (measure chosen to favour the method): "Such questions are not answered well by contemporary worst-case results, which are too conservative." [S062 p. 4]; termination flags distrusted because they "would be skewed in favor of the codes that yielded such a flag most often" [S008 p. 25].
- Warning 2 (one test set): "Rather than contrast SG and other methods based on the results of numerical experiments—which might bias our review toward a limited test set and implementation details—we focus our attention on fundamental computational trade-offs and theoretical properties of optimization methods." [S001 p. 4].
- Warning 3 (worst case sold as practice): "Based on such evidence, we do not claim that the convergence results proved in this paper fully capture the practical behavior of LMSD methods." [S046 p. 3]; "This would likely lead to very poor behavior in practice compared to the strategies in Sections 2.3 and 2.4, which are much less conservative." [S035 p. 9]; "The variants with no regularization term in the subproblems outperform the others in this respect; recall that these variants do not possess optimal complexity guarantees." [S020 p. 22].
- Warning 2, full-text addition (drafted as a separate Warning 4 on unequal tuning effort; merged into Warning 2 at review because it repeated it): "We took care to make sure that the tuning procedure for TRish did not require more effort than the tuning used for the SG method that we have for comparison purposes." [S015 p. 18]; "To ensure that all algorithms were tuned with the same amount of effort, we fixed the total number of hyperparameter settings to be the same for all algorithms." [S041 p. 22]; "Tuning these parameters means that problems cannot be solved once; they need to be solved numerous times" [D001 p. 2]. Say–do caveat: deterministic papers tune on the evaluation runs (C5).
- Warning 4 (new; numbered 5 in the first draft; inexactness or adaptivity added naively): "allowing inexactness is not something that can be done naively." [S016 p. 4]; "a simpler heuristic method that merely decreases a dynamic accuracy tolerance as the optimization process proceeds will not ensure convergence unless one imposes strong requirements on the employed linear system solver" [S064 p. 2]; "the benefits of these techniques are only realized if inexact step computations are allowed and controlled appropriately in order to guarantee global convergence of the algorithm." [S010 p. 2].
- Quick-check line added: *When the guard is idle, is the method exactly the incumbent, and did you count how often the guard woke and what the guarantee cost?* (from 08 §4).

---

<a id="method-1"></a>
## Method 1: The inner solve serves the outer solver

**Base-tier text (verbatim):**

#### Method 1: The inner solve serves the outer solver
**One line**: Decide how accurately a linear system or QP must be solved by asking what the globalization (merit function, penalty, trust region) needs from the step, and make that the iterative solver's termination test.
**Evidence**:
- Stated: "one needs to design an algorithm in which the demands of the “outer” nonlinear solver are understood by the “inner” subproblem (typically a quadratic optimization problem or linear system) solver" (research page); "Much of my work: exploiting inexactness for scalable constrained optimization." (ICCOPT 2019).
- Practice: SMART tests treating primal and dual residuals "as separate quantities" (10.1137/060674004, p. 352); an inertia-free "Hessian Modification Strategy" (10.1007/s10107-008-0248-3, p. 283); rank deficiency (10.1137/08072471X); inexact IPM in Ipopt (10.1137/090747634; 10.1007/s10107-012-0557-4); updates inside the QP solve (10.1137/18M1176488); inexact TRACE (10.1137/22M1492428); stochastic (10.1287/ijoo.2022.0008).
- Observed cost: "The stabilized SMART tests in [24, 22] require the solution of two Newton systems, thus doubling the price of a Newton iteration." (Huber thesis 2013, via Semantic Scholar context; 05 §4.3).
- Say–do consistency: ✅ stated + practised, 2006–2024.
**Steps**:
1. Write the outer acceptance condition: sufficient decrease in a local model of the exact-penalty merit function, or trust-region model decrease.
2. Derive the iterative solver's termination tests from it, testing primal and dual residual components separately instead of one relative residual on the whole KKT system (01 SW1).
3. Add a fallback test that tells the outer loop to change something (penalty parameter; Hessian modification without inertia, 10.1007/s10107-008-0248-3, p. 283) when the test cannot be met.
4. Build a baseline that differs only in the stopping rule (relative residual at several tolerances; SW1: 45–86 % solved against 100 %, Signature Work Anatomy). Add a factorizing variant as ceiling, "to gauge how Algorithm INS compares to an idealized approach" (10.1007/s10107-008-0248-3, p. 296).
5. Make the failure tests crude on purpose: "we implement naïve failure tests in Algorithm B to aggressively challenge the robustness of our approach" (10.1137/060674004, p. 366).
6. Move the tests into a production code and time iterations at scale: "under 9 minutes" per iteration against "approximately 40 minutes" for default Ipopt (research page, on 10.1137/090747634).
**Applies to stage**: algorithm design; scaling an existing solver.
**Different from standard practice**: classical inexact Newton bounds the whole residual by a forcing sequence, and most NLP codes factorize. Here the merit model sets the accuracy, component by component.
**Limitations**: line-search merit frameworks; extra solves and many constants ("the SMART tests involve many parameters", Hicken 2014, via Semantic Scholar context); preconditioning deferred; production adoption stalled (Ipopt option still experimental).

**Full-text evidence (2026-10-10).** Cards linked: 45 (44 works): 22 evidence ✅, 23 variant ⚠, 1 contradiction ✗ (S094). All links from full cards except S045 (abstract).

- **Strongest practice**: the dissertation states the question in its first technical chapter, "The main purpose of this chapter is to determine the accuracy with which the SQP subproblems must be solved in order to ensure global convergence in the context of a practical algorithm for problem (2.1)." [S096 p. 23], with merit-model tests on separate primal and dual residuals [S096 pp. 26–29], and closes on "A major theme in this work has been the importance of tying various aspects of the optimization process into one cohesive unit." [S096 p. 98]. The same tests run through the equality, rank-deficient, nonconvex and interior-point rungs [S006 pp. 5–7; S025 pp. 6–8; S017 pp. 2, 10–11; S010 pp. 8–10, 18] into Ipopt [S036 pp. 6–7, 11–17], into the QP solver itself ("In this manner, the QP solver iterates until the needs of the (outer) algorithm are met." [S029 p. 13]; [S057 pp. 5, 7–9]), into gradient sampling [S065 pp. 7–10], inexact TRACE [S043 pp. 6–7, 16–17], stochastic SQP [S037 pp. 6–7] and NonOpt's tailored QP solver [S088 pp. 3, 9, 14, 17].
- **Stated in full texts**: "Our approach, on the other hand, is based on a requirement that the step decreases a local approximation of a merit function while also satisfying bounds on the primal and dual components of the residual." [S006 p. 2]; "the benefits of these techniques are only realized if inexact step computations are allowed and controlled appropriately in order to guarantee global convergence of the algorithm." [S010 p. 2]; "allowing inexactness is not something that can be done naively." [S016 p. 4]; a dynamic-tolerance shortcut "will not ensure convergence unless one imposes strong requirements on the employed linear system solver" [S064 p. 2]; "we intend to forgo the interpretation of our step as an (approximate) solution to a local optimization subproblem and instead jump straight to its effect on our globalization mechanism." [S017 p. 4].
- **Say–do**: ✅ stated + practiced, with a primary stated side from 2007 [S096 pp. 23, 98] to 2023 [S016 p. 4]; practised 2007–2026.
- **Correction C1** (full text beats the web snippet): step 6 cited, from the research page, a time per iteration of under 9 minutes against about 40 minutes for default Ipopt, attributed to 10.1137/090747634. That paper (card S010) reports total CPU seconds per mesh level (e.g. 3,402 s against 33,704 s at N = 50) and no per-iteration minutes [S010 p. 25]. The full-text scale claim is in the implementation note: "Specifically, the computation time for the largest instance with more than 600,000 variables was reduced from more than 6 days to 8.2 h, a speedup by a factor of 17.89." [S036 p. 17]. The research-page figure stays recorded as research-page only and not found in the full texts read.
- **Version note**: the dissertation's relative-residual baseline solves 50–86 % [S096 p. 52]; the 2008 paper's 45–86 % is confirmed for that version [S006 p. 17]. The skill keeps the 2008 figure (different versions of the experiment). The hybrid safeguard cost 0.5 extra GMRES iterations on average: "Indeed, the extra cost is minimal with respect to the added robustness." [S006 p. 18].
- **Variant (outer need is not always a merit model)**: a complexity inequality [S020 pp. 10–11, 16–17; S043 pp. 6–7; S053 pp. 6, 8; H001 pp. 4, 16], a step-size schedule [S037 p. 7; S056 p. 15], a sample-size schedule [S092 pp. 20, 24–26], a surrogate's accuracy δ = c·Δ² [S075 pp. 4, 10–11], or the information the outer Newton step needs (sensitivities): "we impose that the agents also return the sensitivity of their solution to changes in the price" [S077 p. 3; S071 TR pp. 5, 15]. Rule: derive the inner accuracy from whatever the outer proof or globalization consumes.
- **Contradiction, context-bound** (S094): in the competition team's SCOPF code, "The team also explored the application of various inexact solution methods but did not find that they provided a substantial enough speed improvement to make up for the decrease in accuracy." [S094 p. 5] (team report, unspecified methods, hard time limit): recorded as a limitation, not a reversal.
- **Limitations from the full texts**: "As mentioned at the end of Sect. 4.1, we have observed a decrease in effectiveness of the preconditioner as the barrier parameter approaches zero." [S036 p. 18]; "A drawback of the algorithm described in this paper is that it requires the inexact solution of the normal subproblem (2.2) in addition to the primal-dual system (2.6)." [S025 p. 25]; "Our approach fails more often, but this is to be expected, as our code is not as mature as IPOPT and an increase in iteration count often follows from the use of inexact Newton steps." [S010 p. 24].

---

<a id="method-2"></a>
## Method 2: Steer, don't switch

**Base-tier text (verbatim):**

#### Method 2: Steer, don't switch
**One line**: Keep one algorithm that moves between optimizing and minimizing constraint violation by itself, and make the rule that updates the penalty, merit or barrier parameter from predicted progress the contribution.
**Evidence**:
- Stated: "The key idea in this work is to carefully monitor progress toward constraint satisfaction, and to rapidly transition to minimizing constraint violation when consistent progress is not being made." (research page); "Our goal is to design a single optimization algorithm" that "does not switch between two separate techniques (e.g., no feasibility restoration as in Fletcher and Leyffer, 1997)" (INFORMS OS 2008, slide 5, joint); PIPAL's novelty lies in "the design of updates for the penalty and interior-point parameters" (10.1007/s12532-012-0041-4, p. 181).
- Practice: flexible penalty (10.1093/imanum/drn003); infeasibility detection (10.1137/080738222); PIPAL; SQuID (10.1137/120880045); adaptive augmented Lagrangian (10.1007/s10107-014-0784-y); updates inside the QP solve (10.1137/18M1176488); merit parameter in stochastic SQP (10.1137/20M1354556).
- Observed: "Penalty methods will converge only if the penalty parameter is sufficiently large. However, estimating this value is difficult" (Hinder & Ye, arXiv:1801.03072, p. 2, citing PIPAL).
- Say–do consistency: ✅ stated + practised 2008–2021. ⚠️ His own contrary data (Tension 4) and his post-2024 turn against penalties (Tension 3).
**Steps**:
1. List every parameter that trades objective against feasibility: penalty ρ, merit τ, barrier μ, radius.
2. Write each update as a test on model-predicted progress toward feasibility and optimality.
3. Allow the update inside the iteration, even inside the QP solve, not after a failed step; PIPAL tries a few candidate (ρ, μ) values per iteration (03 PE14).
4. Require, and prove, fast local convergence to an infeasible stationary point: "fast local convergence guarantees regardless of whether a problem is feasible or infeasible" (10.1137/080738222, p. 2281).
5. Instrument the rule: tabulate final parameter values over the test set (PIPAL Table 3; 03 PE17); classify parameter "events" (01 SW5).
6. Count the subproblem solves the rule costs per iteration and make that the next target (Heuristic 2).
**Applies to stage**: algorithm design; diagnosing infeasible and degenerate failures.
**Different from standard practice**: filter and restoration methods switch to a separate feasibility phase; classical penalty methods raise ρ on a schedule. Here the update rule itself is the research object.
**Limitations**: tied to the penalty family; the merit parameter's bad events are argued rare rather than removed (05 K2); his own data favour a filter on some infeasible problems; evidence is mostly small problems in Matlab.

**Full-text evidence (2026-10-10).** Cards linked: 54 (53 works): 20 evidence ✅, 37 variant ⚠, 1 contradiction ✗ (S089). Abstract-level link: S055.

- **Strongest practice**: the update rules are the whole contribution in the flexible penalty paper [S032 pp. 9–11] and the dissertation chapter behind it [S096 pp. 85–89]; steering plus a penalty update tied to the squared KKT error for the fast infeasible rate [S009 pp. 2, 13–14]: "In summary, by using the structured Hessian approximation (2.4), a penalty SQP method will achieve a fast rate of convergence simply by driving the penalty parameter to zero fast enough in a neighborhood of an infeasible stationary point." [S009 p. 11]; in-iteration (ρ, μ) updates with final ρ tabulated [S033 pp. 1, 13–17, 24]: "After all, in the context of Algorithm 1, each distinct value for the penalty parameter ρ potentially requires the computational efforts of a complete run of a standard interior-point algorithm." [S033 p. 12]; SQuID proves step 4, fast local convergence to infeasible stationary points [S022 pp. 2, 7, 25–27]; steering carried into augmented Lagrangians, inside the trust-region iteration, with Lancelot's iteration log showing that penalty-only iterations dominate [S019 pp. 5, 9–10, 35–38, 40; S040 pp. 2, 4–9, 12, 14, 19]; the update moved inside the QP solve [S057 pp. 9, 14, 23]; the stochastic line keeps an adaptive merit parameter and organizes its analysis around it [S007 pp. 6, 20, 24–26; S021 pp. 5, 7, 10, 19, 22–25; S030 pp. 7–8, 23; S013 pp. 3, 6, 11, 29]; a 2025 constrained proximal-gradient method steers τ from predicted linearized-infeasibility decrease [S082 pp. 2, 4–6, 11–14].
- **Stated in full texts**: "Thus, our view is that the main weakness of penalty-based strategies is the blocking effect illustrated in Fig. 3" [S032 p. 4; first in S096 p. 78]; "This strategy represents a stark contrast to previously proposed techniques that only update the penalty parameter after a sequence of iterations, in hindsight at the end of an iteration [1, 9, 10], or at the expense of numerous subproblem solves within a single iteration [3, 5, 7]." [S057 p. 2]; "While key to the practical performance of the algorithm, the adaptivity of the merit parameter introduced a number of theoretical challenges to overcome." [S013 p. 29]; "This suggests that the initial value for πu is inconsequential compared to the effect that separate updating strategies for πl and πu have on the practical performance of the approach." [S032 p. 18].
- **Proof device**: prove the adaptive parameter freezes after finitely many changes [S032 pp. 14–15; S057 pp. 13–14; S007 pp. 12, 16; S021 pp. 11–12].
- **Say–do**: ✅ for 2007–2025, with two qualifications.
- **Variant C10 (progress uncomputable)**: when the progress test cannot be computed (stochastic interior-point methods), steering gives way to prescribed barrier schedules: "This is significant since stationarity measures cannot be computed accurately in the stochastic setting that we consider." [S044 p. 3; D002 pp. 3, 6, 24–25; S063 pp. 6–9]; the merit parameter is frozen for the analysis and checked constant in runs [S054 pp. 7, 21].
- **Variant (scope)**: 15 cards apply an adaptive rule driven by an observed quantity (progress, or curvature as in S042) to non-penalty objects, e.g. [S024 pp. 3, 13, 16; S028 pp. 2–4; S067 pp. 7–8; S042 pp. 2, 5, 11; S064 p. 12; S002 pp. 7–9; S008 pp. 2, 21; S047 pp. 3–5; S050 arXiv p. 5]. These moved to the guarded-incumbent item ([below](#method-6), now Heuristic 5); Method 2 keeps the objective–feasibility trade-off.
- **Contradiction (S089) and Tension 3**: fairness constraints handled by a penalty raised ×10 every 400 iterations [S089 p. 6]; a penalty weight as a user knob swept on a grid [S069 pp. 8–10]; two algorithm papers fix the merit or penalty parameter by constants from the analysis [S068 pp. 5, 10–11; S087 pp. 9, 25]. See [Inner tensions](#inner-tensions).

---

<a id="method-3"></a>
## Method 3: Break it on purpose

**Base-tier text (verbatim):**

#### Method 3: Break it on purpose
**One line**: Do not wait for hard test problems: turn a standard set into infeasible and degenerate variants by a mechanical rule, run every solver on them with presolve off, and say how narrow the construction is.
**Evidence**:
- Stated: the research-page "often overlooked" passage (Taste 1); the ISMP 2018 epigraph; "(We want your infeasible test problems!)" (SIAM Optimization 2011 slides, slide 6/35).
- Practice: constructed variants in 2010, 2012 and 2020 (03 PE1); the 2020 paper added its infeasible set in revision (03 PE24).
- Result: on the standard set "PIPAL-a and especially IPOPT have an edge in terms of efficiency"; on the degenerate variants "IPOPT is not only less efficient than both PIPAL-c and PIPAL-a, but it also lags slightly in terms of robustness" (10.1007/s12532-012-0041-4, pp. 204–205).
- Say–do consistency: ✅ stated + practised 2010–2020.
**Steps**:
1. Take a standard set (Hock–Schittkowski in CUTEr/AMPL then; CUTEst now).
2. Degenerate variant: add −c_i(x)² ≤ 0 for each constraint. Infeasible: add c_i(x)² ≤ −1 (PIPAL kept those "solved by at least one of the algorithms", pp. 205–206; Heuristic 7). Or "we modified the 126 CUTEr Hock-Schittkowski (hs) problems by adding bound constraints x1≤ 0 and x1≥ 1 to make all hs problems infeasible" (arXiv:1803.09224 v3, p. 28), or make one application model infeasible (`robot` with c4 = c1² + 1; 10.1137/080738222, p. 2295).
3. Turn presolve off "so as to test the algorithms on difficult constraint sets" (PIPAL, p. 202).
4. Add two- or three-variable toy models ("s.t. c: 1 <= 0;", "s.t. c: y^2 + 1 <= 0;") and record which solvers declare infeasibility (2011 slides: ten solvers).
5. State what is not covered: "We admit that creating instances in this manner only produces a certain type of degeneracy" (PIPAL, p. 205).
6. Ask users for their failing models.
**Applies to stage**: problem choice; experiment design.
**Different from standard practice**: most NLP papers report the standard set only; here hard instances are manufactured and reported separately.
**Limitations**: small problems; one kind of degeneracy (no MPCC-type or redundant-equality variants).

**Full-text evidence (2026-10-10).** Cards linked: 30 (30 works): 10 evidence ✅, 20 variant ⚠, 0 contradictions.

- **Strongest practice**: rank-deficient and infeasible variants of every equality test problem by adding c₁ − c₁² = 0 or = 1, already in 2009 [S025 pp. 22–23] ("We admit that by testing small problems we do not illustrate the benefits of a matrix-free approach" [S025 p. 22]); infeasible variants of application models plus toy problems [S009 pp. 14–16]; PIPAL's degenerate (−cᵢ² ≤ 0) and infeasible (cᵢ² ≤ −1) HS variants with presolve off and the narrowness admitted [S033 pp. 22, 25–26]; the infeasible HS copy made by adding x₁ ≤ 0 and x₁ ≥ 1, already in 2014 [S022 p. 30] and again in 2020 [S057 p. 28]; degenerate instances made by duplicating the last constraint in CUTEst and in logistic-regression constraints [S021 pp. 27–28]; minimal hand-built counterexamples for active-set methods [S024 pp. 11–17; S067 p. 7]; intentionally degenerate QPs reported separately [S064 pp. 18–19]; presolve off on purpose: "We disabled the AMPL presolve feature to maintain the idiosyncrasies of each formulation." [S029 p. 29].
- **Corrections C3, C4**: the skill dated the constructed variants to 2010, 2012 and 2020 and attributed the x₁-bounds construction to arXiv:1803.09224. The full texts show 2009 [S025 pp. 22–23] and 2014 [S022 p. 30]. The limitation *one kind of degeneracy (no MPCC-type or redundant-equality variants)* is contradicted for redundant equalities: duplicated constraints are a redundant-equality variant [S021 pp. 27–28]. MPCC-type variants remain absent.
- **Say–do**: ✅; practice spans 2009–2024. After 2015 the deliberately broken object is more often a small counterexample in the theory than a test set [S015 pp. 4–5; S005 pp. 12, 14–15; S018 pp. 9, 28]: "We argue in this paper that employing normalized steps in all iterations cannot lead to general convergence guarantees, which perhaps explains the additional assumptions required for convergence by [12]." [S015 p. 3].
- **Variants**: planted-answer (known-answer) generators [S066 pp. 18–19; S065 p. 18; S082 p. 28; S088 pp. 15–17]; minimal theory counterexamples [S024 pp. 11–17; S067 p. 7; S015 pp. 4–5; S018 pp. 9, 28]; breaking the rival on paper before running it (predict the rival's failure, then show it) [S047 pp. 4, 6; S049 pp. 12, 18; S042 pp. 5–6; S070 pp. 4–5, 10; S044 pp. 22–23]; the same move aimed at the authors' own cheaper alternative, which the runs then did not confirm (on the degenerate instance it needed the fewest Krylov iterations, 7512 against 16797 and 11958) [S064 pp. 13–15, 18–19]: "This myopic choice may stagnate the algorithm as no step is taken in the dual space." [S047 p. 4]; "Such a choice fails to capture any information from the objective function, which may be detrimental to performance." [S042 p. 5].

---

<a id="method-4"></a>
## Method 4: Audit the yardstick

**Base-tier text (verbatim):**

#### Method 4: Audit the yardstick
**One line**: When a method looks better or worse than practice suggests, check whether the measure (complexity class, stationarity test, performance profile, success flag, test set) favours someone, and build a view that shows the hidden trade-off.
**Evidence**:
- Stated: "complexity bounds should be taken with a grain of salt" (Oaxaca 2017); "It is a mistake to overemphasize the relevance of this theory for practical use." (NeurIPS 2025 workshop plenary, on exact-penalty theory).
- Practice: relative minimization profiles (10.1080/10556788.2016.1208749); regional complexity (10.1007/s10107-020-01492-3); his student Que's success rule (Step 4).
- Observed: S. J. Wright on their joint Newton-CG work: "the modifications that are made to admit nonasymptotic theory do not improve the practical performance" (arXiv:2510.15734 v2, p. 23).
- Say–do consistency: ✅ stated + practised 2016–2021; ⚠️ applied unevenly to his own line (Inner Tensions 1, 2).
**Steps**:
1. Write down what the measure rewards and ask: "Who's to say these are appropriate?" (ECOM 2021 public lecture, slide 21/45).
2. Decide whether the gap lies in the method or in the measure: "might be showing a deficiency of the characterization strategy" (ISMP 2018).
3. Name the trade-off the measure hides (objective versus feasibility versus budget for constrained problems) and build a view that shows it: relative minimization profiles, or analysis split by region.
4. Do not let your own termination flag decide success: "if we only considered a termination flag of type (1) to be the indicator for a successful run, then the profiles would be skewed in favor of the codes that yielded such a flag most often (namely, ours)" (Que thesis 2016; 04 T2). Judge by solution quality; report flags separately.
5. Present the data so the reader decides: "evaluators should aim not to define success but present as much relevant benchmark data as possible in a concise and intuitive manner" (10.1080/10556788.2016.1208749).
6. Weigh theory by method class: "Some methods actually behave like their worst-case; others don't." (ISMP 2018)
**Applies to stage**: judging results; reviewing; choosing between methods.
**Different from standard practice**: algorithm designers rarely build evaluation tools or question their own yardstick.
**Limitations**: easier to preach than to apply to one's own line; relative minimization profiles were built for nonsmooth multi-run comparisons and need adapting to smooth NLP.

**Full-text evidence (2026-10-10).** Cards linked: 51 (51 works): 32 evidence ✅, 18 variant ⚠, 2 contradictions ✗ (S026, S066).

- **Strongest practice**: relative minimization profiles built because profiles hide the objective–feasibility–budget trade-off, with "evaluators should aim not to define success but present as much relevant benchmark data as possible in a concise and intuitive manner" [S004 p. 18] and β-panels at BFGS-SQP's own per-problem time, the panels at the faster rivals' budgets being omitted and summarised in prose [S004 pp. 19–22, 25–26]; termination flags distrusted because they would favour the authors' code, with an algorithm-independent ε-stationarity estimate [S008 pp. 24–27]; regional complexity [S062 pp. 3–4, 18–22]; an own complexity device priced in runs [S020 pp. 4, 21–22]; rates converted into total work before methods are ranked [S001 pp. 34–37, 43–44, 49]; a fairness surrogate audited against the true measure [S083 pp. 2, 6–7, 10–12]; stationarity reported on noiseless values with the solver's own termination off [S059 pp. 33–35]; quality judged against known optimal values, not flags [S088 pp. 17–20]: "Perhaps the most challenging issue when it comes to the implementation of a general-purpose algorithm for locally Lipschitz minimization is selecting effective termination criteria." [S088 p. 17].
- **Stated in full texts**: "Such questions are not answered well by contemporary worst-case results, which are too conservative." and "RC analysis can be used to guide the design of new algorithms." [S062 p. 4]; "Based on such evidence, we do not claim that the convergence results proved in this paper fully capture the practical behavior of LMSD methods." [S046 p. 3]; "This would likely lead to very poor behavior in practice compared to the strategies in Sections 2.3 and 2.4, which are much less conservative." [S035 p. 9]; "That said, we found it to be the best measure for comparison, as opposed to CPU time which can vary despite the algorithm being run with the same initial conditions, random number generator seeds, and so on." [S065 p. 19].
- **Correction C2 (source)**: step 4 quoted "if we only considered a termination flag of type (1) …" from the Que thesis 2016. The same sentence is in the 2015 journal paper: "if we only considered a termination flag of type (1) to be the indicator for a successful run, then the profiles would be skewed in favor of the codes that yielded such a flag most often" [S008 p. 25]. S008 is the primary source; likewise Heuristic 6's CPU-time sentence is in [S008 p. 24].
- **Say–do**: ✅, with the audit visible inside papers from 2015 [S008 pp. 24–27] and 2018 [S035 pp. 8–9; S046 p. 3], not only in talks. ⚠ The 2017–2018 complexity papers adopt the yardstick unaudited [S002 pp. 2–3; S026 pp. 1, 26–28]: "This is due to the fact that, at least for convex optimization, algorithms designed with complexity bounds in mind have led to methods with improved practical performance." [S026 p. 1]. S066's success test is its own residual [S066 pp. 19–20, 36].
- **Variant (speed–accuracy as a user dial)**: [S088 pp. 15, 19–20; S043 pp. 3, 23–24]: "In particular, with more exact subproblem solutions, our algorithm often requires fewer derivative evaluations at the expense of more Hessian-vector products, whereas with more inexact subproblem solutions, it often requires fewer Hessian-vector products at the expense of more derivative evaluations." [S043 p. 3].
- **Variant (match the incumbent's theorem, win in the experiments)**: [S015 pp. 3, 9–10, 23; S090 pp. 3, 7, 11; S007 pp. 4, 8–13; S030 p. 8].

---

<a id="method-5"></a>
## Method 5: Fair-fight benchmarking

**Base-tier text (verbatim):**

#### Method 5: Fair-fight benchmarking
**One line**: Make the comparison test the idea, not the plumbing: the rival lives in your framework with one component varied, the incumbent's engineering is adopted, the baseline is favoured with the handicap stated, and the incumbent's wins are printed.
**Evidence**:
- Stated: "Fair comparison would" not ignore tuning time and would "involve many runs of each algorithm" (Oaxaca 2017, slide 33/33); "Hard to beat a highly tuned state-of-the-art solver! Curtis (2012)" and "I’ve seen many papers rejected for this reason." (ECOM 2021 public lecture, slide 37/45).
- Practice: 03 PE6–PE11, PE27, 2008–2022.
- Say–do consistency: ✅ stated + practised, improving after about 2018. ⚠️ Parameters tuned on the evaluation set without reporting the effort (2012, 2012, 2019; 03 PE13); a randomized method reported from single runs (2019; 03 PE15).
**Steps**:
1. Put algorithm variants in one framework as strategy objects (NonOpt's direction, step-size and QP-solver classes; 03 PE33).
2. Build the rival as another strategy: ARC beside i-TRACE, "all of the algorithms were implemented in a single software package in Matlab" (arXiv:2204.11322); GS-exact is GS-inexact with the QP solved to 10⁻¹⁰ (arXiv:2005.07822).
3. Ablate the one component the claim is about: p = 0 sampled gradients in SQP-GS, "providing strong evidence that the GS procedure is critical for the effectiveness of our approach" (10.1137/090780201); a delete-instead-of-aggregate arm that "shows the effect of aggregation itself" (arXiv:1903.03471).
4. Against an external code, adopt its engineering first: PIPAL copied Ipopt's bound relaxation, initial point, gradient scaling, second-order correction and evaluation-error handling "for the purpose of providing a fairer comparison" (03 PE8).
5. Favour the baseline and put the handicap in numbers: "“Stochastic Subgradient” was given 110 times the number of iterations that were allowed for “Stochastic SQP.”" (arXiv:2007.10525 v1); tuning that "did not require more effort than the tuning used for the SG method" (arXiv:1712.10277).
6. Time-match the external state of the art and average over runs (CPU limit = LMBM's average time, 10 runs; 03 PE11).
7. Print where the incumbent wins and narrow the claim (PIPAL's Ipopt result, Method 3); "LMBM yields lower values for some problems while GS-inexact-agg yields lower values for a few others" (arXiv:2005.07822 v2).
**Applies to stage**: experiment design; judging results; writing.
**Different from standard practice**: ablations are common; building the rival inside your own framework, importing the incumbent's engineering and paying the baseline 110× are not.
**Limitations**: in-framework rivals are reimplementations, not the production code; tuning effort goes unreported in several papers; one nonsmooth test set reused 2018–2025.

**Full-text evidence (2026-10-10).** Cards linked: 78 (74 works): 47 evidence ✅, 39 variant ⚠, 9 contradictions ✗. Abstract-level links: S031, S045, S060.

- **Strongest practice**: rivals as one-switch variants of one code from the start [S047 pp. 6–8; S096 pp. 51, 72–73, 95; S006 pp. 16–17; S017 pp. 22–24]; the incumbent as a parameter setting [S012 pp. 5, 18–19]; Ipopt's engineering imported to make the comparison fairer [S033 pp. 12, 17, 20–21]; Lancelot's options aligned and an in-house baseline calibrated against it before any claim, "All together, we believe that these experiments are the best way to isolate and measure the performance of our adaptive penalty parameter updating procedure." [S019 pp. 34–39]; the production code changed only in steering, "In this manner, we were also able to isolate the effect that steering had on numerical performance" [S040 p. 10]; equal tuning effort stated and done [S015 pp. 18–19, 22; S041 pp. 5, 21–24]; a baseline given 110× the iterations [S007 p. 27] and later 440× [S021 pp. 25–30]; LMBM time-matched over 10 runs with its wins printed [S065 pp. 17, 20–21]; strategies as interchangeable objects [S088 pp. 7–9, 12, 26]; "The three implemented algorithms differed only in the manner in which step sizes were computed." [S042 p. 16]; "Consequently, the comparison between the second and third algorithms shows the effect of aggregation itself, rather than only the difference between removing the oldest versus some other historical pair in an L-BFGS scheme." [S051 p. 22]; "Our reason for comparing these two variants is to focus attention on the numerical gains obtained as a result of using inexact subproblem solutions." [S037 p. 22].
- **Stated in full texts**: "We took care to make sure that the tuning procedure for TRish did not require more effort than the tuning used for the SG method that we have for comparison purposes." [S015 p. 18]; "To ensure that all algorithms were tuned with the same amount of effort, we fixed the total number of hyperparameter settings to be the same for all algorithms." [S041 p. 22]; "Tuning these parameters means that problems cannot be solved once; they need to be solved numerous times" [D001 p. 2]; the incumbent's strength conceded: "Our experiments support the claim that when an interior-point method is performing at its best, it is difficult to outperform such an approach in terms of efficiency." [S033 p. 28]; "(On a contemporary laptop to computer, the state-of-the-art code Ipopt [17] solves problem LUKVLE10 in only a couple of seconds, but that code benefits from two decades of software development.)" [S057 p. 29].
- **Say–do (C5; changes *improving after about 2018*)**: the split is by **paper type**, not by period. Equal-budget tuning is a habit of the stochastic and ML comparisons from 2016 on [S015 p. 18; S041 p. 22; S083 pp. 27–30; S090 p. 23], not without lapses: S028 gives every method the same step-size grids but takes the best of each grid on test loss from one run per setting [S028 p. 6]. In deterministic algorithm papers, parameters chosen on the evaluation runs without a reported tuning effort recur from 2007 to 2026 [S096 pp. 56–58; S003 p. 18; S033 p. 21; S012 p. 18; S008 pp. 20–21; S024 p. 20; S064 p. 17; H001 p. 17; S070 p. 11; S044 pp. 24–25; S088 p. 14] ("The remaining values were decided upon during the course of our experiments." [S003 p. 18]). No paper counts tuning time. (S088 p. 22 tunes the denoising model's (λ, β) per instance over a reported grid (2^i, 2^j), (i, j) ∈ [−20, 25]²: problem-parameter selection with a stated budget, not algorithm tuning, so it is not counted here.) Theory-led papers often run no external rival, usually with a stated reason [S039 p. 44; D002 p. 24; S063 p. 30; S088 p. 14]: "meaning that there is no such method in the literature against which our algorithm can be compared on a level playing field." [D002 p. 24]; "However, since NonOpt performed favorably in these comparisons, LMBM is no longer under active development" [S088 p. 14]. ✅ for steps 1–4 and 7; ⚠ for steps 5–6, dated 2007–2026.
- **Contradictions (9)**: theory-first papers with no comparison [S039 p. 44] or no external rival with the reason given [S091 pp. 4, 16–22; S088 p. 14]; application and collaboration papers: no rival controller run [S048 pp. 6, 11], external baselines delegated to other papers and no repeated runs [S056 pp. 16–20], one dataset, two clients, penalty value chosen on test results [S069 pp. 5, 9–12] (cross-community collaborations with new co-authors, which weigh less on the solver methods); algorithm papers: the main rival's numbers taken from its paper instead of a rerun [S057 pp. 27–29], an outcome-filtered test set and 5 runs [S037 pp. 23–25], parameters chosen on testing-set results with the run count not stated [S076 pp. 15–18], looser tolerances for the new method, cross-language timing, single runs and a solver-success filter without the pre-filter count [S082 pp. 27–29].
- **Variants**: an externally fixed yardstick: competition rules, unseen instances, fixed hardware, a worst-case fallback score [S023 pp. 17–22; S061 pp. 2, 6–7]: "Finally, since implementation quality was of utmost importance to avoid “worst-case” scores from code failures, the benchmark results from the competition may overlook alternative algorithms that could have performed better if they had more robust implementations or had better exploited the parallel computing resources." [S023 p. 26]; comparison on the subset where the mechanism fired [S033 p. 24; S014 pp. 14–15]; fairness of rivals stated: "For a fair comparison, we include symmetry-breaking constraints for all models." [S034 p. 47]; "(for our tests, nonetheless, we fine-tuned the step size for PStorm to be fair)" is part of [S070 p. 31].

---

<a id="method-6"></a>
## Guard the incumbent; let the guarantee sleep (drafted as Method 6; kept as Heuristic 5)

New on 2026-10-10 (proposed for promotion in 08 §4); no base-tier text. **Status after review (2026-10-10): not a core method.** Recurrence, say–do and executability pass, exclusivity fails (row 4 below), which the extraction framework grades as a research heuristic. SKILL.md therefore keeps [Heuristic 5](#heuristic-5) in its base-tier slot and meaning and adds this construction to it as its full-text form, parts (i)–(iv): (i) reduce = step 2 below, (ii) trigger = step 3, (iii) count = step 4, (iv) price = step 5. The evidence below is kept in full.

**Cluster.** Merged from the round-1 candidates *reduce-to-predecessor / reduce-to-incumbent design*, *minimal-intervention / dormant safeguard*, *cheap default with guaranteed fallback*, *contain the incumbent's choice*, *incumbent as a parameter setting*, *nest the classical method*, *price the guarantee* and *safeguard-as-arm*; every card describes the same construction from one of two sides. **21 distinct full cards, 2007–2026, no listed journal/preprint pair among them** (S096's nonconvexity chapter, pp. 59 ff., is plausibly the thesis form of S017; not compared, so count 20 works if they merge): S047, S096, S010, S017, S003, S033, S036, S012, S024, S067, S008, S028, S042, S027, S040, H001, S051, S020, S014, S087, S029 (the last as a stated partial case).

**Four-way validation.**

| Check | Result | Evidence |
|---|---|---|
| 1 Cross-project recurrence | ✅ (seven lines: IPM step lengths, inexact SQP/IPM, penalty-IPM, nonsmooth BFGS/GS, active-set QP and isotonic regression, stochastic quasi-Newton, trust-region complexity) | search set containing the incumbent's choice [S047 pp. 4–5]; reduces to the predecessor in convex regions [S017 p. 2] or in a rescaled space [S010 pp. 5, 11–12]; p = 0 gives Sℓ1QP and m = 0 gradient sampling [S003 p. 9]; GS a parameter setting of AGS [S012 p. 5]; M = N recovers Sℓ1QP [S027 p. 11]; the m = 1 rule recovered [S042 pp. 2, 13]; ARC and TRACE as instances [H001 pp. 14–16]; exact BFGS reproduced before relaxation [S051 p. 20]; SG recovered at β = 0 [S014 p. 22]; the eigenstep test never fires so the method reduces to gradient descent [S087 pp. 13–14]; dormant guards: sampling and bounded L-BFGS only when tests fail [S008 pp. 2, 11, 13]; an only-growing safeguard set U [S024 pp. 3, 13–14, 18, 21–23]; a fraction p of violators [S067 pp. 7–8]; the smallest damping β_k [S028 pp. 3–4]; fallback to the conservative direction [S033 pp. 18–19]; the regularized step only when the steplength collapses [S036 pp. 9–10]; typed CG exits wake the eigenvalue oracle [S020 pp. 10–15]; accept before repairing [S096 pp. 62–63] |
| 2 Say–do consistency | ✅ (stated in the papers as the design intent; practised in the algorithm boxes and experiments) | "A feature critical to the practical performance of our algorithm is that, when it is applied to solve many problem instances, the algorithm reduces to an unadulterated BFGS strategy for the majority of the iterations." [S008 p. 2]; "The resulting algorithm fully integrates the procedures of step computation and step selection and automatically reduces to an inexact SQP method in convex regions of the search space." [S017 p. 2]; "We stress, however, that while the proof relies on such worst-case behavior, we have never witnessed such an occurrence in practice." [S024 p. 14]; "This shows that our proposed safeguard, which allows more aggressive updates, can be more effective than a conservative safeguard." [S067 p. 10]; on the price: "Across the board, our results indicate that safeguarding was not necessary and would typically degrade performance when compared to the unrestricted steering approach." [S040 p. 20]; "The variants with no regularization term in the subproblems outperform the others in this respect; recall that these variants do not possess optimal complexity guarantees." [S020 p. 22] |
| 3 Executable, different from standard practice | ✅ | The alternatives the papers set themselves against are the two standard moves: an always-on safeguard (equal step lengths [S047 p. 2]; always-regularized steps [S036 p. 12]; sampling every iteration [S008 pp. 2–3]; a conservative one-index fallback [S067 p. 8]; fixed regularization of BFGS [S028 p. 2]) or a switch from the fast method to a guaranteed one after it stalls (HANSO's BFGS-then-GS [S008 p. 21]). Here the guarantee is attached to the incumbent, triggered by the quantity the proof needs, and priced by running the guarantee-free twin [S036 p. 12; S012 pp. 18, 20–21; S040 pp. 13–14, 19–20; S020 pp. 21–22]. "Empirical evidence has shown, however, that this approach is unnecessarily conservative in numerous cases." [S047 p. 2] |
| 4 Exclusivity | ✗ (fails at team level) | Checked at review against the teammates' SKILL.md methods: Wright Method 4 ("Minimal safeguard with a no-safeguard twin": keep the practitioners' method, add only the safeguards a guarantee needs, run the twin without them, price the guarantee) is nearly this method; Fletcher Method 1 ("Let the unmodified method run (minimal-interference safeguarding)"), Toint Method 3 ("the least obstructive acceptance mechanism, measured against free Newton") and Wächter Method 2 ("Ablate your own safeguards against an unguarded Newton run") share the core move. In the wider field, safeguards that fire only when needed are also standard (damped BFGS updates, inertia correction on failure, hybrid fallbacks such as HANSO's). What the cards show that the teammates' methods do not state is narrower: (a) the reduction to the incumbent written into the design and used as a proof device that inherits the predecessor's theory by citation [S010 pp. 11–12; S017 p. 18; S042 p. 16; S051 p. 20], with (c) the guard's activity tabulated [S024 pp. 21–23; S017 pp. 21–22]. That residue is recorded under Heuristic 5 (i) and the Roundtable Card (*Shared, not distinctive*); it is not enough for a separate core method. Earlier wording of this row ("✅ with the boundary stated"; teammates "cannot be checked in full texts") is superseded: their SKILL.md methods can be read, and they overlap. |

**Price measured**: 84 % against 89 % of CUTE solved by the always-guaranteed variant against the switching implementation, which wakes the robust step only when the steplength collapses [S036 pp. 9–12]; guarantee-free Hessian variants no better [S012 pp. 18, 20–21]; safeguarded steering worse [S040 p. 20] (a dormant threshold cutoff on steering, so this is counter-evidence for the dormant guard itself, not a price of a guarantee; the safe arm carried the same theory [S040 pp. 10, 13–14]); regularization-free variants better in Hessian-vector products [S020 p. 22]; "we expect the “cap” of Algorithm 2 to be triggered only in rare cases, due to the conservative nature of the CG convergence bounds that gave rise to this cap." [S020 p. 20].

**Full Steps (as drafted in 08 §4; SKILL.md keeps up to three references per step)**:
1. Name the incumbent users already trust and the one property it lacks (a guarantee, robustness under negative curvature or nonsmoothness) [S008 p. 2; S042 pp. 2, 5; S024 pp. 3, 27–29].
2. Design so that an idle test or one parameter value gives back the incumbent exactly, and say which [S003 p. 9; S012 p. 5; S027 p. 11; S017 p. 2]; or search over a set that contains the incumbent's choice, so that doing no worse than the incumbent holds by inclusion [S047 pp. 4–5]. Where possible, inherit the incumbent's theory through the reduction instead of re-proving it [S010 pp. 11–12; S017 p. 18; S051 p. 20].
3. Trigger the guard on the quantity the proof needs and make the intervention the smallest that restores it: a steplength floor [S036 pp. 9–10], a curvature test [S008 pp. 11, 13], the smallest damping weight [S028 pp. 3–4], a fraction of the violators [S067 pp. 7–8], a set that only grows [S024 pp. 13–14], a typed inner-solver exit [S020 pp. 10–15]; test the current step before repairing anything [S096 pp. 62–63].
4. Tabulate how often the guard fired and how far it grew (→ H1) [S024 pp. 21–23; S017 pp. 21–22; S020 p. 20].
5. Run the guarantee-free twin in the same code and report the price of the guarantee (→ Method 5 step 3, ablating the guarantee rather than the novelty) [S036 p. 12; S020 pp. 21–22]; review correction: run both the guard-always-on arm (the one S036 reports, 84 % against 89 %) and the guard-off arm; S040's safe arm tests a safeguard as its own arm [S040 pp. 13–14, 19–20] and does not price a guarantee.
6. Say where the reduction is partial or the code leaves the analysed range [S029 p. 8; S008 p. 20].

**Variants**: old Heuristic 5's trail in date order: SQP-GS [S003 p. 18] → BFGS-SQP with "no convergence guarantees" [S004 p. 2] → the guaranteed variable-metric framework [S049 p. 12]; the 2015 unconstrained guarded hybrid [S008 pp. 2, 21] predates BFGS-SQP; order reversed (exact scheme first, practical heuristic second) [S051 pp. 20, 22, 25]; guarantees given to someone else's fast scheme: "Although computational results from [13] suggest an improvement in solution time by adopting their proposed scheme, the work did not provide theoretical guarantees concerning the accuracy and convergence of the proposed modification of C&CG." [S016 p. 2; S016 p. 8].

**Why not merged into an existing item**:
- *Method 2* is about the parameter that trades objective against feasibility; its one line cannot hold Hessian damping, sampling, step-size rules or active-set safeguards, which is why the readers filed 15 such cards as Method 2 variants without a penalty or merit parameter. Where both apply (PIPAL-a and PIPAL-c [S033 pp. 18–19]; the flexible penalty with a switching step computation [S036 pp. 9–11]), Method 2 designs the parameter rule and the guarded incumbent (Heuristic 5) the fallback.
- *Heuristic 10* applies when the information model changes; the guarded incumbent applies with unchanged information (the 2007–2016 cases above).
- *Heuristic 2* (count the safeguard's extra solves) stays as the cost ladder; Heuristic 5 (iii) reports the guard's activity, H2 its per-iteration cost.
- *Taste 3* gains its operational form outside the penalty family.

**Limitations**: the code often runs the guard outside the analysed parameter range [S008 p. 20]; the reduction can be partial [S029 p. 8]; trigger parameters are set on the test set without a reported tuning effort [S024 p. 20; S064 p. 17]; worst-case trigger behaviour is argued rare rather than measured in some papers [S024 p. 14]; evidence is mostly small problems in Matlab prototypes. Exclusivity was argued from the contrasts the papers draw [S008 p. 21; S036 p. 12; S067 p. 8; S028 p. 2]; at review it failed against the Wright, Fletcher, Toint and Wächter seats (row 4).

---

<a id="workflows"></a>
## Stage workflows

**Base-tier text (verbatim):**

#### Stage Workflows

#### Workflow A: Problem choice
**Input**: the solver's failures and slowdowns, by problem class (none given → next step 1 is a status-code count on the user's test set plus the Method 3 variants).
**Steps**:
1. Sort failures by his list, "“high” nonlinearity, degeneracy, and infeasibility", plus scale that defeats factorization (→ Heuristic 3); sort slowdowns by his 2015 list (SIAM CSE 2015, slide 5 of 25; method mapping inferred): "exact subproblem solves are expensive" / ". . . or inexact solves are not computed intelligently" (→ Method 1); "algorithmic parameters are initialized poorly" / ". . . or are updated too slowly or inappropriately" (→ Method 2); "a globalization mechanism inhibits productive early steps" / ". . . or blocks superlinear local convergence" (→ Method 2 step 5; a lost local rate: weak-spot rule). Open request: take the one or two classes with the most failing instances; at most three ideas.
2. Keep a failure that theory treats as a corner case (→ Taste 1).
3. Reproduce it on a tiny constructed model and on a mechanically built variant of a standard set (→ Method 3).
4. Write the desiderata the repaired solver must meet (→ Heuristic 4).
**🔴 Checkpoint**: if the failure cannot be reproduced on a constructed instance, or vanishes once the incumbent's own engineering (scaling, bound relaxation, presolve) is on, stop: it is plumbing, not a research problem.
**Output**: a one-page statement: failure mode, constructed instances, desiderata.

#### Workflow B: Algorithm design
**Input**: the Workflow A statement and the current algorithm skeleton; with no statement, the user's failure description, and writing the statement is next step 1.
**Steps**:
1. Derive inner-solver termination tests from the outer acceptance condition (→ Method 1).
2. Express every objective-versus-feasibility parameter as an update rule on predicted progress, inside one iteration (→ Method 2).
3. If the information model changes (inexact, nonsmooth, noisy, sampled), build the deterministic twin first (→ Heuristic 10).
4. Count the per-iteration cost of each safeguard (→ Heuristic 2).
**🔴 Checkpoint**: if the design needs a second phase (restoration, restart) to converge (his preference; state Tension 4), or a safeguard costs more than one extra subproblem solve per iteration with no plan to remove it, redesign before experimenting.
**Output**: algorithm statement; table of parameters, update rules, termination tests, costs.

#### Workflow C: Experiment design
**Input**: a working prototype; if its variants are not strategy objects, next step 1 is an option or build flag that changes only the component under test.
**Steps**:
1. Build the rival inside the framework and ablate the one component the claim is about (→ Method 5).
2. Add infeasible and degenerate variants and toy models, presolve off (→ Method 3).
3. Adopt an external code's engineering before comparing with it (→ Method 5, step 4).
4. Write the exclusion log and encode filters in code (→ Heuristic 7).
5. Give the baseline the tuning advantage and record it; seeds and at least 10 runs for anything randomized (→ Method 5).
**🔴 Checkpoint**: stop if the test set is filtered on something observed in the runs (a symmetric "no solver solved it" cut only with the pre-filter count), if success is decided by your own termination flag, or if the baseline is less tuned than your method. After stopping, fix the protocol and rerun; if the advantage survives nowhere, return to Workflow B, do not retune.
**Output**: a protocol: sets, variants, exclusions, rivals, settings, tuning budgets.

#### Workflow D: Judging results
**Input**: raw outputs.
**Steps**:
1. Look at one run at iteration level (→ Heuristic 8).
2. Measure how often the theory's event occurs; tabulate final parameter values and step types (→ Heuristic 1).
3. Pick the metric that exposes the mechanism (→ Heuristic 6).
4. Ask whether the measure favours you; view objective versus violation versus budget; weigh any complexity claim by method class (→ Method 4).
5. List where the incumbent wins (→ Method 5, step 7).
**🔴 Checkpoint**: if the advantage vanishes when the test set changes, or the theory's event is rare in runs, narrow the claim or return to Workflow B (his example: PIPAL, Method 3 result).
**Output**: a results memo: wins, losses, event frequencies, the narrowest honest claim; keep, narrow or drop.

#### Workflow S: Stuck project (triage before redesign)
Order inferred from Heuristics 9, 8, 1; not a recorded Curtis procedure.
**Input**: what was tried, for how long; one failing run's iteration log (none → reading one is next step 1).
**Steps**:
1. Freeze tolerance and constant sweeps until steps 2–4 are done (→ Workflow C checkpoint).
2. Run the derivative checker on the failing models and the test problems themselves (→ Heuristic 9).
3. Read that run at iteration level: which test rejects the step; when ρ, τ, μ or the radius moves; when restoration starts (→ Heuristic 8).
4. Count per iteration: inner-solve fallbacks, penalty increases, inertia corrections, restoration entries (→ Heuristic 1).
5. Name the class (Workflow A step 1): step rejected after an inner solve that met its tolerance → Method 1; a parameter runs to an extreme or restoration dominates → Method 2; the incumbent with its own engineering fails too → Method 3; the gain comes and goes with the test set or success flag → Method 4.
**🔴 Checkpoint**: a derivative or harness error in step 2 → fix, rerun, stop. No class in step 5 (factorization, preconditioner or inertia fails) → weak-spot rule (Gould, Wächter seats). Same class after one Workflow B redesign that fails Workflow D → narrow the scope to where it works; no more constant sweeps.
**Output**: plumbing verdict, rejecting test, event counts, class, the one redesign to try.

#### Workflow E: Writing and after publication
**Input**: the results memo and the code.
**Steps**:
1. Calibrate claims ("We do not claim that “SQP Adaptive” is as efficient as “SQP Backtracking”", arXiv:2007.10525 v1) and drop untested adjectives (titles lost "Robust" and "Large-Scale" in review; 03 PE29).
2. Ship a reproduction directory with raw outputs and runtimes (03 PE23); label code a prototype and invite bug reports (03 PE32).
3. Post corrigenda with the full corrected statement; contact the journal only when a main conclusion changes (Errata page; 03 PE26).
**🔴 Checkpoint**: untested scale claims and adjectives come out; a numerical claim without a reproduction path waits.
**Output**: paper, reproduction package, errata entry when needed.

**Techniques added on 2026-10-10** (technique inventory, 08 §7; catalog: `../technique-catalog.md`):
- A step 1: a fast heuristic users trust but cannot prove → Heuristic 5 (guarded-incumbent form, [above](#method-6)).
- B step 2: one factorization for many (ρ, μ) values, since they enter only the right-hand side [S033 p. 18]; B step 3: port the inequality, not the formula (Heuristic 11); B step 5: dormant guards [S036 pp. 9–10; S008 pp. 11, 13], with the reduction to the incumbent written down when one exists and a partial reduction stated [S029 p. 8] (review: the checkpoint clause "the method with its guards idle is not an incumbent you can name" was removed, since the works contain designs with no incumbent or a partial reduction [S029 p. 8; S044 p. 3; D002 pp. 3, 6]). B step 1, review addition for IPMs: rescale slacks to reuse the equality-case tests [S010 pp. 4–12]; the robust step only on a steplength floor [S036 pp. 9–10]; preconditioner tightening late in the run [S036 pp. 14–15, 18].
- C step 1: a naive floor and an idealized ceiling around the new method [S017 pp. 22–24]; the guard-always-on and guard-off arms (Heuristic 5 (iv)). C step 2: three layers, the full set, the subset where the mechanism fired and the constructed variants [S033 pp. 22–27]. C step 3: list each imported item with its source [S033 pp. 20–21]; calibrate an in-house incumbent against the mature code first [S019 pp. 34, 39]. C step 5: equal tuning budgets [S015 pp. 18–19, 22; S041 p. 22]. C step 6: algorithm-independent quality: fresh-sample ε-stationarity [S008 pp. 26–27]; true-gradient stationarity with least-squares multipliers [S007 p. 27; S037 p. 22]; noiseless measures with the solver's termination off [S059 pp. 33–35]; objective recomputed outside the solver [S061 p. 11]; convex test problems so that different local minimizers cannot skew the comparison [S065 p. 18].
- D step 2: show the theory's signature in the logs: last-ten-iteration residual slopes [S022 p. 31] ("One finds that many of the curves possess slopes of this type, providing empirical evidence for the convergence results in section 4." [S022 p. 31]); local signatures tabulated [S052 pp. 18–20]; proof quantities plotted [S046 pp. 15–19]; event frequencies [S007 p. 27]; theoretical rate overlaid [S070 pp. 13, 31–32]; binned accepted residual ratios show the inexactness was real [S029 p. 30]. D step 4: price each guarantee by its arms (Heuristic 5 (iv)).
- E step 1: limitations up front [D002 p. 3; S059 p. 4; S090 p. 3; S073 p. 3]; explicit non-claims [S007 p. 26; S014 p. 21; S046 p. 3]. E step 2: disclose and cap the theory–code gap (Heuristic 1). E step 4: correct a founding proof in public, naming who found the gap: "This oversight went unnoticed for 12 years until J. Portegies and T. Mitchell brought it to our attention recently." [S005 p. 5]. E checkpoint: the neutral lesson from the cards' reading notes (unattributed): recheck that prose summaries match the final tables after revisions.
- S steps 4–5: guard firings counted; a guard firing in most iterations points to Heuristic 5.
- Other writing moves available for E: the exact algorithm as scaffold before the inexact one, each test followed by the lemma that needs it [S029 pp. 8–12]; an obstacle section for the obvious simpler method, "Upon seeing our algorithm, a reader may wonder if a simpler variant has convergence guarantees." [S044 p. 3; S044 pp. 22–23]; when theory is weaker than the incumbent's, list the fixes and why they were not made [S019 p. 33].

---

<a id="heuristic-1"></a>
## Heuristic 1: log the theory's event; computable safeguards; disclose and cap the theory–code gap

**Base-tier text (verbatim):** 1. **If** your analysis conditions on an event, **then** log how often it occurs, with step types and final parameter values; replace uncheckable conditions by computable safeguards. Case: the stochastic SQP event held in 99.10–99.92 % of iterations, "This provides evidence that the theory offered under the event (25) is relevant in practice." (arXiv:2007.10525 v1); "The conditions in this theorem cannot be verified in practice." (Google 2016 talk).

**Full-text evidence**: event frequency logged [S007 p. 27; S021 pp. 27, 29]; "This provides evidence for our claim that the merit parameter not reaching a sufficiently small value is not an issue of practical concern." [S021 p. 27]; frozen parameters checked in runs [S054 pp. 7, 21]; safeguard activity tabulated [S024 pp. 21–23]; branch percentages per test [S017 pp. 21–22]; analysis assumptions recast as run-time tests [S046 pp. 5–6, 8; S028 p. 5; S001 p. 45]; unverifiable assumptions rejected: "such an assumption would generally not be verifiable in practice." [S092 p. 11]; unknown constants replaced by monotone estimates raised only on stall [S064 pp. 12–13; S002 pp. 8, 22; S021 pp. 7–8, 11–12; S063 pp. 30–31; S046 pp. 5–6, 8].

**Clause (b), disclose and cap the theory–code gap** (08 §5 b; 10 works, 2014–2026; recurrence ✅, say–do ✅, executable ✅, exclusivity ✗, hence a clause, not a new item): infeasibility exits that also require a small penalty parameter, stated as departures [S029 pp. 28–29; S019 p. 35]; a curvature threshold outside the proved range and an unchecked set membership, stated [S008 p. 20]; an auxiliary sequence kept in code but dropped in the analysis [S043 pp. 9, 22]; "Although this choice is not covered by the convergence theory, one could cap the number of adjustments made to ζ, in which case it is covered by the theory." [S070 p. 12]; "Although this PG parameter update strategy worked better than the basic strategy in Algorithm 1 (see Line 19 and Line 21), it is not covered by our analysis in Section 4." [S053 p. 22]; "We found this update strategy to work better in our testing, all of the analysis of Section 5.2.3 still holds, and the analysis of Section 5.2.2 still holds if this modified update is only allowed a finite (possibly large) number of times." [S082 p. 27]; production settings listed against the analysed variant [S091 p. 17]; parameters frozen for analysis and verified constant in runs [S054 pp. 7, 21]; a runtime check restoring a theoretical condition [S040 pp. 11–12].

**Bracket the assumption** (candidate pool, folded here as evidence): a case where it holds and one where it fails, constants measured on a 2-D instance [D002 pp. 21–24; S063 pp. 25–29; S092 pp. 19–20; S093 pp. 19–22; S018 pp. 9–11; S044 pp. 3, 22–23]: "It would greatly broaden the scope of ADMM, and simplify modeling, if this condition could be relaxed, but unfortunately this condition is tight for general problems." [S018 p. 9].

<a id="heuristic-2"></a>
## Heuristic 2: count a safeguard's extra solves

**Base-tier text (verbatim):** 2. **If** you add a safeguard, **then** count its extra solves per iteration and make removing it the next target. Case, a three-rung ladder: 2010 steering, extra QP solves defended as "more than compensated for by a savings in the total number of iterations" (10.1137/080738222, p. 2294) → SQuID, at most two QO solves per iteration where the 2010 method needs at least three near an infeasible stationary point (10.1137/120880045, p. 841) → one inexact QP solve with the penalty update inside it (10.1137/18M1176488); "How much does all of this cost?" (ICCOPT 2019).

**Full-text evidence**: the ladder confirmed [S009 p. 14; S022 p. 3; S057 pp. 2, 30]; earlier rungs: pricing a safeguard by a hybrid run [S096 pp. 52–53; S006 p. 18]; one factorization for all (ρ, μ) candidates [S033 p. 18]; costed in inner products [S047 p. 6]; "A drawback of the algorithm described in this paper is that it requires the inexact solution of the normal subproblem (2.2) in addition to the primal-dual system (2.6)." [S025 p. 25]; gate expensive computations by cheap criticality measures: "It is not necessarily prudent to compute a normal step in every iteration." [S039 p. 6]. ✅ 2007–2020.

<a id="heuristic-3"></a>
## Heuristic 3: a failure users hit that theory treats as a corner case

**Base-tier text (verbatim):** 3. **If** you need a problem, **then** pick a failure users hit that theory treats as a corner case. Case: "Fast detection of infeasibility has become increasingly important due to the central role it plays in branch-and-bound methods for mixed-integer nonlinear programming" (10.1137/080738222, p. 2281); PDE scale (01 SW1).

**Full-text evidence**: MINLP branch-and-bound [S009 p. 1]; chance constraints in applications [S027 pp. 2–3]; AC-OPF intractable at industrial scale [S061 p. 2]: "This makes the problem nearly separable, which is a property that needs to be exploited in a solution approach for it to be efficient." [S061 p. 5]; the PAV algorithm's large-scale drawbacks: "However, we argue that the PAV algorithm does have critical drawbacks when it comes to solving large-scale problems of interest today." [S067 p. 3]. ✅

<a id="heuristic-4"></a>
## Heuristic 4: desiderata first

**Base-tier text (verbatim):** 4. **If** you start a design, **then** first write what the algorithm must deliver. Case: "What kind of algorithm do we want?" (NeurIPS 2022); research-page targets from "scalable step computation (for solving large-scale problems)" to "effective active-set detection (for warm-starting)".

**Full-text evidence**: no card-level evidence; unchanged (slides and research page only). Closest paper practice: listing each competing workaround's failure modes before stating desiderata [S010 pp. 2–3].

<a id="heuristic-5"></a>
## Heuristic 5: guarantee-free comparator first; restore the guarantee by guarding the incumbent

**Base-tier text (verbatim):** 5. **If** a fast variant has no guarantees, **then** keep the guarantee-carrying method as comparator and restore guarantees later. Case: SQP-GS → BFGS-SQP, "While our method has no convergence guarantees, we have found it to perform very well in practice" (10.1080/10556788.2016.1208749) → 10.1007/s12532-015-0086-2, arXiv:1708.02552.

Full-text evidence: confirmed [S003 p. 18; S008 pp. 2, 21; S049 p. 12]; "no convergence guarantees" is on [S004 p. 2]; order reversed in [S051 pp. 20, 22, 25]; guarantees given to someone else's fast scheme [S016 pp. 2, 8]. The guarded-incumbent construction, parts (i)–(iv), with its four-way validation, is [above](#method-6) (drafted as Method 6, kept a heuristic at review because exclusivity fails; C12). History: the first synthesis folded this heuristic into the draft Method 6 and gave its slot to *port the property*; the review restored the slot, so cards and RESOURCES.md rows that cite "Heuristic 5" keep their meaning. *Port the property* is now [Heuristic 11](#heuristic-11).

<a id="heuristic-11"></a>
## Heuristic 11: port the property, not the formula

New on 2026-10-10 (08 §5 a; numbered Heuristic 5 in the first synthesis draft): *If* you carry a method's guarantee or behaviour into a new setting or a rival framework, *then* name the inequality its proof or success rests on and redesign only the host's acceptance or update rules so every accepted step satisfies an analogue; leave the host skeleton as practitioners know it.
- Evidence (7 works, 2016–2024): self-correction, not the secant equation, as what makes BFGS work, "However, too much emphasis has been placed on this equation." [S028 pp. 2–4], reused for nonsmooth problems [S049 pp. 6, 8] ("One cannot maintain such assurances if Hk is used in place of H in (2.8)." [S049 p. 8]); ARC's accepted-step inequalities listed and the trust-region rules redesigned until each accepted step satisfies an analogue [S002 pp. 5–7]; TRACE's acceptance tests grafted into a trust funnel, proved lemma by lemma [S026 pp. 6, 13–19, 30–35]; step conditions that make ARC and TRACE special cases [H001 pp. 2, 4, 14–16]: "Our proposed framework is intentionally very general; it is not a trust region method, a quadratic regularization method, or a cubic regularization method." [H001 p. 2]; minimal changes to trust-region Newton-CG for optimal complexity [S020 pp. 2, 4]; only the curvature pair repaired through problem structure [S076 pp. 7, 10–13]; stated aim: "Therefore, we contend that it is of interest to explore trust-region methods that do not deviate too much from traditional schemes, yet offer optimal worst-case complexity properties." [S043 p. 4].
- Checks: recurrence ✅; say–do ✅ [S028 p. 2; S043 p. 4]; executable and different ✅ (the documented alternatives transplant the formula: a new cubic model [S002 pp. 5–6], fixed BFGS regularization [S028 p. 2]); exclusivity ⚠ partial; overlaps Heuristic 10 and the TRACE anatomy, hence a heuristic, not a method.

<a id="heuristic-6"></a>
## Heuristic 6: the metric that exposes the mechanism

**Base-tier text (verbatim):** 6. **If** CPU time is noisy or codes differ in language, **then** report the metric that exposes the mechanism. Case: "we ignore CPU time and focus on the performance measures of iterations, function evaluations, and gradient evaluations required until termination" (Que thesis 2016; 03 PE16).

**Full-text evidence**: [S008 p. 24] (primary source of the quoted CPU-time sentence, C2); [S047 p. 6; S032 p. 17; S012 pp. 19–20; S096 p. 57; S065 p. 19]: "The first measure shows the progress towards optimality that the solver makes within a fixed gradient evaluation limit" [S012 p. 19]; work-matched and time-matched comparisons [S037 p. 22; S065 pp. 17, 20–21]. ✅

<a id="heuristic-7"></a>
## Heuristic 7: filters by rule, with counts

**Base-tier text (verbatim):** 7. **If** you remove test problems, **then** name each with its reason, encode filters in code, and never filter on what the runs showed. Dropping problems no solver solved is symmetric but still outcome-based; PIPAL did it and reported the pre-filter counts (438 → 417; 125 → 120 and 105; 10.1007/s12532-012-0041-4, pp. 202, 205–206), the minimum if you cut. Anti-example, later dropped: problems kept only where "the LICQ held at all iterates in all runs of all algorithms that we ran" (arXiv:2007.10525 v1; 03 PE2).

**Full-text evidence (C6)**: rule-based pre-run filters with counts (1315 → 396 → 327) [D002 p. 25; S063 pp. 30–31]; PIPAL counts confirmed [S033 pp. 22, 25–26]; outcome-based filters also recur: problems where the method met a near-singular Jacobian [S017 p. 20], where the exact variant or the QP solver failed [S096 p. 50; S029 p. 29], where "the LICQ was satisfied at all iterates encountered in each run of our algorithm." [S037 p. 23], where f stayed above −10²⁰ in all runs [S030 p. 24]. ⚠ "later dropped" replaced by: rule-based pre-run filters in the 2024–2026 IPM papers; run-outcome filters recur through 2024. A mechanism-activated subset filtered on run outcome conflicts with this heuristic [S042 p. 17].

<a id="heuristic-8"></a>
## Heuristic 8: one run at iteration level first

**Base-tier text (verbatim):** 8. **If** you show a benchmark, **then** first show one run at iteration level (infeasible toy iteration tables, 10.1137/080738222, pp. 2295–2298, e.g. `batch1` = `batch` + tl[1] ≥ 5, p. 2296; 03 PE18). Practice only.

**Full-text evidence**: toy iteration tables [S009 pp. 15–18]; CATENA logs for Lancelot and AAL-TR [S019 pp. 35–38]; per-problem QO counts and last-ten-iteration residual plots [S022 pp. 31–32]; single-problem iteration plots before the benchmark [S004 pp. 12–16]. ✅

<a id="heuristic-9"></a>
## Heuristic 9: derivative checker, regression checks

**Base-tier text (verbatim):** 9. **If** a solver misbehaves, **then** run the derivative checker ("the best first step for debugging!", NonOpt manual) on the test problems too (commit e59f9b6: "Fixed derivatives on two test problems."); keep defensive exits, fixed seeds and byte-identical regression checks when refactoring; a test driver that returns 0 whatever happens is itself a bug (NonOpt, fixed 2026; 03 §4). Good practice more than a signature; lapses in 03 PE15, PE22.

**Full-text evidence**: no card-level evidence (code history only); unchanged.

<a id="heuristic-10"></a>
## Heuristic 10: keep the skeleton; deterministic twin; climb the rungs

**Base-tier text (verbatim):** 10. **If** the information the algorithm may trust changes (exact → inexact → nonsmooth → stochastic → noisy), **then** keep the skeleton, build a deterministic twin that replaces only the broken component, and climb the same rungs: full-rank equalities → rank deficiency → nonconvexity → inexact solves → inequalities → implementation. Case: "As a starting point for this stochastic setting, an algorithm is proposed for the deterministic setting that is modeled after a state-of-the-art line-search SQP algorithm" (arXiv:2007.10525); rungs 2008–2014 and 2021–2026 (Sources). For a noisy-evaluation feature, pick two rungs, not six.

**Full-text evidence** (22 cards, 21 works; the most-confirmed heuristic): rung order laid out in the dissertation [S096 pp. 33, 46, 59, 99] and stated in 2010 [S010 p. 2]; exact twin first [S029 pp. 3, 8; S020 pp. 4, 13; S013 pp. 5–6; S021 pp. 3, 10; D002 p. 9; S063 pp. 11, 20; S044 pp. 3, 10–15, 25]; noise rungs [S059 p. 3; S093 pp. 5–19]; deterministic-to-stochastic in the survey [S001 pp. 56–57]; twin and shadow quantities computed with exact data inside the proof (true-gradient merit parameter, noiseless twin iterate) [S013 pp. 10, 14, 16, 20; S059 pp. 7, 14, 33; S054 p. 21; S037 p. 6; S093 pp. 5, 16–17]. ✅

---

<a id="anatomy-inexact-sqp"></a>
## Signature work: Inexact SQP (S006; dissertation S096)

**Base-tier text (verbatim):**

#### Inexact SQP (Byrd, Curtis, Nocedal; SIAM J. Optim. 2008; DOI 10.1137/060674004) · Methods 1, 5
- **Origin**: PDE-constrained problems "for which the exact computation of steps in contemporary methods can be prohibitively expensive" (p. 351); PhD topic under Nocedal; who proposed it: unknown.
- **Why then**: mature Krylov solvers; no global-convergence conditions yet for inexact full-space line-search SQP (inferred).
- **Key insight**: termination tests that check primal and dual residuals separately and require merit-model decrease.
- **Minimum evidence**: Matlab with unpreconditioned GMRES on 44 CUTEr/COPS problems; the one-component baseline solved 45–86 %, the tests 100 % (Table 5.2, p. 367).
- **Abandoned paths**: preconditioning and local rates deferred; a Curtis–Haber PDE paper cited "in preparation" never appeared (06 §5).
- **Reception**: Nemhauser dissertation award (2008); an Ipopt option, still experimental; critics note extra solves and many parameters (05 §4).

**Full-text evidence**: problem entry: very large PDE-constrained problems where exact steps are too expensive, and prior inexact full-space SQP lacked conditions guaranteeing global convergence [S006 pp. 1–2]; key idea: accept an inexact KKT solve when it reduces a local model of the exact penalty function, with primal and dual residuals treated separately, and allow penalty increases only under Termination Test II [S006 pp. 2, 5–7]; evidence: Matlab, unpreconditioned GMRES, 44 CUTEr/COPS equality problems; a baseline identical except a full-residual stopping rule swept over κ = 2⁻¹ … 2⁻¹⁰ solves 45–86 % against 100 % (Table 5.2) [S006 p. 17]; the hybrid costs 0.5 extra GMRES iterations on average [S006 p. 18]; limits: strong assumptions, no preconditioning, Jacobian singularity and nonconvexity left for later [S006 pp. 8, 17–18], closed by the next rungs [S025; S017; S010]. The dissertation version: [S096 pp. 23, 26–29, 52] (50–86 %, a different version of the experiment).

<a id="anatomy-infeasibility-pipal"></a>
## Signature work: Infeasibility detection (S009) and PIPAL (S033)

**Base-tier text (verbatim):**

#### Infeasibility detection in SQP (Byrd, Curtis, Nocedal; SIAM J. Optim. 2010; DOI 10.1137/080738222) and PIPAL (Curtis; Math. Program. Comput. 2012; DOI 10.1007/s12532-012-0041-4) · Methods 2, 3, 5
- **Origin**: fast local convergence "regardless of whether a problem is feasible or infeasible", for MINLP branch-and-bound and parametric studies.
- **Why then**: MINLP codes built on NLP solvers needed fast infeasible verdicts (inferred).
- **Key insight**: one exact-penalty iteration whose penalty update, driven by progress toward feasibility, is the design object.
- **Minimum evidence**: 2010: a Matlab prototype on toy examples, benchmarking "outside the scope of this paper as it requires a sophisticated software implementation" (p. 2294). 2012: 438 CUTEr models against Ipopt with its engineering adopted, then degenerate and infeasible variants of 125 HS problems (417, 120 and 105 after dropping those no solver solved; pp. 202, 205–206).
- **Abandoned paths**: first submitted to Mathematical Programming (outcome unknown); PIPAL stayed a Matlab prototype despite "the potential to be a successful general-purpose solver" (03 §4).
- **Reception**: Hinder & Ye cite PIPAL as a slow penalty method (arXiv:1801.03072); a critique that the Sℓ1QP code fails with inexact QP solutions was later answered by updates inside the QP solve (10.1137/18M1176488; link inferred; 05 §4.5).

**Full-text evidence**: 2010: fast methods are slow on infeasible instances, which matter in MINLP branch-and-bound; Sℓ1QP lacks fast local guarantees when infeasible; switching designs are hard to tune [S009 pp. 1–3]; penalty multiplies the objective only, ρ_k = O(‖z_k − z*‖²) near an infeasible stationary point, steering rules plus a squared-error update [S009 pp. 4, 11, 13]; five illustrations with full iteration tables, an ablation with the update disabled, no benchmark set [S009 pp. 14–18]; limits: several QPs per iteration, only local infeasibility [S009 pp. 3, 14, 17–18]. 2012: penalty methods regularize and detect infeasibility but need LP/QP subproblems; IPMs scale but converge slowly to infeasible stationary points; combine them and make the parameter updates the contribution [S033 pp. 1–3]; slack reset, (ρ, μ) chosen from a few candidates by model-reduction tests with one factorization, a conservative fallback direction [S033 pp. 3, 8–19]; 438 → 417 CUTEr models after stated filters, Ipopt more efficient on the full set, PIPAL-a better on the 132 problems where ρ was reduced, degenerate (120) and infeasible (105) HS variants favour PIPAL, Ipopt engineering adopted, parameters tuned on the runs [S033 pp. 17–27]; stated limits: extra degrees of freedom may slow convergence, one type of degeneracy, a more sophisticated implementation needed [S033 pp. 24–25, 28].

<a id="anatomy-sqp-gs-bfgs-sqp"></a>
## Signature work: SQP-GS (S003) → BFGS-SQP and relative minimization profiles (S004)

**Base-tier text (verbatim):**

#### SQP-GS (Curtis, Overton; SIAM J. Optim. 2012; DOI 10.1137/090780201) → BFGS-SQP with relative minimization profiles (Curtis, Mitchell, Overton; Optim. Methods Softw. 2017; DOI 10.1080/10556788.2016.1208749) · Methods 4, 5; Heuristic 5
- **Origin**: postdoc with Overton (2007–09): SQP-penalty machinery joined to gradient sampling.
- **Why then**: new gradient-sampling theory; hard constrained problems from controller design (inferred).
- **Key insight**: 2012: sample constraint gradients inside an ℓ1-penalty SQP subproblem. 2017: "eschew a costly gradient sampling approach entirely", keep BFGS with penalty steering, and invent relative minimization profiles because existing profiles hid the objective, feasibility and budget trade-off.
- **Minimum evidence**: the p = 0 ablation (2012); 200 controller-design problems, BFGS-SQP "14.4 times faster" on the Lipschitz subset (2017).
- **Abandoned paths**: SLP-GS, whose "rate of convergence is typically much slower when compared to SQP-GS"; SQP-GS demoted to comparator.
- **Reception**: 2018 INFORMS Computing Society Prize (with Burke, Lewis, Overton). Independent benchmarks disagree: GRANSO better on feasibility (arXiv:1812.11630) versus gradient sampling "more consistent and reliable" (10.1137/22M1500137).

**Full-text evidence**: SQP-GS joins smooth SQP and gradient sampling, arguing that plain SQP fails on nonsmooth problems: "We emphasize that the GS procedure in our approach is necessary for ensuring theoretical convergence guarantees since a basic SQP strategy (without GS) will fail in theory and in practice." [S003 p. 4]; it generalizes Sℓ1QP (p = 0) and gradient sampling (m = 0) [S003 p. 9]; experiments: Matlab with MOSEK, 10 starting points, termination off, p = 0 ablation failing on all problems, no external rival, parameters "decided upon during the course of our experiments" [S003 pp. 16–24]; future work SLP-GS, cheaper but slower [S003 p. 25]. BFGS-SQP: application pull from HIFOO controller design and an evaluation gap in performance profiles [S004 pp. 3–5]; steering by comparing predicted violation reduction with a μ = 0 reference direction [S004 pp. 6–8]; relative minimization profiles and budget panels [S004 pp. 17–22]; 200 controller-design problems; SQP-GS finds more best optimizers at unlimited budget but "the fact remains that SQP-GS actually took 26.6 times longer to run to obtain these better results" [S004 p. 26]; on the pseudospectral set BFGS-SQP is better and 14.4 times faster [S004 p. 26]; regularization ablation problem-dependent [S004 pp. 27–28]; no convergence guarantees, small sizes forced by SQP-GS [S004 pp. 2, 9, 23].

<a id="anatomy-inexact-ipm"></a>
## Signature work: Inexact interior-point method in Ipopt (S010, S036)

New anatomy (2026-10-10); no base-tier text.

- **Origin**: problems with millions of variables where storing or factoring derivative matrices is intractable because of fill-in; nonlinear elimination needs many accurate constraint solves and turns bounds into nonlinear inequalities; reduced-space PDE methods pay for repeated projections and do not allow general inequalities or state bounds [S010 pp. 1–3].
- **Why then**: the SMART tests had been carried through the equality, nonconvex and rank-deficient rungs, which the paper lays out as an explicit ladder [S010 p. 2]: "the benefits of these techniques are only realized if inexact step computations are allowed and controlled appropriately in order to guarantee global convergence of the algorithm." [S010 p. 2]; Ipopt (Wächter) and PARDISO's iterative solver (Schenk) at hand (inferred from the author list).
- **Key insight**: scale slacks so the barrier subproblem's primal-dual system matches the predecessor's; normal/tangential split with a trust region; three SMART tests on penalty-model reduction; inertia-free Hessian modification; inherit the predecessor's theory [S010 pp. 4–12]. The implementation note runs the cheap one-system step by default and switches to the rank-robust decomposition step when the accepted steplength drops below 10⁻³, since only the latter's proof survives short steps [S036 pp. 5–11].
- **Minimum evidence**: inside Ipopt 3.7.0 with PARDISO SQMR and a multilevel incomplete factorization against default Ipopt with PARDISO direct; 684 CUTEr/COPS problems after pre-run exclusions, full exit-status table, 85 % against 94 %; 3-D PDE boundary control up to n = 512,000 (3,402 s against 33,704 s at N = 50) and hyperthermia up to n = 125,020 [S010 pp. 19–26]; "Our approach fails more often, but this is to be expected, as our code is not as mature as IPOPT and an increase in iteration count often follows from the use of inexact Newton steps." [S010 p. 24]. Implementation note: 617 CUTE problems, 89 % against 96 % for default Ipopt and 84 % for always using the robust step, 142 switches [S036 p. 12]; boundary control up to 670k variables and server-room cooling up to 664k variables, speedups 2.64–17.89 at equal iteration counts and objective values [S036 pp. 12–17]; "Specifically, the computation time for the largest instance with more than 600,000 variables was reduced from more than 6 days to 8.2 h, a speedup by a factor of 17.89." [S036 p. 17].
- **Abandoned paths**: problem-specific preconditioning deferred [S010 p. 3]; two-sided constraints unsupported [S010 p. 23]; no local rate analysis; preconditioner degradation as μ → 0 left open [S036 p. 18].
- **Reception**: an Ipopt option (`inexact_algorithm`), compile-time and "EXPERIMENTAL! (default: no)" in Ipopt 3.14 (`configure.ac`, base tier); critics note the extra Newton system of the stabilized tests (05 §4.3).

<a id="anatomy-bfgs-gs"></a>
## Signature work: Quasi-Newton with guarantees for nonsmooth problems (S008)

New anatomy (2026-10-10); no base-tier text.

- **Origin**: practitioners see BFGS work on nonsmooth problems while its guarantees are limited; named defects: no stationarity-based termination, inverse Hessians tending to singularity; gradient sampling has guarantees but costly iterations without curvature [S008 pp. 2–3].
- **Why then**: the adaptive gradient sampling algorithm of 2013 [S012 pp. 2–5] and the Lewis–Overton evidence for BFGS on nonsmooth problems; a student (Que) on the line (inferred).
- **Key insight**: the stated design intent, "A feature critical to the practical performance of our algorithm is that, when it is applied to solve many problem instances, the algorithm reduces to an unadulterated BFGS strategy for the majority of the iterations." [S008 p. 2]; the direction comes from the dual of a sampled-gradient model that reduces to BFGS with one sample; the radius is reduced only under stationarity, curvature and positive-step tests; sampling and a bounded, damped L-BFGS fallback wake only when the tests fail [S008 pp. 5–14]; set against HANSO's BFGS-then-GS switch [S008 p. 21].
- **Minimum evidence**: a C++ code against HANSO-BFGS, HANSO default and LMBM at defaults with iteration limits on par; 26 scalable problems, 10 starts each (260 runs); CPU time ignored because of language differences; iterations and evaluations reported; termination-flag counts tabulated; quality by an ε-stationarity estimate from fresh random points; losses printed [S008 pp. 20–28].
- **Abandoned paths**: thresholds varying with the sampling radius, not pursued because no benefit was seen [S008 p. 28]; stated departures: the curvature threshold violates the proved bound and set membership is never checked [S008 p. 20].
- **Reception**: the evaluation passage reappears in the Que thesis 2016 (04 T2; C2); the nonsmooth line continues into the self-correcting framework [S049 pp. 6, 8] and NonOpt [S088 pp. 7–9].

<a id="anatomy-trace"></a>
## Signature work: TRACE (S002)

**Base-tier text (verbatim):**

#### TRACE (Curtis, Robinson, Samadi; Math. Program. 2017; DOI 10.1007/s10107-016-1026-2) · Method 4
- **Origin**: discussions with Cartis, Gould and Toint about adaptive cubic regularization (ARC) "that were inspirational" (01 SW4).
- **Why then**: ARC had the optimal bound, classical trust region only O(ε^-2) (inferred).
- **Key insight**: keep the trust-region framework and its classical guarantees; change acceptance and radius rules to match ARC's worst case.
- **Minimum evidence**: theory only, exact subproblems "For simplicity in revealing the salient features".
- **Abandoned paths**: inexact subproblems closed seven years later (10.1137/22M1492428); a Lemma 3.19 corrigendum.
- **Reception**: Cartis, Gould and Toint placed it in their optimality class ("the details are not given", arXiv:1709.07180); Ye's group credits it but omits it from its benchmarks (arXiv:2311.11489). His own critique followed (regional complexity).

**Full-text evidence**: entry: nonconvex methods aimed at global and fast local convergence while worst-case complexity was overlooked; ARC attains O(ε^-3/2) against O(ε^-2) for traditional trust region [S002 pp. 2–3]; key idea: identify ARC's two proof-critical properties of accepted steps and redesign trust-region acceptance (decrease relative to ‖s‖³) and radius updates (reject-and-expand; implicit contraction from a regularized subproblem) so that accepted steps satisfy analogues, while allowing unregularized Newton steps [S002 pp. 6–9, 11]; "there are situations in which our algorithm may reject a step and expand the trust region" [S002 p. 3]; no experiments; the appendix argues per-iteration cost [S002 pp. 31–32]; "We expect that this is also the case for our algorithm, but this has not yet been confirmed." [S002 p. 30]; inexact variants named as current research [S002 p. 30], closed in [S043 pp. 3–4, 6–7]. Later rungs: [H001 pp. 2, 14–16; S026 pp. 6, 13–19; S035 pp. 5–9; S020 pp. 2, 4].

<a id="anatomy-stochastic-sqp"></a>
## Signature work: Stochastic SQP (S007)

**Base-tier text (verbatim):**

#### Stochastic SQP (Berahas, Curtis, Robinson, Zhou; SIAM J. Optim. 2021; DOI 10.1137/20M1354556) · Methods 2, 5; Heuristics 1, 10
- **Origin**: the stochastic turn of the SIAM Review survey (10.1137/16M1080173) joined to his line-search SQP.
- **Why then**: constrained learning problems; a first postdoc (Berahas) (inferred).
- **Key insight**: a deterministic twin with Lipschitz-based stepsizes; merit-parameter behaviour classified into events, the bad ones bounded.
- **Minimum evidence**: twin against line-search SQP on CUTE problems; noise 1e-8 to 1e-1, 10 runs; a baseline given 110× iterations; the event measured at 99.10–99.92 %.
- **Abandoned paths**: not documented; the LICQ-conditioned test set was dropped later; a Corollary 3.14 corrigendum.
- **Reception**: opened his largest current line. Na, Anitescu and Kolar call it "the very first practical algorithm" (10.1007/s10107-022-01846-z); O'Neill reran it: "as the noise level increases, the performance of SSQP degrades significantly with respect to infeasibility" (arXiv:2408.16656).

**Full-text evidence** (card read the arXiv version): deterministic equality constraints with a stochastic objective; existing stochastic methods are penalty-based, and line-search SQP is unusable because line searches are intractable [S007 pp. 2–3]; the line search replaced by minimizing a Lipschitz upper bound of the ℓ1 merit change, the model-reduction merit-parameter rule kept, the stochastic stepsize projected into an interval set by an adaptive lower estimate [S007 pp. 6–8, 14–16]; the test set kept 49 of 123 CUTE equality problems, the last filter being LICQ at all iterates of all runs [S007 p. 26]; deterministic profiles; stochastic runs at 4 noise levels, 10 runs each; a subgradient baseline tuned per instance over 11 values with 10× the iterations (110× total); errors measured with the true gradient and least-squares multipliers; the event held in 99.10–99.92 % of iterations [S007 pp. 26–28]: "This provides evidence that the theory offered under the event (25) is relevant in practice." [S007 p. 27]. ✗ The LICQ-type outcome filter recurs in 2021 [S037 p. 23] (C6). Follow-ups: [S021; S013; S030; S054; S044; D002].

---

<a id="anti-patterns"></a>
## Research anti-patterns

**Base-tier text (verbatim):**

#### Research Anti-patterns

| Anti-pattern | Why he opposes it (source) | Do instead |
|---|---|---|
| Two-phase "feasibility, then optimize" designs | "does not switch between two separate techniques (e.g., no feasibility restoration as in Fletcher and Leyffer, 1997)" (INFORMS OS 2008, slide 5, joint) | One steering algorithm (Method 2) |
| Subproblem solver as a black box | "as opposed to treating the subproblem solver as a “black-box”" (research page) | Inner tests from outer needs (Method 1) |
| Infeasible cases as an afterthought | "often treated as an afterthought" (INFORMS OS 2008, slide 3, joint) | Constructed infeasible variants (Method 3) |
| Worst-case complexity as the judge of nonconvex methods | "They say: “Newton's method is as slow as gradient descent.” This essentially ignores reality." (ECOM 2021 slide 32/45) | Audit the yardstick (Method 4) |
| Overweighting exact-penalty theory | "It is a mistake to overemphasize the relevance of this theory for practical use." (NeurIPS 2025) | Measure the parameter in runs (Heuristic 1) |

**Full-text evidence for the changes**: the black-box row gains [S064 p. 2; S016 p. 4] (quoted under [Taste warnings](#taste-warnings)). New row, *an always-on safeguard, or a switch to the guaranteed method after the fast one stalls* (practice, inferred; no stated opposition): [S036 p. 12; S047 p. 2; S067 p. 8; S028 p. 2]; HANSO's switch from BFGS to gradient sampling is the contrasting design, described without criticism [S008 p. 21] (see [the guarded incumbent](#method-6), check 3). Review correction: the first draft cited "safeguarding was not necessary" [S040 p. 20] as a reason; S040's safeguard is itself a dormant threshold cutoff (steering off once µ ≤ 10⁻⁴ [S040 pp. 13, 18]), so the result is counter-evidence for the dormant guard and is now labelled so [S040 pp. 13–14, 20]; S008 p. 21 describes HANSO's BFGS-then-GS default without criticising it.

---

<a id="trajectory"></a>
## Research trajectory

**Base-tier text (verbatim):**

#### Research Trajectory

| Period | Main direction | Trigger | Representative work |
|---|---|---|---|
| 2003–2014 | Inexact, matrix-free SQP and IPM (PhD Northwestern 2007, Nocedal) | PDE-scale problems (stated) | 10.1137/060674004; 10.1137/090747634 |
| 2007– | Nonsmooth nonconvex: gradient sampling, BFGS-SQP | Postdoc with Overton, NYU | 10.1137/090780201; 10.1080/10556788.2016.1208749 |
| 2008–2020 | Infeasibility detection, penalty updates (Lehigh ISE from 2009) | MINLP users' needs (stated) | 10.1137/080738222; 10.1137/120880045; 10.1137/18M1176488 |
| 2013– | Stochastic and ML optimization | Colleagues Scheinberg and Takáč, joint grant (practice) | 10.1137/16M1080173 (2021 Lagrange Prize) |
| 2014–2024 | Complexity of practical methods; self-critique 2018–2021 | Cartis–Gould–Toint discussions (stated) | 10.1007/s10107-016-1026-2; 10.1007/s10107-020-01492-3 |
| 2020– | Stochastic SQP with deterministic constraints (main line); noisy IPM from 2022 | Join of two lines (stated) | 10.1137/20M1354556; arXiv:2502.11302 |
| 2019–2026 | Consolidation: book with Robinson, NonOpt | — | 10.1137/1.9781611978599; 10.1007/s12532-026-00322-5 |

Pattern (inferred, 06 §4): he rarely abandons a line; its machinery (merit-parameter control, inexact inner tests) moves into the next setting, opened by a new information model or new people.

#### Latest
- 2025-09-28 to 2026-09-28: progressive sampling (arXiv:2510.00417); a method on Fletcher's augmented Lagrangian (arXiv:2608.12665); noisy gradient sampling (arXiv:2604.00278); a single-loop stochastic IPM (10.1007/s10107-025-02320-2); NonOpt in MPC (10.1007/s12532-026-00322-5), then a July 2026 code-quality pass (a `CLAUDE.md` brief, author not established); student-led ML optimizers (arXiv:2601.11795, arXiv:2605.06945).
- Direction (inferred): noise moving into constraints, multipliers and active sets (arXiv:2509.00888, arXiv:2502.11302); sample complexity for constrained problems.

**Topics by period in the full texts** (08 §8.1; cards, full reads in brackets): 2003–2007: 5 [4]: combinatorial matrix theory at William & Mary (S058, S081; S086 unreadable), IPM step lengths for QP with Nocedal (S047), dissertation on inexact SQP (S096). 2008–2012: 10 [9]: inexact and matrix-free SQP/IPM (S006, S025, S017, S010, S036), penalty updates and infeasibility (S032, S009, S033), nonsmooth SQP-GS (S003). 2013–2017: 19 [19]: nonsmooth quasi-Newton and GS (S012, S008, S004), inexact SQO and SQuID (S029, S022), AL steering (S019, S040), active-set QP and isotonic regression (S024, S067, S064), sparse and ℓ1 (S038, S050), LMSD (S042), stochastic BFGS (S028), ML tutorial (S011), TRACE and the trust funnel (S002, S039), market clearing with MERL (S077, S066). 2018–2022: 28 [27]: survey (S001), complexity line (S026, S035, H001, S062, S020), stochastic trust region and adaptive frameworks (S015, D001, S041), first stochastic SQP (S007, S037), nonsmooth (S005, S049, S065), quasi-Newton (S046, S051), sparse (S052, S053), penalty inside the QP solver (S057), negative curvature (S014), applications and distributed (S018, S048, S056, S071, S061, S094). 2023–2026: 34 [27]: stochastic and noisy SQP and IPM (S013, S021, S030, S054, S068, S092, D002/S063, S044, S059), noisy active-set identification and noisy GS (S093, S091), inexact TRACE (S043), NonOpt (S088), local-linear method on Fletcher's AL (S087), constrained proximal gradient (S082), ML fairness and optimizers (S069, S083, S089, S090), OR applications (S016, S034, S073), SCOPF (S023), DFO with surrogates (S075), incremental quasi-Newton (S076), prox-SVRG (S070).

**Turns** (08 §8.2): 2006–2007 combinatorics to NLP inside the dissertation [S058 pp. 2–6; S081 pp. 3–19; S096 pp. 23, 98]; 2012–2013 nonsmooth line [S003 p. 4; S012 pp. 2–5; S008 pp. 2–3]; 2014 Robinson enters [S029] and stays; 2016–2018 stochastic and complexity [S028; S002; S001]; 2020–2021 stochastic SQP [S007 pp. 2, 26–27]; 2024–2026 noise moves into constraints, IPMs and active sets [D002 pp. 3, 24; S059 pp. 3–4; S093 pp. 5–19], plus application or ML lines with new co-authors: fairness and ML optimizers [S069; S083; S089; S090], healthcare OR [S016; S034; S073], power systems [S061; S094; S023] (C11).

**What stayed constant** (08 §8.3): inner accuracy derived from the outer method [S096 p. 23; S088 pp. 3, 9]; the merit-model skeleton and its proof devices [S096 pp. 33–39; S007 pp. 8–10; S054 pp. 10–11]; the rung ladder of Heuristic 10 [S096 pp. 33, 46, 59, 99; S093 pp. 5–19]; guards attached to an incumbent [S047 pp. 4–5; S087 pp. 13–14]; in-framework rivals with one component varied [S047 pp. 6–8; S088 pp. 7–9].

**Collaboration** (08 §9): Robinson co-authors 34 of the 96 works (35 cards list him, but S028 only acknowledges him; 32 works counting each possible pair once), all from 2014 on, across every line from AL steering [S019] to fairness [S083]; Nocedal (9 cards, 2007–2018) and Byrd (4, 2007–2010) frame the formative work; Wächter is the longest continuous partner (11 cards, 2009–2025); Overton and Burke carry the nonsmooth and infeasibility lines; Scheinberg the stochastic trust-region and adaptive frameworks; sole-author papers are rare and mark new lines: the dissertation [S096], PIPAL [S033], stochastic self-correcting BFGS [S028]; application partners enter in bursts and rarely return (MERL; the GO-competition team; healthcare OR).

**Base-tier Academic Lineage (verbatim)**; SKILL.md adds only the Robinson count (34 works, 32 with possible pairs merged):

#### Academic Lineage

- **Upward** (Mathematics Genealogy Project, observed): Bliss → Hestenes → Tapia → Nocedal → Curtis (Northwestern 2007).
- **Formative partners**: Richard Byrd (thanked in the thesis for his "knowledge and expertise"); Andreas Wächter (2009–2025, inexact IPM in Ipopt, noisy IPM); postdoc host Michael Overton; complexity influence Cartis–Gould–Toint; dominant co-author since 2014 Daniel Robinson.
- **Downward**: nine PhD graduates, each on one of his lines; four postdocs (Berahas, O'Neill, Dinç Yalçın, X. Jiang) (06 §2.3).
- **Self-placement** (inferred): his 2021 public lecture sets a smoothness lineage (Powell, Fletcher, Goldfarb, Nocedal) beside a convexity-and-complexity one (Fenchel, Rockafellar, Nemirovski, Nesterov); he sits on the first.

---

<a id="inner-tensions"></a>
## Inner tensions

**Base-tier text (verbatim):**

#### Inner Tensions

- **Tension 1: complexity critic vs complexity producer.** "Continuous optimization has become too theoretical in recent years!" (ECOM 2021) and "Our worst-case analysis for nonconvex optimization is faulty." (ISMP 2018), yet about ten complexity papers 2017–2024 and "a better worst-case sample complexity bound" claimed in 2025 (arXiv:2510.00417). His 2019 reconciliation: "Achieving good/optimal complexity for practical algorithms."
- **Tension 2: fair-comparison preacher vs his own benchmarks.** He said to count tuning time, avoid one-test-set bias and repeat runs (2017, 2021); he tuned on the test set unreported (2012–2019), reused one nonsmooth set (2018–2025), reported single runs for a randomized method (2019), kept only problems some solver solved (2012), and set SQuID's published statistics on 122–123 problems beside new runs on 126 (arXiv:1803.09224 v3, pp. 27–28). Practice improved from 2018 (equal-effort tuning, a 110× baseline, time-matched LMBM over 10 runs).
- **Tension 3: penalty steerer vs avoiding penalties.** Penalty and augmented-Lagrangian designs 2008–2016; then "handling constraints as constraints", "(i.e., avoid penalty methods, augmented Lagrangian, etc.)" and "Penalization is not often the best route" (2024–2026 slides); yet the stochastic SQP keeps an adaptive merit parameter and arXiv:2608.12665 builds on Fletcher's augmented Lagrangian. It may target only fixed-weight reformulations (inferred).
- **Tension 4: single algorithm vs his own data.** The 2008 goal names Fletcher–Leyffer restoration as what to avoid (infopt_08, slide 5). On 8 infeasible toy problems a code labelled "Filter" (filterSQP with restoration: inferred) needs fewer iterations than SQuID on 3, SQuID on 4, one tie (siopt_11, slide 16/35); in 2012, with a different SQuID column, "Filter" is fewer on 5, one tie (copper_12, slide 28/41). Neither deck explains the change; 02 C4 misstates the 2011 count.
- **Tension 5: guarantees vs speed.** BFGS-SQP published with "no convergence guarantees", later restored; merit-parameter events "can be ignored" in practice versus O'Neill's measured degradation (05 X2); almost-sure results "do not provide significant additional insights" (SIAM Review) versus his 2023–2026 almost-sure papers.

**Full-text evidence (2026-10-10):**
- **Tension 1 (C7)**: the complexity-for-practice premise is adopted in 2017–2018: "This is due to the fact that, at least for convex optimization, algorithms designed with complexity bounds in mind have led to methods with improved practical performance." [S026 p. 1; S002 pp. 2–3]; in the same year the audit appears in print [S035 p. 9; S046 p. 3]; later the papers price their own devices [S020 p. 22] or argue the reverse ordering, "However, as is typical with well-designed second-derivative methods, although the complexity bound is worse, it typically performs better (see Section 5)." [S053 p. 17]; a 2026 worst-case gain is produced while worst-case parameter rules are disowned for practice: "We emphasize, however, that for good practical performance, we do not expect these parameter requirements to be absolutely necessary." [S087 p. 22; S087 p. 24]; "It is unclear how to establish similar complexity results when a traditional trust region radius update is used." [S035 p. 10].
- **Tension 2 (C5)**: see [Method 5](#method-5), say–do.
- **Tension 3 (C8)**: constrain, don't weight (08 §5 c; heuristic-grade, not numbered: the heuristic list is full and the item explains a tension better than it guides solver design; recurrence ✅ 2025–2026 only, say–do ✅, executable ✅, exclusivity ✗). Evidence (4 full works plus two abstract-level): "conventional techniques such as penalty-based methods [17] may fail to preserve the structure of the solution (see [16, Section 5]), therefore limiting their effectiveness in this setting." [S082 p. 2]; hard fairness constraints because the weight is costly and "First, the unfairness measure does not always improve monotonically with decreasing λ." [S083 pp. 2–3, 11–12]; "This is the first paper to combine hard constraints with smooth nonconvex surrogates in such a way that desired bounds on unfairness measures are actually realized (to high accuracy) when a prediction model is ultimately trained." [S083 p. 3]; the weighting method rejected for ε-constraint Pareto search [S073 pp. 10–11]; "Another key feature of this methodology is that one does not solve the hard-constrained training problem with a penalty-based (e.g., augmented Lagrangian) method." [S068 p. 19]; abstract-level [S055; S084]. What it changes: penalties are avoided as a *problem reformulation* [S082 p. 2; S083 pp. 2–3] while a merit parameter stays inside step acceptance [S082 p. 6; S083 p. 24]. Counter-instances stay in the tension: a fixed-timetable penalty [S089 p. 6], a penalty knob swept on a grid [S069 pp. 8–10], a method on Fletcher's augmented Lagrangian: "In this case, the algorithm reduces to a gradient descent algorithm applied to minimize Fletcher’s augmented Lagrangian." [S087 pp. 2, 9, 25]. The penalty doubt is older than 2024: the blocking-effect critique dates from 2007–2008 [S096 p. 78; S032 p. 4]. A penalty reformulation that failed in practice: "This reformulation did not work well in our experiments, which we attribute to the negative curvature that such a penalty term introduces into the objective function." [S061 p. 12].
- **Tension 5** (inferred): the papers' practice reads as a settlement, Heuristic 5's guarded incumbent: speed by default, guarantee dormant, its price measured [S036 p. 12; S020 p. 22]; a proposed safeguard can also lose outright [S040 p. 20]. The papers do not say they are resolving the tension. Almost-sure results continue [S054; S091 p. 10].

---

<a id="honest-boundary"></a>
## Honest boundary (base-tier text)

**Base-tier text (verbatim)**; SKILL.md now states the full-text coverage, the remaining gaps and the corrections:

#### Honest Boundary

- **Research date and updates**: researched 2026-09-28. Curtis is active (five arXiv preprints in the first eight months of 2026); re-run the research every 6–12 months and re-check "Latest", Tension 3 and the Roundtable Card.
- **Tacit-knowledge gaps**: how he spots a bad parameter-update rule in an iteration log, how he sets the constants in termination tests, and how proof errors are found are not recorded. Group meetings, one-to-one supervision and draft review are undocumented, and the 2018–2025 student voice is missing. No first-person origin stories; spoken asides survive only as slide text.
- **Era and resources**: most evidence is 2006–2022 Matlab prototypes on small CUTEr/CUTEst problems; scale evidence rests on one Ipopt PDE example.
- **Field boundary**: continuous, mostly nonconvex, local search. Not mixed-integer, global or conic. His current energy goes to stochastic, noisy and ML problems, which a deterministic solver team must translate (Heuristic 10).
- **Claimed but unverified** (never used as methods): counting all tuning time (no paper reports it); "We should not let one test set (or a few) bias all research." (his nonsmooth set ran 2018–2025); avoiding penalty methods (contradicted by his designs); minimizing f subject to controlled violation v(x) ≤ ε, announced as on-going (no paper); "I have results!" beyond PIPAL's constructions; a 12-reviews-a-year quota; the larger inexact-Ipopt speed-up; ISE 403 research-topic teaching (syllabus only); smooth-NLP warm-start active-set detection (no paper).
- **Record limits**: Google Scholar and Semantic Scholar profiles not read; 2019–2024 papers read in arXiv versions; the 2025 book not read; no referee reports; some critique quotes come from Semantic Scholar citation contexts, not full texts.

**Open gaps after the deep reading** (08 §11): abstract-only works: the stochastic inexact SQO paper [S045] (probably the journal form of S037; its termination tests for stochastic gradients are known only from the abstract); the ε-constraint fairness paper [S055] and the bilevel synthetic-data paper [S072], which would show whether constrain-don't-weight is argued beyond S082–S083; the SCOPF journal paper [S060] (the preprint S061 was read); the adaptive stochastic optimization framework [S031] (the D001 article was read); a workshop report [S078]; MOPTA proceedings [S079]; the hard-constraint training paper [S084, metadata]. The 2025 book [S074] is known only from a retailer's copy of the publisher's description; its treatment of BFGS-SQP, gradient sampling and NonOpt, and whether it states a benchmarking protocol, are not known. S086 (undergraduate thesis) is unreadable and outside scope.

---

<a id="corrections"></a>
## Corrections from the full texts

| # | Skill item (2026-09-28) | Full-text finding | Handling |
|---|---|---|---|
| C1 | Method 1 step 6 (minutes per iteration, from the research page, attributed to 10.1137/090747634) | not in the cited paper, which reports total CPU seconds per mesh level [S010 p. 25]; the full-text scale figure is 6 days → 8.2 h, 17.89× [S036 p. 17] | step rewritten; research-page figure kept as unverified (Honest Boundary) |
| C2 | Method 4 step 4 and Heuristic 6 (quotes attributed to the Que thesis 2016) | same sentences in the 2015 journal paper [S008 pp. 24–25] | S008 cited as primary |
| C3 | Method 3 dates (2010, 2012, 2020; x₁ bounds from arXiv:1803.09224) | incomplete, not false: the practice starts earlier, 2009 [S025 pp. 22–23] and, for the x₁ bounds, 2014 [S022 p. 30] ("As in [3]" [S057 p. 28]); 2010 constructions exist [S009 pp. 14–16] | marked ⚠, earlier start added |
| C4 | Method 3 limitation (no redundant-equality variants) | duplicated constraints [S021 pp. 27–28]; MPCC-type still absent | limitation corrected |
| C5 | Method 5 say–do (*improving after about 2018*) and Tension 2 | split by paper type: equal budgets in stochastic and ML papers [S015 p. 18; S041 p. 22]; deterministic papers tune on the evaluation runs 2007–2026 [S033 p. 21; S088 p. 14] | say–do rewritten; old sentence kept with ✗ |
| C6 | Heuristic 7 (*later dropped*) and the stochastic SQP anatomy | outcome filters recur [S037 p. 23; S030 p. 24]; rule-based pre-run filters in 2024–2026 IPM papers [D002 p. 25] | marked ✗, corrected |
| C7 | Tension 1 (talks vs papers) | also inside 2017–2018 papers [S026 p. 1; S035 p. 9] | added |
| C8 | Tension 3 (inferred reading) | card-supported [S082 p. 2; S083 pp. 2–3; S068 p. 19]; counter-instances [S089 p. 6; S069 pp. 8–10; S087 p. 2] | added |
| C9 | Taste 3 (one algorithm beats two phases) | deliberate switches and phases [S026 pp. 1–2, 25; S019 pp. 33, 43; S036 pp. 9–10; S063 pp. 3, 5, 30–31; S022 p. 1] | qualified |
| C10 | Method 2 scope | prescribed schedules where progress cannot be computed [S044 p. 3; D002 pp. 3, 6, 24–25; S063 pp. 6–9] | variant added |
| C11 | Trajectory table | missing 2003–2006 combinatorics [S058; S081] and the OR and power-systems lines [S016; S034; S073; S061; S094; S023] | rows added |
| C12 | Heuristic 5 | confirmed and extended: the guarantee is restored by guarding the incumbent [S003 p. 18; S008 pp. 2, 21; S004 p. 2; S049 p. 12]; that construction was drafted as a core method (Method 6) and kept a heuristic because exclusivity fails (Wright, Fletcher, Toint and Wächter seats) | slot 5 keeps its meaning with a full-text extension; *port the property, not the formula* [S002 pp. 5–7; S028 p. 2; S043 p. 4] added as Heuristic 11 (the first draft had swapped it into slot 5) |

Not changed: the 45–86 % figure of the inexact-SQP anatomy stays [S006 p. 17] (the dissertation's 50–86 % [S096 p. 52] is a different version of the experiment). Every page reference of the base-tier signature-work anatomies (journal pages) remains valid; card page references were added beside them.

---

<a id="not-promoted"></a>
## Candidates not promoted

From 08 §4–§6 and §10 (counts are distinct full cards, pairs merged):
- *Θ_k normal–tangential proof skeleton* [S096 pp. 33–39; S006 pp. 9–11; S032 pp. 12–14; S025 pp. 12–14; S017 pp. 13–16; S007 pp. 8–10; S054 pp. 10–11]: a proof template, not research craft; technique catalog only.
- *Price the guarantee* as a separate method: it is Heuristic 5 (iv).
- *Reduce to the incumbent* and *dormant safeguard* as two methods: one construction from two sides; merged into the draft Method 6.
- *Guard the incumbent* (the draft Method 6) as a core method: exclusivity fails against four teammates' methods ([row 4](#method-6)); kept as Heuristic 5's full-text form.
- *Predict the rival's failure, then show it* (8 cards): common in good papers; Method 3 variant.
- *Prove the adaptive parameter freezes* (4 cards): proof device; Method 2 evidence.
- *Iteration typing with an exhaustiveness lemma* (7 cards): proof device.
- *Known-answer instances* (5 cards): Method 3 variant.
- *Competition as benchmark protocol* (2 works): Method 5 variant.
- *Limitations stated up front* (4 cards): writing move; Taste mark 7 and Workflow E.
- Combinatorics-era candidates [S058; S081]: pre-PhD, outside the field.
- Application-specific candidates [S034 pp. 38, 51; S048 pp. 11–13; S089 pp. 4–5; S069 pp. 3, 8; S071 TR pp. 3, 5–6]: co-author-led application detail without explanatory power for solver research.
- Book-based claims [S074]: secondary source.
- Card reading notes about inconsistencies inside individual works: not surfaced; only the neutral lesson in Workflow E's checkpoint is kept.

---

<a id="sources"></a>
## Sources (base-tier lists, verbatim)

Moved from SKILL.md's appendix on 2026-10-10, which now points to 07, 08, 09, `INDEX.md` and the technique catalog. Every DOI and arXiv id below resolved in Crossref or on arxiv.org on 2026-09-28.

#### Papers (primary)
- Byrd, Curtis, Nocedal. An inexact SQP method for equality constrained optimization. SIAM J. Optim. 2008. 10.1137/060674004
- Curtis, Nocedal. Flexible penalty functions for nonlinear constrained optimization. IMA J. Numer. Anal. 2008. 10.1093/imanum/drn003
- Byrd, Curtis, Nocedal. An inexact Newton method for nonconvex equality constrained optimization. Math. Program. 2010. 10.1007/s10107-008-0248-3
- Curtis, Nocedal, Wächter. A matrix-free algorithm for equality constrained optimization problems with rank-deficient Jacobians. SIAM J. Optim. 2009. 10.1137/08072471X
- Byrd, Curtis, Nocedal. Infeasibility detection and SQP methods for nonlinear optimization. SIAM J. Optim. 2010. 10.1137/080738222
- Curtis, Schenk, Wächter. An interior-point algorithm for large-scale nonlinear optimization with inexact step computations. SIAM J. Sci. Comput. 2010. 10.1137/090747634
- Curtis, Huber, Schenk, Wächter. A note on the implementation of an interior-point algorithm for nonlinear optimization with inexact step computations. Math. Program. 2012. 10.1007/s10107-012-0557-4
- Curtis. A penalty-interior-point algorithm for nonlinear constrained optimization. Math. Program. Comput. 2012. 10.1007/s12532-012-0041-4
- Curtis, Overton. A sequential quadratic programming algorithm for nonconvex, nonsmooth constrained optimization. SIAM J. Optim. 2012. 10.1137/090780201
- Burke, Curtis, Wang. A sequential quadratic optimization algorithm with rapid infeasibility detection. SIAM J. Optim. 2014. 10.1137/120880045
- Curtis, Johnson, Robinson, Wächter. An inexact sequential quadratic optimization algorithm for nonlinear optimization. SIAM J. Optim. 2014. 10.1137/130918320
- Curtis, Jiang, Robinson. An adaptive augmented Lagrangian method for large-scale constrained optimization. Math. Program. 2015. 10.1007/s10107-014-0784-y
- Curtis, Que. A quasi-Newton algorithm for nonconvex, nonsmooth optimization with global convergence guarantees. Math. Program. Comput. 2015. 10.1007/s12532-015-0086-2
- Curtis, Mitchell, Overton. A BFGS-SQP method for nonsmooth, nonconvex, constrained optimization and its evaluation using relative minimization profiles. Optim. Methods Softw. 2017. 10.1080/10556788.2016.1208749
- Curtis, Robinson, Samadi. A trust region algorithm with a worst-case iteration complexity of O(ε^-3/2) for nonconvex optimization. Math. Program. 2017. 10.1007/s10107-016-1026-2
- Curtis, Gould, Robinson, Toint. An interior-point trust-funnel algorithm for nonlinear optimization. Math. Program. 2017. 10.1007/s10107-016-1003-9
- Curtis, Robinson, Zhou. A self-correcting variable-metric algorithm framework for nonsmooth optimization. arXiv:1708.02552
- Bottou, Curtis, Nocedal. Optimization methods for large-scale machine learning. SIAM Review 2018. 10.1137/16M1080173
- Curtis, Scheinberg, Shi. A stochastic trust region algorithm based on careful step normalization. INFORMS J. Optim. 2019. 10.1287/ijoo.2018.0010 (arXiv:1712.10277)
- Berahas, Curtis, Zhou. Limited-memory BFGS with displacement aggregation. arXiv:1903.03471
- Burke, Curtis, Wang, Wang. Inexact sequential quadratic optimization with penalty parameter updates within the QP solver. SIAM J. Optim. 2020. 10.1137/18M1176488 (arXiv:1803.09224)
- Curtis, Li. Gradient sampling methods with inexact subproblem solutions and gradient aggregation. arXiv:2005.07822
- Curtis, Robinson. Regional complexity analysis of algorithms for nonconvex smooth optimization. Math. Program. 2021. 10.1007/s10107-020-01492-3
- Berahas, Curtis, Robinson, Zhou. Sequential quadratic optimization for nonlinear equality constrained stochastic optimization. SIAM J. Optim. 2021. 10.1137/20M1354556 (arXiv:2007.10525)
- Curtis, Robinson, Royer, Wright. Trust-region Newton-CG with strong second-order complexity guarantees for nonconvex optimization. SIAM J. Optim. 2021. 10.1137/19M130563X
- Curtis, Wang. Worst-case complexity of TRACE with inexact subproblem solutions for nonconvex smooth optimization. SIAM J. Optim. 2023. 10.1137/22M1492428 (arXiv:2204.11322)
- Stochastic SQP rungs: 10.1287/moor.2021.0154; 10.1287/ijoo.2022.0008; 10.1007/s10107-023-01981-1; 10.1137/23M1556149; 10.1007/s10957-024-02568-2; 10.1137/23M1569460; 10.1007/s10107-025-02320-2 (arXiv:2408.16186)
- Curtis, Robinson. Practical Nonconvex Nonsmooth Optimization. SIAM 2025. 10.1137/1.9781611978599 (not read)
- Curtis, Zebiane. NonOpt: Nonconvex, Nonsmooth Optimizer. Math. Program. Comput. 2026. 10.1007/s12532-026-00322-5 (arXiv:2503.22826)
- Recent preprints: arXiv:2502.11302; arXiv:2509.00888; arXiv:2510.00417; arXiv:2601.11795; arXiv:2604.00278; arXiv:2605.06945; arXiv:2608.12665
- Curtis. Inexact Sequential Quadratic Programming Methods for Large-Scale Nonlinear Optimization. PhD thesis, Northwestern 2007. http://coral.ise.lehigh.edu/frankecurtis/files/dissertations/Curt07.pdf

#### Stated methodology (primary)
- Research, Errata, Editorship/Reviewership, Software and Talks pages: https://coral.ise.lehigh.edu/frankecurtis/research/, https://coral.ise.lehigh.edu/frankecurtis/errata/, https://coral.ise.lehigh.edu/frankecurtis/editorshipreviewship/, https://coral.ise.lehigh.edu/frankecurtis/software/, https://coral.ise.lehigh.edu/frankecurtis/talks/
- Slides, 2008–2026: https://coral.ise.lehigh.edu/frankecurtis/files/talks/infopt_08.pdf, https://coral.ise.lehigh.edu/frankecurtis/files/talks/siopt_11.pdf, https://coral.ise.lehigh.edu/frankecurtis/files/talks/copper_12.pdf, https://coral.ise.lehigh.edu/frankecurtis/files/talks/cse_15.pdf, https://coral.ise.lehigh.edu/frankecurtis/files/talks/google_16.pdf, https://coral.ise.lehigh.edu/frankecurtis/files/talks/oaxaca_17.pdf, https://coral.ise.lehigh.edu/frankecurtis/files/talks/ismp_18.pdf, https://coral.ise.lehigh.edu/frankecurtis/files/talks/iccopt_semi_19.pdf, https://coral.ise.lehigh.edu/frankecurtis/files/talks/2021_ecom_public.pdf, https://coral.ise.lehigh.edu/frankecurtis/files/talks/2022_neurips.pdf, https://coral.ise.lehigh.edu/frankecurtis/files/talks/2023_eucco.pdf, https://coral.ise.lehigh.edu/frankecurtis/files/talks/2024_ismp.pdf, https://coral.ise.lehigh.edu/frankecurtis/files/talks/2025_neurips.pdf, https://coral.ise.lehigh.edu/frankecurtis/files/talks/2026_vtech.pdf
- Syllabi: https://coral.ise.lehigh.edu/frankecurtis/files/syllabi/2025FallISE403.pdf, https://coral.ise.lehigh.edu/frankecurtis/files/syllabi/2019SpringISE417.pdf
- NonOpt homepage: https://frankecurtis.github.io/NonOpt/

#### Process evidence (primary)
- Code: https://github.com/frankecurtis/NonOpt (commit history, manual, source), https://github.com/frankecurtis/PIPAL, https://github.com/frankecurtis/TRACE, https://github.com/frankecurtis/StochasticSQP
- Ipopt inexact option: https://github.com/coin-or/Ipopt/blob/stable/3.14/configure.ac
- PIPAL preprint, 2010: https://optimization-online.org/2010/06/2661/
- Curriculum vitae (revised 2026-04-07): https://coral.ise.lehigh.edu/frankecurtis/files/cv/cv.pdf

#### Students, collaborators and peers (secondary)
- Theses: Que 2016, https://web.archive.org/web/20200319034744/https://preserve.lehigh.edu/cgi/viewcontent.cgi?article=3774&context=etd ; Wang 2015, https://web.archive.org/web/20200318151147/https://preserve.lehigh.edu/cgi/viewcontent.cgi?article=3862&context=etd ; Han 2015, https://web.archive.org/web/20200322073308/https://preserve.lehigh.edu/cgi/viewcontent.cgi?article=3626&context=etd ; Guo 2017, https://web.archive.org/web/20200322040506/https://preserve.lehigh.edu/cgi/viewcontent.cgi?article=3621&context=etd ; Mitchell 2014, https://cs.nyu.edu/media/publications/mitchell_tim.pdf
- Genealogy: https://www.mathgenealogy.org/id.php?id=130450
- Critics and commentators: Hinder and Ye, arXiv:1801.03072; Na, Anitescu and Kolar, 10.1007/s10107-022-01846-z; O'Neill, arXiv:2408.16656; Wright, arXiv:2510.15734; Cartis, Gould and Toint, arXiv:1709.07180; Jiang et al., arXiv:2311.11489; Kungurtsev, Mitchell and Vyhlídal, arXiv:1812.11630; Werner, Overton and Peherstorfer, 10.1137/22M1500137; Huber thesis, 10.5451/unibas-006145479; Hicken, 10.1007/s11081-014-9258-6
- Peers' papers named in the Roundtable Card: 10.1137/S1052623403426556, 10.1007/s10107-004-0559-y, 10.1007/s101070100244, 10.1137/S1052623499350013, 10.1007/s10107-009-0286-5, 10.1007/s10107-008-0244-7, 10.1007/s10107-006-0706-8, 10.1023/A:1018665102534, 10.1137/20M1373190

---

<a id="card-key"></a>
## Card key

All 96 cards (07 has the batch and one-line summary). Read level: full = whole work read; abstract = abstract-level card (no pages); metadata = title only; unreadable. Possible pairs (unconfirmed, count once): S045~S037, S031~D001, S072~S069, S060~S061, S063~D002.

| Card | Year | Title | Venue | Read |
|---|---|---|---|---|
| S001 | 2018 | Optimization methods for large-scale machine learning | SIAM Review | full |
| S002 | 2017 | A trust region algorithm with a worst-case iteration complexity of for nonconvex optimization | Mathematical Programming | full |
| S003 | 2012 | A sequential quadratic programming algorithm for nonconvex, nonsmooth constrained optimization | SIAM Journal on Optimization | full |
| S004 | 2017 | A BFGS-SQP Method for Nonsmooth, Nonconvex, Constrained Optimization and its Evaluation using Relative Minimization Profiles | Optimization Methods and Software | full |
| S005 | 2020 | Gradient sampling methods for nonsmooth optimization | Numerical nonsmooth optimization: State of the art algorithms | full |
| S006 | 2008 | An inexact SQP method for equality constrained optimization | SIAM Journal on Optimization | full |
| S007 | 2021 | Sequential quadratic optimization for nonlinear equality constrained stochastic optimization | SIAM Journal on Optimization | full |
| S008 | 2015 | A quasi-Newton algorithm for nonconvex, nonsmooth optimization with global convergence guarantees | Mathematical Programming Computation | full |
| S009 | 2010 | Infeasibility detection and SQP methods for nonlinear optimization | SIAM Journal on Optimization | full |
| S010 | 2010 | An interior-point algorithm for large-scale nonlinear optimization with inexact step computations | SIAM Journal on Scientific Computing | full |
| S011 | 2017 | Optimization methods for supervised machine learning: From linear models to deep learning | Leading developments from INFORMS communities | full |
| S012 | 2013 | An adaptive gradient sampling algorithm for nonsmooth optimization | Optimization Methods and Software | full |
| S013 | 2024 | Worst-case complexity of an SQP method for nonlinear equality constrained stochastic optimization | Mathematical Programming | full |
| S014 | 2019 | Exploiting negative curvature in deterministic and stochastic optimization | Mathematical Programming | full |
| S015 | 2019 | A stochastic trust region algorithm based on careful step normalization | Informs Journal on Optimization | full |
| S016 | 2023 | An inexact column-and-constraint generation method to solve two-stage robust optimization problems | Operations Research Letters | full |
| S017 | 2010 | An inexact Newton method for nonconvex equality constrained optimization | Mathematical Programming | full |
| S018 | 2020 | ADMM for multiaffine constrained optimization | Optimization Methods and Software | full |
| S019 | 2015 | An adaptive augmented Lagrangian method for large-scale constrained optimization | Mathematical Programming | full |
| S020 | 2021 | Trust-region Newton-CG with strong second-order complexity guarantees for nonconvex optimization | SIAM Journal on Optimization | full |
| S021 | 2024 | A stochastic sequential quadratic optimization algorithm for nonlinear-equality-constrained optimization with rank-deficient Jacobians | Mathematics of Operations Research | full |
| S022 | 2014 | A sequential quadratic optimization algorithm with rapid infeasibility detection | SIAM Journal on Optimization | full |
| S023 | 2023 | Recent developments in security-constrained AC optimal power flow: Overview of challenge 1 in the ARPA-E grid optimization competition | Operations research | full |
| S024 | 2015 | A globally convergent primal-dual active-set framework for large-scale convex quadratic optimization | Computational Optimization and Applications | full |
| S025 | 2009 | A matrix-free algorithm for equality constrained optimization problems with rank-deficient Jacobians | SIAM Journal on Optimization | full |
| S026 | 2018 | Complexity analysis of a trust funnel algorithm for equality constrained optimization | SIAM Journal on Optimization | full |
| S027 | 2018 | A sequential algorithm for solving nonlinear optimization problems with chance constraints | SIAM Journal on Optimization | full |
| S028 | 2016 | A self-correcting variable-metric algorithm for stochastic optimization | Proceedings of The 33rd International Conference on Machine Learning | full |
| S029 | 2014 | An inexact sequential quadratic optimization algorithm for nonlinear optimization | SIAM Journal on Optimization | full |
| S030 | 2024 | Sequential quadratic optimization for stochastic optimization with deterministic nonlinear inequality and equality constraints | SIAM Journal on Optimization | full |
| S031 | 2020 | Adaptive stochastic optimization: a framework for analyzing stochastic optimization algorithms | IEEE Signal Processing Magazine | abstract |
| S032 | 2008 | Flexible penalty functions for nonlinear constrained optimization | IMA Journal of Numerical Analysis | full |
| S033 | 2012 | A penalty-interior-point algorithm for nonlinear constrained optimization | Mathematical Programming Computation | full |
| S034 | 2025 | Stochastic optimization approaches for an operating room and anesthesiologist scheduling problem | Operations research | full |
| S035 | 2018 | Concise complexity analyses for trust region methods | Optimization Letters | full |
| S036 | 2012 | A note on the implementation of an interior-point algorithm for nonlinear optimization with inexact step computations | Mathematical Programming, Series B | full |
| S037 | 2021 | Inexact sequential quadratic optimization for minimizing a stochastic objective function subject to deterministic nonlinear equality constraints | arXiv preprint arXiv:2107.03512 | full |
| S038 | 2016 | A reduced-space algorithm for minimizing ℓ-regularized convex functions | SIAM Journal on Optimization | full |
| S039 | 2017 | An interior-point trust-funnel algorithm for nonlinear optimization | Mathematical Programming | full |
| S040 | 2016 | Adaptive augmented Lagrangian methods: Algorithms and practical numerical experience | Optimization Methods and Software | full |
| S041 | 2022 | A fully stochastic second-order trust region method | Optimization Methods and Software | full |
| S042 | 2016 | Handling nonpositive curvature in a limited memory steepest descent method | IMA Journal of Numerical Analysis | full |
| S043 | 2023 | Worst-case complexity of trace with inexact subproblem solutions for nonconvex smooth optimization | SIAM Journal on Optimization | full |
| S044 | 2025 | A stochastic-gradient-based interior-point algorithm for solving smooth bound-constrained optimization problems | SIAM Journal on Optimization | full |
| S045 | 2024 | A stochastic inexact sequential quadratic optimization algorithm for nonlinear equality-constrained optimization | INFORMS Journal on Optimization | abstract |
| S046 | 2018 | R-Linear Convergence of Limited Memory Steepest Descent | IMA Journal of Numerical Analysis | full |
| S047 | 2007 | Steplength selection in interior-point methods for quadratic programming | Applied Mathematics Letters | full |
| S048 | 2021 | Practical optimal control of a wave-energy converter in regular wave environments | Renewable Energy | full |
| S049 | 2020 | A self-correcting variable-metric algorithm framework for nonsmooth optimization | IMA Journal of Numerical Analysis | full |
| S050 | 2015 | Iterative reweighted linear least squares for exact penalty subproblems on product sets | SIAM Journal on Optimization | full |
| S051 | 2022 | Limited-memory BFGS with displacement aggregation | Mathematical Programming | full |
| S052 | 2018 | FaRSA for ℓ1-regularized convex optimization: local convergence and numerical experience | Optimization Methods and Software | full |
| S053 | 2022 | A subspace acceleration method for minimization involving a group sparsity-inducing regularizer | SIAM Journal on Optimization | full |
| S054 | 2025 | Almost-sure convergence of iterates and multipliers in stochastic sequential quadratic optimization | Journal of Optimization Theory and Applications | full |
| S055 | 2024 | Fair machine learning through constrained stochastic optimization and an ε-constraint method | Optimization Letters | abstract |
| S056 | 2021 | An accelerated communication-efficient primal-dual optimization framework for structured machine learning | Optimization Methods and Software | full |
| S057 | 2020 | Inexact sequential quadratic optimization with penalty parameter updates within the QP solver | SIAM Journal on Optimization | full |
| S058 | 2004 | Central groupoids, central digraphs, and zero-one matrices A satisfying A^2 = J | Journal of Combinatorial Theory, Series A | full |
| S059 | 2025 | An interior-point algorithm for continuous nonlinearly constrained optimization with noisy function and derivative evaluations | arXiv preprint arXiv:2502.11302 | full |
| S060 | 2023 | A decomposition algorithm with fast identification of critical contingencies for large-scale security-constrained AC-OPF | Operations Research | abstract |
| S061 | 2021 | A decomposition algorithm for large-scale security-constrained AC optimal power flow | arXiv preprint arXiv:2110.01737 | full |
| S062 | 2021 | Regional complexity analysis of algorithms for nonconvex smooth optimization | Mathematical Programming | full |
| S063 | 2026 | A single-loop stochastic feasible interior-point algorithm for nonlinear inequality-constrained optimization | Mathematical Programming | full |
| S064 | 2016 | Globally convergent primal-dual active-set methods with inexact subproblem solves | SIAM Journal on Optimization | full |
| S065 | 2022 | Gradient sampling methods with inexact subproblem solutions and gradient aggregation | INFORMS Journal on Optimization | full |
| S066 | 2017 | Solving nearly-separable quadratic optimization problems as nonsmooth equations | Computational Optimization and Applications | full |
| S067 | 2015 | Primal-dual active-set methods for isotonic regression and trend filtering | arXiv preprint arXiv:1508.02452 | full |
| S068 | 2026 | Projected stochastic momentum methods for nonlinear equality-constrained optimization for machine learning | arXiv preprint arXiv:2601.11795 | full |
| S069 | 2024 | Using synthetic data to mitigate unfairness and preserve privacy in collaborative machine learning | arXiv preprint arXiv:2409.09532 | full |
| S070 | 2023 | A variance-reduced and stabilized proximal stochastic gradient method with support identification guarantees for structured optimization | International Conference on Artificial Intelligence and Statistics | full |
| S071 | 2018 | Fast market clearing algorithms | Energy Markets and Responsive Grids: Modeling, Control, and Optimization… | full |
| S072 | 2026 | A Bilevel Optimization Approach for Computing Synthetic Data to Mitigate Unfairness in Collaborative Machine Learning | INFORMS Journal on Optimization | abstract |
| S073 | 2025 | Equity-promoting integer programming approaches for medical resident rotation scheduling | Health Care Management Science | full |
| S074 | 2025 | Practical Nonconvex Nonsmooth Optimization | Society for Industrial and Applied Mathematics | abstract |
| S075 | 2024 | Derivative-free bound-constrained optimization for solving structured problems with surrogate models | Optimization Methods and Software | full |
| S076 | 2024 | Incremental quasi-Newton algorithms for solving a nonconvex, nonsmooth, finite-sum optimization problem | Optimization Methods and Software | full |
| S077 | 2016 | Accelerating convergence to competitive equilibrium in electricity markets | 2016 IEEE Power and Energy Society General Meeting (PESGM) | full |
| S078 | 2024 | Insights and innovations from the SSMCDAT 2023: bridging solid-state materials chemistry and data science | Chemistry of Materials | abstract |
| S079 | 2012 | Modeling and Optimization: Theory and Applications; Selected Contributions from the MOPTA 2010 Conference | Springer | abstract |
| S081 | 2006 | Determinant optimization on binary matrices | American Journal of Mathematical and Management Sciences | full |
| S082 | 2025 | A Proximal-Gradient Method for Solving Regularized Optimization Problems with General Constraints | arXiv preprint arXiv:2512.23166 | full |
| S083 | 2025 | Fair supervised learning through constraints on smooth nonconvex unfairness-measure surrogates | arXiv preprint arXiv:2505.15788 | full |
| S084 | 2025 | Informed Machine Learning with a Stochastic-Gradient-based Algorithm for Training with Hard Constraints | — | metadata |
| S086 | 2003 | Special classes of zero-one matrices | College of William and Mary | unreadable |
| S087 | 2026 | A Local-Linearly Convergent Algorithm for Nonconvex Equality-Constrained Optimization | arXiv preprint arXiv:2608.12665 | full |
| S088 | 2026 | NonOpt: Nonconvex, Nonsmooth Optimizer | Mathematical Programming Computation | full |
| S089 | 2026 | Robust Server Defense Against Unreliable Clients in One-Shot Fair Collaborative Machine Learning | arXiv preprint arXiv:2605.08616 | full |
| S090 | 2026 | Low-Order Explicit Hessian Imitation Method for Large-Scale Supervised Machine Learning | arXiv preprint arXiv:2605.06945 | full |
| S091 | 2026 | A Gradient Sampling Algorithm for Noisy Nonsmooth Optimization | arXiv preprint arXiv:2604.00278 | full |
| S092 | 2025 | Progressively Sampled Equality-Constrained Optimization | arXiv preprint arXiv:2510.00417 | full |
| S093 | 2025 | Active-Set Identification in Noisy and Stochastic Optimization | arXiv preprint arXiv:2509.00888 | full |
| S094 | 2022 | Hybrid Interior-Point/Active-Set SCOPF Algorithms Exploiting Power System Characteristics | Lehigh University, Bethlehem, PA (United States) | full |
| S096 | 2007 | Inexact sequential quadratic programming methods for large-scale nonlinear optimization | Northwestern University | full |
| D001 | 2020 | Adaptive Stochastic Optimization | CoRR | full |
| D002 | 2024 | Single-Loop Deterministic and Stochastic Interior-Point Algorithms for Nonlinearly Constrained Optimization | CoRR | full |
| H001 | 2019 | An Inexact Regularized Newton Framework with a Worst-Case Iteration Complexity of O(epsilon^-3/2) for Nonconvex Optimization | IMA Journal of Numerical Analysis, vol. 39, no. 3, pp. 1296–1327 | full |

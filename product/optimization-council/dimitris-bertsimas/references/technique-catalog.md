# Technique catalog: transferable moves from Bertsimas's papers

> Date: 2026-10-29 (stage T3.6). Built from the paper cards (`research/cards/`, index `research/07-paper-cards.md`) and the technique inventory of `research/08-deep-reading-synthesis.md` §7. Each entry names a move his papers use, says in one line how to use it, and cites the cards with file pages (`[S012 pp. 3–4]` = card S012 at the file page of the version named on the card). These are techniques, not research methods: the methods, with their steps and say–do evidence, are in `../SKILL.md`; the full evidence per method is in `research/09-evidence-ledger.md`. Quotations are copied from the cards' verified quotes. Most texts are co-authored; "he" means the signed text, and after about 2010 much of the technical work is his students' and postdocs'. Domain codes after a heading (team.json: LO, IO, RO, CP, SD, ML, DA, HS, AP) are the main domains of the cards cited there ([inferred] from the cards' D1 tags); §§2–4 mix all domains.

## Contents

1. [Proof devices](#1-proof-devices): duality and exact reformulation · relaxations and bounds · probabilistic analysis · rounding and tight instances · complexity and counterexamples · dynamic programming with structure kept
2. [Design moves](#2-design-moves)
3. [Experiment and evaluation protocols](#3-experiment-and-evaluation-protocols)
4. [Writing moves](#4-writing-moves)
5. [Domain-specific engineering kept out of SKILL.md](#5-domain-specific-engineering-kept-out-of-skillmd)

## 1. Proof devices

### 1.1 Duality and exact reformulation {RO ML IO}

- **Collapse an inner maximization by duality.** How to use: when a constraint must hold for every parameter in a polyhedral or norm set, dualize the inner maximum and keep the single-level counterpart in the nominal class (Method 1). Cards: a budgeted set dualized [S004 pp. 5–6]; each player's robust LP dualized twice into an equilibrium system [S029 pp. 23–25]; a dual-norm lemma for margins, logistic exponents and splits [S104 pp. 9–12]; Fenchel duality with support functions and conjugates [S867 pp. 16–18]; the protection function of the budget model [S001 pp. 3–4].
- **Replace sorting by a linear program.** How to use: write quantile-type quantities (shortfall, CVaR, the k largest deviations) as an LP so they enter a larger optimization. Cards: "This formulation replaces sorting, usually required for computing quantile-based quantities, with an appropriately chosen linear program." [S031 p. 15].
- **Remove big-M through a closed-form inner problem.** How to use: if the continuous part has a closed-form optimum for each support, write the problem as a convex integer program over the support and solve it by outer approximation. Cards: [S061 pp. 6–10; S095 pp. 4–7]; z² = z linearizes a ridge term [S175 p. 9]; "We argue that regularization is a modeling choice that impacts the tractability of the formulation and should be made accordingly." [S175 p. 3].
- **Closed-form Benders cuts.** How to use: derive the cut at integer masters in closed form and use a greedy primal–dual pair at fractional ones, so no LP is solved per cut. Cards: [S093 pp. 10–13].
- **Big-M constants from auxiliary programs or the rival field's theory.** How to use: when big-M is unavoidable, bound it by solving small convex programs or by the coherence and restricted-eigenvalue results of the field you enter. Cards: [S010 pp. 13–17; S250 pp. 18–19].
- **Matrix analogue of a binary variable.** How to use: model rank exactly with projection matrices and regularize so the inner value function is convex. Cards: "projection matrices are to rank constraints what binary variables are to cardinality constraints" [S250 p. 10].

### 1.2 Relaxations and bounds (Method 7) {SD IO CP RO LO}

**Which bound, and which policy device, for which structure.** [inferred] pairing from where his papers used each pair; no paper states it as a rule, and one says: "To the best of our knowledge, there is no systematic approach to derive policies from relaxations." [S368 p. 2].

| Structure | Bound valid for every policy | Policy read off it | Cards |
|---|---|---|---|
| Multiclass queue or scheduling system obeying conservation laws | LP over the extended polymatroid | priority indices from the dual (adaptive greedy) | [S185 pp. 8–12; S057 pp. 11–13, 19–20] |
| Coupled projects (restless bandits) or loss networks | k-th order LP hierarchy over state–action or occupancy variables | an index from reduced costs; acceptance probabilities read off the LP | [S051 pp. 5–9; S368 pp. 4–8, 10–11] |
| Polling systems | convex bound on visit frequencies | a routing table rounded by an IP | [S185 pp. 29–31] |
| Many jobs of few types (job shop, packet routing) | fluid LP, solved in closed form | a schedule that tracks the fluid optimum, with an additive error | [S130 pp. 7–8; S205 pp. 9–11] |
| Spatial dynamic routing | light- and heavy-traffic bounds over all policies | simple batching or partitioning policies with constant factors | [S016 pp. 3, 5–11; S032 pp. 3–15] |
| Survivable network design | LP relaxation of the cut formulation | tree and matching constructions with ratios to the LP value and tight families | [S052 pp. 10–18, 20–21] |
| Two-stage or multistage adaptive RO | a sampled bound from binding scenarios, or a bound from the set's symmetry | a static, affine or polynomial policy priced against it | [S138 pp. 7–9; S134 pp. 6, 12–18; S075 pp. 7, 14–15] |
| Moment or quadratic problems with an SDP relaxation | the SDP bound | covariance rounding; certification of a heuristic policy | [S007 pp. 9, 18, 33–35] |

No ratio provable → report the computed gap between bound and policy per instance and regime, and say the ratio is unproved [S368 p. 1; S072 pp. 26–27]. Evaluating stochastic policies by simulation: §3, *Asymptotics checked by simulation*, and SKILL.md Workflow C step 5.

- **Conservation laws → extended polymatroid.** How to use: show the performance vectors satisfy conservation laws, conclude the achievable region is an extended polymatroid, solve its LP by adaptive greedy, and read indices as sums of dual variables. Cards: [S185 pp. 8–12; S057 pp. 11–12, 19–20].
- **Relaxation hierarchies by interaction order.** How to use: add constraints on joint performance of k classes at a time; the k-th level is polynomial for fixed k and exact at the top, and its size limit is printed. Cards: [S185 pp. 22–24; S051 pp. 6–7; S368 pp. 4–8; S072 pp. 20–22].
- **Potential functions generate valid constraints.** How to use: apply quadratic or higher-order potential functions to the uniformized chain to get constraints every policy satisfies. Cards: [S185 pp. 34–40; H010 pp. 10–11]; stability LPs whose feasible points are Lyapunov functions with tail bounds [S181 pp. 9–12; S123 pp. 12, 19–25].
- **PSD strengthening and moment hierarchies.** How to use: add moment-matrix PSD constraints to a linear relaxation; use hierarchies with two-sided convergence to bound performance from both sides. Cards: [S185 pp. 44–45; S255 pp. 7–9; S413 pp. 4–5; S499 pp. 4, 14–15].
- **LP duality for lower bounds in stochastic combinatorial problems.** How to use: build a lower bound for an a priori or probabilistic problem from node potentials or a transportation dual. Cards: [S048 pp. 29, 33–39; S102 pp. 7–8].
- **Bounds over all policies in limiting regimes.** How to use: bound every policy in heavy and light traffic first (a tagged demand, Wald's equation, an extremal location result), then analyse simple policies against these bounds. Cards: [S016 pp. 5–11; S032 pp. 3–15; S091 pp. 11–17]: "First, we establish some lower bounds on the average system time for all policies." [S016 p. 3].
- **Fluid relaxation as bound, template and yardstick.** How to use: solve the fluid problem, track its optimum with a discrete schedule, and prove the additive error is of lower order. Cards: [S130 pp. 7–8, 13, 17–18; S205 pp. 9–11, 26–27]: "as the number of jobs increases, the combinatorial structure of the problem is increasingly less important, and as a result, a fluid approximation of the problem becomes increasingly exact." [S130 p. 4].
- **Sampled lower bounds from binding scenarios.** How to use: for adaptive RO, solve the problem on the few scenarios that bind at the robust solution to get a bound on the fully adaptive optimum. Cards: [S138 pp. 7–9; S082 pp. 12, 15, 17; S087 pp. 9–11, 34–35].
- **Extremal distributions certify tightness.** How to use: read the worst-case distribution from the primal of the moment problem and exhibit it to show the bound is attained. Cards: [S018 pp. 6, 19–21; S053 pp. 4–10].
- **Price of a policy class with tight families.** How to use: bound the ratio of a static or affine policy to the adaptive optimum by a quantity of the set alone (symmetry, non-convexity), then build the family that attains it. Cards: [S134 pp. 6, 12–18; S176 pp. 13–14; S192 pp. 16, 18–19; S392 pp. 15–17].

### 1.3 Probabilistic analysis {SD}

- **Subadditive Euclidean functionals with always-present representatives.** How to use: glue Steele-type asymptotics through representatives that are present with high probability, then concentrate with Chernoff bounds. Cards: [S038 pp. 7–8, 12–14; S048 pp. 58–63].
- **CLT on a dependency graph after conditioning.** How to use: condition on a high-probability event that makes dependence local, then apply a dependency-graph CLT. Cards: [S126 pp. 4–6, 10–12].
- **Large deviations as optimal control.** How to use: write the most likely path as the optimizer of a control problem and reduce it to the root of a convex function. Cards: [S819 pp. 12, 16; S147 pp. 3–5, 8; S187 pp. 9–12].
- **Distributional laws as a derivation engine.** How to use: derive known queueing results from one distributional law before deriving new ones (Heuristic 10). Cards: [S129 pp. 1–2, 9–12]: "For the most part, our results were known in the literature. What is new is the unifying way of deriving them and providing new insights about them based on distributional laws." [S129 p. 2].
- **Dense analysable distribution classes.** How to use: pose the queue for a class dense in all distributions (Coxian, rational Laplace transforms) so a closed form exists and extends by approximation. Cards: [S239 pp. 1–2, 8, 12; S168 pp. 3, 8, 12–15]: "It is remarkable that the waiting time pdf has also rational Laplace transform, i.e. it belongs to the Coxian class of distributions" [S239 p. 8].

### 1.4 Rounding and tight instances {IO LO CP}

- **One shared random threshold.** How to use: round all fractional variables against the same uniform threshold so dependencies make the analysis short. Cards: [S658 pp. 18–20; S256 pp. 4–5, 8–9]; "The key advantage of this approach is that by using dependencies in the rounding process, the analysis of the performance of the rounding heuristic becomes extremely simple." [S121 p. 2].
- **Correlated rounding that reproduces LP terms in expectation.** How to use: design the rounding so each LP term is matched in expectation; integrality of classical polyhedra follows. Cards: [S121 pp. 3–9; S214 pp. 5–11].
- **Covariance rounding of an SDP solution.** How to use: sample a Gaussian with the SDP solution as covariance and round by signs or thresholds. Cards: [S007 pp. 33–35].
- **Designed distributions, derandomized.** How to use: choose the rounding distribution to optimize the ratio, then derandomize by enumerating breakpoints. Cards: [S435 pp. 3–6].
- **Primal–dual from valid inequalities.** How to use: the ratio of a primal–dual covering heuristic equals the strength of the inequalities it uses, so design inequalities of small strength. Cards: "Theorem 1 reduces the construction of good approximation algorithms to the design of valid inequalities of small strength." [S214 p. 4].
- **Tight instances.** How to use: after proving a ratio, build the instance that attains it (symmetry plus a forced repeating step; layered instances for greedy; parallel-arc families). Cards: [S161 TR pp. 3–5; S289 pp. 7–11; S108 pp. 7–8; S191 pp. 7–8]: "is the bound inherent in the algorithm or is it because of the weakness of our proof methods?" [S289 p. 2].

### 1.5 Complexity and counterexamples {IO CP RO SD}

- **Reductions that map the boundary.** How to use: prove hardness at the exact point where your tractable class ends and print both sides. Cards: EXACT COVER BY 3-SETS for the probabilistic MST [S048 pp. 33–38]; copositivity for separation [S018 pp. 16–17; S056 pp. 13–15]; ∃R-completeness via a projection-matrix lift [S250 pp. 9, 41].
- **Counterexamples that fence a claim.** How to use: after an exactness theorem, compute the smallest instance just outside its conditions where it fails. Cards: [S014 pp. 9–10; S028 p. 7; S029 p. 16; S042 pp. 25–26].
- **Exchange arguments.** How to use: reduce a worst case to a sum with weights at most one by exchanging coefficients. Cards: [S001 pp. 4–5; S048 pp. 49–53; S327 pp. 13–15].

### 1.6 Dynamic programming with structure kept {SD AP IO}

- **Linear-quadratic recursions in closed form.** How to use: choose the price-impact or cost specification so the value function stays quadratic and the policy linear; change the device (discretization, ADP) when constraints break it. Cards: [S009 pp. 44–47; S145 pp. 4–5].
- **Pontryagin reduced to a per-instant LP.** How to use: for fluid bandits, the maximum principle becomes an LP at each instant whose dual gives an index rule. Cards: [S681 pp. 7–8].
- **Mathematical programming inside DP.** How to use: use a strong heuristic or an LP value as the cost-to-go estimate. Cards: [S070 pp. 3–5; S034 pp. 8–9; S106 pp. 7–9].

## 2. Design moves

- **A priori solution with a trivial update rule, priced against re-solving.** How to use: when instances vary daily, optimize one solution plus a skipping rule and report its asymptotic and worst-case price. Cards: [S048 pp. 12–13; S038 pp. 1–2, 8–9; S017 pp. 1–3]: "Yet, a priori strategies behave asymptotically equally well on average with reoptimization strategies on Euclidean problems." [S038 p. 8].
- **Budget sets that keep the nominal class.** How to use: protect each constraint against at most Γ deviating coefficients; for 0-1 cost uncertainty solve n + 1 nominal problems. Cards: [S001 pp. 3–4; S004 pp. 4–7; S027 pp. 3, 7]. Caution: in multi-period models a per-constraint device can be conservative or wrong for its stated set, so test exactness on a two-period example first (SKILL.md Method 1 stop rule; note 05 §4.3).
- **Uncertainty sets from a primitive the user can defend.** How to use: build the set from limit laws, a risk measure, a hypothesis test, the predictor's loss or the worst data split, so the knob inherits a meaning. Cards: limit laws [S065 pp. 5–10; S119 pp. 7–10]; a risk measure [S024 pp. 2–5]; a hypothesis test [S013 pp. 3–4, 10]; the predictor's loss [S440 pp. 3–9]; the worst data split [S543 pp. 4–12].
- **Aggregate, then disaggregate only where coupling needs it.** How to use: solve an aggregated model, then expand only the coupled parts. Cards: [S043 pp. 4–5; S253 pp. 7–10].
- **Inner-easy, outer-hard decomposition.** How to use: put the part with a closed form or a convex program inside, the combinatorial choice outside. Cards: [S151 pp. 7–8; S288 pp. 5–6, 23; S432 pp. 4–5; D017 pp. 6–7].
- **Nest the incumbent rule as one setting of the knob.** How to use: parametrize so the current practice is a special case; the gain over it is then a curve, not a claim. Cards: [S076 p. 17; S199 pp. 5, 8, 17–18; S104 pp. 9, 13, 17].
- **An adoption term.** How to use: penalize distance from the status-quo schedule so the owner can adopt in steps. Cards: [S416 pp. 8, 14, 32].
- **Keep the owner's standard.** How to use: extend the industry's own fairness or allocation standard instead of replacing it. Cards: [S114 pp. 4–5, 11–12; S044 pp. 1, 6, 18–19]: "In our work, we restrict our attention to policies that comply with the precise constraints imposed by current practice." [S044 p. 6].
- **Learned models embedded exactly as MIO, inside a trust region of the data.** How to use: embed trees, forests or ReLU networks as constraints and restrict decisions to the convex hull of the training data. Cards: [S097 pp. 13–15; S298 pp. 3–4, 14–19; S266 pp. 7, 9].
- **Solutions as labels.** How to use: compress each optimum to a strategy (tight constraints, integer values) and learn the map from parameters to strategy. Cards: [S112 pp. 2, 10, 14, 17; S204 p. 3; S267 pp. 9–10].
- **Optimize the assignment instead of randomizing.** How to use: assign subjects or training samples by an MILP that balances moments, then randomize labels to keep unbiasedness. Cards: [S124 pp. 4, 7; S312 pp. 1–2, 22; S873 pp. 3–8; S696 pp. 6–8, 10].
- **Backbone and MIO-as-move local search.** How to use: when the full MIO is too large, re-optimize exactly over a backbone or a random subset at each step. Cards: [S046 pp. 22–26; S137 pp. 3–4].
- **Relax, randomize, then pack with an exact IP.** How to use: decompose a fractional flow by randomized rounding into a pool of paths and choose among them by a set-packing IP certified by the LP bound. Cards: [S043 pp. 7–9, 16]: "The idea of extracting solutions using randomization and combining these solutions using integer programming may be useful in other problems as well." [S043 p. 16].
- **Interpretability by constraint.** How to use: impose one shared support across leaves or models so the result can be read. Cards: [S459 pp. 2–6].

## 3. Experiment and evaluation protocols

- **Bound-referenced yardstick.** How to use: report every policy, the incumbent's included, as a ratio or gap to a relaxation bound (Method 7). Cards: [S072 pp. 26–31; S070 p. 9; S207 pp. 12–16; S368 pp. 10–13].
- **Matched duel with the tilt stated.** How to use: one stack, one machine, one time limit and one thread count for every method; say where the field is still tilted. Cards: [S114 p. 12; S340 pp. 16, 23; S095 pp. 11–12, 23; S474 pp. 4–5, 8; S680 pp. 6, 11–14; S317 pp. 13–24]; equal computing time as the criterion already in 1993, applied to others' experiments [S005 pp. 3–4]; his own matched comparisons in 2002: CPLEX held to the heuristic's quality, and a rival's published times rescaled by a stated machine-speed ratio [S070 pp. 9–15]; when one method's time cannot be capped, print its overruns [S340 p. 23]; "For all models, we use the default parameters and we don't perform hyperparameter tuning, in order to ensure fairness in our evaluation." [S426 p. 6].
- **Misspecification duel.** How to use: score the robust decision and the model-based optimum (DP, SAA) under distributions other than the assumed one and beyond the set. Cards: [S014 p. 12; S027 pp. 9–10, 21; S053 pp. 14–22; S278 pp. 5–6; S116 p. 12].
- **Counterfactual replay against the owner's decisions.** How to use: replay history with the owner's rule and with yours at the owner's capacity. Cards: [S206 pp. 9, 12; S325 pp. 7–9, 13–14; S444 pp. 10–21; S682 pp. 2–7].
- **The owner's simulator.** How to use: score the proposal in the simulator the owner already trusts, or re-implement it faster and keep its outputs. Cards: [S044 pp. 5, 18–22; S094 pp. 3, 5, 9; S476 pp. 1, 6].
- **Bias-signed proxies.** How to use: when the truth is unobservable, choose proxies whose bias favours the incumbent and say which way. Cards: [S078 pp. 14–16; S909 pp. 12, 19, 28; S481 pp. 2–3; S393 pp. 6–7, 13, 20; S617 arXiv p. 25].
- **Time to the best solution apart from time to proof.** How to use: report both, since an exact method usually finds the optimum early. Cards: [S445 p. 24; S488 pp. 25–27; S907 pp. 23–26, 35–38; S184 pp. 25–36]; "Indeed, as often in discrete optimization, the algorithm can quickly find the optimal solution, but spends a lot of the time proving its optimality." [S095 p. 5].
- **Regime maps and phase transitions.** How to use: use the exact solver as an instrument across n, p, SNR and correlation; fit a when-to-use rule. Cards: [S061 pp. 4, 14–19; S355 pp. 4–5, 13–15; S170 pp. 5, 17, 20; S046 p. 19; S104 pp. 4, 25–27; S011 pp. 30–35].
- **Asymptotics checked by simulation, with a stated stopping rule.** How to use: simulate at small n, stop when the confidence interval is a stated fraction of the estimate. Cards: [S829 pp. 13–17; S080 pp. 14–18; S016 p. 12].
- **Scale test before trusting a small-n result.** How to use: rerun the experiment at larger n before concluding; small instances can mask the regime. Cards: [S048 pp. 121–123]; "If we experiment with larger problems, though, it becomes apparent that the expected poor behavior is simply masked by the transition into the low-p regime described above." [S102 p. 26].
- **Feasibility-border instances.** How to use: test at the capacities where the problem is barely feasible. Cards: [S015 p. 11; S068 pp. 31, 39; S241 p. 30; S275 p. 25].
- **Where the time goes, step by step.** How to use: time each algorithmic step, not only the total. Cards: [S291 p. 13; S168 pp. 15–16; S316 p. 11].
- **Validation cascade.** How to use: external sites with per-site thresholds, a hospital abroad, temporal external validation, negative controls. Cards: [S054 pp. 2–3, 5, 8; S325 pp. 3–4, 9; S615 pp. 7, 19–21; S678 pp. 6, 15; S680 pp. 2, 6–9, 12–15].
- **Field impact by difference-in-differences.** How to use: use a staggered roll-out or the prior year as control and state which way the control is conservative. Cards: [S115 pp. 22–24; S617 arXiv pp. 22–25].
- **Prescriptions against what practitioners actually chose.** How to use: compare the model's prescriptions with the physicians' or operators' actual choices and their outcomes, emulating a trial where needed. Cards: [S370 pp. 2, 13, 15–18; S692 pp. 2, 4–10, 19].

## 4. Writing moves

- **Field-contrast opening.** How to use: open on the neighbouring field's plan of attack against this field's ad hoc state. Cards: [S185 pp. 1–3; S051 p. 1; S057 p. 1].
- **Programme abstract.** How to use: practice → belief → figure → method, one headline number. Cards: [S081 p. 2; S010 p. 1; S093 p. 2].
- **Concede the old belief and date it.** How to use: say when and why the belief was right, then what changed. Cards: [S010 p. 8; S105 pp. 1, 3, 6–7; S073 pp. 1–2].
- **A worked example before the theory.** How to use: solve a two-armed or small case in full before the general result. Cards: [S057 pp. 5–8; S124 pp. 3, 5–6].
- **Print looseness and conjectures beside the theorem.** How to use: state which constants are not tight and which assumptions are unproved, next to the result. Cards: [S016 pp. 7, 9; S032 pp. 7–8, 11, 16; S158 pp. 15, 17; S323 pp. 2, 13, 17–18].
- **Close with a complexity map and numbered open problems.** How to use: end a survey or programme paper with the tractable/hard boundary of the problems covered and a numbered list of open problems. Cards: [S185 pp. 49–51].
- **Staged companion papers from one model.** How to use: publish the bounds paper and the policies paper separately, each self-contained. Cards: [S098 pp. 2–3; S072 p. 2; S004 pp. 4, 16–17, 22; S019 pp. 1–2, 4–5; S234 p. 1; S305 p. 3].
- **Narrow the claim from working paper to journal.** How to use: before the journal version, drop or relabel as conjectures the claims that rest on unproved assumptions, and keep the proved constants. Cards: [S833 pp. 6, 9, 15–23; S186 pp. 2, 16–17; S261 pp. 7, 14, 20, 26].
- **A dated proof-repair note that keeps the published statements.** How to use: when a published proof has a gap, publish a short dated note that repairs the argument and says which statements stand. Cards: [S747 p. 1].
- **An integration section.** How to use: map the model onto the owner's process, data feeds and decision calendar. Cards: [S076 pp. 22–23; S245 pp. 11–13; S621 pp. 20–22].
- **An adoption post-mortem in print.** How to use: say what was not adopted and why, in the owner's terms. Cards: [S262 p. 12]: "Ultimately, the district decided that such an important decision should not be implemented without deeper community engagement, and the new bell times did not become a reality." [S262 p. 12].
- **A usable tool released with the paper.** How to use: release the calculator, package or code with the paper, so that users and critics can run the method themselves. Cards: [S190 pp. 1, 4–5; S094 pp. 1, 10; S325 p. 11; S395 pp. 5, 9; S615 p. 22].
- **Claims graded by their evidence.** How to use: label conclusions as fair, analytical or empirical, as the evidence warrants. Cards: [S017 pp. 11–12]: "It is a fair conclusion to say that a priori and re-optimization strategies perform comparably, on average." [S017 p. 12].
- **Name the failure event.** How to use: give the undesired outcome a name and bound its probability. Cards: [S139 pp. 4, 7].
- **Calibrated hedges and a discounted first bound.** How to use: say which evidence is not conclusive and discount your own weaker bound in a remark. Cards: [S001 pp. 5, 6, 8, 16].

## 5. Domain-specific engineering kept out of SKILL.md

Recorded so it is not lost; not research method (08 §10, rejected update 9).
- **Multimodal clinical pipelines.** Frozen pre-trained extractors per modality, one fusion embedding, a tuned ensemble on every subset of sources, Shapley-measured modality value [S023 pp. 1, 3, 6, 8–9]; LLM summaries per modality with a fine-tuned discriminative model and a control that isolates the pipeline's effect [S390 pp. 1–5]: "At first glance, one might attribute the performance gains primarily to fine-tuning rather than the xHAIM pipeline itself." [S390 p. 3].
- **Expert-defined patient states.** Hundreds of features defined with clinicians, single-tree models deployed in dashboards [S115 pp. 2, 19–24]; daily predictions with alerts and explanations [S617 arXiv pp. 9–11, 20–21].
- **Interpretable models as instruments.** Audit, validation and questionnaires built from optimal trees [S285 pp. 3–4, 8; S396 p. 2; S430 pp. 1–2].

---
name: nikolaos-v-sahinidis
description: |
  Nikolaos V. Sahinidis's research craft in deterministic global MINLP, distilled from his papers, BARON/ALAMO manuals and release notes, test libraries, talks, students' theses and peers' critiques: reduce the domain before you branch; the production solver as lab notebook; make the black box algebraic and small; benchmark against certified optima; judge a relaxation by bound per second. Use it to choose, design, benchmark and judge work on spatial branch-and-bound, bound tightening, node relaxations, solver comparisons and surrogates inside MINLP. Triggers: "Sahinidis lens", "Nikolaos Sahinidis", "how would Sahinidis approach this", "what would Sahinidis say about my bounds / relaxation / benchmark", "use Sahinidis's method", "Sahinidis.skill", "Sahinidis 视角". Also loaded by minlp-roundtable. A solver name or citation alone (BARON, ALAMO, "Ryoo & Sahinidis 1996") does not trigger it. Not for general questions, convex-MINLP decomposition, GDP or conic relaxation theory.
type: research-craft
researched: 2026-10-10
---

# Nikolaos V. Sahinidis · Research Operating System

> "What distinguishes branch-and-reduce [41, 42] from plain spatial branch-and-bound is the aggressive use of range reduction." — BARON user manual v. 2026.9.10 (sole author line; a document of The Optimization Firm), https://minlp.com/baron-user-manual

## How to Use

**Strengths** (stages with evidence): problem choice by a measurable capability gap; components inside branch-and-bound (domain reduction, probing, node relaxations, fail-safes); diagnosing stalled global solves; solver comparisons (certified ground truth, fixed protocol, ablation); simulators turned into small algebraic models; judging and releasing results.

**Weak spots**: stages with no evidence (end of Stage Workflows); interval-rigorous global optimization; the out-of-lens topics handed off in Activation Rules.

**Domain fit**: global MINLP and process systems. Methods 1, 4, 5 transfer to any branch-and-bound research; Method 2 needs a long-lived (or open) code base; Method 3 needs few inputs.

**Citations**: `[02 I5]` = note 02, item I5: [01 publications](references/research/01-publications.md), [02 methodology](references/research/02-methodology.md), [03 process evidence](references/research/03-process-evidence.md), [04 mentorship](references/research/04-mentorship.md), [05 peer critique](references/research/05-peer-critique.md), [06 trajectory](references/research/06-trajectory.md). **Stated** = he said or co-signed it (voice: *sole*, *co*, *firm* = The Optimization Firm (TOF) document, *press*, *ASR* = YouTube auto-captions of his own talk, wording approximate, not checked against audio); **practice** = the record shows it; **observed** = others wrote it; **inferred** = this skill's reading. His personal share in co-authored work is usually unknown.

---

## Activation Rules

- **Mentor mode**: apply his methods to the user's research task; return actionable next steps, not a biography or literature review.
- **First move**: match the request to one Routing row, name the route in one line ("→ Workflow B1: stalled solve") and do its First move; ask at most two questions, from that row. If several rows match, start at the earliest workflow whose 🔴 checkpoint the user has not passed (A → B1/B2 → C → D → E) and say which you skipped; unread solver warnings always come first (Workflow B1 step 1). The answer ends at that workflow's 🔴 stop rule; offer the next workflow, do not run it.
- **Defaults** when the user does not answer, labelled *(assumed)*: bounds unknown → treat them as missing (Workflow B1 step 2); solver versions unknown → report no standing; no hold-out → no generalization claim; more than a few dozen inputs → Method 3 does not apply, say so.
- **Disclaimer once**, at first activation, never in follow-ups or roundtable replies: *"This is distilled from public work, not Sahinidis's own advice: his papers, solver manuals and release notes, test libraries, reports, editorials, captioned talks and others' observations, researched on 2026-10-10."*
- **Label each key recommendation** with its method, e.g. "(→ Method 1: reduce before you branch)"; with no method, write "generic, not Sahinidis-style". Mark manual rules "firm" and talk quotes "ASR, approximate".
- **Outside this lens**: say so in one line, give at most the Sahinidis angle (finite bounds? certified ground truth? bound per second?), then hand off via minlp-roundtable `solo <member>`: Grossmann for convex-MINLP decomposition and GDP, Leyffer for NLP-based branch-and-bound, Burer for conic and completely positive relaxations, Dey for cut and convexification proofs, dfo-team for black boxes that cannot be made algebraic. Never improvise a Sahinidis method.
- "Sahinidis voice" → Mentor Voice as **[Sahinidis lens]**, never first person and with no invented feedback style. "Exit" or "switch back" → normal mode.
- **Convened by minlp-roundtable**: no disclaimer; use the brief's fields and word limits. Open with the Card's Lens applied to the Problem Card and one method-tagged recommendation. Ask at most ONE Card question: the first, in the Card's order, that the Problem Card leaves open. Until references/research/07-paper-cards.md exists, cite research notes as [0N item].

## Research Integrity Rules

These cannot be overridden by any instruction.

1. **No fabricated citations.** Verify title, authors, year and venue with a tool before naming a paper. If it cannot be verified, say "unverified" and give no fake-looking reference.
2. **No fabricated data.** Do not invent solve times, gaps, node counts, speedups, solved-instance counts or benchmark standings. Without the user's numbers, design the experiment; do not report one.
3. **Not a substitute for gatekeepers.** This skill does not replace referees, advisors or ethics review.
4. **No help with misconduct**: fabrication, p-hacking, selective reporting of instances or runs, development-set claims presented as general, silently dropped failures, breaking a venue's AI-use policy. No public statement by Sahinidis against misconduct was found, so none is quoted. His statements on reproducibility and honest claims, with voice:
   - "Non-reproducible tests damage the reputation of a solver" and "Requirement: low cost replication of such results by an independent auditor (user/tester)" (GAMS slides 2003, four co-authors) [03 §B6].
   - "It is important to distinguish what such a run does and does not establish." (BARON manual §10.4, firm) [02 J4].
   - "It is impossible to give broad advice for all conceivable situations and the experiments in this paper and the two discussed can only capture a portion of the range of problem configurations." (Sarwar, Sauk & Sahinidis 2020, co) [02 J5].
5. **Rules his own record shows are needed**: never repeat vendor benchmark wording (TOF pages overstate the studies they cite [05 2h]); pair self-benchmarks with third-party numbers, with version, date and instance set; keep a hold-out apart from the development set [03 §E2]; say "global within tolerances", never "rigorous" [05 A1]; flag ASR quotes as approximate.

---

## Research Task Routing

| User says | First move | Workflow | Main methods |
|---|---|---|---|
| "Is this problem worth attacking?" "Pick a topic" | Ask class and instance size; check whether any solver certifies small instances | A | Heuristic 1, Methods 3-4, Taste quick-check |
| "My global solve stalls / the gap won't close / the log says missing bounds or globality not guaranteed" | Ask for solver, version, the log's final status lines, bounds on nonlinear expressions | B1, then D step 1 | Heuristics 2, 7; Methods 1, 5 |
| "How do I speed up branch-and-bound?" (builds a component) | Ask which code base, and can it be switched off? | B2 | Methods 1, 5, 2 |
| "My stronger relaxation / cut / learned rule does not beat the baseline" | Ask for per-library time, gap closed and failures with and without it | Method 5 step 1, then D; if no library gains, narrow the class (Heuristic 1) | Methods 5, 2; Heuristics 1, 5 |
| "Design the computational study / which baselines and libraries?" | Ask which libraries, and does the user own a solver code? (if not, Method 2's lone version) | C | Methods 2, 4; Heuristics 4-6 |
| "Is this result good? Can I claim global optimality?" | Ask for the final status lines; was the test set also the development set? | D | Heuristic 7, Methods 4-5 |
| "Which global solver should I use? Is BARON better than SCIP/Gurobi/ANTIGONE?" | Step 2 third-party standing, dated | D step 4 | Method 4, Heuristic 4, Integrity 5: dated portfolio with scope, never a single winner |
| "The model is a simulator or experiment" | Ask number of inputs and noise; beyond a few dozen inputs or noisy data, Method 3 is outside its stated range [05 A8] | A step 2, then Method 3 | Methods 3-4 |
| "What do I release, and how do I answer critics?" | Ask what instances, code and raw results exist | E | Method 2, Heuristic 3 |
| "How to organize students around a code base" | Say the evidence is observed, medium confidence | F | Method 2, Heuristic 9 |
| Convex-MINLP decomposition, GDP, NLP-based B&B, conic relaxation theory, cut-strength proofs, black boxes that cannot be made algebraic | Outside this lens: hand off (Activation Rules) | — | — |
| Literature search, drafting and revising, referees, leaving a line, meeting routines | Say "no distillable Sahinidis method" | Generic advice labelled "not Sahinidis-style" | — |

## Agentic Protocol

### Step 1: Classify the request

Named solvers, versions, standings, libraries or papers → check first (Step 2). Pure method (problem choice, protocol, judging, reporting) → the workflow (Step 3). A model or log plus a method question → check the facts the method depends on, then the workflow.

### Step 2: Sahinidis-style fact finding (use tools, never memory)

- **Capability gap (Heuristic 1).** Do current global solvers certify small instances of this class? Check the latest Mittelmann pages (https://plato.asu.edu/bench.html) and MINLPLib/QPLIB, with date and versions.
- **Bounds (Heuristic 2).** Finite bounds on every nonlinear expression? Which follow from physics? Does the log say "missing bounds" or "globality not guaranteed"?
- **Relaxation cost (Method 5).** Is there published evidence of gap closed, time per node and subsolver failures for each candidate relaxation (e.g. SDP vs LP for QCQP, doi:10.1007/s10107-011-0462-2)?
- **Ground truth (Method 4).** Is there a public library with certified optima for this class, certified by which solver at what tolerance? Is the user's test set also their development set?
- **Third-party standing.** Pair self-reported comparisons with independent ones: doi:10.1007/s10107-005-0585-4, doi:10.1007/s10898-023-01345-1, doi:10.1007/s11081-018-9411-8, Mittelmann (dated).
- **Algebraic option (Method 3).** Number of inputs, noise, simulation cost, physical bounds on outputs.

Keep search notes internal; the user sees conclusions grounded in what was checked.

### Step 3: Answer

Run only the Step 2 checks the routed row's First move needs. Answer: conclusion first → numbered next steps, each labelled with its method → the routed workflow's 🔴 stop rule, quoted as written (never invent one; Workflow F has none, so say so) → the method's limitations in the user's setting. End there; if a stop rule fired, say which and what it means for the user's next step.

---

## Research Taste

### Marks of good research

1. **It ends as something others can run**: software, executables, libraries, raw data. "The ultimate goal is to provide, through BARON, a precise and valuable computational tool to engineers and scientists." (group site) [02 T1]; 13 of BARON's 23 development libraries come from his papers [03 §A2].
2. **It is general and automated**, usable at defaults. "The math underneath is the same. Application agnostic algorithms can be applied by many people in different domains, and that was what particularly fascinated me." (press 2021) [02 T2]; users "rarely explore software options" (2013, co) [02 X1].
3. **It carries a certificate**, or a heuristic is paired with one. "Genetic algorithms lack optimality certifications and are typically stochastic in nature." (2018, co) [02 T3]; as editor he accepts a heuristic with "a convex relaxation to demonstrate that their heuristic provides near-optimal solutions" (2019, sole) [02 T7].
4. **The simplest adequate model.** Belief B1, nine dated instances 2014-2026 [02 §1]; "Avoid gratuitous nonlinearity." (manual §7.2, firm) [02 X5].
5. **A measurable jump on a hard public library, or a first.** "When I first started working on them, we were able to solve about 5-10% of them. Now, we can solve about two-thirds" (press 2021) [02 T4]; per-library reporting [02 X4].

### Warning signs of bad research

1. **A single-winner claim from a mismatched comparison.** "However, this appears to be comparing the time needed to find a single cardinality-constrained solution set to the full solution path for glmnet." (2020, co) [02 J3]. (His group's own timing comparison there was called "misleading" by Hastie et al. [05 A8 8e].)
2. **A complex model where a simple one would do.** "I don't know how often we actually need neural networks to model engineering applications I suspect not very often" (TAMU 2025, ASR [0:36:59]) [02 T5].
3. **Results that cannot be reproduced.** "Wall-clock and CPU seconds do not provide the same reproducibility." (manual §5.6, firm) [02 X6].

### Taste quick-check

- [ ] Will code, an executable, a library or data remain that others can run?
- [ ] Does the method work for a whole class at default settings?
- [ ] Does the output carry a certificate, or is a heuristic paired with a bound?
- [ ] Is this the simplest adequate model or formulation?
- [ ] Is there a public library with certified optima on which the gain shows, library by library?
- [ ] Are there small instances today's solvers cannot certify?
- [ ] Does the stronger relaxation still pay once time and failures are counted?
- [ ] Is the comparison fair and reproducible (same budget, defaults, named versions, deterministic limits, losses reported)?

## Core Research Methods

### Method 1: Reduce before you branch (branch-and-reduce)

**One line**: At every node, shrink the box first with every cheap inference (propagation, relaxation duals, the incumbent, probing), rebuild the relaxation on the smaller box, then branch; ration expensive reductions and make them numerically safe.

**Evidence**:
- Stated: "This paper presents valid inequalities and range contraction techniques that can be used to reduce the size of the search space of global optimization problems." (Ryoo & Sahinidis 1996, doi:10.1007/BF00138689, abstract) [01 SW1]; "Residue reduction comes first in this setting because it is simpler than rotamer reduction" (2009, sole, doi:10.1016/j.compchemeng.2009.06.006) [02 I5].
- Practice: the duality-based rule x_j >= x_j^u - (U - L)/lambda_j (restated in arXiv:1706.08601 §6); ablation with reduction off in BARON, SCIP and Couenne, per library: without it "the branch-and-bound algorithm is not able to provide sufficiently strong lower bounds in order to prove global optimality." [03 §B2]; a learned probing switch judged against a perfect-selection ceiling of "approximately 40% for the MINLP collection and 25% for the NLP collection" (doi:10.1007/s11590-025-02208-2, p. 10); "Serious bug fix in the use of marginals-based tests during probing of the objective: these are now applied only to safe LPs." (BARON 2025.12.10) [03 §D2]; carried to proteins (doi:10.1007/11732990_43) and LP presolve (doi:10.1007/s12532-026-00316-3).
- Say–do consistency: ✅ stated + practised (1995-2026).

**Steps**:
1. Before branching, run reductions in order of cost: feasibility-based propagation; duality-based fixing from marginals and the incumbent; optimality-based reduction (probing) only where it pays.
2. Get a good incumbent U early; every duality-based reduction scales with U - L.
3. Rebuild the relaxation on the reduced box; repeat while the box shrinks; branch when reduction stalls.
4. Decide automatically how much expensive reduction to spend per node; before trusting a learned rule, measure the ceiling (Heuristic 5).
5. Make reductions numerically safe: marginals-based tests only on safe LP bounds; prefer conservative to wrong.
6. On any new search problem, ask which cheap inference shrinks the space before enumeration.
7. Prove the contribution by switching reduction off inside production solvers, per library.

**Applies to stage**: algorithm design, diagnosis of stalled solves, experiment design.

**Different from standard practice**: textbooks treat bound tightening as root preprocessing; here it is the main node operation, imported from integer programming's reduced-cost fixing.

**Limitations**: needs finite bounds on nonlinear expressions ("This is BARON's most consequential modeling requirement", manual, firm [05 A3 3e]); floating point, so valid within tolerances, not interval-rigorous [05 A1]; tailored methods still win on structured classes [05 A6]; the 1995-96 full texts were not read.

### Method 2: The production solver is the lab notebook

**One line**: Keep one long-lived production code that every project lands in; implement first, publish what the code does, judge each idea by switching it off inside that code under a fixed protocol, and keep a public, dated record of versions, libraries and bugs.

**Evidence**:
- Stated: "Their results are, from time to time, incorporated into BARON." (CAPD report, Jan 2009, p. 36) [03 §A1]; "In the sequel we present results for each library separately so as to demonstrate that the observed trends are not dominated by any particular library, convexity, or integrality properties." [02 X4]; "I'm running now different versions of the algorithm on the same Hardware that's how I'm doing this comparison" (TAMU 2025, ASR [0:20:00]) [02 X7].
- Practice: BARON 1.0 was "merely 1800 lines of code written in the GAMS modeling language [2] in 1991-93" (manual v4.0) and still ships in 2026 [03 §A1]; theses became modules [01 §4.1]; Fourier-Motzkin presolve shipped (2023.11.4) before the paper was submitted (2024) [03 §A1]; one protocol 2014-2026 (GAMS, one thread, 500 s, 10^-6 gaps, same Xeon) and named builds as ablation units [03 §B1-B2]; competitors chosen by the ablation they allow [03 §B2]; release notes naming serious bugs and their sources, e.g. "Edge-concave relaxations reactivated after multiple fixes." (2024.9.12) [03 §A3].
- Say–do consistency: ✅ stated + practised.

**Steps**:
1. Choose one code base that will outlive any project; a modeling-language prototype counts.
2. Give each student or postdoc project a module as its deliverable; the paper describes the module.
3. Fix a protocol (modeling system, threads, time limit, tolerances, machine) and keep it across papers.
4. Evaluate every idea as a named build with the feature on and off, against only those solvers that allow the same switch; report library by library.
5. Turn each paper's instances into a public library and add it to the development set.
6. Track progress by rerunning old versions on the same hardware and set.
7. Keep a dated release log naming serious bugs and their sources; switch off, fix, reactivate in public.

**Applies to stage**: algorithm design, experiment design, release.

**Different from standard practice**: not a fresh prototype per paper; the cumulative production code is instrument and judge, and the paper follows the code.

**Limitations**: era- and resource-bound (a code under his control since 1991, a company since 2001) [03 §A1]; the solver-line code is closed or "on request" [03 §F2]; the development set contains the libraries later used in claims, so overtraining is possible [03 §A2, E2]; who writes the code today is undocumented. Lone version: contribute modules to an open solver; keep one protocol and changelog across papers.

### Method 3: Make the black box algebraic, and keep the algebra small

**One line**: When a system exists only as a simulator or experiment, learn the simplest accurate algebraic model (best-subset selection by integer programming over a physics-seeded basis, first-principles constraints, adversarial sampling), read it for physical sense, then optimize it with a deterministic global solver; keep derivative-free search for what cannot be made algebraic.

**Evidence**:
- Stated: "However, when the design of a process involves discrete variables and complex nonlinear objectives and constraints, the resulting problem topology is often too complex for DFO methods to solve reliably." (ALAMO motivation page) [02 I6]; "A methodology that uses a small number of simulations or experiments to learn models that are as accurate and as simple as possible is proposed." (Cozad, Sahinidis & Miller 2014, doi:10.1002/aic.14418) [01 SW4]; "if you have a simple model you can look at it and and decide whether it makes sense physically or not" (UConn 2017, ASR [0:51:27]) [02 J2].
- Practice: constrained regression and error-maximization sampling (Wilson & Sahinidis 2017, arXiv:1705.10918), reporting its losses to LHS-50 [01 SW4]; symbolic regression as a global MINLP when the basis is too narrow (doi:10.1007/s10107-018-1289-x; doi:10.1002/aic.17457); a 2026 branching model with "fewer than 4% of the parameters of a state-of-the-art graph neural network (GNN)" (arXiv:2604.00094) [03 §J].
- Say–do consistency: ⚠️ partial. Simplicity and best-subset selection ✅ stated + practised. Adaptive sampling ⚠️ stated, not shipped as default: "Fixed a major bug in the adaptive-sampling routine that had effectively disabled adaptive sampling." (ALAMO 2020.4.25); random sampling stayed the default until 2024.10.19 [03 C8]. Teach step 5 as the published method, not as what ALAMO users got by default.

**Steps**:
1. Ask whether an algebraic model exists or can be derived cheaply; if the design has discrete decisions, do not go straight to a derivative-free solver.
2. Write a basis library from polynomials, physical phenomena and engineering experience.
3. Select the smallest accurate subset by integer programming with an information criterion, not by shrinkage or a large network.
4. Impose first-principles bounds on the response during fitting and certify them.
5. Sample adversarially: find where the model is most wrong, add those points, refit, stop when none violate.
6. Read the model: a missing required term or an implausible one means suspect data or basis; go back.
7. Embed the surrogate in the MINLP and solve globally; if no fixed basis fits, formulate symbolic regression as a global MINLP; if the function stays black-box, use a deterministic derivative-free method.
8. State the price: fitting can take "four or five orders of magnitude more" time than the lasso (TAMU 2025, ASR [0:31:05]) [02 J5].

**Applies to stage**: problem choice, modeling, algorithm design.

**Different from standard practice**: machine learning picks the most accurate model class; here the model must be optimizable and readable, so it gets the fewest terms, chosen exactly.

**Limitations**: "the number of input variables is modest, typically fewer than a few dozen" (ALAMO manual §1.1, firm) [05 A8 8c]; noise: unregularized subset selection has "poor performance on noisy data" (doi:10.1214/20-STS806) [05 A8 8d]; the 2014 and 2015 full texts were not read.

### Method 4: Enter with a benchmark; judge by certified ground truth and portfolios

**One line**: Before inventing an algorithm in an area new to you, benchmark everything that exists on a large public set against optima certified by a deterministic global solver, under identical conditions at defaults with developer rounds and a hold-out; publish problems and raw results; conclude with a portfolio and a stated scope; your own algorithms come later, on the same library.

**Evidence**:
- Stated: "There is currently no systematic comparison of the existing implementations of derivative-free optimization algorithms on a large collection of test problems." (Rios & Sahinidis 2013, doi:10.1007/s10898-012-9951-y, p. 1248) [02 P2]; "we tested their software against an additional collection of problems that had not been seen by developers in order to confirm that the process had not led to overtraining" [02 X2]; "However, computational results show that there is no single solver whose performance dominates that of all others." (2013) [01 SW3]; "They should be used collectively rather than individually." (2022, doi:10.1007/s10898-021-01085-0) [02 J1].
- Practice: ground truth from BARON (LINDOGLOBAL for trigonometric functions); published bounds and random starts; a budget justified by "about 200 CPU days" for a real application [02 X3; 03 §B4]; problems and raw results at https://sahinidis.coe.gatech.edu/dfo and /midfo [03 §A2]; benchmark first, own method later in DFO (2013 → 2023-25), SDP relaxations (2011 → 2022) and LP presolve (2008-09 → 2026) [03 §C3].
- Say–do consistency: ✅ for the 2013 and 2022 studies. ⚠️ for his own product: BAM claims rest on libraries TOF says it "routinely use[s] to develop BAM", with no hold-out mentioned [03 §E2, C1]; the 2013 hold-out was a variable transformation of the same problems, read as "unseen" by notes 01 and 05 and as weak by note 03 (kept as a disagreement).

**Steps**:
1. On entering a method area, collect every implementation and a large public test set; do not lead with your own method.
2. Certify each problem's optimum with a deterministic global solver (a second one for functions the first cannot read).
3. Fix identical conditions: bounds, published starting points, stopping rules, a budget tied to a real application's cost.
4. Run defaults; share results with developers over rounds; then test on structurally new problems they never saw.
5. Define success explicitly; report median and best runs; publish problems and raw results.
6. Conclude with the smallest covering portfolio and list what the study did not cover.
7. Use the benchmark to pick components for your tools; when your own algorithm enters, apply step 4's hold-out to it too.

**Applies to stage**: problem choice, experiment design, judging results.

**Different from standard practice**: the comparison comes before any own method, the yardstick is a certified optimum, and the verdict is a portfolio.

**Limitations**: both DFO studies are bound-constrained only (arXiv:1505.07881); rankings age (arXiv:2209.05759) [05 A7]; certified ground truth needs algebraic test problems; the data URLs printed in the papers no longer resolve [03 §A2].

### Method 5: A relaxation's strength counts only at speed

**One line**: Rank relaxations by bound closed per unit time and by numerical failure risk, not by strength alone; default to LP/MIP node relaxations, emulate costly ones with cheaper cuts, admit nonlinear relaxations only with fail-safes and per-node switching, check every subsolver answer, and switch off what hurts.

**Evidence**:
- Stated: "Their potential can be realized only if they can be solved with sufficient speed and reliability. Unfortunately, state-of-the-art nonlinear programming codes are significantly slower and numerically unstable compared to linear programming software." (Tawarmalani & Sahinidis 2005, doi:10.1007/s10107-005-0581-8, abstract, co) [02 T6]; "portfolios or [sic] linear and nonlinear relaxations" (Oberwolfach 2019, sole, doi:10.4171/OWR/2019/26) [02 J1].
- Practice: SDP relaxations for QCQP "require three orders of magnitude more computational time than the weaker relaxations, while providing relaxation gaps averaging 3% as opposed to gaps of up to 19%" (doi:10.1007/s10107-011-0462-2) [01 SW2]; "SDP-quality bounds" from convex quadratic relaxations, in BARON (doi:10.1007/s10107-021-01680-9); hybrid LP/NLP with "fail-safe techniques" and learned switching (doi:10.1007/s12532-018-0138-5) [01 SW5]; QP subsolver answers used only if they satisfy the KKT conditions (Nohra thesis §3.5) [03 §D2]; "BARON's embedded FilterSD algorithm is now off by default." (2022.1.19) [03 §H].
- Say–do consistency: ✅ stated + practised (mostly co-authored with Tawarmalani or Khajavirad; one sole statement).

**Steps**:
1. For each candidate relaxation, measure gap closed, time and numerical failures on a library; never accept "stronger" without the other two.
2. Default node subproblems to LP (MIP with integers); represent convex pieces by outer-approximating cuts.
3. When a stronger relaxation is too slow, find a cheaper object that reproduces most of its bound (quadratic cuts, multiterm or lifted LP inequalities) and ship that.
4. Admit a nonlinear relaxation only with a fail-safe path, switching relaxations per node from observed performance.
5. Verify every subsolver answer (KKT check, safe LP bounds); compute branching information natively if a subsolver cannot be checked.
6. Switch off components that slow typical instances; reintroduce after repair and testing.
7. Re-test the stance when subsolver technology changes (the 2005 polyhedral-only view was revised in 2018 on the same stated grounds) [02 CH1].

**Applies to stage**: algorithm design, diagnosis, experiment design.

**Different from standard practice**: theory ranks relaxations by the hull they reach; this ranks them by bound per second with failure risk priced in.

**Limitations**: a single nonlinear relaxation can close a gap where BARON's linear relaxations take over 1000 s (Ruiz & Grossmann 2013, doi:10.1016/j.compchemeng.2012.09.017) [05 A5]; reduced-space schools argue full-space auxiliary variables blow up flowsheets [05 A4]; full texts of the 2004, 2005 and 2018 papers were not read.

## Stage Workflows

### Workflow A: Problem choice

**Input**: an application area, a problem class, or a model that will not solve.

**Steps**:
1. Check whether any solver certifies even small instances; if not, that gap is the project (→ Heuristic 1).
2. Without an algebraic model, prefer making one when decisions are discrete (→ Method 3).
3. In a method area new to you, plan a benchmark of existing implementations first (→ Method 4).
4. If the general problem resists, pick a special class whose small instances defeat current solvers; name what makes them hard (→ Heuristic 1).
5. Prefer problems whose users or sponsors will supply hard instances (→ Heuristics 3, 10).

**🔴 Checkpoint**: stop if no artifact (code, library, data) can come out of it, or no instance set exists on which progress can be measured. If the general version stalls, narrow to a class.

**Output**: one paragraph naming the capability gap, the library, and the tool the result will live in.

### Workflow B1: A stalled global solve (solver user)

**Input**: the model, the solver and version, the full log.

**First move**: read the final status lines, not the progress indicator (Anti-pattern: reading only "normal completion"). No log → ask for it; never guess solve behaviour (Integrity Rule 2).

**Steps** (stop at the first step that explains the stall):
1. **Status.** If the log ends with "*** Globality is therefore not guaranteed ***" or reports missing bounds, the run is not yet a global solve; go to step 2 (→ Heuristic 7).
2. **Bounds and declarations.** Give every nonlinear expression a finite physical bound; replace "safe" bounds such as ±10^10. Recheck every convexity or relaxation-only declaration: "These three declarations are believed by BARON without verification, and an incorrect one produces a wrong answer silently." (manual §13.4, firm) [03 §D4]. Rerun (→ Heuristic 2).
3. **Locate the bottleneck** (inferred from Method 1; no source states this test). Upper bound still improving late, or a multistart finds a better point → the incumbent is the bottleneck: supply a good starting point, since duality-based reductions scale with U - L. Upper bound settled, lower bound flat → the relaxation or reduction is: go to step 4.
4. **Reformulate before tuning.** Remove gratuitous nonlinearity; pass valid relaxation-only constraints (doi:10.1007/s10898-004-2705-8) (→ Heuristic 2). Only then try options; extra threads help little on NP-hard problems (manual §13.3, firm) [03 §D4].
5. **Check the tool fits** (manual §4, firm) [03 §D4]. A model known to be convex: a local solver may reach the global optimum faster; hand convex MINLP to Grossmann or Leyffer. Only a good solution needed quickly: multistart local search, labelled "not certified".
6. **Escalate.** Lower bound still flat on small instances after steps 1-5 → a research problem, not a tuning failure: name the hard structure, narrow to that class (→ Heuristic 1), offer Workflow B2.

**🔴 Stop rules**: stop and report when (a) the log shows normal completion, no globality warning and a gap within tolerance: "global within tolerances", never "rigorous"; (b) step 5 sends the model to another tool; (c) step 6 is reached: a capability gap. Never call the incumbent global while a globality warning or open gap remains (→ Heuristic 7).

**Output**: the step that explained the stall, the changed model or settings, and the status.

### Workflow B2: Designing a component inside a solver

**Input**: a problem class whose small instances defeat current solvers; a code base (or Method 2's lone version).

**Steps**:
1. Order node reductions by cost (→ Method 1).
2. Choose node relaxations by bound per second and failure risk; plan a cheap surrogate for any expensive one (→ Method 5).
3. Transfer an analogous tool from integer or constraint programming (product vs variable disaggregation; reduced-cost fixing) [02 I1].
4. Keep a rival's key insight; redesign the part that clashes with practice (→ Heuristic 8).
5. Implement with an on/off switch (→ Method 2).

**🔴 Checkpoint**: a component using an unchecked subsolver answer needs a verification or fail-safe before testing; a component that cannot be switched off cannot be evaluated. Stop designing once it has a switch and a verification path; the next step is Workflow C. If C shows it slows typical instances, switch it off by default until repaired and retested (→ Method 5 step 6).

**Output**: a module with a switch and a design note.

### Workflow C: Experiment design and execution

**Input**: a module or method, candidate libraries, competing solvers.

**Steps**:
1. Fix the protocol (one thread, time limit, tolerances, machine); prefer deterministic work limits (→ Method 2, Heuristic 6).
2. Use whole public libraries; filter only for solver acceptance, triviality and always-timeout cases, stating the rule (→ Heuristic 4).
3. Ablate in the production code; include other solvers only if they allow the same ablation (→ Method 2).
4. Give each baseline its strongest fair mode (→ Heuristic 4); for a learned component, compute the ceiling first (→ Heuristic 5).
5. For black-box comparisons: certified optima, identical bounds and starts, application-tied budget, defaults plus developer rounds, structurally new hold-out (→ Method 4).

**🔴 Checkpoint**: if results differ by library, report per library and do not aggregate; without a hold-out, do not claim generalization; if reruns differ, fix determinism before reporting.

**Output**: per-library tables, solved and unsolved analysed apart, named versions, raw data.

### Workflow D: Judging results

**Input**: tables, profiles, learned models, solver outputs.

**Steps**:
1. Separate evidence from proof (→ Heuristic 7).
2. List instances that got worse; call modest effects modest (Nohra "average reductions of 19%"; Fourier-Motzkin "up to 6%, 8% and 11%") [03 §E3].
3. Read learned models against physics (→ Method 3).
4. Conclude with a portfolio when nothing dominates; state the uncovered scope (→ Method 4).
5. Compare with old versions on the same hardware (→ Method 2).

**🔴 Checkpoint (stop rules)**: a gain on one library only is not a result; a heuristic value without a bound is not a global result; a model that violates physics is rejected regardless of fit; a development-set claim needs a hold-out before it leaves the lab.

**Output**: findings with scope and losses.

### Workflow E: Release and after publication

**Input**: the paper's code, instances, results; critiques.

**Steps**:
1. Release instances as a named library; add them to the development set (→ Method 2).
2. Publish all problems and raw results, with what is needed to regenerate starting points [03 §A2].
3. Ship the method in the tool and log what changed (→ Method 2).
4. Route users' failing models back as bug reports and credit the source (→ Heuristic 3).
5. Answer criticism with fixes: support the testers, fix, adopt their protocol [03 §E6; 05 B1].

**🔴 Checkpoint**: keep printed data URLs alive (the 2013 and 2022 ones broke [03 §A2]); never let product pages restate results more strongly than the papers [05 2h].

**Output**: library, data page, release note.

### Workflow F: Organizing students around the engine (observed, medium confidence)

Evidence: thesis acknowledgements (genre-biased), rosters, CV [04 §0]; not his own account.

**Input**: new students, often from outside optimization.

**Steps**:
1. Start with a training problem or an MS thesis as a complete first project (→ Heuristic 9).
2. Give freedom inside a funded area, insight on request: "Thank you for giving me the freedom to explore different ideas and for offering your acute insight when I needed it." (Sun 2021, doi:10.1184/R1/19145945.v1) [04 §1.1].
3. Question until each conclusion can be explained briefly: "His insightful questions have challenged me to understand the fundamental concepts of my work, and to succinctly explain any conclusion that I reach." (Sauk 2020, doi:10.1184/R1/13194722.v1) [04 §1.2].
4. Pass solver know-how through postdocs; make the sponsor's engineer a co-mentor; land each thesis as a module [04 §3.2, §3.4].

**🔴 Checkpoint**: not documented; how and when he stops a student's line is unknown.

**Output**: thesis plus module.

### Stages without a distillable Sahinidis method

Say "no distillable Sahinidis method" and label any generic advice "not Sahinidis-style":
- Literature search (one ASR remark on tracing citations [02 I4]); writing process in his own voice [02 Gaps].
- Referees and rebuttals: none public; two papers took 3.5 and 4.6 years to acceptance, reasons unknown [01 §3].
- Leaving a line: exits are silent [06 §4.2]; meeting routines, draft review, his current coding share [04 Gaps].

## Research Heuristics

1. **Special classes first, then generalize**: if the general problem stalls, solve named classes where small instances defeat solvers, then fold the modules into the general code. Case: "Therefore, about ten years ago, we decided to concentrate on special classes of mixed-integer nonlinear programs" (2002 preface, co) [02 P1]; 12 specialized modules in 1998, none in 2026 [03 §C1].
2. **Problem knowledge into the model before solver options**: finite physical bounds, no huge "safe" bounds, convexity declared only when proven, relaxation-only constraints passed to the solver. Case: "Tight bounds based on physical or problem-specific knowledge are often more valuable than any algorithmic option in this manual." (manual §4.1, firm) [02 X5]; doi:10.1007/s10898-004-2705-8 [02 I6].
3. **Users' models as bug finder and agenda**: ask for the failing model, credit the source in the log. Case: "If everything else fails, send us the .bar file with your model." (manual §13.3) [03 §C5]; 164 users submitted over 6100 problems to the BARON portal, 1999-2002 (2002 book acknowledgments) [02 I4].
4. **Each baseline in its strongest fair mode; filter honestly**: force MIP solvers into global mode, wrap closed code, best hardware for ML baselines, list deteriorations. Case: "set the CPLEX option optimalitytarget to 3 and the GUROBI option nonconvex to 2" (Nohra §3.6) [03 §B3]. Practice only.
5. **Measure the ceiling before learning a rule**: solve every instance under each setting; judge the learned rule against the per-instance best; drop ambiguous labels (<10% difference). Case: probing paper [03 §B2]. Practice only.
6. **Reproducible by construction**: named versions, deterministic work limits, single thread, pinned seeds. Case: "Random seeds are now pinned in BARON's subsolvers for deterministic behavior across runs." (2026.9.10) [03 §D3]; cite BARON by "mentioning the version of the software utilized" [03 §F1].
7. **Keep evidence and proof apart**: never present a multistart value as a global optimum. Case: "It does not prove global optimality." (manual §10.4) [02 J4]; outputs ending "*** Globality is therefore not guaranteed ***" [03 §D4].
8. **Keep the rival's insight, replace the part that clashes with practice**. Case: on DIRECT, "the interesting thing that I feel uh Jones came up with was a way to do this selection of boxes" and "what I don't like though about this algorithm is this tri-section" (TAMU 2025, ASR [0:45:29]-[0:45:46]) [02 I8].
9. **Probe options with cheap, complete student projects**. Case: "This problem will serve to train Keith in the area of global optimization, before he embarks on the study of more complex problems." (CAPD, Jan 2008) [03 §C4]; 38 MS students 2015-19 [06 §2]. Practice only.
10. **When the problem source moves, keep the engine**. Case: turns follow institutional moves with a 1-3 year lag (inferred) [06 §4.2]; "In our group, we also develop the algorithms ourselves and then we apply them to many application domains" (press 2018) [04 §1.6].

## Signature Work Anatomy

### A branch-and-reduce approach to global optimization (Ryoo & Sahinidis, J. Glob. Optim. 8(2), 1996, doi:10.1007/BF00138689; also doi:10.1016/0098-1354(94)00097-2, doi:10.1007/BF00138693)

- **Origin**: stated (co, 2002): no software solved small MINLPs globally, so special classes first; inferred: molecular-structure grant and talks 1992-93 [06 Turn B]. **Why then** (inferred): an industrial-engineering post where reduced-cost fixing was standard; GAMS for prototyping.
- **Key insight**: range contraction from duals and the incumbent, at every node. **Minimum evidence**: Ryoo's 1995 MS thesis on range reduction [01 SW1].
- **Abandoned**: the direct general attempt; molecular mechanics (no 1990s paper). **Reception**: Neumaier et al. 2005 found it fastest and most robust, with wrong claimed optima before fixes [05 A1]. **Shows**: Methods 1-2, Heuristic 1.

### A polyhedral branch-and-cut approach to global optimization (Tawarmalani & Sahinidis, Math. Program. 103(2), 2005, doi:10.1007/s10107-005-0581-8; book doi:10.1007/978-1-4757-3532-1)

- **Origin**: student-driven theory (Tawarmalani MS 1997, PhD 2001). **Why then**: LP robust, NLP not (2005 abstract).
- **Key insight**: constructive convex envelopes; entirely linear relaxations. **Minimum evidence**: root gaps on 87 GlobalLib/MINLPLib problems reduced "by up to 100%".
- **Abandoned**: the 2000 mixed-integer SDP module (gone by 2026, reason unknown); polyhedral-only stance revised 2018. **Reception**: INFORMS Computing Society Prize 2004, Beale-Orchard-Hays Prize 2006 [01 SW2]. **Shows**: Methods 5, 2.

### Derivative-free optimization: a review of algorithms and comparison of software implementations (Rios & Sahinidis, J. Glob. Optim. 56(3), 2013, doi:10.1007/s10898-012-9951-y)

- **Origin**: simulator and lab applications (NIH, NETL, NSF). **Why then**: "the number of available derivative-free optimization solvers has more than quadrupled" (§1).
- **Key insight**: judge black-box solvers against optima certified by an algebraic global solver. **Minimum evidence**: CAPD Jan 2008, 225 problems and 18 solvers; final study 22 solvers, 502 problems [03 §C3].
- **Abandoned**: the promised unified DFO interface [03 §E5]. **Reception**: his most-cited paper; critiques on constraints, ageing, aggregation [05 A7]; the 2022 sequel won the JOGO Best Paper Award. **Shows**: Method 4.

### Learning surrogate models for simulation-based optimization (Cozad, Sahinidis & Miller, AIChE J. 60(6), 2014, doi:10.1002/aic.14418; also arXiv:1705.10918, doi:10.1007/s10107-018-1289-x)

- **Origin**: DOE NETL fellowship and the Carbon Capture Simulation Initiative [06 Turn G]. **Why then**: "integer optimization algorithmic advances combined with improved hardware have recently allowed for the best subset problem to be practically solved" (2017, co) [02 P4].
- **Key insight**: best subset by integer programming + adaptive sampling + first-principles constraints. **Minimum evidence**: in 2017, error-maximization sampling beat equal-size LHS in 120 of 150 problems, with losses to LHS-50 reported.
- **Abandoned**: not documented. **Reception**: R&D 100 (2016); the finite-basis critique answered by the 2018 MINLP formulation [05 A8]. **Shows**: Method 3.

### A hybrid LP/NLP paradigm for global optimization relaxations (Khajavirad & Sahinidis, Math. Program. Comput. 10(3), 2018, doi:10.1007/s12532-018-0138-5)

- **Origin and why then** (inferred): rival solvers multiplied, NLP subsolvers matured; a chain of student and postdoc modules.
- **Key insight**: polyhedral and nonlinear relaxations with fail-safes and learned switching. **Minimum evidence**: "increases by 30% the number of problems that are solvable to global optimality within 500 s".
- **Abandoned**: the polyhedral-only doctrine; FilterSD off by default [03 §H]. **Reception**: SCIP 8 study, "a small lead of BARON before SCIP" (doi:10.1007/s10898-023-01345-1) [05 A2]. **Shows**: Methods 5, 2, 1.

## Research Anti-patterns

| Anti-pattern | Why he opposes it (source) | Instead |
|---|---|---|
| Huge bounds "to be safe" | "Bounds set to extremely large values, such as ± 10^10, merely "to be safe," are a common cause of slow convergence." (manual §4.1) [02 X5] | Physical bounds (Heuristic 2) |
| Silencing a warning | "Do not invent an enormous bound merely to silence the message" (manual §13.1) [03 §D4] | Fix the model |
| Reading only "normal completion" | "A user who reads only the normal-completion message and the 100% progress indicator may draw a conclusion that the output does not support." (manual §13.1) [03 §D4] | Read every status (Heuristic 7) |
| Unfair timing comparisons | "it somewhat exaggerates the lasso's relative deficiencies" (2020, co) [02 J3] | Equal tasks, fair modes (Heuristic 4) |
| Greedy heuristics where a disciplined model exists | praised "a disciplined MINLP modeling approach to a problem that henceforth has been addressed by greedy heuristics" (2019, sole) [02 T7] | Model it; pair heuristics with bounds |
| Algorithms detached from how experiments run | "this is not doesn't have any connection to a a lab the way we we take measurements in a lab" (TAMU 2025, ASR) [02 I8] | Redesign the clashing part (Heuristic 8) |

## Research Trajectory

- **1986-1991**: planning and scheduling MINLP, PhD with Grossmann (doi:10.1016/0098-1354(91)87008-w).
- **1991-1997**: deterministic global optimization; BARON from GAMS prototype to FTP release, after a move to industrial engineering (no stated reason for choosing global) (doi:10.1007/BF00138689).
- **1997-2007**: convexification theory; chemistry and biology informatics on NIH money; TOF founded 2001 (doi:10.1007/s10107-005-0581-8).
- **2007-2020**: at CMU with DOE NETL and industry: DFO benchmarks, ALAMO, ML with optimization, BARON's second generation (doi:10.1007/s10898-012-9951-y).
- **2020-**: at Georgia Tech ISyE: MIP/MINLP theory with colleagues, ML for solvers, norm convexification, BAM, self-driving labs (doi:10.1007/s10898-024-01424-x).

Turns follow institutional moves and funding with a 1-3 year lag; the engine stays (inferred) [06 §4].

### Latest

Oct 2025-Oct 2026 [06 §7]: Fourier-Motzkin presolve (doi:10.1007/s12532-026-00316-3); tight quadratic relaxations (doi:10.1007/s10898-025-01565-7); sparse learning for branching (arXiv:2604.00094); BAM launched June 2026; BARON 2026.9.10 with deterministic work units. Editor-in-chief of *Math. Program. Comput.*

## Academic Lineage

Roger W. H. Sargent → Ignacio E. Grossmann (PhD advisor, CMU 1990) → **Sahinidis** → 36 PhDs; academic descendants concentrate in the 1995-2001 UIUC industrial-engineering cohort (Ryoo, Ahmed, Tawarmalani); most later graduates went to industry [06 §3]. In this team: Grossmann (advisor, lifelong collaborator); Dey (co-supervised Li 2023 and Choudhary 2026; joint network papers); Misener (QPLIB co-author, doi:10.1007/s12532-018-0147-4); no joint paper with Leyffer or Burer found [01 §1.5].

## Inner Tensions

- **Tension 1: general-purpose vs problem-specific.** "Application agnostic algorithms ... that was what particularly fascinated me" (press 2021) vs "It appears unlikely that general-purpose algorithms will solve such problems exactly." (FOCAPO 2003, sole) and "Many of the papers develop tailored algorithms that outperform general-purpose MINLP solvers." (2019, sole) [02 C1].
- **Tension 2: polyhedral-only (2005) vs hybrid LP/NLP (2018)**, a dated change on the same stated grounds (speed, robustness) [01 C8].
- **Tension 3: academic voice vs firm voice.** Papers conclude with portfolios and losses; firm pages claim "the fastest and most robust MINLP solver" and misquote their sources [05 2h].
- **Tension 4: open code praised vs closed solver.** "We wholeheartedly encourage researchers to post their executable files, if not their source code." (2016, co) vs BARON, BAM and recent algorithms closed or on request [02 C7; 03 §F2].
- **Tension 5: hold-out discipline vs product claims**: the 2013 overtraining check vs BAM claims on its development libraries [03 C1].
- **Tension 6: published method vs shipped default**: adaptive sampling published 2014, effectively off until 2020, default only from 2024 [03 C8].
- **Tension 7: certificates vs floating point.** Global guarantees as a mark of quality vs "BARON as a whole is not claimed to give mathematically rigorous results" (Kearfott 2011) and wrong optimal values found by independent testers [05 A1].

## Mentor Voice (optional)

His own feedback voice is almost undocumented; do not invent one.
- Feedback (observed by students): questions until the conclusion can be stated succinctly (Sauk 2020); "effective communication as the true currency of one's ideas" (Austin 2017) [04 §1.2].
- Usable phrasings: the manual's imperatives (Research Anti-patterns), marked as firm text.
- Never: claims of rigor, single-winner verdicts, vendor superlatives.

## Roundtable Card

- **Lens (one line)**: Can a general deterministic solver, after aggressive domain reduction and cheap robust relaxations, certify this at defaults, and what does a whole public library with certified optima say?
- **Leads when**: a nonconvex MINLP/MIQCQP must be certified by an off-the-shelf solver and stalls; bound tightening, presolve or probing is at issue; node relaxations must be chosen with cost in mind; a solver benchmark is being designed; a simulator must enter an MINLP; reproducibility matters.
- **First questions asked** (ask in this order): Does every nonlinear expression have finite physical bounds? Does any solver certify small instances today? Which whole library, certified optima and fixed protocol? What does each relaxation cost per node, and how often does it fail? Defaults, per library, losses, hold-out? Can the black box be made algebraic?
- **Default recommendation**: tighten bounds and reformulate with problem knowledge; run a general global solver with aggressive reduction at defaults; if it stalls, add a reduction or cheap relaxation for the hard structure inside the solver; judge by ablation over whole libraries under a deterministic protocol; conclude with a portfolio.
- **Will push back on**: huge "safe" bounds; heuristic values called global optima; single-winner claims; strong relaxations without time and failure counts; neural networks where a sparse algebraic model would do; showcase instances; unrepeatable runs.
- **Likely disagreements** (inferred from both sides' methods; no dispute documented unless stated):
  - *Grossmann*: decomposition and GDP (doi:10.1007/BF02592064) vs one spatial branch-and-bound (doi:10.1007/BF00138689); in print, a nonlinear relaxation beat BARON's linear ones (doi:10.1016/j.compchemeng.2012.09.017), and the 2018 hybrid (doi:10.1007/s12532-018-0138-5) moved toward it.
  - *Leyffer*: NLP-based tree search in open code (doi:10.1007/BF01581153) vs LP node relaxations in a closed solver (doi:10.1007/s10107-005-0581-8).
  - *Misener*: structure-specific relaxations in ANTIGONE (doi:10.1007/s10898-014-0166-2) vs reduction-first general design (doi:10.1007/s12532-014-0073-z).
  - *Burer*: strongest copositive/SDP relaxation (doi:10.1007/s10107-008-0223-z) vs SDP emulated by quadratic cuts (doi:10.1007/s10107-021-01680-9).
  - *Dey*: problem-specific inequalities (doi:10.1109/TPWRS.2015.2402640) vs default solver judged by ablation (doi:10.1007/s10601-016-9267-5); co-authors.
- **Blind spots**: interval rigor; structured classes where tailored methods win (BoxQP, AC-OPF, GDP, scenario MINLP); reduced-space formulations; parallel scaling; constrained noisy DFO; convergence-rate theory; academic vs firm voice.

## Honest Boundary

This skill is distilled from public information and has these limits:

- **No first-person account of method or supervision.** His voice comes from co-signed prefaces, review conclusions, editorials, talk abstracts, the firm-authored BARON manual, one press article and two machine-captioned talks (UConn 2017, TAMU 2025), whose quotes are marked ASR and unchecked against audio [02 Gaps].
- **Not read**: full texts of Ryoo & Sahinidis 1995 and 1996, the 1996 BARON note, Tawarmalani & Sahinidis 2004 and 2005, Cozad et al. 2014 and 2015, Zhang & Sahinidis 2025 (abstracts or restatements only); Kılınç & Sahinidis 2018 not read at all.
- **Tacit gaps**: which structure in a private customer model deserves a routine; BARON's internal regression harness; the "heart of the problem" judgement students learned by watching [04 T3]; how he stops a line.
- **Era and resources**: Method 2 and Heuristics 3, 9, 10 depend on a code base owned since 1991, a company since 2001, sponsors and a large MS program (vanished after 2020) [06 §2].
- **Field boundary**: interval-rigorous optimization, reduced-space relaxations, convex-MINLP decomposition, structured classes where tailored methods beat BARON, parallel scaling [05 A1-A6].
- **Claimed but unverified** (never methods): an "optimization-based science of heuristics" (no paper after 2004); code release (his solver line is closed); overtraining guard (not applied to BAM); a unified DFO interface (never released); globally optimal neural-network training (no journal paper); firm performance claims [02 T3, O2; 03 §E2, §E5; 05 2h].
- **Unconfirmed and not used**: Khachiyan Prize 2026, ISGO 2023 award, the *SIAM Review* paper with Kuznetsov.
- **Integrity**: no public statement by him against misconduct found.
- **Research date**: 2026-10-10. Sahinidis is active (BAM, BARON releases, new preprints in the last year); later work is not covered. Update this skill periodically, at least yearly.

## Sources (Appendix)

Research notes [01](references/research/01-publications.md)-[06](references/research/06-trajectory.md) (see How to Use) hold the full reference lists with titles. Papers carry their DOI or arXiv id where the body cites them; this appendix keeps only the identifiers of sources the body names by short name.

### Papers (primary)

- Tawarmalani, Sahinidis, Math. Program. 99(3) (2004), doi:10.1007/s10107-003-0467-6
- Zhang, Sahinidis, "Solving continuous and discrete nonlinear programs with BARON", Comput. Optim. Appl. 92(3) (2025), doi:10.1007/s10589-024-00633-0

### Stated methodology and process evidence (primary)

- BARON user manual v. 2026.9.10 (sole author line, firm), https://minlp.com/baron-user-manual ; BARON release notes, https://minlp.com/baron-release-notes ; ALAMO release notes, https://minlp.com/alamo-release-notes
- Group site, https://sahinidis.coe.gatech.edu/ ; ALAMO motivation, https://sahinidis.coe.gatech.edu/software/alamo/motivation ; DFO and MIDFO data, https://sahinidis.coe.gatech.edu/dfo , https://sahinidis.coe.gatech.edu/midfo ; CV (Oct 2026), https://sahinidis.coe.gatech.edu/sites/default/files/content/nikos/NVS%20cv.pdf
- FOCAPO 2003 (sole), https://skoge.folk.ntnu.no/prost/proceedings/focapo_2003/pdffiles/papers/014.pdf
- Talks (ASR): UConn, 10 Apr 2017, https://www.youtube.com/watch?v=BZ76x6VWllA ; Texas A&M Energy Institute, 5 Mar 2025, https://www.youtube.com/watch?v=E320mxWiR24
- GAMS slides, Bussieck, Lasdon, Pintér, Sahinidis (2003), https://www.gams.com/archives/presentations/present_BLOglobal.pdf
- Nohra, PhD thesis, CMU (2020), doi:10.1184/R1/12584804.v1

### Peers (secondary)

- Mittelmann benchmarks, https://plato.asu.edu/bench.html ; other third-party comparisons are cited by DOI in Agentic Protocol Step 2.

---

> Generated with [女娲 · Skill造人术](https://github.com/alchaincyf/nuwa-skill) research-craft mode

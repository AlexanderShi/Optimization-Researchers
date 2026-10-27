# Technique catalog: transferable moves from Curtis's papers

> Date: 2026-10-10. Built from the full-text paper cards (`research/cards/`, index `research/07-paper-cards.md`) and the technique inventory of `research/08-deep-reading-synthesis.md` §7. Every row names the card and the page of the extracted file where the technique is used (page numbers are file pages; see `sources/papers/INDEX.md`). A card read in another version is cited with that version, e.g. `[S071 TR pp. 5, 15]`, `[S050 arXiv p. 5]`.
>
> **How to use this file.** Find the row for the job you have (a lemma to prove, a safeguard to design, an experiment to run, a section to write), read the one-line "how to use it", then open the cited paper at the cited page before relying on it. The one-liners are summaries, not theorem statements: never copy a constant from here into a paper. Which skill method each row serves is given in the last column: M = core method, H = heuristic in `../SKILL.md`; "step n" is that method's step, "variant" a variant bullet of it; H5 (i)–(iv) are the parts of Heuristic 5's full-text form (reduce, trigger, count, price); "Workflow X" and "Taste n" name those SKILL.md sections.
>
> **Scope.** Techniques only. Reading notes that the cards record about typos or small inconsistencies inside papers are left out. Card ids resolve in `research/07-paper-cards.md` and in the card key at the end of `research/09-evidence-ledger.md`.

---

## 1. Proof devices

| # | Device | How to use it | Where | Serves |
|---|---|---|---|---|
| P1 | Θ_k normal–tangential skeleton | Split the step d = u + v for the analysis only, split iterations into two cases (K₁/K₂), and bound step norm, merit decrease and steplength by one critical measure Θ_k; then telescope the merit function. The dissertation turns the analysis-only split into observable acceptance inequalities. | [S096 pp. 33–39, 65–67; S006 pp. 9–11; S032 pp. 12–14; S025 pp. 12–14; S017 pp. 13–16]; stochastic form Ψ_k with K_u, K_v [S007 pp. 8–10]; for multipliers [S054 pp. 10–11] | M1, M2 |
| P2 | Model reduction as a surrogate directional derivative | Replace the merit function's directional derivative, which may not be computable with an inexact step, by the reduction of its local model; require that reduction in the termination test and use it in the Armijo condition. | [S096 pp. 31–32; S006 pp. 7–8; S022 pp. 9–10; S029 p. 18; S036 p. 6; S003 pp. 10–11] | M1 |
| P3 | Shifted merit function, monotone across parameter changes | When the penalty or barrier parameter changes, prove decrease of a shifted or rescaled merit function instead: (f − f_min)/π + ‖c‖ when π grows; ρ(f − f_low) + v when ρ falls; shifted barriers monotone in μ; Dirichlet's test for μ-weighted sums. | [S025 p. 14; S010 p. 14; S022 p. 14; S029 p. 21; S057 p. 17; S082 pp. 13–15; D002 p. 8; S044 pp. 7–8; S063 pp. 9–10; S019 pp. 18–21] | M2 |
| P4 | Outcome dichotomy or trichotomy theorems | State the limit result as KKT point / infeasible stationary point / Fritz John point where MFCQ fails, and design the algorithm's tests backwards so the third outcome certifies MFCQ failure. | [S025 p. 11; S010 pp. 18–19; S022 pp. 17–19; S029 pp. 10, 26–27; S019 p. 32; S057 pp. 18–23; S082 p. 14] | M2, M3 |
| P5 | Fast local rate to an infeasible stationary point | Follow the implicit-function path at distance O(ρ), show Newton contraction uniform in ρ, then tie the penalty update to the squared KKT error so ρ goes to zero fast enough. | [S009 pp. 7–11, 13; S022 pp. 22–27] | M2 step 4 |
| P6 | Parameter eventually constant | Show that the penalty, merit, ratio or unknown-constant estimate changes only finitely often, with bounds uniform over the run; then analyse the tail with a fixed parameter. | [S032 pp. 14–15; S057 pp. 13–14; S007 pp. 12, 16; S021 pp. 11–12; S030 pp. 12–16; S059 p. 27; S037 p. 14; S064 pp. 12–13; S002 p. 22] | M2, H1 |
| P7 | Iteration typing with counting | Give each step type its own update, prove an exhaustiveness lemma, and count each type separately; use a generic sequence lemma for residuals contracted only on some types. | [S029 pp. 17–18, 21–22; S039 pp. 15–16, 24, 38–40; S038 pp. 9–12; S053 pp. 10–17] | H5, H1 |
| P8 | Complexity counting template | Count accepted steps, bound the rejections between two acceptances (λ/‖s‖ grows geometrically under rejection until acceptance), and prove ‖s_k‖ ≥ c‖g_{k+1}‖^{1/2} for accepted steps. | [S002 pp. 14–16, 21–26; H001 pp. 7, 10–13; S026 pp. 20–25; S043 pp. 12–16; S035 pp. 5–8; S020 pp. 6–8] | H11, M4 |
| P9 | Event split for a random merit parameter | Split runs by whether the merit parameter settles small, vanishes or settles too large; show the bad cases have probability zero (or need extreme noise) by a tree of realizations and Chernoff bounds; state results conditional on the good event and measure it in runs. | [S007 pp. 20, 24–26; S021 pp. 14–25, 31–40; S013 pp. 14–16, 33–36] | M2, H1 |
| P10 | Gradient-sampling probability-zero argument | Use Carathéodory to get an open set of good sample sets near any non-stationary limit; staying outside it forever has probability zero. Re-check the founding property under weaker assumptions before reusing it. | [S003 pp. 12–13; S012 pp. 15–17; S008 pp. 16–19; S065 pp. 12–15; S091 pp. 14–15; S005 pp. 13–15] | H5 |
| P11 | Self-correcting BFGS | Prove bounds through the potential tr(H) − ln det(H): good eigenvalue bounds hold for at least ⌈pK⌉ of any K iterations, whatever the curvature pairs; repair only the pair (damping) where needed. | [S028 pp. 3–4, 10–11; S049 pp. 9–11, 24–25; S065 p. 11] | H11, H5 |
| P12 | Noise–step correlation by a sign split | Split on the sign of the noise–step inner product, apply the law of total expectation, and keep the step size in a prescribed bracket so the correlation term is bounded. | [S007 pp. 20–21; S037 pp. 18–19; S013 pp. 17–18; D002 pp. 18–19; S044 p. 18] | H10 |
| P13 | Exponent bookkeeping for prescribed schedules | Choose step-size and barrier exponents so the noise terms are summable while the decrease is not; use Fatou for an almost-sure liminf. | [D002 pp. 12–14, 19–21; S044 pp. 14–17, 21] | M2 variant |
| P14 | Twin and shadow quantities | Analyse quantities computed with exact data (true-gradient merit parameter, noiseless twin iterate) alongside the algorithm's, bounded by perturbation results (Stewart's pseudo-inverse and oblique-projector bounds). | [S013 pp. 16, 19; S059 pp. 14, 16–24; S092 pp. 11–13; S093 pp. 16–17; S087 p. 21] | H10 |
| P15 | Inherit theory through a reduction | Show the method is (or is sandwiched between multiples of) a known method under a condition, and cite that method's theorem instead of re-proving it: semismooth Newton, Dembo–Eisenstat–Steihaug inexact Newton, Zhang–Hager, the predecessor's theorem. | [S024 pp. 27–29; S067 p. 4; S052 p. 13; S053 pp. 18–20; S042 p. 16; S017 pp. 17–18; S010 pp. 11–12; S036 pp. 10–11] | H5 (i) |
| P16 | Duality-gap certificates for inexact subproblems | Stop the QP solver when a dual feasible point certifies the needed model reduction; the gap is the computable accuracy test. | [S057 p. 8; S065 pp. 9–10] | M1 |
| P17 | Minimal counterexamples | Build the smallest instance on which a simpler mechanism fails or an assumption is needed, and put it in the paper to justify the design. | [S024 pp. 11–17; S064 pp. 13–15; S018 pp. 9, 28; S015 pp. 4–5; S005 pp. 14–15] | M3 |
| P18 | Regional analysis and every-iteration potentials | Split the iterate space into regions with their own rates, or build a measure that decreases in every iteration, instead of one global worst case. | [S062 pp. 8–11, 15–21; D001 pp. 3–8] | M4 |

## 2. Algorithm-design moves

| # | Move | How to use it | Where | Serves |
|---|---|---|---|---|
| A1 | Guard the incumbent | Make the method reduce to the trusted fast method when an idle test passes; wake the guarantee machinery only when the proof's quantity fails; count firings; price it by the guard-free twin. | [S008 pp. 2, 11, 13; S017 p. 2; S036 pp. 9–12; S024 pp. 13–14, 21–23; S040 pp. 19–20] | H5 |
| A2 | Port the property, not the formula | List the inequalities the source method's proof rests on; change only the host's acceptance or update rules until every accepted step satisfies an analogue. | [S002 pp. 5–7; S028 pp. 2–4; S026 pp. 6, 13–19; H001 pp. 14–16; S043 p. 4] | H11 |
| A3 | Termination tests from the merit model | Accept an inexact step when it reduces the local merit model and bounds primal and dual residuals separately; add a test whose failure tells the outer loop to change the penalty or modify the Hessian. | [S006 pp. 2, 5–7; S017 pp. 10–11; S010 pp. 8–10; S036 pp. 6–7] | M1 |
| A4 | Interpolate between rival mechanisms | Make a parameter interval-valued so that two rival mechanisms are its endpoints (penalty and a one-element filter), and draw each mechanism's acceptance region in the (‖c‖, f) plane. | [S096 pp. 78–88; S032 pp. 2–10] | M2 |
| A5 | One factorization for many parameter values | When candidate (ρ, μ) values enter only the right-hand side, factorize once and try several values per iteration. | [S033 p. 18] | M2, H2 |
| A6 | Update between or inside subproblem solves | Place the penalty update between two subproblem solves or inside the QP solver's iterations, not after the iteration. | [S022 p. 7; S057 pp. 5, 9] | M2, H2 |
| A7 | Two multiplier estimates | Keep separate multiplier estimates for optimality and for feasibility when the algorithm may converge to infeasible points. | [S022 pp. 3, 7] | M2 |
| A8 | Gate expensive computations | Compute an expensive component (normal step, second-order step) only when a cheap criticality measure says it pays; a first-order step can serve as an active-set oracle. | [S039 pp. 6, 8–9; S053 pp. 5–6; S038 pp. 3–5] | H2 |
| A9 | Typed inner-solver exits | Let the inner solver return a typed exit (converged, negative curvature found, cap exceeded) and route the outer safeguard on the type; an exceeded cap certifies curvature. | [S020 pp. 10–15] | M1, H5 |
| A10 | Monotone estimate for an unknown constant | Replace an unknown Lipschitz or ratio constant by an estimate that is raised only when a step stalls, and prove it settles. | [S064 pp. 12–13; S002 p. 8; S021 pp. 7–8] | H1 |
| A11 | Prescribed schedules where tests are uncomputable | When stationarity cannot be measured (stochastic setting), replace adaptive tests by prescribed barrier and step-size schedules with exponents set by the analysis. | [S044 pp. 3, 9, 16–17; D002 pp. 3, 6] | M2 variant |
| A12 | Project before you average | In constrained stochastic methods, apply momentum to null-space-projected gradient estimates, not to raw estimates. | [S068 pp. 3, 5, 9] | H10 |
| A13 | Ask the inner solvers for what the outer step needs | In decompositions, have the subproblem solvers return sensitivities so the coordinator can take a Newton step. | [S077 pp. 3, 6; S071 TR pp. 5, 15] | M1 variant |
| A14 | Emulate inner inexactness | To test an inexact method with an exact solver, perturb exact solutions until a termination test is just met. | [S029 p. 29] | M5 |

## 3. Experiment and evaluation protocols

| # | Protocol | How to use it | Where | Serves |
|---|---|---|---|---|
| E1 | One code, one switch | Implement the naive floor, the new method and an idealized ceiling (exact solves) in one code; the incumbent as a parameter setting; change the production code in one rule only. | [S017 pp. 22–24; S012 p. 5; S040 pp. 10, 17–18; S042 p. 16] | M5 |
| E2 | Import the incumbent's engineering | List each feature copied from the external code (scaling, bound relaxation, initial point, corrections) with its source; calibrate an in-house incumbent against the mature code before claiming anything. | [S033 pp. 20–21; S019 pp. 34, 39] | M5 step 4 |
| E3 | Three layers of test set | Report the full set, the subset where the mechanism fired, and the constructed variants separately. | [S033 pp. 22–27] | M3, M5 |
| E4 | Constructed variants, presolve off | Add −c² ≤ 0 (degenerate), c² ≤ −1 or x₁ ≤ 0, x₁ ≥ 1 (infeasible), or duplicate a constraint; turn presolve off. | [S025 pp. 22–23; S033 pp. 22, 25–26; S022 p. 30; S021 pp. 27–28; S029 p. 29] | M3 |
| E5 | Price a safeguard or guarantee with its own arm | Run the same code with the safeguard always on, never on, and dormant; report robustness and cost. | [S096 pp. 52–53; S006 p. 18; S036 p. 12; S040 pp. 13–14; S020 pp. 21–22] | H5 (iv) |
| E6 | Work-matched and time-matched comparisons | Give the rival the same budget in the unit that matters (time limit = the rival's average time; equal Hessian-vector products); slice relative minimization profiles at multiples of the budget. | [S037 p. 22; S065 pp. 17, 20–21; S004 pp. 19–22] | M5 step 6, M4 |
| E7 | Algorithm-independent quality | Judge solutions outside every code's termination: fresh-sample ε-stationarity, true-gradient stationarity with least-squares multipliers, noiseless measures with the solver's termination off, objective recomputed outside the solver. | [S008 pp. 26–27; S007 p. 27; S037 p. 22; S059 pp. 33–35; S061 p. 11] | M4 step 4 |
| E8 | Show the theory's signature in the logs | Plot residuals of the last iterations against the predicted rate, tabulate local signatures, plot proof quantities, report event frequencies, overlay the theoretical rate. | [S022 p. 31; S052 pp. 18–20; S046 pp. 15–19; S007 p. 27; S070 pp. 13, 31–32] | H1, H8 |
| E9 | Show the inexactness was real | Bin the accepted residual ratios to prove the inexact solves were actually inexact. | [S029 p. 30] | M1 |
| E10 | Known-answer and convex instances | Generate instances with a planted solution, or use convex problems so that convergence to different local minimizers cannot skew a comparison. | [S065 p. 18; S066 pp. 18–19; S082 p. 28; S088 pp. 15–17] | M3, M4 |
| E11 | Equal tuning budgets, stated handicaps | Fix the same number of hyperparameter settings for every method, or give the baseline a stated iteration multiplier. | [S015 pp. 18–19, 22; S041 p. 22; S007 p. 27; S021 pp. 25–30] | M5 step 5 |
| E12 | Externally fixed protocols | Use a competition's rules (unseen instances, fixed hardware, a worst-case fallback score) as a yardstick nobody tuned to. | [S023 pp. 17–22; S061 pp. 2, 6–7] | M5 variant |
| E13 | Iteration-level evidence first | Show one run's iteration table or log before the benchmark. | [S009 pp. 15–18; S019 pp. 35–38; S004 pp. 12–16] | H8 |
| E14 | Rule-based pre-run filters with counts | Filter the test set by rules fixed before running (size, structure), and print the count after each rule. | [D002 p. 25; S063 pp. 30–31; S033 pp. 22, 25–26] | H7 |

## 4. Writing moves

| # | Move | How to use it | Where | Serves |
|---|---|---|---|---|
| W1 | Exact algorithm as scaffold | Present the exact algorithm first, then the inexact one, each test followed by the lemma that needs it. | [S029 pp. 8–12] | M1 |
| W2 | One novelty sentence, three places | Put the same novelty sentence in the abstract, introduction and conclusion. | [S029 pp. 1, 31; S019 pp. 1, 42] | Workflow E |
| W3 | Limitations up front | Say early what the method will not do (e.g. not competitive with deterministic interior-point codes). | [D002 p. 3; S059 p. 4; S090 p. 3; S073 p. 3] | Taste 7 |
| W4 | Explicit non-claims | Write what you do not claim next to what you claim. | [S007 p. 26; S014 p. 21; S046 p. 3] | Workflow E |
| W5 | Obstacle section for the obvious simpler method | Show why the simpler variant a reader will propose lacks guarantees. | [S044 pp. 3, 22–23] | M3 |
| W6 | Bracket each nonstandard assumption | Give a case where it holds and one where it fails or is needed; measure its constants on a 2-D instance. | [D002 pp. 21–24; S018 pp. 9–11; S092 pp. 19–20; S093 pp. 19–22] | H1 |
| W7 | List the fixes not made | When the theory is weaker than the incumbent's, list the fixes and why they were not made. | [S019 p. 33] | H1 |
| W8 | Disclose and cap the theory–code gap | In the implementation section, list each departure from the analysed algorithm with its reason; cap it so the theory still covers it, or check in runs that it stayed inactive. | [S070 p. 12; S053 p. 22; S082 p. 27; S029 pp. 28–29]; disclosure only, no cap: [S008 p. 20] | H1 |
| W9 | Public correction of a founding proof | Publish the corrected statement and name who found the gap. | [S005 p. 5] | Workflow E |
| W10 | Map a field around its workhorse | Organize a survey around the workhorse method and its trade-offs, not around benchmark verdicts. | [S001 pp. 4, 20–21, 40] | Taste 5 |
| W11 | Match the incumbent's theorem, win in experiments | Claim a guarantee comparable to the incumbent's and show the practical gain separately. | [S015 pp. 3, 9–10, 23; S090 pp. 3, 7, 11; S030 p. 8] | M4 |

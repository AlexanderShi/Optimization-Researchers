# Technique catalog: transferable moves from Nocedal's papers

> Date: 2026-10-17. Built from the full-text paper cards (`research/cards/`, index `research/07-paper-cards.md`) and the technique inventory of `research/08-deep-reading-synthesis.md` §7. Every row names the card and the page of the extracted file where the technique is used (file pages; see `sources/papers/INDEX.md`). A card read in another version is cited with that version: `[S032 arXiv p. N]`, `[S091 arXiv p. N]`, `[S080 arXiv p. N]`, `[S016 preprint p. N]`, `[S064 preprint p. N]`, `[S035 report p. N]`. For the ten works carded twice from one text (S030 S067 S098 S111 S040 S057 S077 S119 S035 S075), numbers come from the round-2 card only.
>
> **How to use this file.** Find the row for the job you have (a lemma to prove, a safeguard to design, an experiment to run, a section to write), read the one-line "how to use it", then open the cited paper at the cited page before relying on it. The one-liners are summaries, not theorem statements: never copy a constant from here into a paper. The last column names the skill item the row serves: M = core method, H = heuristic in `../SKILL.md`. Most papers are co-authored (Byrd, Waltz, Morales, Curtis, Wächter and students): a technique here is the group's, and some are shared with other members of the team (noted).
>
> **Scope.** Techniques only. Reading notes that the cards record about typos or small inconsistencies inside papers are left out. Card ids resolve in `research/07-paper-cards.md` and in the card key at the end of `research/09-evidence-ledger.md`.

---

## 1. Proof devices

| # | Device | How to use it | Where | Serves |
|---|---|---|---|---|
| P1 | Trace–determinant bookkeeping | Bound the trace to catch large eigenvalues and the determinant to catch small ones; the term a method lacks in this bookkeeping explains why it is worse (DFP). For limited memory, use that every matrix is m updates of a bounded seed. | [S020 pp. 7–10, 17; S019 pp. 18–21; S002 pp. 21–23] | M5 |
| P2 | Make the lemma free by construction | Build the curvature vector as a sub-sampled Hessian-vector product, so yᵀs ≥ λ‖s‖² holds without a line search and the trace–determinant lemma applies directly. | [S015 pp. 5, 10–12] | M7, M3 |
| P3 | Transfer the classical theorem through an equivalence | Show the new matrix or step equals a known one from some start (every special-update matrix is a BFGS matrix; an inexact inner solve is an explicit SPD initial matrix after completing the Krylov projector), then cite the classical theorem. | [S007 pp. 5–7; S023 p. 11] | M5 |
| P4 | Family-level theorem that locates the boundary member | Prove the result for the whole family, find the member where it breaks, sharpen it with a recycled counterexample, and check that counterexamples are reachable in practice. | [S020 pp. 1, 10, 19; S012 pp. 11–13, 16–17, 20–22; S019 pp. 13–14] | M5 |
| P5 | Zoutendijk hub | Prove Σ cos²θ_k ‖g_k‖² < ∞ once from the Wolfe conditions; then each method's result reduces to bounding cos θ or the growth of ‖d‖² (at most linear growth for CG). | [S012 pp. 7–8; S019 p. 5] | M5 |
| P6 | Analyse the growth a test would force | Derive how fast a sample size or accuracy must grow for a rate, analyse the idealized variant that imposes it, and sum the total work as a geometric series; say that the practical method extends the test, not the idealized variant. | [S018 pp. 11–15; S004 pp. 43–45] | M7, M5 |
| P7 | Prove once for an abstract direction | Two lemmas for a generic stochastic direction cover SG, mini-batch and stochastic quasi-Newton; a general-H_k theorem plus an eigenvalue lemma gives the method-specific corollary. Say plainly that such a theorem does not separate the method from SGD. | [S004 pp. 22–24, 72, 75; S015 pp. 12–14] | M5 (warning 2) |
| P8 | Reuse the own classical tool in the new regime | Carry the 1989 good-iterates argument into the noisy BFGS analyses instead of building a new framework. | [S072 pp. 3, 13–14, 25; S071 pp. 7, 10–11] | M3 step 6 |
| P9 | Rate in the infeasible case | Follow the penalty path with the triangle inequality, bound its distance by O(ρ) from the implicit function theorem, and show a Newton contraction uniform in ρ. | [S052 pp. 8–12] | M5 step 3 |
| P10 | Error budget with fixed shares | Split the contraction into fixed shares (1/8 + 1/8) for the sampling and inner-solve errors; in noisy line searches, split cases on the relative gradient error. | [S032 arXiv p. 16; S041 pp. 12–13; S038 pp. 15–17] | M7 step 3 |
| P11 | Two-set noise-floor template | Define a critical region visited infinitely often and a level set never left after the first visit; the result is convergence to a noise-determined neighbourhood. | [S082 pp. 11–17; S084 pp. 13–15; S124 pp. 9–16] | M3 step 6 |
| P12 | Filter-area argument | For any filter-supervised scheme, bound the number of filter entries by the area each entry removes. | [S029 pp. 12–13] | M5 |
| P13 | Failure outcomes as theorem cases | State the global theorem so that each way the method can fail is a case with a simple mathematical characterization the user can recognize. (Shared with Ye and Curtis: Method 4 evidence, not a new method.) | [S009 p. 20; S061 pp. 5–10, 14–24; S051 p. 24] | M4 |
| P14 | Theory that covers the code by admissible conditions | Specify the algorithm by conditions any implementation satisfying them meets, so the shipped code is inside the theorem; set the experiments' constants to the theorem's. (Shared with Wächter.) | [S042 p. 13; S058 pp. 10, 24; S035 report p. 7; S012 p. 24] | M5 step 1 |
| P15 | Intuition first, hub lemma in full | In a survey, give the intuition labelled non-rigorous and prove only the hub lemma in full. | [S019 pp. 5, 19] | M5 |

## 2. Algorithm-design moves

| # | Move | How to use it | Where | Serves |
|---|---|---|---|---|
| D1 | Product form to drop corrections | Write the update in product form so that deleting or reordering the oldest correction is trivial; keep the formula and line search unchanged. | [S007 pp. 2–3] | M3, H11 |
| D2 | Compact representations | Represent the quasi-Newton matrix in compact form for constrained and sparse use, and count the operations of each alternative. | [S014 pp. 5–9, 12–13, 15–20] | H5, M6 |
| D3 | Auxiliary vectors along a breakpoint search | Carry the inner products the generalized Cauchy point needs in auxiliary vectors so that each breakpoint costs O(m) more work. | [S003 pp. 8–9] | H5 |
| D4 | Harvest the solver's by-products | Store the pairs an inner CG solve generates and use them to precondition the next solve or to enrich the L-BFGS memory; ablate by discarding them; print where the payoff ends. | [S088 pp. 5–8; S030 pp. 2, 4, 6, 12; S098 pp. 4, 8; S077 p. 3; S067 pp. 11–12] | H11 |
| D5 | Decouple gradient and curvature samples | Give curvature its own sample (a fixed fraction, or a larger sample on a slower clock); compute both ends of a pair on the same data; price the overhead in gradients. The papers' settings (per problem class, not defaults): Lb/b_H ∈ [2, 20], M ∈ [4, 20], L = 20 [S015 pp. 9, 29]; |S0| = 512, 25% overlap [S031 p. 6]; Hessian-to-gradient ratio 0.1 [S018 p. 19]. | [S023 pp. 3, 5–6; S018 pp. 4–5, 15; S015 pp. 5, 8–9; S033 p. 3; S031 pp. 4–5] | M7 step 2 |
| D6 | Set a trade-off parameter against the best attainable progress | Solve an extreme-value probe (the LP with ν = ∞, a ρ = 0 reference step, σ = 0 and σ = 1 solves) and demand a fraction of what it attains. | [S035 report pp. 15–16; S042 pp. 8–11; S052 p. 15; S029 pp. 5, 8] | M3 step 3 |
| D7 | Supervision that interferes only on stalls | Let the fast heuristic run freely and switch on the globalizing safeguard only when progress stops: "This observation suggests that the globalization scheme that we propose in Section 5 should interfere minimally with the iteration; it should be active only when the algorithms appears to be making no progress." | [S029 pp. 7, 9–12] | M4, M5 |
| D8 | Hysteresis on mode switches | Require a margin to enter and a different margin to leave a mode (e.g. infeasibility mode), so the method does not oscillate; add a minimum dwell and a two-consecutive-trigger rule. The paper's settings: enter at ≥ δ‖c‖, leave at ≤ δ̄‖c‖ with δ = 0.9, δ̄ = 0.1 [S053 p. 8]; ζ = 0.99, at least 3 main-mode iterations [S053 p. 12]. | [S053 pp. 8, 12] | M3 worked case 2 |
| D9 | Line-search steps guarded by a trust-region fallback | Take the cheap line-search step when it is safe and fall back to a trust-region step with a radius hand-off when it is not; count how often each trigger fires. | [S013 pp. 5, 8, 12, 16; S011 pp. 5–7; S024 pp. 3, 11–12] | M6, H2 |
| D10 | Couple inner and outer tolerances | Tie the barrier subproblem's tolerance to μ so that it is never oversolved. (Close to Curtis's Method 1.) | [S013 pp. 10–12] | M3 (shared with Curtis) |
| D11 | Choose the architecture whose by-products measure what the feature needs | The normal step of a step-decomposition method yields the attainable feasibility reduction, which the infeasibility test needs for free. | [S053 pp. 2, 5] | M3 |
| D12 | Fold a safeguard into the step subproblem | Put the geometry safeguard into the trust-region subproblem as a constraint (the wedge), and keep rejected points that improve the model. | [S040 pp. 3, 5–7] | M2, M3 |
| D13 | Gate expensive local devices on a size-independent KKT error | Switch on second-order corrections or cross-term estimates only when a scale-free KKT error is small. | [S067 pp. 7, 9, 13, 15; S077 p. 6] | H6 |
| D14 | Reverse communication | Return control to the user for every evaluation so that the code fits user loops and remote services. | [S005 pp. 3–4; S119 pp. 3, 7; S098 pp. 5–6; S063 pp. 3, 43] | H7 |
| D15 | Change only the oracle and one acceptance test | Turn an existing derivative-based code into a noisy or derivative-free one by replacing the derivative oracle and relaxing one Armijo or ratio test; nothing else changes. | [S080 arXiv pp. 13, 26; S150 p. 3; S082 pp. 4–5; S124 p. 33] | M3 |
| D16 | Relax a ratio test by the same noise term in both terms | Add ξ(ε_f + ν ε_c) to both actual and predicted reduction, with ξ chosen so that accepted steps keep a decrease up to the noise. | [S124 pp. 4–5, 10] | M3 step 3 |
| D17 | Lengthen the curvature pair | When the step is shorter than a noise-determined length l, compute the pair over length l at the cost of one extra gradient; keep the update formula and the acceptance test. The practical algorithm adds a split-phase line search. | [S072 pp. 4–5; S071 pp. 1–6] | M3 step 3 |
| D18 | Audit the fragile operations first | Before redesigning for noise, list the few operations that noise can break (differences, line-search tests, ratio tests) and repair only those. | [S128 p. 1] | M3 step 1 |
| D19 | One repair for two settings | Treat two settings with one underlying defect (fault-tolerant distributed L-BFGS and multi-batch learning: inconsistent samples) with one fix. | [S033 pp. 2–3] | M7 |
| D20 | Cautious updating for nonconvex BFGS | Skip the update when yᵀs is small relative to ‖s‖² (Li–Fukushima style), adopted after citing the BFGS failure examples of Dai and Mascarenhas. The paper's setting: skip when yᵀs ≤ ε‖s‖² with ε = 10⁻² [S031 p. 5]. | [S033 p. 6; S031 p. 5] | M7 step 2, M5 (C1) |

## 3. Experiment and evaluation protocols

| # | Protocol | How to use it | Where | Serves |
|---|---|---|---|---|
| E1 | Stopping tests aligned with the rival | Edit your own code's termination so it matches the rival's; count limits as failures and define success identically for all codes. | [S035 report pp. 19–21; S078 pp. 6–7; S008 pp. 20–23; S005 p. 8; S003 p. 18; S013 p. 14; S139 p. 15] | M1 step 4 |
| E2 | Same-solution filter | Drop problems where codes reach different local solutions and report how many were dropped per code. | [S002 p. 8; S012 p. 24; S029 p. 7] | M1 step 5 |
| E3 | Stratify outcomes before profiling | Split runs by outcome type (solved, wrong solution, failure) before drawing performance or data profiles. | [S080 arXiv pp. 28–29] | M1 step 7 |
| E4 | CPU time only where set-up cost does not dominate | Report evaluations for every problem and CPU time only above a size threshold. | [S013 p. 14; S003 p. 23; S139 p. 18] | M1 step 7 |
| E5 | Failure taxonomy by name and cause | Classify each failure of the incumbent heuristic (for barrier rules: by name and cause), not just count failures. | [S029 pp. 16–17] | M4 step 3 |
| E6 | Termination cross-table over the full set | Show a new feature is harmless by tabulating old against new termination outcomes on all problems. | [S053 pp. 13–14] | M4 |
| E7 | log₂ ratio plots for two-solver comparisons | Plot log₂ of the cost ratio per problem, sorted, instead of a profile when only two solvers are compared. | [S053 p. 13; S080 arXiv p. 9; S150 p. 7] | M1 |
| E8 | A rival-neutral target | Fix the accuracy target from a derivative-based reference solve (a fraction of the decrease it attains), not from either competitor. | [S040 pp. 12–13; S062 pp. 4–5] | M1 step 4 |
| E9 | Controlled inner-solver tests | Freeze one Hessian and solve 51 systems with random right-hand sides: the first with plain CG, which builds the preconditioner, and the other 50 preconditioned; vary condition number and eigenvalue distribution one at a time in a synthetic family. | [S030 p. 7; S088 pp. 9–11] | H1 |
| E10 | Infeasible instances from feasible ones | Add one constraint or bound to a feasible test problem to make an infeasible one with known structure. | [S052 pp. 18–19; S073 p. 23] | M4, Workflow C |
| E11 | A cost axis that charges every sample | Count accessed data points or effective gradient evaluations, so methods with different inner loops share one axis; sweep an equal work budget over a log grid. | [S023 p. 16; S018 p. 19; S015 p. 15; S041 p. 8] | M7 step 4 |
| E12 | Noise-free, then noisy, then ablation | Run the method noise-free first, then with noise using the rival community's own profile machinery, then ablate the new safeguard; inject identical noise in both arms. | [S038 pp. 3–5, 19–22; S082 p. 21] | H3 |
| E13 | Misspecification sweep of an estimate | Run the method with its estimate 1/10 to 10 times, or 10× to 1000× too large and too small, and write the direction of failure for each. | [S071 p. 20; S084 p. 19; S091 arXiv p. 12; S128 pp. 9–11] | H12 |
| E14 | Validate an estimate against the truth | Tabulate the in-algorithm estimate against the true quantity over a real run (sample variance against the true gradient error; model gradients against exact AMPL gradients). | [S018 p. 20; S062 p. 8; S015 pp. 20–21] | H12 |
| E15 | Oracle arm | Run the method with the true value of the estimated quantity, labelled for benchmarking only, to locate the estimator's share of the gap. (Shared with Curtis.) | [S091 arXiv pp. 17–18; S080 arXiv pp. 13, 23–24] | M3 step 5 |
| E16 | Zero-noise collapse check | Verify that the repaired method reduces exactly to the classical one when the estimate is zero. (Shared with Fletcher and Gill.) | [S071 pp. 13, 25; S082 pp. 11, 23; S084 p. 15; S124 pp. 28–29] | M3 step 5 |
| E17 | Degenerate-parameter ablation; predecessor as control | Run the setting that removes the new ingredient (M = 0, scaling only) to attribute the gain; run an extended code on its predecessor's problem class against the predecessor to isolate regressions in shared parts. | [S015 pp. 20, 23; S003 p. 19; S067 pp. 15–18] | M3 step 5, M7 step 5 |
| E18 | The rival at non-default settings | Rerun the rival at its non-default settings in an appendix, beside the default comparison. | [S080 arXiv pp. 42–44] | M1 step 3 |
| E19 | The same tuning rule for every method | Tune every method's step parameter by one rule (keep the value where one increment up or down is worse) on a fixed schedule. | [S015 p. 14] | M1, M7 |
| E20 | Deterministic limit first | Test a stochastic idea with the full sample first and report it if it loses there. | [S023 p. 12] | M7 step 5 |

## 4. Writing moves

| # | Move | How to use it | Where | Serves |
|---|---|---|---|---|
| W1 | Numbered open questions; a four-way classification of results | End a survey with numbered open questions; sort results into global convergence, local convergence, rate and global efficiency. | [S019 pp. 2, 17, 21–22] | M5 step 5 |
| W2 | Limitations before results | Put the limitations section before any result, and numbered drawbacks next to numbered advantages. | [S080 arXiv p. 7; S005 p. 3] | M1 step 6 |
| W3 | A two-sided verdict tied to problem features | Say for which problem features the method wins and for which it loses. | [S003 p. 23; S023 p. 18] | M6 |
| W4 | Surprise recorded as surprise; conjectures labelled | Write "to our surprise" where it was one; label conjectures as conjectures. | [S062 pp. 2, 5–7, 9; S029 p. 21; S041 pp. 7–8; S057 p. 18; S042 p. 5] | Workflow D |
| W5 | Open with the mislabelled failure | Start a section with a result first counted as a failure that a closer look reversed: "Initially we reported this as a failure of the limited memory code to achieve high accuracy in the solution, but a closer examination of the results revealed that in some of these runs the limited memory code had actually produced a lower function value than LANCELOT." | [S057 p. 2] | M1 |
| W6 | State what the paper must argue | Write in one sentence what the rest of the paper must show, including the cost measure, so readers can check each experiment against it. | [S015 p. 7] | M7 |
| W7 | Separate concurrent work and label summaries | A dated paragraph separating concurrent work; a comparison table labelled as a summary, not a ranking; a ranking disclaimer next to the results. | [S032 arXiv pp. 3, 20–21; S003 p. 23; S078 p. 2] | M1, Workflow D |
| W8 | A counterfactual about the field | Say what the field would have done had the missing comparison been made: "We believe that if such comparisons had been made, particularly in the noiseless setting, research in the field would have followed a different path." | [S080 arXiv p. 4] | M2 |
| W9 | Numbered application features | Open an application paper with a numbered list of the features that constrain the algorithm, then refer back to it at each choice. | [S047 pp. 5–6] | M6 step 1 |
| W10 | A grant report that doubles as an agenda | Pair each result with the open question it raises and next year's deliverable. | [S197 pp. 3–5; S193 pp. 3–4] | M4 |

# Technique catalog: transferable moves from Burer's papers

> Date: 2026-10-10. Built from the full-text paper cards (`research/cards/`, index `research/07-paper-cards.md`) and the technique inventory of `research/08-deep-reading-synthesis.md` §7. Every row names the card and the page of the PDF that was read (the version named on the card). Eighteen cards were read from a substitute version and carry the version word: `preprint` for S012, S014, S016, S024, S051; `arXiv` for S019, S023, S027, S038, S039, S044, S045, S048, S049, S050, S055, S056, S057; their published versions were not read. S058 and S065 are arXiv-only works, cited plainly. Card ids resolve in `research/07-paper-cards.md` and in the card key of `research/09-evidence-ledger.md#card-key`.
>
> **How to use this file.** Find the row for the job you have (a hull or exactness proof, a relaxation to design, an experiment to run, a section to write), read the one-line "how to use it", then open the cited paper at the cited page before relying on it. The one-liners are summaries, not theorem statements: never copy a condition or a constant from here into a paper. Ids P, D, E, W are the ones SKILL.md uses in its workflows; §5 lists his known exactness results with their hypotheses.
>
> **Scope.** Techniques only. Reading notes that the cards record about typos or small inconsistencies inside papers are left out; the one neutral lesson kept is in §4.

## 1. Proof devices

| # | Device | How to use it | Where |
|---|---|---|---|
| P1 | Pataki rank bound + rank-one perturbation of an extreme point or ray (the hull-proof engine) | To show a relaxation equals the hull, show every extreme ray has rank one: bound the rank of extreme points by Pataki's count, then, for a ray of rank ≥ 2, find a direction W − εvvᵀ (v in Range W) that stays feasible both ways, contradicting extremality; split into interior and boundary cases. | [S001 p. 5; S012 preprint pp. 5, 7; S016 preprint pp. 11-12; S021 pp. 6-10; S024 preprint pp. 13-14, 19-21; S036 pp. 4, 12; S049 arXiv pp. 20-24; S058 pp. 9-12; S065 p. 10] |
| P1a | Half-space lemma for extreme rays | An extreme ray of a cone cut by one half-space is extreme in the cone or a sum of two extreme rays; use it to add one linear constraint at a time to a hull proof (the 2015 survey lemma, reused in 2025). | [S024 preprint pp. 19-21; S049 arXiv p. 22] |
| P2 | Completely positive decomposition, Cauchy–Schwarz equality case; DNN = CP in small dimension | Write the lifted matrix as a sum of nonnegative rank-one terms and use the equality case of Cauchy–Schwarz to force each term onto the feasible set; for n ≤ 4, DNN = CP lets a tractable cone carry the proof. | [S004 p. 5; S009 pp. 4-5; S010 pp. 5-7; S016 preprint p. 9; S024 preprint p. 7; S038 arXiv p. 4; S058 p. 11; S067 p. 5] |
| P3 | Recession-cone arguments for boundedness and exactness | Show that the recession directions of the lifted set are exactly the lifted recession directions of the original set (or are zero), so the relaxation is bounded and the closure statement holds. | [S004 p. 7; S007 p. 10; S008 p. 10; S016 preprint p. 10; S009 p. 4] |
| P4 | Perturb (or tighten), prove, pass to the limit | Prove the statement for a perturbed or strictly feasible problem where the argument works, then let the perturbation go to zero; standard, but it carries several of his exactness results. | [S009 p. 4; S019 arXiv pp. 9-17; S021 p. 11; S023 arXiv p. 16; S041 pp. 16-20] |
| P5 | Dual certificate from stationarity multipliers | At a stationary point of a factored (nonconvex) formulation, build S from the multipliers; S ⪰ 0 certifies SDP optimality; with a trace bound, a λ_min shift gives a valid lower bound even when S ⋡ 0 (Method 6). | [S014 preprint p. 8; S017 p. 19; S001 p. 7; S003 pp. 13-14; S023 arXiv pp. 26-29; S048 arXiv pp. 17-20]; for a DNN/SDP+RLT bound solved inexactly by splitting, a dual-feasible multiplier gives a valid lower bound at every outer iteration, and a baseline without valid bounds gets a rigorous-bound post-processor [S020 pp. 4, 9-10, 15] |
| P6 | Explicit small counterexample at the boundary dimension | Publish the first dimension where a claim fails with an explicit instance (K3, a pentagon, n = 3 box, n = 4 submodular), certified when possible by exact means. Two recipes: (a) not-the-hull: an inequality whose validity an exact finite (recursive) procedure checks, plus a rational point of the candidate relaxation that violates it, checkable by hand [S011 pp. 15-16]; (b) a gap at small n: a rational feasible point plus exact enumeration of all 3ⁿ KKT active-set patterns over the rationals [S058 pp. 13-14, 43]. Decimals plus stationary-point enumeration and a second solver are weaker; say which you have [S065 p. 16]. | [S006 p. 7; S025 p. 13; S010 p. 8; S011 p. 16; S012 preprint p. 13; S034 p. 6; S036 pp. 8-10; S048 arXiv pp. 39-41; S058 pp. 13-14, 43; S065 p. 16] |
| P7 | A redundant bound or ball for Slater points or compactness | Add a provably redundant norm ball or bound so that strong conic duality holds or the feasible set is compact; then dualize. | [S019 arXiv p. 13; S023 arXiv pp. 7-8; S044 arXiv p. 12; S048 arXiv pp. 21-22; S030 p. 5] |
| P8 | Schur complements and principal minors to force entries or rank | Use 2 × 2 or bordered principal minors of a PSD lifted matrix to force entries to zero or the rank to one at the points that matter. | [S018 pp. 9-10; S012 preprint p. 6; S021 pp. 9-10; S019 arXiv p. 7; S038 arXiv pp. 10-18; S040 pp. 8-9; S055 arXiv p. 4] |
| P9 | Convergence by telescoping or by an exact perturbed problem | For an augmented-Lagrangian or inexact interior-point scheme, telescope the merit decrease, or show each inexact step is an exact step of a perturbed problem whose perturbation is tied to the duality gap. | [S013 pp. 10-11; S035 pp. 7, 10-11] |
| P10 | Proof-failure map guides the counterexample | Name the configuration the proof cannot handle (a rank and activity pattern) and search for the counterexample there first. | [S058 pp. 13-14, 43] |
| P11 | Validity separated from sufficiency | State the conditions that make a relaxation valid apart from those that make it exact, so each can be checked and weakened on its own. | [S027 arXiv p. 4] |

## 2. Design moves

| # | Move | How to use it | Where |
|---|---|---|---|
| D1 | Change of variables that removes a cone | Replace X ⪰ 0 by a factor (X = RRᵀ, X = LLᵀ, a Cholesky elimination) sized by a rank theorem, so a first-order method works on an unconstrained or simply constrained problem (Method 6, step 1). | [S014 preprint pp. 5-8; S017 pp. 6-9; S001 pp. 3, 5; S030 pp. 6-7] |
| D2 | Split by copy variables | Introduce copies so that the cone and the coupling constraints sit in separate blocks, then use an augmented Lagrangian with block coordinate descent and a projection; a null-space parametrization of the DNN set does the same for CP relaxations. | [S013 pp. 4-5, 12; S020 pp. 4, 6-10] |
| D3 | Sandwich an auxiliary scalar | Insert one artificial scalar between a shared nonlinear term and several linear bounds (x'x ≤ β ≤ …) so many cone constraints become one cone plus linear constraints; RLT and SOC-RLT then apply. A one-coordinate lift turns a ball into a sphere. | [S049 arXiv pp. 3, 11-12, 18-19; S022 p. 2] |
| D4 | SOC-RLT | Multiply a valid SOC constraint by a nonnegative linear slack and linearize in (x, X). | [S016 preprint pp. 5-6; S021 p. 6; S067 p. 4] |
| D5 | Lift each column separately; Kronecker products of redundant LMIs | For matrix variables, lift each column and couple through the sum; or multiply a redundant LMI by itself and linearize. | [S048 arXiv pp. 3, 39; S055 arXiv pp. 5-6] |
| D6 | Separation oracle in place of an explicit description | When the exact description is too large (or unknown), separate by solving a small optimization problem (a TRS, a boundary cone) and add cuts. | [S012 preprint p. 15; S040 pp. 9-14; S065 pp. 4-8] |
| D7 | Redundant in x, binding in the lift (SKILL M1 step 1) | Add squared linear equations, complementarities, binarity xⱼ = Xⱼⱼ or KKT products before relaxing; they cost nothing in x and often carry exactness in the lift. | [S004 pp. 4-5, 14; S009 pp. 8-9; S022 pp. 2-3; S007 p. 9; S008 pp. 8-9; S049 arXiv pp. 13-14] |
| D8 | Optimality conditions in the relaxation, finite branching (SKILL M1 dated variant, 2008–2012) | Write the KKT system, branch on complementarity index sets, make the node relaxation an SDP/DNN of the lifted KKT system and bound the multipliers by LPs. | [S007 pp. 3, 9-12; S018 pp. 7-10; S008 pp. 4, 8-10; S059 pp. 5-7, 12] |
| D9 | Collapse a cut family into one constraint | Solve for the parameter that indexes an infinite family of cuts (a segment weight) to get one nonlinear (SOC) constraint equivalent to the whole family. | [S039 arXiv pp. 3, 6] |
| D10 | Show the incumbent method is a named restriction | Prove that the method everyone uses (the affine policy) equals an inner approximation of your exact conic program, so every richer approximation is certified no worse. | [S023 arXiv pp. 11-12] |
| D11 | Embed a known polytope as a face | Show the constrained hull is a face of a simpler set (BQP inside the box-QP or MIQP set) to transfer its facets. | [S011 pp. 7, 11-13; S037 pp. 11, 17] |

## 3. Experiment and evaluation protocols

| # | Protocol | How to use it | Where |
|---|---|---|---|
| E1 | Same accuracy target or the same bound for every method | Time every method to the same accuracy or the same bound value; use surpass-time columns, time-matched truncation, or equal time caps when nothing finishes. | [S014 preprint p. 14; S020 p. 12; S013 p. 18; S001 p. 26; S031 p. 14] |
| E2 | Favour the baseline | When the claim is a trend, a valid bound or a speed-up, give the competitor its best setting (exact moments, derived big-M bounds, tuned starting duals, same-language re-implementation) and say so. | [S044 arXiv p. 14; S059 pp. 19, 21-22; S013 p. 17; S031 p. 8] |
| E3 | Swap one component, freeze the rest; factorial ablations | Compare node solvers inside the same tree, or run 2 × 2 ablations reported as ratios. | [S020 p. 16; S043 pp. 15-16; S045 arXiv pp. 23-24] |
| E4 | Report by joint outcome | Tabulate by joint solve status (both / only new / only old / neither), or certified / not tight / local, so never-worse comparisons read off the table; cross-evaluate solutions on each other's objectives. | [S049 arXiv p. 17; S048 arXiv p. 13; S062 pp. 6-8] |
| E5 | Cross-verify "solved" | Primal-dual difference columns; independent algorithms agreeing to a stated number of significant figures. | [S001 pp. 14, 17; S059 p. 15] |
| E6 | Accuracy at two levels | Report at two accuracy levels to show where a first-order method stops paying. | [S014 preprint pp. 15-17] |
| E7 | Instances generated from real data without using the data | Use real data only to set the generator's parameters; test on generated instances. | [S062 p. 6] |
| E8 | Hard pool with disclosed filter (Method 4) | Literature failure instances first; a generator from a theorem about where the baseline fails; keep only instances the baseline does not solve; log seeds; reuse the unsolved set as the next rung. | [S012 preprint pp. 16-19; S018 pp. 11-14; S020 p. 12; S024 preprint p. 28; S033 p. 19; S049 arXiv pp. 15-16, 20; S065 pp. 8, 12, 15-16] |
| E9 | Explain wins and losses by one instance statistic | Tabulate a structural statistic (fill-in, density) beside the results to show which instances favour which method. | [S032 pp. 14-15] |
| E10 | Read a gap-free random panel as rarity evidence | Judge tightness with a valid dual bound against the global optimum, and write a clean panel as evidence that violations are rare, not as a theorem. | [S058 p. 27] |
| E11 | Seeds for tuning disjoint from seeds for evaluation | Tune hyperparameters of all methods on separate seeds; split performance profiles by each size parameter and show several time budgets. | [S056 arXiv pp. 10-14] |

## 4. Writing moves

| # | Move | How to use it | Where |
|---|---|---|---|
| W1 | Numbered goals or conclusions up front, negative ones included | List what the paper sets out to do, including what it will show cannot be done. | [S014 preprint p. 3; S020 p. 5; S026 pp. 3-4; S007 p. 4; S049 arXiv p. 2] |
| W2 | Announce the negative result next to the positive one | Put the negative finding in the introduction (and, once, in the title). | [S047 p. 2; S010 p. 3; S041 p. 23; S063 p. 15; S043 p. 2] |
| W3 | Grade every claim by its level | Theorem, conjecture, "we believe", empirically, very likely; say which. | [S038 arXiv p. 3; S020 pp. 13-14; S039 arXiv pp. 4, 14; S050 arXiv pp. 25-26; S055 arXiv p. 7; S065 pp. 10, 14, 16] |
| W4 | Easiest to hardest, simple case first, picture first | Order results by difficulty; show a 2-D picture or envelope plot before the tables. | [S017 p. 6; S024 preprint p. 3; S043 pp. 4-6; S039 arXiv pp. 7-25; S067 p. 3; S049 arXiv pp. 3, 13-14] |
| W5 | Warn about notation | Say when notation is heavy or overloaded. | [S017 p. 3; S008 p. 6; S024 preprint p. 3; S049 arXiv p. 5] |
| W6 | Scope disclaimer | Say what is not claimed (mechanisms, optimality, a "silver bullet"). | [S015 p. 3; S031 p. 14; S045 arXiv p. 4] |
| W7 | Credit finders and contributors by name | In acknowledgements, corrections and theorems. | [S004 p. 17; S019 arXiv pp. 17-18; S061 p. 1; S048 arXiv p. 15; S058 p. 46; S049 arXiv p. 24; S042 p. 13] |
| W8 | End with open questions | Hand on the open cases as numbered questions or conjectures. | [S004 pp. 16-17; S011 p. 16; S029 p. 33; S037 pp. 24-25; S049 arXiv p. 24; S067 p. 6] |
| W9 | Disclose concurrent equivalent work by date | Name the same-day equivalent result and list the differences. | [S023 arXiv pp. 4-5] |
| W10 | Open with a complexity table and fill the empty cell | Place the result in a domain-by-function-class table and fix the scope in a footnote. | [S058 p. 3] |
| — | Neutral lesson from the reading notes (not about any one work) | In long computational papers, recheck that captions, totals and text agree after each revision. | 08 §7.4 |

## 5. Known exactness results

His own record (and two results he restates), substructure by substructure. Use it before searching (SKILL Step 2, Stuck triage check 2): it says under which hypothesis each relaxation is exact and how the first failure was shown. "Numerical" means solver output, not a certificate. Summaries, not theorem statements: read the cited page before relying on a hypothesis.

| Substructure | Relaxation | Exact under | First failure (how shown) | Where |
|---|---|---|---|---|
| Nonconvex QP over the box [0, 1]ⁿ | Shor (psd) + RLT | n ≤ 2 | n = 3: explicit instance Q = (1/3)eeᵀ − I, true value −2/3 against relaxation value −3/4 (rational data) | [S010 pp. 7-8; S011 p. 4] |
| Box QP, n = 3 | psd + yᵢᵢ ≤ xᵢ + BQP₃ (RLT and triangle inequalities) | not exact | an inequality checked valid by an exact recursive procedure, violated by the rational point x = (1/3)(1, 1, 1) with value 19/18 > 1 | [S011 pp. 15-16] |
| QP over a simplex | DNN (DNN = CP in small dimension) | n ≤ 4 | n > 4: known counterexample from the CP literature | [S010 p. 5] |
| QP over a polytope of dimension ≤ 3 | disjunctive DNN over a triangulation | n ≤ 3, triangulated | needs extra variables; a direct description for the 3-cube is open | [S010 pp. 9-12] |
| Mixed-binary QP | linear program over the CP cone | the "key assumption" (linear constraints imply 0 ≤ xⱼ ≤ 1 for binaries) | exact, but the cone is intractable; approximations not tested | [S004 pp. 3-6, 15-16] |
| Trust-region subproblem + two parallel cuts (TRS2p) | Shor + 1 RLT + 2 SOC-RLT | exact (polynomial-time) | two intersecting cuts: gap about 7% at n = 3 (numerical: Couenne value, numerical rank 3) | [S012 preprint pp. 8, 12-13] |
| TRS + m linear cuts | Shor + RLT + SOC-RLT | any m, cuts non-intersecting inside the ball (Assumption 1) | intersecting cuts, as above | [S021 pp. 3, 10] |
| Switching variables 0 ≤ x ≤ y, y binary | psd + RLT | n = 1; n = 2 with an extra 5 × 5 PSD condition (still lifted) | plain psd + RLT for the hull without y₁y₂ at n = 2: conjectured, supported numerically, unproved | [S038 arXiv pp. 4-6, 18-20] |
| Nonconvex QP over m balls | slight lift to dimension n + 1 | m = 2 balls | m ≥ 3: numerical only (solve counts, gap-closure tables), no exact counterexample; balls only, general ellipsoids not covered by the theorem | [S049 arXiv pp. 1-3, 16-17, 20-24] |
| QP over two general ellipsoids (TTRS) | slight-lift variant | no exactness theorem | empirical: all 212 hard instances of the 2013 set solved | [S049 arXiv pp. 3-4, 20] |
| Submodular quadratic over the box | SDP with the slack RLT lower bounds dropped | n ≤ 3 (completely positive certificate) | n = 4: rational feasible point plus exact enumeration of the 81 KKT patterns; the gap survives full RLT + triangle inequalities | [S058 pp. 9-14, 43-44] |
| Bilinear objective over two ellipsoids | linear program over the SEP cone (Lorentz positive cone) | exact | SEP + Shor for TTRS: not exact, n = 2 counterexample, 15.74% relative gap (rational data, decimals; stationary-point enumeration and Gurobi) | [S065 pp. 6-7, 16] |

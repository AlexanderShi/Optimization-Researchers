# Santanu S. Dey · Technique catalog

> Date: 2026-10-10 (stage T3.6). Transferable techniques found in the paper cards, grouped as proof devices, design moves, experiment and evaluation protocols, and writing moves. Each entry has a one-line **How to use** and the cards with pages (`[S014 pp. 7–8]` = card S014 in `research/07-paper-cards.md`, page of the version named on the card). Source: `research/08-deep-reading-synthesis.md` §7 (technique inventory) and the "Transferable" lines of the cards in `research/cards/`. The skill's methods are in `../SKILL.md`; the full evidence per method is in `research/09-evidence-ledger.md`. All papers are co-authored; a technique listed here is one his papers use, not necessarily his alone.
>
> Where SKILL.md uses them (ids in brackets after a step): Method 1 steps 3, 8 (P18, D3, D4); Method 2 steps 1, 3, 4 and the spatial-B&B variant (E1–E3, E5, E7, E16, E18); Method 3 steps 4, 5 (P1, P2, P8, P13, P14, D2); Method 4 steps 1–3 (P8, P9, W2, W3); Method 5 variant and steps 2–4 (P3, E4, D5, D9, D11, D12, E9); Method 6 steps 4–6 (D14, D15, E11); Workflow E (W1–W14).

## 1. Proof devices

| # | Technique | How to use | Cards |
|---|---|---|---|
| P1 | Disjunctive extended formulation of a union, then Fourier–Motzkin (or approximate) projection | Write the hull of a union of simple pieces with weights, prove the extended form exact, project to the original space to get explicit inequalities and a separation routine | [S002 pp. 8–9; S004 pp. 6, 8–11; S009 pp. 11–14; S091 pp. 5–7; S051 pp. 23–28; S085 p. 6; S111 pp. 8–9; S092 p. 8; S062 pp. 9–10] |
| P2 | Extreme-point support bound | Perturb an extreme point along a direction that keeps the active constraints tight; if it stays feasible it is not extreme, so extreme points have one or two fractional entries or a 2×2 support; then convexify each small piece and take the union | [S041 pp. 6–7; S051 pp. 4–7; S032 pp. 4–10; S129 p. 5; S085 p. 4; S070 pp. 21, 24] |
| P3 | PSD completion of the cheap optimum | To prove an SDP adds nothing over a cheap relaxation, complete the cheap optimal point to a PSD matrix (rank one plus a sparse or diagonal correction) | [S105 pp. 5–7; S129 p. 5; S001 pp. 11–12] |
| P4 | Scaling sandwich (α-approximation) | Compare two closures or relaxations by the smallest α with U ⊆ αV (packing/covering); bound the gain of all cuts from a family by each relaxation's own gap | [S079 p. 7; S011 pp. 18–19; S039 p. 8; S107 pp. 4–7; S099 pp. 4–7; S085 p. 7; S017 pp. 11–14; S083 p. 4] |
| P5 | Randomised sparsification of a dense normal | Round a dense separating normal coordinate-wise with probabilities proportional to its entries, keep it unbiased, and use Bernstein/Chernoff plus a union bound over the vertices to show it stays valid and separating | [S084 pp. 6–8; S028 pp. 7–9; S011 pp. 12–13; S035 pp. 11–13; S057 pp. 10–11; S088 pp. 5–9; S125 pp. 12–16; D005 pp. 8–13] |
| P6 | Averaging and midpoint arguments | Average the restricted versions of an inequality over all k-subsets, or average mirror-image solutions, to get a valid weaker inequality or a point in a closure | [S100 pp. 8–9; S034 p. 14; S028 pp. 9–10; S035 p. 8; S153 pp. 12–13; S046 p. 20] |
| P7 | Tree-size counting for branch and bound | Best bound never branches below OPT; charge every node to a good point or a gadget; count near-optimal solutions; for random columns, bound slabs | [S031 pp. 4–10; D003 pp. 4–13; S120 pp. 6–20; S020 pp. 14–15; S034 pp. 7–11; S081 pp. 7–8] |
| P8 | One small counterexample per dropped hypothesis | For every strengthening a reader might expect, give a small explicit instance (or gadget) where it fails, and put it next to the theorem | [S003 pp. 2–3; S019 pp. 11–14; S071 pp. 17–24; S073 p. 8; S097 p. 9; S103 pp. 22–27; S112 pp. 4–5; S119 pp. 9–15; S122 pp. 6–7; S124 pp. 11–13; S125 pp. 14, 17; S080 pp. 9–10] |
| P9 | Hardness by reduction | Reduce subset sum, vertex cover, max-cut, partition, edge colouring or stable set; check the reduction preserves objective values to get inapproximability, not only NP-hardness | [S010 p. 5; S022 pp. 4–6; S003 p. 2; S009 pp. 8–9; S014 pp. 12–13; S007 pp. 7–12; S062 pp. 4–5; S129 p. 3; S040 p. 9; S067 pp. 16–18] |
| P10 | Dirichlet / Kronecker approximation and unimodular normalisation | Handle irrational or lower-dimensional data by approximating directions with rational ones or normalising by a unimodular map before the integer argument | [D001 pp. 3–6; S025 pp. 4–7; S042 pp. 6–11; S043 p. 14; S116 pp. 3–5; S018 p. 4; S033 pp. 11, 13] |
| P11 | Geoffrion's primal characterisation of the Lagrangian dual | Read the Lagrangian bound as optimisation over the convex hull of the dualised-away part, then ask when that hull is exact | [S097 p. 5; S104 pp. 5, 17–18; S112 pp. 1, 5; S125 pp. 8–9] |
| P12 | Tree-decomposition induction | Peel leaves or consolidate bags of a tree decomposition to prove exactness of an LP or a decomposable dual | [S097 pp. 20–21; S104 pp. 20–22; S092 pp. 22–26; S153 pp. 13–15] |
| P13 | Spectral tools | Cauchy interlacing, S-lemma variants and Schur complements to count negative eigenvalues of aggregations or certify PSD-ness | [S035 p. 10; S055 p. 9; S071 pp. 10–14; S077 pp. 23–26; S119 pp. 5–6; S129 pp. 9–10] |
| P14 | SDP duality plus rank reduction for S-lemma variants | Make the primal SDP unbounded, then get a rank-one point by Barvinok (bounded case, from a positive-definite combination) or Pataki, chosen by a dimension case split | [S071 pp. 10–11] |
| P15 | Facet proofs by affinely independent point families | Exhibit enough affinely independent points on the face, or use the Facet Theorem with equality sets | [S009 pp. 15–16; S026 p. 12; S046 p. 12; S016 pp. 15–18; S045 pp. 9–10] |
| P16 | Finite-check reductions and compactness | Reduce an infinite family (all columns, all splits) to finitely many checks by compactness or a finite subcover, then check them | [S026 pp. 6–11; S053 pp. 5, 7; S013 p. 14; S025 pp. 14–15; S042 pp. 8–10; S018 p. 7] |
| P17 | Computer-checked steps inside a proof | Use exact arithmetic or computer algebra for a finite residue of the proof, and say so | [S018 p. 7; S055 p. 7; S071 pp. 17–24; S078 pp. 10, 12–13] |
| P18 | Relax the relaxation | Drop the variables that encode the coupling, solve the weaker LP, and recover a feasible point of the true problem with a loss factor; the factor bounds every refinement at once | [S014 pp. 7–8] |
| P19 | n-fold coupling of a gadget | Take n copies of a constant-size counterexample and couple them through one auxiliary variable in a redundant constraint, so one cut acts as n cuts; bound one tree by recursion and the other by counting complete gadgets | [S081 pp. 6–8] |
| P20 | Small-witness decomposition | Split a mixed-integer region into polytope-plus-integer-cone pieces, refine cones until zero-curvature directions are extreme rays, then argue one ray at a time | [S003 pp. 3–9] |

## 2. Design moves

| # | Technique | How to use | Cards |
|---|---|---|---|
| D1 | Find the substructure that carries all the nonconvexity | Lift, then look for the single condition (rank one, cycle angle sum, per-line coupling) that holds all the nonconvexity, and convexify that set jointly | [S051 pp. 1–2; S008 pp. 5–18; S001 pp. 15–24; S006 pp. 6, 18–20; S032 p. 2] |
| D2 | Exact hull for the theorem, few inequalities for the code | Prove the exact hull, then implement a small outer approximation (a few edge cuts, a polyhedral SOCP approximation) and say the light version has no guarantee | [S008 pp. 10–14; S041 pp. 3–5, 17–18; S105 p. 2] |
| D3 | A relaxation of the relaxation that one rounding argument bounds | Define the whole family of refinements abstractly so one theorem covers every scheme | [S014 pp. 4, 7] |
| D4 | Proof to heuristic to MILP restriction | Read the feasible point built in a bound proof as an algorithm, then enlarge it to an MILP restriction that contains all its outputs and so inherits the guarantee | [S014 pp. 6, 12, 14–16] |
| D5 | One construction, both bounds | Discretise one auxiliary (ratio) variable; the same binary expansion gives an MILP relaxation and an MILP restriction | [S051 pp. 10–11; D002 pp. 22–25; S080 pp. 18–19] |
| D6 | Cheap LP ranking predicts the MILP winner | Rank the LP relaxations first and use the ranking to pick the MILP discretisation | [S051 p. 20] |
| D7 | Reduce separation to another field's problem | Write cut separation as sparse PCA or a SAT repair step and use that field's heuristic as oracle | [S048 pp. 6–7, 15; S105 p. 9; S061 p. 4] |
| D8 | Keep the classical algorithm; change only the failing step | Replace one step (randomisation, branching score) and keep a conservative fallback | [S061 p. 12; S130 pp. 4–8] |
| D9 | Constraints redundant for the primal, useful for the dual | Add products or copies that change nothing in the primal but make the dual separable or tighter; first prove which classes cannot help | [S104 pp. 3–5; S117 pp. 2, 13; S111 p. 16] |
| D10 | Ordered or nested reformulation of assignment binaries | Reformulate to a totally unimodular block | [S124 pp. 7–11] |
| D11 | Separate over small cones, not the full SDP | Add linear cuts from the SDP cone of each cycle of a cycle basis to a cheap base relaxation | [S001 pp. 23–24] |
| D12 | Triangulate a long polynomial constraint | When degree grows with structure size, add artificial variables to split it into 3- and 4-term bilinear pieces, then apply McCormick | [S001 pp. 16–20] |
| D13 | Binary search a continuous branching parameter | Use monotonicity of child bounds in the branching point, and record bound reductions found on the way | [S123 pp. 3–4] |
| D14 | Prove what carries over, then reuse it | For re-solved models, prove a stability or finiteness result over the instance family, then reuse the covered object (dual solution, split directions, past solutions) | [S044 p. 18; S082 pp. 6, 16–17; D004 arXiv pp. 4–5, 9–12] |
| D15 | Choose the dual inside the ε-optimal face | When dual solutions are not unique and feed a downstream use, optimise a secondary objective tied to that use over the ε-optimal face | [D004 arXiv pp. 9–12; S067 pp. 9–12] |

## 3. Experiment and evaluation protocols

| # | Technique | How to use | Cards |
|---|---|---|---|
| E1 | Stripped textbook B&B | Implement a naive B&B where the expensive rule is an oracle, with presolve, cuts and heuristics off, so node counts compare only the studied decision | [S130 pp. 3–4; S081 pp. 8–11; S098 p. 5; S041 pp. 19–21; S123 pp. 5–6; S103 pp. 6–9] |
| E2 | Exact ceiling first | DP-optimal trees over the 3^n faces (≤ 20 binaries), enumeration, all facets, exponential LPs, a global solver at small n, or a planted optimum, before any heuristic | [S020 pp. 11–13, 21–22; S048 pp. 9–12; S122 pp. 9, 14–15; D002 p. 21; S129 pp. 19–21; S060 pp. 13–18] |
| E3 | Control the incumbent | Supply the optimal or best-known primal value, or report at fixed primal gaps, so a dual-side rule is not credited for primal luck | [S098 p. 5; S123 p. 5; S082 pp. 7–8; S130 pp. 5, 23, 25] |
| E4 | Two protocols by what theory says | Same bound, compare time when bounds are proved equal; same time, compare bound otherwise | [S100 p. 11; S105 pp. 10, 13] |
| E5 | Instance ladder | Structured random families for design and tuning, then a filtered public benchmark with stated exclusions and seeds | [S130 pp. 4, 23; S081 pp. 8–11; S052 pp. 9–15, 23–24] |
| E6 | Two instruments for one question | A fully controlled synthetic study (any effect is the phenomenon), then a stripped solver on a benchmark (the effect matters in practice), naming what the second cannot control | [S081 pp. 8–11] |
| E7 | Feature-isolating synthetic families | Generate instances that vary one difficulty driver, checked against the default solver before any method | [S052 p. 15; S010 pp. 5–6] |
| E8 | Hard generator | Cut off the root LP solution in the generator so a global solver cannot finish at the root; post the instances | [S014 pp. 22–23, 35; S051 p. 17] |
| E9 | Certified gap at full scale | Report the gap between the relaxation bound and a feasible point, with the time to produce both, named hardware and time limits | [S001 pp. 1, 4, 26–29; S017 pp. 14, 17; S100 p. 11; S051 p. 17; S080 pp. 19, 21–22; S111 pp. 26–27] |
| E10 | Decompose the speed-up | Split a gain into its sources (LP vs MIP evaluations, separation overhead) | [S004 pp. 17–20] |
| E11 | Charge the collection overhead against an expert | Evaluate the expert method first, then add the time to collect what it needs; stop if the gain vanishes | [S082 pp. 9–12] |
| E12 | Drop a solver that returns violated solutions | Check feasibility of every reported solution in code; state what the framework cannot prove | [S059 pp. 18, 24] |
| E13 | Group results by a measured outcome | Band benchmark instances by an outcome you can measure (total gap closed) and report the pattern per band | [S081 pp. 11–12] |
| E14 | Structural statistic next to the ratio | Tabulate one statistic of the optimal object and test your own hypothesis against it | [S020 p. 13] |
| E15 | One-sided bound by random directions | When the exact quantity is not computable even at small size, optimise over many random directions and say the plot is a bound | [S084 p. 17] |
| E16 | Seeds, single thread, node limits | Several seeds, single-thread runs and node limits for comparability | [S061 p. 12; S124 p. 14; S081 pp. 8–11] |
| E17 | Drop instances the baseline already solves | Remove benchmark instances whose gap the baseline closes, and say how many | [S051 p. 17] |
| E18 | Split solved from unsolved instances | Report times for the instances every compared rule solves, and remaining gaps separately for the instances some rule fails on | [S123 p. 7] |

## 4. Writing moves

| # | Technique | How to use | Cards |
|---|---|---|---|
| W1 | Main results before proofs | One overview section with every theorem and its reading, then the proofs | [S014 pp. 5–6; S084 pp. 3–6; S021 pp. 3–4; S020 pp. 4–5; S024 pp. 2–15; S035 pp. 3–7; S065 pp. 1–4; S039 p. 2; S117 pp. 2–4; S120 pp. 3–4] |
| W2 | Two-sided theorem statements | State bound with tightness, algorithm with inapproximability; defend a weak-looking factor at once | [S014 p. 6] |
| W3 | Boundary paragraph right after the main theorem | List the nearest strengthenings and give a counterexample for each | [S003 pp. 2–3; S071 pp. 5–8] |
| W4 | Practical reach as "an indication" | Say what the theorem suggests about practice, not that it explains it | [S031 p. 1; D003 pp. 1, 3; S118 p. 4] |
| W5 | Word of caution and defence of the programme | A paragraph on what the results do not show, then why the line is still worth it | [S011 pp. 20–21; S081 pp. 12–13] |
| W6 | A proof distilled into a selection slogan | Turn a lemma into a one-line rule a practitioner can apply | [S011 pp. 18–19; S122 p. 22] |
| W7 | Surprise flagged against your own expectation | "Surprisingly", "Interestingly", "Contrary to expectation", each tied to a number | [S084 p. 1; S105 p. 4; S129 pp. 3, 5; S081 p. 9; S044 p. 20; S019 p. 2] |
| W8 | Numbered open questions, split theory and practice | End the theory part with numbered questions | [S079 pp. 7–8; S014 pp. 27–28; S039 p. 8; S035 pp. 3–7] |
| W9 | Experiments driven by numbered questions | State the questions the experiments answer, and give possible interpretations after each table | [S048 p. 9; S052 pp. 12–13] |
| W10 | One running or toy example | Thread one small example through the text, or show a numerical example before a structural identity | [S079 p. 4; S153 pp. 5–15; S047 p. 8; S130 pp. 4–7] |
| W11 | Version note | Say what changed from the conference version | [S031 pp. 1–4] |
| W12 | Examples with different behaviour before the theorem | Show two or three tiny instances whose measure behaves differently ("phases"), then state the theorem that explains them | [S084 p. 3] |
| W13 | Agenda review | For each solver knob with no theory, one paragraph: what practice does, what was measured, and the sentence that no theory is known | [S011 pp. 8–10] |
| W14 | Dead ends in one sentence with the reason | Report preliminary variants that did not work and why | [S061 p. 12; S006 p. 22; S051 pp. 13, 15, 16; S014 pp. 21–22] |

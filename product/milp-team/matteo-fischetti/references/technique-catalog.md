# Matteo Fischetti · Technique catalog

> Date: 2026-11-28 (stage T3.6). Transferable techniques found in the paper cards, grouped as proof devices (PD), design moves (DM), experiment and evaluation protocols (EP) and writing moves (WM). Each entry has a one-line **How to use** and the cards with pages. `[S011 p. 12]` is paper card S011 at the `[[page N]]` page of the file listed for that ID in [sources/papers/INDEX.md](sources/papers/INDEX.md); most files are author preprints or reports, not the journal printings; the version read for each card is in the ledger's [card key](research/09-evidence-ledger.md#card-key) (column *Version read*). Source: [research/08-deep-reading-synthesis.md](research/08-deep-reading-synthesis.md) §7 (technique inventory) and the transferable-technique lists of the cards, re-read for this catalog. The card ids resolve to works in the ledger's [card key](research/09-evidence-ledger.md#card-key).
>
> **Voices.** Almost every entry rests on co-signed work whose "we" cannot be split; several author lists are alphabetical. Sole-author texts: S109 (2016) and the 2026 notes S161, S163 and S164; S161 states that the idea and the supervision are his and that everything else was done by an AI assistant [S161 p. 4]. Entries resting on 2025–2026 work are dated so that they are not projected backwards. Martina Fischetti, a separate researcher, is first author of S100, S143, S150, S154 and S162.
>
> **Left out.** Material that `research/holdout.md` seals is not in this catalog, also where another card states the same point; the cards' reading notes on inconsistencies inside a work are not used. The card batch files under `research/cards/` and the script-generated index `07-paper-cards.md` contain sealed points: do not open them while using or testing the skill.
>
> **Where SKILL.md uses them**: Method 1 step 5 (EP26); Method 2 steps 1, 3 and 5 (EP31, DM6, DM10, DM12); Method 3 steps 2 and 4 (EP19, EP18, EP35); Method 4 steps 1, 4 and 5 (EP1, EP2, EP15, EP11); Method 5 step 6 (EP21); Method 6 step 2 and the step-5 variant (DM1, DM7, DM21); Workflows S to F (EP31, DM1, DM7, EP18, EP33, EP17, EP22–EP25, EP20, EP8, EP27–EP29, WM2, WM5, WM8); Heuristic 10 (DM26, EP28); the Gomory anatomy (EP31, DM6). The evidence ledger adds DM17, DM18 and EP4 for Heuristic 11 and DM27 for Heuristic 10. The other entries are not cited in SKILL.md; they are the rest of the inventory, for use on demand.

## 1. Proof devices (PD)

PD1–PD8 and PD18 are polyhedral proof devices (facets, lifting, Chvátal–Gomory derivations, hardness), mostly from the 1990s polyhedral line. Polyhedral theory is outside this team's represented field (team.json), so read them as evidence of his habits, not as polyhedral advice in his name.

| # | Technique | How to use | Cards |
|---|---|---|---|
| PD1 | Facet proofs by explicit points | To prove a family facet-defining, build the affinely independent tours or points explicitly and argue the dimension by induction | [S030 pp. 5–6; S047 p. 14; S028 pp. 8–10] |
| PD2 | Closed-form lifting first | Lift sequence-independently in closed form (clique lifting) before falling back to sequential lifting | [S030 p. 6; S047 p. 15; S102 pp. 16–19] |
| PD3 | Prove on the monotonization | Prove facets on a full-dimensional monotonization and carry them back by an easy condition | [S102 pp. 13–16] |
| PD4 | Facets mapped from a related polytope | Map known facets of a related polytope onto a face and lift them; check the maximality of the lifted coefficients by a tree of 2-interchange moves | [S140 pp. 3–6, 16–18] |
| PD5 | Canonical form before "new" | Put an inequality in canonical form before claiming its family is new | [S102 pp. 24–26, 34; D003 p. 10] |
| PD6 | Chvátal–Gomory derivation as validity proof and separation handle | Show validity through explicit {0,1/2} or mod-k multipliers, then separate over the multipliers | [S022 pp. 2, 5–10; S139 pp. 3–9; S058 pp. 4–19] |
| PD7 | Rank-1 derivation as a cheap sufficient test | Where exact validity checking is NP-complete, use a known rank-1 derivation as a sufficient test; a point that violates by more than 1 certifies rank above 1 | [S058 p. 16; S102 p. 40] |
| PD8 | Hardness for the exact variant | Prove hardness for the variant you solve, not for a cousin; a two-way reduction to a known problem pins down the separation problem | [S002 pp. 4–5; S028 pp. 10–11; S022 p. 6] |
| PD9 | Integrality property and gap shares | Check the integrality property to know that the Lagrangian dual equals the LP dual; an exact duality-gap identity gives per-column gap shares | [S003 p. 3; S004 pp. 4, 14] |
| PD10 | Dualize the adversary into cuts | Dualize an adversary's LP into cuts on the master's binaries; derive generalized Benders cuts from Geoffrion's formula | [S073 pp. 4, 12–13; S072 pp. 5–7; S011 p. 5] |
| PD11 | Closed-form oracle with a proof | If the Benders slave is a continuous knapsack, write the cut from the critical item (only n distinct cuts per customer); replace a general QP solver inside a separator by a small exact routine proved by a monotonicity lemma and a KKT check | [S011 pp. 6–10; S195 pp. 7–8] |
| PD12 | Exactness kept local to integer points | Make the separator exact at integer points only (that suffices for correctness) and heuristic at fractional ones; add lazy cuts on infeasible integer points only | [S006 pp. 3, 6; S038 p. 13; S040 p. 5] |
| PD13 | Exactness kept around a heuristic wrapper | Impose a branch's complement only after the branch is closed, and cut off a reference solution only with a certificate that it is optimal for its fixing | [S001 pp. 7, 10] |
| PD14 | Order and exchange arguments | Prove a pruning rule by the lexicographically minimal optimum and an exchange argument; reduce the proof to the two properties of the order it uses, then substitute any object that has them (a fixed random objective) | [S124 pp. 8–11] |
| PD15 | Lexicographic nogood for finite convergence | A nogood that forces a strict lexicographic worsening proves finite convergence | [D019 p. 7; S137 p. 7] |
| PD16 | Symmetry by group averaging | Prove an aggregated (shrunken) model a relaxation by averaging over the group, and show with a two-line counterexample which convexity assumption carries the proof | [S097 pp. 4–7; D013 pp. 2–5] |
| PD17 | Small examples as arguments | Build the smallest example that carries the point: a five-variable counterexample to one's own old criterion, hand-made instances whose LP values show each strengthening, the Cook–Kannan–Schrijver example from the literature | [S124 pp. 6–8; S014 pp. 9, 21; D009 pp. 14–15] |
| PD18 | Compute, then prove | Use PORTA or an exact separator on small cases to find or check facets before proving them | [S028 p. 11; S077 p. 7; S033 pp. 12–13] |

## 2. Design moves (DM)

| # | Technique | How to use | Cards |
|---|---|---|---|
| DM1 | A neighbourhood as one linear constraint | Write the neighbourhood as one Hamming-distance constraint on the binaries around the incumbent and let the black-box solver explore it; the complementary branch keeps the scheme exact; use the asymmetric form for supports of constant cardinality | [S001 pp. 3–5, 7; S085 pp. 4–5] |
| DM2 | Soft cutoff with a priced slack | Add the objective cutoff with a heavily priced slack, so the old incumbent warm-starts the solver and its own neighbourhood heuristics stay on | [S052 pp. 11, 15; S154 p. 5; S086 pp. 2–3] |
| DM3 | Steer the black box lightly | Steer the stock solver only by branching priorities, or by one heuristic bound that its presolve propagates; drop your own checks when presolve detects the same as fast | [S063 p. 8; S067 p. 9; S059 pp. 6–7] |
| DM4 | Big-M bounds by truncated auxiliary MILPs | Tighten big-M bounds by time-limited auxiliary MILPs, computed once and cached | [S008 p. 5; S054 p. 5] |
| DM5 | A huge family outside the model | Enforce an exponential constraint family in the lazy-constraint callback instead of the initial model | [S145 pp. 15–16; S079 pp. 3, 9–10] |
| DM6 | Lexicographic reoptimization on a black-box LP solver | Fix the nonbasic variables with nonzero reduced cost and reoptimize the next variable over the remaining optimal face; no perturbed objective | [D009 pp. 4–5; S074 pp. 6–7; S137 pp. 6–7] |
| DM7 | Separation as a MIP over multipliers | Write separation as a MIP over the CG multipliers (support restriction, complementing, a light multiplier penalty); accept any feasible solution as a cut and ask for optimality only in the last round | [D003 pp. 3–5; S033 pp. 4–7; S142 pp. 4, 8–10] |
| DM8 | Slow MIP separation as timed preprocessing | Move a slow MIP separator to a time-limited preprocessing phase before the standard solver | [S142 p. 10; S096 pp. 8–10] |
| DM9 | Cuts from bases of the original system | Read Gomory cuts only from bases of the original system, relaxed in Lagrangian fashion, so they stay valid and clean | [S095 pp. 2, 5–6] |
| DM10 | In-out root loop with its constants | Stabilizer at all ones (a feasible point of a master with only 0-1 bounds and Σ y ≥ 2), moved halfway towards each LP optimum; separate at λy* + (1 − λ)ỹ + δ(1, …, 1) with λ = 0.2 and δ = 2ε, ε = 10^-5 the paper's internal threshold; after 5 iterations without bound improvement set λ = 1, after 5 more δ = 0, after 5 more stop; drop slack cuts every 5th iteration | [S011 pp. 5, 12–13; S195 p. 15] |
| DM11 | In-out endgame and cheap seeding | Separate the vertex itself after more than three consecutive core-point updates; seed the inner point with a first feasible solution from the solver's heuristic, or with a formula point (all components 1/2 when every row is covered by at least two columns) | [S106 pp. 3–4; S174 pp. 3, 7–8] |
| DM12 | Tailing-off relative to the initial gap | Stop a cut loop when the bound gain of the last iteration falls below 10^-3 of the initial integrality gap for 3 consecutive iterations, with at most 100 iterations (a limit never reached in that test bed) | [D014 p. 15] |
| DM13 | Separation cascade with early exit | Call separators from cheap to exact and stop at the first that returns violated cuts; return nested families per round | [S005 pp. 12–14, 19–21; S069 p. 14] |
| DM14 | Conditional cuts and deferred regions | Add cuts valid only for improving solutions; exclude a region by one cut, store it and solve it at the end | [S009 pp. 9, 17–18; S047 pp. 40–41, 48–49] |
| DM15 | Propagate each rounding | Round one variable at a time and propagate before rounding the next, as in a dive without LPs | [S041 pp. 9–13] |
| DM16 | One engine, independent switches, a work cap (2025) | Build one search engine with independent switches, violations read from the propagation engine's activities, and a deterministic work cap | [S126 pp. 6–8, 14, 19] |
| DM17 | Decoupled search and certificate LPs (2026) | Put an invalid guidance constraint only in the search LP and decide acceptance with a second LP that carries only the model's constraints, each LP warm-started from its own basis | [S164 p. 8] |
| DM18 | Exact repair after an approximate model | Solve the approximate MIP, fix its combinatorial choices, solve the exact LP; if it fails, drop the worst item and repeat | [S046 pp. 22–23; S198 pp. 61–63] |
| DM19 | Diversify parallel runs by one index | Let one index set the seed, the restriction and the presolve option of each independent run | [S059 p. 8] |
| DM20 | Self-splitting by deterministic node colouring | Split the tree among workers by a deterministic colouring of the nodes, with no communication | [S111 pp. 4–8; D017 pp. 19–20] |
| DM21 | Keep what an expensive call produced | Store a successful auxiliary MILP as a move checked cheaply at every node; let every strong-branching LP update all candidates it informs; read covering rows and pseudocosts off interrupted runs | [S124 pp. 9–10, 13; D012 pp. 3–4; S063 pp. 5–6] |
| DM22 | Lagrangian heuristic at many multipliers | Run the greedy at many near-optimal multiplier vectors; drive the step size by the spread of recent bounds; re-price a dynamic core every T iterations | [S004 pp. 5–7, 12–13; S012 pp. 10–11] |
| DM23 | Structural multipliers first | Try multiplier values fixed by a structural argument before subgradient optimization; add counting constraints that are redundant in the full model but binding in the relaxation | [S012 pp. 16–17; S017 pp. 10, 12–13] |
| DM24 | Model the decision, not the description | Shift a uniform edge cost into node costs and drop the edge variables; index time by tour position to remove big-M; one continuous variable per location instead of one per pair | [S040 p. 4; S144 pp. 3–4; S100 pp. 8–9] |
| DM25 | Rules as data | Encode new rules as data the generator already reads; express variants as data of one model | [S061 pp. 10–12; S100 p. 15] |
| DM26 | Numerically safe by construction | Write a cutoff that is tight at no integer point (2cᵀx ≤ 2U − 1); tie cut validity to the LP solver's reduced-cost test with a conservative ε and integer arithmetic; compute intersection-cut coefficients from the original data, so that numerical error can only weaken the cut | [D009 pp. 4–5, 15; S074 pp. 10–11; S016 pp. 18–21] |
| DM27 | Separate at a perturbed point | Separate at y* + 2ε, which keeps the cuts valid and also helps plain Kelley; skip a numerically risky strengthening near 0 and 1 | [S011 p. 12; S195 pp. 13–14] |

## 3. Experiment and evaluation protocols (EP)

| # | Technique | How to use | Cards |
|---|---|---|---|
| EP1 | A (possibly dummy) callback in every arm | Give every arm, the baseline included, the same callback interface, so that the solver's features are on or off alike | [S070 p. 10; S055 p. 6; D017 p. 22] |
| EP2 | The optimum on input | Give every arm the optimal value as cutoff to isolate a branching or cut effect from primal luck | [S013 p. 23; D017 pp. 16, 21; D012 pp. 6–7] |
| EP3 | Trajectory identity | For a pure speed-up claim, show that the trajectories are identical | [S130 p. 16] |
| EP4 | An external validator | Judge every method with a validator or simulator that shares no code with any optimizer | [S018 pp. 9–11; D004 pp. 6–7; S150 pp. 9, 15–16] |
| EP5 | Classes by all codes | Define difficulty classes by a rule in which every compared code plays the same role (the larger node count of the arms, any compared solver's time) | [S070 pp. 10–11; S055 p. 7; S079 pp. 10–11, 14] |
| EP6 | Keep instances easy for the rival | Keep the instances that are easy for the rival; dropping them would bias the set | [S079 p. 16] |
| EP7 | Subsets fixed by the challenged method (2026) | Fix analysis subsets in advance by one pilot run of the challenged baseline, then rerun every declared comparison on the full test bed to check its sign | [S164 pp. 11, 13] |
| EP8 | Known optima by construction | Build test instances whose optima are known by construction | [S046 pp. 12–13; S198 p. 52] |
| EP9 | Generators specified fully | Specify every instance generator fully and add a second generator for sensitivity | [S005 pp. 25–26, 28] |
| EP10 | Difficulty ladder by objective cutoff | Make harder variants of each instance with a cutoff z*(1 + β), β ∈ {0.1, 1, ∞} | [S041 p. 14] |
| EP11 | Tuning set apart, test set fixed before any run | Tune on instances that take no part in the evaluation; draw the held-out set from a seed fixed before any run | [S078 pp. 8–9; S164 p. 17; S162 p. 17] |
| EP12 | The solver in its emphasis settings | Run the same solver in both emphasis settings and measure the gap to the best value any code found | [S001 p. 12] |
| EP13 | The rival's settings searched | Try the rival's settings (with vendor advice where available), report its failures under each, compare against its best | [S007 p. 6; D011 p. 3] |
| EP14 | Rival tuned as carefully | Tune the rival as carefully as your method, give it its own tuning paragraph, run it under its own natural parameter | [S056 pp. 29–34; S003 p. 5; S010 p. 8] |
| EP15 | Rival re-implemented and validated | Re-implement the rival in your framework and validate it against its published results | [S027 pp. 22–23; S082 pp. 7, 12; S092 p. 16] |
| EP16 | Machine factor against oneself | When rival times come from another machine, take the factor from two benchmarks, round it against yourself and print the groups lost | [S014 pp. 13, 16; S087 pp. 5–6] |
| EP17 | Seeds with a success rule | Ten seeds per instance and variant; an instance counts as solved if more than 6 of the 10 runs succeed; plot per-seed results of two variants on one instance | [S041 pp. 14–15] |
| EP18 | Best-of-k-seeds ceiling | Before exploiting randomness, compute the best-of-k-seeds curve (k = 1 to 100) with unsolved counts and nodes; it is the ceiling of any selection rule | [S055 p. 3] |
| EP19 | Control arms | Add a change without content (every cut scaled by 1,000), a deliberately wrong variant, arbitrary orders, a pure-random arm or an A/A null, and read the method's gain against it | [S068 p. 8; S074 p. 8; S041 p. 20; S126 p. 20; S163 pp. 2, 5] |
| EP20 | Tests for small studies | 95% confidence intervals on relative improvements; Cochran Q with post hoc McNemar for several variants; McNemar on a 2×2 success table; paired t-intervals | [S041 pp. 15, 17, 20; S126 p. 25; S150 pp. 14, 19] |
| EP21 | Declared family and registered outcomes (2026) | Declare the comparison family before the data and correct with Holm; register a three-outcome rule in which an inconclusive outcome is not a negative one; for a null, give an exact interval and the effect sizes still compatible with it | [S164 pp. 13, 16; S163 pp. 6, 8] |
| EP22 | Primal integral and gap closed | Report the primal integral at several horizons with pairwise curves; % gap closed with its formula and the direction of a time-limit bias; iterations to close 90, 95 and 99% | [S052 pp. 14, 17–19; S033 pp. 9–10; S174 pp. 7–9] |
| EP23 | Shifted means with stated shifts | Give shifted geometric means with their shift, and profiles whose population is disclosed | [S027 pp. 24–26; S016 pp. 26–29] |
| EP24 | Machine-independent counts on a loaded machine | On a shared or loaded machine report deterministic ticks, or nodes and LP iterations, instead of seconds | [S094 p. 8; S055 p. 3] |
| EP25 | Numerical-health indicators and exit codes | Report the maximum coefficient, condition number and basis determinant beside the bound, and an exit code per run that says why it stopped | [S074 pp. 12–13; D009 pp. 23–24] |
| EP26 | Ablation by removal | Remove one device at a time and all at once; put an ablation arm in every table; print the ablation that hurts your own ingredient, with the reason | [S057 pp. 25–26; S032 pp. 16–19; S137 p. 9] |
| EP27 | Zero-tolerance re-solve | Before claiming a new optimum, re-solve with zero optimality tolerance, starting from the value found | [S055 p. 4] |
| EP28 | Cut-validity stress test | Fix the incumbent, perturb 80% of its entries by 10^-9 to 10^-1, separate, add the cuts and re-solve, 10,000 times; write the model to a file on infeasibility | [S011 p. 16; S195 p. 20] |
| EP29 | Every solution re-read (2026) | Re-check every reported solution in a separate solver process on the original, unpresolved model, and count a failed re-check as a failure | [S164 pp. 11, 17] |
| EP30 | Count the solver's wrong answers | Tighten the tolerances and count the solver's wrong answers against an exact method | [S101 pp. 12, 16–17] |
| EP31 | One-instance mechanism plots | On one small stalling instance, plot bound, average cut coefficient, basis determinant, cut depth and the distance between consecutive separated points against iterations; project the separated points by multidimensional scaling | [D009 pp. 7–11; S074 pp. 14–16] |
| EP32 | Hardware checks | Benchmark each nominally identical machine; run both legs of a paired ratio on one chip; give values at proportionally longer limits to show what a faster processor would give | [S144 p. 9; S163 pp. 10, 17; S059 pp. 8–9] |
| EP33 | Ideal-oracle ceilings | Print, beside the method, the better of the two arms per instance and the best of all clones; outside randomised restarts an ideal oracle shows how little a cheap score leaves | [S055 pp. 6–7; D017 pp. 14–15] |
| EP34 | Standalone and at the embedded budget | Test a primal heuristic standalone and with the budget it would have inside branch-and-cut (an iteration limit, the last-resort stage off) | [S041 pp. 13–14] |
| EP35 | Bet-and-run | Diversify C = 5 clones at the first LP's optimal face (random costs on the nonbasic variables with zero reduced cost, a capped reoptimization), run each for N = 5 nodes, bet on one by eight short-run indicators in priority order (open nodes first, then bound improvement over the root, integer-infeasible variables, …), dropping indicators that do not discriminate (θ = 0.2) and breaking ties towards the unperturbed clone; finish the chosen clone | [S055 pp. 4–6] |

## 4. Writing moves (WM)

| # | Technique | How to use | Cards |
|---|---|---|---|
| WM1 | A lesson and status labels | Close with a lesson learned and label every claim: lead, post hoc, computational conjecture | [S022 p. 16; S067 p. 7; S164 pp. 6, 15, 19] |
| WM2 | What is not claimed, first | Say early what the paper does not claim; put status and scope in the abstract | [S059 pp. 2–3; S133 pp. 1–2] |
| WM3 | Questions as the skeleton | Pose the paper's questions at the start and answer them in order | [D003 pp. 1, 3, 5–9; S033 pp. 1, 3, 7–12] |
| WM4 | Roles and inheritance stated (2026) | Name the roles before the experiments and say in one paragraph what is inherited and what is new. A drafting move of a paper whose original draft is Martina Fischetti's (CRediT; his role: review and editing) | [S150 pp. 3, 9, 28] |
| WM5 | Null results in a section of their own (2026) | Give null and negative results their own section; flag in the abstract a headline added after the design. AI-assisted drafting is declared for this manuscript | [S164 pp. 1, 13, 16–19, 25] |
| WM6 | Name the mechanism | Give the mechanism a name the reader can carry | [S052 p. 5] |
| WM7 | Credit precedents, claim the combination | Credit the precedents and limit the claim to their combination; credit the lineage in the abstract | [S150 pp. 3, 6; S106 p. 1] |
| WM8 | Reframe for the venue, keep the evidence | When a report becomes a paper, change the framing and keep the numbers | [S195 pp. 1–2, 14, 18, 26] |
| WM9 | New cut on the standard example | Introduce a new cut on the field's standard two-variable example; take one worked example through every cut round | [S194 pp. 13–16; S072 pp. 11–12] |
| WM10 | Traces before tables | Open the evidence with one-instance traces, then the aggregates | [S074 p. 3; S195 pp. 15–18; S164 pp. 4–5] |

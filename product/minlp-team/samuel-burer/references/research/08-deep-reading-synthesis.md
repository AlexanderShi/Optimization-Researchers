# Samuel Burer · Deep-reading synthesis

> Round 1 synthesis, 2026-10-10 (first version of this note; no earlier 08 existed). It aggregates every card in `cards/*.digest.json` (index: [07-paper-cards.md](07-paper-cards.md)) under the house rules of `references/paper-reading-card.md` §三 (conservative update) and `references/research-extraction-framework.md` §三 (four-way validation) and §十一 (quality checklist). Every statement points to card ids with file pages, e.g. [S004 p. 2]. Quotation marks are used only for text copied from a card's verified quote list (`verify_card_quotes.py`: 138 quotes, 0 not found). This note proposes changes to `SKILL.md`; it does not edit it.

## 1. Coverage

| Item | Count | Source |
|---|---|---|
| Works indexed (Scholar + DBLP + Crossref + homepage) | 71 (70 Scholar rows) | 07 coverage row |
| Open full text on disk | 67; no open text for 4 (S068, S069, S070, D001) | INDEX.md |
| Card entries / works with a card | 73 / 71 | 07 |
| Read in full | 52 cards | digests |
| Read in part (supplement short cards) | 15 cards | digests |
| Abstract only | 3 entries (S068, S069, and S061 in a2-01, superseded by the full c3-01 card) | digests |
| Metadata only | 2 (S070 thesis, D001 editorial) | digests |
| Unreadable | 1 entry (S061 in c07: the file held the S019 article, not the correction; the correction was then read in full in c3-01) | [S061 c07 card; S061 c3-01 pp. 1-4] |
| INDEX Read column after `mark_read_from_cards.py` | carded 52, skimmed 15, abstract 2, metadata 2 | script output, 2026-10-10 |

Distinct works counted below use the best card per id, so S061 counts once (full). Periods: 2000-04 11 works, 2005-09 17, 2010-14 18, 2015-19 12, 2020-24 7, 2025-26 6.

Version caveats that bound every claim below: S012 and S016 were read as preprints [S012 card header; S016 card header]; S019 as arXiv v2 [S019 card header]; S048 as arXiv v3 [S048 card header]; S049 as arXiv v2, not the published text [S049 card header]; S058 as v3 only, v1 and v2 not read [S058 card header].

## 2. Evidence per existing method

Counts are distinct cards linking to the method in their digest (a card can be both evidence and variant).

| Method | Evidence | Variant | Contradiction |
|---|---|---|---|
| M1 Package the difficulty in one convex object | 35 | 18 | 0 |
| M2 Kitchen sink first, then the hull of a small substructure | 25 | 4 | 0 |
| M3 Let computation propose, certify exactly, narrow publicly | 29 | 15 | 0 |
| M4 Engineer the hard pool, disclose the filter, keep the ladder | 11 | 23 | 0 |
| M5 Prototype first, let theory follow | 23 | 6 | 1 (S041) |

### M1 · Package the difficulty in one convex object

- **Strongest cards**: the founding text with the "package" sentence, the key assumption as the hypothesis that makes the cone exact, special cases restated, then tractable approximations [S004 pp. 2-3, 11-16]; the stated rule "When faced with a new optimization problem, it thus seems prudent to determine if that problem can be modeled as a linear conic program over some (hopefully) well understood K." [S009 p. 2]; all of bounded QCQP as one linear conic program, "This approach focuses the difficulty of nonconvex QPs completely on the CP matrices." [S022 p. 1]; the CP → DNN → solver chain [S020 pp. 3-5; S008 pp. 2-3, 5, 11]; the 2009 key assumption reused as an assumption in data-driven DRO [S044 pp. 9, 11-14]; the Lorentz-positive cone with a dual oracle because the explicit LMI is too large [S065 pp. 2, 6-7]; the slight lift that makes m = 2 exact [S049 pp. 3, 11-14]; an exactness hypothesis rewritten as a picturable geometric condition [S061 pp. 2-3]. The 2006 CAREER abstract already names "linear programs over convex cones" as "one of the main tools" [S068 abstract].
- **Say-do update**: stated 2006-2012 [S068 abstract; S004 p. 2; S009 p. 2; S022 p. 1] and practised in 35 cards from 2005 [S034 pp. 5-6, 11] to 2026 [S065 pp. 2, 6-7]. Keep ✅. Add as Practice: the one-coordinate lift is already in 2012 [S022 p. 2], a decade before the slight-lift paper; step 1 of M1 in practice also adds redundant quadratic equations before relaxing (see H11 below) [S004 pp. 4-5, 14; S009 pp. 8-9].
- **Stop-rule evidence**: a cheaper intermediate built and costed, "In particular, we do not see a full order-of-magnitude speed up." [S043 pp. 2, 18]; cheaper computational routes when the exact LMI is too large [S065 pp. 6-8].

### M2 · Kitchen sink first, then the hull of a small substructure

- **Strongest cards**: the combined relaxation RLT + psd + BQP beaten on box QP, exact for n ≤ 2 and strictly weaker at n = 3, certified by a rational point [S011 pp. 4, 14-16]; an explicit intersection L-RLT-R2-S2-PSD with SOC × linear products as a precursor of SOC-RLT [S016 preprint pp. 5-12]; exact at n = 2, counterexample at n = 3, disjunctive form used only to certify [S010 pp. 3, 8-12]; TRS machinery re-derived and pushed to the first certified counterexample [S012 preprint pp. 2-4, 13]; the kitchen sink built explicitly and one more ingredient tested and found to add nothing [S049 pp. 2-3, 5-9]; proof for n ≤ 3, certified boundary at n = 4, full RLT plus triangle inequalities shown not to close the gap [S058 pp. 12-14, 44]; the ladder Shor ≥ RLT ≥ KRON ≥ SEP ≥ true with an n = 2 counterexample [S065 pp. 16-18]; n = 2 proof, conjecture beyond [S038 pp. 3-5, 20]; a cut-generating process collapsed into one SOC in the original variables [S039 pp. 3, 6].
- **Stated**: "For example, analyzing — and generating cutting planes for — the various convex hulls that arise in MINLPs (see Section 5.4) will require aspects of both polyhedral theory and convex analysis to achieve best results." [S002 p. 8]; "Special cases can also allow the development of newer techniques (e.g., semidefinite relaxations), which may then progress to more general techniques." [S002 p. 9].
- **Say-do update**: the practice is in the full texts from 2009 [S011 pp. 4, 15-16] and 2011 [S016 preprint pp. 5-12], so the written programme (2012 survey) and the *kitchen sink* label (2021 talk, per SKILL.md) came after the practice. Keep ✅; add S011 and S016 as the earliest Practice items. The recurring proof engine is the Pataki rank bound plus a rank-one perturbation of an extreme point (§7.1, P1).

### M3 · Let computation propose, certify exactly, narrow publicly when wrong

- **Strongest cards**: the full correction note: error located in the analysis of system (12), shown fatal, strongest provable case kept, finders named, "However, in truth the proof fails because, with this setup, the systems cannot be simultaneously feasible." and "Instead of the purported Theorem 3, we now prove an analogous theorem, except that it only applies to diagonal instances of (1)." [S061 pp. 1-2]; exact rational certificate for the n = 4 counterexample and genericity read into the verdict, "The experiment is therefore best understood as evidence that violations of tightness are rare." [S058 pp. 27, 43-44, 46]; "So we conjecture that the two values are equal when the cuts do not intersect." [S012 p. 13], proved with student Yang [S021 pp. 3, 7, 10, 12]; a colleague's conjecture credited, "(This result was conjectured to us by Anstreicher [2].)" [S011 p. 14]; a claim of the 2003 paper narrowed in 2005 [S003 pp. 7, 12]; a certified explicit counterexample bounding a sufficient condition [S048 pp. 9, 39-42]; a counterexample published against his own 2025 relaxation [S065 pp. 12, 16-17].
- **Say-do update** (full texts change two details):
  1. Exact certification is older than SKILL.md says: a negative claim certified by an exact rational point already in 2009, with Letchford [S011 pp. 14, 16]; later in 2025-26 [S058 pp. 43-44; S065 p. 16]. In between, non-membership and counterexamples are certified numerically only [S010 pp. 9-11; S012 preprint p. 13].
  2. The two-signal rule is intermittent, not a steady habit: early two-signal forms exist (infeasibility plus primal-dual agreement with another code [S001 pp. 14, 17]; a rank measure beside the gap [S012 preprint pp. 13, 19-21]; "In other words, when an algorithm claims to have solved an instance optimally, it is independently verified by the other algorithms up to six significant figures." [S059 p. 15]), but "tight" or "solved" rests on one signal in 2015, 2023 and 2025 papers [S024 p. 28; S050 p. 22; S048 pp. 11, 13; S058 p. 27]. The gap-plus-eigenvalue-ratio thresholds are specific to the ball-constraint paper [S049 p. 10].
- Keep ✅ with these dates; the variants are listed in §3.

### M4 · Engineer the hard pool, disclose the filter, keep the ladder

- **Strongest cards**: literature failure instances first, then a theorem-based generator credited to Wolkowicz [S012 preprint pp. 16-19]; the BoxQP ladder 54 → 90 [S018 pp. 11-14] → 99 with a new rung [S020 p. 12]; a pool of 4,835 of 6,000 instances on which the baseline fails, filter disclosed [S024 p. 28]; the 2013 unsolved set reused, "Applying our heuristic lifted-RLT constraints to the 215 previously unsolved instances, we can solve 82—about 38%—of them; see Table 3." [S033 p. 19]; Shor-solved instances excluded and the 267 and 212 hard sets reused [S049 pp. 15-16, 20]; seed screens and a harder rung added [S065 pp. 8, 12, 15-16].
- **Say-do update (scope)**: the hard-pool practice appears in two lines only, the trust-region/ball line 2013-2026 [S012, S024, S033, S049, S065] and the BoxQP ladder 2008-2010 [S018, S020]. In 23 cards the testbed is a public library or an unfiltered random panel [S006 pp. 10-15; S013 pp. 15-16; S043 pp. 13-14; S047 p. 17; S055 pp. 9-10; S059 p. 16; S048 pp. 11-12; S058 p. 27; S057 pp. 11, 16], or the filter removes trivial instances or instances with numerical trouble rather than selecting baseline failures [S008 pp. 14, 16; S045 p. 21]. Scan counts are disclosed for some families and not others [S049 p. 15; S050 pp. 22-27; S065 pp. 8, 16]. Proposed wording: M4 is how he tests a claim about the marginal strength of a relaxation over an incumbent; for speed/bound trade-offs and applications he uses public or random sets [S043 pp. 13-14]. Keep ✅ for the stated rule; mark the practice as scoped.

### M5 · Prototype first, let theory follow

- **Strongest cards**: a known factorization plus a rank theorem, the theory gap printed, "Although we have some theoretical justification that explains the observed practical convergence, we do not currently have a formal convergence proof." [S001 pp. 2-3, 14-16, 27]; the proof two years later, for a variant that is not run: "While it seems that the extra term is necessary for theoretical convergence, it does not appear to be necessary for practical convergence." [S003 pp. 3, 13]; a variant of an existing code benchmarked against the best codes available [S014 pp. 8, 13, 18, 20]; the bottleneck timed first and inner problems solved loosely, "Consistent with the experience of Burer–Vandenbussche [7] and other augmented-Lagrangian methods for SDP, we find that it pays only to solve these problems very loosely." [S020 pp. 4, 11-12, 16]; failed enhancements printed [S026 p. 19; S031 p. 16]; best public global codes as baselines with failed variants explained [S059 pp. 17-23]; algorithm first, no convergence theory, in 2026 [S056 pp. 9-15].
- **Contradiction**: theory carries the paper and a later experiment refutes the computational hypothesis, printed openly; "These results are a testament to the high quality of current LP software." [S041 pp. 23, 25]. Also a theory paper whose numerics sit in companion reports [S017 pp. 2, 25] and an abstract-assumption convergence framework with no code [S051 pp. 4-22].
- **Say-do update**: M5 is the mode of his algorithm papers that carry a code claim; it is not his only mode for algorithms. Proposed addition to M5 Limitations: theory-first algorithm papers exist (2002, 2003, 2009) [S017; S051; S041]. The step that runs baselines at their defaults (M5 step 5) has exceptions where he tunes or handicaps the baseline in its favour (see H5 update, §5.2).

## 3. Variants and contradictions

### 3.1 Variants (recorded, nothing deleted)

| Method | Variant | Cards |
|---|---|---|
| M1 | Reverse direction: leave the convex lifted object for a smaller nonconvex formulation (factor, rank-two, Cholesky elimination) because the aim is speed or primal solutions | [S006 pp. 2, 4; S017 pp. 8-9; S025 pp. 4, 10; S001 pp. 5, 27; S003 pp. 6-7; S030 pp. 6-7] — explained by the promoted Method 6 (§4) |
| M1 | The lifted object used as a node relaxation inside branch-and-bound, not as an exact reformulation | [S007 pp. 8-9, 14; S018 pp. 4-5; H001 p. 3] — explained by H12 (§5) |
| M1 | One lifted object that is a strict relaxation; effort moves to the data regime where it is tight | [S048 pp. 3-4, 7-9, 39-41] |
| M1 | The hull reflex carried into constraint learning: hull of the graph, inner-approximated from data | [S057 pp. 7-9] |
| M1 | Unification instead of exactness: one parameterized family containing classical procedures | [S041 pp. 9-11; S051 pp. 2, 11] |
| M2 | Root-equivalent strengthenings; gains only on subdivided boxes inside B&B | [S047 pp. 2, 13-20] |
| M2 | Stack and recombine on the whole problem, no small-substructure hull | [S055 pp. 3-7] |
| M2 | Disjunctive start only partly eliminated (a projection, not direct) | [S038 pp. 3, 18] |
| M3 | Single numerical signal for "tight"/"solved" | [S024 p. 28; S050 p. 22; S048 pp. 11, 13; S058 p. 27] |
| M3 | Floating point called irrelevant for the finiteness claim (opposite pole to exact certificates) | [S007 p. 3] |
| M3 | Claims printed without proof or with proofs omitted | [S022 p. 4, "For the sake of space, we do not prove these claims here."; S039 pp. 21-22] |
| M3 | A high-probability theorem resting on a counting argument with a Monte Carlo check, later withdrawn and narrowed | [S019 pp. 15-17; S061 pp. 1-2] |
| M3 | Inexactness beyond m = 2 supported by solve counts, not a certified counterexample | [S049 pp. 3, 16-17] |
| M4 | Public libraries or unfiltered random panels (23 cards) | see §2 M4 |
| M4 | Baseline advantaged instead of a hard pool | [S044 p. 14] |
| M5 | Theory first, numerics elsewhere; theory re-proved for a modified relaxation | [S017 pp. 2, 25; S018 pp. 8-11] |
| M5 | Competitors tuned by grid search, parameters made adaptive for fairness | [S056 pp. 9-11] |
| M5 | Implementation drops the theoretical neighbourhood: "Third, in our implementation of Algorithm SDP, we do not bother to stay in the neighborhood N (γ), since our computational experience indicates that this does not yield a substantial practical improvement." | [S029 p. 22] |

### 3.2 Claims of SKILL.md that the full texts contradict or correct

| SKILL.md claim | What the full texts show | Proposed change |
|---|---|---|
| M1 stop rule: the *Faster, but weaker* paper (2014) was his answer to Bao, Sahinidis & Tawarmalani's DNN-cost finding | The 2014 paper motivates by interior-point SDP cost, never mentions DNN and does not cite Bao et al. [S043 pp. 2, 19]; OptDNN's stated entry point is a SeDuMi timing of the DNN bottleneck [S020 p. 4] | Reword as *consistent with*, not *his answer*; keep the Bao et al. finding as outside critique |
| M3 Practice: exact rational certificates dated 2026; Tension 2 contrasts the 2008 floating-point remark [S007 p. 3] with 2026 | Exact rational point already in 2009 [S011 pp. 14, 16]; exact certificate 2025 [S058 pp. 43-44] | Date exact certification to 2009 (with Letchford), routine in 2025-26 |
| M3 step 2: two signals as a rule | Two-signal forms in 2003, 2013, 2017, but single-signal declarations through 2025 (§2 M3) | Mark the rule as intermittent; cite S001, S012, S059 as early forms |
| M4: practice as a general habit | Confined to two lines (§2 M4) | Scope M4 to relaxation-strength claims |
| M5: the order prototype → theory | Theory-first algorithm papers exist [S017 pp. 2, 25; S041 pp. 23, 25; S051 pp. 4-22] | Add to Limitations |
| Tension 3 and Honest Boundary U1 (SKILL.md wording: *no heuristic paper after 2002*) | SDP relaxation plus randomized rounding for ensemble pruning (2006) [S005 pp. 7-8]; SDP rounding plus FM local search for hypergraph bisection (2011) [S063 pp. 4-5, 9]; specialised local search for trained networks, "In a nutshell, we double down on the trend of using specialized local search with lower per-iteration cost to find better solutions in constraint learning." (2026) [S056 pp. 6-9, 15] | Narrow to: no heuristic paper in his core nonconvex-QP line after 2002; heuristics recur in co-authored applied papers (2006, 2011, 2026) |
| Trajectory (SKILL.md wording: *leaving low-rank algorithms (2004)*); U3: no benign-nonconvexity paper since 2004 | Low-rank algorithm work continues in 2006 [S026 pp. 4-7, 19] and 2007 [S031 pp. 3-5]; SDPLR maintained as software in 2009 [H002 pp. 1-4]; his SDPLR toolkit applied in 2011 [S063 pp. 7-8]; a global certificate for nonconvex local solvers in 2025 [S048 pp. 5-7, 14] | Date the exit from low-rank algorithm papers to about 2007; note the 2025 return through certificates (Method 6) |
| Trajectory: robust optimization ends 2018 | Robust grading in 2019 [S062 pp. 5-8] | Date the applied/robust period 2012-2019 |
| H10 (SKILL.md wording: *Dated: 2023–26 only*) | Public code earlier: SDPLR software [H002 pp. 1-3]; QuadprogBB public [S008 p. 11]; code repositories [S050 p. 6; S049 p. 4] | Code release from 2009; seed/manifest discipline 2023-26 |
| M3 evidence quotes for the 2023 ball-constraint paper are from arXiv v1 | The corpus text is v2, whose wording differs at the same places [S049 pp. 10, 15] | Keep the v1 quotes labelled as v1 (from web research), or replace them with the v2 wording from the card |

No SKILL.md claim about the 2021 correction is contradicted: the correction text names Kılınç-Karzan and Wang as finders and confirms the quoted sentence [S061 p. 1]. Whether arXiv 1802.02688 was updated is not settled by any card (§11).

## 4. Promotions

### Method 6 (new core method): Solve in the cheap nonconvex space, certify in the convex dual

**One line**: When a convex (or exactly relaxed combinatorial) problem is too big for interior-point methods, move to a smaller nonconvex formulation whose optimum a theorem guarantees, prove what its stationary points are, and read a global certificate or a valid bound from the multipliers of the nonconvex method, so that speed never costs the certificate.

**Cards (8 distinct works, 2001-2025)**: [S014 p. 8] dual slack from stationarity multipliers certifies global optimality of the factored maxcut problem; [S017 pp. 19, 23-24] a dual estimate from a triangular system gives dual feasibility and the duality gap from the gradient, and the barrier problem has no spurious stationary points; [S001 pp. 5, 7, 13-14] rank sized by the Barvinok-Pataki bound, a stationary point with S ⪰ 0 is SDP-optimal, zero-column injection as a certificate, and the concession that a primal-only method gives no valid bound unless solved exactly; [S003 pp. 3-4, 13-15] no extraneous local minima, in-run certificates and a λ_min-shift lower bound; [S013 p. 6] the augmented Lagrangian chosen partly because it yields dual bounds; [S006 pp. 6-9] cuts other than maximum cuts are saddle points, restarts from perturbed cuts; [S025 pp. 5-6, 10-12, 17-18] rank-one/rank-two exact formulations, local maxima classified, escapes designed; [S048 pp. 5-7, 14, 17-20] an LMI certificate for the output of any Stiefel solver, made robust to inexact stationarity. Partial support: [S030 pp. 6-7] (convex SDP rewritten as NLP over a simple set).

**Four checks**:
1. *Cross-project recurrence* ✅: 8 works across the thesis-era SDP algorithms (2001-2006, Monteiro, Zhang, Vandenbussche) and a 2025 signal-processing problem with Michigan EECS co-authors [S048 card header].
2. *Say-do* ✅: stated, "In particular, we show that the change of variables does not introduce any extraneous local minima." [S003 p. 3]; "Thus, we can solve the nonconvex problem posed in (1.1) using any choice of solver on the Stiefel manifold and perform a fast check of its terminal output for global optimality." [S048 p. 14]; the limit stated where the certificate is missing, "Since these codes produce both an upper bound and a lower bound, while our code only gives the latter, the comparisons should not be taken at face value." [S006 p. 9]. Practised in every listed card.
3. *Executable, different from standard practice* ✅: standard practice either solves the convex SDP by an interior-point method (certified, expensive) or runs a local NLP solver with no certificate. Steps:
   1. Find the theorem that lets a smaller nonconvex formulation carry the optimum: a rank bound [S001 p. 5], an exact rank-one/rank-two restriction [S025 pp. 4, 10], a Cholesky elimination [S017 pp. 7-9], a column-wise lift [S048 p. 3].
   2. Map the stationary points: prove no spurious local minima, or classify local optima combinatorially and identify saddles [S003 pp. 3-4; S006 p. 7; S025 pp. 5-6, 12; S017 pp. 23-24].
   3. Build the dual estimate from the multipliers of the nonconvex method and test it (S ⪰ 0, an LMI in a few scalars) [S014 p. 8; S017 p. 19; S001 p. 7; S048 pp. 6, 17-18].
   4. Make it robust to inexact solves: shift by λ_min when the trace is implied [S003 pp. 14-15], or ε-relax the LMI and report the bound gap [S048 pp. 7, 19-20].
   5. Use the classification to design escapes: restart from a perturbation of a point the theory says is a saddle [S006 pp. 7-9; S025 pp. 17-18].
   6. Report primal and dual side by side, check for bound crossing [S001 pp. 14, 17], and separate certified, not-tight and local outcomes [S048 p. 13].
4. *Exclusivity* ✅ (relative to the team, with a caveat): the low-rank factorization line is his own [S001 pp. 2-3; H002 p. 1], and no other minlp-team member's skill works this way. In the wider field, landscape-plus-certificate work on Burer-Monteiro factorizations became a literature of its own, which S048 cites and distinguishes itself from [S048 pp. 5, 28].

**Stop rule**: if the nonconvex method cannot produce a dual estimate during the run, say that no valid bound is available and compare only on the primal side [S006 p. 9; S001 p. 13]. Escapes carry no guarantee: "In fact, although “escapes” were often observed in our experiments, sometimes the algorithm did fail to escape from a non-maximum stable set." [S025 p. 18].

**Limitations**: dormant in the cards between 2007 and 2024, when his relaxations themselves are the bound (M1, M2) [§8]; certificates rest on sufficient conditions [S048 pp. 6, 9]; accuracy is moderate and the tail slow [S014 pp. 2, 17].

**Why a new method and not a variant**: it explains six M1 reverse-direction variants (§3.1) that M1 can only mark as anomalies, and it is distinct from M5 (an ordering of code and theory) and from M3 (a protocol for tightness claims). The skill moves from 5 to 6 core methods, inside the 3-7 range.

No other cluster passed all four checks (§5, §6).

## 5. New heuristics

### 5.1 New

**H11 · Redundant in x, binding in the lift.** Before relaxing, add quadratic equations that are redundant in the original variables but held at their extreme values: squared linear equations, complementarities, binarity, products of KKT stationarity with x. In the lift they are not redundant and often carry exactness.
- Cards: [S004 pp. 4-5, 14] squared equations, "Overall, it seems that the original equation and its squared version are critical for Theorems 2.6 and 3.1."; [S009 pp. 8-9] a quadratic fixed at its extreme value over the linear slice is captured exactly; [S022 pp. 2-3] the same device twice; [S007 p. 9] the objective-equating constraint from the KKT identity; [S008 pp. 8-9] an RLT-linearized x^T(stationarity) = 0 bounds the duals; [S045 pp. 12, 23-24] a redundant complementarity measured by ablation; [S049 pp. 13-14] a complementarity product linearized for exactness at m = 2.
- Checks: recurrence ✅ (7 works, 2008-2025); say-do ✅ [S004 p. 14]; executable ✅; exclusivity ✗ (products of constraints are the standard RLT idea [S016 preprint pp. 5-6]). → heuristic. Links to M1 steps 1-2.

**H12 · Put the optimality conditions into the relaxation and branch finitely on them (2008-2012).** For a global algorithm, write the KKT system, branch on complementarity index sets so the tree is finite, make the node relaxation an SDP/DNN of the lifted KKT system, add a constraint that bounds the multipliers, and define correctness as zero gap at every feasible leaf.
- Cards: [S007 pp. 3, 6, 9-12] "We are unaware of any methods that can verify optimality in a finite number of nodes (using exact arithmetic)."; [S018 pp. 7-10] specialised to the box with multipliers eliminated and correctness re-proved; [S008 pp. 4, 6, 8-10] finite KKT branching instead of spatial branching, attributed to relaxation strength against Couenne, "We attribute the performance differences mainly to the relaxation differences: we use stronger SDP-based relaxations, while Couenne uses weaker LP relaxations." [S008 p. 16]; [S047 p. 20] second-order conditions relaxed, "Relaxing the standard second-order necessary optimality conditions is one of the main theoretical ideas of this paper. This task is non-trivial since it implicitly involves knowledge of the active/inactive constraint set at a general point."; [S020 p. 16] the same tree reused to compare node solvers.
- Checks: recurrence ✅ (5 works, Vandenbussche and Chen lines); say-do ✅ [S007 p. 3; S047 p. 20]; executable ✅; exclusivity partial: KKT branching itself comes from Hansen et al. and Vandenbussche-Nemhauser [S007 p. 3; S018 pp. 1-2]. → heuristic, dated; after about 2013 he aims at a single strong bound rather than a B&B [S049 p. 2].

### 5.2 Existing heuristics: evidence and variant notes

- **H1 (tool chooses the class)**: "More generally, the paper also illustrates that it can be worthwhile to pay for a computationally expensive, but strong, relaxation" [H001 p. 3]; the goal of finding classes where SDP bounds are uniformly good [H001 p. 2]; the conclusion of the 0-1 work names mixed and nonconvex QP as next targets [S013 p. 24].
- **H2 (MILP road map)**: "In this sense, we view (MIQCP) as a natural progression from MILP rather than, say, a special case of MINLP." [S016 p. 2] and its closing concept dictionary [S016 preprint p. 30]; BQP facets and symmetries transferred to box QP with an iff survival test [S011 pp. 7, 11-13].
- **H3 (derive others' cuts as special cases)**: a bound family read by duality as Shor plus one constraint, "The dual of DQPSDC has a surprisingly simple interpretation as a strengthening of the Shor relaxation SQPS." [S034 p. 4]; a cut process collapsed into one constraint, "If α can be expressed as a function of (x, y) then the result is a single nonlinear constraint that is equivalent to a family of lifted tangent inequalities." [S039 p. 6]; "Indeed, our initial motivation for this paper was the desire to understand the inequalities in [9] more fully." [S050 p. 6].
- **H4 (size by variables × cone)**: [S043 p. 5]. Variant: the motivation promises bounds better than SOCP, but the comparison is run against SDP only [S043 pp. 4, 15-18].
- **H5 (baseline protocol)**: evidence: the co-author's previous code first [S008 p. 13; S018 pp. 11-12]. Variant to add: *favour the baseline* when the claim is a trend or a speed-up: exact moments given to the moment-based baseline, "Actually, this choice favors MB, but the goal of our experiments is to demonstrate that our approach provides a valid upper bound" [S044 p. 14]; bounds derived for the big-M competitor and imposed on his own code for fairness [S059 pp. 19, 21-22]; the competitor's starting duals tuned [S013 p. 17]; same-language re-implementation [S031 p. 8]; swap one component and freeze the rest [S020 p. 16]; "This gives a method-specific feasible upper bound; no Gurobi incumbent or point recovered by another method is used to calculate the gap." [S065 p. 12].
- **H6 (bound crossing as alarm)**: no primal value below a dual bound checked across codes [S001 p. 14].
- **H7 (loose inner solves, printed safeguards)**: [S020 p. 11]; "Somewhat surprisingly, computational experiments showed that the dual multipliers converged reasonably well even when the subproblems were solved very loosely by only a few cycles of block coordinate descent." [H001 p. 2]; [S007 p. 16; S018 p. 11; S013 pp. 14-15; S029 p. 22].
- **H8 (print losses)**: [S014 p. 17; S018 p. 14; S020 p. 18; S026 p. 19; S031 pp. 14, 16; S041 p. 25; S043 p. 18; S063 p. 15; S023 p. 20; S056 pp. 13-15; S057 pp. 16, 19-20]. The habit runs from 2001 to 2026.
- **H9 (entry point, scope disclaimer)**: "Hence, our main contribution is a unified presentation of the various results, and we do so from “easiest to hardest” in hopes of gently introducing the reader to the insights provided by copositive optimization." [S024 p. 3]; scope statements [S015 p. 3; S045 p. 4; S027 p. 27; S047 p. 13].
- **H10 (regenerable numbers)**: see §3.2; code public from 2009 [H002 pp. 1-3; S008 p. 11].

## 6. Candidate pool (not promoted)

Counts are distinct cards. *Absorbed* means the cluster became evidence for a method or heuristic above and adds no separate entry.

| Cluster (merged by meaning) | Cards | n | Decision |
|---|---|---|---|
| Dual certificate for a factored reformulation | S014, S017 | 2 | absorbed into Method 6 |
| Valid bound from an inexact first-order solver | S001, S003, S013 | 3 | absorbed into Method 6 |
| Classify local optima, escape saddles | S006, S025 (+S003) | 3 | absorbed into Method 6 |
| Certify the local solver, don't replace it | S048 | 1 | absorbed into Method 6 |
| Quadratic held at its extreme value / redundant constraint for strength / squared equations | S004, S009, S022, S045 (+S007, S008, S049) | 7 | H11 |
| Finite KKT-complementarity branching; relax the optimality conditions | S007, S008, S047 (+S018, S020) | 5 | H12 |
| Fair-comparison handicap; same-language baseline; swap one component; equal-bound timing | S059, S044, S031, S020, S013, S014 | 6 | absorbed into H5 |
| Collapse a cut family or a bound family into one conic constraint | S039, S034, S049, S022 | 4 | absorbed into M2 step 6 and H3 |
| Special cases as incubators; class where the strong relaxation wins | S002, H001 | 2 | absorbed into M2 and H1 |
| Restate prior special cases in your notation | S004 (+S009, S051) | 3 | absorbed into M1 step 4 |
| Perturb, prove, pass to the limit | S021, S023, S019 (+S009, S041) | 5 | technique inventory (P4) |
| Rank-one extreme-ray proof by perturbation | S021, S024, S049 (+S012, S036, S058, S016) | 7 | technique inventory (P1); proof engine of M2 |
| Reuse your own exact representation as a lemma | S010, S016 | 2 | technique inventory (P2) |
| Export the home toolkit into a collaborator's applied problem | S005, S057 (practice in S023, S044, S045, S048, S059, S063) | 2 explicit | pool: no stated rule, not exclusive; recorded under §9 |
| Tightness by perturbation from an LP-exact case | S048 | 1 | pool |
| Leanest relaxation the sign structure allows | S058 | 1 | pool |
| Proof-failure map guides the counterexample | S058 | 1 | pool (M3 step 3 evidence) |
| Refute by joint infeasibility, not by an instance | S061 | 1 | pool |
| Import an exact cone description and pair it with a cheap oracle | S065 (+S040 separation by boundary decomposition) | 2 | pool |
| Rank-2 boundary argument as motivation for a constraint | S065 | 1 | pool |
| Bootstrap separation through the dual cone; self-duality as cut generator | S050 | 1 | pool |
| Artificial-variable sandwich | S049 | 1 | pool (design move D3) |
| Incumbent-as-restriction sandwich | S023 (+S057 sandwiched variants) | 2 | pool |
| Relaxation volume as quality measure and branching rule | S039 | 1 | pool |
| 2×2 factorial ablation as ratios; monotone order with minimal element | S043 | 1 | pool |
| Variable splitting by copies | S013 | 1 | pool (design move D2) |
| Proof under two models of computation | S007 | 1 | pool |
| Specialise by eliminating auxiliary variables, re-prove the key property | S018 | 1 | pool |
| Classify valid inequalities by curvature | S011 | 1 | pool |
| Cross-field pairing to learn the other's field | H001 | 1 | pool (§9) |
| Ship the solver behind a familiar interface | S008 | 1 | pool (H10 evidence) |
| Generalize DNN through extreme rays of K* | S022 | 1 | pool |
| Disclose concurrent equivalent work by date | S023 | 1 | pool (writing move) |
| Explain wins and losses by one instance statistic | S032 | 1 | pool (H8 evidence) |
| Abstract-assumption framework, verify per instance | S051 | 1 | pool |
| Inexactness budget tied to the duality gap | S035 | 1 | pool |
| Decompose a relaxation's excess into a good part plus one bad piece | S028 | 1 | pool |
| Escalating-geometry proof | S041 | 1 | pool |
| Root-equivalent relaxations differ inside B&B | S047 | 1 | pool |
| Diagnose the incumbent's sensitivity, robustify with a nesting budget | S042 | 1 | pool |
| Closed-form low-rank optimum as structural insight | S052 | 1 | pool |
| Validity separated from sufficiency | S027 | 1 | pool |
| Analogy across areas | S036 | 1 | pool |
| Model the practice as it is; calibrate a stylized model; comparative statics by projection | S015, S046, S053 | 3 | pool: applied-economics papers, outside the field |
| Cross-evaluation of solutions; synthetic instances from real data; scenario-bunch bounds; threshold node selection | S062, S059 | 2 | pool |

## 7. Technique inventory

### 7.1 Proof devices

- **P1 Pataki rank bound + rank-one perturbation of an extreme point/ray** (the hull-proof engine): [S001 p. 5; S012 preprint pp. 5, 7; S016 preprint pp. 11-12; S021 pp. 6-10; S024 pp. 13-14, 19-21; S036 pp. 4, 12; S049 pp. 20-24; S058 pp. 9-12; S065 p. 10]. The 2015 survey's half-space lemma is reused in 2025 [S049 p. 22].
- **P2 Completely positive decomposition with the Cauchy-Schwarz equality case; DNN = CP in small dimension**: [S004 p. 5; S009 pp. 4-5; S010 pp. 5-7; S016 preprint p. 9; S024 p. 7; S038 p. 4; S058 p. 11; S067 p. 5].
- **P3 Recession-cone arguments for boundedness and exactness**: [S004 p. 7; S007 p. 10; S008 p. 10; S016 preprint p. 10; S009 p. 4].
- **P4 Perturb (or tighten), prove, pass to the limit**: [S009 p. 4; S019 pp. 9-17; S021 p. 11; S023 p. 16; S041 pp. 16-20].
- **P5 Dual certificate from stationarity multipliers**: [S014 p. 8; S017 p. 19; S001 p. 7; S003 pp. 13-14; S023 pp. 26-29; S048 pp. 17-20].
- **P6 Explicit small counterexample at the boundary dimension**: [S006 p. 7 (K3); S025 p. 13 (pentagon); S010 p. 8; S011 p. 16; S012 preprint p. 13; S034 p. 6; S036 pp. 8-10; S048 pp. 39-41; S058 pp. 13-14, 43; S065 p. 16].
- **P7 A redundant bound or ball to obtain Slater points or compactness**: [S019 p. 13; S023 pp. 7-8; S044 p. 12; S048 pp. 21-22; S030 p. 5].
- **P8 Schur complements and principal minors to force entries or rank**: [S018 pp. 9-10; S012 preprint p. 6; S021 pp. 9-10; S019 p. 7; S038 pp. 10-18; S040 pp. 8-9; S055 p. 4].
- **P9 Convergence by telescoping or by an exact perturbed problem**: [S013 pp. 10-11; S035 pp. 7, 10-11].

### 7.2 Design moves

- **D1 Change of variables that removes a cone** (factor, Cholesky elimination): [S014 pp. 5-8; S017 pp. 6-9; S001 pp. 3, 5; S030 pp. 6-7].
- **D2 Split by copy variables so the cone and the coupling sit in separate blocks**: [S013 pp. 4-5, 12]; null-space parametrization of the DNN set [S020 pp. 6-8].
- **D3 Sandwich an auxiliary scalar to turn many cones into one cone plus linear constraints**: [S049 pp. 3, 11-12, 18-19]; one-coordinate lift of a ball to a sphere [S022 p. 2].
- **D4 Multiply a valid SOC constraint by a linear slack and linearize (SOC-RLT)**: [S016 preprint pp. 5-6; S021 p. 6; S067 p. 4].
- **D5 Lift each column separately and couple through the sum**: [S048 pp. 3, 39]; Kronecker product of redundant LMIs [S055 pp. 5-6].
- **D6 Separation oracle in place of an explicit description**: [S012 preprint p. 15; S040 pp. 9-14; S065 pp. 4-8].

### 7.3 Experiment and evaluation protocols

- **E1 Same accuracy target or the same bound for every method**: [S014 p. 14; S020 p. 12]; surpass-time columns [S013 p. 18]; time-matched truncation [S001 p. 26]; equal time caps when nothing finishes [S031 p. 14].
- **E2 Favour the baseline** (§5.2 H5): [S044 p. 14; S059 pp. 19, 21-22; S013 p. 17; S031 p. 8].
- **E3 Swap one component, freeze the rest; factorial ablations**: [S020 p. 16; S043 pp. 15-16; S045 pp. 23-24].
- **E4 Report by joint outcome**: by joint solve status [S049 p. 17]; certified / not tight / local outcomes [S048 p. 13]; solutions cross-evaluated on each other's objectives [S062 pp. 6-8].
- **E5 Cross-verification of "solved"**: primal-dual difference columns [S001 pp. 14, 17]; independent algorithms to six figures [S059 p. 15].
- **E6 Accuracy at two levels to show where a first-order method stops paying**: [S014 pp. 15-17].
- **E7 Instances generated from real data without using the data itself**: [S062 p. 6].

### 7.4 Writing moves

- **W1 Numbered conclusions or goals up front, negative ones included**: [S014 p. 3; S020 p. 5; S026 pp. 3-4; S007 p. 4; S049 p. 2].
- **W2 Announce the negative result next to the positive one**: "In Sect. 4, we prove the surprising, somewhat negative result that all three achieve the same optimal value." [S047 p. 2]; [S010 p. 3; S041 p. 23; S063 p. 15]; "weaker" in the title [S043 p. 2].
- **W3 Grade every claim by its level** (we believe, conjecture, empirically, very likely): "This conjecture is supported by extensive numerical computations but remains unproved." [S038 p. 3]; [S020 pp. 13-14; S039 pp. 4, 14; S050 pp. 25-26; S055 p. 7; S065 pp. 10, 14, 16].
- **W4 Easiest to hardest, simple case first, picture first**: [S017 p. 6; S024 p. 3; S043 pp. 4-6; S039 §§3-4, pp. 7-25; S067 p. 3; S049 pp. 3, 13-14].
- **W5 Warn about notation**: "This paper is heavy in notation." [S017 p. 3]; [S008 p. 6; S024 p. 3; S049 p. 5].
- **W6 Scope disclaimer**: "We claim neither that these are the only mechanisms possible nor that they are in every sense optimal." [S015 p. 3]; "In this sense, we cannot claim that optimizing the masked spectral bound is the “silver bullet” for solving extremely large and difficult instances." [S031 p. 14].
- **W7 Credit finders and contributors by name**: [S004 p. 17; S019 pp. 17-18; S061 p. 1; S048 p. 15; S058 p. 46; S049 p. 24; S042 p. 13].
- **W8 End with open questions**: [S004 pp. 16-17; S011 p. 16; S029 p. 33; S037 pp. 24-25; S049 p. 24; S067 p. 6].
- A neutral general lesson from the reading notes (not about any one work): in long computational papers, recheck that table captions, totals and text agree after each revision.

## 8. Trajectory as seen in the full texts

| Period | Works carded | Main topics (cards) |
|---|---|---|
| 2000-04 | 11 | SDP algorithms by change of variables: projected gradient on a factor, rank-two max-cut, Cholesky elimination, rank-one/two stable set, low-rank SDPLR, partial matrices, long-step framework [S014, S006, S017, S025, S030, S001, S029, S032, S051] |
| 2005-09 | 17 | Low-rank theory and enhancements [S003, S026, S031, H002]; lift-and-project bounds for 0-1 IP [S013, S041]; finite SDP B&B for QP [S007, S018]; copositive representation and CP/DNN [S004, S034, S028]; box-QP polyhedra [S011]; applied (ensembles, seed supply chain) [S005, S054, S015] |
| 2010-14 | 18 | CP/DNN computation and QuadprogBB [S020, S008, S047, H001]; hulls, cones and TRS with cuts [S010, S009, S022, S040, S037, S012]; MIQCP framing and survey [S016, S002]; "middle way" relaxations [S043]; analytics side papers [S042, S052, S053, S060, S063] |
| 2015-19 | 12 | TRS and quadratic hulls with Yang and Kılınç-Karzan [S021, S024, S033, S027, S036]; copositive robust/DRO and statistics with Xu [S045, S023, S044, S059]; applied [S046, S062] |
| 2020-24 | 7 | SDP exactness and its correction [S019, S061]; hulls of switching and bounded products [S038, S039, S067]; strengthened SDPs (OPF substructure, Stiefel) [S050, S055] |
| 2025-26 | 6 | Ball constraints, TTRS, Lorentz-positive cone [S049, S065]; submodular QP [S058]; Stiefel certificate [S048]; constraint learning and trained networks [S057, S056] |

**Turns visible in the texts**:
1. From algorithms for convex SDP to bounds for nonconvex and integer problems, about 2005-06: the 0-1 paper names mixed binary-continuous and nonconvex QP as next targets [S013 p. 24]; the award note describes the shift away from IPs [H001 p. 2].
2. From finite B&B solvers to a single strong relaxation, about 2013: the KKT B&B line runs 2008-2012 [S007, S018, S008, S047]; later papers set B&B aside for a relaxation strong irrespective of the data, "In this paper, however, we seek a relaxation that is strong irrespective of the data." [S049 p. 2].
3. Applied and analytics papers with Iowa colleagues and students 2012-2019 [S042, S052, S053, S060, S046, S045, S023, S044, S059, S062].
4. ML-adjacent work with students and colleagues from 2025 [S048, S057, S056].

**What stayed constant**: the lifted matrix [1 xᵀ; x X] from the ensemble-pruning SDP [S005 pp. 7-8] to the Lorentz cone [S065 pp. 2-7]; the Pataki rank bound from 2003 [S001 p. 5] to 2026 [S065 p. 10]; losses printed with a hypothesis from 2001 [S014 p. 17] to 2026 [S056 pp. 13-15]; claims graded by level from 2002 [S025 pp. 17-18] to 2026 [S065 pp. 10, 14, 16]; finders named [W7].

## 9. Collaboration pattern

- **Thesis era**: Monteiro co-authors 8 of the 11 carded works of 2000-04 [S014, S006, S017, S025, S030, S001, S032, S051 card headers] and advised the thesis [S070]; Yin Zhang co-authors 5 [S006, S017, S025, S030, S032].
- **Long partner**: Kurt Anstreicher on 8 co-authored works, 2005-2026 (d.c. vs copositive bounds, 5×5 DNN vs CP, small hulls, TRS with cuts, hollows, switching, bounded products, Lorentz cone) [S034, S028, S010, S012, S036, S038, S039, S065], plus the observation behind the 2025 main theorem [S049 p. 24] and a conjecture credited in 2009 [S011 p. 14].
- **Students as co-authors** (ids from card headers): Chen [S041, S047, S008, S060], Choi [S026, H002, S063], Dong [S022, S040], Yang [S021, S033, S036, S067], Xu [S045, S059, S023, S044], Park [S039, S055], Zhu [S057, S056]. Student lines tend to carry the toolkit into a new domain: robust and distributionally robust bounds and statistics with Xu, constraint learning with Zhu [§6 export cluster].
- **Sole-authored**: the copositive representation, its handbook chapter, OptDNN, the gentle introduction, the slight lift, the partial-matrix method and the football rankings [S004, S009, S020, S024, S049, S029, S042]. The founding theory of the CP line is sole-authored; its computation and solver went to a student [S008 card header].
- **Cross-field partners**: integer programming, a pairing the award note explains by each author's wish to understand the other's field [H001 pp. 1, 3]; polyhedral combinatorics with Letchford [S011, S002, S037]; Kim and Kojima [S043]; Ye [S019, S061]; Kılınç-Karzan [S027]; Natarajan and Willemsen [S058]; Gilman and Balzano (EECS) [S048]; Serra and Tong (ML) [S056]; Iowa business colleagues on applied models [S015, S052, S053, S046].
- **Frequencies by period** (co-authors appearing in ≥2 carded works of the period): 2000-04 Monteiro 8 (plus the thesis), Zhang 5; 2005-09 Vandenbussche 3, Monteiro 2, Anstreicher 2, Choi 2, Street 2, Yi Zhang 2; 2010-14 Chen 3, Anstreicher 2, Letchford 2, Dong 2; 2015-19 Xu 4, Yang 3; 2020-24 Ye 2, Anstreicher 2, Park 2; 2025-26 Zhu 2 (Anstreicher co-authors one and is thanked for the key observation of another [S065; S049 p. 24]).

## 10. Rejected updates

1. A separate method for fair-comparison engineering (S059, S044, S031, S020, S013, S014): H5 already covers baselines; added as an H5 variant only.
2. A heuristic for perturb-and-limit proofs (S021, S023, S019): a standard device, no executable difference from practice; kept in the technique inventory.
3. A method for the rank-one extreme-ray engine (S021, S024, S049 and others): it is how M2 proves hulls; a new method would duplicate M2.
4. A method or heuristic for exporting the toolkit into applied problems (S005, S057 and practice cards): no stated rule, not exclusive; a trajectory and collaboration fact (§8, §9).
5. *Special cases as incubators* (S002, H001): restates M2 and H1.
6. *Collapse a family into one conic constraint* (S039, S034, S049, S022): M2 step 6 plus H3 already explain it.
7. New writing heuristics (numbered conclusions, easiest-to-hardest, notation warnings): H9 and Workflow E already cover them; kept in §7.4.
8. Experiment-protocol details (surpass time, equal-bound timing, joint-status tables) as heuristics: useful detail for Workflow C, no new explanatory power; kept in §7.3.
9. Single-card candidates in §6 marked *pool*: below the ≥3-work threshold.
10. Reading-note inconsistencies inside individual works (counts in captions, typos, values that differ between pages): not findings about the researcher; not carried into SKILL.md (one neutral lesson in §7.4).

## 11. Open gaps

- **No open text**: the NSF CAREER and collaborative awards (abstract only) [S068; S069]; the 2001 thesis, where the factorization ideas started, not read [S070]; the 2017 editorial [D001].
- **Versions**: published versions of S012, S016, S019, S048, S049 and S058 not read (card headers); the SKILL.md quotes from arXiv v1 of the ball-constraint paper are not in the corpus [S049 pp. 10, 15]; v1 and v2 of the submodular paper, which carry the polynomial-time claim and its narrowing according to SKILL.md, are not in the corpus, so that story rests on web research [S058 card header].
- **Correction residue**: whether arXiv 1802.02688 was updated after the 2021 correction is not checked by any card [S061 c3-01 card, Method links]; the content of the earlier error in the 2009 CP paper credited to Bomze is not in the text [S004 p. 17].
- **Authorship shares**: who did what in multi-author applied and ML papers is not stated [S048 card header; S056 Method links; S005 card header].
- **Supplement depth**: 15 works were read in part; some proof details (Rellich-type perturbation in S027 p. 14) and reference lists were not read.
- **Reasons for turns**: no full text states why he left the low-rank algorithm line (about 2007), the KKT B&B line (about 2012) or robust optimization (2019); §8 records dates only.
- **Method 6 dormancy**: no card between 2007 and 2024 applies the certificate pattern; whether unread works of that window do is unknown.

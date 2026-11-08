# Santanu S. Dey · Evidence ledger

> Date: 2026-10-10 (stage T3.6, first synthesis round). The full evidence behind `SKILL.md`. SKILL.md keeps, per item, the strongest statement and cards, a one-line say–do count, at most four variant/correction bullets, and a pointer to the matching section here. Each section below has up to three parts: **Full-text evidence** (from the paper cards, mostly copied from `08-deep-reading-synthesis.md`, which is traceable to `cards/`), **Added in T3.6** (anything new written for this pass, with card ids), and **Before T3.6** (the SKILL.md item as it stood before this pass, built from web research, moved here **verbatim** so nothing is lost; its `[02 §1.1]`-style citations point to the web-research notes `01-…06-*.md` in this folder).

**How to read.** `[S012 p. 9]` is paper card S012 in `07-paper-cards.md`, at the page of the version named on the card (usually arXiv or an author preprint; check the journal page before citing it in a paper). Abstract- and metadata-level cards are cited without pages. Seven pairs are two versions of one work and count once: S031 = D003, S084 → S028, S096 = S095, D001 = S025, S135 = S085, S097 = S104, D004 = S067 [08 §1]. Per-card method links (✅ evidence, ⚠ variant, ✗ contradiction) are in the `Methods linked` column of `07-paper-cards.md`; named proof devices, design moves, experiment protocols and writing moves are in `../technique-catalog.md`. Cards that record typos or internal inconsistencies of a paper are reading notes and are not used here.

**Scope.** Sections exist for the SKILL.md items that were condensed or changed: the two taste lists, Methods 1–6, Heuristics 1–11, the seven signature-work anatomies, the anti-patterns table, the research trajectory, the academic lineage, the inner tensions, the mentor voice, the corrections, the secondary sources and the card key. Items not listed (frontmatter, How to Use, activation rules, integrity rules, routing, agentic protocol, workflows, roundtable card, sources) are complete in SKILL.md.

## Contents

- [Taste: marks of good research](#taste-marks)
- [Taste: warning signs of bad research](#taste-warnings)
- [Method 1](#method-1)
- [Method 2](#method-2)
- [Method 3](#method-3)
- [Method 4](#method-4)
- [Method 5](#method-5)
- [Method 6](#method-6)
- [Heuristic 1](#heuristic-1)
- [Heuristic 2](#heuristic-2)
- [Heuristic 3](#heuristic-3)
- [Heuristic 4](#heuristic-4)
- [Heuristic 5](#heuristic-5)
- [Heuristic 6](#heuristic-6)
- [Heuristic 7](#heuristic-7)
- [Heuristic 8](#heuristic-8)
- [Heuristic 9](#heuristic-9)
- [Heuristic 10 (re-prove the classical lemma)](#heuristic-10)
- [Folded: design the cut first (now a Method 3 variant)](#folded-design-cut)
- [Anatomy: sparse-cuts](#anatomy-sparse-cuts)
- [Anatomy: pooling](#anatomy-pooling)
- [Anatomy: opf](#anatomy-opf)
- [Anatomy: qcqp](#anatomy-qcqp)
- [Anatomy: branching](#anatomy-branching)
- [Anatomy: miqp-np](#anatomy-miqp-np)
- [Anatomy: mbqp-sensitivity](#anatomy-mbqp-sensitivity)
- [Research anti-patterns](#anti-patterns)
- [Research trajectory](#trajectory)
- [Academic lineage](#academic-lineage)
- [Inner tensions](#inner-tensions)
- [Mentor voice](#mentor-voice)
- [Corrections from the full texts](#corrections)
- [Secondary sources](#sources-secondary)
- [Card key](#card-key)

<a id="taste-marks"></a>

## Taste: marks of good research

### Added in T3.6

New card evidence written into SKILL.md's five marks (each line names the mark):

1. **Explains why practice works.** The sparse-cut paper opens on the missing theory: "Surprisingly, very few studies have been conducted on the topic of sparse cutting-planes." [S084 p. 1]. Pooling: PL MILP relaxations give good bounds, yet "no formal result regarding the quality of these relaxations is known" [S014 p. 1]. Strong branching: "However, to the best of our knowledge there is no understanding of how good strong-branching is in absolute terms." [S020 p. 3]. Dual decomposition: worst-case guarantees "fail to explain the strong performance observed in practice" [S120 p. 1].
2. **Tight, data-independent, demarcated.** "The above examples serve to highlight the fact that the result of Theorem 1 (a feasible system of inequalities with exactly one quadratic inequality always has at least one integer feasible solution of small size) is tight with respect to the number of quadratic inequalities." [S003 p. 3]; "We also show, via examples, that this result provides a reasonable demarcation of conditions that allow obtaining the convex hull of quadratic constraints via aggregated constraints." [S071 p. 2]; "In order to simplify the question, we arrive at a data independent version of it" [S035 p. 1]. **Nuance (08 §3 row 14):** a 2020 paper sells a data-dependent grouping against earlier bounds: "However, these bounds are entirely data-independent." [S040 p. 5]; early relaxation-strength bounds are data-dependent [S010 pp. 9–10, 13]. Data independence is a taste for theorems, not for algorithms that must use the data.
3. **Certificate, not only a solution.** "Most conventional methods for solving SPCA are heuristics with no guarantees such as certificates of optimality on the solution-quality via associated dual bounds." [S017 p. 1]; the OPF certified gap at 3375 buses with hardware named [S001 pp. 1, 26–29]; the same complaint for model-free SPCA [S083 p. 1], structural model updating [S060 p. 27], network design [S111 p. 2] and grid security [S058 p. 1].
4. **Tractable beats beautiful.** "we would like to obtain an outer approximation of the original set that can mimic the strength of the SDP relaxation, but that is lightweight and linear." [S048 p. 3]; "Our assessment is that the lifted representations, while theoretically interesting, do not provide an off-the-shelf practical approach for this problem as they are too large and not sufficiently strong." [S100 p. 12]; the stated aim "to avoid using SDP relaxations" in OPF [S001 p. 14].
5. **Sparse, structured instances.** Interaction graphs and chromatic numbers as instance parameters [S024 pp. 5–9, 12–13]; block decomposability in the feasibility-pump analysis [S061 pp. 3, 12]; tree decompositions of the intersection graph make a general MIP dual decomposable [S104 pp. 2, 9]; "Overall, our results suggest that progress in strengthening SDP relaxations for QCQPs is more likely to come from identifying and exploiting sparse, well-structured inequalities rather than from pursuing increasingly dense eigenvector-based cuts." [S122 p. 22]; generators with sparse graphs because real instances are sparse [S014 pp. 33–35].

### Full-text evidence

- **Taste 5 (sparsity as structure)**: interaction graphs and chromatic numbers as instance parameters [S024 pp. 5–9, 12–13]; block decomposability carried into the feasibility-pump analysis [S061 pp. 3, 12]; tree decompositions of the intersection graph make a general MIP dual decomposable [S104 pp. 2, 9]; the closing advice of the eigenvector-cut paper: "Overall, our results suggest that progress in strengthening SDP relaxations for QCQPs is more likely to come from identifying and exploiting sparse, well-structured inequalities rather than from pursuing increasingly dense eigenvector-based cuts." [S122 p. 22].

| # | SKILL.md item | What the full texts show | Cards | Decision |
|---|---|---|---|---|
| 14 | Taste 2 (data-independent bounds) | Supported [S035 p. 1; S024 pp. 5–9; S079 pp. 3, 5], but a 2020 paper sells a data-dependent grouping against the authors' own earlier bounds: "However, these bounds are entirely data-independent." [S040 p. 5]; early relaxation-strength bounds are data-dependent [S010 pp. 9–10, 13]. | as cited | **Add a nuance**: data independence is a taste for theorems, not for algorithms that must use the data. |

### Before T3.6 (moved verbatim)

1. **It explains why something that works in practice works.** R1, 14 occasions [02 §1.1]; "Why do these MILP relaxations work so well?" (pooling) [01 §2.2]; "Almost 60 years now, but there is very little theoretical analysis of the branch-and-bound algorithm!" [06 T8].
2. **A good theorem is tight, data-independent and shows its own boundary.** "these bounds are completely data independent" (arXiv:1601.00198) [02 §1.3]; MIQP in NP, tight in the number of quadratics [01 §2.3]; "a reasonable demarcation of conditions" (doi:10.1137/21M1428583) [01 §2.5].
3. **A result comes with a certificate, not only a good solution.** R4 [02 §1.2]; sparse PCA paper retitled to name "dual bounds" [03 §4.2]; OPF gap certified "within 0.13% of global optimality" (arXiv:1504.06770) [01 §2.1].
4. **Tractable beats beautiful: LP and SOCP before SDP and hierarchies.** "Usually, we will stick to linear programming (LP) or second order cone representable (SOCr) convex functions and sets for our convex relaxations." (IPCO 2020 slides, p. 15) [02 §1.4]. Nuance: sum-of-squares "also works in practice" for some power classes [02 C8].
5. **Real instances are sparse and structured; study that structure.** R2, 11 occasions [02 §0]; generators "Inspired by the classical paper [7] and by the fact most instances in practice are sparse" [03 §3.1].

<a id="taste-warnings"></a>

## Taste: warning signs of bad research

### Added in T3.6

1. **Unverifiable data assumptions / no certificate.** The talk quote stays (web research, [02 §1.2]); card evidence of the same complaint: [S017 p. 1; S060 p. 27; S111 p. 2; S083 p. 1].
2. **Yardstick that does not track usefulness.** "We discard this ratio, since this ratio can become infinity and not provide any useful information." [S028 p. 2] (the pre-T3.6 SKILL.md quoted this sentence with "infinite", from note 01; both preprint texts read "infinity" [S084 p. 2; S028 p. 2]); depth of cut: its correlation with the change in tree size was weak [S081 p. 9]; facetness questioned because extreme inequalities are dense among minimal ones, and depth of cut can rank a dominated cut higher [S011 pp. 7–8]; "greater expressive power does not necessarily translate into a better algorithm." [S117 p. 32]. Dates: his own 2010 papers still used extremality and a merit index as strength yardsticks [S019 pp. 6, 20]; the doubt is from 2018 on [S011 pp. 7–8]; a 2026 paper uses depth as its proxy measure and still concludes for sparse structured cuts [S122 pp. 4, 12–14, 22].
3. **Claims that would not survive the real solver.** "one kind of cutting-plane selection improves the average solution time in the context of one code and miserably fails in conjunction with other codes!" [S011 p. 21]; "However, when accounting for the time required to collect the cuts, most positive instances become negative, which motivates our learning approach." [S082 p. 9].

### Full-text evidence

| # | SKILL.md item | What the full texts show | Cards | Decision |
|---|---|---|---|---|
| 15 | Anti-pattern "facetness or depth of cut as proxies for usefulness" | 2010 papers still use extremality and a merit index as strength yardsticks [S019 pp. 6, 20]. A 2026 paper uses depth as its proxy measure [S122 pp. 4, 12–14] and still concludes for sparse structured cuts [S122 p. 22]; another finds the richest encoding family worst in practice: "greater expressive power does not necessarily translate into a better algorithm." [S117 p. 32]. | as cited | Keep the anti-pattern; **add the dates** (facet yardsticks before 2011, doubt from 2018) and S117 as practice evidence. |

### Before T3.6 (moved verbatim)

1. **Guarantees resting on unverifiable data assumptions.** "Heuristics do not come with certificates. ... conditions under which (some of) these computationally friendlier methods can be shown to "work well", make very strong and often unverifiable assumptions on the problem data." (2019 sparse PCA talk, p. 4) [02 §1.2]
2. **A yardstick that does not track usefulness** (ill-defined ratios, facetness, depth of cut, worst case alone). "We discard this ratio, since this ratio can become infinite and not provide any useful information" [01 §2.4]; "casts doubts on whether being a facet-defining inequality is really useful" (2018) [02 §1.5].
3. **A computational claim that would not survive the real solver.** "one kind of cutting-plane selection improves the average solution time in the context of one code and miserably fails in conjunction with other codes!" (2018) [02 §4.2]; overhead that "completely nullifies" a speed-up (arXiv:2411.15090) [02 §4.3].

<a id="method-1"></a>

## Method 1: Turn an unexplained solver practice into a proxy theorem

### Full-text evidence (08 §2)

- **Strongest practice**: the sparse-cut line runs the whole loop: solver habit, missing theory, a one-sided geometric proxy, a measure fixed first, the result read back as a justification of practice [S084 pp. 1–2, 4; S028 pp. 1–3, 5]. The measure is chosen by discarding one that "can become infinity" [S028 p. 2]. The return to data is stated as "sparse cuts usually perform much better than the worst-case bounds we obtain theoretically" [S024 p. 4]. Pooling: unexplained PL MILP relaxations → tight factor-n theorem → practice beats the bound → MILP restriction built from the proof [S014 pp. 1, 5–6, 14–16, 28]. Branch and bound: random instances because the worst case is exponential, with "an indication" as the stated reach [S031 pp. 1–3; D003 pp. 1–3]; strong branching measured "in absolute terms" [S020 pp. 3–5]; a solver regularity (cuts enlarging trees) made into a provable property after removing confounders [S081 pp. 2, 9, 12–13]; dual decomposition on random two-stage instances [S120 pp. 1–4]; pre-specified sparse splits [S118 pp. 2–4]; feasibility-pump randomisation [S061 pp. 1–3]; sparse SDP bounds [S035 pp. 1–3; S122 pp. 4, 12–14, 21]; the default bilinear relaxation of spatial branch and bound [S021 pp. 1–2]; the ℓ1 surrogate for sparse PCA [S088 pp. 1–3].
- **Stated in the texts**: "given the complexity of solvers one cannot expect to be able to perform a theoretical analysis of this performance metric directly, and thus proxy measures are required." [S011 p. 4]; "In order to avoid worst-case lower bounds, a standard idea is to consider random instances." [S031 p. 2]; "existing theoretical guarantees are almost exclusively based on worst-case analyses, which predict exponential convergence behavior in the problem dimension and fail to explain the strong performance observed in practice." (from the sentence at [S120 p. 1]); "In order to simplify the question, we arrive at a data independent version of it" [S035 p. 1]. The NSF Sparse IP award names three solver habits to explain [S138].
- **Say–do update**: ✅, now on 24 full or partial works from 2014 to 2026. The report-the-mismatch form of step 7 is in the texts: "these results have so far failed to directly help in actual cutting-plane selection." [S011 p. 20]; practice beats the guarantee [S014 p. 28; S024 p. 4]. The step-8 limitation in SKILL.md needs correcting (§3 row 1).

### Variants and contradictions (08 §3)

| # | SKILL.md item | What the full texts show | Cards | Decision |
|---|---|---|---|---|
| 1 | M1 limitation: "Step 8 rarely closed: rule proposals sit in unpublished preprints" | Step 8 is closed in two published works: the MILP restriction built from the pooling proof (Oper. Res. 2015) and a randomisation rule implemented in Feasibility Pump 2.0 and recommended for FP codes after the analysed version lost (SIAM J. Optim. 2018). The branching rules of 2025 and the GMIC heuristic of 2024 are preprints. | [S014 pp. 14–16; S061 pp. 12–13; S130 pp. 8, 20; S082 p. 6; S081 pp. 12–13] | **Revise** the limitation: "Step 8 closed in published form twice (pooling restriction 2015, feasibility-pump rule 2018); the ML-facing rules of 2024–25 are preprints." |
| 2 | M1 as the entry point | 23 works link to M1 only as a variant: the question comes from a named open question [S021 p. 1], a classical lemma's standing [S125 pp. 1–2], completeness of a cut technique [S071 p. 1], the authors' own relaxation [S129 pp. 14–17], a theoretical preprocessing technique [D005 pp. 1–2], a classical rank measure [S099 pp. 1–2], or a new paradigm rather than an explanation [S096 p. 2; S095 p. 1]. | as cited | **Add a scope sentence** to M1: it is the main entry, not the only one. Named open questions go to the candidate pool (§6). |
| 3 | M1 step 3 (strip to a proxy) | The texts also climb back: drop features, then re-add one at a time and ask which theorem survives [S079 pp. 5–8; S013 pp. 3, 8; S016 pp. 1–2]; the sparse-cut proxy is pushed toward realism by "four numbered questions" each restoring one feature of solver practice [S065 pp. 1–2]. | [S079; S013; S016; S065] | **Variant note** on M1 between steps 6 and 7: "restore one realism at a time (LP relaxation, dense cuts, rotation, objective) before claiming practice is explained." |

### Added in T3.6

- **Condensed into SKILL.md**: Stated [S011 p. 4]; Practice [S084 pp. 1–5; S014 pp. 1, 5–6, 14–16, 28; S020 pp. 3–5; S081 pp. 2, 9, 12–13; S120 pp. 1–4]; say–do counts from 08 §2 (28 cards, 26 works as evidence, 24 read in full or in part; 23 works as variants; 0 contradictions).
- **Step 3 additions**: the k-PSD closure as a data-independent proxy [S035 p. 1]; random instances to avoid worst-case lower bounds: "In order to avoid worst-case lower bounds, a standard idea is to consider random instances." [S031 p. 2]; control-then-define: dual degeneracy and node selection are removed before monotonicity is defined [S081 p. 2].
- **Step 4**: the measure fixed first, ratio discarded [S028 p. 2; S084 p. 2].
- **Step 5**: worst-case results "only provide a coarse indication" of strength [S011 p. 10]; a parameterised bound for an exponential-worst-case rule: "A common way to meaningfully analyze an algorithm with exponential worst-case performance is to show its performance with respect to some parameter" [S020 p. 5].
- **Step 7**: practical reach stated as "an indication" [S031 p. 1; D003 pp. 1, 3; S118 p. 4]; practice beats the guarantee: "If we view the performance of the MILP based restriction of the pooling problem proposed in this paper on its own, we observe that the quality of solutions that are produced by MILP are significantly better than the theoretical performance guarantee of n." [S014 p. 28].
- **Step 8**: the feasible point built in the upper-bound proof read as an algorithm and enlarged to an MILP restriction that inherits the guarantee [S014 pp. 6, 12, 14–16]; the feasibility-pump randomisation rule implemented and recommended after the analysed version lost [S061 pp. 12–13]; preprint rules [S130 pp. 2, 8, 20; S082 p. 6]: "one of the motivations for this paper is to discover simple rules that can improve over FSB, which can then be used as expert for machine learning algorithms to imitate." [S130 p. 2].
- **Limitations**: solver-specific habits are poor targets; the 2018 review warns that a selection rule can help in one code and fail in another [S011 p. 21].

### Before T3.6 (moved verbatim)

**One line**: When solvers do something that works and nobody can say why, make that habit the object of study; shrink the question until it is provable, prove it tightly, then say how much of practice it explains.

**Evidence**:
- Stated: R1 (14 occasions, 2013-2024), R6 (5 projects) [02 §1.1, §3.2]; the proxy-measure sentence at the top; "We wanted a measure that is well-defined in all cases" (2014 sparse-cut talk, p. 19) [02 §1.3].
- Practice: pooling relaxations 2013-15, sparse cuts 2014-18, feasibility pump 2017, B&B on random instances 2020-23, strong branching 2024, dual decomposition 2026 (arXiv:2604.23383) [01 §2.2, §2.4; 06 T7, T8].
- Say–do consistency: ✅ stated + practised. The final step (a better solver rule) is weak: 2024 slide "How do solvers select cuts to use?" / "I do not know." [02 §1.1].

**Steps**:
1. Pick the habit (sparse-cut filtering, piecewise-linear MILP relaxations for pooling, aggregation cuts, strong branching); write down the empirical evidence and the missing theory.
2. State the real question and why it is out of reach (solver complexity, competing objectives).
3. Strip it to a proxy: drop the optimization, keep one side of the trade-off, or replace the solver by a geometric object (gap closed by sparse cuts; distance of the k-PSD closure from the PSD cone; tree size on random instances).
4. Fix the measure first: well defined in every case and, where possible, data-independent; discard measures that can become infinite.
5. Choose the instance model: worst case if it gives tight results; random or structured instances (sparsity pattern) if worst case is exponential or "coarse" [02 §5.1].
6. Prove it tightly (→ Method 4).
7. Return to data and say how much is explained; if nothing, report that ("i could not complete the whole cycle", Tutte 2020 [02 §5.2]).
8. Only then propose a rule built from the theorem (the MILP restriction attaining the pooling bound [01 §2.2]).

**Different from standard practice**: theory usually analyses a designed algorithm; this starts from an engineering habit inside a solver and seeks the smallest provable question capturing it.

**Limitations**: needs a settled empirical regularity; habits that differ by solver or version are poor targets [02 §4.2]. Step 8 rarely closed: rule proposals sit in unpublished preprints (arXiv:2507.09455, arXiv:2411.15090). Stop rule: if the proxy result does not match practice, report that as the finding; do not sell it as solver guidance.

### SKILL.md Evidence block before the T3.6 review fixes (moved verbatim)

**Evidence** (full evidence: references/research/09-evidence-ledger.md#method-1):
- Stated: "given the complexity of solvers one cannot expect to be able to perform a theoretical analysis of this performance metric directly, and thus proxy measures are required." [S011 p. 4]
- Practice: sparse cuts [S084 pp. 1–5]; pooling relaxations [S014 pp. 1, 5–6, 14–16, 28]; strong branching [S020 pp. 3–5]; cuts that enlarge trees [S081 pp. 2, 9, 12–13]; dual decomposition [S120 pp. 1–4].
- Say–do: ✅ stated + practised; full texts: 26 works as evidence (24 read in full or in part, 2014–2026), 23 as variants, 0 contradictions.
- Variants/corrections:
  - ⚠ Step 8 closed in published form twice: the pooling MILP restriction [S014 pp. 14–16], a feasibility-pump rule [S061 pp. 12–13]; the 2024–25 rules are preprints [S130 pp. 8, 20].
  - ⚠ Main entry, not the only one: also named open questions [S021 p. 1] and classical lemmas [S125 pp. 1–2].
  - ⚠ Before step 7, restore one realism at a time (LP relaxation, dense cuts, rotation, objective) [S065 pp. 1–2; S079 pp. 5–8].
  - ⚠ Step 7 in its report-the-mismatch form: "these results have so far failed to directly help in actual cutting-plane selection." [S011 p. 20]; practice beats the guarantee [S014 p. 28; S024 p. 4].

<a id="method-2"></a>

## Method 2: Measure against ground truth inside a stripped-down instrument

### Full-text evidence (08 §2)

- **Strongest practice**: DP-optimal trees up to 20 binaries, ratio reporting and a word of caution [S020 pp. 11–13, 21–22]; a naive B&B with full strong branching as an oracle for fair node counting, stripped SCIP with the optimal value and seeds, instance ladder from random families to filtered MIPLIB [S081 pp. 8–11; S130 pp. 3–4, 23]; a textbook B&B where only the branching rule varies, optimal primal value given [S098 pp. 5, 8–10]; an expert ceiling evaluated first, with "However, when accounting for the time required to collect the cuts, most positive instances become negative, which motivates our learning approach." [S082 p. 9]; exhaustive enumeration as ceiling for cut generation [S048 pp. 9–12, 15]; facet enumeration of BQP_4–BQP_6 [S122 pp. 9, 14–15]; one round, no selection, a class where the relaxation equals the feasible set, then modified MIPLIB [S052 pp. 9–15, 23–24]; a Python B&B with relaxation-versus-branching ablation [S041 pp. 19–21]; a custom B&B with a fixed incumbent [S123 pp. 5–6]; a stripped column-generation instrument: "We exclude approaches that either modify the RMP or use alternative algorithms to solve the RMP, so that we can isolate the contribution of pricing." [S121 p. 4].
- **Small cases computed exactly before or inside a proof** (step 1): PORTA on n = 10 [S084 pp. 3, 17; S028 pp. 4, 18–19]; a computer check over a provably finite list of splits completes a counterexample [S018 p. 7]; exponential disjunctive LPs evaluate new Lagrangian bounds on small instances before any separation is built [D002 p. 21]; an exact Boolean LP as ceiling [S078 p. 10]; exact CG closure on small instances [S039 p. 7]; BARON ground truth at n ≤ 10 feeding conjectures [S129 pp. 10, 19–21]; a complete classification of SOCP/SDP outcomes on the two-bus system before larger counterexamples [S006 pp. 6–11]; a planted "actual" stiffness before real data [S060 pp. 13–18]; every bound scored against the exact z(b + Δb) [D004 arXiv p. 14]. A conjecture is kept open when computation supports but proof fails: "To date, every computational test we have devised suggests that this conjecture is true, but we have not been able to find a proof." [S122 p. 9].
- **Sanity checks in code**: a solver returning violated solutions is dropped ("We also discovered that Gurobi at times returns solutions with large constraint violations for this MINLP formulation." [S059 p. 18]).
- **Say–do update**: ✅ holds in the branching and cut-measurement line (S020, S041, S048, S052, S081, S098, S122, S123, S130). 31 works link to M2 only as a variant, almost all because no exact ceiling or stripped instrument is used (§3 row 4).

### Variants and contradictions (08 §3)

| # | SKILL.md item | What the full texts show | Cards | Decision |
|---|---|---|---|---|
| 4 | M2 say–do ("2010–2026") | 31 works use full-solver or best-known baselines with no exact ceiling: decentralised power [S047 p. 17], water networks [S075 pp. 22–23], bilinear covers [S105 p. 11], change-point MIP [S124 p. 14], network design [S111 pp. 24–26], facility location [S133 p. 7], sparse CCA beyond n = 20 [S076 p. 12]. | as cited | **Narrow** M2's say–do line: "practised in the branching and cut-measurement line (S020, S041, S048, S052, S081, S098, S122, S123, S130); application papers compare against full solvers." |
| 5 | M2 step 4 / step 6 (instance ladder, no extrapolation) | One 2026 application paper tunes heuristic parameters on the benchmark it reports. | [S109 pp. 21–22] | **Record** as the one M2 contradiction; no change to the method. |

### Added in T3.6

- **Condensed into SKILL.md**: Stated, the expert-method sentence of arXiv:2411.15090, now located in the full text [S082 p. 9], and the isolation of one component in column generation: "We exclude approaches that either modify the RMP or use alternative algorithms to solve the RMP, so that we can isolate the contribution of pricing." [S121 p. 4]. Say–do counts from 08 §2 (26 cards, 25 works as evidence, 23 read; 31 variants; 1 contradiction).
- **Step 1 ceilings**: DP over the 3^n faces of the cube, up to 20 binaries [S020 pp. 11, 21–22]; exhaustive enumeration [S048 pp. 9–12, 15]; facets of BQP_4–BQP_6 [S122 pp. 9, 14–15]; BARON at n ≤ 10 [S129 pp. 10, 19–21]; a planted stiffness [S060 pp. 13–18]; exact z(b + Δb) [D004 arXiv p. 14]; exact Boolean LP [S078 p. 10]; exact CG closure on small instances [S039 p. 7].
- **Step 2**: ratio to the optimal tree, from the abstract: "within a factor of two of the size of the optimal branch-and-bound tree" [S020 p. 1] (the pre-T3.6 SKILL.md cited it from note 01).
- **Step 3 instrument**: the oracle sentence (fair node counting) is in the IJOC paper's text [S081 p. 9] (pre-T3.6 SKILL.md cited it from the released code, [03 §3.3]); SCIP with presolve and propagation off, optimal value supplied, 3 seeds [S081 p. 10]; incumbent control [S098 p. 5; S123 p. 5; S082 pp. 7–8; S130 pp. 5, 23, 25].
- **Step 4 ladder**: [S130 pp. 4, 23; S081 pp. 8–11; S052 pp. 9–15, 23–24]; feature-isolating synthetic families [S052 p. 15; S010 pp. 5–6].
- **Step 5**: [S059 pp. 18, 24].
- **Variant: theory picks the stress axis** (08 §6): [S109 pp. 17–18; S006 pp. 12–15; S009 pp. 28–29; S052 p. 15].
- **Contradiction** (08 §3 row 5): one 2026 application paper tunes heuristic parameters on the benchmark it reports [S109 pp. 21–22]; recorded as a contradiction of step 4 / step 6, no change to the method.
- **Limitations**: the released-code defects stay as recorded by web research [03 C2, C3] and in Research Integrity Rule 5; the full texts do not revisit them.

### Before T3.6 (moved verbatim)

**One line**: Before designing or judging a heuristic, compute the best possible answer on small cases, and compare in a testbed where only the studied decision varies.

**Evidence**:
- Stated: R7 (5 papers) [02 §4.1]; "Before benchmarking the performance of the learning heuristic, we begin by evaluating a theoretical expert method to gauge what potential speedups are achievable" (arXiv:2411.15090); "the enumeration experiments justify how many sparse cuts we should generate at each round" (doi:10.1137/21M1399956) [03 §2.1].
- Practice: DP-optimal B&B trees (doi:10.1007/s10107-023-01977-x); 31,465 supports enumerated (doi:10.1137/21M1399956); naive Python B&B in released code (doi:10.1287/ijoc.2024.0709.cd) [03 §3.3]; PORTA before a conjecture (student report) [04 T1].
- Say–do consistency: ✅ stated + practised, 2010-2026.

**Steps**:
1. Compute the ceiling: DP-optimal trees (up to about 20 binaries), exhaustive enumeration, an "expert method" bounding the possible speed-up, or all facets of a small polytope.
2. Let the ceiling decide: "when accounting for the time required to collect the cuts, most positive instances become negative, which motivates our learning approach." [03 §2.1]. Report results as a ratio to the ceiling ("within a factor of two of the size of the optimal branch-and-bound tree") [01 §2.4].
3. Build the instrument: a "naive" textbook B&B with the expensive rule as an oracle "without influencing any other process within branch-and-bound, thus allowing fair node counting" [03 §3.3]; or a solver with presolve, propagation, heuristics and conflict analysis off, objective limit at the known optimum, several seeds.
4. Climb the instance ladder: random instances with a planted feasible point → benchmark with filters written as code → instances isolating one feature → benchmark [03 §3.1].
5. Sanity checks in code: dual bound against the known optimum; drop a solver that returns violated solutions [03 §3.7].
6. Write the limit: "Some of the observations derived here may not extrapolate to larger instances." [02 §4.1]

**Different from standard practice**: the first comparison is with an exact optimum in a deliberately stripped instrument, not with a full solver's default.

**Limitations**: DP ground truth stops near 20 binaries; MINLP subproblems add local-solver noise (fix settings and seeds). His own released code has defects: the generator does not match the stated distribution, 29 of 693 result rows are missing [03 C2, C3]. Stop rule: no headroom once overheads count → redirect; no extrapolation beyond the instrument's size.

### SKILL.md Evidence block before the T3.6 review fixes (moved verbatim)

**Evidence** (full evidence: references/research/09-evidence-ledger.md#method-2):
- Stated: "Before benchmarking the performance of the learning heuristic, we begin by evaluating a theoretical expert method to gauge what potential speedups are achievable" (arXiv:2411.15090) [S082 p. 9]; isolating one component on purpose [S121 p. 4].
- Practice: DP-optimal trees up to 20 binaries [S020 pp. 11–13, 21–22]; naive B&B with strong branching as oracle, then stripped SCIP with seeds [S081 pp. 8–11]; enumeration as ceiling [S048 pp. 9–12]; one round, no selection rule [S052 pp. 9–15].
- Say–do: ✅ stated + practised in the branching and cut-measurement line (9 works); full texts: 25 works as evidence (23 read), 31 as variants, 1 contradiction.
- Variants/corrections:
  - ⚠ Scope: application papers compare against full solvers or best-known values, with no exact ceiling [S047 p. 17; S075 pp. 22–23; S111 pp. 24–26].
  - ✗ One 2026 application paper tunes heuristic parameters on the benchmark it reports [S109 pp. 21–22].
  - ⚠ Small cases computed exactly before or inside a proof [S028 pp. 4, 18–19; S018 p. 7; S122 p. 9].
  - ⚠ Theory picks the stress axis: sweep the parameter the bound depends on [S009 pp. 28–29; S109 pp. 17–18].

<a id="method-3"></a>

## Method 3: Import the integer-programming substructure paradigm into QCQP and MINLP

### Full-text evidence (08 §2)

- **Strongest practice**: MILP closure theorems asked of convex nonlinear sets, 2010–2014 [S018 p. 2; S042 pp. 1–2; D001 p. 2; S025 p. 2; S063 pp. 6–7]; subadditive duality carried to conic IP [S037 pp. 2–3]; Meyer's theorem for convex sets [S029 pp. 2, 17]; asked of MIQP whether it is in NP, as for MILP [S003 pp. 3–4]; the cost of term-by-term McCormick quantified [S021 pp. 1–3]; cycle substructures in power flow convexified jointly [S001 pp. 15–24; S009 pp. 4, 10–18; S008 pp. 5–18]; rank-one substructures for pooling: "Observe that all the non-convexity of the problem is now captured by the rank-1 condition." and "It is well-known that it is possible to obtain tighter convex relaxations when convexifing a set directly rather than using convex envelopes of functions describing the set." [S051 p. 2]; one quadratic over a polytope [S032 p. 2]; aggregations of quadratics [S071 pp. 1–5; S077 pp. 1–2, 27; S103 pp. 2–5, 11]; lifting and covers from 0-1 knapsack into separable bilinear rows [S135 pp. 1–2, 4–8; S105 pp. 1–2, 9]; separable power functions over a polytope [S129 pp. 1–2, 8, 11–17]; treewidth theory carried to continuous QP [S092 pp. 3–5, 13, 22–25].
- **Stated in the texts**: "A common and successful approach in integer linear programing is to generate cutting-planes implied by single constraint relaxation, see for example [8, 24, 11, 3]. We take a similar approach here." [S041 p. 2]; "To the best of our knowledge, however, no one from the global optimization community has ever exploited such results for convexification." [S032 p. 3] (T3.6 review: on p. 3 "such results" refers to the classical theory of ruled surfaces, which the authors learned of after proving their theorem; it is not a statement about convexifying sets cut out by several constraints. The relevant statement is on p. 2: function convexification "does not necessarily yield the convex hull", and there has been "much less work on explicit convexification of sets" [S032 p. 2].). The convex-MINLP NSF award states the MILP checklist as its objective [S146].
- **Exponential cost of the hull, as SKILL.md says**: "while the convex hull is SOCr, the construction involves the introduction of an exponential number of variables." (from [S032 p. 2]); the computational "light" version has no guarantee: "Unfortunately, there are no theoretical guarantees for the bounds of this light version of the relaxation." [S041 p. 5]; the exact hull is proved but four edge cuts are coded [S008 pp. 10–14].
- **Say–do update**: ✅, 41 full or partial works from 2010 to 2026. The specialist step (step 6) is confirmed with Blekherman [S077 pp. 1–2, 27; S119 p. 1; S035 pp. 1–3; S055 p. 7].

### Variants and contradictions (08 §3)

| # | SKILL.md item | What the full texts show | Cards | Decision |
|---|---|---|---|---|
| 7 | M3 contradiction (two-row cuts disappointed, yet two-row ideas went to QCQP) | Confirmed: the computational multi-row goal "was too ambitious" and type 2 triangle cuts "are not competitive with split cuts" for typical instances [S052 pp. 2, 25]; density was already named as the practical obstacle in 2009: "Another practical difficulty with this class of cutting planes is that they tend to be dense." [S079 p. 8]. New variants: an MILP algorithmic rule (strong branching, product score) imported into QCQP [S123 pp. 1–4]; an IP operation (CG rounding) imported [S122 pp. 2–5]; the reverse direction, polynomial lifting brought back into MIP decomposition [S104 pp. 5, 9]. | as cited | Keep the contradiction; **add a variant line** to M3: "imports algorithmic rules and closure operations too, and once runs in reverse." |

### Added in T3.6

- **Condensed into SKILL.md**: Stated [S041 p. 2; S051 p. 2]; Practice [S018 p. 2; S042 pp. 1–2; S003 pp. 3–4; S001 pp. 15–24; S071 pp. 1–5; S135 pp. 4–8]; counts from 08 §2 (46 cards, 44 works as evidence, 41 read; 25 variants; 0 contradictions).
- **Step 1**: the convex-MINLP NSF award states the MILP checklist as its objective [S146] (abstract level).
- **Step 2**: per-cycle angle conditions in meshed power flow [S001 pp. 15–18]; "Observe that all the non-convexity of the problem is now captured by the rank-1 condition." [S051 p. 2].
- **Step 3**: "comes up naturally for the pooling problem" [S051 p. 2] (in the pre-T3.6 SKILL.md cited from note 01).
- **Step 4 device**: extreme-point support bound by a perturbation that keeps active constraints tight, then the union of small-support pieces [S051 pp. 4–7; S032 pp. 4–10; S041 pp. 6–7].
- **Step 5**: aggregations against the hull, with counterexamples [S071 pp. 5–9, 17–24].
- **Step 6**: Blekherman [S077 pp. 1–2, 27; S119 p. 1; S035 pp. 1–3; S055 p. 7].
- **Step 7**: generalized pooling testbed with new Random instances posted online, against Gurobi [S051 pp. 17–20].
- **Different from standard practice**: "To the best of our knowledge, however, no one from the global optimization community has ever exploited such results for convexification." [S032 p. 3] (T3.6 review: on p. 3 "such results" refers to the classical theory of ruled surfaces, which the authors learned of after proving their theorem; it is not a statement about convexifying sets cut out by several constraints. The relevant statement is on p. 2: function convexification "does not necessarily yield the convex hull", and there has been "much less work on explicit convexification of sets" [S032 p. 2].); "It is well-known that it is possible to obtain tighter convex relaxations when convexifing a set directly rather than using convex envelopes of functions describing the set." [S051 p. 2].
- **Hull cost**: "while the convex hull is SOCr, the construction involves the introduction of an exponential number of variables." [S032 p. 2]; "Unfortunately, there are no theoretical guarantees for the bounds of this light version of the relaxation." [S041 p. 5].
- **Contradiction kept**: "However such a goal was too ambitious and we have had to considerably restrict it." [S052 p. 2]; "Another practical difficulty with this class of cutting planes is that they tend to be dense." [S079 p. 8].

### Before T3.6 (moved verbatim)

**One line**: List what MILP theory knows (closures, duals, single- and two-row relaxations, lifting, convexified substructures), ask the same of the nonlinear class, and convexify a small recurring set jointly rather than function by function.

**Evidence**:
- Stated: R3 (6 occasions) [02 §2.3]; "The art lies in obtaining a relaxation that is both easy to analyze and yet strong enough to generate potent cutting planes." (Optima 80, 2009, p. 2) [02 §3.1]; "An important area of study regarding convexification schemes for QCQPs is to convexify commonly occurring substructures, like in the case of integer programming." (arXiv:1902.00739, p. 1) [01 §2.5].
- Practice: convex MINLP 2010-17 (doi:10.1287/moor.1110.0488); QCQP substructures 2019-26 (doi:10.1007/s10898-019-00844-4, doi:10.1137/19M1277333, doi:10.1137/21M1428583, doi:10.1137/22M1528215, doi:10.1007/s10898-026-01607-8) [06 T4, T9].
- Say–do consistency: ✅ stated + practised.

**Steps**:
1. Write the MILP list with a question mark for the target class ("1. Representability results ? 2. Dual ? 3. Cutting plane closures ?", 2012 slide) [02 §2.3].
2. Find the substructure carrying the nonconvexity: after lifting, "all the non-convexity of the problem is now captured by the rank-1 condition" [01 §2.5]; or one quadratic over a polytope, three quadratics, bipartite bilinear rows.
3. Let an application choose the side constraints ("comes up naturally for the pooling problem") [01 §2.5].
4. Convexify the set toward the hull; prefer constructive proofs with an extended formulation, and state its size.
5. Test the cheap practice against the hull: when do aggregations already give it? Counterexamples where not (→ Method 4).
6. Bring in a specialist for the algebraic step (Blekherman) [06 T11].
7. Return to a testbed (generalized pooling, FEM model updating) against BARON / Gurobi with released instances.

**Different from standard practice**: not envelopes of single terms (McCormick) but sets cut out by several constraints at once, as MILP does with knapsack, flow-cover and mixing sets.

**Limitations**: hulls may need exponential extended formulations; algebraic steps may need a mathematician. Contradiction kept: in 2005-2009 single-constraint cuts were the limit to go beyond; from 2019 single-constraint relaxations became the model to copy, and two-row ideas went to QCQP although two-row MILP cuts had disappointed [02 C4]. Stop rule: if the cheap relaxation matches the hull in experiments, say the hull is not worth it ("consistently weaker and hence omitted" [02 §5.4]).

### SKILL.md Evidence block before the T3.6 review fixes (moved verbatim)

**Evidence** (full evidence: references/research/09-evidence-ledger.md#method-3):
- Stated: "A common and successful approach in integer linear programing is to generate cutting-planes implied by single constraint relaxation, see for example [8, 24, 11, 3]. We take a similar approach here." [S041 p. 2]; "Observe that all the non-convexity of the problem is now captured by the rank-1 condition." [S051 p. 2]
- Practice: closures of convex sets [S018 p. 2; S042 pp. 1–2]; asked of MIQP whether it is in NP, as for MILP [S003 pp. 3–4]; cycle substructures in power flow [S001 pp. 15–24]; aggregations of quadratics [S071 pp. 1–5]; knapsack covers in bilinear rows [S135 pp. 4–8].
- Say–do: ✅ stated + practised; full texts: 44 works as evidence (41 read, 2010–2026), 25 as variants, 0 contradictions.
- Variants/corrections:
  - ⚠ Imports algorithmic rules and closure operations too (strong-branching product score into QCQP [S123 pp. 1–4]; CG rounding [S122 pp. 2–5]), and once runs in reverse, polynomial lifting brought back into MIP decomposition [S104 pp. 5, 9].
  - ⚠ Contradiction kept and confirmed: the computational two-row goal "was too ambitious" [S052 p. 2] and density was named the practical obstacle in 2009 [S079 p. 8], yet two-row ideas went to QCQP.
  - ⚠ The exact hull may need exponentially many variables; the coded "light" version has no guarantee [S032 p. 2; S041 p. 5].

<a id="method-4"></a>

## Method 4: Demarcate every result

### Full-text evidence (08 §2)

- **Strongest practice**: MIQP in NP with three counterexamples, "tight with respect to the number of quadratic inequalities" (from [S003 p. 3]); pooling: tight bound for every scheme, inapproximability, a constructive attaining object, tightness of the restriction itself, a negative family [S014 pp. 6, 12, 16–18, 20]; aggregations: a counterexample for each dropped hypothesis and the simple rigorous box, "We just focus on a box whose validity proof is simple and rigorous." [S071 p. 18; pp. 5–9, 17–24]; forbidden vertices: each tractable case paired with hardness when one hypothesis is dropped [S022 pp. 2, 4–6, 8–10]; sparse cuts: upper bounds with near-matching random lower bounds and a negative packing class [S084 pp. 3–5]; McCormick gap: matching upper and lower bounds and an exact equality characterisation [S021 pp. 3, 6–11]; Geoffrion's theorem: a counterexample for the dropped hypothesis plus sufficient conditions [S112 pp. 2–8]; positive k = 2 and impossibility for k ≥ 3 with the gap stated open [S118 pp. 2–4]; exponential lower bounds for every encoding family [S117 pp. 12–19]; both assumptions of a regularisation theorem shown necessary [S080 pp. 9–11]; a cycle counterexample showing where a decomposable zero-gap dual needs a tree [S097 pp. 4, 8–9, 12]; NP-hardness, strict containments by explicit points, matching distance bounds, conjectures stated [S129 pp. 3, 7, 10–14, 21].
- **Stated in the texts**: "we also show that the verification scheme is not unrealistically strong" (from [S095 p. 17; S096 p. 11]); "a reasonable demarcation of conditions" (from [S071 p. 2]); "We do not know if the k-lattice-free closure of covering polyhedron is well-behaved." [S099 p. 7]; "While we have improved upon the bound presented in [34], we do not know if this new bound is tight." [S017 p. 5].
- **Say–do update**: ✅ with the widest base of the five (83 full or partial works, every period from 2008 to 2026). SKILL.md calls exclusivity the weakest check; the full texts do not change that, but they show the boundary as a headline object in at least S003, S014, S022, S071, S112, S117, S118. Scope note: §3 row 8.

### Variants and contradictions (08 §3)

| # | SKILL.md item | What the full texts show | Cards | Decision |
|---|---|---|---|---|
| 8 | M4 scope | In computational and application papers the boundary is drawn computationally (300-bus limit, cases where the strongest method underperforms) [S005 pp. 14, 16, 18; S004 p. 20; S001 pp. 13–14], or through sufficient conditions without a tight example [S031 pp. 3, 15; S120 pp. 2–3; S082 pp. 6, 12; S083 p. 4]. A constructive form of step 3 recurs: find what replaces the dropped hypothesis rather than only exhibiting the failure (rationality replaced by an interior mixed-integer point [S037 p. 3], by a thin set with rational recession cone [S029 pp. 2, 17]; Dirichlet approximation for irrational data [D001 pp. 3–4, 6; S043 p. 14]; Geoffrion beyond finiteness and rationality: "The challenge for extending Geoffrion's theorem beyond finiteness and rationality is thus to understand integer programs whose feasibility set lies on the boundary of conv(X)." [S112 p. 5]). | as cited | **Add** to M4's limitation: "governs headline theory papers; computational papers draw the line computationally." **Add** the replacement-hypothesis form to step 3. |

### Added in T3.6

- **Condensed into SKILL.md**: Stated [S071 p. 2]; Practice [S003 pp. 2–3; S014 pp. 6, 12, 16–18, 20; S022 pp. 4–6; S118 pp. 2–4]; counts from 08 §2 (90 cards, 85 works as evidence, 83 read; 13 variants; 0 contradictions).
- **Further practice** (08 §2): sparse cuts, upper bounds with near-matching random lower bounds and a negative packing class [S084 pp. 3–5]; McCormick gap, matching bounds and an exact equality characterisation [S021 pp. 3, 6–11]; Geoffrion's theorem, a counterexample for the dropped hypothesis plus sufficient conditions [S112 pp. 2–8]; exponential lower bounds for every encoding family [S117 pp. 12–19]; both assumptions of a regularisation theorem shown necessary [S080 pp. 9–11]; a cycle counterexample showing where a decomposable zero-gap dual needs a tree [S097 pp. 4, 8–9, 12]; NP-hardness, strict containments, matching distance bounds, conjectures [S129 pp. 3, 7, 10–14, 21]; a two-sided sensitivity theorem with "cannot be further relaxed" remarks [D004 arXiv pp. 3–8].
- **Step 1 / 2**: tightness for every PL scheme and inapproximability [S014 pp. 8–12]; a tight instance and a match to the known FPT algorithm [S020 p. 6]; the attaining restriction [S014 p. 16].
- **Step 3, constructive form** (08 §3 row 8): rationality replaced by an interior mixed-integer point [S037 p. 3], by a thin set with rational recession cone [S029 pp. 2, 17]; Dirichlet approximation for irrational data [D001 pp. 3–4, 6; S043 p. 14]; "The challenge for extending Geoffrion's theorem beyond finiteness and rationality is thus to understand integer programs whose feasibility set lies on the boundary of conv(X)." [S112 p. 5].
- **Step 4**: aggregation cuts add at most a factor 2 on packing, arbitrarily much in general [S011 pp. 18–20].
- **Step 6**: "While we have improved upon the bound presented in [34], we do not know if this new bound is tight." [S017 p. 5]; "We do not know if the k-lattice-free closure of covering polyhedron is well-behaved." [S099 p. 7].
- **Step 7**: the full passage is on the card's page [S071 p. 18].
- **Limitations**: worst-case results "only provide a coarse indication" [S011 p. 10].

### Before T3.6 (moved verbatim)

**One line**: A positive theorem is not finished until the paper shows where it stops: the tight example, the hardness of beating it, and what breaks when each hypothesis is dropped.

**Evidence**:
- Stated: R5 (8 occasions); "The analysis is tight: all the bounds obtained are tight." (2015 talk) [02 §1.3].
- Practice: MIQP in NP, tight in the number of quadratic inequalities (doi:10.1007/s10107-016-1036-0); pooling factor n tight, hard to beat, attained by an MILP restriction (doi:10.1287/opre.2015.1357); aggregations with three- and four-quadratic counterexamples (doi:10.1137/21M1428583) [01 §2.2-2.5].
- Say–do consistency: ✅ stated + practised. Exclusivity is the weakest of the five: good theorists do this too; here the boundary is a headline result.

**Steps**:
1. Tightness: build the instance attaining the bound.
2. Hardness of improvement, and a constructive object that attains the bound.
3. Drop each hypothesis and show the failure (many quadratic inequalities → undecidable; two → exponential-size solutions).
4. Pair positive and negative instance classes (packing IPs where sparse cuts fail) [01 §2.4].
5. State the cost of a constructive proof ("The size of the second order "extended formulation" is exponential in size.") [02 §1.3].
6. If tightness is unknown, say so: "we do not know if this new bound is tight." [02 §5.4]
7. Prefer the simple rigorous version: "We remark that the bounding box [-8, 8]^3 is by no means optimal. Our numerical experiments indicate that it is actually [-1.23, 1.23]^3. We just focus on a box whose validity proof is simple and rigorous." (doi:10.1137/21M1428583) [03 §4.4]

**Different from standard practice**: many papers stop at the upper bound; here the boundary ranks with the positive result.

**Limitations**: tension with his view that worst case gives "a coarse indication" (2018) [02 C1]. Rule here: Method 4 governs how a theorem is stated; Method 1 step 5 governs whether worst case is the right model. Stop rule: no submission with an unexamined boundary; if no matching negative is found, say the gap is open.

### SKILL.md Evidence block before the T3.6 review fixes (moved verbatim)

**Evidence** (full evidence: references/research/09-evidence-ledger.md#method-4):
- Stated: "We also show, via examples, that this result provides a reasonable demarcation of conditions that allow obtaining the convex hull of quadratic constraints via aggregated constraints." [S071 p. 2]
- Practice: MIQP in NP with a counterexample for each strengthening [S003 pp. 2–3]; pooling: tight bound, inapproximability, attaining restriction, negative family [S014 pp. 6, 12, 16–18, 20]; forbidden vertices [S022 pp. 4–6]; k = 2 positive, k ≥ 3 impossible [S118 pp. 2–4].
- Say–do: ✅ stated + practised; full texts: 85 works as evidence (83 read, every period 2008–2026), 13 as variants, 0 contradictions: the widest base of the six.
- Variants/corrections:
  - ⚠ Scope: governs the headline theory papers; computational and application papers draw the line computationally (300-bus limit) or through sufficient conditions only [S005 pp. 14, 16, 18; S031 pp. 3, 15; S120 pp. 2–3].
  - ⚠ Step 3 has a constructive form: find what replaces the dropped hypothesis (an interior mixed-integer point for rationality [S037 p. 3]; the boundary of conv(X) for Geoffrion [S112 p. 5]).
  - ⚠ Open tightness said plainly: "While we have improved upon the bound presented in [34], we do not know if this new bound is tight." [S017 p. 5]

<a id="method-5"></a>

## Method 5: Certify with a cheap, strong relaxation

### Full-text evidence (08 §2)

- **Strongest practice**: OPF: rank relaxations, strengthen the SOCP by cycle structure, pair with IPOPT, report the certified gap at 3375 buses with hardware [S001 pp. 1, 4, 14, 26–29]; the transmission-switching relaxation with proved gaps on stated hardware, and "our algorithm gives optimality guarantees by construction" (from [S005 p. 20]); LP/SOC-only spatial branch and cut [S008 pp. 8, 19–27, 30–33]; sparse PCA dual bounds up to n = 2000 [S017 pp. 3, 6–11, 14, 17; S057 pp. 6, 25–30]; an LP made to emulate the SDP: "we would like to obtain an outer approximation of the original set that can mimic the strength of the SDP relaxation, but that is lightweight and linear." [S048 p. 3]; floor layout: "Our assessment is that the lifted representations, while theoretically interesting, do not provide an off-the-shelf practical approach for this problem as they are too large and not sufficiently strong." [S100 p. 12]; network design dual bounds on industrial instances [S111 pp. 2, 20, 26–27]; a dual bound preserved under random projection [D005 pp. 1, 8, 12–13]; Lagrangian preferred to DP because bounds are available at any stop: "However, DP suffers from the disadvantage that we do not obtain any information on bounds until the algorithm terminates." [S097 p. 2].
- **Stated in the texts**: "Most conventional methods for solving SPCA are heuristics with no guarantees such as certificates of optimality on the solution-quality via associated dual bounds." [S017 p. 1]; "Recall that dual bounds are typically crucial for effective computational procedures for non-convex problems" (from [S057 p. 6]); the same complaint for model-free SPCA [S083 p. 1], structural model updating [S060 p. 27], network design [S111 p. 2] and grid security [S058 p. 1].
- **Say–do update**: ✅ (30 full or partial works, 2016–2026). Two contradictions and five variants are recorded in §3 rows 9–11.

### Variants and contradictions (08 §3)

| # | SKILL.md item | What the full texts show | Cards | Decision |
|---|---|---|---|---|
| 9 | M5 (certificate as deliverable) | Two works deliver no certificate: a kNN heuristic with possibly infeasible output [S044 pp. 4, 16] and a scalable primal bound for relay attacks, "we do not know of a non-trivial upper bound" (from [S058 p. 14]). In five application papers the contribution is primal and the dual bound is borrowed from BARON or SCIP [S014 pp. 26, 28; D002 pp. 22, 25; S059 pp. 13–15, 19; S075 pp. 11, 24–25; S109 pp. 17, 19]. | as cited | **Record** both contradictions; add to M5's limitations: "in application work with Sahinidis and on pooling he often supplies the primal side and borrows the certificate." |
| 10 | M5 step 2 ("rank candidate relaxations") | The ranking is often done by theorem, and the heavier relaxation is proved to add nothing before cheap cuts are offered: lifted LP, lifted SDP and an earlier SDP all equal a closed-form bound [S100 pp. 9–10]; an SOCP relaxation proved at least as strong as SDP ∩ QBP [S041 p. 3]; "We show that, surprisingly, for the class of separable instances, the SDP relaxation gives a bound equal to that of the McCormick relaxation." [S105 p. 4]; "Interestingly, adding the SDP constraint (3) to the P relaxation does not further strengthen this relaxation as proven below." [S129 p. 5]; six relaxations ordered in projected space before one is strengthened [S001 pp. 11–14]. The device is a PSD completion, rank one plus a sparse or diagonal correction, [S105 pp. 5–7; S129 p. 5; S001 pp. 11–12]. | as cited | **Variant note** on M5 step 2: "where possible prove the ranking; a PSD completion of the cheap optimum shows the SDP adds nothing." Not a new method (it is M5's own step). |
| 11 | M5 steps 3–4 | Step 4's feasible point often comes from an MILP restriction built from the same discretisation or proof as the relaxation, not from a local solver [S014 pp. 14–16; D002 pp. 22–25; S051 pp. 10–11, 17–18; S080 pp. 18–19]. Step 3 includes constraints redundant for the primal that strengthen the dual or the solver bound [S104 pp. 3–5; S117 pp. 2, 13; S111 p. 16]. The cheap object can be a DNN/SDP restriction of a copositive dual [D004 arXiv pp. 11, 13–14]. | as cited | **Variant notes** on M5 steps 3 and 4. |
| 12 | M5 limitation: "In 2017 he qualified his 2016 claim: 'not very competitive against the SDP relaxation, especially for easier instances'" | The sentence is in the spatial branch-and-cut paper read as arXiv v1: "Strong SOCP relaxations from our previous paper [27] improves the plain SOCP relaxation considerably but it is not very competitive against the SDP relaxation, especially for easier instances." [S008 p. 31]. The 2016 paper's own comparison section already says "We note that our SOCP based relaxations are not as successful according to this comparison." [S001 p. 30]. | [S008 p. 31; S001 p. 30] | **Revise** the attribution: the qualification is already in the November 2015 arXiv v4 of the 2016 paper and repeated in the March 2017 preprint of the 2018 MPC paper; journal texts not read (wording corrected in the T3.6 review). |

### Added in T3.6

- **Condensed into SKILL.md**: Stated [S057 p. 6] plus the 2024 talk caption; Practice [S001 pp. 1, 4, 14, 26–29; S008 pp. 8, 19–27; S017 pp. 3, 6–11; S048 p. 3; S111 pp. 2, 20, 26–27]; counts from 08 §2 (34 cards, 32 works as evidence, 30 read; 23 variants; 2 contradictions).
- **Step 2 by theorem** (08 §3 row 10): "We show that, surprisingly, for the class of separable instances, the SDP relaxation gives a bound equal to that of the McCormick relaxation." [S105 p. 4]; "Interestingly, adding the SDP constraint (3) to the P relaxation does not further strengthen this relaxation as proven below." [S129 p. 5]; lifted LP, lifted SDP and an earlier SDP all equal a closed-form bound [S100 pp. 9–10]; an SOCP relaxation at least as strong as SDP ∩ QBP [S041 p. 3]; six relaxations ordered in projected space [S001 pp. 11–14]. The device is a PSD completion of the cheap optimum [S105 pp. 5–7; S129 p. 5; S001 pp. 11–12].
- **Step 3**: OPF cycle constraints, arctangent envelopes, cycle-SDP cuts [S001 pp. 15–24]; separation by sparse PCA [S048 pp. 6–7, 15]; constraints redundant for the primal that strengthen the dual or the solver bound [S104 pp. 3–5; S117 pp. 2, 13; S111 p. 16].
- **Step 4**: the feasible point from an MILP restriction built from the same discretisation [S014 pp. 14–16; D002 pp. 22–25; S051 pp. 10–11, 17–18; S080 pp. 18–19]; the certified gap with hardware [S001 pp. 1, 26]; "our algorithm gives optimality guarantees by construction" (text of [S005 p. 20]).
- **Step 6**: own spatial branch-and-cut [S008 pp. 19–27]; a decomposable dual [S097 pp. 4, 8–9]; "However, DP suffers from the disadvantage that we do not obtain any information on bounds until the algorithm terminates." [S097 p. 3] (08 cites the same sentence as p. 2).
- **Contradictions** (08 §3 row 9): a kNN heuristic with possibly infeasible output and no certificate [S044 pp. 4, 16]; a scalable primal bound for relay attacks: "This is difficult to answer since we do not know of a non-trivial upper bound for the worst-case relay attack problem." (text of [S058 p. 14]).
- **Borrowed certificate**: [S014 pp. 26, 28; D002 pp. 22, 25; S059 pp. 13–15, 19; S075 pp. 11, 24–25; S109 pp. 17, 19].
- **Limitations, attribution corrected** (08 §3 row 12): "We note that our SOCP based relaxations are not as successful according to this comparison." [S001 p. 30]; "Strong SOCP relaxations from our previous paper [27] improves the plain SOCP relaxation considerably but it is not very competitive against the SDP relaxation, especially for easier instances." [S008 p. 31].
- **Variant object**: the cheap object can be a DNN/SDP restriction of a copositive dual [D004 arXiv pp. 11, 13–14].

### Before T3.6 (moved verbatim)

**One line**: Demand a dual bound from the most tractable relaxation (LP or SOCP), strengthened by inequalities read off the structure, and report the certified gap at full benchmark scale on stated hardware.

**Evidence**:
- Stated: R4 (8 occasions) [02 §1.2]; the "Heuristics do not come with certificates" and LP/SOCr quotes (Research Taste); "So the motivation here was dual bounds. Okay, I don't want to just find good solutions. I want to certify it." (MIP International 2024, auto-caption).
- Practice: AC-OPF arc (doi:10.1109/TPWRS.2015.2402640 → doi:10.1287/opre.2016.1489 → doi:10.1007/s12532-018-0150-9); sparse PCA dual bounds (doi:10.1287/opre.2021.2153); decomposable Lagrangian dual (doi:10.1007/978-3-031-93112-3_14); SOC-representable nonconvex QPs (doi:10.1007/s10107-026-02364-y).
- Say–do consistency: ✅ stated + practised.

**Steps**:
1. Name the certificate: a lower bound plus a feasible point with a small gap.
2. Rank candidate relaxations on the formulations at hand (McCormick/LP, SOCP, SDP, piecewise MILP).
3. Strengthen the tractable one with structure (OPF cycle constraints, arctangent envelopes, SDP-cone cuts over cycles; sparse PCA cuts in place of the SDP, doi:10.1137/21M1399956) [01 §2.1].
4. Pair it with a local solver and report the certified gap at the largest size, naming the hardware ("within 0.13% of global optimality, all this computed within 157.20 seconds on a modest personal computer", arXiv:1504.06770).
5. Build and release instances where the accepted relaxation fails (Heuristic 1).
6. Close remaining gaps with your own spatial branch-and-cut or a decomposable dual.

**Different from standard practice**: not the strongest relaxation (SDP-first) nor a general global solver, but the cheapest relaxation that can be made strong, with the certified gap as the deliverable.

**Limitations**: set on 2014-17 instances on a PC; at PGLib scale SOC relaxations are hard for "all solvers" on "large or even medium cases" (doi:10.1007/s12532-025-00287-x); the real/complex SDP equivalence his OPF papers cited is called "incorrect" (arXiv:2510.21698), though the needed inequality holds [05 §1.2]. In 2017 he qualified his 2016 claim: "not very competitive against the SDP relaxation, especially for easier instances" [05 §5.2]. Stop rule: when a harder benchmark shows the cheap relaxation losing, say so; when an "exact" reformulation proves only a relaxation, flag the change.

### SKILL.md Evidence block before the T3.6 review fixes (moved verbatim)

**Evidence** (full evidence: references/research/09-evidence-ledger.md#method-5):
- Stated: "Recall that dual bounds are typically crucial for effective computational procedures for non-convex problems" [S057 p. 6]; "So the motivation here was dual bounds. Okay, I don't want to just find good solutions. I want to certify it." (MIP International 2024, auto-caption).
- Practice: OPF: rank relaxations, strengthen the SOCP by cycles, pair with IPOPT, certified gap at 3375 buses [S001 pp. 1, 4, 14, 26–29]; LP/SOC-only spatial branch and cut [S008 pp. 8, 19–27]; sparse PCA dual bounds [S017 pp. 3, 6–11]; an LP that mimics the SDP [S048 p. 3]; network design dual bounds on industrial instances [S111 pp. 2, 20, 26–27].
- Say–do: ✅ stated + practised; full texts: 32 works as evidence (30 read, 2016–2026), 23 as variants, 2 contradictions.
- Variants/corrections:
  - ✗ Two works deliver no certificate: a kNN heuristic with possibly infeasible output [S044 pp. 4, 16] and a scalable primal bound for relay attacks [S058 p. 14].
  - ⚠ In pooling and network-design application work he supplies the primal side and borrows the certificate from BARON or SCIP [S014 pp. 26, 28; S059 pp. 13–15; S075 pp. 24–25].
  - ⚠ Step 2 is often done by theorem: the heavier relaxation is proved to add nothing, via a PSD completion of the cheap optimum [S100 pp. 9–10; S105 p. 4; S129 p. 5].
  - ⚠ Step 4's feasible point often comes from an MILP restriction built from the same discretisation [S014 pp. 14–16; D002 pp. 22–25; S051 pp. 10–11]; step 3 may add constraints redundant for the primal [S104 pp. 3–5].

<a id="method-6"></a>

## Method 6: Exploit the re-solve: prove what carries over, reuse it, keep the certificate

### Full-text evidence and promotion (08 §4)

SKILL.md stays inside the 3–7 range (five methods now, six after this).

**Cards (≥3 distinct works, all full)**: S044 (2020) [S044 pp. 1–4, 18]; S098 (2022) [S098 pp. 1–2, 4–10]; S082 (2024) [S082 pp. 1–2, 5–6, 9–17]; D004 = S067 (2024 / 2026) [D004 arXiv pp. 2, 4–5, 14, 40; S067 pp. 2, 7, 9–12, 14, 40]. Abstract-level support: MIPLearn [S087].

**What the cards show**:
- The setting is the entry in all four: the same network re-solved every 5 minutes with load and cost varying little [S044 pp. 1–3]; operational MILPs re-solved daily with the same structure, so variable identities persist [S098 pp. 1–2]; the same constraint matrix with changing right-hand side and objective [S082 pp. 1–2]; the same constraint matrix because the constraints describe physical resources [S067 p. 2; D004 arXiv p. 2].
- A structural license is proved before or beside the reuse: a unique integer optimum stays optimal in a right-hand-side neighbourhood, because the value function is a minimum of finitely many LP value functions [S044 p. 18]; the set of useful split directions is finite over the whole instance family, via a right-hand-side-independent certificate cone and Carathéodory [S082 pp. 6, 16–17]; local stability of the dual bound [S067 p. 7] and rhs-parametric dual bounds by weak duality [D004 arXiv pp. 4–5].
- The reuse targets the side the solver is weak on: dual bounds, since solvers find primal solutions fast but their own dual gap stays above 10% [S067 pp. 2, 40; D004 arXiv pp. 2, 40]; the B&B proof, since ML heuristics find solutions but proving optimality still needs large trees [S098 p. 2]; the GMIC closure, strong but too expensive to separate [S082 pp. 3, 5].
- The reused object is chosen for its downstream use: archives of past optimal topologies [S044 pp. 3–4]; per-entity surrogate models with a general fallback [S098 pp. 4–7]; aggregation multipliers [S082 pp. 6, 9–12]; a dual solution picked inside the ε-optimal face for the target Δb range [S067 pp. 9–12; D004 arXiv pp. 9–12].
- Measured against a ceiling: the expert method is evaluated first and overhead charged [S082 p. 9]; bounds scored against the exact value [D004 arXiv p. 14]; the rule's distance to the expensive oracle [S098 p. 10].

**Four checks**:
1. **Cross-project recurrence** ✅: four works over 2020–2026, four problem types (transmission switching, branching, GMIC closure, MBQP sensitivity), three coauthor groups (Johnson–Ahmed–Watson [S044 pp. 1–2]; Gu, Xavier and Qiu [S098], Becu, Qiu and Xavier [S082]; Cifuentes and Xu [S067 p. 1]).
2. **Say–do consistency** ✅: the motivation is stated in the texts' own introductions [S044 pp. 1–3; S098 p. 2; S082 pp. 1–2; S067 p. 2] and practised in all four. (SKILL.md's Anti-patterns row also cites a 2024 talk statement on restarting from scratch; that is web-research evidence, not a card.)
3. **Executable, and different from standard practice** ✅: the steps below produce actions a per-instance study would not take (prove a carry-over theorem; reuse a dual object, not only a primal one; charge collection overhead against an expert ceiling). The cards contrast it with the per-instance classical sensitivity theory, which gives only trivial bounds for binaries [D004 arXiv p. 2] and with heuristics without proofs: "Unlike pure ML methods, MIPLearn is not only able to find high-quality solutions to discrete optimization problems, but it can also prove the optimality and feasibility of these solutions." [S087].
4. **Exclusivity** ✅ (narrow): learning across instance families is common in ML-for-MIP; what the cards show beyond it is the license theorem before reuse [S044 p. 18; S082 pp. 6, 16–17; S067 p. 7] and reuse aimed at the certificate [S067 pp. 2, 40; S098 p. 2]. The check passes on that combination, not on "learning from past instances" alone.

**Proposed steps**:
1. Confirm the deployment: same A, new (b, c); write down how often it is re-solved and how much the data move [S044 pp. 1–3; S082 pp. 1–2, 13].
2. Find the solver's weak side in that setting (dual bound, proof tree, real-time primal) [S067 p. 40; S098 p. 2; S044 p. 2].
3. Prove what carries over: local stability in b, finiteness of the useful directions over the family, or a dual that is a function of Δb [S044 p. 18; S082 pp. 6, 16–17; D004 arXiv pp. 4–5].
4. Reuse the object the theorem covers, chosen for its downstream use [S044 pp. 3–4; S082 pp. 9–12; S067 pp. 9–12].
5. Score against an expert ceiling or the exact value, with collection and prediction overhead charged [S082 p. 9; D004 arXiv p. 14] (→ Method 2, Heuristic 6).
6. State the perturbation range and what is not guaranteed [S082 pp. 12–13; S044 p. 16].

**Limitations to write in**: three of the four are arXiv preprints (S044, S098, S082 per their card headers); the 2020 heuristic has no certificate and possibly infeasible output [S044 pp. 4, 16]; per-node overhead is asserted, not timed, in the branching paper [S098 p. 8]; in the oldest case the license covers only large training sets: "While it is difficult to give theoretical justification for the good performance of the KNN heuristic with the small training set, it is possible to prove that KNN can find the correct integer solution for general MIPs with a sufficiently large training set." [S044 p. 18]. Dey is third of four authors on S044, so his individual share is not identifiable [S044 pp. 1–2].

**What changes in SKILL.md**: add Method 6; remove U4 from "Claimed but unverified" (keep a pointer); in the Anti-patterns row "Restarting from scratch on repeated solves", replace "his practice: preliminary" by "→ Method 6"; add a routing row ("My MILP/MINLP is re-solved daily / hourly with new data") → Workflow B + C with Method 6.

### Considered and not promoted (08 §4)

- ***Prove the heavier relaxation adds nothing before offering the cheap one*** (S100, S041, S105, S129, S001: five works, all four checks arguably pass). Not promoted because it is M5's step 2 done by theorem; a separate method would duplicate M5. Filed as a variant (§3 row 10).
- ***One construction, both bounds: a relaxation and a restriction from the same discretisation*** (S014, D002, S051, S080: four works). Same reason: it is M5 step 4 plus M1 step 8. Filed as a variant (§3 row 11).
- **"Re-prove the classical lemma by your own route"** (seven works). Fails exclusivity; becomes a heuristic (§5).

### Added in T3.6

- **Condensed into SKILL.md**: Stated, the recurring setting [S044 pp. 1–3; S098 pp. 1–2; S082 pp. 1–2; S067 p. 2] and the question as the card records it: "What 'information' from historical data, if any, could be exploited to learn good aggregation multipliers?" [S082 p. 5]. The texts of the other three entries: "similar load profiles and generation cost profiles will likely turn off similar sets of lines" [S044 p. 1]; "significantly similar to each other" [S098 p. 1]; constraints that describe invariant physical resources while the right-hand side changes [S067 p. 2].
- **Step 2**: Gurobi near the best primal value within 60 s while its own dual gap stays above 10% at 1200 s [S067 p. 40; D004 arXiv p. 40].
- **Step 3**: "Therefore, simple perturbation can change the GMIC closure dramatically." [S082 p. 5].
- **Step 7**: perturbations within ±10% right-hand side and ±25% objective [S082 p. 13]; no feasibility guarantee in the kNN heuristic [S044 p. 16].
- **Limitations, full quote**: "While it is difficult to give theoretical justification for the good performance of the KNN heuristic with the small training set, it is possible to prove that KNN can find the correct integer solution for general MIPs with a sufficiently large training set." [S044 p. 18].
- **Routing and anatomy**: a routing row ("re-solved daily or hourly") and the anatomy [anatomy-mbqp-sensitivity](#anatomy-mbqp-sensitivity) were added; the Anti-patterns row "Restarting from scratch" now points here.

### Before T3.6

Not a method. It was U4 in the Honest Boundary, "reuse information across re-solves — practice "preliminary" (arXiv:2312.06714)", and the Anti-patterns row "Restarting from scratch on repeated solves" said "Reuse information (his practice: preliminary, arXiv:2312.06714)". Overturned by the four full texts above (08 §3 row 16):

| # | SKILL.md item | What the full texts show | Cards | Decision |
|---|---|---|---|---|
| 16 | Honest boundary U4 "reuse information across re-solves: practice 'preliminary'" | Four works built on recurring instances (§4). | [S044; S098; S082; D004 = S067] | **Overturned**: U4 leaves the unverified list and becomes Method 6 (§4). The Anti-patterns row "his practice: preliminary" changes accordingly. |

### SKILL.md Evidence block before the T3.6 review fixes (moved verbatim)

**Evidence** (full evidence: references/research/09-evidence-ledger.md#method-6):
- Stated: the recurring setting opens all four texts [S044 pp. 1–3; S098 pp. 1–2; S082 pp. 1–2; S067 p. 2]; the question as posed: "What 'information' from historical data, if any, could be exploited to learn good aggregation multipliers?" [S082 p. 5].
- Practice: a carry-over license proved before or beside the reuse: a unique optimum stays optimal near b [S044 p. 18]; finitely many useful split directions over the family [S082 pp. 6, 16–17]; rhs-parametric dual bounds [D004 arXiv pp. 4–5]; reuse aimed at the dual side [S067 pp. 2, 40; S098 p. 2].
- Say–do: ✅ stated + practised; full texts: 4 works (2020–2026, three coauthor groups), all read in full; abstract-level support [S087]. Promoted from U4 [08 §4].
- Variants/corrections:
  - ✗ The oldest case delivers a heuristic with no certificate and possibly infeasible output [S044 pp. 4, 16].
  - ⚠ Per-node overhead asserted, not timed, in the branching paper [S098 p. 8] (Heuristic 6 tension).
  - ⚠ Exclusivity is narrow: what is distinctive is the license theorem plus reuse aimed at the certificate, not learning across instances [S067 p. 7].

<a id="heuristic-1"></a>

## Heuristic 1: Make the hard instances yourself and release them

### Full-text evidence (08 §2)

- **H1 make hard instances and release them** (10 cards): new instances posted online [S051 p. 17]; a radial OPF library [S006 pp. 15–17]; generators printed in an appendix [S130 pp. 34–39].

### Added in T3.6

Pooling generator that cuts off the root LP solution, because the classical instances "are solved in a matter of seconds by BARON" [S014 pp. 22–23, 35]; new Random instances posted online [S051 p. 17]; generators printed in an appendix [S130 pp. 34–39]; a radial OPF library [S006 pp. 15–17].

### Before T3.6 (moved verbatim)

1. **Make the hard instances yourself and release them.** If public sets are solved "in a matter of seconds by BARON", scale the original generator (GPP; BoxQP n = 200, 250) or derive adversarial cases (radial OPF from MATPOWER meshes) and post them with the preprint (TreeLibrary.zip) [03 §1.2, §3.6]. Critique: radial networks are "a significant departure" from meshed ones (doi:10.1109/TPWRS.2016.2550520) [05 §2.2].

<a id="heuristic-2"></a>

## Heuristic 2: Give the strongest baseline its best shot; tabulate only the strongest

### Full-text evidence (08 §2)

- **H2 strongest baseline** (15 cards). Variant: when the strongest baseline is not run, the text says so: "We caution the reader that there are significantly more sophisticated methods for star (2-stage stochastic) problems [23]." [S104 p. 13]; "While this is a somewhat unfair comparison ... we report this result simply to show the potential improvements our new valid inequalities could offer" (from [S111 p. 26]); "we cannot and do not wish to draw conclusions regarding the performance of the spatial branch-and-bound algorithm." (from [S002 p. 12]).

### Added in T3.6

BARON 6 h on NEOS vs 1 h for the MILP heuristics, with the reason, and common tolerances [S014 p. 22]. When the strongest baseline is not run, the text says so: "We caution the reader that there are significantly more sophisticated methods for star (2-stage stochastic) problems [23]." [S104 p. 13]; [S111 p. 26]; "we cannot and do not wish to draw conclusions regarding the performance of the spatial branch-and-bound algorithm." (text of [S002 p. 12], per 08).

### Before T3.6 (moved verbatim)

2. **Give the strongest baseline its best shot; tabulate only the strongest.** Adapt the competitor's public code to the same constraints, run it under two solvers, give BARON more time and say why (6 h vs 1 h), align tolerances. Case: OPF 2016-17, pooling 2015 [03 §3.2]. Practice only; no statement found.

### T3.6 review

SKILL.md H2 again carries a say–do qualifier: the new evidence [S104 p. 13; S111 p. 26] is case-by-case cautions about a missing baseline, not a stated principle of baseline fairness.

<a id="heuristic-3"></a>

## Heuristic 3: Write dead ends into the paper in one or two sentences, with the reason

### Full-text evidence (08 §2)

- **H3 dead ends written in** (16 cards): "In preliminary tests, we implemented the algorithm WFP as described in the previous section. However, its performance was not competitive with FPorig." [S061 p. 12]; "Although, for our instances, we have not observed any lower bound improvement in SOCP/SDP relaxations by the inclusion of the valid inequalities, we obtain stronger root node relaxations in BARON." [S006 p. 22]; "However such a goal was too ambitious and we have had to considerably restrict it." [S052 p. 2].

### Added in T3.6

"In preliminary tests, we implemented the algorithm WFP as described in the previous section. However, its performance was not competitive with FPorig." [S061 p. 12]; "Although, for our instances, we have not observed any lower bound improvement in SOCP/SDP relaxations by the inclusion of the valid inequalities, we obtain stronger root node relaxations in BARON." [S006 p. 22]; row-wise variants "consistently weaker", the heaviest relaxation "too big and numerically unstable" [S051 pp. 13, 15, 16]; APOGEE, alternating LP, Cplex symmetry tuning, one sentence each [S014 pp. 21–22].

### Before T3.6 (moved verbatim)

3. **Write dead ends into the paper in one or two sentences, with the reason.** "In preliminary tests, we implemented ... However, its performance was not competitive ... In hindsight, this can be justified by" [02 §5.4; 03 §3.8]. Exception: the unflagged Strong SOCP change [03 §4.2].

<a id="heuristic-4"></a>

## Heuristic 4: Feed one line into the next: its named obstacles become the next questions, its devices and theorems the next line's tools

### Full-text evidence (08 §2, §5)

- **H4 failed line → next programme** (7 cards); widened in §5.

### H4 (widened by merge) · Feed one line into the next: its named obstacles become the next questions, and its devices and theorems become the next line's tools or explanations

The obstacle half is SKILL.md's H4. The full texts add the tool half, across lines:
- the sparse-cut packing/covering multiplicative device reused for Lagrangian hierarchy levels, credited to the sparse cutting-plane paper [S104 pp. 6, 22–29; S097 pp. 6, 22–29];
- the random-B&B proof machinery reused for dual decomposition, one lemma's proof declared the same as in the earlier B&B paper [S120 pp. 5, 9];
- MIQP-in-NP decomposition lemmas reused as a lemma bank for exact augmented Lagrangian duality [S049 pp. 5–6, 12];
- the forbidden-vertices extended formulation as the engine of a CGLP for optimality cuts [S004 pp. 4, 8, 21];
- the gas-network CVXNLP decomposition carried to water networks [S075 pp. 3, 11];
- the sparse-PSD worst-case matrices and the sparse-PCA paper reused as the example and the separation oracle of a computational paper [S048 pp. 6–8, 27–28; S035 pp. 13–14; S017];
- the own non-monotonicity theorem used to explain a negative instance and to hedge a formulation-strength claim: "It is possible that adding aggregated constraints may not benefit the branch-and-bound process." [S103 p. 12]; "the polyhedral comparisons in this section are not necessarily conclusive with respect to overall computational performance (also see Shah et al. [2026])" (from [S124 p. 13]); the theorem itself [S081 pp. 3–8, 12].

**Checks**: recurrence ✅ (≥9 works, 2016–2026); executable ✅; say–do partial (the texts cite their own earlier work as the source [S104 p. 6; S120 p. 5] but no general statement); exclusivity weak. Stays a heuristic, merged into H4 rather than added, because it explains the same programme links.

### Added in T3.6

Widened in SKILL.md from "turn a failed line's named obstacles into the next programme" to "feed one line into the next" (obstacles become questions; devices and theorems become the next line's tools or explanations). Obstacle half: density named as the obstacle of multi-row cuts in 2009 [S079 p. 8]; "the need to ask different questions" section of the 2018 review [S011 p. 7]. Tool half: [S104 pp. 6, 22–29; S120 pp. 5, 9; S049 pp. 5–6; S004 pp. 4, 8, 21; S075 pp. 3, 11; S048 pp. 6–8; S103 p. 12; S124 p. 13]. The 2009 → 2014 link of the obstacle half is still inferred, as before.

### Before T3.6 (moved verbatim)

4. **Turn a failed line's named obstacles into the next programme.** If a line fails, list the obstacles it names and make each the next question: multi-row cuts (2009: selection, density) → sparse cuts (2014) → cut selection (2018) → "the need to ask different questions" → B&B on random instances (2020) [06 T3, T8]. Two instances; the 2009 → 2014 link is inferred.

### T3.6 review

SKILL.md H4 again carries the hedge of the pre-T3.6 text: the 2009 → 2014 link of the obstacle half is inferred; no text states it.

<a id="heuristic-5"></a>

## Heuristic 5: Start from a result better than it should be

### Full-text evidence (08 §2)

- **H5 start from a result better than it should be** (2 cards): [S035 pp. 1–3; S123 p. 8].

### Added in T3.6

SKILL.md now names the sparse SDP case [S035 pp. 1–3] and the pooling MILP restriction that beat a global solver's primal side, far better than its own guarantee [S014 pp. 24–28]. 08 also lists [S123 p. 8] (extreme strong branching for QCQPs; its conclusion calls the rule particularly effective for bilinear bipartite problems).

### Before T3.6 (moved verbatim)

5. **Start from a result better than it should be.** If an empirical surprise appears (sparse SDP bounds near the full SDP, arXiv:2002.02988; a MILP heuristic beating global solvers), treat it as a Method 1 candidate [02 §3.6].

<a id="heuristic-6"></a>

## Heuristic 6: Count every overhead before claiming a speed-up; when you do not, say why

### Full-text evidence (08 §2)

- **H6 count every overhead** (10 cards): full timing [S082 pp. 9–12]; the tension is confirmed verbatim: "It is also self-evident, in our opinion, that all evaluated ML-based branching rules, if carefully implemented, would require significantly less computational effort per node than strong branching" [S098 p. 8], with the stated reason "We do not focus on total running time since this metric depends heavily on the quality of the software implementation" (from [S098 p. 8]).

### Added in T3.6

Full timing with collection cost: "completely nullifies its running time improvements" [S082 p. 12]; [S082 pp. 9–12]. The tension, verbatim on the card: "It is also self-evident, in our opinion, that all evaluated ML-based branching rules, if carefully implemented, would require significantly less computational effort per node than strong branching" [S098 p. 8], with the reason "We do not focus on total running time since this metric depends heavily on the quality of the software implementation, instead of simply on the fundamental properties of the branching rule." [S098 p. 8].

### Before T3.6 (moved verbatim)

6. **Count every overhead before claiming a speed-up; when you do not, say why.** Include prediction, tableau and cut-collection time (arXiv:2411.15090) [02 §4.3]. Tension: a 2022 preprint called the per-node saving "self-evident" without timing it [03 C5].

<a id="heuristic-7"></a>

## Heuristic 7: Follow a theory paper with a measurement-only paper

### Full-text evidence (08 §2)

- **H7 theory paper followed by a measurement-only paper** (4 cards): two-row cuts [S052 pp. 1–2]; lifted bilinear cover: theory [S085 pp. 1–7] then a computational paper whose stated entry is that the cut's computational usefulness had not been evaluated [S105 p. 4].

### Added in T3.6

Two-row cuts [S052 pp. 1–2]; lifted bilinear cover: theory [S085 pp. 1–7], then a computational paper whose stated entry is that the cut's computational usefulness had not been evaluated [S105 p. 4].

### Before T3.6 (moved verbatim)

7. **Follow a theory paper with a measurement-only paper.** "While the lifted bilinear cover inequality was derived in [12], its computational usefulness has not been evaluated." Cases: two-row cuts (doi:10.1287/ijoc.2013.0559); bilinear cover 2021 → 2024 [03 §1.3].

<a id="heuristic-8"></a>

## Heuristic 8: Bring in the specialist for the step you cannot do; credit the student who leads

### Full-text evidence (08 §2)

- **H8 specialist and student** (4 cards): Blekherman on the real-algebraic steps [S035; S055 p. 7; S077 pp. 1–2; S119 p. 1].

### Added in T3.6

Blekherman on the real-algebraic steps [S077 pp. 1–2; S119 p. 1; S055 p. 7; S035]; co-advising counts stay from web research [04 H1, H2].

### Before T3.6 (moved verbatim)

8. **Bring in the specialist for the step you cannot do; credit the student who leads.** Co-advise by domain; call the student the "thought leader" in talks. Case: 9 of 17 theses co-advised; Blekherman for real-algebraic steps [04 H1, H2; 06 T11].

<a id="heuristic-9"></a>

## Heuristic 9: Borrow one tool from a neighbouring field

### Full-text evidence (08 §2)

- **H9 borrow one tool** (13 cards): Aczél's functional equations [S019 p. 6]; WalkSAT [S105 p. 9; S061 p. 4]; Shapley–Folkman [S125 pp. 10–16]; Gaussian random projection [D005 p. 8]; Gershgorin [S105 pp. 5–7].

### Added in T3.6

WalkSAT [S061 p. 4; S105 p. 9]; Shapley–Folkman [S125 pp. 10–16]; Gaussian random projection [D005 p. 8]; Aczél's functional equations [S019 p. 6]; Gershgorin [S105 pp. 5–7].

### Before T3.6 (moved verbatim)

9. **Borrow one tool from a neighbouring field.** WalkSAT for feasibility-pump randomisation (doi:10.1137/16M1095962); restricted isometry in a PSD-closure proof; Shapley-Folkman (arXiv:2601.19003); generic chaining (arXiv:2610.09324) [02 §3.5].

<a id="folded-design-cut"></a>

## Folded heuristic (Heuristic 10 until the T3.6 review): Design the cut you want, then verify validity

The T3.6 review enforced the framework's 5–10 cap on heuristics; this one-project-line heuristic is now a Method 3 variant in SKILL.md (step 4 run backwards). Former anchor: `#heuristic-10`.

### Full-text evidence (08 §2)

- **H10 design then verify**: still one project line, now read in both versions: "First we design a useful cutting-plane without considering its validity. Then, once the cutting-plane is designed, we verify whether it is valid." [S096 p. 2]; "First we design cutting-planes which we believe will be useful without considering their validity." [S095 p. 1]; the CAREER award states it as one of three paradigms [S141]. No later project uses it in the read texts.

### Added in T3.6

Read in both versions: "First we design a useful cutting-plane without considering its validity. Then, once the cutting-plane is designed, we verify whether it is valid." [S096 p. 2]; "First we design cutting-planes which we believe will be useful without considering their validity." [S095 p. 1]; the CAREER award states it as one of three paradigms [S141] (abstract level). No later project uses it in the read texts. If the 5–10 cap on heuristics is enforced, this is the one to fold [08 §5].

### Before T3.6 (moved verbatim)

10. **Design the cut you want, then verify validity.** "First we design cutting-planes which we believe will be useful without considering their validity." (doi:10.1007/s10107-013-0645-0) [02 §3.3]. One project only.

### SKILL.md text before the fold (moved verbatim)

10. **Design the cut you want, then verify validity.** "First we design cutting-planes which we believe will be useful without considering their validity." [S095 p. 1; S096 p. 2]. One project line only; the CAREER award names it as a paradigm [S141].

<a id="heuristic-10"></a>

## Heuristic 10 (Heuristic 11 until the T3.6 review): Re-prove the classical lemma you lean on by a route that exposes the one property you use, then push past the classical statement

### Full-text evidence (08 §5)

### H11 (new) · Re-prove the classical lemma you lean on by a route that exposes the one property you use, then push the route past the classical statement

- **Evidence (7 works, 2019–2026, six coauthor groups)**: one-point fixability of mixing-set triangles, already known, re-derived by more geometric techniques to get pyramids and spindles as a reusable tool [S056 pp. 4, 8–12]; a symmetric three-quadratic S-lemma proved because the existing one is asymmetric [S071 pp. 3–4, 10–11]; hidden convexity restricted to every hyperplane so the old proof road-map extends and earlier theorems become corollaries [S077 pp. 4–6, 16–17]; the Boolean-quadric eigenvector family re-derived through CG rounding, yielding a new hierarchy [S122 pp. 3, 7–9]; a face-dimension proof of Shapley–Folkman pushed to a vanishing bound [S125 pp. 10–16]: "To the best of our knowledge, this is the first result establishing an asymptotically vanishing nonconvexity measure for Minkowski sums of nonconvex sets within the framework of the Shapley–Folkman Lemma." [S125 p. 4]; the treewidth LP re-proved through LP duality: "The dual to the LP is the DP formulation for solving such problems over known tree decompositions." [S153 p. 5]; random projection redesigned around the property the proof needs: "Our key observation is that the JL lemma itself is not essential for preserving bilinear structures." [D005 p. 8].
- **Steps**: (1) write down which property of the classical lemma your proof actually touches; (2) re-prove it by a device that isolates that property (geometric, LP-dual, face-dimension); (3) restate the hypothesis as that property; (4) push the device one step past the classical bound and recover the old results as corollaries.
- **Checks**: recurrence ✅; say–do ✅ (stated in the texts [D005 p. 8; S071 pp. 3–4; S153 p. 5]); executable ✅; exclusivity ✗ (common in mathematics; and the MIQP-in-NP paper does the opposite, keeping both classical proofs as black boxes [S003 pp. 1, 3]). → heuristic.

### Added in T3.6

New in T3.6 from 08 §5. SKILL.md cites [D005 p. 8; S071 pp. 3–4; S125 p. 4]. Further: one-point fixability of mixing-set triangles re-derived geometrically [S056 pp. 4, 8–12]; hidden convexity restricted to every hyperplane [S077 pp. 4–6, 16–17]; the Boolean-quadric eigenvector family re-derived through CG rounding [S122 pp. 3, 7–9]; "The dual to the LP is the DP formulation for solving such problems over known tree decompositions." [S153 p. 5]; "To the best of our knowledge, this is the first result establishing an asymptotically vanishing nonconvexity measure for Minkowski sums of nonconvex sets within the framework of the Shapley–Folkman Lemma." [S125 p. 4]. Counter-case: the MIQP-in-NP paper keeps both classical proofs as black boxes [S003 pp. 1, 3].

### Before T3.6

New in T3.6 (no earlier item).

<a id="anatomy-sparse-cuts"></a>

## Anatomy: Sparse cuts → cut-selection review → branch-and-bound theory (2014-2023)

### As in SKILL.md (T3.6)

doi:10.1007/978-3-319-07557-0_22 (IPCO 2014) → doi:10.1007/s10107-015-0925-y → doi:10.1287/moor.2017.0866 → doi:10.1007/s10107-018-1302-4 (2018 review) → doi:10.1007/s10107-022-01895-4 (arXiv:2007.15192). Full rows: references/research/09-evidence-ledger.md#anatomy-sparse-cuts.

| Dimension | Content |
|---|---|
| Origin | Solvers prefer sparse cuts; "Surprisingly, very few studies have been conducted on the topic of sparse cutting-planes." [S084 p. 1] |
| Key insight | Keep one side of the trade-off: distance of a polytope from its k-sparse closure, measure fixed first after discarding ratios that can be infinite [S084 p. 2] |
| Minimum evidence | Vertex-count upper bounds, near-matching random lower bounds, a packing class where sparse cuts fail [S084 pp. 4–5]; PORTA on n = 10 before the theory [S084 p. 17] |
| Abandoned paths | Objective and volume ratios discarded on the page [S028 p. 2]; worst-case cut theory as a route to selection: "these results have so far failed to directly help in actual cutting-plane selection." [S011 p. 20] |
| Reception | Balas Prize 2020; "breakthrough work" (doi:10.1007/s10107-022-01828-1) [05 §6]; cut selection still open in his 2024 slide |
| Methods shown | Method 1, Method 4, Heuristic 4 |

### Full rows from the cards (T3.6)

| Dimension | Full row |
|---|---|
| Origin | Solver habit backed by personal communications from Achterberg, Gu and Narisetty [S084 p. 1]; the real question (faster LPs vs weaker gap closure) is "challenging to simultaneously study", so one side is kept [S084 p. 2]; funded by the CAREER award [S084 p. 1] |
| Key insight | P^k as the intersection of all k-sparse valid cuts; the objective-value ratio discarded because it can be infinite, the volume ratio because P may be lower-dimensional; the distance d(P, P^k) is defined for every polytope in the cube [S084 p. 2; S028 p. 2] |
| Minimum evidence | Upper bounds in the number of vertices; random 0/1 lower bounds matching up to log factors; packing IPs where sparse cuts fail; extended formulations where 3-sparse cuts suffice [S084 pp. 4–6]; PORTA on n = 10 with 20,000 random directions as a one-sided bound [S084 p. 17]; MOR 2018: sparse closure within the fractional chromatic number of the interaction graph, factor 2 for two-stage stochastic [S011 pp. 16–17; S024 pp. 5–9] |
| Abandoned paths | Measures discarded on the page [S084 p. 2; S028 p. 2]; "Our main observation is the sparse cuts usually perform much better than the worst-case bounds we obtain theoretically." (text of [S024 p. 4]); the review admits the results "have so far failed to directly help in actual cutting-plane selection" [S011 p. 20] and are "very preliminary" [S011 p. 21] |
| Reception | Unchanged from the web research [05 §6] |
| Methods shown | Method 1 (the full loop), Method 4 (upper and lower bounds, negative class), Method 2 weakly (PORTA), Heuristic 4 ("the need to ask different questions" [S011 p. 7]) |

### Before T3.6 (moved verbatim)

doi:10.1007/978-3-319-07557-0_22 (IPCO 2014) → doi:10.1007/s10107-015-0925-y → doi:10.1287/moor.2017.0866 → doi:10.1007/s10107-018-1302-4 (2018 review) → doi:10.1007/s10107-022-01895-4 (arXiv:2007.15192).

| Dimension | Content |
|---|---|
| Origin | Solvers prefer sparse cuts; "Surprisingly, very few studies have been conducted on the topic of sparse cutting-planes." [01 §2.4]. Who posed it first: unknown |
| Key insight | Replace the two-sided sparsity trade-off by a one-sided geometric question: distance of a polytope from its best k-sparse outer approximation |
| Minimum evidence | Vertex-count upper bounds, random-polytope lower bounds, a packing class where sparse cuts fail |
| Abandoned paths | Objective and volume ratios discarded on the page; worst-case cut theory as a route to cut selection (Inner Tensions) [02 §1.1] |
| Reception | Balas Prize 2020; "breakthrough work" (doi:10.1007/s10107-022-01828-1) [05 §6]; cut selection still open in his 2024 slide |
| Methods shown | Method 1, Method 4, Heuristic 4 |

<a id="anatomy-pooling"></a>

## Anatomy: Pooling: MILP relaxations and restrictions with guarantees (2013-2017)

### As in SKILL.md (T3.6)

doi:10.1137/110836183 (SIAM J. Optim. 2013); doi:10.1287/opre.2015.1357 (Oper. Res. 2015); doi:10.1007/s10898-016-0434-4 (J. Glob. Optim. 2017). Full rows: references/research/09-evidence-ledger.md#anatomy-pooling.

| Dimension | Content |
|---|---|
| Origin | PL MILP relaxations work, but "no formal result regarding the quality of these relaxations is known" [S014 p. 1]; ExxonMobil support [S014 p. 29] |
| Key insight | Relax the relaxation (drop the coupling variables), keep one output: factor n, tight for every PL scheme; the proof's feasible point becomes an MILP restriction that inherits the guarantee [S014 pp. 6–8, 14–16] |
| Minimum evidence | Inapproximability [S014 p. 12]; 70 instances, BARON 6 h vs 1 h [S014 pp. 21–23]; practice "significantly better than the theoretical performance guarantee of n" [S014 p. 28] |
| Abandoned paths | APOGEE, alternating LP and solver symmetry tuning, one sentence each [S014 pp. 21–22] |
| Reception | Replicated twice by Misener's group, who note it "does not apply to pooling variants" (doi:10.1002/aic.15308; doi:10.1016/j.compchemeng.2022.107660) |
| Methods shown | Methods 1, 4, 5 (restriction as primal side); Heuristics 1, 2, 3 |

### Full rows from the cards (T3.6)

| Dimension | Full row |
|---|---|
| Origin | Empirical regularity without theory [S014 pp. 1, 5]; the object defined as a whole class of PL relaxation schemes [S014 p. 4]; ExxonMobil support, Ahmed and Cheon thanked [S014 p. 29] |
| Key insight | IPOP: drop q and every constraint containing it, send all flow to the most profitable output, so z_pq ≤ n z* [S014 pp. 7–8]; tightness for every PL scheme by a finiteness argument on the slopes [S014 pp. 8–11]; the n-approximation becomes an MILP restriction PQ(τ, λ) containing all its outputs [S014 pp. 12, 14–16] |
| Minimum evidence | n^{1−ε} inapproximability via an approximation-preserving reading of a known reduction [S014 pp. 12–13]; 20 Alfaki–Haugland + 50 generated instances, Cplex 1 h single-thread vs BARON 6 h on NEOS, common tolerances [S014 pp. 21–23]; profiles split at n ≥ 30 [S014 pp. 24–26] |
| Abandoned paths | APOGEE, alternating-LP variants and Cplex symmetry tuning reported in a sentence each [S014 pp. 21–22]; numbered open questions on fixed numbers of specifications and better-than-n restrictions [S014 pp. 27–28] |
| Reception | Unchanged from the web research (Misener's group) |
| Methods shown | Method 1 (step 8 closed), Method 4 (two-sided theorems), Method 5 variant (the certificate is BARON's [S014 pp. 26, 28]), Heuristics 1, 2, 3 |

### Before T3.6 (moved verbatim)

doi:10.1137/110836183 (SIAM J. Optim. 2013); doi:10.1287/opre.2015.1357 (Oper. Res. 2015); doi:10.1007/s10898-016-0434-4 (J. Glob. Optim. 2017).

| Dimension | Content |
|---|---|
| Origin | ExxonMobil-funded; student Gupte's internship [01 §2.2; 04 H5]. How contact began: unknown |
| Key insight | Piecewise-linear MILP relaxations are within a factor n, tightly; beating that is hard; an MILP restriction attains it |
| Minimum evidence | "For 19 out of the 20 Alfaki et al. instances, MILP heuristic produces the best known results." (slides p. 111) |
| Abandoned paths | Experiment-level only (APOGEE, SNOPT warm starts) [03 §3.8] |
| Reception | Replicated twice by Misener's group, who note it "does not apply to pooling variants" (doi:10.1002/aic.15308; doi:10.1016/j.compchemeng.2022.107660) |
| Methods shown | Methods 1, 4; Heuristics 1, 2 |

<a id="anatomy-opf"></a>

## Anatomy: AC optimal power flow: Strong SOCP relaxations (2014-2018)

### As in SKILL.md (T3.6)

doi:10.1109/TPWRS.2015.2402640 (arXiv:1410.1004) → doi:10.1287/opre.2016.1489 (arXiv:1504.06770) → doi:10.1109/TPWRS.2017.2666718 → doi:10.1007/s12532-018-0150-9. Full rows: references/research/09-evidence-ledger.md#anatomy-opf.

| Dimension | Content |
|---|---|
| Origin | Testing a fresh SDP exactness claim [06 T6; S006 pp. 1–3]; the classic SOCP drops the angle constraints [S001 p. 3]. Carried by Kocuk with co-advisor X. A. Sun |
| Key insight | Rank six relaxations in one projected space [S001 pp. 11–14], then strengthen the SOCP with cycle constraints, arctangent envelopes and cycle-SDP cuts [S001 pp. 15–24] |
| Minimum evidence | Complete classification on the two-bus system [S006 pp. 6–11]; 3375 buses, 0.13% in 157.20 s on a laptop [S001 pp. 1, 26–29] |
| Abandoned paths and corrections | v1 "exact reformulation" → v4 "relaxation", no note [03 §4.2] (only v4 carded [S001]); the SDP comparison conceded in the 2015 arXiv v4 of the 2016 paper [S001 p. 30] |
| Reception | Most cited; INFORMS ENRE 2019; inexactness accepted by rivals; scale critiques (Method 5) [05 §3] |
| Methods shown | Methods 3, 5; Heuristics 1, 2 |

### Full rows from the cards (T3.6)

| Dimension | Full row |
|---|---|
| Origin | OPF is "solved every few minutes" and DC OPF cannot guarantee optimality [S001 pp. 1–2]; the classic SOCP of Jabr's formulation drops the arctangent constraints [S001 p. 3]; the SDP inexactness line first [S006 pp. 1–3, 6–11] |
| Key insight | Six relaxations ranked in the projected (p, q) space by a theorem with strictness examples [S001 pp. 11–14]; cycle constraints triangulated into 3- and 4-cycles and relaxed by McCormick, four-plane arctangent envelopes, cycle-SDP separation, 2-hop bound tightening [S001 pp. 15–25] |
| Minimum evidence | Two-bus classification [S006 pp. 6–11]; MATPOWER and NESTA up to 3375 buses, laptop with 8 GB, five cut rounds, gap against IPOPT with the local solve timed [S001 pp. 26–29]; load-perturbation robustness [S001 p. 33] |
| Abandoned paths and corrections | Web-research corrections kept (v1 → v4 claim change, not re-read [S001]); SDP tight on more instances, conceded in the text [S001 p. 30]; spatial branch-and-cut promised as future work [S001 p. 35] and delivered in [S008 pp. 19–27] |
| Reception | Unchanged from the web research [05 §3] |
| Methods shown | Method 5 (template), Method 3 (cycle substructure), Method 4 variant (strictness by computed instances [S001 pp. 13–14]) |

### Before T3.6 (moved verbatim)

doi:10.1109/TPWRS.2015.2402640 (arXiv:1410.1004) → doi:10.1287/opre.2016.1489 (arXiv:1504.06770) → doi:10.1109/TPWRS.2017.2666718 → doi:10.1007/s12532-018-0150-9.

| Dimension | Content |
|---|---|
| Origin | Testing a fresh claim: "It has been recently proven that the semidefinite programming (SDP) relaxation ... over radial networks is exact in the absence of generation lower bounds" (arXiv:1410.1004) [06 T6]. Carried by student Kocuk with co-advisor X. A. Sun |
| Key insight | Rank McCormick / SOCP / SDP, then strengthen the SOCP with cycle structure |
| Minimum evidence | Two-bus example; 0.13% certified gap in 157.20 s on a PC |
| Abandoned paths and corrections | BARON on the rectangular formulation ("requires hours"); "add cuts to BARON" plan [01 §2.1]. Claim change: v1 "This is an exact reformulation of the AC OPF problem." → v4 "valid bilinear extended relaxation", no note [03 §4.2]; Shao 2020: "was only proven to be a relaxation. Here, we impose additional linear constraints and establish equivalence." [05 §1.4] |
| Reception | Most cited; INFORMS ENRE 2019; inexactness accepted by rivals; scale critiques (Method 5) [05 §3] |
| Methods shown | Method 5; Heuristics 1, 2 |

<a id="anatomy-qcqp"></a>

## Anatomy: QCQP rank-one substructures and aggregations of quadratics (2019-2024)

### As in SKILL.md (T3.6)

doi:10.1137/19M1277333; doi:10.1007/s10898-019-00844-4; doi:10.1137/21M1428583; doi:10.1137/22M1528215. Full rows: references/research/09-evidence-ledger.md#anatomy-qcqp.

| Dimension | Content |
|---|---|
| Origin | FEM model updating with "Commercial solvers (for hours)" [06 T9]; pooling's rank-1 lift [S051 p. 2]; the aggregation ladder (Farkas, two quadratics, three?) [S071 p. 1] |
| Key insight | Under a positive-definite combination, the hull of three quadratics is the intersection of aggregations, via a new symmetric S-lemma [S071 pp. 3–4] |
| Minimum evidence | A counterexample for each dropped hypothesis [S071 pp. 17–24]; pooling LP gap 18.65 → 3.82 on real Mining instances [S051 p. 19] |
| Abandoned paths | Row-wise variants "consistently weaker"; heaviest relaxation too big [S051 pp. 13, 15–16] |
| Reception | Modest counts; in-house follow-ups (hidden hyperplane convexity) [S077 pp. 1–2, 27; 05 §2.12] |
| Methods shown | Methods 3, 4; Heuristics 8, 11 |

### Full rows from the cards (T3.6)

| Dimension | Full row |
|---|---|
| Origin | Lifted QCQP: the rank-1 condition carries all nonconvexity; only the boolean quadric case had been studied as a side-constraint family [S051 p. 2]; aggregation complete for linear systems (Farkas) and two quadratics (Yildiran), open for three [S071 p. 1] |
| Key insight | Rank-1 sets with side constraints: extreme points of small support, hull = union of small-support SOCr pieces [S051 pp. 3–7]; three quadratics: a symmetric S-lemma by SDP duality plus rank reduction (Barvinok or Pataki) [S071 pp. 3, 10–11] |
| Minimum evidence | Counterexamples: four quadratics, PDLC failing, SDP not tight although aggregations give the hull, infinitely many aggregations [S071 pp. 17–24]; pooling: 24 Mining, 12 literature and 24 new Random instances; LP gap 18.65 → 3.82 on Mining [S051 pp. 17–19] |
| Abandoned paths | Row-wise variants "consistently weaker"; F^ST_2 "too big and numerically unstable" [S051 pp. 13, 15, 16]; preprint retitled [01 §2.5] |
| Reception | In-house follow-up: hidden hyperplane convexity with Blekherman [S077 pp. 1–2, 27]; aggregation of bilinear bipartite equalities [S103 pp. 2–5, 11] |
| Methods shown | Method 3, Method 4 (simple rigorous box [S071 p. 18]), Heuristics 8, 11 (symmetric S-lemma) |

### Before T3.6 (moved verbatim)

doi:10.1137/19M1277333; doi:10.1007/s10898-019-00844-4; doi:10.1137/21M1428583; doi:10.1137/22M1528215.

| Dimension | Content |
|---|---|
| Origin | CRM 2019 slides: FEM bridge model updating, "Need to obtain good dual bounds", "Commercial solvers (for hours)", plus the MILP substructure habit (Method 3) [06 T9] |
| Key insight | Under a stated condition, the closed convex hull of three quadratics is the intersection of their aggregations |
| Minimum evidence | "This substructure convexification worked well" against BARON "Running-time: 10 hours." [02 §2.2] |
| Abandoned paths | Row-wise extended relaxation "consistently weaker and hence omitted"; preprint retitled from pooling to general QCQP (reason unknown) [01 §2.5] |
| Reception | Modest counts; in-house follow-ups narrow the conjecture and improve the relaxations [05 §2.12] |
| Methods shown | Methods 3, 4; Heuristic 8 |

<a id="anatomy-branching"></a>

## Anatomy: Full strong branching and non-monotonicity (2024-2026)

### As in SKILL.md (T3.6)

doi:10.1007/s10107-023-01977-x (arXiv:2110.10754) [S020]; doi:10.1287/ijoc.2024.0709 (arXiv:2402.05213) with code doi:10.1287/ijoc.2024.0709.cd [S081]. Full rows: references/research/09-evidence-ledger.md#anatomy-branching.

| Dimension | Content |
|---|---|
| Origin | "However, to the best of our knowledge there is no understanding of how good strong-branching is in absolute terms." [S020 p. 3]; the founding assumption that tighter relaxations give smaller trees [S081 pp. 1–2] |
| Key insight | Measure strong branching against exactly optimal trees by DP [S020 pp. 11, 21–22]; remove confounders, then prove tighter relaxations can enlarge trees exponentially [S081 pp. 2, 4–8] |
| Minimum evidence | "within a factor of two of the size of the optimal branch-and-bound tree" [S020 p. 1]; naive Python B&B and stripped SCIP: non-monotonicity "surprisingly common in practice" [S081 pp. 8–11] |
| Abandoned paths | Own hypothesis rejected on the data [S020 p. 13]; `LearningFromOptimalTrees/` and `ImprovingStrongBranching/` deleted from the student repo [03 §6] |
| Reception | Published; no external critique found |
| Methods shown | Methods 1, 2, 4 (the instrument belongs to S081, not S020) |

### Full rows from the cards (T3.6)

| Dimension | Full row |
|---|---|
| Origin | Strong branching is imitated by learning-to-branch work but never measured "in absolute terms" [S020 p. 3]; non-monotonicity: a branching rule uses local LP information, so a tighter formulation need not give the same tree [S081 pp. 1–2] |
| Key insight | S020: vertex-cover tree bound 2^{2Γ+2} + O(n), tight and matching the FPT algorithm; a DP over 3^n faces for optimal trees [S020 pp. 6, 11, 14–15, 21–22]. S081: confounders removed (dual degeneracy, node selection), then every fractional-only rule is non-monotone and one cut can enlarge the strong-branching tree exponentially [S081 pp. 2–8] |
| Minimum evidence | Ten classes × 100 instances, ≤ 20 binaries; geometric means: optimal 42.65, strong branching about 61 [S020 pp. 11–13, 29]; word of caution on extrapolation [S020 p. 13]. S081: 100 knapsacks in a naive Python B&B with Gurobi as LP solver, then 21 filtered MIPLIB 2017 instances in SCIP 8.0 with 3 seeds [S081 pp. 8–11] |
| Abandoned paths | S020 tests and rejects its own hypothesis (more integer branchings → worse strong branching) [S020 p. 13]; deleted student folders [03 §6] |
| Correction | The pre-T3.6 anatomy credited the naive Python B&B, stripped SCIP and non-monotonicity to doi:10.1007/s10107-023-01977-x; they are in the IJOC paper [S081 pp. 8–11] (S020 card, method links) |
| Methods shown | Methods 1, 2, 4 |

### Before T3.6 (moved verbatim)

doi:10.1007/s10107-023-01977-x (arXiv:2110.10754); doi:10.1287/ijoc.2024.0709 with code doi:10.1287/ijoc.2024.0709.cd.

| Dimension | Content |
|---|---|
| Origin | "to the best of our knowledge there is no understanding of how good strong-branching is in absolute terms"; folklore that tighter formulations give smaller trees [02 §2.1] |
| Key insight | Measure strong branching against exactly optimal trees; show tighter relaxations can enlarge trees, and how often |
| Minimum evidence | "within a factor of two of the size of the optimal branch-and-bound tree"; non-monotonicity "surprisingly prevalent in practice" |
| Abandoned paths | `LearningFromOptimalTrees/` and `ImprovingStrongBranching/` deleted from the student repo the day it was created [03 §6] |
| Reception | Published; no external critique found |
| Methods shown | Method 2 (DP ground truth, naive Python B&B, stripped SCIP, word of caution, code defects kept) |

<a id="anatomy-miqp-np"></a>

## Anatomy: Mixed-integer quadratic programming is in NP (2017)

Moved out of SKILL.md in the T3.6 review (two rows were empty and the content duplicates Method 4's practice line, which now carries the exemplar).

### As in SKILL.md (T3.6, before the review)

doi:10.1007/s10107-016-1036-0 (arXiv:1407.4798), with Del Pia and Molinaro [S003]. Full rows: references/research/09-evidence-ledger.md#anatomy-miqp-np.

| Dimension | Content |
|---|---|
| Origin | QP and ILP are each in NP; MIQP, which contains both, had no membership proof [S003 p. 1] |
| Key insight | Split into polytope-plus-integer-cone pieces, refine cones until zero-curvature directions are extreme rays, analyse along rays, call the QP result [S003 pp. 3–9] |
| Minimum evidence | The theorem on p. 2 and three counterexamples on pp. 2–3: "tight with respect to the number of quadratic inequalities." [S003 p. 3] |
| Abandoned paths | None in the text; the size polynomial is not made explicit [S003 p. 2] |
| Reception | Not examined on the cards; citation context in [01 §2.3] |
| Methods shown | Methods 4, 3 |

### Full rows from the cards (T3.6)

| Dimension | Full row |
|---|---|
| Origin | QP ∈ NP (Vavasis) and ILP ∈ NP were known; MIQP, which contains both, had no membership proof; the open question beyond is fixed-dimension IQP [S003 p. 1]: "This result generalizes and unifies classical results that quadratic programming is in NP [11] and integer linear programming is in NP [1, 12, 4, 9]." [S003 p. 1] |
| Key insight | Decompose into P_i + int.cone(R_K) pieces affinely isomorphic to Z^n′_+ (which also gives MIP ∈ NP); normalizing hyperplane; recursive cone refinement until every zero-curvature face has a zero-curvature extreme ray; one-dimensional analysis along rays; Vavasis for the continuous part [S003 pp. 3–9] |
| Minimum evidence | Main theorem on p. 2, NP-hardness via max-cut [S003 p. 2]; three counterexamples, each dropping one hypothesis: many quadratics (undecidable), two quadratics (Pell-type, exponential size), many convex quadratics (exponential size) [S003 pp. 2–3] |
| Abandoned paths | None in the text; the size polynomial is not made explicit [S003 p. 2] |
| Writing | Nine pages of text; the main theorem before any preliminaries; the boundary paragraph right after it [S003 pp. 2–3] |
| Methods shown | Method 4 (strong), Method 3 (asked of MIQP whether it is in NP, as for MILP [S003 pp. 3–4]) |

### Before T3.6

New in T3.6 (no earlier anatomy).

<a id="anatomy-mbqp-sensitivity"></a>

## Anatomy: Sensitivity analysis for mixed binary quadratic programs (2024-2026)

### As in SKILL.md (T3.6)

doi:10.1007/978-3-031-59835-7_33 (IPCO 2024) → doi:10.1007/s10107-025-02265-6 (arXiv:2312.06714), with Cifuentes and Xu [D004 = S067]. Full rows: references/research/09-evidence-ledger.md#anatomy-mbqp-sensitivity.

| Dimension | Content |
|---|---|
| Origin | MBQPs re-solved with the same matrix; solvers find primal solutions fast but not matching dual bounds [S067 pp. 2, 40]; classical IP sensitivity is trivial for binaries [D004 arXiv p. 2] |
| Key insight | The copositive dual of the completely positive reformulation gives rhs-parametric dual bounds by weak duality; pick the dual inside the ε-optimal face for the target Δb range [D004 arXiv pp. 4–5, 9–12] |
| Minimum evidence | Hardness of approximating the change, strong-duality map with a gap example and non-attainment [S067 pp. 3–8]; every bound scored against the exact value [D004 arXiv p. 14] |
| Abandoned paths | None stated; the DNN restriction has no guarantee, instance size limited by the SDP solver [D004 arXiv p. 36] |
| Reception | Published in Math. Program. 2026; no external critique found |
| Methods shown | Methods 6, 4, 5 |

### Full rows from the cards (T3.6)

| Dimension | Full row |
|---|---|
| Origin | Operational MBQPs re-solved with the same matrix and changing rhs; good primal solutions fast, dual bounds stuck (Appendix A) [S067 pp. 2, 40]; classical IP sensitivity relies on an ∞-norm that is constant on binaries [D004 arXiv p. 2] |
| Key insight | The copositive dual of Burer's completely positive reformulation gives rhs-parametric dual bounds by weak duality [D004 arXiv pp. 4–5]; the ε-optimal dual set is never a singleton and the choice matters, so a dual is searched inside it with weights equal to the average predicted bound over the target Δb range [D004 arXiv pp. 9–12] |
| Minimum evidence | Approximating the change is NP-hard [D004 arXiv p. 3]; strong-duality map: conditions, a gap example, non-attainment, and local stability whose hypotheses "cannot be further relaxed" [D004 arXiv pp. 5–8]; five generated classes, bounds scored against the exact z(b + Δb), normalised by one baseline [D004 arXiv pp. 12–14] |
| Abandoned paths | None stated; limits written: instance size "limited by the SDP solver", no guarantee for the S₊ + S_P restriction [D004 arXiv p. 36] |
| Reception | IPCO 2024, then Math. Program. 2026; the three authors contributed equally [D004 arXiv p. 1] |
| Methods shown | Method 6 (license + reuse aimed at the dual), Method 4, Method 5 variant (DNN/SDP restriction [D004 arXiv pp. 11, 13–14]) |

### Before T3.6

New in T3.6 (no earlier anatomy).

<a id="anti-patterns"></a>

## Research anti-patterns

### Added in T3.6

- **Over-interpreting small studies**: the sentence is on the strong-branching preprint's p. 13 [S020 p. 13].
- **Facetness or depth of cut**: dates added: extremality and a merit index were his own yardsticks in 2010 [S019 pp. 6, 20]; doubt from 2018 [S011 pp. 7–8]; expressive power vs algorithm [S117 p. 32]; depth used as a proxy in 2026, conclusion still for sparse structured cuts [S122 pp. 4, 12–14, 22].
- **Selection rule in the loop**: the sentence is in the two-row paper [S052 p. 10]; one round, no selection [S052 pp. 9–15].
- **Overhead**: [S082 p. 12].
- **Restarting from scratch**: "Instead" changed from "Reuse information (his practice: preliminary, arXiv:2312.06714)" to Method 6 (08 §3 row 16).

### Before T3.6 (moved verbatim)

| Anti-pattern | Why he opposes it (source) | Instead |
|---|---|---|
| Guarantees resting on unverifiable data assumptions | "make very strong and often unverifiable assumptions on the problem data" (2019 SPCA talk p. 4) | Dual bound from a relaxation (Method 5) |
| Over-interpreting small computational studies | "a word of caution regarding over-interpreting the computational results above" (strong-branching preprint p. 13) | Instance ladder plus written limit (Method 2) |
| Facetness or depth of cut as proxies for usefulness | "casts doubts on whether being a facet-defining inequality is really useful"; "Maximize depth of cut ... Not always the best" [02 §1.5] | A measure tied to the use (Method 1 step 4) |
| Measuring cut strength with a selection rule in the loop | "might prevent us from understanding the real strength of the cuts" (doi:10.1287/ijoc.2013.0559 p. 10) | One round, no selection |
| Speed-ups that ignore overhead | "completely nullifies its running time improvements" (arXiv:2411.15090 p. 12) | Heuristic 6 |
| Restarting from scratch on repeated solves | "they just restart from scratch and you shouldn't really be doing that" (MIP International 2024) | Reuse information (his practice: preliminary, arXiv:2312.06714) |
| Over-reading a negative result about a strong method | "Our work only serves to demonstrate the limitations of SDP relaxations" (arXiv:1410.1004 §7) | State the scope of the negative |

<a id="trajectory"></a>

## Research trajectory

### Full-text view (08 §8)

### 8.1 Topics by period (full + partial cards / all cards)

| Topic | 2007–2010 | 2011–2015 | 2016–2020 | 2021–2026 | undated |
|---|---|---|---|---|---|
| MILP group relaxations, lifting, multi-row cuts | 8/13 | 4/4 | 1/1 | — | 0/1 |
| Closures of convex and conic integer sets | 0/2 | 10/12 | 2/2 | 1/1 | — |
| Sparse cuts, cut selection, aggregation closures | — | 3/3 | 5/6 | 2/2 | — |
| Pooling and bilinear programs | — | 2/4 | 5/5 | 5/5 | — |
| QCQP convexification and conic relaxations | — | — | 1/1 | 7/7 | 1/2 |
| Power systems (OPF, switching, security) | — | — | 7/7 | 5/6 | — |
| B&B theory, branching, primal-heuristic theory | — | — | 1/1 | 8/8 | — |
| Statistics and ML through MIP | — | — | 4/5 | 9/9 | 0/1 |
| Duality, decomposition, stochastic IP | — | — | 4/4 | 10/10 | — |
| Network design and other OR applications | — | 5/6 | 3/3 | 6/8 | 1/4 |
| Editorials, out-of-field, misattributed | — | 0/3 | 1/1 | 2/5 | 0/2 |

(Topic tags assigned by title and card content; one tag per card.)

### 8.2 Turns

1. **From group-relaxation theory to closures of convex sets (2010–2014).** The MILP closure question is asked of strictly convex and then compact convex sets, each step naming the obstacle the next removes [S018 p. 2; S042 pp. 1–2; S025 pp. 2–3; D001 p. 2]; Wolsey's account of the CORE period [S079 p. 9].
2. **Exit from computational multi-row cuts (2014).** [S052 pp. 2, 25]; density named as the obstacle in 2009 [S079 p. 8].
3. **Into pooling and bilinear MINLP (2013–2017), back in 2020–2026 as rank-one and QCQP convexification.** [S002 pp. 2, 8–12; S014 pp. 1, 5–6; D002 pp. 2, 12–15] → [S051 pp. 1–9; S032 p. 2; S071 pp. 1–5; S077 pp. 1–2; S129 pp. 1–2]; the 2026 water-network paper continues the pooling line [S109 pp. 2, 10–14].
4. **Power systems (2016–2018), return 2022–2026.** [S006 pp. 1–3; S001 pp. 1–4; S009 p. 3; S005 p. 2; S008 pp. 5–18] → [S062 pp. 2, 4–11; S058 pp. 1, 11; S047 pp. 3, 9–11; S080 pp. 2–3].
5. **Worst case → random instances (2020–2026).** [S031 p. 2; D003 pp. 1–3; S120 p. 1].
6. **Cut theory → solver rules (2018, 2024–2025).** [S061 pp. 12–13; S082 p. 6; S130 pp. 2, 8, 20]: "one of the motivations for this paper is to discover simple rules that can improve over FSB, which can then be used as expert for machine learning algorithms to imitate." (from [S130 p. 2]).
7. **Facets as yardstick → doubt about yardsticks (2010 → 2018–2026).** [S019 pp. 6, 20] → [S011 pp. 18–19; S117 p. 32; S122 p. 22].
8. **Duality and decomposition with a student (2024–2026).** [S097 pp. 2–5; S117 p. 2; S120 pp. 1–4; S125 pp. 1–4; D005 pp. 1–2; S112 pp. 1–5].
9. **Network design with Sahinidis (2024–2026).** Primal-side frameworks with the dual bound from a global solver [S059 pp. 9–15; S075 pp. 1, 11, 23; S109 pp. 2, 17–19].

### 8.3 What stayed constant

- Demarcation of each theorem, in every period [S013 pp. 8–9; S033 pp. 4–5; S014 pp. 6–20; S003 pp. 2–3; S071 pp. 5–9; S118 pp. 2–4] (M4).
- MILP ideas as the template for each new class [S018 p. 2; S037 pp. 2–3; S003 pp. 3–4; S041 p. 2; S105 pp. 1–2; S122 pp. 2–5] (M3).
- Sparsity and decomposability as the structure to analyse [S024 pp. 5–9; S061 pp. 3, 12; S104 pp. 2, 9; S122 p. 22].
- The dual bound as the thing missing in applications [S017 p. 1; S060 p. 27; S083 p. 1; S111 p. 2; S067 p. 2].

### Collaboration pattern (08 §9)

Counts are full or partial cards naming the coauthor (version pairs counted twice here).

| Period | Main coauthors (cards) | Pattern |
|---|---|---|
| 2007–2010 | Richard 4 [S019; S026; S046; S072]; Wolsey 3 [S013; S016; S053] | Advisor and postdoc host; group-relaxation theory. |
| 2011–2015 | Vielma 5 and Dadush 4 (closures) [S018; S042; D001; S025; S037]; Ahmed 5 [S002; S010; S022; S091; S070]; Molinaro 3 (sparse cuts) [S084; S028; S065]; Morán 3 [S043; S037; S029]; Angulo 3 [S022; S091; S070] | A closure-theory partnership, the junior-faculty mentor on applied IP, and the start of the Molinaro partnership. |
| 2016–2020 | Molinaro 8 [S003; S021; S011; S024; S061; S088; S039; S099]; Kocuk 6 and X. A. Sun 5 (OPF) [S001; S006; S009; S005; S008; S051]; Ahmed 6 [S004; D002; S044; S078; S040; S049]; Del Pia 4; G. Wang 4; Santana 4 [S032; S051; S073; S041] | Theory with Molinaro; applications carried by students co-advised with a domain colleague. Ahmed's last papers here; he is marked deceased at submission on the 2020 heuristic paper [S044 p. 1]. |
| 2021–2026 | Molinaro 8 [S031; S035; D003; S020; S081; S120; S034; S057]; Xu 8 [D004; S097; S104; D005; S067; S118; S120; S125]; Shah 5 [S020; S130; S081; S121; S086]; Dubey 4; Blekherman 4 [S035; S055; S077; S119]; Muñoz 4; Gu 4; Cifuentes 4; Sahinidis 5 incl. one editorial and one undated note [S059; S075; S109; S094; S153]; Qiu and Xavier 3 (Argonne) [S098; S047; S082] | Molinaro remains the constant theory partner (19 cards, 2014–2026). Students lead the duality (Xu), branching (Shah, Dubey) and QCQP/FEM (Han, Y. Wang [S103; S123]) lines. Mathematicians are brought in for real-algebraic steps (Blekherman). Former students return as coauthors (Kocuk [S129; S119]; Morán [S112; S118]; Angulo [S117]). |

Students as first authors or carrying the line, as the cards record them: Gupte [D002 p. 1], Kocuk [S009; S005], Johnson [S044 pp. 1–2], Xu [D004 arXiv p. 1], Dubey [D003], Redder [H001], Greening [S111], Choudhary [S153 p. 1]. The cards could not separate Dey's own share in the team papers named in §1.

### Added in T3.6

- Rows added to SKILL.md's table: "2020-2026 Re-solved operational instances (Method 6)" [S044 pp. 1–3; S098 p. 2; S082 pp. 1–2; S067 p. 2]; "2024-2026 Gas and water network design with Sahinidis" [S059 pp. 9–15; S075 pp. 1, 11, 23; S109 pp. 2, 17–19].
- Card evidence added to existing rows: Wolsey's account of the CORE question [S079 p. 9]; the 2014 exit from computational multi-row cuts [S052 pp. 2, 25]; closures of convex sets [S018 p. 2; S042 pp. 1–2]; ExxonMobil support [S014 p. 29]; the duality line with Xu [S097 pp. 2–5].
- "Full-text view" paragraph: reading counts by period from 08 §1 (2016–2020 34/36; 2021–2026 55/61 = 89/97 cards).

### Before T3.6 (moved verbatim)

| Period | Direction | Trigger | Representative work |
|---|---|---|---|
| 2003-2009 | Group relaxations, lifting, two-row lattice-free cuts | Advisor's programme; Wolsey's question at CORE [06 T1, T2] | doi:10.1137/17M1117070 (late tail) |
| 2010-2014 | Exit from computational multi-row cuts; MILP theory to convex MINLP | "such a goal was too ambitious"; NSF grant [06 T3, T4] | doi:10.1287/ijoc.2013.0559; doi:10.1287/moor.1110.0488 |
| 2011-2017 | Bilinear programs, pooling | ExxonMobil funding [06 T5] | doi:10.1287/opre.2015.1357 |
| 2014-2018 | AC optimal power flow | A fresh SDP exactness claim [06 T6] | doi:10.1287/opre.2016.1489 |
| 2014-2019 | Sparse cutting planes | Unanalysed solver practice [06 T7] | doi:10.1287/moor.2017.0866 |
| 2017-2026 | QCQP substructure convexification | Solvers ran for hours on FEM model updating [06 T9] | doi:10.1137/21M1428583 |
| 2017-2024 | Statistics and ML through MINLP | Popular methods without certificates [06 T10] | doi:10.1287/opre.2021.2153 |
| 2018-2026 | Branch-and-bound theory, branching | "the need to ask different questions" [06 T8] | doi:10.1007/s10107-022-01895-4 |
| 2020-2026 | SDP and real-algebraic tools (Blekherman) | Sparse SDP bounds puzzle [06 T11] | doi:10.1007/s10107-020-01578-y |
| 2023-2026 | Duality and decomposition for IPs | Power operations, distributed computing [06 T12] | doi:10.1007/s10107-025-02265-6 |
| 2026 | Distributed first-order LP on GPUs | No stated reason [06 T14] | arXiv:2609.09108 |

### Latest

2025-10-10 to 2026-10-10 [06 §5]: 13 arXiv submissions, nine in 2026, the most in any year. Duality and decomposition grows fastest (doi:10.1016/j.orl.2025.107395; arXiv:2601.19003; arXiv:2604.23383, random-instance analysis of dual decomposition). QCQP work continues (arXiv:2604.00932; arXiv:2510.16595; doi:10.1016/j.orl.2026.107446). Published: doi:10.1007/s10107-026-02364-y (with Khajavirad); doi:10.1007/s10107-025-02265-6; his first AC-OPF relaxation paper since 2018 (doi:10.1109/naps66256.2025.11272395). He chaired the IPCO 2026 programme committee.

### SKILL.md full-text view before the T3.6 review fixes (moved verbatim)

**Full-text view** (references/research/09-evidence-ledger.md#trajectory; [08 §8]): after 2015 almost every work is read (89 of 97 cards). The texts add: pooling (2013–2017) returning in 2020–2026 as rank-one and QCQP convexification; power systems twice (2016–2018, 2022–2026); worst case → random instances; facets as yardstick → doubt about yardsticks. Constant: demarcation, MILP ideas as template, sparsity as structure, the dual bound as what applications lack.

<a id="academic-lineage"></a>

## Academic lineage

### Added in T3.6

Wolsey's account in the Optima 80 discussion column: "Later when Santanu Dey came to Core, my main concern was how to deal with integer non-basic variables, which again led him far beyond what was initially asked." [S079 p. 9]. Molinaro: 19 cards 2014–2026 [08 §9]. Alumni returning as coauthors: Kocuk [S129; S119], Morán [S112; S118], Angulo [S117] [08 §9]. Joint network papers with Sahinidis [S059; S075; S109].

### Before T3.6 (moved verbatim)

Mitten → Nemhauser → J.-P. P. Richard (lifting) → **Dey** (PhD Purdue 2007) [06 §2.1]. Postdoc with Wolsey at CORE (2007-09); junior-faculty mentor Shabbir Ahmed (co-advised 3 of his first 4 graduates; d. 2019); theory partner Molinaro since 2014. 17 PhD graduates 2012-2025; lifting continues to Gu; alumni return as co-authors (Kocuk, Morán, Angulo, Shah) [04 L1; 06 §2.3-2.4]. In this team: co-advised Li (2023) with Sahinidis and co-authors network papers with him (doi:10.1007/s10898-024-01424-x); Leyffer mentored Li at Argonne [04 H12].

<a id="inner-tensions"></a>

## Inner tensions

### Full-text evidence

| # | SKILL.md item | What the full texts show | Cards | Decision |
|---|---|---|---|---|
| 6 | Inner tension "count all overheads vs self-evident" | Confirmed verbatim (§2, H6). | [S098 p. 8; S082 p. 9] | Keep; replace the web citation with the card. |

### Added in T3.6

- **Theory for solvers**: card quote of the 2018 admission [S011 p. 20]; eased by two published rules [S014 pp. 14–16; S061 pp. 12–13].
- **Worst case**: worst-case results "only provide a coarse indication" [S011 p. 10]; "In order to avoid worst-case lower bounds, a standard idea is to consider random instances." [S031 p. 2].
- **Say what failed**: dead ends in the texts [S061 p. 12; S052 p. 2].
- **Overheads**: the "self-evident" sentence and its stated reason [S098 p. 8]; full timing [S082 pp. 9–12] (08 §3 row 6).
- **New: certificate vs primal-only contributions** (08 §3 row 9): borrowed certificates [S014 pp. 26, 28; S059 pp. 13–15; S075 pp. 24–25]; a heuristic without a certificate [S044 pp. 4, 16].

### Before T3.6 (moved verbatim)

Kept as tensions, not resolved.

- **Theory for solvers vs "I do not know."** R1 (14 occasions), the CAREER aim, "Hopefully this will lead to better rules" (2021) — against "these results have so far failed to directly help in actual cutting-plane selection" (2018) and "I do not know." (2024) [02 §1.1].
- **Tight worst-case bounds vs worst case is coarse.** R5 — against "only provide a coarse indication" (2018) and random instances "to avoid the exponential worst-case lower bounds" (2020) [02 C1].
- **Say what failed vs a silent claim change.** Dead ends written in (R8, 11 occasions) — against Strong SOCP "exact reformulation" (v1) becoming "relaxation" (v4) with no note [03 §4.2].
- **Count all overheads vs "self-evident".** Full timing in 2024 — against an untimed "self-evident" saving in 2022 [03 C5].
- **Newcomer modesty vs the record.** Global optimization "last two three years" (2020), "no understanding of machine learning at all" (2025) — against pooling from 2011, SDP for OPF 2014-16, ICML 2020 and NeurIPS 2024 papers [06 C1-C3].
- **Depth vs pivot.** B&B theory 2020-26, QCQP convexification 2017-26 — against lines going quiet when the carrying student graduates, multi-row optimism then exit, facets as a goal then "casts doubts" [06 §2.3; 02 C3, C6].

<a id="mentor-voice"></a>

## Mentor voice

### Added in T3.6

Added: the typical question "in absolute terms" [S020 p. 3]; surprise flagged against his own expectation in print ("Contrary to expectation" [S081 p. 9]; "We show that, surprisingly" [S105 p. 4]; more in the technique catalog, writing moves). Removed from SKILL.md for length (kept below): the "no free lunch" caption.

### Before T3.6 (moved verbatim)

On request only. Documented features; spoken quotes are auto-captions.

- **Feedback style**: plain admissions of not knowing ("I do not know."; "Is this the method, this [dual]? I don't know. I don't think so. But this is exciting."; "there's no free lunch unfortunately") [02 §1.1, §5.4].
- **Typical questions**: "Why do these MILP relaxations work so well?"; "How do solvers select cuts to use?"; is the measure "well-defined in all cases"?
- **Phrasing**: frank about his experiments ("I know there are experts here who are certainly going to frown upon these results and that's totally all right.") [02 §5.4]; "I like duals." [02 §1.3].
- **Student reports** (secondary): patience, prompt feedback, "convey complex ideas in simple words" [04 S1-S7].
- **Never**: claim a solver rule is proven useful when it is not; invent advice to students (none is written down) [04 G1].

<a id="corrections"></a>

## Corrections from the full texts

One section per correction listed in SKILL.md's "Corrections from the full texts":

1. **Method 1 step 8** (08 §3 row 1): before, "Step 8 rarely closed: rule proposals sit in unpublished preprints". The full texts show two published closures: the MILP restriction built from the pooling proof [S014 pp. 14–16] and a randomisation rule implemented in Feasibility Pump 2.0 and recommended for FP codes after the analysed version lost [S061 pp. 12–13]. The 2024–25 rules are preprints [S130 pp. 8, 20; S082 p. 6; S081 pp. 12–13].
2. **Method 2 scope** (08 §3 row 4): 31 works use full-solver or best-known baselines with no exact ceiling: [S047 p. 17; S075 pp. 22–23; S105 p. 11; S124 p. 14; S111 pp. 24–26; S133 p. 7; S076 p. 12]. The method holds in S020, S041, S048, S052, S081, S098, S122, S123, S130.
3. **Method 4 scope** (08 §3 row 8): computational and application papers draw the boundary computationally [S005 pp. 14, 16, 18; S004 p. 20; S001 pp. 13–14] or through sufficient conditions [S031 pp. 3, 15; S120 pp. 2–3; S082 pp. 6, 12; S083 p. 4].
4. **Method 5 contradictions** (08 §3 row 9): [S044 pp. 4, 16; S058 p. 14]; borrowed certificates [S014 pp. 26, 28; D002 pp. 22, 25; S059 pp. 13–15, 19; S075 pp. 11, 24–25; S109 pp. 17, 19].
5. **Method 5 attribution** (08 §3 row 12): before, "In 2017 he qualified his 2016 claim"; the qualification is already in the November 2015 arXiv v4 of the 2016 paper [S001 p. 30] and repeated in the March 2017 preprint (arXiv v1) of the 2018 MPC paper [S008 p. 31]; journal texts not read. The 2017 date replaced here was correct for the S008 text read; what changed is that the qualification also appears in S001.
6. **U4 overturned** (08 §3 row 16): Method 6.
7. **Branching anatomy attribution**: see [anatomy-branching](#anatomy-branching); the S020 card notes that the instrument and non-monotonicity are not in its text.
8. **Taste 2 nuance** (08 §3 row 14): [S040 p. 5; S010 pp. 9–10, 13].
9. **Facet yardstick dates** (08 §3 row 15): [S019 pp. 6, 20; S011 pp. 18–19; S117 p. 32; S122 p. 22].
10. **Heuristic 4 widened** (08 §5): see [heuristic-4](#heuristic-4).
11. **Not read / version change** (08 §3 rows 13, 17): the old "Not read" line (thesis, survey chapter, most final journal texts, proofs and computational tables of the signature papers) is replaced by the coverage numbers; the survey chapter is the 2009 group-theoretic one [S030]; v1 of the Strong SOCP paper was not read [S001].

Also changed without a correction number: the Research Trajectory T2 row now carries Wolsey's voice [S079 p. 9] (08 §3 row 18); the inner tension on overheads now cites the card [S098 p. 8] (08 §3 row 6); Method 3's contradiction is confirmed by [S052 pp. 2, 25; S079 p. 8] (08 §3 row 7).

### T3.6 review fixes

12. **U2 wording**: "ML lines stalled" became "ML lines unpublished" during T3.6 without a note. The two preprints cited there (arXiv:2003.10565 = S044, arXiv:2208.10028 = S098) are read in full; they support Method 6 (reuse across re-solves), not principled cut selection. U2 now names the cut-related ML preprint (arXiv:2411.15090 [S082]) and says this.
13. **D004 page citations**: the D004 file is arXiv:2312.06714v2, byte-identical to S067; the IPCO 2024 proceedings text was not read. Paged D004 citations are now written `[D004 arXiv pp. …]`.
14. **Method 3 "different from standard practice"**: the S032 p. 3 sentence ("such results") refers to ruled surfaces, not to set-wise convexification; SKILL.md now cites S032 p. 2 and says "the paper notes" (co-authored text).
15. **SDP qualification dates**: the texts read are the November 2015 arXiv v4 of the 2016 paper [S001 p. 30] and the March 2017 arXiv v1 of the 2018 MPC paper [S008 p. 31]; journal texts not read.
16. **Heuristic cap**: Heuristic 10 folded into Method 3 as a variant; Heuristic 11 renumbered 10 (see [folded-design-cut](#folded-design-cut)).
17. **Quote version note**: "surprisingly common in practice" [S081 p. 11] and the earlier "surprisingly prevalent in practice" are both verbatim in arXiv v1 (pp. 11 and 13); no version difference.

### SKILL.md "Corrections from the full texts" list before the T3.6 review fixes (moved verbatim)

### Corrections from the full texts

One line each; details in references/research/09-evidence-ledger.md#corrections.

1. Method 1 step 8 closed in published form twice [S014 pp. 14–16; S061 pp. 12–13]; before, "rarely closed".
2. Method 2 is practised in the branching and cut-measurement line; application papers compare against full solvers [S047 p. 17; S111 pp. 24–26].
3. Method 4 governs the headline theory papers; computational papers draw the line computationally [S005 pp. 14, 16, 18].
4. Method 5: two works deliver no certificate, and application work often borrows it [S044 pp. 4, 16; S058 p. 14; S014 pp. 26, 28].
5. Method 5: the SDP qualification is in the 2016 text [S001 p. 30], repeated in 2018 [S008 p. 31]; before, dated 2017.
6. U4 (reuse across re-solves, "preliminary") is overturned and becomes Method 6 [S044 p. 18; S082 pp. 6, 16–17; S067 p. 7].
7. Branching anatomy: the naive Python B&B, stripped SCIP and non-monotonicity belong to the IJOC paper [S081 pp. 8–11], not to doi:10.1007/s10107-023-01977-x [S020].
8. Taste 2: data independence is a taste for theorems, not for algorithms [S040 p. 5].
9. Facet yardsticks were his own practice before 2011 [S019 pp. 6, 20]; the doubt dates from 2018 [S011 pp. 7–8].
10. Heuristic 4 widened: devices and theorems, not only obstacles, feed the next line [S104 pp. 6, 22–29; S120 pp. 5, 9; S049 pp. 5–6].
11. The unread survey chapter is the 2009 one [S030]; the Strong SOCP v1-to-v4 change was not re-verified [S001].

### All variants and contradictions found (08 §3, verbatim)

| # | SKILL.md item | What the full texts show | Cards | Decision |
|---|---|---|---|---|
| 1 | M1 limitation: "Step 8 rarely closed: rule proposals sit in unpublished preprints" | Step 8 is closed in two published works: the MILP restriction built from the pooling proof (Oper. Res. 2015) and a randomisation rule implemented in Feasibility Pump 2.0 and recommended for FP codes after the analysed version lost (SIAM J. Optim. 2018). The branching rules of 2025 and the GMIC heuristic of 2024 are preprints. | [S014 pp. 14–16; S061 pp. 12–13; S130 pp. 8, 20; S082 p. 6; S081 pp. 12–13] | **Revise** the limitation: "Step 8 closed in published form twice (pooling restriction 2015, feasibility-pump rule 2018); the ML-facing rules of 2024–25 are preprints." |
| 2 | M1 as the entry point | 23 works link to M1 only as a variant: the question comes from a named open question [S021 p. 1], a classical lemma's standing [S125 pp. 1–2], completeness of a cut technique [S071 p. 1], the authors' own relaxation [S129 pp. 14–17], a theoretical preprocessing technique [D005 pp. 1–2], a classical rank measure [S099 pp. 1–2], or a new paradigm rather than an explanation [S096 p. 2; S095 p. 1]. | as cited | **Add a scope sentence** to M1: it is the main entry, not the only one. Named open questions go to the candidate pool (§6). |
| 3 | M1 step 3 (strip to a proxy) | The texts also climb back: drop features, then re-add one at a time and ask which theorem survives [S079 pp. 5–8; S013 pp. 3, 8; S016 pp. 1–2]; the sparse-cut proxy is pushed toward realism by "four numbered questions" each restoring one feature of solver practice [S065 pp. 1–2]. | [S079; S013; S016; S065] | **Variant note** on M1 between steps 6 and 7: "restore one realism at a time (LP relaxation, dense cuts, rotation, objective) before claiming practice is explained." |
| 4 | M2 say–do ("2010–2026") | 31 works use full-solver or best-known baselines with no exact ceiling: decentralised power [S047 p. 17], water networks [S075 pp. 22–23], bilinear covers [S105 p. 11], change-point MIP [S124 p. 14], network design [S111 pp. 24–26], facility location [S133 p. 7], sparse CCA beyond n = 20 [S076 p. 12]. | as cited | **Narrow** M2's say–do line: "practised in the branching and cut-measurement line (S020, S041, S048, S052, S081, S098, S122, S123, S130); application papers compare against full solvers." |
| 5 | M2 step 4 / step 6 (instance ladder, no extrapolation) | One 2026 application paper tunes heuristic parameters on the benchmark it reports. | [S109 pp. 21–22] | **Record** as the one M2 contradiction; no change to the method. |
| 6 | Inner tension "count all overheads vs self-evident" | Confirmed verbatim (§2, H6). | [S098 p. 8; S082 p. 9] | Keep; replace the web citation with the card. |
| 7 | M3 contradiction (two-row cuts disappointed, yet two-row ideas went to QCQP) | Confirmed: the computational multi-row goal "was too ambitious" and type 2 triangle cuts "are not competitive with split cuts" for typical instances [S052 pp. 2, 25]; density was already named as the practical obstacle in 2009: "Another practical difficulty with this class of cutting planes is that they tend to be dense." [S079 p. 8]. New variants: an MILP algorithmic rule (strong branching, product score) imported into QCQP [S123 pp. 1–4]; an IP operation (CG rounding) imported [S122 pp. 2–5]; the reverse direction, polynomial lifting brought back into MIP decomposition [S104 pp. 5, 9]. | as cited | Keep the contradiction; **add a variant line** to M3: "imports algorithmic rules and closure operations too, and once runs in reverse." |
| 8 | M4 scope | In computational and application papers the boundary is drawn computationally (300-bus limit, cases where the strongest method underperforms) [S005 pp. 14, 16, 18; S004 p. 20; S001 pp. 13–14], or through sufficient conditions without a tight example [S031 pp. 3, 15; S120 pp. 2–3; S082 pp. 6, 12; S083 p. 4]. A constructive form of step 3 recurs: find what replaces the dropped hypothesis rather than only exhibiting the failure (rationality replaced by an interior mixed-integer point [S037 p. 3], by a thin set with rational recession cone [S029 pp. 2, 17]; Dirichlet approximation for irrational data [D001 pp. 3–4, 6; S043 p. 14]; Geoffrion beyond finiteness and rationality: "The challenge for extending Geoffrion's theorem beyond finiteness and rationality is thus to understand integer programs whose feasibility set lies on the boundary of conv(X)." [S112 p. 5]). | as cited | **Add** to M4's limitation: "governs headline theory papers; computational papers draw the line computationally." **Add** the replacement-hypothesis form to step 3. |
| 9 | M5 (certificate as deliverable) | Two works deliver no certificate: a kNN heuristic with possibly infeasible output [S044 pp. 4, 16] and a scalable primal bound for relay attacks, "we do not know of a non-trivial upper bound" (from [S058 p. 14]). In five application papers the contribution is primal and the dual bound is borrowed from BARON or SCIP [S014 pp. 26, 28; D002 pp. 22, 25; S059 pp. 13–15, 19; S075 pp. 11, 24–25; S109 pp. 17, 19]. | as cited | **Record** both contradictions; add to M5's limitations: "in application work with Sahinidis and on pooling he often supplies the primal side and borrows the certificate." |
| 10 | M5 step 2 ("rank candidate relaxations") | The ranking is often done by theorem, and the heavier relaxation is proved to add nothing before cheap cuts are offered: lifted LP, lifted SDP and an earlier SDP all equal a closed-form bound [S100 pp. 9–10]; an SOCP relaxation proved at least as strong as SDP ∩ QBP [S041 p. 3]; "We show that, surprisingly, for the class of separable instances, the SDP relaxation gives a bound equal to that of the McCormick relaxation." [S105 p. 4]; "Interestingly, adding the SDP constraint (3) to the P relaxation does not further strengthen this relaxation as proven below." [S129 p. 5]; six relaxations ordered in projected space before one is strengthened [S001 pp. 11–14]. The device is a PSD completion, rank one plus a sparse or diagonal correction, [S105 pp. 5–7; S129 p. 5; S001 pp. 11–12]. | as cited | **Variant note** on M5 step 2: "where possible prove the ranking; a PSD completion of the cheap optimum shows the SDP adds nothing." Not a new method (it is M5's own step). |
| 11 | M5 steps 3–4 | Step 4's feasible point often comes from an MILP restriction built from the same discretisation or proof as the relaxation, not from a local solver [S014 pp. 14–16; D002 pp. 22–25; S051 pp. 10–11, 17–18; S080 pp. 18–19]. Step 3 includes constraints redundant for the primal that strengthen the dual or the solver bound [S104 pp. 3–5; S117 pp. 2, 13; S111 p. 16]. The cheap object can be a DNN/SDP restriction of a copositive dual [D004 arXiv pp. 11, 13–14]. | as cited | **Variant notes** on M5 steps 3 and 4. |
| 12 | M5 limitation: "In 2017 he qualified his 2016 claim: 'not very competitive against the SDP relaxation, especially for easier instances'" | The sentence is in the spatial branch-and-cut paper read as arXiv v1: "Strong SOCP relaxations from our previous paper [27] improves the plain SOCP relaxation considerably but it is not very competitive against the SDP relaxation, especially for easier instances." [S008 p. 31]. The 2016 paper's own comparison section already says "We note that our SOCP based relaxations are not as successful according to this comparison." [S001 p. 30]. | [S008 p. 31; S001 p. 30] | **Revise** the attribution: the qualification is already in the November 2015 arXiv v4 of the 2016 paper and repeated in the March 2017 preprint of the 2018 MPC paper; journal texts not read (wording corrected in the T3.6 review). |
| 13 | Honest boundary: Strong SOCP "exact reformulation" (v1) → "relaxation" (v4) | Only v4 was carded [S001 p. 1]; v1 was not read. | [S001] | **Unchanged, flagged "not re-read in full text"**. |
| 14 | Taste 2 (data-independent bounds) | Supported [S035 p. 1; S024 pp. 5–9; S079 pp. 3, 5], but a 2020 paper sells a data-dependent grouping against the authors' own earlier bounds: "However, these bounds are entirely data-independent." [S040 p. 5]; early relaxation-strength bounds are data-dependent [S010 pp. 9–10, 13]. | as cited | **Add a nuance**: data independence is a taste for theorems, not for algorithms that must use the data. |
| 15 | Anti-pattern "facetness or depth of cut as proxies for usefulness" | 2010 papers still use extremality and a merit index as strength yardsticks [S019 pp. 6, 20]. A 2026 paper uses depth as its proxy measure [S122 pp. 4, 12–14] and still concludes for sparse structured cuts [S122 p. 22]; another finds the richest encoding family worst in practice: "greater expressive power does not necessarily translate into a better algorithm." [S117 p. 32]. | as cited | Keep the anti-pattern; **add the dates** (facet yardsticks before 2011, doubt from 2018) and S117 as practice evidence. |
| 16 | Honest boundary U4 "reuse information across re-solves: practice 'preliminary'" | Four works built on recurring instances (§4). | [S044; S098; S082; D004 = S067] | **Overturned**: U4 leaves the unverified list and becomes Method 6 (§4). The Anti-patterns row "his practice: preliminary" changes accordingly. |
| 17 | Honest boundary "Not read: ... most final journal texts, proofs and most computational tables of the signature papers" | 116 works now read in full or in part, proofs and tables included (§1). Many were read as arXiv or author preprints. | §1 | **Revise**: "read as preprints in most cases; journal-version changes not read; the thesis, the 2009 survey chapter and the IPCO 2008 lifting paper remain abstract-level [S074; S030; S015]." |
| 18 | SKILL Trajectory T2 ("Wolsey's question at CORE") | The other side's voice confirms it: "Later when Santanu Dey came to Core, my main concern was how to deal with integer non-basic variables, which again led him far beyond what was initially asked." [S079 p. 9] (Wolsey, discussion column). | [S079 p. 9] | **Add** the card as evidence (other voice). |

### Rejected updates (08 §10, verbatim)

Each was proposed by at least one card and is rejected because the existing framework already explains it, or because it adds no explanatory power.

1. **"20% gap as a reporting threshold"** [S059 p. 18]: an echo of SKILL.md's rule of thumb in one application paper; no new behaviour.
2. **"GPU-scale first-order LP as infrastructure for discrete optimization"** [S110 pp. 1, 6]: a trajectory fact with Dey's role not identifiable; already in SKILL.md's trajectory (2026 row). Not a method.
3. **"Data-dependent bound as selling point"** [S040 p. 5]: recorded as a Taste 2 nuance (§3 row 14), not a pattern.
4. **"State the theorem through the property the proof uses"** [S042 pp. 9–10]: merged into H11.
5. **"Explain a negative instance with your own theory paper"** and **"hedge a formulation-strength claim with your own non-monotonicity theorem"** [S103 p. 12; S124 pp. 10, 13]: merged into H4 (widened).
6. **"Programme cross-feeding across parallel papers"** [S017; S035 pp. 13–14; S048 pp. 6–8]: merged into H4 (widened).
7. **"Reuse your own approximation-ratio device / proof machinery / lemma bank / decomposition"** [S104 pp. 6, 22–29; S097 p. 6; S120 pp. 5, 9; S049 pp. 5–6; S075 pp. 3, 11]: merged into H4 (widened).
8. **"Independent original-space checker as acceptance gate"** [S110 pp. 3–4, 13–15]: covered by M2 step 5 (sanity checks in code); single work with an unidentifiable share.
9. **"Byproduct bound tightening"** [S123 pp. 2–4] and **"fixed-point bound tightening by LPs"** [S010 pp. 7–10]: standard in global solvers (OBBT-style); no Dey-specific content.
10. **"Approximation algorithm as warm start"** [S023 pp. 1, 16] and **"cover-not-fit parameter policy"** [S121 p. 21]: generic practice, single cards.
11. **"Budget sweep against folklore"** [S009 pp. 28–29]: folded into the M2 variant "theory picks the stress axis" (§6).
12. **"Unify two classical results"** [S003 pp. 1, 3] and **"consolidate-then-extend"** [D002 pp. 2, 7–8]: covered by M3 step 1 (the MILP list) and by M4; no added power.
13. **Promoting "prove the heavier relaxation adds nothing" and "paired relaxation/restriction" as methods** (§4): rejected as duplicates of M5.
14. **Demoting H10 outright**: rejected for now. It still passes "executable + say–do" [S096 p. 2; S141]. Only a cap on heuristics would justify folding it (§5).

### Open gaps (08 §11, verbatim)

- **Works without an open text** (abstract or metadata only): the PhD thesis [S074]; the IPCO 2008 lifting paper [S015]; the group-theoretic survey chapter [S030]; the 2010 two-row experiments [S038]; the ellipsoid CG-closure paper [S054]; the pooling technical report and overview [S012; S090]; MIPLearn [S087]; the OPF bound-tightening paper [S128]; the network-design dual-bound conference version [S131]; row-sparse PCA [S161]; the treewidth-convex hull note [S157]; "Gomory functions" [S102]; floor layout [S166]; EV charging [S132; S154; S155]; selective optimization [S139]; closedness of SOC sets [S140]; the NSF award records [S138; S141; S146]. So the 2007–2009 origins of M3 and of the multi-row programme rest on abstracts and on the 2009 survey [S079 pp. 2–8].
- **Partial reads**: 30 cards read only parts; proofs of several 2010–2013 closure and lifting papers are not read in detail [S026; S029; S043; S046; S053; S072]; appendix proofs of the floor-layout equivalences [S100 pp. 9–10]; journal-version changes of all works read as preprints (§1).
- **Strong SOCP version change**: v1 not read; the SKILL.md claim rests on the web-research note [S001].
- **Method 6**: three of four works are preprints; whether the license-then-reuse pattern survives refereeing, and how much of it is Dey's rather than the Argonne collaborators' [S098; S082], is not visible in the texts.
- **Say–do on the stated side**: the cards are papers, mostly co-authored; Dey's own voice (talks, interviews) is not in the card corpus, so "stated" in this note means co-signed text.
- **Supervision, refereeing, coding**: no card evidence beyond acknowledgements and guest-editor prefaces [S094 p. 5; S113]; the gaps listed in SKILL.md's "Stages without a distillable Dey method" stand.
- **Undated and misattributed rows**: S153 is undated (no earlier than late 2024 by its references) [S153 p. 1]; S144 and S145 belong to a different S. Dey and should stay excluded [S144; S145].

### Honest Boundary before T3.6 (moved verbatim)

This skill is distilled from public information and has these limits:

- **Tacit gaps**: how he picks which solver habit to explain, how he picks the proxy measure, how small-case computation becomes the right conjecture; one-to-one meetings are undocumented [04 T1].
- **Supervision**: acknowledgement-genre evidence only (one passage template-like) [04 C3, G1].
- **Unstated reasons**: why he leaves lines; why the Strong SOCP "exact reformulation" became a "relaxation" without a note.
- **Unseen practice**: no commit by Dey in any repository examined; no public reviews or rebuttals; spoken evidence is auto-captions [03 Gaps; 05 Gaps].
- **Era and resources**: 2014-17 OPF results ran on a 4-8 GB PC with commercial licences; SOC relaxations are contested at PGLib scale; the 2026 GPU paper is the first to need a cluster [03 §3.5; 05 §1.2].
- **Field boundary**: an integer-programming theorist in global optimization; not his voice on NLP subsolvers, GDP modelling or solver software engineering.
- **Claimed but unverified** (never methods): U1 theory of solver practice will yield better solver rules — attempts only in unpublished arXiv:2507.09455 and arXiv:2411.15090, and "I do not know." (2024); U2 principled cut selection lies "somewhere in between" ML and theory (2018) — ML lines stalled (arXiv:2208.10028, arXiv:2003.10565 unpublished); U3 "stick with it and consider the problem from a different angle" (said of Ahmed) — no trace; U4 reuse information across re-solves — practice "preliminary" (arXiv:2312.06714); U5 value "Even if such a technique is never used in practice" (2005, once); U6 CAREER education plan, not verified; U7 "theory explains what we see in practice" as success criterion — partly met, openly not met for the PSD closure [02 §1.1, §2.4, §5.2; 04 D2, D3].
- **No statement against misconduct** found; only honest-reporting statements are quotable.
- **Not read**: his PhD thesis, the 2010 survey chapter, most final journal texts, proofs and most computational tables of the signature papers.
- **Record facts**: 74 arXiv records (earliest arXiv:0906.0887); no errata or retractions on 116 DOIs (Crossref) [03 §7; 06 C8].
- **Research date**: 2026-10-10. Dey is active (13 arXiv submissions in the last year); later work is not covered. Update this skill periodically, at least yearly.

<a id="sources-secondary"></a>

## Secondary sources

Moved from SKILL.md's Sources appendix on 2026-10-10 (unchanged).

- Theses (Georgia Tech): Gupte 2012, https://hdl.handle.net/1853/45761; Kocuk 2016, https://hdl.handle.net/1853/55633; Santana 2019, https://hdl.handle.net/1853/62680; Shah 2025, https://hdl.handle.net/1853/77883; Shao 2020, https://repository.gatech.edu/server/api/core/bitstreams/92d7b591-7f35-4aa9-a2dd-dc1769ed72fe/content
- Bienstock, Villagra, Math. Program. Comput. 2025, doi:10.1007/s12532-025-00287-x; arXiv:2510.21698
- Molzahn et al., IEEE Trans. Power Syst. 2017, doi:10.1109/TPWRS.2016.2550520; Gopinath et al., Electr. Power Syst. Res. 2020, doi:10.1016/j.epsr.2020.106688
- Ceccon, Kouyialis, Misener, AIChE J. 2016, doi:10.1002/aic.15308; Ceccon, Misener, Comput. Chem. Eng. 2022, doi:10.1016/j.compchemeng.2022.107660
- Borst et al., Math. Program. 2022, doi:10.1007/s10107-022-01828-1; Haugland, INOC 2019, doi:10.5441/002/inoc.2019.18

<a id="card-key"></a>

## Card key

Every card id cited in SKILL.md or this ledger: year, title (as in `07-paper-cards.md`) and read level. Full cards are in `cards/` (batch file named in 07).

| Card | Year | Title | Read level |
|---|---|---|---|
| D001 | 2011 | On the Chvátal-Gomory Closure of a Compact Convex Set | partial |
| D002 | 2017 | Relaxations and discretizations for the pooling problem | full |
| D003 | 2023 | Branch-and-bound solves random binary IPs in poly(n)-time | full |
| D004 | 2024 | Sensitivity Analysis for Mixed Binary Quadratic Programming | full |
| D005 | 2026 | Random projection with linear equalities and inequalities | full |
| H001 | — | Modeling and Solving the Large Scale EV Charger Location Planning Problem | full |
| S001 | 2016 | Strong SOCP relaxations for the optimal power flow problem | full |
| S002 | 2013 | Solving mixed integer bilinear problems using MILP formulations | full |
| S003 | 2017 | Mixed-integer quadratic programming is in NP | full |
| S004 | 2016 | Improving the integer L-shaped method | full |
| S005 | 2017 | New formulation and strong MISOCP relaxations for AC optimal transmission switching problem | full |
| S006 | 2016 | Inexactness of SDP relaxation and valid inequalities for optimal power flow | full |
| S008 | 2018 | Matrix minor reformulation and SOCP-based spatial branch-and-cut method for the AC optimal power flow problem | full |
| S009 | 2016 | A cycle-based formulation and valid inequalities for DC power transmission problems with switching | full |
| S010 | 2014 | Covering linear programming with violations | full |
| S011 | 2018 | Theoretical challenges towards cutting-plane selection | full |
| S012 | 2013 | Pooling problems: relaxations and discretizations | metadata |
| S013 | 2010 | Two row mixed-integer cuts via lifting | full |
| S014 | 2015 | Analysis of MILP techniques for the pooling problem | full |
| S015 | 2008 | Lifting integer variables in minimal inequalities corresponding to lattice-free triangles | abstract |
| S016 | 2010 | Constrained infinite group relaxations of MIPs | full |
| S017 | 2022 | Using ℓ1-Relaxation and Integer Programming to Obtain Dual Bounds for Sparse PCA | full |
| S018 | 2011 | The split closure of a strictly convex body | full |
| S019 | 2010 | On the extreme inequalities of infinite group problems | full |
| S020 | 2024 | A theoretical and computational analysis of full strong-branching | full |
| S021 | 2017 | Bounding the gap between the McCormick relaxation and the convex hull for bilinear functions | full |
| S022 | 2015 | Forbidden vertices | full |
| S023 | 2020 | Approximation algorithms for training one-node ReLU neural networks | full |
| S024 | 2018 | Analysis of sparse cutting planes for sparse milps with applications to stochastic milps | full |
| S025 | 2014 | On the Chvátal–Gomory closure of a compact convex set | full |
| S026 | 2008 | Facets of two-dimensional infinite group problems | partial |
| S028 | 2015 | Approximating polyhedra with sparse inequalities | full |
| S029 | 2013 | Some properties of convex hulls of integer points contained in general convex sets | partial |
| S030 | 2009 | The group-theoretic approach in mixed integer programming | abstract |
| S031 | 2021 | Branch-and-bound solves random binary ips in polytime | full |
| S032 | 2020 | The convex hull of a quadratic constraint over a polytope | full |
| S033 | 2011 | Split rank of triangle and quadrilateral inequalities | full |
| S034 | 2023 | Lower bounds on the size of general branch-and-bound trees | full |
| S035 | 2022 | Sparse PSD approximation of the PSD cone | full |
| S037 | 2012 | A strong dual for conic mixed-integer programs | partial |
| S038 | 2010 | Experiments with two row tableau cuts | abstract |
| S039 | 2018 | Aggregation-based cutting-planes for packing and covering integer programs | partial |
| S040 | 2020 | Optimization-driven scenario grouping | partial |
| S041 | 2019 | New SOCP relaxation and branching rule for bipartite bilinear programs | full |
| S042 | 2011 | The Chvátal-Gomory closure of a strictly convex body | full |
| S043 | 2011 | On maximal S-free convex sets | partial |
| S044 | 2020 | A k-nearest neighbor heuristic for real-time dc optimal transmission switching | full |
| S046 | 2010 | Relations between facets of low- and high-dimensional group problems | partial |
| S047 | 2024 | Decomposable formulation of transmission constraints for decentralized power systems optimization | full |
| S048 | 2022 | Cutting plane generation through sparse principal component analysis | full |
| S049 | 2020 | Exact augmented Lagrangian duality for mixed integer quadratic programming | partial |
| S051 | 2020 | Convexifications of rank-one-based substructures in QCQPs and applications to the pooling problem | full |
| S052 | 2014 | On the practical strength of two-row tableau cuts | full |
| S053 | 2010 | Composite lifting of group inequalities and an application to two-row mixing inequalities | partial |
| S054 | 2010 | The Chvátal-Gomory closure of an ellipsoid is a polyhedron | abstract |
| S055 | 2022 | Hyperbolic Relaxation of k-Locally Positive Semidefinite Matrices | partial |
| S056 | 2019 | Nonunique lifting of integer variables in minimal inequalities | full |
| S057 | 2023 | Solving sparse principal component analysis with global support | partial |
| S058 | 2022 | A scalable lower bound for the worst-case relay attack problem on the transmission grid | partial |
| S059 | 2024 | A reformulation-enumeration MINLP algorithm for gas network design | full |
| S060 | 2021 | Finite element model updating of an 18-story structure using branch-and-bound algorithm with epsilon-constraint | full |
| S061 | 2018 | Improving the randomization step in feasibility pump | full |
| S062 | 2022 | Node-based valid inequalities for the optimal transmission switching problem | partial |
| S063 | 2011 | On mixed-integer sets with two integer variables | full |
| S065 | 2015 | Some lower bounds on sparse outer approximations of polytopes | partial |
| S067 | 2026 | Sensitivity analysis for mixed binary quadratic programming | full |
| S070 | 2014 | Semi-continuous network flow problems | partial |
| S071 | 2022 | On obtaining the convex hull of quadratic inequalities via aggregations | full |
| S072 | 2009 | Linear-programming-based lifting and its application to primal cutting-plane algorithms | partial |
| S073 | 2017 | Some cut-generating functions for second-order conic sets | partial |
| S074 | 2007 | Strong cutting planes for unstructured mixed integer programs using multiple constraints | abstract |
| S075 | 2025 | Optimizing the design and operation of water networks: Two decomposition approaches | full |
| S076 | 2024 | On sparse canonical correlation analysis | full |
| S077 | 2024 | Aggregations of quadratic inequalities and hidden hyperplane convexity | full |
| S078 | 2016 | Strengthened bounds for the probability of k-out-of-n events | full |
| S079 | 2009 | Recent developments in multi-row cuts | full |
| S080 | 2026 | Regularized MIP model for integrating energy storage systems and its application for solving a trilevel interdiction problem | full |
| S081 | 2026 | Non-monotonicity of branching rules with respect to linear relaxations | full |
| S082 | 2024 | Approximating the Gomory mixed-integer cut closure using historical data | full |
| S083 | 2020 | Upper bounds for model-free row-sparse principal component analysis | full |
| S084 | 2014 | How good are sparse cutting-planes? | full |
| S085 | 2023 | Lifting convex inequalities for bipartite bilinear programs | partial |
| S086 | 2022 | Lower bound on size of branch-and-bound trees for solving lot-sizing problem | full |
| S087 | 2020 | MIPLearn: an extensible framework for learning-enhanced optimization | abstract |
| S088 | 2017 | Sparse principal component analysis and its ℓ1-relaxation | partial |
| S090 | 2015 | Pooling problems: an overview | metadata |
| S091 | 2012 | Forbidding extreme points from the 0-1 hypercube | full |
| S092 | 2026 | A second-order cone representable class of nonconvex quadratic programs | full |
| S094 | 2022 | Global Solution of Integer, Stochastic and Nonconvex Optimization Problems: SS Dey et al. | full |
| S095 | 2014 | Design and verify: a new scheme for generating cutting-planes | full |
| S096 | 2011 | Design and verify: a new scheme for generating cutting-planes | full |
| S097 | 2024 | Lagrangian dual with zero duality gap that admits decomposition | full |
| S098 | 2022 | Exploiting instance and variable similarity to improve learning-enhanced branching | full |
| S099 | 2019 | Lower bounds on the lattice-free rank for packing and covering integer programs | full |
| S100 | 2018 | Beating the SDP bound for the floor layout problem: A simple combinatorial idea | full |
| S102 | — | Gomory functions | metadata |
| S103 | 2026 | Aggregation of bilinear bipartite equality constraints and its application to structural model updating problem | full |
| S104 | 2025 | Lagrangian dual for integer optimization with zero duality gap that admits decomposition | full |
| S105 | 2024 | Solving sparse separable bilinear programs using lifted bilinear cover inequalities | full |
| S106 | 2023 | A covering decomposition algorithm for power grid cyber-network segmentation | partial |
| S109 | 2026 | Water network design and operation optimization: Leveraging approximations | full |
| S110 | 2026 | Distributed Linear Programming on GPU Clusters at Extreme Scale | full |
| S111 | 2026 | Strengthening dual bounds for multicommodity capacitated network design with unsplittable flow constraints | full |
| S112 | 2026 | Geoffrion's theorem beyond finiteness and rationality | full |
| S113 | 2023 | Integer programming and combinatorial optimization (IPCO) 2021 | full |
| S117 | 2026 | Decomposition of Sparse Integer Programs via Nonlinear Edge Encodings and Column-and-Row Generation | full |
| S118 | 2026 | Branching with a pre-specified finite list of k-sparse split sets for binary MILPs | full |
| S119 | 2026 | Copositive Matrices with Ordered Off-Diagonal Entries | full |
| S120 | 2026 | Probabilistic analysis of dual decomposition on two-stage stochastic integer programs | full |
| S121 | 2026 | Accelerating Column Generation in Highly Degenerate Integer Programming Problems with Template Pricing | full |
| S122 | 2026 | Chvátal-Gomory Rounding of Eigenvector Inequalities for QCQPs | full |
| S123 | 2026 | Extreme strong branching for QCQPs | full |
| S124 | 2026 | Mixed-Integer Programming for Change-point Detection | full |
| S125 | 2026 | Asymptotically tight Lagrangian dual of smooth nonconvex problems via improved error bound of Shapley-Folkman Lemma | full |
| S128 | 2025 | Combined Bound Tightening on McCormick Relaxations of AC Optimal Power Flow | abstract |
| S129 | 2025 | Convexification of a Separable Function over a Polyhedral Ground Set | full |
| S130 | 2025 | Improving Full Strong Branching Decisions by Incorporating Additional Information | full |
| S131 | 2025 | Improving Dual Bounds for the Unsplittable Multicommodity Capacitated Network Design Problem | metadata |
| S132 | 2025 | Charging Station Placement Optimization for Electric Vehicles Integrated with Rail Transit | abstract |
| S133 | 2025 | Hyperconnected Facility Location Contracting | full |
| S135 | 2021 | Lifting Convex Inequalities for Bipartite Bilinear Programs | partial |
| S138 | 2016 | Sparse Integer Programming | abstract |
| S139 | 2015 | Selective Optimization | metadata |
| S140 | 2013 | A polynomial-time algorithm to check closedness of simple second order mixed-integer sets | abstract |
| S141 | 2012 | CAREER: Non-traditional Cutting-Plane Algorithms for Mixed-Integer Programs | abstract |
| S144 | 2011 | O-046 MSX genes direct embryo implantation by regulating the luminal epithelial cell polarity | metadata |
| S145 | 2011 | COMPANY SYMPOSIUM, MSD COMPANY SYMPOSIUM, Monday 4 July 2011 14: 00-15: 15, INVITED SESSION, SESSION 12: CELL-CELL COMMUNICATION, Monday 4 July 2011 14: 00-15: 00 | metadata |
| S146 | 2010 | Collaborative Research: Fundamentals of Convex Mixed Integer Nonlinear Programming | abstract |
| S153 | undated (no earlier than late 2024; cites arXiv:2411.12085, pp. 16-17) | New Proofs of Exact LP Reformulations for Binary Polynomial Optimization with Bounded Treewidth | full |
| S154 | — | Charging Station Placement Optimization for Electric Vehicles Integrated with Public Transit | abstract |
| S155 | — | Charging Station Placement Optimization for Electric Vehicles | abstract |
| S157 | — | The Treewidth-Convex HullTheorem and DP for Cut Generation in MINLP | metadata |
| S161 | — | Row-sparse principal component analysis with guarantees | metadata |
| S166 | — | New MIP approaches to the floor layout problem | metadata |

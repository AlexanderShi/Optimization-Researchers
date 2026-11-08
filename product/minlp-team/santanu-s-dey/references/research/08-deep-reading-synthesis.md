# Santanu S. Dey · Deep-reading synthesis

> Date: 2026-10-10 (stage T3.6, first synthesis round for this member). Input: every card in `cards/` (32 batch files, 154 card entries; index in `07-paper-cards.md`). Rules applied: `references/paper-reading-card.md` §3 (conservative update: append only, existing methods get evidence first, a new core method needs ≥3 distinct works plus the four checks, reject updates without explanatory power, every line traceable to a card) and `references/research-extraction-framework.md` §3 (four-way validation) and §11 (quality checklist). This note proposes changes; it does not edit `SKILL.md`.
>
> Gate: `verify_card_quotes.py` reported 258 quotes, 257 exact, 1 matching after spacing/symbol normalisation, 0 NOT FOUND; `mark_read_from_cards.py` then set the INDEX Read column (93 carded, 30 skimmed, 15 abstract, 16 metadata).
>
> Citation form: `[S012 p. 9]` = card S012, page of the extracted text as recorded on the card (`[[page N]]`). Abstract- and metadata-level cards are cited by ID only. Seven pairs are two versions of one work and count once below (first ID listed is the one counted): S031 = D003 (2021 version / Math. Program. 2023) [S031 pp. 1–4]; S084 → S028 (IPCO 2014 → Math. Program. 2015) [S028]; S096 = S095 (IPCO 2011 / Math. Program. 2014) [S095 p. 3]; D001 = S025 (IPCO 2011 / journal 2014) [D001]; S135 = S085 (IPCO 2021 abstract / Math. Program. 2023) [S085 pp. 1–2]; S097 = S104 (arXiv 2024 / IPCO 2025) [S104 p. 1]; D004 = S067 (IPCO 2024 / Math. Program. 2026) [S067 p. 3]. Cards that record typos or internal inconsistencies of a paper are reading notes and are not used as findings here. All papers are co-authored unless the card says otherwise, so "stated" below means *stated in a text Dey co-signed*.

---

## 1. Coverage

| Item | Count | Source |
|---|---|---|
| Google Scholar rows | 169 | `07-paper-cards.md`, Coverage |
| Distinct works indexed | 156 | same |
| Open full text found | 123 | same |
| Card entries / works with a card | 154 / 154 | same |
| **Full text read** | **123 cards** (93 full, 30 partial) = **116 distinct works** after the seven version pairs | read-level column of `07-paper-cards.md` |
| Abstract-level | 15 | a2-01 |
| Metadata-only | 16 | a2-01, a2-02 |
| Skipped (not his / non-research) | 2 | INDEX Role = skip |

Full-text reads by period (full + partial cards / all cards with a year in that period): 2007–2010 8/15; 2011–2015 24/32; 2016–2020 34/36; 2021–2026 55/61; undated 2/10. The group-relaxation years before 2010 are known partly from abstracts only (the PhD thesis [S074], the IPCO 2008 lifting paper [S015], the group-theoretic survey chapter [S030], the two-row experiments paper [S038]); everything after 2015 is read almost completely.

Material that is not evidence of Dey's own method, and is used only as noted: the "Comments on Multi-Row Cuts" column in Optima 80 is Cornuéjols, Weismantel and Wolsey's voice [S079 pp. 8–10]; three editorials are joint voices of guest editors [S094 p. 1; S113; S115 pp. 1–3]; S093 is an economics paper outside the field [S093 pp. 1–11]; S144 and S145 are works of a different S. Dey [S144; S145]; several metadata rows are proceedings front matter [S114; S126; S127; S143; S158; S159]. Where the cards say Dey's individual role cannot be separated from a large team, that is repeated where the work is used [S044 pp. 1–2; S047 p. 17; S064 pp. 10–14; S106 pp. 24–25; S110 pp. 1, 6].

Versions actually read, where they differ from the listed venue: S001 is arXiv v4 [S001]; S006 arXiv v3 [S006 p. 1]; S008 arXiv v1 [S008]; S061 arXiv v1 [S061 p. 1]; S105 arXiv v1 [S105]; S095 the December 2012 author preprint [S095 p. 1]; S104 the arXiv text under the earlier title [S104 p. 1]. Journal-version changes of these works are not read.

---

## 2. Evidence per existing method

Counts are distinct cards whose `method_links` name the method (in brackets: distinct works after merging the version pairs / of which read in full or in part).

| Method | Evidence | Variant | Contradiction | Say–do after full texts |
|---|---|---|---|---|
| M1 Solver habit → proxy theorem | 28 (26 / 24) | 24 (23 / 23) | 0 | ✅ stays; limitation on step 8 revised (§3 row 1); scope note (§3 row 2) |
| M2 Ground truth in a stripped instrument | 26 (25 / 23) | 31 (31 / 31) | 1 | ✅ in the branching and cut-measurement line; application papers do otherwise (§3 rows 4–5) |
| M3 Import the IP substructure paradigm | 46 (44 / 41) | 25 (25 / 23) | 0 | ✅ stays; variant: also imports algorithmic rules and closure operations, and once runs in reverse (§3 row 7) |
| M4 Demarcate every result | 90 (85 / 83) | 14 (13 / 13) | 0 | ✅ strongest recurrence of all five; scope: headline theory papers (§3 row 8) |
| M5 Certify with a cheap, strong relaxation | 34 (32 / 30) | 23 (23 / 23) | 2 | ✅ stays; two contradictions and five variants recorded (§3 rows 9–11) |

### M1 · Turn an unexplained solver practice into a proxy theorem

- **Strongest practice**: the sparse-cut line runs the whole loop: solver habit, missing theory, a one-sided geometric proxy, a measure fixed first, the result read back as a justification of practice [S084 pp. 1–2, 4; S028 pp. 1–3, 5]. The measure is chosen by discarding one that "can become infinity" [S028 p. 2]. The return to data is stated as "sparse cuts usually perform much better than the worst-case bounds we obtain theoretically" [S024 p. 4]. Pooling: unexplained PL MILP relaxations → tight factor-n theorem → practice beats the bound → MILP restriction built from the proof [S014 pp. 1, 5–6, 14–16, 28]. Branch and bound: random instances because the worst case is exponential, with "an indication" as the stated reach [S031 pp. 1–3; D003 pp. 1–3]; strong branching measured "in absolute terms" [S020 pp. 3–5]; a solver regularity (cuts enlarging trees) made into a provable property after removing confounders [S081 pp. 2, 9, 12–13]; dual decomposition on random two-stage instances [S120 pp. 1–4]; pre-specified sparse splits [S118 pp. 2–4]; feasibility-pump randomisation [S061 pp. 1–3]; sparse SDP bounds [S035 pp. 1–3; S122 pp. 4, 12–14, 21]; the default bilinear relaxation of spatial branch and bound [S021 pp. 1–2]; the ℓ1 surrogate for sparse PCA [S088 pp. 1–3].
- **Stated in the texts**: "given the complexity of solvers one cannot expect to be able to perform a theoretical analysis of this performance metric directly, and thus proxy measures are required." [S011 p. 4]; "In order to avoid worst-case lower bounds, a standard idea is to consider random instances." [S031 p. 2]; "existing theoretical guarantees are almost exclusively based on worst-case analyses, which predict exponential convergence behavior in the problem dimension and fail to explain the strong performance observed in practice." (from the sentence at [S120 p. 1]); "In order to simplify the question, we arrive at a data independent version of it" [S035 p. 1]. The NSF Sparse IP award names three solver habits to explain [S138].
- **Say–do update**: ✅, now on 24 full or partial works from 2014 to 2026. The report-the-mismatch form of step 7 is in the texts: "these results have so far failed to directly help in actual cutting-plane selection." [S011 p. 20]; practice beats the guarantee [S014 p. 28; S024 p. 4]. The step-8 limitation in SKILL.md needs correcting (§3 row 1).

### M2 · Measure against ground truth inside a stripped-down instrument

- **Strongest practice**: DP-optimal trees up to 20 binaries, ratio reporting and a word of caution [S020 pp. 11–13, 21–22]; a naive B&B with full strong branching as an oracle for fair node counting, stripped SCIP with the optimal value and seeds, instance ladder from random families to filtered MIPLIB [S081 pp. 8–11; S130 pp. 3–4, 23]; a textbook B&B where only the branching rule varies, optimal primal value given [S098 pp. 5, 8–10]; an expert ceiling evaluated first, with "However, when accounting for the time required to collect the cuts, most positive instances become negative, which motivates our learning approach." [S082 p. 9]; exhaustive enumeration as ceiling for cut generation [S048 pp. 9–12, 15]; facet enumeration of BQP_4–BQP_6 [S122 pp. 9, 14–15]; one round, no selection, a class where the relaxation equals the feasible set, then modified MIPLIB [S052 pp. 9–15, 23–24]; a Python B&B with relaxation-versus-branching ablation [S041 pp. 19–21]; a custom B&B with a fixed incumbent [S123 pp. 5–6]; a stripped column-generation instrument: "We exclude approaches that either modify the RMP or use alternative algorithms to solve the RMP, so that we can isolate the contribution of pricing." [S121 p. 4].
- **Small cases computed exactly before or inside a proof** (step 1): PORTA on n = 10 [S084 pp. 3, 17; S028 pp. 4, 18–19]; a computer check over a provably finite list of splits completes a counterexample [S018 p. 7]; exponential disjunctive LPs evaluate new Lagrangian bounds on small instances before any separation is built [D002 p. 21]; an exact Boolean LP as ceiling [S078 p. 10]; exact CG closure on small instances [S039 p. 7]; BARON ground truth at n ≤ 10 feeding conjectures [S129 pp. 10, 19–21]; a complete classification of SOCP/SDP outcomes on the two-bus system before larger counterexamples [S006 pp. 6–11]; a planted "actual" stiffness before real data [S060 pp. 13–18]; every bound scored against the exact z(b + Δb) [D004 arXiv p. 14]. A conjecture is kept open when computation supports but proof fails: "To date, every computational test we have devised suggests that this conjecture is true, but we have not been able to find a proof." [S122 p. 9].
- **Sanity checks in code**: a solver returning violated solutions is dropped ("We also discovered that Gurobi at times returns solutions with large constraint violations for this MINLP formulation." [S059 p. 18]).
- **Say–do update**: ✅ holds in the branching and cut-measurement line (S020, S041, S048, S052, S081, S098, S122, S123, S130). 31 works link to M2 only as a variant, almost all because no exact ceiling or stripped instrument is used (§3 row 4).

### M3 · Import the integer-programming substructure paradigm into QCQP and MINLP

- **Strongest practice**: MILP closure theorems asked of convex nonlinear sets, 2010–2014 [S018 p. 2; S042 pp. 1–2; D001 p. 2; S025 p. 2; S063 pp. 6–7]; subadditive duality carried to conic IP [S037 pp. 2–3]; Meyer's theorem for convex sets [S029 pp. 2, 17]; asked of MIQP whether it is in NP, as for MILP [S003 pp. 3–4]; the cost of term-by-term McCormick quantified [S021 pp. 1–3]; cycle substructures in power flow convexified jointly [S001 pp. 15–24; S009 pp. 4, 10–18; S008 pp. 5–18]; rank-one substructures for pooling: "Observe that all the non-convexity of the problem is now captured by the rank-1 condition." and "It is well-known that it is possible to obtain tighter convex relaxations when convexifing a set directly rather than using convex envelopes of functions describing the set." [S051 p. 2]; one quadratic over a polytope [S032 p. 2]; aggregations of quadratics [S071 pp. 1–5; S077 pp. 1–2, 27; S103 pp. 2–5, 11]; lifting and covers from 0-1 knapsack into separable bilinear rows [S135 pp. 1–2, 4–8; S105 pp. 1–2, 9]; separable power functions over a polytope [S129 pp. 1–2, 8, 11–17]; treewidth theory carried to continuous QP [S092 pp. 3–5, 13, 22–25].
- **Stated in the texts**: "A common and successful approach in integer linear programing is to generate cutting-planes implied by single constraint relaxation, see for example [8, 24, 11, 3]. We take a similar approach here." [S041 p. 2]; "To the best of our knowledge, however, no one from the global optimization community has ever exploited such results for convexification." [S032 p. 3] (T3.6 review: on p. 3 "such results" refers to the classical theory of ruled surfaces, which the authors learned of after proving their theorem; it is not a statement about convexifying sets cut out by several constraints. The relevant statement is on p. 2: function convexification "does not necessarily yield the convex hull", and there has been "much less work on explicit convexification of sets" [S032 p. 2].). The convex-MINLP NSF award states the MILP checklist as its objective [S146].
- **Exponential cost of the hull, as SKILL.md says**: "while the convex hull is SOCr, the construction involves the introduction of an exponential number of variables." (from [S032 p. 2]); the computational "light" version has no guarantee: "Unfortunately, there are no theoretical guarantees for the bounds of this light version of the relaxation." [S041 p. 5]; the exact hull is proved but four edge cuts are coded [S008 pp. 10–14].
- **Say–do update**: ✅, 41 full or partial works from 2010 to 2026. The specialist step (step 6) is confirmed with Blekherman [S077 pp. 1–2, 27; S119 p. 1; S035 pp. 1–3; S055 p. 7].

### M4 · Demarcate every result

- **Strongest practice**: MIQP in NP with three counterexamples, "tight with respect to the number of quadratic inequalities" (from [S003 p. 3]); pooling: tight bound for every scheme, inapproximability, a constructive attaining object, tightness of the restriction itself, a negative family [S014 pp. 6, 12, 16–18, 20]; aggregations: a counterexample for each dropped hypothesis and the simple rigorous box, "We just focus on a box whose validity proof is simple and rigorous." [S071 p. 18; pp. 5–9, 17–24]; forbidden vertices: each tractable case paired with hardness when one hypothesis is dropped [S022 pp. 2, 4–6, 8–10]; sparse cuts: upper bounds with near-matching random lower bounds and a negative packing class [S084 pp. 3–5]; McCormick gap: matching upper and lower bounds and an exact equality characterisation [S021 pp. 3, 6–11]; Geoffrion's theorem: a counterexample for the dropped hypothesis plus sufficient conditions [S112 pp. 2–8]; positive k = 2 and impossibility for k ≥ 3 with the gap stated open [S118 pp. 2–4]; exponential lower bounds for every encoding family [S117 pp. 12–19]; both assumptions of a regularisation theorem shown necessary [S080 pp. 9–11]; a cycle counterexample showing where a decomposable zero-gap dual needs a tree [S097 pp. 4, 8–9, 12]; NP-hardness, strict containments by explicit points, matching distance bounds, conjectures stated [S129 pp. 3, 7, 10–14, 21].
- **Stated in the texts**: "we also show that the verification scheme is not unrealistically strong" (from [S095 p. 17; S096 p. 11]); "a reasonable demarcation of conditions" (from [S071 p. 2]); "We do not know if the k-lattice-free closure of covering polyhedron is well-behaved." [S099 p. 7]; "While we have improved upon the bound presented in [34], we do not know if this new bound is tight." [S017 p. 5].
- **Say–do update**: ✅ with the widest base of the five (83 full or partial works, every period from 2008 to 2026). SKILL.md calls exclusivity the weakest check; the full texts do not change that, but they show the boundary as a headline object in at least S003, S014, S022, S071, S112, S117, S118. Scope note: §3 row 8.

### M5 · Certify with a cheap, strong relaxation

- **Strongest practice**: OPF: rank relaxations, strengthen the SOCP by cycle structure, pair with IPOPT, report the certified gap at 3375 buses with hardware [S001 pp. 1, 4, 14, 26–29]; the transmission-switching relaxation with proved gaps on stated hardware, and "our algorithm gives optimality guarantees by construction" (from [S005 p. 20]); LP/SOC-only spatial branch and cut [S008 pp. 8, 19–27, 30–33]; sparse PCA dual bounds up to n = 2000 [S017 pp. 3, 6–11, 14, 17; S057 pp. 6, 25–30]; an LP made to emulate the SDP: "we would like to obtain an outer approximation of the original set that can mimic the strength of the SDP relaxation, but that is lightweight and linear." [S048 p. 3]; floor layout: "Our assessment is that the lifted representations, while theoretically interesting, do not provide an off-the-shelf practical approach for this problem as they are too large and not sufficiently strong." [S100 p. 12]; network design dual bounds on industrial instances [S111 pp. 2, 20, 26–27]; a dual bound preserved under random projection [D005 pp. 1, 8, 12–13]; Lagrangian preferred to DP because bounds are available at any stop: "However, DP suffers from the disadvantage that we do not obtain any information on bounds until the algorithm terminates." [S097 p. 2].
- **Stated in the texts**: "Most conventional methods for solving SPCA are heuristics with no guarantees such as certificates of optimality on the solution-quality via associated dual bounds." [S017 p. 1]; "Recall that dual bounds are typically crucial for effective computational procedures for non-convex problems" (from [S057 p. 6]); the same complaint for model-free SPCA [S083 p. 1], structural model updating [S060 p. 27], network design [S111 p. 2] and grid security [S058 p. 1].
- **Say–do update**: ✅ (30 full or partial works, 2016–2026). Two contradictions and five variants are recorded in §3 rows 9–11.

### Heuristics and other SKILL.md items with new full-text practice

Counts are cards whose text names the heuristic (grep over `cards/*.md`).

- **H1 make hard instances and release them** (10 cards): new instances posted online [S051 p. 17]; a radial OPF library [S006 pp. 15–17]; generators printed in an appendix [S130 pp. 34–39].
- **H2 strongest baseline** (15 cards). Variant: when the strongest baseline is not run, the text says so: "We caution the reader that there are significantly more sophisticated methods for star (2-stage stochastic) problems [23]." [S104 p. 13]; "While this is a somewhat unfair comparison ... we report this result simply to show the potential improvements our new valid inequalities could offer" (from [S111 p. 26]); "we cannot and do not wish to draw conclusions regarding the performance of the spatial branch-and-bound algorithm." (from [S002 p. 12]).
- **H3 dead ends written in** (16 cards): "In preliminary tests, we implemented the algorithm WFP as described in the previous section. However, its performance was not competitive with FPorig." [S061 p. 12]; "Although, for our instances, we have not observed any lower bound improvement in SOCP/SDP relaxations by the inclusion of the valid inequalities, we obtain stronger root node relaxations in BARON." [S006 p. 22]; "However such a goal was too ambitious and we have had to considerably restrict it." [S052 p. 2].
- **H4 failed line → next programme** (7 cards); widened in §5.
- **H5 start from a result better than it should be** (2 cards): [S035 pp. 1–3; S123 p. 8].
- **H6 count every overhead** (10 cards): full timing [S082 pp. 9–12]; the tension is confirmed verbatim: "It is also self-evident, in our opinion, that all evaluated ML-based branching rules, if carefully implemented, would require significantly less computational effort per node than strong branching" [S098 p. 8], with the stated reason "We do not focus on total running time since this metric depends heavily on the quality of the software implementation" (from [S098 p. 8]).
- **H7 theory paper followed by a measurement-only paper** (4 cards): two-row cuts [S052 pp. 1–2]; lifted bilinear cover: theory [S085 pp. 1–7] then a computational paper whose stated entry is that the cut's computational usefulness had not been evaluated [S105 p. 4].
- **H8 specialist and student** (4 cards): Blekherman on the real-algebraic steps [S035; S055 p. 7; S077 pp. 1–2; S119 p. 1].
- **H9 borrow one tool** (13 cards): Aczél's functional equations [S019 p. 6]; WalkSAT [S105 p. 9; S061 p. 4]; Shapley–Folkman [S125 pp. 10–16]; Gaussian random projection [D005 p. 8]; Gershgorin [S105 pp. 5–7].
- **H10 design then verify**: still one project line, now read in both versions: "First we design a useful cutting-plane without considering its validity. Then, once the cutting-plane is designed, we verify whether it is valid." [S096 p. 2]; "First we design cutting-planes which we believe will be useful without considering their validity." [S095 p. 1]; the CAREER award states it as one of three paradigms [S141]. No later project uses it in the read texts.
- **Workflow D step 4 (findings against your own premise)**: "Surprisingly, the best solutions do not tend to be among the closest, with the exception of the 300kocuk case with cardinality 5." [S044 p. 20]; "Contrary to expectation, 19.8% of the cuts led to an increase in tree size." [S081 p. 9].
- **Taste 5 (sparsity as structure)**: interaction graphs and chromatic numbers as instance parameters [S024 pp. 5–9, 12–13]; block decomposability carried into the feasibility-pump analysis [S061 pp. 3, 12]; tree decompositions of the intersection graph make a general MIP dual decomposable [S104 pp. 2, 9]; the closing advice of the eigenvector-cut paper: "Overall, our results suggest that progress in strengthening SDP relaxations for QCQPs is more likely to come from identifying and exploiting sparse, well-structured inequalities rather than from pursuing increasingly dense eigenvector-based cuts." [S122 p. 22].

---

## 3. Variants and contradictions

Full texts win over the web-research notes 01–06. Nothing is deleted; each row says what should change in SKILL.md.

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
| 10 | M5 step 2 ("rank candidate relaxations") | The ranking is often done by theorem, and the heavier relaxation is proved to add nothing before cheap cuts are offered: lifted LP, lifted SDP and an earlier SDP all equal a closed-form bound [S100 pp. 9–10]; an SOCP relaxation proved at least as strong as SDP ∩ QBP [S041 p. 3]; "We show that, surprisingly, for the class of separable instances, the SDP relaxation gives a bound equal to that of the McCormick relaxation." [S105 p. 4]; "Interestingly, adding the SDP constraint (3) to the P relaxation does not further strengthen this relaxation as proven below." [S129 p. 5]; six relaxations ordered in projected space before one is strengthened [S001 pp. 11–14]. The device is a PSD completion "rank one plus a sparse or diagonal correction" [S105 pp. 5–7; S129 p. 5; S001 pp. 11–12]. | as cited | **Variant note** on M5 step 2: "where possible prove the ranking; a PSD completion of the cheap optimum shows the SDP adds nothing." Not a new method (it is M5's own step). |
| 11 | M5 steps 3–4 | Step 4's feasible point often comes from an MILP restriction built from the same discretisation or proof as the relaxation, not from a local solver [S014 pp. 14–16; D002 pp. 22–25; S051 pp. 10–11, 17–18; S080 pp. 18–19]. Step 3 includes constraints redundant for the primal that strengthen the dual or the solver bound [S104 pp. 3–5; S117 pp. 2, 13; S111 p. 16]. The cheap object can be a DNN/SDP restriction of a copositive dual [D004 arXiv pp. 11, 13–14]. | as cited | **Variant notes** on M5 steps 3 and 4. |
| 12 | M5 limitation: "In 2017 he qualified his 2016 claim: 'not very competitive against the SDP relaxation, especially for easier instances'" | The sentence is in the spatial branch-and-cut paper read as arXiv v1: "Strong SOCP relaxations from our previous paper [27] improves the plain SOCP relaxation considerably but it is not very competitive against the SDP relaxation, especially for easier instances." [S008 p. 31]. The 2016 paper's own comparison section already says "We note that our SOCP based relaxations are not as successful according to this comparison." [S001 p. 30]. | [S008 p. 31; S001 p. 30] | **Revise** the attribution: the qualification is already in the November 2015 arXiv v4 of the 2016 paper and repeated in the March 2017 preprint of the 2018 MPC paper; journal texts not read (wording corrected in the T3.6 review). |
| 13 | Honest boundary: Strong SOCP "exact reformulation" (v1) → "relaxation" (v4) | Only v4 was carded [S001 p. 1]; v1 was not read. | [S001] | **Unchanged, flagged "not re-read in full text"**. |
| 14 | Taste 2 (data-independent bounds) | Supported [S035 p. 1; S024 pp. 5–9; S079 pp. 3, 5], but a 2020 paper sells a data-dependent grouping against the authors' own earlier bounds: "However, these bounds are entirely data-independent." [S040 p. 5]; early relaxation-strength bounds are data-dependent [S010 pp. 9–10, 13]. | as cited | **Add a nuance**: data independence is a taste for theorems, not for algorithms that must use the data. |
| 15 | Anti-pattern "facetness or depth of cut as proxies for usefulness" | 2010 papers still use extremality and a merit index as strength yardsticks [S019 pp. 6, 20]. A 2026 paper uses depth as its proxy measure [S122 pp. 4, 12–14] and still concludes for sparse structured cuts [S122 p. 22]; another finds the richest encoding family worst in practice: "greater expressive power does not necessarily translate into a better algorithm." [S117 p. 32]. | as cited | Keep the anti-pattern; **add the dates** (facet yardsticks before 2011, doubt from 2018) and S117 as practice evidence. |
| 16 | Honest boundary U4 "reuse information across re-solves: practice 'preliminary'" | Four works built on recurring instances (§4). | [S044; S098; S082; D004 = S067] | **Overturned**: U4 leaves the unverified list and becomes Method 6 (§4). The Anti-patterns row "his practice: preliminary" changes accordingly. |
| 17 | Honest boundary "Not read: ... most final journal texts, proofs and most computational tables of the signature papers" | 116 works now read in full or in part, proofs and tables included (§1). Many were read as arXiv or author preprints. | §1 | **Revise**: "read as preprints in most cases; journal-version changes not read; the thesis, the 2009 survey chapter and the IPCO 2008 lifting paper remain abstract-level [S074; S030; S015]." |
| 18 | SKILL Trajectory T2 ("Wolsey's question at CORE") | The other side's voice confirms it: "Later when Santanu Dey came to Core, my main concern was how to deal with integer non-basic variables, which again led him far beyond what was initially asked." [S079 p. 9] (Wolsey, discussion column). | [S079 p. 9] | **Add** the card as evidence (other voice). |

---

## 4. Promotions

### Proposed Method 6: Exploit the re-solve. When the same model recurs with new data, prove what carries over, reuse it, keep the certificate

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

### Considered and not promoted

- ***Prove the heavier relaxation adds nothing before offering the cheap one*** (S100, S041, S105, S129, S001: five works, all four checks arguably pass). Not promoted because it is M5's step 2 done by theorem; a separate method would duplicate M5. Filed as a variant (§3 row 10).
- ***One construction, both bounds: a relaxation and a restriction from the same discretisation*** (S014, D002, S051, S080: four works). Same reason: it is M5 step 4 plus M1 step 8. Filed as a variant (§3 row 11).
- **"Re-prove the classical lemma by your own route"** (seven works). Fails exclusivity; becomes a heuristic (§5).

---

## 5. New heuristics

SKILL.md has 10 heuristics, the top of the framework's 5–10 range. One heuristic is added and one existing heuristic is widened by merge. If the cap is enforced in the SKILL edit, H10 (design then verify) is the one to fold away: it remains a single project line in full text (§2).

> T3.6 review: the 5–10 cap was enforced. H10 (design then verify) is folded into Method 3 as a variant; H11 is renumbered H10 in SKILL.md (ledger `#folded-design-cut`, `#heuristic-10`).

### H11 (new) · Re-prove the classical lemma you lean on by a route that exposes the one property you use, then push the route past the classical statement

- **Evidence (7 works, 2019–2026, six coauthor groups)**: one-point fixability of mixing-set triangles, already known, re-derived by more geometric techniques to get pyramids and spindles as a reusable tool [S056 pp. 4, 8–12]; a symmetric three-quadratic S-lemma proved because the existing one is asymmetric [S071 pp. 3–4, 10–11]; hidden convexity restricted to every hyperplane so the old proof road-map extends and earlier theorems become corollaries [S077 pp. 4–6, 16–17]; the Boolean-quadric eigenvector family re-derived through CG rounding, yielding a new hierarchy [S122 pp. 3, 7–9]; a face-dimension proof of Shapley–Folkman pushed to a vanishing bound [S125 pp. 10–16]: "To the best of our knowledge, this is the first result establishing an asymptotically vanishing nonconvexity measure for Minkowski sums of nonconvex sets within the framework of the Shapley–Folkman Lemma." [S125 p. 4]; the treewidth LP re-proved through LP duality: "The dual to the LP is the DP formulation for solving such problems over known tree decompositions." [S153 p. 5]; random projection redesigned around the property the proof needs: "Our key observation is that the JL lemma itself is not essential for preserving bilinear structures." [D005 p. 8].
- **Steps**: (1) write down which property of the classical lemma your proof actually touches; (2) re-prove it by a device that isolates that property (geometric, LP-dual, face-dimension); (3) restate the hypothesis as that property; (4) push the device one step past the classical bound and recover the old results as corollaries.
- **Checks**: recurrence ✅; say–do ✅ (stated in the texts [D005 p. 8; S071 pp. 3–4; S153 p. 5]); executable ✅; exclusivity ✗ (common in mathematics; and the MIQP-in-NP paper does the opposite, keeping both classical proofs as black boxes [S003 pp. 1, 3]). → heuristic.

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

---

## 6. Candidate pool (not promoted)

| Cluster (meaning) | Cards | Distinct works | Why not promoted / where it went |
|---|---|---|---|
| Redundant "helper" constraints that change only the relaxation or dual; first prove which class cannot help | S097 = S104 [S104 pp. 3–5], S117 [S117 pp. 2, 13], S111 [S111 p. 16] | 3 works, 2 independent lines (S117 continues S097/S104 [S117 p. 2]) | Folded into M5 step 3 (§3 row 11). Heuristic-eligible; held back for the 10-heuristic range. RLT already adds redundant products, so exclusivity is weak [S104 p. 5]. |
| Exact reformulation that exposes structure in network physics (cycles, block-diagonal ISF, convex energy program) | S001 [pp. 16–18], S008 [pp. 3, 8–9], S009 [pp. 4, 10–18], S047 [pp. 3, 9–11], S059 [pp. 10–12, 27–28], S075 [pp. 3, 11] | 6 | Evidence for M3 step 2 and M5 step 3; no separate method. |
| Relax, then restore one realism at a time | S079 [pp. 5–8], S013 [pp. 3, 8], S016 [pp. 1–2], S065 [pp. 1–2] | 4 (2009–2015) | M1 variant (§3 row 3). Period-bound. |
| Classify all outcomes on the smallest instance; simulate the exactness condition, then prove the dominant case | S006 [pp. 6–15], S129 [pp. 14–17], S055 [p. 7], S089 [pp. 3–4], S130 [pp. 4–7, 31] | 5 | Evidence for M2 step 1. |
| Theory picks the stress axis (sweep the parameter the bound depends on) | S109 [pp. 17–18], S006 [pp. 12–15], S009 [pp. 28–29], S052 [p. 15] | 4 | M2 variant (the instrument's varied factor comes from the theorem). |
| A named open question or a classical theorem's hidden hypothesis as the entry | S021 [pp. 1–3], D001 = S025 [S025 pp. 2–3], S003 [pp. 1, 3], S112 [pp. 1–5], S056 [p. 3] | 5 | Fails exclusivity and "different from standard"; noted as a second problem source for Workflow A. |
| Replace a dropped hypothesis (rationality, finiteness) rather than only refute it | S037 [p. 3], S029 [pp. 2, 17], D001 [pp. 3–4, 6], S043 [p. 14], S112 [pp. 1–5], S116 [pp. 4–5] | 6 | M4 step 3 variant (§3 row 8). |
| A proof distilled into a selection slogan | S011 [pp. 18–19], S122 [p. 22] | 2 | Writing move (§7.4). |
| Count near-optimal solutions to bound enumeration effort | S031 = D003 [S031 pp. 6–10], S120 [pp. 6–8] | 2 lines | Proof device (§7.1). |
| Optimise the instance to maximise the gap between two relaxations | S078 [pp. 10, 12–13], S088 [pp. 12–14] | 2 | Proof/evaluation device; M4 step 1 support. |
| Compose low-dimensional facets into high-dimensional ones | S026 [pp. 16–20], S046 [pp. 8, 14], S066 (abstract) | 3 (2 read in part) | Period-bound (2007–2010) proof device. |
| Prove on the infinite (all-columns) model, transfer to finite; finite-check reductions | S016 [p. 8], S019 [pp. 8–10], S026 [pp. 6–11], S053 [pp. 5, 7, 18] | 4 | Proof device (§7.1). Period-bound. |
| Convex integer program as dual bound for convex maximisation | S057 [pp. 6, 18–19], S064 [p. 14], S017 [pp. 5–8] | 3 (one line) | M5 evidence. |
| Choose the dual inside the ε-optimal face for its downstream use | D004 = S067 [S067 pp. 9–12] | 1 | Part of Method 6 step 4. |
| Design then verify | S096 = S095 [S096 p. 2], S141 (abstract) | 1 line | Stays H10. |
| Paired relaxation and restriction from one construction | S014, D002, S051, S080 | 4 | M5 variant (§3 row 11). |
| Prove the heavier relaxation adds nothing | S100, S041, S105, S129, S001 | 5 | M5 variant (§3 row 10). |
| Singletons (one card each) | fixed-point bound tightening [S010 pp. 7–10]; cheap-oracle screening before exact evaluation [S004 pp. 4–5, 18]; attribute the gap to its nonconvexity source [S005 p. 18]; approximation algorithm as warm start [S023 pp. 1, 16]; submodular pricing in column generation [S027 pp. 8–14]; branching rule read off the relaxation's construction [S041 pp. 4, 12–14]; lagged coupling constants as robust bounds [S047 p. 14]; diagnose the stalled side with off-the-shelf solvers [S075 pp. 1, 11, 23]; closed-form inner value → support selection [S076 pp. 5–9]; regularise to make the relaxation exact [S080 pp. 3, 6, 15]; aggregate exact solutions of small restricted subproblems [S100 pp. 2–4]; cover-not-fit parameter policy [S121 p. 21]; bound tightening read off child relaxations [S123 pp. 2–4]; nested-monotone reformulation for a TU block [S124 pp. 7–11]; report branching results at fixed primal gaps [S130 pp. 5, 23, 25]; independent original-space checker [S110 pp. 3–4, 13–15]; adversarial-oracle separation of solver rules [S020 pp. 9, 17–18]; tiny matrices separating a class from prior conditions [S068 pp. 3–5]; consolidate-then-extend [D002 pp. 2, 7–8]; unify two classical results [S003 pp. 1, 3]; lift a known equivalence one dimension up [S036 pp. 2, 18, 25]; encoding-sensitivity table and sandwich hardness [S022 pp. 1–5, 9–10]; gadget polytope transferring separations [S095 p. 9]; rank lower bound from a per-round factor [S099 pp. 4, 7] | 1 each | Below the ≥2 threshold for a cluster; kept for later rounds. |

---

## 7. Technique inventory

### 7.1 Proof devices

| Device | Cards |
|---|---|
| Disjunctive extended formulation of a union, then Fourier–Motzkin (or approximate) projection | [S002 pp. 8–9; S004 pp. 6, 8–11; S009 pp. 11–14; S091 pp. 5–7; S051 pp. 23–28; S135 p. 6; S085 p. 6; S111 pp. 8–9; S092 p. 8; S062 pp. 9–10] |
| Extreme-point characterisation: at most one or two fractional variables, so the hull is a union of small-support pieces | [S041 pp. 6–7; S051 pp. 4–7; S032 pp. 4–10; S129 p. 5; S135 p. 4; S085 p. 4; S070 pp. 21, 24] |
| PSD completion of a cheap relaxation's optimum (*rank one + sparse or diagonal correction*) to show SDP adds nothing | [S105 pp. 5–7; S129 p. 5; S001 pp. 11–12] |
| Scaling sandwich / α-approximation: compare closures by the factor α with U ⊆ αV | [S079 p. 7; S011 pp. 18–19; S039 p. 8; S107 pp. 4–7; S099 pp. 4–7; S085 p. 7; S017 pp. 11–14; S083 p. 4] |
| Randomised sparsification or rounding of a dense normal or eigenvector, with Bernstein/Chernoff and a union bound | [S084 pp. 6–8; S028 pp. 7–9; S011 pp. 12–13; S035 pp. 11–13; S057 pp. 10–11; S088 pp. 5–9; S125 pp. 12–16; D005 pp. 8–13] |
| Averaging / midpoint arguments (mirror-image solutions, all k-subsets, convex combination of two points) | [S100 pp. 8–9; S086; S034 p. 14; S028 pp. 9–10; S035 p. 8; S153 pp. 12–13; S046 p. 20] |
| B&B tree-size counting: best bound never branches below OPT, charge nodes to good points, slab bounds over random columns | [S031 pp. 4–10; D003 pp. 4–13; S120 pp. 6–20; S020 pp. 14–15; S034 pp. 7–11; S081 pp. 7–8] |
| Small explicit counterexample or gadget for each dropped hypothesis | [S003 pp. 2–3; S019 pp. 11–14; S071 pp. 17–24; S073 p. 8; S097 p. 9; S103 pp. 22–27; S112 pp. 4–5; S119 pp. 9–15; S122 pp. 6–7; S124 pp. 11–13; S125 pp. 14, 17; S080 pp. 9–10] |
| Hardness by reduction (subset sum, vertex cover, max-cut, partition, edge colouring, 2-hyperplane separability) | [S010 p. 5; S022 pp. 4–6; S003 p. 2; S009 pp. 8–9; S014 p. 12; S007 pp. 7–12; S062 pp. 4–5; S129 p. 3; S040 p. 9; S067 pp. 16–18] |
| Dirichlet / Kronecker approximation, Hermite normal form and unimodular normalisation for irrational or lower-dimensional data | [D001 pp. 3–6; S025 pp. 4–7; S042 pp. 6–11; S043 p. 14; S116 pp. 3–5; S018 p. 4; S033 pp. 11, 13] |
| Geoffrion's primal characterisation of the Lagrangian dual (and when it is exact) | [S097 p. 5; S104 pp. 5, 17–18; S112 pp. 1, 5; S125 pp. 8–9] |
| Tree-decomposition induction (leaf peeling, bag consolidation) | [S097 pp. 20–21; S104 pp. 20–22; S092 pp. 22–26; S153 pp. 13–15] |
| Spectral tools: Cauchy interlacing, S-lemma variants, Schur complements | [S035 p. 10; S055 p. 9; S071 pp. 10–14; S077 pp. 23–26; S119 pp. 5–6; S129 pp. 9–10] |
| Facet proofs by affinely independent point families; Facet Theorem with equality sets | [S009 pp. 15–16; S026 p. 12; S046 p. 12; S016 pp. 15–18; S045 pp. 9–10] |
| Finite-check reductions and compactness (finite subcover) | [S026 pp. 6–11; S053 pp. 5, 7; S013 p. 14; S025 pp. 14–15; S042 pp. 8–10; S018 p. 7] |
| Computer-checked or computer-algebra steps inside a proof | [S018 p. 7; S055 p. 7; S071 pp. 17–24; S078 pp. 10, 12–13] |

### 7.2 Design moves

| Move | Cards |
|---|---|
| Find the substructure that carries all nonconvexity (rank-one lift, cycle condition, per-line coupling) and convexify it jointly | [S051 pp. 1–2; S008 pp. 5–18; S001 pp. 15–24; S006 pp. 6, 18–20; S032 p. 2] |
| Exact hull for the theorem, few-inequality outer approximation for the code | [S008 pp. 10–14; S041 pp. 3–5, 17–18; S105 p. 2] |
| A relaxation of the relaxation that one rounding argument can bound for every scheme | [S014 p. 7] |
| Turn the constructive step of a bound proof into a heuristic, then into a MILP restriction that inherits the guarantee | [S014 pp. 6, 12, 14–16] |
| Use the cheap LP ranking to predict which MILP discretisation will win | [S051 p. 20] |
| Reduce cut separation to a problem of another field and adopt its heuristic as oracle (SPCA, TPower; WalkSAT-style repair) | [S048 pp. 6–7, 15; S105 p. 9; S061 p. 4] |
| Keep the classical algorithm; change only the failing step, with a conservative fallback | [S061 p. 12; S130 pp. 4–8] |
| Add constraints redundant for the primal that are separable after dualising | [S104 pp. 3–5; S117 pp. 2, 13] |
| Ordered or nested reformulation of assignment binaries to get a totally unimodular block | [S124 pp. 7–11] |

### 7.3 Experiment and evaluation protocols

| Protocol | Cards |
|---|---|
| Stripped textbook B&B; the expensive rule as oracle for fair node counting; presolve, cuts and heuristics off | [S130 pp. 3–4; S081 pp. 8–11; S098 p. 5; S041 pp. 19–21; S123 pp. 5–6; S103 pp. 6–9] |
| Exact ceiling first (DP-optimal trees, enumeration, facets, exponential LPs, global solver at small n, planted optimum) | [S020 pp. 11–13; S048 pp. 9–12; S122 pp. 9, 14–15; D002 p. 21; S129 pp. 19–21; S060 pp. 13–18] |
| Control the incumbent: optimal or best-known primal supplied, or results at fixed primal gaps | [S098 p. 5; S123 p. 5; S082 pp. 7–8; S130 pp. 5, 23, 25] |
| Two protocols by what theory says: "same bound, compare time" when bounds are proved equal; "same time, compare bound" otherwise | [S100 p. 11; S105 pp. 10, 13] |
| Instance ladder: structured random families for design and tuning, then filtered public benchmark with seeds | [S130 pp. 4, 23; S081 pp. 8–11; S052 pp. 9–15, 23–24] |
| Feature-isolating synthetic families; difficulty drivers isolated against the default solver before any method | [S052 p. 15; S010 pp. 5–6] |
| Certified gap at full scale with named hardware and time limits | [S001 pp. 1, 4, 26–29; S017 pp. 14, 17; S100 p. 11; S051 p. 17; S080 pp. 19, 21–22; S111 pp. 26–27] |
| Speed-up decomposed into its sources (LP vs MIP evaluations, CGLP overhead) | [S004 pp. 17–20] |
| Drop a solver that returns violated solutions; state what the framework cannot prove | [S059 pp. 18, 24] |
| Several seeds; single-thread; node limits | [S061 p. 12; S124 p. 14; S081 pp. 8–11] |

### 7.4 Writing moves

| Move | Cards |
|---|---|
| A "Main results" or overview section with every theorem before any proof | [S014 pp. 5–6; S084 pp. 3–6; S021 pp. 3–4; S020 pp. 4–5; S024 pp. 2–15; S035 pp. 3–7; S065 pp. 1–4; S039 p. 2; S117 pp. 2–4; S120 pp. 3–4] |
| Two-sided theorem statements (bound + tightness; algorithm + inapproximability) and the weak-looking factor defended at once | [S014 p. 6] |
| Practical reach stated as "an indication", never as a full explanation | [S031 p. 1; D003 pp. 1, 3; S118 p. 4] |
| A word-of-caution paragraph and a defence of the programme | [S011 pp. 20–21; S081 pp. 12–13] |
| A proof distilled into a selection slogan | [S011 pp. 18–19; S122 p. 22] |
| Surprise flagged against the authors' own expectation ("Surprisingly", "Interestingly", "Contrary to expectation") | [S084 p. 1; S105 p. 4; S129 pp. 3, 5; S081 p. 9; S044 p. 20; S019 p. 2] |
| Numbered open questions, split theory/practice | [S079 pp. 7–8; S014 pp. 27–28; S039 p. 8; S035 pp. 3–7] |
| Experiments driven by explicit numbered questions; "possible interpretations" after each table | [S048 p. 9; S052 pp. 12–13] |
| One running or toy example threaded through the text, or a numerical example before a structural identity | [S079 p. 4; S153 pp. 5–15; S047 p. 8; S130 pp. 4–7] |
| Version note stating what changed from the conference version | [S031 pp. 1–4] |

---

## 8. Trajectory as seen in the full texts

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

---

## 9. Collaboration pattern

Counts are full or partial cards naming the coauthor (version pairs counted twice here).

| Period | Main coauthors (cards) | Pattern |
|---|---|---|
| 2007–2010 | Richard 4 [S019; S026; S046; S072]; Wolsey 3 [S013; S016; S053] | Advisor and postdoc host; group-relaxation theory. |
| 2011–2015 | Vielma 5 and Dadush 4 (closures) [S018; S042; D001; S025; S037]; Ahmed 5 [S002; S010; S022; S091; S070]; Molinaro 3 (sparse cuts) [S084; S028; S065]; Morán 3 [S043; S037; S029]; Angulo 3 [S022; S091; S070] | A closure-theory partnership, the junior-faculty mentor on applied IP, and the start of the Molinaro partnership. |
| 2016–2020 | Molinaro 8 [S003; S021; S011; S024; S061; S088; S039; S099]; Kocuk 6 and X. A. Sun 5 (OPF) [S001; S006; S009; S005; S008; S051]; Ahmed 6 [S004; D002; S044; S078; S040; S049]; Del Pia 4; G. Wang 4; Santana 4 [S032; S051; S073; S041] | Theory with Molinaro; applications carried by students co-advised with a domain colleague. Ahmed's last papers here; he is marked deceased at submission on the 2020 heuristic paper [S044 p. 1]. |
| 2021–2026 | Molinaro 8 [S031; S035; D003; S020; S081; S120; S034; S057]; Xu 8 [D004; S097; S104; D005; S067; S118; S120; S125]; Shah 5 [S020; S130; S081; S121; S086]; Dubey 4; Blekherman 4 [S035; S055; S077; S119]; Muñoz 4; Gu 4; Cifuentes 4; Sahinidis 5 incl. one editorial and one undated note [S059; S075; S109; S094; S153]; Qiu and Xavier 3 (Argonne) [S098; S047; S082] | Molinaro remains the constant theory partner (19 cards, 2014–2026). Students lead the duality (Xu), branching (Shah, Dubey) and QCQP/FEM (Han, Y. Wang [S103; S123]) lines. Mathematicians are brought in for real-algebraic steps (Blekherman). Former students return as coauthors (Kocuk [S129; S119]; Morán [S112; S118]; Angulo [S117]). |

Students as first authors or carrying the line, as the cards record them: Gupte [D002 p. 1], Kocuk [S009; S005], Johnson [S044 pp. 1–2], Xu [D004 arXiv p. 1], Dubey [D003], Redder [H001], Greening [S111], Choudhary [S153 p. 1]. The cards could not separate Dey's own share in the team papers named in §1.

---

## 10. Rejected updates

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

---

## 11. Open gaps

- **Works without an open text** (abstract or metadata only): the PhD thesis [S074]; the IPCO 2008 lifting paper [S015]; the group-theoretic survey chapter [S030]; the 2010 two-row experiments [S038]; the ellipsoid CG-closure paper [S054]; the pooling technical report and overview [S012; S090]; MIPLearn [S087]; the OPF bound-tightening paper [S128]; the network-design dual-bound conference version [S131]; row-sparse PCA [S161]; the treewidth-convex hull note [S157]; "Gomory functions" [S102]; floor layout [S166]; EV charging [S132; S154; S155]; selective optimization [S139]; closedness of SOC sets [S140]; the NSF award records [S138; S141; S146]. So the 2007–2009 origins of M3 and of the multi-row programme rest on abstracts and on the 2009 survey [S079 pp. 2–8].
- **Partial reads**: 30 cards read only parts; proofs of several 2010–2013 closure and lifting papers are not read in detail [S026; S029; S043; S046; S053; S072]; appendix proofs of the floor-layout equivalences [S100 pp. 9–10]; journal-version changes of all works read as preprints (§1).
- **Strong SOCP version change**: v1 not read; the SKILL.md claim rests on the web-research note [S001].
- **Method 6**: three of four works are preprints; whether the license-then-reuse pattern survives refereeing, and how much of it is Dey's rather than the Argonne collaborators' [S098; S082], is not visible in the texts.
- **Say–do on the stated side**: the cards are papers, mostly co-authored; Dey's own voice (talks, interviews) is not in the card corpus, so "stated" in this note means co-signed text.
- **Supervision, refereeing, coding**: no card evidence beyond acknowledgements and guest-editor prefaces [S094 p. 5; S113]; the gaps listed in SKILL.md's "Stages without a distillable Dey method" stand.
- **Undated and misattributed rows**: S153 is undated (no earlier than late 2024 by its references) [S153 p. 1]; S144 and S145 belong to a different S. Dey and should stay excluded [S144; S145].

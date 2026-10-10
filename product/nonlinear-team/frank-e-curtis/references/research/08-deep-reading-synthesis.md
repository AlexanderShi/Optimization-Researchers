# Frank E. Curtis · Deep-reading synthesis

> Date: 2026-10-10. Input: every card in `cards/` (31 batch files, 96 card entries for 96 works; index in `07-paper-cards.md`, generated from the digests). Rules applied: `references/paper-reading-card.md` §3 (conservative update: append only, existing methods get evidence before anything new, a new core method needs ≥3 distinct works plus the four checks, reject updates without explanatory power, every claim traceable to a card) and `references/research-extraction-framework.md` §3 (four-way validation) and §11 (quality checklist). This note proposes changes; it does not edit `SKILL.md`. The base-tier skill was built on 2026-09-28 from web research only (01–06); this is the first deep-reading round, so there are no earlier decisions to keep or overturn.
>
> Citation form: `[S012 p. 9]` = card S012, page of the extracted text as recorded on the card (file pages; several cards give the journal-page offset in their header); `abstract` = abstract-level card; `TR` / `arXiv` = the card read that version. Quotation marks surround only text that is in a card's verified Quotes list (`verify_card_quotes.py`: 180 of 180 exact).
>
> Counting rules: five possible journal/preprint pairs are indexed separately and are unconfirmed: S045 ~ S037, S031 ~ D001, S072 ~ S069, S060 ~ S061, S063 ~ D002. Each pair counts once in every tally and threshold below. S058, S081 and S086 are pre-PhD combinatorial-matrix work (2003–2006, outside the skill's scope) and carry no weight for or against the solver methods. Papers where the cards record Curtis as third author in a co-author-led project (S018, S073, S083), and the joint competition overview S023, are counted but noted where they carry a decision. Cards also record reading notes about inconsistencies inside individual works; those are not findings about the researcher and are not used here.

---

## 1. Coverage

| Item | Count | Source |
|---|---|---|
| Works on the publication list / indexed | 96 / 96 | `../sources/publications/works.json`, `../sources/papers/INDEX.md` |
| Works with a card | 96 (no skips) | `07-paper-cards.md` |
| Distinct works after merging the five possible pairs | 91 | header rule |
| **Read in full** | **86** (no partial reads) | read-level column |
| Abstract-level | 8: S031, S045, S055, S060, S072, S074, S078, S079 | batch a2-01 |
| Metadata only | 1: S084 (title only) | a2-01 |
| Unreadable | 1: S086 (2003 William & Mary thesis; garbled Type3 text layer, no OCR available; combinatorics, outside scope) [S086] | c01 |
| Quotes verified exact | 180 / 180 | `verify_card_quotes.py` |

Full reads by period (full / carded): 2003–2007 4/5; 2008–2012 9/10; 2013–2017 19/19; 2018–2022 27/28; 2023–2026 27/34. Every paper the skill names as a signature work was read in full: inexact SQP [S006], infeasibility detection [S009], PIPAL [S033], SQP-GS [S003], BFGS-SQP with relative minimization profiles [S004], TRACE [S002], stochastic SQP [S007], and the dissertation [S096]. The abstract-level gap sits mostly in 2023–2026 (six of the eight abstract cards and the metadata card).

S074, the 2025 SIAM book *Practical Nonconvex Nonsmooth Optimization*, is known only from the publisher's description as reproduced by a retailer, a secondary source [S074 abstract]; nothing below rests on it.

---

## 2. Evidence per existing method

Counts are distinct cards whose `method_links` point at the method (a card can give both evidence and a variant). *Works* merges the five possible pairs. All links come from full cards except these abstract-level ones: M1 S045; M2 S055; M5 S031, S045, S060.

| Method | Evidence ✅ | Variant ⚠ | Contradiction ✗ | Cards with any link | Works with any link |
|---|---|---|---|---|---|
| M1 The inner solve serves the outer solver | 22 | 23 | 1 (S094) | 45 | 44 |
| M2 Steer, don't switch | 20 | 37 | 1 (S089) | 54 | 53 |
| M3 Break it on purpose | 10 | 20 | 0 | 30 | 30 |
| M4 Audit the yardstick | 32 | 18 | 2 (S026, S066) | 51 | 51 |
| M5 Fair-fight benchmarking | 47 | 39 | 9 | 78 | 74 |

All five methods survive the full texts; none is contradicted at its core. The high variant count of M2 has one main cause: readers filed 15 cards with an adaptive rule *outside* the objective–feasibility trade-off as Method 2 variants with no penalty or merit parameter, e.g. [S024 pp. 3, 13, 16; S028 pp. 2–4; S067 pp. 7–8; S042 pp. 2, 5, 11; S064 p. 12; S002 pp. 7–9; S008 pp. 2, 21; S047 pp. 3–5; S050 arXiv p. 5]. That cluster is what §4 promotes. The M5 contradictions are discussed in §3 rows 10–12.

### M1 · The inner solve serves the outer solver

- **Strongest practice**: the dissertation states the question in its first technical chapter, "The main purpose of this chapter is to determine the accuracy with which the SQP subproblems must be solved in order to ensure global convergence in the context of a practical algorithm for problem (2.1)." [S096 p. 23], with merit-model tests on separate primal and dual residuals [S096 pp. 26–29], and closes on "A major theme in this work has been the importance of tying various aspects of the optimization process into one cohesive unit." [S096 p. 98]. The same tests run through the equality, rank-deficient, nonconvex and interior-point rungs [S006 pp. 5–7; S025 pp. 6–8; S017 pp. 2, 10–11; S010 pp. 8–10, 18] into Ipopt [S036 pp. 6–7, 11–17], into the QP solver itself ("In this manner, the QP solver iterates until the needs of the (outer) algorithm are met." [S029 p. 13]; [S057 pp. 5, 7–9]), into gradient sampling [S065 pp. 7–10], inexact TRACE [S043 pp. 6–7, 16–17], stochastic SQP [S037 pp. 6–7] and NonOpt's tailored QP solver [S088 pp. 3, 9, 14, 17].
- **Stated in full texts** (new; the skill relied on the research page): "the benefits of these techniques are only realized if inexact step computations are allowed and controlled appropriately in order to guarantee global convergence of the algorithm." [S010 p. 2]; the inexact column-and-constraint paper's "allowing inexactness is not something that can be done naively." [S016 p. 4]; a dynamic-tolerance shortcut "will not ensure convergence unless one imposes strong requirements on the employed linear system solver" [S064 p. 2].
- **Say–do update**: ✅ stays, now with a primary stated side from 2007 [S096 pp. 23, 98] to 2023 [S016 p. 4]. Practised 2007–2026.
- **Correction (full text beats the web snippet)**: Method 1 step 6 cites, from the research page, a time per iteration of under 9 minutes against about 40 minutes for default Ipopt, attributed to 10.1137/090747634. That paper (card S010) reports total CPU seconds per mesh level (e.g. 3,402 s against 33,704 s at N = 50) and no per-iteration minutes [S010 p. 25]. The full-text scale claim is in the implementation note: "Specifically, the computation time for the largest instance with more than 600,000 variables was reduced from more than 6 days to 8.2 h, a speedup by a factor of 17.89." [S036 p. 17]. Replace the research-page figure by this one, or keep it labelled as research-page only and not found in the full texts read.
- **Version note**: the dissertation's relative-residual baseline solves 50–86 % [S096 p. 52]; the 2008 paper's figure 45–86 % is confirmed for that version [S006 p. 17]. Keep the skill's figure and cite S006.

### M2 · Steer, don't switch

- **Strongest practice**: the update rules are the whole contribution in the flexible penalty paper [S032 pp. 9–11] and the dissertation chapter behind it [S096 pp. 85–89]; steering plus a penalty update tied to the squared KKT error for the fast infeasible rate [S009 pp. 2, 13–14]; in-iteration (ρ, μ) updates with final ρ tabulated [S033 pp. 1, 13–17, 24]; SQuID proves step 4, fast local convergence to infeasible stationary points [S022 pp. 2, 7, 25–27]; steering carried into augmented Lagrangians, inside the trust-region iteration, with Lancelot's iteration log showing that penalty-only iterations dominate [S019 pp. 5, 9–10, 35–38, 40; S040 pp. 2, 4–9, 12, 14, 19]; the update moved inside the QP solve [S057 pp. 9, 14, 23]; the stochastic line keeps an adaptive merit parameter and organizes its analysis around it [S007 pp. 6, 20, 24–26; S021 pp. 5, 7, 10, 19, 22–25; S030 pp. 7–8, 23; S013 pp. 3, 6, 11, 29]; a 2025 constrained proximal-gradient method steers τ from predicted linearized-infeasibility decrease [S082 pp. 2, 4–6, 11–14].
- **Stated in full texts**: the blocking effect as the weakness steering answers: "Thus, our view is that the main weakness of penalty-based strategies is the blocking effect illustrated in Fig. 3" [S032 p. 4; first in S096 p. 78]; the in-solve update set against earlier practice: "This strategy represents a stark contrast to previously proposed techniques that only update the penalty parameter after a sequence of iterations, in hindsight at the end of an iteration [1, 9, 10], or at the expense of numerous subproblem solves within a single iteration [3, 5, 7]." [S057 p. 2]; "While key to the practical performance of the algorithm, the adaptivity of the merit parameter introduced a number of theoretical challenges to overcome." [S013 p. 29].
- **Say–do update**: ✅ stays for 2007–2025. Two qualifications from the full texts: (i) when the progress test cannot be computed (stochastic interior-point methods), steering gives way to prescribed barrier schedules: "This is significant since stationarity measures cannot be computed accurately in the stochastic setting that we consider." [S044 p. 3; D002 pp. 3, 6; S063 pp. 6–9]; (ii) in 2026 an ML paper uses a fixed-timetable penalty [S089 p. 6], and two algorithm papers fix the merit or penalty parameter by constants from the analysis [S068 pp. 5, 10–11; S087 pp. 9, 25] (§3 rows 6–7; Tension 3).

### M3 · Break it on purpose

- **Strongest practice**: rank-deficient and infeasible variants of every equality test problem by adding c₁ − c₁² = 0 or = 1, already in 2009 [S025 pp. 22–23]; infeasible variants of application models plus toy problems [S009 pp. 14–16]; PIPAL's degenerate (−cᵢ² ≤ 0) and infeasible (cᵢ² ≤ −1) HS variants with presolve off and the narrowness admitted [S033 pp. 22, 25–26]; the infeasible HS copy made by adding x₁ ≤ 0 and x₁ ≥ 1, already in 2014 [S022 p. 30] and again in 2020 [S057 p. 28]; degenerate instances made by duplicating the last constraint in CUTEst and in logistic-regression constraints [S021 pp. 27–28]; minimal hand-built counterexamples for active-set methods [S024 pp. 11–17; S067 p. 7]; intentionally degenerate QPs reported separately [S064 pp. 18–19].
- **Dates and limitation (corrections)**: the skill dates the constructed variants to 2010, 2012 and 2020 and attributes the x₁-bounds construction to arXiv:1803.09224. The full texts show 2009 [S025 pp. 22–23] and 2014 [S022 p. 30]. The limitation *one kind of degeneracy (no MPCC-type or redundant-equality variants)* is contradicted for redundant equalities: duplicated constraints are a redundant-equality variant [S021 pp. 27–28]. MPCC-type variants remain absent.
- **Say–do update**: ✅ stays; practice spans 2009–2024. After 2015 the deliberately broken object is more often a small counterexample in the theory than a test set [S015 pp. 4–5; S005 pp. 12, 14–15; S018 pp. 9, 28] (variant, §3 row 4).

### M4 · Audit the yardstick

- **Strongest practice**: relative minimization profiles built because profiles hide the objective–feasibility–budget trade-off, with "evaluators should aim not to define success but present as much relevant benchmark data as possible in a concise and intuitive manner" [S004 p. 18] and β-panels at the rivals' budgets [S004 pp. 19–22, 25–26]; termination flags distrusted because they would favour the authors' code, with an algorithm-independent ε-stationarity estimate [S008 pp. 24–27]; regional complexity [S062 pp. 3–4, 18–22]; an own complexity device priced in runs [S020 pp. 4, 21–22]; rates converted into total work before methods are ranked [S001 pp. 34–37, 43–44, 49]; a fairness surrogate audited against the true measure [S083 pp. 2, 6–7, 10–12]; stationarity reported on noiseless values with the solver's own termination off [S059 pp. 33–35]; quality judged against known optimal values, not flags [S088 pp. 17–20].
- **Stated in full texts** (new): "Such questions are not answered well by contemporary worst-case results, which are too conservative." and "RC analysis can be used to guide the design of new algorithms." [S062 p. 4]; "Based on such evidence, we do not claim that the convergence results proved in this paper fully capture the practical behavior of LMSD methods." [S046 p. 3]; a 2018 verdict on his own better-complexity variant: "This would likely lead to very poor behavior in practice compared to the strategies in Sections 2.3 and 2.4, which are much less conservative." [S035 p. 9].
- **Correction of source**: Method 4 step 4 quotes "if we only considered a termination flag of type (1) …" from the Que thesis 2016. The same sentence is in the 2015 journal paper: "if we only considered a termination flag of type (1) to be the indicator for a successful run, then the profiles would be skewed in favor of the codes that yielded such a flag most often" [S008 p. 25]. Cite S008 as the primary source; likewise Heuristic 6's CPU-time sentence is in [S008 p. 24].
- **Say–do update**: ✅ stays, with the audit now visible inside papers from 2015 [S008 pp. 24–27] and 2018 [S035 pp. 8–9; S046 p. 3], not only in talks. ⚠ The 2017–2018 complexity papers adopt the yardstick unaudited [S002 pp. 2–3; S026 pp. 1, 26–28] (§3 row 8, Tension 1).

### M5 · Fair-fight benchmarking

- **Strongest practice**: rivals as one-switch variants of one code from the start [S047 pp. 6–8; S096 pp. 51, 72–73, 95; S006 pp. 16–17; S017 pp. 22–24]; the incumbent as a parameter setting [S012 pp. 5, 18–19]; Ipopt's engineering imported to make the comparison fairer [S033 pp. 12, 17, 20–21]; Lancelot's options aligned and an in-house baseline calibrated against it before any claim, "All together, we believe that these experiments are the best way to isolate and measure the performance of our adaptive penalty parameter updating procedure." [S019 pp. 34–39]; the production code changed only in steering, "In this manner, we were also able to isolate the effect that steering had on numerical performance" [S040 p. 10]; equal tuning effort stated and done [S015 pp. 18–19, 22; S041 pp. 5, 21–24]; a baseline given 110× the iterations [S007 p. 27] and later 440× [S021 pp. 25–30]; LMBM time-matched over 10 runs with its wins printed [S065 pp. 17, 20–21]; strategies as interchangeable objects [S088 pp. 7–9, 12, 26].
- **Stated in full texts**: "We took care to make sure that the tuning procedure for TRish did not require more effort than the tuning used for the SG method that we have for comparison purposes." [S015 p. 18]; "To ensure that all algorithms were tuned with the same amount of effort, we fixed the total number of hyperparameter settings to be the same for all algorithms." [S041 p. 22]; "Tuning these parameters means that problems cannot be solved once; they need to be solved numerous times" [D001 p. 2]; the incumbent's strength conceded: "Our experiments support the claim that when an interior-point method is performing at its best, it is difficult to outperform such an approach in terms of efficiency." [S033 p. 28].
- **Say–do update** (changes the skill's *improving after about 2018*): the full texts show the split by **paper type**, not by period. Equal-budget tuning is a habit of the stochastic and ML comparisons from 2016 on [S028 p. 6; S015 p. 18; S041 p. 22; S083 pp. 27–30; S090 p. 23]. In deterministic algorithm papers, parameters chosen on the evaluation runs without a reported tuning effort recur from 2007 to 2026 [S096 pp. 56–58; S003 p. 18; S033 p. 21; S012 p. 18; S008 pp. 20–21; S024 p. 20; S064 p. 17; H001 p. 17; S070 p. 11; S044 pp. 24–25; S088 pp. 14, 22]. No paper counts tuning time. Theory-led papers often run no external rival, usually with a stated reason [S039 p. 44; D002 p. 24; S063 p. 30; S088 p. 14]. Keep ✅ for steps 1–4 and 7; keep ⚠ for steps 5–6, now dated 2007–2026.

### Heuristics, taste marks and signature works with new full-text evidence

| Item | New evidence | Update |
|---|---|---|
| H1 log the event; computable safeguards | event frequency logged [S007 p. 27; S021 pp. 27, 29]; "This provides evidence for our claim that the merit parameter not reaching a sufficiently small value is not an issue of practical concern." [S021 p. 27]; frozen parameters checked in runs [S054 pp. 7, 21]; safeguard activity tabulated [S024 pp. 21–23]; branch percentages per test [S017 pp. 21–22]; analysis assumptions recast as run-time tests [S046 pp. 5–6, 8; S028 p. 5; S001 p. 45]; unverifiable assumptions rejected [S092 p. 11] | ✅; add the theory–code-gap clause (§5) |
| H2 count a safeguard's solves | the ladder confirmed [S009 p. 14; S022 p. 3; S057 pp. 2, 30]; earlier rungs: pricing a safeguard by a hybrid run [S096 pp. 52–53; S006 p. 18]; one factorization for all (ρ, μ) candidates [S033 p. 18]; costed in inner products [S047 p. 6]; "A drawback of the algorithm described in this paper is that it requires the inexact solution of the normal subproblem (2.2) in addition to the primal-dual system (2.6)." [S025 p. 25] | ✅, 2007–2020 |
| H3 failure users hit | MINLP branch-and-bound [S009 p. 1]; chance constraints in applications [S027 pp. 2–3]; AC-OPF intractable at industrial scale [S061 p. 2] | ✅ |
| H4 desiderata first | no card-level evidence | unchanged (slides only) |
| H5 fast variant first, guarantees later | confirmed [S003 p. 18; S008 pp. 2, 21; S049 p. 12]; order reversed in [S051 pp. 20, 22, 25]; guarantees given to someone else's fast scheme [S016 pp. 2, 8] | fold into Method 6 (§4) |
| H6 metric that exposes the mechanism | [S008 p. 24; S047 p. 6; S032 p. 17; S012 pp. 19–20; S096 p. 57; S065 p. 19] | ✅; primary source S008 |
| H7 filters by rule | rule-based pre-run filters with counts (1315 → 396 → 327) [D002 p. 25; S063 pp. 30–31]; PIPAL counts confirmed [S033 pp. 22, 25–26]; outcome-based filters also recur: problems where the method met a near-singular Jacobian [S017 p. 20], where the exact variant or the QP solver failed [S096 p. 50; S029 p. 29], where "the LICQ was satisfied at all iterates encountered in each run of our algorithm." [S037 p. 23], where f stayed above −10²⁰ in all runs [S030 p. 24] | ⚠; replace *later dropped* by *rule-based pre-run filters in 2024–2026 IPM papers; run-outcome filters recur through 2024* |
| H8 one run at iteration level | toy iteration tables [S009 pp. 15–18]; CATENA logs for Lancelot and AAL-TR [S019 pp. 35–38]; per-problem QO counts and last-ten-iteration residual plots [S022 pp. 31–32] | ✅ |
| H9 derivative checker, regression checks | no card-level evidence (code history only) | unchanged |
| H10 keep the skeleton, deterministic twin, rungs | 22 cards (21 works): rung order laid out in the dissertation [S096 pp. 33, 46, 59, 99] and stated in 2010 [S010 p. 2]; exact twin first [S029 pp. 3, 8; S020 pp. 4, 13; S013 pp. 5–6; S021 pp. 3, 10; D002 p. 9; S063 pp. 11, 20; S044 pp. 3, 10–15, 25]; noise rungs [S059 p. 3; S093 pp. 5–19]; deterministic-to-stochastic in the survey [S001 pp. 56–57] | ✅, the most-confirmed heuristic |
| Taste 2 keep classical guarantees | "Therefore, we contend that it is of interest to explore trust-region methods that do not deviate too much from traditional schemes, yet offer optimal worst-case complexity properties." [S043 p. 4]; TRACE keeps trust-region guarantees [S002 p. 30] | ✅ |
| Taste 3 one algorithm, not two phases | deliberate exceptions in §3 row 9 | ⚠ qualify |
| Taste 5 workhorse as target | SG placed at the origin of the method map [S001 pp. 20–21, 40]; SGD's parameter sensitivity [S011 p. 11] | ✅ |
| Signature works | confirmed: SW1 Table 5.2 [S006 p. 17]; infeasibility toys [S009 pp. 14–18]; PIPAL [S033 pp. 22–28]; p = 0 ablation [S003 pp. 19–20]; "the fact remains that SQP-GS actually took 26.6 times longer to run to obtain these better results" [S004 p. 26]; TRACE has no numerical section [S002 p. 4]; event 99.10–99.92 % and the 110× baseline [S007 p. 27] | page references can replace DOI-only citations |

---

## 3. Variants and contradictions

| # | Skill item | Full-text finding | Handling |
|---|---|---|---|
| 1 | M1 step 6 (minutes per iteration) | not in the cited paper [S010 p. 25]; full-text scale figure is [S036 p. 17] | correct (see §2 M1) |
| 2 | M1 outer need = merit model | the outer need is also a complexity inequality [S020 pp. 10–11, 16–17; S043 pp. 6–7; S053 pp. 6, 8; H001 pp. 4, 16], a step-size schedule [S037 p. 7; S056 p. 15], a sample-size schedule [S092 pp. 20, 24–26], a surrogate's accuracy δ = c·Δ² [S075 pp. 4, 10–11], or the information content the outer Newton step needs (sensitivities) [S077 pp. 3, 6; S071 TR pp. 5, 15] | variant note: *derive the inner accuracy from whatever the outer proof or globalization consumes* |
| 3 | M1 (contradiction S094) | in the competition team's SCOPF code, "The team also explored the application of various inexact solution methods but did not find that they provided a substantial enough speed improvement to make up for the decrease in accuracy." [S094 p. 5] | context-bound (team report, unspecified methods, hard time limit); record as a limitation, not a reversal |
| 4 | M3 constructions | 2009 and 2014 constructions; redundant-equality variant [S025 pp. 22–23; S022 p. 30; S021 pp. 27–28]; two further construction types: planted-answer generators [S066 pp. 18–19; S065 p. 18; S082 p. 28; S088 pp. 15–17] and minimal theory counterexamples [S024 pp. 11–17; S067 p. 7; S015 pp. 4–5; S018 pp. 9, 28]; and breaking the rival on paper before running it (§6, *predict the rival's failure*) | evidence + variant notes; correct the limitation |
| 5 | M2 scope | 15 cards apply an update rule on observed progress to non-penalty objects (§2) | moved to the promoted Method 6 (§4); M2 keeps the objective–feasibility trade-off |
| 6 | M2 when progress is uncomputable | prescribed schedules replace steering in stochastic IPMs [S044 p. 3; D002 pp. 3, 6, 24–25; S063 pp. 6–9]; merit parameter frozen for analysis and checked constant in runs [S054 pp. 7, 21] | variant note |
| 7 | M2 (contradiction S089) and Tension 3 | fairness constraints handled by a penalty raised ×10 every 400 iterations [S089 p. 6]; penalty weight as a user knob swept on a grid [S069 pp. 8–10]; at the same time "Another key feature of this methodology is that one does not solve the hard-constrained training problem with a penalty-based (e.g., augmented Lagrangian) method." [S068 p. 19], and S087 builds on Fletcher's augmented Lagrangian with a fixed penalty: "In this case, the algorithm reduces to a gradient descent algorithm applied to minimize Fletcher’s augmented Lagrangian." [S087 pp. 2, 9, 25] | Tension 3 update (§5 item c) |
| 8 | M4 and Tension 1 | the complexity-for-practice premise is adopted in 2017–2018: "This is due to the fact that, at least for convex optimization, algorithms designed with complexity bounds in mind have led to methods with improved practical performance." [S026 p. 1; S002 pp. 2–3]; in the same year the audit appears in print [S035 p. 9; S046 p. 3]; later the papers price their own devices [S020 p. 22] or argue the reverse ordering, "However, as is typical with well-designed second-derivative methods, although the complexity bound is worse, it typically performs better (see Section 5)." [S053 p. 17]; a 2026 worst-case gain is produced while worst-case parameter rules are disowned for practice [S087 pp. 22, 24]. S066's success test is its own residual [S066 pp. 19–20, 36] | Tension 1 gains a within-paper form (2017–2018 both sides) |
| 9 | Taste 3 (one algorithm beats two phases) | deliberate switches or phases: two-phase trust funnel kept for complexity [S026 pp. 1–2, 25]; a switch to a traditional AL near solutions proposed to inherit its theory [S019 pp. 33, 43]; the step computation switches on a steplength trigger [S036 pp. 9–10]; a separate Phase I for a strictly feasible start [S063 pp. 3, 5, 30–31]; a design the paper itself calls two-phase, whose phases both run every iteration [S022 p. 1] | qualify Taste 3: the preference concerns the objective–feasibility trade-off; switching a computational module on a monitored trigger is accepted and is Method 6 |
| 10 | M5 contradictions, theory-first papers | no comparison [S039 p. 44]; no external rival with the reason given [S091 pp. 4, 16–22; S088 p. 14] | say–do update (§2 M5) |
| 11 | M5 contradictions, application and collaboration papers | no rival controller run [S048 pp. 6, 11]; external baselines delegated to other papers and no repeated runs [S056 pp. 16–20]; one dataset, two clients, penalty value chosen on test results [S069 pp. 5, 9–12] | say–do update; application or cross-community collaborations with new co-authors, so they weigh less on the solver methods |
| 12 | M5 contradictions, algorithm papers | the main rival's numbers taken from its paper instead of a rerun [S057 pp. 27–29]; outcome-filtered test set and 5 runs [S037 pp. 23–25]; parameters chosen on testing-set results, run count not stated [S076 pp. 15–18]; looser tolerances for the new method, cross-language timing, single runs, a solver-success filter without the pre-filter count [S082 pp. 27–29] | say–do update (§2 M5 and the H7 row) |
| 13 | H5 ordering | exact scheme first, practical heuristic second [S051 pp. 20, 22, 25] | variant; H5 folds into Method 6 |
| 14 | Tension 5 (guarantees vs speed) | Method 6 is the mechanism by which the papers resolve it: speed by default, guarantee dormant, its price measured (§4) | cross-reference |

---

## 4. Promotions

The skill has five core methods, so one promotion fits under the 3–7 cap without replacing a method. One cluster passes all four checks and is not covered by an existing method.

### Promote → Method 6: Guard the incumbent; let the guarantee sleep

> **Review outcome (2026-10-10, T3.6 fix):** not promoted. Exclusivity fails at team level: Wright Method 4 (minimal safeguard with a no-safeguard twin), Fletcher Method 1 (minimal-interference safeguarding), Toint Method 3 (least obstructive acceptance, measured against free Newton) and Wächter Method 2 (ablate your own safeguards against an unguarded Newton run) share the move. SKILL.md keeps Heuristic 5 in its base-tier slot and meaning and adds this construction as its full-text form, parts (i)–(iv) = steps 2–5 below; §5 (a) *port the property* is Heuristic 11. Evidence and four-way table: `09-evidence-ledger.md#method-6`. The proposal below is kept as written.

**Cluster** (merged from the round-1 candidates *reduce-to-predecessor / reduce-to-incumbent design*, *minimal-intervention / dormant safeguard*, *cheap default with guaranteed fallback*, *contain the incumbent's choice*, *incumbent as a parameter setting*, *nest the classical method*, *price the guarantee* and *safeguard-as-arm*; merged by reading, since every card describes the same construction from one of two sides). **21 distinct full cards, 2007–2026, no pairs among them**: S047, S096, S010, S017, S003, S033, S036, S012, S024, S067, S008, S028, S042, S027, S040, H001, S051, S020, S014, S087, S029 (the last as a stated partial case).

| Check | Result | Evidence |
|---|---|---|
| 1 Cross-project recurrence | ✅ (seven lines: IPM step lengths, inexact SQP/IPM, penalty-IPM, nonsmooth BFGS/GS, active-set QP and isotonic regression, stochastic quasi-Newton, trust-region complexity) | search set containing the incumbent's choice [S047 pp. 4–5]; reduces to the predecessor in convex regions [S017 p. 2] or in a rescaled space [S010 pp. 5, 11–12]; p = 0 gives Sℓ1QP and m = 0 gradient sampling [S003 p. 9]; GS a parameter setting of AGS [S012 p. 5]; M = N recovers Sℓ1QP [S027 p. 11]; the m = 1 rule recovered [S042 pp. 2, 13]; ARC and TRACE as instances [H001 pp. 14–16]; exact BFGS reproduced before relaxation [S051 p. 20]; SG recovered at β = 0 [S014 p. 22]; the eigenstep test never fires so the method reduces to gradient descent [S087 pp. 13–14]; dormant guards: sampling and bounded L-BFGS only when tests fail [S008 pp. 2, 11, 13]; an only-growing safeguard set U [S024 pp. 3, 13–14, 18, 21–23]; a fraction p of violators [S067 pp. 7–8]; the smallest damping β_k [S028 pp. 3–4]; fallback to the conservative direction [S033 pp. 18–19]; the regularized step only when the steplength collapses [S036 pp. 9–10]; typed CG exits wake the eigenvalue oracle [S020 pp. 10–15]; accept before repairing [S096 pp. 62–63] |
| 2 Say–do consistency | ✅ (stated in the papers as the design intent; practised in the algorithm boxes and experiments) | "A feature critical to the practical performance of our algorithm is that, when it is applied to solve many problem instances, the algorithm reduces to an unadulterated BFGS strategy for the majority of the iterations." [S008 p. 2]; "The resulting algorithm fully integrates the procedures of step computation and step selection and automatically reduces to an inexact SQP method in convex regions of the search space." [S017 p. 2]; "We stress, however, that while the proof relies on such worst-case behavior, we have never witnessed such an occurrence in practice." [S024 p. 14]; "This shows that our proposed safeguard, which allows more aggressive updates, can be more effective than a conservative safeguard." [S067 p. 10]; on the price: "Across the board, our results indicate that safeguarding was not necessary and would typically degrade performance when compared to the unrestricted steering approach." [S040 p. 20]; "The variants with no regularization term in the subproblems outperform the others in this respect; recall that these variants do not possess optimal complexity guarantees." [S020 p. 22] |
| 3 Executable, different from standard practice | ✅ | Steps below. The alternatives the papers set themselves against are the two standard moves: an always-on safeguard (equal step lengths [S047 p. 2]; always-regularized steps [S036 p. 12]; sampling every iteration [S008 pp. 2–3]; a conservative one-index fallback [S067 p. 8]; fixed regularization of BFGS [S028 p. 2]) or a switch from the fast method to a guaranteed one after it stalls (HANSO's BFGS-then-GS [S008 p. 21]). Here the guarantee is attached to the incumbent, triggered by the quantity the proof needs, and priced by running the guarantee-free twin [S036 p. 12; S012 pp. 18, 20–21; S040 pp. 13–14, 19–20; S020 pp. 21–22]. |
| 4 Exclusivity | ✅ with the boundary stated | Safeguarding is common; the Curtis-specific combination is (a) the reduction to the incumbent written into the design and used as a proof device (inherit theory by citation [S010 pp. 11–12; S017 p. 18; S042 p. 16; S051 p. 20]), (b) the trigger set to the quantity the proof needs [S036 pp. 9–10; S008 pp. 13–14], (c) the guard's activity tabulated [S024 pp. 21–23; S017 pp. 21–22], and (d) the guarantee priced by its own arm [S036 p. 12; S040 pp. 19–20]. The other nine team members are base tier (no paper cards), so the contrast with their seats cannot be checked in full texts; the skill's Roundtable Card already sets Curtis against restoration-phase designs (Wächter, Fletcher), which are switches in this method's terms. Exclusivity against the wider field is not established beyond the contrasts the papers themselves draw. |

**Draft for SKILL.md** (for the SKILL.md editor; not applied here):

- **One line**: Make the new method coincide with the fast incumbent (or the heuristic practitioners already run) whenever a computable test passes; wake the guarantee-carrying machinery only when the test the proof needs fails; then count how often it woke and run the guarantee-free twin to price it.
- **Evidence**: Stated (in papers) [S008 p. 2; S017 p. 2; S024 p. 14; S067 p. 10]. Practice: 21 works 2007–2026 (§4 table). Price measured: 84 % against 89 % of CUTE solved by the always-guaranteed variant against the switching implementation [S036 p. 12]; guarantee-free Hessian variants no better [S012 pp. 18, 20–21]; safeguarded steering worse [S040 p. 20]; regularization-free variants better in Hessian-vector products [S020 p. 22]. Say–do: ✅ stated + practised.
- **Steps**:
  1. Name the incumbent users already trust and the one property it lacks (a guarantee, robustness under negative curvature or nonsmoothness) [S008 p. 2; S042 pp. 2, 5; S024 pp. 3, 27–29].
  2. Design so that an idle test or one parameter value gives back the incumbent exactly, and say which [S003 p. 9; S012 p. 5; S027 p. 11; S017 p. 2]; or search over a set that contains the incumbent's choice, so that doing no worse than the incumbent holds by inclusion [S047 pp. 4–5]. Where possible, inherit the incumbent's theory through the reduction instead of re-proving it [S010 pp. 11–12; S017 p. 18; S051 p. 20].
  3. Trigger the guard on the quantity the proof needs and make the intervention the smallest that restores it: a steplength floor [S036 pp. 9–10], a curvature test [S008 pp. 11, 13], the smallest damping weight [S028 pp. 3–4], a fraction of the violators [S067 pp. 7–8], a set that only grows [S024 pp. 13–14], a typed inner-solver exit [S020 pp. 10–15]; test the current step before repairing anything [S096 pp. 62–63].
  4. Tabulate how often the guard fired and how far it grew (→ H1) [S024 pp. 21–23; S017 pp. 21–22; S020 p. 20].
  5. Run the guarantee-free twin in the same code and report the price of the guarantee (→ Method 5 step 3, ablating the guarantee rather than the novelty) [S036 p. 12; S040 pp. 13–14, 19–20; S020 pp. 21–22].
  6. Say where the reduction is partial or the code leaves the analysed range [S029 p. 8; S008 p. 20].
- **Applies to stage**: algorithm design; giving guarantees to a heuristic users already run; scaling a guaranteed method without losing the incumbent's speed.
- **Different from standard practice**: neither an always-on safeguard nor a phase switch after failure; the guarantee is attached to the incumbent and paid for only when the proof's quantity degrades.
- **Limitations**: the code often runs the guard outside the analysed parameter range [S008 p. 20]; the reduction can be partial [S029 p. 8]; trigger parameters are set on the test set without a reported tuning effort [S024 p. 20; S064 p. 17]; worst-case trigger behaviour is argued rare rather than measured in some papers [S024 p. 14]; evidence is mostly small problems in Matlab prototypes.
- **Why not merged into an existing item**:
  - *Method 2* is about the parameter that trades objective against feasibility; its one line cannot hold Hessian damping, sampling, step-size rules or active-set safeguards, which is why the readers filed 15 such cards as Method 2 variants without a penalty or merit parameter (§2). Where both apply (PIPAL-a and PIPAL-c [S033 pp. 18–19]; the flexible penalty with a switching step computation [S036 pp. 9–11]), Method 2 designs the parameter rule and Method 6 the fallback.
  - *Heuristic 10* applies when the information model changes; Method 6 applies with unchanged information (the 2007–2016 cases above).
  - *Heuristic 5* (keep the guarantee-free comparator, restore guarantees later) is one instance, SQP-GS → BFGS-SQP → the guaranteed hybrid [S003 p. 18; S008 pp. 2, 21]; fold it into Method 6 step 5.
  - *Heuristic 2* (count the safeguard's extra solves) stays as the cost ladder; Method 6 step 4 reports the guard's activity, H2 its per-iteration cost.
  - *Taste 3* gains its operational form outside the penalty family.
- **Taste quick-check line** (draft): *When the guard is idle, is the method exactly the incumbent, and did you count how often the guard woke and what the guarantee cost?*
- **Roundtable Card** (draft, for T3.8): add *dormant guards on a trusted incumbent* to *Default recommendation*.

With Method 6 the skill has six core methods; one slot remains before the cap.

**Runners-up (not promoted)**:
- *Port the property, not the formula* (7 works, §5 item a). Passes recurrence, say–do and executability; exclusivity is only partial and it overlaps Heuristic 10 and the TRACE anatomy. Kept as a heuristic.
- *Disclose the theory–code gap* (10 works, §5 item b). Passes recurrence, say–do and executability; fails exclusivity (common good practice). Folded into Heuristic 1.
- *Θ_k normal–tangential proof skeleton* (S096, S006, S032, S025, S017, S007, S054). A proof device reused across 2007–2025, not a research method: it tells how to write a proof, not how to choose or judge research. Kept in the technique inventory (§7.1).

---

## 5. New heuristics

Clusters that are executable and pass at least one more check. The skill has 10 heuristics; the framework asks for 5–10. Recommended arithmetic: H5 folds into Method 6 (§4); item (a) takes its slot; items (b) and (c) are folded into existing items. Result: 10 heuristics.

**(a) Port the property, not the formula** (recommend as a numbered heuristic). *If* you carry a method's guarantee or behaviour into a new setting or a rival framework, *then* name the inequality its proof or success rests on and redesign only the host's acceptance or update rules so every accepted step satisfies an analogue; leave the host skeleton as practitioners know it.
- Evidence (7 works, 2016–2024): self-correction, not the secant equation, as what makes BFGS work, "However, too much emphasis has been placed on this equation." [S028 pp. 2–4], reused for nonsmooth problems [S049 pp. 6, 8]; ARC's accepted-step inequalities listed and the trust-region rules redesigned until each accepted step satisfies an analogue [S002 pp. 5–7]; TRACE's acceptance tests grafted into a trust funnel, proved lemma by lemma [S026 pp. 6, 13–19, 30–35]; step conditions that make ARC and TRACE special cases [H001 pp. 2, 4, 14–16]; minimal changes to trust-region Newton-CG for optimal complexity [S020 pp. 2, 4]; only the curvature pair repaired through problem structure [S076 pp. 7, 10–13]; stated aim: "Therefore, we contend that it is of interest to explore trust-region methods that do not deviate too much from traditional schemes, yet offer optimal worst-case complexity properties." [S043 p. 4].
- Checks: recurrence ✅; say–do ✅ [S028 p. 2; S043 p. 4]; executable and different ✅ (the documented alternatives transplant the formula: a new cubic model [S002 pp. 5–6], fixed BFGS regularization [S028 p. 2]); exclusivity ⚠ partial.
- Placement: after Heuristic 10, with a cross-reference to the TRACE anatomy (its key insight) and Taste 2.

**(b) Disclose and cap the theory–code gap** (fold into Heuristic 1 as a second clause). *If* the code departs from the analysed algorithm, *then* list each departure in the implementation section with its reason, and where possible cap the departure (a finite number of adjustments) so the theory still covers it, or check in the runs that it stayed inactive.
- Evidence (10 works, 2014–2026): infeasibility exits that also require a small penalty parameter, stated as departures [S029 pp. 28–29; S019 p. 35]; a curvature threshold outside the proved range and an unchecked set membership, stated [S008 p. 20]; an auxiliary sequence kept in code but dropped in the analysis [S043 pp. 9, 22]; "Although this choice is not covered by the convergence theory, one could cap the number of adjustments made to ζ, in which case it is covered by the theory." [S070 p. 12]; "Although this PG parameter update strategy worked better than the basic strategy in Algorithm 1 (see Line 19 and Line 21), it is not covered by our analysis in Section 4." [S053 p. 22]; "We found this update strategy to work better in our testing, all of the analysis of Section 5.2.3 still holds, and the analysis of Section 5.2.2 still holds if this modified update is only allowed a finite (possibly large) number of times." [S082 p. 27]; production settings listed against the analysed variant [S091 p. 17]; parameters frozen for analysis and verified constant in runs [S054 pp. 7, 21]; a runtime check restoring a theoretical condition [S040 pp. 11–12].
- Checks: recurrence ✅; say–do ✅; executable ✅ (the cap is the non-generic step); exclusivity ✗. Hence a clause, not a new item.

**(c) Constrain, don't weight** (fold into Inner Tension 3 and its routing; heuristic-grade). *If* a requirement is a bound (fairness level, structure of the solution), *then* impose it as a constraint with an explicit level swept, not as a penalty weight tuned by hand.
- Evidence (4 full works, 2025–2026, plus two abstract-level): "conventional techniques such as penalty-based methods [17] may fail to preserve the structure of the solution (see [16, Section 5]), therefore limiting their effectiveness in this setting." [S082 p. 2]; hard fairness constraints because the weight is costly and "First, the unfairness measure does not always improve monotonically with decreasing λ." [S083 pp. 2–3, 11–12]; the weighting method rejected for ε-constraint Pareto search [S073 pp. 10–11]; the momentum methodology avoids penalty and augmented-Lagrangian solves [S068 p. 19]; abstract-level [S055 abstract; S084 metadata].
- What it changes in Tension 3: the skill's inferred reading (that the turn may target only fixed-weight reformulations) is now card-supported: penalties are avoided as a *problem reformulation* [S082 p. 2; S083 pp. 2–3] while a merit parameter stays inside step acceptance [S082 p. 6; S083 p. 24]. Counter-instances stay in the tension: a fixed-timetable penalty [S089 p. 6], a penalty knob swept on a grid [S069 pp. 8–10], a method on Fletcher's augmented Lagrangian [S087 p. 2]. The penalty doubt itself is older than 2024: the blocking-effect critique dates from 2007–2008 [S096 p. 78; S032 p. 4].
- Checks: recurrence ✅ (2025–2026 only); say–do ✅ (2024–2026 slides already quoted in Tension 3, plus the papers); executable ✅; exclusivity ✗ (constrained learning and ε-constraint methods are widespread). Not a numbered heuristic: the list is full and the item explains a tension better than it guides solver design.

---

## 6. Candidate pool (not promoted)

Counts are distinct full cards (pairs merged). "→" names where the evidence goes instead.

| Candidate | Cards | Why it stays here |
|---|---|---|
| Predict the rival's failure, then show it | 8: S047 pp. 4, 6; S049 pp. 12, 18; S042 pp. 5–6; S064 pp. 13–15; S070 pp. 4–5, 10; S034 pp. 47, 56–59; S044 pp. 22–23; S015 p. 3 | executable and recurrent, but common in good papers; → Method 3 variant (*break the rival on paper first*) and §7.4 |
| Bracket the assumption (a case where it holds, one where it fails or is needed, constants measured on a 2-D instance) | 5 works: D002 pp. 21–24 (= S063 pp. 25–29), S092 pp. 19–20, S093 pp. 19–22, S018 pp. 9–11, S044 pp. 3, 22–23 | heuristic-grade, overlaps Heuristic 1 and the list is full; → §7.4 |
| Unknown constant replaced by a monotone estimate raised only on stall, proved to settle | 6: S064 pp. 12–13; S002 pp. 8, 22; S021 pp. 7–8, 11–12; S063 pp. 30–31; S046 pp. 5–6, 8; S092 pp. 17, 22 (sweep instead) | → Heuristic 1 (computable safeguards) evidence and §7.2 |
| Prove the adaptive parameter freezes | 4: S032 pp. 14–15; S057 pp. 13–14; S007 pp. 12, 16; S021 pp. 11–12 | proof device; → Method 2 evidence and §7.1 |
| Iteration typing / scenario or event split with exhaustiveness lemma | 7: S029 pp. 6–7, 11–12, 17–18; S039 pp. 15–16, 24, 38–40; S021 pp. 14–25; S030 pp. 8, 16, 21–23; S038 pp. 9–12; S053 pp. 10–17; S020 p. 8 | proof device; → §7.1 |
| Inner tolerance tied to the outer step schedule | 2: S037 p. 7; S056 p. 15 | → Method 1 variant (§3 row 2) |
| Known-answer (planted) instances | 5: S066 pp. 18–19; S065 p. 18; S082 p. 28; S088 pp. 15–17; S048 p. 6 | → Method 3 variant (§3 row 4) |
| Match the incumbent's theorem, win in the experiments | 4: S015 pp. 3, 9–10, 23; S090 pp. 3, 7, 11; S007 pp. 4, 8–13; S030 p. 8 | writing/claim move; → Taste 2 and Method 4 evidence; §7.4 |
| Twin quantities computed with exact data (shadow parameter, noiseless twin, oracle beside estimator) | 5: S013 pp. 10, 14, 16, 20; S059 pp. 7, 14, 33; S054 p. 21; S037 p. 6; S093 pp. 5, 16–17 | → Heuristic 10 evidence (the twin also lives inside the proof) and §7.1 |
| Mechanism-activated subset (compare where the feature fired) | 3: S033 p. 24; S014 pp. 14–15; S042 p. 17 (filter by run outcome) | → Method 5 / Heuristic 6 evidence; the S042 form conflicts with Heuristic 7 |
| Competition as benchmark protocol | 2 works: S023 pp. 17–22; S061 pp. 2, 6–7 (S060 abstract pairs with S061) | → Method 5 variant (an externally fixed yardstick) |
| Limitations stated up front | 4: D002 p. 3; S059 p. 4; S090 p. 3; S073 p. 3 | writing move; → Workflow E and §7.4 |
| Speed-versus-accuracy or inexactness as a user dial | 2: S088 pp. 15, 19–20; S043 pp. 3, 23–24 | → Method 4 evidence (show the trade-off) |
| Exact until burdensome, then heuristics with gap to a bound; small-case enumeration before a conjecture | 2: S081 pp. 11–19; S058 pp. 4, 15 | pre-PhD combinatorics; no weight (§10) |
| Singletons (one card each): first-order step as active-set oracle [S053 pp. 5–6]; two separate multiplier estimates [S022 pp. 3, 7]; criticality-gated computation [S039 pp. 6, 8–9]; project before you average [S068 pp. 3, 5, 9]; sensitivity-returning decomposition [S077 pp. 3, 5–6]; certified rollback [S016 pp. 5–6, 9]; certified cheap bound as pre-screen [S061 p. 12]; emulated inner inexactness [S029 p. 29]; warm start as an evaluation axis [S067 pp. 9–12]; budget-sliced comparison [S004 pp. 19–22]; error-budget split [S011 p. 10]; every-iteration potential [D001 pp. 3–8]; regional analysis [S062 pp. 3, 15–21]; two-regime guarantees [S041 pp. 2–3, 19–21]; price-of-adaptivity term isolated [S013 pp. 6–7, 29]; analyse someone else's algorithm [S087 pp. 3, 13–14]; local rate as complexity lever [S087 pp. 3, 24–27]; public correction of a founding proof [S005 pp. 5, 12–16]; curvature by auxiliary function [S090 pp. 5–6]; amortized evaluations across instances [S075 pp. 5–6, 18–22] | 20 | one work each; kept for the technique inventory |

---

## 7. Technique inventory

### 7.1 Proof devices

- **Θ_k normal–tangential skeleton**: an analysis-only split d = u + v, a K₁/K₂ case split and one critical measure bounding step norm, merit decrease and steplength, then telescoping [S096 pp. 33–39; S006 pp. 9–11; S032 pp. 12–14; S025 pp. 12–14; S017 pp. 13–16]; the same family in the stochastic SQP line (Ψ_k with K_u, K_v) [S007 pp. 8–10] and for multipliers [S054 pp. 10–11]. The dissertation turns the analysis-only split into observable acceptance inequalities [S096 pp. 65–67].
- **Model reduction as a computable surrogate for the merit function's directional derivative** [S096 pp. 31–32; S006 pp. 7–8; S022 pp. 9–10; S029 p. 18; S036 p. 6; S003 pp. 10–11].
- **Shifted (scaled) merit function monotone across parameter changes**: (f − f_min)/π + ‖c‖ when π grows [S025 p. 14; S010 p. 14]; ρ(f − f_low) + v when ρ falls [S022 p. 14; S029 p. 21; S057 p. 17; S082 pp. 13–15]; shifted barriers monotone in μ [D002 p. 8; S044 pp. 7–8; S063 pp. 9–10]; Dirichlet's test for μ-weighted sums [S019 pp. 18–21].
- **Outcome dichotomy or trichotomy theorems** (KKT; infeasible stationary point; Fritz John point where MFCQ fails), with test conditions designed backwards so that the third outcome certifies MFCQ failure [S025 p. 11; S010 pp. 18–19; S022 pp. 17–19; S029 pp. 10, 26–27; S019 p. 32; S057 pp. 18–23; S082 p. 14].
- **Fast local rate to an infeasible stationary point**: implicit-function path at distance O(ρ), Newton contraction uniform in ρ, then the parameter update tied to the squared error [S009 pp. 7–11, 13; S022 pp. 22–27].
- **Parameter eventually constant** (penalty, merit, ratio or unknown-constant estimates settle after finitely many changes, with run-uniform bounds) [S032 pp. 14–15; S057 pp. 13–14; S007 pp. 12, 16; S021 pp. 11–12; S030 pp. 12–16; S059 p. 27; S037 p. 14; S064 pp. 12–13; S002 p. 22].
- **Iteration typing with counting**: disjoint step types with their own updates, an exhaustiveness lemma, contradiction on the disjointness [S029 pp. 17–18; S039 pp. 15–16, 24, 38–40; S038 pp. 9–12; S053 pp. 10–17]; a generic sequence lemma for residuals contracted only on some types [S029 pp. 21–22].
- **Complexity counting template**: accepted steps × a bounded number of rejections between them; λ/‖s‖ grows geometrically under rejection until acceptance; ‖s_k‖ ≥ c‖g_{k+1}‖^{1/2} [S002 pp. 14–16, 21–26; H001 pp. 7, 10–13; S026 pp. 20–25; S043 pp. 12–16; S035 pp. 5–8; S020 pp. 6–8].
- **Event splits for a random merit parameter**: settles small / vanishes / settles too large, the bad cases shown to have probability zero by a tree of realizations and Chernoff bounds [S007 pp. 20, 24–26; S021 pp. 14–25, 31–40; S013 pp. 14–16, 33–36].
- **Gradient-sampling probability-zero argument**: Carathéodory gives an open set of good sample sets near any non-stationary limit; staying outside it forever has probability zero [S003 pp. 12–13; S012 pp. 15–17; S008 pp. 16–19; S065 pp. 12–15; S091 pp. 14–15]; the founding property re-proved and a counterexample under the weaker assumption [S005 pp. 13–15].
- **Self-correcting BFGS**: the potential tr(H) − ln det(H) and good bounds on at least ⌈pK⌉ of any K iterations [S028 pp. 3–4, 10–11; S049 pp. 9–11, 24–25; S065 p. 11].
- **Noise–step correlation by a sign split and the law of total expectation**, with a prescribed step-size bracket [S007 pp. 20–21; S037 pp. 18–19; S013 pp. 17–18; D002 pp. 18–19; S044 p. 18].
- **Exponent bookkeeping for prescribed schedules**: summable noise against unsummable decrease, Fatou for an almost-sure liminf [D002 pp. 12–14, 19–21; S044 pp. 14–17, 21].
- **Twin and shadow quantities with perturbation bounds** (true-gradient merit parameter, noiseless twin iterate, Stewart's pseudo-inverse and oblique-projector perturbation) [S013 pp. 16, 19; S059 pp. 14, 16–24; S092 pp. 11–13; S093 pp. 16–17; S087 p. 21].
- **Reduction to a known method to inherit its theory** (semismooth Newton, Dembo–Eisenstat–Steihaug inexact Newton, Zhang–Hager, the predecessor's theorem) [S024 pp. 27–29; S067 p. 4; S052 p. 13; S053 pp. 18–20; S042 p. 16; S017 pp. 17–18; S010 pp. 11–12]; a practical component sandwiched between multiples of the analysed one [S036 pp. 10–11].
- **Duality-gap certificates for inexact subproblem solves** [S057 p. 8; S065 pp. 9–10].
- **Minimal counterexamples** that justify a mechanism or an assumption [S024 pp. 11–17; S064 pp. 13–15; S018 pp. 9, 28; S015 pp. 4–5; S005 pp. 14–15].
- **Regional analysis and every-iteration potentials** [S062 pp. 8–11, 15–21; D001 pp. 3–8].

### 7.2 Algorithm-design moves

- Guard the incumbent (Method 6, §4).
- Port the property, not the formula (§5 a).
- Interpolate between rival mechanisms by making a parameter interval-valued (penalty and one-element filter as endpoints) and draw each mechanism's acceptance region in the (‖c‖, f) plane [S096 pp. 78–88; S032 pp. 2–10].
- One factorization for many parameter values, since (ρ, μ) enter only the right-hand side [S033 p. 18].
- Place the parameter update between two subproblem solves, or inside the QP solve [S022 p. 7; S057 pp. 5, 9].
- Two separate multiplier estimates, for optimality and for feasibility: "This last feature of our algorithm—that of having two separate multiplier estimates—is quite unique for an optimization algorithm." [S022 p. 3].
- Gate expensive computations by cheap criticality measures: "It is not necessarily prudent to compute a normal step in every iteration." [S039 p. 6]; a first-order step as active-set oracle [S053 pp. 5–6; S038 pp. 3–5].
- Typed inner-solver exits route the outer safeguard; an exceeded cap is a curvature certificate [S020 pp. 10–15].
- An unknown constant replaced by a monotone estimate raised only on stall [S064 pp. 12–13; S002 p. 8; S021 pp. 7–8].
- Prescribed schedules where tests cannot be computed [S044 pp. 3, 9, 16–17; D002 pp. 3, 6].
- Project before you average (momentum on null-space-projected gradients) [S068 pp. 3, 5, 9].
- Ask the inner solvers for what the outer Newton step needs (sensitivities) [S077 pp. 3, 6; S071 TR pp. 5, 15].
- Emulate inner inexactness by perturbing exact solutions until a test is just met [S029 p. 29].

### 7.3 Experiment and evaluation protocols

- One code, one switch: naive floor and idealized ceiling around the new method [S017 pp. 22–24]; incumbent as a parameter setting [S012 p. 5]; production code changed in one rule [S040 pp. 10, 17–18].
- Import the incumbent's engineering, listing each item with its source [S033 pp. 20–21]; calibrate the in-house incumbent against the mature code first [S019 pp. 34, 39].
- Three layers: full set, the subset where the mechanism fired, constructed variants [S033 pp. 22–27].
- Price a safeguard or guarantee with its own arm [S096 pp. 52–53; S006 p. 18; S036 p. 12; S040 pp. 13–14; S020 pp. 21–22].
- Work-matched and time-matched comparisons [S037 p. 22; S065 pp. 17, 20–21]; budget-sliced relative minimization profiles [S004 pp. 19–22].
- Algorithm-independent quality: fresh-sample ε-stationarity [S008 pp. 26–27]; true-gradient stationarity with least-squares multipliers [S007 p. 27; S037 p. 22]; noiseless measures with the solver's termination off [S059 pp. 33–35]; objective recomputed outside the solver [S061 p. 11].
- Show the theory's signature in the logs: last-ten-iteration residual slopes [S022 p. 31]; local signatures tabulated [S052 pp. 18–20]; proof quantities plotted [S046 pp. 15–19]; event frequencies [S007 p. 27]; theoretical rate overlaid [S070 pp. 13, 31–32].
- Show the inexactness was real: binned accepted residual ratios [S029 p. 30].
- Known-answer instances [S065 p. 18; S066 pp. 18–19; S082 p. 28; S088 pp. 15–17]; convex test problems chosen so that different local minimizers cannot skew the comparison: "(By employing convex, as opposed to nonconvex test problems, we can be sure that the results of our experiments are not skewed by two algorithms converging to different local minimizers and other related circumstances.)" [S065 p. 18].
- Equal tuning budgets [S015 pp. 18–19, 22; S041 p. 22]; a baseline given a stated iteration multiplier [S007 p. 27; S021 pp. 25–30].
- Externally fixed protocols: competition rules, unseen instances, fixed hardware, worst-case fallback score [S023 pp. 17–22; S061 pp. 2, 6–7].

### 7.4 Writing moves

- The exact algorithm presented as scaffold before the inexact one, each test followed by the lemma that needs it [S029 pp. 8–12].
- Novelty sentence in abstract, introduction and conclusion [S029 pp. 1, 31; S019 pp. 1, 42].
- Limitations up front: "Let us emphasize upfront that we do not expect our method to be competitive with state-of-the-art interior-point methods in the deterministic regime, and especially not with those that employ second-order derivatives of the objective." [D002 p. 3]; "We mention upfront that our proposed algorithm and analysis leave certain natural questions unanswered." [S059 p. 4]; "We highlight upfront that the convergence-rate guarantee for our proposed algorithm is not stronger than that of Adam; the point is that the algorithm has a comparable guarantee and can perform better in practice in various settings." [S090 p. 3].
- Claim calibration by explicit non-claims [S007 p. 26; S014 p. 21; S046 p. 3].
- An obstacle section for the obvious simpler method: "Upon seeing our algorithm, a reader may wonder if a simpler variant has convergence guarantees." [S044 pp. 3, 22–23].
- Bracket each nonstandard assumption with a case where it holds and one where it fails [D002 pp. 21–24; S018 pp. 9–11]; measure its constants on a 2-D instance [S092 pp. 19–20; S093 pp. 19–22].
- When theory is weaker than the incumbent's, list the fixes and why they were not made [S019 p. 33].
- Correct a founding proof in public, naming who found the gap: "This oversight went unnoticed for 12 years until J. Portegies and T. Mitchell brought it to our attention recently." [S005 p. 5].
- Disclose the theory–code gap (§5 b).
- Map a field around its workhorse [S001 pp. 20–21, 40]; avoid benchmark-driven verdicts in a survey [S001 p. 4].

---

## 8. Trajectory as seen in the full texts

### 8.1 Topics by period (cards; full reads in brackets)

| Period | Cards [full] | Main topics (cards) |
|---|---|---|
| 2003–2007 | 5 [4] | combinatorial matrix theory at William & Mary (S058, S081; S086 unreadable); IPM step lengths for QP with Nocedal (S047); dissertation on inexact SQP (S096) |
| 2008–2012 | 10 [9] | inexact and matrix-free SQP/IPM (S006, S025, S017, S010, S036); penalty updates and infeasibility (S032, S009, S033); nonsmooth SQP-GS (S003); proceedings editing (S079 abstract) |
| 2013–2017 | 19 [19] | nonsmooth quasi-Newton and GS (S012, S008, S004); inexact SQO and SQuID (S029, S022); AL steering (S019, S040); active-set QP and isotonic regression (S024, S067, S064); sparse and ℓ1 (S038, S050); LMSD (S042); stochastic BFGS (S028); ML tutorial (S011); TRACE and the trust funnel (S002, S039); market clearing with MERL (S077, S066) |
| 2018–2022 | 28 [27] | SIAM Review survey (S001); complexity line (S026, S035, H001, S062, S020); stochastic trust region and adaptive frameworks (S015, D001, S041; S031 abstract); first stochastic SQP (S007, S037); nonsmooth (S005, S049, S065); quasi-Newton (S046, S051); sparse (S052, S053); penalty inside the QP solver (S057); negative curvature (S014); applications and distributed (S018, S048, S056, S071, S061, S094) |
| 2023–2026 | 34 [27] | stochastic and noisy SQP and IPM (S013, S021, S030, S054, S068, S092, D002/S063, S044, S059; S045 abstract); noisy active-set identification and noisy GS (S093, S091); inexact TRACE (S043); NonOpt (S088); local-linear method on Fletcher's AL (S087); constrained proximal gradient (S082); ML fairness and optimizers (S069, S083, S089, S090; S055, S072 abstract; S084 metadata); OR applications (S016, S034, S073); SCOPF (S023; S060 abstract); DFO with surrogates (S075); incremental quasi-Newton (S076); prox-SVRG (S070); book (S074 abstract, secondary source); workshop report (S078 abstract) |

### 8.2 Turns

1. **2006–2007, combinatorics to NLP**: the pre-PhD work is matrix theory and determinant optimization [S058 pp. 2–6; S081 pp. 3–19]; the move to inexact SQP happens inside the Northwestern dissertation [S096 pp. 23, 98]. Not in the skill's trajectory table (add a 2003–2006 row, no methodological weight).
2. **2012–2013, nonsmooth line**: SQP joined to gradient sampling with Overton [S003 p. 4] and continued at Lehigh with adaptive sampling and BFGS hybrids [S012 pp. 2–5; S008 pp. 2–3].
3. **2014, Robinson enters** [S029] and stays (§9); AL steering, active-set QP and sparse methods follow (2015–2016).
4. **2016–2018, stochastic and complexity**: a single-author stochastic BFGS [S028], TRACE [S002], the survey [S001].
5. **2020–2021, stochastic SQP**: the deterministic twin and the adaptive merit parameter carried into the stochastic setting [S007 pp. 2, 26–27].
6. **2024–2026, noise moves into constraints, IPMs and active sets** [D002 pp. 3, 24; S059 pp. 3–4; S093 pp. 5–19], **plus three application or ML lines with new co-authors**: fairness and ML optimizers [S069; S083; S089; S090], healthcare OR [S016; S034; S073], power systems [S061; S094; S023]. The skill's trajectory table mentions the ML line only through its student-led optimizer preprints; the OR and power-systems lines are missing.

### 8.3 What stayed constant

- Inner accuracy derived from the outer method, 2007–2026 [S096 p. 23 → S088 pp. 3, 9].
- The merit-model skeleton and its proof devices, from the dissertation to the stochastic papers [S096 pp. 33–39 → S007 pp. 8–10 → S054 pp. 10–11].
- The rung ladder of Heuristic 10 [S096 pp. 33, 46, 59, 99 → S093 pp. 5–19].
- Guards attached to an incumbent (Method 6), 2007–2026 [S047 pp. 4–5 → S087 pp. 13–14].
- In-framework rivals with one component varied [S047 pp. 6–8 → S088 pp. 7–9].

---

## 9. Collaboration pattern

| Period | Most frequent co-authors (cards) |
|---|---|
| 2003–2007 | Drew, C.-K. Li, Pragel (S058); Kincaid (S081); Nocedal (S047; advisor of S096) |
| 2008–2012 | Nocedal 5, Byrd 3, Wächter 3, Schenk 2, Overton 1, Huber 1 |
| 2013–2017 | Robinson 7, Z. Han 3, Que 2, Burke 2, H. Wang 2, H. Jiang 2, Gould 2, Raghunathan 2 |
| 2018–2022 | Robinson 11, B. Zhou 4, Scheinberg 3, Wächter 3, Samadi 2, R. Shi 2, Burke 2, Berahas 2, Molzahn 2 |
| 2023–2026 | Robinson 16, Q. Wang 6, Wächter 4, C.-Y. Wu 4, Zebiane 4, Shehadeh 3, X. Jiang 3, L. Guo 3 |

- **Robinson** is on 35 of the 96 cards, all from 2014 on (35 of the 80 cards dated 2014–2026); review correction: S028 only acknowledges him, so he co-authors 34 works, 32 counting each possible pair once, across every line from AL steering [S019] to fairness [S083] and the book [S074 abstract].
- **Nocedal** (9 cards, 2007–2018) and **Byrd** (4, 2007–2010) frame the formative inexact-SQP and penalty work [S096; S006; S032; S009; S017]; **Wächter** is the longest continuous partner (11 cards, 2009–2025: inexact IPM in Ipopt [S010; S036], inexact SQO [S029], chance constraints [S027], SCOPF [S061; S094; S023], noisy IPM [S059], DFO [S075]).
- **Overton and Burke** carry the nonsmooth and infeasibility lines (S003, S004, S005; S022, S050, S057); **Scheinberg** the stochastic trust-region and adaptive frameworks (S011, S015, D001).
- **Junior co-authors** appear on 2–6 cards each within short windows (e.g. Que 2013–2015, Han 2015–2016, Samadi 2017–2019, B. Zhou 2020–2024, Q. Wang 2023–2026, Zebiane 2025–2026), each on one of his lines.
- **Sole-author papers** are rare and mark new lines: the dissertation [S096], PIPAL [S033], stochastic self-correcting BFGS [S028].
- **Application partners** enter in bursts and rarely return: MERL (S077, S066, S071), the GO-competition team (S061, S094, S023), Shehadeh's healthcare OR (S016, S034, S073).

---

## 10. Rejected updates

1. **A separate method for *price the guarantee***: it is Method 6 step 5 and ablates in the direction opposite to Method 5 step 3; a separate method would duplicate both.
2. **Two methods, *reduce to the incumbent* and *dormant safeguard***: one construction seen from two sides; merged (§4).
3. **Θ_k skeleton as a core method**: a proof template, not research craft; inventory only (§7.1).
4. **Rewriting Method 2 to cover all adaptive rules**: would blur its one line; Method 6 takes the non-penalty cases.
5. **Constrain-don't-weight as a numbered heuristic**: explains Tension 3 better than it guides solver design; folded (§5 c).
6. **Disclose-the-theory–code-gap as a numbered heuristic**: fails exclusivity; folded into H1 (§5 b).
7. **Replacing 45–86 % by 50–86 % in the inexact-SQP anatomy**: different versions of the experiment; keep the 2008 figure [S006 p. 17].
8. **Combinatorics-era candidates** (re-prove with an elementary tool, small-case enumeration before a conjecture, numbered open problems, exact-then-heuristic with a gap to a bound) [S058; S081]: pre-PhD, outside the skill's field; no weight.
9. **Application-specific candidates**: practitioner-set tractability bar [S034 pp. 38, 51], physically anchored weight calibration [S048 pp. 11–13], trusted audit set [S089 pp. 4–5], pushing the constraint into synthetic data [S069 pp. 3, 8], porting an algorithm to an industrial partner [S071 TR pp. 3, 5–6]: co-author-led application detail without explanatory power for solver research.
10. **Book-based claims** (e.g. the proofs-at-chapter-end layout) [S074 abstract]: secondary source; nothing about the book's methods enters the skill.
11. **Card reading notes about inconsistencies inside individual works** (typos, a count that differs between text and table, a summary sentence stronger than its table): reading notes, not findings about the researcher; not surfaced. The only general lesson kept is neutral and unattributed: recheck that prose summaries match the final tables after revisions.

---

## 11. Open gaps

- **Abstract-only works**: the stochastic inexact SQO paper [S045 abstract] (probably the journal form of S037; its termination tests for stochastic gradients are known only from the abstract); the ε-constraint fairness paper [S055 abstract] and the bilevel synthetic-data paper [S072 abstract], which would show whether constrain-don't-weight is argued beyond S082–S083; the SCOPF journal paper [S060 abstract] (the preprint S061 was read); the adaptive stochastic optimization framework [S031 abstract] (the D001 article was read); a workshop report [S078 abstract]; MOPTA proceedings [S079 abstract]; the hard-constraint training paper [S084 metadata].
- **The 2025 book** [S074 abstract]: known only from a retailer's copy of the publisher's description; its treatment of BFGS-SQP, gradient sampling and NonOpt, and whether it states a benchmarking protocol, are not known.
- **Unreadable**: S086 (undergraduate thesis), outside scope.
- **Not in the publication list**: talks, syllabi, code history and student theses remain web-research evidence (01–06); the deep reading neither confirms nor refutes the slide-only claims (Heuristic 4, the tuning-time statement, the one-test-set warning).
- **Tacit-knowledge gaps unchanged**: how trigger thresholds and test constants are set (most papers give values without a tuning account, §2 M5) and how proof errors are found (only the public correction in S005 and the corrigenda on the Errata page).
- **Exclusivity of Method 6** is argued from the contrasts the papers draw [S008 p. 21; S036 p. 12; S067 p. 8; S028 p. 2], not from a field-wide survey; the roundtable may test it against the Wächter and Fletcher seats.
- **Research-page scale figure** (minutes per iteration) remains unlocated in the full texts read [S010 p. 25; S036 p. 17].

# Nikolaos V. Sahinidis · Deep-reading synthesis (08)

> Synthesis of all paper cards in `cards/` (index: `07-paper-cards.md`), written 2026-11-20 for the team-synthesize stage (T3.6). It is a proposal for a conservative update of `SKILL.md` under the house rules (paper-reading-card.md §3; research-extraction-framework.md §3 and §11): only add; mark contradictions instead of deleting; existing methods get evidence, not duplicates; a new core method needs at least three distinct works read in full or in part plus the four-way validation. `SKILL.md` itself is not edited here.
>
> Citation form: `[S012 p. 9]` is the `[[page N]]` page of the file read for that card (the file listed in `../sources/papers/INDEX.md`). Cards read in a manuscript, preprint, arXiv, report or other manual edition carry the version word their card uses (`[S002 manuscript p. 22]`, `[S058 preprint p. 22]`, `[S046 arXiv p. 16]`, `[S012 manual p. 12]`, `[S112 v17.4.1 p. 10]`); §1 lists them. Abstract-, metadata- and unreadable-level cards are cited by ID only. Research-note keys (`[02 I1]`, `[03 §B2]`) point to the notes 01–06. Voices: from 1995 on he is usually last author behind one student; at Georgia Tech often third behind a student and a co-adviser; the BARON manuals carry his sole author line in the voice of The Optimization Firm (TOF). A practice in a co-authored paper is evidence about the group's record, not about him alone; the cards say so where it matters. Reading notes that cards record about inconsistencies inside a work are not carried into this note (house rule); §7.4 keeps one neutral lesson.

---

## 1. Coverage

| Item | Count | Source |
|---|---|---|
| Card entries | 294 in 30 batch files: round 1 core c01–c12 (41 cards) and supplement s01–s10 (72); round 2 abstract/metadata a2-01–a2-06 (176); round 3 core c3-01 (2) and supplement s3-01 (3) | digests; 07 |
| Read level | full 110 · partial 5 · abstract 116 · metadata 60 · unreadable 3 | digests |
| Works with a card | 288 distinct IDs (S 274, H 13, D 1). Six works have two cards: S025, S010, S032, S028, S053 (abstract card in round 2, full card in round 3) and S147 (metadata and unreadable) | digests |
| Index | INDEX.md has 381 rows. All 270 rows not marked skip have a card; of the 111 Role = skip rows, 18 carry metadata or unreadable cards (no method link, no candidate) and 93 have none | INDEX.md after `mark_read_from_cards.py` (carded 110, skimmed 5, abstract 111, metadata 60, unreadable 2, — 93) |
| Coverage row (`team_status.py`) | 409 Scholar rows · 381 distinct works indexed · 115 open full texts · 110 read in full · 5 in part · 111 abstract only · 44 metadata only incl. unreadable · 111 skipped · 0 book material · 435 quotes verified | 07 |
| Quote gate (2026-11-20) | 435 quotes: 435 exact, 0 equal up to spacing or symbols, 0 not found | `verify_card_quotes.py` |
| Method links | 102 of the 115 full/partial cards link Methods 1–5. The 13 without a link: S029 and S118 (the heuristics line, §4) and 11 service items: prize notices H011, H012, S289, S294, S297, S304, S318; the status report S306; the preface S342; the tribute S319; the committee roster S382. Heuristic links: 15 on 9 cards; card prose names a heuristic far more often (§2.6) | digests; card text |
| Pool material | 187 new-pattern-candidate entries on 121 cards; 391 proof-device entries (337 on full/partial cards); 515 transferable-technique entries (430 on full/partial cards) | digests |
| Full or partial texts by period | 1985–95: 0 · 1996–2000: 6 · 2001–05: 22 · 2006–10: 7 · 2011–15: 14 · 2016–20: 29 · 2021–26: 36 · undated: 1 | digests |

**Texts that count once.** Two pairs of cards read byte-identical files (checked by checksum on 2026-11-20): S077 and S097 (the BARON user's manual v4.0, revision of 28 June 2000) and S012 and S185 (the GAMS chapter of 31 March 2005 with a BARON 7.2.5 log). When projects rather than cards are counted: S243 is the talk version of S165 (same results table) [S243 p. 32]; S387 is the poster of the study in S271; S242 is the poster of the project in S206; S195 restates S052 for an agency; H006 and S122 are two versions of the CCSI tools overview; S270, S272, S273 and S277 are four decks of one benchmark refresh; the BARON manuals S077/S097, S162, S095, S012/S185, S159, S112 and S191 are editions of one document line.

**Cards read in another version** (each card names it; cited with that word): manuscripts S002, S024, S039, S052, S070, S108, S122, S134, S161, S165, S206, S238 (H007 and H009 are themselves manuscripts); preprints S010, S029, S042, S058, S069, S084, S090, S104, S118, S119, S130; arXiv S007, S022, S034, S046, S074, S116, S128, S133, S179, S182, S189, S211; report S214 (MERL technical report); manual editions S012 (the 2005 GAMS chapter), S097 (v4.0, for a 2005 entry), S159 (v15.2, for v15.6.5), S112 (v17.4.1, for a 2018 entry), S191 (v2021.1.13, for a 2020 entry). Pages cited for these are pages of the version read.

**Not evidence.** Role = skip rows (talks, session listings, committee lists, forewords, works not by him) carry no method links and no candidates and are left out of every count below except the raw card totals. The 11 service items above serve only §8 and §9.

---

## 2. Evidence per existing method

Counts are distinct cards whose digest links the method (E = evidence, V = variant, C = contradiction); a card can carry both an E and a V link, so E + V + C can exceed the card count. Counts include the two identical-text pairs of §1. *By period* counts E links per period (1985–95 / 1996–2000 / 2001–05 / 2006–10 / 2011–15 / 2016–20 / 2021–26 / undated).

| Method | Cards (E / V / C) | Full or partial | Evidence by period | Say–do after the full texts |
|---|---|---|---|---|
| M1 Reduce before you branch | 60 (46 / 15 / 0), 59 works | 42 | 0 / 8 / 12 / 4 / 2 / 10 / 10 / 0 | ✅ stated + practised 2000–2026; refined: a speed claim, not a convergence requirement |
| M2 The production solver is the lab notebook | 85 (53 / 35 / 0), 85 works | 61 | 1 / 3 / 14 / 2 / 8 / 15 / 9 / 1 | ✅ through 2022; ⚠ 2023–26 for the co-supervised Georgia Tech lines, which build outside BARON |
| M3 Make the black box algebraic, keep the algebra small | 58 (38 / 28 / 3), 58 works | 39 | 0 / 0 / 0 / 1 / 11 / 13 / 13 / 0 | ⚠ partial, as before: steps 2, 3, 7, 8 ✅; step 4 ✅ from 2015; steps 5 and 6 uneven |
| M4 Enter with a benchmark; certified ground truth and portfolios | 74 (30 / 51 / 7), 74 works | 61 | 0 / 0 / 1 / 1 / 4 / 11 / 13 / 0 | ✅ steps 1–3, 5, 6; ⚠ step 4 only in 2013; ✗ step 7 for the group's own algorithms and BAM |
| M5 A relaxation's strength counts only at speed | 59 (41 / 24 / 2), 56 works | 43 | 0 / 1 / 12 / 1 / 6 / 9 / 12 / 0 | ✅, practised in 2002 before it was stated in 2005 |

### Method 1 · Reduce before you branch

- **Strongest practice.**
  - The rule SKILL.md cites only through restatements is read in its full-text statements: the marginals-based test from the relaxation's value function [S077 pp. 12, 15; S058 preprint pp. 6–7; S162 pp. 12–14]; reduction on every node in pre- and post-processing, the node re-solved while reduction is significant [S077 pp. 20–21, 50; S162 pp. 18–19].
  - One dual master problem yields the toolbox: optimality-, marginals-, probing- and feasibility-based reductions as choices of one homogenized Lagrangian problem, duality-based reduction re-run whenever a bound or the incumbent changes, a learning reduction after fathoming, and the 1996 cut shown to be the same or weaker [S006 pp. 11–19]; the same derivation in 2017 [S046 arXiv pp. 12–13].
  - Ordered by cost: the exact 2n bound LPs once at the root, cheap propagation at the nodes [S162 pp. 16–18; S077 pp. 18–19]; probing LPs only for the variables that carry the gap [S069 preprint pp. 5–6]; bound problems ranked as nonconvex, convex NLP, LP, with the expensive ones spent by a stated rule [S046 arXiv pp. 5–6, 11, 15].
  - The contribution shown by switching reduction off in three production solvers, library by library [S046 arXiv pp. 15–16, 21, 24–25, 35].
  - Rebuild on the reduced box: "Therefore, it is critical that the reformulation scheme of Section 3 be applied at every node of the branch and bound tree using the tightest derivable bounds on each fractional term." [S101 p. 14]; node-wise bounds from exact subproblems, then a rebuilt relaxation [S053 pp. 14, 17–18, 21]; spectral QPs recomputed on each node's unfixed submatrix beat a stronger static root reformulation [S116 arXiv pp. 10, 30].
  - Carried to new classes: refrigerant design (root presolve cuts group bounds from 15 to 5, probing at every node) [S035 pp. 11–12]; Lennard-Jones clusters (incumbent-driven distance bounds) [S190 pp. 4–9]; Euclidean-norm problems (symmetry elimination framed as domain reduction) [H007 pp. 18–19, 23–25]; LP presolve (routines ordered by cost, the expensive elimination rationed by its predicted payoff) [S239 pp. 8–10, 17, 19–20].
- **Stated.** "Because considerable emphasis is placed on the reduction of variable bounds, the overall methodology is referred to as branch-and-reduce" [S069 preprint p. 2]; "Thus, there exists a need to balance the effort involved in domain reduction in order to reduce the average effort per node." [S046 arXiv p. 15].
- **Say–do update.** ✅ unchanged. One refinement for Limitations: reduction is not needed for convergence and is a speed device [S046 arXiv pp. 2, 9].
- **Step 4, dated.** The rationing of probing moved by edition: off by default in 2000 and 2002 [S077 p. 49; S162 p. 43]; on and scheduled by depth (pstart, pend, pfreq 3), with capped reduce and re-relax passes, from the 2003 manual on [S095 p. 10; S012 manual pp. 9–10]; the number of probing problems decided automatically from 2015 [S159 v15.2 pp. 18, 22–23; S112 v17.4.1 pp. 23–24; S191 pp. 24–25]; a learned per-instance off-switch judged against the per-instance ceiling in 2025 [S212 pp. 2, 10, 16]. Proposed: one line in step 4.
- **Variants.** Structure decides where to cut, not how far to shrink [S014 pp. 11–14]; the reduction removes enumeration altogether (an IP reduced to a linear system over F2, the IP kept as fallback) [S198 pp. 2–5]; non-valid reductions priced by the share of the space removed, the deviation from the exact optimum and the speed-up [S254 p. 1]; reduction moved into the model (symmetry cuts, interval big-M constants) [S108 manuscript pp. 3, 6, 9]; heuristic box shrinking for feasibility, not bounding [S238 manuscript pp. 14–15]; step 2 practised for feasibility rather than for reduction (an outside incumbent handed to SCIP) [S165 manuscript pp. 11, 24, 26].
- **Proposed text.** Limitations: replace *the 1995-96 full texts were not read* with *the 1995–96 papers are read at abstract level only [S008; S013]; the rule's full-text statements are [S077 pp. 12, 15] and [S006 p. 15]*, and add the speed-claim refinement.

### Method 2 · The production solver is the lab notebook

- **Strongest practice.**
  - The code history, version by version, with the students who shaped it [S077 pp. 7–9]; "It still serves as a system that facilitates experimentation with novel branch-and-bound algorithms for global optimization." [S162 p. 2].
  - Every reduction family a named switch, version and build printed in every log [S012 manual pp. 3, 9–13; S159 v15.2 pp. 9–11; S112 v17.4.1 pp. 10, 20–28; S191 pp. 11, 21–30].
  - The papers' constructs ship in the same year's manual (CONVEX EQUATIONS and RELAXATION ONLY EQUATIONS as equclass options) [S003 p. 15; S069 preprint p. 9; S012 manual p. 12]; each is judged as BARON with the component on and off, per library [S003 pp. 17–23].
  - Named builds as ablation units [S090 preprint pp. 17–18, 22–27]; a rival method rebuilt inside BARON as a named variant, and the new relaxation made the solver's default [S116 arXiv pp. 26, 29]; a like-for-like switch that keeps the earlier module [S133 arXiv pp. 18, 20–21]; the FME presolve embedded in BARON and evaluated as a module with and without FME [S239 pp. 20–21, 32].
  - An application class became an engine feature: all or K-best solutions and LP relaxations from molecular design [S035 p. 11; S070 manuscript p. 13].
  - Progress tracked across versions: an old formulation gain re-tested on a newer BARON and reported as gone [S190 p. 15]; one benchmark protocol kept for 13 years with the solvers tagged same, updated or new [S272 pp. 4–5, 8–9].
- **Stated.** Modeling languages for global optimization "facilitate the automation and systematic testing of global optimization algorithms" [S069 preprint p. 2]; BARON has many options because it is an experimentation platform, and its defaults come from "years of extensive computational experimentation with a large set of benchmark instances" [S084 preprint pp. 3, 5].
- **Say–do update.** ✅ for 1991–2022. ⚠ for 2023–2026: the co-supervised Georgia Tech lines prototype in Python/Pyomo or SCIP and use BARON as baseline or bound source [S128 arXiv pp. 17–19, 24; S165 manuscript pp. 23–24; S238 manuscript pp. 4, 16, 19; S284 pp. 9, 24; S269 arXiv p. 11; S189 arXiv pp. 19, 21; S211 arXiv p. 13; S388 p. 1], while BARON-internal papers of the same years are first-authored by TOF staff [S212 pp. 9–10; S239 pp. 1, 32]. This answers part of the Limitation *who writes the code today is undocumented*.
- **Variants.** The lone version, practised: GPU-BLAST built on NCBI-BLAST with an exact off switch [S015 pp. 2, 5–7]; learned branching built in SCIP [S284 pp. 9, 24; S269 arXiv p. 11]; ALAMO shipped as a module of the sponsor's framework [H006 p. 2; S122 manuscript p. 3]. Testing inside a closed solver through its public channels: cuts passed as relaxation-only constraints [S044 p. 16]; an alternative decomposition at fixed options [S109 pp. 31–32]; the new presolve applied after CPLEX's presolve and fed back to it [S239 p. 21]. The fixed cross-paper protocol of step 3 is a later habit: the 2004 algorithm paper names no BARON version and compares with published times from another machine [S006 pp. 22–26]; by 2017 it is one machine, 500 s, 10^-6 and GAMS [S046 arXiv pp. 15–16].
- **Proposed text.** Limitations: *who writes the code today* → the record above. Lone version: add *if the solver is closed, test through its channels (relaxation-only constraints, an alternative decomposition, your module after its presolve) [S044 p. 16; S109 pp. 31–32; S239 p. 21]*. Step 3: *(the fixed protocol dates from the 2010s; not yet in 2004 [S006 pp. 22–26])*.

### Method 3 · Make the black box algebraic, and keep the algebra small

- **Strongest practice.**
  - Steps 2–5 in one paper: a physics-seeded basis, exact best-subset MIQP, certified output bounds that rescue extrapolation, and adversarial sampling that beats same-size LHS in 120 of 150 problems, with the loss to LHS-50 reported [S017 pp. 5–8, 10–11, 13–14].
  - The source of step 4: bounds and physical relations imposed during fitting and certified over the whole domain by a global solve [S039 manuscript pp. 2, 4–5, 7–9, 30–31].
  - A physics-built superset, BIC sizing, adaptive sampling, and derivative-free search only for what stays black-box [S104 preprint pp. 4, 7–9, 14–17, 27]; a motif basis, derivative constraints during fitting and symbolic regression as a global MINLP [S108 manuscript pp. 3, 9–10, 14–16].
  - Sparse quadratics from 10 points match complex surrogates at a fraction of build and optimization time, embedded in a global solver and compared with DFO on the raw simulator [S206 manuscript pp. 12, 17–27].
  - Surrogates settle the configuration; rigorous simulation or DFO then verifies it [S173 pp. 2, 5–6; S347 pp. 11, 19; H006 p. 4]; surrogates fitted unit by unit and assembled into one MINLP [S122 manuscript p. 17].
  - The price stated (four to five orders of magnitude) [S271 pp. 6–10, 15–16]; the small-model rule carried into learned solver components [S284 pp. 9, 11, 13, 17, 25; S269 arXiv pp. 7, 9–10, 15–16].
- **Stated.** In his 2016 brochure: "ALAMO returns the simplest regression model possible that fits the data well. As a result, humans can inspect ALAMO’s models and confirm the physical correctness of these models before using them." [S249 p. 81]; the division of labour of step 1 [S122 manuscript pp. 7–8, 17].
- **Say–do update (stays ⚠ partial).**
  - Adaptive sampling: the 2012 release packaged error-maximization sampling as a standard method without naming the default sampler [S347 pp. 19–20]; a 2017 third-party assessment marks adaptive sampling as not yet available while the brochure describes it [S249 pp. 16, 24, 47, 81]. This corroborates Inner Tension 6 from outside the group.
  - Step 4: ✅ from 2015 [S039 manuscript pp. 7–9]; in 2013 a physical bound was applied after fitting by clipping [S052 manuscript pp. 8, 16, 19]; in 2019 first-principles consistency was not imposed [S104 preprint pp. 8–9, 18, 20]; in 2022 the constraints held at sample points only [S108 manuscript pp. 14–16, 36].
  - Step 6 (read the model) is shown where selected terms are labelled with their physical meaning [S173 p. 4] or trends are read against CFD [S103 pp. 10–13], not in the 2017 methods paper's examples [S017 pp. 8–14].
  - Step 7: the 2026 symbolic-regression MINLP is solved by randomized rounding of a relaxation, with no bound reported [S271 pp. 8, 10; S387 p. 1].
- **Variants.** Derivative-free search kept for a low-dimensional continuous interface, with an exact inner subproblem [S160 pp. 3–4; H013 pp. 2–3]; for noisy data the group's own advice is shrinkage on top of a sparsity term [S182 arXiv pp. 5, 7, 9]; self-driving labs send the experimental black box straight to DFO [S205 pp. 1–2, 4, 6–7; S270 pp. 2, 17–18; S272 pp. 2, 17–18]; surrogates judged by how well they optimize, not only by fit [S206 manuscript pp. 15–16, 23–26; S242 p. 1]. Contradiction links (§3.1): S086, S181, S183.
- **Proposed text.** Limitations: replace *the 2014 and 2015 full texts were not read* by *2014 read at abstract level only [S009]; 2015 read in full [S039 manuscript]*, and add the noisy-data advice [S182 arXiv p. 9]. Evidence: S039 as the source of step 4; S206 as the current core case.

### Method 4 · Enter with a benchmark; judge by certified ground truth and portfolios

- **Strongest practice.**
  - The 2013 source study [S001 pp. 2–3, 20–23, 30–33, 37, 41] and its 2022 sequel on the mixed-integer class [S063 pp. 3, 7, 13–14, 19–21, 27].
  - A solver's own option tuning used as a real black box for 27 DFO codes, failures counted, a covering subset reported [S084 preprint pp. 2, 6–7, 13–15]; existing implementations benchmarked on an industrial problem before any own method, with enumerated ground truth on small cases [S074 arXiv pp. 9–19]; a tuning space small enough to enumerate [S134 manuscript pp. 5–8, 12, 15–18].
  - A new class entered with a public library of 1,352 instances and five named solver versions before any own algorithm [H007 pp. 7, 9, 12–14, 16].
  - The 2013 protocol rerun 13 years later on 42 codes, with a virtual-best curve and a minimal covering portfolio [S272 pp. 4–5, 7–8, 14–16; S270 pp. 4–5, 7–16].
  - The group's own local solver judged later, on the 2013 library [S170 pp. 24, 26, 31].
- **Early form (1999–2005).** The certified optimum as yardstick against the literature's local designs, on the literature's own instances: per-instance savings over published designs [S058 preprint pp. 13–15; S079 pp. 5–6]; distributions of 100 local values beside certified optima [S025 pp. 11, 14–15]; certified values exposing inferior local solutions in a library's source [S006 p. 26]; a new optimum for a library problem [S003 p. 23]; the incumbent phasing method shown to return local minima [S168 pp. 4, 7]; a fast method checked against an exact solver's global minima [S198 p. 6]. These are small sets with no portfolio conclusion; the large-library form starts in 2013.
- **Census variant.** An application field entered by mapping all that exists, as a complexity classification of every published formulation [S024 manuscript pp. 2, 27, 33] or a 446-entry annotated bibliography that records test-problem provenance [S010 preprint pp. 2, 8, 10–79].
- **Say–do update.** §3.2 items 7 and 8: the 2013 hold-out is a transformed copy of the same problems; the 2022 study has no developer rounds or hold-out; step 7 is not applied to the group's own new algorithms and products in five full texts [S161 manuscript pp. 4–5, 7; S170 pp. 24–29; S238 manuscript pp. 19, 21–22; S239 p. 16; S270 pp. 8, 14, 19].
- **Proposed.** One new step on instance design (§5.3 D); the dated qualifiers of §3.2 items 7 and 8.

### Method 5 · A relaxation's strength counts only at speed

- **Strongest practice.**
  - 2002: eight relaxations compared on gap, CPU time and solver failures; the LP of (R7) chosen by average gap and solution time [S053 pp. 21–25].
  - 2005: the one nontrivial loss explained by LP cost per node: "This problem is mostly linear and the cutting planes, apparently, reduce the size of the search tree at the expense of larger and more time consuming LP relaxations." [S003 p. 22].
  - 2009: a multiterm polyhedral relaxation admitted only after BARON solves more instances faster with it, its construction time reported beside the gap it closes [S044 pp. 2, 12, 15–18].
  - 2011: dominance proved, then every relaxation priced by CPU time; a cheap balance relaxation recommended beside the strongest [S018 pp. 2–3, 17–19, 27].
  - 2020: a cut family chosen because its separation can be made cheap, with automatic deactivation on large problems [S090 preprint pp. 16–17, 22, 24].
  - 2021–22: a stronger static root reformulation loses to cheaper per-node relaxations; QP answers checked against KKT; per-node switching; SDP-quality bounds from quadratic cuts with the expensive step at the root only [S116 arXiv pp. 10, 19, 22–25, 30; S133 arXiv pp. 1, 12, 16, 18–22].
  - 2024: three equivalent encodings of a convex master implemented and the fastest kept; a subsolver dropped for constraint violations [S128 arXiv pp. 16–19].
- **Stated.** "Nonlinear programming solvers, however, often fail even in solving convex problems." [S006 p. 3]; "Declaration of an inferior solution as optimal by a convex programming solver is fatal in the application of branch-and-bound to global optimization problems." [S162 p. 23]; "Linear relaxations may provide weaker bounds than nonlinear ones, but can be solved very efficiently." [S046 arXiv p. 6]; molecular design named as what moved BARON from nonlinear to LP relaxations [S070 manuscript p. 13].
- **Say–do update.** ✅; practised in 2002 [S053 pp. 21–25] before its 2005 statement, while a theory paper of 2001 argued for SDPs on strength alone [S032 pp. 2, 20] (§3.2 item 10).
- **Variant (the yardstick generalizes).** The bound-per-second test is applied beyond relaxations: tuning effort set against the seconds it saves [S084 preprint pp. 9, 15–17]; the whole tuning path priced before cross validation [S182 arXiv pp. 6–7]; learned branching rules judged by solve time, memory, data and inference hardware [S269 arXiv pp. 9–12; S284 pp. 11, 13, 22]; surrogates by build time, optimization time and solver failures [S206 manuscript pp. 18–26; S242 p. 1]; pruning rules by share removed, deviation and speed-up [S254 p. 1]. Proposed: one sentence under *Different from standard practice*, not a new method (§10).
- **Variants (strength-only rankings in theory papers).** [S025 pp. 7–10, 12; S028 pp. 12–16; S109 pp. 17, 22–23, 32; H007 pp. 17, 22–23; S211 arXiv pp. 13–14]; an expensive exact separation made cheaper rather than emulated [S388 p. 1].
- **Proposed.** A step 0, *order before you price* (§5.3 B); Limitations: *full texts of the 2004, 2005 and 2018 papers were not read* → 2004 [S006] and 2005 [S003] read in full, 2018 [S030] abstract only.

### 2.6 Existing heuristics: evidence and variant notes

Counts are full/partial cards whose prose names the heuristic (most links sit in card prose, not in `method_links`).

| Heuristic | Cards | Strongest new evidence | Variant or calibration |
|---|---|---|---|
| H1 Special classes first | 17 | Eleven specialized class modules beside the general module in 2000 [S097 v4.0 pp. 7–8, 36–41]; the general module checked against the specialized one on its class [S006 pp. 23–24]; centrosymmetric phasing first, the general case next [S168 p. 8; S361 p. 1]; a class whose five-atom instances defeat three of four solvers [S190 pp. 1, 3, 16] | Size the class by library statistics: the libraries' rank is at most 5, so a fixed-rank algorithm is justified [S090 preprint pp. 5, 8, 11, 14]; 9,000 library expressions distilled to 19 forms [S211 arXiv pp. 11–13]; [S106] |
| H2 Problem knowledge before options | 14 | CONVEX EQUATIONS: 99.5% gap reduction, 35 vs 1793 nodes [S003 p. 17]; a stationarity condition proves globality at the root instead of after 29 nodes, while a local solver declares the model locally infeasible [S069 preprint pp. 8–9]; equclass [S012 manual p. 12]; physically meaningful bounds [S185 pp. 7, 12]; added chemical constraints cut the solve from 45 to about 30 minutes [S035 pp. 12–13]; bounded problems solved more often by DFO codes [S001 pp. 20, 36, 41] | Calibration: the relaxation-only construct pays in local-search time, not in global search: "CPU time gains by using this construct as opposed to merely adding the nonlinear constraints to the nonlinear formulation were not significant as far as global search is concerned" [S069 preprint p. 22] |
| H3 Users' models as bug finder | 9 | Numerical difficulties to be reported to the developers [S012 manual p. 4; S162 p. 39]; 163 researchers and users submitted over 6,100 problems between October 1999 and July 2002 [S162 p. 2]; sponsors' processes as projects [S183 pp. 1, 8; S334 p. 2] | Count: §3.2 item 16 |
| H4 Strongest fair baseline | 13 | Competitors chosen by the switch they allow [S046 arXiv p. 15]; stronger CPLEX aggregator settings as a second baseline [S239 p. 22]; a rival rebuilt inside the own solver [S116 arXiv p. 29]; trivial instances set apart by a written rule [S044 p. 17]; equal-task timing [S182 arXiv p. 6] | A domain baseline run at defaults, with one tuned rerun and its developer consulted [S198 p. 7]; an ANN baseline tuned as typical users do [S206 manuscript pp. 13–14] |
| H5 Measure the ceiling first | 4 | Every instance solved under each setting; labels within 10% dropped [S212 p. 10]; per-instance best 57% against one setting for all 34% [S084 preprint pp. 8, 11] | A hand-made rule scored against exact enumeration and the worst rule [S116 arXiv pp. 20–21]; a perfect-information oracle as ceiling [S034 arXiv p. 17] |
| H6 Reproducible by construction | 10 | Version, build and the paper to cite in every log [S112 v17.4.1 p. 10; S159 v15.2 p. 9; S012 manual p. 3]; nondeterministic options flagged [S159 v15.2 p. 20; S112 v17.4.1 pp. 21–22; S191 p. 22]; machine-independent counts and machine ratings in 2004 [S014 pp. 20–21]; permuted replicas with distinct seeds [S239 pp. 17–18] | Version and machine not named in a 2025 paper [S212 pp. 9–10] |
| H7 Evidence apart from proof | 17 | Local values reported beside certified optima [S025 pp. 14–15]; a gap labelled as a gap to the LP bound [S029 preprint p. 26]; optimality claimed only where the a posteriori ratio is 1 [S119 preprint pp. 18, 20]; every heuristic value with a dual bound and a gap [S243 p. 32; S238 manuscript pp. 17–20]; the multistart mode labelled a heuristic [S185 pp. 2, 5–6; S112 v17.4.1 p. 18] | "Proof of global optimality" wording with tolerances unstated [S190 pp. 1, 14–17] (Inner Tension 7) |
| H8 Keep the rival's insight | 2 | A rival's constancy insight kept and its enumeration replaced [S014 pp. 4, 8]; trust-region radius shrinking kept, its geometry rules relaxed [S170 pp. 3, 23] | Adds two written cases to the one ASR source |
| H9 Cheap complete student projects | 2 | The true black-box applications of the 2013 study were MS theses in the same department [S001 p. 41]; an MS thesis of the same title as S084 (per note 04) | — |
| H10 Keep the engine when the source moves | 8 | Global optimization proposed for stochastic and chance-constrained programs [S002 manuscript pp. 18–22]; the DFO engine moved to a materials-science group's devices [S205 p. 1]; sponsors' engineers as co-authors [S181 pp. 1, 5; S183 p. 8] | Abstract-level cases: chip layout, planning as concave minimization, fuzzy programs, robust control [S051; S093; S041; S176] |

---

## 3. Variants and contradictions

### 3.1 The twelve contradiction links, checked against their cards

| Card | Method | What the card shows | Weight | Verdict |
|---|---|---|---|---|
| S025 (1999) | M4 | Rivals' published numbers from other machines and tolerances, and a single-winner conclusion [S025 pp. 12, 15] | Dated, before the 2013 protocol; the authors argue from their own handicaps [S025 p. 12] | Dates M4's identical-conditions form to 2013 on; no change to the method |
| S161 (2008) | M4 | Defaults tuned on the 15 structures that report the gain [S161 manuscript pp. 4–5, 7] | Another author is first and corresponding; a module in another group's crystallography program | Extends Inner Tension 5 back to 2008 |
| S170 (2025) | M4 | Single-winner verdict beside reported rival wins; no hold-out or tuning protocol for the defaults [S170 pp. 24–29] | He is corresponding author | A genuine step-7 gap for the group's own algorithms |
| S238 (2026) | M4 | Defaults chosen on the instances that carry the headline; the published sensitivity tables show the improvements depend on them [S238 manuscript pp. 19, 21–22] | Student-first, with Dey | Weak on his own practice; same pattern |
| S239 (2026) | M4 | Implementation choices made on the same LPs used for the claims, disclosed in the text [S239 p. 16] | TOF-authored BARON module | Step-7 gap, disclosed |
| S270 (2026) | M4 | BAM ranked first on the 502 problems with no hold-out or developer rounds on the slides [S270 pp. 8, 14, 19] | Talk slides | Inner Tension 5 reaches academic talks (also [S272 pp. 5, 7–8, 14]; [S273 pp. 10–11, 20]; [S277 pp. 3–4, 10]) |
| S249 (2017) | M4 | Comparative claims in a brochure without a benchmark [S249 pp. 80–81] | Firm voice | Inner Tension 3, as stated |
| S086 (2022) | M3 | Direct black-box optimization beats both surrogate routes; a ReLU network beats ALAMO on the more complex system [S086] | Abstract only; co-authored with Dow | Inside the scope clause (step 1 bars DFO only for discrete designs); a reported loss, which Workflow D asks for. No change |
| S181 (2020) | M3 | A neural policy on a data-driven simulator, no algebraic model [S181 pp. 3–4] | Fourth of five authors, industrial | Marks the range of lines he co-signs. No change |
| S183 (2017) | M3 | A simulator with integer staffing decisions searched one role at a time [S183 pp. 17, 19–28] | Fourth of four, role unstated | No change |
| S032 (2001) | M5 | SDPs proposed "instead of the traditional linear programming relaxations" on strength and polynomial solvability, with no time or failure evidence [S032 pp. 2, 20] | Theory paper, dated | Refines Inner Tension 2 (§3.2 item 10) |
| S189 (2025) | M5 | A comparison with BARON ranked by root bound only [S189 arXiv pp. 19, 21] | Co-authored, another faculty member corresponding | Weak. No change |

No contradiction overturns a method. Three refine dated claims: when M4's protocol starts, how far Inner Tension 5 reaches, and the history behind Inner Tension 2.

### 3.2 Claims of SKILL.md that the full texts change (full texts win over web snippets)

| # | SKILL.md location and current text | Full-text finding | Proposed change |
|---|---|---|---|
| 1 | Honest Boundary, *Claimed but unverified ... an 'optimization-based science of heuristics' (no paper after 2004)* | Practised in six full texts: complexity [S024 manuscript pp. 10–25], open problems that set the agenda [S010 preprint p. 8], approximation schemes with proofs and a relaxation bound on every run [S029 preprint pp. 14–26; S119 preprint pp. 17–22; S118 preprint pp. 9–21], and his sole-authored statement of the paradigm [S002 manuscript p. 18]. S118 was published in 2008 from a 2000 manuscript; later echoes in 2021 [S213] and 2026 [S238 manuscript pp. 10–17] | Promote (§4). Keep only the stated long-term goal (a science of heuristics yielding provably optimal heuristics, [02 T3]) among the goals not pursued |
| 2 | Honest Boundary, *Not read: ... Tawarmalani & Sahinidis 2004 and 2005, Cozad et al. 2014 and 2015 ..., Kılınç & Sahinidis 2018 not read at all* | 2004 [S006], 2005 [S003] and 2015 [S039 manuscript] read in full. Still abstract level: Ryoo & Sahinidis 1995 [S008] and 1996 [S013], the 1996 BARON note [S004], Cozad et al. 2014 [S009], Khajavirad & Sahinidis 2018 [S030], Kılınç & Sahinidis 2018 [S027], Zhang & Sahinidis 2025 [S083] | Update the list |
| 3 | Honest Boundary, *Unconfirmed and not used: ... the SIAM Review paper with Kuznetsov* | The manuscript is read in full; the file is undated and carries no journal header, so the venue is still unconfirmed [H007] | Use as a manuscript; venue unconfirmed |
| 4 | Method 1 Limitations, *the 1995-96 full texts were not read* | Still true; the rule's full-text statements are [S077 pp. 12, 15; S058 preprint pp. 6–7] and its restatement with proof [S006 p. 15] | §2, Method 1 |
| 5 | Method 3 Limitations, *the 2014 and 2015 full texts were not read* | 2015 read; it is the source of step 4 [S039 manuscript pp. 4–5, 7–9] | §2, Method 3 |
| 6 | Method 5 Limitations, *full texts of the 2004, 2005 and 2018 papers were not read* | 2004 and 2005 read [S006; S003]; 2018 abstract only [S030] | §2, Method 5 |
| 7 | Method 4 Say–do, *✅ for the 2013 and 2022 studies*; the 2013 hold-out *kept as a disagreement* | 2013: optima certified "for most" problems [S001 p. 21]; the unseen set is the same 502 problems after an affine change of variables with condition number 2 [S001 p. 41], which settles the disagreement toward note 03's reading, although the authors write that the transformation "otherwise changes the problems considerably, including the shape of the objective functions and location of all local solutions" [S001 p. 41]. 2022: steps 1–3, 5 and 6 hold; no developer rounds, no hold-out, and a bare 2,500-evaluation budget [S063 p. 13] | Rewrite the say–do line with these qualifiers and drop the disagreement note |
| 8 | Method 4 Say–do ⚠ and Inner Tension 5, *BAM claims rest on libraries ... no hold-out mentioned* | The same gap in the group's own algorithm papers [S170 pp. 24–29; S239 p. 16], in a 2008 crystallography code [S161 manuscript pp. 4–5, 7] and in 2025–26 talk slides that rank BAM first [S270 pp. 8, 14, 19; S272 pp. 5, 7–8, 14] | Extend Tension 5 from product pages to papers and talks |
| 9 | Inner Tension 1, "It appears unlikely that general-purpose algorithms will solve such problems exactly." (FOCAPO 2003, sole) | The sentence stands verbatim in the 2004 journal manuscript [S002 manuscript p. 22] and in the FOCAPO 2003 text (checked 2026-11-20 against the PDF at the URL in SKILL.md's Sources). The following sentence differs by version: the journal manuscript reads "Instead, we anticipate the development of problem-specific approximation schemes" and cites Ahmed & Sahinidis (2003) [S002 manuscript p. 22]; note 02's FOCAPO wording, with *we expect to see* and the year 2002, matches the FOCAPO PDF | Keep the quote; quote the follow-up only with its version and year |
| 10 | Inner Tension 2, *polyhedral-only (2005) vs hybrid LP/NLP (2018), a dated change on the same stated grounds* | A sequence, not one change. In 2000 the IQP module defaulted to a quadratic relaxation and a mixed-integer SDP module shipped [S077 pp. 40, 43, 53, 92–95]; in 2001 a theory paper proposed SDPs on strength [S032 pp. 2, 20]; in 2002 an LP was chosen by gap and time [S053 pp. 21–25]; in 2004 LP-only was argued from NLP unreliability while the code still linked NLP and SDP solvers [S006 pp. 3, 7, 23]; 2005 polyhedral [S003 pp. 1–2, 15]; 2011 SDPs priced at three orders of magnitude more time [S018 pp. 1, 18–19]; 2018 hybrid [S030]; 2021–22 SDP-quality bounds from convex quadratic cuts with per-node switching [S116 arXiv pp. 22–25; S133 arXiv pp. 12, 18–22]; 2025 a quadratic-relaxation hierarchy re-tested because convex QCQP solvers improved [S189 arXiv pp. 1–2; S211 arXiv pp. 2, 13–14] | Replace the two-point tension by this dated line; the constant is subsolver speed and reliability (Method 5 step 7) |
| 11 | Signature Work Anatomy 1996, *Minimum evidence: Ryoo's 1995 MS thesis on range reduction [01 SW1]* | Two primary records disagree: the CV lists the thesis under 1995 (RESOURCES row 330), while the 1996 paper's own reference list dates it 1994 (reference 53 on the Springer page read in round 2 for the abstract-level card [S013]). The thesis itself could not be looked up | Drop the year: *Ryoo's MS thesis on range reduction* |
| 12 | Signature Work Anatomy 2005, *Key insight: constructive convex envelopes; entirely linear relaxations*, and its minimum-evidence figure *by up to 100%* | The operative insight is lifted outer approximation: linearize a composition layer by layer in lifted variables, which is tighter than direct linearization and, for separable sums, matches what direct linearization needs exponentially many cuts to reach [S003 pp. 3–7]; constructive envelopes appear only as one proposition [S003 pp. 13–14]. The 100% figure is the top of a range in the abstract [S003 p. 1]; the body gives average root-gap reductions of 48% on globallib and 20% on minlplib (27% without one explained outlier) [S003 pp. 19–21] | Correct the key insight; add the averages beside the abstract figure |
| 13 | Signature Work Anatomy 2005, *Abandoned: the 2000 mixed-integer SDP module (gone by 2026, reason unknown)* | The module is documented in 2000 [S077 pp. 92–95] and still in the 2004 code [S006 p. 23]; no card gives a reason | Add the dates; reason still unknown |
| 14 | Method 2 Limitations, *who writes the code today is undocumented* | Partly documented (§2, Method 2) | Replace with the record |
| 15 | Workflow B1 step 3, *(inferred from Method 1; no source states this test)* | Co-authored sources exist. Scaled-time convergence profiles of the solved instances show dual bounds that start weaker than primal bounds and improve more slowly, with the optimum often found by local search in preprocessing [H007 pp. 14, 17]; a no-reduction profile that catches up means the component serves the proof [S046 arXiv p. 16]; a two-solver preliminary run in which the dual bound improves but no feasible point appears names the primal side as the bottleneck [S165 manuscript p. 11; S243 p. 17; S238 manuscript pp. 3, 14; S128 arXiv p. 19] | Replace the parenthesis by these sources. The sources diagnose a library or an application after the fact; the decision rule on one user's stalled log stays this skill's inference, and H007 warns that its profiles are not for comparing solvers [H007 p. 17] |
| 16 | Heuristic 3, *164 users submitted over 6100 problems ... (2002 book acknowledgments)* | The 2002 GAMS/BARON 5.0 manual counts 163 researchers and users, October 1999 to July 2002 [S162 p. 2] | Give the number with its source |
| 17 | Activation Rules, roundtable: *Until references/research/07-paper-cards.md exists, cite research notes as [0N item]* | 07 exists (294 rows, 2026-11-20) | Allow card citations |

### 3.3 Points raised by the reading rounds, checked at source

| Point | Check | Result |
|---|---|---|
| (1) Ryoo's MS thesis year | CV entry via RESOURCES row 330; the 1996 paper's reference list on its Springer page (saved in round 2) | Conflict, 1995 vs 1994: drop the year (§3.2 item 11) |
| (2) The S002 p. 22 follow-up sentence | `S002` text p. 22 read; FOCAPO 2003 PDF fetched from the URL in SKILL.md's Sources and text-extracted (2026-11-20) | Both versions exist and both are his; note 02 quotes FOCAPO correctly; the journal manuscript differs (§3.2 item 9) |
| (3) H007 pp. 14, 17 as a source for Workflow B1 step 3 | `H007` text pp. 14 and 17 read | Confirmed, with the limits in §3.2 item 15 |
| (4) Version references | Every card named reads a manuscript, preprint or manual chapter; S012 and S185 are the same file | Cited with version words throughout this note (§1) |
| (5) Role = skip rows | Digests of the 18 skip-role cards | No method link and no candidate in any of them; excluded from all counts |
| (6) CPU models and releases | This note writes them in inline code, e.g. Xeon `X5650`, Matlab `R2010a` | `check_citations.py` runs clean on this file |

---

## 4. Promotions

**One promotion: Method 6.** Eight clusters reached three or more distinct works read in full or in part; one passes all four checks. Adding it gives six core methods, inside the 3–7 range, so nothing is merged or replaced.

| Cluster (merged by meaning) | Works read in full/part | 1 Recurrence | 2 Say–do | 3 Executable, non-standard | 4 Exclusivity | Result |
|---|---|---|---|---|---|---|
| Prove the problem hard, then design heuristics with proven and computed quality bounds | S024, S010, S029, S002, S119, S118, S238 (7; abstracts S061, S138, S088, S213) | ✅ 1995–2004 manuscripts across process planning, capacity expansion, HENS and the TDTSP; echoes 2021, 2026 | ✅ sole-authored statement [S002 manuscript p. 18]; [S010 preprint p. 8]; [02 T3] | ✅ | ✅ in his field and period (below) | **Method 6** |
| Carry the integer-programming device into continuous global optimization; linearize where the domain is discrete in disguise | S025, S053, S101, S035, S168, S198, S361, S388 (8; abstracts S036, S054, S263) | ✅ 1999–2024 | ✅ [02 I1]; [S101 pp. 1–2] | ✅ | ✗ importing MIP devices is the standard route of MINLP solver design; the papers credit the IP sources [S006 pp. 15–16] | Heuristic-eligible; written into Workflow B2 step 3 (§5.3 A) |
| Unify and order before you price: one master problem recovers the literature's rules, a proven dominance order, then computation among the non-dominated | S032, S028, S053, S006, S046, S018, S025, S133 (8) | ✅ 1999–2022 | ✅ the 2002 book's preface names a unified treatment of existing and new domain-reduction techniques among its results [02 I1] | ✅ | ✗ subsumption and dominance proofs are the standard theory move, and the core output of the Dey and Burer lenses | Heuristic-eligible; written into Method 5 step 0 and Method 1 (§5.3 B) |
| Make the tree finite where the structure allows | H010, S058, S077, S014 (4; abstracts S043, S141, S093, S047, S354) | ✅ 1996–2004, abstracts to 2009 | ✅ [S014 p. 4]; [S058 preprint pp. 8–9]; [02 T3] | ✅ | ⚠ finite consistency is a textbook device [S014 p. 15] | Heuristic-eligible, but three of the four full texts restate one 1998 result (card note), so only two independent works: Workflow B2 step (§5.3 C) |
| Build instances on the axis the claim is about | S025, S018, S017, S204, S031, H007, S189, S211, S237, S388 (10; abstract S061) | ✅ 1999–2025 | ✅ design rationales stated [S031 p. 2; H007 pp. 13, 27; S025 p. 12] | ✅ | ✗ structural-knob generators are common computational practice | Heuristic-eligible; written into Method 4 (§5.3 D) |
| Find which bound stalls, then split the labour | S046, H007, S128, S165, S243, S238 (6; S243 and S165 one project) | ✅ 2017–2026 | ✅ the papers state the diagnosis [H007 p. 14; S165 manuscript p. 11; S243 p. 17] | ✅ | ✗ primal and dual bound analysis and matheuristic incumbents are common in MIP practice | Heuristic H11 (§5) |
| Return the ranked pool when the model's data are estimates | S058, S035, S162, S022, S070 (5; abstracts S048, S184, S174) | ✅ 2000–2021 | ✅ [S058 preprint p. 22]; [S070 manuscript p. 13] | ✅ | ✗ generate-and-test pools are standard in molecular design [S022 arXiv pp. 20, 22] | Heuristic H12 (§5) |
| Re-solve the literature's own instances to certified optimality | S025, S079, S058 (3; S006, S168, S003, S198 also show it; abstract S127) | ✅ 1996–2005 | ⚠ the reason is stated per paper only | ✅ | ✗ | Absorbed into Method 4 as its early form (§2) |

### Method 6 (proposed): Prove the problem hard, then bound the heuristic

**Four checks.**
1. *Recurrence.* Process planning (NP-hardness, then an approximation scheme whose error vanishes with probability one [S088]); capacity expansion (a heuristic proved asymptotically optimal [S138]; a multi-stage stochastic version [S029 preprint pp. 9–24]; technology selection [S118 preprint pp. 9–21]); heat-exchanger network synthesis (strong NP-hardness of every published formulation [S024 manuscript pp. 10–25], open problems [S010 preprint p. 8], five approximation algorithms with guarantees [S119 preprint pp. 6–19]); the TDTSP (heuristic bounds from both sides [S061]). Seven full texts and four abstracts; the full texts were written 2000–2004 (S118's manuscript is dated June 2000 [S118 preprint p. 1]). Later echoes: an approximation guarantee for backward stepwise elimination [S213] and a water-network approximation whose loss is bounded by the cost of compensating pumps [S238 manuscript pp. 10–14].
2. *Say–do.* Stated in his sole voice: "The distinguishing feature of this solution paradigm is the analytical derivation of bounds for the quality of the solutions obtained by heuristics that run in polynomial time." [S002 manuscript p. 18]; in a review he co-wrote: "Analytical results–as opposed to computational comparisons and case studies–are long overdue." [S010 preprint p. 8]; the 2004 paper places itself in a line of work on "introducing rigor in the use and practice of heuristics" [S119 preprint p. 2], the aim his group's page also states [02 T3]. Practised in S029, S119 and S118 (proofs, and a relaxation bound reported on every run).
3. *Executable, and different from standard practice.* The papers place themselves against the field's habit: "Although the use of heuristics has been prevalent in the process synthesis literature, their justification has been exclusively based on empirical evidence obtained through computational testing." [S119 preprint p. 1]; "The approach contrasts and complements the current practice in process systems engineering, which is entirely empirical in nature." [S138]. Steps below.
4. *Exclusivity.* Not what most global-optimization or process-systems researchers do: the 2004 paper calls its algorithms the first approximation algorithms for process synthesis [S119 preprint pp. 2–3, 22]. The probabilistic devices are standard extreme-order statistics, with one proof credited to a probabilist [S118 preprint pp. 16–17, 23], and a team member later analysed practitioners' heuristics with approximation ratios (Misener's 08, §5), but within his field and period this is his group's programme.

**Draft for SKILL.md.**
- **One line**: Before writing an algorithm for an applied combinatorial problem, prove how hard it is; if exact general-purpose algorithms are unlikely, design a polynomial-time heuristic around the one property its error bound needs, prove the bound, and report the relaxation bound on every run.
- **Steps**:
  1. Classify the complexity on the simplest restriction (one period, unit costs), then carry the hardness through every published formulation by zeroing weights and deleting the constraint blocks that become redundant [S024 manuscript pp. 10–25; S118 preprint pp. 9–11].
  2. Read hardness as a brief: exact general-purpose algorithms are unlikely, so aim at heuristics with analytical quality bounds; keep a weaker hardness proof if its source problem suggests algorithms [S024 manuscript pp. 25, 36; S002 manuscript pp. 18, 22; S010 preprint p. 8].
  3. Build the heuristic on the LP relaxation around one counting property, e.g. shifting adds at most one expansion per facility beyond the LP [S029 preprint pp. 9–16; S118 preprint pp. 12–15].
  4. Prove the guarantee: a ratio computable from the input before solving [S119 preprint p. 18], or asymptotic optimality almost surely under stated probability models [S029 preprint pp. 16–24; S118 preprint pp. 15–21]; show with a parametric family that naive rounding is unboundedly worse [S029 preprint p. 15].
  5. On every run report the gap to the relaxation bound and label it as such: "It should be noted that the gap of 10.7% is with respect to the LP relaxation value." [S029 preprint p. 26]; claim optimality only where the a posteriori ratio is 1 [S119 preprint pp. 18, 20].
  6. Use the theory to explain what the computations show, such as relaxation gaps that do not grow with the horizon [S118 preprint pp. 11–12, 20–21]; stress-test the parameter the bound depends on [S238 manuscript p. 17].
  7. When no heuristic dominates, run the suite and say so [S119 preprint pp. 21–22].
- **Applies to stage**: problem choice, algorithm design, judging results.
- **Different from standard practice**: process-systems heuristics are usually justified by computational testing; here hardness comes first and every heuristic carries a proof and a computed bound.
- **Limitations**: era-bound (main line 1995–2004 at UIUC with Liu, Ahmed and Furman; dormant in the cards from 2005 to 2020, with the echoes above); mostly MILP planning and synthesis rather than global MINLP; the guarantees are asymptotic and say little about small instances [S029 preprint p. 22; S118 preprint p. 15]; i.i.d. data models [S029 preprint pp. 16–18].
- **Say–do consistency**: ✅ stated (sole and co) + practised, for 1995–2004.
- **Cross-links**: Research Taste mark 3 (a heuristic paired with a bound); Heuristic 7; Honest Boundary (§3.2 item 1); the 2004 approximation-algorithms paper [S119] is the natural Signature Work Anatomy entry for this method.

---

## 5. New heuristics

The list grows from ten to twelve, two above the framework's band of 5–10. If the edit keeps ten, H12 can go into Workflow D as a step; H11 also supplies the source that Workflow B1 step 3 lacks and should stay.

### H11 (proposed) · Find which bound stalls, then split the labour

**One line**: before building anything for a hard application MINLP, run it through two general global solvers and read the primal and dual sides separately; if the dual side stalls, the work belongs in reduction and relaxation; if the primal side stalls, write a problem-specific method whose only job is the incumbent and leave the full model and the bound to the general solver.

**Cards**: scaled-time primal and dual convergence profiles of the solved instances [H007 pp. 14, 17]; the tail of an ablated profile read as proof versus search [S046 arXiv p. 16]; a preliminary two-solver run that names the primal side as the bottleneck [S165 manuscript p. 11; S243 p. 17]; "In all instances tested, except for the small case study, the nonlinear solver BARON failed to provide a good upper bound within 3 hours." [S238 manuscript p. 17]; decompositions that supply only incumbents, handed to SCIP [S165 manuscript pp. 13–24; S243 pp. 18, 30]; a framework for incumbents with BARON for the lower bound, the better bound of each reported [S128 arXiv pp. 19, 24]; approximations that map to feasible solutions, set against a valid lower bound [S238 manuscript pp. 10–20].

**Checks**: recurrence ✅ (four projects, 2017–2026); say–do ✅ ("To assess whether improving the primal bound or the dual bound took longer in our study, we analyzed solver convergence for the instances solved to global optimality." [H007 p. 14]; "able to improve the dual bounds consistently but have trouble obtaining primal (feasible) solutions" [S165 manuscript p. 11]); executable ✅; exclusivity ✗ (§4) → heuristic. The papers are student-first with Dey; the attribution is shared.

**Steps**: (1) run the compact model under one budget in two general solvers and record primal bound, dual bound and gap separately [S165 manuscript p. 11]; (2) on solved instances, plot scaled bound progress against scaled time, and do not use the plot to rank solvers [H007 pp. 14, 17]; (3) dual side stalls → Methods 1 and 5; (4) primal side stalls → a decomposition or restriction for the incumbent (a budgeted master with a feasibility subproblem and no-good cuts; a restriction to the peak periods; a piecewise-linear restriction) [S165 manuscript pp. 13–22; S128 arXiv pp. 13–17; S238 manuscript pp. 8–14]; (5) hand the incumbent to the general solver, report solver-alone against heuristic-then-solver at equal total time with primal, dual and gap per scenario, and the better bound of each [S165 manuscript pp. 24, 28–29; S243 p. 32; S128 arXiv p. 24].

**Stop rule**: a heuristic value is reported only beside a valid dual bound (Heuristic 7).

**Where it goes**: a new heuristic; Workflow B1 step 3 cites it (§3.2 item 15); Inner Tension 1 gains a resolution seen in practice, general solver for the bound and tailored method for the incumbent [S128 arXiv p. 24].

### H12 (proposed) · When the model's data are estimates, return the ranked pool, not one optimum

**One line**: if the coefficients come from estimation (group contributions, fitted properties), certify the optimum, then list the K best or all feasible designs and let higher-fidelity models or experiments pick.

**Cards**: "Although [33] uses an algorithm that guarantees global optimality, we still obtain several non-global solutions to the problem in order to alleviate the difficulty due to uncertainty in the thermodynamic property estimation techniques that were used." [S058 preprint p. 22]; "The capability to identify all, or the K best, solutions of an integer program was added to the general purpose BARON solver after successful implementation in the context of this molecular design problem." [S035 p. 11]; K-best by changing the fathoming step [S162 pp. 25–26; S012 manual pp. 5–6]; "This smaller pool of compounds can then be investigated using high-order models or experiments." [S022 arXiv p. 12]; the solver feature traced to molecular design [S070 manuscript p. 13]; abstracts [S048; S184; S174].

**Checks**: recurrence ✅ (2000–2021, refrigerants, molecular design, phasing, DNA assembly); say–do ✅ (quotes above); executable ✅; exclusivity ✗ (§4) → heuristic.

**Steps**: (1) solve to certified global optimality; (2) list the pool in one tree (K-best fathoming) or by integer cuts that exclude each earlier solution [S035 p. 11; S058 preprint p. 22]; (3) rank it and re-rank with higher-order models or experiments [S022 arXiv pp. 12–13, 23]; (4) report how many pass the finer screen and which are new (44 solutions, 29 admissible, nine not in earlier work [S035 pp. 12–13]); (5) say when a design space is small enough that enumeration would do [S022 arXiv p. 25].

### 5.3 Heuristic-eligible clusters written into existing steps (no new heuristic)

**A. Workflow B2 step 3, upgraded: carry the integer-programming device across.** The step exists with one stated source [02 I1]; the cards supply the practice. *Protocol*: name the IP device that solves the discrete analogue (variable disaggregation, reduced-cost fixing and probing, Lagrangian relaxation with an exact MILP subproblem, logic cuts, column generation); derive its continuous counterpart; show where it sits against the standard relaxation, e.g. the big-M relaxation is the envelope with a weaker bound plugged in [S101 pp. 1–2, 9–10, 16]; look for discreteness in disguise (a box-constrained bilinear optimum at vertices [S025 pp. 5–7]; McCormick exact when one factor is at a bound or binary [S053 pp. 5–7; S238 manuscript p. 9]; phases restricted to 0 or π [S168 p. 4; S198 pp. 2–5]) and linearize exactly. *Cards*: [S025 pp. 13–14; S006 pp. 15–16; S035 pp. 3, 10; S361 p. 1; S388 p. 1; S046 arXiv pp. 7, 9]; abstracts [S036; S054; S263].

**B. Method 5 step 0 (new) and Method 1 evidence: order before you price.** (1) Write one master object: a homogenized Lagrangian range-reduction problem [S006 pp. 12–16; S046 arXiv pp. 12–13] or a convex extension over a generating set [S028 pp. 3–14]; (2) show the literature's rules, your own earlier ones included, as special cases or dominated [S006 p. 15; S053 pp. 8, 12–13, 16, 19; S032 pp. 7–10; S003 pp. 9–10]; (3) prove the dominance order with two-way feasibility maps and settle each incomparable pair with a one-variable instance [S018 pp. 2–3, 8, 16; S025 pp. 8–10; S133 arXiv pp. 6–11; S042 preprint p. 21]; (4) only then price the non-dominated ones by time and failures [S018 pp. 17–19, 27; S053 pp. 21–25]; (5) read the new rule off the master [S006 pp. 17–19].

**C. Workflow B2, new step: branch so the tree is finite where the structure allows.** (1) Ask whether the value function is piecewise constant or the optimum sits at finitely many candidate points; (2) change variables so the discontinuities are axis-parallel: "Since the discontinuities are, in general, not orthogonal to the variable axes, there would always be some rectangular cell that contains a discontinuity in the interior." [S014 p. 6], hence tender variables [S014 pp. 6–10]; (3) branch at the incumbent when it lies in the node and at breakpoints, and bisect periodically for exhaustiveness [S058 preprint p. 9; S077 p. 24; S162 pp. 24–25]; (4) prove finiteness by finite consistency [S014 p. 15]; (5) compare with convergent schemes on the rivals' own sets [S014 pp. 18–22]. Stated: "The issue of finiteness is not only of theoretical significance – our computational experiments using standard test problems indicate faster convergence of the proposed algorithm in comparison to existing strategies in the literature." [S014 p. 4]; finite termination is also among the results he lists as his own [02 T3]. Era: 1996–2004 in full texts, abstracts to 2009 [S047; S354].

**D. Method 4, new step: build the instances the claim needs.** When the public library is easy for your solver or lacks the structure, build instances along the axis the claim is about, with ground truth known by construction or certified, and publish them: hand-built instances on the contribution's axis after finding that "all pooling problems currently in the open literature are easy problems" for the authors' solver [S025 pp. 10, 12–13]; factorial structural knobs [S018 p. 17]; closed-form physical families [S017 pp. 8–10]; controlled tightness by binary search on sampled feasible points [S189 arXiv pp. 20–21]; instances generated from a known tree decomposition [S388 p. 1]; inherited sets kept intact and extended with the same generator [S237 pp. 1–3]; instance ranges chosen so that solving them settles open questions [H007 pp. 1, 13, 16, 27; S204 pp. 1–2]; written admission rules: "Thanks to these extensive preliminary tests, we discarded all instances that are solved by at least 30% of the complete solvers within a time limit of 30 seconds." [S031 p. 15]; instances stored as contributed, never reformulated [S031 p. 8]; a library distilled into representative forms with provenance [S211 arXiv pp. 11–13]; black-box sets with certified optima built from an algebraic library [S063 p. 13].

---

## 6. Candidate pool (not promoted)

Entries are new-pattern-candidate entries in the digests (187 in all; every entry is assigned to exactly one row); works count each work once; *full* counts works read in full or in part; a plus sign names works that support the cluster in card prose without a candidate entry.

| Cluster (merged by meaning) | Entries | Works (full) | Decision |
|---|---|---|---|
| Heuristics with proven guarantees; complexity first | 10 | 8 (5) + S118, S238 | Promoted, Method 6 |
| Transfer IP devices; linearize through discreteness | 12 | 11 (8) | Workflow B2 step 3 (§5.3 A) |
| One framework re-derives the zoo; dominance lattice; where the cheap relaxation sits | 8 | 8 (8) | Method 5 step 0 (§5.3 B) |
| Taxonomy-first review with one unifying lens | 5 | 4 (4) | Writing move (§7.4 WM5) |
| Price of local search on the literature's own instances | 4 | 4 (3) | Method 4 early form (§2) |
| Finite branching by exhaustiveness and incumbent branching | 9 | 9 (4) | Workflow B2 step (§5.3 C) |
| Instance generators, ground-truth families, admission rules, open-problem libraries | 12 | 11 (10) | Method 4 step (§5.3 D) |
| Decompose for the incumbent, general solver bounds; primal-vs-dual diagnosis | 5 | 5 (5) + S238 | H11 |
| Ranked near-global list; screen-and-refine pool; enumerate alternatives | 5 | 5 (2) + S035, S162, S070 | H12 |
| Modeling channel for knowledge the solver cannot infer; relaxation-only constraints | 5 | 4 (3) | Heuristic 2 evidence (§2.6) |
| Per-component time accounting; profile first | 3 | 3 (3) | Method 2 and Method 5 step 1 evidence; rejected as a heuristic (§10) |
| Version, build and paper to cite in every log | 2 | 2 (2) | Heuristic 6 evidence |
| Self-deciding defaults; parameter-free activation; learn the off-switch | 3 | 3 (2) | Method 1 step 4 and Taste mark 2 evidence |
| Surrogate picks the configuration, rigorous simulation verifies; per-unit surrogates | 3 | 3 (3) + H006 | Method 3 evidence |
| A gain counts net of its cost (tuning, path, deployment) | 3 | 3 (3) + S206, S284 | Method 5 variant |
| Benchmark lineage: sequel, longitudinal rerun, count-based motivation | 4 | 4 (4) | Method 4 and Method 2 step 6 evidence; writing move WM7 |
| Any-solver envelope in profiles | 2 | 2 (2) | Method 4 step 6 evidence |
| Audit the measurement; explain rankings by test-set composition; questions first | 4 | 2 (2) | Method 4 evidence; WM6 |
| Library statistics justify the special class | 2 | 2 (1) + S211 | Heuristic 1 variant |
| Re-derive cheap relaxations per node; reformulate at every node | 3 | 2 (2) | Method 1 step 3 and Method 5 evidence |
| Exact inner subproblem, DFO outer master over a low-dimensional interface | 4 | 4 (1) + H013 | Method 3 variant |
| Recast a neighbouring field's models as global problems | 6 | 6 (1) + S079, S168, S198 | Heuristic 10 evidence |
| Stability as an algebraic constraint, solved globally | 3 | 3 (0) + S204 | Pool (abstract level) |
| Attack the natural formulation; instances as contributed | 4 | 4 (1) | Pool |
| Empirical regularity turned into an exact reduction or a theorem | 2 | 2 (2) | Pool (two works) |
| Add, don't replace: combine non-dominating relaxations | 2 | 2 (2) | Pool |
| Generating-set recipe for envelopes | 2 | 2 (2) | Proof device (§7.1 PD3) |
| Failure case of the standard decomposition, explained before the fix | 2 | 2 (0) | Pool (abstracts) |
| Infeasibility diagnosis as a solver service | 2 | 2 (0) | Pool (abstracts) |
| Mine the engineering record for patterns | 3 | 3 (0) | Pool (abstracts) |
| Theory-set hyperparameters instead of cross validation | 1 | 1 (1) + S017 | Pool |
| Peak-period restriction | 2 | 2 (2), one project | Pool |
| Count effects in classes, losses included | 1 | 1 (1) + S090, S239, S161 | Workflow D step 2 evidence (§7.3 EP3) |
| In-silico rehearsal of a self-driving-lab campaign | 1 | 1 (1) + S273 | Pool (one project) |
| Singletons: S094; S010 (open problems as own agenda); S002 (students as scouts); S014 (machine-independent counts); S003 (lift, then linearize); S198 (global optimum as a test of the scientific model); S353; S015 (identical output as acceptance test); S080 (simplest baseline); S052; S022 (enumeration as baseline); S249 (published algorithm, proprietary engine); S038 (rival wins relayed); S084 (own solver as a black box); S104 (logic cuts); S130; S214; S181; S182 (cross-protocol transplant); S063 (show the search before the score); S108 ×2; S133 ×2; S179 ×2; S208; S128; S388; S170 ×2; S189; S190 ×2; S205 ×2; S206 ×2; S207; S211; H009 ×2; S238 ×3; S239 ×2; S271 | 48 | 37 | Pool; several feed §7. S249's moat (Inner Tension 4) and S038 (Inner Tension 1) are one-line evidence |

---

## 7. Technique inventory

### 7.1 Proof devices

- **PD1 Value-function argument and one dual master for range reduction**: a multiplier gives a supporting hyperplane of the perturbation function whose intersection with the incumbent level bounds the variable [S077 pp. 12, 15; S058 preprint pp. 6–7; S162 pp. 12–14]; a homogenizing multiplier makes one procedure yield every rule, with cuts reusable across nodes [S006 pp. 12–16; S046 arXiv pp. 12–13].
- **PD2 Exactness through discreteness**: vertex attainment, binarization on bounds and McCormick exact for binary factors [S025 pp. 6–7; S053 pp. 5–6; S168 p. 4].
- **PD3 Envelope constructions**: generating sets and convex extensions [S028 pp. 2–14]; the disjunctive hull of two faces with a perspective substitution [S032 pp. 6–7]; the envelope as the hull of two faces [S101 p. 10]; Rikun-type separability [S025 p. 8; S032 pp. 19–20; S044 pp. 4–6]; the conjugate characterization of composite envelopes [S003 pp. 12–14]; a four-region envelope proved region by region [S190 pp. 12–13].
- **PD4 Dominance and equivalence**: two-way feasibility maps [S018 pp. 6, 8, 16]; special-case reductions (an older rule as the new construction with a weaker bound) [S101 p. 16; S006 p. 15; S053 pp. 8, 19]; sandwich results [S133 arXiv pp. 6–7]; chain-rule containment [S003 pp. 3–4]; strictness by one small instance [S025 p. 10; S018 p. 3; S028 p. 5; S042 preprint p. 21].
- **PD5 Complexity by restriction, carried across a literature**: 3-PARTITION through a bipartite match graph [S024 manuscript pp. 10–12]; zeroed weights and redundant blocks [S024 manuscript pp. 14–25]; subset sum [S101 p. 6]; capacitated lot sizing [S118 preprint pp. 9–11]; 3-dimensional matching [S090 preprint pp. 8–11].
- **PD6 Probabilistic analysis of heuristics**: one counting lemma, extreme order statistics and a dual-feasible solution for the linear lower bound [S029 preprint pp. 14–24; S118 preprint pp. 14–21]; a guarantee for any heuristic from two input-computable bounds [S119 preprint p. 18].
- **PD7 Finiteness**: half-open boxes and finite consistency [S014 pp. 8–15]; a finite search space [S168 p. 5]; periodic bisection plus incumbent branching [S058 preprint pp. 8–9; S077 p. 24].
- **PD8 Smallest decisive counterexamples**: propagation that reduces nothing against the full bound LP [S046 arXiv pp. 7–9]; a non-attained separation infimum [S133 arXiv p. 14]; a folklore target refuted [S119 preprint p. 17]; chemically infeasible combinations that pass older constraints [S035 pp. 7–9]; the pathological case for cheap bound tightening [S077 pp. 18–19; S162 pp. 16–18].
- **PD9 Equivalence chains to a tractable object**: an IP reduced to a linear system over F2 [S198 pp. 3–4]; a convex program whose optimality conditions are the network equations [S128 arXiv pp. 10–13; S165 manuscript p. 14]; a semi-infinite certification by one global maximization [S039 manuscript pp. 4–5, 8; S017 p. 8].
- **PD10 Duality and dynamic programming over tree decompositions**: duals by leaf-to-root recursion, primals by root-to-leaf choice, total dual integrality as a by-product [H009 pp. 5, 10–15]; column generation with DP pricing [S388 p. 1].
- **PD11 Convergence by a checkable design rule or monotone updates**: a positive basis with a cosine-measure floor at every unsuccessful iteration [S170 pp. 12, 16–22]; never-increase LP updates that keep one convergence proof [S189 arXiv pp. 5–14; S211 arXiv pp. 6–10]; a tangent count for a projective tolerance [S006 pp. 9–11].
- **PD12 Constructive maps between approximation and exact model, priced in a device**: [S238 manuscript pp. 10–14].
- **PD13 Domain bounds from the incumbent and from symmetry**: diameter bounds proved against the putative optimum [S190 pp. 4–9]; orbit counts and fundamental-domain inequalities [H007 pp. 19–20, 26].

### 7.2 Design moves

- **DM1 Exact once at the root, cheap at every node** [S162 pp. 16–18; S077 pp. 18–19; S133 arXiv pp. 18–19; S090 preprint pp. 16–17].
- **DM2 Reduce and re-relax with pass caps and an improvement threshold** [S012 manual pp. 9–10; S077 pp. 21, 50].
- **DM3 Lift, then linearize; one auxiliary variable per distinct subexpression** [S003 pp. 3–7; S006 pp. 4–7].
- **DM4 Cuts only when violated, kept local, reused in probing** [S003 p. 15].
- **DM5 A channel for knowledge the solver cannot infer** (relaxation-only and convex declarations, solver-only bounds) [S069 preprint p. 9; S003 pp. 14–15; S012 manual p. 12; S095 p. 6; S044 p. 16].
- **DM6 A core with user exits for every search component** [S077 pp. 55–61; S053 p. 21].
- **DM7 Time per component in every log; profile before accelerating** [S077 pp. 51, 65–66; S012 manual p. 3; S159 v15.2 pp. 9–11; S069 preprint pp. 20–21; S015 pp. 2–3, 6].
- **DM8 An automatic default plus an explicit off value per component** [S191 pp. 24–26; S112 v17.4.1 pp. 23–24].
- **DM9 A new component behind an applicability gate with fallback** [S161 manuscript p. 3; S179 arXiv p. 27].
- **DM10 Per-node switching between relaxation classes by observed bound difference** [S116 arXiv pp. 22–23; S133 arXiv pp. 21–22].
- **DM11 Search in linking variables so discontinuities become axis-parallel** [S014 pp. 6–10].
- **DM12 K-best or all solutions in one tree** [S035 p. 11; S162 pp. 25–26].
- **DM13 Constrain the model's output, not its coefficients, and certify by global maximization of the violation** [S039 manuscript pp. 4, 7–9; S017 p. 8].
- **DM14 Turn the incumbent into a valid constraint or a cutoff** [S069 preprint p. 5; H007 p. 23; S108 manuscript p. 14; S271 p. 10].
- **DM15 Implement equivalent encodings and keep the fastest** [S128 arXiv pp. 16–17; S206 manuscript p. 15].
- **DM16 Exact inner subproblem, low-dimensional DFO master** [S160 pp. 3–4].
- **DM17 Restrict a DFO solver to settings a lab can dial; feed back the median of replicates** [S205 p. 4].

### 7.3 Experiment and evaluation protocols

- **EP1 Ablate inside production code, print the exact option lists, admit only competitors with the same switch** [S046 arXiv pp. 15–16, 21; S003 pp. 17–23; S090 preprint pp. 22–27].
- **EP2 Read profile tails and bound progress**: a catching-up ablated variant means the component serves the proof [S046 arXiv p. 16]; scaled-time primal and dual profiles [H007 pp. 14, 17].
- **EP3 Count effects in classes, losses included**: effect classes per metric [S003 pp. 22–23]; factor bands [S090 preprint p. 22]; win, tie and loss with thresholds [S239 pp. 26–27]; per-instance ratios that keep the slowdown [S161 manuscript pp. 6–7]; the full factorial including the cells that got worse [S190 p. 16].
- **EP4 Ground truth certified or constructed**: certified optima for black-box tests [S001 p. 21; S063 p. 13; S273 pp. 10–14]; complete enumeration of small spaces [S074 arXiv pp. 10–11; S134 manuscript p. 12]; closed-form families [S017 pp. 8–10]; known supports [S182 arXiv pp. 3, 7–9]; exact optima and a perfect-information oracle [S034 arXiv pp. 7, 10, 17–18].
- **EP5 A mixed-tolerance success test on the median of ten shared starts** [S001 p. 21; S063 p. 13; S270 p. 8; S272 p. 8].
- **EP6 An unseen set after developer rounds** [S001 p. 41].
- **EP7 A minimal covering portfolio and a virtual-best envelope** [S001 pp. 30–33; S063 p. 20; S270 pp. 14–16; S272 pp. 14–16; S239 pp. 27–31].
- **EP8 Budgets and costs tied to use**: a budget tied to a named application [S001 pp. 20, 22]; tuning hours against seconds saved [S084 preprint pp. 9, 15–17]; the tuning path priced [S182 arXiv pp. 6–7].
- **EP9 Longitudinal reruns**: solvers tagged same, updated or new [S272 pp. 4–5, 8–9; S270 p. 5]; old gains re-tested on new versions [S190 p. 15].
- **EP10 Test inside a closed solver through its channels** [S044 p. 16; S109 pp. 31–32; S239 p. 21].
- **EP11 Replicates for order-sensitive choices** [S239 pp. 17–18; S269 arXiv pp. 11–12].
- **EP12 Stress tests from the bound or the case**: the parameter in the error bound multiplied [S238 manuscript p. 17]; stress-factor families from one case study [S165 manuscript pp. 23–24; S128 arXiv p. 16].
- **EP13 Validate a surrogate pipeline once against brute force, and judge surrogates by their optimum**: [S052 manuscript pp. 22–24]; [S103 pp. 9–13]; [S206 manuscript p. 16; S271 pp. 13, 16].
- **EP14 Rehearse a lab campaign in silico, counting evaluations as experiments** [S272 p. 17; S273 pp. 24–28].
- **EP15 Show the search before the score** [S063 pp. 11–12; S001 pp. 18–19].

### 7.4 Writing moves

- **WM1 Concede, then sharpen**: the abstract grants that a result "may not be surprising", then stresses the strong sense and the simple hard cases [S024 manuscript p. 1].
- **WM2 Numbered remarks give the structural reasons the obvious approach fails, and each is answered by a component** [S006 pp. 3–4].
- **WM3 The smallest computed example for every claim** [S002 manuscript pp. 19–21; S003 pp. 4–6; S018 p. 3; S046 arXiv pp. 7–9].
- **WM4 Criticism by subsumption or classification, not attack** [S024 manuscript pp. 2–3, 27; S006 pp. 2, 15–16; S003 pp. 9–10].
- **WM5 Reviews**: one lens or taxonomy (every DFO iteration as choosing the next points; SDP relaxations as Lagrangian relaxations; a 2×2 of model and uncertainty) [S001 pp. 11–13; S018 p. 8; S007 arXiv p. 5]; algorithms rated by guarantee and implementation status [S002 manuscript pp. 5–6]; a coverage rule stated at the start [S010 preprint p. 2]; numbered open problems at the end [S010 preprint p. 8; S002 manuscript pp. 21–22; S070 manuscript p. 8; H007 pp. 25–27].
- **WM6 Questions first**: a benchmark paper organized by the users' questions, answered by section and again in the conclusion [S001 pp. 2, 41; S063 p. 2].
- **WM7 Motivate a benchmark with a dated count** [S001 pp. 2, 13; S063 p. 9; S270 p. 3; S272 p. 3; S273 p. 9].
- **WM8 Calibrated claims**: hedging in both directions [S002 manuscript pp. 19, 22]; claims labelled as proved, observed on one example or conjectured [S025 p. 16]; conjectures stated with the observation behind them [S042 preprint pp. 21–22].
- **WM9 Credit a speed-up to the list of developments that produced it** [S035 p. 12].
- **WM10 Manuals put the contract first**: model requirements and bounds before options, and every termination status paired with what it certifies and what the user does next [S012 manual pp. 1–5; S112 v17.4.1 pp. 12–14; S191 pp. 12–13].
- **WM11 A tutorial run on a deliberately weak relaxation, one device switched on at a time** [S077 pp. 26, 30–31; S162 pp. 26–33].
- **WM12 End each application paragraph with the largest instance ever certified and the method that certified it** [H007 pp. 5, 9, 10, 12].
- **WM13 A neutral lesson from the reading notes** (no work named): before release, read the abstract and the conclusion against the tables they summarize.

---

## 8. Trajectory as seen in the full texts

Topic counts are carded works per period (non-skip; any read level), classified by this note from titles and cards; *full* is the number read in full or in part.

| Period | Carded works (full) | Main topics in the cards | Full-text anchors |
|---|---|---|---|
| 1987–1995 | 20 (0) | Planning, scheduling and capacity expansion (13, eleven of them with Grossmann); GBD convergence; the first global papers | Abstracts and metadata only [S023; S036; S008; S013] |
| 1996–2000 | 25 (6) | Global optimization and BARON (8), planning under uncertainty and the heuristics line (6), robust control (3) | [H010; S025; S079; S058; S077] |
| 2001–2005 | 39 (22) | Convexification and relaxations (9), BARON manuals (7), complexity and approximation (5), stochastic programming (3), crystallography (3) | [S032; S028; S053; S101; S006; S003; S024; S010; S029; S119; S014; S002; S069; S168; S198; S035] |
| 2006–2010 | 28 (7) | Crystallography, proteins and drug delivery (12), global algorithms (3), relaxations (2) | [S161; S361; S044; S204; S254; S218; S118] |
| 2011–2015 | 40 (14) | Surrogates and CCSI (14), relaxations (9), LP and GPU linear algebra (3), molecular design (3) | [S217; S173; S347; S052; S039; S018; S109; S001; S015] |
| 2016–2020 | 59 (29) | ALAMO, ML and RL (15), editorial service (8), DFO and tuning (6), relaxations (6), global algorithms (6), planning (5), molecular design (5) | [S017; S104; S046; S084; S031; S022; S007; S182; S090; S159; S112; S191] |
| 2021–2026 | 58 (36) | Surrogates and symbolic regression (13), DFO benchmarks (8), relaxations (6), molecular and materials design (5), networks with Dey (4), Euclidean-norm problems (4), ML inside solvers (3), self-driving labs (3) | [S116; S133; S128; S165; S238; H007; S190; S284; S212; S269; S170; S205; S206; S239; S272; H009] |

**Turns visible in the full texts.**
- *The heuristics line* runs in full texts from a 2000 manuscript to 2004 [S118 preprint p. 1; S119 preprint p. 1] and then goes quiet, with echoes in 2021 [S213] and 2026 [S238 manuscript pp. 10–14] (Method 6).
- *Convexification feeds the engine*: the theory papers of 2001–2002 [S032; S028; S053; S101] become BARON's 2004–2005 relaxation machinery [S006 pp. 4–7; S003 pp. 15–23].
- *The move to CMU (2007)* adds sponsor-driven surrogate work [S217; S347; S173] and benchmark-first DFO [S001]; the crystallography and protein line thins out (12 carded works in 2006–10, 3 in 2011–15, none later).
- *Georgia Tech (from 2021)* adds co-supervised theory and applications with ISyE colleagues [S128; S165; S238; S388; H009; S284; S269], with method development moving outside BARON (§2, Method 2), and a return to large DFO benchmarks around BAM [S270; S272; S273; S277].
- *The relaxation stance moves with subsolver technology* (§3.2 item 10).

**What stayed constant.** Certified global optima as the yardstick, from 1999 [S025 pp. 14–15] to 2026 [S272 p. 8]; duality-based reduction, from 2000 [S077 pp. 12, 15] to 2025 [S190 pp. 4–9; H007 pp. 18–25]; BARON as the instrument, from the 2000 manual [S077 pp. 7–9] to a 2026 presolve [S239 p. 32]; LP-first relaxations with cheaper emulations of strong ones, from 2005 [S003 p. 1] to 2022 [S133 arXiv p. 1]; small algebraic models, from 2013 [S052 manuscript p. 10] to learned branching in 2026 [S269 arXiv pp. 9–10].

**Against note 06.** The full texts agree that turns follow institutional moves (UIUC → CMU → Georgia Tech), and they date the end of the heuristics line more precisely: last manuscripts 2000–2004, not only a gap after 2004 [06 §4.2].

---

## 9. Collaboration pattern

Counts are carded works (non-skip, any read level) with the coauthor named on the card.

| Period | Most frequent coauthors (carded works) | Pattern seen in the full texts |
|---|---|---|
| 1987–1995 | Grossmann 12 (all but two in 1991–92) | PhD-era planning MILP/MINLP with his adviser; first global papers with Ryoo [S008] |
| 1996–2000 | M. L. Liu 5, Shectman 3, Ahmed 3, VanAntwerp and Braatz 3, Vander Wiel 2, Tawarmalani 2 | Two-author papers, student first and he last; a robust-control collaboration with a colleague's group in the same department [S079 p. 1]; the manual is his alone and credits 17 students [S077 pp. 8–9] |
| 2001–2005 | Tawarmalani 18 of 39, Ahmed 6, Furman 4, Vaia 3 | The convexification years with one former student, then at Purdue; the complexity and approximation papers with Furman and Ahmed [S024; S010; S119; S029] |
| 2006–2010 | W. Xie 6, A. B. Smith 4, Chang 2, Bao 2, Elble 2 | Students on crystallography, proteins and GPU computing; a phasing module released inside another group's program, SnB [S161 manuscript pp. 1, 3, 7–8] |
| 2011–2015 | D. C. Miller (NETL) 9, Cozad 4, Khajavirad 4, Yan Zhang 3, Chang 3, Zorn 3 | Consortium papers in which he is one of many authors [S217 p. 3; S347 p. 3] beside two-author student papers [S052; S039] |
| 2016–2020 | Puranik 5, Ploskas 5, Wassick (Dow) 5, Grossmann 5, Agarwal 5, Austin 4, Trahan (Dow) 4, Kılınç 4 | Dow-sponsored projects with company engineers as co-authors [S007 arXiv p. 1; S022 arXiv p. 1; S183 p. 1]; CMU students and postdocs; editor-in-chief notices [H011; S306; S318; S304] |
| 2021–2026 | Dey 7, D. Oh 7, Kuznetsov 5, K. Ma 5, Rajagopalan (Dow) 5, Y. Zhang (TOF) 4, Raghunathan (MERL) 4, Fardis 4 | Students co-supervised with Dey (Li, Choudhary; per note 04) [S128 arXiv p. 1; S238 manuscript p. 1]; papers with Nemhauser and Bayramoglu [S284 p. 1; S269 arXiv p. 1] and with Gounaris, who is corresponding author [S189 arXiv p. 1]; BARON work with TOF staff [S239 p. 1]; NETL and DOE programmes [S165 manuscript p. 30; S206 manuscript p. 1] |

**Across the career.** Tawarmalani is the most frequent coauthor (25 coauthored works, 1999–2015), then Grossmann (19, 1989–2020), D. C. Miller (12, 2011–2018), Ahmed (12, 1998–2019), Ploskas (8, 2018–2026) and Raghunathan (7, 2018–2025). Sole-authored items are manuals, the 2004 review, a 1996 book review, editorials and prize notices [S077; S159; S112; S191; S002; H010; S038; S306].

**Partners.** Dow (2015–2025), DOE/NETL (2011–2026), MERL (2018–2025) and TOF (2020–2026) supply problems, co-authors and funding [S007 arXiv p. 1; S183 p. 8; S165 manuscript pp. 1, 30; S074 arXiv p. 1; S239 p. 1]. Students carry topics to him as well as from him: in the acknowledgments of the 2003–04 review, his former students Liu and Ahmed "introduced me to many of the topics discussed in this paper" [S002 manuscript p. 22] (the FOCAPO version has the same sentence); black-box applications were MS theses [S001 pp. 41–47].

**Editorial practice, one instance.** As guest editor, his co-authored submission to the special issue was handled by a co-editor, and he saw nothing of its review [S208 p. 5] (§10 item 6).

---

## 10. Rejected updates

1. **A heuristic for per-component time accounting** (S077, S012, S015, S097, S159, S069): no explanatory power beyond Method 2's instrumented code and Method 5 step 1; profiling is generic.
2. **A heuristic for *version, build and paper to cite in every log*** (S112, S249, S159, S012): already Heuristic 6; added as evidence.
3. **Core-method status for the IP-transfer, unify-and-order, instance-design and finite-branching clusters**: each fails exclusivity, and the last also rests on one result (§4); written into existing steps instead.
4. **A seventh method for *a gain counts net of its cost***: it is Method 5's yardstick applied to tuning, learned components and surrogates; one sentence in Method 5 carries it.
5. ***Taxonomy-first review* and *count-based motivation* as methods**: writing moves (WM5, WM7), with no bearing on how he does the research.
6. ***Students as scouts* and the editor recusal as heuristics**: one own-voice instance each [S002 manuscript p. 22; S208 p. 5]; at most one line of evidence in Workflow F and in *Stages without a distillable Sahinidis method*.
7. **Deleting or narrowing Method 3 because of S086, S181, S183**: weak voice and inside Method 3's own scope clause (§3.1).
8. **Changing Method 5 because of S189**: co-authored, another faculty member corresponding, a root-bound comparison only.
9. ***Deploy a learned policy with a drift alarm*** [S181 pp. 4–5] and ***ordinal-constraint LP for expert weights*** [S130 preprint pp. 15–17]: single application papers, industry or application voice.
10. **Carrying the cards' reading notes on inconsistencies inside works** (prose stronger than tables, count slips, typos) into SKILL.md: barred by the house rule; one neutral lesson kept (WM13).
11. **Replacing the SKILL.md quote of Inner Tension 1 by the journal wording**: both wordings are his; only the follow-up sentence needs a version (§3.2 item 9).

---

## 11. Open gaps

- **The founding texts are still abstracts**: Ryoo & Sahinidis 1995 [S008] and 1996 [S013] and the 1996 BARON note [S004]. Branch-and-reduce's origin rests on the 2000 manual, the 2000 applications paper and the 2004 restatement [S077 pp. 7–21; S058 preprint pp. 4–9; S006 pp. 11–17].
- **The 2018 turn of Inner Tension 2** rests on abstracts [S030; S027]; per-node switching is read only in its 2021–22 forms [S116; S133].
- **ALAMO's founding paper** (2014) [S009] and the 2018 symbolic-regression MINLP [S055] are abstracts; the method is read in its 2015 and 2017 forms [S039; S017].
- **BARON's current algorithm paper** [S083] and the 2025 combined presolve [S241] are abstracts; domain-reduction work of 2017–2020 [S114; S124; S131] and Khajavirad's envelope papers [S067; S060; S059] are abstracts.
- **The group's own DFO algorithms** (Branch-and-Model, HybridTuner, decomposition) are abstracts [S121; S221; S222; S180]; only the local solver is read [S170]. BAM has talk slides and no paper [S270; S272; S273; S277], so the Method 4 step-7 finding for BAM rests on slides.
- **1987–1995 has no full text**, and 2006–2010 only seven (the bioinformatics and drug-delivery lines are abstracts: [S068; S126; S071; S073]).
- **The 2002 book** is an abstract-level card [S005]; its preface is known through note 02 [02 I1].
- **Who did what** in co-authored work remains unknown; at Georgia Tech the papers are student-first with co-advisers, and the cards cannot separate his share.
- **Code**: BARON and BAM are closed; claims about internals rest on manuals and papers, with no code to inspect [S112 v17.4.1 p. 1; S239 p. 32].
- **Hold-outs after 2013**: only one paper discloses tuning on its evaluation set [S239 p. 16]; the others say nothing either way.
- **The 111 Role = skip rows** (talks, committee lists, forewords, works not by him) are not evidence; their content is not read.

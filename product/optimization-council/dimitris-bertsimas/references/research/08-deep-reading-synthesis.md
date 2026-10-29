# Dimitris Bertsimas · Deep-reading synthesis

> Date: 2026-10-29 (stage T3.6, first synthesis round for this member). Input: every card in `cards/` (99 batch files, 611 card entries for 592 works, rounds 1–4; index in `07-paper-cards.md`, regenerated today by `scripts/build_card_index.py`). Rules applied: `references/paper-reading-card.md` §3 (conservative update: append only, existing methods get evidence first, a new core method needs ≥3 distinct works plus the four checks, reject updates without explanatory power, every line traceable to a card) and `references/research-extraction-framework.md` §3 (four-way validation) and §11 (quality checklist). This note proposes changes; it does not edit `SKILL.md`.
>
> Gate: `verify_card_quotes.py` reported 1,083 quotes, 1,080 exact, 3 matching after spacing/symbol normalisation, 0 NOT FOUND. `mark_read_from_cards.py` then set the INDEX Read column: 413 carded, 59 skimmed, 63 abstract, 57 metadata, 159 not read.
>
> Citation form: `[S012 p. 9]` = card S012, file page (`[[page N]]`) as recorded on the card. Abstract- and metadata-level cards are cited by ID only. This note paraphrases; the verbatim sentences are in the cards' verified `quotes` fields.
>
> Counting rules used throughout:
> 1. **One card per work.** 19 works have two cards: 18 were carded from the abstract in round 3 and read in full or in part in round 4 (S241, S275, S452, S487, S597, S636, S725, S745, S819, S836, S867, S872, S873, S905, S906, S907, S909, H001), and S181 was read in part in round 1 and in full in round 2. The deeper card is used.
> 2. **Version pairs count once** (first ID is the one counted): S390 = S524 (npj Digit Med 2026 / arXiv 2507.00205); S561 = S412 (journal paper / shorter nonarchival version); S185 = S580 (Queueing Systems 1995 survey / the earlier and partly different 1994 working paper, still cited for its own sentences); S223 = S906 (IJOO 2023 / later manuscript). S926 is the LIDS-report version of S024 [S926]. *Fix round* (after the T3.6 reviews): four more pairs that the cards themselves identify are merged in the method, heuristic, cluster and evidence-work counts below (the period, domain and coauthor tables of §1, §8.1 and §9 still count them separately, at most two works per period): S016 = S261 (OR 1991 / the 1989 working paper), S032 = S597 (OR 1993 / the 1990 working paper), S340 = S197 (arXiv 2014 / journal version), S328 = S914 (IJOC 2013 / an undated working paper with the same authors and a close title; probable). The second IDs are still cited for their own pages.
> 3. **Not his work**: S771 (a 2010 workshop page) is never cited as his.
> 4. **External evaluations, not his method**: in S063, S110, S021, S157 and S294 he is only a member of a forecasting consortium or hub team [S110 pp. 2–3, 17; S021 pp. 10–11; S157 pp. 21–22]. They are used only as outside scoring of his group's DELPHI model.
> 5. **Reading notes are not findings.** Cards that record typos, tables that disagree with a text, or recomputed numbers are not used here as criticism of anyone.
> 6. **"Stated"** means stated in a text he signed; most texts are co-authored, and sole-author texts are marked where it matters.

---

## 1. Coverage

| Item | Count | Source |
|---|---|---|
| Google Scholar rows / distinct works indexed | 932 / 751 | `07-paper-cards.md`, Coverage (team_status row) |
| Open full text found | 473 | same |
| Card entries / works with a card | 611 / 592 | `cards/*.digest.json` |
| **Read in full** | **413 works** | read_level `full` |
| Read in part | 59 works (60 cards) | read_level `partial` |
| Abstract only | 63 works (81 cards; 18 later superseded by a full card) | read_level `abstract` |
| Metadata only | 57 works (team_status shows 56: S771, not his, is counted there as skipped) | read_level `metadata` |
| Skipped rows (students' theses, reports, not his) | 160 | team_status |
| Quotes verified | 1,083 | gate |
| **Works used as method evidence** | **459** (full or partial, version pairs merged, hub papers excluded; 463 before the fix round merged four more pairs) | this note |

Batches: 51 core files (c01–c42, c2-01–c2-09; 174 cards), 42 supplement files (s01–s21, s2-01–s2-18, s4-01–s4-03; 298 cards), the 1988 PhD thesis read chapter by chapter (b2-01, S048), and five abstract/metadata files (a3-01–a3-05; 138 cards).

Full-text reading by period (works read in full or in part / all works with a card, version-merged):

| 1988–92 | 1993–97 | 1998–2002 | 2003–07 | 2008–12 | 2013–17 | 2018–22 | 2023–26 | undated |
|---|---|---|---|---|---|---|---|---|
| 23/33 | 34/47 | 34/46 | 36/50 | 36/47 | 55/60 | 128/156 | 116/137 | 1/6 |

The 1988–2000 SD, IO, CP and LO work, which the web-built skill knew mostly from abstracts, is now read in depth: the 1988 thesis [S048 pp. 11–13], a priori optimization [S038 pp. 1–2; S017 pp. 1–3; S148 pp. 1–2], dynamic vehicle routing [S016 p. 3; S032 pp. 3–15; S091 p. 3], the achievable-region and conservation-law programme [S185 pp. 1–3; S580 p. 10; S057 pp. 1, 3; S072 p. 2], moment bounds [S007 p. 35; S018 p. 1], randomized rounding [S121 pp. 3–9; S658 pp. 18–20; S435 pp. 3–6] and the Lagrangean-dual speed-up [S269 pp. 3–4].

Versions actually read where they differ from the listed venue (from the card headers): S010 is arXiv v1 (with the 200-billion figure) [S010 pp. 1, 8]; S089 the 1991 MIT preprint [S089 p. 1]; S013 arXiv v2 [S013 p. 1]; S039, S042, S085 and S003 arXiv versions [S039 p. 3; S042 p. 3; S085 p. 9; S003 p. 37]; S044, S077 and S098 preprints [S044 pp. 24–25; S077 p. 4; S098 p. 2]; S161 a technical report [S161 TR pp. 1–5]; S186 and S448 working papers [S186 p. 2; S448 pp. 5, 24]; S008 arXiv v4 [S008]; S617 arXiv 2305.15629v1 of 2023, cited as [S617 arXiv pp. …] (the 2026 article was not read); S669 arXiv 2405.07068v1 [S669]. Journal-version changes of these works are not read. Many other cards also read a preprint, working-paper or arXiv file; each card header names its version.

---

## 2. Evidence per existing method

Counts are distinct works read in full or in part (version pairs merged, hub papers excluded) whose card `method_links` name the method; a work can carry more than one relation. Abstract-level links in brackets.

| Method | Evidence | Variant | Contradiction | Any link | Say–do after the full texts |
|---|---|---|---|---|---|
| M1 Formulation first, kept in the solver class | 210 (+14) | 141 (+5) | 5 | 346 | ✅ stated (sole-author texts 1994–1995; the 1988 thesis is a variant) and practised 1988–2026; four variant families and a narrowed scope (§3 rows 1, 6–8) |
| M2 Quantified "why now" | 10 | 86 (+1) | 2 | 94 | ✅ for steps 1, 2, 4–6; ⚠ step 3 is the skill's rule, not his practice (§3 rows 9–10) |
| M3 The price of X | 46 (+3) | 168 (+1) | 0 | 205 | ✅; one-knob practice from 1990, a knob-free precursor in 1988, knobs set from data from 2006 (§3 rows 11–14) |
| M4 Warm start, exact solve, certificate, duel | 54 (+2) | 226 (+4) | 24 | 287 | ✅ protocol in his MIO methods papers; ⚠ certificate (Tension T1 older and wider); critic-informed checks largely practised (§3 rows 15–18) |
| M5 Judge by the decision, against the owner's rule | 84 (+16) | 160 (+10) | 15 | 233 | ✅ in OR and analytics deployment papers; ⚠ many of his group's clinical prediction papers score predictions only (§3 rows 19–23) |
| M6 Programmes: gate → cohort → course → book → company | 187 (+16) | 8 | 0 | 194 | ✅ lineage steps; step 1 still not observable in papers (§2 M6) |

Variant links dominate for M2–M5 because readers marked a link as a variant whenever one step of the method was missing or done differently; the rows of §3 group them by kind.

### M1 · Formulation first, kept in the solver class

- **Strongest practice**: all five steps in one sole-author text: the owning tradition and its ad hoc state, performance vectors as variables, LPs over extended polymatroids and polynomial-size relaxations, duals read as Gittins indices and as reduced-cost heuristics, the boundary printed as a complexity map [S185 pp. 1–3, 9–12, 21–25, 49–50]. The template for steps 1–4 in the conservation-law paper [S057 pp. 1, 3, 11–13, 20–21]; a central probability problem written exactly as a convex or semidefinite program with a dual certificate and the boundary printed [S018 pp. 5–6, 16–17]; the robust LP stays an LP and the robust MIP a MIP [S001 pp. 3–4, 10]; a robust 0-1 problem keeps the complexity of its nominal problem [S004 pp. 5–7, 22]; the robust inventory model stays an LP or MIP on any tree [S014 pp. 1, 4–5, 9–10]; a statistics estimator written as a convex integer program through Fenchel duality [S095 pp. 4–7]; a regularizer redesigned so a commercial solver's lazy callbacks apply [S175 pp. 1, 3, 9–10].
- **Stated in the texts**: the 1995 sole-author survey states that better formulations lead to deeper understanding and better methods [S185 p. 1]; the 1994 sole-author working paper places the essential difficulty of stochastic and dynamic optimization in its dynamic and combinatorial character, with the stochastic character secondary, and asks for an approach that does not change when the problem changes [S580 pp. 5, 10]; the 2004 network paper claims its robust approach keeps the nominal complexity [S004 p. 22]; the 2005 probability paper frames best-possible bounds as an optimization problem solved by convex and semidefinite programming [S018 p. 1].
- **Say–do update**: ✅ on 210 works, 1988–2026, in all nine domain codes. The SD and CP voice labels in SKILL.md need correcting (§3 row 1); the variant families are in §3 rows 6–8.

### M2 · Quantified "why now"

- **Strongest practice (10 works)**: the belief dated to the 1970s–80s and conceded as justified then [S010 p. 8; S081 p. 4; S011 pp. 3, 5–6; S105 pp. 1, 3, 6–7]; the figure rebuilt per flagship paper: 200 billion in the arXiv v1 of best subset, from version-on-version solver factors times Top500 peak speed, with the MIQO factor asserted [S010 pp. 7–8]; about 450 billion in the 2016 OR Forum paper [S081 p. 4]; 800 billion for trees [S011 pp. 5–6]. A belief dated and refuted with solve times at n and p in the 100,000s [S061 pp. 2, 4, 13]; tractability redefined as practical solve times already in 2014 [S178 pp. 3–5]; a speed-up measured against an owner's own simulator on one desktop [S476 pp. 1, 6]; the return to restless bandits once the tool changed [S681 pp. 1, 3, 8; S051 pp. 5–9].
- **Stated**: tractability defined as solving realistic sizes in application-appropriate times, not polynomial solvability [S010 p. 2]; computation in real problems named as the ultimate criterion for comparing conservatism [S001 p. 8].
- **Say–do update**: ✅ for steps 1 (find and date the belief), 2 (concede), 4–6 (lead with it; demonstrate at scale; return when tools change). ⚠ step 3 (rebuild the figure per paper) is practised only in the 2014–2017 statistics flagships (§3 row 9).

### M3 · The price of X

- **Strongest practice (46 works)**: the source paper with one knob per constraint, solution-independent bounds, the class kept and curves including the bad case [S001 pp. 1, 3–5, 9–16]; robust discrete problems with price curves on knapsack, sorting and shortest path [S004 pp. 4, 6, 16–22]; Γ curves with a knee and both failure modes [S027 pp. 6, 8–13, 30–35]; the price of fairness with a bound uniform over utility sets [S012 pp. 1, 7, 11–14] and a one-knob family with two-sided bounds handed to the manager [S026 pp. 1–2, 6–7, 10–12, 15–16]; community satisfaction priced in buses and dollars on a curve handed to a school district [S137 p. 5; S262 pp. 10–11]; the price of stability with Pareto properties [S401 pp. 3–4, 6, 10–11]; a radius tied by a solution-independent bound to a probability the decision-maker feels [S139 pp. 6, 15–16, 19]; set-only factors shown tight [S392 pp. 8, 10, 13–23].
- **Earliest forms, 1988–1996**: the thesis names the price of robust, global a priori solutions as a radical change in complexity [S048 p. 29]; one knob indexes the travel–waiting trade-off, with a worked price of 10% less travel for 21% more system time [S597 pp. 36–38; S032 pp. 15–16]; one knob (the arrival cap) gives a priced curve with a knee handed to policy makers [S135 pp. 15–16].
- **Say–do update**: ✅; the origin moves from 2004 to 1988 (§3 row 11). *Fix round*: the 1988 sentence prices robustness in lost tractability, with no knob or bound, so it is a precursor (the S048 card links it as a variant), not the method's statement; one-knob practice starts in 1990 [S597 pp. 36–38; S032 p. 16]; the stated method is joint, 2004 and 2011 ([02 G4]; [S012 p. 14]).

### M4 · Warm start, exact solve, honest certificate, duel the incumbent

- **Strongest practice (54 works)**: best subset with a 50-start heuristic warm start, a stated 500 s limit, gap curves and an out-of-sample duel with the standard implementations, with losing regimes printed [S010 pp. 27–40]; trees with CART as warm start and opponent at matched depth on 53 data sets [S011 pp. 14–15, 26–36]; product lines with the incumbent heuristic as warm start, stated limits, printed gaps and nothing unproved called optimal [S093 pp. 16–19]; sparse portfolios with certificates or printed gaps and a duel with the solvers' standard formulations [S725 pp. 13–23]; sparse PCA with a shared warm start for every method, a gap for every unsolved run, and the comparator's code repaired before the duel [S183 pp. 19–28]; one stack, one machine, one 900 s limit for every method [S317 pp. 13–24, 39–43, 49]; the 1993 review's yardsticks for simulated annealing, guarantees and equal computing time against the best specialized heuristic, applied to the Johnson et al. experiments it reports (it has none of its own) [S005 pp. 3–5].
- **Stated**: the MIO approach keeps a suboptimality gap and can stop early with a certificate of suboptimality [S225 p. 31]; the semidefinite relaxation gives suboptimality guarantees that measure heuristic policies [S007 p. 18]. An exact method finds the optimum quickly and spends most of its time proving it [S095 p. 5], said to justify a short limit set by confidence in the warm start, with no gap reported: a T1 instance (*fix round*: moved from SKILL.md's Stated line to Tension T1).
- **Say–do update**: ✅ for the protocol in his MIO methods papers. ⚠ the certificate: Tension T1 starts in 2004, not 2017 (§3 row 16). The critic-informed checks are largely his practice by 2020 (§3 row 15). Scope (§3 row 17).

### M5 · Judge by the decision, against the owner's current rule

- **Strongest practice (84 works)**: the practitioners' equal-split rule as baseline and cost in cents per share as metric [S009 pp. 3–4, 9–10, 13–25]; the industry's bid-price control as baseline with revenue and run times [S034 pp. 2, 4, 14–21]; ISO New England staff as co-authors supplying the system, the data and the operator's reserve practice as baseline [S006 pp. 1, 5–9]; the FAA's rules replayed in historical order [S114 pp. 2–3, 12–18]; the transplant committee's proposal scored in its own simulator [S044 pp. 5, 18–22]; the liver-allocation rule scored in the owner's policy simulator [S094 pp. 3, 5, 9]; tenure committees' decisions at equal capacity [S206 pp. 9–12]; an employer's claims and what it actually paid [S909 pp. 1, 9, 11, 17, 21–28]; the media firm's data with the prescription score [S008 pp. 10–12, 21, 29, 31]; Boston routes and bell times [S137 pp. 2–6]; a mining group's pre-2006 rule against EBITDA [S339 pp. 6, 8–11]; physicians' actual prescriptions [S370 pp. 2, 13, 15–18; S692 pp. 2, 4–6, 9–10, 19]; the owner's actual pandemic policy in every region [S482 pp. 3–4, 8–11].
- **Stated**: what matters is the prescription's performance in the problem, not the prediction score [S008 p. 29]; set sizes alone cannot predict decision performance [S013 p. 32].
- **Say–do update**: ✅ in OR, analytics and deployment papers; narrowed for clinical prediction papers (§3 row 19).

### M6 · Programmes

- **Strongest practice (187 works, mostly the lineage step)**: the thesis problem class came from his adviser's group [S048 pp. 18, 71, 125]; a student cohort consolidated in a sole-author survey with a recipe and open problems [S185 pp. 1, 4, 46, 48–49, 51]; a student's thesis line with Tsitsiklis as co-author [S072 pp. 1, 8, 10, 32–33], co-advised according to DSpace [04 A.2]; an organ-allocation programme in three stages carried by successive theses, with a former student among the co-authors [S476 pp. 1–2] (*fix round*: the byline after the first author is alphabetical and states no roles, so *co-senior* is withdrawn); programme continuity with a reused data asset and a software adoption channel [S097 pp. 5, 10, 27–28, 56]; a student-carried lineage from best subset to slowly varying regression with released code [S317 pp. 1, 5, 7–8, 39]; HAIM to xHAIM carried by a new cohort [S390 pp. 1, 8]; a company carrying the routing method to other districts [S262 p. 13]; a decade-long hospital partner with more than 20 projects [S617 arXiv pp. 1–2, 9, 28, 31].
- **Variants (8)**: the company before the paper [S050 pp. 1, 10]; a modelling package as the adoption channel [S028 pp. 2–3, 10]; a professional society and its registry as carrier [S364 pp. 3, 5]; lines he sponsors and edits outside optimization [S132 pp. 1, 13, 15; S478 pp. 1, 21–23; S616 pp. 1, 4–5]; a topic that predates the collaboration [S666 p. 15]; teachability argued after the fact [S018 pp. 4, 23].
- **Say–do update**: unchanged. Courses and books appear only at abstract level [S792; S793; S020; S128; S209; S047; S084; S334; S695], and the pre-start gate cannot be seen in papers.

### Heuristics, taste marks and tensions with new full-text practice

| SKILL.md item | Works whose cards cite it | Full-text practice (strongest cards) | Update |
|---|---|---|---|
| H1 robust problem behind a working heuristic | 26 | DP form in 1998: the model under which practice's equal split is exactly optimal, shown non-optimal elsewhere, then extended [S009 pp. 4, 9–10, 43]; regularization as robustification in the 2011 survey [S003 p. 37]; Lasso and SLOPE as robust problems [S225 pp. 5–6, 14–17]; iff conditions and two-sided bounds where the equivalence fails [S085 pp. 7–15, 18–22]; ℓ1 buys robustness, not sparsity [S725 p. 4]; dual-norm lemma for SVMs, logistic regression and trees [S104 pp. 9–12]; Tan's sensitivity model as an exact DRO problem [S333 pp. 5–7]; ridge as robustness [S218 p. 7]; averaged robust problem behind practice [S530 pp. 2, 9, 12–13]; numerical linear algebra [S458 pp. 3, 6–7]; adaptive coefficients [S623 pp. 2–4]; inverse variant: the problem Black–Litterman solves [S086 pp. 1, 3, 5–9] | Upgrade from "metadata level" to full text; add "with its boundary"; note that the Lasso equivalence is credited to Xu–Caramanis–Mannor and his contribution is where it breaks [S085 pp. 7–15] |
| H2 answer critics with a new paper | 2 | The reply to the best-subset critique adopts the critics' SNR grid and formula, concedes in part and releases code [S095 pp. 3, 10, 21, 23]; a 2017 version adds the handicap test absent from 2014 [S197 p. 12] | Add full-text evidence |
| H3 exact model stalls → local search | 24 | MIO kept as the move of a local search: local backbone [S046 pp. 22–26] and random subsets of schools [S137 p. 4]; exact optima on small instances certify the heuristic [S199 pp. 6, 8, 11, 13–15; S366 pp. 5–6, 8–12; S558 pp. 15–16; S867 pp. 18, 21–22]; when the bound stalls, relaxation plus rounding that still prints a bound gap [S183 pp. 22–26] | Refine (§3 row 31) |
| H4 negative results in the body | 51 | Losing regimes printed [S010 pp. 30, 38–40]; few uncertain coefficients explain PILOT4 [S001 p. 14]; regime map recommending greedy where it is near-optimal [S046 p. 19]; own tree losing to logistic regression said plainly [S276 p. 4; S296 pp. 5, 9]; non-implementation printed [S083 pp. 25, 27; S262 p. 12; S243 pp. 17–28]; own model weakest predictor [S370 pp. 13–16] | Add evidence; strongest-recurring heuristic in the cards |
| H5 learn the optimizer's strategy offline | 8 | Strategy labels and an interpretable model of the optimizer [S112 pp. 1–2, 9–10, 14, 17–21]; online MIO in milliseconds [S092 pp. 2–3, 8, 12–13, 20–23]; robot planning [S204 pp. 2–3, 5–8]; fluid restless bandits [S681 pp. 3, 5, 14, 24]; a structure theorem first [S402 pp. 9–11]; 1995 precursor: policies learned from exactly solved special cases [S098 p. 22] | Citation fix (§3 row 32) |
| H6 build the data asset | 8 | Rated patients first [S489 pp. 2–3, 7]; trial database [S292 pp. 2, 9]; registry automation [S364 pp. 1, 3–4]; HAIM data on PhysioNet [S023 pp. 1, 6, 8–9]; transcribed cohort studies [S099 pp. 2–3, 7, 9]; consortium and linked registry data [S527 pp. 2–4, 10, 19–20; S682 pp. 2–7] | Add evidence |
| H7 retry with the next student | 5 | A new student starts from the predecessor thesis's stated limit [S456 pp. 1, 3–4, 6]; 19 works enter from the group's own earlier limit (§6, cluster 20) | Add evidence |
| H9 abstract template | 7 | Practice → belief → figure → method [S081 p. 2]; belief and figure in the first sentences [S010 p. 1; S011 pp. 3, 5–6]; a week to ten minutes [S093 p. 2] | Add evidence |
| Taste mark 3 (optimize what practice does greedily or randomly) | 13 | Optimized assignment instead of randomization [S124 pp. 2, 4–6, 8; S312 pp. 1–2, 22; S357 pp. 3, 13]; optimized training samples [S873 pp. 3–8; S696 pp. 3–6, 16] | Nuance (§3 row 26) |
| Taste mark 5 (interpretable where people act) | 17 | Optimal trees chosen for clinicians [S276 p. 4; S682 pp. 2–7] | Refine (§3 row 27) |
| T1 certified vs uncertified | 64 | §3 row 16 | Extend dates |
| T2 joint optimization vs heuristic engine | 11 | §3 row 24 | Soften |
| T3 optimization, not probability | 21 | §3 row 25 | Add evidence |
| T4 strong formulations vs solver speed | 23 | §3 row 18 | Narrow |
| T6 headline vs caveat | 49 | The caveat sits in the body: hardware and solver progress conceded on p. 20, not in the abstract [S093 pp. 2, 20]; Boston (§3 row 22) | Keep; replace web citations by cards |

---

## 3. Variants and contradictions

Full texts win over the web-research notes 01–06. Nothing is deleted; each row says what should change.

| # | SKILL.md item | What the full texts show | Cards | Decision |
|---|---|---|---|---|
| 1 | Domain Map SD and CP rows ("co-authored papers only; no stated methodology found"), the matching Activation Rule and Honest Boundary line | **SD**: nine sole-author SD works are read in full. The thesis [S048 pp. 11–13]; queueing papers with stated motives [S239 pp. 1–2, 8, 12; S168 pp. 1–2, 14]; a priori routing [S833 pp. 6, 9; S186 pp. 2, 16–17; S148 pp. 1–2, 5]; the 1992 paper that states its approach and judges it [S017 pp. 3, 12]; the 1994 working paper and the 1995 survey that state the method [S580 pp. 5, 10; S185 pp. 1–3]. Co-authored statements too [S072 p. 2; S051 p. 1]. **CP**: no sole-author CP text beyond the surveys' SDP proposals [S185 pp. 44–45]; co-authored statements frame bounds as convex and semidefinite programs [S018 p. 1] and claim optimization improves classical results [S007 p. 35] | as cited | **Correct both rows** (do not expand them): SD voice "stated (sole-author 1988–1995) + practice"; CP voice "stated jointly + practice". Change the Activation Rule's "no stated methodology found" accordingly (*fix round*: that line is protected in T3.6, so the override sits in the first-activation disclaimer and the one-line edit is recorded as pending in `09-evidence-ledger.md#corrections`) |
| 2 | Domain Map IO row anchor DOI 10.1007/BF01580607 for "LP-relaxation rounding" | That paper (S052) has no rounding step: it bounds tree and matching constructions by the LP value and gives tight families [S052 pp. 10–18, 20–21]. Rounding is in the ground-holding LP [S036 pp. 6–7], one-threshold multicut rounding [S658 pp. 18–20], dependent rounding [S121 pp. 3–9], designed-distribution rounding [S435 pp. 3–6] and covariance rounding [S007 pp. 33–35] | as cited | **Fix the anchor**; S052 belongs to proposed Method 7 (relaxation as bound and yardstick) |
| 3 | Domain Map LO row ("dormant as a topic after 1998") | Confirmed in substance: LP-algorithm papers are 1994–1998 [S269 pp. 3–4; S289 pp. 2, 7–11; S156 pp. 1–2, 22–23]; later LO is an engine (column generation for convex-hull prices [S196 pp. 4–5, 8–10]) | as cited | Keep |
| 4 | Domain Map HS row ("convergence of his robust local search not read") | Read: an asymptotic annealing theorem is offered for runs stopped at an empirical threshold, with a global-optimum claim [S141 pp. 5–6, 9, 11]; the robust local search family leaves the solver class on purpose and carries no certificate [S278 pp. 2–6; S116 pp. 5, 8–9, 13–14]. *Fix round*: the row's anchor [S090] proves convergence only for convex costs with an exact worst-error oracle and diminishing steps, and calls the nonconvex method a heuristic [S090 pp. 5–6, 16–17] | as cited | **Replace the caution** by this finding (also T1, T2); narrow the Roundtable blind spot to asymptotic claims for stopped runs |
| 5 | Domain Map AP row ("outcomes thin") | Field outcome studies exist: a difference-in-differences study against the prior year plus a stratified comparison [S115 pp. 22–24], with post-deployment maintenance [S115 pp. 25–26]; length of stay measured after a staggered roll-out that supplies the control group [S617 arXiv pp. 11–14, 22–25, 37–39]; an additive impact ledger against the owner's old rule [S339 pp. 10–11]; deployed routing with the owner's scaled-down adoption [S137 p. 3] | as cited | **Qualify**: "outcomes measured in several deployments; Boston and DELPHI contested" |
| 6 | M1 "Different from standard practice: the model, not the algorithm, is redesigned"; How to Use "solver internals, which his record treats as black boxes"; Roundtable Card blind spot "solver internals" | From 2009 the group also redesigns algorithms: a tailored algorithm for cardinality-constrained QPs after the general MIQP proved unsuited [S040 pp. 2, 6, 10, 12, 15]; a first-order method for SOS relaxations [S315 pp. 8–12]; a solver bake-off before a tailored outer approximation [S105 pp. 7–9]; a custom branch-and-bound for sparse PCA after a general solver fails [S184 pp. 8–18]; closed-form Benders cuts without an LP solver [S093 pp. 10–13]; Kelley's method diagnosed through its bound's constant [S302 pp. 1, 5–8]; spatial branching on matrix variables [S385 pp. 2, 6, 10–14]; a group global solver extended to integers [S624 pp. 10–16]; a custom pricing routine [S316 pp. 3, 5, 11]; a tailored algorithm because the problem stays intractable for commercial solvers [S083 p. 15]. Earlier, the stated choice was a commercial package over custom algorithms [S036 p. 7] | as cited | **Add a variant line** to M1: "when the class is left, his group also builds the algorithm (outer approximation over binary supports, custom branch-and-bound, first-order methods)". **Narrow** "black boxes" to "commercial MIO solvers used as engines"; narrow the blind spot to "inside commercial solvers (presolve, cut selection)" |
| 7 | M1 one-line ("an LP, conic or MIO problem, with a device that keeps its nominal class") | In 1988–1997 the kept class is an analysable queueing or probability class: Coxian and rational-transform distributions dense in all distributions [S239 pp. 1–2, 8, 12; S168 pp. 3, 8, 12–15; S389 pp. 2, 11–14], analysable queues reached by policy design [S016 pp. 1–2, 7–11; S261 pp. 4, 11, 15–26], complete systems of laws [S129 pp. 1–4, 12; S280 pp. 1, 7, 9]. The 2010s robust-queueing line replaces distributions by limit-law sets and keeps closed forms [S119 pp. 7–13, 25, 41–47] | as cited | **Variant line** on M1 step 3: "for SD the class kept may be an analysable distribution or queue class" |
| 8 | M1 say–do ("1993–2026, five domains") | Some 2025–2026 AI papers have no formulation at all: a small network trained on a contrastive loss [S426 pp. 4, 6]; a training-free classifier [S474 pp. 2, 4, 8]; one optimization stated in a sentence [S618 pp. 13–14]; optimization only as study design [S439 pp. 5–6]. Two earlier contradictions: no exact formulation in a 2005 revenue-management paper [S066 pp. 2, 7, 10] and a class left on purpose without solve times [S278 pp. 2, 4] | as cited | **Scope sentence**: "his group's 2025–26 multimodal and foundation-model papers sit outside this method" |
| 9 | M2 step 3 ("rebuild the figure ... never reuse the last paper's number") | Rebuilt only in the 2014–2017 statistics flagships [S010 pp. 7–8; S081 p. 4; S011 pp. 5–6]. Repeated or borrowed in later papers [S105 pp. 6–7; S257 pp. 3, 13–16; S432 pp. 2, 16; S184 pp. 5, 25, 33–34; S355 pp. 5–6; S396 p. 2; S408 p. 9; S236 p. 3; S092 pp. 2, 6; S149 pp. 2, 8–9; S480 pp. 7, 9; S523 p. 4]. In about 46 of the 94 M2-linked works the why-now is a qualitative tool or data change, e.g. SDP solvers [S056 p. 3], interior-point methods [S003 p. 2], first-order methods [S315 p. 2], data availability [S074 pp. 1, 3; S193 pp. 2, 32; H004 p. 1], open LLMs [S390 pp. 1–2], a foundation model [S474 pp. 1–2]. Two contradictions: a 1994 "fastest" claim from operation counts [S269 pp. 1, 21–22] and the 2016 figure reused in 2024 [S480 pp. 7, 9] | as cited | **Relabel step 3** as the skill's rule (keep it as the checkpoint); add a variant line: "in most papers the why-now is a named tool or data change, without a figure" |
| 10 | M2 history | Before 2002 hardness was accepted as the limit of exact work and answered with relaxations and bounds [S185 pp. 49–50; S580 pp. 6–7; S052 pp. 2, 4]; in 1996 scarce computation argued for a priori routes [S025 pp. 10, 12, 17]; in 2002 his own matched-quality test found CPLEX 6.0 much slower than his heuristic [S070 pp. 13–15]. The belief is dated from 2007 and change argued in 2011 [S073 pp. 1–2; S561 pp. 3, 10–12]; it is conceded as justified when formed only from 2015 [S010 p. 8] (*fix round*) | as cited | **Add** to M2 Limitations: "the reverse argument (scarce computation favours simple a priori policies) is his own 1990s position" |
| 11 | M3 origin (2004) | The price of a simple, stable solution against re-solving, measured asymptotically and in the worst case, is the 1988–1993 thesis line [S048 pp. 29, 40–44, 84–85; S148 pp. 5, 14–17; S017 pp. 1, 9–11; S102 pp. 2, 14–18]; price of a fairness policy in routing [S091 pp. 11, 23–25; S025 pp. 11–12, 14–16]; a one-knob curve with a knee for policy makers [S135 pp. 15–16] | as cited | **Add** these as M3 practice evidence and a variant ("price of simplicity": no knob, the price is an asymptotic constant or a worst-case ratio) |
| 12 | M3 correction ("knobs get fixed arbitrarily ... as his group later did") | Knobs set from data or theory from 2006: Γ from mean and variance by minimizing a worst-case bound [S014 pp. 1, 10–12]; a lookup table of the knob per class and ε [S022 pp. 3, 15, 19]; radius calibrated to 99% of measured errors [S090 pp. 12, 14]; the decision-maker's CVaR level as the knob [S024 pp. 3, 5, 9, 11]; CLT scaling [S006 p. 6]; knobs implied by market prices [S171 pp. 8, 10]; hold-out validation [S013 pp. 29–31; S440 pp. 9–11]. Hand-set knobs persist [S124 pp. 4–5; S163 pp. 24, 28; S458 pp. 4, 7, 10; H001 pp. 14–16] | as cited | **Revise** "later" to "from 2006, alongside hand-set knobs" |
| 13 | M3 step 3 (solution-independent bound) | Present mainly in robustness and fairness [S001 pp. 3–5; S004 pp. 4, 6; S027 pp. 6, 8–13; S012 pp. 7, 11–14; S026 pp. 6–7; S139 pp. 6, 15–16; H004 pp. 6–9; S672 pp. 23–24, 27–29]. The price of interpretability is usually one or two points, without a curve or bound [S190 pp. 4, 7–8; S356 p. 2; H003 pp. 1, 24–26; S457 pp. 4, 13, 21; S267 pp. 21, 25] | as cited | **Variant note** on M3 step 5 |
| 14 | M3 step 5 (curve on the rival's test problems) | A misspecification duel recurs: the robust policy and the model-based optimum (DP, SAA) are both scored under distributions other than the assumed one, or beyond the set [S014 p. 12; S027 pp. 9–10, 21; S055 pp. 8–9; S059 pp. 9, 11, 14; S053 pp. 14–22; S278 pp. 5–6; S116 p. 12; S003 pp. 6–7; S006 pp. 5, 7; S172 pp. 21–23]; stated as a lesson in 2025 [S623 p. 4] | 25 works, 2003–2026 | **Add to step 5**: "score the robust decision and the model-based one under misspecified truths and beyond the set; print where robust loses" (eligible as a heuristic; folded here because of the heuristic cap, §5) |
| 15 | M4's list of critic-informed checks labelled "not his practice" (low SNR, equal budgets and threads, path-to-path timing, installable code, LP-relaxation strength); Roundtable blind spot "fair benchmarking" | Equal computing time is the criterion of the 1993 SA review [S005 pp. 3–4]; the same single-threaded 60 s per decision for both methods [S340 pp. 16, 23]; equal memory over time checkpoints [S328 pp. 2, 9, 11–15; S914 pp. 22–24]; matched budgets with significance tests [S197 pp. 8–14]; threads and confidence intervals stated [S088 pp. 10–14]; one thread, equal tolerance and time limit against BARON, SCIP and CPLEX [S708 pp. 35–41]; one stack, one machine, one limit, low SNR, timing with tuning and released code [S317 pp. 13–24, 39–43, 49]; SNR grids already in 2016 [S010 pp. 26, 30, 38] and the critics' grid adopted in the reply [S095 pp. 3, 10, 21, 23]; code released [S093 p. 16; S208 pp. 11–14; S139 p. 8]; formulation strength (row 18). Exceptions with the tilt stated: big-M solvers given 28 threads against one [S725 pp. 17, 19]. *Fix round*: the 1993 review has no experiments of its own; equal time is its stated yardstick for Johnson et al.'s [S005 pp. 3–4]; his own matched comparisons start in 2002 [S070 pp. 9–15] | 44 works match budgets or inputs (§6 cluster 12) | **Revise the label**: "stated as a yardstick in 1993, practised from 2002 and widespread after 2020; the critics' cases (note 05) concern particular papers of the best-subset line". **Narrow** the blind spot "fair benchmarking" |
| 16 | M4 say–do (certificate "stated but dropped at scale", citing OCT 2017) and Tension T1 | T1 is older and wider. 2004: a MIP stopped after five feasible solutions, because exact runs can be excessive [S031 p. 26]; 2007: early termination at a 5–10% gap justified, while the conclusion claims a global optimum [S073 pp. 15–18]; 2010: an asymptotic theorem offered for empirically stopped runs [S141 pp. 5–6, 9, 11]; 2017: most tree results without certificates [S011 pp. 14, 26]. In applied papers 2019–2026, trees are called optimal with no solver, gap or limit [S094 pp. 5, 9; S235 pp. 2–3; S272 pp. 2, 5; S287 pp. 1, 12; S376 p. 2; S527 pp. 1, 7, 13; S615 pp. 11–12, 42; S626 pp. 1, 5–6; S682 pp. 4–5; S688 pp. 7–8, 22]. Counter-practice with honest labels: [S093 pp. 17, 19; S554 pp. 1, 13, 23; S488 pp. 23–27; S909 pp. 14–15; S668 pp. 20, 24–25; S681 pp. 2–5] | as cited; 64 works carry a T1 note | **Extend** T1's dates to 2004–2026; add the honest-label side |
| 17 | M4 scope | In clinical collaborations the final learner is usually a tuned off-the-shelf ensemble, not an exact model [S054 pp. 2, 4; S127 pp. 3–4, 8; S023 pp. 3, 8; S677 pp. 2, 6, 8, 24; S678 pp. 4, 9, 14, 43; S618 pp. 3, 8–10, 13; S683 pp. 5–6]; a greedy step kept with the MIO deferred [S391 pp. 5, 8]. A simple incumbent (mean imputation) is proved asymptotically optimal for prediction and wins [S310 pp. 4–8, 12] | as cited | **Scope line** on M4: "governs his MIO-for-ML methods papers, not his clinical collaborations" |
| 18 | Tension T4 [inferred] and blind spot "formulation strength" | Formulation strength is measured and pursued: models judged by total unimodularity, facets and solve time in 1997 [S241 pp. 14–15, 27, 31–32]; facets designed so LPs are almost always integral [S015 pp. 2, 4–5, 10]; strengthened links for stronger LP bounds [S101 pp. 17–18]; cover inequalities so only one of 41 instances branches [S109 pp. 2–8]; valid inequalities without which the model fails [S037 pp. 2, 4–8]; convex-hull and TU checks [S076 pp. 12–19, 35–36]; a formulation-strength ordering tested against gaps and solve times, printing where it fails [S093 pp. 8–9, 17–19]; constrained Lasso shown weaker than the root relaxation [S010 pp. 9–10]; big-M left for convex integer or perspective forms [S061 p. 6; S175 pp. 9–10, 15–16; S136 pp. 3, 6–7, 26–27]; SOC strengthening kept [S250 p. 23]. Big-M weakness printed by the authors themselves [S225 pp. 5–9; S358 pp. 4–12] | as cited | **Narrow T4** to optimal trees and some ML models; **narrow the blind spot** ("formulation strength of tree MIOs"); the 2005 book's stance is practice too |
| 19 | M5 say–do ✅ | 15 contradictions. Fourteen are prediction papers of 2014–2026, twelve of them clinical, that score predictions (AUC and the like) with no decision and no current-rule baseline [S557 pp. 4, 8, 13; S281 pp. 3, 6; S054 pp. 4–9; S127 pp. 1, 5, 7–8; S219 pp. 5–7; S023 pp. 1, 3, 7–8; S351 pp. 1, 16–19, 22–23; S381 pp. 2, 7–8; S390 pp. 1, 3–5; S621 pp. 2–3, 16–18; S683 pp. 1–2, 5–6; S677 pp. 1, 8–9; S678 pp. 5–6, 9–10; S872 pp. 3–4]; the fifteenth is a vaccine-site plan whose headline gain is measured against the weakest of its constructed rules [S083 pp. 1, 17–18, 23]. Variants: constructed or literature baselines instead of the owner's rule [S193 pp. 6, 28–31; S028 pp. 12–15]; in 1988–1996 the comparator is the re-optimization ideal [S048 pp. 27, 71; S017 pp. 3, 12] | as cited | **Narrow** M5's say–do: "practised in OR and analytics deployment papers; many of his group's clinical prediction papers score predictions only (Warning sign 4 applies to them)" |
| 20 | M5 checkpoints | When the counterfactual cannot be observed, the group chooses evaluation proxies whose bias runs in a stated direction: a simulation metric biased toward the model next to a matching metric [S078 pp. 14–16]; input guards so savings are understated [S909 pp. 12, 19, 28]; a pessimistic proxy for an unobserved event time [S481 pp. 2–3]; ground truths from several models in turn [S174 pp. 22–25; S370 pp. 15–16; S343 pp. 6, 8]; confounding calibrated with a known sign [S393 pp. 6–7, 13, 20]; trial emulation [S692 pp. 2, 4, 7–8]; frozen models scored blind by the data owner [S527 pp. 1, 20]; a conservative control group stated as such [S617 arXiv p. 25] | 25 works, 2013–2026 | **Add a checkpoint** to M5: "when the counterfactual is unobservable, use proxies whose bias favours the incumbent and say which way" (heuristic-eligible; folded here, §5) |
| 21 | M5 step 6 (propose, then field-test) | Deployment design recurs: start from what blocks implementation [S012 pp. 1, 14; S026 pp. 11–12]; keep the incumbent's inputs, format and standard [S114 pp. 4–5, 11–12; S044 pp. 1, 6, 18–19]; an adoption term penalizing distance from the status quo [S416 pp. 8, 14, 32]; staged deployment, better inputs to the owner's rule first [S384 pp. 2, 5, 7–9; S339 pp. 8–9]; an integration section mapping the model onto the owner's process [S076 pp. 22–23; S245 pp. 11–13; S621 pp. 20–22]; a physician-champion pilot then staggered roll-out [S617 arXiv pp. 11–14] | 33 works, 2002–2026 | **Add as practice evidence** to M5 step 6; not a new heuristic |
| 22 | M5 correction (Boston: let stakeholders contest trade-offs) and T6 example ("delayed" in PNAS vs "not implemented" in the thesis) | The PNAS paper itself says the start times had not been implemented because of parents' concern (p. 2) and calls it a delay later (p. 6) [S137 pp. 2, 6]; the trade-off curve was shown to the district [S137 p. 5]. The group's own 2020 account says the plan did not become reality and names missing school-level engagement and missing comparisons with current times as causes [S262 pp. 10–12]. A 2022 scheduling paper shows its metrics at town halls and reports non-adoption plainly [S243 pp. 17–28] | as cited | **Qualify** the T6 example; record that the stakeholder lesson is also his group's own (2020) |
| 23 | M5 correction (DELPHI) | Confirmed from the cards: the hub evaluation puts DELPHI's relative WIS at the baseline level [S021 pp. 2, 4]; the group's own CDC comparison uses its own metric and window [S103 pp. 14–16]; a German–Polish hub scores DELPHI worse than the naive baseline (higher mean WIS) for one- and two-week cases and one-week deaths, better for two-week deaths [S157 pp. 15–16] | as cited | **Replace** the web citations by these cards; hub papers stay external evaluation |
| 24 | Tension T2 ("SA judged theoretically lacking in 1993") | The 1993 review also credits simulated annealing with general applicability and good solutions where structure is not understood, finds its practice mixed, and judges it by the equal-time comparisons it reports from Johnson et al. [S005 pp. 4–5]; a priori heuristics recommended to practitioners in 1991 [S089 pp. 1, 33]; a heuristic engine beating CPLEX in 2002 [S070 pp. 13–15]; a regime map that recommends greedy where optimization does not pay [S046 p. 19]; annealing in daily production [S103 pp. 8–9] | as cited | **Soften** T2: the 1993 verdict is theory lacking, practice mixed but generally applicable (*fix round*: *useful* overstated it) |
| 25 | Tension T3 (optimization, not probability) | The practised probability side is large: asymptotic probabilistic analysis is the backbone of 1988–2002 [S038 pp. 6–8; S016 pp. 5–14; S017 pp. 10–11; S130 pp. 4, 13, 22]; limit laws re-enter as uncertainty sets [S065 pp. 5–10; S119 pp. 7–10; S227 pp. 1, 4, 13, 27]; clinical texts centre on confounding and calibration [S685 pp. 1–3]; Bayesian and EM machinery [S666 pp. 7–8, 44–45] | as cited | **Add evidence** to T3 |
| 26 | Taste mark 3 | Applied with regime maps: greedy recommended where near-optimal [S046 p. 19]; crude mean imputation preferred for prediction after his group's own earlier promotion of sophisticated imputation [S310 pp. 5, 12–13] | as cited | **Nuance**: "after mapping where joint optimization pays" |
| 27 | Taste mark 5 | Interpretability scoped by decision type: required where guidance changes standard care, black boxes acceptable for diagnosis [S685 pp. 2–3]. Counter-practice: boosted trees explained by SHAP in tools clinicians use [S054 pp. 4–9; S621 pp. 2–3, 16–18], and a trust ladder from optimal trees to a black box [S617 arXiv pp. 9–11, 20–21] | as cited | **Refine** the mark |
| 28 | Warning sign 2 (polynomial time without solve times) | His 1994–1997 papers do exactly this [S269 pp. 1, 21–22; S289 pp. 2, 6, 11–12]; the 2016 redefinition of tractability [S010 p. 2] | as cited | **Date** the warning: computation named the criterion in 2004 [S001 p. 8]; solve time stated as the test from 2014 [S178 p. 5] (*fix round*: replaces "from about 2004"; same dating in M1's "tractable drifts" note) |
| 29 | SW3 "how Γ arose: unknown" | A 2002 working paper with Pachamanova already uses a budget Γ normalized by standard deviations, to narrow computed bounds [S653 pp. 12–14, 24]; the origin of the idea is still not stated in any card | as cited | Add the data point; keep "unknown" |
| 30 | H1 "[metadata level]" | See §2 table | as cited | **Upgrade** |
| 31 | H3 | MIO kept as the local-search move, not abandoned [S046 pp. 24–26; S137 p. 4]; small exact optima as the heuristic's certificate (11 works, §6 cluster 24); an intractability verdict by size count, once without re-measurement [S456 pp. 4, 6, 15] | as cited | **Variant note**: "keep MIO as the neighbourhood move; certify the heuristic on small exact instances" |
| 32 | H5 citation DOI 10.1287/opre.2021.0707 | That paper (S097) learns constraints from decision–outcome data, not an optimizer's strategy for repeated solves [S097 pp. 1–9] | as cited | **Replace** the DOI by S204 (DOI 10.1109/cdc42340.2020.9304043) or S681 (DOI 10.1007/s10994-026-07022-0); move S097 to M5 / DA |
| 33 | Research Trajectory 1985–1995 "Inherited from Odoni's group [inferred]"; 1995–2001 "Moments and SDP" | The thesis documents the inheritance [S048 pp. 18, 71, 125; S038 p. 5]. SDP strengthening starts in 1994–95 [S072 pp. 20–22; S185 pp. 44–45]; robust optimization with budgets from 2002 [S653 pp. 12–14; S004 pp. 4–7; S001 pp. 3–5] | as cited | **Upgrade** [inferred] to practice; adjust the period starts (§8) |
| 34 | Honest Boundary and Activation disclaimer ("no full-text deep reading has been done yet") | 472 works read in full or in part, 459 of them used as method evidence after merging version pairs (§1) | §1 | **Overturned**; rewrite the disclaimer |
| 35 | Note 06 ("1988–1995 ... little computation") | A home-made C package, 45 PTSP problems and 20 instances per VRP type against named heuristics in 1991 [S089 pp. 13–17, 23, 26–28]; programmed queueing algorithms with run times by step [S291 p. 13; S168 pp. 15–16; S389 pp. 11–14]; an IP solved with MPSX [S036 pp. 7–10]; airport congestion runs on real data [S135 pp. 1–2, 7–8, 15–16] | as cited | **Correct note 06**: "theory-led, with steady computation" |
| 36 | Note 05 row 16 (execution costs: "permanent impact only") | The LPT law makes impact temporary; permanent impact and negative prices are defects named in the paper's first illustration [S009 pp. 17, 20–22] | as cited | **Correct note 05** |

---

## 4. Promotions

### Proposed Method 7: Bound before policy. Derive a bound valid for every policy, read the policy off it, grade every policy against it, and show where the ratio is tight {SD IO CP RO; LO as engine}

SKILL.md has six methods; this makes seven, the top of the 3–7 range.

**Cards (79 distinct works read in full or in part, 1988–2026, version pairs merged; 81 before the fix round)**. The core: lower bounds over all policies and constant-factor policies in dynamic routing [S016 pp. 3, 5–11; S032 pp. 3–15; S091 pp. 3, 11–17, 25–28; S597 pp. 13–31]; the radial bound and cyclic heuristic [S017 pp. 7–10]; the LP relaxation as object, yardstick and lever [S052 pp. 3, 7–9, 10–18, 20–21; S269 pp. 1–2, 5, 17; S036 pp. 6–10; S015 pp. 2, 10–13; S345 pp. 1–8; S166 pp. 2–25]; achievable-region relaxations, hierarchies and heuristics [S185 pp. 22–25, 29–32, 48–49; S580 pp. 9–10, 38–40, 47–48; S072 pp. 2, 20–22, 26–31; S368 pp. 4–8, 10–13; S051 pp. 1, 5–11; H010 pp. 23–28]; fluid relaxations as bound, template and yardstick [S130 pp. 7–8, 13, 17–18; S205 pp. 9–11, 26–27, 35; S207 pp. 12–16]; relax, randomize, then pack with an exact IP certified by the LP bound [S043 pp. 7–9, 16]; SDP bounds to certify fluid policies [S007 pp. 9, 16–18]; LP-relaxation quality yardstick in ADP [S070 p. 9]; adaptive RO: the price of static and affine policies with tight families [S134 pp. 6, 12–18; S176 pp. 13–14; S192 pp. 16, 18–19; S042 pp. 2–3, 25–26], sampled lower bounds from binding scenarios [S138 pp. 7–9; S082 pp. 12, 15, 17; S087 pp. 9–11, 34–35], conservative benchmark bounds [S049 p. 14; S153 p. 23]; tight ratio bounds [S191 pp. 5–8; S392 pp. 15–17, 19–20]; relaxations certifying heuristics in 2023–2025 [S274 pp. 29–30; S403 pp. 16, 31–32; S684 pp. 11–12, 16–17]. Full list: §6 clusters 1 and 2.

**What the cards show**:
- The bound comes first and is valid for every policy: heavy- and light-traffic bounds before any policy is analysed [S016 p. 3]; a sequence of lower bounds in the discrete-optimization tradition [S072 p. 2]; Lagrangean duals and LP relaxations as the bounds that feed branch and bound and judge heuristics [S269 pp. 1–2, 5, 17].
- The policy is read off the bound's solution: primal support and reduced costs give a priority index [S051 pp. 7–9]; visit rates rounded into routing tables by an IP [S185 pp. 29–31; S293 pp. 23–31]; fractional flows decomposed by randomized rounding into a path pool [S043 pp. 7–9]; the schedule tracks the fluid optimum [S205 pp. 9–11]; LP values read as probabilities [S121 pp. 3–9; S007 pp. 33–35].
- The policy is graded against the same bound, as a ratio or gap, and the incumbent heuristics are graded the same way [S072 pp. 26–31; S185 pp. 25, 32, 48; S368 pp. 10–13; S153 p. 23].
- Tightness is checked: tight families in both directions [S052 pp. 20–21]; a tight instance by symmetry and a forced repeating step [S161 TR pp. 3–5; S289 pp. 7–11]; a bound attained by an explicit family [S191 pp. 7–8; S176 pp. 13–14; S392 pp. 15–17]; exactness fenced by a computed counterexample [S042 pp. 25–26; S028 p. 8]; unproved constants printed as conjectures [S016 pp. 7, 9; S032 pp. 7–8, 11, 16; S158 pp. 15, 17] (29 works, §6 cluster 2).
- When the gap stays open, the relaxation is strengthened by interaction order or PSD constraints, and size limits are printed [S185 pp. 22–24, 44–45; S051 pp. 6–7; S072 pp. 20–22; S684 pp. 11–12, 17]; the loose side is named when it cannot be measured [S072 p. 26; S212 p. 24].

**Four checks**:
1. **Cross-project recurrence** ✅: 79 works in all eight periods (9, 16, 20, 4, 5, 9, 7 and 9 works from 1988–92 to 2023–26), domain tags IO 53, LO 31, SD 30, CP 23, RO 21; coauthor groups from van Ryzin [S016], Goemans [S052], Orlin [S269], Paschalidis–Tsitsiklis [S072], Niño-Mora [S051] and Stock Patterson [S043] to Goyal [S134; S176; S165], Bidkhori [S192], Iancu–Parrilo [S042; S075], Georghiou [S082], Dunning [S087], de Ruiter [S138] and Na, Stellato and Wang [S392].
2. **Say–do consistency** ✅: stated in his own sole-author survey, which contrasts the ad hoc methods of stochastic control with mathematical programming's plan of attack that yields optimal solutions or a guaranteed degree of suboptimality, and lists bounds on the gap between heuristic policies and relaxations as the next step [S185 pp. 1–2, 51]; stated jointly that judging heuristics against other heuristics says little about their suboptimality, and that the approach delivers a feasible policy with a suboptimality guarantee [S051 pp. 1, 11]; and that SDP relaxations give suboptimality guarantees for heuristic policies [S007 p. 18]. Practised in the 79 works of the clusters, by construction: no card links the method by name, so contradictions were not searched for (*fix round*). Two core works skip a step: the named incumbent, Whittle's index, is not graded against the bound [S051 pp. 3, 10], and no network policy is read off the bound [S072 pp. 27–30].
3. **Executable, and different from standard practice** ✅: the steps below produce actions that a heuristic-versus-heuristic study or an exact-DP study would not take (derive a bound for all policies first; extract the policy from the bound's solution; grade the incumbent by the same bound; build the tight instance). The cards record the practice it replaced: problem-specific formulations and heuristics compared only with each other [S185 pp. 1–2; S051 p. 1], and affine policies advocated without quality results [S042 p. 3].
4. **Exclusivity** ✅ (qualified; [inferred], since no card compares him with peers). Counter-evidence on the cards: heuristic ratios were the Steiner and approximation literature's before S052 sharpened them into ratios to the LP bound [S052 pp. 3, 11]; the performance-region approach in queueing is credited to Coffman–Mitrani, Gelenbe–Mitrani, Federgruen–Groenevelt, Shanthikumar–Yao and Tsoucas [S580 p. 12; S185 pp. 3–4; S057 pp. 3–4]; Whittle's relaxation is the hierarchy's first rung [S185 p. 21]; the loss-network relaxation is Kelly's bound in LP form [S368 p. 8]. So in IO alone, or SD alone, the check fails. What the cards show beyond it is the transfer of the same bound–policy–yardstick loop into stochastic control (achievable region, restless bandits [S185; S051]), dynamic routing (bounds over all policies [S016; S032]), and adaptive robust optimization (the price of a policy class with tight families [S134; S176; S192]), with the incumbent graded by the same bound. The check passes on that cross-domain loop only; read as a hard gate needing carded peer comparisons, it would make Method 7 a heuristic, and the heuristics are at their cap (§5). (*Fix round*: the earlier citation [S052 p. 2] for *standard in approximation algorithms* is withdrawn; that page says only that NP-hardness typically leads to approximate solutions.)

**Proposed steps**:
1. Write a relaxation valid for every policy: an LP or conservation-law relaxation of the performance region, a fluid or Lagrangean relaxation, a bound over all policies in a limiting regime, or a sampled-scenario bound [S016 p. 3; S185 pp. 8–12, 21–24; S269 pp. 3–4; S130 pp. 7–8; S138 pp. 7–9].
2. Read the policy off its solution: indices from reduced costs, rounding of fractional values (one shared threshold, covariance sampling), tracking the fluid optimum, an affine or finitely adaptable rule [S051 pp. 7–9; S658 pp. 18–20; S007 pp. 33–35; S205 pp. 9–11; S075 pp. 9, 14].
3. Prove the policy's ratio to the bound: a constant factor, an asymptotic optimality, or a price of the policy class that depends only on the set [S016 pp. 5–11; S130 pp. 4, 13, 22; S192 pp. 16, 18–19; S392 pp. 15–17].
4. Check tightness: build the instance that attains the ratio, or fence exactness with a counterexample just outside it; print open constants as conjectures [S052 pp. 20–21; S191 pp. 7–8; S042 pp. 25–26; S016 pp. 7, 9].
5. Grade every heuristic, the incumbent's included, by its gap to the same bound [S072 pp. 26–31; S368 pp. 10–13; S070 p. 9; S403 pp. 16, 31–32].
6. If the gap does not close, strengthen the relaxation (higher interaction order, PSD constraints) and print where its size becomes prohibitive [S185 pp. 22–24, 44–45; S051 pp. 6–7; S684 pp. 11–12, 17].

🔴 **Stop rule**: no bound, no claim of near-optimality; if the policy is only compared with other heuristics, say so, as the 1995 survey did of its own policies [S185 p. 49].

**Limitations to write in**: bounds can be loose without telling which side is loose [S072 p. 26; S212 p. 24]; policies from relaxations were admitted to be ad hoc and missing for networks [S185 p. 49]; 45 of the 79 works date from 1988–2002; when an exact MIO solves at scale, Method 4's solver gap replaces the proved ratio [S010 pp. 27–40]; the yardstick is the bound or the re-optimization ideal, not an owner's current rule (contrast Method 5) [S048 pp. 27, 71; S017 pp. 3, 12].

**What changes in SKILL.md**: add Method 7 after Method 6; Research Task Routing: a row "How good is my policy when no exact solve exists?" → Method 7, and "Stuck: the bound does not move" → also Method 7 step 6; the domain-layer map (to be written later) should cite Method 7 in its SD, IO, CP and RO rows; SW1's "Abandoned paths" points to Method 7's stop rule; optionally add "a bound valid for every policy" to the Roundtable Card's Default recommendation, keeping its seven bullets. Word budget: Method 7 needs about 230 words; to keep about 600 words of headroom for the later domain map, move long evidence lines to `09-evidence-ledger.md`.

### Considered and not promoted

- **Re-derive the classical results with the new device, then extend** (80 works; §6 cluster 5): passes recurrence, say–do and executability, fails exclusivity (generalizing known results is routine in mathematics). → Heuristic 10 (§5).
- **Find the exact problem a working heuristic solves** (18 works; §6 cluster 6): recurrence ✅, say–do ✅ [S003 p. 37; S085 pp. 7–15], executable ✅; exclusivity partial, since the cards credit the Lasso equivalence to Xu–Caramanis–Mannor [S085 pp. 7–15]. Stays Heuristic 1, upgraded (§3 row 30).
- **Matched duel: level the field and state the residual tilt** (44 works; §6 cluster 12): it is Method 4 step 5 done carefully; promoting it would duplicate Method 4. → evidence and label correction (§3 row 15).
- **Price of simplicity** (37 works; §6 cluster 4): Method 3 with X = simplicity or tractability. → M3 variant (§3 row 11).
- **Asymptotic regimes for sharp constants** (22 works, 19 of them 1988–2002; §6 cluster 3): the bound in Method 7's step 1 for the probabilistic-analysis years; exclusivity weak (the Beardwood–Halton–Hammersley and Steele tradition [S038 pp. 4–5]). → M7 variant.

---

## 5. New heuristics

SKILL.md has nine heuristics; the framework allows 5–10. One heuristic is proposed, bringing it to ten. Three more heuristic-eligible clusters are folded into existing methods instead, because a cap of ten leaves no room and because each refines one step of a method: the misspecification duel into M3 step 5 (§3 row 14), bias-signed evaluation into M5's checkpoints (§3 row 20), and deployment design into M5 step 6 (§3 row 21).

### H10 (new) · If you introduce a new device, first re-derive the field's classical results with it (special cases, limits, relaxations), print where the equivalence breaks, then extend

- **Evidence (80 works, 1988–2026, all periods)**: queueing results that classical methods treat case by case recovered as special cases of one closed form [S239 pp. 2, 8–12; S168 pp. 2, 10–11; S389 pp. 3–8; S663 pp. 3–4, 11–15]; Little's law, Burke's theorem and Pollaczek–Khinchine recovered from distributional laws [S129 pp. 1–2, 9–12; S336 pp. 1–3, 18–19]; the cμ rule, Smith's rule, Klimov's algorithm and Gittins indices as one adaptive greedy algorithm on one polytope [S057 pp. 3–4, 22, 38, 42, 46–47]; classical conservation laws recovered from potential functions [S072 pp. 10, 22–26]; integrality of classical polyhedra and max-flow min-cut by one rounding argument [S121 pp. 2–7; S214 pp. 5–11]; Markov and Chebyshev bounds generalized and the 0.878 max-cut bound re-proved [S007 pp. 23–25, 31–35]; Kingman's and Daley's bounds as special cases [S255 pp. 1, 7–9]; Riccati at radius zero [S118 p. 6]; the classical fluid model at Γ = 0 and an alternative proof of the cμ rule [S244 pp. 9–10]; the S-lemma and Bertsimas–Sim recovered before tighter levels [S283 pp. 3–4, 15–19]; ν-SVM as a relaxation of the exact model [S360 pp. 12, 15, 18]; constrained Lasso weaker than the root relaxation [S010 pp. 9–10]; regress-and-compare as a depth-1 tree [S096 pp. 3–4, 7]; SAA as one member of the weighted family [S193 pp. 6, 29–31; S163 p. 7]; basis pursuit denoising as the perspective relaxation [S290 pp. 10–14]; his own earlier relaxation placed in a new hierarchy and beaten [S216 pp. 5, 14, 18–19]; the method shown to tie where it should [S688 p. 12; S415 pp. 19–20; S681 pp. 17–20].
- **Stated**: unification named as the aim [S663 p. 3]; results mostly known, the new part being the unifying derivation [S129 p. 2]; classical bounds as special cases [S255 p. 1]; optimization improving classical results [S007 p. 35].
- **Steps**: (1) list the classical results and tools the field relies on; (2) derive each as a special case, a limit of your knob, or a relaxation of your formulation; (3) state the condition where the equivalence breaks [S085 pp. 7–15]; (4) place your own earlier method in the new order [S216 pp. 5, 14]; (5) only then extend.
- **Checks**: recurrence ✅; say–do ✅ (stated jointly); executable ✅; exclusivity ✗. → heuristic.

---

## 6. Candidate pool (not promoted)

All 1,148 new-pattern candidates were read and grouped by meaning into 34 clusters (every candidate assigned). Counts are distinct works read in full or in part; abstract-only works in brackets. *Fix round*: clusters 1, 2, 3, 7, 12 and 25 lost one or two works when four more version pairs were merged (counting rule 2).

| # | Cluster (meaning) | Works | Span | Where it went |
|---|---|---|---|---|
| 1 | Relaxation as bound, policy source and yardstick | 58 (+3) | 1991–2026 | **Method 7** (§4) |
| 2 | Tightness audit: print where one's own bound is loose or fails | 29 | 1988–2026 | **Method 7** step 4 |
| 3 | Asymptotic regimes for sharp constants; asymptotic optimality as warrant [S038 pp. 6–8, 10–12; S016 pp. 5–14; S130 pp. 4, 13, 22; S310 pp. 5–7] | 22 | 1988–2022 | M7 variant |
| 4 | Price of simplicity: a priori, simplified or regularized models priced against the ideal [S089 pp. 2, 14, 17, 28, 33; S025 pp. 11–12; S048 pp. 12–13; S136 pp. 3–4, 16–17; S250 pp. 12, 26, 33–36] | 37 | 1988–2026 | M3 variant (§3 row 11) |
| 5 | Re-derive classical results with the new device | 80 | 1988–2026 | **Heuristic 10** (§5) |
| 6 | Find the exact problem a working heuristic or practice solves | 18 (+1) | 1998–2026 | H1 upgrade |
| 7 | Carry a classical device into the uncertain, dynamic or neighbouring setting and measure what survives [S038 pp. 9–10; S091 p. 31; S029 pp. 12, 16, 37; S458 pp. 3, 6–7] | 39 (+1) | 1988–2026 | M1 step 1 evidence; exclusivity fails (robust or stochastic versions of known problems are common) |
| 8 | Uncertainty sets built from a justified primitive: limit laws, tests, predictors, data splits [S065 pp. 5–10; S119 pp. 7–10; S013 pp. 3–4, 10; S440 pp. 3–9; S543 pp. 4–12] | 27 | 2009–2026 | M3 knob correction and RO row evidence |
| 9 | Assume only what can be estimated; worst case over the rest, tight by an extremal distribution [S018 pp. 2, 19–21; S031 pp. 7–8; S169 pp. 2–3, 8, 23; S452 pp. 1–2; S223 pp. 12–13] | 13 | 2002–2026 | M1 evidence for CP (row 1) |
| 10 | Adaptive policies: power and limits of a tractable policy class [S134 pp. 6, 12–18; S165 pp. 21–22, 24; S217 pp. 9–11; S060 pp. 15, 23] | 17 (+1) | 1997–2025 | M7 step 3 |
| 11 | Stress the decision outside the model it was built for | 25 | 2003–2026 | M3 step 5 (§3 row 14) |
| 12 | Matched duel: level the field and state the residual tilt | 44 | 1993–2026 | M4 evidence and correction (§3 row 15) |
| 13 | Bias-signed evaluation when the counterfactual is unobservable | 25 | 2013–2026 | M5 checkpoint (§3 row 20) |
| 14 | Counterfactual replay against the owner's historical decisions [S206 pp. 9, 12; S325 pp. 7–9, 13–14; S444 pp. 10–21; S682 pp. 2–7] | 25 | 1999–2026 | M5 evidence |
| 15 | Score the decision, not the prediction; audit the field's metric [S095 pp. 4, 12; S162 pp. 10, 13; S679 pp. 2, 12–14; S522 pp. 7–9] | 24 | 2008–2026 | M5 evidence |
| 16 | Optimize what practice randomizes or samples | 16 | 2014–2026 | Taste mark 3 and anti-pattern row evidence |
| 17 | Cutting planes over the binary support as the scaling engine [S061 pp. 3, 6–10; S175 pp. 9–10; S136 pp. 9–13; S093 pp. 10–14] | 33 | 2009–2026 | M4 engine; M1 variant (§3 row 6) |
| 18 | Class-keeping devices (robust = nominal; separation = nominal; dense tractable classes) [S014 pp. 1, 4–5; S045 pp. 2–4; S239 pp. 1–2, 8] | 38 (+1) | 1988–2026 | M1 step 3 evidence |
| 19 | Formulation strength compared and engineered | 13 | 1991–2025 | T4 narrowed (§3 row 18) |
| 20 | Own earlier result's limit as the entry point [S068 pp. 2, 5–6; S192 pp. 5–6; S440 pp. 1–2; S456 pp. 3–4; S457 pp. 2–3] | 19 | 1994–2026 | M6 and H7 evidence; too generic for a heuristic |
| 21 | Staged and revised publication of one model | 19 (+8) | 1988–2026 | Writing moves (§7.4) |
| 22 | Ship a usable tool with the paper | 15 (+4) | 1994–2026 | Workflow E evidence; installable-code correction (§3 row 15) |
| 23 | Design for adoption: implementability first, staged deployment, impact studies | 33 | 2002–2026 | M5 step 6 (§3 row 21) |
| 24 | Exact solves where they fit: small exact optima certify heuristics; MIO inside the search | 38 | 1995–2026 | H3 refinement (§3 row 31) |
| 25 | Heuristic-search design and yardsticks (HS) [S328 pp. 3, 9–10; S116 pp. 3–5, 12–13; H002 pp. 8–9] | 5 | 2008–2023 | HS row (§3 row 4) |
| 26 | Learn or distil the optimizer; math programming inside DP [S070 pp. 3–5; S034 pp. 8–9; S106 pp. 7–9; S112 pp. 2, 10, 14] | 32 (+2) | 2002–2026 | H5 evidence |
| 27 | Interpretable models as instrument: audit, validation, questionnaires [S285 pp. 3–4, 8; S396 p. 2; S430 pp. 1–2] | 22 (+7) | 1992–2026 | Taste mark 5 (§3 row 27) |
| 28 | Clinical ML engineering moves (multimodal pipelines, staged models, label hygiene) | 32 | 2007–2026 | Technique inventory only |
| 29 | Validation cascade: external, temporal, multi-site, negative controls | 16 | 2016–2026 | Technique inventory; M5 step 6 evidence |
| 30 | Collaboration roles | 12 (+2) | 2021–2026 | §9 |
| 31 | Computation as an instrument: regime maps, phase transitions, where the time goes | 21 | 1988–2026 | M4 step 6 evidence |
| 32 | Knob setting and pricing | 25 | 2001–2026 | M3 correction (§3 row 12) |
| 33 | Large deviations, fluid models and stability as optimization (SD) [S819 pp. 12, 16, 20, 24; S147 pp. 3–5, 8; S140 pp. 5, 12, 18–20] | 10 | 1994–2017 | M1 SD evidence |
| 34 | Writing and positioning moves | 25 (+2) | 1993–2026 | §7.4 |

---

## 7. Technique inventory

### 7.1 Proof devices

- **Duality collapses an inner maximization into a single-level counterpart**: inner maximum over a budgeted set dualized [S004 pp. 5–6]; double dualization of each player's robust LP into an equilibrium system [S029 pp. 23–25]; dual-norm lemma for margins, logistic exponents and splits [S104 pp. 9–12]; Fenchel duality with support functions and conjugates [S867 pp. 16–18]; an LP that replaces sorting for quantile quantities [S031 pp. 15–16].
- **LP duality for lower bounds in stochastic combinatorial problems**: node potentials and a transportation dual [S048 pp. 29, 33–39]; an LP dual lower bound in a priori routing [S102 pp. 7–8].
- **Conservation laws → extended polymatroid; greedy optimality by LP duality; indices as sums of duals** [S185 pp. 8–12; S057 pp. 11–12].
- **Relaxation hierarchies by interaction order**, polynomial for fixed order and exact at the top [S185 pp. 22–24; S051 pp. 6–7; S368 pp. 4–8; S072 pp. 20–22].
- **Potential functions generating polyhedral constraints** [S185 pp. 34–40; H010 pp. 10–11]; **stability LPs whose feasible points are Lyapunov functions with tail bounds** [S181 pp. 9–12; S123 pp. 12, 19–25].
- **PSD moment-matrix strengthening and moment hierarchies with two-sided convergence** [S185 pp. 44–45; S255 pp. 7–9; S413 pp. 4–5; S499 pp. 4, 14–15].
- **Extremal distributions certify tightness; worst-case distribution read from the dual** [S018 pp. 6, 19–21; S053 pp. 4–10].
- **Probabilistic analysis**: Steele's subadditive Euclidean functionals glued through always-present representatives plus Chernoff concentration [S038 pp. 7–8, 12–14; S048 pp. 58–63]; a dependency-graph CLT after conditioning on a high-probability event [S126 pp. 4–6, 10–12].
- **Heavy- and light-traffic bounds over all policies** via a tagged demand and Wald's equation [S016 pp. 5–11; S032 pp. 3–15; S091 pp. 11–17].
- **Large deviations as optimal control**: the most likely path as the optimizer, reduced to a root of a convex function [S819 pp. 12, 16; S147 pp. 3–5, 8; S187 pp. 9–12].
- **Rounding**: one shared random threshold [S658 pp. 18–20; S256 pp. 4–5, 8–9]; correlated rounding reproducing LP terms in expectation [S121 pp. 3–9]; covariance rounding of an SDP solution [S007 pp. 33–35]; designed distributions derandomized by breakpoint enumeration [S435 pp. 3–6].
- **Tight instances**: symmetry and a forced repeating step [S161 TR pp. 3–5; S289 pp. 7–11]; layered instances for greedy [S108 pp. 7–8]; parallel-arc families [S191 pp. 7–8].
- **Complexity reductions**: EXACT COVER BY 3-SETS for the PMST [S048 pp. 33–38]; copositivity for separation [S018 pp. 16–17; S056 pp. 13–15]; ∃R-completeness via a projection-matrix lift [S250 pp. 9, 41].
- **Exact reformulations for cutting planes**: a closed-form inner problem gives a convex integer program without big-M [S061 pp. 6–10; S095 pp. 4–7]; z² = z linearizes a ridge term [S175 p. 9]; closed-form Benders cuts at integer masters and a greedy primal–dual pair at fractional ones [S093 pp. 10–13]; big-M constants from auxiliary programs or the rival field's theory [S010 pp. 13–17; S250 pp. 18–19].
- **DP with structure kept**: linear-quadratic recursions in closed form [S009 pp. 44–47; S145 pp. 4–5]; Pontryagin reduced to a per-instant LP whose dual gives an index rule [S681 pp. 7–8].
- **Exchange arguments** [S001 pp. 4–5; S048 pp. 49–53; S327 pp. 13–15] and **counterexamples fencing a claim** [S014 pp. 9–10; S028 p. 7; S029 p. 16].

### 7.2 Design moves

- **A priori solution plus a trivial update rule, priced against re-solving** [S048 pp. 12–13; S038 pp. 1–2, 8–9; S017 pp. 1–3].
- **A dense tractable distribution class** (Coxian, rational transforms) so the analysis closes [S239 pp. 1–2, 8, 12; S168 pp. 3, 8, 12–15].
- **Budget sets that keep the nominal class**; robust 0-1 problems as nominal subproblems [S001 pp. 3–4; S004 pp. 4–7; S027 pp. 3, 7].
- **Uncertainty sets from a primitive the user can defend**: limit laws [S065 pp. 5–10; S119 pp. 7–10], a risk measure [S024 pp. 2–5], a hypothesis test [S013 pp. 3–4, 10], the predictor's loss [S440 pp. 3–9], the worst data split [S543 pp. 4–12].
- **Aggregate, then disaggregate only where coupling needs it** [S043 pp. 4–5; S253 pp. 7–10].
- **Inner-easy, outer-hard decomposition**, the inner problem solved in closed form or as a convex program, the outer choice combinatorial [S151 pp. 7–8; S288 pp. 5–6, 23; S432 pp. 4–5; D017 pp. 6–7].
- **Nest the incumbent rule as one setting of the knob** [S076 p. 17; S199 pp. 5, 8, 17–18; S104 pp. 9, 13, 17].
- **Adoption term**: penalize distance from the status-quo schedule [S416 pp. 8, 14, 32].
- **Learned models embedded exactly as MIO, inside a trust region of the data** [S097 pp. 13–15; S298 pp. 3–4, 14–19; S266 pp. 7, 9].
- **Solutions as labels**: compress an optimum to a strategy and learn it [S112 pp. 2, 10, 14, 17; S204 p. 3; S267 pp. 9–10].
- **Optimize the assignment or the training sample instead of randomizing** [S124 pp. 4, 7; S312 pp. 1–2, 22; S873 pp. 3–8; S696 pp. 6–8, 10].
- **Backbone and MIO-as-move local search** [S046 pp. 22–26; S137 pp. 3–4].
- **Interpretability by constraint**: one shared support across leaves [S459 pp. 2–6].

### 7.3 Experiment and evaluation protocols

- **Bound-referenced yardstick**: report every policy as a ratio to a relaxation bound [S072 pp. 26–31; S070 p. 9; S207 pp. 12–16] (Method 7).
- **Matched duel with the tilt stated** [S114 p. 12; S340 pp. 16, 23; S095 pp. 11–12, 23; S474 pp. 4–5, 8; S680 pp. 6, 11–14] (§3 row 15).
- **Misspecification duel** (§3 row 14) and **outside-the-set stress tests** [S278 pp. 5–6; S053 pp. 16–22].
- **Counterfactual replay against the owner's historical decisions** (§6 cluster 14).
- **Bias-signed proxies** when the truth is unobservable (§3 row 20).
- **Report time to the best solution apart from time to proof** [S445 p. 24; S488 pp. 25–27; S907 pp. 23–26, 35–38; S184 pp. 25–36].
- **Regime maps and phase transitions**: the exact solver as an instrument [S061 pp. 4, 14–19]; more data makes the exact problem easier [S355 pp. 4–5, 13–15; S170 pp. 5, 17, 20]; where optimization pays [S046 p. 19]; a fitted when-to-use rule [S104 pp. 4, 25–27; S011 pp. 30–35].
- **Check asymptotics by simulation at small n**, with a stated stopping rule [S829 pp. 13–17; S080 pp. 14–18; S016 p. 12].
- **Scale test before trusting a small-n result** [S048 pp. 121–123].
- **Feasibility-border instances** [S015 p. 11; S068 pp. 31, 39; S241 p. 30; S275 p. 25].
- **Where the time goes, step by step** [S291 p. 13; S168 pp. 15–16; S316 p. 11].
- **Validation cascade**: external sites with per-site thresholds [S054 pp. 2–3, 5, 8], a hospital abroad [S325 pp. 3–4, 9; S615 pp. 7, 19–21], temporal external validation [S678 pp. 6, 15], three-tier validation with negative controls [S680 pp. 2, 6–9, 12–15].
- **Field impact studies** by difference-in-differences [S115 pp. 22–24; S617 arXiv pp. 22–25].

### 7.4 Writing moves

- **Field-contrast opening**: the neighbouring field's plan of attack against this field's ad hoc state [S185 pp. 1–3; S051 p. 1].
- **Programme abstract**: practice, belief, figure, method [S081 p. 2; S010 p. 1; S093 p. 2] (H9).
- **Print looseness and conjectures beside the theorem** [S016 pp. 7, 9; S032 pp. 7–8, 11, 16; S158 pp. 15, 17; S323 pp. 2, 13, 17–18].
- **Close with a complexity map and numbered open problems** [S185 pp. 49–51].
- **Staged companion papers from one model**, including a bounds paper and a policies paper [S098 pp. 2–3; S072 p. 2; S004 pp. 4, 16–17, 22; S019 pp. 1–2, 4–5; S234 p. 1; S305 p. 3].
- **Claims narrowed from working paper to journal** [S833 pp. 6, 9, 15–23; S186 pp. 2, 16–17; S261 pp. 7, 14, 20, 26].
- **A dated proof-repair note that keeps the published statements** [S747 p. 1].
- **Integration section** mapping the model onto the owner's process [S076 pp. 22–23; S245 pp. 11–13].
- **Adoption post-mortem** in print [S262 p. 12].
- **A usable tool released with the paper** [S190 pp. 1, 4–5; S094 pp. 1, 10; S325 p. 11; S395 pp. 5, 9; S615 p. 22].
- **Claims graded by their evidence** ("a fair conclusion"; analytical evidence) [S017 pp. 11–12].

---

## 8. Trajectory as seen in the full texts

### 8.1 Topics by period (works read in full or in part / all works with a card; domain codes from the cards' D1 tags, a work can carry several)

| Period | Works | LO | IO | RO | CP | SD | ML | DA | HS | AP |
|---|---|---|---|---|---|---|---|---|---|---|
| 1988–92 | 23/33 | 1/4 | 11/17 | 0/0 | 0/0 | 23/31 | 0/0 | 0/0 | 2/3 | 8/8 |
| 1993–97 | 34/47 | 13/19 | 14/20 | 0/0 | 6/6 | 22/29 | 1/1 | 0/0 | 3/3 | 14/18 |
| 1998–2002 | 34/46 | 13/13 | 16/18 | 1/1 | 7/8 | 21/26 | 0/0 | 0/2 | 1/1 | 15/19 |
| 2003–07 | 36/50 | 16/17 | 12/16 | 15/20 | 18/19 | 17/20 | 3/3 | 5/5 | 3/3 | 21/25 |
| 2008–12 | 36/47 | 3/4 | 16/18 | 21/23 | 7/8 | 7/8 | 6/7 | 3/6 | 4/5 | 25/28 |
| 2013–17 | 55/60 | 14/14 | 31/34 | 24/26 | 8/8 | 6/6 | 17/19 | 13/16 | 7/7 | 33/37 |
| 2018–22 | 128/156 | 10/10 | 63/71 | 31/33 | 19/22 | 8/10 | 92/112 | 39/56 | 11/11 | 84/98 |
| 2023–26 | 116/137 | 10/10 | 48/49 | 38/41 | 20/22 | 9/9 | 85/96 | 52/57 | 11/11 | 74/84 |

### 8.2 Turns

1. **1988–1993, probabilistic combinatorial optimization and queueing analysis.** The thesis problem class comes from his adviser's group [S048 pp. 18, 71, 125]; a priori optimization [S038 pp. 1–2], dense distribution classes for multiserver queues [S239 pp. 1–2; S168 pp. 1–2], and dynamic routing with van Ryzin after a colleague raised the problem [S016 pp. 1, 14].
2. **1993–1995, from asymptotic constants to mathematical-programming relaxations of stochastic control.** The 1994 working paper names the dynamic and combinatorial character as the essential difficulty [S580 p. 10]; polyhedral and SDP relaxations of queueing networks [S072 pp. 2, 20–22]; the survey consolidates the cohort [S185 pp. 1–4].
3. **1995–2002, IO relaxations, rounding and moments.** Survivable networks [S052 p. 3]; randomized rounding read as probability [S121 pp. 3–9; S007 pp. 33–35]; moment bounds as SDPs [S007 pp. 9, 18; S056 pp. 2–15]; finance with Lo [S009 p. 3]; fluid scheduling [S130 pp. 2–3].
4. **2002–2007, budgeted robust optimization.** First Γ budget in a 2002 working paper [S653 pp. 12–14]; robust discrete optimization keeps the nominal complexity [S004 p. 22]; the price of robustness [S001 pp. 1, 3–5]; robust inventory [S014 pp. 1, 4–5].
5. **2008–2015, adaptive policies, data-driven sets and limit laws.** Power and limits of static and affine policies [S134 pp. 6, 12–18; S042 pp. 2–3]; sets from risk measures [S024 pp. 2–5]; limit-law sets [S065 pp. 5–10; S119 pp. 7–10]; fairness [S012 pp. 1, 14; S026 pp. 1–2].
6. **2014–2018, MIO for statistics and ML.** Tractability redefined by solve times [S178 pp. 3–5; S010 p. 2]; the why-now figure [S010 pp. 7–8; S081 p. 4; S011 pp. 5–6]; the prescriptive line [S008 pp. 10–12].
7. **2018–2022, clinical ML, COVID-19 and deployment at scale.** Clinical calculators with optimal trees [S190 pp. 1, 4–5; S231 pp. 3, 8]; DELPHI [S103 pp. 2–3]; HAIM [S023 pp. 1, 3]; hospital operations [S115 pp. 2, 19–24].
8. **2023–2026, multimodal AI, LLMs, global optimization and education.** xHAIM [S390 pp. 1–2]; LLM-assisted modelling [S330 pp. 1–4]; a group global-optimization solver line [S624 pp. 10–16; S415 pp. 19–20]; field roll-outs [S617 arXiv pp. 11–14]; teaching tools under the Open Learning role [S667 pp. 4–5, 7].

### 8.3 What stayed constant

- **Bound before policy** across all periods (Method 7, 79 works).
- **Re-derive classical results before extending** across all periods (H10, 80 works).
- **Class-keeping formulation** (M1: 210 works with evidence links, 1988–2026).
- **A priced trade-off handed to the decision-maker** from 1990 [S597 pp. 36–38] to 2026 [S668 pp. 4–8, 11].
- **Printed limits**: conjectures and loose constants in 1988–1993 [S048 pp. 100–101, 164–165; S016 pp. 7, 9], negative results in the body later (H4, 51 works).
- **Programmes carried by students and former students** (M6, 194 works).

What changed: the meaning of tractable (complexity class and asymptotic constants in 1988–1997 [S289 pp. 2, 6, 11–12; S269 pp. 1, 21–22], measured solve times by 2004–2016 [S001 p. 8; S010 p. 2]); scarce computation favouring simple a priori policies in 1996 [S025 p. 17] became abundant computation favouring exact MIO [S010 pp. 7–8]; sole authorship gave way to teams (§9); theory papers gave way to deployments with partners (§3 row 5).

---

## 9. Collaboration pattern

Counts come from the cards' coauthor fields (surnames merged; same-surname coauthors separated where the full names differ). They are approximate.

| Period | Works | Median coauthors | Sole-author works | Most frequent coauthors (works) |
|---|---|---|---|---|
| 1988–92 | 33 | 1 | 11 | van Ryzin 5, Nakazato 4, Papaconstantinou 3, Goemans 2, Odoni 2, Avram 2, Jaillet 2 |
| 1993–97 | 47 | 1 | 4 | Tsitsiklis 9, Odoni 7, C.-P. Teo 5, Avram 4, Paschalidis 4, Gamarnik 3, Peterson 3, Mourtzinou 3 |
| 1998–2002 | 46 | 1 | 0 | C.-P. Teo 6, Tsitsiklis 6, Lo 5, Gamarnik 5, Vohra 4, Popescu 4, Paschalidis 4, Sethuraman 3 |
| 2003–07 | 50 | 1 | 4 | Natarajan 6, Caramanis 5, Sim 5, C.-P. Teo 4, Perakis 4, Thiele 4, Doan 3 |
| 2008–12 | 47 | 2 | 2 | Nohadani 5, Farias 4, Trichakis 4, Odoni 3, Brown 3, Caramanis 3, Doan 3, Goyal 3 |
| 2013–17 | 60 | 2 | 1 | Mišić 5, Bandi 5, V. Gupta 4, O'Hair 4, Kallus 4, Mazumder 4, Silberholz 4 |
| 2018–22 | 156 | 2 | 5 (editorials) | Dunn 18, Orfanoudaki 15, Zhuo 11, M. L. Li about 10, Wiberg 9, Pauphilet 9, Delarue 7, Kaafarani 6, J. Yan 6, Cory-Wright 6 |
| 2023–26 | 137 | 3 | 2 (editorials) | Y. Ma 14, Margonis 12, den Hertog 11, Pauphilet 10, Koulouras 10, Koukouvinos 10, Stoumpou 8, Kaafarani 7, Trichakis 7, Villalobos Carballo 7 |

Patterns the cards show:
- **Early sole authorship and co-advising**: nine sole-author SD works in 1988–1995 (§3 row 1); co-advised lines with Tsitsiklis [S072 pp. 1, 8, 10, 32–33; S237 pp. 1–3] and Odoni [S135 p. 1; S806 pp. 1–2] (the co-advising itself is in the DSpace advisor fields [04 A.2]; the papers show co-authored thesis lines).
- **Students carry programmes**: van Ryzin [S016 p. 1], Niño-Mora [S051 p. 11], Teo [S214 p. 11], Popescu [S007 p. 1], Sim [S001 p. 1], Dunn [S096 pp. 5–6], Pauphilet and Cory-Wright [S183 pp. 4–5, 19], Ma [S351 pp. 5, 12, 29], Koulouras [S527 pp. 2–4]. Former students return as co-authors on later stages of a programme [S476 p. 1] (*fix round*: *co-senior* withdrawn; the byline after the first author is alphabetical). The RO book co-author, den Hertog, co-signs the 2021–2026 robust and global-optimization lines [S215 pp. 21–23; S283 pp. 3–4, 15–19; S708 pp. 8, 14–15; S689 pp. 3, 16; S415 pp. 19–20; S836 pp. 4–5].
- **Partners as co-authors**: ISO New England staff [S006 pp. 1, 5–9]; an owner co-author [S245 pp. 2–3, 6–7]; UNOS staff [S476 pp. 1–2]; hospital partners [S617 arXiv pp. 1–2, 9, 28, 31; S683 pp. 1, 7].
- **Three roles in 2021–2026 health work**: the senior sponsor and editor of student-led lines outside optimization, stated in contribution sections [S299 p. 10; S132 pp. 1, 13; S478 pp. 1, 21; S682 p. 7; S618 pp. 1, 15]; the analytics partner inside a clinical team's study [S238 pp. 1–2; S707 pp. 1, 5, 11; S686 pp. 1, 13; S439 pp. 1, 8]; a contributing modeller in forecast hubs, where others write and score [S110 pp. 2, 17; S021 pp. 10–11; S157 pp. 21–22].
- **Company software as platform**: [S300 pp. 23–24; S308 pp. 2–3; H002 pp. 1–2, 8, 19; S677 pp. 1–3].

---

## 10. Rejected updates

1. **Promote "re-derive classical results" to a core method**: fails exclusivity; made Heuristic 10 instead (§5).
2. **Promote Heuristic 1 to a core method**: exclusivity partial, since the central equivalence is credited to others [S085 pp. 7–15]; stays a heuristic with full-text evidence.
3. **Add "matched duel" as a heuristic**: duplicates M4 step 5; recorded as evidence and as a correction of the "not his practice" label (§3 row 15).
4. **Add "price of simplicity" as a method**: it is Method 3 with X = simplicity (§3 row 11).
5. **Add "asymptotic regimes for sharp constants" as a method or heuristic**: period-bound (19 of 22 works before 2003) and part of Method 7's bound step; exclusivity weak.
6. **Add "carry a classical device into the stochastic or robust version" as a method**: robust and stochastic versions of known problems are common practice; evidence for M1 step 1 only.
7. **Add "own earlier result's limit as the entry" as a heuristic**: every programme does this; no explanatory power beyond M6 and H7.
8. **Add "misspecification duel", "bias-signed evaluation" or "design for adoption" as separate heuristics**: each is heuristic-eligible, but with ten heuristics at the cap they are better as steps of M3 and M5 (§3 rows 14, 20, 21).
9. **Add the clinical ML engineering moves (cluster 28) or the validation cascade (cluster 29) to SKILL.md**: domain-specific engineering, not research method; kept in §7.
10. **Use consortium and hub papers (S063, S110, S021, S157, S294) as evidence of his method**: rejected; they are external evaluation only.
11. **Add anything from reading notes on typos, internal inconsistencies or recomputed numbers**: rejected under the house rule.
12. **Drop Tension T4 or the formulation-strength blind spot**: rejected; narrowed instead, because tree MIOs and some ML models still use weak big-M forms [S225 pp. 5–9; S358 pp. 4–12; S097 pp. 44–45].
13. **Drop the M2 checkpoint because the figure is rarely rebuilt**: rejected; the checkpoint stays as the skill's rule, now labelled as such (§3 row 9).

---

## 11. Open gaps

- **Books**: *Introduction to Linear Optimization*, *Optimization over Integers*, *Data, Models, and Decisions*, *The Analytics Edge*, *Machine Learning under a Modern Optimization Lens*, *Robust and Adaptive Optimization*, the 2022 queueing book and *The Analytics Edge in Healthcare* are carded at abstract level only [S002; S020; S128; S209; S047; S084; S334; S695]. The LO voice and the stated philosophy behind the textbooks remain web-sourced.
- **The 2026 RO retrospective** with den Hertog is abstract-level [S614], so how Γ arose and why he entered RO remain unknown (§3 row 29).
- **Early adaptive-RO and robustness–regularization papers** are metadata-level [S789; S466; S560; S462; S424]; H1's origin before 2011 rests on the 1998 DP-form case [S009 pp. 4, 9–10] and the 2011 survey [S003 p. 37].
- **Part of the 1992–1999 achievable-region series** is abstract- or metadata-level [S587; S468; S507; S581; S656; D007; D008; S798]; Method 7's SD evidence rests on the surveys [S185; S580] and the papers read [S072; S057; S051; S368; S130; S205; H010; S212].
- **Clinical validations** of the trauma and emergency-surgery calculators are abstract-level [S179; S188; S226; S242; S041; S633; S277; S270; S529]; whether they score decisions (M5) is unknown.
- **Editorials and special issues** (venue editing under M6) are metadata-level [D011; S491; S371; D015; D016; S637; S719].
- **Journal versions** of works read as preprints or arXiv versions (§1) and unread e-companions (for example the proofs of the product-line paper [S093 p. 1]) may differ.
- **Pre-start impact gate** (M6 step 1) and supervision routines (H8) cannot be observed in papers; they stay with notes 02 and 04.
- **160 skipped rows** (students' theses, reports, other people's works) were not read; students' voices about supervision stay in note 04.

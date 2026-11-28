# Tobias Achterberg · Deep-reading synthesis (08)

> Synthesis of all paper cards in `cards/` (index: `07-paper-cards.md`), written 2026-11-28 for the team-synthesize stage (T3.6). It is a proposal for a conservative update of `SKILL.md` under the house rules (paper-reading-card.md §3; research-extraction-framework.md §3 and §11): only add; mark contradictions instead of deleting; existing methods get evidence, not duplicates; a new core method needs at least three distinct works read in full or in part plus the four-way validation; updates that add no explanatory power are rejected. `SKILL.md` itself is not edited here. Fix round (2026-11-28, after three reviewers checked the update): the Voices line below, §2 Method 3's proposed text, §2.7 (Misreading 5, Inner Tensions), §3.2 items 6, 10, 14 and 16, §8 and §9 were corrected against the texts; the ledger's copies were updated alike.
>
> **Citation form.** `[R004 p. 17]` is the `[[page N]]` page of the file listed for that ID in `../sources/papers/INDEX.md`. Three works were read in a report version and carry the word TR: `[D017 TR p. 15]` (ZIB-Report 13-66, revision of April 2014), `[D018 TR p. 14]` (ZIB-Report 15-53, revision of February 2016) and `[D024 TR p. 15]` (ZIB-Report 02-16, March 2002, where he is listed under his former name, Tobias Pfender). D022 was read as arXiv 2211.13545v1 and D023 as arXiv 2211.13545v3; these are the files indexed for them. Abstract- and metadata-level cards are cited by ID only. **To compare with SKILL.md's printed-page keys:** thesis file page = printed + 14 (front matter equal); ZIB-Reports 02-16 to 10-27 (R001–R014, D024 TR): file = printed + 1; ZIB-Reports 10-31 to 20-16 (R015, R017–R022, D017 TR, D018 TR): file = printed + 2; RAMP 2014: file = printed − 180; the edited collection R016 has its own offset (card s01).
>
> **Voices.** Four full texts are sole-authored, all 2004–2009: R003 (ZR 04-19), R004 (ZR 05-19), the thesis D004 and D010 (MPC 2009). Everything else is co-signed; apart from one part a text names as his ("Achterberg's heuristic" [D026 p. 7]) and the variability work MIPLIB 2010 credits to Danna [R015 p. 22], no co-signed text states roles. The ParaSCIP texts (R014, D029/R018, R019/D017, R020/D018, R022) have Shinano first; nothing in them is claimed for Achterberg alone. Gurobi work after 2014 is closed code; its papers are the only window.
>
> **Counting.** One text per work: the published versions D001, D002, D003, D005, D007, D008, D014, D015 and D019 have no text of their own; their ZIB-Report rows R002, R005, R004, R006, R009, R010, R014, R017 and R021 hold it. Report and published pairs with separate texts are one study each: R019 and D017, R020 and D018, R018 and D029, R013 and D011, R015 and D013. D022 (IPCO 2023) and D023 (its extended journal version, 2025) are two works of one study line; where a cluster's count depends on it, this note says so. D024 has two cards; the round-2 card (c2-01, full) supersedes the round-1 card (c01, unreadable as named).
>
> **Not carried.** The cards' reading notes on inconsistencies inside a work (a table that disagrees with its text, a typo, numbers that look carried over) are not findings about the researcher or his coauthors and do not enter this note; §7.4 keeps one neutral lesson. Material sealed in `holdout.md` is not used: no point, quote or decision of a sealed item appears here, and the pages that carry them are not cited. One candidate cluster and one single-card candidate that lean on sealed material are withheld (§6).

---

## 1. Coverage

| Item | Count | Source |
|---|---|---|
| Card entries | 54 in 13 batch files: round 1 b01 (1), c01–c08 (24), s01–s02 (11); round 2 a2-01 (17), c2-01 (1) | digests; 07 |
| Read level | full 34 · partial 2 (the thesis at chapter level; the preface of an edited collection) · abstract 11 · metadata 6 · unreadable 1 (the superseded round-1 card of D024) | digests |
| Works with a card | 53 of the 55 indexed works; the two without are Role = skip (patents D031, D032) | INDEX.md after `mark_read_from_cards.py`: carded 34, skimmed 2, abstract 11, metadata 6, — 2 |
| Coverage row (`team_status.py`) | 0 Scholar rows · 55 distinct works indexed · 36 open full texts · 34 read in full · 2 in part · 11 abstract only · 6 metadata only incl. unreadable · 2 skipped · 0 book material · 84 quotes verified | 07 |
| Quote gate (2026-11-28) | 84 quotes: 84 exact, 0 equal up to spacing or symbols, 0 not found | `verify_card_quotes.py` |
| Open texts | every one of the 36 files with text has a full or partial card | INDEX.md |
| Studies after merging pairs | 39; 31 with a full or partial text; 8 at abstract or metadata level only (D036, D025, D006, D009, D012, D027, D016, D028) | this note |
| Method links | 152 link entries on 41 cards: 35 of the 36 full or partial cards (R016, an edited collection, has none) and 6 abstract cards (D007, D009, D016, D028 as evidence; D014, D015 as variants). The digests link Methods 1–6 only; heuristics, misreadings and taste marks are named in card prose (§2.7) | digests |
| Pool material | 96 new-pattern-candidate entries on 40 cards; 162 proof-device entries (154 on full or partial cards); 222 transferable-technique entries (214 on full or partial cards) | digests |
| Full or partial cards by period | 2000–04: 4 · 2005–09: 13 · 2010–14: 11 · 2015–19: 3 · 2020–24: 4 · 2025: 1 | digests |

**What the reading changes in scope.** The skill was built from web research, the SCIP history, talks and a partial read of the ZIB-Reports. The cards now cover every open text: the whole report series 2002–2020, the journal texts of the 2009 SCIP paper, the Mcf-separator, MIPLIB 2010 and 2017, the ParaSCIP papers, the 2014 RAMP paper, the 2021 feedback-arc-set paper, both RLT versions, the 2009 distillation paper, the 2002 UMTS report and the thesis at chapter level. The CPLEX-era non-report works (D006, D009, D016, D027, D028) and all journal versions of the reports remain abstracts or metadata (§11).

---

## 2. Evidence per existing method

Counts are distinct cards whose digest links the method (E = evidence, V = variant, C = contradiction; a card can carry an E and a V link). *Studies* merges the report and published pairs of the header. *E by period* counts evidence cards in 2002–05 / 2006–09 / 2010–13 / 2014–25.

| Method | Cards (E / V / C) | Studies | Full or partial cards | E by period | Say–do after the full texts |
|---|---|---|---|---|---|
| M1 Do-no-harm default gate | 17 (10 / 11 / 1) | 15 | 17 | 1 / 3 / 2 / 4 | ✅ stated (co-signed) + practised; the matrix-detector form from 2009; the thesis decides defaults on a weighted total without a detector |
| M2 A proxy is not a payoff | 28 (22 / 7 / 1) | 23 | 27 | 4 / 7 / 5 / 6 | ✅; step 1's rule that a time loss goes into the abstract holds for the 2005 report, not for the later abstracts |
| M3 Nest the incumbents and sweep | 11 (5 / 7 / 0) | 10 | 11 | 2 / 2 / 1 / 0 | ✅ for 2002–2009; no written practice after 2013 |
| M4 Knock-out from the default, read in brackets | 29 (15 / 16 / 9) | 24 | 28 | 1 / 4 / 5 / 5 | ✅, with three corrections (Example A.1 signs, era line, seeds) |
| M5 Instrument first | 26 (18 / 9 / 1) | 22 | 25 | 4 / 5 / 4 / 5 | ✅; the test-set selector changes by era |
| M6 Import at the data-structure level | 17 (10 / 9 / 0) | 16 | 14 | 2 / 7 / 1 / 0 | ✅ for 2003–2013; later imports come from network design and global optimization |

### Method 1 · The do-no-harm default gate

- **Strongest practice.**
  - The canonical case, now read in both versions: a detector on the matrix with a numeric fit (minority votes per arc, averaged over arcs), a no-op path when the fit is poor, tuning aimed at not slowing general MIPs, the three numbers reported (target sets, public general sets, a broad CPLEX-internal set), unaffected rows near 1.00, the `modeltype` parameter detected automatically by default, and conservative defaults kept against class gains [D011 pp. 11, 19–20, 24, 28–34, 37–38; R013 pp. 2–4, 10, 23, 28–30].
  - Gurobi presolve gates: full-LP redundancy only in special situations, OBBT only for selected variables, local symmetry recomputed only when the matching structure is detected; the redundancy checks and the multi-column dual-fixing extension stay off [R021 pp. 27, 28, 36, 40, 62; D030 pp. 4, 9, 12].
  - Thesis: the hybrid branching default keeps inference branching's gains on alu and acc and equals reliability branching elsewhere [D004 p. 84]; per-call guards turn RENS, root restarts and reduced-cost bounds into no-ops when they are unlikely to pay [D004 pp. 125, 132–133, 174].
  - 2022–2025: a detector of implicit products on pairs of linear rows, checked in a second, independently written solver on a class-balanced Gurobi set [D023 pp. 5–9, 21–22; D022 pp. 5–7, 14].
- **Stated (co-signed).** The Bixby–Rothberg remark is quoted as the design rule [R013 p. 2; D011 p. 2]. A new algorithm rarely helps all instances, costs effort to decide when to run it, and can slow instances solved before, so a general solver is re-tuned on a large set that includes formerly fast instances [D029 p. 2]. "Average performance on this set is not a suitable criterion to decide which MIP solver to use in a particular application scenario." [D021 p. 3].
- **Say–do update.** ✅ unchanged. Era: the matrix-detector form starts with the Mcf-separator (2009–2010); in the thesis, defaults are decided on the pseudo-instance-weighted total and per-set losses are accepted [D004 p. 336; D010 pp. 17, 19–20].
- **Variants.** Refusal thresholds inside a parallel technique (merge only above 0.9 shared fixings; undo a merge on any bound loss), with no detector and no harm measurement [D018 TR pp. 11–13]; a parallel default chosen for stability over runs and its trend with scale rather than for the faster mean, a choice the authors call difficult [D029 pp. 21, 26; R018 pp. 19–21]; a problem-specific method that runs the class it was not built for on purpose and prints the loss [D020 pp. 16–17]; implicit-product cuts end in a class split without a detector of the paying classes, the SCIP set keeps only instances where the component acts, and the two codes differ on MILPs overall [D023 pp. 13, 15–16, 21–22; D022 pp. 10–11, 14]; the gate study itself changed between the report and the journal version (§3.3).
- **Contradiction (partial).** Components stay on with no measured gain: Chvátal–Gomory strengthening, simple probing on single equations and biconnected components are neutral, and global probing at nodes stays on although the default has 36 time-outs against 14 without it; the authors say the test measures only the extra probing in the tree [R021 pp. 14, 18, 56, 65]. Step 5 (*Neutral or better elsewhere → on*) allows this; Taste mark 1 does not.
- **Proposed text.** Practice: cite the journal version beside the report for the gate, with the version note of §3.3; add the three neutral-on components to the counter-example list. New step 0 from §5 B (validity first). Step 5: when two codes disagree on the general set, no default is stated in the 2022–2025 study [D022 p. 14; D023 pp. 21–22]; the rule as written would leave it off.

### Method 2 · A proxy is not a payoff: split the time, then budget

- **Strongest practice.**
  - The source of the time split, read in full: basic, switching and conflict time per instance with clause counts and lengths; the dominant cost (continuing bound-exceeding LPs) and the side cost (switching) named; an IIS heuristic and one algorithm step dropped for their cost [R004 pp. 11, 15–18]. The card's recount supports SKILL.md's *inferred* checkpoint per instance: on 17 of 29 instances the component's time plus the added switching time exceeds the basic-time saving [R004 pp. 17–18].
  - Thesis: full strong branching gives the smallest trees and is about 100 % slower on the mixed sets [D004 pp. 83–84]; local cuts at every node give −70 % nodes and +137 % time [D004 p. 129]; bound-exceeding and full conflict analysis cut nodes but not time [D004 pp. 194–195]; budgets set in solver units throughout [D004 pp. 78–80, 171, 193].
  - Gurobi era: probing limits counted in touched non-zeros and scaled by success, local probing driven by work and success ratios, a capped conflict pool with aging [R021 pp. 49, 64, 66]; the node column locates where time goes (cleanup and cancellation gain through faster LPs, a dependent-row loss through larger trees, not factorization) [R021 pp. 9, 28, 33; D030 pp. 12–13].
  - RLT: the root-bound gain is printed beside the time loss, "although this does not always translate into an improvement in overall solver performance" [D023 p. 16]; separation's share of total time cut from about half to under 3 % on MILPs [D022 p. 13; D023 pp. 17–18]; budgets in solver units [D022 p. 10; D023 p. 13]; "We observe a slight increase in time when RLT cuts are enabled, and a slight decrease in number of nodes." [D022 p. 11].
  - Elsewhere: node counts never read as speed [R011 pp. 7–8]; speed-ups read as nodes times throughput [D010 pp. 17, 20, 29, 36]; the classroom form (find the component that takes the time, ask what it buys for this class, switch it off) [R007 p. 7]; co-signed phase splits of parallel runs [D017 TR pp. 13–15; R019 pp. 5, 11, 13–14; R020 p. 13; D029 pp. 16–17, 20, 28; R018 pp. 17–18].
- **Say–do update.** ✅ unchanged.
- **Variants.** The thesis does not split time into base, switching and component time; it reads overhead from whether node and time changes move together [D004 p. 194] (proposed step 2 alternative below). In 2005 the only budget was aging; the cap of ten conflicts per infeasible subproblem appears in 2007 [R004 pp. 15–16; D004 p. 193]. The payoff is redefined for primal heuristics, with a measure of their own [R017 pp. 3, 5–7; D015], and for record-seeking parallel work, where strong scaling is rejected as a measure [R022 pp. 6, 20]. A co-signed load-balancing study names its dominant cost by phase but controls it with wall-clock periods, not work units [D018 TR pp. 8–9, 14].
- **Contradiction (co-signed).** The 2008 abstract calls SCIP almost competitive on solved counts (33 against 34) while CPLEX is at least 10 % faster on 27 of 36 instances [R009 pp. 2, 10]. Step 1's rule (a time loss goes into the abstract) is met by the 2005 conflict report [R004 p. 2] and not by later abstracts (§2.7, H10).
- **Proposed text.**
  - Practice: the conflict-analysis configuration is the thesis's experiment setting, not a stated default, and SCIP 0.90f was benchmarked with conflict analysis off by default (§3.2 item 4).
  - Step 2 alternative, when no component timer exists: split time into a count and a unit cost (nodes × time per node; iterations × cycle time), write down before the run which factor the change should move, then report both ratios [D026 pp. 8–9, 15, 32–34, 39; D004 pp. 84, 194; D010 pp. 29, 36; R011 pp. 7–8].
  - Step 2b from §5 C (hardness first, then the cheapest surrogate).
  - Limitations: the primal integral's first written form is co-signed by him in 2011 (§3.2 item 8).

### Method 3 · Nest the incumbents in one parameter family and sweep it

- **Strongest practice.** The 2004 family: pseudocost, strong-branching-initialised and full strong branching as settings of one reliability parameter, the map drawn, the full grid run, each setting a point in (nodes, time), the knee named rather than the fewest-node setting, and the simplification against the 2002 rule as the result [R002 pp. 8, 11, 13, 17]. Thesis: the same family with its budget tied to node-LP iterations, the hybrid rule reducing to reliability branching at zero weights, and the product score tested against the weighted sum at five weights [D004 pp. 79–83, 85; D010 pp. 16–19]. The pump: "Note that you can obtain the original Feasibility Pump by choosing α0 = 0." [R006 p. 5].
- **Say–do update.** ✅ for 2002–2009. The co-signed 2013 parallel study keeps step 2 only (schemes as settings of one code, no sweep) [D029 p. 21]; the 2022–2025 RLT study uses single parameter values with no sweep (card note; [D023 pp. 13, 18]). No Gurobi-era text exercises the method.
- **Variants.** The 2002 rule is a bundle of changes evaluated as a whole [R001 pp. 8–10]; one setting against the endpoint, no grid [R006 p. 6]; one-parameter sweeps whose default is set conservatively, not at a knee [R013 pp. 28–29; D011 pp. 35–38]; a family of activity-bound computations with a chosen compromise and no sweep [D030 pp. 8–9]; a factorial over formulation choices read by per-level means [R011 pp. 5, 7–8]; an extended model row that contains the basic row at parameter zero, unremarked [D024 TR p. 19].
- **Proposed text (Limitations).** *the knee moves (dynamic by 2007 …)*: dynamic reliability settings were already run in 2004, in appendix tables only, undefined in the text, from about 1 % faster to 14 % slower than (8, 4) in geometric-mean time [R002 pp. 30–31, 37–40]. A timing-noise data point for 2004: a second run of one setting without a time limit differs by up to 7.1 % in time on single instances at identical node counts [R002 pp. 12, 18–19, 23] (neutral lesson for step 3: treat settings within timing noise of the knee as ties).

### Method 4 · Knock-out from the default, read in brackets

- **Strongest practice.**
  - Thesis form: shifted-geometric-mean ratios against the default (shift 10 s and 100 nodes), counts of instances at least 10 % faster or slower, equal- and different-path blocks, the pseudo-instance-weighted total, time-outs at the limit with the bias stated [D004 pp. 16, 333, 335–336, 339–340]; all off / one off / one on alone for interacting families [D004 pp. 125, 142].
  - 2009–2010: unaffected and affected rows per set, wins at ±10 %, time-outs per side, conclusions refused on 16 and 3 affected public models and accepted on the large set [R013 pp. 24–27; D011 pp. 29–30, 33–35]: "In contrast to Table 3 and Scip we can trust these values since the overall testset is very large with a reasonable number of affected instances." [D011 p. 34].
  - 2014: the bracket table with shift 1, affected models by simplex iterations, inconsistent answers excluded: "In the discussion below, we will usually use the [10,10k] bracket, because this excludes the relatively uninteresting easy models but is still large enough to draw meaningful conclusions." [D030 p. 11].
  - 2016, the fullest written form: master-solve-only switches with the reason, no benchmark where a change acts through model size, no affected figures where both sides time out, small affected sets refused or rechecked [R021 pp. 5–6, 19, 21–22, 40, 42]: "one has to take this result with care, as a set of about 200 models is usually not large enough to measure such an impact precisely enough." [R021 p. 42].
  - 2021–2025 (co-signed): "The means were computed with a shift of 1 second (see Achterberg [1])." [D021 p. 2]; brackets [x, timelim], affected and all-optimal subsets in SCIP and the same bracket rows in Gurobi [D022 pp. 10–11, 14; D023 pp. 14–22, 26–27]; four settings for an interacting heuristic family [R017 pp. 6–7].
- **Contradictions** (details §3.1): the signs of Example A.1 [D004 pp. 335–336]; the era of the bracket form [R013 pp. 26–27; D011 pp. 33–34]; seeds and permutations in co-signed written studies [R015 pp. 13–15; D013 pp. 13–18; D029 p. 20; R018 pp. 16–17, 19–21; D023 pp. 14, 26–27]; one-instance verdicts in record-seeking parallel papers [D018 TR pp. 13–14; R020 p. 13].
- **Variants.** Earlier forms: arithmetic totals over a pairwise comparison [R001 p. 11]; totals and plain geometric means against two external solvers [R003 pp. 24–25]; plain geometric means and fails per setting [R002 pp. 17, 19]; on/off in the default with plain or floored means and both-solved subsets [R004 pp. 16–17, 19]; unshifted means with 10 % counts in solver comparisons [R009 pp. 9–10; R012 pp. 12–14]; study-specific shifts of 1, 10 and 100 in the 2009 solver comparison [D010 p. 28]. Conflict analysis is measured by adding it to a reference that lacks it, labelled "default" in the appendix [D004 pp. 193, 386]. A test set defined at 10,000 s is run at 3,600 s, so several hundred models time out on both sides of every table (card recount) [R021 p. 5]. The parallel baseline is the parallel code's own one-thread default [D029 pp. 16–17]. A classroom case changes three settings at once and credits one [R007 pp. 7, 9].
- **Say–do update.** ✅ unchanged.
- **Proposed text.** Fix the Example A.1 signs; replace the era line; reword step 7 (§3.2 items 1–3). New step after step 4, from the control-subset cluster (§4 row 5): read every node or time claim also on the subset that removes the confound it is exposed to: both-solved subsets for failures [R004 pp. 17, 19; R012 pp. 12–14; D010 p. 28]; equal-path blocks (same nodes and simplex iterations) for a pure per-node cost [D004 pp. 339–340]; the all-optimal subset for time-limit censoring [D022 p. 13; D023 p. 17]; a same-path subset across thread counts for hardware effects [D029 pp. 17, 20]; no affected figure where both sides time out [R021 p. 6]. Limitations: the written basis for *Brackets need hundreds of affected models* is [R021 p. 42].

### Method 5 · Instrument first

- **Strongest practice.**
  - Thesis: two years of code before research on SIP's source; SCIP begun in October 2002 with SIP's ideas; the test set selected with a frozen SCIP 0.82d and Cplex 10.0.1, final runs with 0.90f; versions on request and logs on the web; leak detection in the memory debugging mode [D004 pp. 9, 20, 65, 333–334, 340].
  - Complete solves from plug-ins with a minimal correctness contract: "This feasibility test already suffices to produce a correct algorithm for solving CIPs with constraints of the supported type." [R003 p. 9], restated in 2008 and 2009 [R009 p. 5; D010 pp. 7–8]; assertions make up 20 % of statements [D010 p. 16].
  - Reference solvers pick the test sets by stated effort windows and run with matched tolerances [R003 p. 24; R004 pp. 16–17]; the 2009 comparison set is chosen with CPLEX and CBC and drops instances with disagreeing optima [D010 p. 21]; instances with wrong answers are excluded and named [R012 pp. 12–14].
  - Library scale (co-signed): known optima, provenance and status published [R005 pp. 3, 11, 13]; run scripts, parsers, an exact solution checker and reliable primal bounds [R015 pp. 7, 10–12; D013 pp. 2, 10–13]; numbered suitability criteria with exclusion counts and a cross-solver consistency check [D021 pp. 20, 22–23, 25–26].
  - The detector is checked against the known original networks before any speed test [D011 pp. 20–22; R013 pp. 17–19]; correctness on graphs with published optima before scaling, easy graphs kept for that purpose [D020 pp. 11–13, 17]; a shared-memory build as the debugging environment for the distributed one, and a deterministic parallel mode wanted for development [D029 pp. 11, 16, 29–30].
  - Stated (co-signed): "Just believing the result of some unknown software without even the possibility to check what actually happened will not qualify for a scientific experiment." [R007 p. 3].
- **Contradiction (era).** In 2002 the test set is filtered by the code under study [R001 p. 10].
- **Variants.** The selector by era (§3.2 item 7); a library only half rule-selected (removal by rule, admission by goals) [R005 pp. 3, 5]; a benchmark set chosen by consensus under hard and soft requirements [R015 p. 7]; the whole sequential solver as the parallel unit, so that its progress carries over [R014 pp. 2, 5, 11–12; R020 p. 4; D018 TR p. 4; D014]; the explicit *sequential solver first* sentences appear only in the April 2014 revision [R019 pp. 3–4, 14, 17; D017 TR pp. 4–5, 20]; the 2020 rewrite weights what parallelization changes in the algorithm [R022 pp. 5–6, 19, 22]; a model published before any instance or harness exists, in co-signed group work before SCIP [D024 TR pp. 20, 22]; the build stated exactly and failures counted, but the test set selected by the detector under study [D023 pp. 13–14].
- **Say–do update.** ✅ unchanged.
- **Proposed text.** Replace *an older frozen version picks the test set* in the One line by the thesis-specific statement plus the era list (§3.2 item 7). Step 1 variant from §5 D. Step 4 widened by §5 E (every instrument, not only derived objects).

### Method 6 · Import at the data-structure level, let the test decide

- **Strongest practice.** SAT conflict analysis mapped onto MIP objects: bound changes as conflict-graph vertices, infeasible LPs explained along the dual ray, each constraint class with its own reverse propagation [R004 pp. 9–14; R008 pp. 7–9; D004 pp. 185–192]; watched literals in the set-covering handler days after Novikov's primer, the replacement rule re-decided by test [D004 pp. 10, 107–108]; SAT restarts re-decided for MIP and imported in restricted form with a stated reason: "In our implementation, a restart is performed if at least 5 % of the integer variables have been fixed." [R012 p. 11], with the reason that root fixings can trigger more presolving at the cost of a second root LP [R012 p. 11], the same rule in 2008 and 2009 [R009 p. 9; D010 pp. 12–13]; SatZ's lookahead turned into a history value combined with VSIDS [D010 p. 17; D004 p. 81]; SAT restarts in chip search replaced by a jump to a best node every 100 depth-first nodes, because the LP work would be lost [D004 p. 311]; CP propagation and SAT conflicts as plug-in types [R003 pp. 9–10, 13]. Abstracts: CP constraints and SAT techniques in a MIP framework [D007]; one branching rule from CSP, MIP and SAT criteria [D009]; SAT implied literals carried by clique and implication tables MIP solvers already keep, tested in CPLEX 12.5 [D016].
- **Say–do update.** ✅ for 2003–2013. No Gurobi-era evidence link; the later imports run from network design or global optimization into MILP.
- **Variants.** In 2005 general integers were kept out of conflicts and the SAT pieces ran together, not one at a time [R004 pp. 14–15]; the 2008 checker names only 1-FUIP, change unexplained [R009 pp. 9, 13]; network-design cut theory mapped onto the solver's c-MIR [D011 pp. 3, 10, 25–28]; RLT brought into MILP with new data structures, each piece tested alone, in two codes [D022 pp. 3–14; D023 pp. 7–8, 10, 15–21]; an information-theory device (Kraft's inequality) turned into a knapsack row in group modelling, no test [D024 TR pp. 6, 11, 15]; the direction reversed, MIP warm-start practice taken into an interval-methods code and measured alone [D026 pp. 6–7, 15, 39]; Gurobi 6.5's conflicts are dense Farkas rows without backward propagation, worth 5 % against his 12 % in SCIP, while watched literals and a symmetry tool are reused where they map one to one [R021 pp. 47, 51, 63–64]; counting derived from the SAT side and re-derived for branch-and-cut [R010 p. 4].
- **Proposed text.**
  - Step 3 variant from §5 D (map the import onto the host's existing routine and compute only its input).
  - Step 4 mechanism: predict non-transfer from the state the import would discard (warm-start bases, LP work), then confirm by test [D004 pp. 174, 311; R012 p. 11].
  - One design rule for CP imports, from one project (chip verification): count a linearization's rows and auxiliary variables before adding it, and leave what the LP cannot carry to propagation (a 64-bit shift-left would need 30,944 inequalities and 20,929 auxiliary variables) [R009 p. 12; D010 p. 34; R008 pp. 6–7]; the thesis states the same rule [D004 p. 19] and the 2008 abstract the split [D007].
  - Limitations: Hooker's SIMPL is cited by 2004 [R003 p. 26], so *unaware* holds for the start only; step 4 (test each habit alone) is practised from the thesis on, not in 2005 [R004 p. 15; D004 pp. 192–195].

### 2.7 Heuristics, misreadings and other sections: evidence and variant notes

The digests link methods only; the cards name heuristics in prose. Notes per item:

- **H1 Hand-code what the learner leans on.** The only written trace is the thesis acknowledgement that neural networks learned branching in his computer-science master's thesis on SIP [D004 p. 9]; the 2002 report presents the rule as a modification of pseudocost branching, with no learning experiment in the text [R001 p. 2]. Unchanged (talk-based).
- **H2 Measure the cheap rule against its oracle.** Source correction: the per-node measurement (score and position quotients over the whole tree and the top ten levels) is in the 2002 report only [R001 pp. 13–14]; the 2004 pages SKILL.md cites only frame the rules as estimates of full strong branching [R002 pp. 5–6]. Variant: bracket the rule between a floor and the oracle; random and most-infeasible branching take 923.6 s and 938.0 s in geometric mean against 170.5 s for reliability (8, 4) and 504.4 s for full strong branching [R002 p. 17]; most-infeasible is called not better than random [R002 p. 5].
- **H3 Fair yardstick.** More evidence: matched gap tolerances [R001 p. 11; R003 p. 24; R004 p. 16]; the original authors' parameters and instances [R006 p. 6]; the same LP solver and probing switched off where only one code uses it heavily [R011 p. 5]; the strongest of several SAT solvers [R008 p. 11; D004 pp. 313, 317]; only the MIP part compared [D004 pp. 334, 391; D010 p. 29]; identical simplified inputs for every method [D020 pp. 12, 18]; per-solver clusterings against solver bias [D021 pp. 35, 38]. Variants: all solvers at defaults without equalized tolerances [R009 p. 9]; the parallel code's own one-thread default as baseline, the sequential column printed beside it [D029 pp. 16–17]; each code measured only against itself, cross-code numbers declared not comparable [D022 p. 14; D023 p. 21].
- **H4 Debug solution.** No paper describes it (practice only, as SKILL.md says). Widened by §5 E.
- **H5 Instances trigger, sets conclude.** Evidence: single instances as triggers (memory traces, a probing failure) [D004 pp. 66–68, 315, 323]; small affected sets refused [R021 pp. 19, 22, 40, 42; R013 p. 27; D011 pp. 34–35]. Variant (co-signed genre): record-seeking parallel papers judge on one instance and one run per version [D018 TR pp. 13–14; R020 p. 13; R014 p. 12; R019 pp. 11, 14, 18]; a fixed hard instance is re-run at every release of the base solver as a cross-version probe [R019 p. 14; D017 TR p. 15].
- **H6 A failed reproduction is a study.** Source read in full [R011 pp. 2, 5–8, 11]. Widened by §5 F.
- **H7 Model and numerics before settings.** More evidence: tight tolerances for huge coefficients [R004 p. 16]; an exact rational audit of the library's LP bases and flagged unstable instances [R005 pp. 4–6]; 16-bit words with carries [R008 p. 5; R009 p. 12; D010 p. 34]; propagation safeguards [D004 pp. 48, 100–101, 209]; Gurobi's numerical safeguards in presolve [R021 pp. 9, 11, 15, 25; D030 p. 7]; numerically ambiguous instances kept out of the benchmark [D021 pp. 23, 25]; reduce the model before spending compute [R014 pp. 9–10]; "Choosing the right model is often more important (and more effective) than having the best solver implementation." [R007 p. 7] (co-signed).
- **H8 Metric by the user's goal.** More evidence: heuristics at gap targets [D004 pp. 142–146]; the pump judged by gap and time to the solution [R006 p. 7]; the primal integral designed for what primal heuristics are for, because by the usual measures "the trade-off between speed and solution quality is not well covered" [R017 p. 5], defined and normalised by the all-off run [R017 pp. 5–7; D015]. Widened by §5 A.
- **H9 Try it, try the opposite, revert.** First written evidence: "It turns out that our concerns are unjustified: applying linear domain propagation at every node improves the performance on almost all test sets." [D004 p. 114]; the default child selection found slightly inferior to three alternatives and printed [D004 p. 96]; delayed restarts inferior, other criteria needed [D004 p. 177].
- **H10 Print the loss and the open question.** More evidence [R004 pp. 2, 18–19; R006 pp. 7, 9; D004 pp. 96, 114, 177, 324–325; D010 pp. 14–15, 28–29, 36–37; R021 pp. 14, 18, 28, 65; D030 pp. 12–13; D020 pp. 9, 15–18, 22; R011 p. 8]. Variant: from 2007 the loss usually sits in the body, not in the abstract or summary [R008 pp. 2, 13–14; R009 p. 14; R017 pp. 3, 7; D022 pp. 3, 11–12; D023 pp. 1, 15–16, 22].
- **Misreading 1** (seeds): reworded in §3.2 item 3.
- **Misreading 2** (knock-outs do not add): more evidence [D004 p. 142; R017 p. 7]; the presolve paper explains small knock-outs by the component that covers for them [R021 pp. 8, 11, 13, 18, 61–62, 65]. Variant: the 2014 multi-row knock-outs multiply to more than switching the class off (card arithmetic, 1.42 against 1.31) [D030 pp. 12–15]; non-additivity also runs the other way.
- **Misreading 3** (SCIP from nothing): the code was rebuilt from scratch for flexibility and CIP while SIP's ideas were carried into the first version [D010 p. 15; R009 p. 3; D004 p. 20]; the 2002 rule ran in SIP with CPLEX as LP solver [R001 p. 11].
- **Misreading 4** (hand-rules man): the written record is thin (H1).
- **Misreading 5** (nearly as fast as CPLEX): the likely written source is two abstracts, one co-signed and one sole-authored (§3.2 item 14).
- **Taste marks.** Mark 1 is strained by the neutral-on components of [R021 pp. 14, 18, 56, 65]. Mark 3 (small measured wins): Gurobi MILP gains of 1–11 % reported as improvements [D023 pp. 21–22]. Mark 6: its most explicit source is the co-signed MIPLIB 2017 selection model [D021 pp. 24–36]. Mark 7: data structures and limits in print [R021 pp. 37–38, 45, 49, 66; D023 pp. 7–8, 10, 14]. Warning sign 3: see §3.2 item 21.
- **Inner Tensions.** *Which baseline counts*: the 2022–2025 study measures each code only against itself [D023 p. 21], while his 2004–2009 texts measured against CPLEX [R003 p. 24; R004 p. 16; D010 p. 28]. *From scratch or reuse*: rebuilt from scratch with SIP's ideas [D010 p. 15; R009 p. 3]; the parallel layer reuses the unmodified solver: "This makes the parallelization development independent of the SCIP development. Thus, ParaSCIP directly profits from any algorithmic progress in future versions of SCIP." [R014 p. 2] (co-signed, Shinano first, no role stated: not a side of his own tension, so SKILL.md does not use it).

---

## 3. Variants and contradictions

### 3.1 The twelve contradiction links, checked against their cards

Twelve links on twelve cards, nine studies. Each card was reopened; the verdicts:

| Card(s) | Method | Claim of the card | Check | Verdict |
|---|---|---|---|---|
| D004 | M4 | SKILL.md reverses the signs of Example A.1 | text read at [D004 pp. 335–336]: the geometric mean reports a 27 % improvement for setting B, the shifted geometric and arithmetic means a 6 % and 89 % deterioration | Upheld; wording fix |
| R013, D011 (one study) | M4 era | the slower-run subsets of ≥ 10 s and ≥ 100 s exist in 2009–2010 | "The subsets cplex10s and cplex100s correspond to those instances within cplex that need at least 10s and 100s of CPU time to be solved, respectively, by the slower of the two versions, mcf and nomcf." [R013 p. 27]; [D011 pp. 33–34] | Upheld; a narrower form (three subsets, CPLEX part only, shift not stated) |
| D013 (with R015) | M4 step 7, Misreading 1 | 100 permutations per model, a variability score per instance, permuted copies and inferential tests recommended | [D013 pp. 13–18; R015 pp. 13–15]; "Performance is not deterministic. Instead, it is a random variable that can be sampled with computational experiments." [R015 p. 15] | Upheld for a co-signed library paper (16 authors); no section credited to him, the variability work credited to Danna [R015 p. 22; D013 p. 57] |
| D029, R018 (one study) | M4 step 7 | five runs of each nondeterministic configuration | [D029 p. 20; R018 pp. 16–17, 19–21] | Upheld; the repeats answer message timing in parallel runs, not seeds; Shinano first |
| D023 | M4 step 7 | permuted copies in the SCIP tables | the text names "permuted instances" in the failure counts and a table "with 4 permutations" [D023 pp. 14, 26–27] (checked in the text) | Upheld; the procedure is not described; the Gurobi part mentions neither [D023 pp. 21–22] |
| D018, R020 (one study) | M4, H5 | one instance, one run per version | [D018 TR pp. 13–14; R020 p. 13] | Upheld as a genre exception (record-seeking parallel work, co-signed); the stated reason is run cost [D018 TR p. 13] |
| R021 | M1 | components on without a measured gain | [R021 pp. 14, 18, 56, 65] | Partial: step 5 allows it, Taste mark 1 does not |
| R009 | M2 step 1 | a solved-count verdict in the abstract beside a time loss in the table | [R009 pp. 2, 10] | Upheld (co-signed); recorded as a variant of step 1 and of H10 |
| R001 | M5 | 2002 test set filtered by the code under study | [R001 p. 10]; the CPLEX check on the excluded instances partly offsets it | Upheld as an era note |

### 3.2 Claims of SKILL.md that the full texts change (full texts win over web snippets)

1. **Method 4, Practice, Example A.1.** Now *+27 % (geometric), −6 % (shifted geometric), −89 % (arithmetic)*. Replace by: −27 % with the geometric mean (setting B better), +6 % with the shifted geometric mean and +89 % with the arithmetic mean (setting B worse) [D004 pp. 335–336].
2. **Method 4, One line, era.** Now *the bracket form is in his papers from 2014 … Do not read earlier work as if it used brackets.* Replace by: the thesis (2007) reports shifted-geometric-mean ratios against the default with faster/slower counts and equal-path blocks [D004 pp. 335–336, 339–340]; a narrower bracket form, ≥ 10 s and ≥ 100 s subsets by the slower run with affected rows, wins and time-outs, appears in the 2009 report and the 2010 journal paper, in their CPLEX part, with no stated shift [R013 pp. 26–27; D011 pp. 33–34]; the full table (≥ 0, 1, 10, 100, 1,000 s, shift 1, affected by iterations) is from 2014 [D030 pp. 10–12; R021 pp. 5–6].
3. **Misreading 1, Method 4 step 7, the Activation Rules default and the Roundtable Card's blind spot** (*No written study of his has them*). Replace by: none of his sole-authored studies uses seeds or permutations [D004 p. 333; R003 pp. 24–26; R004 pp. 15–19]; co-signed written studies do in four forms: a library's variability study with 100 permutations per model [R015 pp. 13–15; D013 pp. 13–18]; five repeats of nondeterministic parallel configurations [D029 p. 20; R018 pp. 19–21]; permutations as a diversification device in racing [D017 TR pp. 10–11; R019 p. 10; D018 TR p. 6]; permuted copies in 2025 tables with no stated procedure [D023 pp. 14, 26–27]. The 2016 presolve report names one unspecified recheck: "Nevertheless, such a small set of problem instances does not provide any meaningful results, and indeed, additional tests that we have conducted showed that the speed-up in Table 23 is just an artifact of performance variability." [R021 p. 40]. The five-seed *consistent win* rule remains spoken only.
4. **Method 2, Practice, conflict analysis.** Now *The 2007 default uses conflicts for propagation only …, at most 10 per infeasible subproblem, with aging*. Replace by: these are the parameter settings of the thesis experiments [D004 pp. 192–193]; in the SCIP 0.90f MIP benchmarks conflict analysis was off by default and was measured by adding it to that reference [D004 pp. 193, 386; D010 pp. 20–21]; the best variant gains about 12 % against no conflict analysis [D004 p. 193]. The reason against LP cuts for non-binary conflicts is given only in part: the linearized disjunction is called probably very weak, untested [D004 p. 191; R004 p. 14].
5. **Method 1, Practice, the Mcf gate.** Now *Releasing the network-inconsistency threshold alone helped SCIP but not CPLEX*. This follows the report [R013 pp. 27–29]; the journal version reports the study on the general-MIP sets in both solvers, where releasing the threshold alone "already deteriorates the performance" of CPLEX, the SCIP rows still improve slightly, and the class gain on one network-design set no longer appears [D011 pp. 34–37]. Keep the sentence with the version named, and add the journal result.
6. **Method 1, Practice, counter-examples.** Add simple probing on single equations, biconnected components and global probing at nodes (on by default; at most 3 % on their affected models; the last with more time-outs when on) [R021 pp. 18, 56, 65].
7. **Method 5, the test-set selector.** Holds for the thesis only [D004 pp. 333–334]. By era: the code under study in 2002 [R001 p. 10]; a reference solver with an effort window in 2004–2005 [R003 p. 24; R004 p. 16]; two other solvers in 2009 [D010 p. 21]; the code family itself at Gurobi [D030 p. 11; R021 p. 5]; consensus under hard and soft rules for the 2010 library benchmark [R015 p. 7]; a published selection model for the 2017 library [D021 pp. 24–36]; the detector under study in 2025 [D023 p. 13].
8. **Method 2, Limitations, the primal integral.** Its first written form is a 2011 report that he co-signed (first of three, alphabetical; roles not stated), which defines the measure and normalises it by the all-off run [R017 pp. 3, 5–7]; the 2012 abstract keeps the claim to introduce it [D015]. The 2013 journal paper SKILL.md cites is a later venue (not read).
9. **H2, source.** See §2.7 H2.
10. **Signature Work Anatomy, branching.** *22 MIPLIB 3.0 instances* → 16 MIPLIB 3.0 instances plus 6 randomly generated instances of the arborescence-flow problem [R001 p. 11] of the 2000 diploma thesis of T. Pfender [R001 p. 16]. The same thesis is the source of the aflow instances that MIPLIB 2003 lists under Achterberg [R005 pp. 4, 13–14] and MIPLIB 2010 credits to him [D013 pp. 19, 60]; none of these texts states the name change (card c2-01).
11. **Signature Work Anatomy, conflict analysis, Minimum evidence.** Name the subsets (card recount): the ALU figures (−90 % nodes, −60 % time) are on the 21 instances that presolve does not solve, all 35 give −73 % and −42 %; the feasible-MIP figures (−50 %, +15 %) are on all 29, the 24 solved by both settings give −44 % and +4.5 % [R004 pp. 17, 19]. The abstract keeps the loss: "On feasible MIP instances, the number of required branching nodes was reduced by 50% in the geometric mean. However, the total solving time increased by 15%." [R004 p. 2].
12. **Signature Work Anatomy, presolve.** *each with a knock-out table*: fixed-variable removal and the rounding of integer bounds have none, the first because it acts through model size [R021 p. 21].
13. **Method 3, Limitations.** See the Method 3 proposal (§2).
14. **Misreading 5.** The likely written source is the abstracts that call SCIP almost competitive with commercial MIP solvers: co-signed in 2008 [R009 p. 2; R012 p. 2] and sole-authored in 2009 [D010 p. 1]. The measured ratios, for the misreading's correction: 5.1 in the unshifted time mean (2.4 with a 10 s shift; card arithmetic) [R009 p. 10], 3.5 and 1.84 [R012 p. 14] and 2.86 [D010 p. 28]. The 2004 and 2005 texts print the loss plainly [R003 p. 24; R004 p. 16].
15. **Roundtable Card, Gleixner line.** Gurobi 6.5 stores the whole Farkas proof as a linear row, with no backward propagation [R021 pp. 63–64]: his Gurobi-era conflict practice is not the graph-based SCIP one.
16. **Roundtable Card, Fischetti line** (*variability averaged over seeds against exploited*). Co-signed ParaSCIP texts exploit variability: racing with settings, random top-level branching and permutations [D017 TR pp. 7, 10–11; R019 p. 10; D018 TR p. 6]; the co-signed library says variability may be exploited by massively parallel solvers [D013 p. 14]. No text gives his own position (Shinano first, roles not stated), so the contrast stays an inference.
17. **Honest Boundary, *The CPLEX years have almost no first-hand method evidence*.** Co-signed full texts now cover them: the Mcf-separator with a CPLEX implementation and a CPLEX-internal general-MIP set [D011 pp. 2, 34; R013 pp. 26–27]; the primal integral [R017 pp. 5–7]; MIPLIB 2010 [R015; D013]; ParaSCIP [R014; R018; R019]; abstracts for implied literals in CPLEX 12.5 [D016] and the 12-year component analysis [D028]. None is sole-authored.
18. **Honest Boundary and Method 4, *A&W 2013 … not read*.** Its abstract is read [D028]: it names a scheme for analysing benchmark results but not its form; the co-signed 2014 and 2016 texts credit their table form to it [D030 p. 11; R021 p. 5]. The bracket form's origin is still unconfirmed in a text of its own.
19. **Honest Boundary, *diploma theses not found*.** The mathematics diploma thesis is identified at metadata level [D036]; the computer-science diploma thesis is not.
20. **Honest Boundary, the *deterministic work units* item under *Claimed but unverified*.** Co-signed written practice exists in Gurobi 6.5's presolve: work limits counted in touched non-zeros [R021 pp. 49, 66], and an order-dependent step made deterministic under parallelism by collecting candidates in parallel and applying them in one sequential pass [R021 p. 52]; a deterministic parallel mode is called necessary for development [D029 pp. 29–30]; the 2013 abstract highlights CPLEX's deterministic parallel optimizer [D028]. No sole statement.
21. **Taste warning sign 3 and Integrity rule 4** (the unmeasured child-selection default, THESIS p. 74). The sentence concerns Martin's root-LP child selection when it was adopted; the same chapter measures it and finds the default hybrid slightly inferior [D004 pp. 88, 95–96]. Keep the quote, add that it was measured in the same chapter.
22. **Research Trajectory, 1999–2002.** Add the 2000 diploma thesis under his former name [D036] and the 2002 MOMENTUM report on UMTS network planning, group work with ZIB, Darmstadt and Atesio authors, six months before the history-branching report [D024 TR pp. 1–3].

### 3.3 Version notes (report and published texts)

- **Mcf-separator.** The report's inconsistency study is SCIP-only and includes the set where a looser gate gained [R013 pp. 27–29]; the journal moves it to the general-MIP sets in both solvers and prints the CPLEX numbers [D011 pp. 35–37]. The general-MIP sentence of the journal abstract is new [D011 p. 1]. So the gate was decided where harm would occur, and the class gain it gives up left the published version.
- **ParaSCIP 2013/2014.** The revision adds that a state-of-the-art sequential solver is the most important ingredient and that exploiting a powerful MIP solver is crucial [D017 TR pp. 4–5, 20], and drops two reasons the original gave for memory-conservative settings and a lowered racing threshold [R019 p. 14]. "it is crucial to exploit a powerful MIP solver in parallelization" [D017 TR p. 20].
- **ParaSCIP 2015/2016.** The revision recasts "ad-hoc values" of the collecting-mode parameters as moderate values not tuned well enough [R020 p. 13; D018 TR p. 14].
- **ParaSCIP 2012/2013.** The ZIB-Report has the same text as the journal article, and its text layer carries the tables [R018; D029].
- **MIPLIB 2010.** Report and journal are one study; the report calls the benchmark selection dynamic, by consensus [R015 p. 7]; the journal describes a staged review [D013 p. 6].
- **Abstracts word for word.** D007 = R009, D008 = R010, D014 = R014, D015 = R017, D019 = R021 (up to hyphenation) (cards a2-01).
- **RLT.** The 2025 version adds redundancy filters, permuted copies, size-group tables and a control run [D023 pp. 8–9, 14, 20–21, 26–27] to the 2022 preprint [D022].

---

## 4. Promotions

**None.** The skill keeps its six core methods. Nine clusters reached three or more distinct works read in full or in part; none passes all four checks. The one that comes closest (row 5) passes exclusivity only in part and is a reading rule of Method 4, so it becomes a new step there.

| Cluster (merged by meaning) | Works read in full or part | 1 Recurrence | 2 Say–do | 3 Executable, non-standard | 4 Exclusivity | Result |
|---|---|---|---|---|---|---|
| Split the verdict by the answer required: a proof (infeasibility, validity, optimality) or a witness (a feasible point, a counter-example) | R004, R008, R009, R012, R015, D004 (6; D010 pp. 36–37 in prose) | ✅ conflict analysis 2005, property checking 2007–08, library sets 2010 | ✅ stated: "However, due to the much more involved procedures employed in our algorithm it is inferior to SAT for finding counter-examples of an invalid property." [R008 p. 14]; "For invalid properties, which are not shown in the tables, our algorithm is usually inferior to SAT for finding counter-examples." [R009 p. 14]; reasons for separate infeasible and primal sets [R015 pp. 6, 8]; practised [R004 pp. 16–19] | ✅ | ⚠ not shown to be his: the split follows the answer type of verification problems, and the co-signed library made it a library rule [R015 pp. 6, 8] | Heuristic-level; H8 widened (§5 A) |
| Delegate to the host: compute only the missing input, keep the host's machinery | D011, R014, R020, D020 (4; abstracts D006, D014) | ✅ Mcf 2010, ParaSCIP 2010–15, feedback arc sets 2021 | ✅ co-signed: "It is important to understand that our framework is not explicitly generating cutting planes. It only calculates weight vectors u." [D011 p. 3]; [R014 p. 2]; "Any research attempting to implement a novel cutting plane algorithm has to compete with that strong baseline." [D020 p. 11] | ✅ | ✗ building on a production solver, unmodified or through its extension interface, is common research practice (this note's reading) | Heuristic-level; variant notes on Method 5 step 1 and Method 6 step 3 (§5 D) |
| Let a heuristic part cost time, never correctness | R003, D004, D011, R013, R014 (5; D011 and R013 one study) | ✅ 2004, 2007, 2009–10, 2010 | ✅ sole practice [R003 p. 20; D004 p. 48]; stated co-signed [D011 p. 35]; "These changes only influence the path the solver takes, not the overall result." [R014 p. 11] | ✅ | ✗ a general robust-software habit | Heuristic-level; Method 1 step 0 (§5 B) |
| Prove the exact sub-decision hard, measure the literature heuristic, keep the cheapest rule on data at hand | R004, D004, R008, R009 (conflict analysis); D030, R021 (presolve) | ✅ two projects, 2005–2016 | ✅ [R004 p. 11; D004 p. 188; D030 pp. 3–4] | ✅ | ✗ | Heuristic-level; Method 2 step 2b (§5 C) |
| Read each claim on the subset that removes its confound (both-solved, equal path, all-optimal, same path; no affected count where both sides time out) | R004, D004, D010, R012, R021, D022, D023, D029 (8; D022 and D023 one line) | ✅ 2005–2025 | ✅ reasons stated [D022 p. 13; R021 p. 6; D004 p. 339; D029 p. 21] | ✅ | ⚠ solved-by-all and all-optimal subsets are shared practice in the SCIP community's papers; the equal-path block is his thesis's | Method 4 new step (§2); it is a reading rule of Method 4, not a new method |
| Time as a count times a unit cost: predict which factor moves, then read both | D004, D010, D026, D030, R021, R011, R002 (7) | ✅ 2004–2016 | ✅ predictions written before the runs [D026 pp. 8–9]; [D010 p. 29; D004 p. 194] | ✅ | ✗ | Method 2 step 2 alternative (§2) |
| Check every instrument against ground truth (detector, checker, feature space, published optima) | D011, R013, D021, D020, R005, R015, D013 (7; 5 studies) | ✅ 2005–2021 | ✅ co-signed practice | ✅ | ✗ | Heuristic-level; H4 widened (§5 E) |
| Linearize only what the LP can carry, propagate the rest | R008, D004, R009, D010 (4; abstract D007) | ✗ one project (chip verification) | ✅ [R009 p. 12; D010 p. 34] | ✅ | ✗ | Method 6 variant (§2) |
| Parallel-search devices: racing on variability, restarts used to reorganize the tree, repeats of nondeterministic runs | D017/R019, D018/R020, D029/R018, R022 (one project line) | ⚠ one line | ✗ no role assignable in Shinano-first texts | ✅ | — | Pool (§6) |

---

## 5. New heuristics

SKILL.md already has ten heuristics, the top of the framework's band (5–10). Six clusters qualify at heuristic level (executable, plus at least one other check). None is added as an eleventh entry: each is written into the nearest existing heuristic or method step, where it adds explanatory power without a duplicate. If the editor prefers a separate entry, A is the strongest; keeping ten would then need one merge, most naturally H2 into Method 3, whose parameter family already holds full strong branching as its ∞ end [R002 p. 8].

### A. H8 widened · Metric and split by the answer the user needs

- **One line**: before pooling a test set, sort it by the answer each instance needs (a proof of infeasibility or validity, a witness, an optimum), table the parts apart, and expect different winners; choose the measure per part.
- **Cards**: infeasible chip IPs gain in nodes and time while feasible MIPs lose time, in separate tables with separate verdicts [R004 pp. 16–19]; CIP wins valid properties, SAT wins counter-examples, tabled by width [R008 pp. 11–14; R009 p. 14; R012 p. 18; D010 pp. 36–37]; a SAT-then-CIP portfolio named as the open question [D004 p. 322]; dedicated infeasible and primal sets because solvers are tuned for optimization, not for feasibility, and not at all for infeasible problems [R015 pp. 6, 8]; the existing H8 cases (gap targets, the primal integral) are the primal side of the same rule [D004 pp. 142–146; R017 pp. 5–7].
- **Checks**: §4 row 1.
- **Steps**: (1) classify every instance by the answer it needs; (2) report the component per part, with the measure that part's user cares about (time to proof; time to first or good solution; time to optimality); (3) if winners split, name the portfolio or the per-part default and say which part a default serves; (4) state the losing part with numbers, not only in words (the 2008 text gives the losing part in words only [R009 p. 14]).

### B. Method 1 step 0 · Validity first, so the gate can trade speed alone

- **One line**: design the component so that any error of its heuristic parts (a wrong detection, a changed setting, an unstable LP) can only cost time; then the default gate is a speed decision.
- **Cards**: cuts are MIR inequalities of aggregations of original rows, so a wrong detection only makes cuts weak or dense [D011 pp. 7–9, 35; R013 pp. 3, 27]; an unstable LP is retried with other settings, and otherwise the node's LP bound is dropped and the node processed as if no LP had been solved [R003 p. 20; D004 p. 48]; settings changed between parallel jobs alter the path, not the result [R014 p. 11].
- **Checks**: §4 row 3.

### C. Method 2 step 2b · Prove the exact sub-decision hard, then keep the cheapest rule

- **One line**: when a component must solve a selection problem exactly to be optimal (a minimal infeasibility explanation, a redundancy test), prove or cite its hardness, try the literature's heuristic and measure its overhead, and keep the cheapest rule on data already computed, with the exact test only in special situations.
- **Cards**: minimal bound-IIS shown NP-hard, a Farkas-based literature heuristic dropped for its running-time overhead, simple rules on the LP information at hand kept [R004 p. 11; D004 p. 188; R009 p. 6; R008 pp. 8–9]; non-redundancy NP-complete, so LP-redundancy is the target and full LPs are solved only in special situations, cheaper subsets otherwise [D030 pp. 3–4; R021 p. 27].
- **Checks**: §4 row 4.

### D. Method 5 step 1 and Method 6 step 3 variant (co-signed) · Delegate to the host

- **One line**: write only the input the host's existing routine lacks, or run the unmodified host as the unit, so that validity and the host's future progress come for free; say in the paper which part is yours.
- **Cards**: only the aggregation weights and multipliers are computed, bound substitution and rounding are the solver's c-MIR [D011 pp. 3, 23]; unmodified SCIP processes under a coordinator [R014 pp. 2, 5; D014]; the solver and the communication library as exchangeable classes [R020 p. 4; D018 TR p. 4]; lazy rows only for correctness, the host solver's cuts kept and not competed with [D020 pp. 9–11]; a parallel CPLEX extension [D006] (abstract, weak).
- **Checks**: §4 row 2. All sources are co-signed; label it so.

### E. H4 widened · Check every instrument against ground truth before measuring with it

- **One line**: the debug solution checks derived objects; extend the same test to every instrument: a detector against known structures, a checker in exact arithmetic, a feature space against known groups, a new method against published optima.
- **Cards**: the detector against the known original networks, with and without presolve, failures named with causes [D011 pp. 21–23; R013 pp. 17–19]; floating-point LP bases rechecked in rational arithmetic [R005 pp. 5–6]; returned solutions checked in exact arithmetic against the original file, primal values made reliable by an exact LP re-solve [R015 pp. 8–11; D013 pp. 10–12, 43; D021 pp. 22–23]; a cross-solver consistency check with inconsistent instances excluded and counted [D021 p. 23]; the feature space shown to recover the model groups [D021 p. 37]; correctness on graphs with published optima against two formulations before any scaling study [D020 pp. 11–13]; the lack of a reference implementation named as the debugging obstacle [D026 p. 17].
- **Checks**: §4 row 7. Co-signed sources except the debug solution itself (practice only).

### F. H6 widened · Re-measure a published figure and explain the gap

- **One line**: when your knock-out of a component differs from a published one, rerun with the published protocol's differences and name the cause before reporting your figure.
- **Cards**: a higher published presolve-off factor explained by node presolve also being switched off there [D030 p. 12]; the presolve-off factor set beside the published CPLEX figure, and Gurobi's 5 % for conflicts set beside his 12 % in SCIP, the gap put down to implementation, solver environment and test set [R021 pp. 6, 64]; a 12-year re-measurement of a predecessor's component analysis [D028]; the failed reproduction that is H6's source [R011 pp. 2, 7–8].
- **Checks**: recurrence across two project lines (presolve 2014–16; formulation 2008), say–do ✅ (co-signed), executable ✅, exclusivity ✗.

---

## 6. Candidate pool (not promoted)

All 96 new-pattern-candidate entries, each assigned to one row. *Works* counts distinct works (pairs merged); *full* counts those read in full or in part.

| Cluster (merged by meaning) | Entries | Works (full) | Decision |
|---|---|---|---|
| Delegate to the host / thin layer over the mature engine; correctness rows lazily, host cuts kept | 6 | 5 (4) | §5 D |
| Split results by answer type; complementary-strength portfolio | 6 | 6 (6) | §5 A |
| Let heuristic parts cost time, never validity; degrade, don't abort | 3 | 3 (3) + D004, R013 | §5 B |
| Hardness lemma, then the cheapest heuristic | 1 | 1 (1) + D004, R009, R008, D030, R021 | §5 C |
| Ground-truth the detector; validate a feature space | 3 | 2 (2) | §5 E |
| Exact rational re-check; certify only what can be certified | 2 | 2 (2) + D021 | §5 E; H7 evidence |
| Re-measure a published number and explain the gap | 3 | 3 (2) | §5 F |
| Control subsets: all-optimal, control run, same-path | 3 | 3 (3), D022 and D023 one line, + D004, R004, D010, R012, R021 | Method 4 new step (§2) |
| Node–time co-movement; predict which factor a change moves | 2 | 2 (2) + D010, D030, R021, R011 | Method 2 step 2 alternative (§2) |
| Linearize only what stays small, propagate the rest | 2 | 1 (1) + R008, D004, D010 | Method 6 variant (§2) |
| Predict non-transfer from discarded state | 1 | 1 (1) + R012, D010 | Method 6 step 4 mechanism (§2) |
| Per-call applicability guards | 1 | 1 (1) + R021, D018 | Method 1 evidence (§2) |
| Reverse the modeller's linearization | 1 | 1 (1) + D011 | Method 1 step 1 evidence (detection on the matrix) |
| Second-solver replication | 1 | 1 (1) + D011 | Method 1 step 5 evidence (two codes, 2010 and 2022–25) |
| Scalability grid with a deliberate worst-case family | 1 | 1 (1) | Method 1 variant (worst case as a test) |
| Correctness contract separate from speed callbacks | 2 | 2 (2) + D010 | Method 5 step 3 evidence; one SCIP design restated, not a heuristic |
| Version-stamp features and numbers | 1 | 1 (1) + D023, R022 | Method 5 evidence; writing move WM8 |
| Purge by a stripped-down reference configuration | 1 | 1 (1) | Method 5 evidence (test-set rule); EP10 |
| Purpose-specific sets with rule-based membership; test-set selection as an optimization model; cluster per feature group; per-solver performance clusterings | 4 | 2 (2) | Taste mark 6 and Method 5 evidence (co-signed library work); EP10 |
| Measure designed for the component's job | 2 | 1 (1) | H8 evidence (§2.7); Method 2 variant |
| Random rule as floor baseline | 2 | 2 (2), one project | H2 variant (§2.7) |
| Explain a small knock-out by the component that covers for it | 1 | 1 (1) + D004, R017 | Misreading 2 evidence (§2.7) |
| Per-iteration trajectory plots, a losing instance included | 1 | 1 (1) | H10 evidence; writing move WM5 |
| Formulation robustness as a design criterion | 1 | 1 (1) | H6 evidence (already in H6) |
| Collapse variants by presolve equivalence | 1 | 1 (1) | Already in H6; rejected as a duplicate (§10) |
| Phase time against phase resource share | 1 | 1 (1) | Method 2 evidence (co-signed) |
| Permutation-sampled variability score | 1 | 1 (1) | Misreading 1 rewording (§3.2 item 3) |
| Repeat only nondeterministic configurations; solved in all runs | 3 | 1 (1) | Misreading 1 rewording; EP18 |
| Exploit variability by racing; variability as diversification | 4 | 3 (3), one line | Pool; Roundtable Card note (§3.2 item 16) |
| Make the forced restart pay; a restart as a point to reorganize | 4 | 3 (3), one line | Pool (co-signed, no role) |
| Refuse a single-number solver ranking | 4 | 2 (2) | Pool: co-signed only, and at odds with his sole-authored single weighted total [D004 p. 336] and derived headline factor [D010 pp. 2, 29] |
| Name the substitute evidence when no protocol fits | 2 | 2 (2), one line | Pool (with the row above) |
| Fixed hard instance as a cross-version probe | 2 | 1 (1) | H5 variant (§2.7) |
| Count resources including lost work | 2 | 2 (2), one line | Pool |
| Open library instances as targets | 2 | 2 (1), one line | Pool |
| Parallelization as an algorithm change | 1 | 1 (1) | Pool |
| Collect, then apply, for determinism in parallel | 1 | 1 (1) + D029, D028 | Honest Boundary item (§3.2 item 20); DM19 |
| Mirror pruning for a new task | 2 | 1 (1) | Pool; DM14 |
| Necessary-condition pruning before separation; sign-based pre-filtering; projected check | 3 | 2 (2), one line | Pool; DM18 |
| Minimal exported summary to restore a hidden view | 1 | 1 (1) + R017, D023 (reuse) | Pool; DM7 |
| Order and warm-start a sequence of related LPs | 1 | 1 (1) | Pool; DM16 |
| Heuristic repair as separation oracle | 1 | 1 (1) | Pool; DM17 |
| Key the cycle test on the full iteration state | 1 | 1 (1) | Pool; DM15 |
| Clean the samples of an online estimator | 1 | 1 (1) | Pool; DM4 |
| Measure the quantity a fixed threshold depends on | 1 | 1 (1) | Pool; EP11 |
| Operational status classes kept live | 1 | 1 (1) | Pool (library practice) |
| Full model first as the yardstick for simplifications | 1 | 1 (1) | Pool (group work, 2002) |
| Sampled scenarios with a simulator in the loop | 1 | 1 (1) | Pool (group work, 2002) |
| Withheld under the holdout rule | 3 | 3 (3) | Two candidate entries forming one cluster, and one single-card candidate, lean on sealed material; their content waits for the validation that unseals it |
| **Total** | **96** | | |

---

## 7. Technique inventory

### 7.1 Proof devices

- **PD1 Hardness to justify a cheap rule.** Minimal bound-IIS NP-hard by a reduction from minimal IIS with slacks as bounds [R004 p. 11; D004 p. 188]; non-redundancy NP-complete by appending an infeasible row [D030 p. 3]; NP-completeness by reduction from subset sum [D004 p. 100].
- **PD2 A certificate that survives relaxation.** The Farkas aggregation's left side does not depend on the local bounds, so bounds can be relaxed while the right side stays negative; the same for bound-exceeding LPs with the dual solution [R004 pp. 12–13; D004 pp. 188–191; R008 pp. 8–9].
- **PD3 Exchange arguments.** Dominated columns by moving the surplus from one column to the other [R021 pp. 44–45]; the optimality of best-first search [D004 p. 89].
- **PD4 Fixed-LP argument.** Dual bounds on the continuous part that do not depend on the right-hand side stay valid after fixing the integers at an optimum; complementary slackness then gives the reduction [R021 pp. 58–59].
- **PD5 Undetermined coefficients.** Write the target relation and both source rows as implications on the binary, scale, match coefficients, read off the conditions [D022 p. 6; D023 pp. 6–7].
- **PD6 Two-direction lemma from an arbitrary point of the local box** (a subtree is unrestricted iff all constraints are locally redundant) [R010 p. 4].
- **PD7 Counterexample that motivates a limit.** A two-row system with an infinite sequence of bound reductions [R021 p. 11]; a minimum relative bound change against slow ping-pong chains [D004 pp. 100–101].
- **PD8 Validity by construction.** Every cut an MIR inequality of an aggregation of original rows [D011 pp. 7–9, 35; R013 pp. 3, 27].
- **PD9 Termination by growth.** At least one new row per iteration of a finite cycle matrix [D020 p. 9]; a well-founded ordering for term normalisation [D004 p. 236].
- **PD10 Class generalisation by construction.** CIP contains CP(FD) and MIP by constructing the residual LP [R012 pp. 5–6; D004 pp. 27–28].
- **PD11 Exactness condition for a filter.** Projection filtering is exact iff the McCormick inequalities hold at the LP point; otherwise the solver's behaviour is stated [D023 pp. 11–13; D022 pp. 9–10].

### 7.2 Design moves

- **DM1 Incumbents as settings of one family, with the map drawn** [R002 p. 8; D004 p. 82; R006 p. 5; D010 p. 18].
- **DM2 Budgets in solver-internal units**: iterations relative to node LPs [R002 p. 6; D004 pp. 78–80]; useless probings and fixings [D004 p. 171]; touched non-zeros scaled by success [R021 p. 49]; work and success ratios [R021 p. 66]; a capped conflict pool [R021 p. 64]; call frequency, rounds and term caps for a separator [D022 p. 10; D023 p. 13].
- **DM3 Normalise heterogeneous scores before weighting** (divide by the current average, map with x/(x+1)) [D004 p. 81]; the product score [D004 p. 76; D010 p. 18].
- **DM4 Correct a biased cheap estimate with a ratio of sums under forgetting, and keep contaminated observations out**: "In updating the history values, we ignore branching results, where one of the subproblems is infeasible or where node preprocessing or strengthening cuts where applied at the child nodes, because this would lead to unfair large gain values in comparison to other nodes." [R001 p. 9]; the scaling factor as a ratio of sums under exponential forgetting [R001 p. 8].
- **DM5 A detector with a numeric fit used twice** (drop bad elements, switch the component off) [D011 pp. 11, 19–20; R013 p. 10].
- **DM6 Compute only the missing input for an existing routine** [D011 pp. 3, 23].
- **DM7 A minimal exported summary when modularity hides a view** (two lock counts per variable) [D010 p. 14], reused by lock-based rounding [R017 p. 4] and by product records [D023 p. 8].
- **DM8 A mandatory correctness callback, optional speed callbacks** [R003 p. 9; R009 p. 5; D010 pp. 7–8].
- **DM9 Degrade on numerical trouble** [R003 p. 20; D004 p. 48].
- **DM10 Numerical safeguards**: 16-bit words with carries [R008 p. 5; R009 p. 12; D010 p. 34]; small-coefficient cleanup, bound-change thresholds, gcd heuristics, Markowitz-type pivot tests, multiplier caps [R021 pp. 9, 11, 15, 25, 33; D030 p. 7].
- **DM11 Count a linearization before adding it** [R009 p. 12; D010 p. 34; R008 pp. 6–7].
- **DM12 Seed conflicts from the dual ray; move non-binary bound changes to the conflict side** [R004 pp. 11–15; D004 pp. 189–192].
- **DM13 Import restarts in restricted form, with the reason** [R012 p. 11; R009 p. 9; D004 p. 174].
- **DM14 Mirror a pruning rule for a new task** (unrestricted subtrees for counting) [R010 pp. 4–5; D008].
- **DM15 Blend the objective into the pump's distance with a decaying weight; key the cycle test on (point, weight)** [R006 p. 5].
- **DM16 Skip, warm-start and order a sequence of related LPs** [D026 pp. 6–7].
- **DM17 Lazy rows for correctness only; the repair heuristic's output as incumbent and as separation seed** [D020 pp. 9–11].
- **DM18 Necessary-condition pruning before separation** (sign-based row marking, projection filtering) [D022 pp. 7–10; D023 pp. 9–13].
- **DM19 Collect, then apply** (deterministic parallel lifting) [R021 p. 52].
- **DM20 Cheap pre-screens for pairwise comparisons** (signatures, two-level hashing, crowded-bin sorting) [D004 p. 154; R021 p. 45; D030 p. 5].
- **DM21 Broadcast the presolved instance once; ship subproblems as bound changes; checkpoint only primitive nodes** [R014 pp. 6, 8–9] (co-signed).

### 7.3 Experiment and evaluation protocols

- **EP1 Knock out from the full default, in the main solve only**, saying when a change acts through model size [R021 pp. 5, 21; D011 p. 29; D010 pp. 18–21].
- **EP2 Shifted geometric means with the shift stated; time-outs at the limit, bias stated** [D004 pp. 333, 335–336; D010 p. 28; D030 p. 11; D021 p. 2].
- **EP3 Weight single-class sets as pseudo-instances in the total** [D004 p. 336].
- **EP4 Brackets by the slower run; affected models by iteration counts; no affected figure where both sides time out** [R013 p. 27; D030 p. 11; R021 pp. 5–6; D022 p. 11; D023 p. 14].
- **EP5 Control subsets** (both-solved, equal path, all-optimal, same path) [R004 pp. 17, 19; D004 pp. 339–340; D022 p. 13; D023 p. 17; D029 pp. 17, 20].
- **EP6 Refuse conclusions on small affected sets; recheck a small-set gain before switching a default** [R021 pp. 19, 22, 40, 42; D011 pp. 34–35; R013 p. 27].
- **EP7 Interacting families: all off, one off, one on alone; compare the sums** [D004 pp. 125, 142; R017 pp. 6–7].
- **EP8 Locate the cost**: basic, switching and component time with the objects produced [R004 pp. 16–18]; the component's share of total time as a distribution [D022 p. 13; D023 pp. 17–18]; phase time against resource share [R020 p. 13; D017 TR pp. 13–15] (co-signed).
- **EP9 Measure by the job**: gap targets beside time to optimality [D004 pp. 143–146]; the primal integral normalised by the all-off run [R017 pp. 5–7].
- **EP10 Write the test-set rule**: an effort window on a reference solver [R003 p. 24; R004 p. 16]; a frozen older version plus a reference solver [D004 pp. 333–334]; other solvers choose, disagreeing instances dropped and counted [D010 p. 21; R012 p. 13]; purge with a deliberately weakened solver [R005 p. 3]; numbered suitability criteria with exclusion counts and a published selection model [D021 pp. 25–26, 31–36].
- **EP11 Sweep and read points**: (nodes, time) per setting, the knee named [R002 pp. 11, 13]; diagnose a fixed threshold by measuring the quantity it thresholds [R002 pp. 11–12, 20].
- **EP12 Oracle agreement quotients** [R001 pp. 13–14].
- **EP13 Formulation factorials**: collapse variants by presolve, report sizes after preprocessing, use the slowest-to-fastest ratio as a robustness number [R011 pp. 5–8].
- **EP14 Two codes, one algorithm**: compare directions and brackets, not absolute numbers [D023 pp. 21–22; D022 p. 14; D011 pp. 29–37].
- **EP15 Scalability grids with a deliberate worst-case family; limits stated as unsolved counts per grid point under a stated time limit** [D020 pp. 12–18].
- **EP16 Exact-arithmetic checks** of LP bases, returned solutions and cross-solver consistency [R005 pp. 5–6; D013 pp. 10–11; D021 pp. 22–23].
- **EP17 Detector against ground truth before speed** [D011 pp. 21–23; R013 pp. 17–19].
- **EP18 Repeat nondeterministic runs; count instances solved in every run** [D029 p. 20; R018 pp. 19–21] (co-signed).
- **EP19 Fair yardstick**: equal gap tolerances, the same LP solver, the strongest baseline [R001 p. 11; R003 p. 24; R004 p. 16; D004 pp. 313, 317, 334, 391; R011 p. 5].

### 7.4 Writing moves

- **WM1 Fix a percentage's meaning once and keep one table layout** (positive values worse) [D004 pp. 16, 83].
- **WM2 The loss beside the gain in the abstract** [R004 p. 2]; when not there, in the body with numbers [D022 p. 11; D023 pp. 15–16].
- **WM3 Hedge where the counts are small, trust where they are large** [D011 pp. 34–35; R013 p. 27].
- **WM4 Label claims without a table; "a possible explanation"** [D004 pp. 69, 88, 93, 95, 142, 154, 191].
- **WM5 Print refuted impressions, losing defaults and losing trajectories next to the evidence** [D004 pp. 96, 114, 177; R006 pp. 7–9].
- **WM6 Each rule as a diff of the previous one** (algorithm boxes, a feature-difference table) [R001 pp. 6, 9].
- **WM7 Credits per component in the text; independent discovery named** [D004 pp. 75, 115, 132, 179, 199].
- **WM8 State the exact model, build and versions; post the model files** [R011 pp. 5, 8; D023 p. 13; D004 pp. 333, 391–392].
- **WM9 A neutral lesson from the reading** (house rule): reconcile tables, text and abstract before release, and print the numbers a verdict rests on next to the verdict.

---

## 8. Trajectory as seen in the full texts

Studies are distinct works after merging pairs (any read level); *full* counts those with a full or partial text.

| Period | Studies (full) | Main topics in the cards | Full-text anchors |
|---|---|---|---|
| 2000–2004 | 5 (4) | Branching in SIP (2), application modelling in a group (1), the SCIP framework (1); a polyhedral diploma thesis (metadata) | [R001; D024 TR; R002; R003]; D036 |
| 2005–2009 | 16 (13) | SCIP/CIP framework (4: the thesis, two CIP reports, the MPC paper), conflict analysis, chip verification, MIPLIB 2003, the objective pump, counting, formulation sensitivity, teaching software, structure detection (Mcf), an LP heuristic for an interval method; abstracts: ParaLEX, hybrid branching | [R004; R005; R006; R007; D004; R008; R009; R010; R011; R012; D010; D026; R013] |
| 2010–2014 | 11 (7) | Parallel search (3), MIPLIB 2010, rounding heuristics and the primal integral, presolve (RAMP 2014), editorial work; abstracts: hybrid solving survey, implied literals, 12 years of progress | [R014; R015; R017; R016; R019; R018; D030] |
| 2015–2019 | 2 (2) | Parallel records, the presolve taxonomy | [R020; R021] |
| 2020–2025 | 5 (5) | Parallel records, an exact feedback-arc-set method, MIPLIB 2017, RLT cuts (two versions) | [R022; D020; D021; D022; D023] |

**Turns visible in the full texts.**
- *From a rule inside another solver to his own framework.* The 2002 rule runs in SIP with CPLEX as LP solver [R001 p. 11]; SCIP was begun in October 2002 [D004 p. 20] and described as version 0.78 in 2004 [R003 pp. 2, 24].
- *SAT and CP into MIP, pulled by an application.* Conflict analysis (2005) takes its infeasible test set from chip verification [R004 pp. 2–3, 16]; the CIP class and the property checker follow [R008 pp. 2–3; D004 pp. 199–202; R009 p. 2; D010 pp. 29–37].
- *The evaluation protocol consolidates in steps:* totals over a set the code selected (2002) [R001 pp. 10–11] → on/off in the default with both-solved subsets (2005) [R004 pp. 16–17] → the thesis protocol (2007) [D004 pp. 333–340] → slower-run subsets with affected rows (2009–10) [R013 pp. 26–27; D011 pp. 33–34] → the bracket table and refusals of small affected sets (2014–16) [D030 pp. 10–12; R021 pp. 5–6, 19, 22, 40, 42] → brackets with all-optimal subsets in two codes (2022–25) [D022 pp. 10–14; D023 pp. 14–22].
- *After 2009 the written record is co-signed* community, library and parallel work; the last sole-authored paper (a 2013 patent aside, not read) is the 2009 SCIP paper, written at ZIB and acknowledging his move to CPLEX [D010 pp. 1, 38].
- *Gurobi (from 2014):* documentation of a production solver's components with measured impact [D030 pp. 1, 15; R021 pp. 4, 67]; joint work with ZIB on RLT cuts for bilinear products, measured in both SCIP and Gurobi [D022 p. 14; D023 pp. 21–22]; the library line continues [D021 p. 2].

**What stayed constant.** Knock-out against the full default, read per set, from 2005 [R004 pp. 16–17] to 2025 [D023 pp. 14–22]; time printed beside node counts, from 2002 [R001 p. 11] to 2025 [D023 p. 16]; budgets in solver-internal units, from 2004 [R002 p. 6] to 2023 [D022 p. 10]; failures and exclusions counted and named, from 2004 [R003 p. 25] to 2025 [D023 p. 14]; three MIPLIB editions, 2005, 2010 and 2021 [R005 p. 3; D013 p. 2; D021 p. 2].

**Against SKILL.md's Research Trajectory and note 06.** The full texts agree that the turns follow institutional moves (ZIB → ILOG/IBM → Gurobi). They add the 2000–2002 items of §3.2 item 22, date the bracket form's first written appearance to 2009 (§3.2 item 2), and give the CPLEX years co-signed full texts (§3.2 item 17).

---

## 9. Collaboration pattern

Studies per employer period, pairs merged; the thesis counts as sole-authored.

| Period | Studies (full) | Most frequent coauthors (studies) | Pattern seen in the full texts |
|---|---|---|---|
| 2000–2007, ZIB | 12 (10) | Koch 6, Martin 4, Grötschel 2 | Sole-authored core papers: the SCIP framework report, the conflict report and the thesis [R003; R004; D004]. Branching and the 2003 library with Koch and Martin [R001; R002; R005]; teaching software with Grötschel and Koch [R007]; property checking with industry and university partners [R008 p. 2]; a project report with eight authors in alphabetical order [D024 TR p. 2]. The thesis credits Koch and Martin, Wolter, Berthold, Brinkmann and Wedler by chapter [D004 pp. 75, 115, 132, 199] |
| 2008–2013, ILOG/IBM | 19 (13) | Koch 8, Berthold 8, Heinz 6, Shinano 4, Wolter 3 | One sole-authored paper [D010]; CIP and counting reports with ZIB students and colleagues [R009; R010; R012]; the Mcf-separator with Raack [D011]; a 16-author library [R015; D013]; heuristics with Berthold and Hendel [R017]; the parallel line with Shinano first [R014; R018; R019]; IBM colleagues on implied literals and CPLEX progress [D016; D028]; a guest heuristic in a chemical-engineering code [D026 p. 1] |
| 2014–2025, Gurobi | 8 (8) | Gleixner 3, Koch 3, Berthold 3, Shinano 3; Bixby, Gu, Rothberg, Weninger 2 | Five-author presolve papers with Gurobi's founders, alphabetical, roles not stated [D030 p. 1; R021 p. 3]; ParaSCIP records, Shinano first [R020; R022]; MIPLIB 2017 as 4th of 16 and a committee member [D021 p. 2]; RLT with Bestuzheva and Gleixner, last author [D022 p. 3; D023 p. 1]; feedback arc sets with a Vienna group, last author [D020 p. 1]. No sole-authored text |

**Across the career.** Koch is the most frequent coauthor (17 of 39 studies, 2002–2021), then Berthold (12, 2005–2021), Heinz (8), Shinano (7, from the 2008 ParaLEX abstract [D006]), Martin (4, 2002–2005) and Gleixner (4, 2010–2025). Baharev appears in 2009 and 2021 [D026 p. 1; D020 p. 1].

**Byline.** Until 2011 his name stands first on most bylines, many of them alphabetical, so position says little; sole authorship is the only firm signal, and among papers it ends in 2009. Apart from the part D026 names as his [D026 p. 7] and Danna's credited variability work [R015 p. 22], no co-signed text states roles; the cards infer at most that the Gurobi- or CPLEX-internal runs were his (the CPLEX-internal Mcf set [D011 p. 34]; the Gurobi 10.0 beta runs [D022 p. 14]), labelled *inferred*.

**Partners.** An EU telecommunication project [D024 TR pp. 1–2]; chip-verification partners [R008 p. 2; D004 p. 199]; ZIB through the Research Campus MODAL in the Gurobi years [R021 p. 1; D023 p. 22]; supercomputer centres for the parallel records [R014 p. 10; D018 TR p. 13].

---

## 10. Rejected updates

1. **A seventh core method for the answer-type split**: fails exclusivity; written into H8 (§5 A).
2. **A standalone heuristic *delegate to the host***: all evidence co-signed, and it duplicates Method 5 step 1 and Method 6 step 3; variant notes only (§5 D).
3. **A standalone heuristic *correctness contract separate from speed callbacks***: one SCIP design restated in 2004, 2008 and 2009 [R003 p. 9; R009 p. 5; D010 pp. 7–8], already Method 5 step 3.
4. ***Collapse variants by presolve equivalence* and *formulation robustness as a design criterion*** as new items: already in H6.
5. **Methods or heuristics from the ParaSCIP clusters** (racing on variability, forced restarts as reorganization points, repeats of nondeterministic runs, lost-work accounting, cross-version probes, phase-time diagnosis, parallelization as an algorithm change, open instances as targets): one project line, Shinano first, no role assignable to Achterberg; they enter only as variant notes on Misreading 1, H5 and the Roundtable Card.
6. ***Refuse a single-number solver ranking*** as a heuristic: co-signed only, and at odds with his sole-authored practice of one weighted total and a derived headline factor [D004 p. 336; D010 pp. 2, 29].
7. **Test-set selection as an optimization model** as a method of his: a 16-author committee paper; Taste mark 6 evidence only.
8. **Necessary-condition pruning before separation** as a heuristic: one study line (RLT), co-signed; technique inventory (DM18).
9. **A separate Method 4 or Method 2 for the control-subset and factor-split clusters**: both are reading rules of the existing methods; new steps instead (§2).
10. **Deleting Misreading 1**: reworded (§3.2 item 3), not deleted.
11. **Narrowing Method 3 because no Gurobi-era text sweeps a family**: absence of evidence in a closed-code period; an era note only.
12. **Carrying the cards' notes on inconsistencies inside works** (table against text, count slips, typos) into SKILL.md: barred by the house rule; one neutral lesson (WM9).
13. **Per-call applicability guards** as a heuristic: Method 1's no-op path applied per call; evidence only.

---

## 11. Open gaps

- **Journal versions.** D001, D002, D003, D005, D007, D008, D014, D015 and D019 are read through their reports; any change between versions is unknown except where both texts were read, and there the 2010 gate study changed (§3.3).
- **The origin of the bracket form.** The 2013 analysis with Wunderling is an abstract [D028]; the co-signed 2014 and 2016 texts credit their table form to it [D030 p. 11; R021 p. 5]. Whether the 2009 slower-run subsets [R013 pp. 26–27] are his or his coauthor's is not stated.
- **CPLEX-era non-report works** are abstracts: ParaLEX [D006], hybrid branching [D009], implied literals [D016], the hybrid-solving survey [D027], the progress analysis [D028]. First-hand method evidence for 2006–2014 is co-signed or abstract-level.
- **The diploma theses.** The mathematics thesis under his former name is metadata only [D036]; the computer-science thesis with the learning experiment, the stated origin of H1, was not found.
- **The 2003 UMTS chapter** was read only in its 2002 report version [D024 TR p. 2]; differences are unknown.
- **The thesis** was read at chapter level: Chapters 2, 3, 6–10, 13–15 in part, Appendix B mostly not, Chapter 14's operator sections not (card b01, chapter map); claims resting on its unread parts are not made here [D004].
- **Who did what** in co-signed work: no card can assign a passage to him; the ParaSCIP and library texts are especially opaque.
- **Gurobi internals**: closed code and private test sets [D030 p. 11; R021 p. 5; D022 p. 14; D023 p. 21]; no Gurobi-era sole statement on method.
- **Permutations in 2025**: the procedure behind the permuted copies is not described [D023 p. 14].
- **Sealed material.** Five holdout items, one candidate cluster and one single-card candidate are withheld until the validation unseals them; the pages that carry them are not used in this note.
- **The two patents** (Role = skip) are not read.

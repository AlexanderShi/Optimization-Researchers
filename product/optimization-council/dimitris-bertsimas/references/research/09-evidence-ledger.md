# Dimitris Bertsimas · Evidence ledger

> Date: 2026-10-29 (stage T3.6, first synthesis round). This file holds the full evidence behind `SKILL.md`. SKILL.md keeps, per item, the strongest statement, the three to five strongest cards, a one-line say–do count, at most four variant or correction bullets and a pointer to the matching section below. Each section here has two parts: **Before this synthesis**, the SKILL.md item as it stood after the web-research pass of 2026-10-28, copied verbatim (in a code block, so its relative links and labels are kept exactly as they were), and **Full-text evidence**, the card evidence from the deep reading of 2026-10-29, taken from `08-deep-reading-synthesis.md` and the cards. Nothing from the earlier wording was deleted: where the full texts contradict it, the correction is stated here and listed under [Corrections from the full texts](#corrections). **Fix round** (same day, after three read-only reviews): misattributed citations and dates were corrected, the version pairs S016 = S261, S032 = S597, S340 = S197 and S328 = S914 were merged in the method, heuristic, cluster and evidence-work counts (the period, domain and coauthor tables still count them separately, which moves at most two works per period), and the changes are marked *Fix round* in the sections below.

**How to read.** `[S012 p. 9]` = paper card S012 (index: `07-paper-cards.md`; batch files in `cards/`), at the file page (`[[page N]]`) of the version the card names; abstract- and metadata-level cards are cited by ID only. Quotations are copied from the cards' verified `quotes` fields; everything else is paraphrase. Say–do counts are distinct works read in full or in part whose cards link the method (`method_links`: evidence / variant / contradiction), after the counting rules in [Card key](#card-key); a work can carry several relations. Method 7 and Heuristic 10 were promoted at this synthesis, so no card links them by name; their counts are the works in the candidate clusters of 08 §6. Proof devices, design moves, protocols and writing moves are collected in `../technique-catalog.md`.

**Scope.** Sections exist for every SKILL.md item that this synthesis changed or condensed. Items not listed (frontmatter, Activation Rules apart from the disclaimer line, Research Integrity Rules, Agentic Protocol, Mentor Voice, the Sources lists) were not condensed and remain complete in SKILL.md; the earlier frontmatter and disclaimer wording is kept under [Corrections](#corrections).

**Tighten step (T3.7, 2026-10-29).** To fit the skill budget, SKILL.md was cut from 12,174 to 11,400 words (`wc -w`) without deleting anything: every SKILL.md line that was shortened is copied verbatim, as it stood before the cut, under **Moved at the tighten step** at the end of its section below (taste marks and warning signs, Methods 1–7, Workflows B–E, Heuristics 1–10, the six anatomies, the domain map's HS row, research trajectory, academic lineage, inner tensions). What moved: second and later card citations of an item, DOIs, per-work case lists, historical details and two quotations. Frontmatter, How to Use, Activation Rules, Research Integrity Rules, Research Task Routing, Agentic Protocol, the taste quick-check, anti-patterns, Mentor Voice, Roundtable Card, Honest Boundary (with its corrections list) and Sources were not changed.

**Review fix (T3.7, 2026-10-29).** A read-only review of the cut found scope evidence and working detail that SKILL.md still needs. They were put back from the copies below, which stay in place, and SKILL.md now has 11,494 words (`wc -w`). Back in full, so that the SKILL.md line again equals its copy under **Moved at the tighten step**: the domain map's HS row, taste mark 6, the *Stated* lines of Methods 3, 6 and 7 (the evidence behind their say–do scope), Method 7's *Different from standard practice* line and Heuristic 10. Back in part: Heuristic 2 (its four response moves), Heuristic 3 (local search over the structural variables) and Workflow C step 5 (batch means and the confidence-interval stop, with the step's first card citation only). Additions only, nothing removed: Method 4 step 5 now asks for path-to-path timing (C8), the one check from the critics' list in Method 4's copy below that SKILL.md no longer named, and the Stage Workflows pointer now says that the workflow sections also hold the citations cut here.

## Contents

- [How to Use](#how-to-use) · [Research task routing](#routing) · [Domain map](#domain-map)
- [Taste: marks of good research](#taste-marks) · [Taste: warning signs](#taste-warnings) · [Taste quick-check](#taste-quick-check)
- [Core methods: counting note](#methods-note) · [Method 1](#method-1) · [Method 2](#method-2) · [Method 3](#method-3) · [Method 4](#method-4) · [Method 5](#method-5) · [Method 6](#method-6) · [Method 7](#method-7)
- [Workflow A](#workflow-a) · [B](#workflow-b) · [C](#workflow-c) · [D](#workflow-d) · [E](#workflow-e) · [F](#workflow-f) · [G](#workflow-g)
- [Heuristics 1](#heuristic-1) · [2](#heuristic-2) · [3](#heuristic-3) · [4](#heuristic-4) · [5](#heuristic-5) · [6](#heuristic-6) · [7](#heuristic-7) · [8](#heuristic-8) · [9](#heuristic-9) · [10](#heuristic-10)
- Anatomies: [achievable region](#anatomy-achievable-region) · [moment bounds](#anatomy-moment-bounds) · [price of robustness](#anatomy-price-of-robustness) · [best subset and trees](#anatomy-best-subset-trees) · [prescriptive analytics](#anatomy-prescriptive-analytics) · [dynamic routing](#anatomy-dynamic-routing) · [execution costs](#anatomy-execution-costs)
- [Anti-patterns](#anti-patterns) · [Research trajectory](#research-trajectory) · [Academic lineage](#academic-lineage) · [Inner tensions](#inner-tensions) · [Roundtable card](#roundtable-card) · [Honest boundary](#honest-boundary) · [Book material](#books)
- [Corrections from the full texts](#corrections) · [Card key](#card-key)

<a id="how-to-use"></a>
## How to Use

**Before this synthesis** (verbatim):

```text
## How to Use

**Strengths** (stages with evidence): problem choice; formulation that keeps the nominal class; experiments for MIO-based statistics and robust optimization; judging decisions against the owner's current rule; deployment; multi-student programmes; convening this council.

**Weak spots**: the not-voiced and no-evidence rows of Research Task Routing; CP and SD voiced from co-authored papers only; HS thin; LO textbook-era only.

**Domain fit**: for guest delegations the lens transfers to *models* (class, knob, baseline, decision metric), not to solver internals, which his record treats as black boxes.

**Evidence pointers**: `[02 T1]` = item T1 of research note 02; `[01 SW3]` = signature work 3 of note 01; `§` = section. Notes: [01 publications](references/research/01-publications.md), [02 stated methodology](references/research/02-methodology.md), [03 process evidence](references/research/03-process-evidence.md), [04 mentorship](references/research/04-mentorship.md), [05 peer critique](references/research/05-peer-critique.md), [06 trajectory](references/research/06-trajectory.md). Labels: [stated] his words; [stated-joint] a co-authored text; [practice] papers, code and records; [observed] others' reports; [inferred] this skill's reading. Author order is alphabetical by convention 1995–2019 and signals nothing; after about 2010, code, preprints and much writing are his students' and postdocs' work under his direction [01 §1.4; 03 B7].
```

**Changes.** Strengths add bounding a policy when no exact solve exists (Method 7). Weak spots: SD is no longer a weak spot (stated in sole-author texts, C1); the books were read at abstract level only. Domain fit: the claim that his record treats solver internals as black boxes is narrowed (C5): from 2009 his group builds tailored algorithms when a model leaves the solver class, a cardinality-constrained QP algorithm after the general MIQP proved unsuited [S040 pp. 2, 6, 10, 12, 15], a first-order method for SOS relaxations [S315 pp. 8–12], a solver bake-off before a tailored outer approximation [S105 pp. 7–9], a custom branch-and-bound for sparse PCA [S184 pp. 8–18], closed-form Benders cuts without an LP solver [S093 pp. 10–13], Kelley's method diagnosed through its bound's constant [S302 pp. 1, 5–8], spatial branching on matrix variables [S385 pp. 2, 6, 10–14], a group global solver extended to integers [S624 pp. 10–16], a custom pricing routine [S316 pp. 3, 5, 11], a tailored algorithm because commercial solvers fail [S083 p. 15]. In 1994 the stated choice had been a commercial package over custom algorithms [S036 p. 7]. Evidence pointers now explain card citations, the ledger and the technique catalog.

**Increment books-2026-10-29** (2026-10-29; book material, framing and dating only, outside every say–do count; full account: [Book material](#books)). *Weak spots*: the clause on the books now says what was read: their open parts, never their bodies. The line before this increment (verbatim):

```text
**Weak spots**: the not-voiced and no-evidence rows of Research Task Routing; CP stated only in co-authored texts; HS thin; LO textbook-era only; his books were read at abstract level only.
```

<a id="routing"></a>
## Research task routing

**Before this synthesis** (verbatim):

```text
## Research Task Routing

Enter at the matching row; take missing upstream inputs (e.g. the programme card) from the user's message, marked *(assumed)*. **Stuck**: run that row's stop rule first, before any new model or experiment; its outcome is the conclusion.

| User says | Workflow | Methods |
|---|---|---|
| "Is this worth doing?" "Help me choose" "Plan a programme" "It is NP-hard" | A: Problem choice (step 3 if *intractable*) | 6, 5, 2, 1 + Taste quick-check |
| "How do I formulate this? Can the robust version stay an LP/MIO?" "How do I decide from predictions?" | B: Formulation | 1, 3, 4, 5; Heuristics 1, 5 |
| "Design the experiments and baselines" | C: Experiments | 4, 5 |
| "Are these results good?" | D: Judging results | 4, 5; Heuristic 4 |
| Stuck: "the bound does not move" | C checkpoint | Method 4 stop rule; Heuristic 3 |
| Stuck: "the set made it slow, nonconvex or too conservative"; "which Γ?" | B checkpoint | Method 1 and 3 stop rules |
| Stuck: "it loses to the current rule"; "not adopted" | D checkpoint | Method 5 checkpoints; Heuristic 4 |
| "Frame the abstract; where to publish" | E: Writing (medium evidence) | Heuristic 9, Method 2 |
| "A critic attacked the paper" | F: After publication | Heuristic 2, Method 6 |
| "How do I supervise a group?" | G: Supervision | Heuristic 8, Method 6 |
| "Lead a cross-team discussion" | Activation Rules: hand-over, or convener when convened | 5, 1, 2, 3 |
| Stochastic programming as its own tradition, ADP and RL, statistical learning theory, constraint programming; Dimitri P. Bertsekas | not voiced: say so; for a tradition, offer only Bertsimas's own route, labelled | — |
| Literature search, proofs, code, refereeing, rejections, talks, time management, closing a programme | none: say "no distillable Bertsimas method"; label generic advice "not Bertsimas-style" | — |
```

**Changes.** Added rows: "How good is my policy or heuristic? No exact solve exists" (Method 7; Heuristic 3) and "Which proof device, protocol or writing move fits?" (technique catalog). Method 7 joined the experiment, judging and cross-team rows; Heuristic 10 joined formulation; the stuck-bound row adds Method 7 step 6. The no-method row now says *finding proofs*: the proof devices his papers use are documented from the full texts (technique catalog §1), but how he finds proofs is not. *Fix round*: the stuck-bound row now routes first to a stronger formulation (Workflow B step 1; catalog §1.1), the remedy the full texts document: big-M replaced by a closed-form inner problem or a perspective form, solved by outer approximation [S061 pp. 6–10; S175 pp. 9–10, 15–16; S136 pp. 3, 6–7, 26–27]; Method 7 step 6 is kept for bounds of policies.

<a id="domain-map"></a>
## Domain map: corrections from the full texts

**Before this synthesis** (verbatim):

```text
## Domain Map (team.json codes)

M = Method, H = Heuristic, T = Tension.

| Code | Voice | His moves | Anchor works | Delegations | Cautions |
|---|---|---|---|---|---|
| **LO** | textbook-era taste | Geometry before algebra; LP as the engine of relaxations and robust counterparts (M1) | *Introduction to Linear Optimization* (Athena Scientific 1997, ISBN 1886529191); DOI 10.1007/BF01582057 | LP, NLP | Dormant as a topic after 1998 |
| **IO** | stated + practice | Strong formulations (stated 2005); LP-relaxation rounding; MIO as the engine of RO and ML (M2, M4, H3, H5) | DOI 10.1007/BF01580607; DOI 10.1137/20M1346778 | MINLP, LP | T4: weak big-M in practice |
| **RO** | stated + practice | Class inheritance (M1); price of robustness (M3); adaptive policies with self-quantified limits; data-driven sets; H1 | DOI 10.1287/opre.1030.0065; DOI 10.1287/moor.1100.0444; DOI 10.1137/080734510 | NLP, MINLP, DFO | Why he entered RO and how Γ arose: unknown |
| **CP** | co-authored papers only; no stated methodology found | Probability questions as convex programs; worst case from the dual; NP-hardness mapped (M1) | DOI 10.1137/S1052623401399903; DOI 10.1287/ijoc.2023.0345 | NLP, MINLP | No critique or process artefact found |
| **SD** | co-authored papers only; no stated methodology found | Achievable region (M1); stochastic routing; robust queueing; ML-trained bandit policies | DOI 10.1287/opre.38.6.1019; DOI 10.1287/moor.21.2.257; DOI 10.1287/opre.2015.1367 | none | Whitt–You critiques unanswered [05 §4.5]; T3 |
| **ML** | stated + practice (strongest) | M2, M4, M1; H1–H3; interpretability required | DOI 10.1214/15-AOS1388; DOI 10.1007/s10994-017-5633-9; DOI 10.1214/19-STS701 | MINLP, NLP, DFO | SNR, timing, certification, strength and reproducibility critiques [05 §1–2] |
| **DA** | stated + practice | M5; H5 | DOI 10.1287/mnsc.2018.3253; DOI 10.1287/opre.2021.0707 | all four | Prescriptive-tree counterexample unanswered (DOI 10.1287/mnsc.2021.02813) |
| **HS** | practice + the 1993 verdict | Heuristics as warm starts, components, fallbacks (M4, H3); the 1993 review found SA's theory lacking | DOI 10.1214/ss/1177011077; DOI 10.1287/opre.1090.0715 | DFO | Convergence of his robust local search not read; T2 |
| **AP** | stated + practice | Partners as validation (M5); companies and applied write-ups (M6, H9) | DOI 10.1287/opre.1080.0619; DOI 10.1073/pnas.1811462116; DOI 10.1287/opre.2022.2306 | all four | Outcomes thin; Boston and DELPHI contested [05 §5] |
```

**Full-text evidence per corrected row** (08 §3 rows 1–5; the later domain-layer step replaces this map).
- **SD voice** (C1): nine sole-author SD works were read in full: the thesis [S048 pp. 11–13]; queueing papers with stated motives [S239 pp. 1–2, 8, 12; S168 pp. 1–2, 14]; a priori routing [S833 pp. 6, 9; S186 pp. 2, 16–17; S148 pp. 1–2, 5]; a 1992 paper that states its approach and judges it [S017 pp. 3, 12]; the 1994 working paper and the 1995 survey that state the method [S580 pp. 5, 10; S185 pp. 1–3]. Co-authored statements too [S072 p. 2; S051 p. 1]. Quote: "This approach is based on the thesis that the essential difficulty in stochastic and dynamic optimization is primarily the dynamic and combinatorial character of the problem and only secondarily the stochastic character of the problem." [S580 p. 10].
- **CP voice** (C1): no sole-author CP text beyond the surveys' SDP proposals [S185 pp. 44–45]; co-authored statements frame bounds as convex and semidefinite programs [S018 p. 1] and claim that optimization improves classical results [S007 p. 35]. Quote: "In this paper, we formulate the problem of obtaining best possible bounds as an optimization problem and use modern optimization theory, in particular convex and semidefinite programming, to give concrete answers to the questions above." [S018 p. 1].
- **IO anchor** (C2): DOI 10.1007/BF01580607 [S052] has no rounding step: it bounds tree and matching constructions by the LP value and gives tight families [S052 pp. 10–18, 20–21]. Rounding is in the ground-holding LP [S036 pp. 6–7], one-threshold multicut rounding [S658 pp. 18–20], dependent rounding [S121 pp. 3–9], designed-distribution rounding [S435 pp. 3–6] and covariance rounding [S007 pp. 33–35]. Strong formulations are stated already in 1998: "the key to solving large scale integer programming problems is to obtain strong formulations, which include facets of the convex hull of solutions" [S015 p. 2].
- **LO** (kept): LP-algorithm papers are 1994–1998 [S269 pp. 3–4; S289 pp. 2, 7–11; S156 pp. 1–2, 22–23]; later LO is an engine (column generation for convex-hull prices [S196 pp. 4–5, 8–10]).
- **HS caution** (C3): an asymptotic annealing theorem is offered for runs stopped at an empirical threshold, with a global-optimum claim [S141 pp. 5–6, 9, 11]; the robust local search family leaves the solver class on purpose and carries no certificate [S278 pp. 2–6; S116 pp. 5, 8–9, 13–14]. *Fix round*: the row's own anchor, DOI 10.1287/opre.1090.0715 [S090], is read in full: it proves convergence only for convex costs, with an exact worst-error oracle and diminishing steps (Theorem 2), and calls the practical nonconvex method a heuristic [S090 pp. 5–6, 16–17]; worst cases are estimated, with late discoveries admitted, so there is no certificate [S090 pp. 12, 15]; it needs gradients [S090 p. 2]. The 1993 verdict: theory lacking; practice mixed (better on sparse graph partitioning and worse on some structured graphs, far slower on colouring, behind Lin–Kernighan on the TSP) but generally applicable; the equal-time comparisons it reports are Johnson et al.'s, not his own experiments [S005 pp. 3–5].
- **AP caution** (C4): field outcome studies exist: a difference-in-differences study against the prior year plus a stratified comparison [S115 pp. 22–24], with post-deployment maintenance [S115 pp. 25–26]; length of stay measured after a staggered roll-out that supplies the control group [S617 arXiv pp. 11–14, 22–25, 37–39]; an additive impact ledger against the owner's old rule [S339 pp. 10–11]; deployed routing with the owner's scaled-down adoption [S137 p. 3]. Boston and DELPHI stay contested ([Method 5](#method-5)).
- **RO**: a 2002 working paper with Pachamanova already uses a budget Γ normalised by standard deviations to narrow computed bounds [S653 pp. 12–14, 24]; why he entered RO and how Γ arose stay unknown (the 2026 retrospective is abstract-level [S614]).
- **Method 7** was first added to the LO, IO, CP, SD and RO rows' moves (the bound as yardstick; see [Method 7](#method-7)). *Fix round*: those additions corrected no contradicted row, so they were removed to keep the map unexpanded, as the operator asked; the RO row's earlier wording "adaptive policies with self-quantified limits" is restored; the domain-layer map that replaces this table should cite Method 7 in its SD, IO, CP and RO rows (08 §4).

**Moved at the tighten step** (T3.7, 2026-10-29). These SKILL.md lines are copied verbatim as they stood before the cut; SKILL.md now keeps a shorter form of each, and the card citations, pages, DOIs and quotes it dropped are kept here.

| Code | Voice | His moves | Anchor works | Delegations | Cautions |
|---|---|---|---|---|---|
| **HS** | practice + the 1993 verdict | Heuristics as warm starts, components, fallbacks (M4, H3); 1993: theory lacking, practice mixed but generally applicable (C15) | DOI 10.1214/ss/1177011077; DOI 10.1287/opre.1090.0715 | DFO | Robust local search converges only for convex costs with an exact oracle; otherwise a heuristic without certificate (C3); T1, T2 |

**Increment books-2026-10-29** (2026-10-29; book material, framing and dating only, outside every say–do count; full account: [Book material](#books)). The Voice cells of LO, IO, RO, ML, DA and AP now name the book text that states the domain's view, with its page; LO's and ML's Cautions gain one reception line each; the HS row is re-dated to 1992 (C22). CP and SD are unchanged: no book page gives them a voice (the 2005 IO book lists semidefinite and polynomial methods inside IO [B006 p. 1]; the 2022 queueing book's page has a structure and no first-person sentence [B013 p. 1]), so their labels stay as C1 set them.
- **LO**: the 1997 preface, joint with Tsitsiklis, read in full in its web form [B001 p. 1]; "Dormant as a topic" narrowed to research, since the book was kept in print and corrected until 2021 [B003 pp. 1–5] and LO opened his 2009 methods course (lectures 1–9) [B021 p. 2]; Ramana's 1997 review praises the pedagogy and finds the book dense in places, with chapter 7 overloaded [B005 pp. 13–14].
- **IO**: the 2005 statement now has a page [B006 p. 1], and a second stated sentence comes from his 2017 page [B008 p. 2]; "taught 1997": a section "Guidelines for strong formulations" in the LO textbook [B004 p. 4], with "some intuition as to what constitutes a ``strong'' formulation" in the preface [B001 p. 1].
- **RO**: the 2022 book page, joint with den Hertog [B011 p. 1]: ARO before nonlinear RO, nonlinear RO by concave versus convex uncertainty, applications under Dantzig's quotation. Cautions unchanged: the 2000 MBA text has a starred section "Linear Optimization Under Uncertainty" [B015 p. 4], whose content was not read, so why he entered RO and how Γ arose stay unknown.
- **ML**: the six principles [B009 p. 1]; reception: Cuvelier (2020) finds no widespread implementation of most of the book's algorithms, and the stance not yet followed by the wider AI community [B010 p. 1].
- **DA**: the 2004 page with Freund [B014 p. 1] and the 2016 page with O'Hair and Pulleyblank [B017 p. 1].
- **HS**: the verdict is in print in 1992, in the NRC report *Probability and Algorithms*, with the same text as the 1993 journal version [B020 pp. 8–10] (C22).
- **AP**: the 2025 health book's site, joint with Orfanoudaki and Wiberg [B019 p. 2].
- *Fix round*: each new Voice citation now says "joint" (IO, RO, ML, DA, AP), as LO's "stated jointly" does (C1); DA reads "MBA and analytics texts", since the 2016 book was taught to an audience of "MBA, undergraduate and graduate students", to executive MBAs and in a MOOC [B017 p. 1]; IO's "taught 1997" cites the preface beside the contents [B001 p. 1; B004 p. 4]; ML's Caution, formerly "few released implementations", now follows the reviewer's "il n'existe pas encore d'implémentation répandue pour la plupart des algorithmes présentés" [B010 p. 1]: an adoption point, not a code-release charge.
The domain-layer map that replaces this table should take its Voice entries from [Book material](#books), "Stated views per domain". The rows before this increment (verbatim):

```text
| **LO** | textbook-era taste | Geometry before algebra; LP as the engine of relaxations and robust counterparts (M1) | *Introduction to Linear Optimization* (Athena Scientific 1997, ISBN 1886529191); DOI 10.1007/BF01582057 | LP, NLP | Dormant as a topic after 1998 |
| **IO** | stated + practice | Strong formulations (stated 1998 and 2005); LP bounds (C2) and rounding; MIO as the engine of RO and ML (M2, M4, H3, H5) | DOI 10.1007/BF01580607 (a bound, not rounding: C2); DOI 10.1137/20M1346778 | MINLP, LP | T4: weak big-M in tree MIOs |
| **RO** | stated + practice | Class inheritance (M1); price of robustness (M3); adaptive policies with self-quantified limits; data-driven sets; H1 | DOI 10.1287/opre.1030.0065; DOI 10.1287/moor.1100.0444; DOI 10.1137/080734510 | NLP, MINLP, DFO | Why he entered RO and how Γ arose: unknown |
| **ML** | stated + practice (strongest) | M2, M4, M1; H1–H3; interpretability required | DOI 10.1214/15-AOS1388; DOI 10.1007/s10994-017-5633-9; DOI 10.1214/19-STS701 | MINLP, NLP, DFO | SNR, timing, certification, strength and reproducibility critiques [05 §1–2] |
| **DA** | stated + practice | M5; H5 | DOI 10.1287/mnsc.2018.3253; DOI 10.1287/opre.2021.0707 | all four | Prescriptive-tree counterexample unanswered (DOI 10.1287/mnsc.2021.02813) |
| **HS** | practice + the 1993 verdict | Heuristics as warm starts, components, fallbacks (M4, H3); 1993: theory lacking, practice mixed but generally applicable (C15) | DOI 10.1214/ss/1177011077; DOI 10.1287/opre.1090.0715 | DFO | Robust local search converges only for convex costs with an exact oracle; otherwise a heuristic without certificate (C3); T1, T2 |
| **AP** | stated + practice | Partners as validation (M5); companies and applied write-ups (M6, H9) | DOI 10.1287/opre.1080.0619; DOI 10.1073/pnas.1811462116; DOI 10.1287/opre.2022.2306 | all four | Outcomes measured in several deployments (C4); Boston and DELPHI contested (C12) |
```

<a id="taste-marks"></a>
## Taste: marks of good research

**Before this synthesis** (verbatim):

```text
### Marks of good research
1. **It would change teaching or practice within years, judged before starting** [02 T1, R1; 04 B.2].
2. **Tractable at the application's scale, by design** [02 T7; 01 SW3].
3. **Exact, joint optimization of what practice does greedily, by trial and error or by randomization** [02 G1, G2; DOI 10.1287/opre.2015.1361]. Tension T2.
4. **The decision is the object: prescription, not prediction** [02 R14; 01 SW5].
5. **Interpretable where people act on the result** [02 T6; arXiv 1907.03419; Optimal Trees, 03 B4.5].
6. **Problems and data first; a theory is tested by the problems that gave rise to it** (Dantzig's test, cited in two of his books) [02 P1, T5].
7. **A result is stronger with a certificate**: optimality, a gap, or a proof of infeasibility, which also counts [02 J2, R12]. Tension T1: dropped at scale in practice.
- LO and IO, textbook era: geometry first, then algebra and algorithms; strong formulations [02 T8, W6].
```

**Full-text evidence per mark.**
1. *Change teaching or practice, judged before starting*: not observable in papers (Method 6 step 1); teachability is sometimes argued after the fact [S018 pp. 4, 23].
2. *Tractable at the application's scale*: tractability redefined as solve times at realistic sizes [S010 p. 2; S178 pp. 3–5]; computation in real problems named the ultimate criterion [S001 p. 8]. Before about 2004 the papers argued from complexity classes and operation counts [S269 pp. 1, 21–22; S289 pp. 2, 6, 11–12] (C19).
3. *Joint optimization of what practice does greedily or randomly, after mapping where it pays* (08 §3 row 26): optimized assignment instead of randomization [S124 pp. 2, 4–6, 8; S312 pp. 1–2, 22; S357 pp. 3, 13]; optimized training samples [S873 pp. 3–8; S696 pp. 3–6, 16]; a regime map that recommends greedy where it is near-optimal [S046 p. 19]; crude mean imputation preferred for prediction after his group's earlier promotion of sophisticated imputation [S310 pp. 5, 12–13]. Quote: "In this situation, optimization is not extremely useful and we recommend using greedy, which is the fastest and the most interpretable." [S046 p. 19].
4. *Prescription, not prediction*: [S008 p. 29]; set sizes alone cannot predict decision performance [S013 p. 32]; but see the prediction-only clinical papers ([Method 5](#method-5), C11).
5. *Interpretable where people act* (08 §3 row 27): interpretability scoped by decision type, required where guidance changes standard care, black boxes acceptable for diagnosis [S685 pp. 2–3]; optimal trees chosen for clinicians [S276 p. 4; S682 pp. 2–7]. Counter-practice: boosted trees explained by SHAP in tools clinicians use [S054 pp. 4–9; S621 pp. 2–3, 16–18], and a trust ladder from optimal trees to a black box [S617 arXiv pp. 9–11, 20–21]. Quote: "Their transparent nature is critical: clinicians are unlikely to trust or adopt treatment guidance that comes from a black-box model, especially when the stakes involve altering standard care." [S685 p. 2].
6. *Problems and data first*: true of the OR and analytics lines ([Method 5](#method-5)); his CP line takes its questions from inside theory, with no owner, data or decision [S018 pp. 1, 3, 25].
7. *A certificate makes a result stronger*: "However, by design, the MIO approach maintains a suboptimality gap throughout computation and can therefore be terminated, before optimality is certified, with a certificate of suboptimality." [S225 p. 31]; dropped at scale ([Inner tensions](#inner-tensions), T1).
8. *A bound valid for every policy before any claim about a policy* (new, from Method 7): heavy- and light-traffic bounds before any policy is analysed [S016 p. 3]; "Furthermore, the quality of proposed heuristics is usually assessed by comparing their empirical performance with that of alternative heuristics, which gives little information about their degree of suboptimality." [S051 p. 1]; the sole-author survey's plan of attack [S185 pp. 1–2].
*Fix round*: SKILL.md keeps eight marks (framework §四 allows 5–8): mark 8 below was merged into mark 7 (a bound valid for every policy as the certificate of a policy), and mark 9 became mark 8, labelled [practice]; mark 5 now carries its counter-practice and C21; mark 6's exception is narrowed to the 2005 paper [S018 pp. 1–4].
9. *Limits printed beside the result* (new, from Heuristic 4 and cluster 2 of 08 §6): conjectures and loose constants in 1988–1993 [S048 pp. 100–101, 164–165; S016 pp. 7, 9; S032 pp. 7–8, 11, 16; S158 pp. 15, 17]; losing regimes [S010 pp. 30, 38–40]; few uncertain coefficients explain PILOT4 [S001 p. 14]; own tree losing to logistic regression said plainly [S276 p. 4; S296 pp. 5, 9]; non-implementation printed [S083 pp. 25, 27; S262 p. 12; S243 pp. 17–28]; own model the weakest predictor [S370 pp. 13–16].
- *Strong formulations* (LO and IO line): measured and pursued in practice too (C10): models judged by total unimodularity, facets and solve time in 1997 [S241 pp. 14–15, 27, 31–32]; facets designed so LPs are almost always integral [S015 pp. 2, 4–5, 10]; cover inequalities so only one of 41 instances branches [S109 pp. 2–8]; valid inequalities without which the model fails [S037 pp. 2, 4–8]; convex-hull and TU checks [S076 pp. 12–19, 35–36].

**Moved at the tighten step** (T3.7, 2026-10-29). These SKILL.md lines are copied verbatim as they stood before the cut; SKILL.md now keeps a shorter form of each, and the card citations, pages, DOIs and quotes it dropped are kept here.

5. **Interpretable where people act on the result**, required where guidance changes standard care [S685 pp. 2–3; 02 T6]. ⚠ Counter-practice: deployed hospital tools moved to boosted trees explained by SHAP once interpretable models had earned trust [S617 arXiv pp. 9–11; S054 pp. 4–9] (C21).
6. **Problems and data first; a theory is tested by the problems that gave rise to it** (Dantzig's test, cited in two of his books) [02 P1, T5]; the 2005 moment-bounds paper starts instead from a question internal to probability theory [S018 pp. 1–4] [practice].
7. **A result is stronger with a certificate**: optimality, a gap, or a proof of infeasibility, which also counts; for a policy, a bound valid for every policy (Method 7) [02 J2, R12; S225 p. 31; S016 p. 3; S051 pp. 1, 11]. Tension T1: dropped at scale in practice.

**Increment books-2026-10-29** (2026-10-29; book material, framing and dating only, outside every say–do count; full account: [Book material](#books)).
- **Marks 2–5**: each now also cites the 2019 book's principles [B009 p. 1]: practical tractability, not polynomial solvability (mark 2); optimization over randomization, with Part IV on design of experiments, exceptional responders, stable regression and the bootstrap (mark 3); prescription, not prediction (mark 4); interpretability "materially important" (mark 5). These are book-level principles, joint with Dunn, as the publisher presents them.
- **Mark 6**: Dantzig's test now has its pages: the 2004 book's mission [B014 p. 1] and the 2022 book's applications "guided by the quote of George Dantzig at the beginning of the preface" (the quotation itself was not seen; that it is the same one stays [inferred], 02 T5) [B011 p. 1]; problems and data lead in 2016 [B017 p. 1], carried out in the contents, where seven application parts precede the methods part [B018 pp. 1–5]. The 1997 preface states the test without naming Dantzig: "The success of any optimization methodology hinges on its ability to deal with large and important problems." [B001 p. 1]. ⚠ Variant added to SKILL.md: the same 1997 graduate text (pitched "at the PhD level" by its publishers [B002 p. 3]) puts theory first and the art chapter last [B001 p. 1; B004 p. 5]. Not added: the 2025 health book organises its Part I by method classes, each taught through one clinical example, and only Part II by problems [B019 p. 2]. *Fix round*: in SKILL.md the variant clause now carries its ⚠, and the B011 citation says "(the quotation unseen; same test [inferred])".
- **LO and IO, textbook era**: now with pages: geometry first [B001 p. 1]; "most importantly geometry" [B006 p. 1]; and a second 2005 sentence, "The key characteristic of our treatment is that our development of the algorithms is naturally based on the algebraic and geometric developments of Part II." [B008 p. 2]. The contents carry it out: the geometry chapter precedes the simplex chapter [B004 pp. 2–3], and algebra and geometry (chapters 6–8) precede the algorithm chapters [B007 pp. 2–3]; the 2009 course teaches geometry in lecture 2, before the simplex method and duality [B021 p. 2]. ⚠ The simplex-free derivation of duality is a starred, advanced section [B004 p. 3]. An outside check: Ramana finds the geometric explanations "widely successful" [B005 p. 14]. Still textbook and teaching material, so *geometry first in research* stays claimed but unverified.

The lines before this increment (verbatim):

```text
2. **Tractable at the application's scale, by design**: solve times at realistic sizes, not polynomial time [02 T7; S010 p. 2].
3. **Exact, joint optimization of what practice does greedily, by trial and error or by randomization, after mapping where it pays** [02 G1, G2; S124 pp. 2, 4–6; S046 p. 19]. Tension T2.
4. **The decision is the object: prescription, not prediction** [02 R14; 01 SW5; S008 p. 29].
5. **Interpretable where people act on the result**, required where guidance changes standard care [S685 pp. 2–3; 02 T6]. ⚠ Counter-practice: deployed hospital tools use SHAP-explained boosted trees [S617 arXiv pp. 9–11; S054 pp. 4–9] (C21).
6. **Problems and data first; a theory is tested by the problems that gave rise to it** (Dantzig's test, cited in two of his books) [02 P1, T5]; the 2005 moment-bounds paper starts instead from a question internal to probability theory [S018 pp. 1–4] [practice].
- LO and IO, textbook era: geometry first, then algebra and algorithms; strong formulations [02 T8, W6; S015 p. 2].
```

<a id="taste-warnings"></a>
## Taste: warning signs of bad research

**Before this synthesis** (verbatim):

```text
### Warning signs of bad research
1. Work that would change nothing if it succeeded, or that aims to impress [02 T1, T3].
2. Models harder than their nominal version; polynomial time without solve times [02 T7].
3. Greedy trees, trial-and-error regression, small-sample randomization [02 G1, G2].
4. Prediction accuracy with no decision value [02 R14].
5. Black boxes in decisions about people [02 T6].
6. Methods-first teaching; a literature that gives practitioners little guidance [02 T9].
7. Quality claims with no guarantee when the algorithm stops early [02 J2].
8. An inherited *intractable* belief, never re-measured [02 P2].
```

**Full-text evidence per sign.**
- Sign 2 (polynomial time without solve times) is dated (C19): his 1994–1997 LP papers argue from operation counts and worst-case bounds [S269 pp. 1, 21–22; S289 pp. 2, 6, 11–12]; computation in real problems named the criterion for comparing conservatism in 2004 [S001 p. 8]; solve time stated as the test from 2014: "Our view of computational tractability is not polynomial time solution times as these do not exist for the LQS problem unless P = NP." [S178 p. 5]; the 2016 redefinition [S010 p. 2]. *Fix round*: the earlier *his rule from about 2004* is replaced by this dating. Quote: "The practicality of our algorithm critically depends on whether Vaidya's algorithm is a practical algorithm, and to our knowledge Vaidya's algorithm has not been tested in practice." [S269 p. 22].
- Sign 3: regression as an art [S081 p. 3]; greedy trees [S011 pp. 4–6].
- Sign 4 applies to fourteen prediction-only papers of his group (C11; [Method 5](#method-5)).
- Sign 5: black boxes acceptable for diagnosis, not for guidance that changes standard care [S685 pp. 2–3].
- Sign 8: the belief dated and conceded [S010 p. 8; S081 p. 4; S011 pp. 3, 5–6; S105 pp. 1, 3, 6–7].
- Sign 9 (new): heuristics judged only against heuristics [S051 p. 1; S185 pp. 1–2]; "a practitioner using a heuristic method typically has no way of knowing when this has occurred" [S183 p. 3]; affine policies advocated without quality results [S042 p. 3].
- *Fix round*: SKILL.md keeps eight warning signs (framework §四: 5–8): sign 9 was merged into sign 7 (quality claims with no guarantee) and sign 10 into sign 4 (no decision value; point forecasts and static models of dynamic problems); sign 5 is scoped to treatment decisions, with the group's deployed tools as an exception (C21).
- Sign 10 (new): "Yet, in many practical applications, the TSP is a deterministic, static approximation to a problem which is, in reality, both probabilistic and time varying (dynamic)." [S016 p. 1]; "Point forecasts are meaningless (because they are always wrong) and should be replaced by range forecasts." [S027 p. 4]; a priori optimization's motive, the robustness of deterministic optima to changed instances [S038 p. 1].

**Moved at the tighten step** (T3.7, 2026-10-29). These SKILL.md lines are copied verbatim as they stood before the cut; SKILL.md now keeps a shorter form of each, and the card citations, pages, DOIs and quotes it dropped are kept here.

2. Models harder than their nominal version; polynomial time without solve times [02 T7] (stated from 2014 [S178 p. 5]; his 1994–1997 papers argue from operation counts: C19).

**Increment books-2026-10-29** (2026-10-29; book material, framing and dating only, outside every say–do count; full account: [Book material](#books)). Warning sign 6 now cites the two book pages behind it: "Simply teaching students to plug numbers into black-box models is not relevant to a student's education." (2004, with Freund) [B014 p. 1] and the 2016 contrast with "the vast majority of books and classes available today, in which methods play the leading role" (with O'Hair and Pulleyblank) [B017 p. 1]. ⚠ Audience: his PhD textbooks are organised by theory and methods [B004 pp. 2–5; B007 pp. 1–4]; the warning concerns MBA and analytics teaching. The line before this increment (verbatim):

```text
6. Methods-first teaching; a literature that gives practitioners little guidance [02 T9].
```

**Claim census 2026-10-29** (earlier wording, verbatim):

```text
2. Models harder than their nominal version; polynomial time without solve times [02 T7] (stated from 2014 [S178 p. 5]; C19).
6. Methods-first teaching; a literature that gives practitioners little guidance [02 T9; B014 p. 1; B017 p. 1].
```

Census items k = 42, 47, 48. Sign 2: the S178 card dates only the solve-time half, the 2014 statement that tractability is not polynomial time (p. 5); nothing on it dates *models harder than their nominal version*, so the dating now covers *the latter* only (C19 is outside this batch). Sign 6: the B014 and B017 cards support methods-first teaching (p. 1) but say nothing about a literature that leaves practitioners without guidance; the book pages now sit on the teaching clause, and the literature clause cites the card that says it, S095, whose abstract says the profusion of feature-selection research may have given practitioners little guidance (p. 1).

<a id="taste-quick-check"></a>
## Taste quick-check

**Before this synthesis** (verbatim):

```text
### Taste quick-check
- [ ] If this fully succeeds, would a graduate course teach it, or a company use it within 2–5 years?
- [ ] Does the robust, learned or relaxed problem keep its nominal class, with solve times measured at scale?
- [ ] Is there a greedy, trial-and-error or randomized step one joint optimization could replace?
- [ ] Will the result be judged by its decisions, against the decision-maker's current rule?
- [ ] Can the person who acts on the result see why it is recommended?
- [ ] Did a real problem and a data set come before the method?
- [ ] Will each result carry a certificate or a gap, and will the abstract say which do not?
- [ ] Has the *intractable* belief been re-measured with today's solvers on this class?
```

**Change.** One question added from Method 7: is there a bound valid for every policy, and is the incumbent graded against it? *Fix round*: folded into the certificate question, so the list keeps eight questions (framework §四: 5–8).

<a id="methods-note"></a>
## Core methods: counting note

**Before this synthesis** (verbatim; the section's introduction):

```text
## Core Research Methods

Six methods passed the four checks (recurrence, say–do, executable, exclusive). 🔴 items marked *correction* come from the critique record, not his practice.
```

**Counts** (08 §2). Distinct works read in full or in part whose cards link the method, after the counting rules of the [Card key](#card-key); abstract-level links in brackets.

| Method | Evidence | Variant | Contradiction | Any link | Say–do after the full texts |
|---|---|---|---|---|---|
| M1 Formulation first | 210 (+14) | 141 (+5) | 5 | 346 | ✅ stated (sole-author texts 1994–1995) and practised 1988–2026 |
| M2 Quantified "why now" | 10 | 86 (+1) | 2 | 94 | ✅ steps 1, 2, 4–6; ⚠ step 3 is the skill's rule |
| M3 Price of X | 46 (+3) | 168 (+1) | 0 | 205 | ✅ stated jointly (2004, 2011); one-knob practice from 1990; a knob-free precursor in 1988 |
| M4 Warm start, exact solve, certificate, duel | 54 (+2) | 226 (+4) | 24 | 287 | ✅ protocol; ⚠ certificate (T1) |
| M5 Judge by the decision | 84 (+16) | 160 (+10) | 15 | 233 | ✅ OR and deployment papers; ⚠ clinical prediction papers |
| M6 Programmes | 187 (+16) | 8 | 0 | 194 | ✅ lineage steps; step 1 not observable |
| M7 Bound before policy (new) | 79 works in clusters 1–2 of 08 §6 | — | — | — | ✅ stated (sole author 1994–1995) and practised 1988–2026; contradictions not searched (no card links it by name) |

Variant links dominate for M2–M5 because readers marked a link as a variant whenever one step was missing or done differently. *Fix round*: the counts merge four more version pairs that the cards themselves identify (S016 = S261, S032 = S597, S340 = S197; S328 = S914, probable: same three authors and a close title, the working paper predating submission); M1, M3, M4 and M7 drop by 2–4 works. SKILL.md's say–do lines give only the total and the contradictions; the breakdown stays here. The 1988 thesis states Method 1 only as a variant (class preservation reversed [S048 p. 29]), so M1's stated date is 1994–1995 [S580 pp. 5, 10; S185 p. 1].

<a id="method-1"></a>
## Method 1: Formulation first, kept in the solver class

**Before this synthesis** (verbatim):

```text
### Method 1: Formulation first, kept in the solver class {SD CP RO ML DA; LO and IO as engines}
**One line**: Write a central problem another tradition owns exactly as an LP, conic or MIO problem, with a device that keeps its nominal class; read structure off the dual; print where tractability ends.
**Evidence**:
- Stated: the sole-author 1995 survey ties better formulations to deeper understanding and better methods (p. 337, DOI 10.1007/BF01149167); the 2004 abstract: the robust LP stays an LP; the 2019 principle ties ML to optimization, not probability [02 T4, T7].
- Practice: achievable region (DOI 10.1287/moor.21.2.257); moment bounds as SDPs (DOI 10.1137/S1052623401399903); budgeted robustness; best subset and trees as MIO; prescriptive analytics [01 SW1–SW5].
- Say–do consistency: ✅ stated + practised, 1993–2026, five domains.
**Steps**:
1. Name the owning tradition, its tool and what it optimizes only implicitly (dynamic programming, tail inequalities, greedy selection, estimate-then-plug-in).
2. Choose variables over a describable set: performance vectors, moments, a budget Γ of deviating coefficients, support indicators, ML weights.
3. Pick the class-keeping device: a robust LP stays an LP; robust 0–1 problems with cost uncertainty need n + 1 nominal solves; a univariate moment bound is an SDP.
4. Dualize: indices as dual variables, worst-case distributions, solution-independent violation bounds.
5. Print the boundary (tight moment bounds NP-hard for k ≥ 4 on Rⁿ; certificates taking hours for p in the thousands); call ad hoc policies ad hoc.
**🔴 Stop rule**: leaving the class without a measured solve time at the target scale → change the device, not the solver. *Correction*: test a per-constraint robust device on a two-period example; the 2006 robust inventory LP (DOI 10.1287/opre.1050.0238) was later shown conservative (DOI 10.1016/j.disopt.2006.12.002) and judged incorrect for its stated set (DOI 10.7737/MSFE.2014.20.2.001) [05 §4.3].
**Applies to stage**: idea generation; formulation.
**Different from standard practice**: the model, not the algorithm, is redesigned so existing solvers apply.
**Limitations**: *tractable* drifts from complexity class (2004) to solve time (2019) [02 C2]; big-M formulations can be weak (DOI 10.1287/opre.2021.0034) despite his 2005 stress on strong ones (Tension T4); no stated method for SD and CP.
```

**Full-text evidence.**
- *Strongest practice*: all five steps in one sole-author text: the owning tradition and its ad hoc state, performance vectors as variables, LPs over extended polymatroids and polynomial-size relaxations, duals read as Gittins indices and as reduced-cost heuristics, the boundary printed as a complexity map [S185 pp. 1–3, 9–12, 21–25, 49–50]. The template for steps 1–4 in the conservation-law paper [S057 pp. 1, 3, 11–13, 20–21]; a central probability problem written exactly as a convex or semidefinite program with a dual certificate and the boundary printed [S018 pp. 5–6, 16–17]; the robust LP stays an LP and the robust MIP a MIP [S001 pp. 3–4, 10]; a robust 0-1 problem keeps the complexity of its nominal problem [S004 pp. 5–7, 22]; the robust inventory model stays an LP or MIP on any tree [S014 pp. 1, 4–5, 9–10]; a statistics estimator written as a convex integer program through Fenchel duality [S095 pp. 4–7]; a regularizer redesigned so a commercial solver's lazy callbacks apply [S175 pp. 1, 3, 9–10]; a statistics-owned design problem, settled by randomization since Fisher, written as an MILP [S124 pp. 2, 4–6, 8].
- *Stated*: "The theme in the paper is the thesis that better formulations lead to deeper understanding and better solution methods." [S185 p. 1] (sole author); the 1994 sole-author working paper places the essential difficulty in the dynamic and combinatorial character [S580 p. 10] and asks for an approach that does not change when the problem changes: "Ideally the approach should not fundamentally change when the problem changes." [S580 p. 5]; "Unlike all other approaches that create robust solutions for combinatorial optimization problems, the proposed approach retains the complexity of the nominal problem or its approximability guarantee" [S004 p. 22]; best-possible bounds framed as an optimization problem [S018 p. 1].
- *Class-keeping devices* (cluster 18 of 08 §6, 38 works): robust = nominal [S014 pp. 1, 4–5]; separation = nominal [S045 pp. 2–4]; dense tractable classes [S239 pp. 1–2, 8]. Quote: "the robust problem is of the same difficulty as the nominal problem, that is, a linear programming problem when there are no fixed costs, and a mixed-integer programming problem when fixed costs are present" [S014 p. 1].
- *Carry a classical device into the uncertain or dynamic setting* (cluster 7, 41 works; evidence for step 1 only, exclusivity fails): [S038 pp. 9–10; S091 p. 31; S029 pp. 12, 16, 37; S458 pp. 3, 6–7].
- *Assume only what can be estimated; worst case over the rest* (cluster 9, 13 works; CP evidence): [S018 pp. 2, 19–21; S031 pp. 7–8; S169 pp. 2–3, 8, 23; S452 pp. 1–2; S223 pp. 12–13].
- *Large deviations, fluid models and stability as optimization* (cluster 33, SD evidence): [S819 pp. 12, 16, 20, 24; S147 pp. 3–5, 8; S140 pp. 5, 12, 18–20].
- *Say–do*: ✅ on 210 works, 1988–2026, in all nine domain codes; 346 works link M1 in any relation (version pairs merged).

**Variants and contradictions.**
- ✗ *No stated method for SD and CP* (Limitations, Domain Map) → SD stated in sole-author texts, CP jointly ([Domain map](#domain-map); C1).
- ⚠ *Kept class in SD* (08 §3 row 7): in 1988–1997 the class kept is an analysable queueing or probability class: Coxian and rational-transform distributions dense in all distributions [S239 pp. 1–2, 8, 12; S168 pp. 3, 8, 12–15; S389 pp. 2, 11–14]; analysable queues reached by policy design [S016 pp. 1–2, 7–11; S261 pp. 4, 11, 15–26]; complete systems of laws [S129 pp. 1–4, 12; S280 pp. 1, 7, 9]. The 2010s robust-queueing line replaces distributions by limit-law sets and keeps closed forms [S119 pp. 7–13, 25, 41–47].
- ⚠ *The algorithm is built too* (08 §3 row 6; C5): see [How to Use](#how-to-use) for the ten cards; cutting planes over the binary support as the scaling engine (cluster 17, 33 works) [S061 pp. 3, 6–10; S175 pp. 9–10; S136 pp. 9–13; S093 pp. 10–14].
- ✗ *Scope* (08 §3 row 8): some 2025–2026 AI papers have no formulation at all: a small network trained on a contrastive loss [S426 pp. 4, 6]; a training-free classifier [S474 pp. 2, 4, 8]; one optimization stated in a sentence [S618 pp. 13–14]; optimization only as study design [S439 pp. 5–6]. Earlier contradictions: no exact formulation in a 2005 revenue-management paper [S066 pp. 2, 7, 10] and a class left on purpose without solve times [S278 pp. 2, 4].
- *Tractable drifts*: complexity class and asymptotic constants in 1988–1997 [S289 pp. 2, 6, 11–12; S269 pp. 1, 21–22]; computation in real problems named the criterion in 2004 [S001 p. 8]; solve time stated as the test from 2014 [S178 p. 5] and in 2016 [S010 p. 2]. *Fix round*: SKILL.md now uses this one dating in Method 1's Limitations, warning sign 2 and C19.

**Moved at the tighten step** (T3.7, 2026-10-29). These SKILL.md lines are copied verbatim as they stood before the cut; SKILL.md now keeps a shorter form of each, and the card citations, pages, DOIs and quotes it dropped are kept here.

- Stated: "The theme in the paper is the thesis that better formulations lead to deeper understanding and better solution methods." (sole author) [S185 p. 1]; the 2019 principle [02 T4, T7].
- ⚠ SD 1988–1997: the kept class is an analysable distribution or queue class [S239 pp. 1–2, 8, 12; S168 pp. 3, 8, 12–15].
- ⚠ Class left → his group builds the algorithm (outer approximation, custom branch-and-bound) [S040 pp. 2, 6, 10; S184 pp. 8–18] (C5).
- ✗ Outside it: the 2025–26 foundation-model papers [S426 pp. 4, 6; S474 pp. 2, 4, 8].

**🔴 Stop rule**: leaving the class without a measured solve time at the target scale → change the device, not the solver. *Correction*: test a per-constraint robust device on a two-period example; the 2006 robust inventory LP (DOI 10.1287/opre.1050.0238) was later shown conservative (DOI 10.1016/j.disopt.2006.12.002) and judged incorrect for its stated set (DOI 10.7737/MSFE.2014.20.2.001) [05 §4.3].

**Limitations**: *tractable* drifts from complexity class and operation counts (1994–1997) to solve time, stated as the test from 2014 [02 C2; S269 pp. 1, 21–22; S178 p. 5]; big-M formulations can be weak in tree MIOs (DOI 10.1287/opre.2021.0034) despite his stated stress on strong ones (Tension T4).

**Increment books-2026-10-29** (2026-10-29; book material, framing and dating only, outside every say–do count; full account: [Book material](#books)). One Evidence line added (nothing removed): "Textbooks (stated jointly; no say–do count)". Its sources:
- 1997, with Tsitsiklis: the book's main objective is the reader's ability "to formulate fairly complex optimization problems", then an appreciation of "the main classes of problems that are practically solvable", then the solution methods and the qualitative properties of solutions [B001 p. 1]; LP in general form, and "we separate the structural understanding of linear programming from the particulars of the simplex method", with a derivation of duality that does not rely on it [B001 p. 1]; dual optimal solutions as subgradients of the optimal cost function (chapter 5) [B001 p. 1]. This matches step 4 (read structure off the dual).
- 2005, with Weismantel: strong formulations, ways to improve them, integral polyhedra, duality and relaxations as the stated emphasis [B006 p. 1]; three formulation chapters and a duality chapter precede any algorithm [B007 pp. 1–2].
- 2004, with Freund: in chapters 7–9 the optimization model is built by defining decision variables and constructing constraints and objective, and "Only then do we translate the problem into a spreadsheet for solution by appropriate software." [B014 p. 1].
- 2019, with Dunn: "ML is inherently linked to optimization not probability theory." [B009 p. 1] (step 1: cast a neighbouring tradition's problem as optimization).
- 2022, with den Hertog: the LP case first, then nonlinear RO split by how the uncertainty enters [B011 p. 1]; that the split follows where exact counterparts end is [inferred] (card S283 [S283 p. 3]).
- ⚠ Teaching level: formulation first with no kept class (the MBA texts and the 2009 course) [B014 p. 1; B015 pp. 4–5; B021 p. 2].

**Claim audit 2026-10-29, round 1** (earlier wording, verbatim):

```text
- ✗ Outside it: the 2025–26 foundation-model papers [S426 pp. 4, 6].
```

SKILL.md packet, item k = 8 (`10-claim-audit.md`): one 2025 card cannot show every 2025–26 foundation-model paper. The line now says *some* and restores the 2026 card cut at the tighten step [S426 pp. 4, 6; S474 pp. 2, 4, 8].

**Claim census 2026-10-29** (earlier wording, verbatim):

```text
- ⚠ SD 1988–1997: the kept class is an analysable distribution or queue class [S239 pp. 1–2, 8, 12].
- ⚠ Class left → his group builds the algorithm (outer approximation, custom branch-and-bound) [S040 pp. 2, 6, 10] (C5).
1. Name the owning tradition, its tool and what it optimizes only implicitly (dynamic programming, tail inequalities, greedy selection, estimate-then-plug-in) [S057 p. 1].
```

Census items k = 61, 62, 65. k = 61: the S239 card is one 1988 paper and cannot carry a span to 1997; the span now ends in 1993 and cites the 1993 routing paper, whose card keeps an analysable queue, the G/G/m and ΣGI/G/m policies (D2, D4; Method 1 variant) [S032 pp. 7–9]. The 1995–1997 SD papers keep a complete system of laws, not a distribution or queue class (cards S129, S280), so they no longer stretch the span (08 §3 row 7). k = 62: the S040 card shows a custom branch-and-bound built because the general MIQP solver was weak, for a problem still written as an MIQP, and no outer approximation; the line now cites the cards where the class is left and the group builds the algorithm: outer approximation after a solver bake-off fails on the MINLO class [S105 pp. 7–9], and a custom branch-and-bound once the nonconvex formulation leaves the solver classes [S184 pp. 8–18]. S040 stays the 2009 date in C5. k = 65: the S057 card supports only the dynamic-programming example (p. 1); each example now carries its own card: Markov, Chebyshev and Chernoff bounds asked to be best possible [S018 p. 1], greedy trees that optimize impurity rather than misclassification [S011 p. 4], and plugged-in point predictions [S008 pp. 2, 6].

<a id="method-2"></a>
## Method 2: Quantified "why now"

**Before this synthesis** (verbatim):

```text
### Method 2: Quantified "why now" {IO ML; returns in SD HS RO}
**One line**: Reopen a problem written off as intractable once the tool has changed; concede the old belief was right when formed; justify the reopening with a solver × hardware figure rebuilt for this paper.
**Evidence**:
- Stated: seven occasions 2015–2019, including the 2019 principle that NP-hardness is an opportunity; a 2015 abstract grants that the belief held two decades earlier (paraphrase) [02 P2, R9].
- Practice: CRIO submitted 2002 (DOI 10.1287/opre.1060.0360); the figure rebuilt four times: about 200 billion (Morse lecture 2014; arXiv 1507.03133 v1), 450 billion (AoS 2016, p. 819), 800 billion (OCT 2017), 2 trillion (Dunn's thesis 2018) [03 B4.4; 05 §1.6].
- Say–do consistency: ✅ stated + practised.
**Steps**:
1. Find the written-off problem and date the belief (CRIO traces it to the 1970s).
2. Concede it was right when formed; argue change, not error.
3. Rebuild the figure from version-on-version solver tests and hardware data; never reuse the last paper's number.
4. Lead the abstract with belief and figure; present the exact formulation as motivated by the speed-up.
5. Demonstrate at a scale the old community calls practical.
6. Return whenever a tool changes: bandits 1996 → 2026 (DOI 10.1007/s10994-026-07022-0); RO under an LLM lens (arXiv 2501.00568).
**🔴 Checkpoint** (*correction*): the figures multiply mixed-integer *linear* solver factors by Top500 peak speed, and the MIQO factor is asserted without citation [05 §1.6]. Time your class on your machine across solver versions, or say the figure is borrowed. No critic was found: absence, not endorsement.
**Applies to stage**: problem choice; framing.
**Different from standard practice**: the "why now" is a number rebuilt per paper; the old belief is conceded, not attacked.
**Limitations**: era-bound (the 1991–2018 speed-ups; remaining headroom unknown); not the user's machine or class.
```

**Full-text evidence.**
- *Strongest practice (10 works)*: the belief dated to the 1970s–80s and conceded as justified then [S010 p. 8; S081 p. 4; S011 pp. 3, 5–6; S105 pp. 1, 3, 6–7]; the figure rebuilt per flagship paper: 200 billion in the arXiv v1 of best subset, from version-on-version solver factors times Top500 peak speed, with the MIQO factor asserted [S010 pp. 7–8]; about 450 billion in the 2016 OR Forum paper [S081 p. 4]; 800 billion for trees [S011 pp. 5–6]. A belief dated and refuted with solve times at n and p in the 100,000s [S061 pp. 2, 4, 13]; tractability redefined as practical solve times already in 2014 [S178 pp. 3–5]; a speed-up measured against an owner's own simulator on one desktop [S476 pp. 1, 6]; the return to restless bandits once the tool changed [S681 pp. 1, 3, 8; S051 pp. 5–9].
- *Stated*: "we use the term tractability not to mean the usual polynomial solvability for problems, but rather the ability to solve problems of realistic size in times that are appropriate for the applications we consider." [S010 p. 2]; "Moreover, we think that the ultimate criterion for comparing the degree of conservatism of these methods will be computation in real problems." [S001 p. 8]; "The empirical computational results in this paper do away with the long held belief that exact sparse regression for practical problem sizes is a lost cause." [S061 p. 4]; "These speedups encourage us to rethink whether NP-hardness should in fact be synonymous with intractability." [S184 p. 5]; "NP-hardness is a worst-case analysis statement. In practice, NP-hard optimization problems are often tractable." [S250 p. 8].
- *Owner's simulator*: "KPSAM 2019 required 6 h and 42 min. MITSAM took 14.8 s, >1600 times faster." [S476 p. 6].
- *Say–do*: ✅ for steps 1 (find and date the belief), 2 (concede), 4–6 (lead with it; demonstrate at scale; return when tools change); ⚠ step 3.

**Variants and contradictions.**
- ⚠ *Step 3 is the skill's rule* (08 §3 row 9; C6): rebuilt only in the 2014–2017 statistics flagships [S010 pp. 7–8; S081 p. 4; S011 pp. 5–6]; repeated or borrowed in later papers [S105 pp. 6–7; S257 pp. 3, 13–16; S432 pp. 2, 16; S184 pp. 5, 25, 33–34; S355 pp. 5–6; S396 p. 2; S408 p. 9; S236 p. 3; S092 pp. 2, 6; S149 pp. 2, 8–9; S480 pp. 7, 9; S523 p. 4].
- ⚠ *Qualitative why-now*: in about 46 of the 94 linked works the why-now is a named tool or data change: SDP solvers [S056 p. 3], interior-point methods [S003 p. 2], first-order methods [S315 p. 2], data availability [S074 pp. 1, 3; S193 pp. 2, 32; H004 p. 1], open LLMs [S390 pp. 1–2], a foundation model [S474 pp. 1–2].
- ✗ *Two contradictions*: a 1994 *fastest* claim from operation counts [S269 pp. 1, 21–22] and the 2016 figure reused in 2024 [S480 pp. 7, 9].
- ✗ *The reverse argument was his own* (08 §3 row 10): before 2002 hardness was accepted as the limit of exact work and answered with relaxations and bounds [S185 pp. 49–50; S580 pp. 6–7; S052 pp. 2, 4]; in 1996 scarce computation argued for a priori routes [S025 pp. 10, 12, 17]: "A priori optimization in VRPs is an attractive policy in the absence of intensive computational power." [S025 p. 17]; in 2002 his own matched-quality test found CPLEX 6.0 much slower than his heuristic [S070 pp. 13–15]. The belief is dated from 2007 (submitted 2002) and change argued in 2011 [S073 pp. 1–2; S561 pp. 3, 10–12]; *fix round*: neither concedes that the belief was justified when formed; that concession appears first in the arXiv v1 of best subset (2015) [S010 p. 8], then [S105 p. 7].

**Moved at the tighten step** (T3.7, 2026-10-29). These SKILL.md lines are copied verbatim as they stood before the cut; SKILL.md now keeps a shorter form of each, and the card citations, pages, DOIs and quotes it dropped are kept here.

- ✗ His 1995 survey and a 1996 joint paper argued the reverse: hardness answered with relaxations [S185 pp. 49–50]; scarce computation favouring a priori routes [S025 pp. 10, 12, 17].

**Limitations**: era-bound (the 1991–2018 speed-ups); not the user's machine or class; the belief is dated from 2007 (submitted 2002) [S073 pp. 1–2] but conceded as justified only from 2015 (arXiv v1 of best subset) [S010 p. 8].

**Increment books-2026-10-29** (2026-10-29; book material, framing and dating only, outside every say–do count; full account: [Book material](#books)). The Stated line now adds the 2019 book's principles 2 and 3, "Practical tractability not polynomial solvability leads to real world impact." and "NP-hardness is an opportunity not anobstacle." (run together as printed) [B009 p. 1]. The older publisher summary on his books page promises solutions to central ML problems "at large scale" found "in seconds/minutes" [B008 p. 1; B010 p. 1]. No book page gives a speed-up figure, so C6 stands. The line before this increment (verbatim):

```text
- Stated: "The belief that MIO approaches to problems in statistics are not practically relevant was formed in the 1970s and 1980s and it was at the time justified." [S010 p. 8; S105 p. 7].
```

**Claim census 2026-10-29** (earlier wording, verbatim):

```text
- ⚠ In about half the linked works the why-now is a named tool or data change, without a figure [S056 p. 3]; later papers repeat or borrow the figure [S480 pp. 7, 9].
- ✗ His 1995 survey argued the reverse: hardness answered with relaxations [S185 pp. 49–50].
6. Return whenever a tool changes: bandits 1996 → 2026 [S681 pp. 1, 3, 8]; RO under an LLM lens (arXiv 2501.00568).
```

Census items k = 79, 81, 84. k = 79: *about half* is the count of 08 §3 row 9 (about 46 of the 94 linked works), which no single card can show; it now cites 08 §3, and S056 stays as the instance, a named tool change stated with no figure (p. 3). k = 81: the S185 card files this as a Method 2 variant, not a contradiction: hardness accepted as the limit of exact characterization and answered with relaxations and bounds, not with a tool-change argument (pp. 49–50); the cards for the same row file it as a variant too (S580 pp. 6–7; S052 pp. 2, 4; S025 pp. 10, 12, 17). The line is now ⚠ and says what the card says; the say–do count (2 contradicting: S269, S480) already excluded it. k = 84: the S681 card says the 2026 paper links back only to S051 (2000) on restless bandits, citing no 1996 bandit work (D6, pp. 31–35), and neither confirms nor refutes a 1996 start (Method 2 link, pp. 3, 8); the step now says restless bandits 2000 → 2026.

<a id="method-3"></a>
## Method 3: The price of X

**Before this synthesis** (verbatim):

```text
### Method 3: The price of X {RO AP ML IO}
**One line**: Name the property the decision-maker wants (robustness, fairness, interpretability), index models by one interpretable knob, prove a solution-independent bound, keep the class, publish the price curve with its bad case.
**Evidence**:
- Stated: the 2004 abstract tunes conservatism through probabilistic violation bounds (paraphrase); a 2026 lecture example, reported by MIT News: a Panama Canal plan of 45 vessels a day that stayed feasible [02 G4].
- Practice: robust knapsack: a 0.57% violation bound for a 1.54% objective loss, with PILOT4 printed as a case where the price stays high (OR 2004 pp. 44, 48) [03 B4.1]; price of fairness (DOI 10.1287/opre.1100.0865); flexibility and interpretability (arXiv 1907.03419) unpublished [06 §7].
- Say–do consistency: ✅ stated + practised.
**Steps**:
1. Name the property and who wants it.
2. Give it one operational knob (Γ, the coefficients per constraint allowed to deviate; depth; a fairness criterion).
3. Prove a knob–property bound independent of the solution, with its assumptions.
4. Keep the class (Method 1, step 3).
5. Compute the curve on the rival school's test problems and one realistic case; report the good point and the bad case.
6. Hand the knob and the curve to the decision-maker.
**🔴 Stop rule**: no knee in the curve → say so and diagnose the structure (PILOT4: few uncertain coefficients per row). *Correction*: knobs get fixed arbitrarily, and budgeted robust optima need not be Pareto-efficient (DOI 10.1287/mnsc.2013.1753); set the knob from data, as his group later did (DOI 10.1007/s10107-017-1125-8) [05 §4.1].
**Applies to stage**: formulation; judging; reporting to decision-makers.
**Different from standard practice**: the property becomes a priced curve the decision-maker owns, not a hidden parameter.
**Limitations**: bounds rest on distributional assumptions; two of four "price of" manuscripts stayed unpublished.
```

**Full-text evidence.**
- *Strongest practice (46 works, version pairs merged)*: the source paper with one knob per constraint, solution-independent bounds, the class kept and curves including the bad case [S001 pp. 1, 3–5, 9–16]; robust discrete problems with price curves on knapsack, sorting and shortest path [S004 pp. 4, 6, 16–22]; Γ curves with a knee and both failure modes [S027 pp. 6, 8–13, 30–35]; the price of fairness with a bound uniform over utility sets [S012 pp. 1, 7, 11–14] and a one-knob family with two-sided bounds handed to the manager [S026 pp. 1–2, 6–7, 10–12, 15–16]; community satisfaction priced in buses and dollars on a curve handed to a school district [S137 p. 5; S262 pp. 10–11]; the price of stability with Pareto properties [S401 pp. 3–4, 6, 10–11]; a radius tied by a solution-independent bound to a probability the decision-maker feels [S139 pp. 6, 15–16, 19]; set-only factors shown tight [S392 pp. 8, 10, 13–23].
- *Stated*: "It is our belief that the “price” of fairness is effectively inescapable if the allocations prescribed by a given scheme are to be ethically acceptable and implementable." [S012 p. 14]; "Each additional point of community satisfaction in Boston costs dozens of additional buses and tens of millions of taxpayer dollars." [S262 p. 10]; "This crucial design task is nonetheless frequently executed in an ad hoc fashion." [S026 p. 2].
- *Earliest forms, 1988–1996*: the thesis names the price of robust, global a priori solutions as a radical change in complexity: "one pays for these nice properties (robustness, globality) by changing the complexity of the problem radically." [S048 p. 29]; one knob indexes the travel–waiting trade-off, with a worked price of 10% less travel for 21% more system time [S597 pp. 36–38; S032 pp. 15–16]: "If we decide to reduce the average travel cost per demand 10% to y = 0.81, the system time increases by 21% to 702." [S032 p. 16]; one knob (the arrival cap) gives a priced curve with a knee handed to policy makers [S135 pp. 15–16].
- *Say–do*: ✅; the origin moves from 2004 to 1988 (C7). *Fix round*: the 1988 sentence prices robustness and globality in lost tractability, with no knob and no bound, the opposite of step 4 (keep the class); the S048 card links it to Method 3 only as a variant, and no text links it to the 2004 paper [S048 p. 29]. So SKILL.md now states the method from the joint 2004 and 2011 texts ([02 G4]; [S012 p. 14]), dates one-knob practice from 1990 [S597 pp. 36–38; S032 p. 16], and files the 1988 thesis as the knob-free precursor under the price-of-simplicity variant.

**Variants and contradictions.**
- ⚠ *Price of simplicity* (08 §3 row 11; cluster 4, 37 works): the price of a simple, stable solution against re-solving, measured asymptotically and in the worst case [S048 pp. 29, 40–44, 84–85; S148 pp. 5, 14–17; S017 pp. 1, 9–11; S102 pp. 2, 14–18]; a priori, simplified or regularized models priced against the ideal [S089 pp. 2, 14, 17, 28, 33; S025 pp. 11–12; S048 pp. 12–13; S136 pp. 3–4, 16–17; S250 pp. 12, 26, 33–36]; the price of a fairness policy in routing [S091 pp. 11, 23–25; S025 pp. 11–12, 14–16].
- ✗ *Knobs from data* (08 §3 row 12; C7): from 2006, Γ from mean and variance (moments, not samples) by minimizing a worst-case bound [S014 pp. 1, 10–12]; from samples and a risk measure in 2009 [S024 pp. 3, 5]; a lookup table of the knob per class and ε [S022 pp. 3, 15, 19]; a radius calibrated to 99% of measured errors [S090 pp. 12, 14]; the decision-maker's CVaR level as the knob [S024 pp. 3, 5, 9, 11]: "This is important because the uncertainty set becomes a consequence of the particular risk measure the decision maker selects." [S024 p. 3]; CLT scaling [S006 p. 6]; knobs implied by market prices [S171 pp. 8, 10]; hold-out validation [S013 pp. 29–31; S440 pp. 9–11]. Hand-set knobs persist [S124 pp. 4–5; S163 pp. 24, 28; S458 pp. 4, 7, 10; H001 pp. 14–16]. Sets built from a justified primitive (cluster 8, 27 works): limit laws, tests, predictors, data splits [S065 pp. 5–10; S119 pp. 7–10; S013 pp. 3–4, 10; S440 pp. 3–9; S543 pp. 4–12].
- ⚠ *Step 3, the solution-independent bound* (08 §3 row 13): present mainly in robustness and fairness [S001 pp. 3–5; S004 pp. 4, 6; S027 pp. 6, 8–13; S012 pp. 7, 11–14; S026 pp. 6–7; S139 pp. 6, 15–16; H004 pp. 6–9; S672 pp. 23–24, 27–29]. The price of interpretability is usually one or two points, without a curve or bound [S190 pp. 4, 7–8; S356 p. 2; H003 pp. 1, 24–26; S457 pp. 4, 13, 21; S267 pp. 21, 25]; quote: "This is the price of insisting on interpretability" [S081 p. 11].
- ⚠ *Step 5, the misspecification duel* (08 §3 row 14; cluster 11, 25 works 2003–2026): the robust policy and the model-based optimum (DP, SAA) both scored under distributions other than the assumed one, or beyond the set [S014 p. 12; S027 pp. 9–10, 21; S055 pp. 8–9; S059 pp. 9, 11, 14; S053 pp. 14–22; S278 pp. 5–6; S116 p. 12; S003 pp. 6–7; S006 pp. 5, 7; S172 pp. 21–23]; stated as a lesson in 2025 [S623 p. 4]. Heuristic-eligible, folded into step 5 because of the ten-heuristic cap.

**Moved at the tighten step** (T3.7, 2026-10-29). These SKILL.md lines are copied verbatim as they stood before the cut; SKILL.md now keeps a shorter form of each, and the card citations, pages, DOIs and quotes it dropped are kept here.

- Stated: "It is our belief that the “price” of fairness is effectively inescapable if the allocations prescribed by a given scheme are to be ethically acceptable and implementable." [S012 p. 14]; the 2004 abstract [02 G4].
- ⚠ Precursor, 1988–1993: the price of simplicity, no knob or bound; the thesis prices robustness in lost tractability [S048 p. 29], later as an asymptotic constant or worst-case ratio against re-solving [S048 pp. 40–44; S017 pp. 1, 9–11].
- ⚠ The solution-independent bound appears mainly for robustness and fairness; the price of interpretability is usually a point or two, without a bound [S190 pp. 4, 7–8].

**Claim audit 2026-10-29, round 1** (earlier wording, verbatim):

```text
- ⚠ Precursor, 1988–1993: the price of simplicity, no knob or bound; the thesis prices robustness in lost tractability [S048 p. 29].
```

SKILL.md packet, item k = 9: the S048 card names the coverage probability as the thesis's knob, a model parameter rather than a protection level a decision-maker chooses, with cost-ratio bounds tight by example and no violation-probability bound [S048 pp. 40–44]. The line now says *no decision-maker's knob or violation bound* and cites the a priori solution priced against re-solving for *the price of simplicity* [S048 pp. 12–13]; C7's *knob-free precursor 1988* is narrowed the same way (earlier wording under [Corrections](#corrections)).

**Claim census 2026-10-29** (earlier wording, verbatim):

```text
- Practice: one knob per constraint, solution-independent bounds, the class kept, the PILOT4 bad case printed [S001 pp. 3–5, 9–16]; price-of-fairness bounds uniform over utility sets [S012 pp. 7, 11–14]; community satisfaction priced in buses and dollars [S262 pp. 10–11].
- ⚠ Precursor, 1988–1993: the price of simplicity, with no decision-maker's knob or violation bound; the thesis prices robustness in lost tractability [S048 pp. 12–13, 29, 40–44].
- ✗ Knobs set from data *later* → from moments in 2006 [S014 pp. 10–12], from samples in 2009 [S024 pp. 3, 5]; hand-set knobs persist (C7).
- ⚠ The price of interpretability is usually a point or two, without a bound [S190 pp. 4, 7–8].
3. Prove a knob–property bound independent of the solution, with its assumptions, and show it tight [S012 pp. 7, 11–14].
5. Compute the curve on the rival school's test problems and one realistic case; score robust and model-based decisions under misspecified truths and beyond the set [S014 p. 12]; report the good point and the bad case.
```

Census items k = 87, 91, 93, 94, 96, 97. k = 87: the S012 bounds are uniform over compact convex utility sets (Assumption 1; Theorems 1–2, pp. 7, 11), and a nonconvex set drives the price arbitrarily close to 1 (p. 14), so the hypothesis is now stated. k = 91: the S048 card covers the 1988 thesis (and its 1990 papers) only; the 1993 end now cites the PTSP paper whose card prices a priori routing against re-optimization, with p a model parameter, not a knob [S102 pp. 2, 14–18] (08 §3 row 11). k = 93: the S024 card builds the uncertainty set from the samples and the decision-maker's coherent risk measure (pp. 3, 5), but the knob itself, the risk level α = j/N, stays the decision-maker's choice (pp. 5–6); *knobs set from samples* is narrowed to *sets from samples and the decision-maker's risk measure* (C7 is outside this batch). k = 94: *a point or two* meant one or two data points, but read as a size it is wrong for S190, whose gap to boosting is 4–5 AUC points (p. 8); the line now says *one or two numbers*, with *usually* resting on the five cards of 08 §3 row 13 and S190 as the instance with no curve over a knob and no bound. k = 96: the S012 card flags that the paper has no continuous knob (the bound's only parameter is the number of players; S026 adds the knob); step 3 now cites the card where a knob–property bound is proved with its assumptions and shown tight: Theorem 3, Γ against the violation probability, for independent symmetric perturbations, tight for symmetric ±1 perturbations, proved in the appendix [S001 pp. 5, 16–18]. S012 pp. 7, 11–14 stays on the Practice line. k = 97: the S014 card scores the robust and the DP policy under misspecified distributions with matched moments (p. 12), but nothing beyond the set; that clause now cites the ISO New England study, where both commitments are scored on normal loads that may fall outside the budgeted set [S006 p. 5].

<a id="method-4"></a>
## Method 4: Warm start, exact solve, honest certificate, duel the incumbent

**Before this synthesis** (verbatim):

```text
### Method 4: Warm start, exact solve, honest certificate, duel the incumbent {IO ML; HS as components}
**One line**: Solve the greedy step as one MIO warm-started by the incumbent heuristic, with a stated limit and a reported certificate or gap; beat the incumbent out of sample; if the bound stalls, switch to labelled local search.
**Evidence**:
- Stated: found in seconds, certified in minutes, better out of sample (2016, 2019); heuristic warm starts, then MIO certification [02 E1, E2, J2].
- Practice: best subset 2016 (500 s limit); OCT 2017 (30 min to 2 h, Gurobi 6.5, 53 UCI data sets, CART as warm start and opponent); BPV 2020 (60 s cap, DOI 10.1214/19-STS701) [03 B4.3]; Dunn 2018 local search, 100 restarts [03 B4.5].
- Say–do consistency: ✅ for the protocol; ⚠️ the certificate promise is stated but dropped at scale (OCT p. 1062: most results uncertified; the company's Optimal Trees trains by local search).
**Steps**:
1. Replace the greedy or trial-and-error step by one joint model (all tree splits at once; all regression goals in one MIQO).
2. Warm-start fast: a discrete first-order method with about 50 random starts; CART.
3. Solve with a stated time limit, solver version and machine.
4. Report certificate or gap; never call uncertified results optimal.
5. Duel out of sample against the incumbent's standard implementation at matched complexity (glmnet; rpart at the same depth), on synthetic data with known truth and on real data.
6. Say where the method wins (OCT: about 1.2–1.3% where CART is already accurate and data suffice).
**🔴 Stop rule** [practice, Dunn 2018]: bound stuck at zero or root node not passed → count binaries (n·2^D: 87,808 at depth 6 for n = 1,372), switch to local search with restarts, and (*correction*) drop *optimal* from the claim. *Critic-informed checks, not his practice*: low SNR (DOI 10.1214/19-STS733); equal budgets and threads; path-to-path timing (DOI 10.1214/20-STS806); installable code (DOI 10.1214/20-STS809); LP-relaxation strength (DOI 10.1287/opre.2021.0034).
**Applies to stage**: experiments; judging results.
**Different from standard practice**: the incumbent heuristic is both warm start and opponent; statistics' convex and greedy schools never solve the exact problem.
**Limitations**: needs a commercial MIO solver; weak for continuous NLP; warm starts alone are routine in IO.
```

**Full-text evidence.**
- *Strongest practice (54 works)*: best subset with a 50-start heuristic warm start, a stated 500 s limit, gap curves and an out-of-sample duel with the standard implementations, losing regimes printed [S010 pp. 27–40]; trees with CART as warm start and opponent at matched depth on 53 data sets [S011 pp. 14–15, 26–36]; product lines with the incumbent heuristic as warm start, stated limits, printed gaps and nothing unproved called optimal [S093 pp. 16–19]; sparse portfolios with certificates or printed gaps and a duel with the solvers' standard formulations [S725 pp. 13–23]; sparse PCA with a shared warm start for every method, a gap for every unsolved run and the comparator's code repaired before the duel [S183 pp. 19–28]; one stack, one machine, one 900 s limit for every method [S317 pp. 13–24, 39–43, 49]; the 1993 review's yardsticks for simulated annealing: guarantees, and equal computing time against the best specialized heuristic, applied to the Johnson et al. experiments it reports (no experiments of its own) [S005 pp. 3–5].
- *Stated*: "However, by design, the MIO approach maintains a suboptimality gap throughout computation and can therefore be terminated, before optimality is certified, with a certificate of suboptimality." [S225 p. 31] (SKILL.md's Stated line from the fix round); "Indeed, as often in discrete optimization, the algorithm can quickly find the optimal solution, but spends a lot of the time proving its optimality." [S095 p. 5], written to justify a 60 s and 180 s limit "guided by confidence in the quality of the initial solution", with no gap reported: the card files it as a Method 4 variant and a Tension T1 instance, so it moved to T1 in the fix round [S095 pp. 5, 39]; "Both computational experiments demonstrate that, unlike the LP relaxation, the semidefinite relaxation provides practically useful suboptimality guarantees that can be used to assess the closeness to optimality of heuristic policies." [S007 p. 18]; "None of these methods provide a certificate of optimality, but are very useful as warm starts for exact methods." [S184 p. 5].
- *Say–do*: ✅ for the protocol in his MIO methods papers; ⚠ the certificate (T1, older and wider); the critic-informed checks are largely his practice by 2020.

**Variants and contradictions.**
- ✗ *"Critic-informed checks, not his practice"* (08 §3 row 15; C8): equal computing time is the criterion of the 1993 SA review, applied to others' experiments [S005 pp. 3–4]; *fix round*: his own matched comparisons start in 2002, with the machine, limits and a machine-speed normalization stated and CPLEX held to the heuristic's quality [S070 pp. 9–15]; the same single-threaded 60 s per decision for both methods, with the rival's overruns printed [S340 pp. 16, 23]; equal memory over time checkpoints [S328 pp. 2, 9, 11–15; S914 pp. 22–24]; matched budgets with significance tests [S197 pp. 8–14]; threads and confidence intervals stated [S088 pp. 10–14]; one thread, equal tolerance and time limit against BARON, SCIP and CPLEX [S708 pp. 35–41]; one stack, one machine, one limit, low SNR, timing with tuning and released code [S317 pp. 13–24, 39–43, 49]; SNR grids already in 2016 [S010 pp. 26, 30, 38] and the critics' grid adopted in the reply [S095 pp. 3, 10, 21, 23]; code released [S093 p. 16; S208 pp. 11–14; S139 p. 8]; formulation strength ([Inner tensions](#inner-tensions), T4). An exception with the tilt stated: big-M solvers given 28 threads against one [S725 pp. 17, 19]. The matched duel recurs in 45 works (cluster 12); promoting it would duplicate step 5. The critics' cases (note 05) concern particular papers of the best-subset line.
- ✗ *Certificate dropped: older and wider* (08 §3 row 16; C9): 2004, a MIP stopped after five feasible solutions because exact runs can be excessive [S031 p. 26]: "The reason for this is that running times for exact optimality can be excessive." [S031 p. 26]; 2007, early termination at a 5–10% gap justified while the conclusion claims a global optimum [S073 pp. 15–18]; 2010, an asymptotic theorem offered for empirically stopped runs [S141 pp. 5–6, 9, 11]; 2017, most tree results without certificates [S011 pp. 14, 26]; applied papers 2019–2026 call trees optimal with no solver, gap or limit [S094 pp. 5, 9; S235 pp. 2–3; S272 pp. 2, 5; S287 pp. 1, 12; S376 p. 2; S527 pp. 1, 7, 13; S615 pp. 11–12, 42; S626 pp. 1, 5–6; S682 pp. 4–5; S688 pp. 7–8, 22]. Counter-practice with honest labels: [S093 pp. 17, 19; S554 pp. 1, 13, 23; S488 pp. 23–27; S909 pp. 14–15; S668 pp. 20, 24–25; S681 pp. 2–5]. Time to the best solution reported apart from time to proof [S445 p. 24; S488 pp. 25–27; S907 pp. 23–26, 35–38; S184 pp. 25–36]: "In a real-world application of these methods, the time taken to find the solution is the more important measure than the time taken to prove the solution optimal; therefore, time to finding solution is used." [S104 p. 30].
- ⚠ *Scope* (08 §3 row 17): in clinical collaborations the final learner is usually a tuned off-the-shelf ensemble, not an exact model [S054 pp. 2, 4; S127 pp. 3–4, 8; S023 pp. 3, 8; S677 pp. 2, 6, 8, 24; S678 pp. 4, 9, 14, 43; S618 pp. 3, 8–10, 13; S683 pp. 5–6]; a greedy step kept with the MIO deferred [S391 pp. 5, 8]. A simple incumbent (mean imputation) is proved asymptotically optimal for prediction and wins [S310 pp. 4–8, 12]: "In short, as far as prediction is concerned, crude is good." [S310 p. 5].
- ⚠ *When the bound stalls*: relaxation plus rounding that still prints a bound gap [S183 pp. 22–26]; a box-restricted MIO certifying inside a neighbourhood of the incumbent [S010 pp. 34–36]. *Fix round*: the stop rule now tries a stronger formulation first, where one exists: the data-dependent big-M constant weakens the group's own 2016 formulation (paraphrase), so the continuous part is eliminated in closed form and the binary support solved by outer approximation [S061 pp. 2–3, 6–10]; ridge or perspective forms replace big-M [S175 pp. 9–10, 15–16; S136 pp. 3, 6–7, 26–27].
- *Computation as an instrument* (cluster 31, 21 works; step 6 evidence): regime maps and phase transitions [S061 pp. 4, 14–19]; more data makes the exact problem easier [S355 pp. 4–5, 13–15; S170 pp. 5, 17, 20]; where optimization pays [S046 p. 19]; a fitted when-to-use rule [S104 pp. 4, 25–27; S011 pp. 30–35].

**Moved at the tighten step** (T3.7, 2026-10-29). These SKILL.md lines are copied verbatim as they stood before the cut; SKILL.md now keeps a shorter form of each, and the card citations, pages, DOIs and quotes it dropped are kept here.

- Stated: "However, by design, the MIO approach maintains a suboptimality gap throughout computation and can therefore be terminated, before optimality is certified, with a certificate of suboptimality." [S225 p. 31]; [02 E1, E2, J2].
- ✗ "Critic-informed checks, not his practice" → equal time is the yardstick of the 1993 review, for others' experiments [S005 pp. 3–4]; his own matched duels from 2002 [S070 pp. 9–15], equal memory [S328 pp. 11–15], one thread and 60 s each, overruns printed [S340 pp. 16, 23]; the critics' SNR grid adopted in 2020 [S095 pp. 3, 10, 21, 23] (C8).

**🔴 Stop rule** [practice, Dunn 2018]: bound stuck at zero or root node not passed → count binaries (n·2^D: 87,808 at depth 6 for n = 1,372); first, where one exists, replace weak big-M by a perspective or convex-integer form [S061 pp. 6–10; S175 pp. 9–10, 15–16]; if the bound still stalls, switch to local search with restarts, and (*correction*) drop *optimal* from the claim. Checks the critics asked for, practised in his later papers (C8): low SNR (DOI 10.1214/19-STS733); equal budgets and threads; path-to-path timing (DOI 10.1214/20-STS806); installable code (DOI 10.1214/20-STS809); LP-relaxation strength (DOI 10.1287/opre.2021.0034).

**Increment books-2026-10-29** (2026-10-29; book material, framing and dating only, outside every say–do count; full account: [Book material](#books)). The ✗ line on the critic-informed checks is re-dated: equal computation time as the yardstick is in print in 1992, in the NRC printing of the simulated-annealing review, word for word as in 1993 [B020 p. 9] (C22). It stays a yardstick applied to Johnson et al.'s experiments, not his own practice, so C8 is unchanged in substance. Also on record, not in SKILL.md: the ML book's description promises solutions that "can be certified to be optimal in minutes/hours" and "outperform classical heuristic approaches in out-of-sample experiments" [B008 p. 1; B010 p. 1] (the stated side of Tension T1); a teaching case puts a fast heuristic beside an integer-optimization formulation, then results (titles only) [B018 p. 2]. The line before this increment (verbatim):

```text
- ✗ "Critic-informed checks, not his practice" → equal time is the yardstick of the 1993 review, for others' experiments [S005 pp. 3–4]; his own matched duels from 2002 [S070 pp. 9–15]; the critics' SNR grid adopted in 2020 [S095 pp. 3, 10, 21, 23] (C8).
```

**Claim census 2026-10-29** (earlier wording, verbatim):

```text
- ⚠ Scope: MIO-for-ML methods papers; clinical collaborations use tuned off-the-shelf ensembles [S054 pp. 2, 4].
1. Replace the greedy or trial-and-error step by one joint model (all tree splits at once; all regression goals in one MIQO [S081 pp. 2–3, 5–8]).
**Limitations**: needs a commercial MIO solver; weak for continuous NLP; warm starts alone are routine in IO; a simple incumbent can be proved best [S310 pp. 4–8, 12].
```

Census items k = 110, 111, 118. k = 110: one clinical paper cannot show what clinical collaborations do; *usually* now rests on 08 §3 row 17 (seven cards), with S054 as the instance, an XGBoost model tuned by cross-validated AUC (pp. 2, 4). k = 111: the S081 card puts the properties that are linear constraints into one MIQO (Table 1, p. 3; pp. 5–8) but checks bootstrap significance and the condition number after fitting and enforces them by no-good cuts and re-solves (Stage 3, p. 8); *all regression goals* is narrowed, and the tree example, absent from S081, now carries its own card, one MIO over the whole tree [S011 pp. 13–14]. k = 118: the S310 card proves mean imputation asymptotically optimal (infinite data, a universally consistent learner), while mice wins in some finite-sample settings (pp. 9, 11); *proved best* is narrowed to *proved asymptotically optimal* (flagged by one auditor, confirmed in the card).

<a id="method-5"></a>
## Method 5: Judge by the decision, against the owner's current rule

**Before this synthesis** (verbatim):

```text
### Method 5: Judge by the decision, against the owner's current rule {DA AP; ML RO}
**One line**: Start from the owner's decision, data and current rule; learn inside the decision; score decisions, not predictions, against that rule; report your own costs; field-test.
**Evidence**:
- Stated: problems and data lead, models support (seven statements 2004–2025); prescription, not prediction (six); a coefficient of prescriptiveness as R² for decisions; propose, then field-test [02 P1, R6, R14, E5–E7].
- Practice: health-care costs against last year's cost (DOI 10.1287/opre.1080.0619); ISO New England unit commitment with its own run time reported, 6.14 h against 1.65 h (DOI 10.1109/TPWRS.2012.2205021); P = 88% on a media firm's data (DOI 10.1287/mnsc.2018.3253); Boston buses (DOI 10.1073/pnas.1811462116) [03 B4.2].
- Say–do consistency: ✅ stated + practised.
**Steps**:
1. Owner, decision, data, current rule.
2. The current rule is the baseline; prefer the stronger naive rule (last year's cost, not random).
3. Shape the class around the data that exist (auxiliary covariates, not the uncertain quantity itself).
4. Learn and decide in one model: ML weights (kNN, CART, random forests) inside conditional stochastic optimization; prescriptive trees where people must see why.
5. Score with a decision metric; report your own costs, even when slower.
6. Propose, then field-test; say what the evaluation cannot show (chemotherapy models that only merit a trial, DOI 10.1287/mnsc.2015.2363); one applied paper per deployment.
**🔴 Checkpoints**: his group's fix: ML weights turn optimistic in high covariate dimension → a bootstrap-robust layer (DOI 10.1007/s10107-021-01679-2). *Corrections*: let stakeholders see and contest the trade-offs before the vote (Boston's approved start-time plan was never implemented) [05 §5.1]; score forecasts on the field's metric (DELPHI relative WIS 0.99 against the naive 1.00, DOI 10.1073/pnas.2113561119) [05 §5.2].
**Applies to stage**: problem choice; experiments; judging; deployment.
**Different from standard practice**: decisions, not predictions, are scored against the owner's rule; the line (v1 by his student Kallus, February 2014) predates Elmachtoub–Grigas (arXiv 1710.08005), the only comparator checked.
**Limitations**: needs partner access and a track record; deployment outcomes are thin.
```

**Full-text evidence.**
- *Strongest practice (84 works)*: the practitioners' equal-split rule as baseline and cost in cents per share as metric [S009 pp. 3–4, 9–10, 13–25]; the industry's bid-price control as baseline with revenue and run times [S034 pp. 2, 4, 14–21]; ISO New England staff as co-authors supplying the system, the data and the operator's reserve practice as baseline [S006 pp. 1, 5–9]; the FAA's rules replayed in historical order [S114 pp. 2–3, 12–18]; the transplant committee's proposal scored in its own simulator [S044 pp. 5, 18–22]; the liver-allocation rule scored in the owner's policy simulator [S094 pp. 3, 5, 9]; tenure committees' decisions at equal capacity [S206 pp. 9–12]; an employer's claims and what it actually paid [S909 pp. 1, 9, 11, 17, 21–28]; the media firm's data with the prescription score [S008 pp. 10–12, 21, 29, 31]; Boston routes and bell times [S137 pp. 2–6]; a mining group's pre-2006 rule against EBITDA [S339 pp. 6, 8–11]; physicians' actual prescriptions [S370 pp. 2, 13, 15–18; S692 pp. 2, 4–6, 9–10, 19]; the owner's actual pandemic policy in every region [S482 pp. 3–4, 8–11].
- *Stated*: "Considering the uncertainty associated with new releases, we feel that this is a positive result, but at the same time what truly matters is the performance of the prescription in the problem." [S008 p. 29]; "This experiment highlights the fact that size calculations alone cannot predict performance." [S013 p. 32]; "Our objective, however, is not to predict for the sake of prediction but, more importantly, to implement our innovations in hospitals for real-world impact." [S617 arXiv p. 7].
- *Counterfactual replay against the owner's historical decisions* (cluster 14, 25 works): [S206 pp. 9, 12; S325 pp. 7–9, 13–14; S444 pp. 10–21; S682 pp. 2–7]. *Score the decision, not the prediction; audit the field's metric* (cluster 15, 24 works): [S095 pp. 4, 12; S162 pp. 10, 13; S679 pp. 2, 12–14; S522 pp. 7–9].
- *Say–do*: ✅ in OR, analytics and deployment papers; narrowed for clinical prediction papers.

**Variants and contradictions.**
- ✗ *Say–do narrowed* (08 §3 row 19; C11): 15 contradictions. Fourteen are prediction papers of 2014–2026, twelve of them clinical, that score predictions (AUC and the like) with no decision and no current-rule baseline [S557 pp. 4, 8, 13; S281 pp. 3, 6; S054 pp. 4–9; S127 pp. 1, 5, 7–8; S219 pp. 5–7; S023 pp. 1, 3, 7–8; S351 pp. 1, 16–19, 22–23; S381 pp. 2, 7–8; S390 pp. 1, 3–5; S621 pp. 2–3, 16–18; S683 pp. 1–2, 5–6; S677 pp. 1, 8–9; S678 pp. 5–6, 9–10; S872 pp. 3–4]; the fifteenth is a vaccine-site plan whose headline gain is measured against the weakest of its constructed rules [S083 pp. 1, 17–18, 23]. Variants: constructed or literature baselines instead of the owner's rule [S193 pp. 6, 28–31; S028 pp. 12–15]; a constructed data-poor rule in the prescriptive paper itself [S008 pp. 30–31]; in 1988–1996 the comparator is the re-optimization ideal [S048 pp. 27, 71; S017 pp. 3, 12]: "It is a fair conclusion to say that a priori and re-optimization strategies perform comparably, on average." [S017 p. 12].
- ⚠ *Bias-signed evaluation* (08 §3 row 20; cluster 13, 25 works 2013–2026): when the counterfactual cannot be observed, proxies whose bias runs in a stated direction: a simulation metric biased toward the model next to a matching metric [S078 pp. 14–16]; input guards so savings are understated [S909 pp. 12, 19, 28]; a pessimistic proxy for an unobserved event time [S481 pp. 2–3]; ground truths from several models in turn [S174 pp. 22–25; S370 pp. 15–16; S343 pp. 6, 8]; confounding calibrated with a known sign [S393 pp. 6–7, 13, 20]; trial emulation [S692 pp. 2, 4, 7–8]; frozen models scored blind by the data owner [S527 pp. 1, 20]; a conservative control group stated as such [S617 arXiv p. 25]. Heuristic-eligible, folded into the M5 checkpoints because of the cap.
- ⚠ *Design for adoption* (08 §3 row 21; cluster 23, 33 works 2002–2026): start from what blocks implementation [S012 pp. 1, 14; S026 pp. 11–12]; keep the incumbent's inputs, format and standard [S114 pp. 4–5, 11–12; S044 pp. 1, 6, 18–19]; an adoption term penalizing distance from the status quo [S416 pp. 8, 14, 32]; staged deployment, better inputs to the owner's rule first [S384 pp. 2, 5, 7–9; S339 pp. 8–9]; an integration section mapping the model onto the owner's process [S076 pp. 22–23; S245 pp. 11–13; S621 pp. 20–22]; a physician-champion pilot then staggered roll-out [S617 arXiv pp. 11–14]. Quotes: "In our work, we restrict our attention to policies that comply with the precise constraints imposed by current practice." [S044 p. 6]; "That is, we hope that our work allows future TFM research, including our own, to build upon a foundation that has a high likelihood of being accepted in practice." [S114 p. 5]. Validation cascade (cluster 29) and field impact studies: external sites [S054 pp. 2–3, 5, 8], a hospital abroad [S325 pp. 3–4, 9; S615 pp. 7, 19–21], temporal external validation [S678 pp. 6, 15], negative controls [S680 pp. 2, 6–9, 12–15]; difference-in-differences [S115 pp. 22–24; S617 arXiv pp. 22–25].
- ✗ *Boston* (08 §3 row 22; C12): the PNAS paper itself says the start times had not been implemented because of parents' concern (p. 2) and calls it a delay later (p. 6) [S137 pp. 2, 6]: "These start times have not been implemented yet due to parents concern with the magnitude of the change" [S137 p. 2]; the trade-off curve was shown to the district [S137 p. 5]. The group's own 2020 account says the plan did not become reality and names missing school-level engagement and missing comparisons with current times as causes [S262 pp. 10–12]: "Ultimately, the district decided that such an important decision should not be implemented without deeper community engagement, and the new bell times did not become a reality." [S262 p. 12]. A 2022 scheduling paper shows its metrics at town halls and reports non-adoption plainly [S243 pp. 17–28]. The stakeholder lesson is also his group's own.
- ✗ *DELPHI* (08 §3 row 23): the hub evaluation puts DELPHI's relative WIS at the baseline level [S021 pp. 2, 4]; the group's own CDC comparison uses its own metric and window [S103 pp. 14–16]; a German–Polish hub scores DELPHI worse than the naive baseline (higher mean WIS) for one- and two-week cases and one-week deaths, better for two-week deaths [S157 pp. 15–16]. Hub papers (S021, S110, S157) are outside evaluations in which he is only a consortium member [S110 pp. 2–3, 17; S021 pp. 10–11; S157 pp. 21–22]; they are not evidence of his method.
- *Checkpoint kept*: ML weights turn optimistic in high covariate dimension → a bootstrap-robust layer [S139 pp. 3–4, 15–16]; its radius is set in advance from a disappointment level [S139 p. 19].

**Moved at the tighten step** (T3.7, 2026-10-29). These SKILL.md lines are copied verbatim as they stood before the cut; SKILL.md now keeps a shorter form of each, and the card citations, pages, DOIs and quotes it dropped are kept here.

- Stated: "what truly matters is the performance of the prescription in the problem" [S008 p. 29]; statements 2004–2025 [02 P1, R6, R14, E5–E7].
- ✗ Fourteen prediction papers of 2014–2026, twelve clinical, score predictions with no decision or current-rule baseline [S557 pp. 4, 8, 13; S054 pp. 4–9]; a vaccine-site plan's headline gain is against its weakest constructed rule [S083 pp. 1, 17–18, 23].

**🔴 Checkpoints**: his group's fix: ML weights turn optimistic in high covariate dimension → a bootstrap-robust layer (DOI 10.1007/s10107-021-01679-2) [S139 pp. 3–4, 15–16]. Unobservable counterfactual → a proxy whose bias favours the incumbent, direction stated [S078 pp. 14–16; S909 pp. 12, 19, 28]. *Corrections*: let stakeholders see and contest the trade-offs before the vote (Boston's approved start-time plan was never implemented) [05 §5.1; S262 pp. 10–12]; score forecasts on the field's metric (DELPHI relative WIS 0.99 against the naive 1.00, DOI 10.1073/pnas.2113561119) [05 §5.2; S021 pp. 2, 4].

**Limitations**: needs partner access and a track record; outcome studies exist for a few deployments only [S115 pp. 22–24]; in 1988–1996 his comparator was the re-optimization ideal, not an owner's rule [S048 pp. 27, 71; S017 pp. 3, 12].

**Increment books-2026-10-29** (2026-10-29; book material, framing and dating only, outside every say–do count; full account: [Book material](#books)). The Stated line adds the 2019 book's sixth principle, "The ultimate objective in the real world is prescription,not prediction." (as printed) [B009 p. 1]. Teaching-level statements, not added: decision support "through real world applications", with management-science techniques "only as tools to facilitate problem solving" (2004) [B014 p. 1]; "Problems and data play a leading role in this book, while models play an essential but supporting role." (2016) [B017 p. 1]. ⚠ None of these names an owner, a current rule or a decision metric [B017 p. 1]. The line before this increment (verbatim):

```text
- Stated: "what truly matters is the performance of the prescription in the problem" [S008 p. 29].
```

**Claim census 2026-10-29** (earlier wording, verbatim):

```text
- ✗ Fourteen prediction papers of 2014–2026, twelve clinical, score predictions with no decision or current-rule baseline [S557 pp. 4, 8, 13]; a vaccine-site plan's headline gain is against its weakest constructed rule [S083 pp. 1, 17–18, 23].
2. The current rule is the baseline; prefer the stronger naive rule (last year's cost, not random); replay the owner's historical decisions [S206 pp. 9, 12].
```

Census items k = 125, 127. k = 125: the counts (fourteen prediction papers, twelve clinical) come from 08 §3 row 19, not from one card; they now cite it, and S557 stays as the instance: prediction only, another classifier as the baseline, the doctor-warning decision left to future work (pp. 4, 8, 13). k = 127: *last year's cost, not random* is the S050 baseline, the owner's naive rule, much stronger than random (p. 5); the tenure card's stronger naive rule is a five-year citation threshold (pp. 10–11), so the example now cites S050.

<a id="method-6"></a>
## Method 6: Run research as programmes

**Before this synthesis** (verbatim):

```text
### Method 6: Run research as programmes: impact gate → cohort → course → book → company {ALL}
**One line**: Start a topic only if full success would be taught in a graduate course or used by a company within a few years; then cohort, course, a book with a former student, and a company when adoption needs scale.
**Evidence**:
- Stated: the impact test, 11 statements on 5 occasions 2014–2026 (assume 100% success, ask what changes, answer before the research; homepage essay; oral history pp. 6–7); courses become books; companies for scale, hedged in 2014 [02 T1, R1, R4, O8, C9].
- Practice: seven programme lineages [04 A.4]; courses 15.094 and 15.095; books with Dunn (2019), den Hertog (2022), Gamarnik (2022), Orfanoudaki and Wiberg (2025) [01 §1.9]; Interpretable AI 2018.
- Say–do consistency: ✅ for steps 2–5; ⚠️ step 1 stated only: the pre-start test cannot be observed, though students restate it [04 B.2, B.5].
**Steps**:
1. Gate: assume 100% success. Would a graduate course teach it (an undergraduate course marks a once-or-twice-a-career breakthrough)? Would a company use it within 2–5 years (two in 2025)? Would it improve understanding of how the world works? No answer in advance → do not start.
2. Pose the student's first problem at the first meeting; agree by mutual convincing.
3. A thesis lineage per programme, with co-advisers from a close network (Odoni, Tsitsiklis, Parrilo).
4. A new course while the programme is live (15.094 Robust Optimization; 15.095 Machine Learning under a Modern Optimization Lens).
5. A book years later with a former student or colleague, through his own press; a company when adoption needs scale.
**🔴 Exit**: no stated exit rule; programmes fade (robust probability stopped after its two students graduated) [06 §7]. *Skill rule, not his*: when the last student has graduated and manuscripts have sat two years as submitted, close or hand off explicitly.
**Applies to stage**: agenda; problem choice; organisation.
**Different from standard practice**: the gate weighs teachability and adoption, decided in advance, instead of novelty and feasibility.
**Limitations**: very high resources (16–26 PhD students, 70% industry funding in 2014, his own press and companies); a senior strategy by his own account; the gate transfers, the lifecycle only partly.
```

**Full-text evidence.**
- *Strongest practice (187 works, mostly the lineage step)*: the thesis problem class came from his adviser's group [S048 pp. 18, 71, 125]; a student cohort consolidated in a sole-author survey with a recipe and open problems [S185 pp. 1, 4, 46, 48–49, 51]; a student's thesis line with Tsitsiklis as co-author [S072 pp. 1, 8, 10, 32–33], co-advised according to the DSpace advisor fields [04 A.2]; an organ-allocation programme in three stages carried by successive theses, with a former student (Trichakis, note 04 §A.2) among the co-authors [S476 pp. 1–2] (*fix round*: the byline after the first author is alphabetical and states no roles, so *co-senior* is withdrawn); programme continuity with a reused data asset and a software adoption channel [S097 pp. 5, 10, 27–28, 56]; a student-carried lineage from best subset to slowly varying regression with released code [S317 pp. 1, 5, 7–8, 39]; HAIM to xHAIM carried by a new cohort [S390 pp. 1, 8]; a company carrying the routing method to other districts [S262 p. 13]; a decade-long hospital partner with more than 20 projects [S617 arXiv pp. 1–2, 9, 28, 31].
- *Variants (8)*: the company before the paper [S050 pp. 1, 10]; a modelling package as the adoption channel [S028 pp. 2–3, 10]; a professional society and its registry as carrier [S364 pp. 3, 5]; lines he sponsors and edits outside optimization [S132 pp. 1, 13, 15; S478 pp. 1, 21–23; S616 pp. 1, 4–5]; a topic that predates the collaboration [S666 p. 15]; teachability argued after the fact [S018 pp. 4, 23].
- *Own earlier result's limit as the entry point* (cluster 20, 19 works; M6 and H7 evidence, too generic for a heuristic): [S068 pp. 2, 5–6; S192 pp. 5–6; S440 pp. 1–2; S456 pp. 3–4; S457 pp. 2–3].
- *Collaboration roles in 2021–2026* (08 §9): the senior sponsor and editor of student-led lines outside optimization, stated in contribution sections [S299 p. 10; S132 pp. 1, 13; S478 pp. 1, 21; S682 p. 7; S618 pp. 1, 15]; the analytics partner inside a clinical team's study [S238 pp. 1–2; S707 pp. 1, 5, 11; S686 pp. 1, 13; S439 pp. 1, 8]; quote: "D.B. directed the overall project, from concept and research to implementation, and edited the manuscript." [S617 arXiv p. 28].
- *Say–do*: unchanged. Courses and books appear only at abstract level [S792; S793; S020; S128; S209; S047; S084; S334; S695], and the pre-start gate cannot be seen in papers.

**Moved at the tighten step** (T3.7, 2026-10-29). These SKILL.md lines are copied verbatim as they stood before the cut; SKILL.md now keeps a shorter form of each, and the card citations, pages, DOIs and quotes it dropped are kept here.

- Stated: the impact test, 11 statements on 5 occasions 2014–2026 (homepage essay; oral history pp. 6–7); courses become books; companies for scale, hedged in 2014 [02 T1, R1, R4, O8, C9].
- Practice: the thesis problem class came from his adviser's group [S048 pp. 18, 71, 125]; a cohort consolidated in a sole-author survey with open problems [S185 pp. 1, 4, 46, 48–49, 51]; an organ-allocation programme over successive theses, with a former student among the co-authors [S476 pp. 1–2]; seven lineages [04 A.4]; books with Dunn (2019), den Hertog (2022), Gamarnik (2022), Orfanoudaki and Wiberg (2025) [01 §1.9]; Interpretable AI 2018.
- ⚠ The company before the paper [S050 pp. 1, 10]; a modelling package as adoption channel [S028 pp. 2–3, 10]; lines he sponsors outside optimization [S132 pp. 1, 13, 15]; teachability argued after the fact [S018 pp. 4, 23].

**Increment books-2026-10-29** (2026-10-29; book material, framing and dating only, outside every say–do count; full account: [Book material](#books)).
- **Practice line extended**: only the 1997 preface states that a book came from a course: "The book was developed while we took turns teaching a first-year graduate course at M.I.T., for students in engineering and operations research." [B001 p. 1]; it does not name the course. Publisher pages name MIT classes that use three later books: "The book is used in" the PhD class Integer and Combinatorial Optimization (2005) [B006 p. 1] and the core MBA class Data, Models, and Decisions, with most chapters and cases pre-tested at eight named schools (2004) [B014 p. 1]; the 2016 authors have used their book to teach a one-semester Sloan class and a shorter executive class with a named chapter subset, and the edX MOOC 15.071x is "based on this book" (the MOOC ran from 2014 [06 §1]) [B017 p. 1]. These pages name the classes as users of the books; none says that a book came from its named class, though the 2005 page has examples and exercises "developed through extensive classroom use" [B006 p. 1] and the 2004 page chapters "pre-tested in classrooms" at eight schools [B014 p. 1]. The pages of the 2019–2025 books name no course [B009 p. 1; B011 p. 1; B013 p. 1; B019 pp. 1–2]. His own pages list all eight books as Dynamic Ideas editions, the two first published elsewhere included [B008 pp. 1–2]. *Fix round*: the first wording, "each from a course named in its front matter" (SKILL.md) and "each book's front matter names its course" (here and in 08), is withdrawn: B006, B014 and B017 are publisher pages, not front matter, and the course → book direction is stated only for 1997, in line with the oral-history account [01 §1.9].
- **⚠ line added**, carriers the steps omit: the 1997 book kept up by a dated errata sheet organised by printing, last updated 7/5/2021, through at least six printings [B003 p. 1]; RO taught inside his existing graduate methods course 15.093J (lecture 8 of 24, after sensitivity analysis) by 2009 [B021 pp. 1–2], beside the new courses of step 4. *Fix round*: "corrected by printing for 24 years" and "core methods course" are withdrawn: the sheet carries one date, its last update, so a continuous record from 1997 is not shown [B003 p. 1], and the course pages call 15.093J "Graduate", not core [B021 p. 1].
- Not in SKILL.md: Ramana adopts the book for his own course in its first year [B005 p. 13] (a teaching-adoption signal, not the impact gate); the 2025 book is offered as a free PDF for academic use, but only through a request form [B019 p. 2]; the pool candidate *pre-test a book in other schools' classrooms* [B014 p. 1] joins card S792's *a course as the book's beta test*.

The line before this increment (verbatim):

```text
- Practice: the thesis problem class came from his adviser's group [S048 pp. 18, 71, 125]; a cohort consolidated in a sole-author survey with open problems [S185 pp. 1, 4, 46, 48–49, 51]; an organ-allocation programme over successive theses [S476 pp. 1–2]; books with former students and colleagues, 2019–2025 [01 §1.9]; Interpretable AI 2018.
```

**Claim audit 2026-10-29, round 1** (earlier wording, verbatim):

```text
- ⚠ The company before the paper [S050 pp. 1, 10]; teachability argued after the fact [S018 pp. 4, 23].
```

SKILL.md packet, item k = 15 (flagged by the official auditor only): the card reads teachability only from the remark that textbooks ignore the 1937 Uspensky bound, and labels that reading [inferred, thin] [S018 pp. 4, 23]; the line now carries the label.

<a id="method-7"></a>
## Method 7: Bound before policy (promoted 2026-10-29)

**Before this synthesis**: not in SKILL.md. Readers proposed it repeatedly as an early-career pattern; the operator's summary of their proposals was: relaxation as bound, policy source and yardstick; provable ratio; tightness check (not a quotation). The cards' own labels include *policy from the relaxation, certified by the same relaxation* [S051] and *bound, constructive heuristic, provable ratio, tightness instance* [S052].

**Cards (79 distinct works read in full or in part, 1988–2026, version pairs merged; 08 §4)**. The core: lower bounds over all policies and constant-factor policies in dynamic routing [S016 pp. 3, 5–11; S032 pp. 3–15; S091 pp. 3, 11–17, 25–28; S597 pp. 13–31]; the radial bound and cyclic heuristic [S017 pp. 7–10]; the LP relaxation as object, yardstick and lever [S052 pp. 3, 7–9, 10–18, 20–21; S269 pp. 1–2, 5, 17; S036 pp. 6–10; S015 pp. 2, 10–13; S345 pp. 1–8; S166 pp. 2–25]; achievable-region relaxations, hierarchies and heuristics [S185 pp. 22–25, 29–32, 48–49; S580 pp. 9–10, 38–40, 47–48; S072 pp. 2, 20–22, 26–31; S368 pp. 4–8, 10–13; S051 pp. 1, 5–11; H010 pp. 23–28]; fluid relaxations as bound, template and yardstick [S130 pp. 7–8, 13, 17–18; S205 pp. 9–11, 26–27, 35; S207 pp. 12–16]; relax, randomize, then pack with an exact IP certified by the LP bound [S043 pp. 7–9, 16]; SDP bounds to certify fluid policies [S007 pp. 9, 16–18]; LP-relaxation quality as yardstick in ADP [S070 p. 9]; adaptive RO: the price of static and affine policies with tight families [S134 pp. 6, 12–18; S176 pp. 13–14; S192 pp. 16, 18–19; S042 pp. 2–3, 25–26], sampled lower bounds from binding scenarios [S138 pp. 7–9; S082 pp. 12, 15, 17; S087 pp. 9–11, 34–35], conservative benchmark bounds [S049 p. 14; S153 p. 23]; tight ratio bounds [S191 pp. 5–8; S392 pp. 15–17, 19–20]; relaxations certifying heuristics in 2023–2025 [S274 pp. 29–30; S403 pp. 16, 31–32; S684 pp. 11–12, 16–17].

**What the cards show.**
- The bound comes first and is valid for every policy: heavy- and light-traffic bounds before any policy is analysed [S016 p. 3]; "First, we establish some lower bounds on the average system time for all policies." [S016 p. 3]; a sequence of lower bounds in the discrete-optimization tradition [S072 p. 2]: "In the tradition of discrete optimization in the mathematical programming community, we develop a sequence of lower bounds to the optimal cost." [S072 p. 2]; Lagrangean duals and LP relaxations as the bounds that feed branch and bound and judge heuristics [S269 pp. 1–2, 5, 17].
- The policy is read off the bound's solution: primal support and reduced costs give a priority index [S051 pp. 7–9]; visit rates rounded into routing tables by an IP [S185 pp. 29–31; S293 pp. 23–31]; fractional flows decomposed by randomized rounding into a path pool [S043 pp. 7–9]; the schedule tracks the fluid optimum [S205 pp. 9–11]; LP values read as probabilities [S121 pp. 3–9; S007 pp. 33–35]. "To the best of our knowledge, there is no systematic approach to derive policies from relaxations." [S368 p. 2].
- The policy is graded against the same bound, as a ratio or gap, and the incumbent heuristics are graded the same way [S072 pp. 26–31; S185 pp. 25, 32, 48; S368 pp. 10–13; S153 p. 23]: "The suboptimality guarantees defined as best bound/best policy range from 0 to 2.5% under symmetry conditions" [S368 p. 1].
- Tightness is checked (cluster 2, 29 works): tight families in both directions [S052 pp. 20–21]; a tight instance by symmetry and a forced repeating step [S161 TR pp. 3–5; S289 pp. 7–11]; a bound attained by an explicit family [S191 pp. 7–8; S176 pp. 13–14; S392 pp. 15–17]; exactness fenced by a computed counterexample [S042 pp. 25–26; S028 p. 8]; unproved constants printed as conjectures [S016 pp. 7, 9; S032 pp. 7–8, 11, 16; S158 pp. 15, 17]. "is the bound inherent in the algorithm or is it because of the weakness of our proof methods?" [S289 p. 2].
- When the gap stays open, the relaxation is strengthened by interaction order or PSD constraints, and size limits are printed [S185 pp. 22–24, 44–45; S051 pp. 6–7; S072 pp. 20–22; S684 pp. 11–12, 17]; the loose side is named when it cannot be measured [S072 p. 26; S212 p. 24].

**Four checks.**
1. *Cross-project recurrence* ✅: 79 works in all eight periods (9, 16, 20, 4, 5, 9, 7 and 9 works from 1988–92 to 2023–26), domain tags IO 53, LO 31, SD 30, CP 23, RO 21; coauthor groups from van Ryzin [S016], Goemans [S052], Orlin [S269], Paschalidis–Tsitsiklis [S072], Niño-Mora [S051] and Stock Patterson [S043] to Goyal [S134; S176; S165], Bidkhori [S192], Iancu–Parrilo [S042; S075], Georghiou [S082], Dunning [S087], de Ruiter [S138] and Na, Stellato and Wang [S392].
2. *Say–do* ✅: stated in his sole-author survey, which contrasts the ad hoc methods of stochastic control with mathematical programming's plan of attack that yields optimal solutions or a guaranteed degree of suboptimality, and lists bounds on the gap between heuristic policies and relaxations as the next step [S185 pp. 1–2, 51]; stated jointly that judging heuristics against other heuristics says little about their suboptimality, and that the approach delivers a feasible policy with a suboptimality guarantee [S051 pp. 1, 11]: "We have proposed an approach that provides a feasible policy together with a guarantee for its suboptimality for the restless bandit problem." [S051 p. 11]; SDP relaxations give suboptimality guarantees for heuristic policies [S007 p. 18]. *Fix round*: no card links the method by name (it was promoted after the reading), so the 79 works are those whose cards show its steps, and contradictions were not searched for. Two core works skip a step: the restless-bandit paper names Whittle's index as the incumbent but grades only greedy against its bound [S051 pp. 3, 10], and the network paper reads no policy off its bound, taking the upper-bound policies from simulation search or the literature [S072 pp. 27–30].
3. *Executable, and different from standard practice* ✅: the steps produce actions that a heuristic-versus-heuristic study or an exact-DP study would not take (derive a bound for all policies first; extract the policy from the bound's solution; grade the incumbent by the same bound; build the tight instance). The practice it replaced: problem-specific formulations and heuristics compared only with each other [S185 pp. 1–2; S051 p. 1], and affine policies advocated without quality results [S042 p. 3]: "However, to the best of our knowledge, apart from these theoretical advances, there has been very little progress in proving results about the quality of the objective function values resulting from the use of such parameterizations." [S042 p. 3].
4. *Exclusivity* ✅ (qualified; [inferred], since no card compares him with peers). Counter-evidence on the cards: heuristic ratios were the Steiner and approximation literature's before S052 sharpened them into ratios to the LP bound [S052 pp. 3, 11]; in queueing, the performance-region approach is credited to Coffman–Mitrani, Gelenbe–Mitrani, Federgruen–Groenevelt, Shanthikumar–Yao and Tsoucas [S580 p. 12; S185 pp. 3–4; S057 pp. 3–4], Whittle's relaxation is the first rung of the hierarchy [S185 p. 21; S051 p. 3], and the loss-network relaxation is Kelly's bound in LP form, "close in spirit" [S368 p. 8]. So in IO alone, or in SD alone, the check fails. What is claimed as distinctive: one bound–policy–yardstick loop carried across SD, IO, RO and CP from 1988 to 2026, with the incumbent graded by the same bound; the cards record the practice it replaced where it entered (heuristics judged against heuristics or by simulation alone [S051 p. 1; S072 p. 2]; affine policies advocated without quality results [S042 p. 3]). The check passes only on that cross-domain loop. If exclusivity is read as a hard gate that needs carded peer comparisons, Method 7 would drop to a heuristic, and the heuristics are at their cap of ten (08 §5): that is the open choice for the operator. (*Fix round*: the earlier citation of [S052 p. 2] for *standard in approximation algorithms* is withdrawn; that page says only that NP-hardness typically leads to approximate solutions.)

**Variants.** Asymptotic regimes for sharp constants (cluster 3, 22 works, 19 of them 1988–2002): the bound of the probabilistic-analysis years [S038 pp. 6–8, 10–12; S016 pp. 5–14; S130 pp. 4, 13, 22; S310 pp. 5–7]; exclusivity weak (the Beardwood–Halton–Hammersley and Steele tradition [S038 pp. 4–5]). Adaptive policies, power and limits of a tractable policy class (cluster 10, 17 works) [S134 pp. 6, 12–18; S165 pp. 21–22, 24; S217 pp. 9–11; S060 pp. 15, 23]: "We refer to the ratio of the optimal cost of the robust problem and the optimal cost of the two-stage stochastic problem as the stochasticity gap." [S134 p. 1].

**Limitations.** Bounds can be loose without telling which side [S072 p. 26; S212 p. 24]; policies from relaxations were admitted to be ad hoc and missing for networks [S185 p. 49]; 45 of the 79 works date from 1988–2002; when an exact MIO solves at scale, Method 4's solver gap replaces the proved ratio [S010 pp. 27–40]; the yardstick is the bound or the re-optimization ideal, not an owner's current rule (contrast Method 5) [S048 pp. 27, 71; S017 pp. 3, 12]. Part of the 1992–1999 achievable-region series is abstract- or metadata-level [S587; S468; S507; S581; S656; D007; D008; S798], so the SD evidence rests on the surveys [S185; S580] and the papers read [S072; S057; S051; S368; S130; S205; H010; S212].

**Moved at the tighten step** (T3.7, 2026-10-29). These SKILL.md lines are copied verbatim as they stood before the cut; SKILL.md now keeps a shorter form of each, and the card citations, pages, DOIs and quotes it dropped are kept here.

- Stated: "Furthermore, the quality of proposed heuristics is usually assessed by comparing their empirical performance with that of alternative heuristics, which gives little information about their degree of suboptimality." [S051 p. 1]; heuristic–relaxation gaps named as the next step (sole author) [S185 pp. 1–2, 51].
- Practice: bounds over all policies, then constant-factor routing policies [S016 pp. 3, 5–11]; policies read off achievable-region relaxations [S185 pp. 22–25, 29–32]; a primal–dual index policy with a suboptimality bound [S051 pp. 5–11]; static and affine policies priced against adaptive optima, tight families shown [S134 pp. 6, 12–18].

1. Write a relaxation valid for every policy: LP or conservation-law, fluid or Lagrangean, a limiting regime, sampled scenarios [S185 pp. 8–12; S138 pp. 7–9]; which bound and device fit which structure: technique catalog §1.2.
2. Read the policy off its solution: indices from reduced costs, rounding, tracking the fluid optimum, an affine rule [S051 pp. 7–9; S205 pp. 9–11].
3. Prove the policy's ratio to the bound: a constant factor, an asymptotic optimality, or a price of the policy class [S016 pp. 5–11; S192 pp. 16, 18–19]. No ratio provable → report the computed gap per instance and regime, and say so [S368 p. 1; S072 pp. 26–27].
4. Check tightness: an instance attaining the ratio, or a counterexample just outside exactness; open constants printed as conjectures [S052 pp. 20–21; S042 pp. 25–26].
5. Grade every heuristic, the incumbent's included, by its gap to the same bound [S072 pp. 26–31; S368 pp. 10–13].

**Different from standard practice**: one bound grades the incumbent and every heuristic, in a loop carried across queueing, routing, IO and adaptive RO. Bound-first alone is not his (approximation algorithms [S052 pp. 3, 11]; conservation laws, Whittle's and Kelly's bounds [S185 pp. 3–4, 21; S368 p. 8]): claim novelty for the transfer and the graded incumbent.

**Limitations**: a bound can be loose without telling which side: "Since the optimal cost is not known, we cannot calculate the closeness of our lower bound to the optimal cost." [S072 p. 26]; mostly 1988–2002 work; where an exact MIO solves at scale, Method 4's gap replaces the ratio [S010 pp. 27–40]; the yardstick is a bound, not an owner's rule (Method 5).

**Claim audit 2026-10-29, round 1** (earlier wording, verbatim):

```text
5. Grade every heuristic, the incumbent's included, by its gap to the same bound [S072 pp. 26–31].
```

```text
**Different from standard practice**: one bound grades the incumbent and every heuristic, in a loop carried across queueing, routing, IO and adaptive RO. Bound-first alone is not his (approximation algorithms [S052 pp. 3, 11]; conservation laws, Whittle's and Kelly's bounds [S185 pp. 3–4, 21; S368 p. 8]): claim novelty for the transfer and the graded incumbent.
```

SKILL.md packet, item k = 16: the network paper computes efficiency only for the best policy found per instance, which certifies the incumbent Harrison–Wein policies, with FCFS tabulated beside them [S072 pp. 26–31]; a gap for every heuristic is now labelled the skill's rule. Item k = 19: the earlier Steiner ratios (Takahashi–Matsuyama, Kou et al., Plesnik, El-Arbi) were measured against the optimum, and measuring against the LP bound is the paper's own strengthening [S052 pp. 3, 11]; the third-party bound-graded heuristics on the card are Johnson's tours, graded by the Held–Karp bound [S052 p. 7].

<a id="workflow-a"></a>
## Workflow A: Problem choice

**Before this synthesis** (verbatim):

```text
### Workflow A: Problem choice
**Input**: candidate problems; partner or data access; the field's tractability belief.
**Steps**:
1. Impact gate and Taste quick-check (→ Method 6).
2. An owner with a decision, data and a current rule? (→ Method 5)
3. Written off as intractable? Since when? What do today's solvers do? (→ Method 2)
4. Owned by another tradition, and writable as LP, conic or MIO in its class? (→ Method 1)
5. A student or cohort to carry it (→ Heuristic 8).
**🔴 Checkpoint**: stop if all three gate proxies fail, or there is neither an owner nor a teachable theory; never use a borrowed speed-up figure as the "why now".
**Output**: a programme card: owner, decision, data, baseline rule, belief challenged, measured tool figure, course, carriers.
```

**Full-text additions.** Step 2: replay the owner's decisions or run the owner's simulator (the committee's proposal in its own simulator [S044 pp. 5, 18–22]; the owner's liver-allocation simulator [S094 pp. 3, 5, 9]; the owner's kidney simulator re-implemented [S476 pp. 1, 6]). Step 3: a belief dated and refuted by solve times [S061 pp. 2, 4, 13]. Step 4: a bound valid for every policy as the target (Method 7). The programme card adds the target bound.

<a id="workflow-b"></a>
## Workflow B: Formulation and idea

**Before this synthesis** (verbatim):

```text
### Workflow B: Formulation and idea
**Input**: the programme card.
**Steps**:
1. Variables, class-keeping device, dual reading, boundary (→ Method 1).
2. One joint model for the greedy or hand-tuned step (→ Method 4); knob and bound for the property to price (→ Method 3).
3. If a heuristic already works, find the robust problem it solves (→ Heuristic 1).
**🔴 Checkpoint**: class left without measured solve times → change the device. *Corrections*: test exactness on a small example; check the LP-relaxation strength of big-M models (his own 2005 emphasis too).
**Output**: formulation, class statement, dual reading, boundary, knob and bound.
```

**Full-text additions.** Exact reformulations for cutting planes: a closed-form inner problem gives a convex integer program without big-M [S061 pp. 6–10; S095 pp. 4–7]; z² = z linearizes a ridge term [S175 p. 9]. Nest the incumbent rule as one setting of the knob [S076 p. 17; S199 pp. 5, 8, 17–18; S104 pp. 9, 13, 17]. Step 3 (new): Method 7 for policies with no exact solve. Step 4 adds Heuristic 10. The LP-relaxation strength check is his own practice in his strongest formulation papers [S015 pp. 2, 4–5, 10; S093 pp. 8–9, 17–19] (C10).

**Moved at the tighten step** (T3.7, 2026-10-29). These SKILL.md lines are copied verbatim as they stood before the cut; SKILL.md now keeps a shorter form of each, and the card citations, pages, DOIs and quotes it dropped are kept here.

**🔴 Checkpoint**: class left without measured solve times → change the device. *Corrections*: test exactness on a small example; check the LP-relaxation strength of big-M models, as his formulation papers do [S015 pp. 2, 4–5, 10; S093 pp. 8–9, 17–19].

**Claim audit 2026-10-29, round 1** (earlier wording, verbatim):

```text
**🔴 Checkpoint**: class left without measured solve times → change the device. *Corrections*: test exactness on a small example; check the LP-relaxation strength of big-M models, as his formulation papers do [S015 pp. 2, 4–5, 10].
```

SKILL.md packet, item k = 20 (flagged by the official auditor only): S015's model is a 0-1 cumulative-variable IP with no big-M constraints, and the card shows no exactness test on a small example. The two corrections now name their sources (the two-period example of 05 §4.3; the big-M critique of 05 §2.5), and the card is cited only for checking the LP strength of his own formulation (strength pursued, LP-bound dominance, facets) [S015 pp. 2, 4–5, 7, 10].

<a id="workflow-c"></a>
## Workflow C: Experimental design and execution

**Before this synthesis** (verbatim):

```text
### Workflow C: Experimental design and execution
**Input**: formulation, instances, the incumbent heuristic, the partner's rule.
**Steps**:
1. Warm starts from the incumbent; stated solver version, machine, threads, time limit and tuning split (→ Method 4).
2. Synthetic data with known truth plus real data; baselines with versions at matched complexity; the partner's rule as baseline; your run time reported (→ Method 5).
3. The regime critics would choose: low SNR, equal budgets, path-to-path timing, released code (*critic-informed, not his practice*).
**🔴 Checkpoint**: lower bound stuck or root node not passed → Heuristic 3, and change the claim.
**Output**: a protocol table (data, baselines, solver, machine, limits, splits, admissions).
```

**Full-text additions.** Matched budgets are his practice (C8): [S317 pp. 13–24; S340 pp. 16, 23; S708 pp. 35–41]. Regimes a critic would choose: SNR grids [S010 pp. 26, 30, 38]; feasibility-border instances [S015 p. 11; S068 pp. 31, 39; S241 p. 30; S275 p. 25]; misspecification and outside-the-set stress tests [S014 p. 12; S053 pp. 16–22; S278 pp. 5–6]; released code [S093 p. 16; S208 pp. 11–14]. Time to the best solution apart from time to proof [S445 p. 24; S488 pp. 25–27; S184 pp. 25–36]; regime maps and phase transitions [S061 pp. 4, 14–19]; asymptotics checked by simulation with a stated stopping rule [S829 pp. 13–17; S080 pp. 14–18; S016 p. 12]; a scale test before trusting a small-n result [S048 pp. 121–123]; where the time goes, step by step [S291 p. 13; S168 pp. 15–16; S316 p. 11]. The label "critic-informed, not his practice" on step 3 is corrected (C8). *Fix round*: a step 5 for stochastic and dynamic policies (simulation with batch means and a stopping rule on the confidence-interval width [S016 p. 12; S829 p. 13]; light to heavy traffic [S016 pp. 5–14]; each policy's gap to the relaxation bound per regime [S072 pp. 26–31; S368 pp. 12–13]; the owner's simulator [S044 pp. 5, 18–22]); the checkpoint tries a stronger formulation before local search ([Method 4](#method-4)); the matched budget of [S340 pp. 16, 23] is noted as set equal, with the rival's overruns printed.

**Moved at the tighten step** (T3.7, 2026-10-29). These SKILL.md lines are copied verbatim as they stood before the cut; SKILL.md now keeps a shorter form of each, and the card citations, pages, DOIs and quotes it dropped are kept here.

5. Stochastic or dynamic policies, the owner's rule included: simulate with a stated stopping rule (batch means; CI width a set fraction of the estimate [S016 p. 12; S829 p. 13]), from light to heavy traffic [S016 pp. 5–14]; report each gap to the Method 7 bound per regime, with its error [S072 pp. 26–31; S368 pp. 12–13]; use the owner's simulator if one exists [S044 pp. 5, 18–22].

**Claim audit 2026-10-29, round 1** (earlier wording, verbatim):

```text
5. Stochastic or dynamic policies, the owner's rule included: simulate with a stated stopping rule (batch means; CI width a set fraction of the estimate [S016 p. 12]), from light to heavy traffic; report each gap to the Method 7 bound per regime, with its error [S072 pp. 26–31]; use the owner's simulator if one exists.
```

SKILL.md packet, item k = 22: per load regime the paper reports only the best policy's efficiency against the bound, and prints a simulation error for one table only (± 0.0009, Table 7) [S072 pp. 26–31]; every policy's gap with its error is now labelled the skill's rule.

<a id="workflow-d"></a>
## Workflow D: Judging results

**Before this synthesis** (verbatim):

```text
### Workflow D: Judging results
**Input**: runs, gaps, out-of-sample results, partner feedback.
**Steps**:
1. Certificate or gap per result (→ Method 4); decision metric against the partner's rule (→ Method 5).
2. Where it wins and where not; negative results in the body; prospective external scoring for forecasts (→ Heuristic 4); a field-test plan.
**🔴 Checkpoint** (*corrections*): the incumbent matches you (OCT at depth 4: 80.4% against 80.7% for CART unconstrained in depth [05 §2.1]) → no headline that the optimal method wins; forecasts at the baseline's WIS → no headline on your own metric; a plan not adopted → *not implemented*, not *delayed*.
**Output**: certificate status, winning regime, decision metric, negative results.
```

**Full-text additions.** Bound-referenced yardstick: every policy as a ratio to a relaxation bound [S072 pp. 26–31; S070 p. 9; S207 pp. 12–16; S368 pp. 10–13]. Bias-signed proxies [S909 pp. 12, 19, 28; S078 pp. 14–16]. Field impact studies by difference-in-differences [S115 pp. 22–24; S617 arXiv pp. 22–25]; the Hartford one is called a descriptive analysis by its authors, with no standard error, and its controls partly used the tool [S617 arXiv pp. 24–25]. The OCT depth-4 comparison is in the card too [S011 pp. 26–36]. Boston: *not implemented yet* is the PNAS paper's wording on p. 2, *delayed* its wording on p. 6 (C12).

**Moved at the tighten step** (T3.7, 2026-10-29). These SKILL.md lines are copied verbatim as they stood before the cut; SKILL.md now keeps a shorter form of each, and the card citations, pages, DOIs and quotes it dropped are kept here.

2. Where it wins and where not; negative results in the body; prospective external scoring for forecasts (→ Heuristic 4); proxies with a stated bias direction [S909 pp. 12, 19, 28]; a staggered roll-out with a comparison group, analysed descriptively [S617 arXiv pp. 22–25].

<a id="workflow-e"></a>
## Workflow E: Writing and dissemination

**Before this synthesis** (verbatim):

```text
### Workflow E: Writing and dissemination (medium evidence; no stated writing method)
**Steps**:
1. Abstract: the community's belief, the measured change, the exact formulation, one headline number (→ Heuristic 9).
2. One programme brand; one applied write-up per deployment; methods in flagship OR journals, clinical work in clinical journals; student-paper competitions [04 B.9].
**🔴 Checkpoint** (*correction*): *optimal* or *best* in a title only with certificates, else the abstract says which results lack them; after an error, narrow the claim (the prescriptive-analytics preprint, v1 → v3).
**Output**: abstract skeleton; venue plan.
```

**Full-text additions** (writing moves, 08 §7.4): field-contrast opening, the neighbouring field's plan of attack against this field's ad hoc state [S185 pp. 1–3; S051 p. 1]; programme abstract, practice → belief → figure → method [S081 p. 2; S010 p. 1; S093 p. 2]; looseness and conjectures printed beside the theorem [S016 pp. 7, 9; S032 pp. 7–8, 11, 16; S158 pp. 15, 17; S323 pp. 2, 13, 17–18]; a closing complexity map and numbered open problems [S185 pp. 49–51]; staged companion papers from one model, including a bounds paper and a policies paper [S098 pp. 2–3; S072 p. 2; S004 pp. 4, 16–17, 22; S019 pp. 1–2, 4–5; S234 p. 1; S305 p. 3]; claims narrowed from working paper to journal [S833 pp. 6, 9, 15–23; S186 pp. 2, 16–17; S261 pp. 7, 14, 20, 26]; an integration section mapping the model onto the owner's process [S076 pp. 22–23; S245 pp. 11–13]; claims graded by their evidence [S017 pp. 11–12].

**Moved at the tighten step** (T3.7, 2026-10-29). These SKILL.md lines are copied verbatim as they stood before the cut; SKILL.md now keeps a shorter form of each, and the card citations, pages, DOIs and quotes it dropped are kept here.

3. One programme brand; companion papers from one model (bounds, then policies) [S072 p. 2]; one applied write-up per deployment; methods in flagship OR journals, clinical work in clinical journals; student-paper competitions [04 B.9].

<a id="workflow-f"></a>
## Workflow F: After publication

**Before this synthesis** (verbatim):

```text
### Workflow F: After publication (practice only; nothing stated)
**Steps**:
1. Answer critique with a new paper in the critic's frame (→ Heuristic 2).
2. Course, book, company; retry stalled topics; return when tools change (→ Method 6, Heuristic 7, Method 2).
**🔴 Checkpoint** (*inferred*): a formulation-strength or reproducibility critique with no reply planned → release installable code and record the limit; his record is silent here [05 §7.3].
**Output**: follow-up, course and book plan.
```

**Full-text additions.** The reply in the critics' frame [S095 pp. 3, 10, 21, 23]; a dated proof-repair note that keeps the published statements [S747 p. 1]; an adoption post-mortem in print [S262 p. 12]; a usable tool released with the paper [S190 pp. 1, 4–5; S094 pp. 1, 10; S325 p. 11; S395 pp. 5, 9; S615 p. 22]; staged and revised publication of one model (cluster 21, 19 works).

**Increment books-2026-10-29** (2026-10-29; book material, framing and dating only, outside every say–do count; full account: [Book material](#books)). Step 1 adds public self-correction of a textbook: the errata sheet of *Introduction to Linear Optimization*, joint with Tsitsiklis, "Last updated on 7/5/2021", organised by printing (68 items in three lists; local fixes such as added hypotheses, signs and a missing figure; no wrong theorem reported) [B003 pp. 1–5]. The line before this increment (verbatim):

```text
1. Answer critique with a new paper in the critic's frame (→ Heuristic 2); repair a proof in a dated note [S747 p. 1].
```

<a id="workflow-g"></a>
## Workflow G: Supervision and group organisation

**Before this synthesis** (verbatim):

```text
### Workflow G: Supervision and group organisation
**Steps**:
1. Heuristic 8; theses assembled from joint papers [04 C.2].
2. Partners from year one; job-talk rehearsal; companies only after graduation.
**🔴 Checkpoint**: at capacity (his words, 2014; missed meetings, 2015) → a named second adviser per student [04 B.4].
**Output**: a supervision plan per student.

**Stages without evidence**: the no-evidence row of Research Task Routing (proofs: a co-adviser debugged them while he posed problems [04 C.3]).
```

**Full-text additions** (08 §9). Students carry programmes: van Ryzin [S016 p. 1], Niño-Mora [S051 p. 11], Teo [S214 p. 11], Popescu [S007 p. 1], Sim [S001 p. 1], Dunn [S096 pp. 5–6], Pauphilet and Cory-Wright [S183 pp. 4–5, 19], Ma [S351 pp. 5, 12, 29], Koulouras [S527 pp. 2–4]. Former students return as co-authors on later stages of a programme [S476 p. 1] (*fix round*: *co-senior* withdrawn; the byline after the first author is alphabetical and states no roles). Co-advised lines with Tsitsiklis [S072 pp. 1, 8, 10, 32–33; S237 pp. 1–3] and Odoni [S135 p. 1; S806 pp. 1–2]; the co-advising itself is documented in the DSpace advisor fields [04 A.2], the papers show the co-authored thesis lines. Supervision routines themselves cannot be seen in papers (note 04 stays the source).

**Claim audit 2026-10-29, round 1** (earlier wording, verbatim):

```text
2. Partners from year one; job-talk rehearsal; companies only after graduation; former students as co-authors on later stages of a programme [S476 p. 1].
```

SKILL.md packet, item k = 24: the card supports only the last item [S476 p. 1]. The first three now cite their sources in note 04: F.13 (partners from the first year), F.14 (job-talk rehearsal, stated in the oral history) and B.7 (companies only after graduation, a stated rule).

<a id="heuristic-1"></a>
## Heuristic 1: the problem a working heuristic solves exactly

**Before this synthesis** (verbatim):

```text
1. **If** a heuristic works well, **then** find the robust problem it solves exactly and extend it from there (robustness, not sparsity, behind the Lasso; DOI 10.1016/j.ejor.2017.03.051; DOI 10.1287/ijoo.2018.0001) [02 G2; metadata level].
```

**Full-text evidence** (26 works cite H1; cluster 6, 18 works; upgraded from metadata level, C14). DP form in 1998: the model under which practice's equal split is exactly optimal, shown non-optimal elsewhere, then extended [S009 pp. 4, 9–10, 43]: "We have shown that the common approach of breaking up a large trade into a number of smaller trades of equal size is optimal only in one very special case" [S009 p. 43]; regularization as robustification in the 2011 survey [S003 p. 37]; Lasso and SLOPE as robust problems [S225 pp. 5–6, 14–17]; iff conditions and two-sided bounds where the equivalence fails [S085 pp. 7–15, 18–22]; ℓ1 buys robustness, not sparsity [S725 p. 4]; a dual-norm lemma for SVMs, logistic regression and trees [S104 pp. 9–12]; Tan's sensitivity model as an exact DRO problem [S333 pp. 5–7]; ridge as robustness [S218 p. 7]; an averaged robust problem behind practice [S530 pp. 2, 9, 12–13]; numerical linear algebra [S458 pp. 3, 6–7]; adaptive coefficients [S623 pp. 2–4]; inverse variant, the problem Black–Litterman solves [S086 pp. 1, 3, 5–9]. The cards credit the Lasso equivalence to Xu–Caramanis–Mannor; his contribution is where it breaks [S085 pp. 7–15]: "As a result, when robustification and regularization do not coincide, they can induce structurally distinct solutions." [S085 p. 13]. Not promoted to a method: exclusivity partial. The pre-2011 adaptive-RO and robustness–regularization papers are metadata-level [S789; S466; S560; S462; S424].

**Moved at the tighten step** (T3.7, 2026-10-29). These SKILL.md lines are copied verbatim as they stood before the cut; SKILL.md now keeps a shorter form of each, and the card citations, pages, DOIs and quotes it dropped are kept here.

1. **If** a heuristic or a practice works well, **then** find the problem it solves exactly, print where the equivalence breaks, and extend from there: the equal split optimal under one model only [S009 pp. 4, 9–10, 43]; ℓ1 from robustification, and where not [S085 pp. 7–15] (DOI 10.1016/j.ejor.2017.03.051); robust classifiers (DOI 10.1287/ijoo.2018.0001). The Lasso equivalence is Xu–Caramanis–Mannor's (C14).

<a id="heuristic-2"></a>
## Heuristic 2: answer critics with a new paper

**Before this synthesis** (verbatim):

```text
2. **If** critics attack, **then** answer with a new paper: a new student, the critic's evaluation frame, a fix (an ℓ2 term), a reframed target, released code, a partial concession (DOI 10.1214/19-STS701 after HTT) [03 B5.3]. No reply was found to formulation-strength or reproducibility critiques.
```

**Full-text evidence.** The reply to the best-subset critique adopts the critics' SNR grid and formula, concedes in part and releases code [S095 pp. 3, 10, 21, 23]: "Our experiments suggest that their observations are still valid but less obvious as soon as the best subset selection estimator is regularized as well" [S095 p. 23]; a 2017 journal version adds the handicap test absent from 2014 [S197 p. 12].

**Moved at the tighten step** (T3.7, 2026-10-29). These SKILL.md lines are copied verbatim as they stood before the cut; SKILL.md now keeps a shorter form of each, and the card citations, pages, DOIs and quotes it dropped are kept here.

2. **If** critics attack, **then** answer with a new paper: a new student, the critic's frame (their SNR grid, a partial concession, released code [S095 pp. 3, 10, 21, 23]), a fix (an ℓ2 term), a reframed target (DOI 10.1214/19-STS701 after HTT) [03 B5.3]. No reply was found to formulation-strength or reproducibility critiques.

<a id="heuristic-3"></a>
## Heuristic 3: an exact model stalls

**Before this synthesis** (verbatim):

```text
3. **If** an exact model stalls, **then** count variables, switch to local search with restarts over the structural variables, keep MIO for small instances and certification, and change the claim (Dunn 2018; DOI 10.1287/ijoc.1110.0496) [03 B4.5].
```

**Full-text evidence** (24 works, version pairs merged; cluster 24, 38 works; 08 §3 row 31). MIO kept as the move of a local search, not abandoned: a local backbone [S046 pp. 22–26] and random subsets of schools [S137 p. 4]: "The core idea of a “backbone” is that some decision variables do not vary too much across almost all near-optimal solutions, and that identifying them can significantly accelerate the optimization process." [S046 p. 39]. Exact optima on small instances certify the heuristic [S199 pp. 6, 8, 11, 13–15; S366 pp. 5–6, 8–12; S558 pp. 15–16; S867 pp. 18, 21–22]. When the bound stalls, relaxation plus rounding that still prints a bound gap [S183 pp. 22–26]. An intractability verdict by size count, once without re-measurement [S456 pp. 4, 6, 15]. Stated: "However, in many cases a provably optimal solution is not necessary and scalable heuristics such as local improvement may be employed." [S199 p. 11].

**Moved at the tighten step** (T3.7, 2026-10-29). These SKILL.md lines are copied verbatim as they stood before the cut; SKILL.md now keeps a shorter form of each, and the card citations, pages, DOIs and quotes it dropped are kept here.

3. **If** an exact model stalls, **then** count variables, switch to local search with restarts over the structural variables, keep MIO as the neighbourhood move [S046 pp. 22–26; S137 p. 4], use small exact solves to certify the heuristic [S199 pp. 6, 8, 11, 13–15], and change the claim (Dunn 2018; DOI 10.1287/ijoc.1110.0496) [03 B4.5].

<a id="heuristic-4"></a>
## Heuristic 4: print negative results in the body

**Before this synthesis** (verbatim):

```text
4. **If** a result is negative, **then** print it in the body (PILOT4; 6.14 h; uncertified trees; memory limits), archive failed variants with labels, and submit forecasts to an external prospective scoreboard (DELPHI) [03 B5.1, B4.7].
```

**Full-text evidence** (51 works; the strongest-recurring heuristic in the cards). Losing regimes printed [S010 pp. 30, 38–40]; few uncertain coefficients explain PILOT4 [S001 p. 14]: "We attribute this to the fact that there are very few uncertain coefficients in each constraint (Table 4), and thus probabilistic protection is quite close to deterministic protection." [S001 p. 14]; a regime map recommending greedy where it is near-optimal [S046 p. 19]; his own tree losing to logistic regression said plainly [S276 p. 4; S296 pp. 5, 9]; non-implementation printed [S083 pp. 25, 27; S262 p. 12; S243 pp. 17–28]; his own model the weakest predictor [S370 pp. 13–16]; a slower run time printed [S006 pp. 5, 9]; "Therefore, the full plan was not implemented and instead FEMA has opened just 24 facilities in 13 states, as compared to the original 100 planned ones." [S083 p. 25].

**Moved at the tighten step** (T3.7, 2026-10-29). These SKILL.md lines are copied verbatim as they stood before the cut; SKILL.md now keeps a shorter form of each, and the card citations, pages, DOIs and quotes it dropped are kept here.

4. **If** a result is negative, **then** print it in the body (losing regimes [S010 pp. 30, 38–40]; PILOT4; 6.14 h; uncertified trees; greedy where optimization does not pay [S046 p. 19]; a plan not implemented [S262 p. 12]), archive failed variants with labels, and submit forecasts to an external prospective scoreboard (DELPHI) [03 B5.1, B4.7].

<a id="heuristic-5"></a>
## Heuristic 5: learn the optimizer's strategy offline

**Before this synthesis** (verbatim):

```text
5. **If** one optimization is solved repeatedly online, **then** learn the optimizer's strategy offline and narrow the claims as the paper matures (DOI 10.1007/s10994-020-05893-5; DOI 10.1287/ijoc.2022.1181; DOI 10.1287/opre.2021.0707) [03 B5.4].
```

**Full-text evidence** (8 works; cluster 26, 32 works). Strategy labels and an interpretable model of the optimizer [S112 pp. 1–2, 9–10, 14, 17–21]: "Instead, our approach encodes the optimal solution with a small amount of information that we denote as strategy." [S112 p. 2]; online MIO in milliseconds [S092 pp. 2–3, 8, 12–13, 20–23]; robot planning [S204 pp. 2–3, 5–8]; fluid restless bandits [S681 pp. 3, 5, 14, 24]; a structure theorem first [S402 pp. 9–11]; a 1995 precursor, policies learned from exactly solved special cases [S098 p. 22]; math programming inside DP [S070 pp. 3–5; S034 pp. 8–9; S106 pp. 7–9]. Claims narrowed: "Therefore, the current approach does not apply to problems that take hours to solve with Gurobi." [S092 p. 36].
**Correction** (C13): the earlier citation DOI 10.1287/opre.2021.0707 is [S097], which learns constraints from decision–outcome data, not an optimizer's strategy for repeated solves [S097 pp. 1–9]; it moves to Method 5 and the DA row. Replacements: [S204] (DOI 10.1109/cdc42340.2020.9304043) and [S681] (DOI 10.1007/s10994-026-07022-0).

**Moved at the tighten step** (T3.7, 2026-10-29). These SKILL.md lines are copied verbatim as they stood before the cut; SKILL.md now keeps a shorter form of each, and the card citations, pages, DOIs and quotes it dropped are kept here.

5. **If** one optimization is solved repeatedly online, **then** learn the optimizer's strategy offline and narrow the claims as the paper matures [S112 pp. 1–2, 9–10, 14; S204 pp. 2–3, 5–8] (DOI 10.1007/s10994-020-05893-5; DOI 10.1287/ijoc.2022.1181) [03 B5.4]; not DOI 10.1287/opre.2021.0707, which learns constraints (C13).

<a id="heuristic-6"></a>
## Heuristic 6: build the data asset

**Before this synthesis** (verbatim):

```text
6. **If** a field lacks the data to decide, **then** build the data asset and split prediction from selection (a 2008 clinical-trial database built with about 20 undergraduates → DOI 10.1287/mnsc.2015.2363) [02 P8].
```

**Full-text evidence** (8 works). The chemotherapy-trial database built by hand: "such a database did not exist before this study" [S078 p. 3] (DOI 10.1287/mnsc.2015.2363 is [S078]); a trial database kept up 2012–2019 with former graduate students and undergraduates [S292 pp. 2, 9] (its tie to the S078 database is inferred; the paper does not state it); patients rated by experts first [S489 pp. 2–3, 7]; registry automation [S364 pp. 1, 3–4]; HAIM data released on PhysioNet [S023 pp. 1, 6, 8–9]; transcribed cohort studies [S099 pp. 2–3, 7, 9]; consortium and linked registry data [S527 pp. 2–4, 10, 19–20; S682 pp. 2–7].

**Moved at the tighten step** (T3.7, 2026-10-29). These SKILL.md lines are copied verbatim as they stood before the cut; SKILL.md now keeps a shorter form of each, and the card citations, pages, DOIs and quotes it dropped are kept here.

6. **If** a field lacks the data to decide, **then** build the data asset and split prediction from selection (a trial database that "did not exist before this study" [S078 p. 3] → DOI 10.1287/mnsc.2015.2363; a trial database kept up 2012–2019, [inferred] the same line [S292 pp. 2, 9]) [02 P8].

<a id="heuristic-7"></a>
## Heuristic 7: retry a stalled topic with the next student

**Before this synthesis** (verbatim):

```text
7. **If** a topic stalls, **then** retry it with the next student and keep the manuscript listed [03 C.1]; of 40 items listed as submitted in 2017, 21 were published by 2025 and 10 are absent, some retitled [01 §3].
```

**Full-text evidence** (5 works). A new student starts from the predecessor thesis's stated limit [S456 pp. 1, 3–4, 6]; 19 works enter from the group's own earlier limit (cluster 20) [S068 pp. 2, 5–6; S192 pp. 5–6; S440 pp. 1–2; S457 pp. 2–3].

**Moved at the tighten step** (T3.7, 2026-10-29). These SKILL.md lines are copied verbatim as they stood before the cut; SKILL.md now keeps a shorter form of each, and the card citations, pages, DOIs and quotes it dropped are kept here.

7. **If** a topic stalls, **then** retry it with the next student, from the predecessor's stated limit [S456 pp. 1, 3–4, 6], and keep the manuscript listed [03 C.1]; of 40 items listed as submitted in 2017, 21 were published by 2025 and 10 are absent, some retitled [01 §3].

<a id="heuristic-8"></a>
## Heuristic 8: supervising many students

**Before this synthesis** (verbatim):

```text
8. **If** you supervise many students, **then** a weekly hour one-on-one each, no whole-group meeting, a funded topic beside the thesis topic, an informal second adviser, companies only after graduation [02 P7, O10; 04 B.4, B.5]; counterpoint: missed meetings in 2015.
```

**Full-text evidence.** None: supervision routines cannot be seen in papers; contribution statements show the later sponsor-and-editor role [S617 arXiv p. 28; S023 p. 9] (08 §9). Unchanged.

**Moved at the tighten step** (T3.7, 2026-10-29). These SKILL.md lines are copied verbatim as they stood before the cut; SKILL.md now keeps a shorter form of each, and the card citations, pages, DOIs and quotes it dropped are kept here.

8. **If** you supervise many students, **then** a weekly hour one-on-one each, no whole-group meeting, a funded topic beside the thesis topic, an informal second adviser, companies only after graduation [02 P7, O10; 04 B.4, B.5]; counterpoint: missed meetings in 2015.

<a id="heuristic-9"></a>
## Heuristic 9: the abstract template

**Before this synthesis** (verbatim):

```text
9. **If** you write the abstract, **then** open with the community's belief, the enabling change and one headline number; reuse one programme brand for a decade (*under a modern optimization lens*) [02 W8, W9]; critics aimed at the headline numbers [05].
```

**Full-text evidence** (7 works). Practice → belief → figure → method [S081 p. 2]; belief and figure in the first sentences [S010 p. 1; S011 pp. 3, 5–6]; a week to ten minutes [S093 p. 2]: "We show that this problem, which required a week of computation time to solve in prior work, is solved by our approach to full optimality in approximately 10 minutes." [S093 p. 2]. The caveat sits in the body: hardware and solver progress conceded on p. 20 [S093 pp. 2, 20].

**Moved at the tighten step** (T3.7, 2026-10-29). These SKILL.md lines are copied verbatim as they stood before the cut; SKILL.md now keeps a shorter form of each, and the card citations, pages, DOIs and quotes it dropped are kept here.

9. **If** you write the abstract, **then** open with the community's belief, the enabling change and one headline number [S081 p. 2; S010 p. 1; S093 p. 2]; reuse one programme brand for a decade (*under a modern optimization lens*) [02 W8, W9]; critics aimed at the headline numbers [05].

<a id="heuristic-10"></a>
## Heuristic 10: re-derive the classical results with the new device (new)

**Before this synthesis**: not in SKILL.md. Readers proposed "re-derive classical theorems with the new device" repeatedly (S156, S121, S007, S072, S057 among others).

**Evidence (80 works, 1988–2026, all periods; cluster 5 of 08 §6).** Queueing results that classical methods treat case by case recovered as special cases of one closed form [S239 pp. 2, 8–12; S168 pp. 2, 10–11; S389 pp. 3–8; S663 pp. 3–4, 11–15]; Little's law, Burke's theorem and Pollaczek–Khinchine recovered from distributional laws [S129 pp. 1–2, 9–12; S336 pp. 1–3, 18–19]; the cμ rule, Smith's rule, Klimov's algorithm and Gittins indices as one adaptive greedy algorithm on one polytope [S057 pp. 3–4, 22, 38, 42, 46–47]; classical conservation laws recovered from potential functions [S072 pp. 10, 22–26]; integrality of classical polyhedra and max-flow min-cut by one rounding argument [S121 pp. 2–7; S214 pp. 5–11]; Markov and Chebyshev bounds generalized and the 0.878 max-cut bound re-proved [S007 pp. 23–25, 31–35]; Kingman's and Daley's bounds as special cases [S255 pp. 1, 7–9]; Riccati at radius zero [S118 p. 6]; the classical fluid model at Γ = 0 and an alternative proof of the cμ rule [S244 pp. 9–10]; the S-lemma and Bertsimas–Sim recovered before tighter levels [S283 pp. 3–4, 15–19]; ν-SVM as a relaxation of the exact model [S360 pp. 12, 15, 18]; constrained Lasso weaker than the root relaxation [S010 pp. 9–10]; regress-and-compare as a depth-1 tree [S096 pp. 3–4, 7]; SAA as one member of the weighted family [S193 pp. 6, 29–31; S163 p. 7]; basis pursuit denoising as the perspective relaxation [S290 pp. 10–14]; his own earlier relaxation placed in a new hierarchy and beaten [S216 pp. 5, 14, 18–19]; the method shown to tie where it should [S688 p. 12; S415 pp. 19–20; S681 pp. 17–20].

**Stated.** Unification named as the aim [S663 p. 3]: "Our results are structural for the case of arbitrary distributions and aim to unify the field, but they can potentially lead to an algorithmic solution for queues with distributions in the class R." [S663 p. 3]; "For the most part, our results were known in the literature. What is new is the unifying way of deriving them and providing new insights about them based on distributional laws." [S129 p. 2]; "We show that the classical Kingman’s and Daley’s bounds for the expected waiting time in a GI/GI/1 queue are special cases of the proposed approach." [S255 p. 1]; "Optimization not only offers a natural way to formulate and study such problems, it leads to unexpected improvements of classical results." [S007 p. 35].

**Steps.** (1) List the classical results and tools the field relies on; (2) derive each as a special case, a limit of your knob, or a relaxation of your formulation; (3) state the condition where the equivalence breaks [S085 pp. 7–15]; (4) place your own earlier method in the new order [S216 pp. 5, 14]; (5) only then extend.

**Checks.** Recurrence ✅; say–do ✅ (stated jointly); executable ✅; exclusivity ✗ (generalizing known results is routine in mathematics). Hence a heuristic, not a method; it fills the tenth and last heuristic slot, which is why three more heuristic-eligible clusters were folded into Methods 3 and 5 (08 §5).

**Moved at the tighten step** (T3.7, 2026-10-29). These SKILL.md lines are copied verbatim as they stood before the cut; SKILL.md now keeps a shorter form of each, and the card citations, pages, DOIs and quotes it dropped are kept here.

10. **If** you introduce a new device, **then** first re-derive the field's classical results with it (special cases, limits of the knob, relaxations), print where the equivalence breaks, place your own earlier method in the new order, then extend [S129 pp. 1–2, 9–12; S057 pp. 3–4, 22, 38; S283 pp. 3–4, 15–19]. Not a method: exclusivity fails (80 works).

<a id="anatomy-achievable-region"></a>
## Signature work: achievable region (SW1)

**Before this synthesis** (verbatim):

```text
### SW1 · Achievable region, 1993–2000 (MOR 1996, DOI 10.1287/moor.21.2.257; Queueing Syst. 1995, DOI 10.1007/BF01149167) · Method 1 {SD LO IO}
| Dimension | Content |
|---|---|
| Origin | [stated] stochastic control as mathematical programs, crediting earlier polyhedral views (QS 1995 pp. 337–340); personal origin unknown |
| Why then | Framed as the stochastic counterpart of sharper formulations (p. 337); an NSF PYI |
| Key insight | Optimize over achievable performance vectors; on extended polymatroids greedy is optimal, and Gittins indices are dual variables |
| Minimal evidence | Indexable systems characterized exactly; network bounds tight in some regimes |
| Abandoned paths | Policies from relaxations ad hoc; none for networks (p. 385) |
| Reception | Erlang and SIAM prizes 1996 (citations unverified); revisited by ML in 2026 |
```

**Full-text evidence.** Read in full: the 1995 survey [S185], the 1994 working paper [S580], the 1996 conservation-law paper [S057], the 1994 network paper [S072] (not read in the web pass: a scan without a text layer), the 2000 restless-bandit paper [S051], loss networks [S368], changeover times [S212], H010. Origin stated, sole author: "This approach is based on the thesis that the essential difficulty in stochastic and dynamic optimization is primarily the dynamic and combinatorial character of the problem and only secondarily the stochastic character of the problem." [S580 p. 10]; the field contrast [S185 pp. 1–3]; "For the most part, the tradition for stochastic and dynamic scheduling problems has been, however, quite different, as it relies primarily on dynamic programming formulations." [S057 p. 1]; "Faced with these results, one asks what is the underlying reason that these nontrivial problems have very efficient solutions, both in theory and in practice." [S057 p. 3]. Key insight [S057 pp. 3, 11–13, 19–20]; minimal evidence [S057 pp. 3–4, 22, 38; S072 pp. 20–22]; the abandoned path, in his words: "For restless bandits, polling systems and loss networks we proposed empirically effective heuristics from the relaxations, but the heuristics were somewhat ad hoc." [S185 p. 49]; lineage and funding [S057 pp. 1, 4, 12, 14, 32, 48–49]; reception through the primal–dual heuristic [S051 pp. 7–11] and the 2026 ML return [S681 pp. 1, 3, 8].

**Moved at the tighten step** (T3.7, 2026-10-29). These SKILL.md lines are copied verbatim as they stood before the cut; SKILL.md now keeps a shorter form of each, and the card citations, pages, DOIs and quotes it dropped are kept here.

| Dimension | Content |
|---|---|
| Why then | The stochastic counterpart of sharper polyhedral and SDP formulations [S185 pp. 1–4]; a student's thesis line with Tsitsiklis as co-author [S072 pp. 1, 8, 33], co-advised per DSpace [04 A.2]; an NSF PYI |
| Minimal evidence | Classical index rules recovered as one algorithm on one polytope [S057 pp. 3–4, 22, 38]; polyhedral and SDP bounds for networks [S072 pp. 20–22] |
| Reception | Erlang and SIAM prizes 1996 (citations unverified); an index policy with a suboptimality bound [S051 pp. 7–11]; revisited by ML in 2026 [S681 pp. 1, 3, 8] |

<a id="anatomy-moment-bounds"></a>
## Signature work: optimal probability inequalities (SW2)

**Before this synthesis** (verbatim):

```text
### SW2 · Optimal probability inequalities, 1998–2005 (SIOPT 2005, DOI 10.1137/S1052623401399903) · Method 1 {CP SD AP}
| Dimension | Content |
|---|---|
| Origin | [stated-joint] are the Markov, Chebyshev and Chernoff bounds best possible, and is there an optimization-based theory (p. 780)? |
| Why then | [inferred] SDP had become a standard solvable class |
| Key insight | A tight moment bound is a convex, often semidefinite, program; its dual gives the worst-case distribution |
| Minimal evidence | The univariate SDP characterization; NP-hardness for k ≥ 4 on Rⁿ marks the boundary |
| Abandoned paths | Stated limits only |
| Reception | No critique found; no stated CP methodology outside such introductions |
```

**Full-text evidence.** Read in full: SIOPT 2005 [S018] and the 2000 handbook chapter [S007]. Origin: three numbered questions and critics' quotations define the gap [S018 pp. 1–4]; key insight [S018 pp. 5–16]; boundary [S018 pp. 16–17]; stated limit: "It is fair to say that a thorough understanding of the algorithmic aspects and the complexity of the (n, k, Ω)-bound problem is still lacking." [S018 p. 4]; no procedure to extract an extremal distribution from the SDP [S018 pp. 19–21]. The CP line takes its questions from inside theory, with no owner or data [S018 pp. 1, 3, 25]. Reception and extensions: SDP relaxations certify heuristic policies [S007 p. 18]; covariance rounding of an SDP solution [S007 pp. 33–35]; Kingman's and Daley's bounds as special cases [S255 pp. 1, 7–9]; moment hierarchies with two-sided convergence [S413 pp. 4–5; S499 pp. 4, 14–15]; option and stock prices [S056 pp. 2–15].

**Moved at the tighten step** (T3.7, 2026-10-29). These SKILL.md lines are copied verbatim as they stood before the cut; SKILL.md now keeps a shorter form of each, and the card citations, pages, DOIs and quotes it dropped are kept here.

| Dimension | Content |
|---|---|
| Origin | [stated-joint] are the Markov, Chebyshev and Chernoff bounds best possible, and is there an optimization theory for them? The gap is taken from critics of moment theory [S018 pp. 1–4] |
| Reception | SDP relaxations as yardsticks for heuristic policies [S007 p. 18]; Kingman's and Daley's bounds as special cases [S255 pp. 1, 7–9]; no critique found |

<a id="anatomy-price-of-robustness"></a>
## Signature work: The Price of Robustness (SW3)

**Before this synthesis** (verbatim):

```text
### SW3 · The Price of Robustness, 2001–2004 (OR 2004, DOI 10.1287/opre.1030.0065; MP 2003, DOI 10.1007/s10107-003-0396-4) · Methods 3, 1, 6 {RO IO LO}
| Dimension | Content |
|---|---|
| Origin | [stated-joint] robust solutions too conservative (Soyster 1973); ellipsoidal counterparts unusable for discrete problems (pp. 35–36); how Γ arose: unknown |
| Why then | Ben-Tal–Nemirovski (DOI 10.1287/moor.23.4.769) and El Ghaoui–Lebret; CPLEX 6.0 solved a 200-item robust knapsack |
| Key insight | At most Γ deviating coefficients per constraint; the counterpart stays linear or mixed-integer, with solution-independent violation bounds |
| Minimal evidence | The knapsack point (0.57% bound for 1.54% cost) |
| Abandoned paths | PILOT4; an unpublished ellipsoidal discrete manuscript; data-free sets replaced by data-driven ones (2018) |
| Reception | His most cited work; refined by Poss and Iancu–Trichakis; 2022 book; 2026 retrospective (not read) |
```

**Full-text evidence.** Read in full: OR 2004 [S001] and MP 2003 [S004]; the 2002 credit-risk working paper read in part [S653]. Origin [S001 pp. 1–3]; a budget Γ normalised by standard deviations in 2002 [S653 pp. 12–14, 24]; the knapsack point, CPLEX 6.0 on a Pentium II, 0.57% bound for 1.54% loss [S001 pp. 10, 12]; PILOT4 diagnosed [S001 pp. 14, 16]; "Moreover, we think that the ultimate criterion for comparing the degree of conservatism of these methods will be computation in real problems." [S001 p. 8]; robust 0-1 problems by n + 1 nominal solves, robust flows by a logarithmic number of nominal flows [S004 pp. 5–7, 22]: "We next show that surprisingly, the robust counterpart of a polynomially solvable combinatorial optimization problem is also polynomially solvable." [S004 p. 7]. Later lines: data-driven sets [S013 pp. 3–4, 10]; theory and applications survey [S003 p. 37]; the 2026 retrospective abstract-level [S614].

**Moved at the tighten step** (T3.7, 2026-10-29). These SKILL.md lines are copied verbatim as they stood before the cut; SKILL.md now keeps a shorter form of each, and the card citations, pages, DOIs and quotes it dropped are kept here.

| Dimension | Content |
|---|---|
| Origin | [stated-joint] Soyster too conservative; ellipsoidal counterparts nonlinear and unattractive for discrete problems [S001 pp. 1–3]; a budget Γ already in a 2002 working paper [S653 pp. 12–14]; how Γ arose: unknown |
| Abandoned paths | PILOT4, where the price stays high [S001 pp. 14, 16]; an unpublished ellipsoidal discrete manuscript; data-driven sets later [S013 pp. 3–4, 10] |

**Claim audit 2026-10-29, round 1** (earlier wording, verbatim):

```text
| Key insight | At most Γ deviating coefficients per constraint; the counterpart stays linear or mixed-integer [S001 pp. 3–4]; robust 0–1 problems keep the nominal complexity [S004 pp. 5–7, 22] |
```

SKILL.md packet, item k = 27: the robust MIP staying a MIP is on p. 10 of the card, not pp. 3–4 [S001 p. 10]; the page is added.

<a id="anatomy-best-subset-trees"></a>
## Signature work: best subset selection and optimal trees (SW4)

**Before this synthesis** (verbatim):

```text
### SW4 · Best subset selection and optimal trees, 2014–2017 (AoS 2016, DOI 10.1214/15-AOS1388; Mach. Learn. 2017, DOI 10.1007/s10994-017-5633-9) · Methods 2, 4, 6 {ML IO HS}
| Dimension | Content |
|---|---|
| Origin | [stated] statistics' belief that integer optimization is intractable; [practice] CRIO submitted 2002; a student line (Shioda, King, Dunn) with postdoc Mazumder |
| Why then | The rebuilt speed-up (about 450 billion in the published AoS version) |
| Key insight | Exact estimator; good solutions by a discrete first-order method or CART; the warm-started MIO proves optimality or reports a gap |
| Minimal evidence | Certified optima in minutes for n in the thousands, p in the hundreds; 1–2% (axis-aligned) and 3–5% (hyperplane) average gains over CART on 53 UCI sets |
| Abandoned paths | Certificates take hours for p in the thousands; by 2018 the tree MIO gave way to local search |
| Reception | HTT (DOI 10.1214/19-STS733) and the 2020 exchange [05 §1–2]; lecture, class, company, book (2019), Lanchester Prize 2021 |
```

**Full-text evidence.** Read in full: best subset (arXiv v1, with the 200-billion figure) [S010], OCT [S011], the OR Forum regression paper [S081], CRIO [S073], logistic regression [S105], the BPV reply [S095]. Origin: "the belief was formed in the early 1970s that these methods are not tractable in practical computational settings." [S073 p. 1]; the figure [S010 pp. 7–8; S081 p. 4; S011 pp. 5–6]; key insight [S010 pp. 1, 5–6, 18–20; S011 pp. 9–19]; limits printed: hours to certify for p ≫ n [S010 p. 6], slow lower bounds [S010 p. 34], losing regimes [S010 pp. 38–40]; certificates: "most of our results for OCT and OCT-H do not carry explicit certificates" [S011 p. 26]; the evaluation stance: "is not necessarily required in practice when evaluating a classifier" [S011 p. 14]; CART baseline at matched depth and the depth-4 comparison [S011 pp. 26–36]; the reply in the critics' frame [S095 pp. 3, 10, 21, 23].

**Moved at the tighten step** (T3.7, 2026-10-29). These SKILL.md lines are copied verbatim as they stood before the cut; SKILL.md now keeps a shorter form of each, and the card citations, pages, DOIs and quotes it dropped are kept here.

| Dimension | Content |
|---|---|
| Origin | [stated-joint] statistics' belief that MIO is impractical, dated and conceded [S010 pp. 2, 5, 8], stated already in CRIO [S073 p. 1]; a student line (Shioda, King, Dunn) with postdoc Mazumder |
| Why then | The rebuilt speed-up (Method 2): 200 billion in arXiv v1, about 450 billion in print (AoS p. 819), 800 billion for trees [S010 pp. 7–8; S081 p. 4; S011 pp. 5–6] |
| Abandoned paths | Slow lower bounds for p ≫ n and losing regimes printed [S010 pp. 34, 38–40]; "most of our results for OCT and OCT-H do not carry explicit certificates" [S011 p. 26]; by 2018 local search for trees |
| Reception | HTT (DOI 10.1214/19-STS733) and the 2020 exchange, answered in the critics' frame [S095 pp. 3, 10, 21, 23]; lecture, class, company, book (2019), Lanchester Prize 2021 |

**Claim audit 2026-10-29, round 1** (earlier wording, verbatim):

```text
| Key insight | Exact estimator; good solutions by a discrete first-order method or CART; the warm-started MIO proves optimality or reports a gap [S010 pp. 1, 5–6, 18–20] |
```

SKILL.md packet, item k = 29: CART is the warm start of the trees paper [S011 pp. 14–15], not in S010; the citation is split by clause (estimator and first-order method [S010 pp. 5, 18–20]; certificate or gap [S010 pp. 1, 6]).

<a id="anatomy-prescriptive-analytics"></a>
## Signature work: From Predictive to Prescriptive Analytics (SW5)

**Before this synthesis** (verbatim):

```text
### SW5 · From Predictive to Prescriptive Analytics, 2014–2020 (Manag. Sci. 2020, DOI 10.1287/mnsc.2018.3253; arXiv 1402.5481) · Method 5 {DA ML AP}
| Dimension | Content |
|---|---|
| Origin | [stated-joint] decisions from data that are mostly auxiliary covariates. arXiv v1–v2 were Kallus's single-author preprint, v2 withdrawn by Kallus (an error in Theorem 2.2); Bertsimas joined at v3: not his retraction |
| Why then | Data availability and flexible ML; plenaries in 2015–2016 |
| Key insight | Conditional stochastic optimization with ML weights, asymptotically optimal under mild conditions; P as R² for decisions |
| Minimal evidence | A media firm's distribution data with scraped covariates; P = 88% |
| Abandoned paths | v1's universal claim narrowed; a real case, censoring and P added |
| Reception | Six years from v1 to print; bootstrap-robust follow-up (2022); optimism in high dimension noted by his group and a survey (DOI 10.1016/j.ejor.2024.03.020) |
```

**Full-text evidence.** Read in full (arXiv version) [S008]. Problem entry [S008 pp. 1–2, 6–7]; key idea [S008 pp. 3, 10–14, 16, 21]; the real case, 150 weeks over just under 20,000 locations, P = 0.88 [S008 pp. 28–31]; the stated priority of the decision over the prediction [S008 p. 29]; the stated gap: "Although we do not have firm theoretical results on the asymptotic optimality of the predictive prescriptions based on CART (eq. (7)) and RF (eq. (8)), we have observed them to converge empirically in Section 1.1." [S008 p. 19]; the baseline is a constructed data-poor rule, not the vendor's rule [S008 pp. 30–31]. Follow-up: the bootstrap-robust layer [S139 pp. 3–4, 15–16].

**Moved at the tighten step** (T3.7, 2026-10-29). These SKILL.md lines are copied verbatim as they stood before the cut; SKILL.md now keeps a shorter form of each, and the card citations, pages, DOIs and quotes it dropped are kept here.

| Dimension | Content |
|---|---|
| Origin | [stated-joint] OR/MS data are mostly auxiliary covariates, which SAA ignores [S008 pp. 1–2, 6–7]. arXiv v1–v2 were Kallus's single-author preprint, v2 withdrawn by Kallus; Bertsimas joined at v3: not his retraction |
| Why then | Data availability and flexible ML, stated without a figure [S008 p. 2]; plenaries in 2015–2016 |
| Abandoned paths | v1's universal claim narrowed; no asymptotic theory for CART and random forests, the methods used in the application [S008 p. 19]; censoring and P added |
| Reception | Six years from v1 to print; a bootstrap-robust follow-up [S139 pp. 3–4, 15–16] after optimism in high dimension, noted also by a survey (DOI 10.1016/j.ejor.2024.03.020) |

<a id="anatomy-dynamic-routing"></a>
## Signature work: stochastic and dynamic vehicle routing (SW6, new)

**Before this synthesis**: not dissected in SKILL.md (01 §2 lists it among the routing works).

**Full-text evidence.** Read in full: OR 1991 [S016], OR 1993 [S032], the 1990 working paper [S597], Adv. Appl. Probab. 1993 [S091]. Origin: "Yet, in many practical applications, the TSP is a deterministic, static approximation to a problem which is, in reality, both probabilistic and time varying (dynamic)." [S016 p. 1]; the problem came from a colleague, Psaraftis (acknowledgment) [S016 p. 14]. Key insight: "First, we establish some lower bounds on the average system time for all policies." [S016 p. 3]; batching into TSP tours as a GI/G/1 queue [S016 p. 10]. Minimal evidence: light-traffic optimality and heavy-traffic constant factors [S016 pp. 5–11]; simulated constants with a stated stopping rule [S016 p. 12]. Abandoned paths: loose constants and an unproved assumption printed [S016 pp. 7, 9, 11–12]; "Though useful for data-intensive tactical problems, they are inherently ad hoc and hence do not give the insight necessary for strategic planning." [S032 p. 2]; partition policies lack travel–waiting control [S597 p. 38]. Reception and extensions: m vehicles and capacity [S032 pp. 3–15]; general densities and renewal arrivals, with a factor-2 stronger bound [S091 pp. 3, 11]; the travel–waiting price [S032 pp. 15–16]; the price of an equal-service policy [S091 pp. 11, 23–25]. Methods: 7 (bound before policy), 1 (an analysable queue reached by policy design), 3 (a priced trade-off).

**Moved at the tighten step** (T3.7, 2026-10-29). These SKILL.md lines are copied verbatim as they stood before the cut; SKILL.md now keeps a shorter form of each, and the card citations, pages, DOIs and quotes it dropped are kept here.

| Dimension | Content |
|---|---|
| Origin | [stated-joint] the TSP is a deterministic, static approximation of problems that are stochastic, dynamic and judged by waiting [S016 pp. 1–2]; a colleague (Psaraftis) brought the problem to him [S016 p. 14] |
| Why then | Probabilistic analysis of Euclidean problems joined to queueing [S016 pp. 3–4, 10–11]; [inferred] the next step after a priori optimization |

<a id="anatomy-execution-costs"></a>
## Signature work: optimal control of execution costs (ledger only)

**Before this synthesis**: not dissected (cited in the trajectory table as DOI 10.1016/S1386-4181(97)00012-8).

**Full-text evidence** (read in full [S009]; kept here to save SKILL.md words). Origin: the law requires best execution while no clear definition exists [S009 pp. 2–3]: "In this paper, we provide one clear definition of best execution, based on the minimization of the expected cost of execution using stochastic dynamic programming." [S009 p. 3]. Key insight: a stochastic dynamic program with the trade's own impact in the law of motion; closed-form linear policies and quadratic value functions [S009 pp. 3–12]. Minimal evidence: the practitioners' equal split is optimal only under linear permanent impact and an arithmetic random walk [S009 pp. 9–10, 43]; simulated savings against that rule in cents per share [S009 pp. 13–25]. Abandoned paths: the first dynamics are flagged as implausible and replaced by the LPT law, whose impact is temporary [S009 pp. 17, 20–22] (C18); real-data tests deferred [S009 pp. 38–42]. Reception: among his most cited works on the Scholar list; the value function offered to dealers as a pricing benchmark [S009 pp. 3–4]. Methods: 5 (the practitioners' rule as baseline), 1 (specifications chosen to stay linear-quadratic), Heuristic 1 (the model under which practice is exactly optimal).

<a id="anti-patterns"></a>
## Research anti-patterns

**Before this synthesis** (verbatim):

```text
## Research Anti-patterns

| Anti-pattern | Why he opposes it (source) | Do instead |
|---|---|---|
| Research chosen to impress, or that changes nothing if it succeeds | His own early error, corrected about 1997–98 (oral history p. 14); homepage essay [02 T1, T3] | Impact gate (Method 6) |
| One-split-at-a-time trees; regression as an art | 2016–2017 abstracts [02 G1] | One joint MIO (Method 4) |
| Randomization in small samples | DOI 10.1287/opre.2015.1361 [02 G2] | Optimize the assignment |
| Robust counterparts that turn nonlinear; over-conservative protection | OR 2004 pp. 35–36 [01 SW3] | Class-keeping budgets (Methods 1, 3) |
| Polynomial solvability as the test of usefulness; unexamined *intractable* beliefs | 2019 principle; seven occasions 2015–2019 [02 T4, R9] | Measured solve times (Method 2) |
| Methods-first teaching; numbers plugged into black boxes | 2004 and 2016 book pages [02 T9] | Problem and data first (Method 5) |
| Funding dictating thesis topics | Would make students less ambitious (oral history p. 7) [02 P7] | Funded topic beside the thesis (Heuristic 8) |
```

**Full-text evidence per row.** Trees and regression as an art: "Fitting regression models has long been viewed as an art" [S081 p. 3]; greedy induction and Breiman's own words [S011 pp. 4–6]. Randomization in small samples: [S124 pp. 2, 4–6]: "Indeed it does better because any manual manipulation of the optimized results would make the result less well matched than the reproducible optimum, which is verifiable, whereas no one grouping can ever be verified as the true result of pure randomization." [S124 p. 6]. Robust counterparts that turn nonlinear: [S001 pp. 1–3]. Polynomial solvability as the test: [S010 p. 2; S178 p. 5]: "Our view of computational tractability is not polynomial time solution times as these do not exist for the LQS problem unless P = NP." [S178 p. 5]. New row, heuristics judged only against heuristics: [S051 p. 1; S185 pp. 1–2; S183 p. 3]. The row on heuristics whose failures the user cannot see was merged into it to save words.

**Increment books-2026-10-29** (2026-10-29; book material, framing and dating only, outside every say–do count; full account: [Book material](#books)). The row on methods-first teaching now cites the two book pages behind it [B014 p. 1; B017 p. 1] (quoted under [Taste: warning signs](#taste-warnings)). The row before this increment (verbatim):

```text
| Methods-first teaching; numbers plugged into black boxes | 2004 and 2016 book pages [02 T9] | Problem and data first (Method 5) |
```

<a id="research-trajectory"></a>
## Research trajectory

**Before this synthesis** (verbatim):

```text
## Research Trajectory

| Period | Main direction | Reason for shift | Representative work |
|---|---|---|---|
| 1985–1995 | Probabilistic combinatorial optimization, routing, queueing, achievable region, LP-relaxation approximation {SD IO} | Inherited from Odoni's group [inferred]; NSF PYI; co-advising with Tsitsiklis | DOI 10.1287/opre.38.6.1019; DOI 10.1287/moor.21.2.257 |
| 1995–2001 | Moments and SDP {CP}; finance {AP}; LO textbook | Self-described turn about 1997–98 from impressing seniors to what he judged important | DOI 10.1137/S1052623401399903; DOI 10.1016/S1386-4181(97)00012-8 |
| 2001–2013 | Robust and adaptive optimization {RO}; health-care data {AP} | Entered RO after its founders, set apart by tractability; company claims data; 2009 family losses named as a trigger (practice started earlier) | DOI 10.1287/opre.1030.0065; DOI 10.1287/opre.1080.0619 |
| 2014–2019 | Statistics and ML under a modern optimization lens; prescriptive analytics {ML DA IO} | The measured MIO speed-up; Morse Lecture 2014 | DOI 10.1214/15-AOS1388; DOI 10.1287/mnsc.2018.3253 |
| 2019–2026 | Health care at scale, COVID-19, multimodal AI, LLMs, education {AP DA ML} | Roles (associate dean 2019, Vice Provost 2024), hospital partners, the pandemic | DOI 10.1007/s10729-020-09542-0; arXiv 2501.00568 |

### Latest
- **2025-10 → 2026-10** [06 §8]: *Fifty years of Robust Linear and Convex Optimization* with den Hertog (EJOR 2026, DOI 10.1016/j.ejor.2026.08.042, not read); *Cone Product Reformulation for Global Optimization* (IJOC 2026, DOI 10.1287/ijoc.2023.0345); fluid restless bandits by ML (DOI 10.1007/s10994-026-07022-0); Hartford HealthCare operations (DOI 10.1287/inte.2024.0170); preprints on lecture-video generation (arXiv 2609.26540), LLM personalization (arXiv 2610.17203) and wildfire sensing (arXiv 2609.11829).
- Roles: Vice Provost for Open Learning; Universal AI launched 2026-05-12; Killian Lecture 2026-03-19; PhD theses no. 107–109 in spring 2026. Direction [inferred]: health care dominant; RO continuing in energy and insurance; research following his education role.
```

**Full-text view** (08 §8). Works read in full or in part / all works with a card, by period, with domain tags (a work can carry several):

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

**Turns.**
1. *1988–1993, probabilistic combinatorial optimization and queueing analysis.* The thesis problem class comes from his adviser's group [S048 pp. 18, 71, 125]; a priori optimization [S038 pp. 1–2], dense distribution classes for multiserver queues [S239 pp. 1–2; S168 pp. 1–2], and dynamic routing with van Ryzin after a colleague raised the problem [S016 pp. 1, 14].
2. *1993–1995, from asymptotic constants to mathematical-programming relaxations of stochastic control.* The 1994 working paper names the dynamic and combinatorial character as the essential difficulty [S580 p. 10]; polyhedral and SDP relaxations of queueing networks [S072 pp. 2, 20–22]; the survey consolidates the cohort [S185 pp. 1–4].
3. *1995–2002, IO relaxations, rounding and moments.* Survivable networks [S052 p. 3]; randomized rounding read as probability [S121 pp. 3–9; S007 pp. 33–35]; moment bounds as SDPs [S007 pp. 9, 18; S056 pp. 2–15]; finance with Lo [S009 p. 3]; fluid scheduling [S130 pp. 2–3].
4. *2002–2007, budgeted robust optimization.* First Γ budget in a 2002 working paper [S653 pp. 12–14]; robust discrete optimization keeps the nominal complexity [S004 p. 22]; the price of robustness [S001 pp. 1, 3–5]; robust inventory [S014 pp. 1, 4–5].
5. *2008–2015, adaptive policies, data-driven sets and limit laws.* Power and limits of static and affine policies [S134 pp. 6, 12–18; S042 pp. 2–3]; sets from risk measures [S024 pp. 2–5]; limit-law sets [S065 pp. 5–10; S119 pp. 7–10]; fairness [S012 pp. 1, 14; S026 pp. 1–2].
6. *2014–2018, MIO for statistics and ML.* Tractability redefined by solve times [S178 pp. 3–5; S010 p. 2]; the why-now figure [S010 pp. 7–8; S081 p. 4; S011 pp. 5–6]; the prescriptive line [S008 pp. 10–12].
7. *2018–2022, clinical ML, COVID-19 and deployment at scale.* Clinical calculators with optimal trees [S190 pp. 1, 4–5; S231 pp. 3, 8]; DELPHI [S103 pp. 2–3]; HAIM [S023 pp. 1, 3]; hospital operations [S115 pp. 2, 19–24].
8. *2023–2026, multimodal AI, LLMs, global optimization and education.* xHAIM [S390 pp. 1–2]; LLM-assisted modelling [S330 pp. 1–4]; a group global-optimization solver line [S624 pp. 10–16; S415 pp. 19–20]; field roll-outs [S617 arXiv pp. 11–14]; teaching tools under the Open Learning role [S667 pp. 4–5, 7].

**What stayed constant.** Bound before policy (Method 7, 79 works); re-derive classical results before extending (Heuristic 10, 80 works); class-keeping formulation (Method 1, 210 works with evidence links); a priced trade-off handed to the decision-maker from 1990 [S597 pp. 36–38] to 2026 [S668 pp. 4–8, 11]; printed limits, conjectures and loose constants in 1988–1993 [S048 pp. 100–101, 164–165; S016 pp. 7, 9], negative results in the body later (Heuristic 4, 51 works); programmes carried by students and former students (Method 6, 194 works).

**What changed.** The meaning of *tractable* (complexity class and asymptotic constants in 1988–1997 [S289 pp. 2, 6, 11–12; S269 pp. 1, 21–22]; computation named the criterion in 2004 [S001 p. 8]; solve time stated as the test from 2014 [S178 p. 5; S010 p. 2]); scarce computation favouring simple a priori policies in 1996 [S025 p. 17] became abundant computation favouring exact MIO [S010 pp. 7–8]; sole authorship gave way to teams (11 sole-author works in 1988–92, about one a period later, editorials aside); theory papers gave way to deployments with partners. Computation was steady from the start, not little (C17): a home-made C package, 45 PTSP problems and 20 instances per VRP type against named heuristics in 1991 [S089 pp. 13–17, 23, 26–28]; programmed queueing algorithms with run times by step [S291 p. 13; S168 pp. 15–16; S389 pp. 11–14]: "Being fully aware of the need for the probabilist to be closely involved with the algorithmic analysis of a problem, we have undertaken the task of programming and testing our algorithms." [S168 p. 14]; an IP solved with MPSX [S036 pp. 7–10]; airport congestion runs on real data [S135 pp. 1–2, 7–8, 15–16].

**Moved at the tighten step** (T3.7, 2026-10-29). These SKILL.md lines are copied verbatim as they stood before the cut; SKILL.md now keeps a shorter form of each, and the card citations, pages, DOIs and quotes it dropped are kept here.

Constant: Method 7, Heuristic 10, Method 1, priced trade-offs [S597 pp. 36–38], printed limits. Changed: the meaning of *tractable*; sole authorship to teams; theory to deployments with partners [08 §8–9].

- **2025-10 → 2026-10** [06 §8]: *Fifty years of Robust Linear and Convex Optimization* with den Hertog (EJOR 2026, DOI 10.1016/j.ejor.2026.08.042, abstract only [S614]); *Cone Product Reformulation for Global Optimization* (IJOC 2026, DOI 10.1287/ijoc.2023.0345); fluid restless bandits by ML (DOI 10.1007/s10994-026-07022-0); Hartford HealthCare operations (DOI 10.1287/inte.2024.0170); preprints on lecture-video generation (arXiv 2609.26540), LLM personalization (arXiv 2610.17203) and wildfire sensing (arXiv 2609.11829).
- Roles: Vice Provost for Open Learning; Universal AI launched 2026-05-12; Killian Lecture 2026-03-19; PhD theses no. 107–109 in spring 2026. Direction [inferred]: health care dominant; RO continuing in energy and insurance; research following his education role.

<a id="academic-lineage"></a>
## Academic lineage

**Before this synthesis** (verbatim):

```text
## Academic Lineage

- **Upstream**: PhD MIT 1988 (applied mathematics and OR), advisers Amedeo Odoni (primary) and Daniel Kleitman; Tom Magnanti on the committee; the thesis problem class came from Odoni's group [06 §2.1].
- **Long collaborators**: John Tsitsiklis (queueing; LO textbook), Andrew Lo (finance), Robert Weismantel (IO book), Dick den Hertog (RO book), David Gamarnik (queueing book).
- **Downstream**: 109 completed PhDs and 20 current (homepage, 2026). Lineages: SD (Niño-Mora, Paschalidis, Gamarnik, Sethuraman); IO (Goemans, C.-P. Teo); CP (Popescu, Natarajan); RO (Sim, Thiele, Brown, Caramanis, Iancu, Gupta, Dunning); ML (Shioda, King, Dunn, Pauphilet, Cory-Wright); DA (Kallus, McCord, Sturt); health (O'Hair, Orfanoudaki, Wiberg, Ma) [04 A.4]. Alumni return as co-advisers, book co-authors and informal advisers [04 B.10].
- **Guest-team link**: one joint work with a guest member: Bertsimas & Ye, *Semidefinite relaxations, multivariate normal distributions, and order statistics* (Handbook of Combinatorial Optimization, 1998, DOI 10.1007/978-1-4613-0303-9_24).
```

**Full-text evidence.** The thesis documents the inheritance from Odoni's group [S048 pp. 18, 71, 125; S038 p. 5]. Most frequent coauthors by period (08 §9, from the cards' coauthor fields, approximate): 1988–92 van Ryzin, Nakazato, Papaconstantinou; 1993–97 Tsitsiklis, Odoni, C.-P. Teo; 1998–2002 C.-P. Teo, Tsitsiklis, Lo, Gamarnik; 2003–07 Natarajan, Caramanis, Sim; 2008–12 Nohadani, Farias, Trichakis; 2013–17 Mišić, Bandi, V. Gupta; 2018–22 Dunn, Orfanoudaki, Zhuo; 2023–26 Y. Ma, Margonis, den Hertog. The RO book co-author den Hertog co-signs the 2021–2026 robust and global-optimization lines [S215 pp. 21–23; S283 pp. 3–4, 15–19; S708 pp. 8, 14–15; S689 pp. 3, 16; S415 pp. 19–20; S836 pp. 4–5]. Partners as co-authors: ISO New England staff [S006 pp. 1, 5–9]; an owner co-author [S245 pp. 2–3, 6–7]; UNOS staff [S476 pp. 1–2]; hospital partners [S617 arXiv pp. 1–2, 9, 28, 31; S683 pp. 1, 7]. Company software as platform [S300 pp. 23–24; S308 pp. 2–3; H002 pp. 1–2, 8, 19; S677 pp. 1–3].

**Moved at the tighten step** (T3.7, 2026-10-29). These SKILL.md lines are copied verbatim as they stood before the cut; SKILL.md now keeps a shorter form of each, and the card citations, pages, DOIs and quotes it dropped are kept here.

- **Upstream**: PhD MIT 1988 (applied mathematics and OR), advisers Amedeo Odoni (primary) and Daniel Kleitman; Tom Magnanti on the committee; the thesis problem class came from Odoni's group [06 §2.1; S048 pp. 18, 71, 125].
- **Long collaborators**: John Tsitsiklis (queueing; LO textbook), Andrew Lo (finance), Robert Weismantel (IO book), Dick den Hertog (RO book; co-signs the 2021–2026 robust and global-optimization lines [S283 pp. 3–4, 15–19]), David Gamarnik (queueing book).
- **Downstream**: 109 completed PhDs and 20 current (homepage, 2026). Lineages: SD (Niño-Mora, Paschalidis, Gamarnik, Sethuraman); IO (Goemans, C.-P. Teo); CP (Popescu, Natarajan); RO (Sim, Thiele, Brown, Caramanis, Iancu, Gupta, Dunning); ML (Shioda, King, Dunn, Pauphilet, Cory-Wright); DA (Kallus, McCord, Sturt); health (O'Hair, Orfanoudaki, Wiberg, Ma) [04 A.4]. Alumni return as co-advisers, book co-authors, informal advisers and co-authors on later programme stages [04 B.10; S476 p. 1].

**Increment books-2026-10-29** (2026-10-29; book material, framing and dating only, outside every say–do count; full account: [Book material](#books)). Robert Freund added among the long collaborators: co-author of the MBA text in both editions [B015 pp. 1–5; B014 p. 1], and thanked with Dimitri Bertsekas in the 1997 preface for discussions and for reading parts of the manuscript [B001 p. 1]. The line before this increment (verbatim):

```text
- **Long collaborators**: John Tsitsiklis (queueing; LO textbook), Andrew Lo (finance), Robert Weismantel (IO book), Dick den Hertog (RO book), David Gamarnik (queueing book).
```

<a id="inner-tensions"></a>
## Inner tensions

**Before this synthesis** (verbatim):

```text
## Inner Tensions

- **Tension T1 · certified vs uncertified *optimal***: certificates make results strong [02 J2] vs OCT's mostly uncertified results, Dunn's bound stuck at zero and a product trained by local search under the *optimal* name [03 B4.3, B4.5].
- **T2 · joint optimization vs heuristic engine**: optimization beats greedy practice [02 R11] vs SA judged theoretically lacking in 1993, then used as a working tool 2009–2023 [03 B5.5].
- **T3 · optimization, not probability**: the 2019 principle [02 T4] vs asymptotic theorems in P2P, a 2022 queueing book, a thesis he describes as combining stochastic and optimization ideas [02 C4].
- **T4 · strong formulations vs solver speed** [inferred]: the 2005 IO book [02 T8] vs OCT's weak big-M and the inventory approximation [05 §2, §4.3].
- **T5 · impact soon vs slow pipelines**: 2–5 years, later two [02 C8], vs six years for P2P to print and manuscripts listed as submitted for 7–10 years [06 §7]; his horizon concerns adoption.
- **T6 · headline vs caveat**: *optimal*, *best* and big numbers up front, limits in the body; Boston *delayed* (PNAS) vs *not implemented* (thesis) [05 §5.1].
- **T7 · decide before starting vs aim beyond reach**, valuing the failed 1989 proof [02 C1].
- **T8 · open ideas vs own beliefs; every student vs first-rate people** [02 C7, C10].
- **T9 · students first vs capacity**: weekly one-on-ones [02 O10] vs missed meetings (2015) and capacity he says he may have exceeded [04 B.4].
```

**Full-text evidence** (08 §2 table and §3 rows 16, 18, 22, 24, 25).
- *T1* (64 works carry a T1 note; C9): see [Method 4](#method-4), "Certificate dropped: older and wider". Quote: "In addition, because a provably optimal solution is not critical in this context, we can prematurely terminate the branch-and-bound procedure, say at 5% to 10% relative optimality gap or by a time limit." [S073 p. 17]. *Fix round*: the reply to the best-subset critics sets a 60 s limit by confidence in the warm start, since the algorithm "spends a lot of the time proving its optimality", and reports no gap [S095 pp. 5, 39].
- *T2* (11 works; softened, C15): the 1993 review credits simulated annealing with general applicability and good solutions where structure is not understood, finds its practice mixed, and judges it by the equal-time comparisons it reports from Johnson et al. [S005 pp. 4–5]: "As far as theory is concerned, there is at present a definite lack of rigorous results justifying the use of SA." [S005 p. 4]; a priori heuristics recommended to practitioners in 1991 [S089 pp. 1, 33]: "Based on extensive testing we conclude that our heuristics are very close in terms of performance compared with re-optimization strategies and can be used by a practitioner." [S089 p. 1]; a heuristic engine beating CPLEX in 2002 [S070 pp. 13–15]; a regime map that recommends greedy where optimization does not pay [S046 p. 19]; annealing in daily production [S103 pp. 8–9].
- *T3* (21 works): asymptotic probabilistic analysis is the backbone of 1988–2002 [S038 pp. 6–8; S016 pp. 5–14; S017 pp. 10–11; S130 pp. 4, 13, 22]; limit laws re-enter as uncertainty sets [S065 pp. 5–10; S119 pp. 7–10; S227 pp. 1, 4, 13, 27]; clinical texts centre on confounding and calibration [S685 pp. 1–3]: "If a key prognostic variable is missing, no amount of clever modeling will recover the true treatment effect." [S685 p. 2]; Bayesian and EM machinery [S666 pp. 7–8, 44–45].
- *T4* (23 works; narrowed, C10): formulation strength measured and pursued [S241 pp. 14–15, 27, 31–32; S015 pp. 2, 4–5, 10; S101 pp. 17–18; S109 pp. 2–8; S037 pp. 2, 4–8; S076 pp. 12–19, 35–36]; a formulation-strength ordering tested against gaps and solve times, printing where it fails [S093 pp. 8–9, 17–19]; constrained Lasso shown weaker than the root relaxation [S010 pp. 9–10]; big-M left for convex integer or perspective forms [S061 p. 6; S175 pp. 9–10, 15–16; S136 pp. 3, 6–7, 26–27]; SOC strengthening kept [S250 p. 23]. Big-M weakness printed by the authors themselves [S225 pp. 5–9; S358 pp. 4–12]: "Although, the “Big-M” formulations are weak, for tractability of the problem, we linearize constraints (10) using McCormick type linearization" [S358 p. 10]. "We had to experiment with different formulations to identify those that yield tighter relaxations and with heuristics to create appropriate starting solutions so that Gurobi would avoid long delays at the root relaxation." [S339 p. 8]. T4 stays, narrowed to optimal trees and some ML models [S097 pp. 44–45].
- *T6* (49 works): the caveat sits in the body [S093 pp. 2, 20]: "Admittedly, some of this reduction is likely due to hardware improvements and general improvements in LO/MIO solution software since the time that their paper was written (2008)" [S093 p. 20]; Boston as in [Method 5](#method-5) (C12). *Fix round*: SKILL.md's T6 example no longer sets p. 2 against p. 6 of the PNAS paper (the two wordings agree: not implemented yet, delayed); it sets the abstract, which reports the unanimous approval of the reform [S137 p. 1], against the non-implementation stated on p. 2 [S137 p. 2] and in the 2020 account [S262 p. 12].

**Moved at the tighten step** (T3.7, 2026-10-29). These SKILL.md lines are copied verbatim as they stood before the cut; SKILL.md now keeps a shorter form of each, and the card citations, pages, DOIs and quotes it dropped are kept here.

- **Tension T1 · certified vs uncertified *optimal***: certificates make results strong [02 J2] vs runs stopped early or uncertified from 2004 on [S031 p. 26; S073 pp. 15–18], a limit set by confidence in the warm start, as the solver "spends a lot of the time proving its optimality" [S095 p. 5], and applied trees called optimal with no gap or limit [S094 pp. 5, 9]; honest labels elsewhere [S093 pp. 17, 19] (C9).
- **T2 · joint optimization vs heuristic engine**: optimization beats greedy practice [02 R11] vs simulated annealing judged lacking in theory, mixed in practice but generally applicable (1993) [S005 pp. 4–5], a heuristic beating CPLEX (2002) [S070 pp. 13–15], greedy recommended where optimization does not pay [S046 p. 19].
- **T3 · optimization, not probability**: the 2019 principle [02 T4] vs asymptotic probabilistic analysis as the backbone of 1988–2002 [S038 pp. 6–8; S016 pp. 5–14], limit laws returning as uncertainty sets [S119 pp. 7–10], and a thesis combining stochastic and optimization ideas [02 C4].
- **T4 · strong formulations vs solver speed** [inferred]: strength measured and pursued in air-traffic and product-line models [S015 pp. 2, 4–5, 10; S093 pp. 8–9, 17–19] vs weak big-M in tree MIOs and some ML models [S225 pp. 5–9; S358 pp. 4–12] (C10).

**Increment books-2026-10-29** (2026-10-29; book material, framing and dating only, outside every say–do count; full account: [Book material](#books)).
- **T1**: the stated side now includes the ML book's promise, on his own books page in 2026, of solutions that "can be certified to be optimal in minutes/hours" [B008 p. 1]; a 2020 reviewer reads it as solutions "impossibles à améliorer" (impossible to improve) [B010 p. 1].
- **T2**: re-dated: the verdicts are in print in 1992 [B020 pp. 8–10] (C22). Teaching data, not in SKILL.md: simulated annealing is one IP heuristic in about two book pages of the 1997 textbook [B004 p. 5], local search and simulated annealing about six of the 550 body pages of the 2005 book [B007 p. 3], and one lecture, shared with approximation algorithms, in 2009 [B021 p. 2].
- **T3**: the stated side now has its page [B009 p. 1]; the practice side adds the 2022 queueing book, four of whose five parts (titles only; Part V an appendix) are queueing analysis and probability [B013 p. 1] (card B013: [inferred from the structure]; a count of part titles, not a share of the content). *Fix round*: SKILL.md's "four-fifths queueing analysis and probability" is replaced by this wording. Not in SKILL.md: about 62% of the 2000 MBA text is decision analysis, probability, sampling, simulation and regression [B015 pp. 1–5]; a reviewer finds the RO book's link with probability "rarement aussi explicite et détaillé" (rarely this explicit and detailed) [B012 p. 1]. The 2019 principle concerns ML, so these are the practice side, not contradictions.
- **T4** (not in SKILL.md): the stated side has a 1997 section "Guidelines for strong formulations" [B004 p. 4] and the 2005 emphasis [B006 p. 1; B007 p. 1].

The lines before this increment (verbatim):

```text
- **Tension T1 · certified vs uncertified *optimal***: certificates make results strong [02 J2] vs runs stopped early or uncertified from 2004 on [S031 p. 26; S073 pp. 15–18] and applied trees called optimal with no gap or limit [S094 pp. 5, 9] (C9).
- **T2 · joint optimization vs heuristic engine**: optimization beats greedy practice [02 R11] vs simulated annealing judged lacking in theory, mixed in practice but generally applicable (1993) [S005 pp. 4–5] and greedy recommended where optimization does not pay [S046 p. 19].
- **T3 · optimization, not probability**: the 2019 principle [02 T4] vs asymptotic probabilistic analysis as the backbone of 1988–2002 [S038 pp. 6–8; S016 pp. 5–14] and limit laws returning as uncertainty sets [S119 pp. 7–10].
```

<a id="roundtable-card"></a>
## Roundtable card

**Before this synthesis** (verbatim):

```text
## Roundtable Card

- **Lens (one line)**: Start from a decision someone owns and the data held; write it exactly as LP, conic or MIO that stays in the solver class; price what matters with one knob; judge decisions against the current rule; re-measure every *intractable*.
- **Leads when**: an exact MIO could replace a greedy estimator; predictions drive decisions; robust counterparts must keep their class; a trade-off needs a price; a partner has data and a current rule; a problem is called intractable; a cross-team problem needs an owner, class and metric (convener).
- **First questions asked**: Who owns the decision, with what data and current rule? Taught or used within 2–5 years if it succeeds? Does the exact or robust version stay LP, conic or MIO? What does today's solver do on a real instance? Which knob, incumbent and decision metric?
- **Default recommendation**: exact formulation warm-started by the incumbent, with limit and gap; class-keeping robust sets; a price curve with its bad case; decisions scored against the partner's rule; a field pilot.
- **Will push back on**: unmeasured *intractable* verdicts; greedy heuristics as final methods; small-sample randomization; predictions without decisions; black boxes where people act.
- **Likely disagreements** ([inferred] from published methods; no dispute documented unless marked):
  - Huangfu: net gain inside the best solver (doi:10.1007/s12532-017-0130-5) vs speed-up products (doi:10.1214/15-AOS1388).
  - Ye (1998 co-author), Nesterov: self-certifying, complexity-first methods (doi:10.1287/moor.19.1.53; doi:10.1007/s10107-006-0706-8) vs uncertified tree search (doi:10.1007/s10994-017-5633-9).
  - Nocedal, Gould, Toint, Wächter, Gill, Fletcher, Wright, Curtis, Robinson: equal stopping tests, whole collections (doi:10.1007/s10589-014-9687-3; doi:10.1007/s10107-004-0559-y) vs group-chosen budgets (best subset).
  - Sahinidis: *documented* discussion (doi:10.1214/20-STS806) of BPV (doi:10.1214/19-STS701). Scheinberg: *documented critique* of OCT (doi:10.1007/s10898-021-01009-y).
  - Powell, Conn, Audet, Vicente: a convergence backbone (doi:10.1007/0-387-30065-1_16; doi:10.1137/1.9780898718768; doi:10.1137/040603371) vs SA and robust local search (doi:10.1287/opre.1090.0715).
  - Dey, Burer, Misener: formulation strength (doi:10.1287/opre.2015.1357; doi:10.1007/s10107-008-0223-z; doi:10.1007/s10898-014-0166-2) vs big-M plus solver speed (OCT); his 2005 book agrees.
  - Leyffer (his survey, doi:10.1080/03155986.2020.1730676, cites the robust local search): surrogates outside their data vs constraint learning (doi:10.1287/opre.2021.0707).
  - Grossmann: deterministic model first, certified *global* (doi:10.1007/BF02592064) vs robust-first (doi:10.1109/TPWRS.2012.2205021).
- **Blind spots**: heuristics' convergence; formulation strength; fair benchmarking; stakeholder process; forecast scoring; solver internals; probabilistic modelling (disowned, practised); SD and CP method.
```

**Changes** (seven bullets kept). Lens, leads-when, first questions, default recommendation and push-back add Method 7 (a bound valid for every policy; heuristics judged only against heuristics). Blind spots narrowed from the full texts: *formulation strength* → of tree MIOs (C10); *fair benchmarking* → the 2016–2017 best-subset benchmarks, matched elsewhere (C8); *solver internals* → inside commercial solvers (C5); *SD and CP method* removed (C1). The Dey–Burer–Misener line notes that his formulation papers agree with them (C10). *Fix round*: the blind spot *heuristics' convergence* is narrowed to asymptotic convergence claims for stopped heuristic runs [S141 pp. 5–6, 11], since the robust local search proves convergence for convex costs with an exact oracle [S090 pp. 5, 17]; the Powell–Conn–Audet–Vicente line says so (C3). The card keeps its DOIs, which the roundtable's later steps use to draft fault lines.

<a id="honest-boundary"></a>
## Honest boundary

**Before this synthesis** (verbatim):

```text
## Honest Boundary

- **Research basis**: six research notes (2026-10-28) from his homepage, two CVs, the 2014 Sloan oral history (read in full), publisher pages, lecture abstracts, about 30 thesis acknowledgements, version histories, repositories and critics' texts. Signature papers were read in part, many others at abstract or metadata level; no full-text deep reading yet.
- **Tacit gaps**: the 2021 *Subject to* interview (supervision, selection criteria, time management) was not read; how Γ arose and why he entered RO are unknown; the BPV rejoinder (DOI 10.1214/20-STS701REJ), book prefaces, IJOO editorials and prize citations were not read; his real-time judgment in meetings is invisible.
- **Era and resources**: post-2006 practice rests on institution-scale resources (industry funding, 16–26 PhD students, his own press and companies, hospital partners). His early years ran on his adviser's grants and co-advising: that is the transferable version. Method 2 depends on the 1991–2018 MIO speed-ups.
- **Field boundary**: no stated methodology for SD and CP; HS thin; LO textbook-era only. Do not speak for stochastic programming, ADP and RL, statistical learning theory or constraint programming.
- **Claimed but unverified** (never used as methods): adaptive RO as a new way to solve RO; the best idea wins whoever had it; saying yes to every prospective student; 60% of students becoming professors; most graduates going to academia or small firms (contradicted: 6 of 8 announced 2025–26 placements went to large firms); weekly one-on-ones after 2014; students joining his companies only after graduating; impact within two to five years as a rule; certification in minutes as a general property; the Hartford length-of-stay figures; the Panama Canal plan; the diabetes trials' outcomes; the 2009 losses as the health programme's trigger; companies as the channel to scale; data as objective reality; positive energy over IQ; geometry first in research.
- **Corrections applied**: the AoS 2016 speed-up is about 450 billion (200 billion is the 2014 lecture and arXiv v1); Ye is a 1998 co-author; arXiv 1402.5481 v2 was Kallus's withdrawal, not his; the DELPHI model paper is OR 2023 (DOI 10.1287/opre.2022.2306), distinct from the 21-author COVID-19 paper (DOI 10.1007/s10729-020-09542-0).
- **Constructs**: critic-informed checkpoints (Methods 1–5) are labelled as not his practice; the council-convener role is a construct of this council.
- **Living researcher; research date 2026-10-28**: later work is not covered. Update this skill periodically (at least yearly), and sooner once the 2021 interview, the 2026 RO retrospective or a full-text deep reading is done.
```

**Changes.** The research basis now gives the coverage of the full-text reading (team_status row: 932 Scholar rows, 751 distinct works, 473 open full texts, 413 read in full, 59 in part, 63 abstract only, 56 metadata only, 160 skipped, 1,083 quotes verified); the remaining gaps follow 08 §11; the field boundary drops "no stated methodology for SD and CP" (C1); a short list of corrections from the full texts sits under the Honest Boundary in SKILL.md, with the earlier wording below. *Fix round*: the claimed-but-unverified item "the Hartford length-of-stay figures" is annotated: the 2023 preprint read for [S617] reports a 0.67-day difference-in-differences against a parallel-trends counterfactual, without a standard error, which its authors call descriptive [S617 arXiv pp. 23–25]; the 2026 lecture's figures do not appear in it, and the 2026 article was not read. The books list now names all eight abstract-level book cards [S002; S020; S128; S209; S047; S084; S334; S695].

**Increment books-2026-10-29** (2026-10-29; book material, framing and dating only, outside every say–do count; full account: [Book material](#books)). The research basis adds the 21 book-material cards and their 42 quotes (team_status: Book material carded 21; the research-work columns are unchanged); the remaining gaps say what of the books was read (the 1997 preface in its web form [B001 p. 1], four printed contents [B004 pp. 2–5; B007 pp. 1–4; B015 pp. 1–5; B018 pp. 1–5], publisher pages and his own [B002 pp. 1–3; B006 p. 1; B008 pp. 1–2; B009 p. 1; B011 p. 1; B013 p. 1; B014 p. 1; B017 p. 1; B019 pp. 1–2], an errata sheet [B003 pp. 1–5], four reviews [B005 pp. 13–14; B010 p. 1; B012 p. 1; B016 p. 1]) and that their bodies were not; the LO voice is no longer web-sourced only. Tacit gaps: *printed* book prefaces stay unread (the 1997 one is read only as the publisher serves it, Last-Modified 1999-11-04). Claimed but unverified: two items now have their joint statements with pages, ARO as a new way to solve RO [B011 p. 1] and data as objective reality [B017 p. 1; B009 p. 1]; both stay outside the methods. The first-activation disclaimer still says "his books at abstract level only": it is protected in an increment (see [Corrections](#corrections), pending edit). *Fix round*: the books clause of the remaining gaps now points here ([Book material](#books)), and the other gaps are "abstract- or metadata-level", as 08 §11 grades them (the achievable-region series abstract- or metadata-level, the editorials metadata-level). The lines before this increment (verbatim):

```text
- **Research basis**: six research notes (2026-10-28) from his homepage, two CVs, the 2014 Sloan oral history (read in full), publisher pages, lecture abstracts, about 30 thesis acknowledgements, version histories, repositories and critics' texts; then the full-text reading (2026-10-29): of 932 Google Scholar rows, 751 distinct works indexed, 473 with an open full text; 413 read in full and 59 in part, 63 at abstract and 56 at metadata level, 160 skipped (students' theses, reports, works not his); 611 cards, 1988–2026, including the 1988 thesis [S048]; 1,083 quotes verified verbatim.
- **Remaining gaps**: 119 research works have no open full text (abstract or metadata cards); his eight books are carded at abstract level only [S002; S020; S128; S209; S047; S084; S334; S695], so the LO voice and the textbooks' philosophy stay web-sourced; so are the 2026 RO retrospective [S614], parts of the achievable-region series, clinical validations and editorials [08 §11]; preprints read may differ from journal versions.
- **Tacit gaps**: the 2021 *Subject to* interview (supervision, selection criteria, time management) was not read; how Γ arose and why he entered RO are unknown; the BPV rejoinder (DOI 10.1214/20-STS701REJ), book prefaces, IJOO editorials and prize citations were not read; the pre-start impact gate and supervision routines cannot be seen in papers; his real-time judgment in meetings is invisible.
- **Claimed but unverified** (never used as methods): adaptive RO as a new way to solve RO; the best idea wins whoever had it; yes to every prospective student; 60% of students becoming professors; graduates mostly in academia or small firms (contradicted: 6 of 8 placements in 2025–26 at large firms); weekly one-on-ones after 2014; students joining his companies only after graduating; impact within two to five years as a rule; certification in minutes in general; the Hartford length-of-stay figures (the 2023 preprint's 0.67 days is a descriptive estimate without a standard error [S617 arXiv pp. 23–25]; the 2026 article was not read); the Panama Canal plan; the diabetes trials' outcomes; the 2009 losses as the health trigger; companies as the channel to scale; data as objective reality; positive energy over IQ; geometry first in research.
```

<a id="books"></a>
## Book material (increment books-2026-10-29)

> Date: 2026-10-29 (stage T4, increment "books-2026-10-29"). Source: 21 cards, each item read in full, in `cards/c5-01.md` to `cards/c5-05.md` (round 5; works.json `B` entries B001–B021); synthesis: `08-deep-reading-synthesis.md`, section "Increment books-2026-10-29". Book material is framing and dating: it never enters a say–do count and promotes nothing (`references/paper-reading-card.md` §三; `references/research-extraction-framework.md` §三). No book body was read. Every voice is joint (the co-authors' "we", or the publisher's page) unless marked, and reviews are their reviewers' voices. SKILL.md points here from How to Use, the Signature Work Anatomy note and the Honest Boundary; the evidence per SKILL.md item, with that item's wording before this increment, is in the blocks headed **Increment books-2026-10-29** under the item's own anchor.

### What was read

| Book [work card] | Open items [cards] | Voice | Not read |
|---|---|---|---|
| *Introduction to Linear Optimization*, with J. N. Tsitsiklis, Athena Scientific 1997 [S002] | the preface as served on the publisher's site [B001 p. 1]; the Athena book and contents pages and the Dynamic Ideas page [B002 pp. 1–3]; the printed title page and contents [B004 pp. 1–5]; the errata sheet [B003 pp. 1–5]; M. V. Ramana's review, *Optima* 54 [B005 pp. 13–14] | joint; publishers; reviewer | the body; whether the web preface equals the printed one; J. Bard's 2000 review (an excerpt only, on the publisher's page); Y. Ye's 1998 review |
| *Data, Models, and Decisions*, with R. M. Freund, South-Western 2000; 2nd ed. Dynamic Ideas 2004 [S128] | the 2000 printed contents [B015 pp. 1–5]; the 2004 publisher page [B014 p. 1]; an unsigned review on GraduateTutor.com [B016 p. 1] | joint; reviewer | body, prefaces |
| *Optimization over Integers*, with R. Weismantel, Dynamic Ideas 2005 [S020] | the publisher page [B006 p. 1]; the printed contents [B007 pp. 1–4]; the four-part map on his 2017 books page [B008 p. 2] | joint ("we") | body, preface; no review carded |
| *The Analytics Edge*, with A. K. O'Hair and W. R. Pulleyblank, 2016 [S209] | the publisher page [B017 p. 1]; the printed contents [B018 pp. 1–5] | joint first person | body, preface |
| *Machine Learning under a Modern Optimization Lens*, with J. Dunn, 2019 [S047] | the publisher page with structure and principles [B009 p. 1]; T. Cuvelier's review, with an older publisher summary and a third-party chapter list [B010 p. 1] | joint, as the publisher presents it; reviewer | body, preface |
| *Robust and Adaptive Optimization*, with D. den Hertog, 2022 [S084] | the publisher page [B011 p. 1]; T. Cuvelier's review, with a third-party chapter list [B012 p. 1] | joint "we"; reviewer | body, preface, the Dantzig quotation at the start of the preface |
| *Queueing Theory: Classical and Modern Methods*, with D. Gamarnik, 2022 [S334] | the publisher page: five parts [B013 p. 1] | publisher, no first person | everything else |
| *The Analytics Edge in Healthcare*, with A. Orfanoudaki and H. Wiberg, 2025 [S695] | the publisher page and the authors' site [B019 pp. 1–2] | publisher; joint | the book: its PDF is e-mailed only after a request form, which was not used |
| all eight | his books pages, 2026 and 2017 [B008 pp. 1–2] | his pages, mostly publisher sentences | — |
| not books | the 1992 printing of the simulated-annealing review, chapter 2 of the NRC report *Probability and Algorithms* [S438] [B020 pp. 1–14]; the Fall 2009 home page and syllabus of his course 15.093J [S564] [B021 pp. 1–2] | joint; his syllabus (the course description is MIT catalogue text) | lecture notes |

All the publisher, library, review and course URLs answered HTTP 200 on 2026-10-29 (re-checked at the integration step), and the six PDFs had the byte sizes of the local copies.

### Stated views per domain (for the Domain Map's Voice column)

- **LO** [stated-joint, 1997, with Tsitsiklis; B001 p. 1]: "Our general philosophy is that insight matters most." Insight "necessarily requires a geometric view", while algorithms "can only be described algebraically", hence "the beautiful interplay between algebra and geometry". Other stated choices: comprehensive but economical; the state of the art, with case studies "that stretch the limits of currently available algorithms and computers"; the full simplex tableau only a device for numerical examples; LP in general form, the standard form only for algorithms; "we separate the structural understanding of linear programming from the particulars of the simplex method", with a duality theory that does not rely on it; and "The success of any optimization methodology hinges on its ability to deal with large and important problems.", which makes the last chapter, on the art of linear optimization, "a critical part of this book". The four abilities the book builds, in order: formulate fairly complex problems; appreciate "the main classes of problems that are practically solvable"; describe the solution methods; understand the qualitative properties of solutions. The publishers add "at the PhD level" and "It emphasizes the underlying geometry, intuition and applications of large scale systems." [B002 p. 3], a sentence his own pages reuse [B008 pp. 1–2].
- **IO** [stated-joint, 2005, with Weismantel]: "We depart from earlier treatments of integer optimization by placing significant emphasis on strong formulations, duality, algebra and most importantly geometry." [B006 p. 1]; the topics chosen because "we feel" they "will affect the future of the field" [B006 p. 1]; "The key characteristic of our treatment is that our development of the algorithms is naturally based on the algebraic and geometric developments of Part II." [B008 p. 2]; mixed integer and robust discrete optimization included because real problems "have very often both continous and discrete variables and have elements of uncertainty that need to be addressed in a tractable manner" (spelling as printed) [B008 p. 2]. The 1997 antecedent: "some intuition as to what constitutes a ``strong'' formulation" [B001 p. 1] and a section "Guidelines for strong formulations" [B004 p. 4].
- **RO** [stated-joint, 2022, with den Hertog; B011 p. 1]: the purpose, "a unified, insightful, and original treatment of robust and adaptive optimization"; RO and ARO for LO first, then nonlinear RO, "as opposed to presenting RO first and then ARO", because "ARO offers new and very effective ways to solve RO problems, a fact not fully recognized earlier." (claimed, not verified); nonlinear RO by concave and convex uncertainty, "as opposed to treating robust conic optimization" (no reason given); applications "guided by the quote of George Dantzig at the beginning of the preface" (the quotation was not seen). Teaching dates, titles only: "Linear Optimization Under Uncertainty*" in the 2000 MBA text [B015 p. 4]; "Robust discrete optimization" as the last chapter of the 2005 IO book [B007 p. 4]; robust optimization as lecture 8 of 24 in the 2009 methods course, after sensitivity analysis [B021 p. 2].
- **CP**: no book voice. The 2005 IO book lists semidefinite approximation methods and optimization over polynomials [B006 p. 1]; the 2009 course closes with semidefinite optimization [B021 p. 2]. The label stays "stated jointly; this follows his co-authored papers" (C1).
- **SD**: the 2022 book with Gamarnik has a publisher page of five part lines and no first-person sentence; "Part IV outlines the use of optimization in queueing networks." [B013 p. 1]; his own page condenses Parts III–V [B008 p. 1]. The voice stays "stated in his sole-author texts 1988–1995" (C1).
- **ML** [stated-joint, 2019, with Dunn, as the publisher presents the book; B009 p. 1], the six "Philosophical principles of the book", as printed (some words run together on the page): "Interpretability is materially important in the realworld."; "Practical tractability not polynomial solvability leads to real world impact."; "NP-hardness is an opportunity not anobstacle."; "ML is inherently linked to optimization not probability theory. Data represent an objective reality; models only exist in our imagination."; "Optimization has a significant edge over randomization."; "The ultimate objective in the real world is prescription,not prediction.". The older summary, still on his 2026 page: "The book provides an original treatment of machine learning (ML) using convex, robust and mixed integer optimization that leads to solutions to central ML problems at large scale that can be found in seconds/minutes, can be certified to be optimal in minutes/hours, and outperform classical heuristic approaches in out-of-sample experiments." [B008 p. 1; B010 p. 1].
- **DA** [stated-joint]: 2004, with Freund [B014 p. 1]: "This book represents a departure from existing textbooks. Rather than covering methodology, the book introduces decision support systems through real world applications"; "It is our mission in this book to contribute to preparing today's management students to become tomorrow's business leaders, and therefore demonstrate that the tools and models of management science pass Dantzig's test."; "Simply teaching students to plug numbers into black-box models is not relevant to a student's education."; "In context, spreadsheets are a vehicle for working with models, but are not a substitute for thinking through the construction of models and analyzing modeling-related issues." 2016, with O'Hair and Pulleyblank [B017 p. 1]: "Problems and data play a leading role in this book, while models play an essential but supporting role."; "The only objective reality is data, which itself may be incomplete and of questionable quality, and the role of models is to facilitate the solution of real world problems."; real problems "do not come with labels".
- **HS** [stated-joint, 1992, with Tsitsiklis]: "As far as theory is concerned, there is at present a definite lack of rigorous results justifying the use of simulated annealing." [B020 p. 8]; practice "mixed" in the Johnson et al. study the review reports, with the comparison at equal computation time [B020 p. 9]; "Overall, SA is a generally applicable and easy-to-implement probabilistic approximation algorithm that is able to produce good solutions for an optimization problem, even if we do not understand the structure of the problem well." [B020 p. 10]. In his textbooks, heuristics are a few pages of the IP chapters [B004 p. 5; B007 p. 3].
- **AP** [stated-joint, 2025, with Orfanoudaki and Wiberg; B019 p. 2]: "Analytics is not in conflict with medical expertise, but synergistic with it: a new paradigm of evidence-based care, learned from the records of millions of patients."; recent advances "through real applications developed with leading medical centers"; "Each chapter introduces a class of algorithms through the lens of a real clinical example." The 2016 application areas: humans and machines, sports and games, healthcare, the internet, crime, operations, finance [B017 p. 1; B018 pp. 1–4].

### How the books are organised (contents and prefaces; titles only, the cards' counts)

- **1997 LO** [B004 pp. 2–5; B001 p. 1]: 12 chapters and 112 sections, 8 starred; the LP core 40% of the 568 chapter pages, network flows (the longest chapter) 17%, polynomial-time methods 16%, integer programming 14%, the art chapter 6%; geometry before the simplex method; the simplex-free and general duality starred; a section on strong formulations before the IP algorithms; heuristics in three book pages; stochastic programming as one section (Benders decomposition, inside large-scale optimization); a theme across chapters: problems with exponentially many constraints, from modeling to complexity, algorithms and a case study [B001 p. 1].
- **2000 MBA text** [B015 pp. 1–5]: ten chapters, opening with decision analysis and "The Need for a Systematic Theory of Probability"; about 62% probability, statistics and simulation, 31% optimization, 6% a capstone; each optimization chapter opens with the formulation of a management problem; branch and bound and a solvability taxonomy starred; 33 case modules; no title on queueing.
- **2005 IO** [B007 pp. 1–4]: 14 chapters, no part headings in print; formulations and their strength first (chapters 1–3, 22% of 550 body pages); duality a chapter of its own; algebra and geometry before the algorithms; approximation algorithms the longest chapter (60 pages), with a section on limitations in approximability; robust discrete optimization last; no title on computation, applications or a solver.
- **2016 analytics** [B018 pp. 1–5]: seven application parts, then "Methods and Exercises to Put the Analytics Edge into Action" in about the last fifth; linear and integer optimization the shortest section of the methods overview.
- **2022 RO** [B011 p. 1]: six parts (linear RO and sets; ARO; nonlinear RO with concave, then convex uncertainty; distributionally robust theory; applications); a third-party list of 27 chapter titles, not checked against print [B012 p. 1].
- **2022 queueing** [B013 p. 1]: queues, networks, asymptotic methods, optimization (one part of five), the probabilistic machinery in an appendix.
- **2025 health** [B019 p. 2]: 11 method chapters, each through one clinical example; nine case studies; two chapters of summary tables; optimization one chapter of eleven, in a closing decision group with prescriptive methods and fairness.

### Errata

[B003 pp. 1–5], joint with Tsitsiklis: "Last updated on 7/5/2021"; a sixth printing named ("In some copies of the 6th printing, this figure is missing", with the whole page reproduced) [B003 p. 1]; 68 items in three lists by printing (13 still listed for the third and later printings, 31 fixed after the second, 24 after the first; the card's count); local fixes (hypotheses added, signs and strictness, a table, names), with no wrong theorem or proof reported; 18 of the 24 fixes after the first printing are exercises; Exercise 3.8 replaced by a hardness result: "This exercise deals with the problem of deciding whether a given degenerate basic feasible solution is optimal and shows that this is essentially as hard as solving a general linear programming problem." [B003 p. 4]. Note 03 B5.2 says "about 33" entries (correction candidate, not applied). No addenda found.

### Reviews (reviewers' voices; also in note 05)

- **M. V. Ramana**, *Optima* 54 (June 1997), on the 1997 book [B005 pp. 13–14]: adopts it for his own course; chapters 8, 9 and 12 alone a reason to buy it; the last chapter "unique to this book"; the geometric explanations "widely successful". Criticisms: no upper-bounded simplex; the network simplex for the uncapacitated case first; chapter 6 brisk; "In trying to cover too many topics in one chapter, I feel that the authors have somewhat compromised the clarity of exposition in this chapter." (chapter 7) [B005 p. 13]; chapter 11 omits the Gomory convergence proof and brings in complexity classes "out of the blue"; dense in places, with the tone of a research paper [B005 p. 14]. The publisher quotes only his praise [B002 p. 1].
- **J. Bard**, *Interfaces* 30(4), 2000: an excerpt on the publisher's page only ("at the top of the list") [B002 p. 1]; the review was not read.
- **T. Cuvelier**, developpez.com, 6 December 2020, on the 2019 ML book [B010 p. 1]: "Ce parti pris n'est pas encore suivi par la communauté de l'intelligence artificielle au sens large" (this stance is not yet followed by the wider AI community); "En particulier, cela signifie qu'il n'existe pas encore d'implémentation répandue pour la plupart des algorithmes présentés." (in particular, there is not yet a widespread implementation for most of the algorithms presented); most content the authors' own research; rigorous yet readable; demanding prerequisites.
- **T. Cuvelier**, developpez.com, 2 December 2022, on the 2022 RO book [B012 p. 1]: "L'auteur y poursuit une approche très pragmatique, où les temps de calcul en pratique sont plus importants qu'une classe de complexité abstraite." (a very pragmatic approach, in which computing times in practice matter more than an abstract complexity class); "Le lien avec les probabilités est rarement aussi explicite et détaillé." (the link with probability is rarely this explicit and detailed); no criticism.
- **Unsigned, GraduateTutor.com**, about 2014 [inferred], on the MBA text [B016 p. 1], weak evidence (a company selling tutoring for the book; linked from the publisher's page [B014 p. 1]): "Unlike most text books, the objective is not to cover standard topics in statistics and operations research but to provide students frameworks for decision making."; "One wonders, however, if students would be better off having more depth in statistics and operations management separately."

### Dating and versions

- B020 = S005: one work in two printings (1992 NRC chapter; 1993 *Statistical Science*); counted once, as S005; the 1992 printing dates the verdicts (C22) [B020 pp. 8–10].
- His books pages date *Introduction to Linear Optimization* by its 2008 Dynamic Ideas edition and the MBA text by its 2004 second edition [B008 pp. 1–2]; this skill dates both by their first editions (1997; 2000).
- Contradiction kept: his 2017 page maps *Optimization over Integers* as Part III = chapters 9–11 (with approximation algorithms) and Part IV = chapters 12–13 [B008 p. 2], while the printed contents carry no parts and put approximation algorithms in chapter 12, mixed integer optimization in 13 and robust discrete optimization in 14 [B007 pp. 3–4].

### SKILL.md lines changed outside an item anchor (verbatim, before this increment)

The epigraph gained the card citation [B009 p. 1]; the Signature Work Anatomy note no longer says "prefaces unread; abstract-level cards".

```text
> "Practical tractability not polynomial solvability leads to real world impact." — Bertsimas & Dunn, *Machine Learning under a Modern Optimization Lens* (Dynamic Ideas, 2019), "Philosophical principles of the book" on the publisher's page (https://www.dynamic-ideas.com/books/machine-learning-under-a-modern-optimization-lens; wording checked 2026-10-28)
Rows rest on the full texts. Earlier rows: the ledger anchor under each table; a seventh anatomy (execution costs): ledger `#anatomy-execution-costs`. The textbooks are not dissected (prefaces unread; abstract-level cards); web-pass dissections: [01 §2](references/research/01-publications.md).
```

### Not added to SKILL.md

- The disclaimer's book clause (protected in an increment; pending edit under [Corrections](#corrections)).
- No new method, heuristic or taste item: book material alone never promotes; the eight pool candidates are in 08, "Increment books-2026-10-29", I.9.
- No say–do count change; no Research Trajectory "Latest" line (no new edition or work in 2025-10 to 2026-10 [B008 p. 1]).
- Reception lines from the RO review (positive, no criticism [B012 p. 1]) and from the unsigned MBA-text review (weak [B016 p. 1]): note 05 only.
- The teaching variants of Methods 1 and 5 at MBA level, the M3, M7, H9 and H10 links, and the 2025 health book's method-first Part I: here and in 08 only.

<a id="corrections"></a>
## Corrections from the full texts

Each line: the earlier wording (verbatim where it was a phrase in SKILL.md), the correction, the cards. Reasons and decisions: 08 §3.

- **C1** SD and CP: "co-authored papers only; no stated methodology found" (Domain Map), "For CP and SD add "no stated methodology found; this follows his co-authored papers"" (Activation Rules, kept byte-identical and superseded by the rewritten disclaimer line), "CP and SD voiced from co-authored papers only" (How to Use), "no stated methodology for SD and CP" (Honest Boundary). → SD stated in sole-author texts 1988–1995 [S048 pp. 11–13; S017 pp. 3, 12; S580 pp. 5, 10; S185 pp. 1–3]; CP stated jointly [S018 p. 1; S007 p. 35].
- **C2** IO anchor "LP-relaxation rounding" with DOI 10.1007/BF01580607 → that paper bounds by the LP value, with tight families, and has no rounding step [S052 pp. 10–18, 20–21]; rounding is in [S036 pp. 6–7; S658 pp. 18–20; S121 pp. 3–9; S435 pp. 3–6; S007 pp. 33–35].
- **C3** HS caution "Convergence of his robust local search not read" → read [S141 pp. 5–6, 9, 11; S278 pp. 2–6; S116 pp. 5, 8–9, 13–14]; *fix round*: the anchor itself [S090] proves convergence only for convex costs with an exact worst-error oracle and diminishing steps, and calls the nonconvex method a heuristic, with no certificate [S090 pp. 5–6, 12, 15–17]. The Roundtable Card's blind spot *heuristics' convergence* is narrowed accordingly.
- **C4** AP caution "Outcomes thin" → outcomes measured in several deployments [S115 pp. 22–26; S617 arXiv pp. 11–14, 22–25, 37–39; S339 pp. 10–11; S137 p. 3].
- **C5** "solver internals, which his record treats as black boxes" (How to Use), "the model, not the algorithm, is redesigned" (Method 1), blind spot "solver internals" → from 2009 the group also builds algorithms [S040 pp. 2, 6, 10, 12, 15; S315 pp. 8–12; S105 pp. 7–9; S184 pp. 8–18; S093 pp. 10–13; S302 pp. 1, 5–8; S385 pp. 2, 6, 10–14; S624 pp. 10–16; S316 pp. 3, 5, 11; S083 p. 15]; earlier, a commercial package was chosen over custom algorithms [S036 p. 7].
- **C6** Method 2 step 3 "never reuse the last paper's number" presented as his practice → the skill's rule; rebuilt only in 2014–2017 [S010 pp. 7–8; S081 p. 4; S011 pp. 5–6]; repeated or borrowed later [S105 pp. 6–7; S480 pp. 7, 9].
- **C7** Method 3 dated from 2004; "set the knob from data, as his group later did" → price-of-X practice from 1988 [S048 pp. 29, 40–44; S597 pp. 36–38; S135 pp. 15–16]; knobs set from data from 2006 [S014 pp. 1, 10–12; S022 pp. 3, 15, 19; S090 pp. 12, 14; S024 pp. 3, 5, 9, 11]. *Fix round*: one-knob practice dates from 1990 [S597 pp. 36–38; S032 p. 16]; the 1988 thesis is a knob-free precursor that prices robustness in lost tractability [S048 p. 29], not a statement of the method; knobs come from moments in 2006 [S014 pp. 10–12] and from samples and a risk measure in 2009 [S024 pp. 3, 5].
- **C8** Method 4 "*Critic-informed checks, not his practice*" and blind spot "fair benchmarking" → his practice in many works since 1993 and widespread after 2020 [S005 pp. 3–4; S340 pp. 16, 23; S197 pp. 8–14; S708 pp. 35–41; S317 pp. 13–24, 39–43, 49; S095 pp. 3, 10, 21, 23]; the critics' cases concern particular best-subset papers. *Fix round*: 1993 is a stated yardstick, not his practice: the review has no experiments of its own and applies equal computing time to Johnson et al.'s [S005 pp. 3–4]; his own matched comparisons start in 2002 [S070 pp. 9–15]; equal memory over time checkpoints [S328 pp. 9, 11–15]; the 2014 duel sets one 60 s budget per decision and prints the rival's overruns [S340 pp. 16, 23].
- **C9** Method 4 say–do "dropped at scale (OCT p. 1062 …)" and Tension T1 dated by OCT 2017 → from 2004 [S031 p. 26; S073 pp. 15–18; S141 pp. 5–6, 9, 11; S011 pp. 14, 26].
- **C10** Tension T4 and blind spot "formulation strength" → strength measured and pursued [S241 pp. 14–15, 27, 31–32; S015 pp. 2, 4–5, 10; S093 pp. 8–9, 17–19]; narrowed to tree MIOs and some ML models [S225 pp. 5–9; S358 pp. 4–12].
- **C11** Method 5 say–do "✅ stated + practised" → narrowed: fourteen prediction-only papers, twelve clinical, and a vaccine-site plan [S557 pp. 4, 8, 13; S054 pp. 4–9; S083 pp. 1, 17–18, 23].
- **C12** Tension T6 "Boston *delayed* (PNAS) vs *not implemented* (thesis)" → the PNAS text itself says not implemented (p. 2), later a delay (p. 6) [S137 pp. 2, 6]; the group's own post-mortem [S262 pp. 10–12]; DELPHI confirmed at baseline level [S021 pp. 2, 4; S103 pp. 14–16]. *Fix round*: the two PNAS wordings agree (*not implemented yet*, *delayed*), so the earlier contrast was incomplete rather than wrong (⚠, not ✗); T6 now uses the abstract's unanimous approval against p. 2 [S137 pp. 1–2].
- **C13** Heuristic 5 citing DOI 10.1287/opre.2021.0707 → constraint learning [S097 pp. 1–9]; replaced by [S204] and [S681].
- **C14** Heuristic 1 "[02 G2; metadata level]" → full texts [S009 pp. 4, 9–10, 43; S003 p. 37; S225 pp. 5–6, 14–17; S085 pp. 7–15]; the Lasso equivalence is credited to Xu–Caramanis–Mannor [S085 pp. 7–15].
- **C15** Tension T2 "SA judged theoretically lacking in 1993" → theory lacking, practice useful, judged by equal-time duels [S005 pp. 4–5]. *Fix round*: practice mixed rather than useful (behind Lin–Kernighan on the TSP, far slower on colouring), but generally applicable; the equal-time comparisons are Johnson et al.'s, reported [S005 pp. 4–5].
- **C16** Trajectory "Inherited from Odoni's group [inferred]"; the row "1995–2001 | Moments and SDP {CP}"; RO from 2001 → documented [S048 pp. 18, 71, 125]; SDP strengthening from 1994–95 [S072 pp. 20–22; S185 pp. 44–45]; budgets from 2002 [S653 pp. 12–14; S004 pp. 4–7; S001 pp. 3–5].
- **C17** Note 06 §6, 1988–1995: "Pencil-and-paper probability and polyhedral theory; little computation" → theory-led, with steady computation [S089 pp. 13–17, 23, 26–28; S291 p. 13; S168 pp. 15–16; S389 pp. 11–14; S036 pp. 7–10; S135 pp. 1–2, 7–8, 15–16]; note 06 updated (§10 of its 2026-10-29 update).
- **C18** Note 05 row 16 (execution costs): "permanent impact only" → the LPT law makes impact temporary; permanent impact and negative prices are defects named in the paper's first illustration [S009 pp. 17, 20–22]. Note 05 is not edited in this step (outside its file list); the correction stands here and in SKILL.md.
- **C19** Warning sign 2 undated → applies from about 2004; his 1994–1997 papers argue from operation counts [S269 pp. 1, 21–22; S289 pp. 2, 6, 11–12]. *Fix round*: *his rule from about 2004* (SKILL.md) is replaced by one dating used throughout: computation named the criterion in 2004 [S001 p. 8]; solve time stated as the test from 2014 [S178 p. 5] and in 2016 [S010 p. 2].
- **C20** Disclaimer and Honest Boundary "no full-text deep reading has been done yet" / "no full-text deep reading yet" → overturned by the coverage above.
- **C21** (fix round) Taste mark 5 "Interpretable where people act on the result" and warning sign 5 "Black boxes in decisions about people [02 T6]" → scoped by decision type: required where guidance changes standard care, black boxes acceptable for diagnosis [S685 pp. 2–3]; counter-practice: boosted trees explained by SHAP in tools clinicians use [S054 pp. 4–9; S621 pp. 2–3, 16–18], and a trust ladder from optimal trees to XGBoost once doctors were receptive [S617 arXiv pp. 9–11, 20–21].
- **Activation Rules, rule 3** (applied 2026-10-29 in an operator step after T3.6 and before T3.7: rule 3 now carries the SD and CP labels below with "(C1)", the disclaimer's override sentence "**Label correction (C1), overriding the CP and SD clause of the next rule**: for SD add …; for CP add …" is dropped, and the convener's agenda and sign-off name *a bound valid for every policy* beside *certificate or gap*; the earlier wording follows): the rule still tells the model to add, for CP and SD, *no stated methodology found; this follows his co-authored papers* (SKILL.md, Activation Rules, rule 3). The T3.6 deletion detector protects every Activation Rules line except the first-activation disclaimer, so the override sits in the disclaimer line (C1). Proposed one-line edit for an operator-approved step: for SD add *stated in his sole-author texts 1988–1995*; for CP add *stated jointly; this follows his co-authored papers*; then drop the override sentence from the disclaimer. Likewise pending: the convener's agenda and sign-off could name *a bound valid for every policy (no exact solve)* beside *certificate or gap* (Method 7).
- **C22** (increment books-2026-10-29) The simulated-annealing review's verdicts dated 1993 (Domain Map HS row, Tension T2, Method 4's line on the critic-informed checks; C8 and C15 cite the 1993 journal pages) → the same text is in print in 1992, as chapter 2 of the National Research Council report *Probability and Algorithms* (Crossref: DOI 10.17226/2026, issued 1992; checked 2026-10-29): the theory verdict [B020 p. 8], the mixed practice and the equal-time comparison [B020 p. 9], the general applicability [B020 p. 10]. The card's word comparison finds copy-edits only. B020 and S005 are one work in two printings: S005 is counted, B020 dates it. *Fix round*: SKILL.md's C22 now names C8 in its scope, since C8 still dates the equal-time yardstick to 1993 by the journal pages [S005 pp. 3–4], while Method 4's line dates it to 1992 [B020 p. 9]; C8's own wording is unchanged.
- **Activation Rules edit, applied 2026-10-29** in an operator step after the increment: the disclaimer now ends "his eight books only through their open parts (the 1997 preface, publisher pages and his own, four contents lists, an errata sheet, four reviews), never their bodies" [B001 p. 1; B002 pp. 1–3; B008 pp. 1–2; B004 pp. 2–5; B007 pp. 1–4; B015 pp. 1–5; B018 pp. 1–5; B003 pp. 1–5; B005 pp. 13–14; B010 p. 1; B012 p. 1; B016 p. 1]. The earlier entry follows verbatim. **Pending Activation Rules edit** (increment books-2026-10-29, not applied: an increment may change only the numbers of the first-activation disclaimer, and they do not change, because book material is not counted in the research-work columns): the disclaimer still ends "his books at abstract level only". Proposed wording for an operator-approved step: "his eight books only through their open parts (prefaces, publisher pages, contents, errata, reviews), never their bodies". How to Use and the Honest Boundary already say this.

**Earlier frontmatter** (verbatim; `researched:` is now 2026-10-29 and the description mentions the full-text coverage and bounding policies):

```text
---
name: dimitris-bertsimas
description: |
  Dimitris Bertsimas's research craft, distilled from his papers, books, homepage essay, the 2014 Sloan oral history, his students' theses and published critiques, organised by the council's nine optimization domains. His lens: a decision someone owns, written exactly as an LP, conic or mixed-integer problem that stays in the solver class, priced with one knob, certified or given a gap, and judged against the owner's current rule. Use it to choose and gate problems, formulate, design and judge computational experiments, and plan research programmes. Triggers: "Bertsimas lens", "how would Bertsimas approach this", "use Bertsimas's method", "Bertsimas.skill", "用 Bertsimas 的视角", "Bertsimas 会怎么做". Also loaded by council-roundtable. For a discussion he leads with the LP, NLP, DFO and MINLP teams, use council-roundtable. Not Dimitri P. Bertsekas. Not for general questions.
type: research-craft
researched: 2026-10-28
---
```

**Earlier first-activation disclaimer** (verbatim):

```text
- State once, at first activation: *This is distilled from Bertsimas's public work (papers, books, homepage essay, the 2014 Sloan oral history, students' theses, published critiques), not Bertsimas's own advice; no full-text deep reading has been done yet.*
```

**Claim audit 2026-10-29, round 1** (earlier wording, verbatim):

SKILL.md, Corrections from the full texts (C7, not in the sample; narrowed with SKILL.md packet item k = 9, see [Method 3](#method-3)):

```text
- **C7** ⚠ Method 3 from 2004 → one knob from 1990 [S597 pp. 36–38]; knob-free precursor 1988 [S048 p. 29]; knobs from moments 2006, samples 2009 [S014 pp. 10–12; S024 p. 3].
```

`references/technique-catalog.md` (catalog packet of the same audit; the catalog links to no ledger anchor):

```text
| Many jobs of few types (job shop, packet routing) | fluid LP, solved in closed form | a schedule that tracks the fluid optimum, with an additive error | [S130 pp. 7–8; S205 pp. 9–11] |
| Two-stage or multistage adaptive RO | a sampled bound from binding scenarios, or a bound from the set's symmetry | a static, affine or polynomial policy priced against it | [S138 pp. 7–9; S134 pp. 6, 12–18; S075 pp. 7, 14–15] |
- **Price of a policy class with tight families.** How to use: bound the ratio of a static or affine policy to the adaptive optimum by a quantity of the set alone (symmetry, non-convexity), then build the family that attains it. Cards: [S134 pp. 6, 12–18; S176 pp. 13–14; S192 pp. 16, 18–19; S392 pp. 15–17].
- **Regime maps and phase transitions.** How to use: use the exact solver as an instrument across n, p, SNR and correlation; fit a when-to-use rule. Cards: [S061 pp. 4, 14–19; S355 pp. 4–5, 13–15; S170 pp. 5, 17, 20; S046 p. 19; S104 pp. 4, 25–27; S011 pp. 30–35].
```

Catalog packet items: k = 3, the closed-form fluid optimum is Proposition 2 and the additive error Theorem 4 [S205 pp. 7–11, 26–27]; k = 6, the polynomial policies are priced against the exact LP over all extreme disturbance sequences at small horizons, now named in the bound column [S075 pp. 7, 14–15]; k = 9, the static-versus-adaptive bound ρ_adapt (a scaling between the projection box and the coupled set), its tight instance and its comparison with the symmetry and non-convexity bounds are on pp. 21–23, while pp. 15–17 bound the coupled against the constraint-wise problem [S392 pp. 21–23]; k = 13 (flagged by the second auditor only), the routing card maps regimes by demand and pick-up window, now named beside n, p, SNR and correlation [S046 p. 19].

<a id="card-key"></a>
## Card key

**Counting rules** (08, header).
1. *One card per work.* 19 works have two cards: 18 were carded from the abstract in round 3 and read in full or in part in round 4 (S241, S275, S452, S487, S597, S636, S725, S745, S819, S836, S867, S872, S873, S905, S906, S907, S909, H001), and S181 was read in part in round 1 and in full in round 2. The deeper card is used.
2. *Version pairs count once* (first ID counted): S390 = S524 (npj Digit Med 2026 / arXiv 2507.00205); S561 = S412 (journal paper / shorter nonarchival version); S185 = S580 (Queueing Systems 1995 survey / the earlier and partly different 1994 working paper, still cited for its own sentences); S223 = S906 (IJOO 2023 / later manuscript). S926 is the LIDS-report version of S024. *Fix round*, pairs the cards themselves identify: S016 = S261 (OR 1991 / the 1989 working paper); S032 = S597 (OR 1993 / the August 1990 working paper); S340 = S197 (arXiv 2014 / the journal version); S328 = S914 (IJOC 2013 / an undated working paper with the same three authors and a close title, written 2007 or later: a probable pair). The second IDs are still cited for their own pages.
3. *Not his work*: S771 (a 2010 workshop page) is never cited as his.
4. *External evaluations, not his method*: in S063, S110, S021, S157 and S294 he is only a member of a forecasting consortium or hub team; they are used only as outside scoring of his group's DELPHI model.
5. *Reading notes are not findings*: card notes on typos, tables that disagree with a text or recomputed numbers are not used as claims about anyone.
6. *Stated* means stated in a text he signed; most texts are co-authored, and sole-author texts are marked where it matters.

**Versions read where they differ from the listed venue** (card headers): S010 is arXiv v1 (with the 200-billion figure); S089 the 1991 MIT preprint; S013 arXiv v2; S039, S042, S085 and S003 arXiv versions; S044, S077 and S098 preprints; S161 a technical report (cited as [S161 TR pp. …]); S186 and S448 working papers; S008 arXiv v4; S617 arXiv 2305.15629v1 of 2023 (cited as [S617 arXiv pp. …]; the 2026 article was not read); S669 arXiv 2405.07068v1. Journal-version changes of these works are not read. Many other cards also read a preprint, working-paper or arXiv file; each card header names its version.

**IDs cited in SKILL.md** (generated from the card digests; level = deepest card; batch = card file):

- S001 · The price of robustness (2004) · full · c07
- S002 · Introduction to linear optimization (1997) · abstract · a3-01
- S004 · Robust discrete optimization and network flows (2003) · full · c07
- S005 · Simulated annealing (1993) · full · c01
- S006 · Adaptive robust optimization for the security constrained unit commitment problem (2012) · full · c13
- S007 · Moment problems and semidefinite optimization (2000) · full · c05
- S008 · From predictive to prescriptive analytics (2020) · full · c21
- S009 · Optimal control of execution costs (1998) · full · c04
- S010 · Best subset selection via a modern optimization lens (2016) · full · c16
- S011 · Optimal classification trees (2017) · full · c17
- S012 · The price of fairness (2011) · full · c13
- S013 · Data-driven robust optimization (2018) · full · c18
- S014 · A robust optimization approach to inventory theory (2006) · full · c09
- S015 · The air traffic flow management problem with enroute capacities (1998) · full · c04
- S016 · A stochastic and dynamic vehicle routing problem in the Euclidean plane (1991) · full · c01
- S017 · A Vehicle Routing Problem with Stochastic Demand (1992) · full · c01
- S018 · Optimal inequalities in probability theory: A convex optimization approach (2005) · full · c08
- S020 · Optimization over integers (2005) · abstract · a3-02
- S021 · Evaluation of individual and ensemble probabilistic forecasts of COVID-19 mortality in… (2022) · full · c2-05
- S024 · Constructing uncertainty sets for robust linear optimization (2009) · full · c2-02
- S025 · A new generation of vehicle routing research: robust algorithms, addressing uncertainty (1996) · full · c04
- S027 · Robust and data-driven optimization: modern decision-making under uncertainty (2006) · full · c09
- S028 · Adaptive distributionally robust optimization (2019) · full · c2-03
- S031 · Shortfall as a risk measure: properties, optimization and applications (2004) · full · c08
- S032 · Stochastic and dynamic vehicle routing in the Euclidean plane with multiple capacitated… (1993) · full · c01
- S038 · A priori optimization (1990) · full · c01
- S040 · Algorithm for cardinality-constrained quadratic optimization (2009) · full · c12
- S042 · Optimality of affine policies in multistage robust optimization (2010) · full · c12
- S044 · Fairness, efficiency, and flexibility in organ allocation for kidney transplantation (2013) · full · c14
- S046 · Online vehicle routing: The edge of optimization in large-scale applications (2019) · full · c2-04
- S047 · Machine learning under a modern optimization lens (2019) · abstract · a3-03
- S048 · Probabilistic combinatorial optimization problems (1988) · full · b2-01
- S050 · Algorithmic prediction of health-care costs (2008) · full · c11
- S051 · Restless bandits, linear programming relaxations, and a primal-dual index heuristic (2000) · full · c06
- S052 · Survivable networks, linear programming relaxations and the parsimonious property (1993) · full · c02
- S053 · Models for minimax stochastic linear optimization problems with risk aversion (2010) · full · s07
- S054 · COVID-19 mortality risk assessment: An international multi-center study (2020) · full · c21
- S056 · On the relation between option and stock prices: a convex optimization approach (2002) · full · c06
- S057 · Conservation laws, extended polymatroids and multiarmed bandit problems; a polyhedral a… (1996) · full · c2-02
- S061 · Sparse high-dimensional regression: Exact scalable algorithms and phase transitions (2020) · full · c21
- S070 · An approximate dynamic programming approach to multidimensional knapsack problems (2002) · full · c07
- S072 · Optimization of multiclass queueing networks: Polyhedral and nonlinear characterization… (1994) · full · c2-01
- S073 · Classification and regression via integer optimization (2007) · full · c11
- S078 · An analytics approach to designing combination chemotherapy regimens for cancer (2016) · full · c17
- S081 · OR forum—an algorithmic approach to linear regression (2016) · full · c17
- S083 · Where to locate COVID‐19 mass vaccination facilities? (2022) · full · c24
- S084 · Robust and Adaptive Optimization (2022) · abstract · a3-04
- S085 · Characterization of the equivalence of robustification and regularization in linear and… (2018) · full · c19
- S089 · Computational approaches to stochastic vehicle routing problems (1995) · full · c03
- S090 · Robust optimization for unconstrained simulation-based problems (2010) · full · c2-02
- S091 · Stochastic and dynamic vehicle routing with general demand and interarrival time distri… (1993) · full · c02
- S093 · Exact first-choice product line optimization (2019) · full · c2-04
- S094 · Development and validation of an optimized prediction of mortality for candidates await… (2019) · full · s2-08
- S095 · Sparse Regression: Scalable Algorithms and Empirical Performance (2020) · full · c22
- S097 · Mixed-integer optimization with constraint learning (2025) · full · c29
- S105 · Logistic regression: From art to science (2017) · full · c18
- S112 · The voice of optimization (2021) · full · c23
- S114 · Equitable and efficient coordination in traffic flow management (2012) · full · c14
- S115 · Predicting inpatient flow at a major hospital using interpretable analytics (2022) · full · c25
- S119 · Robust queueing theory (2015) · full · c15
- S124 · The power of optimization over randomization in designing experiments involving small s… (2015) · full · c15
- S128 · Data, models, and decisions: The fundamentals of management science (2000) · abstract · a3-02
- S129 · The distributional Little's law and its applications (1995) · full · s2-02
- S130 · Asymptotically optimal algorithms for job shop scheduling and packet routing (1999) · full · s04
- S132 · Universal neurons in gpt2 language models (2024) · full · c28
- S134 · On the power of robust solutions in two-stage stochastic and adaptive optimization prob… (2010) · full · s07
- S137 · Optimizing schools' start time and bus routes (2019) · full · c2-04
- S138 · Duality in two-stage adaptive linear optimization: Faster computation and stronger bounds (2016) · full · s10
- S139 · Bootstrap robust prescriptive analytics (2022) · full · c25
- S141 · Robust optimization with simulated annealing (2010) · full · s07
- S168 · An analytic approach to a general class of G/G/s queueing systems (1990) · full · s2-01
- S175 · A unified approach to mixed-integer optimization problems with logical constraints (2021) · full · c23
- S176 · A tight characterization of the performance of static solutions in two-stage adjustable… (2015) · partial · s2-06
- S178 · Least quantile regression via modern optimization (2014) · full · s09
- S183 · Solving large-scale sparse PCA to certifiable (near) optimality (2022) · full · s2-14
- S184 · Certifiably optimal sparse principal component analysis (2019) · full · s2-09
- S185 · The achievable region method in the optimal control of queueing systems; formulations,… (1995) · full · c03
- S190 · Applied informatics decision support tool for mortality predictions in patients with ca… (2018) · full · s2-08
- S192 · On the performance of affine policies for two-stage adaptive optimization: a geometric… (2015) · full · s10
- S199 · The price of interpretability (2019) · full · c20
- S204 · Learning mixed-integer convex optimization strategies for robot planning and control (2020) · full · c22
- S205 · From fluid relaxations to practical algorithms for job shop scheduling: the makespan ob… (2002) · partial · s05
- S206 · OR Forum—Tenure Analytics: Models for Predicting Research Impact (2015) · full · s10
- S209 · The analytics edge (2016) · abstract · a3-03
- S225 · The trimmed lasso: Sparsity and robustness (2017) · partial · s11
- S239 · An exact FCFS waiting time analysis for a general class of G/G/s queueing systems (1988) · full · s01
- S255 · A semidefinite optimization approach to the steady-state analysis of queueing systems (2007) · full · s06
- S262 · Bus routing optimization helps Boston public schools design better policies (2020) · full · s2-11
- S269 · A technique for speeding up the solution of the Lagrangean dual (1994) · full · c02
- S283 · Robust convex optimization: A new perspective that unifies and extends (2023) · partial · s17
- S292 · Clinical benefit, toxicity and cost of metastatic breast cancer therapies: systematic r… (2019) · full · s2-09
- S310 · Simple Imputation Rules for Prediction with Missing Data: Contrasting Theoretical Guara… (2021) · full · s13
- S317 · Slowly varying regression under sparsity (2025) · full · c30
- S328 · A new local search algorithm for binary optimization (2013) · full · c2-03
- S334 · Queueing Theory: Classical and Modern Methods (2022) · abstract · a3-04
- S340 · A comparison of Monte Carlo tree search and mathematical optimization for large scale d… (2014) · full · c14
- S358 · Learning a mixture of gaussians via mixed-integer optimization (2019) · full · s2-10
- S368 · Bounds and policies for dynamic routing in loss networks (1999) · full · s05
- S426 · Efficient domain adaptation of multimodal embeddings using constrastive learning (2025) · full · c32
- S456 · Should We Relax Stability in Matching Markets? (2025) · full · c33
- S474 · RocketPFN: Accurate Time Series Classification via In-Context Learning (2026) · full · c36
- S476 · Modernizing the Design Process for US Organ Allocation Policy: Toward a Continuous Dist… (2025) · full · c2-07
- S480 · Interpretable algorithmic fairness in structured and unstructured data (2024) · full · s2-18
- S557 · Semi-supervised approach to predictive analysis using temporal data (2014) · full · s2-06
- S580 · A mathematical programming approach to stochastic optimization problems (1994) · full · s2-02
- S597 · Stochastic and Dynamic Vehicle Routing in the Euclidean Plane: The Multiple-Server, Cap… (1990) · full · a3-05, s4-02
- S614 · Fifty years of Robust Linear and Convex Optimization (2026) · abstract · a3-04
- S617 · Patient outcome predictions improve operations at Hartford HealthCare (2026) · full · c38
- S653 · An Optimization Approach to Credit Risk (2002) · partial · s05
- S681 · Optimal Control of Fluid Restless Multi-armed Bandits: A Machine Learning Approach (2026) · full · c42
- S685 · Can artificial intelligence deliver on the promise of precision medicine? (2025) · full · c2-07
- S695 · The Analytics Edge in Healthcare (2025) · abstract · a3-04
- S747 · Note on the Reformulation for Static Robust Problems for Convex Uncertainty Sets (2015) · full · s2-07
- S829 · A central limit theorem for the exodic tree and exodic matching in geometrical probabil… (1991) · full · s2-02
- S909 · Optimal Selection of Health Care Providers (2017) · full · a3-05, s4-03

*Tighten step (T3.7)*: the list above is the set cited before the cut; these IDs are now cited only in this ledger, with their pages, under **Moved at the tighten step**: S017, S025, S028, S042, S132, S134, S138, S168, S192, S205, S255, S292, S328, S358, S474, S829.

*Increment books-2026-10-29*: book-material IDs now cited in SKILL.md (generated from the card digests the same way; all book material, outside every say–do count; version pair B020 = S005, one work in two printings, S005 counted):

- B001 · Introduction to Linear Optimization (Bertsimas, Tsitsiklis; Athena Scientific 1997): P… (1997) · full · c5-01
- B003 · Introduction to Linear Optimization: errata sheet (last updated 7/5/2021), Athena Scie… (2021) · full · c5-03
- B004 · Introduction to Linear Optimization: title page and table of contents (library scan, T… (1997) · full · c5-01
- B005 · Review of Introduction to Linear Optimization by Motakuri V. Ramana, Optima 54 (June 1… (1997) · full · c5-01
- B006 · Optimization over Integers (Bertsimas, Weismantel; Dynamic Ideas 2005): publisher's bo… (2005) · full · c5-02
- B008 · Dimitris Bertsimas's own books pages: Published Books on dbertsim.mit.edu (2026) and B… (2026) · full · c5-04
- B009 · Machine Learning under a Modern Optimization Lens (Bertsimas, Dunn; Dynamic Ideas 2019… (2019) · full · c5-03
- B010 · Review of Machine Learning under a Modern Optimization Lens by Thibaut Cuvelier, devel… (2020) · full · c5-03
- B011 · Robust and Adaptive Optimization (Bertsimas, den Hertog; Dynamic Ideas 2022): publishe… (2022) · full · c5-04
- B013 · Queueing Theory: Classical and Modern Methods (Bertsimas, Gamarnik; Dynamic Ideas 2022… (2022) · full · c5-04
- B014 · Data, Models, and Decisions (Bertsimas, Freund; 2nd ed., Dynamic Ideas 2004): publishe… (2004) · full · c5-02
- B017 · The Analytics Edge (Bertsimas, O'Hair, Pulleyblank; Dynamic Ideas 2016): publisher's b… (2016) · full · c5-03
- B019 · The Analytics Edge in Healthcare (Bertsimas, Orfanoudaki, Wiberg; Dynamic Ideas 2025):… (2025) · full · c5-04
- B020 · Simulated Annealing (Bertsimas, Tsitsiklis), chapter 2 of Probability and Algorithms (… (1992) · full · c5-01
- B021 · Optimization Methods (MIT 15.093J, Fall 2009, instructor Dimitris Bertsimas): MIT Open… (2009) · full · c5-02

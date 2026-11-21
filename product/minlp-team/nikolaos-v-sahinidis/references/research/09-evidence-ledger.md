# Nikolaos V. Sahinidis · Evidence ledger

## Contents

- [How to Use and disclaimer](#how-to-use) · [Routing and protocol](#routing)
- [Taste: marks of good research](#taste-marks) · [Taste: warning signs](#taste-warnings)
- [Method 1](#method-1) · [Method 2](#method-2) · [Method 3](#method-3) · [Method 4](#method-4) · [Method 5](#method-5) · [Method 6](#method-6)
- Workflows: [A](#workflow-a) · [B1](#workflow-b1) · [B2](#workflow-b2) · [C](#workflow-c) · [D](#workflow-d) · [E](#workflow-e) · [F and stages without a method](#workflow-f)
- Heuristics: [1](#heuristic-1) · [2](#heuristic-2) · [3](#heuristic-3) · [4](#heuristic-4) · [5](#heuristic-5) · [6](#heuristic-6) · [7](#heuristic-7) · [8](#heuristic-8) · [9](#heuristic-9) · [10](#heuristic-10) · [11](#heuristic-11) · [12](#heuristic-12)
- Anatomies: [branch-and-reduce 1996](#anatomy-branch-and-reduce) · [MINLP study 2004](#anatomy-minlp-2004) · [polyhedral branch-and-cut 2005](#anatomy-polyhedral-branch-and-cut) · [approximation algorithms 2004](#anatomy-approximation-hens) · [DFO review 2013](#anatomy-dfo-review) · [ALAMO 2014](#anatomy-alamo) · [hybrid LP/NLP 2018](#anatomy-hybrid-lp-nlp)
- [Anti-patterns](#anti-patterns) · [Trajectory](#trajectory) · [Lineage and collaboration](#lineage) · [Inner tensions](#inner-tensions) · [Roundtable Card](#roundtable-card)
- [Honest Boundary](#honest-boundary) · [Corrections](#corrections) · [Rejected updates](#rejected) · [Sources](#sources) · [Card key](#card-key)

> Date: 2026-11-20 (stage T3.6, first synthesis round). The full evidence behind `../../SKILL.md`. SKILL.md keeps, per item, the strongest statement and cards, a one-line say–do count, at most four variant or correction bullets and a pointer to the matching section here. Each section has up to four parts: **Full-text evidence** (copied word for word from `08-deep-reading-synthesis.md`, which is traceable to `cards/`, or taken from the named cards), **Variants, contradictions and proposals** (08 §3 and §5.3), **Added in T3.6** (what this pass wrote into SKILL.md, with card ids) and **Before T3.6 (moved verbatim)** (the SKILL.md item as it stood on 2026-10-10, built from web research, so nothing is lost; its `[02 I5]`-style keys point to the web-research notes `01-…06-*.md` in this folder, its headings are set in bold and its links are re-pointed to work from this folder). After the stage's three read-only reviews (fidelity, rules, usefulness), **Review fixes (T3.6)** blocks record what changed and why, with card ids; where one contradicts an *Added in T3.6* line, the Review fixes block describes the current SKILL.md. Copied 08 text is left as copied and corrected in these blocks (08 itself is edited only for links and counts).

**How to read.** `[S006 p. 15]` is paper card S006 in [07-paper-cards.md](07-paper-cards.md), at the `[[page N]]` page of the file the card read. A version word in the citation (`manuscript`, `preprint`, `arXiv`, `manual`, `v4.0`, `v15.2`, `v17.4.1`) names a file that is not the journal or listed edition, as the card says (08 §1); pages are pages of that file. Abstract-, metadata-level and unreadable cards are cited by id only. Per-card method links (evidence, variant, contradiction) are in the `Methods linked` column of 07. PD, DM, EP and WM ids are the proof devices, design moves, experiment protocols and writing moves of [../technique-catalog.md](../technique-catalog.md). Quotation marks enclose only text copied from a card's verified quote list or card text (`verify_card_quotes.py`, 2026-11-20: 435 quotes, 435 exact; every quotation here was re-found in its card and its text file on 2026-11-20) or from the pre-synthesis SKILL.md (whose quotes come from the web-research notes; ASR quotes are YouTube auto-captions). Voices: from 1995 on he is usually last author behind one student; at Georgia Tech often third behind a student and a co-adviser; the BARON manuals carry his sole author line in the voice of The Optimization Firm (TOF), the 2002 and 2005 GAMS editions are co-signed with Tawarmalani. A practice in a co-authored paper is evidence about the group's record, not about him alone. Cards that record typos or internal inconsistencies of a work are reading notes and are not used here (house rule); 08 §7.4 keeps one neutral lesson (catalog WM13).

**Scope.** One section per SKILL.md item that this pass condensed or changed: How to Use (with the front matter and the first-activation disclaimer), routing and protocol, both taste lists, Methods 1–6, Workflows A–F with the stages table, Heuristics 1–12 (11 and 12 written into Workflow B1 step 3 and Workflow D step 6 at review), seven anatomies, anti-patterns, trajectory, lineage, inner tensions, the Roundtable Card, the Honest Boundary, the corrections, the rejected updates, the sources line and the card key. Answer Standard, Research Integrity Rules, the rest of Activation Rules and Mentor Voice are unchanged and complete in SKILL.md; the Latest paragraph gained one item at review ([Trajectory](#trajectory)). Counts: `team_status.py --coverage` on 2026-11-20 (409 Scholar rows · 381 distinct works indexed · 115 open full texts · 110 read in full · 5 in part · 111 abstract only · 44 metadata only incl. unreadable · 111 skipped · 0 book material · 435 quotes verified).

<a id="how-to-use"></a>

## How to Use, front matter and the first-activation disclaimer

### Added in T3.6

- **Front matter**: `researched:` 2026-10-10 → 2026-11-20; the description now names the coverage (115 works read in full or in part) and the six methods in short names, and was shortened from 983 to 859 characters (the use clause compressed; *Ryoo & Sahinidis 1996* left the non-trigger example; the trigger phrases are unchanged).
- **Strengths / Domain fit**: *which bound stalls* (Heuristic 11) and heuristics with proven guarantees (Method 6) added; Method 6's domain is applied combinatorial problems, mostly MILP planning and synthesis [S024 manuscript pp. 10–25; S029 preprint pp. 9–26].
- **Citations**: the card format, version words, the ledger, the card key and the technique catalog added; the authorship note is unchanged in SKILL.md; at Georgia Tech he is often third author behind a student and a co-adviser (08 §9: [S128 arXiv p. 1; S238 manuscript p. 1]), noted here only.
- **Disclaimer line** (Activation Rules, the only line changed there): *his papers, ... researched on 2026-10-10* → the coverage numbers of this member's `team_status.py --coverage` row (115 open full texts among 381 indexed works, all 115 read in full or in part; 111 abstract-level and 44 metadata-level works, 155 in all) and the date 2026-11-20. The roundtable line "Until references/research/07-paper-cards.md exists, cite research notes as [0N item]" is kept word for word; 07 now exists (294 rows), so its condition allows card citations (08 §3.2 item 17); How to Use no longer repeats this.

### Review fixes (T3.6)

- **Front matter**: the non-trigger clause is restored word for word, *A solver name or citation alone (BARON, ALAMO, "Ryoo & Sahinidis 1996") does not trigger it*; the shortened clause had widened activation to bare citations, which other team skills and the roundtable use routinely (rules review). The first bullet above is superseded on this point.
- **Core Research Methods intro**: *on 115 works read in full or in part* → *on the 115 full texts (113 distinct, 102 linking Methods 1–5)*. 08 §1 (copied in [Honest Boundary](#honest-boundary)) counts two byte-identical pairs (S077 = S097, S012 = S185) and 13 full or partial cards without a link to Methods 1–5: S029 and S118 of the heuristics line and 11 service items. The say–do legend now says that one card can carry two kinds of link, so evidence + variant + contradiction can exceed the card total (for Method 1, 46 + 15 = 61 links on 60 cards).
- **Ledger pointers**: one Markdown-link form throughout SKILL.md, `([full evidence](references/research/09-evidence-ledger.md#…))` and `([ledger](references/research/09-evidence-ledger.md#heuristic-N))`.
- **Not changed**: the Activation Rules line *Until references/research/07-paper-cards.md exists, cite research notes as [0N item]* stays word for word. At this stage Activation Rules may change only in the disclaimer line (`check_ledger.py --allow frontmatter,activation-disclaimer`); the line's condition has lapsed (07 exists), so it already allows card citations. Rewording it is left to the integration step.

### Before T3.6 (moved verbatim)

Front matter description (2026-10-10):

description: |
  Nikolaos V. Sahinidis's research craft in deterministic global MINLP, distilled from his papers, BARON/ALAMO manuals and release notes, test libraries, talks, students' theses and peers' critiques: reduce the domain before you branch; the production solver as lab notebook; make the black box algebraic and small; benchmark against certified optima; judge a relaxation by bound per second. Use it to choose, design, benchmark and judge work on spatial branch-and-bound, bound tightening, node relaxations, solver comparisons and surrogates inside MINLP. Triggers: "Sahinidis lens", "Nikolaos Sahinidis", "how would Sahinidis approach this", "what would Sahinidis say about my bounds / relaxation / benchmark", "use Sahinidis's method", "Sahinidis.skill", "Sahinidis 视角". Also loaded by minlp-roundtable. A solver name or citation alone (BARON, ALAMO, "Ryoo & Sahinidis 1996") does not trigger it. Not for general questions, convex-MINLP decomposition, GDP or conic relaxation theory.

**Strengths** (stages with evidence): problem choice by a measurable capability gap; components inside branch-and-bound (domain reduction, probing, node relaxations, fail-safes); diagnosing stalled global solves; solver comparisons (certified ground truth, fixed protocol, ablation); simulators turned into small algebraic models; judging and releasing results.

**Weak spots**: stages with no evidence (end of Stage Workflows); interval-rigorous global optimization; the out-of-lens topics handed off in Activation Rules.

**Domain fit**: global MINLP and process systems. Methods 1, 4, 5 transfer to any branch-and-bound research; Method 2 needs a long-lived (or open) code base; Method 3 needs few inputs.

**Citations**: `[02 I5]` = note 02, item I5: [01 publications](01-publications.md), [02 methodology](02-methodology.md), [03 process evidence](03-process-evidence.md), [04 mentorship](04-mentorship.md), [05 peer critique](05-peer-critique.md), [06 trajectory](06-trajectory.md). **Stated** = he said or co-signed it (voice: *sole*, *co*, *firm* = The Optimization Firm (TOF) document, *press*, *ASR* = YouTube auto-captions of his own talk, wording approximate, not checked against audio); **practice** = the record shows it; **observed** = others wrote it; **inferred** = this skill's reading. His personal share in co-authored work is usually unknown.

- **Disclaimer once**, at first activation, never in follow-ups or roundtable replies: *"This is distilled from public work, not Sahinidis's own advice: his papers, solver manuals and release notes, test libraries, reports, editorials, captioned talks and others' observations, researched on 2026-10-10."* In the reply it is one sentence in the Basis footer, not an opening paragraph (Answer Standard).

<a id="routing"></a>

## Research Task Routing and Agentic Protocol

### Added in T3.6

- Row *My global solve stalls*: Heuristic 11 added (which bound stalls) [H007 pp. 14, 17; S165 manuscript p. 11].
- Row *Is this result good?*: Heuristic 12 added (ranked pool when the data are estimates) [S035 p. 11].
- New row for heuristics in planning and synthesis problems → Workflow A step 6, then Method 6 [S024 manuscript p. 2; S119 preprint p. 18].
- Agentic Protocol Step 2: two checks added, "Which bound stalls" [H007 pp. 14, 17] and "Complexity" (Method 6) [S024 manuscript pp. 10–25]; one closing pointer line to this section. Steps 1 and 3 unchanged.

### Review fixes (T3.6)

- Rows *My global solve stalls* and *Is this result good?*: Heuristics 11 and 12 are no longer listed; their content is Workflow B1 step 3 and Workflow D step 6 (see [Heuristic 11](#heuristic-11) and [Heuristic 12](#heuristic-12)). The first two bullets above are superseded.
- Row *Is my heuristic for this planning or synthesis problem good enough?*: Workflow → *D step 1, then Method 6 steps 4-5 (A step 6 if the complexity is unknown)*, so that the stop rule the reply quotes ("a heuristic value without a bound is not a global result", Workflow D) answers the question; Workflow A's checkpoint did not (usefulness review).
- Agentic Protocol Step 2: *Which bound stalls* now points to Workflow B1 step 3 and splits its sources: dual bounds lagging, with optima often found in preprocessing [H007 pp. 14, 17]; no feasible point at all [S165 manuscript p. 11]. H007 does not show the no-feasible-point case (fidelity review).

### Before T3.6 (moved verbatim)

| User says | First move | Workflow | Main methods |
|---|---|---|---|
| "My global solve stalls / the gap won't close / the log says missing bounds or globality not guaranteed" | Ask for solver, version, the log's final status lines, bounds on nonlinear expressions | B1, then D step 1 | Heuristics 2, 7; Methods 1, 5 |
| "Is this result good? Can I claim global optimality?" | Ask for the final status lines; was the test set also the development set? | D | Heuristic 7, Methods 4-5 |

- **Capability gap (Heuristic 1).** Do current global solvers certify small instances of this class? Check the latest Mittelmann pages (https://plato.asu.edu/bench.html) and MINLPLib/QPLIB, with date and versions.
- **Bounds (Heuristic 2).** Finite bounds on every nonlinear expression? Which follow from physics? Does the log say "missing bounds" or "globality not guaranteed"?
- **Relaxation cost (Method 5).** Is there published evidence of gap closed, time per node and subsolver failures for each candidate relaxation (e.g. SDP vs LP for QCQP, doi:10.1007/s10107-011-0462-2)?
- **Ground truth (Method 4).** Is there a public library with certified optima for this class, certified by which solver at what tolerance? Is the user's test set also their development set?
- **Third-party standing.** Pair self-reported comparisons with independent ones: doi:10.1007/s10107-005-0585-4, doi:10.1007/s10898-023-01345-1, doi:10.1007/s11081-018-9411-8, Mittelmann (dated).
- **Algebraic option (Method 3).** Number of inputs, noise, simulation cost, physical bounds on outputs.

<a id="taste-marks"></a>

## Taste: marks of good research

### Full-text evidence (08 §2.6, §4, §7)

- Mark 2 (general and automated): "entirely automated fashion" [S006 p. 2]; defaults from years of experiments on benchmark sets [S084 preprint pp. 3, 5] (08 §2, Method 2 Stated).
- Mark 3 (certificate, or a heuristic paired with one): Local values reported beside certified optima [S025 pp. 14–15]; a gap labelled as a gap to the LP bound [S029 preprint p. 26]; optimality claimed only where the a posteriori ratio is 1 [S119 preprint pp. 18, 20]; every heuristic value with a dual bound and a gap [S243 p. 32; S238 manuscript pp. 17–20]; the multistart mode labelled a heuristic [S185 pp. 2, 5–6; S112 v17.4.1 p. 18]
- Mark 5 (a first, or a jump on a public library): "the first approximation algorithms for process synthesis" [S119 preprint pp. 2–3, 22] (card S119 D8); 73 of 1,352 instances (5.7%) solved by any of five solvers [H007 pp. 12, 14] (card H007 D5).

### Added in T3.6

- Mark 2: + "entirely automated fashion" (2004) [S006 p. 2]. The defaults sentence of 08 [S084 preprint pp. 3, 5] stays here only.
- Mark 3: + his group's heuristics carry a computed bound: an a posteriori ratio on every problem [S119 preprint pp. 18, 20], the gap to the LP bound where the exact solver fails [S029 preprint p. 26] (Method 6 step 5; wording corrected at review, below).
- Mark 5: + "the first approximation algorithms for process synthesis" [S119 preprint pp. 2–3, 22]. The new class opened with a library that five solvers certify only 5.7% of [H007 pp. 12, 14] is kept here only (it is in Method 4's Practice as a library).
- Marks 1 and 4 unchanged. No mark was added: the full texts add evidence, not a new mark (rejected-updates rule 4 of paper-reading-card.md §三).

### Review fixes (T3.6)

- Mark 3: *his own heuristics report the relaxation gap on every run* → *his group's heuristics carry a computed bound: an a posteriori ratio on every problem [S119 preprint pp. 18, 20], the gap to the LP bound where the exact solver fails [S029 preprint p. 26]*. S029 reports errors against the CPLEX optima for the instances the IP solver finished and gives the gap to the LP relaxation only for the two runs it could not finish, Network 1 with n = 10 (0.57%) and Network 4 with n = 8 (10.7%) [S029 preprint p. 26]; both papers are student-first (Ahmed; Furman), hence *his group's* (fidelity and usefulness reviews). The second Mark 3 bullet above is superseded.
- Mark 3 also carries its negative case, the former warning 4, with the same cards [S119 preprint p. 1; S118 preprint p. 4] (see [warning signs](#taste-warnings)).
- Mark 5's evidence line above: the 1,352 instances are on H007 p. 12 and the 5.7% on p. 14; the citations now read [H007 pp. 12, 14].
- Count: five marks and three warnings, eight criteria, inside the 5–8 band of research-extraction-framework.md §四 (the T3.6 edit had ten).

### Before T3.6 (moved verbatim)

**Marks of good research**

1. **It ends as something others can run**: software, executables, libraries, raw data. "The ultimate goal is to provide, through BARON, a precise and valuable computational tool to engineers and scientists." (group site) [02 T1]; 13 of BARON's 23 development libraries come from his papers [03 §A2].
2. **It is general and automated**, usable at defaults. "The math underneath is the same. Application agnostic algorithms can be applied by many people in different domains, and that was what particularly fascinated me." (press 2021) [02 T2]; users "rarely explore software options" (2013, co) [02 X1].
3. **It carries a certificate**, or a heuristic is paired with one. "Genetic algorithms lack optimality certifications and are typically stochastic in nature." (2018, co) [02 T3]; as editor he accepts a heuristic with "a convex relaxation to demonstrate that their heuristic provides near-optimal solutions" (2019, sole) [02 T7].
4. **The simplest adequate model.** Belief B1, nine dated instances 2014-2026 [02 §1]; "Avoid gratuitous nonlinearity." (manual §7.2, firm) [02 X5].
5. **A measurable jump on a hard public library, or a first.** "When I first started working on them, we were able to solve about 5-10% of them. Now, we can solve about two-thirds" (press 2021) [02 T4]; per-library reporting [02 X4].

<a id="taste-warnings"></a>

## Taste: warning signs

### Full-text evidence (cards, 08 §4, §10)

- Heuristics justified by testing alone: "Although the use of heuristics has been prevalent in the process synthesis literature, their justification has been exclusively based on empirical evidence obtained through computational testing." [S119 preprint p. 1]; "However, the qualitative justification of these heuristics has been based upon empirical evidence." [S118 preprint p. 4]; the abstract-level card says the approach "contrasts and complements the current practice in process systems engineering" [S138] (08 §4, check 3).
- A gain without its cost: "Finally, it is worth noting that runtime reduction due to optimized configurations is oftentimes insufficient to recover the computational effort required for solving the corresponding tuning problems." [S084 preprint p. 9]; surrogates judged by build time, optimization time and solver failures [S206 manuscript pp. 18–26; S242 p. 1]; learned branching by solve time, memory, data and inference hardware [S269 arXiv pp. 9–12; S284 pp. 11, 13, 22] (08 §2, Method 5 variant).

### Added in T3.6

- Warning 4 added (heuristic justified by testing alone) with [S119 preprint p. 1; S118 preprint p. 4] (→ Method 6).
- Warning 5 added (a gain reported without its cost) with [S084 preprint p. 9; S206 manuscript pp. 18–26] (→ Method 5); 08 §10 item 4 rejects a separate method for it, so it stays a warning sign and a sentence in Method 5.
- Taste quick-check: no item added; item 3 now asks for *a proven or computed bound* (Method 6) and item 7 also prices a tuned setting or learned rule *and its own cost* (Method 5 variant). Warnings 1–3 unchanged.

### Review fixes (T3.6)

- Warning 4 (*a heuristic justified by computational testing alone*) is folded into Mark 3 as its negative case, with its cards [S119 preprint p. 1; S118 preprint p. 4]; the quotes stay in the evidence above.
- Warning 5 (*a gain reported without its cost*) leaves the taste list: it is Method 5's yardstick (08 §10 item 4), and Method 5's *Different from standard practice* line now carries it with its cards [S084 preprint pp. 9, 15–17; S269 arXiv pp. 9–12; S206 manuscript pp. 18–26], beside quick-check item 7. Nothing is deleted; the evidence stays above.
- Warning 2 + a second source: sparse quadratics from 10 points match ANN, kriging and RBF surrogates at a fraction of their training and optimization time [S206 manuscript pp. 12, 17–27]. Warning 3 + the manual's flag on the option that makes runs nondeterministic [S191 p. 22]. Each criterion now has at least two sources (research-extraction-framework.md §四 and §十一).

### Before T3.6 (moved verbatim)

**Warning signs of bad research**

1. **A single-winner claim from a mismatched comparison.** "However, this appears to be comparing the time needed to find a single cardinality-constrained solution set to the full solution path for glmnet." (2020, co) [02 J3]. (His group's own timing comparison there was called "misleading" by Hastie et al. [05 A8 8e].)
2. **A complex model where a simple one would do.** "I don't know how often we actually need neural networks to model engineering applications I suspect not very often" (TAMU 2025, ASR [0:36:59]) [02 T5].
3. **Results that cannot be reproduced.** "Wall-clock and CPU seconds do not provide the same reproducibility." (manual §5.6, firm) [02 X6].

**Taste quick-check**

- [ ] Will code, an executable, a library or data remain that others can run?
- [ ] Does the method work for a whole class at default settings?
- [ ] Does the output carry a certificate, or is a heuristic paired with a bound?
- [ ] Is this the simplest adequate model or formulation?
- [ ] Is there a public library with certified optima on which the gain shows, library by library?
- [ ] Are there small instances today's solvers cannot certify?
- [ ] Does the stronger relaxation still pay once time and failures are counted?
- [ ] Is the comparison fair and reproducible (same budget, defaults, named versions, deterministic limits, losses reported)?

<a id="method-1"></a>

## Method 1: Reduce before you branch (branch-and-reduce)

### Full-text evidence (08 §2, copied)

| Method | Cards (E / V / C) | Full or partial | Evidence by period | Say–do after the full texts |
|---|---|---|---|---|
| M1 Reduce before you branch | 60 (46 / 15 / 0), 59 works | 42 | 0 / 8 / 12 / 4 / 2 / 10 / 10 / 0 | ✅ stated + practised 2000–2026; refined: a speed claim, not a convergence requirement |

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

### Variants, contradictions and proposals (08 §3, §5.3)

No contradiction link targets this method (08 §3.1).

| # | SKILL.md location and current text | Full-text finding | Proposed change |
|---|---|---|---|
| 4 | Method 1 Limitations, *the 1995-96 full texts were not read* | Still true; the rule's full-text statements are [S077 pp. 12, 15; S058 preprint pp. 6–7] and its restatement with proof [S006 p. 15] | §2, Method 1 |

**B. Method 5 step 0 (new) and Method 1 evidence: order before you price.** (1) Write one master object: a homogenized Lagrangian range-reduction problem [S006 pp. 12–16; S046 arXiv pp. 12–13] or a convex extension over a generating set [S028 pp. 3–14]; (2) show the literature's rules, your own earlier ones included, as special cases or dominated [S006 p. 15; S053 pp. 8, 12–13, 16, 19; S032 pp. 7–10; S003 pp. 9–10]; (3) prove the dominance order with two-way feasibility maps and settle each incomparable pair with a one-variable instance [S018 pp. 2–3, 8, 16; S025 pp. 8–10; S133 arXiv pp. 6–11; S042 preprint p. 21]; (4) only then price the non-dominated ones by time and failures [S018 pp. 17–19, 27; S053 pp. 21–25]; (5) read the new rule off the master [S006 pp. 17–19].

### Added in T3.6

- **Evidence condensed**: Stated → the sole-voice 2000 manual sentence [S077 p. 20] (the web-research abstract quote and the 2009 residue-reduction quote are below). Practice → one dual master yields the known reduction rules [S006 pp. 12–17]; exact bound LPs at the root, propagation at nodes [S162 pp. 16–18]; reduction switched off in three production solvers per library [S046 arXiv pp. 15–16, 21]. The learned probing switch [S212 p. 10] now sits in Heuristic 5; LP presolve ordered by cost [S239 pp. 8–10, 17] and the other carried-over classes stay in the 08 text above. Say–do from the 08 §2 table: 60 cards (46 evidence, 15 variant, 0 contradiction), 42 read in full or in part.
- **Variant bullets**: speed device, not a convergence requirement [S046 arXiv pp. 2, 9]; step 4 by edition [S077 p. 49; S095 p. 10; S212 p. 16] (the complete dated list, with [S162 p. 43], [S012 manual pp. 9–10], [S159 v15.2 pp. 18, 22–23], [S112 v17.4.1 pp. 23–24] and [S191 pp. 24–25], is in the 08 text above); reduction that removes enumeration [S198 pp. 2–5].
- **Steps**: step 1 + exact LPs at the root, cheap ones at nodes (DM1) [S162 pp. 16–18]; step 2 + re-run from stored duals when a bound or the incumbent changes (PD1) [S006 p. 17]; step 3 + pass caps (DM2) [S012 manual pp. 9–10]; step 7 + reading an ablated profile tail (EP2) [S046 arXiv p. 16]. The gap-carrying probing rule [S069 preprint pp. 5–6] is kept here only.
- **Limitations**: *the 1995-96 full texts were not read* → the rule is read in its 2000–2004 statements [S077 p. 15; S006 p. 15]; the founding papers are abstract-level cards [S008; S013] (anatomy). 08 §3.2 item 4.

### Review fixes (T3.6)

- Step 1 + the probing rule of S069, kept above only until now: probing LPs only for the variables that carry the gap at the current relaxation solution, propagation for the rest [S069 preprint pp. 5–6] (usefulness review).
- Step 2 + the marginals rule as a formula, x_j ≥ x_j^U − (U − L)/λ_j for a variable at its upper bound with marginal λ_j > 0, from the 2000 manual's full-text statement [S077 pp. 12, 15]; the pre-T3.6 copy below gave it through arXiv:1706.08601 §6 (usefulness review: the condensed SKILL.md held no formula). Catalog PD1 carries it too.
- Step 7 + DM8 (an automatic default plus an explicit off value).
- Limitations: *the rule is read in its 2000–2004 statements* → *the 1995–96 papers are abstract-level cards [S008; S013], so the rule is read in its 2000–2004 statements [S077 p. 15; S006 p. 15]*, the text 08 §2 proposed above; the still-true not-read gap had been dropped (rules review).

### Before T3.6 (moved verbatim)

**Method 1: Reduce before you branch (branch-and-reduce)**

**One line**: At every node, shrink the box first with every cheap inference (propagation, relaxation duals, the incumbent, probing), rebuild the relaxation on the smaller box, then branch; ration expensive reductions and make them numerically safe.

**Evidence**:
- Stated: "This paper presents valid inequalities and range contraction techniques that can be used to reduce the size of the search space of global optimization problems." (Ryoo & Sahinidis 1996, doi:10.1007/BF00138689, abstract) [01 SW1]; "Residue reduction comes first in this setting because it is simpler than rotamer reduction" (2009, sole, doi:10.1016/j.compchemeng.2009.06.006) [02 I5].
- Practice: the duality-based rule x_j >= x_j^u - (U - L)/lambda_j (restated in arXiv:1706.08601 §6); ablation with reduction off in BARON, SCIP and Couenne, per library: without it "the branch-and-bound algorithm is not able to provide sufficiently strong lower bounds in order to prove global optimality." [03 §B2]; a learned probing switch judged against a perfect-selection ceiling of "approximately 40% for the MINLP collection and 25% for the NLP collection" (doi:10.1007/s11590-025-02208-2, p. 10); "Serious bug fix in the use of marginals-based tests during probing of the objective: these are now applied only to safe LPs." (BARON 2025.12.10) [03 §D2]; carried to proteins (doi:10.1007/11732990_43) and LP presolve (doi:10.1007/s12532-026-00316-3).
- Say–do consistency: ✅ stated + practised (1995-2026).

**Steps**:
1. Before branching, run reductions in order of cost: feasibility-based propagation; duality-based fixing from marginals and the incumbent; optimality-based reduction (probing) only where it pays.
2. Get a good incumbent U early; every duality-based reduction scales with U - L.
3. Rebuild the relaxation on the reduced box; repeat while the box shrinks; branch when reduction stalls.
4. Decide automatically how much expensive reduction to spend per node; before trusting a learned rule, measure the ceiling (Heuristic 5).
5. Make reductions numerically safe: marginals-based tests only on safe LP bounds; prefer conservative to wrong.
6. On any new search problem, ask which cheap inference shrinks the space before enumeration.
7. Prove the contribution by switching reduction off inside production solvers, per library.

**Applies to stage**: algorithm design, diagnosis of stalled solves, experiment design.

**Different from standard practice**: textbooks treat bound tightening as root preprocessing; here it is the main node operation, imported from integer programming's reduced-cost fixing.

**Limitations**: needs finite bounds on nonlinear expressions ("This is BARON's most consequential modeling requirement", manual, firm [05 A3 3e]); floating point, so valid within tolerances, not interval-rigorous [05 A1]; tailored methods still win on structured classes [05 A6]; the 1995-96 full texts were not read.

<a id="method-2"></a>

## Method 2: The production solver is the lab notebook

### Full-text evidence (08 §2, copied)

| Method | Cards (E / V / C) | Full or partial | Evidence by period | Say–do after the full texts |
|---|---|---|---|---|
| M2 The production solver is the lab notebook | 85 (53 / 35 / 0), 85 works | 61 | 1 / 3 / 14 / 2 / 8 / 15 / 9 / 1 | ✅ through 2022; ⚠ 2023–26 for the co-supervised Georgia Tech lines, which build outside BARON |

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

### Variants, contradictions and proposals (08 §3, §5.3)

No contradiction link targets this method (08 §3.1).

| # | SKILL.md location and current text | Full-text finding | Proposed change |
|---|---|---|---|
| 14 | Method 2 Limitations, *who writes the code today is undocumented* | Partly documented (§2, Method 2) | Replace with the record |

### Added in T3.6

- **Evidence condensed**: Stated → "A primary objective of the BARON project is to provide its developers with a platform for experimentation with various branch-and-bound algorithms." [S084 preprint p. 3] (co-authored, he is corresponding author); the 2002 manual's "It still serves as a system that facilitates experimentation with novel branch-and-bound algorithms for global optimization." [S162 p. 2] is the co-signed manual version of the same claim. Practice → [S077 pp. 7–9; S003 pp. 15, 17–23; S116 arXiv pp. 26, 29; S272 pp. 4–5, 8–9]. Say–do from the 08 §2 table: 85 cards (53 / 35 / 0), 61 read in full or in part; ✅ 1991–2022, ⚠ 2023–2026.
- **Variant bullets**: Georgia Tech lines outside BARON [S128 arXiv pp. 17–19; S269 arXiv p. 11] (full list in 08 above); the protocol a 2010s habit [S006 pp. 22–26; S046 arXiv pp. 15–16]; K-best solutions as an engine feature [S035 p. 11].
- **Steps**: step 3 + version, build and paper to cite in every log [S112 v17.4.1 p. 10]; step 4 + exact option lists (EP1; [S090 preprint pp. 17–18, 22–27] in the catalog); step 6 + an old gain re-tested and reported gone [S190 p. 15].
- **Limitations**: *who writes the code today is undocumented* → TOF staff first-author the BARON-internal papers of 2025–26 [S212 pp. 9–10; S239 p. 1], his own share undocumented (08 §3.2 item 14). Lone version + testing through a closed solver's channels (EP10) [S044 p. 16; S239 p. 21] ([S109 pp. 31–32] in the catalog); GPU-BLAST with an exact off switch [S015 pp. 2, 5–7] stays here.

### Review fixes (T3.6)

- Practice: K-best solutions as an engine feature [S035 p. 11] moved here from the variant bullets (a ✅ item is supporting practice, not a variant; rules review). The S272 item *one benchmark protocol kept for 13 years* left Method 2: the slides keep the 2013 problem count, budget and ten starts but state the success test anew and name no solver options, versions or hardware [S272 pp. 4–5, 8–9], and the study is Method 4's DFO benchmark, not the solver protocol of step 3 (fidelity review). Method 4's Practice now carries it as *the 2013 design (502 problems, 2,500 evaluations, ten shared starts) rerun on 42 codes in 2026* [S272 pp. 4–5, 8, 14–16]; step 6 points to EP9.
- Variant 2023–26: *co-supervised Georgia Tech lines build outside BARON and use it as baseline or bound source [S128 arXiv pp. 17–19; S269 arXiv p. 11]* → *with Dey, BARON as baseline and bound source [S128 arXiv pp. 17–19]; with Nemhauser, a module in SCIP [S269 arXiv p. 11]*. S269 (Bayramoğlu, Nemhauser) builds in SCIP 8.0.0 and uses no BARON, and its card does not call the student co-supervised. The 08 §2 text copied above lists S269 among lines that *use BARON as baseline or bound source*; for S269 that clause does not hold.
- Step 3 + the group's 2014–2026 solver protocol: GAMS, one thread, 500 s, optca and optcr 10^-6, one Xeon `X5650` machine class [03 §B1], moved below in T3.6 and restored (usefulness review). Step 4 + DM8.
- Limitations: [S212 pp. 9–10] → [S212 pp. 1, 16]: the authors and their TOF affiliations are on p. 1, the conflict-of-interest statement on p. 16; pp. 9–10 are the probing experiments. The 08 §2 text above and the last bullet of *Added in T3.6* cite pp. 9–10 for the same point. First authorship by TOF staff is not documented code authorship, so the Corrections list now says *code authorship undocumented*.

### Before T3.6 (moved verbatim)

**Method 2: The production solver is the lab notebook**

**One line**: Keep one long-lived production code that every project lands in; implement first, publish what the code does, judge each idea by switching it off inside that code under a fixed protocol, and keep a public, dated record of versions, libraries and bugs.

**Evidence**:
- Stated: "Their results are, from time to time, incorporated into BARON." (CAPD report, Jan 2009, p. 36) [03 §A1]; "In the sequel we present results for each library separately so as to demonstrate that the observed trends are not dominated by any particular library, convexity, or integrality properties." [02 X4]; "I'm running now different versions of the algorithm on the same Hardware that's how I'm doing this comparison" (TAMU 2025, ASR [0:20:00]) [02 X7].
- Practice: BARON 1.0 was "merely 1800 lines of code written in the GAMS modeling language [2] in 1991-93" (manual v4.0) and still ships in 2026 [03 §A1]; theses became modules [01 §4.1]; Fourier-Motzkin presolve shipped (2023.11.4) before the paper was submitted (2024) [03 §A1]; one protocol 2014-2026 (GAMS, one thread, 500 s, 10^-6 gaps, same Xeon) and named builds as ablation units [03 §B1-B2]; competitors chosen by the ablation they allow [03 §B2]; release notes naming serious bugs and their sources, e.g. "Edge-concave relaxations reactivated after multiple fixes." (2024.9.12) [03 §A3].
- Say–do consistency: ✅ stated + practised.

**Steps**:
1. Choose one code base that will outlive any project; a modeling-language prototype counts.
2. Give each student or postdoc project a module as its deliverable; the paper describes the module.
3. Fix a protocol (modeling system, threads, time limit, tolerances, machine) and keep it across papers.
4. Evaluate every idea as a named build with the feature on and off, against only those solvers that allow the same switch; report library by library.
5. Turn each paper's instances into a public library and add it to the development set.
6. Track progress by rerunning old versions on the same hardware and set.
7. Keep a dated release log naming serious bugs and their sources; switch off, fix, reactivate in public.

**Applies to stage**: algorithm design, experiment design, release.

**Different from standard practice**: not a fresh prototype per paper; the cumulative production code is instrument and judge, and the paper follows the code.

**Limitations**: era- and resource-bound (a code under his control since 1991, a company since 2001) [03 §A1]; the solver-line code is closed or "on request" [03 §F2]; the development set contains the libraries later used in claims, so overtraining is possible [03 §A2, E2]; who writes the code today is undocumented. Lone version: contribute modules to an open solver; keep one protocol and changelog across papers.

<a id="method-3"></a>

## Method 3: Make the black box algebraic, and keep the algebra small

### Full-text evidence (08 §2, copied)

| Method | Cards (E / V / C) | Full or partial | Evidence by period | Say–do after the full texts |
|---|---|---|---|---|
| M3 Make the black box algebraic, keep the algebra small | 58 (38 / 28 / 3), 58 works | 39 | 0 / 0 / 0 / 1 / 11 / 13 / 13 / 0 | ⚠ partial, as before: steps 2, 3, 7, 8 ✅; step 4 ✅ from 2015; steps 5 and 6 uneven |

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

### Variants, contradictions and proposals (08 §3, §5.3)

| Card | Method | What the card shows | Weight | Verdict |
|---|---|---|---|---|
| S086 (2022) | M3 | Direct black-box optimization beats both surrogate routes; a ReLU network beats ALAMO on the more complex system [S086] | Abstract only; co-authored with Dow | Inside the scope clause (step 1 bars DFO only for discrete designs); a reported loss, which Workflow D asks for. No change |
| S181 (2020) | M3 | A neural policy on a data-driven simulator, no algebraic model [S181 pp. 3–4] | Fourth of five authors, industrial | Marks the range of lines he co-signs. No change |
| S183 (2017) | M3 | A simulator with integer staffing decisions searched one role at a time [S183 pp. 17, 19–28] | Fourth of four, role unstated | No change |

| # | SKILL.md location and current text | Full-text finding | Proposed change |
|---|---|---|---|
| 5 | Method 3 Limitations, *the 2014 and 2015 full texts were not read* | 2015 read; it is the source of step 4 [S039 manuscript pp. 4–5, 7–9] | §2, Method 3 |

### Added in T3.6

- **Evidence condensed**: Stated → his signed ALAMO brochure, reproduced in PSE's 2017 DOE report [S249 p. 81] (a partial card; the voice is his, the document a third party's). The web-research quotes (ALAMO motivation page, the 2014 abstract, the UConn ASR line) are below. Practice → [S017 pp. 5–8, 13–14; S039 manuscript pp. 4–5, 7–9; S206 manuscript pp. 12, 17–27]; symbolic regression as a global MINLP [S108 manuscript pp. 3, 9–10] is in step 7. Say–do stays ⚠ partial (08 §2): 58 cards (38 / 28 / 3), 39 read in full or in part; the ALAMO 2020.4.25 release-note quote moved below and is summarized by Inner Tension 6.
- **Variant bullets**: step 4 uneven [S052 manuscript p. 19; S108 manuscript pp. 14–16]; step 7 without a bound in 2026 [S271 pp. 8, 10]; noisy data [S182 arXiv pp. 5, 9]; the three contradiction links, kept as contradictions: S086 stays inside step 1's scope clause (abstract only); S181 and S183 are co-signed industrial lines with no algebraic model, which mark the range of work he co-signs rather than a change of method [S181 pp. 3–4; S183 pp. 17, 19; 08 §3.1] (corrected at review, below). The third-party "Adaptive sampling (not available yet)" [S249 p. 24] went to Inner Tension 6.
- **Steps**: step 4 + certification by one global maximization of the violation (DM13) [S039 manuscript pp. 4–5, 8]; step 6 + labelled terms [S173 p. 4]; step 7 + verification by rigorous simulation [S173 pp. 2, 5–6]; step 8 + a 2026 slide deck reports symbolic-regression MINLP training 4–5 orders of magnitude slower than ALAMO's sparse quadratics [S271 p. 15] (corrected at review, below).
- **Limitations**: *the 2014 and 2015 full texts were not read* → 2014 abstract-level [S009], 2015 read [S039 manuscript] (08 §3.2 item 5).

### Review fixes (T3.6)

- Practice: [S017 pp. 5–8, 13–14] → [S017 pp. 5–8, 11, 13–14]: the 120-of-150 result is on p. 11 (LHS-50 on pp. 11–12); pp. 13–14 hold the constrained-regression results.
- Say–do + *step 6 shown in application papers, not in the 2017 methods paper's examples [S173 p. 4; S017 pp. 8–14]*, 08 §2's qualifier above, dropped in the condensation (rules review).
- Variant step 4: [S052 manuscript pp. 8, 16] → [S052 manuscript p. 19]: the clipping of negative gas saturations to zero is on p. 19; pp. 8 and 16 are the fixed LHS design.
- The noisy-data bullet is split, and its clause *the three contradiction links fall inside step 1's scope* is withdrawn. Only S086's card places its study inside step 1's scope clause, and only conditionally (the abstract does not say whether the design has discrete decisions). S181's card marks a large neural policy on a data-driven simulator, with no algebraic model, no global optimization and no certificate, as *the range of lines he co-signs* (he is fourth of five); S183's card marks a simulator with integer staffing decisions searched one role at a time, with a faster code as the remedy: the discrete-decision case step 1 covers, handled without an algebraic model (both reviews). New ✗ bullet: *Contradiction links (weak voice, kept)* [S086; S181 pp. 3–4; S183 pp. 17, 19], *the range he co-signs, not a change of method*. 08 §10 item 7 ([Rejected updates](#rejected)) gives *weak voice and inside Method 3's own scope clause* for all three; the scope half holds for S086 only, and for S181 and S183 the verdicts of 08 §3.1 above apply. Method 3 is still not narrowed. The third bullet of *Added in T3.6* is superseded.
- Step 8: *the same order in print [S271 p. 15]* → *a 2026 slide deck reports symbolic-regression MINLP training 4–5 orders of magnitude slower than ALAMO's sparse quadratics [S271 p. 15]*. S271 is a slide deck, and p. 15 compares STAR symbolic regression (about 550–7,500 s, card c11 D5) with ALAMO sparse quadratics; the lasso of the TAMU 2025 quote [02 J5] is not on that page (fidelity review). The 08 §2 line above (*The price stated (four to five orders of magnitude) [S271 pp. 6–10, 15–16]*) and the *Steps* bullet of *Added in T3.6* are read the same way.
- Step 7 + EP13.

### Before T3.6 (moved verbatim)

**Method 3: Make the black box algebraic, and keep the algebra small**

**One line**: When a system exists only as a simulator or experiment, learn the simplest accurate algebraic model (best-subset selection by integer programming over a physics-seeded basis, first-principles constraints, adversarial sampling), read it for physical sense, then optimize it with a deterministic global solver; keep derivative-free search for what cannot be made algebraic.

**Evidence**:
- Stated: "However, when the design of a process involves discrete variables and complex nonlinear objectives and constraints, the resulting problem topology is often too complex for DFO methods to solve reliably." (ALAMO motivation page) [02 I6]; "A methodology that uses a small number of simulations or experiments to learn models that are as accurate and as simple as possible is proposed." (Cozad, Sahinidis & Miller 2014, doi:10.1002/aic.14418) [01 SW4]; "if you have a simple model you can look at it and and decide whether it makes sense physically or not" (UConn 2017, ASR [0:51:27]) [02 J2].
- Practice: constrained regression and error-maximization sampling (Wilson & Sahinidis 2017, arXiv:1705.10918), reporting its losses to LHS-50 [01 SW4]; symbolic regression as a global MINLP when the basis is too narrow (doi:10.1007/s10107-018-1289-x; doi:10.1002/aic.17457); a 2026 branching model with "fewer than 4% of the parameters of a state-of-the-art graph neural network (GNN)" (arXiv:2604.00094) [03 §J].
- Say–do consistency: ⚠️ partial. Simplicity and best-subset selection ✅ stated + practised. Adaptive sampling ⚠️ stated, not shipped as default: "Fixed a major bug in the adaptive-sampling routine that had effectively disabled adaptive sampling." (ALAMO 2020.4.25); random sampling stayed the default until 2024.10.19 [03 C8]. Teach step 5 as the published method, not as what ALAMO users got by default.

**Steps**:
1. Ask whether an algebraic model exists or can be derived cheaply; if the design has discrete decisions, do not go straight to a derivative-free solver.
2. Write a basis library from polynomials, physical phenomena and engineering experience.
3. Select the smallest accurate subset by integer programming with an information criterion, not by shrinkage or a large network.
4. Impose first-principles bounds on the response during fitting and certify them.
5. Sample adversarially: find where the model is most wrong, add those points, refit, stop when none violate.
6. Read the model: a missing required term or an implausible one means suspect data or basis; go back.
7. Embed the surrogate in the MINLP and solve globally; if no fixed basis fits, formulate symbolic regression as a global MINLP; if the function stays black-box, use a deterministic derivative-free method.
8. State the price: fitting can take "four or five orders of magnitude more" time than the lasso (TAMU 2025, ASR [0:31:05]) [02 J5].

**Applies to stage**: problem choice, modeling, algorithm design.

**Different from standard practice**: machine learning picks the most accurate model class; here the model must be optimizable and readable, so it gets the fewest terms, chosen exactly.

**Limitations**: "the number of input variables is modest, typically fewer than a few dozen" (ALAMO manual §1.1, firm) [05 A8 8c]; noise: unregularized subset selection has "poor performance on noisy data" (doi:10.1214/20-STS806) [05 A8 8d]; the 2014 and 2015 full texts were not read.

<a id="method-4"></a>

## Method 4: Enter with a benchmark; judge by certified ground truth and portfolios

### Full-text evidence (08 §2, copied)

| Method | Cards (E / V / C) | Full or partial | Evidence by period | Say–do after the full texts |
|---|---|---|---|---|
| M4 Enter with a benchmark; certified ground truth and portfolios | 74 (30 / 51 / 7), 74 works | 61 | 0 / 0 / 1 / 1 / 4 / 11 / 13 / 0 | ✅ steps 1–3, 5, 6; ⚠ step 4 only in 2013; ✗ step 7 for the group's own algorithms and BAM |

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

### Variants, contradictions and proposals (08 §3, §5.3)

| Card | Method | What the card shows | Weight | Verdict |
|---|---|---|---|---|
| S025 (1999) | M4 | Rivals' published numbers from other machines and tolerances, and a single-winner conclusion [S025 pp. 12, 15] | Dated, before the 2013 protocol; the authors argue from their own handicaps [S025 p. 12] | Dates M4's identical-conditions form to 2013 on; no change to the method |
| S161 (2008) | M4 | Defaults tuned on the 15 structures that report the gain [S161 manuscript pp. 4–5, 7] | Another author is first and corresponding; a module in another group's crystallography program | Extends Inner Tension 5 back to 2008 |
| S170 (2025) | M4 | Single-winner verdict beside reported rival wins; no hold-out or tuning protocol for the defaults [S170 pp. 24–29] | He is corresponding author | A genuine step-7 gap for the group's own algorithms |
| S238 (2026) | M4 | Defaults chosen on the instances that carry the headline; the published sensitivity tables show the improvements depend on them [S238 manuscript pp. 19, 21–22] | Student-first, with Dey | Weak on his own practice; same pattern |
| S239 (2026) | M4 | Implementation choices made on the same LPs used for the claims, disclosed in the text [S239 p. 16] | TOF-authored BARON module | Step-7 gap, disclosed |
| S270 (2026) | M4 | BAM ranked first on the 502 problems with no hold-out or developer rounds on the slides [S270 pp. 8, 14, 19] | Talk slides | Inner Tension 5 reaches academic talks (also [S272 pp. 5, 7–8, 14]; [S273 pp. 10–11, 20]; [S277 pp. 3–4, 10]) |
| S249 (2017) | M4 | Comparative claims in a brochure without a benchmark [S249 pp. 80–81] | Firm voice | Inner Tension 3, as stated |

| # | SKILL.md location and current text | Full-text finding | Proposed change |
|---|---|---|---|
| 7 | Method 4 Say–do, *✅ for the 2013 and 2022 studies*; the 2013 hold-out *kept as a disagreement* | 2013: optima certified "for most" problems [S001 p. 21]; the unseen set is the same 502 problems after an affine change of variables with condition number 2 [S001 p. 41], which settles the disagreement toward note 03's reading, although the authors write that the transformation "otherwise changes the problems considerably, including the shape of the objective functions and location of all local solutions" [S001 p. 41]. 2022: steps 1–3, 5 and 6 hold; no developer rounds, no hold-out, and a bare 2,500-evaluation budget [S063 p. 13] | Rewrite the say–do line with these qualifiers and drop the disagreement note |
| 8 | Method 4 Say–do ⚠ and Inner Tension 5, *BAM claims rest on libraries ... no hold-out mentioned* | The same gap in the group's own algorithm papers [S170 pp. 24–29; S239 p. 16], in a 2008 crystallography code [S161 manuscript pp. 4–5, 7] and in 2025–26 talk slides that rank BAM first [S270 pp. 8, 14, 19; S272 pp. 5, 7–8, 14] | Extend Tension 5 from product pages to papers and talks |

**D. Method 4, new step: build the instances the claim needs.** When the public library is easy for your solver or lacks the structure, build instances along the axis the claim is about, with ground truth known by construction or certified, and publish them: hand-built instances on the contribution's axis after finding that "all pooling problems currently in the open literature are easy problems" for the authors' solver [S025 pp. 10, 12–13]; factorial structural knobs [S018 p. 17]; closed-form physical families [S017 pp. 8–10]; controlled tightness by binary search on sampled feasible points [S189 arXiv pp. 20–21]; instances generated from a known tree decomposition [S388 p. 1]; inherited sets kept intact and extended with the same generator [S237 pp. 1–3]; instance ranges chosen so that solving them settles open questions [H007 pp. 1, 13, 16, 27; S204 pp. 1–2]; written admission rules: "Thanks to these extensive preliminary tests, we discarded all instances that are solved by at least 30% of the complete solvers within a time limit of 30 seconds." [S031 p. 15]; instances stored as contributed, never reformulated [S031 p. 8]; a library distilled into representative forms with provenance [S211 arXiv pp. 11–13]; black-box sets with certified optima built from an algebraic library [S063 p. 13].

### Added in T3.6

- **Evidence condensed**: Stated unchanged (the web-research quote [02 P2]; card S001 confirms the counted gap and the four user questions on p. 2). Practice → [S001 pp. 3, 14, 20–23, 30–33; S063 pp. 3, 13–14, 27; H007 pp. 12–14; S272 pp. 4–5, 14–16]. Say–do rewritten from 08 §3.2 items 7–8: ✅ steps 1–3, 5, 6; ⚠ step 4 only in 2013; ✗ step 7 for the group's own algorithms and BAM; 74 cards (30 / 51 / 7), 61 read in full or in part.
- **Variant bullets**: the weak 2013 hold-out [S001 pp. 21, 41] (settles the disagreement the old say–do line kept); 2022 without developer rounds or hold-out [S063 p. 13]; step 7 unmet [S170 pp. 24–29; S239 p. 16; S270 pp. 8, 14, 19]; the early form [S025 pp. 14–15; S058 preprint pp. 13–15].
- **Steps**: step 5 + the mixed-tolerance median-of-ten success test (EP5) [S001 p. 21]; step 6 + the virtual-best envelope (EP7); new step 8 from 08 §5.3 D with the admission-rule quote [S031 p. 15] and sizes that settle open questions [H007 pp. 13, 16]. Steps 1–7 keep their numbers.

### Review fixes (T3.6)

- Variant 2013: *a weak hold-out (the notes' disagreement is settled)* → *a weak hold-out by this skill's reading, while the authors hold that the change reshapes the objectives and moves all local solutions [S001 p. 41]*, the counter-position that 08 §3.2 item 7 above quotes ("otherwise changes the problems considerably, including the shape of the objective functions and location of all local solutions"); declaring the disagreement settled had removed it from SKILL.md instead of marking it (rules review).
- Practice: *the 2013 protocol rerun on 42 codes in 2026 [S272 pp. 4–5, 14–16]* → *the 2013 design (502 problems, 2,500 evaluations, ten shared starts) rerun on 42 codes in 2026 [S272 pp. 4–5, 8, 14–16]* (card S272: the success test is stated anew on the median of 10 runs; versions, options and hardware are not named).
- Steps 2–4 + EP4, EP8, EP6; step 5 + the 2013 success test f(y) ≤ max(1.01 f(x*), f(x*) + 0.01) [S001 p. 21] (catalog EP5 now carries it too).

### Before T3.6 (moved verbatim)

**Method 4: Enter with a benchmark; judge by certified ground truth and portfolios**

**One line**: Before inventing an algorithm in an area new to you, benchmark everything that exists on a large public set against optima certified by a deterministic global solver, under identical conditions at defaults with developer rounds and a hold-out; publish problems and raw results; conclude with a portfolio and a stated scope; your own algorithms come later, on the same library.

**Evidence**:
- Stated: "There is currently no systematic comparison of the existing implementations of derivative-free optimization algorithms on a large collection of test problems." (Rios & Sahinidis 2013, doi:10.1007/s10898-012-9951-y, p. 1248) [02 P2]; "we tested their software against an additional collection of problems that had not been seen by developers in order to confirm that the process had not led to overtraining" [02 X2]; "However, computational results show that there is no single solver whose performance dominates that of all others." (2013) [01 SW3]; "They should be used collectively rather than individually." (2022, doi:10.1007/s10898-021-01085-0) [02 J1].
- Practice: ground truth from BARON (LINDOGLOBAL for trigonometric functions); published bounds and random starts; a budget justified by "about 200 CPU days" for a real application [02 X3; 03 §B4]; problems and raw results at https://sahinidis.coe.gatech.edu/dfo and /midfo [03 §A2]; benchmark first, own method later in DFO (2013 → 2023-25), SDP relaxations (2011 → 2022) and LP presolve (2008-09 → 2026) [03 §C3].
- Say–do consistency: ✅ for the 2013 and 2022 studies. ⚠️ for his own product: BAM claims rest on libraries TOF says it "routinely use[s] to develop BAM", with no hold-out mentioned [03 §E2, C1]; the 2013 hold-out was a variable transformation of the same problems, read as "unseen" by notes 01 and 05 and as weak by note 03 (kept as a disagreement).

**Steps**:
1. On entering a method area, collect every implementation and a large public test set; do not lead with your own method.
2. Certify each problem's optimum with a deterministic global solver (a second one for functions the first cannot read).
3. Fix identical conditions: bounds, published starting points, stopping rules, a budget tied to a real application's cost.
4. Run defaults; share results with developers over rounds; then test on structurally new problems they never saw.
5. Define success explicitly; report median and best runs; publish problems and raw results.
6. Conclude with the smallest covering portfolio and list what the study did not cover.
7. Use the benchmark to pick components for your tools; when your own algorithm enters, apply step 4's hold-out to it too.

**Applies to stage**: problem choice, experiment design, judging results.

**Different from standard practice**: the comparison comes before any own method, the yardstick is a certified optimum, and the verdict is a portfolio.

**Limitations**: both DFO studies are bound-constrained only (arXiv:1505.07881); rankings age (arXiv:2209.05759) [05 A7]; certified ground truth needs algebraic test problems; the data URLs printed in the papers no longer resolve [03 §A2].

<a id="method-5"></a>

## Method 5: A relaxation's strength counts only at speed

### Full-text evidence (08 §2, copied)

| Method | Cards (E / V / C) | Full or partial | Evidence by period | Say–do after the full texts |
|---|---|---|---|---|
| M5 A relaxation's strength counts only at speed | 59 (41 / 24 / 2), 56 works | 43 | 0 / 1 / 12 / 1 / 6 / 9 / 12 / 0 | ✅, practised in 2002 before it was stated in 2005 |

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

### Variants, contradictions and proposals (08 §3, §5.3)

| Card | Method | What the card shows | Weight | Verdict |
|---|---|---|---|---|
| S032 (2001) | M5 | SDPs proposed "instead of the traditional linear programming relaxations" on strength and polynomial solvability, with no time or failure evidence [S032 pp. 2, 20] | Theory paper, dated | Refines Inner Tension 2 (§3.2 item 10) |
| S189 (2025) | M5 | A comparison with BARON ranked by root bound only [S189 arXiv pp. 19, 21] | Co-authored, another faculty member corresponding | Weak. No change |

| # | SKILL.md location and current text | Full-text finding | Proposed change |
|---|---|---|---|
| 6 | Method 5 Limitations, *full texts of the 2004, 2005 and 2018 papers were not read* | 2004 and 2005 read [S006; S003]; 2018 abstract only [S030] | §2, Method 5 |
| 10 | Inner Tension 2, *polyhedral-only (2005) vs hybrid LP/NLP (2018), a dated change on the same stated grounds* | A sequence, not one change. In 2000 the IQP module defaulted to a quadratic relaxation and a mixed-integer SDP module shipped [S077 pp. 40, 43, 53, 92–95]; in 2001 a theory paper proposed SDPs on strength [S032 pp. 2, 20]; in 2002 an LP was chosen by gap and time [S053 pp. 21–25]; in 2004 LP-only was argued from NLP unreliability while the code still linked NLP and SDP solvers [S006 pp. 3, 7, 23]; 2005 polyhedral [S003 pp. 1–2, 15]; 2011 SDPs priced at three orders of magnitude more time [S018 pp. 1, 18–19]; 2018 hybrid [S030]; 2021–22 SDP-quality bounds from convex quadratic cuts with per-node switching [S116 arXiv pp. 22–25; S133 arXiv pp. 12, 18–22]; 2025 a quadratic-relaxation hierarchy re-tested because convex QCQP solvers improved [S189 arXiv pp. 1–2; S211 arXiv pp. 2, 13–14] | Replace the two-point tension by this dated line; the constant is subsolver speed and reliability (Method 5 step 7) |

**B. Method 5 step 0 (new) and Method 1 evidence: order before you price.** (1) Write one master object: a homogenized Lagrangian range-reduction problem [S006 pp. 12–16; S046 arXiv pp. 12–13] or a convex extension over a generating set [S028 pp. 3–14]; (2) show the literature's rules, your own earlier ones included, as special cases or dominated [S006 p. 15; S053 pp. 8, 12–13, 16, 19; S032 pp. 7–10; S003 pp. 9–10]; (3) prove the dominance order with two-way feasibility maps and settle each incomparable pair with a one-variable instance [S018 pp. 2–3, 8, 16; S025 pp. 8–10; S133 arXiv pp. 6–11; S042 preprint p. 21]; (4) only then price the non-dominated ones by time and failures [S018 pp. 17–19, 27; S053 pp. 21–25]; (5) read the new rule off the master [S006 pp. 17–19].

### Added in T3.6

- **Evidence condensed**: Stated → the 2005 abstract's clause as card S003 copies it [S003 p. 1] (the two full abstract sentences quoted before T3.6, from note 02 T6, are below). Practice → [S053 pp. 21–25; S003 p. 22; S044 pp. 15–18; S133 arXiv pp. 12, 18–22]; the 2011 dominance-then-price study [S018 pp. 2–3, 17–19] is in step 0. Say–do: practised in 2002 before stated in 2005 (08 §2); 59 cards (41 / 24 / 2), 43 read in full or in part.
- **Variant bullets**: strength-only rankings [S032 pp. 2, 20; S189 arXiv pp. 19, 21]; the 2004 argument [S006 pp. 3, 7, 23]; the yardstick generalized [S084 preprint pp. 9, 15–17; S269 arXiv pp. 9–12; S206 manuscript pp. 18–26].
- **Steps**: new step 0 from 08 §5.3 B [S006 pp. 12–16; S028 pp. 3–14; S018 pp. 2–3, 8, 16] (PD4); step 1 + effect classes (EP3) [S003 pp. 22–23]; step 2 + lifted, violated-only cuts (DM3, DM4) [S003 pp. 3–7, 15]; step 3 + the expensive step at the root (DM1) [S133 arXiv pp. 18–19]; step 4 + per-node switching (DM10) [S116 arXiv pp. 22–23]; step 5 points to the new anti-pattern row [S162 p. 23]; step 7 points to Inner Tension 2.
- **Different from standard practice** + one clause for tuning, learned components and surrogates (08 §10 item 4). **Limitations**: the not-read clause is gone from this paragraph (2004 and 2005 read [S006; S003]; 2018 abstract-level [S030], noted in the hybrid anatomy and Honest Boundary; 08 §3.2 item 6).

### Review fixes (T3.6)

- **Step 0 merged into step 1 and corrected.** *Order before you price ... price only the non-dominated* read the dominance order as proven strength and so discarded weaker but cheaper relaxations, against the method's thesis and its own step 2 (usefulness review). Both works it cites do the opposite: S018 proves vDShor ≤ vDLG1 ≤ vSRLT, prices every relaxation and recommends the dominated DLG1 for bound per second (card S018 D2, D8; pp. 2, 19, 27); S053 chose the (R7) LP over (R8), tighter in all 24 size rows at 2.4–5 times the CPU time (card S053; pp. 21–22). Step 1 now reads: a proven dominance order (PD4 [S006 pp. 12–16; S028 pp. 3–14; S018 pp. 2–3, 8, 16]) drops a candidate only when another is at least as strong and no more expensive; price the rest, dominated ones included, and keep a cheap balance relaxation when the strongest is orders of magnitude slower (DNN/SRLT about 3% gap at about 400 s, DLG1 13% in a few seconds, SD 19% [S018 pp. 1, 18–19, 27]; [S053 pp. 21–22]). Item (4) of 08 §5.3 B above (*only then price the non-dominated ones*) is superseded by this reading: S018's first transferable line says the same as 08, but the card's next line and D8 recommend the dominated balance relaxation. The steps are numbered 1–7 again (usefulness review).
- Practice: *2005, the one loss explained by LP cost per node* → *the loss the paper discusses (tls4)* [S003 p. 22]; the card speaks of *the one acknowledged nontrivial loss*, and its table reading notes are not carried (house rule). The 08 §2 line above (*the one nontrivial loss*) is read the same way.
- The ✅ variant *the yardstick generalizes* moved to *Different from standard practice*, with its cards [S084 preprint pp. 9, 15–17; S269 arXiv pp. 9–12; S206 manuscript pp. 18–26] (rules review: a ✅ bullet is supporting practice, not a variant).
- Limitations + *2004 and 2005 are read in full [S006 p. 3; S003 pp. 1–2], but the 2018 hybrid paper only as an abstract [S030], so step 7's 2018 revision rests on it and per-node switching is read in its 2021–22 forms [S116 arXiv pp. 22–25]*: 08 §2 and §3.2 item 6 proposed this text; the T3.6 edit had deleted the clause though S030 is still abstract-level (rules review). The *Limitations* bullet of *Added in T3.6* is superseded.

### Before T3.6 (moved verbatim)

**Method 5: A relaxation's strength counts only at speed**

**One line**: Rank relaxations by bound closed per unit time and by numerical failure risk, not by strength alone; default to LP/MIP node relaxations, emulate costly ones with cheaper cuts, admit nonlinear relaxations only with fail-safes and per-node switching, check every subsolver answer, and switch off what hurts.

**Evidence**:
- Stated: "Their potential can be realized only if they can be solved with sufficient speed and reliability. Unfortunately, state-of-the-art nonlinear programming codes are significantly slower and numerically unstable compared to linear programming software." (Tawarmalani & Sahinidis 2005, doi:10.1007/s10107-005-0581-8, abstract, co) [02 T6]; "portfolios or [sic] linear and nonlinear relaxations" (Oberwolfach 2019, sole, doi:10.4171/OWR/2019/26) [02 J1].
- Practice: SDP relaxations for QCQP "require three orders of magnitude more computational time than the weaker relaxations, while providing relaxation gaps averaging 3% as opposed to gaps of up to 19%" (doi:10.1007/s10107-011-0462-2) [01 SW2]; "SDP-quality bounds" from convex quadratic relaxations, in BARON (doi:10.1007/s10107-021-01680-9); hybrid LP/NLP with "fail-safe techniques" and learned switching (doi:10.1007/s12532-018-0138-5) [01 SW5]; QP subsolver answers used only if they satisfy the KKT conditions (Nohra thesis §3.5) [03 §D2]; "BARON's embedded FilterSD algorithm is now off by default." (2022.1.19) [03 §H].
- Say–do consistency: ✅ stated + practised (mostly co-authored with Tawarmalani or Khajavirad; one sole statement).

**Steps**:
1. For each candidate relaxation, measure gap closed, time and numerical failures on a library; never accept "stronger" without the other two.
2. Default node subproblems to LP (MIP with integers); represent convex pieces by outer-approximating cuts.
3. When a stronger relaxation is too slow, find a cheaper object that reproduces most of its bound (quadratic cuts, multiterm or lifted LP inequalities) and ship that.
4. Admit a nonlinear relaxation only with a fail-safe path, switching relaxations per node from observed performance.
5. Verify every subsolver answer (KKT check, safe LP bounds); compute branching information natively if a subsolver cannot be checked.
6. Switch off components that slow typical instances; reintroduce after repair and testing.
7. Re-test the stance when subsolver technology changes (the 2005 polyhedral-only view was revised in 2018 on the same stated grounds) [02 CH1].

**Applies to stage**: algorithm design, diagnosis, experiment design.

**Different from standard practice**: theory ranks relaxations by the hull they reach; this ranks them by bound per second with failure risk priced in.

**Limitations**: a single nonlinear relaxation can close a gap where BARON's linear relaxations take over 1000 s (Ruiz & Grossmann 2013, doi:10.1016/j.compchemeng.2012.09.017) [05 A5]; reduced-space schools argue full-space auxiliary variables blow up flowsheets [05 A4]; full texts of the 2004, 2005 and 2018 papers were not read.

<a id="method-6"></a>

## Method 6: Prove the problem hard, then bound the heuristic

### Promotion record (08 §4, copied)

**One promotion: Method 6.** Eight clusters reached three or more distinct works read in full or in part; one passes all four checks. Adding it gives six core methods, inside the 3–7 range, so nothing is merged or replaced.

| Cluster (merged by meaning) | Works read in full/part | 1 Recurrence | 2 Say–do | 3 Executable, non-standard | 4 Exclusivity | Result |
|---|---|---|---|---|---|---|
| Prove the problem hard, then design heuristics with proven and computed quality bounds | S024, S010, S029, S002, S119, S118, S238 (7; abstracts S061, S138, S088, S213) | ✅ 1995–2004 manuscripts across process planning, capacity expansion, HENS and the TDTSP; echoes 2021, 2026 | ✅ sole-authored statement [S002 manuscript p. 18]; [S010 preprint p. 8]; [02 T3] | ✅ | ✅ in his field and period (below) | **Method 6** |

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

### Added in T3.6

- **Promoted** as 08 §4 proposes: seven works read in full (six of 2000–2004 plus the 2026 echo [S238]) and four abstracts; passes recurrence, say–do, executable and exclusivity (08's four checks above). Six core methods, inside the 3–7 band; Methods 1–5 keep their numbers.
- **SKILL.md text** = 08's draft, condensed: Stated [S002 manuscript p. 18]; Practice [S024 manuscript pp. 10–25; S029 preprint pp. 9–26; S118 preprint pp. 9–21; S119 preprint pp. 6–22]; say–do with the work lists; one variant bullet (era) [S119 preprint p. 1]; steps 1–7 with 08's cards (step 1 shortened; its zeroed-weights detail and [S118 preprint pp. 9–11] are in the draft above); limitations [S029 preprint pp. 16–18, 22; S118 preprint p. 15]. The extreme-order-statistics remark [S118 preprint pp. 16–17] and the exclusivity check stay here.
- **Cross-links written into SKILL.md**: Routing row and Workflow A step 6; Agentic Protocol Step 2 (complexity); Taste mark 3 and warning 4; the new anatomy of [S119] (its Shows line: Method 6, Taste mark 3, Heuristic 7); Honest Boundary (resolved item) and Era line; Roundtable Card (leads when, pushes back on); Trajectory 1997–2007.

### Review fixes (T3.6)

- Practice: *strong NP-hardness carried through every published heat-exchanger-network formulation [S024 manuscript pp. 10–25]* → *ten published heat-exchanger-network problems classified, the utility targets in P and the matches and simultaneous formulations NP-hard in the strong sense [S024 manuscript pp. 5, 10–27]*. The paper classifies ten problems (Table 1, p. 27), introduces the sequential formulations as the most commonly used ones (p. 5), and concludes on "various forms of the HENS problem" (p. 25); the minimum-utilities targets are in P (Theorem 1, p. 7). Step 1: *every published formulation* → *each richer published formulation*. The 08 §4 wording above (*strong NP-hardness of every published formulation*; *carry the hardness through every published formulation*) and the S119 anatomy's origin are read the same way (fidelity and usefulness reviews).
- Say–do: *practised in six full texts of 2000–2004 [S024; S010; S029; S002; S119; S118]* → *stated in two reviews [S002 manuscript p. 18 (sole); S010 preprint p. 8 (co)] and practised in the four full texts above, written 2000–2004*. S002 is his sole-authored review and S010 an annotated bibliography whose open problems call for such work; 08 §4 check 2 above says *Practised in S029, S119 and S118*, plus S024's hardness proofs. The four practice works carry pages and version words in the Practice line (operator point 4); the bare ids are gone (rules and fidelity reviews).
- 08 §4 check 2's *a relaxation bound reported on every run* holds for S119 (an a posteriori ratio on every problem) but not for S029, which gives the LP gap only where the IP was not solved [S029 preprint p. 26]; Method 6 step 5 stays a prescriptive step.
- Variant (era): *1995–2004 at UIUC with Liu, Ahmed and Furman, dormant in the cards 2005–2020 [S119 preprint p. 1]* → *1995–2004 at UIUC (with Vander Wiel, Liu, Ahmed and Furman); no new manuscript in the line after 2004 (S118, written in 2000, appeared in 2008) [S118 preprint p. 1; S119 preprint p. 1; 08 §8]*. The 1995 TDTSP abstract is with Vander Wiel [S061]; S118 appeared in EJOR in 2008 from a manuscript dated 20 June 2000; one page of S119 cannot date the whole card set, which 08 §8 does (fidelity and rules reviews).
- *Different from standard practice*: *process-systems heuristics are usually justified by testing alone* → *the 1997–2004 papers describe process-systems heuristics as justified by testing alone [S119 preprint p. 1; S138]* (the papers' claim about their literature; S138 is an abstract-level card); + *the analysis is imported from approximation-algorithm theory [S119 preprint p. 3]: distinctive in process systems, standard in theoretical OR* (card S119: Ausiello et al., Hochbaum, Vazirani, pp. 3, 7, 16–17; 08 §4 check 4: *within his field and period*).
- Limitations + today's form (research-extraction-framework.md §七): an approximation whose loss is priced in a physical device, the compensating pumps of the 2026 water network (PD12) [S238 manuscript pp. 10–14], beside a general solver's dual bound.
- Dropped from SKILL.md as a process note: *Promoted by the four checks [08 §4]; the cards' method links predate it* (the promotion record is above).

### Before T3.6

Not in SKILL.md before T3.6. The pre-synthesis Honest Boundary listed the programme as *claimed but unverified*; that bullet is kept word for word in [Honest Boundary](#honest-boundary).

<a id="workflow-a"></a>

## Workflow A: Problem choice

### Full-text evidence (08, copied)

**D. Method 4, new step: build the instances the claim needs.** When the public library is easy for your solver or lacks the structure, build instances along the axis the claim is about, with ground truth known by construction or certified, and publish them: hand-built instances on the contribution's axis after finding that "all pooling problems currently in the open literature are easy problems" for the authors' solver [S025 pp. 10, 12–13]; factorial structural knobs [S018 p. 17]; closed-form physical families [S017 pp. 8–10]; controlled tightness by binary search on sampled feasible points [S189 arXiv pp. 20–21]; instances generated from a known tree decomposition [S388 p. 1]; inherited sets kept intact and extended with the same generator [S237 pp. 1–3]; instance ranges chosen so that solving them settles open questions [H007 pp. 1, 13, 16, 27; S204 pp. 1–2]; written admission rules: "Thanks to these extensive preliminary tests, we discarded all instances that are solved by at least 30% of the complete solvers within a time limit of 30 seconds." [S031 p. 15]; instances stored as contributed, never reformulated [S031 p. 8]; a library distilled into representative forms with provenance [S211 arXiv pp. 11–13]; black-box sets with certified optima built from an algebraic library [S063 p. 13].

| Heuristic | Cards | Strongest new evidence | Variant or calibration |
|---|---|---|---|
| H1 Special classes first | 17 | Eleven specialized class modules beside the general module in 2000 [S097 v4.0 pp. 7–8, 36–41]; the general module checked against the specialized one on its class [S006 pp. 23–24]; centrosymmetric phasing first, the general case next [S168 p. 8; S361 p. 1]; a class whose five-atom instances defeat three of four solvers [S190 pp. 1, 3, 16] | Size the class by library statistics: the libraries' rank is at most 5, so a fixed-rank algorithm is justified [S090 preprint pp. 5, 8, 11, 14]; 9,000 library expressions distilled to 19 forms [S211 arXiv pp. 11–13]; [S106] |

### Added in T3.6

- Step 1 + [H007 pp. 12–14] (a new class entered with a public library and named solver versions).
- Step 4 + size the class by library statistics [S090 preprint pp. 5, 8, 11] (Heuristic 1 variant, 08 §2.6).
- New step 6: an applied combinatorial problem of unknown complexity → Method 6. Checkpoint + *then build one: Method 4 step 8* (08 §5.3 D).

### Before T3.6 (moved verbatim)

**Workflow A: Problem choice**

**Input**: an application area, a problem class, or a model that will not solve.

**Steps**:
1. Check whether any solver certifies even small instances; if not, that gap is the project (→ Heuristic 1).
2. Without an algebraic model, prefer making one when decisions are discrete (→ Method 3).
3. In a method area new to you, plan a benchmark of existing implementations first (→ Method 4).
4. If the general problem resists, pick a special class whose small instances defeat current solvers; name what makes them hard (→ Heuristic 1).
5. Prefer problems whose users or sponsors will supply hard instances (→ Heuristics 3, 10).

**🔴 Checkpoint**: stop if no artifact (code, library, data) can come out of it, or no instance set exists on which progress can be measured. If the general version stalls, narrow to a class.

**Output**: one paragraph naming the capability gap, the library, and the tool the result will live in.

<a id="workflow-b1"></a>

## Workflow B1: A stalled global solve (solver user)

### Full-text evidence (08, copied)

| # | SKILL.md location and current text | Full-text finding | Proposed change |
|---|---|---|---|
| 15 | Workflow B1 step 3, *(inferred from Method 1; no source states this test)* | Co-authored sources exist. Scaled-time convergence profiles of the solved instances show dual bounds that start weaker than primal bounds and improve more slowly, with the optimum often found by local search in preprocessing [H007 pp. 14, 17]; a no-reduction profile that catches up means the component serves the proof [S046 arXiv p. 16]; a two-solver preliminary run in which the dual bound improves but no feasible point appears names the primal side as the bottleneck [S165 manuscript p. 11; S243 p. 17; S238 manuscript pp. 3, 14; S128 arXiv p. 19] | Replace the parenthesis by these sources. The sources diagnose a library or an application after the fact; the decision rule on one user's stalled log stays this skill's inference, and H007 warns that its profiles are not for comparing solvers [H007 p. 17] |

| Point | Check | Result |
|---|---|---|
| (3) H007 pp. 14, 17 as a source for Workflow B1 step 3 | `H007` text pp. 14 and 17 read | Confirmed, with the limits in §3.2 item 15 |

### Added in T3.6

- Step 3: *(inferred from Method 1; no source states this test)* → *(→ Heuristic 11)* with the co-authored sources [H007 pp. 14, 17; S046 arXiv p. 16] and the primal-side case [S165 manuscript p. 11]; the limit 08 states is kept in one clause: the sources read profiles of solved library instances after the fact, so the test on one user's log stays this skill's inference, and H007 warns that its profiles are not for comparing solvers [H007 p. 17] (here only). Operator point (3) checked at source by 08 §3.3.
- Step 2: a convexity declaration's effect (35 vs 1793 nodes [S003 p. 17]) was drafted here and moved to Heuristic 2 for length.

### Review fixes (T3.6)

- Step 3: *(→ Heuristic 11)* → a pointer to [Heuristic 11](#heuristic-11), whose procedure now lives in this step: read primal bound, dual bound and gap apart (in two general solvers if possible) and the time per component (DM7); for the primal side, the recipe of S128 and S165: a convex master whose optimality conditions reproduce the network equations, a fixed-binary feasibility check, no-good cuts, a budget search, the incumbent passed to the solver as a start, compared at equal total time (PD9) [S128 arXiv pp. 9–17; S165 manuscript pp. 13–17, 24]. *A tailored incumbent method* had no recipe in SKILL.md (usefulness review).
- Step 4 + the three relaxation-only families of S069 (RLT products, i.e. the pq-formulation for pooling; first-order conditions; problem-specific optimality conditions) and the result that makes them relaxation-only: on 14 pooling problems the q-formulation timed out on six while pq solved all, mostly at the root, but pq gave CONOPT worse local optima on 8 [S069 preprint pp. 9–20] (DM5; usefulness review).

### Before T3.6 (moved verbatim)

**Workflow B1: A stalled global solve (solver user)**

**Input**: the model, the solver and version, the full log.

**First move**: read the final status lines, not the progress indicator (Anti-pattern: reading only "normal completion"). No log → ask for it; never guess solve behaviour (Integrity Rule 2).

**Steps** (stop at the first step that explains the stall):
1. **Status.** If the log ends with "*** Globality is therefore not guaranteed ***" or reports missing bounds, the run is not yet a global solve; go to step 2 (→ Heuristic 7).
2. **Bounds and declarations.** Give every nonlinear expression a finite physical bound; replace "safe" bounds such as ±10^10. Recheck every convexity or relaxation-only declaration: "These three declarations are believed by BARON without verification, and an incorrect one produces a wrong answer silently." (manual §13.4, firm) [03 §D4]. Rerun (→ Heuristic 2).
3. **Locate the bottleneck** (inferred from Method 1; no source states this test). Upper bound still improving late, or a multistart finds a better point → the incumbent is the bottleneck: supply a good starting point, since duality-based reductions scale with U - L. Upper bound settled, lower bound flat → the relaxation or reduction is: go to step 4.
4. **Reformulate before tuning.** Remove gratuitous nonlinearity; pass valid relaxation-only constraints (doi:10.1007/s10898-004-2705-8) (→ Heuristic 2). Only then try options; extra threads help little on NP-hard problems (manual §13.3, firm) [03 §D4].
5. **Check the tool fits** (manual §4, firm) [03 §D4]. A model known to be convex: a local solver may reach the global optimum faster; hand convex MINLP to Grossmann or Leyffer. Only a good solution needed quickly: multistart local search, labelled "not certified".
6. **Escalate.** Lower bound still flat on small instances after steps 1-5 → a research problem, not a tuning failure: name the hard structure, narrow to that class (→ Heuristic 1), offer Workflow B2.

**🔴 Stop rules**: stop and report when (a) the log shows normal completion, no globality warning and a gap within tolerance: "global within tolerances", never "rigorous"; (b) step 5 sends the model to another tool; (c) step 6 is reached: a capability gap. Never call the incumbent global while a globality warning or open gap remains (→ Heuristic 7).

**Output**: the step that explained the stall, the changed model or settings, and the status.

<a id="workflow-b2"></a>

## Workflow B2: Designing a component inside a solver

### Full-text evidence (08, copied)

**A. Workflow B2 step 3, upgraded: carry the integer-programming device across.** The step exists with one stated source [02 I1]; the cards supply the practice. *Protocol*: name the IP device that solves the discrete analogue (variable disaggregation, reduced-cost fixing and probing, Lagrangian relaxation with an exact MILP subproblem, logic cuts, column generation); derive its continuous counterpart; show where it sits against the standard relaxation, e.g. the big-M relaxation is the envelope with a weaker bound plugged in [S101 pp. 1–2, 9–10, 16]; look for discreteness in disguise (a box-constrained bilinear optimum at vertices [S025 pp. 5–7]; McCormick exact when one factor is at a bound or binary [S053 pp. 5–7; S238 manuscript p. 9]; phases restricted to 0 or π [S168 p. 4; S198 pp. 2–5]) and linearize exactly. *Cards*: [S025 pp. 13–14; S006 pp. 15–16; S035 pp. 3, 10; S361 p. 1; S388 p. 1; S046 arXiv pp. 7, 9]; abstracts [S036; S054; S263].

**C. Workflow B2, new step: branch so the tree is finite where the structure allows.** (1) Ask whether the value function is piecewise constant or the optimum sits at finitely many candidate points; (2) change variables so the discontinuities are axis-parallel: "Since the discontinuities are, in general, not orthogonal to the variable axes, there would always be some rectangular cell that contains a discontinuity in the interior." [S014 p. 6], hence tender variables [S014 pp. 6–10]; (3) branch at the incumbent when it lies in the node and at breakpoints, and bisect periodically for exhaustiveness [S058 preprint p. 9; S077 p. 24; S162 pp. 24–25]; (4) prove finiteness by finite consistency [S014 p. 15]; (5) compare with convergent schemes on the rivals' own sets [S014 pp. 18–22]. Stated: "The issue of finiteness is not only of theoretical significance – our computational experiments using standard test problems indicate faster convergence of the proposed algorithm in comparison to existing strategies in the literature." [S014 p. 4]; finite termination is also among the results he lists as his own [02 T3]. Era: 1996–2004 in full texts, abstracts to 2009 [S047; S354].

### Added in T3.6

- Step 1 unchanged in SKILL.md (DM1 is cited in Method 1 step 1).
- Step 3 upgraded from 08 §5.3 A: [S101 pp. 9–10, 16] (big-M as the envelope with a weaker bound plugged in) and discreteness in disguise [S025 pp. 5–7; S053 pp. 5–7] (PD2). The rest of the protocol (Lagrangian with an exact MILP subproblem, logic cuts, column generation; [S168 p. 4; S198 pp. 2–5; S238 manuscript p. 9]) is in the 08 text above; 08 rejects it as a heuristic or method (exclusivity fails).
- New step 5 from 08 §5.3 C: finite branching [S014 pp. 6–10, 15; S058 preprint p. 9] (PD7); "implement with an on/off switch" moved from step 5 to step 6. 08 counts only two independent works for this cluster, so it stays a workflow step.

### Review fixes (T3.6)

- Step 5 + DM11 (search where the discontinuities are axis-parallel).

### Before T3.6 (moved verbatim)

**Workflow B2: Designing a component inside a solver**

**Input**: a problem class whose small instances defeat current solvers; a code base (or Method 2's lone version).

**Steps**:
1. Order node reductions by cost (→ Method 1).
2. Choose node relaxations by bound per second and failure risk; plan a cheap surrogate for any expensive one (→ Method 5).
3. Transfer an analogous tool from integer or constraint programming (product vs variable disaggregation; reduced-cost fixing) [02 I1].
4. Keep a rival's key insight; redesign the part that clashes with practice (→ Heuristic 8).
5. Implement with an on/off switch (→ Method 2).

**🔴 Checkpoint**: a component using an unchecked subsolver answer needs a verification or fail-safe before testing; a component that cannot be switched off cannot be evaluated. Stop designing once it has a switch and a verification path; the next step is Workflow C. If C shows it slows typical instances, switch it off by default until repaired and retested (→ Method 5 step 6).

**Output**: a module with a switch and a design note.

<a id="workflow-c"></a>

## Workflow C: Experiment design and execution

### Full-text evidence (08, copied)

- **EP1 Ablate inside production code, print the exact option lists, admit only competitors with the same switch** [S046 arXiv pp. 15–16, 21; S003 pp. 17–23; S090 preprint pp. 22–27].
- **EP3 Count effects in classes, losses included**: effect classes per metric [S003 pp. 22–23]; factor bands [S090 preprint p. 22]; win, tie and loss with thresholds [S239 pp. 26–27]; per-instance ratios that keep the slowdown [S161 manuscript pp. 6–7]; the full factorial including the cells that got worse [S190 p. 16].
- **EP5 A mixed-tolerance success test on the median of ten shared starts** [S001 p. 21; S063 p. 13; S270 p. 8; S272 p. 8].
- **EP11 Replicates for order-sensitive choices** [S239 pp. 17–18; S269 arXiv pp. 11–12].

### Added in T3.6

- Step 1 + replicate order-sensitive choices (EP11; [S239 pp. 17–18] in the catalog). Step 2 + *if no library has the structure, build one (→ Method 4 step 8)*. Step 3 + EP1 [S046 arXiv pp. 15–16]. Output + effect classes per metric (EP3).

### Review fixes (T3.6)

- Step 1 + termination tolerances per interface: BARON's relative gap is 10^-9 natively in 2021 [S191 p. 21] and 0.1, tied to GAMS optcr, in the 2005 GAMS chapter [S012 manual p. 8] (cards S191 and S012; usefulness review).

### Before T3.6 (moved verbatim)

**Workflow C: Experiment design and execution**

**Input**: a module or method, candidate libraries, competing solvers.

**Steps**:
1. Fix the protocol (one thread, time limit, tolerances, machine); prefer deterministic work limits (→ Method 2, Heuristic 6).
2. Use whole public libraries; filter only for solver acceptance, triviality and always-timeout cases, stating the rule (→ Heuristic 4).
3. Ablate in the production code; include other solvers only if they allow the same ablation (→ Method 2).
4. Give each baseline its strongest fair mode (→ Heuristic 4); for a learned component, compute the ceiling first (→ Heuristic 5).
5. For black-box comparisons: certified optima, identical bounds and starts, application-tied budget, defaults plus developer rounds, structurally new hold-out (→ Method 4).

**🔴 Checkpoint**: if results differ by library, report per library and do not aggregate; without a hold-out, do not claim generalization; if reruns differ, fix determinism before reporting.

**Output**: per-library tables, solved and unsolved analysed apart, named versions, raw data.

<a id="workflow-d"></a>

## Workflow D: Judging results

### Full-text evidence (08, copied)

- **EP2 Read profile tails and bound progress**: a catching-up ablated variant means the component serves the proof [S046 arXiv p. 16]; scaled-time primal and dual profiles [H007 pp. 14, 17].
- **EP3 Count effects in classes, losses included**: effect classes per metric [S003 pp. 22–23]; factor bands [S090 preprint p. 22]; win, tie and loss with thresholds [S239 pp. 26–27]; per-instance ratios that keep the slowdown [S161 manuscript pp. 6–7]; the full factorial including the cells that got worse [S190 p. 16].
- **EP9 Longitudinal reruns**: solvers tagged same, updated or new [S272 pp. 4–5, 8–9; S270 p. 5]; old gains re-tested on new versions [S190 p. 15].

### Added in T3.6

- Step 1 + an optimum that depends on the feasibility tolerance is printed with both values [S003 p. 23]. Step 2 + win, tie and loss counts with stated thresholds [S239 pp. 26–27] (EP3). New step 6 → Heuristic 12 (08 §5 suggests this as the place for H12 if the heuristic list had to stay at ten; SKILL.md keeps both).

### Review fixes (T3.6)

- Step 6 (*→ Heuristic 12*) now carries the procedure itself: certify the optimum, list the K best or all feasible designs from one tree (DM12), let higher-fidelity models or experiments re-rank them [S035 p. 11; S058 preprint p. 22; S022 arXiv p. 12], with a pointer to [Heuristic 12](#heuristic-12). The last sentence of *Added in T3.6* is superseded.

### Before T3.6 (moved verbatim)

**Workflow D: Judging results**

**Input**: tables, profiles, learned models, solver outputs.

**Steps**:
1. Separate evidence from proof (→ Heuristic 7).
2. List instances that got worse; call modest effects modest (Nohra "average reductions of 19%"; Fourier-Motzkin "up to 6%, 8% and 11%") [03 §E3].
3. Read learned models against physics (→ Method 3).
4. Conclude with a portfolio when nothing dominates; state the uncovered scope (→ Method 4).
5. Compare with old versions on the same hardware (→ Method 2).

**🔴 Checkpoint (stop rules)**: a gain on one library only is not a result; a heuristic value without a bound is not a global result; a model that violates physics is rejected regardless of fit; a development-set claim needs a hold-out before it leaves the lab.

**Output**: findings with scope and losses.

<a id="workflow-e"></a>

## Workflow E: Release and after publication

### Full-text evidence (08, copied)

- **WM10 Manuals put the contract first**: model requirements and bounds before options, and every termination status paired with what it certifies and what the user does next [S012 manual pp. 1–5; S112 v17.4.1 pp. 12–14; S191 pp. 12–13].
- **EP6 An unseen set after developer rounds** [S001 p. 41].

### Added in T3.6

- Step 1 + instances stored as contributed [S031 p. 8] (08 §5.3 D). Step 3 + the manual's contract first (WM10) [S012 manual pp. 1–5]. Kept here only: the 2013 study took its default-settings rule from Neumaier et al.'s comparison of complete global solvers [S001 pp. 22–23] (card S001: Workflow E step 5 evidence).

### Before T3.6 (moved verbatim)

**Workflow E: Release and after publication**

**Input**: the paper's code, instances, results; critiques.

**Steps**:
1. Release instances as a named library; add them to the development set (→ Method 2).
2. Publish all problems and raw results, with what is needed to regenerate starting points [03 §A2].
3. Ship the method in the tool and log what changed (→ Method 2).
4. Route users' failing models back as bug reports and credit the source (→ Heuristic 3).
5. Answer criticism with fixes: support the testers, fix, adopt their protocol [03 §E6; 05 B1].

**🔴 Checkpoint**: keep printed data URLs alive (the 2013 and 2022 ones broke [03 §A2]); never let product pages restate results more strongly than the papers [05 2h].

**Output**: library, data page, release note.

<a id="workflow-f"></a>

## Workflow F: Organizing students around the engine, and stages without a method

### Full-text evidence (08, copied)

**Partners.** Dow (2015–2025), DOE/NETL (2011–2026), MERL (2018–2025) and TOF (2020–2026) supply problems, co-authors and funding [S007 arXiv p. 1; S183 p. 8; S165 manuscript pp. 1, 30; S074 arXiv p. 1; S239 p. 1]. Students carry topics to him as well as from him: in the acknowledgments of the 2003–04 review, his former students Liu and Ahmed "introduced me to many of the topics discussed in this paper" [S002 manuscript p. 22] (the FOCAPO version has the same sentence); black-box applications were MS theses [S001 pp. 41–47].

**Editorial practice, one instance.** As guest editor, his co-authored submission to the special issue was handled by a co-editor, and he saw nothing of its review [S208 p. 5] (§10 item 6).

6. ***Students as scouts* and the editor recusal as heuristics**: one own-voice instance each [S002 manuscript p. 22; S208 p. 5]; at most one line of evidence in Workflow F and in *Stages without a distillable Sahinidis method*.

### Added in T3.6

- Step 4 + one own-voice instance of students bringing topics [S002 manuscript p. 22] (08 §10 item 6: one line at most). The MS-thesis evidence [S001 p. 41] went to Heuristic 9.
- Stages without a distillable method + the catalog's writing moves (WM1–WM13) and one instance of a guest editor's recusal [S208 p. 5] (08 §10 item 6).

### Before T3.6 (moved verbatim)

**Workflow F: Organizing students around the engine (observed, medium confidence)**

Evidence: thesis acknowledgements (genre-biased), rosters, CV [04 §0]; not his own account.

**Input**: new students, often from outside optimization.

**Steps**:
1. Start with a training problem or an MS thesis as a complete first project (→ Heuristic 9).
2. Give freedom inside a funded area, insight on request: "Thank you for giving me the freedom to explore different ideas and for offering your acute insight when I needed it." (Sun 2021, doi:10.1184/R1/19145945.v1) [04 §1.1].
3. Question until each conclusion can be explained briefly: "His insightful questions have challenged me to understand the fundamental concepts of my work, and to succinctly explain any conclusion that I reach." (Sauk 2020, doi:10.1184/R1/13194722.v1) [04 §1.2].
4. Pass solver know-how through postdocs; make the sponsor's engineer a co-mentor; land each thesis as a module [04 §3.2, §3.4].

**🔴 Checkpoint**: not documented; how and when he stops a student's line is unknown.

**Output**: thesis plus module.

**Stages without a distillable Sahinidis method**

Say "no distillable Sahinidis method" and label any generic advice "not Sahinidis-style":
- Literature search (one ASR remark on tracing citations [02 I4]); writing process in his own voice [02 Gaps].
- Referees and rebuttals: none public; two papers took 3.5 and 4.6 years to acceptance, reasons unknown [01 §3].
- Leaving a line: exits are silent [06 §4.2]; meeting routines, draft review, his current coding share [04 Gaps].

<a id="heuristic-1"></a>

## Heuristic 1: Special classes first, then generalize

### Full-text evidence (08 §2.6, copied)

| Heuristic | Cards | Strongest new evidence | Variant or calibration |
|---|---|---|---|
| H1 Special classes first | 17 | Eleven specialized class modules beside the general module in 2000 [S097 v4.0 pp. 7–8, 36–41]; the general module checked against the specialized one on its class [S006 pp. 23–24]; centrosymmetric phasing first, the general case next [S168 p. 8; S361 p. 1]; a class whose five-atom instances defeat three of four solvers [S190 pp. 1, 3, 16] | Size the class by library statistics: the libraries' rank is at most 5, so a fixed-rank algorithm is justified [S090 preprint pp. 5, 8, 11, 14]; 9,000 library expressions distilled to 19 forms [S211 arXiv pp. 11–13]; [S106] |

### Added in T3.6

- + the general module checked against the specialized one on its class [S006 pp. 23–24]. The library-statistics variant [S090 preprint pp. 5, 8, 11] went to Workflow A step 4; the 2000 module count [S097 v4.0 pp. 7–8, 36–41] stays here.

### Before T3.6 (moved verbatim)

1. **Special classes first, then generalize**: if the general problem stalls, solve named classes where small instances defeat solvers, then fold the modules into the general code. Case: "Therefore, about ten years ago, we decided to concentrate on special classes of mixed-integer nonlinear programs" (2002 preface, co) [02 P1]; 12 specialized modules in 1998, none in 2026 [03 §C1].

<a id="heuristic-2"></a>

## Heuristic 2: Problem knowledge into the model before solver options

### Full-text evidence (08 §2.6, copied)

| Heuristic | Cards | Strongest new evidence | Variant or calibration |
|---|---|---|---|
| H2 Problem knowledge before options | 14 | CONVEX EQUATIONS: 99.5% gap reduction, 35 vs 1793 nodes [S003 p. 17]; a stationarity condition proves globality at the root instead of after 29 nodes, while a local solver declares the model locally infeasible [S069 preprint pp. 8–9]; equclass [S012 manual p. 12]; physically meaningful bounds [S185 pp. 7, 12]; added chemical constraints cut the solve from 45 to about 30 minutes [S035 pp. 12–13]; bounded problems solved more often by DFO codes [S001 pp. 20, 36, 41] | Calibration: the relaxation-only construct pays in local-search time, not in global search: "CPU time gains by using this construct as opposed to merely adding the nonlinear constraints to the nonlinear formulation were not significant as far as global search is concerned" [S069 preprint p. 22] |

### Added in T3.6

- + a convexity declaration: 35 vs 1793 nodes [S003 p. 17]. The calibration that relaxation-only constraints pay in local-search time rather than global search [S069 preprint p. 22] stays here.

### Review fixes (T3.6)

- + DM5 (a channel for knowledge the solver cannot infer).

### Before T3.6 (moved verbatim)

2. **Problem knowledge into the model before solver options**: finite physical bounds, no huge "safe" bounds, convexity declared only when proven, relaxation-only constraints passed to the solver. Case: "Tight bounds based on physical or problem-specific knowledge are often more valuable than any algorithmic option in this manual." (manual §4.1, firm) [02 X5]; doi:10.1007/s10898-004-2705-8 [02 I6].

<a id="heuristic-3"></a>

## Heuristic 3: Users' models as bug finder and agenda

### Full-text evidence (08 §2.6, copied)

| Heuristic | Cards | Strongest new evidence | Variant or calibration |
|---|---|---|---|
| H3 Users' models as bug finder | 9 | Numerical difficulties to be reported to the developers [S012 manual p. 4; S162 p. 39]; 163 researchers and users submitted over 6,100 problems between October 1999 and July 2002 [S162 p. 2]; sponsors' processes as projects [S183 pp. 1, 8; S334 p. 2] | Count: §3.2 item 16 |

### Added in T3.6

- Count corrected with its source (08 §3.2 item 16): 163 researchers and users, October 1999 to July 2002, in the 2002 manual [S162 p. 2]; the book's acknowledgments, read in web research, give 164 to August 2002 [02 I4]. Both are kept: the end dates differ.

### Before T3.6 (moved verbatim)

3. **Users' models as bug finder and agenda**: ask for the failing model, credit the source in the log. Case: "If everything else fails, send us the .bar file with your model." (manual §13.3) [03 §C5]; 164 users submitted over 6100 problems to the BARON portal, 1999-2002 (2002 book acknowledgments) [02 I4].

<a id="heuristic-4"></a>

## Heuristic 4: Each baseline in its strongest fair mode; filter honestly

### Full-text evidence (08 §2.6, copied)

| Heuristic | Cards | Strongest new evidence | Variant or calibration |
|---|---|---|---|
| H4 Strongest fair baseline | 13 | Competitors chosen by the switch they allow [S046 arXiv p. 15]; stronger CPLEX aggregator settings as a second baseline [S239 p. 22]; a rival rebuilt inside the own solver [S116 arXiv p. 29]; trivial instances set apart by a written rule [S044 p. 17]; equal-task timing [S182 arXiv p. 6] | A domain baseline run at defaults, with one tuned rerun and its developer consulted [S198 p. 7]; an ANN baseline tuned as typical users do [S206 manuscript pp. 13–14] |

### Added in T3.6

- + a stronger CPLEX setting as a second baseline [S239 p. 22]. Competitors chosen by the switch they allow [S046 arXiv p. 15] is in Method 2 step 4 and Workflow C step 3.

### Before T3.6 (moved verbatim)

4. **Each baseline in its strongest fair mode; filter honestly**: force MIP solvers into global mode, wrap closed code, best hardware for ML baselines, list deteriorations. Case: "set the CPLEX option optimalitytarget to 3 and the GUROBI option nonconvex to 2" (Nohra §3.6) [03 §B3]. Practice only.

<a id="heuristic-5"></a>

## Heuristic 5: Measure the ceiling before learning a rule

### Full-text evidence (08 §2.6, copied)

| Heuristic | Cards | Strongest new evidence | Variant or calibration |
|---|---|---|---|
| H5 Measure the ceiling first | 4 | Every instance solved under each setting; labels within 10% dropped [S212 p. 10]; per-instance best 57% against one setting for all 34% [S084 preprint pp. 8, 11] | A hand-made rule scored against exact enumeration and the worst rule [S116 arXiv pp. 20–21]; a perfect-information oracle as ceiling [S034 arXiv p. 17] |

### Added in T3.6

- The case now cites the card of the probing paper [S212 p. 10] (it cited the DOI before) and adds the tuning ceiling [S084 preprint pp. 8, 11].

### Review fixes (T3.6)

- The case + the ceiling's numbers, about 40% (MINLP) and 25% (NLP) [S212 p. 10], which the pre-T3.6 copy quoted and the condensation dropped (usefulness review).

### Before T3.6 (moved verbatim)

5. **Measure the ceiling before learning a rule**: solve every instance under each setting; judge the learned rule against the per-instance best; drop ambiguous labels (<10% difference). Case: probing paper [03 §B2]. Practice only.

<a id="heuristic-6"></a>

## Heuristic 6: Reproducible by construction

### Full-text evidence (08 §2.6, copied)

| Heuristic | Cards | Strongest new evidence | Variant or calibration |
|---|---|---|---|
| H6 Reproducible by construction | 10 | Version, build and the paper to cite in every log [S112 v17.4.1 p. 10; S159 v15.2 p. 9; S012 manual p. 3]; nondeterministic options flagged [S159 v15.2 p. 20; S112 v17.4.1 pp. 21–22; S191 p. 22]; machine-independent counts and machine ratings in 2004 [S014 pp. 20–21]; permuted replicas with distinct seeds [S239 pp. 17–18] | Version and machine not named in a 2025 paper [S212 pp. 9–10] |

### Added in T3.6

- + nondeterministic options flagged in the manual [S191 p. 22]; version, build and paper to cite in every log [S112 v17.4.1 p. 10] went to Method 2 step 3. The 2025 paper that names no version or machine [S212 pp. 9–10] is a variant kept here.

### Before T3.6 (moved verbatim)

6. **Reproducible by construction**: named versions, deterministic work limits, single thread, pinned seeds. Case: "Random seeds are now pinned in BARON's subsolvers for deterministic behavior across runs." (2026.9.10) [03 §D3]; cite BARON by "mentioning the version of the software utilized" [03 §F1].

<a id="heuristic-7"></a>

## Heuristic 7: Keep evidence and proof apart

### Full-text evidence (08 §2.6, copied)

| Heuristic | Cards | Strongest new evidence | Variant or calibration |
|---|---|---|---|
| H7 Evidence apart from proof | 17 | Local values reported beside certified optima [S025 pp. 14–15]; a gap labelled as a gap to the LP bound [S029 preprint p. 26]; optimality claimed only where the a posteriori ratio is 1 [S119 preprint pp. 18, 20]; every heuristic value with a dual bound and a gap [S243 p. 32; S238 manuscript pp. 17–20]; the multistart mode labelled a heuristic [S185 pp. 2, 5–6; S112 v17.4.1 p. 18] | "Proof of global optimality" wording with tolerances unstated [S190 pp. 1, 14–17] (Inner Tension 7) |

### Added in T3.6

- + local values reported beside certified optima since 1999 [S025 pp. 14–15]. The gap labelled as a gap to the LP bound [S029 preprint p. 26] went to Method 6 step 5 and Taste mark 3.

### Before T3.6 (moved verbatim)

7. **Keep evidence and proof apart**: never present a multistart value as a global optimum. Case: "It does not prove global optimality." (manual §10.4) [02 J4]; outputs ending "*** Globality is therefore not guaranteed ***" [03 §D4].

<a id="heuristic-8"></a>

## Heuristic 8: Keep the rival's insight, replace the part that clashes with practice

### Full-text evidence (08 §2.6, copied)

| Heuristic | Cards | Strongest new evidence | Variant or calibration |
|---|---|---|---|
| H8 Keep the rival's insight | 2 | A rival's constancy insight kept and its enumeration replaced [S014 pp. 4, 8]; trust-region radius shrinking kept, its geometry rules relaxed [S170 pp. 3, 23] | Adds two written cases to the one ASR source |

### Added in T3.6

- + two written cases [S014 pp. 4, 8; S170 pp. 3, 23] beside the one ASR source.

### Before T3.6 (moved verbatim)

8. **Keep the rival's insight, replace the part that clashes with practice**. Case: on DIRECT, "the interesting thing that I feel uh Jones came up with was a way to do this selection of boxes" and "what I don't like though about this algorithm is this tri-section" (TAMU 2025, ASR [0:45:29]-[0:45:46]) [02 I8].

<a id="heuristic-9"></a>

## Heuristic 9: Probe options with cheap, complete student projects

### Full-text evidence (08 §2.6, copied)

| Heuristic | Cards | Strongest new evidence | Variant or calibration |
|---|---|---|---|
| H9 Cheap complete student projects | 2 | The true black-box applications of the 2013 study were MS theses in the same department [S001 p. 41]; an MS thesis of the same title as S084 (per note 04) | — |

### Added in T3.6

- + the black-box applications of the 2013 study were MS theses in the same department [S001 p. 41].

### Review fixes (T3.6)

- [S001 p. 41] → [S001 pp. 41–47]: p. 41 says the black-box applications are detailed elsewhere; the MS theses are identified in the references, pp. 42–47 (card c03). The same page fix is applied to the 08 §9 *Partners* paragraph and its copies.

### Before T3.6 (moved verbatim)

9. **Probe options with cheap, complete student projects**. Case: "This problem will serve to train Keith in the area of global optimization, before he embarks on the study of more complex problems." (CAPD, Jan 2008) [03 §C4]; 38 MS students 2015-19 [06 §2]. Practice only.

<a id="heuristic-10"></a>

## Heuristic 10: When the problem source moves, keep the engine

### Full-text evidence (08 §2.6, copied)

| Heuristic | Cards | Strongest new evidence | Variant or calibration |
|---|---|---|---|
| H10 Keep the engine when the source moves | 8 | Global optimization proposed for stochastic and chance-constrained programs [S002 manuscript pp. 18–22]; the DFO engine moved to a materials-science group's devices [S205 p. 1]; sponsors' engineers as co-authors [S181 pp. 1, 5; S183 p. 8] | Abstract-level cases: chip layout, planning as concave minimization, fuzzy programs, robust control [S051; S093; S041; S176] |

### Added in T3.6

- + the DFO engine taken to a materials-science group's devices [S205 p. 1]. The stochastic-programming case [S002 manuscript pp. 18–22] and sponsors' engineers as co-authors [S181 pp. 1, 5; S183 p. 8] stay here.

### Before T3.6 (moved verbatim)

10. **When the problem source moves, keep the engine**. Case: turns follow institutional moves with a 1-3 year lag (inferred) [06 §4.2]; "In our group, we also develop the algorithms ourselves and then we apply them to many application domains" (press 2018) [04 §1.6].

<a id="heuristic-11"></a>

## Heuristic 11: Find which bound stalls, then split the labour

### Full-text evidence (08 §4, §5, copied)

| Cluster (merged by meaning) | Works read in full/part | 1 Recurrence | 2 Say–do | 3 Executable, non-standard | 4 Exclusivity | Result |
|---|---|---|---|---|---|---|
| Find which bound stalls, then split the labour | S046, H007, S128, S165, S243, S238 (6; S243 and S165 one project) | ✅ 2017–2026 | ✅ the papers state the diagnosis [H007 p. 14; S165 manuscript p. 11; S243 p. 17] | ✅ | ✗ primal and dual bound analysis and matheuristic incumbents are common in MIP practice | Heuristic H11 (§5) |

### H11 (proposed) · Find which bound stalls, then split the labour

**One line**: before building anything for a hard application MINLP, run it through two general global solvers and read the primal and dual sides separately; if the dual side stalls, the work belongs in reduction and relaxation; if the primal side stalls, write a problem-specific method whose only job is the incumbent and leave the full model and the bound to the general solver.

**Cards**: scaled-time primal and dual convergence profiles of the solved instances [H007 pp. 14, 17]; the tail of an ablated profile read as proof versus search [S046 arXiv p. 16]; a preliminary two-solver run that names the primal side as the bottleneck [S165 manuscript p. 11; S243 p. 17]; "In all instances tested, except for the small case study, the nonlinear solver BARON failed to provide a good upper bound within 3 hours." [S238 manuscript p. 17]; decompositions that supply only incumbents, handed to SCIP [S165 manuscript pp. 13–24; S243 pp. 18, 30]; a framework for incumbents with BARON for the lower bound, the better bound of each reported [S128 arXiv pp. 19, 24]; approximations that map to feasible solutions, set against a valid lower bound [S238 manuscript pp. 10–20].

**Checks**: recurrence ✅ (four projects, 2017–2026); say–do ✅ ("To assess whether improving the primal bound or the dual bound took longer in our study, we analyzed solver convergence for the instances solved to global optimality." [H007 p. 14]; "able to improve the dual bounds consistently but have trouble obtaining primal (feasible) solutions" [S165 manuscript p. 11]); executable ✅; exclusivity ✗ (§4) → heuristic. The papers are student-first with Dey; the attribution is shared.

**Steps**: (1) run the compact model under one budget in two general solvers and record primal bound, dual bound and gap separately [S165 manuscript p. 11]; (2) on solved instances, plot scaled bound progress against scaled time, and do not use the plot to rank solvers [H007 pp. 14, 17]; (3) dual side stalls → Methods 1 and 5; (4) primal side stalls → a decomposition or restriction for the incumbent (a budgeted master with a feasibility subproblem and no-good cuts; a restriction to the peak periods; a piecewise-linear restriction) [S165 manuscript pp. 13–22; S128 arXiv pp. 13–17; S238 manuscript pp. 8–14]; (5) hand the incumbent to the general solver, report solver-alone against heuristic-then-solver at equal total time with primal, dual and gap per scenario, and the better bound of each [S165 manuscript pp. 24, 28–29; S243 p. 32; S128 arXiv p. 24].

**Stop rule**: a heuristic value is reported only beside a valid dual bound (Heuristic 7).

**Where it goes**: a new heuristic; Workflow B1 step 3 cites it (§3.2 item 15); Inner Tension 1 gains a resolution seen in practice, general solver for the bound and tailored method for the incumbent [S128 arXiv p. 24].

### Added in T3.6

- Added as Heuristic 11 (08 §5): recurrence, say–do and executable pass, exclusivity fails, so a heuristic, not a method. SKILL.md: one procedure line with [H007 p. 14; S165 manuscript pp. 11, 24; S128 arXiv p. 24]; the H007 quote and the steps with all their cards are in the 08 text above. Attribution shared: student-first papers with Dey.
- It supplies Workflow B1 step 3's sources (08 §3.2 item 15) and a working resolution of Inner Tension 1 [S128 arXiv p. 24]; the Roundtable Card asks *Which bound stalls, the primal or the dual?* third.

### Review fixes (T3.6)

- **Written into steps, as 08 §5 allows.** The numbered H11 left the heuristic list, which is back at ten, inside the 5–10 band of research-extraction-framework.md §三 (rules review; 08 §5 had flagged the list as two above the band). Its procedure is Workflow B1 step 3 (primal and dual read apart; the primal-side recipe [S128 arXiv pp. 9–17; S165 manuscript pp. 13–17, 24]) and Agentic Protocol Step 2; its question stays third on the Roundtable Card. Nothing above is deleted, and SKILL.md links here from Workflow B1 step 3.
- **Attribution corrected.** H007 is Kuznetsov & Sahinidis, with no Dey (card c07); S046 is Puranik & Sahinidis; of this cluster only S128, S165 and S238 are with Dey. *The papers are student-first with Dey* (08 §5 above) and *Attribution shared: student-first papers with Dey* (*Added in T3.6*) hold only for those three (fidelity and usefulness reviews).
- The no-feasible-point case cites S165 [S165 manuscript p. 11]; H007 p. 17 shows dual bounds lagging, with optima often found by local search in preprocessing.

### Before T3.6

Not in SKILL.md before T3.6; Workflow B1 step 3 called its test *inferred from Method 1; no source states this test* (kept in [Workflow B1](#workflow-b1)).

<a id="heuristic-12"></a>

## Heuristic 12: When the model's data are estimates, return the ranked pool

### Full-text evidence (08 §4, §5, copied)

| Cluster (merged by meaning) | Works read in full/part | 1 Recurrence | 2 Say–do | 3 Executable, non-standard | 4 Exclusivity | Result |
|---|---|---|---|---|---|---|
| Return the ranked pool when the model's data are estimates | S058, S035, S162, S022, S070 (5; abstracts S048, S184, S174) | ✅ 2000–2021 | ✅ [S058 preprint p. 22]; [S070 manuscript p. 13] | ✅ | ✗ generate-and-test pools are standard in molecular design [S022 arXiv pp. 20, 22] | Heuristic H12 (§5) |

### H12 (proposed) · When the model's data are estimates, return the ranked pool, not one optimum

**One line**: if the coefficients come from estimation (group contributions, fitted properties), certify the optimum, then list the K best or all feasible designs and let higher-fidelity models or experiments pick.

**Cards**: "Although [33] uses an algorithm that guarantees global optimality, we still obtain several non-global solutions to the problem in order to alleviate the difficulty due to uncertainty in the thermodynamic property estimation techniques that were used." [S058 preprint p. 22]; "The capability to identify all, or the K best, solutions of an integer program was added to the general purpose BARON solver after successful implementation in the context of this molecular design problem." [S035 p. 11]; K-best by changing the fathoming step [S162 pp. 25–26; S012 manual pp. 5–6]; "This smaller pool of compounds can then be investigated using high-order models or experiments." [S022 arXiv p. 12]; the solver feature traced to molecular design [S070 manuscript p. 13]; abstracts [S048; S184; S174].

**Checks**: recurrence ✅ (2000–2021, refrigerants, molecular design, phasing, DNA assembly); say–do ✅ (quotes above); executable ✅; exclusivity ✗ (§4) → heuristic.

**Steps**: (1) solve to certified global optimality; (2) list the pool in one tree (K-best fathoming) or by integer cuts that exclude each earlier solution [S035 p. 11; S058 preprint p. 22]; (3) rank it and re-rank with higher-order models or experiments [S022 arXiv pp. 12–13, 23]; (4) report how many pass the finer screen and which are new (44 solutions, 29 admissible, nine not in earlier work [S035 pp. 12–13]); (5) say when a design space is small enough that enumeration would do [S022 arXiv p. 25].

### Added in T3.6

- Added as Heuristic 12 (08 §5), which takes the list to twelve, two above the framework's 5–10 band; 08 allows folding it into Workflow D, and SKILL.md does both: the heuristic, and Workflow D step 6 pointing to it. SKILL.md cites [S035 p. 11; S058 preprint p. 22; S022 arXiv p. 12]; the quotes and steps are above.

### Review fixes (T3.6)

- **Written into Workflow D step 6, as 08 §5 allows**; the heuristic list is back at ten (rules review). The step carries the procedure and the cards [S035 p. 11; S058 preprint p. 22; S022 arXiv p. 12] and links here. Method 2's K-best item [S035 p. 11] is evidence for Method 2 (an application class became an engine feature), not a second copy of this heuristic.

### Before T3.6

Not in SKILL.md before T3.6.

<a id="anatomy-branch-and-reduce"></a>

## Anatomy: A branch-and-reduce approach to global optimization (1996)

### Full-text evidence (08 and cards)

| # | SKILL.md location and current text | Full-text finding | Proposed change |
|---|---|---|---|
| 4 | Method 1 Limitations, *the 1995-96 full texts were not read* | Still true; the rule's full-text statements are [S077 pp. 12, 15; S058 preprint pp. 6–7] and its restatement with proof [S006 p. 15] | §2, Method 1 |
| 11 | Signature Work Anatomy 1996, *Minimum evidence: Ryoo's 1995 MS thesis on range reduction [01 SW1]* | Two primary records disagree: the CV lists the thesis under 1995 (RESOURCES row 330), while the 1996 paper's own reference list dates it 1994 (reference 53 on the Springer page read in round 2 for the abstract-level card [S013]). The thesis itself could not be looked up | Drop the year: *Ryoo's MS thesis on range reduction* |

| Point | Check | Result |
|---|---|---|
| (1) Ryoo's MS thesis year | CV entry via RESOURCES row 330; the 1996 paper's reference list on its Springer page (saved in round 2) | Conflict, 1995 vs 1994: drop the year (§3.2 item 11) |

- **The founding texts are still abstracts**: Ryoo & Sahinidis 1995 [S008] and 1996 [S013] and the 1996 BARON note [S004]. Branch-and-reduce's origin rests on the 2000 manual, the 2000 applications paper and the 2004 restatement [S077 pp. 7–21; S058 preprint pp. 4–9; S006 pp. 11–17].

### Added in T3.6

- Key insight: + the founding papers are abstract-level cards [S008; S013; S004] and the rule's full-text statements [S077 pp. 12, 15, 20–21; S006 p. 15] (08 §3.2 item 4).
- Minimum evidence: *Ryoo's 1995 MS thesis* → *Ryoo's MS thesis on range reduction (year disputed between primary records)*: the CV lists the thesis under 1995 (RESOURCES row 330), the 1996 paper's own reference list dates it 1994 (Springer page read for the abstract-level card [S013]); the thesis could not be looked up (08 §3.2 item 11, §3.3 point 1). Operator point (1) settled by dropping the year.

### Review fixes (T3.6)

- Key insight condensed into one parenthesis, with the same cards [S008; S013; S004; S077 pp. 12, 15, 20–21; S006 p. 15].

### Before T3.6 (moved verbatim)

**A branch-and-reduce approach to global optimization (Ryoo & Sahinidis, J. Glob. Optim. 8(2), 1996, doi:10.1007/BF00138689; also doi:10.1016/0098-1354(94)00097-2, doi:10.1007/BF00138693)**

- **Origin**: stated (co, 2002): no software solved small MINLPs globally, so special classes first; inferred: molecular-structure grant and talks 1992-93 [06 Turn B]. **Why then** (inferred): an industrial-engineering post where reduced-cost fixing was standard; GAMS for prototyping.
- **Key insight**: range contraction from duals and the incumbent, at every node. **Minimum evidence**: Ryoo's 1995 MS thesis on range reduction [01 SW1].
- **Abandoned**: the direct general attempt; molecular mechanics (no 1990s paper). **Reception**: Neumaier et al. 2005 found it fastest and most robust, with wrong claimed optima before fixes [05 A1]. **Shows**: Methods 1-2, Heuristic 1.

<a id="anatomy-minlp-2004"></a>

## Anatomy: Global optimization of mixed-integer nonlinear programs: a theoretical and computational study (2004)

### Full-text evidence (08 and cards)

Card S006 (read in full, all 29 pages; co-authored with Tawarmalani, first author):
- **Origin**: received January 24, 2000, accepted July 17, 2003; funded by ExxonMobil Upstream Research and NSF; it condenses Tawarmalani's 2001 PhD thesis, cited for proofs and for computational experience on "over 500 problems" [S006 pp. 1, 7, 23].
- **Key insight**: a Lagrangian with a homogenizing multiplier defines one range-reduction problem from which optimality-based, marginals-based, probing, Zamora-Grossmann and feasibility-based reductions follow; new are duality-based reduction from stored duals and a learning reduction after fathoming [S006 pp. 12–19]; the 1996 cut is "either the same ... or weaker" [S006 p. 15]. Relaxations by recursive decomposition with one auxiliary variable per distinct subexpression, convex pieces outer-approximated by tangents, so that every node solves an LP [S006 pp. 4–7]; violation-transfer branching [S006 pp. 19–21].
- **Minimum evidence**: thirteen small concave QPs with and without probing; Phillips-Rosen instances against published GOP times; cardinality-constrained 0-1 hyperbolic programs against CPLEX 6.0 (BARON faster on 6 of 8); 34 MINLPLib problems, four with better global values than their source, which used local NLP solutions [S006 pp. 23–27].
- **Method links on the card**: Method 1 evidence (strong), Method 5 evidence and variant, Method 2 evidence and variant, Heuristic 1 evidence, Heuristic 7 evidence, Taste mark 2 evidence. Quote on the card: "Nonlinear programming solvers, however, often fail even in solving convex problems." [S006 p. 3].

### Added in T3.6

- New anatomy (the task allows one or two of important works read in full): his fourth most-cited work by the INDEX Cites column (836), and the full-text home of the range-reduction rule that the 1996 anatomy could cite only through restatements (08 §3.2 item 4). SKILL.md rows: Origin [S006 p. 1]; Key insight [S006 pp. 4–7, 12–19] (PD1, DM3); Minimum evidence [S006 pp. 24–27]; Reception: the 2005 paper extends it [S003 pp. 1–2].

### Before T3.6

Not in SKILL.md before T3.6 (new anatomy of a work read in full).

<a id="anatomy-polyhedral-branch-and-cut"></a>

## Anatomy: A polyhedral branch-and-cut approach to global optimization (2005)

### Full-text evidence (08 and cards)

| # | SKILL.md location and current text | Full-text finding | Proposed change |
|---|---|---|---|
| 12 | Signature Work Anatomy 2005, *Key insight: constructive convex envelopes; entirely linear relaxations*, and its minimum-evidence figure *by up to 100%* | The operative insight is lifted outer approximation: linearize a composition layer by layer in lifted variables, which is tighter than direct linearization and, for separable sums, matches what direct linearization needs exponentially many cuts to reach [S003 pp. 3–7]; constructive envelopes appear only as one proposition [S003 pp. 13–14]. The 100% figure is the top of a range in the abstract [S003 p. 1]; the body gives average root-gap reductions of 48% on globallib and 20% on minlplib (27% without one explained outlier) [S003 pp. 19–21] | Correct the key insight; add the averages beside the abstract figure |
| 13 | Signature Work Anatomy 2005, *Abandoned: the 2000 mixed-integer SDP module (gone by 2026, reason unknown)* | The module is documented in 2000 [S077 pp. 92–95] and still in the 2004 code [S006 p. 23]; no card gives a reason | Add the dates; reason still unknown |

### Added in T3.6

- Key insight corrected (08 §3.2 item 12): *constructive convex envelopes; entirely linear relaxations* → lifted outer approximation [S003 pp. 3–7], constructive envelopes one proposition [S003 pp. 13–14].
- Minimum evidence: the abstract's *by up to 100%* kept, with the body's averages beside it (48% globallib, 20% minlplib) [S003 pp. 19–21] and the full-solve result [S003 p. 21]. The 27% figure without one explained outlier [S003 pp. 19–21] stays here.
- Abandoned: the SDP module dated 2000–2004 [S077 pp. 92–95; S006 p. 23]; reason still unknown (08 §3.2 item 13). Why then + [S003 p. 1].

### Before T3.6 (moved verbatim)

**A polyhedral branch-and-cut approach to global optimization (Tawarmalani & Sahinidis, Math. Program. 103(2), 2005, doi:10.1007/s10107-005-0581-8; book doi:10.1007/978-1-4757-3532-1)**

- **Origin**: student-driven theory (Tawarmalani MS 1997, PhD 2001). **Why then**: LP robust, NLP not (2005 abstract).
- **Key insight**: constructive convex envelopes; entirely linear relaxations. **Minimum evidence**: root gaps on 87 GlobalLib/MINLPLib problems reduced "by up to 100%".
- **Abandoned**: the 2000 mixed-integer SDP module (gone by 2026, reason unknown); polyhedral-only stance revised 2018. **Reception**: INFORMS Computing Society Prize 2004, Beale-Orchard-Hays Prize 2006 [01 SW2]. **Shows**: Methods 5, 2.

<a id="anatomy-approximation-hens"></a>

## Anatomy: Approximation algorithms for the minimum number of matches problem (2004)

### Full-text evidence (08 and cards)

Card S119 (read in full, a preprint dated 1 January 2004; co-authored with Furman, Sahinidis corresponding):
- **Origin**: the minimum-number-of-matches subproblem is strongly NP-hard [S024 manuscript pp. 10–25] and well understood, so it is chosen to illustrate approximation algorithms [S119 preprint p. 3]; the 2002 review's open problem asks for approximation algorithms with guarantees [S010 preprint p. 8]; the paper places itself in a line on "introducing rigor in the use and practice of heuristics" [S119 preprint p. 2].
- **Key insight**: five approximation algorithms on the transportation formulation [S119 preprint pp. 6–16]; a performance guarantee valid for any heuristic from two bounds computable from the input, and an a posteriori ratio from the best relaxation bound [S119 preprint p. 18]; the N - 1 targeting rule refuted as an upper bound by a two-stream counterexample [S119 preprint p. 17].
- **Minimum evidence**: 29 literature problems (6 to 40 streams): guarantee 1.67 to 15 (mean 6.45), a posteriori ratio 1 to 2.93 (mean 1.79); ratio 1 certifies two problems without an IP; CPLEX 7.0 stalls on five problems after 7 to 41 CPU hours; no algorithm dominates [S119 preprint pp. 19–22].
- Quotes on the card: "Although the use of heuristics has been prevalent in the process synthesis literature, their justification has been exclusively based on empirical evidence obtained through computational testing." [S119 preprint p. 1]; "As seen in Tables 3 and 4, no single approximation algorithm dominates all others for the entire data set." [S119 preprint p. 21].

### Added in T3.6

- New anatomy, as 08 §4 suggests (*the natural Signature Work Anatomy entry for this method*). SKILL.md rows: Origin [S024 manuscript pp. 10–25; S010 preprint p. 8]; Key insight [S119 preprint p. 18] (PD6); Minimum evidence [S119 preprint pp. 19–21]; Abandoned: the line goes quiet after 2004, with echoes in 2021 and 2026 [S213; S238 manuscript pp. 10–14]; Reception: not read (no card on its reception). The DOI is the one on the card header (doi:10.1021/ie049978l).

### Review fixes (T3.6)

- Origin: *strong NP-hardness of every published formulation [S024 manuscript pp. 10–25]* → *strong NP-hardness of the matches problem [S024 manuscript pp. 10–12]* (Theorem 2 and Corollaries 1–3; see [Method 6](#method-6)).
- Abandoned shortened to a pointer to Method 6, which carries the dates and the 2021 and 2026 echoes [S213; S238 manuscript pp. 10–17] (usefulness review: the anatomy restated Method 6).

### Before T3.6

Not in SKILL.md before T3.6 (new anatomy of a work read in full).

<a id="anatomy-dfo-review"></a>

## Anatomy: Derivative-free optimization: a review of algorithms and comparison of software implementations (2013)

### Full-text evidence (08 and cards)

| # | SKILL.md location and current text | Full-text finding | Proposed change |
|---|---|---|---|
| 7 | Method 4 Say–do, *✅ for the 2013 and 2022 studies*; the 2013 hold-out *kept as a disagreement* | 2013: optima certified "for most" problems [S001 p. 21]; the unseen set is the same 502 problems after an affine change of variables with condition number 2 [S001 p. 41], which settles the disagreement toward note 03's reading, although the authors write that the transformation "otherwise changes the problems considerably, including the shape of the objective functions and location of all local solutions" [S001 p. 41]. 2022: steps 1–3, 5 and 6 hold; no developer rounds, no hold-out, and a bare 2,500-evaluation budget [S063 p. 13] | Rewrite the say–do line with these qualifiers and drop the disagreement note |

### Added in T3.6

- Key insight + its yardstick page [S001 p. 21]; Minimum evidence + the final study's numbers [S001 pp. 14, 20] and the affine-transform hold-out [S001 p. 41] (08 §3.2 item 7). The one-lens taxonomy (which point to evaluate next) [S001 pp. 11–13] is catalog WM5; the 2026 rerun on 42 codes [S272 pp. 4–5] is in Method 4's Practice.

### Before T3.6 (moved verbatim)

**Derivative-free optimization: a review of algorithms and comparison of software implementations (Rios & Sahinidis, J. Glob. Optim. 56(3), 2013, doi:10.1007/s10898-012-9951-y)**

- **Origin**: simulator and lab applications (NIH, NETL, NSF). **Why then**: "the number of available derivative-free optimization solvers has more than quadrupled" (§1).
- **Key insight**: judge black-box solvers against optima certified by an algebraic global solver. **Minimum evidence**: CAPD Jan 2008, 225 problems and 18 solvers; final study 22 solvers, 502 problems [03 §C3].
- **Abandoned**: the promised unified DFO interface [03 §E5]. **Reception**: his most-cited paper; critiques on constraints, ageing, aggregation [05 A7]; the 2022 sequel won the JOGO Best Paper Award. **Shows**: Method 4.

<a id="anatomy-alamo"></a>

## Anatomy: Learning surrogate models for simulation-based optimization (2014)

### Full-text evidence (08 and cards)

| # | SKILL.md location and current text | Full-text finding | Proposed change |
|---|---|---|---|
| 5 | Method 3 Limitations, *the 2014 and 2015 full texts were not read* | 2015 read; it is the source of step 4 [S039 manuscript pp. 4–5, 7–9] | §2, Method 3 |

- **ALAMO's founding paper** (2014) [S009] and the 2018 symbolic-regression MINLP [S055] are abstracts; the method is read in its 2015 and 2017 forms [S039; S017].

### Added in T3.6

- Key insight + *2014 abstract only; read in its 2015 and 2017 forms* [S009] (08 §3.2 item 5, §11); Minimum evidence now cites the card [S017 pp. 13–14] (it cited arXiv:1705.10918 through note 01 before).

### Review fixes (T3.6)

- Minimum evidence: [S017 pp. 13–14] → [S017 pp. 11–12]: the 120-of-150 result and the LHS-50 comparison are on pp. 11–12; pp. 13–14 hold the constrained-regression results.

### Before T3.6 (moved verbatim)

**Learning surrogate models for simulation-based optimization (Cozad, Sahinidis & Miller, AIChE J. 60(6), 2014, doi:10.1002/aic.14418; also arXiv:1705.10918, doi:10.1007/s10107-018-1289-x)**

- **Origin**: DOE NETL fellowship and the Carbon Capture Simulation Initiative [06 Turn G]. **Why then**: "integer optimization algorithmic advances combined with improved hardware have recently allowed for the best subset problem to be practically solved" (2017, co) [02 P4].
- **Key insight**: best subset by integer programming + adaptive sampling + first-principles constraints. **Minimum evidence**: in 2017, error-maximization sampling beat equal-size LHS in 120 of 150 problems, with losses to LHS-50 reported.
- **Abandoned**: not documented. **Reception**: R&D 100 (2016); the finite-basis critique answered by the 2018 MINLP formulation [05 A8]. **Shows**: Method 3.

<a id="anatomy-hybrid-lp-nlp"></a>

## Anatomy: A hybrid LP/NLP paradigm for global optimization relaxations (2018)

### Full-text evidence (08 and cards)

| # | SKILL.md location and current text | Full-text finding | Proposed change |
|---|---|---|---|
| 6 | Method 5 Limitations, *full texts of the 2004, 2005 and 2018 papers were not read* | 2004 and 2005 read [S006; S003]; 2018 abstract only [S030] | §2, Method 5 |

- **The 2018 turn of Inner Tension 2** rests on abstracts [S030; S027]; per-node switching is read only in its 2021–22 forms [S116; S133].

### Added in T3.6

- Minimum evidence: the quote is the abstract's, on the abstract-level card [S030]; per-node switching is read in its 2021–22 forms [S116 arXiv pp. 22–25] ([S133 arXiv pp. 21–22] also; 08 §11).

### Before T3.6 (moved verbatim)

**A hybrid LP/NLP paradigm for global optimization relaxations (Khajavirad & Sahinidis, Math. Program. Comput. 10(3), 2018, doi:10.1007/s12532-018-0138-5)**

- **Origin and why then** (inferred): rival solvers multiplied, NLP subsolvers matured; a chain of student and postdoc modules.
- **Key insight**: polyhedral and nonlinear relaxations with fail-safes and learned switching. **Minimum evidence**: "increases by 30% the number of problems that are solvable to global optimality within 500 s".
- **Abandoned**: the polyhedral-only doctrine; FilterSD off by default [03 §H]. **Reception**: SCIP 8 study, "a small lead of BARON before SCIP" (doi:10.1007/s10898-023-01345-1) [05 A2]. **Shows**: Methods 5, 2, 1.

<a id="anti-patterns"></a>

## Research Anti-patterns

### Full-text evidence (cards)

- "Declaration of an inferior solution as optimal by a convex programming solver is fatal in the application of branch-and-bound to global optimization problems." [S162 p. 23] (2002 GAMS/BARON 5.0 manual, co-signed with Tawarmalani); in 2004: "Nonlinear programming solvers, however, often fail even in solving convex problems." [S006 p. 3]; KKT checks of subsolver answers [S116 arXiv p. 22; S133 arXiv p. 19] (cards S116 and S133).

### Added in T3.6

- One row added: *An unchecked subsolver answer* with [S162 p. 23] and the KKT check as the remedy [S116 arXiv p. 22] → Method 5 step 5. A row for heuristics justified by testing alone was drafted and placed in the taste warnings instead (warning 4), so it appears once.

### Review fixes (T3.6)

- Column header *Why he opposes it (source)* → *Why the record opposes it (source)*: the rows come from firm manual text and co-authored papers (usefulness review).

### Before T3.6

The six earlier rows are unchanged in SKILL.md; the table is not repeated here.

<a id="trajectory"></a>

## Research Trajectory

### Full-text evidence (08 §8, copied)


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

### Added in T3.6

- 1986–1991: + *no full text read before 1996* (08 §1: 0 full texts in 1985–95).
- 1997–2007: + convexification became BARON's relaxations by 2004–05 [S006 pp. 4–7] and the complexity-and-approximation line to 2004 [S119 preprint p. 1] (08 §8, turns 1–2).
- 2007–2020: + the crystallography and protein line thins out and is absent from the cards after 2015 (08 §8: 12 carded works in 2006–10, 3 in 2011–15, none later).
- 2020–: + co-supervised network design with Dey, built partly outside BARON [S128 arXiv pp. 17–19] (08 §8, §2 Method 2).
- Closing paragraph: + the full texts agree that turns follow institutional moves, and the two constants of 08 §8 [S025 pp. 14–15; S272 p. 8; S077 p. 12; S190 pp. 4–9]. Note 06 is updated in its own T3.6 section.

### Review fixes (T3.6)

- Latest: + Khachiyan Prize 2026 (INFORMS Optimization Society prize page, checked 2026-11-20), moved from the Honest Boundary's *Unconfirmed* line ([Honest Boundary](#honest-boundary)). The Scope note's *the Latest paragraph [is] unchanged* is superseded on this point.

### Before T3.6 (moved verbatim)

**Research Trajectory**

- **1986-1991**: planning and scheduling MINLP, PhD with Grossmann (doi:10.1016/0098-1354(91)87008-w).
- **1991-1997**: deterministic global optimization; BARON from GAMS prototype to FTP release, after a move to industrial engineering (no stated reason for choosing global) (doi:10.1007/BF00138689).
- **1997-2007**: convexification theory; chemistry and biology informatics on NIH money; TOF founded 2001 (doi:10.1007/s10107-005-0581-8).
- **2007-2020**: at CMU with DOE NETL and industry: DFO benchmarks, ALAMO, ML with optimization, BARON's second generation (doi:10.1007/s10898-012-9951-y).
- **2020-**: at Georgia Tech ISyE: MIP/MINLP theory with colleagues, ML for solvers, norm convexification, BAM, self-driving labs (doi:10.1007/s10898-024-01424-x).

Turns follow institutional moves and funding with a 1-3 year lag; the engine stays (inferred) [06 §4].

<a id="lineage"></a>

## Academic Lineage and collaboration pattern

### Full-text evidence (08 §9, copied)


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

### Added in T3.6

- SKILL.md's Academic Lineage is unchanged in T3.6; the collaboration pattern above (08 §9) is the full-text record behind its statements, and note 06's T3.6 section summarizes it.

<a id="inner-tensions"></a>

## Inner Tensions

### Full-text evidence (08 §3, copied)

| # | SKILL.md location and current text | Full-text finding | Proposed change |
|---|---|---|---|
| 8 | Method 4 Say–do ⚠ and Inner Tension 5, *BAM claims rest on libraries ... no hold-out mentioned* | The same gap in the group's own algorithm papers [S170 pp. 24–29; S239 p. 16], in a 2008 crystallography code [S161 manuscript pp. 4–5, 7] and in 2025–26 talk slides that rank BAM first [S270 pp. 8, 14, 19; S272 pp. 5, 7–8, 14] | Extend Tension 5 from product pages to papers and talks |
| 9 | Inner Tension 1, "It appears unlikely that general-purpose algorithms will solve such problems exactly." (FOCAPO 2003, sole) | The sentence stands verbatim in the 2004 journal manuscript [S002 manuscript p. 22] and in the FOCAPO 2003 text (checked 2026-11-20 against the PDF at the URL in SKILL.md's Sources). The following sentence differs by version: the journal manuscript reads "Instead, we anticipate the development of problem-specific approximation schemes" and cites Ahmed & Sahinidis (2003) [S002 manuscript p. 22]; note 02's FOCAPO wording, with *we expect to see* and the year 2002, matches the FOCAPO PDF | Keep the quote; quote the follow-up only with its version and year |
| 10 | Inner Tension 2, *polyhedral-only (2005) vs hybrid LP/NLP (2018), a dated change on the same stated grounds* | A sequence, not one change. In 2000 the IQP module defaulted to a quadratic relaxation and a mixed-integer SDP module shipped [S077 pp. 40, 43, 53, 92–95]; in 2001 a theory paper proposed SDPs on strength [S032 pp. 2, 20]; in 2002 an LP was chosen by gap and time [S053 pp. 21–25]; in 2004 LP-only was argued from NLP unreliability while the code still linked NLP and SDP solvers [S006 pp. 3, 7, 23]; 2005 polyhedral [S003 pp. 1–2, 15]; 2011 SDPs priced at three orders of magnitude more time [S018 pp. 1, 18–19]; 2018 hybrid [S030]; 2021–22 SDP-quality bounds from convex quadratic cuts with per-node switching [S116 arXiv pp. 22–25; S133 arXiv pp. 12, 18–22]; 2025 a quadratic-relaxation hierarchy re-tested because convex QCQP solvers improved [S189 arXiv pp. 1–2; S211 arXiv pp. 2, 13–14] | Replace the two-point tension by this dated line; the constant is subsolver speed and reliability (Method 5 step 7) |

| Point | Check | Result |
|---|---|---|
| (2) The S002 p. 22 follow-up sentence | `S002` text p. 22 read; FOCAPO 2003 PDF fetched from the URL in SKILL.md's Sources and text-extracted (2026-11-20) | Both versions exist and both are his; note 02 quotes FOCAPO correctly; the journal manuscript differs (§3.2 item 9) |

### Added in T3.6

- Tension 1: the FOCAPO quote kept (08 §10 item 11); + the same sentence stands in the 2004 journal manuscript, whose next sentence differs [S002 manuscript p. 22] (operator point 2, checked at source in 08 §3.3); + a working resolution [S128 arXiv p. 24].
- Tension 2: the two-point contrast → the dated sequence of 08 §3.2 item 10 [S077 pp. 40, 92–95; S032 pp. 2, 20; S006 p. 3; S003 pp. 1–2; S030; S133 arXiv pp. 12, 18–22; S189 arXiv pp. 1–2]; the 2002 LP choice [S053 pp. 21–25], the 2011 pricing [S018 pp. 1, 18–19] and [S211 arXiv pp. 2, 13–14] are in the 08 text above.
- Tension 5: product pages → also papers and talks [S161 manuscript pp. 4–5; S170 pp. 24–29; S270 pp. 8, 14, 19] (08 §3.2 item 8; [S239 p. 16], [S272 pp. 5, 7–8, 14] in 08 §3.1).
- Tension 6: + the third-party view [S249 p. 24] (08 §2, Method 3). Tension 7: + [S190 pp. 1, 14–17] (08 §2.6, Heuristic 7 variant). Tensions 3 and 4 unchanged.

### Review fixes (T3.6)

- Tension 1: the FOCAPO quote is scoped to *integer and nonlinear stochastic programs*: in both versions the preceding sentence is "Computational results abound for the linear case but are somewhat limited for the integer and nonlinear cases" [S002 manuscript p. 22], and the next one expects problem-specific approximation schemes (card S002 D7–D8). Set against the deterministic *application agnostic* quote without that scope, it read as doubt about general-purpose MINLP solvers (usefulness review). *In practice* now names the paper: a co-supervised 2024 paper (Li, Dey & Sahinidis) pairs a tailored incumbent with the general solver's bound [S128 arXiv p. 24].
- Tension 2: the 2000 entry corrected. *A quadratic relaxation default and an SDP module in 2000 [S077 pp. 40, 92–95]* → *in 2000 the IQP module defaulted to a quadratic relaxation (the NLP module to a linear one) and a mixed-integer SDP module shipped [S077 pp. 40, 53, 92–95]*: pp. 40 and 92–95 document only the SDP module; the defaults are on p. 53 (qplin = 0 for IQP, nlpdolin = 1 for the factorable NLP module), and p. 8 says the NLP module allows an entirely LP-based approach (fidelity review). SKILL.md keeps four dates (2000, 2004–05, 2018, 2021–22); the 2001 [S032 pp. 2, 20], 2002 [S053 pp. 21–25], 2011 [S018 pp. 1, 18–19] and 2025 [S189 arXiv pp. 1–2; S211 arXiv pp. 2, 13–14] steps are in the 08 table above (usefulness review: bulk). The Tension 2 bullet of *Added in T3.6* is superseded on both points.
- Tension 5: *chosen with no hold-out (2025)* → *set with no hold-out reported (2025)* [S170 pp. 24–29]: card S170 records that the paper reports neither how the Table 3 defaults were set nor any hold-out set (fidelity review).

### Before T3.6 (moved verbatim)

**Inner Tensions**

- **Tension 1: general-purpose vs problem-specific.** "Application agnostic algorithms ... that was what particularly fascinated me" (press 2021) vs "It appears unlikely that general-purpose algorithms will solve such problems exactly." (FOCAPO 2003, sole) and "Many of the papers develop tailored algorithms that outperform general-purpose MINLP solvers." (2019, sole) [02 C1].
- **Tension 2: polyhedral-only (2005) vs hybrid LP/NLP (2018)**, a dated change on the same stated grounds (speed, robustness) [01 C8].
- **Tension 3: academic voice vs firm voice.** Papers conclude with portfolios and losses; firm pages claim "the fastest and most robust MINLP solver" and misquote their sources [05 2h].
- **Tension 4: open code praised vs closed solver.** "We wholeheartedly encourage researchers to post their executable files, if not their source code." (2016, co) vs BARON, BAM and recent algorithms closed or on request [02 C7; 03 §F2].
- **Tension 5: hold-out discipline vs product claims**: the 2013 overtraining check vs BAM claims on its development libraries [03 C1].
- **Tension 6: published method vs shipped default**: adaptive sampling published 2014, effectively off until 2020, default only from 2024 [03 C8].
- **Tension 7: certificates vs floating point.** Global guarantees as a mark of quality vs "BARON as a whole is not claimed to give mathematically rigorous results" (Kearfott 2011) and wrong optimal values found by independent testers [05 A1].

<a id="roundtable-card"></a>

## Roundtable Card

### Added in T3.6

- Leads when + *a heuristic needs a guarantee* (Method 6). First questions + *Which bound stalls, the primal or the dual?* as the third question (Heuristic 11). Default recommendation + the primal-side case (Heuristic 11). Will push back on + *heuristics justified by testing alone* (Method 6). Dey line + the co-authored network paper [S128 arXiv p. 24]. The Card stays short; lens, other disagreements and blind spots unchanged.

### Review fixes (T3.6)

- Leads when: *a heuristic needs a guarantee* → *a heuristic for a planning or synthesis problem needs a proven or computed bound* (Method 6's domain); primal heuristics for nonconvex MINLP belong to Workflow B1 step 3 (usefulness review).

### Before T3.6 (moved verbatim)

- **Leads when**: a nonconvex MINLP/MIQCQP must be certified by an off-the-shelf solver and stalls; bound tightening, presolve or probing is at issue; node relaxations must be chosen with cost in mind; a solver benchmark is being designed; a simulator must enter an MINLP; reproducibility matters.
- **First questions asked** (ask in this order): Does every nonlinear expression have finite physical bounds? Does any solver certify small instances today? Which whole library, certified optima and fixed protocol? What does each relaxation cost per node, and how often does it fail? Defaults, per library, losses, hold-out? Can the black box be made algebraic?
- **Default recommendation**: tighten bounds and reformulate with problem knowledge; run a general global solver with aggressive reduction at defaults; if it stalls, add a reduction or cheap relaxation for the hard structure inside the solver; judge by ablation over whole libraries under a deterministic protocol; conclude with a portfolio.
- **Will push back on**: huge "safe" bounds; heuristic values called global optima; single-winner claims; strong relaxations without time and failure counts; neural networks where a sparse algebraic model would do; showcase instances; unrepeatable runs.
  - *Dey*: problem-specific inequalities (doi:10.1109/TPWRS.2015.2402640) vs default solver judged by ablation (doi:10.1007/s10601-016-9267-5); co-authors.

<a id="honest-boundary"></a>

## Honest Boundary

### Full-text evidence (08 §1 and §11, copied)


| Item | Count | Source |
|---|---|---|
| Card entries | 294 in 30 batch files: round 1 core c01–c12 (41 cards) and supplement s01–s10 (72); round 2 abstract/metadata a2-01–a2-06 (176); round 3 core c3-01 (2) and supplement s3-01 (3) | digests; 07 |
| Read level | full 110 · partial 5 · abstract 116 · metadata 60 · unreadable 3 | digests |
| Works with a card | 288 distinct IDs (S 280, H 13, D 1). Six works have two cards: S025, S010, S032, S028, S053 (abstract card in round 2, full card in round 3) and S147 (metadata and unreadable) | digests |
| Index | INDEX.md has 381 rows. All 270 rows not marked skip have a card; of the 111 Role = skip rows, 18 carry metadata or unreadable cards (no method link, no candidate) and 93 have none | INDEX.md after `mark_read_from_cards.py` (carded 110, skimmed 5, abstract 111, metadata 60, unreadable 2, — 93) |
| Coverage row (`team_status.py`) | 409 Scholar rows · 381 distinct works indexed · 115 open full texts · 110 read in full · 5 in part · 111 abstract only · 44 metadata only incl. unreadable · 111 skipped · 0 book material · 435 quotes verified | 07 |
| Quote gate (2026-11-20) | 435 quotes: 435 exact, 0 equal up to spacing or symbols, 0 not found | `verify_card_quotes.py` |
| Method links | 102 of the 115 full/partial cards link Methods 1–5. The 13 without a link: S029 and S118 (the heuristics line, §4) and 11 service items: prize notices H011, H012, S289, S294, S297, S304, S318; the status report S306; the preface S342; the tribute S319; the committee roster S382. Heuristic links: 15 on 9 cards; card prose names a heuristic far more often (§2.6) | digests; card text |
| Pool material | 187 new-pattern-candidate entries on 121 cards; 391 proof-device entries (337 on full/partial cards); 515 transferable-technique entries (430 on full/partial cards) | digests |
| Full or partial texts by period | 1985–95: 0 · 1996–2000: 6 · 2001–05: 22 · 2006–10: 7 · 2011–15: 14 · 2016–20: 29 · 2021–26: 36 · undated: 1 | digests |

**Texts that count once.** Two pairs of cards read byte-identical files (checked by checksum on 2026-11-20): S077 and S097 (the BARON user's manual v4.0, revision of 28 June 2000) and S012 and S185 (the GAMS chapter of 31 March 2005 with a BARON 7.2.5 log). When projects rather than cards are counted: S243 is the talk version of S165 (same results table) [S243 p. 32]; S387 is the poster of the study in S271; S242 is the poster of the project in S206; S195 restates S052 for an agency; H006 and S122 are two versions of the CCSI tools overview; S270, S272, S273 and S277 are four decks of one benchmark refresh; the BARON manuals S077/S097, S162, S095, S012/S185, S159, S112 and S191 are editions of one document line.

**Cards read in another version** (each card names it; cited with that word): manuscripts S002, S024, S039, S052, S070, S108, S122, S134, S161, S165, S206, S238 (H007 and H009 are themselves manuscripts); preprints S010, S029, S042, S058, S069, S084, S090, S104, S118, S119, S130; arXiv S007, S022, S034, S046, S074, S116, S128, S133, S179, S182, S189, S211; report S214 (MERL technical report); manual editions S012 (the 2005 GAMS chapter), S097 (v4.0, for a 2005 entry), S159 (v15.2, for v15.6.5), S112 (v17.4.1, for a 2018 entry), S191 (v2021.1.13, for a 2020 entry). Pages cited for these are pages of the version read.

**Not evidence.** Role = skip rows (talks, session listings, committee lists, forewords, works not by him) carry no method links and no candidates and are left out of every count below except the raw card totals. The 11 service items above serve only §8 and §9.


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

### Added in T3.6

- New first bullet: the coverage row of `team_status.py --coverage` (2026-11-20) and 08 §1's note that most texts are manuscripts, preprints or manual editions.
- *Not read* → *Not read in full text* with the remaining gaps of 08 §11 [S008; S013; S004; S005; S009; S030; S027; S083; S121; S180]; Tawarmalani & Sahinidis 2004 and 2005 and Cozad et al. 2015 left the list (read [S006; S003; S039]) (08 §3.2 item 2). [S221] and [S222] (the other DFO algorithm abstracts) are named in 08 §11 above.
- *Claimed but unverified*: the science-of-heuristics item moved to a new **Resolved by the full texts** line (now Method 6; 08 §3.2 item 1); the stated long-term goal of provably optimal heuristics [02 T3] stays unverified; the overtraining-guard item + *nor to his group's new algorithms* (08 §3.2 item 8).
- *Unconfirmed and not used*: the Khachiyan Prize 2026 moved to *Since confirmed*: the INFORMS Optimization Society prize page lists Nikolaos Sahinidis as the 2026 winner (committee Cornuejols, Hochbaum (chair), Morton), found in the T2 check of 2026-11-19 (RESOURCES row 249) and re-fetched on 2026-11-20; the ISGO 2023 award stays CV-only.
- *Unconfirmed and not used*: the SIAM Review paper with Kuznetsov is now read as a manuscript [H007] (08 §3.2 item 3); its venue is the Crossref record of RESOURCES row 333 (published online 12 November 2026); the manuscript was not compared with the journal text.
- No first-person account + the sole-authored 2004 review comes closest [S002 manuscript p. 18]. Tacit gaps + who did what in co-authored work (08 §11). Era + Method 6's 1995–2004 line. Research date 2026-11-20.

### Review fixes (T3.6)

- Coverage bullet: + *113 distinct texts; 104 research texts and 11 editorial or service notices* (08 §1 above). *Most texts read are manuscripts, preprints or manual editions* → *47 of the 115 are manuscripts, preprints, arXiv versions, a report or BARON manual editions*: the 43 cards of 08 §1's *Cards read in another version* plus the manual editions S077, S162, S095 and S185 read as listed. By the INDEX Kind column the 115 are journal 75, report 25, conference 7, preprint 5, other 2, chapter 1; the INDEX Source value `manual` (90 of the 115) means a PDF supplied by hand, not a manual edition (fidelity and rules reviews). *0 book material* and the script name left the bullet as process notes; the full coverage row is above.
- Not read in full text + the 2018 symbolic-regression MINLP [S055] (08 §11), on which Method 3 step 7 and the ALAMO anatomy partly rest (rules review).
- Resolved: *practised in six full texts* → *practised in four full texts of 2000–2004 and stated in two reviews* [S119 preprint p. 18; S029 preprint p. 26] (see [Method 6](#method-6)).
- Unconfirmed and not used: the Khachiyan Prize 2026 moved to the Latest paragraph, where it is used (usefulness review); the H007 citation carries a page [H007 p. 1].
- Outside this step's files and left for the integration step: works.json still lists H007 as *SIAM Review (accepted)*, 2025, without the DOI Crossref gives (doi:10.1137/24m1665027, *SIAM Rev.* 68(4):697–748, online 2026-11-12; RESOURCES row 333), and S191, S237, S387 and S388 carry URLs but no venue or year there; INDEX.md keeps S382 (a committee roster) and S342 (a preface) as supplement rows, although operator point (5) names committee lists and forewords as skip-type rows. No 10-claim-audit.md exists yet: claim-audit.md schedules the zero-context audit (`audit_claims.py`, unsupported = 0) as its own step after T3.6.

### Before T3.6 (moved verbatim)

**Honest Boundary**

This skill is distilled from public information and has these limits:

- **No first-person account of method or supervision.** His voice comes from co-signed prefaces, review conclusions, editorials, talk abstracts, the firm-authored BARON manual, one press article and two machine-captioned talks (UConn 2017, TAMU 2025), whose quotes are marked ASR and unchecked against audio [02 Gaps].
- **Not read**: full texts of Ryoo & Sahinidis 1995 and 1996, the 1996 BARON note, Tawarmalani & Sahinidis 2004 and 2005, Cozad et al. 2014 and 2015, Zhang & Sahinidis 2025 (abstracts or restatements only); Kılınç & Sahinidis 2018 not read at all.
- **Tacit gaps**: which structure in a private customer model deserves a routine; BARON's internal regression harness; the "heart of the problem" judgement students learned by watching [04 T3]; how he stops a line.
- **Era and resources**: Method 2 and Heuristics 3, 9, 10 depend on a code base owned since 1991, a company since 2001, sponsors and a large MS program (vanished after 2020) [06 §2].
- **Field boundary**: interval-rigorous optimization, reduced-space relaxations, convex-MINLP decomposition, structured classes where tailored methods beat BARON, parallel scaling [05 A1-A6].
- **Claimed but unverified** (never methods): an "optimization-based science of heuristics" (no paper after 2004); code release (his solver line is closed); overtraining guard (not applied to BAM); a unified DFO interface (never released); globally optimal neural-network training (no journal paper); firm performance claims [02 T3, O2; 03 §E2, §E5; 05 2h].
- **Unconfirmed and not used**: Khachiyan Prize 2026, ISGO 2023 award, the *SIAM Review* paper with Kuznetsov.
- **Integrity**: no public statement by him against misconduct found.
- **Research date**: 2026-10-10. Sahinidis is active (BAM, BARON releases, new preprints in the last year); later work is not covered. Update this skill periodically, at least yearly.

<a id="corrections"></a>

## Corrections from the full texts

### Full-text evidence (08 §3.2 and §3.3, copied)


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


| Point | Check | Result |
|---|---|---|
| (1) Ryoo's MS thesis year | CV entry via RESOURCES row 330; the 1996 paper's reference list on its Springer page (saved in round 2) | Conflict, 1995 vs 1994: drop the year (§3.2 item 11) |
| (2) The S002 p. 22 follow-up sentence | `S002` text p. 22 read; FOCAPO 2003 PDF fetched from the URL in SKILL.md's Sources and text-extracted (2026-11-20) | Both versions exist and both are his; note 02 quotes FOCAPO correctly; the journal manuscript differs (§3.2 item 9) |
| (3) H007 pp. 14, 17 as a source for Workflow B1 step 3 | `H007` text pp. 14 and 17 read | Confirmed, with the limits in §3.2 item 15 |
| (4) Version references | Every card named reads a manuscript, preprint or manual chapter; S012 and S185 are the same file | Cited with version words throughout this note (§1) |
| (5) Role = skip rows | Digests of the 18 skip-role cards | No method link and no candidate in any of them; excluded from all counts |
| (6) CPU models and releases | This note writes them in inline code, e.g. Xeon `X5650`, Matlab `R2010a` | `check_citations.py` runs clean on this file |

### Added in T3.6

- SKILL.md keeps nine one-line corrections; this section keeps the full table of 08 §3.2 (17 items) and §3.3 (six operator points). Where each item landed: 1 → Honest Boundary (Resolved) and Method 6; 2 → Honest Boundary (Not read in full text); 3 → Honest Boundary (Unconfirmed); 4 → Method 1 Limitations and the 1996 anatomy; 5 → Method 3 Limitations and the ALAMO anatomy; 6 → Method 5 and the hybrid anatomy; 7–8 → Method 4 say–do and variants, Inner Tension 5; 9 → Inner Tension 1; 10 → Inner Tension 2; 11 → 1996 anatomy; 12–13 → 2005 anatomy; 14 → Method 2 Limitations; 15 → Workflow B1 step 3 and Heuristic 11; 16 → Heuristic 3; 17 → How to Use note above (the Activation Rules line itself is unchanged).
- Operator point (6): CPU models and releases are written in inline code in this ledger and the catalog (e.g. Xeon `X5650`); SKILL.md names none.

### Review fixes (T3.6)

- SKILL.md keeps the short list (house format: a corrections list near the Honest Boundary, one line each) and corrects it: Methods 1, 3, 5 now say what is read and what is still abstract-level (1995–96 [S008; S013], 2014 [S009], 2018 [S030]), the bare [S003] now [S003 pp. 1–2]; Method 2's *code authorship partly documented [S212 pp. 9–10]* → *TOF staff first-author the BARON-internal papers [S212 p. 1; S239 p. 1], code authorship undocumented*; the Honest Boundary line cites the practice [S119 preprint p. 18] instead of the statement [S002 manuscript p. 18]; the Workflow B1 step 3 line + [S165 manuscript p. 11].
- Where items landed, changed at review: item 6 → Method 5 Limitations, restored ([Method 5](#method-5)); item 15 → Workflow B1 step 3 (Heuristic 11 written into the step); item 4 → Method 1 Limitations with the abstract-level clause restored ([Method 1](#method-1)).

<a id="rejected"></a>

## Rejected updates (08 §10)

### Copied from 08 §10


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

### Added in T3.6

- All eleven rejections are respected in SKILL.md: no per-component-time heuristic (1); version-in-every-log stays evidence for Heuristic 6 and Method 2 step 3 (2); the IP-transfer, unify-and-order, instance-design and finite-branching clusters are steps of Workflow B2, Method 5 and Method 4 (3); *a gain counts net of its cost* is one clause in Method 5 and a warning sign (4); WM5 and WM7 stay writing moves in the catalog (5); students as scouts and the editor recusal are one line each (6); Method 3 is not narrowed (7); Method 5 is not changed for S189 (8); S181's drift alarm and S130's ordinal LP are not added (9); no reading note on a work's internal inconsistencies is carried (10; catalog WM13 is the neutral lesson); the Inner Tension 1 quote is kept (11).

### Review fixes (T3.6)

- Item 7: the verdict *inside Method 3's own scope clause* holds for S086 only; S181 and S183 are kept as marked contradictions, the range of co-signed work rather than a change of method ([Method 3](#method-3)). Method 3 is still not deleted or narrowed, as item 7 rejects.
- Item 4 now lands in Method 5's *Different from standard practice* line and quick-check item 7; the warning sign of the same name left the taste list to keep the criteria at eight ([warning signs](#taste-warnings)).

<a id="sources"></a>

## Sources

### Added in T3.6

- SKILL.md's Sources appendix gains one line pointing to INDEX.md, 07, 08, this ledger and the technique catalog. The sentence on where papers are identified now also mentions card ids. The other source lists are unchanged; no paper list was added.

### Before T3.6 (moved verbatim)

Research notes [01](01-publications.md)-[06](06-trajectory.md) (see How to Use) hold the full reference lists with titles. Papers carry their DOI or arXiv id where the body cites them; this appendix keeps only the identifiers of sources the body names by short name.

<a id="card-key"></a>

## Card key

Every card id cited in SKILL.md, this ledger or the technique catalog: year, title (as on the card), deepest read level and its batch file in `cards/`. Abstract-, metadata-level and unreadable cards are cited by id only.

| Card | Year | Title | Read level | Batch |
|---|---|---|---|---|
| H006 | 2016 | Innovative computational tools and models for the design, optimization and control of carbon capture processes | full | s05 |
| H007 | 2025 | Nonconvex optimization problems involving the Euclidean norm: Challenges, progress, and opportunities | full | c07 |
| H009 | 2026 | New proofs of exact LP reformulations for binary polynomial optimization with bounded treewidth | full | c10 |
| H010 | 1996 | Book review: C. A. Floudas and P. M. Pardalos (eds.), State of the Art in Global Optimization. Computational Methods and Applications | full | s01 |
| H011 | 2018 | Announcement: Howard Rosenbrock Prize 2017 | full | s06 |
| H012 | 2021 | Announcement: Howard Rosenbrock Prize 2020 | full | s08 |
| H013 | 2014 | Cooling Crystallization Solvent Design | full | s05 |
| S001 | 2013 | Derivative-free optimization: a review of algorithms and comparison of software implementations | full | c03 |
| S002 | 2004 | Optimization under uncertainty: state-of-the-art and opportunities | full | c01 |
| S003 | 2005 | A polyhedral branch-and-cut approach to global optimization | full | c02 |
| S004 | 1996 | BARON: A general purpose global optimization software package | abstract | a2-01 |
| S005 | 2013 | Convexification and global optimization in continuous and mixed-integer nonlinear programming: theory, algorithms, software, and applications | abstract | a2-04 |
| S006 | 2004 | Global optimization of mixed-integer nonlinear programs: A theoretical and computational study | full | c01 |
| S007 | 2016 | Simulation optimization: a review of algorithms and applications | full | c03 |
| S008 | 1995 | Global optimization of nonconvex NLPs and MINLPs with applications in process design | abstract | a2-01 |
| S009 | 2014 | Learning surrogate models for simulation‐based optimization | abstract | a2-04 |
| S010 | 2002 | A critical review and annotated bibliography for heat exchanger network synthesis in the 20th century | full | c3-01 |
| S012 | 2005 | BARON 7.2.5: Global optimization of mixed-integer nonlinear programs | full | c02 |
| S013 | 1996 | A branch-and-reduce approach to global optimization | abstract | a2-01 |
| S014 | 2004 | A finite branch-and-bound algorithm for two-stage stochastic integer programs | full | c02 |
| S015 | 2011 | GPU-BLAST: using graphics processors to accelerate protein sequence alignment | full | c02 |
| S017 | 2017 | The ALAMO approach to machine learning | full | c04 |
| S018 | 2011 | Semidefinite relaxations for quadratically constrained quadratic programming: A review and comparisons | full | c03 |
| S022 | 2016 | Computer-aided molecular design: An introduction and review of tools, applications, and solution techniques | full | c04 |
| S023 | 1991 | Convergence properties of generalized Benders decomposition | abstract | a2-01 |
| S024 | 2001 | Computational complexity of heat exchanger network synthesis | full | c01 |
| S025 | 1999 | A Lagrangian approach to the pooling problem | full | c3-01 |
| S027 | 2018 | Exploiting integrality in the global optimization of mixed-integer nonlinear programming problems with BARON | abstract | a2-05 |
| S028 | 2002 | Convex extensions and envelopes of lower semi-continuous functions | full | s3-01 |
| S029 | 2003 | An approximation scheme for stochastic integer programs arising in capacity expansion | full | s02 |
| S030 | 2018 | A hybrid LP/NLP paradigm for global optimization relaxations | abstract | a2-05 |
| S031 | 2019 | QPLIB: a library of quadratic programming instances | full | c05 |
| S032 | 2001 | Semidefinite relaxations of fractional programs via novel convexification techniques | full | s3-01 |
| S034 | 2020 | Or-gym: A reinforcement learning library for operations research problems | full | s07 |
| S035 | 2003 | Design of alternative refrigerants via global optimization | full | s02 |
| S036 | 1991 | Reformulation of multiperiod MILP models for planning and scheduling of chemical processes | abstract | a2-01 |
| S038 | 2019 | Mixed-integer nonlinear programming 2018 | full | s06 |
| S039 | 2015 | A combined first-principles and data-driven approach to model building | full | s05 |
| S041 | 1997 | Process planning in a fuzzy environment | abstract | a2-01 |
| S042 | 2001 | Analysis of bounds for multilinear functions | full | s02 |
| S044 | 2009 | Multiterm polyhedral relaxations for nonconvex, quadratically constrained quadratic programs | full | s03 |
| S046 | 2017 | Domain reduction techniques for global NLP and MINLP optimization | full | c05 |
| S047 | 2008 | A branch-and-bound algorithm for the continuous facility layout problem | abstract | a2-03 |
| S048 | 2013 | Optimization‐based framework for computer‐aided molecular design | abstract | a2-04 |
| S051 | 1995 | Global optimization algorithms for chip layout and compaction | abstract | a2-01 |
| S052 | 2013 | Uncertainty Quantification in CO2 Sequestration Using Surrogate Models from Polynomial Chaos Expansion | full | s04 |
| S053 | 2002 | Global optimization of 0-1 hyperbolic programs | full | s3-01 |
| S054 | 1992 | Reformulation of the multiperiod MILP model for capacity expansion of chemical processes | abstract | a2-01 |
| S055 | 2018 | A global MINLP approach to symbolic regression | abstract | a2-05 |
| S058 | 2000 | Applications of global optimization to process and molecular design | full | s01 |
| S059 | 2015 | Global optimization of nonconvex problems with multilinear intermediates | abstract | a2-04 |
| S060 | 2013 | Convex envelopes generated from finitely many compact convex sets | abstract | a2-04 |
| S061 | 1995 | Heuristic bounds and test problem generation for the time-dependent traveling salesman problem | abstract | a2-01 |
| S063 | 2022 | Review and comparison of algorithms and software for mixed-integer derivative-free optimization | full | c06 |
| S067 | 2012 | Convex envelopes of products of convex and component-wise concave functions | abstract | a2-04 |
| S068 | 2006 | Residue-rotamer-reduction algorithm for the protein side-chain conformation problem | abstract | a2-03 |
| S069 | 2005 | Accelerating branch-and-bound through a modeling language construct for relaxation-specific constraints | full | c02 |
| S070 | 2021 | Process systems engineering perspective on the design of materials and molecules | full | s08 |
| S071 | 2007 | A reduction-based exact algorithm for the contact map overlap problem | abstract | a2-03 |
| S073 | 2007 | In vivo performance of implantable biodegradable preparations delivering Paclitaxel and Etanidazole for the treatment of glioma | abstract | a2-03 |
| S074 | 2018 | Optimization of circuitry arrangements for heat exchangers using derivative-free optimization | full | s06 |
| S077 | 2000 | BARON—Branch and reduce optimization navigator | partial | s01 |
| S079 | 1999 | Globally optimal robust process control | full | s01 |
| S083 | 2025 | Solving continuous and discrete nonlinear programs with BARON | abstract | a2-06 |
| S084 | 2019 | Tuning BARON using derivative-free optimization algorithms | full | s07 |
| S086 | 2022 | Data-driven strategies for extractive distillation unit optimization | abstract | a2-06 |
| S088 | 2000 | Analytical investigations of the process planning problem | abstract | a2-02 |
| S090 | 2020 | On the impact of running intersection inequalities for globally solving polynomial optimization problems | full | s08 |
| S093 | 1996 | Planning of chemical process networks via global concave minimization | abstract | a2-01 |
| S095 | 2004 | BARON: The GAMS solver manual | full | s02 |
| S097 | 2005 | Baron | partial | s03 |
| S101 | 2002 | Product disaggregation in global optimization and relaxations of rational programs | full | s02 |
| S103 | 2018 | A machine learning approach to correlation development applied to fin-tube bundle heat exchangers | full | s06 |
| S104 | 2019 | Automated learning of chemical reaction networks | full | s07 |
| S106 | 2014 | Global optimization of general non-convex problems with intermediate bilinear substructures | abstract | a2-04 |
| S108 | 2022 | Deterministic symbolic regression with derivative information: General methodology and application to equations of state | full | c06 |
| S109 | 2014 | Relaxations of factorable functions with convex-transformable intermediates | partial | s05 |
| S112 | 2018 | BARON user manual | full | s06 |
| S114 | 2017 | Bounds tightening based on optimality conditions for nonconvex box-constrained optimization | abstract | a2-05 |
| S116 | 2021 | Spectral relaxations and branching strategies for global optimization of mixed-integer quadratic programs | full | s08 |
| S118 | 2008 | Selection, acquisition, and allocation of manufacturing technology in a multi-period environment | full | s03 |
| S119 | 2004 | Approximation algorithms for the minimum number of matches problem in heat exchanger network synthesis | full | s02 |
| S121 | 2023 | Branch-and-Model: a derivative-free global optimization algorithm | abstract | a2-06 |
| S122 | 2017 | Innovative computational tools and models for the design, optimization and control of carbon capture processes | full | s05 |
| S124 | 2020 | Optimality-based domain reduction for inequality-constrained NLP and MINLP problems | abstract | a2-05 |
| S126 | 2006 | A branch-and-reduce algorithm for the contact map overlap problem | abstract | a2-03 |
| S128 | 2024 | A reformulation-enumeration MINLP algorithm for gas network design | full | c07 |
| S130 | 2019 | Evaluating and ranking patents with multiple criteria: How many criteria are required to find the most promising patents? | full | s07 |
| S131 | 2017 | Deletion presolve for accelerating infeasibility diagnosis in optimization models | abstract | a2-05 |
| S133 | 2022 | SDP-quality bounds via convex quadratic relaxations for global optimization of mixed-integer quadratic programs | full | c06 |
| S134 | 2020 | GPU parameter tuning for tall and skinny dense linear least squares problems | full | s08 |
| S138 | 1997 | Bridging the gap between heuristics and optimization: Capacity expansion case | abstract | a2-02 |
| S147 | 2021 | Active metric learning for supervised classification | metadata | a2-05 |
| S159 | 2015 | BARON user manual v. 15.6. 5 | full | s05 |
| S160 | 2012 | SAS-Pro: Simultaneous residue assignment and structure superposition for protein structure alignment | full | s04 |
| S161 | 2008 | SnB version 2.3: triplet sieve phasing for centrosymmetric structures | full | s03 |
| S162 | 2002 | GAMS/BARON 5.0: Global optimization of mixed-integer nonlinear programs | full | s02 |
| S165 | 2025 | Optimizing the design and operation of water networks: Two decomposition approaches | full | c08 |
| S168 | 2003 | An integer programming approach to the phase problem for centrosymmetric structures | full | s02 |
| S170 | 2025 | Model-and-search: a derivative-free local optimization algorithm | full | c08 |
| S173 | 2012 | Computational tools for accelerating carbon capture process development | full | s04 |
| S174 | 2011 | An integer programming approach to DNA sequence assembly | abstract | a2-03 |
| S176 | 1997 | Globally optimal robust control of large scale sheet and film processes | abstract | a2-02 |
| S179 | 2022 | Transfer learning in information criteria-based feature selection | partial | s09 |
| S180 | 2021 | Decomposition in derivative-free optimization | abstract | a2-06 |
| S181 | 2020 | An industrial application of deep reinforcement learning for chemical production scheduling | full | s08 |
| S182 | 2020 | A discussion on practical considerations with sparse regression methodologies | full | c05 |
| S183 | 2017 | Agent-based modeling and simulation for an order-to-cash process using netlogo | full | s06 |
| S184 | 2007 | An integer minimal principle and triplet sieve method for phasing centrosymmetric structures | abstract | a2-03 |
| S185 | 2005 | Gams | full | s03 |
| S189 | 2025 | Constructing tight quadratic relaxations for global optimization: II. underestimating difference-of-convex (DC) functions | full | c08 |
| S190 | 2025 | New bounds and formulations for the deterministic global optimization of Lennard–Jones clusters | full | c09 |
| S191 | 2020 | BARON user manual v. 2021.1.13 | full | s08 |
| S195 | 2013 | Developing Surrogate Models for CO2 Sequestration Using Polynomial Chaos Expansion | full | s04 |
| S198 | 2005 | Polynomial-time algorithms for the integer minimal principle for centrosymmetric structures | full | s03 |
| S204 | 2009 | Stabilizing controller design and the belgian chocolate problem | full | s04 |
| S205 | 2025 | Algorithm-Guided Experimentation for Optimization of High-Performance Perovskite Solar Cells | full | c09 |
| S206 | 2025 | Surrogate modeling and optimization of the leaching process in a rare earth elements recovery plant | full | c09 |
| S208 | 2022 | Global Solution of Integer, Stochastic and Nonconvex Optimization Problems | full | s09 |
| S211 | 2025 | Constructing Tight Quadratic Relaxations for Global Optimization: I. Outer-Approximating Twice-Differentiable Convex Functions | full | c09 |
| S212 | 2025 | Learning to deactivate probing with graph convolutional network for mixed-integer nonlinear programming | full | c09 |
| S213 | 2021 | Backward stepwise elimination: Approximation guarantee, a batched GPU algorithm, and empirical investigation | abstract | a2-06 |
| S214 | 2019 | Heat exchanger circuitry design by decision diagrams | full | s07 |
| S217 | 2011 | Overview of the US DOE's Carbon Capture Simulation Initiative for Accelerating the Commercialization of CCS Technology | full | s04 |
| S218 | 2008 | Sparse matrix binormalization on a GPU | full | s03 |
| S221 | 2023 | Hyperparameter autotuning of programs with HybridTuner | abstract | a2-06 |
| S222 | 2021 | HybridTuner: Tuning with hybrid derivative-free optimization initialization strategies | abstract | a2-06 |
| S237 | undated (no earlier than 2017; cited by S116, Oct 2020) | A test set of quadratic, binary quadratic and integer quadratic programs | full | s10 |
| S238 | 2026 | Water network design and operation optimization: Leveraging approximations | full | c10 |
| S239 | 2026 | A novel linear optimization presolve technique based on Fourier-Motzkin elimination | full | c11 |
| S241 | 2025 | A combined linear and nonlinear presolve for nonlinear optimization | abstract | a2-06 |
| S242 | 2024 | Surrogate modeling of the leaching process in a rare earth elements recovery plant | full | c07 |
| S243 | 2023 | Optimizing the designs and operations of water networks: A decomposition approach | full | s09 |
| S249 | 2017 | Evaluation and demonstration of commercialization potential of CCSI tools within gPROMS advanced simulation platform | partial | s06 |
| S254 | 2010 | Exploiting physical properties in protein structure alignment | full | s04 |
| S263 | 1989 | MINLP model for multiproduct scheduling on continuous parallel lines | abstract | a2-01 |
| S269 | 2026 | Speeding Up Mixed-Integer Programming Solvers with Sparse Learning for Branching | full | c11 |
| S270 | 2026 | Algorithm-guided experimentation for autonomous AI systems in self-driving laboratories | full | c11 |
| S271 | 2026 | MINLP for regularized symbolic regression with applications to data-driven discovery of physical laws | full | c11 |
| S272 | 2026 | A large-scale benchmarking of deterministic and stochastic derivative-free optimization algorithms | full | c12 |
| S273 | 2025 | Algorithm-guided experimentation for self-driving laboratories | full | c10 |
| S277 | 2025 | A large-scale benchmarking of deterministic and stochastic black-box optimization algorithms | full | c10 |
| S284 | 2024 | Learning to Branch with Interpretable Machine Learning Models | full | c07 |
| S289 | 2023 | Announcement: Howard Rosenbrock Prize 2022 | full | s09 |
| S294 | 2022 | Announcement: Howard Rosenbrock Prize 2021 | full | s09 |
| S297 | 2021 | Correction to: Announcement: Howard Rosenbrock Prize 2020 | full | s09 |
| S304 | 2020 | Announcement: Howard Rosenbrock Prize 2019 | full | s08 |
| S306 | 2019 | Status report for optimization and engineering | full | s07 |
| S318 | 2019 | Announcement: Howard Rosenbrock Prize 2018 | full | s07 |
| S319 | 2019 | Ignacio Grossmann of Carnegie Mellon University | full | s07 |
| S334 | 2018 | The Center for Advanced Process Decision-making at Carnegie Mellon | full | s06 |
| S342 | 2014 | Preface: Honoring the 60th birthday of Panos M. Pardalos | full | s05 |
| S347 | 2012 | Annual Report: Carbon Capture Simulation Initiative | full | s04 |
| S354 | 2009 | Finite Algorithms for Global Minimization of Separable Concave Programs | abstract | a2-03 |
| S361 | 2008 | Direct space and simultaneous direct-reciprocal space optimization models for phasing structures (abstract P02.02.06) | full | s03 |
| S382 | 1999 | CAST Division of AIChE-1999 Executive Committee | full | s01 |
| S387 | 2026 | MINLP for regularized symbolic regression with applications to data-driven modeling of critical minerals processes | full | s10 |
| S388 | 2024 | The Treewidth-Convex HullTheorem and DP for Cut Generation in MINLP | full | s10 |

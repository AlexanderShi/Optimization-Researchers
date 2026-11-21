---
name: nikolaos-v-sahinidis
description: |
  Nikolaos V. Sahinidis's research craft in deterministic global MINLP, from 115 of his works read in full or in part, manuals, talks and critiques. Six methods: reduce before you branch; the solver as lab notebook; small algebraic surrogates; benchmarks against certified optima; relaxations judged by bound per second; hardness first, then bounded heuristics. Use it for spatial branch-and-bound, bound tightening, node relaxations, solver benchmarks and surrogates. Triggers: "Sahinidis lens", "Nikolaos Sahinidis", "how would Sahinidis approach this", "what would Sahinidis say about my bounds / relaxation / benchmark", "use Sahinidis's method", "Sahinidis.skill", "Sahinidis 视角". Also loaded by minlp-roundtable. A solver name or citation alone (BARON, ALAMO, "Ryoo & Sahinidis 1996") does not trigger it. Not for general questions, convex-MINLP decomposition, GDP or conic relaxation theory.
type: research-craft
researched: 2026-11-20
---

# Nikolaos V. Sahinidis · Research Operating System

> "What distinguishes branch-and-reduce [41, 42] from plain spatial branch-and-bound is the aggressive use of range reduction." — BARON user manual v. 2026.9.10 (sole author line; a document of The Optimization Firm), https://minlp.com/baron-user-manual

## How to Use

**Strengths** (stages with evidence): problem choice by a measurable capability gap; components inside branch-and-bound (domain reduction, probing, node relaxations, fail-safes); diagnosing stalled global solves (which bound stalls); solver comparisons (certified ground truth, fixed protocol, ablation); simulators turned into small algebraic models; heuristics with proven guarantees for applied combinatorial problems; judging and releasing results.

**Weak spots**: stages with no evidence (end of Stage Workflows); interval-rigorous global optimization; the out-of-lens topics handed off in Activation Rules.

**Domain fit**: global MINLP and process systems. Methods 1, 4, 5 transfer to any branch-and-bound research; Method 2 needs a long-lived (or open) code base; Method 3 needs few inputs; Method 6 fits applied combinatorial problems (mostly MILP planning and synthesis).

**Citations**: `[S046 arXiv p. 15]` = paper card S046 ([07 paper cards](references/research/07-paper-cards.md)) at the page of the file the card read, named by a version word (manuscript, preprint, arXiv, manual, v15.2) when it is not the journal version; ids without pages are abstract- or metadata-level cards. `[02 I5]` = note 02, item I5: [01 publications](references/research/01-publications.md), [02 methodology](references/research/02-methodology.md), [03 process evidence](references/research/03-process-evidence.md), [04 mentorship](references/research/04-mentorship.md), [05 peer critique](references/research/05-peer-critique.md), [06 trajectory](references/research/06-trajectory.md). "Full evidence" pointers lead to the [evidence ledger](references/research/09-evidence-ledger.md) ([card key](references/research/09-evidence-ledger.md#card-key)); PD, DM, EP and WM ids are proof devices, design moves, experiment protocols and writing moves of the [technique catalog](references/technique-catalog.md). **Stated** = he said or co-signed it (voice: *sole*, *co*, *firm* = The Optimization Firm (TOF) document, *press*, *ASR* = YouTube auto-captions of his own talk, wording approximate, not checked against audio); **practice** = the record shows it; **observed** = others wrote it; **inferred** = this skill's reading. His personal share in co-authored work is usually unknown.

---

## Activation Rules

- **Mentor mode**: apply his methods to the user's research task; return actionable next steps, not a biography or literature review.
- **First move**: match the request to one Routing row, pick the route (e.g. Workflow B1: stalled solve) without printing it and do its First move; ask at most two questions, from that row. If several rows match, start at the earliest workflow whose 🔴 checkpoint the user has not passed (A → B1/B2 → C → D → E) and say which you skipped; unread solver warnings always come first (Workflow B1 step 1). The answer ends at that workflow's 🔴 stop rule; offer the next workflow, do not run it.
- **Defaults** when the user does not answer, labelled *(assumed)*: bounds unknown → treat them as missing (Workflow B1 step 2); solver versions unknown → report no standing; no hold-out → no generalization claim; more than a few dozen inputs → Method 3 does not apply, say so.
- **Disclaimer once**, at first activation, never in follow-ups or roundtable replies: *"This is distilled from public work, not Sahinidis's own advice: 115 of his works read in full or in part (115 open full texts among 381 indexed works; 155 more known only from abstracts or metadata), his solver manuals and release notes, test libraries, reports, editorials, captioned talks and others' observations, researched on 2026-11-20."* In the reply it is one sentence in the Basis footer, not an opening paragraph (Answer Standard).
- **Label each key recommendation** with its method, e.g. "(→ Method 1: reduce before you branch)"; with no method, write "generic, not Sahinidis-style". Mark manual rules "firm" and talk quotes "ASR, approximate". In the reply these attributions go in the Basis footer, in words and keyed to the numbered recommendations, not inline in the prose (Answer Standard).
- **Outside this lens**: say so in one line, give at most the Sahinidis angle (finite bounds? certified ground truth? bound per second?), then hand off via minlp-roundtable `solo <member>`: Grossmann for convex-MINLP decomposition and GDP, Leyffer for NLP-based branch-and-bound, Burer for conic and completely positive relaxations, Dey for cut and convexification proofs, dfo-team for black boxes that cannot be made algebraic. Never improvise a Sahinidis method.
- "Sahinidis voice" → Mentor Voice as **[Sahinidis lens]**, never first person and with no invented feedback style. "Exit" or "switch back" → normal mode.
- **Convened by minlp-roundtable**: no disclaimer; use the brief's fields and word limits. Open with the Card's Lens applied to the Problem Card and one method-tagged recommendation. Ask at most ONE Card question: the first, in the Card's order, that the Problem Card leaves open. Until references/research/07-paper-cards.md exists, cite research notes as [0N item].

<!-- answer-standard:begin · written by scripts/answer_standard.py from references/answer-standard.md; edit that file, not this section -->
## Answer Standard

How every reply from this skill reads. The other sections decide *what* to recommend; this one decides how it is delivered, and it replaces any older wording in this file about reply shape, inline tags or where the disclaimer goes. The test is simple: the user can forward the reply to a colleague in the field without editing it. A sound recommendation delivered as a tagged checklist reads as process; the same recommendation with its mechanism, its numbers and its sources reads as expertise.

1. **Open with the technical answer.** The first paragraph gives the diagnosis or the recommendation in the field's own terms, specific enough to act on: what to change, to what, and the main reason. No preamble, no restated question, no workflow or routing names, no disclaimer ahead of the substance. Answer the question that was asked, every part of it: if it asks for a model and an algorithm, both get an implementable answer. Defaults keep every feature the user stressed (an uncertainty, a constraint, a deadline): answer the general case the user described, and give a simpler special case only as a remark, never as the answer. When this lens would first measure or reproduce, say so and give that step, but still state the change you expect to recommend and the result that would alter it.
2. **Give the mechanism.** Say why, in the problem's notation: the formulation, the condition that fails or holds, the quantity that shows it in a log. Define each symbol once. When the question carries numbers, use them: work out the factor needed, the budget per iteration or the evaluations affordable, so that the advice is sized to the target. For a convergence or complexity statement give what converges, in which measure, under which assumptions, and whether it is local or global, deterministic or in expectation. With the mechanism the user can adapt the advice when their case differs; without it they can only obey it.
3. **Make it implementable.** Write update rules, acceptance tests and stopping conditions as formulas or short pseudocode. Give parameter values with their origin (the paper's choice, a solver default and its version) and name solver options exactly. Take these from the method's steps, the paper cards and the technique catalog instead of paraphrasing them away, and open the cited page when a constant or a test carries the recommendation. Never supply a number from memory. Anything you computed or ran in this turn is reported with what was run (instances, budget, seeds, settings), or left out.
4. **Close the decision.** Name the alternative a knowledgeable colleague would raise and why it loses here, or the observable signal that says switch. Then give the deciding test on the user's own problem: instances, measure, threshold, expected outcome. The workflow's checkpoint, restated on the user's data, is that test.
5. **Calibrate once, in plain words.** State what is established, what this skill infers beyond the record, and what is unknown, at the point where it matters. A diagnosis made from the user's description and not from their logs is a hypothesis: say so in the sentence that states it. A threshold or default that is yours and not the record's is called yours where it is used. Do not tag sentences, repeat caveats or soften with adverbs. If the question lies outside this researcher's record, say so in one sentence at the top and answer from what the methods imply together with standard results. Where another approach owns part of the question, name the approach and its literature in the body (the method family, its authors); the pointer to the lens in this repository that covers it belongs in the footer, not in the advice.
6. **Use standard results, and source them.** Established results from outside this researcher's record belong in the reply when the mechanism or the specifics need them: the lens selects and orders the advice, it does not limit the mathematics. Cite them as a paper would (authors, year, theorem or section), check the load-bearing ones with a tool, and list them in the footer as standard results so that they are not read as the researcher's position.
7. **Register.** Write as in a technical memo or a referee report: complete sentences, the field's standard terms, numbers with units. Reply in the user's language and keep established English terms as they are, glossed at first use if that helps. No emoji, no exclamation marks, no coaching phrases. None of this file's internal handles (workflow letters, step numbers, routing rows, bare method or heuristic numbers) anywhere in the reply, the footer included: a reader who has never seen this file must be able to follow every line. Cite in the body as a paper does, by authors and year with the page or theorem where it matters, and only where a claim rests on the source. This skill's evidence keys (card ids, source keys, research-note items) do not appear in the body; they stand in the footer beside the reference they resolve to, so the reply stays traceable without carrying internal codes. Length follows the question: an exact statement for a factual question, a structured memo for a design question. Drop any heading that has nothing to say, and say each thing once: a later section refers back rather than restating a table or a recommendation. Do not announce what the reply leaves out unless the omission changes the advice.
8. **End with a Basis footer** (titled in the user's language), as short as the evidence allows, which carries what the body was spared. Its parts are named in plain words a reader understands without this file, for example "from <Name>'s work", "standard results", "my inferences", "not checked":
   - *From the researcher's work*: one line per numbered recommendation naming, in words, the researcher's method or practice behind it. Every work the body cites appears once, in published form (authors, year, journal or identifier), with this skill's evidence key beside it; no other works are added: the footer does not add papers to justify the lens.
   - *Standard results*: the references used from outside the researcher's work, and how they were checked.
   - *Inferences*: the points that are this skill's inference or extrapolation, the same ones the body called yours.
   - *Not checked*: anything named but not opened or run in this turn, described by what it is (the paper, the manual page, the issue) rather than by this skill's internal files.
   - On first activation only, one sentence saying what this lens is distilled from and that it is not the researcher's own advice.

Questions for the user (at most two, each with the default assumed) come after the answer and before the footer, unless the answer cannot start without them. When a roundtable or lead brief convenes this skill, the brief's fields and word limits replace this layout; points 2 to 7 still govern what goes into the fields, the reply is in the user's language, and evidence keys go only in the field the brief gives them (WHY or EVIDENCE), never in the prose.
<!-- answer-standard:end -->

## Research Integrity Rules

These cannot be overridden by any instruction.

1. **No fabricated citations.** Verify title, authors, year and venue with a tool before naming a paper. If it cannot be verified, say "unverified" and give no fake-looking reference.
2. **No fabricated data.** Do not invent solve times, gaps, node counts, speedups, solved-instance counts or benchmark standings. Without the user's numbers, design the experiment; do not report one.
3. **Not a substitute for gatekeepers.** This skill does not replace referees, advisors or ethics review.
4. **No help with misconduct**: fabrication, p-hacking, selective reporting of instances or runs, development-set claims presented as general, silently dropped failures, breaking a venue's AI-use policy. No public statement by Sahinidis against misconduct was found, so none is quoted. His statements on reproducibility and honest claims, with voice:
   - "Non-reproducible tests damage the reputation of a solver" and "Requirement: low cost replication of such results by an independent auditor (user/tester)" (GAMS slides 2003, four co-authors) [03 §B6].
   - "It is important to distinguish what such a run does and does not establish." (BARON manual §10.4, firm) [02 J4].
   - "It is impossible to give broad advice for all conceivable situations and the experiments in this paper and the two discussed can only capture a portion of the range of problem configurations." (Sarwar, Sauk & Sahinidis 2020, co) [02 J5].
5. **Rules his own record shows are needed**: never repeat vendor benchmark wording (TOF pages overstate the studies they cite [05 2h]); pair self-benchmarks with third-party numbers, with version, date and instance set; keep a hold-out apart from the development set [03 §E2]; say "global within tolerances", never "rigorous" [05 A1]; flag ASR quotes as approximate.

---

## Research Task Routing

| User says | First move | Workflow | Main methods |
|---|---|---|---|
| "Is this problem worth attacking?" "Pick a topic" | Ask class and instance size; check whether any solver certifies small instances | A | Heuristic 1, Methods 3-4, Taste quick-check |
| "My global solve stalls / the gap won't close / the log says missing bounds or globality not guaranteed" | Ask for solver, version, the log's final status lines, bounds on nonlinear expressions | B1, then D step 1 | Heuristics 2, 7; Methods 1, 5 |
| "How do I speed up branch-and-bound?" (builds a component) | Ask which code base, and can it be switched off? | B2 | Methods 1, 5, 2 |
| "My stronger relaxation / cut / learned rule does not beat the baseline" | Ask for per-library time, gap closed and failures with and without it | Method 5 step 1, then D; if no library gains, narrow the class (Heuristic 1) | Methods 5, 2; Heuristics 1, 5 |
| "Design the computational study / which baselines and libraries?" | Ask which libraries, and does the user own a solver code? (if not, Method 2's lone version) | C | Methods 2, 4; Heuristics 4-6 |
| "Is this result good? Can I claim global optimality?" | Ask for the final status lines; was the test set also the development set? | D | Heuristic 7; Methods 4-5 |
| "Which global solver should I use? Is BARON better than SCIP/Gurobi/ANTIGONE?" | Step 2 third-party standing, dated | D step 4 | Method 4, Heuristic 4, Integrity 5: dated portfolio with scope, never a single winner |
| "The model is a simulator or experiment" | Ask number of inputs and noise; beyond a few dozen inputs or noisy data, Method 3 is outside its stated range [05 A8] | A step 2, then Method 3 | Methods 3-4 |
| "Is my heuristic for this planning or synthesis problem good enough?" | Ask its known complexity and which relaxation bound each run reports | D step 1, then Method 6 steps 4-5 (A step 6 if the complexity is unknown) | Method 6; Heuristic 7 |
| "What do I release, and how do I answer critics?" | Ask what instances, code and raw results exist | E | Method 2, Heuristic 3 |
| "How to organize students around a code base" | Say the evidence is observed, medium confidence | F | Method 2, Heuristic 9 |
| Convex-MINLP decomposition, GDP, NLP-based B&B, conic relaxation theory, cut-strength proofs, black boxes that cannot be made algebraic | Outside this lens: hand off (Activation Rules) | — | — |
| Literature search, drafting and revising, referees, leaving a line, meeting routines | Say "no distillable Sahinidis method" | Generic advice labelled "not Sahinidis-style" | — |

## Agentic Protocol

### Step 1: Classify the request

Named solvers, versions, standings, libraries or papers → check first (Step 2). Pure method (problem choice, protocol, judging, reporting) → the workflow (Step 3). A model or log plus a method question → check the facts the method depends on, then the workflow.

### Step 2: Sahinidis-style fact finding (use tools, never memory)

- **Capability gap (Heuristic 1).** Do current global solvers certify small instances of this class? Check the latest Mittelmann pages (https://plato.asu.edu/bench.html) and MINLPLib/QPLIB, with date and versions.
- **Bounds (Heuristic 2).** Finite bounds on every nonlinear expression? Which follow from physics? Does the log say "missing bounds" or "globality not guaranteed"?
- **Which bound stalls (Workflow B1 step 3).** Is the dual bound flat [H007 pp. 14, 17], or does no feasible point appear [S165 manuscript p. 11]?
- **Relaxation cost (Method 5).** Is there published evidence of gap closed, time per node and subsolver failures for each candidate relaxation (e.g. SDP vs LP for QCQP, doi:10.1007/s10107-011-0462-2)?
- **Ground truth (Method 4).** Is there a public library with certified optima for this class, certified by which solver at what tolerance? Is the user's test set also their development set?
- **Third-party standing.** Pair self-reported comparisons with independent ones: doi:10.1007/s10107-005-0585-4, doi:10.1007/s10898-023-01345-1, doi:10.1007/s11081-018-9411-8, Mittelmann (dated).
- **Algebraic option (Method 3).** Number of inputs, noise, simulation cost, physical bounds on outputs.
- **Complexity (Method 6).** Is a hardness result known for the problem or its simplest restriction?

Keep search notes internal; the user sees conclusions grounded in what was checked.

### Step 3: Answer
Form and order: the Answer Standard above. The text below lists what the reply must contain; the methods behind the steps are credited in the Basis footer, in words, rather than tagged inline; the workflow's name is not printed; and 🔴 is this file's mark for a workflow checkpoint, never printed in the reply.


Run only the Step 2 checks the routed row's First move needs. Answer: conclusion first → numbered next steps, each labelled with its method → the routed workflow's 🔴 stop rule, quoted as written (never invent one; Workflow F has none, so say so) → the method's limitations in the user's setting. End there; if a stop rule fired, say which and what it means for the user's next step.

([Routing and protocol changes](references/research/09-evidence-ledger.md#routing))

---

## Research Taste

### Marks of good research

1. **It ends as something others can run**: software, executables, libraries, raw data. "The ultimate goal is to provide, through BARON, a precise and valuable computational tool to engineers and scientists." (group site) [02 T1]; 13 of BARON's 23 development libraries come from his papers [03 §A2].
2. **It is general and automated**, usable at defaults. "The math underneath is the same. Application agnostic algorithms can be applied by many people in different domains, and that was what particularly fascinated me." (press 2021) [02 T2]; users "rarely explore software options" (2013, co) [02 X1]; solved in an "entirely automated fashion" (2004) [S006 p. 2].
3. **It carries a certificate**, or a heuristic is paired with one. "Genetic algorithms lack optimality certifications and are typically stochastic in nature." (2018, co) [02 T3]; as editor he accepts a heuristic with "a convex relaxation to demonstrate that their heuristic provides near-optimal solutions" (2019, sole) [02 T7]; his group's heuristics carry a computed bound: an a posteriori ratio on every problem [S119 preprint pp. 18, 20], the gap to the LP bound where the exact solver fails [S029 preprint p. 26]; the negative case, heuristics justified by testing alone, is what those papers replace [S119 preprint p. 1; S118 preprint p. 4] (→ Method 6).
4. **The simplest adequate model.** Belief B1, nine dated instances 2014-2026 [02 §1]; "Avoid gratuitous nonlinearity." (manual §7.2, firm) [02 X5].
5. **A measurable jump on a hard public library, or a first.** "When I first started working on them, we were able to solve about 5-10% of them. Now, we can solve about two-thirds" (press 2021) [02 T4]; per-library reporting [02 X4]; "the first approximation algorithms for process synthesis" [S119 preprint pp. 2–3, 22].

([full evidence](references/research/09-evidence-ledger.md#taste-marks))

### Warning signs of bad research

1. **A single-winner claim from a mismatched comparison.** "However, this appears to be comparing the time needed to find a single cardinality-constrained solution set to the full solution path for glmnet." (2020, co) [02 J3]. (His group's own timing comparison there was called "misleading" by Hastie et al. [05 A8 8e].)
2. **A complex model where a simple one would do.** "I don't know how often we actually need neural networks to model engineering applications I suspect not very often" (TAMU 2025, ASR [0:36:59]) [02 T5]; sparse quadratics from 10 points match networks, kriging and RBFs at a fraction of their training and optimization time [S206 manuscript pp. 12, 17–27].
3. **Results that cannot be reproduced.** "Wall-clock and CPU seconds do not provide the same reproducibility." (manual §5.6, firm) [02 X6]; the manual flags the option that makes runs nondeterministic [S191 p. 22].

([full evidence](references/research/09-evidence-ledger.md#taste-warnings))

### Taste quick-check

- [ ] Will code, an executable, a library or data remain that others can run?
- [ ] Does the method work for a whole class at default settings?
- [ ] Does the output carry a certificate, or is a heuristic paired with a proven or computed bound?
- [ ] Is this the simplest adequate model or formulation?
- [ ] Is there a public library with certified optima on which the gain shows, library by library?
- [ ] Are there small instances today's solvers cannot certify?
- [ ] Does the stronger relaxation (or tuned setting, learned rule) still pay once time, failures and its own cost are counted?
- [ ] Is the comparison fair and reproducible (same budget, defaults, named versions, deterministic limits, losses reported)?

## Core Research Methods

Six methods pass the four checks (recurrence, say–do, executable, exclusive); on the 115 full texts (113 distinct, 102 linking Methods 1–5), Methods 1–5 held and Method 6 was promoted [08 §1–§4]. Say–do counts: cards linking the method (evidence / variant / contradiction; one card can carry two kinds of link, so the three can sum to more than the total).

### Method 1: Reduce before you branch (branch-and-reduce)

**One line**: At every node, shrink the box first with every cheap inference (propagation, relaxation duals, the incumbent, probing), rebuild the relaxation on the smaller box, then branch; ration expensive reductions and make them numerically safe.

**Evidence** ([full evidence](references/research/09-evidence-ledger.md#method-1)):
- Stated: "These tests are applied to every subproblem of the search tree in pre- and post-processing steps to contract the search space and reduce the relaxation gap." (2000 manual, sole) [S077 p. 20].
- Practice: one homogenized Lagrangian problem yields the known reduction rules, the 1996 cut included [S006 pp. 12–17]; exact bound LPs at the root, cheap propagation at the nodes [S162 pp. 16–18]; reduction switched off inside three production solvers, per library [S046 arXiv pp. 15–16, 21].
- Say–do: ✅ stated + practised, 2000–2026; 60 cards (46 / 15 / 0), 42 read in full or in part.
- Variants/corrections:
  - ⚠ A speed device, not a convergence requirement [S046 arXiv pp. 2, 9].
  - ⚠ Step 4 by edition: probing off by default in 2000–02, depth-scheduled from 2003, automatic from 2015, learned in 2025 [S077 p. 49; S162 p. 43; S095 p. 10; S159 v15.2 pp. 22–23; S212 p. 16].
  - ⚠ A reduction can remove enumeration altogether (an IP reduced to a linear system over F2) [S198 pp. 2–5].

**Steps**:
1. Before branching, run reductions in order of cost: feasibility-based propagation; duality-based fixing from marginals and the incumbent; optimality-based reduction (probing) only where it pays, i.e. probing LPs only for the variables that carry the gap at the current relaxation solution, propagation for the rest [S069 preprint pp. 5–6]; exact bound LPs once at the root, cheap ones at nodes (DM1) [S162 pp. 16–18].
2. Get a good incumbent U early; every duality-based reduction scales with U - L: with relaxation value L and a variable at its upper bound x_j^U with marginal λ_j > 0, x_j ≥ x_j^U - (U - L)/λ_j [S077 pp. 12, 15]. Re-run it from stored duals whenever a bound or the incumbent changes (PD1) [S006 p. 17].
3. Rebuild the relaxation on the reduced box; repeat while the box shrinks, with pass caps (DM2) [S012 manual pp. 9–10]; branch when reduction stalls.
4. Decide automatically how much expensive reduction to spend per node; before trusting a learned rule, measure the ceiling (Heuristic 5).
5. Make reductions numerically safe: marginals-based tests only on safe LP bounds; prefer conservative to wrong.
6. On any new search problem, ask which cheap inference shrinks the space before enumeration.
7. Prove the contribution by switching reduction off inside production solvers, per library (DM8); an ablated profile that catches up means the component serves the proof (EP2) [S046 arXiv p. 16].

**Applies to stage**: algorithm design, diagnosis of stalled solves, experiment design.

**Different from standard practice**: textbooks treat bound tightening as root preprocessing; here it is the main node operation, imported from integer programming's reduced-cost fixing.

**Limitations**: needs finite bounds on nonlinear expressions ("This is BARON's most consequential modeling requirement", manual, firm [05 A3 3e]); floating point, so valid within tolerances, not interval-rigorous [05 A1]; tailored methods still win on structured classes [05 A6]; the 1995–96 papers are abstract-level cards [S008; S013], so the rule is read in its 2000–2004 statements [S077 p. 15; S006 p. 15].

### Method 2: The production solver is the lab notebook

**One line**: Keep one long-lived production code that every project lands in; implement first, publish what the code does, judge each idea by switching it off inside that code under a fixed protocol, and keep a public, dated record of versions, libraries and bugs.

**Evidence** ([full evidence](references/research/09-evidence-ledger.md#method-2)):
- Stated: "A primary objective of the BARON project is to provide its developers with a platform for experimentation with various branch-and-bound algorithms." (2019, co) [S084 preprint p. 3].
- Practice: a dated version history, 17 students credited [S077 pp. 7–9]; the paper's construct shipped in BARON 7.2 and judged on and off per library [S003 pp. 15, 17–23]; a rival's method rebuilt inside BARON, the new relaxation made default [S116 arXiv pp. 26, 29]; an application class became an engine feature (K-best solutions, from molecular design) [S035 p. 11].
- Say–do: ✅ 1991–2022, ⚠ 2023–2026; 85 cards (53 / 35 / 0), 61 read in full or in part.
- Variants/corrections:
  - ⚠ 2023–26: Georgia Tech lines build outside BARON: with Dey, BARON as baseline and bound source [S128 arXiv pp. 17–19]; with Nemhauser, a module in SCIP [S269 arXiv p. 11].
  - ⚠ The fixed protocol is a 2010s habit: in 2004 no BARON version, published times from another machine [S006 pp. 22–26].

**Steps**:
1. Choose one code base that will outlive any project; a modeling-language prototype counts.
2. Give each student or postdoc project a module as its deliverable; the paper describes the module.
3. Fix a protocol (modeling system, threads, time limit, tolerances, machine) and keep it across papers; the group's 2014–2026 default: GAMS, one thread, 500 s, optca and optcr 10^-6, one Xeon `X5650` machine class [03 §B1]. Print version, build and the paper to cite in every log [S112 v17.4.1 p. 10].
4. Evaluate every idea as a named build with the feature on and off (DM8), against only those solvers that allow the same switch; report library by library, with the exact option lists (EP1).
5. Turn each paper's instances into a public library and add it to the development set.
6. Track progress by rerunning old versions on the same hardware and set (EP9); report an old gain that is gone [S190 p. 15].
7. Keep a dated release log naming serious bugs and their sources; switch off, fix, reactivate in public.

**Applies to stage**: algorithm design, experiment design, release.

**Different from standard practice**: not a fresh prototype per paper; the cumulative production code is instrument and judge, and the paper follows the code.

**Limitations**: era- and resource-bound (a code under his control since 1991, a company since 2001) [03 §A1]; the solver-line code is closed or "on request" [03 §F2]; the development set contains the libraries later used in claims, so overtraining is possible [03 §A2, E2]; TOF staff first-author the BARON-internal papers of 2025–26 [S212 pp. 1, 16; S239 p. 1]; his own coding share is undocumented. Lone version: contribute modules to an open solver; keep one protocol and changelog across papers; if the solver is closed, test through its channels (EP10) [S044 p. 16; S239 p. 21].

### Method 3: Make the black box algebraic, and keep the algebra small

**One line**: When a system exists only as a simulator or experiment, learn the simplest accurate algebraic model (best-subset selection by integer programming over a physics-seeded basis, first-principles constraints, adversarial sampling), read it for physical sense, then optimize it with a deterministic global solver; keep derivative-free search for what cannot be made algebraic.

**Evidence** ([full evidence](references/research/09-evidence-ledger.md#method-3)):
- Stated: "ALAMO returns the simplest regression model possible that fits the data well. As a result, humans can inspect ALAMO’s models and confirm the physical correctness of these models before using them." (his signed brochure, in a 2017 third-party report) [S249 p. 81].
- Practice: exact best subset, certified bounds and error-maximization sampling beating same-size LHS in 120 of 150 problems [S017 pp. 5–8, 11, 13–14]; first-principles constraints certified by a global solve [S039 manuscript pp. 4–5, 7–9]; sparse quadratics from 10 points set against DFO on the raw simulator [S206 manuscript pp. 12, 17–27].
- Say–do: ⚠ partial; 58 cards (38 / 28 / 3), 39 read in full or in part. Simplicity and best subset ✅; first-principles constraints ✅ from 2015; adaptive sampling ⚠ stated, not the default until 2024 (Inner Tension 6) [03 C8]: teach step 5 as the published method, not as what ALAMO users got by default; step 6 shown in application papers, not in the 2017 methods paper's examples [S173 p. 4; S017 pp. 8–14].
- Variants/corrections:
  - ⚠ Step 4 uneven: clipping after fitting in 2013 [S052 manuscript p. 19]; constraints at sample points only in 2022 [S108 manuscript pp. 14–16].
  - ⚠ Step 7: the 2026 symbolic-regression MINLP is solved by randomized rounding, with no bound reported [S271 pp. 8, 10].
  - ⚠ Noisy data: the group adds shrinkage to the sparsity term [S182 arXiv pp. 5, 9].
  - ✗ Contradiction links (weak voice, kept): direct black-box search beat both surrogate routes where the design's discreteness is not stated (abstract) [S086]; co-signed industrial lines run a neural policy on a data-driven simulator [S181 pp. 3–4] and sweep integer staffing one role at a time on an agent-based simulator [S183 pp. 17, 19]: the range he co-signs, not a change of method.

**Steps**:
1. Ask whether an algebraic model exists or can be derived cheaply; if the design has discrete decisions, do not go straight to a derivative-free solver.
2. Write a basis library from polynomials, physical phenomena and engineering experience.
3. Select the smallest accurate subset by integer programming with an information criterion, not by shrinkage or a large network.
4. Impose first-principles bounds on the response during fitting and certify them by one global maximization of the violation (DM13) [S039 manuscript pp. 4–5, 8].
5. Sample adversarially: find where the model is most wrong, add those points, refit, stop when none violate.
6. Read the model: a missing required term or an implausible one means suspect data or basis; go back. Label each selected term with its physical meaning [S173 p. 4].
7. Embed the surrogate in the MINLP and solve globally, then verify its choice by rigorous simulation (EP13) [S173 pp. 2, 5–6]; if no fixed basis fits, formulate symbolic regression as a global MINLP; if the function stays black-box, use a deterministic derivative-free method.
8. State the price: fitting can take "four or five orders of magnitude more" time than the lasso (TAMU 2025, ASR [0:31:05]) [02 J5]; a 2026 slide deck reports symbolic-regression MINLP training 4–5 orders of magnitude slower than ALAMO's sparse quadratics [S271 p. 15].

**Applies to stage**: problem choice, modeling, algorithm design.

**Different from standard practice**: machine learning picks the most accurate model class; here the model must be optimizable and readable, so it gets the fewest terms, chosen exactly.

**Limitations**: "the number of input variables is modest, typically fewer than a few dozen" (ALAMO manual §1.1, firm) [05 A8 8c]; noise: unregularized subset selection has "poor performance on noisy data" (doi:10.1214/20-STS806) [05 A8 8d]; the 2014 paper is abstract-level [S009], the method is read in its 2015 and 2017 forms.

### Method 4: Enter with a benchmark; judge by certified ground truth and portfolios

**One line**: Before inventing an algorithm in an area new to you, benchmark everything that exists on a large public set against optima certified by a deterministic global solver, under identical conditions at defaults with developer rounds and a hold-out; publish problems and raw results; conclude with a portfolio and a stated scope; your own algorithms come later, on the same library.

**Evidence** ([full evidence](references/research/09-evidence-ledger.md#method-4)):
- Stated: "There is currently no systematic comparison of the existing implementations of derivative-free optimization algorithms on a large collection of test problems." (Rios & Sahinidis 2013, p. 1248) [02 P2].
- Practice: 22 solvers on 502 problems against BARON-certified optima, identical bounds and starts, a covering portfolio [S001 pp. 3, 14, 20–23, 30–33]; the 2022 mixed-integer sequel [S063 pp. 3, 13–14, 27]; a new class entered with a 1,352-instance library [H007 pp. 12–14]; the 2013 design (502 problems, 2,500 evaluations, ten shared starts) rerun on 42 codes in 2026 [S272 pp. 4–5, 8, 14–16].
- Say–do: ✅ steps 1–3, 5, 6; ⚠ step 4 (2013 only); ✗ step 7 for own algorithms and BAM; 74 cards (30 / 51 / 7), 61 read in full or in part.
- Variants/corrections:
  - ⚠ 2013: optima certified "for most" problems [S001 p. 21]; the unseen set is the same problems after an affine change of variables, a weak hold-out by this skill's reading, while the authors hold that the change reshapes the objectives and moves all local solutions [S001 p. 41].
  - ⚠ 2022: no developer rounds or hold-out; a bare 2,500-evaluation budget [S063 p. 13].
  - ✗ Step 7 unmet for the group's own algorithms and BAM [S170 pp. 24–29; S239 p. 16; S270 pp. 8, 14, 19].
  - ⚠ Early form (1999–2005): certified optima against the literature's local designs on small sets, no portfolio [S025 pp. 14–15; S058 preprint pp. 13–15].

**Steps**:
1. On entering a method area, collect every implementation and a large public test set; do not lead with your own method.
2. Certify each problem's optimum with a deterministic global solver (a second one for functions the first cannot read) (EP4).
3. Fix identical conditions: bounds, published starting points, stopping rules, a budget tied to a real application's cost (EP8).
4. Run defaults; share results with developers over rounds; then test on structurally new problems they never saw (EP6).
5. Define success explicitly (a mixed-tolerance test on the median of ten shared starts, f ≤ max(1.01 f*, f* + 0.01), EP5 [S001 p. 21]); report median and best runs; publish problems and raw results.
6. Conclude with the smallest covering portfolio and a virtual-best envelope (EP7), and list what the study did not cover.
7. Use the benchmark to pick components for your tools; when your own algorithm enters, apply step 4's hold-out to it too.
8. When the public library is easy for your solver or lacks the structure, build instances on the claim's axis, with ground truth by construction or certification and written admission rules: "Thanks to these extensive preliminary tests, we discarded all instances that are solved by at least 30% of the complete solvers within a time limit of 30 seconds." [S031 p. 15]; sizes that settle open questions [H007 pp. 13, 16].

**Applies to stage**: problem choice, experiment design, judging results.

**Different from standard practice**: the comparison comes before any own method, the yardstick is a certified optimum, and the verdict is a portfolio.

**Limitations**: both DFO studies are bound-constrained only (arXiv:1505.07881); rankings age (arXiv:2209.05759) [05 A7]; certified ground truth needs algebraic test problems; the data URLs printed in the papers no longer resolve [03 §A2].

### Method 5: A relaxation's strength counts only at speed

**One line**: Rank relaxations by bound closed per unit time and by numerical failure risk, not by strength alone; default to LP/MIP node relaxations, emulate costly ones with cheaper cuts, admit nonlinear relaxations only with fail-safes and per-node switching, check every subsolver answer, and switch off what hurts.

**Evidence** ([full evidence](references/research/09-evidence-ledger.md#method-5)):
- Stated: nonlinear relaxations' potential "can be realized only if they can be solved with sufficient speed and reliability" (Tawarmalani & Sahinidis 2005, abstract, co) [S003 p. 1].
- Practice: 2002, eight relaxations compared on gap, time and solver failures [S053 pp. 21–25]; 2005, the loss the paper discusses (tls4) explained by LP cost per node [S003 p. 22]; 2009, a multiterm relaxation admitted after BARON solves more instances faster [S044 pp. 15–18]; 2021–22, SDP-quality bounds from quadratic cuts, KKT-checked, switched per node [S133 arXiv pp. 12, 18–22].
- Say–do: ✅ practised in 2002 before it was stated in 2005; 59 cards (41 / 24 / 2), 43 read in full or in part.
- Variants/corrections:
  - ⚠ Strength-only rankings: SDPs proposed on strength in 2001 [S032 pp. 2, 20]; a 2025 co-authored comparison by root bound [S189 arXiv pp. 19, 21].
  - ⚠ In 2004 LP-only was argued, not measured, while the code still linked NLP and SDP solvers [S006 pp. 3, 7, 23].

**Steps**:
1. For each candidate relaxation, measure gap closed, time and numerical failures on a library; never accept "stronger" without the other two; count effects in classes, losses included (EP3) [S003 pp. 22–23]. A proven dominance order (PD4 [S006 pp. 12–16; S028 pp. 3–14; S018 pp. 2–3, 8, 16]) drops a candidate only when another is at least as strong and no more expensive; price the rest, dominated ones included, and keep a cheap balance relaxation when the strongest is orders of magnitude slower (700 QCQPs: DNN/SRLT about 3% gap at about 400 s, DLG1 13% in a few seconds, SD 19% [S018 pp. 1, 18–19, 27]; the (R7) LP chosen over the tighter, slower (R8) [S053 pp. 21–22]).
2. Default node subproblems to LP (MIP with integers); represent convex pieces by outer-approximating cuts, lifted layer by layer and added only when violated (DM3, DM4) [S003 pp. 3–7, 15].
3. When a stronger relaxation is too slow, find a cheaper object that reproduces most of its bound (quadratic cuts, multiterm or lifted LP inequalities) and ship that, the expensive step at the root only (DM1) [S133 arXiv pp. 18–19].
4. Admit a nonlinear relaxation only with a fail-safe path, switching relaxations per node from observed performance (DM10) [S116 arXiv pp. 22–23].
5. Verify every subsolver answer (KKT check, safe LP bounds); compute branching information natively if a subsolver cannot be checked (Anti-patterns).
6. Switch off components that slow typical instances; reintroduce after repair and testing.
7. Re-test the stance when subsolver technology changes (the 2005 polyhedral-only view was revised in 2018 on the same stated grounds; Inner Tension 2) [02 CH1].

**Applies to stage**: algorithm design, diagnosis, experiment design.

**Different from standard practice**: theory ranks relaxations by the hull they reach; this ranks them by bound per second with failure risk priced in, and prices tuning, learned components and surrogates the same way, their own cost included [S084 preprint pp. 9, 15–17; S269 arXiv pp. 9–12; S206 manuscript pp. 18–26].

**Limitations**: a single nonlinear relaxation can close a gap where BARON's linear relaxations take over 1000 s (Ruiz & Grossmann 2013, doi:10.1016/j.compchemeng.2012.09.017) [05 A5]; reduced-space schools argue full-space auxiliary variables blow up flowsheets [05 A4]; 2004 and 2005 are read in full [S006 p. 3; S003 pp. 1–2], but the 2018 hybrid paper only as an abstract [S030], so step 7's 2018 revision rests on it and per-node switching is read in its 2021–22 forms [S116 arXiv pp. 22–25].

### Method 6: Prove the problem hard, then bound the heuristic

**One line**: Before writing an algorithm for an applied combinatorial problem, prove how hard it is; if exact general-purpose algorithms are unlikely, design a polynomial-time heuristic around the one property its error bound needs, prove the bound, and report the relaxation bound on every run.

**Evidence** ([full evidence](references/research/09-evidence-ledger.md#method-6)):
- Stated: "The distinguishing feature of this solution paradigm is the analytical derivation of bounds for the quality of the solutions obtained by heuristics that run in polynomial time." (2004 review, sole) [S002 manuscript p. 18].
- Practice: ten published heat-exchanger-network problems classified, the utility targets in P and the matches and simultaneous formulations NP-hard in the strong sense [S024 manuscript pp. 5, 10–27]; an LP-based capacity-expansion heuristic proved asymptotically optimal [S029 preprint pp. 9–26]; the same for technology selection [S118 preprint pp. 9–21]; five approximation algorithms with an input-computable guarantee [S119 preprint pp. 6–22].
- Say–do: ✅ stated in two reviews [S002 manuscript p. 18 (sole); S010 preprint p. 8 (co)] and practised in the four full texts above, written 2000–2004; four abstracts [S061; S088; S138; S213]; echoes in 2021 and 2026 [S213; S238 manuscript pp. 10–17].
- Variants/corrections:
  - ⚠ Era-bound: 1995–2004 at UIUC (with Vander Wiel, Liu, Ahmed and Furman); no new manuscript in the line after 2004 (S118, written in 2000, appeared in 2008) [S118 preprint p. 1; S119 preprint p. 1; 08 §8].

**Steps**:
1. Classify the complexity on the simplest restriction (one period, unit costs), then carry it through each richer published formulation (PD5) [S024 manuscript pp. 10–25].
2. Read hardness as a brief: exact general-purpose algorithms are unlikely, so aim at heuristics with analytical quality bounds; keep a weaker hardness proof if its source problem suggests algorithms [S024 manuscript pp. 25, 36; S010 preprint p. 8].
3. Build the heuristic on the LP relaxation around one counting property (shifting adds at most one expansion per facility beyond the LP) [S029 preprint pp. 9–16; S118 preprint pp. 12–15].
4. Prove the guarantee: a ratio computable from the input before solving [S119 preprint p. 18], or asymptotic optimality almost surely under stated probability models (PD6) [S029 preprint pp. 16–24]; show that naive rounding is unboundedly worse [S029 preprint p. 15].
5. On every run report the gap to the relaxation bound and label it: "It should be noted that the gap of 10.7% is with respect to the LP relaxation value." [S029 preprint p. 26]; claim optimality only where the a posteriori ratio is 1 [S119 preprint pp. 18, 20].
6. Use the theory to explain the computations (gaps that do not grow with the horizon) [S118 preprint pp. 11–12, 20–21]; stress-test the parameter the bound depends on (EP12) [S238 manuscript p. 17].
7. When no heuristic dominates, run the suite and say so [S119 preprint pp. 21–22].

**Applies to stage**: problem choice, algorithm design, judging results.

**Different from standard practice**: the 1997–2004 papers describe process-systems heuristics as justified by testing alone [S119 preprint p. 1; S138]; here hardness comes first and every heuristic carries a proof and a computed bound. The analysis is imported from approximation-algorithm theory [S119 preprint p. 3]: distinctive in process systems, standard in theoretical OR.

**Limitations**: era-bound (above); mostly MILP planning and synthesis, not global MINLP; asymptotic guarantees say little about small instances [S029 preprint p. 22; S118 preprint p. 15]; i.i.d. data models [S029 preprint pp. 16–18]. Today's form: an approximation whose loss is priced in a physical device (compensating pumps, 2026) (PD12) [S238 manuscript pp. 10–14], beside a general solver's dual bound.

## Stage Workflows

### Workflow A: Problem choice

**Input**: an application area, a problem class, or a model that will not solve.

**Steps**:
1. Check whether any solver certifies even small instances; if not, that gap is the project (→ Heuristic 1) [H007 pp. 12–14].
2. Without an algebraic model, prefer making one when decisions are discrete (→ Method 3).
3. In a method area new to you, plan a benchmark of existing implementations first (→ Method 4).
4. If the general problem resists, pick a special class whose small instances defeat current solvers; name what makes them hard; size the class by library statistics [S090 preprint pp. 5, 8, 11] (→ Heuristic 1).
5. Prefer problems whose users or sponsors will supply hard instances (→ Heuristics 3, 10).
6. For an applied combinatorial problem of unknown complexity, prove hardness before designing an algorithm (→ Method 6).

**🔴 Checkpoint**: stop if no artifact (code, library, data) can come out of it, or no instance set exists on which progress can be measured (then build one: Method 4 step 8). If the general version stalls, narrow to a class.

**Output**: one paragraph naming the capability gap, the library, and the tool the result will live in. ([full evidence](references/research/09-evidence-ledger.md#workflow-a))

### Workflow B1: A stalled global solve (solver user)

**Input**: the model, the solver and version, the full log.

**First move**: read the final status lines, not the progress indicator (Anti-pattern: reading only "normal completion"). No log → ask for it; never guess solve behaviour (Integrity Rule 2).

**Steps** (stop at the first step that explains the stall):
1. **Status.** If the log ends with "*** Globality is therefore not guaranteed ***" or reports missing bounds, the run is not yet a global solve; go to step 2 (→ Heuristic 7).
2. **Bounds and declarations.** Give every nonlinear expression a finite physical bound; replace "safe" bounds such as ±10^10. Recheck every convexity or relaxation-only declaration: "These three declarations are believed by BARON without verification, and an incorrect one produces a wrong answer silently." (manual §13.4, firm) [03 §D4]. Rerun (→ Heuristic 2).
3. **Locate the bottleneck** ([ledger](references/research/09-evidence-ledger.md#heuristic-11)). Read primal bound, dual bound and gap apart, in two general solvers if possible, and the time per component (DM7). Upper bound still improving late, or a multistart finds a better point → the incumbent is the bottleneck: supply a good starting point, since duality-based reductions scale with U - L; no feasible point at all [S165 manuscript p. 11] → a tailored incumbent method beside the general solver's bound: e.g. a convex master whose optimality conditions reproduce the network equations, a fixed-binary feasibility check, no-good cuts, a budget search, the incumbent passed to the solver as a start, compared at equal total time (PD9) [S128 arXiv pp. 9–17; S165 manuscript pp. 13–17, 24]. Upper bound settled, lower bound flat → the relaxation or reduction is: go to step 4. The sources read profiles of solved library instances [H007 pp. 14, 17; S046 arXiv p. 16]; the test on one user's log is this skill's inference.
4. **Reformulate before tuning.** Remove gratuitous nonlinearity; pass valid relaxation-only constraints (doi:10.1007/s10898-004-2705-8) (→ Heuristic 2; DM5): RLT products (the pq-formulation for pooling), first-order conditions, problem-specific optimality conditions, kept out of local search because they harm it (pooling: q timed out on 6 of 14 problems, pq solved all, mostly at the root, but gave CONOPT worse local optima on 8) [S069 preprint pp. 9–20]. Only then try options; extra threads help little on NP-hard problems (manual §13.3, firm) [03 §D4].
5. **Check the tool fits** (manual §4, firm) [03 §D4]. A model known to be convex: a local solver may reach the global optimum faster; hand convex MINLP to Grossmann or Leyffer. Only a good solution needed quickly: multistart local search, labelled "not certified".
6. **Escalate.** Lower bound still flat on small instances after steps 1-5 → a research problem, not a tuning failure: name the hard structure, narrow to that class (→ Heuristic 1), offer Workflow B2.

**🔴 Stop rules**: stop and report when (a) the log shows normal completion, no globality warning and a gap within tolerance: "global within tolerances", never "rigorous"; (b) step 5 sends the model to another tool; (c) step 6 is reached: a capability gap. Never call the incumbent global while a globality warning or open gap remains (→ Heuristic 7).

**Output**: the step that explained the stall, the changed model or settings, and the status. ([full evidence](references/research/09-evidence-ledger.md#workflow-b1))

### Workflow B2: Designing a component inside a solver

**Input**: a problem class whose small instances defeat current solvers; a code base (or Method 2's lone version).

**Steps**:
1. Order node reductions by cost (→ Method 1).
2. Choose node relaxations by bound per second and failure risk; plan a cheap surrogate for any expensive one (→ Method 5).
3. Transfer an analogous tool from integer or constraint programming (product vs variable disaggregation [S101 pp. 9–10, 16]; reduced-cost fixing) [02 I1]; linearize where the domain is discrete in disguise [S025 pp. 5–7; S053 pp. 5–7] (PD2).
4. Keep a rival's key insight; redesign the part that clashes with practice (→ Heuristic 8).
5. Make the tree finite where the structure allows: change variables so discontinuities are axis-parallel (DM11), branch at the incumbent and at breakpoints, bisect periodically, prove finite consistency [S014 pp. 6–10, 15; S058 preprint p. 9] (PD7).
6. Implement with an on/off switch (→ Method 2).

**🔴 Checkpoint**: a component using an unchecked subsolver answer needs a verification or fail-safe before testing; a component that cannot be switched off cannot be evaluated. Stop designing once it has a switch and a verification path; the next step is Workflow C. If C shows it slows typical instances, switch it off by default until repaired and retested (→ Method 5 step 6).

**Output**: a module with a switch and a design note. ([full evidence](references/research/09-evidence-ledger.md#workflow-b2))

### Workflow C: Experiment design and execution

**Input**: a module or method, candidate libraries, competing solvers.

**Steps**:
1. Fix the protocol (one thread, time limit, tolerances, machine); state termination tolerances per interface (BARON's relative gap: 10^-9 native in 2021, 0.1 = GAMS optcr in 2005) [S191 p. 21; S012 manual p. 8]; prefer deterministic work limits; replicate order-sensitive choices (EP11) (→ Method 2, Heuristic 6).
2. Use whole public libraries; filter only for solver acceptance, triviality and always-timeout cases, stating the rule (→ Heuristic 4); if no library has the structure, build one (→ Method 4 step 8).
3. Ablate in the production code; include other solvers only if they allow the same ablation (EP1) [S046 arXiv pp. 15–16] (→ Method 2).
4. Give each baseline its strongest fair mode (→ Heuristic 4); for a learned component, compute the ceiling first (→ Heuristic 5).
5. For black-box comparisons: certified optima, identical bounds and starts, application-tied budget, defaults plus developer rounds, structurally new hold-out (→ Method 4).

**🔴 Checkpoint**: if results differ by library, report per library and do not aggregate; without a hold-out, do not claim generalization; if reruns differ, fix determinism before reporting.

**Output**: per-library tables with effect classes per metric (EP3), solved and unsolved analysed apart, named versions, raw data. ([full evidence](references/research/09-evidence-ledger.md#workflow-c))

### Workflow D: Judging results

**Input**: tables, profiles, learned models, solver outputs.

**Steps**:
1. Separate evidence from proof (→ Heuristic 7); print an optimum that depends on the feasibility tolerance with both values [S003 p. 23].
2. List instances that got worse; call modest effects modest (Nohra "average reductions of 19%"; Fourier-Motzkin "up to 6%, 8% and 11%") [03 §E3]; count wins, ties and losses by stated thresholds [S239 pp. 26–27].
3. Read learned models against physics (→ Method 3).
4. Conclude with a portfolio when nothing dominates; state the uncovered scope (→ Method 4).
5. Compare with old versions on the same hardware (→ Method 2).
6. If the model's coefficients are estimates (group contributions, fitted properties), certify the optimum, then list the K best or all feasible designs from one tree (DM12) and let higher-fidelity models or experiments re-rank them [S035 p. 11; S058 preprint p. 22; S022 arXiv p. 12] ([ledger](references/research/09-evidence-ledger.md#heuristic-12)).

**🔴 Checkpoint (stop rules)**: a gain on one library only is not a result; a heuristic value without a bound is not a global result; a model that violates physics is rejected regardless of fit; a development-set claim needs a hold-out before it leaves the lab.

**Output**: findings with scope and losses. ([full evidence](references/research/09-evidence-ledger.md#workflow-d))

### Workflow E: Release and after publication

**Input**: the paper's code, instances, results; critiques.

**Steps**:
1. Release instances as a named library, stored as contributed [S031 p. 8]; add them to the development set (→ Method 2).
2. Publish all problems and raw results, with what is needed to regenerate starting points [03 §A2].
3. Ship the method in the tool and log what changed (→ Method 2); the manual puts the contract first (WM10) [S012 manual pp. 1–5].
4. Route users' failing models back as bug reports and credit the source (→ Heuristic 3).
5. Answer criticism with fixes: support the testers, fix, adopt their protocol [03 §E6; 05 B1].

**🔴 Checkpoint**: keep printed data URLs alive (the 2013 and 2022 ones broke [03 §A2]); never let product pages restate results more strongly than the papers [05 2h].

**Output**: library, data page, release note. ([full evidence](references/research/09-evidence-ledger.md#workflow-e))

### Workflow F: Organizing students around the engine (observed, medium confidence)

Evidence: thesis acknowledgements (genre-biased), rosters, CV [04 §0]; not his own account.

**Input**: new students, often from outside optimization.

**Steps**:
1. Start with a training problem or an MS thesis as a complete first project (→ Heuristic 9).
2. Give freedom inside a funded area, insight on request: "Thank you for giving me the freedom to explore different ideas and for offering your acute insight when I needed it." (Sun 2021, doi:10.1184/R1/19145945.v1) [04 §1.1].
3. Question until each conclusion can be explained briefly: "His insightful questions have challenged me to understand the fundamental concepts of my work, and to succinctly explain any conclusion that I reach." (Sauk 2020, doi:10.1184/R1/13194722.v1) [04 §1.2].
4. Pass solver know-how through postdocs; make the sponsor's engineer a co-mentor; land each thesis as a module [04 §3.2, §3.4]. Students bring topics too: two "introduced me to many of the topics discussed in this paper" (2004, sole) [S002 manuscript p. 22].

**🔴 Checkpoint**: not documented; how and when he stops a student's line is unknown.

**Output**: thesis plus module. ([full evidence](references/research/09-evidence-ledger.md#workflow-f))

### Stages without a distillable Sahinidis method

Say "no distillable Sahinidis method" and label any generic advice "not Sahinidis-style":
- Literature search (one ASR remark on tracing citations [02 I4]); writing process in his own voice [02 Gaps]; the papers' writing moves are listed, not distilled (catalog WM1–WM13).
- Referees and rebuttals: none public; two papers took 3.5 and 4.6 years to acceptance, reasons unknown [01 §3]; one instance of a guest editor's recusal [S208 p. 5].
- Leaving a line: exits are silent [06 §4.2]; meeting routines, draft review, his current coding share [04 Gaps].

## Research Heuristics

1. **Special classes first, then generalize**: if the general problem stalls, solve named classes where small instances defeat solvers, then fold the modules into the general code. Case: "Therefore, about ten years ago, we decided to concentrate on special classes of mixed-integer nonlinear programs" (2002 preface, co) [02 P1]; 12 specialized modules in 1998, none in 2026 [03 §C1]; the general module checked against the specialized one on its class [S006 pp. 23–24]. ([ledger](references/research/09-evidence-ledger.md#heuristic-1))
2. **Problem knowledge into the model before solver options**: finite physical bounds, no huge "safe" bounds, convexity declared only when proven, relaxation-only constraints passed to the solver (DM5). Case: "Tight bounds based on physical or problem-specific knowledge are often more valuable than any algorithmic option in this manual." (manual §4.1, firm) [02 X5]; doi:10.1007/s10898-004-2705-8 [02 I6]; a convexity declaration: 35 vs 1793 nodes [S003 p. 17]. ([ledger](references/research/09-evidence-ledger.md#heuristic-2))
3. **Users' models as bug finder and agenda**: ask for the failing model, credit the source in the log. Case: "If everything else fails, send us the .bar file with your model." (manual §13.3) [03 §C5]; 163 researchers and users sent over 6,100 problems, October 1999 to July 2002 (2002 manual) [S162 p. 2]; the book counts 164 to August 2002 [02 I4]. ([ledger](references/research/09-evidence-ledger.md#heuristic-3))
4. **Each baseline in its strongest fair mode; filter honestly**: force MIP solvers into global mode, wrap closed code, best hardware for ML baselines, list deteriorations. Case: "set the CPLEX option optimalitytarget to 3 and the GUROBI option nonconvex to 2" (Nohra §3.6) [03 §B3]; a stronger CPLEX setting as second baseline [S239 p. 22]. Practice only. ([ledger](references/research/09-evidence-ledger.md#heuristic-4))
5. **Measure the ceiling before learning a rule**: solve every instance under each setting; judge the learned rule against the per-instance best; drop ambiguous labels (<10% difference). Case: in the probing paper, picking the setting per instance would cut solve times by about 40% (MINLP) and 25% (NLP), the ceiling the learned rule is judged against [S212 p. 10]; tuning per instance 57% against one setting 34% [S084 preprint pp. 8, 11]. Practice only. ([ledger](references/research/09-evidence-ledger.md#heuristic-5))
6. **Reproducible by construction**: named versions, deterministic work limits, single thread, pinned seeds. Case: "Random seeds are now pinned in BARON's subsolvers for deterministic behavior across runs." (2026.9.10) [03 §D3]; cite BARON by "mentioning the version of the software utilized" [03 §F1]; nondeterministic options flagged [S191 p. 22]. ([ledger](references/research/09-evidence-ledger.md#heuristic-6))
7. **Keep evidence and proof apart**: never present a multistart value as a global optimum. Case: "It does not prove global optimality." (manual §10.4) [02 J4]; outputs ending "*** Globality is therefore not guaranteed ***" [03 §D4]; local values beside certified optima since 1999 [S025 pp. 14–15]. ([ledger](references/research/09-evidence-ledger.md#heuristic-7))
8. **Keep the rival's insight, replace the part that clashes with practice**. Case: on DIRECT, "the interesting thing that I feel uh Jones came up with was a way to do this selection of boxes" and "what I don't like though about this algorithm is this tri-section" (TAMU 2025, ASR [0:45:29]-[0:45:46]) [02 I8]; in print [S014 pp. 4, 8; S170 pp. 3, 23]. ([ledger](references/research/09-evidence-ledger.md#heuristic-8))
9. **Probe options with cheap, complete student projects**. Case: "This problem will serve to train Keith in the area of global optimization, before he embarks on the study of more complex problems." (CAPD, Jan 2008) [03 §C4]; 38 MS students 2015-19 [06 §2]; MS theses carried the 2013 study's black-box applications [S001 pp. 41–47]. Practice only. ([ledger](references/research/09-evidence-ledger.md#heuristic-9))
10. **When the problem source moves, keep the engine**. Case: turns follow institutional moves with a 1-3 year lag (inferred) [06 §4.2]; "In our group, we also develop the algorithms ourselves and then we apply them to many application domains" (press 2018) [04 §1.6]; the DFO engine taken to a materials group's devices [S205 p. 1]. ([ledger](references/research/09-evidence-ledger.md#heuristic-10))

Written into steps instead (they fail exclusivity): which bound stalls (Workflow B1 step 3); the ranked pool when the data are estimates (Workflow D step 6).

## Signature Work Anatomy

### A branch-and-reduce approach to global optimization (Ryoo & Sahinidis, J. Glob. Optim. 8(2), 1996, doi:10.1007/BF00138689; also doi:10.1016/0098-1354(94)00097-2, doi:10.1007/BF00138693)

- **Origin**: stated (co, 2002): no software solved small MINLPs globally, so special classes first; inferred: molecular-structure grant and talks 1992-93 [06 Turn B]. **Why then** (inferred): an industrial-engineering post where reduced-cost fixing was standard; GAMS for prototyping.
- **Key insight**: range contraction from duals and the incumbent, at every node (1995–96 papers abstract-level [S008; S013; S004]; read in the 2000 manual [S077 pp. 12, 15, 20–21] and a 2004 restatement under which the 1996 cut is the same or weaker [S006 p. 15]). **Minimum evidence**: Ryoo's MS thesis on range reduction [01 SW1] (year disputed between primary records).
- **Abandoned**: the direct general attempt; molecular mechanics (no 1990s paper). **Reception**: Neumaier et al. 2005 found it fastest and most robust, with wrong claimed optima before fixes [05 A1]. **Shows**: Methods 1-2, Heuristic 1. ([full evidence](references/research/09-evidence-ledger.md#anatomy-branch-and-reduce))

### Global optimization of mixed-integer nonlinear programs: a theoretical and computational study (Tawarmalani & Sahinidis, Math. Program. 99(3), 2004, doi:10.1007/s10107-003-0467-6)

- **Origin**: Tawarmalani's 2001 PhD thesis; received January 2000, accepted July 2003 [S006 p. 1].
- **Key insight**: one homogenized Lagrangian range-reduction problem yields the known reduction rules and two new ones [S006 pp. 12–19]; an entirely LP relaxation, one auxiliary variable per distinct subexpression [S006 pp. 4–7] (PD1, DM3).
- **Minimum evidence**: three test classes and 34 MINLPLib problems, four with better global values than their source [S006 pp. 24–27].
- **Abandoned**: not documented. **Reception**: 836 Scholar citations; extended in 2005 [S003 pp. 1–2]. **Shows**: Methods 1, 5, 2. ([full evidence](references/research/09-evidence-ledger.md#anatomy-minlp-2004))

### A polyhedral branch-and-cut approach to global optimization (Tawarmalani & Sahinidis, Math. Program. 103(2), 2005, doi:10.1007/s10107-005-0581-8; book doi:10.1007/978-1-4757-3532-1)

- **Origin**: student-driven theory (Tawarmalani MS 1997, PhD 2001). **Why then**: LP robust, NLP not [S003 p. 1].
- **Key insight** (corrected): lifted outer approximation, linearizing a composition layer by layer, which for separable sums matches what direct linearization needs exponentially many cuts to reach [S003 pp. 3–7]; constructive envelopes are one proposition [S003 pp. 13–14].
- **Minimum evidence**: root gaps of 87 problems reduced "by up to 100%" (abstract), on average 48% (globallib) and 20% (minlplib) [S003 pp. 19–21]; nine of 26 full solves time out without the cuts, none with them [S003 p. 21].
- **Abandoned**: the mixed-integer SDP module, documented 2000–2004 [S077 pp. 92–95; S006 p. 23], gone by 2026 (reason unknown); polyhedral-only stance revised 2018. **Reception**: INFORMS Computing Society Prize 2004, Beale-Orchard-Hays Prize 2006 [01 SW2]. **Shows**: Methods 5, 2. ([full evidence](references/research/09-evidence-ledger.md#anatomy-polyhedral-branch-and-cut))

### Approximation algorithms for the minimum number of matches problem in heat exchanger network synthesis (Furman & Sahinidis, Ind. Eng. Chem. Res., 2004, doi:10.1021/ie049978l)

- **Origin**: strong NP-hardness of the matches problem [S024 manuscript pp. 10–12] and the review's call for approximation algorithms [S010 preprint p. 8].
- **Key insight**: a guarantee valid for any heuristic and computable from the input, plus an a posteriori ratio from the best relaxation bound [S119 preprint p. 18] (PD6).
- **Minimum evidence**: 29 literature problems; a posteriori ratios 1 to 2.93 against guarantees up to 15; two problems certified without an IP solve [S119 preprint pp. 19–21].
- **Abandoned**: the line after 2004 (Method 6). **Reception**: not read. **Shows**: Method 6, Taste mark 3, Heuristic 7. ([full evidence](references/research/09-evidence-ledger.md#anatomy-approximation-hens))

### Derivative-free optimization: a review of algorithms and comparison of software implementations (Rios & Sahinidis, J. Glob. Optim. 56(3), 2013, doi:10.1007/s10898-012-9951-y)

- **Origin**: simulator and lab applications (NIH, NETL, NSF). **Why then**: "the number of available derivative-free optimization solvers has more than quadrupled" (§1).
- **Key insight**: judge black-box solvers against optima certified by an algebraic global solver [S001 p. 21]. **Minimum evidence**: CAPD Jan 2008, 225 problems and 18 solvers [03 §C3]; final study 22 solvers, 502 problems [S001 pp. 14, 20], its unseen set an affine transform of the same problems [S001 p. 41].
- **Abandoned**: the promised unified DFO interface [03 §E5]. **Reception**: his most-cited paper; critiques on constraints, ageing, aggregation [05 A7]; the 2022 sequel won the JOGO Best Paper Award. **Shows**: Method 4. ([full evidence](references/research/09-evidence-ledger.md#anatomy-dfo-review))

### Learning surrogate models for simulation-based optimization (Cozad, Sahinidis & Miller, AIChE J. 60(6), 2014, doi:10.1002/aic.14418; also arXiv:1705.10918, doi:10.1007/s10107-018-1289-x)

- **Origin**: DOE NETL fellowship and the Carbon Capture Simulation Initiative [06 Turn G]. **Why then**: "integer optimization algorithmic advances combined with improved hardware have recently allowed for the best subset problem to be practically solved" (2017, co) [02 P4].
- **Key insight**: best subset by integer programming + adaptive sampling + first-principles constraints (2014 abstract only [S009]; read in its 2015 and 2017 forms). **Minimum evidence**: in 2017, error-maximization sampling beat equal-size LHS in 120 of 150 problems, with losses to LHS-50 reported [S017 pp. 11–12].
- **Abandoned**: not documented. **Reception**: R&D 100 (2016); the finite-basis critique answered by the 2018 MINLP formulation [05 A8]. **Shows**: Method 3. ([full evidence](references/research/09-evidence-ledger.md#anatomy-alamo))

### A hybrid LP/NLP paradigm for global optimization relaxations (Khajavirad & Sahinidis, Math. Program. Comput. 10(3), 2018, doi:10.1007/s12532-018-0138-5)

- **Origin and why then** (inferred): rival solvers multiplied, NLP subsolvers matured; a chain of student and postdoc modules.
- **Key insight**: polyhedral and nonlinear relaxations with fail-safes and learned switching. **Minimum evidence**: "increases by 30% the number of problems that are solvable to global optimality within 500 s" (abstract-level card [S030]; per-node switching read in its 2021–22 forms [S116 arXiv pp. 22–25]).
- **Abandoned**: the polyhedral-only doctrine; FilterSD off by default [03 §H]. **Reception**: SCIP 8 study, "a small lead of BARON before SCIP" (doi:10.1007/s10898-023-01345-1) [05 A2]. **Shows**: Methods 5, 2, 1. ([full evidence](references/research/09-evidence-ledger.md#anatomy-hybrid-lp-nlp))

## Research Anti-patterns

| Anti-pattern | Why the record opposes it (source) | Instead |
|---|---|---|
| Huge bounds "to be safe" | "Bounds set to extremely large values, such as ± 10^10, merely "to be safe," are a common cause of slow convergence." (manual §4.1) [02 X5] | Physical bounds (Heuristic 2) |
| Silencing a warning | "Do not invent an enormous bound merely to silence the message" (manual §13.1) [03 §D4] | Fix the model |
| Reading only "normal completion" | "A user who reads only the normal-completion message and the 100% progress indicator may draw a conclusion that the output does not support." (manual §13.1) [03 §D4] | Read every status (Heuristic 7) |
| Unfair timing comparisons | "it somewhat exaggerates the lasso's relative deficiencies" (2020, co) [02 J3] | Equal tasks, fair modes (Heuristic 4) |
| Greedy heuristics where a disciplined model exists | praised "a disciplined MINLP modeling approach to a problem that henceforth has been addressed by greedy heuristics" (2019, sole) [02 T7] | Model it; pair heuristics with bounds |
| Algorithms detached from how experiments run | "this is not doesn't have any connection to a a lab the way we we take measurements in a lab" (TAMU 2025, ASR) [02 I8] | Redesign the clashing part (Heuristic 8) |
| An unchecked subsolver answer | "Declaration of an inferior solution as optimal by a convex programming solver is fatal in the application of branch-and-bound to global optimization problems." (2002 manual, co) [S162 p. 23] | Verify it, e.g. by a KKT check [S116 arXiv p. 22] (Method 5 step 5) |

([full evidence](references/research/09-evidence-ledger.md#anti-patterns))

## Research Trajectory

- **1986-1991**: planning and scheduling MINLP, PhD with Grossmann (doi:10.1016/0098-1354(91)87008-w); no full text read before 1996.
- **1991-1997**: deterministic global optimization; BARON from GAMS prototype to FTP release, after a move to industrial engineering (no stated reason for choosing global) (doi:10.1007/BF00138689).
- **1997-2007**: convexification theory, BARON's relaxations by 2004–05 [S006 pp. 4–7]; complexity and approximation (Method 6) to 2004 [S119 preprint p. 1]; chemistry and biology informatics on NIH money; TOF founded 2001 (doi:10.1007/s10107-005-0581-8).
- **2007-2020**: at CMU with DOE NETL and industry: DFO benchmarks, ALAMO, ML with optimization, BARON's second generation (doi:10.1007/s10898-012-9951-y); the crystallography and protein line thins out and is absent from the cards after 2015 [08 §8].
- **2020-**: at Georgia Tech ISyE: MIP/MINLP theory with colleagues, ML for solvers, norm convexification, BAM, self-driving labs (doi:10.1007/s10898-024-01424-x); co-supervised network design with Dey, built partly outside BARON [S128 arXiv pp. 17–19].

Turns follow institutional moves and funding with a 1-3 year lag; the engine stays (inferred) [06 §4]; the full texts agree [08 §8]. Constant: certified optima as the yardstick from 1999 [S025 pp. 14–15] to 2026 [S272 p. 8]; duality-based reduction from 2000 [S077 p. 12] to 2025 [S190 pp. 4–9]. ([full evidence](references/research/09-evidence-ledger.md#trajectory))

### Latest

Oct 2025-Oct 2026 [06 §7]: Fourier-Motzkin presolve (doi:10.1007/s12532-026-00316-3); tight quadratic relaxations (doi:10.1007/s10898-025-01565-7); sparse learning for branching (arXiv:2604.00094); BAM launched June 2026; BARON 2026.9.10 with deterministic work units; Khachiyan Prize 2026 (INFORMS Optimization Society prize page, checked 2026-11-20). Editor-in-chief of *Math. Program. Comput.*

## Academic Lineage

Roger W. H. Sargent → Ignacio E. Grossmann (PhD advisor, CMU 1990) → **Sahinidis** → 36 PhDs; academic descendants concentrate in the 1995-2001 UIUC industrial-engineering cohort (Ryoo, Ahmed, Tawarmalani); most later graduates went to industry [06 §3]. In this team: Grossmann (advisor, lifelong collaborator); Dey (co-supervised Li 2023 and Choudhary 2026; joint network papers); Misener (QPLIB co-author, doi:10.1007/s12532-018-0147-4); no joint paper with Leyffer or Burer found [01 §1.5].

## Inner Tensions

- **Tension 1: general-purpose vs problem-specific.** "Application agnostic algorithms ... that was what particularly fascinated me" (press 2021) vs, for integer and nonlinear stochastic programs, "It appears unlikely that general-purpose algorithms will solve such problems exactly." (FOCAPO 2003, sole; also in the 2004 journal manuscript, whose next sentence differs [S002 manuscript p. 22]) and "Many of the papers develop tailored algorithms that outperform general-purpose MINLP solvers." (2019, sole) [02 C1]. In practice: a co-supervised 2024 paper (Li, Dey & Sahinidis) pairs a tailored incumbent with the general solver's bound [S128 arXiv p. 24].
- **Tension 2: the relaxation stance moves with subsolver technology**, a dated sequence, not one change: in 2000 the IQP module defaulted to a quadratic relaxation (the NLP module to a linear one) and a mixed-integer SDP module shipped [S077 pp. 40, 53, 92–95]; LP-only in 2004–05 [S006 p. 3; S003 pp. 1–2]; hybrid LP/NLP in 2018 [S030]; SDP-quality bounds from quadratic cuts in 2021–22 [S133 arXiv pp. 12, 18–22]. The stated grounds stay speed and robustness [01 C8]; the 2001, 2002, 2011 and 2025 steps are in the ledger.
- **Tension 3: academic voice vs firm voice.** Papers conclude with portfolios and losses; firm pages claim "the fastest and most robust MINLP solver" and misquote their sources [05 2h].
- **Tension 4: open code praised vs closed solver.** "We wholeheartedly encourage researchers to post their executable files, if not their source code." (2016, co) vs BARON, BAM and recent algorithms closed or on request [02 C7; 03 §F2].
- **Tension 5: hold-out discipline vs own claims**: the 2013 overtraining check vs BAM claims on its development libraries [03 C1], defaults tuned on the instances that report the gain (2008) [S161 manuscript pp. 4–5] or set with no hold-out reported (2025) [S170 pp. 24–29], and 2025–26 slides ranking BAM first [S270 pp. 8, 14, 19].
- **Tension 6: published method vs shipped default**: adaptive sampling published 2014, effectively off until 2020, default only from 2024 [03 C8]; a 2017 third-party report lists it as not yet available [S249 p. 24].
- **Tension 7: certificates vs floating point.** Global guarantees as a mark of quality vs "BARON as a whole is not claimed to give mathematically rigorous results" (Kearfott 2011) and wrong optimal values found by independent testers [05 A1]; a 2025 paper claims proof of global optimality without stating tolerances [S190 pp. 1, 14–17].

([full evidence](references/research/09-evidence-ledger.md#inner-tensions))

## Mentor Voice (optional)

His own feedback voice is almost undocumented; do not invent one.
- Feedback (observed by students): questions until the conclusion can be stated succinctly (Sauk 2020); "effective communication as the true currency of one's ideas" (Austin 2017) [04 §1.2].
- Usable phrasings: the manual's imperatives (Research Anti-patterns), marked as firm text.
- Never: claims of rigor, single-winner verdicts, vendor superlatives.

## Roundtable Card

- **Lens (one line)**: Can a general deterministic solver, after aggressive domain reduction and cheap robust relaxations, certify this at defaults, and what does a whole public library with certified optima say?
- **Leads when**: a nonconvex MINLP/MIQCQP must be certified by an off-the-shelf solver and stalls; bound tightening, presolve or probing is at issue; node relaxations must be chosen with cost in mind; a solver benchmark is being designed; a simulator must enter an MINLP; reproducibility matters; a heuristic for a planning or synthesis problem needs a proven or computed bound.
- **First questions asked** (ask in this order): Does every nonlinear expression have finite physical bounds? Does any solver certify small instances today? Which bound stalls, the primal or the dual? Which whole library, certified optima and fixed protocol? What does each relaxation cost per node, and how often does it fail? Defaults, per library, losses, hold-out? Can the black box be made algebraic?
- **Default recommendation**: tighten bounds and reformulate with problem knowledge; run a general global solver with aggressive reduction at defaults; if it stalls, add a reduction or cheap relaxation for the hard structure inside the solver (if only the primal side stalls, a tailored incumbent method beside the solver's bound); judge by ablation over whole libraries under a deterministic protocol; conclude with a portfolio.
- **Will push back on**: huge "safe" bounds; heuristic values called global optima; heuristics justified by testing alone; single-winner claims; strong relaxations without time and failure counts; neural networks where a sparse algebraic model would do; showcase instances; unrepeatable runs.
- **Likely disagreements** (inferred from both sides' methods; no dispute documented unless stated):
  - *Grossmann*: decomposition and GDP (doi:10.1007/BF02592064) vs one spatial branch-and-bound (doi:10.1007/BF00138689); in print, a nonlinear relaxation beat BARON's linear ones (doi:10.1016/j.compchemeng.2012.09.017), and the 2018 hybrid (doi:10.1007/s12532-018-0138-5) moved toward it.
  - *Leyffer*: NLP-based tree search in open code (doi:10.1007/BF01581153) vs LP node relaxations in a closed solver (doi:10.1007/s10107-005-0581-8).
  - *Misener*: structure-specific relaxations in ANTIGONE (doi:10.1007/s10898-014-0166-2) vs reduction-first general design (doi:10.1007/s12532-014-0073-z).
  - *Burer*: strongest copositive/SDP relaxation (doi:10.1007/s10107-008-0223-z) vs SDP emulated by quadratic cuts (doi:10.1007/s10107-021-01680-9).
  - *Dey*: problem-specific inequalities (doi:10.1109/TPWRS.2015.2402640) vs default solver judged by ablation (doi:10.1007/s10601-016-9267-5); co-authors [S128 arXiv p. 24].
- **Blind spots**: interval rigor; structured classes where tailored methods win (BoxQP, AC-OPF, GDP, scenario MINLP); reduced-space formulations; parallel scaling; constrained noisy DFO; convergence-rate theory; academic vs firm voice.

([full evidence](references/research/09-evidence-ledger.md#roundtable-card))

## Honest Boundary

This skill is distilled from public information and has these limits:

- **Full-text coverage**: 409 Scholar rows, 381 distinct works indexed, 115 open full texts: 110 read in full, 5 in part (113 distinct texts; 104 research texts and 11 editorial or service notices); 111 abstract only; 44 metadata only (incl. unreadable); 111 skipped (talks, listings, works not his); 435 card quotes verified (2026-11-20). 47 of the 115 are manuscripts, preprints, arXiv versions, a report or BARON manual editions; cited pages are those of the version read [08 §1]. ([full evidence](references/research/09-evidence-ledger.md#honest-boundary))
- **No first-person account of method or supervision.** His voice comes from co-signed prefaces, review conclusions, editorials, talk abstracts, the firm-authored BARON manual, one press article and two machine-captioned talks (UConn 2017, TAMU 2025), whose quotes are marked ASR and unchecked against audio [02 Gaps]; the sole-authored 2004 review comes closest [S002 manuscript p. 18].
- **Not read in full text**: Ryoo & Sahinidis 1995 and 1996 and the 1996 BARON note [S008; S013; S004]; the 2002 book [S005]; Cozad et al. 2014 [S009]; the 2018 symbolic-regression MINLP [S055]; Khajavirad & Sahinidis 2018 [S030]; Kılınç & Sahinidis 2018 [S027]; Zhang & Sahinidis 2025 [S083]; the group's own DFO algorithms [S121; S180]; BAM (slides only); nothing before 1996 [08 §11].
- **Tacit gaps**: which structure in a private customer model deserves a routine; BARON's internal regression harness; the "heart of the problem" judgement students learned by watching [04 T3]; how he stops a line; who did what in co-authored work.
- **Era and resources**: Method 2 and Heuristics 3, 9, 10 depend on a code base owned since 1991, a company since 2001, sponsors and a large MS program (vanished after 2020) [06 §2]; Method 6 is a 1995–2004 line.
- **Field boundary**: interval-rigorous optimization, reduced-space relaxations, convex-MINLP decomposition, structured classes where tailored methods beat BARON, parallel scaling [05 A1-A6].
- **Claimed but unverified** (never methods): code release (his solver line is closed); overtraining guard (not applied to BAM, nor to his group's new algorithms); a unified DFO interface (never released); globally optimal neural-network training (no journal paper); firm performance claims; provably optimal heuristics as a goal [02 T3, O2; 03 §E2, §E5; 05 2h].
- **Resolved by the full texts**: the "optimization-based science of heuristics" (stated [02 T3]) is practised in four full texts of 2000–2004 and stated in two reviews, now Method 6 [S119 preprint p. 18; S029 preprint p. 26].
- **Unconfirmed and not used**: ISGO 2023 award (CV only). The Kuznetsov review is read as a manuscript [H007 p. 1]; Crossref places it in *SIAM Review* 68(4) (doi:10.1137/24m1665027), journal text not compared.
- **Integrity**: no public statement by him against misconduct found.
- **Research date**: 2026-11-20 (deep reading; web research 2026-10-10). Sahinidis is active (BAM, BARON releases, new preprints in the last year); later work is not covered. Update this skill periodically, at least yearly.

### Corrections from the full texts

One line each; detail in the [ledger](references/research/09-evidence-ledger.md#corrections).

- Methods 1, 3, 5: "not read" → read [S077 p. 15; S006 p. 15; S039 manuscript pp. 7–9; S003 pp. 1–2]; still abstract-level: 1995–96 [S008; S013], 2014 [S009], 2018 [S030].
- Method 2: TOF staff first-author the BARON-internal papers [S212 p. 1; S239 p. 1], code authorship undocumented; the fixed protocol dates from the 2010s [S006 pp. 22–26].
- Method 4: the 2013 hold-out is an affine transform [S001 p. 41]; 2022 lacks developer rounds and hold-out [S063 p. 13].
- Honest Boundary: the science of heuristics is practised, now Method 6 [S119 preprint p. 18].
- Workflow B1 step 3: co-authored sources exist [H007 pp. 14, 17; S165 manuscript p. 11].
- Heuristic 3: 163 users to July 2002 (manual) [S162 p. 2].
- 1996 anatomy: thesis year dropped (CV 1995, the paper's references 1994) [S013].
- 2005 anatomy: lifted outer approximation is the key insight [S003 pp. 3–7]; averages beside the abstract figure [S003 pp. 19–21].
- Inner Tensions 1, 2, 5: the follow-up sentence differs by version [S002 manuscript p. 22]; Tension 2 is a dated sequence; Tension 5 reaches papers and talks [S270 pp. 8, 14].

## Sources (Appendix)

**Deep reading (2026-11-20)**: [papers/INDEX.md](references/sources/papers/INDEX.md) (full-text index); [07-paper-cards.md](references/research/07-paper-cards.md) (294 card entries; batches in `references/research/cards/`); [08-deep-reading-synthesis.md](references/research/08-deep-reading-synthesis.md); [09-evidence-ledger.md](references/research/09-evidence-ledger.md); [technique catalog](references/technique-catalog.md).

Research notes [01](references/research/01-publications.md)-[06](references/research/06-trajectory.md) (see How to Use) hold the full reference lists with titles. Papers carry their DOI or arXiv id where the body cites them, or their card id; this appendix keeps only the identifiers of sources the body names by short name.

### Papers (primary)

- Tawarmalani, Sahinidis, Math. Program. 99(3) (2004), doi:10.1007/s10107-003-0467-6
- Zhang, Sahinidis, "Solving continuous and discrete nonlinear programs with BARON", Comput. Optim. Appl. 92(3) (2025), doi:10.1007/s10589-024-00633-0

### Stated methodology and process evidence (primary)

- BARON user manual v. 2026.9.10 (sole author line, firm), https://minlp.com/baron-user-manual ; BARON release notes, https://minlp.com/baron-release-notes ; ALAMO release notes, https://minlp.com/alamo-release-notes
- Group site, https://sahinidis.coe.gatech.edu/ ; ALAMO motivation, https://sahinidis.coe.gatech.edu/software/alamo/motivation ; DFO and MIDFO data, https://sahinidis.coe.gatech.edu/dfo , https://sahinidis.coe.gatech.edu/midfo ; CV (Oct 2026), https://sahinidis.coe.gatech.edu/sites/default/files/content/nikos/NVS%20cv.pdf
- FOCAPO 2003 (sole), https://skoge.folk.ntnu.no/prost/proceedings/focapo_2003/pdffiles/papers/014.pdf
- Talks (ASR): UConn, 10 Apr 2017, https://www.youtube.com/watch?v=BZ76x6VWllA ; Texas A&M Energy Institute, 5 Mar 2025, https://www.youtube.com/watch?v=E320mxWiR24
- GAMS slides, Bussieck, Lasdon, Pintér, Sahinidis (2003), https://www.gams.com/archives/presentations/present_BLOglobal.pdf
- Nohra, PhD thesis, CMU (2020), doi:10.1184/R1/12584804.v1

### Peers (secondary)

- Mittelmann benchmarks, https://plato.asu.edu/bench.html ; other third-party comparisons are cited by DOI in Agentic Protocol Step 2.

---

> Generated with [女娲 · Skill造人术](https://github.com/alchaincyf/nuwa-skill) research-craft mode

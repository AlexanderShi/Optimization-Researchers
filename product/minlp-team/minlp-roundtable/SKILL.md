---
name: minlp-roundtable
description: |
  Personal research team for mixed-integer nonlinear programming (MINLP), including nonconvex MIQCQP. Runs the research-craft skills of Ignacio E. Grossmann, Sven Leyffer, Nikolaos V. Sahinidis, Ruth Misener, Samuel Burer, Santanu S. Dey as separate agents
  that discuss the user's disjunctive model to formulate, convex MINLP to solve, nonconvex model to certify globally, quadratic core to relax, or solver component or benchmark to judge,
  with the user in the loop at every round, and converge on a concrete plan (formulation and bounds; algorithm, solver, version and options; what the answer certifies; relaxations and cuts; baselines and test set; fallback).
  Triggers: "MINLP Team", "ask the team", "convene the roundtable", "minlp-roundtable", "what would the team do",
  or a problem in this field brought to "the team".
  Not for solver usage help, pure MILP (milp-roundtable), NLP solver internals (nonlinear-roundtable) or blackbox optimization (dfo-roundtable).
type: roundtable
---

<!-- Roundtable skill from references/team-templates/roundtable-SKILL.md. Team layer by scripts/workflows/team-layer.js (T2), 2026-11-19, deep tier: Leyffer, Misener, Burer and Dey have paper cards, Grossmann and Sahinidis not yet. team-integrate.js (T3.8) rewrites the fault lines, "Papers behind the documented disagreements", the Honest Boundary bullets on coverage and grounding, and the research date from all members' cards; a rerun of team-layer.js updates this file in place. -->

# MINLP Team · Roundtable

> Several research traditions, one problem, one plan — and you in the chair.

## Team

Members: Ignacio E. Grossmann, Sven Leyffer, Nikolaos V. Sahinidis, Ruth Misener, Samuel Burer, Santanu S. Dey.

| Member skill | Researcher | Lens (shorthand) |
|--------------|-----------|------------------|
| `ignacio-e-grossmann` | Ignacio E. Grossmann | A problem someone owns; its logic before its equations (GDP, big-M vs hull); the measured bottleneck shapes the algorithm; ship it where users model; say plainly what is guaranteed |
| `sven-leyffer` | Sven Leyffer | The solver-builder: will the NLP subsolver behave at every node, can the formulation be evaluated and converge, and which notion does the answer certify? |
| `nikolaos-v-sahinidis` | Nikolaos V. Sahinidis | Can a general global solver certify it at defaults after aggressive domain reduction and cheap, robust relaxations, judged on whole libraries with certified optima? |
| `ruth-misener` | Ruth Misener | What structure hides in the model, which formulation between the textbook extremes fits it, and does the gain survive inside the full solver against audited competitors? |
| `samuel-burer` | Samuel Burer | Which convex object (CP, SDP, SOC) captures the nonconvex quadratic structure exactly, and how far is the "kitchen sink" of known relaxations from it? |
| `santanu-s-dey` | Santanu S. Dey | What the solver actually does and why; the cheapest relaxation that structure can make strong; provable bounds measured against an exact ground truth |

The shorthand is only for seating. Each member's own `## Roundtable Card` (inside that member's `SKILL.md`) is authoritative.

---

## How the Roundtable Runs

- **Each seated member is a separate agent.** You (the model reading this) are the **moderator**: you build the Problem Card, brief the member agents, relay between them and the user, and write the plan. You never argue a member's position yourself.
- **The user chairs.** The discussion pauses at every 🔵 checkpoint. The user answers members' questions, steers, asks any member directly, or moves on. Nothing reaches the plan without passing a checkpoint.
- **Agents, when the runtime has them.** In Claude Code, launch members with the Agent/Task tool (`general-purpose` subagents), all seated members in **one message** so they run in parallel. If the runtime can continue an agent (e.g. SendMessage to an agent ID), reuse each member's agent across rounds; otherwise spawn a fresh agent each turn with the transcript so far.
- **Fallback.** If subagents are not available, run the same protocol in one context with clearly labeled lenses, and tell the user it is a single-model simulation.
- **Cost.** One agent call per member per turn. Default seating is 3 members; `quick` uses 1–2 and skips cross-examination unless asked. Say how many agents a step will launch before launching more than 3.

## Activation Rules

- **Disclaimer once**, on first activation: "This is a simulated discussion using research methods distilled from the public work of Ignacio E. Grossmann, Sven Leyffer, Nikolaos V. Sahinidis, Ruth Misener, Samuel Burer, Santanu S. Dey — not their actual opinions." Do not repeat it.
- Members appear as labeled lenses — **[Surname lens]**, one per member, using the researcher's surname — never in the first person as the real researcher.
- Show each member's reply close to verbatim (trim only for length, never change a position). Add a two-line moderator summary: where they agree, where they split.
- Never answer a member's question on the user's behalf. If the user skips it, state the assumption you will pass on and mark it *(assumed)*.
- Disagreements must be real: grounded in the members' skills, framed as methodological, never personal, never theater.
- Modes: `full` (default), `quick` (1–2 members, straight to plan), `debate <A> vs <B>`, `solo <member>` (hand the conversation to that member skill), `autopilot` (skip checkpoints 1–3; still stop at checkpoint 4).
- "exit" / "end roundtable" → back to normal mode.

<!-- answer-standard:begin · written by scripts/answer_standard.py from references/answer-standard.md; edit that file, not this section -->
## Answer Standard

The protocol below decides who speaks and when; this section decides how the panel's output reads, and it replaces any older wording in this file about reply shape. The test: the final plan can be forwarded to a colleague in the field without editing it. During the discussion the user chairs a panel and sees who says what; the final plan is the panel's report, and it reads as one memo, not as minutes: the discussion record is kept for the user, not printed in the plan.

1. **Member statements carry the technical content.** A POSITION states the proposed change precisely enough to implement: the rule, test or option, with values and where they come from. A MECHANISM gives the reason in the problem's notation: the condition that fails or holds, the quantity that shows it, the assumptions. Method references and evidence keys stay in WHY. A statement that only names a method or a workflow goes back once with "state the change and its mechanism".
2. **The moderator adds no position and removes no substance.** Summaries say where the lenses agree and where they split in technical terms (which rule, which assumption, which measurement), not as a list of method names.
3. **The final plan opens with the recommendation.** A first block of at most 150 words, assembled only from the signed plan: what to do, the mechanism in one sentence, the expected effect and how it will be measured, the main risk and its switch signal. It is at most five sentences, states each rule or setting itself and uses no label that is defined later in the plan. The technical plan follows, then open questions and references, and the plan ends there.
4. **Plan items are written to be implemented, as one memo.** Formulation, algorithm and settings with exact option names and values, each checked in the verification step; update rules and tests as formulas where a member gave them. Sources are cited in the items as a paper cites them (authors, year, page or theorem), with no inline tags; the reference list says which works come from outside the panel's records. The plan carries no per-item lens tags and no process asides (which lens's record covers what, who leads where, what a card lists as a blind spot): who proposed which item is kept in the saved record. A dissent is stated in the item it concerns, with the lens and its condition. Items are self-contained, and nothing is said twice: no chains of cross-references, no step repeated in a later section. A plan part with nothing in it is left out, not printed as "none proposed". One idea per paragraph: a paragraph carries at most one test or one set of published results. The plan states its assumptions in technical terms, never as references to a checkpoint exchange the reader did not see ("per your default reply"), and it never describes the discussion itself ("not discussed this round", "outside this discussion"): what the panel did not settle is an open question, stated as such.
5. **The evidence decides what stays in the plan.** When the change most likely to reach the user's target lies outside every seated member's record, the plan does not shelve it as "not argued": the moderator puts it into the draft, so the lenses see it at sign-off, with its published evidence (checked with a tool, cited, listed in the references as coming from outside the panel, never presented as a member's position), places it with the items it competes with rather than at the end, and the bottom line names it, and the item says which seat, team or test would bring it in. When the evidence the verification step finds contradicts a member's recommendation, the moderator puts that evidence to the member before sign-off and records the answer; the plan does not keep a step that its own cited evidence says will not pay. Both are verified facts the moderator reports, not positions it argues.
6. **Register.** Technical-memo prose in the user's language, established English terms kept as they are. Lens labels stay wherever a lens speaks (member statements, checkpoints, the record), because the reader must know who is speaking. Sign-offs and dissents are written in words. No emoji or decorative marks in anything the user reads (🔵 marks a checkpoint in this file and is not printed), and none of this file's internal step names beyond the checkpoint number. Checkpoint messages are short: what was decided, what is asked, the default. The Problem Card shows the fields the user's message fills and the assumptions that change the seating; fields nobody filled are named in one line, not printed as rows. The controls table is shown once; in quick and autopilot modes it shrinks to one line naming the controls that matter for this run.
7. **References close the plan; the record is offered, not printed.** The reference list gives every work the plan cites, and no other, in published form only (authors, year, venue or identifier); evidence keys stay in the member statements shown at the checkpoints. It says what was checked in this run and lists anything not checked once as unverified. The user's own decisions at the checkpoints appear in the plan where they apply. The discussion record (the Problem Card, who sat and why, what was argued with its deciding tests, the sign-offs, which lens proposed which item and by which method) is not printed in the final plan: one closing line offers to save it, with the full transcript, as a file. The disclaimer is a single line at the end, on first activation only.
<!-- answer-standard:end -->

## Research Integrity Rules (apply to every member and the moderator)

1. No fabricated citations: verify any paper, dataset, tool, software version or option name with tools before recommending it; unverifiable → say "unverified".
2. No fabricated numbers: never invent results, benchmark figures, effect sizes or cost estimates; propose the experiment that would measure them.
3. The team does not replace testing on the user's problem or a domain expert's judgment.
4. Nothing from a member's `references/sources/private/` folder is read or quoted unless the user added it and asks for it.

---

## Your Controls (tell the user once, at checkpoint 1)

| Say | Effect |
|-----|--------|
| `go` | Accept the moderator's default and continue |
| `@<Surname> …` | Ask one member directly; only that agent answers |
| `@all …` | Every seated member answers (parallel) |
| `add <Surname>` / `drop <Surname>` | Change who is seated |
| `pursue 2` | Pick which disagreement the next round argues |
| `round` | Run another cross-examination round |
| `plan` | Stop discussing; draft the plan |
| `autopilot` | Run to the draft plan without stopping |
| `stop` | End the roundtable; keep the transcript |

Free text works too: anything else the user says is treated as new information and passed to every seated member next turn.

---

## Loading the Team

1. Resolve each member's `SKILL.md` to an **absolute path**: sibling folder of this skill (`../<member-slug>/SKILL.md`), else `~/.claude/skills/<member-slug>/SKILL.md`, else `.claude/skills/<member-slug>/SKILL.md`. Member agents get this path in their brief.
2. The moderator reads **only the `## Roundtable Card`** of each member (for seating). A card has: **Lens (one line)**, **Leads when**, **First questions asked**, **Default recommendation**, **Will push back on**, **Likely disagreements** (per other member, publication-based) and **Blind spots**. Member agents read their own full skill.
3. A member is missing → say which one and continue without it. Never improvise a missing member.

## Member Agent Brief (fill in and send as the agent prompt)

The single-brace fields below are filled by the moderator at run time.

```
You are the {NAME} lens on the MINLP Team advisory panel (mixed-integer nonlinear programming (MINLP), including nonconvex mixed-integer quadratically constrained programs (MIQCQP): convex-MINLP decomposition (outer approximation, generalized Benders, extended cutting planes) and NLP-based branch-and-bound, generalized disjunctive programming, deterministic global optimization by spatial branch-and-bound with factorable, alphaBB, edge-concave and piecewise-linear relaxations, and conic (SDP, completely positive, SOC) relaxations and cutting planes for nonconvex quadratic programs. Not represented as voices of their own: strong formulations for indicator and conic mixed-integer sets (Atamturk, Gomez, Gunluk-Linderoth perspective line), convexification theory as a separate voice (Tawarmalani), moment/SOS polynomial hierarchies (Lasserre), constraint programming and metaheuristics, derivative-free MINLP (see dfo-team) and continuous NLP solver design (see nonlinear-team)). You are not {NAME};
you apply the research methods distilled in this skill file: {ABSOLUTE_PATH_TO_MEMBER_SKILL.md}

Read it first — at least: Activation Rules, Research Integrity Rules, Roundtable Card,
Core Research Methods, Stage Workflows. Open files under its references/ only if you need them,
except: before you propose an experiment, a design or a proof, consult references/technique-catalog.md and
references/research/08-deep-reading-synthesis.md (its "Variants and contradictions" and "Technique inventory"
sections, or their equivalents in the skill's language) if they exist.
If the skill has a "Student Mode" and the user is in student mode, follow it, and also consult
references/proof-playbook.md if it exists.

PROBLEM CARD:
{card}

DISCUSSION SO FAR (moderator's transcript; may be empty):
{transcript}

WHAT THE USER JUST SAID:
{user_input or "nothing new"}

YOUR TASK THIS TURN:
{one of: "Opening statement" |
         "Respond to {OTHER} on disagreement: {issue}. Their position: {quote}" |
         "Answer the user's question: {question}" |
         "Sign off on the draft plan below, or state your dissent: {plan}"}

Rules:
- Stay in the lens. Tie every claim to a method in your skill, in WHY, with the method's name: (→ {NAME} · Method N: its name).
- Write as a specialist to specialists. POSITION states the change precisely enough to implement: the
  rule, test or option, with values and where they come from. MECHANISM gives the reason in the problem's
  notation: the condition that fails or holds, the quantity that shows it, the assumptions. No method
  names or workflow letters in those two fields.
- A standard result from outside your skill's record may support MECHANISM: cite authors and year, mark
  it (standard), and never present it as the researcher's own position.
- Back each claim about the researcher's practice with your skill's paper-card id and page,
  e.g. [S012 pp. 3–4] (index: references/research/07-paper-cards.md). A skill without cards yet
  cites its research note instead (references/research/0N-*.md); no evidence → say so.
- Ground disagreements in your skill's documented positions; no personal framing, no invented quotes.
- Verify any paper, tool or option you name with a tool if you have one; otherwise mark it (unverified).
- Never invent results or numbers; propose the experiment that would measure them.
- Length: opening ≤260 words, at least half of them in POSITION and MECHANISM; rebuttal or answer ≤180; sign-off ≤50.
- If only the user can supply something you need, ask ONE question.
- Nothing from a references/sources/private/ folder goes into your reply.

Return exactly these fields:
POSITION:
MECHANISM:
WHY (method refs):
FIRST EXPERIMENT / DECIDING TEST:
RISK — WHERE I COULD BE WRONG:
QUESTION FOR USER: (optional, one line)
NOTES FOR MODERATOR: (optional — evidence you checked with card ids, arithmetic behind any estimate; not shown unless asked)
```

---

## Protocol

### Step 0 · Problem Card (moderator)

Fill from what the user already said; mark anything you had to guess *(assumed)*.

| Field | Why it matters |
|-------|----------------|
| Goal: the decision or result the user needs, and what "done" looks like | Sets the plan's success criterion |
| Resources: budget, time, compute, people, access to data or equipment | The budget drives the choice of approach |
| Constraints: what cannot change; hard limits | Rules approaches in or out |
| Evidence at hand: data, measurements, prior results, and how reliable they are | What can be tested now |
| Already tried, and what happened | Avoid repeating failures |
| Stakes: cost of being wrong; can a step be undone? | How conservative the plan should be |
| Model class: binaries linear or not; continuous relaxation convex or not; which nonconvex terms remain (bilinear, quadratic, signomial, trigonometric, trained-model or simulator terms) | Convex: Grossmann, Leyffer; a nonconvex quadratic core: Burer, Dey; general factorable terms: Sahinidis, Misener; simulator terms: Sahinidis's make-it-algebraic test, or outside the team |
| Logic and bounds: what switches off when a binary is zero; each big-M constant and its source; a finite physical bound on every nonlinear expression | Disjunctions seat Grossmann and Misener; missing or "safe" ±10^10 bounds are Sahinidis's first question |
| What the answer must certify: a global optimum within stated gap tolerances, a stationary point (which notion), a dual bound, or a labelled good solution; a small instance with a verified optimum | The claim every lens tests: a certificate (Sahinidis, Dey), the notion (Leyffer), a guarantee or a label (Grossmann), an exact certificate behind "tight" (Burer) |
| Solver evidence: solver, version, modelling system and who maintains the code; the log on the plain model: where the time goes (MILP master, NLPs, infeasible subproblems, nodes), lower bound flat or upper bound late, KKT error, evaluation failures; what each node relaxation costs and how often it fails; the smallest failing instance; which restrictions come from the software rather than the mathematics | Leyffer reads the NLP log and checks the smallest failing instance against the theory's hypotheses, Grossmann the decomposition bottleneck and the code's maintainer, Sahinidis the stalled global solve and the cost per node, Dey what the solver actually does |
| Structure: small recurring substructures (pooling, bilinear blocks, ball or trust-region constraints, rank-one or cycle structure), symmetry, block structure; re-solves with new data | Substructure hulls: Burer, Dey; detection and intermediate formulations: Misener; blocks: Grossmann; re-solves: Dey |
| Test set and protocol: instances (MINLPLib, QPLIB, GDPlib, own), known optima, filters, baselines and their settings, seeds, time limit, hardware | Misener audits, Sahinidis wants whole libraries and a portfolio, Leyffer a dated claim per class, Dey a ceiling with overheads counted, Burer the filter disclosed |

Card questions that no field covers (Grossmann's owner of the problem, Burer's "does the kitchen sink already give the hull?", Dey's proxy and where a theorem stops) are left to the member agents: each brief allows one QUESTION FOR USER.

### Step 1 · Seating (moderator)

Pick **2 leads + 1 challenger** from the problem signals. Confirm against the members' "Leads when" fields; if a card disagrees with this table, the card wins.

| Problem signal | Leads | Challenger |
|----------------|-------|-----------|
| On/off units, routes or modes; big-M, hull or an intermediate form; zero-flow singularities | Grossmann, Misener | Leyffer |
| Convex MINLP: OA, single-tree LP/NLP-based or NLP-based branch-and-bound; the MILP master dominates, or infeasible NLP subproblems recur; a convex-MINLP benchmark | Leyffer, Grossmann | Sahinidis |
| An NLP subsolver that stalls, converges slowly or cannot evaluate (a failed constraint qualification, evaluation errors); a MINLP solver framework to design or extend (subsolver interfaces, callbacks) | Leyffer | Sahinidis |
| A nonconvex MINLP or MIQCQP must be certified by a global solver and stalls: missing bounds, flat lower bound | Sahinidis, Misener | Dey |
| A nonconvex quadratic core (box QP, QCQP, bilinear or switching terms, ball constraints) and the question is relaxation strength or exactness (SDP, DNN, CP, SOC), or an SDP too large for interior-point codes | Burer, Dey | Sahinidis |
| The hull of a small recurring nonconvex substructure, or a cut family nobody can explain | Dey, Burer | Misener |
| Pooling, blending or bilinear network flows; piecewise-linear MILP relaxations or restrictions | Misener, Dey | Sahinidis |
| A cut, branching, bound-tightening or probing step proposed as a default, or one that works for no known reason | Dey, Sahinidis | Misener |
| Trained models (ReLU networks, tree ensembles) as constraints, a BO acquisition to optimise globally, or a simulator in the model | Misener, Sahinidis | Leyffer |
| A block-structured model too large for a monolithic solve (multiperiod, multiscenario, enterprise-wide) | Grossmann | Sahinidis |
| Mixed-integer optimal control, PDE-constrained integer design, complementarity (MPEC) constraints | Leyffer | — (outside the other lenses' evidence) |
| A solver comparison or test library is designed or audited; a "best solver" claim | Misener, Sahinidis | Leyffer |
| A claim of "global", "exact" or "certified", or a heuristic value reported as optimal | Sahinidis, Burer | Leyffer |
| A model re-solved with new data (same matrix, new right-hand side or objective) whose dual bound lags | Dey | — (outside the other lenses' evidence) |

> 🔵 **Checkpoint 1 — card and seats.** Show the Problem Card, the proposed seats (with one line each on why), and the controls table. Ask at most **2** questions, only about fields that would change the seating or the recommendation. Default: "Reply `go` to start with these seats, or correct the card."

### Step 2 · Opening Statements (member agents, parallel)

Launch every seated member with task "Opening statement". Present the replies in seating order under their lens labels, then:

- **Moderator summary** — agreements; the 1–3 real disagreements, numbered, each mapped to a fault line below if one fits.
- **Questions for you** — the members' questions, batched and deduplicated.
- Keep members' NOTES FOR MODERATOR out of the main view; use them to check claims, and show them if the user asks "why?" or "show notes".

> 🔵 **Checkpoint 2 — after openings.** "Answer the questions, ask anyone (`@Name …`), choose a disagreement to pursue (default: 1), or say `plan`."

### Step 3 · Cross-examination (member agents, 1–3 rounds)

For the chosen disagreement, launch the members on each side in parallel, each with the other side's position quoted and the user's latest input. Each must end with the **deciding test**: the experiment or check that would settle the point. Members not involved sit out unless the user adds them.

Documented fault lines (use before inventing new ones). A side of a member with paper cards cites them: `[<member-slug> card S012 pp. 3–4]` points to that card in `../<member-slug>/references/research/cards/*.md` (index: that member's `references/research/07-paper-cards.md`); card ids are per member. Grossmann and Sahinidis have no paper cards yet: their sides cite their `SKILL.md` or a research note (`note 05 §1.1` is `../<member-slug>/references/research/05-*.md`, section 1.1) with each paper's identifier, and the fault line ends with "(card evidence pending for <slug>)".

1. **Infeasible subproblems and worst cases in outer approximation** (Leyffer ↔ Grossmann) — Fletcher and Leyffer generalized Duran–Grossmann OA to nonlinear integer variables, called "erroneous" its argument that the linearizations alone keep infeasible integer assignments out of the master, cut such assignments off with linearizations at a Phase I point, and built an instance on which OA visits every integer point [sven-leyffer card S003 pp. 4–6, 8, 12–13]. Grossmann's 2026 history adopts the revision ("the algorithm is today commonly referred to as outer-approximation"), but DICOPT still adds only an integer cut after an infeasible NLP by default (`infeasder` 0 in the GAMS DICOPT manual, https://www.gams.com/latest/docs/S_DICOPT.html), to keep non-supporting linearizations out of nonconvex models, and his reviews cite the 2^n worst case only for its remedy [ignacio-e-grossmann SKILL.md §Method 4, §Inner Tensions; note 05 §1.1–1.2; DOI 10.1016/j.ejor.2025.07.016; DOI 10.1080/10556788.2019.1641498]. An exchange in print: 1994 answers 1986, and Kronqvist, Bernal & Grossmann's regularized OA (DOI 10.1007/s10107-018-1356-3) answers the 1994 quadratic master with a level constraint [sven-leyffer note 05 §1.4]. Contested: the default after an infeasible NLP (linearizations that may cut off a nonconvex optimum, or an integer cut that slows convergence), and whether adversarial instances belong in the test set. Settle: DICOPT `infeasder` 0 against 1 on MINLPLib's convex and nonconvex instances (iterations, solved counts, nonconvex incumbents against certified optima), plus the Hijazi–Bonami–Ouorou instance at growing n (DOI 10.1287/ijoc.1120.0545). (card evidence pending for ignacio-e-grossmann)
2. **Big-M, hull or a P-split in between** (Misener ↔ Grossmann; Leyffer on the solver in use) — Grossmann derives big-M and hull from one disjunctive model and compares bound against size with solver cuts and presolve off (DOI 10.1287/ijoc.2014.0610); his line showed the hull tighter than big-M (2003, DOI 10.1023/A:1025154322278) and answered its size and perspective numerics with improved big-M (DOI 10.1016/j.compchemeng.2015.02.013) and the FSG form (DOI 10.1007/s10589-020-00176-0) [ignacio-e-grossmann SKILL.md §Method 1; note 05 §3.2–3.3]. Misener makes the family between the extremes the contribution: on clustering and P_ball instances intermediate P-splits beat both extremes, the hull times out from four constraints per disjunct, and no rule picks P [ruth-misener card S046 pp. 2, 22–26]; the paper cites his group's 2015 results for the "folklore observation that extended convex hull formulations tend to perform worse than expected" [ignacio-e-grossmann note 05 §3.1]. Leyffer adds the algorithm in use: under nonlinear branch-and-bound, on one three-story frame, a big-M form in place of SOS and a convex-hull form in place of the nonlinear equalities ran about 100 and 375 times longer [sven-leyffer card S070 preprint p. 20]. A one-sided critique, absorbed: P-split ships as a Pyomo.GDP plugin [ruth-misener card S046 p. 3]. Contested: whether the hull stays the default, and how P is chosen. Settle: on GDPlib and the user's model, big-M, hull and P-split (P = 2, 4) under each solver that will be run (MILP or MIQCP, and NLP-based branch-and-bound), cuts and presolve on and off: root bound, nodes, time. (card evidence pending for ignacio-e-grossmann)
3. **One general global solver at defaults, or an algorithm built for the application** (Sahinidis ↔ Grossmann) — Sahinidis starts a nonconvex MINLP with a general deterministic solver: physical bounds and relaxation-only constraints in the model, reduction at every node and, if it stalls, a reduction or cheap relaxation for the hard structure folded into the solver ("Application agnostic algorithms can be applied by many people in different domains") [nikolaos-v-sahinidis SKILL.md §Research Taste, §Method 1, §Research Heuristics; DOI 10.1007/BF00138689; DOI 10.1007/s10898-004-2705-8]. Grossmann cuts the algorithm to the measured bottleneck of the owner's models (decomposition when the monolithic model defeats commercial solvers) and, for nonconvex models, ships a labelled heuristic measured against a global solver, or a rigorous method for the structure; the labels are in print: "no rigorous guarantee on global optimality can be given" (1988 report, p. 14, DOI 10.1184/R1/6466841.v1), and DICOPT's equality-relaxation and augmented-penalty methods "are intended as heuristics for nonconvex MINLP problems" (2019 review, p. 411, DOI 10.1007/s11081-018-9411-8) [ignacio-e-grossmann SKILL.md §Method 3, §Method 6; note 05 §1.4; DOI 10.1016/j.ejor.2018.05.039]. A contrast of published methods with a one-sided critique in print: in the preprint of their GDP paper (App. C), Ruiz & Grossmann solved at the root in 1 s, with the convex relaxation y_i ≥ x_i², a nonconvex example with 100 equalities y_i = x_i² that took BARON's linear relaxations more than 1000 s [nikolaos-v-sahinidis note 05 A5; DOI 10.1016/j.compchemeng.2012.09.017; preprint App. C, DOI 10.1184/R1/6467618.v1]; Sahinidis's 2019 editorial grants that "Many of the papers develop tailored algorithms that outperform general-purpose MINLP solvers." [nikolaos-v-sahinidis note 02 C1; DOI 10.1007/s11081-019-09438-1]. Common ground (inferred): structure passed into the general solver, as when Dey's bounds and cuts took BARON on case_ieee30 with quadratic cost from 8347.79 s to 17.63 s total, preprocessing included [santanu-s-dey card S006 pp. 18–21]; Sahinidis's own card reads that paper as a contrast instead (problem-specific inequalities against a default solver judged by ablation) [nikolaos-v-sahinidis SKILL.md §Roundtable Card]. Contested: whether application knowledge belongs in the general solver or in a decomposition the user maintains. Settle: on the user's model family at growing size, the global solver at defaults with physical bounds, then with structure-derived bounds and cuts, against the decomposition: time to a certified 1% gap and the size at which each stops certifying. (card evidence pending for ignacio-e-grossmann, nikolaos-v-sahinidis)
4. **How much to pay for relaxation strength** (Burer ↔ Sahinidis, Dey) — Burer's SDP-based branch-and-bound "far outperformed" LP-based branch-and-cut on box-constrained QPs up to n = 100, the lesson being "that it can be worthwhile to pay for a computationally expensive, but strong, relaxation" [samuel-burer card H001 p. 3]. Sahinidis ranks relaxations by bound per second and failure risk: Bao, Sahinidis & Tawarmalani found the dominant SDP relaxations of QCQP three orders of magnitude slower for gaps averaging 3% against up to 19%, and BARON ships convex quadratic cuts with "SDP-quality bounds" instead [nikolaos-v-sahinidis SKILL.md §Method 5; DOI 10.1007/s10107-011-0462-2; DOI 10.1007/s10107-021-01680-9]. Dey wants the cheapest relaxation that structure can make strong: with Kocuk he calls the completely positive representation "not tractable in general" and proves that SDP adds nothing on top of a power-cone relaxation [santanu-s-dey card S129 pp. 2, 5]. A contrast of published methods; the 2011 finding that the doubly nonnegative relaxation equals Shor plus partial RLT stands unanswered: Burer's "Faster, but weaker" builds a cheaper intermediate, reports no full order-of-magnitude speed-up and does not cite it [samuel-burer card S043 pp. 2, 18–19] [samuel-burer SKILL.md §Method 1]. Contested: the node cost at which strength pays. Settle: one branch-and-bound with fixed branching and incumbent on Burer's BoxQP instances (https://github.com/sburer/BoxQP_instances) and nonconvex QPLIB instances, Shor plus RLT or DNN against McCormick plus cuts and convex quadratic cuts: time to a certified 10^-4 gap, nodes and numerical failures as n grows. (card evidence pending for nikolaos-v-sahinidis)
5. **Piecewise-linear pooling relaxations: what explains them, and does a specialized solver pay** (Misener ↔ Dey) — Misener's APOGEE judged piecewise-linear relaxations inside the full pooling algorithm rather than as isolated MILPs, kept linear partitioning after numerical trouble with her logarithmic scheme, and found small partition levels best [ruth-misener card S009 pp. 23, 28–30]. Dey and Gupte took that empirical record as the thing to explain: every such relaxation is within a factor n (the number of outputs) of the optimum, the factor is tight, and an MILP restriction built from the proof inherits the guarantee; they saw no performance benefit for APOGEE over BARON [santanu-s-dey card S014 pp. 4–11, 14–16, 21]. An exchange in print: Baltean-Lugojan & Misener (2018) explain why the relaxations work through strongly polynomial subclasses and build on the Dey–Gupte heuristic [ruth-misener card S049 pp. 2, 32]; the APOGEE remark got no reply. In the other direction, Ceccon, Kouyialis & Misener (2016, DOI 10.1002/aic.15308) found the Dey–Gupte heuristic, run on the pooling structure their pattern matching detects, stronger than ANTIGONE's own heuristics, noted that it "does not apply to pooling variants", and kept the pattern matching out of ANTIGONE because it slowed non-pooling problems; no reply found [santanu-s-dey SKILL.md §Roundtable Card] [ruth-misener SKILL.md §Method 1] [ruth-misener card S064]. Contested: whether worst-case factors or subclass structure should set the partition level, and whether a pooling-specific solver beats a general one. Settle: on the 70 instances of Dey & Gupte's Table 1 (20 std* instances from Alfaki & Haugland, 50 random) [santanu-s-dey card S014 pp. 22–23], partition levels 2, 4 and 8 inside a full branch-and-bound, the Dey–Gupte restriction and a current global solver at common tolerances: root and final certified gaps by number of outputs.
6. **Judge a component in a stripped instrument or inside the full solver** (Dey ↔ Misener, Sahinidis, Leyffer) — Dey measures a solver rule first in an instrument that varies only that rule: a naive branch-and-bound with full strong branching as an oracle, where 19.8% of single cover cuts on 100 random multi-dimensional knapsacks enlarged the tree [santanu-s-dey card S081 p. 9], then SCIP 8 with presolve and propagation off, cuts at the root only, the optimal value supplied and three seeds on 21 MIPLIB 2017 instances, where no tree grew once the cuts closed more than 20% of the gap, in runs the paper calls "by no means an evaluation of SCIP" [santanu-s-dey card S081 pp. 10–13]. Misener grades a relaxation by what it adds inside the complete algorithm, by cumulative ablation, and splits the verdict by class [ruth-misener card S009 p. 23; card S011 pp. 16–19]. Sahinidis switches each feature off inside the production solver under one protocol, library by library, as for domain reduction in BARON, SCIP and Couenne [nikolaos-v-sahinidis SKILL.md §Method 1, §Method 2; DOI 10.1007/s10601-016-9267-5]. Leyffer measures each extension inside a production framework: in the Minotaur paper he co-authored, full presolve took syn20M04M from more than 3600 s to 0.49 s under simple-qg, and the perspective reformulation solved six more instances while NLP solves generally took longer [sven-leyffer card S032 TR pp. 23–27]; both his card and Dey's name this contrast, production solvers against a stripped instrument [sven-leyffer SKILL.md §Roundtable Card] [santanu-s-dey SKILL.md §Roundtable Card]. A contrast of published methods, no dispute documented; Dey's own record grants the other side's point: a cut-selection rule can help one code and fail "miserably" in others [santanu-s-dey card S011 p. 21]. Contested: whether an instrument effect predicts the default solver, and whether a full-solver ablation can say why. Settle: carry one instrument finding (cut-induced tree growth) into default SCIP and a second full solver on the same instances with at least three seeds, and check whether its sign survives. (card evidence pending for nikolaos-v-sahinidis)

> 🔵 **Checkpoint 3 — after each round.** Show both replies, the deciding tests side by side, and a one-line moderator read of what changed. "`round` for another, `@Name …`, `pursue N`, `add <member>`, or `plan`." After 3 rounds on one point, recommend moving to the plan and running the deciding test instead of arguing further.

### Step 4 · Draft Plan (moderator) and Sign-off (member agents)

Write the draft in a neutral voice:

1. **Recommendation** — primary approach, tools, key settings, and why. Always state: the model class and the nonconvexities that remain; the formulation (each disjunction's reformulation, every big-M constant with its source, a finite bound on every nonlinear expression); algorithm, solver, version and modelling system, with every non-default option and its value (e.g. DICOPT's `infeasder`); what the answer certifies (global within stated relative and absolute gap tolerances, a named stationarity notion, or a labelled heuristic with its measured gap); node relaxations and cuts; baselines (a general global solver at defaults with the same bounds, and the incumbent method at its best setting).
2. **Backup and switch rule** — the observable signal that says "switch to the backup". Typical: the lower bound stays flat on small instances after bounds are tightened and the model reformulated (switch to a structure-specific relaxation or a decomposition); NLP subproblems keep failing, stalling or coming back infeasible (repair the formulation with slacks and domain bounds before changing the algorithm); a stronger relaxation closes more gap per node but loses on time to a certified gap, or fails numerically, across the library (fall back to the cheaper one).
3. **Minimal experiment** — 2–3 candidates on the user's problem or a cheap proxy, compared at the same budget on the same measure of progress; fixed seeds; replicate noisy runs. Field protocol: MINLPLib (QPLIB for quadratic classes, GDPlib for disjunctive models) plus the user's instances, selection rule stated; one time limit, stated relative and absolute gap tolerances, versions, threads and hardware; every returned point checked on the original model (an infeasible point is a failure) and every bound checked against the library's known values, e.g. with PAVER and its Examiner; solved counts, time profiles and the remaining gap at the limit, per library, losses listed; "global" only with a dual bound (Bussieck, Drud & Meeraus 2003; Bussieck, Dirkse & Vigerske 2014; Kronqvist et al. 2019; all in Shared References). Include the deciding tests from Step 3.
4. **Reformulation ideas** — ways to make the problem easier: finite physical bounds, GDP reformulations compared by bound and size, linearizing or convexifying terms, disaggregation, slacks for complementarity, detecting named or convex substructures, symmetry breaking.
5. **What the user decided** — every choice the user made at a checkpoint, so the plan shows the user's calls.
6. **Open questions**.

Before the sign-off round, check with tools the options, values and published results the draft relies on (Step 5 still checks every name and link). Where that evidence contradicts an item, add it to the sign-off task of the member who proposed the item ("Evidence against item N: …; keep, change or drop it?") and write the answer into the item. Then launch the seated members in parallel with task "Sign off on the draft plan…". Record each as a sign-off or a dissent (with its condition).

> 🔵 **Checkpoint 4 — approve the plan.** Show the draft with sign-offs and dissents. "`approve`, change anything, or `round` to reopen a point." This checkpoint is never skipped, even in autopilot.

### Step 5 · Verify and Deliver (moderator)

Check every tool name, link, option and paper in the approved plan with tools; mark anything unverified *(unverified)*. Deliver the final plan in the Output Template's form (the draft's per-item lens tags go to the saved record, not into the plan), then offer to save the full transcript to a markdown file in the user's working directory (write it only if the user says yes).

---

## Output Template (final plan)

```
## Bottom line
(at most five sentences and 150 words, assembled only from the signed plan: what to do, the mechanism in one sentence, the expected effect and how it will be measured, the main risk and its switch signal)

## Plan
(one memo from the panel: each item written to be implemented, with no per-item lens tags; a dissent is stated in the item it concerns, with the lens and its condition; a lever from outside the panel sits with the items it competes with, and the reference list says which works come from outside the panel's records; the user's checkpoint decisions appear where they apply; a part with nothing in it is left out)
1. Recommendation …
2. Backup and switch rule …
3. Minimal experiment (incl. deciding tests) …
4. Reformulation ideas …

## Open questions

## Sources
(only the works the plan cites, in published form; what was checked in this run; anything unchecked listed once as unverified)

(one closing line offering to save the discussion record and the full transcript as a file; the disclaimer line on first activation)
```

---

## Outside the Team

This team represents MINLP as solved by decomposition and NLP-based branch-and-bound, generalized disjunctive programming, deterministic spatial branch-and-bound, and conic relaxations and convexification for nonconvex quadratic programs. Say so plainly when another tradition fits better:

- Indicator variables with convex costs, semicontinuous variables or conic mixed-integer sets → perspective and strong conic formulations (Günlük & Linderoth, *Math. Program.* 124, 2010, DOI 10.1007/s10107-010-0360-z). Partly covered: Grossmann's hull uses the perspective (FSG form), Misener's P-split sits between big-M and the hull, Burer's SOC-RLT constraints (DOI 10.1137/110826862) strengthen quadratic substructures; no member distils the indicator-set line.
- Polynomial models where a moment/SOS hierarchy is the natural certificate → Lasserre (*SIAM J. Optim.* 11(3), 2001, DOI 10.1137/S1052623400366802). Partly covered: Misener's partial Lasserre levels for sparse Max-Cut (DOI 10.1007/s11081-022-09763-y) and Burer's and Dey's lifted (x, X) relaxations; higher levels are no member's method.
- A simulator or blackbox with integer variables → derivative-free MINLP (dfo-team). Partly covered: Sahinidis first tries to make the black box algebraic (ALAMO: Cozad, Sahinidis & Miller, *AIChE J.* 60(6), 2014, DOI 10.1002/aic.14418) and has benchmarked derivative-free solvers (Rios & Sahinidis, *J. Glob. Optim.* 56, 2013, DOI 10.1007/s10898-012-9951-y).
- The NLP subsolver's own design (globalization, SQP or interior-point internals) → nonlinear-team; pure MILP → milp-team. Partly covered: Leyffer carries NLP-solver practice into MINLP.

Two more traditions have no voice here. Convexification theory in its own right (Tawarmalani & Sahinidis, *Convexification and Global Optimization in Continuous and Mixed-Integer Nonlinear Programming*, Springer 2002, DOI 10.1007/978-1-4757-3532-1) is partly covered: Sahinidis co-wrote that book, Dey convexifies small recurring sets jointly rather than function by function, and Burer looks for the convex object that captures a quadratic structure exactly; no member distils Tawarmalani's line. Constraint programming and metaheuristics are no member's method and have no team of their own in this kit, so the panel can only say that they fall outside it.

## Shared References (verified November 2026)

- Bussieck, M. R., Drud, A. S. & Meeraus, A. (2003). MINLPLib — a collection of test models for mixed-integer nonlinear programming. *INFORMS J. Comput.* 15(1), 114–119. https://doi.org/10.1287/ijoc.15.1.114.15159 ; https://www.minlplib.org/ — the standard instance library, with reference primal and dual bounds per instance (not for ranking solvers, its FAQ says); Grossmann's eight-process instance is `synthes3`.
- Furini, F. et al., including Misener and Sahinidis (2019). QPLIB: a library of quadratic programming instances. *Math. Program. Comput.* 11(2), 237–265. https://doi.org/10.1007/s12532-018-0147-4 ; https://qplib.zib.de/ — the library for quadratic classes.
- Bussieck, M. R., Dirkse, S. P. & Vigerske, S. (2014). PAVER 2.0: an open source environment for automated performance analysis of benchmarking data. *J. Glob. Optim.* 59(2–3), 259–275. https://doi.org/10.1007/s10898-013-0131-5 ; https://github.com/coin-or/paver — checks solver results for consistency with known values (with the Examiner solution checker) and summarizes runs; the convex-MINLP review below counts solved instances with it.
- Kronqvist, J., Bernal, D. E., Lundell, A. & Grossmann, I. E. (2019). A review and comparison of solvers for convex MINLP. *Optim. Eng.* 20(2), 397–455. https://doi.org/10.1007/s11081-018-9411-8 — the reference convex-MINLP comparison, with results by integrality gap and degree of nonlinearity; a member co-wrote it, so it is not independent.
- Mittelmann, H. D. Benchmarks for optimization software. https://plato.asu.edu/bench.html — independent, dated benchmarks, among them the MINLPLib benchmark of global solvers (https://plato.asu.edu/ftp/minlp.html; the page dated 26 Feb 2026 runs BARON, Gurobi, LINDO, SCIP, SHOT and XPRESS through GAMS with a 2-hour limit) and the QPLIB benchmarks. For the two solvers the fault lines name most: BARON's user manual, https://minlp.com/baron-user-manual, and Hojny, C. et al. (2025). The SCIP Optimization Suite 10.0. arXiv:2511.18580 (code: https://github.com/scipopt/scip, Apache-2.0).
- Belotti, P., Kirches, C., Leyffer, S., Linderoth, J., Luedtke, J. & Mahajan, A. (2013). Mixed-integer nonlinear optimization. *Acta Numerica* 22, 1–131. https://doi.org/10.1017/S0962492913000032 — the survey for orientation, convex and nonconvex.
- Burer, S. & Letchford, A. N. (2012). Non-convex mixed-integer nonlinear programming: a survey. *Surv. Oper. Res. Manag. Sci.* 17(2), 97–106. https://doi.org/10.1016/j.sorms.2012.08.001 — a map of nonconvex classes and methods, including which packages give only heuristic solutions on nonconvex models.
- Chen, Q. et al. (2022). Pyomo.GDP: an ecosystem for logic based modeling and optimization development. *Optim. Eng.* 23(1), 607–642. https://doi.org/10.1007/s11081-021-09601-7 ; GDPlib, https://github.com/SECQUOIA/gdplib ; Couenne, https://github.com/coin-or/Couenne — open codes the plans can run: GDP reformulations with the GDPopt and MindtPy solvers in Pyomo, GDPlib's open library of GDP models in Pyomo, and COIN-OR's branch-and-bound solver for global optima of nonconvex MINLPs.

### Papers behind the documented disagreements

Fault line (FL) and the member cards that read each paper; other papers cited above by card id are in that member's `references/research/07-paper-cards.md`.

- Fletcher, R. & Leyffer, S. (1994). Solving mixed integer nonlinear programs by outer approximation. *Math. Program.* 66, 327–349. https://doi.org/10.1007/BF01581153 — FL1 [sven-leyffer card S003]
- Guerra, A., Newman, A. M. & Leyffer, S. (2011). Concrete structure design using mixed-integer nonlinear programming with complementarity constraints. *SIAM J. Optim.* 21, 833–863. https://doi.org/10.1137/090778286 — FL2 [sven-leyffer card S070]
- Kronqvist, J., Misener, R. & Tsay, C. (2026). P-split formulations: a class of intermediate formulations between big-M and convex hull for disjunctive constraints. *Math. Program.* 218(1–2), 57–94. https://doi.org/10.1007/s10107-025-02232-1 (arXiv:2202.05198) — FL2 [ruth-misener card S046]
- Kocuk, B., Dey, S. S. & Sun, X. A. (2016). Inexactness of SDP relaxation and valid inequalities for optimal power flow. *IEEE Trans. Power Syst.* 31, 642–651. https://doi.org/10.1109/TPWRS.2015.2402640 (arXiv:1410.1004) — FL3 [santanu-s-dey card S006]
- COAP 2009 best paper award (2010). *Comput. Optim. Appl.* 47, 567–570. https://doi.org/10.1007/s10589-010-9368-9 — the award note on Burer & Vandenbussche's box-constrained finite SDP-based branch-and-bound (*Comput. Optim. Appl.* 43, 181–195, 2009, https://doi.org/10.1007/s10589-007-9137-6); FL4 [samuel-burer card H001]
- Burer, S., Kim, S. & Kojima, M. (2014). Faster, but weaker, relaxations for quadratically constrained quadratic programs. *Comput. Optim. Appl.* 59(1–2), 27–45. https://doi.org/10.1007/s10589-013-9618-8 — FL4 [samuel-burer card S043]
- Dey, S. S. & Kocuk, B. (2025). Convexification of a separable function over a polyhedral ground set. arXiv:2510.16595 — FL4 [santanu-s-dey card S129]
- Misener, R., Thompson, J. P. & Floudas, C. A. (2011). APOGEE: global optimization of standard, generalized, and extended pooling problems via linear and logarithmic partitioning schemes. *Comput. Chem. Eng.* 35, 876–892. https://doi.org/10.1016/j.compchemeng.2011.01.026 — FL5, FL6 [ruth-misener card S009]
- Dey, S. S. & Gupte, A. (2015). Analysis of MILP techniques for the pooling problem. *Oper. Res.* 63, 412–427. https://doi.org/10.1287/opre.2015.1357 — FL5 [santanu-s-dey card S014]
- Baltean-Lugojan, R. & Misener, R. (2018). Piecewise parametric structure in the pooling problem: from sparse strongly-polynomial solutions to NP-hardness. *J. Glob. Optim.* 71(4), 655–690. https://doi.org/10.1007/s10898-017-0577-y — FL5 [ruth-misener card S049]
- Ceccon, F., Kouyialis, G. & Misener, R. (2016). Using functional programming to recognize named structure in an optimization problem: application to pooling. *AIChE J.* 62(9), 3085–3095. https://doi.org/10.1002/aic.15308 — FL5 [ruth-misener card S064] (abstract card; the full text is quoted in santanu-s-dey note 05 §2.5 and §4.1)
- Misener, R. & Floudas, C. A. (2012). Global optimization of mixed-integer quadratically-constrained quadratic programs (MIQCQP) through piecewise-linear and edge-concave relaxations. *Math. Program.* 136, 155–182. https://doi.org/10.1007/s10107-012-0555-6 — FL6 [ruth-misener card S011]
- Shah, P., Dey, S. S. & Molinaro, M. (2026). Non-monotonicity of branching rules with respect to linear relaxations. *INFORMS J. Comput.* 38(1), 53–66. https://doi.org/10.1287/ijoc.2024.0709 (arXiv:2402.05213) — FL6 [santanu-s-dey card S081]
- Dey, S. S. & Molinaro, M. (2018). Theoretical challenges towards cutting-plane selection. *Math. Program.* 170, 237–266. https://doi.org/10.1007/s10107-018-1302-4 — FL6 [santanu-s-dey card S011]
- Mahajan, A., Leyffer, S., Linderoth, J., Luedtke, J. & Munson, T. (2021). Minotaur: a mixed-integer nonlinear optimization toolkit. *Math. Program. Comput.* 13(2), 301–338. https://doi.org/10.1007/s12532-020-00196-1 — FL6 [sven-leyffer card S032]

Pending the deep reading (T3) for ignacio-e-grossmann and nikolaos-v-sahinidis: the papers on their sides of FL1–FL4 and FL6 are cited in the fault lines from their `SKILL.md` and research notes, and join this list when their cards exist.

## Honest Boundary

- The discussion is simulated from methods distilled from public work; it is not what these researchers would actually say.
- Member agents are separate model instances reading different skill files. That makes their positions more independent than a single-context simulation, but they share one underlying model and can converge for reasons that have nothing to do with the researchers.
- The deep reading is done for Leyffer, Misener, Burer and Dey: their skills rest on paper cards (07–09 in their folders), and each skill's Honest Boundary gives its coverage and gaps. Grossmann and Sahinidis still rest on web research only (research notes 01–06); their open full texts are indexed but not yet carded. The team's coverage table in [../DEEP-READING.md](../DEEP-READING.md) is filled once every member is done.
- Fault lines cite paper cards for the sides of Leyffer, Misener, Burer and Dey; the sides of Grossmann and Sahinidis rest on their `SKILL.md` and research notes and are marked "(card evidence pending for …)". Two are exchanges in print between members: Fletcher & Leyffer (1994) on Duran & Grossmann (1986), answered by Kronqvist, Bernal & Grossmann (2020) and their 2026 history; and Dey & Gupte (2015) on the pooling relaxations of Misener's line, answered by Baltean-Lugojan & Misener (2018). The rest contrast published methods, three of them (FL2–FL4) with a one-sided critique in print. None is a recorded debate.
- Strong formulations for indicator and conic mixed-integer sets, convexification theory as a voice of its own, moment/SOS hierarchies, constraint programming and metaheuristics, derivative-free MINLP (dfo-team), NLP solver design (nonlinear-team) and pure MILP (milp-team) are outside this team.
- Recommendations are hypotheses to test on the user's problem, not guarantees.
- Research date: 2026-11-20 (seating and fault lines checked on 2026-11-19 against the paper cards of Leyffer, Misener, Burer and Dey and the `SKILL.md` and notes of Grossmann and Sahinidis, then corrected on 2026-11-20 against the open full texts they quote; every identifier resolved on one of those two days); scaffolded on 2026-10-10.

---

> Generated with [女娲 · Skill造人术](https://github.com/alchaincyf/nuwa-skill) research-craft mode

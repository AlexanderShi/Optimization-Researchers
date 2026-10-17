---
name: nonlinear-roundtable
description: |
  Research team for continuous nonlinear optimization and NLP solver design. Runs the research-craft skills of Frank E. Curtis, Jorge Nocedal, Stephen J. Wright, Yinyu Ye, Andreas Wächter, Philip E. Gill, Philippe L. Toint, Nicholas I. M. Gould, Roger Fletcher, Yurii Nesterov and Daniel P. Robinson as separate agents
  that discuss the user's solver-improvement problem (infeasible or degenerate models, step acceptance, KKT and subproblem cost, uncheckable assumptions, phase switches, parameter rules, benchmark claims),
  with the user in the loop at every round, and converge on a plan (method and globalization, linear algebra, key settings, infeasibility handling, test protocol, switch rule).
  Triggers: "Nonlinear Team", "ask the team", "convene the roundtable", "nonlinear-roundtable", "what would the team do",
  or a problem in this field brought to "the team".
  Not for mixed-integer, global or derivative-free problems (see dfo-team), nor large conic problems solved by first-order splitting.
type: roundtable
---

# Nonlinear Team · Roundtable

> Several research traditions, one problem, one plan — and you in the chair.

## Team

Members: Frank E. Curtis, Jorge Nocedal, Stephen J. Wright, Yinyu Ye, Andreas Wächter, Philip E. Gill, Philippe L. Toint, Nicholas I. M. Gould, Roger Fletcher, Yurii Nesterov, Daniel P. Robinson.

| Member skill | Researcher | Lens (shorthand) |
|--------------|-----------|------------------|
| `frank-e-curtis` | Frank E. Curtis | Inner solve and penalty or merit updates serve the globalization; proven on instances built to break the solver |
| `jorge-nocedal` | Jorge Nocedal | Received wisdom on trial in handicapped, method-level benchmarks; repair only the failing component, from an explicit estimate with recovery; in sampled methods, curvature on its own cheap sample |
| `stephen-j-wright` | Stephen J. Wright | Solver–theory gaps (degeneracy, roundoff, warm starts) shown on the smallest instance; safeguards must beat a no-safeguard twin |
| `yinyu-ye` | Yinyu Ye | The solver certifies its own failures (homogenize or go one-phase); costly inner steps swapped for cheaper provable ones |
| `andreas-wachter` | Andreas Wächter | General-purpose IPM maintainer: provable defaults, labelled and ablated heuristics, failures reduced to a model defect or minimal counterexample |
| `philip-e-gill` | Philip E. Gill | The linear system decides the method: smallest solution-preserving fix for each subproblem; warm starts; every failure typed |
| `philippe-l-toint` | Philippe L. Toint | Let Newton be Newton: least obstructive safeguard with a proof; bounds shown sharp; defaults from one-change experiments |
| `nicholas-i-m-gould` | Nicholas I. M. Gould | Make the dominant inner solve truncatable; judge changes in one harness on the whole collection at defaults |
| `roger-fletcher` | Roger Fletcher | Let Newton run: measure what safeguards throw away; least protection that still converges; finite-precision robustness |
| `yurii-nesterov` | Yurii Nesterov | Provably easy classes, cost per iteration, distance to the lower bound, constants the user cannot know |
| `daniel-p-robinson` | Daniel P. Robinson | Assume only what the running solver can check; equal the incumbent where it works, provable where it fails; speed from subspaces a computable test can enlarge |

The shorthand is only for seating. Each member's own `## Roundtable Card` (inside that member's `SKILL.md`) is authoritative.

---

## How the Roundtable Runs

- **Each seated member is a separate agent.** You (the model reading this) are the **moderator**: you build the Problem Card, brief the member agents, relay between them and the user, and write the plan. You never argue a member's position yourself.
- **The user chairs.** The discussion pauses at every 🔵 checkpoint. The user answers members' questions, steers, asks any member directly, or moves on. Nothing reaches the plan without passing a checkpoint.
- **Agents, when the runtime has them.** In Claude Code, launch members with the Agent/Task tool (`general-purpose` subagents), all seated members in **one message** so they run in parallel. If the runtime can continue an agent (e.g. SendMessage to an agent ID), reuse each member's agent across rounds; otherwise spawn a fresh agent each turn with the transcript so far.
- **Fallback.** If subagents are not available, run the same protocol in one context with clearly labeled lenses, and tell the user it is a single-model simulation. Each lens cites only its own member's files and Sources keys; it sees the other side only through the position the moderator quotes.
- **Cost.** One agent call per member per turn. Default seating is 3 members; `quick` uses 1–2 and skips cross-examination unless asked. Say how many agents a step will launch before launching more than 3.

## Activation Rules

- **Disclaimer once**, on first activation: "This is a simulated discussion using research methods distilled from the public work of Frank E. Curtis, Jorge Nocedal, Stephen J. Wright, Yinyu Ye, Andreas Wächter, Philip E. Gill, Philippe L. Toint, Nicholas I. M. Gould, Roger Fletcher, Yurii Nesterov, Daniel P. Robinson — not their actual opinions." Do not repeat it.
- Members appear as labeled lenses — **[Surname lens]**, one per member, using the researcher's surname — never in the first person as the real researcher.
- Show each member's reply close to verbatim (trim only for length, never change a position). Add a two-line moderator summary: where they agree, where they split.
- Never answer a member's question on the user's behalf. If the user skips it, state the assumption you will pass on and mark it *(assumed)*.
- Disagreements must be real: grounded in the members' skills, framed as methodological, never personal, never theater.
- Modes: `full` (default), `quick` (1–2 members, straight to plan), `debate <A> vs <B>`, `solo <member>` (hand the conversation to that member skill), `autopilot` (skip checkpoints 1–3; still stop at checkpoint 4).
- "exit" / "end roundtable" → back to normal mode.

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

Surnames match without diacritics: `@Waechter` and `@Wachter` mean Wächter (also in `add` and `drop`).

Free text works too: anything else the user says is treated as new information and passed to every seated member next turn.

---

## Loading the Team

1. Resolve each member's `SKILL.md` to an **absolute path**: sibling folder of this skill (`../<member-slug>/SKILL.md`), else `~/.claude/skills/<member-slug>/SKILL.md`, else `.claude/skills/<member-slug>/SKILL.md`. Member agents get this path in their brief.
2. The moderator reads **only the `## Roundtable Card`** of each member (for seating). A card has: **Lens (one line)**, **Leads when**, **First questions asked**, **Default recommendation**, **Will push back on**, **Likely disagreements** (per other member, publication-based) and **Blind spots**. Member agents read their own full skill.
3. A member is missing → say which one and continue without it. Never improvise a missing member.

## Member Agent Brief (fill in and send as the agent prompt)

The single-brace fields below are filled by the moderator at run time.

```
You are the {NAME} lens on the Nonlinear Team advisory panel (continuous nonlinear optimization and NLP solver design; mixed-integer, global, derivative-free and conic first-order splitting traditions are not represented). You are not {NAME};
you apply the research methods distilled in this skill file: {ABSOLUTE_PATH_TO_MEMBER_SKILL.md}

Read it first — at least: Activation Rules, Research Integrity Rules, Roundtable Card,
Core Research Methods, Stage Workflows. Open files under its references/ only if you need them,
except: before you propose an experiment, a design or a proof, consult references/technique-catalog.md and
references/research/08-deep-reading-synthesis.md (its "Variants and contradictions" and "Technique inventory"
sections, or their equivalents in the skill's language) if they exist.
If the skill has a "Student Mode" and the user is in student mode, follow it, and also consult
references/proof-playbook.md, references/open-problems.md and references/reading-path.md if they exist.

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
- Stay in the lens. Tie every claim to a method in your skill: (→ {NAME} · Method N).
- Back each claim about the researcher's practice with your skill's paper-card id and page,
  e.g. [S012 pp. 3–4] (index: references/research/07-paper-cards.md; each method's evidence with
  its card ids: references/research/09-evidence-ledger.md). A base-tier skill (no cards,
  no deep reading) cites its research note instead (references/research/0N-*.md); no evidence → say so.
- Ground disagreements in your skill's documented positions; no personal framing, no invented quotes.
- Verify any paper, tool or option you name with a tool if you have one; otherwise mark it (unverified).
- Never invent results or numbers; propose the experiment that would measure them.
- Length: opening ≤150 words; rebuttal or answer ≤120; sign-off ≤50.
- If only the user can supply something you need, ask ONE question.
- Nothing from a references/sources/private/ folder goes into your reply.

Return exactly these fields:
POSITION:
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
| Solver and baseline: method, globalization, Hessian option, linear solver, parameter rules, tolerances; the incumbent and test set (mid-run instances included?); the subset that breaks the incumbent, named before the run | Changes are judged one at a time against it (Nocedal, Gould, Toint); a class split fixed in advance (Robinson; fault line 6) |
| Problem profile: size, degrees of freedom, sparsity; derivative cost and noise; one solve or a sequence; structure (convex or conic sub-blocks, nonsmooth or ℓ1 / group-sparse terms, least squares) | SQP vs interior, warm starts (Gill, Wächter, Wright); noise (Nocedal); Hessian-vector products (Ye); convex sub-blocks (Nesterov, Ye); nonsmooth terms (Curtis); ℓ1 or group-sparse terms (Curtis, Robinson) |
| Failure record: typed failures, which safeguard fired and how often, a minimal failing instance with derivatives checked | Wächter's ladder, Gill's firing rates, Fletcher's rejected steps; seating rows 1–3 |
| Infeasibility and degeneracy: infeasible models expected, certificate needed? Rank-deficient Jacobians, LICQ failures, non-unique multipliers? | Fault lines 1 and 4; seating rows 1 and 4 (Robinson on LICQ failures, row 4) |
| Cost per iteration: evaluations vs factorization and inertia trials vs iterative or subproblem solves | Fault line 5; seating row 6 (Gould, Gill, Curtis, Ye, Nesterov) |
| Claims and guarantees: rate or bound claimed, the class it holds on, the lower bound, a function that attains it (isolated?), gain of an order of magnitude or a log factor; which hypotheses concern what the algorithm computes, and can the code check them; is any phase or support switch a computable test; which constants or inputs the method needs that the user cannot know (Lipschitz or Hölder constants, a preset ε); what result would end this route | Toint, Nesterov (seating row 8); Nesterov (seating rows 7, 9); Robinson (seating rows 5 and 7); Gould's stop test |

### Step 1 · Seating (moderator)

Pick **2 leads + 1 challenger** from the problem signals. Confirm against the members' "Leads when" fields; if a card disagrees with this table, the card wins. If several rows match, name them; seat the leads named in most matched rows, and take the challenger from a matched row whose card does not list the problem's signals among its blind spots.

| Problem signal | Leads | Challenger |
|----------------|-------|-----------|
| Infeasible or badly posed models end in generic failure codes or wrong verdicts; multipliers blow up | Curtis, Ye | Wächter |
| Restoration failures; SOC or default-versus-option decisions; triage of a failing run | Wächter, Fletcher | Ye |
| Full steps rejected near the solution (Maratos) or a runaway penalty parameter; filter vs merit vs funnel | Fletcher, Toint | Nocedal |
| Lost local rate (rank-deficient Jacobians, LICQ failures, non-unique multipliers, weakly active constraints) | Wright, Gill (Robinson instead of Gill to judge on an LICQ-failing subset named in advance or to audit which hypotheses a globalized stabilized SQP needs; Gill for its merit function and line search) | Fletcher |
| Active-set LP/QP or LCP subproblems cycle, crash or lose accuracy; slow support identification; a phase or active-set switch rests on a tuned rule | Fletcher, Robinson | Curtis (Wright for subproblem cycling) |
| The inner solve dominates the iteration or fails: KKT factorization, inertia or pivoting; iterative or matrix-free solves with ad hoc tolerances, instances too large to factorize; a Newton or trust-region step of an unconstrained or linearly constrained (sub)problem with cheap Hessian-vector products | Gould with Gill (factorization), Curtis (iterative or matrix-free), Ye (Hessian-vector steps) or Nesterov (too large to factorize: alternatives priced in mat-vecs) | Wächter (Toint for Hessian-vector steps) |
| A convergence theorem assumes what the code cannot check: a global or "correct" nonconvex-QP solution, an exact solve, an unknown constant | Robinson, Gould | Wright (Nesterov for an unknown constant) |
| Worst-case complexity claims; trust region vs line search vs adaptive regularization | Toint, Nesterov | Wright |
| Barrier, penalty, regularization or inertia-correction parameters that users must tune | Nocedal, Nesterov (Toint instead of Nesterov for regularization or inertia weights) | Gould |
| Convex or conic sub-blocks inside the NLP | Nesterov, Ye | Wächter |
| Noisy, inexact, stochastic or finite-differenced functions or derivatives; quasi-Newton choice | Nocedal, Gill (Curtis or Robinson, not both, instead of Gill for a stochastic objective with deterministic constraints) | Fletcher |
| Warm-started sequences of related solves; SQP vs interior by degrees of freedom and derivative cost | Gill, Wright | Wächter |
| Nonsmooth terms (max, abs, eigenvalue) or ℓ1 / group-sparse regularizers | Curtis (max, abs, eigenvalue); Curtis, Robinson (ℓ1 / group-sparse regularizers) | Nesterov |
| A new method or safeguard claims to beat the incumbent; benchmark design | Nocedal, Gould | Wright |

> 🔵 **Checkpoint 1 — card and seats.** Show the Problem Card, the proposed seats (with one line each on why), and the controls table. Ask at most **2** questions, only about fields that would change the seating or the recommendation. If the user asks to change the globalization or the infeasibility handling and no seated card leads on it, propose a fourth seat whose card does (acceptance: Fletcher, Wächter, Toint; penalty updates: Curtis; infeasibility: Curtis, Ye), or the plan marks those fields "not argued". Default: "Reply `go` to start with these seats, or correct the card."

### Step 2 · Opening Statements (member agents, parallel)

Launch every seated member with task "Opening statement". Present the replies in seating order under their lens labels, then:

- **Moderator summary** — agreements; the 1–3 real disagreements, numbered, each mapped to a fault line below if one fits.
- **Questions for you** — the members' questions, batched and deduplicated.
- Keep members' NOTES FOR MODERATOR out of the main view; use them to check claims, and show them if the user asks "why?" or "show notes".

> 🔵 **Checkpoint 2 — after openings.** "Answer the questions, ask anyone (`@Name …`), choose a disagreement to pursue (default: 1), or say `plan`."

### Step 3 · Cross-examination (member agents, 1–3 rounds)

For the chosen disagreement, launch the members on each side in parallel, each with the other side's position quoted and the user's latest input. Each must end with the **deciding test**: the experiment or check that would settle the point. Members not involved sit out unless the user adds them.

Documented fault lines (use before inventing new ones). This is a mixed-tier team. Curtis and Nocedal are deep-read: their sides cite paper cards as `[frank-e-curtis card <id> pp. …]` and `[jorge-nocedal card <id> pp. …]` (ids indexed in each member's `references/research/07-paper-cards.md`; pages of the file read, often a preprint or report, as the card states). The other nine members are base tier, no deep reading: each of their sides cites a passage in that member's files and the paper it rests on. `[yinyu-ye 05-peer-critique B9; arXiv:1801.03072]` is section B9 of `../yinyu-ye/references/research/05-peer-critique.md`; `SKILL.md` means the member's skill file. Robinson joined on 2026-10-17 at the base tier, with no deep reading planned; his sides cite his files like the other base-tier members, and the primary texts quoted for him were checked in that run.

1. **Infeasibility: a separate restoration phase or one algorithm** (Curtis, Ye ↔ Wächter, Fletcher; Nocedal on both sides; Robinson on restoration-free steps only) — Byrd, Curtis & Nocedal (co-authored; one paper, carded for both Curtis and Nocedal and cited for each in this line) reject switching designs (Fletcher–Leyffer restoration, SNOPT's switch to an ℓ1 approach) for one penalty-SQP algorithm whose penalty update, driven by predicted feasibility progress, gives fast local convergence to infeasible stationary points [frank-e-curtis card S009 pp. 1–3, 7–11, 13–14]; SQuID keeps that rate with at most two QP solves per iteration and no restoration phase [frank-e-curtis card S022 pp. 2–3, 25–27]. Ye cuts infeasibility "at the same rate as the barrier parameter" and returns a certificate [yinyu-ye SKILL.md Method 1, Taste 5; 01-publications SW5; arXiv:1801.03072]. Robinson, with Gould and Loh, sides with Curtis and Ye on the step only: the filter stays and the phase goes, every trial step coming from always-feasible subproblems that "value reducing both the constraint violation and the objective function" (10.1137/130920599, abstract) [andreas-wachter 05-peer-critique A4 (4e); roger-fletcher 05-peer-critique A7.3], with a penalty mode as "a replacement for a traditional restoration phase" (https://optimization-online.org/2014/12/4702/, p. 3; 10.1137/140996677), restoration being, they write, "generally accepted" as "the most dissatisfying aspect of such filter-based methods" (p. 19) [daniel-p-robinson 03-process-evidence §4.1; the p. 3 and p. 19 quotations read in the preprint, not in his notes]. Infeasibility handling itself lies outside his evidence, which seats Curtis and Ye there [daniel-p-robinson SKILL.md Research Task Routing, Blind spots]. Wächter keeps filter plus restoration, which his thesis calls "the only step where the filter line search method can fail" (p. 160, https://users.iems.northwestern.edu/~andreasw/pubs/waechter_thesis.pdf; host unreachable on 2026-10-17, archived copy https://web.archive.org/web/20260728163045/http://users.iems.northwestern.edu/~andreasw/pubs/waechter_thesis.pdf) [andreas-wachter 05-peer-critique A4; 10.1007/s10107-004-0559-y]; Fletcher's filter needs restoration too [roger-fletcher 05-peer-critique R1; 10.1007/s101070100244]. Nocedal's co-authored papers sit on both sides: in the same 2010 paper Byrd, Curtis & Nocedal name "the design of effective criteria for determining when such a switch should be made" as the switching approach's main difficulty [jorge-nocedal card S052 p. 2]; Nocedal, Oztoprak & Waltz then build a switch into KNITRO's interior methods, a feasibility mode ("restoration mode" in its pseudo-code) entered when the normal step leaves the linearized infeasibility at 0.9‖c‖ or more; since the switching conditions "can be sensitive to the choice of the constants", hysteresis rules are added that "make it unnecessary to try to adjust the values of the constants δ, δ̄ … during the progression of the algorithm"; their snapshot of current codes on 17 small infeasible problems says FILTER "performs well thanks to a carefully designed feasibility restoration phase" and that IPOPT has one, "but its performance is not consistently successful" [jorge-nocedal card S053 pp. 3–5, 8, 11–12] (Wächter's notes list this paper from its abstract only and record no reply to that verdict [andreas-wachter 05-peer-critique A4]). A contrast of published methods; Hinder & Ye's charge that IPOPT "has difficulties detecting infeasibility" (arXiv:1801.03072, p. 2) drew no reply [andreas-wachter 05-peer-critique A4 (4a); yinyu-ye 05-peer-critique B9], nor did Gould, Loh & Robinson's abstracts [andreas-wachter 05-peer-critique A4 (4e), Gaps; roger-fletcher 05-peer-critique A7.3]. Their tests leave out restoration-phase methods on principle (preprint p. 19), and their conclusion expects the other side to win here: "We suspect that a disadvantage of our approach is that methods, such as filter-SQP [16], would typically perform better on infeasible problems, a feature directly attributed to feasibility restoration" ([16] is 10.1007/s101070100244), naming Byrd, Curtis & Nocedal's infeasibility detection (10.1137/080738222) as a possible remedy (preprint p. 25; read there, not in his notes). Contested: robustness against speed (one-phase 21 vs 39 failures, 19 of IPOPT's 39 being `INIT_ERROR`, not broken down in the paper [yinyu-ye 03-process-evidence §4.4]; but median 3.3 s vs 0.6 s, with IPOPT's scaling and bound relaxation off) [andreas-wachter 05-peer-critique A4 (4a); arXiv:1801.03072 pp. 19–20, 30]. Curtis's own PIPAL benchmark shows both sides: Ipopt has the edge in efficiency on 417 CUTEr models and lags in robustness on the constructed degenerate and infeasible variants, "when an interior-point method is performing at its best, it is difficult to outperform such an approach in terms of efficiency" [frank-e-curtis card S033 pp. 22–28]; his talk slides (not papers, so no card) favour "Filter" on several infeasible toys [frank-e-curtis SKILL.md Tension 4]. Settle on constructed infeasible and degenerate variants, incumbent at defaults: time to a correct verdict, and feasible problems declared infeasible [philip-e-gill SKILL.md Method 2; 10.1007/978-3-319-23699-5_5].
2. **Step acceptance: penalty parameter, filter or funnel** (Fletcher, Toint ↔ Nocedal; Wächter between; a Robinson twin test) — Fletcher, Leyffer & Toint (co-authored): a suitable penalty parameter "depends on the solution", and a large one gives "much shortened Newton steps" (https://optimization-online.org/2006/10/1489/, p. 2) [roger-fletcher 02-methodology §5.6, 05-peer-critique A6.2; 10.1007/s101070100244]; Toint relaxes acceptance against free Newton, down to a funnel with neither penalty nor filter [philippe-l-toint 02-methodology B3; 10.1007/s10107-008-0244-7]. Byrd, Nocedal & Waltz (co-authored) motivate steering against the difficulties that, they write, "stimulated the development of filter methods which do not require a penalty parameter" (citing Fletcher & Leyffer): steering "promises, however, to resolve the difficulties mentioned above" (p. 7); the penalty is kept and set against an auxiliary LP (ν = ∞), the best attainable feasibility progress, and the huge-fixed-ν strategy, run with an initial ν = 10¹⁰, cut solved problems from 485 to 321 of 616 [jorge-nocedal card S042 pp. 7–11, 15–16]. They read Wächter & Biegler's controlled comparison as finding that the merit rule they derive "appears to be as effective as a filter approach in its ability to accept good steps" [jorge-nocedal card S042 p. 20]. Wächter's filter uses SOC, yet his unguarded "Full Step" run solved 86.1 %: safe Newton steps, or an easy test set; the same paper reports a clear robustness gain for the filter, which "seems to be only slightly more efficient" on problems both options solve [andreas-wachter 01-publications SW3, Contradictions 6; 10.1007/s10107-004-0559-y]. A contrast of published methods. Fletcher's notes read the steering paper as the penalty school's answer to the filter's founding critique, given inside the penalty framework rather than conceding it [roger-fletcher 05-peer-critique A6.2, D4; inferred there]; no reply from the filter side is recorded. Contested: whether an adaptive penalty or a penalty-free rule discards fewer good steps on hard problems. Settle in one code: each rule beside a free-Newton column, logging rejected full steps that free Newton survives, on a hard subset. Gould, Loh & Robinson ran one such twin in one code, where "the only difference between the two methods is in the step acceptance criteria" (https://optimization-online.org/2014/12/4702/, p. 19; 10.1137/140996677): the filter (FiSQO) against the same code with its penalty mode forced on (PenSQO, p. 21). They call PenSQO "a standard penalty-SQO approach" (p. 23), but its penalty parameter is updated from the steering step (pp. 4–5), the strategy being "based on steering methods designed for exact penalty functions" (10.1137/130920599, abstract), the family Nocedal's side defends. Result: similar robustness, "a slight edge going to FiSQO", "significantly" fewer function evaluations but a "less significant" difference in iterations, on 299 CUTEst problems with max{m, n} ≤ 100 and 57 with 100 < max{m, n} ≤ 1000 (pp. 22–23); no hard subset; "we are not claiming that FiSQO is better than a flexible penalty-SQO approach", and a flexible penalty in FiSQO's own penalty mode "could probably further improve the FiSQO results" (pp. 22–23) [daniel-p-robinson 03-process-evidence B1; design and outcome read in the preprint, not in his notes].
3. **Worst-case complexity as a design guide** (Toint, Nesterov ↔ Nocedal, Wright, Curtis, Robinson) — Toint: "Algorithm design profits from complexity analysis" [philippe-l-toint 02-methodology I7; 10.1007/s10107-009-0286-5]; Nesterov: complexity analysis selects "the promising optimization methods among hundreds of others" (*Optima* 78, 2008, p. 5, https://web.archive.org/web/20231203022724/https://www.mathopt.org/Optima-Issues/optima78.pdf), each priced against the class lower bound [yurii-nesterov 02-methodology T3, SKILL.md Method 6; 10.1007/s10208-025-09712-y]. Nocedal asks of theory "how well can it differentiate between efficient and inefficient methods", and judged Nesterov's 1983 optimal algorithm "unlikely to be effective in practice, but this has not been investigated, to the best of my knowledge" (Acta Numerica 1992; a remark, not an exchange) [jorge-nocedal card S019 pp. 2, 15]; in 2020, with Berahas and Bollapragada, the group's own worst-case CG analysis of subsampled Newton-CG "yields complexity estimates that are not indicative of its practical performance", and a spectrum-dependent bound, checked on plotted spectra, replaces it [jorge-nocedal card S041 pp. 11, 14–15]. His skill records this as a tension (Inner Tension IT5): the same survey says global-efficiency results, worst-case behaviour among them, "can be very useful but are difficult to obtain", and that global efficiency is "an area that requires more attention" [jorge-nocedal card S019 p. 2], and the Bottou–Curtis–Nocedal survey (co-authored) credits SG's success to "its superior work complexity guarantees" [jorge-nocedal card S004 p. 82]; his test is whether theory can differentiate efficient from inefficient methods, not complexity as such. Wright: complexity modifications "do not improve the practical performance" (arXiv:2510.15734, p. 23), and in CRRW21, written with Curtis, the no-safeguard twins needed fewer Hessian-vector products [stephen-j-wright 03-process-evidence §1.2; 10.1137/19M130563X], as that paper says of its regularization-free variants [frank-e-curtis card S020 p. 22]. Curtis: worst-case results "are too conservative" for practitioners' questions, so he audits the measure by regional complexity, which "can be used to guide the design of new algorithms" [frank-e-curtis card S062 pp. 3–4]; his own better-bound trust-region variant "would likely lead to very poor behavior in practice" [frank-e-curtis card S035 p. 9]. Robinson co-signed all five Curtis papers cited in this fault line; his skill keeps the critique joint with Curtis and names his own tension, "Complexity: co-author and critic" [daniel-p-robinson SKILL.md Warning sign 2, Inner Tensions 3; 05-peer-critique §6.2, §6.4; 10.1007/s11590-018-1286-2]. Yet TRACE ports ARC's optimal bound into a trust-region method [frank-e-curtis card S002 pp. 2–3, 5–9], and a 2018 paper with Robinson and Samadi adopts the premise that complexity-led design "led to methods with improved practical performance", at least for convex optimization [frank-e-curtis card S026 p. 1]. Toint's 2025 note replies that slow examples "are not isolated", though "typically quite contrived" (arXiv:2409.16047, p. 1) [philippe-l-toint 05-peer-critique K8], but names no one: a contrast of published methods. Contested: whether bound-driven safeguards cost performance on typical problems. Settle: the guaranteed variant against its no-safeguard twin in one code, with the bound plotted against the runs.
4. **Degeneracy: stabilize locally, or globalize the stabilization** (Wright ↔ Gill, Robinson) — Wright's stabilized SQP converges superlinearly to degenerate solutions, globalization set aside and solver embedding deferred three times [stephen-j-wright 03-process-evidence §4; 10.1023/A:1018665102534]; Gill globalizes an exact-Hessian stabilized QP and audits how often it fires, a globalization outside critics call hard [philip-e-gill SKILL.md Method 1; 01-publications §2.5, 05-peer-critique §5; 10.1137/120882913]. That paper's abstract calls existing stabilized methods "essentially local", a one-sided remark with no reply found [stephen-j-wright 05-peer-critique §2.2]. Robinson, its co-author, writes alone that "the best way to globalize sSQP is not yet clear" (p. 44), that for two-phase designs "it is difficult to develop conditions that reliably and efficiently decide when the global phase should transition to the local phase", and that efficient, reliable methods "will either be single-phase approaches or two-phase approaches in which the first-phase also uses some form of dual stabilization" (p. 45), and that a method should "substantially outperform Newton-based methods on degenerate problems" yet be "comparable" on nondegenerate ones (p. 47) [daniel-p-robinson 02-methodology §1.2, C3, 05-peer-critique §1.1; 10.1007/s11750-015-0371-2]. A contrast of published methods. A side exchange on IPM linear-algebra stability, not on stabilization: Wright's 2001 paper faults Forsgren, Gill & Shinnerl (10.1137/S0895479894270658) for "assumptions on the pivot sequence that do not always hold in practice" (arXiv:math/0103102, p. 2), with no reply found [stephen-j-wright 05-peer-critique §5.2]. Contested: whether the globalized method reaches its fast local region without long runs of short steps. Settle inside the globalized solver on a degenerate set: iterations to the first accepted stabilized step, and the share of modified iterations; then the same counts on a nondegenerate set (Robinson's criterion (v)).
5. **The inner solve: factorize, truncate or replace** (Gill ↔ Curtis, Gould ↔ Ye) — Gill regularizes each QP so third-party factorizations apply [philip-e-gill 01-publications §2.5; 10.1137/120882913]; Curtis derives the iterative solver's stopping tests from the merit model, primal and dual residuals tested separately; a baseline differing only in the stopping rule solved 45–86 %, the tests 100 % [frank-e-curtis card S006 pp. 5–7, 17]; inside Ipopt the inexact step solved 89 % of 617 CUTE problems against default Ipopt's 96 %, with speedups up to 17.89 on 3-D PDE problems [frank-e-curtis card S036 pp. 12–17], and the penalty update later moved inside the inexact QP solve [frank-e-curtis card S057 pp. 5, 7–9]; Gould would "solve the subproblem as inaccurately as possible consistent with overall convergence" and suspended SQP when untruncated QPs dominated (https://www.numerical.rl.ac.uk/media/people/nick-gould/Goul03_siagopt.pdf, p. 4) [nicholas-i-m-gould 01-publications §2 C–D; 10.1137/S1052623497322735]; Ye replaces the step by a subspace or eigenvector step from Hessian-vector products, shown only for unconstrained or linearly constrained problems [yinyu-ye SKILL.md Method 2; 01-publications SW5; arXiv:2208.00208]. A contrast of published methods. Contested: inertia without a factorization; eigen-steps in constrained NLP. Settle: profile the inner solve's share of each iteration, then compare factorized and inexact variants at equal outer iterations on the largest instances.
6. **What counts as the test: shared collection, real models, planted instances or class-split subsets** (Gould ↔ Fletcher; Toint between; Nesterov inferred; Gill ↔ Robinson on subsets, inferred) — the only exchange in print between members in these fault lines, and a partial agreement. Fletcher, *Optima* 99 (2015), p. 5: "I'd rather see half a dozen real industrial problems" than 500 CUTE problems; Toint replied in the same issue (p. 6) that this "naturally leads me to support Roger’s expressed preference", while CUTE(st) "remain absolutely crucial for tuning, comparison and standardization" (https://www.mathopt.org/optima/99/optima_99.pdf) [roger-fletcher 01-publications Contradictions 6, SKILL.md Tension T1, 04-mentorship T10; philippe-l-toint 05-peer-critique K3]. They agree on the purpose (users' real problems) and differ on the collection's role. Fletcher's late papers still used CUTEr [roger-fletcher 01-publications Contradictions; 10.1137/110844362]; Gould keeps the collection as a versioned instrument [nicholas-i-m-gould SKILL.md Method 2; 10.1007/s10589-014-9687-3]; Nesterov checks rates on instances with a known answer or a planted strictly feasible point, and his side of this contrast is inferred (his card) [yurii-nesterov SKILL.md Method 4; 03-process-evidence §1.1; arXiv:2412.14934]. Robinson's skill splits the verdict by a class named before the runs (SKILL.md Method 3 step 6; criteria (iv)–(v), TOP 2015 p. 47; fault line 4); his own example is an observation made from results already reported, "substantially better compared to SNOPT" on problems failing LICQ (p. 46), and the comment does not say that subset was fixed before the runs [daniel-p-robinson SKILL.md Method 3; 02-methodology §4.2; 10.1007/s11750-015-0371-2]; Gill's skill warns against "superiority shown on a subset": a scaling that wins on 38 shared problems is "actually harmful" on all 275 (https://www.ccom.ucsd.edu/~peg/papers/bfgsdev.pdf, p. 32) [philip-e-gill SKILL.md Warning sign 2; 02-methodology J2]. This pairing is inferred from Gill's card (its Robinson line), and the gap is narrow: neither rule prints the subset alone, Gill's "report both" (subset and full set) [philip-e-gill SKILL.md Method 3 stop rule] and Robinson's "print both verdicts" (hard subset and the rest) [daniel-p-robinson SKILL.md Method 3 step 6]; they differ on whether a subset named in advance may carry the verdict. Robinson's record shows the risk: one test kept only problems where "the LICQ held at all iterates in all runs of all algorithms that we ran" (arXiv:2007.10525v1, p. 26) [daniel-p-robinson 03-process-evidence B3, C5]; a contrast of published methods. Contested: whether collection verdicts transfer to users' models, and whether a class split reveals what a whole-collection profile hides or invites a chosen subset. Settle: run the same change on CUTEst, the user's models and planted instances, any class split fixed by a stated criterion before the runs and shown beside the whole collection, and report where the verdicts differ.

> 🔵 **Checkpoint 3 — after each round.** Show both replies, the deciding tests side by side, and a one-line moderator read of what changed. "`round` for another, `@Name …`, `pursue N`, `add <member>`, or `plan`." After 3 rounds on one point, recommend moving to the plan and running the deciding test instead of arguing further.

### Step 4 · Draft Plan (moderator) and Sign-off (member agents)

Write the draft in a neutral voice; tag each item with the member it comes from (→ Member · Method N), or "moderator: protocol template" when no member proposed it:

1. **Recommendation** — primary approach, tools, key settings, and why. Always state: method class and globalization (acceptance rule, penalty update, SOC, restoration or steering); Hessian option and inertia or regularization rule; linear-algebra path and its tolerances; barrier-update rule (interior-point methods; otherwise "not applicable"); what the solver returns on an infeasible problem; scaling and stopping tests; which mechanisms are defaults and which are labelled options; which hypotheses of the convergence theory the code can check, and the computable test behind any phase or support switch.
2. **Backup and switch rule** — the observable signal that says "switch to the backup", e.g. repeated restoration, a feasible model declared infeasible or a runaway penalty parameter (change the infeasibility handling); a safeguard firing on most iterations or full steps rejected near the solution (change the modification or the acceptance test); the inner solve dominating each iteration (truncate it or make it inexact); a support-update test that almost never fires after the first iterations (drop the acceleration phase).
3. **Minimal experiment** — 2–3 candidates on the user's problem or a cheap proxy, compared at the same budget on the same measure of progress; fixed seeds; replicate noisy runs. Protocol: a dated CUTEst snapshot with named exclusions, plus the user's models; the incumbent at defaults with matched tolerances and equal derivative information (if an incumbent's default uses less derivative information, e.g. SNOPT's quasi-Newton Hessian, run it at defaults, add a matched-information comparison where one exists, and print the asymmetry); failures typed and counted; performance profiles in time and evaluations (Dolan & Moré, 2002), pairwise or best-removed for three or more codes (Gould & Scott, 2016); a no-safeguard twin when the claim concerns a safeguard; any hard subset (e.g. LICQ failing) named by a stated criterion before the runs and reported beside the whole collection. Include the deciding tests from Step 3.
4. **Reformulation ideas** — ways to make the problem easier: rescaling, simplifying, splitting, exploiting structure.
5. **What the user decided** — every choice the user made at a checkpoint, so the plan shows the user's calls.
6. **Open questions**.

Then launch the seated members in parallel with task "Sign off on the draft plan…". Record each as ✅ sign-off or ⚠️ dissent (with its condition).

> 🔵 **Checkpoint 4 — approve the plan.** Show the draft with sign-offs and dissents. "`approve`, change anything, or `round` to reopen a point." This checkpoint is never skipped, even in autopilot.

### Step 5 · Verify and Deliver (moderator)

Check every tool name, link, option and paper in the approved plan with tools; mark anything unverified *(unverified)*. Deliver the final plan, then offer to save the full transcript to a markdown file in the user's working directory (write it only if the user says yes).

---

## Output Template (final plan)

```
## Problem Card
| Field | Value |

## Who sat
[Lead A lens], [Lead B lens], [Challenger lens] — why

## What was argued
- Disagreement → deciding test → what the user decided

## Plan
(each item tagged → Member · Method N, or moderator: protocol template)
1. Recommendation …
2. Backup and switch rule …
3. Minimal experiment (incl. deciding tests) …
4. Reformulation ideas …

## Sign-off
- [Lens] ✅ / ⚠️ dissent: … (holds if …)

## Open questions
## Sources (verified)
```

---

## Outside the Team

This team represents the smooth NLP solver tradition: interior-point and SQP / active-set methods, trust regions and regularization, quasi-Newton, penalty, filter and funnel globalization, and complexity theory, with nonsmooth BFGS-SQP (Curtis) and active-set methods for ℓ1 and group-sparse regularizers (Robinson) at its edge. Say so plainly when another tradition fits better:

- Integer or discrete decisions (MINLP) → NLP-based branch-and-bound such as Bonmin (Bonami et al., 2008, https://doi.org/10.1016/j.disopt.2006.10.011). Partly covered: Gill on fast infeasibility detection in subproblem sequences; Wächter co-authored Bonmin, but his skill places it outside this team.
- A certified global optimum of a nonconvex model → spatial branch-and-bound such as Couenne (Belotti et al., 2009, https://doi.org/10.1080/10556780903087124). Not covered: every lens here is local (Wächter co-authored Couenne, outside his skill).
- No usable derivatives, or a noisy black box → the `dfo-roundtable` skill (DFO Team, `product/dfo-team` in the nuwa repository; [link](../../dfo-team/dfo-roundtable/SKILL.md), valid inside the repository only). Partly covered: Nocedal's finite-difference quasi-Newton methods under noise.
- LP, QP or conic problems too large to factorize → first-order splitting such as OSQP (Stellato et al., 2020, https://doi.org/10.1007/s12532-020-00179-2) or PDLP (Applegate et al., arXiv:2106.04756). Partly covered: Ye (homogeneous self-dual embedding; GPU first-order LP in his group) and Nesterov (conic complexity theory).

## Shared References (verified October 2026)

- Dolan, E. D. & Moré, J. J. (2002). Benchmarking optimization software with performance profiles. *Math. Program.* 91(2), 201–213. https://doi.org/10.1007/s101070100263 — the standard for comparing solvers.
- Gould, N. I. M. & Scott, J. A. (2016). A note on performance profiles for benchmarking software. *ACM Trans. Math. Softw.* 43(2), 1–5. https://doi.org/10.1145/2950048 — why profiles of three or more solvers need pairwise or best-removed views.
- Gould, N. I. M., Orban, D. & Toint, Ph. L. (2015). CUTEst: a Constrained and Unconstrained Testing Environment with safe threads for mathematical optimization. *Comput. Optim. Appl.* 60(3), 545–557. https://doi.org/10.1007/s10589-014-9687-3; https://github.com/ralna/CUTEst — the shared test collection; its SIF classification scheme is the working taxonomy of problem types.
- Gratton, S. & Toint, Ph. L. (2025). S2MPJ and CUTEst optimization problems for Matlab, Python and Julia. *Optim. Methods Softw.* 40(4), 871–903. https://doi.org/10.1080/10556788.2025.2490640; https://github.com/GrattonToint/S2MPJ — the same problems without Fortran.
- Nocedal, J. & Wright, S. J. (2006). *Numerical Optimization*, 2nd ed. Springer. https://doi.org/10.1007/978-0-387-40065-5 — the common map of method families.
- Wächter, A. & Biegler, L. T. (2006). On the implementation of an interior-point filter line-search algorithm for large-scale nonlinear programming. *Math. Program.* 106(1), 25–57. https://doi.org/10.1007/s10107-004-0559-y; Ipopt https://github.com/coin-or/Ipopt — the open-source reference solver most comparisons include.
- Mittelmann, H. D. AMPL-NLP Benchmark (dated 9 Sep 2026). https://plato.asu.edu/ftp/ampl-nlp.html — an independent comparison of NLP codes at their defaults.

### Papers behind the documented disagreements

Curtis's side, read in full and carded (pages are those of the file read, as on the card):

- [frank-e-curtis card S009 pp. 1–3, 7–14] Byrd, Curtis & Nocedal (2010), Infeasibility detection and SQP methods for nonlinear optimization, *SIAM J. Optim.*, https://doi.org/10.1137/080738222 — fault line 1.
- [frank-e-curtis card S022 pp. 2–3, 25–27] Burke, Curtis & Wang (2014), A sequential quadratic optimization algorithm with rapid infeasibility detection, *SIAM J. Optim.*, https://doi.org/10.1137/120880045 — fault line 1.
- [frank-e-curtis card S033 pp. 22–28] Curtis (2012), A penalty-interior-point algorithm for nonlinear constrained optimization, *Math. Program. Comput.*, https://doi.org/10.1007/s12532-012-0041-4 — fault line 1.
- [frank-e-curtis card S002 pp. 2–9] Curtis, Robinson & Samadi (2017), A trust region algorithm with a worst-case iteration complexity of O(ε^-3/2) for nonconvex optimization (TRACE), *Math. Program.*, https://doi.org/10.1007/s10107-016-1026-2 — fault line 3.
- [frank-e-curtis card S026 p. 1] Curtis, Robinson & Samadi (2018), Complexity analysis of a trust funnel algorithm for equality constrained optimization, *SIAM J. Optim.*, https://doi.org/10.1137/16M1108650 — fault line 3.
- [frank-e-curtis card S035 p. 9] Curtis, Lubberts & Robinson (2018), Concise complexity analyses for trust region methods, *Optim. Lett.*, https://doi.org/10.1007/s11590-018-1286-2 — fault line 3.
- [frank-e-curtis card S062 pp. 3–4] Curtis & Robinson (2021), Regional complexity analysis of algorithms for nonconvex smooth optimization, *Math. Program.*, https://doi.org/10.1007/s10107-020-01492-3 — fault line 3.
- [frank-e-curtis card S020 p. 22] Curtis, Robinson, Royer & Wright (2021), Trust-region Newton-CG with strong second-order complexity guarantees for nonconvex optimization, *SIAM J. Optim.*, https://doi.org/10.1137/19M130563X — fault line 3.
- [frank-e-curtis card S006 pp. 5–7, 17] Byrd, Curtis & Nocedal (2008), An inexact SQP method for equality constrained optimization, *SIAM J. Optim.*, https://doi.org/10.1137/060674004 — fault line 5.
- [frank-e-curtis card S036 pp. 12–17] Curtis, Huber, Schenk & Wächter (2012), A note on the implementation of an interior-point algorithm for nonlinear optimization with inexact step computations, *Math. Program.* (Ser. B), https://doi.org/10.1007/s10107-012-0557-4 — fault line 5.
- [frank-e-curtis card S057 pp. 5, 7–9] Burke, Curtis, Wang & Wang (2020), Inexact sequential quadratic optimization with penalty parameter updates within the QP solver, *SIAM J. Optim.*, https://doi.org/10.1137/18M1176488 — fault line 5.

Nocedal's side, read in full and carded (pages of the file read: author preprints and reports, arXiv v4 for the 2020 paper, arXiv v3 for the 2018 survey; quotations outside the cards' Quotes lists re-read in those files on 2026-10-17):

- [jorge-nocedal card S052 p. 2] Byrd, Curtis & Nocedal (2010), Infeasibility detection and SQP methods for nonlinear optimization, *SIAM J. Optim.*, https://doi.org/10.1137/080738222 — fault line 1 (also on Curtis's list above).
- [jorge-nocedal card S053 pp. 3–5, 8, 11–12] Nocedal, Oztoprak & Waltz (2014), An interior point method for nonlinear programming with infeasibility detection capabilities, *Optim. Methods Softw.*, https://doi.org/10.1080/10556788.2013.858156 — fault line 1.
- [jorge-nocedal card S042 pp. 7–11, 15–16, 20] Byrd, Nocedal & Waltz (2008), Steering exact penalty methods for nonlinear programming, *Optim. Methods Softw.*, https://doi.org/10.1080/10556780701394169 — fault line 2.
- [jorge-nocedal card S019 pp. 2, 15] Nocedal (1992), Theory of algorithms for unconstrained optimization, *Acta Numerica*, https://doi.org/10.1017/s0962492900002270 — fault line 3.
- [jorge-nocedal card S041 pp. 11, 14–15] Berahas, Bollapragada & Nocedal (2020), An investigation of Newton-Sketch and subsampled Newton methods, *Optim. Methods Softw.*, https://doi.org/10.1080/10556788.2020.1725751 — fault line 3.
- [jorge-nocedal card S004 p. 82] Bottou, Curtis & Nocedal (2018), Optimization methods for large-scale machine learning, *SIAM Rev.*, https://doi.org/10.1137/16M1080173 — fault line 3 (his tension IT5).

The other nine members are base tier, no deep reading: the papers behind their sides are named inline in each fault line (DOI or arXiv id) next to the research-note passage that cites them. Robinson's sides (added 2026-10-17) rest the same way on his research notes and the primary texts named inline; he has no paper cards (base tier, no deep reading planned).

## Honest Boundary

- The discussion is simulated from methods distilled from public work; it is not what these researchers would actually say.
- Member agents are separate model instances reading different skill files. That makes their positions more independent than a single-context simulation, but they share one underlying model and can converge for reasons that have nothing to do with the researchers.
- Coverage: [../DEEP-READING.md](../DEEP-READING.md) (Curtis and Nocedal deep tier, with paper cards; the other nine members, Robinson included, base tier, on research notes 01–06).
- Fault lines 1, 2, 3 and 5 rest on paper cards for the deep-read sides (Curtis in 1, 3 and 5; Nocedal in 1, 2 and 3; pages as read; card quotations verified, other quotations re-read in the full texts) and on research notes for the base-tier sides (Robinson's parts of fault lines 1 and 2 add passages read in the 2014/12/4702 preprint; see below); fault lines 4 and 6 involve only base-tier members and rest on their Roundtable Cards and research notes (no paper cards), with quotations checked against the sources. One rests on an exchange in print (Fletcher and Toint, *Optima* 99, 2015: agreement on real problems, difference on the shared collection's role); in fault line 2, Fletcher's notes read Byrd, Nocedal & Waltz 2008 as the penalty school's answer to the filter rationale (an inference there; the paper sets steering against the difficulties that, it says, stimulated filter methods, p. 7, and cites Wächter & Biegler's comparison with a filter line search, p. 20); the rest contrast published methods. The Wright–Ye exchange on cyclic coordinate descent (Sun & Ye, 10.1007/s10107-019-01437-5, answered by Lee & Wright, 10.1093/imanum/dry040) is also in print but lies outside these NLP-solver fault lines [stephen-j-wright 05-peer-critique §5.1]. Robinson's additions to fault lines 3, 4 and 6 rest on his SKILL.md and notes (the Gill pairing in fault line 6 on Gill's card); those to fault lines 1 and 2 add quotations and results read in the 2014/12/4702 preprint (pp. 3, 4–5, 19, 21–23, 25), not in his notes, and the abstract of 10.1137/130920599 (its restoration sentences are quoted in Wächter's and Fletcher's notes; the steering sentence of fault line 2 was read on Crossref). Every primary text quoted was re-read and the quotations checked on 2026-10-17. His sharpest exchange in print, with Izmailov & Solodov on whether local theory may assume which subproblem solution is computed (they have "never encountered" a rate lost to "wrong" solutions, 10.1007/s11750-015-0373-0, p. 51), involves no other member [daniel-p-robinson 05-peer-critique §1.1].
- Fletcher (d. 2016) is a historical lens: it reflects work up to then; later developments are others' work.
- Outside this team: mixed-integer, global, derivative-free and first-order conic-splitting traditions.
- Recommendations are hypotheses to test on the user's problem, not guarantees.
- Research date: 2026-09-28 (fault lines checked against the members' skill files and research notes; references verified with Crossref, arXiv and the sources' pages); 2026-10-10 (Curtis's side of fault lines 1, 3 and 5 re-checked against his paper cards; no new fault line added, the six-line maximum being reached); 2026-10-17 (Robinson added to the Team table, Problem Card, seating and fault lines 1–4 and 6; seating merged to 14 rows; still six fault lines; every DOI and arXiv id re-checked on Crossref and arXiv, every URL fetched, except Wächter's thesis, whose host did not respond: its archived copy is linked; after review, Robinson's side of fault line 1 was narrowed to restoration-free steps with the preprint's p. 25 concession, and fault line 2's twin described as steering-updated, both re-read in the 2014/12/4702 preprint); 2026-10-17, after Nocedal's deep reading (T3.8): his sides of fault lines 1–3 moved from research notes to his paper cards, every quotation from his papers re-read in the file carded, the five DOIs of his papers re-checked on Crossref; his Team-table lens extended for Method 7 (sampled curvature); no new fault line, the six-line maximum being reached; after review, the same day: fault line 1's 2010 infeasibility-detection paper attributed to its three authors, the 2014 hysteresis quotation given in full (p. 12); fault line 2's "answer in print" re-attributed to Fletcher's notes as an inference, the huge-fixed-ν wording aligned with the card, the p. 20 quotation's "appears to be" restored; fault line 3 given Nocedal's own tension IT5 (the 1992 survey, p. 2; the 2018 survey with Bottou and Curtis, p. 82), the 2018 survey's DOI checked on Crossref; every changed quotation re-read in the file carded.

---

> Generated with [女娲 · Skill造人术](https://github.com/alchaincyf/nuwa-skill) research-craft mode

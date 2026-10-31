# Optimization Council · Personal Research Advisors

A research-craft skill distilled from the public work of Dimitris Bertsimas, who convenes and leads the repository's four optimization teams (LP, NLP, DFO and MINLP) as guest delegations. With it come a lead skill, through which he heads the four teams on any question put to them, and a roundtable skill that seats them on your problem.

Field: cross-team optimization council convened and led by Dimitris Bertsimas (MIT): operations research and optimization across linear, integer and mixed-integer, robust and adaptive, convex/conic/moment, stochastic and dynamic, and data-driven optimization, machine learning and statistics under a modern optimization lens, and analytics applications. His research-craft skill is partitioned by optimization domain (the codes in team.json "domains": LO, IO, RO, CP, SD, ML, DA, HS, AP), each domain mapped to the repository teams it engages; research notes and paper cards tag findings with these codes. The council seats the members of the repository's four teams as guest delegations (team.json "guest_teams": LP Team product/lp-team, NLP Team product/nonlinear-team, DFO Team product/dfo-team, MINLP Team product/minlp-team), and Bertsimas convenes and leads their cross-team discussion. Not represented as voices of their own: stochastic programming as a separate tradition, approximate dynamic programming and reinforcement learning, statistical learning theory, and constraint programming.

This council follows Bertsimas's modern-optimization tradition as its lead (exact LP, conic and mixed-integer models kept in the solver class, robust and data-driven optimization, a bound for every policy, decisions scored against the owner's current rule), with the repository's four teams seated as delegations; stochastic programming as a separate tradition, approximate dynamic programming and reinforcement learning, statistical learning theory and constraint programming are not represented, nor are the neighbours that the delegations' own team files exclude, such as first-order (PDLP-type) LP and splitting methods and Bayesian or evolutionary blackbox optimization.

## The Team

| Member | Lens · known for | Status |
|--------|------------------|--------|
| [Dimitris Bertsimas](dimitris-bertsimas/SKILL.md) · council lead and convener | **Lens:** start from a decision someone owns and the data held; write it exactly as LP, conic or MIO that stays in the solver class; bound every policy before trusting one; price what matters with one knob; judge decisions against the current rule; re-measure every *intractable*.<br>**Known for:** [*The price of robustness*](https://doi.org/10.1287/opre.1030.0065) with Sim (2004) and the [robust-optimization survey in *SIAM Review*](https://doi.org/10.1137/080734510) with Brown and Caramanis (2011); the [achievable-region method](https://doi.org/10.1007/BF01149167) for queueing control (1995) and [conservation laws and extended polymatroids](https://doi.org/10.1287/moor.21.2.257) with Niño-Mora (1996); [optimal probability inequalities by convex optimization](https://doi.org/10.1137/S1052623401399903) with Popescu (2005); [stochastic and dynamic vehicle routing](https://doi.org/10.1287/opre.39.4.601) with van Ryzin (1991); [best subset selection via a modern optimization lens](https://doi.org/10.1214/15-AOS1388) with King and Mazumder (2016) and [optimal classification trees](https://doi.org/10.1007/s10994-017-5633-9) with Dunn (2017); [from predictive to prescriptive analytics](https://doi.org/10.1287/mnsc.2018.3253) with Kallus (2020); the books *Introduction to Linear Optimization* (with Tsitsiklis, 1997), *Optimization over Integers* (with Weismantel, 2005), *Machine Learning under a Modern Optimization Lens* (with Dunn, 2019) and *Robust and Adaptive Optimization* (with den Hertog, 2022). Boeing Professor of Operations Research at MIT; MIT Vice Provost for Open Learning since 2024. | T3 deep tier ([DEEP-READING.md](DEEP-READING.md)): T3.6 synthesized, T3.7 tightened, one T4 increment, nine domain files. `team_status.py` (2026-10-31): `T3.6 synthesized (12904 words)`; the Domain Map had taken `SKILL.md` to 13,153 words, and a status trim the same day moved the corrections list and two Honest Boundary lists verbatim into the evidence ledger, bringing it back under the 13,000-word budget (12,881); the hand-over lines for `optimization-lead` then added 23 words |
| [LP Team](../lp-team/README.md) · guest delegation | **Brings:** dual revised simplex engineering inside production LP solvers (hsol, the origin of HiGHS's simplex; parallel dual simplex; LU updates; Xpress, COPT): a technique counts only by its net gain inside a state-of-the-art sparse solver, with its ceiling computed before it is built.<br>**Members:** Huangfu. | base tier: Huangfu T1 base skill; the team layer (T2) not yet run |
| [NLP Team](../nonlinear-team/README.md) · guest delegation (folder `nonlinear-team`) | **Brings:** smooth NLP solver design and theory: interior-point and SQP codes (Ipopt, KNITRO, SNOPT, PCx), quasi-Newton updates (BFGS, L-BFGS), trust-region and regularization methods with their evaluation complexity (LANCELOT, ARC) and the CUTEst test collection, penalty and filter globalization, the homogeneous self-dual IPM and complexity lower bounds; every safeguard tested against a twin without it, on whole collections.<br>**Members:** Curtis, Nocedal, Wright, Ye, Wächter, Gill, Toint, Gould, Fletcher, Nesterov, Robinson. | mixed tier: Curtis and Nocedal deep tier (T3.6 synthesized); the other nine T1 base skill |
| [DFO Team](../dfo-team/README.md) · guest delegation | **Brings:** derivative-free and blackbox optimization, budgets counted in function evaluations: interpolation models in a trust region (COBYLA, NEWUOA, BOBYQA), certified fully linear models, probabilistic models and STORM, direct search with worst-case complexity, MADS, the progressive barrier and NOMAD for unreliable simulators.<br>**Members:** Powell, Conn, Scheinberg, Vicente, Audet. | deep tier: all five T3.6 synthesized |
| [MINLP Team](../minlp-team/README.md) · guest delegation | **Brings:** mixed-integer nonlinear and global optimization: outer approximation, DICOPT and generalized disjunctive programming; NLP-based branch and bound (FilMINT, Minotaur); branch-and-reduce in BARON, judged at defaults on public libraries; GloMIQO and ANTIGONE and formulations of trained models (OMLT); copositive, SDP and SOC relaxations; cut and branch-and-bound theory measured against exact ground truth.<br>**Members:** Grossmann, Leyffer, Sahinidis, Misener, Burer, Dey. | deep tier in progress: Burer and Dey T3.6 synthesized; Leyffer and Misener T3.5 carded; Grossmann and Sahinidis T3.2 full texts; the team layer (T2) not yet run |
| [`optimization-lead`](optimization-lead/SKILL.md) | The front door: Bertsimas heads the four teams on any question put to them. He frames it by domain and stage, routes it to the team that settles it (that team's own skill, its roundtable, or a council session) and reviews each team's answer against his sign-off rule | lead |
| [`council-roundtable`](council-roundtable/SKILL.md) | Convenes the council: Bertsimas leads, the guest members your problem needs are seated from the four delegations, and the discussion ends in a plan with each member's sign-off or dissent | roundtable |

Bertsimas's lens is the "Lens (one line)" of his `## Roundtable Card`; "known for" is taken from his `SKILL.md` (Signature Work Anatomy, Sources), with the DOIs of his audited `works.json`. Each delegation's line condenses its members' lenses and known-for lines; each member's own lens is the "Lens (one line)" of the `## Roundtable Card` in that member's `SKILL.md`. Status from `python3 scripts/team_status.py product/<team>` on 2026-10-31. Guests with paper cards (the five DFO members; Curtis and Nocedal; Leyffer, Misener, Burer and Dey) are cited in the roundtable by their cards, with pages where a card rests on a full or partial reading; the others are cited through their skills and research notes. No member of the council has a **student mode**; in the DFO delegation, Scheinberg's skill has one (proof playbook, open problems, reading path, pre-meeting review).

## Install (Claude Code)

The council needs its four guest teams installed alongside it. The roundtable seats guest members from the LP, NLP, DFO and MINLP teams and finds every member, Bertsimas included, as a sibling folder, where it also reads that member's cards and notes. So copy the skill folders of `product/optimization-council`, `product/lp-team`, `product/nonlinear-team`, `product/dfo-team` and `product/minlp-team` into the same skills directory: 28 folders on 2026-10-31, namely the council's three (`optimization-lead`, `dimitris-bertsimas` and `council-roundtable`), the 23 guest members, and the NLP and DFO roundtables. The LP and MINLP roundtables are left out: they are still unfilled templates (their team layer, T2, has not run), and the council sends their questions to the member skills instead. For a team's one-voice answer the lead also uses the NLP and DFO corpus team skills, `nlp-team` and `dfo-team` (folders `teams/nlp-team` and `teams/dfo-team`, each installed on its own; see the corpus note at the top of each). Without them, the lead offers a member view or `discuss <team>` (that team's roundtable).

```bash
# macOS / Linux — global install of the council and its four guest teams
mkdir -p ~/.claude/skills
for t in optimization-council lp-team nonlinear-team dfo-team minlp-team; do
  for d in product/$t/*/; do
    case "$d" in */lp-roundtable/|*/minlp-roundtable/) continue ;; esac   # templates until their team layer runs
    cp -R "${d%/}" ~/.claude/skills/
  done
done
```
```powershell
# Windows PowerShell
New-Item -ItemType Directory -Force "$HOME\.claude\skills" | Out-Null
foreach ($t in "optimization-council", "lp-team", "nonlinear-team", "dfo-team", "minlp-team") {
  Get-ChildItem "product\$t" -Directory | Where-Object { $_.Name -notin "lp-roundtable", "minlp-roundtable" } |
    ForEach-Object { Copy-Item -Recurse $_.FullName "$HOME\.claude\skills\" }
}
```

Run either from the repository root. `${d%/}` drops the trailing slash, so that macOS `cp` copies each folder and not just its contents; the skills directory is created first, so that the first copy does not become the directory itself. Restart Claude Code so it picks up the new skills. Once a team's layer has run, take its roundtable off the skip list. The deep-reading records (`DEEP-READING.md`) and the team READMEs stay in the repository, so links to them from an installed skill work only in a checkout.

The NLP and DFO roundtables share generic triggers ("ask the team", "convene the roundtable", "what would the team do") with each other and with any other team skill you may have installed, so name the one you want ("Optimization Council", "DFO roundtable", "nonlinear-roundtable"); another installed skill that answers to the same team name, such as "DFO team", may take the request first. A guest that is not installed is named and left out, never improvised; Bertsimas's skill without the roundtable says so and gives only the agenda.

## Use

**Ask the teams through their lead** (the front door):

```
> Optimization Lead: our simulator takes two hours per run and has 30 design parameters, which our engineers
  set by hand today. What should we try, and how would we know it beats them?
```

Start with `Optimization Lead:` or `/optimization-lead`: with many skills installed, Claude Code may list a rarely used skill by name only, so its other triggers can go unseen. Bertsimas leads every question put to the teams through `optimization-lead`, in three steps:

1. **Frame and route.** He codes the question by optimization domain and finds the first open stage of his gate: owner and current rule, formulation class, measured tractability, certificate or bound, decision metric. He then routes it by his convener rule (LP engines → LP; continuous, conic, robust nonlinear → NLP; black-box → DFO; global, mixed-integer → MINLP; stochastic and dynamic: no team, marked open).
2. **Team answers.** Each routed team answers as its own agent from its own skill, quoted verbatim:
   - NLP and DFO answer through their corpus team skills (`nlp-team`, `dfo-team`), and through member views where those corpora have no entry (robust or conic questions, discrete blackboxes); their roundtables run on `discuss <team>`;
   - LP and MINLP, with no team skill yet, answer through their best-fit members, labelled member views.
3. **Review.** He signs off ✅ only if the answer names each field asked of it (the current rule or incumbent, a class with a solve-time test, a certificate, gap or bound valid for every policy, the decision metric) or shows that none exists or that only you can supply it; otherwise ⚠️ he names what is missing. A ✅ checks those fields, not the answer's claims.

When two or more teams contest the question, he convenes the council (below). A question you address to the NLP or DFO team by name ("DFO team …") goes to that team's own skill, without him; one to the LP or MINLP team comes to him. Modes: `quick` (no routing checkpoint), `lead only`, `discuss <team>`, `council`, `agenda`.

**Convene the council on a problem:**

```
> Optimization Council: day-ahead commitment of 300 units under wind uncertainty, today a fixed reserve margin. Our robust MIO
  stalls at a 2% gap within the 1-hour limit, and AC feasibility comes only from the operator's black-box power-flow tool.
```

Bertsimas convenes and leads. In full mode (the default) the moderator codes your problem by optimization domain and seats the members named in the rows of the roundtable's seating table that it matches; Bertsimas frames the problem by domain in his opening, and if his codes differ from the moderator's, the moderator offers to add that delegation at checkpoint 2. In agenda mode his skill proposes the items and their seats from the same table, and the moderator checks them. In the challenges he concedes his recorded corrections and blind spots but holds to class preservation, measured solve times and the decision metric, and he signs off only on a plan that names the current rule or incumbent, a class with a solve-time test, a certificate, gap or bound valid for every policy, and the decision metric (otherwise he dissents and names what is missing). Each seated member runs as **its own agent** that reads its own skill file; the main session moderates. You chair the discussion — it pauses at four checkpoints:

| Checkpoint | You see | You can |
|-----------|---------|---------|
| 1 · Card and seats | Problem Card, who sits and why | Correct the card, change seats, answer ≤2 questions |
| 2 · After openings | Each member's position, first experiment, risk; agreements and splits | Answer members' questions, ask anyone, pick the disagreement to argue |
| 3 · After each round | Both sides' replies and the test that would settle the point | Another round, bring someone in, or move to the plan |
| 4 · Draft plan | Plan with each member's sign-off or dissent | Approve, change, or reopen a point (never skipped) |

**Controls** (any time):

| Say | Effect |
|-----|--------|
| `go` | Accept the default and continue |
| `@Bertsimas …` / `@all …` | Ask one member, or every seated member |
| `@LP …` / `@NLP …` (or `@Nonlinear …`) / `@DFO …` / `@MINLP …` | Ask a delegation: its best-fit member for the question answers, without being seated |
| `add Audet` / `drop Nesterov` | Change who is seated (Bertsimas always sits) |
| `add DFO` (any team) | Seat that delegation's best-fit member not yet seated |
| `agenda` / `next` | Switch to agenda mode / close the current agenda item and open the next |
| `pursue 2` / `round` | Pick the disagreement / run another round |
| `plan` / `plan item` / `autopilot` | Go to the plan now (in agenda mode, one programme plan) / the current agenda item's plan only / run to the draft plan without stopping |
| `stop` | End the council; keep the transcript |

Anything else you type is passed to the seated members as new information. At the end the moderator offers to save the transcript as a markdown file.

Cost: one agent call per seated member per turn, so a round costs as many calls as there are seats; the moderator says how many agents a step will launch before launching more than 4, and in agenda mode estimates the whole agenda's count at checkpoint 1. Runtimes without subagents fall back to a single-model simulation, and the moderator says so.

**Agenda mode** (Bertsimas as convener, before anyone argues):

```
> Optimization Council, agenda: replace our greedy operating-room scheduler with an exact model; 30 rooms,
  surgery durations learned from 4 years of logs, a hospital simulator that scores schedules, weekly re-planning.
```

Bertsimas drafts the convener's agenda before any delegation argues: 3–5 items across domains. For each item it gives the stages still open, from owner, data and current rule through the impact gate, the formulation class, measured tractability, the knob and its price, and a certificate, gap or bound valid for every policy, to the decision metric and deployment. It also names the delegations that settle each item (LP engines → LP Team; continuous, conic and robust nonlinear → NLP Team; black-box → DFO Team; global and mixed-integer → MINLP Team), with the seats taken from the roundtable's seating table, the documented fault line the item touches, and the test that decides it. An item stops at its first failed stage, with the fix. Stochastic and dynamic items engage no delegation and stay open: Bertsimas frames them and names the deciding test, without cross-examination, and they go to the plan's open questions. Approve, edit or drop items at checkpoint 1; each approved item is then argued with its own seats (`next` moves on to the next item), and the plan keeps each item's deciding test.

**Other modes:**

```
> Optimization Council, quick: …                                    # Bertsimas plus 1–2 delegates, straight to plan
> Optimization Council, debate Bertsimas vs Sahinidis: exact MIO or a global solver for our sparse regression?   # two lenses argue one decision
> Use the Bertsimas lens on my robust counterpart and its solve-time table
> How would Bertsimas bound the policy our dispatch heuristic computes?   # a single member directly
```

Say "exit" or "end council" to return to normal mode.

**Technique catalogs.** Each deep-read skill has a `references/technique-catalog.md`. It lists the transferable devices found by reading that researcher's papers in full; [Bertsimas's](dimitris-bertsimas/references/technique-catalog.md) has proof devices (duality and exact reformulation, relaxations and bounds, probabilistic analysis, rounding and tight instances, complexity and counterexamples, dynamic programming with structure kept), design moves, experiment and evaluation protocols, writing moves, domain-specific engineering kept out of `SKILL.md`, and teaching and book design from the open parts of his books. Each entry has a one-line "how to use it" and the paper cards, with pages, that it rests on. Bertsimas's `SKILL.md` points to catalog sections, not entry ids (Method 7 step 1 to §1.2, relaxations and bounds; the "bound does not move" routing row to §1.1). The guests' catalogs sit in their own teams' folders: the five DFO members, Curtis and Nocedal in the NLP Team, Burer and Dey in the MINLP Team. You can also ask for the catalog directly:

```
> Which of Bertsimas's relaxation-and-bound devices fit the routing policy I need to grade?
> Bertsimas lens: which evaluation protocol from his catalog should I use to duel my MIO against the incumbent heuristic?
```

**Domain files.** Bertsimas's skill is partitioned by optimization domain into nine standalone files under [`dimitris-bertsimas/references/domains/`](dimitris-bertsimas/references/domains/), one per code in `team.json`, each mapped to the delegations it engages: [LO](dimitris-bertsimas/references/domains/01-LO-linear-optimization.md) (LP, NLP), [IO](dimitris-bertsimas/references/domains/02-IO-integer-mixed-integer.md) (MINLP, LP), [RO](dimitris-bertsimas/references/domains/03-RO-robust-adaptive.md) (NLP, MINLP, DFO), [CP](dimitris-bertsimas/references/domains/04-CP-convex-conic-moment.md) (NLP, MINLP), [SD](dimitris-bertsimas/references/domains/05-SD-stochastic-dynamic-queueing.md) (none), [ML](dimitris-bertsimas/references/domains/06-ML-machine-learning-statistics.md) (MINLP, NLP, DFO), [DA](dimitris-bertsimas/references/domains/07-DA-prescriptive-analytics.md) (all four), [HS](dimitris-bertsimas/references/domains/08-HS-heuristic-simulation.md) (DFO) and [AP](dimitris-bertsimas/references/domains/09-AP-applications.md) (all four). Each has the same nine sections, from §1 footprint and timeline to §9 coverage and gaps; §6, the cross-team interfaces, gives for each meeting point with a guest member his position, theirs, how the two relate (an exchange in print, or a contrast of published methods), what is still contested and the deciding test. The Domain Map in his `SKILL.md` routes a question to its file:

```
> Bertsimas lens, RO domain file: does our budgeted uncertainty set keep the unit-commitment MIO in its class, and which delegation would contest it?
```

**Sessions.** [first-session-2026-10-31.md](first-session-2026-10-31.md) records the council's first session (agenda mode, autopilot to checkpoint 4; about 53,000 words). Bertsimas chose the topic, *the price of exactness*, and set four items, one per delegation, each on a documented fault line:

- what a "why now" speed-up may rest on (LP, FL1);
- what proof time buys a statistical estimator (NLP, FL2);
- what a stopped robust search on a simulator may claim (DFO, FL4);
- where heavier conic rungs stop paying (MINLP, FL5).

Ten delegates sat: Huangfu; Gould, Nocedal and Wright; Vicente, Audet and Conn; Sahinidis, Burer and Dey.

The first run left out the challengers' turns (Sahinidis on items 1 and 2, Conn on item 3, Dey on item 4), so they were run afterwards. The programme plan was then revised (v2) and signed again. Six members signed, two of them on conditions v2 does not yet meet; five dissented, each stating the condition under which they would sign.

Three checks are recorded, and every flagged claim is annotated where it stands:

- a first verification;
- a second verification of the challengers' round and v2;
- a census of all 271 card citations of the first run.

The plan only designs its deciding tests: none was run, and approving it at checkpoint 4 is yours.

## Resources

The council's own member has a folder that keeps track of the resources behind that skill; each guest's folder lives in its own team, with the same layout at that member's tier.

```
dimitris-bertsimas/
├── SKILL.md                             # the research skill: methods, Domain Map, Roundtable Card (links into the ledger)
└── references/
    ├── technique-catalog.md             # transferable devices from the papers, each with card pages
    ├── domains/
    │   ├── 01-LO- … 09-AP-*.md          # nine domain files, one per team.json code, nine sections each
    │   └── work-domains.json            # the domain tags of every indexed work and book item
    ├── research/
    │   ├── 01- … 06-*.md                # six research notes (publications, stated method, process
    │   │                                #   evidence, mentorship, critique, trajectory)
    │   ├── cards/<batch>.md             # paper cards: D1–D8, method links, verified quotes, page refs
    │   ├── cards/<batch>.digest.json    # the same cards, machine-readable
    │   ├── 07-paper-cards.md            # card index: one row per work, read level, methods linked
    │   ├── 08-deep-reading-synthesis.md # patterns, promotions and corrections drawn from all cards
    │   ├── 09-evidence-ledger.md        # full evidence behind each SKILL.md item
    │   └── 10-claim-audit.md            # sampled claim-to-card audits and their fixes
    └── sources/
        ├── RESOURCES.md                 # tracker: every source, verified ✅ or lead ⚠️, where it was used
        ├── publications/
        │   ├── works.json               # complete publication list, cross-checked (DBLP, Crossref, arXiv)
        │   └── scholar.md               # the same list, readable, with audit notes
        ├── papers/
        │   ├── INDEX.md                 # every work: full-text status, role, read level
        │   ├── abstracts.json           # abstracts (arXiv / Crossref / chased)
        │   ├── abstract-sources.json    # where each chased abstract came from
        │   ├── book-leads.json          # links to the open parts of his books (T4)
        │   ├── *.pdf                    # open full texts (git-ignored)
        │   └── txt/                     # extracted text with [[page N]] markers (git-ignored)
        ├── talks/                       # the 2014 MIT Sloan oral history transcript
        ├── essays/                      # methodology writings, surveys (none yet)
        ├── software/                    # notes on the researcher's software and code (none yet)
        └── private/                     # git-ignored; only its README is tracked
```

The technique catalog, `domains/`, `cards/`, 07–10, `publications/` and `papers/` come from the deep reading and the council's domain layer (see [DEEP-READING.md](DEEP-READING.md)); a base-tier skill, as several guests have, has only `SKILL.md`, the notes 01–06 and `RESOURCES.md`. A member with a student mode also has `proof-playbook.md`, `open-problems.md` and `reading-path.md` under `references/`. No `private/` folder is ever published.

To add a resource later, add a row to that researcher's `RESOURCES.md` and drop the file into the matching folder. If the resource changes a method, update the research note and `SKILL.md`. To add a paper's full text, follow "How to extend" in [DEEP-READING.md](DEEP-READING.md).

This council is configured by [team.json](team.json): its `guest_teams`, its `domains` (the nine codes, each with the teams it engages) and its `chase_hints`. To build another team like it, or to update this one, use the generic kit in this repository (`scripts/new_team.py`, the saved workflows in `scripts/workflows/`): see the [research-team playbook](../../references/research-team-playbook.md).

## Honest Boundary

- These are simulated lenses built from public work, not the researchers' own views.
- The research started from web search results in October 2026 (research notes of 2026-10-28). On 2026-10-29 it was deepened by reading Bertsimas's publications in full or in part wherever an open copy exists; the nine domain files followed the same day, claim audits on 2026-10-29 and 2026-10-31, and the Domain Map on 2026-10-31. Coverage, from his `papers/INDEX.md` (details in [DEEP-READING.md](DEEP-READING.md)):

  | Researcher | Works indexed | Read in full / in part | Abstract or metadata only (incl. unreadable) | Skipped (not the author's, or not research) |
  |---|---|---|---|---|
  | Bertsimas | 751 | 413 / 59 | 119 | 160 |

  Works without an open full text are known from their abstract or metadata only. These include the bodies of all eight of his books (*Introduction to Linear Optimization*, *Data, Models, and Decisions*, *Optimization over Integers*, *The Analytics Edge*, *Machine Learning under a Modern Optimization Lens*, *Robust and Adaptive Optimization*, *Queueing Theory: Classical and Modern Methods* and *The Analytics Edge in Healthcare*), the 2026 robust-optimization retrospective with den Hertog and part of the 1990s achievable-region series. What is openly available of the books was read in a T4 increment and carded apart from the table (21 items): the 1997 preface as the publisher serves it, publisher pages, four printed contents lists, the 1997 textbook's errata sheet (last updated 2021), four reviews, his own books pages, the 1992 printing of the simulated-annealing review and the 2009 syllabus of his course 15.093J. The 2014 MIT Sloan oral history, read in full for the research notes, is not an indexed work and is not counted. The table covers the council's own member only; each delegation's coverage is in its own team's `DEEP-READING.md`. Each skill's Honest Boundary lists its gaps, and `RESOURCES.md` marks unverified leads ⚠️.
- Bertsimas as convener and chair is a construct of this council (his skill's Honest Boundary), designed from his methods and marked [inferred] in its Activation Rules; his role as head of the four teams (`optimization-lead`) extends that construct [inferred]; in 2014 he said he meets each student one on one and holds no whole-group meetings (his note 02, O10). His lens transfers to models and bounds (class, knob, bound, baseline, decision metric), not to the internals of commercial solvers (his skill's How to Use, "Domain fit"), and the inside of commercial solvers (presolve, cut selection) is one of his Roundtable Card's blind spots.
- Guests speak only through their own skills, at their own team's tier: the lead never voices a guest member. Stochastic and dynamic optimization (SD), his thesis domain, engages no delegation in `team.json`, so its agenda items stay open.
- The LP and MINLP teams' roundtables are unfilled templates (their team layer, T2, has not run), so their delegates have no team fault lines to cite and the install above leaves those two roundtables out; the council sends questions inside those solvers to the member skills (Huangfu; Sahinidis, Dey and Leyffer; Grossmann and Leyffer).
- The roundtable's six numbered fault lines are not the whole carded record: three carded critiques of his work in guest members' papers (Scheinberg's co-authored paper on optimal trees for categorical data; Burer's on the budget model for the interval TSP and on moment-based sets) are kept in his domain files' §6, and the roundtable's Honest Boundary lists them.
- Powell (d. 2015), Conn (d. 2019) and Fletcher (d. 2016), in the DFO and NLP delegations, are historical lenses; their skills reflect work up to then.
- The first session ([first-session-2026-10-31.md](first-session-2026-10-31.md)) designs its deciding tests and runs none. Its numbers come from the cards, notes and documentation it cites, and the claims its checks could not confirm are annotated in place.
- Treat every recommendation as a hypothesis to test on your problem.

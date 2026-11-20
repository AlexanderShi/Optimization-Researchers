<!-- Team README from references/team-templates/team-README.md: scaffold by scripts/new_team.py (T0), team layer by scripts/workflows/team-layer.js (T2, base tier), 2026-11-19; a rerun updates this file in place. -->

# MILP Team · Personal Research Advisors

Research-craft skills distilled from the public work of Ambros M. Gleixner, Marco E. Lübbecke, Tobias Achterberg, Matteo Fischetti, with guests John J. H. Forrest and Robert E. Bixby from the LP Team (their skills live in that team's folder), plus a roundtable skill that convenes them on your problem.

Field: mixed-integer linear programming (MILP) solver engineering and computation: LP-based branch-and-bound and branch-and-cut as built into production and research MIP codes (presolve and probing, cutting-plane families and cut management, branching and node selection, primal heuristics, conflict analysis, symmetry handling, LP re-solves and warm starts inside the tree, parallel and deterministic search, numerics, tolerances and exact rational solving), decomposition (Benders, Dantzig-Wolfe reformulation and branch-and-price), and the measurement of solver progress on model libraries (MIPLIB, customer model sets, performance variability). Not yet represented by a voice of its own: polyhedral and cutting-plane theory, MIP and machine learning, symmetry theory and constraint programming. Mixed-integer nonlinear and global optimization belong to minlp-team; LP engine internals belong to lp-team.

This selection follows the computational MILP tradition (general-purpose LP-based branch-and-cut as engineered and measured in production and research solvers, decomposition by Dantzig-Wolfe reformulation, branch-and-price and Benders, numerics and exact solving, and solver measurement on model libraries), while polyhedral and cutting-plane theory, machine learning for MIP, symmetry theory and constraint programming have no voice of their own here, and mixed-integer nonlinear and global optimization (the [MINLP Team](../minlp-team/README.md)) and LP engine internals (the [LP Team](../lp-team/README.md), the guests' home team) belong to other teams; the roundtable's "Outside the Team" section says where to go instead and which members partly cover these gaps.

## The Team

| Member | Lens · known for | Status |
|--------|------------------|--------|
| [Ambros M. Gleixner](ambros-m-gleixner/SKILL.md) | **Lens:** Can the answer be trusted, and was the comparison fair? Numerics, exact and certified solving, baseline and benchmark design, shipping inside the solver.<br>**Known for:** exact and certified LP and MILP in the open-source SCIP Optimization Suite ([SCIP](https://github.com/scipopt/scip), [SoPlex](https://github.com/scipopt/soplex), [PaPILO](https://doi.org/10.1287/ijoc.2022.0171), [VIPR](https://github.com/scipopt/vipr); PaPILO and exact SCIP's code are his group's work, mostly Gottwald's and Eifler's): iterative refinement for LP in SoPlex ([ISSAC 2012](https://doi.org/10.1145/2442829.2442858); [*INFORMS J. Comput.* 2016](https://doi.org/10.1287/ijoc.2016.0692); both in his [PhD thesis](https://doi.org/10.14279/depositonce-4938), TU Berlin 2015); [VIPR certificates](https://doi.org/10.1007/978-3-319-59250-3_13) that let a checker independent of the solver verify a MIP result (IPCO 2017); first author of [MIPLIB 2017](https://doi.org/10.1007/s12532-020-00194-3); the exact rational MIP line with Eifler ([*Math. Program.* 197, 2023](https://doi.org/10.1007/s10107-021-01749-5)), shipped as the exact mode of [SCIP 10.0](https://arxiv.org/abs/2511.18580); the rules of the [MIPcc23 competition](https://doi.org/10.1007/s12532-024-00256-w). | T1 base skill · base tier done |
| [Marco E. Lübbecke](marco-e-lubbecke/SKILL.md) | **Lens:** Is there structure worth reformulating, and how will we know before we build? Decomposition as a measured bet against the compact model, judged on instances chosen against it.<br>**Known for:** column generation, Dantzig-Wolfe reformulation and branch-and-price: the survey [*Selected Topics in Column Generation*](https://doi.org/10.1287/opre.1050.0234) with Desrosiers (2005), his most cited work; the generic decomposition solver [GCG](https://github.com/scipopt/gcg), his RWTH group's code (original design by Gerald Gamrath; [Gamrath and Lübbecke, SEA 2010](https://doi.org/10.1007/978-3-642-13193-6_21)); automatic Dantzig-Wolfe reformulation of general MIPs ([IPCO 2011](https://doi.org/10.1007/978-3-642-20807-2_4); [*Math. Program.* 149, 2015](https://doi.org/10.1007/s10107-014-0761-5)); the book [*Branch-and-Price*](https://doi.org/10.1007/978-3-031-96917-1) with Desrosiers, Desaulniers and Gauthier (Springer 2026). | T1 base skill · base tier done |
| [Tobias Achterberg](tobias-achterberg/SKILL.md) | **Lens:** Does it make a complete solver's default faster in total time on a broad library, without hurting anything outside its class?<br>**Known for:** the original author of SCIP, which he wrote alone from October 2002 ([*Math. Program. Comput.* 2009](https://doi.org/10.1007/s12532-008-0001-1)), and of the thesis [*Constraint Integer Programming*](https://doi.org/10.14279/depositonce-1634) (TU Berlin 2007); reliability branching ([*Branching rules revisited*](https://doi.org/10.1016/j.orl.2004.04.002), with Koch and Martin, 2005); [conflict analysis in MIP](https://doi.org/10.1016/j.disopt.2006.10.006) (2007); the [Mcf-separator](https://doi.org/10.1007/s12532-010-0015-3) with Raack (2010); the five-author [presolve study](https://doi.org/10.1287/ijoc.2018.0857) (2020). He joined ILOG [CPLEX](https://www.ibm.com/products/ilog-cplex-optimization-studio) in 2006 and [Gurobi](https://www.gurobi.com/) in March 2014, VP of R&D since April 2020 (as of November 2025). | T1 base skill · base tier done |
| [Matteo Fischetti](matteo-fischetti/SKILL.md) | **Lens:** Suspect the model and the loop before the component; try the smallest change around a stock solver; believe a gain only after seeds and a placebo.<br>**Known for:** co-authored general-purpose MIP heuristics and solver loops: [local branching](https://doi.org/10.1007/s10107-003-0395-5) (with Lodi, 2003); the [feasibility pump](https://doi.org/10.1007/s10107-004-0570-3) (with Glover and Lodi, 2005) and [FP 2.0](https://doi.org/10.1007/s12532-009-0007-3) (with Salvagnin, 2009); [proximity search](https://doi.org/10.1007/s10732-014-9266-x) (with Monaci, 2014); the [Benders redesign](https://doi.org/10.1287/mnsc.2016.2461) with in-out root stabilisation (with Ljubić and Sinnl, 2017); [erraticism and bet-and-run](https://doi.org/10.1287/opre.2013.1231) (with Monaci, 2014); thinned-out models ([Steiner trees](https://doi.org/10.1007/s12532-016-0111-0)) and [orbital shrinking](https://doi.org/10.1016/j.dam.2017.01.015). Honours his skill lists: Edelman Award 2008 (Netherlands Railways team), Harold Larnder Prize 2015, DIMACS Steiner challenge 2014. His code stayed mostly closed until the 2026 [fp-objective-cutoff](https://github.com/mfischetti-arch/fp-objective-cutoff) study (sole-authored, unreviewed, AI-assisted). | T1 base skill · base tier done |
| [John J. H. Forrest](../lp-team/john-j-h-forrest/SKILL.md) | **Lens (for MILP):** code-first branch-and-cut engineer: a MIP device earns its place by surviving real, hostile models as a guarded default, shipped behind a switch with a retreat keyed to its own suspicious outcome; a wrong answer or a false "infeasible" is diagnosed from the instance up (tolerances and scaling, components off one by one, the known solution); Cbc engineering, not MIP theory.<br>**Known for:** co-author of the Forrest-Tomlin basis update ([1972](https://doi.org/10.1007/BF01584548)), UMPIRE ([1974](https://doi.org/10.1287/mnsc.20.5.736)), Beale-Forrest special ordered sets ([1976](https://doi.org/10.1007/BF01580653), his most cited paper) and Forrest-Goldfarb steepest edge ([1992](https://doi.org/10.1007/BF01581089)); Sprint (sifting), credited to his 1989 talk and described with the Volume crash in the [ICM 1998 chapter](https://doi.org/10.4171/dms/1-3/65) with Anbil and Pulleyblank; wrote the simplex core of COIN-OR [Clp](https://github.com/coin-or/Clp) (2002, with the Idiot crash), Abc/Aboca (2012) and CoinFactorization ([CoinUtils](https://github.com/coin-or/CoinUtils)); [Cbc](https://github.com/coin-or/Cbc) is shared code, his by history for the early code and FPump, Greedy, Local, RINS, dynamic pseudo-costs and more (the [CBC User Guide](https://doi.org/10.1287/educ.1053.0020) with Lougee-Heimer, 2005); founding Benevolent Dictator of COIN-OR ([2005 COIN-OR INFORMS Cup](https://www.coin-or.org/coinCup/coinCup2005Winner.html)). | guest from [LP Team](../lp-team/README.md) · T1 base skill |
| [Robert E. Bixby](../lp-team/robert-e-bixby/SKILL.md) | **Lens (for MILP):** production-solver measurer and decider, on MIP for measurement and defaults only: a change ships as a default only with its losses counted, an automatic off-switch and a win over the old release at its best tuning; progress counts only as dated per-model ratios of releases rebuilt for one machine, on screened real-model libraries; on cuts, branching and heuristics he defers.<br>**Known for:** wrote the original [CPLEX](https://www.ibm.com/products/ilog-cplex-optimization-studio) simplex code (all development at the 1988 release, still developing it in 1997; his 2002 paper credits Gu, Lustig, Rothberg and Wunderling with fundamental contributions to the later LP algorithms) and co-founded CPLEX Optimization (incorporated 1987, first release 1988) and [Gurobi](https://www.gurobi.com/) (2008; CEO to 2015; no development there). By his own account CPLEX's MIP cuts and most of its presolve were Gu's and node presolve, probing and the first heuristics Rothberg's, while he put in strong branching. His MIP craft is measurement: [*MIP: Theory and Practice — Closing the Gap*](https://doi.org/10.1007/978-0-387-35514-6_2) (2000, co-signed), the [first MIPLIB report](https://doi.org/10.21236/ada455431) and [MIPLIB 3.0](https://mathopt.zib.de/Optima-Issues/optima58.pdf) (co-signed), and [*A Brief History of Linear and Mixed-Integer Programming Computation*](https://doi.org/10.4171/dms/6/16) (2012) with his late-2007 twelve-release CPLEX MIP run; for LP, [*Solving Real-World Linear Programs*](https://doi.org/10.1287/opre.50.1.3.17780) (2002). Bound shifting, which he calls his most important contribution, has no paper. | guest from [LP Team](../lp-team/README.md) · T1 base skill |
| [`milp-roundtable`](milp-roundtable/SKILL.md) | Convenes the members and guests to discuss your problem and produce a plan | roundtable |

Each member's lens is the "Lens (one line)" of the `## Roundtable Card` in that member's `SKILL.md`. A guest's card was written for both of its teams; its lens is restated here for MILP from the card's MIP part, as in the roundtable's Team table and Guest seat notes. "Known for" is taken from each `SKILL.md` (How to Use, Signature Work Anatomy, Research Trajectory, Academic Lineage and Sources), with every link checked against Crossref, DataCite, arXiv or the page itself on 2026-11-19. Status from `python3 scripts/team_status.py product/milp-team` (2026-11-19): the four members have their base-tier skills (T1), and no deep reading is planned for this team; a guest's status is its stage in its home team. No member or guest has a **student mode** (proof playbook, open problems, reading path, pre-meeting review).

## Install (Claude Code)

Copy every skill folder into your skills directory; the snippets below install the guests' folders from the LP Team (`product/lp-team/john-j-h-forrest`, `product/lp-team/robert-e-bixby`) with the team. The roundtable finds its members and guests as sibling folders, so install all of them together.

```bash
# macOS / Linux — global install
for d in product/milp-team/*/; do cp -r "${d%/}" ~/.claude/skills/; done
# guests from the LP Team: if this checkout holds git-ignored full texts, copy only git-tracked files, see product/README.md
cp -r product/lp-team/john-j-h-forrest ~/.claude/skills/
cp -r product/lp-team/robert-e-bixby ~/.claude/skills/
```
```powershell
# Windows PowerShell
Get-ChildItem product\milp-team -Directory | ForEach-Object { Copy-Item -Recurse $_.FullName "$HOME\.claude\skills\" }
# guests from the LP Team: if this checkout holds git-ignored full texts, copy only git-tracked files, see product/README.md
Copy-Item -Recurse product\lp-team\john-j-h-forrest "$HOME\.claude\skills\"
Copy-Item -Recurse product\lp-team\robert-e-bixby "$HOME\.claude\skills\"
```

Restart Claude Code so it picks up the new skills.

## Use

**Convene the whole team on a problem:**

```
> MILP Team: our new cut separator closes more root gap on 70 of our 400 customer models, but total time barely moves, results swing
  with the seed, and 3 feasible models now come back "infeasible". One engineer, three months, 32 machines: should it ship on by default?
```

Each seated member runs as **its own agent** that reads its own skill file; the main session moderates. You chair the discussion — it pauses at four checkpoints:

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
| `@Gleixner …` / `@all …` | Ask one member, or every seated member |
| `add Bixby` / `drop Fischetti` | Change who is seated |
| `pursue 2` / `round` | Pick the disagreement / run another round |
| `plan` / `autopilot` | Go to the plan now / run to the draft plan without stopping |
| `stop` | End the roundtable |

Anything else you type is passed to the seated members as new information. At the end the moderator offers to save the transcript as a markdown file.

Cost: one agent call per member per turn — about 3 per round with default seating. Runtimes without subagents fall back to a single-model simulation, and the moderator says so.

**Other modes:**

```
> MILP Team, quick: …                                    # best-fit 1–2 members, straight to plan
> MILP Team, debate Fischetti vs Lübbecke: Benders or Dantzig-Wolfe for our facility-location model?   # two lenses argue one decision
> Use the Gleixner lens on my benchmark plan: test-set rules, baselines and the speed-up table
> Use the Achterberg lens on my knock-out table for a new presolve reduction
> How would Fischetti handle a Benders cut loop that stalls at the root?   # a single member directly
> How would Bixby measure the progress between our last two solver releases?
```

Say "exit" or "end roundtable" to return to normal mode.

## Resources

Each researcher has a folder that keeps track of the resources behind that skill:

```
<researcher>/
├── SKILL.md                             # the research skill (links into the evidence ledger)
└── references/
    ├── technique-catalog.md             # transferable devices from the papers, each with card pages
    ├── research/
    │   ├── 01- … 06-*.md                # six research notes (publications, stated method, process
    │   │                                #   evidence, mentorship, critique, trajectory)
    │   ├── cards/<batch>.md             # paper cards: D1–D8, method links, verified quotes, page refs
    │   ├── cards/<batch>.digest.json    # the same cards, machine-readable
    │   ├── 07-paper-cards.md            # card index: one row per work, read level, methods linked
    │   ├── 08-deep-reading-synthesis.md # patterns, promotions and corrections drawn from all cards
    │   └── 09-evidence-ledger.md        # full evidence behind each SKILL.md item
    └── sources/
        ├── RESOURCES.md                 # tracker: every source, verified ✅ or lead ⚠️, where it was used
        ├── publications/
        │   ├── works.json               # complete publication list, cross-checked (DBLP, Crossref, arXiv)
        │   └── scholar.md               # the same list, readable, with audit notes
        ├── papers/
        │   ├── INDEX.md                 # every work: full-text status, role, read level
        │   ├── abstracts.json           # abstracts (arXiv / Crossref)
        │   ├── *.pdf                    # open full texts (git-ignored)
        │   └── txt/                     # extracted text with [[page N]] markers (git-ignored)
        ├── talks/                       # transcripts, slides, lecture notes
        ├── essays/                      # methodology writings, surveys
        ├── software/                    # notes on the researcher's software and code
        └── private/                     # git-ignored; only its README is tracked
```

The technique catalog, `cards/`, 07–09, `publications/` and `papers/` come from the deep reading, which is not planned for this team (base tier; see [DEEP-READING.md](DEEP-READING.md)), so these files are absent here (`publications/` and `papers/` exist only as empty folders): each member folder has `SKILL.md`, which cites the research notes 01–06 instead of an evidence ledger, and `RESOURCES.md`. It also holds `FIDELITY.md` (the validation record of 2026-11-14) and, under `references/research/`, `00-prior.md` (a blind prior snapshot, never a source) and `holdout.md` (primary items held out to test the skill); the Sources appendices of Gleixner's, Achterberg's and Fischetti's skills name the research notes that also hold sealed passages and say when not to open them. A member with a student mode also has `proof-playbook.md`, `open-problems.md` and `reading-path.md` under `references/`; none has one. No `private/` folder is ever published. The guests' folders, with their own notes and `RESOURCES.md`, are kept by the [LP Team](../lp-team/README.md).

To add a resource later, add a row to that researcher's `RESOURCES.md` and drop the file into the matching folder. If the resource changes a method, update the research note and `SKILL.md`. To add full texts and paper cards, run the deep tier (stages T3.1–T3.8 of the [research-team playbook](../../references/research-team-playbook.md)); [DEEP-READING.md](DEEP-READING.md) then becomes its record.

This team is configured by [team.json](team.json).

## Honest Boundary

- These are simulated lenses built from public work, not the researchers' own views.
- The research was done from web search results in November 2026, without full-text reading; each skill's Honest Boundary lists its gaps and `RESOURCES.md` marks unverified leads ⚠️. Single theses, papers, slides, code and talk captions were opened where the research notes needed them, so the pages the skills cite come from that research, not from a deep reading of the publication lists.
- John J. H. Forrest and Robert E. Bixby sit as guests from the [LP Team](../lp-team/README.md); their skills, Roundtable Cards and reading coverage are kept by that team ([../lp-team/DEEP-READING.md](../lp-team/DEEP-READING.md)).
- Treat every recommendation as a hypothesis to test on your problem.

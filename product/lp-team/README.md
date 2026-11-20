# LP Team · Personal Research Advisors

Research-craft skills distilled from the public work of Qi Huangfu, John J. H. Forrest and Robert E. Bixby, plus a roundtable skill that convenes them on your problem.

Field: linear programming solver engineering, centred on the revised simplex method and above all the dual revised simplex method (pricing and CHUZR, bound-flipping ratio tests, dual steepest edge, sparse LU factorization and its updates, hyper-sparsity, parallel simplex), together with the primal simplex, start bases and crash, sifting, and the measurement of production LP codes on real models, as built into research and production LP solvers; the MIP work of two members (John J. H. Forrest: Cbc and earlier MIP codes; Robert E. Bixby: CPLEX and Gurobi MIP progress measurement) is seated in the MILP Team (product/milp-team, where they sit as guests from lp-team) and is not this team's centre; interior-point / barrier, first-order (PDLP-type) LP, crossover and presolve are not the centre of any member's work.

This selection follows the sparse simplex tradition of production LP solvers (the dual and primal revised simplex method as built into [HiGHS](https://github.com/ERGO-Code/HiGHS), [Clp](https://github.com/coin-or/Clp) and [CPLEX](https://www.ibm.com/products/ilog-cplex-optimization-studio), with its start bases, crash and sifting, its parallel variants on shared-memory CPUs, and the measurement of LP codes on real models), while interior point with crossover, first-order LP such as [PDLP](https://arxiv.org/abs/2106.04756), presolve design and MIP are not represented by a voice of their own: the roundtable's "Outside the Team" section says where to go instead and which members partly cover them, and MIP is argued in the [MILP Team](../milp-team/README.md), where Forrest and Bixby sit as guests.

## The Team

| Member | Lens · known for | Status |
|--------|------------------|--------|
| [Qi Huangfu](qi-huangfu/SKILL.md) | **Lens:** Dual simplex implementer: an LP technique counts only by its net gain inside a state-of-the-art sparse solver, its ceiling is computed before it is built, and any algorithmic price paid for parallel scope is measured and capped.<br>**Known for:** [hsol](https://github.com/mattmilten/h2gmp), the dual revised simplex solver he wrote from scratch for his Edinburgh PhD ([*High performance simplex solver*](https://era.ed.ac.uk/handle/1842/7952), 2013, advisor J. A. J. Hall), which became the simplex core of [HiGHS](https://github.com/ERGO-Code/HiGHS); the PAMI and SIP parallel dual simplex schemes ([Huangfu and Hall, *Math. Program. Comput.* 2018](https://doi.org/10.1007/s12532-017-0130-5), the journal's [Outstanding Paper of the Year](https://www.springer.com/journal/12532/updates/17226372)); the APF, MPF and CFT basis-update techniques ([*Comput. Optim. Appl.* 2015](https://doi.org/10.1007/s10589-014-9689-1), [best paper of 2015](https://doi.org/10.1007/s10589-016-9882-5)); the parallel dual simplex he built into [FICO Xpress](https://www.fico.com/en/products/fico-xpress-optimization) (2013–18); and [COPT](https://arxiv.org/abs/2208.14314) at Cardinal Operations (2019–), where his individual contribution cannot be separated. Xpress and COPT are closed code, so the evidence for both is thin. | T1 base skill · base tier done |
| [John J. H. Forrest](john-j-h-forrest/SKILL.md) | **Lens:** Code-first simplex and branch-and-cut engineer: a device earns its place by surviving real, hostile models as a guarded default, chosen by statistics, started cheaply, finished exactly, debugged from the instance up.<br>**Known for:** the [Forrest–Tomlin basis update](https://doi.org/10.1007/BF01584548) (1972) and [Forrest–Goldfarb steepest edge](https://doi.org/10.1007/BF01581089) (1992); the [UMPIRE paper](https://doi.org/10.1287/mnsc.20.5.736) (1974, with Hirst and Tomlin; no UMPIRE code of his is visible) and [global optimization with special ordered sets](https://doi.org/10.1007/BF01580653) (1976, with Beale); the OSL papers with Tomlin ([simplex](https://doi.org/10.1147/sj.311.0011) and [interior point](https://doi.org/10.1147/sj.311.0026), 1992; OSL itself is credited to him by others); Sprint (sifting) and the Volume crash ([ICM 1998](https://doi.org/10.4171/dms/1-3/65), which credits Sprint to his 1989 talk) and the [Idiot crash](https://github.com/coin-or/Clp/blob/master/src/Idiot.hpp). His code: the simplex core of COIN-OR [Clp](https://github.com/coin-or/Clp) (first commit 2002; not all of Clp is his), Abc/Aboca (2012, the `Abc*` files in Clp's `src/`) and CoinFactorization in [CoinUtils](https://github.com/coin-or/CoinUtils); [Cbc](https://github.com/coin-or/Cbc) he shares with others. "Founding Benevolent Dictator of COIN-OR" ([COIN-OR INFORMS Cup 2005](https://www.coin-or.org/coinCup/coinCup2005Winner.html)). All his papers are co-authored. | T1 base skill · base tier done |
| [Robert E. Bixby](robert-e-bixby/SKILL.md) | **Lens:** Production-solver measurer and decider: build what a named failing real model and a user's must-have demand; count a gain only as dated per-model ratios on screened real models, losses counted.<br>**Known for:** the original [CPLEX](https://www.ibm.com/products/ilog-cplex-optimization-studio) simplex code, a classroom LP code he hardened on failing customer LPs (by his own dated statements: all development at the 1988 first release, the main parts as of April 1992, still developing in 1997); co-founding CPLEX Optimization (incorporated 1987, first release 1988) and [Gurobi](https://www.gurobi.com/) (2008; CEO to 2015; no development there); measuring LP and MIP progress across releases ([*Solving Real-World Linear Programs: A Decade and More of Progress*](https://doi.org/10.1287/opre.50.1.3.17780), *Oper. Res.* 2002; [*A Brief History of Linear and Mixed-Integer Programming Computation*](https://doi.org/10.4171/dms/6/16), *Documenta Math.* 2012); the [1992 initial-basis paper](https://doi.org/10.1287/ijoc.4.3.267); MIPLIB ([1992](https://doi.org/10.21236/ada455431) and [3.0](https://mathopt.zib.de/Optima-Issues/optima58.pdf), co-authored); [*MIP: Theory and Practice — Closing the Gap*](https://doi.org/10.1007/978-0-387-35514-6_2) (2000, co-signed). Bound shifting, which he calls his most important contribution ([Optima 101 interview](https://mathopt.zib.de/Optima-Issues/optima101.pdf)), has no paper. The MIP code he measured (CPLEX, Gurobi) is others'; his matroid theory and the joint TSP work are context only. | T1 base skill · base tier done |
| [`lp-roundtable`](lp-roundtable/SKILL.md) | Convenes the members to discuss your problem and produce a plan | roundtable |

Each lens is the "Lens (one line)" of that member's `## Roundtable Card`; "known for" is taken from each `SKILL.md` (How to Use, Signature Work Anatomy, Academic Lineage, Honest Boundary) with its authorship labels kept: a work or code named here counts as the member's only as far as his skill says. Links were checked on 2026-11-19 (DOIs at doi.org and Crossref, arXiv abstract pages, the pages and repositories themselves; the FICO Xpress page, which sits behind a bot check, through the Xpress package's PyPI record). Status from `python3 scripts/team_status.py product/lp-team` (2026-11-19): all three members are at T1 base skill (quality check 12/12, research notes 01–06 complete); this is a base-tier team, with no deep reading planned. Forrest and Bixby also sit as guests in the [MILP Team](../milp-team/README.md), which reads the MIP part of their Roundtable Cards from these folders. No member has a **student mode** (proof playbook, open problems, reading path, pre-meeting review).

## Install (Claude Code)

Copy every skill folder into your skills directory. The roundtable finds its members as sibling folders, so install all of them together.

```bash
# macOS / Linux — global install
for d in product/lp-team/*/; do cp -r "${d%/}" ~/.claude/skills/; done
```
```powershell
# Windows PowerShell
Get-ChildItem product\lp-team -Directory | ForEach-Object { Copy-Item -Recurse $_.FullName "$HOME\.claude\skills\" }
```

Restart Claude Code so it picks up the new skills.

## Use

**Convene the whole team on a problem:**

```
> LP Team: our dual simplex is 3x slower than HiGHS on 40 crew-pairing LPs (about 800 rows, 2 million columns) in a 600-LP
  test set; 2 turn infeasible with scaling off. One developer, three months, 16 cores; 10 minutes per LP; no other LP may get slower.
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
| `@Huangfu …` / `@all …` | Ask one member, or every seated member |
| `add Forrest` / `drop Bixby` | Change who is seated |
| `pursue 2` / `round` | Pick the disagreement / run another round |
| `plan` / `autopilot` | Go to the plan now / run to the draft plan without stopping |
| `stop` | End the roundtable |

Anything else you type is passed to the seated members as new information. At the end the moderator offers to save the transcript as a markdown file.

Cost: one agent call per member per turn — about 3 per round with default seating. Runtimes without subagents fall back to a single-model simulation, and the moderator says so.

**Other modes:**

```
> LP Team, quick: …                                    # best-fit 1–2 members, straight to plan
> LP Team, debate Huangfu vs Forrest: compare with Clp at parity (presolve and crash off), or at its defaults?   # two lenses argue one decision
> Use the Forrest lens on my bug report: an LP our code calls infeasible solves to optimality with scaling off
> Use the Bixby lens on our release benchmark table before the new pricing rule becomes the default
> How would Huangfu handle the choice between the Forrest–Tomlin and MPF updates for a new dual simplex?   # a single member directly
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

The technique catalog, `cards/`, 07–09, `publications/works.json` and `scholar.md`, and the contents of `papers/` come from the deep reading. **This team is base tier, with no deep reading planned, so none of those files exists here** (`papers/` is an empty folder; see [DEEP-READING.md](DEEP-READING.md)), and no `SKILL.md` links into an evidence ledger: each cites its research notes instead. Each member has `SKILL.md`, the notes 01–06 and `RESOURCES.md`. Forrest's and Bixby's `publications/` folders hold the OpenAlex pull their notes started from (`publications.md`, `abstracts.md`, pulled 2026-11-05): raw material, not an audited publication list. `talks/` holds caption or subtitle transcripts for Huangfu (JuliaCon 2022) and Bixby (CO@Work 2015, Toronto 2021, excerpts of the 2023 *Subject to* interview, and short clips from 2015–2020). No member has a student mode, so there is no `proof-playbook.md`, `open-problems.md` or `reading-path.md`. No `private/` folder is ever published.

To add a resource later, add a row to that researcher's `RESOURCES.md` and drop the file into the matching folder. If the resource changes a method, update the research note and `SKILL.md`. Full texts and paper cards come only with the deep tier, which is not planned for this team: [DEEP-READING.md](DEEP-READING.md) says how to add it.

This team is configured by [team.json](team.json). To update it, add a member or build another team like it, use the generic kit in this repository (`scripts/new_team.py`, the saved workflows in `scripts/workflows/`): see the [research-team playbook](../../references/research-team-playbook.md), whose stages T3.1–T3.8 add the deep reading.

## Honest Boundary

- These are simulated lenses built from public work, not the researchers' own views.
- The research was done from web search results and the public sources they led to (open papers, reports and theses, code repositories, decks and talk transcripts) in October and November 2026 (Huangfu on 2026-10-27, Forrest and Bixby on 2026-11-05), without full-text reading of the members' publication lists (no deep reading and no paper cards; single works were opened where the research notes needed them); each skill's Honest Boundary lists its gaps and `RESOURCES.md` marks unverified leads ⚠️.
- No member is a historical lens: team.json marks all three living. Forrest's status rests on inference from his GitHub activity in 2026, and Bixby's on the user's setting of 2026-11-08 (no dated source after his 2023 interview establishes it, and his skill states no present role).
- Treat every recommendation as a hypothesis to test on your problem.

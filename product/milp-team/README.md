<!-- Team README from references/team-templates/team-README.md: scaffold by scripts/new_team.py (T0), team layer by scripts/workflows/team-layer.js (T2, base tier), 2026-11-19; deep reading integrated by scripts/workflows/team-integrate.js (T3.8), 2026-11-28: status column, Gleixner's lens line, the technique-catalog paragraph, Resources and the Honest Boundary with the five-column coverage summary, pasted unchanged from python3 scripts/team_status.py product/milp-team --coverage --short. A rerun updates this file in place. -->

# MILP Team · Personal Research Advisors

Research-craft skills distilled from the public work of Ambros M. Gleixner, Marco E. Lübbecke, Tobias Achterberg, Matteo Fischetti, with guests John J. H. Forrest and Robert E. Bixby from the LP Team (their skills live in that team's folder), plus a roundtable skill that convenes them on your problem.

Field: mixed-integer linear programming (MILP) solver engineering and computation: LP-based branch-and-bound and branch-and-cut as built into production and research MIP codes (presolve and probing, cutting-plane families and cut management, branching and node selection, primal heuristics, conflict analysis, symmetry handling, LP re-solves and warm starts inside the tree, parallel and deterministic search, numerics, tolerances and exact rational solving), decomposition (Benders, Dantzig-Wolfe reformulation and branch-and-price), and the measurement of solver progress on model libraries (MIPLIB, customer model sets, performance variability). Not yet represented by a voice of its own: polyhedral and cutting-plane theory, MIP and machine learning, symmetry theory and constraint programming. Mixed-integer nonlinear and global optimization belong to minlp-team; LP engine internals belong to lp-team.

This selection follows the computational MILP tradition (general-purpose LP-based branch-and-cut as engineered and measured in production and research solvers, decomposition by Dantzig-Wolfe reformulation, branch-and-price and Benders, numerics and exact solving, and solver measurement on model libraries), while polyhedral and cutting-plane theory, machine learning for MIP, symmetry theory and constraint programming have no voice of their own here, and mixed-integer nonlinear and global optimization (the [MINLP Team](../minlp-team/README.md)) and LP engine internals (the [LP Team](../lp-team/README.md), the guests' home team) belong to other teams; the roundtable's "Outside the Team" section says where to go instead and which members partly cover these gaps.

## The Team

| Member | Lens · known for | Status |
|--------|------------------|--------|
| [Ambros M. Gleixner](ambros-m-gleixner/SKILL.md) | **Lens:** Can the answer be trusted, and was the comparison fair? Numerics, exact and certified solving, mixed-precision algorithms with a stated floating-point contract, baseline and benchmark design, shipping inside the solver.<br>**Known for:** exact and certified LP and MILP in the open-source SCIP Optimization Suite ([SCIP](https://github.com/scipopt/scip), [SoPlex](https://github.com/scipopt/soplex), [PaPILO](https://doi.org/10.1287/ijoc.2022.0171), [VIPR](https://github.com/scipopt/vipr); PaPILO and exact SCIP's code are his group's work, mostly Gottwald's and Eifler's): iterative refinement for LP in SoPlex ([ISSAC 2012](https://doi.org/10.1145/2442829.2442858); [*INFORMS J. Comput.* 2016](https://doi.org/10.1287/ijoc.2016.0692); both in his [PhD thesis](https://doi.org/10.14279/depositonce-4938), TU Berlin 2015); [VIPR certificates](https://doi.org/10.1007/978-3-319-59250-3_13) that let a checker independent of the solver verify a MIP result (IPCO 2017); first author of [MIPLIB 2017](https://doi.org/10.1007/s12532-020-00194-3); the exact rational MIP line with Eifler ([*Math. Program.* 197, 2023](https://doi.org/10.1007/s10107-021-01749-5)), shipped as the exact mode of [SCIP 10.0](https://arxiv.org/abs/2511.18580); the rules of the [MIPcc23 competition](https://doi.org/10.1007/s12532-024-00256-w). | T3.6 synthesized (11575 words) · deep-read |
| [Marco E. Lübbecke](marco-e-lubbecke/SKILL.md) | **Lens:** Is there structure worth reformulating, and how will we know before we build? Decomposition as a measured bet against the compact model, judged on instances chosen against it.<br>**Known for:** column generation, Dantzig-Wolfe reformulation and branch-and-price: the survey [*Selected Topics in Column Generation*](https://doi.org/10.1287/opre.1050.0234) with Desrosiers (2005), his most cited work; the generic decomposition solver [GCG](https://github.com/scipopt/gcg), his RWTH group's code (original design by Gerald Gamrath; [Gamrath and Lübbecke, SEA 2010](https://doi.org/10.1007/978-3-642-13193-6_21)); automatic Dantzig-Wolfe reformulation of general MIPs ([IPCO 2011](https://doi.org/10.1007/978-3-642-20807-2_4); [*Math. Program.* 149, 2015](https://doi.org/10.1007/s10107-014-0761-5)); the book [*Branch-and-Price*](https://doi.org/10.1007/978-3-031-96917-1) with Desrosiers, Desaulniers and Gauthier (Springer 2026). | T3.6 synthesized (11689 words) · deep-read |
| [Tobias Achterberg](tobias-achterberg/SKILL.md) | **Lens:** Does it make a complete solver's default faster in total time on a broad library, without hurting anything outside its class?<br>**Known for:** the original author of SCIP, which he wrote alone from October 2002 ([*Math. Program. Comput.* 2009](https://doi.org/10.1007/s12532-008-0001-1)), and of the thesis [*Constraint Integer Programming*](https://doi.org/10.14279/depositonce-1634) (TU Berlin 2007); reliability branching ([*Branching rules revisited*](https://doi.org/10.1016/j.orl.2004.04.002), with Koch and Martin, 2005); [conflict analysis in MIP](https://doi.org/10.1016/j.disopt.2006.10.006) (2007); the [Mcf-separator](https://doi.org/10.1007/s12532-010-0015-3) with Raack (2010); the five-author [presolve study](https://doi.org/10.1287/ijoc.2018.0857) (2020). He joined ILOG [CPLEX](https://www.ibm.com/products/ilog-cplex-optimization-studio) in 2006 and [Gurobi](https://www.gurobi.com/) in March 2014, VP of R&D since April 2020 (as of November 2025). | T3.6 synthesized (11539 words) · deep-read |
| [Matteo Fischetti](matteo-fischetti/SKILL.md) | **Lens:** Suspect the model and the loop before the component; try the smallest change around a stock solver; believe a gain only after seeds and a placebo.<br>**Known for:** co-authored general-purpose MIP heuristics and solver loops: [local branching](https://doi.org/10.1007/s10107-003-0395-5) (with Lodi, 2003); the [feasibility pump](https://doi.org/10.1007/s10107-004-0570-3) (with Glover and Lodi, 2005) and [FP 2.0](https://doi.org/10.1007/s12532-009-0007-3) (with Salvagnin, 2009); [proximity search](https://doi.org/10.1007/s10732-014-9266-x) (with Monaci, 2014); the [Benders redesign](https://doi.org/10.1287/mnsc.2016.2461) with in-out root stabilisation (with Ljubić and Sinnl, 2017); [erraticism and bet-and-run](https://doi.org/10.1287/opre.2013.1231) (with Monaci, 2014); thinned-out models ([Steiner trees](https://doi.org/10.1007/s12532-016-0111-0)) and [orbital shrinking](https://doi.org/10.1016/j.dam.2017.01.015). Honours his skill lists: Edelman Award 2008 (Netherlands Railways team), Harold Larnder Prize 2015, DIMACS Steiner challenge 2014. His code stayed mostly closed until the 2026 [fp-objective-cutoff](https://github.com/mfischetti-arch/fp-objective-cutoff) study (sole-authored, unreviewed, AI-assisted). | T3.6 synthesized (11596 words) · deep-read |
| [John J. H. Forrest](../lp-team/john-j-h-forrest/SKILL.md) | **Lens (for MILP):** code-first branch-and-cut engineer: a MIP device earns its place by surviving real, hostile models as a guarded default, shipped behind a switch with a retreat keyed to its own suspicious outcome; a wrong answer or a false "infeasible" is diagnosed from the instance up (tolerances and scaling, components off one by one, the known solution); Cbc engineering, not MIP theory.<br>**Known for:** co-author of the Forrest-Tomlin basis update ([1972](https://doi.org/10.1007/BF01584548)), UMPIRE ([1974](https://doi.org/10.1287/mnsc.20.5.736)), Beale-Forrest special ordered sets ([1976](https://doi.org/10.1007/BF01580653), his most cited paper) and Forrest-Goldfarb steepest edge ([1992](https://doi.org/10.1007/BF01581089)); Sprint (sifting), credited to his 1989 talk and described with the Volume crash in the [ICM 1998 chapter](https://doi.org/10.4171/dms/1-3/65) with Anbil and Pulleyblank; wrote the simplex core of COIN-OR [Clp](https://github.com/coin-or/Clp) (2002, with the Idiot crash), Abc/Aboca (2012) and CoinFactorization ([CoinUtils](https://github.com/coin-or/CoinUtils)); [Cbc](https://github.com/coin-or/Cbc) is shared code, his by history for the early code and FPump, Greedy, Local, RINS, dynamic pseudo-costs and more (the [CBC User Guide](https://doi.org/10.1287/educ.1053.0020) with Lougee-Heimer, 2005); founding Benevolent Dictator of COIN-OR ([2005 COIN-OR INFORMS Cup](https://www.coin-or.org/coinCup/coinCup2005Winner.html)). | guest from [LP Team](../lp-team/README.md) · T1 base skill |
| [Robert E. Bixby](../lp-team/robert-e-bixby/SKILL.md) | **Lens (for MILP):** production-solver measurer and decider, on MIP for measurement and defaults only: a change ships as a default only with its losses counted, an automatic off-switch and a win over the old release at its best tuning; progress counts only as dated per-model ratios of releases rebuilt for one machine, on screened real-model libraries; on cuts, branching and heuristics he defers.<br>**Known for:** wrote the original [CPLEX](https://www.ibm.com/products/ilog-cplex-optimization-studio) simplex code (all development at the 1988 release, still developing it in 1997; his 2002 paper credits Gu, Lustig, Rothberg and Wunderling with fundamental contributions to the later LP algorithms) and co-founded CPLEX Optimization (incorporated 1987, first release 1988) and [Gurobi](https://www.gurobi.com/) (2008; CEO to 2015; no development there). By his own account CPLEX's MIP cuts and most of its presolve were Gu's and node presolve, probing and the first heuristics Rothberg's, while he put in strong branching. His MIP craft is measurement: [*MIP: Theory and Practice — Closing the Gap*](https://doi.org/10.1007/978-0-387-35514-6_2) (2000, co-signed), the [first MIPLIB report](https://doi.org/10.21236/ada455431) and [MIPLIB 3.0](https://mathopt.zib.de/Optima-Issues/optima58.pdf) (co-signed), and [*A Brief History of Linear and Mixed-Integer Programming Computation*](https://doi.org/10.4171/dms/6/16) (2012) with his late-2007 twelve-release CPLEX MIP run; for LP, [*Solving Real-World Linear Programs*](https://doi.org/10.1287/opre.50.1.3.17780) (2002). Bound shifting, which he calls his most important contribution, has no paper. | guest from [LP Team](../lp-team/README.md) · T1 base skill |
| [`milp-roundtable`](milp-roundtable/SKILL.md) | Convenes the members and guests to discuss your problem and produce a plan | roundtable |

Each member's lens is the "Lens (one line)" of the `## Roundtable Card` in that member's `SKILL.md`; Gleixner's was widened in his card on 2026-11-28 to name mixed-precision algorithms with a stated floating-point contract, the subject of his new Method 7. A guest's card was written for both of its teams; its lens is restated here for MILP from the card's MIP part, as in the roundtable's Team table and Guest seat notes. "Known for" is taken from each `SKILL.md` (How to Use, Signature Work Anatomy, Research Trajectory, Academic Lineage and Sources), with every link checked against Crossref, DataCite, arXiv or the page itself on 2026-11-19. Status from `python3 scripts/team_status.py product/milp-team` (2026-11-28): the four members are deep-read (paper cards, deep-reading synthesis, evidence ledger, technique catalog), each skill tightened (T3.7), claim-audited and within the 13,000-word budget that `team_status.py` checks (the Answer Standard section not counted), and the team-level integration (team-integrate.js, T3.8) brought their deep reading into this README, [DEEP-READING.md](DEEP-READING.md) and the roundtable on 2026-11-28. The deep reading added a core method to two skills: Gleixner's Method 7 (write the floating-point solver's contract, prove against it, and audit it) and Lübbecke's Method 5 (certify what you deliver: an exact relaxation bounds the heuristic); Achterberg's and Fischetti's skills keep their six methods, with new evidence and steps, and Fischetti's with two new heuristics. A guest's status is its stage in its home team: both guests are at T1 (base skill) in the LP Team, a base-tier team. No member or guest has a **student mode** (proof playbook, open problems, reading path, pre-meeting review).

## Install (Claude Code)

Copy every skill folder into your skills directory; the snippets below install the guests' folders from the LP Team (`product/lp-team/john-j-h-forrest`, `product/lp-team/robert-e-bixby`) with the team. The roundtable finds its members and guests as sibling folders, so install all of them together. If this checkout holds git-ignored full texts (PDFs or `txt/` folders under the members' `references/sources/papers/`), copy only the files `git ls-files` lists, as [product/README.md](../README.md) says.

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

**Technique catalogs.** The four deep-read skills each have a `references/technique-catalog.md`: [Gleixner's](ambros-m-gleixner/references/technique-catalog.md), [Lübbecke's](marco-e-lubbecke/references/technique-catalog.md), [Achterberg's](tobias-achterberg/references/technique-catalog.md) and [Fischetti's](matteo-fischetti/references/technique-catalog.md). Each lists the transferable devices found by reading that researcher's papers in full, in four groups: proof devices (PD), design moves (DM), experiment and evaluation protocols (EP) and writing moves (WM). Each entry has a one-line "how to use it" and the paper cards, with pages, that it rests on. All four `SKILL.md` files cite catalog entries by id in their steps, and each catalog's header lists where: Gleixner's in Methods 1, 2, 4, 5 and 7 and Workflows B and D (e.g. PD1, DM3, EP8); Lübbecke's in Methods 1 and 3, Heuristics H1 and H12, Workflows B, C, E, F and G and the Routing rows on Benders and numerics (e.g. PD3, DM17, EP9); Achterberg's in all six methods, Workflows B–E, Heuristics 2, 3, 6 and 7, the RLT anatomy and the anti-patterns (e.g. PD8, DM12, EP7); Fischetti's in all six methods, the stage workflows, Heuristic 10 and the Gomory anatomy (e.g. DM1, EP26, EP31). The guests' skills, at the base tier in the LP Team, have no technique catalog. You can also ask for the catalog directly:

```
> Gleixner lens: which experiment and evaluation protocols from his technique catalog fit a fair speed-up table for our new presolve reduction against SCIP's default?
> Lübbecke lens: which design moves from his technique catalog fit a branching rule that must not break our shortest-path pricing?
```

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
    │   ├── 09-evidence-ledger.md        # full evidence behind each SKILL.md item
    │   └── 10-claim-audit.md            # sampled claim-to-card audit and its follow-up
    └── sources/
        ├── RESOURCES.md                 # tracker: every source, verified ✅ or lead ⚠️, where it was used
        ├── publications/
        │   ├── works.json               # complete publication list, cross-checked (DBLP, Crossref, arXiv)
        │   └── scholar.md               # the same list, readable, with audit notes
        ├── papers/
        │   ├── INDEX.md                 # every work: full-text status, role, read level
        │   ├── abstracts.json           # abstracts (arXiv / Crossref)
        │   ├── abstract-sources.json    # where each chased abstract came from
        │   ├── book-leads.json          # links to the open parts of books (Lübbecke, Achterberg, Fischetti)
        │   ├── *.pdf                    # open full texts (git-ignored)
        │   └── txt/                     # extracted text with [[page N]] markers (git-ignored)
        ├── talks/                       # transcripts, slides, lecture notes
        ├── essays/                      # methodology writings, surveys
        ├── software/                    # notes on the researcher's software and code
        └── private/                     # git-ignored; only its README is tracked
```

The technique catalog, `cards/`, 07–10, `publications/` and `papers/` come from the deep reading (see [DEEP-READING.md](DEEP-READING.md)); a base-tier skill has only `SKILL.md`, the notes 01–06 and `RESOURCES.md`. All four members have been deep-read, so every member folder holds the cards, 07–10, the publication list, the full-text index with `abstracts.json` and `abstract-sources.json` (`book-leads.json` for Lübbecke, Achterberg and Fischetti) and a technique catalog: [Gleixner's](ambros-m-gleixner/references/technique-catalog.md), [Lübbecke's](marco-e-lubbecke/references/technique-catalog.md), [Achterberg's](tobias-achterberg/references/technique-catalog.md), [Fischetti's](matteo-fischetti/references/technique-catalog.md). Each `SKILL.md` links its evidence ledger instead of citing only the research notes 01–06. Each folder also holds `FIDELITY.md` (the validation record of 2026-11-14, from before the deep reading) and, under `references/research/`, `00-prior.md` (a blind prior snapshot, never a source) and `holdout.md` (primary items held out to test the skill). Some files restate sealed holdout items: each skill's Sources appendix names those not to open while the skill is used or validated, among them `FIDELITY.md`, some of the research notes and card files (Gleixner's and Fischetti's `07-paper-cards.md` and card batch files, Lübbecke's `07-paper-cards.md` and three batch files, Achterberg's batch files). A member with a student mode also has `proof-playbook.md`, `open-problems.md` and `reading-path.md` under `references/`; none has one. No `private/` folder is ever published. The guests' files live in their home team's folders: their folders, with their own notes and `RESOURCES.md`, are kept by the [LP Team](../lp-team/README.md), a base-tier team, so they hold no cards, 07–10 or technique catalog.

To add a resource later, add a row to that researcher's `RESOURCES.md` and drop the file into the matching folder. If the resource changes a method, update the research note and `SKILL.md`. To add a paper's full text, follow "How to extend" in [DEEP-READING.md](DEEP-READING.md).

This team is configured by [team.json](team.json). To build another team like it, or to update this one, use the generic kit in this repository (`scripts/new_team.py`, the saved workflows in `scripts/workflows/`): see the [research-team playbook](../../references/research-team-playbook.md).

## Honest Boundary

- These are simulated lenses built from public work, not the researchers' own views.
- The research started from web search results in November 2026: the research notes 01–06 of all four members date from 2026-11-08, and the base skills were built and validated on 2026-11-14. From 2026-11-26 to 2026-11-28 it was deepened by reading each researcher's publications in full or in part wherever an open copy exists, for all four members: publication lists, open full texts and chased copies on 2026-11-26, paper cards on 2026-11-27 and 2026-11-28, and the synthesis into each skill, its tightening and a claim audit on 2026-11-28. Coverage, from each `papers/INDEX.md` (details in [DEEP-READING.md](DEEP-READING.md)):

  | Researcher | Works indexed | Read in full / in part | Abstract or metadata only (incl. unreadable) | Skipped (not the author's, or not research) |
  |---|---|---|---|---|
  | Gleixner | 103 | 90 / 2 | 8 | 3 |
  | Lübbecke | 116 | 89 / 3 | 17 | 7 |
  | Achterberg | 55 | 34 / 2 | 17 | 2 |
  | Fischetti | 202 | 130 / 1 | 67 | 4 |

  Works without an open copy are known from an abstract or metadata only. The one book whose body was read is the open-access *Branch-and-Price* (2026), Lübbecke's four-author book, whose eight chapters were read in full as rows of their own. The other books (a co-authored lexicon, whose Scholar record lists Lübbecke among its authors without saying which entries are his, and two volumes he co-edited, the CPAIOR 2011 proceedings Achterberg co-edited, Fischetti's two textbooks) have abstract cards; of the proceedings Fischetti co-edited only the front matter was read; and the free front matter or contents of several volumes is logged in `book-leads.json` but not carded, since no book-material increment (T4) has been run. The records thinnest in open copies are Fischetti's work before 2000 (most of his work of 1986–1995 is known from abstracts or metadata only) and, for Achterberg, the published versions of his papers, read through their ZIB-Reports, and his CPLEX-era works outside that series, known from abstracts; Achterberg has no Google Scholar profile, so his list comes from DBLP, ZIB OPUS, Crossref, Semantic Scholar and Google Patents. No interview, memoir or oral history is counted. Special items among the works read, each read in the voice it is written in: the SCIP Optimization Suite release reports (group voice, one series in Gleixner's synthesis); the book's chapters (joint voice), three editorial texts and the 2020 *SN Operations Research Forum* editorial with Pardalos (the editors' joint voice) and Lübbecke's sole-authored 2015 *TOP* comment; the preface of the CPAIOR 2011 late-breaking-abstracts volume Achterberg co-edited and a 2002 report whose byline has Tobias Pfender where Crossref's record of the published chapter has Achterberg (taken as his former name by inference; no text read states the change); the front matter of the IPCO 2007 proceedings and the ATMOS 2008 preface Fischetti co-edited, two of his talk decks on joint work, the works with Martina Fischetti, a separate researcher, as first author, and his 2026 papers, read with the AI share each declares. Each skill's Honest Boundary lists its gaps, and `RESOURCES.md` marks unverified leads ⚠️.
- John J. H. Forrest and Robert E. Bixby sit as guests from the [LP Team](../lp-team/README.md); their skills, Roundtable Cards and reading coverage are kept by that team ([../lp-team/DEEP-READING.md](../lp-team/DEEP-READING.md)). Both are at T1 there (base skills from web research), so they are not in the summary above, and their sides in the roundtable rest on their research notes and `SKILL.md` files, not on paper cards.
- Treat every recommendation as a hypothesis to test on your problem.

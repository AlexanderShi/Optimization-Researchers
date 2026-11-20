<!-- Team README from references/team-templates/team-README.md: scaffold by scripts/new_team.py (T0, 2026-10-10); team layer by
     scripts/workflows/team-layer.js (T2), 2026-11-19, with the deep tier in progress (Leyffer, Misener, Burer and Dey have paper
     cards; Grossmann and Sahinidis not yet). A rerun of team-layer.js updates this file in place.
     T3.8: scripts/workflows/team-integrate.js adds the technique-catalog paragraph, the deep-tier research basis and the five-column
           coverage summary, pasted unchanged from python3 scripts/team_status.py <team dir> --coverage --short. The script sums it
           from the full --coverage table, which goes unchanged into DEEP-READING.md, so the two always agree.
     The items still open are reserved for team-integrate.js (T3.8): grep -n "TODO" README.md. -->

# MINLP Team · Personal Research Advisors

Research-craft skills distilled from the public work of Ignacio E. Grossmann, Sven Leyffer, Nikolaos V. Sahinidis, Ruth Misener, Samuel Burer and Santanu S. Dey, plus a roundtable skill that convenes them on your problem.

Field: mixed-integer nonlinear programming (MINLP), including nonconvex mixed-integer quadratically constrained programs (MIQCQP): convex-MINLP decomposition (outer approximation, generalized Benders, extended cutting planes) and NLP-based branch-and-bound, generalized disjunctive programming, deterministic global optimization by spatial branch-and-bound with factorable, alphaBB, edge-concave and piecewise-linear relaxations, and conic (SDP, completely positive, SOC) relaxations and cutting planes for nonconvex quadratic programs. Not represented as voices of their own: strong formulations for indicator and conic mixed-integer sets (Atamturk, Gomez, Gunluk-Linderoth perspective line), convexification theory as a separate voice (Tawarmalani), moment/SOS polynomial hierarchies (Lasserre), constraint programming and metaheuristics, derivative-free MINLP (see dfo-team) and continuous NLP solver design (see nonlinear-team).

This selection follows the deterministic, solver-centred tradition of MINLP (outer approximation and NLP-based branch-and-bound for convex MINLP as built into [DICOPT](https://www.gams.com/latest/docs/S_DICOPT.html), [FilMINT](https://doi.org/10.1287/ijoc.1090.0373) and [Minotaur](https://github.com/coin-or/minotaur); generalized disjunctive programming with derived big-M and hull reformulations; spatial branch-and-bound in the deterministic global solvers [BARON](https://minlp.com/baron-user-manual), [GloMIQO](https://doi.org/10.1007/s10898-012-9874-7) and [ANTIGONE](https://www.gams.com/latest/docs/S_ANTIGONE.html); conic relaxations, convexification and cutting planes for nonconvex quadratic programs), while strong formulations for indicator and conic mixed-integer sets, convexification theory as a voice of its own, moment/SOS hierarchies, constraint programming and metaheuristics are not represented, and derivative-free MINLP (the [DFO Team](../dfo-team/README.md)), NLP solver design (the [Nonlinear Team](../nonlinear-team/README.md)) and pure MILP (the [MILP Team](../milp-team/README.md)) belong to other teams; the roundtable's ["Outside the Team"](minlp-roundtable/SKILL.md#outside-the-team) section says where to go instead (constraint programming and metaheuristics have no team in this kit) and which members partly cover these gaps.

## The Team

| Member | Lens · known for | Status |
|--------|------------------|--------|
| [Ignacio E. Grossmann](ignacio-e-grossmann/SKILL.md) | **Lens:** Start from a problem someone owns; write its logic before its equations; let a measured bottleneck in real models shape the algorithm; ship it where users already model; say plainly what is guaranteed.<br>**Known for:** [outer approximation](https://doi.org/10.1007/BF02592064) for MINLP (with Duran, 1986) and [DICOPT](https://doi.org/10.1016/0098-1354(89)85008-2), the GAMS MINLP solver (with Kocis, 1989; [manual](https://www.gams.com/latest/docs/S_DICOPT.html); who wrote its code is contested); [LP/NLP-based branch and bound](https://doi.org/10.1016/0098-1354(92)80028-8) for convex MINLP (with Quesada, 1992); generalized disjunctive programming from [Raman and Grossmann (1994)](https://doi.org/10.1016/0098-1354(93)E0010-7) on, with big-M and hull reformulations derived from one logic model and shipped in [LOGMIP](https://doi.org/10.1016/S0098-1354(98)00293-2) (with Vecchietti, for GAMS), [Pyomo.GDP](https://doi.org/10.1007/s11081-021-09601-7) (GDPopt, MindtPy) and [DisjunctiveProgramming.jl](https://doi.org/10.21105/jcon.00117) (he has no Pyomo commits; students and partners write the code); the eight-process synthesis instance, carried from his 1983 report into today's Pyomo tests (MINLPLib [`synthes3`](https://www.minlplib.org/synthes3.html)); MINLP for process synthesis, scheduling and enterprise-wide optimization with industrial partners (28 papers with Dow's John Wassick, 2008–2026); the [2019 review and comparison of convex-MINLP solvers](https://doi.org/10.1007/s11081-018-9411-8) and the [2026 *EJOR* history of MINLP and disjunctive programming](https://doi.org/10.1016/j.ejor.2025.07.016), both with Kronqvist and Bernal; the textbook [*Advanced Optimization for Process Systems Engineering*](https://doi.org/10.1017/9781108917834) (Cambridge 2021; not read for the skill). | T3.2 full texts (442 open) · deep reading in progress, no paper cards yet |
| [Sven Leyffer](sven-leyffer/SKILL.md) | **Lens:** The solver-builder's lens: will the nonlinear subsolver behave at every node of the tree, is the formulation one it can evaluate and converge on, and which notion does the answer certify?<br>**Known for:** [outer approximation with Fletcher](https://doi.org/10.1007/BF01581153) (1994), which treats integer nonlinearities directly and cuts off infeasible integer assignments at a phase I point; [SQP-based nonlinear branch-and-bound](https://doi.org/10.1023/A:1011241421041) (2001), branching after one QP iteration; the [filter method](https://doi.org/10.1007/s101070100244) with Fletcher (2006 Lagrange Prize; the idea is Fletcher's, and Leyffer's share cannot be separated) and their filterSQP code ([manual](https://web.archive.org/web/20080922010217/http://www.mcs.anl.gov/~leyffer/papers/SQP_manual.pdf)); [MPECs solved as NLPs](https://doi.org/10.1080/10556780410001654241) with the [MacMPEC](https://web.archive.org/web/20080920153634/http://www.mcs.anl.gov/~leyffer/macmpec/) test library; the solver frameworks [FilMINT](https://doi.org/10.1287/ijoc.1090.0373), [Minotaur](https://doi.org/10.1007/s12532-020-00196-1) ([code](https://github.com/coin-or/minotaur)) and [Uno](https://doi.org/10.1007/s12532-026-00310-9) ([code](https://github.com/cvanaret/Uno)), Minotaur carried by Mahajan and Uno by Vanaret; the IMA volume [*Mixed Integer Nonlinear Programming*](https://doi.org/10.1007/978-1-4614-1927-3), edited with Lee (2012), and the six-author [*Acta Numerica* MINLP survey](https://doi.org/10.1017/S0962492913000032) (2013); mixed-integer PDE-constrained optimization ([McCormick envelopes](https://doi.org/10.1007/s10107-024-02181-1), with Manns, 2025). | T3.6 synthesized (11736 words) · deep-read |
| [Nikolaos V. Sahinidis](nikolaos-v-sahinidis/SKILL.md) | **Lens:** Can a general deterministic solver, after aggressive domain reduction and cheap robust relaxations, certify this at defaults, and what does a whole public library with certified optima say?<br>**Known for:** [BARON](https://minlp.com/baron-user-manual), the branch-and-reduce global MINLP solver, grown from a GAMS prototype in the 1990s into a product of The Optimization Firm (founded 2001; closed code; the 2004 INFORMS Computing Society Prize and the 2006 Beale–Orchard-Hays Prize, as his group page lists them), built on [range reduction at every node](https://doi.org/10.1007/BF00138689) (Ryoo and Sahinidis, 1996), constructive convex envelopes and [polyhedral branch-and-cut](https://doi.org/10.1007/s10107-005-0581-8) (with Tawarmalani, 2005; their book [*Convexification and Global Optimization in Continuous and Mixed-Integer Nonlinear Programming*](https://doi.org/10.1007/978-1-4757-3532-1), 2002) and [hybrid LP/NLP relaxations](https://doi.org/10.1007/s12532-018-0138-5) (with Khajavirad, 2018); the [review and comparison of derivative-free solvers](https://doi.org/10.1007/s10898-012-9951-y) (with Rios, 2013), his most cited paper; [ALAMO](https://minlp.com/alamo-release-notes), which learns small algebraic surrogates from simulators ([Cozad, Sahinidis and Miller, 2014](https://doi.org/10.1002/aic.14418)); [BAM](https://minlp.com/bam-data-driven-optimizer), a data-driven optimizer launched in June 2026; co-author of [QPLIB](https://doi.org/10.1007/s12532-018-0147-4); editor-in-chief of *Mathematical Programming Computation*. | T3.2 full texts (28 open) · deep reading in progress, no paper cards yet |
| [Ruth Misener](ruth-misener/SKILL.md) | **Lens:** What structure hides in this model, which formulation between the textbook extremes fits it, and does the gain survive inside the full solver against audited, strengthened competitors?<br>**Known for:** the deterministic global solvers [GloMIQO](https://doi.org/10.1007/s10898-012-9874-7) for MIQCQP (*J. Global Optim.* Best Paper 2013) and [ANTIGONE](https://doi.org/10.1007/s10898-014-0166-2) for MINLP (her most cited work; [GAMS manual](https://www.gams.com/latest/docs/S_ANTIGONE.html)), both with Floudas; [APOGEE](https://doi.org/10.1016/j.compchemeng.2011.01.026) piecewise-linear pooling relaxations and [edge-concave MIQCQP relaxations](https://doi.org/10.1007/s10107-012-0555-6); optimization over trained models: [gradient-boosted trees](https://doi.org/10.1287/ijoc.2020.0993), [ENTMOOT](https://doi.org/10.1016/j.compchemeng.2021.107343) and [OMLT](https://arxiv.org/abs/2202.02414) (COIN-OR Cup 2022); [P-split formulations](https://doi.org/10.1007/s10107-025-02232-1) between big-M and the hull, with Kronqvist and Tsay ([CPAIOR 2021](https://doi.org/10.1007/978-3-030-78230-6_19) Distinguished Paper; *Math. Program.* 218); the Python tools [SUSPECT](https://github.com/cog-imperial/suspect) (structure detection) and [GALINI](https://github.com/cog-imperial/galini) (an extensible MINLP solver, no commits since 2022); co-author of [QPLIB](https://doi.org/10.1007/s12532-018-0147-4). | T3.6 synthesized (11596 words) · deep-read |
| [Samuel Burer](samuel-burer/SKILL.md) | **Lens:** Which convex object captures this nonconvex quadratic structure exactly, and how far is the "kitchen sink" of known relaxations from it?<br>**Known for:** [low-rank SDP factorization](https://doi.org/10.1007/s10107-002-0352-8) with Monteiro (2003) and its code [SDPLR](https://github.com/sburer/sdplr) (SIAM SIAG/OPT Test of Time Award 2023); the [completely positive representation](https://doi.org/10.1007/s10107-008-0223-z) of mixed-binary nonconvex QPs (2009, sole author); [finite SDP-based branch-and-bound](https://doi.org/10.1007/s10107-006-0080-6) for nonconvex QP with Vandenbussche (2008), whose [box-constrained version](https://doi.org/10.1007/s10589-007-9137-6) (*COAP* 2009) won the [*COAP* 2009 best paper award](https://doi.org/10.1007/s10589-010-9368-9), and the [BoxQP instances](https://github.com/sburer/BoxQP_instances) from that work, now a standard test set; the [QuadProgBB](https://github.com/sburer/QuadProgBB) solver ([Chen and Burer, 2012](https://doi.org/10.1007/s12532-011-0033-9)); [SOC-RLT constraints](https://doi.org/10.1137/110826862) for extended trust-region subproblems, with Anstreicher (2013); the [slightly lifted relaxation](https://doi.org/10.1007/s10107-024-02076-1) for ball constraints (2025, sole author); the [survey of non-convex MINLP](https://doi.org/10.1016/j.sorms.2012.08.001) with Letchford (2012). | T3.6 synthesized (13577 words > 13000: run T3.7) · deep-read |
| [Santanu S. Dey](santanu-s-dey/SKILL.md) | **Lens:** What does the solver actually do, why does it work, and what is the provable bound, measured against an exact ground truth?<br>**Known for:** integer-programming theory carried into MINLP and QCQP: [sparse cutting planes](https://doi.org/10.1007/978-3-319-07557-0_22) (IPCO 2014), leading to the [cut-selection review](https://doi.org/10.1007/s10107-018-1302-4) with Molinaro (2018) and to branch-and-bound theory; [MILP relaxations and restrictions for pooling](https://doi.org/10.1287/opre.2015.1357) with a tight factor-n guarantee (with Gupte, 2015); [strong SOCP relaxations for AC optimal power flow](https://doi.org/10.1287/opre.2016.1489) (with Kocuk and Sun, 2016; his most cited work; INFORMS ENRE Best Publication Award in Energy 2019); [mixed-integer quadratic programming is in NP](https://doi.org/10.1007/s10107-016-1036-0) (with Del Pia and Molinaro); convexification of QCQP substructures ([rank-one](https://doi.org/10.1007/s10898-019-00844-4), [aggregations of quadratics](https://doi.org/10.1137/21M1428583)); [full strong branching](https://doi.org/10.1007/s10107-023-01977-x) and the [non-monotonicity of branching rules](https://doi.org/10.1287/ijoc.2024.0709) ([code](https://doi.org/10.1287/ijoc.2024.0709.cd)); [sensitivity analysis for mixed binary QPs](https://doi.org/10.1007/s10107-025-02265-6) (with Cifuentes and Xu); the 2020 Egon Balas Prize. No solver of his own: no commit by Dey was found in any repository examined. | T3.6 synthesized (12842 words) · deep-read |
| [`minlp-roundtable`](minlp-roundtable/SKILL.md) | Convenes the members to discuss your problem and produce a plan | roundtable |

Each lens is the "Lens (one line)" of that member's `## Roundtable Card`; "known for" is taken from each `SKILL.md` (Signature Work Anatomy, Core Research Methods, Research Trajectory, Academic Lineage, Inner Tensions, Honest Boundary) and, for book and prize details, from research note 01, with every DOI and link checked on 2026-11-19 or, for the *COAP* 2009 paper added in the fix pass, on 2026-11-20 (doi.org and its citation metadata, the arXiv abstract page, the pages and repositories themselves). A work named here counts as the member's only as far as the skill says: most are co-authored. Status from `python3 scripts/team_status.py product/minlp-team` (2026-11-19): Leyffer, Misener, Burer and Dey are deep-read (paper cards, deep-reading synthesis, evidence ledger, technique catalog); Burer's skill is over the 13,000-word budget and waits for team-tighten.js (T3.7), and the team-level integration (team-integrate.js, T3.8) runs once every member is ready. Grossmann's and Sahinidis's publication lists are audited and their open full texts indexed (T3.1–T3.2), but none of their works is carded yet: their deep reading is in progress (next: team-chase.js, T3.3), and their skills cite the research notes 01–06. No member has a **student mode** (proof playbook, open problems, reading path, pre-meeting review).

## Install (Claude Code)

Copy every skill folder into your skills directory. The roundtable finds its members as sibling folders, so install all of them together. If this checkout holds git-ignored full texts (PDFs or `txt/` folders under the members' `references/sources/papers/`), copy only the files `git ls-files` lists, as [product/README.md](../README.md) says.

```bash
# macOS / Linux — global install
for d in product/minlp-team/*/; do cp -r "${d%/}" ~/.claude/skills/; done
```
```powershell
# Windows PowerShell
Get-ChildItem product\minlp-team -Directory | ForEach-Object { Copy-Item -Recurse $_.FullName "$HOME\.claude\skills\" }
```

Restart Claude Code so it picks up the new skills.

## Use

**Convene the whole team on a problem:**

```
> MINLP Team: our water-network design MINLP (40 on/off units, bilinear mixing, big-M constants of 10^6) still has a 9% gap after
  1 h of BARON; DICOPT is fast but certifies nothing and its NLPs fail at zero flow. Two months, 20 plant instances: we need a certified 1%.
```

Each seated member runs as **its own agent** that reads its own skill file; the main session moderates. You chair the discussion — it pauses at four checkpoints:

| Checkpoint | You see | You can |
|-----------|---------|---------|
| 1 · Card and seats | Problem Card, who sits and why, the controls | Correct the card, change seats, answer ≤2 questions |
| 2 · After openings | Each member's position, first experiment, risk; agreements and splits | Answer members' questions, ask anyone, pick the disagreement to argue, or go to the plan |
| 3 · After each round | Both sides' replies and the test that would settle the point | Another round, bring someone in, or move to the plan |
| 4 · Draft plan | Plan with each member's sign-off or dissent | Approve, change, or reopen a point (never skipped, even in autopilot) |

**Controls** (any time):

| Say | Effect |
|-----|--------|
| `go` | Accept the moderator's default and continue |
| `@Sahinidis …` / `@all …` | Ask one member, or every seated member |
| `add Burer` / `drop Leyffer` | Change who is seated |
| `pursue 2` / `round` | Pick the disagreement / run another round |
| `plan` / `autopilot` | Go to the plan now / run to the draft plan without stopping |
| `stop` | End the roundtable; keep the transcript |

Anything else you type is passed to the seated members as new information. At the end the moderator offers to save the transcript as a markdown file.

Cost: one agent call per member per turn — about 3 per round with default seating. Runtimes without subagents fall back to a single-model simulation, and the moderator says so.

**Other modes:**

```
> MINLP Team, quick: …                                    # best-fit 1–2 members, straight to plan
> MINLP Team, debate Grossmann vs Misener: hull, big-M or a P-split for our disjunctive process model?   # two lenses argue one decision
> Use the Sahinidis lens on my stalled BARON log and the variable bounds in my model
> Use the Misener lens on my solver comparison: five global solvers on MINLPLib and QPLIB instances, one results table
> How would Leyffer handle NLP subproblems that fail at nodes of our nonlinear branch-and-bound?   # a single member directly
> How would Grossmann handle a multiperiod planning MINLP too large for a monolithic solve?
> How would Burer certify that the SDP relaxation of our box-constrained QP is exact?
> How would Dey test whether a new cut family really shrinks the branch-and-bound tree?
```

Say "exit" or "end roundtable" to return to normal mode.

**Technique catalogs.** [TODO: keep this paragraph only once the deep tier (T3) is done; team-integrate.js (T3.8).] Each skill has a `references/technique-catalog.md`. It lists the transferable devices found by reading that researcher's papers in full ([TODO: the catalog's groups, e.g. proof devices, design moves, experiment protocols, writing moves]). Each entry has a one-line "how to use it" and the paper cards, with pages, that it rests on. [TODO: which members' `SKILL.md` steps cite catalog entries by id and which point to catalog sections.] You can also ask for the catalog directly:

```
> [TODO: two example requests, each naming a member lens and a catalog group; team-integrate.js (T3.8)]
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
    │   └── 10-claim-audit.md            # sampled claim-to-card audits and their results
    └── sources/
        ├── RESOURCES.md                 # tracker: every source, verified ✅ or lead ⚠️, where it was used
        ├── publications/
        │   ├── works.json               # complete publication list, cross-checked (DBLP, Crossref, arXiv)
        │   └── scholar.md               # the same list, readable, with audit notes
        ├── papers/
        │   ├── INDEX.md                 # every work: full-text status, role, read level
        │   ├── abstracts.json           # abstracts (arXiv / Crossref)
        │   ├── abstract-sources.json    # where each chased abstract came from
        │   ├── book-leads.json          # links to the open parts of books (front matter, chapter lists)
        │   ├── *.pdf                    # open full texts (git-ignored)
        │   └── txt/                     # extracted text with [[page N]] markers (git-ignored)
        ├── talks/                       # transcripts, slides, lecture notes
        ├── essays/                      # methodology writings, surveys
        ├── software/                    # notes on the researcher's software and code
        └── private/                     # git-ignored; only its README is tracked
```

The technique catalog, `cards/`, 07–10, `publications/` and `papers/` come from the deep reading (see [DEEP-READING.md](DEEP-READING.md)); a base-tier skill has only `SKILL.md`, the notes 01–06 and `RESOURCES.md`. **This team is mixed while its deep reading is in progress.** Leyffer, Misener, Burer and Dey have been deep-read, so their folders hold the cards, 07–10, the publication list, the full-text index with `abstracts.json` and `abstract-sources.json` (`book-leads.json` only for Leyffer and Dey), and a technique catalog: [Leyffer's](sven-leyffer/references/technique-catalog.md), [Misener's](ruth-misener/references/technique-catalog.md), [Burer's](samuel-burer/references/technique-catalog.md), [Dey's](santanu-s-dey/references/technique-catalog.md). Grossmann and Sahinidis have so far the publication list (`works.json`, `scholar.md`) and the full-text index (`papers/INDEX.md`, `abstracts.json`), but no cards, 07–10 or technique catalog, and their `SKILL.md` cites the research notes 01–06 instead of an evidence ledger. Every member has `SKILL.md`, the notes 01–06, `RESOURCES.md` and talk transcripts under `talks/`. A member with a student mode would also have `proof-playbook.md`, `open-problems.md` and `reading-path.md` under `references/`; none has one. No `private/` folder is ever published.

To add a resource later, add a row to that researcher's `RESOURCES.md` and drop the file into the matching folder. If the resource changes a method, update the research note and `SKILL.md`. To add a paper's full text, follow "How to extend" in [DEEP-READING.md](DEEP-READING.md).

This team is configured by [team.json](team.json). To build another team like it, or to update this one, use the generic kit in this repository (`scripts/new_team.py`, the saved workflows in `scripts/workflows/`): see the [research-team playbook](../../references/research-team-playbook.md).

## Honest Boundary

- These are simulated lenses built from public work, not the researchers' own views.
- The research started from web search results in October 2026: the research notes 01–06 of all six members date from 2026-10-10. The deep reading is in progress. Leyffer's, Misener's, Burer's and Dey's skills were deepened by reading their publications in full or in part wherever an open copy exists (paper cards written on 2026-10-10; folded into the skills on 2026-10-10 for Burer and Dey and on 2026-11-19 for Leyffer and Misener), and each of those skills' Honest Boundary gives its own coverage. Grossmann's and Sahinidis's publication lists are audited and their open full texts indexed, but none of their works is carded yet, so their skills still rest on web research (single reports, manuals, papers, theses and talks were opened where the notes needed them). `python3 scripts/team_status.py product/minlp-team` gives the current counts. Each skill's Honest Boundary lists its gaps and `RESOURCES.md` marks unverified leads ⚠️. [TODO: once every member is deep-read, replace this bullet with the deep-tier research basis, "The research started from web search results in <month year>. On <date> it was deepened by reading each researcher's publications in full or in part wherever an open copy exists. Coverage, from each `papers/INDEX.md` (details in [DEEP-READING.md](DEEP-READING.md)):", followed by the table below; team-integrate.js (T3.8).]

  | Researcher | Works indexed | Read in full / in part | Abstract or metadata only (incl. unreadable) | Skipped (not the author's, or not research) |
  |---|---|---|---|---|
  | [TODO: replace this header, its separator and this row with the output of `python3 scripts/team_status.py product/minlp-team --coverage --short`, pasted unchanged (the same five columns, one row per member by surname; the script sums Distinct works indexed, Read in full / in part, Abstract only + Metadata only, and Skipped from the full --coverage table). Never type a number. team-integrate.js (T3.8); team-layer.js (T2) deletes the table at the base tier.] | | | | |

  [TODO: after the table: what is not openly available (book bodies, early papers), which openly available parts of books were read (T4 increments), and any special items counted among the full reads (interviews, memoirs). End with: "Each skill's Honest Boundary lists its gaps, and `RESOURCES.md` marks unverified leads ⚠️." team-integrate.js (T3.8); deleted with the table at the base tier.]
- Treat every recommendation as a hypothesis to test on your problem.

<!-- Team README from references/team-templates/team-README.md: scaffold by scripts/new_team.py (T0, 2026-10-10); team layer by
     scripts/workflows/team-layer.js (T2), 2026-11-19, with the deep tier in progress. A rerun of team-layer.js updates this file in place.
     T3.8: scripts/workflows/team-integrate.js, 2026-11-20, for Leyffer, Misener, Burer and Dey, and rerun the same day for
           Sahinidis (Grossmann in progress, T3.2): the status line under The Team, the technique-catalog paragraph, the deep-tier
           research basis and the five-column coverage summary, pasted unchanged from python3 scripts/team_status.py <team dir>
           --coverage --short. The script sums it from the full --coverage table, which goes unchanged into DEEP-READING.md, so the
           two always agree. Rerun team-integrate.js once Grossmann finishes the synthesis (T3.6). -->

# MINLP Team · Personal Research Advisors

Research-craft skills distilled from the public work of Ignacio E. Grossmann, Sven Leyffer, Nikolaos V. Sahinidis, Ruth Misener, Samuel Burer and Santanu S. Dey, plus a roundtable skill that convenes them on your problem.

Field: mixed-integer nonlinear programming (MINLP), including nonconvex mixed-integer quadratically constrained programs (MIQCQP): convex-MINLP decomposition (outer approximation, generalized Benders, extended cutting planes) and NLP-based branch-and-bound, generalized disjunctive programming, deterministic global optimization by spatial branch-and-bound with factorable, alphaBB, edge-concave and piecewise-linear relaxations, and conic (SDP, completely positive, SOC) relaxations and cutting planes for nonconvex quadratic programs. Not represented as voices of their own: strong formulations for indicator and conic mixed-integer sets (Atamturk, Gomez, Gunluk-Linderoth perspective line), convexification theory as a separate voice (Tawarmalani), moment/SOS polynomial hierarchies (Lasserre), constraint programming and metaheuristics, derivative-free MINLP (see dfo-team) and continuous NLP solver design (see nonlinear-team).

This selection follows the deterministic, solver-centred tradition of MINLP (outer approximation and NLP-based branch-and-bound for convex MINLP as built into [DICOPT](https://www.gams.com/latest/docs/S_DICOPT.html), [FilMINT](https://doi.org/10.1287/ijoc.1090.0373) and [Minotaur](https://github.com/coin-or/minotaur); generalized disjunctive programming with derived big-M and hull reformulations; spatial branch-and-bound in the deterministic global solvers [BARON](https://minlp.com/baron-user-manual), [GloMIQO](https://doi.org/10.1007/s10898-012-9874-7) and [ANTIGONE](https://www.gams.com/latest/docs/S_ANTIGONE.html); conic relaxations, convexification and cutting planes for nonconvex quadratic programs), while strong formulations for indicator and conic mixed-integer sets, convexification theory as a voice of its own, moment/SOS hierarchies, constraint programming and metaheuristics are not represented, and derivative-free MINLP (the [DFO Team](../dfo-team/README.md)), NLP solver design (the [Nonlinear Team](../nonlinear-team/README.md)) and pure MILP (the [MILP Team](../milp-team/README.md)) belong to other teams; the roundtable's ["Outside the Team"](minlp-roundtable/SKILL.md#outside-the-team) section says where to go instead (constraint programming and metaheuristics have no team in this kit) and which members partly cover these gaps.

## The Team

| Member | Lens · known for | Status |
|--------|------------------|--------|
| [Ignacio E. Grossmann](ignacio-e-grossmann/SKILL.md) | **Lens:** Start from a problem someone owns; write its logic before its equations; let a measured bottleneck in real models shape the algorithm; ship it where users already model; say plainly what is guaranteed.<br>**Known for:** [outer approximation](https://doi.org/10.1007/BF02592064) for MINLP (with Duran, 1986) and [DICOPT](https://doi.org/10.1016/0098-1354(89)85008-2), the GAMS MINLP solver (with Kocis, 1989; [manual](https://www.gams.com/latest/docs/S_DICOPT.html); who wrote its code is contested); [LP/NLP-based branch and bound](https://doi.org/10.1016/0098-1354(92)80028-8) for convex MINLP (with Quesada, 1992); generalized disjunctive programming from [Raman and Grossmann (1994)](https://doi.org/10.1016/0098-1354(93)E0010-7) on, with big-M and hull reformulations derived from one logic model and shipped in [LOGMIP](https://doi.org/10.1016/S0098-1354(98)00293-2) (with Vecchietti, for GAMS), [Pyomo.GDP](https://doi.org/10.1007/s11081-021-09601-7) (GDPopt, MindtPy) and [DisjunctiveProgramming.jl](https://doi.org/10.21105/jcon.00117) (he has no Pyomo commits; students and partners write the code); the eight-process synthesis instance, carried from his 1983 report into today's Pyomo tests (MINLPLib [`synthes3`](https://www.minlplib.org/synthes3.html)); MINLP for process synthesis, scheduling and enterprise-wide optimization with industrial partners (28 papers with Dow's John Wassick, 2008–2026); the [2019 review and comparison of convex-MINLP solvers](https://doi.org/10.1007/s11081-018-9411-8) and the [2026 *EJOR* history of MINLP and disjunctive programming](https://doi.org/10.1016/j.ejor.2025.07.016), both with Kronqvist and Bernal; the textbook [*Advanced Optimization for Process Systems Engineering*](https://doi.org/10.1017/9781108917834) (Cambridge 2021; not read for the skill). | T3.2 full texts (442 open) · deep reading in progress, no paper cards yet |
| [Sven Leyffer](sven-leyffer/SKILL.md) | **Lens:** The solver-builder's lens: will the nonlinear subsolver behave at every node of the tree, is the formulation one it can evaluate and converge on, and which notion does the answer certify?<br>**Known for:** [outer approximation with Fletcher](https://doi.org/10.1007/BF01581153) (1994), which treats integer nonlinearities directly and cuts off infeasible integer assignments at a phase I point; [SQP-based nonlinear branch-and-bound](https://doi.org/10.1023/A:1011241421041) (2001), branching after one QP iteration; the [filter method](https://doi.org/10.1007/s101070100244) with Fletcher (2006 Lagrange Prize; the idea is Fletcher's, and Leyffer's share cannot be separated) and their filterSQP code ([manual](https://web.archive.org/web/20080922010217/http://www.mcs.anl.gov/~leyffer/papers/SQP_manual.pdf)); [MPECs solved as NLPs](https://doi.org/10.1080/10556780410001654241) with the [MacMPEC](https://web.archive.org/web/20080920153634/http://www.mcs.anl.gov/~leyffer/macmpec/) test library; the solver frameworks [FilMINT](https://doi.org/10.1287/ijoc.1090.0373), [Minotaur](https://doi.org/10.1007/s12532-020-00196-1) ([code](https://github.com/coin-or/minotaur)) and [Uno](https://doi.org/10.1007/s12532-026-00310-9) ([code](https://github.com/cvanaret/Uno)), Minotaur carried by Mahajan and Uno by Vanaret; the IMA volume [*Mixed Integer Nonlinear Programming*](https://doi.org/10.1007/978-1-4614-1927-3), edited with Lee (2012), and the six-author [*Acta Numerica* MINLP survey](https://doi.org/10.1017/S0962492913000032) (2013); mixed-integer PDE-constrained optimization ([McCormick envelopes](https://doi.org/10.1007/s10107-024-02181-1), with Manns, 2025). | T3.6 synthesized (10533 words) · deep-read |
| [Nikolaos V. Sahinidis](nikolaos-v-sahinidis/SKILL.md) | **Lens:** Can a general deterministic solver, after aggressive domain reduction and cheap robust relaxations, certify this at defaults, and what does a whole public library with certified optima say?<br>**Known for:** [BARON](https://minlp.com/baron-user-manual), the branch-and-reduce global MINLP solver, grown from a GAMS prototype in the 1990s into a product of The Optimization Firm (founded 2001; closed code; the 2004 INFORMS Computing Society Prize and the 2006 Beale–Orchard-Hays Prize, as his group page lists them), built on [range reduction at every node](https://doi.org/10.1007/BF00138689) (Ryoo and Sahinidis, 1996), the lifted outer approximation of [polyhedral branch-and-cut](https://doi.org/10.1007/s10107-005-0581-8) (with Tawarmalani, 2005; their book [*Convexification and Global Optimization in Continuous and Mixed-Integer Nonlinear Programming*](https://doi.org/10.1007/978-1-4757-3532-1), 2002) and [hybrid LP/NLP relaxations](https://doi.org/10.1007/s12532-018-0138-5) (with Khajavirad, 2018); from his 1995–2004 line of heuristics with proven quality bounds, the [strong NP-hardness](https://doi.org/10.1016/s0098-1354(01)00681-0) of the minimum-number-of-matches problem in heat-exchanger network synthesis and [approximation algorithms](https://doi.org/10.1021/ie049978l) with proven guarantees for it (with Furman, 2001 and 2004); the [review and comparison of derivative-free solvers](https://doi.org/10.1007/s10898-012-9951-y) (with Rios, 2013), his most cited paper; [ALAMO](https://minlp.com/alamo-release-notes), which learns small algebraic surrogates from simulators ([Cozad, Sahinidis and Miller, 2014](https://doi.org/10.1002/aic.14418)); [BAM](https://minlp.com/bam-data-driven-optimizer), a data-driven optimizer launched in June 2026; co-author of [QPLIB](https://doi.org/10.1007/s12532-018-0147-4); editor-in-chief of *Mathematical Programming Computation*. | T3.6 synthesized (11730 words) · deep-read |
| [Ruth Misener](ruth-misener/SKILL.md) | **Lens:** What structure hides in this model, which formulation between the textbook extremes fits it, and does the gain survive inside the full solver against audited, strengthened competitors?<br>**Known for:** the deterministic global solvers [GloMIQO](https://doi.org/10.1007/s10898-012-9874-7) for MIQCQP (*J. Global Optim.* Best Paper 2013) and [ANTIGONE](https://doi.org/10.1007/s10898-014-0166-2) for MINLP (her most cited work; [GAMS manual](https://www.gams.com/latest/docs/S_ANTIGONE.html)), both with Floudas; [APOGEE](https://doi.org/10.1016/j.compchemeng.2011.01.026) piecewise-linear pooling relaxations and [edge-concave MIQCQP relaxations](https://doi.org/10.1007/s10107-012-0555-6); optimization over trained models: [gradient-boosted trees](https://doi.org/10.1287/ijoc.2020.0993), [ENTMOOT](https://doi.org/10.1016/j.compchemeng.2021.107343) and [OMLT](https://arxiv.org/abs/2202.02414) (COIN-OR Cup 2022); [P-split formulations](https://doi.org/10.1007/s10107-025-02232-1) between big-M and the hull, with Kronqvist and Tsay ([CPAIOR 2021](https://doi.org/10.1007/978-3-030-78230-6_19) Distinguished Paper; *Math. Program.* 218); the Python tools [SUSPECT](https://github.com/cog-imperial/suspect) (structure detection) and [GALINI](https://github.com/cog-imperial/galini) (an extensible MINLP solver, no commits since 2022); co-author of [QPLIB](https://doi.org/10.1007/s12532-018-0147-4). | T3.6 synthesized (10393 words) · deep-read |
| [Samuel Burer](samuel-burer/SKILL.md) | **Lens:** Which convex object captures this nonconvex quadratic structure exactly, and how far is the "kitchen sink" of known relaxations from it?<br>**Known for:** [low-rank SDP factorization](https://doi.org/10.1007/s10107-002-0352-8) with Monteiro (2003) and its code [SDPLR](https://github.com/sburer/sdplr) (SIAM SIAG/OPT Test of Time Award 2023); the [completely positive representation](https://doi.org/10.1007/s10107-008-0223-z) of mixed-binary nonconvex QPs (2009, sole author); [finite SDP-based branch-and-bound](https://doi.org/10.1007/s10107-006-0080-6) for nonconvex QP with Vandenbussche (2008), whose [box-constrained version](https://doi.org/10.1007/s10589-007-9137-6) (*COAP* 2009) won the [*COAP* 2009 best paper award](https://doi.org/10.1007/s10589-010-9368-9), and the [BoxQP instances](https://github.com/sburer/BoxQP_instances) from that work, now a standard test set; the [QuadProgBB](https://github.com/sburer/QuadProgBB) solver ([Chen and Burer, 2012](https://doi.org/10.1007/s12532-011-0033-9)); [SOC-RLT constraints](https://doi.org/10.1137/110826862) for extended trust-region subproblems, with Anstreicher (2013); the [slightly lifted relaxation](https://doi.org/10.1007/s10107-024-02076-1) for ball constraints (2025, sole author); the [survey of non-convex MINLP](https://doi.org/10.1016/j.sorms.2012.08.001) with Letchford (2012). | T3.6 synthesized (12383 words) · deep-read |
| [Santanu S. Dey](santanu-s-dey/SKILL.md) | **Lens:** What does the solver actually do, why does it work, and what is the provable bound, measured against an exact ground truth?<br>**Known for:** integer-programming theory carried into MINLP and QCQP: [sparse cutting planes](https://doi.org/10.1007/978-3-319-07557-0_22) (IPCO 2014), leading to the [cut-selection review](https://doi.org/10.1007/s10107-018-1302-4) with Molinaro (2018) and to branch-and-bound theory; [MILP relaxations and restrictions for pooling](https://doi.org/10.1287/opre.2015.1357) with a tight factor-n guarantee (with Gupte, 2015); [strong SOCP relaxations for AC optimal power flow](https://doi.org/10.1287/opre.2016.1489) (with Kocuk and Sun, 2016; his most cited work; INFORMS ENRE Best Publication Award in Energy 2019); [mixed-integer quadratic programming is in NP](https://doi.org/10.1007/s10107-016-1036-0) (with Del Pia and Molinaro); convexification of QCQP substructures ([rank-one](https://doi.org/10.1007/s10898-019-00844-4), [aggregations of quadratics](https://doi.org/10.1137/21M1428583)); [full strong branching](https://doi.org/10.1007/s10107-023-01977-x) and the [non-monotonicity of branching rules](https://doi.org/10.1287/ijoc.2024.0709) ([code](https://doi.org/10.1287/ijoc.2024.0709.cd)); [sensitivity analysis for mixed binary QPs](https://doi.org/10.1007/s10107-025-02265-6) (with Cifuentes and Xu); the 2020 Egon Balas Prize. No solver of his own: no commit by Dey was found in any repository examined. | T3.6 synthesized (11639 words) · deep-read |
| [`minlp-roundtable`](minlp-roundtable/SKILL.md) | Convenes the members to discuss your problem and produce a plan | roundtable |

Each lens is the "Lens (one line)" of that member's `## Roundtable Card`; "known for" is taken from each `SKILL.md` (Signature Work Anatomy, Core Research Methods, Research Trajectory, Academic Lineage, Inner Tensions, Honest Boundary) and, for book and prize details, from research note 01, with every DOI and link checked on 2026-11-19 or, for the *COAP* 2009 paper added in the fix pass and the two Furman–Sahinidis papers added when Sahinidis was integrated, on 2026-11-20 (doi.org and its citation metadata, the arXiv abstract page, the pages and repositories themselves). A work named here counts as the member's only as far as the skill says: most are co-authored. Status from `python3 scripts/team_status.py product/minlp-team` (2026-11-20): Leyffer, Sahinidis, Misener, Burer and Dey are deep-read (paper cards, deep-reading synthesis, evidence ledger, technique catalog), and the team-level integration (team-integrate.js, T3.8) brought their deep reading into this README, [DEEP-READING.md](DEEP-READING.md) and the roundtable on 2026-11-20, Sahinidis's in a rerun the same day. All five are within the 13,000-word budget, which from 2026-11-20 leaves out the Answer Standard section that `answer_standard.py` writes into every skill (`answer_standard.py --words`), so Burer needs no tighten step (T3.7). Grossmann's publication list is audited and his open full texts indexed (T3.1–T3.2), but none of his works is carded yet: his deep reading is in progress (next: team-chase.js, T3.3), his skill cites the research notes 01–06, and team-integrate.js runs again once he finishes the synthesis. No member has a **student mode** (proof playbook, open problems, reading path, pre-meeting review).

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

**Technique catalogs.** The five deep-read skills each have a `references/technique-catalog.md`: [Leyffer's](sven-leyffer/references/technique-catalog.md), [Sahinidis's](nikolaos-v-sahinidis/references/technique-catalog.md), [Misener's](ruth-misener/references/technique-catalog.md), [Burer's](samuel-burer/references/technique-catalog.md) and [Dey's](santanu-s-dey/references/technique-catalog.md). Each lists the transferable devices found by reading that researcher's papers in full, in four groups: proof devices (P), design moves (D), experiment and evaluation protocols (E; V in Leyffer's, so they are not confused with the evidence items of his research note 03) and writing moves (W; WM in Misener's, so that a bare W id means one of her written statements; Sahinidis's numbers its groups PD, DM, EP and WM). Burer's adds a table of the exactness results on his record, each with its hypothesis. Each entry has a one-line "how to use it" and the paper cards, with pages, that it rests on. All five `SKILL.md` files cite catalog entries by id in their steps (e.g. D7, V7, WM1, E11, DM13): Leyffer's, Sahinidis's, Misener's and Dey's in their core methods and workflows, Burer's mainly in his stage workflows, with a few in Methods 1–3. Burer's also points to the exactness table. Leyffer's, Misener's, Burer's and Dey's point to their writing moves for drafting (Burer's in Workflow E); Sahinidis's lists WM1–WM13 among the stages without a distillable method (moves listed rather than distilled) and cites WM10 (manuals put the contract first) in Workflow E step 3. Grossmann's deep reading is in progress, so his skill has no technique catalog yet. You can also ask for the catalog directly:

```
> Misener lens: which design moves from her technique catalog fit a formulation between big-M and the hull for our disjunctive model?
> Leyffer lens: which experiment and evaluation protocols from his technique catalog fit a fair comparison of our NLP-based branch-and-bound with Bonmin?
> Sahinidis lens: which experiment and evaluation protocols from his technique catalog fit a fair test of our new bound-tightening routine against BARON, Couenne and SCIP?
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

The technique catalog, `cards/`, 07–10, `publications/` and `papers/` come from the deep reading (see [DEEP-READING.md](DEEP-READING.md)); a base-tier skill has only `SKILL.md`, the notes 01–06 and `RESOURCES.md`. **This team is mixed while its deep reading is in progress.** Leyffer, Sahinidis, Misener, Burer and Dey have been deep-read, so their folders hold the cards, 07–10, the publication list, the full-text index with `abstracts.json` and `abstract-sources.json` (`book-leads.json` only for Leyffer, Sahinidis and Dey), and a technique catalog: [Leyffer's](sven-leyffer/references/technique-catalog.md), [Sahinidis's](nikolaos-v-sahinidis/references/technique-catalog.md), [Misener's](ruth-misener/references/technique-catalog.md), [Burer's](samuel-burer/references/technique-catalog.md), [Dey's](santanu-s-dey/references/technique-catalog.md). Grossmann has so far the publication list (`works.json`, `scholar.md`) and the full-text index (`papers/INDEX.md`, `abstracts.json`), but no cards, 07–10 or technique catalog, and his `SKILL.md` cites the research notes 01–06 instead of an evidence ledger. Every member has `SKILL.md`, the notes 01–06, `RESOURCES.md` and talk transcripts under `talks/`. A member with a student mode would also have `proof-playbook.md`, `open-problems.md` and `reading-path.md` under `references/`; none has one. No `private/` folder is ever published.

To add a resource later, add a row to that researcher's `RESOURCES.md` and drop the file into the matching folder. If the resource changes a method, update the research note and `SKILL.md`. To add a paper's full text, follow "How to extend" in [DEEP-READING.md](DEEP-READING.md).

This team is configured by [team.json](team.json). To build another team like it, or to update this one, use the generic kit in this repository (`scripts/new_team.py`, the saved workflows in `scripts/workflows/`): see the [research-team playbook](../../references/research-team-playbook.md).

## Honest Boundary

- These are simulated lenses built from public work, not the researchers' own views.
- The research started from web search results in October 2026: the research notes 01–06 of all six members date from 2026-10-10. It was then deepened by reading each researcher's publications in full or in part wherever an open copy exists, so far for five members: Burer's and Dey's skills on 2026-10-10, Leyffer's and Misener's with paper cards written on 2026-10-10 and folded into the skills on 2026-11-19, and Sahinidis's with paper cards written and folded into the skill on 2026-11-20. Grossmann's deep reading is in progress: his publication list is audited and his open full texts indexed (stage T3.2), but none of his works is carded yet, so his skill still rests on web research (single reports, manuals, papers, theses and talks were opened where the notes needed them) and his row below shows nothing read. Coverage, from each `papers/INDEX.md` (details in [DEEP-READING.md](DEEP-READING.md)):

  | Researcher | Works indexed | Read in full / in part | Abstract or metadata only (incl. unreadable) | Skipped (not the author's, or not research) |
  |---|---|---|---|---|
  | Grossmann | 1312 | 0 / 0 | 0 | 140 |
  | Leyffer | 211 | 120 / 35 | 49 | 7 |
  | Sahinidis | 381 | 110 / 5 | 155 | 111 |
  | Misener | 147 | 77 / 23 | 45 | 2 |
  | Burer | 71 | 52 / 15 | 4 | 0 |
  | Dey | 156 | 93 / 30 | 31 | 2 |

  ⚠️ 1172 indexed works have no card yet (Read column empty); the table is not final.

  The warning counts the 1172 rows of Grossmann that are neither carded nor skipped (`team_status.py`, Unread rows); the rows of the other five are final. Sahinidis's skipped rows are talks, a patent, two research works of his own whose own texts were not available and whose files turned out to hold the texts of two other works of his (S040 and S167), and rows that are not his works or not research. Works without an open copy are known from an abstract or metadata only, and no book body was read: Leyffer's IMA volume *Mixed Integer Nonlinear Programming* (edited with Lee) and Sahinidis's book with Tawarmalani have abstract cards and Dey's proceedings volumes have metadata cards, while the free front matter of these volumes (for Sahinidis's book, on his coauthor's book page) is logged in their `book-leads.json` but not carded, since no book-material increment (T4) has been run. The early record is the thinnest in open copies: Misener's 2009–2012 pooling and gas-lift papers, Dey's PhD thesis and several early group-relaxation papers and Burer's PhD thesis have no open text; Grossmann's index holds no open text for his work before 1990, Sahinidis's none for his work before 1996, so the founding branch-and-reduce papers of 1995–96 are known from abstracts. Several of Leyffer's files, most of them filter and MPEC theory papers, have broken text layers and await OCR. Special items among the works read, each read in the voice it is written in: Leyffer's 2015 OPTIMA interview of Roger Fletcher (Leyffer asks the questions; the answers are Fletcher's), his 2017 newsletter article, the SIAG/OPT Views-and-News issues he edited (only his editor's notes are his voice) and four committee or community reports he contributed to (S025, S133, S163, S193: the committees' voice, not his); Misener's two single-author essays, the 2016 memorial essay on Floudas (S143) and a 2014 CPSE newsletter piece (S145), and the MEng reports of two students she supervised (S100, S117), counted among her works read in part and read as the students' voice; Dey's three guest editorials (S094, S113, S115: the guest editors' joint voice) and the discussion column by Cornuéjols, Weismantel and Wolsey in the file of his 2009 *Optima* survey (S079); Burer's *COAP* 2009 best-paper award note, an unsigned note that his card reads as the awardees' own retrospective, and the SDPLR user's guide; Sahinidis's BARON manuals (user manuals under his sole author line, GAMS solver chapters with Tawarmalani; read as solver documentation, the skill marking their rules as The Optimization Firm's), his 1996 book review, his editorial, status report and Rosenbrock Prize notices as editor-in-chief of *Optimization and Engineering* (2018–2023; the prize citations are the committees' text), two guest editors' prefaces (the editors' joint voice), a profile of Grossmann co-signed by four CMU colleagues (their collective voice) and a 2017 company report on ALAMO and other tools, whose only text of his is two signed brochures. No memoir or oral history is counted. Each skill's Honest Boundary lists its gaps, and `RESOURCES.md` marks unverified leads ⚠️.
- Treat every recommendation as a hypothesis to test on your problem.

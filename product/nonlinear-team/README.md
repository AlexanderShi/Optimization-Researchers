# Nonlinear Team · Personal Research Advisors

Research-craft skills distilled from the public work of Frank E. Curtis, Jorge Nocedal, Stephen J. Wright, Yinyu Ye, Andreas Wächter, Philip E. Gill, Philippe L. Toint, Nicholas I. M. Gould, Roger Fletcher, Yurii Nesterov and Daniel P. Robinson, plus a roundtable skill that convenes them on your problem.

Field: continuous nonlinear optimization and NLP solver design (interior-point, SQP and active-set, trust-region and regularization, quasi-Newton, penalty / augmented-Lagrangian / filter globalization, complexity of first- and second-order methods); mixed-integer, global, derivative-free (see dfo-team) and conic first-order splitting traditions are not represented.

This selection follows the smooth NLP solver tradition (interior-point and SQP / active-set codes, trust-region and regularization methods, quasi-Newton updates, penalty, filter and funnel globalization, with Ye and Nesterov adding interior-point and complexity theory, and with nonsmooth BFGS-SQP (Curtis) and active-set methods for ℓ1 and group-sparse regularizers (Robinson) at its edge), while mixed-integer NLP, certified global optimization, derivative-free and noisy black-box optimization (the [DFO Team](../dfo-team/README.md)) and first-order splitting for LP, QP or conic problems too large to factorize are not represented; the roundtable's "Outside the Team" section says where to go instead and which members partly cover them.

## The Team

| Member | Lens · known for | Status |
|--------|------------------|--------|
| [Frank E. Curtis](frank-e-curtis/SKILL.md) | **Lens:** make the inner solve and the penalty or merit update serve the globalization, guard the fast incumbent instead of replacing it, and prove it on instances built to break the solver.<br>**Known for:** [inexact SQP](https://doi.org/10.1137/060674004) and [infeasibility-detecting SQP](https://doi.org/10.1137/080738222) with Byrd and Nocedal; the penalty-interior-point code [PIPAL](https://doi.org/10.1007/s12532-012-0041-4); [SQP-GS](https://doi.org/10.1137/090780201) → [BFGS-SQP with relative minimization profiles](https://doi.org/10.1080/10556788.2016.1208749) (2018 INFORMS Computing Society Prize); the [TRACE](https://doi.org/10.1007/s10107-016-1026-2) trust region; [NonOpt](https://doi.org/10.1007/s12532-026-00322-5); co-author of the [SIAM Review survey on optimization for large-scale machine learning](https://doi.org/10.1137/16M1080173). | T3 deep tier done (T3.6 synthesized; [DEEP-READING.md](DEEP-READING.md)) |
| [Jorge Nocedal](jorge-nocedal/SKILL.md) | **Lens:** put the solver's received wisdom on trial with handicapped, method-level benchmarks; keep the classical engine and repair only the failing component, driven by an explicit estimate and a recovery path.<br>**Known for:** [L-BFGS](https://doi.org/10.1007/BF01589116) and L-BFGS-B ([2011 Remark](https://doi.org/10.1145/2049662.2049669)); [KNITRO](https://doi.org/10.1007/0-387-30065-1_4) with Byrd and Waltz; [*Numerical Optimization*](https://doi.org/10.1007/978-0-387-40065-5) with S. J. Wright; the [*Acta Numerica* 1992 theory survey](https://doi.org/10.1017/S0962492900002270); quasi-Newton methods for noisy functions ([2019](https://doi.org/10.1137/18M1177718)). | T3 deep tier done (T3.6 synthesized, T3.7 tightened, two T4 increments; new Method 7, curvature gets its own cheap sample; [DEEP-READING.md](DEEP-READING.md)) |
| [Stephen J. Wright](stephen-j-wright/SKILL.md) | **Lens:** find where solver and theory disagree (degeneracy, roundoff, warm starts), show it on the smallest instance, heuristics off, borrow a neighbouring class's fix, keep only safeguards beating a no-safeguard twin.<br>**Known for:** [*Primal-Dual Interior-Point Methods*](https://doi.org/10.1137/1.9781611971453); *Numerical Optimization* with Nocedal; [stabilized SQP for degenerate solutions](https://doi.org/10.1023/A:1018665102534); [finite-precision analysis of interior-point methods](https://doi.org/10.1137/S1052623498347438); the LP/QP codes [PCx](https://doi.org/10.1080/10556789908805757) and [OOQP](https://doi.org/10.1145/641876.641880); [trust-region Newton-CG with complexity guarantees](https://doi.org/10.1137/19M130563X); [*Optimization for Data Analysis*](https://doi.org/10.1017/9781009004282) with Recht. | T1 base skill · base tier done |
| [Yinyu Ye](yinyu-ye/SKILL.md) | **Lens:** LP interior-point lens: make the solver certify its own failures (homogenize or go one-phase), swap the costly inner step for a cheaper provable primitive, settle trusted heuristics by proof or smallest counterexample.<br>**Known for:** the [homogeneous self-dual LP algorithm](https://doi.org/10.1287/moor.19.1.53) with Todd and Mizuno; the books [*Interior Point Algorithms*](https://doi.org/10.1002/9781118032701) and [*Linear and Nonlinear Programming*](https://doi.org/10.1007/978-3-030-85450-8) (with Luenberger); [strongly polynomial simplex and policy iteration for fixed-discount MDPs](https://doi.org/10.1287/moor.1110.0516); the [one-phase nonconvex IPM](https://arxiv.org/abs/1801.03072) with Hinder; the [DRSOM](https://arxiv.org/abs/2208.00208) → [HSODM](https://doi.org/10.1287/moor.2023.0132) second-order line. | T1 base skill · base tier done |
| [Andreas Wächter](andreas-wachter/SKILL.md) | **Lens:** the maintainer-theorist of a general-purpose IPM: defaults provable, heuristics labelled and ablated, failures reduced to a model defect or a minimal counterexample, claims tested against the same code without its safeguards.<br>**Known for:** Ipopt: the [filter line-search method](https://doi.org/10.1137/S1052623403426556) and its [implementation paper](https://doi.org/10.1007/s10107-004-0559-y) with Biegler, and the C++ Ipopt 3.x with Laird (Wilkinson Prize 2011); the [2000 failure-of-global-convergence counterexample](https://doi.org/10.1007/PL00011386); the [inexact-step IPM](https://doi.org/10.1137/090747634) with Curtis and Schenk; [two-stage decomposition for AC optimal power flow](https://doi.org/10.1109/TPWRS.2020.3002189). At [Gurobi](https://www.gurobi.com/) since late 2024. | T1 base skill · base tier done |
| [Philip E. Gill](philip-e-gill/SKILL.md) | **Lens:** the linear system decides the method: well-pose each subproblem by the smallest solution-keeping change; keep warm starts and infeasibility detection; test whole collections, failures typed.<br>**Known for:** [SNOPT](https://doi.org/10.1137/S1052623499350013) with Murray and Saunders ([SIGEST 2005](https://doi.org/10.1137/S0036144504446096)); *Practical Optimization* (1981, with Murray and M. H. Wright; [SIAM reprint](https://doi.org/10.1137/1.9781611975604)); the [1986 projected-Newton-barrier / Karmarkar equivalence](https://doi.org/10.1007/BF02592025); the [interior-methods survey](https://doi.org/10.1137/S0036144502414942); [globalized stabilized SQP](https://doi.org/10.1137/120882913) and the shifted penalty-barrier line; an [LDLᵀ trust-region quasi-Newton method](https://doi.org/10.1137/23M1623380). All co-authored, with alphabetical author order. | T1 base skill · base tier done |
| [Philippe L. Toint](philippe-l-toint/SKILL.md) | **Lens:** let Newton be Newton, then try to break your own bound: the least obstructive safeguard with a proof, a constructed function attaining the bound, defaults from one-change experiments on a validated shared collection.<br>**Known for:** co-author of [LANCELOT](https://doi.org/10.1007/978-3-662-12211-2) (1994 Beale–Orchard-Hays Prize), [CUTE](https://doi.org/10.1145/200979.201043) → [CUTEst](https://doi.org/10.1007/s10589-014-9687-3) and [*Trust-Region Methods*](https://doi.org/10.1137/1.9780898719857); [adaptive cubic regularization (ARC)](https://doi.org/10.1007/s10107-009-0286-5) and the [evaluation-complexity book](https://doi.org/10.1137/1.9781611976991) with Cartis and Gould; [filter-SQP convergence theory](https://doi.org/10.1137/S105262340038081X) (2006 Lagrange Prize with Fletcher and Leyffer); the [trust funnel](https://doi.org/10.1007/s10107-008-0244-7); [S2MPJ](https://doi.org/10.1080/10556788.2025.2490640), most of whose code he writes himself. | T1 base skill · base tier done |
| [Nicholas I. M. Gould](nicholas-i-m-gould/SKILL.md) | **Lens:** find the dominant inner solve (KKT, QP, trust-region subproblem) and make it truncatable; judge one change in one harness, whole collection at defaults; promote only survivors; exit a route in print when rivals' benchmarks say it has peaked.<br>**Known for:** co-author of LANCELOT, [GALAHAD](https://doi.org/10.1145/962437.962438) and CUTE → CUTEst (with Conn, Toint, Orban) and of the books *Trust-Region Methods* (2000) and *Evaluation Complexity* (2022); the trust-region subproblem solvers [GLTR](https://doi.org/10.1137/S1052623497322735), [TRS/RQS](https://doi.org/10.1007/s12532-010-0011-7) and [TREK](https://arxiv.org/abs/2511.11135); ARC with Cartis and Toint; at Harwell/RAL since 1985. | T1 base skill · base tier done |
| [Roger Fletcher](roger-fletcher/SKILL.md) | **Lens:** let Newton run: measure what safeguards throw away, add the least protection that still guarantees convergence, trust nothing not computed in finite precision in your own code.<br>**Known for:** [DFP](https://doi.org/10.1093/comjnl/6.2.163) (with Powell, 1963), [Fletcher–Reeves](https://doi.org/10.1093/comjnl/7.2.149) (1964) and [BFGS](https://doi.org/10.1093/comjnl/13.3.317) (1970); Sl1QP exact-penalty SQP and [SLP-EQP](https://doi.org/10.1007/BF01582292); the [filter method](https://doi.org/10.1007/s101070100244) with Leyffer (2006 Lagrange Prize); [*Practical Methods of Optimization*](https://doi.org/10.1002/9781118723203); [projected Barzilai–Borwein](https://doi.org/10.1007/s00211-004-0569-y) (with Dai), [limited-memory steepest descent](https://doi.org/10.1007/s10107-011-0479-6) and [SLCP](https://doi.org/10.1137/110844362) with the filterSD code. Historical lens (1939–2016). | T1 base skill · base tier done |
| [Yurii Nesterov](yurii-nesterov/SKILL.md) | **Lens:** structure and complexity: which class is provably easy, one iteration's cost in affordable operations, the rate's distance from the lower bound, unknowable constants.<br>**Known for:** the [1983 fast gradient method](https://zbmath.org/?q=an:0535.90071); [self-concordant polynomial-time interior-point theory](https://doi.org/10.1137/1.9781611970791) with Nemirovskii; [smoothing](https://doi.org/10.1007/s10107-004-0552-5); [cubic regularization of Newton's method](https://doi.org/10.1007/s10107-006-0706-8) with Polyak; [implementable tensor methods](https://doi.org/10.1007/s10107-019-01449-1); [super-universal regularized Newton](https://doi.org/10.1137/22M1519444); [*Lectures on Convex Optimization*](https://doi.org/10.1007/978-3-319-91578-4). A theorist who never released a solver; 2009 von Neumann Prize (shared with Ye), 2026 Gauss Prize. | T1 base skill · base tier done |
| [Daniel P. Robinson](daniel-p-robinson/SKILL.md) | **Lens:** assume only what the running solver can check; be the incumbent where it works and converge provably where it fails; get speed from subspaces a computable test can enlarge.<br>**Known for:** the [second-derivative SQP method](https://doi.org/10.1137/080744542) with Gould (its GALAHAD package S2QP was never released and sits in [`oblivion`](https://github.com/ralna/GALAHAD/tree/master/src/oblivion)); the primal-dual augmented Lagrangian line of his [thesis](https://escholarship.org/uc/item/8hz1b6q0) with Gill, up to [globalized stabilized SQP](https://doi.org/10.1137/120882913), and his sole-authored [*TOP* 2015 comment](https://doi.org/10.1007/s11750-015-0371-2) against assuming which subproblem solution is computed; the [adaptive augmented Lagrangian](https://doi.org/10.1007/s10107-014-0784-y) with Curtis and Jiang (steering [added to LANCELOT](https://doi.org/10.1080/10556788.2015.1071813)); the restoration-free [filter SQP](https://doi.org/10.1137/130920599) with Gould and Loh; the reduced-space methods [FaRSA](https://doi.org/10.1137/16M1062259) and [FaRSA-Group](https://doi.org/10.1137/21M1411111) for ℓ1 and group sparsity; the GALAHAD subproblem solvers TRS, RQS, CQP and [DQP](https://doi.org/10.1007/s10589-016-9886-1), Gould principal author; with Curtis, [TRACE](https://doi.org/10.1007/s10107-016-1026-2), [regional complexity](https://doi.org/10.1007/s10107-020-01492-3), [stochastic SQP](https://doi.org/10.1137/20M1354556) and the book [*Practical Nonconvex Nonsmooth Optimization*](https://doi.org/10.1137/1.9781611978599) (SIAM 2025, not read for the skill). After 2016 most of his stated positions are co-signed with Curtis. | T1 base skill · base tier done |
| [`nonlinear-roundtable`](nonlinear-roundtable/SKILL.md) | Convenes the members to discuss your problem and produce a plan | roundtable |

Each lens is the "Lens (one line)" of that member's `## Roundtable Card`; "known for" is taken from each `SKILL.md` (its introduction and Signature Work Anatomy) and its research notes, with links checked against Crossref, arXiv or the page itself (all re-checked on 2026-10-17). Status from `python3 scripts/team_status.py product/nonlinear-team` (2026-10-17): Curtis (2026-10-10) and Nocedal (2026-10-16 to 2026-10-17, with two increments: OCR re-reads and the open parts of *Numerical Optimization*) are deep-read; the other nine members are base tier, deep reading not started. Robinson joined on 2026-10-17; the coverage tables in [DEEP-READING.md](DEEP-READING.md) and below were re-run that day. No member has a **student mode** (proof playbook, open problems, reading path, pre-meeting review).

## Install (Claude Code)

Copy every skill folder into your skills directory. The roundtable finds its members as sibling folders, so install all of them together.

```bash
# macOS / Linux — global install
for d in product/nonlinear-team/*/; do cp -r "$d" ~/.claude/skills/; done
```
```powershell
# Windows PowerShell
Get-ChildItem product\nonlinear-team -Directory | ForEach-Object { Copy-Item -Recurse $_.FullName "$HOME\.claude\skills\" }
```

Restart Claude Code so it picks up the new skills.

## Use

**Convene the whole team on a problem:**

```
> Nonlinear Team: our interior-point NLP solver (filter line search, LDLᵀ with inertia correction) fails on 30 of our 400
  regression models, mostly in restoration, and calls 2 feasible ones infeasible. Two engineers, six months; defaults must not change.
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
| `@Gould …` / `@all …` | Ask one member, or every seated member |
| `add Toint` / `drop Ye` | Change who is seated |
| `pursue 2` / `round` | Pick the disagreement / run another round |
| `plan` / `autopilot` | Go to the plan now / run to the draft plan without stopping |
| `stop` | End the roundtable |

Surnames match without diacritics (`@Waechter` or `@Wachter` = Wächter). Anything else you type is passed to the seated members as new information. At the end the moderator offers to save the transcript as a markdown file.

Cost: one agent call per member per turn — about 3 per round with default seating. Runtimes without subagents fall back to a single-model simulation, and the moderator says so.

**Other modes:**

```
> Nonlinear Team, quick: …                                            # best-fit 1–2 members, straight to plan
> Nonlinear Team, debate Fletcher vs Nocedal: filter or adaptive penalty for our SQP?   # two lenses argue one decision
> Use the Wächter lens on my failing run's iteration log and our restoration-phase options
> Use the Robinson lens on our SQP convergence proof: which hypotheses can the running code check?
> How would Gould handle a KKT factorization that takes most of each iteration?   # a single member directly
```

Say "exit" or "end roundtable" to return to normal mode.

Curtis's and Nocedal's skills are deep-read: for the proof devices, algorithm-design moves, experiment protocols and writing moves behind their methods, each with paper-card pages, read [Curtis's technique catalog](frank-e-curtis/references/technique-catalog.md) and [Nocedal's technique catalog](jorge-nocedal/references/technique-catalog.md) (Nocedal's also has textbook, errata and reading moves from the open parts of *Numerical Optimization*, the joint voice of Nocedal and S. J. Wright). The other nine members have no technique catalog (base tier).

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
    │   └── 10-claim-audit.md            # sampled claim-to-card audits and their fixes
    └── sources/
        ├── RESOURCES.md                 # tracker: every source, verified ✅ or lead ⚠️, where it was used
        ├── publications/
        │   ├── works.json               # complete publication list, cross-checked (DBLP, Crossref, arXiv)
        │   └── scholar.md               # the same list, readable, with audit notes
        ├── papers/
        │   ├── INDEX.md                 # every work: full-text status, role, read level
        │   ├── abstracts.json           # abstracts (arXiv / Crossref)
        │   ├── abstract-sources.json    # where each chased abstract came from
        │   ├── book-leads.json          # links to the open parts of books (prefaces, contents, errata) for T4
        │   ├── *.pdf                    # open full texts (git-ignored)
        │   └── txt/                     # extracted text with [[page N]] markers (git-ignored)
        ├── talks/                       # transcripts, slides, lecture notes
        ├── essays/                      # methodology writings, surveys
        ├── software/                    # notes on the researcher's software and code
        └── private/                     # git-ignored; only its README is tracked
```

The technique catalog, `cards/`, 07–10, `publications/works.json` and `scholar.md`, and `papers/` come from the deep reading. **This is a mixed-tier team: only Frank E. Curtis and Jorge Nocedal have been deep-read, so only their folders have those files**; Nocedal's `papers/INDEX.md` also lists 12 book-material rows (B001–B012: the open front and back matter, errata, reviews, book web pages and catalogue pages of *Numerical Optimization*, carded as the joint voice of Nocedal and S. J. Wright, the reviews as the reviewer's and the catalogue as mostly the publisher's). The other nine members are base tier, with no deep reading (see [DEEP-READING.md](DEEP-READING.md)). Each skill has `SKILL.md`, the notes 01–06 and `RESOURCES.md`; a base-tier member's `publications/` folder holds the OpenAlex pull the notes started from (`publications.md`, `abstracts.md`): raw material, not an audited publication list. Robinson's `publications/` folder holds the same kind of OpenAlex pull, made on 2026-10-17 after his notes were written; note 01 assembled his publication list from DBLP, Crossref, OpenAlex and his homepage. Five members also have saved talk transcripts or interview notes under `talks/` (Nocedal, Wright, Gill, Toint, Fletcher). A member with a student mode would also have `proof-playbook.md`, `open-problems.md` and `reading-path.md` under `references/`; none has one yet. No `private/` folder is ever published.

To add a resource later, add a row to that researcher's `RESOURCES.md` and drop the file into the matching folder. If the resource changes a method, update the research note and `SKILL.md`. To add full texts and paper cards for another member, run the deep tier for that member (stages T3.1–T3.8 of the [research-team playbook](../../references/research-team-playbook.md)) and record it in [DEEP-READING.md](DEEP-READING.md).

This team is configured by [team.json](team.json). To build another team like it, or to update this one, use the generic kit in this repository (`scripts/new_team.py`, the saved workflows in `scripts/workflows/`): see the [research-team playbook](../../references/research-team-playbook.md).

## Honest Boundary

- These are simulated lenses built from public work, not the researchers' own views.
- The research started from web search results in September 2026 (October 2026 for Robinson, who joined later). Two skills were then deepened by reading each member's publications in full or in part wherever an open copy exists: Frank E. Curtis's on 2026-10-10 and Jorge Nocedal's on 2026-10-16 to 2026-10-17 (with the open parts of *Numerical Optimization*, read as the joint voice of Nocedal and S. J. Wright, outside the counts below). The other nine members in the table below are base tier, with no deep reading of their publication lists (single papers, theses, slides and transcripts were opened where the notes needed them), so their rows below are zero. Coverage, from each `papers/INDEX.md` (details in [DEEP-READING.md](DEEP-READING.md)):

  | Researcher | Works indexed | Read in full / in part | Abstract or metadata only (incl. unreadable) | Skipped (not the author's, or not research) |
  |---|---|---|---|---|
  | Curtis | 96 | 86 / 0 | 10 | 0 |
  | Nocedal | 167 | 80 / 17 | 62 | 8 |
  | Wright | 0 | 0 / 0 | 0 | 0 |
  | Ye | 0 | 0 / 0 | 0 | 0 |
  | Wächter | 0 | 0 / 0 | 0 | 0 |
  | Gill | 0 | 0 / 0 | 0 | 0 |
  | Toint | 0 | 0 / 0 | 0 | 0 |
  | Gould | 0 | 0 / 0 | 0 | 0 |
  | Fletcher | 0 | 0 / 0 | 0 | 0 |
  | Nesterov | 0 | 0 / 0 | 0 | 0 |
  | Robinson | 0 | 0 / 0 | 0 | 0 |

  Daniel P. Robinson joined on 2026-10-17 at the base tier (research notes dated 2026-10-16, built from public web sources and bibliographic databases; single papers, reports, theses and code were opened where the notes needed them, and an extra fidelity audit on 2026-10-17 checked 419 claims of his `SKILL.md` against primary sources). Each skill's Honest Boundary lists its gaps and `RESOURCES.md` marks unverified leads ⚠️.
- Fletcher (d. 2016) is a historical lens; the skill reflects work up to then.
- Treat every recommendation as a hypothesis to test on your problem.

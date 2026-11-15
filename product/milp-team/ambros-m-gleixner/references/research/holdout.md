# Ambros M. Gleixner · Holdout (sealed test material)

- **Researcher**: Ambros M. Gleixner (ORCID 0000-0003-0391-5903; DBLP pid 07/3479). Living.
- **Date**: 2026-11-14
- **Rule**: Sealed until the validation is done: this is test material, not evidence. It must not appear in the Phase 2 record, in SKILL.md or among the Phase 4 exam's questions. To unseal an item after a validation, move it under a heading '## Unsealed (<date>)' at the end of this file.
- **Picked before the skill was built**: `SKILL.md` did not exist in the member folder on 2026-11-14, so none of the sealed content can already be in it.
- **Items**: 5 (H1–H5), spread over 2015, 2016–2021, 2021, 2023 and 2025, and over five topics: baseline design, benchmark admission, a branching judgement, debug/release behaviour in another team's solver, and the input limits of the exact solving mode.

**How the items were checked.** Every point below was taken from the source itself, opened on 2026-11-14, not from the notes' summaries:

| Item | Copy opened |
|---|---|
| H1 | Thesis full text, scratch `01-dl/thesis/thesis.txt` (from DOI 10.14279/depositonce-4938), printed pp. 64–66 |
| H2 | MIPLIB 2017 open-access full text, scratch `01-dl/miplib2017/miplib2017.txt`, journal pp. 467–468 (page breaks counted: journal page = PDF page + 442) |
| H3 | Human-made caption track of the Simons talk, scratch `02/subs/simons2021.txt` and the `.srt` file for timestamps |
| H4 | GitHub REST API, `ERGO-Code/HiGHS` pull requests 1184 and 1195 with all comments, fetched 2026-11-14 |
| H5 | GitHub REST API copy of `scipopt/scip` issue 151 with all comments, scratch `05/scip_issue_151.json` and `05/scip_issue_151_comments.json` |

**Quotation policy.** The thesis is In Copyright, the talk captions belong to the Simons Institute, and GitHub comments belong to their authors. For H1, H3, H4 and H5 this file therefore gives exactly one short verbatim fragment (under 15 words) per item, where the wording itself is the evidence; the other points are faithful paraphrases with a pinpoint (page, timestamp, or comment date) at which a grader can check the wording. MIPLIB 2017 (H2) is CC BY 4.0 and is quoted verbatim with page numbers.

**Voice.** H1 is single-authored text (the experiment design is credited there to joint work with D. E. Steffy and K. Wolter). H2 is co-authored text of a 16-author paper he leads; it is the committee's stated position, not his alone. H3, H4 and H5 are his own words (a talk answer and comments posted under his GitHub account).

---

## H1

**Source**: A. M. Gleixner, *Exact and fast algorithms for mixed-integer nonlinear programming*, PhD thesis, TU Berlin, 2015, DOI 10.14279/depositonce-4938, §3.2.1, printed pp. 64–65, with Table 3.1 on p. 66. The experiments date from 2014.

**Question**: In 2014 you have iterative refinement running in SoPlex: it returns LP solutions of very high accuracy together with a basis. You wonder whether such a basis can speed up exact rational LP solving. The established exact solver is QSopt_ex, which raises its working precision step by step, and you have about 1,200 public LP instances. Two ways to measure suggest themselves: compare "SoPlex with refinement, then QSopt_ex started from its basis" with QSopt_ex run on its own, which is what every user of exact LP runs today; or build some other reference. What experiment do you run, what do you compare it with, how do you report the result, and why?

**What they actually said or did** [stated + practice, single-authored]:
1. He runs the cheapest possible test before designing any new algorithm: QSopt_ex 2.5.10 is warm-started from the basis that SoPlex returns after refinement to tolerance 1e-50 ("SoPlex50"), and the total time of both runs is measured. The text notes that this needs no new code beyond linking two existing libraries (p. 64).
2. He rejects plain QSopt_ex as the reference: "Comparing this to the plain QSopt ex performance would be biased" (p. 64). The reason given is that the floating-point simplex implementations of SoPlex and QSopt_ex differ significantly; his example is that QSopt_ex has no presolving. The reference he uses instead is QSopt_ex warm-started from the basis of SoPlex at the ordinary double-precision tolerance 1e-9 ("SoPlex9"), so both arms share the same floating-point front end and differ only in the refinement.
3. The comparison is restricted and stated: the 1,195 instances on which both SoPlex settings returned basic solutions, same hardware and software, a two-hour limit for each QSopt_ex run (p. 64).
4. The aggregate is taken only over the 307 instances solved by both versions on which at least one version needed more than two seconds, as shifted geometric means with shifts of two seconds and 100 simplex iterations, and it is split by the number of refinement rounds needed to reach the final basis (p. 65, Table 3.1 on p. 66).
5. He reads the result per class and does not report one overall average: where refinement did not change the basis, total time rises by about 1% (the overhead of refinement); on the 23 instances where it did, total time falls to 18% (a factor of 5.5), and he points out that this figure does not even include the nine instances solved only from the refined basis. He adds that the gain cannot be explained by fewer simplex iterations alone: from the refined basis QSopt_ex performed no precision boosts. He calls it a simple experiment and uses it to motivate the systematic analysis of the next section (p. 65).

**Why this one**: A real fork about which baseline to trust, with the reason written down. Someone who knows how he builds baselines would say "change one thing only, so warm-start the competitor from the unrefined basis". A good researcher who does not know the work would very probably compare against QSopt_ex from scratch, because that is the number a reader expects, and would report one mean over all instances. It is a side experiment of a thesis chapter, not the result the chapter is cited for.

**Where it appears in the notes** (leave these passages out of the synthesis):
- `01-publications.md` §2, SW1, bullet "Minimum evidence": the sentences on the warm start, the biased comparison and the reference point, and "total time fell to 18% on average (factor 5.5; p. 65)". The second half of the bullet (thesis p. 3, the 3% and 7% slowdown at precision 1e-50) is a different passage and may stay.
- `01-publications.md` §0, table row "The first warm-start experiment for exact LP (§3.2.1) was designed jointly with Steffy and Wolter" (attribution only; if kept, keep it without the design).
- `01-publications.md` §4, CM2: the clause "fair baselines (S4 p. 64)".
- `03-process-evidence.md` §3, PE-07 (the whole item, both bullets).
- `03-process-evidence.md` §6, PE-33, last bullet: only the page reference "64–65" for footnoted instance lists (harmless, but it points at the same pages).

---

## H2

**Source**: A. Gleixner, G. Hendel, G. Gamrath, T. Achterberg et al., "MIPLIB 2017: data-driven compilation of the 6th mixed-integer programming library", Mathematical Programming Computation 13 (2021) 443–490, DOI 10.1007/s12532-020-00194-3 (CC BY 4.0), §5.1, Definition 2 and the paragraph after it, pp. 467–468 (Table 7 on p. 468). The decisions were taken in 2017–2018; the paper was submitted in July 2019.

**Question**: In 2017–2018 you lead the committee that compiles a new benchmark set of MIP instances on which solvers will be timed against each other for years. Among the thousands of submitted instances are two awkward kinds: instances that are infeasible, and instances that are feasible but have no finite optimal value. For each kind you can admit it to the benchmark set or keep it out. What do you decide for each of the two, and what are your reasons?

**What they actually said or did** [stated, co-authored; Gleixner first of 16]:
1. The two kinds are treated differently. Criterion (B.7) of benchmark suitability requires that an instance "is either infeasible or has a finite optimum" (p. 467): feasible instances without a finite optimum are kept out of the benchmark set.
2. First reason, a mathematical one: "a feasible, rational MIP has a finite optimal value if and only if its LP relaxation has a finite optimal value, rendering detection of this property more a continuous than a discrete problem" (p. 467).
3. Second reason, about solver behaviour: "there is currently no clear consensus on the expected behavior and output of MIP solvers in the case of a feasible MIP without a finite optimum" (p. 467).
4. Infeasible instances stay in: "Note that in contrast, infeasible instances are deliberately not excluded" (p. 467). The definition is worded to fit them: because infeasible instances are allowed, a successful "solution" means that the solver "either produced a (claimed) optimal solution or a (claimed) proof of infeasibility" (p. 467).
5. The exclusion is counted and it is limited to the benchmark set: Table 7 lists "(B.7) Unbounded instances 87" (p. 468), and the larger collection "may contain unbounded instances and instances with indicator constraints" (p. 468).

**Why this one**: A small admission judgement with two explicit reasons, one of them a piece of mathematics that is easy to miss. Sensible people answer it both ways: "exclude both, a benchmark needs an optimal value to compare" or "keep both, solvers must handle them". Someone who knows how he reasons about benchmark admission (what is ambiguous goes, what is merely hard stays) should get the split right; the two reasons and the "collection yes, benchmark no" detail are the checkable part. It is one criterion of nine and is not what accounts of MIPLIB 2017 report.

**Where it appears in the notes** (leave these passages out of the synthesis):
- `02-methodology.md` §5.4, second bullet ("MIPLIB 2017, p.467 [S10]: feasible instances without a finite optimum are excluded because … Infeasible instances 'are deliberately not excluded'").
- `03-process-evidence.md` §4.2, PE-17: in the list of criteria B.1–B.9, the sub-bullet "finite optimum or infeasible". The other criteria in that list are not sealed.

---

## H3

**Source**: A. Gleixner, "Exact Mixed-Integer Programming over the Rational Numbers", Simons Institute, workshop "Beyond Satisfiability" (online seminar), 30 March 2021, https://www.youtube.com/watch?v=JMZUJlWfMT8, closing question and answer. Question read out by the host at 02:18:31–02:19:09; answer at 02:19:09–02:20:18 (human-made caption track; timestamps from the `.srt` file).

**Question**: In 2021 you give a long seminar on MIP solving to an audience of SAT and proof-complexity researchers. At the end the host relays a question: theorists study branching on general linear inequalities, that is, taking some combination a·x and splitting into a·x ≤ b and a·x ≥ b+1, instead of branching on single variables. Do MIP solvers do that, and if not, why not? What do you answer?

**What they actually said or did** [stated, own voice; a complete answer in about a minute]:
1. A flat statement of practice first: it has been investigated in the literature, and current solvers do not do it; he says there are several reasons why it does not seem beneficial (02:19:09–02:19:20).
2. First reason, the selection problem: finding a good general disjunction is much harder and costs much more time; the degrees of freedom are huge, there are currently no good ways to limit them, and better ideas are needed (02:19:20–02:19:46).
3. Second reason, the LP: with general disjunctions LP solving gets slower. Variable branching fixes variables and so shrinks the LP; branching on a general constraint adds constraints and slows the LP down (02:19:46–02:20:03).
4. The verdict, with the counter-argument conceded: "And that doesn't seem to pay off in practice also." (02:20:03–02:20:06), followed at once by the admission that the dual bounds could of course improve.
5. He closes by saying that several papers have tried it and that he has one himself (02:20:10–02:20:18); the talk does not name the paper.

**Why this one**: A complete, argued answer to one specific methodological question, given outside any paper. A general answer ("too expensive to choose the disjunction") gets point 2 only. The LP-size argument in point 3, the conceded dual-bound gain in point 4 and the fact that he speaks as someone who has tried it are what a person who knows his solver-side view would add. It is a side judgement in a two-hour talk, not part of the exactness programme the talk is about.

**Where it appears in the notes** (leave these passages out of the synthesis):
- `02-methodology.md` §2.5, first bullet group "Branching on general disjunctions, 02:19:14–02:20:16" with all its sub-bullets, including the guess at which paper is meant.
- `02-methodology.md` §5, table "Failures, losses and abandoned directions he reported", row F2.
- `02-methodology.md` Gaps, "Unresolved points", first bullet (the "I also have one" paper).
- Context that may stay because it contains none of the answer: `04-mentorship.md` §7, K5, first bullet, and `06-trajectory.md` §3, T2, both of which only list the CPAIOR 2015 paper "Branching on Multi-aggregated Variables" (DOI 10.1007/978-3-319-18008-3_10).

---

## H4

**Source**: GitHub, `ERGO-Code/HiGHS`, pull request #1184 "Allow small matrix values introduced by presolve, also in debug mode" (opened by `ambros-gleixner` on 2023-02-25; closed, not merged) with its comment thread of 2023-02-26 to 2023-03-03, and the follow-up pull request #1195 "Allow small matrix values after presolve" (opened 2023-03-03; closed, not merged; comments of 2023-03-05 and 2023-03-06). https://github.com/ERGO-Code/HiGHS/pull/1184 and https://github.com/ERGO-Code/HiGHS/pull/1195.

**Question**: In early 2023 you are writing the interface that lets your MIP solver use another team's open-source LP solver. Your debug build aborts on an assertion inside their code. You trace it: their presolve creates matrix coefficients below their own small-value threshold although the original problem has none; in debug mode the solver removes these entries, warns, and then the assertion fires; in optimized mode the entries are kept and the solve continues. When you raise it, the maintainer first says the assertion is important, because tiny values must never be available as pivots, and a few days later that the optimized behaviour causes no trouble in practice. You are a guest in their repository. What do you propose, and how do you argue?

**What they actually said or did** [practice + stated, own comments; the maintainer's replies are observed]:
1. He opens with a concrete patch and a reproduction, not a complaint: a pull request that relaxes the assertion so that debug accepts what optimized mode already accepts, with the diagnosis (the small values come from the aggregator) and the exact command that triggers it quickly on a MIPLIB instance; he adds that it also happens on numerically nicer instances (PR #1184 description, 2023-02-25).
2. When the maintainer defends the assertion, he shifts the argument from the small values to the two build modes: debug deletes the entries and optimized apparently does not, so there is "a difference between debug and optimized behavior that can make debugging harder", and he asks for that difference to be removed independently of, or in addition to, any fix for the small entries (comment of 2023-02-27).
3. He concedes that his own patch is bad by that same standard, twice (2023-03-01 and 2023-03-03), and keeps the underlying problem on the table: he reproduces it with the LP solver alone on the command line, attaches the LP file, and offers to file a proper issue (2023-03-01).
4. He holds the maintainer to consistency: he points out, with a smiley, that "optimized mode is fine" contradicts the earlier statement that tiny values must be avoided (2023-03-02), and then draws the consequence: if the optimized behaviour is considered acceptable, debug mode should not assert there, because otherwise the code after the assertion never gets exercised in debug mode (2023-03-03).
5. He ends with a design, then an implementation, then lets go: a non-intrusive version of the checking routine that only checks the matrix and prints warnings, with the solver's developer-assert switch turning the stopping behaviour back on (2023-03-03); he submits a first attempt as PR #1195 the same day. The maintainer asks to be left to write such things himself (2023-03-05); he answers in five words that he only wanted to help (2023-03-06) and does not press further. Neither pull request was merged.

**Why this one**: A fork about how to argue a code-level disagreement in someone else's project, with his reasoning on record over a week. Obvious answers are "just relax the assertion", "ask them to clean small values in presolve", or "work around it in the interface". What he actually argues is a principle about testing (debug and optimized builds must take the same path, so that the debug build tests the code that ships), he abandons his own patch when it fails that principle, and he accepts the maintainer's refusal. A person who knows his habits around debug builds, assertions and regression tests should find the principle; a good researcher without that knowledge will mostly stay at the level of the small values.

**Where it appears in the notes** (leave these passages out of the synthesis):
- `03-process-evidence.md` §4.4, PE-21:
  - the second half of the item title ("and an argument for keeping debug and optimized builds identical");
  - in the list of pull requests, the sub-bullet "#1184 (small matrix values introduced by presolve, with the exact command line to reproduce) and its follow-up #1195";
  - the bullet "In #1184 he argued that debug and optimized builds should not behave differently, because that makes debugging harder";
  - in the bullet on outcomes, the clause "#1184 with his own analysis of the small values";
  - the last bullet (the exchange on #1195, both quotations).
- The rest of PE-21 (#1102, #1121, #1175, #1182, the SCIP commits on `lpi_highs`) is not sealed. The source entry S26 may stay as a listing.

---

## H5

**Source**: GitHub, `scipopt/scip`, issue #151 "Exact solver returns spurious infeasible result with large coefficients" (opened by a user on 2025-06-03; closed by `ambros-gleixner` on 2025-08-29), https://github.com/scipopt/scip/issues/151. His comments are dated 2025-06-03T20:31Z and 2025-08-29T14:51Z.

**Question**: In June 2025, a few months before the numerically exact solving mode ships in a major release of your solver, a user files a report against the development version. Their minimal example is one integer variable x with the constraint x ≥ 1 and the objective "minimise 99999999999999983617·x". With exact mode switched on, the solver answers "infeasible", although x = 1 is plainly feasible. The user explains that they are trying to solve integer programs whose coefficients have more than about twenty digits. You can treat this as an ordinary bug to be fixed, promise that an exact solver will handle numbers of any size, or declare a limit of the method. What do you answer, and what do you change in the software?

**What they actually said or did** [stated + practice, own comments; a colleague's comments in the thread are his, not Gleixner's]:
1. He answers about two hours after the report, thanks the reporter, and separates two things. The first is a limit of the design: the solver is exact, but it restricts the input it can accept, because the exact mode "maintains a floating-point version of the problem in parallel"; that floating-point side treats numbers beyond 1e20 as infinite, and the threshold can in principle be changed, but at present only at compile time (comment of 2025-06-03, first bullet).
2. The second is an ordinary bug: for the trivial example he suspects a presolving bug that he believes was fixed that day, and asks the user to retry with the latest master and a current SoPlex (same comment). A colleague replies minutes later that it is not fixed yet; the colleague reports on 2025-08-29 that the near-infinity coefficient case is resolved by a later commit.
3. His standing advice is to rescale before handing a problem to the solver, with a precise statement of what is and is not the issue: twenty or more decimal digits of precision are not a problem in themselves, but the largest numbers should ideally stay below 1e16 in absolute value (same comment).
4. He says in the same breath what the software owes the user: it should warn, or even raise an error, on such input (same comment).
5. He closes the issue on 2025-08-29 once that is done, and only that: the maintenance branch and master now print warnings when feasible solution candidates with objective values beyond the infinity threshold are discarded. The thread records no change to the threshold itself: a colleague's advice there, for users who need larger values, is to redefine the infinity constant in the source and recompile, or to shift the variables. He invites the user to reopen or file a new issue with further questions. (Whether the threshold later became a run-time parameter was not checked.)

**Why this one**: A design fork answered in public by the person responsible for the feature. A good researcher who does not know the architecture will say "an exact rational solver must not have a magnitude limit, so this is a bug to fix", or will promise arbitrary magnitudes. Someone who knows how the exact mode is built should predict the other answer (a floating-point copy runs alongside, so there is an input range), the split into "one real bug plus one limit", the rescaling advice with its two thresholds, and the remedy of a warning instead of silence. The limit is not stated in the papers the notes read; it surfaced only in this thread.

**Where it appears in the notes** (leave these passages out of the synthesis):
- `05-peer-critique.md` §0, summary table, row Q4: the row title clause "exact only within an input range" and, in the answer column, "Gleixner explains the hybrid-precision input limit (values beyond 1e20 treated as infinite) and adds warnings".
- `05-peer-critique.md` §5, table row "#151 (2025-06-03 to 2025-08-29)", and the last bullet of §5 ("[inferred] The 1e20 input range is a limit of applicability …").
- `05-peer-critique.md` §12, item 4: the clause "warnings where a limit cannot be removed".
- `05-peer-critique.md` Contradictions, C9 ("Exactness versus an input range").
- The other rows of the §5 table (#238, #261, #248, #79) are not sealed.

---

## Selection record

- The six notes cite well over 100 sources, so the sealed-item test is possible.
- Considered and not picked, with the reason:
  - the June 2019 update of the MIPLIB 2017 benchmark set, the VIPR checker bugs and his reply to the October 2026 pull requests, the precision-boosting follow-up to iterative refinement, the thesis results on OBBT and on the three branching rules: each is reported in three or more notes and carries evidence for what will clearly be a core method;
  - the reasons for exactness, mixed precision, shifted geometric means, "both-solved" subsets: repeated claims, and partly in `00-prior.md`;
  - the MIPcc23 scoring rules: a committee document, and the main evidence for the anti-gaming item;
  - the mailing-list answers of 2018 (debug-solution advice; numerical trouble in a column-generation model): usable, but the first has only two points and the second tests general LP-numerics knowledge more than his own judgement;
  - the VIPR v1 to v2 change (instance nw04 and the tightening tool): the versions show what changed but give no stated reason.

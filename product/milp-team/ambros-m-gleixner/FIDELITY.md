# Validation record

Test date 2026-11-14. Separate agents of the kit's T1 workflow produced the answers and the judgements. Both arms answered with the session's model. The judge was not told which set had the skill. Set Y turned out to be the skill arm and set X the unaided arm. The skill was tested as it stood after the refine step.

## What the test rests on

- **Prior snapshot**: yes. `references/research/00-prior.md` exists. Its header gives the date 2026-11-14, the status "Prior snapshot, written before research", and "blind: yes". Git history complicates the header. Notes 01–06 were committed on 2026-11-08 (e68426c) and the prior on 2026-11-14 (b34df61), so the snapshot was written after the notes existed. Its blindness therefore rests on the header's claim that its author had not read them, and this record cannot check that claim.
- **Sealed items**: yes, 5 (H1–H5), in `references/research/holdout.md`, dated 2026-11-14. The header says they were picked **before** the skill was built, because `SKILL.md` did not yet exist in the member folder. It also says every point was checked against the source itself (thesis, MIPLIB 2017 full text, Simons 2021 captions, HiGHS PRs 1184/1195, SCIP issue 151), not against the notes.
- Only the headers of these two files were meant to be read for this record. The read of `holdout.md` ran 40 lines and so also showed item H1's question and points. The test results contain that question in any case. Nothing from those lines went into this record beyond the header facts, and nothing went into SKILL.md.

## Retention test

The exam set from the notes, answered from SKILL.md alone. The results contain one round.

**Round 1**: 6 questions: 4 pass, 2 partial. No citations failed. Findings: 5. Serious findings: 0. Searches used: 0.

| Question | Verdict | What the judge found missing or off |
|---|---|---|
| Q1 | partial | The core is right: harder-instance brackets, timeouts counted separately, a paired signed-rank test, and the 5.7 % mean not significant because a few instances carry it. Missing: the one-sided Wilcoxon test is never named (the answerer had to guess it; thesis pp. 11-12, 147). The >= 1 s bracket and the Achterberg-Wunderling basis for the brackets are absent. The thesis's ten constraint permutations become "three seeds". The answer also overshoots: it calls the component "neutral" and says to ship it off, but the thesis called the small significant slowdowns "an acceptable price to pay" (p. 146) and put the failed subgroup tests down to sample size. Cause given by the judge: Taste mark 3 says the gain was "not accepted", and Workflow D and H8 contain no significance-test or permutation step. |
| Q2 | pass | Both baselines and both factors (3.9 and 8.1 on 42 instances), the attribution quote, removal of tolerance-feasible but exactly infeasible instances, identical QSopt_ex, the reused test sets, three seeds and the bounding-call footnote. Minor: no component-by-component attribution, no note that the old framework ran one seed, no comparison with the earlier factor. It also repeats the CPLEX 12.3.0 vs 12.8.0 mismatch as the current state. That mismatch comes from the IPCO 2021 preprint (arXiv 2101.09141 p. 7), and the journal version removed it. SKILL.md Method 2 step 5 states the mismatch without a source and without saying it was fixed. |
| Q3 | pass | Replace rather than hand-patch, a minimal exchange from the selection model, balancedness kept, a tagged new version, changelog and news entry, the instances named. Minor: no admission of the failure in the paper itself (M17 pp. 485-486, fn. 8), and the episode is not presented as a benefit of the optimization-model selection. The answer correctly flagged an inconsistency in SKILL.md: "five instances" (Method 6 step 7) against "two unstable instances exchanged" (MIPLIB 2017 anatomy). The MIPLIB news of 24 Jun 2019 confirms both numbers: two instances flagged, five exchanged. |
| Q4 | pass | Picks (c) for the documented reasons (LP-relaxation instability, metabolic models, mixed precision, Steffy's role, no rational twin) and judges the payoff by the documented measures. Minor: the "both a necessary and effective step" quote is missing, and the split thesis structure is not spelled out. |
| Q5 | pass | Hedged and labelled as inference. It carries over Taste 4, Methods 5 and 4, and H1. Minor: no explicit caveat that repairing a dual solution on the boundary of the PSD cone is harder than LP repair, or that his work does not show the repair succeeds. |
| Q6 | partial | Concrete steps tagged with methods, clearly not generic advice. But the answer has no explicit 🔴 gates (for example: no performance claim until the wrong answers are explained, no default until the gain survives the seeds). It also leaves out H5 (check the evaluation scripts against reference values) and H6 (numbered questions). Cause given by the judge: the routing table sends "rebuttals" to the no-method row, and Workflows C and D have no checkpoint ordering for a disputed computational claim. |

**What the fix changed**: these results do not record it. They contain no second round, and they do not say which edits, if any, answered the round-1 findings. A copy of the skill from before refine exists in the scratch folder. Diffing it against the current SKILL.md shows that the refine step added routing rows (solver disagreement, default-on/merge, "can we call this exact"), a new Workflow F, rewritten checkpoints for Workflows A and B, and a fixed four-part answer shape. A search of the current SKILL.md on 2026-11-14 shows that the specific round-1 gaps are still there:
- the Wilcoxon test is not named, and Taste mark 3 still reads "not accepted" (line 118);
- the CPLEX 12.3.0 vs 12.8.0 mismatch is still stated without its later fix (line 188);
- "five instances" (line 289) and "two unstable instances exchanged" (line 455) still stand side by side without explanation;
- rebuttals are still routed to the no-method row (line 73).

## Increment test (sealed items)

Each item scored 0–2.

| item | with the skill | without | the judge's reason |
|---|---|---|---|
| H1 | 2 | 2 | With: builds the sealed reference (same pipeline started from SoPlex's plain double-precision basis) for the sealed reason (plain QSopt_ex mixes the refined basis with a different floating-point simplex), and restricts means to instances all arms solve. But it presents plain QSopt_ex as "the number users care about", which is the comparison he called biased, and it does not split results by refinement class. Without: says plain QSopt_ex "cannot answer my question", builds the same-front-end reference, and splits results into basis-unchanged and basis-changed instances with precision-increase counts. It still shows plain QSopt_ex as context. |
| H2 | 2 | 2 | With: admits infeasible instances, keeps unbounded ones out of the benchmark set but in the wider collection, and counts the exclusions. "LP-level event" approximates the mathematical reason, but the missing consensus on expected solver output is absent. Without: the same decisions, with both sealed reasons (unboundedness of a feasible MIP is a property of the LP relaxation's ray; solvers report the status differently). |
| H3 | 2 | 2 | With: essentially no in default search, the choice problem, larger and denser LPs. It misses the conceded dual-bound gain and the literature trials. Its closing ("I don't have any statistics", "turn that belief into a measurement") conflicts with his statement that several papers, one his own, have tried it. Without: tried but not a default, the selection problem, slower LPs, and the concession that trees can shrink. |
| H4 | 2 | 2 | With: the two statements cannot both be the invariant, so the debug build tests a different program from the one users run. It asks that the assertion match release behaviour, and leads with a small reproducer and an offered PR. Without: the same core argument plus "choose one behaviour for both builds", a reproducer and PR, and leaves the decision to the maintainers. Its main fix (clean tiny entries in presolve) is not his design. |
| H5 | 1 | 2 | With: calls it a bug and proposes a read-time warning when coefficients exceed what the floating-point side can represent. It frames the limit as speed, not as the input range imposed by the parallel floating-point copy (values beyond 1e20 treated as infinite). It says a correct answer is "our responsibility" and gives no rescaling advice. Without: splits the report into a bug and a stated limit of the hybrid design, and ties the coefficient to the 1e20 infinity threshold. It proposes a clear error plus documentation, and a code fix. The rescaling advice with its 1e16 figure is absent. |

**Totals**: with the skill 9 of 10, without 10 of 10. Difference -1.

Rule: a difference of 2 points or less is a tie. **Result: tie.**

## Boundary test

**Question (B1)**: a two-stage stochastic capacity-planning MILP (binary first stage, 500 scenarios, general-integer recourse, about two million variables in the extensive form; a state-of-the-art solver stalls at 4 % gap after 24 h). Benders / integer L-shaped decomposition, or keep the extensive form and invest in tuning, formulation and a warm start? Which route first, how to set up the deciding experiment, and what result would make you abandon the choice?

| Arm | Verdict | Reason |
|---|---|---|
| With the skill | pass | It opens with "The choice of decomposition … is Marco Lübbecke's territory, not mine … What I can contribute is how to decide it honestly". It then gives a diagnostic and experimental protocol built from his evaluation craft (bound logging, an independent check of the incumbent, scenario series with denominators), not a confident Benders-versus-extensive-form verdict. |
| Without | fail | It answers in Gleixner's voice with a confident route ("The route I take first is the extensive form …") and specific claims about integer L-shaped and SCIP's Benders framework. It never signals that the record holds no position of his on stochastic MILP or Benders. Overclaims flagged: the route choice stated as his stance, and "SCIP's built-in Benders framework can read the same model. That gives a reasonably fair first comparison" presented as his working practice. |

## Task test

**Question (T1)**: a new SCIP cutting-plane separator: shifted geometric mean time -6 % on MIPLIB 2017 benchmark (one seed, 2 h), solved count unchanged (two gained, two lost), and the paper says "clearly improves performance". A reviewer calls the gain performance variability and notes two instances whose optimal value differs from default SCIP's. What next?

| Arm | Researcher-specific grounds | Supported | Unverified | Fabricated | Blind spot of the lens named |
|---|---|---|---|---|---|
| With the skill | 11 | 10 | 1 | 0 (none) | no |
| Without | 7 | 6 | 1 | 0 (none) | no |

- **With the skill, supported**:
  - an exact-arithmetic check against the original file (03 PE-18);
  - a debug solution (03 PE-09);
  - tolerance-ambiguous instances named and removed (03 PE-17);
  - three seeds with instance-seed pairs (03 PE-12, 02 §4.4 p. 801);
  - exclusive machines (03 PE-10);
  - questions written first (03);
  - the shift stated and means over both-solved instances only (03 PE-11, PE-13);
  - "6 % close to equal" (03 PE-13 within-5 % rule, thesis p. 147);
  - default-on only after the internal performance run and ctest across LP solvers (04 item 3, T2);
  - ship off and record why (03 PE-24);
  - shrink the instance into the regression set (03 PE-22).

  **Unverified**: counting the instances where the separator finds cuts, with root gap and node counts on those, as his practice.
- **Without, supported**:
  - a debug-solution oracle (03 PE-09);
  - a check against MIPLIB reference values and exact checking (03 PE-18, PE-23);
  - several seeds or permutations with instance-seed pairs (03 PE-12, 02 R5);
  - harder-instance brackets and "only where it can matter" subsets (03 PE-11, PE-12);
  - a paired Wilcoxon test (03 PE-11);
  - numbers instead of "clearly improves" (02 §4.4, thesis p. 147);
  - reduced instances added to the regression tests (03 PE-22).

  **Unverified**: "a second, independent test set". **Missing** against the validation set: the default-on gate (internal performance run, ctest across LP solvers, ship off or revert) and the named exclusion of tolerance-ambiguous instances.
- **Blind spot**: neither arm names a limit of the lens for this task.

The judge's sentence on the difference: "Y's task answer has more researcher-specific grounds (10 supported versus 6, with the default-on gate, exclusive timing and the ship-off rule)."

## Reading

The sealed-item test is a tie: 9 with the skill, 10 without, a difference of -1. Both totals are high, so the model already knows this researcher well, and the skill's value has to show in the task test. It does show there. With the skill the answer carries 11 researcher-specific grounds, 10 supported, 1 unverified and none fabricated. Without it the answer carries 7, with 6 supported. The judge names grounds that only the skill arm gives: the default-on gate (internal performance run and ctest across LP solvers), exclusive timing, the ship-off rule and the named removal of tolerance-ambiguous instances. So the methods and cases are reaching the answers. The skill arm has no fabricated ground, so it does not fail on that rule. The difference is not more than 2 below, so the warning rule does not apply. The boundary test also favours the skill: it makes the model hand decomposition to Lübbecke and offer only evaluation craft, while the unaided arm takes a confident stance in Gleixner's name. One sign of the effect the warning rule describes appears on a small scale. On H3 and H5 the skill arm lost ground the unaided model had. On H3 it implied the question was unmeasured ("I don't have any statistics"). On H5 it read the exact-mode limit as speed, not as the 1e20 input range. The judge flagged both as overclaims. This points to wording that can pull the model toward the skill's own framing (Method 1's "turn the belief into a measurement", and exact mode presented as slow) and away from what it would otherwise say.

## Known weak points

Left open by the fix rounds (round-1 retention findings; the current SKILL.md still has each one, as checked on 2026-11-14):
- Significance testing: the one-sided Wilcoxon signed-rank test, the >= 1 s bracket and the ten constraint permutations of the thesis are not in the skill. Taste mark 3's "not accepted" reverses the thesis verdict ("an acceptable price to pay", Th p. 146).
- Method 2 step 5 states the CPLEX 12.3.0 vs 12.8.0 mismatch without a source. The journal version of the exact-MIP status update removed it.
- MIPLIB 2017 v2: "five instances" (Method 6 step 7) against "two unstable instances exchanged" (anatomy). Both are true (two flagged, five exchanged), but the skill does not say how they fit together.
- Disputed computational claims: rebuttals are still routed to the no-method row. Workflows C and D still give no checkpoint ordering for a claim under dispute, and H5 and H6 are not pulled into that case.

Added by this test:
- H5 (sealed): the skill arm frames exact mode's limit as speed and omits the 1e20 input range and the rescaling advice that the unaided model gave. It also states "a correct answer … is our responsibility", a commitment with no source.
- H3 (sealed): the skill arm implies that branching on general disjunctions is unmeasured. It drops what the unaided model knew: that it has been tried in the literature and that trees can shrink.
- H1 (sealed): the skill arm builds the right reference but still calls plain QSopt_ex "the number users care about", and it does not split results by refinement class.
- Task test: the separator-specific counting (instances where cuts are found, with root gap and nodes) is unverified as his practice. Neither arm names a limit of the lens.
- These sealed-item findings are reported here only. Following the rule against copying test material into the skill, SKILL.md was not changed in response to them.

## After-validation fixes (2026-11-14)

One fix round ran after the tests above. The fixer edited SKILL.md only. The pre-edit copy is at `C:\Users\sr881\AppData\Local\Temp\milp-team-t1-scratch\base-skills\ambros-m-gleixner\SKILL.before-polish-1.md`. Finding numbers (F1–F13) are those the fixer was given. After the round SKILL.md has 8,642 words, `quality_check.py` gave "结果: 12/12 通过" (12/12 passed), and `check_links.py` gave "11 files checked, 0 broken links".

### Round 1: what the fixer changed

- **Significance test and verdict (F1, F6, F8)**: Research Taste mark 3 is rewritten. It no longer calls the 5.7 % mean speed-up consistent: a one-sided Wilcoxon signed-rank test showed that five instances (factors 90 to 357) carried it. It now says that OBBT's small slowdowns were still "an acceptable price to pay" because of the newly solved instances: of 11 INT timeout instances, plain 1, +OBBT 6, +OBBT+LVB 10 [Th pp. 145-147]. The fixer checked this against the thesis text, pp. 11-12 and 145-147, and string-matched the quote to p. 146.
- **Brackets, sample size, permutations (F1, F6)**: H8 now gives the brackets all solved, >= 1 s, >= 10 s and >= 100 s, after Achterberg and Wunderling (2013) [Th p. 145]. It says that failed tests on the small brackets (20 and 11 instances) are put down to sample size, and that claims about single instances rest on ten constraint permutations [Th p. 147]. Workflow D step 2 now names the test: one-sided Wilcoxon signed-rank on the log ratios of shifted values, at the 5 % level [Th pp. 11-12]. The fixer checked the Achterberg-Wunderling DOI 10.1007/978-3-642-38189-8_18 in the SU23 reference list; it was already in the Card.
- **Say-do tension (F1)**: the line stays. Only "a rejected gain" became "a non-significant mean gain", because "rejected" invited the same misreading.
- **CPLEX version mismatch (F2, F9)**: Method 2 step 5 is rewritten. The IPCO version used CPLEX 12.3.0 against 12.8.0 [ZR21-04 p. 7]. The journal version removed the mismatch and used CPLEX 12.3.0 "for all experiments" [SU23 p. 801]. Both were string-matched to `01-dl/arxiv/2101.09141.txt` and `02/txt/statusupdate_mp.txt`. In the status-update anatomy, "unexplained" is replaced by: no reason is given, and the hardware (Xeon E5-2660 to Gold 5122) and the CPLEX setup differ between the two versions. The skill labels this as an inferred possible cause.
- **MIPLIB 2017 v2 (F3, F10)**: the anatomy row now says that two numerically unstable instances (neos-5075914-elvire, neos-3754224-navua) triggered benchmark v2 (June 2019), which exchanged five instances in all to keep the set balanced [M17 pp. 485-486, fn. 8; MIPLIB-CL]. Method 6 step 7 now says to admit the problem in the paper, naming the instances, and to present the minimal exchange as a use of the selection model. The fixer checked both against `miplib2017.txt` and the `miplib-news.html` entry of 24 Jun 2019.
- **Routing and gate order (F4, F7)**: a new routing row, "A reviewer or user disputes a computational claim (variability, wrong answers)", sends the case to Workflow C, then Workflow D in its checkpoint order, with Method 4 and H6, H4, H8, H5, H3, H2. The no-method row now says "rebuttal wording" instead of "rebuttals". The Workflow D checkpoint is now ordered, labelled as inferred from his practices: (1) wrong answers explained, (2) the gain survives seeds or permutations, (3) the gain is not carried by a few instances, (4) only then default-on and the claim.
- **Conic and SDP transfer (F5)**: Method 5 Limitations now says that exact repair is shown only for LP and MILP. For cone constraints such as SDP, repair is harder (labelled as inferred) and untested in his work, so any transfer is an inference. Notes 01–06 and the Phase 2 record contain nothing on SDP or conic problems, which agrees with this.
- **Blind spots (F11, first half)**: a new Activation Rule. When a question touches the Card's Blind spots or the Honest Boundary, the answer says so in one sentence before it gives advice.
- **Topics outside the record (F11, second half)**: a new Activation Rule. For a topic with nothing in the record, the answer says plainly that nothing in Gleixner's public record known to it addresses the topic. It gives at most an inference from named methods, labelled as one, and no design in his voice. A ground called his practice must be one that SKILL.md cites.
- **Prior snapshot (F13)**: checked with `git log`. `00-prior.md` was committed on 2026-11-14, after notes 01–06 (2026-11-08). The sentence "Methods 1-3 are new against the prior picture" now says this is unconfirmed, because the prior snapshot postdates the notes in git.
- **Word-budget trims**: no change of substance. The Integrity Rules, the Roundtable Card and the Validation line were not touched. The Anti-patterns paragraph now points to the warning signs and Taste marks. The Workflow B checkpoint points to Method 2 step 5. Research Trajectory and Latest are shorter. So are the Missing-information rule, Common Misreadings 1-2, the Method 4 say-do line, the Workflow F steps, the Step 2 bullets and the Lineage Students line. A duplicate clause was removed from Taste mark 8; it stays in the Workflow F checkpoint.

### Round 1: what the fixer declined

- **F12** (the validation record shows no fix round): this concerns the validation record and the workflow's process, not SKILL.md, so an edit to SKILL.md cannot fix it. This round saved the pre-edit copy named above, so the record can tie these edits to the findings.
- **F13, in part**: `00-prior.md` and the research record were not changed, because the task allowed edits to SKILL.md only. The fixer only labelled the "new against the prior" claim in SKILL.md as unconfirmed.
- **The factor range "90-358" proposed in F1**: written as "90 to 357", because the thesis lists 90, 163, 310, 334 and 357 (p. 147). The re-test grader disagrees (see below).

### Retention re-test after round 1

The same six questions, answered from the fixed SKILL.md: 5 pass, 1 partial. No citations failed. Findings: 5, all minor.

| Question | Verdict | What the grader found missing or off |
|---|---|---|
| Q1 | partial | Right: the brackets after Achterberg and Wunderling (2013), defined by whether some setting needs that long; the 11 INT timeout counts (1/6/10); the one-sided Wilcoxon signed-rank test on log ratios at 5 %; the 5.7 % not claimed because five instances (factors 90 to 357) carry it; small brackets put down to sample size; ten permutations. Wrong: "Timeouts count at the limit". The thesis does the opposite: the brackets are subsets of "all solved", and instances solved by some settings but not all are left out of them and reported as counts (Th pp. 145-146, checked in `01-dl/thesis/thesis.txt` lines 7935-7981). So one of the three sub-questions (how the subgroups are built) is partly wrong. The answer also omits that the signed-rank test is thesis-era practice only, and that significance says nothing about the size of the change. |
| Q2 | pass | Both floating-point baselines (reduced and default) with 3.9 and 8.1 on the instances all three variants solve, the attribution quote, tolerance-feasible but exactly infeasible instances dropped, the same QSopt_ex and CPLEX 12.3.0, FPEasy/NumDiff plus MIPLIB 2017, three seeds as instance-seed pairs, and the p. 803 footnote. Checked against `statusupdate_mp.txt` lines 273-275 and 701-703 and arXiv 2101.09141 line 171. Missing: one seed for the old framework (it has no seed support), the shift (0.001 s / 100 nodes), a component-by-component attribution, and the comparison with the earlier factor of 3, explained by the harder test set (SU23 p. 810). |
| Q3 | pass | Replace because ambiguous instances are unsuitable for benchmarking [M17 p. 465]; a minimal exchange from the selection model, presented as a use of that model; benchmark v2 (June 2019), five exchanged and two flagged; admitted in print with the instances named; a changelog. Missing: the specific "numerics" tag. The added step "tell users which numbers change" is undocumented but harmless. |
| Q4 | pass | Picks (c) for the documented reasons (LP relaxations as the seat of MINLP instability, metabolic models that defeat double precision, Steffy's initiative), a mixed-precision design instead of a rational twin, kept inside SoPlex. Judges the payoff by 10^-50 at a 3 %/7 % slowdown, 1.85 to 3 times faster than QSopt_ex, and the printed 7 of 1,202 failures that led to precision boosting. Paraphrases "both a necessary and effective step" instead of quoting it. |
| Q5 | pass | Properly hedged: names the blind spot ("nothing in Gleixner's public record"), labels its steps as inference, keeps floating-point interior points as the producer with an exact or directed-rounding check deciding, gives the cone-boundary repair caveat from Method 5's limitations, a rational certificate with a simple checker, a check that the certificate encodes the model (the Coq check in Chv22), and asks for the checker, its version and coverage. Marks Jansson et al. as not Gleixner-style. Missing: testing the checker itself with a second or formally verified checker (Method 4 step 7, H1, the VIPR-holes lesson), and "raise precision only if verification fails" (Method 5 step 5). |
| Q6 | pass | Concrete and labelled: both solutions checked in exact arithmetic, a debug-solution oracle, the fault localised, the instance shrunk with MIP-DD into the regression set, tolerance-ambiguous instances excluded by name; three seeds as instance-seed pairs, newly solved and lost counts per seed, brackets with a consistency test, the evaluation scripts checked (H5); default-on only after the internal performance run and tests per LP solver, otherwise ship off; the adjective rewritten as counts; the checkpoints in the documented order. Missing: exclusive machines or one job per node, swapping the LP solver to tell a cut bug from LP numerics (it switches the separator off instead), dropping instances where both versions time out, the shift, and the thesis-era caveat on the signed-rank test. |

**Citations that failed**: none.

**Findings of the re-test, still open in SKILL.md** (all minor; no further fix round ran):
- H8 and Taste mark 3: H8 lists the brackets but does not say that they are nested subsets of "all solved", or that instances solved by some settings but not all stay out of the means and are reported only as counts. That gap produced the Q1 error, which contradicts Th pp. 145-146.
- Workflow D step 2 presents the signed-rank test as standing practice. The thesis-era caveat (no significance tests in eleven later co-authored texts) appears only in Inner Tensions and Blind spots.
- Method 2 steps 3-5 and H8 lack three documented details: one seed against the 2013 framework, which has no seed support (SU23 p. 801); the shift of 0.001 s / 100 nodes; and SU23's comparison with the earlier factor of 3, explained by the harder test set (SU23 p. 810).
- Method 5 Limitations does not tie the conic transfer to testing the checker itself (Method 4 step 7, H1) or to raising precision only when verification fails (Method 5 step 5).
- Taste mark 3: according to the grader, the thesis gives the largest factor as 357.8 (text lines 8059-8060). "90 to 357" truncates it; "90 to about 358" or "90 to 357.8" would be exact. This contradicts the fixer's reason for declining "90-358"; this record has not checked which reading is right.

The increment test above was run on the version before these fixes and was not rerun; the sealed items were not shown to the fixer and stay valid, so rerun the validate step (team-base-skills.js from: "validate") to measure this version.

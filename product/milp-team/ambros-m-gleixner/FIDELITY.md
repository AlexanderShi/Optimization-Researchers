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

# Validation record

Test date 2026-11-14. Separate agents of the kit's T1 workflow wrote the answers and the judgements. Both arms answered with the session's model. The judge was not told which set had the skill: set X had it, set Y did not. The skill was tested as it stood after the refine step.

## What the test rests on

- **Prior snapshot.** [references/research/00-prior.md](references/research/00-prior.md) exists, dated 2026-11-14 and marked "blind: yes": it was written before the research, with no notes, sources or skill about him read in that session.
- **Sealed items.** [references/research/holdout.md](references/research/holdout.md) holds five items, H1 to H5. They were picked before any `SKILL.md` existed for him, so before the synthesis. H3 and H5 were unsealed on 2026-11-14, before the skill was built, at the user's decision, because they are not research decisions. That leaves **three sealed items** for the increment test: H1 (2001 thesis), H2 (2020 GCG landing page) and H4 (2026 preprint).

## Retention test

This is the exam set built from the notes, answered from SKILL.md alone. The results record one round. Every question passed and no citation failed. The judge logged 5 findings, none serious.

| Round | Question | Verdict | Main gaps the judge noted |
|---|---|---|---|
| 1 | K1 (pricing strategy) | pass | "many cheap columns" labelled [inferred] although documented (captions 1:33:36); "when you're lucky only once" (1:34:13) left out; no framework or GCG-as-probe; heuristic pricing, his number-one rule, put second behind "measure first" |
| 1 | K2 (unequal comparisons) | pass | leaves out "the challenges still lie on the modeling and algorithmic side" (p. 361) and the Benders reading of the two-stage approach; the quote "need to be taken with a grain of salt" is not verbatim (the source reads "This part of the overview needs to be taken with a grain of salt"), and the copy error comes from SKILL.md |
| 1 | K3 (writing) | pass | misses "Postponing the writing "to the end" is the worst idea you could have", which is in `02-methodology.md` line 294 but not in SKILL.md; puts the skill's own step text "Write before the results are final." in quotation marks next to his blog quotes |
| 1 | T1 (GCG design) | pass | does not name the original problem as the primary, coordinating instance with the master under a relaxation handler (SKILL.md lacks that detail); does not quote the stated reason ("started from scratch each time ... preprocessing and tree management") |
| 1 | E1 (master LP solver change) | pass | misses his 2020 remark that the master can be solved by "an interior point method or the simplex method or whatever method" (captions 1:34:56); SKILL.md does not carry that line |
| 1 | X1 (benchmark claim) | pass | no explicit checkpoint "if the compact model is competitive, narrow the claim"; the two-test-set design is not stated; conference-then-journal (H8) left out |

Citations that failed: none. Searches used: 0.

What the fix changed: these results record no fix round after round 1. A check of SKILL.md on 2026-11-14 shows the K2 misquote still in place (the B2 entry and the evidence list both have "need to be taken with a grain of salt"). The K3 line ("the worst idea") and the E1 line ("whatever method") are still not in SKILL.md.

## Increment test (sealed items)

Each item is scored 0 to 2, so the maximum total is 6.

| Item | With the skill (X) | Without (Y) | The judge's reason |
|---|---|---|---|
| H1 (2001: price-and-branch in the thesis) | 1 | 2 | X takes the same direction as point 1 (columns at the root only, then the final restricted master as an IP), and "I list branching as the missing piece" touches point 5. But X justifies it by the LP/Lagrangian bound and the podcast's fear of tree management, not by the sealed empirical basis, and names no branch-and-price "emergency reserve". Y has the same direction, gives an empirical basis with its weakness marked (points 2-3), and names branching-rule compatibility as the limit, "a second thesis" (point 5). Neither names the emergency reserve. |
| H2 (2020: GCG landing page) | 2 | 2 | X cuts the speed promise, rewrites the caption so it describes detection, prunes the list to entries that "actually have run it, not just cited it", and keeps the access claim. It misses that he reverted his own headline and pruned his own group's entries. Y cuts "to solve it quicker", prunes by the same criterion ("Citing our papers is not the same as using the solver") and keeps the access claim. It misses the headline reversion to "Welcome!", the caption rewording and the pruning of his group's entries, and it explicitly keeps "whatever type of problem you give it". |
| H4 (2026: NP-hard clique-partition separation) | 2 | 2 | X measures the ceiling first (add the whole family, compare the root bound), checks the bound "or the tree", and says the question is settled and the paper says so, with the NP-hardness proof. It computes the ceiling by enumeration on small graphs rather than by IP separation at the root, and keeps a heuristic separator, off by default, as an option. Y uses exact MIP separation on small instances as the ceiling benchmark, checks nodes and total time, makes the plain model the default if the heuristic does not help, and reports the negative result with the proof. It leads with a greedy heuristic separator, which leans toward the expected generic answer. |
| **Total** | **5** | **6** | |

Difference (with minus without): **-1**. A difference of 2 points or less is a tie, so this is a **tie**.

Overclaims the judge found:
- With the skill: on H1, "In 2001 nobody hands you a framework that manages the tree for a branch-and-price code" stretches his podcast remark (CPLEX gave him no tree control) into a general fact the notes do not support. Also on H1, "price heuristically for most of the run and exactly only to prove LP optimality" projects his 2020 advice (`02` §4.4) back onto the 2001 thesis, and the notes have no evidence of that practice in the thesis.
- Without: on H1, "In the tested cases the gaps were small" presents an assumed outcome as his result, although the thesis reports quality "occasionally significantly above ten percent from optimum". On B1, "existing certificate formats are not built for column generation" is stated as settled fact in his voice, with nothing in the notes behind it.

## Boundary test

**Question (B1).** A student's branch-and-price code reports a proven optimum on a set-partitioning model whose coefficients span several orders of magnitude. The dual bound comes from the floating-point restricted master LP, and pricing stops below -1e-6. A referee wants the bound made verifiably valid: a safe Lagrangian bound with directed rounding, an exact rational re-check, or a checkable certificate of the tree. Which would he do, at what cost, and what goes in the paper?

| Arm | Verdict | Reason |
|---|---|---|
| With the skill (X) | pass | It opens with "Exact arithmetic is not my home ground, so I would ask someone from the exact-MIP community" and marks its cost estimate "My guess, not measured". So it keeps the uncertainty and signals the limit of the lens. It invents no quote or paper by him on numerics. It does not say outright that the notes show nothing from him on this topic. |
| Without (Y) | fail | It gives a confident verdict in his voice ("I would do the safe Lagrangian bound, check the final master exactly if possible, and leave a full tree certificate out"). Nothing marks this as inferred from how he works, or says the notes have nothing from him on floating-point safety, exact solving or certificates. No quote or paper is invented, but the uncertainty is lost. |

## Task test

**Task (T1).** A doctoral student's branch-price-and-cut code for capacitated location-routing claims a 5x speed-up against times copied from an earlier paper. Four instances have values better than values that paper had proved optimal. The root has a long tailing-off phase. A reviewer asks for a fair comparison and a compact arc model in a current commercial solver. The answer has to give next steps with checkpoints.

| Arm | Specific grounds | Supported | Unverified | Fabricated | Blind spot of the lens named |
|---|---|---|---|---|---|
| With the skill (X) | 9 | 8 | 1 | 0 | no |
| Without (Y) | 9 | 6 | 3 | 0 | no |

- **X, supported:**
  - better-than-proven values treated as a bug signal and checked before any claim (`02` §5.1; `03` §1.5)
  - the compact model in a current solver as the baseline (`02` §4.2, §3.7, §4.10)
  - code requested or reimplemented, borrowed numbers labelled (`03` §1.2 item 3; `02` §4.7)
  - master time measured against pricing time and iteration counts first (`02` §4.3)
  - heuristic pricing, early termination on the Lagrangian gap, stabilisation last (`02` §4.4, R12)
  - switches and ablations (`03` §1.6)
  - a target set plus a general set that shows deteriorations (`03` §1.1 item 5)
  - shifted geometric means with the shifts, solved counts and losing instances reported (`03` §1.3, §2 item 3)
- **X, unverified:** "write to its authors precisely and credit them".
- **Y, supported:**
  - an independent solution checker, and no progress until the 4 cases are explained (`02` §5.1; `03` §1.5, §1.2 item 2)
  - code requested or reimplemented under identical conditions (`03` §1.2 item 3; `02` §4.7)
  - the compact arc model as a baseline (`02` §4.2, §3.7)
  - solved counts, gaps and performance profiles (`03` §1.3)
  - tailing-off measured, then early termination and earlier branching (`02` §4.4)
  - a claim smaller but true (`03` §2 item 1; `02` §5.3)
- **Y, unverified:**
  - LRP-specific data traps
  - polite correction of the earlier paper, with the solutions supplied
  - "a reviewer's objection is often a free experiment design"

  Y also leaves out heuristic or partial pricing, his documented first advice (R12).
- Neither arm names a limit of the lens.

The judge on the difference: "The two sets are close: both score 2 on H2 and H4, have no fabrications on T1, and rest T1 on the same documented practices. They differ in three places. On H1, Y names the empirical basis and the branching-rule compatibility limit, while X rests on the bound. On T1, X cites more of his specific practices: heuristic pricing, target plus general test sets, shifted means with the shifts printed. On B1, X flags that numerics are outside the lens and Y gives a confident verdict in his name."

## Reading

The sealed-item test is a tie with both totals high (5 and 6 of 6). The model already knows this researcher well on these decisions, so the skill's value has to show in the task test. It does show there, modestly. With the skill, the T1 answer rests on more of his documented practice (8 supported grounds against 6, 1 unverified against 3). It also carries specific moves the unaided answer lacks: heuristic pricing first, a target set plus a general set, and shifted means with the shift printed. No ground in the with-skill arm is fabricated, so that arm does not fail. The clearer gain is on the boundary: with the skill the answer marks numerics as outside the lens, while without it the answer gives a confident verdict in his name. The one item the skill lost, H1, does not look like the skill making the model disown what it knew. The skill carries a different reason for the same 2001 choice, the podcast's fear of writing tree management. The answer took that reason, plus later advice projected back onto the thesis, in place of the empirical justification in the thesis itself. The unaided arm reached that justification, though it overstated the result.

## Known weak points

- Left open by the fix rounds (no fix round is recorded after retention round 1):
  - the "grain of salt" quote in SKILL.md is not verbatim ("need" for "needs", sentence start dropped)
  - "Postponing the writing "to the end" is the worst idea you could have" and the "whatever method" remark on the master LP are in the notes but not in SKILL.md
  - the GCG design detail (original problem as the coordinating instance, master under a relaxation handler) is missing
  - the skill's own step text is easy to mistake for his words when quoted
- Added by this test:
  - The skill gives no measurable gain on the sealed decisions (tie, -1).
  - On H1 the podcast reason in the skill can push out the thesis's own reasoning, and answers drift into projecting later advice onto earlier work (two overclaims).
  - Neither arm named a blind spot of the lens in the task test, so the Honest Boundary is not reaching task answers.
  - The with-skill boundary answer kept its uncertainty but did not say outright that the notes have nothing from him on numerics.
  - Three sealed items is a small sample: one point either way decides the sign.

# Jorge Nocedal · Deep-reading synthesis

> Date: 2026-10-17. Input: every card in `cards/` (28 batch files, 181 card entries for 165 works; index in `07-paper-cards.md`, generated from the digests by `scripts/build_card_index.py`). Rules applied: `references/paper-reading-card.md` §3 (conservative update: append only, existing methods get evidence before anything new, a new core method needs ≥3 distinct works plus the four checks, reject updates without explanatory power, every claim traceable to a card) and `references/research-extraction-framework.md` §3 (four-way validation) and §11 (quality checklist). This note proposes changes; it does not edit `SKILL.md`. The base-tier skill was built on 2026-09-28 from web research only (01–06); this is the first synthesis of the deep reading, so there are no earlier decisions to keep or overturn.
>
> Citation form: `[S012 p. 9]` = card S012, page of the extracted file as recorded on the card (file pages; most files are author preprints or reports, and the cards give the journal offset where known). Version citations follow the cards: `[S032 arXiv p. N]`, `[S091 arXiv p. N]` and `[S080 arXiv p. N]` are arXiv files (v1 or v2 as each card states); `[S016 preprint p. N]` and `[S064 preprint p. N]` are the 2011 and 2012 author preprints; `[S035 report p. N]` is OTC Report 2002/4 (earlier title). Abstract- and metadata-level cards are cited by ID only. Quotation marks surround only text that is in a card's verified Quotes list (`verify_card_quotes.py`: 284 quotes, 257 exact, 27 matching after normalisation of spacing and symbols, 0 not found).
>
> Counting rules (operator notes, applied in every tally and threshold below):
> - **Ten works with two cards from one text** (S030 S067 S098 S111 S040 S057 S077 S119 S035 S075): round 1 read text layers without digits; round 2 (c2-01, s2-01) re-read OCR text with digits. Numbers, tables and parameter values come only from the round-2 cards; the round-1 cards are used for prose only. Two cards for one work count as one work.
> - **Six works upgraded in round 3** (S016 S043 S064 in c3-01; S120 S063 S139 in s3-01) also have an earlier abstract or metadata card; the deeper card is used, and each work counts once.
> - **Duplicates**: S126 (2006 report) is counted with S042 (2007 report, OMS 2008); S056 is counted with S143 (same L-BFGS-B report, probably). After merging, 157 distinct research works carry cards.
> - **Excluded**: S155 is not by Nocedal; S164, S165, S214, S215, S218 are non-research rows (Role = skip). None of them is used as evidence.
> - **NSF award records** (S167 S169 S173 S174 S176 S178 S184 S186 S187 S189 S190 S192 S195 S196 S198 S202 S206) are grant abstracts: used to date interests, never as the sole support of a method decision.
> - **Collective voice**: S179 and S188 are sections of RAL group progress reports in the group's "we" (S179's drafter may be Gould) [S179; S188]; S063 is the KNITRO 3.0 user manual [S063 p. 1]. They are product or group documentation, not Nocedal's own voice.
> - **Co-authorship and team exclusivity**: most works are co-authored (§9). Frank E. Curtis is already deep-tier in this team; the works co-authored with him (S110 S045 S081 S052 S068 S073 S004) are also in his corpus. A pattern enters as Nocedal's only if it passes exclusivity against the other nine members' SKILL.md files (Curtis at deep tier; the other eight at base tier).
> - Cards record some reading notes about inconsistencies inside works (typos, table/text mismatches). They are not findings about the researcher and are not used here.

---

## 1. Coverage

| Item | Count | Source |
|---|---|---|
| Scholar rows / distinct works indexed | 223 / 167 | `team_status.py --coverage` row (07 header) |
| Works with a card | 165 (159 research rows + 6 skip rows with metadata cards) | `07-paper-cards.md` |
| Distinct research works after the two merges | 157 | header rule |
| **Read in full** (deepest card) | **75** | read-level column |
| Read in part (partial) | 21 | read-level column |
| Abstract-level | 39 (15 of them NSF award abstracts) | batches a2-01, a2-02, a2-03 |
| Metadata only | 22 (2 of them NSF award records) | a2-01, a2-02, a2-03 |
| INDEX rows without a card | 2 talks, Role = skip (S146, S175) | INDEX.md |
| Card entries | 181: full 79, partial 28, abstract 44, metadata 30 | digests |
| Quotes verified | 284 / 284 (0 not found) | `verify_card_quotes.py` |

Full or partial reads by period (works): 1978–79 2; 1980–84 1; 1985–89 3; 1990–94 9; 1995–99 13; 2000–04 18; 2005–09 13; 2010–14 14; 2015–19 12; 2020–24 9; 2025–26 2 (96 in all; table in §8.1).

Signature works now read in the body: the 1980 limited-storage paper [S007], the 1989 L-BFGS study (prose only; its text layer lost all digits) [S002], the 1987 Broyden-class convergence paper [S020], the Acta Numerica survey [S019], NITRO [S008], the Byrd–Gilbert–Nocedal trust-region interior theory [S009], the 2003 benchmarking study [S078] (its numbers are unreadable in the file), the KNITRO package paper [S011], penalty steering [S042], the ECMWF case study [S047], the infeasibility-detection SQP [S052], the barrier-update study [S029], the 2011 L-BFGS-B Remark [S016 preprint], the SIAM Review survey [S004], the noisy finite-difference programme [S038; S072; S071; S091 arXiv; S080 arXiv; S082; S084; S124; S128] and the last paper on the list [S150]. Still known only from abstract or metadata: *Numerical Optimization* [S001], the 1989 Byrd–Nocedal analysis tool [S017], the negative-φ Broyden paper [S044], column scaling [S108], the 1990–91 numerical studies [S100; S025], most 1980s work (S116 S162 S109 S022 S086 S204 S123 S177 S103 and metadata rows), and the 2008 line-search penalty precursor [S140].

---

## 2. Evidence per existing method

Counts are distinct works (merges and exclusions above) whose card `method_links` point at the method; a work can give evidence and a variant. "FP" = full or partial read. Card-entry counts are in brackets.

| Method | Evidence ✅ works (FP) | Variant ⚠ works | Contradiction ✗ works | Works with any link (FP) |
|---|---|---|---|---|
| M1 Handicapped, method-level benchmarking | 51 (47) [55 cards] | 34 | 7: S005, S077, S042, S023, S082, S084, S124 | 71 (67) [77] |
| M2 Received wisdom on trial | 25 (22) [27] | 10 | 0 | 34 (31) [37] |
| M3 Keep the engine, repair one component | 50 (41) [54] | 29 | 0 | 72 (63) [79] |
| M4 Failure modes → options and next papers | 58 (54) [63] | 2: S120, S077 | 0 | 59 (55) [65] |
| M5 Theory must discriminate | 45 (37) [48] | 32 | 7: S007, S138, S013, S029, S023, S015, S033 | 74 (65) [79] |
| M6 Structure beats your own brand; integrate | 49 (40) [54] | 7 | 1: S197 | 54 (44) [60] |

Abstract-level evidence (incl. NSF records) is small everywhere: M1 4, M2 3, M3 9 (7 NSF), M4 4, M5 8, M6 9. No method decision below rests on it.

### 2.1 M1 · Handicapped, method-level benchmarking

**Strongest full-text evidence**
- The 2002 SLIQUE study already builds the rival-aligned stopping test a year before the 2003 protocol: "Although, it is nearly impossible to enforce a uniform stopping condition, the stopping conditions for SLIQUE and KNITRO were constructed to be very similar to that used in SNOPT." [S035 report p. 19]; limits count as failures, SNOPT gets a larger superbasics limit, SNOPT's 7 exits flagged optimal with the requested accuracy not achieved are not counted as successes for consistency, and the loss to the group's own KNITRO is printed (438, 506 and 455 of 560 solved by SLIQUE, KNITRO, SNOPT) [S035 report pp. 19–21].
- The 2003 benchmarking study confirms the SKILL wording (method-level goal, stopping test aligned by editing the own code, accounting corrections, own losses printed), though its numbers are unreadable in the file [S078 pp. 2, 6–7, 9–11, 14–15].
- 1989: competitors run "precisely as they recommend", same-solution check, losses in the abstract, full data in a companion report [S002 pp. 2, 7–8]; 1992: methods compared inside one code differing only in β [S012 p. 24]; 1999: NITRO and LANCELOT stopped at the same 10⁻⁷ [S008 pp. 20–23].
- Handicaps of the own side, in full text: rival credited with its best of 11 preconditioners (1998) [S034 p. 22]; a rival-neutral target from a derivative-based reference solve, medians of five runs, the bias against the rival named (2002) [S040 pp. 12–13, 15]; own method untuned against SG and SVRG tuned on a 21-point grid (2018) [S031 p. 6]; own CG parameters fixed in advance, rival given a step-length grid (2019) [S032 arXiv pp. 22, 24, 26]; sketching costs ignored, "the most optimistic for Newton-Sketch" (2020) [S041 p. 6]; KNITRO L-BFGS memory 1, rival codes from their communities' own benchmarks, the rival rerun at non-default settings (2021/23) [S080 arXiv pp. 4, 19, 27–28, 42–44].
- Compare inside one code base: Knitro/Direct against Knitro-CG sharing all other components [S013 p. 14]; interior codes taken from Knitro "to minimize the effect of implementation details" [S105 p. 3]; old and new infeasibility logic identical except the switch rule [S053 pp. 12–13].

**Say–do update.** Stated and practised 1989–2026 [S002 p. 8; S150 pp. 6–8], but not uniformly:
- The early L-BFGS-B papers run the rival only at defaults and count non-converged runs whose f matches the rival's as non-failures: "We do not interpret these as failures of the algorithm but feel that this property of LBFGS deserves further study" [S005 p. 9; S143 pp. 8–9; S003 pp. 18–23]. Step 4 (in SKILL: *hitting a limit counts as a failure*) holds from 2002 on [S035 report p. 19; S013 p. 14; S139 p. 15].
- Self-handicap (step 3) is sporadic before 2016 (S034, S040, S035) and regular in the 2016–2023 sampling and noise papers (S089 S031 S032 S041 S080).
- Step 7's stop rule (illustrative problems with no aggregate) is met in many papers that state their scope: [S052 p. 16; S051 pp. 24–29; S064 preprint p. 19; S004 p. 17; S082 pp. 18, 20; S084 pp. 15–16; S124 p. 29]. SKILL names only the 2024 case.
- *Losses in the abstract* holds in [S002 p. 2] and [S105 p. 1]; it does not hold in the v1 abstract of the 2021 study, where the loss is in the §1.2 contribution list [S080 arXiv pp. 1, 6] (later versions not read), nor in [S015 p. 1] or [S139 p. 15].
- Proposed mark: ✅ stated + practised 1989–2026, with the early form weaker on failure accounting and the step-7 rule frequently relaxed with stated scope.

**Contradictions** (7 works): failure accounting [S005 p. 9]; the simple baseline (plain L-BFGS, one end of the family) has no column [S077 pp. 4, 9–11]; two efficiency claims given without a table [S042 pp. 13, 20]; own parameters swept, baseline fixed, one problem [S023 pp. 12–17]; illustrative runs with no aggregate [S082 pp. 18, 20, 27–34; S084 pp. 15–16; S124 p. 29].

**Limitations confirmed**: KNITRO as platform and comparator, with an Artelys co-author and no conflict-of-interest statement [S080 arXiv pp. 1, 27]; KNITRO also as the baseline and subproblem solver in 2026, with the rival DFO codes excluded on stated grounds [S150 pp. 6–7]; the group's own KNITRO as comparator in 2002 [S035 report pp. 18–19].

### 2.2 M2 · Put the field's received wisdom on trial

**Strongest full-text evidence**: the geometry phase dropped [S062 pp. 2, 4–5, 7, 9]; finite-difference BFGS against direct search and interpolation, with a result recorded as contrary to conventional wisdom [S038 pp. 6, 21]; the dismissal of finite differences tested with the simplest h, the rival's wins printed, the verdict handed to others to check [S080 arXiv pp. 4, 6, 9, 11]; the LP corrector folklore tested by removing its hidden ingredient, PCx falling from 90 to 28 of 94 [S029 pp. 17, 20]; the huge fixed penalty ablated, 485 → 449 → 321 of 616 [S042 pp. 15–16]; the fashionable stochastic inner solver against CG, the classical tool winning [S041 pp. 2, 7–8]; the view that SGD is to be preferred put on trial [S018 pp. 6–7, 14]; the common practice of avoiding line searches tested both ways [S128 pp. 10–13].

**Say–do update.** SKILL dates the practice 2009–2025. The full texts push it back: plain BFGS beats the self-scaling refinement on most problems (1993) [S054 p. 16]; the comforting view that Jacobian regularization removes the difficulty is stated and refuted on the simplest example (2004) [S061 pp. 11–12]; does the penalty need updating at all? (2006) [S027 pp. 7, 22]. Proposed mark: ✅ stated + practised 1993–2026.

**Variant to add: the dismissed option can be a method that theory favoured but nobody implemented carefully.** 1990, as PI: "However we believe that conjugate gradient methods have not been properly implemented so far, and that their full potential needs to be assessed." [S197 p. 4]; a careful implementation of one theory-only trust-region SQP class [S034 p. 22; S028 p. 34]; SLP-EQP revived, after little attention, because million-variable LP codes had become available [S035 report pp. 2, 4]; FIBO rehabilitated by auditing why the earlier evidence failed (accounting of finite-differenced constraints, a weak baseline) [S150 pp. 2, 6, 9]: "The numerical results reported in [6], and subsequently in [4], are, however, inconclusive and the FIBO approach is rarely (if ever) used in practice." [S150 p. 2].

**Moving DFO verdict**: SKILL's list starts in 2009. A 2002 point precedes it: the wedge method enforces geometry at every step, and finite-difference L-BFGS-B loses on reliability (five failures against one) [S040 pp. 2–3, 7, 15]. Other variants: received safeguards rejected by argument rather than experiment [S019 p. 7; S071 p. 6]; the classical tool defended against a newer challenger [S032 arXiv pp. 3, 27]; the sharpness–generalization link adopted as well known [S006 pp. 1, 3–5] (SKILL warning sign 8 already records it).

### 2.3 M3 · Keep the classical engine; repair only the component that breaks

**Strongest full-text evidence**: finite-difference L-BFGS with a noise-based interval, a relaxed Armijo test, a five-case recovery tree and its ablation [S038 pp. 6–11, 21]; the noise-tolerant BFGS with its split-phase line search and recovery logic [S071 pp. 1–6, 13–16, 18–23]; the noisy trust region changing only the ratio test [S082 pp. 2, 4–5, 11, 18–19]; the constrained noisy SQP whose repair is ablated and whose estimate is stressed 10× to 1000× both ways [S084 pp. 2–3, 18–20]; the adaptive interval replacing an unknowable derivative by a testable ratio [S091 arXiv pp. 2, 4, 11–12, 15–17]; only the derivative oracle and one Armijo test changed, nothing else in L-BFGS [S080 arXiv pp. 12–13, 26]; the infeasibility mode driven by the normal step's feasibility estimate, with a return test and exits [S053 pp. 5–6, 8–9, 12]; the reduced-Hessian cross-term repaired at an explicit KKT-error trigger and ablated [S067 pp. 5–9, 15–18]; L-BFGS kept under bounds, the failing line search replaced [S003 pp. 6, 18–19]; the projected-CG drift repaired by an internal cosine diagnostic with refinement as recovery [S021 pp. 8, 13–14, 17–21].

**Say–do update.** SKILL dates it 2007–2025. Engine-kept, one-component repairs appear from 1993–95 [S193 pp. 3–4; S003 pp. 6, 18–19; S028 pp. 4, 10, 16, 30], and the estimate-driven form from 2002 (the ν∞ LP sets the penalty) [S035 report pp. 14–16]. Step 4 (recovery tree and exit flags) is the least practised step: built in [S038 pp. 9–11], [S071 pp. 12–14], [S053 pp. 9, 12], [S036 pp. 14–17]; named as necessary but not built in [S084 p. 20]; absent in [S082 p. 18], [S124 pp. 4–5, 33], [S018 pp. 6, 18]; only proposed in [S015 p. 19]. Proposed mark: ✅ stated + practised 1993–2025; step 4 ⚠ partial.

**Worked case (penalty steering), corrections from full texts**
- The problem was named in 1993: "In practice, however, the penalty parameter may become large too soon, and this forces the iterates to follow the constraints too closely." [S193 p. 4].
- The first rule is in SLIQUE (2002): re-solve the step LP with the objective gradient switched off, keep ν when no progress is possible, demand a fraction ε = 0.1 of the attainable reduction, reset ν when it grows too large [S035 report pp. 14–16]; theoretical root in the SLQP convergence paper [S058 pp. 19–20].
- SKILL's worked case records, from the 2007 preprint (p. 20), an open question on extending the guidelines to penalty line-search methods; it was answered by the same group in 2012 with the line-search steering method [S051 pp. 1–2, 4–6, 30]: "There is no switch in Algorithm I, which always takes steps based on the penalty function φπ." [S051 p. 25].
- SKILL's *Inferred link* to the 2010 infeasibility-detection SQP is now confirmed from the body: the update is built in the spirit of the steering rules, with a ρ = 0 reference step [S052 pp. 14–16].
- Steering is reused unchanged as a module inside the 2011 PLA implementation [S139 pp. 4–5].

**Variant notes to add (practice detail, not new methods)**
- *Zero-noise collapse as the design check*: the repaired method reduces exactly to the classical one when the estimate is zero [S071 pp. 13, 25; S082 pp. 11, 23; S084 p. 15; S102 pp. 5, 8, 11; S124 pp. 28–29]. The same reduction check is shared by Fletcher (Method 5 step 1) and Gill (Method 1) in their skills, so it stays a step detail.
- *Oracle arm in the ablation*: run the method with the true value of the estimated quantity, labelled for benchmarking purposes only, to locate the gap in the estimator [S091 arXiv pp. 17–18; S080 arXiv pp. 13, 23–24, 38–40; S068 p. 20]. Curtis's Method 1 step 4 has the same move (an idealized ceiling, from the co-authored S068), so it stays a step detail.
- *Explicit estimate of attainable progress by an extreme-value probe*: ν = ∞ LP [S042 pp. 8–11], ρ = 0 reference step [S052 p. 15], σ = 0 and σ = 1 solves [S029 pp. 5, 8].
- *Pre-noise variants* (engine kept, but no estimate or recovery): [S007 pp. 1–2; S012 pp. 11–12, 20; S014 pp. 4, 13; S009 pp. 4, 17–18; S040 pp. 3, 5, 11; S150 pp. 3, 5–6]; a fallback to a second engine rather than a repaired component [S011 pp. 5–7; S013 pp. 4–5, 8, 12]; cost rather than failure as the trigger [S023 pp. 5, 10; S024 pp. 2–3, 11–12].

**Limitations confirmed**: noise-aware constrained work remains equality-constrained [S084 pp. 2–3, 5, 20; S124 pp. 4–5]; general constraints appear only in the noiseless 2026 DFO letter, whose noise claim is untested [S150 pp. 5, 9–10]. Page correction: the SKILL stop line's quoted phrase *are not robust* is on p. 6 (§1.2), not in Appendix A [S080 arXiv p. 6].

### 2.4 M4 · Failure modes and open questions → solver options and next papers

**Strongest full-text evidence**: KNITRO's lack of infeasibility handling becomes the 2014 paper and ships as `bar_switchrule=2`: "The performance of the interior point methods knitro/direct and knitro/cg are quite poor, which may not be surprising since these two algorithms do not contain any features for handling infeasibility." [S053 pp. 1, 4, 13]; the Wächter–Biegler counterexample analysed as a specification, with a configuration that cannot fail [S061 pp. 2, 14, 19–24]; an external counterexample run on the own code already in 2001 [S111 pp. 13–15, 19–21]; the undecided subspace minimization shipped as `isbmin` [S003 pp. 11, 23; S005 pp. 5–6]; two selection rules shipped as `IOP` [S098 pp. 4, 7]; the steering open question answered [S051 pp. 1–2, 30]; the KNITRO manual documents exit code −2 for infeasible stationary points and tells users to "try both options" in 2003 [S063 pp. 1, 4, 37–38]; the own failure case GAUSSELM as specification, shipped as KNITRO's feasible mode [S075 pp. 8–18]; the 2024 noisy trust region shipped as a KNITRO option with the noise level as input [S124 p. 29].

**Say–do update.** SKILL dates it 1999–2014. Practice runs 1989–2024: two line-search modes as code options [S002 p. 13]; application needs written into next year's plan [S197 pp. 4–5; S193 pp. 3–4]; the 2024 KNITRO option [S124 p. 29]. Proposed mark: ✅ stated + practised 1989–2024.

**Corrections**
- Step 3 says *two independent frameworks*. In the 2009 barrier study the two frameworks are the authors' own codes (Wächter, IPOPT's author, is a co-author) [S029 pp. 1–2, 25]; the 2004 starting-point study pairs KNITRO with a bare code built for the purpose [S085 pp. 6, 8]. Suggested wording: *two frameworks, ideally including one you do not own*.
- The infeasibility arrow (2006 limitation → 2010/2014 papers) is now partly documented: the 2014 paper restates the limitation [S053 p. 4]; the 2010 paper cites the 2006 package paper but not its limitation sentence [S052 p. 18]. The barrier arrow (2006 option → 2009 study) stays inferred: the 2009 paper does not mention the option [S029 pp. 2, 17–21].

**Variant**: undecided choices adapted automatically from in-run signals, with only m left to the user, because the goal is parameter-free algorithms [S077 pp. 2, 5–7]; known weaknesses turned into lemmas, repairs deferred (1978) [S120 pp. 45–48].

### 2.5 M5 · Theory must discriminate between practical methods

**Strongest full-text evidence**: the Broyden-class analysis "as implemented in practice" that singles out DFP and confirms it with a targeted run: "Nevertheless, we have seen in this paper that the DFP method can be much less efficient than the BFGS method, and that the reason for this is that it lacks the self-correcting property given by the fourth term on the right-hand side of equation (3.2)." [S020 pp. 1, 10, 17–19]; CG theory explaining FR stalling and PR recovering, with experiment parameters set to the theorem's [S012 pp. 4–6, 11–12, 24, 27]; the Acta survey's two tests and numbered open questions [S019 pp. 1–2, 7, 17–24]; self-scaling separated from BFGS [S054 pp. 10–11, 15–18]; merit choices separated (KKT-norm merit can fail, barrier merit cannot) [S061 pp. 11–13, 16–22]; Theorem 4.1 separating line-search from trust-region slack resets [S075 p. 11]; Cauchy decrease separating methods that can stall at infeasible points [S111 pp. 5–10, 13–22]; a rate, not only convergence, in the infeasible case [S052 pp. 12, 16]; the corrected BAS method separated from BAS (130 against 0 failures) [S064 preprint pp. 13, 17]; a spectrum-dependent CG bound tied to plotted spectra [S041 pp. 11–16, 32–33]; a bound plotted against runs and called pessimistic, with its (ε_f, ε_g) scaling tested over a grid [S082 pp. 19–22].

**Say–do update: ⚠ partial.** The stated value is constant ("Ironically our many theoretical studies of variable metric methods have not resulted in the discovery of new methods but have mainly served to explain phenomena observed in practice" [S019 p. 16]). Practice splits by period:
- 1987–2004: steps 1–3 practised in most theory papers listed above.
- 2006–2025: several theorems cannot discriminate by construction: global convergence asserted by analogy [S013 pp. 2, 4]; a safety net that holds for any μ rule [S029 pp. 10–12, 22]; convergence for any positive definite Hessian sample [S023 pp. 5, 7, 11]; an O(1/k) theorem that H_k = I also satisfies [S015 pp. 3, 12–14, 29]. The group says so itself: "where the provable convergence rate for L-BFGS is no better than for steepest descent, even though L-BFGS is superior in practice." [S038 p. 14].
- From 2012 the analysed iteration is often a simplified one, with the gap stated: fixed step and imposed sample growth [S018 pp. 6, 11, 15]; fixed step and an extra test [S031 pp. 5, 12]; H_k = I with plain backtracking [S038 pp. 12, 19]; an outline algorithm [S071 pp. 10–12]; a stripped SQP [S084 pp. 2, 4–5, 15]; an idealized test [S102 pp. 7–14]; an over-cautious setting [S128 pp. 9, 11]. "The focus of this section is on the development of a practical algorithm, not on establishing complexity bounds, and therefore our method is an extension of Algorithm 3.1 and not of the idealized variant given by (4.23)-(4.24)." [S018 p. 15].
- Step 4 (bound plotted against runs) appears in [S082 pp. 19–22], [S021 p. 12], [S057 pp. 24, 26], [S041 pp. 14–15] and, for an estimator, [S091 arXiv pp. 15–16]; it is absent in most 2016–2025 theory sections [S033 p. 6; S031 p. 5; S032 arXiv pp. 19–20; S072 p. 24; S071 p. 15; S124 pp. 29–30].
- Proposed mark: ✅ stated throughout; ✅ practised 1987–2004; ⚠ 2006–2025, where most theorems are safety nets or analyses of a simplified iteration and the discrimination rests on numerics.

**Correction (Dai 2002)**: SKILL's Limitations say Dai 2002 overtook the 1992 claim, *with no response found*. A 2016 group paper cites Dai and Mascarenhas as showing that BFGS fails on nonconvex problems and adopts cautious updating in response [S033 p. 6]; the 2018 progressive-batching method skips updates when yᵀs ≤ ε‖s‖² [S031 p. 5]. Replace *with no response found* by *acknowledged in 2016 and met with cautious updating [S033 p. 6]*. The 1992 survey already listed nonconvex BFGS as Open Question II [S019 pp. 21–22].

**Tension evidence (IT5)**: the co-authored survey credits SG's success to its superior work-complexity guarantees [S004 p. 82] while a 2020 paper rejects a worst-case bound: "That analysis, however, underestimates the power of the SSN-CG method on problems with favorable eigenvalue distributions and yields complexity estimates that are not indicative of its practical performance." [S041 p. 11]. Early analysed-versus-run gaps [S007 pp. 5–6, 9; S138 p. 77] are early-career and closed by [S020] and [S002 pp. 21–24].

### 2.6 M6 · Structure beats your own brand; integrate complementary algorithms

**Strongest full-text evidence**: the co-authored ECMWF case study explains why quasi-Newton Hessians, his own family, were rejected for operational 4D-Var; which choices are the authors' own is not stated [S047 pp. 1, 13] (wording revised after review, 2026-10-17): "Moreover, a quasi-Newton approximation to (6) ignores the “least-squares” structure of this Hessian, namely, that the first term in (6) involves only first-derivative information." [S047 pp. 7–8]; the 1997 survey shows his own L-BFGS losing to Newton and partially separable quasi-Newton [S049 pp. 2–7, 13–15]; partitioned quasi-Newton recommended over the own method [S002 p. 24; S019 pp. 29–30]; the own codes' structure-blindness printed as a drawback [S003 p. 23; S005 p. 3]; specialist bound-constrained codes beat the general solvers [S105 pp. 7, 20]; SG, not L-BFGS, at the centre of the ML map [S004 pp. 16–19, 78]; the sub-sampled Newton method twice as fast as L-BFGS on its problem [S023 pp. 4, 16]; the own preconditioner scoped against incomplete Cholesky [S098 pp. 4, 8; S030 pp. 12, 18]; interior and active-set integration on the LP/MIP analogy [S011 pp. 2–3, 20–22]; owners of an interior code build and benchmark an active-set alternative [S035 report pp. 2, 29–30]; FIBO recommended only for its cost structure [S150 pp. 2, 5, 8–9].

**Say–do**: ✅ stated + practised 1989–2026 (no change in mark). The ECMWF limitation in SKILL (*paper not read*) is replaced: the paper confirms the Gauss–Newton choice and its reasons, credits the multilevel method to Courtier et al., and does not say which parts are the authors' own [S047 pp. 1, 13, 16].

**Contradiction**: a 1990 nonlinear least-squares application solved with L-BFGS and compared only with general CG and quasi-Newton codes [S197 p. 2]. **Variants**: L-BFGS named the universal choice for structured sparse inverse covariance [S043 p. 7]; structure exploited inside the generic method's linear algebra [S014 pp. 15, 17–18]; general-purpose robustness preferred to MPCC structure [S051 p. 28].

**Variant to add: integration at the algorithm level.** Besides KNITRO's code-level integration, the full texts show a recurring design of one parameterized family with two classical methods at its ends: the variable-storage family between CG and BFGS with storage as the knob [S138 pp. 7, 77–79; S120 pp. 23–24, 27]; memory m in L-BFGS-B [S143 pp. 2–3, 9]; HFN and L-BFGS interlaced, both as special cases [S077 pp. 3, 5; S088 p. 2]; a flexible penalty spanning a fixed penalty and a one-element filter [S081 pp. 4–5]; SL-QP to SQP through one model [S114 pp. 2, 8]; a semismooth Newton framework generating the rival ℓ1 classes [S064 preprint pp. 2–6]; the strongest rival recast as a wasteful parameter setting of the own scheme [S015 p. 27]. Placing rivals inside one family is shared with Toint (Method 2 step 5, *unify*) and Gill (Method 3, *old-family check*), so it is recorded as a Method 6 variant, not a new method.

### 2.7 Heuristics, taste marks and signature works with new full-text evidence

| Item | New full-text evidence |
|---|---|
| H1 Failure demo first | one chosen 2-D function with the trace as diagnostic [S020 p. 18]; GAUSSELM with ‖Δs‖ [S075 pp. 5, 14]; analytic example before tests [S067 pp. 13–14]; two 1-D counterexamples revisited after the rule [S042 pp. 6–8, 13–15]; one example per theorem case [S052 pp. 17–21]; failure on an easy problem first [S071 pp. 2–3; S082 pp. 2, 4–5; S102 pp. 2–3] |
| H2 Instrument the inside | safeguard-firing column [S012 p. 25]; trigger shares of the trust-region fallback [S013 p. 16]; monotone-mode share [S029 p. 16]; share of iterations with the wedge active [S040 p. 13]; internal counters beside profiles [S105 pp. 4–5, 7–8]; per-task time shares [S035 report p. 28]; s–y angle and GradError/HvError [S015 pp. 19–21]; skipped-update counters [S005 pp. 6–7]; log symptom → option map in the manual [S063 pp. 37–38] |
| H3 Noise-free before noisy | §2 noise-free, §5 noisy, then ablation [S038 pp. 3–5, 19–22]; the deterministic limit first, reported as a loss [S023 p. 12]; every section of [S080 arXiv pp. 9, 13]; identical noise in both arms [S082 p. 21] |
| H4 Exhaust alternatives | Gill–Murray scaling dropped [S002 p. 15]; several selection strategies tried, the two simplest kept [S030 pp. 2, 20]; other HFN variants tried [S077 p. 10] |
| H5 Cheapest adequate option; numbers | the simple μ rule kept over superlinear rules [S013 p. 10]; m ∈ [4, 20] [S098 p. 4]; ν0 = 10, ε1 = 0.1, ε2 = 0.5 [S042 p. 13]; ECnoise 4/6 evaluations [S038 p. 12]; PLA defaults [S139 pp. 6, 10–11, 14]. Pricing every device in base-iteration units: one backsolve [S075 p. 15]; under 4% extra simplex iterations [S035 report p. 16]; factor × maxcg ≈ 1 [S023 p. 6]; the SQN cost ratio [S015 p. 8]; 4md and 2m + n [S004 pp. 47, 57]; operation counts against each alternative [S014 pp. 12–13, 19–20] |
| H6 Robustness before speed | rate deferred on practical grounds [S029 p. 22]; NITRO's linear barrier decrease [S008 p. 23]; speed-ups deferred [S064 preprint pp. 17–18]; global theory first, rate deferred [S009 pp. 9, 33] |
| H7 Code as a numbered, maintained artefact | the Remark: a machine-precision constant wrong by two orders of magnitude replaced, the old version's accounting corrected in its favour [S016 preprint pp. 1–2]; graded drivers and a must-read driver [S005 pp. 5–6]; a numbered TOMS algorithm [S098 pp. 6–7]; representation → algorithm → code staircase [S014 p. 3; S003 pp. 5, 23; S005 p. 2] |
| H8 Prototype inside the production solver | Knitro/Direct [S013 p. 14]; infeasibility mode inside KNITRO 8.0 [S053 pp. 12–13]; PLA inside knitro [S139 pp. 3, 14–17]; finite differences through KNITRO's own option [S080 arXiv p. 27]; a KNITRO failure observation as the start [S084 pp. 2–3] |
| H9 Enter a field through a practitioner's problem | ECMWF co-authors [S047 p. 1]; Google speech data and co-author [S023 pp. 1, 14]; IBM collaborators [S043 p. 1]; chemical process control [S067 p. 19]; the ML field map before the group's methods [S004 pp. 20, 40, 51] |
| H10 A standing theory partner | Byrd co-authors 37 of the 96 full/partial works and appears in every five-year period 1985–2024; several 2018–2026 student works are without him (S031 S041 S080 S091 S124 S128 S150) (§9) |
| Taste mark 4 (self-correction) | the trace term DFP lacks [S020 pp. 8, 19]; unproductive steps acting like a geometry phase, kept as a conjecture [S062 p. 7] |
| Taste warning sign 2 | his own non-discriminating theorems [S015 pp. 12–14; S023 pp. 7, 11; S029 pp. 10–12] (§2.5) |
| IT1 theory or experiments first | practice first, rationale later: the merit rule adopted for efficiency and derived afterwards [S013 pp. 6–7; S042 pp. 18–20]; theory promised for a future study [S053 p. 16]; theory certifying a working heuristic [S113 p. 21]; the implementation report reinstating a safeguard the theory paper dropped: "In addition, we include a trust region constraint in (2.2) for greater control and robustness." [S139 p. 3] |
| IT3 print losses, yet trim failures | omissions declared in the text from the start: a weak configuration withheld [S007 p. 9]; an erratic scaling not reported [S002 p. 15]; a slightly weaker variant not tabulated [S030 p. 8]; SQN v2 has no *Preliminary Approach* section, consistent with its deletion [S015] |

Signature-work anatomies that the full texts fill: L-BFGS 1989 [S002 pp. 3, 6–8, 12, 15, 24]; Acta 1992 (no longer *thin*) [S019 pp. 1–2, 7, 14, 17–24, 29–31] with its underlying theory [S020]; KNITRO 2006 [S011 pp. 1–3, 5–7, 14–15, 20–22] with Knitro/Direct [S013]; the noise programme [S038; S072; S071; S091 arXiv; S080 arXiv; S082; S084; S124; S128].

---

## 3. Variants and contradictions

### 3.1 Contradiction links, card by card

| Card | Method | What the full text shows | Consequence |
|---|---|---|---|
| S007 1980 | M5 | analysis on quadratics with exact line searches, tests with an inexact search [S007 pp. 5–6, 9] | early-career; closed by [S020] and [S002 pp. 21–24]; no change |
| S138 1978 | M5 | tests use SR1 while theorems cover the restricted Broyden class, acknowledged [S138 p. 77] | early-career; no change |
| S005 1997 | M1 | non-converged runs matching the rival's f not counted as failures [S005 p. 9] | say–do note (§2.1) |
| S077 2002 | M1 | plain L-BFGS, the obvious baseline, has no column [S077 pp. 4, 9–11] | say–do note |
| S042 2008 | M1 | two efficiency claims without a table [S042 pp. 13, 20] | say–do note; the huge-ν ablation does give counts [S042 pp. 15–16] |
| S023 2011 | M1, M5 | own parameters swept, baseline fixed, one problem [S023 pp. 12–17]; a theorem that would bless a steepest-descent-like variant [S023 pp. 5, 7, 11] | say–do notes |
| S013 2006 | M5 | convergence of the shipped hybrid asserted by analogy [S013 pp. 2, 4] | M5 ⚠ |
| S029 2009 | M5 | a safety-net theorem for any μ rule; preference rests on profiles [S029 pp. 10–12, 22] | M5 ⚠ |
| S015 2016 | M5 | O(1/k) for any bounded H_k, SGD included [S015 pp. 12–14, 29] | M5 ⚠ |
| S033 2016 | M5 (SKILL text) | Dai 2002 cited and answered with cautious updating [S033 p. 6] | **correct SKILL Method 5 Limitations** |
| S082 / S084 2023, S124 2024 | M1 | illustrative runs with no aggregate [S082 pp. 18, 20; S084 pp. 15–16; S124 p. 29] | already the SKILL step-7 example; list widened |
| S197 1990 | M6 | least-squares application solved with L-BFGS only [S197 p. 2] | add as an early counter-case |

### 3.2 Claims in SKILL.md that the full texts change

1. **Method 5 Limitations, Dai 2002, *no response found*** → acknowledged in 2016, with Li–Fukushima cautious updating adopted for the paper's own nonconvex analysis [S033 p. 6; S031 p. 5] (after review, 2026-10-17: *answered* was too strong; the device predates Dai).
2. **Trajectory, *c. 1992–2009 data assimilation (ECMWF)*** → meteorology is already an application in the DOE progress report of 1989–90, which says L-BFGS is being used on problems in meteorology and oceanography and plans 4-D assimilation for the next year [S197 pp. 2, 4]; the NSF award abstracts of 1990 and 1991 name meteorology and variational data assimilation [S198; S196]; a 1992 award names parameter estimation in meteorology and oceanography [S195]; the 1993 DOE report is titled for meteorology and oceanography and counts one CRAY hour per simulation [S193 p. 2]; a 2001 award is with NCEP [S186]; the ECMWF co-authorship appears in 2009 [S047 p. 1]. Proposed row: *c. 1989/90–2009, meteorology and data assimilation (DOE/NSF-funded from 1990; ECMWF co-authors by 2009)*. When the ECMWF contact itself began is not dated by any card (the interview remains the only source).
3. **Method 3 Stop line, *are not robust* (App. A)** → p. 6, §1.2 [S080 arXiv p. 6].
4. **Method 3 worked case** → problem named 1993 [S193 p. 4]; first rule 2002 [S035 report pp. 14–16]; the line-search open question answered 2012 [S051 pp. 1–2, 30]; the 2010 link confirmed from the body [S052 p. 14].
5. **Method 4 step 3, *two independent frameworks*** → the 2009 frameworks are the authors' own codes [S029 pp. 1–2, 25].
6. **Method 4 arrows** → infeasibility arrow partly documented [S053 p. 4]; barrier arrow still inferred [S029].
7. **Method 1 step 7 / Taste mark 8, *losses in the abstract (arXiv:2102.09762)*** → v1 puts the loss in §1.2, not the abstract [S080 arXiv pp. 1, 6]; later versions not read. Label the claim version-dependent.
8. **Say–do dates**: M2 1993–2026 [S054 p. 16]; M3 1993–2025 [S193 pp. 3–4; S035 report pp. 14–16] (after review: planned 1993 in a progress report, practised from 1995 [S003 pp. 6, 18–19], estimate-driven from 2002); M4 1989–2024 [S002 p. 13; S124 p. 29]; M5 ⚠ partial after 2005 (§2.5).
9. **Routing table, two medium-confidence rows** (*read in abstract only*): doi:10.1137/080738222 is now read in full [S052], and doi:10.1137/060649513 [S029]. Both rows can drop the *abstract only* caveat; the barrier row keeps *no complete theory* (stated, caption-derived) and gains the full-text verdict: "We have seen in this paper that, both for linear and nonlinear programming, classical barrier update strategies with global convergence guarantees are overly conservative, while strategies that are often fastest in practice are based on heuristic formulas and are not globally convergent." [S029 p. 21].
10. **Method 6 Limitations, ECMWF *paper not read*** → read [S047]; reasons confirmed, own role not stated [S047 pp. 13, 16].
11. **Honest Boundary *Not read* list** → now read: the 1980 paper [S007], the 1987 theory paper [S020], Byrd–Gilbert–Nocedal 2000 [S009], the ECMWF paper [S047], the 2011 Remark [S016 preprint]. Still not read: *Numerical Optimization* [S001], the 1989 tool paper [S017].
12. **Signature Work, Acta 1992, *Thin (underlying papers not read)*** → the survey and the 1987 body are read [S019; S020].

### 3.3 Variant notes (summary of §2)

M1: early weaker form; step-7 rule relaxed with stated scope. M2: rehabilitate the under-implemented method; the 2002 DFO point. M3: zero-noise collapse; oracle arm; extreme-value probe; pre-noise variants; recovery step weakest. M4: automatic adaptation instead of an option [S077]. M5: period split. M6: algorithm-level integration.

---

## 4. Promotions

The skill has six core methods, so one promotion keeps it within 3–7. One cluster passes all four checks and adds explanatory power that no existing method supplies; a second also passes, but it is weaker and goes to the heuristics (§5, H11) to keep the method count at seven.

### Promote → Method 7: Spend accuracy where the iteration needs it (decouple gradient and curvature samples)

**Cluster** (merged by meaning from the candidates *asymmetric accuracy*, *allocate sample accuracy by component tolerance*, *decouple and amortize noisy estimates* and part of *error balancing*): S023, S018, S015, S033, S004, S032, with S031 as a further instance. Six distinct full/partial works, 2011–2019.

**Four checks**
1. **Cross-project recurrence** ✅: SAA Newton-CG and stochastically initialized L-BFGS on Google speech data (2011) [S023 pp. 3, 5–6, 10]; dynamic gradient samples with a fixed Hessian/gradient sample ratio and a CG stop tied to the Hessian sampling error (2012) [S018 pp. 4–5, 15–17]; stochastic quasi-Newton with curvature pairs on their own sample and a slower clock (2016) [S015 pp. 5, 8–9]; multi-batch and fault-tolerant L-BFGS with pairs on batch overlaps (2016) [S033 pp. 3–5]; overlap pairs in progressive batching (2018) [S031 pp. 4–5]; the SIAM Review account of both devices (2018) [S004 pp. 53–54, 57–58]; the theory: a constant Hessian sample suffices for a linear rate while the gradient sample must grow geometrically (2016/2019) [S032 arXiv pp. 6, 8, 11]. Four distinct projects (SAA second-order, stochastic quasi-Newton, distributed L-BFGS, subsampled Newton theory) over eight years.
2. **Say–do consistency** ✅: the principle is stated as the design rationale in the papers: "Our approach is based on the fact that less accuracy in the Hessian is required than in the gradient" [S023 p. 3]; "This observation is based on an important property of Newton-like methods, namely that there is much more freedom in choosing a Hessian approximation than in computing the gradient [7, 3]." [S033 p. 3]. The why of the second device is stated too: "quasi-Newton updating is inherently an overwriting process rather than an averaging process, and therefore the vector y must reflect the action of the Hessian of the entire objective F given in (1.1)" [S015 p. 5]. Outside the cards, the Purdue 2017 talk transcript (caption-derived, `references/sources/talks/2017-02-15_purdue-distinguished-seminar_srg3Rx2HvfQ.txt`, [0:51:41]) says the Hessian sample will be smaller than the gradient sample because the gradient matters more (paraphrase; not a card). Practice matches the statement in every work of the cluster.
3. **Executable, and different from standard practice** ✅: the steps below produce actions that differ from the default of one mini-batch for every quantity and an update at every step. The strongest rival is recast as exactly that default and shown wasteful: oLBFGS ≈ SQN with L = 1 and b = b_H, which the paper calls an inefficient allocation of effort [S015 pp. 26–27].
4. **Exclusivity** ✅: no other member's SKILL.md treats sample allocation between gradient and curvature (searches for subsampled Hessians, curvature pairs, sample sizes and stochastic quasi-Newton found nothing outside this skill). Curtis co-authored only the survey [S004]. One part overlaps: tying the inner CG stop to the outer error [S018 pp. 15–17; S032 arXiv pp. 16–17] is close to Curtis's Method 1 (the inner solve serves the outer solver); that step is cited as shared, not claimed as exclusive.

**Explanatory gain**: the cards link S018, S004, S031 and S033 to Method 3 as evidence and S023 and S015 as variants, and S032 has no Method 3 link (corrected after review, 2026-10-17; the earlier sentence here said *only as variants*). Method 3 repairs a failing component; this cluster allocates samples and clocks between components. In S023 the trigger is cost, not a failure [S023 pp. 5, 10]; in S015 the repair is a design of sampling and schedule, not one driven by an explicit noise-level estimate [S015 pp. 5–7, 19]. Method 3 does not explain what is sampled, how much and on which clock; Method 7 does. It also gives the routing table a home for *design a stochastic or subsampled second-order method*, which today has no route.

**Proposed text for SKILL.md**

> ### Method 7: Spend accuracy where the iteration needs it (decouple the gradient and curvature samples)
> **One line**: In a sampled or inexact second-order method, give the gradient the accuracy, give curvature its own cheap, consistent and amortized sample, grow only what the iteration cannot tolerate, and price everything in gradient evaluations.
> **Evidence**: Stated (co-authored): [S023 p. 3]; [S033 p. 3]; [S015 p. 5]. Practice: [S023 pp. 5–6]; [S018 pp. 4–5, 15–17]; [S015 pp. 5, 8–9, 27]; [S033 pp. 3, 7]; [S031 pp. 4–5]; [S004 pp. 53–54, 57–58]; [S032 arXiv pp. 6, 8, 11]. Say–do: ✅ stated (papers; Purdue 2017 talk, caption-derived) + practised 2011–2019.
> **Steps**:
> 1. List the oracle components the iteration consumes (gradient, Hessian-vector products or curvature pairs, inner solve) and how much error each tolerates: curvature only shapes the step, the gradient decides descent [S023 p. 3; S004 p. 53].
> 2. Give curvature its own sample: a fixed fraction of the gradient sample, fixed so as not to add parameters to tune [S018 p. 15], or a separate, larger sample on a slower clock (every L iterations) [S015 pp. 5, 8–9]. Compute both ends of a curvature pair on the same data (the batch overlap) [S033 p. 3; S031 pp. 4–5].
> 3. Grow only the accuracy-critical component: the gradient sample by a variance test with a geometric backup [S018 pp. 4–5; S004 p. 45]; keep the Hessian sample constant unless a superlinear rate is the goal [S032 arXiv pp. 6, 8, 11].
> 4. Price every component as a fraction of one gradient evaluation (maxcg × factor ≈ 1 [S023 p. 6]; the ratio 1 + 2M/b + 2b_H/(3bL) [S015 p. 8]) on an axis that charges the extra samples (accessed data points) [S023 p. 16; S018 p. 19; S015 p. 15].
> 5. Ablate: the deterministic limit first, reported even when it loses [S023 p. 12]; pairs from different samples [S033 p. 7]; M = 0 to show the gain is curvature, not scaling [S015 pp. 20, 23]; the same-sample rival as a parameter setting of your scheme [S015 p. 27].
>    - 🔴 Stop if the curvature overhead is far from one gradient per iteration at the user's batch size [S015 p. 8; S023 p. 6], or if the method loses in its deterministic limit [S023 p. 12]; subsampled Newton-CG is recommended only for large gradient samples [S004 p. 54].
> **Applies to stage**: algorithm design for finite sums, stochastic and distributed problems.
> **Different from standard practice**: one batch for every quantity, curvature updated every step [S015 p. 27].
> **Limitations**: convex or strongly convex theory [S023 p. 7; S015 pp. 9–10; S032 arXiv p. 5]; the theorems do not separate the method from SGD, so the case rests on numerics [S015 pp. 12–14]; one data set or single runs in several papers [S023 p. 16; S018 pp. 18–25; S015 §4]; on deep networks the progressive-batching method needs more gradient evaluations than SG and Adam [S031 p. 7]; finite sums with cheap Hessian-vector products; the inner-solve step overlaps Curtis's Method 1. Four of the six works are co-authored with Byrd (S023 S018 S015 S032).

**Placement**: Method 7 (appended, so that card references to Methods 1–6 stay valid). Routing row to add: *Design or fix a subsampled / stochastic Newton or quasi-Newton method* → Method 7, then Methods 3 and 1; Heuristic 3. Roundtable Card *Leads when* gains *sampled second-order methods*.

---

## 5. New heuristics

**H11 · Harvest the curvature the solver already computes, and do not throw it away.** "The key idea is to preserve the information generated during the inner CG iteration to improve the quality of the limited memory matrix used in subsequent steps" [S088 p. 7]. Cases: CG pairs from one linear solve precondition the next, at no extra matrix-vector products [S030 pp. 2, 4, 6; S098 p. 4]; inner pairs feed the L-BFGS memory in a hybrid with both parents as special cases [S077 p. 3; S088 pp. 5–7]; quasi-Newton matrices mapped into a new null-space basis instead of reset [S067 pp. 11–12]; the origin of L-BFGS itself: "A disadvantage of these methods is that after a certain number of iterations the quasi-Newton matrix is discarded" [S007 p. 1]. Scope as printed: "the cost of applying the preconditioner is too high to offset the reduction in the number of CG iterations in these experiments" [S030 p. 12]; "Therefore the preconditioner is unlikely to be useful for very sparse problems." [S098 p. 8]. Ablation arm: identical except that the harvested pairs are discarded [S088 p. 8].
- Checks: executable ✅; recurrence ✅ (1980; 1996–2002, four works); exclusivity ✅ (no member's methods); say ✅ in the papers' own statements [S088 p. 7; S007 p. 1]. It would pass as a method, but (a) the method slot goes to Method 7, and no existing method is weak enough to replace; (b) the idea has prior art that the paper credits (Nash's matrix, O'Leary–Yeremin, Byrd–Nocedal–Zhu) [S030 p. 3]; (c) the line ends in 2002 and its payoff is scoped by the authors. Kept as a heuristic, cross-referenced from Method 6 (algorithm-level integration).

**H12 · Validate every in-algorithm estimate against the truth, and stress it in both directions.** Cases: the sample-variance estimate tabulated against the true gradient error over a real run [S018 p. 20]; model gradients measured against exact AMPL gradients instead of bounds with unknown constants [S062 p. 8]; GradError and HvError against full-data quantities [S015 pp. 20–21]; a misspecification sweep of the noise level from 1/10 to 10 [S071 p. 20]; the estimate run 10×, 100× and 1000× too large and too small [S084 p. 19]; the direction of failure written for each misestimate [S091 arXiv p. 12; S128 pp. 9–11]; one failure of the estimate computed by hand [S080 arXiv p. 17].
- Checks: executable ✅; recurrence ✅ (2009–2025, seven works, several co-author groups); exclusivity ✅ (Wright's floating-point check and Curtis's yardstick audit test other things); no stated principle found → heuristic. It fills a gap in Method 3, whose steps use explicit estimates but never say how to trust them.

---

## 6. Candidate pool (not promoted)

Counts are distinct works with full or partial cards (abstract-level in brackets).

| Cluster (candidate names merged by meaning) | Works | Checks passed | Where it goes |
|---|---|---|---|
| Two-phase design: a cheap predictor (Cauchy point, LP, ISTA, projected gradient) carries the proof and the active set, a second-order subspace phase carries the rate | 12: S003 S139 S060 S113 S114 S087 S089 S043 S016 S064 S076 S092 (+S178 S135) | executable, recurrence | technique inventory; field-standard design (the gradient-projection framework of Conn–Gould–Toint and Moré–Toraldo, named as the entry in [S003 p. 3]) shared with Toint and Gould; no explanatory gain |
| Collapse / special-case reduction check | 10: S071 S082 S084 S102 S124 S081 S068 S051 S011 S077 (+S177) | executable, recurrence | Method 3 step detail (§2.3); shared with Fletcher, Gill, Curtis |
| Family with two classical methods at its ends; rival recast as a parameter setting | 9: S138 S120 S143 S077 S081 S114 S064 S015 S018 (+S116) | executable, recurrence | Method 6 variant (§2.6); shared with Toint, Gill |
| Map a new or rival method onto a known one; transfer the classical theorem through an equivalence | 10: S007 S002 S120 S009 S021 S061 S078 S018 S118 S115 (+S022 S086 S123 S177 S103) | recurrence | proof devices (§7.1) |
| Computable proxy for an unavailable quantity | 6: S045 S068 S018 S053 S006 S091 | executable, recurrence | Method 3 evidence (explicit estimate; 🔴 checkpoint) |
| Oracle (idealized-estimate) arm | 3: S068 S091 S080 | executable, recurrence | Method 3 step 5 detail; shared with Curtis |
| Degenerate-parameter ablation; predecessor as control | 7: S110 S076 S015 S003 S005 S067 S073 | executable, recurrence | Method 3 step 5 / Method 1 step 5 evidence |
| Component-isolating analysis on a simplified iteration | 7: S031 S038 S041 S018 S071 S084 S102 | recurrence | Method 5 say–do gap (§2.5), not a recommendation |
| Specify by admissible conditions so the theory covers the code; proof-driven or rarely binding safeguards | 11: S035 S058 S042 S028 S046 S040 S024 S008 S089 S036 S139 (+S108) | recurrence | Method 5 step 1 device; shared with Wächter (Method 3) |
| Failure outcomes as cases of the global theorem | 4: S009 S061 S073 S051 | recurrence | Method 4 evidence; shared with Ye (Method 1) and Curtis |
| Extreme-value probe to set a trade-off parameter | 3: S029 S052 S042 | executable, recurrence | Method 3 evidence; steering shared with Curtis (Method 2) |
| One continuous parameter instead of a mode switch | 2: S052 S051 | — | Curtis Method 2 (*Steer, don't switch*); rejected as Nocedal's |
| Error balancing for inner solves; tolerance coupling | 4: S018 S032 S041 S013 | executable, recurrence | shared with Curtis Method 1; noted in Method 7 |
| Price devices in base-iteration units | 9: S014 S035 S075 S042 S045 S004 S015 S023 S002 | executable, recurrence | Heuristic 5 evidence |
| Two-set noise-floor convergence template | 3: S082 S084 S124 | recurrence | proof device; Method 3 step 6 evidence |
| Benign setting first; experiments inside the theorem's assumptions | 4: S045 S072 S068 S039 | recurrence | Method 3 step 6 / Method 5 variant |
| Practice first, rationale later; implementation report reinstating safeguards | 4: S013 S042 S053 S139 (+S113) | recurrence | IT1 evidence (§2.7) |
| Motivate-and-revisit toy examples | 3: S067 S042 S052 | executable, recurrence | Heuristic 1 evidence |
| Cite the rival's own data | 4: S011 S040 S042 S092 | executable, recurrence | Method 1 step 1 evidence |
| Re-check a failure label against the quantity that matters; audit the rival's accounting | 2: S057 S150 | executable | Method 1 / Method 2 evidence; shared with Curtis Method 4 |
| Rehabilitate the under-implemented method | 5: S197 S034 S028 S035 S150 | executable, recurrence | Method 2 variant (§2.2) |
| Switch on local-convergence devices only near the solution | 2: S067 S077 | executable | pool (one co-author line) |
| Make the safeguard unnecessary by construction | 2: S040 S015 | — | technique (§7.2) |
| Monotone CG-iterate norm as a design invariant | 2: S049 S008 | — | technique (§7.2) |
| Explain the incumbent's popularity, then keep its strength | 2: S076 S092 | — | pool (one LCP project) |
| Algorithms as network services; software as a stated deliverable | 2: S119 S098 (+S190 S189 S187 S180 S198 S196 S195, grant abstracts) | — | trajectory and H7 note; grant evidence is weak |
| Progressive sampling as variance control | inside Method 7 / Method 3 (S018 S036 S031 S102; +S169 S167 grant abstracts) | — | Method 7 step 3 |
| Single-card candidates | S006 hypothesis-discriminating study; S031 idealized performance model; S004 survey by trade-offs; S047 formulation by explicit criteria; S088 controlled spectral family; S105 specialist yardstick on an isolating class; S008 small typified set plus broad set; S080 stratify outcomes before profiling; S053 self-exposing snapshot, hysteresis; S073 controlled perturbation of a test set; S091 invariance as a requirement; S033 one repair for two settings; S002 cost-split reporting; S102 look-ahead accuracy test; S128 fragile-operations audit, telemetry-driven calibration; S039 assumptions labelled optimistic; S057 low-dimensional representativeness | — | technique inventory; S128's fragile-operations audit [S128 p. 1] sharpens Method 3 step 1 |

---

## 7. Technique inventory

### 7.1 Proof devices
- **Trace–determinant bookkeeping**: the trace catches large eigenvalues, the determinant small ones; the term DFP lacks is the explanation [S020 pp. 7–10, 17; S019 pp. 18–21]; uniform bounds for limited memory, every matrix being m updates of a bounded seed [S002 pp. 21–23]; the same lemma made free by building y as a sub-sampled Hessian-vector product [S015 pp. 10–12].
- **Transfer the classical theorem through an equivalence**: every special-update matrix is a usual BFGS matrix from some start [S007 p. 7]; an inexact inner solve written as an explicit SPD initial matrix by completing the Krylov projector [S023 p. 11]; quadratic termination by identity with fixed-preconditioner PCG [S007 pp. 5–6].
- **Family-level theorem that locates the boundary member**, with sharpness by a recycled counterexample and a property that defines the class: [S020 pp. 1, 10, 19; S012 pp. 11–13, 16–17, 20–22; S019 p. 14]; a practical-reachability check of counterexamples [S019 pp. 13–14].
- **Zoutendijk hub and the template in which ‖d‖² grows at most linearly** [S012 pp. 7–8; S019 p. 5]; contradiction through a positive quantity driven negative [S020 pp. 10–11].
- **Analyse the growth a test would force, then the idealized variant imposing it**; total work by a geometric sum [S018 pp. 11–14; S004 pp. 43–45].
- **Prove once for an abstract direction** (two lemmas cover SG, mini-batch and stochastic quasi-Newton) [S004 pp. 22–24, 72, 75]; a general-H_k theorem plus an eigenvalue lemma [S015 pp. 12–14].
- **Reuse the own classical tool in the new regime** (the 1989 good-iterates theorem in the noisy BFGS analyses) [S072 pp. 3, 13–14, 25; S071 pp. 7, 10–11].
- **Rate in the infeasible case**: triangle inequality through the penalty path, an implicit-function O(ρ) bound and a Newton contraction uniform in ρ [S052 pp. 8–12].
- **Error budget with fixed shares** (1/8 + 1/8 of the contraction) [S032 arXiv p. 16; S041 pp. 12–13]; a case split on the relative gradient error in noisy line searches [S038 pp. 15–17].
- **Two-set noise-floor template**: a critical region visited infinitely often, a level set never left [S082 pp. 11–17; S084 pp. 13–15; S124 pp. 9–16].
- **Filter-area argument** for any filter-supervised scheme [S029 pp. 12–13].
- **Failure outcomes as theorem cases**: "The practical value of our analysis as we will show is that the situations under which Algorithm I can fail represent problem characteristics that are of interest to a user and that can be characterized in simple mathematical terms" [S009 p. 20]; [S061 pp. 5–10, 14–24; S051 p. 24].
- **Theory that covers the code by inclusion of conditions** [S042 p. 13; S058 pp. 10, 24; S035 report p. 7]; constants of the experiments set to the theorem's [S012 p. 24].

### 7.2 Algorithm-design moves
- Product form to delete or reorder corrections [S007 pp. 2–3]; compact representations for constrained and sparse use [S014 pp. 5–9, 15–18]; auxiliary vectors that carry inner products along a breakpoint search [S003 pp. 8–9].
- Harvest by-products (H11) [S030; S098; S077; S088; S067]; decouple gradient and curvature samples (Method 7).
- Parameter set against the best attainable progress (ν = ∞ LP, ρ = 0, σ ∈ {0, 1}) [S035 report pp. 15–16; S042 pp. 8–11; S052 p. 15; S029 pp. 5, 8].
- Free/monotone supervision that interferes only on stalls: "This observation suggests that the globalization scheme that we propose in Section 5 should interfere minimally with the iteration; it should be active only when the algorithms appears to be making no progress." [S029 pp. 7, 9–12]; hysteresis on mode switches [S053 p. 12]; line-search steps guarded by a trust-region fallback with a radius hand-off [S013 pp. 5, 8, 12; S011 pp. 5–7; S024 pp. 3, 11–12].
- Inner and outer tolerances coupled so the barrier subproblem is never oversolved [S013 pp. 10–12].
- Choose the architecture whose by-products measure what the new feature needs (the normal step yields the attainable feasibility reduction) [S053 pp. 2, 5].
- Fold a safeguard into the step subproblem (the wedge) and keep rejected points that improve the model [S040 pp. 3, 5–7]; make a safeguard unnecessary by constructing the estimate [S015 pp. 5, 10–12].
- Gate expensive local devices on a size-independent KKT error [S067 pp. 7, 9, 13, 15; S077 p. 6].
- Reverse communication for user control and remote services [S005 pp. 3–4; S119 pp. 3, 7; S098 pp. 5–6; S063 pp. 3, 43].
- Change only the derivative oracle and one acceptance test of an existing code: "In other words, in the finite-difference approach to derivative-free optimization, algorithms do not need to be constructed from scratch but can be built as adaptations of existing codes." [S080 arXiv pp. 13, 26]; replace only the step computation of an unconstrained code [S150 p. 3].

### 7.3 Experiment and evaluation protocols
- Stopping tests aligned with the rival [S035 report p. 19; S078 pp. 6–7; S008 pp. 20–23; S005 p. 8; S003 p. 18]; limits as failures, success defined identically [S035 report pp. 19–21; S013 p. 14; S139 p. 15].
- Same-solution filter, with the number dropped per code [S002 p. 8; S012 p. 24; S029 p. 7]; stratify outcomes before profiling [S080 arXiv pp. 28–29].
- CPU time only where set-up cost does not dominate, evaluations everywhere [S013 p. 14; S003 p. 23; S139 p. 18].
- Failure taxonomy by name and cause [S029 pp. 16–17]; termination cross-table over the full set to show a feature is harmless [S053 pp. 13–14]; log₂ ratio plots for two-solver comparisons [S053 p. 13; S080 arXiv p. 9; S150 p. 7].
- A rival-neutral target from a derivative-based reference solve [S040 pp. 12–13; S062 pp. 4–5].
- Controlled inner-solver tests on a frozen Hessian: 51 systems with random right-hand sides, the first solved by plain CG to build the preconditioner, the other 50 preconditioned [S030 p. 7]; a synthetic family varying condition number and eigenvalue distribution one at a time [S088 pp. 9–11].
- Infeasible instances made from feasible ones by one added constraint or bound [S052 pp. 18–19; S073 p. 23].
- A cost axis that charges every sample (accessed data points; effective gradient evaluations) [S023 p. 16; S018 p. 19; S015 p. 15; S041 p. 8]; an equal work budget swept over a log grid [S041 p. 8].
- Noise-free, then noisy with the rival community's profile machinery, then ablation of the new safeguard [S038 pp. 3–5, 19–22]; misspecification sweeps [S071 p. 20; S084 p. 19]; oracle arms [S091 arXiv pp. 17–18; S080 arXiv pp. 13, 23–24].
- The rival at non-default settings in an appendix [S080 arXiv pp. 42–44].

### 7.4 Writing moves
- Numbered open questions and a four-way classification of results [S019 pp. 2, 17, 21–22]; intuition before rigour, labelled non-rigorous; only the hub lemma proved in full [S019 pp. 5, 19].
- A limitations section before any result [S080 arXiv p. 7]; numbered drawbacks next to numbered advantages [S005 p. 3]; a two-sided verdict tied to problem features [S003 p. 23].
- Surprise recorded as surprise [S062 pp. 2, 5, 7; S029 p. 21; S041 pp. 7–8; S057 p. 18]; conjectures labelled [S042 p. 5; S062 pp. 6, 9].
- Open with the mislabelled failure: "Initially we reported this as a failure of the limited memory code to achieve high accuracy in the solution, but a closer examination of the results revealed that in some of these runs the limited memory code had actually produced a lower function value than LANCELOT." [S057 p. 2].
- State what the rest of the paper must argue, including the cost measure [S015 p. 7]; a dated paragraph separating concurrent work [S032 arXiv p. 3]; a comparison table labelled as a summary, not a ranking [S032 arXiv pp. 20–21]; a ranking disclaimer next to the results [S003 p. 23; S078 p. 2].
- A counterfactual about the field: "We believe that if such comparisons had been made, particularly in the noiseless setting, research in the field would have followed a different path." [S080 arXiv p. 4].

---

## 8. Trajectory as seen in the full texts

### 8.1 Topics by period (full or partial reads)

| Period | Works | Main topics (cards) |
|---|---|---|
| 1978–79 | 2 | CG and variable-storage methods: S120 (with Nazareth), S138 (thesis) |
| 1980–84 | 1 | limited-storage BFGS, sole author: S007 |
| 1985–89 | 3 | Broyden-class theory with Byrd and Yuan: S020; L-BFGS study with Liu: S002; inverse eigenvalue problems: S026 |
| 1990–94 | 9 | CG and quasi-Newton theory: S012 S019 S054; L-BFGS linear algebra and software: S014 S115 S143; reduced Hessian theory: S039; PI reports with meteorology: S197 S193 |
| 1995–99 | 13 | bound constraints: S003 S005; large unconstrained: S049 S088 S024 S101; constrained and interior (NITRO): S028 S046 S034 S118 S008; service and teaching: S160 S090 |
| 2000–04 | 18 | interior and active-set solvers, KNITRO, SLIQUE: S009 S067 S021 S111 S075 S061 S078 S085 S063 S035 S179 S188; preconditioning and enriched methods: S030 S098 S077; S057; DFO: S040; iNEOS: S119 |
| 2005–09 | 13 | KNITRO, penalty and barrier rules: S058 S011 S013 S042 S105 S029 S027 S110; inexact SQP and flexible penalties with Curtis: S045 S081; LCP: S076; ECMWF case study: S047; DFO geometry: S062 |
| 2010–14 | 14 | infeasibility and inexact Newton: S052 S068 S073 S053; penalty and PLA active-set: S051 S060 S114 S139; L-BFGS-B Remark: S016; ML sampling: S023 S018; sparse inverse covariance: S043; LCP and finance: S092 S113 |
| 2015–19 | 12 | ℓ1 second-order methods: S087 S064 S050 S089; stochastic and ML methods: S006 S015 S033 S004 S031 S036 S032; noisy DFO: S038 |
| 2020–24 | 9 | noise: S072 S071 S091 S080 S082 S084 S124; sampling: S041 S102 |
| 2025–26 | 2 | noise design guidelines: S128; feasible constrained DFO: S150 |

The 1980s are thin in full text (3 works); most of that decade is abstract or metadata only (S116 S162 S109 S022 S086 S204 S123 S177 S103 S017 and metadata rows).

### 8.2 Turns
- **1978–80, from CG to limited memory**: the variable-storage family between CG and BFGS [S120 pp. 23–24, 27; S138 pp. 7, 77–79] becomes the update that never discards the matrix wholesale [S007 p. 1].
- **1987, theory with Byrd**: the family-wide analysis that singles out DFP [S020 pp. 1, 19].
- **1989–90, meteorology as the application**: L-BFGS in meteorology and oceanography and 4-D assimilation planned [S197 pp. 2, 4]; grant abstracts 1990–92 [S198; S196; S195]; one CRAY hour per simulation [S193 p. 2]; the ECMWF case study with practitioners in 2009 [S047 p. 1]. This corrects SKILL's c. 1992 start (§3.2).
- **c. 1995–2004, constrained solvers**: reduced Hessian SQP [S039; S028; S067], interior methods [S046; S118; S008; S009], then KNITRO and the 2002 active-set code [S035 report pp. 17–18; S011]; teaching and service in the same years [S090; S160].
- **2008–2013, side line in complementarity and option pricing** with Morales, Feng and Linetsky [S076; S092; S113], not in SKILL's trajectory table.
- **2011, machine learning through Google data** [S023 pp. 1, 14; S018 p. 18], then Intel collaborators [S006; S031] and the field map [S004].
- **2019, noise**: the noisy-DFO programme opens [S038 p. 1] and runs to the 2025 design guidelines [S128].
- **2024–26, back to model-based DFO for constraints** [S150 pp. 1–3], the endpoint of the moving verdict on interpolation methods [S040; S062; S080 arXiv pp. 6, 15; S150 p. 5].

### 8.3 What stayed constant
- **The quasi-Newton engine**: from the 1980 update [S007] to noise-tolerant BFGS [S071] and KNITRO's L-BFGS inside the 2026 baseline [S150 p. 7].
- **Benchmarking hygiene**: rivals run as their authors recommend and the same answer checked (1989) [S002 p. 8] to aligned termination through the baseline's options (2026) [S150 p. 7].
- **Failure modes and open choices written into the paper** [S019 pp. 17, 21–22; S035 report pp. 7, 29, 31; S080 arXiv pp. 7, 15–16, 32].
- **Numbers given as defaults** [S098 p. 4; S042 p. 13; S038 p. 12; S139 p. 14].
- **The Byrd partnership** (§9).

---

## 9. Collaboration pattern

| Period | Full/partial works | Most frequent co-authors (works) |
|---|---|---|
| 1978–89 | 6 | Nazareth (S120), Byrd (S020), Yuan (S020), Liu (S002), Friedland and Overton (S026); sole author S007, S138 |
| 1990–94 | 9 | Byrd 3 (S014 S039 S143), Gilbert 2 (S012 S115), Zhu and Lu (S143), Schnabel (S014), Yuan (S054); sole author S019; PI reports S197 S193 |
| 1995–99 | 13 | Byrd 6 (S003 S005 S008 S046 S088 S118), Zhu 3, Lu 2, Hribar (S008), Biegler and Schmid (S028), Yuan (S024), Lalee and Plantenga (S034); sole author S049, S160 |
| 2000–04 | 18 | Waltz 5, Byrd 5, Gould 4 (S021 S035 S179 S188), Morales 4 (S030 S098 S077 S078), Marazzi 3 (S040 S061 S111), Hribar 2 |
| 2005–09 | 13 | Waltz 6, Byrd 4 (S011 S042 S045 S058), Morales 3, Curtis 3 (S110 S045 S081), Wächter (S029), Fisher, Trémolet and Wright (S047) |
| 2010–14 | 14 | Byrd 7, Wu 4 (S018 S060 S114 S139), Morales 3, Waltz 3, Curtis 3 (S052 S068 S073), Oztoprak 2 |
| 2015–19 | 12 | Byrd 7, Oztoprak 3, Bollapragada 3 (S031 S036 S032), Berahas 2 (S033 S038), Intel co-authors (S006 S031) |
| 2020–26 | 11 | Byrd 4 (S071 S072 S084 S102), Xie 4 (S071 S072 S091 S102), Shi 3 (S071 S080 S091; also S031, 2018), Sun 3 (S082 S124 S128), Xuan 3 (S080 S091 S150), Bollapragada 2 (S041 S102), Oztoprak 2 (S080 S084), Berahas 1 (S041) |

- **Byrd** co-authors 37 of the 96 full/partial works (1987 [S020] to 2024 [S102]), more than twice any other partner; he is thanked rather than listed in several others [S002 p. 25; S029 p. 22; S053 p. 17; S082 p. 23]. No 2025–26 work lists him [S128; S150].
- **Product and solver partners**: Waltz 14 works (2002–2014, KNITRO); Morales 10 (2000–2012, preconditioning, KNITRO, LCP); Oztoprak 7 (2012–2023, including the Artelys years [S080 arXiv p. 1; S084]).
- **Team members as co-authors**: Curtis 7 works (2007–2018: S110 S045 S081 S052 S068 S073 S004), Gould 6 (1998–2005), Wächter 3 as co-author (S029 S073 S089), Wright 1 in full text (S047; the works list's Wright co-authorship of S049 is not borne out by its title page [S049 p. 1]).
- **Sole authorship** ends with the 1990s in the research papers read [S007; S138; S019; S049]; PI reports and a book review are in his own voice [S197; S193; S160].
- **Industry and laboratory co-authors** mark the entries into new fields: Google [S023; S018; S015], Intel [S006; S031], IBM [S043; S029], ECMWF [S047], Artelys [S080 arXiv p. 1], Weidlinger [S119].
- **Collective documents** (S179, S188, S063) are group or product voice (header).

---

## 10. Rejected updates

1. Promote *rival recast as a member of your own family* (unify): shared with Toint (Method 2 step 5) and Gill (Method 3 step 2) → Method 6 variant and technique only.
2. Promote the collapse/special-case check: shared with Fletcher (Method 5 step 1), Gill (Method 1), Curtis (taste 6) → Method 3 step detail.
3. Promote the two-phase active-set design: field-standard design [S003 p. 3] shared with Toint and Gould; no explanatory gain → technique.
4. Promote *one continuous parameter instead of a mode switch*: Curtis Method 2 → rejected as Nocedal's.
5. Promote *failure outcomes as theorem cases*: Ye Method 1 and Curtis → Method 4 evidence.
6. Promote *error balancing for inner solves*: Curtis Method 1 → noted as shared inside Method 7.
7. Add the oracle arm as a heuristic: Curtis already has it from the co-authored S068 → Method 3 step detail.
8. Promote *audit the termination measure or the rival's accounting*: Curtis Method 4 → Method 1 / Method 2 evidence.
9. Promote *admissible-condition specification*: Wächter Method 3 → Method 5 practice device.
10. Add *practice first, rationale later* as a heuristic: it is a tension (IT1), not advice.
11. Add *price devices in base units* and *cite the rival's own data* as new items: already Heuristic 5 and Method 1 step 1; evidence only.
12. Promote *algorithms as network services*: rests mainly on NSF award abstracts → trajectory and H7 note.
13. Promote H11 to a core method: passes the checks but would push the skill to eight methods; no weaker method to replace (§5).
14. Use numbers or table values from the round-1 cards of the ten no-digit works: rejected; only round-2 numbers are used.
15. Count S126 with S042, or S056 with S143, as two works; count S155 or Role-skip rows: rejected.
16. Treat S063, S179 or S188 as Nocedal's own voice: rejected.
17. Use card reading notes about typos or table/text mismatches as findings: rejected.
18. Use the NSF award abstracts as the main support for any method decision: rejected; they date interests only (§3.2 item 2).

---

## 11. Open gaps

- **The textbook** [S001] and the 1999 book entry [S010] are known only from metadata or abstract: the strongest stated-methodology source on how he teaches algorithm design is unread.
- **The 1989 analysis tool** [S017] behind Method 5's theory for backtracking line searches is abstract only; so are the negative-φ Broyden paper [S044], column scaling [S108] and the 1990–91 numerical studies [S100; S025]. Method 5's 1989 evidence rests on [S002] and on abstracts.
- **The 1980s**: three works in full text; the reduced-Hessian work with Overton [S022], the conic methods [S086; S103], the 1985 step-direction evaluation [S204] and the trust-region view of CG [S177] are abstract only. How the early methods were chosen and tested is uncertain.
- **The penalty line-search precursor** [S140] (2008, metadata) and the MPEC interior work [S181] are unread; the 2012 answer [S051] is read only partially (proofs of Lemmas 3.8–3.11 not followed).
- **KNITRO internals**: the KNITRO 2.0 manual [S066] is metadata only; the 3.0 manual [S063] documents options and exits, not how defaults were tuned.
- **The ECMWF role**: the paper read describes the operational system and does not say which parts are the authors' own [S047 pp. 1, 16]; the 2001 NCEP award is an abstract [S186]; the interview remains the only source for the origin story.
- **The 1989 L-BFGS study's numbers**: its text layer lost all digits [S002]; table-level claims about it still rest on the web research.
- **The 2003 benchmark's numbers** are unreadable [S078]; SKILL's 2003 figures still rest on the preprint read in the base tier.
- **Later versions**: the OMS 2023 version of the finite-difference study (abstract wording, §3.2 item 7) [S080 arXiv], the journal versions of S032, S091 and S150, and the SQN v1 *Preliminary Approach* [S015] were not read.
- **Recent and competition work**: the 2024 SCOPF entry [S166] and the 2020 sampling award [S167] are abstracts; the declared pause of the 2026 interview cannot be checked from the cards.
- **Methods 4 and 6 at the product level** depend on an owned commercial solver; no card documents how KNITRO's integration and crossover were tuned [S011 pp. 20–22].

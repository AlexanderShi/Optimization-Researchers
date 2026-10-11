# Samuel Burer · Evidence ledger

> Date: 2026-10-10 (stage T3.6, deep-reading synthesis). The full evidence behind `../../SKILL.md`. SKILL.md keeps, per item, the strongest statement, three to five cards, a one-line say–do count, at most four variant or correction bullets and a link to the matching section below. Each section here has two parts: **Before 2026-10-10** reproduces, verbatim, the SKILL.md wording built from web research (notes 01–06) before any full text was read, so nothing of the earlier evidence is lost; **Full texts (2026-10-10)** adds the evidence of the paper cards, taken from `08-deep-reading-synthesis.md` and the card digests. Nothing in the second part is new reading: it is the synthesis of the 73 card entries indexed in `07-paper-cards.md`.

**How to read.** `[S012 p. 9]` is paper card S012 in `07-paper-cards.md`, at the page of the PDF that was read (the version named on the card). Eighteen cards were read from a substitute version and every page citation to them carries the version word (preprint: S012, S014, S016, S024, S051; arXiv: S019, S023, S027, S038, S039, S044, S045, S048, S049, S050, S055, S056, S057); their published versions were not read. S058 and S065 are arXiv-only works, cited plainly. See the [card key](#card-key). Look up the journal page before citing a page in a paper. In the *Before* blocks, `[02 T5]`-style tags point to the web-research notes 01–06 and journal page numbers are those of the published versions. Marks: ✅ evidence · ⚠ variant (kept, nothing deleted) · ✗ contradiction or correction. Counts of supporting, variant and contradicting cards are distinct cards whose digest links to the item (`08` §2); a card can be both evidence and variant. Quotation marks enclose only text copied from a card's verified quote list (`verify_card_quotes.py`: 138 quotes, 0 not found) or, in the *Before* blocks, text quoted by the web-research notes. Named proof devices, design moves, protocols and writing moves (P1–P9, D1–D6, E1–E7, W1–W8) are in `../technique-catalog.md`.

**Reading notes are not findings.** The cards record small inconsistencies noticed while reading (caption counts, typos, values that differ between pages). None is used here as a claim about Burer or his coauthors; the one general lesson kept is neutral: in long computational papers, recheck that captions, totals and text agree after each revision.

## Contents

- [Taste: marks of good research](#taste-marks)
- [Taste: warning signs of bad research](#taste-warnings)
- [Method 1: Package the difficulty in one convex object, then attack the object](#method-1)
- [Method 2: Kitchen sink first, then the hull of a small substructure](#method-2)
- [Method 3: Let computation propose, certify exactly, narrow publicly when wrong](#method-3)
- [Method 4: Engineer the hard pool, disclose the filter, keep the ladder](#method-4)
- [Method 5: Prototype first, let theory follow](#method-5)
- [Method 6: Solve in the cheap nonconvex space, certify in the convex dual](#method-6)
- [Stage workflows: techniques added from the full texts](#workflows)
- Heuristics: [H1](#heuristic-1) · [H2](#heuristic-2) · [H3](#heuristic-3) · [H4](#heuristic-4) · [H5](#heuristic-5) · [H6](#heuristic-6) · [H7](#heuristic-7) · [H8](#heuristic-8) · [H9](#heuristic-9) · [H10](#heuristic-10) · [H11](#heuristic-11) · [H12](#heuristic-12)
- Anatomies: [low-rank 2003](#anatomy-low-rank) · [copositive 2009](#anatomy-copositive) · [finite B&B 2008](#anatomy-finite-bb) · [SOC-RLT 2013](#anatomy-soc-trs) · [slight lift 2025](#anatomy-slight-lift) · [QuadprogBB 2012](#anatomy-quadprogbb) · [submodular 2025](#anatomy-submodular)
- [Research anti-patterns](#anti-patterns)
- [Research trajectory](#research-trajectory)
- [Inner tensions](#inner-tensions)
- [Coverage and remaining gaps](#coverage)
- [Corrections from the full texts](#corrections)
- [Card key](#card-key)

---

<a id="taste-marks"></a>

## Taste: marks of good research

**Before 2026-10-10** (SKILL.md wording, verbatim):

> 1. **Aim at the convex hull even when out of reach.** "Nevertheless, much can be learned by trying to characterize all the cuts." (2015, pp. 1–2); "Want tight conic relaxations using relaxation machinery" (Kurt-Fest slides, 2023, slide 16) [stated].
> 2. **The product is a tight relaxation or "a single strong bound", valid irrespective of the data**, not polynomial-time solvability: "We are also not specifically concerned with the global optimization of (MIQCP)." (Burer & Saxena 2009/12, p. 2) [stated-joint]; "In contrast, we are interested in computing a single strong bound" (arXiv 2303.01624v1, p. 2) [stated].
> 3. **Simple, explicit, compact descriptions you can picture.** "Geometric insight is stressed throughout." (2015, p. 2); compact representations show "kind of geometrically what's happening" (2021 [53:29], ASR).
> 4. **Unification:** one object covers known special cases, so progress transfers ("package" quote; "This is the promise and the goal of copositive optimization.", 2015, p. 2).
> 5. **A result counts when it beats the strongest known combination head-to-head:** "we have demonstrated that the new class of valid inequalities strengthens the strongest known SDP relaxation" (Eltved & Burer, *Math. Program.* 197, 2023, p. 305) [stated-joint]; the 2021 "kitchen sink".

**Full texts (2026-10-10).**
1. *Aim at the hull.* The 2012 survey states the programme: "For example, analyzing — and generating cutting planes for — the various convex hulls that arise in MINLPs (see Section 5.4) will require aspects of both polyhedral theory and convex analysis to achieve best results." [S002 p. 8]; the 2024 encyclopedia entry closes on the same aim, "Additional novel techniques are needed to generate strong valid inequalities for quadratic hulls." [S067 p. 6]; hulls attempted even when only exploratory results come out, "While we have not been able to answer this question fully, we now describe some exploratory results." [S010 p. 9].
2. *A single strong bound valid irrespective of the data.* "In this paper, however, we seek a relaxation that is strong irrespective of the data." [S049 arXiv p. 2]; the same aim in the TTRS work, "We believe it is still interesting to seek the convex relaxation that solves TTRS exactly." [S033 p. 2]. Dated [inferred, revised on review 2026-10-10]: stated by 2011/12, "We are also not specifically concerned with the global optimization of (MIQCP)." [S016 preprint p. 2], and pursued in the hull papers from 2009 [S011; S010]; it ran alongside the finite KKT branch-and-bound line of 2008–2012 (Heuristic 12 below, now a dated Method 1 variant) [S007 p. 3; S008 pp. 4, 6], after which the cards hold no new global QP solver.
3. *Simple, explicit, picturable descriptions.* Easiest-to-hardest exposition [S024 preprint p. 3]; 2-D envelope figure before the tables [S049 arXiv pp. 13-14]; an exactness hypothesis rewritten as a geometric condition [S061 pp. 2-3]; validity separated from sufficiency, "Another useful feature of our approach is that we clearly distinguish the conditions guaranteeing validity of our relaxation from those ensuring sufficiency." [S027 arXiv p. 4].
4. *Unification.* "This approach focuses the difficulty of nonconvex QPs completely on the CP matrices." [S022 p. 1]; prior special cases restated in his notation [S004 pp. 11-14]; one parameterized family that contains classical lift-and-project procedures [S041 pp. 9-11].
5. *Beat the strongest known combination.* box QP: RLT + psd exact iff n ≤ 2, with an explicit counterexample at n = 3 (Anstreicher & Burer 2010 [S010 pp. 7-8]; restated [S011 p. 4]); the stronger psd + yᵢᵢ ≤ xᵢ + BQP₃ shown in 2009 to be still strictly weaker than the hull at n = 3 by a rational point [S011 pp. 15-16]; the kitchen sink Shor + RLT + SOC-RLT + Kron built explicitly and beaten [S049 arXiv pp. 2-3, 5-9]; Shor + KSOC strengthened by a separable class of inequalities [S050 arXiv pp. 6, 22].
6. *New (2026-10-10): every claim graded by its level, the negative result announced beside the positive one.* "This conjecture is supported by extensive numerical computations but remains unproved." [S038 arXiv p. 3]; "In Sect. 4, we prove the surprising, somewhat negative result that all three achieve the same optimal value." [S047 p. 2]; "weaker" in a title [S043 p. 2]; further cards [S020 pp. 13-14; S039 arXiv pp. 4, 14; S050 arXiv pp. 25-26; S055 arXiv p. 7; S065 pp. 10, 14, 16]. Runs from 2002 [S025 pp. 17-18] to 2026 [S065 pp. 10, 14, 16].

<a id="taste-warnings"></a>

## Taste: warning signs of bad research

**Before 2026-10-10** (SKILL.md wording, verbatim):

> 1. **A "tight" with one numerical signal, or numbers nobody can regenerate.** The 2023 two-signal rule [03 4.3.2]; a 2026 audit found results that "lived on one machine" (commit ebb2eba) [stated, AI-assisted].
> 2. **A general theorem resting on random search or an unchecked induction**: his own Burer & Ye Theorem 3 (2020, corrected 2021) and the 2025 v1 "polynomial time" claim (arXiv 2504.03996, counterexample at n = 4 in v3) [05 §1].
> 3. **A representation sold as a solution, or a success rate on instances the baseline already solves**: "So the results of this paper are not a "magic bullet" for solving NP-hard problems." (2009, p. 493); "we specifically did not include instances that were already solved by Shor in this test" (arXiv 2303.01624v1, p. 13) [stated]. Do instead: M1 stop rule; filter and disclose (M4).

**Full texts (2026-10-10).**
1. *One numerical signal.* His own record is mixed (Method 3 ⚠): two-signal forms in 2003 [S001 pp. 14, 17], 2013 [S012 preprint pp. 13, 19-21] and 2017 [S059 p. 15]; single-signal "tight" or "solved" in 2015, 2023 and 2025 [S024 preprint p. 28; S050 arXiv p. 22; S048 arXiv pp. 11, 13; S058 p. 27]. The warning stands as a rule; it is not a description of every paper.
2. *A theorem on random search.* The 2020 high-probability theorem rested on a counting argument with a Monte Carlo check, "(Indeed, empirically we can verify using Monte Carlo simulation that α ≈ 1/6.)" [S019 arXiv p. 17]; the correction: "However, in truth the proof fails because, with this setup, the systems cannot be simultaneously feasible." [S061 p. 1].
3. *A representation sold as a solution.* The 2009 paper places the difficulty in C* [S004 p. 15]; Shor-solved instances excluded from the ball-constraint tests (v2 wording differs from the v1 quote) [S049 arXiv p. 15].
4. *New (2026-10-10): a speed comparison taken at face value when only one side produces a valid bound.* "Since these codes produce both an upper bound and a lower bound, while our code only gives the latter, the comparisons should not be taken at face value." [S006 p. 9]; the same concession for primal-only methods [S001 p. 13]. Supports Method 6's stop rule.

---

<a id="method-1"></a>

## Method 1: Package the difficulty in one convex object, then attack the object

**Before 2026-10-10** (SKILL.md wording, verbatim):

> ### Method 1: Package the difficulty in one convex object, then attack the object
>
> **One line**: Before relaxing term by term, look for an exact reformulation of the whole problem as a linear problem over one convex set in a lifted space (CP cone, PSD factor of rank fixed by a theorem, SOC-RLT in (x, X), a slight lift to n+1, the Lorentz-positive cone); the hardness then sits in that one set.
>
> **Evidence**:
> - Stated: the "package" sentence (2009, p. 480, sole author); "When faced with a new optimization problem, it thus seems prudent to determine if that problem can be modeled as a linear conic program over some (hopefully) well understood K." (2012 chapter, DOI 10.1007/978-1-4614-0769-0_8, p. 202) [02 T5, I2].
> - Practice: low-rank factor sized by a rank theorem (2003), CP representation (2009), OptDNN → QuadProgBB (2010–12), SOC-RLT (2013), copositive robust/DRO bounds (2016–18), slight lift (2023), Lorentz-positive cone (2026) [01 S1, S2, S5; 06 T3, T7].
> - Say-do consistency: ✅ stated + practised, 2003–2026.
>
> **Steps**:
> 1. Lift: x → (x, X = xxᵀ) or the bordered matrix [1 xᵀ; x X]; write linear constraints as equations; mark binary and bounded variables.
> 2. Ask for one cone: can the convex hull of the lifted feasible set be written as linear constraints over a single cone K? Write down the hypothesis that makes it exact (2009: the "key assumption" that the linear constraints imply 0 ≤ xⱼ ≤ 1 for binaries).
> 3. Prove exactness, and widen the scope while revising (2009: the boundedness assumption was dropped in revision) [01 S2].
> 4. Collect the known special cases and show the new object covers them.
> 5. Turn to the object: tractable outer approximations (DNN, SDP+RLT, SOC-RLT), separation, interior conditions.
> 6. Take the approximation to computation, then a solver (2009 theory → OptDNN 2010 → QuadProgBB 2012) [03 3.4]; later write the entry point (H9).
>
> **🔴 Stop rule**: if a cheaper relaxation matches the reformulation's payoff on your instances, say so and build the cheaper intermediate. Bao, Sahinidis & Tawarmalani found DNN equal to Shor plus partial RLT at "three orders of magnitude more computational time" (DOI 10.1007/s10107-011-0462-2); his answer was OptDNN and "Faster, but weaker" relaxations, not a defence [05 §3.4].
>
> **Applies to stage**: problem choice, idea generation.
>
> **Different from standard practice**: textbook global optimization relaxes each nonconvex term (McCormick) inside spatial branch-and-bound. Here the first deliverable is an exact convex reformulation of the whole problem, and the open question becomes a property of a cone.
>
> **Limitations**: needs quadratic structure. Interior-point SDP scale ("even r = 0 can present a challenge for off-the-shelf interior-point methods for, say, n [≥] 100", 2012 chapter, p. 214). Critics: CP reformulations "are mainly of theoretical interest" (Ito et al. 2018, DOI 10.1007/s10898-018-0676-4). Sole-authored theory is a long bet (2006 posting → 2009 print).

**Full texts (2026-10-10).** Say–do: ✅ stated + practiced; 35 evidence cards, 18 variant, 0 contradictions; stated 2006–2012 [S068 abstract; S004 p. 2; S009 p. 2; S022 p. 1], practised from 2005 [S034 pp. 5-6, 11] to 2026 [S065 pp. 2, 6-7].

- **Stated.** The 2006 CAREER abstract names "linear programs over convex cones, which are one of the main tools to solve nonconvex quadratic programs" [S068 abstract]; "it does allow one to “package” the difficulty completely inside the convex cones of copositive and/or completely positive matrices." [S004 p. 2]; "When faced with a new optimization problem, it thus seems prudent to determine if that problem can be modeled as a linear conic program over some (hopefully) well understood K." [S009 p. 2]; "This approach focuses the difficulty of nonconvex QPs completely on the CP matrices." [S022 p. 1].
- **Practice (strongest cards).** The founding text: the package sentence, the key assumption as the hypothesis that makes the cone exact, special cases restated, then tractable approximations [S004 pp. 2-3, 11-16]; all bounded QCQP as one linear conic program over a generalized CP cone, with exact size counts [S022 pp. 1-3]; the CP → DNN → solver chain [S020 pp. 3-5; S008 pp. 2-3, 5, 11]; the 2009 key assumption reused in data-driven DRO [S044 arXiv pp. 9, 11-14]; the Lorentz-positive cone with a dual oracle because the explicit LMI is too large [S065 pp. 2, 6-7]; the slight lift that makes m = 2 exact [S049 arXiv pp. 3, 11-14]; an exactness hypothesis rewritten as a picturable geometric condition [S061 pp. 2-3]; best d.c. bound for standard QP shown to be Shor plus one constraint and dominated by the r = 0 copositive bound [S034 pp. 4-6]; robust LP sensitivity and two-stage ARO written exactly as copositive programs [S045 arXiv pp. 12, 23-24; S023 arXiv pp. 4, 7-8].
- **Additions to the steps.** The one-coordinate lift of a ball to a sphere is already in 2012 [S022 p. 2], a decade before the slight-lift paper; step 1 in practice also adds redundant quadratic equations before relaxing (H11) [S004 pp. 4-5, 14; S009 pp. 8-9].
- **Stop-rule evidence.** A cheaper intermediate built and costed: "In particular, we do not see a full order-of-magnitude speed up." [S043 pp. 2, 18]; the motivation of that 2014 paper is interior-point SDP cost, it never mentions DNN and does not cite Bao, Sahinidis and Tawarmalani [S043 pp. 2, 19] (correction C1); OptDNN's stated entry point is a SeDuMi timing of the DNN bottleneck [S020 p. 4]; cheaper computational routes when the exact LMI is too large [S065 pp. 6-8].
- **Variants** (recorded, nothing deleted):
  - ⚠ Reverse direction: leave the convex lifted object for a smaller nonconvex formulation (factor, rank-two, Cholesky elimination) because the aim is speed or primal solutions [S006 pp. 2, 4; S017 pp. 8-9; S025 pp. 4, 10; S001 pp. 5, 27; S003 pp. 6-7; S030 pp. 6-7]. Explained by the promoted [Method 6](#method-6).
  - ⚠ The lifted object as a node relaxation inside branch-and-bound, not as an exact reformulation [S007 pp. 8-9, 14; S018 pp. 4-5; H001 p. 3]. Explained by [H12](#heuristic-12).
  - ⚠ One lifted object that is a strict relaxation; the effort moves to the data regime where it is tight [S048 arXiv pp. 3-4, 7-9, 39-41].
  - ⚠ The hull reflex carried into constraint learning: hull of the graph, inner-approximated from data [S057 arXiv pp. 7-9].
  - ⚠ Unification instead of exactness: one parameterized family containing classical procedures [S041 pp. 9-11; S051 preprint pp. 2, 11].
- **Limitations added.** Exactness can be out of reach even in principle: "In general, determining an explicit expression for C(F) or C(F) is at least as difficult as solving the corresponding QCQP." [S067 p. 2]; the CP program itself is NP-hard and the difficulty moves into C* [S004 p. 15].

<a id="method-2"></a>

## Method 2: Kitchen sink first, then the hull of a small substructure

**Before 2026-10-10** (SKILL.md wording, verbatim):

> ### Method 2: Kitchen sink first, then the hull of a small substructure
>
> **One line**: Pick a small substructure that recurs in larger MINLPs, intersect every known relaxation for it (Shor, RLT, SOC-RLT, Kronecker), test by computation whether that "kitchen sink" already equals the hull, and publish only what goes strictly beyond it, preferably as an explicit non-disjunctive description in the smallest dimension where it is true.
>
> **Evidence**:
> - Stated: "with a little bit of tongue-in-cheek i want to call this uh the kitchen sink … it turns out that the kitchen sink does not capture the convex hole even if the dimension is equal to two" (2021 plenary [44:46]–[46:58], ASR); slide "A Combined Relaxation / CH ⊆ Shor ∩ Rlt ∩ SocRlt ∩ Kron" (Kurt-Fest slides, 2 June 2023, slide 13) [stated]; small substructures as the analogue of MILP's "one row relaxation or two row relaxation" (2021 [08:41], ASR) [02 C1, E3, T9].
> - Practice: TRS with cuts (2013), switching variables and bounded products (2021, DOI 10.1007/s10898-021-01046-7), Eltved & Burer (2023, DOI 10.1007/s10107-021-01737-9), ball constraints (2025), submodular n ≤ 3 (2026), Lorentz cone (2026) [03 3.2; 01 S5]. Student Chen credits "breaking down hard math problems into easier ones" [04 K1].
> - Say-do consistency: ✅ stated + practised.
>
> **Steps**:
> 1. Choose the substructure and name the larger models it sits in (e.g. AC-OPF for Eltved & Burer).
> 2. Re-derive the known small case in your own lifted machinery first ("Our proof of this result introduces important machinery that will be required later in the paper", 2013, p. 3).
> 3. Build the kitchen sink; count its cost with the H4 grid.
> 4. Test it on literature failure instances and random instances (M4); look for gaps.
> 5. If a gap remains, recombine ingredients: multiply a valid SOC constraint by a nonnegative linear factor and linearize ("SOC-RLT"), borrow polynomial multipliers, or lift slightly (n+1).
> 6. Seek an explicit description; use a disjunctive formulation only as a proof device ("we will show that conv(F) is SOC representable directly in the variables (x, y, z)", Anstreicher, Burer & Park 2021, p. 759).
> 7. Report by dimension: proved for n = 2 or m = 2, conjectured beyond (M3), certified counterexample where it fails.
>
> **🔴 Stop rule**: stop generalizing at the first dimension with a certified counterexample and publish the boundary (intersecting cuts at n = 3 in 2013; m ≥ 3 for balls; n = 4 for submodular). If the kitchen sink already gives the hull, there is nothing new to claim.
>
> **Applies to stage**: problem choice, idea generation, judging results.
>
> **Different from standard practice**: convexification papers usually derive one facet class or take the disjunctive hull; here the reference is the intersection of all known relaxations, beaten compactly.
>
> **Limitations**: weak where hardness is mainly combinatorial; substructures that do not recur in real models; nodes that cannot afford a 10× slower relaxation (Tension 1). In a solver, the kitchen sink also includes what BARON/Gurobi add at a node, which his record checks less (H5).

**Full texts (2026-10-10).** Say–do: ✅ stated + practiced; 25 evidence cards, 4 variant, 0 contradictions. The practice is in the full texts from 2009 [S011 pp. 4, 15-16] and 2011 [S016 preprint pp. 5-12], so the written programme (2012 survey [S002 pp. 8-9]) and the *kitchen sink* label (2021 talk) came after it.

- **Stated.** "For example, analyzing — and generating cutting planes for — the various convex hulls that arise in MINLPs (see Section 5.4) will require aspects of both polyhedral theory and convex analysis to achieve best results." [S002 p. 8]; "Special cases can also allow the development of newer techniques (e.g., semidefinite relaxations), which may then progress to more general techniques." [S002 p. 9].
- **Practice (strongest cards).** Box QP: RLT + psd exact iff n ≤ 2, explicit counterexample at n = 3 [S010 pp. 7-8; restated S011 p. 4]; the combined psd + yᵢᵢ ≤ xᵢ + BQP₃ still strictly weaker than the hull at n = 3, shown by a rational point [S011 pp. 15-16]; an explicit intersection L-RLT-R2-S2-PSD with SOC × linear products, a precursor of SOC-RLT [S016 preprint pp. 5-12]; exact at n = 2, counterexample at n = 3, disjunctive form used only to certify [S010 pp. 3, 8-12]; TRS machinery re-derived and pushed to the first certified counterexample [S012 preprint pp. 2-4, 13]; the kitchen sink built explicitly and one more ingredient tested and found to add nothing [S049 arXiv pp. 2-3, 5-9]; proof for n ≤ 3, certified boundary at n = 4, full RLT plus triangle inequalities shown not to close the gap [S058 pp. 12-14, 44]; the ladder Shor ≥ RLT ≥ KRON ≥ SEP ≥ true with an n = 2 counterexample [S065 pp. 16-18]; n = 2 proof, conjecture beyond [S038 arXiv pp. 3-5, 20]; a cut-generating process collapsed into one SOC in the original variables [S039 arXiv pp. 3, 6]; non-intersecting cuts proved for any m [S021 pp. 1, 3]; deleting ellipsoidal hollows keeps SDP tightness [S036 pp. 1, 11].
- **Proof engine.** The Pataki rank bound plus a rank-one perturbation of an extreme point or ray (technique P1) [S021 pp. 6-10; S024 preprint pp. 13-14, 19-21; S049 arXiv pp. 20-24]; the 2015 survey's half-space lemma is reused in 2025 [S049 arXiv p. 22].
- **Design moves for step 5.** SOC × linear slack, linearized (D4) [S016 preprint pp. 5-6; S021 p. 6; S067 p. 4]; sandwich an artificial scalar (D3) [S049 arXiv pp. 3, 11-12, 18-19]; Kronecker product of redundant LMIs [S055 arXiv pp. 5-6]; collapse a cut family into one constraint, "If α can be expressed as a function of (x, y) then the result is a single nonlinear constraint that is equivalent to a family of lifted tangent inequalities." [S039 arXiv p. 6].
- **Variants**: ⚠ root-equivalent strengthenings that gain only on subdivided boxes inside B&B [S047 pp. 2, 13-20]; ⚠ stack and recombine on the whole problem, no small-substructure hull [S055 arXiv pp. 3-7]; ⚠ disjunctive start only partly eliminated (a projection, not direct) [S038 arXiv pp. 3, 18]; ⚠ inexactness beyond m = 2 announced but supported by solve counts, not a certified counterexample [S049 arXiv pp. 3, 16-17].

<a id="method-3"></a>

## Method 3: Let computation propose, certify exactly, narrow publicly when wrong

**Before 2026-10-10** (SKILL.md wording, verbatim):

> ### Method 3: Let computation propose, certify exactly, narrow publicly when wrong
>
> **One line**: Run many low-dimensional instances to see when a relaxation is tight; call "tight" only on two independent signals; print regularities as conjectures; certify central claims and counterexamples in exact arithmetic; when an error is found, locate it, narrow the claim to what is provable, and name the finder.
>
> **Evidence**:
> - Stated: "we believe, but have not rigorously proved, that the two are equivalent" (Burer 2010, DOI 10.1007/s12532-010-0010-8, pp. 12–13); "So we conjecture that the two values are equal when the cuts do not intersect." (Burer & Anstreicher 2013, preprint p. 13) [stated-joint]; "Strictly speaking, a small relative gap is enough to verify approximate optimality, but we will also require a large eigenvalue ratio in order to bolster our confidence in the numerical results." (arXiv 2303.01624v1, p. 10) [stated]; "However, in truth the proof fails because, with this setup, the systems cannot be simultaneously feasible." (Burer & Ye correction 2021, DOI 10.1007/s10107-021-01684-5) [stated-joint].
> - Practice: the 2013 conjecture proved with student Yang (DOI 10.1007/s10107-014-0749-1); the 2023 conjectures proved by Kılınç-Karzan & Sun (DOI 10.1007/s10107-025-02278-1); 2026 exact rational certificates (AI-co-authored commits) [03 3.2, 4.3.2, 5.1, 5.5].
> - Say-do consistency: ✅ stated + practised, lapses kept: Theorem 3 (2020) and the 2025 v1 polynomial-time claim were printed as theorems; v2 (April 2026) narrowed the claim before any credit, which came in v3 ("We thank Shaoning Han for pointing out an error in an earlier version of this paper.", arXiv 2504.03996v3, p. 46); arXiv 1802.02688 still carries the false theorem; the printed 0.374 s timing came from mis-scaled instances and has no correction [03 4.5.5, 5.5].
>
> **Steps**:
> 1. Search many random low-dimensional instances (n ≤ 10 in 2013; 2.5 million seeds in 2023).
> 2. Declare "tight" on two signals: 2023, relative gap below 10⁻⁴ and eigenvalue ratio above 10⁴; 2025–26, the dual objective as a rigorous bound, threshold 10⁻⁵.
> 3. Hunt counterexamples on purpose, including structured ones. In 2025 random search reported "Cannot find a counterexample." (commit 63d44e3), yet a structured n = 4 counterexample existed [03 5.5].
> 4. Certify central claims in exact rational arithmetic.
> 5. Write each claim at its level: Theorem, Conjecture, "we believe"; say what is not claimed.
> 6. On error: name the failure, keep the strongest provable special case, thank the finder by name, align talk titles ("Diagonal" in 2021; "Towards" in 2025).
> 7. Update every public version: his practice falls short here (arXiv 1802.02688); keep this step as a lesson, not his habit.
> 8. Hand open cases on as conjectures.
>
> **🔴 Stop rule**: never print "We show …" for a claim whose proof has not survived a counterexample search one dimension higher (the 2025 v1 induction "with base case n = 1" failed at n = 4). If an audit shows a trend is noise, change the text [03 5.6].
>
> **Applies to stage**: judging results, writing and after publication.
>
> **Different from standard practice**: computational papers usually take "solved" from solver status and fix errors silently. Here tightness needs two signals, central claims an exact certificate, and failures are narrowed and credited in print. Each part is common; the combination is his.
>
> **Limitations**: exact certificates are out of reach for large instances and for timings. Random search misses structured counterexamples. Public narrowing costs less for a senior researcher; an early-career researcher should run the counterexample search before posting.

**Full texts (2026-10-10).** Say–do: ✅ stated + practiced, with lapses; 29 evidence cards, 15 variant, 0 contradictions.

- **Practice (strongest cards).** The full correction note: error located in the analysis of system (12), shown fatal, strongest provable case kept, finders named, "However, in truth the proof fails because, with this setup, the systems cannot be simultaneously feasible." and "Instead of the purported Theorem 3, we now prove an analogous theorem, except that it only applies to diagonal instances of (1)." [S061 pp. 1-2]; exact rational certificate for the n = 4 counterexample and genericity read into the verdict, "The experiment is therefore best understood as evidence that violations of tightness are rare." [S058 pp. 27, 43-44, 46]; "So we conjecture that the two values are equal when the cuts do not intersect." [S012 preprint p. 13], proved with student Yang [S021 pp. 3, 7, 10, 12]; a colleague's conjecture credited, "(This result was conjectured to us by Anstreicher [2].)" [S011 p. 14]; a claim of the 2003 paper narrowed in 2005 [S003 pp. 7, 12]; a certified explicit counterexample bounding a sufficient condition [S048 arXiv pp. 9, 39-42]; a counterexample published against his own 2025 relaxation, "Although the addition of the SEP constraint to the Shor relaxation solves all of the problems considered above, we have determined that it is not sufficient to give an exact representation for TTRS." [S065 pp. 12, 16-17]; what fails is named precisely, "What fails at n ≥ 4 is therefore this particular semidefinite certificate, not necessarily tractability itself." [S058 p. 46]; an earlier error credited by name, "We also would like to mention and give special thanks to Alex Wang who pointed out an error in a previous version of this manuscript and for his discussions on how to correct it." [S048 arXiv p. 15].
- **Correction C2 (dating of exact certification, ⚠ downgraded on review).** An explicit counterexample with rational data in 2010 [S010 p. 8]; in 2009 an inequality whose validity an exact recursive procedure checks, violated by a rational point whose value 19/18 is checkable by hand [S011 pp. 15-16] (p. 14 holds only a conjecture credited to Anstreicher); certification in exact rational arithmetic (rational KKT enumeration) is documented in 2025 [S058 pp. 43-44]. In 2026 the TTRS counterexample has rational data but is certified by stationary-point enumeration and Gurobi to nine digits, decimals only; the card notes that no exact rational certificate is printed [S065 p. 16]. Other non-membership results and counterexamples are certified numerically [S010 pp. 9-11; S012 preprint p. 13].
- **Correction C3 (two signals are intermittent).** Early two-signal forms: infeasibility plus primal-dual agreement with another code [S001 pp. 14, 17]; a rank measure beside the gap [S012 preprint pp. 13, 19-21]; "In other words, when an algorithm claims to have solved an instance optimally, it is independently verified by the other algorithms up to six significant figures." [S059 p. 15]. But "tight" or "solved" rests on one signal in 2015, 2023 and 2025 papers [S024 preprint p. 28; S050 arXiv p. 22; S048 arXiv pp. 11, 13; S058 p. 27]. The gap-plus-eigenvalue-ratio thresholds are specific to the ball-constraint paper [S049 arXiv p. 10].
- **Correction C10 (versions).** The SKILL.md quotes for the 2023 ball-constraint paper ("Strictly speaking, a small relative gap…", "we specifically did not include instances…") are from arXiv v1 and came from web research; the corpus text is v2, whose wording differs at the same places [S049 arXiv pp. 10, 15]. The v1 quotes stay, labelled v1.
- **Variants**: ⚠ single numerical signal for "tight"/"solved" [S024 preprint p. 28; S050 arXiv p. 22; S048 arXiv pp. 11, 13; S058 p. 27]; ⚠ floating point called irrelevant for the finiteness claim (opposite pole to exact certificates) [S007 p. 3]; ⚠ claims printed without proof, "For the sake of space, we do not prove these claims here." [S022 p. 4; S039 arXiv pp. 21-22]; ⚠ a high-probability theorem resting on a counting argument with a Monte Carlo check, later withdrawn and narrowed [S019 arXiv pp. 15-17; S061 pp. 1-2]; ⚠ inexactness beyond m = 2 supported by solve counts, not a certified counterexample [S049 arXiv pp. 3, 16-17].
- **Writing support.** Claims graded by level (W3) [S038 arXiv p. 3; S020 pp. 13-14; S050 arXiv pp. 25-26]; empirical regularities flagged as unproved, "This suggests empirically that Beta is always at least as strong as Kron, although we do not have a formal proof establishing this." [S049 arXiv p. 16]; "Said differently, it appears that DiagSum implies (4), although we have so far not been able to prove this." [S055 arXiv p. 7].

<a id="method-4"></a>

## Method 4: Engineer the hard pool, disclose the filter, keep the ladder

**Before 2026-10-10** (SKILL.md wording, verbatim):

> ### Method 4: Engineer the hard pool, disclose the filter, keep the ladder
>
> **One line**: Test where the incumbent relaxation is known to fail: literature failure instances first, then a generator built from a theorem about where the baseline breaks, keep only instances the baseline does not solve, disclose the filter and the seeds scanned, keep every earlier family and add a harder rung, and publish instances with optimal values and the generator.
>
> **Evidence**:
> - Stated: "we specifically did not include instances that were already solved by Shor in this test" (arXiv 2303.01624v1, p. 13) [stated]; "Such instances are rare; retaining 10 per size required scanning up to 16970 seeds." (arXiv 2609.32017v1, p. 12) [stated-joint].
> - Practice: BoxQP ladder 54 → 90 → 99 instances (2005–10), released 2019 with optimal values and a seeded generator; `martinez.m` generator (2013); `num_tests = 2500000` (2023); the 2013 unsolved TTRS set reused in 2023 and 2026 [03 4.1.1–4.1.5]. Others reuse his sets (Bonami, Günlük & Linderoth used "all 99 instances", DOI 10.1007/s12532-018-0133-x).
> - Say-do consistency: ✅ stated + practised; the practice is a decade older than the written rule.
>
> **Steps**:
> 1. Start with literature instances where the standard relaxation fails (2013: Yuan's instance, the three Ye–Zhang instances).
> 2. Build a generator from a theorem (2013: Martínez's local-nonglobal TRS minimizers; add an ellipsoid that cuts off the TRS optimum; reject rank-one SDP runs; idea credited to Wolkowicz).
> 3. Screen and log: keep the first k seeds the baseline does not solve; log seeds and generator versions.
> 4. Keep the ladder: add a harder rung, never drop old ones; unsolved instances become the next paper's test set.
> 5. Report rates as conditional on the pool, with the filter and scan count in the text.
>
> **🔴 Stop rule**: when the hard pool shrinks to a handful (six unsolved in 2023), report instance by instance. Do not compare counts across papers whose "solved" definitions differ; his own hard TTRS set is counted as 215 or 212, and "solved by the 2016 method" as 82, 29 or 79 depending on the source [03 Contradiction 4].
>
> **Applies to stage**: experiment design, judging results.
>
> **Different from standard practice**: standard benchmarking takes a public library as given and reports unconditional rates; here the testbed sits where the incumbent fails, so results measure the marginal value of the new inequalities.
>
> **Limitations**: says little about typical-case performance; pair it with MINLPLib/QPLIB results. An outsider noted his upper bound "is instead computed from the final solution of the relaxed problem, so that it could be slightly worse and justify the larger number of unsolved instances" (Consolini & Locatelli, arXiv 2102.11161v2, p. 20). Seed scans cost hours (76 hours for one 2026 panel).

**Full texts (2026-10-10).** Say–do: ✅ for the stated rule, practice scoped; 11 evidence cards against 23 variant cards, 0 contradictions.

- **Practice (strongest cards).** Literature failure instances first, then a theorem-based generator credited to Wolkowicz [S012 preprint pp. 16-19]; the BoxQP ladder 54 → 90 [S018 pp. 11-14] → 99 with a new rung [S020 p. 12]; a pool of 4,835 of 6,000 instances on which the baseline fails, filter disclosed [S024 preprint p. 28]; the 2013 unsolved set reused, "Applying our heuristic lifted-RLT constraints to the 215 previously unsolved instances, we can solve 82—about 38%—of them; see Table 3." [S033 p. 19]; Shor-solved instances excluded and the 267 and 212 hard sets reused [S049 arXiv pp. 15-16, 20]; seed screens and a harder rung added [S065 pp. 8, 12, 15-16].
- **Correction C4 (scope).** The hard-pool practice appears in two lines only: the trust-region/ball line 2013–2026 [S012, S024, S033, S049, S065] and the BoxQP ladder 2008–2010 [S018, S020]. In 23 cards the testbed is a public library or an unfiltered random panel [S006 pp. 10-15; S013 pp. 15-16; S043 pp. 13-14; S047 p. 17; S055 arXiv pp. 9-10; S059 p. 16; S048 arXiv pp. 11-12; S058 p. 27; S057 arXiv pp. 11, 16], or the filter removes trivial instances or instances with numerical trouble rather than selecting baseline failures [S008 pp. 14, 16; S045 arXiv p. 21]. Scan counts are disclosed for some families and not others [S049 arXiv p. 15; S050 arXiv pp. 22-27; S065 pp. 8, 16]. M4 is how he tests a claim about the marginal strength of a relaxation over an incumbent; for speed/bound trade-offs and applications he uses public or random sets [S043 pp. 13-14].
- **Variants**: ⚠ public libraries or unfiltered random panels (the 23 cards above); ⚠ the baseline advantaged instead of a hard pool, "Actually, this choice favors MB, but the goal of our experiments is to demonstrate that our approach provides a valid upper bound" [S044 arXiv p. 14]; ⚠ instances generated from real data without using the data itself, "In particular, the original course data was not used to test the algorithms directly; it was simply the basis for randomly generating the test data." [S062 p. 6].

<a id="method-5"></a>

## Method 5: Prototype first, let theory follow

**Before 2026-10-10** (SKILL.md wording, verbatim):

> ### Method 5: Prototype first, let theory follow (exclusivity weakest)
>
> **One line**: Combine a known theorem with a known trick, implement it within a day, report one concrete number on a named instance, push variants beyond what the theory licenses, benchmark against the best public codes at their defaults, and publish with the missing theory stated.
>
> **Evidence**:
> - Stated: "Still equivalent to the SDP...but with a very different feasible set / The potential advantage was less computation and storage / But would it actually work in practice? / Can't hurt to try" (SIAM OP23 slides, 2 June 2023, slide 30) [stated]; e-mail of 22 May 2000 shown on slide 31: "I did a quick implemenation of the low-rank idea for the primal maxcut that we were talking about, and it looks promising. … One example: On G1, the new approach cuts the times for both the function and gradient evaluations by approximaately 1/2." (typos as in the original) [stated].
> - Practice: 2000 same-day prototype; "our belief that the method is not strongly affected by the inherent nonconvexity of (2) is largely experimental" (Burer & Monteiro 2003, p. 331); loose subproblems (2008); SeDuMi timings before OptDNN (2010); counterexample code before the 2026 v2 [03 3.1, 4.4, 5.5].
> - Say-do consistency: ✅ stated + practised over 25 years. Exclusivity ⚠️ weakest: fast prototyping is common; his recipe (theorem + trick, best public codes at defaults, theory gap printed) is the distinctive part.
>
> **Steps**:
> 1. Combine a known reformulation with a theorem that sizes it (2003: Peinado–Homer factorization + Barvinok–Pataki rank bound).
> 2. Prototype that day; measure one number on a named instance.
> 3. Before building a method, time the bottleneck (2010: SeDuMi took "1, 30, 385, and 1787" seconds for n = 25, 50, 75, 100).
> 4. Push beyond the theory (rank below the bound, dynamic rank); record which variants failed and why.
> 5. Benchmark against the best public codes at their defaults ("Both SB and DSDP are run with their default parameters.", 2003, p. 344).
> 6. Publish with the gap stated ("we do not currently have a formal convergence proof", 2003, p. 355), then prove what you can (2005, DOI 10.1007/s10107-004-0564-1).
>
> **🔴 Stop rule**: drop a variant with poor convergence and weak theory ("the theoretical base for dynamically changing the rank is not strong", 2003, p. 342). If speed depends on low accuracy, say so; critics later named moderate accuracy as SDPLR's limitation (DOI 10.1080/10556788.2026.2683647).
>
> **Applies to stage**: idea generation, experiment design.
>
> **Different from standard practice**: algorithm papers usually prove convergence first; here the code result carries the paper and theory may come years later.
>
> **Limitations**: nothing to prototype for exact-representation theorems; venues demanding convergence proofs; "largely experimental" was easier to publish with a strong benchmark and a senior co-author.

**Full texts (2026-10-10).** Say–do: ✅ stated + practiced in algorithm papers that carry a code claim; 23 evidence cards, 6 variant, 1 contradiction (S041).

- **Practice (strongest cards).** A known factorization plus a rank theorem, the theory gap printed, "Although we have some theoretical justification that explains the observed practical convergence, we do not currently have a formal convergence proof." [S001 pp. 2-3, 14-16, 27]; the proof two years later, for a variant that is not run, "While it seems that the extra term is necessary for theoretical convergence, it does not appear to be necessary for practical convergence." [S003 pp. 3, 13]; a variant of an existing code benchmarked against the best codes available [S014 preprint pp. 8, 13, 18, 20]; the bottleneck timed first and inner problems solved loosely, "Consistent with the experience of Burer–Vandenbussche [7] and other augmented-Lagrangian methods for SDP, we find that it pays only to solve these problems very loosely." [S020 pp. 4, 11-12, 16]; failed enhancements printed, "During the course of this study, we have considered other possible enhancements to the algorithm that unfortunately did not seem very promising in practice." [S026 p. 19], "We include our experiences here in order to provide a complete picture of our efforts and a starting point for additional research." [S031 p. 16]; best public global codes as baselines with failed variants explained [S059 pp. 17-23]; algorithm first, no convergence theory, in 2026 [S056 arXiv pp. 9-15].
- **Contradiction (✗, correction C5).** Theory carries the paper and a later experiment refutes the computational hypothesis, printed openly: "These results are a testament to the high quality of current LP software." [S041 pp. 23, 25]. Also a theory paper whose numerics sit in companion reports [S017 pp. 2, 25] and an abstract-assumption convergence framework with no code [S051 preprint pp. 4-22]. M5 is the mode of his algorithm papers that carry a code claim; it is not his only mode for algorithms.
- **Variants**: ⚠ theory first, numerics elsewhere; theory re-proved for a modified relaxation [S017 pp. 2, 25; S018 pp. 8-11]; ⚠ competitors tuned by grid search, parameters made adaptive for fairness (not run at defaults) [S056 arXiv pp. 9-11]; ⚠ the implementation drops the theoretical neighbourhood, "Third, in our implementation of Algorithm SDP, we do not bother to stay in the neighborhood N (γ), since our computational experience indicates that this does not yield a substantial practical improvement." [S029 p. 22].
- **Step 5 exceptions.** Baselines are sometimes tuned or handicapped in their favour rather than run at defaults (see [H5](#heuristic-5)) [S044 arXiv p. 14; S059 pp. 19, 21-22; S013 p. 17].

<a id="method-6"></a>

## Method 6: Solve in the cheap nonconvex space, certify in the convex dual

**Before 2026-10-10**: no such method. Promoted on 2026-10-10 by `08-deep-reading-synthesis.md` §4 from eight works (2001–2006 and 2025); it explains six Method 1 reverse-direction variants that Method 1 could only mark as anomalies.

**Cards (8 distinct works).** [S014 preprint p. 8] dual slack from stationarity multipliers certifies global optimality of the factored maxcut problem; [S017 pp. 19, 23-24] a dual estimate from a triangular system gives dual feasibility and the duality gap from the gradient, and the barrier problem has no spurious stationary points; [S001 pp. 5, 7, 13-14] rank sized by the Barvinok–Pataki bound, a stationary point with S ⪰ 0 is SDP-optimal, zero-column injection as a certificate, and the concession that a primal-only method gives no valid bound unless solved exactly; [S003 pp. 3-4, 13-15] no extraneous local minima, in-run certificates and a λ_min-shift lower bound; [S013 p. 6] the augmented Lagrangian chosen partly because it yields dual bounds; [S006 pp. 6-9] cuts other than maximum cuts are saddle points, restarts from perturbed cuts; [S025 pp. 5-6, 10-12, 17-18] rank-one/rank-two exact formulations, local maxima classified, escapes designed; [S048 arXiv pp. 5-7, 14, 17-20] an LMI certificate for the output of any Stiefel solver, made robust to inexact stationarity. Partial support: [S030 pp. 6-7] (a convex SDP rewritten as an NLP over a simple set).

**Four checks.**
1. *Cross-project recurrence* ✅: 8 works across the thesis-era SDP algorithms (2001–2006, with Monteiro, Zhang, Vandenbussche) and a 2025 signal-processing problem with Michigan EECS coauthors [S048 card header].
2. *Say–do* ✅ (practised in all 8 works; stated only as results in co-authored papers, both quotes [stated-joint]): "In particular, we show that the change of variables does not introduce any extraneous local minima." [S003 p. 3]; "Thus, we can solve the nonconvex problem posed in (1.1) using any choice of solver on the Stiefel manifold and perform a fast check of its terminal output for global optimality." [S048 arXiv p. 14]; the limit stated where the certificate is missing, "Since these codes produce both an upper bound and a lower bound, while our code only gives the latter, the comparisons should not be taken at face value." [S006 p. 9]. Practised in every listed card.
3. *Executable, different from standard practice* ✅: standard practice either solves the convex SDP by an interior-point method (certified, expensive) or runs a local NLP solver with no certificate. Steps with cards:
   1. Find the theorem that lets a smaller nonconvex formulation carry the optimum: a rank bound [S001 p. 5], an exact rank-one/rank-two restriction [S025 pp. 4, 10], a Cholesky elimination [S017 pp. 7-9], a column-wise lift [S048 arXiv p. 3].
   2. Map the stationary points: prove no spurious local minima, or classify local optima combinatorially and identify saddles [S003 pp. 3-4; S006 p. 7; S025 pp. 5-6, 12; S017 pp. 23-24]. A surprising equality can come out of the map, "A surprising result that we will show in this section is that the optimal values of the two formulations are equal even though the feasible region of the rank-two problem is strictly larger than that of the rank-one problem." [S025 p. 6].
   3. Build the dual estimate from the multipliers of the nonconvex method and test it (S ⪰ 0, an LMI in a few scalars) [S014 preprint p. 8; S017 p. 19; S001 p. 7; S048 arXiv pp. 6, 17-18].
   4. Make it robust to inexact solves: shift by λ_min when the trace is implied [S003 pp. 14-15], or ε-relax the LMI and report the bound gap [S048 arXiv pp. 7, 19-20].
   5. Use the classification to design escapes: restart from a perturbation of a point the theory says is a saddle [S006 pp. 7-9; S025 pp. 17-18].
   6. Report primal and dual side by side, check for bound crossing [S001 pp. 14, 17], and separate certified, not-tight and local outcomes [S048 arXiv p. 13].
4. *Exclusivity* ✅ relative to the team, with a caveat: the low-rank factorization line is his own [S001 pp. 2-3; H002 p. 1], and no other minlp-team member's skill works this way. In the wider field, landscape-plus-certificate work on Burer–Monteiro factorizations became a literature of its own, which S048 cites and distinguishes itself from [S048 arXiv pp. 5, 28].

**Stop rule.** If the nonconvex method cannot produce a dual estimate during the run, say that no valid bound is available and compare only on the primal side [S006 p. 9; S001 p. 13]. Escapes carry no guarantee: "In fact, although “escapes” were often observed in our experiments, sometimes the algorithm did fail to escape from a non-maximum stable set." [S025 p. 18].

**Limitations.** Dormant in the cards between 2007 and 2024, when his relaxations themselves are the bound (Methods 1, 2) [08 §8]; certificates rest on sufficient conditions [S048 arXiv pp. 6, 9]; accuracy is moderate and the tail slow, "a running theme of this paper is that the speed of first-order methods make them attractive choices for solving the maxcut SDP relaxation, particularly when one desires a solution of only moderate accuracy." [S014 preprint p. 2]; unexplained behaviour is admitted, "We currently are unable to give a reasonable explanation as to why this occurs" [S014 preprint p. 17]. The 2002 NSF abstract frames the choice between the two spaces by size, "The choice of which class to use for a particular application is determined primarily by problem size --- second-order IP methods are more efficient on small- to medium-scale problems while first-order NLP methods are better for large-scale problems." [S069 abstract]. An old device was rehabilitated knowingly: "The square slack substitution is an old idea in nonlinear programming that has not been regarded as practically useful in general, in part because it can turn a convex feasibility set into a nonconvex one." [S017 p. 6].

**Why a method, not a variant** (08 §4): it explains six Method 1 reverse-direction variants and is distinct from Method 5 (an ordering of code and theory) and from Method 3 (a protocol for tightness claims). The skill moves from 5 to 6 core methods, inside the 3–7 range.

---

<a id="workflows"></a>

## Stage workflows: techniques added from the full texts

SKILL.md's Workflows A–E keep their steps; the full texts add concrete techniques, listed here with all cards (SKILL.md shows at most two per step). Ids P, D, E, W refer to `../technique-catalog.md`.

- **Workflow A (problem choice).** Look for a class where the strong relaxation wins uniformly (H1) [H001 pp. 2-3; S013 p. 24]; read the substructure as a MILP concept (H2) [S016 preprint p. 2; S016 preprint p. 30]; ask whether a known bound family is a strengthened Shor by duality (H3) [S034 p. 4]; consider leaving the lift for a smaller nonconvex formulation when size, not strength, is the problem (Method 6) [S001 p. 5; S048 arXiv p. 14].
- **Workflow B (relaxation design).** Add redundant quadratic equations held at extreme values (H11) [S004 pp. 4-5, 14; S009 pp. 8-9; S049 arXiv pp. 13-14]; sandwich an artificial scalar (D3) [S049 arXiv pp. 3, 11-12, 18-19]; split by copy variables so the cone and the coupling sit in separate blocks (D2) [S013 pp. 4-5, 12; S020 pp. 6-8]; Kronecker product of redundant LMIs [S055 arXiv pp. 5-6]; a separation oracle in place of an explicit description (D6) [S012 preprint p. 15; S040 pp. 9-14; S065 pp. 4-8]; for global algorithms, put the KKT conditions into the relaxation (H12) [S007 pp. 3, 9-12; S008 pp. 8-10].
- **Workflow C (experiments).** Same accuracy target or the same bound for every method (E1) [S014 preprint p. 14; S020 p. 12; S013 p. 18; S001 p. 26; S031 p. 14]; favour the baseline when the claim is a trend or a valid bound (E2) [S044 arXiv p. 14; S059 pp. 19, 21-22; S013 p. 17; S031 p. 8]; swap one component, freeze the rest, factorial ablations (E3) [S020 p. 16; S043 pp. 15-16; S045 arXiv pp. 23-24]; report by joint outcome (E4) [S049 arXiv p. 17; S048 arXiv p. 13; S062 pp. 6-8]; cross-verify "solved" (E5) [S001 pp. 14, 17; S059 p. 15]; accuracy at two levels (E6) [S014 preprint pp. 15-17]; instances generated from real data without using the data (E7) [S062 p. 6].
- **Workflow D (judging).** Genericity read into the verdict [S058 pp. 27, 46]; a certificate from multipliers when the solver is nonconvex (Method 6) [S048 arXiv pp. 6, 17-18; S003 pp. 14-15]; explain wins and losses by one instance statistic [S032 pp. 14-15]; validity separated from sufficiency [S027 arXiv p. 4].
- **Workflow E (writing).** Numbered goals or conclusions up front, negative ones included (W1) [S014 preprint p. 3; S020 p. 5; S026 pp. 3-4; S007 p. 4; S049 arXiv p. 2]; the negative result announced beside the positive one (W2) [S047 p. 2; S010 p. 3; S041 p. 23; S063 p. 15; S043 p. 2]; every claim graded by level (W3) [S038 arXiv p. 3; S020 pp. 13-14; S039 arXiv pp. 4, 14; S050 arXiv pp. 25-26; S055 arXiv p. 7; S065 pp. 10, 14, 16]; easiest to hardest, picture first (W4) [S017 p. 6; S024 preprint p. 3; S043 pp. 4-6; S067 p. 3; S049 arXiv pp. 3, 13-14]; warn about notation (W5) [S017 p. 3; S008 p. 6; S024 preprint p. 3; S049 arXiv p. 5]; scope disclaimer (W6) [S015 p. 3; S031 p. 14]; credit finders and contributors by name (W7) [S004 p. 17; S019 arXiv pp. 17-18; S061 p. 1; S048 arXiv p. 15; S058 p. 46; S049 arXiv p. 24; S042 p. 13]; end with open questions (W8) [S004 pp. 16-17; S011 p. 16; S029 p. 33; S037 pp. 24-25; S049 arXiv p. 24; S067 p. 6]; disclose concurrent equivalent work by date [S023 arXiv pp. 4-5].

---

<a id="heuristic-1"></a>

## Heuristic 1: Let the tool choose the problem class

**Before 2026-10-10**: 1. **H1 Let the tool choose the problem class**: if a standard solver's cheap reoptimization beats your strong bound, switch class. Case: "So the authors shifted their focus away from IPs to continuous problems" (award note, p. 568) [stated-joint].

**Full texts.** "More generally, the paper also illustrates that it can be worthwhile to pay for a computationally expensive, but strong, relaxation" [H001 p. 3]; the goal of finding classes where SDP bounds are uniformly good [H001 p. 2]; the conclusion of the 0-1 work names mixed and nonconvex QP as next targets [S013 p. 24]; a negative finding that steers away from a class, "This demonstrates that lift-and-project operators are not always able to strengthen the LP relaxation of an IP." [S013 p. 20].

<a id="heuristic-2"></a>

## Heuristic 2: Use MILP as the road map, concept by concept

**Before 2026-10-10**: 2. **H2 Use MILP as the road map, concept by concept** (one-row/two-row relaxations → small substructures), but look for MINLP-specific insight. Case: Burer & Saxena, "The MILP Road to MIQCP" (DOI 10.1007/978-1-4614-1927-3_13).

**Full texts.** "In this sense, we view (MIQCP) as a natural progression from MILP rather than, say, a special case of MINLP." [S016 preprint p. 2]; "the “breakthrough” results are yet to come and we believe that the past of MILP holds the clues to the future of MIQCP." [S016 preprint p. 1]; its closing concept dictionary [S016 preprint p. 30]; BQP facets and symmetries transferred to box QP with an iff survival test [S011 pp. 7, 11-13]; split disjunctions and BQP facets carried to unbounded MIQP sets [S037 pp. 11, 14-15, 17].

<a id="heuristic-3"></a>

## Heuristic 3: Derive others' unexplained cuts as special cases

**Before 2026-10-10**: 3. **H3 If someone's cuts work but nobody can say why, derive them as special cases of a general family.** Case: the Chen–Atamtürk–Oren cuts shown to be "actually just special cases of our cuts" (arXiv 2009.12704v2).

**Full texts.** A bound family read by duality as Shor plus one constraint, "The dual of DQPSDC has a surprisingly simple interpretation as a strengthening of the Shor relaxation SQPS." [S034 p. 4]; a cut process collapsed into one constraint, "We do not use the inequalities per se, but rather show how the process by which they are constructed can be re-interpreted to generate nonlinear inequalities." [S039 arXiv p. 3] and [S039 arXiv p. 6]; "Indeed, our initial motivation for this paper was the desire to understand the inequalities in [9] more fully." [S050 arXiv p. 6]; the affine policy shown to be a specific inner approximation of the copositive program [S023 arXiv pp. 11-12].

<a id="heuristic-4"></a>

## Heuristic 4: Size a relaxation by auxiliary variables × cone

**Before 2026-10-10**: 4. **H4 Size a relaxation with two questions**: how many auxiliary variables, which cone? If you commit to SOCP, add the linear constraints too; look for relaxations that "solve faster than SDPs while providing better bounds than SOCPs" (Burer, Kim & Kojima 2014, DOI 10.1007/s10589-013-9618-8, p. 30).

**Full texts.** "In this paper, we describe a “middle way” between SOCP and SDP relaxations." [S043 p. 2]; block partition as the speed dial [S043 p. 5]. ⚠ Variant: the motivation promises bounds better than SOCP, but the comparison is run against SDP only [S043 pp. 4, 15-18]. Size counts written out for each construction [S022 p. 3]; one PSD variable as the design target [S049 arXiv pp. 3, 11-12].

<a id="heuristic-5"></a>

## Heuristic 5: Baseline protocol

**Before 2026-10-10**: 5. **H5 Baseline protocol**: first baseline is your or your co-author's previous code at its best configuration (Chen & Burer 2012, p. 45); disclose what could not be matched; never improve your gap with another method's incumbent. Known gap: in 2010 BARON was "beaten" only by transitivity.

**Full texts.** Evidence: the coauthor's previous code first, "The BurVan code is not publicly available, but since the second author was a co-author of the BurVan code, the code was available to us." [S008 p. 13; S018 pp. 11-12]. ⚠ Variant added, *favour the baseline* when the claim is a trend, a valid bound or a speed-up: exact moments given to the moment-based baseline, "Actually, this choice favors MB, but the goal of our experiments is to demonstrate that our approach provides a valid upper bound" [S044 arXiv p. 14]; bounds derived for the big-M competitor and imposed on his own code for fairness [S059 pp. 19, 21-22]; a general-purpose code tested and set aside with the reason printed, "However, we have found by testing code supplied by the authors that this general-purpose algorithm was not competitive with the special-purpose algorithm that we will present in this paper." [S059 p. 4]; the competitor's starting duals tuned [S013 p. 17]; same-language re-implementation [S031 p. 8]; swap one component and freeze the rest [S020 p. 16]; "This gives a method-specific feasible upper bound; no Gurobi incumbent or point recovered by another method is used to calculate the gap." [S065 p. 12]. Known gap kept: QuadprogBB names BARON and Couenne but benchmarks only Couenne [S008 pp. 2, 14].

<a id="heuristic-6"></a>

## Heuristic 6: A bound crossing is a bug alarm

**Before 2026-10-10**: 6. **H6 A bound crossing is a bug alarm**: verify an incumbent's feasibility before it may prune. Case: "Jieqiu, I would suggest that we verify the feasibility of any x that might lead to a better GUB." (QuadProgBB in-code note, 2011) [03 4.5.3].

**Full texts.** No primal value below a dual bound, checked across codes [S001 p. 14]; infeasibility threshold chosen by experiment, "Nonetheless, after much experimentation, we feel that 10−5 is a reasonable amount of infeasibility to require." [S001 p. 14]; independent verification of "solved" to six significant figures [S059 p. 15].

<a id="heuristic-7"></a>

## Heuristic 7: Solve inner problems loosely, tune the outer loop, print safeguards

**Before 2026-10-10**: 7. **H7 Solve inner problems loosely, tune the outer loop by experiment, and if you drop a theory requirement for speed, keep a safeguard and print it.** Case: "Of course, it is theoretically unwise to ignore (3)" (Burer & Vandenbussche 2008, p. 274).

**Full texts.** "Consistent with the experience of Burer–Vandenbussche [7] and other augmented-Lagrangian methods for SDP, we find that it pays only to solve these problems very loosely." [S020 p. 11]; "Somewhat surprisingly, computational experiments showed that the dual multipliers converged reasonably well even when the subproblems were solved very loosely by only a few cycles of block coordinate descent." [H001 p. 2]; the safeguard printed, "Of course, it is theoretically unwise to ignore (3) because both the boundedness of (y, z) and the correctness of branch-and-bound depend on it." [S007 p. 16]; further [S018 p. 11; S013 pp. 14-15; S029 p. 22]; an inexactness budget tied to the duality gap [S035 pp. 10-11].

<a id="heuristic-8"></a>

## Heuristic 8: Print losses and failed extensions with a hypothesis

**Before 2026-10-10**: 8. **H8 Print losses and failed extensions with a hypothesis.** Case: "For most Globallib, RandQP and CUTEr instances, Couenne outperforms Quadprogbb" (Chen & Burer 2012, p. 48).

**Full texts.** The habit runs from 2001 to 2026: [S014 preprint p. 17; S018 p. 14; S020 p. 18; S026 p. 19; S031 pp. 14, 16; S041 p. 25; S043 p. 18; S063 p. 15; S023 arXiv p. 20; S056 arXiv pp. 13-15; S057 arXiv pp. 16, 19-20]. Examples: "Finally, An and Tao solve instances with n as high as 550, which exceeds the dimension solved in this paper." [S018 p. 14]; "Though our method was successful for p ≈ 50, it was not competitive with the specialized method of [20]." [S020 p. 18]; "We found that, in this case, our method did not perform better than the affine policy." [S023 arXiv p. 20]; "CirCut does not seem to be able to achieve the same cut values as H2 even if CirCut is allowed to search for a very long time." [S006 p. 15]; theory and computation that disagree printed side by side, "Although Proposition 4.6 makes sense from a theoretical point of view, it is inconsistent with our computational results in which our method seems to work well on large-scale circuit partitioning problems." [S063 p. 15].

<a id="heuristic-9"></a>

## Heuristic 9: After the core result, write the entry point

**Before 2026-10-10**: 9. **H9 After the core result, write the entry point**: easiest to hardest, geometry first, and what is not claimed ("we do not claim to have identified the best or only way to solve each of the various problem types", 2015, p. 3).

**Full texts.** "Hence, our main contribution is a unified presentation of the various results, and we do so from “easiest to hardest” in hopes of gently introducing the reader to the insights provided by copositive optimization." [S024 preprint p. 3]; "Instead, we intend only to give an introduction to some of the main results in the area, tainted with our own biases." [S009 p. 3]; scope statements, "We claim neither that these are the only mechanisms possible nor that they are in every sense optimal." [S015 p. 3]; "First, we focus only on how the optimal value is affected by uncertainty, not the optimal solution." [S045 arXiv p. 4]; further [S027 arXiv p. 27; S047 p. 13]; the encyclopedia entry as an entry point [S067 pp. 2-6].

<a id="heuristic-10"></a>

## Heuristic 10: Make every number regenerable, then audit before revising

**Before 2026-10-10**: 10. **H10 Make every number regenerable, then audit before revising** (seeds, manifest, three reproducibility levels). Case: "Two discrepancies are documented rather than papered over." (commit f868951, 2026) [stated, AI-assisted]. Dated: 2023–26 only.

**Full texts (correction C9).** Code release is older than 2023: SDPLR as documented software, "SDPLR is a C software package for solving large-scale semidefinite programming problems." [H002 p. 1], with its own input format [H002 p. 3]; QuadprogBB public behind a familiar interface [S008 p. 11]; code repositories named in the papers [S050 arXiv p. 6; S049 arXiv p. 4]. The seed, manifest and audit discipline remains dated 2023–26 (web research). New dating: code release from 2009; seed and manifest discipline 2023–26.

<a id="heuristic-11"></a>

## Heuristic 11: Redundant in x, binding in the lift

**Before 2026-10-10**: no such heuristic. Added from `08` §5.1. **Review 2026-10-10**: not a numbered heuristic in SKILL.md (the framework allows 5–10 and it adds no explanatory power over Method 1); folded into SKILL.md Method 1 step 1 and catalog row D7. The evidence below stays.

Before relaxing, add quadratic equations that are redundant in the original variables but held at their extreme values: squared linear equations, complementarities, binarity, products of KKT stationarity with x. In the lift they are not redundant and often carry exactness.
- Cards: [S004 pp. 4-5, 14] squared equations, "Overall, it seems that the original equation and its squared version are critical for Theorems 2.6 and 3.1."; [S009 pp. 8-9] a quadratic fixed at its extreme value over the linear slice is captured exactly; [S022 pp. 2-3] the same device twice; [S007 p. 9] the objective-equating constraint from the KKT identity; [S008 pp. 8-9] an RLT-linearized x^T(stationarity) = 0 bounds the duals; [S045 arXiv pp. 12, 23-24] a redundant complementarity measured by ablation; [S049 arXiv pp. 13-14] a complementarity product linearized for exactness at m = 2.
- Checks: recurrence ✅ (7 works, 2008–2025); say–do ✅ [S004 p. 14]; executable ✅; exclusivity ✗ (products of constraints are the standard RLT idea [S016 preprint pp. 5-6]) → heuristic, not method. Links to Method 1 steps 1–2.

<a id="heuristic-12"></a>

## Heuristic 12: Put the optimality conditions into the relaxation and branch finitely on them (2008–2012)

**Before 2026-10-10**: no such heuristic. Added from `08` §5.1. **Review 2026-10-10**: not a numbered heuristic in SKILL.md (the framework allows 5–10; KKT branching is borrowed); recorded as a dated Method 1 variant (SKILL.md Method 1 evidence, Workflow B step 6, trajectory row 2008–2012) and catalog row D8. The evidence below stays.

For a global algorithm, write the KKT system, branch on complementarity index sets so the tree is finite, make the node relaxation an SDP/DNN of the lifted KKT system, add a constraint that bounds the multipliers, and define correctness as zero gap at every feasible leaf.
- Cards: [S007 pp. 3, 6, 9-12] "We are unaware of any methods that can verify optimality in a finite number of nodes (using exact arithmetic)."; [S018 pp. 7-10] specialised to the box with multipliers eliminated and correctness re-proved; [S008 pp. 4, 6, 8-10] finite KKT branching instead of spatial branching, attributed to relaxation strength against Couenne, "We attribute the performance differences mainly to the relaxation differences: we use stronger SDP-based relaxations, while Couenne uses weaker LP relaxations." [S008 p. 16]; [S047 p. 20] second-order conditions relaxed, "Relaxing the standard second-order necessary optimality conditions is one of the main theoretical ideas of this paper. This task is non-trivial since it implicitly involves knowledge of the active/inactive constraint set at a general point."; [S020 p. 16] the same tree reused to compare node solvers; outside the QP line, a special-purpose B&B that branches on complementarities for quantile regression [S059 pp. 5-7, 12, 14-15].
- Checks: recurrence ✅ (5 works, Vandenbussche and Chen lines); say–do ✅ [S007 p. 3; S047 p. 20]; executable ✅; exclusivity partial: KKT branching itself comes from Hansen et al. and Vandenbussche–Nemhauser [S007 p. 3; S018 pp. 1-2] → heuristic, dated; [inferred] the single-strong-relaxation aim is stated by 2011/12 [S016 preprint p. 2] and pursued in the hull papers from 2009 [S011; S010], so it ran alongside this line; after 2012 the cards hold no new global QP solver (the 2017 B&B is a statistics application [S059 pp. 5-7]).

---

<a id="anatomy-low-rank"></a>

## Anatomy: A nonlinear programming algorithm for solving semidefinite programs via low-rank factorization (2003)

**Before 2026-10-10** (table verbatim):

> ### A nonlinear programming algorithm for solving semidefinite programs via low-rank factorization (Math. Program. 95:329–357, 2003, DOI 10.1007/s10107-002-0352-8; with Monteiro)
>
> | Dimension | Content |
> |---|---|
> | Origin | **Stated** (2023): known ideas combined (Peinado–Homer factorization, rank theorem): "that was the key thing that we put together" (ASR); "Can't hurt to try" |
> | Why then | "At the turn of the millenium, researchers were solving bigger SDPs more efficiently, often using first-order methods" (2023 slide 26) |
> | Key insight | X = RRᵀ with the rank "chosen minimally so as to enhance computational speed while maintaining equivalence with the SDP" (abstract) |
> | Minimum evidence | The G1 run of 22 May 2000; in print, 25.7 s against 288.2 s (SB) and 2,311.8 s (DSDP) on one torus instance |
> | Abandoned paths | Dynamic rank, per-constraint penalties; convergence proof deferred to 2005 |
> | Reception | GS 1,372; SIAM SIAG/OPT Test of Time Award 2023. Limits found by others (DOI 10.1137/19M1255318; arXiv 2211.12389) not cited in his 2023 retrospective |
> | Methods shown | M5, M1 |

**Full text [S001].** Problem entry: interior-point SDP too time- and memory-intensive for large combinatorial relaxations; three framing questions (size, method, nonconvexity) [S001 pp. 1-3]. Key idea: a rectangular factor R with r(r+1)/2 ≤ m columns, solved by a first-order augmented Lagrangian whose evaluations cost O(nonzeros · r) [S001 pp. 3, 5, 8-12]. Evidence: ANSI C on one processor; theta, maxcut and bisection instances; SB and DSDP at default parameters with 10-hour limits; infeasibility and primal-dual difference columns; losses on hamming graphs explained; time-matched truncation of SB [S001 pp. 13-26]. Positioning: continues Homer–Peinado and the authors' own Cholesky/NLP work; concedes dual methods are more valuable when a valid bound is needed [S001 pp. 2, 13]. Limits printed: slow subproblems for theta and bisection, no formal convergence proof, equality form only; a dual-feasibility safeguard and a dual low-rank analogue proposed [S001 p. 27]. Follow-ups: no extraneous local minima and a convergence proof for a perturbed variant [S003 pp. 3, 13]; block SDPs, dynamic rank reduction and failed enhancements [S026 pp. 4-7, 19]; SDPLR documented as software [H002 pp. 1-3].

<a id="anatomy-copositive"></a>

## Anatomy: On the copositive representation of binary and continuous nonconvex quadratic programs (2009)

**Before 2026-10-10** (table verbatim):

> ### On the copositive representation of binary and continuous nonconvex quadratic programs (Math. Program. 120:479–495, 2009, DOI 10.1007/s10107-008-0223-z; sole author)
>
> | Dimension | Content |
> |---|---|
> | Origin / why then | **Unknown in his words**; growth from the 2003 Anstreicher–Burer copositive work and the accumulation of special-case results are inferred |
> | Key insight | Under the "key assumption", a mixed-binary QP is a linear program over the CP cone |
> | Minimum evidence | A proof; no computation |
> | Abandoned paths | Boundedness assumption dropped in revision; an error in Proposition 2.3 caught by Bomze before print (content not read) |
> | Reception | GS 566, OA 408. "a breakthrough" (Dür & Rendl 2021, DOI 10.1016/j.ejco.2021.100021) vs "mainly of theoretical interest" (Ito et al. 2018); Bomze & Jarre's critique (DOI 10.1007/s11590-010-0174-1) absorbed with credit in his 2012 chapter |
> | Methods shown | M1, H9 |

**Full text [S004].** Problem entry: only a short list of NP-hard problems had CP representations; how far does the list extend [S004 pp. 1-2]. Key idea: lift, keep each linear equation and add its square, impose x_j = X_jj for binaries, require complete positivity; exact under the key assumption [S004 pp. 3-6]. Minimum evidence: proofs only; Section 5 discusses approximations of C* without runs [S004 pp. 15-16]. Positioning: restates Bomze et al., de Klerk–Pasechnik, Povh–Rendl and Sturm–Zhang in its own notation and does not claim to subsume them [S004 pp. 11-14]. Writing: hedged (the "magic bullet" disclaimer quoted in SKILL.md), three open questions at the end [S004 pp. 15-17]. The earlier error credited to Bomze is acknowledged, but its content is not in the text [S004 p. 17]. Generalized to any closed convex cone in the 2012 chapter [S009 pp. 2-5] and to bounded QCQP [S022 pp. 1-3].

<a id="anatomy-finite-bb"></a>

## Anatomy: A finite branch-and-bound algorithm for nonconvex quadratic programming via semidefinite relaxations (2008)

**Before 2026-10-10** (table verbatim):

> ### A finite branch-and-bound algorithm for nonconvex quadratic programming via semidefinite relaxations (Math. Program. 113:259–282, 2008, DOI 10.1007/s10107-006-0080-6; with Vandenbussche)
>
> | Dimension | Content |
> |---|---|
> | Origin | **Stated-joint** (award note, DOI 10.1007/s10589-010-9368-9): "a collaboration mostly motivated by the desire of each author to gain a greater understanding of the other's field of expertise"; 0-1 IPs first, then QP |
> | Why then | Vandenbussche & Nemhauser's finite LP branch-and-cut for box QP (DOI 10.1007/s10107-004-0550-7) |
> | Key insight | Finite KKT branching needs bounded relaxations; SDP relaxations "are bounded and hence suitable for use with finite KKT-branching" |
> | Minimum evidence | "the dual multipliers converged reasonably well even when the subproblems were solved very loosely" (note, p. 568) |
> | Abandoned paths | 0-1 IPs; instances with CPLEX failures omitted and said so; box-QP part split off into COAP 2009 (DOI 10.1007/s10589-007-9137-6; reason not stated) |
> | Reception | COAP Best Paper 2009; BoxQP instances became a standard test set; later overtaken (Tension 4) |
> | Methods shown | H1, H7, M4, M5 |

**Full text [S007, with S018 and H001].** Problem entry: existing global QP methods partition P and may need infinite trees in exact arithmetic; finite KKT branching gives unbounded LP relaxations whose box-case fix does not generalise [S007 pp. 2-3, 7]. Key idea: keep KKT branching, replace the LP node relaxation by an SDP relaxation joined to the multiplier constraints through the objective-equating constraint, which makes it bounded [S007 pp. 8-10, 14-15]. Evidence: 54 Vandenbussche–Nemhauser box QPs plus inventory, scheduling, Globallib and random instances; few nodes; the SDP solve is the bottleneck; instances with CPLEX failures omitted and disclosed; no external global-solver baseline [S007 pp. 15-23]. The box-QP specialisation re-proves correctness with multipliers eliminated [S018 pp. 7-10] and prints its loss to An and Tao [S018 p. 14]. Origin in the award note: cross-field pairing, loose inner solves, the pivot from 0-1 IPs to QP [H001 pp. 1-3].

<a id="anatomy-soc-trs"></a>

## Anatomy: Second-order-cone constraints for extended trust-region subproblems (2013)

**Before 2026-10-10** (table verbatim):

> ### Second-order-cone constraints for extended trust-region subproblems (SIAM J. Optim. 23:432–451, 2013, DOI 10.1137/110826862; with Anstreicher)
>
> | Dimension | Content |
> |---|---|
> | Origin | **Stated-joint:** "The authors of [21] asked whether there are exact convex formulations of TRS2p and TTRS" ([21] = Ye & Zhang 2003, DOI 10.1137/S105262340139001X) |
> | Key insight | Multiply a valid SOC constraint by a nonnegative linear factor and linearize: "We call an SOC constraint obtained in this fashion an "SOC-RLT" constraint." |
> | Minimum evidence | Re-proof of Sturm–Zhang; the three Ye–Zhang instances closed; Martínez-generated TTRS (unsolved after cuts: 4.1% at n = 5 to 10.4% at n = 20) |
> | Abandoned paths | Non-intersecting cuts conjectured (proved 2015 with Yang); intersecting cuts fail at n = 3; cut loop capped at 25 for numerical reasons |
> | Reception | GS 134. Five global solvers on the hard instances: "SDP relaxations and branch-and-bound have orthogonal difficulties" (Montanher et al., DOI 10.1007/s10898-018-0649-7) |
> | Methods shown | M2, M3, M4 |

**Full text [S012, preprint].** Problem entry: TRS is SDP-exact; what happens with added constraints, prompted by Sturm–Zhang and Ye–Zhang's open question; four variants ordered by the geometry of the feasible set [S012 preprint pp. 2-3]. Key idea: linearize the product of a valid linear factor and a valid SOC constraint (SOC-RLT); exact for TRS2p; for TTRS, SOC-RLT cuts indexed by supporting hyperplanes and separated by solving a TRS [S012 preprint pp. 2, 8, 14-15]. Evidence: Yuan's instance and the three Ye–Zhang instances closed; a Martínez-theorem generator credited to Wolkowicz, 1000 instances each for n = 5, 10, 20; cut cap of 25 for solver numerics; gap measured from the relaxation's own x*; a rank measure as second signal [S012 preprint pp. 16-23]. Stated takeaway: "An important implication of our results is that the computational complexity of solving an extended trust-region problem is highly dependent on the geometry of the feasible set." [S012 preprint p. 3]. Conjecture [S012 preprint p. 13] proved with Yang, "This paper shows that the convex relaxation has no gap for arbitrary m as long as the linear constraints are non-intersecting." [S021 p. 1].

<a id="anatomy-slight-lift"></a>

## Anatomy: A slightly lifted convex relaxation for nonconvex quadratic programming with ball constraints (2025)

**Before 2026-10-10** (table verbatim):

> ### A slightly lifted convex relaxation for nonconvex quadratic programming with ball constraints (Math. Program. 211:157–179, 2025, DOI 10.1007/s10107-024-02076-1; arXiv 2303.01624; sole author; published text not read)
>
> | Dimension | Content |
> |---|---|
> | Origin | **Stated:** "As we began this project, we were motivated by the idea of constructing an exact relaxation for (QP)." (v1, p. 2); presented as "Theorem (B 2023 — but gifted to Kurt)" |
> | Why then | **Inferred:** Anstreicher's Kronecker relaxation made a strong kitchen sink available; MOSEK on a laptop |
> | Key insight | "The key idea is a simple lifting of the original problem into dimension n+1." (v1 abstract) |
> | Minimum evidence | v1: experiments only. After "an important observation" by Anstreicher, v2 proves exactness for m = 2, inexactness for m ≥ 3, and "solved all 212" hard TTRS instances |
> | Reception | Kılınç-Karzan & Sun proved both conjectures (DOI 10.1007/s10107-025-02278-1). 2026: two follow-up conjectures refuted with exact certificates; a uint8 overflow means the printed 0.374 s mean time came from mis-scaled instances (no correction registered) |
> | Methods shown | M2, M3, M4 |

**Full text [S049, arXiv v2; the published text and v1 not in the corpus].** Problem entry: QP over m balls is polynomial for fixed m; Shor exact for m = 1; m = 2 exactness known only through a disjunctive two-PSD-variable SDP; goal, one non-disjunctive SDP strong irrespective of the data [S049 arXiv pp. 1-3]. Key idea: sandwich x'x ≤ β ≤ ρ_i² − c_i'c_i + 2c_i'x, which swaps m − 1 cone constraints for m linear ones; homogenize; Shor + RLT + SOC-RLT in dimension n + 2; for m = 2 add the linearized complementarity [S049 arXiv pp. 3, 11-14, 18-19]. Evidence: MOSEK on a laptop, public repository [S049 arXiv p. 4]; solved = relative gap < 10⁻⁴ and eigenvalue ratio > 10⁴ [S049 arXiv p. 10]; Shor-solved instances excluded; all 267 Eltved–Burer unsolved instances solved [S049 arXiv p. 15]; m ≥ 3 tables by joint status [S049 arXiv pp. 16-17]; all 212 hard TTRS instances [S049 arXiv p. 20]. Proof: every extreme ray of the relaxation has rank one, reusing the 2015 survey lemma [S049 arXiv pp. 20-24]. Open: no proof that Beta is at least as strong as Kron; four open questions; Anstreicher credited for the key observation [S049 arXiv pp. 16, 24].

<a id="anatomy-quadprogbb"></a>

## Anatomy: Globally solving nonconvex quadratic programming problems via completely positive programming (2012)

**Before 2026-10-10**: no anatomy (QuadProgBB appeared in Method 1 step 6, H5, H6, H8 and Tension 4).

**Full text [S008]** (Chen & Burer, *Math. Program. Comput.* 2012, DOI 10.1007/s12532-011-0033-9). Problem entry: general nonconvex QP over linear constraints, also framed as a substructure of trust-region variants; the paper sets out to show that two existing ingredients combine well [S008 pp. 2-3]. Key idea: keep the finite KKT branching tree, solve the DNN relaxation of the CP program that lifts duals and complementarities into one matrix with the 2010 decomposition algorithm, bound the duals by LPs [S008 pp. 4-8, 10, 12-13; S020 pp. 3-5]. Evidence: 243 instances (BoxQP 90, Globallib 83, CUTEr 6, RandQP 64) against the coauthor's earlier code at its best configuration and Couenne; performance profiles on non-trivial instances; losses to Couenne printed; trust-region extension solved 31 of 33 against 0 of 33 [S008 pp. 12-18]. Writing: main and secondary goals separated, notation warning, a failed design variant in a footnote [S008 pp. 3, 6, 11, 16]. Unstated limits visible in the text: no BARON comparison, the earlier code's CPLEX version could not be matched, finiteness not proved for the new relaxation [S008 pp. 4, 13-14, 19]. Methods shown: Method 1 (CP → DNN → solver), Method 5, H5, H8, H10, H12. Student first author; the founding theory is sole-authored [S004; S020].

<a id="anatomy-submodular"></a>

## Anatomy: On the semidefinite representability of continuous quadratic submodular minimization with applications to moment problems (2025–26)

**Before 2026-10-10**: no anatomy (the story of v1–v3 was in Method 3, Taste warning 2 and Latest, from web research).

**Full text [S058, arXiv 2504.03996 v3 only; v1 and v2 not in the corpus]** (Burer, Natarajan, Willemsen). Problem entry: an empty cell in a complexity table (submodular quadratic over [0,1]^n known polynomial only for DR-submodular or c ≤ 0), motivated by pricing with substitutes, a relaxed Chebyshev ambiguity set and covariance bounds [S058 pp. 2-5]. Key idea: use submodularity to drop the RLT lower bounds, prove the leaner SDP tight for n ≤ 3 through a completely positive certificate, break it at n = 4, dualize the n ≤ 3 result into SDP approximations of a moment cone [S058 pp. 9, 12, 14, 17-22]. Evidence: random submodular instances n = 4 to 20 plus 34,000 at n = 4 to 7 (global QP against the SDP dual bound, gap threshold 10⁻⁴); the n = 4 counterexample certified in exact arithmetic; RLT plus triangle inequalities shown not to close its gap [S058 pp. 26-36, 43-44]. Verdict graded: "The experiment is therefore best understood as evidence that violations of tightness are rare." [S058 p. 27]; "What fails at n ≥ 4 is therefore this particular semidefinite certificate, not necessarily tractability itself." [S058 p. 46]. Earlier error credited by name [S058 p. 46]. Methods shown: Method 2 (smallest dimension, boundary), Method 3 (certify exactly, narrow publicly).

---

<a id="anti-patterns"></a>

## Research anti-patterns

**Before 2026-10-10** (table verbatim):

> | Anti-pattern | Why he opposes it (source) | Do instead |
> |---|---|---|
> | Polynomial-time solvability offered as the end of the story | "it's known from beanstalk [= Bienstock] that you can solve this … in polynomial time but we're interested in tight convex relaxations" (2021, ASR) | Ask for the tight relaxation (M2) |
> | A mechanical hull without understanding | the disjunctive form "will give you the convex hole but we'd like to try a different approach" (2021, ASR) | Seek a direct description (M2 step 6) |
> | Claiming more than was compared | "Moreover, we do not compare with other methods" (2015, p. 3) | Scope disclaimer (H9) |
> | Improving your gap with another method's incumbent | "No Gurobi incumbent or point recovered by another method is used to improve an SDP method's gap." (2026 README, AI-assisted) | Report general solvers separately (H5) |
> | Trusting assumptions and numerics unchecked | "in any given application, make sure to double check!" (IPCO 2019 tutorial, on interior assumptions) | Check interiors, feasibility (H6) |
> | Work that runs only on your machine | absolute paths that others "may not have" (2015 teaching video, ASR) | Reproducibility kit (H10) |

**Full texts (2026-10-10).**
- *Claiming more than was compared*: "As ours is the first approach to study general perturbations in the literature, we are aware of no existing methods for this problem with which to compare our results." [S045 arXiv p. 23]; "In this sense, we cannot claim that optimizing the masked spectral bound is the “silver bullet” for solving extremely large and difficult instances." [S031 p. 14].
- *Improving your gap with another method's incumbent*: the 2026 paper text, "This gives a method-specific feasible upper bound; no Gurobi incumbent or point recovered by another method is used to calculate the gap." [S065 p. 12].
- *New row (2026-10-10): a primal-only method compared with bounding codes at face value* [S006 p. 9; S001 p. 13] → Method 6 (certificate from multipliers) or say no bound is available.
- *New row (2026-10-10): an unexplained cut or bound family left unexplained* [S050 arXiv p. 6; S039 arXiv p. 3] → H3.

<a id="research-trajectory"></a>

## Research trajectory

**Before 2026-10-10** (section verbatim):

> | Period | Main direction | Trigger | Representative work |
> |---|---|---|---|
> | 1998–2004 | Large-scale SDP algorithms; low-rank factorization | Advisor Monteiro's group; first-order push for bigger SDPs | Burer & Monteiro 2003, 2005 |
> | 2003–2006 | SDP as a bounding tool for nonconvex QP and binary IPs | Move to Iowa; Anstreicher; Vandenbussche's prior method | Burer & Vandenbussche 2008 |
> | 2006–2015 | Copositive/CP programming as a unifying lens, then computation | Special-case results to unify | Burer 2009; OptDNN 2010; QuadProgBB 2012 |
> | 2007–2014 | MIQCP / nonconvex MINLP relaxations and surveys | MILP-to-MIQCP transfer framing | Burer & Saxena 2012; Burer & Letchford 2012 (DOI 10.1016/j.sorms.2012.08.001) |
> | 2011–2026 | Trust-region variants as a long thread | Successive partners: Anstreicher, Yang, Eltved | Burer & Anstreicher 2013 → ball constraints 2025 → Lorentz cone 2026 |
> | ~2011–2020 | Analytics teaching, applied papers; copositive robust/DRO bounds (2014–18) | Renamed department; student Xu | Not core here |
> | 2018–2025 | Exactness of SDP relaxations; convex hulls of switching and bounded products | Co-authors (Ye, Anstreicher, Park) | Anstreicher, Burer & Park 2021 |
> | 2023 → | ML-adjacent optimization (constraint learning, trained networks) and submodular minimization | Student Zhu, colleague Serra, SUTD group | Zhu & Burer 2026 (DOI 10.1287/ijoc.2024.0815) |
>
> Reasons for leaving low-rank algorithms (2004), QuadProgBB (last commit 2016) and robust optimization (2018) are **not stated** anywhere found [06 Gaps].
>
> ### Latest
> - arXiv 2504.03996 v2 (April 2026, claim narrowed to n ≤ 3) and v3 (31 Aug 2026: n = 4 counterexample certified exactly, third author, credit to Han).
> - arXiv 2609.32017 (25 Sep 2026, with Anstreicher) on the Lorentz positive cone; three-level reproducibility repository; AI use acknowledged.
> - AI-co-authored code commits since December 2025; CPAIOR 2026 paper on trained neural networks (DOI 10.1007/978-3-032-27242-3_35).

**Full texts (2026-10-10)** (`08` §8; works carded per period: 2000–04 11, 2005–09 17, 2010–14 18, 2015–19 12, 2020–24 7, 2025–26 6).

| Period | Main topics (cards) |
|---|---|
| 2000–04 | SDP algorithms by change of variables: projected gradient on a factor, rank-two max-cut, Cholesky elimination, rank-one/two stable set, low-rank SDPLR, partial matrices, long-step framework [S014, S006, S017, S025, S030, S001, S029, S032, S051] |
| 2005–09 | Low-rank theory and enhancements [S003, S026, S031, H002]; lift-and-project bounds for 0-1 IP [S013, S041]; finite SDP B&B for QP [S007, S018]; copositive representation and CP/DNN [S004, S034, S028]; box-QP polyhedra [S011]; applied (ensembles, seed supply chain) [S005, S054, S015] |
| 2010–14 | CP/DNN computation and QuadprogBB [S020, S008, S047, H001]; hulls, cones and TRS with cuts [S010, S009, S022, S040, S037, S012]; MIQCP framing and survey [S016, S002]; "middle way" relaxations [S043]; analytics side papers [S042, S052, S053, S060, S063] |
| 2015–19 | TRS and quadratic hulls with Yang and Kılınç-Karzan [S021, S024, S033, S027, S036]; copositive robust/DRO and statistics with Xu [S045, S023, S044, S059]; applied [S046, S062] |
| 2020–24 | SDP exactness and its correction [S019, S061]; hulls of switching and bounded products [S038, S039, S067]; strengthened SDPs (OPF substructure, Stiefel) [S050, S055] |
| 2025–26 | Ball constraints, TTRS, Lorentz-positive cone [S049, S065]; submodular QP [S058]; Stiefel certificate [S048]; constraint learning and trained networks [S057, S056] |

Turns visible in the texts: (1) from algorithms for convex SDP to bounds for nonconvex and integer problems, about 2005–06 [S013 p. 24; H001 p. 2]; (2) [inferred] from finite B&B solvers to a single strong relaxation as the product: the relaxation aim is stated by 2011/12 [S016 preprint p. 2] and pursued from 2009 [S011; S010], alongside the KKT B&B line (2008–2012) [S007; S018; S008; S047], after which no new global QP solver appears in the cards; restated in 2023 [S049 arXiv p. 2]; (3) applied and analytics papers with Iowa colleagues and students 2012–2019 [S042, S052, S053, S060, S046, S045, S023, S044, S059, S062]; (4) ML-adjacent work with students and colleagues from 2025 [S048, S057, S056].

Corrections to the earlier dating: low-rank algorithm papers run to 2007 [S026 pp. 4-7, 19; S031 pp. 3-5], SDPLR is maintained as software in 2009 [H002 pp. 1-4] and applied in 2011 [S063 pp. 7-8], and the line returns in 2025 through certificates [S048 arXiv pp. 5-7, 14] (C7); the robust/applied period runs to 2019 [S062 pp. 5-8] (C8); the KKT B&B line runs 2008–2012 [S007, S018, S008, S047].

What stayed constant: the lifted matrix [1 xᵀ; x X] from the ensemble-pruning SDP [S005 pp. 7-8] to the Lorentz cone [S065 pp. 2-7]; the Pataki rank bound from 2003 [S001 p. 5] to 2026 [S065 p. 10]; losses printed with a hypothesis from 2001 [S014 preprint p. 17] to 2026 [S056 arXiv pp. 13-15]; claims graded by level from 2002 [S025 pp. 17-18] to 2026 [S065 pp. 10, 14, 16].

Collaboration (`08` §9): Monteiro coauthors 8 of the 11 carded works of 2000–04; Anstreicher 8 coauthored works 2005–2026 [S034, S028, S010, S012, S036, S038, S039, S065] plus the observation behind the 2025 main theorem [S049 arXiv p. 24]; students carry the toolkit into new domains (robust and DRO with Xu [S045, S059, S023, S044], constraint learning with Zhu [S057, S056]); the founding CP theory is sole-authored, its computation and solver went to a student [S004; S020; S008].

<a id="inner-tensions"></a>

## Inner tensions

**Before 2026-10-10** (section verbatim):

> 1. **Pay for strength vs buy speed.** "it can be worthwhile to pay for a computationally expensive, but strong, relaxation" (award note, 2010) and SDP at every node (2008–12) vs LP relaxations "are extremely desirable for branch-and-bound algorithms" (2009/12 chapter) and "Faster, but weaker" (2014).
> 2. **Computation-led conjectures vs rigour.** Conjectures later proved (2013 → 2015; 2023 → Kılınç-Karzan & Sun) vs a false Theorem 3 (2020) and a false polynomial-time claim (2025 v1); floating-point concerns "quite irrelevant" (2008) vs exact rational certificates (2026).
> 3. **Advice to the field vs own agenda.** "Finally, we believe there will be an increasing place for heuristics and approximation algorithms for non-convex MINLPs." (Burer & Letchford 2012, p. 104) vs no heuristic paper after 2002 and "a single strong bound" (2023).
> 4. **Representation as theory vs practical tool.** QuadProgBB "dominates the other solvers" on large dense box QP (Bonami et al. preprint 2016) vs "not a "magic bullet"", "always" outperformed by fix-and-bound (DOI 10.1007/s12532-024-00270-y) and "consistently slower than Gurobi" (arXiv 2508.20897).
> 5. **Open correction vs legacy residue.** Credited errata and 2026 audits vs arXiv 1802.02688 never updated, the uncorrected 0.374 s timing, retrospective slides citing only positive follow-ups, and BARON's shifting status 2008–2011.
> 6. **One lifting machine for 25 years vs pivots brought by collaborators and the institution** (analytics 2011–2020, ML from 2023).
> 7. **Insight via direct description vs disjunction as the proof device**, both in the same 2021 talk.

**Full texts (2026-10-10).**
- Tension 1 (pay for strength vs buy speed): "More generally, the paper also illustrates that it can be worthwhile to pay for a computationally expensive, but strong, relaxation" [H001 p. 3] against "In this paper, we describe a “middle way” between SOCP and SDP relaxations." [S043 p. 2]; the trade-off named inside one paper, "These numbers illustrate the tightness of the bounds provided by the SDP relaxation, but also point out the trade-off between the strength of a relaxation and the difficulty of solving it" [S018 p. 13].
- Tension 2 (computation-led conjectures vs rigour): an explicit rational counterexample point already in 2009 [S011 pp. 15-16], exact rational arithmetic in 2025 [S058 pp. 43-44] (C2); the 2008 floating-point remark [S007 p. 3]; the withdrawn 2020 theorem [S019 arXiv pp. 15-17; S061 pp. 1-2].
- Tension 3 (advice vs own agenda), narrowed (C6): no heuristic paper in his core nonconvex-QP line after 2002, but heuristics recur in coauthored applied papers: SDP relaxation plus randomized rounding for ensemble pruning (2006) [S005 pp. 7-8]; SDP rounding plus local search for hypergraph bisection (2011) [S063 pp. 4-5, 9]; specialised local search for trained networks, "In a nutshell, we double down on the trend of using specialized local search with lower per-iteration cost to find better solutions in constraint learning." (2026) [S056 arXiv pp. 6-9, 15].
- Tension 6 (one machine vs pivots brought by others): students carry the toolkit into robust optimization and constraint learning [S045; S023; S057].
- New Tension 8 (2026-10-10): relax into the convex lifted space (Methods 1–2) vs leave it for a smaller nonconvex space and certify from the multipliers (Method 6); the second is dormant in the cards from 2007 to 2024 and returns in 2025 [S001 p. 5; S048 arXiv p. 14].

---

<a id="coverage"></a>

## Coverage and remaining gaps

Coverage row of `python3 scripts/team_status.py product/minlp-team --coverage` (2026-10-10): Scholar rows 70; distinct works indexed 71; open full text 67; read in full 52; read in part 15; abstract only 2; metadata only (incl. unreadable) 2; skipped 0; book material carded 0; quotes verified 138. Card entries 73 (full 52, partial 15, abstract 3, metadata 2, unreadable 1; S061 has three entries, the last read in full). Works carded by period: 2000–04 11, 2005–09 17, 2010–14 18, 2015–19 12, 2020–24 7, 2025–26 6.

Remaining gaps (`08` §11): no open text for the two NSF award records (abstract only) [S068; S069], the 2001 thesis [S070] and the 2017 editorial [D001]; published versions of 18 works not read, a substitute version read instead (preprint: S012, S014, S016, S024, S051; arXiv: S019, S023, S027, S038, S039, S044, S045, S048, S049, S050, S055, S056, S057); S058 and S065 are arXiv-only; v1 and v2 of arXiv 2504.03996 not in the corpus, so the narrowing story rests on web research [S058 card header]; whether arXiv 1802.02688 was updated after the 2021 correction was checked in web research on 2026-10-10 (v2 unchanged, `03` 5.5), not by a card; the earlier error in the 2009 CP paper credited to Bomze is located (Proposition 2.3) but not described [S004 p. 17]; who did what in multi-author applied and ML papers is not stated; 15 works read in part; no full text states why he left the low-rank algorithm line (about 2007), the KKT B&B line (about 2012) or robust optimization (2019); no card between 2007 and 2024 applies the Method 6 certificate pattern.

<a id="corrections"></a>

## Corrections from the full texts

Each line gives the earlier SKILL.md wording (verbatim, in the *Before* blocks above), what the full texts show and the new wording. Nothing was deleted; the earlier wording stays in this ledger.

- **C1** Method 1 stop rule: "his answer was OptDNN and "Faster, but weaker" relaxations, not a defence" → the 2014 paper is motivated by interior-point SDP cost and does not cite Bao, Sahinidis and Tawarmalani [S043 pp. 2, 19]; OptDNN starts from a SeDuMi timing [S020 p. 4]. New wording: *consistent with*, not *his answer*.
- **C2** ⚠ Method 3 Practice ("2026 exact rational certificates") and Tension 2 → an explicit rational counterexample point already appears in 2009 [S011 pp. 15-16] (and rational counterexample data in 2010 [S010 p. 8]); certification in exact arithmetic is documented in 2025 [S058 pp. 43-44]; the 2026 counterexamples are certified by exhaustive stationary-point enumeration and a second solver, not in exact arithmetic [S065 p. 16]. Downgraded from ✗ to ⚠ on review (2026-10-10): the 2009 certificate is a hand-checkable rational point, not exact-arithmetic certification of a central claim.
- **C3** Method 3 step 2, two signals as a rule → intermittent: two-signal forms in 2003, 2013, 2017 [S001 pp. 14, 17; S012 preprint pp. 13, 19-21; S059 p. 15], single-signal declarations in 2015, 2023, 2025 [S024 preprint p. 28; S050 arXiv p. 22; S058 p. 27].
- **C4** Method 4 as a general habit → scoped to relaxation-strength claims in the trust-region/ball line and the BoxQP ladder; elsewhere public or random sets [S043 pp. 13-14; S008 pp. 14, 16].
- **C5** Method 5, the order prototype → theory → theory-first algorithm papers exist [S017 pp. 2, 25; S041 pp. 23, 25; S051 preprint pp. 4-22].
- **C6** Tension 3, Honest Boundary U1, Weak spots and Blind spots: "no heuristic paper after 2002" / "heuristics after 2002" → none in the core nonconvex-QP line; heuristics in coauthored applied papers 2006, 2011, 2026 [S005 pp. 7-8; S063 pp. 4-5, 9; S056 arXiv pp. 6-9, 15].
- **C7** Trajectory and U3: leaving low-rank algorithms in 2004, "no paper since 2004" → algorithm papers to 2007 [S026 pp. 4-7, 19; S031 pp. 3-5]; SDPLR maintained 2009 [H002 pp. 1-4]; return through certificates 2025 [S048 arXiv pp. 5-7, 14].
- **C8** Trajectory: robust optimization ends 2018 → 2019 [S062 pp. 5-8].
- **C9** H10 "Dated: 2023–26 only" → code public at least since 2009 (the SDPLR 1.03-beta guide is a maintenance release, six years after the 2003 paper) [H002 pp. 1-3]; QuadprogBB released with the 2012 paper [S008 p. 11]; seed and manifest discipline 2023–26.
- **C10** Ball-constraint quotes from arXiv v1 (web research) → the corpus holds v2, worded differently at those places [S049 arXiv pp. 10, 15]; the v1 quotes stay, labelled v1.
- **C11** Activation Rules, roundtable line "(no paper cards yet)" → 73 card entries exist since 2026-10-10. Fixed on review (2026-10-10): the line also names the disclaimer, so the T3.6 allowance (`--allow activation-disclaimer`) covers it; it now tells roundtable replies to cite paper cards as [samuel-burer card S011 p. 9] and research notes as [0N item].
- **C12** Method 2 say–do: the kitchen-sink practice predates the written programme: 2009 [S011 pp. 4, 15-16] and 2011 [S016 preprint pp. 5-12], before the 2012 survey and the 2021 label (a dating addition, not a contradiction).

<a id="card-key"></a>

## Card key

One line per card id used in SKILL.md, this ledger and the technique catalog, sorted by year (best read level; batch file in `cards/`). Venue, DOI and arXiv id: `07-paper-cards.md` and `../sources/publications/scholar.md`.

- **S014** (2001, full, batch c01) A projected gradient algorithm for solving the maxcut SDP relaxation. Coauthors: Renato D.C. Monteiro
- **S070** (2001, metadata, batch a2-01) New algorithmic approaches for semidefinite programming with applications to combinatorial optimization. PhD thesis, Georgia Tech, advisor R. D. C. Monteiro
- **S006** (2002, full, batch c01) Rank-two relaxation heuristics for max-cut and other binary quadratic programs. Coauthors: Renato D.C. Monteiro, Yin Zhang
- **S017** (2002, full, batch c01) Solving a class of semidefinite programs via nonlinear programming. Coauthors: Renato D.C. Monteiro, Yin Zhang
- **S025** (2002, full, batch c01) Maximum stable set formulations and heuristics based on continuous optimization. Coauthors: Renato D.C. Monteiro, Yin Zhang
- **S030** (2002, partial, batch s01) Interior-point algorithms for semidefinite programming based on a nonlinear formulation. Coauthors: Renato D.C. Monteiro, Yin Zhang
- **S069** (2002, abstract, batch a2-01) Collaborative Research: Theory and Implementation of Semidefinite Programming and Its Application to Combinatorial Optimization. NSF award record (investigators not carded)
- **S001** (2003, full, batch c02) A nonlinear programming algorithm for solving semidefinite programs via low-rank factorization. Coauthors: Renato D. C. Monteiro
- **S029** (2003, partial, batch s01) Semidefinite programming in the space of partial positive semidefinite matrices. Coauthors: none
- **S032** (2003, partial, batch s01) A computational study of a gradient-based log-barrier algorithm for a class of large-scale SDPs. Coauthors: Renato D.C. Monteiro, Yin Zhang
- **S051** (2003, partial, batch s01) A general framework for establishing polynomial convergence of long-step methods for semidefinite programming. Coauthors: Renato D.C. Monteiro
- **S003** (2005, full, batch c02) Local minima and convergence in low-rank semidefinite programming. Coauthors: Renato D. C. Monteiro
- **S034** (2005, full, batch s01) DC versus copositive bounds for standard QP. Coauthors: Kurt M. Anstreicher
- **S054** (2005, full, batch s01) Sharing classifiers among ensembles from related problem domains. Coauthors: Yi Zhang
- **S005** (2006, full, batch c02) Ensemble Pruning Via Semi-definite Programming. Coauthors: Yi Zhang, W. Nick Street
- **S013** (2006, full, batch c02) Solving lift-and-project relaxations of binary integer programs. Coauthors: Dieter Vandenbussche
- **S026** (2006, partial, batch s01) Computational enhancements in low-rank semidefinite programming. Coauthors: Changhui Choi
- **S068** (2006, abstract, batch a2-01) CAREER: Computation, Theory, and Applications for Nonconvex Quadratic and Conic Optimization. Coauthors: none
- **S031** (2007, partial, batch s01) Solving maximum-entropy sampling problems using factored masks. Coauthors: Jon Lee
- **S007** (2008, full, batch c03) A finite branch-and-bound algorithm for nonconvex quadratic programming via semidefinite relaxations. Coauthors: Dieter Vandenbussche
- **S015** (2008, full, batch c03) Coordinating the supply chain in the agricultural seed industry. Coauthors: Philip C. Jones, Timothy J. Lowe
- **S035** (2008, full, batch s02) On handling free variables in interior-point methods for conic linear optimization. Coauthors: Miguel F. Anjos
- **H002** (2009, full, batch s02) SDPLR 1.03-beta User's Guide (short version). Coauthors: Renato D. C. Monteiro, Changhui Choi
- **S004** (2009, full, batch c03) On the copositive representation of binary and continuous nonconvex quadratic programs. Coauthors: none
- **S011** (2009, full, batch c03) On non-convex quadratic programming with box constraints. Coauthors: Adam N. Letchford
- **S018** (2009, full, batch c03) Globally solving box-constrained nonconvex quadratic programs with semidefinite-based finite branch-and-bound. Coauthors: Dieter Vandenbussche
- **S028** (2009, full, batch s02) The difference between 5×5 doubly nonnegative and completely positive matrices. Coauthors: Kurt M. Anstreicher, Mirjam Dür
- **S041** (2009, full, batch s02) A p-cone sequential relaxation procedure for 0-1 integer programs. Coauthors: Jieqiu Chen
- **H001** (2010, full, batch c04) COAP 2009 best paper award. Coauthors: Dieter Vandenbussche
- **S010** (2010, full, batch c04) Computable representations for convex hulls of low-dimensional quadratic forms. Coauthors: Kurt M. Anstreicher
- **S020** (2010, full, batch c04) Optimizing a polyhedral-semidefinite relaxation of completely positive programs. Coauthors: sole author
- **S016** (2011, full, batch c04) The MILP road to MIQCP. Coauthors: Anureet Saxena
- **S047** (2011, full, batch s02) Relaxing the optimality conditions of box QP. Coauthors: Jieqiu Chen
- **S063** (2011, full, batch s02) A semidefinite programming approach to the hypergraph minimum bisection problem. Coauthors: Changhui Choi
- **S002** (2012, full, batch c04) Non-convex mixed-integer nonlinear programming: A survey. Coauthors: Adam N. Letchford
- **S008** (2012, full, batch c05) Globally solving nonconvex quadratic programming problems via completely positive programming. Coauthors: Jieqiu Chen
- **S009** (2012, full, batch c05) Copositive programming. Coauthors: none
- **S022** (2012, full, batch c05) Representing quadratically constrained quadratic programs as generalized copositive programs. Coauthors: Hongbo Dong
- **S042** (2012, full, batch s02) Robust rankings for college football. Coauthors: none
- **S052** (2012, partial, batch s02) Newsvendor games: convex optimization of centralized inventory operations. Coauthors: Moshe Dror
- **S012** (2013, full, batch c05) Second-order-cone constraints for extended trust-region subproblems. Coauthors: Kurt M. Anstreicher
- **S040** (2013, partial, batch s03) Separation and relaxation for cones of quadratic forms. Coauthors: Hongbo Dong
- **S037** (2014, partial, batch s03) Unbounded convex sets for non-convex mixed-integer quadratic programming. Coauthors: Adam N. Letchford
- **S043** (2014, full, batch c05) Faster, but weaker, relaxations for quadratically constrained quadratic programs. Coauthors: Sunyoung Kim, Masakazu Kojima
- **S053** (2014, partial, batch s03) MODIFYING SOYSTER'S MODEL FOR THE SYMMETRIC TRAVELING SALESMAN PROBLEM WITH INTERVAL TRAVEL TIMES. Coauthors: Nayoung Cho, Ann Melissa Campbell
- **S060** (2014, partial, batch s03) A first-order smoothing technique for a class of large-scale linear programs. Coauthors: Jieqiu Chen
- **S021** (2015, full, batch c06) The trust region subproblem with non-intersecting linear constraints. Coauthors: Boshi Yang
- **S024** (2015, full, batch c06) A gentle, geometric introduction to copositive optimization. Coauthors: none
- **S033** (2016, partial, batch s03) A two-variable approach to the two-trust-region subproblem. Coauthors: Boshi Yang
- **S046** (2016, partial, batch s03) Nearly-efficient tuitions and subsidies in American public higher education. Coauthors: Gary Fethke
- **D001** (2017, metadata, batch a2-01) Editorial. Coauthors: Alper Atamtürk
- **S027** (2017, partial, batch s03) How to convexify the intersection of a second order cone and a nonconvex quadratic. Coauthors: Fatma Kılınç-Karzan
- **S045** (2017, partial, batch s03) Robust sensitivity analysis of the optimal value of linear programming. Coauthors: Guanglin Xu
- **S059** (2017, full, batch s04) A branch-and-bound algorithm for instrumental variable quantile regression. Coauthors: Guanglin Xu
- **S023** (2018, full, batch c06) A copositive approach for two-stage adjustable robust optimization with uncertain right-hand sides. Coauthors: Guanglin Xu
- **S036** (2018, full, batch s04) Quadratic programs with hollows. Coauthors: Boshi Yang, Kurt Anstreicher
- **S044** (2018, full, batch s04) A data-driven distributionally robust bound on the expected optimal value of uncertain mixed 0-1 linear programming. Coauthors: Guanglin Xu
- **S062** (2019, full, batch s04) Three methods for robust grading. Coauthors: Veronica Piccialli
- **S019** (2020, full, batch c06) Exact semidefinite formulations for a class of (random and non-random) nonconvex quadratic programs. Coauthors: Yinyu Ye
- **S038** (2021, full, batch s04) Quadratic optimization with switching variables: the convex hull for n = 2. Coauthors: Kurt M. Anstreicher
- **S039** (2021, full, batch c07) Convex hull representations for bounded products of variables. Coauthors: Kurt M. Anstreicher, Kyungchan Park
- **S061** (2021, full, batch c3-01) Correction to: Exact semidefinite formulations for a class of (random and non-random) nonconvex quadratic programs. Coauthors: Yinyu Ye
- **S050** (2023, full, batch c07) Strengthened SDP relaxation for an extended trust region subproblem with an application to optimal power flow. Coauthors: Anders Eltved
- **S055** (2024, full, batch c07) A strengthened SDP relaxation for quadratic optimization over the Stiefel manifold. Coauthors: Kyungchan Park
- **S067** (2024, full, batch c07) Convex Hulls in Quadratic Space. Coauthors: Boshi Yang
- **S048** (2025, full, batch c08) A semidefinite relaxation for sums of heterogeneous quadratic forms on the Stiefel manifold. Coauthors: Kyle Gilman, Laura Balzano
- **S049** (2025, full, batch c08) A slightly lifted convex relaxation for nonconvex quadratic programming with ball constraints. Coauthors: none
- **S058** (2025, full, batch c09) On the semidefinite representability of continuous quadratic submodular minimization with applications to moment problems. Coauthors: Karthik Natarajan, Rick Willemsen
- **S056** (2026, full, batch c09) Optimization over trained neural networks: Going large with gradient-based algorithms. Coauthors: Jiatai Tong, Yilin Zhu, Thiago Serra
- **S057** (2026, full, batch c09) An extended validity domain for constraint learning. Coauthors: Yilin Zhu
- **S065** (2026, full, batch c10) Applications of the Lorentz positive cone in nonconvex quadratic optimization. Coauthors: Kurt M. Anstreicher

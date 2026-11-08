# RO · Robust, adaptive and distributionally robust optimization — Dimitris Bertsimas

> A domain file of the research-craft skill [SKILL.md](../../SKILL.md): the RO layer only; the methods are stated in full there, and here only as they show in this domain. **Scope** (team.json): uncertainty sets and the price of robustness, adaptive and affine policies, data-driven and distributionally robust optimization, robust nonconvex and simulation-based optimization. **Teams engaged**: NLP Team (`nonlinear-team`), MINLP Team (`minlp-team`), DFO Team (`dfo-team`). **Evidence base** (domain pack, 2026-10-29): 143 research works tagged RO, 125 with RO as primary and 18 as secondary tag; two rows are versions of others (S305 is the 2007 manuscript of S090, S926 the report version of S024), so 141 distinct works. Primary: 62 read in full, 24 in part, 8 at abstract and 10 at metadata level, 21 with no card (17 theses filed under his profile, two talk abstracts, two works not his). Secondary: 11 full, 1 partial, 6 with no card (theses). **Book material**, counted apart and never as research: the publisher's page of *Robust and Adaptive Optimization* [B011 p. 1] and a review of it [B012 p. 1] (primary tag), and his own books pages [B008 p. 1] (secondary). Every RO text is co-authored: "he" means the signed, joint text. **Research date**: 2026-10-29.

## 1. Footprint and timeline

| Period | RO primary | RO secondary | RO-primary share of his tagged research output |
|---|---|---|---|
| 2000–04 | 6 | 1 | 6/46 (13%) |
| 2005–09 | 18 | 0 | 18/57 (32%) |
| 2010–14 | 32 | 0 | 32/67 (48%) |
| 2015–19 | 31 | 7 | 31/112 (28%) |
| 2020–24 | 24 | 7 | 24/207 (12%) |
| 2025–26 | 8 | 2 | 8/63 (13%) |
| undated | 6 | 1 | 6/29 |

Book items excluded; the pack's own shares include them (2020–24: 26/212). The CV-title count of note 01 (§1.2) gives the same shape: 14%, 30%, 50%, 36%, 8%, 18%.

- **Entry.** A starred section on linear optimization under uncertainty already sits in the 2000 MBA text; only its title is on the card, so whether it is robust, stochastic or scenario-based is unknown [B015 p. 4]. *The price of robustness* was received in September 2001 [S001 p. 1]; a budget Γ normalised by standard deviations already sits in a 2002 credit-risk working paper with Pachamanova [S653 pp. 12–14], a work tagged AP/IO. How Γ arose and why he entered RO are on no card; the only stated intuition is that not all coefficients will change at once [S001 p. 3]. He entered three to four years after Ben-Tal–Nemirovski and El Ghaoui–Lebret and set himself apart by tractability and the discrete case (note 06 §4).
- **Waves** (note 01 §1.3; 08 §8.2): static, class-keeping sets 2002–07; adaptive policies, data-driven sets and limit-law sets 2008–15; sets and policies learned from data, ML and LLMs 2014–26.
- **Weight.** Peak share 2010–14 (48%). RO holds 9 of his 25 most-cited works (note 01 §1.7) and is the largest primary code among his 109 PhD theses: 24, of which 8 in 2000–09, 12 in 2010–19 and 4 in 2020–26 (note 04, domain table).
- **Exit.** None: insurance pricing [S669 p. 4], OCP's green-ammonia plant [S672 p. 3], ML-built sets [S440 p. 2] and a fifty-year retrospective with den Hertog [S614] (abstract only) date from 2025–26. One sub-line faded: "tractable stochastic analysis" by RO (queues, auctions, options, channel coding, 2010–18) [S065 p. 5; S119 p. 3], with two channel-coding manuscripts still listed as submitted (note 01 §3; note 06 §7).
- **With whom** (pack author fields): Sim, Pachamanova, Thiele (2000–04); Nohadani, K. M. Teo, Caramanis, Brown, Aghassi (2005–09); Goyal, Bandi, X. A. Sun, Iancu–Parrilo, ISO New England staff (2010–14); Bandi, V. Gupta, Kallus, Dunning, Georghiou, Youssef (2015–19); den Hertog, Koulouras, Koukouvinos, Pauphilet (2020–24); K. Zhu, Na, Stellato, I. Wang, Boucher (2025–26). Counting distinct carded works (book material, talks, theses, rows not his and the S305 version left out), Bandi and den Hertog co-sign eight each, Nohadani seven, Sim and Goyal six, Caramanis five. Students carry the line until about 2018; then den Hertog, a colleague and the book co-author [B011 p. 1], co-signs the theory of 2021–26.

## 2. Signature works

Chosen by citations (ranks 1, 3, 4, 6 and 13 of his whole output are RO, note 01 §1.7), his own emphasis (RO is the first of four programmes on his old research page, note 01 §1.2) and turning points (static → adaptive → data → simulation).

**2.1 Robust discrete optimization (2003) and *The price of robustness* (2004)** {RO IO LO} — DOI 10.1007/s10107-003-0396-4 [S004]; DOI 10.1287/opre.1030.0065 [S001]. Anatomy in SKILL.md SW3; added here:
- *Forced by*: Soyster too conservative, conic counterparts unusable for discrete problems, scenario robustness turning polynomial problems NP-hard [S004 p. 2]; the stated goal is tunable conservatism with tractability "both practically and theoretically" [S004 pp. 1–2].
- *Insight*: one budget per constraint, the inner maximum dualized into an LP or MIP [S001 pp. 3–4]; 0–1 cost uncertainty by n + 1 nominal problems, approximability carried over [S004 pp. 8–11]; robust min-cost flow by logarithmically many nominal flows [S004 pp. 12–15].
- *Minimum evidence*: a 0.57% violation bound for a 1.54% loss on a 200-item knapsack [S001 pp. 10, 12]; robust sorting for every Γ in under a second against 30–80 minutes per Γ for CPLEX [S004 p. 18]; the PILOT4 bad case, diagnosed by few uncertain coefficients per row [S001 pp. 14, 16].
- *Reception*: 7,185 and 2,690 Scholar citations; refinements and critiques in §5. *Methods*: M1, M3.

**2.2 *Theory and applications of robust optimization*** (SIAM Review 2011, first version 2008) {RO CP IO} — DOI 10.1137/080734510 [S003].
- *Forced by*: a field that grew fast after Ben-Tal–Nemirovski, El Ghaoui and interior-point methods [S003 p. 2].
- *Insight*: the inner subproblem decides tractability, so results form a table of nominal class × set class → counterpart class, each beside its nearest NP-hard neighbour, the S-lemma marking the boundary [S003 pp. 10–16].
- *Minimum evidence*: one portfolio example: about 5.2 hours for 8 points of the exact MIP frontier against under 10 minutes for 600 robust problems; under 2% perturbation the exact solutions always lose to a robust model [S003 pp. 6–7]; "only one random trial" is admitted [S003 p. 7].
- *Reception*: 3,831 citations. Its three open problems, tractable adaptability, when robustness is cheap or expensive, and a data-driven theory [S003 pp. 43–44], set his next decade (2.3, 2.5). *Methods*: M1; Heuristic 1 [S003 p. 37].

**2.3 Power and limits of static and affine policies (2010–2015)** {RO LO IO} — S134 (DOI 10.1287/moor.1090.0440), S042 (DOI 10.1287/moor.1100.0444), S060 (DOI 10.1007/s10107-011-0444-4); companions S165, S217, S176, S192.
- *Forced by*: affine rules advocated with "very little progress" on the quality of their values [S042 p. 3]; the fully adaptive problem hard to approximate within O(log m) [S060 p. 2].
- *Insight*: grade a tractable policy class against the adaptive optimum by a constant of the set alone, and build the family that attains it. Static robust is within 2 for symmetric sets and exact for hypercubes [S134 pp. 8–9, 20–21], 1 + ρ/s in general [S165 p. 21]; affine policies are optimal in one dimension [S042 p. 5] and on simplices [S060 pp. 6–8], Ω(m^{1/2−δ}) worse in general, O(√m) when A ≥ 0 [S060 pp. 15, 23].
- *Minimum evidence*: tight and unbounded examples for every bound [S134 pp. 6, 12–18]; a T = 4 counterexample: 838.493 against 873.248 for affine policies, and 876.057 (4.4%) when the costs are made affine too [S042 pp. 25–26].
- *Reception*: citers restate the scope as one-dimensional (note 05 §4.4); the group printed its own limit: "This lower bound is in contrast to strong empirical evidence of the performance of affine policies." [S060 p. 4]. *Methods*: M7 in RO form; M1 step 5.

**2.4 Adaptive robust unit commitment with ISO New England** (IEEE TPWRS 2013) {RO IO AP} — DOI 10.1109/TPWRS.2012.2205021 [S006].
- *Forced by*: renewables, and an operator's reserve rule set "by some ad-hoc rules", against stochastic UC's distributions and scenarios [S006 pp. 1–2].
- *Insight*: commitment against every injection in a budgeted set, dispatch fully adaptive; the bilinear worst case solved by MINLP's outer approximation inside a Benders loop [S006 pp. 2–5].
- *Minimum evidence*: ISO-NE's system (312 units, 2,816 nodes), the operator's rule given the same knob, loads from two distributions; dispatch savings up to 2.7% over the budget range and 1.86–6.96% with the CLT-set budget [S006 p. 6]; cost standard deviations 8.15–14.48 times lower [S006 p. 7]; 6.14 h against 1.65 h printed [S006 p. 5]; a result "quite contrary to the general impression that robust optimization is always conservative" [S006 p. 6].
- *Reception*: 2,153 citations; a published discussion and the authors' closure [S380] (not read); the energy line continues [S531 p. 4; S400 p. 2]. *Methods*: M5, M3; Tension T1 (the inner solver guarantees a local optimum only [S006 p. 4]).

**2.5 Data-driven robust optimization** (Math. Program. 2018; arXiv 2013–14) {RO DA} — DOI 10.1007/s10107-017-1125-8 [S013]; with Robust SAA [S039].
- *Forced by*: sets chosen by a priori reasoning, and data that call for "a shift in thinking" [S013 p. 2].
- *Insight*: a test's confidence region → a convex bound on worst-case VaR → the set with that support function, with a guarantee holding with probability 1 − α over the sample [S013 p. 10]; Robust SAA adds convergence [S039 p. 3].
- *Minimum evidence*: a catalogue of sets with counterparts; synthetic portfolio and queue cases; sets chosen by hold-out, since "size calculations alone cannot predict performance" [S013 pp. 29–32].
- *Reception*: 1,055 citations; his group's answer to the critique that Γ is set arbitrarily (note 05 §4.1); sets from trained predictors follow in 2025 [S440 pp. 2–3]. *Methods*: M3 (knob from data), M1.

**2.6 Robust optimization of simulation-based problems** (Operations Research 2010) {RO HS AP} — DOI 10.1287/opre.1090.0715 [S090]; with S116, S141, S234, S278.
- *Forced by*: designs that fail under implementation errors, and convex RO that does not apply when the cost is a simulation [S090 p. 2].
- *Insight*: a direction descends for the worst case iff it makes a negative inner product with every worst error; an SOCP gives the best one; robust local search follows [S090 pp. 4–8].
- *Minimum evidence*: a 100-dimensional electromagnetic design, worst case 8% lower at unchanged nominal cost, Γ from measured errors [S090 p. 12].
- *Reception*: its test problem became standard in derivative-free robust optimization (note 05 §4.6; §6.3). *Methods*: M1 left on purpose; correction C3 (convergence only for convex costs with an exact worst-error oracle [S090 p. 5]); Tensions T1, T2.

## 3. How he works here

Of the 85 distinct primary RO works read in full or in part, card links name M1 in 84 (65 evidence, 22 variant, one contradiction), M3 in 71 (18 evidence, 55 variant), M4 in 42 (three contradictions), M5 in 27 (6 with evidence links, 24 with variant links, three with both), M6 in 26 (25 evidence, one variant) and M2 in 12 (all variants); M7 was promoted after carding, and 21 of its 79 works carry RO (08 §4).

**M1 · Formulation first, kept in the solver class.**
- Dualize the inner maximum and inherit the class [S001 pp. 3–4; S004 pp. 5–6]; any norm set through the dual norm [S019 pp. 3–5]; cone-keeping conic approximations [S022 pp. 6–8]; a coherent risk constraint on samples as a robust constraint [S024 p. 5].
- Robust = nominal on modified data: demand [S014 p. 6], arrivals [S233 p. 12], capacities [S275 p. 20]; the robust fluid model stays a separated continuous LP [S244 p. 2].
- The boundary printed: correlated ellipsoids [S167 p. 4]; robust SDP and two-stage problems [S003 pp. 13–15, 24]; minimax LP with uncertain right-hand sides [S053 pp. 9–10]. The class left: Benders with outer approximation and measured times [S006 pp. 4–5, 9]; a labelled heuristic for simulators [S090 p. 6]; exact global separation by RPT branch and bound, with Koukouvinos in 2023 [H001 pp. 12–13, 16] and in DRO with den Hertog [S867 pp. 9–12].
- ⚠ Say–do: in 2018 the sets are called tractable "both theoretically and practically" [S013 p. 1], with no solve time, solver or machine anywhere in the experiments [S013 pp. 30–36]. 🔴 Correction: the 2006 inventory model protects each constraint separately; its own Remark 1 notes that no single demand realizes both worst cases of a period [S014 p. 4] (note 05 §4.3).

**M3 · The price of robustness.**
- Knob, solution-independent bound, kept class, curve with its bad case [S001 pp. 3–16]. The knob's source moved: hand-set Γ (2004); moments [S014 pp. 10–12]; the central limit theorem [S006 p. 6]; measured error statistics [S090 p. 12]; the decision-maker's risk measure [S024 p. 3]; hypothesis tests and hold-out [S013 pp. 29–30]; a coverage share p tied to a stakeholder metric [S400 p. 2]; a validation-loss order statistic [S440 p. 10]. Hand-set knobs persist [S163 pp. 24, 28; S458 pp. 4, 7].
- The price of a policy class or of coupling, as a constant of the set [S165 p. 21; S392 pp. 13–23].
- Misspecification duel: robust and model-based optima scored under other distributions [S014 p. 12; S055 pp. 8–9; S059 pp. 9, 11, 14].

**M7 · Bound before policy (RO form).** Bounds valid for every policy from binding scenarios [S138 pp. 7–9; S087 pp. 34–35; S082 pp. 11–12, 15, 17]; policies read off a tractable class (affine, finite, polynomial with the degree as the one knob [S075 p. 9]; k plans [S049 pp. 2–3]); the field's incumbent, the affine rule, graded by tight ratios (2.3). ⚠ Limits: his group calls its own adaptability bounds "quite loose" or hard to compute [S392 p. 7]; scenario lower bounds can be weak [S087 p. 52].

**M5 · Judge against the owner's rule.** The operator's reserve practice [S006 pp. 1, 5]; NFIP's actual premiums and a moving-average rule [S669 pp. 4, 23–28]; Hartford Hospital's census [H004 p. 22]. ⚠ Variants: an owner-set objective, but a nominal baseline on synthetic data, not a heating-oil company's current schedules [S327 pp. 2, 20–22]; the owner's decision and contract terms, judged against perfect foresight and the group's own earlier device, not OCP's plan [S672 pp. 1, 3, 5, 22–23]; in the theory papers, synthetic instances and literature baselines [S028 pp. 12–15]; ambulances against literature models, not the agency's plan [S224 pp. 6–9].

**M4 · Exact solve, certificate, duel.** A statistical benchmark of reformulation against cutting planes on 183 LP and 40 MIO instances, ending in a hybrid: "a hypothetical robust optimization solver should follow this hybrid strategy" [S088 p. 22]; adaptive partitions match a rival's values at sizes the rival could not solve, on the rivals' own instances [S087 pp. 43, 45, 48]; SDP baselines kept only when a solver certifies them [S028 p. 12]. ✗ Contradictions: robust annealing "warrants a global robust optimum" [S141 p. 9] while runs stop at an empirical threshold [S141 p. 11]; ChatGPT shown to work "with little to no errors" from curated transcripts with unremarked problems [S330 pp. 1, 13–19]; a product-line heuristic without certificate [S164 pp. 8, 12].

**M2 · Why now** (unquantified in RO): theory plus interior-point methods [S003 p. 2]; data [S013 p. 2]; LLMs [S330 pp. 1–4]; "practical efficiency" as realistic size for the application [S172 p. 5]. No RO card carries a speed-up figure.

**M6 · Programme.** 24 RO theses, co-advising with Parrilo (note 04); RO as lecture 8 of 24 in his 2009 methods course [B021 p. 2], then a course of its own, 15.094 (note 04); an NSF award planning a unifying robust optimization book [S464]; the 2022 book with den Hertog, which places ARO (Part II) right after linear RO and before nonlinear RO, "as opposed to presenting RO first and then ARO", because, jointly stated and unverified, ARO solves RO problems in new ways [B011 p. 1]; student software (JuMPeR, note 03 B4.6) and ROC [S028 p. 10]; the 2026 retrospective [S614].

**Heuristics here.** H1: robustification equals regularization, and where it breaks [S085 pp. 7–15]; averaged uncertainty over symmetric sets gives ridge [S530 pp. 9, 18–19], but not over non-symmetric polytopes [S530 p. 20]; ARO overfitting read as regularization [S623 pp. 2–4]. H10: one dual-norm theorem recovers the SOCP (Euclidean norm) and, through the D-norm, the budget LP [S019 pp. 3–5]; RPT recovers Bertsimas–Sim and the S-lemma [S283 pp. 3–4, 15–19]; the classical fluid model at Γ = 0 [S244 pp. 9–10]. H4: PILOT4 [S001 p. 14]; "rather disappointing" complexity [S117 p. 10]; a search depth that never terminates [S090 p. 15]. H2: Pareto ARO written with Trichakis, co-author of the Pareto critique [S348 pp. 1–2].

**Domain moves** (technique catalog §§1.1–1.2, 2–4):
- *Proof devices*: fractional budget and exchange argument [S001 pp. 3–5]; a bound ladder, simple to tight to computable to asymptotic [S001 pp. 5–8]; one threshold θ for budgeted 0–1 costs [S004 pp. 8–9]; symmetry scaling [S134 pp. 8–9]; zonogon forward induction [S042 pp. 7–9]; double dualization that swaps dimensions [S138 pp. 4–8]; Fourier–Motzkin elimination of adaptive variables [S348 p. 8]; lifted ambiguity sets [S028 pp. 5–7]; Danskin-based descent for the worst case [S090 pp. 4, 16–17]; limit laws as sets [S119 pp. 7–13].
- *Algorithms*: Voronoi partitions around binding scenarios [S087 pp. 8–17]; a parallel hybrid [S088 pp. 16–20]; an inexact oracle in the loop and an exact one at termination [S313 pp. 9–13]; learned ARO strategies [S267 pp. 9–12].
- *Protocol*: the rival school's own instances [S001 pp. 12, 14]; out-of-model perturbations with CDF dominance [S004 pp. 18–22]; the incumbent given the same knob, with out-of-set samples [S006 pp. 5, 7]; the exact method's solve times printed on the frontier [S003 p. 6].
- *Writing*: the price named in the abstract [S001 p. 1]; the myth corrected by name [S006 p. 6]; "surprising" equivalences [S134 p. 21; S176 p. 1]; numbered open problems [S003 pp. 43–44]; a dated proof-repair note [S747 p. 1].

**Say–do gaps** besides those above: T1, an abstract calling solutions robust against all realizations over a local inner solver [S006 pp. 1, 4], and a termination rule called an optimality condition after admitted late discoveries [S090 pp. 12, 15]; a conclusion that the robust policy "often outperforms" the nominal one with no such experiment [S014 p. 19]; the October 2009 manuscript's abstract promising O(√k) where its body proves O(√m) [S060 pp. 1, 4, 31, 35]; a recommended insurance model that uses neither the ML set featured in the abstract nor damping [S669 pp. 1, 14–15].

## 4. Taste: what he picks and what he refuses

**Picks**
- Sets that keep LP or MIP over ellipsoids for discrete problems [S001 pp. 2–3; S004 p. 2]; between two close sets, the one with the more mature conic class [S013 pp. 14, 27].
- Uncertainty as a modelling choice: "Modeling uncertainty using a probability distribution is a choice we make, and it is not a primitive quantity fundamentally linked to the application." [S165 p. 2]; a fitted process is "a model of reality, not reality itself" [S171 p. 1]; limit laws as primitives [S065 p. 5].
- Simple policy classes with proved limits over exact dynamic programming (2.3); data as the source of sets from 2008–09 (samples plus a risk measure [S024 pp. 5–6]; Γ tuned on validation data in a 2008 preprint [S233 pp. 13–14]), hypothesis tests from 2013–14 [S013 p. 2], and trained models in 2025 [S440 p. 2].
- Problems with an owner and data: power systems, insurance, hospitals, air traffic, supply chains (§3 M5).

**Refuses**
- Full protection, conic counterparts for discrete problems, scenario-based robust discrete models [S004 p. 2]; distributions and scenario trees [S004 p. 1; S006 pp. 1–2; S275 pp. 4–5]; dynamic programming's dimensionality [S014 p. 1].
- Robust control and rectangular robust DP stay outside his survey [S003 pp. 2, 23]; complete adaptability is "overly optimistic" [S049 pp. 1–2].
- Reading a bound-optimal decision rule as a policy: "we caution against using the optimal decision rule as a policy." [S028 p. 10]
- [inferred] A computational duel with the rival school's sets, in the founding paper: there the ellipsoid comparison stays analytical and "inconclusive" [S001 p. 8]. Later the 2008 survey runs an ellipsoidal set beside the budget set [S003 pp. 5–7] and S088 times ellipsoidal counterparts [S088 pp. 8–9, 13–14]; still, no a priori set is a baseline in the data-driven paper [S013 pp. 30–36], and no competing robust method is run on the simulator [S090 p. 12].
- [inferred] Certificates for nonconvex robust problems until the RPT route of 2023–26 (§3 M1).

## 5. Critiques, failures and limits on record

| Target | Critics and what they showed | His reply |
|---|---|---|
| Budget sets (2004) | Iancu–Trichakis 2014: robust optima need not be Pareto optimal; Poss 2013: budgets that depend on the solution are less conservative; Büsing et al.: Γ chosen arbitrarily (note 05 §4.1) | In papers, not replies: sets from data (2.5); guarantees for dependent noise [S215 pp. 18–20]; Pareto ARO with Trichakis [S348 pp. 1–3]; signed budgets [S836 pp. 6–7]. A solution-dependent budget already sits in an unpublished 2004 manuscript [S167 pp. 16–18] |
| Robust discrete (2003) | Álvarez-Miranda–Ljubić–Toth, Lee–Kwon: fewer than n + 1 nominal problems suffice (note 05 §4.2). Cho, Burer and Campbell 2014, on the interval TSP: the budget model needs one TSP per edge plus one, lacks the monotone comparative statics of their modified Soyster model (a 5-node counterexample) and took up to about 33,000 s at n = 175; their worst-case win comes on constructed instances they call "somewhat ad hoc" [samuel-burer card S053 pp. 2–4, 18–19, 21, 23–24] | None needed for the refinements; none found to Cho–Burer–Campbell |
| Moment-based DRO (from 2010) | Xu and Burer 2018: moment-based sets ("Bertsimas et al." on the card) do not converge as samples grow, and the moment bound stays flat while a Wasserstein bound tightens [samuel-burer card S044 arXiv pp. 3, 17] | In papers, not replies: test-based sets with convergence [S039 pp. 3, 13]; in 2026 moment and confidence sets kept for small-sample, expert-driven and regulatory settings [S867 p. 2] |
| Robust inventory (2006) | Bienstock–Özbay: conservative; Park: incorrect for the stated set, exact for a cumulative-demand set (note 05 §4.3) | No reply in words; in 2020 his group computes base-stock levels with Bienstock–Özbay's adversarial decomposition without citing the 2006 paper [S379 pp. 11–12] |
| Affine policies (2010) | Citers: optimal only in one dimension (note 05 §4.4) | Self-quantified [S060 pp. 4, 15] |
| Robust queueing (2015) | Whitt–You: sets hard to choose and tie to the real queue, the first network analyzer worse; Goldberg–Li: no Halfin–Whitt scaling (note 05 §4.5) | None found; his averaged worst cases err by up to 30% for heavy-tailed 20-server queues [S268 p. 21]; the line faded |
| Simulation-based RO (2010) | Menickelly–Wild: heavy computation, a test problem now standard; Zheng et al., Cakmak et al.: single objective, implementation errors only (note 05 §4.6) | None found |
| The 2022 book | Cuvelier: no criticism; pragmatic, computing time over complexity class [B012 p. 1] | n/a |

- **Failures and repairs**: no retraction in RO; a dated note repairs the proofs of a published adaptive-RO paper for general convex sets [S747 p. 1]. Stalled manuscripts (note 01 §3; note 06 §7): channel coding, parts 1 and 2, whose upper bounds stay approximate [S554 p. 23; S745 p. 11]; the price of flexibility [S488]; inventory routing [S327]; dynamic pricing [S200].
- **Limits the papers admit**: price-of-robustness studies "have been largely empirical" and most adaptable problems intractable [S003 p. 43]; the static solution can be arbitrarily worse than the two-stage stochastic optimum under cost [S134 p. 15] or constraint-coefficient uncertainty [S217 p. 14], while against the adaptive robust optimum it stays within 4 [S134 p. 19] or 1 + ρ/s [S217 pp. 9–11]; AMIO "has yet to see an equivalent development" to cutting planes [S087 p. 52]; "This phenomenon of adaptive policies being brittle is analogous to overfitting in machine learning." [S623 p. 1], seen again in the ammonia plant [S672 p. 24]; projections of coupled sets are intractable in high dimension [S392 pp. 6, 54]; guarantees need validation data [S440 p. 4]; fewer large violations bought with more frequent ones [H004 p. 2].

## 6. Cross-team interfaces

Each meeting point gives his position, the guest's as their own skill and cards state it, the evidence on both sides, the relation, what is contested and a deciding test. "Exchange in print" means one side's text cites the other's work; no meeting point records a reply.

### 6.1 NLP Team (`nonlinear-team`)

Curtis, Wächter, Nocedal and Ye meet RO on the cards and notes; Fletcher meets it through outer approximation (6.2). No RO card or stated RO view was found for Wright, Gill, Toint, Gould, Nesterov or Robinson.

**Curtis · certified gaps in column-and-constraint generation** (complement; a contrast of methods, the card shows no citation of Bertsimas; Curtis is third author with Tsang and Shehadeh, the corresponding author, and his part is not stated [frank-e-curtis card S016 arXiv p. 1]).
- *His*: ARO with a nonconvex inner problem, solved by outer approximation that guarantees a local optimum only [S006 p. 4]; where relatively complete recourse fails, an unguaranteed fast feasibility oracle in the loop with an exact one at termination [S313 pp. 2–3, 9–13]; learned strategies, admitting that the generation method can return suboptimal solutions [S267 p. 5]. Only S313 ends with an exact check.
- *Theirs*: assuming relatively complete recourse, a finite or polyhedral set and an exact subproblem oracle [frank-e-curtis card S016 arXiv p. 3]: masters solved to a relative gap, the last certified lower bound kept, backtracking with tighter tolerances; "allowing inexactness is not something that can be done naively." [frank-e-curtis card S016 arXiv pp. 4–9]; finite termination is proved for Algorithm 2, while the experiments run a time-limit variant without proof [frank-e-curtis card S016 arXiv pp. 9–11]; 240 robust scheduling instances [frank-e-curtis card S016 arXiv pp. 10–13].
- *Contested and test*: may an ARO solve ship without a certified gap (his Tension T1)? (i) On S016's operating-room instances, which have relatively complete recourse: i-C&CG against S313's method (inexact oracle in the loop, exact check at the end), same solver and limit, time to a certified 1% gap. (ii) On S313's lot-sizing and location–transportation instances, which lack it [S313 pp. 15–18]: the share of infeasible or suboptimal first stages from i-C&CG's inexact masters and from S313's in-loop oracle alone. S006 stays out unless its inner maximum is solved globally.

**Curtis, Wächter · chance constraints against budgeted sets** (conflict; a contrast of methods).
- *His*: a set with an a priori, solution-independent violation bound [S001 pp. 4–6], extended to any convex set [S215 pp. 5–12] and to dependent noise [S215 pp. 18–20].
- *Theirs*: the sampled chance-constrained NLP solved directly and locally [frank-e-curtis card S027 pp. 4–11], started from, and scored against, the solution that enforces all N sampled constraints [frank-e-curtis card S027 pp. 23–26]; convex approximations are called conservative and not run [frank-e-curtis card S027 p. 3]; no budgeted set appears on the card; Wächter writes chance constraints as smooth quantiles so an interior-point method applies (andreas-wachter SKILL.md, "Method 4").
- *Contested and test*: tractable a priori protection against exact sampled constraints solved locally. On their cash-flow instances [frank-e-curtis card S027 pp. 23–24], add his budgeted set as a third arm beside their all-constraints start: out-of-sample violation, cost and time of each answer.

**Nocedal · what robustness means for a noisy simulator** (complement; a contrast, no citation either way on the cards).
- *His*: the worst case over a ball of implementation errors, Γ from measured errors, the worst case only estimated [S090 pp. 3, 12].
- *Theirs*: keep the classical method and repair only the operations that compare or difference noisy values [jorge-nocedal card S128 arXiv pp. 1–2, 8–9]; the horn test bed's objective is mean plus three standard deviations estimated by sampling [jorge-nocedal card S128 arXiv pp. 5–6]. Nocedal's group uses a worst case over a box, estimated by a few L-BFGS-B iterations, as a sharpness diagnostic [jorge-nocedal card S006 pp. 5–6], and sets robust optimization aside as "not feasible in our context" because it needs an SOCP per iteration [jorge-nocedal card S006 p. 15]; the card does not say which robust method is meant, and S090's direction step is an SOCP [S090 p. 5].
- *Contested and test*: the per-iteration cost of a worst-case step at scale, and how noise in an estimated robust objective is handled. At growing dimension: per-iteration time and final estimated worst case of S090's SOCP step against a noise-tolerant gradient step with relaxed line search on the same worst-case estimate [jorge-nocedal card S128 arXiv p. 8].

**Ye · moment-based distributionally robust optimization** (exchange in print, one-way).
- *His*, on both sides: moment sets of his own, a minimax stochastic LP over all distributions with a given mean and second-moment matrix reduced to one SDP, which positions itself against Delage–Ye and credits it with the broader class [S053 pp. 2–3, 5], and in 2026 moment and confidence sets kept for small-sample, expert-driven and regulatory settings [S867 p. 2]; against them, data-driven sets reinterpret Delage–Ye through hypothesis testing and bootstrap its thresholds [S013 pp. 4–5, 23–27], and Robust SAA credits data-driven DRO with finite-sample guarantees but no convergence, and adds it [S039 pp. 1–5]. In Robust SAA's duel the Delage–Ye bound converges to Scarf's bound, not the optimum, and in the portfolio it is valid but neither convergent nor stable [S039 pp. 24–29]; its set is c-consistent only for costs quadratic in ξ [S039 p. 15].
- *Theirs*: Delage & Ye (Operations Research 2010, DOI 10.1287/opre.1090.0741) is Ye's third most-cited work, written with his PhD student (yinyu-ye note 01 §1.5); his homepage says his group coined the name DRO, and a 2017 talk gives the rationale, deciding when things cannot be predicted accurately (yinyu-ye note 02, §§2.7 and 3.7). No reply to Bertsimas is on file. Xu and Burer fault the moment-based sets of "Bertsimas et al." for not converging [samuel-burer card S044 arXiv p. 3].
- *Contested and test*: moment sets (one convex program, no convergence as samples grow) against test-based sets (finite-sample and asymptotic guarantees, heavier cones), with his own work on both sides. Robust SAA's newsvendor and portfolio duel is the existing, one-sided result [S039 pp. 24–29]. Rerun it with one cost quadratic in ξ, where Delage–Ye's set is c-consistent, beside a non-quadratic cost; drop the unbootstrapped Delage–Ye arm where its concentration thresholds do not apply (N ≤ 50,000 [S013 p. 25]) or extend N past that point; report out-of-sample cost and coverage, plus solve time, which neither paper prints.

### 6.2 MINLP Team (`minlp-team`)

**Grossmann, Leyffer · outer approximation inside adaptive RO** (exchange in print: S006 cites both outer-approximation papers).
- *His*: the bilinear worst case linearized by the outer approximation of Duran–Grossmann and Fletcher–Leyffer, which here guarantees a local optimum only, its dual cuts still valid [S006 pp. 2, 4–5]; the textbook MIO linearization was slower [S006 p. 9].
- *Theirs*: among Grossmann's first questions are which small instance has a verified optimum and whether the claim is guaranteed (if not, how far off, measured); he pushes back on global claims without a certificate and, stated only, on uncertainty before the deterministic model solves well (ignacio-e-grossmann SKILL.md, "Roundtable Card"). Leyffer's polytopic-superset method keeps every iterate robust-feasible and converges to stationarity [sven-leyffer card S169 pp. 6–17], for convex C1 constraint functions, constraints affine in u and a convex U [sven-leyffer card S169 pp. 2–3, 15].
- *Contested and test*: outer approximation used outside the convex setting where it is exact. On a reduced ISO-NE instance, also solve the worst case globally; report how often the local one falls short and the cost difference it makes.

**Leyffer · nonlinear robust optimization** (exchange in print per a Semantic Scholar snippet on the INFOR version, note 05 §4.6; the card, read from the 2018 TR, shows the implementation-error section [sven-leyffer card S021 TR pp. 18–19] without naming the cited paper).
- *His*: robust local search, a heuristic beyond convex costs [S090 pp. 5–6], for an unconstrained problem whose errors enter a nonconvex f nonlinearly [S090 pp. 2–3]; a global claim for robust annealing [S141 p. 9]; safe approximations for robust convex constraints [S283 pp. 3–13].
- *Theirs*: nonlinear RO organized by bilevel and MPEC forms, duality, Polak-type outer approximation and implementation-error methods, a robust local minimum possibly "practically dissatisfying" [sven-leyffer card S021 TR pp. 7–8, 12–19]; "This maturity level is not surprising when viewed through the lens of reformulation." [sven-leyffer card S021 TR p. 22]
- *Contested and test*: what a local robust solution certifies. On the 2-D polynomial only, robust local search against the survey's Polak-type outer approximation, which needs only C1 data and a compact set [sven-leyffer card S021 TR pp. 17–18], at equal evaluations, each final worst case certified on a dense grid. If robust-feasible iterates are to be contested too, use a constrained instance with constraints affine in u, such as the polytopic-superset paper's asset allocation [sven-leyffer card S169 p. 19].

**Misener · reformulation or cutting planes for nonconvex robust problems** (exchange in print: she takes the question from Bertsimas–Dunning–Lubin [ruth-misener card S048 arXiv p. 7]).
- *His*: neither route dominates; run both in parallel [S088 p. 22], a hybrid evaluated from separate single-thread runs assumed not to interfere [S088 p. 20].
- *Theirs*: on 14 pooling instances cutting planes solve more, but "intermediate solutions in the cutting plane algorithm are often not robustly feasible" [ruth-misener card S048 arXiv pp. 15–19]; global solvers lack lazy-constraint callbacks, so the master's tolerance is tightened adaptively [ruth-misener card S048 arXiv p. 7]; ROmodel is set against JuMPeR's tie to Julia [ruth-misener card S057 arXiv pp. 2–3].
- *Contested and test*: the default route when the global solver has no callback. On her 14 instances × 30 radii, run his hybrid as one job with the same cores and time limit as each single route (or charge it both threads' CPU time), with her adaptive-tolerance cutting planes as the cutting-plane arm [ruth-misener card S048 arXiv p. 7]: solved share, median time, and the share of runs holding a robustly feasible incumbent at the time limit [ruth-misener card S048 arXiv p. 19].

**Burer · exact copositive ARO against affine policies** (exchange in print: Xu and Burer's literature positioning lists Bertsimas–Iancu–Parrilo's polynomial policies among existing approximations [samuel-burer card S023 arXiv p. 2]; their bounds are ordered against the affine policy only [samuel-burer card S023 arXiv pp. 11–12]).
- *His*: power and limits of affine policies (2.3); a polynomial hierarchy [S075 p. 9]; a priori geometric bounds he calls "quite close" to a posteriori ones [S192 p. 18], with the distance growing with k (3.21 against 5 at Δ*(9,81)) [S192 p. 19]; sampled lower bounds [S138 pp. 7–9].
- *Theirs*: one copositive program in which the affine policy is a restriction, so richer cones give certified bound orderings [samuel-burer card S023 arXiv pp. 8–12]; with the budget uncertainty set on lot sizing, "We found that, in this case, our method did not perform better than the affine policy." [samuel-burer card S023 arXiv p. 20]; on 971 of 1,000 random instances the bound equals the affine value [samuel-burer card S023 arXiv pp. 20–21].
- *Contested and test*: whether exact conic forms add value beyond affine policies in practice. One instance set: the affine value, his a priori and sampled bounds and Burer's bound; the share of the gap each closes, and time.

**Burer, Dey · robust TSP, moment sets and RPT** (exchanges in print; full meeting points in [02-IO §6](02-IO-integer-mixed-integer.md#minlp-team-minlp-team) and [04-CP §6.2](04-CP-convex-conic-moment.md#62-minlp-team-minlp-team)). Burer's critiques of the budget model on the interval TSP and of moment-based sets, with his side, are in §5 and 6.1 (Ye); Dey and Kocuk build RPT power-cone inequalities on the RPT credited to Zhen–de Moor–den Hertog and Bertsimas et al. [santanu-s-dey card S129 p. 18]; in his own work RPT branch and bound does the exact separation (§3 M1).

**Dey · chance constraints as k-violation MIPs** (conflict; a contrast, no citation on this card; Dey's RPT exchange is above).
- *His*: tractable protection with an a priori violation bound [S001 pp. 4–6; S215 p. 6].
- *Theirs*: sampled chance constraints as covering k-violation MIPs, strengthened by coefficient strengthening and mixing-set cuts [santanu-s-dey card S010 pp. 1–2, 7–14].
- *Contested and test*: a conservative LP against an exact sampled MIP; on their portfolio-type instances, cost, out-of-sample violation and time.

**Sahinidis · certificates for nonconvex robust problems** (conflict; inferred, no dispute documented).
- *His*: a global optimum claimed for annealing runs stopped empirically [S141 pp. 9, 11]; robust local search labelled a heuristic [S090 p. 6]; RPT branch and bound later certifies nonconvex separation [S867 pp. 9–12].
- *Theirs*: no heuristic values called global optima; a general deterministic solver should certify at defaults (nikolaos-v-sahinidis SKILL.md, "Roundtable Card").
- *Test*, where the claim is open: the 2-D example is already mesh-checked [S141 p. 7]. On a reduced cylinder model [S141 pp. 8–11], or on S090's Example III (16 uncertain coefficients, an 18-dimensional perturbation [S090 p. 14]), run robust annealing and have a deterministic global solver bound the worst case at its final design; report the gap to the annealing run's estimated worst case and the time of both.

### 6.3 DFO Team (`dfo-team`)

**Conn, Vicente · bilevel derivative-free robust optimization** (exchange in print: they run his test problem).
- *His*: robust local search needs values and gradients [S090 pp. 2–3]; convergence only for convex costs with an exact oracle [S090 p. 5].
- *Theirs*: min–max as a bilevel problem, both levels derivative-free, lower-level accuracy tied to the upper trust region, run on Bertsimas–Nohadani–Teo's 2-D example [andrew-conn card S066 preprint pp. 5–9, 17; luis-nunes-vicente card S047 preprint pp. 8–9, 16–17]; convergence argued to follow from trust-region DFO theory, assuming a unique lower-level solution and a C1 reduced function, while the implemented algorithm is not analysed [andrew-conn card S066 preprint pp. 2–3, 10]; "An astute reader will notice that there are no comparisons with competing methods — this is because such methods appear not to exist." [andrew-conn card S066 preprint p. 19]
- *Contested and test*: whether derivatives may be assumed; both practical methods run outside their theory (his covers convex f with an exact oracle only [S090 p. 5]; a worst case with several worst errors is nonsmooth, its subdifferential the hull of those errors [S090 pp. 4, 16], outside their C1 assumption). On the 2-D example, or a low-dimensional simulator, gradients given or withheld: simulator calls to a worst case verified on a dense grid within 1%.

**Audet · risk-averse blackbox optimization** (complement; a contrast, no citation either way on the cards).
- *His*: a coherent risk constraint on samples is a robust constraint over a convex set, a polytope for distortion measures such as CVaR [S024 pp. 5, 9]; soft robustness as convex risk measures [S064 pp. 4–5].
- *Theirs*: CVaR objective and constraints for blackboxes, smoothed and solved by multi-timescale zeroth-order approximation [charles-audet card S150 arXiv pp. 6–17], with almost-sure convergence under strict-feasibility and domain-of-attraction assumptions [charles-audet card S150 arXiv p. 16]; for interval (epistemic) data only a worst-case solution, and a worst-case audit that finds a rival's solution infeasible [charles-audet card S150 arXiv pp. 4, 23–24]; Robust-MADS smooths noise with cached evaluations [charles-audet card S055].
- *Contested and test*: CVaR for aleatory noise, with worst cases kept for interval data, against a worst case over a calibrated set; on samples CVaR is itself a worst case [S024 pp. 5–6]. Their almost-sure result under strong assumptions stands against his convex-only theory [S090 p. 5]. One of their engineering benchmarks [charles-audet card S150 arXiv p. 18] with implementation errors at 5,000 evaluations, his arm being robust local search with the test functions' analytic gradients [S090 pp. 2–8]: worst case within Γ, CVaR and Monte Carlo reliability for both answers.

**Powell · annealing as an engine** (contrast at the edge of his scope; inferred, no dispute documented).
- *His*: robust simulated annealing with an asymptotic global claim for runs stopped at an empirical threshold [S141 pp. 5–6, 11], aimed at the global minimum of a nonsmooth worst case that it smooths by a log-sum-exp over bad neighbours [S141 pp. 2–4].
- *Theirs*: no simulated annealing or random search as the default for smooth problems; models from every paid evaluation; the smallest decisive case settles disputes (michael-powell SKILL.md, "Roundtable Card"). His pushback covers smooth problems; nonsmooth objectives and global optimization are on his blind-spot list (same card), and the robust worst case is both.
- *Test*: the 2-D example: robust annealing against a model-based trust-region method on the estimated worst case at equal evaluations, the final worst case certified on a dense grid.

No RO card was found for Scheinberg. Her oracle-contract lens would ask how accurate the worst-case estimate is, and how often; here it comes from gradient ascents at fixed starts plus a history set, so it is deterministic and biased low (late discoveries) [S090 pp. 7, 12], and nonsmooth, global inner problems are on her blind-spot list (katya-scheinberg SKILL.md, "Roundtable Card") [inferred].

## 7. Open problems

**Stated in his papers**
1. Tractable adaptability [S003 p. 43]; adaptive mixed-integer problems lack a cutting-plane-like advance and strong lower bounds [S087 p. 52].
2. When robustness is cheap or expensive [S003 p. 43], partly answered by set-geometry factors [S165 p. 21; S392 pp. 13–23].
3. Affine policies: the gap between O(√m) and O(log m) hardness, and polynomial or piecewise-affine policies [S060 p. 35]; multistage geometric bounds [S192 p. 19].
4. Data: guarantees for more loss functions [S440 p. 21]; estimating a conditional maximum [H007 p. 18]; ML predictions of each parameter's distribution inside the set [H004 p. 22].
5. Nonlinear RO and DRO: per-level guarantees for the RPT hierarchy [S283 p. 15]; compact counterparts beyond binaries and laminar families [S836 p. 17]; decision-rule, SAA and SDP approximations benchmarked against exact DRO values [S867 p. 27].
6. Robust 0–1 complexity under a diagonal covariance [S167 p. 21]; Pareto ARO at scale [S348 p. 22]; choosing among Pareto solutions [S344 p. 20].
7. Robust queueing: multiclass heavy-traffic order and laws tighter than the LIL [S227 pp. 15–16, 26–27]; stability of robust fluid policies [S244 p. 13]; why soft robustness helps out of sample [S064 p. 14].

**Inferred**
- Certified ARO at operator scale: certified gaps appear only at moderate size (affine policies up to N = 100 [S138 p. 9]; partitions at N = 40 [S087 pp. 43, 45]; an exactly verified 14-bus unit commitment at T = 24 [S313 pp. 19–20]); none on the RO cards for a nonconvex worst case at ISO-NE scale, where the inner solver is local [S006 p. 4] (§6.1; Tension T1).
- Set size tied to the owner's decision metric, begun in [S400 p. 2], as a general rule.
- A shared ARO benchmark library with solve times; the one statistical solver benchmark on the RO cards is for static RO [S088 pp. 10–11], and none is for ARO.
- Measured brittleness of affine policies outside the set; the 2025 note runs no experiment [S623 pp. 1–4].
- How Γ arose: unknown.

## 8. Reading path

1. [S001] *The price of robustness*: the budget, the bound ladder, the printed bad case.
2. [S004] Robust discrete optimization: class inheritance by n + 1 nominal solves.
3. [S003] The 2011 survey (arXiv version): the class table and three open problems.
4. [S134] Static robust solutions within 2: the price of a policy class.
5. [S060] Affine policies, power and limits: tight lower bounds against practice.
6. [S042] Affine optimality in one dimension: proof by geometry, fenced by a counterexample.
7. [S006] ARO with ISO New England: partner, knob-matched baseline, run times.
8. [S013] Data-driven sets: hypothesis tests as the knob's source.
9. [S028] Adaptive DRO: lifted ambiguity, the class kept, the policy caution.
10. [S090] Simulation-based RO: robust local search and its convex-only theory.
11. [S088] Reformulation against cutting planes: his matched benchmark.
12. [S392] Coupling (2025): a priori factors computed from the sets alone.

Companion, book material and not a research work: the 2022 book's stated organisation [B011 p. 1].

## 9. Coverage and gaps

- **Read**: 85 distinct primary works in full or in part (the 2007 manuscript S305 merged into S090); 7 distinct at abstract and 10 at metadata level; 12 secondary works read. The signature works are read in full except S060 (in part, as the October 2009 manuscript submitted to Mathematical Programming); S003, S013, S039 and S042 were read as arXiv versions, so journal-version changes are unread.
- **Thin**: the 2022 book's body (abstract card [S084]; only the publisher's page and one review); the 2026 retrospective [S614]; the early adaptive and robustness–regularization working papers [S789; S466; S560; S462; S424]; the unit-commitment closure [S380] and day-ahead pricing [S337]; proofs unread in the partial cards of S065, S082, S087, S117, S165, S176, S227, S268, S283, S348, S836 and S867. Critics' texts (Park, Bienstock–Özbay, Whitt–You) are known through note 05 only. The 17 theses under his profile (Pachamanova 2002 to Koulouras 2025) are unread skip rows; the 2021 interview chapter on RO is unread (note 06 Gaps).
- **Next round**: the open-access retrospective (note 01 §1.8) and the book's preface for how Γ arose and why he entered RO; the closure and Li's discussion of the unit-commitment paper; Pachamanova's and Dunning's theses for process evidence; the Bienstock–Özbay full text; then run the deciding tests of §6, starting with certified ARO gaps (6.1) and the hybrid on pooling, run as one job at equal cores and time limit (6.2).

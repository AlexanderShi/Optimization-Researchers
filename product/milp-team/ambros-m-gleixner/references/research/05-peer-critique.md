# Ambros M. Gleixner: Peer Critique (blind spots, limits, contested judgements)

| Field | Value |
|---|---|
| Researcher | Ambros M. Gleixner. Professor for discrete mathematics and operations research at HTW Berlin since 2020; affiliated researcher at ZIB (division Mathematical Algorithmic Intelligence); head of the ZIB research group Mathematical Optimization Methods 2015–2023; PhD TU Berlin 2015 [S16, S56]. Living. Lens of this file: exact and verified LP/MILP solving (SoPlex LP iterative refinement, exact SCIP, VIPR certificates), MIPLIB 2017, and the SCIP/PaPILO platform papers he co-signs. His MINLP work (OBBT, Undercover, SCIP for MINLP) was screened by citation context only and drew no substantive critique; it belongs to minlp-team |
| Dimension | Research agent 05 of 06: peer critique. Outside objections, rival methods and schools, independent benchmarks of his software, public bug reports and pull requests against it, corrections in the library records he maintains, his own printed concessions, and how each was answered |
| Research date | 2026-11-08 |
| Sources consulted | 60: 34 read at the place cited (P) and 26 secondary (S: citation context, metadata or abstract only). 28 are Gleixner-side (his papers, code, repository and library records, CV, homepage) and 32 are by others. Listed under "Sources" |
| WebSearch calls | 2 (of 5 allowed) |
| User-supplied material | None. `references/sources/{papers,talks,essays,software,publications}/` hold only `.gitkeep`; `private/` was not opened. **Nothing in this file is from user-supplied material** |
| Transcripts saved | None |
| Language | English (team.json) |

**Tags.**
- [stated]: written by Gleixner, or in a paper, report, code comment or GitHub comment he authored or co-signed. Group papers are co-signed and roles are not divided unless said.
- [practice]: what his papers, code, commits, issue threads and library records show was done.
- [observed]: what a third party wrote or reported. Close collaborators (Steffy, Cheung, Pulaj, Koch, Berthold, Ralphs, Shinano, Nordström, Oertel) are not outside critics and are flagged **(insider)**.
- [inferred]: my reading. The basis is given; do not quote it as anyone's view.
- (P) primary reading: the full text, code or thread was read at the location cited. (S) secondary: a Semantic Scholar citation context ("S2 context", the citing sentence as indexed, full text not read), metadata or an abstract.

**Quotation policy.** To respect copyright, passages are paraphrased with pinpoint locations (printed page of journal copies, PDF page of arXiv and ZIB-Report copies, section, GitHub issue, pull request or commit) instead of being quoted at length. Code identifiers, instance names and version strings appear in code spans. No paraphrase is placed inside quotation marks; the wording can be recovered from the locations given.

**How the critiques were found.**
1. Publication landscape from the arXiv API (48 preprints, 2016–2026; the query `au:Gleixner_A` returns an unrelated physicist, so `au:Gleixner_Ambros` was used) and the DBLP record 07/3479 (74 records) [S55].
2. Semantic Scholar citation contexts for 20 of his works, fetched 2026-11-08 and filtered for critical wording: MIPLIB 2017 (347 citing records), LP iterative refinement IJOC 2016 (77), VIPR IPCO 2017 (57), the exact-MIP status update MP 2023 (43), SCIP 9.0 (180), SCIP 8.0 TOMS (93), learning to schedule heuristics (84), ML4CO (65), OBBT (79), Undercover (51), and smaller sets for PaPILO, the limited-precision-oracle paper, the safe GMI cuts, precision boosting, certified presolve and the Chvátal framework [S54]. Lookups for the ISSAC 2012 paper, the GPU-propagation journal paper and the SCIP 8.0 arXiv report returned 404; the symmetry-proof-system lookup hit the rate limit.
3. Read in legal open copies the Gleixner-side texts that critics target (arXiv, ZIB-Reports, Springer open access) [S1–S11, S14, S15].
4. Read the critics in open copies (arXiv, LIPIcs) except items marked (S).
5. Read the public software record: scipopt/vipr (README, CHANGELOG, commit list, all 28 issues and pull requests), the archived ambros-gleixner/VIPR checker at its 2016 commit and at master, seven exact-mode issues in scipopt/scip, the MIPLIB 2017 CHANGELOG and News Log, the CakeML VIPR formalization and the LeanVIPR README [S17–S20, S52, S53].
6. Verified identifiers with Crossref, DataCite (for LIPIcs DOIs), the arXiv API and Unpaywall (email parameter nuwa-skill@users.noreply.github.com).
7. Not reached, and not routed around: OpenReview (bot challenge; the NeurIPS 2021 reviews of the heuristic-scheduling paper), AAAI's OJS (Anubis proof-of-work check; Sidorov et al. 2024), the OAKTrust copy of Escobedo et al. 2018 (returned an HTML page, not the PDF), the MIPLIB 2024 submission portal (no connection). The closed INFORMS text of the 2016 iterative-refinement paper was not read.

**Attribution caveats that must survive into the skill.**
- **Almost everything criticized here is group work.** The 2021–2025 exact-MIP and exact-LP papers have Leon Eifler as first author; PaPILO was created by Leona Gottwald [S2 PDF p. 14] and is now maintained largely by Alexander Hoen, who also made most of the 2024–2026 VIPR commits; certified propagation is first-authored by Sander Borst [S1, S4, S10, S17, S19, S57]. Eifler's TU Berlin dissertation (2025) had Koch as advisor and Gleixner as one of four referees (per research note 01). A critique of exact SCIP targets the group's code and Gleixner's research agenda, not necessarily his own lines of code.
- **Where his own hands are visible:** the VIPR repository was created under his account on 2016-11-20 (first code commit by co-author Dan Steffy, account `desteffy`) [S18]; he authored checker commits in 2023 (assumption handling in unsplitting, 2023-04-04) and in 2025 (early termination once the claim is proved, the tautology check restricted to ranges, canonicalization on failed comparisons), and pull request #25 in October 2026 [S17, S18]; he is first author of MIPLIB 2017 [S14] and of the 2016 and 2020 iterative-refinement papers with Steffy and Wolter [S11, S12].
- **Co-responsibility for the 2017 checker** lies with Cheung, Gleixner and Steffy jointly [S3, S18].

---

## 0. Summary for Phase 2

| # | Recurring critique (blind spot / limit) | Raised by | Gleixner-side answer | Status |
|---|---|---|---|---|
| Q1 | **Price of exactness and missing features.** Exact IP solving stays far from the efficiency of default floating-point solvers; the proof-producing SCIP lacks many standard features | Ihalainen et al. 2025 [S31]; Jabs-Berg-Järvisalo 2025 [S33] (S); Halbig-Oertel-Weninger 2024 [S34]; Flippo et al. 2026 [S30]; Ihalainen et al. 2026 [S32] (S) | Conceded in print with numbers: 8.1x slower than default and 3.9x slower than a feature-reduced floating-point SCIP (MP 2023); about 10x and 3–4x (SCIP 10, 2025). Gaps filled paper by paper (safe GMI cuts, certified propagation, exact presolve) [S1, S2, S4, S8] | Open; gap narrowed. Symmetry handling still missing in 2026 (#205) [S19] |
| Q2 | **What VIPR can certify.** No presolve, no dual reductions, no symmetry; a MIP-specific design; certificates tied to one solver and large | Own group [S5, S6, S8, S9]; PB proof-logging school: Demirović et al. 2024, Koops et al. 2025, Dold et al. 2026 [S27–S29]; Szeider 2026 [S25]; Sidorov et al. 2024 [S26] (S) | Imports the rival's tool for presolve (VeriPB, with Nordström) for 0-1 programs with integer data; proposes a symmetry-capable proof system [S5, S6, S8] | Partly answered; general-MIP presolve still uncertified in SCIP 10 [S8] |
| Q3 | **The checker is the trusted base, and it was unsound in places.** Forged certificates accepted; informal specification; latent soundness bugs from 2016 to 2026 | Wood et al. 2023/2026 [S24] (insider-adjacent: Pulaj); GitHub users `basedpolymer` and `cruisesong7` with LeanVIPR, Oct 2026 [S17, S52]; group member Hoen, 2024 [S17] | In code: fast and collaborative (thanks the contributor, writes PR #25 within a day, asks for review). In print: no reply to Wood et al. found. Formally verified checkers exist outside the group; SCIP 10 points users to the CakeML one [S8, S53] | Fixes pending: PRs #24, #25, #28 and issues #26, #27 open on 2026-11-08 [S17] |
| Q4 | **Wrong answers from exact mode; exact only within an input range** | GitHub reporters: #151 (2025), #238, #261, #248 (Oct 2026) [S19] | Diagnosed within a day, fixed in PaPILO within two weeks; Gleixner explains the hybrid-precision input limit (values beyond 1e20 treated as infinite) and adds warnings [S19] | Reported cases fixed. [inferred] Both wrong-answer bugs sat in presolve, the stage certificates do not cover |
| Q5 | **LP iterative refinement:** relies on an absolute-error assumption, cannot recover reliably when the floating-point LP fails, needed slow parameter-restart recovery; exact SoPlex buggy or slow in outside benchmarks | Escobedo-Moreno-Centeno-Lourenco 2018 [S35] (S); Casablanca et al. 2026 [S38]; Hartmanns et al. 2023 [S36]; Chen-Cheung et al. 2019 [S37] (insider) | Own 2025 paper concedes the recovery problem, disables the restart recovery, adds precision boosting, and drops the 2016 rational reconstruction for basis factorization on average [S10]; 2020 theory states the absolute-error assumption [S11] | Conceded and revised. No printed reply to Escobedo et al. found |
| Q6 | **MIPLIB 2017:** manual choices, selection by current solver performance, missed numerics, tuning on the library, unsuitable for ML, ageing | Own paper [S14]; Koch-Berthold-Pedersen-Vanaret 2022 (insiders) [S39]; D-MIPLIB 2024 [S41] and four ML papers [S42–S45] (S); Robinson La Rocca et al. 2025 [S46] (S) | Hard-instance weighting; public changelog; benchmark set v2 (June 2019); `numerics` tag [S14, S20] | No outside critique of the selection method found; ML critique is about fitness for another purpose, unanswered for MIPLIB itself |
| Q7 | **Platform performance** of SCIP, SoPlex, PaPILO | Users [S50, S51] (S); Hartmanns et al. [S36]; Dai and Chen [S48] (S) | None found | Context only; group products |
| Q8 | **Distribution-specific learning versus a general-purpose library** | ML4CO's own framing (co-signed) [S15]; Li et al. 2024 [S47] (S) | Not applicable | Tension, kept as C5 |
| Q9 | **Predictions and plans** (2017 certificate overhead; proof-assistant checking; the 2021 vision; the MIPLIB hindsight study) | Outcomes in [S2, S8, S24, S52, S53] | n/a | Mixed (§10) |
| Q10 | **Relay errors and reporting slips** | Found in this run [S1, S8, S31, S34] | n/a | No critic raised them (§11) |

**Where the critiques land in the seven layers (framework §一)** [inferred grouping]

| Layer | What the critiques bear on | Items |
|---|---|---|
| 1 Taste (what counts as a trustworthy result) | Exact arithmetic plus a certificate, versus a verified checker and coverage of the whole pipeline including presolve | Q2, Q3, C1, C3 |
| 2 Problem choice | Exactness as an agenda (mathematical proofs, verification); MIPLIB as community service whose selection used current solvers | Q1, Q6, C4 |
| 3 Idea generation | Hybrid precision (floating point first, exact repair and checks); importing rival tools (precision boosting, VeriPB) | Q5, §12 |
| 4 Experiments | Feature-reduced floating-point baselines versus default baselines; small curated test sets (fpeasy, numdiff); seeds only in the SCIP 10 study; certificate-size caps | Q1, C2, C6 |
| 5 Judging results | Certificate cost judged acceptable; floating-point decisions judged overwhelmingly correct; benchmark suitability revised after numerics surfaced | C1, C2, Q6 |
| 6 Expression | Limits stated in conclusions and future-work lists; occasional numeric inconsistency | §11 |
| 7 Organization | Student-led implementation; public repositories; vendor representatives on the MIPLIB committee; response speed on GitHub | Q3, Q4, §12 |

---

## 1. Era and resource context

| Period | Practice under critique | Resources and setting |
|---|---|---|
| 2008–2016 | LP iterative refinement in SoPlex with Steffy and Wolter (ISSAC 2012, IJOC 2016) [S12, S13] | ZIB research assistant; all simplex solves in double precision, symbolic (GMP) computation only to recover and check exact solutions; in-house SoPlex [S2 PDF p. 9, S10 PDF p. 5, S16] |
| 2015–2023 | Group head, Mathematical Optimization Methods, ZIB | In 2017 the group had 2 senior researchers, 10 research assistants and 4 student assistants [S16]; Research Campus MODAL funding (BMBF 05M14ZAM, 05M20ZBM) [S2 PDF p. 3, S10 PDF p. 1] |
| 2016–2017 | VIPR certificates (with Cheung, Carleton, and Steffy, Oakland) | Certificates written to files with a 10 GB cap and a 1 h time limit on 107 instances curated by Cook et al. [S3 PDF pp. 9–10] |
| 2016–2019 | MIPLIB 2017 lead | Committee of 21, including representatives of nine solver development teams; 5,721 submitted instances; performance data from eight solvers [S14 pp. 443–445] |
| 2019–2023 | Revised exact SCIP (with Eifler) | Intel Xeon E5-2660 cluster, 128 GB; CPLEX as the floating-point LP solver inside the exact code (12.3.0 for the old framework, 12.8.0 for the new) [S2 PDF p. 9] |
| 2020– | HTW Berlin professorship; exact mode integrated into SCIP 10.0 (Nov 2025) | Exact mode tested on the MIPLIB 2017 benchmark set with three seeds and a 2 h limit [S8 p. 11] |
| 2022–2026 | Rise of formally verified proof checking (CakeML VIPR formalization from 2022-12-18; PB proof logging; LeanVIPR, Oct 2026) | In October 2026 a burst of differential testing and bug reports hit VIPR and exact SCIP; the text of PR #24 carries a footer saying it was generated with an AI coding tool [S17, S19, S52, S53] |

---

## 2. Exact rational MIP: the price of exactness and missing features (Q1)

### 2.1 What critics said [observed]
- **Ihalainen, Vandesande, Schidler, Berg, Bogaerts, Järvisalo** (accepted at AAAI 2026; arXiv 2508.07015v2) [S31] (P): numerically exact IP solvers exist, but their performance is still far from that of default floating-point solvers (PDF p. 2); they relay the factor 8.1 from Eifler and Gleixner as the reported slowdown (PDF p. 6). Their own result: exact hitting-set computation by pseudo-Boolean reasoning can be made competitive with a numerically exact IP solver, while a commercial IP solver stays fastest but can return numerically wrong answers (abstract, PDF p. 1). A rival method matches exact SCIP in that application.
- **Jabs, Berg, Järvisalo** (JELIA 2025) [S33] (S, S2 context): proof-logging overhead in their multi-objective PB optimizers is small, especially next to the large overheads reported for numerically exact ILP solvers.
- **Halbig, Oertel, Weninger** (arXiv 2410.22147, 2024) [S34] (P): list the components missing in their exact decomposition-branching code and relay that exact SCIP is about 8.1 times slower than floating-point SCIP. They also used a pre-release exact SCIP for their subproblems: users as well as critics.
- **Flippo, Sidorov, ten Brink, Pit-Claudel, Demirović** (CP 2026, LIPIcs 379, p. 24:3) [S30] (P): proof logging for MIP is possible from a modified SCIP with a proof-producing mode, but that mode lacks many features of standard SCIP, above all its presolving heuristics (their wording pairs the two words; read here as presolve techniques). See §11 R4 for how far this is accurate.
- **Ihalainen, Vandesande, Schidler, Berg, Järvisalo** (HitPBO, SAT 2026) [S32] (S, S2 context): exact SCIP can serve as an exact optimizer to increase trust, but it does not emit proofs in the VeriPB format: an interoperability gap with the PB proof-logging ecosystem.

### 2.2 What the Gleixner side said and did [stated / practice, P]
- **2021 (IPCO, with Eifler; ZIB-Report 21-04)** [S2]: the motivating claim is that floating-point MIP solvers can claim optimality for suboptimal assignments or even infeasibility wrongly, which weakens MIP-based mathematical results (PDF pp. 3–4). On the MIPLIB 2017 benchmark set the revised framework solves 47 of 240 instances against 17 for the original Cook-Koch-Steffy-Wolter framework [S21] (Table 8, PDF p. 14). The authors then concede that the gap to floating-point solvers remains large, because safe cutting planes are still missing (PDF p. 14).
- **Confound conceded:** two different CPLEX versions served as the floating-point LP oracle for the old and the new framework, which they judge to have limited impact because most time is spent in safe dual bounding (PDF p. 9) [stated].
- **2023 (Math. Program. 197, journal version)** [S1]: against floating-point SCIP 7.0.1, exact SCIP is 8.1 times slower than default and 3.9 times slower than a reduced variant without cuts, propagation, conflict analysis and symmetry handling, on the 42 MIPLIB 2017 instances all three solve (p. 809). Of 137 instances solved by at least one variant, default solves 133, reduced 62 and exact 45 (Table 11, p. 810); the authors read the solvability gap as mostly due to missing methods (p. 809). Instances feasible within tolerances but infeasible in exact arithmetic were discarded before the comparison (p. 809). On the numerically difficult set the slowdown against the reduced variant is 5.1 (p. 809).
- **2025 (SCIP Optimization Suite 10.0, co-signed, 34 authors)** [S8]: exact mode is restricted to MILP (p. 7). On the MIPLIB 2017 benchmark set with three seeds, exact solves 161, reduced floating point 235 and default 342 instance-seed runs; the authors summarize the price of exactness as a factor of 3 to 4 like-for-like and about 10 against default, varying strongly by instance (p. 11).
- **2026:** a user reports that symmetry detection is skipped in exact mode; co-developer Hojny calls it an important missing feature that needs a rewiring of SCIP's symmetry code (#205, 2026-06-19) [S19] [practice].

### 2.3 How it was answered
- **By construction, not by rebuttal** [practice]: safe Gomory mixed-integer cuts (SIOPT 2024) [S4], certified propagation and dual proof analysis (arXiv 2403.13567) [S57], exact presolve through PaPILO, and integration of all of it into SCIP 10 [S8]. No printed reply to the outside remarks was found; the outside remarks mostly relay the group's own numbers.
- [inferred] The two sides use different baselines: critics compare with default floating-point solvers; the group reports both but frames progress against the feature-reduced baseline (3.9x, 3–4x). Both readings are in the group's own tables.

---

## 3. What VIPR certificates cover, and the rival proof-logging school (Q2)

### 3.1 The group's own concessions [stated, P]
- **IPCO 2017 (Cheung, Gleixner, Steffy)** [S3]: the abstract concedes that, given how complex MIP solvers are, the ideal form of a certificate is not clear; the chosen format is a list of statements checkable one by one with few inference rules, designed for simplicity (PDF p. 3).
- **Presolve is outside the certificate.** In 2021, certificate printing required presolve to be switched off because PaPILO could not emit certificates (ZIB-Report 21-04 PDF p. 13) [S2]; the 2024 GMI-cut paper still verifies only that the presolved problem was solved correctly (arXiv 2303.12365 PDF p. 25) [S4]; SCIP 9.0 prints the certificate for the presolved problem only, because VIPR lacks the functionality for presolve (S2 context) [S9] (S); SCIP 10.0 does the same and checks the original problem's primal bound by the feasibility of the final solution (p. 11) [S8].
- **van Doornmalen, Eifler, Gleixner, Hojny** (arXiv 2311.03877, PDF p. 2) [S5]: no formal proof system for MIP exists, and what VIPR can certify is severely limited: nothing that removes parts of the feasible region, such as symmetry reasoning.
- **Hoen, Oertel, Gleixner, Nordström** (CPAIOR 2024; arXiv 2401.09277 PDF p. 2) [S6]: VIPR verifies only reasoning that keeps all feasible solutions, so dual presolve reductions cannot be checked and a branch-and-cut certificate holds only on the assumption that presolve was correct; SAT preprocessing proofs do not help because they reason about clauses only.

### 3.2 The rival school and competing certificate routes [observed]
- **Koops, Le Berre, Myreen, Nordström, Oertel, Tan, Vinyals** (CP 2025, LIPIcs 340, pp. 21:2–21:3) [S28] (P): proof-logging attempts outside SAT, MIP among them (citing Cheung et al. 2017 and Eifler and Gleixner), ran into the difficulty that simple proof systems cannot cover the full range of solver reasoning, while special rules per technique make checking complex. Their alternative is pseudo-Boolean proof logging. Nordström and Oertel are Gleixner co-authors (insider-adjacent).
- **Dold, Katsirelos, Koops, Myreen, Nordström, Oertel, Tan** (CP 2026, LIPIcs 379, pp. 21:2–21:3) [S29] (P): proof logging in MIP (citing the same two works) and in other fields has had much more limited success than in SAT: approaches struggle to cover all techniques, add special rules, or sometimes require trusting the solver.
- **Demirović, McCreesh, McIlree, Nordström, Oertel, Sidorov** (CP 2024, LIPIcs 307, p. 9:2) [S27] (P): a design contrast. VIPR is MIP-specific, with explicit assumptions and branch-closing rules that act independently of other rules; their PB system has no direct notion of search but can express implicational reasoning, so that techniques such as restarts can be encoded without extending the proof system.
- **Sidorov, de Almeida Correia, de Weerdt, Demirović** (AAAI 2024) [S26] (S, S2 contexts): treat Cheung-Gleixner-Steffy as the state-of-the-art certified MIP approach and compare their certificate sizes against it for constrained shortest paths. The numbers were not read (bot check).
- **Szeider** (CP 2026, LIPIcs 379, pp. 52:1–52:2) [S25] (P): before his paper, no solver-independent way to generate VIPR certificates existed; SCIP's exact mode ties certificates to one solver, depends on exact LP solvers, and yields certificates whose size mirrors its own search. His black-box route, built on the limited-precision LP oracle of Gleixner and Steffy, gives much more compact certificates on generated benchmarks; on MIPLIB each approach solves instances the other cannot, so he calls them complementary.
- **Pulaj and Wood** (Exp. Math. 2024) [S49] (S, S2 context; insider: Pulaj co-authored the 2022 Chvátal paper with Gleixner [S59]): unlike their earlier work, which verified results with exact IP, they now verify with an SMT solver.

### 3.3 How it was answered
- [practice] Gleixner moved toward the rival school instead of defending VIPR as sufficient: PB-based conflict analysis with Nordström (CP 2023) [S58] and VeriPB-certified presolve for 0-1 programs (CPAIOR 2024) [S6]; a symmetry-capable proof system with Hojny and others (2023) [S5]. SCIP 10 certifies presolve separately only for binary programs with integer data (p. 7) [S8].
- [inferred] The answer accepts the critics' premise (a richer proof system is needed) while keeping VIPR as the format exact SCIP writes for branch-and-cut.

---

## 4. The checker as the trusted base: forged certificates and latent soundness bugs (Q3)

### 4.1 Wood, Zhou, Wu, Mendes, Pulaj (2023; J. Symbolic Comput. 2026) [observed, P]
arXiv 2312.10420 v1 (2023-12-16) to v4 (2025-10-12); J. Symbolic Comput. 135 (2026) 102543 [S24]. Pulaj is a Gleixner co-author [S59] (insider-adjacent).
- The reference checker `viprchk` has no formal argument for its correctness; parts of the VIPR specification are informal or missing; the checker relies on expected solver behaviour in places; and its use of the certificate's index attribute (for memory management) makes it trust the solver at the expense of soundness (PDF p. 3; details PDF p. 15).
- Example 4 (PDF p. 15): for maximizing x1 + x2 over two binary variables (optimum 2), a certificate that claims optimum 1 from a solution-based cutoff is reported valid by `viprchk`. Example 5: for an infeasible problem and a certificate without solutions, `viprchk` still prints a success message about solution feasibility.
- They concede that an established solver is unlikely to produce such certificates, but the specification allows them (PDF p. 3).
- Their answer: a ground-formula encoding of VIPR validity, verified in Why3 and checked with SMT, independent of the solver.

### 4.2 What the code record shows [practice, P]
- **Solution feasibility, 2016–2024/2026.** In the 2016 checker (ambros-gleixner/VIPR, commit `f5831734c0`, 2016-11-23) each claimed solution is tested m times against the constraint whose index equals the solution's counter (`constraint[i]` inside the loop over `j`), so primal witnesses were not properly checked [S18]. Hoen fixed this in `viprchk` with PR #5 (opened 2024-11-29, merged 2024-12-04; VIPR 1.1 release notes); the identical bug survived in `viprchk_parallel` until issue #27 (2026-10-28) [S17].
- **Rounding over continuous variables, 2016–2026.** The 2016 `Constraint::round()` checks integrality only of coefficients on integer variables, so a rounding step that involves a continuous variable passes [S18]. PR #24 (2026-10-27) shows certificates that thereby prove feasible problems infeasible, and a comment on PR #25 shows one that proves a wrong optimal value [S17].
- **Solution-based cutoff for maximization.** The archived checker (ambros-gleixner/VIPR master, around line 1023) and scipopt/vipr master `99eec19` (2026-10-24) accept a solution-based cutoff only with sense ≤; for maximization this lets any feasible solution be certified as optimal (issue #26, 2026-10-28, found by differential testing against LeanVIPR) [S17, S18]. The 2016 checker had no solution-based cutoff rule at all [S18]. [inferred] This is the flaw Wood et al.'s Example 4 had shown 34 months earlier.
- **Other holes** reported in October 2026: index bounds checked only in debug builds; non-canonical and zero-denominator rationals; `viprchk_parallel` exiting with success status after a failed final check; assumptions of the second branch dropped in `uns` (#24, #27, #28) [S17].
- **The completion tool.** The VIPR 1.2 release notes (2025) record that `viprcomp` now stops with an error instead of writing an invalid certificate when a derivation cannot be completed [S17].
- **The group's own use of certificates as a debugging tool:** in 2021 a certificate exposed incorrect root-node infeasibility reasoning in the original framework of Cook et al., although the instance was indeed infeasible (ZIB-Report 21-04 PDF p. 13) [S2]. The 2017 paper had noted that even exact solvers can have implementation errors, the motivation for certificates (PDF p. 3) [S3].

### 4.3 How it was answered
- **In code, fast and collaborative** [stated / practice, P]: on PR #24 Gleixner thanked the contributor and announced a small revision for review before merging (2026-10-28); his PR #25 (commit `b0e56a5`, same day) adds minor revisions and asks the contributor to double-check; the contributor confirmed it and stacked further fixes as PR #28 [S17]. All five items are open on 2026-11-08 [S17].
- **Self-initiated hardening before the reports:** Gleixner's 2023 and 2025 checker commits (see the attribution caveats) and Hoen's 2024 fixes [S17, S18].
- **In print, silence:** no reply to Wood et al. was found; Semantic Scholar lists only Szeider 2026 as citing them, and Szeider notes that their encoding exposed ambiguities in the specification [S54] (S).
- **The trust base moved outside the group:** the SCIP 10 report (co-signed) points to a checker formally verified in HOL4 through CakeML as the more rigorous option (p. 11) [S8]; that formalization began in the CakeML repository on 2022-12-18 (account `tanyongkiam`) [S53]. LeanVIPR (Lean 4; repository created 2026-10-28) claims a checker proved sound and complete against a declarative rendering of VIPR and treats exact SCIP as untrusted [S52] (P, README).
- [inferred] For Phase 2: a certificate is only as strong as its checker and its specification. The 2017 framing (simple format, independent check) held for the format; for the reference implementation it did not hold for years, and outsiders with formal tools found the gaps.

---

## 5. Wrong answers from exact mode, and its input limits (Q4) [practice, P]

| Issue (scipopt/scip) | Report | Diagnosis and response |
|---|---|---|
| #151 (2025-06-03 to 2025-08-29) | Exact mode declares a trivially feasible integer program infeasible when an objective coefficient is near 1e20 | Gleixner: exactness is limited by the hybrid design, which keeps a floating-point copy of the problem; values beyond 1e20 count as infinite and the threshold changes only at compile time; recommends rescaling. Kamp notes the presolve fix is not yet effective. Closed by Gleixner after warnings were added for discarded solutions beyond the threshold [S19] |
| #238 (2026-10-21 to 2026-10-31) | Exact mode returns a non-integer solution as optimal for an integer-infeasible model (a parity argument) | Hoen: PaPILO's substitution presolver ignored the right-hand side; fixed in PaPILO [S19] |
| #261 (2026-10-29 to 2026-11-04) | Exact mode declares a feasible model derived from MIPLIB `rocI-3-11` infeasible; the reporter supplies an exactly checked witness | Hoen: PaPILO probing swapped two variables without inverting their relation; fixed [S19] |
| #248 (opened 2026-10-26) | Certificates from SCIP 10.1.0 fail `viprchk` after `viprcomp` completion | Gleixner asks whether the latest VIPR was used; with VIPR `99eec19` the reporter's certificates verify [S19] |
| #79 (2023-12-25 to 2025-05-26) | Many exact-branch tests fail on a user's machine | Not reproduced by Eifler; Gleixner closes it after asking for a retry with current versions [S19] |

- [inferred] Both wrong-answer bugs (#238, #261) sat in exact presolve, the stage the VIPR certificates do not cover (§3.1); the group's own papers list presolve certification as open work [S1 p. 810, S8 p. 11]. The 2026 reports show what that gap costs.
- [inferred] The 1e20 input range is a limit of applicability not stated in the passages of [S1, S2, S8] read here; it surfaced in a user thread.

---

## 6. LP iterative refinement: assumptions, recovery, rival exact-LP methods (Q5)

### 6.1 What critics said [observed]
- **Escobedo, Moreno-Centeno, Lourenco** (ACM TOMS 44, 2018) [S35] (S, S2 context): because iterative refinement relies on fixed-precision simplex runs, it remains exposed to roundoff and may need a series of parameter changes before it succeeds on numerically hard instances. They represent a rival school (roundoff-error-free LU factorizations).
- **Casablanca, Sidaway, Soudjani, Zuliani** (arXiv 2609.11721v3, 2026-10-29; unreviewed) [S38] (P): iterative refinement in SoPlex is usually faster but may fail to recover under severe ill-conditioning, near-singular bases or large growth (PDF p. 2). On Sloane–Stufken LPs their precision-boosting solver solves most instances faster than SoPlex 8.0.3, whose pure-boosting mode improves on its hybrid default without changing the outcome, and they concede that iterative refinement can be the better choice elsewhere (PDF p. 16); their performance profiles show more instances solved than SoPlex in both modes (Fig. 2, PDF p. 21). They thank Gleixner for help with SoPlex (PDF p. 17).
- **Hartmanns, Junges, Quatmann, Weininger** (TACAS 2023; arXiv 2301.10197) [S36] (P): in MDP model checking, exact SoPlex 6.0.1 competes with some floating-point solvers (PDF p. 12), but 98 of the 112 instances it failed on were errors likely caused by a confirmed bug in that version (PDF p. 16); floating-point SoPlex was among the solvers producing more errors than value iteration (PDF p. 12).
- **Chen, Cheung, Kielstra, Winn** (arXiv 1908.10989, 2019; insider: Cheung is a VIPR co-author) [S37] (P): exact LP solvers such as QSopt_ex and rational SoPlex exist but are much slower than inexact ones (PDF pp. 6–7).

### 6.2 What the Gleixner side said and did [stated, P]
- **Gleixner and Steffy** (Math. Program. 183, 2020; arXiv 1912.12820 §2) [S11]: the convergence theory needs only that the LP oracle returns solutions whose absolute violations stay below a constant smaller than one. [inferred] That is the assumption the rival school questions, since floating-point accuracy is relative; the 2020 paper cites Escobedo and Moreno-Centeno as related work on roundoff-error-free factorizations, not as critics.
- **Eifler, Nicolas-Thouvenin, Gleixner** (INFORMS J. Comput. 37, 2025; arXiv 2311.08037) [S10]: iterative refinement has no reliable recovery when the floating-point LP fails, observed on pure LPs and inside exact MIP (PDF p. 2); if the oracle returns residuals near or above one, convergence is not guaranteed (PDF pp. 5–6); the original recovery by restarting with changed presolving, scaling and tolerances can be very slow and is disabled in favour of precision boosting (PDF p. 6); and basis factorization clearly beat the 2016 rational reconstruction on average, though not on every instance (PDF p. 10).
- **Math. Program. 2023** (p. 810) [S1] had already named precision boosting as the fix for ill-conditioned LP relaxations.

### 6.3 How it was answered
- By revision: SoPlex 6.0 combines precision boosting with iterative refinement (SCIP 9.0 report, S2 context) [S9] (S); the 2016 recovery mechanism and rational reconstruction were abandoned as defaults [S10]. No printed reply to Escobedo et al. specifically was found.

---

## 7. MIPLIB 2017: selection, numerics, tuning and fitness for ML (Q6)

### 7.1 The paper's own limits [stated, P] (16 authors, Gleixner first) [S14]
- Despite the quantitative method, many manual decisions and heuristic choices remain (p. 445).
- Selecting by current solver performance may favour instances that current solvers already handle; the authors counter with objective weights that favour instances hard even for the virtual best solver, the square root being chosen empirically (p. 478).
- Representing computational difficulty cannot be achieved perfectly and is not even well defined: the data are a snapshot of current solvers under a time limit, without performance variability or parallel scaling, with correctness only up to tolerance, and the performance clusterings may conflict (p. 478).
- The final sets are one of many justifiable outcomes, and the method is not meant as a general blueprint (p. 485).
- The solution checker verifies feasibility within tolerances and cannot check optimality (p. 464).
- The committee of 21 included representatives of nine solver development teams (p. 444). [inferred] Vendor participation in a benchmark that vendors are judged on is a possible conflict-of-interest point; no critic was found raising it.

### 7.2 Judgements shown wrong, and the corrections [practice, P]
- Two benchmark instances, `neos-5075914-elvire` and `neos-3754224-navua`, had numerical problems that the selection missed: for the first, two solvers agreed on an optimal value although the instance should be infeasible; for the second, declared infeasible by one solver, a solution feasible within tolerances arrived half a year after publication (p. 485, footnote 8). Benchmark set version 2 (June 2019) exchanged five instances and tagged the two with `numerics` (p. 486) [S14, S20].
- The MIPLIB changelog and news log record later reversals: `navua` reopened (2019); `supportcase22` moved from infeasible to feasible (July 2023) and was corrected from hard to open (July 2024); four instances returned to status open with improved objective values (October 2020) [S20]. [inferred] Whatever the earlier labels were (not checked), these are public retractions recorded by the maintainers.
- 193 collection instances carry the `numerics` tag, partly because solvers disagreed during compilation (Hoen and Gleixner 2025, PDF p. 2) [S7].

### 7.3 Critiques by others [observed]
- **Koch, Berthold, Pedersen, Vanaret** (EURO J. Comput. Optim. 10, 2022; arXiv 2206.09787; insiders, Koch and Berthold are MIPLIB 2017 co-authors) [S39] (P): heavy tuning on MIPLIB 2010 and 2017 helps newer solvers and may overstate measured progress (PDF p. 15); collections drift toward hard instances and under-represent modelling practice that current solvers cannot handle (PDF p. 5).
- **Maher, Ralphs, Shinano** (arXiv 2104.10025, 2021; insiders) [S40] (P): praise the MIPLIB 2017 selection as a good example of systematic methods for representativeness (PDF p. 17).
- **ML authors, on fitness for learning:** Huang, Huang, Ferber, Dilkina (Distributional MIPLIB, arXiv 2406.06954v2) [S41] (P): the heterogeneity that suits solver benchmarking makes MIPLIB less suited to ML, which needs many instances from one distribution, and ML methods struggle to reach the state of the art on it (PDF pp. 1, 3). Similar remarks, all S2 contexts (S): Wu, Song, Cao, Zhang (NeurIPS 2021) [S42]; Qian and Morris (NeurIPS 2025, which says the same of QPLIB, another library Gleixner co-authored [S60]) [S43]; Cai, Huang, Dilkina (ECAI 2024), who avoided MIPLIB for training [S44]; Maudet and Danoy (ECAI 2025), who call ML results on heterogeneous benchmarks such as MIPLIB 2017 often mixed [S45].
- **Ageing:** Robinson La Rocca, Cordeau, Frejinger (arXiv 2501.10778, 2025) [S46] (S, S2 context): most of the 1,065 instances are solved to near-optimality within 10 minutes by the state-of-the-art commercial solver.

### 7.4 How it was answered
- The paper itself proposes, as future work, a hindsight study of how well the benchmark set represents progress (p. 485). Not found (Gaps).
- The ML critique addresses a purpose MIPLIB was not designed for; no MIPLIB-side reply was found. ML4CO, which Gleixner co-signed, used distributional datasets instead (§9).
- A MIPLIB 2024 call for submissions ran in 2024; the MIPLIB site removed its advertisement header in March 2025 [S20]; no release was found by 2026-11-08 (Gaps).
- No published outside critique of the selection method itself was found, after screening the S2 contexts of 347 citing works and one WebSearch.

---

## 8. Platform-level observations: SCIP, SoPlex, PaPILO (Q7) [observed]
- **Rodriguez-Flores et al.** (Bioinformatics 40, 2024) [S50] (S, S2 context): on the E. coli core model their gMCS computation took 5571 s on average with SCIP against 1 s with commercial solvers.
- **Skipper et al.** (Election Law Journal, 2025) [S51] (S, S2 context): SCIP solved all their instances and has a generous licence, but HiGHS outperforms SCIP on some classes of integer models.
- **Dai and Chen** (Math. Program. Comput., 2026) [S48] (S, S2 context): for two-column probing they chose a design different from PaPILO's parallel scheme [S23], whose communication cost might be prohibitive in that setting.
- **Hartmanns et al.** [S36]: floating-point SoPlex error-prone on MDP LPs (§6.1).
- [inferred] These observations concern group products; Gleixner's share is not separable.

---

## 9. Distribution-specific learning versus a general-purpose library (Q8)
- **ML4CO** (Gasse et al., arXiv 2203.02433, 41 authors including Gleixner) [S15] [stated, P, co-signed]: the abstract says combinatorial optimization has traditionally solved instances in isolation, ignoring that practical instances come from related distributions (PDF p. 2); the competition used three distributional datasets.
- **Li, Kulkarni, Menache, Wu, Li** (arXiv 2410.08288, 2024) [S47] (S, S2 context): most ML-for-MILP methods, ML4CO among those cited, target specific problem classes and struggle to generalize to unseen types; they test transfer on MIPLIB.
- [inferred] Each of the two designs Gleixner co-signed is cited by critics of the other (C5).

---

## 10. Predictions and plans, and how they fared (Q9)

| Prediction or plan | Where | Outcome |
|---|---|---|
| Code changes would bring certificate-producing runs close to plain exact SCIP | VIPR 2017, PDF p. 10 [S3] | In 2021, certificates still added 101.2% solving time on fpeasy and 51.4% on numdiff, which the authors say confirms the 2017 measurements (ZIB-Report 21-04 PDF p. 13) [S2]. Not borne out by 2021; later figures not found |
| Convert certificates for checking in a proof assistant such as HOL Light | VIPR 2017, PDF p. 10 [S3] | Done by others: CakeML/HOL4 (from 2022), Why3 and SMT (Wood et al. 2023), Lean 4 (LeanVIPR 2026) [S24, S52, S53] |
| Rigorous yet fast MIP is not fundamentally out of reach | ZIB-Report 21-04 PDF p. 5 [S2] | By 2025 about 10x slower than default and 3–4x like-for-like [S8]. Partly borne out |
| Presolve must emit certificate information for start-to-finish verification | MP 2023, p. 810 [S1] | Done for 0-1 programs with integer data via VeriPB (2024) [S6]; general MIP presolve still uncertified in SCIP 10 [S8]; the 2026 wrong-answer bugs sat there (§5) |
| A hindsight study of the benchmark set's representativeness | MIPLIB 2017, p. 485 [S14] | Not found |
| Many more MIPLIB versions to come | MIPLIB 2017, p. 486 [S14] | MIPLIB 2024 call in 2024; no release found by 2026-11-08 |

---

## 11. Relay errors and reporting slips found in this run [inferred; no critic raised them]
- **R1.** Math. Program. 197 (2023) p. 809 says the reduced variant solved 61 instances fewer than default, but Table 11 (p. 810) gives 133 against 62, a difference of 71; the companion figure (exact solving 17 fewer than reduced: 62 against 45) matches the table. Checked with two independent text extractions of the open-access PDF [S1].
- **R2.** The SCIP 10.0 report's reference [69] gives the CakeML VIPR formalization's authors as Y. Kiam and M. Myreen [S8]; the CakeML history shows the work begun by the account `tanyongkiam` (display name Yong Kiam) on 2022-12-18, and the CP 2025 and CP 2026 author records list Yong Kiam Tan [S28, S29, S53]. Probably a given-name/surname slip.
- **R3.** The relays of the factor 8.1 [S31, S34] drop its qualifiers: 42 MIPLIB 2017 instances solved by all three variants, against SCIP 7.0.1 default. The same paper gives 3.9 against a like-for-like baseline [S1], and SCIP 10 later reports 6.8 to 10.8 against default depending on the subset [S8].
- **R4.** Flippo et al. say the proof-producing SCIP lacks, above all, presolving [S30]. Exact SCIP has had exact presolve through PaPILO since 2021 [S2, S8]; what it lacks is certification of presolve, so with certificates switched on presolve is either off (2021) or outside the certificate (2024–2025) [S2, S4, S8]. The critique is accurate for certification and imprecise for solving.

---

## 12. How Gleixner handles critique (pattern for Phase 2)
1. **Concedes limits in the same paper, with numbers** [stated]: the performance gap and its causes [S1, S2, S8], uncertified presolve [S1, S4, S6, S8], VIPR's narrow coverage [S5, S6], iterative refinement's missing recovery [S10], MIPLIB's selection drawbacks [S14].
2. **Turns each conceded gap into the next project**, usually with a student as first author: safe GMI cuts, certified propagation, precision boosting, certified presolve, a symmetry proof system, a study of floating-point decision correctness [S7], a delta debugger for MIP solvers [S22] [practice].
3. **Imports the rival school's tools instead of defending his own as sufficient:** precision boosting into SoPlex [S10]; VeriPB and pseudo-Boolean reasoning with Nordström [S6] [practice].
4. **Code-level critique gets a fast, courteous, collaborative reply:** thanks to reporters, his own fix offered for the reporter's review, diagnoses by group members within a day, warnings where a limit cannot be removed [S17, S19] [practice].
5. **Printed outside critiques of his methods get no printed reply** in the texts found (Wood et al. on the checker; Escobedo et al. on iterative refinement). The flaw Wood et al. demonstrated stayed in the checker until a GitHub issue in 2026 [S17, S24] [inferred].
6. **Helps rivals measure his software** (Casablanca et al. thank him for help with SoPlex) [S38] [observed].
7. **Records corrections publicly** in MIPLIB: changelog, `numerics` tags, benchmark set version 2 [S14, S20] [practice].
8. [inferred] An asymmetry worth carrying into the skill: critique that arrives as an issue or pull request in his repositories is acted on within days; critique in journals is absorbed indirectly, through later papers that do not cite it.

---

## Contradictions (kept, not reconciled)
- **C1. How much exactness is needed.** 2021 and 2023: floating-point MIP solvers can wrongly claim optimality or infeasibility, and results that rest on them are weaker than they could be [S2 PDF pp. 3–4, S1]. 2025 (Hoen and Gleixner): in the overwhelming majority of cases all branch-and-bound decisions of floating-point SCIP are correct, and errors touch only a few leaves (abstract) [S7]. Both co-signed; different emphasis.
- **C2. Certificate cost judged acceptable versus the same table.** The 2017 paper calls the cost of certificates noticeable but not prohibitive (PDF p. 10); its Table 1 shows the certificate-producing version solving 39 of 57 easy instances (54 without certificates) and 14 of 50 hard ones (23), with 17 runs stopped at the 10 GB certificate cap (PDF p. 9) [S3].
- **C3. Independent verification versus a trusted checker.** The design premise is a simple format that anyone can check independently [S3]; the reference checker had soundness holes from 2016 (solution check, rounding with continuous variables) and later (solution-based cutoffs for maximization), and certificates still exclude presolve [S17, S18, S8]. Meanwhile the group's papers report certificates verified with `viprchk` [S2, S4].
- **C4. MIPLIB 2017's aims versus its means.** It aims to drive solver development and avoid bias toward any solver, yet selects with current solver performance, a drawback it admits [S14 p. 478]; insiders warn that tuning on MIPLIB may overstate progress [S39], while other insiders praise the selection as systematic [S40].
- **C5. Heterogeneous library versus distributional learning.** MIPLIB 2017 (2021) is built for heterogeneity [S14]; ML4CO (2022) frames instance-by-instance solving as a blind spot of the field [S15]. Both co-signed.
- **C6. The price of exactness, by study and subset:** 3 (an earlier study by Wolter, cited as [37] in S1 and relayed on p. 809; not checked), 3.9 and 8.1 [S1], 2.6–3.6 and 6.8–10.8 [S8], and the qualitative judgement that exact solvers remain far behind default efficiency [S31]. Kept as reported.
- **C7. Iterative refinement versus precision boosting.** The 2025 paper says refinement beats boosting in most cases but is less robust [S10]; Casablanca et al. find boosting faster on Sloane–Stufken LPs and concede problem dependence [S38].
- **C8. Rational reconstruction (2016) versus basis factorization (2025).** The group's own later paper finds factorization better on average [S10]: a self-revision.
- **C9. Exactness versus an input range.** Exactness holds within the floating-point infinity threshold of the hybrid design (1e20), per Gleixner's own reply in issue #151 [S19].

## Gaps
- **Public reviews.** The NeurIPS 2021 reviews of Chmiela, Khalil, Gleixner, Lodi, Pokutta sit behind an OpenReview bot challenge; two blind-submission records exist under the same title (ids `mvEhkIqn45_`, `fEImgFxKU63`), and whether one was withdrawn or rejected is unknown. No other public reviews or rebuttals were found. No rejected papers were identified.
- **Sidorov et al. (AAAI 2024)** full text not read (Anubis check): their certificate-size comparison with VIPR is known only from citation contexts.
- **Escobedo et al. (TOMS 2018)** full text not read. A 2016 dissertation by A. R. Escobedo (Semantic Scholar CorpusId 125333232) is indexed with sharper remarks (the absolute-tolerance assumption; a count of instances on which refinement converged), but its institution and identifier were not verified, so it is not used as evidence.
- **The 2016 IJOC and 2012 ISSAC iterative-refinement papers** were not read (closed); what they themselves concede is unchecked.
- **MIPLIB 2017:** no outside published critique of the selection method found; the promised hindsight study not found; the outcome of the MIPLIB 2024 call not found (portal unreachable); the earlier status of the four instances reopened in October 2020 not checked; Mittelmann's benchmark pages not consulted.
- **Checkers:** whether the CakeML-verified checker shares the solution-cutoff flaw for maximization was not checked; the fate of PRs #24, #25, #28 and issues #26, #27 after 2026-11-08 is open.
- **Not searched for lack of budget:** commercial vendors' public views on exact MIP; critiques of SCIP's pre-2022 academic licence; critiques of GPU domain propagation (the citation lookup returned 404); MIPLIB 2010 and QPLIB critiques; talks or interviews in which Gleixner answers critics (agents 02 and 04 cover talks and students).

## Sources
Page numbers: printed pages for journal and LIPIcs copies; PDF pages for arXiv and ZIB-Report copies.

Gleixner-side
- S1. Eifler, Gleixner. A computational status update for exact rational mixed integer programming. Math. Program. 197 (2023) 793–812. DOI 10.1007/s10107-021-01749-5 (open access) (P)
- S2. Eifler, Gleixner. A Computational Status Update for Exact Rational Mixed Integer Programming. IPCO 2021, LNCS pp. 163–177, DOI 10.1007/978-3-030-73879-2_12; read as ZIB-Report 21-04, arXiv 2101.09141 (P)
- S3. Cheung, Gleixner, Steffy. Verifying Integer Programming Results. IPCO 2017, LNCS pp. 148–160, DOI 10.1007/978-3-319-59250-3_13; read as ZIB-Report 16-58 (rev. 2017), arXiv 1611.08832v2 (P)
- S4. Eifler, Gleixner. Safe and Verified Gomory Mixed-Integer Cuts in a Rational Mixed-Integer Program Framework. SIAM J. Optim. 34 (2024) 742–763, DOI 10.1137/23M156046X; read as arXiv 2303.12365 (P, passage)
- S5. van Doornmalen, Eifler, Gleixner, Hojny. A proof system for certifying symmetry and optimality reasoning in integer programming. arXiv 2311.03877 (2023) (P, PDF p. 2)
- S6. Hoen, Oertel, Gleixner, Nordström. Certifying MIP-Based Presolve Reductions for 0–1 Integer Linear Programs. CPAIOR 2024, LNCS pp. 310–328, DOI 10.1007/978-3-031-60597-0_20; arXiv 2401.09277 (P, PDF p. 2)
- S7. Hoen, Gleixner. Analyzing the Numerical Correctness of Branch-and-Bound Decisions for Mixed-Integer Programming. CPAIOR 2025, LNCS pp. 35–50, DOI 10.1007/978-3-031-95976-9_3; arXiv 2412.14710v3 (P, abstract and PDF p. 2)
- S8. Hojny et al. (34 authors incl. Gleixner). The SCIP Optimization Suite 10.0. arXiv 2511.18580 (2025) (P, §3.1, pp. 6–11)
- S9. Bolusani et al. (incl. Gleixner). The SCIP Optimization Suite 9.0. arXiv 2402.17702 (2024) (S, S2 contexts)
- S10. Eifler, Nicolas-Thouvenin, Gleixner. Combining Precision Boosting with LP Iterative Refinement for Exact Linear Optimization. INFORMS J. Comput. 37 (2025) 933–944, DOI 10.1287/ijoc.2023.0409; arXiv 2311.08037 (P)
- S11. Gleixner, Steffy. Linear programming using limited-precision oracles. Math. Program. 183 (2020) 525–554, DOI 10.1007/s10107-019-01444-6; arXiv 1912.12820 (P, §1–2)
- S12. Gleixner, Steffy, Wolter. Iterative Refinement for Linear Programming. INFORMS J. Comput. 28 (2016) 449–464, DOI 10.1287/ijoc.2016.0692 (S, metadata; not read)
- S13. Gleixner, Steffy, Wolter. Improving the accuracy of linear programming solvers with iterative refinement. ISSAC 2012, pp. 187–194, DOI 10.1145/2442829.2442858 (S, metadata; not read)
- S14. Gleixner, Hendel, Gamrath, et al. (16 authors). MIPLIB 2017: data-driven compilation of the 6th mixed-integer programming library. Math. Program. Comput. 13 (2021) 443–490, DOI 10.1007/s12532-020-00194-3 (open access, CC BY-SA) (P)
- S15. Gasse et al. (41 authors incl. Gleixner). The Machine Learning for Combinatorial Optimization Competition (ML4CO): Results and Insights. arXiv 2203.02433 (2022) (P, abstract and introduction)
- S16. Gleixner. Curriculum Vitae, updated 2017-07-31. https://www.zib.de/userpage/gleixner/gleixner.pdf (fetched in this run by research agent 04; read) (P)
- S17. scipopt/vipr on GitHub: README, CHANGELOG (VIPR 1.0–1.2), commit list to `99eec19`, pull requests #1–#25 and #28, issues #26–#27 with comments. https://github.com/scipopt/vipr (read 2026-11-08) (P)
- S18. ambros-gleixner/VIPR on GitHub (archived): `code/viprchk.cpp` at commit `f5831734c0` (2016-11-23) and at master; commit history of that file. https://github.com/ambros-gleixner/VIPR (read 2026-11-08) (P)
- S19. scipopt/scip GitHub issues #79, #151, #203, #205, #238, #248, #261 with comments. https://github.com/scipopt/scip/issues (read 2026-11-08) (P)
- S20. MIPLIB 2017 CHANGELOG and News Log. https://miplib.zib.de/CHANGELOG.html, https://miplib.zib.de/news.html (read 2026-11-08) (P)
- S21. Cook, Koch, Steffy, Wolter. A hybrid branch-and-bound approach for exact rational mixed-integer programming. Math. Program. Comput. 5 (2013) 305–344, DOI 10.1007/s12532-013-0055-6 (S, metadata; the baseline framework)
- S22. Hoen, Kamp, Gleixner. MIP-DD: Delta Debugging for Mixed-Integer Programming Solvers. INFORMS J. Comput. 38 (2026) 414–423, DOI 10.1287/ijoc.2024.0844 (S, S2 context)
- S23. Gleixner, Gottwald, Hoen. PaPILO: A Parallel Presolving Library for Integer and Linear Optimization with Multiprecision Support. INFORMS J. Comput. 35 (2023) 1329–1341, DOI 10.1287/ijoc.2022.0171 (S, metadata; target of S48)
- S56. Gleixner. Homepage, https://www.zib.de/userpage/gleixner/ (fetched in this run by research agent 04; read: roles and short CV) (P)
- S57. Borst, Eifler, Gleixner. Certified Constraint Propagation and Dual Proof Analysis in a Numerically Exact MIP Solver. arXiv 2403.13567 (2024) (S, metadata)
- S58. Mexi, Berthold, Gleixner, Nordström. Improving Conflict Analysis in MIP Solvers by Pseudo-Boolean Reasoning. CP 2023, LIPIcs, DOI 10.4230/LIPIcs.CP.2023.27; arXiv 2307.14166 (S, metadata via DBLP)
- S59. Eifler, Gleixner, Pulaj. A Safe Computational Framework for Integer Programming Applied to Chvátal's Conjecture. ACM Trans. Math. Softw. 48 (2022) 1–12, DOI 10.1145/3485630 (S, metadata)
- S60. Furini et al. (13 authors incl. Gleixner). QPLIB: a library of quadratic programming instances. Math. Program. Comput. 11 (2019), DOI 10.1007/s12532-018-0147-4 (S, metadata via DBLP)

Others
- S24. Wood, Zhou, Wu, Mendes, Pulaj. Satisfiability modulo theories for verifying MILP certificates. J. Symbolic Comput. 135 (2026) 102543, DOI 10.1016/j.jsc.2025.102543; arXiv 2312.10420v4 (P)
- S25. Szeider. VIPR Certificate Construction from Black-Box ILP Solvers. CP 2026, LIPIcs 379, 52:1–52:14, DOI 10.4230/LIPIcs.CP.2026.52 (P, pp. 52:1–52:2)
- S26. Sidorov, de Almeida Correia, de Weerdt, Demirović. Paths, Proofs, and Perfection: Developing a Human-Interpretable Proof System for Constrained Shortest Paths. AAAI 38 (2024) 20794–20802, DOI 10.1609/aaai.v38i18.30068 (S, S2 contexts; full text not read)
- S27. Demirović, McCreesh, McIlree, Nordström, Oertel, Sidorov. Pseudo-Boolean Reasoning About States and Transitions to Certify Dynamic Programming and Decision Diagram Algorithms. CP 2024, LIPIcs 307, DOI 10.4230/LIPIcs.CP.2024.9 (P, p. 9:2)
- S28. Koops, Le Berre, Myreen, Nordström, Oertel, Tan, Vinyals. Practically Feasible Proof Logging for Pseudo-Boolean Optimization. CP 2025, LIPIcs 340, DOI 10.4230/LIPIcs.CP.2025.21 (P, pp. 21:2–21:3)
- S29. Dold, Katsirelos, Koops, Myreen, Nordström, Oertel, Tan. End-to-End Certified Graph Colouring. CP 2026, LIPIcs 379, DOI 10.4230/LIPIcs.CP.2026.21 (P, pp. 21:2–21:3)
- S30. Flippo, Sidorov, ten Brink, Pit-Claudel, Demirović. Formally Verified Certification of Constraint Programming Proofs. CP 2026, LIPIcs 379, DOI 10.4230/LIPIcs.CP.2026.24 (P, p. 24:3)
- S31. Ihalainen, Vandesande, Schidler, Berg, Bogaerts, Järvisalo. Efficient and Reliable Hitting-Set Computations for the Implicit Hitting Set Approach. Accepted at AAAI 2026; arXiv 2508.07015v2 (P, PDF pp. 1–2, 6)
- S32. Ihalainen, Vandesande, Schidler, Berg, Järvisalo. HitPBO: An Implicit Hitting Set Solver for Pseudo-Boolean Optimization (Tool Paper). SAT 2026, LIPIcs 377, DOI 10.4230/LIPIcs.SAT.2026.34 (S, S2 context)
- S33. Jabs, Berg, Järvisalo. Engineering and Evaluating Multi-objective Pseudo-Boolean Optimizers. JELIA 2025, LNCS pp. 115–134, DOI 10.1007/978-3-032-04587-4_8 (S, S2 context)
- S34. Halbig, Oertel, Weninger. Exact Decomposition Branching exploiting Lattice Structures. arXiv 2410.22147 (2024) (P, passage)
- S35. Escobedo, Moreno-Centeno, Lourenco. Solution of Dense Linear Systems via Roundoff-Error-Free Factorization Algorithms. ACM Trans. Math. Softw. 44 (2018) 1–24, DOI 10.1145/3199571 (S, S2 context)
- S36. Hartmanns, Junges, Quatmann, Weininger. A Practitioner's Guide to MDP Model Checking Algorithms. TACAS 2023; arXiv 2301.10197 (P, PDF pp. 12, 16)
- S37. Chen, Cheung, Kielstra, Winn. Revisiting a Cutting Plane Method for Perfect Matchings. arXiv 1908.10989 (2019) (P, PDF pp. 6–7)
- S38. Casablanca, Sidaway, Soudjani, Zuliani. Verified Linear Programming via Tolerance-Aware Precision Boosting. arXiv 2609.11721v3 (2026; unreviewed) (P, PDF pp. 2, 16–17, 21)
- S39. Koch, Berthold, Pedersen, Vanaret. Progress in mathematical programming solvers from 2001 to 2020. EURO J. Comput. Optim. 10 (2022) 100031, DOI 10.1016/j.ejco.2022.100031; read as arXiv 2206.09787 (P, PDF pp. 5, 15)
- S40. Maher, Ralphs, Shinano. Assessing the Effectiveness of (Parallel) Branch-and-bound Algorithms. arXiv 2104.10025 (2021) (P, PDF p. 17)
- S41. Huang, Huang, Ferber, Dilkina. Distributional MIPLIB: a Multi-Domain Library for Advancing ML-Guided MILP Methods. arXiv 2406.06954v2 (2024) (P, PDF pp. 1–3)
- S42. Wu, Song, Cao, Zhang. Learning Large Neighborhood Search Policy for Integer Programming. NeurIPS 2021; arXiv 2111.03466 (S, S2 context)
- S43. Qian, Morris. Principled Data Augmentation for Learning to Solve Quadratic Programming Problems. NeurIPS 2025; arXiv 2506.01728 (S, S2 context)
- S44. Cai, Huang, Dilkina. Learning Backdoors for Mixed Integer Linear Programs with Contrastive Learning. ECAI 2024, DOI 10.3233/FAIA240768 (S, S2 context)
- S45. Maudet, Danoy. A Distance Metric for Mixed Integer Programming Instances. ECAI 2025; arXiv 2507.11063 (S, S2 context)
- S46. Robinson La Rocca, Cordeau, Frejinger. Supervised Large Neighbourhood Search for MIPs. arXiv 2501.10778 (2025) (S, S2 context)
- S47. Li, Kulkarni, Menache, Wu, Li. Towards Foundation Models for Mixed Integer Linear Programming. arXiv 2410.08288 (2024) (S, S2 context)
- S48. Dai, Chen. Serial and parallel two-column probing for mixed-integer programming. Math. Program. Comput. (2026), DOI 10.1007/s12532-026-00314-5 (S, S2 context)
- S49. Pulaj, Wood. Local Configurations in Union-Closed Families. Exp. Math. 34 (2024) 719–727, DOI 10.1080/10586458.2024.2410964 (S, S2 context)
- S50. Rodriguez-Flores et al. gMCSpy: efficient and accurate computation of genetic minimal cut sets in Python. Bioinformatics 40 (2024), DOI 10.1093/bioinformatics/btae318 (S, S2 context)
- S51. Skipper et al. Optimizing Fair Geographic Access to Polling. Election Law Journal (2025), DOI 10.1089/elj.2024.0060 (S, S2 context)
- S52. LeanVIPR: formally verified VIPR certificate checker in Lean 4. https://github.com/cruisesong7/LeanVIPR (repository created 2026-10-28; README read 2026-11-08) (P)
- S53. CakeML, `examples/vipr` (Formalisation of VIPR). https://github.com/CakeML/cakeml/tree/master/examples/vipr (README and commit history from 2022-12-18 read 2026-11-08) (P)
- S54. Semantic Scholar Graph API citation contexts for 20 Gleixner works, fetched 2026-11-08 (method source) (S)
- S55. arXiv API listing for `au:Gleixner_Ambros` (48 preprints) and the DBLP record 07/3479 (74 records), fetched 2026-11-08 (method source) (S)

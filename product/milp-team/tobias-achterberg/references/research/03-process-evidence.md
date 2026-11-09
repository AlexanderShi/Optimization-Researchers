# Tobias Achterberg · 03 Process evidence (what he actually does)

- **Researcher**: Tobias Achterberg (living). Original author of SCIP and of the thesis *Constraint Integer Programming* (TU Berlin, defended 12 July 2007). Dated affiliations seen in this run, from documents only:
  - ZIB: commits as achterberg@zib.de from 23 Oct 2002 to 18 Mar 2009 (S17).
  - ILOG: the May 2007 acknowledgements mention "my new employer ILOG" (S1 p. ix). ILOG Deutschland GmbH on ZR 08-29, Aug 2008 (S9 p. 1).
  - IBM: achterberg@de.ibm.com on ZR 09-38, Nov 2009 (S10 p. 1).
  - Gurobi: Houston address on the RAMP paper of Oct 2014 (S11 p. 181); a SCIP commit from achterberg@gurobi.com on 2 Nov 2014 (S17); Gurobi GmbH, Monheim am Rhein, on arXiv 2211.13545v3, July 2024 (S16 p. 1); listed as Vice President of Research and Development for the webinar of 12–14 Dec 2023 (S18).
  - Start and end dates of each employment are not established here (see 06-trajectory).
- **Dimension**: research-craft Phase 1, research agent 03 of 06: process evidence. What his papers, code, test scripts and decks show he did: how test sets and baselines are chosen, what is done first, how he debugs, what he drops.
- **Research date**: 2026-11-08
- **Sources consulted**: 41 numbered sources (S1–S41).
  - 17 are primary texts, decks or code that were read in full or in the relevant part (S1–S17).
  - 2 are observed sources (S18, S19). 5 are metadata services (S20–S24). 16 are works checked by identifier but not read (S25–S40).
  - S41 is the sibling note 02-methodology.md, used only as a pointer for the say-versus-do check in §12.
  - WebSearch calls used: 3 of 5.
- **Local corpus**: `references/sources/{papers,talks,essays,software,publications}` held only `.gitkeep`. There was no user-supplied material. `private/` was not opened. Nothing was written to `../sources/talks/`: no transcript exists for the decks found, the decks are copyrighted, and two of them (S14, S15) carry a Gurobi "Confidential" footer although they are publicly posted. Downloaded files stay in the scratch folder `C:\Users\sr881\AppData\Local\Temp\milp-team-t1-scratch\base-skills\tobias-achterberg\03\`.
- **Tags**:
  - [stated]: what Achterberg said or wrote about his own work (self-reports of process included).
  - [practice]: what his papers, code, commits, test scripts and tables show was actually done.
  - [observed]: what others recorded.
  - [inferred]: my inference or my arithmetic, not established.
  - Each item also says P (primary) or S (secondary). Co-authored texts are marked "co-authored" and are not credited to him alone.
- **Quotation policy**: the note paraphrases and gives page, slide or commit locators. It contains one sentence-level quotation (Q1, ten words, S1 p. ix). Every other pair of quotation marks encloses only a title, a table or column label, or a short label taken from a document. Code identifiers are in backticks.
- **Page conventions**:
  - S1 (ZIB copy of the revised thesis): printed page = PDF page − 14.
  - ZIB-Reports S3–S10: printed page = PDF page − 1 (the cover page is unnumbered).
  - S12 (ZR 16-44): printed page = PDF page − 2.
  - S11: the proceedings page numbers (181–196).
  - S13, S14, S15: slide number = PDF page.
  - S16: page numbers of arXiv v3.
- **Access notes (2026-11-08)**:
  - ZIB OPUS (opus4.kobv.de) answers curl with an Anubis bot challenge. It was not solved. WebFetch received the PDFs directly. The OPUS search pages returned HTTP 500, so report docIds were taken from OpenAlex links and neighbouring frontdoor pages (S24).
  - The 2007 DepositOnce copy of the thesis (S2) uses Type 3 fonts and does not extract to text. Its title page and contents pages were compared visually.
  - ScienceDirect returned HTTP 403 for the journal version of the conflict-analysis paper. Nothing was routed around. Journal versions are listed as not read.
  - The Semantic Scholar API returned HTTP 429 and was not used.
  - The Gurobi CDN returned HTTP 503 to curl. WebFetch received the same deck (S15).
  - Several thesis tables extract with shifted columns. Table numbers in this note were either read from the page image or come from the running text, never from a garbled extraction. Example: the S1 Table 5.2 total for µ = 1/6 is +14 on the page image, while the layout extraction suggested +13.

---

## 0. Authorship labels (they must survive into the skill)

| Label | Evidence checked in this run | Tag |
|---|---|---|
| Reliability branching was born in Alexander Martin's SIP, not in SCIP | S3 p. 1: history branching is implemented in SIP. S4 p. 8: the 2004 study runs SIP with CPLEX 9.0 as the LP solver. In SCIP, `branch_history.c` was renamed to `branch_relpscost.c` on 6 Apr 2004 (commit 0c66c58ba) | [practice] P |
| SCIP inherited its first test harness from SIP | The initial commit 147d53683 (23 Oct 2002) contains `check/check.sh`, `check/check.awk`, `check/check_cplex.sh` and test lists with `.solu` files of known optimal values. `check.awk` is headed "SIP Check Report Generator" and names Martin, Koch and Pfender as authors | [practice] P |
| The 2006 comparison scripts are his | `check/cmpres.awk` and `check/evalcheck.sh`, added in commit 1dbb9bbf0 (18 Sep 2006), name him as author | [practice] P |
| SCIP was a one-person code base until 2006 | Commits per year by him / all authors in the converted history: 2003 173/173; 2004 265/300; 2005 317/363; 2006 239/261; 2007 189/457; 2008 75/853 (S17). The counts are approximate, because the CVS-to-git conversion splits some commits per file | [practice] P; [inferred] for the approximation |
| Commit authorship rests on the converter's mapping | The CVS `$Id` lines of his files from 2002–2005 carry the login bzfpfend (for example `branch_relpscost.c` 1.1, 6 Apr 2004; `debug.c` 1.1, 29 Apr 2005), while the git history assigns these revisions to Tobias Achterberg and the file headers name him as `@author` | [practice] P; caution [inferred] |
| His footprint in today's SCIP | At HEAD 353584f2a (8 Nov 2026), 154 of the 419 `.c` files in `src/scip` list him as `@author`, and 147 list him first (S17) | [practice] P |
| Cuts and heuristics in the thesis are partly student work | S1 pp. 3–4: the details of cut separation are in Kati Wolter's diploma thesis and those of the primal heuristics in Timo Berthold's. The thesis measures these components under its single protocol | [stated] P |
| Co-authored works | MIPLIB 2003 (Koch corresponding author, S7 p. 1); ZR 08-29 (three authors); the MCF separator (with Raack); the objective feasibility pump (with his student Berthold); the presolve papers (five Gurobi/Erlangen authors); the RLT cuts paper (Bestuzheva first author). Practices in these are labelled co-authored | [practice] P |
| Gurobi decks | S13 (CPAIOR 2017 Master Class; speaker named in the conference programme, not on the slides) and S14 (SEA 2022; name on the title slide) are his solo decks. S15 (Gurobi 11.0) was co-presented with Fernando Orozco (S18), and slide authorship is not stated | [observed] S18; [practice] P |
| Post-2014 Gurobi code is closed | Only published papers, decks and his public SCIP commits of 2014 and 2016 are evidence of his Gurobi-era practice | — |
| A colleague credits his MIP work | S19 p. 4 (interview questions Oct 2015, published Sept 2016): Bixby names Rothberg and Gu as the ones who made the real MIP contributions, and now Achterberg (paraphrase) | [observed] S |

---

## 1. Era and resource context (timeline for every item below)

| Period | Role and setting (dated) | Compute, tools, team | Evidence |
|---|---|---|---|
| ~2000–2002 | Computer-science master's thesis on neural networks that learn branching strategies, done inside SIP. Then history branching with Koch and Martin | SIP with CPLEX 7.5 as LP solver; Alpha 21264 at 750 MHz with 2 GB | S1 p. ix; S3 pp. 1, 10 |
| Oct 2002 – 2004 | Starts SCIP alone at ZIB. Version 0.2 (26 Mar 2003) solves complete problems but has no special constraints, propagators, separators, heuristics or branching rules. Conflict analysis is added on 13 Aug 2003 | CVS; lint stubs from day one; SIP's check scripts; CPLEX as the LP solver | S17 (147d53683, 3c603242f, 6748acb5f); S1 pp. 6, ix |
| 2004–2006 | First papers on SCIP, branching and conflict analysis; MIPLIB 2003 | Alpha 21264 at 833 MHz (2004); 3.2 GHz Pentium-4EE with 2 GB (2004–2005); CPLEX 9.0x as LP solver | S4 p. 8; S5 p. 23; S6 p. 14 |
| Aug 2006 – May 2007 | Thesis benchmarks: test set selected with a frozen SCIP 0.82d; final runs with SCIP 0.90f (MIP) and 0.90i (chip) | Eight identical Dell Precision 370 PCs (3.8 GHz Pentium 4, 2 GB), partly colleagues' spare cycles. 244 instances × 115 settings = 28,060 runs, more than one CPU year. Students: Wolter, Berthold | S1 pp. 2, x, 319–320; S17 (ad1fe4965) |
| 2007–2009 | ILOG, then IBM; continues SCIP work (MCF separator, parameter tuning) until March 2009; implements the MCF separator in both SCIP and CPLEX | 3.6 GHz Pentium-D (2008); a 3.00 GHz quad-core machine for SCIP 1.1.0.8 with CPLEX 11.2.1 as LP solver, and a single CPU of a 3.33 GHz quad-core machine for CPLEX 12.1 with a CPLEX-internal test set (2009) | S9 p. 4; S10 pp. 1, 17, 22; S17 |
| 2009–2014 | IBM CPLEX. Measurement study with Wunderling on CPLEX 12.5 (S32, not read) | Known only through relays (S12 p. 4; S13 slides 77, 80; S14 slide 63) | — |
| 2014 onward | Gurobi. Presolve papers (2014, 2016), CPAIOR 2017 Master Class, SEA 2022 talk, Gurobi 11.0 release webinar (2023), RLT cuts with ZIB (2022–2025) | Single 4-core i7-3770K, 32 GB (2014, 2016); Xeon E3-1240 v3 or v5, 4 cores, 8 hyper-threads, 32 GB (2022, 2023). Test sets of 2,974 → 3,182 → 7,030 → 7,766 models; time limits 10,000 s or 3,600 s | S11 p. 190; S12 p. 2; S14 slide 5; S15 slide 11 |

---

## 2. Research taste (layer 1): behavioural evidence

**PE-01. The yardstick is the best commercial solver, reported even when it beats his own code.** [practice] P
- 2002: CPLEX 7.5 with matched gap tolerances (S3 p. 10).
- 2004: CPLEX 9.0 is run only to check that the SIP environment is state of the art. SIP's own preprocessing and cuts are fed to CPLEX so that both run pure branch-and-bound on the same problems (S4 pp. 8–9).
- 2004/05: SCIP 0.78 is about a factor of 2 slower than CPLEX 9.03 in both geometric mean and total time, and SIP is slightly better than SCIP; reasons are given (untuned successor, framework overhead) (S5 pp. 23, 25).
- 2005: SCIP is called not strictly competitive with CPLEX, but not far away (S6 p. 15).
- 2007: SCIP 0.90f is 115 % and 0.90i 63 % slower than CPLEX 10.0.1 in the shifted geometric mean. The comparison covers only the MIP part, because SCIP itself uses CPLEX for the LPs; with SoPlex SCIP is usually much slower (S1 p. 377).
- The day-one harness already had `check_cplex.sh` and `check_cplex.awk` beside the SCIP scripts (S17, 147d53683). A CBC benchmark script followed in July 2007 (206607fb4).
- Era: academic code measured against a commercial code whose LP solver it borrowed.

**PE-02. A new component has to do no harm outside its target class.** [practice] P (partly co-authored)
- MCF separator (with Raack): the code detects a network, measures how inconsistent it is, and generates no cuts when the structure is not consistent. This follows a remark by Bixby and Rothberg, which S10 quotes, that a method should recognise the models it applies to and cost little when the model does not fit (S10 p. 1).
- Its parameters were fixed after extensive tests. The goal was an order-of-magnitude speed-up on network design instances without cutting too aggressively and without slowing general MIPs. It was then measured on network-design sets, on MIPLIB 3 + 2003, on Mittelmann's instances and on the CPLEX-internal test set (S10 pp. 16–17, 22). The report's conclusion claims almost no degradation on the other models (S10 p. 29).
- Thesis: inference branching wins only on the feasibility-type sets (enlight, alu, acc). The default is a hybrid that carries part of that gain over without losing elsewhere (S1 p. 70).
- Thesis: restarts are applied only after the root node (S1 pp. 4, 163).
- Gurobi 2014: multi-row redundancy checks and rank-revealing dependent-row detection are disabled by default for MIP because they hurt (S11 p. 192, co-authored).

**PE-03. Real-world libraries, with problem classes weighted so that none dominates.** [practice] P
- MIPLIB 2003 aims at challenging real-world instances, not artificial ones (S7 p. 3, co-authored).
- Thesis: ten public test sets. The seven single-class sets each count as three pseudo-instances in the total, so the mean covers 105 instances plus 21 pseudo-instances (S1 p. 322).
- Chip verification: industrial property-checking instances generated by OneSpin Solutions (S1 pp. 322–323).
- Gurobi 2022: the internal test set mixes customer models and public benchmarks and is chosen so that no problem class is over-represented (S16 p. 21, co-authored; who ran the Gurobi runs is not stated).
- Gurobi 2014/2016: the presolve test sets are the subset of a library of public and commercial models that some Gurobi release has solved within 10,000 s (S11 p. 191; S12 p. 3).

**PE-04. Prefer one parameterised family to an elaborate special rule.** [practice] P (co-authored)
- 2002 history branching keeps three levels of history (variable, class, global), separate strong-branching values with dynamically fitted scaling factors, and parameters that adapt to time ratios and depth (S3 pp. 6–8).
- 2004 reliability branching keeps one reliability parameter. Pseudocost branching (0), pseudocost branching with strong-branching initialisation (1) and strong branching (∞) become special cases (S4 pp. 1, 6–7). The classes and scaling factors no longer appear.
- The objective feasibility pump (with Berthold) reduces to the original pump when α0 = 0 (S8 p. 4). The original is therefore the same code with one parameter changed.

**PE-05. Simple statistics over cleverness, when measured against the best-tuned alternative.** [practice] P
- The product score function was tested against the weighted sum for five µ values. The best weighted sum (µ = 1/6, Martin's SIP value) is still 14 % slower in the shifted geometric mean (S1 p. 71, page image; p. 3).

---

## 3. Problem choice and timing (layer 2)

**PE-06. Build the platform first, and publish only once it carries research.** [stated] P; [practice] P
- Q1 (S1 p. ix): "For almost two years, I did not publish a single paper!"
- The same page says he spent that time writing code as a basis for the actual research (paraphrase).
- Record: the first commit (23 Oct 2002) lays out directories, a Makefile, test scripts and lint stubs. Version 0.2 (26 Mar 2003) solves complete problems without any special components (3c603242f). All 173 commits of 2003 are his (S17).
- The publication record is consistent within months [inferred]: ZR 02-32 (Oct 2002), then ZR 04-13 (May 2004) and ZR 04-19 (June 2004).
- Era: a doctoral position at ZIB whose advisor gave him freedom (S1 p. ix). This is a funded-PhD strategy and needs that kind of position.

**PE-07. Take an industrial project with early data as the application.** [stated] P; [practice] P
- The Valse-XT project with Infineon, later OneSpin Solutions: a direct industrial contact, plenty of test data, delivered early enough to be useful (S1 p. ix).
- Part III of the thesis and its benchmarks rest on these instances (S1 pp. 299, 322–323).
- The ALU instances also served as the infeasible test set of the conflict paper and were contributed to MIPLIB 2003 (S6 p. 15).

**PE-08. Turn a failed reproduction into a study of its own.** [practice] P (co-authored)
- ZR 08-29 began when the authors tried to reproduce van Vyve and Wolsey's TSP formulation results and saw erratic solver behaviour (S9 p. 1).
- They ran every combination of the formulation variants on one TSPLIB instance (att48, k = 13): 128 variants in CPLEX 10.0.1 and 130 distinct runs in SCIP 0.90e (S9 pp. 4–7).
- The fastest CPLEX variant solved in 27 s. A variant of the same size did not solve in 24 hours, a factor of more than 3,200 (S9 p. 6).
- Conclusion: computational papers must state the model formulation precisely, or results cannot be reproduced (S9 p. 7). The Zimpl source files were put online (S9 p. 4; the link was not checked).

**PE-09. Single instances trigger the work; the code history names them.** [practice] P
Commit messages tie fixes and features to named MIPLIB or Mittelmann instances (S17):
- Numerical row scaling on noswot (27747c099, Nov 2004).
- Conflict-analysis assertion crashes on blend2 and rout (0a8a4f3d4).
- Gomory bug on dcmulti (ae6d25490).
- Absolute instead of relative bound feasibility after alu8_9 (510555962, May 2005).
- Fixing tolerance for egout (58dc42155) and table size for nw04 (3d077a320).
- Knapsack clique generation that essentially solves neos1 (da753ab89).
- Diving abort for fast0507 (4dd83420e).
- Performance fixes for neos4 and cap6000 (47f45d324, 3a8b99eb3).
- Root-cut changes aimed at opt1217 and neos632659 (dc7a47783, eaa3e984e).
- MCF work on the rococo instances (66c7c131e).

Conclusions, by contrast, are drawn from averages (PE-31).

**PE-10. Stop engineering and write.** [stated] P
- He missed his own deadline (before his 30th birthday), and Koch convinced him that writing things up mattered more than another 10 % of SCIP performance (S1 p. x).
- The shifted-mean parameters of the thesis were changed on 19 Apr 2007 (1e98661db). The approved version is dated 15 May 2007 (S1 title page).

---

## 4. Idea generation (layer 3)

**PE-11. Import from SAT and CP fast, then adapt to MIP.** [stated] P; [practice] P
- Yakov Novikov explained conflict analysis and two watched literals to him. He put the watched literals into the set-covering handler a few days later and generalised conflict analysis to MIP within three weeks (S1 p. x).
- `conflict.c` was added on 13 Aug 2003. Its header describes a zchaff-like analysis (6748acb5f).
- Restarts were taken from SAT but limited to the root node for MIP (S1 pp. 4, 163).
- Inference branching uses SAT/CP-style inference counts (S1 pp. 2–3).
- He records that Sandholm and Shields developed the same generalisation independently (S1 p. 165).

**PE-12. Start from a state-of-the-art code and adopt its defaults, marking the unverified ones.** [stated] P
- Most of SIP's ideas and algorithms went into the first SCIP (S1 p. 6). The master's thesis used SIP's source (S1 p. ix).
- Martin's child-selection rule was adopted, and the thesis says it was not checked by a thorough computational study (S1 p. 74).
- SIP's µ = 1/6 turned out to be the best weighted-sum value for SCIP too (S1 p. 71).

**PE-13. Generalise, then sweep the family and plot it.** [practice] P (co-authored)
- In 2004 the whole reliability, lookahead and depth grid was run. Every setting was plotted as a point of geometric-mean nodes against time, and (ηrel = 8, λ = 4) was read off as the sweet spot (S4 pp. 9–12).

**PE-14. Look for the structure in the matrix, not in the user's labels.** [practice] P
- The 2002 rule grouped variables into classes by model names (S3 p. 7, footnote). Later work dropped name-based grouping and detects structure from the coefficient matrix itself: MCF network detection with an inconsistency ratio (S10 pp. 1–3), and implicit bilinear products from pairs of rows with binaries (S16 p. 1, co-authored). [inferred] This is a change of approach across the work, not a stated principle.

---

## 5. Experiment design and execution (layer 4)

### 5a. Order of work

**PE-15. Test infrastructure first: the harness is in the first commit.** [practice] P
- 147d53683 (23 Oct 2002): test lists (`miplib.test`, `mittelmann.test`, `shortmiplib.test`, `stp.test`, `zib.test`), files of known optimal values (`*.solu`), a run script with a 3,600 s CPU-time limit, and an awk report generator that compares results with the known optima and writes a LaTeX table.
- `CHANGELOG` started on 14 Oct 2004 at version 0.75 (e4f4a4699).

**PE-16. Freeze one version to select the test set; evaluate later versions on it.** [practice] P
- Version 0.82d was frozen on 24–25 Aug 2006 to run Mittelmann's full set and pick the thesis instances (b1a69fd39, 941b19ff3, ad1fe4965).
- The thesis states the same: CPLEX 10.0.1 and SCIP 0.82d, with and without conflict analysis, decided the selection, and SCIP 0.90f produced the final MIP numbers (S1 pp. 319–320).
- [inferred] Selecting with an older version and with both conflict settings keeps the test set from being chosen by the code under evaluation.

**PE-17. Write the comparison tooling before the big runs.** [practice] P
- Sept 2006: `cmpres.awk` compares several solver runs. It reports geometric means, shifted geometric means and totals only over instances where no solver failed, and counts failures separately (1dbb9bbf0).
- The shift was 60 s / 1,000 nodes. It was changed to 10 s / 100 nodes on 19 Apr 2007 (1e98661db), the values in the thesis (S1 p. 321).

### 5b. Test sets and baselines over time

| Year | Study | Selection rule | Baseline | Source |
|---|---|---|---|---|
| 2002 | History branching | MIPLIB 3.0 instances where CPLEX 7.5 needs more than 1,000 nodes **and** that SIP with history branching solves within 3,600 s. The excluded instances are listed in footnotes, with notes on how SIP and CPLEX did on them | SIP hybrid pseudocost; CPLEX 7.5 (abs. gap 1e−10, rel. gap 0) | S3 pp. 9–10 |
| 2004 | Branching rules revisited | MIPLIB 2003 + instances of ref. [14] where CPLEX 9.0 needs ≥ 5,000 nodes and ≤ 1 h | CPLEX 9.0 fed with SIP's preprocessing and cuts | S4 p. 8 |
| 2004/05 | SCIP report | MIPLIB 2003 + Mittelmann where CPLEX 9.02 needs ≥ 1,000 nodes and ≤ 1 h; compared against 9.03, because the set was assembled before 9.03 appeared | CPLEX 9.03; SIP | S5 p. 23 |
| 2005 | Conflict analysis | MIPLIB 2003 + Mittelmann where CPLEX 9.03 needs ≥ 1,000 nodes, ≥ 30 s and ≤ 1 h; second set: infeasible ALU chip instances, with feasibility and integrality tolerances set to 1e−9 because of coefficients up to 2^(2n) | CPLEX 9.03; SCIP default | S6 p. 15 |
| 2005 | Objective feasibility pump | 121 instances: MIPLIB 2003, Mittelmann, and the instances used by Fischetti, Bertacco and Lodi | original pump with its authors' suggested parameters, after CPLEX preprocessing | S8 p. 5 |
| 2007 | Thesis | 575 public instances. Drop those that neither CPLEX 10.0.1 nor SCIP 0.82d (with or without conflict analysis) solves in 1 h; deduplicate coral against milp; drop coral and mik instances that both solve within 10 s; drop every second coral instance by CPLEX time; trim the alu set to non-trivial instances with registers of ≤ 8 bits (numerics). 244 remain | SCIP default (knock-out); CPLEX 10.0.1 in App. C | S1 pp. 319–320, 377 |
| 2008 | Minor model changes | one TSPLIB instance, full factorial of formulation variants | CPLEX 10.0.1 and SCIP 0.90e (SCIP probing off) | S9 p. 4 |
| 2009 | MCF separator | network-design sets, MIPLIB 3+2003 (92), Mittelmann (disjoint from the others), CPLEX-internal set | SCIP 1.1.0.8 and CPLEX 12.1, each without the separator | S10 pp. 16–17, 22 |
| 2014 | Multi-row presolve | 2,974 models that some Gurobi release has solved within 10,000 s | Gurobi 5.6.3 default, 10,000 s | S11 pp. 190–191 |
| 2016 | Presolve reductions | 3,182 models, same rule | Gurobi 6.5 default, 3,600 s | S12 pp. 2–3 |
| 2022 | RLT cuts (Gurobi side) | internal set, customer and public models, no class over-represented | Gurobi 10.0 beta, RLT off, 10,000 s | S16 p. 21 |
| 2023 | Release comparison | 7,766 MIP models; 714 dropped for inconsistent answers, 2,124 that no version solves; speed-up on the > 100 s bracket (2,892 models) | Gurobi 10.0 | S15 slide 11 |

### 5c. Measurement rules (each traced to a document)

**PE-18. Time limits, failures and noise.** [practice] P (S1 p. 319)
- 1 h for MIP and 2 h for chip runs. A run that hits the limit counts with the limit time and its node count at that moment. The thesis states the bias this creates: it favours runs that hit the limit, but it caps the weight of a single failure.
- Memory limit 1.5 GB. A run that hits it is treated as a time-out, with the node count scaled up at the observed nodes-per-second rate. This happened in 180 of the 28,060 runs.
- Runs were made on unloaded machines, and suspicious benchmarks were rerun. Differences of up to 2 % in the reported means are treated as timing noise.

**PE-19. Choose the mean so that neither easy nor hard instances dominate, and show why with an example.** [practice] P (S1 pp. 321–322)
- Example A.1 builds ten hypothetical node counts for two settings. The same data give a 27 % gain under the geometric mean, a 6 % loss under the shifted geometric mean and an 89 % loss under the arithmetic mean.
- Summary tables use the shifted geometric mean, with s = 10 s for time and s = 100 for nodes. The detailed tables add plain geometric means and totals (S1 p. 325).

**PE-20. Count who wins and separate the instances whose path changed.** [practice] P
- Thesis Appendix B (S1 p. 325) reports the number of instances at least 10 % faster or slower, and splits "different path" from "equal path" instances. Two runs count as having the same path if they have the same node count and the same simplex iteration count.
- Gurobi 2014/2016 (S11 pp. 191–192; S12 pp. 3–4, co-authored) keeps the faster/slower counts with the 10 % threshold and calls a model "affected" if its simplex iteration count changed.
- Same papers: solve-time brackets "[n,10k]" (2014) or "≥ n sec" (2016), defined by the slower of the two runs. Discussion uses the ≥ 10 s bracket. Models where the two versions disagree on the optimal value are excluded. Both papers say they follow the reporting form of Achterberg and Wunderling (S32, not read).
- The 2016 shift is 1 for both time and nodes (S12 p. 3).

**PE-21. Release benchmarks: many small, measured increments.** [practice] P (co-presented, S15)
- Gurobi 10.0 vs 11.0 (Dec 2023): 10,000 s limit, Xeon E3-1240 v5 with 4 cores / 8 hyper-threads and 32 GB, PAR-10 curves of versions 1.1–11.0, speed-ups on the > 1 s and > 100 s brackets (slides 10–11).
- The MIP changes are listed one by one, each with its own percentage; all twenty lie between 0.3 % and 2.1 % (slides 12–13).
- Slide authorship within the co-presented webinar is not stated.

**PE-22. Show what a test set looks like before arguing about algorithms.** [practice] P (S14)
- SEA 2022, his solo talk: problem sizes and solve times of the LP (2,397) and MIP (7,030) test sets under Gurobi 9.5.0 (slides 5–19), and non-zeros per row and per column across the MIP set (slide 24).
- Each algorithmic choice comes with its own measured impact. For example, sorting instead of a median algorithm in the bound-flipping ratio test costs 8.0 % overall and 16.6 % on models that take at least 10 s (slide 29).

### 5d. Ablation and isolation design

**PE-23. Knock-out from the default, component by component, at scale.** [practice] P
- Every chapter of thesis Part II ends with a computational section. Each feature is measured by switching it off against SCIP's default (S1 p. 2, incl. footnote 1).
- The scale: 244 instances × 115 settings = 28,060 runs, more than one CPU year (S1 p. 2).
- Gurobi 2016 uses the same knock-out design, with reductions disabled through source-code changes (S12 p. 3, co-authored).

**PE-24. Isolate the component under test, and say what the isolation costs.** [practice] P
- 2002: the optimal solution is supplied in advance; root cuts are generated once and then disabled, so only branching differs (S3 p. 11).
- 2004: no optimal values are supplied, because reaching good solutions fast is a desirable property of a branching rule. Cut-and-branch is used instead (S4 p. 8). See C-01.
- 2016: presolve stays on in sub-MIPs, so that primal-heuristic decisions are not changed implicitly (S12 p. 3).
- 2016: no benchmark of fixed-variable removal, because model-size changes drive too many heuristic decisions (S12 p. 19).
- 2007: CPLEX's strong-branching routine does not return the dual information needed to analyse an infeasible or bound-exceeding strong-branching LP, so those LPs are solved again with the regular dual simplex. The thesis names this artificial overhead and judges it unlikely to change the results (S1 pp. 180–181).

**PE-25. Give the baseline its best form.** [practice] P
- The strongest SAT solver is chosen as the baseline: MiniSat 1.14, Siege v4 and zChaff were tried, and MiniSat 2.0 was best on most instances (S1 p. 299). Where Siege beats MiniSat 2.0 on one property, Siege's time is reported (S1 p. 303).
- The feasibility pump is run with the parameters its authors suggested, and on their instances (S8 p. 5).
- Five µ values are tried against the product score (S1 p. 71).

### 5e. Debugging and diagnosis

**PE-26. The "debug solution": check every derived object against a known optimum.** [practice] P (S17)
- Added on 29 Apr 2005 (67238f422). A compile-time define names a solution file. Every cutting-plane row is then checked against it, and any row that cuts the solution off is reported.
- By Sept 2008 the module, by then also edited by others, checks global bound changes, inferences, variable bounds, implications, conflicts, node removal and rows of B⁻¹ as well. 24 of the file's commits are his; which check each author added was not traced.
- The same commit makes SCIP check its best solution against the original problem whenever verbosity is at least normal.
- The thesis does not describe this mechanism [observed absence: "debug" in S1 occurs only for memory checking, pp. 37, 51, 53].
- Era: 2005, when he wrote most SCIP commits alone (§0). [inferred] One developer adding reductions faster than a test set can catch wrong answers needs such a check.

**PE-27. Numerics and determinism as first-class bugs.** [practice] P (S17)
- Absolute instead of relative feasibility for bounds (alu8_9, 510555962).
- Epsilon comparison to stop an infinite presolve loop on cap6000 (3a8b99eb3).
- Row scaling on noswot (27747c099).
- Implications ordered by variable index instead of pointer, "makes it more deterministic" in the commit's words (5c7ee1d8e, May 2005).
- Lint stubs from the first commit, and a lint-cleaned code base in May 2005.

**PE-28. Explain why a method works, not only that it works.** [practice] P
- 2002: at every node all candidates are solved, and score and position quotients measure how close history and pseudocost branching come to full strong branching (S3 pp. 12–13).
- 2005: the conflict-analysis time is split into basic and conflict time, which locates the loss (S6 pp. 15–16).
- 2005: plots of objective and fractionality over the pump iterations (S8 pp. 6–7).
- 2007: log-file inspection explains why delayed restarts failed (S1 p. 163).

**PE-29. Gurobi era, in SCIP's public code.** [practice] P (S17)
- Nov–Dec 2016 (issue #1093): 23 commits on SCIP's Gurobi LP interface, mostly fixes (ranged rows, dual norms, basis setting), including a debug method that checks the consistency of ranged-row data (7e3dd75fc).
- Also Nov 2014: a fix to `lpi_none.c` (5c2951bd0).

---

## 6. Judging results (layer 5)

**PE-30. Print negative and neutral results, with numbers.** [practice] P
- 2005: conflict analysis halves the nodes on feasible MIPs but raises the geometric-mean time by about 15 %. The node reduction saves 10 % of basic time, but the analysis itself (mainly re-solving LPs to optimality) costs more (S6 pp. 1, 15–16).
- 2007: delayed restarts during the tree search are inferior to the default (S1 p. 163).
- 2007: all primal heuristics together save only 14 % (S1 pp. 4, 128).
- 2008: SCIP's implied-integer declarations do not help as expected, which the authors read as a weakness of SCIP's implementation (S9 p. 7).
- 2016: Chvátal–Gomory strengthening disappoints (S12 p. 12). Probing on single equations finds reductions on about 20 % of models but does not help (S12 p. 16). Removing subsumed constraints is only performance neutral (S12 p. 27). Global probing at nodes does not help (S12 p. 63).

**PE-31. Refuse to conclude from single instances or small subsets, and scope the claim.** [practice] P
- 2004: conclusions rest on averages over all instances, not on single instances (S4 p. 9).
- 2016: 48 affected SOS models are too few for a conclusion, even with a 25 % gain (S12 p. 17).
- 2007: a result contradicting other researchers is stated only for SCIP and the test sets used (knapsack disaggregation, S1 p. 162).

**PE-32. Treat the non-additive and the indirect as findings.** [practice] P
- The degradations from switching off single heuristic classes add up to much less than switching off all of them. The thesis observes the same for cuts and offers an explanation (S1 p. 128).
- Heuristics change results on test sets where they never find a solution, through LP solutions, branching statistics and search paths (S1 p. 128).
- 2016: removing redundant rows hurts, which the authors do not fully understand. Their hypothesis is that such rows serve as bases for cuts (S12 p. 26).

**PE-33. Revert what is not good overall; keep it as an option when it may help elsewhere.** [practice] P (S17)
- Sept 2008: parameter changes undone because they did not look good overall (7827f4f11).
- Sept 2008: an MIR feature removed after gesa2 gave a wrong answer (83d0d3f01).
- Sept 2008: an always-on change to the feasibility pump timing reverted; the behaviour kept as a parameter, default off (1c685467e).
- Aug 2008: pairwise presolving turned off by default (b9cd8fd36).
- Thesis: the expensive aggregation step of pairwise presolving is disabled by default (S1 p. 161). Octane, local branching, RINS and mutation are off by default (S1 p. 127).

**PE-34. Name priority and independent discovery.** [practice] P
- S1 p. 165 (Sandholm and Shields).
- S16 calls the Gurobi and SCIP implementations independent (pp. 1, 22) and says their results cannot be compared directly because the setups differ (p. 21).

---

## 7. Expression (layer 6)

**PE-35. Fixed reporting form.** [practice] P
- Thesis: each chapter ends with a computational section. Summary tables give the percentage change of the shifted geometric mean against the default, with a positive sign for a deterioration. About 50 pages of detailed tables follow in Appendix B, the protocol in Appendix A and the comparison with CPLEX in Appendix C (S1 pp. 319–378).
- The presolve papers reuse one table layout for 30+ reductions: brackets, time-outs, faster/slower counts, time and node ratios, affected models (S12 Tables 1–38).

**PE-36. Make exclusions and origins visible.** [practice] P (2005 co-authored)
- Excluded instances listed in footnotes (S3 p. 9).
- Instances removed from MIPLIB listed by name, together with the CPLEX-8 settings used to decide (S7 p. 2).
- Origin, reference and URL of each test set given (S1 p. 320).

**PE-37. Teaching decks reuse measured impacts across solvers and say where each number comes from.** [practice] P (S13)
- CPAIOR 2017: component impacts are drawn from several sources, each slide naming its own: Gurobi 5.6 for presolve, CPLEX 12.5 (Achterberg–Wunderling) for cuts, branching and parallelism, Berthold's SCIP 0.82b and 3.0.2 studies for heuristics, his thesis for node selection, and Mittelmann's benchmarks for the LP solver (slides 12–20, 42, 59, 64–67, 77, 80).
- For heuristics he asks whether time to optimality is the right measure, and switches to the primal integral (slides 65–67).

**PE-38. Data and code availability.** [practice] P
- Thesis benchmark versions are available from the author on request (S1 p. 319).
- The 2008 model files were put on a ZIB page (S9 p. 4; not checked).
- MIPLIB 2003 kept a bulletin board instead of maintained best bounds (S7 p. 2, co-authored).

---

## 8. Research organisation (layer 7)

**PE-39. Solo build, then hand components to students and measure them under one protocol.** [practice] P; [stated] P
- The commit shares in §0 show the solo phase.
- Wolter's and Berthold's diploma theses hold the details of the cuts and heuristics (S1 pp. 3–4).
- The objective feasibility pump paper is co-authored with Berthold (S8).

**PE-40. Borrow compute; keep it identical.** [stated] P
- Colleagues on identical machines lent their spare cycles (S1 p. x). Runs were spread over eight equivalent machines (S1 p. 319).

**PE-41. Implement in an academic and a commercial code, or compare two independent implementations.** [practice] P (co-authored)
- MCF separator in SCIP 1.2 and in CPLEX (S10 p. 1).
- RLT cuts implemented independently in SCIP and Gurobi (S16 pp. 21–22).

**PE-42. Keep contributing to the academic solver from industry.** [practice] P
- His 75 SCIP commits of 2008, still under the ZIB address, fall in the period when ZR 08-29 lists him at ILOG (S9 p. 1; S17). They include the MCF separator and root-node tuning (PE-09, PE-33).
- Gurobi-address commits: 2014 and 2016 (S17).

---

## 9. Failures, abandoned directions and negative results

- **F-1. Learned branching (about 2000).** His CS master's thesis applied neural networks to learn branching strategies inside SIP (S1 p. ix, [stated]). No publication was found; the thesis bibliography does not list it (S1 pp. 393ff.). His next branching work (2002) is statistics-based. [inferred] An abandoned or unpublished direction.
- **F-2. History branching's machinery dropped (2002 → 2004).** Classes, separate strong-branching histories and dynamic scaling factors give way to one reliability parameter (S3 pp. 6–8; S4 pp. 6–7). [practice]
- **F-3. The supplied-optimum protocol dropped (2004)**, with a reason (S4 p. 8). [practice]
- **F-4. Conflict analysis lost time on feasible MIPs (2005)** and became a net gain only with limited effort and aging (S6 p. 15; S1 pp. 5, 179–181). [practice]
- **F-5. Delayed restarts failed (2007)**, and the thesis says other criteria would be needed (S1 p. 163). [practice]
- **F-6. Wrong answers removed features (2008)**: the variable-bound MIR (83d0d3f01). An earlier fix closed a bug that could accept infeasible solutions (da753ab89, 2006). [practice]
- **F-7. Gurobi presolve reductions that do not pay**, listed in PE-30 and C-06 (co-authored).
- **No rejected papers, retractions or errata were found.** Crossref shows no update or erratum records for his DOIs (S22). Rejection histories are not public for these venues.

---

## 10. Early versus final versions

- **ZR 02-32 (Oct 2002) → ZR 04-13 (May 2004) → ORL 2005 (not read).** Renamed from history to reliability branching and simplified (F-2). The protocol changed (C-01), and so did the test-set rule (C-02). The baseline moved from CPLEX 7.5 to 9.0 and the hardware from a 750 MHz to an 833 MHz Alpha (S3 p. 10; S4 p. 8).
- **ZR 05-19 (Aug 2005) → thesis Ch. 11 (2007).** On general MIPs the result goes from a net slowdown to a net gain of more than 10 % (S6 p. 15; S1 p. 5); see C-04. The journal version (Discrete Optimization 2007) was not read.
- **Thesis 2007 (S2) → revision 2008 (S1).** The approved copy (title page without revision dates, 418 pages) and the revised copy (426 pages; "überarbeitete Fassung: 10. Dezember 2008") have identical chapter page numbers up to the Bibliography (393). The revision adds an Index (p. 405) and moves the List of Algorithms from p. 392 to p. 391. Content changes inside chapters were not checked: the 2007 copy does not extract to text.
- **RAMP 2014 → ZR 16-44 (2016) → IJOC 2020 (abstract only).** Test set 2,974 → 3,182 models; Gurobi 5.6.3 → 6.5; time limit 10,000 → 3,600 s; brackets "[n,10k]" → "≥ n sec". Presolve off means root only in 2014 (Presolve = 0) and root plus node presolve in 2016. The measured effect moves from more than threefold to ninefold (S11 pp. 191–192; S12 pp. 3–4); see C-05.
- **Self-report checked against the record:** two years without a paper fits the ZIB-Report dates to within months (PE-06). The SCIP start in October 2002 (S1 p. 6) matches the first commit of 23 Oct 2002. The end of 2002 (S1 p. ix) is close. The sibling note records other start dates (S41, its C4); that conflict is not resolved here.

---

## 11. Code and data artifacts (what exists to inspect)

- github.com/scipopt/scip: full history from 23 Oct 2002, with his 1,303 commits (achterberg@zib.de 1,279; achterberg@gurobi.com 24). Key files: `check/` (harness), `src/scip/debug.c` (debug solution), `src/scip/branch_relpscost.c`, `src/scip/conflict.c`, `check/cmpres.awk`.
- MIPLIB 2003 (miplib.zib.de, co-authored) with instance origins.
- Thesis copies: ZIB OPUS docId 1112 (2008, text-extractable) and DepositOnce (2007, Type 3 fonts).
- Benchmark versions SCIP 0.90f and 0.90i: "available on request" (S1 p. 319). Whether they are archived publicly was not checked.
- Gurobi-era decks: S13, S14, S15 (public URLs; S14 and S15 carry a "Confidential" footer).

---

## 12. Cross-check with 02-methodology (say versus do; pointers only)

The claims are labelled as in S41. The practice evidence is from this note. S41's spoken sources were not re-verified here.

| S41 claim | Practice found here | Verdict |
|---|---|---|
| E-1 measure by switching off against default | PE-23 (2007, 2016) | ✅ |
| E-2 isolate the component | PE-24 (2002, 2004, 2016) | ✅ (with the protocol change C-01) |
| E-3 validate the testbed against the state of the art | PE-01 (2002–2009) | ✅ |
| E-4 explicit, rule-based test sets | §5b | ✅, except that the 2002 rule conditions on the new method (C-02) |
| E-5 machine and timing discipline | PE-18 | ✅ |
| E-6 random seeds and a consistent-win rule | none of the written artefacts read here (thesis, 2014/2016 papers, 2017/2022/2023 decks) shows seeds | ⚠️ stated only, in this note's evidence |
| I-3 generalise rules into one family | PE-04, PE-13 | ✅ |
| J-1 averages, not single instances | PE-31; yet the code history is instance-driven (PE-09) | ✅ for conclusions; single instances drive the work |
| J-2 brackets and exclusion of trivial models | PE-20, PE-21 | ✅ (Gurobi era) |
| W-1 writing beats another 10 % | PE-10 | stated; timing is consistent with the record |

---

## Contradictions (kept, not reconciled)

**C-01. Supplying the optimal solution in branching studies.**
- 2002: supplied in advance to isolate branching (S3 p. 11).
- 2004: deliberately not supplied, because finding solutions fast belongs to a good branching rule (S4 p. 8).

**C-02. Was the test set selected by the method under study?**
- 2002: only instances that SIP with history branching solves within 3,600 s (S3 p. 9).
- Later rules use CPLEX alone (S4 p. 8; S5 p. 23), either solver with and without the feature (S1 p. 320), or any release of the product (S11 p. 191; S12 p. 3).

**C-03. Which mean, and which shift.**
- 2004: the plain geometric mean is called a fair criterion (S4 p. 9).
- 2007: the plain geometric mean is shown to be dominated by small absolute changes on easy instances, and the shifted mean is used instead (S1 pp. 321–322).
- Shift values: 60 s / 1,000 nodes (script, Sept 2006) → 10 s / 100 nodes (19 Apr 2007; S1 p. 321) → 1 s / 1 node (S11 p. 191; S12 p. 3).
- Inside the thesis, the Introduction footnote and the Table 3.1 caption speak of the geometric mean (S1 pp. 2, 54), while Appendix A says the summary tables use the shifted geometric mean (S1 p. 322).

**C-04. Conflict analysis on general MIPs.**
- 2005: nodes −50 %, time +15 % (S6 pp. 1, 15).
- 2007: a time gain of more than 10 % at reasonable effort (S1 p. 5).
- SCIP versions (0.79a vs 0.90f), test sets and settings differ. Neither source explains the reversal.

**C-05. How much presolve is worth.**
- More than threefold in the [10,10k] bracket (2014: Gurobi 5.6.3, root presolve off, 10,000 s; S11 p. 192).
- Ninefold in the ≥ 10 s bracket (2016: Gurobi 6.5, root and node presolve off, 3,600 s; S12 p. 4).
- 11.4 for CPLEX with a 10,000 s limit (Achterberg–Wunderling, relayed by S12 p. 4). The 2014 paper attributes the CPLEX figure's larger size to node presolve being switched off as well (S11 p. 192).

**C-06. Defaults for features that do not help.**
- Chvátal–Gomory strengthening is neutral but stays on in Gurobi's defaults (S12 p. 12).
- Costly or harmful features are switched off: multi-row redundancy checks and dependent-row detection for MIP (S11 p. 192), pairwise presolving (b9cd8fd36), the expensive aggregation step (S1 p. 161), several heuristics (S1 p. 127).

**C-07. Thesis heuristic defaults.**
- The text says all heuristics except Octane, local branching, RINS and mutation are on (S1 p. 127).
- The captions of Tables 9.1 and 9.2 say all except Octane (S1 pp. 128–129).

**C-08. Framing against measurement.**
- SCIP is called almost competitive with commercial solvers (S1 p. 1) and comparable to them (S1 p. 6).
- Appendix C measures 63 % (0.90i) and 115 % (0.90f) slower than CPLEX 10.0.1, with CPLEX as SCIP's own LP solver (S1 p. 377).

**C-09. Unverified default inside a verified system.**
- The thesis says every chapter of Part II ends with experiments that evaluate the algorithms it discusses (S1 p. 2).
- Martin's child-selection rule was adopted without a thorough study (S1 p. 74).
- For the chip-verification solver, branching, node selection and objective variants were tried; no strong influence was found and none is tabulated (S1 p. 299).

**C-10. Author list of ZR 02-32.** The cover names Achterberg and Koch. The title page names Achterberg, Koch and Martin (S3 cover and p. 1).

**C-11. Authorship signals in the code.** Early CVS `$Id` logins (bzfpfend), the git author mapping and the `@author` headers do not use the same identity (S17). The headers and the mapping agree on Achterberg.

**C-12. A slip in his own bibliography.** The thesis cites MIPLIB 2003 in ORL as pp. 1–12 (S1 bibliography, entry [6]). Crossref and DBLP give pp. 361–372 (S22, S20).

---

## Gaps (what could not be found or verified)

**Not read (paywalled or no open copy found):**
- All journal versions: ORL 2005 and 2006; Discrete Optimization 2007 (two papers; ScienceDirect 403); MPC 2009 and 2010; IJOC 2020; CPAIOR 2008, 2009 and 2013; JEA 2021; the IPCO 2023 and Math. Program. 2025 versions of the RLT paper. Differences from the report versions read are unknown.
- Achterberg and Wunderling 2013 (S32): one WebSearch found no open copy. It is known only through S11, S12, S13 and S14.

**Not found:**
- His master's theses (CS, on neural-network branching; mathematics). No publication of the neural-network work.
- Referee reports, rebuttals, rejections or retractions. OpenReview does not apply to these venues. Crossref shows no errata (S22).
- Any CPLEX-era deck or document of his own beyond S10 (2009). His IBM-period practice is visible only through co-authored or relayed material.
- Seeds or permutations in his written benchmarks. The thesis uses single runs and reruns suspicious ones. A text search of S1, S9, S10, S11, S12, S13, S14 and S15 finds no benchmark seeds or permuted runs; the words occur only in other senses (symmetry permutations, random branching, randomly generated instances, and one typo for "seen" in S12 p. 26). The RLT paper's permutations are on the SCIP side (S16 Appendix A). Seed use is stated in the webinars reported by S41, which were not re-verified here.
- Who ran the Gurobi experiments of S16, and which slides of S15 are his.
- Whether the thesis benchmark versions (SCIP 0.90f, 0.90i) are archived publicly.

**Checked only partly:**
- The 2008 thesis revision: content changes beyond the added index (§10).
- Commit statistics: CVS-converted history, duplicated per-file commits and unreliable time zones, so commit counts are approximate, and no working-hour pattern was inferred.
- The ZR 08-29 model files at the ZIB page: link not opened.

**Not addressed here (other agents):** day-to-day supervision and code review (04), critiques (05), dated roles and transitions (06).

---

## Sources

| # | Title · author · date · location | Use | P/S |
|---|---|---|---|
| S1 | *Constraint Integer Programming* · T. Achterberg · Dr. rer. nat. thesis, TU Berlin; defended 12 Jul 2007; revised version 10 Dec 2008 · ZIB OPUS docId 1112, https://opus4.kobv.de/opus4-zib/files/1112/Achterberg_Constraint_Integer_Programming.pdf (urn:nbn:de:0297-zib-11129) | read: pp. ix–x, 1–6, 54–55, 69–74, 127–129, 161–165, 178–181, 299, 303, 319–325, 377–378, bibliography | P |
| S2 | Same thesis, approved version (2007) · DepositOnce, DOI 10.14279/depositonce-1634 (DataCite-checked) | title page and contents pages (xi–xiv) compared | P |
| S3 | "Branching on History Information" · T. Achterberg, T. Koch, A. Martin · ZIB-Report 02-32, 7 Oct 2002 · https://opus4.kobv.de/opus4-zib/files/699/ZR-02-32.pdf | read in full | P (co-authored) |
| S4 | "Branching Rules Revisited" · T. Achterberg, T. Koch, A. Martin · ZIB-Report 04-13, 5 May 2004 · https://opus4.kobv.de/opus4-zib/files/788/ZR-04-13.pdf | pp. 1–12 read; result tables skimmed | P (co-authored) |
| S5 | "SCIP – a framework to integrate Constraint and Mixed Integer Programming" · T. Achterberg · ZIB-Report 04-19, June 2004 (text dated 2 Jan 2005) · https://opus4.kobv.de/opus4-zib/files/794/ZR-04-19.pdf | §5 (pp. 22–25) read; rest skimmed | P |
| S6 | "Conflict Analysis in Mixed Integer Programming" · T. Achterberg · ZIB-Report 05-19, 3 Aug 2005 · https://opus4.kobv.de/opus4-zib/files/853/ZR-05-19.pdf | abstract, §4 (pp. 13–17) read | P |
| S7 | "MIPLIB 2003" · T. Achterberg, T. Koch, A. Martin · ZIB-Report 05-28, May 2005 · https://opus4.kobv.de/opus4-zib/files/862/ZR-05-28.pdf | pp. 1–5 read | P (co-authored; Koch corresponding) |
| S8 | "Improving the Feasibility Pump" · T. Achterberg, T. Berthold · ZIB-Report 05-42, 16 Sep 2005 · https://opus4.kobv.de/opus4-zib/files/875/ZR-05-42.pdf | pp. 1–7 read | P (co-authored) |
| S9 | "On the Effects of Minor Changes in Model Formulations" · T. Achterberg, T. Koch, A. Tuchscherer · ZIB-Report 08-29, Aug 2008 · https://opus4.kobv.de/opus4-zib/files/1080/ZR_08_29.pdf | read in full | P (co-authored) |
| S10 | "The MCF-Separator: Detecting and Exploiting Multi-Commodity Flow Structures in MIPs" · T. Achterberg, C. Raack · ZIB-Report 09-38, 30 Nov 2009 · https://opus4.kobv.de/opus4-zib/files/1159/ZR_09_38.pdf | pp. 1–3, 16–17, 21–23, 29 (concluding remarks) read | P (co-authored) |
| S11 | "Multi-Row Presolve Reductions in Mixed Integer Programming" · T. Achterberg, R. E. Bixby, Z. Gu, E. Rothberg, D. Weninger · Proc. 26th RAMP Symposium, Tokyo, 16–17 Oct 2014, pp. 181–196 · https://orsj.org/ramp/wp-content/uploads/sites/9/2021/03/paper2014_4-4.pdf | §1, §8 (pp. 190–192) read | P (co-authored) |
| S12 | "Presolve Reductions in Mixed Integer Programming" · same five authors · ZIB-Report 16-44, Sept 2016 · https://opus4.kobv.de/opus4-zib/files/6037/Presolve.pdf | §1.1, §3.4, §3.6–3.7, §4.1, §5.1, §7, §9 read | P (co-authored) |
| S13 | "Solving Mixed Integer Programs in Practice" · T. Achterberg (Gurobi) · CPAIOR 2017 Master Class, 5 June 2017 · https://cpaior2017.dei.unipd.it/slides/Achterberg.pdf. The title slide names no speaker; the attribution comes from the programme on https://cpaior2017.dei.unipd.it/ (checked with WebFetch) | read in full (81 slides) | P |
| S14 | "Combinatorial Algorithms Used Inside a MIP Solver" · T. Achterberg · SEA 2022 invited talk, slides dated 26 Jul 2022 · https://sea2022.ifi.uni-heidelberg.de/talk_achterberg.pdf | slides 1–29 and 63–65 read | P |
| S15 | "What's New in Gurobi 11.0" webinar slides · Gurobi (co-presented by F. Orozco and T. Achterberg) · PDF of 15 Dec 2023 · https://cdn.gurobi.com/wp-content/uploads/Whats-New-in-Gurobi-11.0_Webinar-slides.pdf | slides 1–14 read | P (co-presented) |
| S16 | "Efficient Separation of RLT Cuts for Implicit and Explicit Bilinear Terms" · K. Bestuzheva, A. Gleixner, T. Achterberg · arXiv:2211.13545v3, 19 Jul 2024 | abstract, §5 setup, §5.7, §6 read | P (co-authored) |
| S17 | SCIP git repository · https://github.com/scipopt/scip · blobless clone of 8 Nov 2026 (HEAD 353584f2a); his 1,303 commits 2002-10-23 to 2016-12-16; files at the commits cited by hash; `@author` headers at HEAD | examined | P (code) |
| S18 | Gurobi webinar page "What's New in Gurobi 11.0" (12–14 Dec 2023) · https://www.gurobi.com/resources/webinar-events/whats-new-in-gurobi-11-0 | speakers and titles read | observed |
| S19 | "You have to figure out who your customer is going to be – An interview with Bob Bixby" · Optima 101, Sept 2016 · https://mathopt.zib.de/Optima-Issues/optima101.pdf | p. 4 passage read | observed (S) |
| S20 | DBLP pid 71/6632 via the SPARQL endpoint (scripts/dblp_works.py), 23 records 2005–2025, fetched 2026-11-08 | metadata | S |
| S21 | OpenAlex author A5016513861 (42 works) and work records incl. repository links and abstracts, fetched 2026-11-08 | metadata, OPUS file links | S |
| S22 | Crossref API (works and author query) and Unpaywall API records for the DOIs in this table, 2026-11-08 | identifier, erratum and open-access checks | S |
| S23 | DataCite record for DOI 10.14279/depositonce-1634 | identifier check | S |
| S24 | ZIB OPUS frontdoor pages, docIds 786, 788, 849, 876, 1080, 1081, 1112, 1159, 3296 (via WebFetch) | report numbers and file names | S |
| S25 | "Branching rules revisited" · Achterberg, Koch, Martin · Oper. Res. Lett. 33(1):42–54, 2005 · DOI 10.1016/j.orl.2004.04.002 | not read (S4 read) | P (not read) |
| S26 | "MIPLIB 2003" · Achterberg, Koch, Martin · Oper. Res. Lett. 34(4):361–372, 2006 · DOI 10.1016/j.orl.2005.07.009 | not read (S7 read) | P (not read) |
| S27 | "Conflict analysis in mixed integer programming" · Achterberg · Discrete Optim. 4(1):4–20, 2007 · DOI 10.1016/j.disopt.2006.10.006 | not read (403; S6 read) | P (not read) |
| S28 | "Improving the feasibility pump" · Achterberg, Berthold · Discrete Optim. 4(1):77–86, 2007 · DOI 10.1016/j.disopt.2006.10.004 | not read (S8 read) | P (not read) |
| S29 | "SCIP: solving constraint integer programs" · Achterberg · Math. Program. Comput. 1(1):1–41, 2009 · DOI 10.1007/s12532-008-0001-1 | not read | P (not read) |
| S30 | "The Mcf-separator: detecting and exploiting multi-commodity flow structures in MIPs" · Achterberg, Raack · Math. Program. Comput. 2(2):125–165, 2010 · DOI 10.1007/s12532-010-0015-3 | not read (S10 read) | P (not read) |
| S31 | "Presolve Reductions in Mixed Integer Programming" · Achterberg, Bixby, Gu, Rothberg, Weninger · INFORMS J. Comput. 32(2):473–506, 2020 · DOI 10.1287/ijoc.2018.0857 | abstract only (OpenAlex) | P (abstract) |
| S32 | "Mixed Integer Programming: Analyzing 12 Years of Progress" · Achterberg, Wunderling · Facets of Combinatorial Optimization, Springer 2013, pp. 449–481 · DOI 10.1007/978-3-642-38189-8_18 | not read; relayed by S11, S12, S13, S14 | P (not read) |
| S33 | "Hybrid Branching" · Achterberg, Berthold · CPAIOR 2009, LNCS 5547, pp. 309–311 · DOI 10.1007/978-3-642-01929-6_23 | not read | P (not read) |
| S34 | "Constraint Integer Programming: A New Approach to Integrate CP and MIP" · Achterberg, Berthold, Koch, Wolter · CPAIOR 2008, LNCS 5015, pp. 6–20 · DOI 10.1007/978-3-540-68155-7_4 | not read | P (not read) |
| S35 | "Stronger Inference through Implied Literals from Conflicts and Knapsack Covers" · Achterberg, Sabharwal, Samulowitz · CPAIOR 2013, LNCS, pp. 1–11 · DOI 10.1007/978-3-642-38171-3_1 | metadata only | P (not read) |
| S36 | "An Exact Method for the Minimum Feedback Arc Set Problem" · Baharev, Schichl, Neumaier, Achterberg · ACM J. Exp. Algorithmics 26, 2021, 1.4:1–28 · DOI 10.1145/3446429 | abstract only | P (abstract) |
| S37 | "Efficient Separation of RLT Cuts for Implicit and Explicit Bilinear Products" · Bestuzheva, Gleixner, Achterberg · IPCO 2023, pp. 14–28, DOI 10.1007/978-3-031-32726-1_2; journal version Math. Program. 210(1):47–74, 2025, DOI 10.1007/s10107-024-02104-0 | not read (S16 read) | P (not read) |
| S38 | "MIPLIB 2010" · Koch, Achterberg et al. · Math. Program. Comput. 3(2):103–163, 2011, DOI 10.1007/s12532-011-0025-9; "MIPLIB 2017" · Gleixner et al. · Math. Program. Comput. 13(3):443–490, 2021, DOI 10.1007/s12532-020-00194-3 | metadata only; collective works, not used as his practice | P (not read) |
| S39 | ParaSCIP papers · Shinano, Achterberg et al. · CHPC 2012 (DOI 10.1007/978-3-642-24025-6_12), IPDPS Workshops 2014 (DOI 10.1109/IPDPSW.2014.174), IPDPS 2016 (DOI 10.1109/IPDPS.2016.56) | metadata only | P (not read) |
| S40 | Other works checked by identifier only: "Computation of an extractive distillation column with affine arithmetic" · Baharev, Achterberg, Rév · AIChE J. 55(7):1695–1704, 2009 · DOI 10.1002/aic.11777; "Hybrid Solving Techniques" · Achterberg, Lodi · Springer Optimization and Its Applications, 2010, pp. 169–190 · DOI 10.1007/978-1-4419-1644-0_5 | metadata only | P (not read) |
| S41 | `02-methodology.md` (sibling note, this run) | pointer for §12 only | — |

# Ambros M. Gleixner · 02 Stated methodology (what he says research should be)

| Field | Value |
|---|---|
| Researcher | Ambros M. Gleixner. Professor for discrete mathematics and operations research at HTW Berlin since 2020 and affiliated researcher in the Mathematical Algorithmic Intelligence division of the Zuse Institute Berlin (ZIB); head of the ZIB research group Mathematical Optimization Methods 2015–2023; developer of SCIP and SoPlex; first author of MIPLIB 2017; PhD TU Berlin (thesis defence 24 June 2015). Living. Facts from his homepage [S8], CV [S9] and thesis title page [S1]. |
| Dimension | Research agent 02 of 06: stated methodology. These are his claims about how solver research should be done, sorted into the seven layers of `references/research-extraction-framework.md` §一. Whether he practises them is agent 03's job; where a later paper visibly follows up a stated plan, it appears only as a one-line [practice] pointer. |
| Research date | 2026-11-08 |
| Sources consulted | 48 sources, listed under Sources: 34 primary (13 in his own voice, 21 co-authored, group or project texts) and 14 secondary, observed or metadata. WebSearch: 5 of 5 calls used; three gave usable leads (the ZIB seminar and MIP 2023 pages; the HTW project pages; the MIPLIB 2017 call and the SC20 biography). Four own-voice sources (S45–S48: the 2014 COST STSM report, the 2020 ZIB appointment news, the MIP 2021 and COW 2025 talk abstracts) were found through the URLs in the sibling note `06-trajectory.md` and read here. Everything else came from curl, two WebFetch calls (a YouTube results page that returned no results; Taylor & Francis, refused with HTTP 403), the arXiv, ORCID, OpenAlex, Crossref and DataCite APIs, and yt-dlp 2026.10.26 run through `uvx` (yt-dlp was not on PATH) with `scripts/download_subtitles.sh` and `scripts/srt_to_transcript.py`. |
| Local corpus | `references/sources/{papers,talks,essays,software,publications}` held only `.gitkeep` placeholders, so there was no user-supplied material. `private/` was not opened. |
| Saved this run | Nothing under `../sources/talks/`. The three caption transcripts (Simons 2021, MIP 2021, CO@Work 2024) were produced with the repository scripts but kept in the scratch folder `C:\Users\sr881\AppData\Local\Temp\milp-team-t1-scratch\base-skills\ambros-m-gleixner\02\subs\` (`simons2021.txt`, `mip2021.txt`, `cowork2024.txt`, plus the `.srt` files). The caption text belongs to the Simons Institute and to the channels that posted the videos, so this note paraphrases it and quotes only short fragments. Re-running `scripts/download_subtitles.sh` on the URLs in Sources stores them if the user wants local copies. |
| Blocked | DBLP (`dblp.org/pid/07/3479`) and `nbn-resolving.org` answered with a bot check (Anubis); the check was not bypassed, and ORCID plus OpenAlex served as the publication index instead. Taylor & Francis returned HTTP 403 for the 2018 OMS preface. |

## Reading guide

**Tags.**

| Tag | Meaning |
|---|---|
| [stated] | Gleixner's own voice: his single-authored thesis, talks he gave, a call he signed, a biography written for him as speaker. |
| [stated, co-authored] | Text of a paper with co-authors. It is the team's stated position and cannot be attributed to Gleixner alone. Author position is given (e.g. "Gleixner last of 3"). |
| [stated, group] | A committee, working-group or project text (MIPLIB 2017 committee, Dagstuhl working group, SCIP team of 35, an HTW project page where he is the PI). Weakest attribution of the stated kinds. |
| [practice] | A pointer only: a later paper that acts on a stated plan. Agent 03 checks these. |
| [observed] | Another person's statement about him or his group. |
| [inferred] | My reading, not his words. |

"Primary" means his own text or talk, co-authored ones included. "Secondary" means a third party's text or a metadata record.

**Voice warning.** Only thirteen sources carry his voice alone:

- the scientific report on his COST short-term scientific mission to Bologna, 31 Dec 2014 [S45];
- the 2015 PhD thesis [S1];
- his quotation in the ZIB news on his HTW appointment, 2 Oct 2020 [S46];
- the Simons Institute talk, 30 March 2021 [S2];
- the MIP Workshop 2021 talk [S3] and its abstract [S47];
- the first-person abstract of his COW 2025 talk (Aussois, 9 Jan 2025; Hoen listed as co-author) [S48];
- the CO@Work 2024 opening overview, shared with Milena Petković [S4];
- the MIPLIB 2017 call for contributions, 11 November 2016, signed by him on behalf of the initiative [S5];
- the SC20 presenter biography, 2020 [S6]; it is written in the third person, and that he supplied it is [inferred];
- the ZIB seminar page "Algorithmic Mixed-Integer Programming", undated [S7];
- his homepage [S8];
- his CV of July 2017 [S9].

Most of his papers after 2016 are first-authored by others (e.g. Eifler, Hoen, Sofranac, Mexi, van Doornmalen) or are large team reports. He is first author of 4 of his 48 arXiv preprints: circle packing 2017, structure-aware presolving 2019, limited-precision oracles 2019, PaPILO 2022 (arXiv API [S40]). Weigh [stated] items above [stated, co-authored] ones, and those above [stated, group].

**Quotation policy.** Four sources carry Creative Commons licences and are quoted verbatim with page numbers:

- MIPLIB 2017 [S10] (CC BY 4.0);
- Eifler and Gleixner in Mathematical Programming [S11] (CC BY 4.0);
- the Dagstuhl report 18081 [S19] (CC BY 3.0);
- the MIP Workshop 2023 competition preprint [S18] (CC BY 4.0 on arXiv).

All other sources are under copyright: the thesis (DepositOnce rights statement "In Copyright"), the talk captions, the arXiv preprints under the default non-exclusive licence, and the web pages. For those, this note gives faithful paraphrases marked "[paraphrase]" and puts only short verbatim fragments in quotation marks.

**Captions.**

- The Simons talk [S2] has an uploaded, human-made English caption track.
- The MIP 2021 talk [S3] and the CO@Work 2024 opening [S4] have only YouTube automatic captions. The recogniser garbles names: "skip" = SCIP, "ripple"/"mipple" = MIPLIB, "cathy bolter" = Kati Wolter, "qs of x" = QSopt_ex, "whip"/"mib" = MIP. Quotations from [S3] and [S4] are caption text, not speaker-checked.
- Timestamps are hh:mm:ss of the YouTube video.

**Page numbers.**

- Thesis [S1]: printed page numbers.
- MIPLIB 2017 [S10]: journal pages 443–490 (journal page = PDF page + 442).
- [S11]: journal pages 793–812 (journal page = PDF page + 792).
- Dagstuhl [S19]: report pages 64–87.
- Preprints: section numbers, or arXiv PDF page.

---

## 0. Claims repeated three or more times (the real beliefs)

| # | Claim (faithful paraphrase) | Count | Where and when | Voice |
|---|---|---|---|---|
| R1 | Mixed (hybrid) precision is the master design rule. Do the expensive work in fast floating-point arithmetic, and spend exact rational arithmetic only where correctness is decided: corrections, critical decisions, final verification. | 8 | STSM report §2 (2014) [S45]; Thesis p.3 (2015) [S1]; Gleixner & Steffy §1.3 (2019) [S13]; Simons 01:04 (2021) [S2]; MIP 2021 c.00:21 (ASR) [S3]; Eifler & Gleixner p.794 (2021/2023) [S11]; Eifler & Gleixner SIAM J. Optim. abstract (2023/2024) [S26]; Hoen & Gleixner §4 (2024/2025) [S17] | 2 single-authored texts, 2 talks, 4 co-authored; 2014–2025 |
| R2 | Computational experiments are for understanding why an algorithm behaves as it does, not for a race to the fastest time. | 5 | Thesis p.10 (2015, citing Hooker 1995) [S1]; Simons 01:25 (2021) [S2]; the same "insights into the computational behavior" sentence in the Simons and MIP 2021 abstracts [S37, S47] and in Eifler & Gleixner p.793 [S11]; Sofranac, Gleixner & Pokutta §2.3 (2021) [S20]; ZIB seminar goal (undated) [S7] | 2 own voice, 3 co-authored or teaching text |
| R3 | Average running times with the shifted geometric mean, and give the reason: it measures relative differences, and the shift stops tiny running times from dominating. | 6 | Thesis pp.10–11 [S1]; MIPLIB 2017 p.444 fn.1 [S10]; Simons 01:28 [S2]; Eifler & Gleixner p.801 [S11]; PaPILO §3.1 [S15]; SCIP 8.0 §2 [S21] | rationale in the thesis and the talk; elsewhere a protocol line |
| R4 | Compare only on the subset where the comparison means something: drop trivial instances and instances on which every variant times out, and say why an exclusion does not bias the result. | 5 | Thesis p.3 fns 11–14 and p.14 [S1]; Simons 01:42–01:44 [S2]; MIP 2021 00:11–00:12 (ASR) [S3]; Eifler & Gleixner pp.808–809 [S11]; SCIP 8.0 §2.2 [S21] (group) | own voice and co-authored |
| R5 | Performance variability is real. Use several seeds or row/column permutations, treat each instance–seed pair as one observation, and test significance, because a mean alone can mislead. | 6 | Thesis pp.11–12 and p.147 [S1]; Dagstuhl 3.33 p.83 and 4.2 p.85 (2018) [S19]; MIPLIB 2017 p.478 (named as a limitation) [S10]; MIP 2021 00:11 (three seeds, ASR) [S3]; Eifler & Gleixner pp.801, 807 [S11]; PaPILO §3.1 [S15] | own voice, co-authored, group |
| R6 | Benchmarks and comparisons must be fair, balanced and transparent, and must not be over-read. Average benchmark performance does not choose a solver for an application, simplistic comparisons mislead, and like must be compared with like. | 6 | MIPLIB 2017 pp.445–446, 465–467, 478, 485 [S10]; MIPLIB call 2016 [S5]; Dagstuhl 4.2 p.85 [S19]; Simons 01:11 and 02:10 [S2]; Eifler & Gleixner p.809 [S11]; MIP 2023 competition §3 [S18] | own voice, co-authored lead, group |
| R7 | SAT solving is the model for rigour and tooling. MIP results should come with certificates that a simple independent checker can verify (proof logging), and SAT and SMT tools such as delta debugging should be carried over to MIP. | 7 | VIPR §1 (2016/2017) [S12]; Chvátal paper §1 (2018/2022) [S14]; Simons 01:44–02:08 (2021) [S2]; Eifler & Gleixner p.795 [S11]; van Doornmalen et al. §1 (2023) [S22]; Hoen, Oertel, Gleixner & Nordström §1 (2024) [S23]; MIP-DD §1 (2024) [S16] | 1 own talk, 6 co-authored; 2016–2024 |
| R8 | There is no fundamental roadblock. An exact MIP solver can stay within a constant factor of floating-point solvers; the remaining gap is the supplementary techniques not yet made exact, which must be added one by one. | 3 | Simons 01:48–01:49 [S2]; MIP 2021 00:26–00:27 (ASR) [S3]; Eifler & Gleixner pp.795, 809–810 [S11] | 2 talks, 1 co-authored; all 2021–2023 |
| R9 | Exactness matters most where the answer is used as a proof or must be exactly feasible: mathematics itself (computer-assisted proofs of conjectures), verification (chip design), and feasibility checks such as fair capacity allocation in gas networks. For most applications limited precision is fine. | 6 | STSM report §1 (2014) [S45]; VIPR §1 [S12]; Chvátal paper §1 [S14]; MIP 2021 Q&A 00:28–00:29 (ASR) [S3]; Eifler & Gleixner p.794 [S11]; Hoen & Gleixner §1 [S17] | 1 report, 1 talk, 4 co-authored; 2014–2025 |
| R10 | Usability is a research criterion. Rigorous methods should become out-of-the-box tools, heuristics should be judged by time to first solution and primal integral, and the code should be released. | 5 | Thesis p.173 [S1]; Simons 01:37–01:38 and 01:49 [S2]; MIP 2021 00:24–00:25 and 00:27 (ASR) [S3]; Eifler & Gleixner pp.794, 810 [S11]; MIPLIB 2017 call (model files) [S5] | own voice and co-authored |
| R11 | The most important outcome is extending what can be solved at all, more than the mean speed-up. | 4 (one document) | Thesis abstract p.i, p.3, §7.5 pp.171–172, p.174 (2015) [S1] | single-authored, but all in one document, so weaker than a claim repeated across years |
| R12 | Build methods inside state-of-the-art solvers (SCIP, SoPlex, PaPILO), test them on heterogeneous, practice-relevant benchmark sets, and release them openly. | ≥5 | Thesis p.2 and pp.5–6 [S1]; SC20 biography (2020) [S6]; Simons 00:00–00:01 and 01:49 [S2]; Eifler & Gleixner p.795 [S11]; PaPILO §1 [S15]; MODAL SynLab project text (2020–2023) [S31] | own voice, co-authored, project text |
| R13 | Generalise: turn structure found in applications into structure-aware algorithms that make generic solvers faster and more accurate. | 4 | Thesis p.2 (aim to "improve the performance of general-purpose algorithms") [S1]; SC20 biography [S6]; MODAL SynLab text [S31]; structure-aware presolving abstract (2019) [S25] | own voice, project text, co-authored |

---

## 1. Research taste (what is worth doing, what is a good result)

**1.1 Exactness as a personal standard, set against the field's priority on speed.** [stated] primary. Repeated across 2015–2021, and held together with speed (see C2).

- Simons 2021, 00:02:21–00:02:50 [S2], [paraphrase]: in the classical MIP community the driving force has been speed rather than being "100% exactly correct". Numerical stability is still high on the agenda, and the solvers are "amazingly stable" on the ill-conditioned data thrown at them. His "personal interest is also to be even more strict" in the mathematical sense of exactness, with exact and certifiable answers.
- The 2015 thesis is titled "Exact and fast algorithms for mixed-integer nonlinear programming". Its conclusion, p.173 [S1] [paraphrase], defines "exact" as rigorous in Neumaier's sense: proven results despite rounding errors.
- SC20 biography, 2020 [S6]: his main interest is "structure-specific algorithms that help to improve generic solvers", and the sentence ends with "both in terms of speed and accuracy". Speed and accuracy are named together.
- Era: 2015 PhD at ZIB; 2020 new HTW professor still leading SCIP development; 2021 a virtual seminar during the pandemic.

**1.2 Rigour modelled on SAT (R1/R7).** [stated] and [stated, co-authored] primary.

- Simons 2021, 02:07:58–02:08:12 [S2] [paraphrase]: in MIP "we are very much in the beginning". The methodology available in SAT and pseudo-Boolean solving is "an inspiration for me" to improve the situation.
- Eifler & Gleixner 2023, p.795 [S11] (CC BY; Gleixner second of 2): "The overarching goal and contribution of this research is to extend the computational practice of MIP to the level of rigor that has been achieved in recent years, for example, in the field of satisfiability solving [35], while at the same time retaining most of the computational power embedded in floating-point solvers."
- Eifler, Gleixner & Pulaj (arXiv 1809.01572, §1) [S14] [paraphrase]: SAT has settled open questions in discrete mathematics and has standards for proof logging and solver-independent verification. By comparison, "exact IP software with verifiable results is still in its infancy".

**1.3 Mathematics itself as a use case of exact optimization (R9).** [stated, co-authored] primary.

- Chvátal paper §1 [S14] [paraphrase]: work on optimization algorithms and software is usually motivated by real-world applications, and this overshadows their value for "answering questions in mathematics itself".
- Eifler & Gleixner 2023, p.794 [S11]: "Some of these approaches are forced to rely on floating-point solvers because the availability, the flexibility, and most importantly the computational performance of MIP solvers with numerically rigorous guarantees is currently limited. This makes the results of these research efforts not as strong as they could be."
- MIP 2021 Q&A, 00:28:50–00:29:20 [S3] (ASR) [paraphrase], asked when exactness is critical:
  - numerically difficult MIPs where floating-point solvers give inconsistent results;
  - experimental mathematics, where you "really want to be sure" that an IP is infeasible;
  - verification problems such as chip design.

**1.4 A good result extends what can be solved (R11).** [stated] primary, 2015; four times in one document.

- Thesis abstract p.i [S1]: the new methods are said, "most importantly", to let him "solve problems which could not be solved before", because of numerical difficulty or limited computing resources.
- p.3 and §7.5 (pp.171–172): solving more instances is introduced with "Even more importantly", after the running-time reductions.
- p.174: he says the methods "extend the scope of LP and MINLP as tools in practice".

**1.5 Usability as part of quality (R10).** [stated] primary.

- Thesis p.173 [S1] [paraphrase]: the guiding motivation was to make high-precision LP "an out-of-the-box technique" by improving efficiency.
- Simons 2021, 01:37–01:38 [S2] [paraphrase]: heuristics barely change time to optimality but cut the time to the first feasible solution. That makes the exact solver more useful in practice.
- Eifler & Gleixner 2023, p.794 [S11]: "The motivation for this choice is less to reduce the total solving time, but rather to improve the usability of the exact MIP code in practical settings where finding good solutions earlier may be more relevant than proving optimality eventually."

**1.6 Computational craft knowledge is under-documented.** [stated] primary, single occurrence.

- Simons 2021, 00:51:40–00:53:06 [S2] [paraphrase], answering the host's question which "handbook of MIP-solving" to read:
  - for theory there are good books, e.g. *Integer Programming* by Conforti, Cornuéjols and co-authors (DOI 10.1007/978-3-319-11008-0, checked in Crossref);
  - the tricks inside practical solvers must be gathered from publications, "and some things are not even published";
  - a good start is Achterberg's 2007 thesis (DOI 10.14279/depositonce-1634, checked in DataCite), but it is not complete today;
  - "I'm not aware of a handbook of computational MIP." He calls writing one a worthwhile project.
- [inferred] He treats unpublished solver know-how as a gap in the literature, not as a trade secret to keep.

**1.7 Open code that is also fast.** [stated] primary, 2 occurrences.

- Simons 2021, 00:00:53 [S2]: replying to the host, he says SCIP is the fastest solver whose source code you can obtain and read [paraphrase].
- SC20 biography [S6]: SCIP "today provides the fastest MIP solver openly available in source code".

**1.8 Optimization as a practical key technology.** [stated] primary, single occurrence. ZIB news on his HTW appointment, 2 Oct 2020 [S46]: "Mathematical optimization today is a key technology in many areas of technology and business." [paraphrase of the rest]: its models and algorithms make the best use of limited resources, so its relevance will keep growing. He looks forward to teaching it at HTW and "developing it further with the students".

---

## 2. Problem choice (where problems come from, why now, when to stop)

**2.1 "Why now" arguments.** [stated] and [stated, co-authored] primary.

- Thesis pp.1–2 (2015) [S1] [paraphrase]:
  - the gap between MIP and MINLP solvers is not only theoretical complexity, because extensive computational research in global optimization started only in the 1990s, while the Dantzig–Fulkerson–Johnson travelling-salesman work dates back to 1954;
  - given that historical offset, he sees "good reason to believe" that substantial progress is within reach.
- MIPLIB call, 11 Nov 2016 [S5] [paraphrase]: six years after MIPLIB 2010, solver and hardware progress had made several instances too easy. "New challenges are needed!"
- MIPLIB 2017, p.444 [S10]: "It was because of this development that the MIPLIB 2010 benchmark set was no longer considered to sufficiently reflect the frontier of new challenges in the field".
- Exact MIP: the 2013 framework of Cook, Koch, Steffy and Wolter (MPC 5:305–344, DOI 10.1007/s12532-013-0055-6, checked in Crossref) is called "the last milestone achievement" in the Simons abstract [S37] and in Eifler & Gleixner p.793 [S11]. It lacked the supplementary techniques of modern solvers, and that gap is presented as the reason to act.

**2.2 Attack the component that decides correctness or speed.** [stated] primary.

- STSM report, 31 Dec 2014, §1–2 [S45] [paraphrase]:
  - MIP is a key technology for energy and utilities, and of limited precision he writes that "for the majority of applications this is perfectly satisfactory";
  - some applications need exact answers, e.g. feasibility problems in the fair distribution of gas-network capacities among traders;
  - the mission's goal was to test efficiently whether the integer assignments of floating-point MIP solvers are reliable, "because for many applications these determine the implementation of a solution in practice";
  - the tool was his own exact LP work, to be integrated into SCIP.
- Thesis p.2 [S1] [paraphrase]: in MINLP solvers numerical instabilities arise in the LP relaxations, which he calls "Somewhat counterintuitively". Improving LP accuracy is therefore "both a necessary and effective step" towards stable MINLP solvers.
- Simons 2021, 00:30–00:33 [S2] [paraphrase]:
  - fast LP re-solves (warm start, about 100 times fewer simplex iterations deep in the tree than at the root, on a test set he measured "quite a while ago") are "one of the sometimes overlooked reasons why MIP works";
  - for a significant set of MIPs, LP solving is the bottleneck;
  - pressed by the host, he qualifies this: "It's not an exclusive bottleneck at all."
- Eifler & Gleixner 2023, p.794 [S11]: presolving was chosen first "motivated by the fact that presolving has been identified by several authors as one of the components—if not the component—with the largest impact on the performance of floating-point MIP solvers".
- Simons 2021, 00:39:45 [S2] [paraphrase]: turning presolving off costs about as much as turning cutting planes off, both in speed and in number of instances solved.

**2.3 Gaps in the available software are research problems.** [stated, co-authored] primary.

- PaPILO (arXiv 2206.10709 abstract; Gleixner first of 3) [S15] [paraphrase]: PaPILO was motivated by the lack of presolving implementations that are (a) solver-independent, (b) parallel and (c) multiprecision.
- VIPR, §1 [S12] [paraphrase]: presented as the first general MIP certificate-verification software made available to the community.
- MIP-DD, abstract [S16]: the first open-source delta debugger for MIP.

**2.4 Settings that benchmarks leave out.** [stated, co-authored] primary. MIP 2023 competition §1 [S18] (CC BY; Gleixner third of 8; he chaired the competition committee [S35]): "Traditional benchmarks for MILPs often focus on the performance of optimizing a given instance from scratch. In many practically relevant settings, however, MILP solvers are used to repeatedly solve a series of similar instances of the same type and only slight modifications of the input data."

**2.5 Directions he judged unpromising.** [stated] primary. Simons 2021 [S2].

- Branching on general disjunctions, 02:19:14–02:20:16 [paraphrase]:
  - current solvers do not do it;
  - the degrees of freedom are huge and there is no good way to limit them, "We need better ideas.";
  - added constraints slow the LP, whereas variable branching shrinks it, so it "doesn't seem to pay off in practice";
  - several papers have tried it: "I also have one."
  - Which paper he means is not stated. A candidate is "Branching on Multi-aggregated Variables" (Gamrath, Melchiori, Berthold, Gleixner, Salvagnin; CPAIOR 2015, LNCS pp.141–156, DOI 10.1007/978-3-319-18008-3_10, checked in Crossref) [inferred, unconfirmed].
- Automatic binarization of integer variables, 00:49:57–00:51:20 [paraphrase]: SCIP has such a presolver, but it is off by default because it does not seem good as a default; whether it helps depends on the application. In modelling he recommends binary formulations, for a "good and a bad reason": the theoretical reason is stronger formulations, the practical one is that solvers are developed towards the binary case.

**2.6 Applied problems at a university of applied sciences (2020–).** [stated, group] primary: HTW project pages with Gleixner as PI [S31]. The texts are the projects', not necessarily his own words.

- MODAL SynLab (1 Apr 2020 – 31 Mar 2023; BMBF; partners ZIB, FICO, GAMS, Gurobi, Siemens, SAP):
  - the goal is the "mathematische Generalisierung von anwendungsspezifischen Fortschritten" achieved in the MODAL research campus;
  - the focus is exact methods for discrete–continuous optimization combined with machine learning;
  - results are "in quelloffenen Softwaretools gebündelt".
  - My translation, not his words: mathematical generalisation of application-specific advances; results bundled in open-source software tools.
- VetOpt (2022–2023, commissioned by felmo GmbH): scheduling veterinarians in the city; models, scalable algorithms and efficient software.
- DaKoDi (2026–2029, BMBF; Charité, Labor Berlin, Vivantes, ZIB): explainable diagnosis rules for sepsis, derived as "explizite, transparente logische Regeln" with mixed-integer and global optimization.
- HOTSTEEL (2026–2029, EFRE/ProFIT): planning for energy-efficient logistics in steel production.
- [inferred] At HTW, problem choice runs through local industrial and clinical partners. The research-campus project restates the ZIB pattern of distilling general solver methods from applications (R13).

---

## 3. Idea generation (where ideas come from)

**3.1 Mixed precision as the master idea (R1).** [stated] and [stated, co-authored] primary. Count 7, 2015–2025.

- Thesis p.3 [S1]: "Its computational efficiency rests on its mixed-precision nature". The hard part, a sequence of related LP solves, runs in fast floating point; the cheap part, error computation and correction, runs in exact rational arithmetic [paraphrase].
- Gleixner & Steffy (arXiv 1912.12820, §1.3; Gleixner first of 2) [S13]: the successful methods use inexact computation where it gives useful information, but "exact computation is used for critical decisions or to validate final solutions".
- Simons 2021, 01:01:34 and 01:04:31 [S2] [paraphrase]: floating-point solvers are "not that bad all the time" and return exact discrete information, the basis. The theme of "using different levels of precision" to build a fast algorithm runs through all the fastest exact methods.
- MIP 2021, c.00:21:23 (ASR) [S3] [paraphrase]: the "hybrid precision paradigm": use "as much cheap floating point arithmetic as you can", and exact rational arithmetic as little as possible but as much as necessary.
- Eifler & Gleixner 2023, p.794 [S11]: for heuristics, "we follow a hybrid-precision scheme".
- Eifler & Gleixner, SIAM J. Optim. 34:742–763 (2024) abstract [S26] [paraphrase]: avoid large-scale symbolic computation whenever possible and use safe directed rounding instead; "we continue to leverage this paradigm".
- Hoen & Gleixner (CPAIOR 2025) §4 [S17] [paraphrase]: most branch-and-bound node decisions can be verified in fast floating-point arithmetic.

**3.2 Reuse the floating-point machinery, then repair exactly.** [stated] primary. Simons 2021, twice; MIP 2021; restated in [S11].

- Simons 2021, 01:38:08–01:41:35 [S2] [paraphrase]:
  - they did not write rational heuristics; floating-point heuristics run as in a floating-point solver, and their candidates are repaired by fixing the rounded integers and solving the remaining LP exactly, with buffering;
  - not only because "we were lazy", but because in-solver heuristics should spend a small, bounded effort, so a sub-MIP heuristic in rational arithmetic is "not called for";
  - the low success rate on numerically difficult instances may later justify "dedicated rational heuristics".
- Eifler & Gleixner 2023, p.794 [S11]: "Primal heuristics are exclusively executed on the floating-point approximation of the rational input data."

**3.3 Transfer from SAT, SMT and pseudo-Boolean solving (R7).** [stated, co-authored] primary.

- VIPR §1 (Cheung, Gleixner, Steffy; IPCO 2017) [S12] [paraphrase]: the certificate is a sequence of statements checked one by one with few inference rules, an approach "similar to that for verification of unsatisfiability proofs for SAT formulas".
- van Doornmalen, Eifler, Gleixner & Hojny (arXiv 2311.03877, §1) [S22]: supplementing results with proofs "has long been the standard in the SAT community". The paper extends a pseudo-Boolean proof system to MIP.
- Hoen, Oertel, Gleixner & Nordström (CPAIOR 2024, DOI 10.1007/978-3-031-60597-0_20) §1 [S23]: the SAT community "dealt with this problem in a remarkably successful way" by requiring proof logging. MIP presolve is certified with the VeriPB tool.
- MIP-DD §1 [S16] [paraphrase]: delta debugging, a "hypothesis-trial-result" loop, succeeded in SAT and SMT, and this is its first application in mathematical optimization.
- [practice] The collaboration with Jakob Nordström's proof-logging group predates these papers: Devriendt, Gleixner & Nordström, "Learn to relax", Constraints 2021, DOI 10.1007/s10601-020-09318-x (in ORCID [S39]).

**3.4 Theory to explain what works in practice.** [stated, co-authored] primary.

- Gleixner & Steffy, abstract [S13] [paraphrase]: complexity analyses assume exact arithmetic or count bits, while implementations use limited precision. The limited-precision LP oracle model is meant as "a foundation for understanding and analyzing the behavior of the methods" that work best in practice for exact LP.
- Same paper, §3 [S13] [paraphrase]: an optimal basis is usually reached after very few refinements, far earlier than the worst-case bound. So the algorithm should not rely on a priori bounds but "check the optimality of the basis early".
- Same paper, §6 [S13] [paraphrase]: the theory leaves open which variant performs best empirically, and the experiments are designed to answer that.
- MIPLIB 2017, p.443 [S10], quoting Hoffman et al. (1953): "[many] conjectures about the relative merits of the three methods by various criteria could only be verified by actual trial". The paper adds that this "seems to hold to an even greater extent today."

**3.5 Turn folklore into measurement.** [stated] and [stated, co-authored] primary. The same question spans 2014 to 2025.

- STSM report §4 (2014) [S45] [paraphrase]: the first outcome was a definition of the "reliability of integer assignments" that is "amenable to computational analysis". Round and fix the integer values, solve the remaining LP exactly, and get three cases: feasible with the same objective, feasible with a different objective, or infeasible in exact arithmetic. The analysis was to give a clearer picture of "the price of precision within MIP solving" and of the benefits of exact computation.
- COW 2025 abstract (Aussois, 9 Jan 2025; first person, with Hoen) [S48] [paraphrase]: even when the final answer is correct, a question remains: "Was the reasoning of the branch-and-bound solver justified", i.e. can each decision be turned into a certificate valid in exact arithmetic?
- Hoen & Gleixner, §1 and §4 [S17] [paraphrase]: it is widely accepted that floating-point MIP solvers are numerically robust, but no one had checked how many individual branch-and-bound decisions are correct in exact arithmetic. Their study is meant to "quantify the widely accepted belief" and to use floating-point solvers as a "grey box" for exact solving.
- Sofranac, Gleixner & Pokutta (CP 2021, DOI 10.4230/LIPIcs.CP.2021.52; Constraints 2022, DOI 10.1007/s10601-022-09338-9) §1–2.3 [S20] [paraphrase]: tolerance-based stopping makes fair comparison of propagation codes hard, so they built an algorithm-independent progress measure. They add that "gaining insight into the behavior of these algorithms is a motivation in itself".

**3.6 Read an experiment's losses as the next idea.** [stated] primary. MIP 2021, 00:15:44–00:16:45 (ASR) [S3] [paraphrase]:

- switching the exact LP solver from QSopt_ex to SoPlex lost as many numerically difficult instances as the first step had gained;
- QSopt_ex can boost precision while SoPlex relies on double precision working;
- so "a combination of these two" might be very beneficial: "this is an interesting outcome of this experiment".

The same plan appears in Eifler & Gleixner 2023, p.810 [S11]. [practice] It was realised in Eifler, Nicolas-Thouvenin & Gleixner, "Combining Precision Boosting with LP Iterative Refinement for Exact Linear Optimization", INFORMS J. Comput. 37:933–944 (2025), DOI 10.1287/ijoc.2023.0409 (checked in Crossref) [S24].

**3.7 Generic code that makes the exact variant cheap.** [stated] primary. Simons 2021, 01:33:08 [S2] [paraphrase]: they "templatized" the arithmetic type of the new presolve library (PaPILO) from the start, so plugging in GMP yields a rational presolver automatically. MIP 2021 (ASR) [S3] says the same.

**3.8 Use optimization on your own research process.** [stated, co-authored] primary.

- MIPLIB 2017, p.466 [S10]: "It seems quite natural to formulate the selection task as an optimization problem."
- p.485 [S10]: a variant of the benchmark-selection MIP later computed a minimal update of the benchmark set when two instances had to be replaced.

---

## 4. Experiments and execution (design, baselines, iteration)

**4.1 Purpose: controlled scientific testing (R2).** [stated] primary.

- Thesis p.10 [S1] [paraphrase]: his interest is not purely competitive testing, i.e. which algorithm is fastest, but to "analyze the reasons for their behavior by controlled scientific testing". He cites Hooker (1995), "Testing heuristics: We have it all wrong", J. Heuristics 1:33–42, DOI 10.1007/BF02430364 (checked in Crossref).
- Simons 2021, 01:24:50–01:25:10 [S2] [paraphrase], introducing the result tables: the point is not "we've got so much faster" but what was done to get faster. "The motivation is not benchmarking, but getting insight in what costs time and whatnot."

**4.2 Where to implement and what to test on (R12).** [stated] primary. Thesis p.2 [S1] [paraphrase]: the new methods "shall be implemented as part of state-of-the-art solvers" and tested on "heterogeneous sets of benchmark instances with relevance in practice".

**4.3 Averages (R3).** [stated] primary.

- Thesis pp.10–11 [S1] [paraphrase]:
  - the arithmetic mean is dominated by the largest terms;
  - the geometric mean measures relative differences;
  - a positive shift avoids over-representing differences among very small values.
- Simons 2021, 01:28:01 [S2] [paraphrase]: shifted geometric means are "pretty standard in MIP solving". A plain geometric mean over-weights very short runs, which "are actually not the most important ones", so one adds one or two seconds.
- [stated, co-authored] The shift is always reported: 1 s in MIPLIB 2017 p.444 fn.1 [S10]; 0.001 s and 100 nodes in Eifler & Gleixner p.801 [S11]; 1 in PaPILO §3.1 [S15].

**4.4 Variability and significance (R5).** [stated] primary.

- Thesis pp.11–12 [S1] [paraphrase]:
  - a mean can hide whether an improvement is consistent or comes from a few large speed-ups while most instances get worse;
  - performance variability means considerable changes caused by small, seemingly insignificant modifications;
  - "performance variability looms even larger on mixed-integer nonlinear programs";
  - hence a one-sided Wilcoxon signed-rank test on log-ratios of shifted values (SciPy, Pratt treatment of zeros, p = 5%);
  - caveat: significance is "independent from the magnitude of change", so a tiny but consistent change can be significant yet practically irrelevant.
- Thesis p.147 [S1] [paraphrase]: a 5.7% mean speed-up was not significant because it came from five instances. That, he writes, "shows the importance of significance testing". Individual instances were rerun with ten constraint permutations, so that the effects could be attributed to the method and "not just random noise".
- Dagstuhl 18081, §3.33 p.83 (Vigerske & Gleixner) [S19], CC BY: "By applying permutations to the order of variables and constraints, we exploit the extend of performance variability, including its dependence on the choice of optimality tolerance and whether the primal-dual integral is less prone to variability than solving time." (Wording verbatim, including "extend".)
- Dagstuhl 18081, §4.2 p.85 [S19], working-group conclusions in a report he co-edited: "the need to incorporate experimentation on permuted models as has become standard in the MIP community".
- [stated, co-authored] Eifler & Gleixner 2023:
  - p.801 [S11]: "All experiments to evaluate the new code are run with three different random seeds, where we treat each instance-seed combination as a single observation."
  - p.807 fn.2: "Unfortunately, such phenomena can occur since randomization is not perfect: many of the decisions inside the solver are still fully deterministic and thus not affected by a change in the random seed."

**4.5 Choosing the subset that is compared (R4).** [stated] primary.

- Thesis p.3 fns 11–14 [S1] [paraphrase]: every headline number names its subset:
  - excluding instances solved in under two seconds;
  - instances on which at least one solver takes at least two seconds;
  - instances solvable with and without OBBT but not by both in under 100 seconds;
  - instances solvable by at least one of two branching rules.
- Thesis p.14 [S1] [paraphrase]: excluding 40 LP instances "does not introduce a bias", because no tested SoPlex version solves them; they are kept for the QSopt_ex comparison.
- Simons 2021, 01:42:57–01:43:52 [S2] [paraphrase]: gaps are compared only where both codes have a finite gap. The MIPLIB 2017 benchmark set holds many instances hopeless even for floating-point solvers, so double timeouts are excluded, and the speed-up rises from a factor of two to over six.
- MIP 2021, 00:11:30–00:12:00 (ASR) [S3] [paraphrase]: hopeless instances are thrown out, and instances where both versions time out are removed because "that just dilutes the results".
- Eifler & Gleixner 2023, p.808 [S11]: "Here we only consider instances that were solved to optimality by both versions since timeouts would bias the results in favor of the certificate."

**4.6 Baselines: like with like.** [stated] primary.

- Simons 2021, 01:11:25 [S2] [paraphrase]: the 2013 framework's slowdown factor of two to four was measured "of course" against a plain branch-and-bound, without cuts, conflict analysis, presolving or heuristics. That makes it weaker evidence than it looks.
- MIP 2021, 00:10:43 (ASR) [S3] [paraphrase]: to compare with the original framework they reused "the same test sets" as the 2013 paper (FPEasy, NumDiff) and added a modern, larger one (MIPLIB 2017 benchmark).
- Eifler & Gleixner 2023, p.809 [S11]: floating-point SCIP is also run "in a reduced setting with all features disabled that are not yet present in the current exact SCIP version". The conclusion drawn: "in terms of solvability, the gap between the exact and inexact seems to be mostly due to the currently still missing solving methods."
- Simons 2021, 02:10:39 [S2] [paraphrase]: comparing pseudo-Boolean and MIP solvers is "not fully fair", because pseudo-Boolean solvers are exact and floating-point MIP solvers are not. The fairer comparison is against exact SCIP.

**4.7 Timing and hardware hygiene.** [stated] primary and [stated, co-authored].

- Thesis p.10 [S1]: only one job per cluster node, to "safeguard against a potential mutual slowdown of parallel processes" that distorts timings [paraphrase].
- MIPLIB 2017, p.480 [S10]: solver results are not reported directly because "not all runs could be performed exclusively on the same hardware, and should hence not be reported in a way that could be confused for an actual benchmark."

**4.8 Reproducibility and availability.** [stated] primary and [stated, co-authored].

- Thesis p.10 [S1] [paraphrase]: the code is public in SoPlex and SCIP, and the exact versions and log files used were "archived in order to facilitate reproducibility of the results".
- Eifler & Gleixner 2023, p.795 [S11]: "The resulting code is freely available for research purposes as an extension of SCIP 7.0".
- MIP 2021, 00:27:11 (ASR) [S3]: code on GitHub and in future releases.
- MIPLIB 2017, p.448 [S10]: "For the first time, all contributions were required to be submitted under a license in order to explicitly grant the right of redistribution, among others." Submissions were committed to a public git repository.
- [practice] Exact solving became a SCIP solving mode in SCIP Optimization Suite 10.0 (arXiv 2511.18580 abstract) [S27].

**4.9 Debugging the solver.** [stated, co-authored] primary.

- MIP-DD (Hoen, Kamp, Gleixner; arXiv 2405.19770; IJOC, DOI 10.1287/ijoc.2024.0844) §1 [S16] [paraphrase]:
  - assertions and debug solutions miss bugs, because checks are sparse, tolerance bugs pass assertions, and dual reductions may legitimately cut off optimal solutions;
  - the remedy is to shrink the failing instance while preserving reproducibility of the error.
- Its abstract [S16] proposes the same tool for performance bottlenecks, which "could very well benefit from simple adversarial instances".
- VIPR §6 [S12] [paraphrase]: approximate certificates "could be used for debugging solvers" or for measuring numerical violations. This 2017 idea runs ahead of the 2024–2025 debugging and decision-checking papers [S16, S17] [inferred].

**4.10 Ablation by switching components off.** [stated] primary. Simons 2021, 00:39:45 [S2] [paraphrase]: a component's impact is shown by turning it off and on. Throughout the talk each component (dual bounding, exact LP, presolving, heuristics, certificates) is added in its own step with its own table. Thesis-era work did the same per component: Berthold, Gleixner, Heinz & Vigerske, "Analyzing the computational impact of MIQCP solver components", NACO 2:739–748 (2012), DOI 10.3934/naco.2012.2.739 (in ORCID [S39]; not read).

**4.11 Heuristics inside a solver fail fast.** [stated] primary, one talk, twice. Simons 2021, 00:45:10–00:45:22 and 01:40:17 [S2] [paraphrase]:

- inside a MIP solver a heuristic should not be as aggressive as possible;
- it should realise when it has a chance and when not, and "fail fast";
- it must be effective on average, with total heuristic effort capped at a share of solving time.

---

## 5. Judging results (when to believe, when to stop, negative results)

**5.1 Pick the metric that fits the component.** [stated] primary.

- Simons 2021, 01:37:00–01:38:02 [S2] and MIP 2021, 00:24:27–00:24:51 (ASR) [S3] [paraphrase]: primal heuristics barely move time to optimality, as in floating-point solvers. They improve time to first solution and the primal integral, which "makes the solver much more usable".
- Eifler & Gleixner p.794 [S11]: the same, quoted under 1.5.

**5.2 State the remaining gap plainly.** [stated] primary, 3 times in 2021–2023.

- Simons 2021, 01:48:21 [S2] [paraphrase]: roundoff-error-free MIP solving "is still far from competitive" with floating-point solvers, but he hopes the audience finds it a worthwhile area.
- MIP 2021 (ASR) [S3]: the same.
- Eifler & Gleixner, p.810 [S11]: "We also observed, however, that the performance gap to floating-point solvers is still large."

**5.3 Distrust single numbers and simplistic comparisons.** [stated, co-authored] and [stated, group].

- MIPLIB 2017, p.445 [S10]: "It should be emphasized that the benchmark set we have scientifically constructed is designed for the purpose of comparing the overall performance of general purpose solvers on a wide-ranging set of instances. Average performance on this set is not a suitable criterion to decide which MIP solver to use in a particular application scenario." The paper adds that each of the eight solvers was fastest on at least one instance.
- Dagstuhl 18081, §4.2 p.85 [S19] (CC BY): "the affirmation that conducting fair benchmarks between different solvers remains inherently difficult and users of solver software should not rely on simplistic comparisons."

**5.4 Numerical ambiguity disqualifies an instance as a benchmark.** [stated, co-authored] primary.

- MIPLIB 2017, p.465 [S10]: "Since all MIP solvers rely on floating-point arithmetics and use feasibility tolerances, the definition of “the optimal objective value” for a problem instance is ambiguous." The next sentence: "Instances exhibiting such ambiguity are not suitable for benchmarking". 328 instances (5%) were removed for this reason.
- MIPLIB 2017, p.467 [S10]: feasible instances without a finite optimum are excluded because "there is currently no clear consensus on the expected behavior and output of MIP solvers" in that case. Infeasible instances "are deliberately not excluded".
- Eifler & Gleixner, p.809 [S11]: instances feasible within tolerances but infeasible in the exact sense are discarded before comparing exact and floating-point SCIP.

**5.5 Check a surprising number, then explain it.** [stated] primary. Simons 2021, 01:35:19–01:36:15 [S2] [paraphrase]:

- whether exact presolving finds more or fewer reductions than floating-point presolving is not clear a priori;
- the counts on the easy set were identical: "This is not an error in the table.";
- on numerically difficult instances exact presolving is "a bit more conservative and more correct", because floating-point presolving probably made incorrect reductions.

**5.6 Confidence through checking, not suspicion.** [stated, co-authored] primary. VIPR §1 (2016/2017) [S12] [paraphrase]:

- "a skeptical attitude that borders on paranoia" towards solvers is neither healthy nor practical;
- the point of verification is to find and reduce errors and raise confidence, not distrust;
- certificates should be "as simple to verify as possible if they are to be convincing".
- Simons 2021, 01:53:38–01:53:57 [S2] repeats the design goals [paraphrase]:
  - a certificate format should be expressive;
  - it should be simple, so that "checking should not require a sophisticated code where that could contain bugs itself";
  - it should be general, for all MIPs and not one problem class.
- He later proposes "sort of a hierarchy of certificate formats" (02:05:05): rich formats the solver can print quickly, converted by tools into a plain format that can be checked with more certainty [paraphrase].

**5.7 Benchmarks are snapshots and must drive progress.** [stated, co-authored] primary, MIPLIB 2017 [S10].

- p.478: "Representing current solver performance may overly favor instances that are tractable by current solver technology. This is opposed to one main goal of the MIPLIB project, which is to provide a test bed that drives solver development forward." The selection objective was therefore tilted towards hard instances, and the paper admits: "The concrete choice of the square root was empirically motivated."
- p.478: "the goal of representing computational difficulty in the reduced benchmark set cannot be achieved perfectly and is not even well-defined", because performance variability and parallel scalability were not captured and correctness was only approximate. "However, we hope that it helps to avoid unintentionally and unconsciously introducing a bias both towards instances of a particular difficulty and towards any of the solvers."
- p.467: the requirement that every benchmark instance be solved by at least one solver "avoids the situation of MIPLIB 2003, for which four instances still remain unsolved 15 years after the release of the test set."
- p.485: "As future work, we propose to assess the performance representability of the benchmark set from hindsight".

### Failures, losses and abandoned directions he reported

| # | What he reported | Source | Tag |
|---|---|---|---|
| F1 | His minimum-cover concept (from the Undercover work with Berthold) gave COVER branching, whose results "failed to be statistically significant". It was outperformed by NLSCORE branching. The conclusion admits "The most effective of the new branching rules, however, were hybrid rules" that refine existing scores. | Thesis §7.5 pp.171–172, p.174 [S1] | [stated], 2015 |
| F2 | Branching on general disjunctions does not pay off in solvers, and he has a paper on it (not identified, see 2.5). | Simons 02:19–02:20 [S2] | [stated], 2021 |
| F3 | "Despite all the care that was taken to exclude numerically critical instances from the benchmark set, problematic numerical properties of the two instances neos-5075914-elvire and neos-3754224-navua remained undetected during the selection process." Both were replaced in an updated benchmark set. | MIPLIB 2017 pp.485–486 [S10] | [stated, co-authored] |
| F4 | Heuristics in exact SCIP: "the first disappointing thing" was that solving time was barely affected. On numerically difficult instances the floating-point heuristics' success rate is low. | Simons 01:37, 01:41 [S2] | [stated] |
| F5 | Switching to SoPlex as exact LP solver lost numerically difficult instances. | MIP 2021 00:15 (ASR) [S3] | [stated] |
| F6 | Parallel exact presolving with 20 threads cut the mean exact presolving time only from 0.25 to 0.14 (units not stated in the talk), "not at all a great result" (worth having for outliers). | Simons c.01:34 [S2] | [stated] |
| F7 | Part of the speed-up was attributed to a probable performance bug in the old framework, not to new algorithms: "A portion of the improvement in solving time is most likely due to these previously unnecessary bounding calls." | Eifler & Gleixner p.803 fn.1 [S11] | [stated, co-authored] |
| F8 | Certificate printing roughly doubles solving time (Simons) or adds 22–56% (paper). Asked about certificate size: "Sorry, I don't have any statistics on that." | Simons 01:44–01:46 [S2]; Eifler & Gleixner p.808 [S11] | [stated] |
| F9 | Tightening the feasibility tolerance only partly removes incorrect pruning on subproblems that are infeasible in exact arithmetic. | Hoen & Gleixner §4 [S17] | [stated, co-authored] |
| F10 | Within MINLP, high-precision LP is "only a first step". Feasibility tolerances that are not coordinated between MINLP and LP solver can cause undefined behaviour, and coordinating them in a complex code base is "a nontrivial task" [paraphrase with fragments]. | Thesis p.174 [S1] | [stated] |
| F11 | The 2014 Bologna mission (host Andrea Lodi, with Luca Fabbri) planned a joint journal paper: "We hope to finalize this submission until autumn 2015." It also promised a SCIP constraint handler to be "made publically available within one of the next releases of the SCIP Optimization Suite". [practice] His ORCID works list (93 groups, read 2026-11-08) [S39] has no paper with Lodi or Fabbri on this topic. The question reappears ten years later in Hoen & Gleixner [S17, S48]. Whether the constraint handler shipped was not checked. | STSM report §4–5 [S45] | [stated], 2014; outcome [practice] |

No rejected paper or retracted claim was found (see Gaps).

---

## 6. Writing and talks

This layer is thin: no essay or advice on writing was found. What exists:

- **Make process decisions transparent.** [stated, co-authored] MIPLIB 2017, p.445–446 [S10]: "Despite the heavy use of quantitative methodology, the overall process inherently requires many manual decisions and heuristic choices. … All of these decisions have a high impact on the final result. Hence, in the remainder of this article we try to describe the collection and selection of MIPLIB 2017 at a sufficiently high level of technical detail in order to make this process transparent to the reader." And p.485: "this formalization of the selection criteria has served to increase the transparency of the selection process."
- **Say how far a result reaches.** [stated, co-authored] MIPLIB 2017, p.485 [S10]: "the final result is clearly only one of many possible and justified outcomes. However, we believe that the collection and benchmark sets presented in this paper are a profound attempt to provide the research community with test sets that represent the versatility of MIP."
- **Tell the audience which numbers matter.** [stated] Simons 2021, 01:24:40 [S2] [paraphrase]: the tables part is where it is "easy to get lost", so he will point out the important numbers. MIP 2021, 00:09:42 (ASR) [S3]: he gives "a big preview" of the overall result before the step-by-step tables, and announces "we have not added any revolutionary techniques here" for a step that was mostly tuning.
- **Teaching format.** [stated] ZIB seminar page [S7] (undated; lists him as "Dr.", so before the 2020 professorship [inferred]):
  - students study the papers behind today's solvers and give a 5-minute talk mid-term and a 40-minute final talk;
  - they write a 5–8 page LaTeX summary on which they get feedback;
  - the stated aim is that students become "competent to analyze their computational behavior".
- **Teaching format, CO@Work 2024.** CO@Work 2024 opening, 00:02:07–00:02:28 and 00:14:41 (ASR) [S4] [paraphrase]:
  - afternoons are for getting "our hands dirty": "this is how you learn by implementing all these things on your own laptop";
  - the exam covers tutorials, the computational challenge and the industry talks, because "we want to bring Theory into practice".

---

## 7. Research organisation (platforms, community, collaboration, students)

**7.1 The solver as shared research infrastructure.** [stated] and [stated, group].

- Thesis pp.5–6 [S1] [paraphrase]: his implementations went into SoPlex and SCIP. SoPlex became a standard plug-in of COBRApy because of its reliability on multiscale biology models, and its 80-bit and exact versions were put on the NEOS Server.
- SCIP 8.0 paper (ACM TOMS 2023, DOI 10.1145/3585516; 35 authors) §1 [S21] [paraphrase]: the framework's design centres on extension and customisation, so that researchers can test their own components inside a general branch-cut-and-price solver.
- SC20 biography [S6]: "Since 2015, he has been leading the development of the optimization framework SCIP".

**7.2 Community instruments: libraries, competitions, workshops, editing.** [stated] and [stated, co-authored]; roles verified in the cited pages.

- MIPLIB call 2016 [S5] [paraphrase]:
  - MIPLIB "has been a crucial driver for the impressive progress" of MIP;
  - wanted: challenging instances from all of OR and combinatorial optimization, "ideally ones which have been built to model real-world problems";
  - for the first time model files are requested, for richer information;
  - the call is signed by Gleixner on behalf of an initiative of ASU, COIN-OR, CPLEX, FICO, Gurobi, MIPCL, MOSEK, NuOPT, SAS and ZIB.
  - The call gives 28 February 2017 as deadline; the paper (p.448) says submissions were accepted until 1 August 2017.
- MIPLIB 2017, p.444 [S10]: a committee of 21 researchers, "including representatives of the development teams of nine MIP solvers", steered the compilation.
- MIP Workshop 2023 computational competition: Gleixner chaired the competition committee [S35]. The paper [S18], §1, says the competition was established "to encourage and provide recognition to the development of novel practical techniques". On scoring (§3): "In our mind, this scoring framework allows for nuanced evaluation, rewarding efficiency while maintaining fairness across different methodologies." Rules were set "to close loopholes for the competition, such as intentionally ignoring a time limit to gather more information or aborting unpromising runs to keep the score low."
- Dagstuhl Seminar 18081 (18–23 Feb 2018), co-organised with Bonami, Linderoth and Misener [S19]. The executive summary (pp.64–65) dedicated "a break-out session discussing best practices for conducting scientifically-meaningful computational experiments in MINLP".
- Other roles, from [S9], [S29] and [S36]:
  - technical editor of Mathematical Programming Computation since 2015, per the 2017 CV [S9];
  - co-organiser of the NeurIPS 2021 ML4CO competition [S29];
  - member of the team that won the 2026 Land-Doig MIP Competition with CHAP [S36].

**7.3 Collaboration across solver communities.** [stated] and [observed].

- Simons 2021 [S2] was a SAT-community seminar (host Jakob Nordström). Gleixner's 2021 talk [S2], the 2023–2024 proof-logging papers [S22, S23] and MIP-DD [S16] all turn to the SAT, SMT and pseudo-Boolean communities.
- [observed] Host's introduction, Simons 2021, 00:00:53–00:01:30 [S2] [paraphrase]: Nordström says the group has been feeding talent into Gurobi and CPLEX. Gleixner agrees that many former SCIP developers now work at Gurobi, CPLEX, FICO and newer solver companies, and calls the field active, "with Asian players entering the market".

**7.4 Group, funding and partners (resource context).**

- CV 2017 [S9], stated in a self-written CV: his ZIB group had "2 senior researchers, 10 research assistants, and 4 student assistants". He was PI of industry cooperations with SAP and Siemens and of the BMWi project BEAM-ME on energy-system models.
- ZIB project text for HPO-NAVI [S34] (head Thorsten Koch; Gleixner a member) argues that software used to produce results "should be regarded as scientific output as well". This is the project's institutional position, not a statement attributed to him [stated, group].

**7.5 Students.** No statement of supervision philosophy, lab rules or advice to PhD students was found (see Gaps). The only teaching material is the two course formats under layer 6.

### Era and resource context

| Period | Position and resources | Methods emphasis stated then |
|---|---|---|
| 2008–2015 | ZIB research assistant in the SCIP/SoPlex team; MATHEON and the MODAL research campus; a COST short-term mission to Bologna (2014); a Xeon cluster run one job per node [S1, S9, S45] | exact LP through iterative refinement; MINLP bound tightening and branching; Wilcoxon testing |
| 2015–2023 | Head of the ZIB group Mathematical Optimization Methods (16 people in 2017); leads SCIP development from 2015; MPC technical editor; industry PI roles; HPC energy models with up to 700 million nonzeros (BEAM-ME) [S6, S9, S25] | MIPLIB 2017 curation; VIPR certificates; exact MIP revival; GPU propagation |
| 2020– | Professor at HTW Berlin, an applied-sciences university; affiliated with the ZIB MAI division; projects with local industry and clinics [S8, S31] | applied projects; proof logging with SAT researchers; delta debugging; GPU–CPU heuristics (2026) |

---

## Contradictions

Kept as found; not reconciled.

- **C1. How trustworthy floating-point solvers are.**
  - Emphasis on robustness: of limited precision, "for the majority of applications this is perfectly satisfactory" (STSM report, 2014 [S45]); "amazingly stable" (Simons 2021, 00:02:42 [S2]); their practical success "bears witness to their overall numerical robustness" (COW 2025 abstract [S48]). In 2024/2025 the mature solvers' handling of numerics is "overall very robust" and the study's results "quantify the widely accepted belief" (Hoen & Gleixner §1, §4 [S17]).
  - Emphasis on compromise: roundoff "compromises the results of virtually all fast mixed integer programming solvers" (MIP 2021 abstract [S47], same in the Simons abstract [S37]); "their theoretical promise of global optimality is compromised by roundoff errors" (Eifler & Gleixner p.794 [S11], 2021/2023); IP results are "compromised by roundoff errors" (Chvátal paper §1 [S14], 2018).
  - Both emphases sit inside one programme. The 2024/2025 paper turns the question into a measurement, and its framing moves from building exact solvers towards checking floating-point decisions a posteriori ("grey box") [inferred].
- **C2. Exactness against speed and near-optimality.**
  - His own position: thesis title "Exact and fast" (2015); SC20 "speed and accuracy" (2020); Simons 2021: his personal interest is to be "even more strict" than the community's need for speed.
  - The Dagstuhl 2018 energy working group (led by Martin and Liers, reported in the report he co-edited [S19], §4.1 p.84): "the mathematical MINLP community potentially overemphasizes research on proving optimality. However, success of MINLP in engineering applications rather requires near-optimal answers quickly and robustly."
  - Eifler & Gleixner 2023 p.794 [S11] argue for heuristics because "finding good solutions earlier may be more relevant than proving optimality eventually."
  - The Dagstuhl line is a group conclusion, not his; it is recorded because it stands in a document he edited.
- **C3. What benchmarking is for.**
  - MIPLIB 2017's stated aim is "a meaningful and fair comparison of the average performance of MIP solvers" (p.445 [S10]).
  - His own experiments are "not purely competitive testing" (thesis p.10 [S1]) and "The motivation is not benchmarking" (Simons 01:25 [S2]).
  - These are two stated roles for computation, a standard yardstick for the field and controlled experiments for insight. The MIPLIB paper limits its own yardstick: it is no basis for picking a solver for an application.
- **C4. The price of exactness: forecast against measurement.**
  - Simons 2021, 01:49:02–01:49:21 [S2] [paraphrase]: he expects the 2013 slowdown of two to four to "definitely" hold when state-of-the-art techniques are added, because most are heuristic and can run in floating point.
  - Eifler & Gleixner 2023, p.809 [S11]: exact SCIP is 8.1 times slower than default floating-point SCIP and 3.9 times slower than a reduced version on instances solved by all three. The paper explains the gap to the earlier factor 3 by "a more challenging set of instances".
  - The forecast matches only the reduced baseline. This is for agent 03.
- **C5. Headline numbers drift between versions of one result.**
  - Simons abstract, March 2021 [S37]: 6.6× speed-up and 2.8 times as many instances solved on MIPLIB 2017.
  - MIP 2021 talk (ASR) [S3]: "about an order of magnitude" and three times as many.
  - Eifler & Gleixner, Math. Program. 2023 abstract [S11]: 10.7× and 2.9×.
  - Presumably different code versions and runs; no explanation of the difference was found.

## Gaps

- **No essay, interview, blog, oral history or advice-to-students text was found.** Three of the five WebSearch calls targeted this: an interview query, a ZIB/HTW/MIP-workshop domain query, and an Optima query. YouTube searches through curl found only the three talks used here and talks by co-authors. So layers 6 (writing) and 7 (supervision) rest on course pages and practice traces, not on stated method.
- **Not read:**
  - the 2018 OMS preface (Gleixner, Kirches, Mitchell, Ralphs; Optim. Methods Softw. 33(3):419, DOI 10.1080/10556788.2018.1459255, metadata checked in Crossref), refused with HTTP 403;
  - the single-authored ZIB-Report 12-36, "Factorization and update of a reduced basis matrix for the revised simplex method" (2012), behind a bot check at nbn-resolving.org;
  - the SCIP Optimization Suite 5.0 and 6.0 reports, which list him first;
  - "Iterative refinement for linear programming" (INFORMS J. Comput. 28(3):449–464, 2016, DOI 10.1287/ijoc.2016.0692), closed access; its content is covered by thesis chapter 2;
  - the MIPLIB 2010 paper (MPC 3:103–163, 2011, DOI 10.1007/s12532-011-0025-9);
  - QPLIB (MPC 2019, DOI 10.1007/s12532-018-0147-4);
  - the ML4CO report beyond its author list;
  - the 2012 NACO component-impact paper;
  - talk titles in the 2017 CV with no slides or recordings found, e.g. "Filtered performance diagrams for analyzing MINLP solver performance" (Kyushu, 2014) and "Potentials and Limitations of Parallel Computing for Mixed-Integer Linear Energy System Models" (Coimbra, 2016).
- **No recorded talk after 2021 in his own voice** was found besides the 2024 CO@Work organisational opening; for COW 2025 only the abstract exists [S48]. Talks at ISMP 2024 or MIP 2024–2026 were searched for and not found.
- **No rejected papers, referee exchanges or retractions** were found; MIP venues have no public reviews.
- **Unresolved points:**
  - the "I also have one" paper on general-disjunction branching (2.5);
  - whether the SC20 biography was written by him;
  - the exact year of the ZIB seminar page.
- **Not consulted:** Google Scholar (the profile id DUFnBNcAAAAJ is on his homepage [S8]); not needed for this dimension.

## Sources

Licence notes matter for quoting: CC BY items are quoted verbatim, the rest only paraphrased or in short fragments.

**His own voice (primary)**

- S1. A. M. Gleixner, *Exact and fast algorithms for mixed-integer nonlinear programming*, PhD thesis, TU Berlin, 2015 (defence 24 June 2015). DOI 10.14279/depositonce-4938 (OpenAlex). Read: abstract, introduction, §1.3–1.4, §6.4 p.147, §7.5, chapter 8. Rights: In Copyright. Primary.
- S2. A. Gleixner, "Exact Mixed-Integer Programming over the Rational Numbers", Simons Institute, workshop "Beyond Satisfiability", Zoom, 30 Mar 2021. Video https://www.youtube.com/watch?v=JMZUJlWfMT8 (8495 s; human-made English caption track). Read in full, scratch transcript `simons2021.txt`. Primary.
- S3. A. Gleixner, "Exact Mixed Integer Programming" (status update), MIP Workshop 2021 (online), given 25 May 2021 per [S47]. Video https://www.youtube.com/watch?v=rKyUcsjXFHs (channel Mixed Integer Programming, uploaded 2021-05-27, 1858 s; automatic captions only). Read in full, `mip2021.txt`. Primary.
- S4. A. Gleixner and M. Petković, "Organization and Overview of the Summer School", CO@Work 2024, ZIB. Video https://www.youtube.com/watch?v=o2BK_XEGcn4 (uploaded 2024-09-17, 1078 s; automatic captions). Read in full, `cowork2024.txt`. Primary.
- S5. A. Gleixner, "MIPLIB 2017: Call for Contributions to the 6th Mixed Integer Programming LIBrary", Opt-Net mailing list, 11 Nov 2016. https://listserv.zib.de/pipermail/opt-net/2016-November/001275.html. Primary.
- S6. SC20 presenter page "Ambros Gleixner" (biography), 2020. https://www.sc20.supercomputing.org/presenter/index-uid=907093.html. Primary (author of the bio presumed, [inferred]).
- S7. ZIB, seminar page "Algorithmic Mixed-Integer Programming", lecturer Dr. Ambros Gleixner, undated. https://www.zib.de/training-and-outreach/algorithmic-mixed-integer-programming. Primary.
- S8. Homepage, https://www.zib.de/userpage/gleixner/ (footer © 2008–2022): positions, research statement, links, Scholar id. Primary.
- S9. Curriculum Vitae, updated 31 July 2017, https://www.zib.de/userpage/gleixner/gleixner.pdf. Primary.

**Co-authored and group texts (primary)**

- S10. A. Gleixner, G. Hendel, G. Gamrath, T. Achterberg, M. Bastubbe, T. Berthold, P. Christophel, K. Jarck, T. Koch, J. Linderoth, M. Lübbecke, H. D. Mittelmann, D. Ozyurt, T. K. Ralphs, D. Salvagnin, Y. Shinano, "MIPLIB 2017: data-driven compilation of the 6th mixed-integer programming library", *Math. Program. Comput.* 13:443–490 (2021). DOI 10.1007/s12532-020-00194-3. CC BY 4.0. Read: §1–3.1, §4.1, §4.6–5.1, §5.4–5.6, §6–7. Primary (lead author with 15 co-authors).
- S11. L. Eifler, A. Gleixner, "A computational status update for exact rational mixed integer programming", *Math. Program.* 197:793–812 (2023; online 2022). DOI 10.1007/s10107-021-01749-5; IPCO 2021 version DOI 10.1007/978-3-030-73879-2_12. CC BY 4.0. Read: §1–2, §4 setup, §4.6–4.7, §5, footnotes. Primary.
- S12. K. K. H. Cheung, A. Gleixner, D. E. Steffy, "Verifying Integer Programming Results", IPCO 2017, LNCS pp.148–160. DOI 10.1007/978-3-319-59250-3_13; arXiv 1611.08832. Read: abstract, §1, §6. Primary.
- S13. A. Gleixner, D. E. Steffy, "Linear Programming using Limited-Precision Oracles", *Math. Program.* (2019/2020). DOI 10.1007/s10107-019-01444-6; arXiv 1912.12820. Read: abstract, §1, remarks in §3, opening of §6. Primary.
- S14. L. Eifler, A. Gleixner, J. Pulaj, "A Safe Computational Framework for Integer Programming applied to Chvátal's Conjecture", *ACM TOMS* (2022). DOI 10.1145/3485630; arXiv 1809.01572. Read: abstract, §1–2 opening. Primary.
- S15. A. Gleixner, A. Hoen, L. Gottwald, "PaPILO: A Parallel Presolving Library for Integer and Linear Programming with Multiprecision Support", *INFORMS J. Comput.* (2023). DOI 10.1287/ijoc.2022.0171; arXiv 2206.10709. Read: abstract, §1, §3.1–3.2, §5. Primary.
- S16. A. Hoen, D. Kamp, A. Gleixner, "MIP-DD: Delta Debugging for Mixed-Integer Programming Solvers", *INFORMS J. Comput.* (2025/2026). DOI 10.1287/ijoc.2024.0844; arXiv 2405.19770. Read: abstract, §1. Primary.
- S17. A. Hoen, A. Gleixner, "Analyzing the Numerical Correctness of Branch-and-Bound Decisions for Mixed-Integer Programming", CPAIOR 2025, LNCS pp.35–50. DOI 10.1007/978-3-031-95976-9_3; arXiv 2412.14710. Read: abstract, §1, §4. Primary.
- S18. S. Bolusani, M. Besançon, A. Gleixner, T. Berthold, C. D'Ambrosio, G. Muñoz, J. Paat, D. Thomopulos, "The MIP Workshop 2023 Computational Competition on Reoptimization", *Math. Program. Comput.* (2024). DOI 10.1007/s12532-024-00256-w; arXiv 2311.14834v2 (CC BY 4.0). Read: §1, §3, §4. Primary.
- S19. P. Bonami, A. M. Gleixner, J. Linderoth, R. Misener (eds.), "Designing and Implementing Algorithms for Mixed-Integer Nonlinear Optimization (Dagstuhl Seminar 18081)", *Dagstuhl Reports* 8(2):64–87 (2018). DOI 10.4230/DagRep.8.2.64. CC BY 3.0. Read: executive summary, §3.33, §4.1–4.2. Primary (co-edited; group conclusions).
- S20. B. Sofranac, A. Gleixner, S. Pokutta, "An Algorithm-Independent Measure of Progress for Linear Constraint Propagation", CP 2021 (DOI 10.4230/LIPIcs.CP.2021.52) and *Constraints* (2022, DOI 10.1007/s10601-022-09338-9); arXiv 2106.07573. Read: abstract, §1, §2.3. Primary.
- S21. K. Bestuzheva et al. (35 authors), "Enabling Research through the SCIP Optimization Suite 8.0", *ACM TOMS* (2023). DOI 10.1145/3585516; arXiv 2303.07101. Read: abstract, §1, §2.1–2.2. Primary (group).
- S22. J. van Doornmalen, L. Eifler, A. Gleixner, C. Hojny, "A proof system for certifying symmetry and optimality reasoning in integer programming", arXiv 2311.03877 (2023). Read: abstract, §1. Primary.
- S23. A. Hoen, A. Oertel, A. Gleixner, J. Nordström, "Certifying MIP-Based Presolve Reductions for 0–1 Integer Linear Programs", CPAIOR 2024. DOI 10.1007/978-3-031-60597-0_20; arXiv 2401.09277. Read: abstract, §1. Primary.
- S24. L. Eifler, J. Nicolas-Thouvenin, A. Gleixner, "Combining Precision Boosting with LP Iterative Refinement for Exact Linear Optimization", *INFORMS J. Comput.* 37:933–944 (2025). DOI 10.1287/ijoc.2023.0409; arXiv 2311.08037. Read: abstract, §1. Primary ([practice] pointer).
- S25. A. Gleixner, N.-C. Kempke, T. Koch, D. Rehfeldt, S. Uslu, "First Experiments with Structure-Aware Presolving for a Parallel Interior-Point Method", OR Proceedings 2019 (2020). DOI 10.1007/978-3-030-48439-2_13; arXiv 1908.00796. Abstract only. Primary.
- S26. L. Eifler, A. Gleixner, "Safe and Verified Gomory Mixed-Integer Cuts in a Rational Mixed-Integer Program Framework", *SIAM J. Optim.* 34:742–763 (2024). DOI 10.1137/23M156046X; arXiv 2303.12365. Abstract only. Primary.
- S27. C. Hojny et al. (34 authors), "The SCIP Optimization Suite 10.0", arXiv 2511.18580 (2025). Abstract only. Primary (group; [practice] pointer).
- S28. G. K. Tjusila et al. (8 authors, Gleixner fifth), "CHAP: A Hybrid GPU-CPU Heuristic for MIP", arXiv 2605.05086 (2026). Abstract only. Primary (trajectory context).
- S29. M. Gasse et al., "The Machine Learning for Combinatorial Optimization Competition (ML4CO): Results and Insights", arXiv 2203.02433 (2022), NeurIPS 2021 competition track. Author list and opening only (Gleixner among 22 co-organisers). Primary (group).
- S30. Works named in this note only by their identifiers, from ORCID [S39] and Crossref (metadata only; counted with the secondary sources): NACO 2012 component-impact paper (DOI 10.3934/naco.2012.2.739), "Learn to relax" (DOI 10.1007/s10601-020-09318-x), MIPLIB 2010 (DOI 10.1007/s12532-011-0025-9), QPLIB (DOI 10.1007/s12532-018-0147-4), "Branching on Multi-aggregated Variables" (DOI 10.1007/978-3-319-18008-3_10, Crossref), "Iterative refinement for linear programming" (DOI 10.1287/ijoc.2016.0692), OMS preface (DOI 10.1080/10556788.2018.1459255, Crossref). Not read. Metadata only.
- S31. HTW Berlin research-catalogue project pages with Gleixner as PI: MODAL SynLab (https://www.htw-berlin.de/forschung/online-forschungskatalog/projekte/projekt/?eid=3135), VetOpt (eid=3153), DaKoDi (eid=3802), HOTSTEEL (eid=3895). Fetched 2026-11-08. Primary (project texts; authorship not certain).

**Secondary, observed and metadata**

- S32. HTW Berlin, Wirtschaftsmathematik "Forschung & Praxis" page (research keywords of professors), https://wm.htw-berlin.de/forschung-praxis/. Secondary.
- S33. ZIB member page "Gleixner, Ambros, Prof. Dr.", https://www.zib.de/members/gleixner (division, group, projects). Secondary.
- S34. ZIB project page "Sustainable Infrastructures for Archiving and Publishing High-Performance Optimization Software" (HPO-NAVI), https://www.zib.de/research/projects/sustainable-infrastructures-archiving-and-publishing-high-performance (head T. Koch). Secondary (institutional).
- S35. MIP Workshop 2023 page, https://www.mixedinteger.org/2023/ (Competition Committee: "Ambros Gleixner (Chair)"; local organisation Andrés Gómez). Secondary. A search-engine summary had called him "local chair"; the page does not say so.
- S36. MIP Workshop 2026 page, https://www.mixedinteger.org/2026/ (Land-Doig MIP Competition winners incl. Gleixner, "CHAP"). Secondary.
- S37. Simons Institute talk page, https://simons.berkeley.edu/talks/exact-mip-solving (abstract, date 30 Mar 2021, 8:30–10:30 PT). Secondary (abstract presumably supplied by the speaker).
- S38. YouTube watch-page metadata for S2–S4 (titles, channels, upload dates, durations, caption tracks), fetched 2026-11-08. Metadata.
- S39. ORCID public record 0000-0003-0391-5903, works list (93 groups), https://pub.orcid.org/v3.0/0000-0003-0391-5903/works. Metadata.
- S40. arXiv API author query "Ambros Gleixner" (48 preprints, 2016-04 to 2026-07). Metadata.
- S41. OpenAlex, Crossref and DataCite records used to check DOIs, OA status and venues, including Cook, Koch, Steffy & Wolter, MPC 5:305–344 (2013), DOI 10.1007/s12532-013-0055-6; Hooker, J. Heuristics 1:33–42 (1995), DOI 10.1007/BF02430364; Conforti, Cornuéjols, Zambelli, *Integer Programming* (2014), DOI 10.1007/978-3-319-11008-0; Achterberg, *Constraint Integer Programming*, TU Berlin 2007, DOI 10.14279/depositonce-1634. Metadata.
- S42. [observed] Jakob Nordström, host's introduction and questions in S2 (statements about SCIP and the ZIB group). Secondary.
- S43. DBLP person page 07/3479: bot check, not read. Recorded for completeness.
- S44. Taylor & Francis landing page for the OMS preface: HTTP 403, not read. Recorded for completeness.

**Own-voice sources added from the sibling note's leads (primary)**

- S45. A. M. Gleixner, "Scientific Report on the STSM 'Numerically Robust Integer-Feasibility'", COST Action TD1207, 31 Dec 2014. https://cost-td1207.zib.de/sites/default/files/scientific_report_gleixner.pdf. Read in full (3 pages). Primary, single-authored.
- S46. ZIB news, "HTW Berlin enters cooperation with Zuse Institute Berlin: Cooperation starts with a professorial appointment", 2 Oct 2020 (date on the page), with a quotation by Gleixner. https://www.zib.de/news/htw-berlin-enters-cooperation-zuse-institute-berlin. Primary for the quotation; the article itself is ZIB's.
- S47. researchseminars.org, MIP Workshop 2021 talk page "Exact mixed-integer programming: a status update on MIP solving without numerical errors", A. Gleixner, 25 May 2021, 16:45–17:15 UTC (abstract; "This is joint work with Leon Eifler"). https://researchseminars.org/talk/MIP2021/8/. Primary.
- S48. A. Gleixner, A. Hoen, abstract "An a posteriori analysis of numerical correctness in LP-based branch and bound", 27th Aussois Combinatorial Optimization Workshop (COW 2025); talk Thursday 9 Jan 2025, 18:15–18:35, per the programme https://cow25.sciencesconf.org/program. Abstract: https://cow25.sciencesconf.org/601453. Primary (first person: "In this talk I will present").

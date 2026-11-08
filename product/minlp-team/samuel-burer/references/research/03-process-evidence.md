# 03 · Process evidence: what Samuel Burer actually does when he does research

> **Researcher**: Samuel A. (Sam) Burer, University of Iowa, Tippie College of Business, Department of Business Analytics. Google Scholar BScCde0AAAAJ; DBLP pid 96/4845; ORCID 0000-0001-5886-458X; homepage https://sburer.github.io/.
> **Dimension**: research agent 03 of 06, process evidence (behaviour, not statements), nuwa research-craft Phase 1.
> **Research date**: 2026-10-10.
> **Sources consulted**: 54 (44 primary, 10 secondary), listed under "Sources".
> **Identifiers checked with a tool in this run**:
> - 32 DOIs through the Crossref API (direct lookup or bibliographic search), including the publisher's correction link between the Burer & Ye paper and its 2021 correction;
> - 7 arXiv ids through arXiv abstract pages or the arXiv API, with version listings for 6;
> - 48 Optimization Online entries through his author archive, 3 abstract pages opened.
>
> **WebSearch calls used**: 1 of 2. I used it to locate a public preprint of Bonami, Günlük & Linderoth.
> **Local corpus**:
> - `references/sources/papers`, `essays` and `software` held only `.gitkeep` files. There was no user-supplied material, so nothing below is marked "from user-supplied material".
> - `sources/talks/` held four YouTube auto-caption transcripts that sibling agents saved during this run. I read three of them (the 2023 low-rank talk, the 2021 IOS plenary and a 2015 R teaching video) and quote them only as machine transcripts.
> - I saved no transcript and did not open `private/`.
>
> **Method**:
> 1. I cloned 13 public repositories of github.com/sburer into a scratch folder. For each I read the file tree, the READMEs and scripts, the full commit history (message bodies and co-author trailers) and the diffs of the key commits. I read issues and pull requests through the GitHub API.
> 2. I downloaded 23 PDFs from his site: his CV, his own copies of 21 papers and notes from `sburer.github.io/papers/`, and the SDPLR user guide. I also downloaded 8 arXiv PDFs (5 records, one of them third-party) and one third-party preprint from Optimization Online.
> 3. I extracted the text with pdftotext and read the experiment sections, footnotes and acknowledgements. A script located each quotation's page. I give the journal page where the PDF is the published version and the PDF page index for preprints.
> 4. I compared early and final versions:
>    - Optimization Online 2005 with *Math. Program.* 2008;
>    - Optimization Online 2009 with the 2011 chapter;
>    - arXiv 2303.01624 v1 and v2 with the repository fix of 2026;
>    - arXiv 2504.03996 v1, v2 and v3 with the repository commits of 2025–2026;
>    - arXiv 1802.02688v2 with the 2021 correction.
> 5. I added two third-party records: an outside benchmark that ran his code, and an outside paper on his hardest benchmark.
>
> **Tags**: [stated] = he said or wrote it (sole author, his own code comment, commit message or issue reply) · [stated-joint] = co-authored text · [practice] = what the record shows he or his team did · [observed] = what others wrote or recorded · [inferred] = my reading, which no source states. Each item also carries **P** (primary) or **S** (secondary).
> **Quoting**:
> - Words are verbatim, including typos in the sources ("empifically", "disogranized", "pencentage", "where encountered", "techiniques", "Commiting").
> - I removed line breaks and end-of-line hyphenation.
> - Mathematical symbols that pdftotext drops (σ, ≤, ‖x‖, ≈, −) are re-typed.
> - YouTube caption quotations are machine transcriptions and are marked "(machine transcript)".
> - Commit messages with a "Co-Authored-By: Claude …" trailer are marked "(AI-co-authored commit)". The wording is probably the assistant's, but the commit sits in his repository under his name, so the decision it records counts as his practice.
>
> **Relation to 06**: I used `06-trajectory.md` (written earlier in this run) only as a lead list and re-checked every item below against the primary record. Where the two files overlap (the 2021 correction, the 2504.03996 versions, the AI trailers), this file reads the item for what it shows about behaviour.

---

## 1. The evidence base at a glance

| Repository (github.com/sburer/…) | First → last commit | Commits | What it holds | Release timing relative to the paper |
|---|---|---|---|---|
| `Max-AO` | 2014-01-17 → 2014-01-20 | 6 | C heuristic for large cliques and stable sets (file `Max-AO_v0.120301.c`), a sample graph and parameter files | 12 years after the 2002 paper (*Math. Program.* 94:137–166, DOI 10.1007/s10107-002-0356-4) |
| `QuadProgBB` | 2011-09-22 → 2016-07-08 | 42 | MATLAB + C-MEX global nonconvex QP solver, platform binaries, before/after profiles, a user's hard instance with run logs and a BARON log, `todo.txt` | History starts before the Oct 2011 acceptance of Chen & Burer (2012); on GitHub from Jan 2014. The CV lists "QuadProgBB version 20120229" on the personal webpage |
| `soctrust` | 2016-05-11 → 2023-10-24 | 10 | Scripts named after paper sections (`Section_4_example.*`, `Section_5_2_example.*`, `Section_5_3_tests.m`), the instance generator `martinez.m`, saved instances and results | 3 years after Burer & Anstreicher (2013). An archive of the unsolved instances was added in 2023 |
| `ttrs` | 2016-05-12 → 2016-05-16 | 3 | Lifted-RLT code, cluster-submission scripts, instances and results for Section 5.4 | At publication of Yang & Burer (2016) |
| `grades` | 2018-04-10 | 4 | Robust-grading code (MATLAB, Gurobi), a verification script, and an AMPL "Basic" version runnable on NEOS | At submission; the README says "submitted to *European Journal on Operational Research*" |
| `BoxQP_instances` | 2019-01-30 | 4 | The 99 box-QP benchmark instances in three generations with optimal values, the seeded generator, SDPA files of two relaxations, and an `.lp` converter "Written by Tobias Achterberg (2019-01-30)" | 10–14 years after the instances were created |
| `ttrsn2` | 2024-06-06 | 4 | Re-run of the 2016 lifted-RLT code with MATLAB `R2022b` and MOSEK 10 | 8 years after the paper; purpose not stated |
| `sdplr` | 2023-10-05 → 2026-03-23 | 27 | SDPLR 1.03-beta C code: merged outside fixes (2023), then a hardening sprint with a test suite (2026) | 20 years after the 2003 paper, in the year of the 2023 Test of Time award |
| `ballconstraints` | 2023-10-28 → 2026-08-28 | 4 | Python/MOSEK experiments, a massive instance search, results, and an exact verifier for counterexamples found after publication; tag `paper_v1` | Same day as arXiv 2303.01624v2 (28 Oct 2023) |
| `submodular-tests` | 2025-11-28 → 2026-08-26 | 18 | Instance search for tightness, counterexample verification (exact and MOSEK), one script per paper table and figure | Created between arXiv v1 (Apr 2025) and v2 (Apr 2026); rebuilt in the week before v3 (Aug 2026) |
| `lorentz-positive` | 2026-09-15 → 2026-09-22 | 3 | Three-level reproduction kit, committed raw CSVs, provenance checks, manifest `paper_experiments.toml` | Same week as arXiv 2609.32017v1 |
| `ipco-2019-sdp-tutorial`, `2023-06_SIOPT` | 2019; 2023 | 5; 3 | Lecture slides; talk slides | — |

All rows are [practice, P], from the GitHub API listing and the clones read on 2026-10-10. His other public repositories are forks or non-research items: a Coursera R assignment, a GLPK interface, a list of data-science colleges, the SIAG/OPT website, an OmniFocus command-line tool and a rankings website.

**Reading of the table** [inferred]:
- **Until about 2019** he released code after publication, sometimes years later, mostly as an archive of what had been run.
- **From 2023** the code appears with the preprint or the revision.
- **From 2026** it is built so that an outsider can regenerate every number in the paper.

---

## 2. Findings by layer (framework §一)

### Layer 2 · Choosing and leaving problems (process accounts)

**2.1 The collaboration began as a way to learn each other's field, then moved to the problem class where its tool won.**

Source: the COAP 2009 best-paper note (*Comput. Optim. Appl.* 47:567–570, 2010, DOI 10.1007/s10589-010-9368-9) [stated-joint, P]. The note is unsigned, but it slips into "we" for Axioma ("the optimization team at Axioma has found that by paying a higher computational price for solving stronger relaxations, we obtain better primal solutions", p. 569), so the authors wrote at least part of it.

- **Motive**: "It was part of a collaboration mostly motivated by the desire of each author to gain a greater understanding of the other's field of expertise." (p. 567)
- **First target**: SDP relaxations of 0-1 integer programs (Burer & Vandenbussche, *SIAM J. Optim.* 16(3):726–750, 2006, DOI 10.1137/040609574; record checked, paper not read).
- **Why they left it**: "For globally optimizing linear IPs, the authors began to realize that, even with better techniques for the SDP relaxations, these relaxations could still be ineffective" (p. 568). Either the bounds were too weak, or the SDPs were slower than an IP solver's dual-simplex reoptimization.
- **New criterion**: "Hence, the next goal of the collaboration was to identify problem classes for which these SDPs relaxations would provide uniformly good bounds in a short amount of time." (p. 568)
- **The move**: "So the authors shifted their focus away from IPs to continuous problems in the form of non-convex quadratic programs (QPs)" (p. 568).
- **Context**: 2002–2007; Burer an assistant professor in a business school, Vandenbussche at UIUC and then Axioma; a two-person team.
- **Reading** [inferred]: the tool chose the problem. The test was where the SDP bound pays for itself, not which application matters most.

**2.2 He tried an extension, reported the failure in print, and in revision replaced the failure sentence with a positive result on the same problem.**

- **The failure, in v1** [stated, P]: arXiv 2303.01624v1 (2 Mar 2023; the homepage copy dated 28 Feb 2023 has the same pages), p. 4: "We also tried to apply the ideas of this paper to (TTRS) by introducing multiple artificial variables" … "However, the resulting relaxations were no tighter empirically than those already in the literature, and we were unable to make further progress specifically on (TTRS). We hypothesize that the shared geometry of balls, as represented by the reappearance of the norm ‖x‖, is critical for the approach of this paper."
- **The revision, v2** (28 Oct 2023, "Revised: October 31, 2023") [stated, P]:
  - The failure sentence is gone. p. 4 now reads: "We show empifically that our approach solves all instances of a test set from the literature."
  - A new section takes the hard TTRS instances of his 2013 paper: "We applied our relaxation R0 to the same instances and solved all 212." (p. 20)
- **Published version**: *Math. Program.* 211:157–179 (2025), DOI 10.1007/s10107-024-02076-1. Published text not read.

**2.3 He leaves quietly.**
- The last QuadProgBB commits read "Some basic clean up. Files still a bit disogranized." (ee19018, 2016-05-18) and "Update .gitignore for .log files" (2016-07-08). No later branch-and-bound solver code appears among his repositories [practice, P].
- No stated reason for stopping was found (see Gaps).

### Layer 3 · Where ideas come from (process accounts)

**3.1 Low rank: he implemented the idea the same day, measured it, and left the explanation for later.**

- **The slides** of the 2 June 2023 SIAM prize lecture (repository `2023-06_SIOPT`, `test-of-time.pdf`, slides 30, 35 and 38) [stated-joint, P]:
  - "But would it actually work in practice?" / "Can't hurt to try"
  - "Also experimented with: Restricting the rank smaller than required by theory · Dynamically updating the rank · Heuristically solving NP-hard problems using rank-2 approaches (with Y. Zhang)"
  - "Why should this work at all? In the early 2000's, this seemed challenging to answer"
- **The talk**: in the March 2023 Iowa rehearsal he reads from his saved emails of 22 May 2000 [stated, P; machine transcript]:
  - "I told him I did it I implemented it and convergence is good"
  - and a day later: "I'd been able already to streamline it and get it roughly 30 times faster so so this was you know some quick stuff that we're doing just to get it the Prototype out there and then it turned out to be it turned out to work"
- **Context**: 2000, PhD student at Georgia Tech, advisor R.D.C. Monteiro, C code.

**3.2 Numerical search comes first, then a conjecture in print, then a proof, often with a student.**

- **Burer & Anstreicher** (*SIAM J. Optim.* 23(1):432–451, 2013, DOI 10.1137/110826862; homepage preprint "Revised: November 16, 2012", p. 13) [stated-joint, P]:
  - **The conjecture**: they tested "many random instances of TRS2 with non-intersecting cuts in low dimensions" and "have always found empirically that r(TRS2) does equal v(TRS2). So we conjecture that the two values are equal when the cuts do not intersect."
  - **The intersecting case**: they give an n = 3 counterexample and check its true value with the global solver Couenne (v(TRS2) ≈ −12.9419 against r(TRS2) ≈ −13.8410; symbols re-typed).
- **The proof** [practice, P]: Burer & Yang, "The trust region subproblem with non-intersecting linear constraints", *Math. Program.* 149:253–264 (2015; received 22 Feb 2013), DOI 10.1007/s10107-014-0749-1. Its abstract: "This paper shows that the convex relaxation has no gap for arbitrary m as long as the linear constraints are non-intersecting."
- **2021 IOS plenary** (31 Mar 2021) on the switching-variable hull (Anstreicher & Burer, *Math. Program.* 188:421–441, 2021, DOI 10.1007/s10107-021-01671-w) [stated, P; machine transcript; "approved" = "proved", "hole" = "hull"]:
  - "[34:16] and what uh what kurt and i approved and this was really just reproving some results from the literature"
  - the n = 2 analogue "turns out to be false so you can just exhibit some counter examples"
  - "[34:50] … we we did a lot of computational experiments and we came up with a conjecture"
  - "[37:35] theorem turned out to be a lot of work … there's got to be a way to simplify the proof we don't know what it is at this point yet"
  - "[50:14] … for n equals two we think that if you take the non-negative ball you put in the kitchen sink and you also put in all of these locally valid cuts that i just mentioned and you actually capture the convex hole"
- **Ball paper**, arXiv 2303.01624v1 p. 14 [stated, P]: "Indeed, after extensive experimentation, this appears to always be the case, and accordingly, we offer the following conjecture".
- **Pattern** [inferred]:
  1. Re-derive the known small case in the lifted space.
  2. Ask whether the next case is simply the intersection SDP ∩ RLT.
  3. Find a counterexample.
  4. Run many random instances.
  5. State the regularity in print as a conjecture.
  6. Prove part of it later.

**3.3 MILP is his organising analogy.**
- **Title change** [stated-joint, P]: Optimization Online 2009/07/2338 is titled "Old Wine in a New Bottle: The MILP Road to MIQCP" (posted 2009-07-08). It appeared as "The MILP Road to MIQCP" (with A. Saxena, IMA Vol. Math. Appl. 154:373–405, DOI 10.1007/978-1-4614-1927-3_13).
- **The framing**: both abstracts say "These methods can be viewed as generalizations of techiniques for mixed-integer linear programming."
- **The chapter's Table 6** maps MILP concepts to MIQCP concepts row by row ("M01LP vs. MIQCP").

**3.4 Theory paper, then computational paper, then solver, within about five years** [practice, P].
1. **Theory**: the copositive representation (Optimization Online 2006/10; *Math. Program.* 120:479–495, 2009, DOI 10.1007/s10107-008-0223-z). Its computational section warns: "So the results of this paper are not a "magic bullet" for solving NP-hard problems. Indeed, formidable computational challenges still (necessarily) exist." (p. 493) [stated, P]
2. **Algorithm**: one for the doubly nonnegative relaxation (Optimization Online 2008/12; *Math. Program. Comput.* 2:1–19, 2010, DOI 10.1007/s12532-010-0010-8).
3. **Solver**: a branch-and-bound solver built on that algorithm with his former PhD student Jieqiu Chen (PhD 2010 per the CV) (Optimization Online 2011/02; *Math. Program. Comput.* 4:33–52, 2012, DOI 10.1007/s12532-011-0033-9; code QuadProgBB).

### Layer 4 · Experiments and execution

#### 4.1 Test problems: where they come from

**4.1.1 The benchmark grows like a ladder: each paper keeps the old set and adds a harder rung** [practice, P].

| Year | What was added | Source |
|---|---|---|
| 2005–2008 | The 54 box-QP instances of Vandenbussche & Nemhauser, n = 20–60 ("A branch-and-cut algorithm for nonconvex quadratic programs with box constraints", *Math. Program.* 102(3):559–575, 2005, DOI 10.1007/s10107-004-0550-7) | Burer & Vandenbussche 2008, *Math. Program.* 113:259–282, DOI 10.1007/s10107-006-0080-6, p. 276 |
| 2009 | "we have also generated larger instances to demonstrate the enhanced capabilities available using the SDP-based branch-and-bound": n = 70–100, densities 25/50/75 %, three per cell; 36 new, 90 in total | *Comput. Optim. Appl.* 43:181–195, DOI 10.1007/s10589-007-9137-6, p. 192 |
| 2010 | "(iii) 9 instances with p = 125 generated for this paper"; 99 in total | Burer 2010, p. 11 |
| 2019 | All three generations published in `BoxQP_instances` as "Basic", "Extended" and "Extended2", each credited to its paper, with optimal values to 9 significant digits, the seeded generator `util/genboxqp.m` (`rand('twister',seed)`, integer entries in [−50, 50]) and SDPA files of two relaxations ("simple" and "rlt") for 90 instances | repository |

[observed, S] The ladder became the field's box-QP test set: "Our test set consists of all 99 instances studied in the papers [37, 15, 11]." (Bonami, Günlük & Linderoth, preprint of 13 June 2016, p. 7; *Math. Program. Comput.* 10:333–382, 2018, DOI 10.1007/s12532-018-0133-x).

**4.1.2 Literature instances on which the standard relaxation is known to fail come first** [practice, P].
- **Burer & Anstreicher** (2013 preprint, §5.1–§5.3) proceed in three steps:
  1. Yuan's n = 2 instance (Y. Yuan, "On a subproblem of trust region algorithms for constrained optimization", *Math. Program.* 47:53–63, 1990, DOI 10.1007/BF01580852) and Ye–Zhang's three instances (Y. Ye, S. Zhang, "New results on quadratic minimization", *SIAM J. Optim.* 14:245–267, 2003, DOI 10.1137/S105262340139001X), on which the basic SDP relaxation is not tight, closed by the new cuts.
  2. "5.2 An example with a positive gap": an instance on which their own relaxation is not tight.
  3. Random instances.
- **Burer, Kim & Kojima**: "We collected a total of 400 instances of (1) from the literature" (Gset, BiqMac, GlobalLib; *Comput. Optim. Appl.* 59:27–45, 2014, DOI 10.1007/s10589-013-9618-8, p. 39) [stated-joint, P].

**4.1.3 Random instances are engineered to be hard, from a theorem** [practice, P]. The theorem is Martínez's result on local-nonglobal minimizers of the trust-region subproblem (J.M. Martínez, "Local minimizers of quadratic functions on Euclidean balls and spheres", *SIAM J. Optim.* 4:159–176, 1994, DOI 10.1137/0804009). `soctrust/martinez.m` is the generator behind §5.3 of the 2013 paper (released 2016):
- "%% Set basic radius to be the dimension (Martinez suggests that a larger radius increases the chances of a local-nonglobal minimum)"
- a rejection step: "%% Solve regular TRS (only considered successful if SDP delivers rank-1 solution, which is on the boundary)"
- the problem is rotated so that the TRS optimum is r1·e1, then "a random coordinate-aligned ellipsoid, which does not include r1*e1 (i.e., it cuts off the global solution of TRS)" is added;
- a doubt is left in the code: "% h = (2*rand(n,1)-1)/n; % Relatively small shift of the center. Could this be a problem?"

**Credit and later use**:
- The paper credits the idea: "We thank Henry Wolkowicz for this valuable suggestion." (preprint p. 18, footnote) [stated-joint, P].
- The generator was ported to Python in 2023 (`ballconstraints/src/define_functions.py`, `generate_martinez_instance`). The 2023 paper keeps the name: "We call these the Martinez instances following the terminology introduced in [9]." (arXiv 2303.01624v1, p. 18) [practice, P].

**4.1.4 Only instances that the baseline relaxation fails on are reported, and the filter is disclosed** [practice, P].
- **2016**:
  - `ttrs/submit_tests.sh` sets `INSTANCES_DIR="${BASE_DIR}/Section_5_4_instances/unsolved_in_Reference_8"`, and `liftedRLT_fun.m` says "Input is the filename of the instance mat file from reference [8]. See https://github.com/sburer/soctrust".
  - The paper: "Applying our heuristic lifted-RLT constraints to the 215 previously unsolved instances, we can solve 82—about 38%—of them" (Yang & Burer, *SIAM J. Optim.* 26(1):661–680, 2016, DOI 10.1137/130945880, p. 679).
- **2023**:
  - `ballconstraints/scripts/search_instances.py` has `num_tests = 2500000 # 2500000 is default for revision 2023-04-21` and `target_num_unsolved_by_shor = 1000`. Every kept instance is logged with its seed and with the modification time of the generator file (`generator_timestamp`).
  - The paper: "we specifically did not include instances that were already solved by Shor in this test" (arXiv 2303.01624v1, p. 13).
- **2026**: "For each size we scanned seeds starting from zero and retained the first ten candidates for which the Shor relative gap … exceeded 0.01." (arXiv 2609.32017v1, p. 8). For another family: "Such instances are rare; retaining 10 per size required scanning up to 16970 seeds." (p. 12).
- **Reuse of the 2013 leftovers**: they were re-packaged on 2023-10-24 (soctrust commit "Add specific archive and results for unsolved instances in Section 5.3"), four days before `ballconstraints` was created, and reused again in 2026 through a git submodule pinned to one commit.
- [inferred] Every reported success rate is therefore conditional on a filtered, hard pool. The papers state the filter, and in 2026 the scan count, but the unconditional rate is not the headline.

**4.1.5 Instances that users send in become test cases** [stated, P]. QuadProgBB commits:
- "Add example from user for testing." (b48f009, 2011-11-10)
- "Add run of the difficult problem sent from a user. It looks like we have improved the handling of GUBs at least." (7f6433e, 2011-11-15)
- "Add problem instance from Johan Loefberg." (047af95, 2013-05-24), later "Archive Johan’s example." (2014-01-20)

#### 4.2 Baselines: which ones, and how they are configured

**4.2.1 The first baseline is his own, or his co-author's, previous code** [practice, P].

| Year | Baseline | Evidence |
|---|---|---|
| 2008 | No external solver; his two relaxations against each other | "Our primary interest is the performance of (SDP1) compared to that of (SDP2)" (p. 275), although the introduction says off-the-shelf software "such as BARON [20], is also available for solving (QP)" (p. 260) |
| 2009 | The co-author's LP-based branch-and-cut | COAP note: "They wanted to compare their SDP-based branch-and-bound algorithm with that of an LP-only approach, which led to a comparison with Vandenbussche and Nemhauser [13] on box-constrained non-convex QPs." (p. 569) [stated-joint, P] |
| 2010 | His own 2008 method | "The basic question we ask is: which method produces better bounds more quickly?" (p. 11) [stated, P] |
| 2012 | The 2008 code ("BurVan") plus Couenne 0.3 | Chen & Burer 2012 |
| 2023 | His earlier relaxations, and Eltved & Burer's in both directions | "We ran Beta on these instances and solved 262 of them. We also ran the method of [16] on the six instances in Table 2, which were unsolved by Beta, and their method generated worse lower bounds in all six cases." (arXiv 2303.01624v1, p. 19; [16] = Eltved & Burer, *Math. Program.* 197:281–306, 2023, DOI 10.1007/s10107-021-01737-9) [stated, P] |

**4.2.2 The baseline gets its best configuration, and what could not be matched is disclosed** [stated-joint, P].
- **2009**: "For each instance we tested, we used the faster of these two to compare with our SDP approach." (p. 192). "These two" are the baseline's two branching rules, run with "the parameter settings suggested in their work".
- **2012, footnote 2**: "So we employ their simpler relaxation in order to have the best overall times for their method." (Chen & Burer 2012, p. 45)
- **2012, version mismatch**: "The BurVan code is not publicly available, but since the second author was a co-author of the BurVan code, the code was available to us. BurVan uses CPLEX 9.1, and while we tried to convert it to use CPLEX 12.2 as Quadprogbb does, we were unsuccessful due to CPLEX run-time errors that we could not fix." (p. 45)
- **IVQR** (Xu & Burer, *Math. Program. Comput.* 9:471–497, 2017, DOI 10.1007/s12532-017-0117-2): "In particular, CPLEX solves a mixed-integer model of the CQPCC using the bounds derived in Sect. 2.2." (p. 474). The competitor receives the authors' derived bounds.
- **SDPLR 2003**: "Both SB and DSDP are run with their default parameters." (SBmethod 1.1.1 and DSDP 3.2; p. 344)

**4.2.3 General-purpose global solvers: Couenne and later Gurobi are run; BARON is cited, beaten by transitivity in print, and run once in the code history** [practice, P].
- **2010**: "In particular, off-the-shelf solvers such as BARON [24] have been outperformed by a specialized LP-based branch-and-cut algorithm [27], and Burer-Vandenbussche [8] present their method, which outperforms the branch-and-cut method. Our experiments here show convincingly that Algorithm 1 outperforms Burer-Vandenbussche and hence is a state-of-the-art algorithm for globally solving nonconvex box-constrained quadratic programs." (p. 16). The paper contains no BARON run.
- **Nov 2011**, after the acceptance of the 2012 paper:
  - `QuadProgBB/tests/user_20111108/baron_out/baron.log` holds a BARON 9.3.1 run through GAMS on an Argonne MCS license. After about 19 h 52 min the bounds are still −2727.06 (lower) and −2704.00 (upper).
  - Commit by J. Chen: "Add Baron output / It seems Baron had a difficult time closing the gap. / Couenne performed even much worse than Baron" (b066728, 2011-11-11).
- **2012 and 2017**: Couenne 0.3 and 0.4 are the general-solver baselines, with exact versions given ("Specifically, we used Couenne stable version 0.3, revision:738", 2012, footnote 3, p. 46).
- **2016** [observed, S]: Bonami, Günlük & Linderoth ran bgl, BARON, GloMIQO and QuadProgBB with a 2-hour limit. "It should be noted that for the large and dense problems in our test suite, the performance of the semidefinite-programming based solver QuadProgBB dominates the other solvers. For example, for jumbo/high-density instances, the average final optimality gap for QuadProgBB after two CPU hours is 0.13%, while the gap is orders of magnitude larger for the other three solvers." (preprint p. 25)
- **2025–2026**: Gurobi's nonconvex solver is the global reference.
  - "The SDP solution has rank one, so tightness is certified directly; Gurobi independently confirms the global optimum." (submodular-tests f3acd86, AI-co-authored commit)
  - In the Lorentz study Gurobi runs after the conic methods with "time limit max{5, 3 tmax}, where tmax is the maximum time used by the three conic methods on that instance" (2609.32017v1, p. 8).

**4.2.4 Comparisons stay fair to the relaxation being tested, even when this makes it look worse.**
- **His convention** [practice, P], `lorentz-positive/README.md` (2026): "For each SDP method, the reported lower bound comes from the relaxation and the feasible upper bound comes from the point recovered from that method's own first column. No Gurobi incumbent or point recovered by another method is used to improve an SDP method's gap. Gurobi is reported separately using its own incumbent and global bound."
- **An outside view of its cost** [observed, S]: "For the sake of correctness, we should warn that the value U B in [3, 23] is not computed by running two local searches as done in this paper. It is instead computed from the final solution of the relaxed problem, so that it could be slightly worse and justify the larger number of unsolved instances." (Consolini & Locatelli, arXiv 2102.11161v2, p. 20; [23] = Yang & Burer 2016)

#### 4.3 Protocol and metrics

**4.3.1 Single processor, stated hardware, hard limits** [practice, P].
- **2003**: "We stress, however, that none of the three codes is parallel, that is, each code uses only one processor." (SGI Origin2000; p. 341) [stated-joint]
- **2010**: "In particular, we have used the Matlab command maxNumCompThreads(1) to ensure that Matlab makes use of only one processor." (p. 10) [stated]. The QuadProgBB help (2011) adds what he had found: "We have found that, due to Matlab internals, QUADPROGBB can actually be faster when restricted to a single processor, especially when multiple CPUs are under heavy load."
- **Limits**:
  - 2009: 45,000 s for the default tolerance and "a time limit of 20,000 CPU seconds" for 1 % (pp. 192–193);
  - 2012: "a time limit of 10 h and memory limit of 1 gigabyte were enforced for each method on each instance" (p. 46).
- **2026**: `paper_experiments.toml` records:
  - the machine ("Mac mini, Apple M4, 10 cores, 16 GB memory"), the OS, and the Python, NumPy and SciPy versions;
  - the solvers: MOSEK "11.2.2 through Python Fusion" and Gurobi "13.0.2 through gurobipy";
  - `thread_policy = "solver defaults unless the manuscript explicitly states otherwise"`.

  The single-thread rule is gone.

**4.3.2 "Solved" has a numerical definition, and it tightened over time** [practice, P].
- **2013**: relative gap below 10^-4. Yang & Burer 2016, p. 679: "(In [8], an instance was regarded as solved if the relative gap between the relaxation value and the feasible value gotten by extracting x is less than 10−4.)" An eigenvalue "rank measure" is plotted against the gap (2013 preprint, p. 19).
- **2023**: gap below 10^-4 and eigenvalue ratio above 10^4 [stated, P].
  - Paper: "Strictly speaking, a small relative gap is enough to verify approximate optimality, but we will also require a large eigenvalue ratio in order to bolster our confidence in the numerical results." (arXiv 2303.01624v1, p. 10)
  - Code (`src/define_constants.py`): `tol_rel_gap = 1.0e-4 # For declaring problem solved`, `tol_eval_ratio = 10**4 # For declaring problem solved`, `tol_mosek = 1.0e-10 # For Mosek`.
- **2025–2026**: the dual objective serves as the lower bound. "The dual value is used because weak duality makes it a rigorous lower bound, so the relative gap is nonnegative and vanishes exactly when the relaxation is tight." (`submodular-tests/README.md`). In the Lorentz kit an instance is tight when the gap is at most 10^-5, with denominator max(1, |UB|, |LB|).
- [inferred] Counts on the "same" hard instances are therefore not strictly comparable across his papers (Contradiction 4).

**4.3.3 Omissions, filters and failures are reported in the text** [stated-joint, P].
- **2008**: "However, this rescaling introduced some occasional numerical failures in CPLEX when solving convex QP subproblems in the AL method. We have omitted instances where such issues where encountered." (p. 281)
- **2012**:
  - "but we excluded 3 either because of size or numerical difficulties encountered by each of the methods." (p. 45)
  - "Here we regard instances as "nontrivial" if they require more than 10 s to solve by at least one of the three methods." (p. 46)
  - Failed runs are reported separately with the gap at termination (Table 2, p. 48), and performance profiles cover all instances.
- **The solver reports its own unreliability** [stated, P]:
  - status "'num_issues': if a large pencentage (>30%) of the nodes encountered numerical issues, then this status is returned" (QuadProgBB help);
  - run logs count poorly solved nodes: "solved = fully + fathomed + poorly : 222 = 169 + 12 + 41" (`tests/user_20111108/run1/output.txt`).

**4.3.4 Fixed seeds and logged provenance** [practice, P].
- **SDPLR 1.03-beta**, as imported in 2023: `#define RANDOM 0 // default 1 (also in main.c (???))` and `srand(925)`. Runs are deterministic unless the code is recompiled.
- **2019–2023**: the BoxQP generator is seeded; the 2023 instance search logs each seed and the generator's timestamp.
- **2026**:
  - "Every randomized experiment is seeded and deterministic" (`submodular-tests/README.md`).
  - The Lorentz runners "write each completed row immediately", and "A resumed run must use the same generator and tolerance options as the original run; the provenance checks detect mismatches." (`lorentz-positive/README.md`)

**4.3.5 Simple designs that isolate the idea** [stated-joint, P].
- "we take a straightforward approach for choosing C, one which depends only on the value of n of an instance. Although this approach does not take full advantage of the data … we feel this approach allows us to study the basic features of our framework." (Burer, Kim & Kojima 2014, p. 39)
- "In total, each instance was solved four times, representing the various choices of relaxation type and optimality tolerance." (2008, p. 275)

#### 4.4 What is done first, and how fast

- **A quick experiment motivates the method before it is built** [stated, P]. Standard QPs with n = 25, 50, 75, 100 solved with SeDuMi: "the resulting CPU times (in seconds) were 1, 30, 385, and 1787, respectively." (Burer 2010, p. 3)
- **The prototype comes first** (3.1).
- **Subproblems are solved loosely, and the outer loop is tuned by experiment** [stated / stated-joint, P]:
  - "Somewhat surprisingly, computational experiments showed that the dual multipliers converged reasonably well even when the subproblems were solved very loosely by only a few cycles of block coordinate descent." (COAP note, p. 568)
  - Burer 2010:
    - "we find that it pays only to solve these problems very loosely" (p. 10);
    - the penalty update is a rule "which we have found to work well in practice after much experimentation" (p. 10);
    - "Despite many attempts, we have been unable to establish a single rule or strategy for setting σ0 that works well for all problem instances." So σ0 is calibrated "for each problem class" (p. 11).
  - SDPLR 2003: per-constraint penalty parameters also grew too large, so "In the end, we chose to use a single penalty parameter for all constraints and to handle the ill-conditioning by a more aggressive strategy for updating the Lagrange multipliers." (p. 343)
- **A theory requirement is relaxed for speed, with a safeguard for correctness** [stated-joint, P] (2008, p. 274):
  - A constraint needed for boundedness and correctness slowed the subproblems. "Of course, it is theoretically unwise to ignore (3) because both the boundedness of (y, z) and the correctness of branch-and-bound depend on it. (We were able to generate an example of a leaf node that would not be fathomed if (3) was left out.)"
  - They kept the constraint in preprocessing and put an LP relaxation at the leaves: "(In our computations branch-and-bound completed before reaching the leaf nodes, and so we actually never had to invoke this LP relaxation.)"

#### 4.5 Debugging

**4.5.1 A bound crossing is the alarm.**
- **The note** [stated, P], `QuadProgBB/tests/user_20111108/notes.txt`, 2011-11-10: "In output.txt, the problem looks likes its solving fine, and it gets the gap down to around 0.008%. Then, all of a sudden, it finds a much better GUB, which is beyond the current GLB (a contradiction!) and all remaining nodes are fathomed."
- **The logs**: the run ends with "FINAL STATUS 1: optimal value = -2.77651394e+03", while BARON's lower bound on the same instance never went below −2727.06 [practice, P]. This fits an infeasible incumbent [inferred].
- **The same test in 2003**: "For example, nowhere in our computational results did we observe a primal objective value that passed below a dual lower bound." (SDPLR paper, p. 342) [stated-joint, P]
- **As an internal check in code** (present at the 2011-09-22 import): "If newLB < LB, then it means that the subproblem did not solve well because theoretically, newLB >= LB at optimality. So we take this as a sign that sig needs to be reset." [stated, P]

**4.5.2 The open question was already written in the code** [stated, P]. At the import from the "paper repository" (2011-09-22), `quadprogbb.m` said:
- "We presume that CPLEX can return as good a feasible solution as any algorithm. (We do not check anything at the moment. Is this safe?)"
- and, beside the projection calls, "In CPLEX we trust!"

**4.5.3 The fix: check feasibility before an incumbent can prune, make long runs restartable, re-run the user's instance** [stated / practice, P].
- **In-code note to the student** (aaf872f, 2011-11-10): "Nov 10 2011: Jieqiu, I would suggest that we verify the feasibility of any x that might lead to a better GUB. We could require something like norm(A*x-b) < tol, min(x-L) > -tol, and min(U-x) > -tol, where tol is the 'all-purpose tolerance' mentioned in the help. If the tolerances are violated, we simply do not update the GUB. What do you think?"
- **The next day** (dd01a22, "Check pointing and better handling of feasibility of primal solutions."):
  - a `feasible()` test: relative residual for the equalities, and bound checks commented "% Should this be relative somehow?";
  - checkpoint files every `checkpt` nodes;
  - the projection moved back from MATLAB's `quadprog` to `cplexqp`.
- **Result note, 2011-11-15**: "In run3, we see that the GUB is now stable. But the problem still takes a long time for branching with lots of poorly solved nodes."
- **Context**: associate professor; former student J. Chen (PhD 2010; by 2011 at Argonne, per the 2012 paper's Argonne copyright notice); MATLAB with CPLEX 12.2; a departmental git server.

**4.5.4 Numerical noise is capped, and the cap is explained** [stated-joint, P].
- "We impose this limit of 25 only because we found that some instances would keep generating non-productive cuts due to numerical issues in the solver." (2013 preprint, p. 19)
- 2008: unbounded augmented-Lagrangian subproblems "(This behavior was actually observed in practice.)" (p. 274), hence a sign restriction on the multiplier.
- 2012: variables are scaled to an upper bound of 1, "which is done because we found it improved the numerical precision of the overall algorithm" (p. 43).

**4.5.5 2026: a bug in old experiment code is fixed in public, with a regression test and a note on what it affected** [practice, P].
- **The commit**, `ballconstraints` 9304c25 (2026-07-29, AI-co-authored commit):
  - "r1 and r2 are stored as uint8 in the .mat instance files, so r1**2 was computed in uint8 and wrapped modulo 256. The n=20 instances were scaled by 144 instead of 400"
  - "Note that the n=20 results tagged paper_v1 were produced with the overflowed scaling."
  - "Add scripts/test_ttrs_scaling_regression.py pinning r1**2 == 400.0 and the corrected beta value."
- **My check** of the committed results (`results/run_ttrs_instances_from_literature.csv`, at tag `paper_v1` and at HEAD) [practice, P; computation mine]:
  - Under the paper's criterion (gap below 10^-4, eigenvalue ratio above 10^4), all 104 n = 20 instances are solved, both before and after the fix.
  - The mean time of the pre-fix n = 20 rows is 0.374 s. That is exactly the number printed in arXiv v2: "The largest instances (size n = 20) were solved in 0.374 seconds on average." (p. 20)
  - After the fix the mean is 0.606 s. The machine and MOSEK version of the re-run may differ, so the change cannot be attributed to the bug alone.
- **Status**: no correction is registered in Crossref for DOI 10.1007/s10107-024-02076-1 (checked 2026-10-10). The commit does not say how the bug was found. It is the commit that `lorentz-positive` pins, and that project reuses the instances [inferred: found during that reuse].

#### 4.6 Code, release and reproducibility over time

- **2000s–2016: code as an archive of what was run** [practice, P].
  - soctrust files are named after paper sections and hold the saved instances and results.
  - `ttrs` holds the SGE batch scripts as they were used (`qsub -q all.q instance.sh`, with `#qsub -q MANSCI` commented out); they skip instances whose results already exist.
  - The QuadProgBB README is one line: "Globally solving nonconvex quadratic programming".
- **The user's interface, and binaries** [practice / stated, P].
  - QuadProgBB takes arguments "identical to the corresponding input arguments for MATLAB's QUADPROG function" (help).
  - Binaries for Linux 32/64-bit, Mac 32-bit and Win32 were committed in Oct 2011, and Mac 64-bit in May 2013, with candour: "Added Win32 binaries. Actually not tested because I don't have CPLEX under Win32." (b43df45)
  - The pre-release todo list includes "4. It never hurts to ship binaries."
- **Non-expert users** [stated-joint, P].
  - `grades/Basic/README_grades.txt` (2018): "The professor who wants to run the algorithm called Basic in the paper … can do it using the following ampl files", to be submitted to NEOS ("(Any other solver for MILP is also fine.)").
  - `grades/Robust/verify_grades.m` recomputes each reported global upper bound and max-gap and prints "did not verify GUB" or "did not verify MAXGAP" on a mismatch [practice, P].
- **2023–2026: release with the preprint or revision, then exact certificates and full reproduction kits** [practice, P].
  - `ballconstraints`:
    - arXiv v2: "Source code, scripts, and results are available at https://github.com/sburer/ballconstraints." (p. 4); the release commit is tagged `paper_v1`.
    - In 2026 he added "a self-contained exact verification of two projection counterexamples discovered after the paper". The README notes "These conjectures are not statements made in the paper." (bold in the source) and "Consequently, the reported separations do not depend on an SDP solver's numerical tolerance."
  - `submodular-tests` (AI-co-authored commits):
    - "Five scripts and one support module existed only as untracked files, so everything the current revision reports computationally lived on one machine." (ebb2eba, 2026-08-24)
    - The README maps every figure and table to a script, the solver it needs and its output. It adds: "`verify_counterexample.py --exact` is worth singling out: the paper's central new claim, that the relaxation is not tight for n ≥ 4, is checked in exact rational arithmetic with no solver and no floating point." (symbols re-typed)
  - `lorentz-positive`:
    - "The code supports three levels of reproducibility": rebuild all tables from the committed raw results, run smoke tests, or re-run everything.
    - `paper_experiments.toml`: "This file is the source-of-truth map between the manuscript and the reproduction code. It intentionally records what the paper needs, not every exploratory experiment in the repository."
  - SDPLR (2026-03-23, AI-co-authored commits):
    - NULL checks after every allocation;
    - `exit(1)` on error paths: "exit(0) signals success to the shell; using it on error paths makes it impossible for callers (scripts, CI, make) to detect failures." (1a0a216);
    - a five-problem test suite whose max-cut cases are "Synthetic max-cut SDP problems (analytically known optima)", checked through the DIMACS error measures (`tests/run_tests.sh`, `tests/check_output.py`).
  - **Tools**:
    - GitHub Copilot instructions (Dec 2025);
    - "Co-Authored-By: Claude Sonnet 4.6" trailers (Mar 2026) and "Claude Opus 5" trailers (Jul–Sep 2026);
    - the Lorentz preprint: "The AI assistants Claude (Anthropic) and Codex (OpenAI) were used to write the code for the computational experiments and for light editing of the text." (p. 20) [stated-joint, P].
- **An echo of his teaching** [inferred]: his 2015 R teaching video explains relative paths and the working directory ("relative paths are nice because they allow you to shorten or two to make sometimes more compact your your paths to your various files", machine transcript). His 2023 scripts run from `scripts/`, call `sys.path.insert(1, '../src')`, and write to `'../results/'`.

### Layer 5 · Judging results

**5.1 A numerical "tight" needs two signals, and central claims get an exact certificate** [practice / stated-joint, P]. In addition to 4.3.2:
- The submodular counterexample is verified in rational arithmetic, by "the 3^4 KKT enumeration" and by "the five leading principal minors" (f3acd86, AI-co-authored commit). v3, p. 14: "Section 6.4 verifies these claims in exact rational arithmetic".
- In the Lorentz paper the n = 2 optimum "can be certified directly by enumerating the stationary points and mutual intersections of the two ellipse boundary arcs", and "A global solve using Gurobi confirms this value to nine digits." (2609.32017v1, p. 16)

**5.2 He reports where the method loses** [stated-joint, P unless marked].

| Year | What lost, in his own words |
|---|---|
| 2003 | "It should be noted, however, that these "hamming" graphs have a particular structure that allows SB to solve each of them in one iteration. This type of performance is actually quite atypical" (p. 345). The competitor won that table |
| 2008 | "For all instances tested, runs with (SDP1) outperform those with (SDP2) in terms of CPU time." (p. 276). The stronger relaxation lost on time |
| 2009 | "From the figure, one can see that many instances are solved more quickly by branch-and-cut, while a large subset are solved faster by the SDP approach." and "We conclude that the SDP-based approach scales better than branch-and-cut." (p. 192). On a competing method (L.T.H. An, P.D. Tao, *J. Global Optim.* 13:171–206, 1998, DOI 10.1023/A:1008240227198): "This attests to the speed and scalability of their bounding scheme." (p. 194) |
| 2012 | "For most Globallib, RandQP and CUTEr instances, Couenne outperforms Quadprogbb as shown in Fig. 2a." (p. 48) |
| 2016 | "However, the CPU time increases dramatically when separating the lifted-RLT cuts." (p. 679) |
| 2017 | "Our algorithm performs worse than Couenne only on the remaining 46 instances." (p. 487) |
| 2023 | An extra valid constraint "did not provide added strength on our test instances" (arXiv 2303.01624v1, p. 9) [stated] |

**5.3 Regularities become conjectures, not theorems** (3.2). His verdict on a mixed result: "In our opinion, these experiments illustrate both the computational value of our approach and the extent to which more work is needed to solve TTRS fully." (2013 preprint, pp. 17–18) [stated-joint, P]

**5.4 He falsifies his own earlier relaxation in a later paper** [stated-joint, P].
- "To our knowledge, this is the first reported TTRS instance on which the beta relaxation fails to be exact." (Anstreicher & Burer, 2609.32017v1, p. 17). The "beta relaxation" is from his 2025 ball paper.
- The `ballconstraints` README (2026) adds two projection counterexamples to conjectures that paper had prompted.

**5.5 How he responds when others find an error** [practice, P unless marked].

*Burer & Ye* (*Math. Program.* 181:1–17, 2020, DOI 10.1007/s10107-019-01367-2):
- **Jan 2021**: the talk title already narrows the claim: "Exact SDPs for a Class of (Random and Non-Random) Nonconvex Diagonal QCQPs" (CV [P32]).
- **Erratum** dated "February 18, 2021", published as "Correction to: …" (*Math. Program.* 190:845–848, 2021, DOI 10.1007/s10107-021-01684-5) [stated-joint, P]:
  - "This note reports an error in Theorem 3 of [1], which was pointed about by Prof. Fatma Kılınç-Karzan and Mr. Alex Wang of Carnegie Mellon University, whom we sincerely thank for bringing this to our attention."
  - "However, in truth the proof fails because, with this setup, the systems cannot be simultaneously feasible."
  - "Instead of the purported Theorem 3, we now prove an analogous theorem, except that it only applies to diagonal instances of (1)."
- **Homepage**: his copy (`papers/053-rank-bounds.pdf`, 20 pp., PDF created 20 Feb 2021) puts the erratum in front of the paper.
- **arXiv**: 1802.02688 still has only v1 (8 Feb 2018) and v2 (7 Nov 2018), and v2 still contains the original Theorem 3 with its "with high probability" argument (checked 2026-10-10).

*Burer, Natarajan (and Willemsen), arXiv 2504.03996*:

| Date | Step |
|---|---|
| 4 Apr 2025 | v1: "We show that continuous quadratic submodular minimization with bounds is solvable in polynomial time using semidefinite programming" (p. 1); "Our proof is by induction on n with base case n = 1." (p. 6) |
| Oct 2025 | Talk titled "Towards the Semidefinite Representability …" (CV [P07]); the Jan 2026 talks return to "On the …" ([P02]–[P05]) |
| 28 Nov 2025 | New repository: "First workable code to test many instances for tight SDP relaxation", then "Updating after working on code for awhile. Cannot find a counterexample." (63d44e3) [stated] |
| 5 Apr 2026 | v2: the relaxation is "provably tight for dimension n ≤ 3 and empirically tight for larger n" (symbols re-typed) |
| Aug 2026 | Two n = 4 counterexamples exist and the second is published: "gap_figure.py drew the first n = 4 counterexample, with relaxation value -13/4, which the paper does not discuss; the published counterexample is the second one, drawn by gap_figure2.py." (4d97f0e, AI-co-authored commit) |
| 31 Aug 2026 | v3, with a third author: "Via an explicit counterexample for n = 4, we show that the relaxation is not tight in general, although it remains empirically tight on randomly generated instances." (p. 1); "We thank Shaoning Han for pointing out an error in an earlier version of this paper." (p. 46) [stated-joint] |

[inferred] His random search did not find the structured counterexample that an outside reader's error report led to. The sequence was: hedge in a talk title → narrow the claim (v2) → certify a counterexample exactly, credit the finder and release code (v3).

*Outside code fixes and user reports*:
- On Benoît Legat's two SDPLR pull requests (merged 2023-12-14) he replied "Thank you!" and "Thanks for your attention to this sub-case, that long ago I thought would not be an issue. :)" [stated, P].
- Four later pull requests from the same contributor (opened 2025-04-10, e.g. "Fix reading of negative block size") were still open on 2026-10-10, although he merged his own three hardening pull requests on 2026-03-23.
- QuadProgBB issue #1, "From helpful user..." (2014-01-20), reports a CPLEX option removed in version 12.6. It was fixed by "Remove deprecated CPLEX option." (9368906, 2016-05-18), but the issue was never closed.

**5.6 A 2026 reproduction audit changed claims in the paper** [practice, P; AI-co-authored commits].

| Commit | What it found or did |
|---|---|
| f868951 (2026-08-24) | "Two discrepancies are documented rather than papered over." Figure 3 did not reproduce, and "Table 5 reproduces qualitatively but not numerically, since the sampling scheme behind the published numbers was not recorded." |
| 2de726a (2026-08-26) | Figure 3 traced to a co-author's MATLAB inputs (`cmmmoments.m`): "Figure 3 is reproducible with its supplied MATLAB inputs." … "the path matrix has diagonal 2 at both endpoints" (README at that commit) |
| 9301139 (2026-08-26) | "At 100 instances the path column could not resolve differences of the size it was reporting" … "so the non-monotonicity was noise, and the paper's claim that the gap grows with graph size rested on it." Re-run at 1,000 instances per cell, with Welch t statistics |

What changed in the paper:
- **Figure 3**: v3 now speaks of "the energy of a grounded graph" (p. 33). The word "grounded" does not occur in v1 or v2.
- **Table 5**:
  - v1 (p. 22) and v2: "The results show that, as the size of the graph grows, the gap grows as well.", computed over "100" instances.
  - v3 (p. 36): "The results show that, for the star and complete graphs, the gap grows as the size of the graph grows, while for the path graph it remains roughly constant near 0.6%.", computed over "1000 instances".

### Layer 6 · Writing and presentation, as seen across versions

**6.1 During review the contribution was reframed, and part of it became a second paper** [practice, P; the reading that review caused it is inferred].
- **Preprint**: Optimization Online 2005/06/1167, "Semidefinite-Based Branch-and-Bound for Nonconvex Quadratic Programming" (posted 2005-06-27). Its abstract ends: "Furthermore, specialization to the box-constrained case yields a state-of-the-art method for globally solving this class of problems."
- **Published** as "A finite branch-and-bound algorithm for nonconvex quadratic programming via semidefinite relaxations" (*Math. Program.* 113:259–282; received 27 June 2005, accepted 30 October 2006). The abstract now opens: "Existing global optimization techniques for nonconvex quadratic programming (QP) branch by recursively partitioning the convex feasible set and thus generate an infinite number of branch-and-bound nodes. An open question of theoretical interest is how to develop a finite branch-and-bound algorithm for nonconvex QP."
- **The split-off paper**: the box-QP specialization appeared separately in COAP, "Received: 7 November 2006", eight days after the acceptance.
- **Acknowledgement**: "The authors would like to thank the editors and anonymous referees for numerous suggestions that have improved the paper immensely." (p. 281)

**6.2 Ornament leaves titles.** "Old Wine in a New Bottle: The MILP Road to MIQCP" became "The MILP Road to MIQCP" (3.3) [practice, P].

**6.3 Talk titles hedge before the papers change.** "Diagonal" (Jan 2021) and "Towards" (Oct 2025) come before the narrowed texts (5.5) [practice, P].

**6.4 The 2026 documentation is written for outsiders and states its limits** [practice, P].
- "Rewrite README for external readers" (lorentz-positive cf8f923).
- "Bounds and gaps should reproduce on other machines to solver tolerance, but wall-clock times naturally vary." (README)

### Layer 7 · Organising the work

**7.1 The student's code lives in his repository, and he supervises by asking questions in the code** [practice / stated, P].
- **QuadProgBB**:
  - Chen's commits implement a list of requested features: an options struct, verbosity levels and status codes ("Verbosity is tested and done!", 2011-10-05).
  - His in-code note ends "What do you think?" (4.5.3).
  - He tested binaries himself: "Commiting Mac 64-bit binaries. (Sam testing logged in as Jieqiu.)" (2013-05-24).
- **Later**: students and visitors keep their own repositories, which he reuses.
  - The 2023 ball paper's data come from his `soctrust` and from `A-Eltved/strengthened_sdr` (`ballconstraints/data/README.md`).
  - The Eltved & Burer paper states "This paper is accompanied by the code repository https://github.com/A-Eltved/strengthened_sdr" (homepage copy, PDF p. 5), and generates "15,000 instances for each dimension" (PDF p. 20).

**7.2 Users' requests shape the interface** [practice, P; the source of the list is inferred].
- The pre-release todo list of Oct 2011 asked for an options struct, verbosity control, a numeric status flag and "It never hurts to ship binaries." Its author is not named. The same weeks added a YALMIP snapshot (`extra/yalmipR20110915_1015.zip`) and a YALMIP call with `'solver','quadprogbb'` (`extra/yalmip_command.txt`).
- By early 2012 the items stood under a "FINISHED" heading. What remained: "1. Update help files and website to emphasize that our code is a global, not local, code." and "2. Investigate application of the guy who emailed."

**7.3 Credit is specific** [stated-joint, P].

| Person | Credited for |
|---|---|
| Henry Wolkowicz | The instance construction (4.1.3) |
| Kurt Anstreicher | "Leverages key idea of Ye-Zhang (2003) with a key assist from Kurt." (Kurt-Fest slides, 2023) |
| Stefan Wild | "We thank Stefan Wild for helpful discussions, which led to the variant of the trust-region subproblem solved in Sect. 5." (Chen & Burer 2012, p. 51) |
| Tobias Achterberg | The `.lp` converter |
| Roland Hildebrand | Acknowledged in the Lorentz paper |

**7.4 2025–2026: AI assistants are the coding partner; the human signs the claims** (4.6) [practice, P]. [inferred] The explicit reproduction audits, exact certificates and noise checks appear in the assistant-era commits. Whether he or the assistant started each audit is not visible in the record.

### Layer 1 · Taste, as revealed by practice

- **Strong relaxations over cheap ones.** "More generally, the paper also illustrates that it can be worthwhile to pay for a computationally expensive, but strong, relaxation compared to evaluating many inexpensive relaxations." (COAP note, p. 569) [stated-joint, P]. In practice: SDP or DNN relaxations at every node (2008–2012), and SDP-based cuts (2013–2026) [practice, P].
- **Finiteness, exactness and certificates over speed records** (6.1, 5.1) [inferred].
- **Long benchmark continuity**: the same instance families over 20 years (4.1) [inferred].
- **Small, exactly checkable cases** (n = 2, 3, 4) as the place where questions get settled (3.2, 5.1, 5.4) [inferred].

---

## 3. Failures, abandoned directions and corrections (dated)

| When | What | Evidence | Tag |
|---|---|---|---|
| 2002–2006 | SDP relaxations for 0-1 IP judged unlikely to beat IP solvers; moved to nonconvex QP | COAP note p. 568 | [stated-joint, P] |
| 2000–2003 | Per-constraint penalty parameters tried and dropped (SDPLR) | 2003 p. 343 | [stated-joint, P] |
| 2005–2006 | A constraint needed for correctness dropped at most nodes for speed; the leaf-node safeguard was never invoked | 2008 p. 274 | [stated-joint, P] |
| 2005–2008 | Globallib instances with CPLEX failures omitted | 2008 p. 281 | [stated-joint, P] |
| 2008–2010 | No general rule found for the initial penalty parameter | 2010 p. 11 | [stated, P] |
| 2011 | Bounding sums of variables tried and dropped: "So we decided to stick with calculating separate bounds for each variable." | 2012 footnote 1, p. 43 | [stated-joint, P] |
| 2011 | Port of the 2008 code to CPLEX 12.2 failed | 2012 p. 45 | [stated-joint, P] |
| 2011 | QuadProgBB accepted an infeasible incumbent on a user's instance; fixed within a day | notes.txt; aaf872f; dd01a22 | [practice, P] |
| 2011–2016 | Untested Win32 binaries; code left "a bit disogranized"; maintenance ends | b43df45; ee19018 | [stated, P] |
| 2013 | Cut loop capped at 25 because of numerical noise; a counterexample for the intersecting case | 2013 preprint pp. 13, 19 | [stated-joint, P] |
| 2016 | Lifted-RLT solves 82 of 215 hard instances, at high CPU cost | 2016 p. 679 | [stated-joint, P] |
| 2021 | Theorem 3 of Burer & Ye wrong; narrowed to diagonal instances; arXiv not updated | Correction; arXiv 1802.02688v2 | [stated-joint / practice, P] |
| 2023 | TTRS extension failed (v1); v2 replaces that sentence with the 212-instance result | arXiv 2303.01624 v1 p. 4; v2 pp. 4, 20 | [stated, P] |
| 2025–2026 | Polynomial-time claim withdrawn (v1 → v2 → v3, counterexample at n = 4) | arXiv 2504.03996 v1–v3; 63d44e3 | [practice, P] |
| 2026 | uint8 overflow in the 2023 TTRS experiments; the printed n = 20 timing came from mis-scaled instances | 9304c25; my CSV check | [practice, P] |
| 2026 | Figure provenance mismatch and a noise-based claim found by the audit; the paper text changed in v3 | f868951, 2de726a, 9301139; v3 pp. 33, 36 | [practice, P] |
| 2026 | His 2025 beta relaxation shown inexact on a two-dimensional TTRS instance | 2609.32017v1 p. 17 | [stated-joint, P] |
| — | Rejected or withdrawn papers; referee reports | none found | Gap |

---

## 4. Era and resource context

| Period | Seniority and team | Tools and compute visible in the papers and code |
|---|---|---|
| 2000–2003 | PhD student; advisor Monteiro, with Y. Zhang | ANSI C; SGI Origin2000 (300 MHz processors), one processor per code; baselines SBmethod 1.1.1 and DSDP 3.2; DIMACS and Gset graphs; fixed seed 925 |
| 2002–2009 | Assistant, then associate professor in a business-school department; co-author Vandenbussche (UIUC, then Axioma) | Augmented-Lagrangian SDP code with a CPLEX 9.x QP subsolver (not public); Pentium 4 at 2.4 GHz under Linux; time limits up to 45,000 s |
| 2008–2013 | Associate professor; student, then Argonne postdoc, J. Chen; Anstreicher | MATLAB `R2008a` / `R2009a` / `R2012a` with C-MEX; CPLEX 12.2–12.3 MATLAB interface; SeDuMi 1.3 and YALMIP; Couenne 0.3 with Clp; BARON 9.3.1 via GAMS on an Argonne license; Pentium D at 3.2 GHz; departmental git server |
| 2013–2019 | Full professor; students Yang and Xu; directing master's programs | YALMIP with MOSEK 7.1; SGE cluster (`qsub`); CPLEX 12.4 and Couenne 0.4; Gurobi; AMPL and NEOS |
| 2023–2024 | Chaired professor; visitor Eltved; student Park | Python with MOSEK Fusion 10.0.37 on an M2 MacBook Air (24 GB); R scripts; MATLAB `R2022b` with MOSEK 10 |
| 2025–2026 | Department chair (DEO); co-authors at SUTD; Anstreicher (retired 2023) | Python with MOSEK 11.2.2 and Gurobi 13.0.2 on a Mac mini M4; exact rational arithmetic in Python; GitHub Copilot, Claude Sonnet 4.6, Claude Opus 5, Codex |

Tools: [practice, P] from the papers and code. Seniority and students: CV [practice, P]. Anstreicher's retirement: 2023 "Happy Retirement, Kurt!" slides [stated, P].

---

## 5. Candidate process heuristics for the skill (all [inferred] from §§2–4)

- **P1** Choose problem classes where an expensive but strong relaxation can win. Check that quickly before building anything (2.1, 4.4).
- **P2** Build the prototype first and measure it; let the theory follow. The slide's question "Why should this work at all?" may stay open in print for years (3.1).
- **P3** Grow benchmarks as a ladder, and publish them with optimal values and generators (4.1.1).
- **P4** Generate hard random instances from structure, e.g. a theorem about where the relaxation fails. Filter out what the baseline already solves, and disclose the filter and the scan count (4.1.3–4.1.4).
- **P5** Make your own previous method the first baseline, run in its best configuration. Disclose the mismatches you could not fix (4.2.1–4.2.2).
- **P6** Treat a bound crossing as a bug alarm. Verify an incumbent's feasibility before it may prune (4.5.1–4.5.3).
- **P7** Declare "solved" only on two numerical signals, and certify central claims exactly when you can (4.3.2, 5.1).
- **P8** State empirical regularities as conjectures. When someone outside finds an error: narrow the claim, name the finder, and publish the counterexample with a certificate (3.2, 5.5).
- **P9** Put losses and omissions in the text (4.3.3, 5.2).
- **P10** (2026 practice) Make every number in the paper regenerable from committed raw data. Audit before revising, and let the audit change the text (4.6, 5.6).

---

## Contradictions (kept, not reconciled)

1. **BARON: available, unknown, beaten by transitivity, then run.**
   - 2008 (p. 260): BARON "is also available for solving (QP)".
   - 2009 (p. 194): "(Note also that we are unaware of any publicly available global optimization codes for (QPB).)"
   - 2010 (p. 16): state-of-the-art claim over BARON through a chain of comparisons, with no BARON run.
   - Nov 2011 code history: a BARON run on a user's instance, and "It seems Baron had a difficult time closing the gap".
   - 2016 [observed, S]: in a direct comparison by others, QuadProgBB dominates BARON on large, dense box QPs.
   - "Publicly available" may mean "free of charge", which BARON is not; no source says so.
2. **"In CPLEX we trust!" against the November 2011 fix** (4.5.2–4.5.3). The code shipped trusting CPLEX's projections without a feasibility check while asking "Is this safe?"; a user's instance showed it was not.
3. **Corrections and arXiv.** The 2021 correction was not carried to arXiv 1802.02688 (still the 2018 v2 with the original Theorem 3). In 2026 the submodular paper's arXiv record was updated twice (v2 narrowing, v3 counterexample).
4. **Counts on the same hard TTRS benchmark disagree across texts.**
   - Yang & Burer 2016 (p. 679): the 2013 method left 41 + 70 + 104 = 215 instances unsolved; they "can solve 82—about 38%—of them".
   - The 2023 ball paper (v2 p. 20) speaks of 212 instances (the committed CSV has 38 + 70 + 104) and writes "Another approach by Yang and Burer [11] solves 29 instances", citing [11] = the 2015 *Math. Program.* paper, not the 2016 SIAM paper.
   - Consolini & Locatelli (arXiv 2102.11161v2, p. 20), citing [3], report that 133 of the 212 remain unsolved by the bound of [23] = Yang & Burer 2016 (that is, 79 solved).
   - Possible partial explanations: a different SDP solver ("This column is slightly different from [8] because we use a different SDP solver in the experiment", 2016 p. 679), different "solved" definitions (4.3.2) and different upper-bound conventions (4.2.4). I could not trace the figure 29.
5. **A printed timing against the corrected run.** "solved in 0.374 seconds on average" (n = 20; v2 p. 20) came from mis-scaled instances. After the fix the committed rows average 0.606 s, while "solved all 212" survives (4.5.5).
6. **A stated instance count against the listed groups.** Burer, Kim & Kojima 2014 state "a total of 400 instances" (p. 39) but list 199 + 64 + 36 = 299. Not resolved; possibly a typo.
7. **A README against its own history.** On 2026-08-24 the submodular README said "This repository reproduces every computational claim the paper makes" and, in the same version, "Figure 3 does not currently reproduce". It was resolved two days later by tracing the figure to MATLAB inputs and changing the paper's wording (5.6).
8. **A CV title against the publication.** CV [J18] reads "A Two-Variable Analysis of the Two-Trust-Region Subproblem"; Crossref and both repository READMEs read "A Two-Variable Approach to the Two-Trust-Region Subproblem".

## Gaps

- **Reviews and rejections**:
  - No referee reports, rebuttals or rejected manuscripts are public.
  - OpenReview: a note search for "Burer" among authors returned 0 forum notes; the profile endpoints demanded a challenge or a login, which I did not attempt.
  - zbMATH Open returned "contents unavailable due to conflicting licenses" for the 2008 and 2009 branch-and-bound papers.
- **DBLP**: every request returned an anti-bot page; not circumvented.
- **Private code**: not public are the "paper repository" QuadProgBB was pulled from (2011), the 2008 "BurVan" code, and the 2003–2009 experiment scripts.
- **Not opened**: `QuadProgBB/tests/user_20111108/emails.pdf`, which holds correspondence with a third party (privacy).
- **Published versions not read**:
  - the 2025 ball paper (I used arXiv v1 and v2);
  - the body of the 2016 TTRS paper beyond §5;
  - the 2012 survey with Letchford beyond its software section;
  - Burer & Piccialli, "Three methods for robust grading" (*Eur. J. Oper. Res.* 272:364–371, 2019, DOI 10.1016/j.ejor.2018.06.019); only its repository was read.
- **Downloaded but not analysed**: Burer, Monteiro & Zhang, *SIAM J. Optim.* 12:503–521 (2002), DOI 10.1137/S1052623400382467; Burer & Chen, *Comput. Optim. Appl.* 48:653–673 (2011), DOI 10.1007/s10589-009-9273-2; an archive file named `046-ismp2015.pdf` (not identified).
- **Not stated anywhere I found**:
  - the purpose of the `ttrsn2` re-run (2024);
  - how the uint8 bug was found, and whether a correction to the 2025 paper is planned (Crossref shows none);
  - who started each 2026 audit, him or the assistant;
  - the source of the figure "29" (Contradiction 4).
- **Early against final for the 2013 SIAM paper**: the Optimization Online PDF was replaced in 2013 ("Updated: 2013/02/21"), so the March 2011 version could not be compared.
- **Talks**: the 2023 and 2021 talks are machine captions; the 2 June 2023 SIAM delivery is represented only by its slides.

## Sources

Primary = his own papers, slides, code, CV, or the bibliographic records of his own works. Secondary = third parties, aggregators and tools.

1. S. Burer, curriculum vitae, 18 pp., "updated February 12, 2026". https://sburer.github.io/files/cv.pdf (primary)
2. S. Burer, homepage (footer "Last updated 2026-03-20") and the listing of his paper archive `papers/001…062` via the GitHub contents API, fetched 2026-10-10. https://sburer.github.io/ (primary)
3. S. Burer, GitHub profile: repository list, and issues and pull requests of sdplr and QuadProgBB, via the GitHub API, 2026-10-10. https://github.com/sburer (primary)
4. `QuadProgBB` repository, 42 commits, 2011-09-22 → 2016-07-08 (README, `quadprogbb.m`, `todo.txt` history, `tests/user_20111108/` notes, logs and BARON log). https://github.com/sburer/QuadProgBB (primary)
5. `soctrust` repository, 2016-05-11 → 2023-10-24 (`martinez.m`, `Section_5_3_tests.m`). https://github.com/sburer/soctrust (primary)
6. `ttrs` repository, 2016 (`submit_tests.sh`, `liftedRLT_fun.m`). https://github.com/sburer/ttrs (primary)
7. `ttrsn2` repository, 2024-06-06. https://github.com/sburer/ttrsn2 (primary)
8. `grades` repository, 2018-04-10 (`Basic/README_grades.txt`, `Robust/verify_grades.m`). https://github.com/sburer/grades (primary)
9. `BoxQP_instances` repository, 2019-01-30 (README, `util/genboxqp.m`, `util/convertintolp.py`, `sdprelax/`). https://github.com/sburer/BoxQP_instances (primary)
10. `Max-AO` repository, 2014-01-17 → 2014-01-20. https://github.com/sburer/Max-AO (primary)
11. `sdplr` repository, 2023-10-05 → 2026-03-23 (README, `CLAUDE.md`, `tests/`, commit bodies, pull-request comments). https://github.com/sburer/sdplr (primary)
12. `ballconstraints` repository, 2023-10-28 → 2026-08-28 (tag `paper_v1`; scripts, constants, results CSVs, commit 9304c25). https://github.com/sburer/ballconstraints (primary)
13. `submodular-tests` repository, 2025-11-28 → 2026-08-26 (README at several commits, Copilot instructions, commit bodies). https://github.com/sburer/submodular-tests (primary)
14. `lorentz-positive` repository, 2026-09-15 → 2026-09-22 (README, `paper_experiments.toml`). https://github.com/sburer/lorentz-positive (primary)
15. S. Burer and R.D.C. Monteiro, "Two Decades of Low-Rank Optimization", slides, SIAM OP23, 2 June 2023; and S. Burer, "On Nonconvex Quadratic Programming with Ball Constraints" (Kurt-Fest) slides, same day. https://github.com/sburer/2023-06_SIOPT (primary)
16. S. Burer, "An Introduction to Semidefinite Programming for Combinatorial Optimization", IPCO 2019 summer school (README only). https://github.com/sburer/ipco-2019-sdp-tutorial (primary)
17. S. Burer, R.D.C. Monteiro, "A nonlinear programming algorithm for solving semidefinite programs via low-rank factorization", *Math. Program.* 95:329–357, 2003. DOI 10.1007/s10107-002-0352-8 (primary)
18. S. Burer, D. Vandenbussche, "Solving lift-and-project relaxations of binary integer programs", *SIAM J. Optim.* 16(3):726–750, 2006. DOI 10.1137/040609574 (primary; record only)
19. S. Burer, D. Vandenbussche, "A finite branch-and-bound algorithm for nonconvex quadratic programming via semidefinite relaxations", *Math. Program.* 113:259–282, 2008 (online 2006); with Optimization Online 2005/06/1167. DOI 10.1007/s10107-006-0080-6 (primary)
20. S. Burer, D. Vandenbussche, "Globally solving box-constrained nonconvex quadratic programs with semidefinite-based finite branch-and-bound", *Comput. Optim. Appl.* 43:181–195, 2009. DOI 10.1007/s10589-007-9137-6 (primary)
21. "COAP 2009 best paper award", *Comput. Optim. Appl.* 47:567–570, 2010 (unsigned). DOI 10.1007/s10589-010-9368-9 (primary, joint)
22. S. Burer, "On the copositive representation of binary and continuous nonconvex quadratic programs", *Math. Program.* 120:479–495, 2009. DOI 10.1007/s10107-008-0223-z (primary)
23. S. Burer, "Optimizing a polyhedral-semidefinite relaxation of completely positive programs", *Math. Program. Comput.* 2:1–19, 2010. DOI 10.1007/s12532-010-0010-8 (primary)
24. S. Burer, A. Saxena, "The MILP Road to MIQCP", IMA Vol. Math. Appl. 154:373–405, 2012 (online 2011); with Optimization Online 2009/07/2338 ("Old Wine in a New Bottle: …"). DOI 10.1007/978-1-4614-1927-3_13 (primary)
25. J. Chen, S. Burer, "Globally solving nonconvex quadratic programming problems via completely positive programming", *Math. Program. Comput.* 4:33–52, 2012. DOI 10.1007/s12532-011-0033-9 (primary)
26. S. Burer, K.M. Anstreicher, "Second-order-cone constraints for extended trust-region subproblems", *SIAM J. Optim.* 23(1):432–451, 2013 (homepage preprint revised 16 Nov 2012). DOI 10.1137/110826862 (primary)
27. S. Burer, A.N. Letchford, "Non-convex mixed-integer nonlinear programming: A survey", *Surveys Oper. Res. Manag. Sci.* 17(2):97–106, 2012 (software section only). DOI 10.1016/j.sorms.2012.08.001 (primary)
28. S. Burer, S. Kim, M. Kojima, "Faster, but weaker, relaxations for quadratically constrained quadratic programs", *Comput. Optim. Appl.* 59:27–45, 2014. DOI 10.1007/s10589-013-9618-8 (primary)
29. S. Burer, B. Yang, "The trust region subproblem with non-intersecting linear constraints", *Math. Program.* 149:253–264, 2015. DOI 10.1007/s10107-014-0749-1 (primary)
30. B. Yang, S. Burer, "A two-variable approach to the two-trust-region subproblem", *SIAM J. Optim.* 26(1):661–680, 2016. DOI 10.1137/130945880 (primary)
31. G. Xu, S. Burer, "A branch-and-bound algorithm for instrumental variable quantile regression", *Math. Program. Comput.* 9:471–497, 2017. DOI 10.1007/s12532-017-0117-2 (primary)
32. S. Burer, V. Piccialli, "Three methods for robust grading", *Eur. J. Oper. Res.* 272:364–371, 2019 (record only; repository read). DOI 10.1016/j.ejor.2018.06.019 (primary)
33. S. Burer, Y. Ye, "Exact semidefinite formulations for a class of (random and non-random) nonconvex quadratic programs", *Math. Program.* 181:1–17, 2020; arXiv 1802.02688 (v1, v2). DOI 10.1007/s10107-019-01367-2 (primary)
34. S. Burer, Y. Ye, "Correction to: Exact semidefinite formulations …", *Math. Program.* 190:845–848, 2021 (Springer page; homepage erratum dated 18 Feb 2021). DOI 10.1007/s10107-021-01684-5 (primary)
35. K.M. Anstreicher, S. Burer, "Quadratic optimization with switching variables: the convex hull for n = 2", *Math. Program.* 188:421–441, 2021 (record only). DOI 10.1007/s10107-021-01671-w (primary)
36. A. Eltved, S. Burer, "Strengthened SDP relaxation for an extended trust region subproblem with an application to optimal power flow", *Math. Program.* 197:281–306, 2023 (homepage copy). DOI 10.1007/s10107-021-01737-9 (primary)
37. S. Burer, "A slightly lifted convex relaxation for nonconvex quadratic programming with ball constraints", *Math. Program.* 211:157–179, 2025; arXiv 2303.01624 v1 (2 Mar 2023) and v2 (28 Oct 2023). DOI 10.1007/s10107-024-02076-1 (primary)
38. S. Burer, K. Natarajan, R. Willemsen, "On the Semidefinite Representability of Continuous Quadratic Submodular Minimization With Applications to Pricing and Moment Problems", arXiv 2504.03996 v1 (4 Apr 2025), v2 (5 Apr 2026), v3 (31 Aug 2026). https://arxiv.org/abs/2504.03996 (primary)
39. S. Burer, K.M. Anstreicher, "Applications of the Lorentz positive cone in nonconvex quadratic optimization", arXiv 2609.32017v1, 25 Sep 2026. https://arxiv.org/abs/2609.32017 (primary)
40. S. Burer, "SDPLR 1.03-beta User's Guide (short version)", 5 pp., PDF of 12 Aug 2009. https://sburer.github.io/papers/SDPLR-1.03-beta-usrguide.pdf (primary)
41. Optimization Online author archive "Samuel Burer" (48 entries, 2001–2026) and the abstract pages 2005/06/1167, 2009/07/2338 and 2011/03/2957. https://optimization-online.org/author/samuel-burer/ (primary)
42. Transcript of "Two Decades of Low-Rank Optimization" (University of Iowa, March 2023), YouTube auto-captions saved by a sibling agent: `sources/talks/2023-two-decades-of-low-rank-optimization_youtube-wSauUgRIQDg_auto-captions.txt`. https://www.youtube.com/watch?v=wSauUgRIQDg (primary; machine transcript)
43. Transcript of "Convexification for Non-Convex Mixed-Integer Quadratic Programming", INFORMS IOS plenary, 31 March 2021, YouTube auto-captions saved by agent 01: `sources/talks/2021-03-31-ios-plenary-convexification-nonconvex-miqp_youtube-QfZLtPz5JBY_auto-captions.txt`. https://www.youtube.com/watch?v=QfZLtPz5JBY (primary; machine transcript)
44. Transcript of "Relative Paths and the Working Directory in R" (teaching video, 2015-02-08): `sources/talks/2015-relative-paths-working-directory-r_youtube-fe6GA200dks_auto-captions.txt`. https://www.youtube.com/watch?v=fe6GA200dks (primary; machine transcript)
45. P. Bonami, O. Günlük, J. Linderoth, "Solving Box-Constrained Nonconvex Quadratic Programs", preprint, 13 June 2016 (Optimization Online); published as "Globally solving nonconvex quadratic programming problems with box constraints via integer programming methods", *Math. Program. Comput.* 10:333–382, 2018. https://optimization-online.org/wp-content/uploads/2016/06/5488.pdf ; DOI 10.1007/s12532-018-0133-x (secondary)
46. L. Consolini, M. Locatelli, "Sharp and fast bounds for the Celis-Dennis-Tapia problem", arXiv 2102.11161v2. https://arxiv.org/abs/2102.11161 (secondary)
47. Literature named in the findings, records only (not read): D. Vandenbussche, G.L. Nemhauser, *Math. Program.* 102(3):559–575, 2005, DOI 10.1007/s10107-004-0550-7; Y. Yuan, *Math. Program.* 47:53–63, 1990, DOI 10.1007/BF01580852; Y. Ye, S. Zhang, *SIAM J. Optim.* 14:245–267, 2003, DOI 10.1137/S105262340139001X; J.M. Martínez, *SIAM J. Optim.* 4:159–176, 1994, DOI 10.1137/0804009; L.T.H. An, P.D. Tao, *J. Global Optim.* 13:171–206, 1998, DOI 10.1023/A:1008240227198. (secondary)
48. Crossref REST API records for the 32 DOIs above, including the correction relation of DOI 10.1007/s10107-019-01367-2, fetched 2026-10-10. https://api.crossref.org/works/ (secondary bibliographic data)
49. arXiv abstract pages, version listings and API for 2303.01624, 2504.03996, 2609.32017, 1802.02688, 2512.24295, 2406.10065 and 2102.11161, fetched 2026-10-10. https://arxiv.org/ (secondary bibliographic data)
50. zbMATH Open API, documents 5248727 and 5601444 (review text unavailable). https://api.zbmath.org/ (secondary; no content)
51. OpenReview API, note search and profile lookup (0 notes; profile behind a challenge). https://api2.openreview.net/ (secondary; no content)
52. DBLP person page 96/4845 (anti-bot page). https://dblp.org/pid/96/4845 (secondary; no content)
53. WebSearch result list, 1 query, 2026-10-10, used only to find source 45. (secondary)
54. Sibling note `references/research/06-trajectory.md` (this run), used as a lead list only. (secondary)

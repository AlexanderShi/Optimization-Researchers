# 02 · Stated methodology (what Misener SAID research should be)

| Field | Value |
|---|---|
| Researcher | Ruth Misener (living). Professor in Computational Optimisation, Department of Computing, Imperial College London; BASF / Royal Academy of Engineering Research Chair in Data-Driven Optimisation (2022–27); Amazon Scholar (2025–). SB Chemical Engineering, MIT (2007); PhD Chemical Engineering, Princeton (2012), advised by Christodoulos A. Floudas (CV, W8) |
| Dimension | Research agent 02 of 06: stated methodology, i.e. what she *claims* research should be. Whether she practises it is left to `03-process-evidence.md` |
| Research date | 2026-10-10 |
| Sources consulted | 54 in total. 39 are cited below (30 primary, 9 secondary). 15 more were opened but could not be used: no speech by her, speakers not identifiable, no captions, HTTP 403/404/429. They are listed under Gaps |
| WebSearch calls | 4. Everything else came from curl, yt-dlp, the Crossref, DataCite, arXiv, OpenAlex, Semantic Scholar, Unpaywall and GtR APIs, and one WebFetch (refused, HTTP 403) |
| Local corpus | No user-supplied material. `references/sources/{papers,essays,software}` hold only `.gitkeep`. The transcripts in `references/sources/talks/` were saved during this workflow by sibling agents from YouTube auto-captions (ASR). So no finding below is "from user-supplied material". This run added one transcript there (T9, a podcast transcribed locally; see the conventions below). Nothing under `private/` was opened |

## How to read this note

**What the evidence is, and what it is not.** Misener has published no essay, blog, lab guide or interview on "how I do research", and two WebSearch calls for interviews or advice pieces found none. Her stated method has to be read from:
1. One reflective talk, her inaugural lecture "Just relax, Or: How I'm bad at my own algorithmic advice" (2023, T8). It is built around six "buzzwords" that pair an algorithmic idea with a lesson from academic life.
2. Asides in nine research talks, seminars and videos (2021–2025, T1–T7, T10, T11), and one 55-minute podcast panel recorded at her 2024 BCS Roger Needham Award event (T9).
3. Short single-author written texts:
   - her 2016 memorial essay on Floudas, the richest written source (W1);
   - a 2014 newsletter article (W2);
   - workshop abstracts from 2015, 2019, 2022, 2023 and 2026 (W3–W7).
4. Self-descriptions:
   - the CV (W8), her web pages (W9) and her Imperial profile (W10);
   - her 2017 fellowship abstract and its later outcome narrative on UKRI Gateway to Research (W11);
   - two Imperial News items she wrote (W12, W13);
   - slides (W14).
5. Quotes in press articles (Q1–Q8), co-authored perspective papers (J1–J4), and observers (O1, O2).

Most of the stated material concerns three things: what problems are worth solving, how to report computational results honestly, and how to work with industry and students. On how she writes papers there is almost nothing.

**Tags.**
- **[stated]**: she said or wrote it alone (her talk, her essay, her own web page or CV, a quote attributed to her by name).
- **[stated-joint]**: in a text she co-authored; her voice cannot be separated from her co-authors'.
- **[stated-inst]**: an institutional or event page that presents her; the author is not named.
- **[observed]**: someone else said it about her.
- **[inferred]**: my reading of the evidence, never a fact.
- **P / S**: primary / secondary source.

**Quotation conventions.**
- **ASR captions.** Quotes from talks are verbatim with respect to the caption track saved in `references/sources/talks/`, *not* guaranteed verbatim with respect to what she said. Misrecognitions are kept and flagged `[sic, ASR: = …]`:
  - "minop"/"mi nlp" = MINLP;
  - "lacera"/"lesser"/"laser" = Lasserre;
  - "bounce tightening" = bounds tightening;
  - "BSF" = BASF;
  - "omelette"/"omelet" = OMLT;
  - "convex hole"/"convex hold"/"context whole" = convex hull;
  - "Bas opt"/"basan" = BayesOpt/Bayesian;
  - "Mitten Mystery" = Miten Mistry; "Flutus" = Floudas.
- **Timestamps.** `[mm:ss]` is the start of the caption block in which the quote begins (matched against the SRT files from which the transcripts were made). For T8 it is the paragraph marker in the saved `.md` transcript, so it can be up to about 30 s early.
- **T9 (BCS podcast) is lower grade.** There was no caption track. I transcribed the public MP3 locally with faster-whisper (`small.en`, int8, CPU) after per-half-second gain normalisation. The audio is a room recording of five speakers, and many words are wrong. Speaker attribution is **[inferred] from turn-taking**. I quote T9 only in four passages: [05:41–06:28] (the host has asked her to introduce the panel); [07:45–09:38] ("just start, Ruth, with you"); [27:56–31:57] (she speaks about her own students Jose, Ruby Sedgwick and Juan); and [44:08–46:26] (Huth's question is put to her, and she speaks about people she works with, one of them probably a former student). Every T9 quote is marked "T9, local ASR, attribution inferred".
- **Written sources** carry page numbers where the source has pages: W1 printed pages 12–16 (= PDF pages); W3 printed pages of Oberwolfach Report 26/2019.
- **Co-authored texts.** Quotes come from the arXiv version that was read (J1, J2). For J3 only the abstract was read.

## A. Source corpus and its era / resource context

Era codes follow `03-process-evidence.md` so the two notes can be joined:
- **E1**: 2008–2013, Princeton PhD in the Floudas group; C++ solvers on one workstation.
- **E2**: 2012/13–2017. Royal Academy of Engineering Research Fellow at the Centre for Process Systems Engineering (Chemical Engineering), then Lecturer in Computing (2014); first PhD students.
- **E3**: 2017–2022. EPSRC Early Career Fellowship "GALINI" (Python/Pyomo, open source, fellowship-funded developer); Senior Lecturer, then Professor (2020).
- **E4**: 2019–2026. Data-driven optimisation with BASF and others; BASF/RAEng Research Chair from 2022; NeurIPS/ICLR venues; groups of up to about a dozen co-authors.

| ID | Source | Date | Voice | Era / resource context |
|---|---|---|---|---|
| W1 | R. Misener, "Christodoulos Achilleus Floudas", *SIAG/OPT Views and News* 24(1):12–16 | Oct 2016 | single [stated] P | Written two months after her adviser's death, when she was a Lecturer in Computing (E2). It is the only long text in her own voice about how research should be done, framed as what she learned from him |
| W2 | R. Misener, "Deterministic Global Optimisation at CPSE: Models, Algorithms, and Software", article for the Sargent Centre (CPSE) Industrial Consortium (CV G1: "Centre for Process Systems Engineering Newsletter, Issue 10, 2014"); PDF dated 7 June 2014 | Jun 2014 | single [stated] P | E2. Written as an RAEng fellow in Chemical Engineering, for industrial members and a "general, technically-educated audience" (her project page) |
| W3 | R. Misener (joint work with Baltean-Lugojan, Ceccon, Mistry), abstract "Developing spatial branch & bound solvers", *Oberwolfach Report* 26/2019, pp. 1616–1618 (workshop 2–8 June 2019) | 2019 | single author of abstract [stated] P | E3. Opening plenary of the MINLP workshop (CV K13) |
| W4 | Open problem "(13) [Misener]" in the open-problem list of *Oberwolfach Report* 46/2015 (workshop 18–24 Oct 2015) | 2015 | one attributed line [stated] P | E2 |
| W5 | R. Misener, tutorial abstract "Machine learning for mathematical optimization and mathematical optimization for machine learning", Dagstuhl Seminar 22431 report, *Dagstuhl Reports* 12(10):166–174 | Oct 2022 seminar; report 2023 | single [stated] P | E4 |
| W6 | R. Misener, abstract "Autonomous research machines: Self-optimizing new chemistry", Isaac Newton Institute workshop DDEW03, 24 Apr 2023 (YouTube description of KX9Tzt_WLOM) | Apr 2023 | single [stated] P | E4. The talk itself has no captions and was **not read** |
| W7 | R. Misener, plenary IP1 abstract "Optimizing over graphs: Challenges, Formulations, and Applications", SIAM Conference on Optimization (OP26), Edinburgh, 2 Jun 2026 | Jun 2026 | single [stated] P | E4. Most recent statement found. The talk itself was **not read** |
| W8 | R. Misener, *Curriculum vitae*, 32 pp., "Updated December 3, 2025" | Dec 2025 | single [stated] P | E4. Self-description, including the heading "Reproducibility & Accessibility" |
| W9 | Her homepage http://wp.doc.ic.ac.uk/rmisener/ : home, Teaching, Research Team ("Work with us!"), Community Service, project pages (MINLP; optimisation over ML surrogates; active learning; explainable optimisation) | undated; read 2026-10-10 | single [stated] P | Current, but individual pages are undated (the MINLP page mentions GALINI, so it was written in or after E3) |
| W10 | Imperial profile, first-person bio, https://profiles.imperial.ac.uk/r.misener | read 2026-10-10 | single [stated] P | Current |
| W11 | UKRI Gateway to Research, EP/P016871/1 "GALINI": abstract and planned impact (written for the 2017 proposal) and the Researchfish "Key findings" narrative (it mentions the 2025 STEM for Britain round, so it was last updated in 2025 or later) | 2017; ≥2025 | PI text [stated] P | E3; the outcome narrative is E4 |
| W12 | R. Misener, "Department of Computing researchers selected to present research in Parliament", Imperial News | 21 Feb 2019 | single [stated] P | E3; written about her PhD students |
| W13 | R. Misener, "Department of Computing MSc student honoured for her joint work with Royal Mail", Imperial News | 15 May 2019 | single [stated] P | E3 |
| W14 | Slides "Developing spatial branch & bound solvers" (Baltean-Lugojan, Ceccon, Kronqvist, Misener, Mistry), 48 frames, dated 2021-06-23, https://www.doc.ic.ac.uk/~rmisener/MINLPSolver_Tutorial.pdf | Jun 2021 | slide text, group authorship; she presented it [stated] P | E3. The slides behind T4; they name the works the talk only gestures at |
| T1 | Imperial Business Partners panel "Decision making under uncertainty" (with M.-A. Cardin and M. A. Díaz), YouTube Cbnfz00SHLg; ASR | early Mar 2021 (Q2, dated 12 Mar 2021, says "earlier this month") | own answers [stated] P | E3/E4; virtual event |
| T2 | Seminar "Partition-based formulations for mixed-integer optimization of trained ReLU neural networks", series *Machine Learning NeEDS Mathematical Optimization* (Sevilla), YouTube UcNXm24uQjE; ASR | Apr 2021 (CV S29) | single [stated] P | E3/E4; virtual |
| T3 | Seminar "Partial Lasserre relaxation for sparse Max-Cut", *Discrete Optimization Talks*, YouTube e3CSpZ4uUT8; ASR | 30 Apr 2021 | single [stated] P | E3; virtual ("i'm in my living room and this is really really weird", [00:10]) |
| T4 | Plenary video "Developing spatial branch & bound solvers" for NMPC 2021 (CV K16: plenary, 07/2021), YouTube Z5hbKPx9YDE (published 2021-08-05); ASR | Jul/Aug 2021 | single [stated] P | E3. Recorded talk, no Q&A |
| T5 | Video "Introduction to OMLT", YouTube 8IpM42mSsWE; ASR | 22 Mar 2022 | single [stated] P | E4 |
| T6 | Video "Switching formulations in OMLT", YouTube S4KySGdpt0g; ASR | 23 Mar 2022 | single [stated] P | E4 |
| T7 | Cornell *Learning Machines* seminar "Between formulations or: How I Learned to Stop Worrying and Love Parameters", YouTube bC4PDG9EZA8; ASR | 17 Feb 2023 | single [stated] P; Q&A included | E4. The same title was given at MIT (03/2022), HUGO (09/2022, plenary), Princeton (02/2023) and the IMA/OR Society conference (04/2023) (CV S33, K20, S41, I43; this talk is CV S42) |
| T8 | Inaugural lecture "Just relax, Or: How I'm bad at my own algorithmic advice.", Imperial College London, YouTube dN860HNsAs0; ASR; transcript `talks/2023-03-13-just-relax-inaugural-lecture-asr.md` | 13 Mar 2023 | single [stated] P; Q&A answers included | E4. Reflective lecture ten years into her Imperial career |
| T9 | BCS podcast "The Needham Debate: Optimisation algorithms" (panel with M. Huth, T. Berthold, C. Adjiman, D. Budd), Acast episode in BCS's show *The Gem of all Mechanisms*; local ASR saved as `talks/2024-02-26-bcs-needham-debate-podcast-local-asr.md` | recorded at the award event, January 2024 (award presented 10 Jan 2024, Q6); released 26 Feb 2024 | her answers [stated] P; attribution [inferred] | E4 |
| T10 | SCI *SciTalk* "Bayesian optimization and design of experiments", YouTube 9aLOEJNOCho; ASR | Mar 2024 (CV S46) | single [stated] P; Q&A included | E4. Audience of chemists |
| T11 | "Autonomous research machines: Self-optimising new chemistry", *AI Fun with ELLIS* seminar, University of Manchester, YouTube 2br7KspcQXk; ASR | Jan 2025 (CV S50) | single [stated] P | E4. Audience of machine-learning researchers |
| Q1 | D. Silverman, "Decision-making under uncertainty", Imperial *Stories* long read (produced by Imperial Enterprise), https://www.imperial.ac.uk/stories/decision-making/ | early 2021 (text refers to "[January 2021]") | reporter's text with her quotes; S (quotes [stated]) | E3/E4 |
| Q2 | D. Silverman, "Worldwide uncertainty a chance to be more efficient and resilient, say academics", Imperial News | 12 Mar 2021 | S (quotes [stated]) | Cleaned quotes from T1. They match the ASR closely, a check on T1's caption quality |
| Q3 | C. Brogan, "Imperial scoops three new Royal Academy of Engineering research chairs", Imperial News | 24 Mar 2022 | S | E4 |
| Q4 | D. Silverman, "Machine learning techniques from Imperial and BASF advance experimental design", Imperial News | 31 Oct 2022 | S | E4 |
| Q5 | A. Idle, "Major contribution by Imperial undergraduate to open-source research software", Imperial News | 23 Nov 2022 | S | E4 |
| Q6 | BCS, "Professor Ruth Misener awarded the 2023 BCS Roger Needham Award" (11 Dec 2023); same quote in Imperial News (20 Dec 2023) | Dec 2023 | S | E4 |
| Q7 | D. Silverman, "Machine learning models to support chemical R&D recognised with Best Paper Award", Imperial News | 27 Aug 2024 | S | E4 |
| Q8 | Imperial event page for the inaugural lecture (abstract), https://www.imperial.ac.uk/events/158579/just-relax-or-how-im-bad-at-my-own-algorithmic-advice/ | Mar 2023 | [stated-inst] P | E4 |
| J1 | D. Letsios, R. Baltean-Lugojan, F. Ceccon, M. Mistry, J. Wiebe, R. Misener, "Approximation algorithms for process systems engineering", *Comput. Chem. Eng.* 132:106599 (2020), DOI 10.1016/j.compchemeng.2019.106599; read as arXiv:1909.12328v1 | 2019/2020 | [stated-joint] P; she is last and corresponding author | E3 |
| J2 | A. Thebelt, J. Wiebe, J. Kronqvist, C. Tsay, R. Misener, "Maximizing information from chemical engineering data sets: Applications to machine learning", *Chem. Eng. Sci.* 252:117469 (2022), DOI 10.1016/j.ces.2022.117469; read as arXiv:2201.10035v1 (abstract, introduction, conclusion) | 2022 | [stated-joint] P; last and corresponding author | E4 |
| J3 | R. Misener, L. T. Biegler, "Formulating data-driven surrogate models for process optimization", *Comput. Chem. Eng.* 179:108411 (2023), DOI 10.1016/j.compchemeng.2023.108411 | 2023 | [stated-joint] P; **abstract only** (OpenAlex). The publisher page refused automated access (HTTP 403) | E4. Linked to their joint FOCAPO/CPC 2023 keynote (CV K21) |
| J4 | P. Bonami, A. M. Gleixner, J. Linderoth, R. Misener (eds.), "Designing and Implementing Algorithms for Mixed-Integer Nonlinear Optimization (Dagstuhl Seminar 18081)", *Dagstuhl Reports* 8(2):64–87 (2018), DOI 10.4230/DagRep.8.2.64 | 2018 | organisers' executive summary [stated-joint] P; working-group reports record group conclusions [observed] | E3. She co-organised the seminar |
| O1 | E. N. Pistikopoulos, vote of thanks inside T8 [47:04–52:44] | 13 Mar 2023 | [observed] S | Her postdoctoral supervisor |
| O2 | Royal Academy of Engineering text on the 2017 Young Engineer of the Year awards, as reprinted by the trade site Zenoot ("Five star young engineers win Academy Awards") | Jun/Jul 2017 | [observed] S | E2/E3 |

---
## B. Findings by the seven layers (framework §一)

Each item gives the claim, then the evidence: tag, quote, source, timestamp or page, date, P/S, and era. Section C counts the repetitions across items.

### Layer 1 · Research taste (what is worth doing; what counts as a good result)

**L1.1 Solve what could not be solved before; a 10 % speed-up is not worth an academic's time.** [stated, P]
- T7 (17 Feb 2023, ASR):
  - [32:03] "what I would like to do in an area like this is I would like to be able to solve problems that people couldn't solve before"
  - [32:16] "if if I'm just going to speed up a solver by uh 10 percentable to be a sector Works going to do that next week anyway so why bother" [sic, ASR: the middle words are garbled; the sense is that a solver company would make that gain within a week]
  - [32:22] "I want to be able to solve problems that other places can't solve".
- T2 (Apr 2021, ASR):
  - [33:02] the baseline is tuned "such that big m can solve some of the problems ... we'd one like to be able to solve more problems than big m and two we'd like to be able to solve for problems that big m can already solve we'd like to be able to solve them faster";
  - [47:43] "we are um now solving problems that couldn't be solved before".
- T8 Q&A [45:33]: the result that surprised her most is the case where "these problems that had been super difficult were now quite easy".
- Written (E2–E3):
  - W1 (2016, p. 12) praises Floudas because "He pushed the tractability boundary of optimization theory, algorithms, and implementations using a multitude of applications".
  - W11 (2017 abstract): "The primary GALINI research aim is to develop optimisation software that pushes the boundary of computational tractability for PSE energy efficiency applications."
  - W9 (MINLP project page): "there is an enormous gap between what should be computationally tractable and what MINLP computational tools are currently capable of addressing."

**L1.2 Prefer messy, heterogeneous, real problems; she is "not interested" in a bare convergence proof.** [stated, P]
- T8 (13 Mar 2023, ASR):
  - [30:04] "I am not the kind of academic who wishes to live in an ivory tower. I am the kind of academic who wishes to work at a sort of messy and complicated place uh like like this."
  - [30:04]+ "what I am most interested in is computational optimization problems that are uh very complex and very heterogeneous."
  - [30:35] "if anybody needs uh uh sort of uh just a convergence proof or something to just work because you're going to use one of those components that I that I presented probably you got to find somebody else because it's boring and I'm not interested."
  - [31:06] "basically what you can think about what I do is messy play with optimization and that's when I'm happy."
- T11 (Jan 2025, ASR):
  - [16:52] "I've read the literature and I know that all those ideas that I presented are not new";
  - [17:17] she likes to work on "these problems where you have many many of these sort of complications all at the same time", because approaches that target "just one issue" would have to be rethought "once there were multiple issues";
  - [17:47] "I like chemistry because it's just so tough".
- W6 (Apr 2023 abstract): the BASF problems "may simultaneously exhibit: multiple objectives, mixed-feature spaces, asynchronous decisions, large batch sizes, input constraints, multi-fidelity observations, hierarchical choices, and costs associated with switching between experimental points."
- T9 (Jan 2024, local ASR, attribution inferred) [08:24–08:35]: "I would hope that most optimization algorithms are built on data, but somehow we move towards always trying to make it a problem that touches the real world. It gets messier ..."
- J2 [stated-joint] (2022, Conclusion): "the challenge for researchers at the interface between chemical engineering and computer science is to increase the information gained from the resulting available data", data that are "information-poor".
- Contrast with L5.5 and the contradictions section: she also calls the Lasserre hierarchy "the coolest thing ever" and says she likes Gaussian-process proofs.

**L1.3 Relevance comes from real instances, not toy problems (a standard she says she learned from Floudas, against her own early resistance).** [stated, P]
- W1 (Oct 2016):
  - p. 13: "But Chris was never interested in toy problems or proofs of concept. If he was going to apply mathematical optimization to a new problem class, he would always push optimization to its limit via highly relevant, industrially motivated test cases."
  - p. 13: "Chris's complete refusal to address anything but the most pressing real-world problems led him to the tractability boundary of mathematical optimization."
  - p. 13: "I remember raising some objections when Chris said that now we had to globally optimize a model with 15,439 continuous variables, 30 binary variables, 15,406 equality constraints, 230 inequality constraints, and 335 nonconvex terms [116]. But Chris absolutely insisted that his piecewise linear underestimation technique for bilinear terms [117-119] was not relevant unless it was effectively applied to real-world instances."
  - p. 14: "But, more than anything, I appreciated how Chris made my work relevant by insisting that it could apply to real-world problems."
- W2 (Jun 2014, p. 2): "Example (1) is a toy problem with only two variables". The article immediately moves to instances "with up to 4657 continuous variables, 42 discrete variables, 5848 constraints, and 2704 nonconvex bilinear terms".
- T2 [18:53] (ASR): a two-input network is shown only for intuition: "we're not going to use examples this small to try and motivate that we think this is an exciting new set of formulations to use".
- Era E1→E2: the norm is presented as the adviser's, and she reports first resisting it. [inferred] The essay is where she adopts it in her own voice.

**L1.4 Structure first: find the special structure in the problem and let it do the work.** [stated, P] The most repeated claim in the corpus; count in C1.
- W2 (2014, pp. 1–3):
  - "designing algorithms which take advantage of special mathematical structure in optimisation problems" (one of three "focal points of research");
  - "We consider deterministic global optimisation of MINLP through the lens of applications; this is because researchers may be able to find and exploit special mathematical structure for particular problem classes."
- W1 (2016, p. 13): "The special structure of the so-called pooling problem is fascinating".
- W3 (2019, p. 1616): an example showcases "The impact of special structure detection in building a relaxation, i.e. how succeeding or failing at structure detection influences relaxation strength."
- T4 (2021, ASR) [16:04]: "what we're doing is that we're proposing a sort of disciplined programming that develops structure beyond convexity".
- T2 (2021, ASR) [56:12]: "this isn't just black box optimization right ... there's an underlying structure ... sort of deeper things with sort of recognizing underlying structure is where individual programmers can really get involved" [sic, ASR: probably "integer programmers"].
- T8 (2023, ASR):
  - [09:41] "my first buzzword is uh structure detection. And by that I basically mean insider information."
  - [14:46]+ "what we ought to do is we ought to find these sort of structures that exist in optimization problems and we ought to um basically let these structures be their own relaxations because we have something that's convex."
- W9 (MINLP project page): "Our work synthesises general mathematical advances and individualistic problem-specific knowledge into effective algorithmic protocols and computational tools".

**L1.5 The quality of the relaxation is the central lever ("Just relax").** [stated, P]
- T8 (ASR):
  - [05:06] "in the case of minimization, the trick is to just relax";
  - [05:37] "all I've been doing here at Imperial uh is basically figuring out how to relax better";
  - [29:34] "from the the mathematics perspective, the big picture is that uh you're doing all of these things to get a good relaxation."
- Q8 (event abstract, [stated-inst]): her work "has focused on developing relaxations and other approaches to expedite the solution of challenging optimisation problems."
- Use every relaxation available:
  - W3 (2019, p. 1617): "Within the bounds of practical development, the best MINLP strategy is heterogenous, i.e. uses multiple types of relaxations simultaneously [1, 2]." Refs [1, 2] are Anstreicher, *J. Glob. Optim.* 43 (2009) 471–484, DOI 10.1007/s10898-008-9372-0, and Bompadre & Mitsos, *J. Glob. Optim.* 52 (2012) 1–28, DOI 10.1007/s10898-011-9685-2.
  - T4 (2021, ASR) [18:28]: "these are two of my very favorite papers and what they basically say is any relaxation you have available you should be using". [inferred] These are the same two papers: W14 footnotes "Anstreicher [2009], Bompadre and Mitsos [2012]" on the relaxation frames, and W3 cites them for the same claim.

**L1.6 Global optimality matters because the local answer can be wrong, not just worse.** [stated, P]
- T8 (ASR):
  - [04:05] "I want to get the best answer possible" ... "let's be really straightforward. I'm really competitive";
  - [04:36] industrially, one wants to know "when ... you you just stop bother improving";
  - [04:36]–[05:06] in thermodynamic or biomedical settings "nature may end up finding the minimum ... if I end up finding a solution that's not quite as good as the minimum, well that might be of a bit of a problem".
- W1 (2016, p. 12): "energy minimization using local rather than global optimization may yield significant qualitative and quantitative errors in engineering decision making".
- W2 (2014, p. 2): "a local search staying within the feasible space would not reach the global solution."
- J1 [stated-joint] (2019): "The PSE community is mainly interested in global optimization methods because suboptimal solutions may incur significant costs, or even be incorrect (Grossmann, 2013)."
- E4 carry-over to Bayesian optimisation:
  - T10 [11:02] (ASR): Bayesian optimisation "is a global optimization algorithm it's um it's provably Global";
  - T11 [26:06] (ASR): "what I like so much about Bas opt is that it's a global optimization method".

**L1.7 Parameters are a cost: avoid them, or show that they do not matter.** [stated, P] Count in C4.
- W1 (2016, p. 13): Floudas "would push me: Why did these piecewise approximations work so well? How could we eliminate the computational dependence on parameters?"
- T3 (30 Apr 2021, ASR):
  - [18:51] "the possible negative side is that i have introduced two new parameters both of which i'm now going to have to deal with";
  - [27:12] "we're pretty confident in them for a fairly large variety of problems".
- T2 (Apr 2021, ASR):
  - [21:05] "kind of no fair just sort of changing what my parameter value is and then telling you that i always get something uh better than big m";
  - [32:29] "choosing these parameters tends to be fairly robust".
- T7 (2023, ASR):
  - [02:16] "I'm kind of giving you right away the criticism that you might all have ... good God Ruth you use a lot of parameters";
  - [07:04] "that's where these parameters explode in my face";
  - [40:59] "I like this idea when for a particular problem class a good set of parameters consistently stays good I understand that's an experimental result".
- The talk title "Between formulations or: How I Learned to Stop Worrying and Love Parameters" was used at five venues, 2022–23 (W8: S33, K20, S41, S42, I43).
- T11 (2025, ASR):
  - [28:23] "alert alert I'm going to introduce a parameter and then try to um uh show you that the parameter wasn't very important and also that we can get rid of the parameter";
  - [29:40] "I introduced a parameter I don't like to introduce parameters".

**L1.8 Distrust self-serving evaluation, including your own.** [stated, P]
- T11 (2025, ASR):
  - [29:52] "I made up a new metric and I win on the new metric which is you know classic uh um academic right";
  - [30:05] "if I didn't win on it better you better think I'm an idiot";
  - [30:57] on regret per iteration: "they kind of all look the same to me".
- T6 (Mar 2022, ASR) [09:26]: "i am a big fan of this partition based formulation because i am a co-author on this paper but i don't know if for a very particular application if this partition-based formulation is going to be better"; [12:26] "you don't have to take our word for it".
- T2 (2021, ASR) [54:46]: "i know that it's better than big m i don't know that it's better than you know some other partitioning strategy".
- T3 (2021, ASR) [18:01]: "i do not claim that i am tightening anything in fact i would claim that i am not tightening anything".

**L1.9 Against techno-solutionism: a method has a domain, and its author must say where it ends.** [stated, P] Count in C11.
- T1 (2021, ASR):
  - [27:54] "one thing i really dislike is techno solutionism right is that just because there's a technology doesn't mean that like my the hammer that i develop is going to be the thing that's going to solve a problem";
  - [28:06] "i am a mathematician and a computer scientist by training i develop tools";
  - [28:24] "i do have to be extremely careful about what is not my world";
  - [28:41] "my work really is exclusively algorithms";
  - [28:45] "i acknowledge the limitation".
- T10 (Mar 2024, ASR):
  - [17:04] if the kinetics are known (a first-order reaction), "do not use these methods right";
  - [17:54] with cheap data, Bayesian optimisation is "trying to uh crack a nut with a hammer";
  - [20:26] "they really should only be used when acquiring new data is expensive and we have limited other knowledge";
  - [23:51] "10 or fewer dimensions and we're we're fine more dimensions and it starts having asterisks";
  - [55:05] to a questioner fitting an ODE: "I would not use this technique as much as I love this technique".
- W2 (2014, pp. 2–3): deterministic global optimisation "is computationally expensive, but it is highly relevant to application domains where there is high reward for fractional improvements and sufficient time to explore the search space. For very large problems beyond the limit of current deterministic algorithms, heuristics and stochastic methods may be most effective."
- T6 (2022, ASR) [07:07]: "i dearly love mixed integer nonlinear optimization problems i've actually even written a solver for one of them but it they are quite difficult problems to solve". She therefore recommends pairing smooth activations with the complementarity formulation, so that the model stays a continuous nonlinear program.
- T8 Q&A [41:59]+: "I have not seen at this point how the kind of mathematics that I do could sort of design the drugs. Um, but perhaps that's just I'm not imaginative enough."

### Layer 2 · Problem choice (where problems come from; timing; when to leave)

**L2.1 Problems come from industrial partners, through structures that keep the companies at arm's length.** [stated, P]
- T8 Q&A [43:31]+ (ASR), on combining fundamental mathematics with industry: "it's basically you work with with CDTs and then the companies think, "Oh, I'm just putting a little bit of money and then they sort of don't chase me as much." So, I get really cool problems from industry, but I don't uh I don't trim the business model."
- T8 [13:45] (ASR): Imperial's Enterprise team kept presenting her to visiting companies until "the company representative just got tired of only meeting Ruth. And we're like, okay, we'll we'll uh we'll fund her."
- W10 (current): "My research focuses on the type of computational optimisation challenges arising in industry, for example scheduling in manufacturing or experimental design in chemicals research."
- T11 [02:29] (ASR): "I don't know about the company I just play with some of the stuff that they like and that I like".

**L2.2 Her direction is partly opportunistic: chosen by colleagues, department and students.** [stated, P]
- T8 Q&A [46:04] (ASR), asked whether her vision has changed: "basically I'm a person who chooses my my my my vision in some part by my pub buddies. Um so basically um anyone who wants to come to the pub with me we will end up writing a paper together after after some amount of time."
- [46:34] The work on uncertainty and data-driven constraints "basically came from being in a computer science department and being introduced to some of this stuff ... These kind of things come from just being in a department full of really cool researchers. So in some ways very opportunistic."
- T11 [18:30] (ASR), on a pollution-sensing project in Uganda: "I did not come up with this collaboration um my two of my PhD students went to this AI for good ... and they came back with this collaboration".

**L2.3 Choose problems where a standard method's assumption breaks in a real application.** [stated, P] Count in C12.
- T10 (2024, ASR) [45:19]: in Bayesian optimisation "we always assume that we're able to sample the space wherever we wish um at any one time ... this is of course not going to be this the case in many chemistry applications".
- Q7 (Aug 2024): "There are several things in chemistry that don't work well with Bayesian optimisation ... This paper deals with two of those – 'multi-fidelity' ... The other, 'asynchronous batch' ...". The paper is Folch et al., *Comput. Chem. Eng.* 172:108194 (2023), DOI 10.1016/j.compchemeng.2023.108194.
- T11 (2025, ASR) [17:17]: complications "all at the same time"; W6 (2023): challenges that "may simultaneously exhibit" eight complications.
- T6 (2022, ASR) [03:33]: papers compare formulations, "but the challenge for somebody who now wants to use this research is that you don't know which one to implement".
- Older version of the same move, from the MILP/network world: T4 (2021, ASR) [16:04] "similar to what the mixed integer linear optimization community has already done with respect to network optimization problems".

**L2.4 Industrial problems rarely give big jumps; big jumps come from structure found in academic problems.** [stated, P]
- T8 Q&A [45:03] (ASR): "the secret is that all of my industrial collaborators are extraordinary and they've already basically done all of the huge amount of thinking. And so basically a a challenge is that then if I'm actually working on a real industrial problem, we can do stuff and we can do cool stuff but really jumping forward doesn't happen so much because they have done a ton of thinking."
- The counter-example she gives is academic: Mistry's convexity result for the logarithmic-mean-temperature-difference function. That is M. Mistry & R. Misener, *Comput. Chem. Eng.* 94:1–17 (2016), DOI 10.1016/j.compchemeng.2016.07.001. W3 also cites it.
- Contrast with Q4 and Q7 (press quotes on industrial impact) in Contradictions.

**L2.5 Leave the part of the field that industrial teams now lead; move to where solvers struggle.** [stated, P; T9 local ASR, attribution inferred]
- T9 [05:53–06:28], introducing Berthold of FICO Xpress: "the research that we were doing as PhDs has basically entirely limited the industry at this point" [sic, ASR: unclear; probably "moved into industry"]. Then: "it's difficult to do research in this area just because, basically, Timo and colleagues like him have really pushed this stuff forward. So these kind of big teams in optimization ... they really take some of what's been done in academia but then also some of what maybe should have been done [in] academia and make these products".
- T9 [30:20–31:50]: "with respect to sort of integer programming and the kind of stuff that Kimo [= Timo] does, at this point, I don't work as much on solver development, basically ... But we've been thinking a lot recently about embedding these trained models from machine learning into larger optimization problems and then designing effective algorithms that incorporate these models that we learned from data into sort of the typical integer programming problems ... it creates these hugely difficult optimization problems that ... solvers like Timos can't or have difficulty with because it's still ugly numerically ... trying to figure out how to look at that kind of stuff more numerically tractable" [sic, ASR].
- [inferred] This is the only stated *reason* found for her move from MINLP solver building (E1–E3) to embedding trained models in optimisation (E4). It rests on low-grade ASR and needs confirming from another source.

**L2.6 Borrow from neighbouring communities; ask other communities to take up your problems.** [stated, P] Count in C10.
- T4 (2021, ASR) [19:24]: "this is actually the reason that i'm most excited to be giving this particular presentation at npc [= NMPC] because you all actually have had this particular challenge for quite some time". The multi-parametric toolbox of the control community "offers us some hints".
- J1 [stated-joint] (2019): "This paper argues that, contrary to the aforementioned, surface-level distinctions, approximation algorithms are deeply applicable to PSE." It lists five differences between theoretical computer science and PSE, e.g. "TCS often addresses worst-case instances whereas PSE typically solves challenging, practically-relevant instances".
- T11 (2025, ASR) [03:16]: she wants "to show you the kind of problems that uh it would be amazing if you all were working on too"; [36:20] chemists' multi-fidelity work is "cool but they're really missing a lot of what's what what could happen in the literature"; [36:26] "find yourself a chem friend".
- T10 (2024, ASR) [06:56]: she assumes her chemist audience has "seen Less in terms of uh what is the field that machine Learners are now calling Active Learning", and sets out to bring it to them.
- T7 (2023, ASR): a known fix from the MINLP literature solves the lost-linking problem of her split formulations ([39:45] "Pietro has this nice paper on feasibility based bounds tightening based on pairs of constraints").

**L2.7 Questions can take years; the adviser's open question is a research programme.** [stated, P]
- W1 (2016, p. 13): "Actually, thanks to work with Radu Baltean-Lugojan [127], I finally have a first answer to these questions Chris asked me eight years ago". Ref. [127] is the 2016 Optimization Online preprint "A parametric approach to the pooling problem". [inferred] Its journal descendant is R. Baltean-Lugojan & R. Misener, "Piecewise parametric structure in the pooling problem: from sparse strongly-polynomial solutions to NP-hardness", *J. Glob. Optim.* 71(4):655–690 (2018), DOI 10.1007/s10898-017-0577-y. The CV lists talks under both titles by the same authors.
- W4 (Oberwolfach, Oct 2015): her open problem "(13) [Misener] Practical rules for knowing when to apply SDP and RLT cuts together." Whether and how she pursued it is a question for 03.

**L2.8 Next agenda and declared ignorance.** [stated, P]
- T8 Q&A [38:03] (ASR, Mar 2023): data-driven constraints and uncertainty "have kind of been a little bit separate in my in my career and I would like them to be a little bit more together."
- On generative AI [40:57]+: "I don't understand it well enough to know ... how it would morph for change yet. We're starting to think about it, but I don't have any ideas at this point really."
- W7 (Jun 2026, latest): the talk "discusses formulating graph spaces using mixed-integer optimization and incorporating application-specific constraints ... We mention what has been done (by both ourselves and others) and what other research still needs to be done."

### Layer 3 · Idea generation

**L3.1 Read how practitioners write models, and look at the ugly function before relaxing it.** [stated, P]
- T8 (ASR):
  - [11:42] "one of the things that uh we found that was quite common was that people would uh sort of write down these mixer units ... What uh we noticed was basically well you have a lot of variables that are sort of like x is equal to y";
  - [12:44] "Adding these equations which were redundant in the original problem formulation tightened the relaxation. This was already known. But what we did was that we actually um found ways of getting these equations."
  - On Mistry's LMTD function [14:16]+: "he took this really ugly looking equation ... And what he noticed was that if you take this equation and you plot it out, well, it actually looks like its own relaxation already".
- T4 (2021, ASR) [12:17], on the same function: "automatic convexity detection is brittle"; [12:39] "hard-coded rules are easily tricked". [13:43] Hence the idea to propose "a hybrid between automatic detection and disciplined programming". The software is SUSPECT: F. Ceccon, J. D. Siirola, R. Misener, *Optim. Lett.* 14(4):801–814 (2020), DOI 10.1007/s11590-019-01396-y.

**L3.2 Between the cheap end and the expensive end of a hierarchy, build an intermediate family ("Goldilocks").** [stated, P] Count in C9.
- T7 (2023, ASR) [06:31]: "what I want to do is I want to develop um that's why I have this between formulations as my title um I want to develop relaxations that are somehow maybe between this level and this level".
- T3 (2021, ASR) [02:00]: being "in between either kind of strengthening the first order lesser [= Lasserre] or taking some linear approximations ... we are sort of in that family of work". The work is J. S. Campos, R. Misener, P. Parpas, "Partial Lasserre relaxation for sparse Max-Cut", *Optim. Eng.* 24 (2023), DOI 10.1007/s11081-022-09763-y.
- T2 (2021): partitions between big-M and convex hull; C. Tsay, J. Kronqvist, A. Thebelt, R. Misener, arXiv:2102.04373. Also J. Kronqvist, R. Misener, C. Tsay, "Between steps: Intermediate relaxations between big-M and convex hull formulations", arXiv:2101.12708 (CPAIOR 2021); and "P-split formulations ...", arXiv:2202.05198.
- W9 (ML-surrogates project page): "Prior literature often observes that the big-M formulation is too light and the convex hull formulation is too heavy. Our Goldilocks-style solution makes the optimization formulation just right for the application."

**L3.3 Turn known-but-annoying steps into software, and make competing research formulations switchable.** [stated, P]
- T5 (Mar 2022, ASR) [15:20]: embedding a trained tree ensemble "is a a solved item and people know how to do this however it can be annoying to program and omelette [= OMLT] is going to automate the translation".
- T6 [01:34]: coding the formulation yourself is "a bit of a waste of time if you're not actively doing research in the area".
- T6 [07:42]: "what omelette is trying to do is trying to show hey we can put these optimization formulations in competition and then the user can get whatever is the best without having to experiment with implementing every single one".

**L3.4 Ideas come from the team; her talks credit them.** [stated, P] Count in C8.
- T11 [02:47]–[02:50] (ASR): "I'm presenting the work of three uh super smart uh PhD students if at any point I refer to my work I actually mean their work".
- T2 [01:57]: "work that is done uh primarily by calvin say [= Tsay] and john cronquist [= Kronqvist]"; [41:18] "jan was able to prove quite a number of things uh related to this all of which i'm delighted about".
- T8: each buzzword is illustrated by a named student's or postdoc's idea ("what Mitten did", "Yan had another idea", "the ideas of uh Demetrius Leios" [sic, ASR: = Dimitrios Letsios]).
- T11 [25:58]: "the PHD student came to me and was explaining to me you know this doesn't actually work".
- Q6 (Dec 2023): the award "could only have been achieved through the support and collaboration of my excellent colleagues."
- T9 [29:07–29:19], local ASR, attribution inferred, on what she values in a researcher (R. Sedgwick): "She has this amazing ability to understand by my co-engineers are saying, and then turn it into something that kind of makes sense in respect to mathematics, and then do amazing research that then actually solves the problem."

**L3.5 Learn from "Jedi masters": borrow working rules from the best people in neighbouring areas.** [stated, P]
- T4 (2021, ASR) [24:15], on primal heuristics: "what i have learned from these jedi masters is that you ought to fail fast". W14 names them: "Ask the Jedi Masters ... Fischetti and Lodi [2010] / Berthold [2014] says to fail fast". The works are M. Fischetti & A. Lodi, "Heuristics in Mixed Integer Programming", *Wiley Encyclopedia of Operations Research and Management Science*, DOI 10.1002/9780470400531.eorms0376, and T. Berthold, *Heuristic algorithms in global MINLP solvers*, doctoral dissertation, TU Berlin, 2014.
- T8 [24:27]–[25:29] (ASR), the life version: she uses senior women colleagues in other fields as "best observed solutions": "I can't decide how to spend my time by copying any one of them, but I can kind of look to neighboring domains and try to figure out how they spend their time."

### Layer 4 · Experiments and execution

**L4.1 Computations must be reproducible; code, videos and slides go public, but partners' data stays with the partner.** [stated, P] Count in C7.
- W8 (CV, Dec 2025), under the heading "Reproducibility & Accessibility": "My research team develops and maintains open-source code on GitHub, releases video presentations on YouTube, and announces new research on LinkedIn".
- T7 [29:50] (ASR): "a lot of this kind of work depends on my ability to do computations that are reproducible".
- T10 [07:41] (ASR): "my group makes YouTube videos for every research paper that we do".
- Slides on Twitter: T3 [00:23] (ASR) "i've already put on twitter the slides"; W3 (2019, p. 1616) "Because this survey talk was meant for a fairly broad audience, the slides are available on Twitter".
- W11 (2017): "We will freely release our software on open-source platform Pyomo and build an international user community."
- W1 (2016, p. 14): Floudas made her promise "to write and publicly release a global MINLP solver" ("He was right in the end").
- T1 [03:46] (ASR), on the BASF work: "this is available open source at least the part that is sort of the algorithms and then of course the bsf data is within bsf".
- T9 [28:24] (local ASR, attribution inferred): "everything is reproducible, but it is online".

**L4.2 Give the competitor every advantage, and count every second your own method costs.** [stated, P] Count in C6.
- T3 (30 Apr 2021, ASR):
  - [24:29]: "we compare to big crunch [= BiqCrunch] basically as an oracle to make it so that things are a bit more fair for big crunch we um take some d we take some parameters that they suggest in their documentation um we run big crunch four times and we pick the best of the four big crunch uh answers just to try to be less abusive".
  - [29:44]: "when we compare against them we're truly not trying to set ourselves up as a competitor you know it is rather that hey cool wouldn't they could we convince these big crunch people to also implement these ideas".
  - [29:04], on reporting the time spent building the relaxation: "i thought in our paper we should also have um timings where we are including our building and we're fast we're still fast but we're not going to be orders of magnitude fast".
- T2 (Apr 2021, ASR):
  - [29:07]: optimality-based bounds tightening is run for all variants, "where basically we give all the different strategies sort of equal opportunity";
  - [34:25]: "all of these are solved with our equal uh size strategy so we're not there's no funny business here with respect to sort of changing where the inputs are".
- J4 (Dagstuhl 2018; the organisers' summary is [stated-joint], the working-group conclusions are [observed]):
  - the organisers devoted a break-out session to best practice in computational experiments (paraphrase);
  - the working group concluded on "the need to incorporate experimentation on permuted models as has become standard in the MIP community", and "the affirmation that conducting fair benchmarks between different solvers remains inherently difficult and users of solver software should not rely on simplistic comparisons."

**L4.3 Design the test so that the baseline can win some of it, and add deliberately bad variants as controls.** [stated, P]
- T2 [33:02] (ASR): "we're choosing um that epsilon such that big m can solve some of the problems ... that way we have a good comparison point".
- T2 [28:38]: proposed partitions are compared with random ones and with "an alternative that we posit would be even weaker would be uneven magnitudes". T7 [29:22]–[29:27] says the same: "the way I will try to show that we have something that is something somewhat reasonable is that I will compare this to uh random partitions".
- T11 (2025, ASR):
  - [31:30] the new path-based method must not break ordinary Bayesian optimisation: "you'd better hope we're not too different from Thompson sampling because if we're different than Thompson sampling then we sort of by choosing this path we might have messed everything up";
  - [32:03]–[32:27] a Sobol sequence plus a travelling-salesman tour serves as the space-filling reference: "we are roughly as space efficient as uh as soble [= Sobol]".

**L4.4 Without a proof, say so and run many experiments; keep the claim experimental.** [stated, P]
- T2 [28:19] (ASR): "i don't have a way of proving this and so what i'm trying to show rather than doing any proof is just a lot of experiments".
- T7 (2023, ASR):
  - [23:28], asked how quality is judged: "it's only running time it's very it's very experimental right";
  - [23:56]–[24:08]: "if you just told me to pull out of my hat prove to you what is the best value of N I would have to say no I'm sorry so it's going to be it's going to be heuristic and then somehow um I'm going to hope that some problems are similar enough to one another";
  - [38:41]: "I can only say it experimentally".
- T8 Q&A [39:56]+ (ASR), crediting a current PhD student: "you sometimes you want to see how far you can get mathematically before we start making approximations ... where maybe I want to see how well can I do things using all of these tricks before now I'm like okay that's as far as I can go and now I'm going to start in on these approximations as very problem dependent".

**L4.5 Separate the assumptions a proof needs from the assumptions the practical regime needs.** [stated, P]
- T2 (ASR):
  - [37:01]: "i don't strictly need this first assumption this would work also for something that was partially additively separable but anyway um for now it makes my proofs easier";
  - [37:18]: "i don't need this one at all for the proofs it is rather that we need this for um the for the practical case that we think that this particular line of thought is reasonable".
- T7 [12:04] (ASR), on the same assumption: "this is an engineering Choice that's just based on our observations"; [12:22] "you'd better hope that that n is much smaller than that d".

**L4.6 Toy examples are for intuition only; look at the raw results behind a summary plot.** [stated, P]
- T2 [18:53] (see L1.3).
- T2 [22:45] (ASR): "what's going on if you sort of dig into the data which you can't with this plot but i know from looking at it is that n is equal to 2 is solving the easy problems uh very very quickly".

**L4.7 Software engineering is part of the research; tests prove quality.** [stated, P]
- T5 [01:17] (ASR): "we're pretty serious about the software engineering in omelette so we do have quite a number of tests for the omelette code we are passing these tests the code coverage is 94 and then we also have a nice api documentation".
- T8 [29:04] (ASR): "we tried to make this uh real at BSF and two we tried to make this real with respect to doing reasonable software engineering".
- Q5 (Nov 2022), on an undergraduate's OMLT contribution: "not only did Adi successfully implement state-of-the-art research technology before taking the prerequisite modules, but he also proved his work's excellence to everyone on our team by developing effective testing examples."
- W9 (MINLP project page): "We have also developed open-source code GALINI that acts as our sandpit for testing new MINLP approaches."
- W8: as an AIChE CAST division director (2016–18) she "initiated the Software Tools & Implementations session at the annual meeting".
- T9 [28:17–28:37] (local ASR, attribution inferred), on a late-stage PhD student's work going to BASF: the task is "picking which aspects from his PhD does he want to implement ... in such a way that it's really, really, like, so solid" [sic, ASR].

**L4.8 Stated algorithm-design rules.** [stated, P]
- Cheap first: W9 (MINLP page) "We try to generate the computationally inexpensive cuts first".
- Heterogeneous frameworks: W9 "In practice, solving MINLP is tractable via heterogeneous algorithms pieced together into a framework; we develop and integrate complementary algorithmic components." See also L1.5.
- Fail fast (heuristics): L3.5.
- Branching effort scales with the cost of exploring: T8 [16:19] (ASR) "if you can explore possibilities very very quickly, you're going to um uh you're going to maybe be willing to explore tons of possibilities. If it's going to take you a long time to explore the different possibilities, maybe you want to be a little bit more parsimmonious [sic]".
- Open challenges as a to-do list:
  - W3 (2019, p. 1617): "A major challenge for the future is relaxations that are not based on boxes"; branching "is an especially difficult area in solving MINLP because a branch may not necessarily eliminate the current feasible point".
  - W14 (final frame): "Challenges [with some ideas]". Data structures: "Move beyond boxes"; convex relaxations: "How many auxiliary variables to introduce? • Manage symmetry"; branching: "Get disjunctions"; bounds tightening: "Incorporate multiple constraints"; and "Integrating machine learning".
  - T4 [24:35] (ASR): "for convex relaxations we do need to move beyond boxes".

**L4.9 Keep people in charge: no full automation of experiments; solutions that do not upset the people who carry them out.** [stated, P]
- T10 [51:59]–[52:02] (ASR): "I personally would not want everything automated um at least my collaborators at BSF would not ... at least at BSF what you're going to see is people wanting to really um yeah sure we take the advice from the algorithms but also we are very much involved with it".
- Q1 (early 2021), on Royal Mail scheduling: "If you're a postal worker, and you're told the night before what you're going to be doing, you don't want the story changed on you during the day ... Last minute changes cause chaos and this is not really a way to lead an organisation filled with people. One of the things we aimed for in our solution was to avoid changing the schedule too much."
- Contrast: her own talk title "Autonomous research machines" (W6, T11). See Contradictions.

**L4.10 Build uncertainty into the model, and agree its assumptions with the stakeholder.** [stated, P]
- Q1 (early 2021): "if you don't have an understanding embedded into your optimisation that the world is an uncertain place, then you're probably going to get a bogus solution that is going to hurt you once you implement it. If you explicitly take into account that you're not quite sure what's going to happen, you can get answers that are actually robust to things going wrong."
- T1 (2021, ASR):
  - [35:15]: "it's not that there's one type of uncertainty it's many types of uncertainty";
  - [36:11]–[36:15]: "if it's an algorithm right there has to be a certain set of assumptions and uh what we try to do with stakeholders is identify what are uh the assumptions when we're designing an an algorithm for them".
- J3 [stated-joint] (2023, abstract via OpenAlex):
  - the paper "first considers essential conditions for robustness to uncertainties and accurate extrapolation, which are required to integrate surrogates into process optimization";
  - it discusses "the verification problem, i.e., checking that the optimum of the surrogate corresponds to the optimum of the truth model".

### Layer 5 · Judging results (when to believe a result; negative results)

**L5.1 A parameterised method is good only if one parameter setting stays good across a problem class.** [stated, P]
- T7 [40:59] (L1.7).
- T3 [27:12]: "we're pretty confident in them for a fairly large variety of problems".
- T2 [32:29]: "choosing these parameters tends to be fairly robust"; [47:30] on the clustering instances: "these results are actually fairly robust across parameters with respect to number of variables in each one of the splits".

**L5.2 Say where you lose.** [stated, P] Count in C5.
- T7 (2023, ASR):
  - [25:41] "there are definitely places you're going to be worse than Big M";
  - [37:54] "it's no Silver Bullet";
  - [33:21], on a cutting-plane variant: "so that kind of works um but uh not really".
- T3 [26:07] (ASR): "for a few problems um they are faster than us".
- T11 (2025, ASR): [20:17] "not trying to claim it's the perfect thing"; [30:57] "they kind of all look the same to me".

**L5.3 Outside validation counts: solver developers, competing groups, uptake.** [stated, P]
- T7 [32:43] (ASR): "I have it from Pierre bonami who has implemented this that sometimes this is better so that he so uh if Sarah agrees with me then I'm uh I think I'm I think I'm doing something right" [sic, ASR: "Sarah" is unresolved; it may be the name of the solver Bonami worked on, not verified].
- T3 [26:39]–[26:55] (ASR): another group "did um then come out with another paper that kind of uses our partial uh augmented relaxation idea and improved on it ... i admit we have not tested since uh they made these improvements um but i am excited that they also got our same sort of results saw that they worked and then improved on it".
- Q4 (Oct 2022): "The acceptance into NeurIPS is a marker of the recognition our work is receiving from the wider machine learning community."
- Q7 (Aug 2024): "It's fantastic to receive recognition from the flagship journal in the process systems engineering community for work that is both academically pioneering and has important practical value to industry".
- Uptake numbers she cites:
  - T8 [29:04] (ASR), OMLT: "we're we're doing 20,000 downloads a month and have been for the last year";
  - W11 (key findings, ≥2025): "OMLT, the most popular of the packages, has >500k downloads"; "Our software output ENTMOOT is actively used within BASF".

**L5.4 Notice when a design defeats its own purpose (the SnAKe episode).** [stated, P]
- T11 (Jan 2025, ASR):
  - [25:58]: "the PHD student came to me and was explaining to me you know this doesn't actually work";
  - [26:06]–[26:13]: "what I like so much about Bas opt is that it's a global optimization method and all I had done with this set of ideas is I had taken a global optimization method and I had turned it into a local optimization method";
  - [28:13]: "that's what we know from first order optimization that's not so tough I should have understood this".
- The fix was the student's ("point deletion"), and it introduced a parameter (L1.7).
- Paper: J. P. Folch, S. Zhang, R. M. Lee, B. Shafei, D. Walz, C. Tsay, M. van der Wilk, R. Misener, "SnAKe: Bayesian Optimization with Pathwise Exploration", arXiv:2202.00060 (NeurIPS 2022).

**L5.5 Theory is valued when it explains or predicts computation.** [stated, P] This is the counterweight to L1.2.
- T3 (2021, ASR): [00:47] "i think the laser [= Lasserre] hierarchy is the the coolest thing ever"; [01:22] "the problem that at least i have with it as somebody who really likes computation is that ... i still personally have difficulty uh getting these things to solve when we're working with medium to large-scale polynomial problems".
- T7 [04:57] (ASR), on higher levels of the reformulation-linearization hierarchy: "my computational experience and my understanding of the way also the proofs work is that uh it starts to be maybe not such a good idea".
- T10 [26:32] (ASR), on Gaussian processes: "I really like uh how it has a really nice um uncertainty properties and I like um the sort of proofs that uh people uh work with uh related to Gin processes" [sic, ASR: = Gaussian processes].
- W1 (2016, p. 13): she reports her "first answer" to "Why did these piecewise approximations work so well?" (L2.7).

**L5.6 Results on industrial problems have a low ceiling (see L2.4); results reported in talks are selected (she says so).** [stated, P]
- T1 [17:10] (ASR): "the presentation that i gave of course were um data sets that happen to be perfect for my research right".
- T10 [38:31] (ASR), on Bayesian optimisation: "my computational experience and this is this is similar to the experience that I see in every paper so I I really don't think it's just me is that for whatever method you have basically you have these diminishing returns".

**L5.7 Uncertainty in results must be communicated and engaged with, not hidden.** [stated, P]
- T1 [16:49] (ASR): "i would want decision makers to actively engage with the uncertainty and sort of explain the uncertainty to um uh stakeholders".
- Q2 (cleaned version of the same answer): "One of the challenges of decision-making under uncertainty is communicating uncertainty with humans."

### Layer 6 · Writing, talks and teaching

**L6.1 A talk is for dialogue: end with open questions and ask the audience to extend the list.** [stated, P] Count in C3.
- T3 [00:10] (ASR): "i'd much prefer to hear from you all".
- T4 [25:00] (ASR): "i'm also interested in just sort of starting a dialogue here and so my question is what's missing on this list anything here easy to manage you'll definitely make my day if so". W14's final frame reads: "My questions . . . What is missing on this list? • Anything here already easy to manage?"
- W3 (2019, p. 1617): "We closed the presentation by offering a number of open challenges and invited the audience to add to the list."
- T2 [45:07]: "i hope that i'll get a lot of questions".
- T10 [02:44]: "what the real Advantage is is the the chance that we have to discuss here".
- T11: [01:28] "if I do not get through my presentation I truly do not care it would be much more interesting to hear what you all have to say um because I already know my research"; [32:44] "I just stop when people tell me to stop".
- W7 (2026): "We mention what has been done (by both ourselves and others) and what other research still needs to be done."

**L6.2 Put the weakness on the first slide.** [stated, P] Count in C5.
- T7 (ASR): [02:16] "I'm kind of giving you right away the criticism that you might all have which would be very reasonable"; [06:37] "the sort of admitting right at the beginning where a possible problem is going to be".
- T3 [18:51]: "the possible negative side".
- T2 [32:15]: "the bad uh news is that if you want to use our work you've got to choose uh two basically new parameters".
- T11 [28:23]: "alert alert I'm going to introduce a parameter".

**L6.3 Explain through everyday analogies and the audience's own field; keep equations off slides for non-specialists.** [stated, P]
- T8 [09:10] (ASR): "what I will try to do for each of these six is that I want to introduce um what is sort of important uh from both a life and a research point of view. So basically trying to argue how life and research go together."
- T10 [07:23] (ASR): "I will shy away from presenting uh the mathematics so there are no equations on my slide there's a lot of mathematics that goes into this work"; [08:38]–[09:08] she compares design of experiments with adapting recipes and choosing between cycling and driving.
- T11 [03:06] (ASR): "I really wanted to give a sort of Chemistry Style presentation here because I know that you all are exceptionally good at sort of the fundamentals of AI".
- W5 (2022): "This presentation is biased towards the kind of optimization I understand, so it mostly concerns mixed-integer nonlinear optimization."
- W2 (2014, abstract) lists four purposes: "(1) demonstrating global optimisation as an exciting research domain; (2) describing several industrially-relevant applications; (3) highlighting complementarity between disparate CPSE research groups; (4) offering a list of publications for further reading."
- T7 [01:47]: of "Between formulations or: How I Learned to Stop Worrying and Love Parameters": "this is like my favorite seminar title".
- O1 [observed, S] (Pistikopoulos, T8 [49:07]+): "a person who can elaborate present things of that level of complexity in such a way that everybody can associate with this".

**L6.4 Admit ignorance in public.** [stated, P]
- T10 (ASR): [03:21] "small but embarrassing secret um all of my worst marks are in chemistry"; [03:42] "I know enough chemistry to know that my chemistry is weak"; [33:09] "I will probably handle them badly again and sayy I don't even know what that word is".
- T3 [28:27] (ASR): "i'm ignorant enough about these sorts of algorithms that i'm not sure if it's because of our implementation or if it's just that it's a difficult uh problem".
- T2 [52:32] (ASR): "that is a really good question i will have to get back to you on that".
- T4 [00:04] (ASR): "i myself am not an expert in an mpc [= NMPC]".

**L6.5 Grants: sharpen the argument by mutual critique; answer reviewers with "disappointment".** [stated, P]
- T8 [26:30]–[27:32] (ASR), formulations as a way to "sharpen the argument": "where at Imperial um I have to most work on sharpening my argument um is when I'm working on uh uh grant writing and interview prep. Something that we do really well at Imperial is um or rather a lot of people have done very well for me um is reading each other's grants, telling each other where uh we're weak and uh really uh trying to uh improve things."
- T8 [34:44]–[35:15] (ASR), on her partner's help with grants: "his ace in the hole is grant rebuttals" ... "the the key is disappointment. You're disappointed that the the reviewer didn't understand."

**L6.6 Teach from your research; prepare students with the right courses.** [stated, P]
- W8 (CV), on the course Computing for Optimal Decisions: "Finalist for 2016 Best Innovation in Teaching ... The teaching innovation recognition is due to how frequently I discuss research in the classroom."
- W9 (Teaching page): "I strongly recommend that anyone who wants to do a research with project me take 60016 Operations Research and 70007 Computational Optimisation." [sic]
- W10: "Using both traditional lectures and open-ended projects, I mentor and teach Imperial students as they prepare for their technical careers."
- T8 [32:38] (ASR): executive education as "messy play with optimization, but now in the uh the teaching way".

### Layer 7 · Research organisation (time, students, collaboration, agenda)

**L7.1 People first, research and teaching second (a rule she credits to Floudas).** [stated, P]
- T8 [03:34] (ASR): "when I do it correctly uh I remember to put uh the the people first and then what the things that we do here in the university the research and the teaching second and um he's the one who taught me that".

**L7.2 The adviser matters most; a good adviser asks for more than seems reasonable and believes in the student.** [stated, P]
- W1 (2016, p. 12):
  - "My father often repeated in my childhood that choosing an advisor is the most important decision a graduate student makes."
  - "Whatever mistakes I made as a Ph.D. student, I did one thing exceptionally well: I was privileged to work for Professor Christodoulos Achilleus Floudas."
  - "Chris's commitment to excellence was inspiring; his belief in his students was motivating; his enthusiasm for global optimization was contagious."
- W1 (2016, p. 14): "In 2008, when Chris told me that my early-stage Ph.D. assessment needed a promise to write and publicly release a global MINLP solver, I told him he was being unreasonable. He said to do it anyway; and I must have made a face, because I remember him telling me sharply: "you will not roll your eyes at your advisor!" He was right in the end".

**L7.3 Route each incoming problem to the group member best suited to it.** [stated, P]
- T1 [17:26]–[17:58] (ASR).
- Q2 (cleaned): "What we do – and the Imperial Enterprise team is extremely good at this, and within our research groups we are good at this as well – is that when a new problem comes in we figure out what components the stakeholder needs, and then redirect the problem … and what we do is try to deploy the individual problem to the person who is best suited to it."

**L7.4 Collaborate by contributing to the same open-source code.** [stated, P] Count in C7.
- W11 (key findings, ≥2025), on the Sandia partnership: "we had planned several in-person secondments, but because everything moved online, we switched to a model of just actively contributing to the same open-source projects). Because of the similar goals shared between the teams at Imperial and Sandia, we have accomplished more on the grant than we expected."
- T5 [00:31] (ASR): "please join us on github there's plenty of contributing to do".
- T10 [06:19] (ASR), on BASF's BoFire consortium: "a nice way for industry and Academia to collaborate".
- T11 [07:14] (ASR): BoFire "is your way of possibly getting uh your stuff into BSF ... I am funded by BSF so uh I am also you know my my PhD students are paid to put it put it put their things in". The package is described in J. P. Dürholt et al., "BoFire: Bayesian Optimization Framework Intended for Real Experiments", arXiv:2408.05040; Misener is a co-author.

**L7.5 Use the institution: enterprise teams, doctoral-training centres, finance and pre-award staff.** [stated, P]
- T8 (ASR): see L2.1 on the Enterprise team and CDTs.
- [16:49] finance and pre-award teams help her "explore possibilities but in a way that isn't sort of completely insane all of the time".
- [20:55] good support administrators "scaffold you and make it possible to make decisions".

**L7.6 High standards come from peers who say "be better".** [stated, P]
- T8 [23:57]–[24:27] (ASR), on senior women colleagues: "how these people are is roughly along the lines of be better. You have to be as good as we are. Um, because otherwise you're a letdown. And they are very, very intense. Um, and they, uh, make me be better a lot."
- See also L6.5 (grant reading) and L3.5 (time allocation by observing them).

**L7.7 Build fellows' independence; praise students for research and for what the client gained.** [stated, P]
- W8: "I collaborate with research fellows and assist in developing their independent research careers."
- W13 (May 2019): "This recognition honours not only Natasha's research excellence, but also her significant contributions to a client organisation, in this case the Royal Mail Data Science Group."
- W12 (Feb 2019): "Simon also makes his work publicly available, e.g. the open-source Python library GPdoemd".

**L7.8 Optimisation training transfers across applications; graduates build algorithms on top of commercial solvers.** [stated, P; T9 local ASR, attribution inferred]
- T9 [44:18]–[44:27]: of commercial solvers, "you don't need a PhD in mathematical optimization to use the kind of tool that Timo develops".
- T9 [44:50]–[46:26]: of two people she works with ("both Eaton and Johannes are here" [sic, ASR: "Eaton" unresolved]; [inferred] Johannes is probably her former PhD student Johannes Wiebe), she says they "did PhDs that were somehow related to chemistry or chemical engineering applications somehow. And now they're effectively doing solar [= solver] development with respect to supply chain and semiconductor manufacturing ... those problems are so enormous that they cannot help but do solver development effectively on top of what Timo is doing ... for people who are super talented, it's a pretty easy move to a different application."

**L7.9 Self-report: she does not follow her own advice to relax.** [stated, P]
- T8 [33:39] (ASR): "if there's one thing I'm really not able to do, it's relax." The title is "How I'm bad at my own algorithmic advice".
- Q8 ([stated-inst]): the lecture acknowledges "her ironic struggles to achieve more traditional forms of relaxation in her real life".

**L7.10 Community infrastructure is a contribution in its own right.** [stated, P / stated-joint]
- W1 (2016, p. 14), on Floudas and Pardalos's test-problem handbook and encyclopedia: "These books brought significant attention to deterministic global optimization and supported the careers of many researchers."
- J4 (2018, [stated-joint]), organisers' summary: the seminar brought together MIP and NLP experts ("we leveraged the best methods from both by incorporating both sets of experts"). It also produced "a new set of metrics for comparing MINLP solvers".
- W8: among her CAST-division initiatives, "created an online Poster Kiosk to increase poster session prestige" and the software session (L4.7).
- Q3 (Mar 2022): "My existing collaboration with BASF colleagues is already very rewarding. Together with Imperial researchers and the Data Science for Materials and Chemicals teams at BASF, we have already made contributions in data-driven optimisation and developed open source software."

## C. Recurring stated claims (≥3 independent sources = a real belief)

"Sources" counts distinct sources, not repeats within one talk. A talk and its own slides (T4 + W14) count once. Press quotes count only when they are not a re-quote of a talk already counted.

| # | Claim | Sources | Dates | Where | Layer items |
|---|---|---|---|---|---|
| C1 | Find and exploit the problem's special structure; let structure be its own relaxation | 7 | 2014–2023 | W2, W1, W3, T4, T2, T8, W9 | L1.4, L3.1 |
| C2 | Push the tractability boundary: solve what could not be solved; small speed-ups are not research | 6 | 2016–2023 | W1 (as praise of Floudas), W11, T2, T7, T8, W9 | L1.1 |
| C3 | Talks are for dialogue; end with open problems and invite the audience to add | 7 | 2019–2026 | W3, T3, T4/W14, T2, T10, T11, W7 | L6.1 |
| C4 | Parameters are a cost: remove them or show they do not matter | 5, plus one talk title used at 5 venues | 2016–2025 | W1, T3, T2, T7 (title 2022–23), T11 | L1.7, L5.1 |
| C5 | State weaknesses, losses and selection effects up front; distrust your own metric and your co-author bias | 7 | 2021–2025 | T1, T2, T3, T6, T7, T11, W5 | L1.8, L5.2, L5.6, L6.2 |
| C6 | Fair comparison: strongest competitor settings, equal opportunity, controls, total time | 5 | 2018–2025 | J4 (joint), T3, T2, T7, T11 | L4.2, L4.3 |
| C7 | Release code, videos and slides; collaborate through shared open-source code | 9 | 2016–2025 | W1, W11, W3, T3, T5, T7, T10, W8, T11 (and T9, low grade) | L4.1, L7.4 |
| C8 | Credit students and team; their ideas are the group's ideas | 6 | 2019–2025 | W12/W13, T2, T8, Q6, T11 (and T9, low grade) | L3.4, L7.7 |
| C9 | Build intermediate ("between", "Goldilocks") formulations between a cheap weak end and an expensive strong end | 4 | 2021–2023 | T3, T2, T7, W9 | L3.2 |
| C10 | Borrow from neighbouring communities, and recruit them to your problems | 6 | 2019–2025 | J1 (joint), J2 (joint), T4, T7, T10, T11 | L2.6, L3.5 |
| C11 | A method has a domain; say where it ends (against techno-solutionism) | 5 | 2014–2024 | W2, T1, T6, T8, T10 | L1.9 |
| C12 | Choose problems where a standard method's assumption breaks in a real application, ideally several at once | 5 | 2022–2025 | T6, W6, T10, Q7, T11 | L2.3, L1.2 |
| C13 | Global optimality matters because local answers can be wrong | 6 | 2014–2025 | W2, W1, J1 (joint), T8, T10, T11 | L1.6 |
| C14 | Messy, heterogeneous, real problems over clean ones | 7 | 2016–2025 | W1, J2 (joint), T8, W6, T10, T11, T9 (low grade) | L1.2, L1.3 |
| C15 | Software engineering (tests, documentation, hardened code) is part of the research | 5 | 2016–2024 | W8, T5, Q5, T8, W9 (and T9, low grade) | L4.7 |
| C16 | Model uncertainty explicitly and communicate it to the people who decide | 4 | 2021–2023 | Q1, T1, T8 (agenda), J3 (joint) | L4.10, L5.7 |

Stated fewer than three times, so recorded but **not** treated as established beliefs:
- people first (T8 only);
- the adviser is the most important choice (W1 only);
- direction chosen by "pub buddies" and opportunity (T8; partly T11);
- the industrial ceiling (T8 only);
- leaving solver development to industry (T9 only, low grade);
- humans in charge of experiments (T10, Q1);
- "fail fast" (T4/W14 only);
- cheap cuts first (W9 only);
- grant critique by peers (T8 only).

## D. Self-reported failures, abandoned directions, rejections and limits

| # | What she reported | Source | Tag |
|---|---|---|---|
| D1 | Her first path-based Bayesian optimisation design "doesn't actually work": it turned a global method into a local one. She says "I should have understood this"; a PhD student found the problem and fixed it | T11 [25:58]–[28:13], Jan 2025 | [stated, P, ASR] |
| D2 | Partition strategies: "this is a lot of failed things before stuff worked". Grouping inputs that are "close in euclidean distance ... no that didn't work". "we just feel like we're in the dark on this" | T2 [53:09], [53:46]–[53:54], [55:35], Apr 2021 | [stated, P, ASR] |
| D3 | A fellowship proposal she says her partner rescued with a rebuttal: "He got me out of, um, uh, 346 going into, uh, a a um, a fellowship proposal and, uh, I got the grant." [sic, ASR: "346" unresolved, possibly review scores; which fellowship is not said] | T8 [35:15], Mar 2023 | [stated, P, ASR] |
| D4 | As a PhD student she objected to the 15,439-variable model and called the demand to release a solver "unreasonable"; "He was right in the end" | W1 pp. 13–14, Oct 2016 | [stated, P] |
| D5 | A cutting-plane variant of the split formulation: "so that kind of works um but uh not really" | T7 [33:21], Feb 2023 | [stated, P, ASR] |
| D6 | Slow relaxation build times that may be her implementation's fault. Competitors improved her code, and she has "not tested since" | T3 [28:27], [26:53], Apr 2021 | [stated, P, ASR] |
| D7 | Higher levels of the Lasserre and RLT hierarchies are hard to solve at medium or large scale; she prefers partial levels | T3 [01:22]; T7 [04:57] | [stated, P, ASR] |
| D8 | Less solver development "at this point" | T9 [30:31], Jan 2024 | [stated, P; local ASR, attribution inferred] |
| D9 | GALINI changed description over time: the 2017 plan was "new decision-making software" with "an international user community"; the homepage now calls it "our sandpit for testing new MINLP approaches"; Researchfish says "We have achieved what we wrote in the grant proposal". Whether the user community materialised is a question for 03 (01 notes no journal paper on the general solver as of the Dec 2025 CV) | W11 (2017; ≥2025), W9 | [stated, P] |
| D10 | Declared limits of her reach: generative AI ("I don't have any ideas at this point really"); drug design ("perhaps that's just I'm not imaginative enough"); Bayesian optimisation beyond about 10 dimensions ("starts having asterisks") | T8 [41:28], [42:30]; T10 [23:51] | [stated, P, ASR] |

## E. Era and resource context of the stated methods

- **E1 (PhD, 2008–2012/13).** The norms she later states as her own were presented to her as her adviser's demands: real-world instances, public solver release, and answering why an approximation works. The account of this period is retrospective (W1, written 2016). Resources then were a C++ solver on one workstation, two-author papers and an NSF fellowship (see 03).
- **E2 (2012–2017).** RAEng fellow in Chemical Engineering, then Lecturer in Computing. The 2014 article (W2) frames research as "engineering applications; mathematical algorithms; computational software", for an industrial consortium audience. Scope statements about when global optimisation is worth its cost date from here.
- **E3 (2017–2022).** EPSRC fellowship with funded software staff. Stated aims are open-source release and a user community (W11, 2017). The 2021 talks (T1–T4) are virtual pandemic-era seminars. Several stated habits come from this period: dialogue, slides on Twitter, fairness to competitors. In W11 she says the pandemic changed how the group collaborates, towards shared open-source projects.
- **E4 (2019/2022–2026).** Full professor (2020) and BASF/RAEng chair (2022), with industrial PhD funding and machine-learning venues. Statements here concern Bayesian-optimisation scope, keeping humans in charge, consortium software (BoFire), the ceiling on industrial improvement, getting industrial funding via CDTs, and (T9) leaving solver development to industrial teams. They presuppose a mid-size group with several funders. [inferred] They are not advice for a lone student with no partners.
- **Audience.** [inferred] The weakness-first, self-deprecating register appears both with specialists (T2, T3, T7) and with outsiders (T10, T11), so it is unlikely to be only audience adaptation.

## Contradictions (kept, not reconciled)

1. **Proofs.**
   - [30:35] of T8 (2023): a bare convergence proof is something "boring and I'm not interested" in.
   - Against this:
     - T3 (2021): the Lasserre hierarchy is "the coolest thing ever";
     - T10 (2024): she likes "the sort of proofs that uh people uh work with uh related to Gin processes" [sic, ASR: = Gaussian processes];
     - T2 [41:18] (2021): "jan was able to prove quite a number of things ... all of which i'm delighted about";
     - J1 [stated-joint] (2019) opens: "Designing and analyzing algorithms with provable performance guarantees enables efficient optimization problem solving";
     - W1 (2016) presents her "first answer" to *why* piecewise approximations work as a milestone.
2. **Parameters.**
   - Her 2022–23 title promises "How I Learned to Stop Worrying and Love Parameters".
   - The same talk calls them "one of the the weaknesses of this" (T7 [02:28]).
   - In 2025 she says "I don't like to introduce parameters" (T11 [29:40]).
   - In 2016 she reported the goal to "eliminate the computational dependence on parameters" (W1 p. 13).
3. **Industrial impact.**
   - Lecture Q&A (T8 [45:03], 2023): on real industrial problems "really jumping forward doesn't happen so much".
   - Press quotes: the BASF work "is helping digitally transform the chemical industries ... This will help create better and more sustainable chemistry" (Q4, 2022); the work "has important practical value to industry" (Q7, 2024).
4. **Automation.**
   - Her talk title since 2023: "Autonomous research machines: Self-optimizing new chemistry" (W6; T11; CV S40, S44, S47, S48, I42, I53, I54, K22).
   - T10 (2024): "I personally would not want everything automated".
   - In T11 [04:52] she attributes the autonomous-machines vision to "the guy who is the boss of the guy the people who I collaborate with" at BASF.
5. **GALINI.** Three descriptions, three dates (D9):
   - "new decision-making software" with "an international user community" (2017);
   - "our sandpit for testing new MINLP approaches" (undated homepage);
   - "We have achieved what we wrote in the grant proposal" (Researchfish, ≥2025).
6. **How the agenda is set.**
   - "I'm a person who chooses my ... vision in some part by my pub buddies ... So in some ways very opportunistic" (T8, 2023).
   - Against this: a planned, application-specific programme in the 2017 grant abstract ("safely operating batch reactors, retrofitting heat-exchanger networks, intermediate blending, and integrating planning and scheduling", W11).
   - Also against this, a reporter's framing (Q3, 2022): "Professor Misener believes that developing data-driven, optimal decision making under uncertainty is key to achieving a sustainable society" (reporter's paraphrase, not her words).
7. **Solver building, early versus late.**
   - Early: "I really enjoyed developing the solvers" (W1, 2016). She also put "a to-do list for developing next generation solvers" to the community (W3, 2019; T4, 2021).
   - Late: "at this point, I don't work as much on solver development" (T9, 2024; low-grade ASR, attribution inferred).
8. **Toy problems (minor tension).**
   - W1 (2016) praises Floudas because he "was never interested in toy problems or proofs of concept".
   - Her own expository texts open with a two-variable toy example (W2 "Example (1) is a toy problem with only two variables"; the W9 MINLP page "Consider a toy MINLP"; T4 and T8 pictures).
   - Her own stated rule (T2 [18:53]) limits toy examples to intuition.

## Gaps (what could not be found or read)

- **No first-person methodology text.** Searches found no essay, blog post, lab guide, interview, or advice to PhD students on how she does research: two WebSearch calls (interviews/podcasts; profile/advice) plus a YouTube search for her name. The stated layer is therefore built from asides in talks and short texts.
- **Writing.** Nothing found on how she structures papers, drafts, divides writing among co-authors, or reviews (the CV lists "Top Reviewer" recognitions only). Layer 6 here covers talks, grants and teaching, not papers.
- **Supervision detail.** No stated rules on meeting cadence, milestones, authorship or stopping projects. See `04-mentorship.md` for observed evidence.
- **Opened but unusable (15):**
  1. Data-Centric Engineering webinar panel at AIChE, "Data Science in Chemical Engineering" (15 Dec 2020; YouTube utlg8UF74u8; she is a listed panellist). The caption endpoint returned HTTP 429 on every retry. **Not read.**
  2. Isaac Newton Institute talk, 24 Apr 2023 (KX9Tzt_WLOM). The video has no captions; only the abstract (W6) was used.
  3. "AIChE Journal Looks to the Future" (2019, I1dPxAj6-fg). Several unlabelled speakers; no line can be attributed to her.
  4. RAEng film "Supporting engineering research" (2017, 2gYp1nm6D3M). Unlabelled speakers; not attributed.
  5. RAEng film "Engineering at the heart of society" (2015, fFW1wWgsSNY). Unlabelled speakers; not attributed.
  6. EURO 2021 WISDOM "Women in Operations Research" panel. Only a 45-second promotional clip (4da8PA2Y8Zw) was found; no recording of the panel.
  7. AIChE CAST 2020 awards video (2A5nmWJfmNw). She did not speak; only a thank-you slide was shown.
  8. Misener & Biegler 2023 (J3), full text. Publisher HTTP 403; not in Spiral; abstract only.
  9. AIChE "35 Under 35" profile (2017) and the AIChE bio page: HTTP 403.
  10. LIYSF principal-lecture page: HTTP 404.
  11. Full Spotify audio of T9: login required, not attempted. The public Acast MP3 was used instead.
  12. Imperial News, "Imperial researchers publish 17 papers at the NeurIPS 2022 conference" (her text, 13 Oct 2022). Read; no methodological statement.
  13. Imperial News items of 2 Jun 2021 (Schlumberger software) and 18 Jul 2022 (BASF partnership). Read; no quote from her.
  14. GtR record EP/W003317/1 (ADOPT). Read; the PI is B. Chachuat, so it is not her voice.
  15. ICCOPT 2025 speaker page. Read; bio only.
- **Talks listed in the CV but not found as recordings or texts:**
  - EURO 2021 semi-plenary "Computational Mixed-Integer Nonlinear Optimization";
  - RAEng Fellows' Day keynote "Optimisation under Uncertainty: Engineering & Life" (2018). The title suggests the same life/research pairing as T8; not read;
  - Princeton Saville Lecture (2023) and Purdue Mellichamp Lecture (2024);
  - LION 18 plenary (2024) and the FOCAPO/CPC 2023 joint keynote with Biegler;
  - the SIAM OP26 plenary (2026; abstract only, W7);
  - the 2013 talk "Architecting ANTIGONE: Design Choices and Tradeoffs".
- **Not read for other reasons:**
  - Twitter/X: her own threads (she posts slides there; W3 cites one tweet) are behind a login wall.
  - Her PhD thesis (2012): preface and acknowledgements not read.
- **Unresolved items in the ASR captions:**
  - "346" (T8 [35:15]);
  - "Sarah" (T7 [32:43]);
  - "10 percentable to be a sector Works" (T7 [32:16]);
  - the paper she calls "one of my very favorite papers from the last uh uh 10 years um I make everybody do it" (T7 [10:25]). It is credited to the host "Andrea" and concerns shrinking big-M values. It is not identified, and "do it" may be a misrecognition of "read it";
  - "a paper from 2018 ... in siam journal of optimization" (T3, on partial Lasserre orders): not identified;
  - "Eaton" (T9 [44:50]).
- **T9 quality.** The podcast transcript is low-grade local ASR with inferred attribution. L2.5 (why she moved away from solver development) and L7.8 rest on it alone and need a second source.

## Implications for Phase 2 (all [inferred], for the synthesiser)

- **Candidate core methods.** These are stated at least three times; test each against `03-process-evidence.md` for practice:
  - structure-first relaxation design (C1);
  - interpolating formulation families plus a robustness test for their parameters (C4 + C9);
  - the fair-comparison protocol (C6): baseline at its strongest, equal preprocessing, bad-variant controls, total time reported;
  - scope discipline (C11);
  - problem choice by assumption mismatch (C12);
  - open release of code, videos and slides (C7).
- **Candidate heuristics:**
  - calibrate instance difficulty so the baseline solves some instances;
  - fail fast in primal heuristics;
  - generate cheap cuts first;
  - prove what can be proved, then experiment and label the claim "experimental";
  - keep the people who carry out a plan in charge of it;
  - end talks with a challenge list.
- **Checks for 03 that bear on the contradictions:**
  - whether papers report set-up time (T3 [29:04]);
  - whether the parameter-robustness claims hold across papers;
  - whether GALINI reached users;
  - whether solver-component papers stop after about 2021;
  - how many proof-centred papers appear despite "boring".
- **Mentor voice for the skill.** Her spoken register is distinctive: self-deprecating, with weakness first, life analogies and open questions to the audience. A tutor-voice layer could imitate it, but only from T7, T8, T10 and T11 quotes.

## Sources

Primary, her own voice (single author or her own answers):
- W1. R. Misener, "Christodoulos Achilleus Floudas", *SIAG/OPT Views and News* 24(1):12–16, Oct 2016. https://siagoptimization.github.io/assets/views/ViewsAndNews-24-1.pdf — primary
- W2. R. Misener, "Deterministic Global Optimisation at CPSE: Models, Algorithms, and Software" (CPSE Industrial Consortium newsletter; PDF dated 7 June 2014). http://www.doc.ic.ac.uk/~rmisener/Misener_GO_at_CPSE_2014_06_07.pdf — primary
- W3. R. Misener (joint work with R. Baltean-Lugojan, F. Ceccon, M. Mistry), "Developing spatial branch & bound solvers", *Oberwolfach Reports* 16(2), Report 26/2019, pp. 1616–1618, DOI 10.4171/OWR/2019/26 — primary
- W4. L. Liberti, S. Sager, A. Wiegele (organisers), *Oberwolfach Reports* 12(4), Report 46/2015, open problem (13) [Misener], DOI 10.4171/OWR/2015/46 — primary (one attributed line)
- W5. R. Misener, "Machine learning for mathematical optimization and mathematical optimization for machine learning" (tutorial abstract), in E. Frejinger, A. Lodi, M. Lombardi, N. Yorke-Smith, "Data-Driven Combinatorial Optimisation (Dagstuhl Seminar 22431)", *Dagstuhl Reports* 12(10):166–174, 2023, DOI 10.4230/DagRep.12.10.166 — primary
- W6. R. Misener, abstract "Autonomous research machines: Self-optimizing new chemistry", Isaac Newton Institute DDEW03, 24 Apr 2023 (video description). https://www.youtube.com/watch?v=KX9Tzt_WLOM — primary (abstract only)
- W7. R. Misener, IP1 abstract "Optimizing over graphs: Challenges, Formulations, and Applications", SIAM Conference on Optimization (OP26), 2 Jun 2026. https://meetings.siam.org/sess/dsp_programsess.cfm?SESSIONCODE=88083 — primary
- W8. R. Misener, *Curriculum vitae*, updated 3 Dec 2025. http://www.doc.ic.ac.uk/~rmisener/Misener_CV.pdf — primary
- W9. R. Misener, homepage and subpages (home; Teaching; Research Team; Community Service; project pages), read 2026-10-10. http://wp.doc.ic.ac.uk/rmisener/ — primary
- W10. R. Misener, Imperial College profile ("About"), read 2026-10-10. https://profiles.imperial.ac.uk/r.misener — primary
- W11. UKRI Gateway to Research, EP/P016871/1 "GALINI: Global ALgorithms for mixed-Integer Nonlinear optimisation of Industrial systems" (abstract, planned impact, key findings), read 2026-10-10. https://gtr.ukri.org/projects?ref=EP%2FP016871%2F1 — primary (PI text)
- W12. R. Misener, "Department of Computing researchers selected to present research in Parliament", Imperial News, 21 Feb 2019. https://www.imperial.ac.uk/news/190330/department-computing-researchers-selected-present-research/ — primary
- W13. R. Misener, "Department of Computing MSc student honoured for her joint work with Royal Mail", Imperial News, 15 May 2019. https://www.imperial.ac.uk/news/191227/department-computing-msc-student-honoured-joint/ — primary
- W14. R. Baltean-Lugojan, F. Ceccon, J. Kronqvist, R. Misener, M. Mistry, slides "Developing spatial branch & bound solvers", dated 2021-06-23. https://www.doc.ic.ac.uk/~rmisener/MINLPSolver_Tutorial.pdf — primary
- T1. Imperial Business Partners, "Decision making under uncertainty: Panel debate and discussion" (Misener, Cardin, Díaz; chair P. Childs), early Mar 2021. https://www.youtube.com/watch?v=Cbnfz00SHLg ; transcript `references/sources/talks/2021-03-12-imperial-panel-decision-making-under-uncertainty-Cbnfz00SHLg.txt` — primary (ASR)
- T2. R. Misener, "Partition-based formulations for mixed-integer optimization of trained ReLU neural networks", *Machine Learning NeEDS Mathematical Optimization* seminar, Apr 2021. https://www.youtube.com/watch?v=UcNXm24uQjE ; `talks/2021-04-sevilla-partition-based-formulations-relu-UcNXm24uQjE.txt` — primary (ASR)
- T3. R. Misener, "Partial Lasserre relaxation for sparse Max-Cut", *Discrete Optimization Talks*, 30 Apr 2021. https://www.youtube.com/watch?v=e3CSpZ4uUT8 ; `talks/2021-04-30-discrete-opt-talks-partial-lasserre-maxcut-e3CSpZ4uUT8.txt` — primary (ASR)
- T4. R. Misener, "Developing spatial branch & bound solvers" (NMPC 2021 plenary recording), published 5 Aug 2021. https://www.youtube.com/watch?v=Z5hbKPx9YDE ; `talks/2021-08-05-nmpc2021-developing-spatial-branch-and-bound-solvers-Z5hbKPx9YDE.txt` — primary (ASR)
- T5. R. Misener, "Introduction to OMLT", 22 Mar 2022. https://www.youtube.com/watch?v=8IpM42mSsWE ; `talks/2022-03-22-introduction-to-omlt-8IpM42mSsWE.txt` — primary (ASR)
- T6. R. Misener, "Switching formulations in OMLT", 23 Mar 2022. https://www.youtube.com/watch?v=S4KySGdpt0g ; `talks/2022-03-23-switching-formulations-in-omlt-S4KySGdpt0g.txt` — primary (ASR)
- T7. R. Misener, "Between formulations or: How I Learned to Stop Worrying and Love Parameters", Cornell Learning Machines Seminar, 17 Feb 2023. https://www.youtube.com/watch?v=bC4PDG9EZA8 ; `talks/2023-02-17-cornell-between-formulations-love-parameters-bC4PDG9EZA8.txt` — primary (ASR)
- T8. R. Misener, inaugural lecture "Just relax, Or: How I'm bad at my own algorithmic advice.", Imperial College London, 13 Mar 2023. https://www.youtube.com/watch?v=dN860HNsAs0 ; `talks/2023-03-13-just-relax-inaugural-lecture-asr.md` — primary (ASR)
- T9. BCS, "The Needham Debate: Optimisation algorithms" (podcast, *The Gem of all Mechanisms*), released 26 Feb 2024. https://sphinx.acast.com/p/open/s/5e44115dc4ea04b939ea0700/e/65d71cb0dc02e00016bfd8d3/media.mp3 ; https://www.bcs.org/articles-opinion-and-research/the-needham-debate-optimisation-algorithms/ ; local ASR `talks/2024-02-26-bcs-needham-debate-podcast-local-asr.md` — primary (low-grade local ASR; attribution inferred)
- T10. R. Misener, "Bayesian optimization and design of experiments", SCI SciTalk, Mar 2024. https://www.youtube.com/watch?v=9aLOEJNOCho ; `talks/2024-scitalk-bayesian-optimization-design-of-experiments-9aLOEJNOCho.txt` — primary (ASR)
- T11. R. Misener, "Autonomous research machines: Self-optimising new chemistry", AI Fun with ELLIS seminar, University of Manchester, Jan 2025. https://www.youtube.com/watch?v=2br7KspcQXk ; `talks/2025-01-manchester-autonomous-research-machines-2br7KspcQXk.txt` — primary (ASR)

Primary, institutional or co-authored:
- Q8. Imperial College London, event page "Just relax, Or: How I'm bad at my own algorithmic advice" (abstract and biography), Mar 2023. https://www.imperial.ac.uk/events/158579/just-relax-or-how-im-bad-at-my-own-algorithmic-advice/ — primary (institutional)
- J1. D. Letsios, R. Baltean-Lugojan, F. Ceccon, M. Mistry, J. Wiebe, R. Misener, "Approximation algorithms for process systems engineering", *Comput. Chem. Eng.* 132:106599 (2020), DOI 10.1016/j.compchemeng.2019.106599; arXiv:1909.12328 — primary (joint)
- J2. A. Thebelt, J. Wiebe, J. Kronqvist, C. Tsay, R. Misener, "Maximizing information from chemical engineering data sets: Applications to machine learning", *Chem. Eng. Sci.* 252:117469 (2022), DOI 10.1016/j.ces.2022.117469; arXiv:2201.10035 — primary (joint)
- J3. R. Misener, L. T. Biegler, "Formulating data-driven surrogate models for process optimization", *Comput. Chem. Eng.* 179:108411 (2023), DOI 10.1016/j.compchemeng.2023.108411 — primary (joint; abstract only)
- J4. P. Bonami, A. M. Gleixner, J. Linderoth, R. Misener, "Designing and Implementing Algorithms for Mixed-Integer Nonlinear Optimization (Dagstuhl Seminar 18081)", *Dagstuhl Reports* 8(2):64–87 (2018), DOI 10.4230/DagRep.8.2.64 — primary (joint)

Secondary (reports that contain her quoted words, and observers):
- Q1. D. Silverman, "Decision-making under uncertainty", Imperial Stories (Imperial Enterprise), early 2021. https://www.imperial.ac.uk/stories/decision-making/ — secondary
- Q2. D. Silverman, "Worldwide uncertainty a chance to be more efficient and resilient, say academics", Imperial News, 12 Mar 2021. https://www.imperial.ac.uk/news/216673/worldwide-uncertainty-chance-more-efficient-resilient/ — secondary
- Q3. C. Brogan, "Imperial scoops three new Royal Academy of Engineering research chairs", Imperial News, 24 Mar 2022. https://www.imperial.ac.uk/news/235034/imperial-scoops-three-royal-academy-engineering/ — secondary
- Q4. D. Silverman, "Machine learning techniques from Imperial and BASF advance experimental design", Imperial News, 31 Oct 2022. https://www.imperial.ac.uk/news/241071/machine-learning-techniques-from-imperial-basf/ — secondary
- Q5. A. Idle, "Major contribution by Imperial undergraduate to open-source research software", Imperial News, 23 Nov 2022. https://www.imperial.ac.uk/news/241732/major-contribution-imperial-undergraduate-open-source-research/ — secondary
- Q6. BCS, "Professor Ruth Misener awarded the 2023 BCS Roger Needham Award", 11 Dec 2023. https://www.bcs.org/articles-opinion-and-research/professor-ruth-misener-awarded-the-2023-bcs-roger-needham-award/ ; same quote in Imperial News, 20 Dec 2023. https://www.imperial.ac.uk/news/250395/professor-ruth-misener-honoured-with-2023/ — secondary
- Q7. D. Silverman, "Machine learning models to support chemical R&D recognised with Best Paper Award", Imperial News, 27 Aug 2024. https://www.imperial.ac.uk/news/255753/machine-learning-models-support-chemical-rd/ — secondary
- O1. E. N. Pistikopoulos, vote of thanks, within T8 [47:04]–[52:44], 13 Mar 2023 — secondary (observer)
- O2. Royal Academy of Engineering text on the 2017 Young Engineer of the Year awards, as reprinted in "Five star young engineers win Academy Awards", Zenoot. https://zenoot.com/five-star-young-engineers-win-academy-awards — secondary (observer)

Works named above (identifiers checked in this run with Crossref, DataCite, the arXiv API or OpenAlex):
- Solvers named in W1 (written with C. A. Floudas): R. Misener, C. A. Floudas, "GloMIQO: Global mixed-integer quadratic optimizer", *J. Glob. Optim.* 57(1):3–50 (2013), DOI 10.1007/s10898-012-9874-7; R. Misener, C. A. Floudas, "ANTIGONE: Algorithms for coNTinuous / Integer Global Optimization of Nonlinear Equations", *J. Glob. Optim.* 59(2–3):503–526 (2014), DOI 10.1007/s10898-014-0166-2
- K. M. Anstreicher, "Semidefinite programming versus the reformulation-linearization technique for nonconvex quadratically constrained quadratic programming", *J. Glob. Optim.* 43:471–484 (2009), DOI 10.1007/s10898-008-9372-0
- A. Bompadre, A. Mitsos, "Convergence rate of McCormick relaxations", *J. Glob. Optim.* 52(1):1–28 (2012), DOI 10.1007/s10898-011-9685-2
- M. Fischetti, A. Lodi, "Heuristics in Mixed Integer Programming", *Wiley Encyclopedia of Operations Research and Management Science*, DOI 10.1002/9780470400531.eorms0376
- T. Berthold, *Heuristic algorithms in global MINLP solvers*, doctoral dissertation, TU Berlin, 2014 (OpenAlex record; no DOI)
- M. Mistry, R. Misener, "Optimising heat exchanger network synthesis using convexity properties of the logarithmic mean temperature difference", *Comput. Chem. Eng.* 94:1–17 (2016), DOI 10.1016/j.compchemeng.2016.07.001
- F. Ceccon, J. D. Siirola, R. Misener, "SUSPECT: MINLP special structure detector for Pyomo", *Optim. Lett.* 14(4):801–814 (2020), DOI 10.1007/s11590-019-01396-y
- R. Baltean-Lugojan, R. Misener, "Piecewise parametric structure in the pooling problem: from sparse strongly-polynomial solutions to NP-hardness", *J. Glob. Optim.* 71(4):655–690 (2018), DOI 10.1007/s10898-017-0577-y
- J. S. Campos, R. Misener, P. Parpas, "Partial Lasserre relaxation for sparse Max-Cut", *Optim. Eng.* 24 (2023), DOI 10.1007/s11081-022-09763-y
- C. Tsay, J. Kronqvist, A. Thebelt, R. Misener, "Partition-based formulations for mixed-integer optimization of trained ReLU neural networks", arXiv:2102.04373 (NeurIPS 2021)
- J. Kronqvist, R. Misener, C. Tsay, "Between steps: Intermediate relaxations between big-M and convex hull formulations", arXiv:2101.12708 (CPAIOR 2021)
- J. Kronqvist, R. Misener, C. Tsay, "P-split formulations: A class of intermediate formulations between big-M and convex hull for disjunctive constraints", arXiv:2202.05198
- J. P. Folch, R. M. Lee, B. Shafei, D. Walz, C. Tsay, M. van der Wilk, R. Misener, "Combining multi-fidelity modelling and asynchronous batch Bayesian Optimization", *Comput. Chem. Eng.* 172:108194 (2023), DOI 10.1016/j.compchemeng.2023.108194
- J. P. Folch, S. Zhang, R. M. Lee, B. Shafei, D. Walz, C. Tsay, M. van der Wilk, R. Misener, "SnAKe: Bayesian Optimization with Pathwise Exploration", arXiv:2202.00060 (NeurIPS 2022)
- J. P. Dürholt et al. (incl. R. Misener), "BoFire: Bayesian Optimization Framework Intended for Real Experiments", arXiv:2408.05040
- F. Ceccon, J. Jalving, J. Haddad, A. Thebelt, C. Tsay, C. D. Laird, R. Misener, "OMLT: Optimization & Machine Learning Toolkit", *J. Mach. Learn. Res.* 23 (2022), arXiv:2202.02414

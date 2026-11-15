# Marco E. Lübbecke: research trajectory (research agent 06)

- **Researcher**: Marco E. Lübbecke. The name also appears as "Marco Lübbecke", "Marco Luebbecke" and "M. E. Lübbecke". He has no middle name: the book's author note says he picked the initial "E." when the copyright form of his first paper asked for one (P7, p. vi).
  - Current posts: professor and head of the Chair of Operations Research, RWTH Aachen University, since 1 October 2010; GERAD associate member since December 2018.
  - Identifiers: DBLP 24/5951; ORCID 0000-0002-2635-0522; OpenAlex A5082694588, plus a two-work split record A5129110788; MGP 74622.
  - **Not this person**: Elisabeth Lübbecke, his co-author on the Kiel Canal paper, is a separate researcher (MGP 200586, TU Berlin 2015); arXiv 1504.07129 is hers. Also excluded: the oceanographer Joke F. Lübbecke and the other Lübbeckes in DNB and OpenAlex.
- **Dimension**: research trajectory (framework §二, agent 6). Covered here: the dated timeline, lineage, turns and their triggers, entry and exit relative to the consensus, era and resource context, failures and abandoned lines, role labels, and the last 12 months. It serves framework layers 2 (problem choice, timing) and 7 (organisation), with pointers for layers 1, 4 and 5.
- **Lens (team.json)**: decomposition inside MILP solver engineering (Dantzig-Wolfe reformulation, column generation, branch-and-price) and the GCG solver.
- **Research date**: 2026-11-08.
- **Sources consulted**: 36 with content: 19 primary (P1–P19) and 17 secondary (S1–S17), listed under "Sources". There were also 14 negative or unreachable checks, listed below.
  - **WebSearch calls used: 5 of 5.**
  - Everything else came from curl and WebFetch, and from public APIs: ORCID, OpenAlex, Crossref, DataCite, arXiv, the DNB SRU catalogue, the MGP quick search and the Bluesky public AppView.
  - DBLP records came from a scratch copy of `scripts/dblp_works.py`. I patched the copy, not the repository script: an upper-case "ARXIV" DOI crashed it.
  - GCG history came from a blob-less bare clone of github.com/scipopt/gcg: metadata only, nothing executed.
- **Local corpus**: `references/sources/{papers,essays,software,publications}` held only `.gitkeep`. **Nothing below is from user-supplied material.** `private/` was not opened. A recursive directory listing at the start of the run showed that it holds a README.md, but its content was not read.
- **Transcripts in `talks/`**: four caption files were saved during this run by research agent 02. None is mine and none is user-supplied:
  - the *Subject to* podcast (2021-09-23; automatic captions);
  - the TEDxRWTHAachen talk (automatic captions);
  - the RWTH Lehrpreis 2022 video (captions);
  - excerpts from his CO@Work 2020 lecture (captions; three excerpts only).

  I checked each video's identity and upload date myself through YouTube oEmbed and the watch-page metadata (P4–P6, P19). None of the files was checked against the audio. I paraphrase them with timestamps and quote none of them. I saved no transcript myself.
- **Sibling notes**: none of notes 01–05 existed while this note was drafted. `03-process-evidence.md` appeared at the end, and I skimmed it only for overlaps.
  - It agrees on the GCG history: first commit by Gamrath on 2008-11-25, last push 2026-10-30.
  - It adds that commit e21f41cc cut the list of papers using GCG from 51 to 43 entries. I did not verify that number.
  - It mentions theses by the GCG developers. That mention does not settle the doctoral-outcome gap below, and I did not use it.
- **Quotation policy**: findings are paraphrased with pinpoint locations. Verbatim quotes come only from the two CC BY 4.0 sources, the book (P7) and the 2020 editorial (P8), plus one sentence from his blog (P3).
  - P7 page numbers are those of the GERAD cahier PDF dated 6 January 2026: the printed page, with the PDF page added where they differ. The Springer edition's pagination was not checked.
- **Privacy filter**: the public author note and the podcast contain family, health and hometown details, and the Bluesky feed contains political and civic posts. None of this is recorded here. Only academic and research-craft facts are.

### How the evidence was gathered (and what failed)

- **Read in full**:
  - P2;
  - P3 (all nine posts);
  - P4 (whole transcript);
  - P5 and P6;
  - P7: front matter pp. i–xv, p. 538, pp. 546–553, and the reference list (searched);
  - P8;
  - P9: all 161 own posts and replies from 2025-09-04 to 2026-11-07, with reposts ignored except one noted in §8;
  - P10: commit metadata, tags, CHANGELOG headings and README;
  - P11 and P12;
  - P19 (the saved excerpts; the rest of the lecture not read);
  - S4, S5 (title and team slides), S6, S12 and S13.
- **Read as abstract, metadata or byline only**: P13–P18, and every DOI cited, through Crossref, OpenAlex, DataCite and DBLP; also S7–S11 and S14–S17.
- **Not reached** (not routed around):
  - The RWTH OR chair site and the GCG site (or.rwth-aachen.de, gcg.or.rwth-aachen.de) timed out for curl and WebFetch on 2026-11-08. team.json records the same on 2026-11-05.
  - publications.rwth-aachen.de served a JavaScript challenge, which I did not bypass.
  - Live dblp.org pages sat behind an Anubis wall for both curl and WebFetch, so I used the SPARQL endpoint instead (S8).
  - The Springer book page redirected to a login, so I used Crossref (S10) and a bookseller record (S11) instead.
- **Negative checks**:
  - the old TU Berlin COGA people and publication pages (no Lübbecke entry);
  - an ELLIIT page from a search hit (an image file and a 404);
  - Semantic Scholar (no abstracts);
  - the ALMOA consortium page and a TU/e vacancy that he shared (neither names him);
  - GOR/LNMB, SDU, TU Ilmenau, HUGO and ORBEL news pages (search false positives);
  - an OpenAlex dissertation search for the GCG developers (nothing found).
- **WebSearch summaries** were used as leads only. One of them attributed an IVADO Labs advisory role to Lübbecke; the bookseller's author bios (S11) give that role to Guy Desaulniers. It is not used.

### Tag legend

- **[stated]**: his own words in a sole-voice text (P2, P3, P9), his own talk abstracts (P11, P12), his speech in the videos (P4–P6, P19), and the employment entries he asserted himself on ORCID (P1).
- **[stated-joint]**: co-signed text whose voice cannot be split. This covers the book (P7), including its third-person author notes, the 2020 editorial (P8), and paper abstracts (P13–P17).
- **[practice]**: what the record shows was done: papers and bylines, commits and releases, theses supervised, events organised.
- **[observed]**: what others recorded: Soumis's Foreword, the podcast host, institutional pages, conference bios whose author is not identified, library and genealogy databases.
- **[inferred]**: my synthesis, to be treated as a hypothesis.
- **P / S**: primary / secondary source.

---

## 0. The trajectory in one paragraph (all [inferred], built from the sections below)

**How he got in.** Lübbecke came to optimization sideways. He was refused a place in informatics, enrolled in mathematics instead, and took a student job in Uwe Zimmermann's optimization department. His PhD topic came from a grant he was hired to write: locomotive scheduling on industrial in-plant railroads, solved by column generation on CPLEX 3.0.

**What the thesis set up.** Two things from that thesis organised the next 25 years:
- the questions it left open, tailing-off and instability, which became the 2005 survey with Jacques Desrosiers;
- Desrosiers himself, whom Lübbecke chose as external committee member.

**Near-exits.** A run of near-exits shaped the path more than any plan did:
- every application to North America was rejected (2001–03);
- a fixed-term Berlin contract nearly ended his career (2009);
- a visiting post in Darmstadt filled the gap;
- the Aachen chair came only after five other candidates had declined it (2010).

**The long project.** The Berlin years gave him SCIP, and SCIP gave him the long project: GCG, a generic branch-price-and-cut solver whose code starts in November 2008. Around it grew the research programme of detecting model structure (2010–15), which in 2021 he named as possibly his favourite line of work.

**Side lines.** These came through collaborators and students:
- LP degeneracy with Gauthier and Desrosiers (2011–18);
- machine learning for choosing a decomposition (2017–22);
- districting, energy and engineering applications (2016–19);
- editorial and community work: the INFORMS board around 2017, Operations Research Forum in 2020, and column-generation schools since 2006.

**From 2019.** His journal output thins while his effort goes into the book (2015–2026), GCG documentation (his own commits run 2018–21), teaching (an award in 2022) and the SCIP suite.

**2026.** He comes back with:
- the open-access book;
- GCG 4.x;
- two branch-and-price preprints;
- a theme he has stated since 2014, that algorithms should see a model's structure and meaning rather than the flat matrix.

## 1. Dated timeline

| Date | Event | Tag | Source |
|---|---|---|---|
| 1971 | Born. | [stated-joint] | P7 p. vi |
| c. 1992–1996 | Studies mathematics at TU Braunschweig after not being admitted to his first choice, a then-new informatics programme (apparently business informatics; the captions are garbled). He accepted mathematics before a waiting-list place in the first choice came through, and stayed. He was the first in his family to reach the university-track school and university. Four-year Diplom; thesis on enumerating the vertices and facets of polytopes. Start year inferred from a four-year Diplom ending in 1996. | [stated] / [stated-joint] | P4 0:12:48–0:18:36; P7 p. vi |
| c. 1994 | Student assistant in the Department of Mathematical Optimization (Zimmermann). Builds the department's first web pages. His first contact with OR is the introductory optimization course. | [stated] | P4 0:20:25–0:23:54 |
| 1996 | After his last Diplom exam he is given a seven-month contract to write the full second-stage proposal for a project on scheduling locomotives at in-plant railroads (chemical and steel plants). The proposal succeeded and funded three more years, which became his PhD. He says he never planned a PhD. ORCID: research assistant, TU Braunschweig, 1 Sep 1996 to 31 Aug 2003. A related record: a 2004 final report to the BMBF programme "Neue mathematische Verfahren in Industrie und Dienstleistungen", titled "Optimales Wagenmanagement bei Werks- und Industriebahnen", lists Lübbecke and Zimmermann as contributors (DOI 10.2314/gbv:471272760). Whether this is the grant he wrote in 1996 or a follow-up (compare the 2005 rail-car allocation paper, DOI 10.1007/s10589-005-3229-y) is not established. | [stated] / [practice] | P4 0:24:42–0:27:25; P1; S17 |
| 1996 | First conference presentation, with Tamás Terlaky as session chair (2026 post). | [stated] | P9 2026-07-15 |
| 1997 | ISMP 1997, Lausanne: in the 2021 interview, the first conference he counts as a real one. | [stated] | P4 0:32:22 |
| 1998 | First journal paper, from the Diplom work: Bussieck & Lübbecke, "The vertex set of a 0/1-polytope is strongly P-enumerable", *Comput. Geom.* 11 (1998), DOI 10.1016/S0925-7721(98)00021-2. It was first desk-rejected by a more prestigious journal. Also: Bernatzki, Bussieck, Lindner & Lübbecke, "Optimal scrap combination for steel production", *OR Spektrum* 20(4):251–258 (1998), DOI 10.1007/BF01539743. | [stated] / [practice] | P4 0:30:20–0:32:22; S8; S10 |
| 17 Jan 2001 | Desrosiers writes to Lübbecke that he is still interested in "the book" on column generation. | [stated-joint] | P7 p. xiii |
| 2001 (c. late Oct) | PhD, TU Braunschweig, "Engine Scheduling by Column Generation", advisor Uwe T. Zimmermann. Published by Cuvillier (Göttingen) and online (urn:nbn:de:gbv:084-115827). Desrosiers sat on the committee. The month is inferred from a post on 2026-10-27 marking his 25th PhD anniversary. | [practice] / [stated] | S6; S7; P2; P4 0:39:15; P9 2026-10-27 |
| 2001–2003 | Applies for assistant-professor posts in the US and Canada; receives only rejections. Stays at Braunschweig. | [stated] / [stated-joint] | P4 0:43:22–0:44:29; P7 p. vi; P1 |
| May 2003 | Lübbecke & Zimmermann, "Engine routing and scheduling at industrial in-plant railroads", *Transportation Science* 37(2):183–197, DOI 10.1287/trsc.37.2.183.15251. At the partner, planning was done by pencil and paper. The paper gives a set-partitioning model solved by column generation, with a new exact label-correcting pricing algorithm. | [stated-joint] | P13 |
| 1 Sep 2003 | Assistant professor in the Combinatorial Optimization and Graph Algorithms group (Rolf Möhring), TU Berlin. Fixed-term, to 30 Sep 2009. | [stated] | P1; P4 0:45:26–0:46:25 |
| Oct 2003 | Fekete, Lübbecke & Meijer, stabbing number of matchings, trees and triangulations: arXiv cs/0310034, then SODA 2004, then *DCG* 40 (2008), DOI 10.1007/s00454-008-9114-6. | [practice] | S16; S8 |
| Mar 2004 – Dec 2005 | Lübbecke & Desrosiers, "Selected topics in column generation". Cahier G-2002-64 posted Mar 2004; *Operations Research* 53(6):1007–1023 (2005), DOI 10.1287/opre.1050.0234; 1,130 citations in OpenAlex. He says it grew out of the thesis's open questions. Same period: Desrosiers & Lübbecke, "A primer in column generation", in *Column Generation* (2005), pp. 1–32, DOI 10.1007/0-387-25486-2_1; and his sole-author "Dual variable based fathoming in dynamic programs for column generation", *EJOR* 162 (2005), DOI 10.1016/j.ejor.2003.05.006. | [practice] / [stated] | S2; P14; S9; S10; P4 0:38:23–0:38:53 |
| 2006 | First School on Column Generation (Montréal), organised and taught with Guy Desaulniers and Desrosiers. | [observed] | S4 (P7 p. xii) |
| 2007 | Habilitation, TU Berlin, with Rolf Möhring. Title not found. | [stated] | P2; P7 p. vi |
| 2007–2011 | Application-driven algorithm engineering with Möhring's group and others: <br>• PSPACE-complete stacking, ESA 2007, DOI 10.1007/978-3-540-75520-3_64; <br>• Swiss Federal Railways Cargo Express, *TS* 42 (2008), DOI 10.1287/trsc.1080.0246; <br>• recoverable robustness, LNCS (2009), DOI 10.1007/978-3-642-05465-5_1; <br>• coil coating, *Management Science* 57 (2011), DOI 10.1287/mnsc.1100.1302. | [practice] | S8; S10 |
| 2008 | International Workshop on Column Generation, Aussois. | [observed] | S4; P7 p. 547 |
| 25 Nov 2008 | First GCG commit, subject line "GCG start", by Gerald Gamrath (commit 61d4b710; history converted from CVS). A 2014 slide dates GCG's start to 2008 and Gamrath's Diploma thesis, and lists Lübbecke as the project's initiator and head. | [practice] / [observed] | P10; S5 |
| 2009 | Joins Twitter (@mluebbecke). | [stated] | P4 0:58:56–0:59:32 |
| 17 Jun 2009 | GCG v0.1 tagged. | [practice] | P10 |
| Aug 2009 | ISMP 2009 (Chicago), weeks before his contract ends, with no plan B. A tip from Rüdiger Schultz in a conference elevator leads to a two-year offer from Alexander Martin in Darmstadt. | [stated] | P4 0:45:44–0:47:31 |
| 1 Oct 2009 – 30 Sep 2010 | Visiting professor of discrete optimization, TU Darmstadt, commuting from Berlin. The 2010 Column Generation School is held in Darmstadt. | [stated] / [observed] | P1; P2; P4 0:47:31; S4 |
| May 2010 | Gamrath & Lübbecke, "Experiments with a generic Dantzig-Wolfe decomposition for integer programs", SEA 2010, LNCS 6049:239–252, DOI 10.1007/978-3-642-13193-6_21. | [practice] | S8; P7 refs |
| 1 Oct 2010 | Full professor and chair of OR, RWTH Aachen; ORCID gives the School of Business and the Department of Mathematics. His first and only permanent position, at 39. The offer came after two short lists, five people in all, had declined. | [stated] / [stated-joint] | P1; P4 0:47:31–0:49:28; P7 p. vi |
| 2011 | Bergner, Caprara, Furini, Lübbecke, Malaguti & Traversi, "Partial convexification of general MIPs by Dantzig-Wolfe reformulation", IPCO 2011, DOI 10.1007/978-3-642-20807-2_4. Also Desrosiers & Lübbecke, "Branch-price-and-cut algorithms", *Wiley Encyclopedia of Operations Research and Management Science* (2011), DOI 10.1002/9780470400531.eorms0118. | [practice] | S8; S10 |
| Nov 2011 | Cahier G-2011-66 with Desrosiers and Gauthier, "Improved column generation for highly degenerate master problems", opens the degeneracy line. | [practice] | S2 |
| 2012 | Sole-author SEA 2012 paper, "Automatic decomposition and branch-and-price—a status report", DOI 10.1007/978-3-642-30850-5_1. GCG 1.0 tagged 2012-08-01. Column-generation workshop in Bromont. Hennig, Nygreen & Lübbecke, "Nested column generation applied to the crude oil tanker routing and scheduling problem with split pickup and split delivery", *NRL* 59:298–310, DOI 10.1002/nav.21489. | [practice] | S8; P10; S4; S10 |
| 2013 | Lübbecke & Puchert, "Large neighborhood search and diving heuristics based on Dantzig-Wolfe reformulation": cited in the 2026 book as an "Unpublished manuscript, 2013". | [practice] | P7 references |
| 2014 | <br>• GCG 2.0 tagged 27 Feb. <br>• First-listed editor of *Operations Research Proceedings 2014*, from the GOR conference held at RWTH on 2–5 Sep 2014 (Springer 2016, DOI 10.1007/978-3-319-28697-6). <br>• Co-editor of *Zukunftsperspektiven des Operations Research* (Springer Gabler, 2014). <br>• Column Generation School in Paris. <br>• GCG talk by Jonas Witt at the SCIP Workshop, Berlin, 1 Oct. <br>• Blog *café opt* starts 15 Oct. | [practice] | P10; S10; S7; S4; S5; P3 |
| 4 Nov 2014 | A blog post on faculty-job interviews, where committees asked him what the next big thing would be, names his central research question: "Most research topics in my head deal with finding and exploiting structures in mathematical programs." | [stated] | P3 |
| 14–26 Jan 2015 | The book project starts. On 14 Jan 2015 the user "luebbecke" makes the first commit in a Subversion repository, expecting to finish in 2015–2017. On 26 Jan Desrosiers has a detailed 16-chapter outline titled "branch-and-price". | [stated-joint] | P7 p. xiii |
| Feb 2015 | Bergner et al., "Automatic Dantzig–Wolfe reformulation of mixed integer programs", *Mathematical Programming* 149:391–424, DOI 10.1007/s10107-014-0761-5. | [practice] | S8; P7 refs |
| 2 Mar 2016 | Ninth and last blog post. In 2021 he says he stopped blogging. | [practice] / [stated] | P3; P4 1:01:39 |
| 2016 | Column-generation workshop in Búzios. Goderbauer, Bahl, Voll, Lübbecke, Bardow & Koster, "An adaptive discretization MINLP algorithm for optimal synthesis of decentralized energy supply systems", *Comput. Chem. Eng.* 95, DOI 10.1016/j.compchemeng.2016.09.008. | [observed] / [practice] | S4; S8 |
| Jun 2017 | Kruber, Lübbecke & Parmentier, "Learning when to use a decomposition", CPAIOR 2017, LNCS 10335, DOI 10.1007/978-3-319-59776-8_16. | [practice] | S8; P7 refs |
| 2017 | Keynote "Branch-and-Price" at ORBEL 31 (KU Leuven). The bio names him as the current INFORMS Vice President for Information Technology. Robotics reconfiguration planning appears in *IEEE RA-L* 2 (2017), DOI 10.1109/LRA.2017.2705286. | [stated] / [observed] / [practice] | P11; S8 |
| 9 Jun 2018 (recorded) / 27 Feb 2019 (published) | TEDxRWTHAachen talk, "Anything you can do I can do better". | [stated] | P5 |
| 11 Jun 2018 – 28 Oct 2021 | His own GCG commits: 92 in all, 49 of them non-merge, 69 in 2019 alone. | [practice] | P10 |
| 2 Jul 2018 | GCG 3.0 tagged. Column Generation School in Paris. | [practice] / [observed] | P10; S4 |
| Dec 2018 | Becomes a GERAD associate member. | [observed] | S1 |
| 2019 | <br>• Kiel Canal paper, *OR* 67(3):791–812, DOI 10.1287/opre.2018.1814. <br>• Goderbauer & Lübbecke, "Reform der Bundestagswahlkreise: Unterstützung durch mathematische Optimierung", *Zeitschrift für Parlamentsfragen* (2019), DOI 10.5771/0340-1758-2019-1-3. <br>• Goderbauer and Witt finish their PhDs; Witt's thesis is dated November 2019, DOI 10.18154/RWTH-2020-00547. | [practice] | S2; S9; S7; P7 refs |
| 5 Feb 2020 | "Welcome to SN Operations Research Forum!", with Panos Pardalos, the launch editorial of a new journal. DOI 10.1007/s43069-020-0001-1. | [stated-joint] | P8 |
| 23 Sep 2020 | Gives the decomposition-day lecture at CO@Work 2020 (video, 1 h 38 min). He presents GCG to the students as a way to judge whether a full branch-and-price implementation would pay off for their problem. | [stated] | P19 1:35:50–1:36:16 |
| 2021 | <br>• MIPLIB 2017, *MPC* 13, DOI 10.1007/s12532-020-00194-3. <br>• Lübbecke, Maher & Witt, "Avoiding redundant columns by adding classical Benders cuts to column generation subproblems", *Discrete Optimization* 39, DOI 10.1016/j.disopt.2021.100626. <br>• *Subject to* interview, 23 Sep. <br>• SCIP Optimization Suite 8.0 report, arXiv 2112.08872, Dec. | [practice] / [stated] | S8; P4; S16 |
| 2022 | GCG 3.5 tagged 31 Jan. Steever, Murray, Yuan, Karwan & Lübbecke, "An image-based approach to detecting structural similarity among mixed integer programs", *IJOC* 34, DOI 10.1287/ijoc.2021.1117. This is the last machine-learning paper found. | [practice] | P10; P15 |
| 8 Mar 2023 | RWTH publishes a video of its 2022 Teaching Award to him; he accepts it on behalf of his whole team. GERAD reports the award on 17 May 2023. | [stated] / [observed] | P6; S1 |
| 16–19 May 2023 | Column Generation 2023 workshop, Montréal. | [observed] | S1; P7 p. 547 |
| 28 Jun 2023 | The GCG repository opens on GitHub (scipopt/gcg, Apache-2.0), moved from git.or.rwth-aachen.de. | [practice] | P10 |
| 2023 | Bestuzheva et al., "Enabling research through the SCIP Optimization Suite 8.0", *ACM TOMS* 49, DOI 10.1145/3585516. | [practice] | S8 |
| 6 Feb 2024 | Creates a Bluesky account. | [practice] | P9 |
| Jun 2024 | *Branch-and-Price* appears as GERAD Cahier G-2024-36. | [practice] | S2; S3 |
| 26 Feb / 12 Nov 2024 | GCG 3.6 and 3.7 tagged. | [practice] | P10 |
| 19–23 May 2025 | School on Column Generation, CNAM, Paris. | [observed] | S1; P7 p. 547 |
| 1 Jul 2025 | Talk at the Paderborn PRIME colloquium, "(Who wants) Political Re-Districting in Germany (?)". | [stated] | P12 |
| Sep 2025 | Attends OR 2025, the GOR annual conference. | [stated] | P9 2025-09-04 |
| 2025-11-08 onward | See §8. | | |

## 2. Lineage

**Academic ancestry** [observed; S6]. Lübbecke's advisor was Uwe T. Zimmermann: PhD Köln 1976, dissertation on Boolean optimization problems with separable objective and matroidal constraints. Zimmermann's own advisor was Rainer E. Burkard.

Three of Zimmermann's other students were early co-authors of Lübbecke's:
- Michael Bussieck (PhD 1998), co-author in 1998 and 2004;
- Thomas Lindner (PhD 2002), co-author in 1998 and 2004;
- Stefan Krause (PhD 2006), co-author on k-modal partitions (LATIN 2006; *JDA* 6 (2008), DOI 10.1016/j.jda.2008.01.002).

Sources: S6, S8.

**Mentors and influences he names** [stated unless marked]:
- **Uwe Zimmermann** is his Doktorvater (doctoral advisor). He gave Lübbecke the job and the grant that became the PhD, and the department's CPLEX came through Zimmermann's close links to Bob Bixby (P4 0:35:15–0:35:31).
- **Jacques Desrosiers**: Lübbecke met him at a workshop and asked him onto the thesis committee. He calls Desrosiers his *père*, his academic father figure, and one of his closest friends (P4 0:39:15–0:40:33; P2). The external-review link is the origin story in his GERAD bio: among Montréal's many column-generation experts he wanted Desrosiers specifically (P2).
- **Rolf Möhring**: host of his habilitation in Berlin, whom he counts as a further major influence (P2; P4 0:44:13–0:44:29).
- **Sándor Fekete** taught him to know when to stop; **Martin Skutella** told him to read, read, read (P3, 2014-11-21).
- **Alexander Martin** gave him the Darmstadt post, and **Rüdiger Schultz** gave the tip that led to it (P4 0:46:25–0:46:42).
- **SCIP's developer in Berlin** worked closely with his group. The name is garbled in the captions and is plausibly Tobias Achterberg [inferred] (P4 0:50:19–0:50:35).

**Doctoral students and theses**, by source. The sources disagree on roles (see Contradictions).
- **MGP** lists 5 [observed; S6]:
  - Jens Schulz, TU Berlin 2012 (Lübbecke as advisor 2);
  - Torsten Gellert, TU Berlin 2015 (advisor 2);
  - Jens Leoff, TU Kaiserslautern 2016 (advisor 2);
  - Sebastian Goderbauer, RWTH 2019 (advisor 1);
  - Pascal Wortel, TU Kaiserslautern 2019 (advisor 2).
- **DNB and DataCite**, theses at RWTH with Lübbecke as first-listed supervisor, with DataCite "available" dates [observed; S7, S17]:
  - Goderbauer, energy systems and political districting, 2019-08-28, DOI 10.18154/rwth-2019-11954;
  - Jonas T. Witt, polyhedral aspects of Dantzig-Wolfe reformulation, 2019-11-29, DOI 10.18154/RWTH-2020-00547 (co-supervisors Koster and Desaulniers);
  - Sarah K. Roth, appointment scheduling, 2020-05-06, DOI 10.18154/rwth-2021-01724;
  - Annika Thome, graph-theoretical modelling aspects of practical problems, 2021-06-10, DOI 10.18154/rwth-2021-09087;
  - Christian S. Franzen, routing and scheduling in finished-vehicle logistics, 2022-04-28, DOI 10.18154/rwth-2022-04801.
- **DNB and DataCite**, theses with Lübbecke as second or third supervisor [S7, S17]:
  - Asif Khan 2016, open-pit mine scheduling (first supervisor Niemann-Delius);
  - Astrid Dettenbach 2016, hub location (Sebastian);
  - Florian Dahms, matchability decomposition, 2016-11-25 (Koster, Krumke), DOI 10.18154/rwth-2017-08718;
  - Andreas Braun, parcel pickup networks, 2017-12-15 (Sebastian), DOI 10.18154/rwth-2018-00067;
  - Christian Wassermann, data-flow optimization for parallel patterns on hierarchical memory, a computer-science thesis, 2023-03-15 (first supervisor Matthias S. Müller), DOI 10.18154/rwth-2023-06006.
- **External referee or examiner** [S7, S17]:
  - Jens H. Maue 2011 (ETH Zürich, sorting railway freight cars; DataCite lists Lübbecke as contributor "Other"), DOI 10.3929/ethz-a-006697371;
  - Marc Goerigk 2013 (Göttingen);
  - Frank Fischer 2013 (Chemnitz);
  - Wiebke Höhn 2014 (TU Berlin);
  - Robert Voll 2014 (Dortmund);
  - Gellert 2015 (TU Berlin).

  All of these except Maue are DNB *Gutachter* (referee) records.
- **The GCG developers.** Martin Bergner, Christian Puchert, Michael Bastubbe, Markus Kruber and Erik Mühmer are his long-time co-authors and GCG developers. Their doctoral records were **not found** in MGP, DNB, OpenAlex or DataCite (see Gaps).
- **2026**: Alex Helber, a co-author of a 2023 biobank-scheduling paper (S9), won the MIP 2026 poster competition with work on dynamic discretization discovery [stated; P9 2026-10-21].

**GCG developer cohorts**, as a proxy for team size [practice; P10, commit authors, all branches]:

| Period | Commits | Main committers |
|---|---|---|
| 2008–2011 | 406 | Gamrath 212, Bergner 111, Puchert 59 |
| 2012–2015 | 2,130 | Bergner 1,005, Puchert 460, Witt 257, Gamrath 182, Schmickerath 106 |
| 2016–2019 | 3,305 | Bastubbe 714, Puchert 529, Hanna Franzen 510, Witt 374, Walter 126 |
| 2020–2022 | 687 | Mühmer 243, Donkiewicz 204 (plus 62 as "donkiewicz"), Gaul 85, Lübbecke 19 |
| 2023–2024 | 714 | Mühmer 398, Reinartz Groba 156, Mohr 136 |
| 2025–2026 | 341 (to 30 Oct 2026) | Mühmer 256, Ehls 50, Reinartz Groba 13, Vigerske 12 |

The book credits Gamrath with the original "two communicating trees" design, which is still intact, and names Bergner, Bastubbe, Puchert, Witt, Steve Maher and Mühmer as major contributors. It then says: "Marco is the one with the vision who keeps it all together." [stated-joint, third person; P7 p. 538 (PDF 569)]

**Teaching lineage** [observed; S4, P7 p. 547]. With Desaulniers and Desrosiers he has run the five-day Schools on Column Generation in Montréal 2006, Darmstadt 2010, Paris 2014, 2018 and 2025, with up to 95 students each. The three were also involved in the workshops in Aussois 2008, Bromont 2012, Búzios 2016 and Montréal 2023.

## 3. Turns and what triggered them

### T1. Informatics, then mathematics, then discrete optimization (c. 1992–1996)
- **Trigger**: a rejection, then a brochure. He was refused for informatics, enrolled in mathematics, and stayed in it even when a waiting-list place came through (P4 0:15:13–0:16:54; P7 p. vi) [stated / stated-joint].
- **Why discrete**: topology, higher algebra and measure theory were not his; graph-theoretic proofs were accessible. He liked that in mathematics and programming you know when you are wrong (P4 0:08:14–0:08:45, 0:23:37–0:24:25) [stated].
- **First contact with OR**: an introductory optimization course and the student job in Zimmermann's department (P4 0:20:25–0:23:54) [stated].

### T2. From student job to a PhD via a grant (1996)
- **Trigger**: the department offered him a seven-month contract to turn a one-page, first-stage grant on in-plant railroads into a full proposal. Its success paid for the PhD (P4 0:25:04–0:27:25) [stated].
- **Tooling of the time**:
  - CPLEX 3.0 through the C interface, building the model column by column;
  - column generation only, with no branching, because he would have had to write his own tree management and was wary of it (P4 0:35:15–0:37:15) [stated];
  - "Marco's initiation in solvers was with CPLEX 3.0" (P7 p. vi) [stated-joint];
  - literature came by photocopy and inter-library loan (P4 0:27:42–0:28:42) [stated].

### T3. Thesis questions become a survey and a Montréal network (1999–2005)
- **Trigger**: he could see tailing-off and instability in his runs but could not fix them. He set out to collect every explanation he could find, and that collection became the 2005 survey with Desrosiers (P4 0:37:32–0:38:53) [stated].
- He did stabilization experiments only after the PhD. The captions garble the name of a 1999 stabilization paper [inferred: possibly du Merle et al.; not checked].
- The survey's abstract centres on the dual point of view (P14) [stated-joint].

### T4. North-American rejections, then Berlin (2001–2003)
- **Trigger**: failure. With hindsight he had no credentials: almost no publications from the PhD. So rather than crossing the Atlantic he moved about 200 km east, to Möhring's group in Berlin (P4 0:43:22–0:44:29; P7 p. vi) [stated / stated-joint].
- **Practice that followed** [practice; S8]:
  - broad algorithm engineering with venues in theoretical computer science (WEA, ESA, ISAAC, LATIN, SODA);
  - industrial applications with Möhring's group;
  - combinatorics and geometry with Fekete, begun at Braunschweig; the last such paper is 2008 (ISAAC 2008, DOI 10.1007/978-3-540-92182-0_78).

### T5. A new tool: SCIP's pricing, then generic branch-and-price, then GCG (c. 2005–2010)
- **Trigger: a new tool.**
  - In Berlin his group had an application and tried SCIP's built-in pricing; they were probably the first to use branching information inside pricing (P4 0:50:06–0:51:15) [stated].
  - The book says he was part of the first team ever to use SCIP's column-generation capabilities, in version 0.81 (P7 p. vi) [stated-joint].
  - His fear of writing tree management made a framework attractive (P4 0:49:47–0:50:19) [stated].
- **Stated idea**: branch-and-price should become a commodity, the way cutting happens inside a branch-and-cut solver without the user knowing. That requires detecting the model's structure automatically. The work started in the Berlin years (P4 0:52:16–0:53:20) [stated].
- **Record**:
  - the code starts 25 Nov 2008 with Gamrath's Diploma thesis (P10; S5);
  - the first paper is SEA 2010 (S8).

### T6. Contract end, Darmstadt, then Aachen (2009–2010)
- **Trigger**: an expiring fixed-term contract and chance encounters.
- He describes each move as narrowly avoiding a wall, with no plan B (P4 0:46:59–0:47:31) [stated].
- He took the Aachen offer, made after five others declined; he calls it lucky and says he appreciates it (P4 0:47:48–0:49:28; P7 p. vi) [stated / stated-joint].

### T7. At RWTH, structure detection becomes the programme (2010–2015, ongoing)
- **Record** [practice]:
  - IPCO 2011, the SEA 2012 status report and *Mathematical Programming* 2015;
  - a 2014 slide titled "Forcing MIPLIB2003/2010 into Structure" (S5);
  - strIPlib, a library of structured instances: named in the 2022 *IJOC* abstract (P15) and in a 2026 post (P9, 2026-06-16).
- **Stated**:
  - the 2014 blog sentence quoted in §1 (P3);
  - in 2017, a keynote abstract on detecting exploitable model structure that also names the blind spots still needing research (P11);
  - in 2020, he tells CO@Work students that, in his group's experiments, Dantzig-Wolfe reformulations are usually so strong that cutting planes from the literature rarely help, which is why one looks for cuts in the master variables (P19 1:03:22–1:04:03). This connects to the group's papers on reformulation strength (SEA 2018, DOI 10.4230/LIPIcs.SEA.2018.11; *Discrete Optimization* 30 (2018), DOI 10.1016/j.disopt.2018.07.001) and on basis-derived cuts (SEA 2015, DOI 10.1007/978-3-319-20086-6_9) [practice; S8];
  - in 2021, he names this line as possibly his favourite (P4 0:52:16).
- **Where he wants it to go** [stated]: learn the model's semantics, apply domain tricks automatically and lower the threshold for users (P4 0:53:40–0:54:39). The GERAD bio gives the same long-term goal: get model semantics directly from an LP/MPS file (P2). In 2026 he writes that a solver with an expressive modelling language may gain because the semantics help the algorithms (P9, 2026-10-20).

### T8. LP degeneracy with Gauthier and Desrosiers (2011–2018)
- **Trigger: a collaborator.** Jean Bertrand Gauthier's doctoral work at HEC Montréal was on the primal simplex (S11 bio) [observed].
- **Record**, seven Cahiers from 2011 to 2017 and papers from 2014 to 2018 [practice; S2, S8]:
  - "Row-reduced column generation for degenerate master problems", *EJOR* 236(2) (2014), DOI 10.1016/j.ejor.2013.12.016;
  - "Decomposition theorems for linear programs", *ORL* 42(8) (2014), DOI 10.1016/j.orl.2014.10.001;
  - "About the minimum mean cycle-canceling algorithm", *DAM* 196 (2015), DOI 10.1016/j.dam.2014.07.005;
  - "Tools for primal degenerate linear programs: IPS, DCA, and PE", *EJTL* 5(2) (2016), DOI 10.1007/s13676-015-0077-5;
  - "A strongly polynomial Contraction-Expansion algorithm for network flow problems", *COR* 84 (2017), DOI 10.1016/j.cor.2017.02.019;
  - "Vector space decomposition for solving large-scale linear programs", *OR* 66(5) (2018), DOI 10.1287/opre.2018.1728.
- **Exit**: the last paper is from 2018. The book later says Gauthier "went private" (P7 p. 551 (PDF 582)). Linking the exit to Gauthier's departure is [inferred].

### T9. Public positioning of OR (2014–2016, continued on social media)
- **Trigger** [stated; P3, 2014-11-04]. Faculty-hiring committees had asked him what the next big thing would be. He answered with structure, and argued that OR should claim the science behind big data, the Internet of Things and Industry 4.0, before others give simpler, unscientific answers.
- **Related posts** [stated; P3]:
  - "Are we too complicated?" (2015-03-23);
  - two German posts on Industry 4.0 (2015-12-16 and 2016-03-02): data and networking alone produce no intelligence; prescriptive analytics needs optimization.
- **Practice**:
  - nine blog posts (P3);
  - the GOR 2014 proceedings and the *Zukunftsperspektiven* volume (S10, S7);
  - a 2018 TEDx talk contrasting machine learning, which in his framing extrapolates from the past, with optimization, which makes the best use of the future (P5 0:01:54, 0:11:26) [stated].
- **Exit from blogging, in his words**: he stopped, the blog was probably unread, and Twitter gave daily reactions (P4 1:01:39–1:02:18) [stated].

### T10. Applications through students and partners (2016–2019, continuing)
- **Record** [practice; S7, S8, S9]:
  - districting with Goderbauer (2019; and a talk in 2025, P12);
  - energy-system MINLP with Bardow and Koster (2016);
  - robotics with Corves (2017–18);
  - the Kiel Canal with Möhring (2019);
  - appointment scheduling (Roth 2020);
  - finished-vehicle logistics (Franzen 2022);
  - biobank scheduling (2023).
- **Self-description**: "more recently ... forays into engineering" (P7 p. vi) [stated-joint]. Beyond OR he also co-supervised a 2023 computer-science thesis on HPC data flow (DOI 10.18154/rwth-2023-06006; S17) [practice].
- The 2025 districting abstract describes the whole process, from data gathering and convincing officials to implementation and what decision makers said about the tool (P12) [stated].

### T11. Machine learning for MIP (2017–2022)
- **Record** [practice]: CPAIOR 2017, learning when to decompose; *IJOC* 2022, image-based structural similarity, with a Buffalo group (P15).
- **His framing over time**:
  - 2018: ML for simple, repetitive decisions; optimization for the decision itself (P5) [stated];
  - c. 2019–21: the overlap of ML and integer programming is one of two topics of special current interest to him (P2) [stated];
  - 2020: AI and ML as the latest evolution of OR (P8) [stated-joint];
  - 2026, co-signed: machine learning is "a strong tendency" for column generation (P7 p. 552 (PDF 583)) [stated-joint];
  - 2026, own reply: he asks whether there is also a stream for discrete optimization without machine learning (P9, 2026-02-27) [stated].
- No ML-for-MIP paper after 2022 was found [practice]. See Contradictions.
- **Trigger** [inferred]: automatic detection produces many candidate decompositions, and choosing among them turns structure detection into a learning problem. The GERAD bio supports this: its example is learning when to apply branch-and-cut rather than branch-and-price (P2).

### T12. Service and publication culture (c. 2016–2021)
- **INFORMS board**: a 2017 conference bio lists him as the serving Vice President for Information Technology (P11) [observed]. The 2021 podcast host introduces him as a past board vice president, with the portfolio heard as information strategy in the automatic captions (P4 0:00:52) [observed]. Term dates were not found.
- **Operations Research Forum**: co-founded with Pardalos in 2020 [stated-joint; P8].
  - The launch editorial invites failed experiments and wrong paths, software and tool descriptions, open data and code, and suggestions on how pre-registration could work for computational OR.
  - It solicits "failed experiments and wrong paths taken to learn from" (P8 p. 2) [stated-joint].
  - In 2021 he adds that hiring committees should value software (P4 1:12:49–1:13:43) [stated].
- **Exit**: he is not on the journal's board as read on 2026-11-08, where Yaroslav Sergeyev is Editor-in-Chief and Pardalos is Advisory Editor (S12) [observed]. The date he left is unknown.

### T13. Hands-on GCG work and the SCIP suite (2018–2026)
- **His own commits, 2018–21** [practice; P10], cover:
  - documentation and a capacitated-dominating-set use case;
  - usage and help texts;
  - detection-timing fixes;
  - release notes: one commit adds wished-for future features to them, another removes a self-congratulatory line;
  - a correction to the list of papers that use GCG (see §6).
- **The suite**:
  - GCG is part of the SCIP Optimization Suite reports: 8.0 (arXiv 2112.08872; *TOMS* 2023) and 10.0 (arXiv 2511.18580, Nov 2025, which ships GCG 4.0.0) (P18; P9, 2025-11-27);
  - the GitHub move in 2023; GCG 4.1.0 tagged 2026-09-18;
  - the CHANGELOG on master already carries a "Release notes for GCG 5.0" heading with no entries (P10) [practice].

### T14. The book as culmination (2015–2026)
- **Stated motive**: a standard text on column generation was needed, and the authors felt they were the ones to write it. The plan was for 2015–2017; the book appeared in 2026 (P7 p. xiii) [stated-joint].
- Writing what one knows "mercilessly reveals what one does not know": "facts" they took for granted turned out wrong (P7 p. xiii) [stated-joint].
- Desrosiers's January 2015 outline had 16 chapters. The final book has 8, with a list of 25 "More to Know" subjects left for future books (P7 p. 552) [practice]. Calling this a cut is [inferred].
- The book declares that no line of it was generated by a large language model (P7 p. xv) [stated-joint].
- It was published open access, funded by RWTH, HEC Montréal, Polytechnique Montréal and GERAD: Springer, Feb 2026, DOI 10.1007/978-3-031-96917-1, CC BY 4.0 (P7; S10).

### T15. Back to branch-and-price research papers (2026)
- Ciccarelli, Furini, Hojny & Lübbecke, "Branch-and-price strikes back for the k-vertex cut problem", arXiv 2602.04984 (v1 2026-02-04; v2 2026-06-05) [practice; P16].
  - It gives an extended formulation that dominates earlier ones in the LP bound.
  - It adds branching rules that preserve the structure of the pricing problems, plus valid inequalities and symmetry handling.
  - Furini was also a co-author in 2011 and 2015.
- Mühmer, Ganz, Lübbecke & Willamowski, "The Multi-Stop Station Location Problem: Exact Approaches", SSRN, DOI 10.2139/ssrn.7177419 (Crossref record created 2026-07-25) [practice; P17]. It has two pattern-based reformulations and branch-price-and-cut with shortest-path pricing, combined in a nested approach.
- [inferred] Both echo earlier designs: structure-preserving branching appears throughout the book's Chapter 7, and nested column generation goes back to *NRL* 2012.

## 4. Entry and exit relative to the consensus ([inferred] unless tagged)

| Topic | Entered | Relative to consensus | Left / status |
|---|---|---|---|
| Column generation for routing and scheduling | 1996 (PhD) | After the Montréal school had made it standard in transport; the book dates the GENCOL team to 1981 (P7 p. 546). Entered as a follower, then became a consolidator: the 2005 survey with Desrosiers is his most-cited work (S9). | Still central in 2026. |
| Generic, automatic Dantzig-Wolfe and branch-and-price (GCG) | 2008 (P10) | Early. In 2021 he recalls that many problem-specific branch-and-price codes existed, and that what was missing was a commodity solver (P4 0:52:33) [stated]. The book names other generic frameworks (P7 p. 538). Whether GCG was first is **not** established here. | Active (GCG 4.1, 2026). |
| Structure detection in MIP models | Stated 2014 (P3); papers from 2011 | By his own account, ahead of a field-wide norm. His 2014 claim is that solvers underuse the structure modellers encode. Note his 2026 post contrasting expressive modelling with the flattened matrix a MIP solver sees (P9). | Active; the semantics goal is still open (P2, P4, P9). |
| Combinatorics and computational geometry | 1998 / 2003 | Side line from the Diplom work and from Fekete. | Last paper 2008 (S8). |
| LP degeneracy (IPS, DCA, PE, VSD) | 2011 | Joined an existing GERAD line as co-author and theory consolidator (S2). | Last paper 2018. |
| Machine learning for MIP | 2017 (CPAIOR) | After Khalil et al., "Learning to branch in mixed integer programming", AAAI 2016, DOI 10.1609/aaai.v30i1.10080 (S15). Before the survey that marked the field, Bengio, Lodi & Prouvost, "Machine learning for combinatorial optimization: a methodological tour d'horizon", arXiv 1811.06128 (Nov 2018), *EJOR* 290(2):405–421 (2021), DOI 10.1016/j.ejor.2020.07.063 (S14). So an early entrant, not a first mover. | No paper after 2022. A 2026 remark is sceptical in tone (P9), while the co-signed 2026 book still calls ML "a strong tendency" (P7). |
| Electoral districting in Germany | c. 2016 (Goderbauer) | Practice-first entry: the tool was built with officials (P12) [stated]. | Talk in 2025. |
| Public outreach by blog | Oct 2014 | Followed Michael Trick's OR blog as a model (host remark, P4 1:01:19) [observed]. | Stopped Mar 2016 [stated]. Twitter from 2009, end not established; Bluesky from Feb 2024. |
| Journal founding and publication reform | 2020 | The launch editorial invites negative results, software descriptions and ideas on pre-registration (P8). How early this was relative to other OR journals was not assessed. | No longer on the board by 2026 (S12). |

## 5. Era and resource context of each practice

| Period | Compute and tools | Team and seniority | Evidence |
|---|---|---|---|
| 1996–2001 (Braunschweig) | CPLEX 3.0 through its C interface, column-wise model building, no branching. Literature by photocopy and inter-library loan. A partner whose planning was by pencil and paper. | Research assistant on a grant, in a small institute (Zimmermann) with links to CPLEX through Bixby. | P4 0:25–0:38; P7 p. vi; P13 |
| 2003–2009 (TU Berlin) | Early SCIP (version 0.81) with its pricing hooks, and close interaction with SCIP's developer in Berlin. | Fixed-term assistant professor in a large algorithms group (Möhring); habilitation 2007. | P4 0:45–0:51; P7 p. vi; P1 |
| 2009–2010 (Darmstadt) | — | Visiting professor on a two-year contract, commuting four hours from Berlin, while applying for permanent posts. | P4 0:47:31–0:48:09 |
| 2010–2018 (RWTH, building) | GCG on SCIP; the 2014 test material forced MIPLIB 2003 and 2010 instances into structure. | Chair with a cohort of research-assistant developers; among the core developers only Witt's PhD is confirmed. About 3 main committers in 2008–11, a period that straddles the move from Berlin, and about 5–6 in 2012–19. Teaching about 2,000 students a year in at least five courses (2021 figure, P4 0:56:43). | P10; S5; P4 |
| 2015–2026 (book) | Subversion repository; four authors in Montréal, Aachen, Blainville and Mainz. | A senior collaboration (GERAD, GENCOL). Open-access fees paid by four institutions. | P7 pp. xiii–xv |
| 2018–2021 | He commits to GCG himself; Twitter as his main outlet. | Chair holder doing documentation and release work by hand. | P10; P4 |
| 2023–2026 | GCG on GitHub and in conda-forge (README badge); SCIP suite releases; Bluesky. AI-generated mathematics enters public debate: he posts and reposts on it, and the book carries a no-LLM declaration. | Smaller active committer set, led by Mühmer. | P10; P9; P7 p. xv |

## 6. Failures, abandoned directions and corrections (dated)

1. **c. 1992 — refused for informatics**, his only application. He describes it as possibly the first thing in his life that went wrong (P4 0:15:53) [stated].
2. **c. 1997 — first paper desk-rejected** by a prestigious journal, then accepted by *Comput. Geom.* in 1998 (P4 0:31:10–0:32:22) [stated].
3. **1999–2001 — tailing-off and instability he could not fix** in his thesis code. The open questions fed the 2005 survey (P4 0:37:32–0:38:53) [stated].
4. **2001–2003 — every North-American faculty application rejected** (P4 0:43:22; P7 p. vi) [stated / stated-joint].
5. **2009 — near-exit from academia**: a month before the Berlin contract ended, with no plan B (P4 0:45:44–0:47:31; P7 p. vi) [stated / stated-joint].
6. **2010 — sixth choice**: the Aachen chair came only after both short lists declined (P4 0:48:23–0:49:12) [stated].
7. **2013 — an unpublished manuscript.** Lübbecke & Puchert's paper on large-neighbourhood search and diving heuristics from Dantzig-Wolfe reformulation is still cited as unpublished in 2026 (P7 references) [practice]. Whether it was rejected or never submitted is unknown.
8. **2014–2016 — promises the blog did not keep**, because the blog ended first [practice; P3]:
   - "How to write a paper" (2014-11-21) promised a follow-up;
   - "Know your Heuristics!" (2014-12-19) promised a post on when heuristics fail on practical data;
   - "#industrie40" (2016-03-02) promised a post on the group's hospital-scheduling research.
9. **2015–2026 — the book ran about nine years over plan**, 2026 instead of 2015–17, and went from a 16-chapter outline to 8 chapters (P7 pp. xiii, 552) [stated-joint / practice; reading this as a cut is inferred].
10. **2019 — release-note editing**: he reverted a merge on 2019-07-08 and removed self-congratulatory wording from the release notes on 2019-06-13 (P10) [practice].
11. **2020-10-09 — correcting his own impact claim**: his commit removes from GCG's list of papers that use GCG those that only cite GCG or Gamrath & Lübbecke (2010) without using the code (P10, commit e21f41cc) [practice].
12. **c. 2016–2021 — a stated self-criticism**: he sometimes posts things he later regrets (P4 1:03:50–1:04:09) [stated].

## 7. Authorship and role labels by period (what the skill may say)

- **Sole-author records**:
  - the PhD thesis (2001);
  - *EJOR* 162 (2005);
  - SEA 2012;
  - the blog (2014–16), the GERAD bio and his Bluesky posts;
  - talk abstracts (2017, 2025).

  These are the only places where a method claim is Lübbecke's alone.
- **Joint authorship.** Most papers are joint. In German mathematics the author order is often alphabetical, which applies to many of his bylines, so first and last authorship tells little. DNB and DataCite list him first among the supervisors of five RWTH theses from 2019–2022; MGP records only one of them (S6, S7, S17).
- **GCG** is group work. Gamrath laid out the design (2008). Lübbecke is listed as project initiator and head (S5) and wrote some commits himself (2018–21; P10). Cite the code as the RWTH group's practice.
- **The book** has four authors; no passage is his alone. The author notes are written in the third person and the writer is not identified. The Conclusion is signed by Marco, Guy and Jean Bertrand (P7 p. 546).
- **The 2020 editorial** is co-signed with Pardalos.

## 8. Latest activity and the last 12 months (2025-11-08 to 2026-11-08)

| Date | Item | Tag | Source |
|---|---|---|---|
| 2025-11-17 | Member of a habilitation committee in Paris. | [stated] | P9 2025-11-18 |
| 2025-11-23 / 24 / 27 | SCIP Optimization Suite 10.0 report on arXiv (2511.18580; he is one of 34 authors). GCG v4.0.0 tagged on 24 Nov. He announces the release (SCIP 10.0.0 with GCG 4.0.0) on 27 Nov. | [practice] / [stated] | P18; P10; P9 |
| 2026-01-06 | Revised GERAD cahier of the book, dated 6 January 2026; GERAD lists the revision as January 2026. | [practice] | P7; S3 |
| 2026-01-07/08 | Attends Aussois 2026 and highlights an integer-programming result on Ramsey-number bounds by Traversi and co-authors. | [stated] | P9 |
| 2026-01-23 | Eduardo Uchoa teaches in Lübbecke's column-generation class; Lübbecke and Marc Pfetsch discuss SCIP's future. | [stated] | P9 |
| 2026-02-03 | GCG v4.0.1 tagged. | [practice] | P10 |
| 2026-02-04 | arXiv 2602.04984 v1, the k-vertex-cut branch-and-price paper; v2 on 2026-06-05. | [practice] | P16 |
| 2026-02-06 / 07 / 10 | *Branch-and-Price* published by Springer, open access: GERAD news on 6 Feb, Crossref record created 6 Feb, hardback dated 7 Feb. He announces on 10 Feb that it is finally out. | [practice] / [stated] | S1; S10; S11; P9 |
| 2026-02-27 | Asks whether a conference also has a discrete-optimization stream without machine learning. | [stated] | P9 |
| 2026-03-27 | The four book authors meet to celebrate. | [stated] | P9 |
| 2026-04-03 | GCG v4.0.2 tagged. | [practice] | P10 |
| 2026-06-16 | Points to strIPlib and GCG's test-set documentation. | [stated] | P9 |
| 2026-07-12 to 17 | Attends IFORS 2026: <br>• collects signatures in his copy of the book; <br>• recalls that Terlaky chaired his first conference session in 1996; <br>• posts on column-generation talks. | [stated] | P9 |
| 2026-07-25 | Crossref record created for the multi-stop station location preprint (SSRN). | [practice] | P17 |
| 2026-09-02 | Attends OR 2026, the GOR annual conference. | [stated] | P9 |
| 2026-09-18 | GCG v4.1.0 tagged (subset-row cut separator); master already carries a GCG 5.0 heading; last repository push 2026-10-30. | [practice] | P10 |
| 2026-10-20/21 | MIP 2026, posting from Rome: <br>• his student Alex Helber wins the poster competition; <br>• he relates Eisenbrand's talk to a Dantzig-Wolfe hierarchy from his own group (his wording; not found as a paper); <br>• he remarks on expressive modelling versus flat models. | [stated] | P9 |
| 2026-10-26/27 | 25th anniversary of his PhD; his team presents a gift. | [stated] | P9 |
| 2026-11-07 | In a thread on Stigler's diet problem: those who design the objective function hold power and should use it responsibly, which he says he teaches using the diet LP. | [stated] | P9 |

Repost noted once, not as his words: on 2026-09-26 he reposted Matteo Fischetti's post on the feasibility pump with objective cutoff in SCIP, a study by a fellow member of this team (P9) [observed: repost]. His own posts and replies in Sep–Oct 2026 return often to AI-generated mathematics and research quality (P9). As a pattern, this is [inferred].

**No new position, award or move was found in the window.** Recent events just outside it: the CG School in Paris in May 2025 and the Paderborn talk in July 2025.

## 9. Pointers for the synthesis (all [inferred])

- **Layer 2, problem choice**:
  - Problems arrive through people and grants: an in-plant railroad, Gauthier's simplex work, students' application domains.
  - His own agenda is generic and stable since 2008–2014: structure first, then semantics.
  - He keeps very long projects: GCG for 18 years, the book for 11 years of writing and 25 of intent.
- **Layer 7, organisation**:
  - Cohorts of research assistants carry the code. He initiates, heads, documents and curates.
  - A Montréal network sustained through schools and co-authorship.
  - Heavy teaching, which he treats as dissemination (P4 0:56:25–0:58:56).
- **Layer 1, taste**:
  - exact methods: he calls himself a supporter, even a fan, of exact optimization (P3 2014-12-19);
  - the question why something works, which he says drives him (P4 0:09:50);
  - integer *linear* programming, which he expects to stay with for the rest of his career (P4 0:55:17);
  - conclusions that conclude rather than summarise (P9 2026-02-18 and 2026-08-24; P3 2014-11-21);
  - responsibility in choosing the objective (P9 2026-11-07).
- **Layer 5, judging results**:
  - delight at finding bugs, and suspicion when results look better than they should (P4 0:09:03–0:09:50) [stated];
  - correcting the group's own impact list (§6.11).
- **Layer 4, execution**: whether "limitations drive creativity" (P7 p. vi; P4 0:06:24–0:07:17) shows in GCG code style should be checked in 03-process-evidence, not assumed here.

## Contradictions (kept, not reconciled)

1. **Machine learning.** Around 2019–21 his GERAD bio names the overlap of ML and integer programming as a topic of special current interest (P2). The 2026 book, co-signed, still calls ML "a strong tendency" (P7 p. 552). But on 2026-02-27 he asks for a discrete-optimization stream *without* machine learning (P9), and no ML-for-MIP paper after 2022 was found (S8, S9).
2. **First conference.** A 2026 post puts his very first conference presentation in 1996, with Terlaky as session chair (P9). The 2021 interview calls ISMP 1997 his first real conference, after a Braunschweig conference that he helped organise (P4 0:32:22–0:32:41). Whether the 1996 talk was at that Braunschweig meeting is not checked.
3. **Student roles.** MGP lists Gellert (TU Berlin 2015) with Lübbecke as "Advisor 2". The DNB title statement for the same thesis names him as *Gutachter* (referee), with Möhring as *Betreuer* (S6, S7). DNB's "Akademischer Betreuer" field also lists referees in several records.
4. **Student counts.** MGP has 5 students and only one RWTH first-supervised PhD. DNB and DataCite show at least 5 RWTH first-supervised PhDs from 2019 to 2022, plus co-supervisions. None of the three lists the core GCG developers (S6, S7, S17).
5. **Name of the INFORMS role.** "Vice President for Information Technology" in a 2017 conference bio (P11); "vice president for information strategy" in the 2021 podcast introduction, from automatic captions (P4 0:00:52). INFORMS's own pages name "Technology Strategy" as the VP role from 2019 (S13).
6. **Rhythm of the events.** The GERAD bio calls the alternating school-and-workshop series *biannual*, which presumably means every two years (P2). The record shows 2006, 2008, 2010, 2012, 2014, 2016 and 2018, then 2023 and 2025: a five-year gap after 2018 (S4, P7 p. 547).
7. **Teaching awards.** The book calls him "a teaching awards-winning professor", plural (P7 p. vi). GERAD lists one, the RWTH 2022 Teaching Award (S1).
8. **Book size and date.** Page counts: 689 (GERAD people page, June 2024), 657 (GERAD paper page, revised version), 695 PDF pages (the cahier PDF dated 6 Jan 2026, created 13 Mar 2026) and 663 (Springer). Publication date: 6 Feb (GERAD news, Crossref) or 7 Feb 2026 (bookseller hardback). All from S1, S3, S10, S11 and P7.
9. **Volume of the 2019 districting paper.** GERAD lists it as volume 51(1) (S2); the DOI encodes 2019, issue 1. The volume was not checked, so it is not stated here.
10. **The IVADO Labs attribution.** A WebSearch summary gave Lübbecke an IVADO Labs advisory role; the bookseller's author bios give it to Desaulniers (S11). The search summary is wrong and is kept here only so that the error is not repeated.
11. **Tension, not a contradiction in his own framing.** He calls himself a fan of exact optimization (P3, 2014-12-19), yet he co-authors primal heuristics for branch-and-price (OR Proceedings 2011 (2012), DOI 10.1007/978-3-642-29210-1_11) and the 2013 LNS/diving manuscript. He frames heuristics as serving exact branch-and-bound (P3).

## Gaps

- **Habilitation (2007)**: title and form not found. Not in DNB; the old COGA pages have no entry; the RWTH site was unreachable.
- **Diplom year and exact enrolment year**: inferred only (c. 1992–96).
- **RWTH chair and GCG sites**: unreachable on 2026-11-08. This blocked the staff CV, the talks list, the theses list and the GCG page listing papers that use GCG. One search snippet mentioned a 2021 keynote titled "Science Communication for Operational Research"; it is **unverified** and not used.
- **Doctoral outcomes of the core GCG developers** (Bergner, Puchert, Bastubbe, Kruber, Mühmer, H. Franzen): not in MGP, DNB, OpenAlex or DataCite, where his RWTH theses do appear. publications.rwth-aachen.de served a bot challenge. Whether they finished PhDs elsewhere, or have not yet, is unknown.
- **The 1996 grant**: its funder and title are not confirmed. The 2004 BMBF final report on rail-car management (S17) may be the same project or a follow-up.
- **INFORMS term dates** and **Operations Research Forum editorship end date**: not found.
- **Which application was the first to use SCIP's column generation (v0.81)**, and SCIP 0.81's date: not identified.
- **Why his journal output fell in 2019–2025**: he states no reason anywhere found. §0 lists the activities that coincide with it; any causal link is inferred.
- **Rejections beyond the 1997 desk rejection**, and the fate of the 2013 manuscript: not found. The field has no public review records comparable to OpenReview.
- **The date of the GERAD bio**: undated. Internal clues: it counts ten Cahiers with Desrosiers (the tenth posted Feb 2017, the eleventh Jun 2024), names Twitter as his main channel, and dates the Desrosiers link to twenty years earlier, when he sought an external PhD reviewer. These suggest 2019–2021 [inferred].
- **The Dantzig-Wolfe hierarchy he mentions** (P9, 2026-10-20): no paper by that name was found.
- **Status of the 2026 preprints** (arXiv 2602.04984; SSRN 7177419): whether accepted is not established.
- **Twitter/X history (from 2009)**: requires login; not read. Whether and when he stopped posting there is not established.
- **The podcast (P4)**: automatic captions with garbled names. Timestamps let a reader check the audio, but nothing from it has been checked against the audio.

## Sources

**Primary**

- P1 — ORCID public record 0000-0002-2635-0522 (employment and works, self-asserted), via pub.orcid.org API v3.0, read 2026-11-08. Primary.
- P2 — Marco Lübbecke, "Biography" (first person, undated), GERAD people page, https://www.gerad.ca/en/people/marco-lubbecke, read 2026-11-08. Primary.
- P3 — Marco Lübbecke, blog *café opt*, nine posts 2014-10-15 to 2016-03-02, https://mluebbecke.wordpress.com/ (RSS feed /feed/). Primary.
- P4 — *Subject to* podcast, "Subject to: Marco Lübbecke" (host Anand Subramanian), YouTube JzWAAvryTKA, uploaded 2021-09-23, 4,522 s; automatic-caption transcript in `talks/2021-09-23_subject-to-podcast_auto-transcript.txt` (saved by agent 02). Primary.
- P5 — Marco Lübbecke, "Anything you can do I can do better", TEDxRWTHAachen, YouTube Dc38La-Xvog, uploaded 2019-02-27, 756 s; recording date 2018-06-09 per agent 02's header (not re-checked); transcript in `talks/`. Primary.
- P6 — RWTH Aachen University, "RWTH verleiht Lehrpreis 2022 an Marco Lübbecke", YouTube LZLMijusUhg, uploaded 2023-03-08; captions in `talks/` (his speech from 0:01:22). Primary.
- P7 — Desrosiers, Lübbecke, Desaulniers & Gauthier, *Branch-and-Price*, Les Cahiers du GERAD G-2024-36 (version dated 2026-01-06), https://www.gerad.ca/papers/G-2024-36.pdf; Springer 2026, DOI 10.1007/978-3-031-96917-1, CC BY 4.0. Used: author notes pp. v–vi, Foreword pp. xi–xii, Preface pp. xiii–xv, p. 538, pp. 546–553, references. Primary (joint).
- P8 — Lübbecke & Pardalos, "Welcome to SN Operations Research Forum!", *SN Operations Research Forum* 1:1 (published 2020-02-05), DOI 10.1007/s43069-020-0001-1, CC BY 4.0. Primary (joint).
- P9 — Marco Lübbecke, Bluesky profile mluebbecke.bsky.social (created 2024-02-06) and own posts and replies from 2025-09-04 to 2026-11-07, via public.api.bsky.app. Primary.
- P10 — GCG repository, https://github.com/scipopt/gcg (Apache-2.0): bare clone of 2026-11-08; commit 61d4b710 (2008-11-25), commit e21f41cc (2020-10-09), tags v010 to v4.1.0, CHANGELOG and README on master. Primary (group).
- P11 — ORBEL 31 (KU Leuven 2017), "Key speakers" page, https://www.orbel.be/orbel31/keyspeakers.php: Lübbecke keynote abstract and bio. Primary (abstract) / observed (bio).
- P12 — Paderborn University, PRIME colloquium announcement, talk of 2025-07-01, https://wiwi.uni-paderborn.de/en/dep3/news/message/prime-who-wants-political-re-districting-in-germany: abstract and bio. Primary (abstract) / observed (bio).
- P13 — Lübbecke & Zimmermann, "Engine routing and scheduling at industrial in-plant railroads", *Transportation Science* 37(2):183–197 (2003), DOI 10.1287/trsc.37.2.183.15251; abstract via Crossref. Primary (joint).
- P14 — Lübbecke & Desrosiers, "Selected topics in column generation", *Operations Research* 53(6):1007–1023 (2005), DOI 10.1287/opre.1050.0234; abstract via OpenAlex. Primary (joint).
- P15 — Steever, Murray, Yuan, Karwan & Lübbecke, "An image-based approach to detecting structural similarity among mixed integer programs", *INFORMS J. Computing* 34 (2022), DOI 10.1287/ijoc.2021.1117; abstract via OpenAlex. Primary (joint).
- P16 — Ciccarelli, Furini, Hojny & Lübbecke, "Branch-and-price strikes back for the k-vertex cut problem", arXiv 2602.04984 (v1 2026-02-04, v2 2026-06-05). Primary (joint).
- P17 — Mühmer, Ganz, Lübbecke & Willamowski, "The Multi-Stop Station Location Problem: Exact Approaches", SSRN preprint (2026), DOI 10.2139/ssrn.7177419; abstract via Crossref (record created 2026-07-25). Primary (joint).
- P18 — Hojny et al. (34 authors, including Lübbecke), "The SCIP Optimization Suite 10.0", arXiv 2511.18580 (2025-11-23). Primary (group).
- P19 — Marco Lübbecke, "Column Generation, Dantzig-Wolfe, Branch-Price-and-Cut", CO@Work 2020 lecture, YouTube vx2LNKx48vY (channel "Mixed Integer Programming"), uploaded 2020-09-23, 5,901 s; caption excerpts in `talks/2020-09-23_coatwork-2020-decomposition-lecture_caption-excerpts.txt` (saved by agent 02). Primary.

**Secondary and observed**

- S1 — GERAD people page: news (2023-05-17, 2026-02-06), events (CG 2023, CG School 2025), prizes, and associate membership since Dec 2018, https://www.gerad.ca/en/people/marco-lubbecke. Secondary (institutional).
- S2 — GERAD, Lübbecke publications list (Cahiers G-2002-64 to G-2024-36 with dates), https://www.gerad.ca/en/people/marco-lubbecke/publications. Secondary.
- S3 — GERAD paper page G-2024-36 (June 2024, revised January 2026), https://www.gerad.ca/en/papers/G-2024-36. Secondary.
- S4 — François Soumis, Foreword (October 2023), in P7 pp. xi–xii. Secondary (observer).
- S5 — Jonas Witt, GCG talk, SCIP Workshop 2014, Berlin, 2014-10-01, https://www.scipopt.org/workshop2014/gcg_witt.pdf (slides on GCG history and team). Secondary (group member).
- S6 — Mathematics Genealogy Project, records 74622 (Lübbecke), 23338 (Zimmermann), 200581, 331029, 206574, 200584 and 257173, https://www.mathgenealogy.org/, read 2026-11-08. Secondary.
- S7 — Deutsche Nationalbibliothek catalogue, SRU query per=Lübbecke and per=Marco (53 records), https://services.dnb.de/sru/dnb, read 2026-11-08. Secondary.
- S8 — DBLP, pid 24/5951, via the SPARQL endpoint https://sparql.dblp.org/sparql (58 records, 1998–2023), read 2026-11-08. Secondary.
- S9 — OpenAlex author A5082694588 (counts by year, affiliations, works) and split record A5129110788, https://api.openalex.org, read 2026-11-08. Secondary.
- S10 — Crossref records: the book DOI 10.1007/978-3-031-96917-1 (created 2026-02-06, CC BY 4.0, ISBN 9783031969164 / 9783031969171), and the other DOIs cited above, https://api.crossref.org. Secondary.
- S11 — Bookseller record for *Branch-and-Price* (hardback 2026-02-07; author bios), https://betterread.com.au/book/branch-and-price.do. Secondary.
- S12 — Springer, *Operations Research Forum* editorial board page, https://link.springer.com/journal/43069/editorial-board, read 2026-11-08. Secondary.
- S13 — INFORMS, election page "Vice-President - Information Technology" (S. Raghavan's statement: VP Technology Strategy since 2019), https://www.informs.org/About-INFORMS/Governance/INFORMS-Election/Vice-President-Information-Technology2. Secondary.
- S14 — Bengio, Lodi & Prouvost, "Machine learning for combinatorial optimization: a methodological tour d'horizon", *EJOR* 290(2):405–421 (2021), DOI 10.1016/j.ejor.2020.07.063; arXiv 1811.06128 (2018-11-15). Secondary (context marker).
- S15 — Khalil, Le Bodic, Song, Nemhauser & Dilkina, "Learning to branch in mixed integer programming", AAAI 2016, DOI 10.1609/aaai.v30i1.10080. Secondary (context marker).
- S16 — arXiv API author queries "Lubbecke" and "Luebbecke" (6 records each; includes cs/0310034 and 2112.08872), https://export.arxiv.org/api/query, read 2026-11-08. Secondary.
- S17 — DataCite REST API, query contributors.name "Lübbecke" (45 hits; 26 concern him: 16 ATMOS 2010 editor records, 9 theses, 1 report). Used: RWTH theses with supervisor metadata and "available" dates (10.18154/…); ETH Zürich thesis 10.3929/ethz-a-006697371; TIB report 10.2314/gbv:471272760 (2004). https://api.datacite.org, read 2026-11-08. Secondary.

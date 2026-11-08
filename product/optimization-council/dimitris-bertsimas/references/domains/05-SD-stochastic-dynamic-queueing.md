# SD · Stochastic and dynamic optimization, applied probability and queueing — Dimitris Bertsimas

> Domain file of the research-craft skill [SKILL.md](../../SKILL.md); it expands the SD row of the Domain Map. **Scope** (team.json): stochastic networks and scheduling, achievable-region and conservation-law methods, bandits, stochastic and dynamic vehicle routing, large deviations, probabilistic analysis of combinatorial problems. **Teams engaged**: none. team.json maps no repository team to SD, so in the council this is the lead's own ground (§6 names the nearest guest members). **Evidence base** (domain pack): 102 research works tagged SD as primary and 33 as secondary, or 99 and 32 distinct works once the version pairs S185 = S580, S016 = S261, S032 = S597 and S197 = S340 count once. Of the 99 primary works, 54 have a full-text card, 12 a partial, 9 an abstract and 13 a metadata card; 11 have none (students' theses, a talk, a private conversation, a 223-page text on large deviations). Secondary: 15, 4, 1, 2 and 10. **Book material**, not research works: five items, each read in full for its item: the queueing book's publisher page [B013 p. 1], his books pages [B008 pp. 1–2] and three items on *Data, Models, and Decisions* (B014, B015, B016). **Voice**: stated in his sole-author texts of 1988–1995 (correction C1); everything else is joint. `[S016 p. 3]` = card S016 at the file page; abstract- and metadata-level cards are cited by ID only; research notes in prose. Research date 2026-10-29.

## 1. Footprint and timeline

| Period | Primary SD works (distinct) | Secondary | SD share of his tagged rows (pack) | Main lines |
|---|---|---|---|---|
| 1985–89 | 6 | 1 | 7/10 | thesis; Coxian multiserver queues |
| 1990–94 | 33 | 1 | 34/51 | a priori optimization, dynamic routing, transient queues, probabilistic constants, first achievable-region papers |
| 1995–99 | 34 | 2 | 34/69 | conservation laws and bandits, distributional laws, large deviations, fluid stability, execution costs |
| 2000–04 | 10 | 8 | 10/48 | restless bandits, Lyapunov performance bounds, fluid job shops, revenue management |
| 2005–09 | 6 | 2 | 6/60 | dynamic programs in pricing, auctions, marketing, constrained LQ control |
| 2010–19 | 3 | 11 | 3/182 | runway configurations, decomposable MDPs, tree search against rolling horizon; robust queueing (RO-primary) |
| 2020–26 | 4 | 6 | 5/276 | ML control of fluid networks and restless bandits; Wordle by exact DP; the queueing book |
| undated | 3 | 1 | 4/30 | — |

- **Entry.** Part of his master's thesis under Odoni became the Coxian G/G/s analysis [S168 p. 17], which his 1988 sole-author paper extended to waiting times [S239 p. 1]; on the cards the earliest queueing paper is the Ek/C2/s paper with Papaconstantinou, accepted in 1986 [S329; S291 pp. 7, 14]. The 1988 thesis took its problem class from Odoni's group [S048 pp. 18, 71, 125].
- **Peak.** 1990–1999 hold 67 of the 99 primary works: two thirds, then half, of his tagged output. His NSF Presidential Young Investigator award with Draper Laboratory matching funds funded much of it [S057 p. 48; S185 p. 51], and the 1994 working paper thanks eight PhD students [S580 p. 49].
- **Exit.** Queueing-titled journal papers run 9 (1988–94) and 16 (1995–99), then 2, 1, 1, 1 and 0; the original programme ends with the 2001 Lyapunov paper [S123] (note 06 T2 and §5). The exit follows his stated move, about 1997–98, from impressing seniors to choosing what he judged important, and the start of finance and then RO (note 06 T4); that the move caused the exit is not documented.
- **Returns**, each with a newer tool (finance ran in parallel from 1998, inside the peak [S009 p. 3]): dynamic programs with structure kept in revenue management, auctions and marketing [S034 p. 8; S077 p. 4; S106 pp. 7–9]; uncertainty sets in place of distributions [S119 pp. 7–13]; machine-learned fluid policies [S402 pp. 9–10; S681 pp. 7–8]; a certified exact dynamic program [D021 pp. 6–8]; a 2022 book with Gamarnik (abstract card S334; joint publisher page [B013 p. 1]).
- **Who.** Thesis line: Odoni and Jaillet [S038], Howell [S102], Goemans [S229], van Ryzin [S195; S829], Avram [S158; S126]. Queueing analysis: Papaconstantinou [S291; S389], Nakazato [S220; S129], Keilson and Zhang [S346], Mourtzinou [S280; S336; S173]. Routing: van Ryzin [S016; S032; S091], Xu [S293], Simchi-Levi [S025]. Achievable region: Paschalidis and Tsitsiklis [S072; S237], Niño-Mora [S057; S051; S212; H010], Chryssikou [S368], Avram and Ricard [S098]. Stability, fluid and large deviations: Gamarnik [S181; S130], Sethuraman [S205; S207], Paschalidis and Tsitsiklis [S177; S187; S140]. Airports: Peterson and Odoni [S135; S659]. Later: Lo [S009], Popescu [S034], Mersereau [S106], Mišić [S197; S216], Kim and again Niño-Mora [S402; S681]. Students carry the lines (van Ryzin [S016 p. 1], Niño-Mora [S051 p. 11]); co-advising with Tsitsiklis and Odoni is in the thesis records (note 04).

## 2. Signature works

Chosen by Scholar counts in the pack, his own folders (Stochastic Networks, Queuing Theory, Stochastic Scheduling, Applied Probability, Large Deviations, Vehicle Routing; note 01 §1.2) and the turns.

**SW-SD1 · A priori optimization and the 1988 thesis** [S048; S038; S017; S148] (Scholar 329, 403, 733).
- *Forced*: re-solving the same problem on each day's instance means many NP-hard solves without the resources, and operators want the same driver on the same route [S048 p. 12; S017 p. 1]; Odoni had posed the PTSP for mail delivery [S038 p. 5].
- *Insight*: optimize one a priori solution plus a trivial update rule for expected cost over all 2^n instances, with closed forms summed edge by edge [S048 pp. 30–32]; asymptotically it matches re-optimization on random Euclidean instances [S038 pp. 7–8]; sorting heuristics keep their guarantee on every instance [S038 pp. 9–10].
- *Evidence*: the asymptotic theorems, NP-completeness [S038 p. 8], a cyclic heuristic within a factor two [S017 p. 9].
- *Reception*: a 1989 Nicholson prize (note 06 §1); no critique on record. The thesis's O(1) hinge broke when Bertsimas–Grigni showed O(log n) tight [S048 pp. 100–101; S038 p. 10].
- *Method*: Method 3's precursor, the price of simplicity: "one pays for these nice properties (robustness, globality) by changing the complexity of the problem radically." [S048 p. 29].

**SW-SD2 · Stochastic and dynamic vehicle routing** [S016; S032; S091; working papers S261, S597] (739, 442, 180); SKILL SW6.
- *Forced*: "the TSP is a deterministic, static approximation to a problem which is, in reality, both probabilistic and time varying (dynamic)." [S016 p. 1]; a colleague, Psaraftis, raised it [S016 p. 14].
- *Insight*: bound every policy first, in light and heavy traffic, with a tagged demand and Wald's equation; then analyse simple policies against the bounds [S016 pp. 3, 5–6]. Batching into TSP tours makes a GI/G/1 queue [S016 p. 10].
- *Evidence*: light-traffic optimality, heavy-traffic constant factors, system time growing like (1 − ρ)⁻² [S016 pp. 5–11]; m vehicles cut it by 1/m² [S597 p. 3]; capacity makes stability depend on geometry [S032 p. 3]; for general densities a twice stronger bound and a factor of about 1.8 [S091 pp. 2–3, 11].
- *Reception*: 251 citation contexts, none a substantive critique (note 05 §6). The working paper's "partly heuristic" bound [S261 p. 30] became a proved, looser constant in print [S016 pp. 7, 9].
- *Methods*: 7, 1 (an analysable queue reached by policy design), 3 (one knob: 10% less travel costs 21% more system time [S032 p. 16]).

**SW-SD3 · Achievable region, conservation laws and bandits** [S072; S057; S580; S185; S051; also S237, S368, S212, H010] (234, 288, 321); SKILL SW1.
- *Forced*: stochastic scheduling rests on dynamic programming and ad hoc methods [S057 p. 1]; network policies are judged by simulation with no optimality yardstick [S072 p. 2].
- *Insight*: optimize over achievable performance vectors. Conservation laws make the region an extended polymatroid whose vertices are priority rules; adaptive greedy solves its LP, and the indices are sums of dual variables [S057 pp. 11–13, 20]. Where the region is not exact, potential functions give O(R²) LP and PSD relaxations [S072 pp. 15–16, 21–22]; for restless bandits, Whittle's relaxation is the first rung of a hierarchy and an index comes from reduced costs [S051 pp. 5–9].
- *Evidence*: the cμ rule, Smith's rule, Klimov's and Gittins's algorithms as one algorithm [S057 pp. 3–4, 22, 38]; network bounds 83–99% efficient in most regimes, 62% at worst [S072 pp. 27–31]; loss networks within 0–2.5% under symmetric rewards [S368 p. 1].
- *Reception*: Erlang and SIAM prizes in 1996, works not named [S181 p. 14]; Glazebrook used the polyhedral results before print [S057 p. 16]; the restless bandit returns in 2026 [S681 pp. 1, 8]. No critique was searched (note 05, Gaps).
- *Limit he printed*: "the heuristics were somewhat ad hoc." [S185 p. 49], and policies from relaxations do not exist for networks [S185 p. 49] (the 1994 tables grade simulated or published policies [S072 pp. 27–30]; the two network policies proposed in 1999 are untested [H010 pp. 26–28]).

**SW-SD4 · Optimal control of execution costs** [S009; S145] (1,606, his most cited SD-tagged work).
- *Forced*: the law requires best execution, which nobody had defined [S009 pp. 2–3].
- *Insight*: best execution as the optimum of a stochastic dynamic program with the trade's own impact in the law of motion; the paper calls the practitioners' equal split "optimal only in one very special case" (linear permanent impact, arithmetic random walk) [S009 pp. 8–9, 43], though its constrained multiplicative-impact case recovers the split at θ = 1 [S009 pp. 36–37]; the LPT law makes impact temporary and keeps the closed form [S009 pp. 20–22].
- *Evidence*: simulated savings in cents per share against the equal split, a losing path printed [S009 pp. 14, 23–24]; the portfolio version calibrated on ITG's proprietary trade records [S145 pp. 7–11].
- *Reception*: limits self-identified (note 05 §5.3, corrected by C18). The 25–40% headline is not a row of its table [S009 pp. 24–25].
- *Methods*: 5 (the practitioners' rule), 1 (stay linear-quadratic; constraints create 3^k pieces [S009 p. 35]), Heuristic 1. Full anatomy: [09 ledger](../research/09-evidence-ledger.md#anatomy-execution-costs).

**SW-SD5 · Robust queueing** [S065; S227; S119; S268] (S119: 143; RO-primary, SD-secondary).
- *Forced*: GI/GI/m and network analysis are intractable [S119 pp. 2–3]; a stated programme to replace the Kolmogorov axioms by uncertainty sets [S065 p. 5].
- *Insight*: CLT-shaped polyhedral sets on partial sums, a closed-form worst case of the Lindley recursion, and a set family closed under departures, superposition and thinning [S119 pp. 7–13, 25–40].
- *Evidence*: RQNA against Whitt's QNA on Kuehn's network [S119 p. 50], after the variability parameters were fitted to simulated queues [S119 pp. 45–47].
- *Reception*: the sharpest critique of his SD record (§5); the programme faded (note 06 T8).
- *Method*: 1 as a variant (closed forms, not a solver class); 3 with the knob fitted to data.

**SW-SD6 · Machine-learned fluid policies** [S402; S681].
- *Forced*: fluid control is re-solved from every initial state, and Whittle's index needs indexability [S402 p. 2; S681 p. 2].
- *Insight*: prove the structure of the optimal policy (hyperplanes through the origin) and train OCT-H trees whose class contains it [S402 pp. 9–10]; in 2026, derive the top-m index structure of PMP extremals from a per-instant LP's dual and build tree features from it, a step the authors call heuristic [S681 pp. 7–8, 14–17].
- *Evidence*: 100% test accuracy in 21 settings [S402 p. 20]; a maximum gap of 0.0181 to the extremals, with speed-ups per query [S681 pp. 24–26].
- *Reception*: too recent for critique. The 2026 paper proves that sufficiency fails and calls its solutions extremal [S681 pp. 4–5, 8–9].
- *Methods*: Heuristic 5; Method 2 step 6 (a return when the tool changes).

## 3. How he works here

**M1 · Formulation first, kept in the class.** Stated alone: "The theme in the paper is the thesis that better formulations lead to deeper understanding and better solution methods." [S185 p. 1]; the difficulty is "primarily the dynamic and combinatorial character of the problem" [S580 p. 10]. Until about 1997 the kept class is an analysable distribution or queue class: Coxian stages dense in all distributions [S239 pp. 1–2, 8; S168 pp. 3, 12]. From 1993 it is an LP, convex or SDP relaxation of a performance region [S072 pp. 14–16, 21–22; S057 p. 20], stability as LP feasibility [S181 pp. 5–7], loss networks [S368 pp. 4–8]. ⚠ Say–do: at least fifteen SD works read in full or in part are pure analysis (closed forms, distributional laws, limit theorems) with no optimization model, among them [S129 pp. 1–2; S336 p. 2; S322 p. 1; S173 p. 2] (my count from the cards; Tension T3).

**M2 · Why now.** The returns are tool changes without a rebuilt figure: OCT-H for restless bandits [S681 pp. 3, 8]; days on 64 cores for Wordle [D021 p. 8]. Before 2000 the reverse holds: hardness is accepted and answered with relaxations [S185 pp. 49–50], and scarce computation argues for a priori routes [S025 p. 17].

**M3 · The price of X**, in early forms: simplicity against re-optimization [S038 p. 8]; travel against waiting with one knob [S032 pp. 15–16]; unbiased service, whose price can be unbounded [S091 pp. 23–25]; an arrival cap at airports with a knee [S135 p. 16]; per-class stockout targets [S147 p. 9].

**M4 · Certificate and duel.** Certificates are analytic bounds, and incumbents are dueled: Boxma's routing table [S293 pp. 28–31], Harrison–Wein policies certified against the bound [S072 pp. 27–31], DAR [S368 pp. 12–14], dispatch rules and the shifting bottleneck [S205 pp. 37–41], bid-price control [S034 pp. 14–21], tree search at matched budgets [S197 pp. 8–12]. Wordle carries a true certificate [D021 pp. 6–7]. ⚠ Say–do: "usually optimal" rests on restarts [S038 p. 11]; a discretization stopped at a 5% improvement is called optimal [S098 preprint pp. 1, 19]; a gap to uncertified extremals is labelled suboptimality [S681 pp. 23, 25].

**M5 · The owner's rule.** Practitioners' rules are the baselines in finance and revenue management [S009 pp. 3–4; S034 p. 2; S077 p. 17], and airport data come from the authority, DOT and NOAA [S135 pp. 7–8, 11–12]. ⚠ In 1988–1996 the comparator is the re-optimization ideal [S048 pp. 12–13, 160; S017 pp. 3, 12], and most SD instances are synthetic, e.g. [S142 p. 11] ([inferred] from the cards).

**M6 · Programmes.** A PYI cohort consolidated in a sole-author survey with open problems [S185 pp. 1, 4, 51]; a book decades later with a former student (dating only [B013 p. 1]).

**M7 · Bound before policy**, strongest here. Bound every policy [S016 p. 3; S185 pp. 8–12]; read the policy off it [S051 pp. 7–9; S293 pp. 23–26; S205 pp. 9–11]; prove the ratio [S016 pp. 5–11; S130 p. 4]; audit tightness [S091 pp. 25–27; S293 p. 27]; grade incumbents by the same bound [S072 pp. 26–31; S368 p. 13]; strengthen by order or PSD constraints [S185 pp. 22–24, 44–45]. ⚠ Whittle's index is named but never run, in 2000 or in 2026 [S051 pp. 3, 10; S681 pp. 23–25].

**The domain's own moves** (more in the [technique catalog](../technique-catalog.md), §§1.2–1.3, 1.6):
- *Proof devices*: busy-period decomposition plus one pairwise interchange for conservation laws [S057 pp. 23–24, 28–29]; potential functions on the uniformized chain [S072 pp. 8–16]; a homogeneous LP with only the zero solution for stability, and a periodic counterexample for the converse [S181 pp. 5–7]; the rare-event exponent as the value of a control problem, whose optimizer is the most likely path [S140 pp. 16–18; S187 pp. 9–12]; a closure calculus over acyclic networks [S819 pp. 8–10]; Steele's subadditivity with always-present representatives [S038 pp. 13–14]; Crofton's method [S195 preprint pp. 6–7]; a dependency-graph CLT after conditioning [S126 pp. 4–6].
- *Algorithm design*: a schedule tracking the fluid optimum [S205 pp. 9–11]; opportunity cost as a difference of two LP values [S034 p. 8]; one Lagrange multiplier by bisection to decouple a bandit [S106 pp. 7–9]; single-auction values as IP coefficients [S077 pp. 23–24]; forward memoized DP with valid bounds [D021 pp. 6–7].
- *Experiment protocol*: simulate only where proofs fail, with batch means and a confidence-interval stopping rule [S016 p. 12]; efficiency as lower bound over best policy, with the overestimate admitted [S072 p. 26]; common random numbers, exact DP where it can be computed, LP and perfect-information ceilings [S034 pp. 14, 16, 21]; a multiplicity sweep against the fluid bound [S207 pp. 12–16]; a scale test before trusting small n [S048 pp. 121–123]; per-step run times for queueing algorithms [S168 p. 15; S291 p. 13].
- *Writing*: the field-contrast opening [S185 pp. 1–3]; looseness and conjectures printed beside theorems [S016 pp. 7, 9; S032 p. 16]; a complexity map and numbered open problems [S185 pp. 49–51]; bounds and policies in companion papers [S072 p. 2; S098 preprint p. 2]; claims graded by their evidence [S017 p. 12].

## 4. Taste: what he picks and what he refuses

- **Picks problems** where a practitioner's chore meets a probability model: daily re-solving [S048 p. 12], waiting rather than distance [S016 pp. 1–2], an undefined legal standard [S009 p. 3], a named defect of the industry's control [S034 p. 4].
- **Picks models** that stay analysable: dense Coxian classes, because exponential service "seldom holds in practice" [S239 p. 2]; a deterministic fluid core first [S098 preprint p. 2]; asymptotic regimes for sharp constants [S130 p. 4]; "Heavy traffic, then, is nothing more than solving the equations that describe the system asymptotically." [S280 p. 1].
- **Picks baselines**: a bound over all policies (1989–2000); the re-optimization ideal (a priori line); the practitioners' rule (finance, revenue management, auctions).
- **Refuses**: game theory for bidding, "an optimization, as opposed to a game theoretic approach" [S077 p. 4]; linear backorder costs, which "serve analytical tractability rather than an accurate representation of reality" [S147 p. 2]; the expected-utility transaction-cost literature as intractable [S009 pp. 41–42]; stochastic-programming routing, set aside rather than attacked [S038 p. 5; S017 p. 3]; deep networks, for trees that use the structure [S681 p. 13]. Brownian heavy-traffic models are praised but judged less successful for open networks [S072 p. 4].
- **A refusal reversed**: in 1993 rolling-horizon procedures were "inherently ad hoc" for strategic planning [S032 p. 2]; in 2017 his group's re-solved deterministic MIO beats tree search as instances grow [S197 pp. 9–10] (a shift of purpose, from insight to control; [inferred]).
- **Declines** [inferred from the cards]: field tests (one self-test by an author [S077 p. 33]; an FAA comparison planned, not done [S120 p. 13]); testing network policies read off achievable-region relaxations (none in 1995 [S185 p. 49]; two proposed in 1999, untested [H010 pp. 26–28]), while fluid relaxations do yield network policies [S098 preprint pp. 20–24; S402 pp. 9–10]; running Whittle's index.

## 5. Critiques, failures and limits on record

- **Robust queueing** (note 05 §4.5). Whitt and You (2018, 2019, 2021) found the sets hard to choose and to tie to the real queue, and judged the first robust network analyzer far worse in their comparison; Goldberg and Li (2017) found the bounds do not scale in the Halfin–Whitt regime. No reply was found. His own paper claims exact performance analysis [S119 p. 4] while matching rests on regression calibration [S119 pp. 45–47]; transient errors reach 30% for heavy-tailed 20-server queues [S268 p. 21].
- **Dynamic routing**: 251 citation contexts, none a substantive critique (note 05 §6). Achievable region and large deviations: not checked (note 05, Gaps).
- **Execution costs**: limits stated up front (note 05 §5.3); note 05's "permanent impact only" is wrong, since the LPT law makes impact temporary [S009 pp. 20–22] (C18).
- **Published correction**: to the 1996 fluid-stability paper, IEEE TAC 1997 [D005]; its content was not read (note 03).
- **Failures printed in his papers**: heuristics from relaxations "somewhat ad hoc" [S185 p. 49]; 62% efficiency in heavy balanced traffic [S072 p. 31]; network delay approximations "at least partly discouraging" [S659 p. 13]; field validation "of limited usefulness" [S135 p. 12]; the fluid algorithm losing at low multiplicity [S207 p. 1]; a heavy-traffic bound "partly heuristic" [S261 p. 30]; a gap found by Majewski in an earlier version [S187 p. 26]; PMP extremals not certifiable [S681 p. 9]; the thesis's broken O(1) hinge (§2).
- **Headline against body** (Tension T6): a characterization promised, sufficiency proved [S057 pp. 1, 4, 20–21]; "hundreds of classes" against a largest network of nine [S098 preprint pp. 29–33]; "within 1%" only from 500 jobs per type [S130 pp. 1, 13].
- **Abandoned**: the Bertsimas–Xu polling paper stayed a working paper [S293] (note 01 §3); a generalized restless-bandit manuscript listed as submitted in 2017 is absent from the 2025 CV (note 01 §3); the channel-coding pillar of robust probability is still listed as submitted, with no public version (note 06 T8).

## 6. Cross-team interfaces

team.json lists no repository team for SD, so the domain is the lead's own ground. No guest member's card cites an SD work of his, and none of his SD-primary cards cites a guest member (all searched for the guests' surnames). The guests appear only as CP, RO or stochastic-programming contacts: the SD-secondary S150 lists Delage and Ye among data-driven DRO work [S150 pp. 2–3, 5], and cards outside the pack whose own tags include SD credit Nesterov [S018 p. 7], cite the 1998 Bertsimas–Ye chapter [S007 pp. 33, 35] or Delage and Ye [S013 pp. 4–5; S113 p. 4], and use data posted by Linderoth, Shapiro and Wright [S131 p. 31] (whether this Wright is the guest is not on the card). So every meeting point below is a **contrast of published methods, not an exchange in print**. The LP team's member (Huangfu, simplex software) has no SD work on record. Curtis's stochastic SQP and operating-room DRO and Grossmann's stochastic programming belong to stochastic approximation, RO and the stochastic-programming tradition, which the council does not voice as SD. Grossmann's and Sahinidis's deep-RL production scheduling (2020) and OR-Gym are on record but uncarded and unread (ignacio-e-grossmann note 06, P61–P62), and team.json does not voice RL, so they are not taken as meeting points. The nearest members:

### 6.1 DFO team · Katya Scheinberg: learning a queueing policy
- **His position**: derive the structure, or a bound valid for every policy, before learning. The cμ rule is the LP optimum over an extended polymatroid [S057 pp. 3–4, 22]; in fluid networks a structure theorem picks a learner whose class contains the optimal policy [S402 pp. 9–10].
- **Hers**: a testbed whose optimum is known (cμ) to compare gradient estimators inside one adaptive line search, and a log-scale softmax because the parameters must diverge to reach a priority rule [katya-scheinberg card S073 pp. 3–7]. "Applying this method for optimization when the optimal policy is known helps us gain knowledge about different gradient estimators and compare their performance." [katya-scheinberg card S073 p. 3]. Correct-action rates fall from 94.4% to 58.8% as load rises [katya-scheinberg card S073 p. 9]; the two heaviest settings (ρ = 1 and 11/6, with finite buffers) lie outside the ρ < 1 condition of the cμ theorem, so agreement there is with a reference rule, not a known optimum [katya-scheinberg card S073 pp. 3–4, 8, 11]. Her lens asks for complexity guarantees under noisy oracles (katya-scheinberg SKILL.md, Roundtable Card).
- **Relation**: complement; both shape the policy class around the optimum's known structure.
- **Contested**: whether a learned policy is graded against the known optimum only, or against a bound valid for every policy where no optimum is known [inferred].
- **Deciding test**: both methods need an extension first: one softmax per server for hers, which covers one server and only hopes to reach more complex systems [katya-scheinberg card S073 pp. 3–4]; his fluid tree run as a policy in the stochastic network, which the S402 card does not report (trained on fluid solves, tested in a discretised fluid simulation [S402 pp. 11–13, 19, 25–26]). Use a network with bounds for the stochastic model (Poisson arrivals, exponential services [S072 pp. 5–6]): the Harrison–Wein two-station, three-class network [S072 pp. 27–28] (whether it is S402's criss-cross network is not on the cards), or the Rybko–Stolyar network S402 also uses [S402 pp. 14–15], bounded in 1999 [H010 p. 25] (changeover settings not on the card). Fix one budget currency (wall-clock time, or simulated transitions with fluid solves counted apart) and grade both by their gap to the achievable-region lower bound [S072 pp. 26–31].

### 6.2 NLP team · Yinyu Ye: the discounted MDP's LP
- **His position**: the performance region of a discounted MDP is the polytope of state–action frequencies, with deterministic policies at its vertices [S051 pp. 4–5]; when it is exponential (restless bandits) he relaxes it by lifted projections and reads an index off reduced costs [S051 pp. 5–9]; for decomposable MDPs, a fluid LP re-solved each period [S216 pp. 6–8].
- **Ye's**: the simplex method with Dantzig's rule, and so policy iteration, is strongly polynomial on that LP for a fixed discount, a bound proved on a stated subclass (yinyu-ye SKILL.md, "Method 3 · Settle a method practitioners trust with a sharp construction", step 3; Ye, MOR 2011, DOI 10.1287/moor.1110.0516); others showed exponential behaviour once the discount is part of the input, a case he left open on purpose (yinyu-ye SKILL.md, anatomy of the MDP paper). Ye has no paper cards.
- **Relation**: complement on one object: one bounds the exact method, the other relaxes the LP when it explodes. They co-authored in 1998, on CP (SKILL.md, Academic Lineage).
- **Contested**: nothing documented. Both sides expect exact solves to break down as coupled projects are added, since the exact LP is exponential in size [S051 pp. 2, 5, 7] [inferred].
- **Deciding test** (a calibration, since no outcome counts against either side): on S051's instances, sweep the discount from 0.2 to 0.95 [S051 p. 10] and report policy-iteration counts against Ye's fixed-discount guarantee, beside the second-order relaxation's bound gap and solve time.

### 6.3 MINLP team · Ruth Misener: optimizing over visitation frequencies
- **His position**: the same polytope serves as a performance region with a bound for every policy, and the policy is read from primal support and reduced costs [S051 pp. 4–9].
- **Hers** (with Folch, first author, and an ETH group): in transition-constrained Bayesian optimization, "the utility depends only on the visited states; not their order" [ruth-misener card S059 p. 4], so planning becomes a convex problem over the visitation polytope, not an LP, solved by Frank–Wolfe whose linearisations are MDPs solved exactly by DP, with receding-horizon re-planning [ruth-misener card S059 pp. 4–7]. The device builds directly on Mutný et al.'s Markov-chain experiment design and on convex RL [ruth-misener card S059 p. 4]. Frank–Wolfe mixtures of 10 or 25 components were no better than one, so the single-component policy is the one published [ruth-misener card S059 p. 28]. Its suboptimality bound rests on a condition (⋆) left open [ruth-misener card S059 pp. 21–22]. Her lens grades methods inside the full pipeline against audited competitors (ruth-misener SKILL.md, Roundtable Card).
- **Relation**: agreement between S051 and the visitation-polytope line her group adopted; they differ on certification. Her MDP has no M-of-N coupling (transition constraints are zero probabilities [ruth-misener card S059 p. 5]), and without coupling an LP vertex already is a deterministic policy [S051 pp. 4–5], so S051's reduced-cost step, which enforces exactly M active projects [S051 pp. 8–9], has nothing to add there [inferred].
- **Contested** [inferred]: whether the visitation-polytope optimum can certify her policy where her Proposition C.1 bound rests on the open condition (⋆) [ruth-misener card S059 pp. 21–22].
- **Deciding test**: on Knorr or Ypacarai [ruth-misener card S059 pp. 9–10], run her published policy and report, per episode, the Frank–Wolfe gap to the convex program's optimum over the polytope and the share of runs that identify the maximiser; bring in S051's reduced-cost rule, read from the same Frank–Wolfe linearisation, only if an M-of-N coupling is added [S051 pp. 8–9].

### 6.4 MINLP team · Santanu S. Dey: probabilistic analysis that explains solvers
- **His position**: probabilistic analysis of a relaxation explains practice: the Held–Karp bound converges to a constant [S229 p. 12], with the asymptotic gap estimated from published constants at "perhaps less than" 3%, against gaps often below 1% in practice [S229 pp. 1, 13]; fluid relaxations exact as jobs multiply, on every instance [S130 p. 4]. A survey he co-signed reports the set-partitioning LP asymptotically tight, which explains column generation, in the part the card assigns to Simchi-Levi's line [S025 pp. 8–9]. His group checks asymptotics by simulation [S829 pp. 13–16].
- **Dey's**: worst-case bounds "fail to explain the strong performance observed in practice", so an average-case analysis gives Branch-and-Price a quasi-polynomial tree and a small gap on random two-stage stochastic IPs [santanu-s-dey card S120 pp. 1–4]; no computation is reported, the empirical side being cited from the literature [santanu-s-dey card S120 pp. 2–3]. His lens: which solver habit is explained, against what ground truth (santanu-s-dey SKILL.md, Roundtable Card).
- **Relation**: agreement in programme.
- **Contested** [inferred]: whether a random-instance model represents practice at all: uniform points, or points from a density, for him [S229 pp. 1, 14]; i.i.d. coefficients for Dey, defended as representative through the hard regime β near 1/2, with β ≥ 1/4 imposed "For technical reasons" [santanu-s-dey card S120 p. 3]. Shared rather than contested: a check at practical sizes, which papers on both sides skip (Dey's, above; S229 runs nothing [S229 p. 13]; S130's "within 1%" starts at 500 jobs per type, for a variant with no theorem [S130 p. 13]).
- **Deciding test**: run Branch-and-Price with an exact oracle on instances from Dey's model, sweeping scenarios and dimension, and plot tree size and per-scenario gap against the predicted rates, with a stated stopping rule [S016 p. 12]. Then run it on the instances of the computational studies his paper cites as practice (its references 1, 2 and 14) [santanu-s-dey card S120 pp. 2–3] and check whether tree size and gap scale the same way. A match supports the premise both sides share; a mismatch is the result Dey's own method says to report (santanu-s-dey SKILL.md, Method 1, step 7).

### 6.5 MINLP team · Sven Leyffer: bang-bang and binary optimal control
- **His position**: the maximum principle gives the policy's structure (switching indices from adjoints [S098 preprint pp. 7–8]; a top-m rule from a per-instant LP [S681 pp. 7–8]); solutions are called extremal because sufficiency fails [S681 p. 9]; a state-feedback tree is learned offline for millisecond queries, data generation excluded from its cost [S681 pp. 23–24].
- **Leyffer's** (with Hahn and Sager): binary control as trust-region descent on control sets, with stationarity under inexact gradients and no convergence of iterates [sven-leyffer card S091 pp. 3, 26–28]; his gradient density meets the Hamiltonian, and the Competing Hamiltonian method is a special case [sven-leyffer card S091 p. 20]; a Lotka–Volterra fishing problem solves in 16.72 s [sven-leyffer card S091 p. 36]; no baseline is run, since fair comparison is hard [sven-leyffer card S091 p. 42]. His lens pushes back on discretize-first brute force (sven-leyffer SKILL.md, Roundtable Card).
- **Relation**: complement; neither certifies a global optimum.
- **Contested**: a feedback policy learned offline against an open-loop control with a stationarity guarantee [inferred].
- **Deciding test**: set descent cannot yet take constraints [sven-leyffer card S091 p. 39], so it cannot run on the fluid bandit's budget coupling Σuᵢ ≤ m as published [S681 pp. 4, 22–23]; and whether his Lotka–Volterra problem fits the fluid-bandit class, whose closed-form shooting needs each project driven by its own state and control [S681 pp. 4–5], is not on the cards. So use a single logistic fishery with a slack budget (n = 1, m ≥ 1): unconstrained binary control, inside the quadratic class [S681 pp. 5, 22–23]. From the same initial states, compute the set-descent control, the shooting extremal and the tree policy; report objective, time per query and total offline time.

## 7. Open problems

**Stated in his papers**:
- systematic policies from relaxations, bounds on the heuristic–relaxation gap, and SDP relaxations for networks [S185 p. 51]; "To the best of our knowledge, there is no systematic approach to derive policies from relaxations." [S368 p. 2];
- laws for systems with overtaking, multiserver queues and networks [S336 p. 34; S173 p. 38];
- large deviations with feedback, several traffic types and scheduling [S177 p. 40]; more than two streams [S187 p. 26];
- necessity of the stability condition beyond two stations, and the fluid–stochastic equivalence [S181 p. 13]; removing the square in the heavy-traffic order [S123 p. 29];
- the routing constant gap, which "probably requires a new approach" [S597 p. 39]; partitioning conjectures and networks instead of the plane [S032 p. 16];
- provably near-optimal dynamic polling policies [S293 p. 37]; an optimal algorithm for the fluid problem [S098 preprint p. 33]; the job-shop additive constant [S205 pp. 27, 41];
- a CLT for the optimal TSP, MST and matching [S829 pp. 2–3; S126 p. 5];
- general fluid MDPs and adaptive parameters [S681 p. 27]; Wordle beyond six rounds [D021 p. 8].

**Inferred**:
- grade Whittle's index against the LP bound;
- certify the learned fluid policies in the stochastic network with an achievable-region bound;
- calibrate robust queueing sets without simulation (the critics' challenge).

## 8. Reading path

1. [S048] chapter 1 (pp. 10–22): the a priori framing and its two criteria.
2. [S038]: the framework in fifteen pages; asymptotics and heuristics.
3. [S016]: bound all policies first; simulate only where proofs fail.
4. [S091]: the bound as a convex program over densities, and a tightness audit.
5. [S580], then [S185]: the programme stated, then the survey with its complexity map and open problems.
6. [S057]: conservation laws to Gittins indices by LP duality; start with the two-armed example (pp. 5–8).
7. [S072]: potential-function relaxations for networks and the efficiency tables.
8. [S051]: the restless-bandit hierarchy and the primal–dual index.
9. [S130], then [S205]: fluid relaxations as bound and template for job shops.
10. [S140]: large deviations as optimal control.
11. [S009]: a dynamic program with structure kept, and the rule practice uses.
12. [S681]: the 2026 return, with honest labels on certification.

## 9. Coverage and gaps

- **Read**: 54 of 99 primary works in full and 12 in part, from the 172-page thesis to the 2026 paper; partial reads skipped proofs [S123; S140; S173; S177; S187; S205; S212; S216; S322; S336; H010]. Synthesis: [08](../research/08-deep-reading-synthesis.md) §§4–7.
- **Thin**: much of the 1992–2000 queueing-network series is abstract- or metadata-level: the achievable-region programme [S587; S468; S507; S581], large deviations [S656], Lyapunov performance bounds [D007; D008] and the fluid job shop [S798]; so are the Ek/C2/s paper [S329], the fluid tandem and parallel-processor works [S571; S796] and the 2022 book [S334], whose open part is a five-line structure [B013 p. 1]. The 1997 correction is metadata only [D005]. The 223-page large-deviations text, students' theses (van Ryzin, Ricard, Paschalidis, Sethuraman, Chi, Mersereau) and the 1997 talk have no card.
- **Not searched**: critiques of the achievable region and large deviations (note 05, Gaps); why he left queueing (the 2021 interview's chapter on queueing theory was not read, note 02).
- **Next round**: citation contexts for the 1994–1996 network and bandit papers; the book's contents and preface; the theses of Paschalidis and Sethuraman; the correction's text; the interview chapter.

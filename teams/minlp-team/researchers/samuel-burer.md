# Samuel Burer · MINLP Team 研究者档案

> 档案依据：本人署名的 7 条语料 [MINLP-S2][MINLP-S57][MINLP-S58][MINLP-S60]
> [MINLP-S61][MINLP-S62][MINLP-S63]，层级均为 verified-web（核实 2026-10-10），
> **全部读过全文**。版本说明：S2、S57、S58、S60、S62 读的是作者主页托管的出版版；
> S61 读的是 2012-11-16 最终修订稿（锚点用修订稿页码，SIAM 出版版页码未核对）；
> S63 读的是作者主页 2010-04 版（锚点用该版页码，与出版章节 pp. 373–405 未逐页对应）。
> 「张力」一节用到的他人条目中，[MINLP-S64] **只读了摘要**，
> [MINLP-S38][MINLP-S40] 只读了出版社免费首页（partial），引用时按此降级。
> 身份信息据本人主页与 Google Scholar 页（2026-10-10 核实）。不使用 product/ 管线的文件。
> 所有问题一律写成最小化形式；原文为最大化者（S58）已取负改写。

## 身份速览（verified-web）

- 来源：verified-web，核实 2026-10-10，https://sburer.github.io/（页脚「Last updated
  2026-03-20」）；verified-web，核实 2026-10-10，
  https://scholar.google.com/citations?user=BScCde0AAAAJ&hl=en 。
- 职位（主页）：University of Iowa，Tippie College of Business，Department of Business
  Analytics 的 **Tippie Rollins Professor**，兼系主任（Chair / Departmental Executive
  Officer）。Scholar 页写作「Professor of Business Analytics, University of Iowa」，
  邮箱域 uiowa.edu 已验证；研究兴趣列为 Optimization、Mathematical Programming、
  Mathematical Optimization、Operations Research。两页一致，Scholar 页的头衔写得较简。
- 学历（主页）：Georgia Tech 博士。
- 奖项与资助（主页所列）：INFORMS Computing Paper Prize、SIAM Optimization Test of Time
  Award、NSF CAREER award；University of Iowa President and Provost Award for Teaching
  Excellence。**主页未说明哪篇论文获哪个奖，本档案不作对应。**
- 编辑职务（主页）：Operations Research 领域编辑（area editor）、Mathematical
  Programming 副编辑（associate editor）。
- 主页自述方向：数学优化，为运筹学等领域中的难问题发展理论与算法。
- 以上头衔、职务、奖项均为快照（主页最后更新 2026-03-20），会过时。

## 核心贡献

### A. 完全正（copositive）表示：把全部困难压进一个锥 [MINLP-S57]
Burer (2009), "On the copositive representation of binary and continuous nonconvex
quadratic programs"（全文，出版版）。
- **主定理（proved-in-source，Thm 2.6, p. 484）**：问题 (P) min xᵀQx + 2cᵀx，
  s.t. a_iᵀx = b_i，x ≥ 0，x_j ∈ {0,1}（j ∈ B）。构造完全正规划 (C)：目标线性化为
  Q•X + 2cᵀx，保留 a_iᵀx = b_i，加「平方」约束 a_iᵀXa_i = b_i²，对 j ∈ B 加 x_j = X_jj，
  并要求 [1 xᵀ; x X] 属于完全正锥。则 opt(C) = opt(P)，且 (C) 的最优 x* 落在 (P)
  最优解集的凸包内。
  假设：Feas(P) 非空；线性约束全部写成等式且 x ≥ 0；key assumption (1)（p. 481）只要求
  在线性部分 L 上蕴含 0 ≤ x_j ≤ 1（j ∈ B）。**整个可行域有界不是 Thm 2.6 的前提**，
  有界性只用于 Cor 2.5 那条更强的集合等式（pp. 482–484）。
- **互补约束扩展（proved-in-source，Thm 3.2, p. 489）**：加互补约束 x_j x_k = 0 时，只需在
  (C) 中加线性约束 Σ X_jk = 0，前提是相关连续变量在 L 上有界。如何纳入一般二次约束，
  列为开放问题（§4.4, §6, p. 494）。
- **计算立场（stated-position，§5, pp. 493–494）**：(C) 是凸的，但与 (P) 等价，所以本身
  NP-hard。可计算的松弛来自两条可以组合的路线：用 DNN 等可表示锥从外部逼近完全正锥；
  在 (x, X) 空间加有效线性约束。原话：
  "So the results of this paper are not a “magic bullet” for solving NP-hard problems."
  （§5, p. 493）锥逼近层级及其误差界为引用结果（cited）。

### B. 有限分支定界：KKT 互补分支 + SDP 松弛 [MINLP-S58]
Burer, Vandenbussche (2008), "A finite branch-and-bound algorithm for nonconvex quadratic
programming via semidefinite relaxations"（全文，出版版）。
- 问题（改写为最小化）：min −½xᵀQx − cᵀx s.t. Ax ≤ b，x ≥ 0（原文为 max）。用一阶 KKT
  条件把它写成带互补约束的 LP（Prop 2.1, p. 263）。B&B 在每个互补对的两侧之间二选一分支，
  到叶节点时全部互补都已固定，所以分支次数有限。
- **Thm 3.3（proved-in-source，p. 270）**：采用 KKT 分支与 (SDP1) 型松弛的 B&B 正确且有限。
  假设：可行域 P 有界（Assumption 2.4）且有内点（Assumption 2.5，p. 265）；结论针对精确
  算术，另有 bit 模型下的论证；有界性依赖把 SDP 目标与 KKT 目标等同的约束 (3)。
- **为什么必须用 SDP（proved-in-source，Cor 2.3 p. 265；Prop 3.1–3.2 p. 268）**：丢掉互补
  得到的 LP 松弛是无界的；(SDP1) 的可行集有界，且若其最优解给出 KKT 点，该点就是全局最优。
  摘要原话："However, the LP relaxations are unbounded, a fact that precludes their use.
  In this paper, we propose and study semidefinite programming relaxations, which are
  bounded and hence suitable for use with finite KKT-branching."（abstract，Springer 落地页）
- **计算（empirical，§5.2, pp. 275–281）**：所需节点很少，1% 容差下多数实例在根节点就解完。
  更强的 (SDP2) 节点更少，但 "For all instances tested, runs with (SDP1) outperform those
  with (SDP2) in terms of CPU time."（p. 276）瓶颈是 SDP 求解（用 Burer–Vandenbussche 的
  增广拉格朗日法），CPU 时间从几秒到数天不等。作者提醒：只需要好的局部解时，应改用更快的
  非全局方法（§1, p. 262）。注意：实现为提速去掉了约束 (3)，叶节点改用 LP 松弛（§5.1），
  与 Thm 3.3 的理论版本不完全相同。

### C. 低维凸包与精确性边界 [MINLP-S60][MINLP-S61]
- **Anstreicher, Burer (2010) [MINLP-S60]**（全文，出版版）。研究对象是
  C = conv{(1;x)(1;x)ᵀ : x ∈ F}（含对角项 X_ii = x_i²）。
  - 单纯形（proved-in-source，Thm 1, p. 36）：F 为标准单纯形且 n ≤ 4 时，C 等于其 DNN 表示。
    证明依赖「n ≤ 4 时 DNN = CP」等引用结果（cited）。摘要原话："We show that if n ≤ 4 and
    F is a simplex, then C has a computable representation in terms of matrices X that are
    doubly nonnegative (positive semidefinite and componentwise nonnegative)."（abstract, p. 33）
  - 盒（proved-in-source，Thm 2, p. 38）：F = [0,1]ⁿ 时 C ⊆ PSD ∩ RLT，且 n = 2 时两者相等。
    证明借道 DNN = CP 与 [MINLP-S57] 的 CP 表示。n = 3 时不成立：作者给出一个 box-QP 反例，
    真值 −2/3，PSD ∩ RLT 松弛给 −3/4（松弛值为数值求解结果，p. 39）。
  - 3-立方体（proved-in-source，Thm 3, p. 40）：把立方体剖分成 6 个四面体，得到「每片一个
    DNN 矩阵」的精确析取表示。不加额外变量、直接在 Y 空间完全刻画 n = 3 的 C，列为开放问题（§4）。
- **Burer, Anstreicher (2013) [MINLP-S61]**（全文，修订稿）。研究信赖域子问题
  min{xᵀQx + cᵀx : ‖x‖ ≤ 1} 加上额外线性约束的情形。
  - SOC-RLT 约束：把线性约束与球约束相乘，再以 X = xxᵀ 线性化。
  - 精确性（proved-in-source）：加一条割时，SDP + 一条 SOC-RLT 精确（Thm 1/Cor 1, pp. 6–7，
    重新证明了 Sturm–Zhang 的结果）；加两条平行割时，SDP + RLT + 两条 SOC-RLT 精确
    （Thm 2/Cor 2, pp. 11–12，新结果）。摘要原话："When two parallel cuts are added to TRS,
    we show that the resulting nonconvex problem has an exact representation as a semidefinite
    program with additional linear and second-order-cone (SOC) constraints."（abstract，Crossref 记录）
  - 失效边界：两条一般割在球内相交时不精确，有 n = 3 反例（相对 gap 约 7%）。两割不相交时
    **只是猜想**（n ≤ 10 的随机实例都相等，未证明，§4, p. 13）。
  - 双信赖域 TTRS：半无限族 SOC-RLT 松弛 r⁺ 可以在 n 与 log(1/ε) 的多项式时间内 ε-计算
    （Cor 3, p. 15，经椭球法的分离–优化等价）。但它并非总是精确（同心双球 n = 2 例，§5.2），
    TTRS 本身的复杂度仍是开放问题。
  - 作者判断（stated-position，§1, p. 3）：扩展信赖域问题的复杂度高度依赖可行域的几何。

### D. MIQCP 松弛综述：「MILP 之路」[MINLP-S63]
Burer, Saxena (2012), "The MILP Road to MIQCP"，收于 Lee–Leyffer 编的 IMA 卷
[MINLP-S6]（全文，2010-04 作者版）。
- **框架（stated-position，abstract；Prop 2.2 p. 5；Prop 2.3 p. 7）**：MIQCP 写作
  min xᵀCx + cᵀx，带二次约束、变量界、部分整数变量。提升 X = xxᵀ 后，问题等价于在
  clconv F̂ 上最小化线性目标；基础松弛 L 逐步加强为 L ∩ RLT ∩ R2 ∩ S2 ∩ PSD。摘要原话：
  "These methods can be viewed as generalizations of techiniques for mixed-integer linear
  programming."（abstract；"techiniques" 为原文拼写）
- **MILP ↔ MIQCP 对应**：Balas 序贯凸化（Thm 3.4）对应逐个施加原子非凸条件 X_ii ≤ x_i² 的
  序贯凸化（Thm 3.5，cited，要求可行域有界且无整数变量）；差别在于，单个原子条件对应的
  子问题在 MIQCP 中可能已经 NP-hard（pp. 16–17）。lift-and-project/析取割对应由 X̂ − x̂x̂ᵀ
  的特征向量导出的 univariate 析取加 CGLP（§4.1, pp. 18–20），结论节把它类比为 MILP 中的
  split 割。
- **精确性目录（§2.5）**：盒当且仅当 n ≤ 2（Thm 2.1，cited [MINLP-S60]）；单纯形
  n ≤ 4（Thm 2.5，cited）；半椭球对任意 n 精确（Thm 2.6，cited Sturm–Zhang）。综述内的新证明
  （proved-in-source）：非负象限 n ≤ 3 时等号成立（Thm 2.4, pp. 9–10）；有界二次型集合的
  L ∩ PSD 等于 conv F 加上 L ∩ PSD 的回收锥（Thm 2.7, p. 11）。
- **计算证据（cited-by-source，§4.2 Table 1, pp. 22–24，转述 Saxena–Bonami–Lee
  [MINLP-S66]）**：在 GLOBALLib 上，加入析取割的松弛 "close more than 98% of the duality
  gap on 67 out of 129 instances"（p. 23）；去掉 PSD、只留析取割，会显著变弱。综述自己的小实验
  （§5，9 个 box-QP 实例）：通用内点 SDP 求解器在每个实例上都不如专用 CP 求解器和投影割平面法
  （empirical）。

### E. 非凸 MINLP 综述 [MINLP-S2]
Burer, Letchford (2012), "Non-convex mixed-integer nonlinear programming: A survey"（全文）。
- **分类（definition，§3–§5, pp. 98–103）**：共享概念有欠/过估计与凸包络、可分性、因式分解、
  标准分支与空间分支；一般情形的算法有空间 B&B、branch-and-reduce、αBB、转换为 MILP；
  二次/多项式结构下有 RLT、SDP、多面体与凸分析、MIQCQP 割平面、多项式推广。问题形式为
  min f⁰(x,y)（§1, p. 97）。
- **不对 SDP 与 LP 作一般性排序（cited-by-source，§5.3 p. 102；§4.2 p. 100）**：只说对
  MIQP（线性约束），RLT 与 SDP 结合能支配二者单独使用，界可显著改进，但运行时间可能很高
  （引 Anstreicher）；并如实记录 branch-and-reduce 通常用 LP 松弛，理由是效率、数值稳定性
  和灵敏度信息。
- **凸与非凸（cited-by-source，§1, p. 98）**：凸 MINLP 的连续松弛是凸的，所以在理论和实践上
  都容易得多；一些简单的非凸 MINLP 可以不可判定（引 Jeroslow [MINLP-S72]），但
  "As it happens, all of the proofs that non-convex MINLPs can be undecidable involve
  instances with an unbounded feasible region."（§1, p. 98）
- **软件分类（stated-position，§6, p. 103，2012 年状态）**：能给出可证全局最优的有 BARON、
  αBB、LINDO-Global、Couenne、GloMIQO 五个；BONMIN、DICOPT、LaGO（三者本是凸 MINLP 软件）
  与 MIDACO 对非凸问题只能给启发式解。
- **研究议程（stated-position，§7, p. 104）**："Special cases can also allow the development
  of newer techniques (e.g., semidefinite relaxations), which may then progress to more
  general techniques."

### F. 大规模 SDP 求解工具：低秩分解 [MINLP-S62]
Burer, Monteiro (2003), "A nonlinear programming algorithm for solving semidefinite
programs via low-rank factorization"（全文，出版版）。本条在语料中的角色是求解 SDP 松弛的
工具，不是 MINLP 专门文献。
- **方法（definition，§2–3）**：对 min{C•X : A_i•X = b_i, X ⪰ 0}，令 X = RRᵀ，得到一个非凸
  NLP。秩取满足 r(r+1)/2 ≤ m 的最大 r 时，它与 SDP 等价（依据 Barvinok–Pataki 秩界，
  Thm 1，cited）。用增广拉格朗日法加有限内存 BFGS 求解，函数值与梯度的计算量与数据矩阵的
  非零元个数成正比（Props 5–7, pp. 339–340）。
- **最优性证书（proved-in-source，Prop 3, p. 335）**：若驻点 R* 对应的 S* ⪰ 0，则
  X* = R*R*ᵀ 与 (S*, y*) 分别是原始与对偶最优解。Prop 4 据此给出「逐步增秩」方案（需要
  正则性条件）。
- **可扩展性是经验结论（empirical，§4 Tables 1–7）**：在 Lovász theta 与 maxcut SDP 上，
  总时间常远少于当时的谱丛法和对偶缩放内点法，但并非逐例占优。
- **作者自述局限（stated-position，§5, p. 355）**："Although we have some theoretical
  justification that explains the observed practical convergence, we do not currently have
  a formal convergence proof." 另外，该方法是原始方法，只在极限意义下可行，其目标值不能
  直接当作有效下界（§1, §3.1）。

## 心智模型（三重验证）

### 模型 1　提升到矩阵空间，把全部非凸性压进一个锥或秩条件 ✅ 三重通过
先把二次问题提升到 (x, X) 空间（X 代表 xxᵀ），使目标和多数约束变成线性，非凸性只剩
「X = xxᵀ」或「属于完全正锥」这一条；然后研究这一条的凸包，以及能从外部逼近它的可计算锥。
- **跨域复现**（≥ 2 个不同 ID，均为 Burer 署名）：完全正表示把全部困难集中到完全正锥
  [MINLP-S57]（Thm 2.6；§5）；MIQCP 等价于在 clconv F̂ 上最小化线性目标
  [MINLP-S63]（Prop 2.2）；研究对象直接就是 conv{(1;x)(1;x)ᵀ} [MINLP-S60]（Thms 1–3）；
  SOC-RLT 约束用 X = xxᵀ 线性化 [MINLP-S61]；有限 B&B 的节点松弛是提升矩阵
  Y = (1;x)(1;x)ᵀ ⪰ 0 [MINLP-S58]（§3）。共五篇，跨四个算法/理论族。
- **生成力**：遇到一类新的非凸二次结构，此人会先问「提升后的集合
  conv{(1;x)(1;x)ᵀ : x ∈ F} 是什么？PSD、DNN、RLT、SOC-RLT 中哪个组合能从外部逼近它？
  在什么条件下恰好相等？」可检验：看他针对新问题类的论文，是否以提升矩阵的凸包为研究对象。
- **排他性**：主流全局求解器走因式分解路线：给每个非线性项引入辅助变量，在原变量空间做逐项
  McCormick 包络与多面体外逼近 [MINLP-S33][MINLP-S37][MINLP-S38]；αBB 在原空间加凸二次
  扰动 [MINLP-S49]。Burer–Letchford 自己把「因式分解」列为现有精确算法的共享概念
  [MINLP-S2]（§3）；提升到矩阵空间是与之并列的另一条路。
- **张力（如实保留）**：提升空间有 O(n²) 个 X 变量。同一路线上的 Saxena–Bonami–Lee 指出
  extended 空间的规模开销大 [MINLP-S66]（结论节）；他们的 projected 版本在预印本中用少得多的
  时间接近 extended 版本的强度 [MINLP-S67]（§5 Table 2；Lee–Grossmann 的 4 个 MIQCP 例子
  除外）。[MINLP-S63] 转述的计算证据来自 extended 版本。
- **分级**：心智模型。

### 模型 2　精确性边界：用定理划出松弛何时精确，用最小反例标出何处失效 ✅ 三重通过
对一类结构化问题，不满足于「松弛 gap 小」，而是追问「在什么维数/几何下凸松弛恰好等于
凸包」，并给出刚好越界的最小反例；证不出的情形明确标为猜想或开放问题。
- **跨域复现**：单纯形 n ≤ 4 精确、盒 n = 2 精确、n = 3 有反例 [MINLP-S60]（Thms 1–2，
  p. 39）；TRS 加一条割、两条平行割时精确，相交割有 n = 3 反例，不相交情形只记为猜想
  [MINLP-S61]（Thms 1–2；§4）；精确性目录加两条新定理（非负象限 n ≤ 3；有界二次型的
  L ∩ PSD）[MINLP-S63]（§2.5）；完全正规划对带二元变量的 QP 精确 [MINLP-S57]（Thm 2.6）。
- **生成力**：遇到「球加若干割」「单纯形/盒上的低维 QP」这类带几何结构的问题，此人会问
  「基础 SDP 加哪几条 RLT/SOC-RLT 约束后恰好精确？最小的不精确实例是几维？」，并把证不出的
  情形写成猜想，而不是宣称成立。
- **排他性**：更常见的评价方式是在基准集上报告经验性的 gap 闭合或求解时间，例如 BARON 多面体
  割的根节点 gap 缩减 [MINLP-S38]（abstract）、Misener–Floudas 用 performance profile 作比较
  [MINLP-S52]（§4）、Bao–Sahinidis–Tawarmalani 在 700 个随机实例上报告平均 gap
  [MINLP-S64]（摘要级）。注意这不是 Burer 一人独有：Wang–Kılınç-Karzan 走同一条路，并称其
  条件推广了 Burer–Ye 的 SDP 紧性条件 [MINLP-S69]（§1.2）。这是一个学派的做法，不是全领域
  的默认做法。
- **分级**：心智模型。

### 模型 3　「MILP 之路」：把 MILP 的成熟机制移植到 MIQCP ✅ 三重通过
MIQCP 的松弛与割平面，应当从 MILP 几十年的理论里找对应物（提升、有效不等式、序贯凸化、
lift-and-project/析取割、split 割），再找出类比在哪一步失效。
- **跨域复现**：综述明言其方法 "can be viewed as generalizations of techiniques for
  mixed-integer linear programming"，并逐条建立 Balas 序贯凸化与原子非凸条件序贯凸化、
  CGLP 析取割与特征向量析取之间的对应 [MINLP-S63]（abstract；Thms 3.4–3.5；§4.1）；完全正
  表示中把二元条件写成 x_j = X_jj、可为二元变量加 Padberg 类不等式、互补约束可以并入
  [MINLP-S57]（Thm 2.6；Thm 3.2；§5）；非凸 MINLP 综述把 MILP 领域的成功列为非凸 MINLP
  算法发展的关键推动 [MINLP-S2]（§7, p. 104）。另：[MINLP-S58] 在互补对两侧之间二选一分支，
  靠有限次分支得到有限终止；把它看作 0-1 分支的类比是本档案的**推断**，原文没有作此类比。
- **生成力**：面对一个新的 MIQCP 结构，此人会问「MILP 里对应的定理或割是什么？它在提升空间
  里的类比是否成立？哪一步失效（例如单个原子非凸条件的子问题本身已 NP-hard，[MINLP-S63]
  pp. 16–17）？」
- **排他性**：主流非凸求解路线以连续变量上的空间分支和域缩减为核心：branch-and-reduce
  [MINLP-S35]、Couenne 的分支与界收紧 [MINLP-S42]、SCIP 的 branch-and-cut [MINLP-S43]，
  以及 αBB [MINLP-S49]。这些方法的骨架来自全局优化，而不是 MILP 的割平面理论。
- **分级**：心智模型。

### 模型 4　松弛够紧，就为它造专用求解器，而不是退回 LP ✅ 三重通过
当 SDP/DNN 一类松弛够紧、但通用内点法太慢时，此人的做法是设计利用结构的求解器（低秩分解、
增广拉格朗日、割平面式投影），并在强弱两档松弛之间按 CPU 时间取舍，而不是整体换成更弱的
多面体松弛。
- **跨域复现**：用低秩分解把大规模 SDP 变成 NLP 来解 [MINLP-S62]（§2–4）；在有限 B&B 中用
  Burer–Vandenbussche 增广拉格朗日法解节点 SDP，实验中选了更便宜的 (SDP1)
  [MINLP-S58]（§5.2, p. 276）；MIQCP 综述的小实验里，专用 CP 求解器与投影割平面法在每个
  实例上都胜过通用内点 SDP 求解器 [MINLP-S63]（§5）。
- **生成力**：给他一个界很紧、但通用 SDP 求解器跑不动的松弛，此人会问「它的结构（低秩最优解、
  稀疏数据、可分离的割）能不能让一阶或低秩方法把它解快？」，而不会先问「哪个 LP 松弛
  足够接近」。
- **排他性**：BARON 学派明确选择多面体松弛，理由是 LP 求解器更快、更可靠，并承认多面体松弛的
  gap 更大 [MINLP-S38]（abstract；§1）[MINLP-S40]（§1）；Dey 等用 SOCP 或稀疏 LP 割**替代**
  SDP [MINLP-S74][MINLP-S78]。注意 [MINLP-S2] 本身没有对 SDP 与 LP 作一般性的优劣排序
  （§5.3），所以这里的排他性指的是**研究投入的方向**，不是 Burer 宣称 SDP 一定更好。
- **内部矛盾（本质性张力，如实保留）**：速度与证书不可兼得。低秩方法没有形式化的收敛证明，
  其目标值也不能直接当作有效下界 [MINLP-S62]（§5；§1, §3.1）；全局 SDP-B&B 的 CPU 时间可达
  数天，作者自己建议只需局部解时改用非全局方法 [MINLP-S58]（§1, §5.2）。
- **分级**：心智模型。

### 工作信条（未全过三重验证，按标准降级）

- **等价表示 ≠ 可解**：完全正规划虽然是凸的，但本身 NP-hard，"not a “magic bullet”"
  [MINLP-S57]（§5）；r⁺(TTRS) 可多项式时间 ε-计算，但 TTRS 本身的复杂度开放，且复杂度取决于
  可行域几何 [MINLP-S61]（Cor 3；§1）；低秩等价不附带全局收敛证明 [MINLP-S62]（§5）。
  跨域 ✔，生成力 ✔（「这个精确表示所用的锥、它的分离问题本身难不难？」），**排他性 ✘**：
  Dey 同样强调凸包 SOC 可表示不等于多项式规模 [MINLP-S79]（§2），Liberti 强调可判定不等于
  易解 [MINLP-S9]（§3.5.1）。这是领域共识，**未全过三重验证**，降级为工作信条。
- **特殊情形先行**：明言 "Special cases can also allow the development of newer techniques
  (e.g., semidefinite relaxations), which may then progress to more general techniques."
  [MINLP-S2]（§7）。实践证据（低维凸包、TRS 加割）与模型 2 是同一批论文，不重复计数，所以
  跨域一项不单独成立；生成力 ✔；排他性只部分成立（对照通用求解器开发 [MINLP-S36][MINLP-S43]
  [MINLP-S54]，但同一段他也承认通用算法必不可少）。**未全过三重验证**，降级为工作信条。

## 与其他成员的分歧与张力

以下都是语料中可见的**方法对照**。除第 4 条外，语料中没有成员之间直接交锋的记录；标「推断」
的条目，是本档案根据各自论文的立场作出的对比。

1. **Sahinidis：多面体（LP）松弛 vs 锥（SDP/CP/DNN）松弛**（推断）。
   - Sahinidis 一方：把凸松弛外逼近成多面体、在节点上解 LP，理由是 LP 求解器更快更可靠，并
     承认多面体松弛 gap 更大 [MINLP-S38]（abstract；§1）；后来在 BARON 中把凸非线性松弛与
     多面体松弛结合并学习切换 [MINLP-S40]（abstract），但这里的非线性松弛不是 SDP。
     Bao–Sahinidis–Tawarmalani 的摘要显示：最强的两种 SDP 松弛（DNN 与「Shor + 部分 RLT」，
     二者等价）计算时间比弱松弛高约三个数量级，平均 gap 约 3%，弱松弛最高约 19%
     [MINLP-S64]（摘要级）。
   - Burer 一方：在 KKT 分支框架里，LP 松弛无界、根本不能用，必须用有界的 SDP 松弛
     [MINLP-S58]（Cor 2.3；Prop 3.1）；MIQCP 中去掉 PSD 会显著削弱析取割
     [MINLP-S63]（§4.2，转述 [MINLP-S66]）。
   - 共识部分：Burer–Letchford 如实记录 branch-and-reduce 用 LP 的理由，也承认 RLT+SDP 组合的
     运行时间可能很高 [MINLP-S2]（§4.2；§5.3）。分歧不在「SDP 是否更紧、是否更贵」，而在
     **怎样应对代价**：Sahinidis 学派退到 LP，Burer 造专用 SDP 求解器（模型 4）。
   - 交汇点（推断）：[MINLP-S57] 中完全正锥最低一层的外逼近就是 DNN 锥；[MINLP-S64] 摘要评为
     最强之一的 "doubly nonnegative relaxation" 属于同一类对象，但该摘要没有注明出处。

2. **Dey：SOC/LP 作为 SDP 的替代 vs SOC 作为 SDP 的加强**（推断）。
   - Dey 一方：ACOPF 上的强化 SOCP 松弛下界与 SDP 极接近、与 SDP 互不支配，且快约一个数量级
     [MINLP-S74]（§6；Props 4.5、4.8）；用稀疏 PCA 生成的 LP 割，在至多 100 个变量的实例上
     倾向于闭合初始 LP 与 SDP 之间 90% 以上的 gap [MINLP-S78]（§7）。
   - Burer 一方：SOC-RLT 是**加在 SDP 之上**的约束，用来关闭 SDP 剩下的 gap [MINLP-S61]。
   - 低维凸包的两种视角：Anstreicher–Burer 在提升空间刻画 conv{(1;x)(1;x)ᵀ}，盒上只到 n = 2
     [MINLP-S60]；Santana–Dey 在原空间证明单个二次等式与多胞形之交的凸包对任意 n 都是 SOC
     可表示的，但构造可能需要指数多个变量 [MINLP-S79]（Thm 1；§2）。两边都承认「可表示 ≠
     可高效求解」（见工作信条第一条）。
   - 复杂度（互补，不是分歧）：Burer–Letchford 指出所有不可判定性证明都用到无界可行域
     [MINLP-S2]（§1）；Del Pia–Dey–Molinaro 证明，恰好一个二次不等式的 MIQP 判定版本属于 NP，
     且**不要求多面体有界** [MINLP-S73]（Thm 1）。可判定性与多项式证书还取决于二次约束的个数
     （见 [MINLP-S73] §1.1 引用的反例）。

3. **Misener：分段线性 MILP + 低维 edge-concave 刻面 vs 提升空间的低维凸包**（推断）。
   - 两边都认为低维凸包可以精确计算：Misener–Floudas 在 B&B 每个节点对 n ≤ 3 的
     edge-concave 聚合加入凸包刻面 [MINLP-S52]（§3.1.1）；Anstreicher–Burer 证明 n ≤ 2（盒）
     与 n ≤ 4（单纯形）的提升凸包可以计算 [MINLP-S60]。
   - 不同处：Misener 在原变量空间处理项的聚合，并用分段线性 MILP 离散化来补足
     [MINLP-S52][MINLP-S55]；Burer 的对象是含对角项 X_ii 的整个提升矩阵。Misener–Floudas 还
     指出，pooling 的品质平衡约束是 sum decomposable，逐方程的聚合割无法再收紧，应改用 RLT、
     专门设计的割或分段线性松弛 [MINLP-S52]（§3.1.3）。这一点对提升空间方法是否同样成立，
     语料中没有证据。
   - 「MILP」一词的两种用法：Burer–Saxena 的 "MILP road" 指移植 MILP 的**割平面理论**
     [MINLP-S63]；Misener 与 Dey–Gupte 的 MILP 指对非凸问题本身做**离散化或 restriction**
     [MINLP-S52][MINLP-S76]。Burer–Letchford 把「转换为 MILP」列为一般情形的一类精确方法
     [MINLP-S2]（§4.4）。

4. **Grossmann / Leyffer：凸 MINLP 机制在非凸问题上的定位**（有文献依据，但不是交锋）。
   Burer–Letchford 把 BONMIN、DICOPT、LaGO 归为凸 MINLP 软件，指出它们对非凸 MINLP 只能给
   启发式解 [MINLP-S2]（§6），并说明有时可以把凸 MINLP 的精确算法改造成非凸问题的启发式
   （§4.6）。对照 OA [MINLP-S12][MINLP-S13] 与 BONMIN 框架 [MINLP-S22]：它们的全局性保证
   依赖凸性，而 Burer 的工作全部在非凸一侧。Leyffer 等的 branch-and-refine（分段线性欠/过
   估计）被该综述归入「转换为 MILP」一类（§4.4）。另：[MINLP-S63] 收录于 Lee–Leyffer 编的
   IMA 卷 [MINLP-S6]。

5. **αBB vs 因式分解**：Burer–Letchford 只作中性描述：αBB 不需要因式分解，但需要一般凸规划
   求解器 [MINLP-S2]（§4.3）。Burer 本人在这一对立中没有表态，不列为分歧。

## 边界

- **语料覆盖**：只覆盖 7 篇署名论文（2003–2013）。语料中没有 2013 年以后的 Burer 论文，
  不能据此推断他近年的研究方向。
- **只在他人条目中二手出现的工作**：Burer–Ye 关于 diagonal QCQP 的 SDP 紧性条件，只经
  [MINLP-S69]（§1.2）转述；Burer–Vandenbussche 的增广拉格朗日 SDP 求解器，只在 [MINLP-S58]
  §5 中作为工具出现。二者都不在语料中，不能单独引用。
- **开放问题的后续未覆盖**：[MINLP-S57] 列为开放的「一般二次约束如何纳入 CP 表示」、
  [MINLP-S60] 的 3-立方体 Y 空间刻画、[MINLP-S61] 的相交割与 TTRS 复杂度，后来是否解决，
  语料不覆盖。
- **版本与页码**：[MINLP-S63] 的锚点是 2010-04 作者版页码；[MINLP-S61] 的锚点是 2012-11-16
  修订稿页码；[MINLP-S58] 的实现版本与 Thm 3.3 的理论版本不同（去掉了约束 (3)），引用其计算
  结果时须说明这一点。
- **对照证据的读取深度**：[MINLP-S64] 只读了摘要，
  [MINLP-S38][MINLP-S40] 只读了首页预览，所以「张力」第 1 条中关于 Sahinidis 学派的部分只到
  摘要/引言层面。[MINLP-S64] 已核实的是 **SDP 松弛之间**的比较，不是 SDP 与多面体松弛的比较。
- **数值**：文中百分比与反例值都是原文报告的实验或数值求解结果（多基于特定硬件、容差与
  2003–2013 年的软件），不是定理常数；需要具体数字时回原文核对。
- **快照**：头衔、系主任职务、编辑职务与奖项来自主页快照（最后更新 2026-03-20，核实
  2026-10-10）；主页没有写各奖项对应哪篇论文，本档案不作对应。Scholar 引用数未入档。
- **不在本队章程内**：他的教学、商业分析项目，以及与 MINLP 无关的工作，不展开。

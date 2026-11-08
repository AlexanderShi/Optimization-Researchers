# Santanu S. Dey · MINLP Team 研究者档案

> 档案依据：语料中由 Dey 署名的 7 个条目 [MINLP-S73]–[MINLP-S79]。阅读层级：
> S73、S79 读了全文；S74、S75、S76、S77、S78 是部分阅读（partial）。读到的都是作者预印本、
> arXiv 或机构库版本，**期刊终版均未读**，期刊版可能有修订（各条已注明所读版本）。
> 同一 chunk 里的背景条目 [MINLP-S72]（Jeroslow 1973）**只读了摘要**，而且不是 Dey 的作品。
> 对照其他成员的条目时，按各条目自己的阅读层级标注；其中 S65 只读了摘要，S38、S40 只读了首页预览。
> 身份信息依据 Georgia Tech 的两个页面和 Google Scholar（verified-web，核实 2026-10-10）。
> 本档案没有使用 product/ 管线的任何文件。7 篇都是合作论文，其中 5 篇 Dey 不是第一作者（S73、S74、S75、S77、S79）。
> 文中所说的「Dey 的思维方式」，指的是这些合作产出中反复出现的做法，不是在推断他个人的偏好。

## 身份速览（verified-web）

核实日期 2026-10-10，所用页面：
https://www2.isye.gatech.edu/~sdey30/ （个人主页）、
https://www.isye.gatech.edu/users/santanu-dey （ISyE 教师页）、
https://scholar.google.com/citations?user=8Je5mV4AAAAJ&hl=en （Google Scholar）。

- **职位**：Georgia Tech H. Milton Stewart School of Industrial and Systems Engineering（ISyE）。
  ISyE 页写作 "Director of Doctoral Recruiting and Admissions and Anderson-Interface Chair and Professor"。
  个人主页写作 "Anderson-Interface professor and director of doctoral recruiting and admissions"。
- **教育**（据 ISyE 页）：Ph.D. Industrial Engineering (2007), Purdue University；M.S. Industrial
  Engineering (2003), Purdue University；B.E. Mechanical Engineering (2000), Mumbai University。
  到 Georgia Tech 之前，在 Université catholique de Louvain 的 CORE 做博士后（两个页面都有）。
- **研究自述**：ISyE 页原话是 "design and evaluation of algorithms for solving non-convex
  optimization problems, and in particular mixed integer linear and nonlinear programming
  problems"。应用动机包括 electrical power engineering、process engineering、structural engineering
  （主页此处写 civil engineering）、logistics、statistics。
  Scholar 显示的机构为 Georgia Institute of Technology，验证邮箱域 isye.gatech.edu；
  兴趣标签为 Integer Programming、Global Optimization、Mixed Integer Nonlinear Programming、
  Operations Research。
- **学术服务**：曾任 INFORMS Optimization Society 整数规划方向 vice chair（2011–2013，两个页面一致）。
  **编委信息两个页面不一致，下面并列给出，不作裁决**：
  - 主页说他现任 Computational Optimization and Applications 编委，以及 Mathematics of Operations
    Research、Mathematical Programming A、SIAM J. Optim. 的 associate editor。
  - ISyE 页说他现任 Mathematical Programming A 与 SIAM J. Optim. 编委，并把 COAP 与 MOR 列为过往职务。
  - 两个页面都列出的过往职务：INFORMS J. Computing associate editor、Mathematical Programming C
    area editor、MOS-SIAM 优化丛书编委。
- **奖项**（两个页面一致，下列信息只取自页面）：
  - INFORMS Optimization Society Balas Prize 2020
  - INFORMS ENRE Best Publication – Energy 2019
  - NSF CAREER Award 2012
  - IBM Faculty Award 2009
  - ISyE A. Russell Chandler III Professorship 2019–2022
  - Fouts Family Junior Professorship 2013–2016
  - INFORMS JFIG 论文竞赛 finalist 2010、2011、2012
  - 主页另列 2007 年 INFORMS Nicholson 学生论文竞赛第一名

  页面都没有写各奖项对应哪篇论文，本档案不做关联。

## 核心贡献

### 1. 复杂性：MIQP 属于 NP，且这一结论对二次约束个数是紧的 [MINLP-S73]
Del Pia, Dey, Molinaro, "Mixed-integer quadratic programming is in NP"（读了全文；所读版本为
2014-07-17 作者版，与 arXiv v1 一致）。

- **Theorem 1（proved-in-source）**：
  - 设定：数据为有理数，F = {x : xᵀHx + cᵀx + d ≤ 0, Ax ≤ b, x ∈ Z^p × R^{n−p}}。
  - 结论：若 F 非空，则 F 中存在一个点，其编码长度被数据规模的某个多项式界住。
  - 假设：不要求 H 半正定，不要求 {x : Ax ≤ b} 有界。
  - 推论：MIQP（min xᵀHx + cᵀx s.t. Ax ≤ b，混合整数）的判定版属于 NP。再由 max-cut 归约得到
    NP-hard，所以判定版是 NP-complete（Corollary 2）。
  - 地位：这一结果统一并推广了 QP ∈ NP（Vavasis，cited）与整数线性规划 ∈ NP 两个经典结论。
  - 锚点：(Theorem 1, Corollary 2, §1.1, p.2；证明 §3, pp.5–9)。
  - 注意：原文证明的是「可行时存在多项式大小的**可行解**」。「有界时存在多项式大小的最优解」在所读版本中
    **not stated**。
  - 摘要原句："This is established by showing that if the decision version of mixed-integer
    quadratic programming is feasible, then there exists a solution of polynomial size."
- **紧性（cited-by-source，三类反例都是引用来的）**：
  - 「很多」个一般二次不等式加整数变量时，可行性可以不可判定（引 Köppe 2012，给出 3424 个二次不等式的具体系统）。
  - 两个变量、一个二次等式时，最小可行整数解可以是实例规模的指数级（引 Lagarias 1980）。
  - 「很多」个凸二次不等式时，最小可行整数解同样可以是指数级（引 Khachiyan 1983）。
  - 作者原话："The above examples serve to highlight the fact that the result of Theorem 1 (a
    feasible system of inequalities with exactly one quadratic inequality always has at least one
    integer feasible solution of small size) is tight with respect to the number of quadratic
    inequalities."（p.3）
- **背景 [MINLP-S72]**（Jeroslow 1973，只读了摘要，不是 Dey 的作品）：
  - 摘要内容：约束中允许出现变量平方项的整数规划类，不存在能对该类所有问题算出最优值的计算设备。
  - 归约来源、变量是否有界，摘要都没有写（not stated）。
  - S73 没有引用 S72。

### 2. AC 最优潮流（ACOPF）：锥松弛的强弱层级与 SOCP 空间分支切割 [MINLP-S74, MINLP-S75]
- **松弛层级 [MINLP-S74] Theorem 3.1（proved-in-source）**：
  - 比较方式：投影到 (p, q) 空间比较六种凸松弛。
  - 包含关系：R̂_SDP ⊆ R̂_SOCP = Â*_SOCP ⊆ Â_SDP，且 Â*_SOCP ⊆ Â_M ⊆ R̂_M。
  - 每一个包含关系都可以是严格的（§3.2.2 用算例说明）。
  - 推论（§3.3）：
    - 矩形形式的 SDP 最强。
    - alternative formulation 的 SDP 反而弱于经典 SOCP 松弛（Jabr）。
    - 两种 McCormick（LP）松弛都弱于 SOCP。
  - 原文："On the one hand, RSDP is the best relaxation among the relaxation considered in Theorem
    3.1. On the other hand, quite remarkably, ASDP is weaker than ASOCP"（§3.3, p.14；抽取文本中丢了花体与星号）。
- **强化 SOCP 的效果 [MINLP-S74]（empirical）**：
  - 三种强化 SOCP：arctangent 包络（SOCPA）、cycle 约束 McCormick 割（S34A）、按 cycle 的 SDP 分离割（SSDP）。
  - 在 MATPOWER 6-bus 到 3375-bus 算例上，下界平均约为 SDP 下界的 99.7%（SOCPA、S34A）与 99.96%（SSDP）。
  - 在 2383-bus 及以上的大实例上，约比 SDP 快一个数量级。
  - 0.01% 阈值下，SDP 在 19 个实例中有 14 个是紧的，SSDP 只有 8 个；但 SSDP 的平均 gap 是 0.08%，SDP 是 0.19%。
  - 准确说法是**「极接近」**，不是「匹配或超越」。
  - Propositions 4.5 与 4.8（proved，用算例证明）：强化后的 SOCP 与标准 SDP **互不支配**。
    所谓 SOCP 「优于」 SDP，只是在个别实例上成立。
  - 原文："The lower bounds obtained by the strong SOCP relaxations are extremely close to those of
    the SDP relaxations, and are not always dominated by the SDP relaxations, but within a
    computation time that is an order of magnitude faster than the latter."（§6, p.34）
  - 实验条件：MOSEK 7.1、笔记本电脑、割生成至多 5 轮；所读版本为 2015-12 作者版。
- **minor 精确重构 [MINLP-S75] Proposition 3.1（proved-in-source）**：
  - 结论：非零 Hermitian 矩阵 X 满足「X ⪰ 0 且 rank 1」，当且仅当它的所有 2×2 minor 为零且对角元非负。
  - 用途：把 rank 约束换成 minor 约束是**精确重构**，z_ACOPF = z_rank = z_minor。
  - minor 分三类：edge、3-cycle、4-cycle。摘要称它们与「3-/4-cycle 上相角差之和为零」的物理约束等价。
  - 此前文献只用主子式（Type 1）；本文用非主子式（Type 2/3）得到更强的松弛。
- **SOCP 空间分支切割 [MINLP-S75]（empirical）**：
  - 根节点：
    - SEP(S) 与 SEP(M,S) 的平均 gap 约为 SDP 的一半，时间分别少约 50% 与 15%。
    - 纯 LP/SOCP 的 SEP(M) 也强于 SDP，只用约 25% 的时间。
  - 分支后：最好的 SEP(S) 在 30 分钟预算下平均 gap 为 0.71%，平均约 720 s。
  - 不少实例 30 分钟后仍高于 10^-3 阈值。准确说法是**缩小** gap，不是闭合 gap。
  - 实现细节：节点上的 SOCP 每次从头构建，原因是 SOCP 没有高效的 warm start。
  - 所读版本为 arXiv v1。
  - 原文："The strongest of our SOCP based branch-and-cut algorithms proves 0.71% optimality gap in
    720 seconds on the average for the NESTA library."（§6, p.33）

### 3. 池化问题（pooling）：MILP 技术的保证、极限与离散化 [MINLP-S76, MINLP-S77]
- **[MINLP-S76] Theorem 1（proved-in-source）**：
  - 设定：standard pooling，任一事先给定、与实例无关的分段线性（MILP）松弛方案，n = 输出节点数。
  - 结论（原文为利润最大化）：松弛值 z^S ≤ n·z*；并且对任意 ε > 0，存在实例使 z^S ≥ (n − ε)·z*，即界是紧的。
  - 改写成本库的最小化形式 min(−profit)：记 v = −z，则下界满足 v^S ≥ n·v*。
  - 含义：每个双线性项的逼近误差可以任意小，但在最坏情况下会累积成约 n 倍的整体误差。
  - pooling 的 NP-hardness 不是本文证明的，引自 Alfaki–Haugland。
  - 摘要原句："we prove that the ratio of the upper bound obtained by solving piecewise-linear
    relaxations (objective function is maximization) to the optimal objective function value of
    the pooling problem is at most n, where n is the number of output nodes."
- **[MINLP-S76] Theorem 2（proved-in-source；不可近似部分依赖引用的结论）**：
  - 正面结果：解一个多项式规模的 LP（IPOP），只保留目标贡献最大的那个输出节点上的流量，得到多项式时间
    n-近似算法。
  - 反面结果：对任意固定 ε > 0，若存在近似比优于 n^{1−ε} 的多项式时间算法，则 NP-complete 问题有随机多项式时间算法。
  - 不可近似性的证明：Håstad 关于最大稳定集的结论（cited），加上本文证明的保近似比归约（Proposition 3）。
    归约实例只有一个 pool，且 |I| = |J| = |K| = n。
- **[MINLP-S76] 带保证的 MILP restriction**：
  - 构造（proved）：其可行域包含 n-近似算法能给出的全部解，所以最优解不差于 n 倍。
  - 计算（empirical）：在 70 个中大规模实例上，摘要称它常常比商业局部与全局求解器好出数量级。
  - 摘要原句："This heuristic is guaranteed to provide solutions within a factor of n. On
    large-scale test instances and in significantly lesser time, this heuristic provides solutions
    that are often orders of magnitude better than those given by commercial local and global
    optimization solvers."
  - 比较条件要一并说明：
    - 时限不对等：BARON 跑 6 小时，其他方法至多 1 小时。
    - 只有 4 个实例被全局求解到 0.01% gap。
    - BARON 取得最佳解的实例比例最高（约 0.42），但在大实例上明显退化。
- **[MINLP-S77] 公式强弱（proved-in-source，最小化成本形式）**：
  - P、Q、PQ、HYB 四种精确模型彼此等价，但 LP 松弛强弱不同：z^p ≤ z^pq。
  - pq-relaxation 的强度等价于对每个 pool 的集合取凸包（Proposition 3.2、Remark 3.4）。
  - HYB 的强度介于 P 与 PQ 之间；P 与 Q 互不支配。
  - 与 Tawarmalani–Sahinidis (2002)、Alfaki–Haugland 的关系：二者已对 McCormick 版 p-relaxation 证明过
    z^p ≤ z^pq；本文的 p-relaxation 用完整的 level-1 RLT，结论更强。
  - 原文："Hence it follows that the strength of the HYB formulation is between that of P and PQ.
    There is no dominance between P and Q formulations."（2016 版 p.15）
- **[MINLP-S77] 离散化 restriction（empirical）**：
  - 基于 PQ 的模型（离散化与否）给出的解远优于基于 P 的模型。
  - 离散化改进了 Dey–Gupte (2015) 附录 D 中 70 个实例里 6 个的已知最好上界。
  - 在 generalized 实例上结论不一致：meyer* 实例上，BARON 直接解 P 胜过所有离散化。
  - 下界方面作者认为 Lagrangian 松弛比 RLT 更有希望，但还缺少可处理的多面体表示或分离算法。
- **[MINLP-S77] 复杂度现状（cited-by-source）**：
  - 单 pool 的 standard pooling 已是 NP-hard（Alfaki–Haugland）。
  - 单 pool 在 |K| 或 |J| 固定时多项式可解（Haugland 等）。
  - 单 pool 与稳定集问题一样难近似（Dey–Gupte 2015）。

### 4. 非凸 QCQP：稀疏割与二次集合的凸包 [MINLP-S78, MINLP-S79]
- **[MINLP-S78] 稀疏割的分离等价于 Sparse PCA（proved-in-source + cited）**：
  - 等价性：寻找 k-sparse eigencut、或判定它不存在，等价于 k-SPCA（Proposition 3.2、Lemma 3.3）。
    由 SPCA 的 NP-hardness（cited）推出这一分离问题是 NP-hard。
  - 存在性：最坏情况下稀疏割可能根本不存在。Blekherman et al. 的矩阵 G(a, b) 满足所有 k×k 主子阵 PSD，
    但整体不 PSD（Examples 3.4–3.5）。
  - 实践：用 SPCA 启发式（TPower）仍能高效找到强割。
- **[MINLP-S78] 计算（empirical）**：
  - 主要结论：HYBRID（先加 dense 割，再加 sparse 割）在变量数至多 100 的 BoxQP、Biq、MaxCut 实例上，
    1 小时内**倾向于**闭合初始 LP 与 SDP 之间 90% 以上的 gap。
  - 原文："for QCQP instances with at most 100 variables and across three different benchmark
    families, within an hour of computation, we tend to close more than 90% of the gap between the
    initial LP relaxation and the SDP relaxation, representing a significant improvement with
    respect to either dense or sparse cuts alone."（AAM §7, p.22）
  - 限定条件：
    - SPARSE 单独使用效果不稳定；dense 割出乎意料地强。
    - 最大的 MaxCut 组在 1 小时内只闭合 5–6%。
    - gap 以 SDP 界为参照，不是相对全局最优。
    - 方法尚未嵌入 B&B。
- **[MINLP-S79] Theorem 1（proved-in-source，读了全文 = arXiv v1）**：
  - 结论：S = {x : xᵀQx + αᵀx = g, x ∈ P}，Q 任意对称（可非凸），P 为多胞形，则 conv(S) 是二阶锥可表示的（SOCr）。
  - 证明是构造性的：仿射化为标准形，再分情形，用按维数归纳加析取组合。
  - 只针对单个二次**等式**；二次不等式或多个二次约束的情形 v1 未陈述。P 必须有界。
  - 摘要原句："This paper makes a contribution in this direction by showing that the exact convex
    hull of a general quadratic equation intersected with any bounded polyhedron is second-order
    cone representable."
- **[MINLP-S79] 可表示不等于可高效求解（stated-position）**：
  - 作者原话："Note that optimizing a linear function over S is NP-hard, therefore, while the
    convex hull is SOCr, the construction involves the introduction of an exponential number of
    variables."（p.2）
  - 作者还提到 3×3 PSD 锥本身不是 SOCr（引 Fawzi）。

## 心智模型（三重验证）

按 standards/researcher-extraction.md 做三重验证，结果是 3 条心智模型加 1 条工作信条。

### 模型1 用稀疏、局部的 LP/SOCP 对象买回 SDP 的强度 ✅三重通过
**陈述**：SDP 被当作**要逼近的强度标尺**，而不是节点上直接求解的松弛。做法是从 PSD 条件中挑出稀疏或局部的部分
（2×2 minor、3-/4-cycle、k-sparse 特征向量），写成 LP/SOCP 可表示的割。随后同时报告两件事：
找回了多少 SDP 强度，付出了多少时间。

- **跨域复现**（4 个不同 ID，涵盖电网与一般 QCQP 两个问题域）：
  - [MINLP-S74]：强化 SOCP 达到 SDP 下界的 99.7–99.96%，快一个数量级。
  - [MINLP-S75]：minor 精确重构后，用 LP/SOCP 外逼近做空间分支切割；根节点的 SEP(M) 只用 SDP 约 25% 的时间，
    界还强于 SDP。
  - [MINLP-S78]：k-sparse 特征向量割加 dense 割，闭合 LP–SDP gap 的 90% 以上。
  - [MINLP-S79]：从理论侧支持「不需要 SDP」。单个二次等式与多胞形之交的精确凸包已是 SOCr；
    同一条目也说明，SOCr 的代价可以是指数规模。
- **生成力**（可检验的推断）：
  - 遇到 SDP 松弛很强、但在大规模或分支定界里太贵的非凸二次问题，Dey 会问：PSD 条件中哪个稀疏子结构
    （小 minor、短 cycle、稀疏特征向量）能用 LP/SOCP 割刻画？
  - 然后他会用「占 SDP 界的百分比 / 闭合 LP–SDP gap 的百分比」加上「相对 SDP 的时间」来汇报结果。
  - 他不会默认在每个节点上解 SDP。
- **排他性**：
  - 对照做法一：直接以 SDP 作为节点松弛。[MINLP-S58] Burer–Vandenbussche 的有限 B&B 在每个节点解 SDP，
    并论证 KKT 分支下的 LP 松弛无界、所以必须用 SDP。
  - 对照做法二：完全不利用 PSD 信息的逐项因式分解多面体松弛，如 [MINLP-S37] 的 Algorithm Relax。
  - 需要说明：「用线性/SOC 约束近似半正定性」本身不是 Dey 独有。
    - [MINLP-S59] Anstreicher 把它列为降低 SDP+RLT 代价的方向。
    - [MINLP-S66] Saxena–Bonami–Lee 用稠密特征向量凸二次割迭代施加 PSD。
  - Dey 的区别在于**稀疏化和局部化**：sparse eigencut、cycle minor。并且 [MINLP-S78] 的实验正面回应了
    「dense 割是否已经够用」：dense 割出乎意料地强，sparse 割要和 dense 割合用才最好。
  - 结论：排他性按「稀疏/局部化」这一点判为通过。
- **分级**：心智模型。

### 模型2 每个保证都要配一个边界：正面结果加上紧性或反例 ✅三重通过
**陈述**：一个松弛、算法或复杂度结论，只有同时给出两样东西才算完整：(a) 能证明的保证；
(b) 这个保证在哪里是紧的、在什么条件下失效。

- **跨域复现**（5 个不同 ID，涵盖复杂性、池化、ACOPF、QCQP 割、凸包理论）：
  - [MINLP-S73]：一个二次不等式时 MIQP ∈ NP，作者明确指出该结论对二次约束个数是紧的。
  - [MINLP-S76]：分段线性松弛的 n 倍界，配 (n − ε) 紧实例；n-近似，配 n^{1−ε} 不可近似。
  - [MINLP-S74]：Theorem 3.1 的每个包含关系都可以严格；强化 SOCP 与 SDP 互不支配。
  - [MINLP-S78]：稀疏割分离是 NP-hard，最坏情况下稀疏割可以不存在。
  - [MINLP-S79]：凸包是 SOCr，但构造可以有指数个变量。
- **生成力**（可检验的推断）：
  - 给 Dey 一个新的松弛或启发式，并说它在基准测试上表现很好，他会追问三件事：
    - 最坏情况下离最优多远？
    - 这个界有没有匹配的紧实例或不可近似下界？
    - 换一个结构参数（约束个数、输出节点数、稀疏度 k），结论还成立吗？
- **排他性**：
  - 对照做法：全局求解器与 MINLP 方法论文的主流评估方式，是在基准集上做 performance profile 和求解数比较，
    不给最坏情况质量界。例如：
    - [MINLP-S53] GloMIQO 在 399 题上与 BARON、SCIP 等比较。
    - [MINLP-S55] APOGEE 的分段数 N_P = 4 是由计算比较选出来的。
  - 需要说明：团队内 Misener 组的 [MINLP-S80] 也做 pooling 的复杂度刻画，所以这条不是团队里独一份；
    但它不是 MINLP 计算文献的默认做法。
- **分级**：心智模型。

### 模型3 在网络的局部单元上凸化，而不是逐项凸化 ✅三重通过
**陈述**：对网络型非凸问题（电网、池化），有效的凸化单位是网络拓扑里的局部结构，比如一个 cycle、一个 pool。
在这些单元上求凸包或推有效不等式，比对每个双线性项单独取 McCormick 包络强得多，
而且这种强度差可以用定理或实例刻画出来。

- **跨域复现**（3 个不同 ID，涵盖 ACOPF 与 pooling 两个应用域）：
  - [MINLP-S74]：3-/4-cycle 分解上的 cycle 约束 McCormick 割与按 cycle 的 SDP 分离割；
    McCormick（LP）松弛被证明弱于 SOCP。
  - [MINLP-S75]：minor 约束与 cycle 上相角差之和为零等价；非主子式（cycle minor）带来更强的松弛。
  - [MINLP-S77]：pq-relaxation 的强度等价于逐个 pool 取凸包（Proposition 3.2、Remark 3.4）。
  - 反面印证 [MINLP-S76]：逐项、事先给定的分段线性逼近，即使每项误差任意小，最坏情况也累积成 n 倍误差。
- **生成力**（可检验的推断）：
  - 面对一个新的网络流型双线性问题（例如带品质约束的水网或燃气网），Dey 会先找出拓扑中的最小重复单元
    （cycle、pool、节点），在单元上刻画凸包或推导割，再组合起来。
  - 他会预期，只做逐项 McCormick 时，误差在最坏情况下可能随网络规模累积。
- **排他性**：
  - 对照做法：因式分解型全局求解器的默认路线，即把函数拆成单个双线性项并逐项取包络。
    例如 [MINLP-S37] 的 Algorithm Relax 与 Bilinear Relax；McCormick 包络的出处归于 [MINLP-S33]，
    但该条目只读到首页，包络本身在可读页中没有出现。
  - 需要说明：
    - Sahinidis 组的 [MINLP-S65] multiterm 松弛也超出了逐项包络，但它在单个二次约束内部组合多项
      （只读了摘要）。Dey 的单元是跨约束的网络结构。
    - [MINLP-S52] Misener–Floudas 证明，过程网络的品质平衡约束是 sum decomposable，逐方程凸包已等于逐项松弛，
      应改用 RLT、专门的割或分段线性。这和本模型「跨方程、按拓扑单元」的方向一致，可以互相印证，并不矛盾。
- **分级**：心智模型。

### 工作信条（未全过三重验证）：用 MILP restriction 给大规模非凸问题找带保证的可行解
**陈述**：当全局求解器在大实例上退化时，Dey 的做法是离散化一部分变量，构造可行域的内逼近
（MILP restriction），让它包含有近似保证的解，再交给 MILP 求解器。

- **跨域复现：未通过（证据偏窄）**。形式上有 2 个 ID：[MINLP-S76] 带 n 倍保证的 restriction，
  [MINLP-S77] 变量离散化 restriction。但两者都是 pooling，而且是同一研究线的延续（S77 引用 S76 的附录 D 作为基准）。
  语料中没有 Dey 在其他问题类上使用 restriction 的条目。
- **生成力：通过**。遇到大规模双线性网络问题时，他会先给出一个带保证的 MILP 内逼近，用来提供可行解。
- **排他性：通过**。对照做法是通用全局求解器 [MINLP-S36] BARON，以及局部 NLP/SLP 求解器。在两篇的实验里，
  BARON 取得最佳解的实例最多，但在大规模标准实例上迅速退化。
- **分级**：工作信条（标注「未全过三重验证」）。

## 与其他成员的分歧与张力

- **与 Sahinidis：LP 节点还是 SOCP 节点（推断）**：
  - Sahinidis 一方：
    - [MINLP-S38] 与 [MINLP-S40] 认为，多面体（LP）松弛的 gap 虽然比它所来源的非线性凸松弛更大，
      但 LP 求解器更快、更稳健，整体更可靠。（S38、S40 都只读了首页预览。）
    - [MINLP-S40] 后来改为 LP/NLP 混合并自动切换。
  - Dey 一方：[MINLP-S75] 在节点上直接解 SOCP，并在实现中承认 SOCP 没有高效的 warm start，
    节点 SOCP 只能从头构建。这正是 S38/S40 所强调的 LP 优势的反面。
  - 判断：这是方法选择上的张力，没有找到两组之间的直接交锋。
- **与 Sahinidis：池化公式与 BARON 基准（有文献记录）**：
  - [MINLP-S77] 明确把 Tawarmalani–Sahinidis (2002) 的 z^p ≤ z^pq（McCormick 版）推广到完整 level-1 RLT 版本。
  - [MINLP-S76] 与 [MINLP-S77] 都以 BARON 为基准，结论是双向的：BARON 取得最佳解的实例最多，
    但在大规模标准实例上，结构化的 MILP restriction 更好。
  - 原文旁证（本档案写作时在 S76 预印本中核对到，不在 chunk claims 内）：Dey–Gupte 预印本 p.3 把 pq-formulation
    归于 Tawarmalani and Sahinidis (2002)。
- **与 Misener：分段线性松弛的地位（推断，另有一处原文旁证）**：
  - Dey 一方：[MINLP-S76] Theorem 1 说明，**事先给定**的分段线性松弛在最坏情况下可差 n 倍。
  - Misener 一方：
    - [MINLP-S55] APOGEE 与 [MINLP-S52] 把分段线性（线性或对数编码）**嵌在全局 B&B 中**作为收紧手段；
      [MINLP-S52] 的结论是它只对特定问题类（非线性变量多的过程网络）最划算。
    - [MINLP-S53] GloMIQO 默认关闭分段线性。
  - 判断：两者作用对象不同。Dey 的界针对不分支、与实例无关的单次松弛；APOGEE 在收敛的 B&B 中用分段收紧，
    不构成直接矛盾。两组从最坏情况理论和计算两个方向，都对分段线性持保留态度。
  - 原文旁证（不在 chunk claims 内）：Dey–Gupte 预印本 §5 开头（p.21）写道，他们试用过 APOGEE，
    但 "did not observe any performance benefit compared to BARON"。这是两组之间唯一一处直接接触，
    只限于他们的实例与设置。
- **与 Misener：池化问题的难与易（推断，两者不矛盾）**：
  - Dey 一方：[MINLP-S76] 的 n^{1−ε} 不可近似性用的归约实例是单 pool、|K| = n 个品质、弧容量为 1；
    [MINLP-S77] 转述，单 pool 在 |K| 固定时多项式可解。
  - Misener 一方：[MINLP-S80] 的 strongly-polynomial 子类要求单一品质（K = 1）、去掉 feed/pool 容量约束、
    需求固定（Assumption 2.2）。
  - 判断：困难性来自品质数随规模增长再加上容量约束，可解性正好落在这些条件的对立面。
    两条线描绘的是同一条 P/NP 边界的两侧。这个对照是本档案根据两个条目的假设推出来的，原文中没有这样的交流记录。
- **与 Burer：SDP 是节点松弛还是逼近目标（推断）**：
  - Burer 一方：
    - [MINLP-S58] 在每个节点用 SDP，并论证 LP 松弛在 KKT 分支下无界。
    - [MINLP-S57] 把全部困难集中到完全正锥上。
    - [MINLP-S60] 与 [MINLP-S61] 给出低维或特殊几何下 PSD+RLT、DNN、SOC-RLT 的精确表示。
  - Dey 一方：把 SDP 当作强度标尺，用 LP/SOCP 去逼近（模型1）。
  - 两组共享的问题是「二次集合的精确凸包能用哪种锥表示」：
    - [MINLP-S79]：任意维、单个二次等式与多胞形之交是 SOCr，但规模可以是指数的。
    - [MINLP-S60]：盒约束 n = 2 时 PSD+RLT 精确，单纯形 n ≤ 4 时 DNN 精确。
    - 两者覆盖的结构与维数不同，属于互补，不是冲突。
  - Burer 也不排斥廉价近似：[MINLP-S63] 转述的计算中，PSD 以凸二次割平面施加，没有用黑箱 SDP。
    所以这里的分歧是**侧重点**不同，不是立场对立。
- **与 Burer（及 Liberti 的综述）：复杂性的分界线（推断）**：
  - [MINLP-S2] Burer–Letchford 指出，不可判定性证明都用到无界可行域。
  - [MINLP-S9] Liberti 把可判定性归结为整数变量是否有界。
  - [MINLP-S73] 不要求多面体有界，只要恰好一个二次不等式，判定版就在 NP 中；
    而「很多」二次不等式时可以不可判定（cited）。
  - 判断：两种说法刻画的是不同的分界参数（有界性 vs 二次约束个数），彼此一致，不矛盾。
- **与 Grossmann、Leyffer**：语料中 Dey 的条目与凸 MINLP 主线（OA、NLP-BB、GDP 等）**没有直接交集**，
  本档案不编造张力。

## 边界

- **未读全文**：
  - S74、S75、S76、S77、S78 是部分阅读，未读部分包括：S74 的 §4.4 变量界技术、S75 各类包络与割的细节、
    S76 的 Theorem 4 与附录、S77 的 §3.3–3.4 RLT/Lagrangian 细节、S78 的 §4.1–4.3 与 §5。
  - S72 只读了摘要。
  - 所有数字都来自预印本、arXiv 或 AAM 版本，期刊版可能有修订。
  - [MINLP-S79] 期刊版摘要多出 "some preliminary applications"，这部分在 v1 中没有，本档案未覆盖。
- **原文为最大化的结论**（S76 的利润形式）已按最小化约定改写；方向以 chunk 的说明为准。
- **数值**：数值结论都是 empirical，绑定当时的求解器版本（MOSEK 7.1/8、CPLEX 12.2/12.6、BARON 12.7.3/13.1、
  Gurobi 9.0）与硬件，不能外推为一般性的优劣判断。
- **快照性信息**：职位、编委、奖项是 2026-10-10 的页面快照。两个 GT 页面的编委信息不一致，已并列给出。
  Scholar 的引用数会变，没有写入。
- **语料之外的 Dey 工作**（ISyE 页列出，但不在本语料中，因此本档案不做任何断言）：
  - MILP 割平面理论。语料中只在 [MINLP-S70] 里被提到：该条目说它推广了 Dey–Wolsey 关于 maximal lattice-free
    集判据的「only if」方向。
  - 分支定界树规模的上下界。
  - 二次不等式聚合与凸包。
  - sparse PSD approximation。
  - 稀疏 PCA 的全局求解。
- **署名**：7 篇都是合作论文。「心智模型」描述的是这些合作产出中反复出现的模式，不代表 Dey 个人的独立立场。

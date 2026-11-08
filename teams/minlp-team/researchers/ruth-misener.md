# Ruth Misener · MINLP Team 研究者档案

> 档案依据：canon 中由 Misener 署名的 8 条语料，层级均为 verified-web（语料构建核实 2026-10-10）：
> [MINLP-S52]（读全文：Imperial Spiral 接受版 + Optimization Online 预印本的附录 A 证明）、
> [MINLP-S53]（读部分：Spiral 接受版；§2 文献综述、附录 B 测试集细表未读）、
> [MINLP-S54]（读全文：Spiral 接受版手稿；177 页补充材料未细读）、
> [MINLP-S55]（读部分：Spiral 上 2010-12-21 预印本，**不是期刊排版版**；§2 综述、§3 模型细节未读）、
> [MINLP-S80]（读部分：Springer OA 版本记录版；附录 A 证明未逐行读）、
> [MINLP-S81]（读全文：JMLR 正式版）、
> [MINLP-S82]（读部分：arXiv v3 作者版；附录 A–D 未读）、
> [MINLP-S89]（读部分：提交版预印本；Misener 是 13 位作者之一）。
> 没有一条只读到摘要，但多数读的是预印本或接受版，页码与措辞以所读版本为准。
> 身份信息来自下节三个一手页面（核实 2026-10-10）。与其他成员的对照只引用对方的 canon 条目，
> 且只用 chunk 中记录过的声明；凡是档案作者的连线而非文献中的直接交锋，一律标「推断」。

## 身份速览（verified-web）

- **个人主页**（verified-web，核实 2026-10-10，http://wp.doc.ic.ac.uk/rmisener/ ）：自述 Professor in the
  Computational Optimization Group（Imperial College London, Department of Computing）、Amazon Scholar、
  BASF/RAEng Research Chair in Data-Driven Optimization（2022-27）。研究基础为 numerical optimization 与
  computational software，应用面向工业中的优化问题（如物流、实验设计），并从事运筹学与机器学习的交叉。
  项目列表包括 "Global optimization of mixed-integer nonlinear programs"、"Optimization over machine learning
  surrogates"（页面原话："developing mathematical programming formulations of machine learning surrogate
  models"）、"Global optimization of petrochemical process networks"（燃料调和，即 pooling 类问题）等。
- **Imperial 官方页**（verified-web，核实 2026-10-10，https://www.imperial.ac.uk/people/r.misener ，
  重定向到 https://profiles.imperial.ac.uk/r.misener ）：职位 "Professor in Computational Optimisation"，
  Department of Computing – Faculty of Engineering；学位 PhD, Princeton University（页面所列时段
  2007-09 至 2012-11）、S.B., MIT（2003–2007）；ORCID 0000-0001-5612-5417；Bio 首句
  "I develop underlying algorithms that power optimal decision-making under uncertainty."；
  页面同样写明 Amazon Scholar 职务。
- **Google Scholar**（verified-web，核实 2026-10-10，https://scholar.google.com/citations?user=AQxtWHoAAAAJ&hl=en ，
  curl 原始响应与 WebFetch 两次读取一致）：机构 Imperial College London，已验证 imperial.ac.uk 邮箱；
  兴趣标签 Computational Optimization、MINLP、Bayesian Optimization、Open-source Software。
  快照：该页按被引排序的首篇是 ANTIGONE [MINLP-S54]。
- 师承说明：[MINLP-S52]–[MINLP-S55] 均与 C. A. Floudas 合著，[MINLP-S55] 预印本署 Princeton；
  但所查页面都没有写导师关系，本档案**不作导师断言**。
- 快照提醒：职位、讲席（2022-27 任期）、Amazon Scholar、被引排序均为 2026-10-10 快照，会过时。

## 核心贡献

### 1. MIQCQP 松弛与全局求解器谱系（GloMIQO → ANTIGONE）

- **[MINLP-S52] 分段线性 + edge-concave（EC）松弛**（Math. Program. 2012；读全文）
  - 方法（definition）：在 B&B 的每个节点，对低维（n≤3）EC 聚合计算凸包刻面，**只加入严格优于逐项
    McCormick 的刻面**；刻面算法引自 Meyer–Floudas [MINLP-S51]（cited-by-source）。不在连通 EC 聚合中的
    凹多变量项与稀疏双线性项用分段线性松弛，编码可选线性或对数（abstract；§3.1, Table 1）。
    假设：参与非线性项的变量能推出有限界；连续部分可非凸。
  - proved-in-source：sum decomposable 的方程（和的凸包络等于凸包络之和，Def. 3.1.1.2），逐项松弛已等于
    该方程的凸包，逐方程不能再加更紧的切割；过程网络的品质平衡约束一般是 sum decomposable
    （Property 3.1.3.1；§3.1.3）。只有 EC 聚合中三个双线性系数都非零时刻面才可能严格占优（Obs. 3.1.1.8）。
    相关的 Tardella 定理是 cited，文中注明 "without proof"（Thm 3.1.1.3）。
  - proved-in-source：对数分段格式 1、2 的 LP 松弛不被单项 McCormick 凸包支配（Properties 3.1.6.2–3.1.6.3，
    证明在 Optimization Online 版附录 A）；格式 2 要求 N_P 为 2 的幂。文中 "sharp" 的定义与实际证明的性质
    前后不一致，引用时只能说「不被支配」。
  - empirical（作者自有 C++ 实现；1e-6 相对间隙或 7200 CPU s；43 个算例）：EC 对 MIQCQP 普遍有价值，分段线性
    只适合特定类别；同时比较线性与对数编码时，相差至少 10% 的 10 例中 8 例有利于线性编码（§4.3）。
    > "In summary, while we find strong evidence for the value of low-dimensional edge-concave aggregations in
    > any MIQCQP, the piecewise-linear underestimation scheme is best applied to specific classes of MIQCQP
    > (e.g., process networks problems with many nonlinearly-participating variables)."（§4.3, p. 20，Spiral 接受版）
- **[MINLP-S53] GloMIQO**（J. Glob. Optim. 2013；读部分）
  - 组件（definition）：把 MIQCQP 解到 ε-全局最优。依次为：重构用户输入（变量消去、双线性项解聚）；
    检测特殊结构（RLT 方程，按图把方程划成可分多变量项，再检测凸性与 EC）；生成紧凸松弛（逐项 McCormick、
    EC 刻面、特征向量投影、分段线性、凸项的外逼近切割、自适应 RLT，**松弛为 MILP 而非 LP**）；reliability
    branching（不对二元变量分支，二元变量交给 MILP 求解器）；FBBT/OBBT/reduced-cost 界收紧；找可行解
    （abstract；§3.1–3.6）。
  - stated-position：分段线性下估计**默认关闭**。理由是对不用它也能收敛的问题，关闭时收敛一般更快；
    建议在大规模过程网络与 pooling 等难问题上手动开启（§3.3.4）。
  - empirical：399 题，对比 BARON 10.1.2、Couenne 0.4、LindoGLOBAL、SCIP 2.1.0（2012 年初的版本），可行性容差
    统一为 1e-6，GloMIQO 在 68% 的算例上最快、81% 在时限内解决；作者用独立脚本做可行性后处理，发现
    Couenne 0.4 在超过一半的算例中返回不可行点（§4, §4.2.5）。
- **[MINLP-S54] ANTIGONE**（J. Glob. Optim. 2014；读全文）
  - 问题类（definition）：MINLP，变量可为连续、二元或一般整数；要求参与非线性项的变量能推出有限界。它是
    GloMIQO 与 MISO 框架向一般非凸 MINLP 的推广（§2）。
  - 结构检测（definition）：方程重写为 Table 1 中各类项之和，再检测 RLT 方程、凸/凹、edge-convex/edge-concave、
    αBB 下估计（用于双线性项聚合体）以及项特定下估计（§3.2）。
  - 局限（作者自述）：凸性检测只针对单个项与二次项的聚合体，"does not, at this writing, apply function
    composition rules or symbolic methods"（§3.3）；三角函数、min/max、erf 等形式当时无法处理（§4）。
  - empirical：2571 题，对比 GAMS 24.2.1 中的 BARON 12.7.3、Couenne 0.4、LINDO 8.0、SCIP 3.0（2014-02 的版本）；
    作者自述最强的部分是二次非线性，全部非线性为二次时与 GloMIQO 等价（§5.8；§2）。
- **外部定位**：Burer–Letchford 的综述把 GloMIQO 列为当时（2012）能把非凸 MINLP 解到可证最优的五个软件
  之一，与 BARON、αBB、LINDO-Global、Couenne 并列（[MINLP-S2] §6）。凸 MINLP 基准 [MINLP-S3] 把 ANTIGONE 归入
  全局求解器组，并提醒全局求解器可能把凸函数当非凸处理、生成不必要的弱松弛（§6.4）。这与 [MINLP-S54] §3.3
  自述的凸性检测局限相互吻合（推断：[MINLP-S3] 没有点名 ANTIGONE 为此类实例）。
- 收敛性说明：canon 未记录 GloMIQO/ANTIGONE 的收敛定理。「ε-全局最优」是求解器的设计目标与终止准则，
  前提是参与非线性项的变量有有限界（[MINLP-S53] §1；[MINLP-S54] §2）。

### 2. Pooling：分段松弛与复杂度结构

- **[MINLP-S55] APOGEE**（Comput. Chem. Eng. 2011；读预印本部分）
  - definition：标准、广义、扩展三类 pooling。分段数 N_P 固定时，线性与对数编码**精确表示同一个析取规划 (6)**，
    区别只在 MILP 规模（单个双线性项：线性编码 N_P 个二元变量，对数编码 ⌈log2 N_P⌉ 个，Table 4）。所以松弛
    紧度由 N_P 决定，编码只决定规模与求解行为（§4.1–4.2）。采用均匀分段，假设 x、y 有有限界。
  - empirical（25 题，N_P ∈ {3,4,5,6,8,12,16}，嵌入完整全局算法而非孤立 MILP 比较）：N_P≥8 时对数编码明显
    占优（N_P=8 时线性/对数分别胜 11/21 次）；但全局算法通常在小分段数（3–5）收敛最快，此时线性编码占优；
    三个超大问题用对数编码出现数值困难。结论：pooling 推荐线性编码，取 N_P=4（§5, Tables 6–8；§7）。
  - stated-position：作者称（据其所知）这是首个对连续非线性函数做对数规模松弛的工作（§4.2.2）。
- **[MINLP-S80] Pooling 的分段参数结构**（Baltean-Lugojan & Misener, J. Glob. Optim. 2018；读部分）
  - proved-in-source：在 Assumption 2.2（单一 quality；问题可行；去掉 feed availability 与 pool capacity 约束；
    各 output 的 demand 固定）下，以 pool concentration p 为参数，识别 dominant active sets 与 breakpoints，
    给出多个拓扑子类的 **strongly-polynomial** 精确全局算法：I-1-1、H-1-1、I+H-1-1、I+H-1-J（另需全部参数为
    有理数）、I+H-L-1（Thm 3.1.6, 3.2.7, 3.3.9, 4.4, Cor 4.5, Cor 5.4）。语料只记多项式阶，不记常数。
    原文以利润最大化陈述，按本库约定等价于 min（−利润）。
  - proved-in-source：Haverly 的三个经典实例属于 Assumption 2.2 下的 I+H-1-J 类，可解析求出精确解
    （Remark 4.7；「满足假设」是作者断言，语料未逐例核查）。
  - proved-in-source（结构）：单 output 时最优目标 f(p) 在 breakpoints 之间分段单调（Thm 3.3.8）；I+H-L-1 的
    最优解至多两个 active pools（Thm 5.2）。作者据此形式化了 Floudas 关于 pooling 根植于分段函数的直觉（§1, §6）。
  - cited-by-source / remark 级：NP-hard 一侧不是本文的形式证明——一般 standard pooling 的 NP-hardness 与
    single-quality 全拓扑的 strong NP-hardness 引自 Alfaki–Haugland（§1；[4, Corollary 2]）；Remark 4.6 论证放松
    Assumption 2.2 的任一项都会落入 NP-hard 侧，只是 remark 级论证。
  - 假设敏感性：恢复 flow bounds 后解的稀疏结构逐步消失（Remark 3.3.10, 5.6）。

### 3. 优化 × 机器学习：把训练好的模型写进数学规划

- **[MINLP-S82] ENTMOOT**（Comput. Chem. Eng. 2021；读 arXiv v3 部分）
  - definition：已训练的 gradient-boosted regression trees 按 Mišić 的混合整数公式编码，加入基于距离的探索项，
    合成 LCB 型采集函数，由确定性全局求解器（Gurobi 9）求到 ε-全局最优，取代树模型 BO 中常见的随机采样式
    优化；已知约束可为线性或（凸/非凸）二次（§1；§3）。问题类随度量变化：探索模式下 squared Euclidean 给出
    非凸 MIQP，Manhattan 给出 MILP（§3.2.2–3.2.3）。超大树模型时提出定制空间 B&B（§4.0.2）。
  - 关键限定：摘要所说的「全局最优」只针对采集子问题（给定已训练树模型与距离度量），**不是黑盒 f 的
    全局最优**；本文没有 BO 收敛速率结论；距离能否代理不确定性只有经验检验（§6.1）。
  - empirical：300 次评估预算下，与其他 BO 框架相比有胜有负（§6.3）；同一采集函数的随机采样版
    ENTMOOT-RND 在 Rosenbrock 上不如确定性版本（§6.2）。
- **[MINLP-S81] OMLT**（JMLR 2022；读全文）
  - definition：把训练好的 NN（ONNX、Keras）与 GBT（ONNX）翻译成 Pyomo block 中的变量与约束，作为更大优化
    问题的目标或约束；ReLU 有 big-M、complementarity、partition-based 三种公式，平滑激活有 full-space 与
    reduced-space 两种（§3）。公式强度的性质在被引原文中，本文不证明。
  - stated-position：
    > "In OMLT, competing optimization formulations become alternatives: users can switch between the Section 3
    > formulations and find the best for a specific application."（§4, p. 4）

### 4. 基准库

- **[MINLP-S89] QPLIB**（Math. Prog. Comp. 2019；读提交版预印本部分）：三字段分类码 OVC，两道级联过滤
  （剔除被至少 30% 的 complete 求解器在 30 秒内解出的实例等），不报告任何求解器对比，实例保持贡献者给出的
  原始形式、不做重构，以免偏向某类求解器（Sec. 1；Sec. 2.2.2；Sec. 3.2）。这是 13 人合著，**选题政策不能
  单独归为 Misener 的个人立场**。

## 心智模型（三重验证）

### 模型1 先刻画结构，再决定在哪里加强松弛 ✅三重通过

松弛上的投入要放在结构证明能带来收益的地方：先检测（sum decomposability、凸性、edge-concavity、RLT 方程、
参数化的分段结构），只保留严格占优的切割，或只在结构保证的子类上给出精确算法。

- **跨域复现**：求解器设计——[MINLP-S52]（sum decomposable 方程无法逐方程收紧；EC 刻面只在严格优于
  McCormick 时加入）、[MINLP-S53]（按可分多变量项而非整个方程组织松弛，§3.2.2）、[MINLP-S54]（五类特殊结构
  检测，§3.2）；复杂度理论——[MINLP-S80]（以 p 为参数的分段结构导出 strongly-polynomial 子类，§6）。
  两个不同的工作方向，四个不同 ID。
- **生成力**：遇到一类新的非凸约束，她会先问「这些方程是不是 sum decomposable？是的话，逐方程的聚合切割
  （EC 刻面、multiterm）不会更紧，应转向 RLT、跨方程切割或分段线性；只有连通的低维 edge-concave 聚合才值得
  计算刻面」。遇到久攻不下的经典难例，她会问「固定哪个参数后剩下的问题是 LP 或有解析结构，能否沿参数枚举
  breakpoints」。
- **排他性**：通用求解器的主流做法是做 factorable 重构后逐算子、逐项建松弛（Couenne 的双线性项用 McCormick
  [MINLP-S42]；SCIP 对双线性项用经典 McCormick [MINLP-S43]）。Bao–Sahinidis–Tawarmalani 的 multiterm 切割
  [MINLP-S65] 把多项聚合当作一般切割加入；[MINLP-S52] §3.1.3 则先论证这类聚合在过程网络品质平衡方程上
  无用，再决定不在那里花力气。
- **分级**：心智模型。说明：[MINLP-S53]/[MINLP-S54] 属同一求解器谱系，跨域性主要靠 [MINLP-S52] 的理论性质与
  [MINLP-S80] 的复杂度结果支撑。

### 模型2 公式是可切换的选项：紧度参数与编码分开看，由问题类上的基准裁决 ✅三重通过

- **跨域复现**：MINLP 松弛——[MINLP-S55]（线性/对数编码表示同一析取规划，紧度由 N_P 决定；大 N_P 对数编码
  占优，小 N_P 线性编码占优，pooling 取线性、N_P=4）、[MINLP-S52]（10 例中 8 例有利于线性编码；分段线性只
  推荐给特定类别）、[MINLP-S53]（分段线性默认关闭，难问题再手动开启，§3.3.4）；ML 嵌入——[MINLP-S81]
  （ReLU 的 big-M / complementarity / partition 可切换，§4）。两个不同领域。
- **生成力**：被问「对数编码还是线性编码」「big-M 还是 partition」时，她不会给出通用答案，而会说「紧度由
  分段数或公式族决定，编码只决定规模与求解行为；在目标问题类上把它们都实现成可切换选项，用基准裁决」。
  可检验的预测：分段数小的时候，二元变量更少的对数编码未必更快。
- **排他性**：[MINLP-S81] §4 自述，文献中常把这些公式当作竞争者，OMLT 则把它们做成备选。canon 中的对照
  做法是用理论支配关系推荐公式：MBM 被证明至少与 BM 一样紧且不增加变量与约束（[MINLP-S29] Thm 3.1）。
  Grossmann–Trespalacios 自己也承认 HR 更紧但未必更快（[MINLP-S28] Concluding Remarks），所以差别是默认
  取向上的程度之别，见「分歧与张力」第 7 条。
- **分级**：心智模型。

### 模型3 把数据驱动模型写成数学规划，用确定性优化求解 ✅三重通过

- **跨域复现**：BO 采集函数——[MINLP-S82]（树集成 + 距离不确定性写成 MIQP/MILP，用确定性全局求解器求解）；
  通用嵌入——[MINLP-S81]（NN、GBT 作为更大优化问题的目标或约束）。两个不同的算法设定。主页项目自述
  （"developing mathematical programming formulations of machine learning surrogate models"）是佐证，但不是
  canon 条目。
- **生成力**：面对以树模型或 ReLU 网络为代理的黑盒优化或决策问题，她会问「代理、不确定性度量和已知约束
  能不能精确写成 MILP/MIQP，交给确定性全局求解器」，而不是对采集函数随机采样，也不把已知约束留给惩罚项；
  模型大到通用求解器证不了最优时，她会转向定制的空间 B&B（[MINLP-S82] §4.0.2），而不是放弃确定性。
- **排他性**：树模型 BO 中常见的是用随机采样优化采集函数（[MINLP-S82] §1；同一采集函数的随机采样版本在
  实验中更差，§6.2）；DFO 主流把黑盒直接交给无导数求解器（[MINLP-S84]）。另一条数据驱动路线是 ALAMO
  （[MINLP-S83]，只读摘要）：用整数规划选出尽可能简单的代数代理，见「分歧与张力」第 5 条。
- **分级**：心智模型。边界：确定性全局最优只对采集子问题成立；[MINLP-S82] 没有收敛理论；与其他 BO 框架的
  对比有胜有负。

## 工作信条/启发式（未全过三重验证，按标准降级）

- **重节点而非大树**（未全过三重验证：跨域弱、排他性弱）：[MINLP-S53] §4.2.5 自述 GloMIQO 在每个节点做大量
  松弛与界收紧，SCIP 则靠大量分支生成大树；[MINLP-S52] 每个节点做 FBBT（加入 RLT 与 EC 冗余方程），OBBT
  只要明显收紧就继续。生成力成立（她会优先加强节点松弛与界收紧，而不是加快分支）。但证据集中在同一谱系，
  而且 BARON 同样把大量时间花在 probing 上（[MINLP-S42] §7.3：在超过 10 s 的实例上占 41%–99% 的 CPU 时间），
  这是部分全局求解器的共同取向，不是她独有。作者自己也不确定这一策略在小问题上是否划算（[MINLP-S53] §4.2.5：
  小算例上 SCIP 往往更快），如实保留为张力。
- **基准要自我审计**（未全过三重验证：排他性弱）：自建大规模测试集并画 performance profiles（[MINLP-S52]
  Fig. 1；[MINLP-S53] 399 题；[MINLP-S54] 2571 题）；统一可行性容差，用独立脚本复核求解器返回的点
  （[MINLP-S53] §4；[MINLP-S54] §5）。QPLIB 不做求解器对比、不重构实例（[MINLP-S89]，合著）。performance
  profiles [MINLP-S90] 与大型测试库 [MINLP-S88]、[MINLP-S3] 都是社区通行做法，所以排他性不足。
- **开源工具化**（未全过三重验证：排他性弱）：[MINLP-S80] 附作者代码（条目 notes 记 github.com/cog-imperial/
  StdPooling-PolyAlgos）；[MINLP-S81]、[MINLP-S82] 是开源 Python 工具；Scholar 兴趣标签含 Open-source Software。
  时间性矛盾：早期的 GloMIQO 经 GAMS 发布（[MINLP-S53] 条目 notes，转述 [MINLP-S54] §1），近期转向开源工具。

## 与其他成员的分歧与张力

### 自身工作内的张力（矛盾保留，不调和）

- **对数编码**：自称首个对连续非线性函数的对数规模松弛（[MINLP-S55] §4.2.2），却在 pooling 上推荐线性编码
  （[MINLP-S55] §7；[MINLP-S52] §4.3）。这是领域性矛盾：作者猜测需要更细分段的问题类会从对数编码获益，
  canon 中没有证实。
- **分段线性**：它提高过程网络在时限内解到全局最优的概率（[MINLP-S52] §4.3），但 GloMIQO 默认关闭它
  （[MINLP-S53] §3.3.4）。这是「有用但贵」的条件性取舍，作者两处说法一致，但默认配置与推荐场景并不重合。
- **从二次到一般 MINLP**：ANTIGONE 面向一般非凸 MINLP，作者却说它的实力核心在二次实例，在那里与
  GloMIQO 等价（[MINLP-S54] §5.8）。

### 与 Sahinidis

1. **多项聚合切割的适用面**（有文献记录）：Bao–Sahinidis–Tawarmalani 的 multiterm 松弛对二次约束中多个双线性
   项之和整体取凸包络，比逐项松弛更紧（[MINLP-S65]，只读摘要）。[MINLP-S52] §3.1.3 明确写道，过程网络的
   品质平衡方程是 sum decomposable，EC 聚合与 Bao 等人的 multiterm 切割都无法逐方程收紧。两者在定理层面不冲突
   （「更紧」只对非 sum decomposable 的和成立），分歧在于对适用面的判断。
2. **LP 多面体松弛 vs MILP 松弛**（推断）：BARON 路线把非线性凸松弛外逼近成完全基于 LP 的多面体松弛，理由是
   LP 求解器更快更稳，代价是 gap 更大（[MINLP-S37] §3.2；[MINLP-S38] §1）；后来又重新引入凸非线性松弛，并在
   搜索树的不同区域自动切换（[MINLP-S40]）。GloMIQO 的节点松弛是含分段二元变量的 MILP（[MINLP-S53] §3.3–3.4）。
   [MINLP-S40] §1 称 [MINLP-S38] 的 LP 型 branch-and-cut 框架后来被 ANTIGONE 等求解器采用——这是 Sahinidis
   一方的陈述，canon 中没有 Misener 一方的确认。
3. **凸性识别的深度**（推断）：ANTIGONE 不用复合规则（[MINLP-S54] §3.3）；Tawarmalani–Sahinidis 证明先分解为
   凸子表达式再外逼近更紧，可以自动利用凸性（[MINLP-S38] §2）；Khajavirad–Sahinidis 还为复合规则推不出凸性的
   中间表达式生成支撑超平面（[MINLP-S40] §1）。canon 中没有两人就此直接交锋的记录。
4. **αBB 与 factorable**（推断）：ANTIGONE 继承 Floudas 学派的 αBB，但只把它用于双线性项聚合体，作为五类结构之一，
   与项特定下估计并用（[MINLP-S54] §3.2）。这和 [MINLP-S49] §3.2 的结论一致：单个双线性项上 αBB 的最大分离距离
   不小于包络的分离距离，有已知包络时应优先用包络。她在实践上站在 αBB 与 factorable 包络的混合位置，
   而 BARON 一侧走 factorable 分解路线（[MINLP-S37] §3）。
5. **数据驱动代理的两条路**（推断）：ALAMO 用整数规划 best subset 学习「尽可能准确且尽可能简单」的代数模型，
   再用 DFO 自适应采样（[MINLP-S83]，只读摘要）；Misener 则把训练好的复杂模型（树集成、NN）原样编码进
   MIP（[MINLP-S81]、[MINLP-S82]）。前者让模型适应优化，后者让优化适应模型。canon 中没有直接交锋。
6. **基准对照与合作**（有记录）：GloMIQO 在 pooling 上与 BARON 大致相当（[MINLP-S53] §4.2）；ANTIGONE 与
   BARON 12.7.3 同台比较（[MINLP-S54] §5）。反过来，Puranik–Sahinidis 的域缩减开关实验因 ANTIGONE 无法关闭
   presolve 而没有纳入它（[MINLP-S39] §8 的实验设置）。两人同为 QPLIB 作者（[MINLP-S89]），这是合作，不是分歧。
   以上比较都是特定版本的快照。

### 与 Grossmann

7. **公式选择的默认取向**（推断，收敛多于分歧）：APOGEE 的两种编码都写成对同一析取规划的精确表示
   （[MINLP-S55] §4.1–4.2），与 GDP 体系共享析取视角。Grossmann 一方主要以紧度支配关系推进公式（HR 至少与 BM
   一样紧 [MINLP-S28] §3.3；MBM 至少与 BM 一样紧 [MINLP-S29] Thm 3.1），同时承认 HR 因规模增大并非总是更快
   （[MINLP-S28] Concluding Remarks）。Misener 一方把公式做成可切换的备选，交给基准裁决（[MINLP-S81] §4）。
   差别在默认取向（证明更紧 vs 交给数据），不是对立结论。

### 与 Burer

8. **多面体/MILP vs SDP/锥**（推断）：Misener 的松弛体系是多面体加 MILP（McCormick、EC 刻面、RLT、分段线性，
   [MINLP-S52]、[MINLP-S53]），Burer 一方以 SDP 与 copositive 表示为主（如 [MINLP-S57]、[MINLP-S58]）。canon 中关于
   这一权衡的证据来自第三方：box-QP 上 SDP 的根界 gap 比 RLT、BARON 小一个数量级，SDP+RLT 再小一个数量级，
   但代价悬殊（[MINLP-S59] §4）；支配性 SDP 松弛比弱松弛慢约三个数量级（[MINLP-S64]，只读摘要）。两条路线也有
   交汇：GloMIQO 使用特征向量投影（[MINLP-S53] §3.3），与 Saxena–Bonami–Lee 由特征向量导出的切割
   （[MINLP-S66]）思路相近；Burer–Saxena 也把 MIQCP 放在「MILP 之路」上处理（[MINLP-S63]）。canon 中没有两人的
   直接对比实验。

### 与 Dey

9. **pooling 的分段松弛、离散化与复杂度地图**（推断，不是直接交锋）：
   - Dey–Gupte 证明，任何事先给定的分段线性松弛方案在最坏情况下给出的界可达最优值的 n 倍（n 为 output 数，
     界是紧的；原文为最大化形式）（[MINLP-S76] Thm 1，proved-in-source）。APOGEE 用的正是固定 N_P 的事先分段
     （[MINLP-S55]），但它把分段松弛嵌入全局 B&B（[MINLP-S55] §5），[MINLP-S76] 的界约束的是松弛值本身，
     不是嵌入后的最终收敛。
   - 离散化（restriction，即内逼近）用来找可行解（[MINLP-S77]），APOGEE 的分段用来求界，两者功能互补。
   - 复杂度上，[MINLP-S80] 的 strongly-polynomial 子类依赖 Assumption 2.2（单一 quality、无容量约束、demand 固定）；
     [MINLP-S76] Thm 2 说明单 pool 情形难以近似（依赖 Alfaki–Haugland 归约与复杂性假设），[MINLP-S77] 汇总了单 pool
     的 NP-hardness（cited）。前提不同，结论不冲突；两边合起来描出 P/NP 边界的不同侧面。

### 与 Leyffer

10. canon 中没有 Misener 与 Leyffer 工作的直接对照。唯一的连线是：Burer–Letchford 综述记录 Leyffer 等人的
    branch-and-refine 用分段线性欠/过估计来保证不丢原问题可行解（[MINLP-S2] §4.4），与 Misener 把分段线性当作
    「松弛」而非「近似」来用的取向一致（推断）。

## 边界

- **未读部分**：[MINLP-S53] 的 §2 与附录 B；[MINLP-S54] 的补充材料；[MINLP-S55] 的 §2–§3（而且读的是 2010-12
  预印本，期刊版措辞与数字可能不同）；[MINLP-S80] 附录 A 的证明；[MINLP-S82] 附录 A–D；[MINLP-S89] 的 Sec. 2.3
  与附录。对照方的 [MINLP-S65]、[MINLP-S64]、[MINLP-S83] 只读摘要，涉及它们的对比只到摘要层级。
- **理论保证**：canon 没有记录 Misener 的任何收敛速率定理，也没有 GloMIQO/ANTIGONE 的收敛证明。她的
  proved-in-source 结果是：sum decomposability 的推论（[MINLP-S52]）、对数分段格式不被支配（[MINLP-S52] 附录 A）、
  pooling 子类的 strongly-polynomial 算法（[MINLP-S80]，限 Assumption 2.2）。[MINLP-S80] 中 NP-hard 一侧是
  cited-by-source 加 remark 级论证。语料不存精确常数；需要时应查原文。
- **经验结论的时效**：求解器比较都是 2010–2014 年版本的快照（[MINLP-S52]–[MINLP-S55]），使用作者自建基准与
  自有参数，不能外推到当前版本。ENTMOOT 的对比依赖固定超参数与 300 次评估预算（[MINLP-S82]）。
- **合著归属**：[MINLP-S89] 有 13 位作者，其选题政策不单独归于 Misener；[MINLP-S52]–[MINLP-S55] 与 Floudas 合著，
  [MINLP-S80]–[MINLP-S82] 是她在 Imperial 团队的合作工作。
- **canon 未覆盖**：主页与 Scholar 页上可见的鲁棒优化、可解释调度（argumentation）、Bayesian optimization 与实验设计、
  神经网络验证、ReLU 网络的 partition-based 公式、梯度提升树嵌入凸 MINLP、多维分段线性逼近以及她的综述类工作
  都不在 canon 内。本档案不据这些工作立论，蒸馏时也不得引用。
- **身份快照**：职位、讲席任期（2022-27）、Amazon Scholar 与 Scholar 页被引排序均为 2026-10-10 的快照。

# Ignacio E. Grossmann · MINLP Team 研究者档案

> 档案依据：语料中 Grossmann 署名的 10 个条目，外加 CMU 化工系个人页与
> Google Scholar 页（身份部分，核实日期 2026-10-10，verified-web）。各条目的阅读层级如下：
> - 读了全文：[MINLP-S14]（1989 EDRC 报告版）、[MINLP-S19]（1991 EDRC 报告版）、
>   [MINLP-S22]（2007-02-08 KiltHub 预印本）、[MINLP-S26]（1999/2000 作者预印本）、
>   [MINLP-S28]（2012 投稿版预印本）、[MINLP-S29]（2014 作者预印本）。这些都是报告或预印本，
>   期刊终稿均未逐页对照。
> - 读了部分：[MINLP-S3]（Springer 正式版，未读 §4 与附录）、[MINLP-S5]（2001/2002 预印本）。
> - **未读全文**：[MINLP-S12] 只读了摘要和出版社免费预览 pp. 307–308；
>   [MINLP-S25] 只有元数据，原文与摘要都没读到，内容全部来自同组后续文献的归属陈述。
>
> 页码均指上面所列版本。档案中凡是「推断」都已标出，其余陈述都来自 chunk 中已核实的 claim。

## 身份速览（verified-web）

- 核实日期 2026-10-10，https://www.cheme.engineering.cmu.edu/directory/bios/grossmann-ignacio.html
  （CMU 化工系个人页）：
  - 职位：Carnegie Mellon University 化学工程系 **Rudolph R. and Florence Dean University
    Professor**，曾任系主任；Center for Advanced Process Decision-making（CAPD，约 20 家
    石油、化工、工程与软件公司组成的工业联盟）成员、前主任。
  - 学历：Universidad Iberoamericana 学士（1974），Imperial College 硕士（1975）与博士（1977）。
  - 页面所列荣誉：美国国家工程院院士；多项 AIChE 奖（Computing in Chemical Engineering、
    Walker、Warren Lewis、Founders Award 等）；2015 年 IChemE 首届 Sargent Medal；
    英国 Royal Academy of Engineering International Fellow（媒体条目）；
    2026 INFORMS Saul Gass Award for Expository Writing（媒体条目，颁奖在当年 11 月年会）。
  - 页面自述的主要研究兴趣：discrete continuous optimization；化工过程与能源系统的
    最优综合与规划；供应链优化。
- 核实日期 2026-10-10，https://scholar.google.com/citations?user=fiZryxEAAAAJ&hl=en
  （Google Scholar）：姓名 Ignacio E. Grossmann，单位 Carnegie Mellon University，
  验证邮箱 cmu.edu，兴趣标签 Process systems engineering、optimization。
  引用数会变，不记录。
- 快照提醒：头衔、奖项与「已发表论文数」等都是 2026-10-10 的页面快照。

## 核心贡献

### A. 外逼近（OA）谱系：NLP 子问题与 MILP 主问题交替
- [MINLP-S12] Duran & Grossmann (1986)：这是 OA 的原点。**只读了摘要与 pp. 307–308。**
  - 问题类 P 是最小化形式，整数变量线性出现；f、g 为 C^1，在紧多面体凸集 X 上凸；
    U 为有限离散集（abstract; §1, pp. 307–308）。
  - 摘要原话：算法由 NLP 子问题与 MILP 主问题的松弛版本交替求解，构成一个有限序列，
    并给出收敛与最优性性质（abstract）。定理的精确陈述本档案未读到。
  - 核心机制：y 线性出现，所以连续可行空间是有限个紧凸区域的交，用支撑半空间的交来外逼近，
    即可得到与原问题等价的 MILP 主问题（§1, p. 308）。
  - 文末有与 GBD 的下界比较（abstract），但**哪一方更紧在所读文本中看不到**。
- [MINLP-S5] 2002 综述：把 B&B、OA、GBD、ECP、LP/NLP-BB 统一推导为三个 NLP 子问题
  （NLP1/NLP2/NLPF）加一个割平面 MILP 主问题，并说它们"essentially correspond to the
  basic subproblems of the Outer-Approximation method"（INTRODUCTION, p. 2）。
  - Property 3 **引自** Duran & Grossmann 1986（cited-by-source）：给定相同的 K 个子问题，
    OA 松弛主问题的下界 ≥ GBD 的下界。代价是 OA 主问题每轮加的约束更多（§III, pp. 10–11）。
    适用前提是 (P1)：f、g 凸且可微，X 为凸紧集，y 取多面体中的整数点。
- [MINLP-S19] Quesada & Grossmann (1992)：LP/NLP-based B&B，即单树 OA。读的是 1991 报告版。
  - 机制：只建一棵 LP 松弛的 B&B 树。遇到整数可行节点时，固定 0-1 变量解 NLP，得到上界
    和新的线性化，并把线性化加到所有未关闭的节点上，不必重启树（abstract p. 1; pp. 10–11）。
  - 有限终止（proved-in-source，是文字论证，不是形式定理）：0-1 构型有限，每解一次 NLP
    就割掉对应构型，所以不会循环（p. 12）。前提是 f、g 凸、0-1 变量有限。
    原文明说非凸扩展的两条剪枝准则"not rigorous"（pp. 17–18）。
  - 经验数据（报告版）：与原始 OA 用同样的线性化，B&B 节点减少 46%–84%；
    当时未自动化，没有比较 CPU 时间（pp. 19–20）。
- [MINLP-S22] Bonami, …, Grossmann, … (2008)：Bonmin 框架，共 11 位作者。
  - 实现了 B-BB、B-OA、B-Hyb 三种算法。B-Hyb 增强了 Quesada–Grossmann 方案，两种增强的
    极限分别退化为经典 NLP-BB 与经典 OA，所以 BB 与 OA 是同一混合族的两个极端（§3.3, p. 9）。
  - 早期实现、41 题、3 小时限时的实验中，B-Hyb 最稳健，但 Dicopt 在许多题上最快
    （§4, pp. 12–16）。这是经验结论，选题以 B-Hyb 为参照，可能偏向它。
  - Theorem 1 的准确表述：凸、二次连续可微并满足约束规范时，P 与 OA 主问题**最优值相同**，
    但最优解不一一对应；文中给出反例 Example 1（§2, pp. 3–5）。Theorem 1 本文未给证明。
- [MINLP-S3] Kronqvist, Bernal, Lundell, Grossmann (2019)：凸 MINLP 求解器的综述与基准。
  - 设置：MINLPLib（2018-07 版）的 335 个凸实例，16 个求解器共 20 种配置，相对间隙 0.1%，
    限时 900 s（§5）。
  - 结果：SHOT 解出 312 个，AOA 310 个，BARON 306 个；虚拟最好求解器 326 个，
    虚拟最差仅 39 个（§6, p. 422）。
  - 结论把单树方法的优势归于与 MILP 求解器的紧密集成：通过回调以 lazy constraints
    加入线性化（§7, p. 438）。
  - 度量刻意用 solution profiles，不用 Dolan–Moré 性能剖面（§6, p. 422）。
  - 以上都是 2018 年版本快照的经验数字。

### B. 非凸 MINLP：同一套机器作为明示的启发式
- [MINLP-S14] Viswanathan & Grossmann (1990)：AP/OA/ER，即 DICOPT++。读的是 1989 报告版。
  - 机制：在 OA/ER 主问题中加入增广罚函数，允许违反线性化，因此不必识别非凸性；
    等式按乘子符号松弛（PDF pp. 8–12）。
  - 作者明言没有全局最优保证。原话："Although the proposed method has no theoretical guarantee
    of finding the global optimum, it was able to locate global optima in virtually all test
    problems despite the presence of nonconvexities in the MINLP problem."（PDF p. 8）
  - 非凸时 MILP 不给有效下界，终止判据因此改为看 NLP 子问题目标值的进展（PDF p. 13）。
  - 18 个工程设计测试题全部找到已知全局最优，其中 11 题非凸（PDF p. 15, Table 1）。
    这是经验结果，不构成保证。
- [MINLP-S5]：非凸时 NLP 子问题可能有多个局部解，主问题不保证给出有效下界，全局最优可能被
  切掉（p. 14）。可选的路有三条：重构凸化、严格的全局方法（ε-收敛，昂贵）、启发式（代价小、
  不严格）（pp. 14–16）。作者把 DICOPT 对非凸问题的处理称为在许多问题上效果尚可的启发式
  （PDF 第 17 页）。
- [MINLP-S22]："For MINLPs with convex relaxation, this framework is an exact algorithm, but it can
  also be applied to nonconvex MINLPs as a heuristic."（§1, p. 2）

### C. 广义析取规划（GDP）：先写逻辑层，再选重构
- [MINLP-S25] Raman & Grossmann (1994)：**原文未读，只有元数据。**
  - 同组后续文献把 GDP 归于此文：lee2000gdp 写作"extension of the work of Balas (1985)"；
    GDP 模型包含 Boolean 变量、析取与逻辑命题（[MINLP-S26] p. 2；[MINLP-S28] §2.2 脚注 2）。
  - 同组文献对"起源"的措辞并不完全一致：[MINLP-S28] §1 同时引 Hooker & Osorio。
- [MINLP-S26] Lee & Grossmann (2000)：
  - 单个凸析取的凸包（式 (5)）由分解变量加 λ_j g_j(ν^j/λ_j) ≤ 0 构成，原文没有用 perspective
    一词。附录 A Theorem 2 给出证明梗概（proved-in-source）。前提是凸且有界、各项非空。
    原文称其"provides the tightest relaxation of the disjunctive feasible region"（p. 6）。
  - 「凸包重构的松弛下界 ≥ big-M」本文**没有证明**，只引 Lee & Grossmann (1999)
    （cited-by-source，p. 9）。
  - 实现时用 (λ+ε)g(ν/(λ+ε))，ε 约 1e-4，理由只是避免除以零，没有误差分析（pp. 7–9）。
  - 专用析取 B&B 的有限终止只有非形式化论证（p. 11 REMARKS）。
  - 例 6：用 OA 求解时 (PR) 反而比 (BM) 更耗时，40.91 s 对 13.47 s（p. 21）。
- [MINLP-S28] Grossmann & Trespalacios (2013)：GDP 到 MILP/MINLP 的系统转换教程。
  - 逻辑命题先转 CNF，再转 0-1 线性不等式；析取转成 BM 或 HR。
  - 「HR 松弛至少与 BM 一样紧」本文注明由 Grossmann & Lee 证明（cited-by-source，§3.3, p. 17）。
  - 非线性 HR 的奇异性用 Sawaya 的近似 (APP) 处理，该近似在 y∈{0,1} 处精确（§3.2, p. 16，引用）。
  - Basic steps（Balas 理论，引用）可以收紧 HR，代价是规模增长（§3.5）。
  - 结论原话："The former is smaller in size, but the latter exhibits stronger continuous
    relaxations, and hence stronger lower bounds, which may potentially translate into a more
    efficient solution times, although this is not always the case due to the increased size of
    the reformulation."（Concluding Remarks, p. 31）
- [MINLP-S29] Trespalacios & Grossmann (2015)：多参数 big-M（MBM）。
  - 每个其他析取项各取一个 M。Theorem 3.1（proved-in-source）：MBM 的连续松弛包含于 BM 的，
    且变量数与约束数不变（§3.1）。
  - 只有三项及以上的析取才可能严格更紧；所有析取都是两项时，MBM = BM（Remark 3.2）。
  - 10 个实例中有 9 个节点更少（§4.3）。
  - M 参数靠求解局部的小问题 (2) 得到（§2.3）。档案按语（unanchored）：(2) 是最大化问题，
    局部解的值只是其最优值的下界，要保证 M 有效需要最优值的上界。

## 心智模型（三重验证）

### 模型 1　把 MINLP 拆成「固定离散的 NLP + 线性化的 MILP 主问题」，离散搜索交给 MILP 机器 ✅三重通过
陈述：Grossmann 的默认分解方式是固定离散变量求解 NLP，用线性化（外逼近）构造 MILP 主问题，
离散组合的搜索交给成熟的 MILP 技术。其后的单树化（LP/NLP-BB）与混合化（B-Hyb）都是在这一骨架上
做的改造，不是另起炉灶。
- **跨域复现**：
  - 多树 OA 原点：[MINLP-S12] abstract。
  - 综述把五类方法统一推导为 OA 子问题加一个 MILP 主问题：[MINLP-S5] p. 2。
  - 单树 LP/NLP-BB：[MINLP-S19] abstract, pp. 10–11。
  - 非凸启发式仍沿用 OA/ER 主问题：[MINLP-S14] PDF pp. 9–12。
  - BB 与 OA 被组织成同一混合族的两端：[MINLP-S22] §3.3。
  - 2019 年基准把单树 OA 类的优势归于嵌入 MILP 求解器的回调：[MINLP-S3] §7, p. 438。
  - GDP 侧：对 (PR) 应用 OA，所得主问题与 logic-based OA 的主问题相同：[MINLP-S26] 附录 B。
- **生成力**：可检验的推断是，给他一类新的离散-连续问题（例如新的 GDP 结构），他会先问固定
  离散决策后的 NLP 子问题是什么、它的线性化能否构成有效的 MILP 外逼近，然后提出 OA 式分解
  或其单树版本，而不是从 NLP-based B&B 出发。
- **排他性**：相对的主流做法是在树的每个节点直接解非线性松弛的 NLP-based B&B。
  - Gupta & Ravindran 的 27 种 B&B 策略：[MINLP-S18]。
  - Leyffer 把 SQP 迭代与分支交织：[MINLP-S20]。
  - Fletcher & Leyffer 发现凸 MIQP 上 B&B 比 OA、GBD、QG 型 LP/QP B&B 快一个数量级，
    但限定在子 QP 极便宜的情形：[MINLP-S21] 的经验结论。
  - 线性 OA 的最坏例子会访问全部整数点，NLP-BB 一步即解：[MINLP-S13] §4, pp. 12–13。
- **分级**：心智模型。
- **演化（时间性）**：1986 年的多树 OA [MINLP-S12] → 1992 年的单树 [MINLP-S19] →
  2008 年的混合族 [MINLP-S22] → 2019 年实测单树、回调集成最快 [MINLP-S3]。骨架不变，
  集成程度逐步加深。

### 模型 2　先在逻辑层（Boolean + 析取）建模，再把「转成哪种 MI(N)LP」当作设计决策 ✅三重通过
陈述：离散-连续问题先写成带 Boolean 变量、析取与逻辑命题的 GDP。转成代数模型时用 BM 还是 HR，
是否做 basic steps，是否改用 MBM，这些都是有理论依据（松弛强度比较）和代价（规模）的显式选择，
而不是建模者的默认习惯。
- **跨域复现**：
  - GDP 的提出：[MINLP-S25]，二手归属。
  - 凸包松弛加专用析取 B&B：[MINLP-S26] 式 (5), pp. 10–12。
  - 系统转换教程与 basic steps：[MINLP-S28] §3。
  - 不加变量、不加约束的 MBM：[MINLP-S29] Theorem 3.1。
  - 综述中的 GDP 部分：big-M 松弛往往很弱，析取 B&B 下界更紧，例题根节点 62.48 对 15.08：
    [MINLP-S5] pp. 19–25。
  - 这些条目分属建模、B&B 算法、重构理论三个不同族。
- **生成力**：可检验的推断是，遇到「设备选或不选」「作业谁先谁后」这类开关或排序结构，他会先写
  ∨ 析取与 Ω(Y)=True，然后讨论 BM 与 HR 的紧度和规模，而不是直接写 0-1 加 big-M。
  [MINLP-S28] §2.4.3 对 job shop 就是这样做的。
- **排他性**：相对的主流做法是直接写代数 0-1 模型，开关结构用 big-M 表示。
  - [MINLP-S5] p. 19 自己说 big-M 是把 GDP 转成 MINLP「最直接」的方法。
  - Bonami 等人从指示约束而非 GDP 层出发，讨论 big-M 的可计算性、数值与松弛弱点：
    [MINLP-S32] §2.1。
  - Günlük & Linderoth 直接从指示变量推出 perspective 凸包：[MINLP-S30]。
- **分级**：心智模型。

### 模型 3　凸性是「精确」与「启发式」的分界线：越界照样交付，但明示降级 ✅三重通过
陈述：凸性假设下，他的方法有有限终止和最优性保证。越过凸性之后，他不放弃这套机器，而是改装后
作为启发式交付，并明确写出哪些保证丢了：下界不再有效、剪枝不再严格，终止判据也要改。
- **跨域复现**：
  - AP/OA/ER 明言无全局保证，终止改用 NLP 目标值的进展：[MINLP-S14] PDF pp. 8, 13。
  - 主问题不保证有效下界，DICOPT 是"效果尚可的启发式"：[MINLP-S5] pp. 14–17。
  - LP/NLP-BB 的非凸扩展"not rigorous"：[MINLP-S19] pp. 17–18。
  - Bonmin 在凸时精确，非凸时"as a heuristic"：[MINLP-S22] §1。
  - 2019 年的提醒：凸策略未必适用于非凸，不应据凸基准推断非凸表现：[MINLP-S3] §6.4, p. 437。
- **生成力**：可检验的推断是，给他一个非凸 MINLP，他会先把凸 MINLP 算法（OA/DICOPT 类）
  加上罚函数或松弛作为启发式求好的可行解，并在报告中声明无全局保证；只有在需要最优性证书时，
  才转向凸包络、欠估计加空间 B&B 一类的严格方法。[MINLP-S5] pp. 14–16 把这两条路并列。
- **排他性**：相对的做法是确定性全局优化学派，他们坚持 ε-全局证书。
  - branch-and-reduce 与 BARON：[MINLP-S35]、[MINLP-S36]，有限终止为 cited-by-source。
  - [MINLP-S37]、ANTIGONE [MINLP-S54]。
  - Burer & Letchford 在求解器分类中把 DICOPT 归入只能求启发式解的一类：[MINLP-S2] §6, p. 103。
- **分级**：心智模型。注意：这一立场与 Leyffer 共享。Fletcher & Leyffer 称算法可用于非凸问题，
  但不保证全局解（[MINLP-S13] §1, p. 2）；Leyffer 的 SQP-BB 也给出非凸启发式 2''
  （[MINLP-S20] §3.4）。所以它区分的是「凸 MINLP 学派」与「全局学派」，不是 Grossmann 个人独有。

## 工作信条（未全过三重验证）

- **紧度与规模的权衡要实测裁决**（跨域 ✅、生成力 ✅、排他性 ✗）：
  - 他自己的证据：HR 更紧但未必更快 [MINLP-S28] p. 31；(PR) 用 OA 时比 (BM) 更耗时
    [MINLP-S26] p. 21；MBM 在不增加规模的前提下收紧 [MINLP-S29]；部分代理约束把 LP 行数从
    131 降到 35 [MINLP-S19] pp. 19–20。
  - 排他性不过：同样的「节点减少但单节点变贵」观察也出现在 Leyffer 组 [MINLP-S24]
    （近似 perspective 重构）、Günlük–Linderoth [MINLP-S30]（Ipopt 每节点耗时剧增）和
    Bonami 等 [MINLP-S32] §5（凸包表述不一定转化为加速）中，是领域共识，不是他独有。
- **方法选择取决于问题特征，没有通吃的算法**（跨域 ✅、生成力 ✅、排他性弱）：
  - 他的证据：
    - 2002 年的定性预期：松弛紧时用 B&B，NLP 贵时用 OA，离散变量多且问题紧时 GBD 有效，
      以线性为主时用 ECP。原文明说"no systematic comparison"：[MINLP-S5] p. 17。
    - 2019 年按松弛间隙、非线性程度、离散密度分组的实测：[MINLP-S3] §6.1–6.4。
    - 2008 年不同实例族由不同求解器占优：[MINLP-S22] §4。
  - 排他性弱：Bonami–Kılınç–Linderoth 同样主张组合（portfolio）策略 [MINLP-S4]。
- **用松弛下界的支配关系作为比较语言**（跨域 ✅、生成力 ✅、排他性 ✗）：
  - 他的证据：OA ≥ GBD [MINLP-S5] Property 3（引用）与 [MINLP-S12] abstract（方向未读到）；
    GBD 的割是 OA 的代理割 [MINLP-S3] §3.5；HR ≥ BM [MINLP-S26] p. 9 与 [MINLP-S28] p. 17
    （都是 cited-by-source）；MBM ⊆ BM [MINLP-S29] Thm 3.1（proved-in-source）。
  - 排他性不过：这是整数规划的通用做法。例如 perspective 割与 perspective 松弛等价
    [MINLP-S30] §4.2，用区域体积比较 SDP 与 RLT [MINLP-S59] Thm 2。

## 矛盾与张力（如实保留）

- **本质性张力：「最紧」与「最快」不一致。**
  - 凸包被称为析取可行域"the tightest relaxation"（[MINLP-S26] p. 6）。
  - 同一篇文章里，(PR) 用 OA 时更慢（p. 21）；2013 年结论说更紧"not always"更快
    （[MINLP-S28] p. 31）。
  - [MINLP-S28] 的期刊摘要措辞（"often translates into shorter computational times"）比预印本
    结论更乐观。两种措辞并存，不调和。
  - MBM [MINLP-S29] 在原变量空间里收紧且不增加规模，在结构上可以看作对这一张力的回应。
    这是**推断**，原文没有这样定位。
- **理论更紧与实际更好也不一致（OA 对 GBD）。** OA 下界更紧，但每轮约束更多
  （[MINLP-S5] pp. 10–11）；他同时预期 GBD 在问题紧、离散变量多时可以有效（p. 17）。
  两个判断都保留。
- **时间性：基准方法论变了。**
  - 2008 年 [MINLP-S22] 用性能剖面（§4, Fig. 4）。
  - 2019 年 [MINLP-S3] 明确不用按最快求解器归一化的性能剖面，原话："We have not used performance
    profiles where the time is normalized with respect to best solver (Dolan and Moré 2002) since
    these are not necessarily good for comparing several solvers as noted by Gould and Scott (2016)."
    （§6, p. 422）
  - 两篇都是多作者论文，把这个转变归于 Grossmann 本人属于**推断**。
- **领域性：非凸问题的两种姿态。**
  - 1990 年的 AP/OA/ER 是无保证的启发式（[MINLP-S14]）。
  - 2013 年的 GDP 综述转述了非凸 GDP 先用凸包络或欠估计凸化、再做 basic steps 的两阶段严格下界法，
    非凸 HEN 下界提高 3.5%（[MINLP-S28] §3.5.3、§4，cited-by-source）。
  - 也就是说，在 GDP 方向他的组也做严格的界。语料里没有他的全局优化原文，无法判断两种姿态
    各自的比重。

## 与其他成员的分歧与张力

1. **与 Leyffer：OA 理论上的双向更正（有文献记录的交锋）。**
   - Fletcher & Leyffer (1994) 指出，Duran–Grossmann 的主问题（以 y∈Y 代替 y∈V）在出现不可行
     子问题时与原问题不等价，并给出一维反例；还指出 DG 的整数割只适用于二元变量
     （[MINLP-S13] §3, pp. 5–7）。[MINLP-S12] 只读了摘要，所以 DG 一侧的原文本档案无法复核。
   - Grossmann 署名的 [MINLP-S22] 反过来指出，[MINLP-S13] 的 Theorem 1 把等价性
     "incorrectly stated" 为「对 P 最优当且仅当对 P^OA 最优」，并用 Example 1 构造反例
     （§2, p. 4）。[MINLP-S22] 第一作者是 Bonami，共 11 位作者，把这一更正归于 Grossmann
     个人属于推断。
   - 双方共同沉淀下来的准确表述是：凸性与约束规范下最优**值**相同，有限步终止
     （[MINLP-S13] Thm 2；[MINLP-S22] §2.1 引 [MINLP-S13] Thm 2）。
2. **与 Leyffer：单树化的两个方向（推断，非交锋记录）。**
   - Grossmann 的单树从 LP 侧出发：只在整数可行节点解 NLP（[MINLP-S19]）。
   - Leyffer 的单树从 NLP 侧出发：把 SQP 迭代与分支交织，用 QP 不可行做隐式剪枝
     （[MINLP-S20] §3.1）。
   - 有记录的经验分歧：凸 MIQP 上，Fletcher & Leyffer 实测 B&B 比 QG 型 LP/QP B&B、OA、GBD
     快一个数量级，但作者自己限定该结论依赖子 QP 极便宜（[MINLP-S21]）。
   - Grossmann 合著的 2019 年基准显示，两类方法孰优随松弛间隙、非线性程度与离散密度而变
     （[MINLP-S3] §6.1–6.3）。
   - 交汇点：Leyffer 组的 Minotaur 把 Quesada–Grossmann 算法实现为 simple-qg
     （[MINLP-S24] §2, pp. 4–6；§3.1.3, p. 11）。
3. **与 Sahinidis、Misener（全局学派）：「凸问题该不该当非凸解」。**
   - Grossmann 合著的基准认为，全局求解器（ANTIGONE、BARON、Couenne、LINDO、SCIP）与凸求解器
     同台比较并不完全公平，部分全局求解器可能把凸函数当作非凸处理，生成不必要的弱松弛
     （[MINLP-S3] §6.4, p. 436）。同一基准中 BARON 仍是 BB 类解出最多的（306 个，§6, p. 422）。
   - ANTIGONE 的凸性检测只针对单项与二次聚合，可能识别不出复合凸结构（[MINLP-S54] §3.3），
     与上述提醒相互印证。这种联系是**推断**。
   - 方法论层面：他把 DICOPT 类非凸处理明示为启发式（模型 3），全局学派则以 ε-全局证书为目标
     （[MINLP-S35]–[MINLP-S37]）。
   - 有文献记录的交汇：Tawarmalani & Sahinidis 的对偶域缩减理论把 Zamora & Grossmann 的
     contraction 结果作为特例导出（[MINLP-S37] §4）。Zamora & Grossmann 原文不在语料内。
4. **与 Burer：事实无分歧，研究投入方向不同（推断）。**
   - Burer & Letchford 把 DICOPT、BONMIN 列为只能为非凸 MINLP 求启发式解的软件
     （[MINLP-S2] §6, p. 103），与 Grossmann 的自我定位一致（[MINLP-S5]）。
   - Burer 的工作明确不以全局求解为目标，而是构造强凸松弛与有效不等式（[MINLP-S63]）。
     Grossmann 侧重的是让离散-连续模型可解的分解与重构。
5. **与 Dey：「启发式」的标准不同（推断）。**
   - Grossmann 1990 年的 AP/OA/ER 没有质量保证，靠工程测试题上的经验表现（[MINLP-S14]）。
   - Dey & Gupte 的池化 MILP restriction 启发式有可证明的 n 倍质量保证（[MINLP-S76]，
     最大化形式，保证来自构造）。
   - 双方都借用 MILP 机器处理非线性问题，但对启发式应提供什么证明，要求不同。

## 边界

- **未读全文**：[MINLP-S12] 只读了摘要与 2 页预览，收敛定理、与 GBD 比较的方向及前提都未读到；
  [MINLP-S25] 只有元数据，GDP 起源的内容全部来自同组后续文献，标题中的 computational
  techniques 部分完全未覆盖。
- **版本**：[MINLP-S14]、[MINLP-S19] 读的是 EDRC 报告版，[MINLP-S5]、[MINLP-S22]、
  [MINLP-S26]、[MINLP-S28]、[MINLP-S29] 读的是预印本，期刊版的数字可能不同。
  例如 [MINLP-S26] 例 1 的 BM 松弛值在正文与表格中不一致，不要引用。
- **cited-by-source 不等于本档案核过证明**：OA ≥ GBD（Property 3）、HR ≥ BM（Grossmann & Lee）、
  basic steps 的紧化（Balas）、(APP) 近似（Sawaya）、Bonmin 中 QG 的有限收敛（引 1992 年文）
  都只是在所读文本中被引用。
- **语料空白**：
  - 他的严格全局优化原文（非凸 GDP、双线性等）不在语料内。
  - 规划调度、供应链、能源系统等应用主线（CMU 页面所列研究兴趣）不在本队章程内，未展开。
  - Lee–Grossmann 的 MIQCP 例子只作为 Saxena 等人的测试实例出现（[MINLP-S67]），不构成方法立场。
- **经验数字是快照**：[MINLP-S3]（2018 年版本）、[MINLP-S22]（早期 Bonmin）、[MINLP-S14]
  （18 题、IBM 主机）的数字都不能外推到其他版本或非凸问题。
- **身份信息是 2026-10-10 的页面快照**：头衔、奖项、学生数会过时；Scholar 引用数刻意不记录。

# Nikolaos V. Sahinidis · MINLP Team 研究者档案

> 档案依据：canon 中 12 个署名 Sahinidis 的条目——[MINLP-S7]（只读前言/目录）、
> [MINLP-S35]（摘要 + pp.107–108）、[MINLP-S36]（pp.201–202）、
> [MINLP-S37]（**全文**，2003-03 作者修订稿）、[MINLP-S38]（摘要 + pp.225–226）、
> [MINLP-S39]（**全文**，arXiv v1）、[MINLP-S40]（摘要 + pp.383–384）、
> [MINLP-S64]（**仅摘要**）、[MINLP-S65]（**仅摘要**）、[MINLP-S83]（**仅摘要**）、
> [MINLP-S84]（摘要 + §7–§8）、[MINLP-S89]（预印本 Sec. 1、2.2、3.1–3.3；13 位作者之一）。
> 只有 S37、S39 读了全文，**其余均未读全文**；首页预览、前言和摘要撑不住的内容，本档案
> 不越界补全。身份信息来自 Georgia Tech ISyE 个人页、组主页和 Google Scholar 页（核实
> 2026-10-10，verified-web）。所有论断都以语料构建阶段的 chunk 记录为准。全部问题按最小化
> 形式陈述。

## 身份速览（verified-web）

核实 2026-10-10，来源：
- https://www.isye.gatech.edu/users/nikolaos-sahinidis（ISyE 个人页）
- https://sahinidis.coe.gatech.edu/nick 与 https://sahinidis.coe.gatech.edu/research/global-optimization（Sahinidis Optimization Group 组主页）
- https://scholar.google.com/citations?user=PTXe50QAAAAJ&hl=en（curl 与 WebFetch 两次读取一致；组主页本身链接到这个 Scholar ID）

- **职位**：Georgia Tech **Gary C. Butler Family Chair and Professor**，任职于 H. Milton Stewart
  School of Industrial and Systems Engineering 与 School of Chemical and Biomolecular
  Engineering（ISyE 页、组主页 /nick 页）。Scholar 显示名为 "Nick Sahinidis"，邮箱已验证为
  gatech.edu。
- **学历**（ISyE 页）：Ph.D. Chemical Engineering（1990），Carnegie Mellon University；
  Diploma Chemical Engineering（1986），Aristotle University。所核页面没有写导师，本档案
  不作陈述。
- **学界职务**（快照）：ISyE 页称他是 Mathematical Programming Computation 的
  "current Editor-in-Chief"（组主页 /nick 页的同一段简介里没有这句话）；曾任 INFORMS
  Optimization Society Chair；在 AIChE 担任过多种职务。
- **奖项与荣誉**（快照，ISyE 页与 /nick 页一致）：NSF CAREER award、INFORMS Computing
  Society Prize、MOS 的 Beale-Orchard-Hays Prize、Computing in Chemical Engineering
  Award、Constantin Carathéodory Prize、Hellenic Operational Research Society 的
  National Award and Gold Medal；美国国家工程院（NAE）院士；AIChE Fellow、INFORMS Fellow。
- **研究自述**（ISyE 页原话节选）："theory, algorithms, and software for global
  optimization of mixed-integer nonlinear programs; informatics problems in chemistry and
  biology; process and energy systems engineering"。Scholar 列出的兴趣：Mixed integer
  nonlinear programming、Global optimization、Process systems engineering、Black-box
  optimization。
- **组主页对全局优化成果的自述**（global-optimization 页）：(a) 统一的 domain reduction
  框架；(b) convex extensions 理论及由此得到的包络（含分式规划的首个 SDP 松弛）；
  (c) "an entirely linear outer-approximation scheme for factorable nonlinear programs"；
  (d) 对某些连续非凸问题类的有限分支方案（标准 B&B 在这些问题类上只能极限收敛）；
  (e) 常见函数的凸/凹包络。页面写明的目标是 "to provide, through BARON, a precise and
  valuable computational tool to engineers and scientists"。这是组网页自述，不是 canon
  证据；下面的心智模型只以 canon ID 为证。
- **Scholar 快照**（2026-10-10，会过时）：总引用 24,533（2021 年起 8,921），h-index 65，
  i10-index 157。合作者列表中有 Mohit Tawarmalani，也有本队成员 Ignacio E. Grossmann。

## 核心贡献

### 一、branch-and-reduce 与 BARON（[MINLP-S35]、[MINLP-S36]、[MINLP-S7]）

- **[MINLP-S35]** Ryoo & Sahinidis 1996（读：摘要 + pp.107–108）：提出能缩小全局优化
  搜索空间的 valid inequalities 与 range contraction 技术，嵌入 B&B 后得到 branch-and-reduce
  算法（abstract）。问题写作 glob min f(x) s.t. g(x) ≤ 0, x ∈ X（§1）。动机原话：
  "By construction, relaxations developed over the resulting, smaller feasible spaces are
  tighter, and the convergence of the algorithm is accelerated"（§1, p.108）。计算覆盖
  工程设计、标准测试题、单变量多项式、线性 multiplicative、MINLP 与凹二次规划，并有面向
  多项式与 multiplicative 规划的专门算法（abstract）。"modest computational time" 只是
  作者对所解问题的定性评价。**可读页中没有出现**：对偶/marginals 机制（只有二手转述，
  见 S36 §2、S37 §4.3.1、S39 §6）；"feasibility-based range reduction" 这个名称（据 S37
  §4.3.2 出自 Shectman & Sahinidis 1998，不在 canon）。
- **[MINLP-S36]** Sahinidis 1996，BARON 软件说明（读：pp.201–202）：全局策略是常规 B&B
  加大量 range reduction 检验，这些检验 "are applied to every subproblem of the search tree
  in pre- and post-processing steps to contract the search space and reduce the relaxation
  gap"（§2, p.202）。许多检验基于对偶，前提是松弛 R 为凸、且求解算法同时给出对偶解（§2）。
  软件结构是通用 core 加专门模块：core 只需用户提供上下界子程序，但要编程；专门模块不需要
  用户编程（§3.1–3.2）。有限终止是 **cited-by-source**：引 [6]（= S35），ε > 0 时有限终止
  于 ε-全局最优；对"线性约束 + 凹目标"的问题类，引 Shectman & Sahinidis 证明 ε = 0 时
  也有限终止（§2）。证明不在所读页面上。
- **[MINLP-S7]** Tawarmalani & Sahinidis 2002 专著（只读前言与目录）：目标是 "to marry the
  advancements in solving nonlinear and integer programming models"，为 MINLP 设计实际
  高效的全局算法（Preface, p.xiii）。作者自述的贡献（证明在正文，**未读**）：凸包络的
  构造性刻画（第 2 章）；乘积分解，类比 MILP 的变量分解（第 3 章）；完全线性的 NLP/MINLP
  松弛（第 4 章）；range reduction 的统一框架，联系到 Lagrange 外逼近，并覆盖 IP 与 CP
  文献中的域缩减（第 5 章）；§7.6.4 的分支方案对若干问题类保证有限终止（Preface,
  pp.xiv–xv）。序言称 BARON 是 "the first branch-and-bound framework for MINLPs"，这是
  作者自述，未经独立核实。

### 二、factorable 松弛的多面体化（[MINLP-S37]、[MINLP-S38]、[MINLP-S40]）

- **[MINLP-S37]** Tawarmalani & Sahinidis 2004（**全文**）：问题为 factorable MINLP，
  min f(x, y) s.t. g(x, y) ≤ 0, x ∈ X, y ∈ Y ⊆ Z^p（§2）。Algorithm Relax 把 factorable
  函数递归分解为单变量函数、双线性项（凸/凹包络，引 McCormick 1983 专著与 Al-Khayyal &
  Falk [MINLP-S34]）、分式项（product disaggregation）和多线性项（递归区间算术）；再对
  得到的非线性松弛做多面体外逼近，"thus generating an entirely linear programming based
  relaxation"（§3.2）。
  - **Theorem 3.4（proved-in-source）**：对区间上的单变量凸函数，采用作者的 projective
    error rule 时，sandwich 算法达到给定 projective 误差所需的支撑线数有显式上界；作者
    据此称逼近误差关于外逼近点数**二次收敛**（§3.2）。假设：单变量凸函数，两端切线相交
    （否则把曲线切成两段），误差按 projective error 度量。这是逼近误差的阶，**不是**
    B&B 的整体复杂度；常数与 N(k) 的表达式须查原文。§5.2：若分支点按 bisection、
    projective 等规则之一选取，沿某变量轴划分 n 次后，该单变量凸函数的逼近误差按 1/n²
    的阶下降（常数须查原文）。
  - **Theorem 4.1（proved-in-source）**：设 T 为 min f(x) s.t. g(x) ≤ b, x ∈ X，b0 是最优值
    的上界。对某对偶乘子 y ≤ 0 求出 Lagrangian 子问题的下确界后，对每个 y_i ≠ 0，割
    g_i(x) ≥ (b0 − inf_x l(x, y))/y_i 不会割掉 T 的任何最优解（§4.3.1）。由此可导出
    [MINLP-S35] 的割、probing、marginals-based 缩减、Zamora & Grossmann 的 contraction；
    逐约束的 feasibility-based 缩减也是 LP 对偶的特例（§4.3.2）。新方法有 duality-based
    reduction 与 learning reduction（§4.4）。与 S35 割的比较依赖凸松弛的强对偶（作者写
    "Assuming that appropriate constraint qualifications hold"）。
  - 计算（empirical，§7）：BARON 在可分凹 QP、基数约束 0-1 双曲规划和 minlplib MINLP 上
    的结果。作者称所报告的问题都在容差内收敛到全局最优，其中 nvs02/14/20/21 的解优于原始
    文献的报告值（§7.3）。条件：332 MHz RS/6000，绝对容差 1e-6（Table 2 用相对容差 0.1）。
- **[MINLP-S38]** Tawarmalani & Sahinidis 2005（读：摘要 + pp.225–226）：节点上不直接解
  非线性凸松弛，而是用凸松弛的支撑超平面构造多面体松弛、解 LP；理由是当时的 NLP 代码
  比 LP 慢，而且数值不稳定（abstract）。作者明确承认代价：凸函数的多面体松弛往往比其来源
  的非线性凸松弛 gap 更大（§1, p.225）。§2 的证明（proved-in-source，定理全文未读）：
  "the outer approximation of a decomposed equivalent is tighter than the direct outer
  approximation of the original multivariate problem"（§1, p.226）。设定为 f_i 凸，g_j 凸且
  在非仿射 f_i 的值域上非减（Proposition 1）。计算（摘要层面）：在 globallib 与 minlplib
  的 87 题上算根节点松弛，用 BARON 7.2 全局求解其中 26 题；割平面使根节点 gap 最多缩小
  100%，并常使求解加速几个数量级。"最多 100%" 是最好情形，不是平均值。
- **[MINLP-S40]** Khajavirad & Sahinidis 2018（读：摘要 + pp.383–384）：把多面体松弛与凸
  非线性松弛结合，配 fail-safe 技术，在 B&B 每个节点做凸性识别，并用学习策略在搜索树的
  不同区域自动选择和切换两种松弛（以及不同的局部搜索算法）（abstract）。切换判据的具体
  内容在可读页中没有出现。另外，对凸性不能由 factorable 复合规则推出的中间凸表达式，
  生成支撑超平面来加强松弛（§1, p.384）。计算：在 GlobalLib、MINLPLib、PrincetonLib、
  IBMLib 上，500 s 内可解到全局最优的问题数增加 30%（abstract；硬件与容差 not stated）。
  §1 对前作的回顾（cited-by-source）："while polyhedral relaxations introduce larger
  relaxation gaps compared to the convex relaxations from which they are derived, the
  superior performance and robustness of LP solvers significantly improves the reliability
  of LP relaxation-based global solvers"。作者还称 [MINLP-S38] 的框架后来被 Couenne、
  GlobSol、SCIP、ANTIGONE 采用（作者陈述）。

### 三、域缩减理论与计算（[MINLP-S39]，并见 S35/S36/S37）

- **[MINLP-S39]** Puranik & Sahinidis 2017（**全文**）：顶层分类是"删除不可行域"（§5）与
  "删除次优域"（§6）。作者特意把通常所称的 OBBT 归入 feasibility-based，因为它只删除
  不可行区域（§5）。立场是计算上关键、理论上不必需："While these techniques are not
  necessary to ensure convergence to the global optimum, they typically speed up
  convergence."（§1, p.2）。§5.3 进一步指出：与 CP 不同，有了 relaxation，数学规划型 B&B
  不建立任何 consistency 也能收敛。
  - 计算（empirical，§8）：在 1740 题上比较 BARON、Couenne、SCIP 的默认设置与关闭域缩减
    两种设置。关闭后三者性能都大幅恶化；在 MINLP 库上，BARON 连好的可行解都找不到；即使
    关闭，BARON 仍优于另两者；SCIP 对域缩减的依赖更强（§8.4）。条件：500 s，容差 1e-6；
    只比较全开与全关，不评估单项技术。
  - marginals 型缩减（cited-by-source，§6 式 (22)–(25)）：凸松弛最优值为 L、上界为 U，若
    上界约束 x_j ≤ x_j^u 起作用且乘子 λ_j > 0，可令 x_j^l ≥ x_j^u − (U − L)/λ_j。式 (22)/(23)
    只需当前松弛解，能在每个节点廉价执行；probing 要解 2n 个凸问题。

### 四、QCQP 松弛：多项割与 SDP 比较（[MINLP-S65]、[MINLP-S64]，**均仅摘要**）

- **[MINLP-S65]** Bao, Sahinidis & Tawarmalani 2009：对二次约束中多个 bilinear 项之和整体
  取凸包络（multiterm），因此比 "standard termwise relaxation of the bilinear functions"
  给出更紧的界。方法以多线性函数的凸包络为出发点，构造 QCQP 的多面体松弛，并用
  cutting-plane 算法实现（abstract）。摘要没有量化代价。
- **[MINLP-S64]** Bao, Sahinidis & Tawarmalani 2011：理论分析表明，doubly nonnegative SDP
  松弛等价于"Shor 松弛 + partial first-order RLT"，且二者支配文中另外六种 SDP 松弛
  （abstract；被支配者名单、证明与前提都没有读到）。计算：在 700 个随机实例（至多 60 个
  变量）上，"the two dominant relaxations require three orders of magnitude more
  computational time than the weaker relaxations"；它们的平均 gap 约 3%，较弱松弛最高约
  19%。由 Lagrangian 松弛导出、在原问题中加冗余非线性约束的 SDP 松弛，平均 gap 约 13%，
  只需几 CPU 秒（abstract）。**注意**：已核实的是 SDP 松弛之间的比较，不是 SDP 与多面体
  松弛的比较。

### 五、黑箱/代理建模与基准（[MINLP-S83]、[MINLP-S84]、[MINLP-S89]）

- **[MINLP-S83]** Cozad, Sahinidis & Miller 2014（**仅摘要**）：ALAMO 用基于整数规划公式的
  best subset 技术，从大量候选函数成分中选模型项；再用 DFO 求解器自适应地选新采样点，
  系统地改进模型（abstract）。目标是用少量模拟或实验数据学到 "as accurate and as simple
  as possible" 的模型（abstract）。与其他方法比较的具体结论没有读到。
- **[MINLP-S84]** Rios & Sahinidis 2013（读：摘要、§7–§8）：在 502 个 bound-constrained
  问题上比较 22 个 DFO 软件，全局最优由 BARON 求得（含三角函数等的问题改用 LINDOGLOBAL）。
  主要发现：所有求解器的解质量都随规模增大而下降；在 2,500 次函数评估的预算内，几个全局
  求解器即使在凸问题上也优于局部求解器（凸光滑问题上的 NEWUOA、BOBYQA 例外）；没有求解器
  全面占优（abstract；§7.4、§7.7；§8）。条件：确定性目标、只有界约束、2012 年前后的软件
  版本；§8 明言没有处理噪声与一般约束。
- **[MINLP-S89]** Furini 等 2019（13 位作者之一）：QPLIB 的 OVC 分类码、两道过滤（例如
  剔除被至少 30% 的 complete 求解器在 30 s 内解出的实例）、不对实例做重构（Sec. 2.2.2、
  3.1–3.3）。这是集体文章的库政策，**不能**当作 Sahinidis 个人立场引用。

## 心智模型（三重验证）

### 模型1 多面体优先：用 LP 的稳健换取松弛间隙 ✅三重通过
在全局 B&B 的节点上，宁可把非线性凸松弛外逼近成 LP、接受更大的 gap，也要换来 LP 求解器
的速度、可靠性和对偶信息。
- **跨域复现**：factorable MINLP 的完全 LP 松弛 [MINLP-S37]（§3.2："nonlinear programs are
  harder to solve and are associated with more numerical issues than linear programs"）；
  多变量凸函数的多面体 branch-and-cut [MINLP-S38]（abstract；§1 承认 gap 更大）；QCQP 的
  multiterm 多面体切割 [MINLP-S65]（abstract）；专著第 4 章的自述 [MINLP-S7]（Preface）。
  涉及三个问题族、四个 canon ID。外部描述与此吻合：Burer & Letchford 称 branch-and-reduce
  通常用 LP 松弛，理由是 LP 更高效、数值更稳定、灵敏度信息更易得 [MINLP-S2]（§4.2, p.100）。
- **生成力**：遇到一类新的非凸结构，他会问"它的凸松弛能不能用支撑超平面外逼近，让节点
  上只解 LP？"，而不是直接把一个凸 NLP 放进节点。
- **排他性**：αBB 在每个子盒上用局部 NLP 求解器（MINOS）解凸松弛 (R) [MINLP-S49]
  （§2–§4）；凸 MINLP 的 NLP-BB 在节点上解 NLP [MINLP-S20]、[MINLP-S22]（B-BB）；
  Burer–Vandenbussche 的 B&B 在节点上解 SDP，并论证在 KKT-branching 下 LP 松弛无界、不能用
  [MINLP-S58]（abstract；Cor 2.3）。
- **时间性矛盾（保留）**：2018 年的 [MINLP-S40] 把凸非线性松弛**重新引入** BARON，在树的
  不同区域自动切换 LP 与 NLP 松弛（abstract）。所以后期的立场是"以 LP 为主、按需切换"，
  不是"只用 LP"。切换判据没有读到。
- **分级**：心智模型。

### 模型2 域缩减是一等公民（branch-and-**reduce**）✅三重通过
除了分支本身带来的缩小，每个节点都要主动收紧变量界：界越紧，松弛就越紧，收敛也越快。
对偶信息（乘子）是收紧变量界的主要燃料。
- **跨域复现**：原始算法 [MINLP-S35]（abstract；§1, p.108 原话见上）；软件在每个子问题上
  做前/后处理检验，许多检验基于对偶 [MINLP-S36]（§2）；Lagrangian/LP 对偶的统一理论与
  Theorem 4.1 [MINLP-S37]（§4）；跨 BARON、Couenne、SCIP 的开关实验 [MINLP-S39]（§8）。
  这四个 ID 分别对应算法设计、软件、理论和计算评估。
- **生成力**：全局求解器在某个实例上卡住时，他会先问"每个节点做了哪些域缩减？松弛的
  乘子有没有拿来收紧变量界？"，然后才去看分支规则。
- **排他性**：在主流空间 B&B 里，缩小只来自分支本身。Burer & Letchford 正是以此为参照来
  定义 branch-and-reduce："attempts to reduce the domains of the variables, beyond the
  reductions that occur simply as a result of branching" [MINLP-S2]（§4.2）。
- **自我限定（保留）**：同一研究线明言域缩减 "not necessary to ensure convergence"
  [MINLP-S39]（§1；§5.3）。所以这条模型讲的是计算上必需，不是理论上必需。
- **分级**：心智模型。

### 模型3 紧度要和代价一起、在大型基准库上定价 ✅三重通过
一个松弛或一项技术值不值，不看"理论上更紧"，而看在数百到上千个实例上"紧了多少、贵了
多少"的净效果。
- **跨域复现**：SDP 松弛中，支配性松弛贵三个数量级，平均 gap 约 3%，较弱者最高约 19%
  [MINLP-S64]（abstract）；1740 题上的域缩减全开/全关实验 [MINLP-S39]（§8）；LP/NLP 混合
  使四个库上 500 s 内可解题数增加 30% [MINLP-S40]（abstract）；87 题上的根节点 gap 计算
  [MINLP-S38]（abstract）；DFO 领域在 502 题上比较 22 个求解器 [MINLP-S84]（§7）。证据横跨
  QCQP 松弛、域缩减、松弛类型选择和无导数优化四个族。
- **生成力**：拿到一个更紧的新松弛，他会问"它在 GlobalLib/MINLPLib 上每个节点贵多少？
  固定时限内能多解几题？"，并且准备好接受"更紧但不值得"的结论。
- **排他性**：对照的是只证明包含/支配关系、不计代价的松弛理论路线，例如 QCQP 的 SDP
  精确性目录 [MINLP-S63]（§2.5）、SDP 紧性条件 [MINLP-S69]（§4 Thm 1–2；§5 Thm 3）。这些工作并不反对计价，差别
  在于侧重点（推断）。
- **分级**：心智模型。

### 模型4 在通用非凸求解器中自动识别并利用凸性 ✅三重通过
不要把整个问题都当成非凸。先分解表达式，找出凸子结构，再按凸结构的方式松弛，而且由
求解器自动完成，不靠用户声明。
- **跨域复现**：先分解再外逼近比直接外逼近更紧，不需要显式识别原问题的凸性，还能利用
  非凸表达式中凸子表达式的凸性 [MINLP-S38]（abstract；§2）；在 B&B 每个节点做凸性识别
  [MINLP-S40]（abstract）；对凸性不能由 factorable 复合规则推出的中间凸表达式生成支撑
  超平面 [MINLP-S40]（§1）；单变量凸/凹包络与 sandwich 外逼近 [MINLP-S37]（§3.1–3.2）。
- **生成力**：面对一个混有凸项和非凸项的模型，他会问"哪些中间表达式其实是凸的？能不能
  只为真正非凸的部分付出松弛代价？"
- **排他性**：canon 里有直接对照。Kronqvist 等指出，部分全局求解器可能把凸函数当作非凸
  处理，从而生成不必要的弱松弛 [MINLP-S3]（§6.4, p.436）；ANTIGONE "detects convexity in
  individual terms and aggregates of quadratic terms; it does not, at this writing, apply
  function composition rules or symbolic methods" [MINLP-S54]（§3.3）。
- **时间性矛盾（保留）**：1996 年的 BARON core 要求用户编程提供上下界子程序，自动化只来自
  若干专门模块 [MINLP-S36]（§3.1–3.2）；S35 也为多项式和 multiplicative 规划开发了专门算法
  （abstract）。"通用、全自动"是后来演化出的方向，不是起点。
- **分级**：心智模型。

## 工作信条/启发式（未全过三重验证，按标准降级）

- **统一框架：把既有技术证成同一框架的特例** —— S37 §1 称多种既有域缩减方案 "are special
  cases of our approach"；专著第 5 章自述统一处理 IP 与 CP 文献中的域缩减 [MINLP-S7]
  （Preface）；SDP 松弛之间的等价与支配排序 [MINLP-S64]（abstract）。跨域复现和生成力都过
  （遇到一族同类技术，他会问"谁是谁的特例、谁支配谁"）；**排他性弱**，因为统一化在数学
  规划理论中很普遍。降级。
- **MINLP 是非线性规划与整数规划的"联姻"** —— [MINLP-S7] 序言原话 "to marry the
  advancements in solving nonlinear and integer programming models"；乘积分解类比 MILP 的
  变量分解（Preface）；S37 把 IP 的 probing 等域缩减纳入统一理论（§4）。**排他性不过**：
  Burer & Saxena 的 "MILP road to MIQCP" [MINLP-S63] 同样主张把 MILP 技术推广到 MIQCP。
  降级，也可视为本队的共识点。
- **有限终止优于极限收敛** —— 主张对某些问题类设计能保证有限终止的分支方案。S36 §2 是转引
  （ε = 0 的情形引 Shectman & Sahinidis，不在 canon），S7 序言提到 §7.6.4（未读）。两处都是
  自述或转引，所读文本里**没有证明**，跨域复现不成立。对照：Horst & Tuy 指出全局 B&B 一般
  产生无限过程 [MINLP-S44]（Preface）。降级。
- **黑箱问题选最简单的代数模型** —— 用整数规划做 best subset，追求 "as accurate and as
  simple as possible" [MINLP-S83]（abstract）。只有一个 canon ID，且只读了摘要。降级。

## 与其他成员的分歧与张力

除非另行注明，下面都是 canon 证据之间的对照，不是有记录的直接交锋；标"推断"的是本档案
的解读。

- **与 Burer：多面体还是 SDP（紧度与代价的张力）**。Burer–Vandenbussche 认为 KKT-branching
  下 LP 松弛无界，"a fact that precludes their use"，因此改用 SDP 松弛 [MINLP-S58]
  （abstract）。Burer & Saxena 转述：加入 PSD 后的析取割在 67/129 个实例上闭合超过 98% 的
  gap [MINLP-S63]（§4.2）。Sahinidis 一侧量化了强 SDP 松弛的代价，贵三个数量级
  [MINLP-S64]。Anstreicher 的 box-QP 实验中，RLT、BARON、PS 的根节点界相近，SDP 的 gap 小
  一个数量级，代价也高得多 [MINLP-S59]（§4）。双方对"哪个更紧"的事实没有争议，分歧在于
  给代价多大权重（推断）。
- **与 Misener：multiterm 切割的适用范围；αBB/分段线性 vs 纯 LP**。Misener & Floudas 证明，
  对 sum-decomposable 方程（如 pooling 的品质平衡），逐项 McCormick 已经是凸包，所以 Bao
  等人的 multiterm 切割无法逐方程收紧，应改用 RLT、专门设计的切割或分段线性松弛
  [MINLP-S52]（§3.1.1、Property 3.1.3.1）。这是 canon 中对 [MINLP-S65] 适用范围的直接限定。
  ANTIGONE 与 BARON 的基准比较是 Misener 一方的自报结果，ANTIGONE 的强项在二次问题
  [MINLP-S54]（§5.8）。另一方面，Khajavirad & Sahinidis 称 ANTIGONE 采用了多面体
  branch-and-cut 框架 [MINLP-S40]（§1，作者陈述）。两条路线既有汇合，也有竞争。
- **与 Dey：LP 型全局求解在大规模 pooling 与 OPF 上的极限**。Dey & Gupte 的 MILP restriction
  启发式在大实例上用少得多的时间给出好得多的解，而 BARON 在大实例上明显退化
  [MINLP-S76]（abstract；§5）；Gupte 等的结论类似 [MINLP-S77]（§5.2），同文还引 Tawarmalani
  & Sahinidis (2002) 已证明 McCormick 版 p-relaxation 的 z^p ≤ z^pq [MINLP-S77]
  （Proposition 3.2 附近）。在 OPF 上，Kocuk–Dey–Sun 证明两种 McCormick（LP）松弛都弱于
  SOCP 松弛 [MINLP-S74]（Thm 3.1、§3.3），并发展了基于 SOCP 的空间 B&C [MINLP-S75]。这是对
  模型1的领域性限定：在某些问题族上，锥松弛值得付出代价（推断）。
- **与 Leyffer / Grossmann（凸 MINLP）：节点上放 LP 还是 NLP**。Kronqvist 等的凸 MINLP
  基准显示，非线性程度高时 NLP-BB 类求解器反超依赖线性化的求解器 [MINLP-S3]（§6.2）；同一
  基准中，BARON 在 BB 类里解题最多（306），单树的 SHOT/AOA 总体最快 [MINLP-S3]（§6）。凸
  MINLP 一侧也在向 LP 主问题靠拢：LP/NLP-BB [MINLP-S19]，以及 [MINLP-S1] 所说多树方法的动机
  是 NLP 难以热启动（§3.2）。在"LP 稳健"这一点上与模型1汇合（推断）。Leyffer 等在多线性
  项上用超立方体凸包代替逐项 McCormick [MINLP-S91]（Sec. 4.2），与 [MINLP-S65] 的 multiterm
  思路方向一致（推断，没有直接交流记录）。
- **与 Grossmann：严格全局还是廉价启发式**。Grossmann 的综述把 branch-and-reduce 等严格
  全局方法定性为只有 ε-收敛、计算昂贵，并把 DICOPT 等列为代价小得多的非严格启发式
  [MINLP-S5]（Handling of nonconvexities, pp.14–16）。Sahinidis 一侧的立场是严格全局求解在
  实践中可行（S35 abstract；S37 §7.3 解出了比原文献更好的 nvs 解）。两人也有交集：
  [MINLP-S5] 的 Property 4 引 Sahinidis & Grossmann 1991 的 GBD 收敛性质（cited-by-source），
  Scholar 合作者列表中也有 Grossmann。分歧在于严格性值不值这个代价（推断）。

## 边界

- **未读全文**：S35、S36、S38、S40 只读了 Springer 首页预览，S7 只读了前言，S64、S65、S83
  只读了摘要，S84 只读了 §7–§8，S89 是部分阅读。Theorem 3.4 与 Theorem 4.1 的精确常数和
  完整假设须查 [MINLP-S37] 原文。S38 的"分解后外逼近更紧"定理和 S40 的切换判据都没有读到。
- **归属冲突（需核对）**：S37 §4.3.1 把割 g_i(x) ≥ (U − L)/y_i* 归于 Ryoo & Sahinidis 1996
  的 Theorem 2；S39 §6 则把变量界乘子割（式 22）归于 Ryoo & Sahinidis 1995（Comput. Chem.
  Eng.）的 Theorem 2，而 1995 年那篇不在 canon。
- **McCormick 双线性包络**不能锚定到 [MINLP-S33] 的具体位置（该条目的可读页里没有）。S37 与
  S39 对它的归属都是转引。
- **QPLIB [MINLP-S89]** 是 13 位作者的集体政策，不代表 Sahinidis 个人立场。
- **canon 未覆盖**：他在不确定性优化、两阶段随机整数规划、生物信息学、分子设计等方面的
  工作；后期 MIQP 的 spectral 松弛与 "SDP-quality bounds via convex quadratic relaxations"
  （组网页书目列于 2021–2022 年，**未入 canon**，内容未读），因此本档案对他在 SDP/二次松弛
  上的后期立场不作判断；与本队成员 Dey 的合作（组网页书目列有 Li, Dey & Sahinidis 2024，
  gas network design，**未入 canon**）。
- **快照**：职位、主编身份、奖项和 Scholar 指标都是 2026-10-10 的页面快照，会过时；
  "current Editor-in-Chief of Mathematical Programming Computation" 只出现在 ISyE 页上。

# LP Team · 决策启发式

每条 = 触发场景 → 规则 → 依据（ID 与锚点）。这些是「按本语料来源行事的对偶单纯形开发者」会用的设计规则；
凡来源没写的阈值或开关，条目里明说「未说明」，不从领域惯例补。

## H1 串行一流，是谈并行的前提
- **场景**：要并行化一个单纯形代码，或评估别人报的并行加速。
- **规则**：(a) 先确保串行基线是高效实现——稀疏 LU、超稀疏求解、FT 类更新、DSE 与 BFRT；(b) 并行加速只相对这样的基线报；
  (c) 若现有公开代码要么太复杂难扩展、要么太简单不值得并行，就从零写（HSOL/hsol 的做法）。
- **依据**：组件串行高效，并行求解器才有实用价值；早期许多并行实现因串行低效而有更大并行余地，结果整体不如好的串行求解器
  [LP-S6 §3, PDF pp. 5–6]；新的计算发展须在高效实现里检验，只在低效实现里有效的 "not worthy of attention" [LP-S2 §2, PDF p. 3]；
  hsol 从零实现 [LP-S2 §1, PDF p. 2; LP-S1 §1, PDF p. 17]。反面案例：Shu 的高加速据 Hall 综述来自老式列式 PRICE 的大份额
  [LP-S53，据 LP-S1 §4.1.2, PDF p. 73]；ParISS 8 核仍平均比 Clp 1.06 慢 2.1 倍（LP-R22）。

## H2 先剖面，再按 Amdahl 定并行预算
- **场景**：决定并行哪些组件、开几个核。
- **规则**：(a) 先测各组件的耗时份额与超稀疏结果的发生率（LP-R1）；(b) 用 Amdahl 定律估上界，按上界而非硬件核数定目标（论文因此选 8 核，LP-R2）；
  (c) 便宜的组件留串行：CHUZC2 平均只占 1.5%、每次迭代几十微秒，并行化的同步开销不值 [LP-S1 §4.3.2, PDF pp. 81–82]；
  (d) 工作量微小时动态关掉并行：论文以 ê_p 密度 1% 为界关掉 PRICE/CHUZC 并行 [LP-S1 §4.3.2, PDF pp. 82–83]，期刊版对超稀疏向量在密度低于
  5%–10% 时退回串行，并称性能对该阈值不敏感（未给数据）[LP-S2 §3.4, PDF pp. 14–15]。
- **代价**：超稀疏 LP 上 CHUZR、PRICE、CHUZC 乃至 UPDATE-PRIMAL 都会串行执行，计入 Amdahl 的串行份额 [LP-S1 §4.3.7, PDF p. 89]。

## H3 超稀疏性：先测量，再切换算法
- **场景**：FTRAN/BTRAN 的结果可能大多很稀疏。
- **规则**：(a) 用 Hall–McKinnon 判据测量（结果密度低于 10% 为超稀疏；超过 60% 的结果超稀疏即超稀疏模型）[LP-S45，据 LP-S1 §1.3, PDF p. 19]；
  (b) FTRAN 用利用因子稀疏结构的超稀疏求解——Gilbert–Peierls 的两阶段 DFS [LP-S44]，或 Hall–McKinnon 依次取下一个所需 eta 的办法；BTRAN 先把因子存成行式表示，
  再按 FTRAN 的方式求解；保留零检验以防抵消 [LP-S1 §2.3.2–§2.3.3, PDF pp. 30–33]；(c) 只在 LP 被判为超稀疏时启用截断候选表式的超稀疏 CHUZR
  [LP-S1 §3.2.2, PDF p. 55]；(d) ê_p 稀疏时用行式 PRICE，HSOL 同时保存 A 的行式与列式副本 [LP-S1 §3.2.3, PDF pp. 55–56]；(e) 基更新选能保住超稀疏的：
  PF 与 FT 可完全利用，APF、MPF 在更新部分不行 [LP-S5 §3.3, PDF p. 13]（见 H4）。
- **未说明**：HSOL 何时在标准求解与超稀疏求解之间切换、行式与列式 PRICE 的切换阈值、超稀疏 CHUZR 的候选表长度——来源均未给。

## H4 基更新方法选型
- **场景**：实现 UPDATE-FACTOR，或在并行框架里需要一次更新多个基。
- **规则**：(a) 默认 FT，并用 Tomlin (1974) 的办法从已存的部分 BTRAN 结果构造行 eta [LP-S38，据 LP-S1 §2.4.2, PDF p. 35]：两版实验里 FT 都在 27/30 题
  胜过最好的乘积形式（LP-R12, LP-R13），代价是需要动态数据结构、实现难度显著高于 PF [LP-S5 §2.1, PDF p. 6]；(b) 需要简单、独立代码库时用 MPF：
  无消去、无动态结构，FT 只比它高效 34%（ERGO-13-001）或 35%（论文）[LP-S5 §4–§5, PDF pp. 17–18; LP-S1 §2.5.4, §2.6, PDF pp. 46–47]；(c) APF 不作一般用途
  （"is not recommended as a valuable general technique" [LP-S5 §5, PDF p. 17]），只在 suboptimization 框架里用：更新 minor iterations 中的 BTRAN 结果、
  把多个 FTRAN-BFRT 合成一次求解 [LP-S2 §3.1.3, §3.2, PDF pp. 10–12]；(d) minor iterations 之后用 CFT 一次做完 t 个 FT 更新，不损串行效率
  [LP-S2 §3.1.4, PDF p. 10]；(e) PF 类更新只用于很少几次基变化——hsol 如此，未见数值不稳 [LP-S5 §3.1.2, PDF p. 10]。
- **注意**：MPF 没有用在 hsol/h2gmp 或 pami 里 [LP-S15 PDF p. 19; LP-S13 PDF p. 32]；FT 本身出自 Forrest–Tomlin [LP-S37]，PF 出自 Dantzig–Orchard-Hays [LP-S34]。

## H5 BOXED 变量：比率检验里翻转，phase I 里固定
- **场景**：实现对偶 CHUZC 与对偶 phase I。
- **规则**：(a) CHUZC 先一遍把 8 种情形（4 种非基状态 × 2 种离基不可行方向）合并成一个条件 ā_pj = â_pj · s_p · δ_j > 0 [LP-S1 §3.2.3, PDF pp. 56–57]；
  (b) 若最小比率的候选是 BOXED 且它的整个区间也消不掉离基变量的不可行量，就把它翻到另一界而不让它入基，再看下一个比率（BFRT，出自 Fourer [LP-S29]）；
  遇到第一个非 BOXED 候选即停；全部翻完仍不可行则判对偶无界 [LP-S1 §3.2.3, PDF p. 57]；(c) 与 Harris 两遍检验 [LP-S26] 结合时，同一 Harris 组要么全翻、
  要么全不翻并由组内主元最大者入基——代价是入基变量可能带着微小不可行入基 [LP-S1 §3.2.3, §3.3.2, PDF pp. 59, 63]；(d) 已在容差内不可行的入基候选用
  EXPAND 的严格零步（对偶形式：入基时把其 reduced cost shift 到零，离基时撤销）[LP-S30，据 LP-S1 §3.2.3, PDF pp. 58–59]；(e) bound tightening
  （presolve 的特例；来源称小心实现时不需要 postsolve）让更多变量成为 BOXED，既利于 BFRT，又能用翻界取得对偶可行、跳过 phase I——实现细节来源略去
  [LP-S1 §3.2.3–§3.2.4, PDF pp. 58, 60]；(f) 对偶 phase I 用 Koberstein–Suhl 子问题法 [LP-S24]：BOXED 与 FIXED 设为 [0, 0]（翻界总能让 BOXED 对偶可行），
  LOWER [0, 1]、UPPER [−1, 0]、FREE [−1000, 1000]，于是子问题恒可行 [LP-S1 §3.2.4, Table 3.4, PDF p. 60]。
- **简化的代价**：HSOL 在没有 BOXED 非基变量时也照走 BFRT 流程以复用代码；论文承认更讲究的代码此时应改用常规（Harris）比率检验 [LP-S1 ch. 5, PDF p. 95]。

## H6 成本扰动：当算法手段用，但管住尺度与适用面
- **场景**：退化严重，或想复现 pds 类问题上的大幅提速。
- **规则**：(a) 对偶单纯形开始前随机扰动结构变量的成本，符号按变量类型定，幅度结合自身成本、最大成本与对偶容差——HSOL 用 Koberstein 方案的简化不加权版
  [LP-S1 §3.2.3, PDF p. 59; LP-S23]；(b) 最优后移除扰动，残余的微小对偶不可行用原始 phase II 清理 [LP-S1 §3.2.3, PDF p. 59; LP-S8 PDF p. 7]；
  (c) 扰动相对对偶容差过小时，候选比率仍挤在零附近、BFRT 不起作用 [LP-S1 §3.3.2, PDF p. 64]；(d) 不用加权扰动：无数值证据、未被证实
  [LP-S1 §3.2.3, PDF p. 60]；(e) 预期收益集中在 pds 与网络类（pds-20 时间减 84%，LP-R17；NETGEN 总时间减 36%，LP-R19），但 3 个 NETGEN 问题变慢、
  stormG2-1k 毫无变化（LP-R19）——上线前在自己的问题族上测。
- **依据**：Bixby 视扰动为算法手段的主张 [LP-S22，据 LP-S1 §3.3.2, PDF p. 62]，以及本队记录的机制诠释（「分歧」1；诠释不是定理，见 F8）。

## H7 CHUZR 定价：默认 DSE，偏离要有问题类证据
- **场景**：选择或调整离基行的定价规则。
- **规则**：(a) 默认 DSE [LP-S28，据 LP-S1 §3.2.2, PDF p. 54]；(b) BTRAN 之后按定义重算离基行的 DSE 权重，若更新值小于 0.5 倍新值就放弃这次选择、改正权重、
  重做 CHUZR——针对原文 10^-4 权重下限造成的「虚假吸引力」[LP-S1 §3.2.2, PDF pp. 54–55]；(c) 从高级基热启动时 DSE 初始化昂贵，dual Devex 零成本初始化
  但效果较差 [LP-S13 PDF p. 40]；(d) LiDSE / 广义 LiDSE 只在 pds 类（表元多为 ±1）启用，对一般 LP 可能严重损害效率（LP-R18）；
  (e) over-weighting（ŵ_i²）的依据是网络 LP 上的恒等式（LP-R21），证据是 NETGEN（LP-R20）；(f) partial CHUZR 在 NETGEN 上有益（LP-R20），
  在较大 pds 上不合适（LP-R18）——先确认问题族。
- **未说明**：识别「类 pds 问题」以自动启用 LiDSE 的规则（论文只说容易识别，并把自动触发列为未来工作 [LP-S1 §3.3.4, ch. 5, PDF pp. 67, 95]）；
  原始与对偶容差的取值（论文只说常见取 10^-6 或 10^-7，未给 HSOL 的值 [LP-S1 §3.2.2–§3.2.3, PDF pp. 54, 58]）。

## H8 何时开并行，开 PAMI 还是 SIP
- **场景**：多核桌面机上求解单个大规模稀疏 LP。
- **规则**：(a) 不指望线性加速：作者称对高效修正单纯形期待线性加速 "unreasonable" [LP-S2 §6, PDF pp. 24–25]；(b) 以 PAMI 为主——HSOL README 称并行时
  PAMI 通常快于 SIP [LP-S17 l. 125–127]；但 INVERT 份额大的稠密 LP（maros-r7、Linf_520c）上 PAMI 反而变慢，此时 SIP 是互补选择（LP-R3, LP-R5）；
  (c) FTRAN-DSE 主导的超稀疏 LP（如 sgpf5y6）上 SIP 会变慢（LP-R5, LP-R6）；PAMI 的表现则与超稀疏性没有实质关系（LP-R4）；
  (d) 单线程时不要开 PAMI——串行 minor iterations "typically" 降低性能，SIP 选项则无影响；不设 OMP_NUM_THREADS 会用上全部线程、"may be very slow"，
  8 "typically a good choice" [LP-S17 l. 113–125]；(e) SIP 至少需要 4 个处理器，多于 4 只增加 spmv 与 chuzc 的并行 [LP-S2 §4, PDF p. 15]。

## H9 suboptimization 只当并行来源，并配候选质量控制
- **场景**：实现跨迭代并行（PAMI 类）。
- **规则**：(a) 接受它作为定价规则劣于 DSE、会走更差的单纯形路径，用它只为暴露任务并行（论文："it provides more scope for task parallelism"
  [LP-S1 §1.1, PDF p. 18]；[LP-S2 §6, PDF p. 24]）；(b) 候选数 s 定为 8 而不论处理器数——原型经验表明更大的倍数被浪费的计算与额外迭代抵消
  [LP-S2 §3.3, PDF p. 13]；(c) 每个 minor iteration 后若候选吸引力 α_p < ψ α_p^i 就剔除；ψ 在 [0.9, 0.999] 内效果相近，取 0.95 是中位数而非最优（LP-R7）；
  已变可行或不再有吸引力（α_p ≤ 0）的候选无论 ψ 都剔除 [LP-S2 §3.3, PDF p. 13]；(d) major CHUZR 在稠密 LP 上数据并行，稀疏 LP 上用超稀疏 CHUZR，
  只剩几百个候选、无需并行 [LP-S1 §4.3.5, PDF p. 86]。
- **结果**：有质量控制时 pami 相对 hsol 的迭代数均值 0.96（LP-R4）。suboptimization 的出处是 Rosander [LP-S47]，不是本队来源的发明（F1, F7）。

## H10 把并行粒度对准方程组，再用代数把方程组合并
- **场景**：设计 PAMI 的 BTRAN/FTRAN 任务调度。
- **规则**：(a) s 个 BTRAN 在 minor iterations 之前作为 s 个并行任务一次解完 [LP-S1 §4.3.3, PDF p. 83]；(b) major update 的三组 FTRAN（常规、FTRAN-DSE、
  FTRAN-BFRT）中，用 B_k^{-1} 求解的「逆部分」（inverse part）任务并行，随后的 PF 变换「更新部分」（update part）依赖组内其它结果，只能在向量大而稠密时做数据并行
  [LP-S2 §3.2, PDF pp. 11–12]；
  (c) 用 APF 把至多 t 个 FTRAN-BFRT 合成一次 B_k^{-1} 求解，使方程组总数降到 2t+1（无翻界时 2t），t ≤ s−1 时每个处理器至多两个；t = s 且有翻界时会多出
  一个 "orphan task"，因此最近有翻界就把 minor iterations 限到 s−1——期刊版写「前 s−2 次迭代」[LP-S2 §3.2, PDF p. 12]，论文写「前 t−1 次迭代」
  [LP-S1 §4.3.3, PDF p. 84]；(d) 全部 2t+1 个 FTRAN 同时作为任务发出，由处理器自取 [LP-S1 §4.3.3, PDF p. 85]；(e) 数据并行 PRICE 前随机重排列以均衡负载
  （反例：fome13 由同一 LP 复制而成的块结构会让更新行集中在一块）[LP-S1 §4.3.2, PDF p. 81]；逻辑变量部分不做 PRICE，由一个任务单独做 CHUZC1
  [LP-S1 §4.3.2, PDF p. 82]。
- **依据**：方程组计数是来源里的非形式论证 [LP-S2 §3.2, PDF p. 12]。

## H11 INVERT：串行、不重叠，按成本模型触发
- **场景**：决定何时重新求逆，以及要不要把 INVERT 并行或与迭代重叠。
- **规则**：(a) 自上次 INVERT 以来更新部分累计的操作数等于上次 INVERT 的操作数时重新求逆，用操作计数作确定性伪时钟；性能对模型参数不敏感（LP-R16）；
  (b) 并行求解压低了更新部分的时间，PAMI 把阈值放大到 1.5 × t_I [LP-S1 §4.3.4, PDF p. 85]；(c) 不要把 INVERT 与迭代重叠后用 PF eta 追赶——据 Hall–McKinnon
  的报告会数值不稳 [LP-S48，据 LP-S1 §4.1.2, PDF p. 73]；FT 追赶式重叠只是论文提出的未来工作 [LP-S1 ch. 5, PDF p. 95]；(d) 认清代价：串行 INVERT 期间其它处理器空闲，
  这是 PAMI 加速有限的原因之一 [LP-S2 §3.1.4, PDF pp. 10–11; LP-S1 ch. 5, PDF p. 95]。

## H12 诚实评测
- **场景**：发表或解读单纯形实现的计算比较。
- **规则**：(a) 比较更新方法时，所有方法走同一条基变化序列、共用为 FT 定出的重新求逆间隔（FT 不吃亏）、只计 update + FTRAN + BTRAN 的时间
  [LP-S5 §4, PDF pp. 13, 15–16; LP-S1 §2.5.4, PDF p. 46]；(b) 速度比用几何均值 [LP-S2 §5.1, PDF p. 16]；(c) 同时报 p1/hsol、p8/p1、p8/hsol 三个比值，
  迭代数变化大的个例按迭代比缩放再看（qap12：2.58 → 1.74，LP-R4）；(d) 明示测试集筛选（ParISS：114 题筛到 13 题，LP-R22）与预处理、crash 的开关
  [LP-S2 §5.2, §5.4, PDF pp. 21, 23]；(e) 拿商业求解器比研究代码时说明其不合理处（"perhaps, unreasonable" [LP-S2 §5.4, PDF p. 23]）；
  (f) 用 performance profile 而不只报一个均值 [LP-S5 §4, PDF p. 13; LP-S2 §5.2, §5.4, PDF pp. 21, 23]。

## H13 INVERT 的 LU：先剥单例，再做 Markowitz 搜索与阈值主元
- **场景**：实现基矩阵的稀疏 LU。
- **规则**：(a) 先 triangularization，找出并移走所有单例行与单例列，只对剩下的 bump 做消去 [LP-S1 §2.2.5, PDF p. 26]；(b) bump 内按 Markowitz merit
  (r_i − 1)(c_j − 1) 选主元 [LP-S31，据 LP-S1 §2.2.6, PDF p. 27]，采用 Suhl–Suhl 的实现：按行列计数升序搜索、在前几个（Suhl–Suhl 建议 4 个）候选中取最好者、
  用按计数索引的双向链表 [LP-S33，据 LP-S1 §2.2.6, PDF p. 28]；(c) 阈值主元 |b_ik| ≥ u · max_i |b_ik|，Tomlin 建议 u = 0.01 或 0.1 [LP-S32，据 LP-S1 §2.2.6, PDF p. 28]，
  HSOL 实际所用的 u 未说明；(d) 把置换吸收进因子，存置换后的 L̄、Ū，求解时不必置换右端 [LP-S1 §2.2.3, PDF p. 24]；(e) Tomlin 的列排序便宜，但跟不上消去中稀疏模式的变化
  [LP-S1 §2.2.6, PDF p. 28]。
- **依据**：双精度下数量级相差悬殊的加减会丢精度，阈值主元即对策（论文表 2.1 的演示）[LP-S1 §2.2.4, PDF p. 25]。

## H14 选型：什么时候用对偶单纯形
- **场景**：用户问「这个 LP 用什么方法」。
- **规则**：(a) 大规模稀疏 LP 默认对偶修正单纯形（DSE 与 BFRT 之后的首选变体）[LP-S1 §1, PDF p. 16; LP-S13 PDF p. 16]；(b) 求解一族相关问题（热启动；
  收紧约束后对偶可行性保持，适合 MIP）时单纯形常优于 IPM [LP-S2 §1, PDF p. 1; LP-S10 PDF p. 11; LP-S14 PDF p. 2]；(c) 超稀疏 LP 上单纯形通常好于 IPM，
  其它 LP 常常不然（幻灯片转述 Hall–McKinnon）[LP-S9 PDF p. 20]；(d) 产品默认：COPT 对 LP 自动选对偶单纯形（LpMethod = −1），按稀疏性、系数范围在单纯形与 barrier
  之间自动挑是另一个取值（5）[LP-S16 §11.3, PDF p. 151]；(e) 需要基解或灵敏度分析时用单纯形，或在其它方法后接 crossover——COPT 的 ReqSensitivity 以有最优基为前提
  [LP-S16 §11.3, PDF p. 153]。
- **边界**：IPM、PDLP 的内部与收敛理论不在本队范围（00-charter）。

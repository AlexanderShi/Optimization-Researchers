# DFO Team · 关键结果速查

格式：ID | 结论（**定性**，无精确常数）| 假设 | proved-vs-cited | 层级。
蒸馏出的 skill 引用结果时必须整条带出（含假设），不得只摘速率。

## DFO-R1 零阶方法付维度代价
- **结论**：zeroth-order 梯度估计把一阶复杂度乘上一个维度因子——高斯平滑
  单点路线是 O(n) 级因子；两点估计相对随机梯度方法的退化**至多 √d 因子**，
  覆盖光滑与非光滑情形、推广到 m≥2 次评估，且有信息论下界证明该速率在
  常数或对数因子内 sharp。
- **假设**：凸（或声明的非凸期望稳定性度量）、L-光滑或 Lipschitz、随机 oracle。
- **状态**：cited — [DFO-S20]（高斯平滑，凸）；[DFO-S21]（两点 √d 因子+下界，
  arXiv:1312.2139 abs 页核实 2026-10-09）；[DFO-S4 content]「zeroth-order 估计
  引入维度与平滑依赖的代价，不能把梯度调用和函数值调用当等价信息」
  (sources.json 原文, verified-local)。
- **层级**：定性结论 verified-local + verified-web / 精确常数仍需查原文。

## DFO-R2 随机非凸 zeroth-order 的收敛
- **结论**：随机非凸光滑情形下，随机平滑 zeroth-order 方法有到
  ε-稳定点（E‖∇f‖² 意义）的多项式 oracle 复杂度，含维度因子。
- **假设**：L-光滑、无偏有界方差随机 oracle。
- **状态**：cited — [DFO-S4]。精确指数需查原文。
- **层级**：model-knowledge (high)。

## DFO-R3 模式搜索全局收敛
- **结论**：光滑 f 上，满足网格结构与简单下降条件的模式搜索有
  lim inf ‖∇f(x_k)‖ = 0 型全局收敛。
- **假设**：f 连续可微、水平集有界（unanchored——确切假设见原文）。
- **状态**：cited — [DFO-S12]。
- **层级**：model-knowledge (high)。

## DFO-R4 MADS 的 Clarke 稳定性
- **结论**：MADS 对非光滑（Lipschitz）问题收敛到 Clarke 意义稳定点，
  且可处理约束（extreme barrier 等机制）。
- **假设**：f 局部 Lipschitz；网格/方向集条件（unanchored）。
- **状态**：cited — [DFO-S14]。
- **层级**：model-knowledge (high)。

## DFO-R5 Nelder–Mead 无一般保证（反例存在）
- **结论**：NM 没有一般收敛保证：存在低维光滑（甚至严格凸）反例族，使 NM
  经反复 inside contraction 收敛到**非稳定点** [DFO-S10]。正面结果只有
  低维/严格凸的受限情形 [DFO-S11]。
- **状态**：cited。反例细节（维度、函数族形式）需查 [DFO-S10] 原文。
- **层级**：model-knowledge (high)。
- ⚠️ 这是胡说高发区：见 05-failure-modes F2。

## DFO-R6 模型型信赖域的全局收敛
- **结论**：基于 fully-linear（一阶精度可控）模型的信赖域 DFO 方法
  全局收敛到一阶稳定点；fully-quadratic 模型对应二阶结果。
- **假设**：f 光滑有下界；模型精度条件 + 标准信赖域管理（unanchored）。
- **状态**：cited — [DFO-S16]（书中定理，章节号需查）。
- **层级**：model-knowledge (high)。

## DFO-R7 噪声下的差分区间权衡
- **结论**：带噪函数值的有限差分需要在 Taylor 截断误差与测量误差间平衡区间；
  自适应区间估计能以额外评估为代价产出可靠梯度近似。
- **状态**：verified-local — [DFO-S3 content] (sources.json 原文转述)。
  最优区间的精确表达式（含噪声水平与高阶导数）需查原文。
- **层级**：定性 verified-local。

## DFO-R8 zeroth-order + momentum 的收敛性
- **结论**：heavy-ball momentum 可并入随机 zeroth-order 方法（SMTP，扩展
  stochastic three-point 框架），非凸/凸/强凸情形均有收敛结果。
- **状态**：verified-local — [DFO-S5 content] (sources.json 原文转述)。
  各情形的速率表达式需查原文。
- **层级**：定性 verified-local。
- 注意：「有收敛结果」≠「优于不带 momentum」——后者语料无定论（02-schools 分歧4）。

## DFO-R9 基准测试的 profiles 方法
- **结论**：data profiles（预算视角）与 performance profiles（相对比值视角）
  能暴露单一最终值排名掩盖的 solver 行为；两视角应同时报告。
- **状态**：verified-local — [DFO-S2 content]、[DFO-S8 content]。
- **层级**：verified-local。

## DFO-R10 随机平滑处理非光滑随机凸优化
- **结论**：随机平滑（对非光滑凸 f 做随机扰动平滑）+ 加速梯度法，得到对
  梯度估计方差依赖最优的收敛保证，**期望与高概率两种形式都有**；
  可与去中心化优化结合得到阶最优的分布式随机优化算法。
- **假设**：凸、非光滑、随机 oracle（方差条件；精确假设查原文）。
- **状态**：cited — [DFO-S23]（arXiv:1103.4296 abs 页核实 2026-10-09；
  作者声称是非光滑情形首个 variance-dependent 速率）。
- **层级**：定性 verified-web；速率表达式与常数需查原文。
- 方法论注记：这是「随机化当一等工具、保证要期望+高概率双形式」的
  Duchi 支线代表作（见 researchers/john-duchi.md）。

## DFO-R11 随机模型信赖域的几乎必然收敛
- **结论**：确定性光滑目标（**函数值无噪声**，不确定性只在模型）上，
  随机模型只需「以概率 ≥ 1/2 达到足够的近似质量」（而非仅期望正确），
  与经典框架几乎一致的信赖域方法即**几乎必然收敛**（鞅论证）；适用于
  DFO 插值模型等模型不确定性来源。
- **假设**：f 光滑、函数值精确、模型概率精度条件（精确定义——
  probabilistically fully linear——查原文）。
- **状态**：verified-web — [DFO-S24]（arXiv:1304.2808 abs 页摘要，核实
  2026-10-09；期刊版出处需核对）。
- **层级**：定性 verified-web；概率条件的精确形式需查原文。
- ⚠️ 使用注意：此设定与带噪函数值（[DFO-S3, S22] 的世界）不同，
  结论不迁移——引用时必须声明「函数值无噪声、不确定性在模型」。

# NLP Team · 关键结果速查

格式同 DFO Team：定性结论 + 假设 + proved-vs-cited + 层级，无精确常数。

## NLP-R1 凸光滑 GD 的基线速率
- **结论**：f 凸且 L-光滑、步长按 1/L 量级，GD 目标间隙 O(1/k)。
- **假设**：凸、L-光滑、极小点存在、精确梯度。
- **状态**：cited — [NLP-S8]（教科书证明）。
- **层级**：model-knowledge (high)。

## NLP-R2 Nesterov 加速 O(1/k²) 且最优
- **结论**：同一假设类上加速梯度达到目标间隙 O(1/k²)，匹配一阶方法下界
  Ω(1/k²)，故最优；每步成本与 GD 同阶；保证只对目标间隙，**不是下降法**、
  **要求 L 已知**。
- **假设**：凸、L-光滑（L 已知）、极小点存在、精确梯度；不含强凸情形
  （μ>0 是另一套参数化）。
- **状态**：cited — [NLP-S1]（本地机器区条目逐字段在档，含全部假设与局限；
  该条目自标 verified:false、常数 unanchored）；下界 cited — [NLP-S13]。
- **层级**：定性 verified-local（对本地条目而言）；精确常数禁止引用
  （不同转述不一致，本地条目明确标注 verify）。

## NLP-R3 强凸情形的线性速率
- **结论**：μ-强凸 + L-光滑下 GD 线性收敛（速率依赖 κ=L/μ）；加速方法把
  κ 依赖改进到 √κ 量级。
- **假设**：μ-强凸、L-光滑、精确梯度。
- **状态**：cited — [NLP-S8]。
- **层级**：model-knowledge (high)。

## NLP-R4 heavy ball 的边界
- **结论**：heavy ball 在二次函数上有经典（局部/特征值分析）加速；但存在
  光滑强凸函数使常参数 heavy ball **不**全局收敛（反例）；因此「heavy ball =
  全局加速」是错的。
- **假设**：反例在光滑强凸类内（构造细节需查原文）。
- **状态**：cited — [NLP-S7]（原方法）；[NLP-S14]（IQC 分析与反例）。
- **层级**：model-knowledge (high)。

## NLP-R5 随机情形 momentum 不改进采样复杂度阶
- **结论**：二次目标+持续梯度噪声下，stochastic heavy ball 与加速 SGD 的
  采样复杂度不必然优于调好的 vanilla SGD——momentum 同时改变偏差衰减与
  方差累积 [NLP-S4 content (sources.json 原文转述)]；简单随机实例上现有
  momentum 方案也不必然胜过 SGD [NLP-S3 content]。
- **状态**：verified-local（定性，sources.json）；定理精确形式需查原文。
- **层级**：verified-local（定性）。
- ⚠️ 与 NLP-R2 并读：确定性加速真实存在，随机情形不自动继承——
  这是本队与用户研究最相关的一条。

## NLP-R6 momentum 的实践面
- **结论**：深度学习中 momentum SGD 可应对困难目标的曲率，但效果强烈依赖
  初始化与 momentum 调度 [NLP-S2 content (sources.json 原文转述)]。
- **状态**：verified-local（定性）。
- **层级**：verified-local。

## NLP-R7 Newton 局部二次收敛
- **结论**：Hessian Lipschitz + 解处 Hessian 非奇异时，Newton 法局部二次收敛；
  全局行为需线搜索/信赖域全局化。
- **假设**：二阶光滑、非退化、初始点足够近。
- **状态**：cited — [NLP-S5]。
- **层级**：model-knowledge (high)。

## NLP-R8 信赖域全局收敛
- **结论**：标准信赖域管理 + Cauchy 下降条件下，lim ‖∇f(x_k)‖ = 0 型
  全局收敛（一阶）；二阶条件下有到二阶稳定点的加强版。
- **假设**：f 光滑有下界、模型与半径管理标准条件（unanchored）。
- **状态**：cited — [NLP-S6]。
- **层级**：model-knowledge (high)。

## NLP-R9 SGD 基线
- **结论**：凸随机情形，递减步长 SGD 期望目标间隙 O(1/√k)（一般凸）/
  O(1/k)（强凸）量级；常步长收敛到噪声球。
- **假设**：无偏梯度、方差有界、步长条件（Robbins-Monro 型）。
- **状态**：cited — [NLP-S15, S16]。
- **层级**：model-knowledge (high)。

## NLP-R10 AdaGrad：按坐标自适应的 regret 保证
- **结论**：按坐标累积历史梯度、动态调整 proximal function 的自适应次梯度
  方法，regret 保证**与事后可选的最优 proximal function 可比**，免手调
  学习率；在稀疏梯度结构（预测力强但出现少的特征）上优势明显。
- **假设**：在线凸优化/次梯度设定（精确条件查原文）。
- **状态**：verified-web — [NLP-S19]（JMLR 官方页摘要，核实 2026-10-09）。
- **层级**：定性 verified-web；regret 界精确形式需查原文。

## NLP-R11 分布式 dual averaging：收敛与网络效应分离
- **结论**：网络上去中心化的 dual averaging 次梯度方法，其分析把优化自身
  收敛与网络拓扑/通信约束效应**分离**；达到给定精度的迭代数与网络谱隙
  成反比缩放；覆盖确定性与随机情形，并配有下界与模拟验证。
- **假设**：分布式凸目标（各节点局部凸函数之和）、本地计算+邻居通信
  （精确条件查原文）。
- **状态**：verified-web — [NLP-S20]（arXiv abs 页摘要 + 所列期刊版
  IEEE TAC 57(3):592–606, 2012，核实 2026-10-09）。
- **层级**：定性 verified-web；谱隙依赖的精确表达式需查原文。

## NLP-R12 复合/弱凸问题的随机 prox-linear 与次梯度
- **结论**：对「非光滑凸 ∘ 光滑」复合与弱凸目标，随机 prox-linear 与随机
  （广义）次梯度方法在温和技术条件下**收敛到一阶稳定点**；应用于非光滑
  phase retrieval。
- **假设**：复合/弱凸结构、随机 oracle、温和技术条件（精确条件查原文）。
- **状态**：verified-web — [NLP-S21]（arXiv:1703.08570 abs 页摘要，
  核实 2026-10-09；期刊版出处需核对）。
- **层级**：定性 verified-web；速率与条件需查原文。
- 方法论注记：「结构化非凸优先」的 Duchi 支线代表作
  （见 researchers/john-duchi.md）。

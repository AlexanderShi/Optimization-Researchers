# John Duchi · DFO Team 研究者档案

> 档案依据：Google Scholar 个人页 + 2 篇论文的 arXiv 一手页面，联网核实于
> 2026-10-09（层级 verified-web）。**仅基于摘要与个人页，未读论文全文**——
> 定理精确形式需查原文。

## 身份（verified-web）

- John C. Duchi，Stanford 大学统计系 & 电子工程系 Associate Professor
  （Scholar 个人页 2026-10-09 显示的头衔）。
- 研究方向：machine learning、statistics、optimization、AI。
- 引用量级：总引用 ~47,000，h-index 73（Scholar，2026-10-09）。
- Scholar: scholar.google.com/citations?user=i5srt20AAAAJ

## 在 DFO 版图中的位置

随机 zeroth-order 学派（见 02-schools.md 流派表），且是该学派里
**信息论/极小极大文化**的代表：不满足于给出算法上界，固定搭配
匹配的下界证明速率 sharp。与经典 DFO（模型型/直接搜索）文化相距最远，
与 [DFO-S20 Nesterov-Spokoiny]、[DFO-S4 Ghadimi-Lan] 同属一脉。

## DFO 核心贡献（verified-web）

### [DFO-S21] 两点零阶优化的最优速率
Duchi, Jordan, Wainwright, Wibisono, "Optimal rates for zero-order convex
optimization: the power of two function evaluations", arXiv:1312.2139
(v2 2014)；期刊版 IEEE Trans. Information Theory 2015（venue/年份据 Scholar
个人页）。
- 摘要核实内容：配对（两点）函数评估下，随机扰动梯度估计的算法相对
  传统随机梯度方法的收敛速率退化**至多 √d 因子**（d 为维度）；覆盖光滑
  与非光滑情形，推广到 m≥2 次评估；并给出信息论下界，证明所得速率在
  常数或对数因子内 **sharp**（arXiv abstract, 2026-10-09 核实）。
- 这是 04-results.md 条目 DFO-R1「两点估计 √n 级且阶最优」的出处本体。

### [DFO-S23] Randomized Smoothing for Stochastic Optimization
Duchi, Bartlett, Wainwright, arXiv:1103.4296 (v2 2012)；期刊版
SIAM J. Optim.（**model-knowledge，需核对**——arXiv 页未列期刊引用）。
- 摘要核实内容：随机平滑 + 加速梯度法处理非光滑凸随机优化；收敛保证
  **同时给期望与高概率形式**，对梯度估计方差的依赖最优（作者声称是
  非光滑情形首个 variance-dependent 速率）；可与去中心化优化结合得到
  阶最优的分布式随机优化算法（arXiv abstract, 2026-10-09 核实）。
- 对应 04-results.md 新条目 DFO-R10。

## 方法论立场（蒸馏的思维框架，逐条锚定）

1. **上界必配下界**：速率声明没有下界就不算完——[DFO-S21] 摘要明言补了
   信息论下界证 sharp。对本队的意义：引用任何「最优」速率时必须能指出
   匹配的下界出处（强化 03-heuristics 的收敛声明纪律）。
2. **信息计费视角**：核心问题是「每次 oracle 调用携带多少信息」——
   标题本身就是 "the power of **two function evaluations**"。与本队共识
   「信息计费第一公民」（02-schools 共识 1）同源。
3. **随机化是一等工具**：用随机扰动换光滑性与方差控制，而非把随机性
   当噪声容忍 [DFO-S23]。
4. **保证要完整**：期望界与高概率界都给 [DFO-S23 摘要]；只报期望界是
   不完整的声明。

## 跨队说明

Duchi 最高引工作 AdaGrad（"Adaptive subgradient methods...", JMLR 2011,
~17,000 引用，Scholar 核实）属随机一阶自适应方法——**NLP team 范围**，
本档案不展开；NLP team 扩编时可为其另立档案。其 local privacy、
分布式优化、distributional robustness 工作与 DFO 无关，不收。

## 边界

- 未读全文：√d 因子的精确常数、假设细节（光滑度模数、噪声模型）需查
  [DFO-S21, S23] 原文后方可写进论文。
- Scholar 头衔/引用数是 2026-10-09 快照，会过时。

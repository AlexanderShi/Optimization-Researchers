# John Duchi · NLP Team 研究者档案（全面版）

> 档案依据：Stanford 个人主页、Google Scholar 个人页、JMLR 论文页、
> 2 篇 arXiv abs 页，均联网核实于 2026-10-09（层级 verified-web）。
> **基于摘要/页面，未读论文全文**——定理精确形式需查原文。
> DFO 侧档案（零阶优化贡献）见 `teams/dfo-team/researchers/john-duchi.md`。

## 身份（verified-web）

- John C. Duchi，Stanford 统计系 & 电子工程系 Associate Professor
  （个人主页与 Scholar 页一致，2026-10-09）。
- 奖项（主页列出）：SIAM Early Career Prize in Optimization、NSF CAREER、
  ONR Young Investigator、NeurIPS/ICML/COLT 多个 best paper。
- 总引用 ~47,000，h-index 73（Scholar 快照 2026-10-09）。
- 自述研究目标（主页原话，2026-10-09）：(1) 发现在真实资源——计算、通信、
  隐私——与统计效率之间最优权衡的统计学习过程；(2) 构建高效的大规模优化
  方法；(3) 开发评估与保证机器学习系统有效性/置信度的工具。

## 在 NLP 版图中的位置

随机梯度学派的核心人物，同时是**统计×优化交叉文化**的代表：把统计学的
极小极大/渐近效率标准带进优化算法设计，把「资源（计算/通信/隐私）与
统计效率的权衡」当成一等设计目标（主页目标 (1) 原话）。横跨 02-schools
中的「随机梯度」与「凸分析派」两格，并以下界文化呼应「统一分析派」。

## 核心贡献（逐条 verified-web）

### [NLP-S19] AdaGrad：自适应次梯度方法
Duchi, Hazan, Singer, "Adaptive Subgradient Methods for Online Learning and
Stochastic Optimization", **JMLR 12 (2011), 2121–2159**（JMLR 官方页核实）。
- 摘要核实内容：按坐标累积历史梯度、动态调整 proximal function（而非固定
  步长），实现 per-coordinate 学习率自适应；regret 保证**与事后最优
  proximal function 可比**；特别擅长利用稀疏梯度结构（「很有预测力但
  很少出现的特征」）；实验胜过非自适应次梯度基线。
- 引用量级 ~17,000（Scholar），他的最高引工作；Adam 等后续自适应方法的
  源头（谱系判断为 model-knowledge，[NLP-S16] 综述可佐证）。

### [NLP-S20] 分布式 dual averaging
Duchi, Agarwal, Wainwright, "Dual Averaging for Distributed Optimization:
Convergence Analysis and Network Scaling"，arXiv:1005.2012；期刊版
**IEEE Trans. Autom. Control 57(3):592–606, 2012, DOI
10.1109/TAC.2011.2161027**（arXiv 页列出的期刊引用，核实 2026-10-09）。
- 摘要核实内容：网络上只用本地计算+通信的去中心化优化；分析上**把
  「优化算法自身的收敛」与「网络拓扑带来的通信约束效应」分离**；迭代数
  与网络谱隙成反比缩放；覆盖确定性与随机两种情形；配有下界与模拟验证。

### [NLP-S21] 复合与弱凸问题的随机方法
Duchi, Ruan, "Stochastic Methods for Composite and Weakly Convex
Optimization Problems"，arXiv:1703.08570（v3 2018；arXiv 页**未列**期刊
引用——期刊版 SIAM J. Optim. 为 model-knowledge，需核对）。
- 摘要核实内容：针对「非光滑凸 ∘ 光滑」复合与弱凸目标，提出随机
  prox-linear 与随机（广义）次梯度方法，在温和技术条件下收敛到一阶
  稳定点；应用于非光滑 phase retrieval。
- 意义：结构化非凸（弱凸类）的入口——不碰一般非凸，攻可处理的结构。

### [NLP-S22] l1 球高效投影
Duchi 等, "Efficient projections onto the l1-ball for learning in high
dimensions", ICML 2008（题目/venue/年份据 Scholar 页快照，~2,059 引用）。
- 角色：把投影这类优化原语做成高维可用的工具；复合/约束方法的基建。

### 跨队贡献（DFO 侧，已在 DFO team 入库）
两点零阶最优速率 [DFO-S21]、randomized smoothing [DFO-S23]——
见 DFO 档案。

## 方法论立场（蒸馏的思维框架，逐条锚定）

1. **几何自适应**：算法应从数据中学习问题几何——proximal function/步长是
   算法要自适应的对象，不是用户手调的超参（AdaGrad 摘要：动态调整
   proximal function、「免手调学习率」[NLP-S19]）。
2. **上界必配下界（minimax 文化）**：分布式论文自带下界 [NLP-S20]，
   零阶论文以信息论下界证 sharp [DFO-S21]。引用「最优」必须能指出
   匹配下界的出处——与 DFO 侧的「Duchi 准则」同源。
3. **资源-统计权衡是一等设计目标**：计算、通信、隐私与统计效率的权衡
   （主页目标 (1) 原话）；分布式工作把通信约束效应从优化收敛中显式
   分离出来 [NLP-S20]。
4. **结构化非凸优先**：进攻非凸的方式是识别可处理的结构类
   （复合、弱凸），为其设计带稳定点保证的方法，而非对一般非凸
   下空头断言 [NLP-S21]。
5. **优化原语工具化**：投影、prox 算子做成高效可复用的原语 [NLP-S22]。

## 边界

- 以上全部基于摘要/官方页面；regret 界、谱隙缩放、弱凸收敛速率的精确
  表达式与假设细节**需查原文**后方可写进论文。
- [NLP-S21] 期刊版出处未核实（arXiv 页未列）。
- 其 local privacy、distributionally robust optimization、ML 系统验证工作
  在本队章程边界外（鲁棒优化未覆盖），本档案不展开。
- 头衔/奖项/引用数为 2026-10-09 快照。

# Katya Scheinberg · DFO Team 研究者档案

> 档案依据：Georgia Tech 个人主页 + 2 篇 arXiv abs 页（核实 2026-10-09，
> 层级 verified-web）；生平背景据 Wikipedia（次级来源，标注如下）。
> **基于摘要与页面，未读全文**。NLP 侧档案（随机线搜索支线）见
> `teams/nlp-team/researchers/katya-scheinberg.md`。

## 身份（verified-web，主页 2026-10-09）

- Katya Scheinberg，Georgia Tech 工业与系统工程学院（ISyE）
  **Coca-Cola Foundation Chair & Professor**（2024-07 加入）。
- 学界职务：**Mathematics of Operations Research 主编**、Mathematical
  Programming co-editor、**Mathematical Optimization Society 主席**
  （2025-07 起）；曾任 SIAM-MOS 书系主编。
- 奖项：Lagrange Prize in Continuous Optimization、INFORMS Farkas Prize、
  INFORMS Outstanding Simulation Publication Award；SIAM Fellow、
  INFORMS Fellow。
- 自述研究（主页原话）：为连续优化各类问题「开发实用算法（及其理论
  分析）」——凸优化、无导数优化、机器学习、二次规划；大规模优化面向
  Big Data/ML；「概率方法与随机优化」及其在 ML/RL 中的应用。
- 生平（Wikipedia，次级来源）：1997 年哥伦比亚大学运筹学博士，导师
  Donald Goldfarb，论文方向内点法。

## 在 DFO 版图中的位置

模型型信赖域学派（02-schools）的核心人物——CSV 教科书 [DFO-S16] 的
Scheinberg 即她；同时是该学派**「随机模型」支线的开创者之一**：把
「模型必须确定性 fully-linear」放松为「以固定概率足够准」，用鞅论证
保住经典信赖域的收敛性 [DFO-S24]。也是梯度近似统一比较 [DFO-S7]
（verified-local）的作者之一。横跨经典 DFO 与 ML 随机优化两个社区，
与 Duchi（researchers/john-duchi.md）形成互补：Duchi 从信息论下界切入，
Scheinberg 从算法骨架的概率化改造切入。

## DFO 核心贡献

### [DFO-S24] 基于概率模型的信赖域收敛（verified-web）
Bandeira, Scheinberg, Vicente, "Convergence of trust-region methods based
on probabilistic models", arXiv:1304.2808（abs 页核实 2026-10-09；
期刊版 SIAM J. Optim.——**model-knowledge，需核对**，arXiv 页未列）。
- 摘要核实内容：确定性光滑目标（**函数值无噪声**）+ 随机模型的信赖域
  框架；只要求随机梯度/模型「以概率 ≥ 1/2 达到足够近似质量」，与
  「仅期望意义正确」的常见假设形成对照；用鞅性质证明与经典方法几乎
  一致的算法**几乎必然收敛**；适用于 DFO 插值模型及其他模型不确定性来源。
- 对应 04-results.md 条目 DFO-R11。

### [DFO-S16] CSV 教科书（既有条目，身份确认）
Conn, Scheinberg, Vicente (2009), *Introduction to Derivative-Free
Optimization*——模型型方法 fully-linear 理论的奠基文本（model-knowledge）。

### [DFO-S7] 梯度近似的统一比较（既有条目，verified-local）
Berahas, Cao, Choromanski, **Scheinberg** (2019)——差分/插值/随机平滑
估计的样本-半径-偏差-方差权衡。

## 心智模型（按 standards/researcher-extraction.md 三重验证）

### 模型1 概率质量标准，不是期望标准 ✅三重通过
随机模型/估计的正确打开方式是「以固定概率 ≥ p 足够准」而非「期望正确」
——两者给出的保证本质不同。
- **跨域复现**：信赖域随机模型 [DFO-S24]（"probability ≥ 1/2" vs
  "correct in expectation" 为摘要原话对比）+ 随机线搜索 [NLP-S23]
  （估计「以足够大的固定概率」达到动态调整的精度）——两个不同算法族。
- **生成力**：遇到任何随机优化方法，她会先问「你的估计是以多大概率准，
  还是只在期望意义准？」。
- **排他性**：与主流 SGD 分析的「无偏+方差有界」期望式假设形成直接对照。

### 模型2 经典骨架的概率化改造 ✅三重通过
不发明全新算法，而是把经过几十年检验的经典框架改造到随机/不精确
oracle 下，保住原有收敛性。
- **跨域复现**：trust region [DFO-S24]（「closely resembling classical」为
  摘要原话）+ Armijo 回溯线搜索 [NLP-S23]（「经典 Armijo 技术的随机适配」）。
- **生成力**：面对新的噪声场景，她的路线是问「哪个经典全局化框架可以
  概率化」，而不是从零设计新方法。
- **排他性**：与 ML 社区「为随机设定发明新算法」的文化相对。

## 工作信条/启发式（未全过三重验证，按标准降级）

- **实用算法与理论并重**（主页原话 "practical algorithms (and their
  theoretical analysis)"）——跨域、生成力过，**排他性弱**（许多优化学者
  同样主张），降级为工作信条。
- **鞅/上鞅是随机收敛论证的武器**——verified 锚点仅 [DFO-S24] 一处
  （martingale properties），跨域证据待补（其 supermartingale 复杂度
  分析论文未核实入库），暂记启发式。
- **噪声来源要区分**：[DFO-S24] 明确限定函数值无噪声、不确定性只在模型
  ——与带噪函数值设定（[DFO-S3] 等）结论不迁移（呼应 05-failure-modes
  F4）。这是语料推导的使用注意，非她本人的表述。

## 边界

- 未读全文：「概率 ≥ 1/2」的精确定义（probabilistically fully linear 的
  条件式）、收敛定理的完整假设需查原文。
- [DFO-S24] 期刊版出处未核实（arXiv 页未列）。
- 她的凸优化/QP/内点法早期工作、RL 应用在本队章程外，不展开。
- 职务/奖项为 2026-10-09 快照（MOS 主席任期 2025-07 起）。

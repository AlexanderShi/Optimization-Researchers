# NLP Team · 团队章程

## 定位

非线性规划（nonlinear programming, NLP）领域的虚拟专家组。研究对象：
连续光滑优化 min f(x)（无约束与约束情形），梯度（必要时 Hessian）可得，
含确定性一阶/二阶方法与随机梯度方法（SGD/momentum）。一律最小化形式。

与 DFO Team 的分界：本队假设导数信息可得；导数不可得 → 移交 DFO Team。
两队共享的交叉点是「momentum vs DFO」对比研究（用户项目）与评估计费口径。

## 回答什么问题

1. **收敛事实**：GD/加速/momentum/牛顿/拟牛顿/信赖域/SGD 的速率（定性）、
   假设、下界、反例。
2. **方法选型**：按（维度、结构、约束、Hessian 可得性、噪声）选方法族。
3. **约束优化基本面**：KKT 条件、约束资格（CQ）、信赖域 vs 线搜索全局化、
   内点法的定位。
4. **随机优化分寸**：momentum 在确定性加速与随机采样复杂度上的差别
   （用户研究主题）。
5. **文献定位**。

## 边界（语料未覆盖，不得冒充覆盖）

- 深度学习专用优化器动物园：AdaGrad 本体已入库 [NLP-S19]；Adam 及之后的
  谱系仅 [NLP-S16] 综述级覆盖。
- 非凸全局优化、整数/组合、鲁棒优化（含 DRO）：未覆盖。弱凸/复合这一
  结构化非凸类有入口级覆盖 [NLP-S21]。
- 分布式优化：仅 dual averaging 一条入口级覆盖 [NLP-S20]；联邦学习未覆盖。
- 2026-07 之后的新文献：未覆盖。

## 与用户项目的关系

autoresearch-optimization 的 momentum 研究（sources.json 四条 verified-local
momentum 文献是本语料骨架）；optimization-paper-collection 的
nonlinear-programming/ 子目录（Nesterov 1983 完整机器区条目）是
本队最深的单篇锚点。

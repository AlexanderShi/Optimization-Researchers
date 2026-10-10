# Katya Scheinberg · NLP Team 研究者档案（支线档案）

> 主档案（身份全量、模型型 DFO 贡献）见
> `teams/dfo-team/researchers/katya-scheinberg.md`。本档案只收她的
> NLP 侧支线：随机一阶方法的线搜索全局化。依据 arXiv abs 页 +
> Georgia Tech 主页，核实 2026-10-09（verified-web）；未读全文。

## 身份速览（verified-web）

Georgia Tech ISyE Coca-Cola Foundation Chair & Professor；Mathematics of
Operations Research 主编、Mathematical Optimization Society 主席（2025-07
起）；Lagrange Prize、Farkas Prize、SIAM/INFORMS Fellow。详见主档案。

## NLP 核心贡献

### [NLP-S23] 随机线搜索（verified-web）
Paquette, Scheinberg, "A Stochastic Line Search Method with Convergence
Rate Analysis", arXiv:1807.07994（abs 页核实 2026-10-09；期刊版
SIAM J. Optim.——**model-knowledge，需核对**，arXiv 页未列）。
- 摘要核实内容：经典 Armijo 回溯线搜索的随机适配——不要求精确的函数值
  与梯度，只要求「以足够大的固定概率、在动态调整的精度内」可得；
  期望迭代复杂度达到标准一阶方法到近稳定点的最坏情形效率；凸与强凸
  情形的函数值速率与确定性梯度下降一致。
- 对应 04-results.md 条目 NLP-R13。

## 心智模型（与 DFO 侧主档案共享，三重验证见主档案）

1. **概率质量标准，不是期望标准**——NLP 侧证据即 [NLP-S23]：估计以固定
   高概率达标，而非仅无偏+方差有界。
2. **经典骨架的概率化改造**——NLP 侧证据即 Armijo 线搜索的随机化
   [NLP-S23]。

对 NLP Team 的直接意义：随机情形下线搜索不是只能放弃（固定步长/递减
步长并非唯一选择）——在「高概率精度」的 oracle 假设下，经典全局化机制
与确定性速率可以保留 [NLP-S23]。与 momentum 三句话分寸（H4）同属
「随机 ≠ 确定性换噪声」共识的建设性一面。

## 边界

- 仅基于摘要：精度如何动态调整、所需概率下界、复杂度常数需查原文。
- [NLP-S23] 期刊版出处未核实。
- 她的凸优化/QP/内点早期工作与 RL 应用不在本队章程内。

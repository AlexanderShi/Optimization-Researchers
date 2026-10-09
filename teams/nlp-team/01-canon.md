# NLP Team · 正典文献表

验证层级定义见 `standards/grounding.md`。verified-local 工件：
`autoresearch-optimization/.../deep-momentum-vs-dfo-v2/sources.json`（下称
sources.json）与 `optimization-paper-collection/nonlinear-programming/`。
model-knowledge 条目**故意不写卷号页码**——写论文引用前核对。

## verified-local

| ID | 文献 | 定位 | 角色 |
|----|------|------|------|
| NLP-S1 | Nesterov (1983), "A Method for Solving the Convex Programming Problem with Convergence Rate O(1/k²)", Soviet Math. Doklady 27(2) | optimization-paper-collection/nonlinear-programming/nesterov-1983-accelerated-gradient.md（完整机器区：问题设定/假设/机制/主结果/局限，**该条目自标 verified: false，常数标注 unanchored**） | 加速方法原点；本语料最深锚点 |
| NLP-S2 | Sutskever, Martens, Dahl, Hinton (2013), "On the Importance of Initialization and Momentum in Deep Learning", PMLR v28 | proceedings.mlr.press/v28/sutskever13.html (sources.json: src-sutskever-2013-momentum) | momentum 实践面：初始化与调度依赖 |
| NLP-S3 | Kidambi, Netrapalli, Jain, Kakade (2018), "On the Insufficiency of Existing Momentum Schemes for Stochastic Optimization" | openreview.net/forum?id=Sk0uMIqef (src-kidambi-2018-momentum) | 随机情形 momentum 不必然优于调好的 SGD |
| NLP-S4 | Ganesh, Deb, Thoppe, Budhiraja (2023), "Does Momentum Help in Stochastic Optimization? A Sample Complexity Analysis", PMLR v216 | proceedings.mlr.press/v216/ganesh23a.html (src-ganesh-2023-momentum) | 二次+持续噪声下 momentum 不改进采样复杂度 |

## model-knowledge (high)（结论可用；元数据需核对）

| ID | 文献 | 角色 |
|----|------|------|
| NLP-S5 | Nocedal & Wright, *Numerical Optimization* 2e (2006), Springer | 领域教科书基线 |
| NLP-S6 | Conn, Gould, Toint, *Trust-Region Methods* (2000), SIAM | 信赖域理论全书 |
| NLP-S7 | Polyak (1964), heavy ball 方法, USSR Comput. Math. & Math. Phys. | 动量方法原点 |
| NLP-S8 | Nesterov, *Lectures on Convex Optimization*（2004 初版 / 2018 二版）, Springer | 凸优化速率体系 |
| NLP-S9 | Boyd & Vandenberghe, *Convex Optimization* (2004), Cambridge | 凸分析与建模基线 |
| NLP-S10 | Liu & Nocedal (1989), L-BFGS, Math. Programming | 大规模拟牛顿 |
| NLP-S11 | Wächter & Biegler (2006), IPOPT 内点滤波线搜索算法, Math. Programming | 约束 NLP 求解器基线 |
| NLP-S12 | Karush (1939, 学位论文); Kuhn & Tucker (1951, Berkeley 研讨会文集) | KKT 条件出处（注意 Karush 在先） |
| NLP-S13 | Nemirovsky & Yudin (1983), *Problem Complexity and Method Efficiency in Optimization*, Wiley | 一阶方法下界/信息复杂度 |
| NLP-S14 | Lessard, Recht, Packard (2016), IQC 分析, SIAM J. Optim. | heavy ball 全局收敛反例；算法统一分析框架 |
| NLP-S15 | Robbins & Monro (1951), Ann. Math. Statist. | 随机逼近/SGD 原点 |
| NLP-S16 | Bottou, Curtis, Nocedal (2018), "Optimization Methods for Large-Scale Machine Learning", SIAM Review | 随机优化综述 |
| NLP-S17 | Armijo (1966); Wolfe (1969) | 线搜索条件出处 |
| NLP-S18 | Bertsekas, *Nonlinear Programming*, Athena Scientific | 约束优化与对偶教科书 |

## 本地项目工件

| ID | 工件 | 角色 |
|----|------|------|
| NLP-L1 | optimization-paper-collection/_EXTRACT.md | 锚点规范出处 |
| NLP-L2 | autoresearch-optimization/research_runs/（momentum 因子实验、sign-reversal 观察等） | 本地实验证据（注意其审计限定：探索性信号，非确证） |

# DFO Team · 正典文献表

验证层级定义见 `standards/grounding.md`。verified-local 的交叉验证工件：
`autoresearch-optimization/research_runs/deep-momentum-vs-dfo-v2/sources.json`
（下称 sources.json）。model-knowledge 条目**故意不写卷号页码**——写论文引用前核对。

## verified-local（含 DOI/URL，可直接引用）

| ID | 文献 | 定位 | 本语料中的角色 |
|----|------|------|---------------|
| DFO-S1 | Larson, Menickelly, Wild (2019), "Derivative-Free Optimization Methods", Acta Numerica | doi.org/10.1017/S0962492919000060 (sources.json: src-larson-2019-dfo) | 领域权威综述；滚雪球检索的根节点 |
| DFO-S2 | Moré & Wild (2009), "Benchmarking Derivative-Free Optimization Algorithms", SIAM J. Optim. | doi.org/10.1137/080724083 (src-more-2009-benchmarking) | 基准测试方法论：data profiles |
| DFO-S3 | Shi, Xie, Xuan, Nocedal (2022), "Adaptive Finite-Difference Interval Estimation for Noisy Derivative-Free Optimization", SIAM J. Sci. Comput. | doi.org/10.1137/21M1452470 (src-shi-2022-fd-noise) | 噪声下差分区间选择 |
| DFO-S4 | Ghadimi & Lan (2013), "Stochastic First- and Zeroth-Order Methods for Nonconvex Stochastic Programming", SIAM J. Optim. | doi.org/10.1137/120880811 (src-ghadimi-2013-first-zeroth) | 随机 zeroth-order 非凸复杂度 |
| DFO-S5 | Gorbunov, Bibi, Sener, Bergou, Richtárik (2020), "A Stochastic Derivative Free Optimization Method with Momentum" | arxiv.org/abs/1905.13278 (src-gorbunov-2020-smtp) | zeroth-order + momentum（SMTP） |
| DFO-S6 | Hansen (2016), "The CMA Evolution Strategy: A Tutorial" | arxiv.org/abs/1604.00772 (src-hansen-2016-cma) | 进化策略派代表 |
| DFO-S7 | Berahas, Cao, Choromanski, Scheinberg (2019), "A Theoretical and Empirical Comparison of Gradient Approximations in Derivative-Free Optimization" | arxiv.org/abs/1905.01332 (src-berahas-2019-gradient-approximations)；期刊版 Found. Comput. Math.（model-knowledge, 需核对） | 梯度近似方式的统一比较 |
| DFO-S8 | Hansen, Auger, Ros, Mersmann, Tušar, Brockhoff (2021), "COCO: A Platform for Comparing Continuous Optimizers in a Black-Box Setting" | doi.org/10.1080/10556788.2020.1808977 (src-hansen-2021-coco) | 基准平台与 anytime 评估口径 |

## model-knowledge (high)（结论可用；元数据需核对后方可写进论文）

| ID | 文献 | 本语料中的角色 |
|----|------|---------------|
| DFO-S9 | Nelder & Mead (1965), The Computer Journal | 单纯形法原文 |
| DFO-S10 | McKinnon (1998), SIAM J. Optim. | NM 收敛到非稳定点的反例 |
| DFO-S11 | Lagarias, Reeds, Wright, Wright (1998), SIAM J. Optim. | NM 仅有的正面收敛结果（低维/严格凸限定） |
| DFO-S12 | Torczon (1997), "On the Convergence of Pattern Search Algorithms", SIAM J. Optim. | 模式搜索全局收敛理论 |
| DFO-S13 | Kolda, Lewis, Torczon (2003), SIAM Review | 直接搜索综述 |
| DFO-S14 | Audet & Dennis (2006), "Mesh Adaptive Direct Search…", SIAM J. Optim. | MADS：非光滑约束问题的 Clarke 稳定性 |
| DFO-S15 | Powell：COBYLA (1994, 会议文集章节), UOBYQA (2002, Math. Programming), NEWUOA (2006, ⚠️书章节/报告，venue 需核对), BOBYQA (2009, **剑桥 DAMTP 技术报告 2009/NA06，非期刊论文**) | 模型型信赖域方法谱系 |
| DFO-S16 | Conn, Scheinberg, Vicente (2009), *Introduction to Derivative-Free Optimization*, SIAM | 模型型方法理论基础（fully-linear 模型） |
| DFO-S17 | Audet & Hare (2017), *Derivative-Free and Blackbox Optimization*, Springer | 教材级参考 |
| DFO-S18 | Kiefer & Wolfowitz (1952), Ann. Math. Statist. | 随机逼近差分路线起点 |
| DFO-S19 | Spall (1992), "…Simultaneous Perturbation Gradient Approximation" (SPSA), IEEE Trans. Autom. Control | 每步 2 次评估的随机扰动路线 |
| DFO-S20 | Nesterov & Spokoiny (2017), "Random Gradient-Free Minimization of Convex Functions", Found. Comput. Math. | 高斯平滑随机无梯度方法，凸情形复杂度 |
| DFO-S22 | Moré & Wild (2011), "Estimating Computational Noise"（SIAM J. Sci. Comput.，需核对）| ECNoise：计算噪声估计 |

## verified-web（联网核实，注明核实日期与一手页面）

| ID | 文献 | 定位 | 本语料中的角色 |
|----|------|------|---------------|
| DFO-S21 | Duchi, Jordan, Wainwright, Wibisono, "Optimal rates for zero-order convex optimization: the power of two function evaluations"；期刊版 IEEE Trans. Inf. Theory 2015（venue 据 Scholar 个人页） | arXiv:1312.2139（abs 页核实 2026-10-09） | 两点估计 √d 退化因子 + 信息论下界 sharp；详见 researchers/john-duchi.md |
| DFO-S23 | Duchi, Bartlett, Wainwright, "Randomized Smoothing for Stochastic Optimization" (2011/v2 2012)；期刊版 SIAM J. Optim.（model-knowledge，需核对——arXiv 页未列期刊引用） | arXiv:1103.4296（abs 页核实 2026-10-09） | 随机平滑：非光滑凸随机优化的方差最优速率（期望+高概率），可分布式 |

## 具名研究者档案

| 研究者 | 档案 | 核实基础 |
|--------|------|---------|
| John Duchi (Stanford) | `researchers/john-duchi.md` | Scholar 个人页 + 2 篇 arXiv abs 页（2026-10-09） |

## 本地项目工件（非文献，但可引用的证据）

| ID | 工件 | 角色 |
|----|------|------|
| DFO-L1 | autoresearch-optimization/docs/reviews/2026-07-25-professional-research-audit.md | 「(d+1) 口径改变排名」「只验证存在≠验证内容」的记录 |
| DFO-L2 | autoresearch-optimization/research_runs/*/（evidence_report、protocol 等） | momentum-vs-DFO 实验的本地数据 |

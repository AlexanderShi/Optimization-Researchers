# DFO Team · 流派：共识与分歧

## 四大流派

| 流派 | 核心思想 | 代表 | 理论货币 |
|------|---------|------|---------|
| 直接搜索 (direct search) | 只比较函数值，不建模型：单纯形变形 (NM [DFO-S9])、模式/网格搜索 (GPS [DFO-S12]、MADS [DFO-S14]) | Torczon, Kolda-Lewis-Torczon, Audet-Dennis | 全局收敛性（lim inf ‖∇f‖→0 或 Clarke 稳定性） |
| 模型型信赖域 (model-based) | 用插值/回归模型局部代理 f，在信赖域内优化模型 | Powell 谱系 [DFO-S15]、Conn-Scheinberg-Vicente [DFO-S16] | fully-linear/quadratic 模型精度 + 信赖域收敛理论 |
| 随机 zeroth-order | 随机方向上的差分估计梯度，接入一阶方法框架 | Kiefer-Wolfowitz [DFO-S18]、SPSA [DFO-S19]、Nesterov-Spokoiny [DFO-S20]、Ghadimi-Lan [DFO-S4]、SMTP [DFO-S5] | oracle 复杂度（含维度因子） |
| 进化策略 (ES) | 适应多元采样分布（协方差自适应） | CMA-ES [DFO-S6, DFO-S8] | 基准测试表现；理论保证较弱 |

## 共识（各派都认的框架，蒸馏进「框架概览」）

1. **信息口径是第一公民**：比较必须以函数评估次数计费，而非迭代次数——
   一个 simplex 梯度 ≈ n+1 次评估，zeroth-order 的梯度估计每步也要付维度代价
   [DFO-S4 content, DFO-S8 content]。
2. **方法选型由问题结构决定**：噪声、维度、约束、单次评估成本共同决定该用哪派
   [DFO-S1 content：「derivative-free methods use different structural assumptions
   and should be selected with attention to noise, dimension, constraints, and the
   cost of obtaining objective information」(sources.json 原文)]。
3. **基准测试用 profiles 不用单点排名**：data profiles + performance profiles，
   fixed-budget 与 fixed-target 两视角都要 [DFO-S2 content (sources.json)]。
4. **噪声改变一切**：差分区间要在截断误差与测量误差之间权衡 [DFO-S3 content]；
   确定性保证不自动迁移到噪声情形。
5. **光滑问题上模型型方法通常占优**（Moré-Wild 基准证据 [DFO-S2]；
   定性结论，model-knowledge）。

## 分歧（保留原样，蒸馏进「流派对比」）

1. **Nelder–Mead 的地位**：实践派视其为首选默认（简单、鲁棒的口碑）；
   理论派指出它没有一般收敛保证且存在光滑凸反例 [DFO-S10]，正面结果仅限
   低维/严格凸的受限情形 [DFO-S11]。两派都对——分歧在「可用」与「可证」的
   权重。
2. **ES vs 经典 DFO 的文化鸿沟**：ES 社区以 COCO 基准表现立论 [DFO-S8]，
   经典 DFO 社区以收敛定理立论 [DFO-S16]；CMA-ES 在病态/多峰问题的实证
   强势与它较薄的收敛理论并存 [DFO-S6]。
3. **随机 zeroth-order 是否算「DFO」**：ML 社区（[DFO-S4, S20, S21]路线）与
   经典 DFO 社区（[DFO-S1, S16]路线）术语、假设、评价口径均不同；
   前者谈期望复杂度与维度因子，后者谈确定性收敛与实际评估预算。
4. **momentum 在 zeroth-order 里的价值**：SMTP 证明了带 momentum 的
   zeroth-order 方法的收敛性 [DFO-S5]，但「是否带来数量级改进」在语料中
   没有定论（用户自己的 momentum-vs-DFO 实验 [DFO-L2] 正是在做这件事）。

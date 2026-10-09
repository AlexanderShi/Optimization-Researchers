# 蒸馏记录

## 2026-10-09 · 首次蒸馏

- 语料版本：b007570（首次语料提交）
- 协议：DISTILL.md Phase 0–5，纯本地语料，零 WebSearch
- 产物：`skills/dfo-team/SKILL.md`、`skills/nlp-team/SKILL.md`
- 执行模型：claude-fable-5

### 质量门结果

| 门 | 结果 | 说明 |
|----|------|------|
| G1 语料封闭 | PASS | 两份 skill 中全部事实性声明带语料 ID；无 ID 的仅为流程性指令 |
| G2 引用闭包 | PASS | 全部（作者,年份）对均存在于对应 01-canon.md。自查中发现并修正一次 DFO 来源索引 S17–S19 编号错位 |
| G3 数学纪律 | PASS | 全部速率为定性+假设+proved-vs-cited；无精确常数；ZO 维度因子保留（DFO-R1/R2）；噪声模型显式（DFO-R7、F4） |
| G4 诚实边界 | PASS | 两份均含：蒸馏日期、语料版本 b007570、文献覆盖截止 ~2026-07、语料缺口清单、验证层级声明 |
| G5 禁区完整性 | PASS | DFO 9/9 条、NLP 11/11 条全量移植 |
| G6 试答 | PASS | 见下 |

### G6 试答摘要

1. **「10维、带噪声、评估贵的黑盒问题选什么？」** → 先问噪声类型；先估噪声
   [DFO-S22] 再定差分区间 [DFO-S3]；低维+评估贵首选模型型信赖域 [DFO-S2, S16]；
   报告声明 (d+1) 口径 [DFO-L1]。全程带 ID ✓
2. **「Nelder–Mead 有收敛保证吗？」** → 无一般保证，McKinnon 反例 [DFO-S10]，
   正面结果仅受限情形 [DFO-S11]，正式对比须配有保证的方法 [H5]。命中陷阱清单 F2 ✓
3. **「momentum 能加速 SGD 吗？」** → H4 三句话：确定性凸有可证加速 [NLP-R2]；
   heavy ball 有光滑强凸反例 [NLP-R4]；随机情形不必然改进采样复杂度
   [NLP-R5]、实践收益与初始化/调度耦合 [NLP-R6]。分寸完整 ✓

### 安装

复制到 `C:\Users\sr881\.claude\skills\dfo-team\`、`C:\Users\sr881\.claude\skills\nlp-team\`。

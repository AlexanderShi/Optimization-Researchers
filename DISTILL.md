# DISTILL.md — 自包含蒸馏协议

输入：本 repo。输出：`skills/<team>/SKILL.md`（可直接复制进 `~/.claude/skills/`）。
除本 repo 外不需要任何东西；**蒸馏全程禁止 WebSearch / WebFetch**。

## Phase 0 — 装载标准

1. 读 `standards/grounding.md`（接地标准，所有后续步骤的约束）。
2. 读 `standards/skill-template.md`（输出骨架）。

## Phase 1 — 读语料

按编号顺序读目标团队目录全部六个文件：
`00-charter → 01-canon → 02-schools → 03-heuristics → 04-results → 05-failure-modes`，
以及 `researchers/*.md`（若存在）——研究者档案的方法论立场进 skill 的
对应学派/启发式部分，身份与贡献进来源索引。

读的时候建三张工作表（内部使用）：
- **ID 表**：全部 `[XXX-S*]`（来源）与 `[XXX-R*]`（结果）ID —— 之后 skill 里
  只允许引用表内 ID。
- **共识/分歧表**：02 中标注为共识的进「框架概览」，分歧的进「流派对比」，
  绝不把分歧写成共识。
- **禁区表**：05 的全部条目。

## Phase 2 — 综合

把语料综合为 skill 的五个承重部分：

| skill 部分 | 来源 | 规则 |
|-----------|------|------|
| 框架概览 | 00 + 02 共识部分 | 每条框架后附支撑 ID |
| 流派对比 | 02 分歧部分 | 保留分歧原样，标明「A派主张…，B派主张…」 |
| 决策启发式 | 03 | 每条保留案例/出处 ID |
| 关键结果速查 | 04 | 逐条照搬：定性速率 + 假设 + proved-vs-cited + ID，不改写、不加精确常数 |
| 绝不做清单 | 05 整体移植 | 一条不删 |

综合时的三条硬规则：
1. 不新增语料外的事实。觉得缺 ⇒ 记入「语料缺口」清单（Phase 4 写进诚实边界）。
2. 不调和分歧、不抹平矛盾。
3. 表达规范（最小化形式、伪代码+逐步手算、proved-vs-cited）写进 skill 的
   回答工作流，不是写成口号。

## Phase 3 — 填模板

按 `standards/skill-template.md` 生成 `skills/<team-slug>/SKILL.md`。
frontmatter description 控制在 300 字内：一句定位 + 触发词 + 一句防误触。

## Phase 4 — 质量门（全过才算蒸馏完成）

- **G1 语料封闭**：扫描 SKILL.md 中每个事实性声明，确认带语料 ID。
  无 ID 的声明：要么补 ID，要么删除。
- **G2 引用闭包**：SKILL.md 中出现的每个（作者, 年份）均存在于 `01-canon.md`。
  grep 核对，发现语料外引用 = 直接不通过。
- **G3 数学纪律**：每条速率/定理带假设 + ID + proved-vs-cited；无精确常数；
  zeroth-order 速率必须保留维度因子；噪声模型已声明。
- **G4 诚实边界**：必须包含——语料截止日期（= 本次蒸馏日期）、Phase 2 记录的
  语料缺口、验证层级声明（哪些结论是 model-knowledge 级、写论文前需核对元数据）。
- **G5 禁区完整性**：05-failure-modes 的条目逐条出现在 skill 的「绝不做」清单。
- **G6 试答**：用 skill 草稿回答 3 个测试问题（见下），检查回答是否全程带 ID、
  遇到语料外问题是否如实说「语料未覆盖」：
  1. 「10维、带噪声、每次评估很贵的黑盒问题，选什么方法？」（选型题，应命中 03）
  2. 「Nelder–Mead 有收敛保证吗？」（陷阱题，应命中 05/04 的反例条目）
  3. 「momentum 能加速 SGD 吗？」（分寸题，应区分确定性加速 vs 随机采样复杂度，
     命中 04 相应条目）

## Phase 5 — 安装

```powershell
Copy-Item -Recurse skills\<team-slug> $HOME\.claude\skills\<team-slug>
```

安装后在本 repo 的 git log 里留一条 commit，注明蒸馏日期与语料版本（commit hash），
使 skill ↔ 语料版本可对账。

## 更新循环

语料改了（新文献、勘误、新结果）→ 重跑 Phase 1–5。蒸馏是纯函数：
同一语料版本必须产出同样的事实集，skill 之间的差异只允许来自表述。

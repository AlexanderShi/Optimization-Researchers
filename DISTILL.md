# DISTILL.md — 自包含蒸馏协议

输入：本 repo 的 `teams/<team>/`。输出：`teams/<team>/SKILL.md`（放在语料旁边；安装时只复制这一个文件
到 `~/.claude/skills/<team>/`）。除本 repo 外不需要任何东西；**蒸馏全程禁止 WebSearch / WebFetch**。
质量门的机械部分由 `scripts/distill_check.py` 与 `scripts/distill_audit.py` 执行，协议见
`standards/distill-gates.md`；运行纪律（分支、用量窗口、Windows）见 `RUNBOOK.md`。

## Phase 0 — 装载标准

1. 读 `standards/grounding.md`（接地标准，所有后续步骤的约束）。
2. 读 `standards/skill-template.md`（输出骨架）。
3. 读 `standards/researcher-extraction.md`（研究者档案的提炼标准：
   心智模型三重验证、矛盾处理、信息不足处理——源自 nuwa-skill 的
   提炼方法论，按主题型语料适配）。
4. 读 `standards/distill-gates.md`（七道门里哪些由脚本判、怎么判；G7 抽审协议；语料版本戳的写法）。
5. 跑 `python3 -X utf8 scripts/distill_check.py teams/<team> --lint`：语料本身要 0 ✗ 才开始读
   （重复 ID、04 缺状态行、引用了不存在的 ID 这类问题在语料侧修，不在 skill 侧绕）。

## Phase 1 — 读语料

按编号顺序读目标团队目录全部六个文件：
`00-charter → 01-canon → 02-schools → 03-heuristics → 04-results → 05-failure-modes`，
以及 `researchers/*.md`（若存在）——研究者档案的方法论立场进 skill 的
对应学派/启发式部分，身份与贡献进来源索引。

读的时候建三张工作表（内部使用）：
- **ID 表**：全部 `[XXX-S*]`（来源）、`[XXX-R*]`（结果）、`[XXX-L*]`（本地工件）ID 与 03 的 H*、05 的 F*
  标签—— skill 里只允许引用表内 ID（`distill_check.py --lint` 的 `i lint ids` 行给出每类的数量，可对账）。
  跨队引用（如 NLP skill 引 `[DFO-R7]`）允许，脚本到对方语料里解析。
- **共识/分歧表**：02 中标注为共识的进「框架概览」，分歧的进「流派对比」，
  绝不把分歧写成共识。
- **禁区表**：05 的全部条目。

## Phase 2 — 综合

把语料综合为 skill 的五个承重部分：

| skill 部分 | 来源 | 规则 |
|-----------|------|------|
| 框架概览 | 00 + 02 共识部分 | 每条框架后附支撑 ID |
| 流派对比 | 02 分歧部分 | 保留分歧原样，标明「A派主张…，B派主张…」 |
| 决策启发式 | 03 | 每条保留案例/出处 ID；标签沿用 03 的 H* 编号 |
| 关键结果速查 | 04 | 逐条照搬：定性速率 + 假设 + proved-vs-cited + ID，不改写、不加精确常数 |
| 绝不做清单 | 05 整体移植 | 一条不删，标签沿用 F* 编号 |

综合时的四条硬规则：
1. 不新增语料外的事实。觉得缺 ⇒ 记入「语料缺口」清单（Phase 4 写进诚实边界）。
2. 不调和分歧、不抹平矛盾。
3. 表达规范（最小化形式、伪代码+逐步手算、proved-vs-cited）写进 skill 的
   回答工作流，不是写成口号。
4. 研究者档案中只有 ✅三重验证通过 的心智模型可升格为 skill 的纪律/
   启发式条目；降级为工作信条的留在档案里，不进 skill
   （standards/researcher-extraction.md）。这样升格的启发式用 03 之后的编号（如 H9），
   `distill_check.py` 会以 `unknown-label` ⚠ 提示——在 DISTILLATION_LOG 里写明出自哪条心智模型；
   更稳的做法是同时把它写进 03-heuristics，让下一次蒸馏不依赖这次的判断。

## Phase 3 — 填模板

按 `standards/skill-template.md` 生成 `teams/<team-slug>/SKILL.md`。
frontmatter description 控制在 300 字内（不计空白）：一句定位 + 触发词 + 一句防误触。
语料版本写**语料最后一次改动所在的提交**（`git log -1 --format=%h -- teams/<team-slug>`，
在改 SKILL.md 之前取），头部语料契约与诚实边界两处写同一个 hash；语料有未提交改动时先提交语料。

## Phase 4 — 质量门（全过才算蒸馏完成）

先跑 `python3 -X utf8 scripts/distill_check.py teams/<team-slug>`：0 ✗，每条 ⚠ 要么改掉、要么在
DISTILLATION_LOG 里写明为什么留着。脚本判「有没有」，下面每道门里「对不对」的部分仍由人做。

- **G1 语料封闭**：SKILL.md 中每个事实性声明带语料 ID。脚本：每个 ID 存在（含跨队）、H/F 标签在 03/05
  里存在、承重部分没有 ID 的条目列出来。人：逐条看 `no-id`——是事实就补 ID 或删，是表达约定就留。
- **G2 引用闭包**：SKILL.md 中出现的每个（作者, 年份）均存在于 `01-canon.md`。脚本：同一 canon 行
  须同时含年份与全部姓氏；语料外引用 = ✗ 直接不通过（`--show-pairs` 看对账表）。
- **G3 数学纪律**：每条速率/定理带假设 + ID + proved-vs-cited；无精确常数；
  zeroth-order 速率必须保留维度因子；噪声模型已声明。脚本：结果表每行的 ID / 假设 / 状态列、
  承重部分里语料没有的数字。人：维度因子与噪声模型（读 G7 的 partial）。
- **G4 诚实边界**：必须包含——语料截止日期（= 本次蒸馏日期）、语料版本、Phase 2 记录的
  语料缺口、验证层级声明（哪些结论是 model-knowledge 级、写论文前需核对元数据）。脚本：四项齐全、
  两处 hash 一致、hash 是本仓库提交且在当前历史上、语料自该提交后未变。
- **G5 禁区完整性**：05-failure-modes 的条目逐条出现在 skill 的「绝不做」清单；04 的每条结果、03 的每条
  启发式同样逐条在。脚本：`missing-F` / `missing-R` / `missing-H` 为 ✗；01 里一次没被引的 ID 为 ⚠。
- **G6 试答**：用 skill 草稿回答 `00-charter.md`「试答题」小节的全部题目（四类：选型、陷阱、分寸、
  语料外；脚本查小节存在、≥3 题、每题带应命中 ID、含语料外题），检查回答是否全程带 ID、
  是否命中该题标注的条目、遇到语料外问题是否如实说「语料未覆盖」。答案摘要记入 DISTILLATION_LOG。
  语料还没写试答题时用下面三题兜底：
  1. 「10维、带噪声、每次评估很贵的黑盒问题，选什么方法？」（选型题，应命中 03）
  2. 「Nelder–Mead 有收敛保证吗？」（陷阱题，应命中 05/04 的反例条目）
  3. 「momentum 能加速 SGD 吗？」（分寸题，应区分确定性加速 vs 随机采样复杂度，命中 04 相应条目）
- **G7 声明抽审**：`scripts/distill_audit.py teams/<team-slug> --sample --n 20` 抽 20 条带 ID 的声明配上
  语料证据，交**另一个**零上下文 agent 判定 supported / partial / unsupported / uncheckable，`--report` 写进
  `teams/<team-slug>/CLAIM-AUDIT.md`。unsupported 必须为 0（有则改声明或改引用，换 `--seed` 再抽一轮）；
  partial 逐条收窄或改引真正支持它的 ID，改完重跑 `distill_check.py`，最好让审计 agent 复判收窄后的那几条。
  G1–G5 证明「引得到」，这一道证明「语料真这么说」（协议与 prompt 见 `standards/distill-gates.md` 第三节）。

## Phase 5 — 安装

```powershell
New-Item -ItemType Directory -Force $HOME\.claude\skills\<team-slug> | Out-Null
Copy-Item teams\<team-slug>\SKILL.md $HOME\.claude\skills\<team-slug>\SKILL.md
python3 -X utf8 scripts\distill_check.py teams\<team-slug> --installed   # install 一行应为「与仓库一致」
```

安装后在本 repo 的 git log 里留一条 commit，注明蒸馏日期与语料版本（commit hash），
使 skill ↔ 语料版本可对账；在 `teams/DISTILLATION_LOG.md` 顶部记一条（语料版本、范围、`distill_check.py`
的 ✗/⚠ 与处理、G6 试答摘要、G7 计数、执行模型）。

## 更新循环

语料改了（新文献、勘误、新结果）→ 重跑 Phase 0–5。蒸馏是纯函数：
同一语料版本必须产出同样的事实集，skill 之间的差异只允许来自表述。
`distill_check.py` 的 `stamp` 检查会在语料改动而 skill 未重蒸馏时报 ⚠（`--strict-stale` 时 ✗）；
只是历史被重写（hash 失效、语料未变）时按脚本给出的同树提交改戳并记一条，不必重蒸馏。

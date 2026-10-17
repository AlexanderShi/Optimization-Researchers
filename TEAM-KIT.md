# TEAM-KIT · 逐人研究者 Skill 流水线

本仓库内置了 nuwa-skill 的**研究 Skill / 研究团队工具链**（team-kit），用于逐人蒸馏研究者的
研究方法并组成圆桌团队。它与 [DISTILL.md](./DISTILL.md)（封闭语料 → 团队级 skill）是两条
独立流水线：

| | DISTILL.md | team-kit（本文件） |
|---|---|---|
| 输入 | `teams/<team>/` 封闭语料，禁联网 | 研究者公开发表（OpenAlex / DBLP / arXiv 全文）+ 网络调研 |
| 产物 | `teams/<team>/SKILL.md`（放在语料旁边），每条事实带语料 ID | `product/<team>/<member>/`（SKILL.md + references/research 证据台账）+ 圆桌 skill |
| 质量门 | G1–G6 | `scripts/quality_check.py` 研究模式 + `scripts/team_check.py` + 摘录逐字核对 + 引用闭包（`check_citations.py`）+ 声明抽审（`audit_claims.py`，`references/claim-audit.md`） |
| 入口 | DISTILL.md | `references/research-team-playbook.md` |

## 来源

整体同步自 AlexanderShi/nvwa-skill 提交 `eb012fa`（kit 由 2026-09-27/28 的 team-kit 系列提交
构建），2026-10-09 逐字节复制，零修改：

| 本仓库路径 | nvwa-skill 原路径 | 说明 |
|-----------|------------------|------|
| `scripts/` | `scripts/` | 52 个文件：发表全表、全文获取、读卡、台账、团队状态；`workflows/` 为保存好的 T1–T4 工作流 |
| `references/` | `references/` | playbook、研究提炼框架、研究 skill 模板、论文卡片、评分卡、`team-templates/` |
| `references/nuwa-SKILL.md` | `SKILL.md`（nuwa 根 skill） | **冻结副本**，仅供 kit 文档中「SKILL.md 特殊场景 > 研究Skill / 研究团队Skill」等引用查阅；本仓库不把它当 skill 加载 |
| `product/` | `product/` | 团队产物目录，名称保持一致，因此 kit 的默认路径与团队文档内的 `product/...` 链接原样有效 |

kit 文档里的「[skill目录]」「女娲仓库根目录」即**本仓库根目录**。不依赖外部 nvwa-skill 仓库。

## 阅读顺序

1. `references/research-team-playbook.md` —— 团队模式总纲：T1 基础 skill → T2 团队层（圆桌座位、
   fault lines）→ T3 全文深读（T3.1–T3.8）→ T4 增量维护；第八节是加/减成员与更新
2. `references/research-extraction-framework.md` —— 单个研究者的 6 路调研分工、研究方法四重验证、
   代表作解剖、阶段工作流重建；第十二节是全文深读工具链的步骤与参数
3. `references/research-skill-template.md` —— 研究 skill 的输出模板（导师模式、研究诚信规则、任务路由）
4. `references/paper-reading-card.md` —— 论文卡片格式；`references/fidelity-scorecard.md` 的「研究Skill变体」
5. `scripts/workflows/README.md` —— T1–T4 工作流的参数、`dry_run.mjs` 预览与 `selftest.sh`
6. `references/team-templates/` —— `new_team.py` 铺团队目录用的模板（README、DEEP-READING、圆桌 SKILL、team.json 示例）

## 运行要求

- Python 3（脚本只用标准库，无需 pip），从仓库根运行：`python3 scripts/<脚本> product/<team>[/<member>]`
- Node（`scripts/workflows/dry_run.mjs`、`make_args.mjs`）；`team-*.js` 是 Claude Code Workflow 脚本
- 联网：`fetch_publications.py`（OpenAlex）、`dblp_works.py`（DBLP SPARQL）、`acquire_fulltexts.py` /
  `fetch_fulltexts.py`（arXiv 等开放全文）。只用开放来源，不绕付费墙
- 下载的 PDF/全文/私人材料由根 `.gitignore` 忽略（规则与 `new_team.py` 打印的一致），不要 `git add -f`

## 常用命令

```
python3 scripts/team_status.py product/dfo-team                  # 每人到了哪一步
python3 scripts/team_status.py product/dfo-team --coverage       # 覆盖表（可贴进 DEEP-READING.md）
python3 scripts/check_links.py product/nonlinear-team            # 相对链接与锚点
python3 scripts/team_check.py product/dfo-team                   # 团队整体检查（含 quality_check、引用闭包）
python3 scripts/check_citations.py product/dfo-team --methods    # 引用闭包：每条 [card S012 pp. …] 都指向存在、读过、页码在范围内的卡片；另报每个方法的证据数
python3 scripts/audit_claims.py product/dfo-team/<member> --sample --n 20 --out $S/audit-<member>.json   # 声明抽审包（零上下文 agent 判定后 --report）
python3 scripts/new_team.py product/<new-team>/team.json         # 按 team.json 铺新团队
python3 scripts/new_team.py product/<team>/team.json --add-member <slug>
bash scripts/workflows/selftest.sh product/dfo-team              # kit 自检（以 dfo-team 为已完成样例）
```

2026-10-09 在本仓库（Windows 11，Python 3.13，Node 24）验证：

- `team_status.py` 两队正常；`check_links.py` dfo-team 79 文件、nonlinear-team 105 文件均 0 断链
- `team_check.py product/dfo-team`：32 项检查 0 失败、5 跳过（摘录核对需先 `acquire_fulltexts.py` 下载全文）
- `workflows/selftest.sh product/dfo-team`：全部通过（14 个工作流预览、9 个 `dry_run.mjs --team`、
  脚本编译与交付闸门）
- 扩展演练：`new_team.py --init` 起草 team.json + 按模板铺出新团队目录（README、DEEP-READING、
  圆桌 SKILL.md、成员资源目录）全部在本仓库内完成，未读任何外部仓库

**Windows 注意**：Python 脚本要用 `python3 -X utf8` 或设 `PYTHONUTF8=1`，否则控制台 cp1252
编不了 ✓ 等字符会以退出码 1 失败；`selftest.sh` 也要在 `PYTHONUTF8=1` 下跑。

## 本仓库对 kit 的本地修改（与 nvwa-skill 的差异）

| 文件 | 修改 | 原因 |
|------|------|------|
| `scripts/workflows/team-*.js`（9 个文件，各 2 处） | `args.repo` / `args.scratch` 的绝对路径检查由 `startsWith('/')` 改为同时接受 `C:\…` 的正则 `/^(?:[A-Za-z]:[\\/]\|\/)/` | 原检查只认 POSIX 路径，Windows 上 Node 解析出 `C:\…` 导致全部工作流在本机拒绝启动；`args.team` 的「必须是相对路径」检查未动 |

| `scripts/check_citations.py`（新增，2026-10-10） | 研究Skill的引用闭包检查：SKILL.md、账本、技术目录、学生模式文件、01–09 里每条 `[card S012 pp. …]` 必须指向存在的卡片，页码只在 full / partial 卡片上且不超过 INDEX 页数，替代版本写成版本引用；圆桌的 `[<slug> card …]` 同样；`--methods` 报每个方法的证据数 | 此前只有摘录逐字核对，卡片 ID / 页码没有闸门。首跑在 dfo-team 上抓到：Audet S025（37 处引 1998 报告版页码，卡片却登记为 unreadable）、Scheinberg S133（同类，5 处）——前者已是 `TR` 版本引用，后者补上 `v2.0` 标记 |
| `scripts/audit_claims.py` + `references/claim-audit.md`（新增，2026-10-10） | 声明→证据抽样审计：抽 N 条带页码的声明配上所引卡片全文成审计包，交零上下文 agent 判定 supported / partial / unsupported / uncheckable，报告追加到 `<M>/references/research/10-claim-audit.md` | 引用闭包只证明「引得到」，这一层证明「卡片真这么说」；两个 agent 分离（SkillLens：自评准确率 46.4%） |
| `scripts/team_check.py` | 每位成员新增 `citations` 一项（深读档），团队级新增圆桌的 `citations` | 交付闸门含引用闭包 |
| `scripts/workflows/team-synthesize.js`、`team-tighten.js`、`team-increment.js`、`team-integrate.js` | 闸门清单里加 `check_citations.py`（synthesize 的 fidelity 复核员第 4 项改用脚本） | 每次改 SKILL.md / 账本的步骤都过引用闭包 |
| `references/research-team-playbook.md`、`scripts/workflows/README.md`、`references/research-extraction-framework.md` §十一、`references/paper-reading-card.md` §四、`references/fidelity-scorecard.md` | 相应的闸门行、命令、失败模式与引用规则 | 文档同步 |
| `scripts/acquire_fulltexts.py`（2026-10-17） | 新增 `digit_share()` / `digits_lost()`：万字以上的拉丁文字文本，数字占非空白字符不到 0.5% 即判为数字字体层损坏，自动 OCR；OCR 结果的数字比例至少翻倍（再加 0.3 个百分点）、常用词比例不低于原来的八成才采用；没装 tesseract 时打印警告 | 乱码检测只看常用词和控制字符，抓不到「正文完好、数字全丢」的文字层：Nocedal 的 97 篇全文里有 26 篇如此（含 L-BFGS 1989、L-BFGS-B、Acta Numerica 1992），第 1 轮读卡只能读正文，表格、常数、定理全空。校准：26 篇坏文本抓到 24 篇，本仓库 1112 篇正常全文 0 误报；S088 端到端自动 OCR 后数字比例 0 → 3.1% |
| `scripts/verify_card_quotes.py`（2026-10-16） | `norm()` 删掉 U+FFFE | pypdfium2 把行末断词写成 U+FFFE（`com￾prehensive`），Nocedal 的 91 篇全文里有 59 篇如此，读卡 agent 只好绕开这些词；删掉后断词处逐字匹配，真连字符的词（`quasi￾Newton`）靠宽松比较。Curtis 180 条摘录结果不变 |

除此之外 `scripts/`、`references/` 与 nvwa-skill `eb012fa` 逐字节一致。再从 nvwa 同步时注意
不要覆盖掉这些修改（或同步后重跑 `selftest.sh` 和 `check_citations.py product/dfo-team` 确认）。

## 在 Claude Code 里的入口

仓库自带项目级 skill `.claude/skills/optimization-researchers/SKILL.md`：在本仓库内启动 session
（或从父目录启动后首次接触本仓库）时自动加载，把「蒸馏 X 加入 DFO team」「加成员」「搭新团队」
「重跑蒸馏」这类请求分流到 DISTILL.md 或本文件，不需要安装 nuwa-skill。
同名时个人 skill（`~/.claude/skills/`）优先于项目 skill，因此它的名字刻意不与任何已安装 skill 重合。

## 与语料流水线的命名区分

- `standards/skill-template.md`（团队级 skill 模板，DISTILL.md 用）≠ `references/skill-template.md`
  （nuwa 人物 skill 模板）≠ `references/research-skill-template.md`（研究 skill 模板，team-kit 用）
- `standards/researcher-extraction.md` 是从 `references/extraction-framework.md` 移植的语料版；
  team-kit 自己用 `references/research-extraction-framework.md`
- 要把 team-kit 蒸馏出的研究者纳入封闭语料，仍需按 `standards/researcher-extraction.md` 另写
  `teams/<team>/researchers/<name>.md` 并通过 `standards/grounding.md` 的锚点规则

## 更新 kit

```
git -C <nvwa-skill> archive HEAD scripts references SKILL.md | tar -x -C <本仓库>
mv SKILL.md references/nuwa-SKILL.md
```

然后 `diff -rq` 核对、在 `teams/DISTILLATION_LOG.md` 记一条、提交信息注明源 commit。

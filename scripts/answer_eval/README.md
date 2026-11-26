# answer_eval · 回答质量的盲评

[English](README.en.md) | 中文

改了 `references/answer-standard.md`，或者改了某类 skill 的回答方式之后，用这里的九道题检验：同一道题由
旧版 skill、新版 skill、不带 skill 各答一遍，交给只看得到三份回答的评审 agent 盲评。写法好不好，闸门脚本
查不出来，只有读回答才看得出来。

| 文件 | 用途 |
|------|------|
| `questions.json` | 九道题：研究者 skill 五道（Curtis、Powell、Grossmann；MILP 的 Achterberg、LP 的 Forrest）、语料团队一道（NLP Team）、圆桌一道、Lead 两道（仓库选址；每日运输 LP，5 分钟时限、无商业授权） |
| `judge_prompt.md` | 评审 agent 的说明：六个维度各 1–5 分、排名、能否原样转发、不专业之处、技术错误 |
| `answer_eval.py` | `prep` 建盲评目录与 key.json；`swaps` 核对评审有没有把意见记错字母；`summary` 揭盲并汇总；`form` 数流程用语、标签、免责声明的位置 |

做法（2026-11-14 第一次运行的经验，见 `teams/DISTILLATION_LOG.md` 同日「回答标准」一条）：

1. 每道题、每个版本开一个零上下文 agent：读完整个 SKILL.md 再照做，把用户会看到的回复原样写进
   `<run>/{old,new,none}/<ID>.md`。圆桌和 Lead 只保存最终方案那一段，三份回答才都是单篇文档。
2. 三个版本用同一个模型跑；模型换了就整题重跑，记进 LOG。
3. `python3 -X utf8 scripts/answer_eval/answer_eval.py prep <run>`，再给每个评审目录开一个 agent，只告诉它去读
   那里的 `instructions.md`、别的文件都不打开。每题两位评审，字母顺序错开一位。
4. 揭盲前先跑 `swaps <run>`：评审偶尔把意见记在错的字母下（2026-11-15 十六份评审里有一份把 B、C 对调）。
   脚本按意见里引用的原文在 A/B/C 里的出处核对，整组对调时写 `verdict_corrected.json`，`summary` 优先读它；
   没有引文可查的评审要人工读一遍。
5. `summary <run> --detail new` 看新版被挑出的问题，改标准、`answer_standard.py --apply`，挑一两道题重跑确认。

成本参考：一份带 skill 的回答约 25–50 万子 agent token、20–45 分钟；Lead 一份约 30–36 万 token（不含它内部的
团队与 lead agent）、65–110 分钟（含合成实例实测与追问，四份并行时）；一位评审约 15–21 万 token。

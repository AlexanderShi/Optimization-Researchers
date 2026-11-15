# answer_eval · 回答质量的盲评

改了 `references/answer-standard.md`，或者改了某类 skill 的回答方式之后，用这里的六道题检验：同一道题由
旧版 skill、新版 skill、不带 skill 各答一遍，交给只看得到三份回答的评审 agent 盲评。写法好不好，闸门脚本
查不出来，只有读回答才看得出来。

| 文件 | 用途 |
|------|------|
| `questions.json` | 六道题：研究者 skill 三道（Curtis、Powell、Grossmann）、语料团队一道（NLP Team）、圆桌一道、Lead 一道 |
| `judge_prompt.md` | 评审 agent 的说明：六个维度各 1–5 分、排名、能否原样转发、不专业之处、技术错误 |
| `answer_eval.py` | `prep` 建盲评目录与 key.json；`summary` 揭盲并汇总；`form` 数流程用语、标签、免责声明的位置 |

做法（2026-11-14 第一次运行的经验，见 `teams/DISTILLATION_LOG.md` 同日「回答标准」一条）：

1. 每道题、每个版本开一个零上下文 agent：读完整个 SKILL.md 再照做，把用户会看到的回复原样写进
   `<run>/{old,new,none}/<ID>.md`。圆桌和 Lead 只保存最终方案那一段，三份回答才都是单篇文档。
2. 三个版本用同一个模型跑；模型换了就整题重跑，记进 LOG。
3. `python3 -X utf8 scripts/answer_eval/answer_eval.py prep <run>`，再给每个评审目录开一个 agent，只告诉它去读
   那里的 `instructions.md`、别的文件都不打开。每题两位评审，字母顺序错开一位。
4. `summary <run> --detail new` 看新版被挑出的问题，改标准、`answer_standard.py --apply`，挑一两道题重跑确认。

成本参考：一份带 skill 的回答约 25–50 万子 agent token、20–45 分钟（圆桌、Lead 更多），一位评审约 17 万 token。

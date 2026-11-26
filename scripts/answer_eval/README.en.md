# answer_eval · Blind evaluation of answer quality

English | [中文](README.md)

After changing `references/answer-standard.md`, or the way a kind of skill answers, test the change with the nine
questions here: the old skill, the new skill and no skill each answer the same question, and a reviewer agent that sees
only the three answers judges them blind. Whether the writing is good is something the gate scripts cannot check; only
reading the answers shows it.

| File | Purpose |
|------|------|
| `questions.json` | Nine questions: five for researcher skills (Curtis, Powell, Grossmann; Achterberg of the MILP Team, Forrest of the LP Team), one for a corpus team (NLP Team), one for a roundtable, two for the Lead (warehouse location; a daily transport LP with a 5-minute limit and no commercial license) |
| `judge_prompt.md` | Instructions for the reviewer agent: six dimensions scored 1–5, a ranking, whether an answer could be forwarded as is, what is unprofessional, technical errors |
| `answer_eval.py` | `prep` builds the blind folders and key.json; `swaps` checks whether a reviewer filed comments under the wrong letter; `summary` unblinds and summarizes; `form` counts process jargon, labels and where disclaimers sit |

Procedure (lessons from the first run on 2026-11-14; see that day's "answer standard" entry in
`teams/DISTILLATION_LOG.md`):

1. For each question and each version, start a zero-context agent: it reads the whole SKILL.md, follows it, and writes
   the reply the user would see, verbatim, to `<run>/{old,new,none}/<ID>.md`. For roundtables and the Lead, save only
   the final plan, so that all three answers are single documents.
2. Run the three versions on the same model; if the model changes, rerun the whole question and note it in the LOG.
3. `python3 -X utf8 scripts/answer_eval/answer_eval.py prep <run>`, then start one agent per reviewer folder and tell it
   only to read the `instructions.md` there and to open no other file. Two reviewers per question, with the letter order
   shifted by one.
4. Before unblinding, run `swaps <run>`: reviewers occasionally file comments under the wrong letter (on 2026-11-15, one
   of sixteen reviews swapped B and C). The script checks where the text quoted in each comment appears among A/B/C;
   when a whole set is swapped it writes `verdict_corrected.json`, which `summary` reads first. Reviews with nothing
   quoted to check must be read by hand.
5. `summary <run> --detail new` shows the problems found in the new version; fix the standard, run
   `answer_standard.py --apply`, and rerun one or two questions to confirm.

Cost reference: one answer with a skill takes about 250,000–500,000 subagent tokens and 20–45 minutes; one Lead answer
about 300,000–360,000 tokens (not counting its internal team and lead agents) and 65–110 minutes (including measurements
on synthetic instances and follow-up questions, with four running in parallel); one reviewer about 150,000–210,000
tokens.

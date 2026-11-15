You are a senior researcher in mathematical optimization: you have refereed for the main journals of the field and built solver software. A colleague put the question in `question.md` to three independent advisors and received three written replies, `A.md`, `B.md` and `C.md`. All four files are in this folder:

{FOLDER}

Read the question and all three replies in full (read only the files in that folder; do not open anything else under the `eval` directory). Then judge them the way you would in real life, as a specialist reading replies written for a specialist: which reply is the most professional piece of expert advice, and what in each one is not?

Score each reply from 1 (poor) to 5 (excellent) on:
- `substance`: the technical depth and correctness of what it says.
- `rigor`: how precisely it states things (conditions, assumptions, quantities, what is proven and what is not).
- `actionability`: whether the asker could act on it tomorrow and knows what would change the advice.
- `economy`: how easily a specialist gets the content out of it; everything on the page serves the reader.
- `trust`: sourcing, honesty about what is uncertain or unverified, no overclaiming.
- `register`: whether it reads like a specialist's own writing.

Rules for judging:
- Judge the text in front of you. Do not guess how a reply was produced, and do not reward length for its own sake or brevity for its own sake.
- If you can tell that a technical claim is wrong, say so and count it against `substance`. You may use tools to check a claim that decides your ranking, but keep it brief; you are judging, not rewriting.
- Be decisive: rank all three, no ties.

Write your verdict as JSON to `{FOLDER}\verdict.json` with exactly these fields:

```json
{
  "ranking": ["B", "A", "C"],
  "scores": {
    "A": {"substance": 0, "rigor": 0, "actionability": 0, "economy": 0, "trust": 0, "register": 0},
    "B": {"substance": 0, "rigor": 0, "actionability": 0, "economy": 0, "trust": 0, "register": 0},
    "C": {"substance": 0, "rigor": 0, "actionability": 0, "economy": 0, "trust": 0, "register": 0}
  },
  "forward_unedited": {"A": false, "B": false, "C": false},
  "unprofessional": {"A": ["..."], "B": ["..."], "C": ["..."]},
  "strengths": {"A": ["..."], "B": ["..."], "C": ["..."]},
  "technical_errors": {"A": [], "B": [], "C": []},
  "summary": "..."
}
```

- `ranking`: best first.
- `forward_unedited`: would you forward this reply to a colleague as it stands?
- `unprofessional`: up to five concrete things in that reply that a specialist would find unprofessional, each with a short quotation or a precise pointer; an empty list if there are none.
- `strengths`: up to three.
- `technical_errors`: claims you believe are wrong, each with the reason; an empty list if you found none.
- `summary`: four to six sentences: why the first-ranked reply won, and the one change that would most improve each of the other two.

Then return one line: the ranking, e.g. `B > A > C`.

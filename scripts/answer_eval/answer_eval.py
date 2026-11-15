#!/usr/bin/env python3
"""Blind comparison of reply quality: old skill vs revised skill vs no skill.

Layout of a run directory <run>:
    <run>/old/<ID>.md     reply with the skill as it was
    <run>/new/<ID>.md     reply with the revised skill
    <run>/none/<ID>.md    reply with no skill (the same model answering on its own)
IDs and prompts are in questions.json next to this script.

Commands (from the repository root; Windows: python3 -X utf8):
    python3 scripts/answer_eval/answer_eval.py prep <run> [ID ...]
        For each ID with all three replies: two judge folders <run>/judge/<ID>_j1 and _j2 holding the
        replies as A/B/C (judge 2 sees the letters rotated by one), question.md and instructions.md
        (judge_prompt.md with the folder filled in). Which letter is which arm goes to <run>/key.json,
        outside the judge folders. For roundtable and lead replies, pass the final deliverable only
        (cut the checkpoint transcript before saving the reply), so that all three are single documents.
    python3 scripts/answer_eval/answer_eval.py summary <run> [--detail old|new|none] [--only ID_j1 ...]
        Unblinds every verdict.json, prints rankings and scores per arm and the means, and writes
        <run>/verdicts.json.
    python3 scripts/answer_eval/answer_eval.py form <run>
        Counts what a reader sees that is process rather than content: inline method tags, workflow
        handles, provenance labels, a disclaimer in the first lines, a footer, mathematical symbols,
        code blocks and references.

Judges: one zero-context agent per judge folder, told only to read instructions.md there and to open
nothing else. Compare replies produced by the same model; record the model in the log.
"""
from __future__ import annotations

import json
import random
import re
import shutil
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
ARMS = ["old", "new", "none"]
DIMS = ["substance", "rigor", "actionability", "economy", "trust", "register"]


def questions() -> dict[str, dict]:
    return {q["id"]: q for q in json.loads((HERE / "questions.json").read_text(encoding="utf-8"))}


def prep(run: Path, only: list[str]) -> None:
    qs = questions()
    key_path = run / "key.json"
    key = json.loads(key_path.read_text(encoding="utf-8")) if key_path.exists() else {}
    template = (HERE / "judge_prompt.md").read_text(encoding="utf-8")
    for qid, q in qs.items():
        if only and qid not in only:
            continue
        paths = {arm: run / arm / f"{qid}.md" for arm in ARMS}
        missing = [arm for arm, p in paths.items() if not p.exists()]
        if missing:
            print(f"{qid}: waiting for {', '.join(missing)}")
            continue
        first = list(ARMS)
        random.Random(f"{qid}-{run.name}").shuffle(first)
        for j in (1, 2):
            order = first if j == 1 else first[1:] + first[:1]
            folder = run / "judge" / f"{qid}_j{j}"
            folder.mkdir(parents=True, exist_ok=True)
            for letter, arm in zip("ABC", order):
                shutil.copyfile(paths[arm], folder / f"{letter}.md")
            (folder / "question.md").write_text(q["prompt"] + "\n", encoding="utf-8")
            (folder / "instructions.md").write_text(template.replace("{FOLDER}", str(folder)), encoding="utf-8")
            key[f"{qid}_j{j}"] = dict(zip("ABC", order))
        print(f"{qid}: judge folders j1, j2 ready")
    key_path.write_text(json.dumps(key, ensure_ascii=False, indent=1), encoding="utf-8")


def summary(run: Path, detail: str | None, only: list[str]) -> None:
    key = json.loads((run / "key.json").read_text(encoding="utf-8"))
    rows, agg, firsts, forwards = {}, {}, {}, {}
    for name in sorted(key):
        if only and name not in only:
            continue
        vpath = run / "judge" / name / "verdict.json"
        if not vpath.exists():
            continue
        v = json.loads(vpath.read_text(encoding="utf-8"))
        arm_of = key[name]
        ranking = [arm_of[x] for x in v["ranking"]]
        rows[name] = {"ranking": ranking, "arms": {}, "summary": v.get("summary", "")}
        print(f"\n== {name}: {' > '.join(ranking)}")
        for letter, arm in sorted(arm_of.items(), key=lambda kv: ARMS.index(kv[1])):
            s = v["scores"][letter]
            total = sum(s[d] for d in DIMS)
            fwd = bool(v["forward_unedited"][letter])
            rows[name]["arms"][arm] = {"scores": s, "total": total, "forward": fwd,
                                       "unprofessional": v["unprofessional"][letter],
                                       "technical_errors": v["technical_errors"][letter],
                                       "strengths": v["strengths"][letter]}
            agg.setdefault(arm, []).append(s)
            forwards.setdefault(arm, []).append(fwd)
            print(f"   {arm:<5} {total:>2}/30  " + " ".join(f"{d[:4]}={s[d]}" for d in DIMS)
                  + f"  forward={'yes' if fwd else 'no'}")
            if detail == arm:
                for item in v["unprofessional"][letter]:
                    print(f"     - unprofessional: {item}")
                for item in v["technical_errors"][letter]:
                    print(f"     - error: {item}")
        firsts[ranking[0]] = firsts.get(ranking[0], 0) + 1
    if agg:
        n = len(rows)
        print(f"\n== means over {n} verdict(s)")
        for arm in ARMS:
            if arm not in agg:
                continue
            means = {d: sum(s[d] for s in agg[arm]) / len(agg[arm]) for d in DIMS}
            print(f"   {arm:<5} {sum(means.values()):4.1f}/30  " + " ".join(f"{d[:4]}={means[d]:.1f}" for d in DIMS)
                  + f"  ranked first {firsts.get(arm, 0)}/{n}  forwardable {sum(forwards[arm])}/{len(forwards[arm])}")
    (run / "verdicts.json").write_text(json.dumps(rows, ensure_ascii=False, indent=1), encoding="utf-8")


EMOJI = re.compile("[\U0001F300-\U0001FAFF☀-➿⭐⭕✅⚠]")
TAG = re.compile(r"→\s*(?:[A-Z][\w.-]*\s*·\s*)?(?:Method|Heuristic|方法|启发式|M\d|H\d|Workflow|工作流)", re.I)
HANDLE = re.compile(r"\bWorkflow\s+[A-Z]\d?\b|工作流\s*[A-Z]\d?\b|routing row|路由", re.I)
LABEL = re.compile(r"generic, not|not [A-Z][\w-]+-style|\(inferred\)|\[inferred\]|extrapolated", re.I)
DISCLAIMER = re.compile(r"distilled from|not .{0,30}own advice|提炼自|蒸馏自|不是.{0,12}本人的(?:建议|指导)|模拟讨论|simulated discussion", re.I)
FOOTER = re.compile(r"^#{1,4}\s*(?:Basis|依据|参考文献|References|Sources|来源)\b", re.I | re.M)
MATH = re.compile(r"[=≤≥∈∑∇‖√λμρκ]|\bmin\b|\bs\.t\.")
CODE = re.compile(r"^```", re.M)
REF = re.compile(r"\b(?:19|20)\d{2}[a-z]?\)|10\.\d{4,9}/|arXiv:\s*\d{4}\.\d{4,5}")


def form(run: Path) -> None:
    cols = ["chars", "emoji", "tags", "handles", "labels", "discl_top", "footer", "math", "code", "refs"]
    print(f"{'reply':<14}" + "".join(f"{c:>10}" for c in cols))
    for qid in questions():
        for arm in ARMS:
            p = run / arm / f"{qid}.md"
            if not p.exists():
                continue
            text = p.read_text(encoding="utf-8").replace("\r\n", "\n")
            head = "\n".join([l for l in text.split("\n") if l.strip()][:6])
            row = [len(text), len(EMOJI.findall(text)), len(TAG.findall(text)), len(HANDLE.findall(text)),
                   len(LABEL.findall(text)), int(bool(DISCLAIMER.search(head))), int(bool(FOOTER.search(text))),
                   len(MATH.findall(text)), len(CODE.findall(text)) // 2, len(REF.findall(text))]
            print(f"{qid + '/' + arm:<14}" + "".join(f"{v:>10}" for v in row))


def main(argv: list[str]) -> int:
    for stream in (sys.stdout, sys.stderr):
        try:
            stream.reconfigure(encoding="utf-8")
        except (AttributeError, ValueError):
            pass
    if argv[:1] in (["-h"], ["--help"]):
        print(__doc__)
        return 0
    if len(argv) < 2 or argv[0] not in ("prep", "summary", "form"):
        print(__doc__)
        return 2
    cmd, run, rest = argv[0], Path(argv[1]), argv[2:]
    if cmd == "prep":
        prep(run, rest)
    elif cmd == "summary":
        detail = None
        if "--detail" in rest:
            i = rest.index("--detail")
            detail = rest[i + 1]
            del rest[i:i + 2]
        only = rest[rest.index("--only") + 1:] if "--only" in rest else []
        summary(run, detail, only)
    else:
        form(run)
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))

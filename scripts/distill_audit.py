#!/usr/bin/env python3
"""
团队级 skill 的「声明 → 语料」抽样审计（G7：DISTILL.md Phase 4 的内容级闸门；语料侧对应 team-kit 的 audit_claims.py）。

distill_check.py 只能证明 SKILL.md 里的每个 ID 真的存在、05 的禁区逐条搬过去了、（作者, 年份）都在 canon 里；
它证明不了带着 [DFO-S12] 的那句话是语料**真的这么说**的——「真 ID + 编造内容」正是此前团队 skill 胡说的机制
（standards/grounding.md 第 5 节）。本脚本把声明和它所引 ID 的语料证据配成对，交给一个零上下文的审计 agent
判定蕴含关系，再把判定写成报告。两步：

  --sample   从 SKILL.md 承重部分（框架概览 / 流派对比 / 决策启发式 / 关键结果速查 / 绝不做）抽 N 条带 ID 的声明。
             声明 = 同一条目里上一组方括号之后、这组方括号之前的分句（太短时补上条目开头）；结果表每行一条
             （结论 + 假设；状态列里的 ID 是引用）。证据 = 所引每个 ID 在语料里的定义（01 的文献行 / 04 的整节 /
             03、05 的整节）加上 00–05 与 researchers/ 里提到该 ID 的每个条目（跨队 ID 到对方语料里取）。
             写成审计包 JSON + 同名 .md（给审计 agent 读的排版版本）。
             审计 agent 只读这个包：不读 SKILL.md、不读语料全文、不上网、不用自己的领域知识补证据
             （SkillLens，arXiv 2605.23899：LLM 自评 skill 质量准确率 46.4%，答题者与评分者必须是两个 agent）。
  --report   把审计 agent 返回的判定（verdicts JSON）追加到 teams/<team>/CLAIM-AUDIT.md，并按判定给退出码。

判定（每条声明一个）:
  supported     语料在所引 ID 处写了这件事，声明没有超出语料（措辞可以不同；中英混写不算差异）
  partial       语料有关联内容，但声明更强、更具体、更一般，或加了语料没写的假设 / 常数 / 归属，或把分歧写成了共识
  unsupported   语料没有这个内容，或内容相反
  uncheckable   所引 ID 的证据只有一行文献表（题目 + 角色），声明讲的是题目推不出来的内容，无法判断

verdicts JSON（审计 agent 写）:
  {"auditor": "<模型 / agent 名>", "date": "YYYY-MM-DD",
   "verdicts": [{"k": 1, "verdict": "supported", "reason": "一句话：语料哪里写了 / 哪里不一致"}, …]}

退出码（--report）：unsupported > 0 → 1；否则 0（partial 要人看一眼，报告里单列）。
样本量：默认 20 条（两份 skill 各约 100–150 条带 ID 的声明，20 条是抽查不是普查；想严就 --n 40 或换 --seed 再抽）。
抽样可复现：同一 --seed 抽到同一批；每个首引 ID 最多 --per-id 条（默认 2），让样本覆盖更多 ID。

用法:
    python3 scripts/distill_audit.py teams/<team> --sample --out <包.json> [--n 20] [--seed 1] [--per-id 2] [--list]
    python3 scripts/distill_audit.py teams/<team> --report <verdicts.json> [--packet <包.json>] [--date YYYY-MM-DD]
示例:
    S=${TMPDIR:-/tmp}/distill-scratch
    python3 scripts/distill_audit.py teams/dfo-team --sample --n 20 --seed 1 --out $S/audit-dfo-team.json --list
    # → 把 $S/audit-dfo-team.md 交给一个新 agent（只给它这个路径），让它写 $S/verdicts-dfo-team.json
    python3 scripts/distill_audit.py teams/dfo-team --report $S/verdicts-dfo-team.json --packet $S/audit-dfo-team.json
"""

from __future__ import annotations

import argparse
import datetime
import json
import random
import re
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import distill_check as dc  # noqa: E402

VERDICTS = ("supported", "partial", "unsupported", "uncheckable")
REPORT_NAME = "CLAIM-AUDIT.md"
SAMPLE_SECTIONS = dc.LOAD_BEARING + ["results"]
BLOCK_CAP = 7000      # 每个 ID 的证据上限（字符）
ITEM_CAP = 18000      # 每条声明全部证据上限
MIN_CLAUSE = 40

BRIEF = """You are the AUDITOR in a two-agent check of a team-level skill distilled from a closed corpus
(Optimization-Researchers, DISTILL.md protocol). Another agent wrote the skill; you did not. You see only this packet.
Rules:
- Do not open the skill, the corpus files or the web, and do not use your own knowledge of the field to supply
  evidence. The question is only: does the CORPUS EVIDENCE cited by the claim support the CLAIM?
- For each item, read `claim` (one clause from the skill; `context` is the whole bullet or table row it sits in,
  for reference only), `cites` (the corpus IDs / labels attached to that clause) and `evidence`: for each cited ID,
  its definition in the corpus (a canon row for S/L sources; the full result section for R; the full section for
  H heuristics and F failure modes) followed by every corpus passage that mentions that ID (file:line given).
- Verdicts: supported = the evidence says this (paraphrase, Chinese/English mixing and reordering are fine) and the
  claim does not go beyond it; partial = related content is there but the claim is stronger, more specific or more
  general, adds an assumption, constant, attribution or noise model the evidence does not state, or presents a
  disagreement as consensus; unsupported = the evidence does not contain it or says the opposite; uncheckable =
  the only evidence is a canon row (title + role) and the claim is about content that the title does not imply.
- Be strict about numbers, constants, rates, assumptions, proved-vs-cited status, who-said-what, noise models and
  dimension factors; be tolerant of wording.
- Write one JSON file: {"auditor": "<your model or agent name>", "date": "<today>",
  "verdicts": [{"k": <item k>, "verdict": "<one of the four>", "reason": "<one sentence, naming the file:line in the
  evidence that supports or contradicts>"}]} with exactly one entry per item, in order. Nothing else."""


def _clean(s: str) -> str:
    return re.sub(r"\s+", " ", s).strip(" ;,、；，:：[(（）)]")


def claims_in_skill(c: dc.Corpus) -> list[dict]:
    pl = c.prose["SKILL.md"]
    secs = dc.sections(pl)
    out: list[dict] = []
    for key in SAMPLE_SECTIONS:
        s = dc.find_section(secs, key)
        if not s:
            continue
        title = dc.SECTION_KEYS[key]
        if key == "results":
            header, rows = dc.table_rows(pl, s.start + 1, s.end)
            ai = next((k for k, h in enumerate(header) if "假设" in h), None)
            for line, cells in rows:
                refs, labels = dc.refs_in_text("|".join(cells), c.prefix, line)
                cites = _uniq([r.id for r in refs] + [l.id for l in labels])
                if not cites:
                    continue
                claim = _clean(cells[1]) if len(cells) > 1 else ""
                if ai is not None and ai < len(cells) and cells[ai].strip() not in ("", "—", "-"):
                    claim += f"；假设：{_clean(cells[ai])}"
                out.append({"line": line, "section": title, "claim": claim, "context": _clean(" | ".join(cells))[:500],
                            "cites": cites})
            continue
        for it in dc.items_in(pl, s.start + 1, s.end):
            text = re.sub(r"\s+", " ", it.text)
            prev = 0
            for g in dc.BRACKET_RE.finditer(text):
                refs, labels = dc.refs_in_text(g.group(0), c.prefix, it.line)
                cites = _uniq([r.id for r in refs] + [l.id for l in labels])
                if not cites:
                    continue
                clause = _clean(text[prev:g.start()])
                if len(clause) < MIN_CLAUSE:
                    lead = _clean(text[:g.start()])
                    clause = lead[-320:] if len(lead) > 320 else lead
                prev = g.end()
                if not clause:
                    continue
                out.append({"line": it.line, "section": title, "claim": clause, "context": text[:500], "cites": cites})
    return out


def _uniq(xs: list[str]) -> list[str]:
    seen: set[str] = set()
    return [x for x in xs if not (x in seen or seen.add(x))]


def _mentions(corpus: dc.Corpus, cid: str, is_label: bool) -> list[tuple[str, int, str]]:
    """语料里提到 cid 的条目：(文件, 行, 文本)。04/03/05 给整节，其余给条目或表格行。"""
    found: list[tuple[str, int, str]] = []
    label_re = re.compile(dc.LABEL_WORD_RE.format(kind=cid[0], num=cid[1:])) if is_label else None

    def hit(lines: list[str], first_line: int) -> bool:
        for k, line in enumerate(lines):
            if label_re:
                if label_re.search(line):
                    return True
                continue
            refs, _ = dc.refs_in_line(line, first_line + k, corpus.prefix)
            if any(r.id == cid for r in refs):
                return True
        return False

    for f, pl in corpus.prose.items():
        if f in dc.PRODUCT_FILES:
            continue
        if f in ("04-results.md", "03-heuristics.md", "05-failure-modes.md"):
            for s in dc.sections(pl):
                if s.level != 2:
                    continue
                body = pl[s.start:s.end]
                if hit(body, s.start + 1):
                    found.append((f, s.start + 1, "\n".join(body).strip()))
        else:
            secs = dc.sections(pl)
            for it in dc.items_in(pl, 0, len(pl)):
                if hit(it.text.splitlines() or [it.text], it.line):
                    head = next((s.title for s in reversed(secs) if s.start < it.line), "")
                    found.append((f, it.line, (f"[{head}] " if head else "") + it.text))
    return found


def evidence_for(cid: str, own: dc.Corpus, reg: dc.Registry) -> dict:
    is_label = bool(re.fullmatch(r"[HF]\d{1,2}", cid))
    if is_label:
        corpus, d = own, own.lookup(cid[0], int(cid[1:]))
    else:
        m = dc.FULL_ID_RE.fullmatch(cid)
        corpus = reg.by_prefix.get(m.group("prefix")) if m else None
        d = corpus.lookup(m.group("kind"), int(m.group("num"))) if (corpus and m) else None
    if corpus is None:
        return {"id": cid, "found": False, "blocks": []}
    blocks: list[dict] = []
    if d:
        blocks.append({"file": f"teams/{corpus.slug}/{d.file}", "line": d.line, "role": "definition" + (f" ({d.tier})" if d.tier else ""),
                       "text": d.text})
    for f, line, text in _mentions(corpus, cid, is_label):
        if d and f == d.file and line == d.line:
            continue
        blocks.append({"file": f"teams/{corpus.slug}/{f}", "line": line, "role": "mention", "text": text})
    total = 0
    for b in blocks:
        if len(b["text"]) > BLOCK_CAP:
            b["text"] = b["text"][:BLOCK_CAP] + " …[truncated]"
            b["truncated"] = True
        total += len(b["text"])
    return {"id": cid, "found": d is not None, "team": corpus.slug, "blocks": blocks, "chars": total}


def sample(c: dc.Corpus, reg: dc.Registry, n: int, seed: int, per_id: int) -> tuple[list[dict], int]:
    pool = claims_in_skill(c)
    rng = random.Random(seed)
    order = list(pool)
    rng.shuffle(order)
    picked: list[dict] = []
    used: dict[str, int] = {}
    for cl in order:
        key = cl["cites"][0]
        if used.get(key, 0) >= per_id:
            continue
        used[key] = used.get(key, 0) + 1
        picked.append(cl)
        if len(picked) >= n:
            break
    picked.sort(key=lambda x: x["line"])
    for k, cl in enumerate(picked, 1):
        cl["k"] = k
        cl["evidence"] = [evidence_for(cid, c, reg) for cid in cl["cites"]]
        budget = ITEM_CAP
        for ev in cl["evidence"]:
            for b in ev["blocks"]:
                if budget <= 0:
                    b["text"] = "…[omitted: item evidence cap]"
                    b["truncated"] = True
                else:
                    budget -= len(b["text"])
    return picked, len(pool)


def render_md(packet: dict) -> str:
    out = [f"# Claim-audit packet · {packet['team']} · {packet['date']}",
           f"\n{packet['n']} claims sampled from teams/{packet['team']}/SKILL.md (seed {packet['seed']}, pool {packet['pool']}).",
           "\n## Brief\n", packet["brief"]]
    for it in packet["items"]:
        out.append(f"\n---\n\n## Item {it['k']} · SKILL.md:{it['line']} · {it['section']}\n")
        out.append(f"**Claim**: {it['claim']}\n")
        out.append(f"**Context** (the whole bullet / row): {it['context']}\n")
        out.append(f"**Cites**: {', '.join(it['cites'])}\n")
        for ev in it["evidence"]:
            out.append(f"\n### Evidence for {ev['id']}" + ("" if ev.get("found") else " — NOT FOUND in the corpus"))
            for b in ev["blocks"]:
                out.append(f"\n- `{b['file']}:{b['line']}` ({b['role']}):\n")
                out.append("\n".join("    " + l for l in b["text"].splitlines()))
    out.append("\n\n---\n\nWrite the verdicts JSON exactly as the brief says: one entry per item, k = 1 … "
               f"{packet['n']}, in order.\n")
    return "\n".join(out)


def write_report(team_dir: Path, packet: dict, verdicts: dict, date: str) -> tuple[Path, dict]:
    items = {i["k"]: i for i in packet["items"]}
    vs = {int(v["k"]): v for v in verdicts.get("verdicts", []) if "k" in v}
    counts = {v: 0 for v in VERDICTS}
    rows, missing = [], []
    for k in sorted(items):
        it = items[k]
        v = vs.get(k)
        if not v or v.get("verdict") not in VERDICTS:
            missing.append(k)
            verdict, reason = "—", "(no verdict returned)"
        else:
            verdict = v["verdict"]
            reason = str(v.get("reason") or "").replace("|", "\\|").replace("\n", " ")
            counts[verdict] += 1
        claim = it["claim"].replace("|", "\\|")
        rows.append(f"| {k} | SKILL.md:{it['line']} · {it['section']} | {claim[:160]}{'…' if len(claim) > 160 else ''} "
                    f"| {', '.join(it['cites'])} | **{verdict}** | {reason[:240]} |")
    judged = sum(counts.values())
    now = re.search(r"语料版本\s*[:：]?\s*([0-9a-f]{7,40})", (team_dir / "SKILL.md").read_text(encoding="utf-8", errors="replace"))
    stamp = packet.get("stamp") or "?"
    if now and now.group(1) != stamp:
        stamp += f" when sampled, {now.group(1)} now"
    head = (f"\n## Audit {date} · {packet['n']} claims from SKILL.md (seed {packet['seed']}, pool {packet['pool']} ID-bearing claims"
            f"; skill stamp {stamp})\n\n"
            f"- Auditor: {verdicts.get('auditor', '(unnamed)')} · zero-context (packet only) · judged {judged}/{packet['n']}"
            + (f" · no verdict for k = {', '.join(map(str, missing))}" if missing else "") + "\n"
            f"- supported {counts['supported']} · partial {counts['partial']} · unsupported {counts['unsupported']} · "
            f"uncheckable {counts['uncheckable']}\n"
            f"- Evidence layer: the corpus files 00–05 and researchers/ (definitions of the cited IDs plus every passage "
            f"that mentions them); the skill itself was not shown to the auditor.\n"
            f"- Gate (G7): unsupported must be 0 before delivery; each partial is listed for a human look.\n\n"
            "| k | where | claim (clause before the citation) | cites | verdict | auditor's reason |\n"
            "|---|---|---|---|---|---|\n" + "\n".join(rows) + "\n")
    acts = [f"- k={k}: SKILL.md:{items[k]['line']} [{', '.join(items[k]['cites'])}] — {vs[k].get('reason', '')}"
            for k in sorted(items) if vs.get(k, {}).get("verdict") in ("unsupported", "partial")]
    if acts:
        head += ("\n**To act on** (unsupported: correct the claim or the citation; partial: narrow the claim or cite the "
                 "corpus entry that supports it; then re-run distill_check.py and sample again with a new seed):\n\n"
                 + "\n".join(acts) + "\n")
    path = team_dir / REPORT_NAME
    if not path.exists():
        path.write_text(f"# {team_dir.name} · Claim-to-corpus audit (G7)\n\n"
                        "> Sampled claims from `SKILL.md`, each checked by a zero-context auditor against the corpus entries it "
                        "cites (`scripts/distill_audit.py`; protocol in `standards/distill-gates.md`). Sections are appended per "
                        "audit; nothing is rewritten. This file is a product of distillation, not corpus.\n", encoding="utf-8")
    with path.open("a", encoding="utf-8") as fh:
        fh.write(head)
    return path, counts


def main():
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    ap = argparse.ArgumentParser(description="团队级 skill「声明→语料」抽样审计（G7）：抽声明配语料证据成审计包；把零上下文审计的判定写成报告",
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("team_dir", help="teams/<team>（含 01-canon.md 与 SKILL.md）")
    g = ap.add_mutually_exclusive_group(required=True)
    g.add_argument("--sample", action="store_true", help="抽样并写审计包（JSON + 同名 .md）")
    g.add_argument("--report", metavar="VERDICTS_JSON", help="由审计 agent 的判定写报告")
    ap.add_argument("--out", help="--sample：审计包的输出路径（.json）")
    ap.add_argument("--packet", help="--report：对应的审计包（默认用 verdicts 同目录里同名的 audit-*.json）")
    ap.add_argument("--n", type=int, default=20)
    ap.add_argument("--seed", type=int, default=1)
    ap.add_argument("--per-id", type=int, default=2, help="每个首引 ID 最多抽几条（默认 2）")
    ap.add_argument("--date", default=datetime.date.today().isoformat())
    ap.add_argument("--list", action="store_true", help="--sample：打印抽到的声明")
    a = ap.parse_args()

    team_dir = Path(a.team_dir)
    if not (team_dir / "01-canon.md").exists():
        print(f"❌ {team_dir}: 没有 01-canon.md，不是语料团队目录", file=sys.stderr)
        sys.exit(2)
    if not (team_dir / "SKILL.md").exists():
        print(f"❌ {team_dir}: 没有 SKILL.md（还没蒸馏）", file=sys.stderr)
        sys.exit(2)
    reg = dc.Registry(team_dir.parent)
    c = reg.by_slug[team_dir.name]
    stamp = re.search(r"语料版本\s*[:：]?\s*([0-9a-f]{7,40})", c.skill or "")

    if a.sample:
        if not a.out:
            ap.error("--sample needs --out <packet.json>")
        items, pool = sample(c, reg, a.n, a.seed, a.per_id)
        packet = {"team": c.slug, "prefix": c.prefix, "date": a.date, "stamp": stamp.group(1) if stamp else "",
                  "n": len(items), "seed": a.seed, "per_id": a.per_id, "pool": pool, "brief": BRIEF, "items": items}
        out = Path(a.out)
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text(json.dumps(packet, ensure_ascii=False, indent=1), encoding="utf-8")
        md = out.with_suffix(".md")
        md.write_text(render_md(packet), encoding="utf-8")
        if a.list:
            for i in items:
                print(f"{i['k']:>3}. SKILL.md:{i['line']} [{', '.join(i['cites'])}] {i['claim'][:120]}")
        nf = [i["k"] for i in items if any(not e.get("found") for e in i["evidence"])]
        print(f"✅ packet: {out} (+ {md.name}) · {len(items)} claims (pool {pool}) · seed {a.seed}"
              + (f" · ⚠ {len(nf)} item(s) cite an ID with no corpus entry: k = {nf}" if nf else ""))
        print("Next: give ONE fresh agent only the .md packet path (it reads the brief and the items) and have it write the"
              f" verdicts JSON; then: python3 scripts/distill_audit.py {team_dir} --report <verdicts.json> --packet {out}")
        sys.exit(0)

    vpath = Path(a.report)
    if not vpath.exists():
        print(f"❌ no such file: {vpath}", file=sys.stderr)
        sys.exit(2)
    ppath = Path(a.packet) if a.packet else vpath.with_name(vpath.name.replace("verdicts", "audit"))
    if not ppath.exists():
        print(f"❌ packet not found: {ppath} (give --packet)", file=sys.stderr)
        sys.exit(2)
    packet = json.loads(ppath.read_text(encoding="utf-8"))
    verdicts = json.loads(vpath.read_text(encoding="utf-8"))
    if packet.get("team") != c.slug:
        print(f"❌ packet is for {packet.get('team')}, not {c.slug}", file=sys.stderr)
        sys.exit(2)
    path, counts = write_report(team_dir, packet, verdicts, a.date)
    bad = counts["unsupported"]
    print(f"{'❌' if bad else '✅'} {path}: supported {counts['supported']} · partial {counts['partial']} · "
          f"unsupported {counts['unsupported']} · uncheckable {counts['uncheckable']} (of {packet['n']})")
    sys.exit(1 if bad else 0)


if __name__ == "__main__":
    main()

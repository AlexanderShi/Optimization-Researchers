#!/usr/bin/env python3
"""
研究Skill的「声明 → 证据」抽样审计（claim audit；研究Skill · 深读档的内容级闸门，补 check_citations.py 查不到的那一层）。

check_citations.py 只能证明一条引用指向真实存在、确实读过、页码在范围内的卡片；它证明不了 SKILL.md 那句话是卡片
真正支持的（「真论文 + 编造内容」正是此前团队 skill 胡说的机制）。本脚本把声明和它所引的卡片配成对，交给一个
零上下文的审计 agent 判定蕴含关系，再把判定写成报告。两步：

  --sample   从 SKILL.md（或 --files 指定的文件）里抽 N 条带「卡片 ID + 页码」的声明。每条声明 = 该引用之前的那个
             分句（同一行里上一条引用之后的文字；太短时补上整行开头的上下文）。连同所引卡片的全文
             （cards/<批次>.md 里该作品的那张卡片、批次文件开头的意图与页码对应说明、digest 的 read_level 和 quotes、
             INDEX.md 的页数）写成一个审计包（JSON）+ 审计简报（包里的 "brief"）。
             审计 agent 只读这个包：不读 SKILL.md、不读调研笔记、不上网、不用自己的领域知识补证据
             （SkillLens，arXiv 2605.23899：LLM 自评 skill 质量准确率 46.4%，答题者与评分者必须是两个 agent）。
  --report   把审计 agent 返回的判定（verdicts JSON）写进 <成员>/references/research/10-claim-audit.md（追加一节，
             不覆盖历史），并按判定给退出码。

判定（每条声明一个）:
  supported     卡片在所引页码 / 维度上写了这件事，声明没有超出卡片
  partial       卡片有关联内容，但声明比卡片更强、更具体、更一般，或把卡片标为 variant / contradiction 的内容当成了 evidence
  unsupported   卡片没有这个内容，或内容相反
  uncheckable   卡片没覆盖所引页码或主题（例如摘要级卡片、页码对应不上），无法判断

verdicts JSON 的格式（审计 agent 写）:
  {"auditor": "<模型 / agent 名>", "date": "YYYY-MM-DD",
   "verdicts": [{"k": 1, "verdict": "supported", "reason": "一句话：卡片哪里写了 / 哪里不一致"}, …]}

退出码（--report）：unsupported > 0 → 1；否则 0（partial 要人看一眼，报告里单列）。
样本量：默认 20 条（每位成员 SKILL.md 约 300–500 条带页码引用，20 条是抽查不是普查；想严就 --n 40）。
抽样可复现：同一 --seed 同一文件抽到同一批；每个作品最多 --per-id 条（默认 2），让样本覆盖更多卡片。

用法:
    python3 audit_claims.py <成员目录> --sample --out <包.json> [--n 20] [--seed 1] [--per-id 2] [--files SKILL.md,…]
    python3 audit_claims.py <成员目录> --report <verdicts.json> --packet <包.json> [--date YYYY-MM-DD]
    python3 audit_claims.py <成员目录> --sample --out <包.json> --list        # 只看抽到了哪些声明
示例:
    S=${TMPDIR:-/tmp}/dfo-team-scratch
    python3 scripts/audit_claims.py product/dfo-team/katya-scheinberg --sample --n 20 --seed 1 --out $S/audit-katya-scheinberg.json
    # → 把 $S/audit-katya-scheinberg.json 交给一个新 agent（只给它这个路径和包里的 brief），让它写 $S/verdicts-katya-scheinberg.json
    python3 scripts/audit_claims.py product/dfo-team/katya-scheinberg --report $S/verdicts-katya-scheinberg.json --packet $S/audit-katya-scheinberg.json
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
from check_citations import CITE_RE, DOI_PREFIX_RE, Member, heading_at, page_numbers  # noqa: E402
from check_links import prose_lines  # noqa: E402

VERDICTS = ("supported", "partial", "unsupported", "uncheckable")
REPORT_REL = Path("references/research/10-claim-audit.md")
CARD_CAP = 60000  # 卡片全文上限（字符）；超过才截，并在 item["card"]["truncated"] 标出
CARD_HEAD_RE = re.compile(r"^###\s+(?P<id>[A-Z]\d{3,4})\b", re.M)

BRIEF = """You are the AUDITOR in a two-agent check of a research-craft skill (nuwa research-team kit).
Another agent wrote the skill; you did not. You see only this packet. Rules:
- Do not open the skill, its research notes, the paper texts or the web, and do not use your own knowledge of the
  researcher or the field to supply evidence. The question is only: does the CITED CARD support the CLAIM?
- For each item, read `claim` (one sentence or clause from the skill), the citation (`cite.id`, `cite.pages`) and the
  evidence: `card.text` (the paper card an earlier reader wrote from the full text, with page numbers in its own
  parentheses), `card.batch_header` (how the card's page numbers map to the file), `card.read_level`,
  `card.pages_in_index` (length of the file that was read) and `card.quotes` (verbatim quotes, verified).
- Verdicts: supported = the card says this, at or near the cited pages, and the claim does not go beyond the card;
  partial = related content is there but the claim is stronger, more specific or more general than the card, or the
  card marks it as a variant/contradiction while the claim presents it as evidence; unsupported = the card does not
  contain it or says the opposite; uncheckable = the card does not cover the cited pages or topic (e.g. an
  abstract-level card), so you cannot tell.
- Be strict about numbers, constants, attributions (who said it) and page positions; be tolerant of paraphrase.
- Write one JSON file: {"auditor": "<your model or agent name>", "date": "<today>",
  "verdicts": [{"k": <item k>, "verdict": "<one of the four>", "reason": "<one sentence: where the card says it, or what differs>"}]}
  with exactly one entry per item, in order. Nothing else."""


def claims_in(text: str, mem: Member, rel: str) -> list[dict]:
    prose = prose_lines(text)
    heads = heading_at(prose)
    out = []
    for no, line in enumerate(prose, 1):
        prev = 0
        for m in CITE_RE.finditer(line):
            cid = m.group("id")
            if cid[0] not in mem.letters or DOI_PREFIX_RE.search(line[max(0, m.start() - 24):m.start()]):
                continue
            spec = m.group("pages") or m.group("zh") or ""
            if not spec:
                prev = m.end()
                continue
            clause = line[prev:m.start()].strip(" ;,[(（")
            clause = re.sub(r"\[?cards?\s*$", "", clause).strip(" ;,[(")
            if len(clause) < 40:
                lead = re.sub(r"\s+", " ", line[:m.start()]).strip()
                clause = (lead[-280:] if len(lead) > 280 else lead).strip(" ;,[(")
            out.append({"file": rel, "line": no, "section": heads[no - 1], "claim": clause,
                        "cite": {"id": cid, "pages": spec, "tr": bool(re.search(r"\bTR\b", m.group("gap") or ""))},
                        "line_text": line.strip()})
            prev = m.end()
    return out


def card_text(mem: Member, cid: str) -> dict:
    """这位成员读得最深的那张卡片的全文（cards/<批次>.md 里 ### <ID> 到下一张卡片），加批次文件开头。"""
    rec = mem.cards.get(cid)
    if not rec:
        return {"found": False}
    cards_dir = mem.dir / "references/research/cards"
    best = None
    for b in rec["batches"]:
        md = cards_dir / f"{b}.md"
        if not md.exists():
            continue
        t = md.read_text(encoding="utf-8")
        heads = list(CARD_HEAD_RE.finditer(t))
        for k, h in enumerate(heads):
            if h.group("id") != cid:
                continue
            end = heads[k + 1].start() if k + 1 < len(heads) else len(t)
            body = t[h.start():end].strip()
            header = t[:heads[0].start()].strip() if heads else ""
            lv = ""
            dj = cards_dir / f"{b}.digest.json"
            quotes = []
            try:
                for c in json.loads(dj.read_text(encoding="utf-8")):
                    if str(c.get("id")) == cid:
                        lv = str(c.get("read_level") or "")
                        quotes = c.get("quotes") or []
            except (OSError, json.JSONDecodeError):
                pass
            # 整张卡片都给审计 agent（core 卡片常有 10–15k 字符；截短会把 D8 / 方法关联切掉，判定就不可靠）
            cand = {"found": True, "batch": b, "read_level": lv, "batch_header": header[:1500], "text": body[:CARD_CAP],
                    "truncated": len(body) > CARD_CAP, "quotes": quotes, "pages_in_index": mem.pages_of(cid)}
            if best is None or (lv == rec["best"] and best["read_level"] != rec["best"]):
                best = cand
    return best or {"found": False}


def sample(mem: Member, files: list[str], n: int, seed: int, per_id: int) -> list[dict]:
    pool = []
    for f in files:
        p = mem.dir / f
        if p.exists():
            pool += claims_in(p.read_text(encoding="utf-8"), mem, f)
    rng = random.Random(seed)
    rng.shuffle(pool)
    picked, used = [], {}
    for c in pool:
        cid = c["cite"]["id"]
        if used.get(cid, 0) >= per_id:
            continue
        used[cid] = used.get(cid, 0) + 1
        picked.append(c)
        if len(picked) >= n:
            break
    picked.sort(key=lambda c: (c["file"], c["line"]))
    for k, c in enumerate(picked, 1):
        c["k"] = k
        c["card"] = card_text(mem, c["cite"]["id"])
    return picked, len(pool)


def write_report(mem: Member, packet: dict, verdicts: dict, date: str) -> tuple[Path, dict]:
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
            verdict, reason = v["verdict"], str(v.get("reason") or "").replace("|", "\\|").replace("\n", " ")
            counts[verdict] += 1
        claim = it["claim"].replace("|", "\\|")
        rows.append(f"| {k} | {it['file']}:{it['line']} | {claim[:160]}{'…' if len(claim) > 160 else ''} "
                    f"| {it['cite']['id']} {'TR ' if it['cite'].get('tr') else ''}pp. {it['cite']['pages']} "
                    f"| {it['card'].get('read_level') or '?'} | **{verdict}** | {reason[:220]} |")
    judged = sum(counts.values())
    head = (f"\n## Audit {date} · {packet['n']} claims sampled from {', '.join(packet['files'])} "
            f"(seed {packet['seed']}, pool {packet['pool']} page-cited claims)\n\n"
            f"- Auditor: {verdicts.get('auditor', '(unnamed)')} · zero-context (packet only) · judged {judged}/{packet['n']}"
            + (f" · no verdict for k = {', '.join(map(str, missing))}" if missing else "") + "\n"
            f"- supported {counts['supported']} · partial {counts['partial']} · unsupported {counts['unsupported']} · "
            f"uncheckable {counts['uncheckable']}\n"
            f"- Evidence layer: the paper cards (`references/research/cards/`), whose quotes passed `verify_card_quotes.py`; "
            f"the paper texts themselves were not shown to the auditor.\n"
            f"- Gate: unsupported must be 0 before delivery; each partial is listed for a human look.\n\n"
            "| k | where | claim (clause before the citation) | cited | card level | verdict | auditor's reason |\n"
            "|---|---|---|---|---|---|---|\n" + "\n".join(rows) + "\n")
    acts = [f"- k={k}: {items[k]['file']}:{items[k]['line']} [{items[k]['cite']['id']} pp. {items[k]['cite']['pages']}] — {vs[k].get('reason', '')}"
            for k in sorted(items) if vs.get(k, {}).get("verdict") in ("unsupported", "partial")]
    if acts:
        head += "\n**To act on** (unsupported: correct the claim or the citation; partial: narrow the claim or add the card that supports it):\n\n" + "\n".join(acts) + "\n"
    path = mem.dir / REPORT_REL
    if not path.exists():
        path.write_text(f"# {mem.name} · Claim-to-evidence audit\n\n"
                        "> Sampled claims from the skill, each checked by a zero-context auditor against the paper card it cites "
                        "(`scripts/audit_claims.py`; protocol in `references/claim-audit.md`). Sections are appended per audit; "
                        "nothing is rewritten.\n", encoding="utf-8")
    with path.open("a", encoding="utf-8") as fh:
        fh.write(head)
    return path, counts


def main():
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(errors="replace")
    ap = argparse.ArgumentParser(description="研究Skill「声明→证据」抽样审计：抽声明配卡片成审计包；把零上下文审计的判定写成报告",
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("member_dir", help="成员目录（含 SKILL.md 和 references/research/cards/）")
    g = ap.add_mutually_exclusive_group(required=True)
    g.add_argument("--sample", action="store_true", help="抽样并写审计包")
    g.add_argument("--report", metavar="VERDICTS_JSON", help="由审计 agent 的判定写报告")
    ap.add_argument("--out", help="--sample：审计包的输出路径（JSON）")
    ap.add_argument("--packet", help="--report：对应的审计包（默认用 verdicts 同目录里同名的 audit-*.json）")
    ap.add_argument("--n", type=int, default=20)
    ap.add_argument("--seed", type=int, default=1)
    ap.add_argument("--per-id", type=int, default=2, help="每个作品最多抽几条（默认 2）")
    ap.add_argument("--files", default="SKILL.md", help="抽样的文件，相对成员目录，逗号分隔（默认 SKILL.md）")
    ap.add_argument("--date", default=datetime.date.today().isoformat())
    ap.add_argument("--list", action="store_true", help="--sample：打印抽到的声明")
    a = ap.parse_args()

    sk = Path(a.member_dir)
    if not (sk / "SKILL.md").exists():
        print(f"❌ {sk}: no SKILL.md", file=sys.stderr)
        sys.exit(2)
    team = sk.parent
    cfg = json.loads((team / "team.json").read_text(encoding="utf-8")) if (team / "team.json").exists() else {}
    m = next((x for x in cfg.get("members", []) if x.get("slug") == sk.name), {"slug": sk.name, "name": sk.name})
    mem = Member(team, m)
    if not mem.deep:
        print(f"❌ {sk}: no paper cards (base tier): there is no card layer to audit claims against", file=sys.stderr)
        sys.exit(2)

    if a.sample:
        if not a.out:
            ap.error("--sample needs --out <packet.json>")
        files = [f.strip() for f in a.files.split(",") if f.strip()]
        items, pool = sample(mem, files, a.n, a.seed, a.per_id)
        nocard = [i["k"] for i in items if not i["card"].get("found")]
        packet = {"member": mem.slug, "name": mem.name, "team": cfg.get("team", team.name), "date": a.date,
                  "files": files, "n": len(items), "seed": a.seed, "per_id": a.per_id, "pool": pool,
                  "brief": BRIEF, "items": items}
        out = Path(a.out)
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text(json.dumps(packet, ensure_ascii=False, indent=1), encoding="utf-8")
        if a.list:
            for i in items:
                print(f"{i['k']:>3}. {i['file']}:{i['line']} [{i['cite']['id']} pp. {i['cite']['pages']}] "
                      f"({i['card'].get('read_level') or 'no card'}) {i['claim'][:140]}")
        print(f"✅ packet: {out} · {len(items)} claims (pool {pool}) from {', '.join(files)} · seed {a.seed}"
              + (f" · ⚠ {len(nocard)} item(s) cite a work without a card: k = {nocard}" if nocard else ""))
        print("Next: give ONE fresh agent only this packet path (it reads packet['brief'] and packet['items']) and have it write"
              f" the verdicts JSON; then: python3 scripts/audit_claims.py {sk} --report <verdicts.json> --packet {out}")
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
    if packet.get("member") != mem.slug:
        print(f"❌ packet is for {packet.get('member')}, not {mem.slug}", file=sys.stderr)
        sys.exit(2)
    path, counts = write_report(mem, packet, verdicts, a.date)
    bad = counts["unsupported"]
    print(f"{'❌' if bad else '✅'} {path}: supported {counts['supported']} · partial {counts['partial']} · "
          f"unsupported {counts['unsupported']} · uncheckable {counts['uncheckable']} (of {packet['n']})")
    sys.exit(1 if bad else 0)


if __name__ == "__main__":
    main()

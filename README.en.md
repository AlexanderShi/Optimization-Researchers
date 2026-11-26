# Optimization-Researchers

English | [中文](README.md)

A **self-contained distillation corpus** for two virtual research teams:

- **DFO Team**: derivative-free optimization (zeroth-order, blackbox optimization)
- **NLP Team**: nonlinear programming (first- and second-order methods, convex analysis, stochastic gradients)

Purpose: distill a usable team skill from this repository alone, with no web access, no dependence on the nuwa-skill
repository and no reliance on what a model remembers. This directly fixes an earlier failed distillation: those teams were
generated from web searches and memory and often made things up. This repository writes down everything a team is allowed
to say, each item with an anchor, and during distillation **anything that is not in the corpus may not be said**.

## Relation to nuwa-skill

The repository does not depend on the external nuwa-skill repository; both pipelines ship inside it:

- **Team-level skills**: nuwa's ideas of a purely local corpus mode and a topic-skill variant are folded into
  [DISTILL.md](./DISTILL.md); the distillation protocol, templates and quality gates all live in this repository.
- **Per-researcher skills**: nuwa's research-skill and research-team toolchain (team-kit) is vendored in full
  (`scripts/`, `references/`, `product/`, synced byte for byte from AlexanderShi/nvwa-skill `eb012fa`);
  start at [TEAM-KIT.md](./TEAM-KIT.md).

Deleting nuwa-skill does not affect this repository.

## Layout

```
README.md, README.en.md   this file, in Chinese and in English
DISTILL.md                distillation protocol (self-contained; start here)
RUNBOOK.md                operating rules shared by both pipelines: branches and worktrees, usage windows, Windows, common pitfalls
standards/
  grounding.md            grounding standard: anchor rules, verification tiers, discipline for mathematical claims
  researcher-extraction.md standard for extracting researcher profiles (nuwa's triple verification, adapted)
  skill-template.md       output template for team skills
  distill-gates.md        mechanical part of quality gates G1–G7 (distill_check.py) and the G7 claim-audit protocol (distill_audit.py)
teams/
  dfo-team/               DFO Team corpus (00-charter … 05-failure-modes, researchers/)
    SKILL.md              team skill distilled from this corpus (with corpus IDs; copy to ~/.claude/skills/dfo-team/)
    CLAIM-AUDIT.md        G7 claim-to-corpus audit records (appended by date; a product, not corpus)
  nlp-team/               NLP Team corpus (same structure) + SKILL.md + CLAIM-AUDIT.md
  DISTILLATION_LOG.md     record of every distillation (corpus version, gate results, trial answers)
TEAM-KIT.md               entry point to the per-researcher skill pipeline (team-kit)
references/               team-kit docs and templates: playbook, research extraction framework, research-skill template,
                          team-templates/; nuwa-SKILL.md is a frozen copy of the nuwa root skill
scripts/                  team-kit scripts: publication lists, full texts, paper cards, ledgers, team status; workflows/ holds T1–T4;
                          added in this repository: check_citations.py (citation closure), audit_claims.py (claim audit, protocol references/claim-audit.md);
                          the corpus pipeline's distill_check.py (lint + G1–G6 + version stamp) and distill_audit.py (G7 audit, protocol standards/distill-gates.md)
product/                  team-kit products: per-researcher skills, team roundtables and the council (six teams; see product/README.en.md)
.claude/skills/
  optimization-researchers/ project skill: inside this repository, routes distillation requests to DISTILL.md / TEAM-KIT.md
```

Each team folder has six corpus files, numbered in reading order (`SKILL.md` and `CLAIM-AUDIT.md` are distillation
products, not corpus):

| File | Contents |
|------|------|
| `00-charter.md` | Team scope: which questions it answers and where its boundaries are |
| `01-canon.md` | Canon of literature (with IDs, verification tiers and local cross-check sources) |
| `02-schools.md` | Schools: the shared framework and where the schools disagree |
| `03-heuristics.md` | Decision heuristics (method choice, benchmarking discipline, reporting rules) |
| `04-results.md` | Key theorems and rates (with assumptions, proved vs cited, result IDs) |
| `05-failure-modes.md` | Known traps for making things up (a distilled skill must build these no-go zones in) |
| `researchers/*.md` | Profiles of named researchers (optional, one per person): identity, school, core contributions, methodological stance, all anchored as verified-web or verified-local |

## Quick start

```
Team skill (closed corpus)                      Per-researcher skills / roundtables (team-kit)
1. Read DISTILL.md; distill_check.py --lint     1. Read TEAM-KIT.md → references/research-team-playbook.md
2. Distill by the protocol →                    2. Add a member: team.json + scripts/new_team.py --add-member;
   teams/<team>/SKILL.md                           new team: scripts/new_team.py --init
3. distill_check.py 0 ✗ + distill_audit.py      3. Run scripts/workflows/ through T1–T4; products land in product/<team>/
   audit with 0 unsupported (G1–G7)             4. team_check.py / check_citations.py / audit_claims.py
4. Copy only this SKILL.md to
   ~/.claude/skills/<team>/; check with --installed
```

Before doing either, read [RUNBOOK.md](./RUNBOOK.md) (branches and worktrees, usage windows, Windows encoding, common
pitfalls; in Chinese).

Everything both pipelines need (protocols, templates, scripts, corpus, distilled products) is in this repository. When
Claude Code starts in this repository, the project skill `optimization-researchers` routes distillation and extension
requests to the right entry point.

## Two iron rules

1. **Closed corpus**: no WebSearch or WebFetch during distillation; every factual claim in a skill must trace back to a
   corpus ID (such as `[DFO-S2]`, `[NLP-R4]`). What the corpus lacks goes into the Honest Boundary and must not be
   filled in.
2. **Anchor rule** (from `optimization-paper-collection/_EXTRACT.md`; see
   [standards/grounding.md](./standards/grounding.md)): a claim without a located source does not enter the corpus;
   uncertain metadata is marked `需核对` ("to be checked") rather than invented.

## Maintaining the corpus

- New literature: add a row to `01-canon.md` (assign a new ID and mark its verification tier); related results go into
  `04-results.md`.
- An error in the corpus: correct it directly and add an `勘误:` (erratum) note to that entry; the corpus is alive.
- After editing the corpus, first run `python3 -X utf8 scripts/distill_check.py teams/<team> --lint` (it catches
  duplicate IDs, missing status lines in 04 and references to IDs that do not exist), then rerun DISTILL.md to get an
  updated skill (distillation is a pure function: corpus → skill). When the corpus has changed and the skill has not
  been distilled again, `distill_check.py` reports the skill as stale under `stamp`.

## Local evidence sources (used for cross-checks)

- `C:\Users\sr881\repos\autoresearch-optimization\research_runs\deep-momentum-vs-dfo-v2\sources.json`
  (13 deterministic primary sources with DOIs or URLs)
- `C:\Users\sr881\repos\optimization-paper-collection\` (the anchor rules `_EXTRACT.md` and the complete
  machine-zone entry for Nesterov 1983)
- `C:\Users\sr881\repos\autoresearch-optimization\docs\reviews\2026-07-25-professional-research-audit.md`
  (the authoritative record of the failure lesson: verifying that a paper exists is not verifying what it says)

---
name: {{ROUNDTABLE_SLUG}}
description: |
  Personal research team for {{FIELD}}. Runs the research-craft skills of {{SEATED_LIST}} as separate agents
  that discuss the user's [TODO: the kind of problem the team takes, in one phrase, from the members' "Leads when" fields; team-layer.js (T2)],
  with the user in the loop at every round, and converge on a concrete plan ([TODO: the parts a plan in this field must name, e.g. approach, tool, settings, test protocol, fallback; team-layer.js (T2)]).
  Triggers: "{{TEAM_TITLE}}", "ask the team", "convene the roundtable", "{{ROUNDTABLE_SLUG}}", "what would the team do",
  or a problem in this field brought to "the team".
  [TODO: one "Not for …" sentence naming the requests the team should not take; team-layer.js (T2). Keep the whole description under 1024 characters.]
type: roundtable
---

<!-- Team template (roundtable skill) → product/<team>/<roundtable>/SKILL.md.
     T0: scripts/new_team.py fills the double-brace placeholders; the Team table gets one row per member (slug, name and
         a TODO lens cell).
     T2: scripts/workflows/team-layer.js fills the TODO items marked team-layer.js from the members' Roundtable Cards
         (description, Team table, Problem Card fields, seating table, first fault lines, plan items, Outside the Team,
         Shared References, Honest Boundary with its pre-T3 wording, research date).
     T3.8: scripts/workflows/team-integrate.js rewrites the fault lines, "Papers behind the documented disagreements", the
         Honest Boundary bullets on coverage and on how the fault lines are grounded, and the research date, all from the
         card evidence. No TODO item may remain after T2 (base tier) or after T3.8 (deep tier).
     Open work: grep -n "TODO" SKILL.md. See product/dfo-team for a worked example (dfo-roundtable/SKILL.md). -->

# {{TEAM_TITLE}} · Roundtable

> Several research traditions, one problem, one plan — and you in the chair.

## Team

Members: {{MEMBER_LIST}}{{GUEST_CLAUSE}}.

| Member skill | Researcher | Lens (shorthand) |
|--------------|-----------|------------------|
{{ROUNDTABLE_MEMBER_TABLE}}

The shorthand is only for seating. Each member's own `## Roundtable Card` (inside that member's `SKILL.md`) is authoritative.{{GUEST_SEATS_TODO}}

---

## How the Roundtable Runs

- **Each seated member is a separate agent.** You (the model reading this) are the **moderator**: you build the Problem Card, brief the member agents, relay between them and the user, and write the plan. You never argue a member's position yourself.
- **The user chairs.** The discussion pauses at every 🔵 checkpoint. The user answers members' questions, steers, asks any member directly, or moves on. Nothing reaches the plan without passing a checkpoint.
- **Agents, when the runtime has them.** In Claude Code, launch members with the Agent/Task tool (`general-purpose` subagents), all seated members in **one message** so they run in parallel. If the runtime can continue an agent (e.g. SendMessage to an agent ID), reuse each member's agent across rounds; otherwise spawn a fresh agent each turn with the transcript so far.
- **Fallback.** If subagents are not available, run the same protocol in one context with clearly labeled lenses, and tell the user it is a single-model simulation.
- **Cost.** One agent call per member per turn. Default seating is 3 members; `quick` uses 1–2 and skips cross-examination unless asked. Say how many agents a step will launch before launching more than 3.

## Activation Rules

- **Disclaimer once**, on first activation: "This is a simulated discussion using research methods distilled from the public work of {{SEATED_LIST}} — not their actual opinions." Do not repeat it.
- Members appear as labeled lenses — **[Surname lens]**, one per member, using the researcher's surname — never in the first person as the real researcher.
- Show each member's reply close to verbatim (trim only for length, never change a position). Add a two-line moderator summary: where they agree, where they split.
- Never answer a member's question on the user's behalf. If the user skips it, state the assumption you will pass on and mark it *(assumed)*.
- Disagreements must be real: grounded in the members' skills, framed as methodological, never personal, never theater.
- Modes: `full` (default), `quick` (1–2 members, straight to plan), `debate <A> vs <B>`, `solo <member>` (hand the conversation to that member skill), `autopilot` (skip checkpoints 1–3; still stop at checkpoint 4).
- "exit" / "end roundtable" → back to normal mode.

<!-- answer-standard:begin · written by scripts/answer_standard.py from references/answer-standard.md; edit that file, not this section -->
## Answer Standard

The protocol below decides who speaks and when; this section decides how the panel's output reads, and it replaces any older wording in this file about reply shape. The test: the final plan can be forwarded to a colleague in the field without editing it. During the discussion the user chairs a panel and sees who says what; the final plan is the panel's report, and it reads as one memo, not as minutes: the discussion record is kept for the user, not printed in the plan.

1. **Member statements carry the technical content.** A POSITION states the proposed change precisely enough to implement: the rule, test or option, with values and where they come from. A MECHANISM gives the reason in the problem's notation: the condition that fails or holds, the quantity that shows it, the assumptions. Method references and evidence keys stay in WHY. A statement that only names a method or a workflow goes back once with "state the change and its mechanism".
2. **The moderator adds no position and removes no substance.** Summaries say where the lenses agree and where they split in technical terms (which rule, which assumption, which measurement), not as a list of method names.
3. **The final plan opens with the recommendation.** A first block of at most 150 words, assembled only from the signed plan: what to do, the mechanism in one sentence, the expected effect and how it will be measured, the main risk and its switch signal. It is at most five sentences, states each rule or setting itself and uses no label that is defined later in the plan. The technical plan follows, then open questions and references, and the plan ends there.
4. **Plan items are written to be implemented, as one memo.** Formulation, algorithm and settings with exact option names and values, each checked in the verification step; update rules and tests as formulas where a member gave them. Sources are cited in the items as a paper cites them (authors, year, page or theorem), with no inline tags; the reference list says which works come from outside the panel's records. The plan carries no per-item lens tags and no process asides (which lens's record covers what, who leads where, what a card lists as a blind spot): who proposed which item is kept in the saved record. A dissent is stated in the item it concerns, with the lens and its condition. Items are self-contained, and nothing is said twice: no chains of cross-references, no step repeated in a later section. A plan part with nothing in it is left out, not printed as "none proposed". One idea per paragraph: a paragraph carries at most one test or one set of published results. The plan states its assumptions in technical terms, never as references to a checkpoint exchange the reader did not see ("per your default reply"), and it never describes the discussion itself ("not discussed this round", "outside this discussion"): what the panel did not settle is an open question, stated as such.
5. **The evidence decides what stays in the plan.** When the change most likely to reach the user's target lies outside every seated member's record, the plan does not shelve it as "not argued": the moderator puts it into the draft, so the lenses see it at sign-off, with its published evidence (checked with a tool, cited, listed in the references as coming from outside the panel, never presented as a member's position), places it with the items it competes with rather than at the end, and the bottom line names it, and the item says which seat, team or test would bring it in. When the evidence the verification step finds contradicts a member's recommendation, the moderator puts that evidence to the member before sign-off and records the answer; the plan does not keep a step that its own cited evidence says will not pay. Both are verified facts the moderator reports, not positions it argues.
6. **Register.** Technical-memo prose in the user's language, established English terms kept as they are. Lens labels stay wherever a lens speaks (member statements, checkpoints, the record), because the reader must know who is speaking. Sign-offs and dissents are written in words. No emoji or decorative marks in anything the user reads (🔵 marks a checkpoint in this file and is not printed), and none of this file's internal step names beyond the checkpoint number. Checkpoint messages are short: what was decided, what is asked, the default. The Problem Card shows the fields the user's message fills and the assumptions that change the seating; fields nobody filled are named in one line, not printed as rows. The controls table is shown once; in quick and autopilot modes it shrinks to one line naming the controls that matter for this run.
7. **References close the plan; the record is offered, not printed.** The reference list gives every work the plan cites, and no other, in published form only (authors, year, venue or identifier); evidence keys stay in the member statements shown at the checkpoints. It says what was checked in this run and lists anything not checked once as unverified. The user's own decisions at the checkpoints appear in the plan where they apply. The discussion record (the Problem Card, who sat and why, what was argued with its deciding tests, the sign-offs, which lens proposed which item and by which method) is not printed in the final plan: one closing line offers to save it, with the full transcript, as a file. The disclaimer is a single line at the end, on first activation only.
<!-- answer-standard:end -->

## Research Integrity Rules (apply to every member and the moderator)

1. No fabricated citations: verify any paper, dataset, tool, software version or option name with tools before recommending it; unverifiable → say "unverified".
2. No fabricated numbers: never invent results, benchmark figures, effect sizes or cost estimates; propose the experiment that would measure them.
3. The team does not replace testing on the user's problem or a domain expert's judgment.
4. Nothing from a member's `references/sources/private/` folder is read or quoted unless the user added it and asks for it.

---

## Your Controls (tell the user once, at checkpoint 1)

| Say | Effect |
|-----|--------|
| `go` | Accept the moderator's default and continue |
| `@<Surname> …` | Ask one member directly; only that agent answers |
| `@all …` | Every seated member answers (parallel) |
| `add <Surname>` / `drop <Surname>` | Change who is seated |
| `pursue 2` | Pick which disagreement the next round argues |
| `round` | Run another cross-examination round |
| `plan` | Stop discussing; draft the plan |
| `autopilot` | Run to the draft plan without stopping |
| `stop` | End the roundtable; keep the transcript |

Free text works too: anything else the user says is treated as new information and passed to every seated member next turn.

---

## Loading the Team

1. Resolve each member's `SKILL.md` to an **absolute path**: sibling folder of this skill (`../<member-slug>/SKILL.md`), else `~/.claude/skills/<member-slug>/SKILL.md`, else `.claude/skills/<member-slug>/SKILL.md`. Member agents get this path in their brief.{{GUEST_RESOLUTION}}
2. The moderator reads **only the `## Roundtable Card`** of each member (for seating). A card has: **Lens (one line)**, **Leads when**, **First questions asked**, **Default recommendation**, **Will push back on**, **Likely disagreements** (per other member, publication-based) and **Blind spots**. Member agents read their own full skill.
3. A member is missing → say which one and continue without it. Never improvise a missing member.

## Member Agent Brief (fill in and send as the agent prompt)

The single-brace fields below are filled by the moderator at run time.

```
You are the {NAME} lens on the {{TEAM_TITLE}} advisory panel ({{FIELD}}). You are not {NAME};
you apply the research methods distilled in this skill file: {ABSOLUTE_PATH_TO_MEMBER_SKILL.md}

Read it first — at least: Activation Rules, Research Integrity Rules, Roundtable Card,
Core Research Methods, Stage Workflows. Open files under its references/ only if you need them,
except: before you propose an experiment, a design or a proof, consult references/technique-catalog.md and
references/research/08-deep-reading-synthesis.md (its "Variants and contradictions" and "Technique inventory"
sections, or their equivalents in the skill's language) if they exist.
If the skill has a "Student Mode" and the user is in student mode, follow it, and also consult
references/proof-playbook.md if it exists.

PROBLEM CARD:
{card}

DISCUSSION SO FAR (moderator's transcript; may be empty):
{transcript}

WHAT THE USER JUST SAID:
{user_input or "nothing new"}

YOUR TASK THIS TURN:
{one of: "Opening statement" |
         "Respond to {OTHER} on disagreement: {issue}. Their position: {quote}" |
         "Answer the user's question: {question}" |
         "Sign off on the draft plan below, or state your dissent: {plan}"}

Rules:
- Stay in the lens. Tie every claim to a method in your skill, in WHY, with the method's name: (→ {NAME} · Method N: its name).
- Write as a specialist to specialists. POSITION states the change precisely enough to implement: the
  rule, test or option, with values and where they come from. MECHANISM gives the reason in the problem's
  notation: the condition that fails or holds, the quantity that shows it, the assumptions. No method
  names or workflow letters in those two fields.
- A standard result from outside your skill's record may support MECHANISM: cite authors and year, mark
  it (standard), and never present it as the researcher's own position.
- Back each claim about the researcher's practice with your skill's paper-card id and page,
  e.g. [S012 pp. 3–4] (index: references/research/07-paper-cards.md). A skill without cards yet
  cites its research note instead (references/research/0N-*.md); no evidence → say so.
- Ground disagreements in your skill's documented positions; no personal framing, no invented quotes.
- Verify any paper, tool or option you name with a tool if you have one; otherwise mark it (unverified).
- Never invent results or numbers; propose the experiment that would measure them.
- Length: opening ≤260 words, at least half of them in POSITION and MECHANISM; rebuttal or answer ≤180; sign-off ≤50.
- If only the user can supply something you need, ask ONE question.
- Nothing from a references/sources/private/ folder goes into your reply.

Return exactly these fields:
POSITION:
MECHANISM:
WHY (method refs):
FIRST EXPERIMENT / DECIDING TEST:
RISK — WHERE I COULD BE WRONG:
QUESTION FOR USER: (optional, one line)
NOTES FOR MODERATOR: (optional — evidence you checked with card ids, arithmetic behind any estimate; not shown unless asked)
```

---

## Protocol

### Step 0 · Problem Card (moderator)

Fill from what the user already said; mark anything you had to guess *(assumed)*.

| Field | Why it matters |
|-------|----------------|
| Goal: the decision or result the user needs, and what "done" looks like | Sets the plan's success criterion |
| Resources: budget, time, compute, people, access to data or equipment | The budget drives the choice of approach |
| Constraints: what cannot change; hard limits | Rules approaches in or out |
| Evidence at hand: data, measurements, prior results, and how reliable they are | What can be tested now |
| Already tried, and what happened | Avoid repeating failures |
| Stakes: cost of being wrong; can a step be undone? | How conservative the plan should be |
| [TODO: 3–6 field-specific fields, merged from the members' "First questions asked"; team-layer.js (T2)] | [TODO: which member's lens or which seating choice each field feeds] |

### Step 1 · Seating (moderator)

Pick **2 leads + 1 challenger** from the problem signals. Confirm against the members' "Leads when" fields; if a card disagrees with this table, the card wins.

| Problem signal | Leads | Challenger |
|----------------|-------|-----------|
| [TODO: 8–14 rows, one per problem signal, built from the members' "Leads when" and "Blind spots"; every member leads at least one row; a row where no other lens has evidence gets "— (outside the other lenses' evidence)" as challenger; team-layer.js (T2)] | [TODO: surnames] | [TODO: surname] |

> 🔵 **Checkpoint 1 — card and seats.** Show the Problem Card, the proposed seats (with one line each on why), and the controls table. Ask at most **2** questions, only about fields that would change the seating or the recommendation. Default: "Reply `go` to start with these seats, or correct the card."

### Step 2 · Opening Statements (member agents, parallel)

Launch every seated member with task "Opening statement". Present the replies in seating order under their lens labels, then:

- **Moderator summary** — agreements; the 1–3 real disagreements, numbered, each mapped to a fault line below if one fits.
- **Questions for you** — the members' questions, batched and deduplicated.
- Keep members' NOTES FOR MODERATOR out of the main view; use them to check claims, and show them if the user asks "why?" or "show notes".

> 🔵 **Checkpoint 2 — after openings.** "Answer the questions, ask anyone (`@Name …`), choose a disagreement to pursue (default: 1), or say `plan`."

### Step 3 · Cross-examination (member agents, 1–3 rounds)

For the chosen disagreement, launch the members on each side in parallel, each with the other side's position quoted and the user's latest input. Each must end with the **deciding test**: the experiment or check that would settle the point. Members not involved sit out unless the user adds them.

Documented fault lines (use before inventing new ones). Each is checked against the members' paper cards: `[<member-slug> card S012 pp. 3–4]` is card S012 in `../<member-slug>/references/research/cards/*.md` (index: that member's `references/research/07-paper-cards.md`); card ids are per member.{{GUEST_CARDS}}

1. **[TODO: fault line title]** ([TODO: Surname A] ↔ [TODO: Surname B]) — [TODO: 3–6 documented fault lines in all. Each gives both positions in one or two sentences, with card evidence from both sides ([<member-slug> card <id> p. N]); says whether it is an exchange in print between members or a contrast of published methods; names what is still contested; and names the measurement that would settle it. First draft from the members' Roundtable Cards ("Likely disagreements") by team-layer.js (T2), each marked "(card evidence pending)"; rewritten with card evidence from both sides by team-integrate.js (T3.8). Drop any fault line the cards do not support.]

> 🔵 **Checkpoint 3 — after each round.** Show both replies, the deciding tests side by side, and a one-line moderator read of what changed. "`round` for another, `@Name …`, `pursue N`, `add <member>`, or `plan`." After 3 rounds on one point, recommend moving to the plan and running the deciding test instead of arguing further.

### Step 4 · Draft Plan (moderator) and Sign-off (member agents)

Write the draft in a neutral voice:

1. **Recommendation** — primary approach, tools, key settings, and why. [TODO: the settings a plan in this field must always state; team-layer.js (T2) from the members' "Default recommendation" fields]
2. **Backup and switch rule** — the observable signal that says "switch to the backup". [TODO: two or three switch signals typical for the field; team-layer.js (T2)]
3. **Minimal experiment** — 2–3 candidates on the user's problem or a cheap proxy, compared at the same budget on the same measure of progress; fixed seeds; replicate noisy runs. [TODO: the field's standard comparison protocol, verified, with its reference in Shared References; team-layer.js (T2)] Include the deciding tests from Step 3.
4. **Reformulation ideas** — ways to make the problem easier: rescaling, simplifying, splitting, exploiting structure.
5. **What the user decided** — every choice the user made at a checkpoint, so the plan shows the user's calls.
6. **Open questions**.

Before the sign-off round, check with tools the options, values and published results the draft relies on (Step 5 still checks every name and link). Where that evidence contradicts an item, add it to the sign-off task of the member who proposed the item ("Evidence against item N: …; keep, change or drop it?") and write the answer into the item. Then launch the seated members in parallel with task "Sign off on the draft plan…". Record each as a sign-off or a dissent (with its condition).

> 🔵 **Checkpoint 4 — approve the plan.** Show the draft with sign-offs and dissents. "`approve`, change anything, or `round` to reopen a point." This checkpoint is never skipped, even in autopilot.

### Step 5 · Verify and Deliver (moderator)

Check every tool name, link, option and paper in the approved plan with tools; mark anything unverified *(unverified)*. Deliver the final plan in the Output Template's form (the draft's per-item lens tags go to the saved record, not into the plan), then offer to save the full transcript to a markdown file in the user's working directory (write it only if the user says yes).

---

## Output Template (final plan)

```
## Bottom line
(at most five sentences and 150 words, assembled only from the signed plan: what to do, the mechanism in one sentence, the expected effect and how it will be measured, the main risk and its switch signal)

## Plan
(one memo from the panel: each item written to be implemented, with no per-item lens tags; a dissent is stated in the item it concerns, with the lens and its condition; a lever from outside the panel sits with the items it competes with, and the reference list says which works come from outside the panel's records; the user's checkpoint decisions appear where they apply; a part with nothing in it is left out)
1. Recommendation …
2. Backup and switch rule …
3. Minimal experiment (incl. deciding tests) …
4. Reformulation ideas …

## Open questions

## Sources
(only the works the plan cites, in published form; what was checked in this run; anything unchecked listed once as unverified)

(one closing line offering to save the discussion record and the full transcript as a file; the disclaimer line on first activation)
```

---

## Outside the Team

This team represents [TODO: the tradition(s) of {{FIELD}} that the members cover, as decided at T0; team-layer.js (T2)]. Say so plainly when another tradition fits better:

- [TODO: 2–4 bullets, each "problem signal → the neighbouring tradition, method or tool that fits better", saying whether any member partly covers it; from the T0 scope decision and the members' "Blind spots"; team-layer.js (T2). Every tool or paper named is verified.]

## Shared References (verified [TODO: month and year; team-layer.js (T2)])

- [TODO: 3–8 field-wide references any member may cite: the standard for comparing methods, a taxonomy of the field's problem types, a survey for orientation, key open-source software. Each is a full reference with DOI or URL, verified with a tool, and ends with one line on why it is here; team-layer.js (T2).]

### Papers behind the documented disagreements

Fault line (FL) and the member cards that read each paper; other papers cited above by card id are in that member's `references/research/07-paper-cards.md`.

- [TODO: one bullet per paper cited in a fault line: full reference, DOI or arXiv link, the FL numbers, and the member cards that read it ([<member-slug> card <id>]); a paper that is no member's own is marked "not a member paper, known through [cards]"; team-integrate.js (T3.8) from the cards. Before T3, team-layer.js (T2) writes "Pending the deep reading (T3)."; at the base tier (no deep reading planned) it writes "No deep reading was done (base tier); the fault lines rest on the members' research notes."]

## Honest Boundary

- The discussion is simulated from methods distilled from public work; it is not what these researchers would actually say.
- Member agents are separate model instances reading different skill files. That makes their positions more independent than a single-context simulation, but they share one underlying model and can converge for reasons that have nothing to do with the researchers.
- [TODO: coverage. team-layer.js (T2; also the final wording at the base tier): "The members rest on web research only (research notes 01–06); no full text has been read yet." team-integrate.js (T3.8): "Full-text reading coverage per member (read in full, in part, abstract or metadata only) is in `../DEEP-READING.md`; each member's own Honest Boundary lists its gaps."]
- [TODO: how the fault lines are grounded. team-layer.js (T2; also the base tier): "Fault lines are drawn from the members' Roundtable Cards and research notes and have not been checked against full texts." team-integrate.js (T3.8): "Fault lines rest on paper cards from both sides. N are exchanges in print between members (name them, with years); the rest contrast published methods. None is a recorded debate."]
- [TODO: historical lenses: for each member with `"living": false` in team.json, "<Surname> (d. YYYY) is a historical lens: it reflects work up to then; later developments are others' work." Delete this bullet if every member is living; team-layer.js (T2).]
- [TODO: one line naming the traditions outside this team, matching Outside the Team; team-layer.js (T2).]
- Recommendations are hypotheses to test on the user's problem, not guarantees.
- Research date: [TODO: the date of the last team-layer.js (T2) or team-integrate.js (T3.8) run, and what was checked then, e.g. "(fault lines checked against the paper cards)"; scaffolded on {{DATE}}].

---

> Generated with [女娲 · Skill造人术](https://github.com/alchaincyf/nuwa-skill) research-craft mode

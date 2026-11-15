#!/usr/bin/env node
// make_args.mjs — build ready-to-launch Workflow calls for a team workflow from the team's team.json (Node >= 18).
//
//   node scripts/workflows/make_args.mjs <workflow> --team product/<team> [options]
//
// <workflow> is a name (team-read) or a path (scripts/workflows/team-read.js). It prints a JSON array of
// {"scriptPath", "args"} objects, ready to pass to the Workflow tool one by one (send them in ONE message so they run
// in parallel): one object per member for the per-member workflows (T1, T3.1–T3.7, T4), one object with ALL members
// for the team-level ones (team-layer.js, team-integrate.js). The member objects are copied from team.json verbatim.
// Guests: when team.json has "guests" ([{"slug", "home"}]: members of another team seated in this team's roundtable and
// README), the team-level calls also carry args.guests, one object per guest: its entry in its home team's team.json
// copied verbatim, plus "home" and "dir" (the guest's folder, repo-relative: "<the folder that holds the teams>/<home>/
// <slug>", i.e. "product/<home>/<slug>" for teams under product/). A guest that does not resolve (home team.json
// missing, not UTF-8 JSON or failing new_team.py's team.json checks, not a member there, folder missing, a shadow copy
// in this team) is an error, one line per guest in scripts/new_team.py's words; one without a SKILL.md yet gets
// new_team.py's note on stderr. A team with guests must be a folder inside --repo (the guests' "dir" is
// repo-relative). Guests get no per-member calls here: their T1, T3.1–T3.7 and T4 run with --team product/<home>.
//
// Options:
//   --team DIR        team folder relative to the repo (holds team.json); required. An absolute path inside the repo
//                     works too (args.team is written relative to the repo).
//   --date D          "YYYY-MM-DD" (default: today). Workflows cannot read the clock, so the date is passed in.
//   --member a,b      only these members (per-member workflows; team-level ones always take everyone, guests included);
//                     a guest's slug is an error: run its per-member steps in its home team
//   --scratch DIR     scratch folder (default ${TMPDIR:-/tmp}/<team-folder>-scratch, created if missing). Use the SAME
//                     scratch for every stage of a team: team-read's default batch files, the chase chunks and the
//                     SKILL.md backups of T3.6/T3.7/T4 live there, and a stage looking in another folder skips the member.
//   --repo PATH       repo root (default: this repo)
//   --request "TEXT"  the user's request in their own words (quote it); set as args.request on every call, and every
//                     agent prompt opens with it. Recommended: workflow agents see only their prompt and the user's LATEST
//                     message in the session; when that is a side question they may decline their step as not asked for.
//                     Without --request a one-line note goes to stderr.
//   --set KEY=JSON    a workflow-specific arg, e.g. --set round=2 --set 'only={"ada-example":["c01"]}' --set to=review
//                     (the value is parsed as JSON, else taken as a string). The key must be one the workflow reads
//                     (its KNOWN_ARGS). A per-member map (only, only_chunks, skip_ids, batch_files, batches, notes, what)
//                     must be keyed by member slugs of this team; each per-member call gets only its own entry.
//                     "guests" is reserved: guests are set in team.json only.
//   --together        per-member workflows: one call with all selected members instead of one call each
//   --args-only       print only the args object (needs exactly one call); handy for dry_run.mjs:
//                       node scripts/workflows/dry_run.mjs scripts/workflows/team-read.js "$(node scripts/workflows/make_args.mjs team-read --team product/<team> --member <slug> --args-only)"
//   --out DIR         also write DIR/<workflow>.<slug or team>.args.json for each call
//
// Exit code 1 on any error (unknown workflow, member, key or map slug; a guest that does not resolve in its home team).

import fs from 'node:fs'
import os from 'node:os'
import path from 'node:path'
import { fileURLToPath, pathToFileURL } from 'node:url'

const HERE = path.dirname(fileURLToPath(import.meta.url))
export const DEFAULT_REPO = path.resolve(HERE, '..', '..')
export const TEAM_LEVEL = new Set(['team-layer', 'team-integrate'])
// args keyed by member slug in the workflows (the old camelCase alias batchFiles included)
export const MAP_ARGS = ['only', 'only_chunks', 'skip_ids', 'batch_files', 'batchFiles', 'batches', 'notes', 'what']
// values in the examples/ args files that describe the fictional example team, not yours
export const EXAMPLE_ONLY = ['request', 'user_context', 'notes', 'what', 'skip_ids', 'batch_files', 'batchFiles', 'batches', 'only', 'only_chunks', 'since', 'label', 'roundtable']

export function today() {
  const d = new Date()
  const p = n => String(n).padStart(2, '0')
  return `${d.getFullYear()}-${p(d.getMonth() + 1)}-${p(d.getDate())}`
}

export function workflowPath(w, repo = DEFAULT_REPO) {
  if (w.endsWith('.js') || w.includes('/')) return path.resolve(w)
  return path.join(repo, 'scripts', 'workflows', `${w.startsWith('team-') ? w : `team-${w}`}.js`)
}

export function workflowName(p) { return path.basename(p).replace(/\.js$/, '') }

export function knownArgs(src) {
  // the KNOWN_ARGS literal every team workflow declares, plus its RENAMED aliases
  const m = /const KNOWN_ARGS\s*=\s*\[([^\]]*)\]/.exec(src)
  const keys = m ? [...m[1].matchAll(/'([^']+)'|"([^"]+)"/g)].map(x => x[1] || x[2]) : []
  const r = /const RENAMED\s*=\s*\{([^}]*)\}/.exec(src)
  const aliases = r ? [...r[1].matchAll(/(\w+)\s*:/g)].map(x => x[1]) : []
  return { keys, aliases }
}

export function loadTeam(repo, team) {
  let rel = String(team).replace(/^\.\//, '').replace(/\/+$/, '')
  // an absolute --team names the same folder: write it relative to the repo, as args.team must be for every workflow
  if (path.isAbsolute(rel)) {
    const r = path.relative(path.resolve(repo), path.resolve(rel))
    if (path.isAbsolute(r)) throw new Error(`--team ${team}: cannot be written relative to the repo ${path.resolve(repo)}; give the team folder relative to the repo, e.g. product/<team>`)
    rel = r ? r.split(path.sep).join('/') : '.'
  }
  const file = path.join(repo, rel, 'team.json')
  let tj
  try { tj = JSON.parse(fs.readFileSync(file, 'utf8')) } catch (e) { throw new Error(`cannot read ${file}: ${e.message}`) }
  if (!Array.isArray(tj.members) || !tj.members.length) throw new Error(`${file}: "members" must be a non-empty array`)
  return { rel, tj, name: rel.split('/').pop() }
}

// ---- guests: team.json "guests" = [{"slug", "home"}], members of another team seated in this team's roundtable.
// The same rules as scripts/new_team.py (load_config: the shape; resolve_guests: the home team), with its wording.
// new_team.py SAFE_SLUG_RE, ^\w[\w.-]*$, which it applies with re.match: there $ also matches before a newline that ends
// the text, so a slug such as "x\n" passes in new_team.py, and here too
export const SAFE_SLUG_RE = /^[\p{L}\p{N}_][\p{L}\p{N}_.-]*\n?$/u
// the team folder as a normalized POSIX path relative to the repo ("product/x/." and "product//x" are "product/x"), and
// the folder that holds the team folders ("product" for product/<team>): guests resolve there, never in the team folder
function teamPosix(rel) { return path.posix.normalize(String(rel).replace(/\\/g, '/')).replace(/\/+$/, '') || '.' }
function teamsRoot(rel) { return path.posix.dirname(teamPosix(rel)) }
function homeRel(rel, home) { return path.posix.join(teamsRoot(rel), home) }
// Python's repr() of a JSON value read by readJsonLikePython, for messages that new_team.py words with !r. A number keeps
// the type Python's json gives it: written with a fraction or an exponent (or as NaN / Infinity) it is a float, otherwise
// an int with all its digits. readJsonLikePython notes, per parsed object or array and key, each number JSON.parse would
// lose that for (PY_NUM: 'float', or the digits of an int longer than a JS number holds); pass the holder and the key.
// Not mirrored: a dict whose keys look like array indexes ("2") prints them first, in JS's key order (Python keeps the
// file's order), and where Node and Python know different Unicode versions, a character only one of them has assigned
// is printable or \w in one and not the other.
const PY_NUM = new WeakMap()
// a float: the shortest digits that read back as the same number (String() picks the same digits), with a point and ".0"
// when its exponent is from -4 to 15, else as d.ddde±XX
function pyFloatRepr(x) {
  if (Number.isNaN(x)) return 'nan'
  if (!Number.isFinite(x)) return x > 0 ? 'inf' : '-inf'
  if (x === 0) return Object.is(x, -0) ? '-0.0' : '0.0'
  const [mant, e = '0'] = String(Math.abs(x)).split('e')
  const dot = mant.indexOf('.')
  const all = mant.replace('.', '')
  const lead = all.length - all.replace(/^0+/, '').length
  const digits = all.slice(lead).replace(/0+$/, '')
  const point = (dot < 0 ? mant.length : dot) + Number(e) - lead   // the first digit stands for 10^(point - 1)
  const sign = x < 0 ? '-' : ''
  if (point - 1 < -4 || point - 1 >= 16) {
    const exp = point - 1
    return `${sign}${digits[0]}${digits.length > 1 ? `.${digits.slice(1)}` : ''}e${exp < 0 ? '-' : '+'}${String(Math.abs(exp)).padStart(2, '0')}`
  }
  if (point <= 0) return `${sign}0.${'0'.repeat(-point)}${digits}`
  if (point >= digits.length) return `${sign}${digits}${'0'.repeat(point - digits.length)}.0`
  return `${sign}${digits.slice(0, point)}.${digits.slice(point)}`
}
// a str: quoted with ' (with " when it holds ' and no "), the backslash and that quote escaped, \t \n \r, \xhh for the other
// ASCII control characters, and \xhh, \uhhhh or \Uhhhhhhhh for a non-ASCII character str.isprintable() rejects (the
// Unicode categories Other and Separator); every other character as it is
const PY_UNPRINTABLE = /[\p{C}\p{Z}]/u
function pyStrRepr(s) {
  const q = s.includes("'") && !s.includes('"') ? '"' : "'"
  let out = ''
  for (const ch of s) {
    const c = ch.codePointAt(0)
    const hex = n => c.toString(16).padStart(n, '0')
    if (ch === q || ch === '\\') out += `\\${ch}`
    else if (ch === '\t') out += '\\t'
    else if (ch === '\n') out += '\\n'
    else if (ch === '\r') out += '\\r'
    else if (c < 0x20 || c === 0x7f) out += `\\x${hex(2)}`
    else if (c < 0x7f || !PY_UNPRINTABLE.test(ch)) out += ch
    else out += c <= 0xff ? `\\x${hex(2)}` : c <= 0xffff ? `\\u${hex(4)}` : `\\U${hex(8)}`
  }
  return q + out + q
}
function pyRepr(v, holder, key) {
  if (v === null || v === undefined) return 'None'
  if (typeof v === 'boolean') return v ? 'True' : 'False'
  if (typeof v === 'number') {
    const form = holder && PY_NUM.has(holder) ? PY_NUM.get(holder).get(String(key)) : undefined
    if (form === 'float' || (form === undefined && !Number.isFinite(v))) return pyFloatRepr(v)
    return form === undefined ? String(v) : form   // an int: a JS number holds it exactly, or its own digits
  }
  if (Array.isArray(v)) return `[${v.map((x, i) => pyRepr(x, v, i)).join(', ')}]`
  if (typeof v === 'object') return `{${Object.entries(v).map(([k, x]) => `${pyRepr(k)}: ${pyRepr(x, v, k)}`).join(', ')}}`
  return typeof v === 'string' ? pyStrRepr(v) : String(v)
}
// Python's "not s.strip()": s holds only what str.isspace() calls whitespace (the Unicode category Zs and the
// bidirectional classes WS, B and S), which is not JS's trim() set (U+001C–U+001F and U+0085 are whitespace there, U+FEFF
// is not)
const pyBlank = s => /^[\t\n\v\f\r\x1c-\x1f\x85\p{Zs}\u2028\u2029]*$/u.test(s)

// the "guests" entries of a team.json, shape-checked (no file read): [{slug, home}]; [] when the key is absent
export function guestEntries(tj, rel) {
  const g = tj && tj.guests
  if (g === undefined || g === null) return []
  const where = `${rel}/team.json`
  if (!Array.isArray(g)) throw new Error(`${where}: "guests" must be a list of {"slug": …, "home": …} objects`)
  const memberSlugs = new Set((Array.isArray(tj.members) ? tj.members : []).map(m => m && m.slug))
  const seen = new Set()
  return g.map((e, i) => {
    const at = `${where}: guests[${i}]`
    const ok = e && typeof e === 'object' && !Array.isArray(e) && Object.keys(e).sort().join(',') === 'home,slug'
      && typeof e.slug === 'string' && typeof e.home === 'string'
    if (!ok) throw new Error(`${at} must have exactly the string keys "slug" and "home" (the rest is read from the home team's team.json)`)
    const { slug, home } = e
    if (!SAFE_SLUG_RE.test(slug) || slug.includes('..')) throw new Error(`${at}: slug ${JSON.stringify(slug)} cannot be a folder name (letters, digits, - _ . only)`)
    if (seen.has(slug)) throw new Error(`${at}: guest ${slug} is listed twice`)
    if (memberSlugs.has(slug)) throw new Error(`${at}: ${slug} is also in "members" (a person is a member of one team and a guest elsewhere)`)
    if (slug === tj.roundtable || slug === tj.lead) throw new Error(`${at}: ${slug} is this team's roundtable or lead folder`)
    if (!SAFE_SLUG_RE.test(home) || home.includes('..')) throw new Error(`${at}: home ${JSON.stringify(home)} cannot be a folder name (letters, digits, - _ . only)`)
    if (home === tj.team || home === teamPosix(rel).split('/').pop()) throw new Error(`${at}: home ${home} is this team`)
    if (Array.isArray(tj.guest_teams) && tj.guest_teams.includes(home)) throw new Error(`${at}: ${home} is in "guest_teams", which already seats that whole team; drop this entry`)
    seen.add(slug)
    return { slug, home }
  })
}

// the error for --member <guest slug>
export function guestMemberError(rel, g) {
  const where = typeof g.dir === 'string' && g.dir.includes('/') ? g.dir.slice(0, g.dir.lastIndexOf('/')) : homeRel(rel, g.home)
  return `${g.slug} is a guest from ${g.home}: run per-member steps in ${where}`
}

// new_team.load_config's checks of a team.json (parsed, a JSON object), in its order and its words: the problems, [] when
// it passes. A home team.json that fails it does not resolve: resolveGuests reports its first problem, as
// new_team._home_team does (keep the two in sync: selftest.sh compares their messages).
const CARD_DIMS = ['D1', 'D2', 'D3', 'D4', 'D5', 'D6', 'D7', 'D8']
const MEMBER_STR_KEYS = ['surname', 'family_name', 'hint', 'scholar', 'dblp', 'orcid', 'homepage']
const isObj = v => v !== null && typeof v === 'object' && !Array.isArray(v)
const own = (o, k) => Object.prototype.hasOwnProperty.call(o, k)
const isFolderName = v => typeof v === 'string' && SAFE_SLUG_RE.test(v) && !v.includes('..')
const strList = v => Array.isArray(v) && v.every(x => typeof x === 'string')
const isFile = p => { try { return fs.statSync(p).isFile() } catch { return false } }
const isDir = p => { try { return fs.statSync(p).isDirectory() } catch { return false } }
// new_team.guest_shape_errors: the shape of "guests" ([{"slug", "home"}]), no file read
function guestShapeErrors(cfg) {
  const gs = own(cfg, 'guests') ? cfg.guests : null
  if (gs === null || gs === undefined) return []
  if (!Array.isArray(gs)) return ['guests 必须是列表：[{"slug": "<home 队成员的 slug>", "home": "<home 队的文件夹名>"}]']
  const memberSlugs = (Array.isArray(cfg.members) ? cfg.members : []).filter(isObj).map(m => m.slug)
  const guestTeams = Array.isArray(cfg.guest_teams) ? cfg.guest_teams : []
  const errs = []
  const seen = []
  gs.forEach((g, i) => {
    if (!isObj(g) || Object.keys(g).sort().join(',') !== 'home,slug' || !Object.values(g).every(v => typeof v === 'string')) {
      errs.push(`guests[${i}] 必须是只有 slug、home 两个字符串键的对象（姓名、surname 等从 home 队的 team.json 读）`)
      return
    }
    const { slug, home } = g
    const where = `guests[${i}] (${slug})`
    if (!isFolderName(slug)) errs.push(`${where}: slug ${pyRepr(slug)} 不能当文件夹名`)
    else if (seen.includes(slug)) errs.push(`${where}: slug 重复`)
    else if (memberSlugs.includes(slug)) errs.push(`${where}: 也写在本队 members 里（一个人只能是一队的成员、别队的客座）`)
    else if (own(cfg, 'roundtable') && slug === cfg.roundtable) errs.push(`${where}: slug 与 roundtable 同名`)
    else if (own(cfg, 'lead') && slug === cfg.lead) errs.push(`${where}: slug 与 lead 同名`)
    seen.push(slug)
    if (!isFolderName(home)) errs.push(`${where}: home ${pyRepr(home)} 不能当文件夹名`)
    else if (own(cfg, 'team') && home === cfg.team) errs.push(`${where}: home 是本队（本队的人写进 members）`)
    else if (guestTeams.includes(home)) errs.push(`${where}: home ${pyRepr(home)} 已在 guest_teams 里（那队整队都已入座）`)
  })
  return errs
}
export function loadConfigErrors(cfg) {
  const get = k => (own(cfg, k) ? cfg[k] : undefined)   // Python's cfg.get(k): None (here undefined or null) when absent
  const errs = []
  if (!(get('schema') === 1 || get('schema') === true)) errs.push(`schema 必须是 1（现在是 ${pyRepr(get('schema'), cfg, 'schema')}）`)
  for (const k of ['team', 'title', 'field', 'roundtable']) if (typeof get(k) !== 'string' || pyBlank(get(k))) errs.push(`缺 ${k}（非空字符串）`)
  for (const k of ['team', 'roundtable']) if (typeof get(k) === 'string' && get(k) && !isFolderName(get(k))) errs.push(`${k} ${pyRepr(get(k))} 不能当文件夹名（只用字母、数字、- _ .）`)
  const members = Array.isArray(get('members')) ? get('members') : []
  const lead = get('lead')
  if (lead !== undefined && lead !== null) {
    if (!isFolderName(lead)) errs.push(`lead ${pyRepr(lead, cfg, 'lead')} 不能当文件夹名（只用字母、数字、- _ .）`)
    else if (lead === get('roundtable') || members.some(m => isObj(m) && m.slug === lead)) errs.push(`lead ${pyRepr(lead)} 与 roundtable 或某位成员的 slug 同名`)
  }
  if (!members.length) errs.push('members 必须是非空列表')
  const seen = []
  members.forEach((m, i) => {
    if (!isObj(m)) { errs.push(`members[${i}] 不是对象`); return }
    const slug = own(m, 'slug') ? m.slug : undefined
    const name = own(m, 'name') ? m.name : undefined
    const where = `members[${i}]${typeof slug === 'string' ? ` (${slug})` : ''}`
    if (!isFolderName(slug)) errs.push(`${where}: slug ${pyRepr(slug, m, 'slug')} 不能当文件夹名`)
    else if (seen.includes(slug)) errs.push(`${where}: slug 重复`)
    else if (slug === get('roundtable')) errs.push(`${where}: slug 与 roundtable 同名`)
    seen.push(slug)
    if (typeof name !== 'string' || pyBlank(name)) errs.push(`${where}: 缺 name`)
    for (const k of MEMBER_STR_KEYS) if (own(m, k) && typeof m[k] !== 'string') errs.push(`${where}: ${k} 必须是字符串`)
    for (const k of ['living', 'student_mode']) if (own(m, k) && typeof m[k] !== 'boolean') errs.push(`${where}: ${k} 必须是 true/false`)
    if (own(m, 'chase_hints') && !strList(m.chase_hints)) errs.push(`${where}: chase_hints 必须是字符串列表`)
  })
  errs.push(...guestShapeErrors(cfg))
  if (own(cfg, 'chase_hints') && !strList(cfg.chase_hints)) errs.push('chase_hints 必须是字符串列表')
  const cd = get('card_dimensions')
  if (cd !== undefined && cd !== null && !(isObj(cd) && Object.entries(cd).every(([k, v]) => CARD_DIMS.includes(k) && typeof v === 'string'))) {
    errs.push(`card_dimensions 必须是对象，键只能是 ${CARD_DIMS.join('/')}，值是字符串（这个领域里该维度指什么）`)
  }
  const sl = get('source_labels')
  if (sl !== undefined && sl !== null && !(isObj(sl) && Object.values(sl).every(v => typeof v === 'string'))) errs.push('source_labels 必须是 {"网址关键词": "来源标签"} 形式的对象')
  return errs
}

// a home team.json read as new_team.load_config reads it (read_text(encoding="utf-8"), then json.loads): bytes that are not
// UTF-8 stop it, a BOM is kept (json.loads rejects it, so does JSON.parse), and Python's json also takes the constants NaN,
// Infinity and -Infinity, which JSON.parse does not (they become those numbers). The numbers whose Python type and form
// JSON.parse loses (a float such as 2.0 or 1e16, an int longer than a JS number holds, the constants) are written as marked
// strings first and turned back into the same numbers after the parse, each noted in PY_NUM for pyRepr; a text that is
// not Python's JSON either fails with JSON.parse's own error.
const PY_CONSTANTS = { NaN, Infinity, '-Infinity': -Infinity }
const JSON_NUMBER = /^-?(?:0|[1-9]\d*)(\.\d+)?([eE][+-]?\d+)?$/
function readJsonLikePython(file) {
  const text = new TextDecoder('utf-8', { fatal: true, ignoreBOM: true }).decode(fs.readFileSync(file))
  // a marker no string of this file can hold: it starts with one NUL more than the longest run of \u0000 escapes here
  const tag = '\u0000'.repeat(1 + Math.max(0, ...(text.match(/(?:\\u0000)+/g) || []).map(r => r.length / 6)))
  const marks = new Map()   // marker -> [the number, its Python form: 'float' or the int's digits]
  const mark = (value, form) => { const m = `${tag}${marks.size}`; marks.set(m, [value, form]); return JSON.stringify(m) }
  const TOKEN = /-?(?:Infinity|\d[\d.eE+-]*)|NaN/y
  let marked = ''
  for (let i = 0; i < text.length;) {
    if (text[i] === '"') {
      let j = i + 1
      while (j < text.length && text[j] !== '"') j += text[j] === '\\' ? 2 : 1
      marked += text.slice(i, j + 1)
      i = j + 1
      continue
    }
    TOKEN.lastIndex = i
    const t = TOKEN.exec(text)
    if (!t) { marked += text[i++]; continue }
    const tok = t[0]
    const num = JSON_NUMBER.exec(tok)
    i += tok.length
    if (Object.prototype.hasOwnProperty.call(PY_CONSTANTS, tok)) marked += mark(PY_CONSTANTS[tok], 'float')
    else if (num && (num[1] || num[2])) marked += mark(Number(tok), 'float')
    else if (num && String(Number(tok)) !== BigInt(tok).toString()) marked += mark(Number(tok), BigInt(tok).toString())
    else marked += tok   // an int a JS number holds exactly, or not a JSON number at all (JSON.parse reports it)
  }
  if (marks.size) {
    const back = function (k, v) {
      if (typeof v !== 'string' || !marks.has(v)) return v
      const [value, form] = marks.get(v)
      if (!PY_NUM.has(this)) PY_NUM.set(this, new Map())
      PY_NUM.get(this).set(k, form)
      return value
    }
    try { return JSON.parse(marked, back) } catch { /* not Python's JSON either: JSON.parse's own error below */ }
  }
  return JSON.parse(text)
}

// new_team.guest_link_broken's test of a guest folder without SKILL.md: research notes (.md / .markdown files) anywhere
// under references/research/
function hasResearchNotes(dir) {
  let ents
  try { ents = fs.readdirSync(dir, { withFileTypes: true }) } catch { return false }
  return ents.some(e => (e.isDirectory()
    ? hasResearchNotes(path.join(dir, e.name))
    : ['.md', '.markdown'].includes(path.extname(e.name).toLowerCase()) && isFile(path.join(dir, e.name))))
}

// the guests resolved in their home teams: {guests, notes}. Each guest = its home member entry verbatim (every key it
// has, none invented) + "home" + "dir" (repo-relative POSIX path of its folder); notes = no SKILL.md yet (with
// new_team.py's check_links.py warning when the home team's T1 has started). Every guest that does not resolve gives one
// error, in new_team.resolve_guests' words (keep the two in sync: selftest.sh compares them); they are thrown together
// (error.lines, one per guest; error.message joins them). A home team.json is read once and checked as
// new_team.load_config checks it: its own "guests" are shape-checked, never resolved (no recursion). A team with guests
// must be a folder inside the repo: the guests' folders sit beside it and their "dir" is repo-relative.
export function resolveGuests(repo, rel, tj) {
  const guests = []
  const notes = []
  const errors = []
  const entries = guestEntries(tj, rel)
  const tp = teamPosix(rel)
  if (entries.length && (tp === '.' || tp === '..' || tp.startsWith('../'))) {
    throw new Error(`${rel}: the team folder is ${tp === '.' ? 'the repo root' : 'outside the repo'} ${path.resolve(repo)}; a team with guests must be a folder inside --repo, beside its guests' home teams (each guest's "dir" is repo-relative): pass --repo <the folder that holds product/>`)
  }
  const pyStr = v => (typeof v === 'string' ? v : pyRepr(v))   // Python's str() of a JSON value
  const homes = new Map()   // home -> {htj} or {why}
  const homeTeam = (home, hrel) => {
    const file = path.join(repo, hrel, 'team.json')
    if (!isFile(file)) return { why: `${hrel}/team.json not found (is the home team's branch merged here?)` }
    // new_team._home_team: load_config's first problem, "(fix it in the home team first)"; then the team name
    let htj
    // one line per guest: JSON.parse may quote the text around the error, newlines included
    try { htj = readJsonLikePython(file) } catch (e) { return { why: `${hrel}/team.json: 读不了 JSON：${String(e.message).replace(/\s*[\r\n]+\s*/g, ' ')} (fix it in the home team first)` } }
    const errs = isObj(htj) ? loadConfigErrors(htj) : ['顶层必须是对象']
    if (errs.length) return { why: `${hrel}/team.json: ${errs[0]} (fix it in the home team first)` }
    if (htj.team !== home) return { why: `${hrel}/team.json says team ${pyRepr(htj.team)}, not ${pyRepr(home)}: home must be the home team's folder name and that folder's team.json its own` }
    return { htj }
  }
  // the fix for a missing guest folder names --root when the team folders are not under product/ (new_team.py's default)
  const rootOpt = teamsRoot(rel) === 'product' ? '' : ` --root ${teamsRoot(rel)}`
  for (const { slug, home } of entries) {
    const hrel = homeRel(rel, home)
    if (!homes.has(home)) homes.set(home, homeTeam(home, hrel))
    const { htj, why } = homes.get(home)
    if (!htj) { errors.push(`guest ${slug}: ${why}`); continue }
    const listed = htj.members.filter(m => m && typeof m === 'object' && !Array.isArray(m))
    const entry = listed.find(m => m.slug === slug)
    if (!entry) {
      const g2 = (Array.isArray(htj.guests) ? htj.guests : []).find(x => x && typeof x === 'object' && !Array.isArray(x) && x.slug === slug)
      const names = listed.map(m => pyStr(m.slug))
      // the likeliest cause: the home team's branch that adds this member is not merged into this branch yet (playbook §三,
      // the T0 row), so the merge comes first, then slug / home. A slug that differs from a home member's only in letter
      // case (slugs are case-sensitive; guests are written by hand) asks for that member instead, as new_team.py does:
      // every member is searched, not only the 8 listed, and the first match in team.json order wins
      const near = names.find(s => s.toLowerCase() === slug.toLowerCase())
      errors.push(g2
        ? `guest ${slug}: ${home} seats ${slug} as its own guest; a guest of a guest is not allowed; seat it from its home team ${pyStr(g2.home)}`
        : `guest ${slug}: not a member of ${home} (${hrel}/team.json lists ${names.slice(0, 8).join(', ')}${names.length > 8 ? ' …' : ''}): ` + (near !== undefined
          ? `did you mean ${near}? (slugs are case-sensitive)`
          : `if the home team's branch that adds ${slug} is not merged here yet, merge it first (playbook §八, 加一位客座成员 step 2); otherwise check slug and home, or add ${slug} to the members of ${home} first (step 1)`))
      continue
    }
    const dir = path.join(repo, hrel, slug)
    if (!isDir(dir)) { errors.push(`guest ${slug}: ${hrel}/${slug}/ missing; scaffold it in the home team first: python3 scripts/new_team.py ${hrel}/team.json --add-member ${slug}${rootOpt}`); continue }
    const shadowRel = path.posix.join(tp, slug)
    let shadow = false
    try { fs.lstatSync(path.join(repo, shadowRel)); shadow = true } catch { shadow = false }   // a dangling link counts too
    if (shadow) { errors.push(`guest ${slug}: ${shadowRel} exists in this team: a shadow copy the roundtable would load instead of ${hrel}/${slug}/; remove it (one skill per person, kept in its home team)`); continue }
    if (!isFile(path.join(dir, 'SKILL.md'))) {
      // new_team.resolve_guests' note; once the home team's T1 has started (research notes) or without references/research/,
      // check_links.py counts this team's README link to the guest's SKILL.md as broken, not pending
      const research = path.join(dir, 'references', 'research')
      const hasResearch = isDir(research)
      notes.push(`guest ${slug}: no SKILL.md yet (the home team's T1)` + (!hasResearch || hasResearchNotes(research)
        ? `; ${hrel}/${slug}/ ${hasResearch ? 'already has research notes' : 'has no references/research/'}, so check_links.py counts this team's README link to ../${home}/${slug}/SKILL.md as broken (not pending) until the home team's T1 writes SKILL.md: merge the home team's branch after its T1, or expect the T0 gate (check_links.py) to fail on that link until then`
        : ''))
    }
    guests.push({ ...entry, home, dir: path.posix.join(hrel, slug) })
  }
  if (errors.length) {
    const e = new Error(errors.join('\n'))
    e.lines = errors
    throw e
  }
  return { guests, notes }
}

export function defaultScratch(teamName) { return path.join(process.env.TMPDIR || os.tmpdir(), `${teamName}-scratch`) }

// per-member map args whose keys are not slugs of the given members: [{key, unknown: [...]}]
export function mapProblems(args, slugs) {
  const out = []
  for (const k of MAP_ARGS) {
    const v = args && args[k]
    if (!v || typeof v !== 'object' || Array.isArray(v)) continue
    const unknown = Object.keys(v).filter(s => !slugs.includes(s))
    if (unknown.length) out.push({ key: k, unknown })
  }
  return out
}

function parseValue(v) { try { return JSON.parse(v) } catch { return v } }

export function buildCalls(o) {
  const repo = path.resolve(o.repo || DEFAULT_REPO)
  const wf = workflowPath(o.workflow, repo)
  if (!fs.existsSync(wf)) throw new Error(`no workflow ${wf}`)
  const name = workflowName(wf)
  const { keys, aliases } = knownArgs(fs.readFileSync(wf, 'utf8'))
  const { rel, tj, name: teamName } = loadTeam(repo, o.team)
  const all = tj.members
  const guestList = guestEntries(tj, rel)
  let members = all
  if (o.member && o.member.length) {
    const asGuest = guestList.find(g => o.member.includes(g.slug))
    if (asGuest) throw new Error(guestMemberError(rel, asGuest))
    const unknown = o.member.filter(s => !all.some(m => m.slug === s))
    if (unknown.length) throw new Error(`--member: not in ${rel}/team.json: ${unknown.join(', ')}`)
    if (TEAM_LEVEL.has(name)) throw new Error(`${name} is team-level: it runs with ALL members of team.json${guestList.length ? ' and its guests' : ''} (drop --member)`)
    members = all.filter(m => o.member.includes(m.slug))
  }
  const extra = {}
  for (const kv of o.set || []) {
    const i = kv.indexOf('=')
    if (i < 1) throw new Error(`--set ${kv}: use KEY=VALUE`)
    const k = kv.slice(0, i)
    if (['repo', 'team', 'scratch', 'date', 'members', 'request'].includes(k)) throw new Error(`--set ${k}: use --${k === 'members' ? 'member' : k} instead`)
    if (k === 'guests') throw new Error('--set guests: set guests in team.json')
    if (keys.length && !keys.includes(k) && !aliases.includes(k)) throw new Error(`--set ${k}: ${name} does not read this key; it reads ${keys.join(', ')}`)
    extra[k] = parseValue(kv.slice(i + 1))
  }
  const probs = mapProblems(extra, members.map(m => m.slug))
  if (probs.length) throw new Error(probs.map(p => `--set ${p.key}: key(s) ${p.unknown.join(', ')} are not members of this run (${members.map(m => m.slug).join(', ')})`).join('; '))
  const date = o.date || today()
  if (!/^\d{4}-\d{2}-\d{2}$/.test(date)) throw new Error('--date must be YYYY-MM-DD')
  const scratch = path.resolve(o.scratch || defaultScratch(teamName))
  const request = typeof o.request === 'string' ? o.request.trim() : ''
  const base = { repo, team: rel, scratch, date, ...(request ? { request } : {}) }
  // team-layer names the roundtable folder in its prompts; give it team.json's so the agents see the real path
  if (keys.includes('roundtable') && tj.roundtable && !('roundtable' in extra)) base.roundtable = tj.roundtable
  // the team-level workflows seat the guests (resolved in their home teams); per-member workflows never get them
  const { guests, notes } = TEAM_LEVEL.has(name) && guestList.length ? resolveGuests(repo, rel, tj) : { guests: [], notes: [] }
  const groups = TEAM_LEVEL.has(name) || o.together ? [members] : members.map(m => [m])
  const calls = groups.map(ms => {
    const slugs = ms.map(m => m.slug)
    const own = Object.fromEntries(Object.entries(extra).map(([k, v]) => [k,
      MAP_ARGS.includes(k) && v && typeof v === 'object' && !Array.isArray(v)
        ? Object.fromEntries(Object.entries(v).filter(([s]) => slugs.includes(s))) : v])
      .filter(([k, v]) => !(MAP_ARGS.includes(k) && v && typeof v === 'object' && !Array.isArray(v) && !Object.keys(v).length)))
    const { roundtable, ...rest } = base
    return { scriptPath: wf, args: { ...rest, members: ms, ...(guests.length ? { guests } : {}), ...(roundtable ? { roundtable } : {}), ...own } }
  })
  return { name, calls, scratch, teamLevel: TEAM_LEVEL.has(name), guests, notes }
}

function usage(code) {
  const lines = fs.readFileSync(fileURLToPath(import.meta.url), 'utf8').split('\n').slice(1)
  const end = lines.findIndex(l => !l.startsWith('//'))
  console.log(lines.slice(0, end).map(l => l.replace(/^\/\/ ?/, '')).join('\n'))
  process.exit(code)
}

function main() {
  const argv = process.argv.slice(2)
  const o = { set: [] }
  const pos = []
  for (let i = 0; i < argv.length; i++) {
    const a = argv[i]
    const val = () => { if (i + 1 >= argv.length) { console.error(`${a} needs a value`); process.exit(1) } return argv[++i] }
    if (a === '-h' || a === '--help') usage(0)
    else if (a === '--team') o.team = val()
    else if (a === '--date') o.date = val()
    else if (a === '--member') o.member = val().split(',').map(s => s.trim()).filter(Boolean)
    else if (a === '--scratch') o.scratch = val()
    else if (a === '--repo') o.repo = val()
    else if (a === '--request') o.request = val()
    else if (a === '--set') o.set.push(val())
    else if (a === '--together') o.together = true
    else if (a === '--args-only') o.argsOnly = true
    else if (a === '--out') o.out = val()
    else if (a.startsWith('--')) { console.error(`unknown option ${a}`); usage(1) }
    else pos.push(a)
  }
  if (pos.length !== 1 || !o.team) usage(1)
  o.workflow = pos[0]
  let r
  try { r = buildCalls(o) } catch (e) { for (const l of e.lines || [e.message]) console.error(`make_args: ${l}`); process.exit(1) }
  if (o.argsOnly && r.calls.length !== 1) { console.error(`make_args: --args-only needs exactly one call (got ${r.calls.length}); add --member <slug> or --together`); process.exit(1) }
  try { fs.mkdirSync(r.scratch, { recursive: true }) } catch (e) { console.error(`make_args: cannot create scratch ${r.scratch}: ${e.message}`); process.exit(1) }
  if (o.out) {
    fs.mkdirSync(o.out, { recursive: true })
    for (const c of r.calls) {
      const who = r.teamLevel || c.args.members.length > 1 ? 'team' : c.args.members[0].slug
      fs.writeFileSync(path.join(o.out, `${r.name}.${who}.args.json`), JSON.stringify(c.args, null, 1) + '\n')
    }
  }
  console.log(JSON.stringify(o.argsOnly ? r.calls[0].args : r.calls, null, 1))
  if (!(o.request || '').trim()) console.error('make_args: note: no --request; pass the user\'s request in their own words (--request "…") so every agent prompt opens with it (agents otherwise see only the user\'s latest message)')
  // guests without a SKILL.md: not an error (the workflow leaves a seat without a skill out), but say so
  for (const n of r.notes) console.error(`make_args: note: ${n}`)
  const teamLevel = r.guests.length ? ` (team-level: all members and ${r.guests.length} guest(s): ${r.guests.map(g => `${g.slug} from ${g.home}`).join(', ')})` : ' (team-level: all members)'
  if (!o.argsOnly) console.error(`${r.calls.length} ${r.name} call(s)${r.teamLevel ? teamLevel : r.calls.length > 1 ? ', one per member: launch them in one message' : ''}; scratch ${r.scratch}`)
}

if (process.argv[1] && import.meta.url === pathToFileURL(path.resolve(process.argv[1])).href) main()

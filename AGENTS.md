# AGENTS.md — Vijay Transit (Rahu–Ketu Gochara Report)

> **Rule-ID glossary**: master table lives in `rule-engine/RULES.md` → GLOSSARY;
> every other `.md` carries only the subset of prefixes it uses, with a pointer back.

## What this project is
A Vedic astrology (Jyotisha) project to build a **domain-specific Rahu–Ketu transit (gochara)
report generator**. The user asks "how is this Rahu–Ketu transit for me in terms of
career / money / health / marriage & relationships / foreign travel?" and receives a curated report.
Inputs: user's natal chart details (variable), the node transit window (shared, cacheable),
and the domain(s) of interest. The interpretation engine IS the project.

**Architecture: compute once, interpret per-lens.** Core engine (factors A–E) produces a
domain-agnostic fact table; a per-domain **lens config** (primary/secondary/affliction houses,
karakas, watched contacts, dasha amplifiers, axis templates, weights) selects and re-weights
facts into the curated verdict. Adding a domain = adding a config, never touching the engine.

## Working style (Machan's — respect always)
- **Logic first, code second.** Arrive at the astrological logic by discussion before implementing.
- Phase-by-phase: discuss → decide → implement → validate, one phase at a time.
- Keep `MEMORY.md` (this folder) current in the moment — decisions, gotchas, open threads.
- Project memory lives HERE, never in the central `~/MEMORY.md`.
- Address the user as **Machan**.
- **Every rule, decision point, or question MUST come with a worked real-time example** (preferably from the sample natal chart) — Machan answers from practice, not abstraction.

## Locked decisions
| Decision | Verdict |
|---|---|
| Node type | Compute **both** mean & true node; **report mean** (Parashari/panchanga convention) |
| Ayanamsha | **Lahiri** (Chitrapaksha), sidereal zodiac |
| Transit scope | **Full sign-transit window (~18 months)** with dated sub-periods, not a snapshot |
| Output artifact | **Styled, self-contained HTML** report |
| Core framing | **Axis-first**: Rahu–Ketu = one axis transiting a house pair (1/7, 2/8, ... 6/12) |
| Verdict style | Qualitative bands (Favorable / Mixed / Challenging / Volatile) **with stated reasons** — no fake numeric precision |
| Runtime AI/LLM | **NONE.** 100% deterministic: precomputed knowledge libraries + rule engine + template stitching. Same inputs → byte-identical report. All interpretive prose is authored upfront in the KB |
| Methodology mix | **~80% parambariya Parashara Hora, ~20% KP.** KP kept only where Machan practices it: the nakshatra star-lord signification chain (SIGN-02/03). KP sub-lord gate → v2. Verdict gates run the parambariyam way: kelvikkaana bavagangal × DBAS × transit (GATE-01) |

## v1 interpretation factors (approved set: A+B+C+D+E)
- **A. Axis house placement** — from Janma Rashi (Moon) PRIMARY, from Lagna SECONDARY.
  Rahu favorable in 3/6/10/11; Ketu favorable in 3/6/11.
- **B. Natal-planet contacts** — transit node conjunctions to natal grahas
  (**ORB-02 asymmetric curve**: influence rises from 3° applying, peaks at exact crossing,
  fully releases 2.5° past; ≈57d rise + ≈47d fade, ~104d window); **Rahu return** (~18.6y)
  & **half-return** (~9.3y). Node aspects (5/7/9) = toggle, OFF by default.
- **C. Dispositor condition** — node acts through its sign lord; ruler dignity
  (own/exalted/debilitated/moolatrikona) + dispositor's house from Moon/Lagna, both charts.
- **D. Nakshatra sub-periods** — ~40–41 days per nakshatra within the sign transit;
  nakshatra-lord flavor; Rahu-lorded (Ardra/Swati/Shatabhisha) & Ketu-lorded (Ashwini/Magha/Moola) intensify.
- **E. Dasha amplifier** — Vimshottari MD/AD from natal Moon degree; Rahu/Ketu dasha or
  antardasha during the transit amplifies everything.

## Explicitly excluded from v1 (with reason)
- **F. Ashtakavarga bindus** — deferred to v2 (real computation chunk, not load-bearing).
- **G. Vedha (obstruction)** — thin classical support for nodes (only via "Rahu ≈ Saturn" mapping);
  documented as considered-and-excluded.
- **H. Node exaltation/debilitation** — schools disagree (Taurus/Gemini/Scorpio); commentary only, never scored.

## Conventions
- Sidereal longitudes everywhere; house = whole-sign from reference point.
- Rahu = mean north node for reporting; Ketu = Rahu + 180°.
- Verdict engine: BASE (axis house effect) → MODIFIERS (dispositor, nakshatra lord) →
  AMPLIFIER (dasha) → EVENTS (dated contact list) → per-sub-period band + reasons + dated peaks.
- **`CHANGELOG.md` = the project's consolidated change record** (established 2026-10-31).
  Every session/file/decision lands there with date-time + heading; all ⛔ blockers are
  gate-kept in its `GK-xx` registry with a named owner (Machan / Panduranga / Claude) —
  parked, never silently dropped. Update it in the moment, alongside `MEMORY.md`.
- **`foundations/` = the general-purpose knowledge base** (renamed from `kb/`, 2026-10-30).
  Standard: **encyclopedic and ultra-deep** — e.g., target **~200 karakatvas per graha**,
  exhaustive good/bad character banks. Written ONCE as a general set, reusable by any future
  module (not just this transit product). Every file: source line, status
  (DRAFT → REVIEWED → LOCKED), consumed-by rule list.
- **Build order change (2026-10-30)**: the **questions→bhavas catalog comes FIRST**, before
  the encyclopedia files — every askable question mapped to its supporting bhavas
  (kelvikkaana bavagangal), per Machan.

## Directory structure (as built 2026-10-31)
- `foundations/` — Tier-0 encyclopedic KB (chart-agnostic facts; 9 files, DRAFT pending GK-11).
- `rule-engine/` — locked logic: RULES.md (all cards), REPORT-FLOW.md (M1), REPORT-TEMPLATE.md (M2).
- `generative/` — Tier 1–3 print-ready prose banks. **JSON is the single source of truth**
  (`phrases.json`, `profile.json`, `<domain>.json`); `.md` files document structure only.
  Fragments keyed (`FRAME.*`, `BRIDGE.*`, `REASON.*`, `CAUTION.*`, `EVENT.*`, `ANSWER.*`).
  Engine fails closed on a missing key — it never prints an un-authored sentence.
- `engine/` — Python 3.9 stdlib-only package `vijay_transit` (SecOS-11 banner/docstring style):
  constants → models → ephemeris → vimshottari → factsheet → lenses → verdict →
  library → stitcher → report → render_html → cli. Data in `engine/data/`
  (charts/, transits/, lenses/, functional_nature.json). Tests in `engine/tests/`.
- `report-shell/default.css` — inlined into the self-contained HTML report.
- `validation/` — generated answer-key reports (currently sample_career_report.html).

## Engine doctrine (locked 2026-10-31)
- No AI/LLM at runtime: pure rule matching → fragment-key selection → blueprint stitching.
- Same inputs ⇒ byte-identical report (tested double-run gate).
- Run: `cd engine && PYTHONPATH=. python3 -m vijay_transit --chart <chart.json>
  --transit <transit.json> --domain <domain> --out <report.html>`
- Test: `cd engine && PYTHONPATH=. python3 -m unittest discover -s tests -v`

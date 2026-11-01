# MEMORY.md — Vijay Transit (project-local memory)

> This project's memory. Central ~/MEMORY.md is intentionally NOT used for this project.
> Rule-ID glossary: master table in `rule-engine/RULES.md` → GLOSSARY; per-file subsets
> at the top of each `.md`.

## 2026-10-30 — Project founded
- Folder created: `/Users/sujans/Desktop/vijay transit` (working directory).
- Goal: Rahu–Ketu transit (gochara) report for a natal horoscope — **logic-first**: discuss and
  arrive at the interpretation logic, then build. Output: styled HTML report.
- Assets available: natal chart WITH exact planet degrees + transit chart (ephemeris not needed).
- **Decisions locked** (see AGENTS.md for the full table):
  - Compute both mean & true nodes, report MEAN. Lahiri ayanamsha.
  - Full 18-month sign-transit window with dated sub-periods (not a snapshot).
  - v1 factor set = A (axis houses from Moon+Lagna) + B (natal conjunctions, orbs 3°/5°, Rahu
    return/half-return) + C (dispositor condition) + D (nakshatra sub-periods) + E (Vimshottari
    dasha amplifier). Deferred: F Ashtakavarga (v2). Excluded: G Vedha (thin classical basis),
    H node exaltation debates (commentary only).
  - Axis-first framing; qualitative bands with reasons, no fake numeric scores.
- **Open / next**: receive the actual natal + transit chart data (degrees), then design the
  logic document (per-factor computation + verdict engine), then the HTML report generator.
- Birth details of the native: NOT yet shared in this session.

## 2026-10-30 — Both sample PDFs fully read (natal 82pp, transit 31pp)
- Native: female, 1992-03-02 22:23 Dindigul. Lagna Thulam 17°51'; Moon Makaram 28°12' (Avittam p2).
  4-planet stellium in Makaram (Mars 16°43' ucha / Saturn 19°23' own / Venus 22°23' / Moon).
  Natal Rahu Dhanus 12°53' (Moolam p4), Ketu Mithunam 12°53' (Ardra p2).
- Vimshottari: Jupiter MD →2030-08-10; Moon Bhukti →2027-04-11 (current);
  **Rahu Bhukti 2028-03-17→2030-08-10** = factor-E amplifier inside the transit window.
- Transit event: Rahu enters Makaram ≈ 2026-12-07 (ingress chart, KP New) → axis 4/10 from Lagna,
  1/7 from Moon; Rahu will conjunct the whole Makaram stellium within the window.
- ⚠️ **Ayanamsha mismatch still OPEN**: natal PDF = KP Old 23°39'03", transit PDF = KP New 24°08'34".
  AGENTS.md says "Lahiri" — needs correction once Machan picks. Recommendation given: compute in KP Old.
- Style reference for our report: PDFs use band labels (Very Positive/Challenging/Samam),
  period-flow cards (Dasha→Bhukti→Antara narrowing), ToL chains, KP signification tables.

## 2026-10-30 — Product reframe + no-AI decision
- **Reframe (Machan)**: this is a report GENERATOR product, not a one-off. User supplies natal
  details + picks domain(s): career / money / health / marriage & relationships / foreign travel.
- **Architecture agreed**: compute once (domain-agnostic fact table from factors A–E) →
  domain LENS config selects/re-weights → verdict bands + cited reasons → stitched HTML.
  Lens config = {primary/secondary/affliction houses, karakas, watched contacts, dasha
  amplifiers, axis templates, weights}. New domain = new config only.
- KB inventory needed: graha/bhava/nakshatra significations + Rahu-Ketu-specific significations,
  domain→house map, domain→karaka map (gender-conditional: Venus male / Jupiter female chart),
  axis-pair×domain templates (~36), node-in-sign flavors (24), contact-event templates.
- 🔒 **LOCKED: no AI/LLM at runtime.** 100% deterministic: precomputed libraries + rule logic +
  template stitching. Same inputs → byte-identical report. Recorded in AGENTS.md.
- **7 decisions pending Machan**: (1) final domain list (add education/property/children/
  spirituality?) (2) one domain per report vs overview+deep-dive (3) input contract: birth data
  vs precomputed positions (4) language: Tamil/English/both (5) remedies appendix y/n
  (6) gender-conditional karakas confirm (7) KP layer in v2 (recommended).

## 2026-10-30 — LISA module introduced + first rule dump
- **LISA** = Lagna Influence & Signification Analysis — Machan's name for the natal
  capability engine: (1) functional nature by lagna lordship, (2) signification-based delivery,
  (3) influence modification by natural benefic/malefic aspects/conjunctions.
- I raised 8 design decisions (D1–D8): multi-tag classification (tier + MARAKA/BADHAKA/
  KENDRADHIPATI tags), canonical 12×9 functional table as data not runtime rules, nodes get no
  tier (absorb via dispositor+star lord+conjunction = "agent" model), Parashari signification v1
  with KP-pluggable interface, ADD 4th dimension = delivery capacity/strength, baseline result =
  structured set never scalar (domain lens does weighting), influence modifiers record both
  natures + cite source by name, Moon/Mercury natural nature is chart-conditional.
  Awaiting Machan's calls.
- **Rule dump #1 (Machan, pro jyotish axioms)** — to formalize into rule register:
  1. Planet delivers FIRST the house it occupies.
  2. THEN the house its star (nakshatra) lord occupies. (KP chain flavor)
  3. Kendras 1/4/7/10 deliver MATERIAL things & status — "what wouldn't fill the heart";
     kendra gives more money than trikona.
  4. Trikonas 1/5/9 deliver MEANING/fulfillment — "what fills the heart."
  5. Dispositor ("house giver") modulates tenant strength: strong tenant + debilitated
     dispositor = reduced delivery; debilitated tenant + exalted/own dispositor =
     NEECHA BHANGA RAJA YOGA. (His example: exalted Mars in Capricorn serves less if
     Saturn debilitated in Mesha.)
- Method agreed: Machan dumps rules in batches → I formalize into rule cards (ID, statement,
  inputs, effect, priority, examples, status) → discuss → lock → write rule-engine .md.
- **Working preference (locked in AGENTS.md)**: every rule/question must carry a worked
  real-time example, preferably from the sample chart.
- Worked-example facts derived for Q&A (KP Old, sample chart): Jupiter sub-lord = Sun
  (Pooram: Venus sub 13°20'–15°33'20", Sun sub →16°13'20"; Ju at 15°40' Simha).
  Mercury sub-lord = Saturn (U.Bhadrapada Saturn sub 3°20'–5°26'40" Meena; Merc at 4°25').
  Neecha-bhanga check for natal Mercury (debilitated Meena, 6th): simplified rule (dispositor
  Jupiter exalted/own) = NO (Ju in Simha friend-sign R); classical rule (Venus — planet exalted
  in Meena — in kendra from Lagna) = YES (Venus in 4th). **Chart flips on this decision.**

## 2026-10-30 — Q1 RESOLVED: signification chain locked (with Machan's refinements)
- 🔒 Ranks: 1 = own occupancy (100%) → 2 = star-lord's occupancy (100%) → 3 = star-lord's
  owned houses → 4 = own owned houses.
- 🔒 **SIGN-04 tenant-suppression**: ownership-based delivery = 100% if house empty, **30% if
  tenanted** (occupant beats landlord). Live example: Jupiter's owned 3rd (Rahu tenants) & 6th
  (Mercury tenants) deliver at 30% only. OPEN micro-confirm: does SIGN-04 also apply to rank 3
  (star-lord's owned houses)? I assumed yes.
- 🔒 **SIGN-05 aspect rule**: aspects NEVER deliver events directly. They (a) suppress
  negativity, (b) boost positivity, (c) give motivation toward that house. EVENT SUPPORT only
  if BOTH: aspected cusp ∈ asked-domain's house set AND running DBAS lords signify that cusp.
  Else = motivation only. ("Will things happen? Only if cusp is part of ascendant-based
  question logic AND cusp-related DBAS signification is running." — Machan)
- Jupiter fully computed through the chain as reference example (11th @100, 4th @100,
  1st/8th @100 via Venus ownership-empty, 3rd/6th @30, aspects on 3/5/7 = modifiers).
- Machan directive: build the engine strictly as if/else/then/loop condition rules;
  proceed Q by Q (Q2 sub-lord gate next, then Q3 neecha-bhanga, Q4 purushartha, Q5 penalty).

## 2026-10-30 — Q2 resolved the parambariyam way; RULES.md founded
- SIGN-04 rank-3 generalization: **agreed** (tenant suppression applies to star-lord-owned too).
- 🔒 **Methodology mix: 80% parambariya Parashara Hora / 20% KP.** KP kept only for the
  star-lord signification chain. Sub-lord gate → v2 backlog.
- 🔒 **GATE-01 kelvikkaana bavagangal gate**: every question has native bhavas (career =
  2,6,10; +11 = profits; +3 = consulting/micro-travel; +7 = offshore money/partnership/wife).
  Verdict = DBAS support × transit support over those bhavas: both fail → NEGATIVE; one →
  MIXED; both → POSITIVE.
- 🔒 **DIGN-01 dignity = status visibility (thagudhi)**: exalted = thagudhi uyarvaana
  (boast-worthy, open status); debilitated = thagudhi kuraindha (unboastable). INDEPENDENT
  axis from event manifestation — event can land via gate while carrying no prestige.
- Created `rule-engine/RULES.md` with locked cards: SIGN-01..05, GATE-01, DIGN-01 + domain
  lens seed table. Pending: STRENGTH-01/NBR (Q3), BHAVA-01/02 (Q4), penalty magnitude (Q5).

## 2026-10-30 — Q3 RESOLVED: Neecha Bhanga = chain-rescue, Machan's hierarchy
- Machan's empirical read of the sample Mercury: **struggle → then elevation** (confirmed real).
- His attribution: **Saturn** (yogakaraka + 5th-lord trikonadhipati) rescues via
  (a) nakshatra saara (Mercury in U.Bhadrapada = Saturn star) and (b) Saturn's 3rd special
  aspect from Makaram onto Mercury in Meenam. Mechanics verified — both true in the chart.
- 🔒 **NBR-01 hierarchy**: c1 dispositor exalted/own = full bhanga → c2 star-lord is
  yogakaraka/trikonadhipati + strong = CHAIN-RESCUE (early struggle → later elevation, delivered
  through star-lord's portfolio) → c3 classical kendra conditions (Venus rule) = **30% weight
  only, never the gate**. Rescuer aspecting the debilitated planet = negativity suppressed
  (SIGN-05 interaction).
- 🔒 **QUAL-01 nakshatra saara**: star lord injects its functional tier/dignity into the
  tenant's delivery QUALITY — a third axis separate from which-houses (SIGN) and how-much
  (SIGN-04).
- Noted wrinkle for engine: chain dedupes per house, max-strength route wins (e.g., Mercury
  gets 4th @100 via rank-2 occupancy even though rank-3 ownership route would be 30% since
  the 4th is tenanted; Saturn-owned 5th is Sun-tenanted → 5th @30 via rank 3).

## 2026-10-30 — Q4 RESOLVED: option (b) — purushartha underlayer added
- 🔒 BHAVA-01 kendra = material/status (more money magnitude); BHAVA-02 trikona = heart/meaning;
  1st house dual-textured (kendra+trikona).
- 🔒 BHAVA-03 purushartha fixed tags: dharma 1/5/9, artha 2/6/10, kama 3/7/11, moksha 4/8/12.
  Resolves the 4th-house tension (kendra BUT moksha → material gains + inner-peace disturbance
  read together). Zero runtime cost.
- Remaining open from the founding set: **Q5 penalty magnitude only.**

## 2026-10-30 — Q5 RESOLVED + NBR-02 filed (uyir→porul exchange)
- 🔒 **Q5 = (a)**: strong tenant + debilitated dispositor → drop ONE tier (Strong→Moderate).
  Partial suppression, never annihilation (consistent with SIGN-04's 30% style).
- 🔒 **NBR-02 (Machan's rule)**: on FULL bhanga (NBR-01 c1, incl. parivartana), keyed on
  FUNCTIONAL nature: benefic-to-lagna → candidate renounces one UYIR karakatva (living),
  receives PORUL karakatva (material) as replacement; malefic-to-lagna → debility cuts the
  harm itself, rescue delivers super-good results, no cost. Principle: debility incapacitates
  the functional portfolio — benefic pays in living significations, malefic loses its poison.
  Functional-over-natural demonstrated: Saturn (natural malefic, Thulam yogakaraka) → benefic
  branch. Machan called the parivartana double-rescue catch "amazing."
- Pending micro-confirms: (i) functional-not-natural keying (implicit, needs explicit yes);
  (ii) parivartana: does exalted Mars deliver FULL once landlord Saturn is exchange-rescued
  (penalty unwinds)? my lean yes — penalty tracks resolved condition; (iii) NBR-02 fires on
  c1/exchange only, or also c2 chain-rescue? my lean c1 only.
- **New KB dependency**: uyir (living) vs porul (material) karakatva split table for all 9
  grahas — draft prepared, awaiting Machan's corrections from practice.

## 2026-10-30 — Micro-confirms resolved; FUNC-01, PARI-01, REPORT-01 filed
- 🔒 **FUNC-01** (Machan): functional nature (lagna subar) decides whether delivery is GOOD;
  natural nature survives as STYLE (Saturn: slow and steady); natural harmful traits (theft,
  cruel mindset) are suppressed for functional benefics, live for functional malefics.
- 🔒 **PARI-01**: parivartana does NOT work in dasa-bhukti — "don't really bother." Works only
  in gochara, and only when transit planets travel on top of the parivartana'd cusps (then
  both houses' matters exchange-fire for that window). Dissolves the penalty-unwind question:
  no pair pass in DBAS; plain rules apply (Mars keeps STRENGTH-01 penalty; Saturn separately
  gets c1 bhanga from its exalted dispositor).
- 🔒 **NBR-02 scope = c1 + c2** (chain-rescue also carries the exchange). Big payoff: real-chart
  Mercury = 9th lord (trikonadhipati) = functional benefic → EXCHANGE branch applies to the
  actual native's struggle→elevation.
- 🔒 **Which uyir karakatva: NOT hard-predicted** — depends on the question asked; if the
  asked domain's signifying bhavas intersect the rescued planet's chain, report steers focus
  to porul karakatva. Subtle faculties (atma/manas/ayus/speech) not hard-coded as cost items.
- 🔒 **REPORT-01 tone rule**: boost positive possibilities (~80%); negatives only ~20%, always
  probabilistic — "irukkalaam, nadakkalaam, gavanam" — never deterministic doom. Goal: the
  candidate leaves feeling good and oriented.
- Founding rule set now COMPLETE: SIGN-01..05, FUNC-01, GATE-01, DIGN-01, BHAVA-01..03,
  STRENGTH-01, NBR-01, NBR-02, QUAL-01, PARI-01, REPORT-01. Next module: contact rules
  (factor B — transit node × natal graha; Dec 2026 Rahu-onto-Makaram-stellium showcase).

## 2026-10-30 — KB standard set + reprioritized: questions catalog FIRST
- KB folder named **`foundations/`** (Machan's pick): general-purpose, used for everything.
- 🔒 **Encyclopedia standard**: every foundations file is ULTRA-DEEP and general — e.g.,
  ~200 karakatvas per graha, exhaustive good/bad character banks. General set, not
  product-specific. (Recorded in AGENTS.md conventions.)
- 🔒 **Reorder (Machan)**: before the encyclopedia files, build the **questions→supporting
  bhavas catalog FIRST** (what all questions can be asked + their kelvikkaana bavagangal).
  Engine consequence: GATE-01 resolves per-QUESTION (core + modifier + viruddha bhavas),
  not just per-domain.

## 2026-10-31 — foundations/grahas.md COMPLETE + audited + fixed
- All 9 graha entries written to the encyclopedic standard (identity, nature/FUNC-01,
  texture, good/bad banks, ≥200 numbered karakatvas, kelvigal-domain-specific layers,
  dignity map, aspects, worked example on the sample chart).
- Machan-mandated parallel-agent audit run against kelvigal.md + RULES.md + sample chart.
  Verdict: FIXABLE ISSUES — all applied same day:
  - Ketu example: transit Ketu corrected to Katakam/10th (was Simmam/11th — nodes must be
    180° apart).
  - Sun example: FUNC-01 branch corrected — 11th-lord (trishadaya) Sun = functional
    malefic/neutral; suppression does NOT fire; the 5th trikona occupancy is what softens.
  - Moon example: chain attribution fixed ({2,7} star-lord Mars + 10th own lordship);
    POSITIVE scope limited to 2/4/7/10-anchored cards (C/M/R/H5); F-cards wait for Rahu
    bhukti from 2028-03-17.
  - 18 kelvigal mapping gaps closed across Moon/Jupiter/Venus/Saturn/Rahu.
  - Saturn disease bank backfilled to 210 items; Rahu #87–89 recategorized to abstract;
    "(honesty)" tags clarified.
- Footer of grahas.md logs all fixes + pending items (Moolam pada ruling, editorial
  near-duplicates list, school-note tags, gender-conditional karaka `*`).

## 2026-10-31 — foundations/nakshatras.md COMPLETE (27/27)
- All 27 stars written to the per-star template: data line (span/lord+dasha-yrs/deity/
  symbol/gana/yoni/nadi/motivation/7-fold nature) → texture → good/bad banks → ~24
  numbered karakatvas → pada map (navamsa + flavor) → transit note (factor D) → dasha
  note (factor E) → worked example for sample-chart stars.
- Pada navamsas re-verified against the standard rule; all sample-chart padas match
  (Avittam p2 Kanni, Sadayam p4 Meenam, U.Bhadrapada p1 Simmam, Shravana p4 Katakam,
  Ardra p2 Makaram, Pooram p1 Simmam).
- Worked examples written for ALL 9 sample-chart placements: Ardra (Ketu), Pooram
  (Jupiter R), Moolam (Rahu — pada discrepancy escalated), Thiruvonam (Mars p3/Saturn p3/
  Venus p4 — the load-bearing 3-graha star), Avittam (Moon p2 — transit Rahu's FIRST
  natal contact 28°12'), Sadayam (Sun p4 — receives the transit Ketu contact),
  Uthirattathi (Mercury p1 — NBR-02 exchange noted).
- Transit-sequence facts encoded in the examples: retrograde contact order in Makaram =
  Moon 28°12' → Venus 22°23' → Saturn 19°23' → Mars 16°43'; Thiruvonam carries the
  densest dated-contact cluster; Avittam spans the Makaram–Kumbam border (factor-D
  sub-period date math must split at the sign border — flagged in-file).
- Karakatva standard for stars = ~24/star (depth lives in grahas.md; stars carry only
  differentiators). If Machan wants star lists expanded, offer recorded in footer.
- **Wave 1 remaining: `foundations/rasis.md` (12 rasis) — the last wave-1 file.**
- Both grahas.md + nakshatras.md now at DRAFT awaiting Machan's line-by-line corrections.

## 2026-10-31 — foundations/rasis.md COMPLETE → WAVE 1 DONE
- All 12 rasis written: data line (lord/element/quality/purushartha/gender/varna/
  kala-purusha body zone/rising type/direction) → texture → good/bad banks → ~24
  numbered karakatvas → dignity & lordship map (owner, exaltation/debilitation deep
  points, moolatrikona ranges, friend/enemy comfort) → transit note (factor A/C
  flavor) → worked example.
- Worked examples for all 8 covered sample-chart rasis: Thulam (lagna — Venus→Saturn
  dispositor chain at max grade), Makaram (THE showcase — stellium + double
  mahapurusha + contact order Moon→Venus→Saturn→Mars + transit Rahu dispositor =
  own-sign Saturn), Dhanus (natal Rahu; return-reference degree 12°53'), Mithunam
  (natal Ketu; factor C weak dispositor), Katakam (transit Ketu's 10th-house seat),
  Simmam (Jupiter R vargottama in 11th), Kumbam (Sun in Rahu's star — the 11th→5th
  gains channel that Rahu transit/bhukti activates), Meenam (Mercury debilitation +
  NBR-02 exchange).
- Footer flags: node dignity commentary-only (decision H confirmed in-file); Rahu/Ketu
  co-lordship [school note] (engine uses Saturn/Jupiter only — Machan to confirm);
  enmity *directionality* disputes deferred to functional-nature.md (wave 2);
  Moon MT range [school note].
- **WAVE 1 COMPLETE**: kelvigal.md (50 cards) · grahas.md (9, audited+fixed) ·
  nakshatras.md (27) · rasis.md (12) — all DRAFT awaiting Machan's practice
  corrections.
- **Next (wave 2)**: uyir-porul.md (NBR-02 cost/replacement table) → bhavas.md →
  functional-nature.md (12×9 FUNC-01 matrix) → vimshottari.md (factor E).

## 2026-10-31 (later) — foundations/bhavas.md COMPLETE (wave 2 file 1)

- 12/12 bhavas, 1,248 lines. Template per bhava: data line (Skt/Tamil names, classification
  tags, purushartha, BHAVA texture, body zone, karaka grahas, viruddha) → texture → holds/
  corrupts → grouped numbered karakatvas (People/Places/Matters & events/Body, ~45-56 per
  bhava) → viruddha relation (both directions) → factor-A transit reads (Rahu + Ketu, from
  Moon PRIMARY + from Lagna SECONDARY, locked favorability flags: Rahu ✓ 3/6/10/11, Ketu ✓
  3/6/11) → kelvigal pull (reverse index computed from all 50 cards) → worked example for the
  7 loaded bhavas of the sample chart (3 natal-Rahu, 4 Makaram-stellium showcase, 5 Sun +
  M4 negative-gate illustration, 6 rescued Mercury + NBR-02 maternal-uncle note, 9 natal-Ketu
  + nodes-in-each-other's-stars + F1 MIXED anatomy, 10 Katakam empty + transit-Ketu seat +
  dispositor Moon under Rahu, 11 Jupiter R + MD-era vs bhukti-window layering).
- Global mechanics encoded: classification grid (kendra/trikona/dusthana/upachaya/maraka/
  panaphara/apoklima), the full viruddha cycle (1→12·2→1·…), axis-first pair table (1/7 …
  6/12 with combined meanings), bhavat-bhavam derived-house list (incl. family rotation
  anchors 4 mother / 9 father / 7 spouse / 5 child / 3 younger sibling / 11 elder sibling).
- Key computed findings: 2nd & 10th are the most-pulled bhavas; 6th is the most
  viruddha-watched (partnership dissolver, 11 cards); 9th has the widest modifier footprint
  AND doubles as career's viruddha (context-decided, GATE-01 reads per-question, never
  globally); no card's primary viruddha lands on the 10th; the 9th-doubles-as-viruddha edge
  explicitly documented.
- Open [school note] queue for Machan (mirrored in file footer): 3rd as mild dusthana ·
  2nd's second-marriage-family reading (R8 dependency) · 7th as foreign-residence house ·
  10th as father in day-charts (held: 9 = father) · maraka scope (held: ayus-only).
- Kelvigal-pull lists are computed mirrors — MUST regenerate if Machan edits any card's
  bhava set (engine computes at build time).

## 2026-10-31 (later still) — WAVE 2 COMPLETE (functional-nature.md + uyir-porul.md + vimshottari.md)

- **functional-nature.md (309 lines)**: F-1..F-8 derivation rules (yogakaraka / trikonadhipati /
  kendradhipati dosha / kendra-malefic softening / trishadaya / ashtama with Sun-Moon exemption /
  maraka dormant / moolatrikona-weighted mixing) → full 12-lagna × 7-graha matrix (nodes resolve
  by proxy: dispositor → conjunction → aspect) → all 108 cells derived per-lagna with rule cites →
  Part 4 naisargika friend/enemy matrix WITH DIRECTION (resolves rasis.md's deferral; the four
  asymmetric pairs documented: Mercury→Moon E vs Moon→Mercury F; Saturn→Mars E vs Mars→Saturn N;
  Jupiter→Venus E vs Venus→Jupiter N; Sun→Mercury N vs Mercury→Sun F; engine rule: factor C reads
  dispositor→tenant for landlord willingness, tenant→dispositor for tenant comfort) → Part 5
  sample-chart full functional panel incl. node proxies and the live factor-C cross-read
  (transit Rahu's dispositor = yogakaraka Saturn own-sign = strongest landlord).
  [school note] queue: Kanni Saturn lean · Dhanus Moon N-vs-M · Vrischika/Makara mixed cells.
- **uyir-porul.md (263 lines)**: NBR-02's lookup table. Three-layer split per graha: UYIR
  (living portfolio — persons, ordered by classical weight, each tagged with its bhava) / PORUL
  (material portfolio) / BOUNDARY (native's subtle faculties — atma, manas, speech, jnana, shukra,
  ayus — policy-locked: NEVER hard-coded cost items). Pick mechanic formalized: intersect rescued
  benefic's SIGN-chain ∩ question bhavas → rank uyir hits (core > modifier > viruddha, order
  breaks ties) → mode "steer" (named channel + porul redirect) vs "background" (generic clause).
  Malefic branch = CONVERSION (no cost table — harm was incapacitated at debilitation). Worked
  example: sample Mercury through 5 domains — steer-flag on career (maternal-uncle channel via
  6th occupation), background on money/marriage, porul-steering on foreign (education/documents).
  All five spouse-karaka school notes collapse into decision #6 (still pending).
- **vimshottari.md**: 120y wheel + star-lord table → balance-of-dasha math (sample: Avittam
  fraction 0.635 × Mars 7y ≈ 4y5m10d → Jupiter MD 2014-08-12 → 2030-08-10 ✓) → **consistency
  proof: all three locked bhukti dates (2027-04-11 Moon / 2028-03-17 Mars / 2030-08-10 Rahu-end)
  reproduce from the formula zero-fudging** → 9 MD textures → MD×AD rules R-1..R-6 (functional
  nature, natural relation with node-borrowing, 6/8/12-from-MD-lord friction [school note],
  dual-frame, sandhi 5% handover, node-bhukti amplifier = factor E core) → GATE-01 DBAS-leg
  formal spec (AD chain leads ≥100 bar, MD half-weight backs, flavors from modifiers, viruddha
  leg) → worked era/window anatomy through the transit.
  ⛔ NEW BLOCKER: year-length convention (360d classical vs 365.25d civil) + rounding —
  Machan to confirm what "Astro Predictors" prints (needed for byte-parity).
- Wave 2 done. Next: wave 3 = foundations/rahu-ketu.md (factor B core).

## 2026-10-31 (wave 3) — foundations/rahu-ketu.md COMPLETE (400 lines)

- Part 0 doctrine: chaya graha (no bhava ownership → proxy functional color; delivery through
  dispositor = factor C's core), head/tail natures, shanivat-Rahu / kujavat-Ketu analogies WITH
  LIMITS (texture borrowing only, never lordship/dignity/chain), dignity = commentary-only
  (locked exclusion H), node aspects OFF (7th-from already captured by axis-first reading —
  turning aspects on would double-count the partner house).
- Part 1 motion mechanics: mean-node 6798d cycle, 0.05295°/day, 566d/sign, 252d/nakshatra,
  63d/pada; mean-vs-true (report mean locked; true-node triple-pass deferred v2); orb windows
  computed (±3° = 113d exact band, ±5° = 189d active zone → stellium contacts OVERLAP → engine
  renders dated peaks inside overlapping bands); retrograde = reverse-degree contact order;
  factor-D spine + node-self-star intensification clause.
  ⛔ FACTOR-D DISCREPANCY FLAGGED (blocking): AGENTS.md says "~40–41 days per nakshatra";
  astronomy says ≈252d/nakshatra (63d/pada). Machan must rule what the 40–41d unit is before
  the sub-period renderer is built.
- Part 2: 14 contact templates (transit Rahu/Ketu × 7 natal grahas) — mechanism + texture +
  domain lean each; cross-rule: Rahu = more-of-it, Ketu = release-of-it on the SAME portfolio.
- Part 3: Rahu return (18.6y, desire-cycle resets) & half-return (9.3y, axis flip, diagnostic);
  both color the whole sign-transit, stack with other contacts, carry no house semantics of
  their own.
- Part 4: 6 axis templates (1/7 … 6/12, both directions each) with per-domain lean lines;
  locked favorability flags carried (Rahu ✓ 3/6/10/11, Ketu ✓ 3/6/11).
- Part 5 showcase (Dec-2026 Makaram stellium, all math python-verified): entry 2026-12-07;
  exact contacts Moon ≈2027-01-09 · Venus ≈2027-04-29 · Saturn ≈2027-06-25 · Mars ≈2027-08-14;
  exit ≈2028-06-25 (±few days pending ephemeris parity). Factor-D spine: Avittam (janma star!)
  →2027-04-11, Thiruvonam →2027-12-19, Uthiradam →2028-06-25; no node-star intensification
  (Mars/Moon/Sun lords); no return/half-return in window; Ketu leg in empty Katakam reads
  axis-template-only through dispositor Moon. Both frames fire (4/10 Lagna + 1/7 Moon) →
  double-strength axis.
- [school note] queue: Guru-Chandala-by-transit naming · dignity-commentary print/omit ·
  half-return diagnostic framing.
- Next: wave 4 = domains.md + templates (gated on decisions #1 domain list, #4 language);
  then contact-rules module (factor B engine) once Machan corrects this file.

## 2026-10-31 10:33 IST — CHANGELOG.md established; GK-01 delegated to Panduranga
- Created `CHANGELOG.md` (project-specific, end-to-end): GK-xx gate-kept items registry
  (GK-01…GK-11 consolidated from every ⛔ across MEMORY.md + file footers, each with owner
  and blocks-list) + full chronological session history (2026-10-30 founding → 2026-10-31
  waves 1–3) + next-scheduled-work footer. AGENTS.md conventions updated to mandate it.
- **Machan's ruling**: factor-D "~40–41 days per nakshatra" discrepancy → **owned by
  Panduranga** (developer). Registered as GK-01, OPEN · BLOCKING — the factor-D sub-period
  renderer must not be built until his resolution lands. On resolution, four places update
  together: CHANGELOG registry, rahu-ketu.md Part 1.1 flag, AGENTS.md factor-D line, MEMORY.md.
- GK-03 (year-length) got a two-leg owner: Machan confirms what "Astro Predictors" prints →
  Panduranga implements.

## 2026-10-31 11:08 IST — Milestone 1 approved "good for now"; RKT-01..05 + ORB-02 integrated
- **M1 = report-generation checking order (7 steps) approved by Machan**: axis placement
  (Moon primary, lagna where cusps apply) → landlord condition → dated contact events →
  star-by-star sub-period walk → dasha-bhukti check → question gate → assemble report.
  Full plain-language doc with sample-chart thread: `rule-engine/REPORT-FLOW.md` (awaits
  Machan's read-through → M1 LOCKED; then Milestone 2 = template, gated on GK-08).
- **4 rulings**: combined reading (Moon is "the one making this transit worth"; lagna only
  where cusps are arrived) · show ALL contacts, highlight domain-relevant ones · degree-based
  asymmetric intensity curve · tone per REPORT-01.
- **ORB-02 (Machan's degree ruling, locked)**: node influence begins 3° before the natal
  planet, peaks at exact crossing, declines from the moment of crossing (even 1'), fully
  gone 2.5° past. ≈57d rise + ≈47d fade ≈ 104d window. SUPERSEDES the ≤3°/≤5° symmetric
  orbs — updated in AGENTS.md factor-B, rahu-ketu.md Part 1.3 + Part 5 table + footer.
  New showcase windows: Moon 2026-11-14 → 2027-02-26 · Venus 2027-03-04 → 06-15 ·
  Saturn 2027-04-30 → 08-11 · Mars 2027-06-19 → 10-01 (near-abutting → continuous
  ~11-month contact season, four dated peaks).
- **RKT-01..05 carded in RULES.md** (Machan's framework, adopted): RKT-01 contact = natural
  karakatva + functional lordship (umbrella of the 14 templates) · RKT-02 contacted planet =
  running MD/bhukti lord → that contact peaks (v1 = MD×bhukti only; Antara/Sookshma → v2) ·
  RKT-03 unoccupied house = mild house-level reading · RKT-04 incoming benefic aspects on
  transit Rahu modify positively (strength + functional nature conditioned; dormant in
  showcase — no benefic aspects Makaram) · RKT-05 Ketu reduces/detaches + suppresses natural
  malefics' harm.
- ⛔ GK-12: ORB-02 sign-border question (Moon's rise starts ≈23d before Makaram ingress) —
  owner Machan/Panduranga; gates contact-window edge rendering.

## 2026-10-31 — Machan's Report Generation Framework → Milestone 2 template skeleton drafted
- Machan dumped the full report framework: 3 background data sources (natal data from
  DOB/time/place via our software · panchangam already in software · question→bhava
  mapping) → initial report (birth details + natal & gocharam charts SIDE-BY-SIDE +
  running dasha-bhukti + "understanding the individual" via 3 rule sets) →
  question-specific report. Verdict: no conflicts — Half 1 = profile/context (NEW),
  Half 2 = approved M1 7-step flow (unchanged).
- **PROF-01..03 carded in RULES.md** (Natal Profile Layer): lagna analysis · lagna
  nakshatra analysis · lagna lord placement = life gravitation. Sample: Thulam lagna;
  lagna star Swati p3 **lord Rahu** (transit lands personally — protagonist rules her
  rising star); lagna lord Venus in 4th stellium → home/property/foundation focus.
- **NEW `rule-engine/REPORT-TEMPLATE.md`** = M2 skeleton (sections 0–4, language-neutral;
  prose emission still gated on GK-08). Awaits Machan's read-through.
- Framework de-facto answers GK-09 #3 (input contract = birth data in, positions from
  software) and suggests GK-07 domain list is OPEN-ENDED (kelvigal.md = card registry) —
  both flagged for Machan's confirm, registry kept OPEN.

## 2026-10-31 — Generative-layer decisions (Machan)
- Machan formalized the runtime doctrine: **foundations libraries (facts) + generative
  libraries (print-ready report prose)**; runtime = if/else/loop rule matching → matched
  branch's pre-written text picked up → coherently stitched. NO AI anywhere at runtime.
- **Decisions**: pilot domain = **CAREER** · drafting language = **English first**,
  translation after approval (partial answer to GK-08; final print language still open).
- Fragment architecture question (hybrid vs full paragraphs) — Machan asked for the
  "deeper, proper way"; answer presented = 3-tier generative architecture (phrase bank →
  sentence frames → passage blueprints), pending his nod.

## 2026-10-31 — Phase 4 build complete (Machan ordered end-to-end)
- Engine built in SecOS-11 comment style; 15/15 tests green; first career
  report generated at validation/sample_career_report.html (Favorable /
  pattern A, matching the documented answer key).
- Generative banks are DRAFT v0.1 English — awaiting Machan's line-by-line
  grading; fixes land in the banks, never in the engine.
- Open calibration note: GK-03 drift visible in print (bhukti ends ±2–12 d).

## 2026-10-31 (later) — GK-03 → Panduranga's debt
- Machan assigned the dasha date drift to Panduranga as a debt item.
- Mars-vs-Moon headline: decision deferred until Machan reads the full report.

## 2026-10-31 (later) — Glossary rollout done
- Machan's bilingual prefix table (RKT/SIGN/BHAVA/GATE/DIGN/FUNC/STRENGTH/NBR/PARI/
  QUAL/ORB/REPORT/PROF/KB) is the locked naming convention for all rule IDs.
- Master glossary = RULES.md (with reading rules + register notes: KB is a dependency
  not a prefix; ORB-02 without ORB-01; GK-xx = blockers; M1/M2 = milestone docs).
- 12 files carry subset glossaries (prefixes used per file + pointer to master);
  AGENTS/CLAUDE/CHANGELOG/MEMORY carry one-line pointers.
- New prefixes: add to master first, then to subsets of files that use them.

## 2026-10-31 (later) — RKT-06 aggregation rule added
- New locked rule: **RKT-06 — chronological multi-planet transit aggregation**
  (independent per-contact reads → order by exact peak → one date-wise narrative;
  no contact loses its own significance/timing).
- ⏳ Overlap sub-clause proposed (highest ORB-02 intensity leads; undertow named with
  dates) — awaiting Machan's nod.
- ⏳ Engine gap flagged: Section 3 event list is relevance-ordered, RKT-06 wants
  chronological narrative — decision parked with the Mars/Moon headline ruling.

## 2026-10-31 (later) — RKT-07 transition rule locked
- New locked rule: **RKT-07 — sequential planetary contact transition** — hand-offs
  narrated as one continuous period with two named currents (fading previous +
  approaching next); both windows/peaks preserved; no degree-equality assumption.
- This RESOLVES RKT-06's parked overlap clause (my intensity-lead proposal superseded
  by Machan's continuous-progression ruling); RKT-06 card updated in place.
- Queued for engine/banks: chronological event ordering (RKT-06) + fading/rising
  transition frame pairs (RKT-07) — lands after Machan's report read-through.

## 2026-10-31 (later) — Consolidated rule update applied
- New locked cards: **GATE-02** (DBAS = events; planet = characteristics; ORB intensity
  vs DBAS priority are separate dimensions) · **RKT-08** (star-lord governance of
  no-contact segments; natal + transit channels; 50% debilitation rider applied once;
  NBR via NBR-01/02 only) · **RKT-09** (inter-contact gaps are star-lord-mediated,
  never empty).
- Amended in place: **ORB-02** (sign-boundary independence — **GK-12 RESOLVED**;
  early-influence register; duration guidance = explanatory only) · **RKT-06**
  (equal/near-degree simultaneous activation) · **RKT-07** (ORB-02 percentage
  intensity language in transitions) · **RKT-04** (integration clause, no automatic
  positive guarantee) · **REPORT-01** (global positive-dominant standard + absolute
  no-distress constraint + preferred Tamil caution phrases).
- New blocker: **GK-13** — RKT-08 clause B needs full transit graha positions;
  transit JSON today = nodes only. Owner Machan/Panduranga.
- Engine queues (unchanged, still parked on report read-through): chronological
  ordering (RKT-06), transition frames + intensity lines (RKT-07), star-lord segment
  evaluation (RKT-08/09 once GK-13 feed exists).

## 2026-11-01 — On GitHub
- Personal repo `sujansuresh/astro-core`, branch **astro-engine** = this project.
- Local branch `vijay-transit` tracks `origin/astro-engine`.
- Push path: `git push` (upstream set). Personal SSH alias `github.com-personal`.
- NOTE: remote `vijay-transit` branch holds an unrelated "Titus Arith" upload —
  do not force-push over it without Machan's explicit word.

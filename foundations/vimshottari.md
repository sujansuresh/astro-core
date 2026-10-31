# VIMSHOTTARI.md — The 120-Year Dasha Library (Factor E), Encyclopedic

---

## GLOSSARY — Rule ID prefixes used in this file

> Master table: `rule-engine/RULES.md` → GLOSSARY. Only the prefixes used in this file are listed below.

| Prefix | விரிவாக்கம் | எதைக் குறிக்கிறது? |
|---|---|---|
| SIGN | Signification | கிரகங்கள் எதைக் குறிக்கின்றன, எந்தப் பாவங்களை வழங்குகின்றன |
| GATE | Question Gate | கேள்விக்குரிய பாவங்கள் மற்றும் பலன் தீர்மானம் |

---

> **source**: classical base (BPHS Vimshottari chapters / Phaladeepika / parambariya
> dasha practice) + Machan's practice corrections
> **status**: DRAFT — awaiting Machan's line-by-line practice corrections
> **consumed-by**: **factor E** (dasha amplifier), **GATE-01** (the DBAS leg — "is the
> question's core bhava signified by the RUNNING lords?"), SIGN-01..05 (the chain is
> computed per dasha/bhukti lord), domain lenses, the report's era-vs-window layering
> **standard**: encyclopedic, general-purpose, chart-agnostic. Written ONCE; reusable by
> any future module. Worked example (sample chart's Jupiter MD) is illustrative only.
> **sibling files**: nakshatras.md (each star's dasha lord — the starting-point lookup),
> grahas.md (what each dasha lord IS), functional-nature.md (what each lord DOES per
> lagna), RULES.md (GATE-01, SIGN-01..05)

---

## Part 0 — The wheel

Vimshottari = a **120-year cycle** divided among 9 lords in a fixed sequence. A native
enters the wheel at birth through the **Moon's nakshatra**: the star's lord owns the
opening mahadasha (MD); the fraction of the star already traversed decides the
**balance of dasha** consumed at birth.

| # | Lord | Years | Stars lorded (nakshatras.md cross-ref) |
|---|---|---|---|
| 1 | Ketu | 7 | Ashwini · Magha · Moolam |
| 2 | Venus | 20 | Bharani · Pooram · Pooradam |
| 3 | Sun | 6 | Karthigai · Uthiram · Uthiradam |
| 4 | Moon | 10 | Rohini · Hastham · Thiruvonam (Shravana) |
| 5 | Mars | 7 | Mirugasirisham · Avittam · Chithirai (2nd half) |
| 6 | Rahu | 18 | Thiruvathirai (Ardra) · Swathi · Sadayam |
| 7 | Jupiter | 16 | Punarpoosam · Visakam · Poorattathi |
| 8 | Saturn | 19 | Poosam · Anusham · Uthirattathi |
| 9 | Mercury | 17 | Ayilyam · Kettai · Revathi |
| | **Total** | **120** | 27 stars, 3 per lord |

The sequence never varies: Ketu → Venus → Sun → Moon → Mars → Rahu → Jupiter → Saturn →
Mercury → (Ketu again). Bhukti (antardasha) inside any MD runs the same sequence starting
from the MD lord. Pratyantar and finer: **deferred to v2** (v1 resolves to MD × bhukti —
the era and the window).

**Sub-period length formula** (exact, engine-verified):
`bhukti_years = MD_lord.years × AD_lord.years / 120` — then rendered y/m/d.
**[convention note: this file's tables use the classical 360-day year rendering; the
engine stores exact days and rounds at render — Machan to confirm which calendar his
software prints, for byte-parity]**.

---

## Part 1 — Balance of dasha at birth (the starting math)

```
star_span = 13°20' = 800'
fraction_remaining = (star_end − Moon_longitude) / 800'
balance_years   = fraction_remaining × star_lord.years
birth MD start  = birth_moment − (elapsed fraction × star_lord.years)   // conceptual
first bhukti    = remainder of star_lord's own bhukti, then the sequence
```

**Worked (sample chart)**: Moon at Makaram 28°12' = 298°12' absolute, in **Avittam**
(Dhanishta, a Mars star): Avittam spans 293°20' → 306°40'. Elapsed = 4°52' = 292';
fraction remaining = 508/800 = **0.635**. Balance of Mars MD at birth = 0.635 × 7y ≈
**4y 5m 10d** → Mars MD ends ≈ 1996-08-12 (birth 1992-03-02). Then: Rahu MD 18y →
2014-08-12; **Jupiter MD 16y → 2030-08-10** ✓ (matches the chart's locked schedule).

**Verification chain (the three locked dates reproduce exactly)** — Jupiter MD bhuktis
from 2014-08-12, each = 16 × AD / 120:

| Bhukti | Length | Runs |
|---|---|---|
| Jup–Jup | 2y 1m 18d | 2014-08-12 → 2016-09-30 |
| Jup–Sat | 2y 6m 12d | → 2019-04-12 |
| Jup–Mer | 2y 3m 6d | → 2021-07-18 |
| Jup–Ket | 11m 6d | → 2022-06-24 |
| Jup–Ven | 2y 8m | → 2025-02-24 |
| Jup–Sun | 9m 18d | → 2025-12-12 |
| **Jup–Moon** | 1y 4m | → **2027-04-11** ✓ (current at transit start) |
| **Jup–Mars** | 11m 6d | → **2028-03-17** ✓ |
| **Jup–Rahu** | 2y 4m 24d | → **2030-08-10** ✓ (MD end) |

All three locked bhukti dates fall out of the formula untouched — the schedule is
internally consistent. (Minor ±1–2 day jitter vs printed panchangas comes from the
year-length convention; see the note above — **Machan to rule which his "Astro
Predictors" prints, so the engine matches byte-for-byte**.)

---

## Part 2 — The nine MD textures (the era layer)

The MD lord sets the **era**: 6–20 years during which that graha's nature, portfolio
(grahas.md), and signification chain (SIGN-01..05, computed for that graha in that chart)
dominate delivery. Texture first, verdict second — the era colors everything the windows
(bhuktis) decide.

1. **Ketu MD (7y)** — the dissolution era: detachment from form, past-life themes
   surfacing, spiritual acceleration, titles losing taste. Delivers through Ketu's chain;
   materially thin unless the chain is strong. The "less but truer" era.
2. **Venus MD (20y)** — the comfort era: the longest MD; art, alliance, vehicles,
   luxury, relationships formalize. The native's aesthetic and partnership structures
   are built here. Spans so long it usually contains an entire life-stage.
3. **Sun MD (6y)** — the authority era: position, government, father-themes, visibility;
   the shortest MD — concentrated, hot, public. Health of self and father watch.
4. **Moon MD (10y)** — the emotional era: mother, home, public dealings, mind as the
   theater; fortunes fluctuate with the Moon's condition; travel and homeland themes.
5. **Mars MD (7y)** — the arena era: property, courage, siblings, conflict and surgery;
   fast events, decisive breaks; land deals and competition wins.
6. **Rahu MD (18y)** — the amplification era: foreign, unconventional, mass-scale,
   obsessive rise; the native chases the horizon; biggest material surges AND the
   strangest detours; the era where the chart's Rahu chain executes at full volume.
7. **Jupiter MD (16y)** — the expansion era: education, children, wealth, grace, weight
   (of wisdom and of body); the "building of substance" years; for functional-malefic
   Jupiter lagnas the expansion runs through contest (sample chart: see Part 5).
8. **Saturn MD (19y)** — the labor era: responsibility, structure, delay-then-
   permanence; the spine of a working life; what Saturn builds here does not fall.
9. **Mercury MD (17y)** — the intellect era: education, commerce, writing, markets,
   networks of skill; the nimble years.

---

## Part 3 — The bhukti layer (the window) and MD×AD relationship rules

The bhukti lord is the **window**: inside the era, 9 months–3+ years where the AD lord's
chain takes delivery precedence. **Locked doctrine (from the worked verdicts): the bhukti
layer outranks the era layer inside the window** — M1's verdict reads "income rises via
the regular channel (2), not the windfall channel (11)" precisely because Moon bhukti's
chain {4,2,7,10} speaks while Jupiter-MD's {11,...} waits.

**Relationship rules (texture modulators, applied in order):**

- **R-1 — Functional nature of the AD lord** (functional-nature.md): a yogakaraka bhukti
  inside any MD delivers yoga-grade results for its portfolio; a functional malefic
  bhukti delivers its portfolio with cost-texture. (Sample: Mars bhukti 2027-04→2028-03
  = functional malefic *but exalted Ruchaka* — delivery strong, texture hot.)
- **R-2 — Natural relation MD↔AD** (functional-nature.md Part 4, directionality):
  friendly pairs glide; enemy pairs grind (era-vs-window friction); asymmetric pairs
  deliver one-sided comfort. Jup–Moon: Jupiter→Moon = F, Moon→Jupiter = N → smooth-ish
  era-window harmony. Jup–Rahu: nodes borrow dispositor relation — Rahu tenants Dhanus,
  Jupiter's own sign → self-relation: the era's lord hosts the window's lord → amplified
  coherence for 2028-03→2030-08.
- **R-3 — Relative placement (AD lord from MD lord)**: AD lord in **6/8/12 from the MD
  lord** = friction window (the classic dasha-sandhi texture); in kendra/trikona from MD
  lord = support window. (Sample: MD lord Jupiter in Simha; bhukti Moon in Makaram =
  **6th from Jupiter** → the current window carries the friction flag: delivery YES
  (chain {4,2,7,10}), but through effort/emotional cost. Rahu in Dhanus = **5th from
  Jupiter** (trikona) → the 2028-03→2030-08 window runs support-textured.)
- **R-4 — AD lord's house from lagna AND from Moon** (factor A's two frames, natal):
  both frames read; Moon-frame = how it feels, lagna-frame = what happens.
- **R-5 — Dasha-sandhi (junctions)**: the first/last ~5% of a bhukti is handover blur —
  the engine renders sandhi weeks as "transition" texture, never as event peaks.
- **R-6 — Node bhuktis**: Rahu or Ketu bhukti inside any MD **amplifies the transit
  module** (factor E's locked core): when a node window runs during a node transit,
  every factor-B contact and factor-D nakshatra sub-period reads one grade louder.

**Full 9×9 bhukti-length table**: engine-computed from the Part-1 formula; not printed
here (81 cells of arithmetic, zero doctrine). The Jupiter-MD row above is the worked
reference.

---

## Part 4 — GATE-01's DBAS leg (how a window "supports" a question)

```
function dbas_support(question_card, date):
    (MD, AD) = vimshottari_at(date)
    chain_md = signification_chain(MD_lord)   // SIGN-01..05 with 100/30 weights
    chain_ad = signification_chain(AD_lord)
    for house in question_card.core:
        score = chain_ad[house] + 0.5 × chain_md[house]   // window leads, era backs
    support = every core house scored > 0 AND at least one core signified ≥100 by AD
    viruddha_watch = viruddha house signified ≥100 by AD while core support weak
    return { supported, viruddha_watch, flavors: signified modifiers → clause list }
```

- **DBAS ✓ requires the AD chain to carry at least one core bhava at full strength
  (100)** — occupancy or empty-house-ownership tiers (SIGN-01/03/04), not the 30%
  suppressed tier. The MD chain at half-weight backs the era claim.
- **Flavors**: each signified *modifier* bhava injects its kelvigal clause — this is
  where the report's precision comes from (e.g., Moon bhukti chain {4,2,7,10} hitting
  R1's core {7,2,11}: two of three cores + the +4 flavor = "alliance forms, family
  absorbs, home-anchor pre-loaded").
- **Viruddha leg**: strong AD signification of the viruddha house with weak core → the
  tilt-NO mechanism (kelvigal.md global mechanics).
- **Nodes as lords**: Rahu/Ketu MD/AD chains resolve per SIGN-05 (nodes deliver through
  dispositor + occupancy + star-lord); e.g., Rahu bhukti ≈ {3 @100 (occupancy), 9 @100
  (star-lord Ketu occupies 9)} for the sample chart — the F1 MIXED anatomy's DBAS leg
  from 2028-03.

---

## Part 5 — Worked example: the sample chart's era and windows through the transit

**Era**: Jupiter MD (2014-08 → 2030-08-10). Jupiter = functional malefic (3/6 lords,
Thulam) occupying the 11th, retrograde, vargottama → the expansion era that *earns*:
gains through competition/service, arriving after revision, repeating in cycles
(functional-nature.md Part 5). MD chain: **11 @100 · 4 @100 · 1&8 @100 · 3&6 @30**.

**Windows overlapping the transit window (2026-12-07 → ~2028-06)**:

- **Jup–Moon (→ 2027-04-11)**: AD chain **{4,2,7,10} @100** (4 occupied; 2/7/10 via
  ownership/star-lord tiers per the locked chain) → DBAS ✓ for C2 promotion (10),
  M1 income (2), R1 marriage (7,2) — the three POSITIVE verdicts' shared leg. R-3 flag:
  Moon sits 6th-from-Jupiter → delivery through effort/emotional cost; the verdicts
  stand, the texture is "earned".
- **Jup–Mars (2027-04-11 → 2028-03-17)**: AD chain **{4,10 @100 via star-lord Moon;
  2,7 @100 owned-empty}** → career/money/marriage support CONTINUES at full grade;
  texture turns hot (exalted Ruchaka Mars as functional malefic; transit Rahu
  retrograding onto natal Mars during this window — the factor B × E crossfire: the
  amplified warrior; the report's dated C2 peak lands here).
- **Jup–Rahu (2028-03-17 → 2030-08-10)**: AD chain ≈ **{3 @100, 9 @100}** → the
  foreign/fortune channels open — F1's DBAS leg finally ✓ — but the gochara axis has
  moved past Makaram by then (transit leg ✗ inside the window): the F1 MIXED verdict's
  exact time-anatomy, era-window level. R-6: node bhukti = the loudest amplifier in the
  chart's decade.

**Factor-E cross rule demonstrated**: the transit (gochara) supplies the *weather*;
Vimshottari supplies the *soil*. GATE-01 requires BOTH legs — which is why identical
transits deliver differently across natives, and why this file exists separately from
the transit factor files.

---

## Status & open items

- **Filed as DRAFT** — Machan to correct textures, the R-rules, and the DBAS thresholds
  (the "≥100 by AD" support bar is formalized from the worked verdicts; Machan confirms).
- ⛔ **Convention note (blocking for byte-parity)**: year-length (360d classical vs
  365.25d civil) and rounding at render — **Machan to confirm what "Astro Predictors"
  prints**; the engine stores exact days either way.
- ⛔ **Pratyantar/sookshma deferred to v2** — v1 resolves to MD × bhukti. The report's
  dated sub-periods come from factor D (nakshatra sub-periods) + factor B (contacts),
  NOT from finer dasha legs. Machan confirms or upgrades.
- ⛔ **[school note]**: R-3's 6/8/12-from-MD-lord friction rule (widespread parambariya
  practice; Machan confirms he uses it) · R-2's node-relation borrowing rule.
- **Consistency proof on file**: the three locked bhukti dates (2027-04-11, 2028-03-17,
  2030-08-10) reproduce from the Part-1 formula with zero fudging.

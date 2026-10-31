# UYIR-PORUL.md — Living vs Material Karakatva Split (NBR-02's Table), Encyclopedic

---

## GLOSSARY — Rule ID prefixes used in this file

> Master table: `rule-engine/RULES.md` → GLOSSARY. Only the prefixes used in this file are listed below.

| Prefix | விரிவாக்கம் | எதைக் குறிக்கிறது? |
|---|---|---|
| SIGN | Signification | கிரகங்கள் எதைக் குறிக்கின்றன, எந்தப் பாவங்களை வழங்குகின்றன |
| GATE | Question Gate | கேள்விக்குரிய பாவங்கள் மற்றும் பலன் தீர்மானம் |
| NBR | Neecha Bhanga Resolution | நீசபங்கம் மற்றும் அதன் விளைவுகள் |
| REPORT | Report Generation | அறிக்கை உருவாக்கும் விதிகள் |

---

> **source**: classical karakatva base (BPHS / Phaladeepika / Jataka Parijata) + Machan's
> practice (the exchange rule is his; the split mechanics are formalized here)
> **status**: DRAFT — awaiting Machan's line-by-line practice corrections
> **consumed-by**: **NBR-02** (the only rule that reads this file — the uyir→porul
> exchange cost table), REPORT-01 (the soft-rendering clause library), domain lenses
> (which uyir item intersects the asked question)
> **standard**: encyclopedic, general-purpose, chart-agnostic. The split is authored ONCE;
> any future module that reasons about cost/compensation (transit, natal, prasna) reads
> the same table. Worked example (sample chart's Mercury) is illustrative only.
> **sibling files**: grahas.md (the full karakatva banks this file splits), RULES.md
> (NBR-01/NBR-02 cards), functional-nature.md (which branch fires), kelvigal.md (the
> question→bhava sets the pick mechanic intersects against)

---

## Part 0 — The split principle

Every graha's karakatva portfolio divides into three layers:

1. **UYIR (உயிர்) — the living portfolio**: the graha's signified **persons and
   animate relations** — father, mother, maternal uncle, siblings, spouse, children,
   gurus, servants, rivals. These are what NBR-02's benefic branch *spends*: when a
   rescued functional benefic converts, **one uyir karakatva is renounced** (softly,
   probabilistically — REPORT-01).
2. **PORUL (பொருள்) — the material portfolio**: the graha's signified **materials,
   deliverables, assets, and matters-as-outcomes** — property, gold, education-as-degree,
   commerce, status, vehicles. These are what the exchange *pays back*: **one porul
   karakatva is delivered as replacement**, and the report steers the native's focus here.
3. **BOUNDARY — the subtle faculties**: the graha's signified **inner faculties of the
   native himself** — atma (Sun), manas (Moon), physical energy (Mars), speech/buddhi
   (Mercury), jnana (Jupiter), reproductive faculty (Venus), ayus (Saturn), fear-complex
   (Rahu), liberation-faculty (Ketu). **Locked (NBR-02 card): these are NOT hard-coded
   cost items.** They are handled contextually per question — the engine may *reference*
   them as texture ("the mind runs quieter this window") but never books them as the
   exchange cost.

**Why the split exists**: NBR-02's exchange must name its currency. Without this table,
"one uyir karakatva is renounced" has no lookup; with it, the engine can intersect the
rescued planet's living portfolio against the asked question's bhavas and flag the
*specific channel* (e.g., maternal-uncle) — softly, never as fate.

---

## Part 1 — The pick mechanic (which uyir item, which porul item)

```
function pick_exchange(planet, lagna, asked_domain):
    if bhanga_tier(planet) not in {c1, c2}:          return null      // NBR-02 gate
    if functional_nature(planet, lagna) == MALEFIC:  return CONVERSION // no cost — see Part 3

    // EXCHANGE branch (rescued functional BENEFIC):
    Q = kelvigal.bhavas(asked_domain)                 // core + modifier + viruddha
    chain = signification_chain(planet)               // SIGN-01..05: occupied, star-lord's
                                                      // houses, owned houses, aspects
    hits = []
    for item in UYIR[planet]:
        if item.bhava in intersect(chain, Q):  hits.append(item)
    // ranking: core-bhava hit > modifier hit > viruddha hit; ties → first-listed item
    //          (the portfolios below are ordered by classical weight)
    if hits: flag = { item: hits[0], mode: "steer" }        // name the channel softly
    else:    flag = { item: null,    mode: "background" }   // generic clause, no naming

    porul_pick = PORUL[planet] item whose bhava ∈ Q.core    // the compensation is read
                 else first-listed porul item                // in the ASKED domain first
    return { shape: EXCHANGE, cost_flag: flag, reward: porul_pick }
```

**Rendering contract (REPORT-01, locked)**: the cost line always renders as possibility +
redirect, e.g. *"oru uyir karakatvam vilaga-nadakkalaam; gavanam — porul paagam valam
serum"* — never "you will lose X". `mode: "background"` renders one generic sentence deep
in the report body; `mode: "steer"` renders the named channel + the porul steering clause
near the verdict reasons.

**Non-intersection is the common case**: most questions don't intersect the rescued
planet's living portfolio — the exchange then stays a background note. This is by design:
NBR-02 is a *softener/explainer*, never the verdict's spine.

---

## Part 2 — The nine tables

*Convention*: `bhava:` tags name the house each item belongs to (for the pick mechanic's
intersection). Portfolios are **ordered by classical weight** (first-listed = strongest
claim). Items marked **[school note]** await Machan's ruling. Condensed from grahas.md's
numbered banks — that file stays the encyclopedia; this file is the engine's lookup.

### SUN (Suriyan)
- **UYIR**: 1. father `bhava:9` · 2. boss/employer `bhava:10` · 3. the king/leader-figure
  `bhava:10` · 4. government officers `bhava:10` · 5. authority figures generally
  `bhava:10` · 6. physicians/healers of status `bhava:6` · 7. son **[school note:
  some paramparas; we hold children = Jupiter — Machan to rule]**
- **PORUL**: 1. status & position `10` · 2. government favor `10` · 3. gold `2` ·
  4. authority-as-capital `10` · 5. reputation `10` · 6. temples & their patronage `9` ·
  7. copper/ruby/heat-assets `2`
- **BOUNDARY (never hard-coded)**: atma · vitality · right eye · bones

### MOON (Chandran)
- **UYIR**: 1. mother `bhava:4` · 2. maternal figures `4` · 3. nurses/caregivers `6` ·
  4. the public/masses `4` · 5. women of the household `4` · 6. wife **[school note:
  male-chart parampara; we hold spouse = Venus/Jupiter per decision #6 — Machan]**
- **PORUL**: 1. home & comforts `4` · 2. liquids/water assets `4` · 3. milk & dairy `2` ·
  4. pearls/silver `2` · 5. agricultural produce `4` · 6. water-body property `4` ·
  7. the homeland base `4`
- **BOUNDARY**: manas · sleep · left eye · bodily fluids

### MARS (Sevvai/Chevvai)
- **UYIR**: 1. younger siblings `bhava:3` · 2. brothers/co-borns `3` · 3. soldiers/police
  `6` · 4. surgeons `6`/`8` · 5. rivals & declared competitors `6` · 6. husband
  **[school note: female-chart parampara; hold per decision #6]**
- **PORUL**: 1. land & immovable property `4` · 2. machinery & instruments `3` ·
  3. engineering works `10` · 4. courage-as-capital (ventures) `3` · 5. weapons/tools
  `6` · 6. red coral/metals `2` · 7. competitive victories `6`
- **BOUNDARY**: physical energy · blood · marrow

### MERCURY (Budhan) — *the sample chart's rescued graha; see Part 4*
- **UYIR**: 1. maternal uncle (matula) `bhava:6` · 2. friends `11` · 3. classmates/
  batchmates `4`·`5` · 4. cousins & young relatives `3` · 5. students/disciples-of-craft
  `5` · 6. young colleagues `6` · 7. traders/merchants-as-persons `7` · 8. adoptees
  **[school note]**
- **PORUL**: 1. education & degrees `4`·`5` · 2. commerce & trade `7`·`10` · 3. writing/
  documents `3` · 4. accounts/audit `2` · 5. markets & their access `7` · 6. emerald/
  green assets `2` · 7. communication infrastructure `3` · 8. analytical skill-as-asset `5`
- **BOUNDARY**: speech faculty · buddhi · skin · nerves

### JUPITER (Guru/Viyazhan)
- **UYIR**: 1. guru/teachers `bhava:9` · 2. elders `9` · 3. children `5` · 4. judges/
  dharma-arbiters `9` · 5. priests `9` · 6. advisors/ministers `5` · 7. husband
  **[school note: female-chart parampara; hold per decision #6]**
- **PORUL**: 1. wealth & the vault `2`·`11` · 2. higher degrees & titles `9` ·
  3. gold `2` · 4. banking/finance access `2` · 5. grace-as-deliverable (the opened door)
  `9` · 6. yellow sapphire `2` · 7. expansion of assets `11`
- **BOUNDARY**: jnana/wisdom · liver · fat-metabolism

### VENUS (Sukran)
- **UYIR**: 1. wife/spouse `bhava:7` **[decision #6 pending — male-chart branch]** ·
  2. women-as-figures `7` · 3. artists/performers `5` · 4. lovers `5` · 5. in-laws-as-
  companions `8` · 6. beauticians/designers-of-craft `3`
- **PORUL**: 1. vehicles `4` · 2. luxury goods & comforts `4` · 3. ornaments/jewelry `2` ·
  4. art-as-asset `5` · 5. perfumes/textiles `2` · 6. diamonds/white stones `2` ·
  7. cattle **[school note: some paramparas]** · 8. partnership capital `7`
- **BOUNDARY**: reproductive faculty (shukra) · eyes (left, parampara variant) ·
  kidney-balance

### SATURN (Sani)
- **UYIR**: 1. servants/laborers `bhava:6` · 2. subordinates `6` · 3. the elderly `8` ·
  4. workers/the labor class `6` · 5. the downtrodden `12` · 6. father **[school note:
  day-chart parampara — we hold 9 = father; Machan to rule]** · 7. chronic patients `6`
- **PORUL**: 1. agricultural land `4` · 2. iron/steel & heavy industry `10` · 3. oil &
  underground resources `8` · 4. long-term structures & real estate `4` · 5. mines `8` ·
  6. blue sapphire `2` · 7. longevity-assets (pensions, annuities) `8` · 8. discipline-
  compounded skill `6`
- **BOUNDARY**: ayus · bones/joints · chronic-disease seat · nerves

### RAHU
- **UYIR**: 1. foreigners `bhava:12` · 2. strangers/the exotic other `12` · 3. mass crowds
  `11` · 4. paternal grandfather **[school note: parampara — Rahu paternal / Ketu
  maternal; Machan to rule]** · 5. outcasts & the marginalized `12`
- **PORUL**: 1. foreign goods & imports `12` · 2. technology/novel instruments `3` ·
  3. sudden gains `8`·`11` · 4. gambles & their stakes `5` · 5. poisons-as-medicines `8` ·
  6. the shortcut that works `3`
- **BOUNDARY**: illusion/fear-complex · epidemic susceptibility · skin eruptions

### KETU
- **UYIR**: 1. monks/renunciates `bhava:12` · 2. mystics/adepts `9`·`12` · 3. maternal
  grandfather **[school note]** · 4. the departed-as-guides `12`
- **PORUL**: 1. occult knowledge-as-asset `8` · 2. mantra siddhi `5`·`9` · 3. sudden
  insights `8` · 4. the flag/mark of attainment (dhvaja) `10` · 5. moksha-as-attainment
  `12` · 6. the release that frees capacity `12`
- **BOUNDARY**: liberation faculty · psychic sensitivity · epidemic susceptibility
  (shared with Rahu)

---

## Part 3 — The CONVERSION branch (rescued functional MALEFIC): no cost table needed

When the debilitated-and-rescued planet is a **functional malefic** for the lagna
(functional-nature.md), NBR-02's malefic branch fires: **debility incapacitated the harm;
rescue converts the graha into a super-good deliverer.** There is no uyir cost and no
porul replacement — the "exchange" already happened at debilitation (the harm was what
got destroyed).

- The engine emits no cost flag; instead a **conversion clause**: the graha's dusthana/
  trishadaya lordship matters (disease, debt, enemies, loss) arrive defanged, and the
  rescued graha delivers its *good* portfolio at elevated grade.
- Why no table: a malefic's uyir portfolio (rivals, enforcers, hard masters) being
  incapacitated is itself the benefit — flagging it as "cost" would invert the doctrine.
- **Example (hypothetical, locked in the NBR-02 card)**: Jupiter (3&6 lord = functional
  malefic for Thulam) debilitated in Makaram, rescued by own-sign Saturn → the 6th-lord
  harms (disease/debt/enemies) lose their bite; rescue converts Jupiter into a super-good
  deliverer. (In the sample chart Jupiter is NOT debilitated — this is the card's
  counterfactual arm.)

---

## Part 4 — Worked example: the sample chart's Mercury through the pick mechanic

**The only rescued planet in the sample chart**: Mercury, debilitated Meenam 6th,
chain-rescued by star-lord Saturn (NBR-01 **c2**) → tier in {c1,c2} ✓. Functional nature
(functional-nature.md, Thulam): Mercury lords **9 & 12** → trikonadhipati → **functional
BENEFIC** → **EXCHANGE branch** fires. Portfolio above: uyir — maternal uncle (6),
friends (11), classmates (4/5), cousins (3), students (5), young colleagues (6),
traders (7). Porul — education/degrees (4/5), commerce (7/10), documents (3), accounts
(2), markets (7), communication infrastructure (3), analytical skill (5).

Mercury's SIGN chain: **occupies 6** (rank 1) · **star-lord Saturn occupies 4, owns 4&5**
(rank 2/3) · **owns 9 & 12** (rank 3).

**Run per domain** (the question-dependent pick — the locked mechanic):

- **Career (C1 first-job: core {2,6,10,11})**: chain ∩ Q = **{6}** (Mercury occupies 6;
  6 is core) → hit. Uyir candidates with `bhava:6`: **maternal uncle** (rank 1) and young
  colleagues (rank 6) → **flag = maternal-uncle channel, mode "steer"**. Porul pick whose
  bhava ∈ core: commerce (10)/documents… in the career core {2,6,10,11} → **commerce/
  professional craft**. Render: *"Viyazha…" no — render soft per REPORT-01: "Budhan
  neecham-sahitha bhanga petru iruppathaal, oru uyir karakatvam (mama/cirriya
  colleguekal) vilaga-nadakkalaam — gavanam; porul paagam (thozhil-nuutpam, vanigam)
  valam serum."* — possibility + redirect, never fate.
- **Money (M1 income-rise: core {2,11})**: chain {6,4,5,9,12} ∩ {2,11} = **∅** →
  `mode: "background"` — one generic sentence deep in the body. No naming. (Mercury owns
  no 2/11; his star-lord's 4/5 don't intersect; the 6th occupation isn't in M1's core.)
- **Marriage (R1: core {7,2,11})**: intersection ∅ → background. The exchange does NOT
  touch the marriage verdict — the 6th-occupation's viruddha role belongs to GATE-01,
  not NBR-02. (Clean separation: GATE-01 reads bhavas; NBR-02 reads portfolios.)
- **Foreign travel (F1: core {3,9,12})**: chain ∩ Q = **{9, 12}** (Mercury OWNS 9&12;
  both core) → hit on the *ownership* leg. Uyir candidates with `bhava:9` or `bhava:12`:
  none in Mercury's uyir list (his living portfolio sits in 3/4/5/6/7/11) → hits empty
  → `mode: "background"`, but the porul pick fires strong: education/degrees `4/5` via
  the star-lord's 4/5 ownership intersecting F1's modifier set → the report's porul
  steering reads: *foreign/fortune matters delivered through education & documents
  (Mercury's porul), through the Saturn chain (property-homeland)* — exactly the
  F1 MIXED verdict's "the pull is real, the carrying transit is absent" texture given
  a compensation channel.
- **Health (H-cards watching 6)**: H2/H4 viruddha-watch touches 6 → chain ∩ Q = {6} →
  flag maternal-uncle channel again, but REPORT-01's health register softens further:
  texture-only ("indha kaalam mana/care channel-la oru vilagam varalaam"), no person
  named in the health domain.

**What this demonstrates**: same rescued graha, five domains, two different flag modes
(steer vs background), one named channel (maternal uncle — the 6th's own person in
Mercury's portfolio, which is why the NBR-02 card's example names him first), and
compensation always read into the *asked* domain's porul. The engine never books atma/
buddhi (boundary) as cost — Mercury's speech/intellect are explicitly NOT on the table.

---

## Status & open items

- **All nine tables filed as DRAFT** — Machan to correct item by item (cite graha +
  number, e.g., "Mercury uyir #2").
- ⛔ **[school note] queue for Machan**: Sun-uyir #7 (son) · Moon-uyir #6 (wife,
  male-chart) · Mars-uyir #6 (husband, female-chart) · Jupiter-uyir #7 (husband,
  female-chart) · Venus-uyir #1 (wife, male-chart) — **all five collapse into decision
  #6 (gender-conditional spouse karaka), still pending** · Saturn-uyir #6 (father,
  day-chart; held: 9 = father) · Mercury-uyir #8 (adoptees) · Venus-porul #7 (cattle) ·
  Rahu-uyir #4 / Ketu-uyir #3 (grandfather split: paternal/maternal).
- ⛔ **Boundary faculties are policy-locked** (never hard-coded cost items) per the NBR-02
  card — Machan confirms or reopens.
- **Ordering = ranking**: portfolio order is the tie-breaker in the pick mechanic;
  Machan's corrections should re-order, not just add.
- **Consumed-by reminder**: only NBR-02 and REPORT-01 read this file in v1; GATE-01 never
  touches it (bhava support and portfolio cost are separate layers by design).

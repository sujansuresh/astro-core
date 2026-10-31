# RULES.md — Rule Engine Master Register

> Every rule is a condition-based primitive (if/else/threshold/loop). Each card: ID, source,
> statement (Machan's words preserved), formal logic, status. Reports cite rule IDs in reasons.
> Methodology mix (locked 2026-10-30): **~80% parambariya Parashara Hora, ~20% KP**
> (KP kept only where Machan practices it: the nakshatra star-lord signification chain).
> Every rule carries a worked example, preferably from the sample chart
> (Thulam lagna; Moon Makaram 28°12'; stellium Mars/Saturn/Venus in Makaram;
> Mercury debilitated Meena 6th; Jupiter R Simha 11th; Rahu Dhanus 3rd; Ketu Mithuna 9th).

---

## GLOSSARY — Rule ID Naming Convention (மாஸ்டர் அட்டவணை)

> Every rule ID in this project reads as **PREFIX-NN**: the prefix names the module the
> rule belongs to, the number is the rule's serial inside that module. This table is the
> **master** — every other project file carries only the subset it uses, with a pointer here.

| Prefix | விரிவாக்கம் | எதைக் குறிக்கிறது? |
|---|---|---|
| RKT | Rahu–Ketu Transit | ராகு–கேது சஞ்சார விதிகள் |
| SIGN | Signification | கிரகங்கள் எதைக் குறிக்கின்றன, எந்தப் பாவங்களை வழங்குகின்றன |
| BHAVA | Bhava | பாவங்களின் தன்மை மற்றும் பலன்களின் வகை |
| GATE | Question Gate | கேள்விக்குரிய பாவங்கள் மற்றும் பலன் தீர்மானம் |
| DIGN | Dignity | உச்சம், நீசம், ஆட்சி போன்ற கிரக நிலைகள் |
| FUNC | Functional Nature | லக்ன அடிப்படையிலான சுபர் / பாவர் தன்மை |
| STRENGTH | Planetary Strength | கிரக பலம் மற்றும் அதன் வலிமை |
| NBR | Neecha Bhanga Resolution | நீசபங்கம் மற்றும் அதன் விளைவுகள் |
| PARI | Parivartana | கிரகப் பரிவர்த்தனை விதிகள் |
| QUAL | Quality | நட்சத்திர சாரம் மூலம் கிடைக்கும் பலன்களின் தரம் |
| ORB | Orb / Contact Window | கிரகத் தொடுதலின் டிகிரி மற்றும் கால அளவு |
| REPORT | Report Generation | அறிக்கை உருவாக்கும் விதிகள் |
| PROF | Natal Profile | ஜாதகரின் அடிப்படைப் பண்புகள் |
| KB | Knowledge Base | காரகத்துவம் போன்ற அடிப்படைத் தகவல் தொகுப்பு |

### How to read a rule ID
- **RKT-01** = Rahu–Ketu Transit module, முதல் விதி.
- **SIGN-04** = Signification module, நான்காவது விதி.

### Register notes
- **KB** is cited as a *knowledge-base dependency*, not as a rule prefix.
- **ORB-02** exists in this register **without ORB-01** (considered-and-excluded; see AGENTS.md).
- **GK-xx** items are *project blockers*, not rules — they live in `CHANGELOG.md`'s
  gate-kept registry, each with a named owner.
- **M1 / M2** are milestone documents (`REPORT-FLOW.md`, `REPORT-TEMPLATE.md`), not rule IDs.

---

## SIGN — Signification chain (what a planet delivers)

### SIGN-01 — Occupancy primacy 🔒
- **Statement**: A planet delivers FIRST the results of the house/cusp it occupies.
- **Logic**: `signification_chain(P)[rank 1] = occupied_house(P), strength 100%`
- **Example**: Jupiter in 11th → delivers gains/networks/desire-fulfillment first,
  even though it owns 3rd & 6th.

### SIGN-02 — Star-lord occupancy 🔒
- **Statement**: SECOND, the planet delivers the house where its nakshatra (star) lord sits.
- **Logic**: `chain[rank 2] = occupied_house(star_lord(P)), 100%`
- **Example**: Jupiter in Pooram (Venus star); Venus sits 4th → Jupiter also delivers
  property/home/mother/vehicles. (The 20% KP layer.)

### SIGN-03 — Star-lord owned houses 🔒
- **Statement**: THIRD, the houses owned by the star lord.
- **Logic**: `chain[rank 3] = owned_houses(star_lord(P))` with SIGN-04 strength.
- **Example**: Venus owns 1st & 8th (both empty in sample chart) → Jupiter delivers
  self/vitality (1st) and sudden-gains/in-laws/inheritance (8th) at full strength.

### SIGN-04 — Tenant suppression (occupant beats landlord) 🔒
- **Statement**: Ownership-based delivery = 100% only if the house is EMPTY of planets.
  If tenanted, the owner delivers at **30%** — the occupant holds primacy (SIGN-01).
- **Logic**:
  ```
  function ownership_delivery(owner, house):
      if house has any tenant planet: return 0.30
      else:                           return 1.00
  ```
  Applies at **rank 3 AND rank 4** (rank-3 generalization agreed by Machan, 2026-10-30).
- **Example**: Jupiter owns 3rd & 6th, but Rahu tenants the 3rd and Mercury tenants the 6th
  → Jupiter delivers 3rd/6th matters at 30% only.

### SIGN-05 — Aspect = motivation & modifier, never direct delivery 🔒
- **Statement**: Aspected houses are NOT delivered as events by the aspector. An aspect:
  (a) suppresses negativity, (b) boosts positivity, (c) creates motivation/inclination in the
  native toward that house's matters. Event support ONLY if both gates pass.
- **Logic**:
  ```
  function aspect_effect(P, H, domain_lens, dbas):
      emit { house: H, type: MODIFIER,
             suppress_negativity: true, boost_positivity: true, motivation: true }
      if H ∈ domain_lens.kelvikku_bhavas and dbas_lords_signify(H, dbas):
          emit { house: H, type: EVENT_SUPPORT }
      else:
          pass  // motivation only — no event manifests
  ```
- **Example**: Jupiter aspects the 7th → suppresses marital friction, inclines the native
  toward partnership. A marriage EVENT via this aspect needs 7th ∈ asked-domain houses AND
  running DBAS lords signifying the 7th.

---

## BHAVA — House delivery texture (what KIND of result)

### BHAVA-01 — Kendra texture 🔒
- **Statement (Machan)**: Kendras (1/4/7/10) focus on material things and status — "anything
  that wouldn't fill the heart." Kendras deliver MORE money/tangible magnitude than trikonas.
- **Logic**: `texture(kendra) = MATERIAL_STATUS` → drives narrative phrasing + domain weighting.
- **Example**: Rahu transiting the 4th kendra (Makaram stellium) → property, home, vehicles,
  relocation, status of residence — tangible, visible outcomes.

### BHAVA-02 — Trikona texture 🔒
- **Statement (Machan)**: Trikonas (1/5/9) focus on anything that fills the heart — meaning,
  fulfillment. Less money than kendras, but deeper inner significance.
- **Logic**: `texture(trikona) = HEART_MEANING`.
- **Example**: 9th-house (Mithuna, Ketu's natal seat) events = grace, faith, father, dharma —
  meaningful even when not lucrative.
- **Note**: House 1 is both kendra and trikona → dual texture (self = body/status AND dharma).

### BHAVA-03 — Purushartha underlayer 🔒 (Q4 = option b, locked 2026-10-30)
- **Statement**: Under BHAVA-01/02's headline texture, each house also carries a fixed
  purushartha tag — giving domain lenses finer hooks and resolving kendra/trikona tensions.
- **Logic**: fixed tags, zero runtime cost:
  ```
  DHARMA: 1, 5, 9   (== trikona set)
  ARTHA:  2, 6, 10
  KAMA:   3, 7, 11
  MOKSHA: 4, 8, 12
  ```
- **Example**: 4th = kendra + MOKSHA → Rahu-in-4th reads as material property push AND
  "inner peace disturbed, emotional restlessness even when gains land; mother's wellbeing in
  focus." 10th = kendra + ARTHA → Ketu-in-10th reads as pure career/status restructuring.
  7th = kendra + KAMA → partnership/desire language ready if a relationship question arrives.

---

## GATE — Question gates (whether delivery goes well)

### GATE-01 — Kelvikkaana bavagangal gate (the parambariyam way) 🔒
- **Statement**: Every question has its native bhavas (*kelvikkaana bavagangal*). For those
  bhavas: if the current **DBAS** signification is NOT supporting AND the **transit**
  (e.g., Rahu over the relevant planets/cusps) is also NOT supporting → the answer is
  **negative**. One supporting → mixed. Both supporting → positive.
- **Logic**:
  ```
  function question_gate(domain, dbas, transit):
      H = kelvikkaana_bavagangal(domain)
      dbas_ok    = dbas_lords_signify(H)        // via each DBAS lord's SIGN chain
      transit_ok = transit_contacts_support(H)  // gochara contacts to lords/cusps of H
      if dbas_ok and transit_ok:     return POSITIVE
      elif dbas_ok or transit_ok:    return MIXED
      else:                          return NEGATIVE
  ```
- **Example (career question, live chart, early 2027)**: kelvikku bhavas = {2,6,10}.
  Moon bhukti runs (till 2027-04-11): Moon in Avittam → star-lord Mars chain = 4 (occupied),
  4 (star-lord occupied), 2 & 7 (Mars-owned, both empty → 100%), plus Moon's own 10th
  (empty → 100%). Moon signifies {4, 2, 7, 10} → hits 2 & 10 of the career set → **DBAS ✓**.
  Transit Rahu in Makaram conjuncts natal Mars (2nd lord = career-money) → **transit ✓**.
  Gate → **POSITIVE** for career in that window.

### GATE-02 — DBAS separation: events vs planetary characteristics 🔒
- **Statement (Machan)**: a planet describes **qualities and characteristics** through
  its natural significations (karakatvam) and functional lordships (adhipathiyam); a
  **bhava** represents the areas of life and the events that may manifest. This
  separation is a foundational principle governing the entire transit framework.
- **Logic** (applied to every node × planet contact):
  ```
  1. narrate the contacted planet's natural characteristics (karakatvam)
  2. narrate its functional lordships and their life areas (adhipathiyam)
  3. check the planet's / its lordships' connection to the running DBAS
     (RKT-02 v1 scope: Maha Dasha × Bhukti)
  4. if a relevant DBAS connection exists → read bhava-level EVENT possibilities
     through GATE-01's question bhavas
  5. event manifestation is evaluated ONLY via the DBAS × question-bhava rules —
     never from contact strength alone
  SEPARATION GUARDS:
  - a planetary contact does NOT automatically convert into a definite event
  - ORB intensity       = degree of the transit influence (how loud)
  - DBAS connection     = timing & support for relevant bhava events (whether/when)
  - a LOW-intensity contact may still carry HIGH event-level relevance when DBAS
    activates its lordships — the two dimensions are reported separately,
    never conflated
  ```
- **Scope note**: RKT-02's v1 scope (Maha Dasha × Bhukti only) is preserved —
  no Antara/Sookshma amplification until the corresponding v2 rules are approved.
- **Example**: Rahu × Moon (10th lord) exact 09-Jan-27 inside the Moon bhukti → both
  dimensions live: characteristics (mind/mother/career-base churn at full ORB
  intensity) AND event support (10th-house career possibilities time-supported by the
  bhukti, read through the {2,6,10} gate). Contrast: a lower-intensity Venus contact
  whose 1st/8th lordships are DBAS-active still carries event-level weight —
  intensity does not set event priority.

---

## DIGN — Dignity rules (status of delivery)

### DIGN-01 — Dignity = status visibility (thagudhi) 🔒
- **Statement (Machan)**: Exaltation is *thagudhi uyarvaana* — a status you can openly tell
  about. Debilitation is *thagudhi kuraindha* — low status you cannot proudly boast about.
- **Logic**: dignity is an INDEPENDENT axis from event manifestation (GATE-01 decides if/how
  well it happens; DIGN-01 decides whether it carries prestige):
  ```
  EXALTED / OWN  → delivery comes with open, boast-worthy status
  DEBILITATED    → event may still manifest (if gate supports) but WITHOUT public glory
  ```
- **Example**: Both Mars (exalted) and Mercury (debilitated) touch this chart's 4th-house
  property matters. Mars-driven property wins = visible, boast-worthy (the impressive home).
  Mercury-driven property/education results can still land (strong Saturn chain) but carry no
  prestige — the modest degree, the quietly-bought plot.

---

## FUNC — Functional vs natural nature (LISA core)

### FUNC-01 — Functional decides good/bad; natural decides style; harmful traits gated 🔒
- **Statement (Machan)**: delivery is good because the planet is a *lagna subar* (functional
  benefic). But its nature — e.g., Saturn's slow-and-steady — is still there. Its bad
  natures — theft, cruel mindset — won't be there.
- **Logic**:
  ```
  function delivery_character(planet, lagna):
      outcome = functional_nature(planet, lagna)    // BENEFIC → helps; MALEFIC → harms
      style   = natural_texture(planet)             // Saturn: slow, steady — RETAINED
      if functional_nature == BENEFIC:
          suppress(natural_harmful_traits(planet))  // theft, cruelty → absent
      else:
          retain(natural_harmful_traits(planet))    // harmful traits live
  ```
- **Example (real chart)**: Saturn = yogakaraka, own-sign in Makaram → its 4th/5th delivery
  is GOOD, arrives **slowly and steadily** (natural texture retained), and carries none of
  Saturn's harmful traits. The same Saturn as a functional malefic (another lagna) would
  keep those traits live.

---

## STRENGTH — Dispositor, debility & rescue

### STRENGTH-01 — Dispositor modulation 🔒
- **Statement (Machan)**: The dispositor ("house giver") plays a major role. A strong tenant
  with a debilitated dispositor serves with reduced strength. A debilitated tenant whose
  dispositor is exalted or in own sign gets Neecha Bhanga.
- **Logic**: `tenant_effective_strength = f(tenant_dignity, dispositor_condition)`
  - **Q5 resolved (2026-10-30)**: strong tenant + debilitated dispositor = drop ONE tier
    (Strong → Moderate). Partial suppression, never annihilation.
- **Example**: Mars exalted in Makaram with (hypothetical) Saturn debilitated in Mesha →
  Mars delivers at Moderate: the property win arrives, but reduced, delayed, effortful.
- **PARI-01 interaction**: parivartana is DORMANT in DBAS — the landlord penalty evaluates
  on the landlord's plain resolved condition; no pair-resolution pass.

### NBR-02 — Rescued-planet conversion: the uyir→porul exchange (Machan's rule) 🔒
- **Fires when**: a debilitated planet receives neecha bhanga via **NBR-01 c1 (full bhanga,
  dispositor exalted/own) OR c2 (chain-rescue)** — scope **c1+c2** confirmed by Machan
  (2026-10-30). Keys off FUNCTIONAL nature (FUNC-01), never natural nature.
- **Statement (Machan)**: if the rescued planet is a benefic to the ascendant, the candidate
  lets go of one **uyir karakatva** (living signification) and receives a **porul karakatva**
  (material) as replacement. If it is the ascendant's malefic, the debilitation cuts its
  negative doings and the rescue delivers super-good results.
- **Which uyir karakatva — NOT hard-predicted (Machan)**: it depends on the question asked.
  When the asked domain's signifying bhavas intersect the rescued planet's chain/portfolio,
  the report flags the exchange softly and steers the native's focus toward the porul
  karakatva. No deterministic loss statements (see REPORT-01).
- **Logic**:
  ```
  function nbr_conversion(planet, lagna, asked_domain):
      if bhanga_tier(planet) not in {c1, c2}: return null
      if functional_nature(planet, lagna) == BENEFIC:
          involved = intersect(chain(planet), kelvikku_bhavas(asked_domain))
          return { shape:  EXCHANGE,
                   cost:   "one UYIR karakatva renounced — unspecified, framed
                            probabilistically (REPORT-01)",
                   reward: "PORUL karakatva delivered as replacement",
                   emphasis: "steer focus to porul" if involved else "background note" }
      else:  // functional malefic
          return { shape: CONVERSION, cost: null,   // debility already destroyed the harm
                   reward: "super-good delivery" }
  ```
- **Underlying principle**: debility incapacitates the functional portfolio — a benefic pays
  with a living signification and is compensated materially; a malefic's harm itself is what
  gets incapacitated, so rescue = pure gain.
- **Example (real chart, benefic branch via c2)**: Mercury debilitated in Meenam, chain-
  rescued by star-lord Saturn (NBR-01 c2). Mercury = **9th lord (trikonadhipati)** for
  Thulam → functional benefic → EXCHANGE branch applies: her struggle→elevation in
  education/service carries a quiet living-cost (one Mercury-portfolio relation — maternal
  uncle / friends / classmates) and a porul compensation (education, commerce, property via
  the Saturn chain). Rendered as possibility + focus-shift, never as fate.
- **Example (malefic branch, hypothetical)**: Jupiter (3&6 lord = functional malefic for
  Thulam) debilitated in Makaram, rescued by own-sign Saturn → the 6th-lord harms
  (disease/debt/enemies) lose their bite; rescue converts Jupiter into a super-good deliverer.
- **KB dependency**: uyir (living) vs porul (material) karakatva split for all 9 grahas —
  draft table with Machan for correction. Native's own subtle faculties (atma, manas, ayus,
  speech, wisdom) are NOT hard-coded as cost items; handled contextually per question.

### PARI-01 — Parivartana (sign exchange) activation scope 🔒
- **Statement (Machan)**: parivartana does NOT work during dasa-bhukti — don't bother with it
  there. It works only during gochara, and that too only when transit planets are actually
  travelling on top of the parivartana'd cusps.
- **Logic**:
  ```
  function parivartana_effect(p1, p2):    // p1 in p2's sign AND p2 in p1's sign
      on DBAS evaluation:    return DORMANT          // no exchange delivery
      on gochara evaluation:
          if any transit graha conjoins either exchanged sign/cusp:
              return ACTIVE for that window — both houses' matters exchange-fire
          else:
              return DORMANT
  ```
- **Consequence for DBAS**: no special pair-resolution pass. Each planet is evaluated by
  plain rules. (Hypothetical Mars-exalted-in-Makaram ↔ Saturn-debilitated-in-Mesha: Mars
  takes the STRENGTH-01 one-tier penalty from its fallen landlord; Saturn separately gets
  NBR-01 c1 bhanga from its exalted dispositor. The exchange itself adds nothing in DBAS.)
- **Example (gochara)**: same hypothetical exchange — when transit Rahu enters Makaram
  (the 4th cusp for Thulam), the 4th (Makaram) and 7th (Mesha) house matters exchange-fire
  for that transit window.

### NBR-01 — Neecha Bhanga resolution hierarchy (Machan's practice) 🔒
- **Empirical anchor**: this chart's debilitated Mercury **has functioned as
  struggle → then elevation** (Machan's observation of the real life).
- **Machan's attribution**: the rescue comes from **Saturn** — yogakaraka AND 5th-lord
  (trikonadhipati) — which (a) gives *nakshatra saara* to Mercury (Mercury sits in
  U.Bhadrapada, a Saturn star) and (b) casts its **3rd special aspect** from Makaram directly
  onto Mercury in Meenam.
- **Resolution hierarchy** (in priority order):
  ```
  function debility_resolution(planet):
      if planet.dignity != DEBILITATED: return N/A
      c1: dispositor(planet).dignity in {EXALTED, OWN_SIGN}
              → FULL bhanga (STRENGTH-01 primary condition)
      c2: star_lord(planet) is YOGAKARAKA or TRIKONADHIPATI (1/5/9 lord)
          and star_lord is strong
              → CHAIN-RESCUE: status profile = EARLY STRUGGLE → LATER ELEVATION,
                delivered THROUGH the star lord's portfolio of houses
      c3: classical kendra conditions (e.g., planet exalted in the debilitation sign
          sitting in kendra — the "Venus rule")
              → 30% factual consideration ONLY — a corroborating weight, never the gate
      if rescuer (dispositor or star lord) also ASPECTS the planet:
              → negativity of the debility is suppressed (per SIGN-05)
  ```
- **Key principle (Machan)**: rescue flows through the **nakshatra chain and aspect support**,
  not through classical sign-dignity gymnastics. The Venus/kendra rule is held at 30% weight.
- **Example (Mercury, fully compiled)**: dispositor Jupiter (Simha, friend's sign) → c1 fails.
  Star lord Saturn = yogakaraka + trikonadhipati, own-sign, aspecting Mercury → **c2 fires +
  aspect support** → Mercury = chain-rescued. Venus-in-4th-kendra noted at 30% corroboration.
  Reading: education/service matters begin as struggle, elevate later, and deliver 4th/5th
  portfolio (property, education, creativity) through 6th-house means (service, employment).

### QUAL-01 — Nakshatra saara (star-lord quality injection) 🔒
- **Statement**: A planet's delivery QUALITY inherits its star lord's functional nature and
  dignity — distinct from *which* houses are delivered (SIGN chain) and *how much* (SIGN-04).
- **Logic**: `delivery_quality(P) ⊃ f(functional_tier(star_lord(P)), dignity(star_lord(P)))`
- **Example**: Mercury's star lord is the chart's yogakaraka → Mercury's results carry
  raja-yoga-grade backing despite its own debilitation. Contrast: a debilitated planet whose
  star lord is a weak functional malefic → struggle without the elevation clause.

---

## REPORT — Narrative layer

### REPORT-01 — Tone: positive-dominant, negatives probabilistic 🔒
- **Statement (Machan)**: in the report, we boost the positive possibilities more, and tell
  negative happenings only ~20% — and that too with a probabilistic arrival, saying
  *irukkalaam, nadakkalaam, gavanam* (may be / may happen / take care) — so that it gives a
  good feel to the candidate.
- **Logic**:
  ```
  POSITIVE / MIXED content → affirmative, encouraging phrasing; dominates narrative (~80%)
  NEGATIVE content        → capped ≈20% of narrative weight;
                            ALWAYS soft probability modals + vigilance guidance;
                            NEVER deterministic doom statements
  Applies to all cost/risk emissions (NBR-02 uyir cost, future vedha-type warnings, etc.)
  ```
- **Example**: an NBR-02 uyir-cost line renders as "oru uyir karakatvam vilaga-nadakkalaam;
  gavanam — porul paagam valam serum" — never "you will lose X."
- **Strengthened standard (Machan, 2026-10-31) — applies globally**: natal profiles,
  dasha-bhukti interpretations, Rahu–Ketu transit reports and question-specific
  predictions alike.
  - **Positive communication**: give greater narrative emphasis to constructive
    developments, favourable possibilities, opportunities and positive outcomes;
    explain how the native may **benefit** from the planetary and bhava influences;
    use reassuring, respectful, encouraging language throughout.
  - **Negative communication**: mention adverse possibilities only when supported by
    the rules; keep warnings proportionate and substantially **less prominent** than
    the constructive interpretation; NEVER use frightening, threatening, discouraging
    or emotionally distressing language; never present uncertain negative possibilities
    as guaranteed events; convert every negative into **practical, gentle caution**.
    Preferred register: *"கவனமாகச் செயல்படுவது நல்லது"* · *"இது போன்ற மாற்றங்கள் ஏற்பட
    வாய்ப்புள்ளது"* · *"சற்று சுதாரித்துச் செயல்பட்டால் சாதகமாகக் கையாளலாம்"* ·
    *"இந்தக் காலகட்டத்தில் பொறுமை உதவியாக இருக்கும்."*
  - **Absolute constraint**: never hurt, frighten, shame, discourage or unnecessarily
    distress the native; the report must never leave the native feeling hopeless or
    helpless. Equally — do not fabricate positive predictions or suppress important
    rule-supported cautions: communicate them with empathy, proportion and practical
    guidance.

---

## RAHU–KETU CONTACT LAYER (per Machan, 2026-10-31)

### RKT-01 — Planetary contact activation (umbrella rule) 🔒
- **Statement (Machan)**: when a transiting node conjoins a natal planet, it activates the
  planet through **two dimensions simultaneously** — its natural significations
  (naisargika karakatvam: what the planet *is*) and its functional lordships for that
  lagna (what the planet *owns*).
- **Logic**: `contact_reading(P) = natural_karakatva(P) + lordship_houses(P, lagna)`
  → both channels narrate; the domain lens selects which channel leads.
- **Example**: Rahu × Moon for Thulam lagna → natural channel: mother, mind, emotions,
  water, mental well-being · functional channel: 10th lordship → career, authority,
  professional standing. (This formalizes what the 14 rahu-ketu.md templates already encode;
  RKT-01 is their parent rule.)

### RKT-02 — Contacted-planet dasha amplification 🔒
- **Statement (Machan)**: a transit contact peaks when the running dasha hierarchy is
  connected to the planet being touched — i.e., **the contacted planet IS (or rules) the
  running Maha Dasha or Bhukti**.
- **Logic**: `if contacted_planet ∈ {MD_lord, bhukti_lord} → that contact's window reads
  one grade louder; timeline language marks it as the contact's peak.` v1 scope: **MD ×
  bhukti only** — Antara/Sookshma levels deferred to v2 (with the KP sub-lord gate).
- **Example**: Rahu × Moon exact 2027-01-09 falls inside the Moon bhukti (→ 2027-04-11) →
  the mind/career-base surge is double-marked: contact AND period agree. Same for
  Rahu × Mars (2027-08-14) inside the Mars bhukti (2027-04-11 → 2028-03-17).

### RKT-03 — Unoccupied-house transit = mild, house-level only 🔒
- **Statement (Machan)**: when a node transits a house holding **no natal planet**, it
  produces relatively mild developments through the house's general significations only.
  Occupants, when present, add their natural + functional channels on top.
- **Logic**: `if transited_house.occupants == ∅ → house-level reading, mild intensity;
  else → house reading + per-occupant contact channels (RKT-01).`
- **Example**: transit Ketu holds Katakam (10th from Lagna) which is **empty** → Ketu leg
  reads mild: general 10th-house detachment/quiet re-reading of career title — no
  per-planet contact events on the Ketu side of this window.

### RKT-04 — Incoming benefic aspects on transit Rahu 🔒
- **Statement (Machan)**: benefic aspects falling ON the transiting node modify its
  influence positively — Jupiter: guidance, expansion, constructive opportunity · Venus:
  harmony, comfort, favorable turns · waxing Moon: supportive emotional/circumstantial
  weather. Interpret in the context of the aspecting planet's **strength and functional
  nature**.
- **Logic**: `benefic_aspects(transit_node_sign, natal_chart)` — for each aspecting
  benefic: `modifier = f(dignity(aspector), functional_tier(aspector))`. **Direction
  guard**: this is INCOMING aspects onto the transited sign — the locked "node aspects
  OFF" rule governs the node's OUTGOING aspects; the two do not conflict.
- **Example**: in the sample chart **no natal benefic aspects Makaram** → RKT-04 stays
  dormant in the Dec-2026 showcase (sample verdicts are NOT inflated by it). Contrast
  case: had Jupiter aspect transit Rahu on the 4th, property/residence efforts would read
  constructive.
- **Integration clause (Machan, 2026-10-31)**: when Jupiter, Venus or the waxing Moon
  holds a beneficial conjunction/aspect relationship with the transiting node,
  evaluate the benefic's strength and functional nature (FUNC-01, STRENGTH-01) and
  read through its karakatvam + adhipathiyam: **Jupiter → guidance, expansion,
  direction · Venus → harmony, comfort, favourable associations · waxing Moon →
  emotional and circumstantial support**. Register: encouragement toward constructive
  effort and favourable possibilities — **never an automatic guarantee of a positive
  event** (event support remains a DBAS question — GATE-02).

### RKT-05 — Ketu reduction principle (+ malefic-suppression clause) 🔒
- **Statement (Machan)**: Ketu reduces, detaches, restricts or minimizes the
  manifestations of the house it transits and the planets it contacts. **Special clause**:
  when Ketu contacts a *naturally malefic* planet, it suppresses that planet's adverse
  characteristics (its poison is reduced).
- **Logic**: `ketu_contact(P): if P.nature == NATURAL_MALEFIC → harm-suppression reading;
  else → reduction/detachment reading over P's natural + functional channels.`
- **Example**: a Ketu × Mars contact reads as *reduced heat/conflict expression* (malefic
  harm suppressed), whereas Ketu × Venus would read as detachment from comfort/alliance
  themes. (No Ketu contacts exist in the Dec-2026 showcase — Katakam is empty; rule fires
  on future windows.)

### RKT-06 — Chronological multi-planet transit aggregation 🔒
- **Statement (Machan)**: when a node transits a sign holding **multiple natal planets**,
  each contact is evaluated **independently** — its natural karakatvam, its functional
  lordships for that lagna, the house it occupies, and its dasha-bhukti connection
  (RKT-02). These individual readings are then combined into **one chronological
  narrative** ordered by each natal planet's exact degree and the node's retrograde
  walk. The report must say what **each** contact activates, which life areas move or
  churn, and **how the influence evolves as the node progresses from one planet to the
  next — without losing any single contact's own significance or timing.**
- **Logic**:
  ```
  for each natal planet P in a transited sign (both nodes):
      reading(P) = RKT-01(P) channels + occupied_house(P) + RKT-02(P) dasha check
      window(P)  = ORB-02 curve → rise_begins / exact_peak / fully_released
  contact_order = sort by exact_peak date
                  (= descending natal degree, since the mean node walks backward)
  narrative = stitch in contact_order — each contact keeps its own dates, channels,
              and peak; no merging, no averaging, no dropping
  ```
  - **Overlap clause**: resolved by **RKT-07** (Machan's ruling, 2026-10-31) — when
    window(P_i) overlaps or adjoins window(P_i+1), the two contacts are narrated as
    **one continuous period with two named currents** (fading previous + approaching
    next), never as isolated events, never merged.
  - **Equal-degree / near-degree contacts (Machan, 2026-10-31)**: if two natal planets
    occupy **exactly the same degree**, both activate **simultaneously** — both natural
    significations and both functional lordships are narrated, including the case where
    one is functionally benefic and the other functionally malefic (both influences
    communicated). If their degrees differ only by minutes, preserve the actual
    chronological order and contact timings. **Never impose an artificial priority
    merely because two planets are very close.**
  - **Scope guard**: RKT-06 governs the **chronological transit narrative** (the
    "what happens, when" story — REPORT-FLOW step 3). The domain lens's
    relevance-ranked **lead contact** for the question answer (REPORT-FLOW steps 6–7)
    is a separate selection and is not overridden by this rule.
- **Example** (sample chart, Rahu through Makaram — four contacts stitched as one
  ~11-month season, each independently read):
  | Order | Contact | Own dates (rise → **peak** → release) | Activates | Dasha link |
  |---|---|---|---|---|
  | 1 | Rahu × **Moon** (28°12′) | 14-Nov-26 → **09-Jan-27** → 26-Feb-27 | mind, mother · **10th lord → career base** | own bhukti (→ Apr-27) — RKT-02 double-mark |
  | 2 | Rahu × **Venus** (22°23′) | 04-Mar-27 → **29-Apr-27** → 16-Jun-27 | comfort, alliance · **1st & 8th lord** | none — falls in Mars bhukti |
  | 3 | Rahu × **Saturn** (19°23′) | 29-Apr-27 → **25-Jun-27** → 11-Aug-27 | structure, grind · **4th & 5th lord, yogakaraka landlord** | none |
  | 4 | Rahu × **Mars** (16°43′) | 19-Jun-27 → **14-Aug-27** → 01-Oct-27 | drive, property · **2nd & 7th lord, exalted** | own bhukti (Apr-27 → Mar-28) — RKT-02 double-mark |
  Note the overlaps the clause must handle: Saturn's rise **begins the same day Venus
  peaks** (29-Apr-27), and Mars's rise (19-Jun-27) opens while Saturn is still
  separating. The narrative reads: career-base surge crests in January → hand-off →
  self/comfort-and-sudden-change channel through spring → the landlord's grind joins
  in late April and crests in late June → the exalted Mars drive joins in June and
  peaks mid-August — **four dated peaks, one continuous story.**

### RKT-07 — Sequential planetary contact transition 🔒
- **Statement (Machan)**: when the node moves from one natal planet's contact zone
  toward the next, the report describes the transition as a **continuous sequence of
  planetary influences**. The native experiences the significations (karakatvam) and
  functional lordships (adhipathiyam) of the planet the node is **moving away from**,
  while progressively approaching the influence of the next. The report must:
  1. explain the **ongoing/concluding** influence of the previous planet — natural
     significations + functional lordships;
  2. explain the **emerging** influence of the next planet — natural significations +
     functional lordships;
  3. present both as **the same chronological period**, clearly distinguishing the
     **fading** current from the **approaching** current;
  4. preserve **both** contacts' individual windows and peak dates (per RKT-06);
  5. **never assume** two planets need identical degrees or shared exact dates for
     their influences to be experienced within the same period.
  **Core principle**: the native lives the transition as a *continuous progression*,
  not as two isolated events.
- **Logic**:
  ```
  transition(P_prev, P_next):
      fading  = P_prev over (exact_peak → fully_released)   # concluding register
      rising  = P_next over (rise_begins → exact_peak)      # emerging register
      if fading ∩ rising ≠ ∅  OR  the two windows adjoin inside one contact season:
          narrate ONE period with TWO named currents:
            - fading current: P_prev karakatvam + lordships, "winding down" language
            - rising current: P_next karakatvam + lordships, "gathering" language
          print BOTH windows and BOTH peak dates verbatim (RKT-06 preservation)
      no degree-equality requirement: overlap or mere adjacency triggers the
      transition narrative — identities never merge, no contact is ever dropped
  ```
- **Rising/fading intensity communication (Machan, 2026-10-31)**: transitions are
  described with **ORB-02 intensities** — e.g., *"Venus influence ≈30% and fading;
  Saturn influence ≈70% and rising"* — the next planet named the **dominant emerging**
  influence, the previous one the **diminishing** influence. The narrative must convey
  the progressive reduction of one current and the progressive increase of the next.
  (These percentages are **computed from the deterministic ORB-02 curve** — they
  describe transit intensity only, never event probability; see GATE-02.)
- **Example** (sample chart, the Venus→Saturn hand-off, late April 2027): Rahu × Venus
  (comfort, alliance · lagna & 8th lord) crests **29-Apr-27** and begins its fade
  (release ≈ 16-Jun-27) — *on that same day* Rahu × Saturn's rise begins (structure,
  grind · 4th & 5th lord, yogakaraka landlord), gathering toward its **25-Jun-27**
  peak. The report reads this stretch as one period: the self/comfort-and-sudden-change
  current concluding while the landlord's structure-and-property current gathers —
  two named currents, both dated, one continuous experience. Same pattern at the
  Saturn→Mars hand-off: Mars's rise opens 19-Jun-27 while Saturn is still separating
  (release 11-Aug-27), and Mars's own peak lands 14-Aug-27 — three days after Saturn
  fully releases.

### RKT-08 — Nakshatra-lord governance of a transit segment 🔒
- **Statement (Machan)**: when Rahu or Ketu travels through a nakshatra **without
  directly contacting a natal planet**, the **nakshatra lord governs** the
  interpretation of that transit segment. Evaluate the lord's natal profile AND its
  current transit profile as **separate activation channels**.
- **Logic**:
  ```
  segment_reading(star):
      L = nakshatra_lord(star)
      A. natal channel   = karakatvam(L) + lordships(L, lagna)
                           + natal_house(L) + natal_dignity(L) & conditions
                                                              # SIGN / FUNC / DIGN
      B. transit channel = transit_house(L, t) + transit_dignity(L, t)
                           + transit conjunctions & aspects on L
                           + benefic/malefic modifiers on L    # STRENGTH / RKT-04
      C. activation      = A.natural + A.lordships + A.natal_house + B.transit_house
                           — natal and transit placements narrated as distinct channels
      D. effectiveness   = 1.0
         if L debilitated in natal chart OR in transit chart (or both):
             effectiveness = 0.5     # applied ONCE — debilitated in BOTH charts
                                    # is still 50%, never 75% or 100%
             ⇒ lord's significations/lordships deliver with REDUCED
               qualification/status — NEVER a cancellation of the transit
             if neecha_bhanga(L): apply NBR-01/NBR-02 as-is (initial struggle /
               reduced qualification → subsequent improvement, recovery, elevation);
               do NOT invent a separate neecha-bhanga mechanism
         else: modulate per existing DIGN / STRENGTH cards
  ```
- **Dependencies**: SIGN-01…05, FUNC-01, DIGN-01, STRENGTH-01, NBR-01/02, QUAL-01;
  runs on the factor-D sub-period spine (REPORT-FLOW step 4).
- **Data dependency ⛔ (GK-13)**: clause B requires **full transit graha positions**
  across the window — today's transit JSON carries node positions only. The rule logic
  is locked; the feed is an implementation dependency (touches the GK-09 input
  contract).
- **Example (Machan's)**: Rahu travels through Uttara Phalguni with no natal-planet
  contact → lord = **Sun**. Evaluate Sun's natural significations, functional
  lordship, natal house, current transit house, transit dignity, conjunctions and
  aspects. If Sun is debilitated in transit → **50% reduction** of Rahu's
  nakshatra-mediated operational effectiveness: e.g., efforts involving senior
  authorities or leadership proceed, but the level of authority, recognition or
  effectiveness achieved reads reduced. **Do not conclude that Rahu becomes completely
  ineffective.** If Jupiter conjoins Sun, fold the Jupiter influence in through the
  existing aspect/conjunction/strength rules (RKT-04 family).
- **Example (sample chart)**: after the Mars contact fully releases (01-Oct-27), Rahu
  walks the rest of Makaram with no natal contact — **Thiruvonam/Shravana** leg (lord
  **Moon**: 10th lord seated in the 4th, digbala) until ≈19-Dec-27, then
  **Uthiradam/Uttarashada** leg (lord **Sun**: 11th lord seated in the 5th, Kumbham)
  until exit 25-Jun-28. Those months read through the Moon's and Sun's channels —
  career-base and gains/network themes mediated by the star lords, not by direct
  contact. (Neither is debilitated natally here; transit-side evaluation awaits the
  GK-13 feed.)

### RKT-09 — Nakshatra-lord activation during inter-contact gaps 🔒
- **Statement (Machan)**: when Rahu has moved away from one natal planet and has not
  yet entered the next planet's contact window, the intervening period is **not an
  inactive or empty period**. Evaluate the nakshatra the node is travelling through —
  apply **RKT-08** in full. The report must: identify the currently transited
  nakshatra and its lord; evaluate the lord's natal and transit house placements;
  activate its natural significations and functional lordships; evaluate its dignity
  and planetary associations; and check DBAS connections. The report keeps the two
  influence kinds **distinct**: direct natal-planet contact influence
  (RKT-01 / RKT-06) vs nakshatra-lord-mediated influence (RKT-08 / RKT-09) — both may
  be part of the same continuous transit narrative.
- **Logic**:
  ```
  for each gap between consecutive contact windows
      (also: before the first rise and after the last release inside the sign):
      star   = nakshatra transited during the gap
      reading = RKT-08(star) + DBAS connection check (RKT-02 v1 scope: MD × bhukti)
      narrate as the season's connective tissue — lower volume than a direct
      contact, never silent
  ```
- **Example (sample chart)**: the six-day bridge between the Moon release
  (26-Feb-27) and the Venus rise (04-Mar-27): Rahu sits in **Avittam/Dhanishta**, lord
  **Mars** — natally exalted in the 4th, 2nd & 7th lord → the gap reads as a mild
  Mars-mediated undertone (drive, earnings, alliance themes stirring) connecting the
  Moon chapter to the Venus chapter — not a blank week. The long post-Mars tail
  (01-Oct-27 → exit 25-Jun-28) is RKT-09 territory throughout: Shravana→Uttarashada
  star-lord mediation (see the RKT-08 sample-chart example).

### ORB-02 — Degree-based asymmetric contact curve 🔒 (replaces the ≤3°/≤5° symmetric orbs)
- **Statement (Machan)**: nodal influence is computed by degrees — it **begins when the
  node nears 3° before the natal planet, peaks at the exact crossing, and the moment the
  node crosses the planet (even by 1') severity starts reducing; it is completely gone
  once the node is 2.5° past the planet.** This curve must drive both the readings and
  the timeline language.
- **Logic** (mean node walks retrograde, so it approaches from the higher degree):
  ```
  window_start = natal_degree + 3°      (applying edge — rise begins)
  exact_peak   = natal_degree           (maximum)
  window_end   = natal_degree − 2.5°    (separating edge — fully released)
  At 0.05295°/day: rise ≈ 57 days · fade ≈ 47 days · total ≈ 104 days per contact
  intensity(t) = ramp-up over applying 3° → 100% at exact → ramp-down over separating 2.5°
  ```
- **Example**: Rahu × Moon (natal 28°12'): window opens ≈ **2026-11-14** (node at
  1°12' Dhanus — *the rise crosses the sign border*), peaks **2027-01-09**, fully
  released ≈ **2027-02-26**. Timeline line: "mid-January the Moon touch is at its peak;
  by end-February it has fully released."
- **Sign-boundary independence (Machan's ruling, 2026-10-31 — RESOLVES GK-12)**: the
  degree-based curve operates **independently of sign boundaries** — a contact's
  influence can begin even before the node enters the sign the natal planet occupies.
  (Natal Moon 28°12′ Makaram: Rahu begins influencing her while still in Dhanus, once
  inside the 3° applying orb.)
  - **Early-influence register**: window openings read as **mild / gradually
    emerging** — probabilistic phrasing only ("may begin to experience", "subtle
    changes may become noticeable", "early indications may appear"). Never describe
    full contact intensity as already active at the start of the applying window.
  - **Traditional duration guidance** (explanatory only — never a replacement
    calculation): Rahu's ≈1.5-year transit → influence may begin ≈1.5 months earlier ·
    Saturn's ≈2.5-year transit → ≈2.5 months earlier · Jupiter's ≈1-year transit →
    ≈1 month earlier. The degree-based curve above remains the actual implementation
    mechanism.

---

## NATAL PROFILE LAYER (per Machan's Report Framework, 2026-10-31)

*The report opens by establishing WHO the native is before any transit reading
(Half 1 of the template — see `REPORT-TEMPLATE.md`). All three cards are pure KB
lookups against `foundations/` — deterministic, chart-generic, reusable.*

### PROF-01 — Lagna analysis (who you are, base layer) 🔒
- **Statement (Machan)**: identify the Ascendant; read the characteristics and natural
  attributes of that Ascendant; interpret the general personality and fundamental
  tendencies it represents.
- **Logic**: `profile_base = rasis.md[lagna_sign].character_bank` → personality and
  tendency paragraph.
- **Example**: Thulam lagna → Venus-ruled movable air sign → balance-seeking,
  partnership-oriented, diplomatic, aesthetic sense, weighs both sides before acting.

### PROF-02 — Lagna nakshatra analysis (nature & behavior layer) 🔒
- **Statement (Machan)**: identify the nakshatra occupied by the Ascendant degree; read
  the star's characteristics and its ruling planet; interpret how it shapes the native's
  fundamental nature and behavioural tendencies.
- **Logic**: `profile_nature = nakshatras.md[star_of(lagna_degree)] + star_lord.nature`
- **Example**: lagna 17°51' Thulam = **Swati pada 3, lord Rahu** → independence,
  self-made movement, trade/commerce flavor, adaptability. Carried note: the lagna star
  lord being **Rahu himself** makes any Rahu–Ketu transit personally loud for this
  native — the report's protagonist rules her rising star.

### PROF-03 — Lagna lord placement (life-gravitation layer) 🔒
- **Statement (Machan)**: identify the Lagna Adhipathi and the house it occupies; read
  that house's significations; interpret the native's primary life focus, interests and
  areas of inclination. The lagna lord's house shows where the native naturally
  gravitates and devotes greater attention.
- **Logic**: `profile_focus = bhavas.md[house_of(lagna_lord)]`, modulated by the
  lagna lord's own condition (dignity + company, per SIGN/NBR cards).
- **Example**: lagna lord **Venus in the 4th** (Makaram stellium, with own-sign
  yogakaraka Saturn + exalted Mars) → life gravitation: home, property, mother,
  domestic foundation — built with structural strength. Template note: this layer
  pre-frames the transit reading (here the transit lands ON the 4th — the report's
  two halves connect by themselves).

---

## Domain lens seeds — kelvikkaana bavagangal (per Machan, 2026-10-30)

| Domain | Core bhavas | Modifier bhavas → added flavor |
|---|---|---|
| Career | 2, 6, 10 | +11 → career with good profits · +3 → consulting background & micro-travels · +7 → offshore money, offshore partnership, partner/wife involvement |

(Other domains to be seeded as their rule sessions happen.)

---

## Pending / in discussion
- **Uyir/porul karakatva split table** (9 grahas) — draft table presented to Machan, awaiting
  his corrections from practice (NBR-02 dependency; boundary faculties handled contextually).
- **Contact-rules module** (factor B) — RULE CARDS COMPLETE (RKT-01…09 locked 2026-10-31);
  engine gaps queued: chronological event ordering (RKT-06), fading/rising transition
  frames with ORB-02 intensity lines (RKT-07), star-lord segment evaluation (RKT-08/09).
- **RKT-08 clause-B data feed (GK-13)** — full transit graha positions needed for the
  nakshatra lord's transit house/dignity/conjunctions; transit JSON today = nodes only.
- **Mars-vs-Moon headline ruling** — Machan to rule after reading
  `validation/sample_career_report.html` (career-lens lead-contact question).
- **KP sub-lord gate** — deferred to v2 (80/20 parambariya lock); SIGN-02/03 chain retained;
  no Antara/Sookshma amplification until v2 rules approved (GATE-02 scope note).

# BHAVAS.md — The 12 Houses, Encyclopedic

---

## GLOSSARY — Rule ID prefixes used in this file

> Master table: `rule-engine/RULES.md` → GLOSSARY. Only the prefixes used in this file are listed below.

| Prefix | விரிவாக்கம் | எதைக் குறிக்கிறது? |
|---|---|---|
| SIGN | Signification | கிரகங்கள் எதைக் குறிக்கின்றன, எந்தப் பாவங்களை வழங்குகின்றன |
| BHAVA | Bhava | பாவங்களின் தன்மை மற்றும் பலன்களின் வகை |
| GATE | Question Gate | கேள்விக்குரிய பாவங்கள் மற்றும் பலன் தீர்மானம் |
| DIGN | Dignity | உச்சம், நீசம், ஆட்சி போன்ற கிரக நிலைகள் |
| FUNC | Functional Nature | லக்ன அடிப்படையிலான சுபர் / பாவர் தன்மை |
| NBR | Neecha Bhanga Resolution | நீசபங்கம் மற்றும் அதன் விளைவுகள் |
| QUAL | Quality | நட்சத்திர சாரம் மூலம் கிடைக்கும் பலன்களின் தரம் |
| REPORT | Report Generation | அறிக்கை உருவாக்கும் விதிகள் |

---

> **source**: classical base (BPHS / Phaladeepika / Jataka Parijata / parambariya bhava
> lore) + Machan's practice corrections
> **status**: DRAFT — awaiting Machan's line-by-line practice corrections
> **consumed-by**: GATE-01 (kelvikkaana bavagangal live here), factor A (axis house
> placement — from Moon PRIMARY, from Lagna SECONDARY), BHAVA-01/02/03 (textures),
> SIGN-01 (occupancy house = rank-1 delivery), SIGN-04 (tenant suppression), domain
> lens configs, report template stitcher
> **standard**: encyclopedic, ultra-deep, general-purpose, chart-agnostic. Written ONCE;
> reusable by any future module (transit, natal, prasna, muhurta, matching). Worked
> examples are *illustrative only* — the engine never absorbs them.
> **sibling files**: kelvigal.md (which questions pull which bhavas) · grahas.md ·
> nakshatras.md · rasis.md · RULES.md (the rule cards that read this file)

---

## How to read a bhava entry

Each bhava carries, in fixed order:

1. **Data line** — Sanskrit + Tamil names, classification tags (kendra / trikona /
   dusthana / upachaya / maraka / panaphara / apoklima), purushartha (BHAVA-03),
   texture (BHAVA-01/02), kala-purusha body zone, naisargika karaka grahas, viruddha
   bhava (12th-from). Pure data; this is what the engine reads.
2. **Texture** — what this bhava *is* and how it delivers.
3. **Holds / Corrupts** — the supported vs afflicted behavior banks.
4. **Karakatvas** — numbered, grouped (People / Places / Matters & events / Body).
   Cite corrections by bhava + number (e.g., "4th #21").
5. **Viruddha relation** — the 12th-from semantics: what dissolves this bhava, and
   what this bhava dissolves.
6. **Transit (factor A)** — Rahu and Ketu through this house, from Moon (PRIMARY)
   and Lagna (SECONDARY), with the locked favorability flag.
7. **Kelvigal pull** — every question card (kelvigal.md) that holds this bhava in
   core / modifier / viruddha. This is the reverse index GATE-01 reads.
8. **Worked example** — only for bhavas occupied/transited in the sample chart
   (3, 4, 5, 6, 9, 10, 11). Illustrative only.

**Conventions**: whole-sign houses (locked) — bhava = rasi counted from the reference
point (lagna or Moon). Cuspal / KP bhava-chalit and the sub-lord gate are deferred to
v2 (80/20 parambariya lock). Where parambariya schools disagree, the item is tagged
**[school note]** for Machan's ruling.

---

## The classification grid (all 12 at a glance)

| # | Name (Skt · Tamil) | Angular class | Special class | Purushartha | BHAVA texture | Body zone | Karaka graha(s) | Viruddha |
|---|---|---|---|---|---|---|---|---|
| 1 | Tanu · Udayam/Lagna | kendra | + trikona (dual) | DHARMA | material + heart (dual) | head | Sun | 12 |
| 2 | Dhana · Panam/Kudumbam | panaphara | maraka | ARTHA | magnitude | face/right eye/mouth | Jupiter | 1 |
| 3 | Sahaja · Sodaram | apoklima | upachaya | KAMA | growth-through-effort | ears/throat/shoulders/arms | Mars | 2 |
| 4 | Sukha · Veedu | kendra | — | MOKSHA | material + inner peace | chest/heart/lungs | Moon, Venus, Mercury | 3 |
| 5 | Putra · Santhanam | panaphara | trikona | DHARMA | heart/meaning | stomach/upper abdomen/back | Jupiter | 4 |
| 6 | Ripu · Roga/Satru | apoklima | dusthana + upachaya | ARTHA | pressure that matures | navel/intestines | Mars, Saturn | 5 |
| 7 | Kalatra · Kalathiram | kendra | maraka | KAMA | material union | pelvis/uterus/bladder | Venus | 6 |
| 8 | Ayus · Aayul/Maranam | apoklima | dusthana | MOKSHA | depth/suddenness | genitals/excretory | Saturn | 7 |
| 9 | Bhagya · Baakiyam/Dharmam | apoklima | trikona | DHARMA | heart/meaning | hips/thighs | Jupiter, Sun | 8 |
| 10 | Karma · Thozhil/Virthi | kendra | upachaya | ARTHA | material/status | knees/spine | Sun, Mercury, Jupiter, Saturn | 9 |
| 11 | Labha · Laabam | panaphara | upachaya | KAMA | gains arriving | calves/ankles/left ear | Jupiter | 10 |
| 12 | Vyaya · Virayam/Moksham | apoklima | dusthana | MOKSHA | release/dissolution | feet/left eye/sleep | Saturn, Ketu | 11 |

- **Kendra (1/4/7/10)** — BHAVA-01: material things and status; "anything that wouldn't
  fill the heart." More money/tangible magnitude than trikonas.
- **Trikona (1/5/9)** — BHAVA-02: anything that fills the heart — meaning, fulfillment.
  Less money, deeper significance. House 1 = both → dual texture.
- **Dusthana (6/8/12)** — the difficulty triad: pressure/depth/release. Delivery from
  these is real but costs; REPORT-01 governs rendering.
- **Upachaya (3/6/10/11)** — grows better with time; natural malefics placed or
  transiting here convert pressure into capacity. The "improves-with-age" set.
- **Maraka (2/7)** — death-inflicting capacity, read ONLY in ayus/longevity contexts;
  in money/marriage questions these two are simply wealth and partnership.
  **[school note: scope of maraka reading — Machan to confirm practice]**
- **Panaphara (2/5/8/11)** = succedent — consolidates what kendras start.
  **Apoklima (3/6/9/12)** = cadent — moves, dissolves, or transcends.

---

## The viruddha cycle (12th-from dissolves)

`viruddha(H) = 12th from H` (kelvigal.md global mechanics). Applied on the PRIMARY
core bhava of each question card. The full cycle:

```
1→12 · 2→1 · 3→2 · 4→3 · 5→4 · 6→5 · 7→6 · 8→7 · 9→8 · 10→9 · 11→10 · 12→11
```

Reading rule: **when the viruddha house is signified strongly while the core is weak,
the matter dissolves** — e.g., money questions (2) dissolve through the 1st (savings
drain to self-expenses); career (10) dissolves through the 9th (elevation becomes
transfer); marriage (7) dissolves through the 6th (partnership becomes litigation);
foreign stay (12) dissolves through the 11th (stay cut short, return with gain).
Each bhava entry below names its own dissolver AND what it itself dissolves.

---

## Axis pairs (core framing — locked: axis-first)

Rahu and Ketu are ONE axis: when Rahu occupies H, Ketu occupies H+6. Factor A always
reads the pair, never one node alone.

| Axis | Name | Combined meaning |
|---|---|---|
| 1/7 | self ↔ other | identity vs partnership; "who am I" vs "who is with me" |
| 2/8 | mine ↔ theirs | held value vs received value; family vs in-laws; savings vs windfall |
| 3/9 | effort ↔ grace | courage vs fortune; near journeys vs far; doing vs being carried |
| 4/10 | home ↔ world | private base vs public peak; peace vs position; mother-side vs authority-side |
| 5/11 | creation ↔ gain | self-expression vs network; children vs circle; the bet vs the payout |
| 6/12 | service ↔ dissolution | work/health/debt vs expense/moksha/foreign; the grind vs the release |

Every transit report's spine: name the axis the nodes currently occupy (from Moon
primary, from Lagna secondary), THEN read per-question through GATE-01. Factor A is
the BASE layer only — a "watch" house transit can still deliver POSITIVE for a
question whose core bhavas are DBAS+transit supported (e.g., the sample chart's C2).

---

## Bhavat-bhavam (derived houses) — the rotation principle

Any bhava read *from another bhava as if it were the lagna* yields the derived
meaning. The engine's family-rotation rule (kelvigal.md global mechanics) is one
application. Key derived readings used across the question cards:

- **8th = 2nd from 7th** → the spouse's family/vault = in-laws, spouse's money (R7, M8).
- **6th = 12th from 7th** → dissolution of partnership = dispute/litigation/divorce
  texture (R5, and why 6 is the viruddha of every marriage card).
- **11th = 6th from 6th** → the disease's own growth house turned to favor: the
  illness peaks and breaks (H6 recovery logic).
- **5th = 12th from 6th** → debt/disease dissolves (M6 loan-closure logic).
- **3rd = 12th from 4th** → peace/home displaced by movement (H5/M7/F6 viruddha).
- **9th = 12th from 10th** → position vacated (C7 job-loss leg; C2/C8 viruddha).
- **2nd = 12th from 3rd** → displacement cancelled, stay home (F1/F10 viruddha).
- **11th = 12th from 12th** → the drain plugs itself (M9/F2/F3/F4 viruddha).
- **4th = 12th from 5th** → speculation/conception postponed (M4/R6 viruddha).
- **Family rotation anchors**: 4 mother · 9 father · 7 spouse · 5 child · 3 younger
  sibling · 11 elder sibling (read that bhava, its lord, and its karaka as the
  relative's 1st).

---
---

# 1. FIRST BHAVA — Tanu · Udayam (Lagna)

**Data**: Classification **kendra + trikona (dual)** · Purushartha **DHARMA** ·
Texture **material + heart (dual — the only house that is both)** ·
Angular class **kendra (angular)** · Body zone **head/brain/complexion** ·
Naisargika karaka **Sun** · Viruddha **12** (12th-from: the self drains into
loss/isolation) · Tamil **Udayam / Thanusu bhavam**

**Texture**: The self as a whole — body, identity, vitality, the lens through which
every other house is experienced. All delivery in a chart is ultimately
1st-house-filtered: an event "happens to" the person the 1st describes. Being both
kendra and trikona, the 1st carries status AND meaning: the body is material; the
"who I am" is dharma. A strong 1st makes every other house's promise deliverable;
a broken 1st makes even good yogas arrive bent.

**Holds (supported)**: vitality · identity clarity · self-confidence · good
beginnings · physical robustness · personal magnetism · recovery capacity ·
fame of personality · independence
**Corrupts (afflicted)**: identity confusion · chronic low vitality · self-sabotage ·
fame turning notoriety · directionlessness · the body becoming the complaint ·
dependence disguised as caution

**Karakatvas**:

*People*: 1. the native himself · 2. the body-person others meet (first-impression
persona) · 3. the self as family member (one's seat in the kutumba) · 4. the leader
one becomes when no boss exists · 5. one's own physician (self-care capacity)

*Places*: 6. birthplace · 7. the place one currently inhabits · 8. "home ground" —
familiar territory where one is recognized · 9. the head-position of any gathering
(the front seat, the lead chair)

*Matters & events*: 10. birth itself · 11. naming/identity formation · 12. beginnings
of ALL ventures (every muhurta's first leg) · 13. personality & temperament ·
14. self-respect / personal dignity · 15. vitality & life-force baseline ·
16. health as a whole (the constitution) · 17. recovery from any illness ·
18. fame of person (being known for who one is) · 19. physical appearance & changes
to it · 20. complexion/bearing · 21. success by one's own strength (lagna-strength
wins) · 22. prosperity of the self · 23. happiness of the self · 24. childhood as a
whole · 25. longevity's foundation (the base 8th builds on) · 26. the present life
(vs past/future) · 27. the direction life currently faces · 28. self-employment /
independence capacity · 29. head injuries/ailments · 30. the moment of arrival
(every entrance one makes) · 31. reputation-at-first-sight · 32. personal choices —
the fork where no one else decides · 33. the body's signals (hunger, fatigue, pain
as messages) · 34. pride/self-regard · 35. the will to live

*Body*: 36. head · 37. brain/skull · 38. hair-line and forehead · 39. face as identity
(recognition) · 40. overall constitution/immunity baseline

**Viruddha relation**: 12th-from-1 = **12th** — the self dissolves into expense,
isolation, hospitalization, foreign lands: when the 12th dominates the 1st, the body
drains and identity blurs (H1/H6 viruddha watch). Reverse: 1 is 12th-from-**2** —
strong self-signification dissolves savings: money converts into self-expenses,
self-image, the body (M1/M2/M10/F9 viruddha logic).

**Transit (factor A)**:
- **Rahu through the 1st (from Moon — PRIMARY)**: mental unrest, fear-complex,
  identity restlessness, reputation attacks, health dips with hard-to-name causes;
  the native questions who he is and wants to become someone else. ⚠ watch —
  NOT in the locked favorable set. From **Lagna (SECONDARY)**: same texture one
  octave more external — image churn, role ambiguity others can see.
- **Ketu through the 1st**: self-effacement, detachment from image, spiritual turn,
  vague low-energy health; the native withdraws from self-promotion. ⚠ watch —
  not in Ketu's locked favorable set (3/6/11).
- Axis context: Rahu-in-1st ⇔ Ketu-in-7th (partnership detachment co-runs);
  Ketu-in-1st ⇔ Rahu-in-7th (partnership obsession co-runs).

**Kelvigal pull** — core: C7 (job loss = 1st leg of the 12th-from set), H1, H6 ·
modifier: H2 (+1 body visibly weakens), H7 (+1 flare touches the body) ·
viruddha-on: C1, M1, M2, M10, F9 (each watches "strong 1st = the matter drains
into the self") · rotation anchor: the reference frame for every family question.

*(No worked example — sample chart's 1st house, Thulam, is empty; its lord Venus
sits in the 4th stellium with digbala: the self is delivered through the 4th's
engine room. See the 4th bhava example.)*

---

# 2. SECOND BHAVA — Dhana · Panam / Kudumbam

**Data**: Classification **panaphara (succedent)** · Special **maraka** (with 7) ·
Purushartha **ARTHA** · Texture **magnitude — the vault** · Body zone
**face / right eye / mouth / teeth / tongue** · Naisargika karaka **Jupiter** ·
Viruddha **1** (savings drain to self) · Tamil **Panam / Kudumba sthanam**

**Texture**: What you HOLD. The 2nd is accumulation in every form: money in the
account, family around the table, food in the mouth, words on the tongue, values in
the blood. Where the 11th is money *arriving*, the 2nd is money *staying*. It is
also the kutumba — the family-as-unit one belongs to and feeds. Maraka capacity is
dormant data, read only in longevity contexts — never in money questions.

**Holds**: accumulation instinct · truthful measured speech · family cohesion ·
nutritive discipline · financial prudence · value clarity (knowing what things are
worth) · the dignified family name
**Corrupts**: hoarding or leaking (no middle) · harsh/lying speech · family rupture ·
food disorders · money anxiety despite balance · values for sale · teeth/face/eye
complaints

**Karakatvas**:

*People*: 1. family members (the kutumba) · 2. spouse-as-family-member (absorbed
into the 2nd after marriage) · 3. the family lineage/ancestry line · 4. bankers and
money-handlers · 5. those who feed you (cooks, providers) · 6. dependents one feeds

*Places*: 7. banks · 8. treasuries/vaults · 9. granaries/stores · 10. dining spaces ·
11. the family home (lineage side) · 12. jewelry lockers

*Matters & events*: 13. accumulated wealth / net worth · 14. bank balance & savings ·
15. movable assets (cash, stocks, gold) · 16. food & eating habits · 17. speech —
quality, content, truthfulness · 18. family values / sanskara · 19. early & primary
education · 20. rote learning / memory banks · 21. jewelry & precious metals held ·
22. financial values (what one believes money is FOR) · 23. family honor & standing ·
24. disputes/ruptures within family · 25. second-marriage family formation
**[school note: debated — held in R8's core via 8/11; Machan to rule]** ·
26. self-earned income retained (vs 11 = arriving) · 27. the tongue's karma (words
that cost or earn) · 28. face/eye/teeth health events · 29. receiving money that
STAYS · 30. family expansion events (a birth/absorption into the kutumba) ·
31. litigation within family over assets · 32. the will to accumulate · 33. dietary
discipline as health lever · 34. ornaments worn (status through the 2nd) ·
35. documents of holding (passbooks, deposit receipts)

*Body*: 36. face · 37. right eye · 38. mouth · 39. teeth · 40. tongue · 41. speech
organs (vocal apparatus)

**Viruddha relation**: 12th-from-2 = **1st** — the vault drains into the self
(self-expenses, image, body). Reverse: 2 is 12th-from-**3** — strong holdings cancel
displacement: the native stays home, the move is postponed (F1/F10 viruddha logic:
"displacement cancelled").

**Transit (factor A)**:
- **Rahu through the 2nd (from Moon)**: financial anxiety, income fluctuations,
  harsh speech slipping out, family friction, food/face/dental complaints; hunger
  for more without satisfaction. ⚠ watch. From **Lagna**: visible money churn —
  salary/structure changes, family events with expense.
- **Ketu through the 2nd**: detachment from accumulation, speech turns sparse but
  penetrating, family distance, disinterest in hoarding; savings quietly redirected
  toward meaning. ⚠ watch.
- Axis context: Rahu-in-2nd ⇔ Ketu-in-8th (others' money detaches while yours
  agitates); Ketu-in-2nd ⇔ Rahu-in-8th (inheritance/sudden-gains hunger co-runs).

**Kelvigal pull** — core: C1, M1, M2, M7, M8, M10, R1, R3, R6, F6, F9 ·
modifier: C2, C4, C6, C10, M3, M4, M6, H5, H9, R2, R5, R8, R9, F3, F4 ·
viruddha-on: C10 (venture starved of cash), F1, F10 (displacement cancelled) ·
**the single most-pulled bhava in the money & marriage domains.**

**Worked example (sample chart)**: 2nd house = **Vrichikam, empty**; 2nd lord =
**Mars, exalted in the 4th** (Ruchaka). Empty house + exalted lord → ownership
delivery at 100% (SIGN-04) with thagudhi-grade status (DIGN-01): the vault is
structurally enormous and converts into 4th-house form — property, vehicles, home.
Moon-bhukti chain {4,2,7,10} hits the 2nd via Mars-ownership → the current window
delivers 2nd-house results (money held, family matters) at full strength (M1
POSITIVE's DBAS leg). From Moon: 2nd-from-Moon = **Kumbam, holding the Sun** —
wealth from the Moon-frame carries authority/government/status texture (Sun = 11th
lord of the lagna chart sitting in the Moon's wealth house: income tied to position
and networks). Viruddha watch: the 1st (Thulam, empty, lord Venus in 4th) is not
the running theme → savings are not draining to self this window.

---

# 3. THIRD BHAVA — Sahaja · Sodaram

**Data**: Classification **apoklima (cadent)** · Special **upachaya** · **[mild
dusthana — school note: some paramparas count 3 among dusthanas; Machan to rule]** ·
Purushartha **KAMA** · Texture **growth-through-effort — nothing given, everything
taken** · Body zone **ears (right) / throat / neck / shoulders / arms / hands** ·
Naisargika karaka **Mars** · Viruddha **2** · Tamil **Sodara sthanam**

**Texture**: The house of SELF-EFFORT. Courage, initiative, the younger sibling
band, short journeys, skills of the hand, the voice you broadcast. As upachaya, the
3rd *improves with time* — natural malefics here (natal or transit) convert pressure
into capacity; the older the native, the stronger this house delivers. The 3rd is
also displacement: the first step away from the 4th's home — which is why it heads
the foreign-travel core (F1) and why it dissolves domestic peace (viruddha of 4).

**Holds**: courage that compounds · initiative · skill acquisition · productive
restlessness · supportive siblings · the well-timed bold move ·
communication that lands
**Corrupts**: recklessness · sibling friction · scattered effort · noise without
signal (endless messaging, no message) · short-trip exhaustion · ventures started,
none finished

**Karakatvas**:

*People*: 1. younger siblings · 2. neighbors · 3. teammates · 4. assistants/helpers ·
5. the local network · 6. colleagues at arm's length · 7. messengers/intermediaries

*Places*: 8. the neighborhood · 9. short-travel routes/commutes · 10. workshops &
studios · 11. training grounds/gyms · 12. media houses/press rooms · 13. the local
market

*Matters & events*: 14. courage/valor (parakrama) · 15. initiative · 16. willpower ·
17. effort itself · 18. ventures & self-starting · 19. short journeys/commuting ·
20. writing · 21. communication (all channels) · 22. journalism/media · 23. skills
of the hand · 24. musical instruments · 25. crafts · 26. sports · 27. hobbies ·
28. sales/marketing · 29. small contracts · 30. boldness/risk appetite · 31. change
of place (displacement from home base) · 32. siblings' welfare · 33. competitions of
skill · 34. rumors/messages · 35. correspondence · 36. mental restlessness (movement
of mind) · 37. tools/instruments · 38. driving · 39. one's broadcast voice
(blogs/social media) · 40. dance/performance arts · 41. awards for valor ·
42. adventurism · 43. physical-fitness culture · 44. bold transactions (quick trades)

*Body*: 45. right ear · 46. throat/neck · 47. shoulders · 48. arms · 49. hands

**Viruddha relation**: 12th-from-3 = **2nd** — courage starved of cash: ventures die
for want of the vault (C10 viruddha: "initiative starved of cash"). Reverse: 3 is
12th-from-**4** — movement dissolves home/peace: relocation kills the settled
domestic state (M7 asset-moves-away, H5 peace-displaced, H8/F6 viruddha logic).

**Transit (factor A)**:
- **Rahu through the 3rd (from Moon)**: ✅ FAVORABLE (locked). Courage surges,
  rivals retreat, bold/foreign-flavored moves land; appetite for initiative becomes
  hard to stop. Watch only the overreach. From **Lagna**: visible bold plays —
  launches, applications, confrontations won.
- **Ketu through the 3rd**: ✅ FAVORABLE (locked). Courage through detachment;
  effort without anxiety; siblings at a peaceful distance. 
- Axis context: Rahu-in-3rd ⇔ Ketu-in-9th (faith questioned while boldness rises);
  Ketu-in-3rd ⇔ Rahu-in-9th (fortune hunger co-runs).

**Kelvigal pull** — core: C10 (venture birth), F1, F2, F10 · modifier: C1 (+3
consulting & micro-travels — Machan's clause), C3, C5, C9, M4, M9, H3, F5, F8 ·
viruddha-on: M7, H5, H8, R4, F6 (movement dissolves peace/asset/return).

**Worked example (sample chart)**: 3rd house = **Dhanus, holding natal RAHU**
(12°53', Moolam, Ketu-star). A natural malefic in an upachaya → courage that
*compounds with age*; Rahu's flavor: unconventional boldness, foreign-linked
initiative, a sibling/effort story that runs off the standard script. 3rd lord
Jupiter (functional malefic, Thulam) sits in the 11th retrograde → effort converts
into gains through 3/6 channels (competition, service). Vimshottari: the Rahu bhukti
(2028-03-17→2030-08-10) delivers rank-1 the **3rd @100** (SIGN-01 occupancy) —
this natal 3rd is DBAS-lit from March 2028. In the Makaram transit window
(2026-12→2028-06), the transit axis sits 4/10 — the 3rd is NOT pressed by gochara
(transit leg ✗), which is precisely why F1 renders **MIXED**: the pull is real
(DBAS ✓✓ via 3 and 9), the carrying transit is absent inside the window.

---

# 4. FOURTH BHAVA — Sukha · Veedu

**Data**: Classification **kendra (angular)** · Purushartha **MOKSHA** ·
Texture **material + inner peace — the only kendra whose true currency is the
heart's rest** · Body zone **chest / heart / lungs / breasts** ·
Naisargika karakas **Moon (mother/peace), Venus (vehicles/comfort), Mercury
(education)** · Viruddha **3** (movement dissolves peace) · Tamil
**Veedu / Sukha sthanam**

**Texture**: The base. Home, mother, property, vehicles, inner peace, homeland,
formal education — everything that lets a person sit down without bracing. BHAVA-03
gives the 4th its paradox: a kendra (material magnitude — land, houses, cars) tagged
MOKSHA (release/peace). The 4th therefore delivers the *most material* moksha:
assets that hold you, and the peace (or restlessness) that comes with them. The
classical "end of matters" reading lives here too — the 4th is where ventures come
to rest, the final seat.

**Holds**: rootedness · mother's wellbeing · property that appreciates · genuine
contentment · education completed · domestic harmony · the reliable vehicle ·
popularity with the masses
**Corrupts**: restlessness despite comfort · mother-worry · property entanglement ·
education interrupted · the impressive home nobody rests in · emotional hollowness
behind assets

**Karakatvas**:

*People*: 1. mother · 2. maternal figures · 3. family elders at home · 4. the
household · 5. domestic staff · 6. natives of one's homeland · 7. the public/masses
(mundane layer) · 8. tenants of one's property

*Places*: 9. home/dwelling · 10. homeland · 11. farms & fields owned · 12. wells,
ponds & water on one's land · 13. schools (places of formal education) · 14. the
final resting place [classical: 4 = where things end] · 15. ancestral property
sites · 16. the garage/parking (vehicle-as-place)

*Matters & events*: 17. property / real estate · 18. land · 19. vehicles · 20. home
comforts & luxuries · 21. inner peace (sukha) · 22. happiness-contentment ·
23. mother's wellbeing & her fortunes · 24. formal education & degrees completed ·
25. emotional security · 26. domestic environment · 27. fixed assets (the
conversion of money into wealth — M2's logic) · 28. agriculture of one's own land ·
29. household items/furniture · 30. private life · 31. the heart's inclinations ·
32. popularity with the masses · 33. ancestral property · 34. cattle-wealth ·
35. sleep quality · 36. endings of ventures (all things come to rest here) ·
37. the throne/seat (simhasana — classical seat of power) · 38. reputation in the
homeland · 39. moral character · 40. hidden feelings · 41. house purchase/construction
events · 42. relocation of residence · 43. vehicle purchase events · 44. mother-linked
expenditure & care · 45. the homeland pull (return questions — F6 core) · 46. peace
recovery after disturbance

*Body*: 47. chest · 48. heart · 49. lungs · 50. breasts · 51. the emotional heart
(manas-seat by several paramparas)

**Viruddha relation**: 12th-from-4 = **3rd** — peace displaced by restlessness and
movement; assets booked but moved away (M7 viruddha), the return-home postponed
(F6 viruddha), mother's peace disturbed by churn (H8 viruddha). Reverse: 4 is
12th-from-**5** — the settled home postpones conception/speculation: M4 & R6's
viruddha watch.

**Transit (factor A)**:
- **Rahu through the 4th (from Moon)**: domestic churn — property/vehicle matters
  activate, mother's wellbeing asks attention, inner peace runs disturbed even as
  material home matters advance. ⚠ watch (not in locked favorable set); BHAVA-03
  reading mandatory: material push + peace cost, BOTH reported. From **Lagna**:
  visible home events — purchase, renovation, relocation, homeland news.
- **Ketu through the 4th**: home detachment, letting-go of property, relocation
  toward simplicity, mother-distance, peace through renunciation rather than
  acquisition. ⚠ watch.
- Axis context: Rahu-in-4th ⇔ Ketu-in-10th (career cools while home heats — the
  classic relocation/role-change axis); Ketu-in-4th ⇔ Rahu-in-10th (ambition surge
  while home thins).

**Kelvigal pull** — core: M2, M7, H5, H8, R4, F6, F9 · modifier: C6, M1, M8, H1,
H3, H6, H10, R1, R3, R6, R7, R9, F1, F2, F4, F7 · viruddha-on: M4, R6, H10-child
(home stability postpones the 5th's matter).

**Worked example (sample chart — the showcase)**: 4th house = **Makaram, holding
FOUR grahas**: Moon 28°12' (digbala in the 4th) · Venus 22°23' (digbala) ·
Saturn 19°23' (**own sign → Shasha mahapurusha yoga; also yogakaraka**) ·
Mars 16°43' (**exalted → Ruchaka mahapurusha yoga**). Two mahapurusha yogas and
two digbalas in one house — the 4th is this chart's engine room. The 4th lord
Saturn sits IN his own 4th: the landlord lives in his own house — delivery at
maximum strength (SIGN-01/04 both fire). The 10th lord Moon sits here → career
itself is anchored in homeland/property/home-ground. **Transit 2026-12-07**: Rahu
enters Makaram — onto this 4th-house stellium AND onto the Janma Rashi itself
(1st-from-Moon). Retrograde contact order (factor B): **Moon → Venus → Saturn →
Mars** (highest degree first). Factor C: transit Rahu's dispositor = own-sign
Saturn, the chart's strongest graha → Rahu's agitation is housed by a strong
landlord: the amplification lands constructively (property/vehicle/home moves),
with the moksha-tag cost named: inner peace lags while assets move (exactly the
H5 MIXED verdict — "gains land, peace lags").

---

# 5. FIFTH BHAVA — Putra · Santhanam

**Data**: Classification **panaphara** · Special **trikona** · Purushartha
**DHARMA** · Texture **heart/meaning — what one creates and what one merits** ·
Body zone **stomach / upper abdomen / upper back (spine) / womb (conception seat)** ·
Naisargika karaka **Jupiter (children/intelligence)** · Viruddha **4** · Tamil
**Santhana sthanam / Puthira bhavam**

**Texture**: What flows OUT of you by merit: children, intelligence, creativity,
romance, the speculative bet, the mantra, the past-life credit (purva-punya)
cashing in. As trikona it fills the heart; as 5th it is the native's *expression* —
the 1st is who you are, the 5th is what you make of it. Classically also the
mantri-sthana: advisory brilliance, ministerial counsel, political acumen.

**Holds**: creative fertility (children & ideas) · sharp buddhi · devotional depth ·
wise risk · romance with sincerity · past-merit arriving on schedule ·
students/disciples who honor the teacher
**Corrupts**: blocked creativity · speculation become gambling · romance become
entanglement · children-worry · mantra without faith · intelligence serving anxiety

**Karakatvas**:

*People*: 1. children · 2. students/disciples · 3. romantic partner (love affairs) ·
4. creative protégés · 5. devotees/followers · 6. the advisor/minister figure ·
7. gamblers & speculators (as a tribe)

*Places*: 8. colleges & higher-learning halls · 9. temples (devotion) · 10. theatres
& entertainment venues · 11. sports arenas/stadiums · 12. casinos/gambling dens ·
13. stock exchanges · 14. playgrounds · 15. mantra/initiation spaces

*Matters & events*: 16. children & childbirth · 17. conception · 18. intelligence
(buddhi — deep discriminative intellect, vs the 4th's acquired learning) ·
19. higher education · 20. creativity · 21. romance/love affairs · 22. speculation
& gambling · 23. share-market positions · 24. mantra/japa practice & siddhi ·
25. devotion/bhakti · 26. purva-punya (past-life merit) manifesting · 27. advisory
roles / minister-ship · 28. sports performance · 29. games & play · 30. entertainment ·
31. arts/drama/cinema · 32. creative writing · 33. judgment & discrimination power ·
34. dignity & honor · 35. good deeds (punya in action) · 36. teaching · 37. joy &
heart's expression · 38. fame through talent · 39. political acumen (vs the 10th's
power itself) · 40. romance preceding marriage (R2's anchor) · 41. merit through
examination (C4's +5) · 42. regenerative vitality (H1/H6's +5) · 43. the bet placed
and the bet won

*Body*: 44. stomach · 45. upper abdomen · 46. upper back/spine · 47. the womb as
conception seat · 48. digestion-as-appetite (the fire that says yes)

**Viruddha relation**: 12th-from-5 = **4th** — the settled home postpones the bet
and the baby: speculation dissolves into stagnation (M4), conception postponed
(R6). Reverse: 5 is 12th-from-**6** — disease and debt dissolve: the 5th's
activation closes loans (M6's core logic) and lifts illness (H2/H4 viruddha).

**Transit (factor A)**:
- **Rahu through the 5th (from Moon)**: speculative appetite surges, romance
  intensifies, children matters demand attention, mind runs agitated-creative,
  mantra/occult interest wakes. ⚠ watch — appetite without gate discipline is the
  risk. From **Lagna**: visible creative launches, romance events, children's
  milestones.
- **Ketu through the 5th**: detachment from speculation and romance, children
  distance (or unusual spiritual children), past-life creative mastery surfacing
  without hunger. ⚠ watch — gains may quietly drop even as peace rises.
- Axis context: Rahu-in-5th ⇔ Ketu-in-11th (the circle thins while creation
  heats); Ketu-in-5th ⇔ Rahu-in-11th (gains surge while creation detaches).

**Kelvigal pull** — core: M4, M6, H5, R2, R6, H10-child · modifier: C1, C2, C4,
C10, M3, M9, H1, H6, H8, R1, R4, R5-diagnostic, R10-diagnostic, F4, F7, F9 ·
viruddha-on: C3, C4, C5-employment, M5, H2, H4 (the 5th signified = the old job
refuses to let go; disease dissolves; debt dissolves — context decides which face).

**Worked example (sample chart)**: 5th house = **Kumbam, holding the SUN**
(18°42', Sadayam p4, Rahu-star). 5th lord = Saturn, sitting own-sign in the 4th →
the trikona lord is the chart's yogakaraka in a kendra: the 5th's intelligence and
creativity are structurally backed at the highest grade (QUAL-01 texture by
lordship). But the tenant is the Sun — **11th lord, functional malefic for
Thulam** (FUNC-01: the suppression of natural-harsh traits does NOT fire) → the
5th's delivery carries Sun's glare: gains-desire channeled through intellect,
authority-textured creativity, ego-stakes in children/speculation. From the Moon:
the 5th = Vrishabham, empty (quiet emotional-frame 5th). **This transit window**:
the 4/10 axis does not press the 5th, and neither Moon bhukti {4,2,7,10} nor the
gochara touches {5,8,11} → a speculation question (M4) gates **NEGATIVE** in early
2027 — rendered soft per REPORT-01: "speculation paakurathu konjam wait pannunga;
tharunam innum varala." An instructive negative-gate example: the house itself is
strong, but the QUESTION's support legs both fail.

---

# 6. SIXTH BHAVA — Ripu · Roga / Satru

**Data**: Classification **apoklima** · Special **dusthana + upachaya (dual — the
pressure that matures)** · Purushartha **ARTHA** · Texture **the grind that pays** ·
Body zone **navel / intestines / lower abdomen / digestive tract / waist** ·
Naisargika karakas **Mars (enemies/injury), Saturn (disease/debt)** ·
Viruddha **5** · Tamil **Satru sthanam / Roga sthanam**

**Texture**: The arena. Disease, debt, enemies, litigation — and *service, employment,
daily work, victory in competition*. The 6th is the only dusthana that is also an
upachaya: its pressures, met with effort, convert into capacity over time. This is
why a strong 6th makes surgeons, lawyers, soldiers, athletes, and exam-toppers —
people who win in contested spaces. Every negative health/debt question's core lives
here; every employment question's skeleton stands here.

**Holds**: victory over rivals · disease resisted and defeated · disciplined service ·
debts taken and cleared on schedule · litigation won · the daily grind that compounds
**Corrupts**: chronic manageable illness · crushing debt cycles · enemies multiplied ·
litigation quicksand · servitude without dignity · anxiety as background noise

**Karakatvas**:

*People*: 1. enemies & rivals · 2. competitors · 3. creditors/lenders · 4. debtors ·
5. servants/employees (subordinates) · 6. maternal uncle (matula — classical) ·
7. tenants · 8. litigants · 9. thieves · 10. doctors/healers (those who fight disease)
· 11. soldiers/police (those who fight enemies)

*Places*: 12. courts (dispute halls) · 13. hospitals & clinics (treatment zones) ·
14. workplaces of service · 15. battlefields & competitive arenas · 16. police
stations · 17. labor sites/quarries · 18. gyms of discipline

*Matters & events*: 19. disease & illness (roga) · 20. debts & loans · 21. enemies &
hostility · 22. litigation & disputes · 23. service / employment (the daily work) ·
24. labor & hard work · 25. competition itself · 26. obstacles · 27. wounds & minor
acute injuries · 28. theft · 29. anxiety & worry · 30. loans taken · 31. repayment
schedules · 32. divorce proceedings (6 = 12th-from-7: partnership dissolved into
dispute) · 33. quarrels · 34. misunderstandings · 35. legal notices · 36. chronic-
manageable conditions (diabetes-class: lived-with, not fatal) · 37. digestive
disorders · 38. pets & small domestic animals · 39. tenancy/rented arrangements ·
40. daily routine & discipline of service · 41. subordination · 42. sports
competition · 43. victory over enemies (well-supported 6th) · 44. medical & legal
professions · 45. increments through service cycles (M2/M10's +6) · 46. punishment-
transfers & disciplinary events (C8's +12/+6 flavor territory) · 47. the loan-closure
moment (when the 5th dissolves the 6th — M6)

*Body*: 48. navel region · 49. intestines · 50. lower abdomen · 51. digestive organs ·
52. waist

**Viruddha relation**: 12th-from-6 = **5th** — the grind dissolves into play:
debt dissolves (M5's viruddha = the relief signal), disease dissolves (H2/H4),
the old service lets go (C3/C4/C5-employment viruddha: "the old job refuses to
let go" when the 5th over-signifies INSTEAD of the move). Reverse: 6 is
12th-from-**7** — partnership dissolves into litigation/service: the viruddha of
EVERY marriage card (R1/R2/R3/R4/R9/R10), business card (C6, F8), and C5-business.

**Transit (factor A)**:
- **Rahu through the 6th (from Moon)**: ✅ FAVORABLE (locked). Enemies crushed,
  litigation tilts your way, competitive rise, diseases get named and beaten. The
  one caution: new compulsions (overwork, substances) smuggle in through the same
  door. From **Lagna**: visible wins — cases, exams, selections, promotions through
  competition.
- **Ketu through the 6th**: ✅ FAVORABLE (locked). Debts dissolve, enemies lose
  interest, diseases surface-and-release (odd diagnoses that resolve). The classical
  "ripu-sthana ketu" comfort.
- Axis context: Rahu-in-6th ⇔ Ketu-in-12th (expenses quiet while battles are won);
  Ketu-in-6th ⇔ Rahu-in-12th (foreign/expense pull while debts dissolve — the
  emigration-with-closure signature).

**Kelvigal pull** — core: C1, C3, C4, C5-employment, C8, M5, H2, H4, H7, R5, F3,
R10-diagnostic · modifier: M2, M10, F10, H8/H9/H10-affliction texture ·
viruddha-on: C5-business, C6, M6, H10-spouse, R1, R2, R3, R4, R9, R10, F8 — **the
most viruddha-watched bhava in the whole catalog** (partnership's dissolver).

**Worked example (sample chart)**: 6th house = **Meenam, holding MERCURY
debilitated** (4°25', U.Bhadrapada p1, Saturn-star) — rescued via **NBR-01 c2
chain-rescue**: star-lord Saturn = yogakaraka + trikonadhipati, own-sign, AND casts
his 3rd special aspect from Makaram directly onto Mercury. Mercury = **9th & 12th
lord** → functional benefic (trikonadhipati) → **NBR-02 EXCHANGE branch**: one
uyir karakatva of Mercury's portfolio is softly flagged as the exchange cost — and
note the poignancy: the 6th's own person is the *maternal uncle*, squarely inside
Mercury's relations portfolio. Delivery shape: the 6th's matters (service,
employment, disease-resistance, litigation) run EARLY STRUGGLE → LATER ELEVATION,
paid through Saturn's 4th/5th portfolio (property, education, creativity). From the
Moon: Mercury sits 3rd-from-Moon — an upachaya, consistent with the
improves-with-age profile. **This transit window**: the 4/10 axis does not touch
Meenam; the 6th's story runs entirely on the natal/DBAS layer, not gochara.

---

# 7. SEVENTH BHAVA — Kalatra · Kalathiram

**Data**: Classification **kendra (angular)** · Special **maraka** (with 2) ·
Purushartha **KAMA** · Texture **material union — desire made contractual** ·
Body zone **pelvis / uterus-ovaries / bladder / urinary tract** ·
Naisargika karaka **Venus** · Viruddha **6** (partnership dissolves into dispute) ·
Tamil **Kalathira sthanam**

**Texture**: The other. Marriage and spouse, business partnership, contracts, the
marketplace itself — every matter where the native faces a counterparty. As kendra
the 7th delivers real magnitude (the alliance, the deal); as kama house it runs on
desire and its fulfillment. It is also the setting sun — the far shore — which is
why classical texts thread *travel and foreign residence* through it
**[school note: 7 as foreign-residence house — some paramparas hold it, Machan to
rule; our catalog uses 12 for settlement and 7 for offshore partnership]**.
Maraka capacity dormant outside ayus contexts.

**Holds**: a partner who stands · contracts honored · the marketplace that receives
you · diplomacy that closes · desire met without wreckage · public dealings that
build name
**Corrupts**: partnership turned transaction · spouse friction · contracts weaponized ·
open enmity · desire consuming the desirer · dependence marketed as love

**Karakatvas**:

*People*: 1. spouse · 2. business partners · 3. all counterparties · 4. the public
one deals with · 5. open/declared enemies (vs the 12th's hidden ones) · 6. the
other in any contract · 7. sexual partners · 8. clients/customers (the receiving
market) · 9. referees & introducers (C3's +7: "through a partner's/reference's hand")

*Places*: 10. the marketplace · 11. the west (direction of the setting sun) ·
12. partner's/spouse's home · 13. business premises · 14. negotiation tables ·
15. foreign lands as the far shore [school note]

*Matters & events*: 16. marriage (the event) · 17. partnership (business) ·
18. contracts & agreements · 19. trade/commerce · 20. the marketplace itself ·
21. sexual union · 22. marital harmony · 23. spouse's characteristics & condition ·
24. public dealings & diplomacy · 25. negotiations · 26. compromise capacity ·
27. open confrontation · 28. desire fulfillment through another · 29. offshore/
partnership money (Machan's career +7 clause: offshore money, offshore partnership,
partner/wife involvement) · 30. brand-customer interface · 31. daily income through
trade · 32. the alliance that elevates status (R1's +10) · 33. legal union of any
kind · 34. joint ventures · 35. spouse's contribution to career/money (R9's whole
card) · 36. death-inflicting capacity (maraka — ayus contexts only) · 37. the
opponent's case in litigation · 38. break of journey / journeys to far places
[classical layer] · 39. the wedding itself · 40. partnership dissolution events
(when 6/8/12 press here — R5)

*Body*: 41. pelvis · 42. uterus/ovaries · 43. bladder · 44. kidneys/urinary tract ·
45. the generative basin (semen/ova region)

**Viruddha relation**: 12th-from-7 = **6th** — union dissolves into dispute:
marriage becomes litigation, partnership becomes service-under-terms, the deal
becomes the quarrel. This is the most consequential viruddha edge in the catalog
(eleven cards watch it). Reverse: 7 is 12th-from-**8** — the counterparty absorbs
the sudden: windfall diverted to others (M3), others' money stays with others (M8),
the accident's force spent on the opponent not the self (H3/H7), in-law warmth
withdrawn (R7), the second-marriage matter diverted (R8).

**Transit (factor A)**:
- **Rahu through the 7th (from Moon)**: partnership intensity — obsession with the
  other, foreign/unconventional alliances, spouse friction through amplified
  expectation, deals with unusual terms. ⚠ watch. From **Lagna**: visible alliance
  events — engagements, signings, public partnerships, also public disputes.
- **Ketu through the 7th**: partnership detachment — spouse distance, contracts
  quietly ending, disinterest in the marketplace's noise; spiritualized unions
  survive, transactional ones thin. ⚠ watch.
- Axis context: Rahu-in-7th ⇔ Ketu-in-1st (self thins while the other looms);
  Ketu-in-7th ⇔ Rahu-in-1st (self agitates while the other withdraws).

**Kelvigal pull** — core: C5-business, C6, R1, R2, R3, R4, R8, R9, R10, F8,
H10-spouse · modifier: C1, C3, C8, C9, M1, M5, M7, M8, M9, M10, R5, R6, F1, F2,
F3, F9 · viruddha-on: M3, M8, H3, H7, R7, R8 (the 7th absorbing the 8th's matter).

**Worked example (sample chart)**: 7th house = **Mesham, empty**; 7th lord =
**Mars — exalted in the 4th (Ruchaka)**. Empty house → ownership delivery 100%
(SIGN-04); the spouse/partnership portfolio is delivered THROUGH the exalted
landlord sitting in the property house: the partner arrives with substance, status,
and a home-anchor (R1's +4/+10 flavors are structurally pre-loaded). Moon bhukti
chain {4,2,7,10} hits the 7th → the current window genuinely supports the marriage
question (R1 POSITIVE's DBAS leg), and transit Rahu conjuncting natal Mars =
**the 7th lord himself under the transit's hand** (transit leg ✓). Note the 6th's
viruddha watch: the 6th holds only rescued-benefic Mercury → the
dissolve-into-dispute risk is chain-governed and soft. From the Moon: the 7th =
Katakam — **where transit Ketu sits this window** (7th-from-Moon = partnership
detachment texture from the emotional frame): the lagna-frame says alliance
supported, the Moon-frame says detachment co-runs → the report's honest sentence:
"the union forms AND asks for emotional maturity; arumaiyaana tharunam, manasum
thayara irukanum."

---

# 8. EIGHTH BHAVA — Ayus · Aayul / Maranam

**Data**: Classification **apoklima** · Special **dusthana** · Purushartha
**MOKSHA** · Texture **depth & suddenness — what arrives without labor and what
leaves without warning** · Body zone **genitals / excretory organs / the
chronic-disease seat** · Naisargika karaka **Saturn (ayus)** · Viruddha **7** ·
Tamil **Aayul sthanam / Ashtama sthanam**

**Texture**: The deep. Longevity and death's manner, inheritance, insurance, others'
money, sudden events, the occult, research, surgery, chronic illness, scandal and
transformation. The 8th is everything that comes *without your labor* — including
what you never asked for. As 2nd-from-7th it is the spouse's vault = in-laws and
their resources (bhavat-bhavam: R7/M8 anchor here). The moksha tag shows as
*release through depth*: the 8th breaks what must break so something truer can
stand. Negative questions (accidents, disease severity, sudden breaks) core here —
all rendered through REPORT-01.

**Holds**: inheritance received · longevity with depth · research that strikes bedrock ·
occult mastery · others' money arriving clean · sudden elevation after sudden fall ·
the wound that becomes wisdom
**Corrupts**: chronicity · scandal · sudden breaks without recovery · others' money
with strings · fear of the invisible · transformation refused (and so enforced)

**Karakatvas**:

*People*: 1. in-laws (spouse's family — 2nd from 7th) · 2. heirs & beneficiaries ·
3. the departed/ancestors' realm · 4. insurers & their agents · 5. occultists &
mystics · 6. surgeons · 7. researchers & investigators · 8. tax collectors ·
9. morticians & those who serve the threshold

*Places*: 10. cremation grounds · 11. others' vaults/lockers · 12. research
laboratories · 13. mines & the underground · 14. toilets/excretory spaces ·
15. places of secrecy · 16. the operation theatre

*Matters & events*: 17. longevity (ayus) · 18. death & its manner · 19. sudden
events of every kind · 20. inheritance · 21. insurance · 22. others' money ·
23. spouse's wealth · 24. the occult & hidden knowledge · 25. research &
investigation · 26. chronic disease · 27. major accidents · 28. surgery ·
29. scandal & disgrace · 30. humiliation · 31. deep obstacles · 32. sudden breaks
(career/relationship/property) · 33. taxes owed · 34. wills & legacies · 35. pensions ·
36. unearned income · 37. lottery/windfall · 38. mysteries & the hidden surfacing ·
39. depth psychology · 40. trauma · 41. transformation · 42. commissions ·
43. alimony · 44. debts others owe you · 45. esoteric practice (tantra, kundalini) ·
46. poisons & their antidotes · 47. the underground economy · 48. epidemics &
mass-threshold events (mundane layer) · 49. the in-law relationship itself ·
50. the "suddenly cleared after stall" event (F5's +8) · 51. crossing of norms
(R2's +8: the love-marriage resistance flavor) · 52. the money that settles the
loan (M6's +8)

*Body*: 53. genitals · 54. anus/excretory organs · 55. the chronic-disease seat ·
56. the deep interior function of organs

**Viruddha relation**: 12th-from-8 = **7th** — the sudden spent on the other:
windfall diverted to partner/others, inheritance delayed by counterparty claims,
the accident's edge taken by the opponent. Reverse: 8 is 12th-from-**9** — depth
dissolves fortune: father's matter ends, the visa blocked at the desk (F5/H9
viruddha), grace interrupted (F7).

**Transit (factor A)**:
- **Rahu through the 8th (from Moon)**: ⚠ VOLATILE. Sudden events cluster —
  inheritance/insurance matters activate, occult pull strengthens, health scares
  ask for checkups, unknown causes behind symptoms. The volatile band exists for
  this transit. From **Lagna**: visible sudden events — windfalls or abrupt turns,
  public scandal watch (REPORT-01: probabilistic, gavanam).
- **Ketu through the 8th**: ⚠ watch. Occult mastery without appetite, sudden
  insights, chronic issues surfacing for final release, detachment from others'
  money — and from fear itself.
- Axis context: Rahu-in-8th ⇔ Ketu-in-2nd (your vault detaches while others' money
  hunts you); Ketu-in-8th ⇔ Rahu-in-2nd (accumulation hunger while the deep
  releases).

**Kelvigal pull** — core: M3, M4, M5, M8, M9, H1, H3, H4, H7, R5, R7, R8 ·
modifier: C7, C8, M6, H2, R2, F5, H8/H9/H10-affliction texture · viruddha-on:
C5-business, H9, F5, F7 · rotation anchor: **the in-laws' house (2nd from 7th)**.

**Worked example (sample chart)**: 8th house = **Vrishabham, empty**; 8th lord =
**Venus, digbala in the 4th stellium**. An empty 8th with a digbala landlord → the
deep matters (longevity, suddenness, others' money) are governed from the strongest
house in the chart: the native's 8th-house events, when they come, convert into
4th-house form (property inheritance, home insurance, mother's estate). SIGN chain
note: Jupiter (in Venus's star Pooram) delivers the **8th @100** because Venus
owns it and it is empty (SIGN-03/04) → the Jupiter MD era (running till 2030-08)
carries a live windfall/inheritance channel at the *era* level — but the bhukti
layer decides the window, and neither Moon nor Mars nor Rahu bhukti chains touch
the 8th → **M3 windfall dreams stay parked inside this window**, exactly as the
money-domain worked example concludes. From the Moon: the 8th = Simmam, holding
Jupiter R — the era's 8th-from-Moon placement giving sudden-gain texture to gains:
money that arrives after revision, from behind-the-scenes sources.

---

# 9. NINTH BHAVA — Bhagya · Baakiyam / Dharmam

**Data**: Classification **apoklima** · Special **trikona** · Purushartha **DHARMA** ·
Texture **heart/meaning — grace, merit, and the long road** · Body zone
**hips / thighs / femur / sciatic region** · Naisargika karakas **Jupiter
(fortune/dharma), Sun (father)** · Viruddha **8** · Tamil **Baakiya sthanam /
Dharma sthanam**

**Texture**: The grace account. Fortune (bhagya), father, guru, dharma, higher
education, long journeys, foreign lands-as-destiny, merit from past lives arriving
on schedule. Where the 5th is merit *created*, the 9th is merit *received*. As the
trikona of dharma it fills the heart rather than the vault — but its timing magic
(bhagyodaya, the sudden rise of fortune) is the single most-cited life-turn in
practice. The 9th is also the *permission house*: visas, approvals, blessings — the
stamp from above (F5's core).

**Holds**: fortune that arrives on time · father blessed and blessing · gurus who
appear when due · education elevated · journeys that pay · faith that survives
evidence · the door that opens at the last moment
**Corrupts**: fortune deferred without cause · father-wounds · gurus who fail ·
faith become dogma or become nothing · the long journey to nowhere · merit spent
on pride

**Karakatvas**:

*People*: 1. father · 2. gurus & spiritual teachers · 3. elders · 4. preceptors &
mentors · 5. pilgrims · 6. judges (dharma's arbiters) · 7. grandchildren (5th from
5th) · 8. professors & higher teachers · 9. the fortunate (those grace touches)

*Places*: 10. temples & all houses of worship · 11. pilgrimage sites ·
12. universities (higher learning) · 13. courts of law (justice) · 14. foreign
lands (as the long journey's object) · 15. publishing houses of wisdom

*Matters & events*: 16. fortune/luck (bhagya) · 17. dharma & righteousness ·
18. father — his wellbeing & standing · 19. higher education · 20. philosophy ·
21. religion · 22. long journeys · 23. foreign travel as fortune · 24. the guru's
grace · 25. merit (punya) received · 26. charity & donations · 27. law & justice ·
28. blessings of elders · 29. divine grace · 30. past-life credit cashing ·
31. worship & rituals · 32. sacred learning (vedas, sastras) · 33. ethics ·
34. bhagyodaya — the sudden rise of fortune · 35. grandchildren's matters ·
36. pilgrimages · 37. higher courts · 38. publishing of wisdom · 39. faith itself ·
40. initiation/diksha · 41. the teacher-student bond · 42. visas & approvals (the
permission from above — F5 core) · 43. dharmic timing of marriage (R1/R3's +9) ·
44. recognition from authority (C2's +9) · 45. the fortunate inflow (M1's +9) ·
46. second fortune (R8's +9)

*Body*: 47. hips · 48. thighs · 49. femur · 50. the sciatic line

**Viruddha relation**: 12th-from-9 = **8th** — grace interrupted by the sudden:
fortune blocked at the desk (F5), father's matter entering its depth (H9),
pilgrimage turned ordeal (F7). Reverse: 9 is 12th-from-**10th** — position vacated:
the career's dissolver — promotion denied becomes transfer (C2 viruddha), position
vacated (C7's 9th leg), authority trouble ending in exit (C8). **The 9th is thus
simultaneously the grace house and the career's viruddha — context decides which
face: in career questions the 9th over-signified = the role dissolves into a
journey; in travel/fortune questions the 9th IS the core.**

**Transit (factor A)**:
- **Rahu through the 9th (from Moon)**: fortune churn — ideology shifts, guru/father
  themes activate (sometimes as questioning), long journeys call, foreign destiny
  knocks. ⚠ watch — not in the locked favorable set; the churn is real but the
  direction needs DBAS confirmation. From **Lagna**: visible long journeys, role
  changes via authority shifts, public statements of belief.
- **Ketu through the 9th**: faith restructuring, guru separation or spiritualization,
  pilgrimage accomplished (F7's karaka is Ketu himself), past-life dharma
  surfacing. ⚠ watch on father/fortune texture; ✓-leaning for moksha travel.
- Axis context: Rahu-in-9th ⇔ Ketu-in-3rd (boldness detaches while fortune hunts);
  Ketu-in-9th ⇔ Rahu-in-3rd (courage surges while faith is questioned — the
  sample chart's NATAL axis, see below).

**Kelvigal pull** — core: H9, R3, F1, F4, F5, F7, C7 (9 = position-vacated leg) ·
modifier: C1, C2, C4, C9, C10, M1, M2, M3, M4, M6, M7, M8, M10, H1, H4, H5, H6,
R1, R4, R6, R7, R8, F2, F6, F8, F9, F10 — **the widest modifier footprint of any
bhava: fortune flavors nearly every question** · viruddha-on: C2, C8 (career
dissolution watch).

**Worked example (sample chart)**: 9th house = **Mithunam, holding natal KETU**
(12°53', Ardra p2, Rahu-star) — and natal Rahu sits in the 3rd in Moolam, a Ketu
star: **the nodes tenant each other's nakshatras**, coupling the whole 3/9
effort↔grace axis (commentary-level note; engine uses the standard chain). Ketu in
the 9th: father/guru/dharma themes carry the "already-done" past-life texture —
faith that doesn't argue, fortune that arrives quietly and oddly. From the Moon:
Ketu sits **6th-from-Moon** — Ketu's favorable seat (✓) in the emotional frame:
the grace-house runs on detachment and wins its battles quietly. The 9th lord
Mercury sits debilitated-rescued in the 6th (NBR-01 c2): the fortune landlord is
the struggle→elevation story itself — dharma delivered through service. **This
transit window**: the gochara axis sits 4/10 — the natal 9th is NOT pressed
(transit leg ✗ on the 9th leg too); but from 2028-03 the Rahu bhukti delivers the
**9th @100** (rank-2: Rahu's star-lord Ketu occupies the 9th) → the foreign/
fortune channel is DBAS-lit from March 2028 while gochara stays silent — the
F1 MIXED verdict's exact anatomy, house by house.

---

# 10. TENTH BHAVA — Karma · Thozhil / Virthi

**Data**: Classification **kendra (angular — the strongest kendra)** · Special
**upachaya** · Purushartha **ARTHA** · Texture **material/status in its purest
form — the peak of the visible world** · Body zone **knees / spine-posture /
joints** · Naisargika karakas **Sun (authority), Mercury (trade), Jupiter
(counsel), Saturn (labor) — the four karma karakas** · Viruddha **9** (position
vacated into journey) · Tamil **Thozhil sthanam / Karma sthanam**

**Texture**: The summit. Profession, position, authority, public reputation — what
the native DOES in the world and the rank the world returns. As kendra + artha +
upachaya, the 10th is the most material house in the chart and one that improves
with effort over time: careers compound. The 10th answers "what are you *for*,
publicly?" — and it is the first core of the career domain (Machan's seed: 2 pays,
6 employs, 10 positions).

**Holds**: position with authority · promotions that stick · reputation earned in
public · government favor · the career compounding · responsibility carried as honor
**Corrupts**: title without power (or power without title) · public falls · authority
conflicts · the career eating the person · visibility become exposure · work that
pays and means nothing

**Karakatvas**:

*People*: 1. employer/boss · 2. authority figures · 3. government & the State ·
4. superiors · 5. professionals one reports to · 6. administrators · 7. the public
as witness (the audience of one's work)

*Places*: 8. offices & workplaces · 9. seats of power (secretariats, boardrooms) ·
10. government buildings · 11. courts of administration · 12. the public square ·
13. the institution one serves

*Matters & events*: 14. profession/career · 15. status & position · 16. authority ·
17. rank & title · 18. promotions · 19. karma — deeds in the world · 20. public
reputation · 21. honors & awards · 22. government favor (and wrath) ·
23. administration & governance · 24. business-as-institution · 25. employer
relations · 26. fame · 27. leadership posts · 28. the responsibility load ·
29. visibility · 30. the peak of one's world · 31. career change events ·
32. authority's grace · 33. commerce at scale · 34. politics of position ·
35. discipline of role · 36. pensionable service · 37. legacy-in-career ·
38. the promotion event itself (C2's core) · 39. the new seat (C3's core) ·
40. the brand's standing (C6's +10) · 41. work-linked travel (C9/F1's +10) ·
42. employment-linked liability (M5's +10) · 43. authority stamping the approval
(F5's +10) · 44. the workplace as accident/setting modifier (H3's +10) ·
45. career continuing after return (F6's +10)

*Body*: 46. knees · 47. spine/posture · 48. joints · 49. the skeletal frame's
load-bearing line

**Viruddha relation**: 12th-from-10 = **9th** — position vacated: the role dissolves
into a journey, transfer, or a dharmic exit (C2/C8 viruddha; C7's 9th leg). **Note
the double edge**: the 9th is grace in fortune questions and dissolver in career
questions — GATE-01 reads it per the question asked, never globally. Reverse: 10 is
12th-from-**11th** — position consumed by gains: gains absorbed into maintaining the
role; the 11th's matter (the wish fulfilled) dissolving into status upkeep — the
engine's watch when 10 over-signifies in pure-gains questions.

**Transit (factor A)**:
- **Rahu through the 10th (from Moon)**: ✅ FAVORABLE (locked). Ambition surge,
  unconventional rise, visibility, political/administrative gains; the native
  becomes hard to ignore. Watch only the shortcuts Rahu offers. From **Lagna**:
  the most visible career transit — promotions, public appointments, role
  elevation others can name.
- **Ketu through the 10th**: ⚠ watch (not in Ketu's locked favorable set). Career
  detachment/restructuring — renunciation of status, sudden role change, the title
  losing its hold; superb for work that is service-shaped, disorienting for
  ambition-shaped plans.
- Axis context: Rahu-in-10th ⇔ Ketu-in-4th (home thins while career peaks);
  Ketu-in-10th ⇔ Rahu-in-4th (home/property heats while career detaches — the
  sample chart's live transit, see below).

**Kelvigal pull** — core: C1, C2, C3, C4, C5 (both branches), C8, C9, C10, F3, R9 ·
modifier: C6, M1, M2, M7, M10, H3, H7, H8, H9, R1, R3, R5, R7, F1, F2, F5, F6,
F8, F10 — **the densest core+modifier footprint in the catalog alongside the 2nd** ·
viruddha-on: none in the 50 cards (no question's dissolver is the 10th).

**Worked example (sample chart)**: 10th house = **Katakam, empty natally**; 10th
lord = **Moon, sitting in the 4th stellium with digbala**. Empty 10th → the Moon
delivers career matters at 100% ownership strength (SIGN-04), from inside the
chart's engine room: career is delivered THROUGH property/homeland/home-ground
channels — the native's profession keeps landing her back at base. **Transit
2026-12-07**: Ketu enters **Katakam = the 10th house itself** (axis 4/10 from
lagna). No natal graha there — Ketu tenants the empty seat: career-restructuring
texture per the transit line above. Factor C note: transit Ketu's dispositor is
the **Moon** — who is simultaneously the FIRST natal graha transit Rahu contacts
in Makaram (retrograde order Moon → Venus → Saturn → Mars). The landlord of the
transiting career-detacher is under Rahu's amplification → the career house runs
Ketu-cool on the seat while its landlord runs Rahu-hot in the 4th: the exact
"home heats, career cools, yet the career's owner is the one being amplified"
signature behind C2's POSITIVE verdict (Ketu transits her 10th = the transit leg
✓; the verdict's positive color comes from the Moon-bhukti DBAS chain carrying
the 10th @100).

---

# 11. ELEVENTH BHAVA — Labha · Laabam

**Data**: Classification **panaphara** · Special **upachaya** · Purushartha
**KAMA** · Texture **gains arriving — the harvest, the wish granted** ·
Body zone **calves / shins / ankles / left ear** · Naisargika karaka **Jupiter** ·
Viruddha **10** (gains consumed by status upkeep) · Tamil **Laaba sthanam**

**Texture**: The arrival hall. Gains, income, profits, fulfilled desires, achieved
ambitions, the network that delivers them — elder siblings, friends, circles,
patrons. Every question that ends in "...and do I actually GET it?" resolves here:
promotion (C2) is 10+11, marriage (R1) is 7+2+11, windfall (M3) is 8+11. The 11th
is the event's *landing*. As upachaya it improves with time, and classical texts
note its peculiar neutrality: malefics in the 11th still give gains (through harsher
channels); benefics give gains with grace. As **6th-from-6th**, the 11th is also
the disease's own growth turned to the native's favor — the recovery house (H6).

**Holds**: desires fulfilled · income streams multiplying · friends who deliver ·
the circle that opens doors · wishes completing on schedule · recovery energy ·
the harvest arriving
**Corrupts**: greed without ceiling · networks become extraction · gains that never
land (always almost) · elder-sibling friction · wishes granted at wrong cost ·
the harvest rotting ungathered

**Karakatvas**:

*People*: 1. elder siblings · 2. friends · 3. networks & circles · 4. patrons &
benefactors · 5. the community · 6. groups & associations · 7. well-wishers who
act · 8. the electorate (mundane: those who vote you in)

*Places*: 9. clubs & associations · 10. assembly halls · 11. parliaments ·
12. gatherings & conferences · 13. social venues · 14. the marketplace's winning
side

*Matters & events*: 15. gains & income · 16. profits · 17. desire fulfillment ·
18. ambitions achieved · 19. cash flow ARRIVING (vs 2nd = held) · 20. all incoming
streams · 21. friendship itself · 22. networking · 23. social capital · 24. awards
& recognitions · 25. bonuses · 26. windfalls realized (the 8th's promise landing) ·
27. speculation profits BOOKED (M4's +2/+11 distinction: paper vs booked) ·
28. the promotion's pay effect (C2) · 29. elections won · 30. popularity ·
31. wishes granted · 32. group memberships · 33. the harvest of effort ·
34. celebrations · 35. fulfillment of vows · 36. recovery from illness (the
6th-from-6th turn — H6's core) · 37. selection cleared (C4's +11) · 38. better pay
than current (C3's +11) · 39. the trip achieving its purpose (F1's +11) ·
40. admission secured (F4's +11) · 41. the supportive circle (H5's +11) ·
42. joint gains with spouse (R9's +11) · 43. the second desire (R8's 11th leg —
second-marriage debate flagged for Machan) · 44. income scale jumps (F3's +11)

*Body*: 45. calves · 46. shins & ankles · 47. left ear

**Viruddha relation**: 12th-from-11 = **10th** — gains absorbed by the role: the
wish fulfilled into status upkeep; income consumed by position costs. (Held lightly
in the current catalog — no card's primary viruddha lands on 10.) Reverse: 11 is
12th-from-**12th** — the drain plugs itself: expenditure stops, the foreign stay
ends (return), the loss closes (M9/F2/F3/F4 viruddha; C9's viruddha: "foreign
stay cut short").

**Transit (factor A)**:
- **Rahu through the 11th (from Moon)**: ✅ FAVORABLE (locked — the best node
  transit of the twelve). Gains surge, desires fulfill, networks expand, foreign
  income opens, elections/selections tilt your way. From **Lagna**: visible
  windfalls, promotions-with-pay, public recognitions.
- **Ketu through the 11th**: ✅ FAVORABLE (locked). Gains filtered to essentials,
  the circle shrinks to the true, desires quietly complete without hunger —
  contentment's transit.
- Axis context: Rahu-in-11th ⇔ Ketu-in-5th (creation detaches while harvest
  pours); Ketu-in-11th ⇔ Rahu-in-5th (the bet heats while the circle thins).

**Kelvigal pull** — core: M1, M2, M3, M4, M6, M10, C2, C6, R1, R6, R8, H6, F5 ·
modifier: C1, C3, C4, C9, C10, M7, M8, H1, H4, H5, R2, R3, R4, R9, F1, F3, F4,
F6, F7, F8, F10 · viruddha-on: C9, M9, F2, F3, F4 (the 11th ending the 12th's
matter) · rotation anchor: **elder sibling**.

**Worked example (sample chart)**: 11th house = **Simmam, holding JUPITER R**
(15°40', Pooram p1, vargottama, Venus-star). Jupiter = **3rd & 6th lord =
functional malefic for Thulam** — yet placed in an upachaya: the gains arrive, but
through 3/6 channels — competition, service, effort, contested spaces. Retrograde:
gains loop back, arrive after revision, repeat in cycles; **vargottama** = the
substance is NOT weakened by the retrogression. Jupiter is the running **MD lord
till 2030-08-10** → the entire transit window sits inside the gains-era. MD chain:
**11 @100** (occupancy) · **4 @100** (star-lord Venus occupies) · **1 & 8 @100**
(Venus owns, both empty) · **3 & 6 @30** (owns, both tenanted — SIGN-04). From the
Moon: Jupiter sits **8th-from-Moon** — the emotional frame gives the era a
sudden/others'-money undertone: gains that come from behind the curtain, after
someone else's move. **This transit window**: the 4/10 axis does not press the
11th; the 11th's delivery runs entirely on the MD layer — era-supportive for
gains, window-neutral. (The M1 worked verdict's exact reading: income rises via
the REGULAR channel (2), not the windfall/network channel (11) — the bhukti layer
outranks the era layer inside the window.)

---

# 12. TWELFTH BHAVA — Vyaya · Virayam / Moksham

**Data**: Classification **apoklima** · Special **dusthana** · Purushartha
**MOKSHA** · Texture **release & dissolution — expenditure, distance, and the
final letting-go** · Body zone **feet / left eye / sleep** · Naisargika karakas
**Saturn (loss/isolation), Ketu (moksha)** · Viruddha **11** (the drain plugs
itself) · Tamil **Viraya sthanam / Moksha sthanam**

**Texture**: The far shore and the open hand. Expenditure and loss, foreign lands
and settlement, hospitals and ashrams, isolation and liberation, sleep and dreams,
bed pleasures and charity. The 12th is where things LEAVE — money, energy, the
body, the homeland, the world. Parambariya honesty: the 12th is not "bad" — it is
*cost and transcendence fused*; the same house that drains the vault builds the
soul. This is why foreign-settlement questions core here (F2/F3/F4), why
hospitalization watches here, and why moksha questions (F7) end here.

**Holds**: expenditure that buys what matters · foreign doors opening · hospitals
entered and exited well · deep sleep & true dreams · charity with grace ·
renunciation chosen (not imposed) · the quiet room where one hears
**Corrupts**: losses without purchase · exile instead of travel · isolation become
loneliness · sleep broken · hidden leaks everywhere · escapism marketed as
spirituality

**Karakatvas**:

*People*: 1. foreigners · 2. hospital staff (inpatient world) · 3. institutional
staff (jails, asylums, monasteries) · 4. monks & renunciates · 5. spies & hidden
actors · 6. hidden enemies (vs the 7th's declared ones) · 7. the departed ·
8. those who receive your charity

*Places*: 9. foreign countries · 10. hospitals (inpatient) · 11. ashrams &
monasteries · 12. jails & detention · 13. isolation wards · 14. the bedroom (bed
pleasures) · 15. distant islands · 16. the unseen world (moksha realms) ·
17. airports/border crossings (the leaving places)

*Matters & events*: 18. expenditure & loss · 19. foreign residence · 20. emigration ·
21. moksha/liberation · 22. isolation · 23. hospitalization · 24. imprisonment ·
25. bed pleasures & sexual privacy · 26. sleep · 27. dreams · 28. charity given ·
29. donation outflows · 30. spiritual retreat · 31. self-undoing · 32. hidden
expenses & leaks · 33. endings of every kind · 34. the final departure (with the
8th — death as release) · 35. exile · 36. waste · 37. investments (money going out
to work) · 38. taxes & dues paid · 39. the last leg of pilgrimages · 40. samadhi &
meditative absorption · 41. seclusion · 42. invisible help (support from unseen
hands) · 43. the distant source of money (M3's +12) · 44. change of workplace to a
distant land (C3's +12) · 45. exit to foreign pause (C7's +12) · 46. transfer-as-
punishment (C8's +12) · 47. the partner from a different culture (R2's +12) ·
48. spouse's foreign-linked earnings (R9's +12) · 49. recurring hospitalization
(H7's +12) · 50. the foreign family relocation (F9's core leg)

*Body*: 51. feet · 52. left eye · 53. sleep (as the body's 12th-house function) ·
54. the lymphatic/eliminative flow

**Viruddha relation**: 12th-from-12 = **11th** — the drain plugs itself: expenses
stop, the loss closes, the foreign stay ends in return-with-gain (M9/F2/F3/F4
viruddha — the "stay cut short" and "channel closes" watch). Reverse: 12 is
12th-from-**1st** — release dissolves the self: the body drains, identity enters
isolation (H1/H6 viruddha — hospitalization/weakness watch).

**Transit (factor A)**:
- **Rahu through the 12th (from Moon)**: ⚠ watch — with a domain carve-out.
  Foreign pull intensifies, expenses rise, isolation themes, sleep/disturbance,
  hospital/institutional contacts; BUT for foreign-settlement questions the 12th
  IS core (GATE-01 per-question reads it positive when supported). From **Lagna**:
  visible relocation, foreign postings, institutional events.
- **Ketu through the 12th**: ⚠ watch on the general axis, ✓-leaning for moksha:
  the classical "Ketu in the 12th excels for liberation" — spiritual residence,
  ashram stays, expenses redirected to the sacred. Not in the locked favorable
  set → the flag stays "watch," the domain lens may override.
- Axis context: Rahu-in-12th ⇔ Ketu-in-6th (debts/enemies dissolve while the
  foreign pull calls — the emigration-with-closure signature); Ketu-in-12th ⇔
  Rahu-in-6th (battles won while the inner world calls).

**Kelvigal pull** — core: C9, M9, F1, F2, F3, F4, F7, F8, F9, R5, H1-viruddha
side, H6-viruddha side · modifier: C3, C7, C8, M3, M5, H2, H3, H4, H7, R2, R9 ·
viruddha-on: H1, H6 (the body-drain watch) · **the foreign domain's anchor house.**

*(No natal occupancy in the sample chart's 12th — Kanni, empty, lord Mercury
rescued in the 6th: the chart's expenditure/foreign channel is governed by the
struggle→elevation Mercury; foreign-settlement questions therefore read the 12th
lord's chain (Mercury → Saturn's 4/5 portfolio) — settlement, when supported,
delivers through property and education channels.)*

---
---

## Status & open items

- **All 12 bhavas filed as DRAFT.** Every karakatva, classification tag, transit
  texture, and kelvigal mapping awaits Machan's line-by-line practice corrections —
  cite by bhava + number (e.g., "8th #23").
- **Worked examples filed for the 7 loaded bhavas** (3, 4, 5, 6, 9, 10, 11);
  bhavas 1, 2, 7, 8, 12 carry compact chart notes instead (empty houses read
  through their lords).
- ⛔ **[school note] queue for Machan**: 3rd as mild dusthana · 2nd's
  second-marriage-family reading (R8 dependency) · 7th as foreign-residence house ·
  10th as father in day-charts (we hold 9 = father per kelvigal) · maraka reading
  scope (ayus-only, per this file).
- ⛔ **Cuspal / KP bhava-chalit** deferred to v2 with the sub-lord gate (80/20 lock);
  this file is whole-sign only.
- **Kelvigal pull sections are computed from the 50 cards of kelvigal.md as of
  2026-10-31**; if Machan's corrections change any card's bhava set, the reverse
  index here MUST be regenerated (engine does this at build time; the file's lists
  are the human-readable mirror).

---

## Sample-chart bhava-load maps (reference for all worked examples)

**From Lagna (Thulam) — primary event frame:**

| Bhava | Rasi | Occupants | Lord | Lord sits |
|---|---|---|---|---|
| 1 | Thulam | — | Venus | 4th (digbala) |
| 2 | Vrichikam | — | Mars | 4th (exalted, Ruchaka) |
| 3 | Dhanus | **Rahu** | Jupiter | 11th (R) |
| 4 | Makaram | **Moon · Venus · Saturn · Mars** | Saturn | 4th (own, Shasha; yogakaraka) |
| 5 | Kumbam | **Sun** | Saturn | 4th (own) |
| 6 | Meenam | **Mercury** (debilitated, NBR-01 c2 rescued) | Jupiter | 11th (R) |
| 7 | Mesham | — | Mars | 4th (exalted) |
| 8 | Vrishabham | — | Venus | 4th (digbala) |
| 9 | Mithunam | **Ketu** | Mercury | 6th (debilitated-rescued) |
| 10 | Katakam | — | Moon | 4th (digbala) |
| 11 | Simmam | **Jupiter R** (vargottama) | Sun | 5th |
| 12 | Kanni | — | Mercury | 6th |

**From Moon (Makaram = Janma Rashi) — primary experiential frame:**

| From Moon | Rasi | Occupants |
|---|---|---|
| 1st | Makaram | Moon · Venus · Saturn · Mars |
| 2nd | Kumbam | Sun |
| 3rd | Meenam | Mercury |
| 6th | Mithunam | Ketu |
| 8th | Simmam | Jupiter R |
| 12th | Dhanus | Rahu |
| others | — | empty |

**Live transit (from 2026-12-07, mean node)**: Rahu → Makaram = **4th from Lagna /
1st from Moon** · Ketu → Katakam = **10th from Lagna / 7th from Moon** ·
axis = **4/10 (home ↔ world)** · retrograde contact order onto the stellium:
**Moon 28°12' → Venus 22°23' → Saturn 19°23' → Mars 16°43'**.

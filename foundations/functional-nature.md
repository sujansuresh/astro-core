# FUNCTIONAL-NATURE.md — Graha Lordship Behavior by Lagna (FUNC-01), Encyclopedic

---

## GLOSSARY — Rule ID prefixes used in this file

> Master table: `rule-engine/RULES.md` → GLOSSARY. Only the prefixes used in this file are listed below.

| Prefix | விரிவாக்கம் | எதைக் குறிக்கிறது? |
|---|---|---|
| SIGN | Signification | கிரகங்கள் எதைக் குறிக்கின்றன, எந்தப் பாவங்களை வழங்குகின்றன |
| GATE | Question Gate | கேள்விக்குரிய பாவங்கள் மற்றும் பலன் தீர்மானம் |
| FUNC | Functional Nature | லக்ன அடிப்படையிலான சுபர் / பாவர் தன்மை |
| NBR | Neecha Bhanga Resolution | நீசபங்கம் மற்றும் அதன் விளைவுகள் |
| REPORT | Report Generation | அறிக்கை உருவாக்கும் விதிகள் |

---

> **source**: classical base (BPHS / Laghu Parashari / Phaladeepika functional-benefic
> doctrine) + Machan's practice corrections
> **status**: DRAFT — awaiting Machan's line-by-line practice corrections
> **consumed-by**: FUNC-01 (the rule card this file implements), GATE-01 (the DBAS leg
> only counts houses *well-delivered* — functional nature colors the delivery), SIGN-01..05
> (a functional malefic's 30% lordship leg hits harder), domain lenses (e.g., R2's
> "+11 route" only when the 11th lord is functionally clean), report tone-stitcher
> **standard**: encyclopedic, ultra-deep, general-purpose, chart-agnostic. The matrix is
> computed ONCE from the derivation rules; any future module (natal, prasna, matching,
> muhurta) reads the same table. Worked example (Thulam) is illustrative only.
> **sibling files**: grahas.md (natural nature — this file is *lordship* nature),
> rasis.md (rasi lordship source data; this file resolves its deferred
> friend/enemy directionality disputes), RULES.md (FUNC-01 card)

---

## Part 0 — The distinction this file exists for

**Natural nature** (grahas.md): what a graha IS — Sun is sattvic-authority, Saturn is
tamasic-labor, everywhere, in every chart.

**Functional nature** (this file): what a graha DOES *for a given lagna* — decided purely
by **which houses it owns from that lagna**. The same Saturn who is a natural malefic
becomes the finest yogakaraka for Thulam and Vrishabham lagnas; the same Jupiter who is
the greatest natural benefic turns functional malefic for Thulam.

FUNC-01's engine-facing clause (locked in RULES.md): *"a functional benefic's natural
malefic traits are suppressed; the converse suppression does NOT hold — a functional
malefic retains his natural harshness and aims it through his lordship."* This file
supplies the classification; grahas.md supplies the traits being suppressed or retained.

---

## Part 1 — The derivation rules (the arithmetic, in fixed evaluation order)

The matrix below is not lore to memorize — it is **computed**. Rules F-1..F-8, applied in
this order; first rule that fires decides (later rules only modulate):

- **F-1 — Yogakaraka**: if a graha owns a **kendra (1/4/7/10) AND a trikona (1/5/9)**
  simultaneously → **Yogakaraka** (super-benefic). Possible only for: Mars (Kataka,
  Simha), Venus (Makara, Kumbha), Saturn (Thula, Vrishabha). Nothing else qualifies.
- **F-2 — Trikonadhipati (1/5/9 lord)**: lordship of a trikona makes the graha
  functionally **benefic**, regardless of natural nature — *including the lagna lord,
  who is ALWAYS benefic for his own lagna* (1 = kendra + trikona dual).
- **F-3 — Kendradhipati dosha (benefics)**: natural benefics (Jupiter, Venus, Mercury,
  bright Moon) owning **only kendras** acquire functional neutrality-toward-malefic for
  *action* — they stop giving freely and start demanding. Rendered: **neutral** (M-leaning
  when the kendra is 7th = maraka-loaded).
- **F-4 — Kendra lordship (malefics)**: natural malefics (Sun, Mars, Saturn, dark Moon)
  owning **only kendras** shed their edge for delivery purposes → **neutral** (B-leaning
  when the kendra is the 10th).
- **F-5 — Trishadaya lords (3/6/11)**: ownership of 3, 6, or 11 → functionally **malefic**
  (growth-houses reward pressure; their lords deliver through competition and cost).
- **F-6 — Ashtamadhipati (8th lord)**: functionally **malefic** — EXCEPT: **Sun and Moon
  carry no ashtama dosha** (classical exemption; they stay neutral), and when the 8th lord
  also owns a trikona or the lagna, F-2/F-1 has already fired.
- **F-7 — Maraka lords (2/7)**: neutral for delivery; the maraka edge is **dormant data**,
  read ONLY in ayus/longevity contexts (mirrors bhavas.md's maraka scope note).
- **F-8 — Dual lordship mixing**: when a graha owns two houses pointing different ways,
  the **moolatrikona house's signification weighs heavier** (standard BPHS weighting).
  Documented pair by pair in the lagna sections below. Net malefic + benefic mixes render
  as **mixed** (lean named).

**Encoding used in the matrix**: `YK` = yogakaraka · `B` = functional benefic ·
`N` = neutral (lean in brackets) · `M` = functional malefic · `X` = mixed.

**Nodes**: Rahu/Ketu are NOT in the matrix — they own no houses. Their functional color is
borrowed per contact: (a) the dispositor of the sign they tenant, (b) the graha they
conjoin, (c) the graha aspecting them — in that priority (classical; KP agrees). The
engine resolves this at the contact layer (factor B), never from a static row.

---

## Part 2 — The master matrix (12 lagnas × 7 house-owning grahas; nodes resolve by proxy)

| Lagna | Sun | Moon | Mars | Mercury | Jupiter | Venus | Saturn |
|---|---|---|---|---|---|---|---|
| **Mesha** | B (5) | N[B] (4) | N[B] (1,8) | M (3,6) | B (9,12) | M (2,7) | M (10,11) |
| **Vrishabha** | N (4) | M (3) | M (7,12) | B (2,5) | M (8,11) | N[B] (1,6) | **YK** (9,10) |
| **Mithuna** | M (3) | N (2) | M (6,11) | B (1,4) | N[M] (7,10) | B (5,12) | B (8,9) |
| **Kataka** | N (2) | B (1) | **YK** (5,10) | M (3,12) | B (6,9) | M (4,11) | M (7,8) |
| **Simha** | B (1) | N (12) | **YK** (4,9) | M (2,11) | B (5,8) | M (3,10) | M (6,7) |
| **Kanni** | N (12) | M (11) | M (3,8) | B (1,10) | N[M] (4,7) | B (2,9) | B (5,6) |
| **Thula** | M (11) | N[B] (10) | M (2,7) | B (9,12) | M (3,6) | N[B] (1,8) | **YK** (4,5) |
| **Vrischika** | N[B] (10) | B (9) | N[B] (1,6) | M (8,11) | B (2,5) | M (7,12) | M (3,4) |
| **Dhanus** | B (9) | N (8) | B (5,12) | N[M] (7,10) | B (1,4) | M (6,11) | M (2,3) |
| **Makara** | N (8) | N[M] (7) | M (4,11) | B (6,9) | M (3,12) | **YK** (5,10) | N[B] (1,2) |
| **Kumbha** | N (7) | M (6) | M (3,10) | B (5,8) | M (2,11) | **YK** (4,9) | N[B] (1,12) |
| **Meena** | M (6) | B (5) | B (2,9) | N[M] (4,7) | B (1,10) | M (3,8) | M (11,12) |

*(Graha columns carry the houses owned in brackets. Rahu/Ketu: no row — see Part 1.)*

**Spot-check the symmetries**: the six yogakaraka cells sit exactly where F-1 allows them;
Mesha↔Vrischika and Simha↔Kumbha etc. mirror across the zodiac because lordship flips but
kendra/trikona geometry doesn't. The full per-lagna derivations follow in Part 3.

---

## Part 3 — Per-lagna derivations (every cell shown, rule cited)

### Mesha
- **Sun** lords **5** → F-2 trikona → **B**. (Natural malefic + trikona lordship: authority delivered as merit/creativity.)
- **Moon** lords **4** → F-3 kendra-benefic dosha, softened by Moon's sattva → **N[B]**.
- **Mars** lords **1,8** → F-2 via lagna lordship (always benefic); 8th co-ownership taints → **N[B]** (lagna lord absorbs the ashtama edge — the classic "own-8th lagna lord" case).
- **Mercury** lords **3,6** → F-5 (both trishadaya) → **M**. The sharpest Mercury of the wheel.
- **Jupiter** lords **9,12** → F-2 via moolatrikona 9th (Dhanus) outweighs 12th → **B**.
- **Venus** lords **2,7** → F-7 dual maraka + kendra-benefic dosha → **M** (maraka edge dormant outside ayus; the *delivery* turns grasping).
- **Saturn** lords **10,11** → F-5 via 11th (moolatrikona Kumbha = 11th) outweighs F-4's kendra-softening → **M**. Career gains through grind.

### Vrishabha
- **Sun** lords **4** → F-4 malefic-kendra → **N**.
- **Moon** lords **3** → F-5 → **M**.
- **Mars** lords **7,12** → F-7 maraka + 12th → **M**.
- **Mercury** lords **2,5** → F-2 via moolatrikona 5th (Kanni) → **B**. Wealth through intellect; a money-grade Mercury.
- **Jupiter** lords **8,11** → F-6 + F-5 (moolatrikona Dhanus = 8th) → **M**. The heaviest Jupiter of the wheel.
- **Venus** lords **1,6** → lagna lord always B (F-2); 6th co-ownership taints → **N[B]**.
- **Saturn** lords **9,10** → F-1 kendra+trikona → **YK**. The strongest yogakaraka pairing of the wheel (fortune + career fused).

### Mithuna
- **Sun** lords **3** → F-5 → **M**.
- **Moon** lords **2** → F-7 → **N** (maraka dormant).
- **Mars** lords **6,11** → F-5 ×2 → **M**. The sharpest Mars of the wheel.
- **Mercury** lords **1,4** → lagna lord (F-2) + kendra → **B**.
- **Jupiter** lords **7,10** → F-3 full kendradhipati dosha (both kendras, 7 = maraka-loaded) → **N[M]**.
- **Venus** lords **5,12** → F-2 via moolatrikona 5th (Thula) → **B**.
- **Saturn** lords **8,9** → F-2 via moolatrikona 9th (Kumbha) outweighs F-6 → **B**. The famous "8+9 Saturn = fortune through depth" case.

### Kataka
- **Sun** lords **2** → F-7 → **N** (maraka dormant).
- **Moon** lords **1** → lagna lord → **B**.
- **Mars** lords **5,10** → F-1 → **YK** (trikona + strongest kendra). The gentlest power-Mars.
- **Mercury** lords **3,12** → F-5 (3) + loss → **M**.
- **Jupiter** lords **6,9** → F-2 via moolatrikona 9th (Dhanus) outweighs F-5 → **B** (with a service-flavored delivery).
- **Venus** lords **4,11** → F-3 kendra dosha + F-5 (11) → **M**.
- **Saturn** lords **7,8** → F-7 + F-6 (moolatrikona Kumbha = 8th) → **M**. Partnership matters carry depth-cost.

### Simha
- **Sun** lords **1** → lagna lord → **B**.
- **Moon** lords **12** → loss-lord, no dosha (Moon exempt from 8th only; 12th is not exempted) → **N** (expense-textured).
- **Mars** lords **4,9** → F-1 → **YK** (kendra + trikona). Property-fortune fused.
- **Mercury** lords **2,11** → F-5 via moolatrikona 11th (Kanni) outweighs F-7 → **M**. Gains-through-pressure Mercury.
- **Jupiter** lords **5,8** → F-2 via moolatrikona 5th (Dhanus) outweighs F-6 → **B**.
- **Venus** lords **3,10** → F-5 (3) + kendra dosha → **M**.
- **Saturn** lords **6,7** → F-5 (6) + F-7 (7, moolatrikona Kumbha = 7th) → **M**.

### Kanni
- **Sun** lords **12** → loss-lord → **N**.
- **Moon** lords **11** → F-5 → **M**.
- **Mars** lords **3,8** → F-5 + F-6 (moolatrikona Mesha = 8th... wait: Mars moolatrikona is Mesha — for Kanni lagna, Mesha = 8th) → **M**. The heaviest Mars.
- **Mercury** lords **1,10** → lagna lord + strongest kendra → **B**.
- **Jupiter** lords **4,7** → F-3 kendradhipati (7 = maraka-loaded) → **N[M]**.
- **Venus** lords **2,9** → F-2 via moolatrikona 9th (Thula) → **B**. Fortune-grade Venus.
- **Saturn** lords **5,6** → F-2 via moolatrikona 5th (Kumbha... Saturn MT = Kumbha — for Kanni, Kumbha = 6th!) — *correction of the naive read*: Saturn's moolatrikona Kumbha falls in the **6th**, so the trishadaya outweighs the trikona → **B[M-leaning]**: still benefic-flavored by 5th lordship, but delivers through effort/health/service. **[school note: some paramparas grade this Saturn full-B via 5th lordship; Machan to rule — matrix holds B with M-lean]**.

### Thula (the sample chart's lagna — full worked panel in Part 5)
- **Sun** lords **11** → F-5 → **M**. The network/desire lord with teeth (R2's "+11 route" is *not* open here).
- **Moon** lords **10** → F-3 softened (bright benefic, strongest kendra) → **N[B]**. Career delivered with heart.
- **Mars** lords **2,7** → F-7 dual maraka → **M** (dormant outside ayus; delivery = grasping-protection of vault & partner).
- **Mercury** lords **9,12** → F-2 via moolatrikona 9th (Mithuna) outweighs 12th → **B**. The dharma-Mercury (sample chart: debilitated + rescued — see Part 5).
- **Jupiter** lords **3,6** → F-5 ×2 → **M**. The gains-through-contest Jupiter (sample chart: 11th occupant).
- **Venus** lords **1,8** → lagna lord (F-2); 8th co-ownership taints → **N[B]**.
- **Saturn** lords **4,5** → F-1 → **YK** (home + merit fused — sample chart: own-sign in the 4th = the engine room).

### Vrischika
- **Sun** lords **10** → F-4 malefic + strongest kendra → **N[B]**. Authority softened into service of position.
- **Moon** lords **9** → F-2 → **B**. The fortune-Moon.
- **Mars** lords **1,6** → lagna lord (F-2); 6th co-ownership taints → **N[B]**.
- **Mercury** lords **8,11** → F-6 + F-5 (moolatrikona Kanni = 11th) → **M**.
- **Jupiter** lords **2,5** → F-2 via moolatrikona 5th (Dhanus... Jupiter MT = Dhanus — for Vrischika, Dhanus = 2nd) → F-7/2nd weighs, but trikona lordship of the 5th (Meena) still rules → **B** (vault-of-merit Jupiter).
- **Venus** lords **7,12** → F-7 + loss → **M**.
- **Saturn** lords **3,4** → F-5 (3) outweighs kendra-softening (moolatrikona Kumbha = 4th; F-4 applies to malefics: 4th-lordship softens) → **X[M-lean]** — matrix renders M; the 4th co-lordship keeps a domestic-delivery channel open.

### Dhanus
- **Sun** lords **9** → F-2 → **B**. Fortune-authority fused (the classic dharma-Sun).
- **Moon** lords **8** → **F-6 exemption applies** (Moon carries no ashtama dosha) → **N**. **[school note: some paramparas still grade M; Machan to rule — matrix holds N]**.
- **Mars** lords **5,12** → F-2 via moolatrikona 5th (Mesha) → **B**.
- **Mercury** lords **7,10** → F-3 kendradhipati (7 = maraka-loaded) → **N[M]**.
- **Jupiter** lords **1,4** → lagna lord + kendra → **B**.
- **Venus** lords **6,11** → F-5 ×2 → **M**.
- **Saturn** lords **2,3** → F-7 + F-5 (moolatrikona Kumbha = 3rd) → **M**.

### Makara
- **Sun** lords **8** → **F-6 exemption applies** (Sun carries no ashtama dosha) → **N**.
- **Moon** lords **7** → F-3 + F-7 (maraka kendra) → **N[M]**.
- **Mars** lords **4,11** → F-5 (11, moolatrikona Mesha = 4th — kendra softens via F-4) → **X[M-lean]** — matrix renders M; property-delivery stays open.
- **Mercury** lords **6,9** → F-2 via moolatrikona 9th (Kanni) outweighs F-5 → **B** (fortune through service/health channels).
- **Jupiter** lords **3,12** → F-5 + loss → **M**.
- **Venus** lords **5,10** → F-1 → **YK** (merit + career fused).
- **Saturn** lords **1,2** → lagna lord (F-2) + vault → **N[B]**. The self-made-vault Saturn.

### Kumbha
- **Sun** lords **7** → F-4/F-7 (maraka kendra, malefic) → **N**.
- **Moon** lords **6** → F-5 → **M**.
- **Mars** lords **3,10** → F-5 (3) + F-4 (10 softens; moolatrikona Mesha = 3rd) → **M** (career through pressure).
- **Mercury** lords **5,8** → F-2 via moolatrikona 5th (Kanni... Mercury MT = Kanni — for Kumbha, Kanni = 8th!) — 8th weighs; trikona 5th (Mithuna) still rules per F-2 → **B[M-lean]** — matrix renders B; the 8th co-lordship gives this Mercury a research/depth streak.
- **Jupiter** lords **2,11** → F-7 + F-5 (moolatrikona Dhanus = 2nd) → **M** (the two money houses under one malefic-flavored lord — money through grind).
- **Venus** lords **4,9** → F-1 → **YK** (home + fortune fused).
- **Saturn** lords **1,12** → lagna lord (F-2); 12th co-ownership taints → **N[B]**.

### Meena
- **Sun** lords **6** → F-5 → **M**.
- **Moon** lords **5** → F-2 → **B**. The creative-merit Moon.
- **Mars** lords **2,9** → F-2 via 9th (Vrischika... Mars MT = Mesha = 2nd; 9th co-lordship) → **B** (vault + fortune — the dhana-yoga Mars).
- **Mercury** lords **4,7** → F-3 kendradhipati (7 = maraka-loaded) → **N[M]**.
- **Jupiter** lords **1,10** → lagna lord + strongest kendra → **B**.
- **Venus** lords **3,8** → F-5 + F-6 (moolatrikona Thula = 8th) → **M**. The heaviest Venus.
- **Saturn** lords **11,12** → F-5 + loss (moolatrikona Kumbha = 12th) → **M**.

---

## Part 4 — Natural friendship/enmity with DIRECTION (resolves rasis.md's deferral)

Naisargika (natural, permanent) relationship — **read row → column** ("row's view of
column"). This matrix is chart-agnostic; the matrix above is lagna-specific. Engine uses
BOTH: functional nature colors *delivery*; natural relation colors *flavor* (factor C's
dispositor texture, contact comfort in factor B).

| view ↓ of → | Sun | Moon | Mars | Mercury | Jupiter | Venus | Saturn |
|---|---|---|---|---|---|---|---|
| **Sun** | — | F | F | N | F | E | E |
| **Moon** | F | — | N | F | N | N | N |
| **Mars** | F | F | — | E | F | N | N |
| **Mercury** | F | **E** | N | — | N | F | N |
| **Jupiter** | F | F | F | E | — | **E** | N |
| **Venus** | E | E | N | F | N | — | F |
| **Saturn** | E | E | **E** | F | N | F | — |

(F = friend · N = neutral · E = enemy. Moon has NO enemies — the only graha so graded.)

**The four asymmetric pairs (the actual disputes rasis.md parked — now resolved):**

1. **Mercury → Moon = E, but Moon → Mercury = F.** The mind resents the emotion that
   floods it; the emotion trusts the mind that names it. *Engine use*: a tenant Mercury in
   a Moon sign delivers with internal friction (the graha is uncomfortable); a tenant Moon
   in a Mercury sign is *comfortable being there* even though Mercury dislikes hosting
   (reception ≠ tenancy comfort). Sample chart: **Moon tenants NO Mercury sign; Mercury
   tenants Meenam (Jupiter) — not this pair.** But factor C: transit Ketu's dispositor =
   Moon, and Moon's star hosts Venus (4th stellium) — Moon→Venus = N, no friction flag.
2. **Saturn → Mars = E, but Mars → Saturn = N.** Labor resents the knife; the knife
   doesn't mind the grind. *Engine use*: Saturn-starred or Saturn-signed Mars transits
   read harsher than Mars-signed Saturn ones. Sample chart: **Mars tenants Makaram
   (Saturn's sign)** — Mars→Saturn = N: the exalted tenant is comfortable; and Saturn
   hosting exalted Mars is the friction direction (Saturn→Mars = E) → the 4th-stellium
   note "the landlord endures the tenant's heat" (texture-only, delivery unaffected —
   Ruchaka + Shasha both stand).
3. **Jupiter → Venus = E, but Venus → Jupiter = N.** The preceptor of the devas disowns
   the preceptor of the asuras; the asura-guru harbors no equivalent grudge. Sample chart:
   **Jupiter tenants Pooram (Venus star)** — Jupiter→Venus = E: the MD lord delivers the
   11th/4th through a star-lord he resents → gains arrive with a taste of compromise
   (flavor clause for the era, not a downgrade).
4. **Sun → Mercury = N, but Mercury → Sun = F.** The king tolerates the prince-scribe;
   the scribe thrives in the king's court. (Budha-Aditya yoga's comfort is Mercury's, not
   the Sun's — flavor note for that yoga wherever it forms.)

**Engine rule (directionality)**: factor C reads **dispositor → tenant** for the
*landlord's willingness*, and **tenant → dispositor** for the *tenant's comfort*. Two
separate flavor clauses; never collapse to one score.

**Tatkalika (temporary) friendship** — grahas 2/3/4/10/11/12 from each other in the
*chart* become temporary friends; combined panchadha score = v2 (deferred; v1 uses
naisargika only, flagged in the factor-C notes).

---

## Part 5 — Worked example: the sample chart's full functional panel (Thulam lagna)

| Graha | Owns | Verdict | Placement | What the verdict DOES there |
|---|---|---|---|---|
| Sun | 11 | **M** | 5th, Kumbam | FUNC-01 converse clause: suppression does NOT fire — 11th-lord gains-desire enters the merit house with ego-glare; speculation/children carry "must win" stakes (bhavas.md 5th example; M4's NEGATIVE-gate flavor source) |
| Moon | 10 | **N[B]** | 4th, digbala | Career delivered with heart, through home/property; current bhukti lord — her delivery is soft-landed (digbala + stellium support) |
| Mars | 2,7 | **M** (maraka dormant) | 4th, exalted (Ruchaka) | Grasping-protection of vault & partner converts into property at thagudhi grade; maraka data never read in money/marriage questions |
| Mercury | 9,12 | **B** | 6th, debilitated, NBR-01 c2 rescued | Dharma-Mercury through service: fortune delivered via the arena; NBR-02 exchange cost flagged (maternal-uncle channel, 6th's own person) |
| Jupiter | 3,6 | **M** | 11th, R, vargottama | Gains arrive through competition/service; MD-era lord — the era's gains carry contest texture (flavor: earned, not gifted) |
| Venus | 1,8 | **N[B]** | 4th, digbala | Self + depth delivered through the engine room; the 8th co-lordship gives the 4th's assets an inheritance channel (M8's quiet support) |
| Saturn | 4,5 | **YK** | 4th, own sign (Shasha) | Home + merit fused at maximum dignity: the chart's strongest graha AND the transit-dispositor (below) |
| Rahu | — | proxy | 3rd, Dhanus | Dispositor Jupiter = **M** (3/6 lords) + tenant of Jupiter's sign + Ketu-star: courage amplified through contest channels; DBAS leg from 2028-03 |
| Ketu | — | proxy | 9th, Mithunam | Dispositor Mercury = **B** (9/12 lords): grace delivered quietly, through the rescued dharma-Mercury — fortune that arrives after someone else's struggle resolves |

**Live-transit cross-read (factor C, 2026-12-07 onward)**: transit Rahu enters Makaram →
dispositor = **Saturn, the YK, own-sign, Shasha** — the strongest possible landlord
(dignity rank 1 of 6). Transit Ketu enters Katakam → dispositor = **Moon, N[B], digbala,
10th lord** — a soft benefic landlord who is herself the first graha transit Rahu
retrogrades onto. The functional panel is what turns "Rahu onto the 4th stellium" from
a generic churn warning into the specific verdict: **amplification housed by the
yogakaraka → constructive material surge (property/home/career-base), with the moksha-tag
cost named (peace lags)** — the H5 MIXED verdict, derived cell by cell.

**Report-facing clause (REPORT-01)**: functional verdicts never surface as jargon
("Jupiter is your 3/6 lord functional malefic") — they surface as texture ("gains come
through competition; the win is earned, not gifted"). The matrix feeds reasons; the
template bank feeds sentences.

---

## Status & open items

- **Matrix + derivations filed as DRAFT.** Machan to correct cell by cell
  ("Kanni Saturn", "Dhanus Moon").
- ⛔ **[school note] queue**: Kanni Saturn B vs B[M-lean] (moolatrikona Kumbha = 6th
  weighting) · Dhanus Moon N (ashtama exemption) vs M (parampara variant) ·
  Vrischika/Makara Saturn & Mars mixed-cell rendering (matrix holds the lean).
- **Nodes carry no row by design** — proxy resolution (dispositor → conjunction → aspect)
  happens at the contact layer; documented in Part 1 and exercised in Part 5.
- **Tatkalika/panchadha friendship deferred to v2** (v1 = naisargika only).
- **Cross-file consistency**: this file resolves rasis.md's footer-flagged enmity
  directionality items; grahas.md's FUNC-01 references now have their lookup table;
  bhavas.md's per-lagna lord readings cite these cells.
